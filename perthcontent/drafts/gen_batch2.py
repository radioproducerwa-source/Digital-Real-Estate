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
    "slug": "blog-roi-video-content-perth-businesses",
    "title": "The ROI of Video Content for Perth Businesses",
    "tag": "Strategy", "date": "2026-08-31", "date_display": "31 August 2026", "read_time": 6,
    "meta": "Is video worth the investment? We break down conversion rates, reach, and lead quality metrics to help Perth businesses calculate their video content ROI.",
    "excerpt": "Is video worth the investment? We look at the numbers — conversion rates, time on site, social reach, and sales velocity — to help Perth businesses calculate the return on video content.",
    "body": """<p>Video is a significant investment for most Perth small businesses. Before committing the budget, it's fair to ask: what's the actual return? The challenge is that video ROI is harder to measure than a paid ad click — but it's very real. Here's how to think about it, measure it, and optimise for it.</p>

<h2>The Metrics That Matter</h2>
<p>Video ROI shows up across three areas of your business:</p>

<h3>Website Performance</h3>
<ul>
  <li><strong>Time on page:</strong> Pages with video see 88% longer average visit duration. More time means more trust built.</li>
  <li><strong>Bounce rate:</strong> Video reduces bounce rate by giving visitors a reason to stay.</li>
  <li><strong>Conversion rate:</strong> Landing pages with video convert at up to 80% higher rates than text-only pages. For a page generating 10 enquiries per month, that could mean 18 enquiries — with no extra traffic spend.</li>
</ul>

<h3>Social Media Performance</h3>
<ul>
  <li><strong>Organic reach:</strong> Video posts get 48% more views than static posts on Facebook and Instagram. More reach = more brand awareness without increased ad spend.</li>
  <li><strong>Engagement rate:</strong> Video generates 1200% more shares than text and image content combined.</li>
  <li><strong>Click-through rate:</strong> Video ads on Facebook and Instagram consistently outperform static image ads by 20–30%.</li>
</ul>

<h3>Sales and Lead Quality</h3>
<ul>
  <li><strong>Lead quality:</strong> Prospects who've watched your explainer video or testimonials arrive more informed and more convinced. Sales calls are shorter and close rates are higher.</li>
  <li><strong>Deal velocity:</strong> Educated prospects make decisions faster. Video does the objection-handling before the sales conversation starts.</li>
</ul>

<h2>A Simple ROI Calculation</h2>
<p>Here's a framework Perth businesses can apply:</p>
<ol>
  <li>Identify your average client lifetime value (e.g. $3,000)</li>
  <li>Estimate how many additional enquiries per month the video drives (e.g. 3 extra enquiries from improved landing page conversion)</li>
  <li>Apply your close rate (e.g. 30% → 1 additional client per month)</li>
  <li>Calculate monthly revenue increase: 1 × $3,000 = $3,000/month</li>
  <li>Divide your video investment by monthly increase: $2,000 video ÷ $3,000/month = payback in under 1 month</li>
</ol>
<p>Even conservative assumptions produce strong ROI — especially because video keeps working for months and years after production.</p>

<h2>The Compounding Effect</h2>
<p>Unlike a paid ad that stops the moment you stop paying, video content compounds over time. A well-optimised YouTube video can drive search traffic for years. A testimonial on your homepage builds trust for every visitor indefinitely. Your video investment in 2025 can still be generating leads in 2028.</p>

<h2>How to Track Your Video ROI</h2>
<ul>
  <li><strong>UTM links:</strong> Add UTM parameters to any link included in your video descriptions (YouTube, social bios) to track traffic in Google Analytics.</li>
  <li><strong>Enquiry source tracking:</strong> Ask leads "how did you find us?" — many will mention watching a video.</li>
  <li><strong>Before/after comparison:</strong> Track your website conversion rate for 30 days before adding a video, and 30 days after.</li>
  <li><strong>Social analytics:</strong> Monitor reach and engagement on video posts vs non-video posts in your native platform analytics.</li>
</ul>

<p>The businesses most disappointed by their video investment are usually those that produced one video, posted it once, and expected magic. Video ROI compounds with <em>consistency</em> — regular content builds audiences that compound over time.</p>
<p>Perth Content helps businesses build sustainable video content strategies. <a href="contact.html">Talk to us about your goals.</a></p>"""
  },
  {
    "slug": "blog-how-to-choose-video-editor-perth",
    "title": "How to Choose a Video Editor in Perth",
    "tag": "How-To", "date": "2026-09-07", "date_display": "7 September 2026", "read_time": 5,
    "meta": "With dozens of video editors in Perth, how do you pick the right one? This guide covers what to look for, what to ask, and which red flags to avoid.",
    "excerpt": "With dozens of video editors and production companies in Perth, how do you find the right one for your project? This guide covers what to look for, what to ask, and what red flags to avoid.",
    "body": """<p>A quick Google search for "video editor Perth" returns dozens of results — freelancers, boutique agencies, production companies, and content studios. How do you find the right one without getting burned? Here's what experienced buyers look for when hiring a video editor in Perth.</p>

<h2>Freelancer vs Agency vs Marketplace</h2>
<p>Your first decision is what type of provider to work with:</p>
<ul>
  <li><strong>Freelance editor:</strong> Typically lower cost, direct communication, but capacity can be limited. Best for single projects or ongoing relationships with a trusted individual.</li>
  <li><strong>Production agency:</strong> Full team (producer, shooter, editor), higher cost, more scalable. Best for large or complex productions that require multiple specialists.</li>
  <li><strong>Video marketplace (like Perth Content):</strong> Combines the cost efficiency of freelancers with the reliability of a managed service. Fixed pricing, vetted editors, fast turnaround. Best for businesses that need consistent, recurring output.</li>
</ul>

<h2>What to Look for in a Portfolio</h2>
<p>Portfolio review is the most important step. Look for:</p>
<ul>
  <li><strong>Style match:</strong> Does their editing style match the tone you want? A wedding videographer's portfolio won't tell you much about their corporate work.</li>
  <li><strong>Industry experience:</strong> Have they worked in your industry? Real estate videos have different conventions to restaurant content or corporate explainers.</li>
  <li><strong>Consistency:</strong> One great video is encouraging. Ten great videos across different clients is convincing.</li>
  <li><strong>Audio quality:</strong> Watch with your sound on. Poor audio mix is a common blind spot in lower-tier editors.</li>
</ul>

<h2>Questions to Ask Before Hiring</h2>
<ul>
  <li>What's your standard turnaround time for a project like mine?</li>
  <li>How many rounds of revisions are included?</li>
  <li>What file formats do you deliver?</li>
  <li>Do you retain copyright of the music and assets used?</li>
  <li>How do you handle brief changes mid-project?</li>
  <li>Can I speak to a previous client as a reference?</li>
</ul>

<h2>Red Flags to Avoid</h2>
<ul>
  <li><strong>No written contract or scope:</strong> Verbal agreements create expensive disagreements. Everything should be in writing.</li>
  <li><strong>Full payment required upfront:</strong> Reputable editors take a deposit (typically 30–50%) with the balance on delivery.</li>
  <li><strong>Can't show relevant portfolio work:</strong> "I can do any style" without examples to prove it is a warning sign.</li>
  <li><strong>Unusually low pricing:</strong> Professional editing takes time. A quote dramatically below market rate often means offshore editing, stock templates, or inexperience.</li>
  <li><strong>Slow communication before you've even hired them:</strong> If they're slow to respond when they're trying to win your business, imagine how responsive they'll be mid-project.</li>
</ul>

<h2>Understanding Pricing Structures</h2>
<ul>
  <li><strong>Hourly rate:</strong> $80–$200/hr for professional Perth editors. Risk: costs can escalate with scope changes.</li>
  <li><strong>Per-project (fixed price):</strong> Safest for clients. You know the cost before work begins. Perth Content operates on fixed pricing.</li>
  <li><strong>Retainer:</strong> Monthly agreement for ongoing content. Best value for businesses producing regular video — usually 10–20% below project rates.</li>
</ul>

<h2>Why Local Matters</h2>
<p>Working with a Perth-based editor has real advantages: same timezone for fast feedback, potential for in-person briefings, and an understanding of the local market, suburbs, and business culture. For <a href="corporate-video-perth.html">corporate video</a> or real estate work, local context matters.</p>
<p>Perth Content is based in Perth and works with businesses across the metro area. <a href="contact.html">Get a quote and find out if we're the right fit.</a></p>"""
  },
  {
    "slug": "blog-what-equipment-perth-video-editors-use",
    "title": "What Equipment Do Perth Video Editors Use?",
    "tag": "How-To", "date": "2026-09-14", "date_display": "14 September 2026", "read_time": 5,
    "meta": "From DaVinci Resolve to M-series MacBook Pros — the software and hardware professional Perth video editors rely on in 2025, and what it means for your project.",
    "excerpt": "From DaVinci Resolve to Premiere Pro, from M2 MacBook Pros to Wacom tablets — here's the software and hardware setup that professional Perth video editors rely on in 2025.",
    "body": """<p>Understanding what equipment professional video editors use isn't just interesting trivia — it affects the quality of your final video, the speed of delivery, and the types of effects and colour work your editor can achieve. Here's what the Perth video editing industry is actually running in 2025.</p>

<h2>Editing Software</h2>

<h3>Adobe Premiere Pro</h3>
<p>The industry standard for commercial video editing. Premiere Pro's deep integration with Adobe After Effects, Audition, and Photoshop makes it the go-to for complex projects requiring motion graphics, sound design, and multi-format delivery. Most Perth corporate and social media editors use Premiere Pro.</p>

<h3>DaVinci Resolve</h3>
<p>Blackmagic Design's Resolve has become the gold standard for colour grading — and increasingly, for full editing workflows. Its free version is genuinely professional-grade. Editors working on cinematic content, documentary, or high-end corporate video often prefer Resolve for its colour tools.</p>

<h3>Final Cut Pro</h3>
<p>Apple's professional editor is popular among Mac-based freelancers for its speed and efficiency on Apple Silicon machines. Not as widely used for agency work (no Windows version), but excellent for solo editors with a high-volume social media workflow.</p>

<h3>CapCut Pro</h3>
<p>Increasingly used for social-first content — particularly TikTok and Instagram Reels. Its AI-powered auto-captions, trending effects, and direct social publishing make it fast for high-volume social content, though it lacks the depth for complex productions.</p>

<h2>Hardware</h2>

<h3>Apple MacBook Pro (M2/M3/M4)</h3>
<p>The most popular editing machine among Perth freelancers and boutique studios. Apple Silicon's performance per watt is extraordinary — editing 4K footage in real-time with minimal proxy workflow. The M3 Max and M4 Max chips handle even 6K and 8K footage smoothly.</p>

<h3>Custom Windows PC</h3>
<p>Preferred by many studio editors for maximum RAM and GPU headroom. A high-end Windows workstation with an NVIDIA RTX 4090, 128GB RAM, and fast NVMe storage handles any render demand. Also easier to upgrade over time than a laptop.</p>

<h3>Wacom Tablet</h3>
<p>Used for precise colour grading and mask drawing. Most professional colourists prefer a stylus to a mouse for detailed work in DaVinci Resolve's colour panel.</p>

<h3>Calibrated Monitor</h3>
<p>Colour-accurate output requires a calibrated display. Professional editors use monitors like the LG UltraFine, ASUS ProArt, or Sony BVM series — displays that accurately reproduce colour space so what you see matches what your audience sees across devices.</p>

<h2>Storage and Backup</h2>
<ul>
  <li><strong>NVMe SSD:</strong> For active project files — fast enough for real-time 4K editing without proxies.</li>
  <li><strong>NAS (Network Attached Storage):</strong> For archiving and team collaboration. Common in agency environments.</li>
  <li><strong>Cloud backup:</strong> Dropbox, Google Drive, or Backblaze for disaster recovery. Reputable editors always maintain off-site backups of client footage.</li>
</ul>

<h2>Audio Tools</h2>
<ul>
  <li><strong>Adobe Audition:</strong> Industry standard for audio clean-up, noise reduction, and mixing.</li>
  <li><strong>iZotope RX:</strong> The professional tool for removing background noise, hums, and audio artefacts from problematic recordings.</li>
  <li><strong>Epidemic Sound / Artlist:</strong> Royalty-free music libraries used by Perth editors for client projects — legally licensed for commercial use.</li>
</ul>

<h2>What This Means for Your Project</h2>
<p>When hiring a Perth video editor, it's worth asking what software they use and whether their setup can handle your footage format. If you're shooting in 4K or RAW, confirm your editor has the hardware to handle it without excessive render times. A professional setup means faster delivery and higher quality colour work.</p>
<p>Perth Content uses professional-grade software and hardware for every project. <a href="contact.html">Get a quote today.</a></p>"""
  },
  {
    "slug": "blog-how-to-use-video-on-perth-business-website",
    "title": "How to Use Video on Your Perth Business Website",
    "tag": "Strategy", "date": "2026-09-21", "date_display": "21 September 2026", "read_time": 5,
    "meta": "Video on your website reduces bounce rates, increases time on site, and improves conversions. Here's exactly where to place video on your Perth business website.",
    "excerpt": "Video on your website can reduce bounce rates, increase time on site, and dramatically improve conversions. Here's where to place video on your Perth business website — and what type to use.",
    "body": """<p>Adding a video to your website is one of the highest-ROI changes any Perth business can make. But placement matters. Dropping a video in the wrong spot — or using the wrong type — can actually hurt your results. Here's where video works hardest on a business website, and what to put there.</p>

<h2>Homepage Hero</h2>
<p><strong>What to use:</strong> A 30–60 second brand overview or silent ambient loop<br/>
<strong>Goal:</strong> Immediate trust-building, reduced bounce rate</p>
<p>The hero section is the first thing a visitor sees. A well-produced brand video here communicates who you are, what you do, and why you're different — faster than any headline can. If you go with an autoplaying silent loop (no sound, no play button), make it atmospheric and visually compelling. If you use a play-to-watch video, put a thumbnail that invites a click.</p>
<p>Pages with a hero video retain visitors significantly longer — giving your copy, testimonials, and CTAs time to do their work.</p>

<h2>About Page</h2>
<p><strong>What to use:</strong> A 1–2 minute "meet the team" or founder story video<br/>
<strong>Goal:</strong> Build human connection and trust</p>
<p>The About page is where curious, warming prospects go to decide if they like you. A video of real team members talking about why they do what they do converts far better than a wall of bios. Perth buyers especially value knowing who they're dealing with before they pick up the phone.</p>

<h2>Service Pages</h2>
<p><strong>What to use:</strong> Short explainer video (60–90 seconds) specific to that service<br/>
<strong>Goal:</strong> Explain the service, overcome objections, drive enquiry</p>
<p>Most service pages are text-heavy and hard to scan. Embedding a short explainer video above the fold gives visitors an alternative consumption path. Many people will watch a 90-second video before reading a single paragraph. An <a href="explainer-video-perth.html">explainer video</a> on each service page also improves that page's Google ranking — pages with video rank higher.</p>

<h2>Testimonials / Social Proof Section</h2>
<p><strong>What to use:</strong> 60–90 second customer testimonial videos<br/>
<strong>Goal:</strong> Convert warm prospects who are weighing up their options</p>
<p>Written testimonials are easily dismissed as fabricated. Video testimonials are viscerally convincing — a real face, real voice, real emotion. Embedding 2–3 <a href="testimonial-video-perth.html">testimonial videos</a> on your homepage or dedicated reviews page can dramatically improve your close rate on inbound enquiries.</p>

<h2>FAQ / How It Works Section</h2>
<p><strong>What to use:</strong> A 2–4 minute process walkthrough or FAQ video<br/>
<strong>Goal:</strong> Reduce pre-sale anxiety, answer common objections</p>
<p>Buyers have questions before they enquire. A video answering your 5 most common questions (pricing, process, timeline, guarantees) reduces the friction between interest and contact. It also shortens your sales calls significantly.</p>

<h2>Blog Posts</h2>
<p><strong>What to use:</strong> Embedded YouTube video relevant to the post topic<br/>
<strong>Goal:</strong> Increase time on page, improve SEO rankings</p>
<p>Google's algorithm considers "dwell time" as a quality signal. Embedding a relevant video in blog posts keeps readers on the page longer — and that improved dwell time improves your search ranking over time.</p>

<h2>Contact Page</h2>
<p><strong>What to use:</strong> A short 30–45 second "what happens next" reassurance video<br/>
<strong>Goal:</strong> Reduce form abandonment</p>
<p>A brief video on your contact page saying "Here's exactly what happens when you fill in this form" removes the fear of the unknown. Conversion rates on contact forms with a reassurance video are consistently higher than those without.</p>

<h2>Technical Considerations</h2>
<ul>
  <li>Host videos on YouTube or Vimeo — don't host video files directly on your website (page load speed will suffer).</li>
  <li>Use lazy-loading for video embeds to keep page speed fast.</li>
  <li>Always add captions — for accessibility and because many viewers watch on mute.</li>
  <li>Optimise your video thumbnail — it's the first impression that determines whether people click play.</li>
</ul>
<p>Perth Content can produce the right video for every section of your website. <a href="contact.html">Get a quote today.</a></p>"""
  },
  {
    "slug": "blog-social-proof-videos-testimonials-perth",
    "title": "Social Proof Videos — Why Testimonials Outperform Written Reviews for Perth Businesses",
    "tag": "Corporate", "date": "2026-09-28", "date_display": "28 September 2026", "read_time": 5,
    "meta": "A video testimonial is worth 10 written reviews. Here's why Perth businesses that use video testimonials convert more visitors into clients — and how to produce them on any budget.",
    "excerpt": "A video testimonial is worth 10 written reviews. Here's why Perth businesses that use video testimonials convert more visitors into clients — and how to produce them on any budget.",
    "body": """<p>Online reviews are good. Video testimonials are transformative. The difference isn't just format — it's the psychological impact of seeing a real person, hearing their real voice, and watching their genuine reaction. For Perth businesses trying to convert website visitors into paying clients, video social proof is the single most effective tool available.</p>

<h2>Why Written Reviews Have a Trust Problem</h2>
<p>The problem with written reviews isn't that they don't work — they do. But buyers are increasingly sceptical. Reviews can be purchased, faked, or incentivised. Even legitimate five-star Google reviews feel anonymous and generic. "Great service, highly recommend!" tells you almost nothing.</p>
<p>A video testimonial is fundamentally harder to fake. A real face, real name, real emotion — that's not something you can manufacture cheaply. Buyers know this. It's why video testimonials carry a trust premium that no written review can match.</p>

<h2>What Video Testimonials Do That Written Reviews Can't</h2>
<ul>
  <li><strong>Emotional resonance:</strong> A client saying "working with these guys completely transformed our marketing" carries 10x the impact when you can hear the enthusiasm in their voice.</li>
  <li><strong>Specific detail:</strong> Video testimonials naturally include more specific, useful information — because the client is talking, not typing.</li>
  <li><strong>Identity credibility:</strong> Seeing the actual person, their business, their location adds authenticity that an anonymous username never can.</li>
  <li><strong>Watch time:</strong> A video testimonial keeps visitors on your page longer — compounding the trust-building effect.</li>
</ul>

<h2>How to Get Great Video Testimonials</h2>

<h3>Choose the Right Client</h3>
<p>Pick clients who are enthusiastic, articulate, and ideally represent your target market. A testimonial from a business similar to your prospects' business is far more persuasive than a generic one.</p>

<h3>Make It Easy for Them</h3>
<p>Clients hesitate to participate because they don't know what to say. Give them 3–4 prompt questions in advance:</p>
<ul>
  <li>What was the challenge you had before working with us?</li>
  <li>What made you choose us over other options?</li>
  <li>What specific results have you seen?</li>
  <li>Who would you recommend us to?</li>
</ul>
<p>These prompts produce specific, compelling answers rather than generic praise.</p>

<h3>Film It Properly</h3>
<p>A testimonial filmed on a noisy phone in a cluttered office undermines your brand even as it tries to support it. Invest in proper filming — clean background, good lighting, clear audio. A professional half-day shoot can capture 3–5 client testimonials efficiently.</p>

<h3>Keep It Short</h3>
<p>60–90 seconds is the ideal testimonial length. If the client has more to say, produce a short version for your website and a longer version for YouTube. Edit ruthlessly — remove um's, ah's, and tangents.</p>

<h2>Where to Use Video Testimonials</h2>
<ul>
  <li>Homepage (above the fold or in a dedicated social proof section)</li>
  <li>Service pages (relevant testimonial alongside the relevant service)</li>
  <li>Sales proposals and pitch decks</li>
  <li>Social media (especially LinkedIn and Instagram)</li>
  <li>Email nurture sequences</li>
  <li>Trade show displays</li>
</ul>

<h2>Budget Options</h2>
<ul>
  <li><strong>Client films themselves, you edit:</strong> $300–$600 for a professionally edited testimonial from self-shot footage</li>
  <li><strong>Half-day shoot (3–5 testimonials):</strong> $1,500–$3,000 all-in including filming, editing, and delivery</li>
  <li><strong>On-location at client's business:</strong> Adds context and authenticity — usually worth the extra effort</li>
</ul>

<p>Perth Content's <a href="testimonial-video-perth.html">testimonial video service</a> covers everything from filming through to final edit. <a href="contact.html">Get a quote today.</a></p>"""
  },
  {
    "slug": "blog-how-to-film-talking-head-video-business",
    "title": "How to Film a Great Talking Head Video for Your Business",
    "tag": "How-To", "date": "2026-10-05", "date_display": "5 October 2026", "read_time": 5,
    "meta": "Talking head videos are the most versatile business content format. Here's how to set up lighting, background, framing, and audio for a professional result.",
    "excerpt": "Talking head videos are the most versatile content format — but only when they're produced well. Here's how to set up your background, lighting, framing, and audio for a professional result.",
    "body": """<p>Talking head videos — where a person speaks directly to camera — are the backbone of business video content. Testimonials, thought leadership pieces, LinkedIn videos, FAQ responses, product walkthroughs — all are variations of the same format. Get the setup right, and even phone-filmed content can look genuinely professional. Get it wrong, and expensive camera equipment won't save you.</p>

<h2>Background: The First Thing Viewers Notice</h2>
<p>A cluttered, chaotic background tells viewers you didn't prepare. A clean, intentional background tells them you're professional.</p>
<ul>
  <li><strong>Best option:</strong> A simple, uncluttered office environment with some depth — bookshelves, plants, or a branded wall work well. Avoid busy patterns.</li>
  <li><strong>Second best:</strong> A solid-colour wall (medium grey, navy, or a brand colour). Avoid pure white — it creates exposure challenges.</li>
  <li><strong>Avoid:</strong> White walls with light switches, cluttered desks in frame, busy open-plan offices, or windows directly behind the speaker.</li>
</ul>
<p><strong>Depth tip:</strong> Position your speaker at least 1–2 metres from the background. This creates natural background blur (bokeh), making even simple setups look cinematic.</p>

<h2>Lighting: The Biggest Differentiator</h2>
<p>Good lighting separates "recorded on a phone" from "looks like it was filmed professionally." The good news: you don't need expensive equipment.</p>
<ul>
  <li><strong>Key light:</strong> Your main light source, positioned at 45° to one side of the speaker's face and slightly above eye level. A ring light, softbox, or even a large window on a cloudy day works well.</li>
  <li><strong>Fill light:</strong> A softer light (or white reflector card) on the opposite side to reduce harsh shadows from the key light.</li>
  <li><strong>Avoid:</strong> Overhead fluorescent lights (they cast unflattering shadows under eyes and nose), direct sunlight (harsh and unpredictable), and mixing different colour temperature light sources.</li>
</ul>
<p><strong>Best free option:</strong> A large window with indirect natural light (cloudy day or north-facing) is flattering and free. Position the speaker facing the window, not with it behind them.</p>

<h2>Framing: How to Position Your Subject</h2>
<ul>
  <li><strong>Eye level:</strong> The camera lens should be at or very slightly above eye level. Looking up at the camera is unflattering; looking down at it is condescending. Prop your laptop or phone on books if needed.</li>
  <li><strong>Rule of thirds:</strong> Don't centre the speaker perfectly — position their eyes at the top third of the frame, and their face slightly left or right of centre.</li>
  <li><strong>Headroom:</strong> Leave a small amount of space above the speaker's head — roughly 10–15% of the frame. Too much headroom looks amateurish; none looks cramped.</li>
  <li><strong>Aspect ratio:</strong> Film in 16:9 (landscape) for YouTube and LinkedIn. Film vertically (9:16) for Instagram Reels and TikTok. If you need both, film vertical and reframe for landscape in post.</li>
</ul>

<h2>Audio: The Non-Negotiable</h2>
<p>Viewers will forgive average visuals. They will not forgive bad audio. Poor audio — echo, background noise, low volume — is the number one reason professional-looking videos feel amateur.</p>
<ul>
  <li><strong>Lavalier (lapel) microphone:</strong> The most reliable option for solo talking heads. A Rode SmartLav+ ($70) connected to your phone or camera eliminates room echo and background noise dramatically.</li>
  <li><strong>USB condenser microphone:</strong> Excellent for desk setups (podcast-style). The Rode NT-USB or Blue Yeti are popular choices.</li>
  <li><strong>Avoid built-in camera/phone mics:</strong> They capture everything — air conditioning, traffic, room echo. Only use them as a last resort.</li>
  <li><strong>Room treatment:</strong> Record in a carpeted room with soft furnishings — these absorb sound reflections. Avoid bare, tiled, or concrete rooms.</li>
</ul>

<h2>Delivery: Looking Good on Camera</h2>
<ul>
  <li>Look at the camera lens, not the screen — this creates the appearance of eye contact with your viewer.</li>
  <li>Speak slightly slower than feels natural — nervousness speeds us up.</li>
  <li>Wear solid colours that contrast with your background. Avoid fine stripes or busy patterns (they cause visual aliasing).</li>
  <li>Do a 10-second test recording and review it before filming in earnest.</li>
</ul>

<p>If filming yourself isn't your strength, Perth Content offers a <a href="corporate-video-perth.html">professional filming and editing service</a> that handles everything. <a href="contact.html">Get a quote today.</a></p>"""
  },
  {
    "slug": "blog-youtube-for-perth-businesses-worth-it",
    "title": "YouTube for Perth Businesses — Is It Worth It in 2025?",
    "tag": "Social Media", "date": "2026-10-12", "date_display": "12 October 2026", "read_time": 5,
    "meta": "Is YouTube worth a Perth business's time and investment in 2025? We weigh the effort against the payoff — with practical advice on what types of content perform.",
    "excerpt": "YouTube is the world's second-largest search engine. But is it worth a Perth business's time to build a channel? We weigh the effort against the payoff — with examples from local businesses.",
    "body": """<p>YouTube is the world's second-largest search engine, with over 2 billion logged-in users every month. For Perth businesses, that represents an enormous potential audience — but also a significant time investment. Is building a YouTube channel worth it? The honest answer: it depends on your business type and how you approach it.</p>

<h2>Why YouTube Is Different From Other Social Platforms</h2>
<p>Instagram and TikTok content typically has a lifespan of 24–48 hours before it's algorithmically buried. YouTube content compounds: a well-optimised video can drive organic search traffic for years. A Perth plumbing business that uploads "How to fix a dripping tap in Perth" today might still be getting calls from that video in 2030.</p>
<p>This permanence makes YouTube a fundamentally different investment — more like SEO than social media.</p>

<h2>When YouTube Is Worth It for Perth Businesses</h2>
<ul>
  <li><strong>Service businesses with educational content:</strong> Tradies, lawyers, accountants, health professionals, and financial advisers can all build authority by answering the questions their clients Google. If your clients search for answers, YouTube is where you should be providing them.</li>
  <li><strong>B2B companies with complex products:</strong> Software demos, technical walkthroughs, and case studies work exceptionally well on YouTube. Enterprise buyers conduct extensive video research before making decisions.</li>
  <li><strong>Businesses in competitive markets:</strong> When every competitor is running the same Google Ads, a YouTube channel that educates and builds trust gives you an organic channel competitors can't easily buy.</li>
  <li><strong>Businesses with interesting processes:</strong> "How it's made" content, behind-the-scenes access, and process documentation attracts engaged audiences who become loyal customers.</li>
</ul>

<h2>When YouTube Might Not Be Worth the Effort</h2>
<ul>
  <li>Your target audience is over 55 and not online (rare, but exists)</li>
  <li>Your business is purely local with no need for content reach (a small café serving regulars, for example)</li>
  <li>You can't commit to at least one video per fortnight — inconsistency is the main cause of channel failure</li>
</ul>

<h2>What Actually Gets Views on YouTube in 2025</h2>
<ul>
  <li><strong>SEO-targeted how-to content:</strong> Videos that directly answer search queries ("How to [X] in Perth") consistently outperform brand videos on views and sustained traffic.</li>
  <li><strong>Shorts (under 60 seconds):</strong> YouTube's algorithm aggressively promotes Shorts to new audiences — an excellent discovery tool to funnel viewers to your long-form content.</li>
  <li><strong>Series and playlists:</strong> Channels that group related content into series see higher subscriber rates and watch time.</li>
  <li><strong>Consistent upload schedule:</strong> YouTube's algorithm rewards channels that upload regularly. Weekly or fortnightly is more effective than sporadic high-quality uploads.</li>
</ul>

<h2>The Realistic Time Investment</h2>
<p>A 5–8 minute YouTube video for a Perth business typically requires:</p>
<ul>
  <li>30–60 minutes of scripting and preparation</li>
  <li>30–60 minutes of filming</li>
  <li>2–4 hours of editing (or 1–2 hours if outsourced to a professional editor)</li>
  <li>30 minutes for thumbnail design, titling, description, and SEO optimisation</li>
</ul>
<p>Total: 4–6 hours per video, or 2–3 hours if you outsource the editing. Our <a href="youtube-video-editing-perth.html">YouTube video editing service</a> handles the production side so you can focus on content.</p>

<h2>The Bottom Line</h2>
<p>YouTube is worth it for Perth businesses with something valuable to teach, demonstrate, or share — and the consistency to keep publishing. If you're willing to commit to 6–12 months of regular content, YouTube can become your most durable source of organic leads. If you're looking for quick results, Instagram Reels or LinkedIn video will get you there faster.</p>
<p><a href="contact.html" class="btn btn-primary">Talk to Perth Content About Video Strategy</a></p>"""
  },
]

for p in POSTS:
    html = page(p)
    path = os.path.join(OUT, f"{p['slug']}.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✓ {p['slug']}.html")

print(f"\nGenerated {len(POSTS)} files.")
