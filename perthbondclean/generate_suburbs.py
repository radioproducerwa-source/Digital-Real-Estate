#!/usr/bin/env python3
"""Generate suburb pages for Perth Bond Clean."""

import os

SUBURBS = [
    {
        "slug": "joondalup",
        "name": "Joondalup",
        "nearby": [("Morley", "morley.html"), ("Karrinyup", "karrinyup.html"), ("Scarborough", "scarborough.html")],
        "intro": "Joondalup is one of Perth's major northern hubs, home to Edith Cowan University, Lakeside Joondalup Shopping City, and one of the fastest-growing rental markets in WA. With thousands of apartments and homes turning over each year — from the CBD precinct around Joondalup Drive to the quieter streets near Lake Joondalup — demand for reliable bond cleaning in Joondalup has never been higher.",
        "area": "the Joondalup CBD, around Lake Joondalup, and throughout the City of Joondalup including Ocean Reef, Currambine, and Heathridge",
        "local_note": "Many Joondalup rentals are managed by agencies along Lakeside Drive, and property managers in the area are known to follow the REIWA exit checklist strictly.",
    },
    {
        "slug": "subiaco",
        "name": "Subiaco",
        "nearby": [("Claremont", "claremont.html"), ("Cottesloe", "cottesloe.html"), ("Mount Lawley", "mount-lawley.html")],
        "intro": "Subiaco is one of Perth's most sought-after inner suburbs, prized for its café culture along Rokeby Road, boutique shopping, and proximity to the CBD. With a mix of heritage homes, apartments, and townhouses commanding some of Perth's highest rents, property managers in Subiaco have high expectations for exit cleans — making a professional bond clean essential.",
        "area": "Subiaco, West Subiaco, and surrounding streets near the Rokeby Road strip, Subiaco Oval, and Kings Park",
        "local_note": "Subiaco property managers frequently require REIWA-compliant bond cleans, and properties near Roberts Road and Bagot Road are among the most frequently turned over in the inner west.",
    },
    {
        "slug": "fremantle",
        "name": "Fremantle",
        "nearby": [("Cottesloe", "cottesloe.html"), ("Canning Vale", "canning-vale.html"), ("Rockingham", "rockingham.html")],
        "intro": "Fremantle's vibrant port city character attracts a constant stream of renters drawn to its arts scene, café strip, and historic streetscapes. From apartments near the Fremantle Markets to homes in the South Fremantle and Beaconsfield areas, the rental market is active year-round — and property managers along High Street and South Terrace demand thorough bond cleans.",
        "area": "Fremantle, South Fremantle, Beaconsfield, and surrounding areas near the Fremantle CBD and Victoria Quay",
        "local_note": "Many Fremantle heritage homes have period features like original timber floors and ornate cornices that require extra care during a bond clean — our cleaners are experienced with these properties.",
    },
    {
        "slug": "rockingham",
        "name": "Rockingham",
        "nearby": [("Baldivis", "baldivis.html"), ("Mandurah", "mandurah.html"), ("Fremantle", "fremantle.html")],
        "intro": "Rockingham's coastal lifestyle and affordable housing have made it one of Perth's most popular rental destinations, particularly for families and Defence Housing residents from HMAS Stirling on Garden Island. With a large volume of rental properties turning over regularly across Rockingham, Port Kennedy, and Safety Bay, professional bond cleaning is in high demand.",
        "area": "Rockingham, Safety Bay, Shoalwater, Port Kennedy, and the broader City of Rockingham coastal strip",
        "local_note": "Defence Housing properties in Rockingham have strict exit condition requirements. Our cleaners are experienced with DHA inspections and know exactly what's required to pass first time.",
    },
    {
        "slug": "baldivis",
        "name": "Baldivis",
        "nearby": [("Rockingham", "rockingham.html"), ("Canning Vale", "canning-vale.html"), ("Mandurah", "mandurah.html")],
        "intro": "Baldivis has seen explosive growth over the past decade, becoming one of Perth's fastest-expanding outer suburbs with estates like Settlers Hills, Rivergums, and Baldivis Parks. The suburb's relatively young housing stock means many tenants are vacating modern 4x2 homes with high-finish kitchens and bathrooms that require thorough professional cleaning.",
        "area": "Baldivis, including the Settlers Hills, Rivergums, Baldivis Parks, and Secret Harbour estates",
        "local_note": "Modern Baldivis homes often feature stone benchtops, glass splashbacks, and tiled wet areas that benefit from professional-grade cleaning products and equipment.",
    },
    {
        "slug": "canning-vale",
        "name": "Canning Vale",
        "nearby": [("Armadale", "armadale.html"), ("Cannington", "cannington.html"), ("Baldivis", "baldivis.html")],
        "intro": "Canning Vale is one of Perth's largest southern suburbs, known for its mix of established family homes and newer estates. Located within the City of Canning, it's a high-turnover rental area popular with families, and its proximity to major shopping centres and highways makes it an attractive choice for tenants — and a busy market for bond cleaning services.",
        "area": "Canning Vale, Willetton, Riverton, and surrounding southern suburbs within the City of Canning",
        "local_note": "Canning Vale properties managed through southern Perth real estate agencies typically require comprehensive bond cleans including oven, carpet, and all wet areas.",
    },
    {
        "slug": "midland",
        "name": "Midland",
        "nearby": [("Morley", "morley.html"), ("Ellenbrook", "ellenbrook.html"), ("Bayswater", "bayswater.html")],
        "intro": "Midland is the eastern gateway to Perth's Swan Valley and a key commercial hub for the eastern corridor. With major infrastructure investment around the Midland Health Campus and the redevelopment of the Midland Gate shopping precinct, rental demand in the area is strong. Tenants vacating homes around Midland, Bellevue, and Swan View rely on professional bond cleaners to meet exit standards.",
        "area": "Midland, Bellevue, Swan View, Middle Swan, and the broader eastern suburbs corridor",
        "local_note": "Properties in Midland's older housing stock often require extra attention to grout, window tracks, and oven deep-cleans — areas our cleaners prioritise.",
    },
    {
        "slug": "morley",
        "name": "Morley",
        "nearby": [("Bayswater", "bayswater.html"), ("Stirling", "stirling.html"), ("Midland", "midland.html")],
        "intro": "Morley is a well-established northern suburb offering affordable housing within easy reach of the Perth CBD via the Tonkin Highway and Morley Drive. With a busy rental market driven by its proximity to Galleria Shopping Centre and strong demand from families and young professionals, Morley sees consistent demand for reliable end-of-lease cleaning services.",
        "area": "Morley, Noranda, Bedford, and surrounding suburbs in the City of Bayswater",
        "local_note": "Morley's mix of 1960s–80s brick homes and newer townhouse developments means varied property types — our cleaners are experienced with all styles.",
    },
    {
        "slug": "ellenbrook",
        "name": "Ellenbrook",
        "nearby": [("Midland", "midland.html"), ("Morley", "morley.html"), ("Bayswater", "bayswater.html")],
        "intro": "Ellenbrook is one of Perth's newest master-planned communities, featuring modern housing estates, parks, and the Ellenbrook town centre. Located in the City of Swan, the suburb has a high proportion of owner-occupiers transitioning to new builds alongside a growing rental market. Its modern homes with contemporary finishes demand thorough professional bond cleaning.",
        "area": "Ellenbrook, The Vines, Aveley, and surrounding estates in the City of Swan",
        "local_note": "Ellenbrook's newer homes often feature stacker doors, large alfresco areas, and stone benchtops — all of which require specialist cleaning techniques our team is trained in.",
    },
    {
        "slug": "mandurah",
        "name": "Mandurah",
        "nearby": [("Rockingham", "rockingham.html"), ("Baldivis", "baldivis.html"), ("Armadale", "armadale.html")],
        "intro": "Mandurah, sitting on the Peel Inlet about 70km south of Perth, is a popular coastal city with a thriving rental market driven by its canal developments, waterfront apartments, and sea-change lifestyle appeal. With significant rental activity across Mandurah, Halls Head, and Falcon, professional bond cleaning services are in strong demand from tenants vacating both holiday-style rentals and long-term homes.",
        "area": "Mandurah, Halls Head, Falcon, Dudley Park, and surrounding Peel region suburbs",
        "local_note": "Mandurah canal homes and waterfront properties often feature tiled floors throughout, glass balustrades, and large entertaining areas that our cleaning teams handle routinely.",
    },
    {
        "slug": "armadale",
        "name": "Armadale",
        "nearby": [("Canning Vale", "canning-vale.html"), ("Cannington", "cannington.html"), ("Baldivis", "baldivis.html")],
        "intro": "Armadale is a rapidly growing outer suburb in Perth's south-eastern corridor, experiencing significant urban expansion with new estates in Haynes, Harrisdale, and Piara Waters. Its affordable rental prices attract a large volume of tenants, and the high turnover of rental properties across the City of Armadale drives consistent demand for professional end-of-lease cleaning.",
        "area": "Armadale, Haynes, Harrisdale, Piara Waters, and surrounding suburbs in the City of Armadale",
        "local_note": "New estates in Armadale's southern fringe feature modern specifications with tile-and-carpet mixes, and property managers in new developments often use detailed entry condition reports that tenants must match at exit.",
    },
    {
        "slug": "cannington",
        "name": "Cannington",
        "nearby": [("Canning Vale", "canning-vale.html"), ("Armadale", "armadale.html"), ("Victoria Park", "victoria-park.html")],
        "intro": "Cannington is a busy south-eastern suburb anchored by Westfield Carousel, one of Perth's largest shopping centres. Its central location, access to Roe Highway, and mix of housing styles make it a popular rental destination. With strong turnover across units, townhouses, and houses near the Cannington showgrounds and Sevenoaks Street, bond cleaning demand is consistently high.",
        "area": "Cannington, East Cannington, Beckenham, Queens Park, and surrounding southern suburbs",
        "local_note": "Cannington's high-density areas feature many apartment complexes and townhouse groups managed by large real estate agencies that use standardised exit inspection processes.",
    },
    {
        "slug": "victoria-park",
        "name": "Victoria Park",
        "nearby": [("Mount Lawley", "mount-lawley.html"), ("Bayswater", "bayswater.html"), ("Cannington", "cannington.html")],
        "intro": "Victoria Park — or 'Vic Park' as locals call it — is one of Perth's most vibrant inner suburbs, known for its diverse dining scene along Albany Highway and its proximity to the CBD. It's a popular choice for young professionals and couples, with a dense mix of apartments, villas, and character homes. Property managers in this area hold high standards for exit cleans.",
        "area": "Victoria Park, East Victoria Park, St James, and surrounding inner southern suburbs",
        "local_note": "Vic Park's heritage homes and newer apartment blocks require different cleaning approaches — our team is experienced with both tile and timber floors, as well as the tight spaces common in older Perth rental units.",
    },
    {
        "slug": "mount-lawley",
        "name": "Mount Lawley",
        "nearby": [("Bayswater", "bayswater.html"), ("Victoria Park", "victoria-park.html"), ("Morley", "morley.html")],
        "intro": "Mount Lawley is one of Perth's most desirable inner-north suburbs, renowned for its café culture along Beaufort Street, stunning Art Deco and Federation architecture, and proximity to the CBD. Its competitive rental market and above-average rental prices attract discerning tenants and equally discerning property managers who expect immaculate exit cleans.",
        "area": "Mount Lawley, Inglewood, and surrounding inner north suburbs along and around Beaufort Street",
        "local_note": "Mount Lawley's heritage homes with jarrah floors, ornate cornices, and leadlight windows require careful, experienced cleaning — our team handles period properties with the attention they deserve.",
    },
    {
        "slug": "scarborough",
        "name": "Scarborough",
        "nearby": [("Karrinyup", "karrinyup.html"), ("Stirling", "stirling.html"), ("Joondalup", "joondalup.html")],
        "intro": "Scarborough's beach lifestyle and recent foreshore redevelopment have made it one of Perth's most desirable coastal rental markets. New high-rise apartments and revitalised retail along The Esplanade attract a young, transient rental population, resulting in high turnover and strong demand for professional bond cleaning services — particularly for modern apartment exits.",
        "area": "Scarborough, Doubleview, Churchlands, and surrounding northern coastal suburbs",
        "local_note": "Scarborough's newer beachfront apartment developments have glass balustrades, sea-facing windows, and salt-air exposure that require specialist descaling and polishing — services our cleaners include as standard.",
    },
    {
        "slug": "cottesloe",
        "name": "Cottesloe",
        "nearby": [("Claremont", "claremont.html"), ("Fremantle", "fremantle.html"), ("Subiaco", "subiaco.html")],
        "intro": "Cottesloe is Perth's premium beachside suburb, known for the iconic Hotel Cottesloe, its family-friendly beach, and some of the city's most expensive real estate. While owner-occupiers dominate, a healthy rental market exists in the suburb's apartments and character homes along Marine Parade and Eric Street — and property managers here expect nothing short of perfection.",
        "area": "Cottesloe, Swanbourne, and surrounding western suburbs near the Indian Ocean foreshore",
        "local_note": "Cottesloe's premium rental properties often command detailed exit inspection reports, and tenants expect their full bond back. Our cleaners treat every Cottesloe property with the high-end attention it deserves.",
    },
    {
        "slug": "claremont",
        "name": "Claremont",
        "nearby": [("Cottesloe", "cottesloe.html"), ("Subiaco", "subiaco.html"), ("Fremantle", "fremantle.html")],
        "intro": "Claremont is an affluent riverside suburb on the Claremont Crescent strip, home to upscale boutiques, quality dining, and prestigious schools. Its mix of period homes, riverside apartments, and modern developments make it a sought-after rental market, particularly among professionals and families. Property managers in Claremont maintain strict exit clean standards.",
        "area": "Claremont, Peppermint Grove, and surrounding western riverside suburbs",
        "local_note": "Claremont's high-value properties — particularly those along the Swan River — often have premium fixtures, stone benchtops, and high-gloss cabinetry that benefit from our professional-grade cleaning products.",
    },
    {
        "slug": "karrinyup",
        "name": "Karrinyup",
        "nearby": [("Scarborough", "scarborough.html"), ("Stirling", "stirling.html"), ("Joondalup", "joondalup.html")],
        "intro": "Karrinyup is a well-established northern suburb anchored by the recently expanded Karrinyup Shopping Centre. With excellent schools, easy freeway access, and a mix of family homes and modern apartments, it's a popular rental destination. The suburb's active property market means consistent demand for professional end-of-lease cleaning services.",
        "area": "Karrinyup, Carine, Gwelup, and surrounding northern suburbs near Karrinyup Road",
        "local_note": "Karrinyup's post-renovation apartment towers near the shopping centre feature modern finishes requiring professional-grade cleaning equipment to achieve the streak-free, spotless results property managers expect.",
    },
    {
        "slug": "stirling",
        "name": "Stirling",
        "nearby": [("Karrinyup", "karrinyup.html"), ("Morley", "morley.html"), ("Scarborough", "scarborough.html")],
        "intro": "Stirling sits within the City of Stirling — Perth's most populous local government area — and encompasses suburbs like Balga, Dianella, and Nollamara. Its affordability and excellent public transport links make it a high-volume rental market, particularly for families and first-time renters, resulting in consistent demand for professional bond cleaning throughout the area.",
        "area": "Stirling, Balga, Nollamara, Dianella, and surrounding suburbs within the City of Stirling",
        "local_note": "The City of Stirling's high rental turnover means many tenants are working with tight timelines between exit and move-in dates — our same-day and next-day availability is especially valued here.",
    },
    {
        "slug": "bayswater",
        "name": "Bayswater",
        "nearby": [("Mount Lawley", "mount-lawley.html"), ("Morley", "morley.html"), ("Victoria Park", "victoria-park.html")],
        "intro": "Bayswater is a charming inner-north suburb straddling the Swan River, known for its weekend markets, café culture along King William Street, and excellent train connections to the CBD. Its mix of character bungalows, modern townhouses, and riverside apartments attracts a broad rental demographic, with high property manager standards for exit condition reports.",
        "area": "Bayswater, Maylands, Bassendean, and surrounding inner northern suburbs along the Swan River corridor",
        "local_note": "Bayswater's period bungalows with polished jarrah floors and original tiling require experienced bond cleaners who understand how to restore these features without damage — exactly what our team specialises in.",
    },
]

