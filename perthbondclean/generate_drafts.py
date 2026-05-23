#!/usr/bin/env python3
"""Generate 30 draft blog posts for the weekly publishing queue."""

import os
import json

DRAFTS_DIR = "drafts"
os.makedirs(DRAFTS_DIR, exist_ok=True)

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
    <p style="color:var(--muted);font-size:0.95rem;margin-top:12px;">Published {pub_date} &nbsp;|&nbsp; {read_time} min read</p>
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
{{"@context":"https://schema.org","@type":"Article","headline":"{title}","description":"{meta}","url":"https://perthbondclean.com/{slug}.html","datePublished":"{pub_iso}","dateModified":"{pub_iso}","author":{{"@type":"Organization","name":"Perth Bond Clean","url":"https://perthbondclean.com"}},"publisher":{{"@type":"Organization","name":"Perth Bond Clean","url":"https://perthbondclean.com","logo":{{"@type":"ImageObject","url":"https://perthbondclean.com/logo.png"}}}},"mainEntityOfPage":{{"@type":"WebPage","@id":"https://perthbondclean.com/{slug}.html"}}}}
</script>
</body>
</html>'''

ARTICLES = [
  {
    "slug": "blog-bond-cleaning-east-perth",
    "title": "Bond Cleaning East Perth — What Apartment Renters Need to Know",
    "h1": "Bond Cleaning East Perth — What Apartment Renters Need to Know",
    "tag": "Suburbs",
    "meta": "Bond cleaning in East Perth is mostly apartment work — high-rise and mid-rise units with specific requirements around balconies, elevators, and strata access. What you need to know.",
    "read_time": 4,
    "excerpt": "East Perth is dominated by apartment living — high-rise and mid-rise units with specific requirements around balconies, strata access, and sometimes multiple bathrooms. Here's what renters in East Perth need to know.",
    "content": """
      <p>East Perth is one of the most densely rented suburbs in the metropolitan area, with a high proportion of apartments ranging from compact studios to large multi-bedroom units overlooking the Swan River. Bond cleaning in East Perth has a few specific considerations compared to suburban Perth.</p>
      <h2>Apartment-Specific Requirements</h2>
      <p>Most East Perth rentals are apartments, and the bond clean requirements reflect that. Balconies are standard — sometimes large terraces — and are always included in the exit inspection. Building access for cleaners needs to be arranged, whether through a resident fob or coordination with the strata manager.</p>
      <h2>What Property Managers Check in East Perth Apartments</h2>
      <ul class="checklist">
        <li>Balcony floor, glass balustrade, and ceiling (cobwebs)</li>
        <li>Split-system air conditioning filters — very common in East Perth apartments</li>
        <li>Carpet in bedrooms if present — steam cleaning often required in higher-end units</li>
        <li>Stainless steel appliances in modern kitchens — fingerprints and streaks are noted</li>
        <li>Floor-to-ceiling windows — internal cleaning required, external upper floors add-on</li>
        <li>Exhaust fans in bathrooms and the kitchen rangehood</li>
      </ul>
      <h2>Common East Perth Property Types</h2>
      <p>Typical East Perth rentals range from 1-bedroom units ($250–$350 bond clean) to 2-bedroom, 2-bathroom apartments ($350–$500). Some premium buildings have 3-bedroom configurations with a higher clean cost. Modern buildings often have dishwashers, quality rangehoods, and tiled or timber-look floors throughout — all of which require specific cleaning approaches.</p>
      <h2>Building Access for Cleaners</h2>
      <p>Most East Perth apartment buildings require fob or key access. Arrange this before booking — either you'll be present to let cleaners in, or you'll need to organise a temporary access method. Our cleaners are police-checked and fully insured for unattended access.</p>
      <h2>Getting a Quote for East Perth</h2>
      <p>When requesting a quote for an East Perth property, mention the floor level, whether you have a balcony, and whether upper-floor external windows need cleaning. Get in touch and we'll have a price back to you within the hour.</p>
"""
  },
  {
    "slug": "blog-bond-cleaning-south-perth",
    "title": "Bond Cleaning South Perth — Suburb Guide for Renters",
    "h1": "Bond Cleaning South Perth — What Renters Need to Know",
    "tag": "Suburbs",
    "meta": "Bond cleaning in South Perth covers everything from riverfront apartments to family homes. What property managers check, typical costs, and how to get your full bond back.",
    "read_time": 4,
    "excerpt": "South Perth is a mix of riverfront apartments and established family homes — bond cleaning requirements vary significantly. Here's what renters in South Perth need to know about exit cleans and inspections.",
    "content": """
      <p>South Perth covers a wide range of rental property types — from premium apartments on the river to established 3 and 4-bedroom family homes in quieter streets. Bond cleaning requirements vary based on the property type, but the REIWA standard applies across the board.</p>
      <h2>Property Types in South Perth</h2>
      <h3>Apartments (Como and riverside areas)</h3>
      <p>Apartments near the South Perth foreshore and in Como tend to have premium fixtures — quality stone benchtops, floor-to-ceiling windows, and large balconies. Cleaning standards at exit are correspondingly high. Stainless steel surfaces must be streak-free, shower screens must be spot-free, and balcony glass needs to be clear of salt and dust.</p>
      <h3>Family Homes</h3>
      <p>Larger 3 and 4-bedroom homes in South Perth often have multiple bathrooms, a garage, and backyard areas that all need attention. Carpet steam cleaning is commonly required for these properties. Expect a thorough exit inspection that covers the outdoor alfresco, clothesline, and garden bed condition.</p>
      <h2>Typical Bond Cleaning Costs in South Perth</h2>
      <ul class="checklist">
        <li>1-bedroom apartment: $250–$350</li>
        <li>2-bedroom, 2-bathroom apartment: $350–$500</li>
        <li>3-bedroom house: $400–$600</li>
        <li>4-bedroom house with garage: $550–$750</li>
      </ul>
      <h2>What to Watch For</h2>
      <p>South Perth property managers tend to be thorough. The suburb has a mix of owner-investors and longer-term landlords who maintain their properties to a high standard. Ensure your oven, rangehood, and all bathrooms are cleaned to a commercial standard — not just surface-wiped.</p>
      <p>For homes with pools, confirm with your property manager what the exit condition expectation is. Pool cleaning and water chemistry is typically the tenant's responsibility during tenancy but not necessarily part of the bond clean scope.</p>
      <h2>Book Early</h2>
      <p>South Perth is a popular suburb with competitive rental turnovers. Bond cleaners in the area book out at month-ends — contact us at least 2 weeks before your move-out date to secure your slot.</p>
"""
  },
  {
    "slug": "blog-bond-cleaning-nedlands",
    "title": "Bond Cleaning Nedlands — Guide for Perth Renters",
    "h1": "Bond Cleaning Nedlands — What Renters Need to Know",
    "tag": "Suburbs",
    "meta": "Bond cleaning in Nedlands covers premium homes and apartments near UWA. What property managers check, typical costs, and how to ensure a smooth exit inspection.",
    "read_time": 4,
    "excerpt": "Nedlands is a premium Perth suburb with a mix of established family homes and properties near UWA. Bond cleaning standards are high — here's what renters need to know about exit cleans in Nedlands.",
    "content": """
      <p>Nedlands is one of Perth's most sought-after suburbs, with premium homes close to the Swan River and the University of Western Australia. Rental properties in Nedlands range from modern apartments to large character homes, and exit inspections here tend to be thorough.</p>
      <h2>Character Homes — Specific Considerations</h2>
      <p>Many Nedlands rental properties are established homes with features like original timber floors, older bathroom tiles, and sash windows. These require specific cleaning approaches:</p>
      <ul class="checklist">
        <li>Timber floors — clean with appropriate floor cleaner, avoid excessive moisture</li>
        <li>Older bathroom tiles — grout may require extra attention due to age</li>
        <li>Sash windows — tracks and sills accumulate significant dust and debris</li>
        <li>Fireplaces — if present, the surround should be clean even if not used</li>
      </ul>
      <h2>UWA Student Properties</h2>
      <p>Properties near UWA often house multiple tenants and experience higher-than-average wear. At exit, property managers inspect these carefully for furniture damage, carpet stains, and kitchen cleanliness. Bond cleans for multi-tenant properties need to be particularly thorough in shared areas — kitchens and bathrooms especially.</p>
      <h2>Typical Costs in Nedlands</h2>
      <ul class="checklist">
        <li>1–2 bedroom apartment: $280–$420</li>
        <li>3-bedroom house: $420–$600</li>
        <li>4-bedroom house: $560–$780</li>
        <li>Carpet steam cleaning: $100–$220 depending on rooms</li>
      </ul>
      <h2>What Nedlands Property Managers Focus On</h2>
      <p>In premium suburbs like Nedlands, property managers representing landlords with significant assets tend to inspect very carefully. The oven and rangehood, bathroom grout, and blind slats are the most commonly flagged items. Don't underestimate the time required for a thorough exit clean of a large character home — professional teams are the reliable choice here.</p>
"""
  },
  {
    "slug": "blog-bond-cleaning-leederville",
    "title": "Bond Cleaning Leederville — What Perth Renters Need to Know",
    "h1": "Bond Cleaning Leederville — A Renter's Guide",
    "tag": "Suburbs",
    "meta": "Bond cleaning in Leederville covers apartments, units, and character homes. What property managers check at exit inspections and how to get your full bond back.",
    "read_time": 4,
    "excerpt": "Leederville is a trendy inner-suburb with a mix of apartments, units, and older character homes. Bond cleaning requirements here are standard but the older building stock means a few specific things to watch for.",
    "content": """
      <p>Leederville sits just north of the Perth CBD and is popular with young professionals and students. The suburb has a mix of newer apartment complexes and older character homes and units — both of which have their own exit clean considerations.</p>
      <h2>Newer Apartments</h2>
      <p>Modern apartment buildings in Leederville typically have stainless steel appliances, tiled or floating floor throughout, and split-system air conditioning. For these properties, the key areas are:</p>
      <ul class="checklist">
        <li>Air conditioning filters — very frequently missed in DIY cleans</li>
        <li>Oven and rangehood — modern ovens have more crevices and glass surfaces</li>
        <li>Balcony glass — often floor-to-ceiling and requires proper glass cleaner</li>
        <li>Bathroom grout — newer grout stains just as easily as older</li>
      </ul>
      <h2>Older Units and Character Homes</h2>
      <p>Older Leederville properties tend to have painted weatherboard exteriors, older bathroom tiles, and sometimes carpet throughout. For these:</p>
      <ul class="checklist">
        <li>Older bathroom tiles — may have existing discolouration that's fair wear and tear, but grout mould is your responsibility</li>
        <li>Carpet — often present in all rooms; steam cleaning commonly required</li>
        <li>Timber floor skirting boards — paint may chip easily, clean carefully</li>
        <li>Window sashes and tracks — accumulate significant grime in older frames</li>
      </ul>
      <h2>Typical Costs</h2>
      <p>Leederville bond clean prices are consistent with Perth inner-suburb averages: 1-bedroom unit $270–$350, 2-bedroom $340–$470, 3-bedroom house $420–$600. Carpet steam cleaning is an add-on where required.</p>
      <h2>Proximity and Booking</h2>
      <p>We service all of Leederville and surrounding suburbs. Contact us for a quote — we respond within 1 hour and can often accommodate short-notice bookings during quieter periods of the month.</p>
"""
  },
  {
    "slug": "blog-bond-cleaning-northbridge",
    "title": "Bond Cleaning Northbridge Perth — Apartment Exit Clean Guide",
    "h1": "Bond Cleaning Northbridge Perth — What Renters Need to Know",
    "tag": "Suburbs",
    "meta": "Bond cleaning in Northbridge is primarily apartment work in a high-turnover inner suburb. What property managers check and how to pass your exit inspection.",
    "read_time": 4,
    "excerpt": "Northbridge is Perth's most densely populated rental suburb — apartments turn over frequently and property managers inspect closely. Here's what renters in Northbridge need to know about bond cleans.",
    "content": """
      <p>Northbridge is Perth's entertainment and arts hub, with a high density of rental apartments catering to students, hospitality workers, and young professionals. It's one of Perth's highest-turnover rental suburbs, which means property managers here see a lot of exit cleans — and know exactly what to look for.</p>
      <h2>What Northbridge Property Managers Check</h2>
      <p>High turnover means experienced property managers with sharp eyes. The most commonly flagged items in Northbridge apartments:</p>
      <ul class="checklist">
        <li>Kitchen — heavy cooking in small kitchens means significant oven and rangehood buildup</li>
        <li>Bathroom grout — high humidity in compact bathrooms accelerates mould growth</li>
        <li>Air conditioning filters — apartments run AC heavily in Perth summers</li>
        <li>Carpet — if present, pet hair and staining are common issues</li>
        <li>Walls near light switches — fingerprints and marks in high-traffic areas</li>
      </ul>
      <h2>Small Apartment Considerations</h2>
      <p>Many Northbridge apartments are compact studios and 1-bedroom units where the kitchen, living area, and sometimes the bedroom share open-plan space. In these layouts, cooking odours and grease can settle on surfaces throughout the apartment, not just in the kitchen. A thorough bond clean addresses all surfaces, not just the obvious areas.</p>
      <h2>Parking and Access</h2>
      <p>Northbridge has limited street parking. When booking a bond clean, let us know the building access requirements and any parking arrangements for our team's equipment — particularly for carpet steam cleaning where a machine needs to be brought in.</p>
      <h2>Costs</h2>
      <p>Studio: $200–$300. 1-bedroom: $270–$370. 2-bedroom: $350–$480. These prices are for a full REIWA-aligned clean with our bond back guarantee. Contact us for an exact quote for your Northbridge property.</p>
"""
  },
  {
    "slug": "blog-bond-cleaning-wembley",
    "title": "Bond Cleaning Wembley Perth — What Renters Need to Know",
    "h1": "Bond Cleaning Wembley Perth — Renter's Guide to Exit Cleans",
    "tag": "Suburbs",
    "meta": "Bond cleaning in Wembley covers family homes and units in this popular inner-western suburb. What property managers check and how to get your full bond back.",
    "read_time": 4,
    "excerpt": "Wembley is a popular inner-western suburb with a mix of family homes and apartment complexes. Bond cleaning here follows the REIWA standard — here's what Wembley renters need to know.",
    "content": """
      <p>Wembley sits between Subiaco and Scarborough, making it a popular choice for families and professionals. The suburb has a mix of older brick homes, newer developments, and apartment blocks — all of which are well-maintained by local property managers.</p>
      <h2>Property Types in Wembley</h2>
      <p>Wembley's rental stock ranges from older 1960s–70s brick homes to newer townhouses and apartments. Older properties often have:</p>
      <ul class="checklist">
        <li>Aluminium window frames — tracks accumulate significant rust and grime</li>
        <li>Carpet in all bedrooms — steam cleaning commonly required</li>
        <li>Older bathroom tiles — require careful grout cleaning</li>
        <li>Separate laundry rooms with older fixtures</li>
      </ul>
      <h2>What Wembley Property Managers Focus On</h2>
      <p>Like most family-oriented suburbs, Wembley property managers pay particular attention to:</p>
      <ul class="checklist">
        <li>Carpet condition — wear, staining, and odour after families with children or pets</li>
        <li>Kitchen oven and rangehood — heavy family cooking leaves significant buildup</li>
        <li>Backyard condition — lawn length, garden beds, and general tidiness</li>
        <li>Garage floor — oil stains and general cleanliness</li>
        <li>All bathrooms to a consistent standard</li>
      </ul>
      <h2>Typical Costs in Wembley</h2>
      <ul class="checklist">
        <li>2-bedroom unit: $320–$450</li>
        <li>3-bedroom house: $420–$580</li>
        <li>4-bedroom house: $560–$750</li>
        <li>Carpet steam cleaning: $120–$200</li>
        <li>Garage add-on: $70–$100</li>
      </ul>
      <p>Contact us for a Wembley bond cleaning quote — we service the entire inner-western corridor and respond within the hour.</p>
"""
  },
  {
    "slug": "blog-bond-cleaning-maylands",
    "title": "Bond Cleaning Maylands Perth — Renter's Guide",
    "h1": "Bond Cleaning Maylands Perth — What Renters Need to Know",
    "tag": "Suburbs",
    "meta": "Bond cleaning in Maylands covers a mix of apartments, character homes, and townhouses. What property managers check at exit and how to get your bond back.",
    "read_time": 4,
    "excerpt": "Maylands is one of Perth's most popular inner-northern suburbs — a mix of character homes, renovated cottages, and newer apartments. Bond cleaning here has a few suburb-specific things to know.",
    "content": """
      <p>Maylands has become one of Perth's most sought-after inner suburbs over the past decade. With a vibrant café strip and good transport links, it attracts a diverse rental population. Property types range from original 1920s–1940s character homes to newer apartment developments along the main road.</p>
      <h2>Character Homes — What's Different</h2>
      <p>Older character homes in Maylands often have features that require specific cleaning attention:</p>
      <ul class="checklist">
        <li>Jarrah or pine floorboards — clean with appropriate product, no excess water</li>
        <li>Sash or casement windows — tracks and sills need careful attention</li>
        <li>High ceilings — light fittings require a ladder and can accumulate significant dust</li>
        <li>Older kitchen layouts — sometimes have spaces behind or under appliances that trap debris</li>
        <li>Evaporative air conditioning — filter pads need to be cleaned or replaced</li>
      </ul>
      <h2>Newer Apartments</h2>
      <p>Modern apartment buildings along Whatley Crescent and surrounding streets are typical inner-suburban apartments — split-system AC, tiled floors, balconies. Standard bond clean applies with AC filter cleaning included.</p>
      <h2>Evaporative Cooling — A Common Issue</h2>
      <p>Many older Maylands properties have evaporative cooling rather than reverse-cycle split systems. Evaporative systems have pads that absorb water and can accumulate scale and mould over a tenancy. These should be cleaned (or the condition noted in the ingoing PCR) before the exit inspection.</p>
      <h2>Costs and Booking</h2>
      <p>1-bedroom unit: $260–$360. 2-bedroom character home: $350–$480. 3-bedroom house: $430–$600. Contact us for an exact quote for your Maylands property and we'll respond within the hour.</p>
"""
  },
  {
    "slug": "blog-bond-cleaning-belmont-perth",
    "title": "Bond Cleaning Belmont Perth — What Renters Need to Know",
    "h1": "Bond Cleaning Belmont Perth — Renter's Guide to Exit Cleans",
    "tag": "Suburbs",
    "meta": "Bond cleaning in Belmont covers a mix of older homes and newer developments. What property managers check and how to pass your exit inspection first time.",
    "read_time": 4,
    "excerpt": "Belmont is an affordable inner-eastern suburb with a mix of older homes and newer units. Bond cleaning standards follow the REIWA checklist — here's what Belmont renters need to know.",
    "content": """
      <p>Belmont is a well-established suburb east of the Perth CBD, popular with families and first-home buyers entering the rental market. It has a large stock of affordable older homes alongside newer units and townhouses developed over the past two decades.</p>
      <h2>Older Homes — What to Watch For</h2>
      <p>Many Belmont rentals are 1970s–1990s brick homes with features that need specific attention:</p>
      <ul class="checklist">
        <li>Older bathroom tiles and grout — may require multiple cleaning applications for mould</li>
        <li>Aluminium window frames — oxidise and collect grime in the tracks</li>
        <li>Carpet throughout — steam cleaning commonly specified in older home leases</li>
        <li>Older rangehood designs — difficult to access all interior surfaces</li>
        <li>Separate laundry with fibreglass tub — requires specific cleaner to avoid scratching</li>
      </ul>
      <h2>What Belmont Property Managers Check</h2>
      <p>Belmont property managers tend to be thorough on the basics. The most commonly flagged items are the oven, carpets, and bathroom grout. With a professional bond clean and the REIWA checklist, these areas are covered comprehensively.</p>
      <h2>Typical Costs in Belmont</h2>
      <ul class="checklist">
        <li>2-bedroom unit: $310–$430</li>
        <li>3-bedroom house: $400–$560</li>
        <li>4-bedroom house: $520–$700</li>
        <li>Carpet steam cleaning (whole house): $130–$200</li>
      </ul>
      <h2>We Service All of Belmont</h2>
      <p>Our cleaners regularly work across Belmont, Rivervale, and surrounding suburbs. Get a quote today — same-day and next-day availability is often possible on weekdays outside of month-end.</p>
"""
  },
  {
    "slug": "blog-bond-cleaning-willetton",
    "title": "Bond Cleaning Willetton Perth — What Renters Need to Know",
    "h1": "Bond Cleaning Willetton Perth — Renter's Exit Clean Guide",
    "tag": "Suburbs",
    "meta": "Bond cleaning in Willetton covers family homes in one of Perth's most popular southern suburbs. What property managers check and how to pass your exit inspection.",
    "read_time": 4,
    "excerpt": "Willetton is a family-oriented southern suburb with a large stock of 3 and 4-bedroom homes. Bond cleaning here typically involves carpets, garages, and established gardens — here's what renters need to know.",
    "content": """
      <p>Willetton is one of Perth's most popular family suburbs, known for its good schools and quiet residential streets. The rental stock is dominated by 3 and 4-bedroom family homes, making it a suburb where bond cleans tend to be larger in scope and higher in cost than inner-city apartments.</p>
      <h2>Typical Willetton Rental Properties</h2>
      <p>Most Willetton rentals are 3 or 4-bedroom brick homes from the 1980s to 2000s. Common features include:</p>
      <ul class="checklist">
        <li>Carpet in bedrooms and often the main living areas</li>
        <li>Double garage</li>
        <li>Large backyard with lawn</li>
        <li>Established garden beds</li>
        <li>Alfresco or patio area</li>
        <li>Sometimes a pool</li>
      </ul>
      <h2>What Property Managers Focus On in Willetton</h2>
      <p>Family homes in Willetton exit inspections focus heavily on:</p>
      <ul class="checklist">
        <li>Carpet condition throughout — must be professionally steam cleaned if specified in lease</li>
        <li>Backyard and garden — lawns mowed, gardens weeded</li>
        <li>Garage — floor swept, oil stains treated</li>
        <li>Kitchen oven and rangehood after years of family cooking</li>
        <li>Multiple bathrooms to the same standard</li>
      </ul>
      <h2>Typical Bond Clean Costs for Willetton</h2>
      <ul class="checklist">
        <li>3-bedroom, 1-bathroom: $400–$540</li>
        <li>3-bedroom, 2-bathroom: $440–$600</li>
        <li>4-bedroom, 2-bathroom: $540–$720</li>
        <li>Double garage add-on: $80–$120</li>
        <li>Carpet steam cleaning: $150–$220</li>
      </ul>
      <p>Book at least 2 weeks before your exit inspection date. Contact us for a fixed-price Willetton bond cleaning quote.</p>
"""
  },
  {
    "slug": "blog-bond-cleaning-gosnells",
    "title": "Bond Cleaning Gosnells Perth — What Renters Need to Know",
    "h1": "Bond Cleaning Gosnells Perth — Renter's Guide",
    "tag": "Suburbs",
    "meta": "Bond cleaning in Gosnells covers established family homes and affordable rental properties. What property managers check and how to get your full bond back.",
    "read_time": 4,
    "excerpt": "Gosnells is an affordable southeastern suburb with a large stock of established homes and units. Bond cleaning here follows the REIWA standard — here's what Gosnells renters need to know about exit cleans.",
    "content": """
      <p>Gosnells is one of Perth's larger southeastern suburbs, with a mix of older affordable homes and newer developments. It's a popular suburb for families and first-time renters, with a strong demand for professional bond cleaning services at month-ends.</p>
      <h2>Property Types in Gosnells</h2>
      <p>Gosnells rentals range from 1970s and 1980s brick homes to newer group housing and units. Older properties often have:</p>
      <ul class="checklist">
        <li>Carpet in all bedrooms and living areas</li>
        <li>Older bathroom configurations — separate bath and shower in some</li>
        <li>Single-car garages</li>
        <li>Larger block sizes with established gardens</li>
      </ul>
      <h2>What to Know About Older Gosnells Properties</h2>
      <p>Older rental homes can accumulate significant grime in less-obvious areas after years of tenancy. When preparing for your exit inspection:</p>
      <ul class="checklist">
        <li>Check behind and under the stove — older stoves have more gaps for grease to collect</li>
        <li>Clean the laundry window — often overlooked but always checked</li>
        <li>Check the hot water system area if accessible — dust and cobwebs accumulate here</li>
        <li>Old roller blinds — may need replacement if broken, not just cleaned</li>
      </ul>
      <h2>Typical Costs in Gosnells</h2>
      <ul class="checklist">
        <li>2-bedroom unit: $300–$420</li>
        <li>3-bedroom house: $390–$540</li>
        <li>4-bedroom house: $510–$680</li>
        <li>Carpet steam cleaning: $120–$190</li>
      </ul>
      <p>We service Gosnells and surrounding southeastern suburbs including Maddington, Kenwick, and Martin. Contact us for a quote.</p>
"""
  },
  {
    "slug": "blog-bond-cleaning-wanneroo",
    "title": "Bond Cleaning Wanneroo Perth — What Renters Need to Know",
    "h1": "Bond Cleaning Wanneroo Perth — Renter's Exit Clean Guide",
    "tag": "Suburbs",
    "meta": "Bond cleaning in Wanneroo covers new and established family homes in Perth's northern growth corridor. What property managers check and how to get your bond back.",
    "read_time": 4,
    "excerpt": "Wanneroo is part of Perth's northern growth corridor with a mix of brand-new homes and established properties. Bond cleaning here has specific considerations for both new builds and older homes.",
    "content": """
      <p>Wanneroo is at the centre of Perth's northern growth corridor, with a large number of newer rental properties alongside older established homes. The suburb's rental market includes everything from new house-and-land packages to older 3-bedroom brick homes from the 1980s and 1990s.</p>
      <h2>New Properties — Specific Considerations</h2>
      <p>Brand-new properties and properties less than 5 years old are held to a higher standard at exit because the ingoing condition report documented pristine condition. Key areas in newer Wanneroo homes:</p>
      <ul class="checklist">
        <li>Oven — builders' ovens are often premium models with multiple racks and glass surfaces</li>
        <li>Double garage — concrete floor must be clean, builders' grout residue from move-in shouldn't be on you</li>
        <li>Alfresco area — often large in newer homes, floor and ceiling included</li>
        <li>Multiple bathrooms to identical standards</li>
        <li>Ducted air conditioning — check filter location and clean thoroughly</li>
      </ul>
      <h2>Older Wanneroo Properties</h2>
      <p>Established homes in older parts of Wanneroo follow standard REIWA requirements. Carpet is common throughout, and single or double garages are the norm. These properties typically have more wear in their ingoing condition reports — work from your ingoing PCR to understand the standard you need to meet.</p>
      <h2>Typical Costs in Wanneroo</h2>
      <ul class="checklist">
        <li>3-bedroom, 1-bathroom: $400–$540</li>
        <li>4-bedroom, 2-bathroom: $540–$720</li>
        <li>Ducted AC filter cleaning: included in our standard service</li>
        <li>Double garage add-on: $80–$120</li>
        <li>Carpet steam cleaning: $150–$220</li>
      </ul>
      <p>We service all of Wanneroo and the northern corridor including Joondalup, Clarkson, and Mindarie. Get a quote today.</p>
"""
  },
  {
    "slug": "blog-bond-cleaning-cockburn-central",
    "title": "Bond Cleaning Cockburn Central Perth — What Renters Need to Know",
    "h1": "Bond Cleaning Cockburn Central Perth — Renter's Guide",
    "tag": "Suburbs",
    "meta": "Bond cleaning in Cockburn Central covers apartments and townhouses in Perth's fast-growing southern hub. What property managers check and how to pass your exit inspection.",
    "read_time": 4,
    "excerpt": "Cockburn Central is one of Perth's fastest-growing southern suburbs, dominated by modern apartments and townhouses. Bond cleaning here has specific requirements for newer builds — here's what renters need to know.",
    "content": """
      <p>Cockburn Central has grown rapidly over the past decade into one of Perth's key southern hubs. The rental market is dominated by modern apartments and townhouses, making it one of the few Perth suburbs where the majority of bond cleans are for newer builds.</p>
      <h2>Modern Apartment and Townhouse Requirements</h2>
      <p>Newer Cockburn Central properties typically feature:</p>
      <ul class="checklist">
        <li>Stone or engineered stone benchtops — clean with pH-neutral cleaner, avoid acid-based products</li>
        <li>Stainless steel appliances — streak-free finish required</li>
        <li>Tiled floors throughout — grout lines get attention at inspection</li>
        <li>Split-system air conditioning — filters must be cleaned</li>
        <li>Balcony or courtyard — always included in the inspection</li>
        <li>Double lock-up garage (many townhouses) — floor swept and door clean</li>
      </ul>
      <h2>What Property Managers Check in Cockburn Central</h2>
      <p>Because most properties are new or nearly new, ingoing condition reports document pristine condition. Property managers inspect to that standard — there's little room for ambiguity about what was there at the start. The most common issues at exit:</p>
      <ul class="checklist">
        <li>Grout in bathrooms and kitchen — even new grout stains within 12 months</li>
        <li>Oven door glass — hard to clean without the right technique</li>
        <li>Balcony glass or screens — salt and dust accumulate quickly</li>
        <li>AC filters — often the first question from property managers</li>
      </ul>
      <h2>Typical Costs</h2>
      <ul class="checklist">
        <li>2-bedroom, 2-bathroom apartment: $380–$500</li>
        <li>3-bedroom townhouse: $440–$600</li>
        <li>4-bedroom townhouse with double garage: $580–$780</li>
      </ul>
      <p>Contact us for a fixed-price quote for your Cockburn Central property. We service all southern suburbs.</p>
"""
  },
  {
    "slug": "blog-eco-friendly-bond-cleaning-perth",
    "title": "Eco-Friendly Bond Cleaning in Perth — Green Options That Still Pass Inspection",
    "h1": "Eco-Friendly Bond Cleaning in Perth — Can You Go Green and Still Pass?",
    "tag": "Guides",
    "meta": "Can you use eco-friendly cleaning products for a Perth bond clean and still pass the exit inspection? The honest answer, and which green alternatives actually work.",
    "read_time": 4,
    "excerpt": "More Perth renters are asking about eco-friendly options for their bond clean. Can you use green cleaning products and still pass the REIWA exit inspection? The honest answer may surprise you.",
    "content": """
      <p>Environmental awareness has increased significantly among Perth renters, and more people are asking whether their bond clean can be done with eco-friendly products. The short answer: yes — but with important caveats.</p>
      <h2>Where Eco-Friendly Products Work Well</h2>
      <p>For general surface cleaning, plant-based and biodegradable cleaners have become genuinely effective. Good eco-friendly options for:</p>
      <ul class="checklist">
        <li>General surface wiping — plant-based all-purpose cleaners work as well as conventional</li>
        <li>Glass and windows — vinegar-based glass cleaners perform well</li>
        <li>Floors — biodegradable floor cleaners are largely equivalent</li>
        <li>Skirting boards and walls — mild eco-cleaners handle dust and light marks</li>
        <li>Light fixtures — a damp eco-cloth is all that's needed</li>
      </ul>
      <h2>Where Eco-Friendly Products Struggle</h2>
      <p>There are areas where the chemistry of conventional cleaners is genuinely hard to match:</p>
      <ul class="checklist">
        <li><strong>Oven grease</strong> — heavy carbonised grease requires strong alkaline chemistry. Most eco-oven cleaners require significantly longer dwell times and more physical effort</li>
        <li><strong>Shower screen mineral deposits</strong> — Perth's hard water needs acid-based descalers. White vinegar works for light buildup; heavy deposits need stronger solutions</li>
        <li><strong>Mould in grout</strong> — effective mould treatment requires bleach or hydrogen peroxide. Some eco-brands use hydrogen peroxide, which works but more slowly</li>
        <li><strong>Rangehood filters</strong> — heavy grease buildup responds best to strong degreaser chemistry</li>
      </ul>
      <h2>A Practical Hybrid Approach</h2>
      <p>For most eco-conscious renters, the most effective approach is a hybrid: eco-friendly products for general cleaning (70% of the work) and targeted conventional products for the specific problem areas (oven, shower screen, mould). This significantly reduces chemical use while ensuring inspection-standard results.</p>
      <h2>Professional Eco-Friendly Bond Cleaning</h2>
      <p>Some Perth bond cleaning companies offer eco-friendly product options on request. Ask specifically when booking — the default is usually conventional commercial products. If eco-cleaning is a priority for you, mention it when requesting your quote.</p>
"""
  },
  {
    "slug": "blog-how-to-photograph-rental-property",
    "title": "How to Photograph Your Rental Property for Bond Protection",
    "h1": "How to Photograph Your Rental Property — A Complete Guide for Perth Renters",
    "tag": "Guides",
    "meta": "Date-stamped photos are your best protection in a Perth bond dispute. How to photograph your rental at move-in and move-out to protect your full bond.",
    "read_time": 4,
    "excerpt": "Date-stamped photos are your best protection against unfair bond deductions. How to photograph your rental at move-in and move-out to create evidence that holds up in a dispute.",
    "content": """
      <p>The most common reason Perth tenants lose bond money they shouldn't is a lack of documentation. Property managers will say damage occurred during your tenancy; without photos, you have no way to prove otherwise. Here's how to photograph your rental properly — at move-in and at move-out.</p>
      <h2>Move-In Photography — What to Capture</h2>
      <p>Do this before moving any furniture in. Every photo should have a date stamp visible — most modern phones embed the date in file metadata, but also check your camera settings for on-image date display.</p>
      <ul class="checklist">
        <li>Every room from multiple angles — wide shot, then close-up of any marks or damage</li>
        <li>Every wall — specifically scuffs, marks, holes, and paint condition</li>
        <li>Every window — condition of glass, frame, sill, and track</li>
        <li>Every blind and curtain — condition of slats, vanes, cords, and hems</li>
        <li>Oven interior — the pre-existing state of the cavity and racks</li>
        <li>Rangehood — filters and housing condition</li>
        <li>All bathroom tiles and grout — existing mould or discolouration</li>
        <li>Carpets — any stains, worn areas, or damage</li>
        <li>Garage floor — existing oil stains or concrete damage</li>
        <li>Outdoor areas — garden, lawn, and any existing damage</li>
      </ul>
      <h2>Move-Out Photography — What to Capture</h2>
      <p>After the bond clean is complete and before handing back keys. This set of photos is your evidence that the property was left in excellent condition.</p>
      <ul class="checklist">
        <li>Every room after cleaning — wide shots showing clean condition</li>
        <li>Oven cavity — before and after comparison is ideal</li>
        <li>Shower screen — show the clean glass clearly</li>
        <li>All bathrooms — tile, grout, toilet, and vanity</li>
        <li>Garage floor — show the swept, clean state</li>
        <li>Outdoor areas — mowed lawn, clean alfresco</li>
      </ul>
      <h2>How to Store Your Photos</h2>
      <p>Don't rely solely on your phone. After photographing, immediately back up to cloud storage (Google Photos, iCloud, or similar). These services automatically tag photos with date and time. Store the move-in and move-out sets in separate folders labelled clearly. Keep them for at least 12 months after your bond is refunded.</p>
      <h2>What Happens Without Photos</h2>
      <p>Without documentation, a dispute becomes your word against the property manager's. Courts and tribunals have to assess the balance of probabilities — and a property manager with an outgoing condition report noting an issue has a significant evidential advantage over a tenant with no documentation. Don't put yourself in that position.</p>
"""
  },
  {
    "slug": "blog-bond-cleaning-after-long-tenancy",
    "title": "Bond Cleaning After a Long Tenancy in Perth — What's Different",
    "h1": "Bond Cleaning After a Long Tenancy in Perth — What You Need to Know",
    "tag": "Guides",
    "meta": "Moving out after 5+ years in a Perth rental? Bond cleaning after a long tenancy has specific considerations around fair wear and tear, accumulated grime, and what you're actually required to do.",
    "read_time": 5,
    "excerpt": "Moving out after 5, 7, or 10 years in a Perth rental? The bond clean is bigger, there's more accumulated wear, and the fair wear and tear rules work in your favour more than you might think.",
    "content": """
      <p>Leaving a rental you've lived in for 5 years or more is a different proposition to a short-term tenancy exit. The accumulated wear is greater, the bond clean scope is larger, and the fair wear and tear rules become increasingly important in protecting your bond. Here's what long-term Perth tenants need to know.</p>
      <h2>Fair Wear and Tear Is on Your Side</h2>
      <p>The longer a tenancy, the more fair wear and tear has accumulated — and the less a landlord can legitimately claim. After 5+ years:</p>
      <ul class="checklist">
        <li>Carpet that was new at move-in has significantly depreciated — even substantial wear may not be chargeable</li>
        <li>Paint and wall condition — repainting after a long tenancy is often considered a landlord maintenance cost</li>
        <li>Minor marks and scuffs that would concern a property manager in a 12-month tenancy may be accepted as normal in a 7-year one</li>
        <li>Old appliances — a landlord cannot claim full replacement cost for appliances that were already approaching end-of-life</li>
      </ul>
      <h2>What Still Needs to Meet the Standard</h2>
      <p>Fair wear and tear doesn't excuse poor cleaning. Regardless of tenancy length, you still need to return the property in a reasonable state of cleanliness. Years of cooking means a very dirty oven — that's cleaning, not wear and tear. Mould from insufficient ventilation is still your responsibility. The distinction is between deterioration from normal use versus accumulated dirt and damage.</p>
      <h2>The Practical Challenge — Accumulated Grime</h2>
      <p>In a long tenancy, grime accumulates in places nobody cleans regularly: the top of kitchen cupboards, behind the stove, inside the rangehood housing, in window tracks, and behind appliances. A professional bond clean addresses all of these systematically. For a very long tenancy, the cleaning job is often significantly larger than a standard quote would reflect — be upfront with your cleaner about the property's condition and tenure.</p>
      <h2>Documenting the Ingoing Condition</h2>
      <p>If you've been in the property for 5+ years, your ingoing condition report is from years ago. Retrieve a copy from your property manager — it's the baseline for any exit claim. Items that were already in poor condition when you moved in cannot be charged to you now.</p>
      <h2>Getting the Right Quote</h2>
      <p>Be honest with your bond cleaner about the property's condition. A property that hasn't had a deep clean in years takes significantly longer than a well-maintained property — and a realistic quote at the start prevents surprises on the day.</p>
"""
  },
  {
    "slug": "blog-bond-cleaning-after-short-tenancy",
    "title": "Bond Cleaning After a Short Tenancy in Perth (3–12 Months)",
    "h1": "Bond Cleaning After a Short Tenancy in Perth — What to Expect",
    "tag": "Guides",
    "meta": "Moving out of a Perth rental after only 3–12 months? Short tenancies have specific bond cleaning considerations — higher standards, less wear and tear allowance, and a more scrutinised exit.",
    "read_time": 4,
    "excerpt": "Short-tenancy exits in Perth are often more scrutinised than longer ones. Property managers know the property was barely worn in, and standards are correspondingly high. Here's what short-tenancy renters need to know.",
    "content": """
      <p>Moving out of a Perth rental after just a few months is common — people relocate for work, circumstances change, or a fixed-term lease ends early. Short tenancies have a specific dynamic at exit: the property was barely worn in, and the property manager knows it.</p>
      <h2>The Higher Standard in Short Tenancies</h2>
      <p>In a short tenancy, there's very little fair wear and tear to speak of. The property should look almost as good as it did on the day you moved in. This means:</p>
      <ul class="checklist">
        <li>Any mark on a wall that wasn't there at the start will be noted</li>
        <li>Any stain in the carpet is not wear and tear — it's damage</li>
        <li>Any buildup in the oven or rangehood will be questioned — it accumulated in your tenancy</li>
        <li>Grout that has moulded in just a few months suggests inadequate ventilation — your responsibility</li>
      </ul>
      <h2>What Works in Your Favour</h2>
      <p>The flip side: a short tenancy means less accumulated grime overall. The oven buildup is from your cooking, not decades of tenants. The bond clean scope is the same, but the starting point is usually better. A thorough clean of a well-maintained short-tenancy property is achievable — and the cost should be on the lower end of the pricing scale.</p>
      <h2>Breaking Lease Early</h2>
      <p>If you're leaving before the end of a fixed-term lease, you'll have additional obligations around break fees and re-letting costs on top of the bond clean. Get clear written confirmation of all financial obligations before your move-out date. The bond clean itself is separate from any lease-break costs.</p>
      <h2>Documentation Is Even More Important</h2>
      <p>With a short tenancy, your ingoing condition report is recent — and you should have photos from move-in that are still clearly relevant. Use these at the exit inspection. If a property manager claims damage that was present at the start, your documentation should be clear and fresh.</p>
      <h2>Cost of a Short-Tenancy Bond Clean</h2>
      <p>Because the property has had limited wear, the clean is often faster and cheaper than a long-tenancy equivalent. A 2-bedroom apartment after 6 months: $300–$420. Contact us for a specific quote for your property.</p>
"""
  },
  {
    "slug": "blog-first-time-renter-bond-perth",
    "title": "First-Time Renter in Perth — Everything You Need to Know About Your Bond",
    "h1": "First-Time Renter in Perth — A Complete Guide to Your Bond",
    "tag": "Guides",
    "meta": "First-time renters in Perth need to understand how bonds work, how to protect them from day one, and what's needed to get them back in full at exit.",
    "read_time": 6,
    "excerpt": "If you're renting in Perth for the first time, your bond is usually the biggest upfront cost — and understanding how to protect it from day one is essential. A complete guide for first-timers.",
    "content": """
      <p>Renting for the first time in Perth involves a lot of firsts — first lease, first bond payment, first property manager relationship. Of all the things you need to understand, the bond is the most financially significant. Here's a complete guide for first-time Perth renters.</p>
      <h2>What Is a Bond?</h2>
      <p>A bond (also called a security deposit) is a sum of money — typically 4 weeks' rent — paid at the start of your tenancy and held in trust by the WA Bond Administrator. It's not the landlord's money. It's held to cover any legitimate costs at the end of the tenancy: unpaid rent, cleaning beyond a reasonable standard, or damage beyond fair wear and tear. If none of these apply, you get it back in full.</p>
      <h2>The Ingoing Inspection — Your Most Important Moment</h2>
      <p>Before you sign anything or pay your bond, walk through the property with the ingoing Property Condition Report in hand. Document every imperfection — every mark on a wall, every stain in the carpet, every scratch on a floor. Take date-stamped photos. If you find something after you've signed, report it to your property manager in writing within 5 days. This documentation is your protection when you leave.</p>
      <h2>Your Responsibilities During the Tenancy</h2>
      <ul class="checklist">
        <li>Pay rent on time — unpaid rent is the most common bond deduction</li>
        <li>Report maintenance issues in writing — this protects you from being blamed for problems that developed during your tenancy</li>
        <li>Ventilate bathrooms — mould from poor ventilation is a tenant responsibility</li>
        <li>Keep the property reasonably clean — not spotless, but maintained</li>
        <li>Don't make unapproved modifications — hanging things with large hooks, painting walls, or adding fixtures without permission</li>
      </ul>
      <h2>When You Leave — The Bond Clean</h2>
      <p>At exit, the property must be returned in a reasonable state of cleanliness consistent with the ingoing condition. A professional bond clean is the most reliable way to meet this standard — the cleaner works from the REIWA checklist, backs the work with a guarantee, and handles any re-clean if the property manager flags something.</p>
      <h2>Getting Your Bond Back</h2>
      <p>If the exit inspection goes well, your property manager submits the bond disposal form and you receive your bond refund within 3–5 business days. If there's a dispute, respond in writing promptly and don't accept deductions you don't believe are fair. See our <a href="blog-how-to-get-bond-back-perth.html" style="color:var(--green);">full guide to getting your bond back</a>.</p>
"""
  },
  {
    "slug": "blog-pest-control-vacate-cleaning-perth",
    "title": "Pest Control and Bond Cleaning in Perth — What Renters Need to Know",
    "h1": "Pest Control and Bond Cleaning in Perth — What's Required and When",
    "tag": "Guides",
    "meta": "Some Perth leases require flea treatment or pest control at exit. How to know if it applies to you, what's required, and how it fits with your bond clean.",
    "read_time": 4,
    "excerpt": "Some Perth leases require professional pest control or flea treatment at exit — especially if you've had pets. How to know if it applies to you, and how to coordinate it with your bond clean.",
    "content": """
      <p>Pest control and flea treatment at exit is an obligation many Perth renters don't think about until the last minute — then realise they needed to book a licensed pest controller in addition to a bond cleaner. Here's what you need to know.</p>
      <h2>Does Your Lease Require Pest Control at Exit?</h2>
      <p>Check your lease agreement. The most common scenarios where pest control is required:</p>
      <ul class="checklist">
        <li><strong>Flea treatment for pet-friendly tenancies</strong> — if your lease permitted pets, it almost certainly requires professional flea treatment by a licensed operator at exit</li>
        <li><strong>General pest control</strong> — some leases specify professional pest control for all tenants at exit</li>
        <li><strong>Specific infestations</strong> — if a pest infestation occurred during the tenancy (cockroaches, rodents), the property manager may require professional treatment</li>
      </ul>
      <h2>Flea Treatment — What's Involved</h2>
      <p>Professional flea treatment is performed by a licensed pest controller using registered products. The property must be vacated for treatment and remain vacant for the period specified by the pest controller (typically 2–4 hours). Treatment involves spraying all carpeted areas and soft furnishings. The pest controller provides a certificate — keep this receipt as your property manager will require it.</p>
      <h2>Timing — The Order of Operations</h2>
      <p>Get the sequence right:</p>
      <ul class="checklist">
        <li>Bond clean first — any pest treatment chemical on cleaned surfaces needs to dry and settle</li>
        <li>Flea treatment after the bond clean — carpets should be cleaned before treatment is applied</li>
        <li>Allow drying time — treatment needs to dry before the exit inspection</li>
        <li>Book both services at least 1–2 weeks before your exit inspection</li>
      </ul>
      <h2>What Pest Control Doesn't Cover</h2>
      <p>Pest control treats insects and vermin — it's not a cleaning service. Your bond clean still needs to be done to the full REIWA standard. Pest control is in addition to, not instead of, the bond clean.</p>
      <h2>Cost of Professional Flea Treatment in Perth</h2>
      <p>Professional flea treatment from a licensed pest controller in Perth typically costs $150–$300 depending on property size. Contact a licensed pest controller (separate to your bond cleaning company) — they need to be licensed to provide the required certificate.</p>
"""
  },
  {
    "slug": "blog-move-in-cleaning-perth",
    "title": "Move-In Cleaning Perth — Should You Clean Before You Unpack?",
    "h1": "Move-In Cleaning Perth — Should You Clean Before You Unpack?",
    "tag": "Guides",
    "meta": "Should you do a move-in clean before unpacking in your new Perth rental? What's the landlord's obligation, what you can request, and what to do if the property isn't clean.",
    "read_time": 4,
    "excerpt": "Moving into a new Perth rental that isn't as clean as you expected? Your landlord has obligations — and knowing them upfront saves you from inheriting cleaning costs you shouldn't have to pay.",
    "content": """
      <p>Starting a new Perth tenancy in a property that isn't spotlessly clean is frustrating — and it can also cost you money at exit if you don't handle it correctly from day one. Here's what to know about move-in cleaning.</p>
      <h2>The Landlord's Obligation</h2>
      <p>Under the Residential Tenancies Act 1987 (WA), a landlord is required to provide a rental property in a reasonable state of cleanliness at the start of a tenancy. "Reasonable" is the operative word — it doesn't mean professionally cleaned, but it shouldn't be dirty.</p>
      <p>If a previous tenant's professional bond clean was required by their lease, the property should be in good condition. If the property was vacant for a period, dust accumulation is common but heavy grime is not acceptable.</p>
      <h2>What to Do If the Property Isn't Clean</h2>
      <p>Before you unpack:</p>
      <ul class="checklist">
        <li>Document everything — date-stamped photos of every area that isn't clean</li>
        <li>Note all issues in writing on the ingoing Property Condition Report</li>
        <li>Send a written email to your property manager noting the cleaning issues and requesting they be addressed or noted</li>
        <li>Keep a copy of all communication</li>
      </ul>
      <h2>Why This Matters at Exit</h2>
      <p>If you clean the property to a higher standard at exit than it was when you moved in, you've done work you shouldn't need to do. More importantly, if you moved into a dirty property without documenting it, you may be held responsible for that pre-existing state at exit. Document now to protect yourself later.</p>
      <h2>Move-In Cleaning — Do You Need a Professional?</h2>
      <p>If the property needs cleaning and your property manager isn't arranging it, you have two options: clean it yourself or hire a professional. A professional move-in clean costs $200–$500 depending on property size and gives you a fresh, documented starting point. It also often catches pre-existing issues that get noted and photographed as part of the service.</p>
      <h2>Keep Your Move-In Photos for the Entire Tenancy</h2>
      <p>Your move-in photos are your protection at exit — sometimes years later. Store them in cloud storage with a clear date stamp. Don't delete them until your bond is fully refunded at exit.</p>
"""
  },
  {
    "slug": "blog-how-long-bond-refund-takes-wa",
    "title": "How Long Does a Bond Refund Take in WA? (2025 Guide)",
    "h1": "How Long Does a Bond Refund Take in Western Australia?",
    "tag": "Bond",
    "meta": "How long does it take to get your bond back in WA in 2025? The timeline, what causes delays, and how to speed up your bond refund.",
    "read_time": 4,
    "excerpt": "How long does it actually take to get your bond back after moving out of a Perth rental? The timeline, what causes delays, and the steps you can take to speed it up.",
    "content": """
      <p>One of the most common questions from Perth renters after moving out is: when do I actually get my bond money back? The answer depends on a few variables, but here's the realistic timeline.</p>
      <h2>The Ideal Timeline (No Disputes)</h2>
      <ul class="checklist">
        <li><strong>Exit inspection:</strong> Day 0</li>
        <li><strong>Property manager submits bond disposal form:</strong> Day 1–5 (most submit within a few business days)</li>
        <li><strong>Bond Administrator processes the form:</strong> 3–5 business days</li>
        <li><strong>Funds in your account:</strong> Day 4–10 after the exit inspection</li>
      </ul>
      <p>When everything goes smoothly — clean inspection, no disputes, prompt paperwork — you can have your bond back within 1–2 weeks of moving out.</p>
      <h2>What Causes Delays</h2>
      <ul class="checklist">
        <li><strong>Disputed cleaning or damage:</strong> Back-and-forth negotiation can take weeks</li>
        <li><strong>Property manager slow to submit:</strong> Some agencies batch paperwork weekly rather than daily</li>
        <li><strong>Outstanding water or utility bills:</strong> These need to be calculated and agreed before the bond is released</li>
        <li><strong>Formal dispute process:</strong> If it goes to the Magistrates Court, it can take months</li>
        <li><strong>Outdated bank details:</strong> An old account number causes the refund to bounce and be re-processed</li>
      </ul>
      <h2>How to Speed It Up</h2>
      <ul class="checklist">
        <li>Pass the exit inspection first time — no disputes means the fastest possible refund</li>
        <li>Ask your property manager how quickly they typically process bond disposal forms</li>
        <li>Confirm your bank details with the Bond Administrator are current</li>
        <li>Respond promptly to any questions from your property manager — delays compound</li>
        <li>If you haven't received confirmation of the bond disposal within 2 weeks, follow up in writing</li>
      </ul>
      <h2>What the Bond Administrator Can Tell You</h2>
      <p>The WA Bond Administrator (Department of Mines, Industry Regulation and Safety) can confirm whether your bond is lodged and in what amount. Contact them at 1300 30 40 54 if you have concerns about the status of your bond. You can also verify online through the DMIRS tenant portal.</p>
"""
  },
  {
    "slug": "blog-rental-inspection-perth-tips",
    "title": "Routine Rental Inspections in Perth — How to Prepare and What to Expect",
    "h1": "Routine Rental Inspections in Perth — How to Prepare",
    "tag": "Guides",
    "meta": "Routine property inspections happen every 3–6 months in Perth rentals. How to prepare, what property managers look for, and how your routine inspection results affect your exit inspection.",
    "read_time": 4,
    "excerpt": "Routine rental inspections happen every 3–6 months in Perth. How you perform in these inspections can affect your exit experience — here's how to approach them.",
    "content": """
      <p>Routine inspections are a standard part of Perth renting — property managers typically conduct them every 3 to 6 months. Many tenants treat them as a nuisance; the smart approach is to treat them as an opportunity to document your tenancy and build a positive relationship with your property manager.</p>
      <h2>What Property Managers Check at Routine Inspections</h2>
      <p>Routine inspections are not as comprehensive as exit inspections — they're generally checking:</p>
      <ul class="checklist">
        <li>Overall cleanliness and tidiness of the property</li>
        <li>Any damage or maintenance issues that need reporting</li>
        <li>Compliance with lease conditions (no unapproved pets, no unauthorised people living there)</li>
        <li>Garden and outdoor area condition</li>
        <li>Signs of any unauthorised modifications</li>
      </ul>
      <h2>How to Prepare</h2>
      <ul class="checklist">
        <li>Tidy up — this doesn't mean deep-clean, but the property should be presentable</li>
        <li>Make a list of any maintenance issues you want to flag — routine inspections are the ideal time to report these in person</li>
        <li>Ensure any pets are contained or removed if your lease requires it</li>
        <li>Be present or arrange key access if you won't be home</li>
      </ul>
      <h2>How Routine Inspections Affect Your Exit</h2>
      <p>Property managers who have seen a property in poor condition at routine inspections will approach the exit inspection differently. Conversely, a property manager who has seen consistently well-maintained property throughout the tenancy is more likely to approach the exit with a positive disposition.</p>
      <p>Routine inspections also create documentation of the property's ongoing condition — a useful paper trail if anything is disputed at exit. Maintenance issues you raised at routine inspections (in writing or through inspection reports) create a record that the issue predates your departure.</p>
      <h2>If Your Property Manager Sends a Report After the Inspection</h2>
      <p>Respond to any issues raised in the inspection report promptly and in writing. If a property manager has flagged a cleaning issue at routine inspection and you address it, note this in writing. It demonstrates good faith and prevents the same issue being raised again at exit.</p>
"""
  },
  {
    "slug": "blog-summer-bond-cleaning-perth",
    "title": "Bond Cleaning in Perth Summer — Tips for the Heat",
    "h1": "Bond Cleaning in Perth Summer — What You Need to Know",
    "tag": "Guides",
    "meta": "Bond cleaning during Perth's hot summer has specific challenges — fast-drying products, heat-related grime, and scheduling around extreme weather. Tips for a successful summer exit clean.",
    "read_time": 4,
    "excerpt": "Perth summers are extreme — 40°C+ days, rapid product drying, and properties that have been running AC all season. Bond cleaning in summer has specific challenges that are worth knowing before you book.",
    "content": """
      <p>Perth's summer is no joke. Temperatures exceeding 40°C, months of air conditioning use, and intense UV exposure on windows and outdoor surfaces create specific conditions for a bond clean. Here's what to know if your move-out falls in Perth's warmer months.</p>
      <h2>Product Drying Time — A Summer Challenge</h2>
      <p>In Perth summer heat, cleaning products evaporate significantly faster than in cooler months. This can cause:</p>
      <ul class="checklist">
        <li>Glass cleaners drying before they're wiped — leaving streaks harder to remove than if cleaned in cooler conditions</li>
        <li>Oven degreaser drying before it's activated — needs to be applied more liberally and the area kept moist during dwell time</li>
        <li>Surface cleaners crystallising on benchtops — requiring a follow-up rinse pass</li>
      </ul>
      <p>Professional bond cleaners work around this — it's a known challenge that comes with experience. If you're doing it yourself, work room by room with the doors closed and avoid direct sunlight on surfaces you're cleaning.</p>
      <h2>Air Conditioning — Heavy Summer Use</h2>
      <p>Perth properties that have run their air conditioning all summer have filters that have been working overtime. Split-system filters are checked at exit inspections and should be cleaned as part of your bond clean. Don't overlook this — a visibly dirty filter is a quick easy note on the exit report.</p>
      <h2>Windows — UV Exposure and Insects</h2>
      <p>Perth's intense UV can cause mineral deposits on external windows to bake on over summer, making them harder to clean. Internal windows should still be clean, but be aware that heavily UV-damaged external glass may show marks even after cleaning.</p>
      <p>Perth summers also bring more insects — dead insects in light fittings and on windowsills are common and need to be cleared as part of the bond clean.</p>
      <h2>Outdoor Areas in Summer</h2>
      <p>Gardens and outdoor areas need to be in good condition at exit regardless of season. Perth's summer heat makes lawn maintenance harder — if the grass has died or patched significantly during extreme heat, the ingoing condition report is your guide to what the landlord can legitimately claim.</p>
      <h2>Scheduling</h2>
      <p>Book your summer bond clean early in the morning to avoid the worst heat — most professional bond cleaners schedule summer jobs for 7:00–8:00am starts. The property should have some cooling running (or at least shade) for the duration of the clean.</p>
"""
  },
  {
    "slug": "blog-bond-cleaning-brand-new-apartment",
    "title": "Bond Cleaning a Brand-New Apartment in Perth — What You Need to Know",
    "h1": "Bond Cleaning a Brand-New Apartment in Perth — What to Expect",
    "tag": "Guides",
    "meta": "Moving out of a brand-new Perth apartment? Exit inspections for new builds are held to the highest standard. What property managers look for and how to meet the bar.",
    "read_time": 4,
    "excerpt": "Brand-new apartments are held to the highest exit standard — the ingoing condition was pristine and the property manager knows it. Here's what renters in brand-new Perth apartments need to know.",
    "content": """
      <p>Moving into a brand-new apartment is exciting. Moving out of one requires careful thought — because the exit standard is the highest possible. The ingoing condition report documented pristine, developer-finished condition, and that's the benchmark the property manager will use at exit.</p>
      <h2>Why New Apartments Are Different</h2>
      <p>In an older property, the ingoing condition report might note pre-existing grout discolouration, minor wall scuffs, or a worn oven cavity. None of these will be on a brand-new property's ingoing report. The baseline is perfect condition — which means you're held to a higher standard at exit than a tenant in a 10-year-old property.</p>
      <h2>What Property Managers Focus On in New Apartments</h2>
      <ul class="checklist">
        <li><strong>Stone benchtops</strong> — any etching from acidic foods or cleaners is noted. Use pH-neutral cleaners only.</li>
        <li><strong>Grouting</strong> — new grout stains quickly. Mould in bathroom grout after even a 12-month tenancy will be flagged.</li>
        <li><strong>Stainless steel appliances</strong> — scratches from incorrect cleaning are noted. Use stainless-steel specific cleaners and cloths.</li>
        <li><strong>Timber-look flooring</strong> — swelling or warping from moisture, scratches from furniture</li>
        <li><strong>Painted walls</strong> — new paint shows any mark clearly. Magic eraser use requires care — can dull the finish.</li>
        <li><strong>Oven door glass</strong> — premium ovens have larger, more prominent glass that shows grease clearly</li>
      </ul>
      <h2>What You Can't Be Charged For</h2>
      <p>Even in a new apartment, fair wear and tear applies. Light surface marks on flooring from normal furniture use over a 12-month tenancy are not your liability. Grout that has discoloured evenly from normal showering is different from mould caused by inadequate ventilation. Know the distinction.</p>
      <h2>The Safest Approach</h2>
      <p>For a brand-new apartment, professional bond cleaning is the clear choice. The finishes are premium, the standard is high, and the guarantee means any re-clean is handled at no cost. Contact us for a quote specific to your new build.</p>
"""
  },
  {
    "slug": "blog-carpet-professional-vs-diy-cleaning",
    "title": "Professional vs DIY Carpet Cleaning for Your Bond — Perth Guide",
    "h1": "Professional vs DIY Carpet Cleaning for Bond Inspections in Perth",
    "tag": "Carpet",
    "meta": "Does DIY carpet cleaning pass Perth bond inspections? A comparison of professional steam cleaning vs DIY options — when each is acceptable and when you need a professional.",
    "read_time": 5,
    "excerpt": "Can a hired carpet cleaner from Bunnings or a DIY machine pass a Perth bond inspection? The honest comparison of professional vs DIY carpet cleaning, and when your lease may decide for you.",
    "content": """
      <p>Hire machines from hardware stores and professional steam cleaning services both exist in Perth — and the price difference is significant. So when can you use a DIY carpet cleaning machine for your bond, and when do you need to pay for a professional?</p>
      <h2>What Your Lease Says — The Deciding Factor</h2>
      <p>Many Perth leases specify "professional carpet steam cleaning by a licensed operator" as a condition of exit. If your lease says this, there's no choice — a DIY machine from Bunnings doesn't satisfy the requirement. Your property manager will ask for a receipt from a licensed cleaning company. Without it, you'll be charged for professional cleaning regardless of what you did.</p>
      <p>If your lease just says "carpets to be steam cleaned" without specifying professional, there's more flexibility — but read it carefully and ask your property manager for clarification before assuming DIY is acceptable.</p>
      <h2>The Performance Difference</h2>
      <p>Hire machines from supermarkets and hardware stores use hot water extraction — the same basic process as professional machines. The difference is in power:</p>
      <ul class="checklist">
        <li><strong>Water pressure:</strong> Professional truck-mounted systems operate at 200–300 PSI; hire machines at 50–100 PSI</li>
        <li><strong>Temperature:</strong> Professional systems use water at 80–100°C; hire machines often achieve 60–70°C</li>
        <li><strong>Extraction power:</strong> Professional systems extract far more moisture — hire machine carpets take 12–24 hours to dry vs 4–6 hours for professional</li>
        <li><strong>Pre-treatment:</strong> Professional operators apply pre-treatment for stains; hire machines typically don't include this step</li>
      </ul>
      <h2>When DIY Is Adequate</h2>
      <p>For lightly-used carpet in good condition with no significant staining and a lease that doesn't specify professional cleaning, a hire machine can produce acceptable results. Key requirements: vacuum thoroughly before wet-cleaning, use appropriate carpet cleaning solution, don't over-wet the carpet, and allow full drying time before the inspection.</p>
      <h2>When Professional Is Required</h2>
      <ul class="checklist">
        <li>Your lease specifies professional or licensed cleaning</li>
        <li>There are significant stains that need pre-treatment</li>
        <li>Pet odour is present — requires enzyme treatment, not just steam</li>
        <li>Carpets are high-pile or natural fibre (wool) — hire machines can damage these</li>
        <li>You want the protection of a receipt for dispute purposes</li>
      </ul>
"""
  },
  {
    "slug": "blog-bond-cleaning-osborne-park",
    "title": "Bond Cleaning Osborne Park Perth — What Renters Need to Know",
    "h1": "Bond Cleaning Osborne Park Perth — Renter's Guide",
    "tag": "Suburbs",
    "meta": "Bond cleaning in Osborne Park covers a mix of apartments, units, and commercial-adjacent rentals. What property managers check and how to get your full bond back.",
    "read_time": 4,
    "excerpt": "Osborne Park is an inner-northern suburb with a mix of residential apartments and the occasional converted or commercial-adjacent property. Here's what renters need to know about bond cleans in Osborne Park.",
    "content": """
      <p>Osborne Park sits between the inner northern suburbs and commercial areas along Scarborough Beach Road. It has a diverse rental mix — from standalone houses to apartment complexes — and a range of property ages from mid-century to recently developed.</p>
      <h2>Property Types in Osborne Park</h2>
      <p>Osborne Park's rental stock includes:</p>
      <ul class="checklist">
        <li>Older brick homes from the 1960s–1980s</li>
        <li>Newer apartment and unit complexes</li>
        <li>Townhouses and group housing developments</li>
        <li>Some converted properties (former commercial spaces)</li>
      </ul>
      <h2>What to Watch For in Osborne Park Properties</h2>
      <p>Older Osborne Park properties often have:</p>
      <ul class="checklist">
        <li>Aluminium window frames — tracks accumulate rust and grime that needs specific treatment</li>
        <li>Older bathroom configurations with full-size baths</li>
        <li>Laundries with older tub and tapware that need careful cleaning to avoid scratching</li>
        <li>Sometimes evaporative cooling rather than split systems — pads need cleaning</li>
      </ul>
      <h2>Newer Developments</h2>
      <p>Modern apartment buildings in Osborne Park have the standard requirements: AC filter cleaning, stainless steel appliances, balcony cleaning, and grout maintenance. These properties are held to the same standard as apartments anywhere else in Perth's inner suburbs.</p>
      <h2>Typical Costs in Osborne Park</h2>
      <ul class="checklist">
        <li>1-bedroom unit: $270–$370</li>
        <li>2-bedroom apartment: $360–$490</li>
        <li>3-bedroom house: $430–$580</li>
      </ul>
      <p>We service all of Osborne Park and surrounding suburbs including Innaloo, Stirling, and Balcatta. Contact us for a quote.</p>
"""
  },
  {
    "slug": "blog-bond-cleaning-innaloo",
    "title": "Bond Cleaning Innaloo Perth — What Renters Need to Know",
    "h1": "Bond Cleaning Innaloo Perth — Renter's Exit Clean Guide",
    "tag": "Suburbs",
    "meta": "Bond cleaning in Innaloo covers units and family homes close to Westfield Innaloo and Perth's northern beaches. What property managers check at exit inspection.",
    "read_time": 4,
    "excerpt": "Innaloo is a popular inner-northern suburb with easy access to the northern beaches and Westfield. Bond cleaning here covers a mix of units and family homes — here's what renters need to know.",
    "content": """
      <p>Innaloo is a convenient inner-northern suburb popular with families and young professionals, close to public transport, Westfield Innaloo, and the northern beaches corridor. It has a mix of older home stock and newer unit developments.</p>
      <h2>What's Common in Innaloo Rentals</h2>
      <p>Innaloo's rental stock includes older brick homes and newer group housing and apartment complexes. Most properties have:</p>
      <ul class="checklist">
        <li>Reverse-cycle or split-system air conditioning</li>
        <li>Some carpet in bedrooms (particularly in older homes)</li>
        <li>Backyard and garage in standalone homes</li>
        <li>Balcony or courtyard in apartments and townhouses</li>
      </ul>
      <h2>What Property Managers Check in Innaloo</h2>
      <p>Innaloo property managers follow the standard REIWA checklist with particular attention to:</p>
      <ul class="checklist">
        <li>Oven and cooktop — standard focus in any property</li>
        <li>Bathroom grout and shower screen — high humidity from Perth's warmer climate</li>
        <li>Air conditioning filters — essential given Perth summer temperatures</li>
        <li>Carpet condition — steam cleaning often required in older homes</li>
        <li>Garage floor in standalone homes</li>
      </ul>
      <h2>Typical Costs in Innaloo</h2>
      <ul class="checklist">
        <li>1-bedroom unit: $270–$360</li>
        <li>2-bedroom unit: $340–$470</li>
        <li>3-bedroom house: $420–$570</li>
        <li>Carpet steam cleaning: $100–$180</li>
      </ul>
      <p>We service Innaloo and all surrounding northern suburbs. Get a fixed-price quote from us — we respond within the hour.</p>
"""
  },
  {
    "slug": "blog-bond-cleaning-spearwood",
    "title": "Bond Cleaning Spearwood Perth — What Renters Need to Know",
    "h1": "Bond Cleaning Spearwood Perth — Renter's Guide",
    "tag": "Suburbs",
    "meta": "Bond cleaning in Spearwood covers family homes in Perth's southern coastal suburbs. What property managers check at exit inspection and how to get your full bond back.",
    "read_time": 4,
    "excerpt": "Spearwood is a southern suburb with a solid stock of family homes close to the coast. Bond cleaning here follows the REIWA standard — here's what Spearwood renters need to know.",
    "content": """
      <p>Spearwood is a well-established southern suburb near Fremantle and the coast. It's popular with families and has a large stock of 3 and 4-bedroom homes, many of which have been rental properties for years. The area's proximity to the ocean means properties can accumulate salt-related marks on external surfaces.</p>
      <h2>Coastal Proximity — What It Means for Your Bond Clean</h2>
      <p>Properties close to the southern coast can accumulate salt deposits on:</p>
      <ul class="checklist">
        <li>External windows and frames — salt film builds up and requires an acid-based glass cleaner</li>
        <li>Balcony or alfresco glass — may need more attention than properties further from the coast</li>
        <li>Metal fixtures outdoors — hinges, clothesline hardware, and window frames</li>
      </ul>
      <p>Internal cleaning is unaffected by coastal proximity — the standard REIWA requirements apply. But if your exit inspection includes external windows, mention the coastal location when getting a quote.</p>
      <h2>Typical Spearwood Property Types</h2>
      <p>Most Spearwood rentals are standalone brick homes with:</p>
      <ul class="checklist">
        <li>3–4 bedrooms with carpet throughout</li>
        <li>Single or double garage</li>
        <li>Established backyard and garden</li>
        <li>Alfresco or patio area</li>
      </ul>
      <h2>Typical Costs in Spearwood</h2>
      <ul class="checklist">
        <li>3-bedroom, 1-bathroom house: $400–$540</li>
        <li>3-bedroom, 2-bathroom house: $440–$600</li>
        <li>4-bedroom house: $540–$720</li>
        <li>Carpet steam cleaning: $130–$200</li>
        <li>Garage add-on: $70–$100</li>
      </ul>
      <p>We service all of Spearwood and the southern Fremantle corridor. Contact us for a quote today.</p>
"""
  },
  {
    "slug": "blog-bond-cleaning-thornlie",
    "title": "Bond Cleaning Thornlie Perth — What Renters Need to Know",
    "h1": "Bond Cleaning Thornlie Perth — Renter's Exit Clean Guide",
    "tag": "Suburbs",
    "meta": "Bond cleaning in Thornlie covers established family homes in Perth's southeastern suburbs. What property managers check and how to get your full bond back.",
    "read_time": 4,
    "excerpt": "Thornlie is a well-established southeastern suburb with a large stock of family homes. Bond cleaning here typically involves multiple rooms, carpet, and garages — here's what renters need to know.",
    "content": """
      <p>Thornlie is one of Perth's larger southeastern suburbs, with a well-established character and a high proportion of family homes. Most Thornlie rentals are 3 and 4-bedroom brick homes that have been in the rental market for many years — well-known to local property managers.</p>
      <h2>Common Thornlie Property Features</h2>
      <ul class="checklist">
        <li>Carpet throughout bedrooms and often the main living areas</li>
        <li>Single-car garage — sometimes a carport</li>
        <li>Established backyard with lawn and garden beds</li>
        <li>Older bathroom configurations — separate bath in many properties</li>
        <li>Older kitchen layouts with less bench space</li>
      </ul>
      <h2>What Property Managers Focus On in Thornlie</h2>
      <p>Local Thornlie property managers are experienced with the suburb's older housing stock. The most commonly flagged items at exit:</p>
      <ul class="checklist">
        <li>Carpet condition — must be steam cleaned if specified in lease</li>
        <li>Oven — older oven designs accumulate more grease in harder-to-reach areas</li>
        <li>Bathroom grout — older tiles can have deep-set staining</li>
        <li>Window tracks in aluminium frames</li>
        <li>Backyard tidiness — lawn mowing and garden maintenance</li>
      </ul>
      <h2>Typical Costs in Thornlie</h2>
      <ul class="checklist">
        <li>3-bedroom, 1-bathroom house: $390–$530</li>
        <li>3-bedroom, 2-bathroom house: $430–$580</li>
        <li>4-bedroom house: $520–$700</li>
        <li>Carpet steam cleaning (whole house): $130–$190</li>
      </ul>
      <p>We service Thornlie and surrounding southeastern suburbs including Gosnells, Kenwick, and Maddington. Get a quote today.</p>
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
    pub_date = "2025"
    pub_iso = "2025-01-01"
    header = HEADER.format(
        slug=slug, title=title, h1=h1, meta=meta,
        read_time=read_time, content=content,
        pub_date=pub_date
    )
    footer = FOOTER.format(
        slug=slug,
        title=title.replace('"', '\\"'),
        meta=meta.replace('"', '\\"'),
        pub_iso=pub_iso
    )
    return header + "\n" + footer

queue = []
for article in ARTICLES:
    filename = article["slug"] + ".html"
    html = build_page(article)
    filepath = os.path.join(DRAFTS_DIR, filename)
    with open(filepath, "w") as f:
        f.write(html)
    print(f"Created: {filepath}")
    queue.append({
        "slug": article["slug"],
        "title": article["title"],
        "tag": article["tag"],
        "read_time": article["read_time"],
        "excerpt": article["excerpt"]
    })

queue_path = os.path.join(DRAFTS_DIR, "queue.json")
with open(queue_path, "w") as f:
    json.dump({"queue": queue}, f, indent=2)
print(f"\nCreated: {queue_path}")
print(f"\nDone. {len(ARTICLES)} drafts created.")
