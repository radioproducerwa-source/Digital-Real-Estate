#!/usr/bin/env python3
"""Generate 20 suburb landing pages for Perth Mechanic."""

import os

SUBURBS = [
    {
        "slug": "fremantle",
        "name": "Fremantle",
        "nearby": [("Cottesloe", "cottesloe.html"), ("Cannington", "cannington.html"), ("Victoria Park", "victoria-park.html")],
        "intro": "Fremantle is one of Perth's most vibrant and densely populated inner suburbs, with a large number of older vehicles and a high proportion of renters who rely on local mechanics for servicing and repairs. Mechanics in Fremantle service everything from older European cars near the port precinct to modern family vehicles in the surrounding South Fremantle and Beaconsfield areas. Fremantle drivers are value-conscious and expect transparent pricing — which is exactly what our Fremantle mechanic network delivers.",
        "area": "Fremantle, South Fremantle, Beaconsfield, and surrounding inner western suburbs",
        "local_note": "Many older vehicles in Fremantle require mechanics with experience in European makes — our Fremantle network includes specialists in VW, BMW, and Mercedes alongside Japanese and Korean brands.",
        "faqs": [
            ("How much does a car service cost in Fremantle?", "A minor service in Fremantle typically costs $150–$280. A major service runs $300–$600+ depending on your vehicle. Our Fremantle mechanics provide upfront pricing before any work begins."),
            ("Can I get a logbook service in Fremantle without going to a dealership?", "Yes — under Australian consumer law, any qualified mechanic can perform your logbook service. Our Fremantle mechanics stamp manufacturer logbooks using specified parts and fluids at significantly lower prices than dealerships."),
            ("Do Fremantle mechanics work on European cars?", "Absolutely. Our Fremantle network includes mechanics who specialise in European makes including VW, Audi, BMW, and Mercedes alongside all Japanese and Korean brands."),
            ("How quickly can I get a mechanic in Fremantle?", "For routine services, appointments are typically available within 24–48 hours. For urgent repairs in Fremantle, same-day availability is often possible — contact us and we'll find the fastest option."),
            ("Is there a mobile mechanic in Fremantle?", "For select services including battery replacement and diagnostics, mobile mechanic options may be available in Fremantle. Mention this in your quote request and we'll check availability."),
        ],
    },
    {
        "slug": "joondalup",
        "name": "Joondalup",
        "nearby": [("Morley", "morley.html"), ("Karrinyup", "karrinyup.html"), ("Balcatta", "balcatta.html")],
        "intro": "Joondalup is one of Perth's major northern hubs, home to Edith Cowan University, Lakeside Joondalup Shopping City, and a large, diverse residential population. The northern corridor generates significant demand for mechanical services — from logbook services for new family vehicles to repairs for the many tradies and fleet vehicles operating out of Joondalup. Our Joondalup mechanic network covers the full range of services for all makes and models across the northern suburbs.",
        "area": "Joondalup, Ocean Reef, Currambine, Heathridge, Kinross, and surrounding northern suburbs",
        "local_note": "Joondalup has a high proportion of newer vehicles from families in the northern corridor — our mechanics are well-versed in modern logbook service schedules and warranty requirements.",
        "faqs": [
            ("Where can I get a logbook service in Joondalup?", "Perth Mechanic connects Joondalup drivers with qualified mechanics who perform manufacturer-compliant logbook services — keeping your warranty valid without dealership prices."),
            ("Do mechanics in Joondalup service European cars?", "Yes — our Joondalup network includes mechanics who work on European makes alongside all Japanese, Korean, and American brands."),
            ("How often should I service my car in Joondalup?", "Most vehicles require servicing every 10,000–15,000km or 12 months. Check your manufacturer logbook for the specific schedule for your vehicle."),
            ("Can I get a same-day mechanic in Joondalup?", "For urgent jobs and breakdowns, same-day availability in Joondalup is often possible. Submit your request and note 'URGENT' — we'll prioritise finding an available mechanic."),
            ("What's the average cost of a major service in Joondalup?", "A major service in Joondalup typically costs $350–$600+ depending on your vehicle make and model. Our mechanics provide a firm quote before any work begins."),
        ],
    },
    {
        "slug": "midland",
        "name": "Midland",
        "nearby": [("Morley", "morley.html"), ("Malaga", "malaga.html"), ("Belmont", "belmont.html")],
        "intro": "Midland is the gateway to Perth's Swan Valley and a key commercial and transport hub for the eastern corridor. With a large population of tradies, fleet vehicle operators, and families in surrounding eastern suburbs, Midland generates consistent demand for mechanical services ranging from routine logbook services to fleet maintenance programs. Mechanics in Midland are experienced with the heavy use patterns of the eastern corridor — utes, 4WDs, and commercial vehicles are bread and butter work.",
        "area": "Midland, Bellevue, Swan View, Middle Swan, Stratton, and the broader eastern suburbs corridor",
        "local_note": "Midland mechanics regularly service 4WDs and utes used by tradies and eastern corridor residents — practical, heavy-use vehicles that need experienced hands.",
        "faqs": [
            ("Do mechanics in Midland service 4WDs and utes?", "Yes — Midland mechanics in our network are experienced with 4WDs, dual-cab utes, and light commercial vehicles commonly used by tradies in the eastern corridor."),
            ("Can I get a fleet service in Midland?", "Absolutely. We connect Midland businesses with mechanics who offer scheduled fleet maintenance programs for vehicles of all sizes."),
            ("How much does a logbook service cost in Midland?", "Logbook service costs in Midland vary by vehicle make and model — typically $180–$350. Our mechanics provide a firm upfront quote before any work."),
            ("Is there an auto electrician in Midland?", "Yes — our Midland network includes qualified auto electricians for battery, alternator, ECU diagnostics, and sensor replacement."),
            ("How long does a major service take in Midland?", "A major service typically takes 2–4 hours depending on the vehicle. Most Midland mechanics can complete same-day if you book early."),
        ],
    },
    {
        "slug": "armadale",
        "name": "Armadale",
        "nearby": [("Canning Vale", "canning-vale.html"), ("Cannington", "cannington.html"), ("Thornlie", "thornlie.html")],
        "intro": "Armadale is a rapidly expanding outer suburb in Perth's south-eastern corridor, with new estates growing across Haynes, Harrisdale, and Piara Waters. The suburb's car-dependent layout and growing population create strong ongoing demand for mechanical services — particularly logbook services for the many newer vehicles driven by young families in the new developments. Armadale mechanics serve a diverse mix of vehicles from budget hatchbacks to family SUVs.",
        "area": "Armadale, Haynes, Harrisdale, Piara Waters, Seville Grove, and surrounding south-eastern suburbs",
        "local_note": "Armadale's new housing estates mean many residents drive newer vehicles requiring manufacturer logbook servicing — our Armadale mechanics are familiar with current logbook schedules across all major brands.",
        "faqs": [
            ("Is there a good mechanic in Armadale?", "Perth Mechanic connects Armadale drivers with licensed, insured mechanics who provide transparent pricing and quality workmanship. Submit a quote request and we'll match you with the right mechanic."),
            ("Can I get a logbook service in Armadale without going to a dealership?", "Yes — qualified mechanics in our Armadale network can service your new car and stamp your logbook at a fraction of dealership prices, while keeping your warranty valid."),
            ("Do Armadale mechanics work on hybrids?", "Yes — our network includes mechanics with hybrid vehicle experience, including Toyota Prius, RAV4 Hybrid, and Camry Hybrid."),
            ("How much is a brake repair in Armadale?", "Brake pad replacement in Armadale typically costs $180–$350 for front or rear pads. A full brake job including rotors runs $350–$600+. We provide firm quotes upfront."),
            ("Can I get a tyre fitting in Armadale?", "Absolutely. Our Armadale mechanics stock major tyre brands and can fit and balance new tyres on any vehicle make and model."),
        ],
    },
    {
        "slug": "rockingham",
        "name": "Rockingham",
        "nearby": [("Mandurah", "mandurah.html"), ("Cockburn Central", "cockburn-central.html"), ("Fremantle", "fremantle.html")],
        "intro": "Rockingham's coastal lifestyle and large residential population make it one of Perth's most active southern markets for mechanical services. With HMAS Stirling on Garden Island nearby, a significant Defence Housing community adds to demand — and Defence Housing properties tend to have specific vehicle maintenance requirements. Rockingham mechanics are well-experienced with the full range of family and fleet vehicles common across the southern coastal corridor.",
        "area": "Rockingham, Safety Bay, Shoalwater, Port Kennedy, Waikiki, and the broader City of Rockingham",
        "local_note": "Rockingham has a large Defence Housing community with vehicles that are well-used and require regular professional servicing — our Rockingham mechanics understand fleet and family vehicle maintenance programs.",
        "faqs": [
            ("Do Rockingham mechanics service Defence Housing vehicles?", "Yes — our Rockingham network has experience with Defence-adjacent fleet vehicle servicing and individual service members' personal vehicles."),
            ("Where can I get a pre-purchase inspection in Rockingham?", "Our Rockingham mechanics provide full pre-purchase inspection reports including mechanical and body assessments — essential before buying any used vehicle."),
            ("How much does an AC re-gas cost in Rockingham?", "An air conditioning re-gas in Rockingham typically costs $120–$200 depending on refrigerant type and system condition. Perth summers make this a priority — don't wait until your AC fails entirely."),
            ("Can I get a same-day service in Rockingham?", "For urgent repairs, same-day availability in Rockingham is often possible. Submit a quote request noting the urgency and we'll find the fastest available option."),
            ("Do Rockingham mechanics do wheel alignments?", "Yes — wheel alignment is available through our Rockingham network. Proper alignment extends tyre life significantly and improves handling and fuel economy."),
        ],
    },
    {
        "slug": "mandurah",
        "name": "Mandurah",
        "nearby": [("Rockingham", "rockingham.html"), ("Cockburn Central", "cockburn-central.html"), ("Armadale", "armadale.html")],
        "intro": "Mandurah is WA's second-largest city, sitting on the Peel Inlet 70km south of Perth. With a large and growing residential population, significant canal and waterfront developments, and a high per-capita car ownership rate, Mandurah generates strong demand for all categories of mechanical services. Mandurah mechanics in our network cover everything from routine logbook services to fleet maintenance programs for local businesses.",
        "area": "Mandurah, Halls Head, Falcon, Dudley Park, Lakelands, and the broader Peel region",
        "local_note": "Mandurah's coastal environment means salt-related corrosion can affect vehicles — our mechanics check for corrosion on brake lines, exhaust components, and suspension parts as part of routine inspections.",
        "faqs": [
            ("Are there qualified mechanics in Mandurah?", "Yes — Perth Mechanic has a network of licensed mechanics in Mandurah covering logbook services, repairs, brakes, tyres, and more."),
            ("How much does a car service cost in Mandurah?", "A minor service in Mandurah costs approximately $150–$280. A major service runs $300–$600+. Our mechanics provide upfront pricing before any work begins."),
            ("Can Mandurah mechanics service European cars?", "Yes — our Mandurah network includes mechanics experienced with European, Japanese, Korean, and Australian vehicles."),
            ("Is same-day emergency mechanical service available in Mandurah?", "For urgent breakdowns in Mandurah, same-day service is often available. Contact us with your location and we'll prioritise finding an available mechanic."),
            ("Do Mandurah mechanics offer logbook servicing?", "Yes — our Mandurah mechanics perform manufacturer-compliant logbook services that keep your new car warranty valid without the dealership price premium."),
        ],
    },
    {
        "slug": "canning-vale",
        "name": "Canning Vale",
        "nearby": [("Cannington", "cannington.html"), ("Armadale", "armadale.html"), ("Thornlie", "thornlie.html")],
        "intro": "Canning Vale is one of Perth's largest southern suburbs, combining established residential streets with significant industrial and commercial areas. The suburb's location within the City of Canning makes it a hub for light industrial businesses and fleet operators — and the residential population drives steady demand for family vehicle servicing. Canning Vale mechanics in our network work across both passenger vehicles and light commercial vehicles.",
        "area": "Canning Vale, Willetton, Riverton, and surrounding southern suburbs in the City of Canning",
        "local_note": "Canning Vale's industrial precincts house many small business fleets — our mechanic network offers fleet servicing programs that minimise downtime for local businesses.",
        "faqs": [
            ("Is there a mechanic near Canning Vale?", "Yes — Perth Mechanic has qualified mechanics available throughout Canning Vale and surrounding southern suburbs. Submit a request for a same-day quote."),
            ("Can I get fleet servicing in Canning Vale?", "Absolutely. Our Canning Vale mechanic network offers scheduled fleet maintenance programs for local businesses with vehicles of all types."),
            ("How much does a logbook service cost in Canning Vale?", "Logbook service costs in Canning Vale are typically $180–$350 depending on your vehicle. Our mechanics stamp your logbook using manufacturer-specified parts."),
            ("Do Canning Vale mechanics do tyre fitting?", "Yes — our mechanics stock major tyre brands and can fit and balance tyres on all vehicles. Wheel alignment is also available."),
            ("How quickly can I get a mechanic in Canning Vale?", "For routine services, appointments are available within 24–48 hours. Urgent repairs often have same-day availability. Submit your request and note any urgency."),
        ],
    },
    {
        "slug": "cannington",
        "name": "Cannington",
        "nearby": [("Victoria Park", "victoria-park.html"), ("Canning Vale", "canning-vale.html"), ("Thornlie", "thornlie.html")],
        "intro": "Cannington is one of Perth's busiest automotive suburbs, anchored by Westfield Carousel and well-known as a hub for car dealerships and mechanic workshops. The suburb's central location and excellent road access make it a natural draw for drivers from across the southern corridor seeking mechanical services. Cannington mechanics in our network compete on quality and price — not dealership overheads.",
        "area": "Cannington, East Cannington, Beckenham, Queens Park, and surrounding southern suburbs",
        "local_note": "Cannington's concentration of automotive businesses means our mechanics here compete on service quality — you'll get better value from an independent in our network than from dealership service centres in the area.",
        "faqs": [
            ("Why should I choose an independent mechanic in Cannington over a dealership?", "Independent mechanics in Cannington typically charge 20–40% less than dealerships for the same work, use equivalent parts, and provide more personalised service. Our Cannington network mechanics are all fully licensed."),
            ("Can I get a same-day brake repair in Cannington?", "For brake repairs in Cannington, same-day service is often possible given the area's concentration of mechanics. Contact us with your vehicle details for fast availability."),
            ("Do Cannington mechanics do pre-purchase inspections?", "Yes — our Cannington mechanics provide pre-purchase inspection reports. Given the number of used car dealers in the area, this service is in high demand."),
            ("How much is an auto electrical repair in Cannington?", "Auto electrical repair costs in Cannington vary by fault type. Battery replacement starts from $150. Alternator repairs run $300–$600+. We provide upfront quotes before any diagnostic work."),
            ("Is there a mechanic open on weekends in Cannington?", "Some mechanics in our Cannington network offer Saturday appointments. Mention weekend availability in your quote request and we'll match you accordingly."),
        ],
    },
    {
        "slug": "morley",
        "name": "Morley",
        "nearby": [("Joondalup", "joondalup.html"), ("Midland", "midland.html"), ("Balcatta", "balcatta.html")],
        "intro": "Morley is a well-established northern suburb with excellent road links via Tonkin Highway and Morley Drive, and a busy mix of residential and commercial activity centred around Galleria Shopping Centre. The suburb's accessible location makes it a popular destination for drivers from the broader northern corridor seeking mechanical services. Morley mechanics in our network serve the full mix of family vehicles, older vehicles, and newer models common across the northern suburbs.",
        "area": "Morley, Noranda, Bedford, and surrounding suburbs in the City of Bayswater",
        "local_note": "Morley is centrally located between the northern and eastern corridors, making it a convenient service location for drivers across a wide catchment area.",
        "faqs": [
            ("Where can I find a reliable mechanic in Morley?", "Perth Mechanic connects Morley drivers with licensed, insured mechanics who provide upfront pricing. Submit a quote request for a same-day response."),
            ("Do Morley mechanics service diesel vehicles?", "Yes — our Morley network includes mechanics experienced with diesel passenger vehicles and light commercial vehicles."),
            ("How much does a minor service cost in Morley?", "A minor service in Morley typically costs $150–$250 depending on your vehicle. Oil and filter change with a safety inspection is the core of a minor service."),
            ("Can I get my car's AC serviced in Morley?", "Yes — air conditioning re-gas and full AC system service is available through our Morley mechanic network."),
            ("Is there a mechanic in Morley who does wheel alignments?", "Yes — wheel alignment is available through our Morley network. Proper alignment is recommended every 10,000km or after hitting a significant pothole."),
        ],
    },
    {
        "slug": "osborne-park",
        "name": "Osborne Park",
        "nearby": [("Balcatta", "balcatta.html"), ("Karrinyup", "karrinyup.html"), ("Morley", "morley.html")],
        "intro": "Osborne Park is already one of Perth's major automotive hubs — Scarborough Beach Road through the suburb is lined with car dealerships, tyre shops, and mechanical workshops. But not all mechanics on the strip are equal, and dealership service prices can be significantly inflated. Perth Mechanic connects Osborne Park drivers with independently qualified mechanics who offer the same standard of work at competitive pricing, without the dealership overhead.",
        "area": "Osborne Park, Innaloo, Stirling, and surrounding northern suburbs along Scarborough Beach Road",
        "local_note": "Osborne Park is Perth's auto strip — our mechanic network here competes directly with dealership service centres, and consistently offers better value for the same standard of work.",
        "faqs": [
            ("Should I use a mechanic in Osborne Park instead of a dealership?", "Independent mechanics in Osborne Park are qualified to the same standard as dealership technicians and typically charge 20–40% less. Our network mechanics are all licensed and insured."),
            ("Where is a good mechanic in Osborne Park?", "Perth Mechanic matches you with qualified, licensed mechanics in Osborne Park who provide upfront pricing and quality workmanship. Submit a request for a fast quote."),
            ("Do Osborne Park mechanics work on European cars?", "Yes — given Osborne Park's European car dealership presence, our network includes mechanics with significant European vehicle experience."),
            ("Can I get a logbook service in Osborne Park that keeps my warranty?", "Yes — under Australian consumer law, any qualified mechanic can perform warranty-valid logbook services. Our Osborne Park mechanics stamp your logbook correctly at below-dealership prices."),
            ("How much is a tyre fitting in Osborne Park?", "Tyre fitting in Osborne Park varies by tyre brand and size. Our mechanics provide competitive pricing on major brands with professional fitting and balancing included."),
        ],
    },
    {
        "slug": "victoria-park",
        "name": "Victoria Park",
        "nearby": [("Cannington", "cannington.html"), ("Subiaco", "subiaco.html"), ("Fremantle", "fremantle.html")],
        "intro": "Victoria Park — or 'Vic Park' as locals call it — is one of Perth's most vibrant inner suburbs, popular with young professionals who often own newer vehicles and are time-poor but quality-conscious. The suburb's diverse Albany Highway strip and proximity to the CBD makes it a natural hub for drivers seeking convenient mechanical services. Vic Park mechanics in our network understand the expectations of the inner-suburb market — fast, transparent, and reliable.",
        "area": "Victoria Park, East Victoria Park, St James, and surrounding inner southern suburbs",
        "local_note": "Victoria Park's young professional demographic typically drives newer vehicles and values efficiency — our mechanics respond quickly, quote clearly, and complete work on time.",
        "faqs": [
            ("Is there a good mechanic in Victoria Park?", "Perth Mechanic connects Victoria Park drivers with qualified, licensed mechanics who offer competitive pricing and same-day quotes. Submit a request to find your local match."),
            ("Can I get a logbook service in Victoria Park?", "Yes — our Victoria Park mechanics perform manufacturer logbook services for all makes and models, keeping your warranty valid without dealership pricing."),
            ("Do Victoria Park mechanics work on performance cars?", "Our network includes mechanics with experience in performance vehicles. Mention your specific vehicle in the quote request and we'll match you with the most appropriate mechanic."),
            ("How much does a service cost in Victoria Park?", "Minor service in Victoria Park: $150–$280. Major service: $300–$600+. Pre-purchase inspection: $150–$250. All pricing is provided upfront with no hidden charges."),
            ("Can I get a mechanic in Victoria Park on short notice?", "For urgent repairs in Victoria Park, same-day availability is often possible given the suburb's inner-city location and access to multiple mechanics. Note urgency in your request."),
        ],
    },
    {
        "slug": "subiaco",
        "name": "Subiaco",
        "nearby": [("Claremont", "claremont.html"), ("Cottesloe", "cottesloe.html"), ("Victoria Park", "victoria-park.html")],
        "intro": "Subiaco is one of Perth's most sought-after inner suburbs, home to professionals, families, and long-term residents who take pride in their vehicles. The suburb's affluent demographic means a higher-than-average proportion of European vehicles — BMW, Mercedes, Audi, and Volkswagen are common on Subiaco streets. Our Subiaco mechanic network includes specialists in European makes alongside all other brands, delivering quality service at significantly better value than dealerships.",
        "area": "Subiaco, West Subiaco, Daglish, and surrounding inner western suburbs",
        "local_note": "Subiaco has a high concentration of European vehicles — our mechanic network specifically includes specialists in BMW, Mercedes, Audi, and Volkswagen for Subiaco and the western suburbs.",
        "faqs": [
            ("Is there a European car mechanic in Subiaco?", "Yes — our Subiaco network includes mechanics who specialise in European makes including BMW, Mercedes-Benz, Audi, and Volkswagen."),
            ("How much does a BMW service cost in Subiaco?", "BMW servicing through our Subiaco network typically costs $250–$500 depending on service level — significantly less than BMW dealerships. We use equivalent OEM-quality parts."),
            ("Can I get a pre-purchase inspection in Subiaco?", "Yes — our Subiaco mechanics provide full pre-purchase inspection reports, especially useful for the higher-value used vehicles common in the inner western suburbs."),
            ("Do Subiaco mechanics work on older classic cars?", "Some mechanics in our Subiaco network have classic vehicle experience. Mention your vehicle in the quote request and we'll identify the best match."),
            ("How quickly can I get an appointment with a Subiaco mechanic?", "For standard services, appointments are typically available within 24–48 hours in Subiaco. For urgent repairs, same-day availability is often possible."),
        ],
    },
    {
        "slug": "cottesloe",
        "name": "Cottesloe",
        "nearby": [("Claremont", "claremont.html"), ("Subiaco", "subiaco.html"), ("Fremantle", "fremantle.html")],
        "intro": "Cottesloe is Perth's iconic beachside suburb, known for the Hotel Cottesloe, family-friendly beaches, and some of Perth's most premium real estate. The suburb's affluent demographic means late-model, often high-value vehicles are the norm — and the expectation for automotive services is correspondingly high. Our Cottesloe mechanic network delivers premium-quality service at independent prices, not dealership rates.",
        "area": "Cottesloe, Swanbourne, North Cottesloe, and surrounding western beachside suburbs",
        "local_note": "Cottesloe's coastal location means salt-air exposure is a real consideration for vehicle maintenance — our mechanics check for salt corrosion on brake components, suspension, and exhaust during routine inspections.",
        "faqs": [
            ("Is there a mechanic near Cottesloe Beach?", "Yes — our Cottesloe and western suburbs mechanic network covers the beach corridor. Submit a quote request and we'll match you with a local mechanic."),
            ("Do mechanics in Cottesloe work on luxury European cars?", "Yes — our network includes mechanics who specialise in premium European brands commonly found in the western suburbs including Porsche, BMW, Mercedes, and Audi."),
            ("Can salt air damage my car in Cottesloe?", "Salt air accelerates corrosion on brake lines, suspension components, and exhaust systems. Our Cottesloe mechanics specifically check these areas during inspections for coastal residents."),
            ("How much does a service cost in Cottesloe?", "Service pricing in Cottesloe is consistent with Perth metro rates — minor service $150–$280, major service $300–$600+. Premium vehicles at the higher end of the range. Upfront quotes always provided."),
            ("How do I book a mechanic in Cottesloe?", "Submit a quote request through Perth Mechanic with your vehicle details and suburb. We'll respond with a firm quote within 30 minutes and confirm your booking."),
        ],
    },
    {
        "slug": "claremont",
        "name": "Claremont",
        "nearby": [("Cottesloe", "cottesloe.html"), ("Subiaco", "subiaco.html"), ("Karrinyup", "karrinyup.html")],
        "intro": "Claremont is an affluent riverside suburb known for its upscale retail, quality dining, and proximity to prestigious schools. The western suburb demographic drives a high proportion of premium and European vehicles — and the expectation for automotive service quality is high. Claremont drivers are looking for mechanics who are qualified, reliable, and honest — exactly the standard we hold our Claremont network to.",
        "area": "Claremont, Peppermint Grove, Dalkeith, and surrounding western riverside suburbs",
        "local_note": "Claremont has one of Perth's highest concentrations of premium and European vehicles — BMW, Porsche, Mercedes, and Lexus are common in the suburb's residential streets.",
        "faqs": [
            ("Where is the best mechanic near Claremont?", "Perth Mechanic connects Claremont drivers with qualified, licensed mechanics in the western suburbs. Submit a request and receive a quote within 30 minutes."),
            ("Do mechanics in Claremont service BMW and Mercedes?", "Yes — our Claremont and western suburbs network includes mechanics with specialist European vehicle experience, covering BMW, Mercedes, Audi, Porsche, and Lexus."),
            ("Can I get a pre-purchase inspection in Claremont for a prestige car?", "Yes — our mechanics provide thorough pre-purchase inspections including diagnostic scanning for stored fault codes, particularly important for premium European vehicles."),
            ("How much does an Audi service cost in Claremont?", "Audi servicing through our Claremont network is typically 25–40% less than Audi dealerships for the same standard of work. We provide an upfront quote before any work begins."),
            ("Is there a mechanic in Claremont who does air conditioning service?", "Yes — AC re-gas and full system service is available through our Claremont network. Essential maintenance for Perth's hot summers."),
        ],
    },
    {
        "slug": "karrinyup",
        "name": "Karrinyup",
        "nearby": [("Osborne Park", "osborne-park.html"), ("Joondalup", "joondalup.html"), ("Balcatta", "balcatta.html")],
        "intro": "Karrinyup is a well-established northern suburb anchored by the recently expanded Karrinyup Shopping Centre and surrounded by quality residential streets. Families and professionals in Karrinyup drive a mix of newer family vehicles and older models — and the suburb's proximity to major arterials makes it a convenient location for accessing mechanic services across the northern corridor. Our Karrinyup mechanic network covers all vehicle types with efficient, no-surprise service.",
        "area": "Karrinyup, Carine, Gwelup, and surrounding northern suburbs near Karrinyup Road",
        "local_note": "Karrinyup's post-renovation developments have attracted newer residents with newer vehicles — our mechanics are experienced with current logbook service schedules and warranty requirements across all major brands.",
        "faqs": [
            ("Is there a mechanic near Karrinyup Shopping Centre?", "Yes — our Karrinyup and northern suburbs network provides convenient access to qualified mechanics for all vehicle types and services."),
            ("Can I get a logbook service in Karrinyup?", "Yes — our Karrinyup mechanics perform manufacturer-compliant logbook services for all makes and models, keeping your warranty valid at below-dealership pricing."),
            ("How much is a tyre fitting in Karrinyup?", "Tyre fitting in Karrinyup includes professional mounting and balancing. Pricing varies by brand and tyre size. We provide competitive quotes upfront."),
            ("Do Karrinyup mechanics work on newer model vehicles?", "Absolutely — our Karrinyup network includes mechanics current with the latest vehicle technologies, including direct-injection engines, CVT transmissions, and hybrid systems."),
            ("Can I get a brake inspection in Karrinyup?", "Yes — brake inspections and repairs are available through our Karrinyup network. If you're hearing grinding or experiencing a soft pedal, don't delay — contact us for a fast quote."),
        ],
    },
    {
        "slug": "balcatta",
        "name": "Balcatta",
        "nearby": [("Osborne Park", "osborne-park.html"), ("Morley", "morley.html"), ("Karrinyup", "karrinyup.html")],
        "intro": "Balcatta is an industrial-residential suburb in Perth's northern corridor, housing a mix of light industrial businesses, warehouses, and residential streets. The suburb's industrial character means mechanics in Balcatta are well-experienced with fleet vehicles, light commercial vehicles, and the hard-working vehicles driven by local tradespeople. Our Balcatta mechanic network covers the full spectrum from passenger cars to commercial fleet servicing.",
        "area": "Balcatta, Herdsman, Westminster, and surrounding northern industrial and residential suburbs",
        "local_note": "Balcatta's industrial precinct means our mechanic network is particularly well-suited to commercial vehicle servicing, fleet maintenance programs, and heavy-duty mechanical repairs.",
        "faqs": [
            ("Do Balcatta mechanics service commercial vehicles?", "Yes — Balcatta mechanics in our network regularly service light commercial vehicles, vans, and utes used by local tradespeople and small businesses."),
            ("Is there fleet servicing available in Balcatta?", "Absolutely. Our Balcatta network offers fleet maintenance programs with consolidated invoicing and priority booking to minimise business downtime."),
            ("How much does a service cost in Balcatta?", "Minor service in Balcatta: $150–$250. Major service: $300–$550. Commercial vehicle servicing may be higher depending on vehicle type. Upfront quotes always provided."),
            ("Can I get auto electrical work done in Balcatta?", "Yes — qualified auto electricians are available in our Balcatta network for battery, alternator, wiring, and ECU diagnostics."),
            ("Do Balcatta mechanics do diesel vehicles?", "Yes — diesel vehicle servicing is a specialty of our Balcatta network given the suburb's commercial vehicle concentration."),
        ],
    },
    {
        "slug": "malaga",
        "name": "Malaga",
        "nearby": [("Midland", "midland.html"), ("Morley", "morley.html"), ("Balcatta", "balcatta.html")],
        "intro": "Malaga is one of Perth's largest industrial suburbs, housing hundreds of businesses across automotive, manufacturing, construction, and logistics. The suburb's commercial character means mechanics in Malaga are among the most experienced in Perth for fleet vehicles, heavy-use vehicles, and light commercial servicing. Our Malaga mechanic network serves both business fleet clients and private vehicle owners across the northern industrial corridor.",
        "area": "Malaga, Noranda, Mirrabooka, and surrounding northern industrial suburbs",
        "local_note": "Malaga's industrial environment means our mechanics are experienced with high-kilometre, heavy-use vehicles — they're used to seeing vehicles that work hard and need practical, efficient servicing.",
        "faqs": [
            ("Do mechanics in Malaga do fleet vehicle servicing?", "Yes — fleet servicing is a core capability of our Malaga mechanic network. We offer scheduled maintenance programs with consolidated invoicing for businesses of all sizes."),
            ("Is there an auto electrician in Malaga?", "Yes — our Malaga network includes qualified auto electricians for all electrical diagnosis, battery, alternator, and ECU work."),
            ("How much is a diesel service in Malaga?", "Diesel vehicle servicing in Malaga varies by vehicle type — light commercial diesel: $200–$350. Heavy ute or van: $280–$450+. Upfront quotes provided before any work begins."),
            ("Can I get a pre-purchase inspection in Malaga for a used ute?", "Yes — our Malaga mechanics provide pre-purchase inspection reports for utes and light commercial vehicles, which is particularly valuable in Perth's active used ute market."),
            ("Do Malaga mechanics work on 4WDs?", "Yes — 4WD servicing including suspension checks, diff oil changes, and transfer case service is available through our Malaga network."),
        ],
    },
    {
        "slug": "belmont",
        "name": "Belmont",
        "nearby": [("Victoria Park", "victoria-park.html"), ("Midland", "midland.html"), ("Cannington", "cannington.html")],
        "intro": "Belmont is a well-connected inner-eastern suburb near Perth Airport, with a diverse residential and commercial mix. Its central location makes it accessible for drivers from across the eastern corridor. Belmont has a broad mix of vehicle types — from older affordable vehicles to newer family cars — and our Belmont mechanic network is equipped to service all makes, models, and ages.",
        "area": "Belmont, Rivervale, Kewdale, and surrounding inner eastern suburbs near Perth Airport",
        "local_note": "Belmont's proximity to Perth Airport means we occasionally service airport staff vehicles — often high-kilometre vehicles that need experienced, efficient mechanics.",
        "faqs": [
            ("Is there a mechanic near Belmont?", "Yes — Perth Mechanic has qualified mechanics available throughout Belmont and surrounding inner eastern suburbs. Submit a request for a fast quote."),
            ("How much is a car service in Belmont?", "Minor service in Belmont: $150–$250. Major service: $280–$550. Prices depend on your vehicle make and model. Upfront quotes always provided before work begins."),
            ("Can I get a logbook service in Belmont?", "Yes — our Belmont mechanics perform manufacturer logbook services and stamp your logbook using manufacturer-specified parts and fluids."),
            ("Do Belmont mechanics do tyre fitting and balancing?", "Yes — tyre fitting, balancing, and wheel alignment are available through our Belmont network."),
            ("Is there an auto electrician in Belmont?", "Yes — auto electrical services including battery, alternator, and diagnostic scanning are available through our Belmont mechanic network."),
        ],
    },
    {
        "slug": "cockburn-central",
        "name": "Cockburn Central",
        "nearby": [("Mandurah", "mandurah.html"), ("Rockingham", "rockingham.html"), ("Canning Vale", "canning-vale.html")],
        "intro": "Cockburn Central is one of Perth's fastest-growing southern hubs, with modern apartments, new family homes, and a busy commercial precinct centred around Cockburn Gateway shopping centre. The suburb's growth brings a high proportion of newer vehicles and first-time buyers who need logbook servicing to protect their warranties. Cockburn Central mechanics in our network are experienced with the full range of modern vehicles common in this rapidly developing suburb.",
        "area": "Cockburn Central, Success, Hammond Park, Atwell, and surrounding southern growth suburbs",
        "local_note": "Cockburn Central's rapid growth means many residents drive newer vehicles on finance agreements — our mechanics protect your warranty with proper manufacturer-compliant logbook servicing.",
        "faqs": [
            ("Is there a mechanic in Cockburn Central?", "Yes — Perth Mechanic connects Cockburn Central drivers with licensed mechanics available for same-day quotes on all services."),
            ("Can I get a logbook service in Cockburn Central?", "Yes — our mechanics in Cockburn Central perform manufacturer-compliant logbook services for all brands, keeping your new car warranty valid at competitive pricing."),
            ("How much does a service cost in Cockburn Central?", "Minor service: $150–$260. Major service: $280–$550. Logbook service varies by manufacturer schedule. Upfront quotes always provided."),
            ("Do Cockburn Central mechanics work on hybrids?", "Yes — hybrid vehicle servicing including Toyota Prius, RAV4 Hybrid, and other hybrid models is available through our Cockburn Central network."),
            ("Can I get same-day tyre fitting in Cockburn Central?", "Same-day tyre fitting is often available in Cockburn Central depending on tyre availability and mechanic schedule. Submit your request and note the urgency."),
        ],
    },
    {
        "slug": "thornlie",
        "name": "Thornlie",
        "nearby": [("Canning Vale", "canning-vale.html"), ("Armadale", "armadale.html"), ("Cannington", "cannington.html")],
        "intro": "Thornlie is a well-established southeastern suburb with a large population of long-term residents and family homeowners. The suburb's solid residential character means steady, year-round demand for mechanical services — particularly servicing of older and mid-age vehicles that are workhorse family cars rather than prestige vehicles. Thornlie mechanics in our network provide practical, affordable servicing with the reliability that Thornlie residents expect.",
        "area": "Thornlie, Canning Vale, Kenwick, Maddington, and surrounding southeastern suburbs",
        "local_note": "Thornlie's residents are practical and value-conscious — our mechanics provide honest assessments, upfront pricing, and quality work without upselling unnecessary services.",
        "faqs": [
            ("Where can I find a reliable mechanic in Thornlie?", "Perth Mechanic connects Thornlie drivers with licensed, insured mechanics who provide transparent pricing. Submit a quote request for a response within 30 minutes."),
            ("How much is a car service in Thornlie?", "Minor service in Thornlie: $150–$240. Major service: $280–$520. Our mechanics quote upfront — no hidden charges after the job."),
            ("Do Thornlie mechanics service older vehicles?", "Yes — our Thornlie network is experienced with older vehicles and can advise on cost-effective repairs versus replacement when vehicles reach high mileage."),
            ("Can I get brake repairs in Thornlie?", "Yes — brake pad replacement, disc machining, and full brake system repairs are available through our Thornlie mechanic network."),
            ("Is there a mechanic in Thornlie who does pre-purchase inspections?", "Yes — pre-purchase vehicle inspections are available through our Thornlie network. Highly recommended before purchasing any used vehicle in the southeastern corridor."),
        ],
    },
]

