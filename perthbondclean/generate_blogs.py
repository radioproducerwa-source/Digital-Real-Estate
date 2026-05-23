#!/usr/bin/env python3
"""Generate blog post HTML files for perthbondclean."""

import os

HEADER = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="{meta}" />
  <meta name="robots" content="index, follow" />
  <title>{title} | Perth Bond Clean</title>
  <link rel="canonical" href="https://perthbondclean.com/{slug}.html" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="css/style.css" />
</head>
<body>
<header class="site-header">
  <div class="container header-inner">
    <a href="index.html" class="logo">Perth<span>Bond</span>Clean</a>
    <nav class="main-nav" id="main-nav">
      <a href="index.html">Home</a>
      <a href="services.html">Services</a>
      <div class="dropdown">
        <button class="dropdown-btn">Suburbs &#9660;</button>
        <div class="dropdown-menu">
          <a href="joondalup.html">Joondalup</a><a href="subiaco.html">Subiaco</a><a href="fremantle.html">Fremantle</a><a href="rockingham.html">Rockingham</a><a href="baldivis.html">Baldivis</a><a href="canning-vale.html">Canning Vale</a><a href="midland.html">Midland</a><a href="morley.html">Morley</a><a href="ellenbrook.html">Ellenbrook</a><a href="mandurah.html">Mandurah</a><a href="armadale.html">Armadale</a><a href="cannington.html">Cannington</a><a href="victoria-park.html">Victoria Park</a><a href="mount-lawley.html">Mount Lawley</a><a href="scarborough.html">Scarborough</a><a href="cottesloe.html">Cottesloe</a><a href="claremont.html">Claremont</a><a href="karrinyup.html">Karrinyup</a><a href="stirling.html">Stirling</a><a href="bayswater.html">Bayswater</a>
        </div>
      </div>
      <a href="about.html">About</a>
      <a href="blog.html" class="active">Blog</a>
      <a href="contact.html" class="btn btn-primary">Get a Quote</a>
    </nav>
    <div class="header-right">
      <button class="hamburger" id="hamburger" aria-label="Open menu" aria-expanded="false">&#9776;</button>
    </div>
  </div>
</header>
<section class="about-hero">
  <div class="container" style="max-width:800px;">
    <div style="margin-bottom:12px;"><a href="blog.html" style="color:var(--green);font-size:0.9rem;text-decoration:none;">&larr; Back to Blog</a></div>
    <h1>{h1}</h1>
    <p style="color:var(--muted);font-size:0.95rem;margin-top:12px;">Published May 2025 &nbsp;|&nbsp; {read_time} min read</p>
  </div>
</section>
<section class="section-pad">
  <div class="container" style="max-width:800px;">
    <article class="blog-article">
{content}
      <div style="text-align:center;margin:40px 0 16px;">
        <a href="contact.html" class="btn btn-primary btn-lg">Get a Free Bond Cleaning Quote &rarr;</a>
      </div>
      <p style="text-align:center;color:var(--muted);font-size:0.9rem;">We respond within 1 hour, 7 days a week.</p>
    </article>
  </div>
</section>'''

FOOTER = '''<footer class="site-footer">
  <div class="container">
    <div class="footer-top">
      <div class="footer-brand">
        <a href="index.html" class="logo">Perth<span>Bond</span>Clean</a>
        <p>Perth\'s #1 Bond Cleaning Lead Service.<br>Helping Perth renters get their full bond back since 2020.</p>
        <p>&#x2709;&#xFE0F; <a href="mailto:info@perthbondclean.com">info@perthbondclean.com</a></p>
      </div>
      <div class="footer-links">
        <h4>Quick Links</h4>
        <ul>
          <li><a href="index.html">Home</a></li><li><a href="services.html">Services</a></li><li><a href="about.html">About</a></li><li><a href="blog.html">Blog</a></li><li><a href="contact.html">Contact</a></li>
        </ul>
      </div>
      <div class="footer-suburbs">
        <h4>Suburbs We Serve</h4>
        <ul>
          <li><a href="joondalup.html">Joondalup</a></li><li><a href="subiaco.html">Subiaco</a></li><li><a href="fremantle.html">Fremantle</a></li><li><a href="rockingham.html">Rockingham</a></li><li><a href="baldivis.html">Baldivis</a></li><li><a href="canning-vale.html">Canning Vale</a></li><li><a href="midland.html">Midland</a></li><li><a href="morley.html">Morley</a></li><li><a href="ellenbrook.html">Ellenbrook</a></li><li><a href="mandurah.html">Mandurah</a></li><li><a href="armadale.html">Armadale</a></li><li><a href="cannington.html">Cannington</a></li><li><a href="victoria-park.html">Victoria Park</a></li><li><a href="mount-lawley.html">Mount Lawley</a></li><li><a href="scarborough.html">Scarborough</a></li><li><a href="cottesloe.html">Cottesloe</a></li><li><a href="claremont.html">Claremont</a></li><li><a href="karrinyup.html">Karrinyup</a></li><li><a href="stirling.html">Stirling</a></li><li><a href="bayswater.html">Bayswater</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; <span id="year"></span> Perth Bond Clean. All rights reserved. | Website by Perth Bond Clean</p>
    </div>
  </div>
