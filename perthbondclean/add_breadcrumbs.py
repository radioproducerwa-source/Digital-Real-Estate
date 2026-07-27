#!/usr/bin/env python3
"""Add BreadcrumbList JSON-LD schema to PerthBondClean inner pages."""

import os
import re
import glob

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "https://perthbondclean.com"

SUBURB_FILES = [
    "armadale", "baldivis", "bayswater", "canning-vale", "cannington",
    "claremont", "cottesloe", "ellenbrook", "fremantle", "joondalup",
    "karrinyup", "mandurah", "midland", "morley", "mount-lawley",
    "rockingham", "scarborough", "stirling", "subiaco", "victoria-park",
]

SKIP_FILES = {
    "index.html", "blog.html", "services.html", "about.html", "contact.html",
}


def slug_to_name(slug):
    """Convert a slug like 'canning-vale' to 'Canning Vale'."""
    return " ".join(word.capitalize() for word in slug.split("-"))


def extract_title(html, suffix=" | Perth Bond Clean"):
    """Extract page title from <title> tag, stripping the site suffix."""
    match = re.search(r"<title>(.*?)</title>", html, re.IGNORECASE | re.DOTALL)
    if not match:
        return None
    title = match.group(1).strip()
    if title.endswith(suffix):
        title = title[: -len(suffix)].strip()
    return title


def build_blog_breadcrumb(title):
    return (
        '<script type="application/ld+json">\n'
        '{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":['
        '{"@type":"ListItem","position":1,"name":"Home","item":"' + DOMAIN + '/"},'
        '{"@type":"ListItem","position":2,"name":"Blog","item":"' + DOMAIN + '/blog.html"},'
        '{"@type":"ListItem","position":3,"name":"' + title + '"}'
        "]}\n"
        "</script>"
    )


def build_suburb_breadcrumb(suburb_name):
    return (
        '<script type="application/ld+json">\n'
        '{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":['
        '{"@type":"ListItem","position":1,"name":"Home","item":"' + DOMAIN + '/"},'
        '{"@type":"ListItem","position":2,"name":"Areas","item":"' + DOMAIN + '/"},'
        '{"@type":"ListItem","position":3,"name":"' + suburb_name + '"}'
        "]}\n"
        "</script>"
    )


def process_file(filepath, breadcrumb_script):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Skip if already has BreadcrumbList
    if "BreadcrumbList" in content:
        print(f"  SKIP (already has BreadcrumbList): {os.path.basename(filepath)}")
        return False

    # Insert before </body>
    if "</body>" not in content:
        print(f"  WARN (no </body> found): {os.path.basename(filepath)}")
        return False

    new_content = content.replace("</body>", breadcrumb_script + "\n</body>", 1)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    return True


def main():
    added = 0
    skipped = 0

    # --- Blog posts ---
    blog_files = sorted(glob.glob(os.path.join(BASE_DIR, "blog-*.html")))
    print(f"\nProcessing {len(blog_files)} blog post files...")
    for filepath in blog_files:
        filename = os.path.basename(filepath)
        if filename in SKIP_FILES:
            continue

        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        title = extract_title(content)
        if not title:
            print(f"  WARN (no title found): {filename}")
            skipped += 1
            continue

        script = build_blog_breadcrumb(title)
        if process_file(filepath, script):
            print(f"  OK: {filename}  →  \"{title}\"")
            added += 1
        else:
            skipped += 1

    # --- Suburb pages ---
    print(f"\nProcessing {len(SUBURB_FILES)} suburb files...")
    for slug in SUBURB_FILES:
        filepath = os.path.join(BASE_DIR, f"{slug}.html")
        if not os.path.exists(filepath):
            print(f"  WARN (file not found): {slug}.html")
            skipped += 1
            continue

        suburb_name = slug_to_name(slug)
        script = build_suburb_breadcrumb(suburb_name)
        if process_file(filepath, script):
            print(f"  OK: {slug}.html  →  \"{suburb_name}\"")
            added += 1
        else:
            skipped += 1

    print(f"\nDone. Added: {added}  |  Skipped/warned: {skipped}")


if __name__ == "__main__":
    main()
