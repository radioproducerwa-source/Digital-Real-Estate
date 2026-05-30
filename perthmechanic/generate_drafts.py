#!/usr/bin/env python3
"""Generate 28 draft blog posts for Perth Mechanic weekly publishing queue."""

import os
import json

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DRAFTS_DIR = os.path.join(SCRIPT_DIR, "drafts")
os.makedirs(DRAFTS_DIR, exist_ok=True)

NAV = """      <a href="index.html">Home</a>
      <a href="services.html">Services</a>
      <div class="dropdown">
        <button class="dropdown-btn">Suburbs &#9660;</button>
        <div class="dropdown-menu">
          <a href="fremantle.html">Fremantle</a><a href="joondalup.html">Joondalup</a><a href="midland.html">Midland</a><a href="armadale.html">Armadale</a><a href="rockingham.html">Rockingham</a><a href="mandurah.html">Mandurah</a><a href="osborne-park.html">Osborne Park</a><a href="canning-vale.html">Canning Vale</a><a href="cannington.html">Cannington</a><a href="morley.html">Morley</a>
        </div>
      </div>
      <a href="about.html">About</a>
      <a href="blog.html" class="active">Blog</a>
      <a href="contact.html" class="btn btn-primary">Get a Quote</a>"""

HEADER_TPL = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="{meta}" />
  <meta name="robots" content="index, follow" />
  <title>{title} | Perth Mechanic</title>
  <link rel="canonical" href="https://perthmechanic.com/{slug}.html" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="css/style.css" />
</head>
<body>
<header class="site-header">
  <div class="container header-inner">
    <a href="index.html" class="logo">Perth<span>Mechanic</span></a>
    <nav class="main-nav" id="main-nav">
{nav}
    </nav>
    <div class="header-right">
      <button class="hamburger" id="hamburger" aria-label="Open menu" aria-expanded="false">&#9776;</button>
    </div>
  </div>
</header>
<section class="page-hero">
  <div class="container" style="max-width:800px;">
    <div style="margin-bottom:12px;"><a href="blog.html" style="color:var(--accent);font-size:0.9rem;text-decoration:none;">&larr; Back to Blog</a></div>
    <h1>{h1}</h1>
    <p style="color:rgba(255,255,255,.7);font-size:0.95rem;margin-top:12px;">Published {pub_date} &nbsp;|&nbsp; {read_time} min read</p>
  </div>
</section>
<section class="section-pad">
  <div class="container" style="max-width:800px;">
    <article class="blog-article">
{content}
      <div style="text-align:center;margin:40px 0 16px;">
        <a href="contact.html" class="btn btn-primary btn-lg">Get a Free Mechanic Quote &rarr;</a>
      </div>
      <p style="text-align:center;color:var(--muted);font-size:0.9rem;">We respond within 30 minutes. All Perth suburbs covered.</p>
    </article>
  </div>
</section>"""

FOOTER_TPL = """<footer class="site-footer">
  <div class="container">
    <div class="footer-top">
      <div class="footer-brand">
        <a href="index.html" class="logo">Perth<span>Mechanic</span></a>
        <p>Perth\'s trusted mechanic connection service.<br>Matching Perth drivers with qualified, affordable mechanics since 2024.</p>
        <p>&#x2709;&#xFE0F; <a href="mailto:info@perthmechanic.com">info@perthmechanic.com</a></p>
      </div>
      <div class="footer-links">
        <h4>Quick Links</h4>
        <ul><li><a href="index.html">Home</a></li><li><a href="services.html">Services</a></li><li><a href="about.html">About</a></li><li><a href="blog.html">Blog</a></li><li><a href="contact.html">Contact</a></li></ul>
      </div>
      <div class="footer-suburbs">
        <h4>Suburbs We Serve</h4>
        <ul><li><a href="fremantle.html">Fremantle</a></li><li><a href="joondalup.html">Joondalup</a></li><li><a href="midland.html">Midland</a></li><li><a href="rockingham.html">Rockingham</a></li><li><a href="mandurah.html">Mandurah</a></li><li><a href="osborne-park.html">Osborne Park</a></li><li><a href="armadale.html">Armadale</a></li><li><a href="cannington.html">Cannington</a></li><li><a href="thornlie.html">Thornlie</a></li><li><a href="cockburn-central.html">Cockburn Central</a></li></ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; <span id="year"></span> Perth Mechanic. All rights reserved.</p>
    </div>
  </div>
</footer>
<script src="js/main.js"></script>
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Article","headline":"{title}","description":"{meta}","url":"https://perthmechanic.com/{slug}.html","datePublished":"{pub_iso}","dateModified":"{pub_iso}","author":{{"@type":"Organization","name":"Perth Mechanic","url":"https://perthmechanic.com"}},"publisher":{{"@type":"Organization","name":"Perth Mechanic","url":"https://perthmechanic.com"}},"mainEntityOfPage":{{"@type":"WebPage","@id":"https://perthmechanic.com/{slug}.html"}}}}
</script>
</body>
</html>"""

ARTICLES = [
  {
    "slug": "blog-car-service-cost-perth",
    "title": "How Much Does a Car Service Cost in Perth? [2026 Guide]",
    "h1": "How Much Does a Car Service Cost in Perth? [2026 Guide]",
    "tag": "Cost / Info",
    "meta": "Car service cost Perth 2026: minor service $150-$280, major service $300-$600+. Full breakdown of Perth mechanic pricing for all service types.",
    "read_time": 6,
    "excerpt": "Perth car service costs vary widely by vehicle and service type. A minor service runs $150-$280, a major service $300-$600+. Here's the complete 2026 breakdown.",
    "content": """
      <p>Car servicing costs in Perth depend on your vehicle make, model, age, and the type of service required. Here's what Perth drivers should expect to pay in 2026 for each service type.</p>
      <h2>Minor Service Cost in Perth</h2>
      <p>A minor service covers the essential maintenance items: engine oil and filter change, all fluid top-ups, and a visual safety inspection. Typical Perth pricing:</p>
      <ul>
        <li>Small hatchback / sedan (e.g. Toyota Yaris, Mazda 2): $150–$200</li>
        <li>Medium car (e.g. Toyota Corolla, Hyundai i30): $180–$240</li>
        <li>Large car / SUV (e.g. Toyota Camry, Mazda CX-5): $200–$280</li>
        <li>European vehicles: add 20–40% to above figures</li>
      </ul>
      <h2>Major Service Cost in Perth</h2>
      <p>A major service includes all minor service items plus air and cabin filter replacement, spark plug replacement (petrol), brake fluid flush, and a comprehensive safety inspection. Typical Perth pricing:</p>
      <ul>
        <li>Small hatchback / sedan: $280–$380</li>
        <li>Medium car: $320–$480</li>
        <li>Large car / SUV: $380–$600</li>
        <li>European vehicles: $450–$900+</li>
      </ul>
      <h2>Logbook Service Cost in Perth</h2>
      <p>Logbook service costs depend on your manufacturer's service schedule. Vehicles with shorter service intervals or those requiring synthetic oil are at the higher end:</p>
      <ul>
        <li>Budget brands (Kia, Hyundai, MG): $180–$280</li>
        <li>Japanese brands (Toyota, Mazda, Honda): $200–$350</li>
        <li>European brands (VW, BMW, Mercedes): $350–$800+</li>
      </ul>
      <h2>What Affects the Price?</h2>
      <ul>
        <li>Oil type — synthetic oil costs more than conventional but lasts longer</li>
        <li>Vehicle age and complexity — newer vehicles have more complex service requirements</li>
        <li>Workshop location — inner-city workshops typically charge higher labour rates</li>
        <li>Dealership vs independent — dealerships charge 30–60% more for equivalent work</li>
      </ul>
      <h2>How to Get a Fair Price in Perth</h2>
      <p>The best approach is to get two or three quotes from qualified independent mechanics before committing. Perth Mechanic provides a fixed upfront quote — you know the price before any work begins and there are no surprises on the invoice.</p>
"""
  },
  {
    "slug": "blog-logbook-service-vs-general-service",
    "title": "Logbook Service vs General Service: What's the Difference?",
    "h1": "Logbook Service vs General Service: What's the Difference?",
    "tag": "Info",
    "meta": "What's the difference between a logbook service and a general service in Perth? This guide explains both options, when you need each one, and how to keep your warranty valid.",
    "read_time": 5,
    "excerpt": "Confused about logbook vs general service? A logbook service follows your manufacturer's schedule and keeps your warranty valid. A general service is more flexible. Here's when to choose each.",
    "content": """
      <p>Many Perth drivers aren't sure whether they need a logbook service or a general service for their vehicle. The difference matters — particularly if your car is still under the manufacturer's warranty.</p>
      <h2>What Is a Logbook Service?</h2>
      <p>A logbook service follows the exact schedule set out in your vehicle's manufacturer service logbook. This includes specific parts, fluids, and inspection points required by the manufacturer at defined intervals (e.g. every 10,000km or 12 months). The mechanic stamps and records the service in the logbook, creating a complete documented history.</p>
      <p>Logbook services are essential for:</p>
      <ul>
        <li>Vehicles still under manufacturer warranty</li>
        <li>Vehicles purchased new or near-new</li>
        <li>Maintaining maximum resale value</li>
        <li>Ensuring manufacturer defect coverage is preserved</li>
      </ul>
      <h2>What Is a General Service?</h2>
      <p>A general service (or standard service) covers the core maintenance items — typically oil and filter change, fluid checks and top-ups, and a safety inspection — without following a specific manufacturer schedule. It's appropriate for:</p>
      <ul>
        <li>Older vehicles out of the warranty period</li>
        <li>Vehicles where maintaining specific warranty coverage isn't the priority</li>
        <li>Situations where you want a cost-effective maintenance check</li>
      </ul>
      <h2>Does a Logbook Service Have to Be Done at a Dealership?</h2>
      <p>No — and this is one of the most common misconceptions among Perth drivers. Under Australian consumer law (Competition and Consumer Act 2010), you can have your logbook service performed by any qualified mechanic. The dealership cannot void your warranty simply because you chose an independent mechanic, as long as the service was performed correctly using appropriate parts and fluids, and the logbook was stamped.</p>
      <h2>Which One Should You Choose?</h2>
      <p>If your vehicle is within the warranty period (typically 5–7 years for most brands), a logbook service is always the right choice. Once out of warranty, a general service is perfectly adequate for most vehicles, though a logbook service still adds to resale documentation.</p>
