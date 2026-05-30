# VonKlitzing Media — Digital Real Estate Portfolio Status

> Last updated: May 2026 (Perth Mechanic launched)
> Update this file whenever a site launches, goes live on Vercel, or hits a milestone.

---

## Business Overview

**Owner:** Robbie Von Klitzing  
**Model:** Rank-and-rent lead generation websites + future directory listings  
**Stack:** Static HTML/CSS/JS — GitHub + Vercel — GitHub Actions for automation  
**Repo:** `radioproducerwa-source/digital-real-estate` (branch: `claude/create-perthbondclean-folder-QyWUw`)  
**Blueprint file:** `/home/user/VonKlitzing_Digital_Real_Estate_Blueprint.xlsx` (full tracker)

---

## Site 1 — PerthBondClean ✅ LIVE

| Field | Detail |
|-------|--------|
| **Domain** | perthbondclean.com |
| **Niche** | End-of-lease / bond cleaning — Perth WA |
| **Folder** | `perthbondclean/` in this repo |
| **Status** | Live and ranking |
| **GSC** | Connected ✅ — 1,470 impressions, 2 clicks (May 2026) |
| **Sitemap** | Submitted ✅ |
| **Directories** | Listed on 10+ local directories ✅ |
| **Automation** | Weekly blog active — every Monday 9am AWST ✅ |
| **Blog queue** | 27 drafts remaining (~Nov 2026 before top-up needed) |
| **Schema fix** | Applied May 2026 — LocalBusiness + Place types |
| **Suburb pages** | 20 live |

**Revenue status:** Not yet monetised — building traffic first. Target: 200+ clicks/month before approaching buyers.

**Next actions:**
- Monitor GSC weekly — suburb pages indexing over next 4 weeks
- Top up blog queue October 2026 (say: *"generate 30 more bond cleaning blog drafts and add to queue.json"*)

---

## Site 2 — Perth Mechanic ✅ LIVE

| Field | Detail |
|-------|--------|
| **Domain** | perthmechanic.com |
| **Niche** | Car servicing & mechanical repairs — Perth WA |
| **Folder** | `perthmechanic/` in this repo |
| **Status** | Live — launched May 2026 |
| **Vercel** | Connected ✅ — project `perth-mechanic` |
| **GSC** | Connected ✅ — launched May 2026 |
| **Sitemap** | Submit to GSC ⬜ |
| **Directories** | Not yet listed ❌ |
| **Automation** | Weekly blog active — every Monday 9am AWST ✅ |
| **Blog queue** | 26 drafts remaining in `perthmechanic/drafts/queue.json` |
| **Suburb pages** | 20 live |
| **Formspree** | `YOUR_FORM_ID` placeholder — replace with real ID ⬜ |

**Revenue status:** Not yet monetised — building traffic first. Target: 200+ clicks/month before approaching buyers.

**Next actions:**
- Submit `sitemap.xml` in GSC → Sitemaps → `https://perthmechanic.com/sitemap.xml`
- Set up Formspree at formspree.io → replace `YOUR_FORM_ID` in all HTML files
- List on 10+ local directories (Yellow Pages, True Local, Hotfrog, Yelp AU, Localsearch)
- Monitor GSC weekly — indexing will take 4–8 weeks
- Top up blog queue October 2026 (say: *"generate 30 more mechanic blog drafts and add to queue.json"*)

---

## Site 3 — Perth MC Pro 📄 HANDOVER READY

| Field | Detail |
|-------|--------|
| **Domain** | TBD — check availability (perthmcpro.com.au recommended) |
| **Niche** | MC & event hosting — Perth WA |
| **Folder** | Not yet built — needs new Claude chat |
| **Handover doc** | `01_Perth_MC_Site_Handover.docx` at `/home/user/` |
| **Status** | Handover doc ready — not started |

**To start:** Open new Claude Code session → create new GitHub repo → paste Part 8 prompt from handover doc.

---

## Site 4 — Perth Video Pro 📄 HANDOVER READY

