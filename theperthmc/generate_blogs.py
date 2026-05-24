#!/usr/bin/env python3
"""Generate all published blog posts for The Perth MC.
Run from the theperthmc/ directory: python3 generate_blogs.py
Generates 26 blog HTML files directly into theperthmc/.
"""

import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

HEADER = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="{meta}" />
  <meta name="robots" content="index, follow" />
  <title>{title}</title>
  <link rel="canonical" href="https://theperthmc.com.au/{slug}.html" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="css/style.css" />
</head>
<body>

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

<section class="blog-hero">
  <div class="container">
    <a href="blog.html" class="blog-back">&larr; Back to Blog</a>
    <h1>{h1}</h1>
    <div class="blog-meta">{date_str} &nbsp;&middot;&nbsp; {read_time} min read &nbsp;&middot;&nbsp; {tag}</div>
  </div>
</section>
"""

FOOTER = """
<section class="cta-band">
  <div class="container">
    <h2>Planning an Event in Perth?</h2>
    <p>Check availability for your date — we respond within 24 hours.</p>
    <a href="contact.html" class="btn btn-primary btn-lg">Check Availability</a>
  </div>
</section>

<footer class="site-footer">
  <div class="container">
    <div class="footer-top">
      <div class="footer-brand">
        <a href="index.html" class="logo">The Perth<span>MC</span></a>
        <p>Perth's professional MC for weddings, corporate events, galas, conferences, and milestone celebrations.</p>
        <p>&#x2709;&#xFE0F; <a href="mailto:info@theperthmc.com.au">info@theperthmc.com.au</a></p>
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
      <p>&copy; <span id="year"></span> The Perth MC. All rights reserved. | Perth, Western Australia</p>
    </div>
  </div>
</footer>

<script src="js/main.js"></script>

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "{h1}",
  "description": "{meta}",
  "datePublished": "{date_iso}",
  "dateModified": "{date_iso}",
  "author": {{"@type": "Organization", "name": "The Perth MC"}},
  "publisher": {{"@type": "Organization", "name": "The Perth MC", "url": "https://theperthmc.com.au"}}
}}
</script>
</body>
</html>
"""

CTA_BOX = """<div class="blog-cta-box">
  <h3>Need a Professional MC for Your Event?</h3>
  <p>Perth-based, experienced across all event types, and available to discuss your date.</p>
  <a href="contact.html" class="btn btn-primary">Check Availability</a>
</div>"""

ARTICLES = [
    {
        "slug": "blog-how-to-choose-wedding-mc-perth",
        "title": "How to Choose a Wedding MC in Perth | The Perth MC",
        "h1": "How to Choose a Wedding MC in Perth",
        "meta": "The right MC can make or break your reception. A practical guide to choosing a Perth wedding MC — what to look for, questions to ask, and red flags to avoid.",
        "tag": "Weddings",
        "read_time": 6,
        "content": """<div class="blog-body">
<p>Choosing a wedding MC is one of the most important vendor decisions you'll make — and one of the most underestimated. Couples spend months selecting a venue, photographer, and florist, then spend fifteen minutes finding someone to host the most important evening of their lives.</p>
<p>Here's how to do it properly.</p>

<h2>What a Wedding MC Actually Does</h2>
<p>Before you start searching, it helps to be clear on the role. A wedding MC is the host of your reception — they open the evening, introduce the bridal party, manage the speeches, cue the first dance, and keep the program moving from start to finish. They also liaise with your DJ, band, venue coordinator, and photographer so all the moving parts connect.</p>
<p>They are not an entertainer performing their own set. They are not a friend who "knows how to talk in front of people." They are the invisible architecture of your evening — and when the role is done well, your guests don't notice the hosting at all. They just feel like the night flowed perfectly.</p>

<h2>Start with Experience</h2>
<p>Ask how many weddings they've hosted. There's no magic number, but an MC with 10 weddings under their belt is very different from one with 100. Experience matters because it builds situational awareness — the ability to read a room, adapt when speeches overrun, handle AV problems calmly, and know when to step back and let a moment breathe.</p>
<p>Ask specifically about Perth weddings. Local experience means they'll know the venues, understand the timing challenges of outdoor Perth summers, and have relationships with local vendors.</p>

<h2>Specificity Over Personality</h2>
<p>When you meet a prospective MC, listen for how specific they are about your wedding versus how much they're selling a generic version of themselves. A great MC asks about your relationship, your families, your venue, your run sheet, and any moments that need to be handled with care. An average MC tells you how great they are.</p>
<p>The question to ask: "Can you walk me through how you'd approach our particular reception?" Their answer will tell you everything.</p>

<h2>Ask About Their Process</h2>
<p>A professional MC has a clear pre-wedding process. Look for:</p>
<ul>
<li>A detailed briefing call (not just an email exchange)</li>
<li>Run sheet review and input</li>
<li>A custom script — not a template they reuse</li>
<li>Vendor coordination (DJ, band, photographer)</li>
<li>Contingency planning for common issues</li>
</ul>
<p>If an MC can't describe a clear preparation process, that's a red flag. Preparation is where the work happens. The night is just the execution.</p>

<h2>Red Flags to Watch For</h2>
<ul>
<li>They can't tell you about specific weddings they've hosted (venues, challenges, outcomes)</li>
<li>They use humour as their main selling point rather than preparation and reliability</li>
<li>They have no clear process for briefings and run sheets</li>
<li>They're reluctant to share reviews or references</li>
<li>Their pricing is dramatically lower than the market — which usually means dramatically less experience</li>
</ul>

<h2>The Right Questions to Ask</h2>
<ul>
<li>How many weddings have you MC'd in Perth?</li>
<li>Can you describe your preparation process from booking to wedding day?</li>
<li>What happens if you're sick or unavailable on the day?</li>
<li>How do you handle speeches that run over time?</li>
<li>What do you do if the AV fails during an important moment?</li>
<li>Do you use a generic script or write one specifically for each wedding?</li>
</ul>

<h2>Trust Your Gut</h2>
<p>After all the practical questions, trust your instinct about whether this person gets you. The best MC for your wedding isn't necessarily the most experienced or the funniest — it's the one who listens carefully, asks the right questions, and makes you feel like your evening is in genuinely safe hands.</p>
<p>That's the standard. Don't settle for less.</p>
""" + CTA_BOX + "</div>",
    },
    {
        "slug": "blog-what-does-mc-do-at-wedding",
        "title": "What Does an MC Actually Do at a Wedding? | The Perth MC",
        "h1": "What Does an MC Actually Do at a Wedding?",
        "meta": "Most couples know they need one — but what does a wedding MC actually do all night? A full breakdown of the role from ceremony to last dance.",
        "tag": "Weddings",
        "read_time": 5,
        "content": """<div class="blog-body">
<p>It's one of the most common questions from couples in the early stages of wedding planning: "What does the MC actually do?" They know the role exists. They know they probably need one. But beyond "introducing speeches," most people are genuinely unclear on what fills the rest of the evening.</p>
<p>Here's the full picture.</p>

<h2>Before the Reception Even Starts</h2>
<p>A professional MC arrives at your venue well before guests do. They walk the space, check the microphone and AV setup, meet the venue coordinator, brief the DJ or band on cues, and connect with the photographer about key moments. This is where most of the behind-the-scenes work happens — and it's invisible to your guests, which is exactly the point.</p>

<h2>The Welcome and Opening</h2>
<p>The MC officially opens the reception — welcoming guests, acknowledging the occasion, and setting the tone for the evening. This first two minutes matters more than almost anything else. It's when guests form their impression of the night ahead. A confident, warm, well-prepared opening tells the room: you're in good hands, relax and enjoy this.</p>

<h2>Bridal Party Introductions</h2>
<p>The MC introduces the bridal party — typically the groomsmen and bridesmaids, then the flower girls and ring bearers, then the parents of the couple, and finally the newlyweds themselves. This sequence is carefully choreographed with the DJ or band so every entrance gets the right musical moment. The MC times it, calls it, and keeps energy high throughout.</p>

<h2>Managing the Program</h2>
<p>The MC is the keeper of the run sheet throughout the night. They announce when it's time to be seated, signal the kitchen for courses, transition between speeches, coordinate the cake cutting, announce the first dance, and manage any activity or game during the reception. Every transition is their responsibility — and every delay or confusion is theirs to solve gracefully.</p>

<h2>Speech Management</h2>
<p>This is where many non-professional MCs struggle. Managing speeches means more than handing someone a microphone. It means briefing speakers beforehand about timing, gently signalling when they've gone long, keeping energy up during long pauses, and ensuring every speaker gets a proper introduction that warms the audience up for them. An experienced MC keeps speeches to time without anyone feeling rushed.</p>

<h2>Reading the Room</h2>
<p>The most underrated part of the MC role is the constant, invisible work of reading the room. Is the energy dropping? Do guests need a moment to breathe, or do they need to be brought back to attention? Is the bar queue backing up at a moment when guests should be seated? A great MC notices these things and responds — often before the couple or coordinator even registers the issue.</p>

<h2>Handling the Unexpected</h2>
<p>AV drops out. A speaker goes off-script. The meal is delayed by 20 minutes. A family member spontaneously wants to say something. An experienced MC has contingency plans for every common scenario and the improvisation skills to handle the ones they don't. The couple never needs to know anything went sideways.</p>

<h2>Closing the Evening</h2>
<p>The MC closes the formal part of the reception — often with a final toast, an announcement about the dance floor opening, and a farewell to guests not staying for the full evening. It's a moment that deserves as much care as the opening. The best closings leave guests feeling like the evening was complete.</p>
""" + CTA_BOX + "</div>",
    },
    {
        "slug": "blog-wedding-mc-cost-perth",
        "title": "Wedding MC Cost Perth 2025 — Honest Pricing Guide | The Perth MC",
        "h1": "How Much Does a Wedding MC Cost in Perth? (2025 Guide)",
        "meta": "Transparent pricing guide for Perth wedding MCs in 2025. What affects cost, what's included, and how to avoid paying for things you don't need.",
        "tag": "Pricing",
        "read_time": 5,
        "content": """<div class="blog-body">
<p>MC pricing in Perth ranges widely — and that range reflects a genuine difference in experience, preparation, and what you actually get on the day. Here's an honest breakdown.</p>

