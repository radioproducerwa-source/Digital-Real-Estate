#!/usr/bin/env python3
"""Generate 20 new blog draft HTML files and append them to drafts/queue.json."""

import json, os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DRAFTS_DIR = os.path.join(BASE_DIR, "drafts")
QUEUE_FILE = os.path.join(DRAFTS_DIR, "queue.json")

POSTS = [
    {
        "slug": "blog-engine-warning-light-perth",
        "title": "Engine Warning Light On? Here's What Perth Drivers Should Do",
        "tag": "Advice",
        "read_time": 5,
        "excerpt": "That little orange light on your dashboard can mean anything from a loose fuel cap to a serious engine fault. Here's how to decode it and what to do next.",
        "h1": "Engine Warning Light On? Here's What Perth Drivers Should Do",
        "meta": "Engine warning light on in Perth? Find out what the most common causes are, which ones are urgent, and when to book your car in with a mechanic.",
        "content": """<p>The engine warning light — also called the check engine light or malfunction indicator lamp (MIL) — is one of the most misunderstood signals in any car. It can indicate something minor, or something that, if ignored, leads to thousands of dollars in repair bills.</p>

<h2>What Triggers the Engine Warning Light?</h2>
<p>Modern vehicles have an OBD-II (on-board diagnostics) system that monitors hundreds of sensors. When one reads outside its expected range, it stores a fault code and illuminates the warning light. Common causes include:</p>
<ul>
  <li><strong>Loose or faulty fuel cap</strong> — one of the most common and easiest fixes</li>
  <li><strong>Faulty oxygen sensor</strong> — affects fuel efficiency and emissions</li>
  <li><strong>Catalytic converter issues</strong> — often triggered by failing oxygen sensors</li>
  <li><strong>Mass airflow sensor fault</strong> — causes rough idling and poor acceleration</li>
  <li><strong>Spark plug or ignition coil failure</strong> — engine misfires are a telltale sign</li>
  <li><strong>Transmission problems</strong> — some faults trigger the engine light rather than a separate warning</li>
</ul>

<h2>Steady Light vs Flashing Light</h2>
<p>A <strong>steady engine warning light</strong> usually means a non-critical fault — the car is safe to drive to a mechanic soon, but you don't need to pull over immediately.</p>
<p>A <strong>flashing or blinking engine warning light</strong> is more serious. It typically indicates an active engine misfire, which can damage your catalytic converter if you keep driving. Pull over safely, let the car cool, and call for assistance.</p>

<h2>Other Warning Signs to Watch For</h2>
<p>If your engine warning light is accompanied by any of the following, treat it as urgent:</p>
<ul>
  <li>Rough idling or shaking</li>
  <li>Loss of power when accelerating</li>
  <li>Strong fuel smell from inside the cabin</li>
  <li>Smoke from under the bonnet</li>
  <li>Temperature gauge spiking</li>
</ul>

<h2>Can You Drive With the Engine Warning Light On?</h2>
<p>In most cases, a steady light means you can drive carefully to a mechanic within a day or two. But you should avoid highway speeds, towing, or long trips until it's diagnosed. Ignoring the light for weeks is where drivers get into expensive trouble.</p>

<h2>Getting It Diagnosed in Perth</h2>
<p>A mechanic will plug a scan tool into your OBD-II port (usually located under the dashboard near the steering column) to read the stored fault codes. This diagnostic check takes 15–30 minutes and typically costs $80–$150 in Perth, though many workshops include it in the cost of repairs.</p>
<p>Don't be tempted to clear the codes yourself without fixing the underlying fault — the light will come back on within a few drive cycles.</p>

<h2>Perth Summer and Warning Lights</h2>
<p>Perth's extreme summer heat puts extra stress on cooling systems, fuel systems, and batteries. It's not unusual to see an uptick in warning lights during January and February. Regular servicing — including coolant checks and battery tests — can prevent many of these faults from occurring in the first place.</p>

<h2>Book a Diagnostic Check</h2>
<p>If your engine warning light is on, don't wait and hope it goes away. Book a diagnostic check with a Perth mechanic and get a clear answer on what's happening under the bonnet.</p>"""
    },
    {
        "slug": "blog-oil-change-perth",
        "title": "How Often Should You Change Your Oil in Perth?",
        "tag": "Maintenance",
        "read_time": 4,
        "excerpt": "Oil change intervals have changed dramatically with modern engines. Here's what Perth drivers actually need to know — and why the old '5,000km rule' no longer applies.",
        "h1": "How Often Should You Change Your Oil in Perth?",
        "meta": "Wondering how often to change your car's oil in Perth? Get the facts on modern oil change intervals, what type of oil your car needs, and when to book a service.",
        "content": """<p>Ask five Perth mechanics how often you should change your oil and you might get five different answers. The reality is it depends on your car, the oil type, and how you drive. Here's what actually matters.</p>

<h2>The Old Rule vs Modern Reality</h2>
<p>For decades, the standard advice was to change your oil every 5,000 km or three months. That rule was based on older engine technology and conventional mineral oil. Most modern vehicles with synthetic oil can go significantly longer — typically 10,000–15,000 km between changes, and some newer cars up to 20,000 km.</p>
<p>Always check your owner's manual first. Manufacturer recommendations vary considerably between makes and models.</p>

<h2>Factors That Affect Oil Change Intervals</h2>
<ul>
  <li><strong>Oil type</strong> — Synthetic oil lasts longer than semi-synthetic or mineral oil</li>
  <li><strong>Engine age</strong> — Older engines often benefit from more frequent changes</li>
  <li><strong>Driving conditions</strong> — Short trips, stop-start city driving, and towing are harder on oil than highway driving</li>
  <li><strong>Perth heat</strong> — High ambient temperatures accelerate oil breakdown; our summers are tough on lubricants</li>
  <li><strong>Turbo engines</strong> — Turbocharged engines run hotter and may need more frequent oil changes</li>
</ul>

<h2>Signs Your Oil Needs Changing</h2>
<p>Don't rely only on kilometre intervals. Check your oil regularly and look for these signs it's due for a change:</p>
<ul>
  <li>Oil is very dark or black (clean oil is golden-amber)</li>
  <li>Oil level is low on the dipstick</li>
  <li>Oil warning light illuminated</li>
  <li>Engine sounds noisier than usual (knocking or ticking)</li>
  <li>Burning oil smell inside the cabin</li>
</ul>

<h2>What Oil Does Your Car Need?</h2>
<p>Using the wrong viscosity grade can cause premature engine wear. Your owner's manual specifies the correct grade (e.g. 5W-30, 0W-20). In Perth's climate, the "W" rating (winter rating) matters less, but the high-temperature rating matters more. Always use the manufacturer-specified grade.</p>

<h2>Oil Changes as Part of a Full Service</h2>
<p>In Perth, a standard logbook service includes an oil and filter change as a base. If you're due for a service and an oil change at the same time, it's more cost-effective to combine them rather than booking separately.</p>
<p>For vehicles between services that need just an oil top-up or change, most Perth workshops offer a quick-service option for around $80–$180 depending on oil type and quantity required.</p>

<h2>Book Your Oil Change in Perth</h2>
<p>Regular oil changes are the single most effective thing you can do to extend your engine's life. If you're not sure when yours is due, a Perth mechanic can check your service history and advise on the right interval for your vehicle.</p>"""
    },
    {
        "slug": "blog-suspension-problems-perth",
        "title": "Suspension Problems: Signs Your Shocks Need Replacing in Perth",
        "tag": "Repairs",
        "read_time": 5,
        "excerpt": "Worn suspension doesn't just make your ride uncomfortable — it affects braking distances and steering control. Here's how to spot the signs before Perth's road conditions cause a bigger problem.",
        "h1": "Suspension Problems: Signs Your Shocks Need Replacing in Perth",
        "meta": "Worn shocks and struts are a safety issue, not just a comfort one. Learn the warning signs of suspension problems and what replacement costs in Perth.",
        "content": """<p>Perth's roads — from the smooth freeway to the potholed suburban backstreets — put real stress on your car's suspension system. Worn shocks and struts don't just make your ride rougher; they increase braking distances and reduce your ability to steer around hazards.</p>

<h2>How Suspension Works</h2>
<p>Your car's suspension system serves two purposes: keeping your tyres in contact with the road, and absorbing bumps so the cabin stays stable. The key components are shock absorbers (shocks), struts, springs, control arms, and bushings. When any of these wear out, handling and safety suffer.</p>

<h2>Warning Signs of Worn Suspension</h2>
<ul>
  <li><strong>Bouncing after bumps</strong> — if your car continues to bounce after hitting a dip, shocks are likely worn</li>
  <li><strong>Nose-diving under braking</strong> — the front dips sharply when you brake</li>
  <li><strong>Body roll in corners</strong> — excessive lean when turning</li>
  <li><strong>Uneven tyre wear</strong> — cupping or scalloping on the tyre tread is a classic sign</li>
  <li><strong>Clunking or knocking sounds</strong> — especially over speed humps or rough surfaces</li>
  <li><strong>Vehicle pulling to one side</strong> — can indicate a worn strut or bushing on one side</li>
  <li><strong>Vibration through the steering wheel</strong> — at highway speeds especially</li>
</ul>

<h2>The Bounce Test</h2>
<p>A simple roadside test: push down hard on each corner of your car and release. If the car bounces more than 1–2 times before settling, your shocks are likely worn.</p>

<h2>How Long Do Shocks Last?</h2>
<p>Most shocks and struts have a service life of around 80,000–100,000 km, though this varies significantly based on road conditions and load. Perth drivers who regularly carry heavy loads or travel on corrugated roads may see shorter lifespans.</p>

<h2>Shocks vs Struts: What's the Difference?</h2>
<p>Shocks and struts both dampen suspension movement, but struts are structural components that also support the vehicle's weight. Replacing struts is more involved (and expensive) than replacing shocks. Your mechanic can advise which your vehicle uses.</p>

<h2>What Does Suspension Replacement Cost in Perth?</h2>
<p>Shock absorber replacement in Perth typically costs $150–$400 per corner including parts and labour, depending on the vehicle. Strut replacement runs higher — $300–$700 per corner. Replacing in pairs (both fronts or both rears) is standard practice to maintain balanced handling.</p>

<h2>Don't Ignore Suspension Problems</h2>
<p>Worn suspension directly affects your ability to stop and steer in an emergency. If you're noticing any of the signs above, have your suspension inspected by a Perth mechanic before the next long drive — especially if you're planning a trip to regional WA where road quality varies significantly.</p>"""
    },
    {
        "slug": "blog-4wd-servicing-perth",
        "title": "4WD Servicing Perth: What's Different From a Regular Car Service",
        "tag": "4WD",
        "read_time": 5,
        "excerpt": "Perth is Australia's gateway to some of the most remote off-road terrain in the world. If you're running a 4WD, your servicing needs are different — here's what to know.",
        "h1": "4WD Servicing Perth: What's Different From a Regular Car Service",
        "meta": "4WDs need specialised servicing beyond a standard logbook service. Learn what Perth 4WD owners should have checked — especially before heading off-road in WA.",
        "content": """<p>Perth is the jumping-off point for some of Australia's best 4WD country — the Kimberley, Gibb River Road, Coral Bay, and hundreds of tracks across the Southwest. If you're running a 4WD in Perth, a standard logbook service is just the baseline. Here's what else needs attention.</p>

<h2>Why 4WDs Need Specialised Servicing</h2>
<p>Four-wheel drive vehicles have additional drivetrain components that standard passenger cars don't: transfer cases, front and rear differentials, locking hubs, and (on some vehicles) solid front axles. These components have their own fluid and maintenance requirements that a standard car service won't address.</p>

<h2>Key 4WD Service Items</h2>
<ul>
  <li><strong>Differential oils</strong> — front and rear diffs need fluid changes at regular intervals (typically every 40,000–60,000 km, or after water crossings)</li>
  <li><strong>Transfer case fluid</strong> — the gearbox that distributes power between front and rear axles</li>
  <li><strong>Wheel bearing inspection</strong> — 4WDs carry heavier loads and take harder punishment; bearings wear faster</li>
  <li><strong>CV joint and driveshaft inspection</strong> — critical on vehicles with front independent suspension</li>
  <li><strong>Brake inspection</strong> — heavier vehicles need more braking force; pads and rotors wear faster</li>
  <li><strong>Suspension lift and aftermarket component check</strong> — if you've lifted your 4WD, steering geometry and component compatibility should be verified</li>
  <li><strong>Snorkel and air filter</strong> — essential if driving in dusty or wet conditions</li>
</ul>

<h2>Pre-Trip 4WD Inspection</h2>
<p>Before any serious off-road trip from Perth, get a dedicated pre-trip inspection. This should cover:</p>
<ul>
  <li>All fluid levels including coolant, brake fluid, power steering</li>
  <li>Tyre condition and pressure (including spare)</li>
  <li>Brake system</li>
  <li>Lights and electrics</li>
  <li>Recovery points and tow bar if fitted</li>
  <li>Anything that's been making noise or handling oddly</li>
</ul>

<h2>After Off-Road Use</h2>
<p>After a serious off-road trip — especially any water crossings — have the following checked:</p>
<ul>
  <li>Diff and transfer case fluids for water contamination (milky appearance = water ingress)</li>
  <li>Brake calipers and drums for mud packing</li>
  <li>Undercarriage for damage or rock strikes</li>
  <li>Wheel bearings for play</li>
</ul>

<h2>Finding a 4WD Specialist in Perth</h2>
<p>Not all mechanics have experience with serious 4WD servicing. Look for a workshop that services your make (Toyota, Nissan, Mitsubishi, Ford, etc.) and has experience with off-road setups. Perth's northern and southern industrial suburbs — Malaga, Osborne Park, Wangara, Bibra Lake — have a high concentration of 4WD specialists.</p>

<h2>Book Your 4WD Service Before Your Next Trip</h2>
<p>Don't head to a remote WA track with a service overdue. Book a 4WD service in Perth before you go — a mechanical failure 500 km from the nearest town is a very different problem than one on the highway.</p>"""
    },
    {
        "slug": "blog-car-battery-perth",
        "title": "Car Battery Replacement Perth: When & How Much",
        "tag": "Maintenance",
        "read_time": 4,
        "excerpt": "Perth's summer heat is one of the biggest killers of car batteries. Here's how to spot a failing battery, how long they last in WA, and what replacement costs.",
        "h1": "Car Battery Replacement Perth: When & How Much",
        "meta": "Car batteries fail faster in Perth's heat. Learn the warning signs of a dying battery, how long they last in WA, and what battery replacement costs in Perth.",
        "content": """<p>Perth's summers are brutal on car batteries. The extreme heat accelerates the chemical degradation inside the battery, which is why WA drivers often find their batteries failing earlier than the manufacturer's rated life.</p>

<h2>How Long Do Car Batteries Last in Perth?</h2>
<p>In cooler climates, a car battery typically lasts 4–6 years. In Perth, the heat-accelerated degradation often means 2.5–4 years is more realistic — especially for vehicles parked outdoors in summer. Batteries that spend time in very hot engine bays (common in older engine designs) also degrade faster.</p>

<h2>Warning Signs of a Failing Battery</h2>
<ul>
  <li><strong>Slow cranking</strong> — engine turns over sluggishly, especially on cold mornings</li>
  <li><strong>Battery warning light</strong> on the dashboard</li>
  <li><strong>Electrical issues</strong> — flickering lights, power windows moving slowly</li>
  <li><strong>Swollen battery case</strong> — a visible sign of heat damage</li>
  <li><strong>Clicking sound</strong> when you turn the key (insufficient charge to crank)</li>
  <li><strong>Needing a jump start</strong> more than once</li>
</ul>

<h2>Don't Wait for a No-Start</h2>
<p>Battery failure often happens without warning — one morning the car starts fine, the next it won't start at all. This is especially true in summer when the overnight cooling provides a brief respite before another hot day destroys what's left of the battery's capacity. If your battery is 3+ years old and you're noticing any symptoms, proactively replace it rather than waiting for a breakdown.</p>

<h2>Battery Testing in Perth</h2>
<p>Most Perth mechanics and auto electricians can load-test your battery in about 10 minutes. A load test reveals the true health of the battery — not just whether it's holding a surface charge, but whether it can deliver the power needed to start your engine under real conditions. Many workshops offer free battery testing.</p>

<h2>What Does a New Battery Cost in Perth?</h2>
<p>Battery prices in Perth depend on the type and size required for your vehicle:</p>
<ul>
  <li><strong>Standard lead-acid battery</strong> — $150–$280 fitted</li>
  <li><strong>AGM (Absorbent Glass Mat) battery</strong> — $250–$450 fitted — required for many modern vehicles with stop-start systems</li>
  <li><strong>Lithium battery</strong> — $400+ — mainly aftermarket/performance applications</li>
</ul>
<p>Note: Some modern European vehicles require the battery to be "registered" to the car's ECU after replacement — a process your mechanic must perform to prevent charging system issues.</p>

<h2>How Long Does Battery Replacement Take?</h2>
<p>A straightforward battery swap takes 15–30 minutes. Vehicles requiring ECU registration may take slightly longer.</p>

<h2>Book a Battery Check in Perth</h2>
<p>If your car is starting to feel hesitant or you've got a battery that's more than 3 years old heading into summer, get it tested. A $10 battery test now is cheaper than a $150 call-out fee if you're stranded in a car park on a 40-degree Perth afternoon.</p>"""
    },
    {
        "slug": "blog-diesel-vs-petrol-servicing",
        "title": "Diesel vs Petrol Car Servicing: What's the Difference in Perth?",
        "tag": "Advice",
        "read_time": 5,
        "excerpt": "Diesel and petrol engines have different servicing needs, costs, and intervals. If you're switching from one to the other — or just want to know what you're paying for — here's the breakdown.",
        "h1": "Diesel vs Petrol Car Servicing: What's the Difference in Perth?",
        "meta": "Diesel and petrol engines need different servicing. Find out how service intervals, costs, and maintenance requirements differ for Perth drivers.",
        "content": """<p>Diesel engines have traditionally been popular in Perth for their torque, towing capability, and fuel economy on long regional drives. But diesel servicing is different from petrol — and in some respects, more involved. Here's what Perth drivers should know.</p>

<h2>Service Intervals</h2>
<p><strong>Petrol engines</strong> typically require servicing every 10,000–15,000 km with synthetic oil, or every 6–12 months.</p>
<p><strong>Diesel engines</strong> generally need servicing more frequently — every 10,000–15,000 km is standard, but some high-mileage diesel vehicles benefit from oil changes at 7,500 km intervals. Diesel engines produce more soot and contaminants that accumulate in the oil faster, especially in stop-start city driving.</p>

<h2>Fuel Filters</h2>
<p>Diesel fuel filters are more significant than petrol fuel filters. Diesel is more susceptible to contamination from water and particulates, which can damage expensive injectors. Diesel fuel filters typically need replacing every 30,000–40,000 km. Some diesel vehicles also have a water separator that needs draining regularly.</p>

<h2>DPF — Diesel Particulate Filter</h2>
<p>Modern diesel vehicles (post-2010 roughly) are fitted with a Diesel Particulate Filter (DPF), which captures soot from the exhaust. The DPF periodically "regenerates" by burning off the accumulated soot — a process that requires sustained highway driving speeds. Perth city drivers who rarely venture onto the highway can experience premature DPF blockage.</p>
<p>A blocked DPF is expensive to replace ($1,500–$4,000+). The best prevention is regular highway driving to allow passive regeneration, and ensuring your service intervals are kept up to date.</p>

<h2>Glow Plugs</h2>
<p>Instead of spark plugs, diesel engines use glow plugs to heat the combustion chamber for cold starts. Glow plugs typically last 80,000–100,000 km and are replaced as a set. Signs of failing glow plugs include hard starting on cold mornings and white smoke on startup.</p>

<h2>Oil Type and Capacity</h2>
<p>Diesel engines require diesel-specific oil (look for C-ratings: C1, C2, C3 etc. on the label). Using the wrong oil in a diesel with a DPF can cause filter damage. Diesels also tend to have larger oil capacities than equivalent petrol engines, which increases the cost per service slightly.</p>

<h2>Which Is Cheaper to Service?</h2>
<p>In Perth, a standard petrol service runs $150–$300 depending on the vehicle. Diesel services typically run $200–$400 — slightly higher due to larger oil volumes, diesel-specific filters, and the additional complexity. However, diesel's better fuel economy often compensates over time for drivers covering high kilometres.</p>

<h2>Turbo Diesel Maintenance</h2>
<p>Most modern diesels are turbocharged. Turbo seals and bearings are oil-lubricated, so maintaining clean oil is critical. After hard driving, it's good practice to let the engine idle for 1–2 minutes before switching off — this allows the turbo to cool while still being lubricated.</p>

<h2>Book Your Diesel Service in Perth</h2>
<p>Whether you're driving a Hilux, Ranger, Prado, or a European diesel, find a mechanic experienced with your engine type. Diesel servicing done right pays dividends in longevity — most diesel engines, properly maintained, will reach 400,000+ km without major overhaul.</p>"""
    },
    {
        "slug": "blog-transmission-service-perth",
        "title": "Transmission Service Perth: When Do You Need One?",
        "tag": "Repairs",
        "read_time": 5,
        "excerpt": "Automatic transmission fluid degrades over time, causing gear slip and eventual failure. Here's when Perth drivers need a transmission service and what it costs.",
        "h1": "Transmission Service Perth: When Do You Need One?",
        "meta": "Automatic transmission service in Perth — find out the warning signs, service intervals, and costs for keeping your gearbox healthy.",
        "content": """<p>The transmission (or gearbox) is one of the most expensive components in your vehicle to replace — often $3,000–$8,000 or more. Regular servicing is the most cost-effective way to avoid that bill. Yet transmission servicing is frequently overlooked by Perth drivers.</p>

<h2>Manual vs Automatic Transmission Service</h2>
<p><strong>Manual gearboxes</strong> require gearbox oil changes every 60,000–80,000 km in most vehicles. They're relatively simple compared to automatics.</p>
<p><strong>Automatic transmissions</strong> are more complex. They contain hydraulic fluid (ATF — Automatic Transmission Fluid) that serves as both lubricant and hydraulic medium. ATF degrades over time, especially under heat, causing shifting problems and eventually internal damage.</p>

<h2>How Often Should You Service Your Automatic Transmission?</h2>
<p>Recommendations vary by manufacturer, but a common guideline for automatic transmissions in Perth's conditions is:</p>
<ul>
  <li><strong>Standard service</strong> — every 60,000–80,000 km (fluid and filter change)</li>
  <li><strong>Hard use / towing / off-road</strong> — every 40,000–50,000 km</li>
  <li><strong>CVT transmissions (common in smaller cars)</strong> — every 40,000–60,000 km with CVT-specific fluid</li>
</ul>
<p>Some manufacturers claim "lifetime fluid" — this is marketing, not reality. Fluid degrades, and in Perth's heat it degrades faster.</p>

<h2>Warning Signs Your Transmission Needs Attention</h2>
<ul>
  <li>Slipping gears — engine revs rise but the car doesn't accelerate proportionally</li>
  <li>Delayed engagement — pause between shifting from Park to Drive</li>
  <li>Rough or jerky gear changes</li>
  <li>Shuddering at highway speeds (common in worn CVTs)</li>
  <li>Transmission warning light</li>
  <li>Dark or burnt-smelling ATF (should be red or pink, not brown-black)</li>
  <li>Fluid leak (red fluid under the car)</li>
</ul>

<h2>What's Involved in a Transmission Service?</h2>
<p>A standard transmission service includes draining the old ATF, replacing the transmission filter (if accessible), cleaning the pan, and refilling with fresh fluid to the correct level. A full flush — using a machine to push all old fluid through — may also be recommended in some cases, though opinion is divided on this approach for high-mileage transmissions.</p>

<h2>Transmission Service Costs in Perth</h2>
<ul>
  <li><strong>Standard drain & refill</strong> — $150–$300</li>
  <li><strong>Full service with filter replacement</strong> — $250–$450</li>
  <li><strong>Machine flush</strong> — $300–$600</li>
</ul>
<p>Prices vary based on vehicle type, ATF required, and workshop. European vehicles and CVTs often cost more due to specialist fluid requirements.</p>

<h2>Don't Wait for Symptoms</h2>
<p>Transmission problems are progressive. What starts as a slight shudder or occasional slip can progress to full gear failure. If your transmission hasn't been serviced in 60,000+ km, booking a service is cheap insurance against an expensive repair.</p>"""
    },
    {
        "slug": "blog-fuel-economy-tips-perth",
        "title": "Improve Fuel Economy: Mechanic Tips for Perth Drivers",
        "tag": "Money",
        "read_time": 5,
        "excerpt": "Perth's sprawling layout means most drivers cover serious kilometres. These mechanic-backed tips can meaningfully improve your fuel economy without changing how you drive.",
        "h1": "Improve Fuel Economy: Mechanic Tips for Perth Drivers",
        "meta": "Fuel economy tips for Perth drivers — find out how car maintenance and driving habits can reduce your fuel costs significantly in WA.",
        "content": """<p>With Perth's urban sprawl and fuel prices consistently among the highest in Australia, improving fuel economy is one of the most practical things a Perth driver can do. The good news: most of the biggest gains come from basic maintenance, not expensive upgrades.</p>

<h2>1. Check Your Tyre Pressure</h2>
<p>Under-inflated tyres increase rolling resistance, which means your engine works harder and burns more fuel. Research suggests tyres 20% under-inflated increase fuel consumption by around 5%. Perth's temperature swings — cold mornings, scorching afternoons — affect tyre pressure, so check monthly. Correct pressures are listed in your fuel cap or door jamb sticker.</p>

<h2>2. Service Your Air Filter</h2>
<p>A clogged air filter restricts airflow to the engine, forcing it to burn more fuel to maintain power. In Perth's dusty conditions — especially if you do any unsealed road driving — air filters can clog faster than manufacturer intervals suggest. Inspect annually and replace when dirty. Typically $20–$60 in parts.</p>

<h2>3. Use the Right Engine Oil</h2>
<p>Using a thicker oil than specified increases friction inside the engine, reducing efficiency. Always use the manufacturer-specified viscosity grade. Switching from a 10W-40 to the correct 5W-30, for example, can improve fuel economy by 1–2%.</p>

<h2>4. Replace Worn Spark Plugs</h2>
<p>Worn spark plugs cause incomplete combustion — your engine burns fuel less efficiently. Replacing spark plugs at the recommended interval (typically 30,000–100,000 km depending on type) can restore fuel economy to near-new levels.</p>

<h2>5. Fix a Failing Oxygen Sensor</h2>
<p>A faulty oxygen sensor causes the engine to run rich (too much fuel). A bad O2 sensor can reduce fuel economy by 20–40%. It's also one of the most common causes of an engine warning light. Replacement costs $150–$350 and pays for itself quickly in fuel savings.</p>

<h2>6. Check for Dragging Brakes</h2>
<p>Brakes that don't fully release add constant resistance. You might not feel it when driving, but your engine is fighting against it constantly. Signs include one wheel feeling hotter than others after driving, or the car pulling to one side.</p>

<h2>7. Keep Up With Logbook Servicing</h2>
<p>A well-maintained engine runs more efficiently than a neglected one. Fresh oil, a clean fuel system, correct ignition timing, and functioning sensors all contribute to better fuel economy. Skipping services to save money often costs more in fuel over time.</p>

<h2>8. Reduce Unnecessary Weight</h2>
<p>Every 50 kg of extra weight in your vehicle increases fuel consumption by roughly 1%. Clear out your boot — don't carry tools, sports equipment, or gear you don't need for that trip.</p>

<h2>9. Combine Trips</h2>
<p>Cold engines burn significantly more fuel than warm ones. Combining several short errands into one trip rather than multiple cold starts can meaningfully reduce your weekly fuel bill — especially relevant for Perth's sprawling suburb layout.</p>

<h2>Get a Fuel Economy Inspection</h2>
<p>If your fuel economy has noticeably worsened, a Perth mechanic can run diagnostics to identify the cause. Don't accept high fuel costs as normal — often the cause is fixable and the savings quickly recoup the repair cost.</p>"""
    },
    {
        "slug": "blog-spark-plugs-perth",
        "title": "Spark Plugs: When to Replace & What It Costs in Perth",
        "tag": "Maintenance",
        "read_time": 4,
        "excerpt": "Spark plugs are small but critical. Worn plugs cause misfires, poor fuel economy, and hard starting. Here's what Perth drivers need to know about spark plug replacement.",
        "h1": "Spark Plugs: When to Replace & What It Costs in Perth",
        "meta": "When should you replace spark plugs in Perth? Learn the signs of worn plugs, service intervals for different plug types, and typical replacement costs.",
        "content": """<p>Spark plugs are often overlooked in routine maintenance — they're small, hidden under covers, and tend to fail gradually rather than suddenly. But worn spark plugs can cause rough running, misfires, poor fuel economy, and hard starting. Replacing them at the right interval keeps your engine running cleanly.</p>

<h2>What Do Spark Plugs Do?</h2>
<p>Spark plugs ignite the air-fuel mixture in your engine's combustion chambers. Each plug fires thousands of times per minute. Over time, the electrode erodes, the gap widens, and the plug requires more voltage to fire — eventually causing misfires.</p>

<h2>How Long Do Spark Plugs Last?</h2>
<p>Service life depends heavily on the plug type:</p>
<ul>
  <li><strong>Copper spark plugs</strong> — 30,000–40,000 km (less common in modern vehicles)</li>
  <li><strong>Platinum spark plugs</strong> — 60,000–80,000 km</li>
  <li><strong>Iridium spark plugs</strong> — 100,000–120,000 km (most modern vehicles)</li>
</ul>
<p>Check your owner's manual for the specified interval and plug type. Using the wrong plug type can cause performance issues.</p>

<h2>Signs Your Spark Plugs Need Replacing</h2>
<ul>
  <li>Rough idling or engine vibration</li>
  <li>Hesitation or stumbling during acceleration</li>
  <li>Poor fuel economy</li>
  <li>Hard starting — especially on cold Perth winter mornings</li>
  <li>Engine warning light (misfires trigger fault codes)</li>
  <li>Engine misfires under load</li>
</ul>

<h2>What's Involved in Spark Plug Replacement?</h2>
<p>On straightforward engines (inline 4-cylinders with easy access), spark plug replacement takes 30–60 minutes. On V6 and V8 engines, or those with tight engine bays, it can take 2–4 hours due to access difficulty. European vehicles with coil packs integrated into the plug wells add complexity.</p>

<h2>Spark Plug Replacement Cost in Perth</h2>
<ul>
  <li><strong>4-cylinder engine</strong> — $80–$200 parts and labour</li>
  <li><strong>6-cylinder engine</strong> — $150–$350</li>
  <li><strong>V8 engine</strong> — $200–$450</li>
</ul>
<p>Iridium plugs cost more than copper or platinum in parts, but their longer lifespan typically makes them better value. Labour rates in Perth range from $100–$180 per hour depending on the workshop.</p>

<h2>Ignition Coils</h2>
<p>Spark plugs work with ignition coils. If a coil fails, the plug it serves won't fire — causing a cylinder misfire. Coil failure is common in older vehicles and often triggers a specific fault code. When replacing plugs on a high-mileage vehicle, it's worth having coils tested at the same time.</p>

<h2>Book Your Spark Plug Service in Perth</h2>
<p>If your car is overdue for a spark plug change or you're experiencing any of the symptoms above, a Perth mechanic can inspect and replace plugs quickly. It's one of the best value maintenance items you can do for engine performance and fuel economy.</p>"""
    },
    {
        "slug": "blog-coolant-flush-perth",
        "title": "Coolant Flush Perth: What Is It & When Do You Need One?",
        "tag": "Maintenance",
        "read_time": 4,
        "excerpt": "Engine coolant doesn't last forever. As it degrades, it becomes acidic and starts corroding your cooling system from the inside. Here's when Perth drivers need a coolant flush.",
        "h1": "Coolant Flush Perth: What Is It & When Do You Need One?",
        "meta": "Engine coolant needs replacing on a schedule. Find out when to do a coolant flush in Perth, what's involved, and why ignoring it leads to expensive repairs.",
        "content": """<p>Engine coolant (antifreeze) does two jobs: it keeps your engine from overheating in Perth's summer heat, and it prevents corrosion inside your cooling system. Over time, the corrosion inhibitors in the coolant deplete, and the fluid becomes acidic — quietly attacking your radiator, water pump, and hoses from the inside.</p>

<h2>What Is a Coolant Flush?</h2>
<p>A coolant flush (also called a radiator flush) involves draining the old coolant, flushing the system with clean water or a cleaning agent to remove scale and deposits, and refilling with fresh coolant to the correct concentration. It's different from simply "topping up" the coolant reservoir — that just adds fluid without removing the degraded stuff.</p>

<h2>How Often Should You Flush Your Coolant?</h2>
<p>Service intervals depend on the coolant type in your vehicle:</p>
<ul>
  <li><strong>Green/blue conventional coolant</strong> — every 2 years or 40,000–50,000 km</li>
  <li><strong>Red/pink OAT (Organic Acid Technology) coolant</strong> — every 5 years or 150,000 km</li>
  <li><strong>Yellow/gold HOAT coolant</strong> — every 5 years (common in European vehicles)</li>
</ul>
<p>Check your owner's manual for the correct type. Mixing coolant types can cause chemical reactions that accelerate corrosion — always use the manufacturer-specified fluid.</p>

<h2>Signs Your Coolant Needs Replacing</h2>
<ul>
  <li>Coolant is rust-coloured, brown, or milky instead of bright green/red/yellow</li>
  <li>Visible debris or scale floating in the overflow tank</li>
  <li>Temperature gauge running higher than normal</li>
  <li>Heater performance has deteriorated</li>
  <li>Coolant needs frequent top-ups (may indicate a leak or burning)</li>
  <li>Last coolant change was more than 5 years ago</li>
</ul>

<h2>Perth's Climate and Your Cooling System</h2>
<p>Perth's summers push cooling systems hard. Ambient temperatures of 40°C+ mean your radiator has to work significantly harder to dissipate engine heat. A cooling system running degraded coolant under these conditions is at elevated risk of overheating. Proactive coolant maintenance is even more important here than in cooler climates.</p>

<h2>What Does a Coolant Flush Cost in Perth?</h2>
<p>A coolant flush in Perth typically costs $100–$200 including fluid and labour, depending on the vehicle's coolant capacity and the type of coolant required. Some larger 4WD engines require more coolant volume, which increases the cost slightly. European vehicles requiring OEM-spec coolant can cost more in parts.</p>

<h2>Coolant Leaks vs Coolant Degradation</h2>
<p>If you're regularly topping up your coolant, there's a leak that needs fixing — not just topping up. Coolant can leak externally (visible drips or stains under the car), or internally through a failing head gasket (appears as white smoke from the exhaust or milky oil). Neither should be ignored.</p>

<h2>Book a Cooling System Service in Perth</h2>
<p>If your coolant is overdue for a change or you're heading into another Perth summer with an ageing cooling system, get a coolant flush booked. It's inexpensive compared to a head gasket repair or water pump replacement caused by a corroded system.</p>"""
    },
    {
        "slug": "blog-used-car-buying-perth",
        "title": "Buying a Used Car in Perth? Get a Pre-Purchase Inspection First",
        "tag": "Advice",
        "read_time": 5,
        "excerpt": "Perth's used car market is active — and so are sellers hiding problems. A pre-purchase inspection from an independent mechanic is the smartest $150 you'll spend before signing anything.",
        "h1": "Buying a Used Car in Perth? Get a Pre-Purchase Inspection First",
        "meta": "Before buying a used car in Perth, get an independent pre-purchase inspection. Find out what's checked, what it costs, and how it protects you from expensive surprises.",
        "content": """<p>Perth's used car market has never been more active — private sales, dealer lots, and online platforms all compete for buyers. With vehicles transacted at $5,000 to $50,000+, a pre-purchase inspection from an independent mechanic is one of the best decisions you can make before handing over any money.</p>

<h2>What Is a Pre-Purchase Inspection?</h2>
<p>A pre-purchase inspection (PPI) is an independent mechanical assessment of a vehicle you're considering buying. You engage a mechanic — separate from the seller — to inspect the car thoroughly and give you an honest report on its condition. The key word is "independent": a mechanic with no relationship to the seller has no incentive to hide problems.</p>

<h2>What's Covered in a Pre-Purchase Inspection?</h2>
<p>A thorough PPI in Perth typically covers:</p>
<ul>
  <li><strong>Body and paint</strong> — evidence of past accidents, panel repairs, mismatched paint</li>
  <li><strong>Underbody and chassis</strong> — rust, accident damage, oil leaks</li>
  <li><strong>Engine</strong> — oil condition, coolant condition, leaks, sounds, smoke at startup</li>
  <li><strong>Transmission</strong> — fluid condition, gear changes, smooth operation</li>
  <li><strong>Brakes</strong> — pad depth, rotor condition, calipers</li>
  <li><strong>Suspension and steering</strong> — worn bushings, play in joints, shock absorber condition</li>
  <li><strong>Tyres</strong> — tread depth, uneven wear (which signals alignment or suspension issues)</li>
  <li><strong>Electrical systems</strong> — lights, air conditioning, windows, instruments</li>
  <li><strong>OBD diagnostic scan</strong> — reading stored fault codes even if no warning light is visible</li>
  <li><strong>Logbook review</strong> — service history verification</li>
</ul>

<h2>How Much Does a Pre-Purchase Inspection Cost in Perth?</h2>
<p>Expect to pay $150–$250 for a comprehensive inspection in Perth. Some workshops charge at the lower end for a visual inspection, more for a full inspection including a hoist and diagnostic scan. It's worth paying for the thorough version.</p>

<h2>Can the Seller Refuse?</h2>
<p>A private seller can technically refuse a PPI — and that itself is a red flag. Any seller who won't allow an independent inspection to be conducted has something to hide. Walk away. There are plenty of good used cars in Perth.</p>
<p>Licensed dealers are required to allow reasonable inspections under Australian Consumer Law.</p>

<h2>REVS and PPSR Checks</h2>
<p>A pre-purchase inspection assesses mechanical condition — but separately, you should also run a PPSR (Personal Property Securities Register) check to confirm the vehicle isn't listed as stolen, hasn't been written off, or has money owing against it. PPSR checks cost around $2 through the government portal.</p>

<h2>Common Problems Found in Perth Used Cars</h2>
<p>Perth's conditions create some specific issues to watch for:</p>
<ul>
  <li>Rust on vehicles from coastal suburbs (Fremantle, Scarborough, Cottesloe)</li>
  <li>Heat-damaged rubber seals and hoses on older vehicles</li>
  <li>Flood damage — relevant after Perth storms and if a vehicle has interstate history</li>
  <li>High-mileage wear on vehicles used for FIFO and long regional drives</li>
</ul>

<h2>The $150 Insurance Policy</h2>
<p>Think of a PPI as a $150 insurance policy against a potential $3,000–$10,000 repair bill. It also gives you negotiating power — a legitimate problem found in an inspection often results in a price reduction that more than covers the cost of the inspection itself.</p>
<p>Book your pre-purchase inspection with a Perth mechanic before you sign any contracts or hand over a deposit.</p>"""
    },
    {
        "slug": "blog-power-steering-problems",
        "title": "Power Steering Problems: Warning Signs & Repair Costs Perth",
        "tag": "Repairs",
        "read_time": 4,
        "excerpt": "Whether you have hydraulic or electric power steering, problems show up as heavy steering, noise, or a warning light. Here's what Perth drivers need to know.",
        "h1": "Power Steering Problems: Warning Signs & Repair Costs Perth",
        "meta": "Power steering problems in Perth — identify warning signs of hydraulic or electric power steering failure, and what repairs cost at a Perth mechanic.",
        "content": """<p>Power steering makes parking and low-speed manoeuvring effortless. When it starts failing, you'll notice quickly — steering becomes heavy, noisy, or unpredictable. Here's how to recognise power steering problems early and what to do about them in Perth.</p>

<h2>Hydraulic vs Electric Power Steering</h2>
<p>Older vehicles (generally pre-2010) use <strong>hydraulic power steering (HPS)</strong>, which relies on power steering fluid pressurised by a pump driven by the engine. Newer vehicles increasingly use <strong>electric power steering (EPS)</strong>, which uses a motor rather than hydraulic fluid — simpler in some respects, but with its own failure modes.</p>

<h2>Warning Signs of Power Steering Problems</h2>
<ul>
  <li><strong>Heavy or stiff steering</strong> — especially at low speeds or when parking</li>
  <li><strong>Whining or groaning noise</strong> when turning (hydraulic systems) — usually indicates low fluid or a failing pump</li>
  <li><strong>Jerky steering response</strong> — inconsistent assistance</li>
  <li><strong>Power steering warning light</strong> — primarily in EPS-equipped vehicles</li>
  <li><strong>Steering wheel vibrating</strong> or feeling loose</li>
  <li><strong>Fluid leak</strong> — power steering fluid is typically clear to light brown and found near the pump or rack</li>
</ul>

<h2>Common Hydraulic Power Steering Problems</h2>
<ul>
  <li><strong>Low fluid level</strong> — check the reservoir under the bonnet; low fluid often indicates a leak</li>
  <li><strong>Failing power steering pump</strong> — the most common HPS failure; causes noise and loss of assist</li>
  <li><strong>Rack and pinion leak</strong> — the steering rack develops a leak, causing loss of fluid and assist</li>
  <li><strong>Power steering hose leak</strong> — high-pressure hoses crack with age</li>
</ul>

<h2>Common Electric Power Steering Problems</h2>
<ul>
  <li><strong>EPS motor failure</strong> — rare but expensive</li>
  <li><strong>Torque sensor failure</strong> — the sensor that reads steering input malfunctions</li>
  <li><strong>Software/ECU fault</strong> — sometimes resolved by a software update from the dealer</li>
  <li><strong>Wiring fault</strong> — corrosion or damaged connectors affecting the EPS motor</li>
</ul>

<h2>Can You Drive With Power Steering Problems?</h2>
<p>You can physically drive without power steering — vehicles were driven without it for decades. But it's harder work, especially at low speeds, and if there's an underlying fault, the condition will likely worsen. Don't ignore a power steering warning light or progressive loss of assist.</p>

<h2>Power Steering Repair Costs in Perth</h2>
<ul>
  <li><strong>Fluid top-up and leak inspection</strong> — $50–$100</li>
  <li><strong>Power steering pump replacement</strong> — $400–$900 parts and labour</li>
  <li><strong>Steering rack replacement</strong> — $600–$1,500+</li>
  <li><strong>EPS motor replacement</strong> — $500–$1,200 (varies significantly by vehicle)</li>
</ul>

<h2>Book a Power Steering Inspection in Perth</h2>
<p>If your steering is feeling heavier than usual or you're hearing unfamiliar noises when turning, have it inspected before the problem progresses. A failing power steering pump or rack leak won't repair itself, and the cost generally increases the longer you leave it.</p>"""
    },
    {
        "slug": "blog-mechanic-morley",
        "title": "Mechanic in Morley: North-East Perth Driver's Guide",
        "tag": "Suburb",
        "read_time": 4,
        "excerpt": "Morley is one of Perth's busiest north-eastern suburbs with a large and diverse vehicle mix. Here's what Morley drivers need to know about getting their car serviced locally.",
        "h1": "Mechanic in Morley: North-East Perth Driver's Guide",
        "meta": "Looking for a mechanic in Morley? Find out what car services Morley drivers use most, what to expect from local workshops, and tips for choosing the right mechanic.",
        "content": """<p>Morley sits at the heart of Perth's north-eastern suburbs — a busy, diverse area with a mix of families, tradies, and commuters who collectively put serious kilometres on their vehicles. Whether you're driving the Reid Highway to work, tackling the school run, or running a small business fleet, having a reliable local mechanic is essential.</p>

<h2>Common Vehicle Types in Morley</h2>
<p>Morley's vehicle mix reflects its demographics — a blend of family SUVs, utes, hatchbacks, and older sedans. Many residents commute to the CBD via Tonkin Highway or Wanneroo Road, while others head east toward Midland or south to Cannington. High-kilometre driving is common, making regular servicing especially important.</p>

<h2>Services Morley Drivers Use Most</h2>
<ul>
  <li>Logbook servicing for family vehicles (Toyota, Honda, Mazda, Hyundai)</li>
  <li>Brake and suspension work on utes and 4WDs</li>
  <li>Air conditioning service ahead of summer</li>
  <li>Tyre replacement and wheel alignment</li>
  <li>Pre-purchase inspections on used cars</li>
</ul>

<h2>What to Look for in a Morley Mechanic</h2>
<p>When choosing a mechanic in or near Morley, look for:</p>
<ul>
  <li><strong>Licensed technicians</strong> — look for MTA-affiliated or ARC-licensed (for air conditioning work) workshops</li>
  <li><strong>Clear pricing</strong> — any reputable workshop will provide a written quote before starting work</li>
  <li><strong>Google Reviews</strong> — a consistent track record of recent positive reviews is a good signal</li>
  <li><strong>Make experience</strong> — if you drive a specific brand, find a mechanic with experience on your make</li>
</ul>

<h2>Proximity to Key Areas</h2>
<p>Morley is well-positioned for accessing workshops in surrounding areas — Bayswater, Noranda, Bassendean, and Dianella are all within a short drive, giving residents a broad selection of mechanical workshops to choose from.</p>

<h2>Logbook Servicing in Morley</h2>
<p>Keeping your logbook stamped is essential for maintaining manufacturer warranty and maximising resale value. A local Morley mechanic can perform logbook services using genuine or OEM-equivalent parts that meet your manufacturer's specifications — at a significantly lower cost than dealer servicing.</p>

<h2>Book a Mechanic Service Near Morley</h2>
<p>Perth Mechanic services the Morley area and surrounding north-east Perth suburbs. Whether you need a routine service, unexpected repair, or a pre-purchase inspection, get a quote today and get your car booked in.</p>"""
    },
    {
        "slug": "blog-mechanic-cannington",
        "title": "Mechanic in Cannington: South Perth Driver's Guide",
        "tag": "Suburb",
        "read_time": 4,
        "excerpt": "Cannington is one of Perth's most important southern commercial hubs. Here's what Cannington drivers and nearby residents need to know about local mechanic services.",
        "h1": "Mechanic in Cannington: South Perth Driver's Guide",
        "meta": "Looking for a mechanic in Cannington? Find out what services are most in demand in Perth's southern commercial hub and how to choose the right workshop.",
        "content": """<p>Cannington is one of Perth's most significant southern commercial centres — home to Westfield Carousel, a busy retail strip, and a large industrial area stretching toward Beckenham and Bentley. It's also a major thoroughfare for commuters heading between the hills and the city via Albany Highway and Orrong Road.</p>

<h2>Vehicle Types Common in Cannington</h2>
<p>Cannington sees a wide cross-section of vehicles. Tradies heading to and from the southern suburbs, families running the school run to nearby suburbs, and commuters logging significant kilometres on busy corridors like Albany Highway and Leach Highway. The area also has a significant used car market, making pre-purchase inspections a common service request.</p>

<h2>Most In-Demand Services in Cannington</h2>
<ul>
  <li>Log book services for family sedans and SUVs</li>
  <li>Brake inspections and replacements — Albany Highway is hard on brakes</li>
  <li>Tyre replacement and wheel alignment</li>
  <li>Air conditioning regas ahead of summer</li>
  <li>Rego inspection readiness checks</li>
  <li>Pre-purchase inspections for the active local used car market</li>
</ul>

<h2>Why Independent Mechanics vs Dealerships in Cannington</h2>
<p>Cannington has several dealerships along its main strips, but independent mechanics generally offer more competitive pricing for routine servicing — often 20–40% less than dealer rates for the same work. Under Australian Consumer Law, using an independent mechanic does not void your vehicle warranty, provided the correct parts and fluids are used and the service is documented.</p>

<h2>Choosing a Mechanic Near Cannington</h2>
<p>Look for workshops that:</p>
<ul>
  <li>Provide written quotes before work starts</li>
  <li>Have strong local Google reviews from the past 12 months</li>
  <li>Are licensed (check for MTA WA membership)</li>
  <li>Offer clear communication about what was found and what was done</li>
</ul>

<h2>Nearby Areas Served</h2>
<p>Residents in Beckenham, Bentley, St James, Queens Park, and East Cannington are all conveniently located for accessing Cannington-area workshops. The Carousel area in particular has a concentration of automotive service businesses.</p>

<h2>Book a Service Near Cannington</h2>
<p>Perth Mechanic services Cannington and surrounding south-east Perth suburbs. Get a quote online or call to book your next service, repair, or inspection.</p>"""
    },
    {
        "slug": "blog-mechanic-victoria-park",
        "title": "Mechanic in Victoria Park: Inner South-East Perth Guide",
        "tag": "Suburb",
        "read_time": 4,
        "excerpt": "Victoria Park's dense inner-suburb location and mix of young professionals and established families creates a specific set of car servicing needs. Here's what you need to know.",
        "h1": "Mechanic in Victoria Park: Inner South-East Perth Guide",
        "meta": "Looking for a mechanic in Victoria Park? Find out what services inner south-east Perth drivers use most and how to find a reliable local workshop.",
        "content": """<p>Victoria Park — or Vic Park as locals call it — sits just a few kilometres from the CBD, offering residents easy city access while maintaining a vibrant local culture. Its dense population of young professionals, families, and long-term residents creates a broad range of vehicle servicing needs.</p>

<h2>Vehicle Mix in Victoria Park</h2>
<p>Victoria Park tends toward smaller vehicles — hatchbacks, small SUVs, and city cars that suit its urban setting and compact street parking. Older homes mean some residents run older vehicles that need more frequent maintenance. There's also a reasonable share of prestige and European vehicles among the suburb's professional demographic.</p>

<h2>Common Services for Victoria Park Residents</h2>
<ul>
  <li>Logbook servicing for Asian and European brands</li>
  <li>City driving wear repairs — brakes, tyres, and suspension take a beating in stop-start traffic</li>
  <li>Air conditioning service — essential in Perth's summers</li>
  <li>Battery testing and replacement — heat-related battery failures are common</li>
  <li>Diagnostic checks for warning lights</li>
  <li>Pre-purchase inspections for the local used car market</li>
</ul>

<h2>Inner-Suburb Mechanic Options</h2>
<p>Victoria Park itself has some local workshops, with more options available in adjacent suburbs — Burswood, East Perth, St James, and Carlisle. Given its inner-city location, residents have good access to a range of workshop types from budget to premium.</p>

<h2>European Vehicle Servicing</h2>
<p>For residents running European brands (BMW, Mercedes, Volkswagen, Audi, Volvo), finding a mechanic with European vehicle experience is worthwhile. Independent European specialists typically charge significantly less than dealership rates while using manufacturer-approved processes.</p>

<h2>Parking and Urban Logistics</h2>
<p>If leaving your car at a workshop is logistically challenging due to Victoria Park's urban density, look for workshops that offer drop-off and collection services or have a loaner car option — some Perth mechanics offer this for longer jobs.</p>

<h2>Book a Mechanic Near Victoria Park</h2>
<p>Perth Mechanic services Victoria Park and surrounding inner south-east Perth suburbs. Get in touch for a quote on your next service or repair — no obligation, same-day responses.</p>"""
    },
    {
        "slug": "blog-mechanic-mandurah",
        "title": "Mechanic in Mandurah: What Drivers in Perth's South Should Know",
        "tag": "Suburb",
        "read_time": 4,
        "excerpt": "Mandurah is 75 km south of Perth but has its own thriving automotive service scene. Here's what Mandurah residents should know about car servicing and mechanical repairs.",
        "h1": "Mechanic in Mandurah: What Drivers in Perth's South Should Know",
        "meta": "Looking for a mechanic in Mandurah? Find out what car services Mandurah and Peel region drivers use most and how to choose the right local workshop.",
        "content": """<p>Mandurah sits at the edge of the Peel region, 75 km south of Perth, and has grown significantly over the past two decades into a city in its own right. With a population approaching 100,000 and a mix of retirees, young families, FIFO workers, and commuters, Mandurah's automotive servicing needs are diverse.</p>

<h2>The Mandurah Commuter</h2>
<p>Many Mandurah residents work in Perth, making the daily drive on the Kwinana Freeway or the Mandurah train one of their defining activities. Those who drive put significant kilometres on their vehicles — 30,000–40,000+ km per year is not unusual for committed commuters. This level of use demands strict adherence to service intervals.</p>

<h2>Common Servicing Needs in Mandurah</h2>
<ul>
  <li>High-mileage logbook services</li>
  <li>Tyre replacement — freeway driving wears tyres differently than city driving</li>
  <li>Brake inspections — long freeway runs require effective brakes, especially in wet winter conditions</li>
  <li>Air conditioning service — Mandurah's summers are hot and humid near the estuary</li>
  <li>4WD and boat vehicle servicing — Mandurah's coastal lifestyle means many residents run 4WDs and tow boat trailers</li>
</ul>

<h2>4WD and Towing in Mandurah</h2>
<p>Boating, fishing, and beach access are central to life in Mandurah. Vehicles used for towing — whether a boat, caravan, or horse float — require additional attention to transmission servicing, tow bar electrics, and brake wear. Salt air exposure from coastal locations also accelerates corrosion on brake components and undercarriage.</p>

<h2>Finding a Mechanic in Mandurah</h2>
<p>Mandurah has a well-developed local automotive service industry — you won't need to drive to Perth for most servicing needs. Look for workshops that:</p>
<ul>
  <li>Specifically mention experience with your vehicle make</li>
  <li>Offer ADAS (advanced driver assistance system) calibration if your vehicle has cameras and sensors</li>
  <li>Can handle towing gear and 4WD drivetrain servicing</li>
</ul>

<h2>Coastal Corrosion Watch</h2>
<p>Living near Mandurah's waterways means salt air exposure is a year-round reality for your vehicle's undercarriage. Proactive checks for rust on brake lines, suspension components, and exhaust systems can prevent failures before they become dangerous.</p>

<h2>Book a Service in Mandurah</h2>
<p>Perth Mechanic services the Mandurah and Peel region. Whether you need a routine logbook service, towing-related inspection, or 4WD maintenance, get a quote today.</p>"""
    },
    {
        "slug": "blog-mechanic-balcatta",
        "title": "Mechanic in Balcatta: North Perth Driver's Guide",
        "tag": "Suburb",
        "read_time": 4,
        "excerpt": "Balcatta is one of Perth's key northern commercial and industrial suburbs. Here's what Balcatta residents and nearby drivers need to know about car servicing in the area.",
        "h1": "Mechanic in Balcatta: North Perth Driver's Guide",
        "meta": "Looking for a mechanic in Balcatta? Find out about car servicing options in Perth's northern commercial hub and what to look for in a local workshop.",
        "content": """<p>Balcatta is one of Perth's busiest northern commercial and light industrial suburbs, sitting off the Mitchell Freeway between Stirling and Osborne Park. It's a heavily trafficked area with a mix of trade businesses, retail, and residential streets that feed into major north-south corridors.</p>

<h2>Why Balcatta Has Strong Mechanic Options</h2>
<p>Balcatta's industrial zoning has attracted a wide range of automotive businesses — from tyre and exhaust specialists to full-service mechanical workshops. Residents in nearby suburbs (Stirling, Gwelup, Hamersley, Woodlands) have good access to the range of workshops in the Balcatta precinct.</p>

<h2>Vehicle Mix in Balcatta and Surrounds</h2>
<p>Balcatta's north-Perth location means plenty of tradespeople using utes and vans, families in SUVs, and professionals commuting to Joondalup or the CBD via the Mitchell Freeway. Higher daily kilometres than inner-city suburbs means oil changes and tyre wear come around faster.</p>

<h2>Key Services for Balcatta Drivers</h2>
<ul>
  <li>Logbook services for Toyota, Mazda, Hyundai, Ford, and Holden</li>
  <li>Commercial vehicle and van servicing for trade businesses</li>
  <li>Tyre and wheel alignment services</li>
  <li>Brake inspections — freeway driving takes a toll at merge points and exits</li>
  <li>Fuel system servicing for high-km vehicles</li>
</ul>

<h2>Commercial and Fleet Servicing</h2>
<p>Given Balcatta's industrial character, fleet servicing is in high demand. Local businesses with trade vehicles benefit from workshops that offer scheduled fleet maintenance programs — reducing downtime and keeping vehicles compliant with logbook requirements.</p>

<h2>Choosing a Mechanic in Balcatta</h2>
<ul>
  <li>Look for MTA WA membership — a sign of professional standards</li>
  <li>Check Google Reviews from the last six months</li>
  <li>Ask whether they provide a written quote before starting work</li>
  <li>Confirm they use OEM or equivalent parts to preserve your warranty</li>
</ul>

<h2>Book a Service Near Balcatta</h2>
<p>Perth Mechanic services Balcatta and surrounding north Perth suburbs including Stirling, Gwelup, Hamersley, and Woodlands. Get in touch for a quote on your next service.</p>"""
    },
    {
        "slug": "blog-mechanic-subiaco",
        "title": "Mechanic in Subiaco: Inner West Perth Guide",
        "tag": "Suburb",
        "read_time": 4,
        "excerpt": "Subiaco is one of Perth's most prestigious inner suburbs with a mix of prestige vehicles and everyday family cars. Here's what Subiaco drivers should know about local mechanic options.",
        "h1": "Mechanic in Subiaco: Inner West Perth Guide",
        "meta": "Looking for a mechanic in Subiaco? Find out about car servicing in Perth's prestigious inner-west suburb and what services are most in demand for local drivers.",
        "content": """<p>Subiaco is one of Perth's most vibrant and sought-after inner suburbs — a mix of heritage homes, modern apartments, professional residents, and the buzz of Rokeby Road and the old Subiaco Oval precinct. Its inner-city location means residents have a range of vehicle types and servicing needs.</p>

<h2>Vehicle Mix in Subiaco</h2>
<p>Subiaco's professional demographic means a higher-than-average proportion of European and prestige vehicles — BMW, Mercedes, Audi, Volvo, and Lexus are common on its streets. That said, the suburb also has plenty of everyday vehicles — hatchbacks, small SUVs, and older vehicles that long-term residents have kept for years.</p>

<h2>European Vehicle Servicing in Subiaco</h2>
<p>For prestige and European vehicle owners in Subiaco, finding a mechanic experienced with your make is important. European vehicles often have manufacturer-specific requirements around oil grades, part specifications, and diagnostic software. Independent European specialists in nearby suburbs (Osborne Park, Leederville, West Perth) can handle these requirements at significantly lower cost than dealership servicing.</p>

<h2>Common Services for Subiaco Residents</h2>
<ul>
  <li>Logbook servicing for European and Asian brands</li>
  <li>Air conditioning service and regas</li>
  <li>Battery testing and replacement — heat-related failures are common</li>
  <li>Tyre replacement and alignment</li>
  <li>Diagnostic checks and warning light investigation</li>
  <li>Pre-purchase inspections</li>
</ul>

<h2>City Driving and Brake Wear</h2>
<p>Inner-city driving is harder on brakes than highway driving — frequent stops, traffic lights, and tight parking. Subiaco residents may find their brake pads need more frequent attention than suburban counterparts. If you're hearing a squeal or grind, get brakes inspected promptly.</p>

<h2>Access to Nearby Workshops</h2>
<p>Subiaco itself has limited workshop space due to its residential density, but nearby Osborne Park, Leederville, and West Perth offer a strong selection of mechanical workshops within a short drive. Many offer pickup/drop-off services for inner-suburb residents.</p>

<h2>Book a Mechanic Near Subiaco</h2>
<p>Perth Mechanic services Subiaco and surrounding inner-west Perth suburbs. Get a quote for your next service or repair — European and prestige vehicles welcome.</p>"""
    },
    {
        "slug": "blog-roadworthy-wa-guide",
        "title": "Roadworthy Inspections in WA: Complete Guide for Perth Drivers",
        "tag": "Compliance",
        "read_time": 5,
        "excerpt": "Vehicle inspections in WA work differently from other states. Here's what Perth drivers need to know about licensing inspections, Vehicle Examination Certificates, and keeping your car road-legal.",
        "h1": "Roadworthy Inspections in WA: Complete Guide for Perth Drivers",
        "meta": "Guide to vehicle inspections and roadworthy requirements in WA. Find out when you need a Vehicle Examination Certificate in Perth and what's checked.",
        "content": """<p>Western Australia's vehicle inspection system works differently from other Australian states, and there's often confusion among new residents or people buying and selling cars. Here's a clear breakdown of what's required, when, and who does what.</p>

<h2>WA Doesn't Have a Roadworthy Certificate System</h2>
<p>Unlike Victoria, Queensland, and NSW — which require a Certificate of Roadworthiness or Safety Certificate before a vehicle can change hands — WA does not have a mandatory pre-sale roadworthy system for private sales. In WA, vehicles are sold "as is" unless a Vehicle Examination Certificate is specifically required.</p>

<h2>What Is a Vehicle Examination Certificate (VEC)?</h2>
<p>A Vehicle Examination Certificate (VEC) — sometimes still called a "blue slip" — is a formal inspection issued by a DoT-licensed Vehicle Examination Station. It's required in specific circumstances:</p>
<ul>
  <li>Registering a vehicle in WA that was previously registered interstate</li>
  <li>Re-registering a vehicle that has been unregistered for 3+ months</li>
  <li>Registering a modified vehicle</li>
  <li>Certain older vehicles or rebuild/kit cars</li>
  <li>Heavy vehicles in some categories</li>
</ul>

<h2>Annual Licensing Inspections</h2>
<p>Some vehicle categories require annual safety inspections as part of licensing in WA:</p>
<ul>
  <li>Heavy vehicles and trucks</li>
  <li>Passenger transport vehicles (taxis, rideshare, buses)</li>
  <li>Trailers over certain weight ratings</li>
</ul>
<p>Standard private passenger vehicles do not require annual inspection in WA for registration renewal — this is handled by a remote or in-person check of registration details, not a physical inspection.</p>

<h2>Buying a Used Car in WA</h2>
<p>Because WA doesn't require a pre-sale roadworthy, buyers take on more risk when purchasing used vehicles privately. This makes independent pre-purchase inspections even more important in WA than in other states. A licensed mechanic can assess the vehicle's safety and mechanical condition before you commit to buying.</p>

<h2>What's Inspected in a VEC?</h2>
<p>A Vehicle Examination Certificate inspection covers safety-critical items:</p>
<ul>
  <li>Brakes and brake system</li>
  <li>Steering and suspension</li>
  <li>Lights and electrical systems</li>
  <li>Tyres and wheels</li>
  <li>Body and chassis integrity</li>
  <li>Engine and emissions</li>
  <li>Seatbelts and safety equipment</li>
</ul>

<h2>How to Find a Licensed Vehicle Examination Station</h2>
<p>VECs can only be issued by DoT-licensed Vehicle Examination Stations — not all mechanical workshops are licensed for this. Check the DoT WA website or ask your mechanic if they hold this licence. In Perth, licensed stations are found across all major areas including Osborne Park, Malaga, Cannington, and Fremantle.</p>

<h2>Cost of a VEC in Perth</h2>
<p>A Vehicle Examination typically costs $100–$200 in Perth depending on vehicle type and the workshop's fees. This is separate from any repairs needed to bring the vehicle to standard.</p>

<h2>Stay Road Legal in Perth</h2>
<p>Even without mandatory annual inspections, Perth drivers are responsible for keeping their vehicles roadworthy at all times. A vehicle with faulty brakes, bald tyres, or non-functioning lights is not just illegal — it's dangerous. Regular servicing is your safeguard.</p>"""
    },
]

