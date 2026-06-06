# VonKlitzing Media — Digital Real Estate Portfolio Status

> Last updated: May 2026 (Perth Content launched; Perth Mechanic confirmed built)
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
| **Folder** | `perthbondclean/` |
| **Status** | Live and ranking |
| **GSC** | Connected ✅ — 1,470 impressions, 2 clicks (May 2026) |
| **Sitemap** | Submitted ✅ |
| **Directories** | Listed on 10+ local directories ✅ |
| **Automation** | Weekly blog active — every Monday 9am AWST ✅ |
| **Blog queue** | ~27 drafts remaining (~Nov 2026 before top-up needed) |
| **Suburb pages** | 20 live |
| **Formspree** | `mzdodayb` ✅ |
| **GA4** | Not yet added ⬜ |

**Revenue status:** Not yet monetised — building traffic first. Target: 200+ clicks/month before approaching buyers.

**Next actions:**
- Monitor GSC weekly — suburb pages indexing over next 4 weeks
- Top up blog queue October 2026 → *"generate 30 more bond cleaning blog drafts and add to queue.json"*

---

## Site 2 — Perth MC ✅ LIVE

| Field | Detail |
|-------|--------|
| **Domain** | perthmc.com |
| **Niche** | Professional MC / event hosting — Perth WA |
| **Folder** | `theperthmc/` |
| **Status** | Live — launched 2026 |
| **Vercel** | Connected ✅ — project `theperthmc`, root dir `theperthmc/` |
| **GSC** | Connected ✅ |
| **Sitemap** | `theperthmc/sitemap.xml` (51 URLs) |
| **Directories** | Not yet listed ❌ |
| **Automation** | Weekly blog active — every Monday 9am AWST ✅ |
| **Blog queue** | 28 drafts remaining (~28 weeks of content) |
| **Landing pages** | 14 event types + 6 suburb pages = 20 live |
| **Formspree** | `YOUR_FORM_ID` — still placeholder ❌ needs replacing |
| **GA4** | Not yet added ⬜ |

**Revenue status:** Not yet monetised — building traffic first. Target: 200+ clicks/month before approaching buyers.

**Next actions:**
- Replace `YOUR_FORM_ID` in all `theperthmc/` HTML files with real Formspree ID
- List on 10+ local directories (Yellow Pages, True Local, Hotfrog, Yelp AU, Localsearch)
- Monitor GSC weekly
- Top up blog queue October 2026 → *"generate 30 more MC blog drafts and add to queue.json"*

---

## Site 3 — Perth Content ✅ LIVE

| Field | Detail |
|-------|--------|
| **Domain** | perthcontent.com |
| **Niche** | Video editing & content production — Perth WA |
| **Folder** | `perthcontent/` |
| **Status** | Live — launched May 2026 |
| **Vercel** | Connected ✅ — project `perthcontent`, root dir `perthcontent/` |
| **GSC** | Connected ✅ — TXT DNS record verified via Namecheap |
| **Sitemap** | `perthcontent/sitemap.xml` (53+ URLs, grows weekly) ✅ |
| **Directories** | Not yet listed ❌ |
| **Automation** | Weekly blog active — every Monday 9am AWST ✅ |
| **Blog queue** | 28 drafts remaining (Dec 2026–Feb 2027) |
| **Service pages** | 20 live |
| **Suburb pages** | 12 live |
| **Live blog posts** | 16 published |
| **Formspree** | `mzdodayb` ✅ |
| **GA4** | Not yet added ⬜ — owner to get G-XXXXXXXXXX ID, then tell Claude |

**Revenue status:** Not yet monetised — building traffic first. Target: 200+ clicks/month before approaching buyers.

**Next actions:**
- Add GA4 → get Measurement ID from analytics.google.com → tell Claude: *"Add GA4 ID G-XXXXXXXXXX to all perthcontent pages"*
- List on 10+ local directories (Yellow Pages, True Local, Hotfrog, Yelp AU, Localsearch)
- Monitor GSC weekly — first meaningful rankings expected 8–12 weeks post-launch
- Top up blog queue February 2027 → *"generate 30 more video blog drafts and add to queue.json"*

---

## Site 4 — Perth Mechanic ✅ LIVE

| Field | Detail |
|-------|--------|
| **Domain** | perthmechanic.com |
| **Niche** | Car servicing & mechanical repairs — Perth WA |
| **Folder** | `perthmechanic/` |
| **Status** | Live — launched May 2026 |
| **Vercel** | Connected ✅ — project `perth-mechanic`, root dir `perthmechanic/` |
| **GSC** | Connected ✅ — launched May 2026 |
| **Sitemap** | `perthmechanic/sitemap.xml` (26 URLs) — not yet submitted to GSC ⬜ |
| **Directories** | Not yet listed ❌ |
| **Automation** | Weekly blog active — every Monday 9am AWST ✅ |
| **Blog queue** | 27 drafts remaining (~27 weeks of content) |
| **Suburb pages** | 20 live |
| **Live blog posts** | 1 published |
| **Formspree** | `mzdodayb` ✅ |
| **GA4** | Not yet added ⬜ |

**Revenue status:** Not yet monetised — building traffic first. Target: 200+ clicks/month before approaching buyers.

