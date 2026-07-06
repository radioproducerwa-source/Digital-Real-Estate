#!/usr/bin/env python3
"""Generate 30 new draft blog posts for Perth Content and append them to queue.json."""

import json, os
from datetime import date, timedelta

DRAFTS_DIR = "/home/user/Digital-Real-Estate/perthcontent/drafts"
QUEUE_PATH  = "/home/user/Digital-Real-Estate/perthcontent/drafts/queue.json"

def make_html(slug, title, description, tag, date_display, date_iso, read_time, hero_sub, body):
    f = slug
    jsonld = json.dumps({
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "description": description,
        "datePublished": date_iso,
        "author": {"@type": "Organization", "name": "Perth Content"},
        "publisher": {"@type": "Organization", "name": "Perth Content", "url": "https://perthcontent.com"}
    }, ensure_ascii=False, separators=(',', ':'))
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="{description}" /><meta name="robots" content="index, follow" />
  <title>{title} | Perth Content</title>
  <link rel="canonical" href="https://perthcontent.com/{slug}.html" />
  <meta property="og:title" content="{title}" /><meta property="og:description" content="{description}" />
  <meta property="og:url" content="https://perthcontent.com/{slug}.html" /><meta property="og:type" content="article" />
  <link rel="preconnect" href="https://fonts.googleapis.com" /><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="css/style.css" />
  <script type="application/ld+json">{jsonld}</script>
</head>
<body>
<header class="site-header"><div class="container header-inner">
  <a href="index.html" class="logo">Perth<span>Content</span></a>
  <nav class="main-nav" id="main-nav">
    <a href="index.html">Home</a>
    <div class="dropdown"><button class="dropdown-btn">Services &#9660;</button>
      <div class="dropdown-menu">
        <a href="corporate-video-perth.html">Corporate Video</a><a href="real-estate-video-perth.html">Real Estate Video</a><a href="social-media-video-perth.html">Social Media Video</a><a href="instagram-reels-editing-perth.html">Instagram Reels</a><a href="youtube-video-editing-perth.html">YouTube Editing</a><a href="event-highlight-video-perth.html">Event Highlights</a><a href="explainer-video-perth.html">Explainer Video</a><a href="training-video-perth.html">Training Video</a><a href="drone-video-editing-perth.html">Drone Video</a><a href="restaurant-hospitality-video-perth.html">Restaurant &amp; Hospitality</a><a href="wedding-videography-perth.html">Wedding Video</a><a href="product-video-perth.html">Product Video</a><a href="promotional-video-perth.html">Promotional Video</a><a href="linkedin-video-perth.html">LinkedIn Video</a><a href="startup-video-perth.html">Startup Video</a><a href="tiktok-video-editing-perth.html">TikTok Editing</a><a href="conference-seminar-video-perth.html">Conference &amp; Seminar</a><a href="fitness-wellness-video-perth.html">Fitness &amp; Wellness</a><a href="testimonial-video-perth.html">Testimonial Video</a><a href="annual-report-video-perth.html">Annual Report Video</a>
      </div>
    </div>
    <a href="about.html">About</a><a href="portfolio.html">Portfolio</a><a href="blog.html" class="active">Blog</a>
    <a href="contact.html" class="btn btn-primary">Get a Quote</a>
  </nav>
  <div class="header-right"><button class="hamburger" id="hamburger" aria-label="Open menu" aria-expanded="false">&#9776;</button></div>
</div></header>
<section class="page-hero"><div class="container">
  <div class="breadcrumb"><a href="index.html">Home</a> &rsaquo; <a href="blog.html">Blog</a> &rsaquo; {tag}</div>
  <h1>{title}</h1><p>{hero_sub}</p>
</div></section>
<section class="blog-post"><div class="container blog-post-layout">
  <article class="blog-post-content">
    <div class="post-meta"><span>&#128197; {date_display}</span><span>&#127991; {tag}</span><span>&#9200; {read_time} min read</span></div>
    {body}
  </article>
  <aside class="post-sidebar">
    <div class="post-sidebar-card"><h4>Get a Free Quote</h4>
      <form action="https://formspree.io/f/mzdodayb" method="POST" data-formspree data-success-id="{f}-ss">
        <div class="form-row">
          <div><label for="{f}-n">Name</label><input id="{f}-n" type="text" name="name" placeholder="Your name" required /></div>
          <div><label for="{f}-e">Email</label><input id="{f}-e" type="email" name="email" placeholder="Your email" required /></div>
          <div><label for="{f}-s">Service</label>
            <select id="{f}-s" name="service"><option value="">Select&#8230;</option><option>Corporate Video</option><option>Real Estate Video</option><option>Social Media Content</option><option>Explainer Video</option><option>Wedding &amp; Event</option><option>Other</option></select>
          </div>
          <button type="submit" class="btn btn-primary">Get Quote</button>
        </div>
      </form>
      <div id="{f}-ss" hidden style="display:none;" class="form-success">&#10003; We&#39;ll be in touch shortly!</div>
    </div>
    <div class="post-sidebar-card"><h4>Popular Services</h4><ul>
      <li><a href="corporate-video-perth.html">Corporate Video Perth</a></li>
      <li><a href="real-estate-video-perth.html">Real Estate Video Perth</a></li>
      <li><a href="social-media-video-perth.html">Social Media Video Perth</a></li>
      <li><a href="explainer-video-perth.html">Explainer Video Perth</a></li>
      <li><a href="drone-video-editing-perth.html">Drone Video Editing Perth</a></li>
    </ul></div>
  </aside>
</div></section>
<section class="cta-section"><div class="container">
  <h2>Ready to Create Stunning Video Content?</h2>
  <p>Get a free quote from Perth Content &mdash; we respond within 2 business hours.</p>
  <div class="cta-btns"><a href="contact.html" class="btn btn-amber btn-lg">Get a Free Quote</a><a href="services.html" class="btn btn-outline-white">View Our Services</a></div>
</div></section>
<footer class="site-footer"><div class="container"><div class="footer-grid">
  <div class="footer-brand"><a href="index.html" class="logo">Perth<span>Content</span></a><p>Perth&#39;s video content marketplace &#8212; connecting businesses with expert editors and producers.</p></div>
  <div class="footer-col"><h4>Top Services</h4><a href="corporate-video-perth.html">Corporate Video</a><a href="real-estate-video-perth.html">Real Estate Video</a><a href="social-media-video-perth.html">Social Media Video</a><a href="explainer-video-perth.html">Explainer Video</a><a href="wedding-videography-perth.html">Wedding Video</a></div>
  <div class="footer-col"><h4>Company</h4><a href="about.html">About Us</a><a href="portfolio.html">Portfolio</a><a href="blog.html">Blog</a><a href="contact.html">Contact</a></div>
  <div class="footer-col"><h4>More Services</h4><a href="drone-video-editing-perth.html">Drone Video</a><a href="instagram-reels-editing-perth.html">Instagram Reels</a><a href="tiktok-video-editing-perth.html">TikTok Editing</a><a href="testimonial-video-perth.html">Testimonial Video</a><a href="event-highlight-video-perth.html">Event Highlights</a></div>
</div>
<div class="footer-bottom"><p>&copy; <span id="year"></span> Perth Content. All rights reserved.</p><p>Serving Perth, WA &#8212; Professional Video Editing &amp; Production</p></div>
</div></footer>
<script src="js/main.js"></script>
</body>
</html>"""


# ── Post definitions ───────────────────────────────────────────────────────────
# Dates: 25 existing queued posts publish weekly from 2026-08-31 → last on 2027-02-15
# New batch starts 2027-02-22, one per week.
START = date(2027, 2, 22)

POSTS = [

# 1
dict(
slug="blog-video-marketing-perth-real-estate-agents",
title="Video Marketing for Perth Real Estate Agents — Beyond the Property Tour",
description="Property tour videos are just the start. Perth real estate agents using agent profile videos, suburb stories, and sold-result reels are winning more listings and more buyers.",
tag="Industry",
read_time=5,
excerpt="Property tour videos are just the start. Perth real estate agents using agent profile videos, suburb highlight reels, and client result videos are winning more listings — here is how.",
hero_sub="Property tour videos are table stakes. The agents pulling ahead in Perth are using video across every stage of the client journey — here is the playbook.",
body="""<p>Most Perth real estate agents have a property tour video or two. But the agencies consistently winning more listings are doing something different: they are using video at every stage of the client relationship, not just to sell individual properties.</p>

<h2>Agent Profile Videos</h2>
<p>Before a vendor lists with you, they Google you. An agent profile video on your website and LinkedIn profile does what a headshot never can: it conveys energy, communication style, and trustworthiness. A 60-90 second video introducing who you are, what suburbs you specialise in, and what your clients say about you will convert more profile visitors into appraisal requests than any static bio.</p>

<h2>Suburb Spotlight Videos</h2>
<p>Buyers researching Perth suburbs are hungry for local knowledge. A short video walking through a suburb — the cafe strips, school zones, transport links, lifestyle feel — positions you as the local expert before you have even spoken to them. These videos rank well on YouTube for searches like "living in [suburb] Perth" and drive warm inbound leads.</p>

<h2>Sold Result Videos</h2>
<p>After a successful sale, capture a brief testimonial from your vendor. Sixty seconds of a happy client explaining what it was like to work with you is worth more than any award or accolade on your profile. These clips perform strongly on Facebook and Instagram, where social proof drives action.</p>

<h2>Market Update Videos</h2>
<p>Monthly or quarterly market update videos — two to three minutes covering local clearance rates, days on market, and price trends — build long-term authority. Agents who post these consistently become the go-to resource for Perth property owners in their patch, months before those owners are ready to sell.</p>

<h2>Open Home Teasers</h2>
<p>A 15-30 second Reel posted 48 hours before an open home — showing the standout feature of the property — consistently drives higher attendance than static listing photos alone. Keep it punchy: one striking visual, the key selling point, and the open home time.</p>

<h2>Production Tips for Agents</h2>
<ul>
  <li><strong>Consistency beats perfection:</strong> A good video posted regularly outperforms a great video posted once a year.</li>
  <li><strong>Natural light is your friend:</strong> Film agent intro videos near a window rather than in a dim office.</li>
  <li><strong>Captions on every social video:</strong> Most viewers watch without sound — captions ensure your message lands.</li>
  <li><strong>Keep a video library:</strong> Testimonial clips, suburb videos, and market updates are evergreen assets. Build them incrementally.</li>
</ul>

<p>Perth Content works with real estate agencies to build sustainable video libraries. <a href="contact.html">Talk to us about a content package.</a></p>"""
),

# 2
dict(
slug="blog-how-to-create-video-content-calendar-perth",
title="How to Create a Video Content Calendar for Your Perth Business",
description="A video content calendar stops the feast-and-famine cycle of posting. Here is how Perth businesses can plan, batch-film, and schedule video content that runs consistently all year.",
tag="Strategy",
read_time=6,
excerpt="A video content calendar stops the feast-and-famine cycle. Here is how Perth businesses can plan, batch-film, and schedule video content that stays consistent all year.",
hero_sub="Without a content calendar, video marketing becomes reactive and inconsistent. Here is how to build a system that keeps your Perth business publishing every week without the scramble.",
body="""<p>Most Perth businesses approach video content the same way they approach going to the gym: with great intentions that fade within a few weeks. The fix is not more motivation — it is a system. A video content calendar transforms video from a one-off project into a predictable pipeline.</p>

<h2>Start With Your Business Goals</h2>
<p>Your content calendar should map to real business outcomes. Ask: what do we want video to do for us this quarter? Common goals include generating enquiries, building brand awareness, nurturing existing clients, or supporting a product launch. Each goal points to a different content type.</p>

<h2>Map Content Types to the Buyer Journey</h2>
<ul>
  <li><strong>Awareness (top of funnel):</strong> Educational content, how-to videos, industry tips — designed to reach people who do not yet know you exist.</li>
  <li><strong>Consideration (mid funnel):</strong> Case studies, behind-the-scenes, explainer videos — for people evaluating whether to work with you.</li>
  <li><strong>Decision (bottom of funnel):</strong> Testimonials, process walkthroughs, FAQ videos — for people close to committing.</li>
