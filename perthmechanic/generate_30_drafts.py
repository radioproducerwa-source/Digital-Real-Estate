#!/usr/bin/env python3
"""Generate 30 new draft blog posts for perthmechanic and append them to the queue."""

import json
import os

DRAFTS_DIR = os.path.join(os.path.dirname(__file__), "drafts")
QUEUE_FILE = os.path.join(DRAFTS_DIR, "queue.json")

# ---------------------------------------------------------------------------
# Post definitions: (slug, title, tag, read_time, excerpt, html_body)
# ---------------------------------------------------------------------------

POSTS = [
    # ── SUBURB PAGES ───────────────────────────────────────────────────────
    {
        "slug": "blog-mechanic-ellenbrook",
        "title": "Mechanic in Ellenbrook: North-East Perth Driver's Guide",
        "tag": "Suburbs",
        "read_time": 4,
        "excerpt": "Ellenbrook is one of Perth's fastest-growing northern suburbs, with thousands of family vehicles covering long commutes every day. Here's what Ellenbrook drivers need to know about car servicing.",
        "body": """
      <p>Ellenbrook sits roughly 27 km north-east of Perth's CBD and has grown rapidly into one of the city's largest outer suburban communities. Long daily commutes on the Great Northern Highway and Reid Highway put serious kilometres on local vehicles, making regular servicing essential.</p>

      <h2>Why Ellenbrook Drivers Need Reliable Mechanics</h2>
      <p>With limited public transport options, most Ellenbrook households run two or more cars. Breakdowns here are genuinely disruptive — the nearest major service hubs are Midland to the south or Joondalup to the west, both involving significant travel time. Having a trusted local mechanic or a quick-response service matters more here than in inner suburbs.</p>

      <h2>Common Vehicle Issues in Ellenbrook</h2>
      <ul>
        <li><strong>Tyre wear:</strong> High-speed freeway commuting accelerates tyre wear, especially on front-wheel-drive vehicles</li>
        <li><strong>Air conditioning:</strong> Perth's northern suburbs run hot — AC systems work overtime and need annual checks</li>
        <li><strong>Brake servicing:</strong> Stop-start school and commuter traffic increases brake pad wear</li>
        <li><strong>Logbook servicing:</strong> Newer Ellenbrook housing stock means many families are running vehicles still under manufacturer warranty</li>
      </ul>

      <h2>What to Expect From a Local Service</h2>
      <p>A standard logbook service in the Ellenbrook area typically costs between $180 and $350 depending on vehicle make, model, and oil type. Most Perth mechanics offer mobile servicing that reaches Ellenbrook, which is convenient if your car won't start or you can't get time off work.</p>

      <h2>How Perth Mechanic Helps Ellenbrook Drivers</h2>
      <p>Perth Mechanic connects Ellenbrook residents with qualified mechanics who service the Swan Valley and northern corridor. Whether you need a logbook service, brake inspection, or pre-purchase check, submit a quote request and we'll match you with a reliable local mechanic promptly.</p>

      <div style="text-align:center;margin:40px 0 16px;">
        <a href="contact.html" class="btn btn-primary btn-lg">Get a Free Mechanic Quote &rarr;</a>
      </div>
      <p style="text-align:center;color:var(--muted);font-size:0.9rem;">We respond within 30 minutes. All Perth suburbs covered.</p>
""",
    },
    {
        "slug": "blog-mechanic-claremont",
        "title": "Mechanic in Claremont: Western Suburbs Driver's Guide",
        "tag": "Suburbs",
        "read_time": 4,
        "excerpt": "Claremont is one of Perth's most established western suburbs, home to a mix of prestige vehicles and everyday family cars. Here's what Claremont drivers need to know about finding a reliable mechanic.",
        "body": """
      <p>Claremont occupies a prime position on the western suburbs strip, 11 km from the CBD along the Stirling Highway. It's an affluent and well-connected suburb with a high concentration of European marques, SUVs, and late-model vehicles — meaning mechanics here need to handle a wide range of sophisticated systems.</p>

      <h2>The Claremont Vehicle Mix</h2>
      <p>Claremont's demographics skew toward professionals and established families. Expect a high proportion of BMW, Mercedes-Benz, Audi, Volvo, and late-model Japanese SUVs. These vehicles often require specialist knowledge, particularly for:</p>
      <ul>
        <li>European-spec oils and fluids</li>
        <li>Dealer-level diagnostic software</li>
        <li>Timing chain inspections on German engines</li>
        <li>DSG and dual-clutch transmission services</li>
      </ul>

      <h2>Logbook Servicing Without the Dealer Price Tag</h2>
      <p>Many Claremont residents default to dealer servicing out of habit or warranty concern — but independent mechanics can legally perform logbook services that maintain manufacturer warranties under Australian Consumer Law. A non-dealer logbook service on a European vehicle in Perth typically costs 20–40% less than the dealership equivalent.</p>

      <h2>Parking and Access</h2>
      <p>Claremont's proximity to Cottesloe, Swanbourne, and Nedlands means mechanics covering the western suburbs zone can reach you quickly. Mobile mechanics are particularly popular here for minor services and tyre work.</p>

      <h2>Get a Quote for Claremont</h2>
      <p>Perth Mechanic works with mechanics experienced in European and prestige vehicles across the western suburbs corridor. Request a quote and specify your vehicle make and model for an accurate price.</p>

      <div style="text-align:center;margin:40px 0 16px;">
        <a href="contact.html" class="btn btn-primary btn-lg">Get a Free Mechanic Quote &rarr;</a>
      </div>
      <p style="text-align:center;color:var(--muted);font-size:0.9rem;">We respond within 30 minutes. All Perth suburbs covered.</p>
""",
    },
    {
        "slug": "blog-mechanic-kwinana",
        "title": "Mechanic in Kwinana: South Perth Industrial Corridor Guide",
        "tag": "Suburbs",
        "read_time": 4,
        "excerpt": "Kwinana is Perth's heavy industrial heartland, home to tradies, fleet operators, and working vehicles that need tough, reliable servicing. Here's what Kwinana drivers need to know.",
        "body": """
      <p>Kwinana sits 35 km south of Perth CBD and is WA's most concentrated industrial zone — refineries, freight depots, manufacturing plants, and heavy vehicle operations define the suburb. The vehicle mix here is distinctly working-class: utes, vans, 4WDs, diesel workhorses, and fleet vehicles that rack up serious kilometres.</p>

      <h2>What Kwinana Vehicles Need</h2>
      <p>Industrial and tradie use puts different demands on vehicles compared to suburban commuters:</p>
      <ul>
        <li><strong>Diesel servicing:</strong> DPF maintenance, injector cleaning, and diesel particulate filter issues are common in stop-start industrial driving</li>
        <li><strong>Heavy load wear:</strong> Suspension, brakes, and tyres wear faster when vehicles carry constant payloads</li>
        <li><strong>Fleet servicing:</strong> Many Kwinana employers run vehicle fleets that require scheduled group servicing</li>
        <li><strong>Air conditioning:</strong> Industrial environments and Perth heat make AC reliability critical for worker safety</li>
      </ul>

      <h2>Fleet and Commercial Servicing</h2>
      <p>Many mechanics serving Kwinana specialise in fleet and commercial work — they understand DPF cycles, can perform after-hours servicing to minimise downtime, and are experienced with Isuzu, Toyota HiLux, Ford Ranger, and Mercedes-Benz Sprinter platforms that dominate commercial fleets.</p>

      <h2>Proximity to Rockingham and Cockburn</h2>
      <p>Kwinana drivers have solid options nearby in Rockingham to the south and Cockburn Central to the north. Mobile mechanics also serve Kwinana regularly given the industrial nature of the area.</p>

      <h2>Get a Quote for Kwinana</h2>
      <p>Perth Mechanic connects Kwinana residents and fleet operators with mechanics experienced in commercial and heavy-use vehicles. Submit your details and vehicle type for a tailored quote.</p>

      <div style="text-align:center;margin:40px 0 16px;">
        <a href="contact.html" class="btn btn-primary btn-lg">Get a Free Mechanic Quote &rarr;</a>
      </div>
      <p style="text-align:center;color:var(--muted);font-size:0.9rem;">We respond within 30 minutes. All Perth suburbs covered.</p>
""",
    },
    {
        "slug": "blog-mechanic-welshpool",
        "title": "Mechanic in Welshpool: Perth's Industrial East Guide",
        "tag": "Suburbs",
        "read_time": 4,
        "excerpt": "Welshpool is one of Perth's major industrial and commercial hubs, with a high concentration of fleet vehicles and trade utes. Here's what Welshpool drivers and businesses need to know about local mechanic services.",
        "body": """
      <p>Welshpool lies 8 km south-east of Perth CBD and is one of the city's oldest and most established industrial zones. The suburb is dominated by warehousing, manufacturing, and automotive businesses — ironically making it one of Perth's best areas for mechanical services with dozens of workshops in the area.</p>

      <h2>Why Welshpool Has Strong Mechanic Options</h2>
      <p>Welshpool's zoning has attracted automotive businesses for decades. Trade workshops, panel beaters, tyre retailers, and parts suppliers are concentrated here, creating genuine competition that keeps prices reasonable and quality high. Industrial businesses that rely on vehicles as tools — not just transport — demand fast turnaround and competent work.</p>

      <h2>Vehicle Types Common in Welshpool</h2>
      <ul>
        <li>Heavy commercial vehicles and light trucks</li>
        <li>Trade utes (HiLux, Ranger, BT-50, Amarok)</li>
        <li>Diesel vans (Transit, Sprinter, Hiace)</li>
        <li>Forklifts and equipment (specialist servicing)</li>
        <li>Company cars and fleet sedans</li>
      </ul>

      <h2>After-Hours and Mobile Options</h2>
      <p>Given Welshpool's business concentration, many mechanics in the area offer after-hours and weekend slots to service vehicles without disrupting operations. Mobile mechanics can also reach Welshpool quickly from nearby Belmont and Cannington.</p>

      <h2>Residents Near Welshpool</h2>
      <p>Belmont, Carlisle, and St James residents often use Welshpool mechanics for their competitive pricing and wide service range — it's worth the short drive for complex or specialist work.</p>

      <div style="text-align:center;margin:40px 0 16px;">
        <a href="contact.html" class="btn btn-primary btn-lg">Get a Free Mechanic Quote &rarr;</a>
      </div>
      <p style="text-align:center;color:var(--muted);font-size:0.9rem;">We respond within 30 minutes. All Perth suburbs covered.</p>
""",
    },
    {
        "slug": "blog-mechanic-wangara",
        "title": "Mechanic in Wangara: North Perth Industrial Zone Guide",
        "tag": "Suburbs",
        "read_time": 4,
        "excerpt": "Wangara is Perth's major northern industrial suburb with a large cluster of automotive workshops. Here's what Wangara and northern corridor drivers need to know about car servicing in the area.",
        "body": """
      <p>Wangara is located 22 km north of Perth CBD and functions as the northern counterpart to Welshpool — a major industrial and commercial hub with a dense cluster of automotive businesses, mechanics, and vehicle service providers along Wanneroo Road and nearby streets.</p>

      <h2>An Established Automotive Hub</h2>
      <p>Wangara's industrial zoning has made it a natural home for automotive businesses. The area features a range of mechanics from small independent workshops to larger multi-bay operations, plus major tyre retailers, parts suppliers, and specialist shops. This concentration drives competitive pricing and broad service availability.</p>

      <h2>Who Uses Wangara Mechanics</h2>
      <ul>
        <li>Residents from Wangara, Landsdale, Darch, and Madeley</li>
        <li>Businesses running northern Perth fleets</li>
        <li>Drivers from Wanneroo and Two Rocks who travel south for specialist work</li>
        <li>Trades businesses using the area as a base</li>
      </ul>

      <h2>Services Readily Available in Wangara</h2>
      <p>Thanks to the concentration of workshops, Wangara can handle almost any automotive task: logbook services, major repairs, diesel servicing, 4WD fitments, tyres, wheel alignments, and auto electrical work. Wait times are generally shorter here than in more residential suburbs because there's more competition for business.</p>

      <h2>Getting to Wangara</h2>
      <p>Wangara is accessible from the Mitchell Freeway via Hepburn Avenue or Gnangara Road. Drop-off and collection services are common given the suburb's industrial layout — most customers leave their car and get picked up or use rideshare.</p>

      <div style="text-align:center;margin:40px 0 16px;">
        <a href="contact.html" class="btn btn-primary btn-lg">Get a Free Mechanic Quote &rarr;</a>
      </div>
      <p style="text-align:center;color:var(--muted);font-size:0.9rem;">We respond within 30 minutes. All Perth suburbs covered.</p>
""",
    },
    {
        "slug": "blog-mechanic-bibra-lake",
        "title": "Mechanic in Bibra Lake: South Perth Driver's Guide",
        "tag": "Suburbs",
        "read_time": 4,
        "excerpt": "Bibra Lake is a key southern industrial and residential suburb with good access to mechanics serving Cockburn, Jandakot, and the surrounding area. Here's what local drivers need to know.",
        "body": """
      <p>Bibra Lake sits in Perth's southern corridor, roughly 20 km from the CBD near the Cockburn Central commercial hub. It's a mixed-use suburb with residential pockets surrounded by industrial and commercial estates, including automotive workshops that serve drivers across the Cockburn, Jandakot, and Yangebup areas.</p>

      <h2>Bibra Lake's Location Advantage</h2>
      <p>The suburb's proximity to Cockburn Central and access from Cockburn Road and Bibra Drive puts multiple automotive businesses within easy reach. Drivers from Yangebup, Aubin Grove, Atwell, and Banjup regularly use Bibra Lake mechanics as their closest convenient option.</p>

      <h2>Typical Service Needs in the Area</h2>
      <ul>
        <li><strong>SUV and 4WD servicing:</strong> The southern corridor's family-focused demographics mean a high proportion of SUVs</li>
        <li><strong>Logbook servicing:</strong> Many Bibra Lake residents drive newer vehicles still under manufacturer warranty</li>
        <li><strong>Air conditioning:</strong> Perth's southern suburbs get hot in summer — AC servicing is in constant demand</li>
        <li><strong>Tyre and wheel services:</strong> High freeway usage on Kwinana Freeway and Stock Road accelerates tyre wear</li>
      </ul>

      <h2>Fleet and Commercial</h2>
      <p>Bibra Lake's industrial estates house businesses that run light commercial vehicles. Mechanics in the area are accustomed to small fleet jobs and can schedule servicing to minimise business downtime.</p>

      <h2>Perth Mechanic in Bibra Lake</h2>
      <p>Perth Mechanic can connect Bibra Lake drivers with reliable mechanics in the Cockburn and southern corridor zone. Submit a quote request with your postcode and vehicle details for a fast response.</p>

      <div style="text-align:center;margin:40px 0 16px;">
        <a href="contact.html" class="btn btn-primary btn-lg">Get a Free Mechanic Quote &rarr;</a>
      </div>
      <p style="text-align:center;color:var(--muted);font-size:0.9rem;">We respond within 30 minutes. All Perth suburbs covered.</p>
""",
    },
    {
        "slug": "blog-mechanic-duncraig",
        "title": "Mechanic in Duncraig: North Coastal Perth Driver's Guide",
        "tag": "Suburbs",
        "read_time": 4,
        "excerpt": "Duncraig is a quiet, established northern suburb between Joondalup and Karrinyup. Here's what Duncraig residents need to know about finding a reliable local mechanic.",
        "body": """
      <p>Duncraig is a well-established residential suburb approximately 18 km north of Perth CBD, positioned between the Karrinyup corridor to the south and Joondalup to the north. It's a predominantly family suburb with a mature housing stock and a vehicle mix weighted toward practical family cars and SUVs.</p>

      <h2>Duncraig's Vehicle Profile</h2>
      <p>Duncraig households tend to run reliable, mid-market vehicles — Toyota RAV4, Mazda CX-5, Honda CR-V, and Hyundai Tucson are common. The suburb's demographics lean toward families and retirees who prioritise reliability and fair pricing over performance or prestige.</p>

      <h2>Where Duncraig Residents Service Their Cars</h2>
      <p>Duncraig doesn't have a major commercial strip with workshops, so most residents travel to:</p>
      <ul>
        <li><strong>Karrinyup / Carine:</strong> 5–10 minutes south, with a solid concentration of workshops</li>
        <li><strong>Joondalup:</strong> 10 minutes north, Perth's northern commercial hub with excellent mechanic options</li>
        <li><strong>Stirling / Osborne Park:</strong> 15 minutes south via Mitchell Freeway for specialist work</li>
      </ul>

      <h2>Mobile Mechanics in Duncraig</h2>
      <p>Mobile mechanics are popular in Duncraig for routine servicing — they can perform logbook services, oil changes, brake pad replacements, and battery swaps in your driveway or street, saving the trip to a workshop. For major repairs, dropping the car at a nearby workshop is the better option.</p>

      <h2>Annual Servicing Costs</h2>
      <p>Standard logbook service for a Japanese or Korean SUV in the Duncraig area: $180–$320. European vehicles: $280–$500. Mobile call-out fee adds approximately $30–$60 to these figures.</p>

      <div style="text-align:center;margin:40px 0 16px;">
        <a href="contact.html" class="btn btn-primary btn-lg">Get a Free Mechanic Quote &rarr;</a>
      </div>
      <p style="text-align:center;color:var(--muted);font-size:0.9rem;">We respond within 30 minutes. All Perth suburbs covered.</p>
""",
    },
    {
        "slug": "blog-mechanic-kingsley",
        "title": "Mechanic in Kingsley: North Perth Suburban Driver's Guide",
        "tag": "Suburbs",
        "read_time": 4,
        "excerpt": "Kingsley is a well-established northern suburb with easy access to mechanics along the Mitchell Freeway corridor. Here's what Kingsley residents need to know about local car servicing.",
        "body": """
      <p>Kingsley is located approximately 20 km north of Perth CBD, east of Duncraig and west of Warwick. It's a largely residential suburb with good freeway access to both Joondalup and the Perth CBD, making it well-positioned for drivers who commute long distances each week.</p>

      <h2>Vehicle Mix in Kingsley</h2>
      <p>Kingsley's mix of families, tradies, and commuters creates diverse servicing demands. You'll see everything from family station wagons and SUVs to dual-cab utes and older model sedans. The suburb's affordability relative to coastal suburbs like Duncraig and Carine means a slightly older average vehicle age.</p>

      <h2>Finding a Mechanic Near Kingsley</h2>
      <p>The closest commercial areas with mechanic concentrations are:</p>
      <ul>
        <li><strong>Warwick:</strong> Immediately east, with several workshops along Beach Road</li>
        <li><strong>Greenwood/Padbury:</strong> A short drive with independent mechanics</li>
        <li><strong>Joondalup:</strong> 15 minutes north for dealers and major chains</li>
        <li><strong>Osborne Park:</strong> 20 minutes south for specialist and prestige work</li>
      </ul>

      <h2>Logbook Servicing and Warranty</h2>
      <p>Independent mechanics in the Kingsley area can perform logbook services that maintain your vehicle's manufacturer warranty — they must use correct oils, filters, and record the service in your log book. This is worth understanding because dealer servicing can cost significantly more for identical work.</p>

      <h2>Get a Quote in Kingsley</h2>
      <p>Perth Mechanic matches Kingsley drivers with qualified mechanics in the northern suburbs. Fill in your details and we'll connect you with a mechanic who covers your area at a fair price.</p>

      <div style="text-align:center;margin:40px 0 16px;">
        <a href="contact.html" class="btn btn-primary btn-lg">Get a Free Mechanic Quote &rarr;</a>
      </div>
      <p style="text-align:center;color:var(--muted);font-size:0.9rem;">We respond within 30 minutes. All Perth suburbs covered.</p>
""",
    },
    {
        "slug": "blog-mechanic-east-perth",
        "title": "Mechanic in East Perth: Inner City Driver's Guide",
        "tag": "Suburbs",
        "read_time": 4,
        "excerpt": "East Perth is one of Perth's most densely populated inner suburbs, home to apartment dwellers, professionals, and a mix of city cars and commuter vehicles. Here's what East Perth residents need to know about car servicing.",
        "body": """
      <p>East Perth sits immediately east of the CBD on the Swan River foreshore — a high-density inner suburb of apartments, townhouses, and professional residences. Parking is tight, public transport is excellent, and many East Perth residents keep a car purely for weekend and regional travel.</p>

      <h2>Car Ownership in East Perth</h2>
      <p>East Perth's car ownership rates are lower than outer suburbs, but vehicles here tend to be:</p>
      <ul>
        <li>Late-model hatchbacks and small SUVs (low kilometres, infrequent servicing)</li>
        <li>Performance and prestige vehicles (high-end residents near the foreshore)</li>
        <li>Older city runarounds (students, young professionals)</li>
      </ul>
      <p>The challenge for East Perth drivers is that there are few mechanics within walking distance — it's an inner residential zone, not a commercial strip.</p>

      <h2>Best Options for East Perth Drivers</h2>
      <p>East Perth drivers have several good options:</p>
      <ul>
        <li><strong>Vic Park / Burswood:</strong> 5 minutes east, with a number of independent workshops</li>
        <li><strong>Belmont:</strong> 10 minutes for a wider range including tyre and wheel shops</li>
        <li><strong>Welshpool:</strong> 15 minutes for specialist and heavy repair work</li>
        <li><strong>Mobile mechanics:</strong> The most practical option for East Perth apartment dwellers — they come to you in your building's car park or on-street</li>
      </ul>

      <h2>Mobile Servicing in Apartments</h2>
      <p>Mobile mechanics can perform most logbook services in a basement car park — they bring their own lighting, drainage mats, and equipment. Building management permission is usually required; most mechanics will confirm what they need when booking.</p>

      <div style="text-align:center;margin:40px 0 16px;">
        <a href="contact.html" class="btn btn-primary btn-lg">Get a Free Mechanic Quote &rarr;</a>
      </div>
      <p style="text-align:center;color:var(--muted);font-size:0.9rem;">We respond within 30 minutes. All Perth suburbs covered.</p>
""",
    },
    {
        "slug": "blog-mechanic-leederville",
        "title": "Mechanic in Leederville: Inner North Perth Driver's Guide",
        "tag": "Suburbs",
        "read_time": 4,
        "excerpt": "Leederville is a vibrant inner-north suburb with a mix of young professionals, established residents, and a strong café culture. Here's what Leederville drivers need to know about local car servicing.",
        "body": """
      <p>Leederville is one of Perth's most desirable inner-north suburbs, just 3 km from the CBD with excellent café strips, arts venues, and transport links. Like many inner Perth suburbs, it has limited local mechanic presence but excellent access to nearby service hubs.</p>

      <h2>Leederville's Vehicle Profile</h2>
      <p>Leederville residents tend to run smaller, newer vehicles suited to inner-city parking and driving. Hatchbacks, small SUVs, and older European cars are common. The demographics — young professionals, creatives, small families — mean vehicles often accumulate fewer kilometres but still need regular servicing to maintain warranty and reliability.</p>

      <h2>Where to Get Your Car Serviced Near Leederville</h2>
      <ul>
        <li><strong>Osborne Park:</strong> 5 minutes north via Main Street — Perth's premier auto service suburb with dozens of workshops</li>
        <li><strong>Northbridge / Perth CBD fringe:</strong> Several workshops on the inner city edge</li>
        <li><strong>Wembley:</strong> A short drive west with solid suburban mechanic options</li>
        <li><strong>Mobile mechanics:</strong> Popular for Leederville's tight streets — park in your driveway or terrace house forecourt</li>
      </ul>

      <h2>Osborne Park: The Natural Choice</h2>
      <p>Most Leederville drivers use Osborne Park mechanics. The suburb's Mitchell Freeway access and concentration of automotive businesses make it Perth's most convenient service hub for inner-north residents. Prices are competitive and specialist expertise (European, prestige, performance) is readily available.</p>

      <h2>Annual Servicing Costs</h2>
      <p>Small hatchback logbook service: $150–$280. Medium SUV: $200–$350. Drop your car at an Osborne Park workshop before work, catch public transport into the CBD, and collect on the way home.</p>

      <div style="text-align:center;margin:40px 0 16px;">
        <a href="contact.html" class="btn btn-primary btn-lg">Get a Free Mechanic Quote &rarr;</a>
      </div>
      <p style="text-align:center;color:var(--muted);font-size:0.9rem;">We respond within 30 minutes. All Perth suburbs covered.</p>
""",
    },

    # ── TECHNICAL / MAINTENANCE TOPICS ────────────────────────────────────
    {
        "slug": "blog-tyre-rotation-perth",
        "title": "Tyre Rotation Perth: Why It Matters and How Often to Do It",
        "tag": "Maintenance",
        "read_time": 4,
        "excerpt": "Tyre rotation is one of the cheapest maintenance tasks Perth drivers skip — and one of the most worthwhile. Here's why rotation matters, how often to do it, and what it costs.",
        "body": """
      <p>Tyre rotation is the process of moving tyres between positions on your vehicle — front to rear, side to side, or in a cross pattern — to equalise wear across all four tyres. It's inexpensive, quick, and genuinely extends tyre life, yet it's one of the most commonly skipped maintenance items in Perth.</p>

      <h2>Why Tyres Wear Unevenly</h2>
      <p>Front and rear tyres carry different loads and perform different jobs:</p>
      <ul>
        <li><strong>Front tyres</strong> handle steering and braking forces, causing faster shoulder wear — especially on front-wheel-drive cars where they also drive the vehicle</li>
        <li><strong>Rear tyres</strong> on FWD vehicles carry less load and wear more slowly</li>
        <li><strong>RWD vehicles</strong> wear rear tyres faster under acceleration</li>
        <li><strong>AWD vehicles</strong> require precise rotation to avoid drivetrain strain from mismatched tread depths</li>
      </ul>

      <h2>How Often Should Perth Drivers Rotate Their Tyres?</h2>
      <p>The standard recommendation is every 8,000–10,000 km or at every second oil change. For Perth drivers who cover 15,000–20,000 km per year on a mix of freeway and suburban roads, that translates to approximately twice a year.</p>

      <h2>Signs You've Left It Too Long</h2>
      <ul>
        <li>Noticeable difference in tread depth between front and rear tyres</li>
        <li>Vibration or rumbling at highway speeds</li>
        <li>Uneven wear patterns visible on the tyre shoulder</li>
      </ul>

      <h2>Cost of Tyre Rotation in Perth</h2>
      <p>A four-tyre rotation typically costs $30–$60 at most Perth workshops. Many mechanics include it free with a logbook service. Given that rotation can add 20,000–30,000 km to a set of tyres, it's one of the best value maintenance items available.</p>

      <div style="text-align:center;margin:40px 0 16px;">
        <a href="contact.html" class="btn btn-primary btn-lg">Get a Free Mechanic Quote &rarr;</a>
      </div>
      <p style="text-align:center;color:var(--muted);font-size:0.9rem;">We respond within 30 minutes. All Perth suburbs covered.</p>
""",
    },
    {
        "slug": "blog-wheel-alignment-perth",
        "title": "Wheel Alignment Perth: Signs You Need One and What It Costs",
        "tag": "Maintenance",
        "read_time": 5,
        "excerpt": "Misaligned wheels cost you money every day in extra tyre wear and fuel consumption. Here's how to spot the signs, what causes misalignment, and what wheel alignment costs in Perth.",
        "body": """
      <p>Wheel alignment refers to the angle and direction your wheels point relative to each other and the road. When alignment is off — even slightly — your tyres scrub against the road rather than rolling cleanly. The result: accelerated tyre wear, pulling to one side, and worse fuel economy. Perth's road quality, with its mix of freeway expansion joints and suburban kerb strikes, makes regular alignment checks worthwhile.</p>

      <h2>Signs Your Wheels Need Aligning</h2>
      <ul>
        <li>Car pulls left or right when you let go of the steering wheel on a flat road</li>
        <li>Steering wheel sits off-centre when driving straight</li>
        <li>Tyres wearing unevenly — especially on one edge</li>
        <li>Vibration through the steering wheel</li>
        <li>After hitting a kerb or pothole hard</li>
      </ul>

      <h2>What Causes Misalignment?</h2>
      <p>Alignment shifts gradually through normal driving, but is accelerated by:</p>
      <ul>
        <li>Hitting kerbs (common in tight Perth car parks)</li>
        <li>Driving through potholes at speed</li>
        <li>Worn suspension or steering components</li>
        <li>Tyre changes that weren't followed by an alignment check</li>
      </ul>

      <h2>Types of Alignment</h2>
      <p>Most modern vehicles need a four-wheel alignment, which adjusts camber, caster, and toe on all four corners. Older vehicles with rigid rear axles may only need a front-end alignment. Four-wheel is the standard and gives the most complete result.</p>

      <h2>Wheel Alignment Costs in Perth</h2>
      <ul>
        <li>Front-wheel alignment: $60–$90</li>
        <li>Four-wheel alignment: $90–$150</li>
        <li>After suspension work or new tyres: always get a four-wheel alignment</li>
      </ul>
      <p>When you replace tyres, always request an alignment check — fitting new tyres without aligning them is one of the easiest ways to waste money in car ownership.</p>

      <div style="text-align:center;margin:40px 0 16px;">
        <a href="contact.html" class="btn btn-primary btn-lg">Get a Free Mechanic Quote &rarr;</a>
      </div>
      <p style="text-align:center;color:var(--muted);font-size:0.9rem;">We respond within 30 minutes. All Perth suburbs covered.</p>
""",
    },
    {
        "slug": "blog-brake-fluid-flush-perth",
        "title": "Brake Fluid Flush Perth: What It Is and Why It Matters",
        "tag": "Maintenance",
        "read_time": 4,
        "excerpt": "Brake fluid is hygroscopic — it absorbs moisture from the air over time, lowering its boiling point and compromising your braking. Here's when Perth drivers need a brake fluid flush and what it costs.",
        "body": """
      <p>Brake fluid is the hydraulic medium that transfers pressure from your brake pedal to your brake callipers. It operates under high heat and pressure — and unlike engine oil, most drivers never think about it until something goes wrong. In Perth's heat, degraded brake fluid is a genuine safety concern.</p>

      <h2>Why Brake Fluid Degrades</h2>
      <p>Brake fluid is hygroscopic — it actively absorbs moisture from the air through microscopic pathways in your brake lines and master cylinder. As moisture accumulates:</p>
      <ul>
        <li>The boiling point drops (fresh DOT4 boils at 230°C; used fluid can drop to below 150°C)</li>
        <li>Under heavy braking — descending hills, emergency stops — overheated fluid can vaporise, creating gas bubbles that compress rather than transmit pressure</li>
        <li>This is called "brake fade" or "vapour lock" and can cause a sudden loss of braking effectiveness</li>
      </ul>

      <h2>How Often to Flush Brake Fluid</h2>
      <p>Most manufacturers recommend every 2 years regardless of mileage. Perth's high temperatures accelerate fluid degradation, so some mechanics recommend every 18 months for vehicles driven hard or in hilly areas. A simple test strip (available at most workshops) can check moisture content in minutes.</p>

      <h2>Signs Your Brake Fluid Needs Changing</h2>
      <ul>
        <li>Fluid appears dark brown or black (fresh fluid is pale yellow)</li>
        <li>Soft or spongy brake pedal</li>
        <li>Longer stopping distances than usual</li>
        <li>It's been more than 2 years since the last flush</li>
      </ul>

      <h2>Cost of a Brake Fluid Flush in Perth</h2>
      <p>A brake fluid flush (including bleeding all four wheels) typically costs $80–$150 in Perth. It takes approximately 45 minutes at most workshops and is often bundled with a major logbook service.</p>

      <div style="text-align:center;margin:40px 0 16px;">
        <a href="contact.html" class="btn btn-primary btn-lg">Get a Free Mechanic Quote &rarr;</a>
      </div>
      <p style="text-align:center;color:var(--muted);font-size:0.9rem;">We respond within 30 minutes. All Perth suburbs covered.</p>
""",
    },
    {
        "slug": "blog-cabin-air-filter-perth",
        "title": "Cabin Air Filter Perth: When to Replace It and Why It Matters",
        "tag": "Maintenance",
        "read_time": 4,
        "excerpt": "Your cabin air filter cleans the air coming through your car's vents. In Perth's dusty conditions, it clogs faster than the service interval suggests. Here's what you need to know.",
        "body": """
      <p>The cabin air filter (also called the pollen filter or microfilter) sits behind your glovebox or under the dashboard and cleans all air that enters your car through the heating and air conditioning system. It traps dust, pollen, insects, and particulates before they reach the cabin. In Perth — with its combination of dust, pollen seasons, and long dry summers — it's one of the most important filters to maintain.</p>

      <h2>How Often to Replace the Cabin Air Filter</h2>
      <p>Manufacturer recommendations typically say every 15,000–25,000 km or once a year. But in Perth's conditions:</p>
      <ul>
        <li>Summer dust storms (especially in eastern and northern suburbs) can clog a filter in weeks</li>
        <li>Spring pollen loads are exceptionally high in the Swan Valley and Hills</li>
        <li>Construction sites and unsealed roads add grit load quickly</li>
      </ul>
      <p>The practical recommendation for Perth: inspect it every 10,000 km and replace when visibly grey or clogged.</p>

      <h2>Signs Your Cabin Filter Needs Replacing</h2>
      <ul>
        <li>Reduced airflow from vents even at maximum fan speed</li>
        <li>Musty or stale smell when the aircon is running</li>
        <li>Increased dust accumulation on your dashboard</li>
        <li>Allergy symptoms in the car that don't occur outside</li>
      </ul>

      <h2>Cost of Replacement in Perth</h2>
      <p>A cabin air filter itself costs $20–$60 depending on vehicle. Workshop labour to fit it is $20–$40 (many are accessible in minutes). Total: $40–$100. This is also a DIY job on most vehicles — YouTube the procedure for your specific car. Most filters slot in without tools.</p>

      <h2>HEPA and Carbon Filters</h2>
      <p>Upgraded HEPA or activated carbon filters are available for most common vehicles and cost $40–$80. They provide better particle filtration and can absorb exhaust odours — worth considering if you or a passenger have respiratory conditions.</p>

      <div style="text-align:center;margin:40px 0 16px;">
        <a href="contact.html" class="btn btn-primary btn-lg">Get a Free Mechanic Quote &rarr;</a>
      </div>
      <p style="text-align:center;color:var(--muted);font-size:0.9rem;">We respond within 30 minutes. All Perth suburbs covered.</p>
""",
    },
    {
        "slug": "blog-headlight-restoration-perth",
        "title": "Headlight Restoration Perth: Fix Yellowed, Cloudy Headlights",
        "tag": "Maintenance",
        "read_time": 4,
        "excerpt": "Perth's UV intensity turns clear polycarbonate headlights yellow and cloudy within years. Here's what headlight restoration involves, whether it's worth it, and what it costs compared to replacement.",
        "body": """
      <p>If your car is more than four years old and sits outside regularly, there's a good chance your headlight lenses have yellowed or developed a cloudy, hazy appearance. This is UV oxidation — Perth's intense UV index is among the highest in Australia, and it breaks down the protective coating on polycarbonate headlight lenses faster than almost anywhere else in the country.</p>

      <h2>Why Yellowed Headlights Are a Safety Issue</h2>
      <p>It's not just cosmetic. Severely oxidised headlights can reduce light output by up to 80% compared to new lenses. At night on dark suburban roads or highways, that's a significant safety reduction. In WA, severely degraded lights can also result in a defect notice at inspection time.</p>

      <h2>What Headlight Restoration Involves</h2>
      <p>Professional headlight restoration involves:</p>
      <ol>
        <li>Wet sanding with progressive grits to remove the oxidised layer</li>
        <li>Machine polishing to restore clarity</li>
        <li>Application of a UV-protective sealant or coating</li>
      </ol>
      <p>A good restoration should restore 80–95% of original clarity and last 1–3 years depending on whether the vehicle is garaged and the quality of the sealant used.</p>

      <h2>Restoration vs Replacement</h2>
      <ul>
        <li><strong>Restoration:</strong> $80–$150 per pair professionally, $20–$40 DIY with a kit</li>
        <li><strong>OEM headlight replacement:</strong> $200–$800+ per side depending on vehicle</li>
        <li><strong>Aftermarket replacement:</strong> $80–$300 per side</li>
      </ul>
      <p>For most vehicles, restoration makes financial sense. Exception: if the lenses are cracked, chipped, or the yellowing has penetrated into the lens (not just the surface coating), replacement is the better option.</p>

      <h2>DIY or Workshop?</h2>
      <p>Headlight restoration kits ($20–$50 from Repco or Supercheap) give reasonable results if done carefully. For better results that last longer, a professional mobile detailer or mechanic's $80–$150 job is worth it.</p>

      <div style="text-align:center;margin:40px 0 16px;">
        <a href="contact.html" class="btn btn-primary btn-lg">Get a Free Mechanic Quote &rarr;</a>
      </div>
      <p style="text-align:center;color:var(--muted);font-size:0.9rem;">We respond within 30 minutes. All Perth suburbs covered.</p>
""",
    },
    {
        "slug": "blog-windscreen-chip-repair-perth",
        "title": "Windscreen Chip Repair Perth: Fix It Before It Spreads",
        "tag": "Repairs",
        "read_time": 4,
        "excerpt": "A small chip in your windscreen can spread into a full crack within days in Perth's heat. Here's when repair is possible, when replacement is necessary, and how insurance covers it.",
        "body": """
      <p>Perth's freeways — particularly the Mitchell and Kwinana — generate significant stone chip damage. Gravel from roadworks, aggregate on freshly sealed surfaces, and trucks carrying loose loads are constant chip hazards. The good news: a chip caught early can almost always be repaired for a fraction of replacement cost.</p>

      <h2>When Can a Chip Be Repaired?</h2>
      <p>Windscreen repair works by injecting a clear resin into the damaged area under vacuum, then curing it with UV light. The result is structural and optical — the crack is stabilised and barely visible. Repair is possible when:</p>
      <ul>
        <li>The chip is smaller than a 10-cent coin (approximately 25mm)</li>
        <li>The damage is not in the driver's direct line of sight (some repairers will still fix it, check RMS guidelines)</li>
        <li>The chip is not a "star break" that extends to the outer edge of the glass</li>
        <li>There is only one layer of damage (not through the inner laminate)</li>
      </ul>

      <h2>When Replacement Is Required</h2>
      <ul>
        <li>Cracks longer than 30cm</li>
        <li>Chips in the driver's primary vision zone</li>
        <li>Damage that has spread to the windscreen edge</li>
        <li>Any damage on the inner surface of the glass</li>
      </ul>

      <h2>Heat Makes Chips Spread Fast</h2>
      <p>In summer, a chip can spread overnight as the windscreen expands and contracts. Air conditioning blasting cold air onto a hot windscreen accelerates this. If you have a chip, avoid directing AC vents at it and get it assessed within days.</p>

      <h2>Cost and Insurance</h2>
      <ul>
        <li>Chip repair: $50–$100</li>
        <li>Full windscreen replacement: $250–$800+ depending on vehicle and whether ADAS recalibration is needed</li>
        <li>Comprehensive insurance: Most policies cover chip repair at zero excess — check your policy before paying out of pocket</li>
      </ul>

      <div style="text-align:center;margin:40px 0 16px;">
        <a href="contact.html" class="btn btn-primary btn-lg">Get a Free Mechanic Quote &rarr;</a>
      </div>
      <p style="text-align:center;color:var(--muted);font-size:0.9rem;">We respond within 30 minutes. All Perth suburbs covered.</p>
""",
    },
    {
        "slug": "blog-hybrid-car-servicing-perth",
        "title": "Hybrid Car Servicing Perth: What's Different From a Petrol Service",
        "tag": "Maintenance",
        "read_time": 5,
        "excerpt": "Hybrid vehicles are becoming common on Perth roads. Their servicing needs differ from pure petrol vehicles in important ways — here's what Perth hybrid owners need to know.",
        "body": """
      <p>Hybrid vehicles — led by the Toyota Corolla Hybrid, RAV4 Hybrid, Kluger Hybrid, and Lexus range — have become a fixture on Perth's roads over the past decade. They offer real-world fuel savings on Perth's suburban mix of stop-start and freeway driving, but their servicing requirements differ from conventional petrol vehicles in ways many owners don't anticipate.</p>

      <h2>What Hybrids Share With Petrol Cars</h2>
      <p>Hybrid vehicles still have a combustion engine that requires:</p>
      <ul>
        <li>Engine oil and filter changes (same intervals as petrol equivalents)</li>
        <li>Air filter replacement</li>
        <li>Spark plug replacement (less frequent than non-hybrid — iridium plugs last 100,000km+)</li>
        <li>Coolant flushes</li>
        <li>Transmission fluid (for CVT or automatic transmissions)</li>
      </ul>

      <h2>What's Different on a Hybrid</h2>
      <ul>
        <li><strong>Brakes last much longer:</strong> Regenerative braking does most of the work — brake pads and discs often last 100,000km+ on Toyotas. However, because they're used less, they can corrode and seize — a workshop inspection is still needed annually</li>
        <li><strong>HV battery maintenance:</strong> The high-voltage battery typically carries an 8–10 year/160,000km warranty. It doesn't require regular servicing, but a health check at high mileage is worthwhile</li>
        <li><strong>12V auxiliary battery:</strong> Often smaller than a petrol car equivalent, it can fail without warning and leave the hybrid unable to start. Replacement cost: $150–$250</li>
        <li><strong>Air conditioning:</strong> Hybrids use electric-drive air conditioning compressors that require specific hybrid-compatible refrigerant and oil — not all workshops carry it</li>
      </ul>

      <h2>Finding a Hybrid-Competent Mechanic in Perth</h2>
      <p>Most Toyota dealers and many independent mechanics now have hybrid training. When booking, specify your vehicle is a hybrid so they can confirm their competence with HV systems and have the right fluids on hand.</p>

      <h2>Cost Comparison</h2>
      <p>Hybrid logbook service costs are similar to petrol equivalents — approximately $200–$380 for a Toyota RAV4 Hybrid. Savings come from extended brake service intervals, not reduced oil change frequency.</p>

      <div style="text-align:center;margin:40px 0 16px;">
        <a href="contact.html" class="btn btn-primary btn-lg">Get a Free Mechanic Quote &rarr;</a>
      </div>
      <p style="text-align:center;color:var(--muted);font-size:0.9rem;">We respond within 30 minutes. All Perth suburbs covered.</p>
""",
    },
    {
        "slug": "blog-catalytic-converter-perth",
        "title": "Catalytic Converter Perth: Problems, Theft, and Replacement Costs",
        "tag": "Repairs",
        "read_time": 5,
        "excerpt": "Catalytic converters are a key emissions component — and a theft target. Here's what Perth drivers need to know about cat converter problems, signs of failure, and what replacement costs.",
        "body": """
      <p>The catalytic converter sits in your exhaust system and converts harmful combustion gases (hydrocarbons, carbon monoxide, nitrogen oxides) into less harmful emissions. It's a legally required emissions component in Australia, and a failing cat can cause a vehicle to fail its emissions test, trigger a check engine light, and reduce performance significantly.</p>

      <h2>Signs of a Failing Catalytic Converter</h2>
      <ul>
        <li>Check engine light on (P0420 or similar codes)</li>
        <li>Rotten egg smell from the exhaust (sulphur, indicating incomplete conversion)</li>
        <li>Reduced engine performance or acceleration</li>
        <li>Engine running rich (excessive fuel smell)</li>
        <li>Rattling noise from under the vehicle (internal substrate breakdown)</li>
        <li>Excessive heat under the car</li>
      </ul>

      <h2>What Causes Catalytic Converter Failure?</h2>
      <ul>
        <li><strong>Engine misfires:</strong> Unburnt fuel entering the cat causes it to overheat and melt the internal substrate — the most common cause of cat failure</li>
        <li><strong>Oil or coolant burning:</strong> Internal engine leaks contaminate the substrate</li>
        <li><strong>Physical damage:</strong> Road debris, speed bumps, or accident damage</li>
        <li><strong>Old age:</strong> Most cats last 160,000–200,000 km under normal conditions</li>
      </ul>

      <h2>Catalytic Converter Theft in Perth</h2>
      <p>Cat theft has become a significant problem across Australia, including Perth. Hybrid vehicles (particularly Toyota Prius and RAV4 Hybrid) are targeted because their cats contain higher concentrations of precious metals (platinum, palladium, rhodium) that retain value during cold starts. Theft takes under two minutes with an angle grinder. Prevention options include anti-theft plates and cages available from specialist suppliers.</p>

      <h2>Replacement Costs in Perth</h2>
      <ul>
        <li>Standard petrol sedan: $500–$1,200 fitted</li>
        <li>Diesel vehicles (DPF): $1,500–$3,500+</li>
        <li>Hybrid vehicles: $1,500–$4,000+ (higher precious metal content)</li>
        <li>Aftermarket cats are legal in WA if ADR-compliant; OEM replacements cost more but last longer</li>
      </ul>

      <div style="text-align:center;margin:40px 0 16px;">
        <a href="contact.html" class="btn btn-primary btn-lg">Get a Free Mechanic Quote &rarr;</a>
      </div>
      <p style="text-align:center;color:var(--muted);font-size:0.9rem;">We respond within 30 minutes. All Perth suburbs covered.</p>
""",
    },
    {
        "slug": "blog-rust-treatment-perth",
        "title": "Rust Treatment Perth: Stopping Corrosion Before It Spreads",
        "tag": "Maintenance",
        "read_time": 4,
        "excerpt": "Perth's coastal salt air and summer humidity create rust risk that inland drivers don't face. Here's how to identify rust early, treat it effectively, and protect your vehicle.",
        "body": """
      <p>Rust is less common in Perth than in humid eastern-state cities, but it's far from absent — especially for vehicles in coastal suburbs like Cottesloe, Scarborough, Fremantle, and Rockingham where salt air accelerates corrosion. Early treatment stops rust in its tracks; ignored rust becomes structural and expensive.</p>

      <h2>Where Rust Starts on Perth Vehicles</h2>
      <p>Perth's most common rust locations:</p>
      <ul>
        <li>Wheel arches and sill edges (stone chip damage exposes bare metal)</li>
        <li>Undercarriage, especially near the exhaust and fuel lines</li>
        <li>Brake callipers and rotor edges (surface rust after rain is normal; deep pitting is not)</li>
        <li>Sunroof drains and door drain holes (if blocked, water pools)</li>
        <li>Boot floor and spare tyre well (water ingress from faulty seals)</li>
        <li>Around windscreen rubber — Perth's UV degrades rubber seals, allowing water in</li>
      </ul>

      <h2>Surface Rust vs Structural Rust</h2>
      <p>Surface rust (reddish discolouration with intact metal below) can be treated and stopped. Structural rust (bubbling paint, flaking metal, holes) requires panel repair or replacement and is significantly more expensive. The key is intervention at the surface stage.</p>

      <h2>Treatment Options</h2>
      <ul>
        <li><strong>Sand and respray:</strong> Proper treatment for panel rust — grind back to bare metal, apply rust converter, prime, and repaint</li>
        <li><strong>Rust converters:</strong> Chemical treatments (Killrust, Inox) convert iron oxide to a stable compound and seal the surface — good for undersides and hidden areas</li>
        <li><strong>Wax injection:</strong> Cavity wax applied to door cavities and sills provides long-term protection — worth doing at purchase on used vehicles near the coast</li>
      </ul>

      <h2>Prevention in Coastal Suburbs</h2>
      <p>If you park within 2 km of the ocean: rinse the undercarriage with fresh water monthly, wax the paint twice a year, and check door seals and sunroof drains annually. An annual underbody inspection at a hoist-equipped workshop costs $50–$100 and catches issues early.</p>

      <div style="text-align:center;margin:40px 0 16px;">
        <a href="contact.html" class="btn btn-primary btn-lg">Get a Free Mechanic Quote &rarr;</a>
      </div>
      <p style="text-align:center;color:var(--muted);font-size:0.9rem;">We respond within 30 minutes. All Perth suburbs covered.</p>
""",
    },
    {
        "slug": "blog-car-detailing-vs-car-wash-perth",
        "title": "Car Detailing vs Car Wash Perth: What's the Difference?",
        "tag": "Maintenance",
        "read_time": 4,
        "excerpt": "Perth drivers often confuse a car detail with a car wash. They're not the same thing — and knowing the difference helps you get the right service at the right time and price.",
        "body": """
      <p>In Perth's dusty, sun-intense climate, keeping a car clean is more than cosmetic — it protects the paint from UV damage, removes corrosive contaminants like bird droppings and tree sap, and maintains resale value. But "car detailing" and "car wash" are very different services at very different price points.</p>

      <h2>What a Car Wash Includes</h2>
      <p>A car wash — whether tunnel, hand wash, or self-serve — cleans the exterior surface:</p>
      <ul>
        <li>Rinse and soap wash of the exterior</li>
        <li>Wheel rinse</li>
        <li>Window wipe</li>
        <li>Sometimes a basic vacuum</li>
      </ul>
      <p>Cost: $10–$30. Time: 10–20 minutes. Purpose: remove surface dirt. Does not address paint correction, interior deep cleaning, or protection.</p>

      <h2>What Car Detailing Includes</h2>
      <p>Detailing is a comprehensive treatment addressing paint, interior, and protection:</p>
      <ul>
        <li><strong>Exterior detail:</strong> Clay bar treatment (removes bonded contaminants), paint decontamination, machine polish (removes swirl marks, light scratches), sealant or wax application</li>
        <li><strong>Interior detail:</strong> Vacuum, steam clean, leather conditioning, plastic dressing, glass cleaning</li>
        <li><strong>Full detail:</strong> Combines both — takes 4–8 hours</li>
      </ul>
      <p>Cost: $150–$600+ depending on vehicle size and level of paint correction. Time: half a day to a full day.</p>

      <h2>When Does Perth's Climate Demand Detailing?</h2>
      <ul>
        <li>After a summer of UV exposure — paint can oxidise and fade without protection</li>
        <li>When buying or selling a used vehicle</li>
        <li>After a bushfire season — fine ash is mildly acidic and damages unprotected paint</li>
        <li>If bird droppings or tree sap have etched the clear coat</li>
      </ul>

      <h2>Ceramic Coating</h2>
      <p>For long-term protection in Perth's harsh conditions, ceramic coating ($500–$2,000 professionally applied) creates a semi-permanent protective layer that repels UV, water, and contaminants. It's the premium option for drivers who want minimal maintenance and maximum paint protection.</p>

      <div style="text-align:center;margin:40px 0 16px;">
        <a href="contact.html" class="btn btn-primary btn-lg">Get a Free Mechanic Quote &rarr;</a>
      </div>
      <p style="text-align:center;color:var(--muted);font-size:0.9rem;">We respond within 30 minutes. All Perth suburbs covered.</p>
""",
    },
    {
        "slug": "blog-performance-car-servicing-perth",
        "title": "Performance Car Servicing Perth: What's Different and Who to Trust",
        "tag": "Maintenance",
        "read_time": 5,
        "excerpt": "Servicing a performance car in Perth requires specialist knowledge, correct fluids, and experience with high-revving engines. Here's what performance car owners need to know.",
        "body": """
      <p>Performance cars — everything from hot hatches like the Volkswagen Golf GTI and Honda Civic Type R, to sports cars like the Porsche 718, Subaru WRX, and Ford Mustang GT — demand more from their drivers and their mechanics. Standard logbook servicing processes don't always translate to high-performance platforms.</p>

      <h2>Why Performance Cars Need Specialist Servicing</h2>
      <ul>
        <li><strong>Higher-spec engine oil:</strong> Performance engines often require fully synthetic oil with specific viscosity ratings (0W-40, 5W-40) and sometimes OEM-specific approvals (VW 502.00, Porsche A40)</li>
        <li><strong>Shorter oil change intervals:</strong> Turbocharged engines put more stress on oil — many manufacturers specify 10,000km intervals even with synthetic oil, down from 15,000km on standard cars</li>
        <li><strong>Brake servicing:</strong> High-performance brakes run hotter and require more frequent fluid changes and pad inspection</li>
        <li><strong>Suspension and alignment:</strong> Performance-tuned suspension is more sensitive to wear and alignment deviations — handling degrades noticeably when components are past specification</li>
      </ul>

      <h2>Turbocharged Engine Care</h2>
      <p>Perth drivers with turbo engines should observe:</p>
      <ul>
        <li>Allow 60–120 seconds of idle before shutting off after hard driving — lets the turbo cool and circulates oil to the bearings</li>
        <li>Avoid cold revving — let the oil circulate for 30 seconds before driving away in winter mornings</li>
        <li>Change oil at the shorter end of the manufacturer's range if the car is regularly driven hard</li>
      </ul>

      <h2>Finding a Specialist in Perth</h2>
      <p>Perth has a number of enthusiast-oriented independents who specialise in European performance, Japanese sports cars, or American muscle. Key indicators of a competent shop: dealer-level diagnostic software, experience with your specific platform, correct OEM or equivalent fluids stocked, and a customer base of enthusiasts. Perth Mechanic can connect you with mechanics who specialise in your vehicle type.</p>

      <h2>Cost Expectations</h2>
      <p>Performance logbook services typically cost 30–60% more than equivalent standard-car services due to oil specification, longer service times (more complex access), and higher-cost consumables. Budget $300–$600 for a performance hatchback service, $500–$900+ for a Porsche or similar.</p>

      <div style="text-align:center;margin:40px 0 16px;">
        <a href="contact.html" class="btn btn-primary btn-lg">Get a Free Mechanic Quote &rarr;</a>
      </div>
      <p style="text-align:center;color:var(--muted);font-size:0.9rem;">We respond within 30 minutes. All Perth suburbs covered.</p>
""",
    },
    {
        "slug": "blog-winter-car-maintenance-perth",
        "title": "Winter Car Maintenance Perth: What to Check Before the Cold Hits",
        "tag": "Seasonal",
        "read_time": 4,
        "excerpt": "Perth winters are mild but wet — and cold morning starts, wet roads, and reduced visibility create specific risks. Here's a practical winter car checklist for Perth drivers.",
        "body": """
      <p>Perth's winter (June–August) is mild compared to southern Australia but brings consistent rain, lower temperatures, and conditions that expose maintenance gaps drivers have ignored all summer. Cold, wet mornings are when ageing batteries fail, worn wiper blades fail their one important job, and tyre grip on slick roads becomes critical.</p>

      <h2>Winter Pre-Season Checklist</h2>

      <h3>Battery</h3>
      <p>Cold temperatures reduce battery capacity, and a battery that barely managed summer heat may fail on a cold June morning. If your battery is more than 3 years old, have it tested (free at most battery retailers and mechanics). A battery that fails a load test should be replaced proactively — Perth winter mornings at 8°C are not the time to discover a weak battery.</p>

      <h3>Wiper Blades</h3>
      <p>Perth's dry summer bakes rubber wiper blades — they often split, harden, or tear during the long non-use period. Test your wipers before the first winter rain: streaking, squealing, or skipping means replacement. A set of good quality blades costs $30–$60 and takes 5 minutes to fit.</p>

      <h3>Tyres</h3>
      <p>Wet-weather grip depends on tyre tread depth. In WA, the legal minimum is 1.5mm, but safety standards recommend a minimum of 3mm for wet-weather driving. Check tread depth with a coin (the tread should cover the text on a 20-cent piece).</p>

      <h3>Lights</h3>
      <p>Winter's earlier sunsets and rain mean your lights work harder. Check all bulbs — headlights, taillights, brake lights — and clean the lenses. Reduced-visibility conditions also mean it's worth replacing headlight bulbs proactively if they're original and the car is 5+ years old.</p>

      <h3>Heater and Demister</h3>
      <p>Test the heater and front/rear demisters before you need them. A failed heater matrix or demister element is an expensive and inconvenient repair to discover at 7am on a foggy morning.</p>

      <div style="text-align:center;margin:40px 0 16px;">
        <a href="contact.html" class="btn btn-primary btn-lg">Get a Free Mechanic Quote &rarr;</a>
      </div>
      <p style="text-align:center;color:var(--muted);font-size:0.9rem;">We respond within 30 minutes. All Perth suburbs covered.</p>
""",
    },
    {
        "slug": "blog-summer-car-maintenance-perth",
        "title": "Summer Car Maintenance Perth: Protect Your Car From the Heat",
        "tag": "Seasonal",
        "read_time": 4,
        "excerpt": "Perth's summers are brutal on vehicles — 40°C+ days, intense UV, and air conditioning running constantly. Here's a summer maintenance checklist to prevent breakdowns and protect your car.",
        "body": """
      <p>Perth summer means temperatures regularly exceeding 40°C, UV index at extreme levels, and vehicles running air conditioning for months on end. Summer in Perth is harder on vehicles than winter — it's when batteries fail, coolant systems are stressed, and tyres reach their limits on hot asphalt. A pre-summer maintenance check can prevent the most expensive breakdowns.</p>

      <h2>Summer Car Maintenance Checklist</h2>

      <h3>Cooling System</h3>
      <p>Your coolant level and condition are critical in summer. Check that coolant is at the correct level and that it hasn't turned brown (indicating contamination or degradation). A coolant system pressure test ($50–$80) checks for leaks before they strand you on the Mitchell Freeway.</p>

      <h3>Air Conditioning</h3>
      <p>If your AC isn't cooling as well as it should, have it regassed before peak heat. An annual regas costs $80–$150 and restores cooling performance. Also check the cabin air filter — a clogged filter reduces airflow significantly.</p>

      <h3>Battery</h3>
      <p>Counterintuitively, summer heat kills batteries faster than winter cold. Perth's 40°C summer temperatures accelerate internal battery degradation — vehicles that park outdoors in direct sun are particularly vulnerable. If your battery is 3+ years old, test it before summer.</p>

      <h3>Tyres</h3>
      <p>Hot asphalt increases tyre operating temperature. Under-inflated tyres build up more heat on hot days, increasing blowout risk. Check tyre pressures monthly in summer — pressure rises 1–2 PSI per 10°C increase in temperature, so check cold (before driving).</p>

      <h3>Wiper Blades and Fluid</h3>
      <p>Summer dust means you'll use washers constantly. Ensure fluid is topped up with proper washer fluid (water degrades rubber and promotes algae). Summer UV also deteriorates wiper rubber — replace if they smear or squeak.</p>

      <div style="text-align:center;margin:40px 0 16px;">
        <a href="contact.html" class="btn btn-primary btn-lg">Get a Free Mechanic Quote &rarr;</a>
      </div>
      <p style="text-align:center;color:var(--muted);font-size:0.9rem;">We respond within 30 minutes. All Perth suburbs covered.</p>
""",
    },
    {
        "slug": "blog-driving-tips-extend-car-life",
        "title": "Driving Tips That Extend Your Car's Life: Perth Mechanic's Advice",
        "tag": "Maintenance",
        "read_time": 5,
        "excerpt": "How you drive has as much impact on your car's longevity as how often you service it. These mechanic-backed habits can add years and tens of thousands of kilometres to any vehicle.",
        "body": """
      <p>Mechanics see a pattern: two identical vehicles, same age, same model, vastly different condition. The difference is almost always driving habits and servicing discipline. The good news is that the habits that extend a car's life cost nothing to adopt — they just require awareness.</p>

      <h2>Smooth Acceleration and Braking</h2>
      <p>Aggressive acceleration from lights puts stress on drivetrain components, burns more fuel, and accelerates tyre wear. Hard braking does the same to brake pads and rotors. Perth's predictable traffic flow on arterial roads makes smooth driving easy — read the lights ahead, coast to decelerate, and accelerate progressively.</p>

      <h2>Avoid Short Trips When Possible</h2>
      <p>Cold engine oil is thicker and circulates less effectively — it takes 5–10 minutes of driving for oil to reach operating temperature and provide proper lubrication. Frequent short trips (under 5km) mean the engine spends most of its time in a cold-running state, causing increased wear. Combine errands into longer trips where possible.</p>

      <h2>Let the Car Warm Up (Briefly)</h2>
      <p>Modern fuel-injected engines don't need extended warm-up periods like carburettor cars did. Idling for 30–60 seconds on cold mornings before driving away is sufficient — then drive gently for the first few kilometres rather than sitting and idling.</p>

      <h2>Load Management</h2>
      <p>Every extra kilogram you carry permanently increases fuel consumption, tyre wear, and brake wear. Remove unnecessary heavy items from the boot — roof racks and bike carriers add aerodynamic drag even when empty. Carrying only what you need for each trip makes a measurable difference over time.</p>

      <h2>Listen to Your Car</h2>
      <p>Unusual noises, new vibrations, changes in fuel economy, or warning lights are all communication. Ignoring them doesn't make them go away — it usually makes the eventual repair more expensive. Early diagnosis is almost always cheaper than late diagnosis.</p>

      <h2>Service on Time</h2>
      <p>The single biggest predictor of longevity is consistent, timely servicing. Engine oil is the most important fluid in the car — old, degraded oil accelerates wear on every moving part in the engine. Service at or before the manufacturer's recommended interval, not when it's convenient.</p>

      <div style="text-align:center;margin:40px 0 16px;">
        <a href="contact.html" class="btn btn-primary btn-lg">Get a Free Mechanic Quote &rarr;</a>
      </div>
      <p style="text-align:center;color:var(--muted);font-size:0.9rem;">We respond within 30 minutes. All Perth suburbs covered.</p>
""",
    },
    {
        "slug": "blog-car-storage-tips-perth",
        "title": "Storing Your Car in Perth: How to Prevent Problems During Long Periods Off the Road",
        "tag": "Maintenance",
        "read_time": 4,
        "excerpt": "Whether you're heading overseas, storing a second car, or putting a classic away for winter, Perth's climate creates specific storage challenges. Here's how to do it properly.",
        "body": """
      <p>Leaving a car unused for weeks or months creates problems that most drivers don't anticipate — flat tyres, dead batteries, fuel degradation, corrosion in unexpected places, and seized brake components. Perth's UV and heat make outdoor storage particularly harsh. Done right, a stored vehicle can sit for months and start first time when you return.</p>

      <h2>Before You Store</h2>
      <ul>
        <li><strong>Full tank of fuel:</strong> A full tank reduces the air space above the fuel, limiting oxidation and moisture accumulation. If storing for 6+ months, add a fuel stabiliser (available from automotive stores for $15–$20)</li>
        <li><strong>Fresh oil:</strong> Used oil contains acids and combustion byproducts that corrode engine internals over long periods. Service the car before storage, not after</li>
        <li><strong>Clean the vehicle thoroughly:</strong> Bird droppings, tree sap, and road grime left on paint can etch or corrode during storage</li>
        <li><strong>Check tyre pressures:</strong> Inflate to the upper end of the recommended range (or 10% over) to counteract the gradual loss that occurs over months</li>
      </ul>

      <h2>Battery Maintenance</h2>
      <p>A car battery will discharge to a damaging level within 4–8 weeks of no use. Options:</p>
      <ul>
        <li>Disconnect the negative terminal (simple, free, means resetting the clock/radio)</li>
        <li>Connect a battery tender or trickle charger ($40–$80) — the best option for long-term storage</li>
      </ul>

      <h2>Brakes and Wheels</h2>
      <p>Brake discs rust quickly when unused. Try to park on a firm, flat surface and avoid applying the handbrake for long periods — use wheel chocks instead to prevent brake pad/disc bonding.</p>

      <h2>Where to Store in Perth</h2>
      <p>Indoor storage is significantly better than outdoor in Perth. Options include self-storage facilities with vehicle bays ($100–$250/month), climate-controlled storage ($200–$500/month), and covered parking. If outdoor storage is unavoidable, a fitted car cover (not a generic tarp) is essential to protect paint from UV.</p>

      <div style="text-align:center;margin:40px 0 16px;">
        <a href="contact.html" class="btn btn-primary btn-lg">Get a Free Mechanic Quote &rarr;</a>
      </div>
      <p style="text-align:center;color:var(--muted);font-size:0.9rem;">We respond within 30 minutes. All Perth suburbs covered.</p>
""",
    },
    {
        "slug": "blog-roadside-assistance-perth",
        "title": "Roadside Assistance Perth: What's Covered and Which Plan to Choose",
        "tag": "Maintenance",
        "read_time": 4,
        "excerpt": "Breaking down in Perth — especially in summer or on a remote stretch of highway — can be dangerous. Here's what roadside assistance plans cover, what they cost, and which is worth it for Perth drivers.",
        "body": """
      <p>Perth's sprawling geography means breakdowns can happen far from help — from the outer suburbs to regional highways like the Great Eastern and Brand. Roadside assistance isn't just a city convenience; for WA drivers it's a genuine safety measure, especially in summer when temperatures exceed 40°C.</p>

      <h2>What Roadside Assistance Covers</h2>
      <p>All major plans include the basics:</p>
      <ul>
        <li>Battery jump-start</li>
        <li>Tyre change (if you have a serviceable spare)</li>
        <li>Emergency fuel delivery (usually a small amount to get you to a petrol station)</li>
        <li>Lockout assistance (if you've locked your keys inside)</li>
        <li>Towing to the nearest mechanic (distance limits vary by plan)</li>
      </ul>

      <h2>Major Providers in WA</h2>
      <ul>
        <li><strong>RAC:</strong> WA's own motoring club — excellent coverage across regional WA, strong local network, well-regarded response times. Annual membership from $105</li>
        <li><strong>NRMA/IAG:</strong> Expanding coverage in WA, often bundled with car insurance. Check coverage for remote areas before relying on it</li>
        <li><strong>Manufacturer plans:</strong> BMW Assist, Toyota Roadside Assistance, etc. — usually free for the warranty period (2–5 years), then require renewal</li>
        <li><strong>Insurance add-ons:</strong> Many insurers offer roadside assistance for $30–$60/year as an add-on</li>
      </ul>

      <h2>Regional WA Considerations</h2>
      <p>For drivers who regularly travel regional WA — the Nullarbor, Pilbara, Great Southern — check the provider's coverage map carefully. Some plans only cover major highways; others have response time clauses that render them ineffective in remote areas. RAC has the most established regional WA network.</p>

      <h2>Is Roadside Assistance Worth It?</h2>
      <p>At $100–$150/year, roadside assistance costs less than a single tow (which averages $150–$300 in Perth). For any driver with a vehicle more than 4–5 years old, it's worth it. For newer vehicles still under manufacturer warranty with included assistance, the factory plan often suffices for the first few years.</p>

      <div style="text-align:center;margin:40px 0 16px;">
        <a href="contact.html" class="btn btn-primary btn-lg">Get a Free Mechanic Quote &rarr;</a>
      </div>
      <p style="text-align:center;color:var(--muted);font-size:0.9rem;">We respond within 30 minutes. All Perth suburbs covered.</p>
""",
    },
    {
        "slug": "blog-second-hand-car-checklist-perth",
        "title": "Second-Hand Car Checklist Perth: What to Check Before You Buy",
        "tag": "Buying",
        "read_time": 5,
        "excerpt": "Buying a used car in Perth? This mechanic's checklist covers everything to inspect before you sign — from the test drive to the REVS check. Don't buy without reading this first.",
        "body": """
      <p>Perth's used car market is active and competitive — and sellers aren't always forthcoming about problems. A systematic inspection before purchase can save you thousands in immediate repair costs and reveal deal-breakers before they become your problem. This checklist is based on what mechanics look for when performing a pre-purchase inspection.</p>

      <h2>Before You Go to See It</h2>
      <ul>
        <li><strong>PPSR check (REVS):</strong> Run the registration number through the Personal Property Securities Register (ppsr.gov.au, $2) to confirm there's no financial encumbrance, it hasn't been written off, and the VIN matches what's advertised</li>
        <li><strong>Research common issues:</strong> Search "[make/model/year] common problems" — every model has known weaknesses that responsible buyers research in advance</li>
      </ul>

      <h2>Body and Exterior</h2>
      <ul>
        <li>Check panel gaps — inconsistent gaps indicate panel replacement after a collision</li>
        <li>Look down the panels from a low angle in good light — waves or ripples indicate body filler</li>
        <li>Check paint colour match between panels — slightly different shades indicate respray</li>
        <li>Open and close all doors, bonnet, and boot — they should operate smoothly and seal evenly</li>
        <li>Check for rust at wheel arches, sill edges, and under the boot carpet</li>
      </ul>

      <h2>Under the Bonnet</h2>
      <ul>
        <li>Check oil level and condition — black sludge indicates neglected servicing</li>
        <li>Check coolant reservoir — milky or oily coolant suggests a head gasket issue</li>
        <li>Look for signs of oil leaks around the engine, valve cover, and sump</li>
        <li>Check service records if available — consistent logbook history is a major positive</li>
      </ul>

      <h2>Test Drive</h2>
      <ul>
        <li>Cold start — note any excessive smoke (blue = oil burning, white = coolant, black = rich fuel)</li>
        <li>Brakes: firm pedal, straight stopping line, no vibration under braking</li>
        <li>Steering: centred, no pull, no vibration at speed</li>
        <li>Transmission: smooth shifts with no hesitation, slip, or clunk</li>
        <li>Air conditioning: blows cold within 60 seconds</li>
        <li>All warning lights extinguish after start</li>
      </ul>

      <h2>Pre-Purchase Inspection</h2>
      <p>Even with the above checks, a professional pre-purchase inspection ($150–$200) by an independent Perth mechanic is money well spent on any car over $8,000. They'll check components you can't see — wheel bearings, suspension joints, brake condition, diagnostic codes — and give you an impartial assessment.</p>

      <div style="text-align:center;margin:40px 0 16px;">
        <a href="contact.html" class="btn btn-primary btn-lg">Get a Free Mechanic Quote &rarr;</a>
      </div>
      <p style="text-align:center;color:var(--muted);font-size:0.9rem;">We respond within 30 minutes. All Perth suburbs covered.</p>
""",
    },
    {
        "slug": "blog-exhaust-system-repairs-perth",
        "title": "Exhaust System Repairs Perth: Signs, Causes, and What It Costs",
        "tag": "Repairs",
        "read_time": 4,
        "excerpt": "A failing exhaust isn't just noisy — it can be a safety hazard and a legal issue. Here's how to recognise exhaust problems, what causes them, and what repairs cost in Perth.",
        "body": """
      <p>Your vehicle's exhaust system does more than remove combustion gases — it reduces noise, controls emissions, and in some configurations improves engine performance. Problems range from minor nuisances (a small leak) to safety hazards (carbon monoxide entering the cabin). In WA, a defective exhaust can generate a defect notice and make a vehicle unregisterable.</p>

      <h2>Signs of an Exhaust Problem</h2>
      <ul>
        <li>Louder than normal exhaust note, especially a ticking or puffing sound at idle</li>
        <li>Exhaust smell inside the cabin — a serious safety concern (carbon monoxide risk)</li>
        <li>Hissing or rattling noise from under the vehicle</li>
        <li>Reduced fuel economy</li>
        <li>Check engine light (triggered by downstream oxygen sensor readings affected by leaks)</li>
        <li>Visible rust, holes, or hanging exhaust components</li>
      </ul>

      <h2>Common Exhaust System Failures</h2>
      <ul>
        <li><strong>Rusted exhaust pipes and mufflers:</strong> The most common failure — moisture from combustion accumulates inside, and external rust progresses from the outside. Short-trip driving accelerates this as exhaust never gets hot enough to dry out fully</li>
        <li><strong>Cracked or blown exhaust manifold:</strong> The manifold bolts to the engine and cracks under thermal cycling — produces a characteristic ticking sound that changes with engine temperature</li>
        <li><strong>Failed flexi-pipe:</strong> The corrugated flexible section near the engine fails on higher-mileage vehicles, causing a loud blowing noise</li>
        <li><strong>Broken hangers and mounts:</strong> Rubber mounts degrade and snap — the exhaust drops and rattles against the chassis</li>
      </ul>

      <h2>Exhaust Repair Costs in Perth</h2>
      <ul>
        <li>Flexi-pipe replacement: $180–$350 fitted</li>
        <li>Muffler replacement: $250–$500</li>
        <li>Full system replacement (cat-back): $400–$1,200</li>
        <li>Exhaust manifold repair or replacement: $400–$900+</li>
        <li>Hanger/mount replacement: $80–$150</li>
      </ul>

      <div style="text-align:center;margin:40px 0 16px;">
        <a href="contact.html" class="btn btn-primary btn-lg">Get a Free Mechanic Quote &rarr;</a>
      </div>
      <p style="text-align:center;color:var(--muted);font-size:0.9rem;">We respond within 30 minutes. All Perth suburbs covered.</p>
""",
    },
    {
        "slug": "blog-clutch-replacement-perth",
        "title": "Clutch Replacement Perth: Signs It's Failing and What It Costs",
        "tag": "Repairs",
        "read_time": 5,
        "excerpt": "A failing clutch gives clear warning signs before it fails completely. Here's how to recognise the symptoms, what causes clutch wear in Perth conditions, and what replacement costs.",
        "body": """
      <p>The clutch is a wear item — designed to last 80,000–150,000 km under normal conditions, though driving style has enormous impact on this. Perth's mix of heavy stop-start suburban traffic, hills in the western suburbs and Hills District, and long freeway runs creates varied clutch demands. Recognising early symptoms saves you from the classic failure scenario: clutch goes fully at the worst possible time.</p>

      <h2>Warning Signs of a Failing Clutch</h2>
      <ul>
        <li><strong>Slipping:</strong> Engine revs rise under acceleration but vehicle speed doesn't increase proportionally — the clutch plate is no longer gripping effectively</li>
        <li><strong>Difficulty engaging gears:</strong> Hard to get into gear, crunching when changing, or grinding when trying first gear from a standstill</li>
        <li><strong>Clutch pedal vibration:</strong> A juddering or chattering through the pedal when releasing the clutch from a standstill</li>
        <li><strong>High engagement point:</strong> Clutch only engages near the top of the pedal travel (normal is mid-travel) — indicates significant wear</li>
        <li><strong>Burning smell:</strong> Distinctive smell from the driver's footwell area, especially after hill starts or heavy traffic use</li>
        <li><strong>Noisy clutch pedal:</strong> Squeaking or squealing when pressing the pedal suggests a worn release bearing</li>
      </ul>

      <h2>What Causes Early Clutch Wear</h2>
      <ul>
        <li>Riding the clutch (keeping partial pressure on the pedal while driving)</li>
        <li>Resting your foot on the clutch pedal at lights instead of placing it on the floor</li>
        <li>Launching aggressively from standstill (slipping the clutch under high throttle)</li>
        <li>Hill starts in traffic — frequent clutch slipping in stop-start hill traffic</li>
      </ul>

      <h2>What's Replaced in a Clutch Job</h2>
      <p>A proper clutch replacement includes three components — the clutch plate (friction disc), the pressure plate, and the release bearing. These are always replaced as a set. Many mechanics also resurface or replace the flywheel at the same time (the flywheel must be removed anyway), as a worn flywheel can cause the new clutch to fail prematurely.</p>

      <h2>Clutch Replacement Costs in Perth</h2>
      <ul>
        <li>Small hatchback (Mazda 3, Corolla): $600–$900</li>
        <li>Medium sedan/SUV (Subaru WRX, Mazda 6): $800–$1,400</li>
        <li>Ute or 4WD (HiLux, Ranger, Triton): $1,000–$2,000+</li>
        <li>European performance (Golf GTI, 86, BRZ): $1,200–$2,500</li>
      </ul>
      <p>Labour is a significant component — most clutch jobs require removing the gearbox, which takes 3–6 hours depending on vehicle complexity.</p>

      <div style="text-align:center;margin:40px 0 16px;">
        <a href="contact.html" class="btn btn-primary btn-lg">Get a Free Mechanic Quote &rarr;</a>
      </div>
      <p style="text-align:center;color:var(--muted);font-size:0.9rem;">We respond within 30 minutes. All Perth suburbs covered.</p>
""",
    },
    {
        "slug": "blog-air-conditioning-regas-perth",
        "title": "Air Conditioning Regas Perth: What It Is, When You Need It, and What It Costs",
        "tag": "Maintenance",
        "read_time": 4,
        "excerpt": "Perth's summer makes air conditioning essential, not optional. Here's what an AC regas involves, how to tell if you need one, and what it costs at Perth workshops.",
        "body": """
      <p>In Perth, air conditioning isn't a luxury — it's a necessity for 5–6 months of the year. A vehicle without functional AC in February is a genuine health risk, not just a comfort issue. AC systems naturally lose refrigerant over time, and the regas is one of the most straightforward and cost-effective services any Perth driver can get.</p>

      <h2>How Car Air Conditioning Works</h2>
      <p>Car AC uses a refrigerant (R134a in most pre-2020 vehicles, R1234yf in newer models) compressed by a belt-driven compressor to absorb heat from inside the cabin and release it outside. The refrigerant circulates in a closed loop and gradually leaks through microscopic permeation points in hoses and seals over time — even in a perfectly healthy system.</p>

      <h2>Signs You Need a Regas</h2>
      <ul>
        <li>AC blows cool but not as cold as it used to</li>
        <li>AC blows cold initially but warms up after a few minutes</li>
        <li>AC takes longer than 60 seconds to begin cooling</li>
        <li>It's been more than 2 years since the last service or regas</li>
      </ul>

      <h2>What a Regas Involves</h2>
      <ol>
        <li>Recover any remaining refrigerant (legally required — venting to atmosphere is not permitted)</li>
        <li>Check system pressure for leaks</li>
        <li>Pull the system to vacuum for 20–30 minutes to remove moisture</li>
        <li>Recharge with the correct refrigerant type and quantity</li>
        <li>Add UV dye (for future leak detection) and lubricant oil</li>
      </ol>
      <p>The whole process takes 45–60 minutes.</p>

      <h2>AC Regas Costs in Perth</h2>
      <ul>
        <li>R134a regas (pre-2020 vehicles): $80–$150</li>
        <li>R1234yf regas (newer vehicles): $180–$350 (the refrigerant itself is significantly more expensive)</li>
        <li>If a significant leak is found: additional diagnosis and repair required ($150–$400+)</li>
      </ul>

      <h2>When to Book</h2>
      <p>Don't wait until you're sweltering in February — workshops are booked out during Perth's peak summer. October or November is ideal: book a regas before the first 35°C day and you'll be set for summer without the wait.</p>

      <div style="text-align:center;margin:40px 0 16px;">
        <a href="contact.html" class="btn btn-primary btn-lg">Get a Free Mechanic Quote &rarr;</a>
      </div>
      <p style="text-align:center;color:var(--muted);font-size:0.9rem;">We respond within 30 minutes. All Perth suburbs covered.</p>
""",
    },
]

