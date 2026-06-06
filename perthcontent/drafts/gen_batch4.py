#!/usr/bin/env python3
"""Generate batch 4 — 10 new Perth Content draft blog posts (Dec 2026 – Feb 2027)."""

import os

OUT = os.path.dirname(os.path.abspath(__file__))

NAV = """<header class="site-header">
  <div class="container header-inner">
    <a href="index.html" class="logo">Perth<span>Content</span></a>
    <nav class="main-nav" id="main-nav">
      <a href="index.html">Home</a>
      <div class="dropdown">
        <button class="dropdown-btn">Services &#9660;</button>
        <div class="dropdown-menu">
          <a href="corporate-video-perth.html">Corporate Video</a>
          <a href="real-estate-video-perth.html">Real Estate Video</a>
          <a href="social-media-video-perth.html">Social Media Video</a>
          <a href="instagram-reels-editing-perth.html">Instagram Reels</a>
          <a href="youtube-video-editing-perth.html">YouTube Editing</a>
          <a href="event-highlight-video-perth.html">Event Highlights</a>
          <a href="explainer-video-perth.html">Explainer Video</a>
          <a href="training-video-perth.html">Training Video</a>
          <a href="drone-video-editing-perth.html">Drone Video</a>
          <a href="restaurant-hospitality-video-perth.html">Restaurant &amp; Hospitality</a>
          <a href="wedding-videography-perth.html">Wedding Video</a>
          <a href="product-video-perth.html">Product Video</a>
          <a href="promotional-video-perth.html">Promotional Video</a>
          <a href="linkedin-video-perth.html">LinkedIn Video</a>
          <a href="startup-video-perth.html">Startup Video</a>
          <a href="tiktok-video-editing-perth.html">TikTok Editing</a>
          <a href="conference-seminar-video-perth.html">Conference &amp; Seminar</a>
          <a href="fitness-wellness-video-perth.html">Fitness &amp; Wellness</a>
          <a href="testimonial-video-perth.html">Testimonial Video</a>
          <a href="annual-report-video-perth.html">Annual Report Video</a>
        </div>
      </div>
      <a href="about.html">About</a>
      <a href="portfolio.html">Portfolio</a>
      <a href="blog.html" class="active">Blog</a>
      <a href="contact.html" class="btn btn-primary">Get a Quote</a>
    </nav>
    <div class="header-right">
      <button class="hamburger" id="hamburger" aria-label="Open menu" aria-expanded="false">&#9776;</button>
    </div>
  </div>
</header>"""

SIDEBAR = """    <aside class="post-sidebar">
      <div class="post-sidebar-card">
        <h4>Get a Free Quote</h4>
        <form action="https://formspree.io/f/mzdodayb" method="POST" data-formspree data-success-id="sidebar-success-{sid}">
          <div class="form-row">
            <div><label for="{sid}-name">Name</label><input id="{sid}-name" type="text" name="name" placeholder="Your name" required /></div>
            <div><label for="{sid}-email">Email</label><input id="{sid}-email" type="email" name="email" placeholder="Your email" required /></div>
            <div><label for="{sid}-svc">Service</label>
              <select id="{sid}-svc" name="service">
                <option value="">Select&#8230;</option>
                <option>Corporate Video</option>
                <option>Real Estate Video</option>
                <option>Social Media Content</option>
                <option>Explainer Video</option>
                <option>Wedding &amp; Event</option>
                <option>Other</option>
              </select>
            </div>
            <button type="submit" class="btn btn-primary">Get Quote</button>
          </div>
        </form>
        <div id="sidebar-success-{sid}" hidden style="display:none;" class="form-success">&#10003; We'll be in touch shortly!</div>
      </div>
      <div class="post-sidebar-card">
        <h4>Popular Services</h4>
        <ul>
          <li><a href="corporate-video-perth.html">Corporate Video Perth</a></li>
          <li><a href="real-estate-video-perth.html">Real Estate Video Perth</a></li>
          <li><a href="social-media-video-perth.html">Social Media Video Perth</a></li>
          <li><a href="explainer-video-perth.html">Explainer Video Perth</a></li>
          <li><a href="drone-video-editing-perth.html">Drone Video Editing Perth</a></li>
        </ul>
      </div>
    </aside>"""

FOOTER = """<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <a href="index.html" class="logo">Perth<span>Content</span></a>
        <p>Perth's video content marketplace — connecting businesses with expert editors and producers.</p>
      </div>
      <div class="footer-col">
        <h4>Top Services</h4>
        <a href="corporate-video-perth.html">Corporate Video</a>
        <a href="real-estate-video-perth.html">Real Estate Video</a>
        <a href="social-media-video-perth.html">Social Media Video</a>
        <a href="explainer-video-perth.html">Explainer Video</a>
        <a href="wedding-videography-perth.html">Wedding Video</a>
      </div>
      <div class="footer-col">
        <h4>Company</h4>
        <a href="about.html">About Us</a>
        <a href="portfolio.html">Portfolio</a>
        <a href="blog.html">Blog</a>
        <a href="contact.html">Contact</a>
      </div>
      <div class="footer-col">
        <h4>More Services</h4>
        <a href="drone-video-editing-perth.html">Drone Video</a>
        <a href="instagram-reels-editing-perth.html">Instagram Reels</a>
        <a href="tiktok-video-editing-perth.html">TikTok Editing</a>
        <a href="testimonial-video-perth.html">Testimonial Video</a>
        <a href="event-highlight-video-perth.html">Event Highlights</a>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; <span id="year"></span> Perth Content. All rights reserved.</p>
      <p>Serving Perth, WA — Professional Video Editing &amp; Production</p>
    </div>
  </div>
</footer>
<script src="js/main.js"></script>"""

def page(p):
    sid = p["slug"].replace("blog-", "").replace("-", "")[:12]
    sidebar = SIDEBAR.replace("{sid}", sid)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="{p['meta']}" />
  <meta name="robots" content="index, follow" />
  <title>{p['title']} | Perth Content</title>
  <link rel="canonical" href="https://perthcontent.com/{p['slug']}.html" />
  <meta property="og:title" content="{p['title']}" />
  <meta property="og:description" content="{p['meta']}" />
  <meta property="og:url" content="https://perthcontent.com/{p['slug']}.html" />
  <meta property="og:type" content="article" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="css/style.css" />
  <script type="application/ld+json">{{"@context":"https://schema.org","@type":"Article","headline":"{p['title']}","description":"{p['meta']}","datePublished":"{p['date']}","author":{{"@type":"Organization","name":"Perth Content"}},"publisher":{{"@type":"Organization","name":"Perth Content","url":"https://perthcontent.com"}}}}</script>