<h2>The Perth Wedding MC Price Range (2025)</h2>
<ul>
<li><strong>Budget / part-time MCs:</strong> $400–$700 — typically newer MCs, limited wedding experience, often minimal pre-event preparation</li>
<li><strong>Mid-range professional MCs:</strong> $800–$1,400 — experienced, with a clear preparation process and custom scripting</li>
<li><strong>Premium / high-demand MCs:</strong> $1,500–$2,500+ — extensive experience, strong referral networks, often booked 12+ months ahead</li>
</ul>
<p>For most Perth weddings, a well-prepared professional MC sits in the $900–$1,400 range. That's the market for someone who will genuinely invest in your event — not just show up with a generic script.</p>

<h2>What Affects the Price</h2>
<ul>
<li><strong>Hours required:</strong> A 4-hour reception is priced differently to a 7-hour event with ceremony hosting included</li>
<li><strong>Preparation complexity:</strong> Multicultural elements, multiple languages, or a complex program require more preparation time</li>
<li><strong>Travel:</strong> Events in Mandurah, regional WA, or requiring overnight stays attract travel costs</li>
<li><strong>Date:</strong> Peak season dates (November–March) and popular Saturdays may attract a premium</li>
<li><strong>Additional services:</strong> Some MCs offer add-ons like photo montage coordination or additional briefing calls</li>
</ul>

<h2>What Should Be Included as Standard</h2>
<p>At any price point above budget, your MC package should include:</p>
<ul>
<li>Pre-wedding briefing call (not just an email)</li>
<li>Run sheet review and recommendations</li>
<li>Custom script preparation for your specific wedding</li>
<li>Vendor coordination (DJ/band, photographer, venue)</li>
<li>On-the-night hosting from arrival to close</li>
</ul>
<p>If an MC at any price point can't confirm these are included, that's worth noting.</p>

<h2>Is It Worth It?</h2>
<p>Consider what you're actually paying for: the person who holds your entire evening together. Your photographer captures memories. Your florist sets the scene. Your MC determines whether the night actually flows — whether speeches land, whether guests stay engaged, whether the moments that matter most are given the time and space they deserve.</p>
<p>The difference between a $600 and a $1,200 MC is not $600. It's the difference between someone who shows up and someone who shows up prepared.</p>
""" + CTA_BOX + "</div>",
    },
    {
        "slug": "blog-corporate-mc-vs-comedian-perth",
        "title": "Corporate MC vs Comedian Perth — Which Is Right? | The Perth MC",
        "h1": "Corporate MC vs Comedian — What's Right for Your Event?",
        "meta": "Both can work brilliantly. Both can fail spectacularly. How to decide between a corporate MC and a comedian for your Perth event.",
        "tag": "Corporate",
        "read_time": 6,
        "content": """<div class="blog-body">
<p>It's a question corporate event planners in Perth face regularly: do we book a professional MC or bring in a comedian to host the night? Both options have merit — and both can go badly wrong if the choice doesn't match the event.</p>

<h2>What a Corporate MC Does</h2>
<p>A professional corporate MC is a host and facilitator. Their job is to manage the program, introduce speakers, keep energy up across a long day or evening, handle Q&amp;As, coordinate with AV and vendors, and keep the event moving at pace. Their success is measured by how smoothly the event runs and how engaged the audience stays — not by how many laughs they get.</p>

<h2>What a Comedian Does</h2>
<p>A comedian's primary job is to entertain. When they're also hosting an event, they bring a performance-oriented energy that can work brilliantly — if the audience and context are right. The risk is that comedy that works in a club doesn't always work in a conference room with mixed age groups, different cultural backgrounds, and colleagues who have to work together on Monday.</p>

<h2>When a Comedian MC Works Well</h2>
<ul>
<li>The event is primarily social rather than formal (Christmas party, team day)</li>
<li>The audience shares a broadly similar demographic and sensibility</li>
<li>The client has seen the comedian's material and is confident it suits their culture</li>
<li>Program management is simple and the event doesn't require heavy facilitation</li>
<li>The comedian has genuine MC experience — not just stand-up</li>
</ul>

<h2>When a Professional MC Is the Safer Choice</h2>
<ul>
<li>The event has complex program management (conferences, AGMs, awards nights)</li>
<li>The audience is diverse in age, background, or seniority</li>
<li>The stakes are high (client-facing events, major industry awards)</li>
<li>The event requires genuine facilitation (panels, Q&amp;As, live auctions)</li>
<li>Brand alignment and professionalism are non-negotiable</li>
</ul>

<h2>The Hybrid Question</h2>
<p>Some experienced MCs are genuinely funny — and some comedians are genuinely skilled at event management. The question isn't comedian vs MC as a personality type; it's which skillset your event actually requires.</p>
<p>If your event is 80% program and 20% entertainment, you need an MC with good humour. If it's 80% entertainment and 20% program, a comedian with MC experience might serve you better. Most corporate events in Perth sit firmly in the first category.</p>

<h2>The Question to Ask Yourself</h2>
<p>If something goes wrong on the night — the AV fails, a speaker overruns by 20 minutes, the dinner is delayed — who do you want on the microphone managing the room? A comedian who needs to be funny, or a professional MC who knows how to handle the unexpected with calm and authority?</p>
<p>That question usually provides the answer.</p>
""" + CTA_BOX + "</div>",
    },
    {
        "slug": "blog-questions-to-ask-mc-before-booking",
        "title": "Questions to Ask Your MC Before Booking | The Perth MC",
        "h1": "Questions to Ask Your MC Before Booking",
        "meta": "Don't sign a contract until you've asked these. A checklist of essential questions that reveal whether an MC is right for your event.",
        "tag": "Planning",
        "read_time": 5,
        "content": """<div class="blog-body">
<p>Meeting a prospective MC for your event is a bit like a job interview — except you're the one doing the hiring. The right questions will quickly reveal whether you're talking to a professional or an enthusiastic amateur. Here's the checklist.</p>

<h2>Experience Questions</h2>
<ul>
<li>How many events like mine have you hosted?</li>
<li>Can you give me a specific example of a wedding (or corporate event) you've hosted recently — venue, challenges, how the night went?</li>
<li>Have you worked at my venue before?</li>
<li>What's the most challenging event you've managed and how did you handle it?</li>
</ul>

<h2>Process Questions</h2>
<ul>
<li>Walk me through your preparation process from booking to event day.</li>
<li>Do you use a generic script or write one specifically for each event?</li>
<li>How do you approach a pre-event briefing?</li>
<li>How do you handle the run sheet — do you work with the venue coordinator, or separately?</li>
<li>How do you coordinate with the DJ/band and photographer?</li>
</ul>

<h2>On-Night Scenarios</h2>
<ul>
<li>What do you do if a speech runs significantly over time?</li>
<li>How do you handle AV failures during an important moment?</li>
<li>What happens if the program falls 30 minutes behind schedule?</li>
<li>Have you ever had to manage a difficult or emotional moment on the microphone? How did you approach it?</li>
</ul>

<h2>Logistics and Contract Questions</h2>
<ul>
<li>What happens if you're ill or unavailable on the day — do you have a backup?</li>
<li>What's included in your fee and what costs extra?</li>
<li>How do travel costs work if the venue is outside Perth metro?</li>
<li>What do you need from me between booking and the event?</li>
<li>When do you arrive at the venue relative to guest arrival?</li>
</ul>

<h2>The Most Revealing Question</h2>
<p>Ask them: "What questions do you have for me about my event?"</p>
<p>A professional MC will have a list. They'll want to understand the couple's story, the audience demographic, any sensitive family dynamics, the venue's layout, the program structure, and what the event should feel like by the end of the night. An average MC will nod along and tell you they can handle anything.</p>
<p>Curiosity about your specific event is the clearest sign of a prepared professional. Treat it as a green flag.</p>
""" + CTA_BOX + "</div>",
    },
    {
        "slug": "blog-mc-vs-dj-who-runs-the-room",
        "title": "MC vs DJ — Who Actually Runs the Room? | The Perth MC",
        "h1": "MC vs DJ — Who Actually Runs the Room?",
        "meta": "Two completely different roles that are often confused. Understanding what each one does will make your event planning much clearer.",
        "tag": "Weddings",
        "read_time": 5,
        "content": """<div class="blog-body">
<p>One of the most common misconceptions in wedding and event planning is that the DJ and the MC do similar things — or that one can substitute for the other. They can't. They're distinct roles with distinct skillsets, and confusing them leads to poor hiring decisions and gaps in your event coverage.</p>

<h2>What the DJ Does</h2>
<p>A DJ manages the music and audio. They read the dance floor, mix tracks, manage the room's musical energy, and operate the sound system. A skilled DJ is an artist — they know how to build a room from dinner background music through to late-night dancing, when to drop a classic, and how to read what the crowd wants next.</p>
<p>What a DJ does not do: manage your program, introduce your speakers, time your speeches, coordinate your bridal party, or manage the flow of your event. Their world is sound. Everything else is outside their lane.</p>

<h2>What the MC Does</h2>
<p>An MC is the host and program manager. They open the evening, introduce the bridal party, manage speeches, coordinate with all vendors, keep the event on time, and hold the room's attention during every transition. A skilled MC is invisible at their best — guests don't notice the hosting, they just feel like the night flows naturally.</p>
<p>What an MC does not do: manage the music system, read the dance floor, or fill time with entertainment. Their job is coordination and communication — the connective tissue of your event.</p>

<h2>How They Work Together</h2>
<p>The best events happen when the MC and DJ are in sync. The MC signals the DJ for specific cues (bridal party entry music, first dance countdown, transition to dancing after speeches), and the DJ executes those cues at exactly the right moment. This requires clear communication and mutual respect — which is why a good MC will always introduce themselves to the DJ at the start of the evening.</p>

<h2>What Happens When There's No MC</h2>
<p>Sometimes a DJ will offer to "MC the night" as part of their package. For some very simple events, this can work. For a wedding with bridal party introductions, multiple speeches, formal dinners, and key moments to be cued — it almost never works well. The DJ is managing music and audio while trying to manage a microphone and a program. Something suffers.</p>
<p>The result: transitions feel abrupt, speeches aren't properly introduced, energy drops between moments, and the program runs behind schedule without anyone managing it back on track.</p>

