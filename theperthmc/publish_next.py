#!/usr/bin/env python3
"""Publish the next draft blog post from the queue.

Run from the theperthmc/ directory.
Updates: {slug}.html, blog.html, drafts/queue.json, sitemap.xml
"""

import json
import os
import re
import sys
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DRAFTS_DIR = os.path.join(BASE_DIR, "drafts")
QUEUE_FILE = os.path.join(DRAFTS_DIR, "queue.json")
BLOG_HTML = os.path.join(BASE_DIR, "blog.html")
SITEMAP_XML = os.path.join(BASE_DIR, "sitemap.xml")

with open(QUEUE_FILE, encoding="utf-8") as f:
    data = json.load(f)

queue = data.get("queue", [])
if not queue:
    print("Queue is empty — nothing to publish.")
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

with open(src, encoding="utf-8") as f:
    content = f.read()

pub_date = datetime.now().strftime("%Y-%m-%d")
canonical_url = f"https://perthmc.com/{slug}.html"

# 1. Fix noindex → index, follow
content = content.replace(
    'content="noindex, nofollow"',
    'content="index, follow"'
)
content = content.replace(
    "content='noindex, nofollow'",
    "content='index, follow'"
)

# 2. Add canonical tag if missing
if 'rel="canonical"' not in content:
    canonical_tag = f'  <link rel="canonical" href="{canonical_url}" />\n'
    content = content.replace(
        '  <meta name="viewport"',
        canonical_tag + '  <meta name="viewport"'
    )

# 3. Add OG + Twitter tags if missing
if 'og:title' not in content:
    # Extract description from meta tag
    desc_match = re.search(r'<meta name="description" content="([^"]+)"', content)
    description = desc_match.group(1) if desc_match else excerpt
    og_tags = (
        f'  <meta property="og:title" content="{title}" />\n'
        f'  <meta property="og:description" content="{description}" />\n'
        f'  <meta property="og:url" content="{canonical_url}" />\n'
        f'  <meta property="og:type" content="article" />\n'
        f'  <meta property="og:site_name" content="Perth MC" />\n'
        f'  <meta name="twitter:card" content="summary" />\n'
        f'  <meta name="twitter:title" content="{title}" />\n'
        f'  <meta name="twitter:description" content="{description}" />\n'
    )
    content = content.replace(
        '  <link rel="preconnect"',
        og_tags + '  <link rel="preconnect"'
    )

# 4. Add Article JSON-LD if missing
if 'application/ld+json' not in content:
    schema = (
        '<script type="application/ld+json">\n'
        '{"@context":"https://schema.org","@type":"Article",'
        f'"headline":"{title}",'
        f'"description":"{excerpt}",'
        f'"url":"{canonical_url}",'
        f'"datePublished":"{pub_date}",'
        f'"dateModified":"{pub_date}",'
        '"author":{"@type":"Organization","name":"Perth MC","url":"https://perthmc.com"},'
        '"publisher":{"@type":"Organization","name":"Perth MC","url":"https://perthmc.com"},'
        f'"mainEntityOfPage":{{"@type":"WebPage","@id":"{canonical_url}"}}}}\n'
        '</script>\n'
    )
    content = content.replace('</head>', schema + '</head>')
else:
    # Fix datePublished to actual publish date (not the hardcoded draft date)
    content = re.sub(
        r'"datePublished"\s*:\s*"[^"]*"',
        f'"datePublished":"{pub_date}"',
        content
    )
    content = re.sub(
        r'"dateModified"\s*:\s*"[^"]*"',
        f'"dateModified":"{pub_date}"',
        content
    )
    # Fix url in schema if it has draft path
    content = re.sub(
        r'"url"\s*:\s*"https://perthmc\.com/[^"]*"',
        f'"url":"{canonical_url}"',
        content
    )