"""
  },
  {
    "slug": "blog-how-often-service-car-perth",
    "title": "How Often Should You Service Your Car in Perth?",
    "h1": "How Often Should You Service Your Car in Perth?",
    "tag": "Info",
    "meta": "How often should you service your car in Perth? Most vehicles need servicing every 10,000-15,000km or 12 months. Perth's hot climate may affect the recommended interval for some vehicles.",
    "read_time": 5,
    "excerpt": "Most Perth cars need servicing every 10,000-15,000km or 12 months. But Perth's extreme summer heat can affect oil degradation rates. Here's the guide for Perth drivers.",
    "content": """
      <p>The most common service interval question Perth mechanics hear is: "How often do I actually need to bring my car in?" The answer depends on your vehicle — but here's the practical guide.</p>
      <h2>Standard Service Intervals</h2>
      <p>Most modern vehicles specify one of these service intervals:</p>
      <ul>
        <li>Every 10,000km or 12 months — common for Japanese and Korean brands</li>
        <li>Every 15,000km or 12 months — common for newer vehicles with synthetic oil</li>
        <li>Every 20,000–25,000km or 24 months — some premium European vehicles with long-life servicing</li>
        <li>Always follow the "whichever comes first" rule for time vs distance</li>
      </ul>
      <h2>How Perth's Heat Affects Service Intervals</h2>
      <p>Perth's extreme summer temperatures — regularly exceeding 40°C — put additional stress on engine oil and cooling systems. Conventional oil degrades faster in high-heat conditions. If you're using conventional (non-synthetic) oil and your car operates in Perth summer conditions regularly (particularly stop-start city driving in summer), consider servicing at the shorter end of your interval range.</p>
      <p>Synthetic oil is significantly more heat-stable and is specified by most manufacturers for vehicles made in the last 10 years. If your mechanic recommends synthetic oil, this is one of the reasons why.</p>
      <h2>Check Your Logbook First</h2>
      <p>Your manufacturer's service logbook is the authoritative source for your specific vehicle's requirements. Look for the service schedule section — it lists the interval and what's included at each service point. If you've lost your logbook, your vehicle's VIN can be used to look up the manufacturer's schedule.</p>
      <h2>Warning Signs You Need a Service Now</h2>
      <ul>
        <li>Service light illuminated on your dashboard</li>
        <li>Dark, dirty oil when you check the dipstick</li>
        <li>Engine running rougher than usual</li>
        <li>Increased fuel consumption</li>
        <li>More than 12 months since last service regardless of km</li>
      </ul>
"""
  },
  {
    "slug": "blog-signs-car-needs-mechanic",
    "title": "7 Signs Your Car Urgently Needs a Mechanic",
    "h1": "7 Signs Your Car Urgently Needs a Mechanic in Perth",
    "tag": "Emergency",
    "meta": "7 warning signs your car urgently needs a mechanic. Don't ignore these symptoms — they indicate serious issues that get more expensive the longer you wait.",
    "read_time": 5,
    "excerpt": "Some car problems can wait. These seven can't. If you notice any of these warning signs in your Perth vehicle, book a mechanic today before the repair bill gets much worse.",
    "content": """
      <p>Some car issues are minor inconveniences that can wait for the next scheduled service. Others are urgent safety risks or problems that escalate dramatically in cost if left unattended. Here are the seven signs that mean you need a Perth mechanic now — not next month.</p>
      <h2>1. Warning Lights on Your Dashboard</h2>
      <p>The engine warning light, oil pressure light, temperature warning, or brake warning light all indicate a system that needs immediate attention. Don't assume it's just a sensor glitch — these lights exist because something needs professional diagnosis. Have your vehicle scanned for fault codes.</p>
      <h2>2. Brakes Grinding, Squealing, or Feeling Soft</h2>
      <p>Brake noise or a soft pedal pedal means your stopping ability is compromised. Grinding usually indicates metal-on-metal contact — pads have worn through and rotors are being damaged with every stop. This is a safety emergency, not an inconvenience.</p>
      <h2>3. Overheating</h2>
      <p>If your temperature gauge is creeping toward the red, pull over immediately. In Perth's summer heat, overheating can cause catastrophic engine damage within minutes of ignition. Do not continue driving an overheating vehicle.</p>
      <h2>4. Oil Pressure Warning</h2>
      <p>The oil pressure warning light is one of the most serious warnings your car can give you. Low oil pressure means moving engine parts may not be adequately lubricated — continued driving can cause permanent engine damage costing thousands to repair.</p>
      <h2>5. Steering or Suspension Feels Wrong</h2>
      <p>Pulling to one side, vibration through the steering wheel, unusual noises over bumps, or a feeling that the car is "wandering" all indicate suspension or steering issues. These affect your vehicle's handling and can cause tyre wear and control problems.</p>
      <h2>6. Unusual Smoke or Smells</h2>
      <p>White smoke from the exhaust can indicate coolant burning (head gasket issue). Blue smoke indicates oil burning. Black smoke means over-fuelling. A burning smell without smoke suggests an electrical fault or brake/clutch issue. Any unusual smoke or smell needs urgent investigation.</p>
      <h2>7. Starting Problems</h2>
      <p>A car that struggles to start, clicks but won't turn over, or starts intermittently has a battery, alternator, or starter motor problem. In Perth's summer heat, battery failure becomes more common — and getting stranded is significantly worse than proactively replacing a borderline battery.</p>
"""
  },
  {
    "slug": "blog-choose-mechanic-perth",
    "title": "How to Choose a Trustworthy Mechanic in Perth",
    "h1": "How to Choose a Trustworthy Mechanic in Perth",
    "tag": "Guide",
    "meta": "How to find a trustworthy mechanic in Perth: what qualifications to check, what questions to ask, and the red flags that indicate a mechanic you should avoid.",
    "read_time": 6,
    "excerpt": "Finding a trustworthy mechanic in Perth is harder than it should be. Here's exactly what to look for, what to ask, and the warning signs that should send you elsewhere.",
    "content": """
      <p>Perth has hundreds of mechanic workshops, ranging from excellent to genuinely problematic. The challenge for drivers is that it's hard to tell the difference until you've already handed over your keys. Here's how to evaluate a mechanic before trusting them with your vehicle.</p>
      <h2>Check Their Licence</h2>
      <p>In Western Australia, mechanics performing vehicle repair work must hold a Motor Vehicle Repairer licence issued by Consumer Protection WA. This is non-negotiable — it's a legal requirement. You can verify a mechanic's licence online through the Consumer Protection WA website. If a workshop can't or won't confirm their licensing, walk away.</p>
      <h2>Look for Genuine Reviews</h2>
      <p>Google Reviews are a reasonable signal for mechanic quality — but look at the pattern, not just the star rating. A mechanic with 40 genuine reviews averaging 4.7 stars is more reliable than one with 200 reviews averaging 4.9 (which can indicate managed reviews). Look for reviews that mention specific work done, honest assessments, and follow-through on quotes.</p>
      <h2>Get a Written Quote Before Authorising Work</h2>
      <p>A trustworthy mechanic always provides a written quote before starting work. Under WA consumer law, mechanics are required to provide an estimate upon request and cannot charge significantly more than that estimate without contacting you first. If a mechanic won't quote before starting, that's a significant red flag.</p>
      <h2>Questions to Ask Before Committing</h2>
      <ul>
        <li>Are you a licensed Motor Vehicle Repairer?</li>
        <li>Can you provide a written quote before starting work?</li>
        <li>Do you use genuine or OEM-equivalent parts?</li>
        <li>What warranty do you provide on your work?</li>
        <li>Will you show me the old parts if you replace something?</li>
      </ul>
      <h2>Red Flags to Watch For</h2>
      <ul>
        <li>Won't provide a written quote upfront</li>
        <li>Quotes low, then discovers additional problems once the car is pulled apart</li>
        <li>Pressures you to approve additional work immediately without time to consider</li>
        <li>Can't explain clearly what work they found is needed</li>
        <li>No fixed address — pop-up mechanics without a verifiable business location</li>
      </ul>
"""
  },
  {
    "slug": "blog-what-included-car-service",
    "title": "What's Included in a Full Car Service? Complete Checklist",
    "h1": "What's Included in a Full Car Service? Complete Perth Checklist",
    "tag": "Checklist",
    "meta": "What's included in a car service in Perth? Full checklist of minor service, major service, and logbook service items — so you know exactly what you're paying for.",
    "read_time": 7,
    "excerpt": "Not sure what a car service actually includes? Here's the complete checklist of what a minor service, major service, and logbook service covers — so you know exactly what you're getting.",
    "content": """
      <p>Many Perth drivers pay for car services without knowing exactly what work is being done. Here's a complete breakdown of what should be included in each service type, so you can verify you're getting what you're paying for.</p>
      <h2>Minor Service — What's Included</h2>
      <ul>
        <li>Engine oil drain and refill with specified grade oil</li>
        <li>Oil filter replacement</li>
        <li>Coolant level check and top-up</li>
        <li>Brake fluid level check</li>
        <li>Power steering fluid check (if applicable)</li>
        <li>Windscreen washer fluid top-up</li>
        <li>Battery condition check</li>
        <li>Tyre pressure check and adjustment</li>
        <li>Tyre tread depth check</li>
        <li>Brake inspection (visual check of pad thickness)</li>
        <li>Lights check (all exterior lights)</li>
        <li>Drive belt visual inspection</li>
        <li>Under-vehicle inspection for leaks</li>
      </ul>
      <h2>Major Service — Additional Items</h2>
      <ul>
        <li>Air filter replacement</li>
        <li>Cabin (pollen) filter replacement</li>
        <li>Spark plug replacement (petrol vehicles)</li>
        <li>Glow plug inspection (diesel vehicles)</li>
        <li>Brake fluid flush and replacement</li>
        <li>Coolant flush (at specified intervals)</li>
        <li>Fuel filter replacement (if serviceable)</li>
        <li>Detailed brake inspection including callipers</li>
        <li>Suspension visual inspection</li>
        <li>Steering components visual inspection</li>
        <li>Exhaust inspection</li>
        <li>Throttle body cleaning (some vehicles)</li>
      </ul>
      <h2>Logbook Service — Extra Requirements</h2>
      <ul>
        <li>All items from minor or major service per manufacturer schedule</li>
        <li>Manufacturer-specified oil grade and part numbers used</li>
        <li>All items on the manufacturer's service checklist completed</li>
        <li>Service history logbook stamped with date and odometer</li>
        <li>Any manufacturer-specific items (e.g. transmission fluid, transfer case oil) as specified</li>
      </ul>
      <h2>What Should Be Documented</h2>
      <p>A reputable mechanic will provide you with a service invoice listing every item checked and replaced. This is your proof of service for warranty and resale purposes. If the invoice only says "minor service" without a checklist, ask for itemisation.</p>