<h2>The Bottom Line</h2>
<p>For any event with a formal program — speeches, presentations, key moments, or a guest count above 60 — you need both. The DJ runs the music. The MC runs the room. They're partners, not substitutes.</p>
""" + CTA_BOX + "</div>",
    },
    {
        "slug": "blog-how-to-write-run-sheet-for-mc",
        "title": "How to Write a Run Sheet for Your MC | The Perth MC",
        "h1": "How to Write a Run Sheet for Your MC",
        "meta": "A tight run sheet is the backbone of a smooth event. Step-by-step guide to writing one your MC and all vendors can actually use.",
        "tag": "Planning",
        "read_time": 6,
        "content": """<div class="blog-body">
<p>A run sheet is the single most important document in event planning. It's the shared truth that keeps your MC, venue coordinator, DJ, and photographer all working from the same page. A vague run sheet leads to confusion. A tight one leads to a smooth night.</p>
<p>Here's how to build one that actually works.</p>

<h2>Structure: Column by Column</h2>
<p>A good run sheet has four columns:</p>
<ul>
<li><strong>Time:</strong> The scheduled time for each element (e.g., 6:30 PM)</li>
<li><strong>Duration:</strong> How long that element runs (e.g., 5 min)</li>
<li><strong>Element:</strong> What's happening (e.g., "Bridal party entry")</li>
<li><strong>Notes:</strong> Who's responsible, what music plays, any special instructions</li>
</ul>
<p>Keep it as a simple table — in a Word doc, Google Sheet, or even a printed spreadsheet. The simpler the format, the easier it is to read under pressure.</p>

<h2>Start with the Anchors</h2>
<p>Begin by locking in the non-negotiable time anchors — the moments that have external dependencies:</p>
<ul>
<li>Guest arrival / cocktail hour start</li>
<li>Guests seated for dinner</li>
<li>Meal service times (agreed with the venue/caterer)</li>
<li>Sunset / golden hour (for photography)</li>
<li>Venue noise curfew (if applicable)</li>
<li>Finish time</li>
</ul>
<p>Everything else is built around these.</p>

<h2>Build in Buffer Time</h2>
<p>Every event planner underestimates this. Speeches always run a few minutes long. The kitchen is slightly late. The bridal party needs a moment. Build 10–15 minutes of buffer time into your run sheet — especially around meal service and speeches. It means arriving at the dancing phase on time rather than 45 minutes late.</p>

<h2>Speech Order and Timing</h2>
<p>Be specific. Don't just write "Speeches — 7:30 PM." Write:</p>
<ul>
<li>7:30 PM — Father of the Bride (allocated 5 min)</li>
<li>7:36 PM — Best Man (allocated 7 min)</li>
<li>7:44 PM — Maid of Honour (allocated 5 min)</li>
<li>7:50 PM — Couple's response (allocated 5 min)</li>
</ul>
<p>Share these timings with speakers beforehand and ask your MC to gently signal when time is up.</p>

<h2>Include MC Cues Explicitly</h2>
<p>Your MC needs to know exactly what they're announcing and when. For every element in the run sheet, note:</p>
<ul>
<li>Does the MC announce this? (Yes/No)</li>
<li>What music should play (if any)?</li>
<li>Who triggers it — MC, DJ, or venue coordinator?</li>
</ul>

<h2>Share It with Everyone</h2>
<p>Every vendor should have the run sheet at least a week before the event. Your MC, DJ/band, photographer, videographer, venue coordinator, and caterer should all be working from the same document. Discrepancies are much easier to resolve before the day than during it.</p>

<h2>Keep a Master Copy</h2>
<p>Nominate one person (usually the venue coordinator or the MC) as the keeper of the master run sheet. They're the one making adjustments on the night and communicating changes to other vendors. Everyone else should be checking in with them, not running their own timing.</p>
""" + CTA_BOX + "</div>",
    },
    {
        "slug": "blog-best-wedding-venues-perth-2025",
        "title": "Best Wedding Venues in Perth 2025 — MC's Guide | The Perth MC",
        "h1": "Best Wedding Venues in Perth 2025",
        "meta": "Perth's top wedding venues reviewed by a professional MC who's hosted at most of them — from Swan Valley wineries to Fremantle heritage spaces.",
        "tag": "Venues",
        "read_time": 7,
        "content": """<div class="blog-body">
<p>Perth has an outstanding range of wedding venues — and as an MC who's hosted events at dozens of them, I have opinions. Here's a practical guide to some of Perth's best wedding venues, written from the perspective of someone who's stood at the microphone in most of them.</p>

<h2>Swan Valley: Winery Weddings</h2>
<p>The Swan Valley is Perth's premier wine country wedding destination. Venues like Mandoon Estate, Sandalford Wines, and Houghton Winery offer the combination of stunning grounds, on-site catering, and established event infrastructure that makes hosting straightforward. The indoor/outdoor flow at most Swan Valley venues is excellent — ceremony in the vines, reception in a beautifully converted barrel hall.</p>
<p>From an MC perspective: Swan Valley venues are generally well-run. The AV is usually solid, the venue coordinators are experienced, and the run sheets tend to be tight because these venues do this every weekend.</p>

<h2>Fremantle: Heritage and Harbour</h2>
<p>Fremantle offers a unique character that no other Perth precinct can match. The Fremantle Arts Centre is one of the most atmospheric wedding venues in Western Australia — a 19th century Gothic building with beautiful grounds. The Esplanade Hotel offers harbour views and a more traditional function centre experience. Little Creatures is a wildly popular choice for couples who want something deliberately different.</p>
<p>Freo venues reward couples who embrace their venue's personality. These aren't blank-canvas spaces — they have a distinct character, and the best weddings I've MC'd here worked with that character rather than against it.</p>

<h2>Kings Park and the Botanic Garden</h2>
<p>Fraser's Restaurant at Kings Park is one of Perth's most iconic wedding venues — cantilevered over the park with views of the city skyline and the Swan River. The setting is genuinely spectacular, and the venue's operation is polished. The Terrace at Fraser's hosts outdoor ceremonies that, on a clear Perth evening, are hard to beat for sheer visual impact.</p>

<h2>Riverside and Waterfront Venues</h2>
<p>Venues along the Swan River — including Frasers, the Novotel Vines, and a number of private estate properties — offer the Perth waterway backdrop that photographs beautifully and creates a natural sense of occasion. Timing around sunset at these venues requires careful run sheet management — golden hour is short and the photography window is critical.</p>

<h2>City Hotels and Function Centres</h2>
<p>For large guest lists (200+) or events with complex staging, Perth's major hotels — Crown, Pan Pacific, QT Perth, and the Ritz-Carlton — offer professional infrastructure and experienced event teams. These venues are particularly well-suited to corporate wedding receptions where polish and logistics take priority over character.</p>

<h2>Intimate and Boutique Options</h2>
<p>For smaller weddings, Perth has excellent boutique venues — Lamont's Bishops House in East Perth, The Flour Factory in the CBD, and various private estate properties in the hills. These spaces suit couples who want something intimate and distinctive over something grand.</p>

<h2>Choosing the Right Venue for Your MC</h2>
<p>When you're shortlisting venues, ask your MC if they've hosted there before. Familiarity with a venue's layout, AV setup, and team can make a significant difference — particularly for outdoor venues where acoustics and crowd management are more complex.</p>
""" + CTA_BOX + "</div>",
    },
    {
        "slug": "blog-do-you-need-mc-small-wedding",
        "title": "Do You Need an MC for a Small Wedding? | The Perth MC",
        "h1": "Do You Need an MC for a Small Wedding?",
        "meta": "50 guests or under — do you still need a professional MC? An honest answer that considers your venue, program length, and what could go wrong.",
        "tag": "Weddings",
        "read_time": 5,
        "content": """<div class="blog-body">
<p>It's the question couples planning intimate weddings frequently ask: with only 30, 40, or 50 guests, do we really need a professional MC? The honest answer is: it depends. Here's how to decide.</p>

<h2>When You Probably Don't Need a Professional MC</h2>
<ul>
<li>Your event is truly informal — a backyard gathering or casual lunch with no formal program</li>
<li>You have no speeches at all, or just one brief toast</li>
<li>There's no DJ or band — just a playlist</li>
<li>There are no formal moments to coordinate (no bridal party entry, no cake cutting, no first dance)</li>
<li>The venue is very small and acoustics mean a microphone isn't needed</li>
</ul>
<p>In this case, a trusted friend or family member can handle the minimal hosting required, and the intimacy of a small gathering makes professional hosting feel more formal than necessary.</p>

<h2>When You Still Need a Professional MC</h2>
<ul>
<li>You have multiple speeches that need to be managed and timed</li>
<li>You have formal moments — bridal party entry, first dance, cake cutting</li>
<li>You're using a venue with a run sheet and coordinating with a DJ or band</li>
<li>Your guest list includes different family groups who don't know each other</li>
<li>You want to actually enjoy the night rather than worry about what comes next</li>
</ul>
<p>This last point is underrated. At a small wedding, the couple is visible to every guest at almost every moment. If the program falls apart, there's nowhere to hide — and if the couple is anxious about timing and logistics, every guest can see it.</p>

<h2>The Friend-as-MC Risk</h2>
<p>The most common small wedding MC mistake is giving the role to a friend who's "good at talking." The problem: that friend is also a guest at your wedding. They want to drink, chat, and celebrate. When the role conflicts with being present in the moment, something gives — and it's usually the hosting.</p>
<p>A professional MC is not a guest. Their job is to be present and focused while everyone else celebrates. That's a very different mindset — and it's why the professional almost always outperforms the willing friend, even at small events.</p>

<h2>The Alternative: A Day-of Coordinator</h2>
<p>For genuinely intimate weddings with minimal program elements, a day-of wedding coordinator can often handle the light hosting responsibilities alongside their logistics role. This can be a cost-effective middle ground for small guest lists with simple programs.</p>
<p>For anything with speeches, a bridal party, and formal moments — even with 40 guests — a dedicated MC will serve you better.</p>
""" + CTA_BOX + "</div>",
    },
    {
        "slug": "blog-how-far-advance-book-wedding-mc",
        "title": "How Far in Advance to Book a Wedding MC Perth | The Perth MC",
        "h1": "How Far in Advance Should You Book a Wedding MC?",
        "meta": "Spoiler: earlier than you think. The timeline for booking an MC in Perth and what to do if you're already running late.",
        "tag": "Planning",
        "read_time": 4,
        "content": """<div class="blog-body">
<p>Most couples book their venue 12–18 months out, their photographer 10–12 months out, and their MC about three weeks before the wedding after realising they forgot. Here's why that's backwards — and what the right timeline looks like.</p>

