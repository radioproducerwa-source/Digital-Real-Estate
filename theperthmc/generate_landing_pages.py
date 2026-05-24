#!/usr/bin/env python3
"""Generate all 20 landing pages for Perth MC.
Run from the theperthmc/ directory: python3 generate_landing_pages.py
"""

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

HEADER = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="{meta}" />
  <meta name="robots" content="index, follow" />
  <title>{title}</title>
  <link rel="canonical" href="https://perthmc.com/{slug}.html" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="css/style.css" />
</head>
<body>

<!-- ── HEADER ── -->
<header class="site-header">
  <div class="container header-inner">
    <a href="index.html" class="logo">The Perth<span>MC</span></a>
    <nav class="main-nav" id="main-nav">
      <a href="index.html">Home</a>
      <a href="services.html">Services</a>
      <div class="dropdown">
        <button class="dropdown-btn">Events &#9660;</button>
        <div class="dropdown-menu">
          <a href="wedding-mc-perth.html">Wedding MC Perth</a>
          <a href="corporate-mc-perth.html">Corporate MC Perth</a>
          <a href="conference-mc-perth.html">Conference MC Perth</a>
          <a href="charity-gala-mc-perth.html">Charity Gala MC</a>
          <a href="awards-night-mc-perth.html">Awards Night MC</a>
          <a href="mc-50th-birthday-perth.html">50th Birthday MC</a>
          <a href="school-formal-mc-perth.html">School Formal MC</a>
          <a href="christmas-party-mc-perth.html">Christmas Party MC</a>
          <a href="product-launch-mc-perth.html">Product Launch MC</a>
          <a href="black-tie-event-mc-perth.html">Black Tie Event MC</a>
        </div>
      </div>
      <a href="about.html">About</a>
      <a href="blog.html">Blog</a>
      <a href="contact.html" class="btn btn-primary">Check Availability</a>
    </nav>
    <div class="header-right">
      <a href="contact.html" class="header-cta-link">Check Availability</a>
      <button class="hamburger" id="hamburger" aria-label="Open menu" aria-expanded="false">&#9776;</button>
    </div>
  </div>
</header>
"""

FOOTER = """
<!-- ── CTA BAND ── -->
<section class="cta-band">
  <div class="container">
    <h2>Ready to Check Availability?</h2>
    <p>Tell us about your event and we'll confirm availability — usually within 24 hours.</p>
    <a href="contact.html" class="btn btn-primary btn-lg">Check Availability</a>
    &nbsp;&nbsp;
    <a href="services.html" class="btn btn-outline-white btn-lg">View All Services</a>
  </div>
</section>

<!-- ── FOOTER ── -->
<footer class="site-footer">
  <div class="container">
    <div class="footer-top">
      <div class="footer-brand">
        <a href="index.html" class="logo">The Perth<span>MC</span></a>
        <p>Perth's professional MC for weddings, corporate events, galas, conferences, and milestone celebrations.</p>
        <p>&#x2709;&#xFE0F; <a href="mailto:info@perthmc.com">info@perthmc.com</a></p>
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
      <div class="footer-events">
        <h4>Event Types</h4>
        <ul>
          <li><a href="wedding-mc-perth.html">Wedding MC Perth</a></li>
          <li><a href="corporate-mc-perth.html">Corporate MC Perth</a></li>
          <li><a href="conference-mc-perth.html">Conference MC</a></li>
          <li><a href="charity-gala-mc-perth.html">Charity Gala MC</a></li>
          <li><a href="awards-night-mc-perth.html">Awards Night MC</a></li>
          <li><a href="mc-50th-birthday-perth.html">50th Birthday MC</a></li>
          <li><a href="school-formal-mc-perth.html">School Formal MC</a></li>
          <li><a href="christmas-party-mc-perth.html">Christmas Party MC</a></li>
          <li><a href="product-launch-mc-perth.html">Product Launch MC</a></li>
          <li><a href="black-tie-event-mc-perth.html">Black Tie Event MC</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; <span id="year"></span> Perth MC. All rights reserved. | Perth, Western Australia</p>
    </div>
  </div>
</footer>

<script src="js/main.js"></script>

