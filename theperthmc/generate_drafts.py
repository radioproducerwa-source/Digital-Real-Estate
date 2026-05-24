#!/usr/bin/env python3
"""Generate all 28 draft blog posts for The Perth MC.
Run from the theperthmc/ directory: python3 generate_drafts.py
Generates draft HTML files in theperthmc/drafts/
"""

import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DRAFTS_DIR = os.path.join(BASE_DIR, "drafts")

HEADER = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="{meta}" />
  <meta name="robots" content="noindex, nofollow" />
  <title>{title}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../css/style.css" />
</head>
<body>

<header class="site-header">
  <div class="container header-inner">
    <a href="../index.html" class="logo">The Perth<span>MC</span></a>
    <nav class="main-nav" id="main-nav">
      <a href="../index.html">Home</a>
      <a href="../services.html">Services</a>
      <a href="../about.html">About</a>
      <a href="../blog.html">Blog</a>
      <a href="../contact.html" class="btn btn-primary">Check Availability</a>
    </nav>
    <div class="header-right">
      <button class="hamburger" id="hamburger" aria-label="Open menu" aria-expanded="false">&#9776;</button>
    </div>
  </div>
</header>

<section class="blog-hero">
  <div class="container">
    <a href="../blog.html" class="blog-back">&larr; Back to Blog</a>
    <h1>{h1}</h1>
    <div class="blog-meta">{tag} &nbsp;&middot;&nbsp; {read_time} min read</div>
  </div>
</section>
"""

FOOTER = """
<section class="cta-band">
  <div class="container">
    <h2>Planning an Event in Perth?</h2>
    <p>Check availability for your date — we respond within 24 hours.</p>
    <a href="../contact.html" class="btn btn-primary btn-lg">Check Availability</a>
  </div>
</section>

<footer class="site-footer">
  <div class="container">
    <div class="footer-top">
      <div class="footer-brand">
        <a href="../index.html" class="logo">The Perth<span>MC</span></a>
        <p>Perth's professional MC for weddings, corporate events, galas, conferences, and milestone celebrations.</p>
      </div>
      <div class="footer-links">
        <h4>Quick Links</h4>
        <ul>
          <li><a href="../index.html">Home</a></li>
          <li><a href="../services.html">Services</a></li>
          <li><a href="../about.html">About</a></li>
          <li><a href="../blog.html">Blog</a></li>
          <li><a href="../contact.html">Contact</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2026 The Perth MC. All rights reserved.</p>
    </div>
  </div>
</footer>
<script src="../js/main.js"></script>
</body>
</html>
"""

CTA_BOX = """<div class="blog-cta-box">
  <h3>Need a Professional MC for Your Event?</h3>
  <p>Perth-based, experienced across all event types, and available to discuss your date.</p>
  <a href="../contact.html" class="btn btn-primary">Check Availability</a>
</div>"""

DRAFTS = [
    {
        "slug": "blog-why-hire-professional-mc-vs-friend",
        "title": "Why Hire a Professional MC Instead of a Friend? | The Perth MC",
        "h1": "Why Hire a Professional MC Instead of a Friend?",
        "meta": "The honest case for hiring a professional MC over a willing friend — and what the difference looks like on the night.",
        "tag": "Planning", "read_time": 5,
        "content": """<div class="blog-body">
<p>It's a conversation that happens at almost every wedding planning session: "My mate is really funny and great with people — could he do the MC?" The answer is almost always: it's a risk. Here's why.</p>
<h2>Your Friend Is a Guest</h2>
<p>The fundamental conflict is simple. Your friend is also attending your wedding. They want to drink, chat with people they haven't seen in years, and enjoy the celebration. Every time the MC role calls for focus and attention, that conflicts with being a present guest. Something gives — and it's usually the hosting.</p>
<h2>Being Funny Is Not the Same as Being an MC</h2>
<p>Event hosting is a specific skill. It requires preparation, run sheet management, vendor coordination, speech timing, reading a room, handling the unexpected, and keeping 150 people's experience running smoothly — simultaneously. Being charming and funny in social situations is a very different capability.</p>
<h2>The Cost of Getting It Wrong</h2>
<p>A mediocre professional MC produces a fine night. A friend who struggles with the role produces memories of awkward pauses, overrun speeches, missed cues, and an evening that felt like it never quite found its rhythm. These aren't abstract risks — they're the most common feedback from couples who went with a friend.</p>
<h2>What Your Friend Will Actually Thank You For</h2>
<p>Most friends who are asked to MC are quietly relieved when they're let off the hook. The responsibility of running someone's wedding or major event is significant. Letting them celebrate as a guest — fully, without obligation — is often the greater gift.</p>
""" + CTA_BOX + "</div>",
    },
    {
        "slug": "blog-wedding-mc-mistakes-to-avoid",
        "title": "Wedding MC Mistakes to Avoid | The Perth MC",
        "h1": "Wedding MC Mistakes to Avoid (And How to Prevent Them)",
        "meta": "The most common wedding MC mistakes — from over-running speeches to missed cues — and how to prevent every one of them.",
        "tag": "Weddings", "read_time": 6,
        "content": """<div class="blog-body">
<p>After hosting hundreds of Perth weddings, certain mistakes appear reliably. Most are preventable. Here's the list — and how to avoid every one.</p>
<h2>1. No Pre-Event Briefing</h2>
<p>An MC who shows up on the day without a detailed briefing is operating blind. They don't know the family dynamics, the inside references, the moments to handle carefully, or the couple's vision for the evening. A thorough pre-wedding briefing call is non-negotiable.</p>
<h2>2. Generic Introductions</h2>
<p>Reading a name and title from a card is not an introduction — it's an announcement. Every bridal party member deserves a specific, warm, personalised introduction that makes the audience actually happy to see them walk through the door.</p>
<h2>3. No Speech Timing Plan</h2>
<p>Speeches that aren't timed will overrun. Always. Brief speakers on their allocated time, brief the MC to signal when time is up, and build buffer time into the run sheet. A reception that runs 45 minutes behind by the cake cutting never fully recovers.</p>
<h2>4. Fighting the Run Sheet</h2>
<p>Experienced MCs work with the run sheet, not around it. Improvising transitions, skipping elements, or changing the order on the night without communicating it to the venue and DJ creates confusion and gaps.</p>
<h2>5. Forgetting to Enjoy the Room</h2>
<p>The best wedding MCs are present — genuinely enjoying the evening and communicating that enjoyment to the room. An MC who is visibly managing logistics rather than hosting is not serving the celebration well.</p>
""" + CTA_BOX + "</div>",
    },
    {
        "slug": "blog-how-to-brief-wedding-mc",
        "title": "How to Brief a Wedding MC — The Complete Guide | The Perth MC",
        "h1": "How to Brief a Wedding MC — The Complete Guide",
        "meta": "Everything your MC needs to know before your wedding day — and exactly when and how to give it to them.",
        "tag": "Weddings", "read_time": 6,
        "content": """<div class="blog-body">