<h2>The Recommended Booking Timeline</h2>
<ul>
<li><strong>12+ months out:</strong> Ideal for peak season dates (October–March, especially Saturdays). Popular MCs are booked this far ahead.</li>
<li><strong>8–10 months out:</strong> Still good for most dates. You'll have strong options across all experience levels.</li>
<li><strong>4–6 months out:</strong> Possible for mid-week or off-peak dates. Weekends in spring and summer may be limited.</li>
<li><strong>Under 3 months:</strong> You'll need to be flexible and may have limited choices, particularly for sought-after dates.</li>
</ul>

<h2>Why Perth's Peak Season Books Out Fast</h2>
<p>Perth has a genuine wedding season — spring and summer weekends (October through March) are highly competitive. A professional MC with strong reviews and repeat referrals will often have their peak season calendar substantially booked 12 months ahead. The best vendors in any category sell out first.</p>

<h2>What to Do If You're Already Running Late</h2>
<p>Don't panic — reach out immediately and be transparent about your timeline. Good MCs often have cancellations, and a short-notice booking isn't necessarily impossible. Be clear about your date, venue, and guest numbers so they can quickly confirm availability.</p>
<p>If your preferred MC isn't available, ask for a referral. Professional event vendors in Perth tend to know each other and can often point you toward someone at a similar level who may have your date free.</p>

<h2>Book Before You've Finalised the Run Sheet</h2>
<p>You don't need a complete program plan to book an MC. You just need a confirmed date and venue. A good MC will help you build and refine the run sheet — that's part of what you're hiring them for. Book the person first, then develop the program together.</p>

<h2>The One-Step Action</h2>
<p>If you've just started wedding planning and you're reading this at the 12-month mark: add "contact MC" to this week's list, alongside venue viewings. Treat it as an early priority, not a late afterthought. The best dates go to the couples who plan ahead.</p>
""" + CTA_BOX + "</div>",
    },
    {
        "slug": "blog-what-to-wear-wedding-mc-perth-summer",
        "title": "What to Wear as a Wedding MC in Perth Summer | The Perth MC",
        "h1": "What to Wear as a Wedding MC in Perth Summer",
        "meta": "Dress standards, heat management, and why the right outfit matters more than you'd think. Practical advice for Perth's outdoor wedding season.",
        "tag": "Weddings",
        "read_time": 5,
        "content": """<div class="blog-body">
<p>Perth summer is spectacular — and unforgiving. Temperatures regularly exceed 35°C on wedding days from December through February, and even October and March can deliver surprises. For an MC standing in the sun, managing a microphone and a run sheet for six or seven hours, what you wear matters practically as well as aesthetically.</p>

<h2>Dress Standard: Match or Slightly Below the Couple</h2>
<p>The standard rule: dress one step below the couple's wedding party. If groomsmen are in full morning suits, the MC wears a tailored suit. If groomsmen are in linen blazers, the MC might wear smart trousers and a dress shirt. The MC should look polished and coordinated without competing with the bridal party.</p>
<p>Check with the couple about their preferred dress code. Some couples have colour preferences or specific requests — an MC who asks is an MC who's thinking about the full picture.</p>

<h2>Fabric Choices for Perth Summer</h2>
<ul>
<li><strong>Linen:</strong> Breathable and appropriate for outdoor Perth events. Slightly less formal but well-suited to beach and garden settings.</li>
<li><strong>Light wool:</strong> Surprisingly good in heat if the weave is open. Holds its shape better than linen and looks more polished.</li>
<li><strong>Lightweight cotton:</strong> Works for smart-casual events but can look informal for more formal weddings.</li>
<li><strong>Avoid:</strong> Heavy wool, polyester suits, or anything dark-coloured if the ceremony is outdoors in full sun.</li>
</ul>

<h2>Practical Considerations</h2>
<ul>
<li>Arrive early enough to acclimatise to the heat before guests arrive</li>
<li>Stay hydrated — you're talking for six to seven hours and dry voice is a real issue</li>
<li>Have a contingency plan for shade during outdoor elements</li>
<li>Know where the nearest cool space is if you need a moment between program elements</li>
<li>Consider SPF — if you're outdoors for the ceremony, sunscreen is not optional</li>
</ul>

<h2>For Evening Receptions</h2>
<p>Perth evenings in summer are beautiful — warm without being oppressive, with a sea breeze that usually arrives by 5–6 PM. Indoor receptions are climate-controlled. For evening events, a full suit is entirely appropriate and comfortable.</p>

<h2>The Bigger Picture</h2>
<p>Your MC's appearance is part of the event's presentation. A well-dressed, professional-looking host signals to guests that they're in good hands before a word is spoken. It's worth investing in an outfit appropriate for the venue and occasion — not just wearing something that almost fits.</p>
""" + CTA_BOX + "</div>",
    },
    {
        "slug": "blog-how-to-brief-mc-corporate-event",
        "title": "How to Brief Your MC for a Corporate Event | The Perth MC",
        "h1": "How to Brief Your MC for a Corporate Event",
        "meta": "The information your MC needs before any corporate event — and why a thorough briefing is the most valuable thing you can do before the day.",
        "tag": "Corporate",
        "read_time": 5,
        "content": """<div class="blog-body">
<p>The quality of your MC on the night is largely determined by the quality of the briefing you give them in the days and weeks before. A thorough, well-organised briefing produces a prepared, confident host. A last-minute email with the run sheet attached produces an MC who's still reading their notes when guests arrive.</p>
<p>Here's what your MC needs — and when they need it.</p>

<h2>Timing: At Least One Week Out</h2>
<p>Send your MC the complete briefing pack at least a week before the event. Ideally two. This gives them time to research, prepare their script, come back to you with questions, and feel fully across the program before they walk in the room.</p>

<h2>The Run Sheet</h2>
<p>Your MC needs the complete, current run sheet — not a draft, not a summary. Every element timed, every transition noted, every speaker listed with their allocated time and a brief description of their role.</p>
<p>If the run sheet changes after you've sent it (it will), send an updated version immediately. Run sheet discrepancies on the night are avoidable.</p>

<h2>Speaker Information</h2>
<p>For every speaker, your MC needs:</p>
<ul>
<li>Full name (correctly spelled and confirmed pronunciation)</li>
<li>Title and organisation</li>
<li>A 2–3 sentence bio for their introduction</li>
<li>Topic or focus of their presentation</li>
<li>Allocated time</li>
<li>Any special requirements (slides, water, specific microphone setup)</li>
</ul>
<p>Nothing undermines an MC's credibility faster than mispronouncing a speaker's name or reading a bio that's six years out of date. Verify all speaker information directly with the speakers or their assistants.</p>

<h2>Audience Information</h2>
<ul>
<li>Who is attending? (Industry, seniority mix, demographic)</li>
<li>Are there any VIPs or clients in the room who warrant specific acknowledgement?</li>
<li>Is there any organisational context the MC needs? (A recent acquisition, a team achievement, a difficult year?)</li>
<li>Are there any topics, jokes, or references to avoid?</li>
</ul>

<h2>Logistics</h2>
<ul>
<li>Venue address and parking/access details</li>
<li>Contact name for the venue coordinator on the day</li>
<li>AV contact (who manages the screens, microphone, and tech)</li>
<li>Dress code</li>
<li>Call time (when should the MC arrive?)</li>
<li>Any planned surprises or off-program moments</li>
</ul>

<h2>The Briefing Call</h2>
<p>Send the written briefing pack first, then schedule a 30-minute call to discuss it. The call is where nuance happens — the things that are hard to capture in a document, like the tone you want, the moments that matter most, and any sensitivities around specific content or people.</p>
<p>An MC who asks good questions on the briefing call is an MC who's already preparing. That's the one you want.</p>
""" + CTA_BOX + "</div>",
    },
    {
        "slug": "blog-indoor-vs-outdoor-wedding-mc-perth",
        "title": "Indoor vs Outdoor Wedding MC Tips Perth | The Perth MC",
        "h1": "Indoor vs Outdoor Wedding MC Tips Perth",
        "meta": "Outdoor weddings in Perth are stunning — and logistically more complex. What your MC needs to know when the venue is open-air.",
        "tag": "Weddings",
        "read_time": 6,
        "content": """<div class="blog-body">
<p>Perth is blessed with weather that makes outdoor weddings genuinely viable for much of the year. But outdoor venues come with a specific set of challenges — acoustic, logistical, and meteorological — that require different preparation from an indoor reception. Here's what your MC needs to know.</p>

<h2>The Acoustic Challenge</h2>
<p>Outdoor spaces don't contain sound the way buildings do. Voices disperse. Background noise (traffic, wind, ambient sound) competes. Guests at the back of a large outdoor setting may struggle to hear clearly, even with a microphone. An experienced outdoor MC knows how to project effectively through a PA system, position themselves to take advantage of the sound setup, and adjust their pacing for outdoor acoustics.</p>
<p>When booking an outdoor venue, ask specifically about their PA system and speaker placement. A poorly placed sound system in an outdoor setting can render even the best MC difficult to hear.</p>

<h2>Wind: The Outdoor MC's Nemesis</h2>
<p>Perth's Fremantle Doctor arrives reliably from the south-west in the afternoon from October through February. For outdoor ceremonies and receptions starting before 5 PM, wind management is a real consideration. Lapel microphones can be affected by wind noise. Handheld mics require a specific grip to minimise it. An experienced outdoor MC knows which microphone type works best in which conditions and will discuss this with the AV team beforehand.</p>

<h2>Timing Around the Sun</h2>
<p>Outdoor Perth weddings are partly about the light — and your photographer will have strong feelings about golden hour. The timing of key photographic moments (bridal party shots, couple portraits) relative to sunset requires careful run sheet management. Your MC should know the sunset time for your wedding date and build this into their program awareness.</p>
<p>A great outdoor MC plans the program so that the couple is in the right place at the right time for their photography — not scrambling to get portraits done after the light has gone.</p>

<h2>Weather Contingency Planning</h2>
<p>Perth weather is generally reliable — but 'generally' is not 'always.' Outdoor venue bookings should come with a weather contingency plan. Your MC needs to know:</p>
<ul>
<li>What is the wet weather backup plan?</li>
<li>At what point is the decision made to move indoors?</li>
<li>Who makes that call, and who communicates it to guests?</li>
<li>How does the indoor setup differ from the outdoor plan?</li>
</ul>
<p>The MC is often the person communicating program changes to guests, so they need to know the contingency plan before the event, not when it starts raining.</p>