<script type="application/ld+json">
{schema}
</script>
</body>
</html>
"""

LANDING_PAGES = [
    {
        "slug": "wedding-mc-perth",
        "title": "Wedding MC Perth | Professional Wedding Host | Perth MC",
        "h1": "Wedding MC Perth",
        "meta": "Perth's professional wedding MC for ceremonies and receptions. Fully tailored, obsessively prepared, and experienced across 200+ Perth weddings. Check availability today.",
        "intro": "Your wedding reception is the celebration of a lifetime — and the MC sets the tone for every single moment. From the bridal party introductions to the last dance, a great wedding MC ensures your evening flows seamlessly, your guests stay engaged, and you actually get to enjoy the night you've planned for months.",
        "what_we_do": [
            "Ceremony &amp; reception hosting",
            "Bridal party introductions",
            "Wedding speech management &amp; timing",
            "Liaison with DJ, band &amp; photographer",
            "First dance, cake cutting &amp; entrance cues",
            "Personalised script — never a generic template",
            "Pre-wedding briefing &amp; run sheet review",
            "Guest entertainment during transitions",
        ],
        "why": "Perth couples choose Perth MC because we understand that a wedding is unlike any other event. The emotional stakes are higher, the family dynamics are more complex, and the moments that matter most can't be rushed or repeated. We've hosted over 200 Perth weddings — in the Swan Valley, along the river, in Fremantle's heritage venues, and in beachside locations from Cottesloe to Scarborough.",
        "nearby": [
            ("corporate-mc-perth.html", "Corporate MC Perth"),
            ("outdoor-wedding-mc-perth.html", "Outdoor Wedding MC"),
            ("wedding-mc-fremantle.html", "Wedding MC Fremantle"),
            ("wedding-mc-subiaco.html", "Wedding MC Subiaco"),
        ],
        "event_type": "Wedding",
        "schema_type": "Event",
    },
    {
        "slug": "corporate-mc-perth",
        "title": "Corporate MC Perth | Conference &amp; Event Host | Perth MC",
        "h1": "Corporate MC Perth",
        "meta": "Professional corporate MC in Perth for conferences, AGMs, awards nights, product launches, and team events. Brand-aligned, authoritative, and thoroughly prepared.",
        "intro": "Corporate audiences have high expectations and low tolerance for amateur hosting. They're professionals — often time-poor — and they can tell the difference between an MC who's done this a hundred times and one who's winging it. Perth MC brings preparation, authority, and the ability to read a corporate room.",
        "what_we_do": [
            "Conference &amp; AGM hosting",
            "Keynote &amp; speaker introductions",
            "Panel &amp; Q&amp;A facilitation",
            "Awards presentation scripting",
            "Multi-session day management",
            "Brand-aligned hosting style",
            "AV &amp; technical coordination",
            "Team energising &amp; audience engagement",
        ],
        "why": "Perth's corporate events market is competitive — the standard your audience expects is high. Whether it's a 50-person strategy day or a 600-person national conference, we research your organisation, understand your culture, and deliver hosting that reflects your brand. No icebreakers. No filler. Just confident, purposeful event management.",
        "nearby": [
            ("conference-mc-perth.html", "Conference MC Perth"),
            ("awards-night-mc-perth.html", "Awards Night MC"),
            ("product-launch-mc-perth.html", "Product Launch MC"),
            ("christmas-party-mc-perth.html", "Christmas Party MC"),
        ],
        "event_type": "CorporateEvent",
        "schema_type": "Event",
    },
    {
        "slug": "wedding-mc-fremantle",
        "title": "Wedding MC Fremantle | Professional Wedding Host Freo | Perth MC",
        "h1": "Wedding MC Fremantle",
        "meta": "Professional wedding MC for Fremantle weddings — ceremonies and receptions at Fremantle's iconic venues. Experienced, personalised, and available for your date.",
        "intro": "Fremantle is one of Perth's most beloved wedding destinations — a city with character, heritage, and a relaxed coastal energy that makes for unforgettable celebrations. From the Fremantle Arts Centre to waterfront venues along the harbour, we know Freo's wedding venues and what makes each one unique.",
        "what_we_do": [
            "Ceremony &amp; reception hosting",
            "Bridal party introductions",
            "Speech management &amp; timing",
            "Venue &amp; vendor coordination",
            "Personalised script for your wedding",
            "Pre-wedding briefing &amp; run sheet review",
            "First dance, entrances &amp; key moment cues",
            "Experience at Fremantle's top venues",
        ],
        "why": "Fremantle weddings have a distinct vibe — relaxed but sophisticated, coastal but cultural. We've MC'd at Fremantle venues including the Arts Centre, Esplanade Hotel, Little Creatures, and numerous private venues throughout the port city. We know how these spaces work and how to make your evening feel distinctly Freo.",
        "nearby": [
            ("wedding-mc-perth.html", "Wedding MC Perth"),
            ("wedding-mc-subiaco.html", "Wedding MC Subiaco"),
            ("wedding-mc-scarborough.html", "Wedding MC Scarborough"),
            ("wedding-mc-rockingham.html", "Wedding MC Rockingham"),
        ],
        "event_type": "Wedding",
        "schema_type": "Event",
    },
    {
        "slug": "wedding-mc-joondalup",
        "title": "Wedding MC Joondalup | Professional Wedding Host | Perth MC",
        "h1": "Wedding MC Joondalup",
        "meta": "Professional wedding MC for Joondalup and Perth's northern suburbs. Experienced, fully tailored, and ready for your date. Check availability now.",
        "intro": "Joondalup and Perth's northern corridor is home to some of WA's most beautiful wedding venues — lakeside settings, garden estates, and modern function centres that suit every style of celebration. We're experienced hosting weddings across the northern suburbs, from Joondalup itself to Wanneroo, Two Rocks, and Yanchep.",
        "what_we_do": [
            "Ceremony &amp; reception hosting",
            "Bridal party introductions",
            "Speech management &amp; timing",
            "Venue &amp; vendor coordination",
            "Personalised script for your wedding",
            "Pre-wedding briefing &amp; run sheet review",
            "Experience at northern Perth venues",
            "Available for northern suburbs &amp; coastal weddings",
        ],
        "why": "Joondalup's wedding scene has grown significantly — and with it, the quality expected from every vendor, including the MC. We've hosted celebrations at venues including Joondalup Resort, The Lakeside Function Centre, and private properties throughout Perth's northern corridor. We know the logistics and we know how to work them in your favour.",
        "nearby": [
            ("wedding-mc-perth.html", "Wedding MC Perth"),
            ("wedding-mc-scarborough.html", "Wedding MC Scarborough"),
            ("corporate-mc-perth.html", "Corporate MC Perth"),
            ("wedding-mc-mandurah.html", "Wedding MC Mandurah"),
        ],
        "event_type": "Wedding",
        "schema_type": "Event",
    },
    {
        "slug": "wedding-mc-mandurah",
        "title": "Wedding MC Mandurah | Professional Wedding Host | Perth MC",
        "h1": "Wedding MC Mandurah",
        "meta": "Professional wedding MC for Mandurah weddings — waterway venues, coastal settings, and function centres. Fully tailored to your event. Check availability.",
        "intro": "Mandurah is one of Western Australia's most picturesque wedding destinations — with its waterways, canals, and coastal backdrop creating settings that are hard to match anywhere in the country. We travel to Mandurah regularly for weddings and understand what makes events in this beautiful city work.",
        "what_we_do": [
            "Ceremony &amp; reception hosting",
            "Bridal party introductions",
            "Speech management &amp; timing",
            "Mandurah venue knowledge",
            "Personalised script for your wedding",
            "Pre-wedding briefing &amp; run sheet review",
            "Vendor coordination at Mandurah venues",
            "Available for Mandurah &amp; Peel region",
        ],
        "why": "Mandurah sits about an hour south of Perth, and we travel there for weddings regularly. We've hosted events at waterfront venues along the Mandurah Estuary, at Meadow Springs, and at private properties throughout the Peel region. Travel costs apply for Mandurah bookings — contact us to discuss.",
        "nearby": [
            ("wedding-mc-perth.html", "Wedding MC Perth"),
            ("wedding-mc-rockingham.html", "Wedding MC Rockingham"),
            ("corporate-mc-perth.html", "Corporate MC Perth"),
            ("wedding-mc-fremantle.html", "Wedding MC Fremantle"),
        ],
        "event_type": "Wedding",
        "schema_type": "Event",
    },
    {
        "slug": "wedding-mc-subiaco",
        "title": "Wedding MC Subiaco | Professional Wedding Host | Perth MC",
        "h1": "Wedding MC Subiaco",
        "meta": "Professional wedding MC for Subiaco and inner-west Perth weddings. Experienced at Subiaco's best venues — Framesby, Fraser's, and more. Check availability.",
        "intro": "Subiaco is one of Perth's most sought-after inner-city wedding precincts — walkable, vibrant, and home to some of the city's finest function venues and restaurants. We regularly host weddings in Subiaco and the surrounding inner west, and understand the character and energy these locations bring to a celebration.",
        "what_we_do": [
            "Ceremony &amp; reception hosting",
            "Bridal party introductions",
            "Speech management &amp; timing",
            "Inner-west Perth venue experience",
            "Personalised script for your wedding",
            "Pre-wedding briefing &amp; run sheet review",
            "Vendor coordination",
            "Available for Subiaco &amp; inner-west Perth",
        ],
        "why": "Subiaco's wedding venues are as diverse as the suburb itself — from intimate heritage spaces to modern rooftop venues and lush garden settings. We've hosted events at venues including Fraser's Kings Park, The Subiaco Hotel, and private function spaces throughout the inner west. We know how to make the most of what these venues offer.",
        "nearby": [
            ("wedding-mc-perth.html", "Wedding MC Perth"),
            ("wedding-mc-fremantle.html", "Wedding MC Fremantle"),
            ("wedding-mc-scarborough.html", "Wedding MC Scarborough"),
            ("outdoor-wedding-mc-perth.html", "Outdoor Wedding MC"),
        ],
        "event_type": "Wedding",
        "schema_type": "Event",
    },
    {
        "slug": "wedding-mc-scarborough",
        "title": "Wedding MC Scarborough | Beachside Wedding MC Perth | Perth MC",
        "h1": "Wedding MC Scarborough",
        "meta": "Professional wedding MC for Scarborough and coastal Perth weddings. Beachside ceremony hosting, sunset receptions, and full wedding MC services. Check availability.",
        "intro": "Scarborough and the northern coastal suburbs of Perth offer some of the most spectacular wedding settings in the country — ocean views, Indian Ocean sunsets, and a laid-back coastal energy that makes for genuinely memorable celebrations. We love hosting coastal weddings and know the unique logistical considerations these venues bring.",
        "what_we_do": [
            "Beachside ceremony hosting",
            "Reception hosting with ocean views",
            "Bridal party introductions",
            "Speech management in outdoor settings",
            "Coastal venue AV &amp; wind considerations",
            "Personalised script for your wedding",
            "Sunset timing &amp; photography cues",
            "Available for Scarborough &amp; coastal Perth",
        ],
        "why": "Coastal weddings in Scarborough, City Beach, and Trigg require an MC who understands the unique challenges — wind, light changes, outdoor acoustics, and the fluid nature of beachside timing. We've hosted dozens of coastal weddings along Perth's northern beaches and know how to work with the environment, not against it.",
        "nearby": [
            ("wedding-mc-perth.html", "Wedding MC Perth"),
            ("outdoor-wedding-mc-perth.html", "Outdoor Wedding MC"),
            ("wedding-mc-joondalup.html", "Wedding MC Joondalup"),
            ("wedding-mc-subiaco.html", "Wedding MC Subiaco"),
        ],
        "event_type": "Wedding",
        "schema_type": "Event",
    },
    {
        "slug": "wedding-mc-rockingham",
        "title": "Wedding MC Rockingham | Professional Wedding Host | Perth MC",
        "h1": "Wedding MC Rockingham",
        "meta": "Professional wedding MC for Rockingham and Perth's southern suburbs. Experienced, fully tailored, and available for your date. Check availability now.",
        "intro": "Rockingham's coastal setting and growing wedding venue scene make it an increasingly popular choice for Perth couples. Whether you're celebrating at a waterfront venue, a garden estate, or an intimate private property in the southern corridor, we bring the same level of preparation and polish to every event.",
        "what_we_do": [
            "Ceremony &amp; reception hosting",
            "Bridal party introductions",
            "Speech management &amp; timing",
            "Southern Perth venue experience",
            "Personalised script for your wedding",
            "Pre-wedding briefing &amp; run sheet review",
            "Vendor coordination",
            "Available for Rockingham &amp; southern suburbs",
        ],
        "why": "Rockingham sits about 45 minutes south of Perth and we travel there regularly for weddings. We've hosted events in the Rockingham area and throughout Perth's southern corridor, including Secret Harbour and Safety Bay. Contact us to discuss your date and venue — we'd love to be part of your day.",
        "nearby": [
            ("wedding-mc-perth.html", "Wedding MC Perth"),
            ("wedding-mc-mandurah.html", "Wedding MC Mandurah"),
            ("wedding-mc-fremantle.html", "Wedding MC Fremantle"),
            ("outdoor-wedding-mc-perth.html", "Outdoor Wedding MC"),
        ],
        "event_type": "Wedding",
        "schema_type": "Event",
    },
    {
        "slug": "mc-50th-birthday-perth",
        "title": "MC for 50th Birthday Perth | Milestone Birthday Host | Perth MC",
        "h1": "MC for a 50th Birthday Party in Perth",
        "meta": "Professional MC for 50th birthday parties in Perth. Personalised tribute, speech management, and seamless event hosting for milestone celebrations. Check availability.",
        "intro": "A 50th birthday is a once-in-a-lifetime milestone — and it deserves more than a playlist and a friend who 'used to do a bit of public speaking.' The right MC weaves the guest of honour's story through the evening, manages the speeches, and creates moments that guests will be talking about for years.",
        "what_we_do": [
            "Personalised tribute &amp; roast elements",
            "Family &amp; friend speech management",
            "Video tribute &amp; slideshow cuing",
            "Guest entertainment &amp; interactive elements",
            "Toast management &amp; timing",
            "Surprise reveal coordination",
            "Pre-event family briefing",
            "Photography &amp; DJ coordination",
        ],
        "why": "50th birthday parties are unique — the crowd spans multiple generations, the emotions run high, and there's usually a mix of family, old friends, and colleagues who've never met. We know how to bring these different groups together into a single, cohesive evening that celebrates the guest of honour in a way they'll genuinely love.",
        "nearby": [
            ("mc-21st-birthday-perth.html", "MC for 21st Birthday"),
            ("wedding-mc-perth.html", "Wedding MC Perth"),
            ("charity-gala-mc-perth.html", "Charity Gala MC"),
            ("awards-night-mc-perth.html", "Awards Night MC"),
        ],
        "event_type": "SocialEvent",
        "schema_type": "Event",
    },
    {
        "slug": "mc-21st-birthday-perth",
        "title": "MC for 21st Birthday Perth | Birthday Party Host | Perth MC",
        "h1": "MC for a 21st Birthday Party in Perth",
        "meta": "Professional MC for 21st birthday parties in Perth. High energy, personalised, and perfectly pitched for a milestone birthday celebration. Check availability.",
        "intro": "A 21st birthday is a significant milestone — a transition worth celebrating properly. Whether it's a backyard marquee party, a function centre celebration, or something in between, the right MC ensures the night has a shape, the speeches land well, and the guest of honour feels genuinely celebrated.",
        "what_we_do": [
            "High-energy birthday party hosting",
            "Key of the door presentation",
            "Family &amp; friend speech management",
            "Video tribute &amp; slideshow cuing",
            "Guest entertainment &amp; games",
            "Dance floor energy management",
            "Pre-event briefing with family",
            "Photography coordination",
        ],
        "why": "21st birthday parties have a particular energy — they're celebratory, a little nostalgic, and usually involve a mix of family members and the birthday person's friends who don't know each other. We know how to manage the room across those different groups, keep the speeches warm and moving, and make sure the guest of honour's milestone feels exactly as significant as it is.",
        "nearby": [
            ("mc-50th-birthday-perth.html", "MC for 50th Birthday"),
            ("wedding-mc-perth.html", "Wedding MC Perth"),
            ("school-formal-mc-perth.html", "School Formal MC"),
            ("christmas-party-mc-perth.html", "Christmas Party MC"),
        ],
        "event_type": "SocialEvent",
        "schema_type": "Event",
    },
    {
        "slug": "conference-mc-perth",
        "title": "Conference MC Perth | Professional Conference Host | Perth MC",
        "h1": "Conference MC Perth",
        "meta": "Professional conference MC in Perth for single-day and multi-day events. Keynote speaker introductions, panel facilitation, and full conference hosting. Check availability.",
        "intro": "Conferences are among the most logistically demanding events to host. Multiple sessions, diverse speakers, audience Q&amp;A, timing pressures, and the need to maintain energy across a long day — or several days. A professional conference MC is not a luxury; they're the invisible infrastructure that makes everything hold together.",
        "what_we_do": [
            "Full-day &amp; multi-day conference hosting",
            "Keynote speaker introductions",
            "Panel &amp; Q&amp;A facilitation",
            "Session transition management",
            "Audience energy management",
            "AV &amp; technical coordination",
            "Speaker briefing &amp; timing management",
            "Brand &amp; theme alignment",
        ],
        "why": "Perth hosts major industry conferences across sectors including mining, construction, healthcare, technology, and education. We've hosted conferences for organisations of all sizes and understand the unique demands of conference hosting — long days, mixed audiences, technical complexity, and the need to keep 200 professionals engaged after lunch.",
        "nearby": [
            ("corporate-mc-perth.html", "Corporate MC Perth"),
            ("awards-night-mc-perth.html", "Awards Night MC"),
            ("product-launch-mc-perth.html", "Product Launch MC"),
            ("charity-gala-mc-perth.html", "Charity Gala MC"),
        ],
        "event_type": "BusinessEvent",
        "schema_type": "Event",
    },
    {
        "slug": "charity-gala-mc-perth",
        "title": "Charity Gala MC Perth | Fundraiser Event Host | Perth MC",
        "h1": "Charity Gala MC Perth",
        "meta": "Professional MC for charity galas and fundraiser events in Perth. Auction facilitation, cause storytelling, and black tie event hosting. Check availability.",
        "intro": "Charity galas and fundraiser events have a unique dual purpose: they need to be enjoyable social occasions and effective fundraising vehicles. The MC is the bridge between those two goals — keeping the room warm and entertained while also driving genuine engagement with your cause and your auction.",
        "what_we_do": [
            "Charity gala &amp; dinner hosting",
            "Charity auction facilitation",
            "Cause storytelling &amp; mission framing",
            "Paddle bidding management",
            "VIP guest &amp; table management",
            "Keynote &amp; guest speaker support",
            "Dinner program management",
            "Entertainment transition hosting",
        ],
        "why": "Perth's charity sector runs some of the most sophisticated fundraising events in Australia — and the MC plays a central role in how much money is raised. We understand the art of warm fundraising: building emotion around a cause, creating urgency without pressure, and facilitating auctions that maximise results without alienating donors.",
        "nearby": [
            ("awards-night-mc-perth.html", "Awards Night MC"),
            ("black-tie-event-mc-perth.html", "Black Tie Event MC"),
            ("fundraiser-mc-perth.html", "Fundraiser MC Perth"),
            ("conference-mc-perth.html", "Conference MC Perth"),
        ],
        "event_type": "SocialEvent",
        "schema_type": "Event",
    },
    {
        "slug": "school-formal-mc-perth",
        "title": "School Formal MC Perth | Year 12 Formal Host | Perth MC",
        "h1": "School Formal MC Perth",
        "meta": "Professional MC for Perth school formals — Year 12 formals, Year 10 formals, and graduation dinners. Crowd-appropriate, energetic, and experienced. Check availability.",
        "intro": "A school formal is a milestone for students who've worked hard for years — and it deserves a host who understands that significance without being too serious about it. We bring energy, appropriate humour, and the ability to manage a crowd of teenagers and their guests in a way that keeps the night running and the vibe high.",
        "what_we_do": [
            "Formal arrival &amp; entry hosting",
            "Year 12 King &amp; Queen announcements",
            "School leader &amp; principal speeches",
            "Dinner program management",
            "Dance floor energy &amp; engagement",
            "Photo booth &amp; activity cuing",
            "Teacher &amp; organiser briefing",
            "Age-appropriate content &amp; tone",
        ],
        "why": "School formals are logistically complex — there are formal components that need to run smoothly and then a party that needs to build. We've hosted numerous Perth school formals and know how to navigate the transition from dinner to dance floor, keep the important moments feeling significant, and adapt our style to the specific energy of each year group.",
        "nearby": [
            ("awards-night-mc-perth.html", "Awards Night MC"),
            ("mc-21st-birthday-perth.html", "21st Birthday MC"),
            ("corporate-mc-perth.html", "Corporate MC Perth"),
            ("christmas-party-mc-perth.html", "Christmas Party MC"),
        ],
        "event_type": "SocialEvent",
        "schema_type": "Event",
    },
    {
        "slug": "awards-night-mc-perth",
        "title": "Awards Night MC Perth | Professional Awards Ceremony Host | Perth MC",
        "h1": "Awards Night MC Perth",
        "meta": "Professional MC for awards nights in Perth — industry awards, corporate recognition events, and formal award ceremonies. Polished, prepared, and impactful. Check availability.",
        "intro": "Awards nights are among the most high-stakes events to host. Every recipient deserves their moment to feel significant, the program needs to move at pace without feeling rushed, and the overall tone must balance celebration with gravitas. A great awards MC makes every winner feel like the star they are.",
        "what_we_do": [
            "Awards ceremony scripting &amp; presentation",
            "Category &amp; recipient introductions",
            "Award presenter management",
            "Winner acknowledgement &amp; photography timing",
            "Dinner program management",
            "Entertainment transitions",
            "Audience energy management",
            "Industry knowledge &amp; brand alignment",
        ],
        "why": "Perth's awards nights span every industry — from UDIA real estate awards to construction excellence, hospitality, and health sector recognition events. We research each category, each organisation, and each presenter so that every moment of the evening reflects the significance it deserves. No generic scripts, no mispronounced names.",
        "nearby": [
            ("charity-gala-mc-perth.html", "Charity Gala MC"),
            ("black-tie-event-mc-perth.html", "Black Tie Event MC"),
            ("corporate-mc-perth.html", "Corporate MC Perth"),
            ("conference-mc-perth.html", "Conference MC Perth"),
        ],
        "event_type": "BusinessEvent",
        "schema_type": "Event",
    },
    {
        "slug": "christmas-party-mc-perth",
        "title": "MC for Christmas Party Perth | Corporate Christmas Event Host | Perth MC",
        "h1": "MC for Christmas Party Perth",
        "meta": "Professional MC for corporate Christmas parties in Perth. Year-end event hosting, awards, entertainment facilitation, and team energy. Check availability for December.",
        "intro": "Corporate Christmas parties should be the highlight of the year — a chance to celebrate achievements, acknowledge people, and send the team into the holidays on a high. Too often they're forgettable. The difference is usually in how the night is hosted.",
        "what_we_do": [
            "Year-end event &amp; party hosting",
            "Awards &amp; recognition presentation",
            "Entertainment facilitation",
            "Team energising &amp; engagement",
            "Activity &amp; game hosting",
            "Dinner program management",
            "DJ transition management",
            "Brand-aligned hosting style",
        ],
        "why": "Perth's corporate Christmas party season runs from late November through December — and popular dates book fast. We've hosted year-end events for small teams of 20 and company-wide celebrations of 500+. If you want your people to actually enjoy the night and leave feeling valued, the hosting matters more than the venue.",
        "nearby": [
            ("corporate-mc-perth.html", "Corporate MC Perth"),
            ("awards-night-mc-perth.html", "Awards Night MC"),
            ("team-building-mc-perth.html", "Team Building MC"),
            ("conference-mc-perth.html", "Conference MC Perth"),
        ],
        "event_type": "SocialEvent",
        "schema_type": "Event",
    },
    {
        "slug": "product-launch-mc-perth",
        "title": "MC for Product Launch Perth | Brand Event Host | Perth MC",
        "h1": "MC for Product Launches &amp; Brand Events Perth",
        "meta": "Professional MC for product launches and brand events in Perth. Brand-aligned hosting, media management, panel facilitation, and keynote support. Check availability.",
        "intro": "A product launch is a brand moment — and the MC is the voice of your brand on the night. Every word, every transition, and every energy shift needs to align with what you're trying to communicate. This is not the night for a generalist. It's the night for an MC who has done their homework.",
        "what_we_do": [
            "Product reveal facilitation",
            "Brand-aligned hosting style",
            "Media &amp; influencer management",
            "Panel &amp; Q&amp;A hosting",
            "Keynote speaker support",
            "Demo &amp; activation cuing",
            "Guest experience management",
            "Post-launch networking facilitation",
        ],
        "why": "Perth's business community launches products, services, and campaigns regularly — and the quality of the event reflects directly on the brand. We research your product, your positioning, and your audience before every launch, so the hosting feels authentic rather than announced. We've worked with brands across retail, technology, health, property, and consumer goods.",
        "nearby": [
            ("corporate-mc-perth.html", "Corporate MC Perth"),
            ("conference-mc-perth.html", "Conference MC Perth"),
            ("awards-night-mc-perth.html", "Awards Night MC"),
            ("christmas-party-mc-perth.html", "Christmas Party MC"),
        ],
        "event_type": "BusinessEvent",
        "schema_type": "Event",
    },
    {
        "slug": "outdoor-wedding-mc-perth",
        "title": "Outdoor Wedding MC Perth | Ceremony &amp; Garden Wedding Host | Perth MC",
        "h1": "Outdoor Wedding MC Perth",
        "meta": "Professional outdoor wedding MC in Perth. Experienced with garden ceremonies, beachside weddings, vineyard receptions, and all outdoor Perth venues. Check availability.",
        "intro": "Outdoor weddings in Perth are spectacular — and logistically more demanding than indoor events. Wind, light, acoustics, timing around sunset, managing guests on grass, and adapting when the weather has ideas of its own. An experienced outdoor wedding MC handles all of this without your guests ever noticing.",
        "what_we_do": [
            "Garden ceremony &amp; reception hosting",
            "Beachside &amp; coastal wedding hosting",
            "Swan Valley &amp; vineyard wedding experience",
            "Outdoor acoustics &amp; microphone management",
            "Sunset timing &amp; photography window cues",
            "Wind &amp; weather contingency planning",
            "Marquee &amp; tent event experience",
            "Outdoor guest management",
        ],
        "why": "Perth has some of Australia's most beautiful outdoor wedding venues — and we've MC'd at most of them. Swan Valley wineries, Kings Park, beachside locations from City Beach to Cottesloe, garden estates in the hills, and private properties across the metro area. Each outdoor venue has its own character and challenges — we know them all.",
        "nearby": [
            ("wedding-mc-perth.html", "Wedding MC Perth"),
            ("wedding-mc-scarborough.html", "Wedding MC Scarborough"),
            ("wedding-mc-fremantle.html", "Wedding MC Fremantle"),
            ("wedding-mc-subiaco.html", "Wedding MC Subiaco"),
        ],
        "event_type": "Wedding",
        "schema_type": "Event",
    },
    {
        "slug": "black-tie-event-mc-perth",
        "title": "Black Tie Event MC Perth | Formal Gala Host | Perth MC",
        "h1": "Black Tie Event MC Perth",
        "meta": "Professional MC for black tie events in Perth — gala dinners, formal awards nights, and charity fundraisers. Polished, commanding, and experienced with formal protocol.",
        "intro": "Black tie events demand a different standard of hosting — polished, commanding, and fully aware of the protocols that make these occasions feel significant. Perth MC has hosted numerous black tie events in Perth and understands how to hold a room of discerning, formally dressed guests.",
        "what_we_do": [
            "Black tie gala dinner hosting",
            "Formal awards ceremony presentation",
            "VIP guest &amp; head table management",
            "Charity auction facilitation",
            "Formal protocol adherence",
            "Entertainment &amp; speaker transitions",
            "Dinner program management",
            "Post-dinner &amp; dancing transition",
        ],
        "why": "Perth hosts black tie events across the charity, corporate, and social sectors — from the major hospital foundation galas to industry black tie awards and private formal celebrations. These events have specific protocols and expectations. We know them, we follow them, and we make the evening feel exactly as distinguished as it should.",
        "nearby": [
            ("charity-gala-mc-perth.html", "Charity Gala MC"),
            ("awards-night-mc-perth.html", "Awards Night MC"),
            ("fundraiser-mc-perth.html", "Fundraiser MC Perth"),
            ("corporate-mc-perth.html", "Corporate MC Perth"),
        ],
        "event_type": "SocialEvent",
        "schema_type": "Event",
    },
    {
        "slug": "fundraiser-mc-perth",
        "title": "Fundraiser MC Perth | Charity &amp; Fundraising Event Host | Perth MC",
        "h1": "Fundraiser MC Perth",
        "meta": "Professional MC for fundraising events in Perth. Charity dinners, silent auctions, paddle auctions, and gala fundraisers — we help you raise more. Check availability.",
        "intro": "Fundraising events are about more than entertainment — they're about connection to a cause and the motivation to give. The right MC doesn't just host the room; they help raise the room. How the cause is framed, when the asks are made, and how momentum is maintained throughout the evening can make a significant difference to what's raised.",
        "what_we_do": [
            "Charity dinner &amp; fundraiser hosting",
            "Silent &amp; live auction facilitation",
            "Paddle bidding management",
            "Cause framing &amp; storytelling",
            "Donor acknowledgement",
            "Keynote &amp; impact speaker support",
            "Entertainment transitions",
            "Pledge &amp; donation management",
        ],
        "why": "We've worked with organisations across Perth's charity sector — hospitals, youth services, disability support, environmental causes, and arts organisations. Every fundraiser is different: different causes, different audiences, different giving cultures. We research each one and tailor our approach accordingly.",
        "nearby": [
            ("charity-gala-mc-perth.html", "Charity Gala MC"),
            ("black-tie-event-mc-perth.html", "Black Tie Event MC"),
            ("awards-night-mc-perth.html", "Awards Night MC"),
            ("corporate-mc-perth.html", "Corporate MC Perth"),
        ],
        "event_type": "SocialEvent",
        "schema_type": "Event",
    },
    {
        "slug": "team-building-mc-perth",
        "title": "MC for Team Building Events Perth | Corporate Team Host | Perth MC",
        "h1": "MC for Team Building Events Perth",
        "meta": "Professional MC for team building events in Perth. Activity hosting, group facilitation, corporate team days, and staff engagement events. Check availability.",
        "intro": "Team building events are notoriously hit or miss — and the hosting is usually the difference. An MC who can facilitate activities with genuine energy, keep a diverse group engaged, and transition smoothly between structured and social elements can make your team day something people actually remember positively.",
        "what_we_do": [
            "Team day &amp; activity facilitation",
            "Group challenge &amp; competition hosting",
            "Quiz &amp; trivia facilitation",
            "Awards &amp; recognition presentation",
            "Breakout session management",
            "Dinner &amp; social event hosting",
            "Multi-group logistics management",
            "Energy management across long days",
        ],
        "why": "Perth businesses invest significantly in team building — and we've seen what separates the events people talk about from the ones they quietly dreaded. It comes down to facilitation. We make activities genuinely competitive and fun, we read the group dynamic quickly, and we ensure the day has genuine energy from start to finish.",
        "nearby": [
            ("corporate-mc-perth.html", "Corporate MC Perth"),
            ("christmas-party-mc-perth.html", "Christmas Party MC"),
            ("conference-mc-perth.html", "Conference MC Perth"),
            ("awards-night-mc-perth.html", "Awards Night MC"),
        ],
        "event_type": "BusinessEvent",
        "schema_type": "Event",
    },
]


def build_page(page):
    what_we_do_items = "\n".join(
        f"          <li>{item}</li>" for item in page["what_we_do"]
    )
    nearby_links = "\n".join(
        f'          <a href="{href}">{label}</a>' for href, label in page["nearby"]
    )
    schema = f"""{{
  "@context": "https://schema.org",
  "@type": "{page['schema_type']}",
  "name": "{page['h1']}",
  "description": "{page['meta']}",
  "location": {{
    "@type": "City",
    "name": "Perth",
    "addressCountry": "AU"
  }},
  "organizer": {{
    "@type": "LocalBusiness",
    "name": "Perth MC",
    "url": "https://perthmc.com"
  }}
}}"""

    header = HEADER.format(
        meta=page["meta"],
        title=page["title"],
        slug=page["slug"],
    )
    body = f"""