</footer>
<script src="js/main.js"></script>
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Article","headline":"{title}","description":"{meta}","url":"https://perthbondclean.com/{slug}.html","datePublished":"2025-05-01","dateModified":"2025-05-01","author":{{"@type":"Organization","name":"Perth Bond Clean","url":"https://perthbondclean.com"}},"publisher":{{"@type":"Organization","name":"Perth Bond Clean","url":"https://perthbondclean.com","logo":{{"@type":"ImageObject","url":"https://perthbondclean.com/logo.png"}}}},"mainEntityOfPage":{{"@type":"WebPage","@id":"https://perthbondclean.com/{slug}.html"}}}}
</script>
</body>
</html>'''

ARTICLES = [
  {
    "slug": "blog-vacate-cleaning-perth",
    "title": "Vacate Cleaning Perth — What It Is and What to Expect",
    "h1": "Vacate Cleaning Perth — What It Is and What to Expect",
    "meta": "Vacate cleaning in Perth explained. What's included, how it differs from a regular clean, average costs, and how to make sure you pass your exit inspection.",
    "read_time": 5,
    "content": """
      <p>Vacate cleaning, bond cleaning, and end-of-lease cleaning all refer to the same thing — a comprehensive deep clean of a rental property when the tenant moves out. In Perth, the term "vacate clean" is commonly used by property managers and tenants alike.</p>
      <h2>What Does a Vacate Clean Cover?</h2>
      <p>A proper Perth vacate clean follows the REIWA Property Condition Report and covers every area of the home. No surface, appliance, or cupboard interior is skipped.</p>
      <ul class="checklist">
        <li>Full kitchen deep clean including oven, rangehood filters, and cupboard interiors</li>
        <li>All bathrooms — shower screens, grout, toilet, vanity, exhaust fans</li>
        <li>Laundry tub, taps, and appliance spaces</li>
        <li>Bedroom wardrobes — shelves, rails, tracks, and door faces</li>
        <li>Blind slats individually wiped</li>
        <li>Skirting boards along every wall</li>
        <li>Window sills, tracks, and internal glass</li>
        <li>Light fittings and ceiling fans</li>
        <li>All floors vacuumed and mopped</li>
      </ul>
      <h2>How Much Does a Vacate Clean Cost in Perth?</h2>
      <p>Prices depend on the size and condition of the property. A studio or 1-bedroom starts from around $250–$350. A 3x2 home is typically $400–$600. Carpet steam cleaning is an add-on if required by your lease. See our <a href="blog-bond-cleaning-cost-perth.html" style="color:var(--green);">full price guide</a> for a detailed breakdown.</p>
      <h2>Do I Need a Professional Vacate Cleaner?</h2>
      <p>Not legally — but practically, for most Perth tenants, yes. A professional works from the same REIWA checklist your property manager uses, and backs the clean with a bond back guarantee. If anything is flagged within 72 hours, they return and fix it free of charge.</p>
      <p>The cost of a professional vacate clean is almost always less than the bond deductions that follow a failed exit inspection. Most Perth renters who've tried both say they'll never do it themselves again.</p>
      <h2>When Should I Book?</h2>
      <p>Book 1–2 weeks before your move-out date. Perth vacate cleaners fill up quickly at month-ends. The clean should be completed 1–2 days before your exit inspection, giving you time to spot-check and replace any blown light globes.</p>
      <h2>What Happens After the Vacate Clean?</h2>
      <p>Your property manager will carry out the exit inspection, comparing the property to the ingoing condition report. With a professional clean and a guarantee behind you, any flagged items can be addressed immediately at no extra cost — keeping your full bond intact.</p>
"""
  },
  {
    "slug": "blog-exit-cleaning-perth",
    "title": "Exit Cleaning Perth — Everything Tenants Need to Know",
    "h1": "Exit Cleaning Perth — Everything Tenants Need to Know",
    "meta": "Exit cleaning in Perth explained. What's required, what property managers check, costs, and how to make sure you get your full bond back at the end of your tenancy.",
    "read_time": 5,
    "content": """
      <p>Exit cleaning — also called bond cleaning or vacate cleaning — is the deep clean required when you move out of a rental in Perth. It's the last major task before handing back the keys, and it's the one most likely to affect whether you get your bond back in full.</p>
      <h2>What Is Exit Cleaning?</h2>
      <p>Exit cleaning restores a rental property to the standard documented in the ingoing Property Condition Report — the form completed when you first moved in. Property managers in Perth compare the ingoing and outgoing reports to assess whether any cleaning deductions are warranted.</p>
      <h2>What's Required in a Perth Exit Clean?</h2>
      <p>The REIWA exit condition checklist covers every room. Key requirements include:</p>
      <ul class="checklist">
        <li>Kitchen: oven, rangehood, cupboards, benchtops, sink, dishwasher</li>
        <li>Bathrooms: shower screen, grout, toilet, vanity, exhaust fans</li>
        <li>All rooms: skirting boards, blind slats, window tracks, wardrobes, light fittings</li>
        <li>Floors: vacuumed and mopped throughout</li>
        <li>Garage and outdoor areas if applicable</li>
      </ul>
      <p>If your lease specifies professional carpet steam cleaning, that's a separate requirement with its own receipt needed.</p>
      <h2>How Much Does Exit Cleaning Cost in Perth?</h2>
      <p>A 1-bedroom unit: $250–$350. A 2x1: $320–$450. A 3x2: $400–$600. Larger homes: $600–$1,000+. These prices include all standard rooms and appliances. See our <a href="blog-bond-cleaning-cost-perth.html" style="color:var(--green);">2025 Perth bond cleaning price guide</a>.</p>
      <h2>The Bond Back Guarantee — Why It Matters</h2>
      <p>A reputable Perth exit cleaner backs every job with a bond back guarantee: if your property manager flags any cleaning issue within 72 hours, the cleaner returns to fix it at no cost. This is the safety net that protects your bond if anything is missed on the first clean.</p>
      <h2>Tips for a Smooth Exit</h2>
      <ul class="checklist">
        <li>Book your exit clean at least 1 week before your inspection</li>
        <li>Have the property completely vacated before the clean begins</li>
        <li>Take timestamped photos after the clean and before handing back keys</li>
        <li>Keep all receipts — exit clean, carpet cleaning, any repairs</li>
        <li>Attend the exit inspection if possible</li>
      </ul>
"""
  },
  {
    "slug": "blog-mould-removal-bond-clean-perth",
    "title": "Mould in Your Rental? What It Means for Your Bond in Perth",
    "h1": "Mould in Your Rental? What It Means for Your Bond in Perth",
    "meta": "Mould in the bathroom or laundry can cost you bond money. How to treat mould before your exit inspection in Perth, what counts as fair wear and tear, and when you're liable.",
    "read_time": 5,
    "content": """
      <p>Mould is one of the most disputed issues at Perth exit inspections. Tenants often assume it's a building problem — property managers often disagree. Here's how to handle it before your bond inspection so you're not left out of pocket.</p>
      <h2>Is Mould Your Responsibility as a Tenant?</h2>
      <p>It depends on the cause. In Western Australia, mould caused by inadequate ventilation — for example, not using the exhaust fan during showers or leaving wet towels in the bathroom — is generally the tenant's responsibility. Mould caused by a structural defect (a leaking roof, rising damp, or inadequate waterproofing) is the landlord's responsibility.</p>
      <p>In practice, most bathroom mould in Perth rentals is caused by condensation and poor ventilation — which falls on the tenant. Property managers will check for it, and "it was already there" is very hard to prove without photo evidence from the ingoing condition report.</p>
      <h2>Where Mould Is Most Commonly Found</h2>
      <ul class="checklist">
        <li>Shower grout and silicone — the most common location</li>
        <li>Bathroom ceiling, especially around the exhaust fan</li>
        <li>Window tracks and sills in poorly ventilated rooms</li>
        <li>Laundry walls near the washing machine</li>
        <li>Behind furniture in poorly ventilated bedrooms</li>
      </ul>
      <h2>How to Treat Mould Before Your Exit Inspection</h2>
      <p>For surface mould on tiles and grout, a bleach-based mould spray left to dwell for 10–15 minutes then scrubbed with a stiff brush is effective. For grout that has deep mould staining, a commercial tile and grout cleaner or a diluted bleach solution applied repeatedly over a few days can improve the colour significantly.</p>
      <p>For black mould on silicone sealant, surface treatment usually isn't enough — the silicone often needs to be removed and reapplied. This is something a professional bond cleaner can assess and arrange.</p>
      <h2>What Professional Bond Cleaners Do Differently</h2>
      <p>Our cleaners use commercial-grade mould treatment products not available in supermarkets, and have the equipment and technique to treat grout lines properly. Where mould is significant, we'll flag it before the clean so there are no surprises on inspection day.</p>
      <h2>Document Everything</h2>
      <p>If you believe mould was present at the start of your tenancy and wasn't documented in the ingoing condition report, take photos with a date stamp and raise it in writing with your property manager before the exit inspection. This creates a paper trail if there's a dispute.</p>
"""
  },
  {
    "slug": "blog-blind-cleaning-rental-perth",
    "title": "Blind Cleaning for Bond Inspections in Perth — What You Need to Know",
    "h1": "Blind Cleaning for Bond Inspections in Perth — What You Need to Know",
    "meta": "Blind slats are one of the most commonly missed items in Perth bond cleans. How to clean venetian and vertical blinds properly before your exit inspection.",
    "read_time": 4,
    "content": """
      <p>Ask any Perth property manager what gets missed most often in DIY bond cleans, and blind slats come up in the top three every time. They're easy to overlook, time-consuming to do properly, and always checked. Here's how to handle them before your exit inspection.</p>
      <h2>Why Blinds Are Commonly Flagged</h2>
      <p>Dust accumulates on each individual slat over months and years. A quick visual glance at a room won't reveal it — but a property manager running a finger along the slats will. Even in a property that looks spotless, dusty blinds are a quick and easy deduction.</p>
      <h2>Types of Blinds in Perth Rentals</h2>
      <h3>Venetian Blinds (Horizontal Slats)</h3>
      <p>Each slat needs to be wiped individually — both sides. Close the blinds one direction and wipe, then close in the opposite direction and wipe the other side. Use a damp microfibre cloth or a dedicated blind-cleaning tool (available cheaply from hardware stores). For heavy dust buildup, a mild all-purpose cleaner works well.</p>
      <h3>Vertical Blinds</h3>
      <p>Wipe each vane individually with a damp cloth. Start at the top and work down. For fabric verticals, check whether they can be removed and hand-washed — some can, and it's the most thorough option.</p>
      <h3>Roller Blinds</h3>
      <p>Wipe the face of the blind with a damp cloth. Pay attention to the bottom bar and side channels. For fabric roller blinds, spot-clean any marks with a mild detergent.</p>
      <h2>How Long Does It Take?</h2>
      <p>For a typical 3-bedroom Perth home with venetian blinds in each room, thorough blind cleaning takes 45–90 minutes. It's tedious but straightforward. If you're short on time, it's one of the areas where a professional bond cleaner earns their fee — they do it on every job and are fast at it.</p>
      <h2>Don't Forget Curtains</h2>
      <p>If your property has curtains, check the ingoing condition report to see their stated condition. Curtains that are dusty or carry pet hair may need dry cleaning. Your property manager will note any significant deterioration beyond normal use.</p>
"""
  },
  {
    "slug": "blog-bond-cleaning-apartment-perth",
    "title": "Bond Cleaning an Apartment in Perth — What's Different",
    "h1": "Bond Cleaning an Apartment in Perth — What's Different",
    "meta": "Bond cleaning a Perth apartment has specific requirements around balconies, shared areas, and strata obligations. What you need to know before your exit inspection.",
    "read_time": 5,
    "content": """
      <p>Bond cleaning a Perth apartment or unit has a lot in common with cleaning a house — but there are a few specific considerations worth knowing before your exit inspection.</p>
      <h2>What's the Same</h2>
      <p>The REIWA Property Condition Report applies the same way. Your property manager will check every room, every appliance, every cupboard, and every surface using the same checklist as a house. Oven, rangehood, bathroom, blinds, skirting boards — all the same requirements apply.</p>
      <h2>What's Different in an Apartment</h2>
      <h3>Balconies</h3>
      <p>Most Perth apartments have a balcony. It's included in your bond clean scope — floor swept and hosed down, glass or balustrade wiped, any BBQ or outdoor furniture areas cleaned. Don't leave it to the last minute; it's checked.</p>
      <h3>Air Conditioning</h3>
      <p>Split-system air conditioning units are common in Perth apartments and the filters are almost always checked. Remove the filters, wash them in warm soapy water, dry them thoroughly, and replace. The exterior unit housing should also be wiped down.</p>
      <h3>Common Areas</h3>
      <p>Common areas — stairwells, lifts, shared laundries — are managed by the strata company and are not your responsibility to clean. Your obligation ends at your apartment door. However, if you've caused damage or left rubbish in a common area, the strata can charge this back to the owner, who may pursue you.</p>
      <h3>Smaller Footprint, Faster Clean</h3>
      <p>Most Perth apartments are 1–2 bedrooms. A professional bond clean of a 1-bedroom apartment takes 3–5 hours and costs $250–$350. It's a straightforward job when done by someone who does it regularly.</p>
      <h2>Carpets in Apartments</h2>
      <p>Many Perth apartments have a mix of tiles and carpet. Check your lease for carpet steam cleaning requirements. If only one or two rooms are carpeted, the cost for professional steam cleaning is usually $80–$140 — well worth it if your lease requires it.</p>
      <h2>Getting Your Apartment Bond Back</h2>
      <p>The same principles apply as for a house: professional clean, REIWA checklist, bond back guarantee. The smaller size of most apartments means a lower cost and a faster turnaround — contact us for a quote and we'll get back to you within the hour.</p>
"""
  },
  {
    "slug": "blog-fair-wear-and-tear-wa",
    "title": "Fair Wear and Tear in WA — What Landlords Can and Can't Charge For",
    "h1": "Fair Wear and Tear in WA — What Landlords Can and Can't Charge For",
    "meta": "Understanding fair wear and tear in Western Australia. What counts as normal deterioration, what landlords can legitimately deduct from your bond, and how to protect yourself.",
    "read_time": 6,
    "content": """
      <p>One of the most misunderstood aspects of renting in Western Australia is fair wear and tear. Tenants often accept bond deductions they shouldn't, and landlords sometimes claim costs they're not entitled to. Here's a clear explanation of how it works.</p>
      <h2>What Is Fair Wear and Tear?</h2>
      <p>Fair wear and tear refers to the gradual, inevitable deterioration of a property and its contents through normal everyday use over time. In WA, the Residential Tenancies Act 1987 prohibits landlords and property managers from claiming bond money for fair wear and tear.</p>
      <h2>Examples of Fair Wear and Tear (Cannot Be Charged)</h2>
      <ul class="checklist">
        <li>Minor scuff marks on walls from furniture or normal movement</li>
        <li>Small nail holes from hanging pictures</li>
        <li>Carpet worn down in high-traffic areas over a long tenancy</li>
        <li>Faded paint or wallpaper due to sunlight</li>
        <li>Loose door handles or hinges from normal use</li>
        <li>Light scratches on floors from furniture over time</li>
      </ul>
      <h2>Examples of Damage (Can Be Charged)</h2>
      <ul class="checklist">
        <li>Large holes in walls from improper hanging or accidents</li>
        <li>Burns or deep stains on carpet</li>
        <li>Broken tiles, glass, or fixtures</li>
        <li>Pet scratches on doors or floors</li>
        <li>Mould caused by inadequate ventilation</li>
        <li>Unapproved modifications</li>
        <li>Missing or broken keys, remotes, or fobs</li>
      </ul>
      <h2>The Age Factor</h2>
      <p>WA tribunals and courts consider the age and expected lifespan of items when assessing damage claims. Carpet that was already 8 years old at the start of your tenancy has a limited remaining value — even if you caused a stain, the replacement cost cannot be charged at full price. A landlord can only claim the proportional remaining value.</p>
      <h2>How to Protect Yourself</h2>
      <p>The ingoing Property Condition Report is your most important protection. When you move in, document everything thoroughly — note existing marks, stains, scratches, and worn areas. Take photos. If the ingoing report misses something, add it in writing and keep a copy. This creates a baseline that makes it very difficult for a landlord to claim damage that pre-existed your tenancy.</p>
      <h2>If You're Facing an Unfair Deduction</h2>
      <p>Respond in writing, clearly citing the fair wear and tear principle and the Residential Tenancies Act 1987 (WA). If the property manager proceeds with the claim, contact Consumer Protection WA for advice or apply to the Magistrates Court to dispute it.</p>
"""
  },
  {
    "slug": "blog-property-condition-report-wa",
    "title": "The Property Condition Report in WA — A Tenant's Guide",
    "h1": "The Property Condition Report in WA — A Tenant's Guide",
    "meta": "How the REIWA Property Condition Report works in Western Australia, why it's your most important document as a tenant, and how to use it to protect your bond.",
    "read_time": 5,
    "content": """
      <p>The Property Condition Report (PCR) is the most important document in your tenancy. It's the baseline used to assess whether any bond deductions are warranted at the end of your lease — and most bond disputes come down to what's in it.</p>
      <h2>What Is the Property Condition Report?</h2>
      <p>The PCR is a room-by-room assessment of the property's condition at the start of your tenancy. It records the state of walls, floors, ceilings, fixtures, appliances, windows, and outdoor areas — noting any existing damage, marks, or wear. Both the property manager and tenant sign it.</p>
      <p>In Western Australia, property managers are required to provide a completed PCR to the tenant within 7 days of the tenancy commencing. The tenant has 5 days to add comments and return a copy.</p>
      <h2>Why It Matters So Much</h2>
      <p>At the end of your tenancy, your property manager completes an outgoing PCR using the same form. They compare the ingoing and outgoing reports to identify any changes beyond fair wear and tear. Those changes are the basis for any bond claim.</p>
      <p>If the ingoing report doesn't document a mark or stain that was already there when you moved in, you may be charged for it at exit — even though you didn't cause it. The PCR is your protection against this.</p>
      <h2>How to Complete the Ingoing PCR Properly</h2>
      <ul class="checklist">
        <li>Walk through every room carefully — don't rush the process</li>
        <li>Note every mark, stain, scratch, and worn area in writing on the form</li>
        <li>Take photos of everything you note — date-stamped photos are your evidence</li>
        <li>If you find something after the 5-day window, notify your property manager in writing immediately</li>
        <li>Keep a copy of the signed ingoing PCR for the entire duration of your tenancy</li>
      </ul>
      <h2>Requesting a Copy</h2>
      <p>If you no longer have your ingoing PCR, request a copy from your property manager or real estate agency. They are required to keep it and provide it on request. Do this before your exit inspection — you need it for comparison.</p>
      <h2>The PCR and Your Bond Clean</h2>
      <p>A professional bond cleaner uses the REIWA checklist that mirrors the PCR. By cleaning to that standard, you're directly addressing what your property manager will be checking room by room. It's the most reliable way to ensure the outgoing report matches the ingoing one.</p>
"""
  },
  {
    "slug": "blog-bond-dispute-wa",
    "title": "How to Dispute a Bond Deduction in Western Australia",
    "h1": "How to Dispute a Bond Deduction in Western Australia",
    "meta": "Your property manager is claiming part of your bond in WA. Here's how to dispute it — the process, your rights, and how to maximise your chance of getting money back.",
    "read_time": 6,
    "content": """
      <p>Receiving a bond deduction claim after moving out is frustrating — especially when you feel the claim is unfair. In Western Australia, you have clear rights and a straightforward process for disputing it. Here's how it works.</p>
      <h2>Step 1 — Respond in Writing Immediately</h2>
      <p>As soon as you receive a claim, respond in writing (email is fine). State that you dispute the claim and request a breakdown of what is being claimed and why. Ask for the outgoing condition report if you haven't received it.</p>
      <p>Keep your response factual and unemotional. Attach any supporting evidence — photos, receipts for professional cleaning, the ingoing condition report showing pre-existing issues.</p>
      <h2>Step 2 — Negotiate</h2>
      <p>Many bond disputes are resolved at this stage. A property manager claiming $400 for a re-clean on a property where you have a professional cleaning receipt and a bond back guarantee from the cleaner is in a weak position. Present your evidence clearly and offer to discuss.</p>
      <h2>Step 3 — Contact Consumer Protection WA</h2>
      <p>Consumer Protection WA provides free advice on bond disputes and tenancy rights. They can explain the process, help you understand your position, and in some cases assist with conciliation between you and the property manager.</p>
      <p>Phone: 1300 30 40 54 | Website: consumerprotection.wa.gov.au</p>
      <h2>Step 4 — Apply to the Magistrates Court</h2>
      <p>If the property manager lodges a formal claim against your bond with the Bond Administrator, you can contest it through the Magistrates Court of WA. For amounts under $10,000, the process is designed to be accessible without a lawyer.</p>
      <p>You'll need to prepare your evidence: the ingoing PCR, outgoing PCR, professional cleaning receipts, photos taken at move-out, and any written correspondence. The court will assess the evidence and make a binding determination.</p>
      <h2>What Makes a Strong Defence</h2>
      <ul class="checklist">
        <li>Professional bond clean receipt with a bond back guarantee</li>
        <li>Date-stamped photos of the property taken after the clean</li>
        <li>The ingoing PCR showing the issue was pre-existing</li>
        <li>Written correspondence showing you raised the issue promptly</li>
        <li>Evidence that the claimed amount exceeds the actual cost (get competing quotes)</li>
      </ul>
      <h2>Prevention Is Better Than Dispute</h2>
      <p>A professional bond clean with a guarantee is the best way to avoid a dispute entirely. If your property manager flags anything within 72 hours, the cleaner returns and fixes it — so by the time any formal claim process could begin, the issue is already resolved.</p>
"""
  },
  {
    "slug": "blog-same-day-bond-cleaning-perth",
    "title": "Same-Day Bond Cleaning in Perth — Is It Possible?",
    "h1": "Same-Day Bond Cleaning in Perth — Is It Possible?",
    "meta": "Need a bond clean today in Perth? Same-day and urgent bond cleaning is possible — here's how to secure a booking and what to expect when you're in a rush.",
    "read_time": 4,
    "content": """
      <p>Settlement dates change, property managers move inspections forward, and life doesn't always go to plan. Same-day and next-day bond cleaning in Perth is available — but you need to act fast and know what to ask for.</p>
      <h2>Is Same-Day Bond Cleaning Actually Possible?</h2>
      <p>Yes — with caveats. Perth bond cleaners who offer same-day service typically have a small number of spots reserved for urgent bookings, or can reallocate a team if there's a cancellation. The earlier in the day you contact them, the better the chance of securing a same-day slot.</p>
      <p>Weekday bookings are far easier to arrange same-day than Friday or Saturday — the end of the month is particularly hard as every cleaner in Perth is fully booked.</p>
      <h2>What to Have Ready When You Call</h2>
      <ul class="checklist">
        <li>Exact address and access method (key, lockbox code, you'll be present)</li>
        <li>Number of bedrooms and bathrooms</li>
        <li>Whether carpets need steam cleaning</li>
        <li>Whether you have a garage or balcony to include</li>
        <li>Your inspection time — the cleaner needs to finish before it</li>
      </ul>
      <h2>What to Expect With a Same-Day Booking</h2>
      <p>A reputable cleaner can still complete a full REIWA-aligned bond clean in a same-day window — a 2-bedroom unit in 3–5 hours, a 3-bedroom house in 5–7 hours. The work and the guarantee should be exactly the same as a scheduled booking.</p>
      <p>One consideration: if the property has heavy buildup (years of oven grease, severe mould) a single-day clean may require more time than originally estimated. Be upfront about the property's condition when booking.</p>
      <h2>Same-Day Carpet Steam Cleaning</h2>
      <p>This is harder to arrange same-day since it requires specialist equipment and longer drying time (4–8 hours). If your lease requires steam cleaning and you're in a rush, contact us immediately — we'll do our best to coordinate both services.</p>
      <h2>The Most Important Step</h2>
      <p>Contact us now. Same-day spots go to whoever calls first. Fill in the quote form and mark it urgent, or email info@perthbondclean.com directly — we respond within the hour during business hours.</p>
"""
  },
  {
    "slug": "blog-bond-cleaning-after-pets-perth",
    "title": "Bond Cleaning After Pets in Perth — What to Expect",
    "h1": "Bond Cleaning After Pets in Perth — What to Expect",
    "meta": "Renting with pets in Perth means extra scrutiny at the exit inspection. What property managers look for, what costs more, and how to get your full bond back after having pets.",
    "read_time": 5,
    "content": """
      <p>Renting with pets in Perth is increasingly common — but it comes with extra obligations at the end of your tenancy. Property managers look more closely at pet-friendly properties at exit, and there are specific issues that can cost you bond money if not handled properly.</p>
      <h2>What Property Managers Check Extra Carefully After Pets</h2>
      <ul class="checklist">
        <li><strong>Pet hair in carpets</strong> — embedded deep in fibres, regular vacuuming doesn't remove it</li>
        <li><strong>Pet odour</strong> — particularly in carpets, soft furnishings, and curtains</li>
        <li><strong>Scratch marks</strong> — on doors, door frames, timber floors, and skirting boards</li>
        <li><strong>Urine stains</strong> — on carpets and sometimes timber floors</li>
        <li><strong>Backyard damage</strong> — from digging, wear, or mess</li>
        <li><strong>Flea treatment</strong> — many leases with pet permission require professional flea treatment at exit</li>
      </ul>
      <h2>Does Having a Pet Affect My Bond Clean Cost?</h2>
      <p>It can. If the property has significant pet hair in carpets, odour, or requires specialist treatment, professional cleaners may apply a surcharge or requote after assessment. Be upfront when requesting a quote — describe the pet situation honestly so there are no surprises on the day.</p>
      <h2>Carpet Steam Cleaning After Pets</h2>
      <p>Standard carpet steam cleaning addresses most pet hair and mild odour. For heavy pet odour or urine damage, specialist enzyme-based pet odour treatment is needed. This costs more than a standard steam clean but is far more effective — and necessary if you want to avoid bond deductions.</p>
      <h2>Does My Lease Require Flea Treatment?</h2>
      <p>Many Perth leases that permit pets include a clause requiring professional flea treatment at exit. Check your lease carefully. If it's required, arrange it through a licensed pest controller and keep the receipt — your property manager will ask for it.</p>
      <h2>Scratch Marks on Doors and Floors</h2>
      <p>Minor surface scratches may be considered fair wear and tear depending on the length of your tenancy. Significant scratching that goes beyond normal use is damage and can be charged against your bond. Touch-up paint and minor repair can address some door and skirting board scratches before the inspection.</p>
      <h2>Plan Ahead</h2>
      <p>If you've had pets in the property, budget for a higher-cost bond clean than you might otherwise expect. Get a quote that explicitly covers pet hair removal, odour treatment, and any flea treatment required by your lease. A professional bond cleaner experienced with pet properties will know exactly what's needed.</p>
"""
  },
  {
    "slug": "blog-is-professional-bond-cleaning-worth-it",
    "title": "Is Professional Bond Cleaning Worth It in Perth? (Honest Answer)",
    "h1": "Is Professional Bond Cleaning Worth It in Perth? (Honest Answer)",
    "meta": "Should you hire a professional bond cleaner or do it yourself? A straight cost-benefit analysis for Perth renters — when it's worth it and when it might not be.",
    "read_time": 5,
    "content": """
      <p>Professional bond cleaning costs money. DIY is free. So is it actually worth paying for? Here's a straight cost-benefit analysis — not a sales pitch.</p>
      <h2>The Core Numbers</h2>
      <p>A professional bond clean for a 3-bedroom Perth home costs roughly $400–$600. Your bond on a $450/week rental is $1,800. A failed exit inspection resulting in cleaning deductions typically costs $300–$800, sometimes more. The question is: what's the probability that your DIY clean passes the inspection at the same standard as a professional one?</p>
      <h2>When Professional Cleaning Is Clearly Worth It</h2>
      <ul class="checklist">
        <li><strong>You're time-poor.</strong> A 3x2 house takes 8–12 solo hours to clean properly. During a move, that time is almost impossible to find.</li>
        <li><strong>Your property is 3+ bedrooms.</strong> Larger properties have more surface area, more appliances, more blind slats — the risk of missing something increases significantly.</li>
        <li><strong>You have carpet that needs steam cleaning.</strong> Your lease may require a licensed operator. DIY doesn't satisfy that requirement.</li>
        <li><strong>Your property manager is known to be strict.</strong> If you've received routine inspection feedback throughout your tenancy about cleanliness, the exit standard will be high.</li>
        <li><strong>You've had pets in the property.</strong> Pet hair in carpets and pet odour require specialist treatment that consumer products can't fully address.</li>
        <li><strong>Your oven has significant buildup.</strong> Heavy carbonisation is very difficult to shift without commercial-grade products and technique.</li>
      </ul>
      <h2>When DIY Might Be Okay</h2>
      <ul class="checklist">
        <li>Small property (studio or 1-bedroom) in excellent condition</li>
        <li>You're meticulous, have the time, and know what the REIWA checklist covers</li>
        <li>No carpet steam cleaning required by your lease</li>
        <li>A relaxed property manager based on your rental history</li>
      </ul>
      <h2>The Real Decision Factor: The Guarantee</h2>
      <p>The biggest advantage of professional cleaning isn't the clean itself — it's the bond back guarantee. If your property manager flags anything within 72 hours, the cleaner returns and fixes it at no cost. DIY gives you no such safety net. One missed item — a greasy rangehood, dusty blind slats — and you're back negotiating a deduction.</p>
      <h2>The Verdict</h2>
      <p>For most Perth tenants moving out of a 2+ bedroom property, professional bond cleaning is worth it. The cost is predictable, the guarantee is real, and the alternative risk (a portion of your bond) is significantly larger. For a spotless 1-bedroom flat with no carpet, DIY is a reasonable option with our <a href="blog-end-of-lease-cleaning-checklist-perth.html" style="color:var(--green);">REIWA checklist</a> as your guide.</p>
"""
  },
  {
    "slug": "blog-how-to-dispute-bond-deduction-wa",
    "title": "How to Dispute a Bond Deduction in WA — Step by Step",
    "h1": "How to Dispute a Bond Deduction in WA — Step by Step",
    "meta": "Your landlord is trying to keep part of your bond in WA. Here is a clear step-by-step guide to disputing unfair deductions and getting your money back.",
    "read_time": 5,
    "content": """
      <p>Disputing a bond deduction in Western Australia is a structured process. If you have evidence and you act promptly, you have a genuine chance of recovering money that shouldn't have been taken. Here's how to do it.</p>
      <h2>Before You Dispute — Assess Your Position Honestly</h2>
      <p>Before investing time in a dispute, assess whether the claim has merit. Were there genuine cleaning issues? Was there damage beyond fair wear and tear? Is the claimed amount reasonable? If the answer is yes to any of these, a partial concession may be more practical than a full dispute.</p>
      <p>If the claim is for cleaning that you had professionally done, for damage that was already present at the start of your tenancy, or for fair wear and tear, you have a strong position to dispute.</p>
      <h2>Step 1 — Gather Your Evidence</h2>
      <ul class="checklist">
        <li>Ingoing Property Condition Report</li>
        <li>Outgoing Property Condition Report (request a copy if not received)</li>
        <li>Professional cleaning receipts</li>
        <li>Carpet steam cleaning receipt</li>
        <li>Date-stamped photos taken after the clean and before key return</li>
        <li>All written correspondence with the property manager</li>
        <li>Bond back guarantee documentation from your cleaner</li>
      </ul>
      <h2>Step 2 — Write a Formal Dispute Letter</h2>
      <p>Send an email to the property manager stating clearly: you dispute the claim, the specific items you dispute, and your evidence for each. Keep it professional and factual. Attach your evidence. Request a response within 7 days.</p>
      <h2>Step 3 — Contact Consumer Protection WA</h2>
      <p>If the property manager doesn't respond or won't negotiate, contact Consumer Protection WA. They provide free advice and in some cases offer conciliation services. Phone 1300 30 40 54.</p>
      <h2>Step 4 — Magistrates Court Application</h2>
      <p>If the property manager has applied to the Bond Administrator to withhold part of your bond, you can lodge a counterclaim with the Magistrates Court of WA. File at the nearest Magistrates Court, pay the filing fee (around $70–$130 depending on claim amount), and present your evidence. The court makes a binding decision.</p>
      <h2>Timeline</h2>
      <p>Act quickly — bond disputes have time limits. The property manager must apply to the Bond Administrator within 30 days of the end of the tenancy. Respond to any claim promptly and don't let correspondence go unanswered.</p>
"""
  },
  {
    "slug": "blog-bond-cleaning-furnished-property-perth",
    "title": "Bond Cleaning a Furnished Rental in Perth — What's Different",
    "h1": "Bond Cleaning a Furnished Rental in Perth — What's Different",
    "meta": "Bond cleaning a furnished property in Perth has extra requirements beyond the building itself. What you need to address, what the property manager will check, and how to protect your bond.",
    "read_time": 4,
    "content": """
      <p>Furnished rentals in Perth are common in the inner suburbs and short-stay market. When it comes to the exit clean, there's everything a standard bond clean involves — plus the condition of the furniture and fixtures themselves.</p>
      <h2>What's Different in a Furnished Property</h2>
      <p>The ingoing Property Condition Report for a furnished property includes an inventory of every piece of furniture and its condition at the start of the tenancy. At exit, your property manager will check each item on that list for damage, staining, or significant wear beyond normal use.</p>
      <h2>Key Areas of Extra Attention</h2>
      <ul class="checklist">
        <li><strong>Upholstered furniture</strong> — sofas and chairs are checked for stains, pet hair, and odours. Spot cleaning may be needed; for significant staining, professional upholstery cleaning.</li>
        <li><strong>Mattresses</strong> — staining or odour can result in replacement costs. Mattress protectors (often required in furnished rentals) should be laundered.</li>
        <li><strong>Dining tables and chairs</strong> — wiped clean, scratches noted against ingoing condition.</li>
        <li><strong>Bed frames and wardrobes</strong> — dust and marks cleaned, drawers emptied and wiped.</li>
        <li><strong>Whitegoods if included</strong> — fridge (defrosted and wiped inside), washing machine filter cleaned.</li>
        <li><strong>Curtains</strong> — some furnished properties have curtains that require dry cleaning at exit.</li>
      </ul>
      <h2>What You Can't Claim Is Fair Wear and Tear</h2>
      <p>Furniture wears with use — some degree of fading, minor surface marks, and loose joints over a long tenancy is normal. However, stains, burns, significant scratches, and damage from negligence are not fair wear and tear and can be charged. The age of the furniture matters — a 10-year-old sofa cannot be replaced at full cost on your account.</p>
      <h2>Getting a Quote for a Furnished Property</h2>
      <p>When requesting a bond clean quote for a furnished property, be specific: mention it's furnished, describe the key items, and flag anything that needs extra attention. Professional bond cleaners who regularly work on furnished Perth properties know exactly what's checked and can price accordingly.</p>
"""
  },
  {
    "slug": "blog-bond-cleaning-mistakes-perth",
    "title": "The 10 Most Common Bond Cleaning Mistakes Perth Renters Make",
    "h1": "The 10 Most Common Bond Cleaning Mistakes Perth Renters Make",
    "meta": "These bond cleaning mistakes cost Perth renters hundreds of dollars every year. Learn what they are and how to avoid them before your exit inspection.",
    "read_time": 5,
    "content": """
      <p>After handling hundreds of exit cleans across Perth, we see the same mistakes come up again and again. These are the ones that cost tenants the most money — and they're all preventable.</p>
      <h2>1. Cleaning Before Moving Out Fully</h2>
      <p>Cleaning around furniture doesn't count. A property manager will check behind and under everything. The property must be completely empty before the bond clean begins.</p>
      <h2>2. Skipping the Oven Completely</h2>
      <p>Some tenants simply don't clean the oven because it seems too hard. It's always checked and always deducted if dirty. Budget the time or hire a professional.</p>
      <h2>3. Forgetting the Rangehood Filters</h2>
      <p>Greasy rangehood filters are invisible until someone pulls them out — which your property manager will do. Soak them or run them through the dishwasher.</p>
      <h2>4. Wiping Blind Slats as One Unit</h2>
      <p>Running a cloth across closed blinds doesn't clean between the slats. Each one needs to be wiped individually — both sides.</p>
      <h2>5. Missing Cupboard Interiors</h2>
      <p>Inside every kitchen cupboard and drawer gets checked. Crumbs, grease, and old liner paper are common deductions.</p>
      <h2>6. Not Replacing Blown Light Globes</h2>
      <p>Property managers check every light switch. A blown globe is a quick easy note on the exit report. Buy a pack of spares and check every fitting before the inspection.</p>
      <h2>7. Leaving the Garage</h2>
      <p>The garage floor, walls, and door are part of the exit inspection. Many DIY cleaners focus entirely on the interior and forget it exists.</p>
      <h2>8. Not Treating Mould — Just Wiping It</h2>
      <p>Wiping surface mould with a cloth spreads it and leaves behind roots in the grout. Use a proper mould treatment product and dwell time before scrubbing.</p>
      <h2>9. Handing Back Keys Before Getting Written Confirmation</h2>
      <p>Once you've handed back the keys, your access to the property ends. If cleaning issues are found after key return, you can't go back to fix them without the property manager's permission. Walk through and confirm satisfaction before handing the keys over.</p>
      <h2>10. Not Keeping Receipts</h2>
      <p>If you hire a professional cleaner and a dispute arises, your receipt (and the bond back guarantee) is your primary evidence. Keep every receipt until your bond is fully refunded.</p>
"""
  },
  {
    "slug": "blog-move-out-cleaning-timeline-perth",
    "title": "Move-Out Cleaning Timeline for Perth Renters — When to Do What",
    "h1": "Move-Out Cleaning Timeline for Perth Renters — When to Do What",
    "meta": "A week-by-week move-out cleaning timeline for Perth tenants. When to book your bond clean, when to clean, and how to sequence everything for a smooth exit inspection.",
    "read_time": 4,
    "content": """
      <p>The difference between a stressful exit and a smooth one often comes down to timing. Getting the sequencing right — what to do when — means the bond clean happens on an empty property, the inspection happens after the clean, and nothing falls through the cracks.</p>
      <h2>4–6 Weeks Out</h2>
      <ul class="checklist">
        <li>Give formal written notice to your property manager</li>
        <li>Book your removalists — Perth end-of-month slots fill early</li>
        <li>Review your ingoing Property Condition Report</li>
        <li>Note any repairs or touch-ups you want to arrange before exit</li>
        <li>Check your lease for carpet steam cleaning requirements</li>
      </ul>
      <h2>2 Weeks Out</h2>
      <ul class="checklist">
        <li>Book your professional bond clean for 1–2 days before the exit inspection</li>
        <li>Book carpet steam cleaning if required (can usually be bundled with the bond clean)</li>
        <li>Start decluttering — less to move means less to clean around</li>
        <li>Notify utilities providers (electricity, gas, internet) with your move-out date</li>
      </ul>
      <h2>Moving Day</h2>
      <ul class="checklist">
        <li>Complete the full move — everything out of the property</li>
        <li>Do a final sweep for items left in cupboards, under beds, in the garage</li>
        <li>Take out all rubbish including from external bins</li>
      </ul>
      <h2>Bond Clean Day (1–2 Days Before Inspection)</h2>
      <ul class="checklist">
        <li>Professional bond clean completed on empty property</li>
        <li>Carpet steam clean done if applicable</li>
        <li>Check light globes — replace any blown ones</li>
        <li>Take date-stamped photos of every room</li>
      </ul>
      <h2>Inspection Day</h2>
      <ul class="checklist">
        <li>Attend the inspection if possible</li>
        <li>Bring your ingoing condition report and cleaning receipts</li>
        <li>Have all keys, remotes, and fobs ready</li>
        <li>Request a copy of the outgoing condition report</li>
      </ul>
      <h2>Why the Sequence Matters</h2>
      <p>Cleaning before the property is empty means cleaning around furniture — property managers check behind it. Cleaning too far in advance means dust settles back on surfaces before the inspection. One to two days before is the sweet spot: fresh enough to show, done in time to fix anything that needs it.</p>
"""
  },
  {
    "slug": "blog-how-to-clean-walls-bond-inspection",
    "title": "How to Clean Walls for a Bond Inspection in Perth",
    "h1": "How to Clean Walls for a Bond Inspection in Perth",
    "meta": "Scuff marks and stains on walls are a common source of bond deductions in Perth. How to clean walls properly before your exit inspection without damaging the paint.",
    "read_time": 4,
    "content": """
      <p>Walls are checked at every Perth bond inspection. Scuff marks near light switches, fingerprints around door frames, crayon or pen marks from kids, and general grime that builds up over time — all of it gets noted. The good news is that most marks can be addressed with the right technique.</p>
      <h2>What Property Managers Look For</h2>
      <ul class="checklist">
        <li>Scuff marks from furniture or bags near doorways and corners</li>
        <li>Finger and hand marks around light switches and power points</li>
        <li>Marks behind door handles where the door opens against the wall</li>
        <li>Crayon, pen, or marker marks (especially in family homes)</li>
        <li>Grease splatter near the stove (if the kitchen has painted walls)</li>
        <li>Large holes or gouges from picture hooks or shelving</li>
      </ul>
      <h2>The Magic Eraser Method</h2>
      <p>Melamine foam erasers (sold as Magic Erasers or similar) are highly effective on scuff marks and light staining on painted walls. Dampen slightly and rub gently in a circular motion. Test a small hidden area first — on some flat paints they can dull the surface slightly.</p>
      <h2>Sugar Soap for General Grime</h2>
      <p>A sugar soap solution (available from hardware stores) wiped with a cloth or sponge removes general grime and grease without damaging most painted surfaces. Wipe down, then follow with a clean damp cloth to remove residue. This is what professional cleaners use for routine wall cleaning.</p>
      <h2>Touch-Up Paint</h2>
      <p>For marks that won't come off with cleaning, touch-up paint is the answer. Use the same colour as the existing wall — if you don't have the original paint, try to source a matching colour from a paint store. Apply with a small brush or foam roller to blend in. If the existing paint has faded, a touch-up will be visible — in this case, it may be worth painting the entire wall for consistency.</p>
      <h2>What's Fair Wear and Tear on Walls</h2>
      <p>Very minor scuffs and small nail holes from hanging pictures are generally considered fair wear and tear in WA — particularly over a long tenancy. However, significant damage, large holes, or widespread marking is not. When in doubt, clean and touch up rather than leave it and hope for the best.</p>
"""
  },
  {
    "slug": "blog-notice-to-vacate-wa",
    "title": "Notice to Vacate in WA — What Renters Need to Know",
    "h1": "Notice to Vacate in WA — How Much Notice and What the Rules Are",
    "meta": "How much notice do you need to give your landlord in Western Australia? Notice periods for fixed and periodic leases, how to give notice properly, and what happens if you get it wrong.",
    "read_time": 5,
    "content": """
      <p>Getting your notice period right is the first step to a clean exit from your rental in Perth. Give too little notice and you may owe additional rent. Give it in the wrong form and it may not be valid. Here's exactly how it works in Western Australia.</p>
      <h2>Notice Periods in WA</h2>
      <h3>Fixed-Term Lease — End of Lease</h3>
      <p>When a fixed-term lease ends naturally, you are not legally required to give notice — the lease simply ends. However, it's good practice to confirm in writing at least 4 weeks before the end date that you're vacating. This avoids any misunderstanding and gives the property manager time to find a new tenant.</p>
      <h3>Periodic (Month-to-Month) Tenancy</h3>
      <p>If your tenancy has rolled over to a periodic arrangement, you must give at least 21 days' written notice of your intention to vacate. This means 21 days from the day the property manager receives your notice — not 21 days from when you send it.</p>
      <h3>Breaking a Fixed-Term Lease Early</h3>
      <p>If you need to leave before your fixed term ends, you're breaking the lease. You may be liable for: a break fee (if specified in your lease), re-letting fees, and rent until a new tenant is found and the property is re-leased. Some leases include a fixed break fee amount; others calculate it based on time remaining. Check your lease carefully.</p>
      <h2>How to Give Notice Properly</h2>
      <ul class="checklist">
        <li>Give notice in writing — email is acceptable and creates a record</li>
        <li>Address it to the property manager (not just the landlord)</li>
        <li>State your name, property address, and intended vacate date clearly</li>
        <li>Keep a copy with the sent timestamp</li>
      </ul>
      <h2>If Your Property Manager Gives You Notice</h2>
      <p>In WA, a landlord can end a tenancy in specific circumstances: at the end of a fixed term (with 30 days' notice), for renovation or demolition (with appropriate notice), or for breach of the lease. For a periodic tenancy, a landlord must give 60 days' notice without grounds. Notice requirements changed under the 2023 WA tenancy reforms — check the current rules at Consumer Protection WA if you receive a notice.</p>
"""
  },
  {
    "slug": "blog-renters-rights-bond-wa",
    "title": "Renters' Rights Around Bonds in Western Australia",
    "h1": "Renters' Rights Around Bonds in Western Australia",
    "meta": "Your rights as a renter regarding the bond in WA. How bonds are held, what landlords can and cannot deduct, the dispute process, and where to get help.",
    "read_time": 5,
    "content": """
      <p>Your bond is your money — held in trust until the end of your tenancy. Understanding your rights around it is one of the most important things you can do as a Perth renter.</p>
      <h2>How Bonds Are Held in WA</h2>
      <p>In Western Australia, all residential tenancy bonds must be lodged with the Bond Administrator, which is managed by the Department of Mines, Industry Regulation and Safety (DMIRS). Your landlord or property manager cannot hold the bond themselves. They must lodge it within a specific timeframe of receiving it.</p>
      <p>You can confirm your bond is properly lodged by contacting the Bond Administrator directly.</p>
      <h2>Maximum Bond Amount</h2>
      <p>In WA, the maximum bond a landlord can charge is 4 weeks' rent for unfurnished properties and 6 weeks' rent for furnished properties. If you were charged more than this, it's a breach of the Residential Tenancies Act 1987.</p>
      <h2>What Can Be Deducted From Your Bond</h2>
      <p>At the end of a tenancy, a landlord can claim bond money for:</p>
      <ul class="checklist">
        <li>Unpaid rent</li>
        <li>Cleaning costs where the property wasn't returned in a reasonable state of cleanliness</li>
        <li>Damage beyond fair wear and tear</li>
        <li>Outstanding bills (water usage, utilities) specified in the lease</li>
        <li>Costs for replacing items that are missing or damaged</li>
      </ul>
      <h2>What Cannot Be Deducted</h2>
      <ul class="checklist">
        <li>Fair wear and tear from normal use</li>
        <li>Pre-existing damage documented in the ingoing condition report</li>
        <li>Costs the landlord would incur regardless (e.g., repainting after a normal-length tenancy)</li>
        <li>Any amount beyond the actual cost incurred</li>
      </ul>
      <h2>How to Get Your Bond Back</h2>
      <p>Both you and your property manager must agree on the bond disposal. If you agree it should be refunded in full, either party can submit a bond disposal form to DMIRS. If there's a dispute, the matter goes to the Magistrates Court. See our <a href="blog-how-to-get-bond-back-perth.html" style="color:var(--green);">full guide to getting your bond back</a> for step-by-step details.</p>
"""
  },
  {
    "slug": "blog-rangehood-cleaning-bond-perth",
    "title": "Rangehood Cleaning for Bond Inspections in Perth",
    "h1": "Rangehood Cleaning for Bond Inspections — What Perth Property Managers Check",
    "meta": "Greasy rangehood filters are one of the most commonly flagged items at Perth bond inspections. How to clean them properly and what property managers look for.",
    "read_time": 4,
    "content": """
      <p>Rangehood filters accumulate grease invisibly over months of cooking — until a property manager pulls them out at your exit inspection and holds them up. It's a quick, easy deduction that catches a lot of Perth tenants off guard. Here's how to handle it.</p>
      <h2>What Gets Checked</h2>
      <p>Property managers inspect the rangehood thoroughly:</p>
      <ul class="checklist">
        <li>Mesh or baffle filters — removed and checked for grease buildup</li>
        <li>Interior of the rangehood housing — accumulated grease and cooking residue</li>
        <li>Exterior housing and underside — grease and marks</li>
        <li>Fan blades if accessible</li>
      </ul>
      <h2>How to Clean Rangehood Filters</h2>
      <h3>Dishwasher Method (Easiest)</h3>
      <p>Most metal mesh and baffle filters are dishwasher-safe. Place them on the bottom rack, run a hot cycle, and they come out clean. This works well for moderate grease buildup.</p>
      <h3>Soaking Method</h3>
      <p>For heavier grease, fill the sink or a large tub with very hot water and add a cup of dishwashing liquid plus half a cup of baking soda. Submerge the filters and leave for 30–60 minutes. Scrub with a stiff brush, rinse, and dry before replacing. For very stubborn buildup, add a cup of white vinegar to the soak.</p>
      <h3>Degreaser Spray</h3>
      <p>Commercial degreaser sprays (available from hardware stores) applied directly to the filter, left to dwell for 10 minutes, then scrubbed and rinsed are effective for heavy carbonised grease.</p>
      <h2>Cleaning the Rangehood Interior</h2>
      <p>Spray a degreaser or diluted dish soap solution into the housing, leave briefly, then wipe with a cloth. Multiple wipe-throughs are usually needed for older rangehoods. Pay attention to the area directly above the burners — this is where grease accumulates most.</p>
      <h2>Carbon Filters</h2>
      <p>Some ducted rangehoods use carbon filters rather than metal mesh. These cannot be cleaned — they need to be replaced. Carbon filters typically last 3–6 months with regular cooking. Check whether your rangehood has one and whether it needs replacing before your exit inspection.</p>
"""
  },
  {
    "slug": "blog-how-to-clean-shower-screen-bond",
    "title": "How to Clean a Shower Screen for Your Bond Inspection",
    "h1": "How to Clean a Shower Screen for Your Bond Inspection in Perth",
    "meta": "Soap scum and hard water marks on shower screens are one of the top causes of bond deductions in Perth. The products and techniques that actually work.",
    "read_time": 4,
    "content": """
      <p>Shower screens are one of the first things Perth property managers check at an exit inspection — and soap scum and water spotting are almost impossible to hide. The good news is that with the right products and technique, most shower screens can be restored to near-new condition.</p>
      <h2>Why Shower Screens Are So Commonly Flagged</h2>
      <p>Hard water minerals in Perth's water supply — particularly calcium and magnesium — combine with soap residue to form a film that builds up with every shower. Standard bathroom sprays don't cut through it. By the time you move out after a year or more of tenancy, the buildup can be significant.</p>
      <h2>What Actually Works</h2>
      <h3>Acid-Based Glass Cleaner</h3>
      <p>Products containing citric acid or diluted hydrochloric acid are specifically designed for mineral deposits and soap scum on glass. Apply, leave for 5–10 minutes (longer for heavy buildup), scrub with a non-scratch pad, and rinse thoroughly. Wear gloves.</p>
      <h3>White Vinegar Solution</h3>
      <p>Undiluted white vinegar sprayed on the screen and left for 15–20 minutes breaks down mineral deposits effectively for moderate buildup. Scrub with a microfibre cloth, rinse, and dry with a squeegee to prevent re-spotting.</p>
      <h3>Bicarb + Vinegar Paste</h3>
      <p>Mix bicarb soda with enough white vinegar to make a paste. Apply to the screen, leave for 10 minutes, scrub, and rinse. Effective for moderate soap scum and light mineral staining.</p>
      <h2>For Heavy Mineral Deposits</h2>
      <p>Years of untreated hard water deposits require a commercial descaler. Bathroom tile and glass descalers (available from hardware stores) contain stronger acids that dissolve calcium carbonate deposits that household products won't touch. Follow the product instructions carefully and ensure good ventilation.</p>
      <h2>The Finishing Step — Prevent Re-Spotting</h2>
      <p>After cleaning, dry the screen with a clean microfibre cloth and squeegee to remove all water. Any water left to dry will leave mineral spots. If the inspection is the next day, give it one final wipe before the property manager arrives.</p>
      <h2>Shower Door Tracks</h2>
      <p>Don't forget the tracks at the bottom of the shower screen. Soap scum, mould, and hair accumulate in these narrow channels and are always checked. Use an old toothbrush with a cleaning solution to get into the grooves.</p>
"""
  },
  {
    "slug": "blog-carpet-stains-bond-inspection-perth",
    "title": "Carpet Stains and Your Bond Inspection in Perth — What You Need to Know",
    "h1": "Carpet Stains and Your Bond Inspection in Perth — What You Need to Know",
    "meta": "Carpet stains are a major source of bond deductions in Perth. What counts as damage vs fair wear and tear, how to treat common stains, and when professional cleaning is needed.",
    "read_time": 5,
    "content": """
      <p>Carpet is one of the most disputed items at Perth exit inspections. Stains, worn patches, and embedded dirt all get scrutinised — and the cost of carpet cleaning or replacement can be significant. Here's how to approach it.</p>
      <h2>Stains vs Fair Wear and Tear</h2>
      <p>General traffic wear — carpet compressed and slightly faded in high-use areas — is fair wear and tear and cannot be charged to the tenant. Stains, pet damage, burns, and tears are damage and can result in a bond claim.</p>
      <p>The age and quality of the carpet matters. A landlord cannot charge you the full replacement cost of 10-year-old carpet. They can only claim the proportional remaining value based on the carpet's expected lifespan (typically assessed at 10–15 years for residential carpet).</p>
      <h2>Common Stains and How to Treat Them</h2>
      <h3>Red Wine</h3>
      <p>Blot (don't rub) immediately. Apply a mix of cold water and dish soap, blot again. For set stains, a commercial carpet stain remover or a hydrogen peroxide solution (test in a hidden area first) can lighten the mark.</p>
      <h3>Pet Urine</h3>
      <p>Use an enzyme-based cleaner specifically designed for pet urine — it breaks down the proteins causing the odour, which standard cleaners don't address. Blot the area dry after treatment. Steam cleaning alone will not remove pet odour.</p>
      <h3>Coffee and Tea</h3>
      <p>Blot, then apply cold water. Commercial carpet cleaners work well on these stains. Avoid hot water — it sets the stain.</p>
      <h3>Grease</h3>
      <p>Apply baking soda to absorb the grease, leave for 15 minutes, vacuum up. Then apply a small amount of dish soap with cold water, blot, and rinse with cold water.</p>
      <h2>Does Professional Steam Cleaning Remove Stains?</h2>
      <p>Professional steam cleaning significantly reduces or removes many common stains. For deep-set or older stains, the cleaner may apply pre-treatment before the steam process. Pet stains and odour typically require specialist enzyme treatment in addition to or instead of steam cleaning.</p>
      <h2>When to Disclose Before the Inspection</h2>
      <p>If you have a significant carpet stain that won't be fully removed by cleaning, it may be worth disclosing it to your property manager before the inspection rather than hoping it goes unnoticed. Proactively offering to pay for treatment (rather than replacement) is often a better outcome than a full replacement claim after the fact.</p>
"""
  },
  {
    "slug": "blog-cheapest-bond-cleaning-perth",
    "title": "Cheap Bond Cleaning in Perth — What You Get and What You Risk",
    "h1": "Cheap Bond Cleaning in Perth — What You Get and What You Risk",
    "meta": "Looking for cheap bond cleaning in Perth? Here's an honest guide to what the lowest-priced quotes usually mean, and the real cost of getting it wrong at your exit inspection.",
    "read_time": 5,
    "content": """
      <p>There's no shortage of cheap bond cleaning quotes in Perth — a quick search will return options starting from $120. But understanding what those prices actually mean is the difference between saving money and losing your bond.</p>
      <h2>Why Cheap Quotes Exist</h2>
      <p>Very low bond cleaning quotes in Perth usually indicate one or more of the following:</p>
      <ul class="checklist">
        <li><strong>No insurance or ABN</strong> — operating illegally, no protection if something goes wrong</li>
        <li><strong>Hourly rate quoted, not flat-rate</strong> — the price blows out significantly on the day</li>
        <li><strong>Abbreviated checklist</strong> — not following the REIWA standard, key areas skipped</li>
        <li><strong>No guarantee</strong> — if you fail the inspection, you're on your own</li>
        <li><strong>Inexperienced operator</strong> — learning on your property at your bond's expense</li>
        <li><strong>Cash only, no receipt</strong> — no proof of cleaning if a dispute arises</li>
      </ul>
      <h2>The Real Cost of a Cheap Bond Clean</h2>
      <p>A $150 bond clean that results in a failed exit inspection costs you $150 plus the deduction. A typical cleaning deduction from a Perth property manager for a re-clean of a 3-bedroom house is $300–$600. Add the stress, the back-and-forth, and the delay to your bond refund — and the "saving" is anything but.</p>
      <h2>What a Fair Price Looks Like</h2>
      <p>For context on what to expect from a reputable, insured bond cleaner in Perth:</p>
      <ul class="checklist">
        <li>1-bedroom unit: $250–$350</li>
        <li>2-bedroom, 1-bathroom: $320–$420</li>
        <li>3-bedroom, 2-bathroom: $400–$580</li>
        <li>4-bedroom, 2-bathroom: $520–$720</li>
      </ul>
      <p>These prices include the full REIWA checklist, insurance, and a bond back guarantee. Anything significantly below this range warrants careful scrutiny.</p>
      <h2>What to Look for Instead of the Cheapest Price</h2>
      <ul class="checklist">
        <li>Bond back guarantee — in writing</li>
        <li>Public liability insurance confirmed</li>
        <li>REIWA checklist followed</li>
        <li>Flat-rate pricing with no hidden extras</li>
        <li>Verifiable reviews on Google, Hipages, or Oneflare</li>
      </ul>
      <p>The cheapest option isn't always the most expensive in the end. A mid-range price from a reputable, insured cleaner with a strong guarantee is almost always the better value.</p>
"""
  },
  {
    "slug": "blog-end-of-lease-cleaning-tips-perth",
    "title": "End of Lease Cleaning Tips for Perth Renters — From the Professionals",
    "h1": "End of Lease Cleaning Tips for Perth Renters — From the Professionals",
    "meta": "Professional tips for end of lease cleaning in Perth. What to prioritise, common shortcuts that backfire, and how to make sure you pass your exit inspection first time.",
    "read_time": 5,
    "content": """
      <p>After cleaning hundreds of Perth rentals at end of lease, we know exactly what works, what doesn't, and what costs tenants the most money. Here are the most useful tips from people who do this every day.</p>
      <h2>Work From a Written Checklist</h2>
      <p>Cleaning from memory means missing things. Always work from a written checklist aligned with the REIWA Property Condition Report. Our <a href="blog-end-of-lease-cleaning-checklist-perth.html" style="color:var(--green);">complete room-by-room checklist</a> covers every item your property manager will check. Print it and tick off as you go.</p>
      <h2>Do the Oven First</h2>
      <p>Apply oven degreaser first and let it dwell while you clean everything else. By the time you come back to it, the product has done the hard work and the grease wipes off more easily. Don't leave the oven to last — it's the most time-consuming task and you don't want to rush it.</p>
      <h2>Clean Top to Bottom, Back to Front</h2>
      <p>Start with ceiling fans and light fittings, then work down to skirting boards, then floors. Start at the back of each room and work toward the door. This way, you're never dropping dust onto a surface you've already cleaned.</p>
      <h2>The Blind Trick</h2>
      <p>Close venetian blinds all the way in one direction and wipe. Then close them the other way and wipe again. Two passes — both sides of every slat — without having to remove the blinds.</p>
      <h2>Shower Screen — Work Dry Last</h2>
      <p>Clean the shower screen with your chosen product, rinse off, then do a final dry wipe and squeegee as the absolute last step in that bathroom. Any moisture left on glass will dry as spots. A dry microfibre cloth and squeegee after everything else in the room is done gives you a streak-free finish for the inspection.</p>
      <h2>Don't Forget These Commonly Missed Areas</h2>
      <ul class="checklist">
        <li>Inside the dishwasher — filter and spray arms</li>
        <li>Wardrobe tracks at the floor level</li>
        <li>Behind the toilet base</li>
        <li>Under the laundry tub</li>
        <li>Top of the door frames</li>
        <li>Exhaust fan covers in bathrooms</li>
        <li>Skirting boards behind appliances</li>
      </ul>
      <h2>Take Photos After You Finish</h2>
      <p>Once the clean is done, take timestamped photos of every room, the oven, the shower screen, the bathrooms, and the garage. These photos are your evidence if a dispute arises. Store them somewhere you can access them quickly — not just on a phone that might be lost or reset.</p>
"""
  },
]

def build_page(a):
    slug = a["slug"]
    title = a["title"]
    h1 = a["h1"]
    meta = a["meta"].replace('"', '&quot;')
    read_time = a["read_time"]
    content = a["content"]
    header = HEADER.format(
        slug=slug, title=title, h1=h1, meta=meta, read_time=read_time, content=content
    )
    footer = FOOTER.format(slug=slug, title=title.replace('"', '\\"'), meta=meta.replace('"', '\\"'))
    return header + "\n" + footer

for article in ARTICLES:
    filename = article["slug"] + ".html"
    html = build_page(article)
    with open(filename, "w") as f:
        f.write(html)
    print(f"Created: {filename}")

print(f"\nDone. {len(ARTICLES)} files created.")