# Load existing queue
with open(QUEUE_FILE) as f:
    data = json.load(f)

existing_slugs = {item["slug"] for item in data["queue"]}

# Write HTML files and append to queue
added = 0
for post in POSTS:
    slug = post["slug"]
    if slug in existing_slugs:
        print(f"SKIP (already in queue): {slug}")
        continue

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{post['title']} | Perth Mechanic</title>
  <meta name="description" content="{post['meta']}">
  <link rel="canonical" href="https://perthmechanic.com/{slug}.html">
  <link rel="stylesheet" href="css/style.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "{post['h1']}",
    "description": "{post['meta']}",
    "publisher": {{"@type": "Organization", "name": "Perth Mechanic", "url": "https://perthmechanic.com"}},
    "mainEntityOfPage": {{"@type": "WebPage", "@id": "https://perthmechanic.com/{slug}.html"}}
  }}
  </script>
</head>
<body>
<header class="site-header">
  <div class="container header-inner">
    <a href="index.html" class="logo">Perth<span>Mechanic</span></a>
    <button class="hamburger" id="hamburger" aria-label="Open menu">&#9776;</button>
    <nav class="main-nav" id="main-nav">
      <ul>
        <li><a href="index.html">Home</a></li>
        <li><a href="services.html">Services</a></li>
        <li><a href="about.html">About</a></li>
        <li class="nav-active"><a href="blog.html">Blog</a></li>
        <li><a href="contact.html">Contact</a></li>
      </ul>
    </nav>
  </div>