NAV_SUBURBS = """
          <a href="joondalup.html">Joondalup</a>
          <a href="subiaco.html">Subiaco</a>
          <a href="fremantle.html">Fremantle</a>
          <a href="rockingham.html">Rockingham</a>
          <a href="baldivis.html">Baldivis</a>
          <a href="canning-vale.html">Canning Vale</a>
          <a href="midland.html">Midland</a>
          <a href="morley.html">Morley</a>
          <a href="ellenbrook.html">Ellenbrook</a>
          <a href="mandurah.html">Mandurah</a>
          <a href="armadale.html">Armadale</a>
          <a href="cannington.html">Cannington</a>
          <a href="victoria-park.html">Victoria Park</a>
          <a href="mount-lawley.html">Mount Lawley</a>
          <a href="scarborough.html">Scarborough</a>
          <a href="cottesloe.html">Cottesloe</a>
          <a href="claremont.html">Claremont</a>
          <a href="karrinyup.html">Karrinyup</a>
          <a href="stirling.html">Stirling</a>
          <a href="bayswater.html">Bayswater</a>"""

FOOTER_SUBURBS = "\n".join(
    f'          <li><a href="{s["slug"]}.html">{s["name"]}</a></li>'
    for s in SUBURBS
)

HEADER = """\
<!-- ── HEADER ── -->
<header class="site-header">
  <div class="container header-inner">
    <a href="index.html" class="logo">Perth<span>Bond</span>Clean</a>
    <nav class="main-nav" id="main-nav">
      <a href="index.html">Home</a>
      <a href="services.html">Services</a>
      <div class="dropdown">
        <button class="dropdown-btn">Suburbs &#9660;</button>
        <div class="dropdown-menu">%(nav)s
        </div>
      </div>
      <a href="about.html">About</a>
      <a href="contact.html" class="btn btn-primary">Get a Quote</a>
    </nav>
    <div class="header-right">
      <a href="tel:[TRACKED_NUMBER]" class="header-phone">[TRACKED_NUMBER]</a>
      <button class="hamburger" id="hamburger" aria-label="Open menu" aria-expanded="false">&#9776;</button>
    </div>
  </div>
</header>""" % {"nav": NAV_SUBURBS}