<h2>Guest Management in Open Spaces</h2>
<p>Indoor venues naturally corral guests into defined areas. Outdoor spaces don't. Guests wander, conversations continue, and gathering attention for a program element is harder. An experienced outdoor MC knows how to command attention in an open space — how to signal a transition, how to gather a dispersed crowd, and how to time announcements so they don't catch guests mid-conversation in a far corner.</p>

<h2>The Practical Checklist</h2>
<ul>
<li>Confirm PA system coverage for the outdoor area</li>
<li>Know the sunset time and plan photography windows</li>
<li>Understand the wind direction and peak arrival time for your date</li>
<li>Confirm the wet weather contingency plan</li>
<li>Arrive early to test the microphone in the outdoor setting</li>
<li>Coordinate shade and hydration for yourself during the event</li>
</ul>
""" + CTA_BOX + "</div>",
    },
    {
        "slug": "blog-how-to-make-christmas-party-fun-perth",
        "title": "How to Make Your Corporate Christmas Party Actually Fun | The Perth MC",
        "h1": "How to Make Your Corporate Christmas Party Actually Fun",
        "meta": "Most corporate Christmas parties are forgettable. Here's the formula for one people will still be talking about in February.",
        "tag": "Corporate",
        "read_time": 5,
        "content": """<div class="blog-body">
<p>The corporate Christmas party has a reputation problem. It's often the event that people go to because they feel like they have to — and leave as quickly as politeness allows. That's not inevitable. It's a hosting and planning problem, and it's very fixable.</p>

<h2>Start with a Clear Purpose</h2>
<p>Most forgettable Christmas parties fail at the brief. "Have a Christmas party" is not a brief. "Celebrate this year's achievements, recognise our standout performers, and send the team into the break feeling genuinely valued" — that's a brief. Everything from venue to hosting to entertainment flows from a clear sense of what the event is actually for.</p>

<h2>Acknowledge What Actually Happened This Year</h2>
<p>Nothing makes a Christmas party feel more generic than a speech that could have been given in any year at any company. The MC and the speaking programme should reference specific things that happened this year — wins, milestones, challenges overcome, people who stepped up. Specificity creates connection. Generic platitudes create eye-rolling.</p>

<h2>Keep the Formal Program Short</h2>
<p>The tolerance for formal content at a Christmas party is limited. Speeches should be tight — CEO address: 5 minutes maximum. Awards: move quickly, keep energy high. The goal is to get through the formal program efficiently so the social part of the evening can breathe. An MC who runs formal proceedings tightly is worth their fee in goodwill alone.</p>

<h2>Add One Unexpected Element</h2>
<p>The parties people talk about always have something they didn't expect. A surprise performer. An interactive activity during dinner. A roast segment. A photo booth with ridiculous props. A quiz with prizes that are actually worth winning. One well-chosen unexpected element elevates a party from "fine" to "actually fun."</p>

<h2>The Awards That Actually Matter</h2>
<p>Recognition at a Christmas party works when it's genuine and specific. "Employee of the Year" presented as a tick-box exercise is worse than not having awards at all. Awards that work: are given to people who genuinely deserve them, come with a real explanation of why they're receiving it, and are delivered by someone who actually knows the recipient's work.</p>

<h2>Give the MC Real Information to Work With</h2>
<p>The difference between a good Christmas party MC and a great one is the briefing they receive. An MC who knows the team's wins, knows who's leaving, knows the inside jokes that are safe to make, and knows what the team actually cares about can make a room feel like they're celebrating themselves — not just showing up for a free meal.</p>
<p>Brief your MC thoroughly. The investment of an hour's prep call pays dividends all night.</p>
""" + CTA_BOX + "</div>",
    },
    {
        "slug": "blog-multicultural-wedding-mc-perth",
        "title": "MC for a Multicultural Wedding in Perth | The Perth MC",
        "h1": "MC for a Multicultural Wedding in Perth — What to Know",
        "meta": "How a professional MC navigates cultural traditions, bilingual elements, and complex family dynamics at multicultural Perth weddings.",
        "tag": "Weddings",
        "read_time": 6,
        "content": """<div class="blog-body">
<p>Perth is one of Australia's most multicultural cities — and Perth weddings reflect that diversity beautifully. Multicultural weddings are among the most rewarding events to host — rich in tradition, layered in meaning, and full of genuine celebration. They also require specific preparation that not every MC brings to the table.</p>

<h2>Understanding the Cultural Program</h2>
<p>Every culture has wedding traditions — some visible, some invisible to outsiders. A couple planning a multicultural wedding should sit down with their MC well in advance to walk through every cultural element in the program and explain its significance. The MC needs to understand not just what happens but why it happens and what the right tone is for each moment.</p>
<p>For Western couples incorporating a partner's cultural traditions: the MC should do their own research, not rely solely on the briefing. A basic familiarity with the tradition demonstrates respect and builds confidence with the family.</p>

<h2>Bilingual and Multilingual Elements</h2>
<p>Many multicultural Perth weddings include elements in two languages — a speech delivered in Mandarin, a toast in Italian, a blessing in Filipino. The MC's role here is to prepare the audience for what's coming, provide brief context if needed, and manage the transition before and after without making the non-English element feel marginalised.</p>
<p>Ask the couple whether any translation is expected and who will provide it. Some guests will need it; others won't. The MC should know the plan before the evening, not improvise on the night.</p>

<h2>Pronunciation: Get It Right</h2>
<p>Nothing undermines an MC's credibility at a multicultural wedding faster than mispronouncing the names of the couple's family members. Get a list of every name you'll need to say, ask for phonetic pronunciation, and practise. Send a recording of yourself saying each name to the couple and ask them to correct it.</p>
<p>This applies to place names, cultural terms, and any non-English elements that will appear in your script. It takes 30 minutes of preparation and makes an enormous difference to how you're perceived.</p>

<h2>Navigating Family Dynamics</h2>
<p>Multicultural weddings often bring together families with very different expectations about weddings — different attitudes toward formality, speaking, alcohol, music, and timing. An experienced MC reads these dynamics quickly and adjusts accordingly: being more formal in acknowledgements when family elders are present, managing the pace more carefully when the two families are still finding their comfort level with each other.</p>

<h2>The Tone Around Cultural Moments</h2>
<p>Cultural traditions at weddings deserve to be treated with the same weight as Western elements — not novelty, not spectacle. The MC's introduction to a traditional tea ceremony, a hora, a jumping of the broom, or a tossing of sweets should convey genuine respect for the tradition and its meaning. If you're not sure what to say, less is more. Let the moment speak for itself.</p>

<h2>Ask the Couple What They Actually Want</h2>
<p>Some multicultural couples want both cultures represented equally throughout the evening. Others want to incorporate specific traditions but otherwise run a more Western-style reception. There's no correct answer — the MC's job is to understand what this couple wants and deliver it, not to impose their own assumptions about what a multicultural wedding should look like.</p>
""" + CTA_BOX + "</div>",
    },
    {
        "slug": "blog-mc-vs-wedding-celebrant-difference",
        "title": "MC vs Wedding Celebrant — What's the Difference? | The Perth MC",
        "h1": "What's the Difference Between an MC and a Wedding Celebrant?",
        "meta": "Two completely different roles that are often confused. Understanding what each one does will make your vendor planning much clearer.",
        "tag": "Weddings",
        "read_time": 5,
        "content": """<div class="blog-body">
<p>They both hold a microphone. They both stand at the front of the room. They're often confused — but a wedding celebrant and a wedding MC are entirely different roles with different training, different responsibilities, and different parts of the day.</p>

<h2>The Wedding Celebrant</h2>
<p>A celebrant is legally authorised to solemnise marriages. They conduct the wedding ceremony — the legal part of the day that makes you officially married. Their role covers:</p>
<ul>
<li>Preparing and lodging the legal paperwork (Notice of Intended Marriage, Declaration of No Legal Impediment)</li>
<li>Writing and delivering the ceremony script</li>
<li>Personalising the ceremony to reflect your relationship</li>
<li>Officiating the vows and ring exchange</li>
<li>Witnessing and signing the marriage certificate</li>
</ul>
<p>Once the ceremony ends, the celebrant's formal role is complete. Some celebrants stay for the reception as guests; most don't. They are not responsible for the reception program.</p>

<h2>The Wedding MC</h2>
<p>An MC (Master of Ceremonies) hosts the reception — the celebration that follows the ceremony. They have no legal function. Their role covers:</p>
<ul>
<li>Welcoming guests to the reception</li>
<li>Introducing the bridal party</li>
<li>Managing speeches, toasts, and transitions</li>
<li>Coordinating with DJ, band, venue, and photographer</li>
<li>Keeping the program on time and the energy high</li>
<li>Closing the formal part of the evening</li>
</ul>
<p>An MC is not qualified or required to do anything a celebrant does. They are two separate vendors for two separate parts of the day.</p>

<h2>Can the Same Person Do Both?</h2>
<p>Sometimes. Some celebrants also offer MC services, and some MCs have obtained celebrant accreditation. If a vendor offers both, ask careful questions about their experience in each role — they're both significant responsibilities, and a vendor who does one exceptionally may be average at the other.</p>
<p>For most weddings, using separate professionals for each role produces better outcomes. You're hiring for depth of expertise in each area, not breadth.</p>

<h2>Which Do You Need?</h2>
<p>If you're getting married: both. The celebrant handles the ceremony; the MC handles the reception. They should be briefed jointly at some point to ensure the transition from ceremony to reception is coordinated — particularly around timing, photography, and the cocktail hour.</p>
<p>Brief them together at least once before the day. A celebrant who knows when the reception starts and an MC who knows when the ceremony is finishing produce a much smoother handover than two separate vendors who've never spoken.</p>
""" + CTA_BOX + "</div>",
    },
    {
        "slug": "blog-how-to-write-wedding-mc-script",
        "title": "How to Write a Wedding MC Script | The Perth MC",
        "h1": "How to Write a Wedding MC Script",
        "meta": "The key elements of a wedding MC script — from opening welcome to last call. A framework you can customise for your event.",
        "tag": "Weddings",
        "read_time": 7,
        "content": """<div class="blog-body">
<p>A wedding MC script is not a speech — it's a working document that guides every transition, introduction, and announcement across the entire reception. Here's how to build one that's practical, personal, and adaptable.</p>