# ---------------------------------------------------------------------------
# HTML template
# ---------------------------------------------------------------------------

HTML_TEMPLATE = """\
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="{meta_description}" />
  <meta name="robots" content="index, follow" />
  <title>{page_title} | Perth Mechanic</title>
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
      <a href="index.html">Home</a>
      <a href="services.html">Services</a>
      <div class="dropdown">
        <button class="dropdown-btn">Suburbs &#9660;</button>
        <div class="dropdown-menu">
          <a href="fremantle.html">Fremantle</a><a href="joondalup.html">Joondalup</a><a href="midland.html">Midland</a><a href="armadale.html">Armadale</a><a href="rockingham.html">Rockingham</a><a href="mandurah.html">Mandurah</a><a href="osborne-park.html">Osborne Park</a><a href="canning-vale.html">Canning Vale</a><a href="cannington.html">Cannington</a><a href="morley.html">Morley</a>
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
<section class="page-hero">
  <div class="container" style="max-width:800px;">
    <div style="margin-bottom:12px;"><a href="blog.html" style="color:var(--accent);font-size:0.9rem;text-decoration:none;">&larr; Back to Blog</a></div>
    <h1>{h1_title}</h1>
    <p style="color:rgba(255,255,255,.7);font-size:0.95rem;margin-top:12px;">Published 2026 &nbsp;|&nbsp; {read_time} min read</p>
  </div>
</section>
<section class="section-pad">
  <div class="container" style="max-width:800px;">
    <article class="blog-article">
{body}
    </article>
  </div>
</section>
<footer class="site-footer">
  <div class="container">
    <div class="footer-top">
      <div class="footer-brand">
        <a href="index.html" class="logo">Perth<span>Mechanic</span></a>
        <p>Perth's trusted mechanic connection service.<br>Matching Perth drivers with qualified, affordable mechanics since 2024.</p>
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
{{"@context":"https://schema.org","@type":"Article","headline":"{schema_headline}","description":"{meta_description}","url":"https://perthmechanic.com/{slug}.html","datePublished":"2026-01-01","dateModified":"2026-01-01","author":{{"@type":"Organization","name":"Perth Mechanic","url":"https://perthmechanic.com"}},"publisher":{{"@type":"Organization","name":"Perth Mechanic","url":"https://perthmechanic.com"}},"mainEntityOfPage":{{"@type":"WebPage","@id":"https://perthmechanic.com/{slug}.html"}}}}
</script>
</body>
</html>"""