**Next actions:**
- Submit sitemap in GSC → `https://perthmechanic.com/sitemap.xml`
- List on 10+ local directories (Yellow Pages, True Local, Hotfrog, Yelp AU, Localsearch)
- Add GA4 tracking → get Measurement ID, then tell Claude: *"Add GA4 ID G-XXXXXXXXXX to all perthmechanic pages"*
- Monitor GSC weekly — first meaningful rankings expected 8–12 weeks post-launch
- Top up blog queue October 2026 → *"generate 30 more mechanic blog drafts and add to queue.json"*

---

## Site 5 — (Next Site TBD) 📋 PLANNED

**To start:** Open new Claude Code session, read CLAUDE.md and PORTFOLIO_STATUS.md for conventions.

---

## How This Repo Is Structured

```
digital-real-estate/
├── perthbondclean/          ← Site 1 (LIVE)
│   ├── index.html
│   ├── blog.html / services.html / about.html / contact.html
│   ├── sitemap.xml + robots.txt
│   ├── [20 suburb pages].html
│   ├── [57+ blog posts].html
│   ├── drafts/              ← ~27 unpublished posts + queue.json
│   └── publish_next.py
│
├── theperthmc/              ← Site 2 (LIVE)
│   ├── index.html
│   ├── blog.html / services.html / about.html / contact.html
│   ├── sitemap.xml + robots.txt
│   ├── [20 landing pages].html
│   ├── [26 blog posts].html
│   ├── drafts/              ← 28 unpublished posts + queue.json
│   └── publish_next.py
│
├── perthcontent/            ← Site 3 (LIVE)
│   ├── index.html
│   ├── blog.html / services.html / about.html / contact.html / portfolio.html
│   ├── sitemap.xml + robots.txt
│   ├── [20 service landing pages].html
│   ├── [12 suburb pages].html
│   ├── [6 blog posts].html
│   ├── drafts/              ← 28 unpublished posts + queue.json
│   ├── publish_next.py
│   └── generate_blogs.py
│
├── perthmechanic/           ← Site 4 (LIVE)
│   ├── index.html
│   ├── blog.html / services.html / about.html / contact.html
│   ├── sitemap.xml + robots.txt
│   ├── [20 suburb pages].html
│   ├── [1 blog post].html
│   ├── drafts/              ← 27 unpublished posts + queue.json
│   └── publish_next.py
│
├── .github/workflows/
│   ├── weekly-blog-post.yml          ← PerthBondClean (Mondays 9am AWST)
│   ├── weekly-mc-blog-post.yml       ← Perth MC (Mondays 9am AWST)
│   ├── weekly-video-blog-post.yml    ← Perth Content (Mondays 9am AWST)
│   └── weekly-mechanic-blog.yml      ← Perth Mechanic (Mondays 9am AWST)
│
├── CLAUDE.md                ← Working blueprint + conventions
└── PORTFOLIO_STATUS.md      ← This file
```

---

## Vercel Projects

| Site | Vercel Project | Root Directory | Domain |
|------|---------------|----------------|--------|
| PerthBondClean | perthbondclean | `perthbondclean/` | perthbondclean.com |
| Perth MC | theperthmc | `theperthmc/` | perthmc.com |
| Perth Content | perthcontent | `perthcontent/` | perthcontent.com |
| Perth Mechanic | perth-mechanic | `perthmechanic/` | perthmechanic.com |

**How Vercel works with this repo:** Each site is a separate Vercel project pointing to the same GitHub repo but with a different Root Directory. All deploy from branch `claude/create-perthbondclean-folder-QyWUw`.

---

## Weekly Automation Summary

All four sites auto-publish one blog post every **Monday at 9:00am AWST** (01:00 UTC).

The GitHub Action for each site:
1. Runs `publish_next.py` in the site's folder
2. Copies the next draft from `drafts/` to the site root
3. Prepends a blog card to `blog.html`
4. Adds the URL to `sitemap.xml`
5. Commits and pushes automatically

**Queue top-up reminders:**
- PerthBondClean: October 2026
- Perth MC: October 2026
- Perth Mechanic: October 2026
- Perth Content: December 2026

---

## Revenue Targets

| Site | Target clicks/mo | Expected rental | Expected per-lead |
|------|-----------------|-----------------|-------------------|
| PerthBondClean | 200+ | $500–$2,000/mo | $30–$80/lead |
| Perth MC | 200+ | $500–$1,500/mo | $100–$300/lead |
| Perth Content | 200+ | $300–$1,000/mo | $50–$200/lead |
| Perth Mechanic | 200+ | $500–$2,000/mo | $50–$150/lead |

---

## Quick Commands for Future Claude Sessions

**Top up PerthBondClean blog queue:**
> "Generate 30 more bond cleaning blog drafts for Perth and add them to `perthbondclean/drafts/queue.json`"

**Top up Perth MC blog queue:**
> "Generate 30 more MC/events blog drafts for Perth and add them to `theperthmc/drafts/queue.json`"

**Top up Perth Content blog queue:**
> "Generate 30 more video/content blog drafts for Perth and add them to `perthcontent/drafts/queue.json`"

**Add GA4 to Perth Content:**
> "Add GA4 ID G-XXXXXXXXXX to all perthcontent pages"

**Top up Perth Mechanic blog queue:**
> "Generate 30 more mechanic blog drafts for Perth and add them to `perthmechanic/drafts/queue.json`"

**Add GA4 to Perth Mechanic:**
> "Add GA4 ID G-XXXXXXXXXX to all perthmechanic pages"

**Update GSC figures:**
> "Update PORTFOLIO_STATUS.md with the latest GSC figures I'm about to share"

**Check overall portfolio status:**
> Read CLAUDE.md and PORTFOLIO_STATUS.md to get up to speed