</ul>
<p>A healthy calendar includes content across all three stages, not just promotional posts.</p>

<h2>Plan in Quarters, Batch in Days</h2>
<p>Map out a full quarter of content at the start of each quarter — 12-13 posts if you publish weekly. Once you have the topics, group similar shoots together. A single half-day filming session with good preparation can produce 4-6 pieces of content. This is far more efficient than filming one video at a time.</p>

<h2>Your Calendar Template</h2>
<p>Each entry in your calendar should capture:</p>
<ol>
  <li>Publish date</li>
  <li>Topic / title</li>
  <li>Platform (Instagram, YouTube, LinkedIn, website)</li>
  <li>Format (talking head, b-roll montage, screen record, animation)</li>
  <li>Call to action</li>
  <li>Status (idea → scripted → filmed → edited → scheduled → published)</li>
</ol>
<p>A simple Google Sheet works well for this. Keep it visible to anyone involved in content production.</p>

<h2>Seasonal Hooks for Perth Businesses</h2>
<p>Perth's calendar has natural content pegs: summer entertaining (December), back to school (January/February), EOFY (June), and Fringe World (February). Build these into your calendar in advance so you are not scrambling for relevance at the last minute.</p>

<h2>When to Bring in a Video Production Partner</h2>
<p>The calendar discipline is yours to own, but production quality matters for your highest-stakes content. Plan which videos in your calendar need professional production versus what you can film on your phone. A hybrid approach — professional quarterly hero videos plus regular self-filmed social content — works well for most Perth businesses.</p>

<p>Perth Content can help you plan and produce your quarterly video content. <a href="contact.html">Book a strategy call.</a></p>"""
),

# 3
dict(
slug="blog-gym-fitness-video-marketing-perth",
title="Video Marketing for Perth Gyms and Personal Trainers — What Actually Works",
description="Perth gyms and PTs using video are consistently filling classes and growing client rosters. Here is the playbook: facility tours, transformation stories, class highlights, and social content.",
tag="Industry",
read_time=5,
excerpt="Perth gyms and personal trainers using video are filling classes and growing rosters faster. Here is the content playbook: facility tours, transformation content, class highlights, and social video.",
hero_sub="The Perth fitness industry is competitive. Video is the single most effective way to show prospective members what your gym or training style feels like before they walk through the door.",
body="""<p>Fitness is one of the most visual industries in the world, yet many Perth gyms and personal trainers are still relying on static Instagram grids and word-of-mouth referrals. Video changes the game — it lets prospects feel the energy of your space, your coaching style, and your community before they commit.</p>

<h2>Facility Tour Videos</h2>
<p>A well-produced 90-second facility tour — showing your equipment, space, and atmosphere — is often the highest-converting piece of content on a gym's website. Film it when the gym is busy and energetic. Show the things prospective members actually care about: the equipment quality, cleanliness, locker rooms, and the vibe of people training. Keep it fast-paced with upbeat music.</p>

<h2>Class and Session Highlight Reels</h2>
<p>Short clips (30-60 seconds) from group fitness classes, personal training sessions, or HIIT circuits perform strongly on Instagram and Facebook. These show prospective members exactly what a session looks like and feel like. Film these regularly — they are the most shareable content in the fitness niche.</p>

<h2>Personal Trainer Introduction Videos</h2>
<p>If you have multiple trainers, an individual introduction video for each coach on your website and Instagram profile dramatically improves the sign-up rate from people who are choosing a PT. Cover their specialisation, training philosophy, and what their sessions involve. Sixty to ninety seconds is ideal.</p>

<h2>Client Transformation and Testimonial Content</h2>
<p>Transformation stories are among the most powerful content in the fitness industry, but they require client consent and careful execution. A 2-3 minute video following a client's journey — where they started, what they worked on, and how they feel now — builds deep trust. Avoid before-and-after framing that focuses purely on appearance; focus on fitness milestones, energy levels, and confidence.</p>

<h2>Educational Short-Form for Instagram and TikTok</h2>
<p>Quick technique tips, exercise substitutions, nutrition basics, and training myths are consistently high-performing formats on Reels and TikTok. This content positions your trainers as authorities, builds a following beyond your existing client base, and drives organic enquiries. Aim for one educational short-form video per week.</p>

<h2>Seasonal Campaigns</h2>
<p>Perth's fitness market has clear seasonal peaks: January (New Year resolutions), pre-winter (May), and the pre-summer push (September/October). Plan dedicated video campaigns around these windows — offer a free trial, a challenge, or a new program — and use video to promote it across social and email.</p>

<p>Perth Content helps fitness businesses produce ongoing social video content. <a href="contact.html">Get a quote.</a></p>"""
),

# 4
dict(
slug="blog-dental-medical-practice-video-perth",
title="Video Marketing for Perth Dental and Medical Practices — Building Trust Before the Appointment",
description="Perth dental and medical practices using video reduce no-show rates, attract better-fit patients, and build the trust that keeps patients returning. Here is how to do it compliantly.",
tag="Industry",
read_time=5,
excerpt="Video helps Perth dental and medical practices reduce patient anxiety, increase bookings, and build lasting trust. Here is a guide to what to produce and how to do it compliantly.",
hero_sub="Healthcare is one of the highest-trust industries. Video bridges the gap between a Google search and a first appointment — here is how Perth practices are using it effectively.",
body="""<p>For many Perth patients, choosing a new dentist, GP, or specialist is an anxiety-laden decision. They are searching not just for competence but for comfort — a sense that the practice is welcoming, professional, and right for them. Video addresses this better than any other medium.</p>

<h2>Practice Tour Videos</h2>
<p>A 60-90 second practice tour — reception, consultation rooms, equipment — significantly reduces first-visit anxiety. Show the waiting room, the friendliness of your front desk team, the cleanliness of the clinical spaces. This video belongs on your homepage, Google Business profile, and new patient booking confirmation emails.</p>

<h2>Meet the Team Videos</h2>
<p>A short video introduction for each practitioner (30-60 seconds) covering their background, special interests, and communication style helps patients choose a doctor or dentist they feel comfortable with. This is especially valuable for practices with multiple providers.</p>

<h2>Patient Education Explainers</h2>
<p>Short animated or talking-head videos explaining common procedures — a dental crown, a skin check, a blood test — reduce pre-appointment anxiety and cut down the time practitioners spend on explanations during the consultation. Host these on your website and YouTube channel, and link to them in appointment confirmation emails.</p>

<h2>FAQ Videos</h2>
<p>Every practice fields the same questions repeatedly. Record short answers to your top 10 patient questions and embed them on your FAQ page. This improves patient preparedness and reduces time spent on phone calls answering routine enquiries.</p>

<h2>Compliance Considerations</h2>
<p>Healthcare video in Australia must comply with AHPRA advertising guidelines. Key rules to observe:</p>
<ul>
  <li>Do not use patient testimonials that make claims about clinical outcomes</li>
  <li>Avoid before-and-after imagery in most clinical contexts</li>
  <li>All claims must be substantiated and not create unrealistic expectations</li>
  <li>Obtain written consent for any patient-facing video featuring identifiable patients</li>
</ul>
<p>Educational content, practice tours, and team introductions are the safest and most effective formats for healthcare marketing video.</p>

<h2>Where to Use Healthcare Video</h2>
<ul>
  <li>Homepage hero video</li>
  <li>Google Business Profile (increases profile views significantly)</li>
  <li>New patient confirmation emails</li>
  <li>Waiting room screens (loop practice and education videos)</li>
  <li>YouTube (patient education content ranks for long-tail health searches)</li>
</ul>

<p>Perth Content produces healthcare video with sensitivity to AHPRA guidelines. <a href="contact.html">Talk to us about your practice.</a></p>"""
),

# 5
dict(
slug="blog-how-to-film-with-iphone-business-perth",
title="How to Film Professional-Quality Video on Your iPhone for Your Perth Business",
description="The latest iPhones shoot cinema-quality footage. With the right settings, accessories, and techniques, Perth business owners can produce compelling video without hiring a crew every time.",
tag="Production",
read_time=6,
excerpt="Modern iPhones shoot genuinely professional video. With the right settings, a couple of accessories, and good technique, Perth businesses can produce compelling content without a crew every time.",
hero_sub="You do not always need a full crew to create great video. With the right setup, your iPhone can produce content that looks polished, performs well on social, and builds your brand.",
body="""<p>The gap between professional camera footage and iPhone footage has narrowed dramatically. The iPhone 15 Pro can shoot ProRes video at 4K 60fps — the same format used by professional cinematographers. The limiting factor for most Perth business owners is not the hardware; it is knowing how to use it.</p>

<h2>Camera Settings to Use</h2>
<ul>
  <li><strong>ProRes (iPhone 15 Pro and above):</strong> For content that will be professionally edited, ProRes gives editors maximum flexibility in colour grading. Note: ProRes files are large — allow 6GB+ per hour of footage.</li>
  <li><strong>4K 30fps:</strong> The best all-round setting for most business content. Clean, high-resolution, manageable file sizes.</li>
  <li><strong>Lock focus and exposure:</strong> Tap and hold on your subject to lock AE/AF before recording. This prevents the camera from hunting focus mid-shot — a tell-tale sign of amateur footage.</li>
  <li><strong>Turn off digital zoom:</strong> Move closer to your subject instead. Optical zoom on the telephoto lens is fine; digital zoom degrades quality noticeably.</li>
  <li><strong>Cinematic mode:</strong> Useful for hero shots and interviews — it mimics shallow depth of field. However, it is harder for editors to work with, so check with your post-production team first.</li>
</ul>

<h2>The Single Biggest Upgrade: Audio</h2>
<p>Poor audio will undermine even the best-looking iPhone footage. The built-in iPhone microphone picks up room noise, air conditioning, and background sound. A wireless lavalier microphone — the Rode Wireless GO II is the industry favourite at around $400 — clips to your subject's collar and delivers broadcast-quality audio directly to your iPhone. This one accessory makes more difference than any other.</p>

<h2>Lighting for Business Video</h2>
<p>Natural light is your best and cheapest option. Position your subject facing a large window (not with their back to it). For indoor shoots without good natural light, a portable LED panel ($60-150 on Amazon) gives you a reliable key light. Avoid mixing natural and artificial light sources as it creates awkward colour temperature mismatches.</p>

<h2>Stability</h2>
<p>Shaky footage is the clearest signal of unprofessional production. A phone tripod ($30-60) eliminates this completely for static shots. For moving shots, a smartphone gimbal (DJI OM 6, around $180) delivers cinema-smooth tracking shots that look genuinely impressive.</p>

<h2>When to Still Hire a Professional</h2>
<p>iPhone filming is appropriate for regular social content, quick updates, behind-the-scenes, and staff introductions. But for your homepage hero video, major product launches, or anything appearing in paid advertising, professional production is worth the investment — the gap in quality shows at scale.</p>

<p>Perth Content offers production services across all budgets. <a href="contact.html">Talk to us about what you need.</a></p>"""
),

# 6
dict(
slug="blog-staff-introduction-videos-perth-businesses",
title="Staff Introduction Videos — Why Perth Businesses Should Put Their Team on Camera",
description="Staff introduction videos humanise your Perth business, build client trust before the first meeting, and improve retention by making employees feel valued. Here is how to produce them.",
tag="Strategy",
read_time=5,
excerpt="Staff introduction videos humanise your Perth business and build trust before the first meeting. Here is why they work and how to produce them without putting your team through an awkward ordeal.",
hero_sub="Your team is one of your greatest competitive advantages. Staff introduction videos let prospective clients meet your people before the first call — here is how to make them work.",
body="""<p>People buy from people. Yet most Perth business websites present teams as a row of headshots and job titles. A staff introduction video transforms this — it lets prospective clients assess whether your team's communication style, expertise, and personality are the right fit before they pick up the phone.</p>