def main():
    os.makedirs(DRAFTS_DIR, exist_ok=True)

    # Load existing queue
    with open(QUEUE_FILE, "r") as f:
        queue_data = json.load(f)

    existing_slugs = {item["slug"] for item in queue_data["queue"]}
    generated = []
    skipped = []

    for post in POSTS:
        slug = post["slug"]
        if slug in existing_slugs:
            skipped.append(slug)
            continue

        # Build the HTML file
        html = HTML_TEMPLATE.format(
            slug=slug,
            page_title=post["title"],
            h1_title=post["title"],
            meta_description=post["excerpt"].replace('"', '&quot;'),
            schema_headline=post["title"].replace('"', '\\"'),
            read_time=post["read_time"],
            body=post["body"],
        )

        out_path = os.path.join(DRAFTS_DIR, f"{slug}.html")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)

        # Append queue entry
        queue_data["queue"].append({
            "slug": slug,
            "title": post["title"],
            "tag": post["tag"],
            "read_time": post["read_time"],
            "excerpt": post["excerpt"],
        })
        existing_slugs.add(slug)
        generated.append(slug)
        print(f"  [OK] {slug}.html")

    # Save updated queue
    with open(QUEUE_FILE, "w", encoding="utf-8") as f:
        json.dump(queue_data, f, indent=2, ensure_ascii=False)

    print(f"\nDone. Generated: {len(generated)}  Skipped (already in queue): {len(skipped)}")
    if skipped:
        print("Skipped:", skipped)
    print(f"Queue now contains {len(queue_data['queue'])} entries.")


if __name__ == "__main__":
    main()