"""
  },
  {
    "slug": "blog-pre-purchase-inspection-perth",
    "title": "Pre-Purchase Car Inspection Perth: Why You Need One",
    "h1": "Pre-Purchase Car Inspection Perth: Why You Need One Before Buying",
    "tag": "Guide",
    "meta": "Pre-purchase car inspection Perth: what's checked, how much it costs ($150-$250), and why skipping it on a used car purchase is a false economy.",
    "read_time": 5,
    "excerpt": "A pre-purchase car inspection costs $150-$250 in Perth. It can save you from buying a car with $5,000+ in hidden faults. Here's exactly what gets checked and why it's always worth it.",
    "content": """
      <p>Buying a used car in Perth without a pre-purchase inspection is a gamble. The person selling the car knows more about its history than you do — and not all of that information is volunteered. A pre-purchase inspection by a qualified mechanic levels the playing field.</p>
      <h2>What Is a Pre-Purchase Inspection?</h2>
      <p>A pre-purchase inspection (PPI) is a comprehensive mechanical assessment of a vehicle performed by a qualified mechanic before you commit to buying it. The mechanic checks every major system and produces a written report detailing the vehicle's current condition, any faults found, and an assessment of likely future maintenance costs.</p>
      <h2>What Gets Checked</h2>
      <ul>
        <li>Engine condition — compression, oil leaks, unusual noises</li>
        <li>Transmission — smooth gear changes, no slipping or jerking</li>
        <li>Brakes — pad thickness, rotor condition, brake fluid</li>
        <li>Suspension and steering — wear in bushings, ball joints, tie rod ends</li>
        <li>Tyres — tread depth, age, uneven wear patterns</li>
        <li>Body and chassis — evidence of accident damage, rust, structural issues</li>
        <li>Electrical systems — all lights, climate control, windows</li>
        <li>OBD-II diagnostic scan — any stored fault codes</li>
        <li>Fluid conditions — oil colour, coolant condition</li>
        <li>Test drive assessment</li>
      </ul>
      <h2>How Much Does a PPI Cost in Perth?</h2>
      <p>A pre-purchase inspection in Perth typically costs $150–$250 depending on the thoroughness of the inspection and the mechanic. Some mechanics charge more for European vehicles due to the additional diagnostic complexity. Compare this to the potential cost of buying a car with undisclosed mechanical faults — engine work can cost $3,000–$15,000+.</p>
      <h2>When Should You Get One?</h2>
      <p>Always — for any private sale vehicle over $5,000. Even for dealer sales, a PPI is worthwhile on older or higher-kilometre vehicles. A dealer who refuses to allow a pre-purchase inspection should be treated as a red flag.</p>
      <h2>Who Pays — Buyer or Seller?</h2>
      <p>The buyer pays for a pre-purchase inspection. It's your due diligence cost. If the inspection finds significant faults, you can use the report to negotiate a price reduction or walk away entirely.</p>
"""
  },
  {
    "slug": "blog-car-ac-service-perth",
    "title": "Car Air Conditioning Service Perth: When & Why",
    "h1": "Car Air Conditioning Service Perth: When to Service and Why It Matters",
    "tag": "Service",
    "meta": "Car air conditioning service Perth: when to re-gas, signs your AC needs attention, and why Perth's extreme summer makes AC maintenance essential.",
    "read_time": 4,
    "excerpt": "Perth's summers regularly hit 40°C+. A failing car AC in February is more than uncomfortable — it's a health risk. Here's when to service your car's AC and what's involved.",
    "content": """
      <p>Car air conditioning is a necessity in Perth, not a luxury. With summer temperatures regularly exceeding 40°C, a functioning AC system is a basic safety requirement — especially for families with children or elderly passengers. Here's what Perth drivers need to know about AC servicing.</p>
      <h2>Signs Your Car's AC Needs Servicing</h2>
      <ul>
        <li>Air isn't as cold as it used to be — most common sign of low refrigerant</li>
        <li>System takes longer to cool the cabin after starting</li>
        <li>Unusual noise when AC is turned on</li>
        <li>Water dripping inside the cabin (not outside) — blocked drain line</li>
        <li>Musty or mouldy smell from the vents — cabin filter or evaporator issue</li>
        <li>AC light flashing — system fault code requiring diagnosis</li>
      </ul>
      <h2>What Is an AC Re-Gas?</h2>
      <p>An AC re-gas (refrigerant recharge) is the most common AC service — the mechanic removes the old refrigerant, checks for leaks, and refills the system to the manufacturer's specified pressure. Most vehicles lose a small amount of refrigerant naturally over time. A re-gas typically restores full cooling performance in systems without underlying faults.</p>
      <h2>How Much Does AC Servicing Cost in Perth?</h2>
      <ul>
        <li>Re-gas only: $120–$180</li>
        <li>Re-gas with leak test: $150–$220</li>
        <li>Full system service including cabin filter: $180–$280</li>
        <li>Compressor replacement: $600–$1,500+ depending on vehicle</li>
      </ul>
      <h2>How Often Should You Service Your Car's AC?</h2>
      <p>Most manufacturers recommend an AC service every 2 years or whenever you notice reduced performance. In Perth's climate, where AC systems run heavily for 6+ months per year, annual checks are sensible. Replacing the cabin filter (which filters the air entering the cabin) should be done every 12–15,000km.</p>
      <h2>Don't Run a Low-Refrigerant System</h2>
      <p>Running your AC when refrigerant is low damages the compressor — the most expensive component in the system. A $150 re-gas preventing a $1,200 compressor replacement is straightforward value arithmetic.</p>
"""
  },
  {
    "slug": "blog-brake-pads-vs-discs-perth",
    "title": "Brake Pads vs Brake Discs: What Needs Replacing?",
    "h1": "Brake Pads vs Brake Discs: What Needs Replacing in Perth?",
    "tag": "Info",
    "meta": "When do brake pads vs brake discs need replacing? How to tell the difference, typical costs in Perth, and why brake maintenance should never be deferred.",
    "read_time": 5,
    "excerpt": "Brake pads and discs wear at different rates. Understanding which needs replacing — and when — can save you hundreds compared to replacing both unnecessarily. Perth driver's guide.",
    "content": """
      <p>Brakes are the single most important safety system on your vehicle. Understanding the difference between pad wear and disc wear — and knowing when each needs attention — helps you maintain your brakes correctly and avoid overpaying for unnecessary replacements.</p>
      <h2>How Disc Brakes Work</h2>
      <p>Disc brake systems use a caliper to squeeze brake pads against a spinning metal disc (rotor) to slow the vehicle. The pads are the sacrificial wear component — designed to wear out and be replaced relatively cheaply. The discs are thicker and designed to last longer, but do wear and can also warp from heat cycling.</p>
      <h2>When Do Brake Pads Need Replacing?</h2>
      <p>Brake pads need replacing when:</p>
      <ul>
        <li>The pad thickness reaches 2–3mm (minimum safe thickness) — usually indicated by a wear indicator that creates a squealing sound</li>
        <li>You hear persistent squealing during normal braking (not just cold weather)</li>
        <li>You hear grinding metal-on-metal contact — pads are completely worn through</li>
        <li>Visual inspection shows thin pads through the wheel spokes</li>
      </ul>
      <h2>When Do Brake Discs Need Replacing?</h2>
      <p>Brake discs need replacing or machining when:</p>
      <ul>
        <li>Disc thickness is below the manufacturer's minimum specification</li>
        <li>Deep grooves are scored into the disc surface from worn-through pads</li>
        <li>Significant warping causes pulsation through the pedal under braking</li>
        <li>Significant rust pitting that can't be machined out</li>
      </ul>
      <h2>Do You Always Replace Both Together?</h2>
      <p>Not necessarily — but it depends on the condition of each. If pads are worn but discs are within specification and free of scoring, replacing pads only is appropriate. If discs are scored or below minimum thickness, they must be replaced or machined — and new pads should always go on with machined or new discs. Running new pads on worn discs compromises performance and accelerates the new pads' wear.</p>
      <h2>Typical Brake Costs in Perth</h2>
      <ul>
        <li>Brake pad replacement (front or rear): $180–$350</li>
        <li>Brake disc machining (per axle): $120–$200</li>
        <li>Brake disc replacement (per axle, budget pads): $280–$500</li>
        <li>Full brake job (all four corners, quality parts): $600–$1,200</li>
      </ul>