NAV_SUBURBS = """
          <a href="fremantle.html">Fremantle</a>
          <a href="joondalup.html">Joondalup</a>
          <a href="midland.html">Midland</a>
          <a href="armadale.html">Armadale</a>
          <a href="rockingham.html">Rockingham</a>
          <a href="mandurah.html">Mandurah</a>
          <a href="canning-vale.html">Canning Vale</a>
          <a href="cannington.html">Cannington</a>
          <a href="morley.html">Morley</a>
          <a href="osborne-park.html">Osborne Park</a>
          <a href="victoria-park.html">Victoria Park</a>
          <a href="subiaco.html">Subiaco</a>
          <a href="cottesloe.html">Cottesloe</a>
          <a href="claremont.html">Claremont</a>
          <a href="karrinyup.html">Karrinyup</a>
          <a href="balcatta.html">Balcatta</a>
          <a href="malaga.html">Malaga</a>
          <a href="belmont.html">Belmont</a>
          <a href="cockburn-central.html">Cockburn Central</a>
          <a href="thornlie.html">Thornlie</a>"""

FOOTER_SUBURBS = "\n".join(
    f'          <li><a href="{s["slug"]}.html">{s["name"]}</a></li>'
    for s in SUBURBS[:10]
)

HEADER = """\
<!-- ── HEADER ── -->
<header class="site-header">
  <div class="container header-inner">
    <a href="index.html" class="logo">Perth<span>Mechanic</span></a>
    <nav class="main-nav" id="main-nav">
      <a href="index.html">Home</a>
      <a href="services.html">Services</a>
      <div class="dropdown">
        <button class="dropdown-btn">Suburbs &#9660;</button>
        <div class="dropdown-menu">%(nav)s
        </div>
      </div>
      <a href="about.html">About</a>
      <a href="blog.html">Blog</a>
      <a href="contact.html" class="btn btn-primary">Get a Quote</a>
    </nav>
    <div class="header-right">
      <button class="hamburger" id="hamburger" aria-label="Open menu" aria-expanded="false">&#9776;</button>
    </div>
  </div>
</header>""" % {"nav": NAV_SUBURBS}