<h2>Why They Work</h2>
<p>Research consistently shows that video on professional profiles increases contact rates. On LinkedIn, a profile with a video introduction receives significantly more connection requests and messages than one without. On a business website, team pages with video bios have higher engagement and lower bounce rates than static pages. The mechanism is simple: trust is built faster through video than through text.</p>

<h2>What to Include in Each Video</h2>
<p>Keep each staff introduction to 45-90 seconds. Cover:</p>
<ul>
  <li>Name and role</li>
  <li>Years of experience or background</li>
  <li>What they specialise in or what they enjoy most about their work</li>
  <li>One personal detail (hobby, local connection, or fun fact) to make them memorable</li>
  <li>A brief invitation to get in touch or work together</li>
</ul>
<p>Avoid reading from a script. Have each team member speak to a colleague standing just off-camera — this produces a more natural eyeline and genuine delivery.</p>

<h2>Dealing with Camera-Shy Team Members</h2>
<p>Most people are uncomfortable on camera until they have done it once or twice. A few techniques help:</p>
<ul>
  <li>Let them see a playback immediately — most people are harder on themselves than the footage warrants</li>
  <li>Do multiple takes without pressure — assure them you will use the best one</li>
  <li>Ask questions rather than asking them to perform — conversation is more natural than recitation</li>
  <li>Film in a familiar, comfortable location (their office, at their desk) rather than a formal set</li>
</ul>

<h2>Where to Use Staff Introduction Videos</h2>
<ul>
  <li>Team page on your website</li>
  <li>Individual LinkedIn profiles</li>
  <li>Email signature (linked thumbnail)</li>
  <li>New client welcome sequences</li>
  <li>Job advertisements (to show culture to prospective hires)</li>
</ul>

<h2>Production Tips</h2>
<p>Film all team introductions in the same session for visual consistency — same background, same lighting setup. This gives your team page a cohesive, professional feel rather than a patchwork of different video styles filmed over time.</p>

<p>Perth Content offers team day packages — we come to your office and film your full team in one session. <a href="contact.html">Ask us about pricing.</a></p>"""
),

# 7
dict(
slug="blog-video-for-perth-recruitment-employer-branding",
title="Using Video for Recruitment and Employer Branding in Perth",
description="Perth businesses using employer branding video are attracting better candidates and reducing time-to-hire. Here is how to create day-in-the-life, culture, and employee story videos.",
tag="Strategy",
read_time=5,
excerpt="Perth businesses using employer branding video are attracting better candidates and reducing time-to-hire. Here is how to create culture videos and employee stories that pull the right people in.",
hero_sub="The best candidates have options. Employer branding video shows prospective hires who you really are as a company — before they apply. Here is how Perth businesses are using it.",
body="""<p>In Perth's tight labour market, attracting quality candidates is as competitive as attracting clients. Employer branding video gives candidates a genuine sense of your workplace culture, team, and values before they apply — filtering for people who will genuinely thrive in your environment, and reducing costly mis-hires.</p>

<h2>Culture Videos</h2>
<p>A culture video (2-3 minutes) captures the feel of your workplace: the team dynamic, how you celebrate wins, the physical environment, and the values that guide how you work. These are not corporate polished productions — authenticity outperforms production value here. A genuine laugh, a real conversation, or a team lunch will convey more than a scripted "we are a family" voiceover.</p>

<h2>Day-in-the-Life Videos</h2>
<p>Short-form day-in-the-life videos following a specific role for a day — filmed POV style or as a quick montage — consistently perform well on LinkedIn and Instagram. They answer the question every candidate has: "What would my day actually look like?" These are especially effective for roles that are hard to explain in a job ad (field technicians, creative roles, complex project management roles).</p>

<h2>Employee Testimonial Videos</h2>
<p>Ask three to five current employees to speak on camera for 60-90 seconds about why they joined, what they enjoy, and what they have learned. These carry more credibility than anything a hiring manager says about the workplace. Post them on your careers page, share them when advertising specific roles, and add them to your LinkedIn company page.</p>

<h2>Where to Use Recruitment Video</h2>
<ul>
  <li><strong>SEEK listings:</strong> SEEK allows video in job advertisements — listings with video receive higher application rates.</li>
  <li><strong>LinkedIn:</strong> Post culture clips when you open a role — the organic reach of video on LinkedIn means your network amplifies your job ad for free.</li>
  <li><strong>Careers page:</strong> A dedicated careers video on your website separates you from competitors who have nothing.</li>
  <li><strong>Interview process:</strong> Send a culture video to candidates who progress to interview — it sets context and reduces no-shows.</li>
</ul>

<h2>Production Approach</h2>
<p>Employer branding video does not need to be expensive. A half-day shoot with a professional videographer, capturing candid team moments and scripted employee testimonials, can produce enough content for 6-12 months of recruitment marketing. The investment is small relative to even one bad hire.</p>

<p>Perth Content produces employer branding video packages. <a href="contact.html">Talk to us about your hiring goals.</a></p>"""
),

# 8
dict(
slug="blog-childcare-education-video-marketing-perth",
title="Video Marketing for Perth Childcare Centres and Educational Institutions",
description="Perth childcare centres and schools using video are filling enrolments faster and keeping families better informed. Here is how to use video for tours, parent reassurance, and event highlights.",
tag="Industry",
read_time=5,
excerpt="Perth childcare centres and schools using video are filling enrolments faster. Here is how to use virtual tours, parent reassurance content, and event highlights to connect with your community.",
hero_sub="Choosing a childcare centre or school is one of the most emotionally significant decisions a family makes. Video lets you show — not just tell — why your environment is the right one.",
body="""<p>When Perth families research childcare options or consider a school change, they are looking for reassurance above everything else. Video gives them something no brochure can: a window into the daily experience of the children in your care.</p>

<h2>Facility Tour Videos</h2>
<p>A warm, well-lit facility tour (2-3 minutes) showing your classrooms, outdoor spaces, resources, and daily routines is the single most effective enrolment tool a childcare centre or school can produce. Walk through the spaces during typical activity. Show the interactions between educators and children (with appropriate consent). Narrate what makes your environment unique.</p>

<h2>Director or Principal Introduction</h2>
<p>A personal 90-second video from the Centre Director or Principal — speaking directly to prospective families — dramatically improves the conversion rate from enquiry to tour. Families are not just choosing a facility; they are choosing leadership. A face and a voice builds trust that text bio never can.</p>

<h2>Parent Reassurance Content</h2>
<p>Short videos addressing common parent concerns — "What does a typical day look like?", "How do you handle separation anxiety?", "What is your approach to learning?" — reduce the number of questions families ask before enrolling and increase conversion rates from tour to enrolment.</p>

<h2>Event Highlights</h2>
<p>End-of-year concerts, sports days, excursions, and graduation ceremonies are moments families treasure. A professional highlight reel (3-5 minutes) of these events serves double duty: it is a gift to current families, and a compelling piece of content for prospective families who want to see your community in action.</p>

<h2>Safety and Consent</h2>
<p>All video featuring children requires written consent from parents or guardians. Establish a media consent process at enrolment — most families are happy to provide it, but it must be documented. For public-facing video, do not show identifying information alongside children's faces (full names, locations).</p>

<h2>Where to Share Education Video</h2>
<ul>
  <li>Website homepage and enrolment page</li>
  <li>Facebook page (highly effective for childcare and school communities)</li>
  <li>Email newsletters to current families</li>
  <li>Google Business profile</li>
</ul>

<p>Perth Content has experience producing video for educational environments. <a href="contact.html">Enquire about our approach.</a></p>"""
),

# 9
dict(
slug="blog-trade-show-expo-video-perth",
title="Trade Show and Expo Video for Perth Businesses — Making Your Presence Last Beyond the Day",
description="Trade shows are expensive to attend. Video content before, during, and after your Perth expo presence multiplies the value — here is how to plan and produce it.",
tag="Industry",
read_time=5,
excerpt="Trade show attendance is a significant investment. Video before, during, and after your Perth expo appearance multiplies that investment — here is how to plan and produce it.",
hero_sub="A trade show lasts two days. The right video content can make your Perth business visible to people who were never in the room — for months afterwards.",
body="""<p>Perth businesses spend significant sums exhibiting at trade shows and expos — stand build, floor space, staff time, and collateral. Yet most walk away with nothing shareable beyond a stack of business cards. Video changes the ROI equation entirely.</p>

<h2>Pre-Show Promo Videos</h2>
<p>A short video (30-60 seconds) announcing your presence at an upcoming expo — posted on social and sent to your email list — builds anticipation, drives foot traffic to your stand, and begins conversations before the doors open. Include your stand number, what you will be showcasing, and a hook that gives people a reason to find you.</p>

<h2>Day-of Coverage</h2>
<p>Capture your exhibition stand in action. B-roll of the space, demonstrations, conversations with visitors (with consent), and team interviews all contribute to a compelling post-show package. Designate someone to capture footage throughout the day rather than trying to film and exhibit simultaneously.</p>
<ul>
  <li><strong>Stand overview shot:</strong> A wide shot of your stand setup and branding establishes context</li>
  <li><strong>Product/service demonstrations:</strong> Close-up footage of what you are showcasing is often more impactful in video than in person</li>
  <li><strong>Team interviews:</strong> Brief on-camera comments from your team about what excites them about the event</li>
  <li><strong>Visitor reactions:</strong> If visitors are willing, brief testimonials captured on the day are gold</li>
</ul>

<h2>Post-Show Highlight Reels</h2>
<p>A 60-90 second highlight reel edited from your day-of footage is one of the highest-performing pieces of content you can post after an expo. It shows your network that you showed up, you engaged, and you are active in your industry. Post it within 48 hours while the event is still fresh.</p>

<h2>Sponsor and Partnership Content</h2>
<p>If you sponsored a stage session or speaking slot, video of that presentation (edited to 3-5 minutes) positions you as a thought leader in your industry. This content works particularly well on LinkedIn and YouTube.</p>

<h2>Using Expo Footage Year-Round</h2>
<p>Trade show footage feeds your content pipeline for months. Clip individual demos as product videos, use stand b-roll as social proof on your website, and include expo highlights in pitch decks to demonstrate market presence.</p>

<p>Perth Content provides event videography and post-production for expos and trade shows. <a href="contact.html">Get a quote for your next event.</a></p>"""
),

# 10
dict(
slug="blog-how-to-brief-videographer-vs-editor",
title="How to Brief a Videographer vs a Video Editor — Key Differences Perth Businesses Should Know",
description="A videographer shoots your footage. An editor shapes it into a finished video. Perth businesses that understand the difference write better briefs and get better results. Here is what each role needs from you.",
tag="Production",
read_time=5,
excerpt="A videographer shoots footage. An editor shapes it into a finished video. Perth businesses that understand the difference write better briefs — and get far better results. Here is the breakdown.",
hero_sub="Confusing a videographer brief with an editor brief is one of the most common mistakes Perth businesses make. Here is what each professional actually needs from you.",
body="""<p>Many Perth businesses treat videographers and video editors as interchangeable — they are not. Understanding the distinction, and knowing what information each professional needs to do their best work, is the difference between a smooth production process and an expensive do-over.</p>

<h2>The Videographer Brief</h2>
<p>A videographer is responsible for capturing raw footage. They need to know:</p>
<ul>
  <li><strong>Location and logistics:</strong> Address, access requirements, parking, and any restrictions on filming (private property, noise-sensitive areas)</li>
  <li><strong>Shot list:</strong> A list of the specific shots you need — wide establishing shots, close-ups of products, talking head setups, action sequences. The more specific, the better.</li>
  <li><strong>Talent and subjects:</strong> Who will appear on camera, whether they need direction, and any specific looks or movements required</li>
  <li><strong>Technical requirements:</strong> Resolution (4K or 1080p), frame rate, any specific camera or lens requirements</li>
  <li><strong>Brand guidelines:</strong> Colour palette, any visual elements to feature, competitors to avoid referencing</li>
  <li><strong>Timeline:</strong> How many hours they have on site and the required delivery format for the raw footage</li>
</ul>