FOOTER = """\
<!-- ── FOOTER ── -->
<footer class="site-footer">
  <div class="container">
    <div class="footer-top">
      <div class="footer-brand">
        <a href="index.html" class="logo">Perth<span>Bond</span>Clean</a>
        <p>Perth's #1 Bond Cleaning Lead Service.<br>Helping Perth renters get their full bond back since 2020.</p>
        <p>&#128222; <a href="tel:[TRACKED_NUMBER]">[TRACKED_NUMBER]</a></p>
        <p>&#9993;&#65039; <a href="mailto:info@perthbondclean.com">info@perthbondclean.com</a></p>
      </div>
      <div class="footer-links">
        <h4>Quick Links</h4>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="services.html">Services</a></li>
          <li><a href="about.html">About</a></li>
          <li><a href="contact.html">Contact</a></li>
        </ul>
      </div>
      <div class="footer-suburbs">
        <h4>Suburbs We Serve</h4>
        <ul>
%(suburbs)s
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; <span id="year"></span> Perth Bond Clean. All rights reserved. | Website by Perth Bond Clean</p>
    </div>
  </div>
</footer>""" % {"suburbs": FOOTER_SUBURBS}


def build_page(s):
    slug = s["slug"]
    name = s["name"]
    nearby = s["nearby"]
    intro = s["intro"]
    area = s["area"]
    local_note = s["local_note"]

    nearby_pills = "\n".join(
        f'          <a href="{href}">{n}</a>' for n, href in nearby
    )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="Professional bond cleaning in {name}, Perth WA. 100% Bond Back Guarantee, same-day quotes, REIWA-approved checklist. Call [TRACKED_NUMBER] for a free quote." />
  <meta name="robots" content="index, follow" />
  <title>Bond Cleaning {name} | End of Lease Cleaning {name} Perth | Perth Bond Clean</title>
  <link rel="canonical" href="https://perthbondclean.com/{slug}.html" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="css/style.css" />