# 5. Fix ../  paths (drafts/ relative → root relative)
content = content.replace('href="../css/', 'href="css/')
content = content.replace('src="../js/', 'src="js/')
content = content.replace('href="../index.html"', 'href="index.html"')
content = content.replace('href="../services.html"', 'href="services.html"')
content = content.replace('href="../about.html"', 'href="about.html"')
content = content.replace('href="../blog.html"', 'href="blog.html"')
content = content.replace('href="../contact.html"', 'href="contact.html"')
# Fix back-to-blog link in article body
content = content.replace('href="../blog.html"', 'href="blog.html"')

# 6. Replace simplified draft nav with full nav (including Events dropdown)
FULL_NAV = '''    <nav class="main-nav" id="main-nav">
      <a href="index.html">Home</a>
      <a href="services.html">Services</a>
      <div class="dropdown">
        <button class="dropdown-btn">Events &#9660;</button>
        <div class="dropdown-menu">
          <a href="wedding-mc-perth.html">Wedding MC Perth</a>
          <a href="corporate-mc-perth.html">Corporate MC Perth</a>
          <a href="conference-mc-perth.html">Conference MC Perth</a>
          <a href="charity-gala-mc-perth.html">Charity Gala MC</a>
          <a href="awards-night-mc-perth.html">Awards Night MC</a>
          <a href="mc-50th-birthday-perth.html">50th Birthday MC</a>
          <a href="school-formal-mc-perth.html">School Formal MC</a>
          <a href="christmas-party-mc-perth.html">Christmas Party MC</a>
          <a href="product-launch-mc-perth.html">Product Launch MC</a>
          <a href="black-tie-event-mc-perth.html">Black Tie Event MC</a>
        </div>
      </div>
      <a href="about.html">About</a>
      <a href="blog.html" class="active">Blog</a>
      <a href="contact.html" class="btn btn-primary">Check Availability</a>
    </nav>
    <div class="header-right">
      <a href="contact.html" class="header-cta-link">Check Availability</a>
      <button class="hamburger" id="hamburger" aria-label="Open menu" aria-expanded="false">&#9776;</button>
    </div>'''

# Replace simple nav (without dropdown) if present
simple_nav_pattern = re.compile(
    r'<nav class="main-nav"[^>]*>.*?</nav>\s*<div class="header-right">.*?</div>',
    re.DOTALL
)
if simple_nav_pattern.search(content):
    content = simple_nav_pattern.sub(FULL_NAV, content, count=1)

with open(dst, "w", encoding="utf-8") as f:
    f.write(content)
print(f"Published: {slug}.html")

# Update blog.html
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

with open(BLOG_HTML, encoding="utf-8") as f:
    blog = f.read()

marker = '<div class="blog-grid">'
if marker not in blog:
    print("ERROR: Could not find blog grid marker in blog.html")
    sys.exit(1)

blog = blog.replace(marker, marker + new_card, 1)
with open(BLOG_HTML, "w", encoding="utf-8") as f:
    f.write(blog)
print("Updated: blog.html")

# Update sitemap.xml (guard against duplicates)
new_url = f'  <url><loc>https://perthmc.com/{slug}.html</loc><lastmod>{pub_date}</lastmod><changefreq>monthly</changefreq><priority>0.7</priority></url>\n'

with open(SITEMAP_XML, encoding="utf-8") as f:
    sitemap = f.read()

if f"{slug}.html" not in sitemap:
    sitemap = sitemap.replace("</urlset>", new_url + "</urlset>")
    with open(SITEMAP_XML, "w", encoding="utf-8") as f:
        f.write(sitemap)
    print("Updated: sitemap.xml")
else:
    print(f"Sitemap already contains {slug}.html — skipped.")

# Remove from queue
queue.pop(0)
data["queue"] = queue
with open(QUEUE_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
    f.write("\n")

remaining = len(queue)
print(f"Removed from queue. {remaining} post{'s' if remaining != 1 else ''} remaining.")
print(f"PUBLISHED_SLUG={slug}")
print(f"PUBLISHED_TITLE={title}")