<h2>The Editor Brief</h2>
<p>An editor works with existing footage to build a finished video. They need entirely different information:</p>
<ul>
  <li><strong>Footage delivery:</strong> Where to access the raw files, organised by scene or shoot day</li>
  <li><strong>Desired length:</strong> Is this a 90-second social clip, a 3-minute website video, or a 10-minute documentary?</li>
  <li><strong>Reference videos:</strong> Examples of the look, pace, and feel you want — visual references save more time than lengthy descriptions</li>
  <li><strong>Music:</strong> Provide approved tracks or specify mood (upbeat, corporate, emotional) and tempo</li>
  <li><strong>Graphics and text:</strong> Lower thirds, title cards, subtitles — provide your brand fonts and any specific text required</li>
  <li><strong>Voiceover or script:</strong> If there is a VO, provide the audio file or the approved script</li>
  <li><strong>Revision process:</strong> How many revision rounds are included and who has sign-off authority</li>
</ul>

<h2>When One Person Does Both</h2>
<p>Many Perth video professionals are shoot-and-edit operators — they handle both production and post-production. In this case, your brief combines both lists, but the principle remains: be specific about the end deliverable from the start. Ambiguity at the brief stage always shows up as extra cost or reshoots later.</p>

<p>Perth Content handles both production and editing. <a href="contact.html">Talk to us about your project.</a></p>"""
),

# 11
dict(
slug="blog-music-licensing-perth-business-videos",
title="Music Licensing for Perth Business Videos — What You Need to Know",
description="Using unlicensed music in your business video can get it removed from every platform and expose you to copyright claims. Here is how Perth businesses should handle music licensing correctly.",
tag="Production",
read_time=5,
excerpt="Unlicensed music will get your video pulled from every platform and can result in copyright claims. Here is how Perth businesses should handle music licensing correctly and affordably.",
hero_sub="The wrong music choice can get your video removed from YouTube, Instagram, and Facebook overnight. Here is the straightforward guide to music licensing for Perth businesses.",
body="""<p>It is tempting to drop a popular song into your business video. Do not. Copyright infringement on business video content is enforced actively across every major platform — and the consequences range from content removal to legal claims. Here is what Perth businesses need to know.</p>

<h2>Why You Cannot Use Popular Music</h2>
<p>Popular music is protected by copyright. The rights are typically held by a record label (master rights) and a publisher (sync rights). Using that music in a commercial video without a synchronisation licence is infringement, even if you own the song on Spotify or iTunes. Platforms including YouTube, Instagram, and Facebook use automated content recognition (ContentID on YouTube) to detect unlicensed music and will mute, restrict, or remove your video.</p>

<h2>Royalty-Free Music Libraries</h2>
<p>Royalty-free does not mean free — it means you pay once and can use the track without ongoing royalties. The major platforms used by Australian video producers are:</p>
<ul>
  <li><strong>Epidemic Sound:</strong> Subscription-based ($15-49/month), excellent quality, full commercial licence included. The standard choice for Perth social media and YouTube content.</li>
  <li><strong>Artlist:</strong> Subscription-based ($30/month), strong curation, lifetime licence for tracks downloaded during your subscription.</li>
  <li><strong>Musicbed:</strong> Per-track and subscription options, higher-quality tracks, used for premium brand videos.</li>
  <li><strong>YouTube Audio Library:</strong> Free, limited selection, suitable for basic corporate content.</li>
</ul>

<h2>Sync Licences for Paid Advertising</h2>
<p>If you want to use a specific well-known track in a paid ad, you need a sync licence from the rights holders. This involves contacting the publisher and negotiating terms — a process that can cost thousands of dollars and take weeks. For most Perth businesses, royalty-free libraries are the practical alternative.</p>

<h2>Common Misconceptions</h2>
<ul>
  <li><strong>"It is only for internal use":</strong> Internal training videos are lower risk, but technically still require a licence for copyrighted music.</li>
  <li><strong>"I credited the artist":</strong> Attribution does not substitute for a licence.</li>
  <li><strong>"It is only a short clip":</strong> There is no "fair use for business" exception in Australian copyright law for commercial purposes.</li>
</ul>

<h2>Practical Advice</h2>
<p>For most Perth business video, an Epidemic Sound or Artlist subscription covers your ongoing needs at a cost that is negligible relative to the production investment. Build this into your video budget from the start.</p>

<p>Perth Content sources appropriately licensed music for all client projects. <a href="contact.html">Talk to us about your video.</a></p>"""
),

# 12
dict(
slug="blog-case-study-videos-perth-b2b",
title="Case Study Videos for Perth B2B Businesses — Your Most Persuasive Sales Asset",
description="A well-produced case study video is the closest thing to a warm referral you can put on your website. Here is how Perth B2B businesses can produce client story videos that actually close deals.",
tag="Strategy",
read_time=5,
excerpt="A well-produced case study video is the closest thing to a warm referral. Here is how Perth B2B businesses can structure and produce client story videos that actually convert prospects.",
hero_sub="Prospects do not just want to know what you do — they want to see what you have done for someone like them. Case study videos are the most persuasive content in the B2B toolkit.",
body="""<p>In B2B sales, the most powerful moment is when a prospect says "you sound like exactly what we need — have you done this for someone in our industry?" A case study video lets you answer that question on your website, before the sales conversation ever starts.</p>

<h2>The Structure That Works</h2>
<p>Effective B2B case study videos follow a simple three-act structure:</p>
<ol>
  <li><strong>The problem:</strong> What challenge was the client facing before they engaged you? Be specific — generic problems produce generic interest. Concrete problems produce recognition in similar prospects.</li>
  <li><strong>The solution:</strong> How did you approach it? What made your solution different from what the client could have done themselves or found elsewhere?</li>
  <li><strong>The results:</strong> What changed? Quantify where possible — percentages, dollar values, time saved, growth achieved. Numbers are memorable and shareable.</li>
</ol>
<p>Two to three minutes is the ideal length for a B2B case study video. Long enough to tell the story compellingly; short enough to watch in a single sitting.</p>

<h2>Getting Clients to Participate</h2>
<p>Most clients are happy to appear in a case study video — the challenge is making it easy for them. Key approaches:</p>
<ul>
  <li>Frame it as a profile of their success, not a testimonial for you</li>
  <li>Provide the questions in advance so they can prepare</li>
  <li>Handle all logistics — come to their office, keep it to 30-45 minutes of their time</li>
  <li>Offer to share the finished video with their own marketing team (it is useful content for them too)</li>
</ul>

<h2>Where to Use Case Study Videos</h2>
<ul>
  <li><strong>Website:</strong> Create a dedicated case studies section, organised by industry or outcome</li>
  <li><strong>Sales process:</strong> Send relevant case studies to prospects at the proposal stage</li>
  <li><strong>LinkedIn:</strong> Post individual client stories as LinkedIn video — tag the client (with permission) for amplified reach</li>
  <li><strong>Pitch decks:</strong> Embed or link to case study videos in your proposals</li>
</ul>

<h2>What Separates Great from Good</h2>
<p>The best case study videos are specific, honest, and personal. Avoid corporate language and generic claims. Let the client speak in their own words about the real impact on their business. Authenticity outperforms polish in this format.</p>

<p>Perth Content produces B2B case study videos across a range of industries. <a href="contact.html">Talk to us about your client stories.</a></p>"""
),

# 13
dict(
slug="blog-video-email-marketing-perth",
title="Video in Email Marketing — How Perth Businesses Can Boost Open Rates and Click-Throughs",
description="Adding video to your email marketing campaigns lifts open rates, click-through rates, and conversions. Here is the practical guide for Perth businesses — what works and what does not.",
tag="Strategy",
read_time=5,
excerpt="Video in email marketing lifts open rates and click-through rates significantly. Here is the practical guide for Perth businesses on what works, what does not, and how to implement it.",
hero_sub="Email remains one of the highest-ROI marketing channels for Perth businesses. Adding video to your campaigns can dramatically increase the impact — here is how to do it right.",
body="""<p>Mentioning the word "video" in an email subject line increases open rates by an average of 19%, and click-through rates by up to 65%. Yet most Perth businesses are not using video in their email marketing at all — which means it is a clear differentiator for those who do.</p>

<h2>The Technical Reality: Embedding vs Thumbnails</h2>
<p>Most email clients (Outlook, Apple Mail, Gmail) do not support embedded video playback. Attempting to embed a video that auto-plays in an email will cause it to be blocked or broken for most recipients. The correct approach is to use a static image thumbnail that links to the video hosted elsewhere (your website, YouTube, or Vimeo). The thumbnail creates the visual impression of a video player; the click takes the reader to the video.</p>

<h2>Creating the Perfect Video Email Thumbnail</h2>
<ul>
  <li>Use a frame from the video that is visually compelling — a face, a key moment, or a striking image</li>
  <li>Overlay a play button icon so the image clearly reads as a video</li>
  <li>Keep it the same width as your email template</li>
  <li>Write alt text describing the video in case images are disabled</li>
</ul>

<h2>Subject Lines That Work</h2>
<p>Including the word "video" in your subject line — "[Video] How we reduced our client's marketing costs by 40%" — consistently outperforms subject lines without it. The word signals something different from the usual text-heavy email, which drives curiosity and opens.</p>

<h2>Where Video Fits in Email Sequences</h2>
<ul>
  <li><strong>Welcome sequences:</strong> A video introduction from your team in email 1 dramatically improves engagement with subsequent emails</li>
  <li><strong>Post-enquiry nurturing:</strong> A case study video sent after an initial enquiry can significantly increase conversion to consultation</li>
  <li><strong>Proposal follow-up:</strong> Following up a written proposal with a short video personalising the key points lifts close rates</li>
  <li><strong>Re-engagement campaigns:</strong> A video message to lapsed clients or subscribers tends to outperform text-only re-engagement emails</li>
</ul>

<h2>Personalised Video</h2>
<p>Tools like Loom allow you to quickly record a short, personalised video message addressed directly to a specific prospect or client. Used at high-value points in the sales cycle — after a proposal, before a renewal conversation — personalised video is one of the highest-converting tactics available.</p>

<p>Perth Content can produce video content optimised for email use. <a href="contact.html">Get in touch about your email strategy.</a></p>"""
),

# 14
dict(
slug="blog-4k-vs-1080p-video-perth-businesses",
title="4K vs 1080p Video — What Perth Businesses Actually Need to Know",
description="The resolution debate confuses many Perth businesses. Here is a practical guide to when 4K matters, when 1080p is perfectly fine, and what to specify for your next video project.",
tag="Production",
read_time=5,
excerpt="The 4K vs 1080p debate confuses most Perth businesses. Here is a practical guide to when the difference matters, when it does not, and what to specify for your next video project.",
hero_sub="4K sounds better. But for most Perth business video, 1080p delivers exactly the same result at a fraction of the storage and processing cost. Here is when each resolution makes sense.",
body="""<p>Camera specifications are a topic video companies love to lead with. 4K, 6K, 8K — the numbers escalate rapidly. For most Perth businesses producing marketing and corporate video, this is largely noise. Here is what actually matters.</p>

<h2>What 4K and 1080p Mean in Practice</h2>
<p>1080p (Full HD) has a resolution of 1920x1080 pixels. 4K (Ultra HD) has a resolution of 3840x2160 pixels — four times as many pixels. On a screen smaller than 55 inches, most viewers cannot perceive the difference when content is compressed for web delivery. On a large display or LED video wall, 4K shows a visible improvement.</p>

<h2>When 4K Is Worth It</h2>
<ul>
  <li><strong>Reframing in post-production:</strong> If you shoot 4K and deliver 1080p, your editor has room to reframe, crop in, or stabilise the image without losing quality. This is genuinely valuable for run-and-gun shooting where every shot cannot be perfectly composed.</li>
  <li><strong>Future-proofing:</strong> If your video will be used for 5+ years on large-screen displays, 4K provides longevity.</li>
  <li><strong>Digital billboards and large-format displays:</strong> For video wall installations or trade show screens, 4K is appropriate.</li>
  <li><strong>Colour grading latitude:</strong> 4K cameras often capture more colour information (Log or RAW), giving editors more flexibility in colour grading.</li>