"""
  },
  {
    "slug": "blog-auto-electrical-problems",
    "title": "Auto Electrical Problems: Warning Signs & Solutions",
    "h1": "Auto Electrical Problems: Warning Signs and Solutions",
    "tag": "Info",
    "meta": "Auto electrical problems in Perth: warning signs of battery, alternator, and electrical faults, and what to do before you're stranded on the road.",
    "read_time": 5,
    "excerpt": "Modern vehicles are complex electrical systems. These are the most common auto electrical problems Perth drivers face — and what to do before a warning light becomes a breakdown.",
    "content": """
      <p>Modern vehicles contain more complex electrical systems than ever before. The average new car has over 100 million lines of software code — and when electrical systems fail, they can be difficult to diagnose without the right equipment. Here are the most common auto electrical problems Perth drivers encounter.</p>
      <h2>Battery Problems</h2>
      <p>The battery is the most common point of electrical failure. Warning signs include:</p>
      <ul>
        <li>Slow or laboured engine cranking when starting</li>
        <li>Battery warning light on dashboard</li>
        <li>Electrical accessories behaving erratically (windows slow, lights dim)</li>
        <li>Car starts fine in cool conditions but struggles in summer heat</li>
      </ul>
      <p>Perth's extreme summer heat accelerates battery degradation. Most car batteries last 3–5 years in Perth conditions — shorter than the same battery would last in a cooler climate. Have your battery load-tested if it's over 3 years old — this test reveals actual capacity, not just voltage.</p>
      <h2>Alternator Problems</h2>
      <p>The alternator charges the battery while the engine runs. Signs of alternator failure:</p>
      <ul>
        <li>Battery warning light (red battery icon) on the dashboard</li>
        <li>Dimming headlights while driving</li>
        <li>Multiple electrical accessories failing simultaneously</li>
        <li>Battery going flat even after charging — alternator isn't maintaining charge</li>
      </ul>
      <h2>Starter Motor Problems</h2>
      <p>The starter motor cranks the engine for starting. Signs of starter failure:</p>
      <ul>
        <li>Single or multiple clicks when turning the key — starter solenoid engaging but motor not turning</li>
        <li>Intermittent starting — works fine sometimes, then doesn't</li>
        <li>Grinding noise on startup — starter gear not engaging properly</li>
      </ul>
      <h2>Sensor and ECU Problems</h2>
      <p>Modern vehicles use dozens of sensors to manage engine performance, emissions, and safety systems. When sensors fail, the engine management system throws fault codes that illuminate the check engine light. Common sensor faults include oxygen sensors, mass airflow sensors, and throttle position sensors. These require OBD-II diagnostic scanning by a qualified auto electrician to correctly identify.</p>
      <h2>What to Do When You Have Electrical Issues</h2>
      <p>Don't ignore warning lights — they indicate a system that needs professional diagnosis. An auto electrician with current diagnostic equipment can identify the fault quickly and accurately, preventing you from replacing parts unnecessarily. Perth Mechanic connects you with qualified auto electricians across all suburbs.</p>
"""
  },
  {
    "slug": "blog-mechanic-fremantle",
    "title": "Best Mechanic in Fremantle: What to Look For",
    "h1": "Finding the Best Mechanic in Fremantle: What Freo Drivers Need to Know",
    "tag": "Suburb",
    "meta": "Looking for a mechanic in Fremantle? What to look for, typical service costs, and how Perth Mechanic connects Fremantle drivers with qualified, affordable mechanics.",
    "read_time": 4,
    "excerpt": "Fremantle's mix of older European vehicles and inner-suburb demographics creates specific demands for mechanics. Here's what Fremantle drivers should look for in a local mechanic.",
    "content": """
      <p>Fremantle is one of Perth's most distinctive suburbs — a mix of heritage, port culture, and a youthful, independent spirit. The vehicle mix reflects the suburb's character: older European cars are more common here than almost anywhere else in Perth, alongside the usual Japanese and Korean family vehicles.</p>
      <h2>What Makes Fremantle Mechanics Different</h2>
      <p>Mechanics who work extensively in Fremantle are used to seeing older vehicles — VW Golf, Mercedes sedans from the 2000s, older BMWs — alongside newer family cars. If your vehicle is European or older, a mechanic with experience in those makes is especially important.</p>
      <h2>What to Look For in a Fremantle Mechanic</h2>
      <ul>
        <li>Licensed Motor Vehicle Repairer (verify through Consumer Protection WA)</li>
        <li>Experience with your vehicle make — particularly important for European vehicles</li>
        <li>Written quotes provided before work begins</li>
        <li>Honest diagnosis — not every knock or clunk is an expensive repair</li>
        <li>Genuine reviews from Fremantle customers</li>
      </ul>
      <h2>Typical Service Costs in Fremantle</h2>
      <ul>
        <li>Minor service (Japanese/Korean): $160–$250</li>
        <li>Minor service (European): $220–$380</li>
        <li>Major service (Japanese/Korean): $300–$500</li>
        <li>Major service (European): $450–$900+</li>
        <li>Pre-purchase inspection: $160–$260</li>
      </ul>
      <h2>How Perth Mechanic Helps Fremantle Drivers</h2>
      <p>Perth Mechanic maintains a curated network of qualified mechanics in Fremantle and surrounding western suburbs. When you submit a request, we match you with a mechanic whose expertise fits your vehicle — European specialists for European cars, not a generalist who'll work from a service manual they're unfamiliar with.</p>
      <p>Submit a quote request to find a Fremantle mechanic today — we respond within 30 minutes.</p>
"""
  },
  {
    "slug": "blog-mechanic-joondalup",
    "title": "Finding a Reliable Mechanic in Joondalup",
    "h1": "Finding a Reliable Mechanic in Joondalup: Local Driver's Guide",
    "tag": "Suburb",
    "meta": "Looking for a mechanic in Joondalup? What to look for, typical service costs in the northern suburbs, and how to find a trustworthy local mechanic.",
    "read_time": 4,
    "excerpt": "Joondalup is one of Perth's largest northern hubs with a busy car culture. Here's what local drivers need to know about finding a reliable, honest mechanic in Joondalup.",
    "content": """
      <p>Joondalup is the commercial and residential hub of Perth's northern corridor — home to Lakeside Joondalup, Edith Cowan University, and a large population of families with newer vehicles. The demand for mechanic services in Joondalup is consistently high, and the quality varies. Here's how to find a reliable one.</p>
      <h2>Joondalup's Vehicle Mix</h2>
      <p>Joondalup and the northern corridor have a high proportion of newer family vehicles — SUVs, mid-size sedans, and people movers are common. Logbook services are a major part of the local mechanic workload, given the number of vehicles still within warranty periods driven by northern suburbs families.</p>
      <h2>What to Look for in a Joondalup Mechanic</h2>
      <ul>
        <li>Current Motor Vehicle Repairer licence</li>
        <li>Experience with your specific vehicle make and model</li>
        <li>Ability to perform manufacturer logbook services with stamping</li>
        <li>Clear, upfront pricing before any work begins</li>
        <li>Good local reputation — ask neighbours or check Google Reviews</li>
      </ul>
      <h2>Typical Mechanic Costs in Joondalup</h2>
      <ul>
        <li>Logbook service: $200–$380</li>
        <li>Minor service: $160–$260</li>
        <li>Major service: $320–$580</li>
        <li>Brake pad replacement: $190–$360</li>
        <li>AC re-gas: $130–$200</li>
      </ul>
      <h2>Perth Mechanic's Joondalup Network</h2>
      <p>We have qualified, licensed mechanics available throughout Joondalup and the northern corridor. Submit a quote request and we'll match you with the right mechanic for your vehicle and service needs. We respond within 30 minutes during business hours.</p>
"""
  },
  {
    "slug": "blog-mechanic-osborne-park",
    "title": "Mechanic in Osborne Park: Perth's Auto Hub Explained",
    "h1": "Mechanic in Osborne Park: Perth's Auto Hub Explained",
    "tag": "Suburb",
    "meta": "Osborne Park is Perth's auto strip — dealerships and mechanics line Scarborough Beach Road. Here's how to navigate the choices and find a trustworthy Osborne Park mechanic.",
    "read_time": 4,
    "excerpt": "Osborne Park's Scarborough Beach Road is Perth's car strip — dealerships, tyre shops, and mechanics everywhere. Here's how to navigate it and find a mechanic worth trusting.",
    "content": """
      <p>Osborne Park is arguably Perth's most densely automotive suburb. Scarborough Beach Road through the area is lined with car dealerships, tyre shops, smash repairers, and mechanic workshops. For drivers, the abundance of choice is both an advantage and a challenge — quality varies significantly.</p>
      <h2>Dealerships vs Independent Mechanics in Osborne Park</h2>
      <p>The concentration of dealerships on the Osborne Park strip creates a common misconception: that dealership service departments are the best option for your car. This isn't true. Dealership service centres employ qualified technicians — but so do independent mechanics. The difference is labour rates:</p>
      <ul>
        <li>Dealership labour: typically $180–$280/hour</li>
        <li>Independent mechanic labour: typically $110–$160/hour</li>
      </ul>
      <p>For the same work, the same parts, and the same qualified technician skill level, independent mechanics consistently offer better value.</p>
      <h2>How to Choose Among Osborne Park's Options</h2>
      <ul>
        <li>Verify the mechanic's licence — applies to independents and dealerships alike</li>
        <li>Get a written quote for specific work — compare apples to apples</li>
        <li>Ask about part quality — OEM vs aftermarket vs genuine, and what each means for your vehicle</li>
        <li>Check their specialisation for European vehicles if applicable</li>
      </ul>
      <h2>Perth Mechanic's Osborne Park Network</h2>
      <p>We've curated a network of qualified independent mechanics in Osborne Park who consistently provide quality work at honest prices. Submit a request and we'll match you with the right mechanic — no need to navigate the strip yourself.</p>