<h2>The Core Principle: Scripts Should Serve, Not Constrain</h2>
<p>A script is a starting point, not a prison. The best MCs work from detailed notes rather than word-for-word scripts, which allows them to respond to what's actually happening in the room. The script captures what needs to happen; the MC decides in the moment exactly how to say it.</p>
<p>That said, some elements — particularly emotional introductions and specific announcements — benefit from careful pre-written language. Write those sections word-for-word. Write the rest as bullet points and talking points.</p>

<h2>Element 1: The Welcome</h2>
<p>The opening welcome sets the tone. It should:</p>
<ul>
<li>Welcome guests warmly and acknowledge the occasion</li>
<li>Briefly mention any housekeeping (where bathrooms are, phone etiquette)</li>
<li>Set the energy for the evening ahead</li>
<li>Transition smoothly into the first element (usually entrances)</li>
</ul>
<p>Keep it to 90 seconds. The room is waiting for the couple — don't make them wait too long.</p>

<h2>Element 2: Bridal Party Introductions</h2>
<p>For each member, you need: name, relationship to the couple, and one specific, warm detail that personalises the introduction. Generic ("the best man, John Smith") is forgettable. Specific ("the best man, John Smith — who's been the groom's best friend since Year 8 at Churchlands and who, I understand, is entirely responsible for the groom's obsession with camping trips that always end in disaster") is memorable.</p>
<p>Coordinate with the DJ on entry music and cue each person individually with a nod or signal.</p>

<h2>Element 3: Speech Introductions</h2>
<p>Each speaker deserves a genuine introduction — not just a name and title. Write 3–4 sentences that warm the audience up for the speaker: who they are, their relationship to the couple, and one specific, affectionate observation. End the introduction with a clear invitation to the stage.</p>

<h2>Element 4: Transition Announcements</h2>
<p>Between speeches, courses, and activities, the MC needs bridge language. These don't need to be scripted word-for-word, but note:</p>
<ul>
<li>What's coming next</li>
<li>Any instructions for guests (please take your seats, help yourselves at the bar)</li>
<li>Approximate timing if relevant</li>
</ul>

<h2>Element 5: Key Moments</h2>
<p>First dance, cake cutting, bouquet toss, and any surprises need specific notes:</p>
<ul>
<li>The cue to the DJ for the music</li>
<li>Any words to the guests (please join us on the dance floor, etc.)</li>
<li>Photography instructions if needed</li>
</ul>

<h2>Element 6: The Close</h2>
<p>The formal close of the reception — often after the last speech or before the dance floor opens. Thank the guests for being present, acknowledge the couple, and invite everyone to continue celebrating. Keep it warm, brief, and leave the room on a high note.</p>

<h2>Practical Script Format Tips</h2>
<ul>
<li>Use large font (14pt minimum) for easy reading at a podium</li>
<li>Print double-spaced so you can annotate on the night</li>
<li>Have a backup digital copy on your phone</li>
<li>Number each page clearly</li>
<li>Mark your cues to the DJ/band in a distinct colour</li>
</ul>
""" + CTA_BOX + "</div>",
    },
    {
        "slug": "blog-tips-choosing-corporate-mc-perth",
        "title": "Tips for Choosing a Corporate Event MC in Perth | The Perth MC",
        "h1": "Tips for Choosing a Corporate Event MC in Perth",
        "meta": "Corporate events have unique requirements. What to look for in a corporate MC — and the questions that reveal whether they've actually done this before.",
        "tag": "Corporate",
        "read_time": 5,
        "content": """<div class="blog-body">
<p>Choosing an MC for a corporate event requires different criteria than choosing a wedding MC. The stakes are different, the audience is different, and the skillset required is different. Here's what actually matters.</p>

<h2>Relevant Experience Over General Experience</h2>
<p>An MC who has hosted 200 weddings is not necessarily qualified to host your national conference. Ask specifically about corporate event experience — the types of events, the audience sizes, the industries they've worked in, and any events similar to yours.</p>
<p>Corporate hosting requires the ability to facilitate Q&amp;As, manage panels, introduce speakers professionally, and maintain audience engagement across a long day. These are different skills from wedding hosting, and they're built through specific experience.</p>

<h2>Brand Alignment</h2>
<p>Your MC represents your brand on the night. They need to understand your organisation's culture, your communication style, and the tone that's appropriate for your audience. A high-energy entertainer might work for a mining company's end-of-year celebration; they would be entirely wrong for a healthcare AGM.</p>
<p>When interviewing an MC, give them a brief description of your organisation and event, then ask how they would adapt their style. An MC who gives you a specific, thoughtful answer has done this before. One who says "I can do anything" probably hasn't.</p>

<h2>Facilitation Skills</h2>
<p>Many corporate events require more than announcements — they require genuine facilitation. Can your MC manage a live Q&amp;A? Can they hold a panel conversation that covers the content while keeping the audience engaged? Can they handle an audience member who derails the discussion? These are skills worth asking about explicitly.</p>

<h2>Preparation and Process</h2>
<ul>
<li>Do they ask for comprehensive speaker bios and verify pronunciation?</li>
<li>Do they request a briefing call with the event organiser?</li>
<li>Do they review and provide input on the run sheet?</li>
<li>Do they coordinate with AV and the venue team independently?</li>
</ul>
<p>A professional MC has a clear process. If they can't describe one, that's a red flag.</p>

<h2>What to Avoid</h2>
<ul>
<li>MCs whose main credential is being funny — humour is useful, but it's not the primary requirement</li>
<li>MCs who send you a generic quote without asking about your event</li>
<li>MCs who don't ask for speaker information until the week of the event</li>
<li>MCs who can't provide references from similar corporate events</li>
</ul>

<h2>The Reference Check</h2>
<p>Ask for two or three references from similar corporate events. Actually call them. Ask specifically: was the MC thoroughly prepared? Did they adapt when something went off-script? How did the audience respond? Would you hire them again? References from wedding clients are not useful for a corporate booking — ask for corporate references.</p>
""" + CTA_BOX + "</div>",
    },
    {
        "slug": "blog-how-to-handle-difficult-crowd-mc",
        "title": "How to Handle a Difficult Crowd as an MC | The Perth MC",
        "h1": "How to Handle a Difficult Crowd as an MC",
        "meta": "Every MC eventually faces the crowd that won't engage. Techniques for reading resistance, adjusting energy, and turning the room around.",
        "tag": "Craft",
        "read_time": 6,
        "content": """<div class="blog-body">
<p>Every MC, no matter how experienced, eventually faces the crowd that won't come with them. The table that talks through every announcement. The audience that responds to warmth with silence. The group that arrived tired, distracted, or simply resistant. Here's how professionals handle it.</p>

<h2>First: Diagnose Before You React</h2>
<p>Not all "difficult" crowds are the same. Before changing your approach, diagnose what's actually happening:</p>
<ul>
<li><strong>Tired crowd:</strong> A conference audience on day two after a big evening. Solution: high energy, shorter segments, more movement.</li>
<li><strong>Distracted crowd:</strong> People checking phones, side conversations running. Solution: direct address, a question that requires a response, something unexpected.</li>
<li><strong>Resistant crowd:</strong> An audience that didn't choose to be there, or who have grievances with the event itself. Solution: acknowledge the situation (carefully), reduce formality, build genuine connection before asking for anything.</li>
<li><strong>Diverse crowd:</strong> Age ranges, cultures, and shared contexts are too broad for one approach. Solution: find the universal — shared experience, common humanity, moments everyone can recognise.</li>
</ul>

<h2>Lower Your Energy When They're Tired</h2>
<p>Counter-intuitive but true: when a crowd is exhausted, matching their energy with high-volume enthusiasm makes the disconnect worse. Drop your register. Slow down. Speak to them conversationally rather than performatively. Meet them where they are, then gradually bring energy up. Never try to force energy into a room that has none left to give.</p>

<h2>Create Interaction</h2>
<p>The fastest way to engage a passive audience is to make them active. Ask a direct question that requires a show of hands. Ask someone in the room for a genuine opinion. Reference something specific about a person in the audience (with appropriate permission or prior knowledge). Interaction breaks the passive spectator mode and re-engages the room in seconds.</p>

<h2>Acknowledge Reality</h2>
<p>Sometimes the most powerful move is simply naming what's happening. "I know we've been here since 8 AM and it's now 4:30 — I promise we're nearly there." The acknowledgement builds trust. It tells the audience you see them, you're not going to pretend everything is fine, and you're on their side. That kind of honesty often produces more goodwill than any performance would.</p>

<h2>Reduce the Formal Program</h2>
<p>If you're losing a room, consider working with the event organiser to reduce or compress what's left of the formal program. Cutting a segment that no longer has audience buy-in is better than pushing through it at the cost of everyone's goodwill. Know what's non-negotiable and what can flex.</p>

<h2>Never Fight the Room</h2>
<p>The least effective response to a difficult crowd is to increase pressure — to speak louder, project more energy, or attempt to dominate the audience into engagement. This always backfires. Crowds can feel when a host is fighting them, and the resistance increases. Work with the room, not against it. Flexibility and genuine responsiveness are the marks of an experienced MC.</p>
""" + CTA_BOX + "</div>",
    },
    {
        "slug": "blog-black-tie-event-etiquette-mc",
        "title": "Black Tie Event Etiquette — What Your MC Needs to Know | The Perth MC",
        "h1": "Black Tie Event Etiquette — What Your MC Needs to Know",
        "meta": "Black tie events have protocols most MCs don't know. What distinguishes a polished formal event host from someone who just owns a suit.",
        "tag": "Events",
        "read_time": 5,
        "content": """<div class="blog-body">
<p>Black tie events operate by a set of unwritten rules that experienced event professionals absorb over time. For an MC, not knowing these rules is visible — and in a room full of formally dressed, discerning guests, that visibility comes at a cost.</p>

<h2>The Language of Formality</h2>
<p>Black tie events require a particular register of language — more formal than a cocktail party, more measured than a conference. This means:</p>
<ul>
<li>Referring to guests as "ladies and gentlemen" (or the modern "guests and distinguished visitors" if the event calls for it)</li>
<li>Using full titles for VIPs — "The Honourable," "Professor," "His Excellency" — and verifying their correct form of address in advance</li>
<li>Avoiding colloquialisms, casual language, and any humour that reads as low-register</li>
<li>Pacing speech more deliberately — black tie events move at a stately pace, not an energetic one</li>
</ul>