</ul>

<h2>When 1080p Is Perfectly Fine</h2>
<ul>
  <li>Social media video (Instagram, Facebook, TikTok, LinkedIn)</li>
  <li>Website video (compressed for web delivery)</li>
  <li>YouTube videos watched on phones and laptops</li>
  <li>Training and internal communication video</li>
  <li>Testimonial and interview footage</li>
</ul>
<p>Platforms compress video during upload regardless of source resolution. A 4K video uploaded to Instagram is compressed and delivered at effective 1080p quality anyway.</p>

<h2>File Size and Workflow Implications</h2>
<p>4K footage produces files roughly four times larger than 1080p. A one-hour shoot in 4K ProRes can produce over 400GB of footage. This affects storage costs, upload time, and editing performance (you need a faster machine). For high-volume social content, 1080p is often the more practical choice.</p>

<h2>What to Specify for Your Project</h2>
<p>For most Perth business marketing video: 4K capture, 1080p delivery. You get the reframing benefits of 4K during editing, without the delivery overhead. For social-only content on a tight turnaround: 1080p throughout is simpler and faster.</p>

<p>Perth Content advises clients on the right specifications for their project. <a href="contact.html">Talk to us.</a></p>"""
),

# 15
dict(
slug="blog-perth-construction-trades-video-marketing",
title="Video Marketing for Perth Builders, Electricians, and Trades — Show the Work, Win the Job",
description="Perth builders, electricians, plumbers, and landscapers using video are winning more jobs. Time-lapses, before-and-afters, and client testimonials are the most effective formats — here is how to use them.",
tag="Industry",
read_time=5,
excerpt="Perth trades and builders using video are consistently winning more work. Time-lapses, before-and-afters, and testimonials are the top-performing formats — here is the practical guide.",
hero_sub="In the trades, your work speaks for itself — but only if people can see it. Video is the best way to showcase completed projects, build trust, and stand out from every other quote.",
body="""<p>Perth homeowners searching for a reliable builder, electrician, or landscaper face a difficult problem: every tradesperson claims to be professional, reliable, and quality-focused. Video is the fastest way to prove it rather than just claim it.</p>

<h2>Project Time-Lapses</h2>
<p>A time-lapse of a project from start to finish — construction, landscaping, renovation — is one of the most compelling video formats for the trades. It demonstrates the scope of your work, the pace of your team, and the transformation you deliver, all in 60-90 seconds. A basic time-lapse setup (a GoPro or phone in a fixed position) costs almost nothing to produce. The results on social media are consistently high-engagement.</p>

<h2>Before-and-After Videos</h2>
<p>The before-and-after format works across almost every trade: electrical switchboard upgrades, bathroom renovations, deck installations, landscaping transformations. Film the starting condition, conduct the work, then film the finished result. Splice them together with a simple wipe transition. This format dominates renovation and home services content on Facebook and Instagram.</p>

<h2>On-Site Explainer Videos</h2>
<p>Short videos filmed on site explaining what you are doing and why — "Here is why we are running the conduit this way rather than the direct route" — position you as an expert, not just a pair of hands. Homeowners are fascinated by the reasoning behind trade decisions. These videos build enormous trust and answer the unasked questions that slow down quoting decisions.</p>

<h2>Client Testimonials After Handover</h2>
<p>The moment of handover — handing over the keys to a completed renovation, showing a client their finished deck, switching on a new lighting installation — is the perfect time to capture a brief client testimonial. Emotions are high and genuine satisfaction is visible. These clips are your most powerful sales tool.</p>

<h2>Google Business Profile Videos</h2>
<p>Google Business profiles that include video receive significantly more calls than those without. Upload your best project before-and-after or testimonial video directly to your Google Business profile — it appears in search results when people look for your trade in their Perth suburb.</p>

<p>Perth Content helps trades businesses build a content library from their project footage. <a href="contact.html">Talk to us about a simple production setup.</a></p>"""
),

# 16
dict(
slug="blog-nonprofit-charity-video-perth",
title="Video for Perth Nonprofits and Charities — Telling Stories That Drive Donations and Support",
description="Perth nonprofits and charities using video raise more donations, recruit more volunteers, and build stronger community connections. Here is how to produce impact stories on a tight budget.",
tag="Industry",
read_time=5,
excerpt="Perth nonprofits using video raise more, recruit more volunteers, and build stronger communities. Here is how to produce powerful impact stories even on a tight budget.",
hero_sub="Video is the most powerful medium for the kind of emotional connection that drives generosity. Perth nonprofits using it strategically are raising more and reaching further than those that do not.",
body="""<p>Charity and cause marketing is driven by emotional resonance. Donors and supporters do not give to statistics — they give to stories. Video is the only medium that can deliver the full emotional impact of a beneficiary story, a community need, or an organisation's vision.</p>

<h2>Beneficiary and Impact Stories</h2>
<p>A 2-3 minute video following one person or family whose life has been changed by your organisation's work is the single most effective fundraising content you can produce. The formula is simple: show the before (the need or challenge), show the intervention (your organisation's role), and show the transformation. This format consistently outperforms all other fundraising communication in donations per impression.</p>

<h2>Campaign and Appeal Videos</h2>
<p>For specific fundraising campaigns — end-of-financial-year appeals, capital campaigns, emergency responses — a dedicated campaign video with a clear call to action outperforms text appeals significantly. Include a specific, concrete ask: "Your $50 will provide X" performs better than general impact statements.</p>

<h2>Annual Report and Impact Videos</h2>
<p>Increasingly, Perth nonprofits are supplementing written annual reports with short video summaries (3-5 minutes) covering the year's highlights, impact statistics, and organisational direction. These are shared with donors, presented at AGMs, and used in grant applications to demonstrate organisational capability.</p>

<h2>Volunteer Recruitment Videos</h2>
<p>Showing potential volunteers what they will actually do — the tasks, the environment, the team — converts more applicants from the enquiry stage to the first shift. A current volunteer speaking candidly about their experience is more persuasive than any written recruitment message.</p>

<h2>Budget-Conscious Production</h2>
<p>Many Perth nonprofits assume professional video is beyond their budget. It does not have to be:</p>
<ul>
  <li>Some Perth production companies offer nonprofit rates or pro-bono arrangements — ask directly</li>
  <li>A skilled volunteer with a good camera and editing software can produce effective content with modest production guidance</li>
  <li>Authenticity often outperforms production value in this sector — raw, real footage can be more powerful than polished corporate video</li>
</ul>

<p>Perth Content supports nonprofit organisations with flexible production arrangements. <a href="contact.html">Talk to us about your organisation.</a></p>"""
),

# 17
dict(
slug="blog-how-to-prepare-video-shoot-day",
title="How to Prepare for a Video Shoot Day — A Perth Business Checklist",
description="Poor preparation is the biggest cause of wasted time and budget on video shoot days. Here is a complete checklist for Perth businesses — what to do in the week before, the day before, and on the day.",
tag="Production",
read_time=5,
excerpt="Poor preparation is the biggest cause of wasted budget on video shoot days. Here is a complete checklist for Perth businesses — what to do in the week before, the day before, and on the day.",
hero_sub="Every hour of wasted time on a video shoot day costs money. Most of the common mistakes are entirely preventable — here is the checklist that keeps Perth shoots running on schedule.",
body="""<p>A video shoot day has a fixed window of time and a fixed cost. What makes the difference between a smooth, productive day and an expensive scramble is almost always preparation. Here is the checklist Perth businesses should work through before any shoot.</p>

<h2>One Week Before</h2>
<ul>
  <li><strong>Confirm the run sheet:</strong> A detailed schedule showing what is being filmed, when, and who is needed on camera for each segment</li>
  <li><strong>Lock the shot list:</strong> Agree the final list of shots with your videographer — changes on the day cost time</li>
  <li><strong>Brief all on-camera talent:</strong> Share the topics they will discuss, the tone you want, and what not to say. The goal is relaxed familiarity, not memorised scripts.</li>
  <li><strong>Book the location:</strong> Confirm access permission, parking for crew, and any permits required for outdoor filming</li>
  <li><strong>Organise props and products:</strong> If products, signage, or branded materials will feature, confirm they are available and in good condition</li>
</ul>

<h2>The Day Before</h2>
<ul>
  <li><strong>Clean and declutter the filming location:</strong> Camera picks up background chaos that is invisible to the naked eye. Remove anything from the background that should not appear.</li>
  <li><strong>Check wardrobe:</strong> Brief on-camera participants on what to wear (solid colours work well; avoid tight patterns which create a strobe effect). Remind them what not to wear (branding of competitors, anything too casual).</li>
  <li><strong>Brief reception or front desk:</strong> Let your team know filming is happening so phones are answered quietly, loud deliveries are avoided, and unexpected visitors do not walk into shot.</li>
  <li><strong>Charge everything:</strong> If you are providing any equipment (laptops for screen recordings, devices for demonstrations), ensure they are charged and functioning.</li>
</ul>

<h2>On the Day</h2>
<ul>
  <li><strong>Start with the most important shot:</strong> Film your hero content while everyone is fresh and time buffer exists</li>
  <li><strong>Turn off HVAC if possible:</strong> Air conditioning noise is the most common audio problem in Perth office shoots</li>
  <li><strong>Silence phones:</strong> Ask everyone in the filming area to put phones on silent</li>
  <li><strong>Give talent a warmup take:</strong> Most people improve significantly from take 1 to take 3 — factor this into your schedule</li>
  <li><strong>Capture b-roll last:</strong> Once your hero shots are in the can, fill time with supplementary b-roll footage</li>
</ul>

<p>Perth Content provides a pre-shoot checklist as standard with every production engagement. <a href="contact.html">Enquire about our production process.</a></p>"""
),

# 18
dict(
slug="blog-corporate-headshot-vs-video-bio-perth",
title="Corporate Headshot vs Video Bio — Which Is Better for Perth Professionals in 2027?",
description="The corporate headshot is being replaced by the video bio on professional profiles. Here is how Perth professionals can create a compelling 60-second video introduction that works harder than any photo.",
tag="Strategy",
read_time=5,
excerpt="The corporate headshot is giving way to the video bio. Here is how Perth professionals can create a compelling 60-second video introduction that builds more trust than any photo ever could.",
hero_sub="A headshot tells people what you look like. A video bio tells them who you are. Here is why Perth professionals are switching, and how to produce one that works.",
body="""<p>For the past decade, the corporate headshot has been the standard professional calling card — on LinkedIn, on your firm's website, in conference programmes. In 2027, it remains useful, but it is increasingly being supplemented by something more powerful: the video bio.</p>

<h2>What a Video Bio Is</h2>
<p>A video bio is a 60-90 second video introduction filmed directly to camera in which you briefly cover who you are, what you specialise in, who you help, and what makes your approach distinctive. It sits on your LinkedIn profile, your website's team page, or your email signature as a linked thumbnail.</p>

<h2>What a Video Bio Does That a Headshot Cannot</h2>
<ul>
  <li><strong>Demonstrates communication style:</strong> In service-based professions, how you communicate is as important as what you know. A video bio lets potential clients assess whether they will enjoy working with you.</li>
  <li><strong>Builds pre-meeting trust:</strong> Prospects who have watched your video bio before an initial meeting report feeling more comfortable and prepared — meetings start warmer and close faster.</li>
  <li><strong>Stands out on LinkedIn:</strong> Very few Perth professionals have a video bio. It immediately differentiates your profile from the thousands of static headshots in any search result.</li>
  <li><strong>Shows personality:</strong> A smile, a laugh, a moment of genuine enthusiasm — these are trust signals that no photograph can convey.</li>
</ul>

<h2>What to Include in 60-90 Seconds</h2>
<ol>
  <li>Who you are and your role (15 seconds)</li>
  <li>What you specialise in and who you help (20 seconds)</li>
  <li>What makes your approach different or your unique value (20 seconds)</li>
  <li>One personal element that makes you memorable (10 seconds)</li>
  <li>A brief invitation to connect or get in touch (10 seconds)</li>