"""
  },
  {
    "slug": "blog-mechanic-rockingham",
    "title": "Best Mechanic in Rockingham: Local Driver's Guide",
    "h1": "Best Mechanic in Rockingham: What Local Drivers Need to Know",
    "tag": "Suburb",
    "meta": "Looking for a mechanic in Rockingham? Local driver's guide to finding a qualified, reliable mechanic in Rockingham and surrounding southern suburbs.",
    "read_time": 4,
    "excerpt": "Rockingham drivers have specific mechanical needs — from Defence Housing vehicle servicing to coastal corrosion checks. Here's what to look for in a Rockingham mechanic.",
    "content": """
      <p>Rockingham's coastal location and significant Defence Housing community create specific demands for mechanical services that differ slightly from other Perth suburbs. Here's what Rockingham drivers need to know.</p>
      <h2>Rockingham's Unique Vehicle Profile</h2>
      <p>Rockingham has a higher-than-average proportion of utes, 4WDs, and practical working vehicles — common among Defence personnel and tradies in the area. The coastal environment also means vehicles are more exposed to salt-air corrosion than inland suburbs.</p>
      <h2>Coastal Considerations for Rockingham Vehicles</h2>
      <ul>
        <li>Brake components — brake lines and callipers corrode faster in coastal environments</li>
        <li>Exhaust — salt air accelerates rust on exhaust systems</li>
        <li>Suspension — bushes and ball joints benefit from periodic inspection and greasing</li>
        <li>Regular underbody checks are particularly valuable for Rockingham vehicles</li>
      </ul>
      <h2>What to Look For in a Rockingham Mechanic</h2>
      <ul>
        <li>Licensed Motor Vehicle Repairer — verify through Consumer Protection WA</li>
        <li>4WD and ute servicing experience if applicable to your vehicle</li>
        <li>Awareness of coastal corrosion in their inspection routine</li>
        <li>Clear upfront pricing and written quotes</li>
      </ul>
      <h2>Typical Costs in Rockingham</h2>
      <ul>
        <li>Minor service: $160–$260</li>
        <li>Major service: $310–$560</li>
        <li>4WD service: $280–$500+</li>
        <li>AC re-gas: $130–$210</li>
        <li>Pre-purchase inspection: $150–$250</li>
      </ul>
      <p>Perth Mechanic has mechanics available across Rockingham, Safety Bay, and surrounding southern coastal suburbs. Submit a quote request for a 30-minute response.</p>
"""
  },
  {
    "slug": "blog-mechanic-armadale",
    "title": "Mechanic in Armadale: What Residents Should Know",
    "h1": "Mechanic in Armadale: What Residents Need to Know",
    "tag": "Suburb",
    "meta": "Looking for a mechanic in Armadale? What Armadale and south-eastern Perth residents need to know about local mechanic services, costs, and finding qualified professionals.",
    "read_time": 4,
    "excerpt": "Armadale's rapid growth brings lots of newer vehicles requiring logbook servicing. Here's what Armadale residents need to know about finding a good local mechanic.",
    "content": """
      <p>Armadale has grown rapidly over the past decade, with new estates across Haynes, Harrisdale, and Piara Waters bringing thousands of new residents — and thousands of newer vehicles. The suburb's growth means mechanic demand is high and options are expanding.</p>
      <h2>Armadale's Vehicle Profile</h2>
      <p>New estate residents in Armadale typically drive newer vehicles — many still within their warranty periods. Logbook servicing is the dominant service category, followed by the inevitable repairs that arise as the vehicle population ages. First-home buyers and young families make up a large proportion of the Armadale market, often with Japanese and Korean brand vehicles.</p>
      <h2>Why Logbook Service Matters in Armadale</h2>
      <p>With so many newer vehicles in the suburb, maintaining logbook service records is particularly important for Armadale residents. A complete, stamped service history protects your warranty and significantly improves resale value — especially relevant for vehicles on finance that may be sold or traded within the first 3–5 years.</p>
      <h2>What to Look For in an Armadale Mechanic</h2>
      <ul>
        <li>Current Motor Vehicle Repairer licence</li>
        <li>Manufacturer logbook servicing capability — ask if they use manufacturer-specified parts</li>
        <li>Upfront written quotes</li>
        <li>Good response time — Armadale is growing and good mechanics book out quickly</li>
      </ul>
      <h2>Typical Costs in Armadale</h2>
      <ul>
        <li>Logbook service: $190–$360</li>
        <li>Minor service: $150–$250</li>
        <li>Major service: $290–$520</li>
        <li>Brake repairs: $190–$380</li>
      </ul>
      <p>Perth Mechanic covers Armadale and surrounding southeastern suburbs. Get a same-day quote by submitting your request online.</p>
"""
  },
  {
    "slug": "blog-new-tyres-perth-guide",
    "title": "When to Get New Tyres: Perth Driver's Complete Guide",
    "h1": "When to Get New Tyres: Perth Driver's Complete Guide",
    "tag": "Guide",
    "meta": "When do you need new tyres in Perth? Tread depth minimums, age limits, and warning signs that your tyres need replacing. Complete guide for Perth drivers.",
    "read_time": 5,
    "excerpt": "Perth's hot roads and sun exposure age tyres faster than cooler climates. Here's how to know when you need new tyres, what to look for, and how much they cost.",
    "content": """
      <p>Tyres are your vehicle's only contact with the road — and in Perth's conditions, they face specific challenges that accelerate wear and ageing compared to cooler climates. Here's how to know when yours need replacing.</p>
      <h2>Legal Minimum Tread Depth in WA</h2>
      <p>In Western Australia, tyres must have a minimum tread depth of 1.5mm across the full width of the tread area. Most tyres have tread wear indicators — small raised sections moulded into the grooves at 1.6mm height. When the tread is level with these indicators, the tyre is legally worn out. Many safety experts recommend replacing at 3mm — tyre performance in wet conditions degrades significantly below this level.</p>
      <h2>Checking Tread Depth</h2>
      <ul>
        <li>Tread wear indicators: visible in the main tyre grooves at the legal limit</li>
        <li>20-cent coin test: insert a 20-cent coin into the groove — if you can see the full number 20, the tread is below 3mm</li>
        <li>Tread depth gauge: most mechanics have these and can check for free</li>
      </ul>
      <h2>Tyre Age — Perth's UV Problem</h2>
      <p>Perth's intense UV radiation and summer heat cause rubber to degrade faster than in cooler climates. A tyre that looks fine may have significant internal cracking or sidewall degradation. Most tyre manufacturers recommend replacing tyres after 6 years regardless of apparent tread condition, and a maximum of 10 years from the date of manufacture. The manufacture date is moulded into the sidewall as a 4-digit code — the last four digits of the DOT code show the week and year of manufacture (e.g., "2319" = 23rd week of 2019).</p>
      <h2>Other Signs You Need New Tyres</h2>
      <ul>
        <li>Visible cracks in the sidewall — indicates rubber degradation</li>
        <li>Bulges or blisters in the sidewall — internal damage, immediate replacement needed</li>
        <li>Vibration through the steering that balancing doesn't fix</li>
        <li>Uneven tread wear — indicates alignment or suspension problems (fix the cause too)</li>
      </ul>
      <h2>Tyre Prices in Perth</h2>
      <ul>
        <li>Budget tyres (small car): $80–$130 each fitted</li>
        <li>Mid-range tyres (sedan/SUV): $130–$220 each fitted</li>
        <li>Premium tyres (sedan/SUV): $200–$400 each fitted</li>
        <li>4WD all-terrain tyres: $250–$500 each fitted</li>
      </ul>
"""
  },
  {
    "slug": "blog-car-overheating-perth",
    "title": "Car Overheating in Perth Summer: What To Do Right Now",
    "h1": "Car Overheating in Perth Summer: What To Do Right Now",
    "tag": "Emergency",
    "meta": "Car overheating in Perth summer? What to do immediately, what causes overheating, and how much engine overheating can cost if you don't act fast.",
    "read_time": 4,
    "excerpt": "Car overheating in Perth's 40+ degree summer can destroy your engine in minutes. Here's exactly what to do if your temperature gauge starts climbing — and how to prevent it.",
    "content": """
      <p>Perth's summer is one of the most demanding environments for vehicle cooling systems in Australia. When temperatures exceed 40°C and you're stuck in city traffic with the AC running, cooling systems are working at their limit. An overheating vehicle needs immediate action.</p>
      <h2>What To Do Immediately</h2>
      <p>If your temperature gauge is in the red or an overheat warning appears:</p>
      <ul>
        <li>Turn off the air conditioning immediately — this reduces engine load</li>
        <li>Turn on the heater to full heat — this helps dissipate engine heat through the cabin heater core</li>
        <li>Find a safe place to pull over as quickly as possible</li>
        <li>Turn the engine off and do NOT restart it</li>
        <li>Do NOT open the radiator cap — the cooling system is under pressure and will spray scalding coolant</li>
        <li>Wait at least 30 minutes for the engine to cool before approaching the radiator</li>
      </ul>
      <h2>What Causes Overheating?</h2>
      <ul>
        <li>Low coolant level — most common cause, often from a slow leak</li>
        <li>Faulty thermostat — stuck closed, preventing coolant circulation</li>
        <li>Failed radiator fan — fan not turning on when needed</li>
        <li>Blocked radiator — restricted airflow through the radiator core</li>
        <li>Head gasket failure — most serious cause, allows combustion gases into the cooling system</li>
        <li>Water pump failure — pump not circulating coolant</li>
      </ul>
      <h2>What Overheating Can Cost</h2>
      <ul>
        <li>Thermostat replacement: $150–$300</li>
        <li>Radiator fan replacement: $300–$600</li>
        <li>Water pump replacement: $400–$900</li>
        <li>Head gasket repair: $1,500–$4,000+</li>
        <li>Engine replacement (from severe overheating damage): $3,000–$15,000+</li>
      </ul>
      <p>The cost progression shows why stopping immediately is so critical. A vehicle that overheats briefly and is shut down promptly often needs only minor cooling system repairs. One that is driven for 10 minutes while overheating can suffer permanent engine damage.</p>
      <h2>Prevention</h2>
      <p>Check your coolant level monthly during Perth's summer. A quick check under the bonnet takes 30 seconds and can prevent a five-figure repair bill. If your level is repeatedly low, there's a leak that needs diagnosis before summer arrives.</p>
