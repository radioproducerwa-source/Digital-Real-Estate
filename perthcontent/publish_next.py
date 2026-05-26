#!/usr/bin/env python3
"""publish_next.py — Perth Content
Publishes the next draft blog post from drafts/queue.json.

Steps:
1. Reads drafts/queue.json — takes the first item in "queue"
2. Copies drafts/{slug}.html → {slug}.html (site root)
3. Prepends a new card to blog.html's .blog-grid div
4. Appends a <url> entry to sitemap.xml
5. Removes the published item from the queue
6. Prints PUBLISHED_SLUG= and PUBLISHED_TITLE= for GitHub Actions

Run from the perthcontent/ directory (or any directory — uses absolute paths).
"""

import json
import shutil
import os
import sys
from datetime import datetime

BASE_DIR   = os.path.dirname(os.path.abspath(__file__))
DRAFTS_DIR = os.path.join(BASE_DIR, "drafts")
QUEUE_FILE = os.path.join(DRAFTS_DIR, "queue.json")
BLOG_HTML  = os.path.join(BASE_DIR, "blog.html")
SITEMAP    = os.path.join(BASE_DIR, "sitemap.xml")

# ── Read queue ──────────────────────────────────────────────────────────────
with open(QUEUE_FILE, encoding="utf-8") as f:
    data = json.load(f)

queue = data.get("queue", [])
if not queue:
    print("Queue is empty — nothing to publish.")
    sys.exit(0)

post      = queue[0]
slug      = post["slug"]
title     = post["title"]
tag       = post["tag"]
read_time = post["read_time"]
excerpt   = post["excerpt"]

# ── Check draft file exists ──────────────────────────────────────────────────
src = os.path.join(DRAFTS_DIR, f"{slug}.html")
dst = os.path.join(BASE_DIR,   f"{slug}.html")

if not os.path.exists(src):
    print(f"ERROR: Draft not found: {src}")
    print("Generate drafts first with: python3 generate_blogs.py --drafts")
    sys.exit(1)

# ── Copy draft to site root ──────────────────────────────────────────────────
shutil.copy2(src, dst)
print(f"Published: {slug}.html")

# ── Inject card into blog.html ───────────────────────────────────────────────
pub_month = datetime.now().strftime("%B %Y")
new_card = (
    f'\n      <div class="blog-card">'
    f'<div class="blog-card-body">'
    f'<div class="blog-cat">{tag}</div>'
    f'<div class="blog-meta">{pub_month} &nbsp;&middot;&nbsp; {read_time} min read</div>'
    f'<h3><a href="{slug}.html">{title}</a></h3>'
    f'<p>{excerpt}</p>'
    f'<a href="{slug}.html" class="read-more">Read more &rarr;</a>'
    f'</div></div>\n'
)

with open(BLOG_HTML, encoding="utf-8") as f:
    blog = f.read()

marker = '<div class="blog-grid">'
if marker in blog:
    blog = blog.replace(marker, marker + new_card, 1)
    with open(BLOG_HTML, "w", encoding="utf-8") as f:
        f.write(blog)
    print(f"Added card to blog.html")
else:
    print("WARNING: Could not find .blog-grid in blog.html — card not added")

# ── Append to sitemap.xml ────────────────────────────────────────────────────
sitemap_entry = (
    f"  <url><loc>https://perthcontent.com/{slug}.html</loc>"
    f"<changefreq>monthly</changefreq><priority>0.6</priority></url>\n"
)

with open(SITEMAP, encoding="utf-8") as f:
    sitemap = f.read()

if f"{slug}.html" not in sitemap:
    sitemap = sitemap.replace("</urlset>", sitemap_entry + "</urlset>")
    with open(SITEMAP, "w", encoding="utf-8") as f:
        f.write(sitemap)
    print(f"Added {slug}.html to sitemap.xml")

# ── Remove from queue ────────────────────────────────────────────────────────
data["queue"] = queue[1:]
with open(QUEUE_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"Removed from queue. Remaining: {len(data['queue'])} posts")

# ── Output for GitHub Actions ────────────────────────────────────────────────
print(f"PUBLISHED_SLUG={slug}")
print(f"PUBLISHED_TITLE={title}")