FOOTER_TPL = """\
<!-- ── FOOTER ── -->
<footer class="site-footer">
  <div class="container">
    <div class="footer-top">
      <div class="footer-brand">
        <a href="index.html" class="logo">Perth<span>Mechanic</span></a>
        <p>Perth\'s trusted mechanic connection service.<br>Matching Perth drivers with qualified, affordable mechanics since 2024.</p>
        <p>&#9993;&#65039; <a href="mailto:info@perthmechanic.com">info@perthmechanic.com</a></p>
      </div>
      <div class="footer-links">
        <h4>Quick Links</h4>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="services.html">Services</a></li>
          <li><a href="about.html">About</a></li>
          <li><a href="blog.html">Blog</a></li>
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
      <p>&copy; <span id="year"></span> Perth Mechanic. All rights reserved.</p>
    </div>
  </div>
</footer>"""


def build_page(s):
    slug = s["slug"]
    name = s["name"]
    nearby = s["nearby"]
    intro = s["intro"]
    area = s["area"]
    local_note = s["local_note"]
    faqs = s["faqs"]

    nearby_pills = "\n".join(
        f'          <a href="{href}">{n}</a>' for n, href in nearby
    )

    faq_items = ""
    for q, a in faqs:
        faq_items += f"""      <div class="faq-item">
        <button class="faq-q" aria-expanded="false">{q} <span class="faq-icon">+</span></button>
        <div class="faq-a">{a}</div>
      </div>
"""

    footer = FOOTER_TPL % {"suburbs": FOOTER_SUBURBS}

    schema = f"""  {{
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "name": "Perth Mechanic — {name}",
    "url": "https://perthmechanic.com/{slug}.html",
    "description": "Qualified mechanic services in {name}, Perth WA. Logbook service, brake repairs, tyres, auto electrical and more.",
    "areaServed": {{
      "@type": "Place",
      "name": "{name}, Western Australia"
    }},
    "address": {{
      "@type": "PostalAddress",
      "addressLocality": "{name}",
      "addressRegion": "WA",
      "addressCountry": "AU"
    }}
  }}"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="Mechanic in {name} Perth — logbook service, brake repairs, tyres, auto electrical and more. Same-day quotes from licensed {name} mechanics. Get a free quote today." />
  <meta name="robots" content="index, follow" />
  <title>Mechanic in {name} | Car Service &amp; Repairs {name} Perth | Perth Mechanic</title>
  <link rel="canonical" href="https://perthmechanic.com/{slug}.html" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="css/style.css" />
  <script type="application/ld+json">
{schema}
  </script>
</head>
<body>

{HEADER}

<!-- ── HERO ── -->
<section class="suburb-hero">
  <div class="container">
    <h1>Mechanic in {name} | Car Service &amp; Repairs {name} Perth</h1>
    <p>Perth Mechanic connects {name} drivers with fully qualified, affordable mechanics for all services. Same-day quotes, upfront pricing, licensed professionals.</p>
    <div class="hero-cta">
      <a href="#quote" class="btn btn-primary btn-lg">Get a Free Quote</a>
      <a href="services.html" class="btn btn-outline-white btn-lg">View Services</a>
    </div>
  </div>
</section>

<!-- ── STATS BAR ── -->
<div class="stats-bar">
  <div class="container stats-inner">
    <div class="stat"><div class="stat-num">&#10003;</div><div class="stat-label">Licensed Mechanics</div></div>
    <div class="stat"><div class="stat-num">30 min</div><div class="stat-label">Quote Response</div></div>
    <div class="stat"><div class="stat-num">&#10003;</div><div class="stat-label">Upfront Pricing</div></div>
    <div class="stat"><div class="stat-num">&#10003;</div><div class="stat-label">All Makes &amp; Models</div></div>
  </div>
</div>

<!-- ── MAIN CONTENT ── -->
<section class="section-pad">
  <div class="container suburb-content">
    <div>
      <h2>Car Servicing &amp; Repairs in {name}, Perth WA</h2>
      <p style="color:var(--muted);margin:16px 0;font-size:0.97rem;line-height:1.8;">{intro}</p>

      <h3 style="margin-top:28px;margin-bottom:12px;">Mechanic Services Available in {name}</h3>
      <ul class="checklist">
        <li>Logbook Service — manufacturer-compliant, warranty valid</li>
        <li>Minor &amp; Major Service — oil, filters, fluids, full inspection</li>
        <li>Brake Repairs — pads, discs, fluid, callipers</li>
        <li>Tyre Fitting &amp; Balancing — all major brands</li>
        <li>Auto Electrical — battery, alternator, ECU diagnostics</li>
        <li>Pre-Purchase Inspection — full mechanical report</li>
        <li>Air Conditioning Service — re-gas, leak detection</li>
        <li>Fleet Servicing — scheduled programs for businesses</li>
      </ul>

      <h3 style="margin-top:28px;margin-bottom:12px;">Why {name} Drivers Choose Perth Mechanic</h3>
      <p style="color:var(--muted);margin-bottom:12px;font-size:0.95rem;">{local_note}</p>
      <ul class="checklist">
        <li>All mechanics hold a current Motor Vehicle Repairer licence</li>
        <li>Firm upfront quotes — no surprise charges after the job</li>
        <li>Public liability insurance on all mechanics</li>
        <li>Response to every enquiry within 30 minutes</li>
        <li>All makes and models: Japanese, European, Korean, American</li>
      </ul>

      <h3 style="margin-top:28px;margin-bottom:12px;">Service Area Near {name}</h3>
      <p style="color:var(--muted);margin-bottom:16px;font-size:0.95rem;">We service {area}. We also cover nearby suburbs:</p>
      <div class="nearby-suburbs">
        <div class="nearby-list">
{nearby_pills}
          <a href="index.html">View all suburbs</a>
        </div>
      </div>

      <div style="margin-top:32px;">
        <a href="services.html" style="color:var(--blue);font-weight:600;font-size:0.93rem;">View all mechanic services &rarr;</a>
      </div>
    </div>

    <!-- QUOTE FORM -->
    <div id="quote">
      <div class="form-card-light">
        <h3>Get a Free Quote in {name}</h3>
        <p class="card-sub">We respond within 30 minutes during business hours (Mon–Sat 7am–7pm).</p>
        <form action="https://formspree.io/f/XXXXXXXX" method="POST" data-formspree data-success-id="{slug}-success">
          <div class="form-two-col">
            <div class="form-group">
              <label for="{slug}-name">Full Name *</label>
              <input type="text" id="{slug}-name" name="name" placeholder="John Smith" required />
            </div>
            <div class="form-group">
              <label for="{slug}-phone">Phone *</label>
              <input type="tel" id="{slug}-phone" name="phone" placeholder="04XX XXX XXX" required />
            </div>
          </div>
          <div class="form-group">
            <label for="{slug}-suburb">Suburb *</label>
            <input type="text" id="{slug}-suburb" name="suburb" placeholder="{name}" value="{name}" required />
          </div>
          <div class="form-group">
            <label for="{slug}-service">Service Needed *</label>
            <select id="{slug}-service" name="service" required>
              <option value="">Select a service…</option>
              <option>Logbook Service</option>
              <option>Minor Service</option>
              <option>Major Service</option>
              <option>Brake Repairs</option>
              <option>Tyre Fitting &amp; Balancing</option>
              <option>Auto Electrical</option>
              <option>Pre-Purchase Inspection</option>
              <option>Air Conditioning Service</option>
              <option>Fleet Servicing</option>
              <option>Other / Not Sure</option>
            </select>
          </div>
          <div class="form-group">
            <label for="{slug}-vehicle">Vehicle Make &amp; Model *</label>
            <input type="text" id="{slug}-vehicle" name="vehicle" placeholder="e.g. Toyota Corolla 2019" required />
          </div>
          <div class="form-group">
            <label for="{slug}-message">Additional Details</label>
            <textarea id="{slug}-message" name="message" rows="3" placeholder="Describe the issue, any warning lights, or any other details…"></textarea>
          </div>
          <button type="submit" class="btn btn-primary btn-full btn-lg">Get My Free Quote &rarr;</button>
        </form>
        <div id="{slug}-success" class="form-success-light" hidden>
          <h3>&#10003; Thanks! We'll be in touch within 30 minutes.</h3>
          <p>We've received your {name} enquiry and will match you with a qualified local mechanic shortly.</p>
        </div>
      </div>

      <div style="background:var(--blue-lt);border:1.5px solid var(--border);border-radius:var(--radius);padding:20px;margin-top:20px;text-align:center;">
        <p style="font-weight:600;margin-bottom:6px;color:var(--navy);">Have a question?</p>
        <a href="mailto:info@perthmechanic.com" style="font-size:1rem;font-weight:700;color:var(--blue);">info@perthmechanic.com</a>
        <p style="font-size:0.85rem;color:var(--muted);margin-top:6px;">We reply within 1 hour, Mon–Sat 7am–7pm</p>
      </div>
    </div>
  </div>
</section>

<!-- ── FAQ ── -->
<section class="section-pad bg-light">
  <div class="container">
    <h2 class="section-title">FAQ — Mechanics in {name}</h2>
    <p class="section-sub">Common questions from {name} drivers about car servicing and repairs.</p>
    <div class="faq-list">
{faq_items}    </div>
  </div>
</section>

<!-- ── CTA ── -->
<section class="cta-band">
  <div class="container">
    <h2>Ready to Book a {name} Mechanic?</h2>
    <p>Same-day quotes. Licensed mechanics. Upfront pricing. All of {name} and surrounding suburbs covered.</p>
    <div style="display:flex;gap:14px;justify-content:center;flex-wrap:wrap;">
      <a href="#quote" class="btn btn-outline-white btn-lg">Get a Free Quote</a>
      <a href="index.html" class="btn btn-outline-white btn-lg">Back to Home</a>
    </div>
  </div>
</section>

{footer}

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
