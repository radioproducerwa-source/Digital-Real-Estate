#!/usr/bin/env python3
import os
OUT = os.path.dirname(os.path.abspath(__file__))

NAV = '''<header class="site-header"><div class="container header-inner">
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
</div></header>'''

FOOTER = '''<section class="cta-section"><div class="container">
  <h2>Ready to Create Stunning Video Content?</h2>
  <p>Get a free quote from Perth Content — we respond within 2 business hours.</p>
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
<script src="js/main.js"></script>'''

def page(p):
    sb = f'''<aside class="post-sidebar">
    <div class="post-sidebar-card"><h4>Get a Free Quote</h4>
      <form action="https://formspree.io/f/mzdodayb" method="POST" data-formspree data-success-id="{p['slug']}-ss">
        <div class="form-row">
          <div><label for="{p['slug']}-n">Name</label><input id="{p['slug']}-n" type="text" name="name" placeholder="Your name" required /></div>
          <div><label for="{p['slug']}-e">Email</label><input id="{p['slug']}-e" type="email" name="email" placeholder="Your email" required /></div>
          <div><label for="{p['slug']}-s">Service</label>
            <select id="{p['slug']}-s" name="service"><option value="">Select&#8230;</option><option>Corporate Video</option><option>Real Estate Video</option><option>Social Media Content</option><option>Explainer Video</option><option>Wedding &amp; Event</option><option>Other</option></select>
          </div>
          <button type="submit" class="btn btn-primary">Get Quote</button>
        </div>
      </form>
      <div id="{p['slug']}-ss" hidden style="display:none;" class="form-success">&#10003; We&#39;ll be in touch shortly!</div>
    </div>
    <div class="post-sidebar-card"><h4>Popular Services</h4><ul>
      <li><a href="corporate-video-perth.html">Corporate Video Perth</a></li>
      <li><a href="real-estate-video-perth.html">Real Estate Video Perth</a></li>
      <li><a href="social-media-video-perth.html">Social Media Video Perth</a></li>
      <li><a href="explainer-video-perth.html">Explainer Video Perth</a></li>
      <li><a href="drone-video-editing-perth.html">Drone Video Editing Perth</a></li>
    </ul></div>
  </aside>'''
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="{p['meta']}" /><meta name="robots" content="index, follow" />
  <title>{p['title']} | Perth Content</title>
  <link rel="canonical" href="https://perthcontent.com/{p['slug']}.html" />
  <meta property="og:title" content="{p['title']}" /><meta property="og:description" content="{p['meta']}" />
  <meta property="og:url" content="https://perthcontent.com/{p['slug']}.html" /><meta property="og:type" content="article" />
  <link rel="preconnect" href="https://fonts.googleapis.com" /><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="css/style.css" />
  <script type="application/ld+json">{{"@context":"https://schema.org","@type":"Article","headline":"{p['title']}","description":"{p['meta']}","datePublished":"{p['date']}","author":{{"@type":"Organization","name":"Perth Content"}},"publisher":{{"@type":"Organization","name":"Perth Content","url":"https://perthcontent.com"}}}}</script>
</head>
<body>
{NAV}
<section class="page-hero"><div class="container">
  <div class="breadcrumb"><a href="index.html">Home</a> &rsaquo; <a href="blog.html">Blog</a> &rsaquo; {p['tag']}</div>
  <h1>{p['title']}</h1><p>{p['excerpt']}</p>
</div></section>
<section class="blog-post"><div class="container blog-post-layout">
  <article class="blog-post-content">
    <div class="post-meta"><span>&#128197; {p['date_display']}</span><span>&#127991; {p['tag']}</span><span>&#9200; {p['read_time']} min read</span></div>
    {p['body']}
  </article>
  {sb}
