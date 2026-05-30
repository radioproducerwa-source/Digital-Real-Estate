# Digital Real Estate — Project Blueprint

Rank-and-rent lead generation portfolio. Two static HTML/CSS/JS sites in one GitHub repo.
No frameworks. Deployed on Vercel. Weekly blog auto-publish via GitHub Actions.

---

## Repo Structure

```
Digital-Real-Estate/
├── perthbondclean/          # Project #1 — bond cleaning leads
├── theperthmc/              # Project #2 — MC/event hosting leads
└── .github/workflows/
    ├── weekly-blog-post.yml          # PerthBondClean auto-publisher
    └── weekly-mc-blog-post.yml       # Perth MC auto-publisher
```

---

## Project #1 — Perth Bond Clean

**Domain:** perthbondclean.com
**Niche:** End-of-lease bond cleaning, Perth WA
**Contact email:** info@perthbondclean.com
**Formspree:** Replace `YOUR_FORM_ID` in all forms

### Brand
- Primary colour: `#1D9E75` (green)
- Font: Inter (Google Fonts)

### Pages
- 5 core: index, services, about, blog, contact
- Suburb landing pages (Armadale, Baldivis, Bayswater, etc.)
- 57+ published blog posts

### Blog automation
- **Workflow:** `.github/workflows/weekly-blog-post.yml`
- **Schedule:** Every Monday 9am AWST (01:00 UTC)
- **Queue file:** `perthbondclean/drafts/queue.json`
- **Queue remaining:** ~26 posts
- **Publisher script:** `perthbondclean/publish_next.py`
- On publish: copies draft HTML → root, inserts blog card into `blog.html` after `<div class="blog-grid">`, adds URL to `sitemap.xml`, removes from queue

### Vercel
- Project: `perthbondclean` (or `digital-real-estate`)
- Root Directory: `perthbondclean`
- Branch: `claude/create-perthbondclean-folder-QyWUw` (production)

---

## Project #2 — Perth MC

**Domain:** perthmc.com
**Niche:** Professional MC / event hosting, Perth WA
**Contact email:** info@perthmc.com
**Formspree:** Replace `YOUR_FORM_ID` in all forms

### Brand
- Charcoal dark: `#0D0D0D` / `#1C1C1C`
- Champagne gold: `#D4AF37`
- Gold dark: `#B8961E`
- Gold light: `#FBF5DD`
- Font: Inter (Google Fonts)
- Checklist marker: `✦` (gold)

### Pages
- 5 core pages: `index.html`, `services.html`, `about.html`, `blog.html`, `contact.html`
- 20 landing pages:
  - Event types: `wedding-mc-perth`, `corporate-mc-perth`, `conference-mc-perth`, `charity-gala-mc-perth`, `awards-night-mc-perth`, `christmas-party-mc-perth`, `school-formal-mc-perth`, `product-launch-mc-perth`, `fundraiser-mc-perth`, `team-building-mc-perth`, `mc-50th-birthday-perth`, `mc-21st-birthday-perth`, `outdoor-wedding-mc-perth`, `black-tie-event-mc-perth`
  - Suburbs: `wedding-mc-fremantle`, `wedding-mc-joondalup`, `wedding-mc-mandurah`, `wedding-mc-subiaco`, `wedding-mc-scarborough`, `wedding-mc-rockingham`
- 26 published blog posts (see `blog.html` for full list)
- 28 draft posts in queue

### Blog automation
- **Workflow:** `.github/workflows/weekly-mc-blog-post.yml`
- **Schedule:** Every Monday 9am AWST (01:00 UTC)
- **Queue file:** `theperthmc/drafts/queue.json`
- **Queue remaining:** 28 posts (~28 weeks of content)
- **Publisher script:** `theperthmc/publish_next.py`
- On publish: copies draft from `drafts/` → root, inserts blog card into `blog.html` after `<div class="blog-grid">`, adds URL to `sitemap.xml`, removes from queue

### Vercel
- Project: `theperthmc`
- Root Directory: `theperthmc`
- Branch: `claude/create-perthbondclean-folder-QyWUw` (both projects share this branch)

### SEO
- Canonical URLs: `https://perthmc.com/`
- Sitemap: `theperthmc/sitemap.xml` (51 URLs)
- Robots: `theperthmc/robots.txt`
- JSON-LD schemas: LocalBusiness (all pages), Article (blog posts), FAQPage (homepage)
- Meta descriptions on every page

### Design is rank-and-rent safe
- No personal names anywhere
- "We/our/us" language throughout (not "I/me")
- No headshots or personal bio
- Brand name "Perth MC" matches domain exactly

---

## Shared Conventions

### Adding pages
- Copy an existing landing page as template
- Add URL to `sitemap.xml`
- Add nav link if needed

### Generating content in bulk
- `theperthmc/generate_landing_pages.py` — regenerates all 20 landing pages
- `theperthmc/generate_blogs.py` — regenerates all 26 published blog posts
- `theperthmc/generate_drafts.py` — regenerates all 28 draft posts into `drafts/`
- Run from the `theperthmc/` directory

### When the draft queue runs dry
Re-run `generate_drafts.py` with new slugs/titles added to the script, update `queue.json`.

### Formspree setup
1. Go to formspree.io, create a form
2. Copy the form ID
3. Find/replace `YOUR_FORM_ID` across all HTML files in the project folder

### Branch strategy
- Both projects currently deployed from `claude/create-perthbondclean-folder-QyWUw`
- Development branch: `claude/file-upload-constraints-XOrHc`
- Consider merging both to `main` for cleaner long-term management

---

## Pending / Owner Actions

- [ ] Set up Formspree and replace `YOUR_FORM_ID` in all Perth MC forms
- [ ] Add `perthmc.com` as custom domain in Vercel
- [ ] Build backlinks (local Perth directories: Yellow Pages, True Local, Hotfrog, Yelp AU, Localsearch)
- [ ] Create Facebook + Instagram pages for Perth MC pointing to perthmc.com
- [ ] Top up draft queue when it runs dry (~28 weeks from launch)
