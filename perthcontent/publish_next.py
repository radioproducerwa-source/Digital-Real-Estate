#!/usr/bin/env python3
"""Publish the next draft blog post from the queue.

Adapted for Perth Content.
Run from any directory — uses absolute paths.
Updates: {slug}.html, blog.html, drafts/queue.json, sitemap.xml
"""

import json
import shutil
import os
import sys
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DRAFTS_DIR = os.path.join(BASE_DIR, "drafts")
QUEUE_FILE = os.path.join(DRAFTS_DIR, "queue.json")
BLOG_HTML = os.path.join(BASE_DIR, "blog.html")
SITEMAP_XML = os.path.join(BASE_DIR, "sitemap.xml")

with open(QUEUE_FILE) as f:
    data = json.load(f)

queue = data.get("queue", [])
if not queue:
    print("Queue is empty — nothing to publish this week.")
    sys.exit(0)

post = queue[0]
slug = post["slug"]
title = post["title"]
tag = post["tag"]
read_time = post["read_time"]
excerpt = post["excerpt"]

src = os.path.join(DRAFTS_DIR, f"{slug}.html")
dst = os.path.join(BASE_DIR, f"{slug}.html")

if not os.path.exists(src):
    print(f"ERROR: Draft file not found: {src}")
    sys.exit(1)

shutil.copy2(src, dst)
print(f"Published: {slug}.html")

pub_month = datetime.now().strftime("%B %Y")
new_card = (
    f'\n      <div class="blog-card"><div class="blog-card-body">'
    f'<span class="blog-tag">{tag}</span>'
    f'<div class="blog-meta">{pub_month} &nbsp;&middot;&nbsp; {read_time} min read</div>'
    f'<h2><a href="{slug}.html">{title}</a></h2>'
    f'<p>{excerpt}</p>'
    f'<a href="{slug}.html" class="blog-read-more">Read more &rarr;</a>'
    f'</div></div>\n'
)

with open(BLOG_HTML) as f:
    blog = f.read()

marker = '<div class="blog-grid">'
if marker not in blog:
    print("ERROR: Could not find blog grid marker in blog.html")
    sys.exit(1)

blog = blog.replace(marker, marker + new_card, 1)
with open(BLOG_HTML, "w") as f:
    f.write(blog)
print("Updated: blog.html")

new_url = f'  <url><loc>https://perthcontent.com/{slug}.html</loc><changefreq>monthly</changefreq><priority>0.7</priority></url>\n'

with open(SITEMAP_XML) as f:
    sitemap = f.read()

sitemap = sitemap.replace("</urlset>", new_url + "</urlset>")
with open(SITEMAP_XML, "w") as f:
    f.write(sitemap)
print("Updated: sitemap.xml")

queue.pop(0)
data["queue"] = queue
with open(QUEUE_FILE, "w") as f:
    json.dump(data, f, indent=2)

remaining = len(queue)
print(f"Removed from queue. {remaining} post{'s' if remaining != 1 else ''} remaining.")
print(f"PUBLISHED_SLUG={slug}")
print(f"PUBLISHED_TITLE={title}")