</div></section>
{FOOTER}
</body>
</html>'''

POSTS = [
  {
    "slug": "blog-how-to-create-brand-video-perth-startup",
    "title": "How to Create a Brand Video for a Perth Startup",
    "tag": "Corporate", "date": "2026-10-19", "date_display": "19 October 2026", "read_time": 5,
    "meta": "A strong brand video opens doors for Perth startups — investor pitches, partnership meetings, and customer acquisition. Here's how to make one on a lean budget.",
    "excerpt": "A strong brand video can open doors for a Perth startup — investor meetings, partnership pitches, and customer acquisition. Here's how to make one that works even on a lean budget.",
    "body": """<p>For a Perth startup, a brand video isn't a luxury — it's a competitive weapon. In investor meetings, pitch competitions, and first sales conversations, a polished brand video communicates legitimacy, vision, and momentum far more powerfully than a slide deck alone. Here's how to create one that works, even with a lean budget.</p>

<h2>What a Startup Brand Video Needs to Do</h2>
<p>A startup brand video serves multiple audiences simultaneously — investors, potential clients, strategic partners, and future team members. It needs to communicate:</p>
<ul>
  <li>The problem you solve (immediately and specifically)</li>
  <li>Your solution and why it's different</li>
  <li>The team behind it (faces, not just names)</li>
  <li>Proof points — early traction, pilot clients, or meaningful validation</li>
  <li>Where you're headed — the vision</li>
</ul>
<p>That's a lot to pack into 2–3 minutes. Ruthless editing is essential.</p>

<h2>The Ideal Length</h2>
<p>For most startup contexts, aim for 90 seconds to 2.5 minutes. Investor attention spans are short. A tight, energetic 2-minute video beats a comprehensive 5-minute one every time. If your video needs to be longer for technical reasons, create two versions: a 90-second "hero" cut and a longer deep-dive version.</p>

<h2>Structure That Works</h2>
<ol>
  <li><strong>Hook (0–10 sec):</strong> Open with the problem statement or a striking visual — not your logo and company name.</li>
  <li><strong>Problem (10–30 sec):</strong> Establish the pain your target market feels. Make them feel seen.</li>
  <li><strong>Solution (30–75 sec):</strong> Introduce your product or service. Show it in action wherever possible — product demos beat descriptions.</li>
  <li><strong>Credibility (75–100 sec):</strong> Early clients, pilot results, team credentials, notable advisers. Anything that says "this is real and it's working."</li>
  <li><strong>Vision and CTA (100–120 sec):</strong> Where are you going? End with energy and a clear call to action.</li>
</ol>

<h2>Lean Budget Approaches</h2>
<p>You don't need $20,000 to produce a compelling startup brand video. Perth Content works with startups regularly on lean budgets:</p>
<ul>
  <li><strong>Script + self-film + professional edit:</strong> You film the interviews and b-roll on a good camera or iPhone Pro. We handle the editing, colour, sound, and graphics. Total cost: $800–$2,000 for a polished 2-minute result.</li>
  <li><strong>Half-day shoot package:</strong> A videographer for half a day covering your office/workspace, team interviews, and product/service footage. Total with editing: $2,500–$4,500.</li>
  <li><strong>Animation for the product section:</strong> If your product is digital or hard to film, a short animated segment (30–45 seconds) can illustrate the product while the rest of the video is live-action. Hybrid productions often look better than pure animation.</li>
</ul>

<h2>Music and Brand Tone</h2>
<p>Music defines the energy of your brand video more than almost any other element. Choose a track that reflects where your brand is going — not where it is today. Startups often benefit from music that feels forward-moving, contemporary, and slightly aspirational.</p>
<p>Always use properly licensed music. Using commercial tracks without licensing is a copyright liability — use royalty-free libraries like Artlist, Epidemic Sound, or Musicbed for commercially safe options.</p>

<h2>Where to Use Your Brand Video</h2>
<ul>
  <li>Pitch deck opener (play before the presentation begins)</li>
  <li>Website homepage hero</li>
  <li>LinkedIn company page</li>
  <li>Investor updates and outreach emails</li>
  <li>Startup competitions and demo day profiles</li>
  <li>PR and media outreach</li>
</ul>

<p>Perth Content specialises in <a href="startup-video-perth.html">startup video production</a> for Perth and WA-based companies. <a href="contact.html">Get a quote for your brand video.</a></p>"""
  },
  {
    "slug": "blog-event-highlight-videos-perth-corporate",
    "title": "Event Highlight Videos — Why Every Perth Corporate Event Needs One",
    "tag": "Events", "date": "2026-10-26", "date_display": "26 October 2026", "read_time": 4,
    "meta": "Your corporate event is over in a day but a highlight video lets you leverage it for months. Here's why Perth companies invest in event video and what a great one looks like.",
    "excerpt": "Your corporate event is over in a day. A well-edited highlight video lets you leverage it for months. Here's why Perth companies are investing in event video — and what a great one looks like.",
    "body": """<p>Your annual conference, product launch, awards night, or team event takes months to plan and thousands to produce — and then it's over in a day. Without a video, your event lives only in the memories of those who attended. With a well-produced highlight video, it becomes a content asset that works for your brand for months.</p>

<h2>What an Event Highlight Video Does for Your Business</h2>
<ul>
  <li><strong>Extends your reach:</strong> Stakeholders, clients, partners, and prospects who couldn't attend can still experience the event. Your audience goes from 300 room attendees to potentially thousands of online viewers.</li>
  <li><strong>Demonstrates scale and credibility:</strong> A polished event video signals organisational sophistication — the kind of thing that impresses enterprise clients and prospective partners.</li>
  <li><strong>Creates evergreen content:</strong> Conference highlights, keynote excerpts, and testimonial moments filmed at an event can fuel your social media calendar for 6–12 weeks.</li>
  <li><strong>Promotes next year's event:</strong> The most effective marketing tool for your next conference or event is a compelling highlight reel from the last one.</li>
</ul>

<h2>What Goes Into a Great Event Highlight Video</h2>
<p>The best event highlight videos feel energetic, authentic, and emotionally resonant — they capture the atmosphere and the moments that made the event worth attending.</p>
<p>Key elements:</p>
<ul>
  <li><strong>Arrival and atmosphere:</strong> The energy of guests arriving, networking, and settling in — this establishes the scale of the event.</li>
  <li><strong>Speaker highlights:</strong> The best 15–30 seconds from each keynote or presentation. These anchor the narrative and demonstrate content quality.</li>
  <li><strong>Crowd reactions:</strong> Audience engagement, laughter, applause, and genuine reactions are gold. These moments make the event feel alive.</li>
  <li><strong>Candid moments:</strong> Conversations between attendees, behind-the-scenes preparation, informal interactions — authenticity beats perfection.</li>
  <li><strong>Closing energy:</strong> The end of the event — awards, celebrations, final moments — gives the video its emotional climax.</li>
</ul>

<h2>Length and Format</h2>
<ul>
  <li><strong>Social highlight cut:</strong> 60–90 seconds for Instagram, LinkedIn, and Facebook — high energy, music-driven</li>
  <li><strong>Full highlight reel:</strong> 3–5 minutes for your website, YouTube, and event follow-up email</li>
  <li><strong>Speaker excerpts:</strong> Individual 2–4 minute clips of each keynote, useful for speakers to share on their own channels</li>
</ul>

<h2>Planning for the Video</h2>
<p>Great event video requires pre-planning, not just showing up on the day:</p>
<ul>
  <li>Brief your videographer on the run sheet — they need to know when key moments will happen</li>
  <li>Identify 3–5 attendees to interview on camera for 60–90 second testimonials during the event</li>
  <li>Ensure your venue has adequate lighting for filming (many conference venues have poor lighting for video)</li>
  <li>Reserve a quiet corner for interview setups</li>
  <li>Clarify music licensing — conference highlight videos for commercial use require properly licensed music</li>
</ul>

<h2>Cost Ranges for Perth Event Video</h2>
<ul>
  <li>Single videographer, half-day event, social highlight only: $800–$1,500</li>
  <li>Single videographer, full-day event, social + full highlight: $1,500–$2,500</li>
  <li>2-camera crew, full-day event, multiple deliverables: $3,000–$6,000</li>
</ul>

<p>See our <a href="event-highlight-video-perth.html">event highlight video service</a> for Perth corporate events. <a href="contact.html">Get a quote for your upcoming event.</a></p>"""
  },
  {
    "slug": "blog-video-captions-subtitles-perth-businesses",
    "title": "Video Captions and Subtitles — Why They Matter for Perth Businesses",
    "tag": "Social Media", "date": "2026-11-02", "date_display": "2 November 2026", "read_time": 4,
    "meta": "85% of social video is watched on mute. Captions are no longer optional for Perth businesses — they're essential for reach, accessibility, and engagement.",
    "excerpt": "85% of social video is watched on mute. Captions and subtitles aren't optional anymore — they're essential. Here's how Perth businesses should be using them across every platform.",
    "body": """<p>Here's a fact that reshapes how you should think about every business video you produce: 85% of social media video is watched without sound. On Facebook, Instagram, LinkedIn, and TikTok, the majority of your viewers have their phone on silent, their headphones not in, or they're in a public place. If your video communicates only through audio, you're losing most of your audience before they've had a chance to engage.</p>

<h2>Captions vs Subtitles: What's the Difference?</h2>
<ul>
  <li><strong>Subtitles</strong> translate spoken dialogue into text — traditionally used for foreign language content.</li>
  <li><strong>Captions</strong> transcribe spoken dialogue for viewers who can't or choose not to listen — including sound effects and speaker identification for accessibility purposes.</li>
</ul>
<p>For most Perth business video purposes, "captions" is the correct term — you're transcribing your own content for muted viewers, not translating it.</p>

<h2>Why Captions Are Non-Negotiable in 2025</h2>

<h3>1. Most Social Video Is Watched on Mute</h3>
<p>This applies to Facebook (85% muted), Instagram (60%+ muted), LinkedIn (many users view from offices without headphones), and even TikTok. If your video opens with someone talking but no text appears, muted viewers scroll immediately.</p>

<h3>2. Captions Increase Completion Rates</h3>
<p>Videos with captions see 12% higher watch time than those without, according to Facebook research. When viewers can follow along without sound, they're far more likely to watch to the end — which tells the algorithm your content is high quality.</p>

<h3>3. Accessibility and Legal Compliance</h3>
<p>Captions make your content accessible to Deaf and hard-of-hearing viewers. For Australian businesses producing public-facing content, accessibility is increasingly both an ethical obligation and, in some contexts, a legal requirement.</p>

<h3>4. SEO and Searchability</h3>
<p>YouTube indexes closed captions as text content, making captioned videos more discoverable in search. Uploading a proper caption file (SRT/VTT) improves your YouTube SEO with zero additional content effort.</p>

<h2>Caption Styles for Social Media</h2>
<p>Not all captions are created equal. For social media in 2025, the most effective style is:</p>
<ul>
  <li><strong>Large, bold, high-contrast text</strong> — readable on a small phone screen without squinting</li>
  <li><strong>Word-by-word highlighting</strong> (karaoke style) — keeps eyes engaged with the text rhythm</li>
  <li><strong>Short phrases per screen</strong> — 3–5 words max, not full sentences</li>
  <li><strong>Branded colours</strong> — captions using your brand palette reinforce visual identity</li>
</ul>
<p>CapCut, Premiere Pro, and DaVinci Resolve all support animated captions. For social content, animated word-by-word captions consistently outperform static subtitle-style text.</p>

<h2>How Perth Businesses Should Implement Captions</h2>
<ul>
  <li><strong>Social Reels and TikToks:</strong> Animated captions burned into the video file (not closed captions) — they display automatically without viewer action</li>
  <li><strong>YouTube:</strong> Upload an SRT caption file separately — allows viewers to toggle them and improves SEO</li>
  <li><strong>LinkedIn native video:</strong> Burned-in captions or LinkedIn's auto-caption feature (check accuracy before publishing)</li>
  <li><strong>Website video:</strong> Closed captions with a visible CC toggle for accessibility compliance</li>
</ul>

<h2>Auto-Captions: Useful but Not Reliable</h2>
<p>YouTube, LinkedIn, TikTok, and Instagram all offer automatic captions. They're remarkably accurate for clear speech — but they make errors with industry jargon, proper nouns, and Australian accents. Always review auto-generated captions before publishing. An uncorrected captioning error on a business video is embarrassing at best, misleading at worst.</p>

<p>Perth Content includes professional captioning on all social media video packages. <a href="contact.html">Get a quote for your next video project.</a></p>"""
  },
  {
    "slug": "blog-linkedin-video-grow-perth-business",
    "title": "How to Use LinkedIn Video to Grow Your Perth Business",
    "tag": "Social Media", "date": "2026-11-09", "date_display": "9 November 2026", "read_time": 5,
    "meta": "LinkedIn video gets 3x more reach than static posts. Here's a practical guide for Perth professionals — what to post, how often, and what drives enquiries on LinkedIn.",
    "excerpt": "LinkedIn video gets 3x more reach than static posts. Here's a practical guide for Perth professionals and businesses — what to post, how often, and what actually drives enquiries on LinkedIn.",
    "body": """<p>LinkedIn is Perth's most valuable B2B marketing channel — and video is the highest-performing content format on the platform. Native LinkedIn video receives three times more reach than static posts, and video comments drive conversations that text posts rarely generate. Yet most Perth businesses and professionals either don't post video on LinkedIn, or they post the wrong type. Here's what actually works.</p>

<h2>Why LinkedIn Video Is Different</h2>
<p>LinkedIn audiences are professional, time-poor, and sceptical of overt sales content. What performs on Instagram (aspirational lifestyle, trending audio) rarely works on LinkedIn. What works on LinkedIn is insight, expertise, and authenticity — ideally delivered in a format that respects a professional's time.</p>

<h2>What Types of Video Perform on LinkedIn</h2>

<h3>Thought Leadership and Opinion Pieces</h3>
<p>Your take on an industry development, a counterintuitive view on a common practice, or a lesson from a client project. These perform best when you have a genuine perspective — not just restating conventional wisdom. Keep to 60–90 seconds.</p>

<h3>Behind-the-Scenes Process Videos</h3>
<p>"Here's how we approach [X]" content demonstrates expertise while feeling transparent rather than promotional. Perth professionals respond strongly to seeing how their peers work.</p>

<h3>Client Results and Case Studies</h3>
<p>Brief video case studies — "we helped a Subiaco café solve X by doing Y, and here's what happened" — combine proof of performance with educational content. Far more persuasive than written case studies.</p>

<h3>Short Educational Tips</h3>
<p>A 30–60 second practical tip relevant to your target audience. These are highly shareable and establish expertise efficiently. "3 questions to ask before hiring a video editor" or "Why most Perth business websites don't convert" — specific, actionable, valuable.</p>

<h3>Event and Conference Coverage</h3>
<p>A 60–90 second highlight from a conference you attended or spoke at, with your key takeaway. These perform well on LinkedIn because they signal active professional development.</p>

<h2>Format Specifications for LinkedIn Video</h2>
<ul>
  <li><strong>Aspect ratio:</strong> Square (1:1) or portrait (4:5) for mobile-first feed; 16:9 landscape for professional content</li>
  <li><strong>Length:</strong> 60–90 seconds for organic posts; up to 10 minutes for educational deep-dives</li>
  <li><strong>File format:</strong> MP4, H.264</li>
  <li><strong>Captions:</strong> Essential — many LinkedIn users watch at work without headphones</li>
  <li><strong>Hook in first 3 seconds:</strong> LinkedIn autoplay is silent — your opening visual must stop the scroll</li>
</ul>

<h2>Posting Frequency and Strategy</h2>
<ul>
  <li><strong>Individual / personal brand:</strong> 2–3 videos per week is the sweet spot for algorithmic reach. Consistency matters more than frequency.</li>
  <li><strong>Company page:</strong> 1–2 videos per week; company pages get less organic reach than personal profiles — use them to amplify content your team members create.</li>
  <li><strong>Best time to post:</strong> Tuesday–Thursday, 7–9am AWST (before the Perth workday begins) or 12–1pm (lunch break scrolling)</li>
</ul>

<h2>What Drives Enquiries on LinkedIn</h2>
<p>LinkedIn video builds awareness and trust over time. Direct enquiries rarely come from a single video — they come from consistent presence over weeks and months. The pattern is: viewer sees several of your videos → views your profile → connects → reaches out when a need arises.</p>
<p>Calls to action on LinkedIn video should be light-touch: "Happy to share more in the comments" or "DM me if you'd like to discuss" outperforms "Book a call now" on organic content.</p>

<p>Perth Content's <a href="linkedin-video-perth.html">LinkedIn video service</a> covers scripting, filming, editing, and captioning. <a href="contact.html">Get a quote today.</a></p>"""
  },
  {
    "slug": "blog-best-video-editing-software-2025",
    "title": "Best Video Editing Software in 2025 — A Perth Professional's Guide",
    "tag": "How-To", "date": "2026-11-16", "date_display": "16 November 2026", "read_time": 5,
    "meta": "DaVinci Resolve, Premiere Pro, Final Cut, CapCut — which video editing software should Perth businesses and creators use in 2025? Compared by use case and budget.",
    "excerpt": "DaVinci Resolve, Premiere Pro, Final Cut, CapCut — which editing software should Perth businesses and creators be using? We compare the top options for 2025 by use case and budget.",
    "body": """<p>The video editing software landscape has never been more capable — or more overwhelming. Whether you're a Perth business owner wanting to handle your own social content, or a marketer evaluating what your contracted editor uses, understanding the options helps you make smarter decisions. Here's the 2025 breakdown.</p>

<h2>Adobe Premiere Pro</h2>
<p><strong>Best for:</strong> Agency and studio work, complex multi-platform projects, teams<br/>
<strong>Cost:</strong> ~$65/month (Adobe Creative Cloud subscription)<br/>
<strong>Platform:</strong> Windows and Mac</p>
<p>Premiere Pro is the industry standard for a reason. Its integration with After Effects (motion graphics), Audition (audio), and the broader Adobe ecosystem makes it unmatched for complex professional projects. The AI-powered tools added in 2024–2025 — including auto-reframe, speech-to-text captions, and generative fill — have made repetitive tasks dramatically faster.</p>
<p><strong>Verdict:</strong> The right choice for professional editors and agencies handling diverse client work. The subscription cost is the main barrier for small operators.</p>

<h2>DaVinci Resolve</h2>
<p><strong>Best for:</strong> Colour-critical work, film/documentary, anyone wanting professional results for free<br/>
<strong>Cost:</strong> Free (Studio version: ~$500 one-time license)<br/>
<strong>Platform:</strong> Windows, Mac, Linux</p>
<p>DaVinci Resolve's free version is genuinely professional-grade — used in Hollywood feature film production. Its colour grading tools are the best in the industry at any price point. The 2025 AI features include magic mask, super scale upscaling, and voice isolation. The interface has a steeper learning curve than Premiere Pro, but the no-subscription cost makes it extraordinary value.</p>
<p><strong>Verdict:</strong> The best choice for cost-conscious professionals, especially those where colour quality matters. Also the smart choice for editors who want to avoid ongoing subscription costs.</p>

<h2>Apple Final Cut Pro</h2>
<p><strong>Best for:</strong> Mac-based editors with high-volume social content workflows<br/>
<strong>Cost:</strong> ~$500 one-time purchase (Mac only)<br/>
<strong>Platform:</strong> Mac only</p>
<p>Final Cut Pro is extraordinarily fast on Apple Silicon Macs — processing and rendering speeds that leave Premiere Pro behind on the same machine. Its magnetic timeline and streamlined workflow make it excellent for editors who produce high volumes of social content. The lack of Windows support and After Effects integration limits it for agency use.</p>
<p><strong>Verdict:</strong> Ideal for Mac-only freelancers with a social-first content workflow. Not suitable for Windows users or complex motion graphics work.</p>

<h2>CapCut (Pro)</h2>
<p><strong>Best for:</strong> Social media content, TikTok and Instagram Reels, beginners<br/>
<strong>Cost:</strong> Free with paid Pro tier (~$15/month)<br/>
<strong>Platform:</strong> iOS, Android, Web, Windows</p>
<p>CapCut has become the dominant tool for social-first video editing — especially among creators producing TikTok and Reels content. Its AI auto-captions, trending effect library, and direct social publishing make it remarkably fast for high-volume social content. It lacks the depth for complex productions but is genuinely excellent for its target use case.</p>
<p><strong>Verdict:</strong> The right tool for social media content creators and businesses managing their own Reels. Not a replacement for Premiere Pro or DaVinci Resolve for professional client work.</p>

<h2>iMovie</h2>
<p><strong>Best for:</strong> Complete beginners, very simple edits, iPhone/iPad users<br/>
<strong>Cost:</strong> Free (Apple devices only)</p>
<p>iMovie is a perfectly serviceable starting point for someone who has never edited video before. It handles basic cuts, transitions, and titles. Its limitations become apparent quickly — no colour grading tools, limited audio control, basic effects. Think of it as training wheels for Final Cut Pro.</p>

<h2>Which Should Your Perth Business Use?</h2>
<ul>
  <li><strong>Running your own social media content:</strong> CapCut Pro</li>
  <li><strong>Occasional editing, cost-sensitive:</strong> DaVinci Resolve (free)</li>
  <li><strong>Mac user, high-volume content:</strong> Final Cut Pro</li>
  <li><strong>Complex corporate or client projects:</strong> Adobe Premiere Pro</li>
  <li><strong>Colour-critical work:</strong> DaVinci Resolve Studio</li>
</ul>

<p>Of course, the simplest option is to outsource your editing entirely to Perth Content — we use professional-grade tools and return polished results with 48-hour turnaround. <a href="contact.html">Get a quote today.</a></p>"""
  },
  {
    "slug": "blog-video-ads-perth-facebook-instagram",
    "title": "How to Use Video Ads on Facebook and Instagram for Perth Businesses",
    "tag": "Social Media", "date": "2026-11-23", "date_display": "23 November 2026", "read_time": 5,
    "meta": "Video ads on Facebook and Instagram convert higher than static ads for Perth businesses — when built for the platform. Here's what works for video ad creative in 2025.",
    "excerpt": "Video ads on Facebook and Instagram convert at a higher rate than static ads — but only when they're built for the platform. Here's what Perth businesses need to know about video ad creative in 2025.",
    "body": """<p>Facebook and Instagram video ads consistently outperform static image ads on click-through rate, engagement, and conversion rate — but only when they're produced with platform-specific intent. A corporate brand video dumped into an ad account will perform poorly. A 15-second vertical video built specifically for mobile social will outperform it every time. Here's what Perth businesses need to know.</p>

<h2>The Mobile-First Reality</h2>
<p>Over 90% of Facebook and Instagram ad impressions are delivered on mobile devices. This fundamentally changes how you should approach video ad creative:</p>
<ul>
  <li>Vertical (9:16) or square (1:1) framing — not landscape 16:9</li>
  <li>Text and key visuals centred in the safe zone (not near edges)</li>
  <li>Large, readable text overlay — don't assume viewers will zoom in</li>
  <li>Sound-off by default — your video must communicate value without audio</li>
</ul>

<h2>The First 3 Seconds Are Everything</h2>
<p>Meta's data consistently shows that 65% of ad video viewers who watch the first 3 seconds continue watching to 10 seconds. Those who don't watch the first 3 seconds are lost. Your hook must be immediate:</p>
<ul>
  <li>Start with your most compelling visual, not a logo animation or brand intro</li>
  <li>Use text overlay to establish value immediately ("Perth tradespeople save $400/month with...")</li>
  <li>Show the end result first — curiosity gap works better than chronological story structure in ads</li>
  <li>Pattern interrupt: something unexpected, colourful, or motion-heavy that breaks the feed scroll</li>
</ul>

<h2>Optimal Length by Placement</h2>
<ul>
  <li><strong>Facebook/Instagram Feed:</strong> 15–30 seconds for awareness; up to 60 seconds for retargeting warm audiences</li>
  <li><strong>Stories:</strong> 6–15 seconds (full-screen immersive, expires after 24 hours)</li>
  <li><strong>Reels placement:</strong> 15–30 seconds, vertical, feels organic not ad-like</li>
  <li><strong>In-stream (mid-roll):</strong> 6–15 seconds — short enough to be tolerated, long enough to land a message</li>
</ul>

<h2>The Best Perth Video Ad Formats</h2>

<h3>Problem/Solution</h3>
<p>Open with the pain (3 sec), introduce the product/service as the solution (10 sec), show a result (5 sec), CTA (2 sec). Clean, direct, effective for bottom-of-funnel.</p>

<h3>Testimonial Cut</h3>
<p>A 15–20 second cut of a real client talking about a specific result. Authentic faces convert better than polished corporate production for social ads. Add your logo and CTA overlay.</p>

<h3>Before/After</h3>
<p>Split screen or sequential before/after demonstration. Works for physical products, real estate, fitness, food, renovation — anything with a visual transformation.</p>

<h3>Behind the Scenes</h3>
<p>Showing your process builds trust at a lower cost-per-click than direct sales creative. Use for top-of-funnel awareness campaigns targeting cold audiences.</p>

<h2>Captions Are Mandatory</h2>
<p>With 85% of social video viewed without sound, your ad without captions is communicating nothing to the majority of viewers. Captions should be high-contrast, large, and styled to match your brand. Perth Content adds captions to all video ad deliverables as standard.</p>

<h2>Testing and Iteration</h2>
<p>The best video ads are discovered through testing, not predicted. Run at least 3 creative variations in every campaign — different hooks, different lengths, different CTA copy. Meta's algorithm will allocate spend to the best performer. Most winning ad creative comes from the 2nd or 3rd variant, not the one you were most confident in.</p>

<p>Perth Content produces video ad creative for Facebook and Instagram campaigns. <a href="contact.html">Get a quote for your next campaign.</a></p>"""
  },
  {
    "slug": "blog-product-video-perth-ecommerce",
    "title": "Product Video for Perth eCommerce — How to Sell More with Video",
    "tag": "Social Media", "date": "2026-11-30", "date_display": "30 November 2026", "read_time": 5,
    "meta": "Product videos increase eCommerce conversions by up to 80%. Here's how Perth retailers and online stores can use video to sell more on Shopify, Amazon, and social.",
    "excerpt": "Product videos increase conversion rates by up to 80% on eCommerce listings. Here's how Perth retailers and online stores can use video to sell more — on Shopify, Amazon, and social.",
    "body": """<p>A product image shows what something looks like. A product video shows what it does, how it feels, and why someone should buy it. For Perth eCommerce businesses, product video isn't just a nice-to-have — it's one of the highest-ROI investments in your marketing stack. Here's why, and how to do it right.</p>

<h2>The Numbers Behind Product Video</h2>
<ul>
  <li>Product pages with video convert at up to 80% higher rates than those without</li>
  <li>74% of consumers say they're more likely to buy a product after watching a video about it</li>
  <li>Return rates drop by up to 25% when products have accurate video demonstrations — because buyers know exactly what they're getting</li>
  <li>Amazon product listings with video see significantly higher conversion rates and BSR (Best Seller Rank) improvement</li>
</ul>

<h2>Types of Product Video That Sell</h2>

<h3>Product Demo Video</h3>
<p>Shows the product in use, from multiple angles, demonstrating its key features and benefits. This is the most common and most effective format. Keep it under 60 seconds for eCommerce — buyers are in purchase mode, not learning mode.</p>

<h3>Lifestyle Video</h3>
<p>Shows the product in its natural context — a skincare product on a bathroom shelf, a kitchen gadget being used in a real kitchen, an outdoor product in an actual outdoor setting. Lifestyle video sells aspiration, not just functionality. Perth-specific lifestyle content (local beaches, coffee culture, outdoor living) resonates strongly with WA buyers.</p>

<h3>Unboxing and Reveal</h3>
<p>High-performing on social media and YouTube. The unboxing experience can be as important as the product itself — particularly for gift items, luxury products, and subscription boxes.</p>

<h3>360° or Rotational Video</h3>
<p>Allows viewers to see the product from every angle — approximating the in-store experience. Particularly valuable for jewellery, shoes, electronics, and homewares where detail matters.</p>

<h3>Comparison Video</h3>
<p>"Our product vs the competition" videos, when done fairly and factually, are powerful conversion tools — especially if your product genuinely outperforms alternatives on specific features.</p>

<h2>Platform-Specific Considerations</h2>
<ul>
  <li><strong>Shopify product pages:</strong> MP4 video, autoplay muted loop on desktop, 16:9 or 1:1 aspect ratio. Keep under 30 seconds for most categories.</li>
  <li><strong>Amazon:</strong> Strict requirements — minimum 1280x720, H.264, under 5GB. Product should be clearly visible for the first 5 seconds. No competitive product names or pricing.</li>
  <li><strong>Instagram Shopping:</strong> Square or vertical format, under 60 seconds, captioned for muted viewing.</li>
  <li><strong>Facebook Marketplace / Shops:</strong> Native video performs better than YouTube embeds. Keep under 30 seconds.</li>
</ul>

<h2>DIY vs Professional for Product Video</h2>
<p>Unlike talking head or corporate video, many product videos can be filmed to a professional standard on a phone — with the right lighting, background, and basic stabilisation. Consider:</p>
<ul>
  <li><strong>DIY with professional editing:</strong> Film your product at home with a lightbox or simple white sweep. Send footage to Perth Content for professional editing, colour correction, and music. Total cost: $200–$500 per product video.</li>
  <li><strong>Full production:</strong> Lifestyle shoots with a photographer/videographer and styled sets. Better results, higher investment — suited to hero products or campaign launches ($800–$3,000+).</li>
</ul>

<p>Perth Content's <a href="product-video-perth.html">product video service</a> covers both editing-only and full production. <a href="contact.html">Get a quote for your product range.</a></p>"""
  },
  {
    "slug": "blog-how-to-measure-video-marketing-roi-perth",
    "title": "How to Measure Video Marketing ROI for Your Perth Business",
    "tag": "Strategy", "date": "2026-12-07", "date_display": "7 December 2026", "read_time": 5,
    "meta": "Tracking video marketing ROI for Perth businesses — the metrics that matter, how to attribute leads to video, and how to prove your video investment is working.",
    "excerpt": "How do you know if your video content is working? This guide covers the metrics Perth businesses should be tracking — from views and watch time to lead attribution and sales conversion.",
    "body": """<p>Producing video without measuring its impact is like running ads without tracking clicks. You're spending, but you don't know what's working. For Perth businesses investing in video content — whether it's testimonials, Reels, YouTube, or website video — measuring ROI properly is what separates a strategic content investment from an expensive hobby.</p>

<h2>The Challenge of Video Attribution</h2>
<p>Video ROI is harder to measure than paid ads because the path from "watched video" to "became a client" is rarely linear. Someone might watch three of your LinkedIn videos over two weeks, visit your website, read your about page, then call you a month later. That sale was influenced by video, but Google Analytics might attribute it to "direct" traffic.</p>
<p>This means video ROI often requires a mix of hard data and smart inference — not just a single dashboard number.</p>

<h2>Metrics by Channel</h2>

<h3>Website Video Metrics</h3>
<ul>
  <li><strong>Video play rate:</strong> What % of page visitors click play? Below 20% suggests a weak thumbnail or placement issue.</li>
  <li><strong>Watch-through rate:</strong> What % of viewers watch to 50%? 75%? 100%? Declining watch-through highlights where your content loses viewers.</li>
  <li><strong>Time on page:</strong> Pages with video should show significantly higher average session duration than equivalent pages without video. Track this in GA4.</li>
  <li><strong>Conversion rate on video pages:</strong> Compare conversion rates (enquiry form completions, phone call clicks) between pages with and without video.</li>
</ul>

<h3>YouTube Metrics</h3>
<ul>
  <li><strong>Average view duration:</strong> How long do viewers watch before leaving? Aim for 50%+ on educational content.</li>
  <li><strong>Click-through rate (CTR):</strong> What % of impressions result in a click? Industry average is 2–10%.</li>
  <li><strong>Impressions to watch time:</strong> The flywheel that drives YouTube growth — more impressions → more watches → more channel authority → more impressions.</li>
  <li><strong>Traffic to website:</strong> Track clicks from YouTube to your website in GA4 via UTM links in your video descriptions.</li>
</ul>

<h3>Social Media Video Metrics</h3>
<ul>
  <li><strong>Reach vs engagement:</strong> Reach tells you how many people saw it; engagement (comments, shares, saves) tells you how many cared.</li>
  <li><strong>Profile visits from video:</strong> Instagram and TikTok show how many viewers clicked to your profile after watching — a strong intent signal.</li>
  <li><strong>Link clicks:</strong> For videos with links in bio or caption, track how many viewers clicked through to your website.</li>
  <li><strong>Follower growth:</strong> Measure new followers attributable to video-heavy periods vs non-video periods.</li>
</ul>

<h2>How to Track Video-Influenced Leads</h2>
<ul>
  <li><strong>Ask the question:</strong> Add "How did you find us?" to your enquiry form. Many leads will specifically mention watching a video.</li>
  <li><strong>UTM parameters:</strong> Add UTM tracking to any link in video descriptions, social bios, or pinned comments. These appear in GA4 as trackable traffic sources.</li>
  <li><strong>CRM notes:</strong> Train your sales team to record what content a lead engaged with during discovery conversations.</li>
  <li><strong>Before/after analysis:</strong> Measure your average monthly enquiry volume for 90 days before adding video content, and 90 days after. The difference provides a directional ROI estimate.</li>
</ul>

<h2>A Practical ROI Framework</h2>
<p>Once you have even rough data, apply this calculation:</p>
<ol>
  <li><strong>Monthly video-influenced leads:</strong> e.g. 5 leads per month mentioning video or attributed via UTM</li>
  <li><strong>Close rate:</strong> e.g. 30% → 1.5 clients per month</li>
  <li><strong>Average client value:</strong> e.g. $2,500</li>
  <li><strong>Monthly revenue from video:</strong> 1.5 × $2,500 = $3,750</li>
  <li><strong>Video investment (amortised):</strong> $3,000 video ÷ 12 months = $250/month</li>
  <li><strong>ROI:</strong> ($3,750 - $250) ÷ $250 = 1400%</li>
</ol>
<p>Even with conservative assumptions, video ROI is typically exceptional — because the asset keeps working long after the production cost is paid off.</p>

<h2>The Long Game</h2>
<p>Video ROI compounds. A testimonial produced today may still be converting leads two years from now. YouTube videos accumulate views and authority over months and years. The businesses that measure video ROI most accurately are those that track it consistently over 12+ months — not those looking for results after a single upload.</p>

<p>Perth Content helps businesses build video content strategies that are measurable from the start. <a href="contact.html">Talk to us about your video goals.</a></p>"""
  },
]

for p in POSTS:
    html = page(p)
    path = os.path.join(OUT, f"{p['slug']}.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✓ {p['slug']}.html")

print(f"\nGenerated {len(POSTS)} files.")