| Field | Detail |
|-------|--------|
| **Domain** | TBD — check availability |
| **Niche** | Video editing & production — Perth WA |
| **Folder** | Not yet built — needs new Claude chat |
| **Handover doc** | `02_Perth_Video_Site_Handover.docx` at `/home/user/` |
| **Status** | Handover doc ready — not started |

**To start:** Open new Claude Code session → create new GitHub repo → paste Part 8 prompt from handover doc.

---

## Directory Sites (separate project — not tracked here)

- **LocalPerth** — multi-niche Perth directory, being built in a separate Claude session
- Blueprint and handover doc: `03_FindPerth_Directory_Handover.docx` at `/home/user/`
- Not part of this lead-gen repo

---

## How This Repo Is Structured

```
digital-real-estate/
├── perthbondclean/          ← Site 1 (LIVE)
│   ├── index.html
│   ├── blog.html
│   ├── services.html
│   ├── about.html
│   ├── contact.html
│   ├── sitemap.xml
│   ├── [20 suburb pages].html
│   ├── [60+ blog posts].html
│   ├── drafts/              ← 27 unpublished posts + queue.json
│   ├── generate_drafts.py
│   └── publish_next.py
│
├── perthmechanic/           ← Site 2 (BUILT — needs Vercel)
│   ├── index.html
│   ├── blog.html
│   ├── services.html
│   ├── about.html
│   ├── contact.html
│   ├── sitemap.xml
│   ├── [20 suburb pages].html
│   ├── drafts/              ← 27 unpublished posts + queue.json
│   ├── generate_drafts.py
│   └── publish_next.py
│
├── .github/workflows/
│   ├── weekly-blog-post.yml          ← PerthBondClean automation
│   └── weekly-mechanic-blog.yml      ← PerthMechanic automation
│
└── PORTFOLIO_STATUS.md              ← This file
```

---

## Vercel Projects

| Site | Vercel Project | Root Directory | Domain |
|------|---------------|----------------|--------|
| PerthBondClean | perthbondclean | `perthbondclean/` | perthbondclean.com |
| Perth Mechanic | perth-mechanic | `perthmechanic/` | perthmechanic.com |

**How Vercel works with this repo:** Each site is a separate Vercel project pointing to the same GitHub repo but with a different Root Directory. Vercel serves only that subfolder as the site root.

---

## Weekly Automation Summary

Both sites auto-publish one blog post every **Monday at 9:00am AWST** (01:00 UTC).

The GitHub Action:
1. Runs `publish_next.py` in the site's folder
2. Copies the next draft from `drafts/` to the site root
3. Prepends a blog card to `blog.html`
4. Adds the URL to `sitemap.xml`
5. Commits and pushes automatically

**Queue top-up reminder: October 2026** — say *"generate 30 more [site] blog drafts and add to queue.json"* in the relevant Claude session.

---

## Revenue Targets

| Site | Target clicks/mo to approach buyers | Expected rental | Expected per-lead |
|------|--------------------------------------|-----------------|-------------------|
| PerthBondClean | 200+ | $500–$2,000/mo | $30–$80/lead |
| Perth Mechanic | 200+ | $500–$2,000/mo | $30–$80/lead |
| Perth MC Pro | 200+ | $500–$1,500/mo | $100–$300/lead |
| Perth Video Pro | 200+ | $300–$1,000/mo | $50–$200/lead |

---

## Quick Commands for Future Claude Sessions

**Top up PerthBondClean blog queue:**
> "Generate 30 more bond cleaning blog drafts for Perth and add them to `perthbondclean/drafts/queue.json`"

**Top up Perth Mechanic blog queue:**
> "Generate 30 more mechanic blog drafts for Perth and add them to `perthmechanic/drafts/queue.json`"

**Check GSC data and update this file:**
> "Update PORTFOLIO_STATUS.md with the latest GSC figures I'm about to share"

**Launch Perth Mechanic on Vercel:**
> "Walk me through connecting perthmechanic.com to Vercel using the perthmechanic/ folder in this repo"