</head>
<body>

{HEADER}

<!-- ── HERO ── -->
<section class="suburb-hero">
  <div class="container">
    <h1>Bond Cleaning {name} | End of Lease Cleaning {name}</h1>
    <p>Perth Bond Clean connects {name} renters with vetted, insured end-of-lease cleaners. We follow the REIWA exit checklist and guarantee your bond back.</p>
    <div class="hero-cta">
      <a href="#quote" class="btn btn-primary btn-lg">Get a Free Quote</a>
      <a href="tel:[TRACKED_NUMBER]" class="btn btn-outline-white btn-lg">&#128222; Call [TRACKED_NUMBER]</a>
    </div>
  </div>
</section>

<!-- ── STATS BAR ── -->
<div class="stats-bar">
  <div class="container stats-inner">
    <div class="stat"><div class="stat-num">&#10003;</div><div class="stat-label">100% Bond Back Guarantee</div></div>
    <div class="stat"><div class="stat-num">30 min</div><div class="stat-label">Quote Response Time</div></div>
    <div class="stat"><div class="stat-num">4.9&#9733;</div><div class="stat-label">Average Rating</div></div>
    <div class="stat"><div class="stat-num">7 days</div><div class="stat-label">Mon–Sun Availability</div></div>
  </div>
</div>