"""
  },
  {
    "slug": "blog-read-logbook-perth",
    "title": "How to Read Your Car's Service Logbook",
    "h1": "How to Read Your Car's Service Logbook",
    "tag": "Info",
    "meta": "How to read your car's manufacturer service logbook — what the service intervals mean, how to check if your car has been properly serviced, and what happens if the logbook is incomplete.",
    "read_time": 4,
    "excerpt": "Your car's service logbook is more than just a stamped record. Here's how to read it properly, what to look for, and what a missing stamp could mean for your warranty or resale value.",
    "content": """
      <p>Most car owners know they have a service logbook but aren't entirely sure what it means or how to use it. Here's a practical guide to reading your manufacturer's service logbook.</p>
      <h2>What Is the Service Logbook?</h2>
      <p>The service logbook is a document provided by the vehicle manufacturer that specifies exactly what maintenance needs to be performed at each service interval. It also provides a record — with stamps — of each service that has been completed, when, and by whom. This record is valuable for warranty coverage, resale value, and understanding your vehicle's maintenance history.</p>
      <h2>How to Read the Service Schedule</h2>
      <p>The logbook contains a service schedule table, typically showing:</p>
      <ul>
        <li>Odometer milestones (e.g., 10,000km, 20,000km, 30,000km) — the "what" for each service</li>
        <li>Time intervals (e.g., 12 months, 24 months) — the "when" for time-based items</li>
        <li>The "whichever comes first" rule — whichever threshold is reached first triggers the service</li>
        <li>Items marked with a different symbol or colour at certain intervals — these are more comprehensive services</li>
      </ul>
      <h2>Reading the Service History Stamps</h2>
      <p>Each service should have a stamp from the mechanic or dealership that performed it, along with:</p>
      <ul>
        <li>Date of service</li>
        <li>Odometer reading at time of service</li>
        <li>Signature or stamp of the mechanic / workshop</li>
        <li>Workshop name and contact details</li>
      </ul>
      <h2>What Missing Stamps Mean</h2>
      <p>A missing service stamp means that service was either not performed, or performed but not recorded. For warranty purposes, missing stamps can complicate warranty claims if the issue relates to a component covered by that service. For resale, a complete service history adds value — gaps reduce it. If you've lost your logbook, your vehicle's VIN can sometimes be used to retrieve the history.</p>
      <h2>Manufacturer vs Non-Dealer Stamps</h2>
      <p>A common question: are stamps from independent mechanics valid? Yes — under Australian consumer law, any qualified mechanic can perform your logbook service. Their stamp is as valid as a dealership stamp, provided the correct parts and fluids were used and all items completed.</p>
"""
  },
  {
    "slug": "blog-mechanic-ripping-off",
    "title": "How to Tell If Your Mechanic Is Ripping You Off",
    "h1": "How to Tell If Your Mechanic Is Ripping You Off",
    "tag": "Consumer",
    "meta": "How to tell if a mechanic is overcharging or recommending unnecessary work. The warning signs of a dishonest mechanic and your rights as a Perth driver.",
    "read_time": 6,
    "excerpt": "Not every mechanic is honest. These are the warning signs that you're being overcharged or upsold unnecessary work — and what your rights are under WA consumer law.",
    "content": """
      <p>Most Perth mechanics are honest professionals who do good work at fair prices. A small minority aren't — and their tactics are consistent enough that once you know what to look for, they're recognisable. Here's how to protect yourself.</p>
      <h2>Warning Sign #1: Quote Creep</h2>
      <p>You bring the car in for a specific job. The mechanic calls you and says they've found several additional problems that also need urgent attention. This happens to some extent with every vehicle — but watch for the pattern of discovery. Legitimate additional work is explained clearly, with a written quote for each item and no pressure to approve immediately. Dishonest mechanics use high-pressure tactics and vague descriptions to get you to approve additional work while you're on the phone.</p>
      <h2>Warning Sign #2: Not Showing Old Parts</h2>
      <p>When a mechanic replaces a part, they should offer to show you the old part upon request. If they won't — or if the old part looks suspiciously new when you see it — that's a concern. Ask to see what was replaced.</p>
      <h2>Warning Sign #3: Urgent But Vague</h2>
      <p>A mechanic who says "it needs urgent attention but I can't really explain it simply" is a red flag. Qualified mechanics should be able to explain in plain terms what's wrong and why it needs fixing. If the explanation is vague, ask follow-up questions until it's clear — or get a second opinion.</p>
      <h2>Warning Sign #4: No Written Quote</h2>
      <p>A reputable mechanic always provides a written quote before starting work. A mechanic who won't commit to a price in writing is creating an environment where the final invoice can be whatever they decide after the work is done. This isn't acceptable — it's also contrary to WA consumer law requirements.</p>
      <h2>Your Rights Under WA Consumer Law</h2>
      <ul>
        <li>You have the right to request a written estimate before authorising work</li>
        <li>Mechanics must contact you if the cost will exceed the estimate by a significant amount</li>
        <li>Work must be of acceptable quality and fit for purpose</li>
        <li>You can dispute an invoice that significantly exceeds the authorised quote</li>
      </ul>
      <h2>What to Do If You Think You've Been Overcharged</h2>
      <p>Request an itemised invoice. Compare it against the original quote. For any item significantly above the quote, ask for an explanation. If you're not satisfied, contact Consumer Protection WA — they handle complaints about motor vehicle repairers. You can also pursue disputes through the State Administrative Tribunal.</p>
"""
  },
  {
    "slug": "blog-service-history-resale",
    "title": "Why Car Service History Matters for Resale in WA",
    "h1": "Why Car Service History Matters for Resale Value in Western Australia",
    "tag": "Info",
    "meta": "How much does service history affect car resale value in WA? Complete service records can add thousands to your sale price. Here's why and how to maintain yours properly.",
    "read_time": 4,
    "excerpt": "A complete service history can add $1,000-$3,000+ to your car's resale value in WA. Here's why buyers care, what records to keep, and what to do if yours are incomplete.",
    "content": """
      <p>When selling a used car in Western Australia, the service history is one of the most important factors affecting price and buyer confidence. Here's what you need to know about maintaining and presenting your vehicle's service records.</p>
      <h2>How Much Does Service History Add to Resale Value?</h2>
      <p>A complete, stamped service history adds tangible value to used car sales in WA. Industry estimates suggest that a full service history adds:</p>
      <ul>
        <li>$500–$1,500 for budget vehicles under $15,000</li>
        <li>$1,500–$4,000 for mid-range vehicles $15,000–$40,000</li>
        <li>$3,000–$8,000 for premium vehicles over $40,000</li>
      </ul>
      <p>The effect is greater for older vehicles — a 2015 vehicle with full service history commands significantly more than the same vehicle with gaps in the record.</p>
      <h2>What Buyers Look For</h2>
      <ul>
        <li>Stamps at each interval — gaps raise questions about what was skipped</li>
        <li>Consistency between the logbook and odometer — do the services align with the km driven?</li>
        <li>Major service items — spark plugs, timing belt/chain, brake fluid flush</li>
        <li>Notes about any significant repairs — honest documentation of work done</li>
        <li>Service dates relative to current date — how recent is the last service?</li>
      </ul>
      <h2>Dealer vs Independent Mechanic Stamps</h2>
      <p>Independent mechanic stamps are perfectly legitimate and accepted by buyers. Many buyers prefer them — they suggest the owner was cost-conscious enough to use an independent rather than paying dealership prices, and the vehicle still received proper maintenance.</p>
      <h2>If Your Service History Has Gaps</h2>
      <p>If you've serviced your vehicle but don't have stamps — perhaps a mechanic didn't stamp the logbook, or you did your own oil changes — gather whatever documentation you can: invoices, receipts, photos. These provide partial evidence of maintenance even without formal stamps. For future services, always ensure the logbook is stamped.</p>
"""
  },
  {
    "slug": "blog-timing-belt-vs-chain",
    "title": "Timing Belt vs Timing Chain: When to Replace in Perth",
    "h1": "Timing Belt vs Timing Chain: What Perth Drivers Need to Know",
    "tag": "Info",
    "meta": "Does your car have a timing belt or timing chain? How to tell, when to replace, and what happens if a timing belt snaps. Complete guide for Perth drivers.",
    "read_time": 5,
    "excerpt": "Timing belt failure can destroy your engine in seconds. Timing chains should theoretically last the life of the vehicle — but don't always. Here's what Perth drivers need to know.",
    "content": """
      <p>The timing belt or chain is one of the most critical components in your engine — and also one of the least understood. Here's what Perth drivers need to know about this essential maintenance item.</p>
      <h2>What Does the Timing Belt or Chain Do?</h2>
      <p>The timing belt or chain synchronises the crankshaft (which drives the pistons) with the camshaft (which opens the intake and exhaust valves) to ensure the valves open and close at precisely the right moments. If this synchronisation fails — even momentarily — the valves and pistons can collide, causing catastrophic engine damage.</p>
      <h2>Timing Belt vs Timing Chain: The Difference</h2>
      <p>A timing belt is a rubber-reinforced belt that requires periodic replacement as part of scheduled maintenance. A timing chain is a metal roller chain similar to a bicycle chain, designed to last significantly longer and typically not requiring scheduled replacement.</p>
      <ul>
        <li>Timing belts are quieter but have a finite lifespan (typically 60,000–100,000km)</li>
        <li>Timing chains are louder but designed to last the life of the engine if properly maintained</li>
        <li>Both can fail prematurely if oil changes are neglected — oil quality directly affects chain wear</li>
      </ul>
      <h2>How to Tell Which One Your Car Has</h2>
      <p>Check your owner's manual or ask your mechanic. Generally, if your vehicle has a timing belt replacement schedule in the logbook, it has a belt. If there's no replacement schedule mentioned for the timing component, it likely has a chain. Common timing belt engines include: older Honda, Subaru (EJ series), older Mitsubishi. Common timing chain engines include: most Toyota, Mazda, most newer Honda, most European brands from 2005+.</p>
      <h2>When to Replace a Timing Belt</h2>
      <p>Follow your manufacturer's specified interval — typically 60,000–100,000km or 5–7 years, whichever comes first. Perth's heat accelerates rubber degradation, so erring toward the earlier replacement is sensible. The water pump is usually replaced at the same time as the belt.</p>
      <h2>Timing Belt Replacement Cost in Perth</h2>
      <ul>
        <li>Four-cylinder engine: $600–$1,200 (including water pump)</li>
        <li>V6 engine: $900–$1,800</li>
        <li>If the belt snaps on an interference engine: $2,000–$10,000+</li>
      </ul>