<!-- ── HERO ── -->
<section class="landing-hero">
  <div class="container">
    <div class="hero-badge">&#10022; Perth MC</div>
    <h1>{page['h1']}</h1>
    <p>{page['intro']}</p>
    <div class="hero-cta">
      <a href="contact.html" class="btn btn-primary btn-lg">Check Availability</a>
      <a href="services.html" class="btn btn-outline-white btn-lg">View All Services</a>
    </div>
  </div>
</section>

<!-- ── STATS BAR ── -->
<div class="stats-bar">
  <div class="container stats-inner">
    <div class="stat"><div class="stat-num">500+</div><div class="stat-label">Events Hosted</div></div>
    <div class="stat"><div class="stat-num">10+</div><div class="stat-label">Years Experience</div></div>
    <div class="stat"><div class="stat-num">5.0★</div><div class="stat-label">Client Rating</div></div>
    <div class="stat"><div class="stat-num">24hr</div><div class="stat-label">Response Time</div></div>
  </div>
</div>

<!-- ── MAIN CONTENT ── -->
<section class="section-pad">
  <div class="container landing-content">
    <div>
      <h2 style="font-size:1.5rem;margin-bottom:16px;">What We Provide</h2>
      <ul class="checklist" style="margin-bottom:32px;">
{what_we_do_items}
      </ul>

      <h2 style="font-size:1.5rem;margin-bottom:16px;">Why Perth MC?</h2>
      <p style="color:var(--muted);font-size:0.97rem;line-height:1.75;margin-bottom:24px;">{page['why']}</p>

      <div class="nearby-events">
        <h3>Related Services</h3>
        <div class="nearby-list">
{nearby_links}
        </div>
      </div>
    </div>

    <div>
      <div class="form-card-light">
        <h3>Check Availability</h3>
        <p class="card-sub">Tell us about your event and we'll confirm availability within 24 hours.</p>
        <form action="https://formspree.io/f/YOUR_FORM_ID" method="POST" data-formspree data-success-id="{page['slug']}-success">
          <div class="form-group">
            <label for="{page['slug']}-name">Full Name *</label>
            <input type="text" id="{page['slug']}-name" name="name" placeholder="Jane Smith" required />
          </div>
          <div class="form-group">
            <label for="{page['slug']}-phone">Phone *</label>
            <input type="tel" id="{page['slug']}-phone" name="phone" placeholder="04XX XXX XXX" required />
          </div>
          <div class="form-group">
            <label for="{page['slug']}-email">Email *</label>
            <input type="email" id="{page['slug']}-email" name="email" placeholder="jane@example.com" required />
          </div>
          <div class="form-group">
            <label for="{page['slug']}-event">Event Type</label>
            <input type="text" id="{page['slug']}-event" name="event_type" value="{page['event_type']}" />
          </div>
          <div class="form-group">
            <label for="{page['slug']}-date">Event Date *</label>
            <input type="date" id="{page['slug']}-date" name="event_date" required />
          </div>
          <div class="form-group">
            <label for="{page['slug']}-notes">Tell Us About Your Event</label>
            <textarea id="{page['slug']}-notes" name="message" rows="4" placeholder="Venue, guest numbers, any special requirements…"></textarea>
          </div>
          <button type="submit" class="btn btn-primary btn-full">Check Availability &rarr;</button>
        </form>
        <div id="{page['slug']}-success" class="form-success-light" hidden>
          <h3>&#10003; Thanks! We'll be in touch within 24 hours.</h3>
          <p>We've received your enquiry and will confirm availability shortly.</p>
        </div>
      </div>
    </div>
  </div>
</section>
"""

    footer = FOOTER.format(schema=schema)
    return header + body + footer


def main():
    for page in LANDING_PAGES:
        slug = page["slug"]
        html = build_page(page)
        out_path = os.path.join(BASE_DIR, f"{slug}.html")
        with open(out_path, "w") as f:
            f.write(html)
        print(f"Generated: {slug}.html")
    print(f"\nDone — {len(LANDING_PAGES)} landing pages generated.")


if __name__ == "__main__":
    main()