</ol>

<h2>Production Tips</h2>
<p>Film near a window for flattering natural light. Use a clean, professional background — your office, a bookcase, or a plain wall. Speak conversationally; avoid reading from a script. One or two takes recorded on a modern iPhone or mirrorless camera with a lavalier microphone will produce professional results.</p>

<p>Perth Content offers video bio sessions for individuals and professional firms. <a href="contact.html">Book a session.</a></p>"""
),

# 19
dict(
slug="blog-hospitality-hotel-video-perth",
title="Video Marketing for Perth Hotels and Hospitality Businesses — Converting Browsers into Bookings",
description="Perth hotels, resorts, and hospitality venues that invest in professional video consistently outperform competitors in direct bookings. Here is what to produce and where to use it.",
tag="Industry",
read_time=5,
excerpt="Perth hotels and hospitality venues with professional video consistently outperform competitors in direct bookings. Here is what to produce and where to use it to convert browsers into guests.",
hero_sub="A hotel booking is an emotional purchase. Video creates the desire to stay — it shows the experience before guests arrive. Here is the hospitality video playbook for Perth properties.",
body="""<p>Hotel guests do not book rooms — they book experiences. And nothing sells an experience like video. Perth properties that invest in professional video consistently outperform their competitors on direct booking conversions, reducing dependence on OTA commissions.</p>

<h2>Property Showcase Video</h2>
<p>A 90-second to 2-minute property showcase is the cornerstone of hotel video marketing. Capture your lobby, rooms, pool, gym, restaurant, and view. The footage should be aspirational — shot during golden hour, with beautiful ambient lighting, to make guests feel the experience before they arrive. This video belongs on your homepage, OTA listings where permitted, and social media.</p>

<h2>Room Type Videos</h2>
<p>Short individual videos (30-45 seconds) for each room category — standard, deluxe, suite — hosted on your direct booking engine perform well for two reasons: they increase the average booking value (guests are more likely to upgrade when they can see what the higher room looks like), and they reduce booking abandonment by answering visual questions before checkout.</p>

<h2>Dining and Experience Videos</h2>
<p>If your property has a restaurant, bar, spa, or other experiences, short individual videos for each increase the total spend per guest. A 45-second video of your restaurant in dinner service — the plating, the atmosphere, the crowd — is more effective than any menu description.</p>

<h2>Weddings and Events</h2>
<p>If your venue hosts weddings and corporate events, a dedicated video for this market is essential. Show the ballroom configured for a wedding ceremony, then a reception. Show the conference facilities in use. These videos significantly increase direct enquiries from event planners and couples who have already decided they want to get married in Perth.</p>

<h2>Seasonal and Campaign Content</h2>
<p>Perth has distinct seasons for hospitality — summer weekends, winter escapes, school holiday packages. Short social video content timed to each season, featuring the specific reasons to visit during that period, drives direct bookings and reduces reliance on last-minute OTA discounting.</p>

<p>Perth Content produces hospitality video for properties across Perth and the South West. <a href="contact.html">Talk to us about your property.</a></p>"""
),

# 20
dict(
slug="blog-perth-startup-pitch-video-guide",
title="The Perth Startup Pitch Video Guide — What Investors Actually Want to See",
description="A compelling pitch video can open doors to Perth and Australian investors before a face-to-face meeting. Here is the structure, production approach, and distribution strategy that works.",
tag="Strategy",
read_time=6,
excerpt="A compelling pitch video opens investor doors before the meeting. Here is the structure, production approach, and distribution strategy Perth startups should use to get noticed.",
hero_sub="Investors see hundreds of pitch decks. A well-produced pitch video cuts through the noise and gets you to the conversation. Here is how Perth startups should approach it.",
body="""<p>The startup funding process is competitive. A pitch video does not replace a pitch deck or a meeting — it gets you the meeting. For Perth startups approaching angel investors, VCs, or accelerator programmes, a well-produced pitch video is an increasingly essential asset.</p>

<h2>Pitch Video vs Explainer Video</h2>
<p>These are different things. An explainer video is aimed at customers — it explains what your product does and why they should use it. A pitch video is aimed at investors — it explains the business opportunity and why you are the team to execute it. Get clear on which you are producing before you start.</p>

<h2>The Structure That Gets Responses</h2>
<p>A startup pitch video should be 2-3 minutes maximum. Longer loses attention; shorter sacrifices the detail investors need. Cover these elements in order:</p>
<ol>
  <li><strong>The problem (20 seconds):</strong> Make the pain point vivid and specific. Investors need to believe the problem is real and significant.</li>
  <li><strong>Your solution (30 seconds):</strong> What do you do and how does it work? Show the product if possible — a demo clip is more compelling than a description.</li>
  <li><strong>The market (20 seconds):</strong> How big is the addressable market? Why now?</li>
  <li><strong>Traction (30 seconds):</strong> What have you achieved so far? Revenue, customers, partnerships, pilot results. Numbers build credibility.</li>
  <li><strong>The team (20 seconds):</strong> Who are you and why are you uniquely qualified to solve this problem? Investors back people as much as ideas.</li>
  <li><strong>The ask (20 seconds):</strong> How much are you raising, what will you use it for, and what milestones will it achieve?</li>
</ol>

<h2>Production Quality</h2>
<p>Production quality signals professionalism. Investors do not expect Hollywood — but they do expect clean audio, decent lighting, and a steady shot. A poorly produced pitch video can undermine an otherwise compelling story. Invest in professional production for this asset.</p>

<h2>Where to Share Your Pitch Video</h2>
<ul>
  <li>AngelList / Equity Crowdfunding platforms</li>
  <li>LinkedIn (tag relevant investors and accelerator programmes)</li>
  <li>Cold outreach emails to angel investors and VCs (video thumbnails drive higher response rates than text)</li>
  <li>Perth accelerator programme applications (Spacecubed, Founders at Curtin)</li>
</ul>

<p>Perth Content produces startup pitch videos and product demos. <a href="contact.html">Talk to us about your raise.</a></p>"""
),

# 21
dict(
slug="blog-instagram-stories-vs-reels-perth-business",
title="Instagram Stories vs Reels for Perth Businesses — Which Format Drives More Results?",
description="Stories and Reels serve different strategic purposes on Instagram. Here is how Perth businesses should be using each format in 2027 to maximise reach, engagement, and enquiries.",
tag="Platforms",
read_time=5,
excerpt="Stories and Reels serve different strategic purposes on Instagram. Here is how Perth businesses should use each format to maximise reach, engagement, and enquiries in 2027.",
hero_sub="Reels and Stories are both video — but they do completely different jobs for your Perth business. Here is when to use each, and how to make them work together.",
body="""<p>Many Perth businesses post the same content to both Stories and Reels without thinking about the different audiences and mechanics of each format. Understanding the distinction unlocks significantly better results from both.</p>

<h2>How They Differ Fundamentally</h2>
<p><strong>Stories</strong> are ephemeral (24 hours), shown exclusively to your existing followers in the Stories tray, and designed for casual, intimate content. They prioritise relationship-maintenance with people who already know you.<br>
<strong>Reels</strong> are permanent (until you delete them), distributed to non-followers via the Explore feed and Reels tab, and designed for discoverability. They prioritise reaching new audiences.</p>

<h2>When to Use Stories</h2>
<p>Stories are the right format for:</p>
<ul>
  <li>Behind-the-scenes glimpses of your day or team</li>
  <li>Quick updates, announcements, or time-sensitive offers</li>
  <li>Polls, quizzes, and Q&amp;A stickers to drive engagement with existing followers</li>
  <li>Sharing client wins or quick testimonials</li>
  <li>Driving traffic to specific links (using the link sticker)</li>
  <li>Re-sharing Reels to your Story after posting, to give them a second wave of exposure</li>
</ul>

<h2>When to Use Reels</h2>
<p>Reels are the right format for:</p>
<ul>
  <li>Educational content — tips, how-tos, industry insights</li>
  <li>Showcasing your work and results</li>
  <li>Reaching potential clients who do not yet follow you</li>
  <li>Trending audio formats that drive algorithmic boost</li>
  <li>Campaign content with a specific call to action</li>
</ul>

<h2>The Content Overlap Mistake</h2>
<p>A common Perth business mistake is re-sharing a Reel directly to Stories, adding a "Watch my Reel!" sticker. This performs poorly. Your followers have likely already seen the Reel. Instead, create Stories content that references the Reel with additional context — behind the scenes of how you made it, a question related to the Reel topic, or a poll that adds interactivity.</p>

<h2>The Right Ratio for Perth Businesses</h2>
<p>A sustainable approach: 1-2 Reels per week (planned, produced content) plus 3-5 Stories per week (spontaneous, authentic moments). This keeps discovery working while maintaining the relationship content that turns followers into clients.</p>

<p>Perth Content produces Reels-optimised video for Perth businesses. <a href="contact.html">Get in touch.</a></p>"""
),

# 22
dict(
slug="blog-video-production-timeline-perth",
title="How Long Does a Video Project Take? A Realistic Timeline for Perth Businesses",
description="Perth businesses often underestimate how long video production takes. Here is a realistic breakdown of timelines by project type — from brief to delivered file.",
tag="Production",
read_time=5,
excerpt="Perth businesses consistently underestimate how long video production takes. Here is a realistic timeline breakdown by project type — from initial brief to final delivery.",
hero_sub="Video projects take longer than most Perth businesses expect. Understanding the realistic timeline by project type helps you plan, brief suppliers, and avoid costly last-minute rushes.",
body="""<p>One of the most common frustrations in video production is a mismatch between client expectations and production timelines. "Can we have it by Friday?" is a question video producers hear regularly. Here is what realistic timelines look like for different types of video projects.</p>

<h2>What Drives Production Time</h2>
<p>Every video project has three phases, each with its own timeline drivers:</p>
<ul>
  <li><strong>Pre-production:</strong> Brief, concept development, scripting, location scouting, talent confirmation, scheduling</li>
  <li><strong>Production:</strong> The shoot day(s)</li>
  <li><strong>Post-production:</strong> Editing, colour grading, audio mix, motion graphics, review rounds, final export</li>
</ul>
<p>Rushing any phase usually creates problems in the next. Scripts written in an hour produce awkward shoot days. Shoots with no pre-production produce edit nightmares.</p>

<h2>Realistic Timelines by Project Type</h2>
<p><strong>Social media short-form clip (15-60 seconds):</strong><br>
Simple, single-location: 1-2 weeks from brief to delivery. Rush possible in 3-4 business days with a clear brief and immediate asset provision.</p>

<p><strong>Corporate talking head video (1-3 minutes):</strong><br>
2-3 weeks. Allow time for script approval, scheduling on-camera talent, a shoot day, and 1-2 review rounds.</p>

<p><strong>Brand / homepage hero video (60-90 seconds):</strong><br>
3-5 weeks. Concept development, multiple locations, professional shoot, careful edit, multiple review rounds.</p>

<p><strong>Event highlight reel:</strong><br>
Footage captured on event day, delivery within 5-7 business days is reasonable. Same-day turnaround is possible for an extra fee.</p>

<p><strong>Explainer or animated video (60-90 seconds):</strong><br>
4-6 weeks. Script, voiceover recording, animation, review rounds. Animation is time-intensive.</p>

<p><strong>Case study or documentary-style video (3-5 minutes):</strong><br>
4-8 weeks. Multiple shoot locations, interview scheduling across different clients, complex edit.</p>

<h2>What Slows Projects Down</h2>
<ul>
  <li>Unclear or changing brief after production starts</li>
  <li>Multiple stakeholders with sign-off authority (each review round adds days)</li>
  <li>Late provision of brand assets, logos, or approved music</li>
  <li>Talent unavailability for shoot day scheduling</li>
</ul>

