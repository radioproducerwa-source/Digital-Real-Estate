#!/usr/bin/env python3
"""Update nav in all existing perthcontent HTML pages.
Replaces the old Suburbs dropdown nav with the new Services dropdown nav.
Run from the perthcontent/ directory.
"""

import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

NEW_NAV = '''    <nav class="main-nav" id="main-nav">
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
      <a href="blog.html">Blog</a>
      <a href="contact.html" class="btn btn-primary">Get a Quote</a>
    </nav>'''

# Pattern matches everything from <nav class="main-nav"... to </nav>
PATTERN = re.compile(
    r'<nav class="main-nav" id="main-nav">.*?</nav>',
    re.DOTALL
)

updated = []
skipped = []

for filename in sorted(os.listdir(BASE_DIR)):
    if not filename.endswith('.html'):
        continue
    filepath = os.path.join(BASE_DIR, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    if 'main-nav' not in content:
        skipped.append(filename)
        continue
    new_content = PATTERN.sub(NEW_NAV, content)
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        updated.append(filename)
    else:
        skipped.append(filename)

print(f"Updated {len(updated)} files:")
for f in updated:
    print(f"  ✓ {f}")
if skipped:
    print(f"\nSkipped {len(skipped)} files (no nav found or unchanged):")
    for f in skipped:
        print(f"  - {f}")
