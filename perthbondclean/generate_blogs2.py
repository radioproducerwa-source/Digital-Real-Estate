#!/usr/bin/env python3
"""Generate blog post HTML files — batch 2."""

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
        <ul><li><a href="index.html">Home</a></li><li><a href="services.html">Services</a></li><li><a href="about.html">About</a></li><li><a href="blog.html">Blog</a></li><li><a href="contact.html">Contact</a></li></ul>
      </div>
      <div class="footer-suburbs">
        <h4>Suburbs We Serve</h4>
        <ul><li><a href="joondalup.html">Joondalup</a></li><li><a href="subiaco.html">Subiaco</a></li><li><a href="fremantle.html">Fremantle</a></li><li><a href="rockingham.html">Rockingham</a></li><li><a href="baldivis.html">Baldivis</a></li><li><a href="canning-vale.html">Canning Vale</a></li><li><a href="midland.html">Midland</a></li><li><a href="morley.html">Morley</a></li><li><a href="ellenbrook.html">Ellenbrook</a></li><li><a href="mandurah.html">Mandurah</a></li><li><a href="armadale.html">Armadale</a></li><li><a href="cannington.html">Cannington</a></li><li><a href="victoria-park.html">Victoria Park</a></li><li><a href="mount-lawley.html">Mount Lawley</a></li><li><a href="scarborough.html">Scarborough</a></li><li><a href="cottesloe.html">Cottesloe</a></li><li><a href="claremont.html">Claremont</a></li><li><a href="karrinyup.html">Karrinyup</a></li><li><a href="stirling.html">Stirling</a></li><li><a href="bayswater.html">Bayswater</a></li></ul>
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
    "slug": "blog-bond-cleaning-townhouse-perth",
    "title": "Bond Cleaning a Townhouse in Perth — What's Covered",
    "h1": "Bond Cleaning a Townhouse in Perth — What's Covered",
    "meta": "Bond cleaning a Perth townhouse involves stairs, multiple levels, and shared boundary areas. What's included, what costs more, and how to prepare for your exit inspection.",
    "read_time": 4,
    "content": """
      <p>Townhouses are one of the most common property types in the Perth rental market, particularly in the inner and middle suburbs. Bond cleaning a multi-level townhouse has a few specific considerations compared to a single-storey unit or house.</p>
      <h2>What's Different in a Townhouse</h2>
      <h3>Stairs and Landings</h3>
      <p>Stairs accumulate dust and debris on each tread, riser, and on the skirting boards either side. The stair balustrade — whether timber, glass, or metal — also gets checked. Budget extra time for stairs in a DIY clean, or make sure your professional cleaner includes them explicitly.</p>
      <h3>Multiple Bathrooms</h3>
      <p>Most Perth townhouses have an ensuite plus at least one additional bathroom. Each is checked to the same standard — shower screen, grout, toilet, vanity, exhaust fan. More bathrooms mean more time and a slightly higher cleaning cost.</p>
      <h3>Courtyard or Small Outdoor Area</h3>
      <p>Most townhouses have a small courtyard or alfresco area rather than a full backyard. These are included in the exit inspection — swept, free of weeds and debris, any surface staining addressed.</p>
      <h3>Garage</h3>
      <p>Many townhouses include a single or double garage. Garage cleaning is usually priced as an add-on. The floor, walls, and door are all checked.</p>
      <h2>Standard Inclusions</h2>
      <p>Everything in a standard bond clean applies: full kitchen deep clean, all bathrooms, bedrooms with wardrobes, living areas with skirting boards and blinds, window tracks, light fittings, and all floors. The townhouse format doesn't reduce any of these requirements.</p>
      <h2>How Long Does a Townhouse Bond Clean Take?</h2>
      <p>A 3-bedroom, 2-bathroom townhouse typically takes a professional team of 2 around 5–7 hours. With stairs and a garage, add another hour. Professional cleaners working in teams are significantly faster than solo DIY due to parallel work — one person in the kitchen while another does bathrooms.</p>
      <h2>Getting a Quote</h2>
      <p>When requesting a quote, mention it's a townhouse, specify the number of levels, bedrooms, and bathrooms, and note whether you have a garage and courtyard. This ensures the quote is accurate and there are no surprises on the day.</p>
"""
  },
  {
    "slug": "blog-bond-cleaning-4-bedroom-perth",
    "title": "Bond Cleaning a 4-Bedroom Home in Perth — Cost and What's Involved",
    "h1": "Bond Cleaning a 4-Bedroom Home in Perth — Cost and What to Expect",
    "meta": "Bond cleaning a 4-bedroom house in Perth typically costs $520–$720. What's included, how long it takes, carpet cleaning, and how to get the best result at exit inspection.",
    "read_time": 4,
    "content": """
      <p>Larger homes take longer and cost more to bond clean — but the same principles apply. Here's what to expect when bond cleaning a 4-bedroom property in Perth.</p>
      <h2>Typical Cost</h2>
      <p>A professional bond clean for a 4-bedroom, 2-bathroom Perth home typically costs $520–$720. Add $150–$220 for carpet steam cleaning if required by your lease. A garage adds $60–$100. Total with carpets and garage: $730–$1,040 depending on the property's condition and size.</p>
      <p>This is still significantly less than the bond on a 4-bedroom Perth home — typically $2,000–$3,500 or more. The maths strongly favour a professional clean.</p>
      <h2>How Long Does It Take?</h2>
      <p>A professional team of 2 typically takes 6–9 hours for a 4-bedroom, 2-bathroom house. Larger homes — 4 bedrooms plus study, 3 bathrooms, double garage — can take a full day. Our teams work in parallel to complete the job without cutting corners.</p>
      <h2>What's Included</h2>
      <p>All rooms and areas to REIWA standard:</p>
      <ul class="checklist">
        <li>Full kitchen including oven, rangehood, all cupboards</li>
        <li>All 2+ bathrooms to the same high standard</li>
        <li>All 4 bedrooms with wardrobes, blinds, skirting boards</li>
        <li>Living, dining, and family areas</li>
        <li>All windows internal, all floors vacuumed and mopped</li>
      </ul>
      <h2>The Most Important Areas in a Large Home</h2>
      <p>In a 4-bedroom property, the sheer volume of surface area means more opportunities for something to be missed. The areas that get deducted most often in larger Perth homes:</p>
      <ul class="checklist">
        <li>Secondary bathrooms and ensuites — often used less but checked equally</li>
        <li>Wardrobes in spare bedrooms — used for storage and often skipped</li>
        <li>Window tracks in multiple rooms accumulate a lot of debris</li>
        <li>Outdoor entertaining areas and alfresco</li>
      </ul>
      <h2>Book Early</h2>
      <p>A full-day booking for a large home needs to be secured at least 2 weeks in advance, especially at month-end. Contact us for a fixed-price quote — we'll confirm the price before the clean begins.</p>
"""
  },
  {
    "slug": "blog-bond-cleaning-outdoor-areas-perth",
    "title": "Bond Cleaning Outdoor Areas in Perth — What Gets Checked",
    "h1": "Bond Cleaning Outdoor Areas in Perth — What Property Managers Check",
    "meta": "Outdoor areas are included in Perth bond inspections. What property managers check in the backyard, alfresco, balcony, and garage, and how to get them inspection-ready.",
    "read_time": 4,
    "content": """
      <p>Many Perth tenants focus their bond clean on the interior of the property and leave outdoor areas as an afterthought. But property managers check every part of the property — and an untidy backyard or grimy balcony can cost you just as much as a dirty oven.</p>
      <h2>Backyard and Garden</h2>
      <p>The garden doesn't need to be immaculate, but it needs to be in a reasonable condition consistent with how it was described in the ingoing report. Property managers check:</p>
      <ul class="checklist">
        <li>Lawns mowed and edged</li>
        <li>Garden beds free of excessive weeds</li>
        <li>Leaves and debris cleared from paths and garden areas</li>
        <li>No rubbish or personal items left behind</li>
        <li>Garden hose and fittings still present if listed in the ingoing report</li>
      </ul>
      <h2>Alfresco and Outdoor Entertaining</h2>
      <ul class="checklist">
        <li>Floor swept and pressure-washed or scrubbed if stained</li>
        <li>Outdoor ceiling fans dusted if present</li>
        <li>BBQ area cleaned — grill plates, surrounding surfaces</li>
        <li>Outdoor light fittings wiped</li>
        <li>Shade sail or pergola structure free of significant cobwebs and debris</li>
      </ul>
      <h2>Balcony (Apartments and Townhouses)</h2>
      <ul class="checklist">
        <li>Floor swept and mopped or hosed</li>
        <li>Glass balustrade or railing cleaned — no water marks or fingerprints</li>
        <li>Any built-in storage wiped out</li>
        <li>Outdoor power points wiped</li>
      </ul>
      <h2>Garage</h2>
      <ul class="checklist">
        <li>Floor swept — oil stains treated where possible</li>
        <li>Walls wiped for dust and marks</li>
        <li>Garage door cleaned inside and out</li>
        <li>Remote controls left (and working)</li>
        <li>Any shelving wiped down</li>
      </ul>
      <h2>The Clothesline</h2>
      <p>Small but checked — wipe the clothesline arms and line with a damp cloth. It sounds minor but property managers do look.</p>
      <h2>Professional Coverage</h2>
      <p>When getting a bond clean quote, confirm which outdoor areas are included. Standard bond clean quotes typically include alfresco and balcony. Garage, backyard, and garden are usually add-ons — confirm in writing so there's no confusion on the day.</p>
"""
  },
  {
    "slug": "blog-air-conditioning-cleaning-bond-perth",
    "title": "Air Conditioning Cleaning for Bond Inspections in Perth",
    "h1": "Air Conditioning Cleaning for Bond Inspections in Perth",
    "meta": "Air conditioning filters are checked at Perth bond inspections. How to clean split system and ducted aircon filters, what property managers look for, and when replacement is needed.",
    "read_time": 4,
    "content": """
      <p>Perth's climate means air conditioning runs hard — and dirty AC filters are a commonly noted item on exit condition reports. It's a quick clean that most tenants either skip or do poorly. Here's what's required.</p>
      <h2>What Gets Checked</h2>
      <p>Property managers look at:</p>
      <ul class="checklist">
        <li>Indoor unit filter — dusty or clogged filters are the most common issue</li>
        <li>Indoor unit housing — exterior panel wiped clean</li>
        <li>Vents and louvres — dust buildup visible from the floor</li>
        <li>Outdoor condenser unit — exterior wiped and free of debris</li>
      </ul>
      <h2>How to Clean a Split System Filter</h2>
      <ol style="color:var(--dark);padding-left:1.4em;line-height:2.2;">
        <li>Switch the unit off at the wall</li>
        <li>Open the front panel — it usually clips or slides open</li>
        <li>Remove the filter panels — they slide or clip out</li>
        <li>Take them outside and tap gently to remove loose dust</li>
        <li>Wash with warm water and mild dish soap — rinse thoroughly</li>
        <li>Allow to dry completely before replacing — a damp filter put back into a unit can cause mould</li>
        <li>Wipe the interior of the unit with a dry cloth</li>
        <li>Wipe the exterior panel and louvres</li>
      </ol>
      <h2>Ducted Air Conditioning</h2>
      <p>For ducted systems, the return air filter is usually located in a ceiling vent in the main living area or hallway. It looks like a large grille. Unclip, remove the filter, wash, dry, and replace. The supply vents throughout the house should also be wiped clean of dust.</p>
      <h2>When Filters Need Replacing</h2>
      <p>Most residential AC filters can be washed multiple times before needing replacement. If a filter is torn, has holes, or is so clogged that washing doesn't restore it, it needs replacing. Filters are inexpensive ($10–$30 from appliance stores or online) and are worth replacing rather than arguing about at exit.</p>
      <h2>Professional Cleaning</h2>
      <p>If the air conditioning system has been running for years without filter cleaning and there's significant mould or buildup inside the unit, a professional AC clean (separate to a bond clean) may be needed. Costs range from $80–$150 per unit. For a straightforward filter clean, it's included as part of our standard bond cleaning service.</p>
"""
  },
  {
    "slug": "blog-skirting-boards-bond-clean-perth",
    "title": "Skirting Board Cleaning for Perth Bond Inspections",
    "h1": "Skirting Board Cleaning for Perth Bond Inspections — Why It Matters",
    "meta": "Dusty skirting boards are one of the most commonly missed items in Perth bond cleans. How to clean them properly and make sure you don't lose bond money on something so simple.",
    "read_time": 3,
    "content": """
      <p>Skirting boards are easy to overlook — they're low, they're behind furniture, and in day-to-day life nobody really looks at them. But property managers specifically check them at exit inspections, and a band of dust along the bottom of every room is a quick easy deduction.</p>
      <h2>Why Skirting Boards Accumulate So Much Dust</h2>
      <p>Skirting boards sit at floor level where air currents deposit dust. In Perth's dry climate, fine dust settles quickly and compresses into a grey film along the top and face of the boards. Regular mopping doesn't clean them — you need to wipe them separately.</p>
      <h2>How to Clean Skirting Boards Properly</h2>
      <p>Use a damp microfibre cloth or a slightly damp flat mop head. Wipe along the top edge, the face, and the junction with the floor. For painted skirting boards, avoid soaking them — excess moisture can cause the paint to bubble or lift.</p>
      <p>For marks or scuffs, a small amount of sugar soap on a cloth will lift most staining without damaging the paint. A magic eraser works well on black scuff marks.</p>
      <h2>Don't Forget Behind Furniture</h2>
      <p>The skirting boards behind the fridge, washing machine, and other heavy appliances are just as subject to inspection as the visible ones. Pull appliances out before the clean and make sure the boards behind them are wiped.</p>
      <p>In bedrooms, the skirting boards behind wardrobes and under bed bases are checked. Move furniture out before the bond clean — or make sure it's already removed before the cleaners arrive.</p>
      <h2>Corners and Joints</h2>
      <p>Dust accumulates most heavily in the corners where two skirting boards meet. Use a dry brush or vacuum attachment to clear the corner first, then wipe with a damp cloth.</p>
      <h2>When Are Skirting Boards Considered Damaged?</h2>
      <p>Scuff marks from furniture, particularly along the face of skirting boards in hallways and doorways, can accumulate over a tenancy. Light marks are fair wear and tear. Significant gouging, chips, or broken sections may result in a repair claim. Touch-up paint can address minor surface marks.</p>
"""
  },
  {
    "slug": "blog-light-fittings-bond-clean-perth",
    "title": "Cleaning Light Fittings and Ceiling Fans for Your Perth Bond Inspection",
    "h1": "Cleaning Light Fittings and Ceiling Fans for Your Perth Bond Inspection",
    "meta": "Dusty ceiling fans and light fittings are always checked at Perth exit inspections. How to clean them safely and what property managers look for.",
    "read_time": 3,
    "content": """
      <p>Ceiling fans and light fittings are at eye level when a property manager walks through your property — and a thick band of dust on fan blades or dead insects inside light covers is an easy note on the exit report.</p>
      <h2>Ceiling Fans</h2>
      <p>Ceiling fan blades accumulate a thick layer of dust on their upper face that's invisible from below but visible when the fan moves — and property managers know to look. Clean both sides of each blade with a damp microfibre cloth. Use a step ladder to reach safely.</p>
      <p>Wipe the motor housing, the pull chains, and the underside of the blade brackets. In Perth's dust-prone climate, this can take longer than expected — allow 10–15 minutes per fan for a thorough job.</p>
      <h2>Light Covers and Diffusers</h2>
      <p>Frosted plastic or glass light covers trap dead insects and dust over time. Remove the cover (most unscrew or clip off), tip out any insects, wash with warm soapy water, dry thoroughly, and replace. Don't put a wet cover back onto the fitting.</p>
      <h2>Exposed Bulb Fittings</h2>
      <p>For pendant lights and exposed bulb fittings, wipe the fitting itself with a dry cloth. Check that the bulb is working — a blown bulb in an otherwise-clean fitting is still noted on the exit report.</p>
      <h2>Bathroom Exhaust Fans</h2>
      <p>Exhaust fan covers in bathrooms and laundries accumulate significant dust, often mixed with moisture. Remove the cover, wash it, dry it, and wipe the visible part of the fan housing before replacing. This is one of the most commonly missed items in DIY bond cleans.</p>
      <h2>Safety Notes</h2>
      <p>Always turn off the light at the switch before cleaning fittings. For high ceilings or hard-to-reach fittings, use a proper step ladder — don't stand on chairs or benches. If a fitting is unusually difficult to access safely, a professional cleaner will have the equipment and experience to handle it.</p>
"""
  },
  {
    "slug": "blog-garage-cleaning-bond-inspection-perth",
    "title": "Garage Cleaning for Perth Bond Inspections — What Gets Checked",
    "h1": "Garage Cleaning for Perth Bond Inspections — What Property Managers Check",
    "meta": "The garage is included in Perth bond inspections. What property managers check, how to treat oil stains on concrete, and what counts as fair wear and tear in a garage.",
    "read_time": 4,
    "content": """
      <p>The garage is one of the most neglected areas in a bond clean. Tenants often spend hours on bathrooms and kitchens, then give the garage a quick sweep and call it done. Property managers notice, and garage issues can result in deductions on an otherwise strong exit report.</p>
      <h2>What Gets Checked in the Garage</h2>
      <ul class="checklist">
        <li>Concrete floor — swept clean and oil stains treated</li>
        <li>Walls — dust and marks wiped</li>
        <li>Garage door — inside and outside cleaned</li>
        <li>Ceiling — cobwebs cleared</li>
        <li>Any built-in shelving — wiped down</li>
        <li>Garage door remotes — present and working</li>
        <li>Manual lock and key if applicable</li>
      </ul>
      <h2>Oil Stains on Concrete</h2>
      <p>Oil stains on garage floors are extremely common and one of the most contentious issues. If the oil stains were already there when you moved in and documented in the ingoing condition report, they cannot be charged to you. If they appeared during your tenancy, you may be liable for treatment.</p>
      <p>To treat fresh oil stains: pour kitty litter or baking soda over the stain and leave for several hours to absorb the oil, then sweep up. Apply a degreaser, scrub with a stiff brush, and rinse. Older set stains are harder to fully remove — a commercial concrete degreaser or caustic soda solution (follow safety directions carefully) can lighten them significantly.</p>
      <h2>Fair Wear and Tear in a Garage</h2>
      <p>General dustiness, minor marks on walls from parking, and light surface staining on concrete over a long tenancy are fair wear and tear. Significant oil contamination, damage to the garage door mechanism, or broken shelving are damage and can be claimed.</p>
      <h2>Is Garage Cleaning Included in a Standard Bond Clean?</h2>
      <p>Most Perth bond cleaning companies price the garage as an add-on — typically $60–$100 for a single-car garage. Confirm when getting your quote whether it's included or separate. If you have a double garage or there's significant cleanup needed, mention this when booking.</p>
"""
  },
  {
    "slug": "blog-bond-cleaning-studio-apartment-perth",
    "title": "Bond Cleaning a Studio Apartment in Perth — Cost and What to Expect",
    "h1": "Bond Cleaning a Studio Apartment in Perth — Cost and What to Expect",
    "meta": "Bond cleaning a studio apartment in Perth costs $200–$300 and takes 2–4 hours. What's included, how long it takes, and whether you can do it yourself.",
    "read_time": 3,
    "content": """
      <p>Studio apartments are the smallest bond cleaning job in Perth — but the same REIWA standards apply as for a five-bedroom house. Property managers don't lower their expectations because the property is small.</p>
      <h2>Typical Cost</h2>
      <p>A professional bond clean for a Perth studio apartment typically costs $200–$300, depending on the condition and whether add-ons like carpet steam cleaning are needed. It's the most affordable bond clean available, and the cost is easily justified by the bond protection it provides.</p>
      <h2>How Long Does It Take?</h2>
      <p>A studio apartment in good condition: 2–4 hours for a professional cleaner. A studio in poor condition with buildup in the kitchen and bathroom: up to 5 hours. Solo DIY typically takes 4–8 hours depending on how meticulous you are.</p>
      <h2>What's Included</h2>
      <p>The same checklist as any property:</p>
      <ul class="checklist">
        <li>Kitchen: oven, cooktop, rangehood, cupboards, sink, benchtops</li>
        <li>Bathroom: shower screen or bath, toilet, vanity, exhaust fan</li>
        <li>Living/sleeping area: wardrobe (if present), skirting boards, blinds, window tracks</li>
        <li>All floors vacuumed and mopped</li>
        <li>Light fittings and ceiling fan if present</li>
      </ul>
      <h2>Can I DIY a Studio Bond Clean?</h2>
      <p>Of all Perth rental properties, a studio is where DIY is most feasible. The footprint is small, there's limited surface area to cover, and it can realistically be cleaned thoroughly in a day. Use our <a href="blog-end-of-lease-cleaning-checklist-perth.html" style="color:var(--green);">full REIWA checklist</a> and work methodically.</p>
      <p>That said, even a studio will cost you money if the oven, shower screen, or rangehood aren't properly cleaned. If you're short on time or not confident in your cleaning standard, a professional clean for $200–$300 is worth it for the guarantee alone.</p>
"""
  },
  {
    "slug": "blog-bond-cleaning-vs-spring-cleaning",
    "title": "Bond Cleaning vs Spring Cleaning — Key Differences Explained",
    "h1": "Bond Cleaning vs Spring Cleaning — What's the Same and What's Very Different",
    "meta": "Bond cleaning and spring cleaning both involve a thorough clean — but they are very different in scope, standard, and purpose. Here's what sets them apart.",
    "read_time": 4,
    "content": """
      <p>Perth tenants sometimes assume a spring clean of their rental will be sufficient for a bond inspection. It won't be — and understanding why can save you a significant bond deduction.</p>
      <h2>The Purpose Is Different</h2>
      <p>A spring clean is done for your own benefit — to freshen up a home you're living in. You choose what to clean and how thoroughly. A bond clean is done to satisfy a third party — your property manager — against a specific documented standard. There's no personal discretion involved.</p>
      <h2>The Standard Is Different</h2>
      <p>Spring cleaning typically means cleaning visible surfaces to a comfortable standard. Bond cleaning means cleaning every surface, appliance interior, cupboard interior, blind slat, and skirting board to a standard that matches the ingoing condition report — regardless of whether you'd personally notice the difference.</p>
      <h2>The Checklist Is Different</h2>
      <p>Spring cleaning has no checklist — you clean what bothers you. Bond cleaning follows the REIWA Property Condition Report, which is room-by-room and item-by-item. Every entry on that document will be checked. If you haven't addressed it, it gets noted.</p>
      <h2>What Spring Cleaning Misses</h2>
      <ul class="checklist">
        <li>Inside every kitchen cupboard and drawer</li>
        <li>Oven racks, door glass, and rubber seal</li>
        <li>Rangehood filter interior</li>
        <li>Individual blind slats — both sides</li>
        <li>Wardrobe interiors and tracks</li>
        <li>Window sliding tracks</li>
        <li>Behind and under heavy appliances</li>
        <li>Exhaust fan covers</li>
      </ul>
      <h2>Can I Do a Spring Clean as My Bond Clean?</h2>
      <p>If you do a spring clean and also cover every item on the REIWA checklist to the standard required — yes. But at that point, you've done a bond clean, not a spring clean. The difference is the checklist and the standard, not the label.</p>
      <p>If you're using a regular spring clean approach and hoping it's thorough enough, the risk is real. Property managers in Perth are experienced at identifying what's been cleaned versus what's been maintained — and the REIWA checklist exists specifically to close the gap.</p>
"""
  },
  {
    "slug": "blog-end-of-lease-cleaning-guide-perth",
    "title": "The Complete End of Lease Cleaning Guide for Perth Renters",
    "h1": "The Complete End of Lease Cleaning Guide for Perth Renters (2025)",
    "meta": "Everything Perth renters need to know about end of lease cleaning in 2025. What's required, what it costs, how to choose a cleaner, and how to get your full bond back.",
    "read_time": 8,
    "content": """
      <p>End of lease cleaning in Perth is one of the most important tasks in your moving-out process. Done well, it's the difference between getting your full bond back and losing hundreds of dollars. This guide covers everything you need to know.</p>
      <h2>What Is End of Lease Cleaning?</h2>
      <p>End of lease cleaning — also called bond cleaning or vacate cleaning — is a comprehensive deep clean of a rental property carried out when a tenant moves out. It's designed to restore the property to the condition recorded in the ingoing Property Condition Report, which was completed when you first moved in.</p>
      <h2>Is It Legally Required?</h2>
      <p>Not in the sense that you must hire a professional. But the Residential Tenancies Act 1987 (WA) requires you to return the property in a reasonable state of cleanliness. If your lease specifies professional cleaning or carpet steam cleaning, those lease terms are legally binding.</p>
      <h2>What Does It Cover?</h2>
      <p>A REIWA-aligned end of lease clean covers every area of the property:</p>
      <ul class="checklist">
        <li>Kitchen: oven, rangehood, all cupboards inside and out, benchtops, sink, dishwasher</li>
        <li>Bathrooms: shower screen, grout, toilet, vanity, exhaust fans</li>
        <li>All rooms: skirting boards, blind slats, window tracks, wardrobes, light fittings</li>
        <li>Floors: vacuumed and mopped throughout</li>
        <li>Outdoor areas: balcony, alfresco, garage</li>
      </ul>
      <h2>How Much Does It Cost in Perth?</h2>
      <p>Average prices for 2025:</p>
      <ul class="checklist">
        <li>Studio / 1-bedroom: $250–$350</li>
        <li>2-bedroom, 1-bathroom: $320–$420</li>
        <li>3-bedroom, 2-bathroom: $400–$580</li>
        <li>4-bedroom, 2-bathroom: $520–$720</li>
        <li>5+ bedroom: $700–$1,000+</li>
      </ul>
      <p>Carpet steam cleaning is typically $80–$220 extra. See our <a href="blog-bond-cleaning-cost-perth.html" style="color:var(--green);">full 2025 price guide</a> for more detail.</p>
      <h2>DIY vs Professional</h2>
      <p>For most Perth tenants, a professional clean is the more cost-effective choice when you factor in the time required, the risk of missing REIWA checklist items, and the absence of a guarantee on DIY work. For a small, well-maintained property with a flexible timeline, DIY is viable. See our <a href="blog-diy-bond-clean-perth.html" style="color:var(--green);">full DIY vs professional analysis</a>.</p>
      <h2>How to Choose a Cleaner</h2>
      <p>Look for: a bond back guarantee (72-hour minimum), public liability insurance, police-checked cleaners, REIWA checklist confirmation, flat-rate pricing, and verifiable reviews. Read our <a href="blog-how-to-choose-bond-cleaner-perth.html" style="color:var(--green);">full guide to choosing a Perth bond cleaner</a>.</p>
      <h2>When to Book</h2>
      <p>At least 1–2 weeks before your move-out date. The clean should happen 1–2 days before the exit inspection — after the property is fully vacated.</p>
      <h2>After the Clean</h2>
      <p>Take date-stamped photos of every room. Replace any blown light globes. Attend the exit inspection with your cleaning receipt, ingoing condition report, and keys. If any cleaning issue is raised, your bond back guarantee covers the re-clean at no cost.</p>
"""
  },
  {
    "slug": "blog-how-to-prevent-bond-deductions-perth",
    "title": "How to Prevent Bond Deductions in Perth — A Practical Guide",
    "h1": "How to Prevent Bond Deductions in Perth — A Practical Guide",
    "meta": "The most effective ways to prevent bond deductions in Perth. From the ingoing inspection to the exit clean — what you can do throughout your tenancy to protect your full bond.",
    "read_time": 5,
    "content": """
      <p>Bond deductions are largely preventable. The tenants who get their full bond back consistently aren't lucky — they've taken specific steps throughout their tenancy that protect them at exit. Here's what those steps are.</p>
      <h2>At Move-In: The Ingoing Condition Report</h2>
      <p>The ingoing Property Condition Report is your single most important protective document. Complete it thoroughly:</p>
      <ul class="checklist">
        <li>Walk through every room carefully before signing anything</li>
        <li>Note every mark, stain, scratch, and pre-existing issue in writing</li>
        <li>Take date-stamped photos of everything you note</li>
        <li>If you find something after the 5-day addition period, notify your property manager in writing immediately</li>
        <li>Keep a copy of the signed ingoing PCR for the entire tenancy</li>
      </ul>
      <h2>During the Tenancy</h2>
      <ul class="checklist">
        <li>Report maintenance issues promptly in writing — a leaking shower that causes mould is not your responsibility if you reported it</li>
        <li>Ventilate bathrooms during and after showers — exhaust fan on, window open if possible</li>
        <li>Clean the oven every few months rather than leaving it to build up over years</li>
        <li>Use furniture pads under chairs and tables to prevent floor scratches</li>
        <li>Fix minor damage — a small hole from a picture hook is far cheaper to repair yourself than to have the landlord arrange it and charge you</li>
        <li>Keep all correspondence with your property manager in writing</li>
      </ul>
      <h2>At Move-Out: The Bond Clean</h2>
      <p>A professional bond clean with a REIWA-aligned checklist and a bond back guarantee is the most effective single action you can take to prevent deductions. It addresses the cleaning standard comprehensively and gives you a guaranteed safety net if anything is missed.</p>
      <h2>At the Exit Inspection</h2>
      <ul class="checklist">
        <li>Attend the inspection if possible</li>
        <li>Bring the ingoing condition report and cleaning receipts</li>
        <li>Take photos before handing back the keys</li>
        <li>Raise any disputes in writing promptly — don't let claims go unanswered</li>
      </ul>
      <h2>The Bottom Line</h2>
      <p>Most bond deductions in Perth come from three things: cleaning standard, undocumented pre-existing damage, and unreported maintenance issues. Address all three proactively and the exit process becomes significantly smoother.</p>
"""
  },
  {
    "slug": "blog-exit-condition-report-perth",
    "title": "The Exit Condition Report in Perth — What It Is and What Happens",
    "h1": "The Exit Condition Report in Perth — What It Is and What to Expect",
    "meta": "The exit condition report is completed at the end of your Perth tenancy and compared to the ingoing report. How it works, what gets noted, and how to prepare.",
    "read_time": 4,
    "content": """
      <p>The exit condition report is the document your property manager completes when you vacate your Perth rental. It's compared directly against the ingoing condition report signed at the start of your tenancy — and any differences are the basis for any bond claim.</p>
      <h2>What Is the Exit Condition Report?</h2>
      <p>It's the outgoing version of the REIWA Property Condition Report — the same form completed at the start of your tenancy. The property manager walks through every room and records the condition of walls, floors, ceilings, fixtures, appliances, blinds, carpets, and outdoor areas.</p>
      <h2>Who Completes It?</h2>
      <p>Your property manager or their representative completes it during the exit inspection. You have the right to be present, and it's strongly recommended that you attend — it allows you to respond to any concerns in real time.</p>
      <h2>What Happens After It's Completed?</h2>
      <p>The property manager compares the outgoing report to the ingoing report. Any deterioration beyond fair wear and tear can result in a bond claim. If both parties agree the property is in satisfactory condition, the bond disposal process can begin and you'll receive your bond refund.</p>
      <p>If the property manager finds issues, they'll notify you and explain what deductions they intend to claim. You then have the right to negotiate, rectify, or dispute.</p>
      <h2>How to Prepare</h2>
      <ul class="checklist">
        <li>Complete a thorough bond clean 1–2 days before the inspection</li>
        <li>Walk through yourself with the ingoing report before the inspection</li>
        <li>Replace all blown light globes</li>
        <li>Have all keys, remotes, and fobs ready</li>
        <li>Bring your cleaning receipts and the ingoing condition report</li>
        <li>Take date-stamped photos immediately after the clean</li>
      </ul>
      <h2>If You Disagree With the Exit Report</h2>
      <p>You are entitled to add your own comments and note any disagreements on the exit condition report. Do this in writing at the inspection. If the property manager proceeds with a claim you dispute, follow the dispute process through Consumer Protection WA or the Magistrates Court. See our <a href="blog-bond-dispute-wa.html" style="color:var(--green);">full bond dispute guide</a>.</p>
"""
  },
  {
    "slug": "blog-renting-perth-tips",
    "title": "Renting in Perth — Tips for New Tenants to Protect Their Bond",
    "h1": "Renting in Perth for the First Time — How to Protect Your Bond From Day One",
    "meta": "Tips for new renters in Perth on how to protect your bond from the start. The ingoing inspection, what to document, maintenance reporting, and how to set yourself up for a smooth exit.",
    "read_time": 5,
    "content": """
      <p>If you're renting in Perth for the first time, your bond is typically four weeks' rent — a significant sum of money. Protecting it starts on your first day in the property, not on your last. Here's what first-time renters need to know.</p>
      <h2>Understand What the Bond Is For</h2>
      <p>Your bond is a security deposit held by the WA Bond Administrator. It's not the landlord's money — it's yours, held in trust. At the end of your tenancy, it's returned to you unless there are legitimate claims for unpaid rent, cleaning beyond a reasonable standard, or damage beyond fair wear and tear.</p>
      <h2>The Ingoing Inspection Is Critical</h2>
      <p>Before you sign off on the ingoing Property Condition Report, walk through the property thoroughly. Document every mark, stain, scratch, and worn area — in writing on the form and with date-stamped photos. This documentation is your protection when you leave. Without it, you could be charged for damage that pre-existed your tenancy.</p>
      <h2>Report Maintenance Issues in Writing</h2>
      <p>If something breaks, leaks, or stops working properly — report it to your property manager in writing (email) promptly. This creates a record that the issue wasn't caused by your negligence. A leaking shower that causes mould over three years is the landlord's responsibility if you reported it — and your responsibility if you didn't.</p>
      <h2>Keep Your Lease and All Correspondence</h2>
      <p>Keep your lease agreement, all email correspondence with your property manager, receipts for any repairs you arrange, and the ingoing condition report. Store them somewhere accessible for the duration of your tenancy.</p>
      <h2>Understand Fair Wear and Tear</h2>
      <p>Normal use of a property causes gradual deterioration — minor wall scuffs, carpet wear, small nail holes. This is fair wear and tear and cannot be charged to you. Understanding this distinction prevents you from accepting deductions you shouldn't pay. See our <a href="blog-fair-wear-and-tear-wa.html" style="color:var(--green);">fair wear and tear guide</a> for full details.</p>
      <h2>Plan Your Exit Early</h2>
      <p>Don't leave the exit clean to the last minute. Book a professional bond cleaner 2 weeks before your move-out date, attend the exit inspection, and have your documentation ready. A smooth exit is planned, not improvised.</p>
"""
  },
  {
    "slug": "blog-how-to-clean-grout-perth",
    "title": "How to Clean Grout for Your Bond Inspection in Perth",
    "h1": "How to Clean Grout for Your Bond Inspection in Perth",
    "meta": "Dirty or mouldy grout is one of the most commonly flagged items at Perth exit inspections. The products and techniques that actually work on bathroom and kitchen grout.",
    "read_time": 4,
    "content": """
      <p>Grout is porous and stains easily — and once it's discoloured or mouldy, it's one of the hardest things to restore in a rental property. Property managers check grout closely in showers, bathrooms, and kitchens. Here's how to approach it before your exit inspection.</p>
      <h2>Types of Grout Issues</h2>
      <h3>Surface Dirt and Soap Scum</h3>
      <p>The most straightforward type — grime sitting on the surface of the grout. A stiff grout brush and a good bathroom cleaner (or diluted bleach solution) scrubbed into the lines, left for 5–10 minutes, then scrubbed again and rinsed will remove most of it.</p>
      <h3>Mould in Grout</h3>
      <p>Mould penetrates into porous grout. Surface wiping won't remove it — you need a mould treatment with dwell time. Apply a bleach-based mould spray, leave for 15–30 minutes, then scrub with a stiff grout brush. Multiple applications may be needed for deep mould. Good ventilation is essential when using bleach-based products.</p>
      <h3>Deep Staining</h3>
      <p>Grout that has darkened significantly over time may require a commercial grout cleaner with an acid-based formula. These are available from tile shops and hardware stores and are more aggressive than household products. Follow the product instructions carefully and wear gloves.</p>
      <h2>The Right Tools</h2>
      <ul class="checklist">
        <li>Stiff grout brush (an old toothbrush works for small areas)</li>
        <li>Bleach-based mould spray or a commercial grout cleaner</li>
        <li>Good ventilation</li>
        <li>Gloves and eye protection for strong cleaning agents</li>
      </ul>
      <h2>When Grout Can't Be Cleaned</h2>
      <p>Some grout that has been stained or moulded for years can't be restored to its original colour through cleaning — the discolouration has penetrated too deeply. In these cases, grout re-colouring products (available from tile stores) can be applied over the cleaned grout to create a uniform appearance. This is a DIY option but takes time to do neatly.</p>
      <p>In extreme cases, grout re-pointing (removing and replacing the grout) may be necessary. This is a landlord maintenance responsibility if the grout has failed structurally, but staining from tenant use is typically the tenant's issue.</p>
"""
  },
  {
    "slug": "blog-bond-cleaning-laundry-room",
    "title": "Laundry Room Cleaning for Perth Bond Inspections",
    "h1": "Laundry Room Cleaning for Perth Bond Inspections — What Gets Checked",
    "meta": "The laundry is checked at every Perth bond inspection. What property managers look for, how to clean it properly, and the areas most commonly missed.",
    "read_time": 3,
    "content": """
      <p>The laundry is a small room but it gets a thorough check at exit. It's often neglected in DIY bond cleans because it seems less significant than the kitchen or bathrooms — but property managers walk through every room with the same REIWA checklist in hand.</p>
      <h2>What Gets Checked</h2>
      <ul class="checklist">
        <li>Laundry tub — scrubbed clean, taps polished, drain cleared</li>
        <li>Walls — particularly around the tub where water and detergent splash</li>
        <li>Flooring — swept and mopped, including behind and under the washing machine space</li>
        <li>Cupboards and shelving — wiped inside and out</li>
        <li>Washing machine space — lint, dust, and detergent residue behind and around where the machine sits</li>
        <li>Exhaust fan cover if present — dust buildup is common</li>
        <li>Window sill and track</li>
      </ul>
      <h2>If a Washing Machine Is Being Left</h2>
      <p>If you're leaving a washing machine in the property, it should be clean. Wipe the drum interior with a damp cloth, clean the door seal (mould often grows in the rubber), clean the detergent drawer, and clean the lint filter if accessible. Run a hot maintenance cycle if possible.</p>
      <h2>If a Dryer Is Present</h2>
      <p>Clean the lint filter and wipe the drum interior. The exterior of the dryer should be wiped down. For condenser dryers, empty and rinse the water reservoir.</p>
      <h2>Common Issues</h2>
      <p>The most commonly flagged laundry issues at Perth exit inspections:</p>
      <ul class="checklist">
        <li>Limescale and soap buildup in and around the laundry tub</li>
        <li>Detergent residue on walls near the tub</li>
        <li>Grime behind the washing machine — only visible when the machine is moved</li>
        <li>Dirty exhaust fan cover</li>
      </ul>
      <p>A thorough laundry clean takes 20–30 minutes. Don't skip it.</p>
"""
  },
  {
    "slug": "blog-bond-cleaning-balcony-perth",
    "title": "Balcony Cleaning for Perth Bond Inspections",
    "h1": "Balcony Cleaning for Perth Bond Inspections — What You Need to Do",
    "meta": "Balconies are checked at Perth apartment and townhouse exit inspections. What property managers look for and how to get your balcony inspection-ready.",
    "read_time": 3,
    "content": """
      <p>If your Perth rental has a balcony — whether it's a city apartment overlooking the CBD or a townhouse in the suburbs — it will be checked at your exit inspection. Here's what's required.</p>
      <h2>What Gets Checked on a Balcony</h2>
      <ul class="checklist">
        <li>Floor — swept and mopped or hosed down, any staining addressed</li>
        <li>Glass balustrade or railing — wiped clean of bird droppings, water marks, and fingerprints</li>
        <li>Ceiling or overhead structure — cobwebs cleared</li>
        <li>Outdoor light fittings — wiped and globe working</li>
        <li>Any built-in storage or cupboards — wiped out</li>
        <li>Drain — cleared of debris</li>
        <li>Outdoor power points — wiped</li>
      </ul>
      <h2>Glass Balustrades</h2>
      <p>Glass balustrades on Perth apartments accumulate salt, dust, and water spots over time — particularly on higher-floor properties exposed to wind. Use a glass cleaner and squeegee for streak-free results. For heavy water spotting, an acid-based glass cleaner or white vinegar solution is more effective than standard glass spray.</p>
      <h2>BBQ Areas</h2>
      <p>If you have a BBQ on the balcony, clean the grill plates and surrounding area. Property managers note residual grease and carbon buildup on BBQ areas. Soak grill plates in hot soapy water, scrub, and dry before the inspection.</p>
      <h2>Bird Droppings</h2>
      <p>Bird droppings on balcony floors and railings are common in Perth, particularly in areas with ibis, pigeons, or magpies. They need to be cleaned regardless of source — a property manager won't distinguish between bird-caused and tenant-caused mess. Wet the area first (dried droppings are harder to shift), scrub, and rinse.</p>
      <h2>Is Balcony Cleaning Included in a Bond Clean?</h2>
      <p>Balcony cleaning is typically included as standard in our bond clean price for apartments and townhouses. Confirm with your cleaner at booking. If you have an unusually large terrace or a heavily soiled area, mention it so it can be accounted for in the quote.</p>
"""
  },
  {
    "slug": "blog-cost-of-moving-perth",
    "title": "The Full Cost of Moving Out of a Rental in Perth",
    "h1": "The Full Cost of Moving Out of a Rental in Perth — What to Budget For",
    "meta": "What does it actually cost to move out of a rental in Perth? Removalists, bond cleaning, carpet cleaning, storage, and hidden costs — a realistic budget breakdown.",
    "read_time": 5,
    "content": """
      <p>Moving out of a rental in Perth involves more costs than most tenants budget for. Getting a realistic picture upfront means no nasty surprises when you're already dealing with the stress of a move.</p>
      <h2>Removalists</h2>
      <p>The biggest variable cost. Perth removalist prices depend heavily on the amount of furniture and the distance of the move:</p>
      <ul class="checklist">
        <li>Small apartment (1–2 bedroom, local move): $300–$600</li>
        <li>House (3–4 bedroom, local move): $600–$1,200</li>
        <li>Long-distance or interstate: $1,500–$5,000+</li>
      </ul>
      <p>Book 4+ weeks in advance, especially for month-end moves. Get at least two quotes.</p>
      <h2>Bond Cleaning</h2>
      <ul class="checklist">
        <li>Studio / 1-bedroom: $250–$350</li>
        <li>2-bedroom: $320–$470</li>
        <li>3-bedroom: $400–$600</li>
        <li>4-bedroom: $520–$720</li>
      </ul>
      <h2>Carpet Steam Cleaning</h2>
      <p>If required by your lease: $80–$220 depending on number of rooms. Often discounted when bundled with the bond clean.</p>
      <h2>Mail Redirection</h2>
      <p>Australia Post mail redirection: approximately $35 for 3 months, $55 for 6 months, $100 for 12 months. Set this up as early as possible — it takes a few days to activate.</p>
      <h2>Minor Repairs and Maintenance</h2>
      <p>Touch-up paint, replacing light globes, filling nail holes, replacing broken fixtures you're responsible for. Budget $50–$200 depending on the property's condition at the end of your tenancy.</p>
      <h2>Temporary Storage</h2>
      <p>If there's a gap between moving out and moving into your new place: Perth self-storage typically costs $80–$200/month depending on unit size.</p>
      <h2>New Property Costs</h2>
      <p>Your new bond (typically 4 weeks' rent), advance rent, and connection fees for utilities at the new property. These come at the same time as your move-out costs — it's the financial crunch that catches many Perth renters off guard.</p>
      <h2>Total Realistic Budget</h2>
      <p>For a typical 3-bedroom Perth rental move:</p>
      <ul class="checklist">
        <li>Removalists: $700–$1,000</li>
        <li>Bond clean: $400–$600</li>
        <li>Carpet cleaning: $150–$200</li>
        <li>Miscellaneous: $100–$200</li>
        <li><strong>Total: $1,350–$2,000+</strong></li>
      </ul>
      <p>Planning for this in advance makes the move significantly less stressful — and ensures you're not cutting corners on the bond clean to save money in the wrong place.</p>
"""
  },
  {
    "slug": "blog-how-to-get-bond-back-faster-wa",
    "title": "How to Get Your Bond Back Faster in Western Australia",
    "h1": "How to Get Your Bond Back Faster in WA — Practical Steps",
    "meta": "Perth renters waiting for their bond refund. How to speed up the process, what causes delays, and how to ensure your money comes back as quickly as possible.",
    "read_time": 4,
    "content": """
      <p>After vacating your Perth rental, your bond refund can take anywhere from a few days to several weeks depending on how the exit process goes. Here's how to make it as fast as possible.</p>
      <h2>What Causes Bond Refund Delays</h2>
      <ul class="checklist">
        <li>Disputed cleaning — back-and-forth between tenant and property manager takes time</li>
        <li>Property manager slow to submit the bond disposal form</li>
        <li>Outstanding rent or water usage bills being calculated</li>
        <li>Damage disputes requiring quotes from contractors</li>
        <li>Administrative delays at the Bond Administrator</li>
      </ul>
      <h2>Step 1 — Pass the Exit Inspection First Time</h2>
      <p>The fastest path to your bond refund is passing the exit inspection with no issues. A professional bond clean with a REIWA-aligned checklist and a bond back guarantee is the most reliable way to do this. No dispute means no delay.</p>
      <h2>Step 2 — Submit the Bond Disposal Form Promptly</h2>
      <p>Once both parties agree there are no issues, either you or the property manager can submit a bond disposal form to the Bond Administrator (DMIRS). Ask your property manager how soon they can submit it after the inspection — some process it same day, others take a week.</p>
      <h2>Step 3 — Agree on Outstanding Amounts</h2>
      <p>If there's a utility bill or rent owing, agree on the amount quickly. Prolonged back-and-forth over small amounts delays the entire bond refund. It's often worth quickly agreeing on a reasonable figure to unblock the process.</p>
      <h2>Step 4 — Confirm Your Bank Details Are Updated</h2>
      <p>The Bond Administrator will refund your bond to the bank account on file. Make sure your details with the Bond Administrator are up to date — an outdated account number causes a delay that's entirely avoidable.</p>
      <h2>How Long Does It Take?</h2>
      <p>When everything goes smoothly — clean inspection, no dispute, prompt bond disposal form — the refund typically takes 3–5 business days after the form is submitted. With disputes, it can take weeks or longer if the matter goes to the Magistrates Court.</p>
"""
  },
  {
    "slug": "blog-bond-cleaning-what-is-included",
    "title": "What Is Included in a Bond Clean in Perth? (Full Breakdown)",
    "h1": "What Is Included in a Bond Clean in Perth? (Full Room-by-Room Breakdown)",
    "meta": "Exactly what a professional Perth bond clean includes — kitchen, bathrooms, bedrooms, living areas, and outdoor areas. What's standard and what costs extra.",
    "read_time": 5,
    "content": """
      <p>Not all bond cleans are equal. When you're getting quotes, knowing exactly what should be included protects you from under-specification and explains why prices vary significantly between providers. Here's a full breakdown of what a proper Perth bond clean covers.</p>
      <h2>Kitchen</h2>
      <ul class="checklist">
        <li>Oven — cavity, racks, door glass (inside and out), door seal, drawer below</li>
        <li>Cooktop — burners, drip trays, surrounding surfaces</li>
        <li>Rangehood — filters (soaked or dishwashed), interior housing, exterior</li>
        <li>Microwave — interior and exterior</li>
        <li>Dishwasher — filter cleaned, interior wiped, door seal</li>
        <li>All cupboards — doors inside and out, shelves, drawers</li>
        <li>Benchtops and splashback</li>
        <li>Sink — scrubbed, taps polished, drain cleared</li>
        <li>Window sill, track, and internal glass</li>
        <li>Light switches and power points</li>
        <li>Floor swept and mopped</li>
      </ul>
      <h2>Bathrooms (Each)</h2>
      <ul class="checklist">
        <li>Shower screen or bath — soap scum and water marks removed</li>
        <li>Tiles and grout — scrubbed, mould treated</li>
        <li>Shower or bath drain cleared</li>
        <li>Toilet — bowl inside (under rim), cistern exterior, seat, base</li>
        <li>Vanity and basin — taps, cabinet inside and out, mirror</li>
        <li>Exhaust fan cover removed and cleaned</li>
        <li>Floor mopped including behind toilet</li>
      </ul>
      <h2>Bedrooms and Living Areas</h2>
      <ul class="checklist">
        <li>Wardrobe interiors — shelves, rail, tracks, door faces</li>
        <li>Blind slats — each one, both sides</li>
        <li>Window sills, tracks, and internal glass</li>
        <li>Skirting boards along all walls</li>
        <li>Light fittings and ceiling fans dusted</li>
        <li>Light switches and power points wiped</li>
        <li>Walls spot-cleaned</li>
        <li>Floors vacuumed and mopped (or carpets vacuumed)</li>
      </ul>
      <h2>What's Typically an Add-On</h2>
      <ul class="checklist">
        <li>Carpet steam cleaning — usually priced separately</li>
        <li>External window cleaning</li>
        <li>Garage cleaning</li>
        <li>Fridge interior</li>
        <li>Outdoor areas beyond a standard balcony</li>
      </ul>
      <p>When getting a quote, always confirm whether these add-ons are included or separate, and get it in writing. The gap between a $300 and a $550 quote for the same property size often comes down to which add-ons are included and whether a guarantee is offered.</p>
"""
  },
  {
    "slug": "blog-bond-cleaning-two-storey-perth",
    "title": "Bond Cleaning a Two-Storey House in Perth — What to Expect",
    "h1": "Bond Cleaning a Two-Storey House in Perth — What to Expect",
    "meta": "Bond cleaning a two-storey Perth home involves stairs, multiple bathrooms, and more surface area. What's included, typical costs, and how long it takes.",
    "read_time": 4,
    "content": """
      <p>Two-storey homes are increasingly common in Perth's outer suburbs and newer developments. Bond cleaning them involves everything in a single-storey home plus some specific considerations for the second level and staircase.</p>
      <h2>The Staircase</h2>
      <p>Stairs accumulate dust and grime on every tread, riser, and the skirting boards either side. The stair balustrade — whether timber rails, glass panels, or metal — is also checked. Stairs take longer to clean properly than an equivalent floor area because each step needs individual attention. Allow extra time, or confirm with your professional cleaner that stairs are specifically included.</p>
      <h2>Upstairs Bedrooms and Bathrooms</h2>
      <p>The second storey typically houses the bedrooms and ensuite in most Perth two-storey homes. Each bedroom gets the same treatment as in a single-storey property: wardrobes, blinds, skirting boards, window tracks, and floors. The ensuite is checked to the same bathroom standard as downstairs.</p>
      <h2>External Windows on the Upper Level</h2>
      <p>Standard bond cleaning includes internal window cleaning throughout. External cleaning of upper-level windows requires access equipment (a ladder or water-fed pole) and is usually priced as an add-on. If your ingoing condition report noted clean external upper windows, you may need to arrange this.</p>
      <h2>Typical Cost for a Two-Storey Perth Home</h2>
      <p>A 4-bedroom, 2-bathroom two-storey home: $550–$750 for a professional bond clean. With carpet steam cleaning for upstairs bedrooms: add $100–$180. These are indicative figures — get a specific quote based on your property's layout.</p>
      <h2>How Long Does It Take?</h2>
      <p>A professional team of 2: typically 7–10 hours for a standard two-storey 4x2. Larger homes with multiple bathrooms, double garage, and alfresco can take longer. Book a full day to be safe.</p>
      <h2>Tips for Two-Storey Bond Cleans</h2>
      <ul class="checklist">
        <li>Ensure the property is completely vacated on both levels before the clean starts</li>
        <li>Confirm stairs are explicitly included in your cleaner's scope</li>
        <li>Ask about upper-level external windows if they were clean at ingoing</li>
        <li>Book early — full-day jobs are in higher demand</li>
      </ul>
"""
  },
  {
    "slug": "blog-move-out-day-perth",
    "title": "Move-Out Day in Perth — A Practical Guide for Renters",
    "h1": "Move-Out Day in Perth — A Practical Step-by-Step Guide",
    "meta": "Everything you need to do on move-out day in Perth. The order of operations, what to check before you leave, and how to hand back the property without issues.",
    "read_time": 4,
    "content": """
      <p>Move-out day is chaotic for most Perth renters. With removalists arriving, boxes everywhere, and a deadline to hand back the keys — it's easy for things to fall through the cracks. Here's how to manage the day so nothing important is missed.</p>
      <h2>Before the Removalists Arrive</h2>
      <ul class="checklist">
        <li>Check every room, cupboard, and drawer for items you might have missed in packing</li>
        <li>Check the garage, shed, and outdoor areas</li>
        <li>Take final photos of any furniture positions (useful if there's a floor damage question later)</li>
      </ul>
      <h2>During the Move</h2>
      <ul class="checklist">
        <li>Remove all rubbish — don't leave anything in bins inside or outside the property</li>
        <li>Check under beds and in the back of wardrobes — things get left here</li>
        <li>Don't leave cleaning products, paint tins, or chemicals — they're your responsibility to dispose of</li>
      </ul>
      <h2>After the Property Is Empty</h2>
      <p>The bond clean should happen on an empty property — 1–2 days before your exit inspection if you've planned well, or the same day if your timeline is tight. A professional cleaner can come in as soon as the removalists leave.</p>
      <h2>After the Bond Clean</h2>
      <ul class="checklist">
        <li>Replace any blown light globes — check every switch</li>
        <li>Take date-stamped photos of every room, the oven, bathrooms, and garage</li>
        <li>Collect all keys, remotes, and garage fobs</li>
        <li>Check all windows and doors close and lock properly</li>
      </ul>
      <h2>Key Handover</h2>
      <p>Return all keys at the agreed time. If you're posting keys, send them by registered post so there's a delivery record. Don't hand keys back before you've walked through the property and are satisfied with the condition — once you've handed over access, you can't go back to fix anything without the property manager's permission.</p>
      <h2>After Key Handover</h2>
      <p>Contact your utility providers to ensure final readings are taken and accounts closed. Redirect your mail if you haven't already. Keep all your tenancy documentation for at least 12 months in case a bond dispute arises later.</p>
"""
  },
  {
    "slug": "blog-what-is-vacate-cleaning",
    "title": "What Is Vacate Cleaning? Everything Perth Renters Need to Know",
    "h1": "What Is Vacate Cleaning? Everything Perth Renters Need to Know",
    "meta": "Vacate cleaning explained for Perth renters. What it involves, how it differs from bond cleaning, what's required, and how to make sure you get your full bond back.",
    "read_time": 4,
    "content": """
      <p>If you're moving out of a rental in Perth and searching for information on vacate cleaning, you're in the right place. Here's everything you need to know about what it is, what it involves, and how to get it right.</p>
      <h2>What Does "Vacate Cleaning" Mean?</h2>
      <p>Vacate cleaning is simply another term for bond cleaning or end-of-lease cleaning. All three terms refer to the same thing: the comprehensive deep clean of a rental property carried out when a tenant vacates. The term "vacate clean" is commonly used by property managers and real estate agents across Perth.</p>
      <h2>What Does a Vacate Clean Include?</h2>
      <p>A proper Perth vacate clean follows the REIWA Property Condition Report and covers every room and area of the property to a standard that matches or exceeds the condition at the start of the tenancy:</p>
      <ul class="checklist">
        <li>Kitchen — oven, rangehood, all cupboard interiors, benchtops, sink</li>
        <li>Bathrooms — shower screen, grout, toilet, vanity, exhaust fan</li>
        <li>Bedrooms — wardrobes inside, blind slats, skirting boards, window tracks</li>
        <li>Living areas — same room requirements as bedrooms</li>
        <li>All floors — vacuumed and mopped</li>
        <li>Balcony or alfresco if applicable</li>
      </ul>
      <h2>Does a Vacate Clean Include Carpet Cleaning?</h2>
      <p>Standard vacate cleaning includes thorough vacuuming of carpets. Professional carpet steam cleaning (hot water extraction) is typically a separate add-on. Check your lease — if it specifies professional steam cleaning, you'll need a separate receipt from a licensed operator.</p>
      <h2>How Much Does a Vacate Clean Cost in Perth?</h2>
      <p>$250–$350 for a 1-bedroom, $320–$470 for a 2-bedroom, $400–$580 for a 3-bedroom, $520–$720 for a 4-bedroom. For a full breakdown see our <a href="blog-bond-cleaning-cost-perth.html" style="color:var(--green);">2025 price guide</a>.</p>
      <h2>Do I Have to Hire a Professional?</h2>
      <p>No — but you do have to return the property in a reasonable state of cleanliness. A professional vacate cleaner follows the REIWA checklist and backs the clean with a bond back guarantee. DIY is an option for small, well-maintained properties. For anything larger or more complex, professional cleaning is almost always the better investment.</p>
"""
  },
  {
    "slug": "blog-bond-cleaning-checklist-wa",
    "title": "Bond Cleaning Checklist WA — The Official REIWA Standard",
    "h1": "Bond Cleaning Checklist WA — The REIWA Standard Explained",
    "meta": "The WA bond cleaning checklist based on the REIWA Property Condition Report. What every area of the property must meet for a successful exit inspection in Western Australia.",
    "read_time": 5,
    "content": """
      <p>In Western Australia, property managers use the REIWA Property Condition Report as the standard for exit inspections. This checklist is based on that document — if your property meets this standard, you've met the requirement to return the property in a reasonable state of cleanliness.</p>
      <h2>Kitchen Checklist</h2>
      <ul class="checklist">
        <li>Oven — cavity clean, racks clean, door glass clear, seal wiped, drawer clean</li>
        <li>Cooktop — burners, drip trays, and surrounding surfaces grease-free</li>
        <li>Rangehood — filters degreased, interior clean, exterior wiped</li>
        <li>Dishwasher — filter clean, interior wiped, door seal clean</li>
        <li>Microwave — interior and exterior clean</li>
        <li>All cupboards — shelves wiped, drawers clean inside and out</li>
        <li>Benchtops — clean and dry</li>
        <li>Splashback — grease-free</li>
        <li>Sink — clean, taps polished, drain clear</li>
        <li>Window sill and track clean</li>
        <li>Floor swept and mopped</li>
      </ul>
      <h2>Bathroom / Ensuite Checklist</h2>
      <ul class="checklist">
        <li>Shower screen — no soap scum or water marks</li>
        <li>Tiles and grout — no mould or heavy staining</li>
        <li>Shower floor or bath — clean, drain clear</li>
        <li>Toilet — bowl (under rim), seat, lid, cistern exterior, base</li>
        <li>Vanity — basin, taps, cabinet inside and out, mirror</li>
        <li>Exhaust fan cover — removed and cleaned</li>
        <li>Floor mopped including behind the toilet</li>
      </ul>
      <h2>Bedroom / Living Area Checklist</h2>
      <ul class="checklist">
        <li>Wardrobe — shelves, rail, tracks, door faces inside and out</li>
        <li>Blinds — each slat individually, both sides</li>
        <li>Window sills and tracks — dust and debris cleared</li>
        <li>Skirting boards — along all walls including behind furniture</li>
        <li>Light fittings and ceiling fans — dusted</li>
        <li>Light switches and power points — wiped</li>
        <li>Walls — spot cleaned for marks</li>
        <li>Floors — vacuumed and mopped</li>
      </ul>
      <h2>Laundry</h2>
      <ul class="checklist">
        <li>Tub clean, taps polished, drain clear</li>
        <li>Cupboards and shelving wiped</li>
        <li>Floor swept and mopped</li>
        <li>Appliance space clean if leaving machines</li>
      </ul>
      <h2>Outdoor / General</h2>
      <ul class="checklist">
        <li>All light globes working</li>
        <li>All keys and remotes returned</li>
        <li>All rubbish removed</li>
        <li>Smoke detectors functional</li>
        <li>Air conditioning filters cleaned</li>
        <li>Garage floor swept, door clean</li>
        <li>Balcony or alfresco swept and cleaned</li>
      </ul>
      <p>This checklist forms the basis of our professional bond cleaning service. Every item above is addressed on every clean we do — and backed by our bond back guarantee.</p>
"""
  },
  {
    "slug": "blog-bond-cleaning-tips-landlords",
    "title": "What Landlords in Perth Actually Want From a Bond Clean",
    "h1": "What Perth Landlords and Property Managers Actually Want From a Bond Clean",
    "meta": "Understanding what Perth property managers and landlords expect at a bond inspection. The standard, the common issues, and how tenants can meet it without overspending.",
    "read_time": 5,
    "content": """
      <p>Most bond cleaning guides are written from the tenant's perspective. This one is different — we're going to look at what property managers and landlords in Perth actually expect, so you can meet that standard precisely without wasting time or money.</p>
      <h2>The Benchmark: The Ingoing Condition</h2>
      <p>Property managers don't expect a rental property to be returned in better-than-new condition. They expect it to be returned in the same condition as the ingoing Property Condition Report — allowing for fair wear and tear. That's a very specific benchmark, and understanding it is key.</p>
      <p>A property manager who received the property from a developer with pristine grout and a spotless oven will hold you to that standard. A property manager who received it from a previous tenant with already-worn carpet won't hold you responsible for that wear. The ingoing report is the baseline.</p>
      <h2>What Property Managers Check Most Carefully</h2>
      <p>From years of experience across Perth, these are the areas property managers spend the most time on:</p>
      <ul class="checklist">
        <li><strong>Oven</strong> — checked first, every time</li>
        <li><strong>Shower screen and bathroom grout</strong> — a major focus in older properties</li>
        <li><strong>Carpets</strong> — condition and whether steam cleaning has been done</li>
        <li><strong>Blind slats</strong> — run a finger test</li>
        <li><strong>Skirting boards</strong> — particularly behind furniture</li>
        <li><strong>Rangehood filters</strong> — removed and inspected</li>
      </ul>
      <h2>What Property Managers Don't Penalise</h2>
      <p>Fair-minded property managers distinguish between damage and normal use. Minor wall scuffs in a 3-year tenancy, small nail holes, carpet compression in traffic areas, and faded curtains are fair wear and tear. Most Perth property managers won't claim for these items — and those who do can be challenged effectively with the evidence of the ingoing report.</p>
      <h2>The Receipt Question</h2>
      <p>Most Perth property managers feel more comfortable approving a bond refund when they see professional cleaning receipts. It's not a legal requirement for a clean property, but it signals professionalism and gives the property manager confidence that the REIWA standard was followed. A receipt also protects you — if a dispute arises later, you have documented evidence.</p>
      <h2>The Bottom Line</h2>
      <p>Property managers want the property back in the condition it was handed over, without having to spend time and money organising re-cleaning. Meet that standard, have the documentation to prove it, and the bond refund process is almost always straightforward.</p>
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