<p>Perth Content builds realistic project timelines into every engagement from the first brief. <a href="contact.html">Start a conversation about your project.</a></p>"""
),

# 23
dict(
slug="blog-thumbnail-design-youtube-perth",
title="YouTube Thumbnail Design — How Perth Businesses Can Dramatically Improve Click-Through Rates",
description="Your YouTube thumbnail is the single biggest lever for improving video performance. Here is how Perth businesses should design thumbnails that get clicked, using proven visual principles.",
tag="Platforms",
read_time=5,
excerpt="Your YouTube thumbnail is the biggest lever for improving video performance. Here is how Perth businesses should design thumbnails that get clicked, using proven visual principles.",
hero_sub="YouTube gives every video two ways to earn a click: the title and the thumbnail. Most Perth businesses neglect the thumbnail — and leave a huge amount of view potential on the table.",
body="""<p>YouTube's algorithm distributes videos based on click-through rate. A video with a compelling thumbnail that earns a 10% CTR will be shown to far more people than the same video with a boring thumbnail earning 3% CTR. For Perth businesses investing in YouTube content, thumbnail design is not a cosmetic detail — it is a performance driver.</p>

<h2>Why Thumbnails Matter More Than Titles</h2>
<p>Studies of YouTube viewer behaviour consistently show that thumbnails attract the eye before titles are read. When browsing search results or recommended videos, viewers are scanning visual elements first. A striking thumbnail earns the attention that allows the title to be read.</p>

<h2>The Elements of a High-CTR Thumbnail</h2>
<ul>
  <li><strong>A face with an expression:</strong> Human faces (particularly with strong, specific expressions — surprise, curiosity, enthusiasm) are the most attention-grabbing element in any visual environment. If your content involves on-camera talent, use a close-cropped face as the anchor of your thumbnail.</li>
  <li><strong>Bold, minimal text:</strong> 3-5 words maximum, in a large font (legible at thumbnail size, which is very small on mobile). The text should tease or complement the title, not repeat it.</li>
  <li><strong>High contrast:</strong> Your thumbnail needs to stand out against YouTube's white/dark background. Use strong contrast between foreground elements and the background.</li>
  <li><strong>Brand consistency:</strong> Use the same font, colour palette, and layout style across all your thumbnails. Viewers who have watched one of your videos should recognise subsequent thumbnails instantly.</li>
</ul>

<h2>Tools for Creating Thumbnails</h2>
<ul>
  <li><strong>Canva:</strong> Easiest for non-designers. Has a YouTube thumbnail template with correct dimensions (1280x720px).</li>
  <li><strong>Adobe Photoshop or Express:</strong> More control, better for photo manipulation and background removal.</li>
  <li><strong>Figma:</strong> Good for teams maintaining brand consistency across multiple creators.</li>
</ul>

<h2>A/B Testing Thumbnails</h2>
<p>YouTube Studio allows you to A/B test thumbnails against each other to see which version drives a higher CTR. If you are producing content consistently, test a new thumbnail approach every quarter. Small improvements in CTR compound into significant additional views over time.</p>

<h2>Common Mistakes</h2>
<ul>
  <li>Using a random auto-generated screenshot from the video</li>
  <li>Thumbnail too cluttered or busy</li>
  <li>Text too small to read at thumbnail size</li>
  <li>No brand consistency across the channel</li>
</ul>

<p>Perth Content helps clients develop branded YouTube thumbnail templates. <a href="contact.html">Ask about our creative services.</a></p>"""
),

# 24
dict(
slug="blog-how-to-repurpose-webinar-content-video",
title="How to Repurpose Your Webinar Recording Into 12 Pieces of Video Content",
description="A webinar recording is a goldmine of reusable content. Here is how Perth businesses can extract clips, short-form social videos, audiograms, and highlights from a single webinar recording.",
tag="Strategy",
read_time=5,
excerpt="A single webinar recording can yield 12+ pieces of content. Here is how Perth businesses can systematically extract clips, Reels, LinkedIn video, and more from one session.",
hero_sub="Most Perth businesses record a webinar and then let the recording sit in a Google Drive folder. Here is how to turn that same footage into a month of video content.",
body="""<p>A 60-minute webinar contains enough content to fuel your social channels for weeks. The mistake most Perth businesses make is posting the full recording once and moving on. Repurposing requires a systematic approach — here is the framework.</p>

<h2>Step 1: Identify the Clips First</h2>
<p>Before any editing, watch your recording and timestamp the moments worth extracting:</p>
<ul>
  <li>Key insights or statistics (30-60 seconds)</li>
  <li>Strong analogies or memorable explanations (60-90 seconds)</li>
  <li>Audience questions with particularly good answers (60-120 seconds)</li>
  <li>Any moment of genuine energy, humour, or emotional resonance</li>
  <li>The opening hook (the first 60 seconds of a well-structured webinar is often the best clip)</li>
</ul>
<p>A 60-minute webinar typically yields 8-15 clipable moments.</p>

<h2>What You Can Create From a Single Webinar</h2>
<ul>
  <li><strong>Full recording:</strong> Upload to YouTube (optimised with title, description, chapters, thumbnail) and embed on your website</li>
  <li><strong>Highlight reel:</strong> 3-5 minute edited summary of the best moments for LinkedIn and YouTube</li>
  <li><strong>Short-form clips (Reels/TikTok):</strong> 4-8 clips, each 30-60 seconds, cropped to vertical for Instagram/TikTok</li>
  <li><strong>LinkedIn video posts:</strong> 3-5 horizontal clips (60-90 seconds) with individual context captions</li>
  <li><strong>Audiogram:</strong> Audio from a key moment overlaid on a static or animated waveform graphic — effective on platforms where video production is not expected</li>
  <li><strong>Blog post:</strong> Transcribe a section of the webinar into a structured blog post — not directly covered here, but frequently paired with video repurposing</li>
</ul>

<h2>Caption Every Clip</h2>
<p>All short-form clips should have captions. Most webinar content is talking-head footage, and 85% of social video is watched on mute. Captions dramatically increase completion rates on clips from educational content.</p>

<h2>Scheduling for Maximum Reach</h2>
<p>Spread your repurposed content over 4-6 weeks rather than releasing everything at once. This extends the value of a single recording across an entire content calendar period.</p>

<p>Perth Content provides webinar editing and repurposing packages. <a href="contact.html">Talk to us after your next webinar.</a></p>"""
),

# 25
dict(
slug="blog-sports-club-association-video-perth",
title="Video Marketing for Perth Sports Clubs and Associations — Building Community and Winning Sponsors",
description="Perth sports clubs using video are growing memberships, attracting sponsors, and building the kind of community that keeps members returning. Here is the content playbook.",
tag="Industry",
read_time=5,
excerpt="Perth sports clubs using video are growing memberships, attracting sponsors, and building genuine community. Here is the content playbook for clubs of any size and any sport.",
hero_sub="Sports is one of the most visual content categories in the world. Perth clubs that document their season on video build communities that grow and sponsors that stay.",
body="""<p>Sports clubs have one of the richest content environments of any organisation — athletes competing, coaches coaching, volunteers giving, communities celebrating. Yet most Perth clubs produce almost no video. Those that do have a significant advantage in membership growth and sponsor retention.</p>

<h2>Match and Training Highlights</h2>
<p>A weekly highlight reel from training or matches (60-90 seconds) is the most engaging recurring content a sports club can produce. Post it every week without fail. Over a season, this builds a following that starts tagging friends, sharing clips, and recruiting new members organically.</p>
<p>You do not need a professional videographer to do this — a club member with a phone and basic editing skills (CapCut is free and excellent) can produce compelling weekly highlights with minimal time investment.</p>

<h2>Player and Athlete Profiles</h2>
<p>Short videos (60-90 seconds) profiling individual players — their background, their role in the team, their goal for the season — humanise your club and are consistently among the highest-engagement posts for sports organisations. They also give featured athletes content to share with their own networks, dramatically amplifying your organic reach.</p>

<h2>Season Recap Videos</h2>
<p>An end-of-season recap (3-5 minutes) celebrating the season, acknowledging key contributors, and reviewing highlights is one of the most shared pieces of content your club will produce all year. For clubs with an AGM or presentation night, this video is a centrepiece asset.</p>

<h2>Sponsor Showcase Videos</h2>
<p>If your club has sponsors, produce a short video each season featuring each sponsor's branding and contribution in context — players wearing jerseys with sponsor logos, club facilities with signage. This is valuable sponsor reporting content that increases renewal rates.</p>

<h2>Recruitment and Membership Campaigns</h2>
<p>A 60-second "join us" video — showing the fun, the competition, the camaraderie — should run as a social ad campaign at registration season. This is far more effective than a text post asking people to sign up.</p>

<p>Perth Content offers affordable video packages for sports organisations. <a href="contact.html">Talk to us about your club.</a></p>"""
),

# 26
dict(
slug="blog-perth-property-developer-video-marketing",
title="Video Marketing for Perth Property Developers — Selling Before You Build",
description="Perth property developers using video from pre-sale through to handover are achieving faster sales, better-informed buyers, and higher prices. Here is the complete content strategy.",
tag="Industry",
read_time=5,
excerpt="Perth property developers using video from pre-sale through to completion achieve faster sales and better-informed buyers. Here is the complete content strategy from concept to handover.",
hero_sub="Selling off-the-plan is a challenge of imagination — buyers are committing to something that does not yet exist. Video bridges that gap better than any other medium.",
body="""<p>Property development is one of the most video-intensive marketing environments. Developers who invest in a comprehensive video content strategy across the project lifecycle consistently outperform those relying on static renders and brochures.</p>

<h2>Pre-Sales: CGI and Virtual Walkthroughs</h2>
<p>Before a shovel hits the ground, video sells the vision. Architectural CGI walkthroughs (60-90 seconds) allow prospective buyers to virtually walk through apartment layouts, common areas, and the overall building design. Drone footage of the development site, combined with CGI overlays showing the completed development in context, has become standard for Perth off-the-plan marketing.</p>

<h2>Location and Lifestyle Videos</h2>
<p>Buyers are not just buying an apartment or a lot — they are buying into a location and a lifestyle. A location video covering walkability, transport, nearby amenities, and the suburb feel converts undecided buyers who are still weighing multiple areas. These videos work well on YouTube (where "living in [suburb] Perth" searches occur) and in paid social campaigns.</p>

<h2>Construction Progress Updates</h2>
<p>Monthly or quarterly construction progress videos — drone footage of the build, combined with a brief update on milestones — serve several purposes simultaneously. They maintain buyer confidence during the construction period, drive ongoing social media content, and provide content for your Google Business profile and website. Off-the-plan buyers who receive progress updates have significantly lower rescission rates.</p>

<h2>Display Home and Show Suite Videos</h2>
<p>A professionally produced display home video (2-3 minutes) captures fixtures, finishes, natural light, and scale in a way that photos and floorplans cannot. Host it on your project website and send to prospect enquiries who cannot visit in person — particularly relevant for interstate and overseas investors.</p>

<h2>Handover and Testimonial Content</h2>
<p>The settlement period is an emotional high point for buyers. Capture brief testimonials from purchasers as they receive keys. These clips serve as social proof for the next stage release and demonstrate the delivery quality of your product.</p>

<p>Perth Content works with property developers on full project video strategies. <a href="contact.html">Talk to us about your development.</a></p>"""
),

# 27
dict(
slug="blog-video-for-perth-law-firms",
title="Video Marketing for Perth Law Firms — Building Authority and Trust Online",
description="Perth law firms using video are generating more enquiries, better-qualified leads, and stronger brand recognition. Here is what to produce and how to stay within LPCC advertising guidelines.",
tag="Industry",
read_time=5,
excerpt="Perth law firms using video generate more enquiries and better-qualified leads. Here is what to produce, what performs best, and how to stay compliant with legal advertising guidelines.",
hero_sub="Legal services are built on trust. Video lets prospective clients assess your lawyers before the first call — building the confidence that converts enquiries into clients.",
body="""<p>The legal industry in Perth has been slow to adopt video marketing, which makes early movers significantly advantaged. A law firm with a strong video presence stands out against a landscape of identical brochure-style websites and generic practice area descriptions.</p>