<p>The quality of your MC on the night is largely determined by the quality of your briefing. Here's everything they need and when to provide it.</p>
<h2>At Booking: The Big Picture</h2>
<ul><li>Wedding date, venue, and rough timeline</li><li>Number of guests and event style (formal, relaxed, etc.)</li><li>Your story as a couple — how you met, key moments</li><li>Any cultural elements or special requirements</li></ul>
<h2>2–4 Weeks Out: The Detail</h2>
<ul><li>Complete run sheet with times and durations</li><li>Full bridal party list with names, relationships, and one personalised detail for each</li><li>Speaker list with names, relationships, bios, and allocated times</li><li>Pronunciation guide for any non-English names</li><li>Contact details for venue coordinator and DJ/band</li></ul>
<h2>1 Week Out: Confirmation and Nuance</h2>
<ul><li>Any changes to the run sheet</li><li>Family dynamics to be aware of (divorced parents, estranged relatives, etc.)</li><li>Any surprises or off-program moments planned</li><li>Confirmed ceremony end time</li><li>MC call time and venue access details</li></ul>
<h2>The Briefing Call</h2>
<p>Send the written briefing, then schedule a 30–45 minute call to discuss it. The call is where nuance happens — things that are hard to put in a document but essential to get right on the night.</p>
""" + CTA_BOX + "</div>",
    },
    {
        "slug": "blog-conference-mc-checklist",
        "title": "Conference MC Checklist for Event Organisers | The Perth MC",
        "h1": "Conference MC Checklist for Event Organisers",
        "meta": "Everything your conference MC needs from you — and everything to confirm before the day. A practical checklist for organisers.",
        "tag": "Corporate", "read_time": 5,
        "content": """<div class="blog-body">
<p>A well-briefed conference MC is one of the best investments you can make in your event's success. Here's the complete checklist.</p>
<h2>2+ Weeks Before</h2>
<ul><li>Share the complete run sheet (all sessions, breaks, meals)</li><li>Provide speaker bios and confirm pronunciation of all names</li><li>Share event theme, key messages, and organisational context</li><li>Confirm dress code</li><li>Schedule a briefing call with the event organiser</li></ul>
<h2>1 Week Before</h2>
<ul><li>Send updated run sheet with any changes</li><li>Confirm AV contact and technical setup</li><li>Share audience profile (seniority, industry, approximate numbers)</li><li>Confirm any VIP acknowledgements required</li><li>Confirm MC call time and venue access</li></ul>
<h2>Day Before</h2>
<ul><li>Final run sheet confirmation</li><li>Confirm any last-minute program changes</li><li>Venue logistics confirmation (parking, AV test time)</li></ul>
<h2>Day Of</h2>
<ul><li>MC arrives 60–90 minutes before first session</li><li>AV sound check</li><li>MC meets with venue coordinator and AV team</li><li>Brief run-through with key staff</li></ul>
""" + CTA_BOX + "</div>",
    },
    {
        "slug": "blog-awards-night-timeline-guide",
        "title": "Awards Night Timeline — A Complete MC Guide | The Perth MC",
        "h1": "Awards Night Timeline — A Complete MC Guide",
        "meta": "How to structure an awards night program so it moves at pace, gives every winner their moment, and ends on a high.",
        "tag": "Events", "read_time": 6,
        "content": """<div class="blog-body">
<p>Awards nights have a particular pacing challenge: too slow and the room loses energy between categories; too fast and winners feel rushed. Here's the structure that works.</p>
<h2>A Workable Awards Night Timeline</h2>
<ul>
<li><strong>6:00–7:00 PM</strong> — Arrival drinks and networking</li>
<li><strong>7:00 PM</strong> — Guests seated, MC welcome and housekeeping</li>
<li><strong>7:10 PM</strong> — Entrée service, background entertainment</li>
<li><strong>7:40 PM</strong> — First award category (2–3 categories before main course)</li>
<li><strong>8:10 PM</strong> — Main course service (brief entertainment or guest speaker)</li>
<li><strong>8:40 PM</strong> — Resume awards presentation (bulk of categories)</li>
<li><strong>9:40 PM</strong> — Major award of the night (saved for maximum impact)</li>
<li><strong>9:55 PM</strong> — Dessert, close of formal program</li>
<li><strong>10:15 PM</strong> — Networking, dancing if applicable</li>
</ul>
<h2>Managing Award Pacing</h2>
<p>Each award category should take 3–5 minutes: presenter walks to stage, MC introduces them (30 sec), presenter announces and reads the citation (90 sec), winner accepts and speaks (60–90 sec), photography (30 sec), transition to next. Any longer and the night becomes a test of endurance.</p>
<h2>The Major Award</h2>
<p>Save your highest-profile award for last. Build to it with specific acknowledgement of the category's significance. The winner of the final award should leave the stage to the highest energy of the evening.</p>
""" + CTA_BOX + "</div>",
    },
    {
        "slug": "blog-how-to-plan-fundraiser-dinner-perth",
        "title": "How to Plan a Fundraiser Dinner in Perth | The Perth MC",
        "h1": "How to Plan a Fundraiser Dinner in Perth",
        "meta": "A step-by-step guide to planning a fundraiser dinner in Perth — venue, program structure, entertainment, auction, and MC briefing.",
        "tag": "Events", "read_time": 6,
        "content": """<div class="blog-body">
<p>A fundraiser dinner done well raises significant money and leaves donors feeling genuinely good about their contribution. Done poorly, it raises less than expected and leaves people feeling sold to. The difference is in the planning.</p>
<h2>Set a Clear Financial Goal</h2>
<p>Before any other decision, establish what you're trying to raise, how (ticket sales, auction, direct ask, sponsorship), and what success looks like. Every planning decision — venue, ticket price, program length, entertainment spend — flows from this number.</p>
<h2>Venue: Capacity and Atmosphere</h2>
<p>The venue needs to seat your guest list comfortably and support the emotional atmosphere you're trying to create. A cause that works with intimate connection needs a venue that facilitates it. A gala-scale fundraiser needs space, production values, and AV that can carry the program to the back row.</p>
<h2>Program Structure</h2>
<p>The most effective fundraiser dinner programs: open with cause context (not money), build emotional connection through storytelling and impact, intersperse entertainment to maintain energy, place the financial ask at the moment of maximum emotional engagement, and close warmly with gratitude.</p>
<h2>The Auction</h2>
<p>Auction lots should be genuinely desirable — experiences, access, and exclusivity outperform physical goods. Brief your MC on each lot so they can sell it authentically. A live auction with 8–12 well-chosen lots almost always outperforms a silent auction alone.</p>
<h2>MC Briefing</h2>
<p>Your MC needs to understand the cause deeply, know the impact stories, be briefed on each auction lot, and understand the emotional arc of the evening. A fundraiser MC who hasn't been briefed is a fundraising liability.</p>
""" + CTA_BOX + "</div>",
    },
    {
        "slug": "blog-gala-dinner-program-guide",
        "title": "Gala Dinner Program Guide — Getting the Order Right | The Perth MC",
        "h1": "Gala Dinner Program Guide — Getting the Order Right",
        "meta": "The order of a gala dinner program matters more than most organisers realise. How to sequence content, entertainment, and program elements for maximum impact.",
        "tag": "Events", "read_time": 5,
        "content": """<div class="blog-body">