<!-- ── MAIN CONTENT ── -->
<section class="section-pad">
  <div class="container suburb-content">
    <div>
      <h2>End-of-Lease Cleaning in {name}, Perth WA</h2>
      <p style="color:var(--muted);margin:16px 0;font-size:0.97rem;line-height:1.8;">{intro}</p>

      <h3 style="margin-top:28px;margin-bottom:12px;">What's Included in a {name} Bond Clean</h3>
      <p style="color:var(--muted);margin-bottom:16px;font-size:0.95rem;">Every bond clean we arrange in {name} covers the complete REIWA exit checklist:</p>
      <ul class="checklist">
        <li>Oven, rangehood &amp; kitchen deep clean</li>
        <li>Bathroom descaling, grout scrub &amp; mould treatment</li>
        <li>All windows cleaned inside (tracks &amp; sills)</li>
        <li>Wardrobes, cupboards &amp; drawers inside &amp; out</li>
        <li>Walls spot-cleaned, skirting boards &amp; light fittings</li>
        <li>All floors vacuumed &amp; mopped</li>
        <li>Balcony / alfresco swept, garage swept</li>
        <li>Cobwebs removed throughout</li>
      </ul>

      <h3 style="margin-top:28px;margin-bottom:12px;">Why {name} Renters Trust Perth Bond Clean</h3>
      <p style="color:var(--muted);margin-bottom:12px;font-size:0.95rem;">{local_note}</p>
      <ul class="checklist">
        <li>Bond Back Guarantee — free return visit within 72 hours if needed</li>
        <li>Police-checked, fully insured cleaners</li>
        <li>Flat-rate pricing — no surprise charges</li>
        <li>Same-day and next-day bookings available</li>
        <li>Carpet steam cleaning available as add-on</li>
      </ul>

      <h3 style="margin-top:28px;margin-bottom:12px;">Areas We Cover Near {name}</h3>
      <p style="color:var(--muted);margin-bottom:16px;font-size:0.95rem;">We service {area}. We also cover the following nearby suburbs:</p>
      <div class="nearby-suburbs">
        <div class="nearby-list">
{nearby_pills}
          <a href="index.html">View all suburbs</a>
        </div>
      </div>
    </div>

    <!-- QUOTE FORM -->
    <div id="quote">
      <div class="form-card-light">
        <h3>Get a Free Quote in {name}</h3>
        <p class="card-sub">We respond within 1 hour during business hours (7am–7pm, 7 days).</p>
        <form action="https://formspree.io/f/REPLACE_WITH_YOUR_ID" method="POST" data-formspree data-success-id="{slug}-success">
          <div class="form-two-col">
            <div class="form-group">
              <label for="{slug}-name">Full Name *</label>
              <input type="text" id="{slug}-name" name="name" placeholder="Jane Smith" required />
            </div>
            <div class="form-group">
              <label for="{slug}-phone">Phone Number *</label>
              <input type="tel" id="{slug}-phone" name="phone" placeholder="04XX XXX XXX" required />
            </div>
          </div>
          <div class="form-two-col">
            <div class="form-group">
              <label for="{slug}-email">Email Address *</label>
              <input type="email" id="{slug}-email" name="email" placeholder="jane@example.com" required />
            </div>
            <div class="form-group">
              <label for="{slug}-suburb">Suburb *</label>
              <input type="text" id="{slug}-suburb" name="suburb" placeholder="{name}" value="{name}" required />
            </div>
          </div>
          <div class="form-two-col">
            <div class="form-group">
              <label for="{slug}-beds">Bedrooms *</label>
              <select id="{slug}-beds" name="bedrooms" required>
                <option value="">Select…</option>
                <option>1 Bedroom</option>
                <option>2 Bedrooms</option>
                <option>3 Bedrooms</option>
                <option>4 Bedrooms</option>
                <option>5+ Bedrooms</option>
              </select>
            </div>
            <div class="form-group">
              <label for="{slug}-baths">Bathrooms *</label>
              <select id="{slug}-baths" name="bathrooms" required>
                <option value="">Select…</option>
                <option>1 Bathroom</option>
                <option>2 Bathrooms</option>
                <option>3 Bathrooms</option>
                <option>4+ Bathrooms</option>
              </select>
            </div>
          </div>
          <div class="form-group">
            <label for="{slug}-date">Move-out Date *</label>
            <input type="date" id="{slug}-date" name="moveout_date" required />
          </div>
          <div class="form-group">
            <label for="{slug}-notes">Additional Notes</label>
            <textarea id="{slug}-notes" name="message" rows="3" placeholder="Carpet steam cleaning? Garage? Anything else to note…"></textarea>
          </div>
          <button type="submit" class="btn btn-primary btn-full btn-lg">Get My Free Quote &rarr;</button>
        </form>
        <div id="{slug}-success" class="form-success-light" hidden>
          <h3>&#10003; Thanks! We'll be in touch within 1 hour.</h3>
          <p>We've received your {name} enquiry and will match you with a trusted local bond cleaner shortly.</p>
        </div>
      </div>

      <div style="background:var(--green-lt);border:1.5px solid var(--border);border-radius:var(--radius);padding:20px;margin-top:20px;">
        <p style="font-weight:600;margin-bottom:4px;">Prefer to call?</p>
        <a href="tel:[TRACKED_NUMBER]" style="font-size:1.3rem;font-weight:800;color:var(--green);">[TRACKED_NUMBER]</a>
        <p style="font-size:0.85rem;color:var(--muted);margin-top:4px;">Mon–Sun, 7am–7pm</p>
      </div>
    </div>
  </div>
</section>

<!-- ── CTA ── -->
<section class="cta-band">
  <div class="container">
    <h2>Ready to Book Your {name} Bond Clean?</h2>
    <p>Free quotes within 30 minutes. 100% Bond Back Guarantee. 7 days a week.</p>
    <div style="display:flex;gap:14px;justify-content:center;flex-wrap:wrap;">
      <a href="#quote" class="btn btn-outline-white btn-lg">Get a Free Quote</a>
      <a href="tel:[TRACKED_NUMBER]" class="btn btn-outline-white btn-lg">&#128222; Call [TRACKED_NUMBER]</a>
    </div>
  </div>
</section>

{FOOTER}

<script src="js/main.js"></script>
</body>
</html>
"""


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    for s in SUBURBS:
        filename = os.path.join(script_dir, f"{s['slug']}.html")
        content = build_page(s)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  ✓ {s['slug']}.html")
    print(f"\nGenerated {len(SUBURBS)} suburb pages.")


if __name__ == "__main__":
    main()