<h2>Practice Area Explainer Videos</h2>
<p>Short explainer videos (60-90 seconds) covering common client questions in plain language are the highest-performing legal video format for SEO and organic lead generation. Examples:</p>
<ul>
  <li>"What happens at a property settlement in WA?"</li>
  <li>"How does the Family Law Act divide assets in a divorce?"</li>
  <li>"What is a testamentary trust and do I need one?"</li>
</ul>
<p>These videos rank on YouTube and Google for the exact searches prospective clients are conducting during a stressful period. Being present with clear, helpful answers builds enormous goodwill before the first contact.</p>

<h2>Meet the Lawyer Videos</h2>
<p>A 60-90 second introduction from each solicitor — covering their areas of practice, their background, and their approach to client communication — dramatically improves conversion from website visits to consultation bookings. Clients are not just choosing a firm; they are choosing someone to trust with significant life events.</p>

<h2>Process Walkthrough Videos</h2>
<p>Videos explaining what to expect from a legal process — "What happens during the conveyancing process?", "What is mediation and should I try it before litigation?" — reduce client anxiety, improve appointment quality, and establish authority. They also reduce the time solicitors spend on preliminary education during paid consultation time.</p>

<h2>Compliance Considerations</h2>
<p>Legal advertising in WA is governed by the Legal Profession Act and the Law Society's guidelines. Key rules for video:</p>
<ul>
  <li>Do not make claims about outcomes — "We win cases" or "Best results in Perth" are problematic</li>
  <li>Distinguish clearly between general information and legal advice</li>
  <li>Client testimonials must comply with advertising guidelines — consult the Law Society guidance before using them</li>
</ul>

<p>Perth Content has experience producing legal video content. <a href="contact.html">Talk to us about your firm.</a></p>"""
),

# 28
dict(
slug="blog-how-long-video-editing-takes-perth",
title="How Long Does Video Editing Actually Take? An Honest Guide for Perth Businesses",
description="Perth businesses consistently underestimate post-production time. Here is an honest breakdown of how long video editing takes by project type, complexity, and revision process.",
tag="Production",
read_time=5,
excerpt="Perth businesses consistently underestimate editing time. Here is an honest breakdown by project type — how long editing actually takes, what slows it down, and how to plan for it.",
hero_sub="Editing is where your video is actually made. Most Perth businesses do not understand how long it takes — here is the honest answer, broken down by project type.",
body="""<p>The most common source of frustration between Perth businesses and their video editors is timing. Businesses underestimate how long editing takes; editors underestimate how many revision rounds clients will want. Here is the honest breakdown.</p>

<h2>The Edit Time Formula</h2>
<p>A rough rule of thumb: professional video editing takes 4-10 hours of editing time for every 1 minute of finished video. The wide range reflects the variables — number of cameras, complexity of the edit, amount of colour grading, motion graphics, and revision rounds.</p>

<h2>By Project Type</h2>
<p><strong>Social media clip (15-60 seconds):</strong> 2-4 hours. Simple assembly, music, captions, colour correction. Faster with clean, well-organised footage; longer if extensive search through raw material is required.</p>

<p><strong>Corporate talking head video (2-3 minutes):</strong> 6-12 hours. Multiple cameras, dialogue editing, lower thirds, music, colour grading, usually 2 rounds of revisions.</p>

<p><strong>Event highlight reel (2-4 minutes):</strong> 8-16 hours. Large amount of raw footage to review, music-driven edit, multiple participants to feature, often time-sensitive delivery requirements.</p>

<p><strong>Explainer/brand video with motion graphics (90 seconds):</strong> 15-30 hours. Motion graphics design and animation is time-intensive even for simple elements.</p>

<p><strong>Animated explainer video (60-90 seconds):</strong> 30-60 hours. Script, voiceover sync, frame-by-frame animation, audio mix — animation is the most labour-intensive video format.</p>

<h2>What Slows Editing Down</h2>
<ul>
  <li><strong>Disorganised footage:</strong> Unlabelled files, no shot list, mixed camera cards — an editor spending 2 hours just organising footage is time you are paying for.</li>
  <li><strong>Unclear brief:</strong> "I will know it when I see it" produces endless revision rounds. Clear reference videos and a specific written brief are worth hours of saved edit time.</li>
  <li><strong>Multiple sign-off parties:</strong> Each additional stakeholder in the approval process adds at least one revision round. Nominate a single decision-maker.</li>
  <li><strong>Late-stage structural changes:</strong> Requesting a change to the fundamental structure of the edit (reordering sections, changing the script) after colour grading has started is expensive.</li>
</ul>

<h2>How to Plan for Editing</h2>
<p>Build post-production time into your campaign calendar — not as an afterthought. Plan for 1 week of editing per 1-2 minutes of finished video as a conservative estimate.</p>

<p>Perth Content provides transparent timelines at the brief stage. <a href="contact.html">Talk to us about your project.</a></p>"""
),

# 29
dict(
slug="blog-client-onboarding-video-perth-businesses",
title="Client Onboarding Videos — How Perth Businesses Use Video to Set Expectations and Reduce Churn",
description="Perth businesses using video in their client onboarding process see higher satisfaction, fewer misunderstandings, and better retention. Here is how to build a video onboarding system.",
tag="Strategy",
read_time=5,
excerpt="Perth businesses using video onboarding see higher client satisfaction and better retention. Here is how to build a video welcome and onboarding system that scales without extra staff time.",
hero_sub="The first 30 days of a new client relationship sets the tone for everything that follows. Video onboarding creates clarity, builds trust, and reduces the kind of misunderstandings that end contracts early.",
body="""<p>Many Perth service businesses invest heavily in winning a client, then handle onboarding with a generic welcome email and a PDF. Video onboarding is a low-cost way to dramatically improve the early client experience — and the data shows it pays off in retention.</p>

<h2>The Welcome Video</h2>
<p>A personalised or semi-personalised welcome video from the account manager or director is the highest-impact onboarding video you can send. Sixty to ninety seconds recording on Loom or Zoom — addressing the client by name, welcoming them to the team, and confirming what to expect next — makes a strong first impression that no written email can replicate. Clients who receive a welcome video before the onboarding call report feeling more valued and more confident in their decision.</p>

<h2>Process Walkthrough Videos</h2>
<p>Short videos (2-4 minutes) explaining how your process works — what happens in week one, when the client can expect their first deliverable, how to submit feedback, who to contact for what — eliminate the most common sources of early-stage confusion. These are evergreen assets you produce once and use with every new client.</p>

<h2>How-To Videos for Your Platform or Tools</h2>
<p>If clients interact with a portal, dashboard, CRM, or communication tool, a short screen-recorded walkthrough reduces support burden significantly. A 3-minute screen recording showing clients how to log in, where to find their reports, and how to request changes saves your account managers time on repeat explanations.</p>

<h2>FAQ Videos</h2>
<p>If you answer the same five questions at every new client kickoff call, record video answers to each one and send them proactively in the onboarding sequence. Clients who arrive at the kickoff call with their basic questions already answered are more prepared, more engaged, and more focused on the strategic conversation.</p>

<h2>CRM Integration</h2>
<p>The most scalable onboarding video strategy uses your CRM to trigger video delivery automatically. When a deal is marked as won, your CRM sends the welcome video. After the kickoff call, it sends the process walkthrough. This creates a consistent, professional experience without any manual effort per client.</p>

<p>Perth Content produces professional onboarding video series for service businesses. <a href="contact.html">Ask about our onboarding video packages.</a></p>"""
),

# 30
dict(
slug="blog-perth-influencer-vs-professional-video",
title="Perth Influencer Content vs Professional Video Production — When to Use Each",
description="Influencer and UGC content is not always better than professional video — and professional video is not always better than influencer content. Here is how Perth businesses should decide.",
tag="Strategy",
read_time=5,
excerpt="Influencer and UGC content is not always better than professional video. Here is how Perth businesses should decide which approach to use, and when a hybrid strategy delivers the best results.",
hero_sub="Raw influencer content sometimes outperforms polished production — and sometimes the opposite is true. Here is the framework Perth businesses should use to decide.",
body="""<p>The rise of influencer marketing and user-generated content has created genuine confusion for Perth businesses about where to direct their video budget. Both approaches have merit; neither is universally superior. The right choice depends on your objective, your audience, and your brand positioning.</p>

<h2>What Influencer and UGC Content Does Well</h2>
<ul>
  <li><strong>Authenticity and relatability:</strong> Content that looks like it was made by a real person performing product discovery is perceived as more genuine by audiences primed to distrust advertising.</li>
  <li><strong>Native platform performance:</strong> Influencer-style content is built for platform algorithms and consumption habits. It often outperforms polished ads in raw engagement metrics.</li>
  <li><strong>Reach:</strong> An influencer with an engaged Perth audience can deliver your message to thousands of relevant people quickly.</li>
  <li><strong>Speed and cost:</strong> A brief to a micro-influencer can produce content faster and cheaper than a professional production.</li>
</ul>

<h2>What Professional Video Production Does Well</h2>
<ul>
  <li><strong>Brand integrity:</strong> For premium or B2B brands, low-production-quality content can undermine positioning. Professional production signals investment, stability, and seriousness.</li>
  <li><strong>Complex messages:</strong> If your product requires explanation, demonstration, or a structured narrative, professional editing and production are necessary.</li>
  <li><strong>Long-term assets:</strong> A professionally produced brand video lives on your website, in your pitch decks, and in your sales process for years. Influencer content has a shorter useful life.</li>
  <li><strong>Paid advertising performance:</strong> At scale, professionally produced video ads with strategic creative tend to outperform UGC in conversion-optimised campaigns, particularly for higher-priced products and services.</li>
</ul>

<h2>The Hybrid Approach</h2>
<p>Many Perth businesses find that a hybrid strategy delivers the best overall results:</p>
<ul>
  <li>Use professional production for hero brand content, homepage video, and high-budget paid campaigns</li>
  <li>Use influencer and UGC content for organic social, top-of-funnel awareness, and creative testing</li>
  <li>Use professionally edited UGC — raw influencer footage sent to a professional editor for polishing — as a bridge between the two</li>
</ul>

<h2>Questions to Ask Before Deciding</h2>
<ol>
  <li>What does this video need to achieve?</li>
  <li>Where will it live — organic social, paid ad, website, or sales process?</li>
  <li>What does my target audience trust — polished brands or real voices?</li>
  <li>What are the long-term usage requirements of this content?</li>
</ol>

<p>Perth Content advises businesses on the right production approach for their goals. <a href="contact.html">Talk to us about your strategy.</a></p>"""
),

]  # end POSTS


def fmt_date(d):
    months = ["January","February","March","April","May","June",
              "July","August","September","October","November","December"]
    return f"{d.day} {months[d.month-1]} {d.year}"


def main():
    os.makedirs(DRAFTS_DIR, exist_ok=True)

    with open(QUEUE_PATH, "r", encoding="utf-8") as f:
        queue_data = json.load(f)

    new_entries = []
    for i, p in enumerate(POSTS):
        pub_date = START + timedelta(weeks=i)
        date_display = fmt_date(pub_date)
        date_iso = pub_date.strftime("%Y-%m-%d")

        html = make_html(
            slug=p["slug"],
            title=p["title"],
            description=p["description"],
            tag=p["tag"],
            date_display=date_display,
            date_iso=date_iso,
            read_time=p["read_time"],
            hero_sub=p["hero_sub"],
            body=p["body"],
        )

        path = os.path.join(DRAFTS_DIR, f"{p['slug']}.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"  Written: {p['slug']}.html")

        new_entries.append({
            "slug": p["slug"],
            "title": p["title"],
            "tag": p["tag"],
            "read_time": p["read_time"],
            "excerpt": p["excerpt"],
        })

    queue_data["queue"].extend(new_entries)
    with open(QUEUE_PATH, "w", encoding="utf-8") as f:
        json.dump(queue_data, f, indent=2, ensure_ascii=False)

    print(f"\nDone. {len(new_entries)} posts written to drafts/ and added to queue.json.")
    print(f"Queue now contains {len(queue_data['queue'])} entries.")


if __name__ == "__main__":
    main()
