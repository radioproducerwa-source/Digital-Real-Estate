# Digital Real Estate — Project Blueprint

Rank-and-rent lead generation portfolio. Three static HTML/CSS/JS sites in one GitHub repo.
No frameworks. Deployed on Vercel. Weekly blog auto-publish via GitHub Actions.

---

## Repo Structure

```
Digital-Real-Estate/
├── perthbondclean/          # Project #1 — bond cleaning leads
├── theperthmc/              # Project #2 — MC/event hosting leads
├── perthcontent/            # Project #3 — video editing/production leads
├── CLAUDE.md                # This file — working blueprint
├── PORTFOLIO_STATUS.md      # Master status tracker
└── .github/workflows/
    ├── weekly-blog-post.yml          # PerthBondClean auto-publisher
    ├── weekly-mc-blog-post.yml       # Perth MC auto-publisher
    └── weekly-video-blog-post.yml    # Perth Content auto-publisher
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
- Branch: `claude/create-perthbondclean-folder-QyWUw` (production)

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

## Project #3 — Perth Content

**Domain:** perthcontent.com
**Niche:** Video editing & content production, Perth WA
**Contact email:** info@perthcontent.com
**Formspree ID:** `mzdodayb`

### Brand
- Electric blue: `#0EA5E9` / dark: `#0284C7` / light: `#E0F2FE`
- Dark charcoal: `#0f0f0f` / mid: `#1e293b`
- Accent amber: `#F59E0B`
- Font: Inter (Google Fonts)

### Pages
- 6 core pages: `index.html`, `services.html`, `about.html`, `blog.html`, `contact.html`, `portfolio.html`
- 20 service landing pages: `corporate-video-perth`, `real-estate-video-perth`, `social-media-video-perth`, `instagram-reels-editing-perth`, `youtube-video-editing-perth`, `event-highlight-video-perth`, `explainer-video-perth`, `training-video-perth`, `drone-video-editing-perth`, `restaurant-hospitality-video-perth`, `wedding-videography-perth`, `product-video-perth`, `promotional-video-perth`, `linkedin-video-perth`, `startup-video-perth`, `tiktok-video-editing-perth`, `conference-seminar-video-perth`, `fitness-wellness-video-perth`, `testimonial-video-perth`, `annual-report-video-perth`
- 12 suburb pages: `subiaco`, `fremantle`, `joondalup`, `scarborough`, `cottesloe`, `mount-lawley`, `south-perth`, `nedlands`, `victoria-park`, `mosman-park`, `canning-vale`, `bayswater`
- 6 published blog posts
- 28 draft posts in queue (publishing weekly from June 2026)

### Blog automation
- **Workflow:** `.github/workflows/weekly-video-blog-post.yml`
- **Schedule:** Every Monday 9am AWST (01:00 UTC)
- **Queue file:** `perthcontent/drafts/queue.json`
- **Queue remaining:** 28 posts (~28 weeks — through Dec 2026)
- **Publisher script:** `perthcontent/publish_next.py`
- On publish: copies draft from `drafts/` → root, inserts blog card into `blog.html` after `<div class="blog-grid">`, adds URL to `sitemap.xml`, removes from queue

### Vercel
- Project: `perthcontent`
- Root Directory: `perthcontent`
- Branch: `claude/create-perthbondclean-folder-QyWUw` (production)

### SEO
- Canonical URLs: `https://perthcontent.com/`
- Sitemap: `perthcontent/sitemap.xml` (43+ URLs, grows weekly)
- Robots: `perthcontent/robots.txt`
- JSON-LD schemas: LocalBusiness + Service (landing pages), Article (blog posts)
- Meta descriptions on every page

### Pending owner actions
- [ ] Add GA4 tracking (paste `G-XXXXXXXXXX` ID to Claude — will add to all 44 pages)
- [ ] Build backlinks (Yellow Pages, True Local, Hotfrog, Yelp AU, Localsearch)
- [ ] Top up blog queue December 2026

---

## Shared Conventions

### Adding pages
- Copy an existing landing page as template
- Add URL to `sitemap.xml`
- Add nav link if needed

### Generating content in bulk
- `theperthmc/generate_landing_pages.py` — regenerates all 20 MC landing pages
- `theperthmc/generate_blogs.py` — regenerates all 26 published MC blog posts
- `theperthmc/generate_drafts.py` — regenerates all 28 MC draft posts into `drafts/`
- `perthcontent/generate_blogs.py` — generates Perth Content blog posts (populate POSTS list first)
- Run scripts from within their respective project directory

### When the draft queue runs dry
Generate new blog HTML files, add slugs to `queue.json`. Target: top up 3 months before queue empties.

### Formspree setup
1. Go to formspree.io, create a form
2. Copy the form ID
3. Find/replace the old ID (or `YOUR_FORM_ID`) across all HTML files in the project folder
- PerthBondClean: `mzdodayb` (shared with Perth Content — OK to separate later)
- Perth Content: `mzdodayb`
- Perth MC: `YOUR_FORM_ID` — still needs replacing

### Branch strategy
- All three projects deploy from `claude/create-perthbondclean-folder-QyWUw` (production branch)
- Feature work done on separate branches, merged to production when complete
- Consider renaming production branch to `main` for cleaner long-term management

---

## Pending / Owner Actions

### Perth MC
- [ ] Set up Formspree — replace `YOUR_FORM_ID` in all `theperthmc/` HTML files
- [ ] Add `perthmc.com` as custom domain in Vercel
- [ ] Build backlinks (local Perth directories)
- [ ] Create social media pages pointing to perthmc.com

### Perth Content
- [ ] Add GA4 measurement ID — tell Claude: "Add GA4 ID G-XXXXXXXXXX to all perthcontent pages"
- [ ] Build backlinks (local Perth directories)
- [ ] Top up blog queue December 2026