<p>The sequence of a gala dinner program directly affects how engaged guests are, how much is raised (if it's a fundraiser), and how the evening is remembered. Here's how to get the order right.</p>
<h2>The Core Principle: Build, Then Peak</h2>
<p>A well-structured gala dinner builds emotional and social energy across the evening, reaching its peak at the major moment — the keynote, the major award, or the fundraising ask — before relaxing into a social close. Programs that front-load heavy content exhaust guests before the significant moments; programs that back-load everything leave the dining portion feeling directionless.</p>
<h2>Arrival and Pre-Dinner</h2>
<p>The pre-dinner drinks period sets expectations. Use it for networking — light background music, canapés, and minimal formal content. Save the microphone for when guests are seated and focused.</p>
<h2>First Course: Establish, Don't Demand</h2>
<p>During the entrée, the program should be light — a brief MC welcome, essential housekeeping, and at most one short program element. Guests are still orienting themselves to the evening.</p>
<h2>Main Course: Sustain and Build</h2>
<p>The main course period is where the bulk of the content program runs — awards, keynotes, short-form entertainment. Energy has been established; guests are settled and ready to engage.</p>
<h2>Dessert and Close: Peak and Release</h2>
<p>Save your most significant moment for after main course is cleared — when guests are comfortable, slightly relaxed, and the evening's emotional investment is at its highest. Close warmly, give people a reason to celebrate, and transition to networking or dancing with genuine energy.</p>
""" + CTA_BOX + "</div>",
    },
    {
        "slug": "blog-mc-for-outdoor-events-perth",
        "title": "MC for Outdoor Events — Tips for Perth's Alfresco Season | The Perth MC",
        "h1": "MC for Outdoor Events — Tips for Perth's Alfresco Season",
        "meta": "Outdoor events in Perth are spectacular — and distinctly more challenging to host. What every event organiser and MC needs to know.",
        "tag": "Planning", "read_time": 5,
        "content": """<div class="blog-body">
<p>Perth's outdoor event season runs from roughly September through April — and the conditions that make alfresco events beautiful also make them genuinely more demanding to host. Here's what to plan for.</p>
<h2>Sound: The Biggest Variable</h2>
<p>Outdoor acoustics are unpredictable. Sound disperses, wind interferes with microphones, and ambient noise competes with the program. The investment in a quality PA system with appropriate speaker placement is non-negotiable for outdoor events above 50 guests. Test the system in the actual outdoor space before guests arrive.</p>
<h2>Wind Management</h2>
<p>Perth's Fremantle Doctor arrives reliably from the south-west in spring and summer afternoons. For events with late afternoon outdoor components, wind management should be part of your site plan. Windbreaks, mic placement, and script management (holding papers in wind is harder than it sounds) all matter.</p>
<h2>Timing Around the Sun</h2>
<p>Outdoor events in Perth mean working with the light. Build your run sheet around the sun — golden hour for photography, sunset transitions managed intentionally, and evening elements timed to begin when the light is right rather than fighting it.</p>
<h2>Wet Weather Plan</h2>
<p>Perth weather is generally reliable but never certain. Every outdoor event needs a wet weather contingency. Your MC should know the plan before the day — not be informed of it when it starts raining.</p>
<h2>Hydration and Shade</h2>
<p>A simple one often overlooked: ensure your MC has access to shade and water throughout the event. Hosting outdoors for 4–6 hours in Perth summer heat without either is a voice and energy management problem.</p>
""" + CTA_BOX + "</div>",
    },
    {
        "slug": "blog-how-to-handle-last-minute-changes",
        "title": "How to Handle Last-Minute Event Changes as an MC | The Perth MC",
        "h1": "How to Handle Last-Minute Event Changes as an MC",
        "meta": "Events never go exactly to plan. The techniques experienced MCs use to adapt in real time — from late speakers to AV failures to on-the-night program changes.",
        "tag": "Craft", "read_time": 5,
        "content": """<div class="blog-body">
<p>In ten-plus years of event hosting, I've never hosted an event that went exactly to the run sheet. The speaker who flew in from Sydney is stuck in traffic. The AV drops out during the keynote. The venue is running 20 minutes behind on the meal service. These are not exceptional circumstances — they're the normal texture of live events. Here's how to handle them.</p>
<h2>The Pre-Event Contingency Conversation</h2>
<p>Before every event, have a brief conversation with the organiser and venue coordinator: "What are the two or three things most likely to go off-plan tonight, and what do we do if they do?" This conversation means that when something shifts on the night, you're executing a plan rather than improvising under pressure.</p>
<h2>The Audience Knows Less Than You Think</h2>
<p>When something changes on the night, the audience rarely knows it's a deviation from the plan — unless you tell them. Manage program changes quietly, fill time smoothly, and communicate any necessary information to guests in a way that maintains confidence rather than creating anxiety. "We have a brief moment before our next speaker joins us" is better than "We're running late."</p>
<h2>Buy Time Gracefully</h2>
<p>Every experienced MC has techniques for filling unexpected gaps: brief, engaging observations about the evening; inviting table conversations; transitioning to a different element earlier than planned. The key is having these tools ready so they can be deployed without visible preparation.</p>
<h2>Communicate Changes to Vendors Immediately</h2>
<p>When the program shifts, the DJ, venue coordinator, and photographer need to know. A 15-minute delay that the MC is managing smoothly becomes a problem if the kitchen is about to send out main course on the old timing. Communication between vendors on the night is the MC's responsibility.</p>
""" + CTA_BOX + "</div>",
    },
    {
        "slug": "blog-corporate-run-sheet-template",
        "title": "Corporate Event Run Sheet Template | The Perth MC",
        "h1": "Corporate Event Run Sheet Template — What to Include",
        "meta": "A practical template for corporate event run sheets — every field your MC, AV team, and venue coordinator needs.",
        "tag": "Corporate", "read_time": 5,
        "content": """<div class="blog-body">
<p>A great run sheet is the shared truth that keeps all your vendors working together. Here's the template format that works for corporate events of any scale.</p>
<h2>The Core Columns</h2>
<ul>
<li><strong>Time:</strong> Scheduled start time for each element</li>
<li><strong>Duration:</strong> How long the element runs</li>
<li><strong>Element:</strong> What's happening (session, break, meal, speaker, etc.)</li>
<li><strong>Responsibility:</strong> Who's managing this element (MC, venue, AV, speaker)</li>
<li><strong>Notes:</strong> Special instructions, AV requirements, room setup changes</li>
</ul>
<h2>Speaker Information Block</h2>
<p>For every speaker, include: full name (confirmed pronunciation), title and organisation, session topic, allocated time, AV requirements (slides, clicker, lapel vs handheld mic), and the MC introduction text (or a briefing note for the MC to prepare it).</p>
<h2>Transition Notes</h2>
<p>Between every element, note what music plays (if any), whether guests move or stay, and any room setup changes needed. Transitions are where lost time accumulates — the more specific your notes, the tighter your transitions.</p>
<h2>Contact List</h2>
<p>Add a contact block at the top or bottom of the run sheet: MC name and mobile, venue coordinator name and mobile, AV technician name and mobile, and any key speaker contacts. Every vendor should have every other vendor's mobile number.</p>
<h2>Distribution</h2>
<p>Send the final run sheet to all vendors at least 5 business days before the event. Mark it with a version number and date — when you send updates, everyone knows which version is current.</p>
""" + CTA_BOX + "</div>",
    },
    {
        "slug": "blog-wedding-entertainment-perth-guide",
        "title": "How to Choose Wedding Entertainment in Perth | The Perth MC",
        "h1": "How to Choose Wedding Entertainment in Perth",
        "meta": "Bands, DJs, soloists, photo booths, and everything in between. A guide to wedding entertainment in Perth and how it works with your MC.",
        "tag": "Weddings", "read_time": 6,
        "content": """<div class="blog-body">
<p>Wedding entertainment choices set the atmosphere from the moment guests arrive — and the right combination depends on your venue, your guest profile, and the experience you want to create. Here's how to navigate the options.</p>
<h2>Ceremony Music</h2>
<p>A live musician (acoustic guitarist, string quartet, solo vocalist) elevates a ceremony significantly over a Spotify playlist. The ability to extend or compress a piece to match the bridal party's pace is a practical advantage that recordings can't provide. For outdoor Perth ceremonies, confirm the musician can play without amplification if needed.</p>
<h2>Cocktail Hour</h2>
<p>Background music during cocktails should facilitate conversation — present enough to create atmosphere, quiet enough to talk over. A jazz trio, acoustic duo, or solo pianist is ideal. Volume is everything: test it at cocktail hour level, not reception level.</p>
<h2>Reception: Band vs DJ</h2>
<p>Live bands create an energy and visual spectacle that DJ sets can't replicate — but they cost more, require more space, and have a finite song list. DJs offer infinite musical range, can read the room and pivot instantly, and generally cost less. Many couples use a band for the first hour of dancing and a DJ for the remainder — the best of both.</p>
<h2>Entertainment Elements</h2>
<p>Photo booths, caricature artists, lawn games during cocktails, and interactive elements add texture to the evening and give guests something to do during transitions. Brief your MC on any entertainment elements so they can facilitate and announce them at the right moment.</p>
<h2>Coordinating Entertainment with Your MC</h2>
<p>Your MC needs to know every entertainment element, when it starts, and what their role is in facilitating it. A photo booth that opens without announcement gets 20% of the usage it would get with a proper MC call-out. Brief your MC as if they're part of the entertainment team — because they are.</p>
""" + CTA_BOX + "</div>",
    },
    {
        "slug": "blog-what-is-mc-rider-explained",
        "title": "What Is an MC Rider? Event Hosting Costs Explained | The Perth MC",
        "h1": "What Is an MC Rider? Event Hosting Costs Explained",
        "meta": "Some MCs have riders — requirements beyond their fee. What a rider is, what it typically includes, and how to factor it into your event budget.",
        "tag": "Planning", "read_time": 4,
        "content": """<div class="blog-body">
<p>If you've been booking performers and entertainers, you've probably encountered the term "rider." Here's what it means for MC bookings and how to think about it.</p>
<h2>What Is a Rider?</h2>
<p>A rider is a list of requirements attached to a performance or service contract — things the client must provide in addition to the fee. For musicians, riders can be elaborate (specific drinks, backstage requirements, technical specifications). For MCs, riders are generally simpler and practically motivated.</p>
<h2>What an MC Rider Typically Includes</h2>
<ul>
<li><strong>Technical requirements:</strong> Microphone type preference (handheld vs lapel), monitor speaker, specific PA setup</li>
<li><strong>Space requirements:</strong> A clear sight line to the AV operator; access to the stage or hosting position</li>
<li><strong>On-night requirements:</strong> Water at the hosting position throughout the event</li>
<li><strong>Preparation requirements:</strong> Briefing call minimum X weeks before the event; run sheet provided by a specific date</li>
<li><strong>Travel and accommodation:</strong> For events outside Perth metro, travel costs and overnight accommodation if required</li>
</ul>
<h2>Is a Rider a Red Flag?</h2>
<p>Not at all — a rider with reasonable, professional requirements signals an MC who has done this enough to know what they need to perform at their best. The requirements above are practical, not excessive.</p>
<h2>What to Watch For</h2>
<p>An MC whose rider is unreasonably complex or who treats preparation requirements as optional while demanding their technical requirements be met exactly has misaligned priorities. The preparation requirements matter more than the microphone preference.</p>
""" + CTA_BOX + "</div>",
    },
    {
        "slug": "blog-how-to-introduce-wedding-party",
        "title": "How to Introduce the Wedding Party — MC's Guide | The Perth MC",
        "h1": "How to Introduce the Wedding Party — MC's Guide",
        "meta": "Bridal party introductions are among the highest-energy moments of any wedding reception. A step-by-step guide to getting them exactly right.",
        "tag": "Weddings", "read_time": 5,
        "content": """<div class="blog-body">
<p>The bridal party entry is the first big set piece of the reception — and getting it right sets the tone for the entire evening. Here's how to execute it with maximum impact.</p>
<h2>Preparation: Get the Details Right</h2>
<p>For every member of the bridal party, you need: correct name pronunciation, their relationship to the couple, and one specific, warm, personalised detail. The detail is what separates a memorable introduction from an announcement. "James, the best man" is an announcement. "James, who has been the groom's closest friend since they met at a football tryout in Year 9 and somehow managed to convince him that camping was an acceptable way to spend a weekend" — that's an introduction.</p>
<h2>The Order</h2>
<p>Standard introduction order: flower girls and page boys first (crowd reaction is immediate and it sets a warm tone), then bridesmaids paired with groomsmen, then the maid of honour and best man (the crowd's energy should be building), then the parents of the couple, then the newlyweds. Adjust based on the couple's preferences.</p>
<h2>Coordinate with the DJ</h2>
<p>Every entry needs music. Coordinate with the DJ on:</p>
<ul><li>Which song plays for which group</li><li>Your cue to the DJ to start each track</li><li>When to cross-fade or cut as the next group enters</li></ul>
<h2>The Newlyweds' Entry</h2>
<p>The couple's entry is the climax. Build the audience's anticipation across every preceding introduction so that when the couple walks through the door, the room is already at maximum energy. The newlyweds' introduction should be the most personal, the most specific, and the most emotionally resonant of the entire sequence.</p>
""" + CTA_BOX + "</div>",
    },
    {
        "slug": "blog-mc-50th-birthday-tips",
        "title": "MC for a 50th Birthday — Tips for the Perfect Milestone Party | The Perth MC",
        "h1": "MC for a 50th Birthday — Tips for the Perfect Milestone Party",
        "meta": "50th birthdays are once-in-a-lifetime — and they deserve more than a DJ and a willing friend. How a professional MC makes a milestone birthday genuinely memorable.",
        "tag": "Events", "read_time": 5,
        "content": """<div class="blog-body">
<p>A 50th birthday party sits in a distinct category of events — significant enough to warrant professional hosting, personal enough to require a level of customisation that generic event hosting can't provide. Here's what makes a 50th birthday MC service worth having.</p>
<h2>The Tribute</h2>
<p>The centrepiece of any great 50th is a tribute to the guest of honour — a narrative thread woven through the evening that celebrates who they are, what they've achieved, and what they mean to the people in the room. A professional MC researches this: speaking with family beforehand, gathering stories, and weaving the material into introductions, transitions, and the closing toast.</p>
<h2>Managing Diverse Speeches</h2>
<p>50th birthday speeches come from family members, old friends, and colleagues who likely don't know each other. Managing the tone across those different relationships requires a skilled MC — warm when the family stories are personal, energetic when the workplace roast begins, measured when emotional moments need space.</p>
<h2>The Room Dynamics</h2>
<p>A typical 50th has the guest of honour's parents' generation, their own generation, and their children's generation all in the same room. The MC needs to pitch content that works across that demographic range — nothing too niche, nothing too broad, everything warm and inclusive.</p>
<h2>The End of the Formal Program</h2>
<p>The formal portion of a 50th — speeches, tribute, cake cutting — should end at the peak of the evening's emotion, transitioning naturally into a dance floor or social close that the guest of honour actually gets to enjoy. An MC who runs the formal portion too long keeps the guest of honour on duty all night. The goal is to celebrate them, then let them be present in the celebration.</p>
""" + CTA_BOX + "</div>",
    },
    {
        "slug": "blog-how-to-choose-mc-charity-gala",
        "title": "How to Choose the Right MC for Your Charity Gala | The Perth MC",
        "h1": "How to Choose the Right MC for Your Charity Gala",
        "meta": "Not every MC is right for a charity gala. What to look for in a gala MC — and the specific skills that make the difference to how much your event raises.",
        "tag": "Events", "read_time": 5,
        "content": """<div class="blog-body">
<p>Charity gala MCs have a fundamentally different brief from wedding or corporate MCs. They need to entertain while also fundraising — holding the room emotionally while creating the conditions for generosity. Not every MC can do both. Here's how to find one who can.</p>
<h2>Ask About Auction Experience Specifically</h2>
<p>Facilitating a live auction is a specific skill. Ask any prospective gala MC: how many live auctions have you facilitated? What techniques do you use to build competition between bidders? How do you handle a lot that isn't moving? These questions reveal experience that general MC credentials don't.</p>
<h2>Emotional Range</h2>
<p>A charity gala requires an MC who can move between registers — warm and entertaining for most of the evening, then genuinely moving and purposeful when the cause is front and centre, then commercial and energetic during the auction. An MC who is only comfortable in one register will struggle.</p>
<h2>Cause Preparation</h2>
<p>Your gala MC should be briefed on your cause in genuine depth — the impact stories, the specific need you're addressing, the outcomes you're trying to fund. An MC who can speak authentically about your cause from the stage is significantly more effective than one who's reading from a card they were handed at the venue.</p>
<h2>References from Similar Events</h2>
<p>Ask for references specifically from charity galas and fundraising events — not just general event hosting. The skills required are different, and an MC's track record with fundraising events is a meaningful predictor of their effectiveness at yours.</p>
""" + CTA_BOX + "</div>",
    },
    {
        "slug": "blog-perth-conference-venues-guide",
        "title": "Perth Conference Venues — A Guide from the Stage | The Perth MC",
        "h1": "Perth Conference Venues — A Guide from the Stage",
        "meta": "A review of Perth's major conference venues — written by a professional MC who's hosted events at most of them.",
        "tag": "Corporate", "read_time": 7,
        "content": """<div class="blog-body">
<p>Perth has a strong conference venue offering — from CBD hotels with full production capability to purpose-built conference centres and intimate creative spaces. Here's an honest review from the MC's perspective.</p>
<h2>Perth Convention and Exhibition Centre (PCEC)</h2>
<p>The PCEC is Perth's flagship conference venue — with multiple plenary spaces, excellent AV infrastructure, and a professional event services team. Best suited for large-scale events (300+ delegates). The Riverside Theatre is acoustically excellent; the larger ballrooms require careful AV planning for audience engagement at the rear.</p>
<h2>Crown Perth</h2>
<p>Crown's conference and event spaces range from boardroom scale to ballroom capacity. The Grand Ballroom can hold 1,500+ for gala events. AV infrastructure is strong. Location and accommodation on-site make Crown practical for interstate delegates and multi-day events.</p>
<h2>CBD Hotels</h2>
<p>The Pan Pacific, QT, COMO The Treasury, and Westin all offer quality conference and event spaces in the CBD. These work well for mid-size corporate events (50–300 delegates) where CBD location is a priority. Each has a distinct personality — QT brings creative energy; The Treasury brings heritage atmosphere.</p>
<h2>AQWA and Alternative Venues</h2>
<p>For events that want to be memorable rather than conventional, Perth has excellent alternative options — AQWA for events in front of the shark tank, the WA Museum Boola Bardip for heritage atmosphere, and the State Theatre Centre for production-heavy events.</p>
<h2>What to Ask Any Conference Venue</h2>
<ul><li>AV capabilities (in-house vs contracted external, LED screens, sound system specs)</li><li>Natural light management (blackout capabilities for daytime AV)</li><li>Breakout room availability and configuration flexibility</li><li>Catering flexibility and dietary accommodation capability</li><li>Dedicated event coordinator assigned to your event</li></ul>
""" + CTA_BOX + "</div>",
    },
    {
        "slug": "blog-team-building-event-ideas-perth",
        "title": "Team Building Event Ideas Perth 2025 | The Perth MC",
        "h1": "Team Building Event Ideas Perth 2025",
        "meta": "The best team building event ideas in Perth for 2025 — from activity-based days to hosted dinners. Options for every budget and group size.",
        "tag": "Corporate", "read_time": 6,
        "content": """<div class="blog-body">
<p>Perth's team building market has evolved significantly — the days of trust falls and rope courses are largely behind us. Here are the options that actually work for Perth teams in 2025, with notes on what makes each one effective.</p>
<h2>Hosted Trivia and Quiz Events</h2>
<p>A well-run quiz with a professional MC is consistently one of the highest-rated team building formats — competitive, social, inclusive across age and role, and flexible in scale from 20 to 200 people. The key is a host who can build genuine competitive energy without making it feel forced. Best for end-of-year events and social occasions.</p>
<h2>Cooking Challenges</h2>
<p>Facilitated cooking challenges (at venues like The Cooking Professor or catered via private chefs) work well for teams that want activity and interaction without competitive pressure. The shared experience of producing food together — and eating it — creates genuine connection. Works best for teams of 20–50.</p>
<h2>Swan Valley Day Events</h2>
<p>A hosted day in the Swan Valley — combining wine tasting, a group lunch, and a structured activity (wine blending, cheese making, chocolate workshop) — is perennially popular with Perth teams. The relaxed setting shifts social dynamics productively. Best for senior teams or reward-based events.</p>
<h2>Escape Rooms and Puzzle Events</h2>
<p>Escape room experiences work well for problem-solving teams and can scale via concurrent rooms or competitive formats. The post-activity debrief (facilitated by your MC or event host) is where the team building actually happens — the activity creates the material.</p>
<h2>Volunteer and Give-Back Activities</h2>
<p>Teams increasingly value activities with genuine social purpose — Foodbank packing shifts, habitat restoration, charity bike rides. These require less MC facilitation but benefit from a strong emcee for the pre and post elements (briefing the group, celebrating their contribution).</p>
""" + CTA_BOX + "</div>",
    },
    {
        "slug": "blog-how-to-manage-event-running-late",
        "title": "How to Manage an Event That's Running Late | The Perth MC",
        "h1": "How to Manage an Event That's Running Late",
        "meta": "Events fall behind schedule. What separates experienced MCs from beginners is how they manage the recovery — without panicking guests or blowing the program.",
        "tag": "Craft", "read_time": 5,
        "content": """<div class="blog-body">
<p>Events run late. It's inevitable. The question isn't whether it'll happen but how you respond when it does. Here's the approach that works.</p>
<h2>Diagnose How Late and Why</h2>
<p>Not all delays are created equal. Five minutes behind on speeches is recoverable in the next transition. Thirty minutes behind at the start of the main course requires real program surgery. Understand the scale of the deviation before deciding how to respond.</p>
<h2>Don't Announce the Delay to the Room</h2>
<p>Announcing that you're running late tells guests something is wrong. Most delays can be managed invisibly — by compressing elements that can flex, moving to the next element early if the previous one finished ahead of schedule, and communicating timing changes to vendors quietly rather than publicly.</p>
<h2>Identify What Can Flex</h2>
<p>Work with the event organiser to identify which program elements are non-negotiable and which can be shortened or cut. Entertainment segments, extended transitions, and optional program elements are candidates. Core moments — the speeches, the major awards, the couple's first dance — are not.</p>
<h2>Communicate Changes to Vendors Immediately</h2>
<p>When the program shifts, the kitchen, DJ, photographer, and venue coordinator all need to know. The MC is the communication hub on the night. Pick up the phone, send a message, or physically find each vendor — but ensure everyone is working from the same updated timeline.</p>
<h2>Compress Strategically</h2>
<p>Compressing a program means tightening transitions, reducing the MC's connective tissue between elements, and asking speakers to keep to time more strictly. It does not mean rushing significant moments. The compression should be invisible to guests — they should feel relaxed even as the MC is quietly managing a tighter clock.</p>
""" + CTA_BOX + "</div>",
    },
    {
        "slug": "blog-mic-techniques-event-mc",
        "title": "Microphone Techniques Every Event MC Should Know | The Perth MC",
        "h1": "Microphone Techniques Every Event MC Should Know",
        "meta": "The technical side of event hosting — microphone types, handling techniques, and the practical skills that separate confident MCs from those who fight the PA.",
        "tag": "Craft", "read_time": 5,
        "content": """<div class="blog-body">
<p>The microphone is an MC's primary tool — and poor microphone technique is one of the most visible signs of an inexperienced host. Here are the practical skills that matter.</p>
<h2>Microphone Types and When to Use Them</h2>
<ul>
<li><strong>Handheld dynamic:</strong> The most common event microphone. Versatile, durable, and works well for most situations. Requires consistent distance maintenance — too close and it distorts; too far and it loses level.</li>
<li><strong>Lapel/lavalier:</strong> Hands-free, ideal for when you're moving around a stage. Prone to clothing noise and wind interference outdoors. Requires a transmitter pack clipped to clothing.</li>
<li><strong>Headset:</strong> Common for high-movement presentations or when a consistent sound level is critical. Locks mic position relative to the mouth.</li>
</ul>
<h2>The 5cm Rule</h2>
<p>For handheld mics, maintain approximately 5cm between the capsule and your mouth. The most common mistake: dropping the mic as you speak, which causes dramatic volume drops at the end of sentences. Keep the mic at the same height throughout your speaking.</p>
<h2>Working with the AV Operator</h2>
<p>Arrive early enough to do a proper sound check — not just "testing, testing" but actual spoken content at the level and pace you'll use during the event. Build a working relationship with the AV operator: they're your technical partner on the night, and they need to know your style to support you properly.</p>
<h2>Handling Feedback</h2>
<p>Audio feedback (the high-pitched squeal) happens when a microphone picks up its own amplified signal. The immediate response: lower the mic or point it away from the nearest speaker. Do this calmly and without theatrical reaction — guests take their cue from how you respond.</p>
""" + CTA_BOX + "</div>",
    },
    {
        "slug": "blog-how-to-plan-black-tie-event-perth",
        "title": "How to Plan a Black Tie Event in Perth | The Perth MC",
        "h1": "How to Plan a Black Tie Event in Perth",
        "meta": "A complete guide to planning a black tie event in Perth — venue, dress code, program structure, catering standards, and MC briefing.",
        "tag": "Events", "read_time": 6,
        "content": """<div class="blog-body">
<p>A black tie event signals a standard of occasion that every detail needs to honour — from the invitation to the final farewell. Here's how to plan one that justifies the dress code.</p>
<h2>Venue: The Foundation of Formality</h2>
<p>Black tie events require venues that match the register. Heritage buildings (the WA Museum, Government House Ballroom, historic hotel ballrooms), luxury hotel spaces (Crown Grand Ballroom, Pan Pacific), and purpose-built formal event centres are all appropriate. Industrial or casual-aesthetic venues — regardless of how well-designed — undermine the black tie register from the moment guests arrive.</p>
<h2>The Invitation Sets the Expectation</h2>
<p>A black tie event invitation should be physical — not digital. The quality of the paper, the formality of the language, and the precision of the dress code instruction all signal the event's register to guests before they arrive. "Black tie" should be specified clearly; "black tie optional" creates confusion and results in a mixed-dress crowd that dilutes the atmosphere.</p>
<h2>Catering Standards</h2>
<p>Black tie catering means courses, not buffet. A formal plated dinner with professional service staff is non-negotiable. The quality of the food and the professionalism of the service team are visible signals of the event's seriousness. Cocktail canapés at arrival should be substantial and high-quality.</p>
<h2>Entertainment</h2>
<p>Live entertainment is expected at black tie events — at minimum, a string quartet or jazz ensemble during pre-dinner drinks. Post-dinner entertainment (a band, a featured performer) elevates the occasion further. DJ-only receptions can work at black tie if the music selection and production quality are calibrated appropriately.</p>
<h2>The MC Brief</h2>
<p>Brief your MC specifically on the formal protocols for your event — acknowledgement of VIPs, table of honour management, form of address for titled guests, and the precise register you want maintained throughout. Provide this in writing, not just verbally. A black tie event MC who hasn't been briefed on the formalities is a visible liability.</p>
""" + CTA_BOX + "</div>",
    },
    {
        "slug": "blog-school-formal-mc-checklist",
        "title": "School Formal MC Checklist for Organisers | The Perth MC",
        "h1": "School Formal MC Checklist for Organisers",
        "meta": "Everything your school formal MC needs — and everything to confirm before the night. A practical checklist for teachers and event coordinators.",
        "tag": "Events", "read_time": 4,
        "content": """<div class="blog-body">
<p>School formals require more MC preparation than most organisers realise. Here's the complete checklist for a smooth night.</p>
<h2>2 Weeks Before</h2>
<ul><li>Send MC the complete run sheet with all times</li><li>Provide list of all formal entries and names (confirm pronunciation for every student)</li><li>Confirm King and Queen nominees and reveal process</li><li>List of teachers to be acknowledged and their correct titles</li><li>Any students giving speeches or presentations — names and topics</li><li>Confirm MC dress code (usually formal/black tie)</li></ul>
<h2>1 Week Before</h2>
<ul><li>Final run sheet confirmation</li><li>Venue address, parking, and MC arrival time</li><li>Venue coordinator contact on the night</li><li>DJ/band contact and liaison plan</li><li>Confirmation of any awards or special presentations not on original run sheet</li></ul>
<h2>Night Of</h2>
<ul><li>MC arrives 60 minutes before student arrival</li><li>Sound check with venue AV team</li><li>Brief run-through with venue coordinator</li><li>Confirm current student/entry list is finalised</li><li>Confirm King and Queen reveal process with organiser</li></ul>
<h2>Content Guidance for the MC</h2>
<ul><li>Keep all content age-appropriate and school-appropriate</li><li>Avoid references that could embarrass specific students</li><li>Match energy to the room — students who want to dance should not be held hostage to an extended formal program</li><li>Acknowledge teachers warmly but briefly — the night belongs to the students</li></ul>
""" + CTA_BOX + "</div>",
    },
    {
        "slug": "blog-wedding-mc-opening-speech",
        "title": "Wedding MC Opening Speech — Examples and Tips | The Perth MC",
        "h1": "Wedding MC Opening Speech — Examples and Tips",
        "meta": "The opening welcome sets the tone for the entire reception. What a great opening speech includes, what to avoid, and examples of language that works.",
        "tag": "Weddings", "read_time": 6,
        "content": """<div class="blog-body">
<p>The opening welcome is the first words guests hear from the MC — and first impressions at weddings, as at everything else, matter enormously. Here's what goes into an opening that sets the evening up right.</p>
<h2>What the Opening Must Do</h2>
<ul><li>Welcome guests warmly and specifically (not generically)</li><li>Acknowledge the significance of the occasion</li><li>Handle any essential housekeeping (exits, dietary service, phone etiquette)</li><li>Set the tone for the evening — the emotional register the night will operate in</li><li>Transition smoothly to the first element (usually the bridal party entrance)</li></ul>
<h2>Length: 90 Seconds Maximum</h2>
<p>The room is waiting for the couple. Every second of MC opening time before the bridal party enters is a second the audience is waiting. Be warm, be specific, be brief, and get to the entrance.</p>
<h2>What to Avoid</h2>
<ul><li>Generic language ("What a wonderful occasion this is") — it could apply to any event anywhere</li><li>Jokes in the opening — save humour for when you've earned the room's trust</li><li>Lengthy housekeeping that eats into entrance energy</li><li>Thanking the couple for having you — this is your job; don't make it about you</li></ul>
<h2>Example Language That Works</h2>
<p>"Good evening everyone — and welcome to one of the best evenings you're going to have this year. Tonight we celebrate [Name] and [Name] — two people who somehow managed to find each other in this city, fall completely in love, and talk 140 of their favourite people into wearing their nicest clothes on a Saturday night. I'd say you made the right call. The bar is open, the food is extraordinary, and if tonight goes as well as I know it will — the dance floor is going to be extraordinary too. But first — the moment you've been waiting for. Ladies and gentlemen, please put your hands together..."</p>
<p>Note what this does: it acknowledges the guests, names the couple, creates warmth and light humour, sets positive expectations, and transitions directly into the entrance — all in under 90 seconds.</p>
""" + CTA_BOX + "</div>",
    },
    {
        "slug": "blog-how-to-write-toast-as-mc",
        "title": "How to Write a Toast as an MC | The Perth MC",
        "h1": "How to Write a Toast as an MC",
        "meta": "An MC toast is different from a speech — brief, warm, and designed to bring the room together in a single shared moment. How to write one that lands.",
        "tag": "Craft", "read_time": 5,
        "content": """<div class="blog-body">
<p>An MC toast is not a speech. It's a specific, short form — typically 60–90 seconds — designed to bring a room together in a single shared moment of acknowledgement. Written badly, it's awkward. Written well, it's the moment people remember.</p>
<h2>The Structure of a Great Toast</h2>
<ul>
<li><strong>Context (1 sentence):</strong> Why are we toasting right now? What moment are we marking?</li>
<li><strong>Acknowledgement (2–3 sentences):</strong> Who or what is being toasted? What specifically do we appreciate or celebrate about them?</li>
<li><strong>The ask (1 sentence):</strong> The call to raise glasses — clear, specific, warm.</li>
<li><strong>The toast itself (1 sentence):</strong> The actual toast line. Memorable, appropriate, brief.</li>
</ul>
<h2>What Makes a Toast Line Work</h2>
<p>The best toast lines are specific enough to feel personal and universal enough to resonate with every guest. "To James and Emma — may the adventure you started today last a lifetime" works because it's warm, true, and anyone in the room can sincerely mean it.</p>
<p>Toast lines that don't work: inside references that 30% of the room doesn't get; humour that undermines the sincerity of the moment; quotes that feel borrowed rather than genuine.</p>
<h2>Timing the Toast</h2>
<p>Before a toast, the MC needs to ensure all glasses are full. A 30-second heads-up ("In just a moment I'm going to ask you all to raise your glasses, so now would be a great time to make sure you have a drink in hand") is practical and signals what's coming.</p>
<h2>The Delivery</h2>
<p>Slow down for the toast. The buildup can move at normal pace, but as you approach the toast line itself, drop your rate slightly. Look across the room rather than at your notes. Make eye contact with the person or people being toasted. The toast line should feel like it's being said to the room, not read to it.</p>
""" + CTA_BOX + "</div>",
    },
    {
        "slug": "blog-perth-event-hire-checklist",
        "title": "Perth Event Hire Checklist 2025 | The Perth MC",
        "h1": "Perth Event Hire Checklist 2025",
        "meta": "Everything you need to hire for a Perth event — venue, AV, catering, entertainment, and MC — with timeline guidance and questions to ask each vendor.",
        "tag": "Planning", "read_time": 5,
        "content": """<div class="blog-body">
<p>Planning a Perth event from scratch involves coordinating multiple vendors across a tight timeline. Here's the complete checklist — with suggested booking windows for each category.</p>
<h2>Book 12+ Months Out (Peak Season)</h2>
<ul><li><strong>Venue:</strong> Popular Perth venues book 12–18 months ahead for Saturday events in peak season (Oct–Mar)</li><li><strong>MC:</strong> Sought-after MCs fill their calendar 12 months out for peak dates — book early</li><li><strong>Photographer / Videographer:</strong> Often the first vendors to book out</li><li><strong>Band:</strong> Quality function bands have limited Saturdays — book 12 months out</li></ul>
<h2>Book 6–8 Months Out</h2>
<ul><li><strong>Caterer / catering package:</strong> If not managed by the venue</li><li><strong>DJ:</strong> Quality DJs book quickly for peak dates</li><li><strong>Florist / décor:</strong> Particularly for large floral installations</li><li><strong>Audio-visual company:</strong> For events requiring production beyond basic venue AV</li></ul>
<h2>Book 3–4 Months Out</h2>
<ul><li>Celebrant (for weddings)</li><li>Photo booth hire</li><li>Entertainment (comedian, string quartet, etc.)</li><li>Graphic design (invitations, signage, menus)</li></ul>
<h2>Book 4–8 Weeks Out</h2>
<ul><li>Stationery printing</li><li>Transport (cars, buses for guests)</li><li>Event staff (MCs, hosts, greeters)</li><li>Cake / dessert</li></ul>
<h2>Questions for Every Vendor</h2>
<ul><li>What's included in your package vs priced separately?</li><li>What's your cancellation and rescheduling policy?</li><li>When do you need final numbers and program details?</li><li>Do you have backup plans if you're unavailable on the day?</li><li>Can you provide references from similar events?</li></ul>
""" + CTA_BOX + "</div>",
    },
    {
        "slug": "blog-fundraiser-mc-perth-tips",
        "title": "How to Choose an MC for Your Perth Fundraiser | The Perth MC",
        "h1": "How to Choose an MC for Your Perth Fundraiser",
        "meta": "Fundraising events have specific MC requirements. What to look for when choosing an MC for your Perth fundraiser — and the questions that reveal their auction experience.",
        "tag": "Events", "read_time": 5,
        "content": """<div class="blog-body">
<p>Choosing the wrong MC for a fundraiser doesn't just make for a less entertaining evening — it can directly reduce what you raise. Here's how to find the right one.</p>
<h2>Fundraising Experience Is Not Interchangeable with General MC Experience</h2>
<p>A wedding MC who's hosted 200 receptions is not automatically qualified to run your charity auction. Fundraising events require specific skills — cause storytelling, emotional framing of asks, live auction facilitation, and the ability to convert room energy into generosity. Ask specifically about fundraising experience.</p>
<h2>The Auction Question</h2>
<p>Ask every prospective fundraiser MC: "How many live auctions have you facilitated, and what results have events achieved?" An experienced auction MC will have a clear answer and specific examples. Someone who hasn't done it will tell you it's no different from regular hosting — it is very different.</p>
<h2>Cause Alignment</h2>
<p>Brief your MC on your cause in depth — the stories, the impact data, the emotional truth of what you're raising money for. An MC who is genuinely moved by your cause will communicate that authentically. An MC who is going through the motions will raise less.</p>
<h2>The Paddle Raise</h2>
<p>Ask any prospective MC whether they've facilitated a paddle raise or fund-a-need. This single fundraising technique, executed well by a skilled MC, can raise significant funds in 10–15 minutes. Not every MC knows how to do it. The ones who do are significantly more valuable at fundraising events.</p>
<h2>Match Energy to Cause</h2>
<p>A children's hospital fundraiser has a different emotional register than a conservation charity gala. Make sure your MC's natural style and energy can calibrate to the specific emotional landscape of your cause — not just any cause in general.</p>
""" + CTA_BOX + "</div>",
    },
    {
        "slug": "blog-conference-mc-day-two-energy",
        "title": "Keeping Conference Energy Up on Day Two | The Perth MC",
        "h1": "Keeping Conference Energy Up on Day Two",
        "meta": "Day two of a multi-day conference is the MC's greatest challenge. Practical techniques for maintaining audience energy when attention is at its lowest.",
        "tag": "Corporate", "read_time": 5,
        "content": """<div class="blog-body">
<p>Day two of a multi-day conference is objectively harder than day one. Delegates have attended a full day of content, likely stayed up later than they should have at the networking dinner, and are returning to their seats with depleted cognitive reserves. An experienced MC knows this — and plans for it.</p>
<h2>Acknowledge the Reality (Briefly)</h2>
<p>Opening day two with a wink at the situation — "I can see you've all taken full advantage of last night's networking dinner" — acknowledges what everyone is feeling without dwelling on it. It creates connection through shared experience and signals that the MC is present with the audience, not performing above them.</p>
<h2>Higher Energy, Shorter Segments</h2>
<p>Day two programming should have more frequent breaks, shorter sessions, and more physical movement built in than day one. The MC can advocate for this in the planning stage — and on the day itself, can compress transitions and build in brief movement moments ("take 30 seconds, stretch, say hello to the person next to you") that are subtle but effective.</p>
<h2>Connect Content to What Happened Yesterday</h2>
<p>The MC who references specific moments from day one — a key insight from a morning session, a great question from the audience, an unexpected laugh from the networking dinner — demonstrates genuine engagement and creates continuity. Delegates feel the conference is building toward something, not just repeating.</p>
<h2>Vary the Format</h2>
<p>Day two sessions that mirror day one's format exactly compound the energy problem. Work with organisers to ensure at least one element of day two is structurally different — a panel instead of presentations, a workshop instead of keynotes, a Q&amp;A session that's genuinely audience-driven. Variety signals progression.</p>
""" + CTA_BOX + "</div>",
    },
    {
        "slug": "blog-wedding-mc-swan-valley",
        "title": "Wedding MC in the Swan Valley — What to Know | The Perth MC",
        "h1": "Wedding MC in the Swan Valley — What to Know",
        "meta": "The Swan Valley is Perth's premier wine country wedding destination. What makes Swan Valley weddings unique — and how to get the most out of a winery reception.",
        "tag": "Venues", "read_time": 6,
        "content": """<div class="blog-body">
<p>The Swan Valley is one of Western Australia's most beautiful wedding regions — rolling vineyards, estate properties, and a relaxed wine country atmosphere that creates a distinctly Perth kind of celebration. Having MC'd dozens of Swan Valley weddings, here's what makes them unique.</p>
<h2>The Venues</h2>
<p>Mandoon Estate, Sandalford Wines, Houghton Winery, and Olive Farm Wines are among the region's most established wedding venues — each with significant event experience, strong on-site catering, and the physical beauty that makes winery weddings so appealing. Smaller boutique properties and private vineyard estates are also available for more intimate celebrations.</p>
<h2>The Outdoor Opportunity</h2>
<p>Swan Valley weddings almost always make use of outdoor spaces — ceremony in the vines, cocktail hour on a terrace, reception in a beautifully converted barrel hall or marquee. The transition from outdoor ceremony to indoor reception is one of the most common logistical challenges I manage at Swan Valley events. Having a clear plan for guest movement — and building buffer time into the run sheet — is essential.</p>
<h2>The Atmosphere</h2>
<p>Swan Valley weddings tend to have a relaxed, celebratory energy. Guests arrive in a good mood — they've driven out of the city, they're in a beautiful setting, they've had a glass of wine on arrival. This is a gift for an MC: a room that's already warm and receptive. The art is sustaining and building that energy across the evening rather than letting it plateau.</p>
<h2>Practical Considerations</h2>
<ul><li>Travel logistics matter — many guests will need transport arrangements. Brief the MC on whether to make transport announcements during the evening.</li><li>Perth summer heat in the Swan Valley is real — outdoor elements need shading, hydration for guests, and timing that avoids peak afternoon heat.</li><li>AV in outdoor settings at vineyards can be variable — always confirm what's available and test it properly on the day.</li></ul>
""" + CTA_BOX + "</div>",
    },
    {
        "slug": "blog-product-launch-mc-guide",
        "title": "How to Choose an MC for a Product Launch | The Perth MC",
        "h1": "How to Choose an MC for a Product Launch",
        "meta": "Product launches require an MC who understands brand alignment. What to look for, what questions to ask, and what separates a great product launch MC from a generic event host.",
        "tag": "Corporate", "read_time": 5,
        "content": """<div class="blog-body">
<p>A product launch is a brand moment — and the MC is the voice of your brand on the night. Not every MC can do this well. Here's how to find one who can.</p>
<h2>Brand Alignment Is Not Optional</h2>
<p>At a product launch, your MC needs to understand your brand positioning, your communication style, and the tone you want associated with the product being launched. An MC who treats a product launch like a generic event hosting gig will deliver generic event hosting — and your brand will feel exactly that generic to every person in the room.</p>
<h2>Questions to Ask</h2>
<ul><li>Have you MC'd a product launch before — what industry, what scale, and what was the outcome?</li><li>How do you approach brand research before an event?</li><li>How would you describe our brand's tone, based on what you know so far?</li><li>How do you handle media or influencer guests differently from a standard corporate audience?</li></ul>
<h2>The Brief They Need</h2>
<p>Your product launch MC needs more than a run sheet. They need: your brand guidelines and tone of voice, the key messages you want associated with the product, the target audience for the product (so they can speak to the room appropriately), any embargo or media management considerations, and the specific moments you want to ensure land with maximum impact (the reveal, the first demo, the guest speaker).</p>
<h2>Enthusiasm vs Authenticity</h2>
<p>The risk with product launch MCs is forced enthusiasm — hosts who are visibly performing excitement rather than genuinely communicating it. Audiences, especially media and industry professionals, detect this immediately. Brief your MC thoroughly enough that their enthusiasm is informed by genuine understanding of what's being launched.</p>
""" + CTA_BOX + "</div>",
    },
]


def build_draft(draft):
    header = HEADER.format(
        meta=draft["meta"],
        title=draft["title"],
        h1=draft["h1"],
        tag=draft["tag"],
        read_time=draft["read_time"],
    )
    return header + draft["content"] + FOOTER


def main():
    os.makedirs(DRAFTS_DIR, exist_ok=True)
    for draft in DRAFTS:
        html = build_draft(draft)
        out_path = os.path.join(DRAFTS_DIR, f"{draft['slug']}.html")
        with open(out_path, "w") as f:
            f.write(html)
        print(f"Generated draft: {draft['slug']}.html")
    print(f"\nDone — {len(DRAFTS)} draft posts generated.")


if __name__ == "__main__":
    main()
