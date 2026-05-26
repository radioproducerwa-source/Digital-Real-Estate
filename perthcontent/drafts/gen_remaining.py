#!/usr/bin/env python3
"""Generate remaining 23 blog draft HTML files for Perth Content."""
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
    sidebar = f'''<aside class="post-sidebar">
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
  {sidebar}
</div></section>
{FOOTER}
</body>
</html>'''

POSTS = [
  {
    "slug": "blog-how-to-brief-a-video-editor",
    "title": "How to Brief a Video Editor for Your Business",
    "tag": "How-To", "date": "2026-06-22", "date_display": "22 June 2026", "read_time": 5,
    "meta": "A clear brief saves time, money, and revision rounds. Learn exactly what to include when briefing a video editor so they deliver what you need, first time.",
    "excerpt": "A clear brief saves time, money, and revisions. This guide explains exactly what to include in a video editing brief so your editor can deliver exactly what you need.",
    "body": """<p>The single biggest cause of over-budget, late, and disappointing video projects isn't poor editing — it's a poor brief. A vague brief leads to guesswork, and guesswork leads to revisions. Every unnecessary revision costs time and money. Here's how to brief a video editor so your project runs smoothly from day one.</p>

<h2>Why the Brief Matters More Than You Think</h2>
<p>A professional video editor can work with almost any footage and almost any style — but they can't read your mind. Without a clear brief, they'll make assumptions about tone, pacing, music, and structure. Some of those assumptions will be right. Many won't. The result? Multiple revision rounds, frustrated client, frustrated editor, and a final product that still doesn't feel quite right.</p>
<p>A solid brief eliminates that problem. It aligns expectations before a single frame is cut.</p>

<h2>The 8 Things Every Video Brief Must Include</h2>

<h3>1. Purpose and Goal</h3>
<p>What is this video for? What do you want viewers to do after watching it? Examples: "Build trust with new website visitors," "Explain our software to potential enterprise clients," "Drive traffic to our contact page." Be specific.</p>

<h3>2. Target Audience</h3>
<p>Who is watching? A video for C-suite executives feels very different to one for 25-year-old Instagram users. Describe your audience: industry, age range, pain points, what they care about.</p>

<h3>3. Desired Length</h3>
<p>Give a target length or a maximum. "Under 90 seconds" or "2–3 minutes" gives the editor a clear constraint to work within. If you're unsure, ask for their recommendation based on the platform.</p>

<h3>4. Style References</h3>
<p>Share 2–3 video links that match the feel you're after — even if they're from other industries. This is the fastest way to communicate tone, pacing, and aesthetic without lengthy descriptions.</p>

<h3>5. Music Preferences</h3>
<p>Upbeat or calm? Corporate or casual? Instrumental or with vocals? Music drives the emotional feel of a video more than almost anything else. If you have a specific track in mind, share it. If not, describe the energy you want.</p>

<h3>6. Text, Captions, and Graphics</h3>
<p>Do you need subtitles? Lower-thirds (name and title labels)? A logo animation? Specific calls to action as text overlays? List every graphic element you need, or explicitly say "no text overlays."</p>

<h3>7. Deadline</h3>
<p>Give both your ideal deadline and your hard deadline. "We'd love it by Friday but need it no later than Monday" is much more useful than just "ASAP."</p>

<h3>8. Delivery Format</h3>
<p>How will you use the video? Web (H.264 MP4), social (vertical 9:16 for Reels/TikTok, square 1:1 for feed), broadcast (ProRes)? Do you need multiple aspect ratios? Confirm this upfront — reformatting after the fact adds cost.</p>

<h2>A Simple Brief Template</h2>
<p>Copy and fill in this template before your next project:</p>
<ul>
  <li><strong>Project:</strong> [Name/description]</li>
  <li><strong>Goal:</strong> [What this video needs to achieve]</li>
  <li><strong>Audience:</strong> [Who will watch it]</li>
  <li><strong>Length:</strong> [Target or maximum]</li>
  <li><strong>Style references:</strong> [Links to 2–3 videos]</li>
  <li><strong>Music:</strong> [Genre/energy/specific track]</li>
  <li><strong>Text/graphics needed:</strong> [List or "none"]</li>
  <li><strong>Delivery format:</strong> [Platform and specs]</li>
  <li><strong>Ideal deadline:</strong> [Date]</li>
  <li><strong>Hard deadline:</strong> [Date]</li>
  <li><strong>Revision rounds included:</strong> [Confirm with editor]</li>
</ul>

<h2>Common Briefing Mistakes</h2>
<ul>
  <li><strong>Sending raw footage without context:</strong> Always explain what you filmed and why, even if it's obvious to you.</li>
  <li><strong>"Make it look professional":</strong> This means something different to everyone. Use references instead.</li>
  <li><strong>Changing the brief mid-edit:</strong> Scope changes after editing has begun are the most common cause of budget blowouts. Finalise your brief before work starts.</li>
  <li><strong>Forgetting about music licensing:</strong> If you want a specific commercial track, check licensing costs before committing it in your brief.</li>
</ul>

<p>A great brief is a partnership. The more clearly you communicate what you need, the better your <a href="corporate-video-perth.html">video editor</a> can deliver it. Take 20 minutes to complete your brief properly — it will save you hours of back-and-forth later.</p>
<p><a href="contact.html" class="btn btn-primary">Get a Quote from Perth Content</a></p>"""
  },
  {
    "slug": "blog-repurpose-one-video-ten-pieces-content",
    "title": "How to Repurpose One Video Into 10 Pieces of Content",
    "tag": "Strategy", "date": "2026-07-06", "date_display": "6 July 2026", "read_time": 5,
    "meta": "One well-produced video can fuel a month of content across Instagram, LinkedIn, YouTube, website, and email. Here's the exact repurposing workflow for Perth businesses.",
    "excerpt": "One well-produced video can fuel a month of content across Instagram, LinkedIn, YouTube, your website, and email. Here's the exact workflow Perth Content uses with clients.",
    "body": """<p>Most Perth businesses treat video as a one-and-done asset: produce it, post it once, move on. That's one of the biggest missed opportunities in content marketing. A single well-produced video — an interview, brand film, or webinar recording — can be repurposed into a full month of content across every channel your business uses. Here's exactly how.</p>

<h2>Start With a Long-Form Anchor Video</h2>
<p>The repurposing workflow starts with one high-quality long-form piece: a 5–15 minute brand interview, a recorded webinar, a behind-the-scenes documentary, or a client case study. This is your content mine — everything else gets extracted from it.</p>
<p>The key is to film it properly from the start: good lighting, clean audio, multiple camera angles if possible. This footage will be cut many ways, so raw quality matters.</p>

<h2>The 10 Pieces You Can Extract</h2>

<h3>1. Full YouTube Upload</h3>
<p>Upload the full-length video to YouTube with SEO-optimised title, description, and chapters. This builds long-term search traffic and gives you a permanent home for the content.</p>

<h3>2. 60-Second Instagram Reel</h3>
<p>Cut the single best minute — the most compelling moment, insight, or story — as a vertical Reel. Add captions. This gets the most reach of any format on Instagram. See our <a href="instagram-reels-editing-perth.html">Instagram Reels editing service</a>.</p>

<h3>3. TikTok Vertical Cut</h3>
<p>A different 30–45 second clip (or the same one with different caption copy) posted natively to TikTok. See our <a href="tiktok-video-editing-perth.html">TikTok editing service</a>.</p>

<h3>4. LinkedIn Native Video</h3>
<p>A 60–90 second clip with a thoughtful caption posted as a native LinkedIn video (not a YouTube link). LinkedIn native video gets 3x more reach than external links.</p>

<h3>5. Blog Post With Embedded Video</h3>
<p>Transcribe the video (or have AI do it), clean it up into a blog post, embed the YouTube video within it. Now you have a long-form SEO article too.</p>

<h3>6. Email Newsletter Feature</h3>
<p>Use a still from the video as the email thumbnail, link through to the YouTube or blog version. Video thumbnails in email consistently outperform text-only newsletters on click-through rate.</p>

<h3>7. Quote Graphic From a Spoken Line</h3>
<p>Pull one powerful quote from the video, design it as a branded static graphic, post across Instagram, LinkedIn, and Facebook. Zero additional filming required.</p>

<h3>8. Podcast-Style Audio</h3>
<p>Strip the audio track and upload it to podcast platforms (Spotify, Apple Podcasts). Interview content translates especially well. Many business owners consume content on commutes — meet them there.</p>

<h3>9. Website Homepage Hero</h3>
<p>If the footage is strong enough, cut a 30–60 second silent loop for your website hero section. This dramatically increases time-on-page and conversion rates.</p>

<h3>10. Facebook or Instagram Video Ad</h3>
<p>Take the strongest 15–30 seconds, add a clear call-to-action overlay, and run it as a paid ad. You've now created ad creative without an additional shoot.</p>

<h2>The Workflow</h2>
<ol>
  <li>Film and edit the long-form anchor video</li>
  <li>Export the full-length version for YouTube</li>
  <li>Have your editor cut 3–5 short clips in the same session (much cheaper than separate edits)</li>
  <li>Transcribe and write the blog post</li>
  <li>Schedule social posts across the week</li>
  <li>Set up the email and ad campaigns</li>
</ol>
<p>The entire workflow can be built from a single half-day shoot and one editing session. For Perth businesses on tight content budgets, this is the highest-leverage approach available.</p>
<p>Perth Content can handle the full repurposing workflow — from editing the anchor video to cutting all the derivative clips. <a href="contact.html">Talk to us about your next project.</a></p>"""
  },
  {
    "slug": "blog-best-video-lengths-instagram-linkedin-youtube-tiktok",
    "title": "Best Video Lengths for Instagram, LinkedIn, YouTube, and TikTok in 2025",
    "tag": "Social Media", "date": "2026-07-13", "date_display": "13 July 2026", "read_time": 4,
    "meta": "Optimal video lengths for every platform in 2025 — Instagram, LinkedIn, YouTube, TikTok, and Facebook. Maximise reach and watch time for Perth businesses.",
    "excerpt": "Every platform has an ideal video length that maximises reach and watch time. Here's the 2025 guide to optimal video duration on every platform Perth businesses should care about.",
    "body": """<p>Platform algorithms reward videos that keep viewers watching. Posting a 10-minute brand video on TikTok or a 15-second clip on YouTube misses the mark on both. Here's the 2025 guide to optimal video lengths by platform — so every video you post performs as well as possible.</p>

<h2>Instagram</h2>
<ul>
  <li><strong>Reels:</strong> 15–30 seconds for maximum reach. The algorithm heavily favours Reels under 30 seconds. For storytelling, up to 60 seconds works well — beyond that, drop-off increases sharply. See our <a href="instagram-reels-editing-perth.html">Instagram Reels editing</a>.</li>
  <li><strong>Feed videos:</strong> 30–60 seconds. Anything longer struggles for watch-through rate in the feed.</li>
  <li><strong>Stories:</strong> 15 seconds per card. Multi-card sequences of 3–5 cards perform best for step-by-step content.</li>
</ul>

<h2>LinkedIn</h2>
<ul>
  <li><strong>Native video (personal/company posts):</strong> 60–90 seconds is the sweet spot for engagement and reach. LinkedIn audiences are professional and time-poor — get to the point quickly.</li>
  <li><strong>LinkedIn Live / long-form:</strong> Up to 10 minutes works for webinar replays and in-depth content, but only for engaged followers. Don't use long-form for top-of-funnel posts.</li>
  <li><strong>Video ads:</strong> 15–30 seconds. LinkedIn video ads with a clear hook in the first 3 seconds perform significantly better. See our <a href="linkedin-video-perth.html">LinkedIn video service</a>.</li>
</ul>

<h2>YouTube</h2>
<ul>
  <li><strong>Standard videos:</strong> 8–15 minutes hits the sweet spot for ad revenue, watch time signals, and SEO. Videos over 8 minutes can include mid-roll ads, which YouTube rewards with more distribution.</li>
  <li><strong>YouTube Shorts:</strong> Under 60 seconds. Shorts are a separate feed from long-form — treat them as a discovery tool to drive subscribers to your main channel.</li>
  <li><strong>Tutorials and how-tos:</strong> 5–12 minutes. Longer is fine if the content genuinely warrants it — YouTube rewards watch time, not brevity. See our <a href="youtube-video-editing-perth.html">YouTube editing service</a>.</li>
</ul>

<h2>TikTok</h2>
<ul>
  <li><strong>Sweet spot:</strong> 21–34 seconds. Research consistently shows this length gets the highest completion rates and best algorithmic push for new accounts.</li>
  <li><strong>Storytelling / educational:</strong> 45–60 seconds works well once you have an established audience. TikTok now supports up to 10 minutes, but long-form TikToks only work for creators with large followings.</li>
  <li><strong>Hook rule:</strong> The first 1–2 seconds determine everything. See our <a href="tiktok-video-editing-perth.html">TikTok editing service</a>.</li>
</ul>

<h2>Facebook</h2>
<ul>
  <li><strong>Organic feed videos:</strong> 1–3 minutes performs best for reach. Facebook's algorithm prioritises videos that generate comments and shares.</li>
  <li><strong>Facebook Reels:</strong> Under 60 seconds, matching Instagram Reels best practice.</li>
  <li><strong>Video ads:</strong> 15–30 seconds. Mobile-first, captioned, hook in the first 3 seconds.</li>
</ul>

<h2>Website Hero Video</h2>
<p>30–60 seconds, silent loop, autoplaying. Website hero videos are ambient — they create mood and context while the visitor reads your copy. Keep them short, visually compelling, and free of dialogue (most visitors have their sound off).</p>

<h2>The Golden Rule</h2>
<p>Make it as long as it needs to be — and no longer. Every platform rewards completion rate over duration. A 20-second video that 90% of viewers finish outperforms a 2-minute video that 10% finish, every time. When in doubt, cut it shorter.</p>
<p>Perth Content can edit your raw footage to the optimal length and format for every platform. <a href="contact.html">Get a quote today.</a></p>"""
  },
  {
    "slug": "blog-diy-vs-professional-video-editing-perth",
    "title": "DIY vs Professional Video Editing — The Honest Comparison for Perth Businesses",
    "tag": "How-To", "date": "2026-07-27", "date_display": "27 July 2026", "read_time": 5,
    "meta": "CapCut vs professional video editing for Perth businesses — an honest comparison of quality, time cost, and when each approach is the right choice.",
    "excerpt": "Free tools like CapCut and DaVinci Resolve are tempting — but are they good enough for your Perth business? We give you the honest comparison of DIY vs professional editing.",
    "body": """<p>Free video editing tools have never been better. CapCut, DaVinci Resolve, and iMovie can all produce decent results in the hands of someone who knows what they're doing. But for most Perth businesses, DIY editing costs far more than you'd expect — just not always in dollars.</p>

<h2>What DIY Editing Does Well</h2>
<p>Let's be fair: DIY editing works perfectly for some use cases:</p>
<ul>
  <li>Quick Instagram Stories and casual behind-the-scenes content</li>
  <li>Simple social Reels with trending audio and basic cuts</li>
  <li>Internal team communications and update videos</li>
  <li>Low-stakes social content where authenticity matters more than polish</li>
</ul>
<p>For these purposes, CapCut on a phone can get you 80% of the way there in 20 minutes. That's entirely reasonable.</p>

<h2>The Hidden Cost of DIY Editing</h2>
<p>Where businesses go wrong is applying DIY editing to content that represents their brand at high-stakes moments. Consider the real cost:</p>
<ul>
  <li><strong>Learning curve:</strong> Getting proficient in DaVinci Resolve or Premiere Pro takes 50–100+ hours. That's time you're not spending running your business.</li>
  <li><strong>Your hourly rate:</strong> If your time is worth $100/hour and an edit takes you 6 hours, you've just "spent" $600 on something a professional editor could have done in 2 hours for $300–$400.</li>
  <li><strong>Software and hardware:</strong> Professional editing requires a capable computer. An underpowered machine makes editing painful and crashes costly.</li>
  <li><strong>Revision time:</strong> DIY edits often go through many more revision rounds because the creator can't see their own blind spots.</li>
</ul>

<h2>What Professional Editing Delivers</h2>
<p>A professional Perth video editor brings skills that take years to develop:</p>
<ul>
  <li><strong>Colour grading:</strong> Consistent, cinematic colour across all footage — matching different cameras, correcting for lighting conditions.</li>
  <li><strong>Sound design:</strong> Clean dialogue, balanced music, professional sound effects. Bad audio ruins otherwise good footage.</li>
  <li><strong>Motion graphics:</strong> Animated lower-thirds, logo stings, and text overlays that look polished and branded.</li>
  <li><strong>Story instinct:</strong> Knowing which takes to use, where to cut, how to pace — the invisible craft that separates a great edit from a serviceable one.</li>
  <li><strong>Speed:</strong> What takes a beginner 8 hours takes a professional 2.</li>
</ul>

<h2>When DIY Is Fine</h2>
<ul>
  <li>Casual social content (Stories, quick Reels, TikToks)</li>
  <li>Internal communications</li>
  <li>Rapid-response content (news commentary, trending audio)</li>
  <li>When budget genuinely doesn't allow for professional editing</li>
</ul>

<h2>When You Need a Professional</h2>
<ul>
  <li>Homepage hero video or any content that lives on your website</li>
  <li>Investor presentations, pitch videos, or board presentations</li>
  <li>Trade show or conference display video</li>
  <li>Broadcast advertising (TV, cinema)</li>
  <li>Sales enablement videos used in proposals</li>
  <li>Any video that will be seen by enterprise clients or high-value prospects</li>
</ul>

<h2>The Hybrid Approach</h2>
<p>Many Perth businesses use a smart middle path: film yourself (with a good camera and decent lighting), then hand the raw footage to a professional editor. You save on production costs, they bring the craft. Perth Content's <a href="corporate-video-perth.html">editing-only service</a> is built exactly for this workflow — fast turnaround, professional results, from your footage.</p>
<p><a href="contact.html" class="btn btn-primary">Get an Editing Quote</a></p>"""
  },
  {
    "slug": "blog-what-makes-great-explainer-video-perth",
    "title": "What Makes a Great Explainer Video for a Perth Business?",
    "tag": "Explainer Video", "date": "2026-08-03", "date_display": "3 August 2026", "read_time": 5,
    "meta": "The best explainer videos make complex ideas instantly clear. Here's what separates great Perth business explainer videos from expensive ones nobody watches.",
    "excerpt": "The best explainer videos do one thing well: make a complex idea instantly clear. Here's what separates great explainer videos from expensive ones that nobody watches.",
    "body": """<p>Perth businesses spend thousands on explainer videos every year. Many of those videos are technically well-produced but practically useless — they're too long, try to say too much, or bury the point so deeply that viewers give up and leave. Here's what actually makes a great explainer video work.</p>

<h2>The One-Idea Rule</h2>
<p>Every great explainer video explains exactly one thing. Not your full service offering, not your company history, not six different features. One idea, clearly. The moment you try to explain two things in one video, you dilute both.</p>
<p>Before scripting, write a single sentence: "After watching this video, my viewer will understand ___." If you can't fill that blank with one specific thing, you're not ready to script yet.</p>

<h2>Ideal Length: 60–90 Seconds</h2>
<p>Research consistently shows that viewer drop-off begins sharply after 60 seconds for explainer content. The sweet spot is 75–90 seconds — long enough to explain the problem and solution, short enough to hold attention. Anything over 2 minutes needs to earn every extra second with genuinely valuable content.</p>
<p>At a natural speaking pace (125–150 words per minute), 90 seconds gives you roughly 190–225 words of script. That's enough. Cut ruthlessly.</p>

<h2>The 4 Components of a Great Explainer</h2>

<h3>1. Hook (First 5 Seconds)</h3>
<p>You have 5 seconds before a viewer decides to keep watching. Open with the problem statement — not your company name, not a welcome. "Struggling to get tenants to pay on time?" is a hook. "Welcome to PropertyPro, Perth's leading property management solution" is not.</p>

<h3>2. Problem Statement</h3>
<p>Name the pain your viewer feels. Be specific. The more precisely you describe their problem, the more confident they'll be that your solution understands them.</p>

<h3>3. Solution Showcase</h3>
<p>Explain your solution simply. Show it (screen recording, animation, live demo) rather than just describing it. Visuals do the heavy lifting that words can't.</p>

<h3>4. Single Call to Action</h3>
<p>End with one clear next step. "Get a free quote," "Start your free trial," "Call us today." One CTA, not three. Confusion kills conversions.</p>

<h2>Animation vs Live Action</h2>
<p>Both work — the right choice depends on your product and audience:</p>
<ul>
  <li><strong>Animation:</strong> Better for software, abstract concepts, services that are hard to film, and businesses without a "visual" product. Also ages better and is easier to update.</li>
  <li><strong>Live action:</strong> Better for service businesses where trust and human connection matter — professional services, healthcare, real estate. Seeing real people builds credibility that animation can't match.</li>
</ul>

<h2>Common Explainer Video Mistakes</h2>
<ul>
  <li><strong>Trying to say too much:</strong> Feature-dumping kills engagement. Every sentence should earn its place.</li>
  <li><strong>Poor audio:</strong> Viewers will forgive average visuals but not bad audio. Invest in a good voiceover.</li>
  <li><strong>Generic stock footage:</strong> Nothing screams "we didn't try" like generic handshake stock video. Use real visuals of your product or team wherever possible.</li>
  <li><strong>No clear CTA:</strong> An explainer without a CTA is a brochure nobody can act on.</li>
</ul>

<h2>Cost Ranges in Perth</h2>
<ul>
  <li>Simple live-action explainer (1 min, editing only): $800–$1,500</li>
  <li>Full production live-action explainer: $2,000–$4,000</li>
  <li>2D animated explainer: $2,500–$6,000</li>
  <li>Premium 3D animated explainer: $6,000–$15,000+</li>
</ul>

<p>Perth Content produces <a href="explainer-video-perth.html">explainer videos</a> across all formats. <a href="contact.html">Get a quote for your project.</a></p>"""
  },
  {
    "slug": "blog-how-to-write-video-script-for-business",
    "title": "How to Write a Video Script for Your Business",
    "tag": "How-To", "date": "2026-08-10", "date_display": "10 August 2026", "read_time": 6,
    "meta": "A great video script is the foundation of every successful business video. Follow this step-by-step guide to write compelling scripts for any format or length.",
    "excerpt": "A great script is the foundation of every great business video. This step-by-step guide walks you through writing a compelling script — whether it's for a 60-second Reel or a 5-minute brand film.",
    "body": """<p>A polished video with a weak script will underperform every time. Conversely, a strong script can make even modest production values feel compelling. Learning to write effective video scripts is one of the highest-ROI skills any Perth business owner or marketer can develop.</p>

<h2>Why the Script Comes First</h2>
<p>Everything downstream depends on the script: the shoot plan, the location, the B-roll list, the edit structure, the music choice. Starting a video project without a script is like starting a building without blueprints — technically possible, practically chaotic.</p>

<h2>Word Counts by Video Length</h2>
<p>Speaking at a natural, conversational pace of approximately 130 words per minute:</p>
<ul>
  <li><strong>30 seconds:</strong> ~65 words</li>
  <li><strong>60 seconds:</strong> ~130 words</li>
  <li><strong>90 seconds:</strong> ~195 words</li>
  <li><strong>2 minutes:</strong> ~260 words</li>
  <li><strong>3 minutes:</strong> ~390 words</li>
  <li><strong>5 minutes:</strong> ~650 words</li>
</ul>
<p>Use these as your targets. If your first draft is twice the word count, cut it in half before you do anything else.</p>

<h2>The 3-Part Structure</h2>

<h3>Hook (First 10–15% of script)</h3>
<p>Open with a question, a surprising statistic, or a bold statement that immediately identifies the viewer's problem or desire. "Did you know 85% of social video is watched on mute?" is a hook. "Today I'm going to talk about video captions" is not.</p>

<h3>Body (Middle 70–75%)</h3>
<p>Deliver the value you promised in the hook. Structure it in 2–4 clear points. Each point should have a brief explanation and, where possible, a concrete example. Avoid jargon — write for your least-informed viewer.</p>

<h3>Call to Action (Final 10–15%)</h3>
<p>Tell the viewer exactly what to do next. One action, stated clearly. "Visit perthcontent.com to get a free quote" is better than "Feel free to reach out to us if you'd like to discuss your needs further."</p>

<h2>Writing for the Ear, Not the Eye</h2>
<p>Video scripts are spoken, not read. Write the way people actually talk:</p>
<ul>
  <li>Use contractions (we're, you'll, it's)</li>
  <li>Keep sentences short — rarely longer than 15 words</li>
  <li>Start sentences with "And," "But," or "So" — perfectly fine in spoken English</li>
  <li>Avoid passive voice ("it was found that" → "we found")</li>
  <li>Read every line aloud. If it sounds awkward, rewrite it.</li>
</ul>

<h2>Adding B-Roll Notes</h2>
<p>As you write the script, note what visuals should appear on screen at each moment. These are called B-roll notes and they make your editor's job significantly easier:</p>
<p><em>"We work with over 50 Perth businesses..."</em> → [B-roll: team working at desk, client meeting, before/after video comparison]</p>
<p>You don't need to be prescriptive — suggestions are enough. Your editor can interpret and improve on them.</p>

<h2>The Approval Process</h2>
<p>Before shooting begins, get written approval from all stakeholders on the script. Changes to a script before the shoot cost nothing. Changes after the shoot may require an expensive reshoot. Lock the script before the cameras roll.</p>

<h2>A Sample Script Template</h2>
<pre style="background:#f1f5f9;padding:1rem;border-radius:6px;font-size:0.85rem;overflow-x:auto;">
[HOOK]
"[Open with question or statistic that nails your viewer's problem]"

[PROBLEM]
"[Name the pain. Be specific and empathetic.]"

[SOLUTION]
"[Introduce your product/service as the answer. Keep it simple.]"

[PROOF]
"[One sentence of credibility: a client result, a stat, a credential.]"

[CTA]
"[One clear next step. URL or phone number.]"
</pre>

<p>Need help turning your script into a finished video? Perth Content handles everything from scripting through to final delivery. <a href="corporate-video-perth.html">See our corporate video service</a> or <a href="contact.html">get a quote today.</a></p>"""
  },
  {
    "slug": "blog-top-5-video-styles-perth-small-businesses",
    "title": "Top 5 Video Styles for Perth Small Businesses",
    "tag": "Strategy", "date": "2026-08-17", "date_display": "17 August 2026", "read_time": 4,
    "meta": "The 5 most effective video formats for Perth small businesses — ranked by ROI, ease of production, and versatility. Find the right style for your budget.",
    "excerpt": "Not all video styles work for every business. Here are the five most effective video formats for Perth SMBs — ranked by ROI, ease of production, and versatility.",
    "body": """<p>With so many video formats available — Reels, testimonials, explainers, live streams, documentaries — it's easy to get overwhelmed. Most Perth small businesses don't need all of them. They need the right two or three. Here are the five most effective video styles for SMBs, ranked by return on investment.</p>

<h2>1. Customer Testimonial Video</h2>
<p><strong>Best for:</strong> Service businesses, professional services, tradespeople, healthcare, real estate</p>
<p>A genuine testimonial from a real Perth client outperforms every other content type for trust-building. It works because it's not you saying how good you are — it's someone else. That third-party credibility converts sceptical prospects better than any brochure or website copy.</p>
<p><strong>Typical Perth cost:</strong> $500–$2,000 including filming and editing</p>
<p>See our <a href="testimonial-video-perth.html">testimonial video service</a>.</p>

<h2>2. Explainer Video</h2>
<p><strong>Best for:</strong> Software, professional services, financial products, anything complex</p>
<p>If your product or service requires explanation, an explainer video does it once — and keeps doing it 24/7 on your website, social channels, and sales decks. A good 90-second explainer can reduce your sales call length by half because prospects arrive already educated.</p>
<p><strong>Typical Perth cost:</strong> $1,500–$4,000 for live-action; $2,500–$6,000 for animation</p>
<p>See our <a href="explainer-video-perth.html">explainer video service</a>.</p>

<h2>3. Social Media Reels</h2>
<p><strong>Best for:</strong> Any business wanting to grow brand awareness on Instagram, TikTok, or Facebook</p>
<p>Short-form video is the single highest-reach organic content format on every major social platform in 2025. A 20–30 second Reel showing your work, your team, or a useful tip can reach thousands of Perth-area viewers at zero ad spend. The key is consistency — one Reel per week beats one perfect Reel per quarter.</p>
<p><strong>Typical Perth cost:</strong> $200–$600 per edited Reel (editing only)</p>
<p>See our <a href="instagram-reels-editing-perth.html">Instagram Reels editing service</a>.</p>

<h2>4. Behind-the-Scenes / Culture Video</h2>
<p><strong>Best for:</strong> Any business trying to attract customers or staff who value authenticity</p>
<p>People buy from people they like and trust. A 2–3 minute "day in the life" or "meet the team" video humanises your brand in a way no amount of polished marketing copy can. For trade businesses, showing the quality of your work in action is especially powerful.</p>
<p><strong>Typical Perth cost:</strong> $800–$2,500 for a half-day shoot and edit</p>

<h2>5. Product or Service Demo Video</h2>
<p><strong>Best for:</strong> eCommerce, SaaS, physical products, any business with a visual service</p>
<p>Show, don't tell. A demo video showing your product or service in action — before and after, step by step, or in real-world use — reduces purchase anxiety and dramatically increases conversion rates on product pages and sales proposals.</p>
<p><strong>Typical Perth cost:</strong> $600–$2,000 (editing only from supplied footage)</p>
<p>See our <a href="product-video-perth.html">product video service</a>.</p>

<h2>How to Choose</h2>
<p>If you're just starting out, begin with a testimonial video and a social Reel series. These two formats give you the trust-building and reach you need without a large upfront investment. Add an explainer video once you've validated your messaging. Build from there.</p>
<p>Perth Content can help you plan and produce all five formats. <a href="contact.html">Get a free consultation.</a></p>"""
  },
  {
    "slug": "blog-drone-footage-real-estate-marketing-perth",
    "title": "How Drone Footage Is Used in Real Estate Marketing in Perth",
    "tag": "Real Estate", "date": "2026-08-24", "date_display": "24 August 2026", "read_time": 5,
    "meta": "Perth agents use drone footage to sell properties faster. Learn how aerial video fits into a complete real estate marketing strategy and when it's worth the investment.",
    "excerpt": "From Cottesloe beachfronts to Joondalup lakeside estates, Perth agents are using drone footage to sell property faster. Here's how aerial video fits into a complete real estate marketing strategy.",
    "body": """<p>Perth's property market is one of the most visually diverse in Australia. Oceanfront homes in Cottesloe, acreage in the Swan Valley, lakeside estates in Joondalup, and leafy prestige streets in Nedlands and Dalkeith — these properties have context that ground-level photography simply can't capture. That's where drone footage changes everything.</p>

<h2>Why Drone Footage Sells Property</h2>
<p>Aerial footage does three things that still photography can't:</p>
<ul>
  <li><strong>Context:</strong> Shows the property in relation to its surroundings — proximity to the beach, parkland, schools, or the CBD. Buyers understand the lifestyle, not just the bricks.</li>
  <li><strong>Scale:</strong> Large blocks, expansive gardens, and commercial properties look completely different from the air. Aerial footage communicates size accurately in a way floor plans alone can't.</li>
  <li><strong>Emotion:</strong> A sweeping drone shot of a Cottesloe property at golden hour, ocean glittering in the background, triggers an emotional response that converts browsers into enquiries.</li>
</ul>

<h2>Perth Properties That Benefit Most from Drone Footage</h2>
<ul>
  <li>Waterfront and ocean-view properties (Cottesloe, Mosman Park, Scarborough, Sorrento)</li>
  <li>Large residential blocks (750m²+)</li>
  <li>Acreage and rural properties in the Swan Valley and outer suburbs</li>
  <li>Commercial and industrial properties where surrounding access matters</li>
  <li>New developments and display homes where the estate context is a selling point</li>
  <li>Properties near parks, reserves, or notable landmarks</li>
</ul>

<h2>CASA Regulations for Drone Filming in WA</h2>
<p>Drone operators in Australia are regulated by the Civil Aviation Safety Authority (CASA). For commercial real estate drone work, you must use a licensed drone operator with a Remote Pilot Licence (RePL) and operator accreditation. Penalties for unlicensed commercial drone use are significant.</p>
<p>When hiring a drone videographer in Perth, always confirm they hold current CASA accreditation and appropriate insurance. This protects both you and your client.</p>

<h2>What to Expect from a Drone Shoot</h2>
<ul>
  <li><strong>Timing:</strong> Golden hour (the 30–60 minutes after sunrise or before sunset) produces the most cinematic results. Plan your shoot accordingly.</li>
  <li><strong>Weather:</strong> Wind above 20–25 knots makes drone footage unstable. Your operator will monitor conditions and may reschedule if needed.</li>
  <li><strong>Duration:</strong> A typical drone session for a single property is 45–90 minutes on-site, producing 10–30 minutes of raw footage.</li>
  <li><strong>Editing:</strong> Expect the edited drone footage to be 30–90 seconds of highlight material, integrated into the full property video.</li>
</ul>

<h2>Integrating Drone with Ground-Level Video</h2>
<p>The strongest real estate videos combine both perspectives: drone establishes the location and lifestyle, ground-level footage shows the interior quality and detail. A typical structure:</p>
<ol>
  <li>Opening drone shot establishing the suburb and property position (5–10 sec)</li>
  <li>Ground-level exterior walkthrough</li>
  <li>Interior room-by-room showcase</li>
  <li>Lifestyle B-roll (pool, garden, kitchen, morning light)</li>
  <li>Closing drone shot pulling away from the property</li>
</ol>

<h2>Cost of Drone Add-On in Perth</h2>
<ul>
  <li>Drone footage add-on to existing video package: $500–$1,000</li>
  <li>Drone-only package (filming + edited footage): $600–$1,500</li>
  <li>Premium package with licensed operator and multiple battery runs: $1,000–$2,000+</li>
</ul>

<p>Perth Content works with licensed drone operators across the Perth metro area. Our <a href="drone-video-editing-perth.html">drone video editing service</a> can transform raw aerial footage into a polished, emotion-driven property video. For end-to-end real estate video production, see our <a href="real-estate-video-perth.html">real estate video service</a>.</p>
<p><a href="contact.html" class="btn btn-primary">Get a Drone Video Quote</a></p>"""
  },
]

for p in POSTS:
    html = page(p)
    path = os.path.join(OUT, f"{p['slug']}.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✓ {p['slug']}.html")

print(f"\nGenerated {len(POSTS)} files.")