</header>

<main>
  <article class="blog-post-wrap">
    <div class="container blog-post-inner">
      <div class="blog-post-meta"><span class="blog-tag">{post['tag']}</span> &nbsp;&middot;&nbsp; {post['read_time']} min read</div>
      <h1>{post['h1']}</h1>
      <div class="blog-post-body">
        {post['content']}
      </div>
      <div class="blog-cta-box">
        <h3>Need a mechanic in Perth?</h3>
        <p>Get a fast, no-obligation quote from Perth Mechanic. We service all Perth suburbs.</p>
        <a href="contact.html" class="btn">Get a Free Quote</a>
      </div>
      <p style="margin-top:2rem;"><a href="blog.html">&larr; Back to Blog</a></p>
    </div>
  </article>
</main>

<footer class="site-footer">
  <div class="container footer-inner">
    <p>&copy; <span id="yr"></span> Perth Mechanic. All rights reserved.</p>
    <nav class="footer-nav">
      <a href="index.html">Home</a>
      <a href="services.html">Services</a>
      <a href="blog.html">Blog</a>
      <a href="contact.html">Contact</a>
    </nav>
  </div>
</footer>
<script src="js/main.js"></script>
</body>
</html>"""

    path = os.path.join(DRAFTS_DIR, f"{slug}.html")
    with open(path, "w") as f:
        f.write(html)

    data["queue"].append({
        "slug": slug,
        "title": post["title"],
        "tag": post["tag"],
        "read_time": post["read_time"],
        "excerpt": post["excerpt"]
    })
    existing_slugs.add(slug)
    added += 1
    print(f"Created: {slug}.html")

with open(QUEUE_FILE, "w") as f:
    json.dump(data, f, indent=2)

print(f"\nDone. {added} new drafts added. Total queue: {len(data['queue'])} posts.")