<h2>Table of Honour Protocol</h2>
<p>Black tie events usually have a top table or table of honour. The MC needs to know who's seated there, in what order of precedence, and whether any of them will be acknowledged individually during the evening. Precedence at formal events matters — acknowledging a mayor after a less senior official is a visible gaffe.</p>

<h2>The Welcome and Acknowledgements</h2>
<p>Formal black tie events typically require specific acknowledgements at the opening — distinguished guests, the event patron, the organisation's leadership. These should be scripted precisely, ordered by precedence, and delivered with appropriate gravity. Rushing through acknowledgements signals that you don't understand the significance of the occasion.</p>

<h2>Managing the Program with Formality</h2>
<p>Black tie events have a formal program that should be adhered to — deviations feel inappropriate in this context. If the program needs to flex, communicate changes quietly and privately to the relevant parties rather than announcing adjustments to the room. Maintaining the appearance of everything proceeding as planned is part of the MC's role.</p>

<h2>Dress and Presentation</h2>
<p>The MC at a black tie event should be in black tie unless the event organiser has specified otherwise. A well-fitted dinner suit, correctly styled, is non-negotiable. This is not the event for creative interpretation of the dress code. The MC's appearance sets a standard — dress to match or slightly below the event's most formally dressed attendees.</p>

<h2>The Quiet Authority of a Great Formal MC</h2>
<p>The best black tie MCs have a quality that's difficult to describe but instantly recognisable: quiet authority. They don't need to work hard to command the room's attention. Their presence and poise are sufficient. This comes from genuine confidence built on thorough preparation — knowing the program, knowing the people, and trusting that the evening is in good hands.</p>
""" + CTA_BOX + "</div>",
    },
    {
        "slug": "blog-how-to-plan-gala-dinner-perth",
        "title": "How to Plan a Gala Dinner in Perth | The Perth MC",
        "h1": "How to Plan a Gala Dinner in Perth",
        "meta": "A comprehensive guide to planning a gala dinner in Perth — venue, catering, program structure, entertainment, and MC briefing.",
        "tag": "Events",
        "read_time": 6,
        "content": """<div class="blog-body">
<p>A gala dinner is one of the most sophisticated events you can host — and one of the most complex to execute. Done well, it's the event people talk about all year. Done poorly, it's the event your guests politely describe as "quite good" while quietly wishing they'd left after entrée.</p>

<h2>Step 1: Define the Purpose</h2>
<p>Before any other decision is made, be clear on why you're hosting a gala. Is it:</p>
<ul>
<li>Fundraising for a cause?</li>
<li>Recognising industry achievement?</li>
<li>Celebrating an organisational milestone?</li>
<li>A client appreciation event?</li>
</ul>
<p>The purpose determines everything — the program structure, the tone, the entertainment, the MC brief, and the metrics by which you'll measure success.</p>

<h2>Step 2: Venue Selection</h2>
<p>Perth has excellent gala dinner venues across the city. Key considerations:</p>
<ul>
<li><strong>Capacity:</strong> Does the space seat your guest list comfortably in a banquet configuration with a dance floor?</li>
<li><strong>AV infrastructure:</strong> Is there a professional AV setup, including screens for presentations or auction items?</li>
<li><strong>Catering quality:</strong> Gala dinner catering is not the place to cut corners — the quality of the meal shapes the guests' overall impression of the event</li>
<li><strong>Acoustics:</strong> A room with poor acoustics makes every speech harder to follow and fatigues guests faster</li>
<li><strong>Parking and access:</strong> Particularly important for elderly or mobility-impaired guests at formal events</li>
</ul>

<h2>Step 3: Program Structure</h2>
<p>A typical gala dinner program runs:</p>
<ul>
<li>6:00–7:00 PM: Pre-dinner drinks and networking</li>
<li>7:00 PM: Guests seated, welcome address</li>
<li>7:15 PM: Entrée service</li>
<li>7:45 PM: Keynote speaker or first award category</li>
<li>8:00 PM: Main course service</li>
<li>8:30 PM: Awards presentation / main program content</li>
<li>9:30 PM: Dessert, entertainment, or auction</li>
<li>10:00 PM: Dancing / networking</li>
<li>11:30 PM: Close</li>
</ul>
<p>This is a template — your specific event will require adjustments. Build in buffer time around meal service and speeches.</p>

<h2>Step 4: Entertainment</h2>
<p>Entertainment at a gala dinner should complement, not compete with, the program. Live music during pre-dinner drinks and dinner is almost always appropriate. A performance element (band, singer, comedian) is best placed after the formal program so it doesn't disrupt the awards or keynote flow.</p>

<h2>Step 5: The MC Brief</h2>
<p>Brief your MC at least two weeks before the event with:</p>
<ul>
<li>The complete run sheet</li>
<li>Full details on every award category and recipient</li>
<li>Speaker bios and pronunciation guides</li>
<li>VIP and top table seating list</li>
<li>Auction or fundraising details if applicable</li>
<li>The tone and register you want for the event</li>
</ul>
<p>A well-briefed MC makes every part of the program flow better. An under-briefed MC is visible — and at a gala dinner, that visibility reflects on you as the organiser.</p>
""" + CTA_BOX + "</div>",
    },
    {
        "slug": "blog-mc-charity-auction-perth",
        "title": "MC for a Charity Auction in Perth — What to Expect | The Perth MC",
        "h1": "MC for a Charity Auction — What to Expect",
        "meta": "Charity auctions require a very specific MC skillset. What a great auction MC does — and the difference it makes to how much is raised.",
        "tag": "Events",
        "read_time": 5,
        "content": """<div class="blog-body">
<p>A charity auction is one of the most high-stakes moments in any fundraising event — and the MC's performance during the auction can meaningfully affect how much money is raised. Here's what to expect from a professional auction MC and how to set them up for success.</p>

<h2>The Two Roles of the Auction MC</h2>
<p>The MC in a charity auction serves two simultaneous functions: they're the emotional anchor of the room (building connection to the cause) and the commercial driver (creating urgency and momentum around bidding). Both must happen simultaneously, and the balance requires genuine skill.</p>
<p>An MC who's too commercially focused feels like a sales pitch. One who's too emotionally focused loses the bidding momentum. The best auction MCs move fluidly between both — building emotional context, then converting it into action.</p>

<h2>Live vs Silent Auction Hosting</h2>
<p><strong>Live auctions</strong> are run by the MC verbally — calling out lot items, managing bids from the room, building competition between bidders, and creating the sense of occasion around each lot. The MC needs energy, clarity, and the ability to manage the room during bidding without letting the pace drop.</p>
<p><strong>Silent auctions</strong> run themselves on paper or via auction apps, but the MC can meaningfully influence engagement by drawing attention to specific lots, announcing the close of bidding with urgency, and acknowledging generosity publicly.</p>

<h2>What a Great Live Auction MC Does</h2>
<ul>
<li>Introduces each lot with genuine enthusiasm and specific detail</li>
<li>Builds the emotional case for each item before stating the opening bid</li>
<li>Manages competitive bidding with energy without being auctioneer-style aggressive</li>
<li>Acknowledges generous bidders publicly (with permission) to encourage others</li>
<li>Keeps the pace moving — slow auctions lose momentum and money</li>
<li>Transitions between lots cleanly with brief cause reinforcement</li>
</ul>

<h2>How to Brief Your Auction MC</h2>
<ul>
<li>Provide detailed descriptions of every auction item — what it is, what it's worth, why it's desirable</li>
<li>Confirm the opening bid for each lot</li>
<li>Confirm whether there are any anonymous donors or VIP bidders who should or shouldn't be acknowledged</li>
<li>Discuss the cause framing — what's the most emotionally resonant story to tell around each item?</li>
<li>Agree on the bidding increment convention</li>
<li>Confirm who manages the bid cards/paddles and records winning bids</li>
</ul>

<h2>The Paddle Raise</h2>
<p>The paddle raise (also called a fund-a-need or direct ask) is often more effective than a traditional auction for charity events. The MC asks all guests who can contribute at a specific level to raise their paddle simultaneously — no competition, just collective generosity. Done well, this can raise significant funds in minutes. It requires a skilled MC who can create the right emotional moment and execute the ask without it feeling transactional.</p>
""" + CTA_BOX + "</div>",
    },
    {
        "slug": "blog-school-formal-mc-perth",
        "title": "School Formal MC Perth — What Makes a Great One | The Perth MC",
        "h1": "School Formal MC — What Makes a Great One",
        "meta": "School formals are high-stakes for students and organisers alike. What a great school formal MC brings to the night — and what to avoid.",
        "tag": "Events",
        "read_time": 5,
        "content": """<div class="blog-body">
<p>School formals occupy a unique place in the event hosting landscape. They're significant milestone events for students who've worked hard and waited long. They're logistically complex for teachers and organisers. And they require an MC who understands how to hold a room of teenagers — which is, frankly, a specific skill not every MC has.</p>

<h2>The Unique Challenge</h2>
<p>A school formal audience is unlike any corporate or wedding crowd. Year 12 students are:</p>
<ul>
<li>Highly attuned to authenticity — they detect performance immediately and respond with disengagement</li>
<li>More likely to talk among themselves than listen to a host they haven't bought into</li>
<li>Excited but also slightly overwhelmed — it's a night they've built up for months</li>
<li>Watching everything about how the night is hosted and drawing conclusions about what kind of event this is</li>
</ul>
<p>An MC who treats a school formal like a corporate conference will lose the room in the first five minutes. One who treats it like a comedy show will lose the teachers. The tone sits precisely between: energetic, genuine, and appropriate.</p>

<h2>What Works</h2>
<ul>
<li>Opening with high energy that acknowledges the significance of the night without being saccharine about it</li>
<li>Brief, punchy announcements — long speeches kill energy at formals</li>
<li>Humour that lands on the side of warmth rather than edge</li>
<li>Genuine interaction — asking the room questions, getting a response</li>
<li>King and Queen announcements handled with the right mix of celebration and dignity</li>
<li>Transition to dancing managed with momentum — the formal program should end when the room is ready to dance, not before</li>
</ul>

<h2>What to Avoid</h2>
<ul>
<li>References to being "young" or "this being the best years of your life" — students find this patronising</li>
<li>Humour that could embarrass specific students in the room</li>
<li>Dragging out the formal program when students are ready to dance</li>
<li>An MC who is visibly trying too hard to connect — teenagers can smell it immediately</li>
<li>Ignoring the teachers — acknowledging them (briefly) keeps the room balanced</li>
</ul>

