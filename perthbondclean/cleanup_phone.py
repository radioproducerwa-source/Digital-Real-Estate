#!/usr/bin/env python3
"""
Remove [TRACKED_NUMBER] from all perthbondclean HTML pages.
- Strips phone from header, footer, hero CTAs, CTA bands, contact details
- Replaces "Prefer to call?" box with an email nudge
- Updates meta descriptions and FAQ text
- Leaves contact form as the sole primary CTA
"""
import re, os, glob

BASE = os.path.dirname(os.path.abspath(__file__))

# Replacement for the "Prefer to call?" box in suburb pages
EMAIL_BOX = (
    '\n      <div style="background:var(--green-lt);border:1.5px solid var(--border);'
    'border-radius:var(--radius);padding:20px;margin-top:20px;text-align:center;">\n'
    '        <p style="font-weight:600;margin-bottom:6px;color:var(--dark);">Have a question?</p>\n'
    '        <a href="mailto:info@perthbondclean.com" '
    'style="font-size:1rem;font-weight:700;color:var(--green);">'
    'info@perthbondclean.com</a>\n'
    '        <p style="font-size:0.85rem;color:var(--muted);margin-top:6px;">'
    'We reply within 1 hour, 7 days a week</p>\n'
    '      </div>'
)


def clean(content):
    # ── 1. Meta description: remove "Call [TRACKED_NUMBER] today." ──
    content = re.sub(
        r' Call \[TRACKED_NUMBER\] today\.',
        '',
        content
    )

    # ── 2. Header phone link (single line) ──
    content = re.sub(
        r'\n[ \t]*<a href="tel:\[TRACKED_NUMBER\]" class="header-phone">\[TRACKED_NUMBER\]</a>',
        '',
        content
    )

    # ── 3. Footer phone <p> line ──
    content = re.sub(
        r'\n[ \t]*<p>&#128222; <a href="tel:\[TRACKED_NUMBER\]">\[TRACKED_NUMBER\]</a></p>',
        '',
        content
    )

    # ── 4. "Prefer to call?" box → email nudge ──
    content = re.sub(
        r'\n[ \t]*<div style="background:var\(--green-lt\)[^>]*>'
        r'\s*<p[^>]*>Prefer to call\?</p>.*?</div>',
        EMAIL_BOX,
        content,
        flags=re.DOTALL
    )

    # ── 5. Phone contact-detail blocks (anchored on 📞 emoji) ──
    content = re.sub(
        r'\n[ \t]*<div class="contact-detail">[ \t]*\n'
        r'[ \t]*<span[^>]*>📞</span>.*?</div>[ \t]*\n[ \t]*</div>',
        '',
        content,
        flags=re.DOTALL
    )

    # ── 6. All remaining tel: anchor tags (buttons, inline links) ──
    content = re.sub(
        r'\n[ \t]*<a href="tel:\[TRACKED_NUMBER\]"[^>]*>.*?</a>',
        '',
        content
    )

    # ── 7. FAQ sentence referencing the phone number ──
    content = content.replace(
        'call us directly on [TRACKED_NUMBER] and',
        'use the contact form on this page and'
    )

    # ── 8. Sweep: any remaining [TRACKED_NUMBER] text ──
    content = content.replace('[TRACKED_NUMBER]', '')

    # ── 9. Clean up leftover empty tel: hrefs just in case ──
    content = re.sub(r'<a href="tel:"[^>]*>[^<]*</a>', '', content)

    # ── 10. Collapse 3+ blank lines to 2 ──
    content = re.sub(r'\n{3,}', '\n\n', content)

    return content


html_files = sorted(glob.glob(os.path.join(BASE, '*.html')))
changed = 0

for path in html_files:
    with open(path, 'r', encoding='utf-8') as f:
        original = f.read()
    updated = clean(original)
    if updated != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(updated)
        remaining = updated.count('TRACKED_NUMBER')
        flag = f' ⚠ {remaining} remaining!' if remaining else ''
        print(f'  ✓ {os.path.basename(path)}{flag}')
        changed += 1
    else:
        print(f'  · {os.path.basename(path)} (unchanged)')

print(f'\n{changed}/{len(html_files)} files updated.')

# Final check
leftover = []
for path in html_files:
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
    n = c.count('TRACKED_NUMBER')
    if n:
        leftover.append((os.path.basename(path), n))

if leftover:
    print('\n⚠ Remaining TRACKED_NUMBER occurrences:')
    for fname, n in leftover:
        print(f'  {fname}: {n}')
else:
    print('\n✅ All [TRACKED_NUMBER] placeholders removed.')