"""
  },
  {
    "slug": "blog-fleet-servicing-perth",
    "title": "Fleet Vehicle Servicing Perth: Business Owner's Guide",
    "h1": "Fleet Vehicle Servicing Perth: Complete Business Owner's Guide",
    "tag": "B2B",
    "meta": "Fleet vehicle servicing Perth: how to manage scheduled maintenance, minimise downtime, and find mechanics who offer fleet programs for Perth businesses.",
    "read_time": 5,
    "excerpt": "Managing a fleet of vehicles is one of Perth's most common small business challenges. Here's how to set up a servicing program that minimises downtime and keeps vehicles on the road.",
    "content": """
      <p>For Perth businesses operating vehicle fleets — tradies with utes, delivery businesses, professional service firms — keeping vehicles serviced and on the road is a direct cost centre. Poorly managed fleet maintenance leads to breakdowns at the worst possible times and expensive reactive repairs instead of affordable preventive maintenance. Here's how to do it right.</p>
      <h2>The Cost of Reactive vs Preventive Fleet Maintenance</h2>
      <p>An unplanned breakdown typically costs 4–6 times more than a scheduled service to resolve, when you factor in:</p>
      <ul>
        <li>Emergency labour rates from roadside assistance or after-hours mechanics</li>
        <li>Towing costs</li>
        <li>Lost productivity while the vehicle is off the road</li>
        <li>Damage from running a vehicle beyond service intervals (oil breakdown, accelerated wear)</li>
      </ul>
      <h2>Setting Up a Fleet Service Program</h2>
      <p>An effective fleet service program includes:</p>
      <ul>
        <li>Scheduled service intervals tracked per vehicle (km or time-based)</li>
        <li>A mechanic partner who prioritises fleet work and understands your business needs</li>
        <li>Consolidated invoicing — one invoice per period rather than per job</li>
        <li>Service records maintained per vehicle</li>
        <li>Pre-purchase inspections before adding used vehicles to the fleet</li>
      </ul>
      <h2>What to Look For in a Fleet Mechanic</h2>
      <ul>
        <li>Experience with your vehicle types — utes, vans, 4WDs, sedans as applicable</li>
        <li>Ability to service multiple vehicles efficiently — not just a one-person shop</li>
        <li>Mobile servicing option for large fleets to reduce downtime</li>
        <li>Fleet account terms — don't pay per job, set up a proper account</li>
        <li>Proactive communication — contacts you before service is due, not after</li>
      </ul>
      <h2>Fleet Types Perth Mechanic Serves</h2>
      <ul>
        <li>Tradie utes (single or multi-vehicle operators)</li>
        <li>Delivery vans and light commercial vehicles</li>
        <li>Real estate and professional services car fleets</li>
        <li>NDIS and care transportation fleets</li>
        <li>Mining and construction support vehicles</li>
      </ul>
      <p>Perth Mechanic can connect Perth businesses with fleet-capable mechanics across all suburbs. Enquire today and we'll find a mechanic who fits your fleet size and service requirements.</p>
"""
  },
  {
    "slug": "blog-roadworthy-certificate-wa",
    "title": "Vehicle Examination Certificate WA: Everything You Need to Know",
    "h1": "Vehicle Examination Certificate WA: Complete Guide",
    "tag": "Compliance",
    "meta": "Vehicle Examination Certificate WA (formerly roadworthy certificate): when you need one, what's checked, how much it costs, and how to get a VEC in Perth.",
    "read_time": 5,
    "excerpt": "A Vehicle Examination Certificate (VEC) is required for certain vehicle transfers and modifications in WA. Here's when you need one, what's inspected, and how to get it in Perth.",
    "content": """
      <p>Western Australia's Vehicle Examination Certificate (VEC) — sometimes called a roadworthy or safety certificate — is required for specific vehicle transactions and modifications. Here's what Perth drivers need to know.</p>
      <h2>When Is a VEC Required in WA?</h2>
      <p>In Western Australia, a VEC is typically required when:</p>
      <ul>
        <li>Transferring a vehicle registration where the vehicle is more than a certain age</li>
        <li>Re-registering an unregistered vehicle</li>
        <li>Completing modifications to a vehicle that affect safety-critical systems</li>
        <li>Some dealers require it as part of a used vehicle sale</li>
      </ul>
      <p>Note: WA's requirements differ from other states. The VEC requirement here is more limited than in states like Victoria or Queensland where a roadworthy certificate is required for every vehicle transfer.</p>
      <h2>What Is Checked in a WA Vehicle Examination?</h2>
      <p>A vehicle examination in WA covers safety-critical systems:</p>
      <ul>
        <li>Brakes — operation, pad/shoe condition, fluid level</li>
        <li>Steering and suspension — condition and operation</li>
        <li>Tyres and wheels — tread depth, condition, rim condition</li>
        <li>Lights — all exterior lighting operation</li>
        <li>Windscreen and wipers — visibility and wiper operation</li>
        <li>Seatbelts — condition and operation</li>
        <li>Horn — operation</li>
        <li>Body structure — condition relevant to safety</li>
      </ul>
      <h2>Who Can Perform a Vehicle Examination in WA?</h2>
      <p>In WA, vehicle examinations must be performed by a licensed Authorised Examination Station (AES). Not all mechanics are licensed for this — check with your mechanic whether they hold AES authorisation, or Perth Mechanic can direct you to an AES-licensed mechanic in your area.</p>
      <h2>How Much Does a VEC Cost in Perth?</h2>
      <ul>
        <li>Vehicle examination: $100–$220 depending on vehicle type</li>
        <li>Any repairs required to pass: quoted separately by the mechanic</li>
      </ul>
      <h2>How Long Does a VEC Last?</h2>
      <p>A Vehicle Examination Certificate in WA is valid for a defined period for registration purposes. Check the current requirements with the Department of Transport WA as the specific validity period may have been updated.</p>
"""
  },
  {
    "slug": "blog-save-money-car-service-perth",
    "title": "7 Ways to Save Money on Car Servicing in Perth",
    "h1": "7 Ways to Save Money on Car Servicing in Perth",
    "tag": "Money",
    "meta": "How to save money on car servicing in Perth without compromising quality. 7 practical strategies for Perth drivers to reduce their car maintenance costs.",
    "read_time": 5,
    "excerpt": "Perth drivers can save significantly on car servicing without taking shortcuts that cost more in the long run. Here are 7 practical strategies that actually work.",
    "content": """
      <p>Car servicing in Perth doesn't have to cost as much as many drivers pay. With the right approach, you can maintain your vehicle properly while spending significantly less than the average driver. Here are seven strategies that work.</p>
      <h2>1. Use an Independent Mechanic Instead of a Dealership</h2>
      <p>This is the single biggest saving available to most Perth drivers. Dealership service departments typically charge $180–$280/hour in labour rates. Independent mechanics charge $110–$160/hour for the same work with equivalent parts. On a $400 service, that difference is often $100–$150 in labour alone.</p>
      <h2>2. Service on Schedule, Not Late</h2>
      <p>Running a car past its service interval doesn't save money — it costs more. Degraded oil increases engine wear. Worn brake pads destroy discs. Dirty air filters reduce fuel economy. Every deferred service costs more in accelerated wear than it saves in the deferred cost.</p>
      <h2>3. Compare Quotes</h2>
      <p>Get two or three quotes before committing to major repairs. There's genuine price variation among Perth mechanics for the same work — sometimes 20–30%. Perth Mechanic provides competitive quotes from our network so you know you're getting fair value.</p>
      <h2>4. Bundle Jobs Together</h2>
      <p>Labour is often the largest cost component in mechanical repairs. If you know two or three things need doing, have them done at the same appointment. The mechanic has already done the diagnosis and pulled apart the relevant areas — multiple jobs at once reduce total labour time.</p>
      <h2>5. Ask About Part Options</h2>
      <p>For non-warranty repairs, ask your mechanic about part quality tiers. Genuine manufacturer parts are the most expensive. OEM-equivalent (parts made to manufacturer specifications by specialist suppliers) are typically 20–40% cheaper with equivalent quality. Budget aftermarket parts exist but are appropriate only for low-stress applications. Ask the mechanic what they recommend and why for your specific situation.</p>
      <h2>6. Learn to Check Basics Yourself</h2>
      <p>Checking your oil level, coolant level, tyre pressures, and windscreen washer fluid takes 5 minutes and can prevent problems that escalate from minor to major. Top up between services. A low coolant level that's caught early is a $20 top-up; one that's not caught is a head gasket.</p>
      <h2>7. Keep Your Service Records</h2>
      <p>A complete service history is worth money at sale time — typically adding $1,000–$4,000 to a private sale. Every dollar spent on proper, documented servicing returns more than a dollar in resale value on a well-maintained vehicle. Don't cut corners and then sell the car at a discount because the history is incomplete.</p>
"""
  },
  {
    "slug": "blog-ev-servicing-perth",
    "title": "Electric Vehicle Servicing Perth: What EV Owners Need to Know",
    "h1": "Electric Vehicle Servicing Perth: Complete Guide for EV Owners",
    "tag": "EV",
    "meta": "Electric vehicle servicing in Perth: what EVs need, what they don't need, how costs compare to petrol cars, and where to get your EV serviced in Perth.",
    "read_time": 5,
    "excerpt": "EVs have fewer moving parts and lower servicing costs than petrol vehicles — but they still need maintenance. Here's what Perth EV owners need to know about servicing their electric vehicle.",
    "content": """
      <p>Electric vehicle ownership is growing in Perth, and with it comes a common question: what does an EV actually need for servicing, and who can do it? The good news is that EVs have significantly lower servicing requirements than petrol vehicles — but they still need attention.</p>
      <h2>What EVs Don't Need (That Petrol Cars Do)</h2>
      <ul>
        <li>Engine oil and oil filter changes — no combustion engine</li>
        <li>Spark plugs</li>
        <li>Timing belt or chain</li>
        <li>Fuel filter</li>
        <li>Transmission fluid (for most EVs with single-speed transmissions)</li>
        <li>Exhaust system servicing</li>
      </ul>
      <h2>What EVs Do Need</h2>
      <ul>
        <li>Tyre rotation and replacement — EVs are heavier than equivalent petrol cars, accelerating tyre wear</li>
        <li>Brake inspection — EVs use regenerative braking extensively, so brake pads last longer, but still require periodic inspection</li>
        <li>Cabin air filter replacement — same as any vehicle</li>
        <li>Coolant check — EV battery thermal management systems use coolant</li>
        <li>Windscreen wiper replacement</li>
        <li>12V auxiliary battery — EVs have a small 12V battery separate from the traction battery that needs periodic replacement</li>
        <li>Software updates — often done over-the-air, but some require workshop visits</li>
      </ul>
      <h2>Battery Maintenance</h2>
      <p>The high-voltage traction battery doesn't require routine service, but there are practices that protect its longevity:</p>
      <ul>
        <li>Avoid regularly charging to 100% — most manufacturers recommend 80% for daily use</li>
        <li>Avoid regularly depleting to 0%</li>
        <li>Use DC fast charging occasionally but not exclusively — repeated fast charging accelerates degradation</li>
        <li>In Perth's heat, keep the vehicle plugged in when possible — thermal management works better when connected to power</li>
      </ul>
      <h2>Who Can Service an EV in Perth?</h2>
      <p>High-voltage battery and electrical work requires EV-specific training. For routine maintenance (tyres, brakes, cabin filters, 12V battery), most qualified mechanics can perform the work. For high-voltage systems, seek a mechanic with certified EV training. Perth Mechanic can connect you with mechanics who work on EVs — specify your vehicle make and model when requesting a quote.</p>
      <h2>EV Servicing Costs in Perth</h2>
      <ul>
        <li>Annual inspection / service: $100–$250 (significantly less than petrol equivalents)</li>
        <li>Tyre set: similar to petrol car ($400–$1,200 depending on size)</li>
        <li>12V battery replacement: $150–$300</li>
        <li>Brake inspection: $80–$150</li>
      </ul>