</head>
<body>

{NAV}

<section class="page-hero">
  <div class="container">
    <div class="breadcrumb"><a href="index.html">Home</a> &rsaquo; <a href="blog.html">Blog</a> &rsaquo; {p['tag']}</div>
    <h1>{p['title']}</h1>
    <p>{p['excerpt']}</p>
  </div>
</section>

<section class="blog-post">
  <div class="container blog-post-layout">
    <article class="blog-post-content">
      <div class="post-meta">
        <span>&#128197; {p['date_display']}</span>
        <span>&#127991; {p['tag']}</span>
        <span>&#9200; {p['read_time']} min read</span>
      </div>

{p['body']}

      <p><a href="contact.html" class="btn btn-primary">Talk to Perth Content Today</a></p>

    </article>

{sidebar}
  </div>
</section>

<section class="cta-section">
  <div class="container">
    <h2>Ready to Create Stunning Video Content?</h2>
    <p>Get a free quote from Perth Content — we respond within 2 business hours.</p>
    <div class="cta-btns">
      <a href="contact.html" class="btn btn-amber btn-lg">Get a Free Quote</a>
      <a href="services.html" class="btn btn-outline-white">View Our Services</a>
    </div>
  </div>
</section>

{FOOTER}
</body>
</html>"""

POSTS = [
  {
    "slug": "blog-colour-grading-business-video-perth",
    "title": "Colour Grading for Business Videos — What Perth Companies Need to Know",
    "tag": "How-To",
    "date": "2026-12-14",
    "date_display": "14 December 2026",
    "read_time": 5,
    "meta": "Colour grading transforms raw footage into polished, on-brand business video. Here's what Perth companies need to know about colour correction, LUTs, and how to brief your editor.",
    "excerpt": "Colour grading is one of the most powerful — and most overlooked — steps in video post-production. Here's what Perth businesses need to know about it.",
    "body": """      <p>You've seen the difference between a flat, ungraded video and a professional production — even if you couldn't name it. That difference is often colour grading. For Perth businesses investing in video content, understanding colour grading helps you brief your editor better, set realistic expectations, and get a final product that truly reflects your brand.</p>

      <h2>Colour Correction vs Colour Grading — What's the Difference?</h2>
      <p>These two terms are often used interchangeably, but they describe different stages of the editing process:</p>
      <ul>
        <li><strong>Colour correction</strong> fixes technical problems — exposure issues, white balance inconsistencies, skin tone accuracy. It makes footage look natural and balanced.</li>
        <li><strong>Colour grading</strong> is the creative step — applying a specific look, mood, or stylistic treatment. It's where raw, corrected footage becomes cinematic, warm, moody, or energetic.</li>
      </ul>
      <p>Professional Perth video editors handle both, typically in that order. Correction first, then creative grading on top.</p>

      <h2>Why Colour Matters for Brand Video</h2>
      <p>Colour carries emotional weight. A warm, golden grade says something different from a cool, desaturated corporate look. For Perth businesses, the colour treatment of your video should align with your brand identity:</p>
      <ul>
        <li>A <a href="real-estate-video-perth.html">real estate video</a> in Perth's coastal suburbs benefits from bright, warm, high-contrast grades that make properties feel aspirational.</li>
        <li>A <a href="corporate-video-perth.html">corporate brand video</a> might use a cleaner, neutral grade with subtle colour accents matching the company's brand palette.</li>
        <li>A <a href="fitness-wellness-video-perth.html">fitness or wellness video</a> might use high contrast and vivid saturation to convey energy and intensity.</li>
      </ul>

      <h2>What Are LUTs and Should You Care?</h2>
      <p>LUTs (Look-Up Tables) are preset colour transforms that editors apply to footage to instantly achieve a specific look. They're the editing equivalent of Instagram filters — but far more sophisticated.</p>
      <p>Professional editors often start with a LUT as a base and then fine-tune. If your business has worked with a videographer before and has reference footage you love, your editor can reverse-engineer the look or use it as a creative brief. Saying "I want something like our last brand video" is completely valid creative direction.</p>

      <h2>How to Brief Your Editor on Colour</h2>
      <p>Most Perth business owners don't think about colour when briefing a video editor — and that's fine. But if you want more control over the final look, here's how to communicate it effectively:</p>
      <ul>
        <li><strong>Share reference videos:</strong> Find 2–3 videos whose look and feel you like. These don't need to be in your industry — just videos that match the mood you're after.</li>
        <li><strong>Describe mood, not technical specs:</strong> "Warm and inviting" or "clean and corporate" gives your editor better direction than "I want saturation at 40%."</li>
        <li><strong>Share your brand colours:</strong> A good editor can incorporate your primary and secondary palette into the grade subtly — in highlights, shadows, or ambient tones.</li>
        <li><strong>Specify skin tone priority:</strong> If your video features people, accurate, flattering skin tones are non-negotiable. Make sure this is a stated priority.</li>
      </ul>

      <h2>What Software Do Perth Video Editors Use for Colour?</h2>
      <p>Most professional Perth video editors use <strong>DaVinci Resolve</strong> for colour grading — it's the industry standard, used by major film productions worldwide. Adobe Premiere Pro and Final Cut Pro also have capable colour tools and are common in the local market.</p>
      <p>DaVinci Resolve's dedicated Colour page gives editors node-based control over every aspect of the image — far beyond what most hobbyist tools offer. If your project needs precision colour work (e.g., a brand film or commercial), confirm your editor works in Resolve.</p>

      <h2>Does Colour Grading Cost Extra?</h2>
      <p>In most Perth video editing quotes, basic colour correction is included as standard. Advanced creative grading — particularly for longer projects, multi-camera shoots, or heavily stylised looks — may be quoted separately. Ask your editor upfront what's included so there are no surprises.</p>
      <p>For most <a href="social-media-video-perth.html">social media content</a> and standard business video, the included correction and light grade is more than sufficient. For brand films, commercials, or high-end event productions, investing in dedicated colour grading is worth it.</p>"""
  },
  {
    "slug": "blog-vertical-video-guide-perth-businesses",
    "title": "Vertical Video in 2025 — A Perth Business Guide to Reels, Shorts, and TikTok",
    "tag": "Social Media",
    "date": "2026-12-21",
    "date_display": "21 December 2026",
    "read_time": 5,
    "meta": "Vertical video dominates social media in 2025. Perth businesses that master Reels, YouTube Shorts, and TikTok are capturing reach that landscape video simply can't. Here's your complete guide.",
    "excerpt": "Vertical video now dominates every major social platform. Perth businesses that haven't adapted are leaving enormous organic reach on the table — here's how to fix that.",
    "body": """      <p>The shift is complete. Vertical video — 9:16 aspect ratio, designed for mobile screens — is now the default format on the platforms that drive the most social engagement. Instagram Reels, YouTube Shorts, TikTok, and Facebook Reels all prioritise vertical content in their algorithms. For Perth businesses still producing landscape-only video, this represents a significant missed opportunity.</p>

      <h2>Why Vertical Video Outperforms Landscape on Social</h2>
      <p>The mechanics are simple: over 90% of people hold their phone vertically when browsing social media. Vertical video fills the entire screen, creating an immersive experience that landscape video can't match on mobile. The algorithms know this — they reward content that gets watched to completion, and vertical video consistently outperforms landscape on watch-through rate.</p>
      <p>The result: vertical video typically gets 2–3x more organic reach than equivalent landscape content posted to the same accounts.</p>

      <h2>Platform-by-Platform Guide for Perth Businesses</h2>

      <h3>Instagram Reels</h3>
      <p>Reels remain Instagram's highest-reach format by a wide margin. For Perth businesses, Reels work best when they're:</p>
      <ul>
        <li>Under 60 seconds for maximum algorithm boost</li>
        <li>Captioned (most Perth users watch on mute)</li>
        <li>Locally relevant — mentioning Perth suburbs, locations, or landmarks increases engagement</li>
        <li>Posted 3–5 times per week for consistent reach</li>
      </ul>
      <p>Our <a href="instagram-reels-editing-perth.html">Instagram Reels editing service</a> handles the cutting, captioning, and formatting for Perth businesses who shoot their own footage.</p>

      <h3>YouTube Shorts</h3>
      <p>Shorts are YouTube's answer to TikTok and one of the fastest-growing content formats on the platform. They appear in a dedicated Shorts feed and can also appear in regular YouTube search results — meaning Shorts can drive traffic to your longer-form content.</p>
      <p>Perth businesses in trades, professional services, and real estate are finding strong traction on Shorts with tips, walkthroughs, and before-and-after content.</p>

      <h3>TikTok</h3>
      <p>TikTok's algorithm is uniquely democratic — content from zero-follower accounts can go viral based purely on engagement. For Perth businesses, TikTok works best for industries with visual processes: construction, food, fitness, beauty, real estate, and trades. Our <a href="tiktok-video-editing-perth.html">TikTok editing service</a> can turn raw footage into platform-native content.</p>

      <h2>How to Shoot Vertical Video for Your Perth Business</h2>
      <p>If you're shooting yourself, keep these principles in mind:</p>
      <ul>
        <li><strong>Frame for 9:16 from the start.</strong> Don't crop landscape footage — it degrades quality and cuts off key information. Hold your phone vertically or set your camera to 9:16 mode.</li>
        <li><strong>Keep the subject centred.</strong> Text overlays and captions typically appear in the top and bottom thirds — keep your key action in the middle 50% of the frame.</li>
        <li><strong>Shoot in good light.</strong> Natural light near a window is sufficient for most talking-head or demonstration content.</li>
        <li><strong>Keep it moving.</strong> Vertical video audiences have high expectations for pacing. Aim for a new visual element, cut, or caption every 2–3 seconds.</li>
      </ul>

      <h2>Can You Repurpose Landscape Video Into Vertical?</h2>
      <p>Yes — with caveats. A skilled editor can reframe landscape footage into vertical using crop-and-pan techniques, adding background blur or branded graphics to fill the empty frame space. The result isn't as good as native vertical footage, but it's far better than posting nothing. This is a common approach for Perth businesses converting older brand films or testimonials into social-ready content.</p>

      <h2>Batch Vertical Content for Efficiency</h2>
      <p>The most efficient approach for Perth businesses is to batch your vertical content. Set aside one shoot day per month, record 10–15 short clips in a single session, and have them edited into a month's worth of Reels, Shorts, and TikToks. This keeps your content calendar full without requiring constant production effort. <a href="contact.html">Talk to us about a monthly retainer</a> that handles your vertical content end-to-end.</p>"""
  },
  {
    "slug": "blog-behind-scenes-video-content-perth",
    "title": "Behind the Scenes Video Content — Why Perth Businesses Should Be Sharing It",
    "tag": "Strategy",
    "date": "2026-12-28",
    "date_display": "28 December 2026",
    "read_time": 5,
    "meta": "Behind the scenes video content builds more trust than polished promotional video. Here's why Perth businesses should be sharing their process, people, and workspace on video.",
    "excerpt": "The most effective trust-building video for Perth businesses isn't always the most polished. Here's why behind the scenes content outperforms traditional promotional video.",
    "body": """      <p>There's a counterintuitive truth in business video content: the less polished it looks, the more trust it often builds. Behind the scenes (BTS) content — raw, process-driven video that shows the real work behind your business — consistently outperforms traditional promotional video on engagement, shares, and enquiry conversion. For Perth businesses, it's one of the highest-return content types available.</p>

      <h2>Why Behind the Scenes Video Works So Well</h2>
      <p>Promotional video tells people how good you are. Behind the scenes video <em>shows</em> them. That distinction matters enormously to modern buyers who are deeply sceptical of polished marketing claims and hungry for authentic evidence.</p>
      <p>BTS content works because it:</p>
      <ul>
        <li><strong>Reduces buyer risk:</strong> Seeing the actual process, the real team, and the real workspace eliminates uncertainty before the first conversation.</li>
        <li><strong>Humanises your brand:</strong> People buy from people. BTS content introduces the humans behind your business in a way no headshot or bio can match.</li>
        <li><strong>Demonstrates expertise without claiming it:</strong> Showing your process — the craftsmanship, the attention to detail, the care you take — demonstrates competence far more credibly than asserting it.</li>
        <li><strong>Performs exceptionally on social media:</strong> Authentic, unscripted content gets more comments, saves, and shares than polished promotional posts.</li>
      </ul>

      <h2>What BTS Content Works for Perth Businesses?</h2>

      <h3>Trades and Construction</h3>
      <p>Perth trades businesses have an enormous BTS content opportunity. Time-lapses of installations, before-and-after reveals, footage of tricky jobs being solved — this content is genuinely fascinating and performs extremely well on Instagram and TikTok. A plumber showing a drain rescue, a builder doing a frame walk-through, an electrician explaining a switchboard upgrade — all captivating for homeowners in the research phase.</p>

      <h3>Professional Services</h3>
      <p>Law firms, accountants, and consultants often assume BTS doesn't apply to them — but that's wrong. Office culture, team introductions, client meeting processes (anonymised), and "day in the life" content all work well and help prospects feel comfortable before they reach out.</p>

      <h3>Hospitality and Retail</h3>
      <p>Perth restaurants, cafes, and retailers have some of the most shareable BTS content available: kitchen prep, barista process, product sourcing stories, arrival of new stock. Customers who see behind your operation become advocates for your business.</p>

      <h3>Creative Services</h3>
      <p>Designers, videographers, photographers, and marketers can showcase their actual workflow — mood boarding, colour grading sessions, set building, shoot day footage. It educates prospects about what they're buying before they buy it.</p>

      <h2>How to Capture BTS Content Without Disrupting Your Workflow</h2>
      <p>The most common objection is time. Here's how Perth businesses can capture BTS content with minimal disruption:</p>
      <ul>
        <li><strong>Designate a "content capture" person:</strong> One team member with a phone, tasked with capturing 2–3 clips per day. No filming, no sound — just point and shoot.</li>
        <li><strong>Set up a camera on a tripod:</strong> For consistent location shots (a workshop, a kitchen, a treatment room), a fixed camera on a tripod captures ambient footage automatically.</li>
        <li><strong>Batch the editing:</strong> Accumulate a week of raw clips, then send them to your editor in one batch. The edited content drips out daily or every few days.</li>
      </ul>

      <h2>The Role of Professional Editing in BTS Content</h2>
      <p>BTS content doesn't need to look like a Hollywood production — but it does need to be watchable. Poor audio, shaky footage, and unstructured clips undermine the trust you're trying to build. A professional editor can take rough BTS footage and transform it into compelling, platform-optimised content with captions, music, pacing, and colour correction.</p>
      <p>Our <a href="social-media-video-perth.html">social media video editing service</a> specialises in exactly this — taking authentic Perth business footage and making it polished enough to convert. <a href="contact.html">Get in touch to discuss a monthly BTS content package.</a></p>"""
  },
  {
    "slug": "blog-food-restaurant-video-perth",
    "title": "Food and Restaurant Video Content — A Perth Hospitality Guide",
    "tag": "Strategy",
    "date": "2027-01-04",
    "date_display": "4 January 2027",
    "read_time": 5,
    "meta": "Perth restaurants and cafes using video content are driving more bookings, more social engagement, and more loyal regulars. Here's the complete guide to hospitality video in Perth.",
    "excerpt": "Perth's hospitality scene is competitive. Restaurants and cafes using video are pulling ahead — here's the playbook for food and hospitality video content that actually drives bookings.",
    "body": """      <p>Perth's restaurant and hospitality scene is one of the most competitive in Australia. From Fremantle's waterfront dining to Northbridge's late-night venues, the city's food culture is sophisticated and demanding. In this environment, video content has become one of the most powerful tools for attracting new customers, driving repeat visits, and building the kind of loyal following that sustains a hospitality business long-term.</p>

      <h2>Why Video Works Particularly Well for Hospitality</h2>
      <p>Food is inherently visual. The sizzle of a steak, the pour of a coffee, the cross-section of a perfectly crafted burger — these moments trigger appetite and desire in a way that text menus and static photos can't match. Video adds motion, sound, and sensory immediacy that makes food genuinely irresistible.</p>
      <p>The data backs this up: restaurants with video content on social media see significantly higher engagement rates than those relying on photos alone, and video ads for hospitality businesses consistently outperform static image ads on click-through and conversion.</p>

      <h2>The Types of Video That Work Best for Perth Restaurants</h2>

      <h3>Hero Dish Videos</h3>
      <p>Short, beautiful close-up videos of your signature dishes — the pour, the steam, the texture. These are the most shareable hospitality content format on Instagram and TikTok, and they perform best when they're 10–30 seconds with ambient sound or music. No voiceover needed; the food speaks for itself.</p>

      <h3>Chef and Kitchen Process Videos</h3>
      <p>Perth diners love seeing how their food is made. Kitchen process videos — showing prep, technique, and craft — build extraordinary credibility and trust. They're particularly effective for venues with a clear culinary philosophy: woodfire kitchens, nose-to-tail cooking, house-fermented products.</p>

      <h3>Venue Atmosphere Videos</h3>
      <p>A 60–90 second venue tour showing the ambience, lighting, outdoor areas, and the energy of a busy service helps potential guests visualise their experience before they book. These are essential for function venues and date-night restaurants where atmosphere is part of what's being sold.</p>

      <h3>Team and Story Videos</h3>
      <p>Perth locals support local. A brief story about why your venue exists, who built it, and what drives your team creates an emotional connection that converts first-time visitors into regulars. These perform well on Facebook and YouTube where slightly longer content gets engagement.</p>

      <h2>Platform Strategy for Perth Hospitality</h2>
      <ul>
        <li><strong>Instagram:</strong> The primary platform for Perth food content. Reels under 30 seconds, Stories for daily updates and specials, Feed for polished hero shots.</li>
        <li><strong>TikTok:</strong> Growing rapidly in Perth's under-40 food audience. Kitchen process videos and "day in the life" content perform well. Our <a href="tiktok-video-editing-perth.html">TikTok editing service</a> can handle the formatting.</li>
        <li><strong>Facebook:</strong> Still important for Perth's 35+ demographic and for event promotion, function bookings, and longer-form content.</li>
        <li><strong>Google Business Profile video:</strong> Often overlooked — short venue videos on your GMB listing appear in Maps and local search results and directly impact booking intent.</li>
      </ul>

      <h2>What Does Hospitality Video Cost in Perth?</h2>
      <p>A professional food and hospitality video shoot in Perth typically ranges from $800 for a half-day hero dish shoot to $3,000–$5,000 for a full venue brand film. For <a href="restaurant-hospitality-video-perth.html">Perth restaurant video production</a>, we typically recommend starting with a monthly content package — one shoot day producing 8–12 pieces of edited content — rather than one large brand film that dates quickly.</p>
      <p>This gives you fresh, seasonal content that keeps your feeds active and your Google Business Profile updated year-round. <a href="contact.html">Talk to us about a hospitality content package.</a></p>"""
  },
  {
    "slug": "blog-animation-vs-live-action-video-perth",
    "title": "Animation vs Live Action — Which Works Best for Perth Businesses?",
    "tag": "How-To",
    "date": "2027-01-11",
    "date_display": "11 January 2027",
    "read_time": 5,
    "meta": "Animation and live action video each have distinct strengths for Perth businesses. Here's how to choose the right format for your industry, budget, and marketing goals.",
    "excerpt": "Should your Perth business use animation or live action for its next video project? Here's a practical guide to choosing the right format for your goals and budget.",
    "body": """      <p>One of the most common questions Perth businesses ask when starting a video project is whether to go animated or live action. Both formats are effective — but they excel in different contexts. Understanding the strengths and limitations of each helps you make the right call for your specific goals, audience, and budget.</p>

      <h2>The Case for Animation</h2>
      <p>Animation excels when:</p>
      <ul>
        <li><strong>Your product or service is abstract or invisible.</strong> Software platforms, financial products, insurance, SaaS tools, and professional services are hard to film. Animation makes the invisible visible — showing data flows, processes, and concepts that live action simply can't capture.</li>
        <li><strong>You need to simplify complexity.</strong> An <a href="explainer-video-perth.html">animated explainer video</a> can condense a complicated process into 90 seconds of clear, engaging visuals. Perth businesses in fintech, legal, and healthcare often choose animation for this reason.</li>
        <li><strong>You have no footage to work with.</strong> New businesses, pre-launch products, or companies without photogenic physical operations often have nothing to film. Animation solves this completely.</li>
        <li><strong>You need a timeless look.</strong> Live action dates — hair, clothes, office decor, and technology all age. Animation can be styled to remain current for 3–5 years without reshooting.</li>
      </ul>

      <h2>The Case for Live Action</h2>
      <p>Live action outperforms animation when:</p>
      <ul>
        <li><strong>Trust and authenticity are the priority.</strong> Real people, real places, and real products build more trust than animation. For Perth service businesses where the relationship with the client matters, live action <a href="testimonial-video-perth.html">testimonial videos</a> are far more persuasive than animated equivalents.</li>
        <li><strong>Your product is physical and beautiful.</strong> Food, real estate, fashion, fitness, automotive, and retail products are best shown, not illustrated. The texture, the movement, the sensory reality of a physical product demands live footage.</li>
        <li><strong>You want to feature your team.</strong> Seeing the real humans behind a Perth business — their faces, their environment, their personality — creates connection that no animated character can replicate.</li>
        <li><strong>Budget is a constraint.</strong> Simple live action footage (talking-head interviews, product demonstrations, venue tours) can be produced and edited at lower cost than quality animation.</li>
      </ul>

      <h2>The Hybrid Approach</h2>
      <p>Increasingly, Perth businesses are combining both formats. A live action brand video might use animated graphics to display statistics, illustrate a process, or highlight key messages. This hybrid approach gets the trust-building power of real people alongside the explanatory clarity of animation.</p>
      <p>Common hybrid use cases include:</p>
      <ul>
        <li><a href="corporate-video-perth.html">Corporate brand films</a> with animated data visualisations</li>
        <li>Training videos with live demonstrations plus animated process diagrams</li>
        <li>Social media content combining live footage with animated text and graphics</li>
      </ul>

      <h2>Cost Comparison for Perth</h2>
      <p>Animation and live action have different cost structures. Live action requires shoot costs (crew, location, talent) but lower post-production costs for simple formats. Animation has minimal shoot costs but significant production time in post — especially for custom illustration and character animation.</p>
      <p>Rough benchmarks for Perth:</p>
      <ul>
        <li><strong>Simple motion graphics animation (60–90 sec):</strong> $800–$2,500</li>
        <li><strong>Custom illustrated animation (60–90 sec):</strong> $2,500–$8,000</li>
        <li><strong>Live action brand video (2–3 min):</strong> $1,500–$5,000</li>
        <li><strong>Hybrid (live + motion graphics):</strong> $2,000–$6,000</li>
      </ul>
      <p>The right choice depends less on cost and more on what your audience needs to see to make a decision. <a href="contact.html">Talk to us about what format fits your next project.</a></p>"""
  },
  {
    "slug": "blog-instagram-reels-strategy-perth",
    "title": "Instagram Reels Strategy for Perth Businesses — A 2025 Playbook",
    "tag": "Social Media",
    "date": "2027-01-18",
    "date_display": "18 January 2027",
    "read_time": 6,
    "meta": "Instagram Reels are the highest-reach content format available to Perth businesses in 2025. Here's a complete playbook — what to post, how often, and how to turn views into enquiries.",
    "excerpt": "Instagram Reels consistently deliver more organic reach than any other format on the platform. Here's the complete strategy for Perth businesses to turn Reels into a lead generation tool.",
    "body": """      <p>Instagram Reels have fundamentally changed the organic reach equation on the platform. Where a static post might reach 5–10% of your existing followers, a well-crafted Reel can reach tens of thousands of non-followers in Perth and beyond — purely through algorithmic distribution. For Perth businesses willing to invest in this format, Reels represent one of the most cost-effective awareness channels available in 2025.</p>

      <h2>How the Reels Algorithm Works (And How to Work With It)</h2>
      <p>Instagram's Reels algorithm prioritises content based on watch-through rate, replays, saves, and shares. Likes and comments matter less than they used to. This means your goal with every Reel is to:</p>
      <ul>
        <li>Hook the viewer in the first 1–2 seconds so they don't scroll</li>
        <li>Keep them watching to the end (or beyond — loops count as replays)</li>
        <li>Create content worth saving or sharing to friends</li>
      </ul>
      <p>For Perth businesses, this reframes the entire content brief. You're not making ads — you're making content people genuinely want to watch.</p>

      <h2>What Reels Format Works for Perth Businesses?</h2>

      <h3>Tips and How-To Content</h3>
      <p>The most consistently high-performing format across industries. A tradie sharing "3 signs your roof needs replacing." A mortgage broker explaining "how to improve your borrowing capacity." A chef demonstrating a simple technique. This format works because it delivers genuine value and positions you as an expert without asking for anything in return.</p>

      <h3>Before and After</h3>
      <p>Universally effective for any business with a transformation process — cleaners, landscapers, renovators, personal trainers, beauty professionals. The payoff of the reveal keeps viewers watching to the end, which the algorithm rewards heavily.</p>

      <h3>Behind the Scenes</h3>
      <p>Day-in-the-life content, showing your process, your team, or your workspace. This builds the kind of authentic connection that converts followers into clients over time. Perth audiences in particular respond well to local, genuine content rather than polished corporate messaging.</p>

      <h3>Myth-Busting</h3>
      <p>"Myth: you need a big budget to produce great video." "Truth: [explanation]." This format drives high comment engagement as viewers agree, disagree, and share their own experiences — all signals that push the content to more people.</p>

      <h2>Posting Frequency and Consistency</h2>
      <p>Instagram's algorithm rewards consistency. For Perth businesses starting a Reels strategy, we recommend:</p>
      <ul>
        <li><strong>Minimum:</strong> 2 Reels per week to see consistent growth</li>
        <li><strong>Optimal:</strong> 4–5 Reels per week for aggressive reach building</li>
        <li><strong>Sustainable:</strong> Batch-shoot once per month, edit to schedule across the weeks</li>
      </ul>
      <p>The biggest mistake Perth businesses make is posting inconsistently — 10 Reels one week, then nothing for a month. The algorithm penalises dormant accounts.</p>

      <h2>Turning Reels Views Into Enquiries</h2>
      <p>Views are vanity if they don't convert. The path from Reel to enquiry requires:</p>
      <ul>
        <li><strong>A clear bio with a call to action:</strong> "DM 'QUOTE' for a free video quote" or a link to your contact page</li>
        <li><strong>Engagement in comments:</strong> Respond to every comment in the first hour — this signals to the algorithm that the post is active</li>
        <li><strong>Occasional direct CTAs:</strong> Not every Reel needs a hard sell, but include a CTA caption in 1 in 4 posts ("Link in bio for a free quote")</li>
        <li><strong>Consistent posting so viewers see you repeatedly:</strong> Most Perth clients won't enquire after one Reel — they need repeated exposure before they reach out</li>
      </ul>

      <h2>Getting Your Reels Edited Professionally</h2>
      <p>You don't need to master video editing to run a successful Reels strategy. Our <a href="instagram-reels-editing-perth.html">Instagram Reels editing service</a> handles the cutting, captioning, music licensing, colour correction, and formatting — you just supply the raw footage from your phone. Many Perth business owners film on their iPhone and send us the clips weekly. <a href="contact.html">Get in touch to discuss a Reels editing package.</a></p>"""
  },
  {
    "slug": "blog-video-seo-youtube-perth-businesses",
    "title": "Video SEO — How to Get Your Perth Business Videos Found on YouTube",
    "tag": "Strategy",
    "date": "2027-01-25",
    "date_display": "25 January 2027",
    "read_time": 6,
    "meta": "YouTube is the world's second-largest search engine. Perth businesses that optimise their video content for search can capture leads searching for exactly what they offer. Here's how.",
    "excerpt": "YouTube SEO is one of the most underutilised strategies for Perth businesses. Here's how to optimise your videos to rank in YouTube and Google search results.",
    "body": """      <p>Most Perth businesses think of YouTube as a place to upload videos — not as a search engine to rank in. That's a missed opportunity. YouTube processes over 3 billion searches per month, and videos optimised for YouTube often appear directly in Google search results as well. For Perth businesses, a well-optimised YouTube channel can generate consistent, qualified traffic without any paid advertising.</p>

      <h2>Why YouTube SEO Is Different from Website SEO</h2>
      <p>Website SEO ranks pages based on text content, backlinks, and technical factors. YouTube SEO ranks videos based on a different set of signals:</p>
      <ul>
        <li><strong>Video title and description:</strong> Must contain the keywords people are searching for</li>
        <li><strong>Watch time and retention:</strong> How long people watch your video relative to its length</li>
        <li><strong>Click-through rate:</strong> What percentage of people click your video when they see it in search results</li>
        <li><strong>Engagement:</strong> Likes, comments, saves, and shares</li>
        <li><strong>Channel authority:</strong> The overall size and engagement rate of your channel</li>
      </ul>
      <p>The good news: Perth-specific keywords have far less competition than national terms. Ranking for "corporate video production Perth" or "real estate video Perth" is significantly more achievable than ranking for national equivalents.</p>

      <h2>Keyword Research for Perth Business Video</h2>
      <p>Before you film anything, research what your potential clients are actually searching for. Tools like Google's autocomplete, YouTube search suggestions, and free tools like TubeBuddy or vidIQ can reveal the exact phrases Perth buyers use.</p>
      <p>For a Perth video production company, high-value search terms might include:</p>
      <ul>
        <li>"corporate video production Perth cost"</li>
        <li>"how to choose a video editor Perth"</li>
        <li>"real estate video Perth"</li>
        <li>"best video editing software Perth"</li>
      </ul>
      <p>The best YouTube videos for business answer a specific question or solve a specific problem — make that problem your title.</p>

      <h2>Optimising Your Video Title</h2>
      <p>Your title does two jobs: it tells the algorithm what your video is about, and it persuades humans to click. The formula that works: <strong>[Primary keyword] — [Benefit or hook]</strong></p>
      <p>Example: "Corporate Video Production Perth — How Much Does It Cost? (2025 Guide)"</p>
      <p>Keep titles under 60 characters so they don't get truncated in search results. Include the year where relevant — it signals freshness and improves click-through rate.</p>

      <h2>Writing Descriptions That Rank</h2>
      <p>YouTube descriptions should be at least 250 words for videos targeting competitive keywords. Include your primary keyword in the first two sentences, use natural language throughout, and add your key services and location. Always include:</p>
      <ul>
        <li>A direct link to your website (with full URL) in the first few lines</li>
        <li>A call to action ("For a free quote, visit [URL] or call [number]")</li>
        <li>Timestamps for longer videos (chapters improve watch time)</li>
        <li>Relevant tags covering your topic, location, and related terms</li>
      </ul>

      <h2>Thumbnails Are Your #1 Click-Through Factor</h2>
      <p>Custom thumbnails drive significantly higher click-through rates than auto-generated YouTube thumbnails. For Perth business videos, effective thumbnails typically include:</p>
      <ul>
        <li>A clear, large headline (3–5 words maximum)</li>
        <li>High-contrast colours that stand out in search results</li>
        <li>A human face where possible (faces outperform everything else for click-through)</li>
        <li>Your brand colours for channel recognition</li>
      </ul>

      <h2>How Often Should Perth Businesses Post?</h2>
      <p>YouTube rewards consistency over volume. One high-quality, well-optimised video per week outperforms three rushed, unoptimised uploads. For most Perth businesses, starting with one video per fortnight and building a library of evergreen content (how-to guides, FAQ answers, service explanations) is the most sustainable approach.</p>
      <p>Our <a href="youtube-video-editing-perth.html">YouTube video editing service</a> handles the editing, thumbnail creation, and metadata optimisation — so you focus on filming, not post-production. <a href="contact.html">Get a quote for ongoing YouTube editing.</a></p>"""
  },
  {
    "slug": "blog-conference-seminar-video-perth",
    "title": "Conference and Seminar Video Production in Perth — What to Capture",
    "tag": "Events",
    "date": "2027-02-01",
    "date_display": "1 February 2027",
    "read_time": 5,
    "meta": "Perth conferences and seminars generate enormous content opportunities — but only if you capture and edit the right footage. Here's what to film, how to edit it, and how to use it.",
    "excerpt": "A Perth conference or seminar generates a day's worth of footage — but most of it goes unused. Here's how to capture and edit conference video that works for your business for months.",
    "body": """      <p>Perth hosts hundreds of conferences, seminars, and professional events every year — from large-scale industry conferences at the Perth Convention and Exhibition Centre to intimate professional development workshops in Subiaco and West Perth. Every one of these events is a content goldmine. But without a clear capture-and-edit strategy, most of that footage either isn't filmed, or sits on a hard drive never to be used.</p>

      <h2>The Business Case for Conference Video</h2>
      <p>A well-produced conference recap video delivers multiple returns on a single production investment:</p>
      <ul>
        <li><strong>Promotion for next year's event:</strong> Nothing sells tickets better than footage from a successful previous event</li>
        <li><strong>Speaker content:</strong> Keynote clips, packaged for speakers to share, drive huge reach with their existing audiences</li>
        <li><strong>Social media content:</strong> Quotes, highlights, and audience reaction clips across multiple platforms for weeks</li>
        <li><strong>Sponsor deliverables:</strong> Professional video content for sponsors justifies higher sponsorship tiers</li>
        <li><strong>Internal training material:</strong> For companies hosting internal seminars, recorded sessions become permanent training resources</li>
      </ul>

      <h2>What to Film at a Perth Conference or Seminar</h2>

      <h3>The Venue and Atmosphere</h3>
      <p>B-roll of the venue, registration desk, networking areas, and catering establishes the scale and quality of the event. Shoot this before and after the main sessions when crowds are moving and the space is energetic.</p>

      <h3>Keynote Addresses and Panel Sessions</h3>
      <p>These are typically the highest-value content from the event. For <a href="conference-seminar-video-perth.html">Perth conference video</a>, use a minimum of two cameras: one locked-off wide shot of the stage, one operated close-up on the speaker. This gives your editor the raw material to cut a dynamic, engaging presentation video rather than a static single-angle recording.</p>

      <h3>Audience and Reaction Shots</h3>
      <p>Cut-away shots of engaged audience members — nodding, taking notes, laughing at a speaker's point — are essential for making event highlight reels feel alive and credible. Budget time for an operator to capture these throughout sessions.</p>

      <h3>Vox Pops and Delegate Testimonials</h3>
      <p>Brief 30–60 second interviews with delegates about their experience, key takeaways, or why they attend annually. These are gold for event promotion and sponsor reporting. Set up a simple interview spot with branded backdrop near the exit at the end of the day.</p>

      <h3>Sponsor Branding and Activations</h3>
      <p>If your event has sponsors, dedicated coverage of their branding, activations, and signage is often a deliverable in the sponsorship agreement. Ensure your production team knows which sponsors need coverage.</p>

      <h2>Post-Production: What You Get Out of the Raw Footage</h2>
      <p>A well-captured day of conference footage can produce:</p>
      <ul>
        <li>A 2–3 minute event highlight reel (the primary promotional asset)</li>
        <li>Full edited recordings of each keynote or panel session</li>
        <li>10–15 short social media clips (30–60 seconds each) of key moments</li>
        <li>Individual speaker clips for each presenter to share on LinkedIn</li>
        <li>A 30–60 second teaser for next year's event promotion</li>
      </ul>

      <h2>Planning Your Perth Conference Video Production</h2>
      <p>Advance planning is essential. Brief your video production team at least 2–4 weeks before the event with the run sheet, venue layout, key speakers, sponsor requirements, and your content goals. Last-minute arrangements result in missed shots and substandard coverage.</p>
      <p>Our <a href="event-highlight-video-perth.html">event highlight video service</a> covers Perth conferences and seminars with professional multi-camera teams and fast turnaround editing. <a href="contact.html">Get in touch 4+ weeks before your event to secure a team.</a></p>"""
  },
  {
    "slug": "blog-tiktok-perth-service-businesses",
    "title": "TikTok for Perth Service Businesses — Does It Actually Work?",
    "tag": "Social Media",
    "date": "2027-02-08",
    "date_display": "8 February 2027",
    "read_time": 5,
    "meta": "Perth service businesses are discovering TikTok drives real enquiries — not just views. Here's an honest look at what works, what doesn't, and how to get started without a content team.",
    "excerpt": "Perth plumbers, lawyers, real estate agents, and consultants are quietly building audiences — and enquiries — on TikTok. Here's an honest assessment of whether it's right for your business.",
    "body": """      <p>Two years ago, most Perth service businesses would have dismissed TikTok as a platform for teenagers dancing. Today, the fastest-growing demographic on the platform is 25–44 year olds — the exact buyers who hire tradespeople, engage professional services, and make property decisions. TikTok for service businesses is no longer a novelty. For the Perth businesses taking it seriously, it's a lead generation channel.</p>

      <h2>The TikTok Algorithm Advantage</h2>
      <p>TikTok's algorithm is fundamentally different from Instagram or Facebook in one critical way: it doesn't require a large existing audience to reach new people. Every piece of content is evaluated independently and pushed to a test audience based on watch time and engagement. A Perth electrician with 50 followers can post a video that reaches 50,000 Perth homeowners — organically, for free — if the content is engaging enough.</p>
      <p>This democratisation of reach is why Perth service businesses that commit to the platform early often outperform much larger competitors who are slower to adapt.</p>

      <h2>Which Perth Service Businesses Thrive on TikTok?</h2>

      <h3>Trades (High Potential)</h3>
      <p>Perth plumbers, electricians, builders, and landscapers are producing some of the most viewed TikTok content in Australia's service business space. The format is perfect: showing a problem → diagnosing it → fixing it is inherently compelling content that Perth homeowners search for. A video titled "why your hot water system keeps running cold in Perth" solves a real problem and positions the tradie as the obvious person to call.</p>

      <h3>Real Estate (High Potential)</h3>
      <p>Perth's property market is one of the most active in Australia. First-home buyers, investors, and upsizers are all active on TikTok, hungry for local market insights. Agents and buyers' advocates who explain the Perth market plainly and without jargon build significant followings quickly.</p>

      <h3>Professional Services — Law, Finance, Accounting (Medium Potential)</h3>
      <p>Perth professionals who can simplify complex topics for everyday consumers (not other professionals) find strong audiences on TikTok. The key is to avoid industry jargon and speak to the specific situations your clients face: "what to do if your employer doesn't pay super on time" for an employment lawyer, or "how much deposit do you actually need in Perth right now" for a mortgage broker.</p>

      <h3>Retail and Hospitality (High Potential)</h3>
      <p>Product reveals, behind-the-scenes kitchen content, "what's new this week" content — Perth retail and hospitality businesses with photogenic products or processes can build loyal local followings that translate directly into foot traffic.</p>

      <h2>What Doesn't Work on TikTok</h2>
      <p>Several approaches consistently underperform on TikTok for Perth service businesses:</p>
      <ul>
        <li><strong>Repurposed advertising:</strong> TikTok users actively reject anything that looks or feels like a traditional ad. Content needs to look native to the platform.</li>
        <li><strong>Polished corporate video:</strong> TikTok's culture rewards authenticity over production value. A slightly rough, genuine video outperforms a slick production.</li>
        <li><strong>Content without a hook:</strong> You have 1–2 seconds to stop someone from scrolling. Your opening line must immediately signal what they're about to learn or see.</li>
      </ul>

      <h2>Getting Started Without a Content Team</h2>
      <p>You don't need a social media manager or video crew to start on TikTok. The most successful Perth service business accounts are often run by the business owner themselves — talking to camera on their phone, in their work environment, about topics they know inside out.</p>
      <p>The editing — captions, music, pacing, cuts — is where professional help adds the most value. Our <a href="tiktok-video-editing-perth.html">TikTok editing service</a> takes your raw phone footage and transforms it into platform-optimised content ready to post. Many Perth clients film 5–10 clips in one sitting and let us schedule edited versions throughout the month. <a href="contact.html">Get a quote for TikTok content editing.</a></p>"""
  },
  {
    "slug": "blog-video-content-professional-services-perth",
    "title": "Video Content for Perth Professional Services — Law, Finance, and Consulting",
    "tag": "Corporate",
    "date": "2027-02-15",
    "date_display": "15 February 2027",
    "read_time": 5,
    "meta": "Perth law firms, financial advisers, and consultants are using video to build trust before the first meeting. Here's how professional services businesses in Perth should approach video content.",
    "excerpt": "Professional services in Perth face a unique challenge: selling expertise that's invisible until after the engagement. Video solves this — here's how law, finance, and consulting firms are using it.",
    "body": """      <p>Professional services firms face a marketing challenge unlike almost any other industry. You're selling expertise that the client can't evaluate before they buy. They can't test your legal advice before they retain you. They can't assess your financial guidance before they engage you. This information asymmetry creates enormous buyer hesitation — and video is the most powerful tool available to reduce it.</p>

      <h2>Why Video Works Particularly Well for Perth Professional Services</h2>
      <p>Perth's professional services market is relationship-driven. Referrals matter enormously, and decisions are based heavily on trust and perceived expertise. Video addresses both:</p>
      <ul>
        <li><strong>It builds trust before the first contact.</strong> A potential client who has watched three videos of your principal explaining their approach arrives at the first meeting already feeling like they know you. That relationship head-start is worth its weight in gold.</li>
        <li><strong>It demonstrates expertise without claiming it.</strong> Telling people you're an expert sounds like marketing. Explaining a complex topic clearly and accurately proves it.</li>
        <li><strong>It scales your referral network.</strong> Videos that educate or help viewers get shared — extending your reach well beyond existing clients and referrers.</li>
      </ul>

      <h2>Video Content Types That Work for Perth Professional Services</h2>

      <h3>Educational FAQ Videos</h3>
      <p>The highest-value format for most professional services firms. Answer the questions your clients most commonly ask — in plain language, without jargon. A Perth family lawyer explaining "what happens to the family home in a separation" or a financial adviser explaining "how much super should I have at 45" reaches exactly the clients who need their services, at exactly the moment they're researching.</p>
      <p>These videos rank well on YouTube and appear in Google search results, creating a passive enquiry channel that compounds over time.</p>

      <h3>Team Introduction Videos</h3>
      <p>Professional services is about people. A short video introducing each principal or senior adviser — their background, their approach, and what they genuinely enjoy about their work — helps prospects find the person they'll feel most comfortable working with. These reduce the barrier to making first contact significantly.</p>

      <h3>Client Story Videos</h3>
      <p>Case studies told in video format (with client permission and appropriate anonymisation where needed) are extraordinarily persuasive for professional services. "We helped a Perth family business navigate a complex succession" is far more compelling than any credentials list. Our <a href="testimonial-video-perth.html">testimonial video service</a> handles these professionally and sensitively.</p>

      <h3>Process Explainer Videos</h3>
      <p>"What happens when you engage us" — walking a prospect through your onboarding, engagement, and delivery process — is one of the most trust-building videos a professional services firm can create. It eliminates the uncertainty of what working with you actually looks like. An <a href="explainer-video-perth.html">animated explainer video</a> works particularly well for complex multi-step processes.</p>

      <h2>What Perth Professional Services Firms Should Avoid</h2>
      <ul>
        <li><strong>Overly formal, scripted presentations:</strong> Clients want to see the real person, not a rehearsed broadcast. Natural, slightly imperfect delivery is more relatable than a perfectly polished read.</li>
        <li><strong>Jargon-heavy content:</strong> If you're speaking to potential clients rather than peers, assume zero technical knowledge. Use plain language throughout.</li>
        <li><strong>Generic brand videos with no substance:</strong> "We put clients first" tells viewers nothing they couldn't say about any competitor. Specificity and genuine insight are what differentiate.</li>
      </ul>

      <h2>Getting Started</h2>
      <p>Most Perth professional services firms start with 3–5 educational videos answering their most common prospect questions, a team introduction video, and one client story. This baseline content library can be filmed in a single half-day shoot and represents a long-term asset for the business.</p>
      <p>Our <a href="corporate-video-perth.html">corporate video production service</a> in Perth specialises in professional services content — including coaching on delivery, scripting support, and post-production that makes every principal look their best on camera. <a href="contact.html">Get in touch to discuss your first video project.</a></p>"""
  }
]

for p in POSTS:
    html = page(p)
    path = os.path.join(OUT, f"{p['slug']}.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated: {p['slug']}.html")

print(f"\nDone — {len(POSTS)} files written to {OUT}/")