<h2>Briefing the School Formal MC</h2>
<p>Give your MC:</p>
<ul>
<li>The complete run sheet with timing</li>
<li>Names of the King and Queen nominees and winner if pre-determined</li>
<li>Names of any students giving speeches or presentations</li>
<li>Names of teaching staff to be acknowledged</li>
<li>Any inside references or themes relevant to the year group (with appropriate vetting)</li>
<li>Clear guidance on tone and any content boundaries</li>
</ul>
<p>A good school formal MC will always ask for this information. One who shows up without requesting it hasn't done enough events to know what they need.</p>
""" + CTA_BOX + "</div>",
    },
    {
        "slug": "blog-how-to-choose-music-corporate-event-perth",
        "title": "How to Choose Music for Your Corporate Event Perth | The Perth MC",
        "h1": "How to Choose Music for Your Corporate Event Perth",
        "meta": "Music sets the atmosphere before a single word is spoken. A guide to music selection for corporate events — and how it works with your MC.",
        "tag": "Corporate",
        "read_time": 5,
        "content": """<div class="blog-body">
<p>Music at corporate events is more than background. It's atmosphere-setting, energy management, and brand communication all happening simultaneously — before anyone has said a word from the stage. Getting it right takes more thought than most event planners give it.</p>

<h2>The Three Phases of Corporate Event Music</h2>
<p><strong>Arrival and networking:</strong> Music should facilitate conversation — present enough to feel welcoming, quiet enough to talk over. Mid-tempo, familiar but not distracting. Volume should allow comfortable conversation at normal speaking level.</p>
<p><strong>During formal program:</strong> Usually no music, or very subtle background during meal service. Music during speeches or presentations competes for attention — avoid it.</p>
<p><strong>Post-program / dancing:</strong> If your event has a social component after the formal program, the music needs to build — starting where dinner background music left off and building toward something energetic over 30–45 minutes.</p>

<h2>Matching Music to Brand</h2>
<p>Your music choices signal something about your organisation. A tech company playing background jazz feels misaligned. A law firm playing EDM feels wrong. Think about what musical choices are consistent with your organisation's personality and how you want guests to feel about you.</p>
<p>This doesn't mean rigid genre conventions — it means thinking about music the way you'd think about any other brand touchpoint.</p>

<h2>Live vs Recorded Music</h2>
<p>Live music at corporate events almost always elevates the atmosphere. Even a simple solo acoustic guitar or piano during cocktail hour creates an impression that a Spotify playlist can't replicate. For larger budgets, a jazz trio, string quartet, or function band transforms the room.</p>
<p>If live music is not in the budget, invest in a good DJ rather than a playlist. A DJ can read the room and adjust in real time. A playlist cannot.</p>

<h2>How Your MC and DJ Work Together</h2>
<p>Your MC needs to coordinate closely with your DJ or band on musical cues. Key transition points that require precise coordination:</p>
<ul>
<li>When to cut music for the MC's welcome</li>
<li>Music during any video presentations or slides</li>
<li>Post-speech musical transition to resume dinner service</li>
<li>The handover from formal program to social/dancing portion</li>
</ul>
<p>Schedule a call between your MC and DJ before the event. If they've never spoken by the day itself, you're relying on improvised coordination for every one of these moments.</p>

<h2>Volume: The Most Common Mistake</h2>
<p>Background music that's too loud is the most common corporate event music mistake. Guests spend the evening straining to have conversations, leave feeling subtly exhausted, and the event is remembered as "a bit loud." Volume should be checked from multiple points in the room — not just near the speakers — and adjusted accordingly.</p>
""" + CTA_BOX + "</div>",
    },
    {
        "slug": "blog-smooth-wedding-reception-timeline",
        "title": "Tips for a Smooth Wedding Reception Timeline | The Perth MC",
        "h1": "Top Tips for a Smooth Wedding Reception Timeline",
        "meta": "Reception timelines go wrong for predictable reasons. A professional MC's guide to building a timeline that actually holds together on the night.",
        "tag": "Planning",
        "read_time": 6,
        "content": """<div class="blog-body">
<p>Wedding receptions run late for predictable, preventable reasons. After hosting hundreds of them, certain patterns emerge — and most of the timeline disasters I've seen were visible in the run sheet weeks before the day. Here's how to build a timeline that holds.</p>

<h2>The Most Common Causes of Timeline Collapse</h2>
<ul>
<li>Speeches scheduled back-to-back with no buffer between them</li>
<li>Assuming guests will move from cocktail hour to the dining room instantly</li>
<li>No time allocated for the couple to be photographed before entrée</li>
<li>Speeches allocated the same time they were promised rather than what they'll realistically take</li>
<li>No buffer between entrée service finishing and speeches starting</li>
<li>First dance placed immediately after speeches when people need to circulate</li>
</ul>

<h2>Build Buffers, Not Aspirations</h2>
<p>Your timeline should be built around what will realistically happen, not what you hope will happen. For every formal element, add 5–10 minutes of buffer. For meal service, add 15 minutes. For the transition from cocktail hour to seating, allow 10–15 minutes beyond what feels necessary.</p>
<p>A reception that runs slightly ahead of schedule feels relaxed. One that runs late feels chaotic — and late receptions are almost never recovered in the final hours.</p>

<h2>Speeches: The Biggest Variable</h2>
<p>Speeches are the element most likely to blow your timeline. Best man speeches run long. Fathers get emotional. Someone decides to add a sibling who wasn't on the list. Plan for reality:</p>
<ul>
<li>Allocate 1.5x the time each speaker has been asked to take</li>
<li>Brief speakers firmly on timing — "5 minutes" means 5 minutes</li>
<li>Give your MC permission to signal speakers at the 4-minute mark</li>
<li>Place the longest speeches (best man, father of the bride) earlier, so if they run, there's time to recover</li>
</ul>

<h2>Coordinate Speeches with Kitchen Service</h2>
<p>Nothing kills speech energy like cold food. Work with your venue to time speeches so they don't overlap with hot course service. The typical structure that works: entrée during cocktails or early seating, speeches between entrée and main, main during a break, dessert after speeches.</p>
<p>Confirm this structure with your venue coordinator and put it in your run sheet. Your MC will need to keep the speeches moving at pace to protect the kitchen's timing.</p>

<h2>Give the Couple Breathing Room</h2>
<p>Build two or three moments into the timeline specifically for the couple to not have a hosting obligation — short windows where they can be with their guests rather than being processed from one program element to the next. A 10-minute "wander the room" buffer before the cake cutting, or a brief break between speeches and dancing, preserves their ability to actually enjoy their wedding.</p>

<h2>Confirm the Timeline with Every Vendor</h2>
<p>Your MC, venue coordinator, caterer, DJ, photographer, and videographer should all be working from the same timeline at least a week before the wedding. Discrepancies found before the day are easily resolved. Discrepancies discovered at 7:30 PM are much harder to manage.</p>
""" + CTA_BOX + "</div>",
    },
    {
        "slug": "blog-how-to-introduce-speakers-corporate-event",
        "title": "How to Introduce Speakers at a Corporate Event | The Perth MC",
        "h1": "How to Introduce Speakers at a Corporate Event",
        "meta": "Speaker introductions are often the weakest part of corporate events. The formula for an introduction that gives your speaker the best possible start.",
        "tag": "Corporate",
        "read_time": 4,
        "content": """<div class="blog-body">
<p>Speaker introductions are consistently the most underprepared element of corporate events. The MC reads from a bio that's two years out of date, mispronounces the speaker's name, and delivers it in a flat monotone that leaves the speaker walking to the podium into silence. Every speaker deserves better. Here's the formula.</p>

<h2>The Purpose of an Introduction</h2>
<p>A good speaker introduction does three things:</p>
<ul>
<li>Establishes the speaker's credibility so the audience trusts what they're about to hear</li>
<li>Creates genuine anticipation — the audience should be leaning forward by the time the speaker takes the stage</li>
<li>Signals to the speaker that they're valued and well-prepared for</li>
</ul>
<p>An introduction that just reads a bio does none of these things effectively.</p>

<h2>The Formula: Context, Credibility, Curiosity</h2>
<p><strong>Context (1–2 sentences):</strong> Frame why this speaker is relevant right now — connect their expertise to what the event is about or what's been discussed. "We've been talking this morning about the future of our industry — and our next speaker has spent the last decade building the organisation that's most directly shaping what that future looks like."</p>
<p><strong>Credibility (2–3 sentences):</strong> The headline facts that establish their authority. Not a full CV recitation — three specific achievements or roles that are most relevant to this audience, this day. Focus on what this audience will find impressive, not everything impressive about the speaker.</p>
<p><strong>Curiosity (1 sentence):</strong> End the introduction with something that makes the audience want to hear more. A question the speaker is about to answer. A provocative observation. A result that demands explanation. "Please join me in welcoming [Name]."</p>

<h2>Practical Requirements</h2>
<ul>
<li>Verify the pronunciation of the speaker's name before you write your introduction — not in the moment</li>
<li>Confirm the introduction with the speaker or their assistant — they may have updated credentials or a preference for how they're introduced</li>
<li>Keep it to 60–90 seconds — longer introductions are self-indulgent and undermine the speaker's opening</li>
<li>Make eye contact with the audience, not your notes, for the final sentence and the call to applause</li>
</ul>

<h2>The Handover</h2>
<p>End your introduction with a clear, warm invitation — not "please welcome" in a flat voice, but a genuine call to applause that gives the speaker the start they deserve. Stand at the side of the stage, wait for the speaker to reach the podium, then step aside. The handover is the last impression your introduction makes — execute it cleanly.</p>
""" + CTA_BOX + "</div>",
    },
]


def build_page(article):
    date_str = "May 2026"
    date_iso = "2026-05-01"
    header = HEADER.format(
        meta=article["meta"],
        title=article["title"],
        slug=article["slug"],
        h1=article["h1"],
        date_str=date_str,
        read_time=article["read_time"],
        tag=article["tag"],
    )
    footer = FOOTER.format(
        h1=article["h1"],
        meta=article["meta"],
        date_iso=date_iso,
    )
    return header + article["content"] + footer


def main():
    for article in ARTICLES:
        html = build_page(article)
        out_path = os.path.join(BASE_DIR, f"{article['slug']}.html")
        with open(out_path, "w") as f:
            f.write(html)
        print(f"Generated: {article['slug']}.html")
    print(f"\nDone — {len(ARTICLES)} blog posts generated.")


if __name__ == "__main__":
    main()