"""
  },
  {
    "slug": "blog-emergency-mechanic-perth",
    "title": "Emergency Mechanic Perth: What To Do When Your Car Breaks Down",
    "h1": "Emergency Mechanic Perth: What To Do When Your Car Breaks Down",
    "tag": "Emergency",
    "meta": "Car broken down in Perth? What to do immediately, who to call, and how to get an emergency mechanic. Step-by-step guide for Perth drivers.",
    "read_time": 4,
    "excerpt": "Breaking down in Perth — especially in summer — is stressful. Here's the step-by-step guide to handling a breakdown safely and getting help fast.",
    "content": """
      <p>A breakdown is stressful at any time, but in Perth's summer heat or on a busy freeway, it can be dangerous. Here's exactly what to do, in order, when your car breaks down in Perth.</p>
      <h2>Step 1: Get Safely Off the Road</h2>
      <p>As soon as you notice a problem — warning light, loss of power, smoke, strange noise — begin moving toward the left-hand side of the road or the nearest safe stopping point. If on a freeway, use the emergency lane. Don't stop suddenly; indicate and move gradually to safety.</p>
      <h2>Step 2: Make Your Vehicle Visible</h2>
      <p>Once stopped in a safe location:</p>
      <ul>
        <li>Turn on your hazard lights immediately</li>
        <li>If you have safety triangles or a reflective vest, deploy them</li>
        <li>Stay in your vehicle with seatbelt on if on a freeway — it's safer than standing outside</li>
        <li>If stopped on a road with traffic, move behind the safety barrier if possible</li>
      </ul>
      <h2>Step 3: Assess and Don't Do These Things</h2>
      <ul>
        <li>Don't open the bonnet if you see or smell smoke — get well away from the vehicle first and call 000 if there's fire</li>
        <li>Don't attempt to top up coolant in an overheated vehicle — wait 30+ minutes</li>
        <li>Don't try to push-start a modern vehicle — it won't work and is dangerous in traffic</li>
        <li>Don't leave the vehicle without making it visible and securing it</li>
      </ul>
      <h2>Who to Call</h2>
      <p>If you have roadside assistance (RAC in WA, NRMA, RACQ, or similar through insurance), call them first — they handle many common breakdowns on the spot (flat battery, flat tyre). For breakdowns requiring a mechanic, Perth Mechanic can arrange same-day emergency mechanic attendance for urgent situations. Note "URGENT" in your request.</p>
      <h2>Common Roadside Breakdowns and What They Usually Are</h2>
      <ul>
        <li>Car won't start — flat battery (most common), starter motor, or fuel system</li>
        <li>Sudden power loss while driving — fuel, ignition, or transmission fault</li>
        <li>Overheating — coolant system issue</li>
        <li>Flat tyre — puncture or blowout</li>
        <li>Dashboard warning lights all illuminating — alternator failure (not charging battery)</li>
      </ul>
      <h2>After the Breakdown</h2>
      <p>Once you're safe and have arranged assistance, document what happened — what you noticed and when. This information helps the mechanic diagnose the fault faster and more accurately. Intermittent faults that disappear when cold or hot are notoriously difficult to diagnose without this context.</p>
"""
  },
  {
    "slug": "blog-mechanic-canning-vale",
    "title": "Mechanic in Canning Vale: Local Guide for Residents",
    "h1": "Mechanic in Canning Vale: Complete Local Guide for Residents",
    "tag": "Suburb",
    "meta": "Looking for a mechanic in Canning Vale? Local guide to car servicing in Canning Vale, typical costs, and how Perth Mechanic connects Canning Vale drivers with qualified mechanics.",
    "read_time": 4,
    "excerpt": "Canning Vale is one of Perth's largest southern suburbs with a busy mix of residential and industrial areas. Here's what Canning Vale residents need to know about local mechanic services.",
    "content": """
      <p>Canning Vale is one of Perth's most densely populated southern suburbs, with a large residential base in the City of Canning alongside significant industrial and commercial precincts. The suburb generates consistent demand for mechanical services from both private vehicles and the many business fleets operating from the local industrial areas.</p>
      <h2>Canning Vale's Vehicle Mix</h2>
      <p>The residential streets of Canning Vale are home to a broad cross-section of Perth families with typical family vehicles — SUVs, sedans, and hatchbacks of all brands. The industrial areas bring in utes and light commercial vehicles. Our Canning Vale mechanic network serves both populations.</p>
      <h2>Common Services in Canning Vale</h2>
      <ul>
        <li>Logbook services for new family vehicles on finance</li>
        <li>General servicing for the suburb's diverse vehicle age range</li>
        <li>Fleet servicing for local businesses</li>
        <li>Tyre fitting — high demand given the suburb's volume of newer vehicles</li>
        <li>Brake repairs — a consistent category across all suburbs</li>
      </ul>
      <h2>Typical Mechanic Costs in Canning Vale</h2>
      <ul>
        <li>Minor service: $160–$250</li>
        <li>Major service: $300–$560</li>
        <li>Logbook service: $190–$380</li>
        <li>Brake pad replacement: $190–$360</li>
        <li>Tyre fitting (per tyre, fitted): $130–$250</li>
      </ul>
      <h2>Perth Mechanic in Canning Vale</h2>
      <p>Perth Mechanic maintains a network of qualified mechanics in Canning Vale and surrounding southern suburbs including Willetton, Riverton, and Cannington. Submit a quote request and receive a response within 30 minutes. For fleet enquiries, note "FLEET" in your message for priority handling.</p>
"""
  },
  {
    "slug": "blog-mechanic-midland",
    "title": "Mechanic in Midland: Best Options for Eastern Corridor Drivers",
    "h1": "Mechanic in Midland: What Eastern Corridor Drivers Need to Know",
    "tag": "Suburb",
    "meta": "Looking for a mechanic in Midland? Guide to car servicing in Midland and the eastern Perth corridor — what to look for, typical costs, and local mechanic options.",
    "read_time": 4,
    "excerpt": "Midland is the hub of Perth's eastern corridor — a working suburb with a heavy concentration of utes, 4WDs, and fleet vehicles. Here's what Midland drivers need to know about local mechanics.",
    "content": """
      <p>Midland sits at the gateway to the Swan Valley and the broader eastern corridor, functioning as Perth's eastern commercial hub. With the Midland Health Campus, major shopping precinct, and easy access to the Great Eastern Highway, Midland generates significant demand for mechanic services from a practical, working-suburb demographic.</p>
      <h2>Midland's Vehicle Profile</h2>
      <p>Midland and the eastern corridor have a higher proportion of working vehicles than most Perth suburbs. Dual-cab utes, 4WDs, and vans are common alongside the standard family car mix. Mechanics in our Midland network are experienced with the full range — from a first-car Toyota Yaris to a fleet of tradie HiLuxes.</p>
      <h2>Why Midland Drivers Need a Good Mechanic</h2>
      <p>The eastern corridor includes some of Perth's highest-mileage vehicles. Tradies, delivery drivers, and people commuting long distances to work through Midland put serious kilometres on their vehicles. Proactive, scheduled servicing is especially important for high-use vehicles — deferred maintenance on a high-km ute can quickly become an expensive repair.</p>
      <h2>Common Services in Midland</h2>
      <ul>
        <li>Regular servicing for high-km vehicles</li>
        <li>4WD and ute specialisation</li>
        <li>Fleet servicing for local businesses</li>
        <li>Auto electrical — common issue for work vehicles with heavy electrical loads</li>
        <li>Pre-purchase inspections for the active used ute market</li>
      </ul>
      <h2>Typical Costs in Midland</h2>
      <ul>
        <li>Minor service: $150–$250</li>
        <li>Major service: $300–$560</li>
        <li>4WD service (including diff oil): $350–$600</li>
        <li>Pre-purchase inspection: $150–$250</li>
        <li>Auto electrical: $100–$300 for diagnosis and common repairs</li>
      </ul>
      <p>Perth Mechanic covers Midland and all eastern corridor suburbs. Submit a quote request for a fast response from our local mechanic network.</p>
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
    pub_date = "2026"
    pub_iso = "2026-01-01"

    header = HEADER_TPL.format(
        slug=slug, title=title, h1=h1, meta=meta,
        read_time=read_time, content=content,
        pub_date=pub_date, nav=NAV
    )
    footer = FOOTER_TPL.format(
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
    with open(filepath, "w", encoding="utf-8") as f:
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
with open(queue_path, "w", encoding="utf-8") as f:
    json.dump({"queue": queue}, f, indent=2)
print(f"\nCreated: {queue_path}")
print(f"\nDone. {len(ARTICLES)} drafts created.")
