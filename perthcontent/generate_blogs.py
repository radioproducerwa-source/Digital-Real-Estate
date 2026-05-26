#!/usr/bin/env python3
"""
generate_blogs.py — Perth Content
Generates blog post HTML files from a list of post definitions.
Run from the perthcontent/ directory.

Usage:
    python3 generate_blogs.py              # generates all posts in POSTS list
    python3 generate_blogs.py --drafts     # writes to drafts/ folder instead
"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DRAFTS_DIR = os.path.join(BASE_DIR, "drafts")
WRITE_TO_DRAFTS = "--drafts" in sys.argv

SITE_URL = "https://perthcontent.com"
SITE_NAME = "Perth Content"
FORMSPREE_ID = "mzdodayb"

HEADER_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="{meta}" />
  <meta name="robots" content="index, follow" />
  <title>{title} | {site_name}</title>
  <link rel="canonical" href="{site_url}/{slug}.html" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{meta}" />
  <meta property="og:url" content="{site_url}/{slug}.html" />
  <meta property="og:type" content="article" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="css/style.css" />
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "{title}",
    "description": "{meta}",
    "datePublished": "{date}",
    "author": {{"@type": "Organization", "name": "{site_name}"}},
    "publisher": {{"@type": "Organization", "name": "{site_name}", "url": "{site_url}"}}
  }}
  </script>
</head>
<body>

<header class="site-header">
  <div class="container header-inner">
    <a href="index.html" class="logo">Perth<span>Content</span></a>
    <nav class="main-nav" id="main-nav">
      <a href="index.html">Home</a>
      <div class="dropdown">
        <button class="dropdown-btn">Services &#9660;</button>
        <div class="dropdown-menu">
          <a href="corporate-video-perth.html">Corporate Video</a>
          <a href="real-estate-video-perth.html">Real Estate Video</a>
          <a href="social-media-video-perth.html">Social Media Video</a>
          <a href="instagram-reels-editing-perth.html">Instagram Reels</a>
          <a href="youtube-video-editing-perth.html">YouTube Editing</a>
          <a href="event-highlight-video-perth.html">Event Highlights</a>
          <a href="explainer-video-perth.html">Explainer Video</a>
          <a href="training-video-perth.html">Training Video</a>
          <a href="drone-video-editing-perth.html">Drone Video</a>
          <a href="restaurant-hospitality-video-perth.html">Restaurant &amp; Hospitality</a>
          <a href="wedding-videography-perth.html">Wedding Video</a>
          <a href="product-video-perth.html">Product Video</a>
          <a href="promotional-video-perth.html">Promotional Video</a>
          <a href="linkedin-video-perth.html">LinkedIn Video</a>
          <a href="startup-video-perth.html">Startup Video</a>
          <a href="tiktok-video-editing-perth.html">TikTok Editing</a>
          <a href="conference-seminar-video-perth.html">Conference &amp; Seminar</a>
          <a href="fitness-wellness-video-perth.html">Fitness &amp; Wellness</a>
          <a href="testimonial-video-perth.html">Testimonial Video</a>
          <a href="annual-report-video-perth.html">Annual Report Video</a>
        </div>
      </div>
      <a href="about.html">About</a>
      <a href="portfolio.html">Portfolio</a>
      <a href="blog.html" class="active">Blog</a>
      <a href="contact.html" class="btn btn-primary">Get a Quote</a>
    </nav>
    <div class="header-right">
      <button class="hamburger" id="hamburger" aria-label="Open menu" aria-expanded="false">&#9776;</button>
    </div>
  </div>
</header>

<section class="page-hero">
  <div class="container">
    <div class="breadcrumb">
      <a href="index.html">Home</a> &rsaquo; <a href="blog.html">Blog</a> &rsaquo; {tag}
    </div>
    <h1>{title}</h1>
    <p>{excerpt}</p>
  </div>
</section>

<section class="blog-post">
  <div class="container blog-post-layout">
    <article class="blog-post-content">
      <div class="post-meta">
        <span>&#128197; {date_display}</span>
        <span>&#127991; {tag}</span>
        <span>&#9200; {read_time} min read</span>
      </div>
'''

FOOTER_TEMPLATE = '''
    </article>

    <aside class="post-sidebar">
      <div class="post-sidebar-card">
        <h4>Get a Free Quote</h4>
        <form action="https://formspree.io/f/{formspree_id}" method="POST"
              data-formspree data-success-id="{slug}-sidebar-success">
          <div class="form-row">
            <div>
              <label for="{slug}-sb-name">Name</label>
              <input id="{slug}-sb-name" type="text" name="name" placeholder="Your name" required />
            </div>
            <div>
              <label for="{slug}-sb-email">Email</label>
              <input id="{slug}-sb-email" type="email" name="email" placeholder="Your email" required />
            </div>
            <div>
              <label for="{slug}-sb-svc">Service</label>
              <select id="{slug}-sb-svc" name="service">
                <option value="">Select&#8230;</option>
                <option>Corporate Video</option>
                <option>Real Estate Video</option>
                <option>Social Media Content</option>
                <option>Explainer Video</option>
                <option>Wedding &amp; Event</option>
                <option>Other</option>
              </select>
            </div>
            <button type="submit" class="btn btn-primary">Get Quote</button>
          </div>
        </form>
        <div id="{slug}-sidebar-success" hidden style="display:none;" class="form-success">
          &#10003; We&#39;ll be in touch shortly!
        </div>
      </div>
      <div class="post-sidebar-card">
        <h4>Popular Services</h4>
        <ul>
          <li><a href="corporate-video-perth.html">Corporate Video Perth</a></li>
          <li><a href="real-estate-video-perth.html">Real Estate Video Perth</a></li>
          <li><a href="social-media-video-perth.html">Social Media Video Perth</a></li>
          <li><a href="explainer-video-perth.html">Explainer Video Perth</a></li>
          <li><a href="drone-video-editing-perth.html">Drone Video Editing Perth</a></li>
        </ul>
      </div>
    </aside>

  </div>
</section>

<section class="cta-section">
  <div class="container">
    <h2>Ready to Create Stunning Video Content?</h2>
    <p>Get a free quote from Perth Content — we respond within 2 business hours.</p>
    <div class="cta-btns">
      <a href="contact.html" class="btn btn-amber btn-lg">Get a Free Quote</a>
      <a href="services.html" class="btn btn-outline-white">View Our Services</a>
    </div>
  </div>
</section>

<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <a href="index.html" class="logo">Perth<span>Content</span></a>
        <p>Perth&#39;s video content marketplace &#8212; connecting businesses with expert editors and producers.</p>
      </div>
      <div class="footer-col">
        <h4>Top Services</h4>
        <a href="corporate-video-perth.html">Corporate Video</a>
        <a href="real-estate-video-perth.html">Real Estate Video</a>
        <a href="social-media-video-perth.html">Social Media Video</a>
        <a href="explainer-video-perth.html">Explainer Video</a>
        <a href="wedding-videography-perth.html">Wedding Video</a>
      </div>
      <div class="footer-col">
        <h4>Company</h4>
        <a href="about.html">About Us</a>
        <a href="portfolio.html">Portfolio</a>
        <a href="blog.html">Blog</a>
        <a href="contact.html">Contact</a>
      </div>
      <div class="footer-col">
        <h4>More Services</h4>
        <a href="drone-video-editing-perth.html">Drone Video</a>
        <a href="instagram-reels-editing-perth.html">Instagram Reels</a>
        <a href="tiktok-video-editing-perth.html">TikTok Editing</a>
        <a href="testimonial-video-perth.html">Testimonial Video</a>
        <a href="event-highlight-video-perth.html">Event Highlights</a>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; <span id="year"></span> Perth Content. All rights reserved. ABN: 00 000 000 000</p>
      <p>Serving Perth, WA &#8212; Professional Video Editing &amp; Production</p>
    </div>
  </div>
</footer>
<script src="js/main.js"></script>
</body>
</html>
'''

# ── POST DEFINITIONS ─────────────────────────────────────────────────────────
# Each dict: slug, title, tag, date, date_display, read_time, meta, excerpt, body
# body is plain HTML — use <h2>, <h3>, <p>, <ul><li> etc.

POSTS = [
    # Add post definitions here when generating posts.
    # See drafts/queue.json for the full list of planned topics.
    # Example structure:
    # {
    #     "slug": "blog-example-post",
    #     "title": "Example Post Title",
    #     "tag": "Corporate",
    #     "date": "2025-06-01",
    #     "date_display": "1 June 2025",
    #     "read_time": 5,
    #     "meta": "SEO meta description (155 chars max).",
    #     "excerpt": "Short intro shown in hero and blog card.",
    #     "body": "<p>Post content here...</p>",
    # },
]

# ── GENERATOR ────────────────────────────────────────────────────────────────

def generate(post: dict, output_dir: str):
    head = HEADER_TEMPLATE.format(
        slug=post["slug"],
        title=post["title"],
        tag=post["tag"],
        meta=post["meta"],
        excerpt=post["excerpt"],
        date=post["date"],
        date_display=post["date_display"],
        read_time=post["read_time"],
        site_url=SITE_URL,
        site_name=SITE_NAME,
    )
    foot = FOOTER_TEMPLATE.format(
        slug=post["slug"],
        formspree_id=FORMSPREE_ID,
    )
    content = head + post["body"] + foot
    out_path = os.path.join(output_dir, f"{post['slug']}.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)
    return out_path


if __name__ == "__main__":
    if not POSTS:
        print("No posts defined in POSTS list. Add post dicts and re-run.")
        sys.exit(0)

    output_dir = DRAFTS_DIR if WRITE_TO_DRAFTS else BASE_DIR
    os.makedirs(output_dir, exist_ok=True)

    generated = []
    for post in POSTS:
        path = generate(post, output_dir)
        generated.append(path)
        print(f"Generated: {path}")

    print(f"\n{len(generated)} post(s) generated to {'drafts/' if WRITE_TO_DRAFTS else './'}")
