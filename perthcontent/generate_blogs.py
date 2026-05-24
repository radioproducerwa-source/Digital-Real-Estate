"""
generate_blogs.py
Generates 30 published blog post HTML files for perthcontent.com
Run: python3 generate_blogs.py
"""

import os


def make_head(slug, title, meta, tag, read_time):
    return f"""<!DOCTYPE html>
<html lang="en-AU">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | Perth Content</title>
  <meta name="description" content="{meta}">
  <link rel="canonical" href="https://perthcontent.com/{slug}.html">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/style.css">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "{title}",
    "description": "{meta}",
    "datePublished": "2025-01-15",
    "author": {{"@type": "Organization", "name": "Perth Content"}},
    "publisher": {{"@type": "Organization", "name": "Perth Content", "url": "https://perthcontent.com"}}
  }}
  </script>
</head>
<body>
<header class="site-header">
  <div class="container header-inner">
    <a href="index.html" class="logo">Perth<span>Content</span></a>
    <nav class="main-nav" id="main-nav">
      <a href="index.html">Home</a>
      <a href="services.html">Services</a>
      <div class="dropdown">
        <button class="dropdown-btn">Industries &#9660;</button>
        <div class="dropdown-menu">
          <a href="corporate-video-production-perth.html">Corporate Video</a>
          <a href="real-estate-video-perth.html">Real Estate Video</a>
          <a href="social-media-video-editing-perth.html">Social Media Video</a>
          <a href="event-highlight-video-perth.html">Event Video</a>
          <a href="explainer-video-perth.html">Explainer Video</a>
          <a href="drone-video-editing-perth.html">Drone Video</a>
          <a href="restaurant-hospitality-video-perth.html">Restaurant Video</a>
          <a href="youtube-video-editing-perth.html">YouTube Editing</a>
          <a href="linkedin-video-content-perth.html">LinkedIn Video</a>
          <a href="wedding-videography-editing-perth.html">Wedding Video</a>
        </div>
      </div>
      <a href="about.html">About</a>
      <a href="blog.html" class="active">Blog</a>
      <a href="contact.html" class="btn btn-primary">Get a Quote</a>
    </nav>
    <div class="header-right">
      <button class="hamburger" id="hamburger" aria-label="Open menu" aria-expanded="false">&#9776;</button>
    </div>
  </div>
</header>
<main>
<div class="container" style="padding-top:2rem;padding-bottom:.5rem;">
  <nav class="breadcrumb"><a href="index.html">Home</a> &rsaquo; <a href="blog.html">Blog</a> &rsaquo; <span>{title}</span></nav>
</div>
<article class="blog-article">
  <div class="container content-narrow">
    <div class="article-meta">
      <span class="blog-tag">{tag}</span>
      <span class="article-read-time">{read_time} min read</span>
    </div>
    <h1 class="article-title">{title}</h1>
"""


def make_foot():
    return """    <div class="article-cta">
      <h3>Need video content for your Perth business?</h3>
      <p>Get a free consultation and quote &mdash; we respond within one business day.</p>
      <a href="contact.html" class="btn btn-primary btn-lg">Get a Free Quote &rarr;</a>
    </div>
  </div>
</article>
</main>
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <div class="footer-logo">Perth<span>Content</span></div>
        <p class="footer-tagline">Professional video content for Perth businesses.</p>
      </div>
      <div>
        <h4>Services</h4>
        <ul>
          <li><a href="services.html">All Services</a></li>
          <li><a href="corporate-video-production-perth.html">Corporate Video</a></li>
          <li><a href="real-estate-video-perth.html">Real Estate Video</a></li>
          <li><a href="social-media-video-editing-perth.html">Social Media Video</a></li>
        </ul>
      </div>
      <div>
        <h4>Company</h4>
        <ul>
          <li><a href="about.html">About</a></li>
          <li><a href="blog.html">Blog</a></li>
          <li><a href="contact.html">Contact</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom"><p>&copy; 2025 Perth Content. All rights reserved.</p></div>
  </div>
</footer>
<script src="js/main.js"></script>
</body>
</html>
"""


ARTICLES = [
    {
        "slug": "blog-corporate-video-cost-perth",
        "title": "How Much Does Corporate Video Production Cost in Perth? (2025 Guide)",
        "tag": "Guides",
        "read_time": 6,
        "meta": "A detailed breakdown of corporate video production costs in Perth for 2025 — from social media edits to full corporate productions, with honest price ranges.",
        "content": """
    <p>One of the most common questions Perth businesses ask before commissioning video work is: <em>what is this actually going to cost?</em> The honest answer is that video production pricing varies enormously depending on what you need. A quick social media Reel edit and a full-day brand shoot are completely different products. This guide breaks down realistic price ranges for every type of corporate video work in Perth for 2025.</p>

    <h2>Perth Corporate Video Pricing by Service Type</h2>

    <p>The following table shows typical price ranges from Perth video professionals in 2025. These are project-based prices covering either editing-only services (where you provide the footage) or full production (filming plus editing).</p>

    <table>
      <thead>
        <tr>
          <th>Service</th>
          <th>Price Range (AUD)</th>
          <th>Notes</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Social media Reel edit (footage provided)</td>
          <td>$150 &ndash; $300</td>
          <td>Edit-only, music, basic colour grade</td>
        </tr>
        <tr>
          <td>Short promo video (1&ndash;2 min)</td>
          <td>$500 &ndash; $1,500</td>
          <td>May include simple filming or edit-only</td>
        </tr>
        <tr>
          <td>Corporate overview video (2&ndash;3 min)</td>
          <td>$1,500 &ndash; $3,500</td>
          <td>Half-day shoot, professional edit</td>
        </tr>
        <tr>
          <td>Full brand story production</td>
          <td>$3,000 &ndash; $8,000</td>
          <td>Full-day shoot, scripting, motion graphics</td>
        </tr>
        <tr>
          <td>Full-day shoot + comprehensive editing</td>
          <td>$5,000 &ndash; $15,000+</td>
          <td>Multi-deliverable, multiple crew, complex post</td>
        </tr>
      </tbody>
    </table>

    <h2>What Drives the Price Up (or Down)</h2>

    <p>Understanding what moves the needle on cost helps you make smarter decisions about where to invest and where to save. The biggest cost variable is whether you need filming or editing only. If you already have quality footage from a previous shoot, an edit-only quote will be significantly lower than a full production quote.</p>

    <p>Crew size has a direct impact on cost. A solo videographer who shoots and edits is the most affordable option. Adding a dedicated camera operator, a lighting technician, or a producer each adds day rate cost. For most Perth small business corporate videos, a solo operator or two-person crew is entirely sufficient.</p>

    <p>Location requirements affect pricing when permits are needed (Perth City Council permits are required for commercial filming in many public spaces), when travel outside metro Perth is required, or when the location demands specific equipment like generators or scaffolding. Keep location simple and you control a significant cost variable.</p>

    <p>Post-production complexity is where many quotes surprise clients. A clean talking-head interview edit is straightforward. Complex motion graphics, 3D text animation, advanced colour grading, VFX compositing, or extensive audio design all add time and cost in post. Music licensing (using a commercial track rather than royalty-free library music) can also add $100&ndash;$500 per track.</p>

    <ul>
      <li><strong>Revision rounds:</strong> most professional quotes include 2 revision rounds; additional rounds are typically charged at an hourly rate ($80&ndash;$150/hr)</li>
      <li><strong>Rush fees:</strong> turnaround under 48 hours typically adds 25&ndash;50% to the quote</li>
      <li><strong>Multiple deliverables:</strong> different aspect ratios (16:9, 9:16, 1:1) or length cuts add editing time</li>
      <li><strong>Script and storyboard services:</strong> if your editor is also scripting, budget an additional $300&ndash;$800</li>
      <li><strong>Transcription and captioning:</strong> often an add-on, typically $50&ndash;$150 per video</li>
    </ul>

    <h2>How to Get Maximum Value From Your Video Budget</h2>

    <p>The single best thing you can do to reduce cost is to arrive with a clear brief. Editors and videographers who know exactly what they are producing spend less time clarifying and less time revising. A one-page brief covering objective, audience, tone, references and technical specs can save you hundreds of dollars in back-and-forth.</p>

    <p>If you are providing footage, organise it. An editor who receives a clearly labelled folder with selects and B-roll separated will finish faster than one who receives a hard drive of raw, unsorted clips spanning multiple shoots. Sorting your footage before sending it can meaningfully reduce the editing quote.</p>

    <p>Bundling multiple deliverables from a single shoot is one of the smartest moves available to Perth businesses. If you are paying for a half-day corporate shoot, brief your videographer to capture enough material for a 90-second brand video, three 30-second social cuts, and a 60-second testimonial in the same session. The incremental editing cost of additional deliverables is far lower than the cost of additional shoot days.</p>

    <p>When getting quotes, ask for a project-based price rather than an hourly rate where possible. Project rates give you cost certainty. If you are comparing multiple quotes, make sure you are comparing like for like &mdash; a $500 quote and a $2,000 quote for the &ldquo;same video&rdquo; almost certainly include very different scopes of work. Ask each editor exactly what is and is not included before making a decision purely on price.</p>
""",
    },
    {
        "slug": "blog-why-perth-business-needs-video",
        "title": "Why Your Perth Business Needs Video Content in 2025",
        "tag": "Strategy",
        "read_time": 5,
        "meta": "Perth businesses that haven't embraced video are falling behind. Here's why video content is no longer optional for businesses competing in 2025.",
        "content": """
    <p>Video has moved from a marketing nice-to-have to a baseline expectation in 2025. Consumers in Australia now spend an average of six hours per day consuming online video, and that number climbs year on year. For Perth businesses, the window to gain a competitive advantage from early adoption is narrowing &mdash; but it has not closed. Here is why video content deserves a serious place in your marketing budget this year.</p>

    <h2>Perth Is a Mobile-First City</h2>

    <p>Perth's geography and lifestyle play directly into video consumption patterns. Commuters on the Mandurah and Joondalup lines, people at Cottesloe beach, and workers on extended FIFO rosters consume content almost entirely on smartphones. Perth has one of the highest smartphone penetration rates in Australia, and mobile video consumption dominates. Short-form content &mdash; Reels, TikToks, YouTube Shorts &mdash; performs particularly well because it fits the on-the-go consumption behaviour of Perth audiences.</p>

    <p>This matters for your business because if your competitors are running polished video on Instagram and you are posting static images, the algorithm is actively favouring their content over yours. Instagram, TikTok, Facebook, and LinkedIn all explicitly prioritise video in their feed ranking. This is not a subtle difference &mdash; video posts routinely receive three to five times the organic reach of equivalent static posts.</p>

    <h2>Video Converts Better Than Any Other Format</h2>

    <p>Landing pages with an explainer video convert at rates 80% higher than pages without one, according to multiple marketing studies. When a potential client can watch a 90-second overview of your service before they call, they arrive as a warmer lead. They have already self-selected as interested, they understand your offering, and the sales conversation starts from a higher baseline of trust.</p>

    <p>Video also improves SEO performance in ways that are meaningful for Perth businesses. Google frequently returns video results for local service searches. Searches like &ldquo;video production Perth&rdquo; or &ldquo;real estate agent Subiaco&rdquo; increasingly surface YouTube videos in the results page. A well-optimised YouTube video gives you a second point of presence in Google search results &mdash; something no amount of blog writing achieves on its own.</p>

    <ul>
      <li>Video content gets 1,200% more shares on social media than text and image content combined</li>
      <li>LinkedIn video receives 3x more engagement than text posts from the same account</li>
      <li>Emails with &ldquo;video&rdquo; in the subject line have 19% higher open rates</li>
      <li>Websites with video have 2x lower bounce rates than text-only pages</li>
      <li>Businesses using video grow revenue 49% faster than those that don't, according to Aberdeen Group research</li>
    </ul>

    <h2>Perth-Specific Opportunity</h2>

    <p>In industries like Perth real estate, hospitality, and trade services, video adoption is still uneven. Many businesses in these sectors are still running campaigns built entirely on static images and written copy. This means there is a genuine first-mover advantage available in many Perth market segments right now. A Subiaco restaurant with consistent, high-quality Instagram video will stand out on a feed full of static food photography. A Perth tradesperson with a YouTube channel answering common client questions will dominate local search results for their trades category over competitors with no video presence.</p>

    <p>The cost of video production has also dropped significantly. What required a production crew and $10,000 in 2015 can now be achieved with a skilled solo videographer and $2,000&ndash;$4,000. The barrier is lower than it has ever been, and the return &mdash; through better reach, higher conversion and stronger brand authority &mdash; has never been higher. Waiting is no longer a neutral position; while you delay, your competitors are building video libraries that compound in value with every passing month.</p>
""",
    },
    {
        "slug": "blog-real-estate-video-vs-photos-perth",
        "title": "Real Estate Video vs Photos &mdash; Which Sells Property Faster in Perth?",
        "tag": "Real Estate",
        "read_time": 5,
        "meta": "Perth real estate agents are increasingly using video alongside photography. Here's the honest comparison of video vs photos in Perth's competitive property market.",
        "content": """
    <p>Perth's property market has been among the strongest in Australia in recent years, but strong demand does not mean agents can afford to be complacent with their marketing. In a market where buyers are scrolling through dozens of listings on REIWA.com.au and Domain, the properties that convert interest into inspections are the ones that tell a compelling visual story. So does video actually outperform photography, or is it an expensive add-on? The answer depends on the property &mdash; but for many listings, video is not optional.</p>

    <h2>What Video Shows That Photos Cannot</h2>

    <p>Great real estate photography captures individual rooms at their best. What it cannot convey is the <em>flow</em> of a property &mdash; how the hallway connects to the living space, how natural light moves through the home over the course of a morning, or how the outdoor entertaining area feels when you are standing in it. Video captures spatial relationships and movement in a way that a static image, no matter how well shot, simply cannot replicate.</p>

    <p>Video also conveys neighbourhood context far better than photography. A walk-through that starts from the street, shows the nearby park, and captures the sound of the suburb communicates lifestyle in a way that resonates emotionally with buyers. Perth buyers are often making purchasing decisions partly based on suburb feel &mdash; proximity to the coast, school zones, the character of the street. Video communicates all of this; photography communicates the house.</p>

    <p>Research from real estate marketing platforms consistently shows that listings with video receive more enquiries and generate longer time-on-page than photo-only listings. When a buyer spends four minutes watching a property walkthrough rather than ten seconds clicking through photos, they are already more invested before they contact the agent.</p>

    <h2>Cost Comparison and When Video Makes Sense</h2>

    <p>Professional real estate photography in Perth typically runs $300&ndash;$600 for a standard residential property. Adding a professional video walkthrough adds approximately $500&ndash;$1,200 to that cost, depending on property size, editing complexity, and whether drone footage is included. For most properties, that is a meaningful but justifiable investment when you consider the potential impact on days-on-market and final sale price.</p>

    <ul>
      <li><strong>Premium properties ($800k+):</strong> video is effectively non-negotiable; buyers at this price point expect it</li>
      <li><strong>Architecturally distinctive homes:</strong> video showcases design intent that photos flatten</li>
      <li><strong>Properties in slower-moving suburbs:</strong> video gives a listing a marketing edge in markets with longer days-on-market</li>
      <li><strong>Acreage or large lots:</strong> drone footage is the only way to properly convey the scale of the land</li>
      <li><strong>Investment properties:</strong> out-of-state or overseas buyers rely more heavily on video when they cannot inspect in person</li>
    </ul>

    <p>Drone footage adds an additional $350&ndash;$700 to a real estate video package but provides something photographs and ground-level video simply cannot: aerial context. For a property in Applecross, drone establishes the Swan River proximity. For a Fremantle terrace, it shows the neighbourhood streetscape and proximity to the port. For a Hills acreage in Kalamunda or Mundaring, it reveals the scope of the land and tree coverage in a single cinematic shot.</p>

    <h2>The Practical Recommendation</h2>

    <p>Video does not replace professional photography for Perth real estate &mdash; it works alongside it. The property portal images that buyers see first in their REIWA search results are still photographs; video is not used as the primary listing image. The strategy that works is using professional photography for portal thumbnails and listing images (because that is what buyers see in search), and video for social media sharing, the property website or microsite, and email marketing to the agent's buyer database.</p>

    <p>A well-produced property video shared on the listing agent's Instagram or Facebook can reach buyers who were not actively searching the portals. It can generate enquiries from passive buyers &mdash; people who were not looking but respond to a compelling property video in their feed. That social media reach is where video provides return that photography simply cannot match.</p>
""",
    },
    {
        "slug": "blog-how-to-brief-video-editor",
        "title": "How to Brief a Video Editor for Your Business",
        "tag": "Guides",
        "read_time": 4,
        "meta": "A good video brief saves time, money and multiple revision rounds. Here's exactly what to include when briefing a video editor for your Perth business.",
        "content": """
    <p>The most common reason video projects run over budget and over time is not technical skill &mdash; it is an unclear brief. When a video editor does not know exactly what you need, they make assumptions. Some of those assumptions will be wrong. You will ask for changes. They will revise. You will ask for more changes. Before long, you have burned through your included revision rounds and the working relationship is strained. A one-page written brief, provided before work starts, prevents almost all of this.</p>

    <h2>The Eight Elements of a Strong Video Brief</h2>

    <p><strong>1. Objective.</strong> What should a viewer do immediately after watching this video? The answer should be a single, specific action: visit the website, call the number on screen, book an appointment, or follow the account. If you cannot answer this question in one sentence, you are not ready to brief an editor.</p>

    <p><strong>2. Target audience.</strong> Describe your viewer: their age range, their role (consumer vs business decision-maker), where they will watch the video (Instagram feed, website homepage, in-person presentation), and what they already know about your business. A video targeting 55-year-old property investors watches differently to one targeting 28-year-old first home buyers.</p>

    <p><strong>3. Key message.</strong> Write one sentence that captures the single most important thing the video must communicate. Everything else in the video exists to support this sentence.</p>

    <p><strong>4. Tone.</strong> Describe the emotional register: corporate and professional, warm and approachable, high-energy and exciting, calm and trustworthy. Include adjectives that feel right and, importantly, adjectives that definitely feel wrong. &ldquo;Professional but not stiff; confident but not arrogant&rdquo; is a useful tone description. &ldquo;Good vibes&rdquo; is not.</p>

    <p><strong>5. Reference videos.</strong> This is the single most useful thing you can provide. Find two or three YouTube or Vimeo links to videos whose style you like &mdash; these do not need to be from your industry. Note which specific elements you like: the pacing, the music style, the colour grade, the text animation style, or the interview format.</p>

    <ul>
      <li><strong>6. Technical specifications:</strong> platform (Instagram Reels, YouTube, website), aspect ratio (9:16, 16:9, 1:1), target length, and file format required on delivery</li>
      <li><strong>7. Timeline:</strong> your deadline, the date you will provide feedback on the first cut, and how many revision rounds you expect</li>
      <li><strong>8. Footage details:</strong> what raw footage you are providing, how it is labelled, any selects you have already identified, and any gaps you know about</li>
    </ul>

    <h2>Common Mistakes That Cause Revision Cycles</h2>

    <p>Vague tone descriptions like &ldquo;make it pop&rdquo; or &ldquo;professional&rdquo; are interpreted differently by every editor. Without reference videos, editors default to their own aesthetic preferences, which may not match yours. Not specifying the platform means the editor may deliver a 16:9 file for a project you needed in 9:16 for Instagram. Changing the key message after editing has started &mdash; for example, deciding midway through the project that you want to focus on a different service &mdash; can require a near-complete rebuild.</p>

    <p>When you receive the first cut, watch it twice before sending feedback. Watch it once all the way through for overall feel, without pausing. Then watch it a second time and note specific timestamps for specific feedback. Feedback like &ldquo;at 0:23 the music feels too loud relative to the voiceover&rdquo; is actionable in minutes. Feedback like &ldquo;the whole vibe is off&rdquo; requires a follow-up conversation before any work can happen.</p>
""",
    },
    {
        "slug": "blog-short-form-vs-long-form-video-perth",
        "title": "Short-Form vs Long-Form Video &mdash; What Works for Perth Businesses?",
        "tag": "Strategy",
        "read_time": 5,
        "meta": "Should your Perth business focus on short Reels and TikToks, or invest in longer YouTube content? Here's the honest breakdown for different business types.",
        "content": """
    <p>The short-form vs long-form debate comes up in almost every video strategy conversation, and the answer is not one-size-fits-all. Both formats serve genuinely different purposes, and the right mix depends on your business type, your marketing goals, and the resources you have available to produce and manage content consistently. Here is a practical breakdown to help you decide where to start.</p>

    <h2>Defining the Formats</h2>

    <p>Short-form video is typically under 60 seconds: Instagram Reels, TikTok, YouTube Shorts, and Facebook Stories all fall into this category. The format is designed for rapid consumption, algorithm-driven discovery, and entertainment. People encounter short-form content while scrolling; they did not actively search for it. This means your first three seconds need to earn attention from a stranger with no prior relationship to your brand.</p>

    <p>Long-form video spans anything from two minutes to 20 or more: YouTube videos, website brand films, LinkedIn native video essays, webinar recordings, and product walkthroughs. Long-form is generally consumed by people in an active research or consideration mindset. They found your video by searching, or they chose to click through from a short-form piece that earned their trust. Long-form converts deeper engagement into real business outcomes.</p>

    <h2>Platform Breakdown for Perth Businesses</h2>

    <p>Instagram and TikTok are discovery platforms &mdash; they are excellent for reaching people who do not yet know your business exists. A hospitality venue, a personal trainer, a boutique retailer, or a real estate agent can all build significant organic reach on these platforms through consistent, high-quality short-form video. The trade-off is that brand awareness does not always translate directly into leads, especially in B2B contexts.</p>

    <p>YouTube and your website are conversion platforms. A potential client who watches a five-minute case study video on your website has self-selected as highly interested. A plumber with a YouTube channel of &ldquo;common Perth plumbing problems&rdquo; tutorials builds trust and SEO authority simultaneously. This is where long-form genuinely earns its cost.</p>

    <ul>
      <li><strong>Short-form wins for:</strong> hospitality, fitness, retail, beauty, real estate, brand awareness campaigns, social media growth</li>
      <li><strong>Long-form wins for:</strong> B2B services, professional services, technical products, complex offerings requiring explanation, SEO-focused content strategies</li>
      <li><strong>Both formats together:</strong> e-commerce, coaching and education, agencies, trades businesses with both awareness and SEO goals</li>
    </ul>

    <h2>The Hybrid Approach That Works for Most Businesses</h2>

    <p>The most cost-efficient strategy is the one that treats long-form content as the source material for short-form. Film a five-minute brand story or case study video, then extract three or four 30-second clips from it for Reels and TikTok. Film a 10-minute YouTube tutorial, then cut the key insight into a 45-second short. One shoot generates content for multiple formats and channels, which dramatically improves your return on production cost.</p>

    <p>For Perth SMBs starting from scratch, the practical recommendation is to begin with short-form. The barrier to production is lower (your phone plus a lapel mic is sufficient for early content), the feedback loop is faster (you see engagement data within 24 hours), and the skills you develop &mdash; hooking attention quickly, clear messaging, consistent posting habits &mdash; transfer directly to long-form production when you are ready to invest in it. Most Perth businesses should run short-form consistently for three to six months before adding a long-form YouTube strategy on top.</p>

    <p>Budget comparison: a single professionally edited Reel costs $150&ndash;$300. A professionally produced YouTube video of three to five minutes costs $500&ndash;$1,500. The Reel reaches more people faster; the YouTube video pays dividends longer. The businesses winning with video in Perth are doing both &mdash; just not necessarily simultaneously from day one.</p>
""",
    },
    {
        "slug": "blog-repurpose-one-video-ten-content",
        "title": "How to Repurpose One Video Into 10 Pieces of Content",
        "tag": "Strategy",
        "read_time": 4,
        "meta": "Smart Perth businesses film once and publish across every channel. Here's how to turn a single video shoot into 10 or more pieces of content.",
        "content": """
    <p>The biggest waste in video marketing is not producing bad content &mdash; it is producing good content and then publishing it once. A professionally produced brand video that lives on your website and nowhere else represents a fraction of its potential value being extracted. The most efficient approach is to plan every shoot as a content multiplication exercise from the start: one shoot, one edit, ten publishable assets. Here is how to make that work in practice.</p>

    <h2>Start With a Hero Piece</h2>

    <p>A &ldquo;hero piece&rdquo; is your primary deliverable from a shoot: a brand story video, a team culture overview, a client case study, or a product overview. This is the polished, complete video that earns the most production effort. It might run two to four minutes. From this single piece of source material, everything else flows.</p>

    <p>The critical mindset shift is to brief your videographer and editor <em>before</em> the shoot with the full repurpose plan in mind. If you know you will need a 15-second TikTok hook, tell your videographer to capture a punchy standalone moment at the start of the shoot. If you want a testimonial clip, make sure your interview subject gives at least one short, quotable answer that stands alone without context. The repurpose plan should shape what you film, not just what you edit.</p>

    <h2>The 10 Assets From One 3-Minute Corporate Video</h2>

    <p>Here is a practical example of what a single three-minute corporate overview video can produce:</p>

    <ul>
      <li><strong>1. 60-second hero cut</strong> &mdash; condensed version for LinkedIn feed and website homepage above the fold</li>
      <li><strong>2. 30-second Instagram promo</strong> &mdash; cropped to 9:16, fast-paced edit with music, used as a Reel and for paid ads</li>
      <li><strong>3. 15-second TikTok hook</strong> &mdash; the single most compelling moment or hook line from the video, standalone format</li>
      <li><strong>4&ndash;6. Three 30-second testimonial clips</strong> &mdash; if interviews were conducted, each usable quote becomes a standalone trust piece</li>
      <li><strong>7. Audiogram</strong> &mdash; a key quote or insight with static branded background, waveform animation, used on LinkedIn and Twitter/X</li>
      <li><strong>8. Still frames for social posts</strong> &mdash; export high-resolution stills from cinematic B-roll moments for Instagram grid and LinkedIn image posts</li>
      <li><strong>9. Key quote graphic</strong> &mdash; pull the strongest line from the video, design a branded quote card for social and email</li>
      <li><strong>10. Blog post from the script</strong> &mdash; the video script, lightly edited for reading, becomes a 500&ndash;800 word article that earns SEO value over time</li>
    </ul>

    <p>Two bonus assets: the script reformatted as an email newsletter introduction, and an embedded video slide for presentations and pitch decks. A three-minute corporate video can realistically generate 12 publishable pieces of content.</p>

    <h2>The Production Brief That Makes Repurposing Work</h2>

    <p>Brief your videographer and editor on the repurpose plan before shooting. Tell them which moments need to be standalone (so they ensure clean audio and framing for those sections independently), which parts need to be cropped to 9:16 (so they frame subjects centrally in the horizontal shot), and which quotes you want captured in multiple takes for reliability. A shoot briefed for repurposing generates better raw material than one briefed only for the hero piece.</p>

    <p>Perth businesses that adopt this approach consistently find that their cost-per-content-piece drops dramatically. Instead of paying $500&ndash;$1,500 per piece of edited content, the incremental cost of each additional format cut from existing footage falls to $50&ndash;$150 per asset. That is the mathematics that makes professional video production genuinely affordable at scale.</p>
""",
    },
    {
        "slug": "blog-best-video-lengths-platforms",
        "title": "Best Video Lengths for Instagram, LinkedIn, YouTube and TikTok in 2025",
        "tag": "Strategy",
        "read_time": 4,
        "meta": "Optimal video lengths for each social platform in 2025. A practical guide for Perth businesses creating video content.",
        "content": """
    <p>One of the most practical questions in video marketing is also one of the most specific: how long should this video actually be? Every platform has its own algorithm preferences, audience expectations, and technical constraints. Getting the length right is not about following rules for the sake of it &mdash; it is about maximising the chance that your video is watched, rewarded by the algorithm, and remembered. Here is the current state of play for each major platform in 2025.</p>

    <h2>Platform-by-Platform Length Guide</h2>

    <p><strong>Instagram Reels:</strong> The sweet spot for organic reach is 7&ndash;15 seconds. Counterintuitive as it sounds, shorter Reels have higher completion rates, and completion rate is the primary metric Instagram uses to determine whether a video gets pushed to new audiences. For educational or storytelling content where you genuinely need more time, up to 90 seconds is viable &mdash; but every second beyond 15 needs to earn its place by keeping the viewer actively engaged.</p>

    <p><strong>TikTok:</strong> Research from TikTok's own data team has identified 21&ndash;34 seconds as the completion-rate sweet spot for most content categories. Videos in this range have the highest rate of full views, which the algorithm rewards heavily. TikTok now supports videos up to 10 minutes, and storytelling content can work well at 2&ndash;3 minutes for engaged audiences &mdash; but discovery content (content designed to reach people who don't follow you) performs best under 45 seconds.</p>

    <p><strong>LinkedIn:</strong> LinkedIn video rewards slightly longer content than Instagram because the platform's audience is in a professional browsing mindset rather than entertainment-scrolling mode. For most business posts, 30&ndash;90 seconds performs best. LinkedIn native video can run up to 10 minutes, and thought leadership pieces or presentations can justify 3&ndash;5 minutes &mdash; but only if the content density is high throughout.</p>

    <p><strong>YouTube:</strong> YouTube rewards watch time in absolute minutes, not percentage completion. The optimal length for search-optimised content is 8&ndash;15 minutes, because longer videos allow for more natural keyword coverage in speech and generate more absolute watch time. For brand-focused content not targeting SEO, 2&ndash;5 minutes is more appropriate. YouTube Shorts (under 60 seconds) operate on different algorithm logic, closer to TikTok.</p>

    <ul>
      <li><strong>Facebook feed video:</strong> 1&ndash;3 minutes for organic content; 15&ndash;30 seconds for paid advertising formats</li>
      <li><strong>Website hero video:</strong> 60&ndash;90 seconds with muted autoplay works well; longer than 2 minutes and most visitors won't watch to the end</li>
      <li><strong>Email marketing video:</strong> link to a video rather than embed; 60&ndash;120 seconds is the appropriate destination length</li>
      <li><strong>LinkedIn video ads:</strong> 15&ndash;30 seconds for best completion rates in paid placements</li>
    </ul>

    <h2>The Rule That Overrides All Platform Guidance</h2>

    <p>Every platform guideline is a starting point, not a ceiling. The real rule is simpler: your video should be exactly as long as it needs to be to deliver its message, and not one second longer. Every frame that doesn't advance the story, deliver value, or maintain attention is a frame that costs you completion rate and viewer trust.</p>

    <p>Watch your video analytics regularly. YouTube, Instagram, and TikTok all show you exactly where in your video people stop watching. If your four-minute video loses 60% of viewers at the 90-second mark, the question to ask is not &ldquo;how do I keep people watching at the 90-second mark?&rdquo; &mdash; it is &ldquo;what would this video look like if it was 90 seconds long?&rdquo; Your analytics are the most honest briefing document you have for your next edit.</p>
""",
    },
    {
        "slug": "blog-how-to-plan-corporate-video-shoot-perth",
        "title": "How to Plan a Corporate Video Shoot in Perth",
        "tag": "Production",
        "read_time": 5,
        "meta": "Planning your first corporate video shoot in Perth? Here's a comprehensive checklist covering pre-production, shoot day, and what to have ready.",
        "content": """
    <p>A corporate video shoot that runs smoothly is almost always one that was planned thoroughly. Conversely, most shoot-day problems &mdash; unexpected delays, subpar interview footage, missing B-roll, lighting issues &mdash; can be traced back to gaps in pre-production. Whether you are organising a shoot yourself or working alongside a videographer, this guide covers what needs to happen before, during, and after your shoot day.</p>

    <h2>Pre-Production: The Week Before</h2>

    <p>Finalise your script or shot list at least one week before the shoot date, not the day before. Last-minute script changes cascade into location changes, talent preparation issues, and shooting schedule overruns. If you are conducting on-camera interviews, send your subjects the questions in advance so they have time to think &mdash; not to rehearse scripted answers, but to arrive with clear thoughts and genuine examples ready.</p>

    <p>Confirm your locations and access well in advance. If you are filming in a Perth CBD office building, confirm that building management permits commercial filming. If you plan to use public spaces like Elizabeth Quay, Kings Park, or the Perth Cultural Centre as establishing shot locations, check whether a City of Perth filming permit is required for your scope of work. Many productions use these locations for quick B-roll shots without issues, but larger productions or those involving tripods and multiple crew members may require permits.</p>

    <p>Perth-specific location tips: avoid scheduling outdoor interviews between 11am and 3pm in summer (October through March). The midday sun creates harsh shadows under eyes and across faces that are difficult to correct in post-production. Golden hour &mdash; the hour after sunrise and the hour before sunset &mdash; produces cinematic light with warm tones and long, flattering shadows. For interviews, overcast days actually provide the most even, flattering outdoor light.</p>

    <ul>
      <li>Brief all on-camera subjects on what to wear: solid colours film best; avoid fine stripes, busy patterns, and pure white (overexposes easily)</li>
      <li>Confirm parking and logistics for the crew &mdash; Perth CBD parking can add 30+ minutes of setup delay if not pre-arranged</li>
      <li>Prepare a shot list with estimated time at each location so everyone knows the schedule</li>
      <li>Check that all equipment is charged, batteries are spare, and memory cards are formatted and empty</li>
      <li>Identify a backup location in case of weather or access issues</li>
    </ul>

    <h2>On Shoot Day</h2>

    <p>Brief everyone on their role at the start of the day, even if they have been on camera before. Let interview subjects know roughly how long each take runs, that you will likely do two or three takes of each question, and that it is fine to pause and restart a sentence at any point. Subjects who understand this are measurably more relaxed and deliver better footage. Have water available &mdash; long shoot days with on-camera speaking drain energy quickly, and a dry throat affects voice quality noticeably.</p>

    <p>Capture more B-roll than you think you need. B-roll &mdash; the supplementary footage of your workplace, team, products, and processes that plays over interview audio &mdash; is what makes the difference between an interview video and a polished corporate production. Most editors will tell you they wish they had more B-roll to work with. Budget time for B-roll capture at every location.</p>

    <h2>After the Shoot</h2>

    <p>Transfer and back up all footage immediately after the shoot, before doing anything else. Hard drive failure is rare but not unheard of, and losing a day of footage is a costly disaster that a simple backup prevents entirely. Provide your editor with a clearly organised folder structure, your brief recap, and any selects you identified during the shoot. Aim to review the first cut within 48 hours of receiving it &mdash; momentum matters for the editing process, and prompt feedback keeps the project on schedule.</p>
""",
    },
    {
        "slug": "blog-diy-vs-professional-video-editing",
        "title": "DIY vs Professional Video Editing &mdash; The Honest Comparison for Perth Businesses",
        "tag": "Guides",
        "read_time": 5,
        "meta": "Should your Perth business edit its own videos or hire a professional? An honest, balanced comparison of DIY and professional video editing.",
        "content": """
    <p>The case for DIY video editing has genuinely improved in recent years. Free and low-cost tools have become powerful, smartphones shoot in 4K, and platforms like TikTok have trained audiences to accept and even prefer raw, authentic-looking content over polished production. But the case for professional editing has not weakened &mdash; if anything, the bar for what looks &ldquo;good enough&rdquo; on professional channels and customer-facing content has risen. Here is how to think through the choice honestly.</p>

    <h2>What DIY Tools Are Actually Available</h2>

    <p><strong>CapCut</strong> (free, mobile and desktop) is the most capable free editing tool available right now, and it is purpose-built for short-form social content. Auto-captions, trending music integration, aspect ratio conversion, and a library of transitions make it genuinely useful for Instagram and TikTok content. Its limitations are at the quality ceiling: colour grading tools are basic, audio mixing is limited, and it does not handle complex multi-track timelines well.</p>

    <p><strong>DaVinci Resolve</strong> (free version) is a professional-grade editor that the film and television industry uses for colour grading. The free version is extraordinarily capable &mdash; more so than most paid subscription tools. The trade-off is a steep learning curve. A beginner spending their first week in DaVinci Resolve will spend most of that week on YouTube tutorials, not on editing their business content.</p>

    <p><strong>Adobe Premiere Pro</strong> (subscription, approx. $60/month) is the industry standard for a reason: it integrates seamlessly with After Effects, Audition, and the rest of the Adobe ecosystem. For businesses already in the Adobe suite, it is the natural choice. For those without existing subscriptions, the monthly cost adds up against a limited use case.</p>

    <h2>When to DIY and When to Hire a Professional</h2>

    <p>The honest framework is based on stakes, not skill level. Low-stakes content &mdash; Instagram Stories, behind-the-scenes clips, quick product updates, team culture content &mdash; is genuinely well-served by DIY production. Audiences have calibrated expectations for this type of content, and authentic imperfection is often an asset rather than a liability.</p>

    <ul>
      <li><strong>DIY is appropriate for:</strong> Stories and behind-scenes content, employee updates, quick social announcements, low-stakes experiments</li>
      <li><strong>Professional is appropriate for:</strong> homepage hero video, testimonials, paid advertising, brand story films, anything representing your business formally</li>
      <li><strong>The time cost:</strong> a beginner editor will spend 4&ndash;6 hours producing a 2-minute edit that a professional completes in 1.5&ndash;2 hours; at a professional hourly rate of $100+, paying for the edit is economically rational</li>
    </ul>

    <h2>The Hybrid Model That Most Perth Businesses Settle On</h2>

    <p>The approach that makes financial and strategic sense for most Perth SMBs is a hybrid: hire a professional for hero content (quarterly brand video, testimonials, service explainers), and handle day-to-day social content in-house using CapCut or similar tools.</p>

    <p>The professional's role is not just to produce better-looking content &mdash; it is also to set up a system. Ask your editor to create a branded CapCut or Premiere template for your social content: correct colours, fonts, lower-thirds, intro and outro elements. Your team then uses this template for day-to-day content, maintaining brand consistency without needing professional production for every post. This approach combines the quality ceiling of professional production with the volume and speed of DIY &mdash; and it is what video-mature Perth businesses are already doing.</p>
""",
    },
    {
        "slug": "blog-what-makes-great-explainer-video",
        "title": "What Makes a Great Explainer Video for a Perth Business?",
        "tag": "Production",
        "read_time": 4,
        "meta": "The key elements that separate effective explainer videos from forgettable ones — a guide for Perth businesses.",
        "content": """
    <p>An explainer video is any video that explains a product, service, or process &mdash; and almost every Perth business has a use for one. The challenge is that most explainer videos fail not because of poor production quality, but because of poor structure. They try to say too much, they open with company history instead of the viewer's problem, or they end with a vague call to action that leads nowhere. The framework below is what separates the explainer videos that convert from the ones that get politely ignored.</p>

    <h2>The AIDA Framework for Explainer Video</h2>

    <p><strong>Attention (0&ndash;5 seconds):</strong> Your opening line must hook the problem, not introduce the company. &ldquo;If your Perth business isn't getting enquiries from your website, this might be why&rdquo; is a strong opening. &ldquo;Hi, we're [Company Name] and we've been helping Perth businesses since 2010&rdquo; is a weak opening. The viewer's only question in the first five seconds is: &ldquo;Is this relevant to me?&rdquo; Answer yes before they can leave.</p>

    <p><strong>Interest (5&ndash;25 seconds):</strong> Having hooked the problem, describe it in enough detail that viewers who recognise it lean in. Name the specific pain: the wasted ad spend, the slow turnaround time, the difficulty explaining a complex service to new customers. Viewers who see their own situation described accurately will keep watching to find out if you have a solution.</p>

    <p><strong>Desire (25&ndash;75 seconds):</strong> Introduce your solution and describe its benefits in terms of outcomes, not features. &ldquo;We produce a 90-second brand video that you can use across your website, social media, and email campaigns&rdquo; describes a feature. &ldquo;Our clients typically see a 30% increase in website enquiries within 60 days of publishing their brand video&rdquo; describes a desire. Benefits beat features in every persuasion context.</p>

    <p><strong>Action (final 10&ndash;15 seconds):</strong> State a single, specific, low-friction next step. &ldquo;Click below to get a free quote&rdquo; is better than &ldquo;Contact us to learn more.&rdquo; One CTA, not three. Clarity converts; hedging does not.</p>

    <h2>Length, Style and What Fails</h2>

    <p>Sixty to ninety seconds is the optimal length for most business explainer videos. At 150 words per minute (a comfortable on-screen voiceover pace), 90 seconds gives you 225 words &mdash; more than enough to deliver the full AIDA arc with clarity. Explainers that run longer than 2 minutes almost always contain information that the viewer does not need at the awareness stage of their journey. That information belongs in a separate, deeper piece of content.</p>

    <ul>
      <li><strong>Live action</strong> builds trust through human presence and is best for service businesses where personal connection matters</li>
      <li><strong>Animation</strong> excels for abstract concepts, technical products, and processes that cannot be filmed (software workflows, financial products, B2B SaaS)</li>
      <li><strong>Hybrid</strong> uses live footage as the story vehicle with animated data or process graphics overlaid</li>
    </ul>

    <p>What fails most often in explainer videos: starting with company history or credentials instead of the viewer's problem; trying to explain every feature rather than the core benefit; using technical jargon that the target viewer does not use themselves; and ending with a weak or missing call to action. A 60-second explainer with a sharp hook and a clear CTA will consistently outperform a three-minute production values showcase that never earns the viewer's trust.</p>
""",
    },
    {
        "slug": "blog-how-to-write-video-script",
        "title": "How to Write a Video Script for Your Business",
        "tag": "Production",
        "read_time": 5,
        "meta": "Writing a video script for your Perth business doesn't need to be complicated. A practical, step-by-step guide to scripting effective business video.",
        "content": """
    <p>The script is the most undervalued step in video production. Businesses that invest time in a proper script before the camera is turned on produce better videos faster, spend less on reshoots, and give their editors a clear framework to work within. The good news is that writing a business video script does not require formal screenwriting skills. It requires clarity about your message and a willingness to write for the ear, not the page.</p>

    <h2>Script Formats and When to Use Each</h2>

    <p>A <strong>word-for-word script</strong> is best when the presenter will be reading from a teleprompter, when precise language matters (legal, medical, financial services), or when the video requires a voiceover that must sync perfectly with visuals. Write it exactly as it will be spoken, including contractions. &ldquo;We are&rdquo; becomes &ldquo;We're&rdquo;; &ldquo;It is&rdquo; becomes &ldquo;It's&rdquo;. Reading-style formality sounds stiff on camera.</p>

    <p>A <strong>bullet-point outline</strong> works better when you want natural delivery and conversational energy. The presenter knows the key points they need to cover and speaks to each one naturally, without memorising exact lines. This produces more authentic footage at the cost of precision control over timing and exact wording. It is the approach most talking-head social content uses successfully.</p>

    <p>A <strong>shot list script</strong> is used for B-roll-heavy or montage-style videos where there is no continuous on-camera presenter. It maps visual shots to voiceover lines or on-screen text, ensuring the editor knows what visuals correspond to what content.</p>

    <h2>The Three-Act Structure for Business Video</h2>

    <p>Every effective business video &mdash; regardless of length or format &mdash; follows a version of the three-act structure:</p>

    <ul>
      <li><strong>Act 1 (15&ndash;20% of runtime):</strong> Hook and problem. Open with the viewer's pain point or a bold, attention-grabbing statement. Establish why this video is relevant to this viewer right now.</li>
      <li><strong>Act 2 (60&ndash;70% of runtime):</strong> Solution and benefits. Present your offering in terms of the outcomes it delivers. Use concrete examples, numbers where available, and a human story where possible.</li>
      <li><strong>Act 3 (10&ndash;20% of runtime):</strong> CTA and next step. State one clear action, with minimal friction. Tell the viewer exactly what to do and why to do it now.</li>
    </ul>

    <h2>Writing Tips for On-Camera Scripts</h2>

    <p>Write for the ear, not the eye. Sentences that read well on a page are often too long for on-camera delivery. Read your script aloud as you write it &mdash; if you run out of breath before the sentence ends, break it in two. Avoid jargon and industry acronyms unless your target audience uses them fluently. Never start with &ldquo;Hi, I'm [Name] from [Company]&rdquo; &mdash; lead with the viewer's problem instead. Your name and company can be introduced after you have earned the viewer's attention.</p>

    <p>If using a teleprompter, mark emphasis words in bold so the presenter knows where to land stress. Use double-spacing to improve readability at scroll speed. Rehearse the script once before shooting &mdash; not to memorise it, but to identify phrases that sound natural when written but awkward when spoken. Rewrite those phrases until they feel like natural speech. A script that a presenter can deliver smoothly without it sounding scripted is the goal.</p>
""",
    },
    {
        "slug": "blog-top-video-styles-perth-small-business",
        "title": "Top 5 Video Styles for Perth Small Businesses",
        "tag": "Strategy",
        "read_time": 4,
        "meta": "Not sure which type of video to make for your Perth small business? The 5 most effective video styles and when to use each.",
        "content": """
    <p>When Perth small business owners decide to invest in video, the first question is usually: what kind of video should I actually make? The options are genuinely broad &mdash; from polished brand films to raw behind-the-scenes phone footage &mdash; and the right answer depends on your budget, your brand personality, and where you are in your video journey. Here are the five most effective video styles for Perth SMBs and how to decide which is right for you.</p>

    <h2>1. Talking Head / Founder Story</h2>

    <p>A founder or team member speaking directly to camera is the most accessible and often the most powerful format for small business video. It requires minimal equipment, can be shot in your workspace, and creates immediate personal connection. Audiences respond to faces and human voices in ways they simply don't respond to text or static images. For service businesses &mdash; consultants, coaches, trades, healthcare practitioners, financial advisers &mdash; a confident, authentic talking-head video builds trust faster than almost any other format.</p>

    <h2>2. Product or Service Demo</h2>

    <p>A demo video shows exactly what you do in practice. For product businesses, it shows the product being used in a real context. For service businesses, it might be a screen recording walking through your software, a before-and-after renovation sequence, or a time-lapse of your process. Demo videos reduce buyer anxiety by answering the implicit question: &ldquo;Do I actually understand what I'm paying for?&rdquo; They are particularly high-converting on website service pages and in email nurture sequences.</p>

    <h2>3. Customer Testimonial</h2>

    <p>Video testimonials are the single most trusted form of social proof available to a small business. A client speaking candidly about their experience with your business &mdash; with their face visible, in a real location, in their own words &mdash; is more persuasive than any amount of marketing copy. Most happy clients are genuinely willing to participate when the process is made easy: 15 minutes, at their office or on a call, no preparation needed. The cost of producing a testimonial video is relatively modest ($300&ndash;$800); the conversion value is disproportionately high.</p>

    <h2>4. Behind-the-Scenes</h2>

    <p>Behind-the-scenes content shows the real people, processes, and culture behind your business. A kitchen preparing for service, a tradesperson mid-job, a designer at the drafting table &mdash; these moments humanise a brand in ways that polished, formal content cannot. Behind-the-scenes content performs exceptionally well on Instagram and TikTok, has a low production threshold (a smartphone is sufficient), and builds a sense of transparency and authenticity that modern consumers actively value.</p>

    <h2>5. Explainer / Animated Video</h2>

    <p>Explainer videos &mdash; either animated or live-action &mdash; are best suited for businesses with complex, abstract, or technical offerings. If what you do is difficult to explain in a few words, a structured 60&ndash;90 second explainer can do the heavy lifting that your homepage copy struggles with. Animation excels for digital products, financial services, and anything involving invisible processes. Live-action explainers work for professional services and anything where a human face adds credibility.</p>

    <ul>
      <li><strong>Start here if your budget is limited:</strong> behind-the-scenes content on your phone is free to produce and builds genuine brand affinity</li>
      <li><strong>Add this next:</strong> customer testimonials as you build your client base; the trust ROI is exceptional</li>
      <li><strong>Invest here when ready:</strong> a polished founder story or brand overview video to anchor your website and paid channels</li>
    </ul>

    <p>The most common mistake Perth small businesses make is waiting until they have the &ldquo;perfect&rdquo; setup before starting. Behind-the-scenes content filmed today on an iPhone will outperform a polished brand video that never gets made. Start where you are, with what you have, and upgrade your production quality as your content strategy matures.</p>
""",
    },
    {
        "slug": "blog-drone-footage-real-estate-perth",
        "title": "How Drone Footage Is Used in Real Estate Marketing in Perth",
        "tag": "Real Estate",
        "read_time": 4,
        "meta": "Drone footage has become standard in Perth real estate marketing. Here's how aerial video works, the legal requirements, and when it's worth the investment.",
        "content": """
    <p>Aerial drone footage has shifted from a premium add-on to an expected element of professional real estate marketing in Perth over the past five years. The reason is straightforward: Perth's urban geography makes drone footage unusually relevant. Proximity to the coast, the Swan River, major parks, and suburb context are key value drivers for Perth properties &mdash; and these features are only visible from the air. Here is everything a Perth vendor or agent needs to know about real estate drone footage.</p>

    <h2>What Drone Footage Captures for Perth Properties</h2>

    <p>Ground-level photography and video can only show what a person standing on the property can see. Drone changes the frame of reference entirely. An aerial shot of a property in Cottesloe communicates its distance from the beach in a single frame. A drone pan over a Duncraig or Carine property shows the street layout, tree canopy, and proximity to parks that define the neighbourhood's liveability. For a large lot in the Hills, drone is often the only way to convey the true scale of the land relative to the house.</p>

    <p>Drone also captures development context that matters to investors and developers &mdash; adjacent vacant lots, nearby commercial developments, and the shape of the landholding as seen from above. For off-the-plan or renovation projects, drone footage of the site combined with rendered overlays communicates potential in a way no ground-level image can.</p>

    <h2>CASA Licensing Requirements in WA</h2>

    <p>Commercial drone operations in Australia are regulated by the Civil Aviation Safety Authority (CASA). Any operator flying a drone for commercial purposes &mdash; including real estate photography &mdash; must hold at minimum a Remote Pilot Licence (RePL) and operate under an approved operator certificate. Unlicensed commercial drone work is illegal and exposes both the operator and the client to liability.</p>

    <ul>
      <li>Perth Airport and Jandakot Airport both have controlled airspace; drone flights within these zones require specific CASA authorisation</li>
      <li>RAAF Pearce near Bullsbrook is a restricted zone with strict airspace controls</li>
      <li>Standard operating conditions require flights below 120m AGL and within visual line of sight</li>
      <li>Night operations and flights over people require additional approvals</li>
      <li>Always ask your drone operator to confirm their RePL and operator certificate before booking</li>
    </ul>

    <h2>When Is Drone Worth the Investment?</h2>

    <p>A standard real estate drone session in Perth &mdash; including editing and colour grading to match interior footage &mdash; typically runs $350&ndash;$700. For properties at the lower end of the price range, this is a meaningful proportional cost. For premium properties, it is an essential marketing investment. The general guidance: drone footage makes most economic sense for properties priced at $700,000 or above, large lots with significant land area, properties within 2km of the coast or river, and properties where the street or suburb context is a key selling point.</p>

    <p>The best time of day for Perth real estate drone is golden hour &mdash; the 45 minutes after sunrise or before sunset. At this time, the sun is low, shadows are long and dramatic, and the warm light quality is cinematic. Midday drone footage in Perth's summer produces flat, harsh images that serve the property poorly. Booking your drone session at golden hour adds a scheduling complexity but meaningfully improves the final product.</p>
""",
    },
    {
        "slug": "blog-roi-video-content-perth-businesses",
        "title": "The ROI of Video Content for Perth Businesses",
        "tag": "Strategy",
        "read_time": 5,
        "meta": "Can Perth businesses actually measure the return from video content? A practical framework for calculating video ROI and setting realistic expectations.",
        "content": """
    <p>The ROI of video is one of the most discussed and least precisely measured topics in marketing. Business owners who invest in video production reasonably want to know whether they are getting their money back. The challenge is that video contributes to business outcomes through multiple pathways &mdash; brand awareness, trust-building, SEO, direct conversions &mdash; and not all of those pathways are directly attributable in a simple analytics dashboard. Here is a practical framework for thinking about video ROI in a Perth business context.</p>

    <h2>Define Your Goal Before Measuring Anything</h2>

    <p>Video ROI is only measurable against a defined goal. The same video can deliver completely different &ldquo;ROI&rdquo; depending on what you were trying to achieve. The main goal categories are brand awareness (reach, impressions, follower growth), lead generation (form fills, calls, enquiries directly attributable to video), conversion support (video viewed before a purchase or booking), and retention (repeat business from clients who engage with your content regularly). Each of these requires different tracking approaches and has different payback timelines.</p>

    <h2>How to Track Video Performance</h2>

    <p>For lead generation goals, add UTM parameters to every link you include in video descriptions, captions, and pinned comments. UTM parameters let Google Analytics attribute website sessions, enquiry form fills, and other conversion events to the specific video that drove them. This is not perfect attribution &mdash; a viewer might watch your video on Tuesday and return directly on Thursday to enquire &mdash; but it captures a meaningful portion of the signal.</p>

    <p>Website session behaviour data tells a powerful story about video impact even without direct conversion tracking. Pages with embedded video have higher average session duration and lower bounce rates than equivalent pages without video. These signals improve your SEO performance over time, which compounds into more organic traffic and more enquiries. Track your website's average session duration before and after adding video content to key pages.</p>

    <ul>
      <li>Ask every new enquiry: &ldquo;How did you find us?&rdquo; and record the answer; many clients who found you through a YouTube video or Instagram Reel will tell you if you ask</li>
      <li>YouTube Analytics provides detailed retention, click-through rate, and traffic source data; for search-optimised content, watch your impression count grow over time</li>
      <li>LinkedIn video analytics shows view count, unique viewers, and engagement rate per post</li>
      <li>Instagram Reels insights track reach, plays, likes, shares, and saves &mdash; saves and shares are the strongest signals of high-value content</li>
    </ul>

    <h2>Realistic Expectations and the Compounding Effect</h2>

    <p>Brand videos pay off over 12&ndash;24 months, not in the week after publication. A testimonial video or service explainer placed on a high-traffic page of your website is an asset that earns value every day it is live. A YouTube video optimised for a Perth service search can generate leads three years after it was uploaded, with zero additional production or promotion cost. This compounding characteristic is what makes video fundamentally different from paid advertising, which stops generating leads the moment you stop paying.</p>

    <p>A simple break-even calculation: if a new client is worth $1,500 in gross profit and a brand video costs $3,000, you need two new clients who can be attributed (directly or indirectly) to that video to break even. Given that most professional business videos remain relevant and discoverable for two to five years, two attributable clients over that timeframe represents an extremely modest hurdle. Most Perth businesses that invest consistently in video production find the compounding value of their content library to be one of their highest-returning marketing investments over a three-to-five year horizon.</p>
""",
    },
    {
        "slug": "blog-how-to-choose-video-editor-perth",
        "title": "How to Choose a Video Editor in Perth",
        "tag": "Guides",
        "read_time": 4,
        "meta": "Choosing the right video editor in Perth can make or break your project. What to look for, the questions to ask, and how to avoid costly mistakes.",
        "content": """
    <p>Perth has a growing number of talented video editors and videographers, which is excellent for businesses seeking quality work at competitive prices. It also means that finding the right person for your specific project requires more than a quick Google search and a price comparison. The questions you ask before hiring, the portfolio work you review, and the red flags you look for matter more than the hourly rate in the final decision.</p>

    <h2>Questions to Ask Before Hiring</h2>

    <p>Before committing to any video editor in Perth, work through these questions in your initial conversation or briefing email:</p>

    <ul>
      <li><strong>What is your experience with this type of video?</strong> A real estate video editor and a corporate testimonial editor have very different skills; ask specifically about comparable projects</li>
      <li><strong>Can I see three examples of similar work?</strong> Not their showreel &mdash; three specific examples matching your brief</li>
      <li><strong>What is your typical turnaround time for this scope of work?</strong> Get a specific number, not &ldquo;it depends&rdquo;</li>
      <li><strong>How many revision rounds are included in your quote?</strong> Industry standard is two; more than three should be reflected in a higher price</li>
      <li><strong>What file formats do you deliver, and at what resolution?</strong> Confirm your platforms require before the edit starts</li>
      <li><strong>What editing software do you use?</strong> Premiere Pro, DaVinci Resolve, and Final Cut Pro are all professional-grade; be cautious of editors working only in consumer tools for professional briefs</li>
      <li><strong>How do you prefer to receive feedback?</strong> Organised editors use timestamp-based feedback tools; this question reveals professionalism</li>
      <li><strong>Is your pricing project-based or hourly?</strong> Project-based gives you cost certainty; hourly can escalate unpredictably</li>
    </ul>

    <h2>Red Flags to Watch For</h2>

    <p>An editor who cannot show relevant portfolio work in your category is a risk. A real estate video portfolio has no bearing on their ability to produce a B2B corporate overview. Inability to provide a written quote with clear scope is a sign of either inexperience or a business practice that leads to scope disputes. No revision policy means disagreements about what was agreed will be resolved in their favour. Poor communication responsiveness before the project starts is a reliable predictor of poor communication responsiveness during it.</p>

    <h2>Experience vs Specialisation, and Freelancer vs Agency</h2>

    <p>A specialist with two years of experience in your video category will typically deliver better results than a generalist with ten. If you need restaurant video content, find an editor whose portfolio is full of food and hospitality work &mdash; they understand lighting for food, pacing for atmosphere, and music for dining experiences in a way a generalist does not intuitively grasp.</p>

    <p>Freelancers are often more cost-effective and offer more direct communication than agencies. Agencies bring additional resources (producers, motion graphics artists, audio engineers) that matter for large or complex productions. For most Perth small business video projects, a specialist freelancer is the better-value choice. Perth Content connects you with pre-vetted professionals matched to your specific brief, removing the research burden entirely.</p>
""",
    },
    {
        "slug": "blog-equipment-perth-video-editors-use",
        "title": "What Equipment Do Perth Video Professionals Use?",
        "tag": "Production",
        "read_time": 4,
        "meta": "Curious what cameras, software and tools Perth video professionals use? A behind-the-scenes look at the Perth video production toolkit.",
        "content": """
    <p>Clients often ask what equipment Perth video professionals use &mdash; partly out of curiosity, and partly because they assume equipment quality directly determines output quality. The reality is more nuanced: the skill, eye, and judgment of the operator matters more than the camera body. That said, understanding the standard toolkit helps you have informed conversations with your videographer and understand what the equipment differences mean for your production.</p>

    <h2>Cameras</h2>

    <p>The <strong>Sony FX3</strong> has become one of the most common cameras on Perth corporate and commercial shoots. It is a full-frame cinema camera in a compact body &mdash; capable of producing genuinely cinematic images with excellent low-light performance, which matters for indoor Perth office shoots where lighting control is limited. The FX3 records in S-Log3 or S-Cinetone colour profiles that give editors significant flexibility in the colour grade.</p>

    <p>The <strong>Canon EOS R5</strong> is widely used by Perth real estate videographers and stills/video hybrid operators because it delivers broadcast-quality 4K video and outstanding still images from the same body &mdash; ideal for operators who provide both photography and video to real estate clients. The <strong>Blackmagic Pocket Cinema Camera</strong> (BMPCC 4K and 6K variants) is popular with editors who prioritise colour grading, as Blackmagic RAW footage is widely regarded as among the most flexible to grade in post.</p>

    <p>For drone work, the <strong>DJI Air 3</strong> and <strong>DJI Mini 4 Pro</strong> are the most common platforms on Perth real estate drone shoots. Both are licensed for commercial use, shoot in 4K, and produce footage that matches well with Sony and Canon ground-level footage after colour grading.</p>

    <h2>Editing Software</h2>

    <p><strong>Adobe Premiere Pro</strong> remains the industry-standard editing platform for most Perth video professionals. Its integration with After Effects for motion graphics, Audition for audio cleaning, and the broader Creative Cloud ecosystem makes it the natural choice for full-service production workflows.</p>

    <p><strong>DaVinci Resolve</strong> has gained significant market share in Perth's professional video community over the past three years, driven by its industry-leading colour grading tools and the availability of a free version that is fully professional-grade. Many Perth editors now use DaVinci Resolve exclusively, or use it for colour grading while cutting on Premiere. <strong>Final Cut Pro</strong> remains the platform of choice for Mac-based editors who prioritise speed of workflow, particularly for social content output.</p>

    <ul>
      <li><strong>Audio:</strong> Rode Wireless Go (lapel mic for interviews), DJI Mic (compact wireless alternative), Sennheiser boom mic for run-and-gun documentary-style work</li>
      <li><strong>Lighting:</strong> Aputure and Godox LED panels are the standard on Perth corporate shoots for their colour accuracy and CRI ratings</li>
      <li><strong>Stabilisation:</strong> DJI RS gimbal series for smooth handheld movement, slider rigs for controlled tracking shots in studio-style setups</li>
    </ul>

    <h2>What Actually Matters Most</h2>

    <p>An experienced cinematographer with a mid-range Sony mirrorless camera, proper lighting knowledge, and a good lapel mic will consistently outperform a less experienced operator with cinema-grade equipment. The camera does not choose the angle, control the light, direct the interview subject, or know when the expression is genuine. The operator does. When evaluating Perth video professionals, spend far more attention on their portfolio work than on their equipment list.</p>
""",
    },
    {
        "slug": "blog-use-video-on-perth-business-website",
        "title": "How to Use Video on Your Perth Business Website",
        "tag": "Strategy",
        "read_time": 4,
        "meta": "Video can transform your Perth business website's performance. Here's exactly where to use video, how to embed it correctly, and how to avoid killing your page speed.",
        "content": """
    <p>Adding video to your website is one of the highest-impact changes a Perth business can make to their online presence. Done correctly, it increases time on site, reduces bounce rate, improves SEO performance, and converts more visitors into enquiries. Done incorrectly &mdash; particularly embedding large video files directly on the server &mdash; it can devastate your page load speed and push potential clients away before the video even starts. Here is how to use website video strategically and technically correctly.</p>

    <h2>Where to Place Video on Your Website</h2>

    <p>The <strong>homepage hero section</strong> is the highest-impact video placement on any business website. A 60&ndash;90 second brand overview video, autoplaying muted in the background of your homepage hero, immediately communicates who you are, what you do, and the energy of your business before the visitor reads a single word. Perth businesses that add a homepage hero video consistently report higher engagement metrics and more time spent on the page.</p>

    <p>The <strong>about page</strong> is the second most impactful placement. Visitors who reach the about page are already interested &mdash; they want to know who they are dealing with. A short founder or team video here builds the personal connection that converts consideration into genuine interest. The <strong>services pages</strong> benefit enormously from a 90-second explainer on each core service &mdash; it reduces the cognitive load of explaining a complex offering through text alone.</p>

    <ul>
      <li><strong>Testimonials section:</strong> swap written reviews for video testimonials; the trust conversion uplift is significant</li>
      <li><strong>FAQ page:</strong> short video answers to common questions improve both time-on-page and SEO (Google sometimes features FAQ video answers)</li>
      <li><strong>Contact page:</strong> a short &ldquo;here's what happens when you get in touch&rdquo; video reduces enquiry anxiety and increases form completion rates</li>
    </ul>

    <h2>Technical Implementation: The Non-Negotiable Rules</h2>

    <p>Never upload video files directly to your web server. A self-hosted video file will devastate your page load speed, fail to load reliably on slow mobile connections, and cost significant bandwidth charges. Host all video on YouTube or Vimeo and embed via their iframe embed code. This offloads the serving infrastructure to platforms optimised for global video delivery, keeps your page load fast, and makes video playback reliable across all devices.</p>

    <p>Autoplay video is acceptable &mdash; and often desirable for hero sections &mdash; provided it is muted by default. Google Chrome (and all major browsers) will not autoplay video with sound without explicit user interaction. Muted autoplay is permitted and creates the cinematic hero section effect without triggering the browser's autoplay blocking. Add a visible unmute button so visitors who want sound can access it.</p>

    <p>Use lazy-loading for video thumbnails placed below the fold. If your about page has a video 800 pixels down the page, it should not load until the visitor scrolls near it. Most modern CMS platforms handle this automatically, but confirm it is active on your configuration. The same principle applies on mobile &mdash; test your video pages on a 4G connection on an actual mobile device before publishing. What looks fine on desktop broadband can be a painful experience on mobile.</p>
""",
    },
    {
        "slug": "blog-testimonial-videos-vs-written-reviews",
        "title": "Why Testimonial Videos Outperform Written Reviews for Perth Businesses",
        "tag": "Strategy",
        "read_time": 4,
        "meta": "Written reviews are valuable but video testimonials are in a different league. Here's why Perth businesses are switching to testimonial video.",
        "content": """
    <p>Google reviews, Trustpilot ratings, and client testimonials on your website are all valuable forms of social proof. But if you have ever watched a potential client's decision-making process closely, you will have noticed something: they skim written reviews quickly, looking for red flags, not building genuine trust. Video testimonials work differently. When a real person looks into a camera and describes how your business helped them, the psychological response is fundamentally different &mdash; and significantly more persuasive.</p>

    <h2>The Psychology Behind Video Testimonials</h2>

    <p>Humans are wired to read faces. We process facial expressions, tone of voice, and body language at a pre-conscious level, and we use these signals to assess whether someone is being truthful and whether their emotions are genuine. A written review strips all of this signal away. All that remains is words, which can be cherry-picked, fabricated, or simply empty of the emotional resonance that converts sceptical buyers.</p>

    <p>A video testimonial shows the client's face, captures the warmth in their voice when they describe a result they are genuinely proud of, and places them in a real, identifiable context (their office, their home, their business). This authenticity is extraordinarily difficult to fake and audiences recognise it instinctively. The client who appears relaxed, specific, and genuinely enthusiastic is more convincing than any written blurb &mdash; no matter how well-written.</p>

    <p>Research from conversion rate optimisation studies consistently shows that websites featuring video testimonials convert at rates 20&ndash;40% higher than equivalent pages with only written testimonials or no testimonials at all. Time-on-page increases significantly when video testimonials are present, and increased time-on-page directly improves your SEO ranking signals.</p>

    <h2>How to Ask Clients for a Video Testimonial</h2>

    <p>Most happy clients will agree to a short video testimonial if you make the process easy for them. Frame it as genuinely simple: 15 minutes of their time, at their office or on a video call, you ask the questions (they don't need to prepare anything), and they keep full approval rights over the final content. Very few clients with a genuinely positive experience say no to this.</p>

    <ul>
      <li><strong>Ask immediately after a positive milestone:</strong> when the project delivers results, when the client expresses satisfaction, when they refer someone to you</li>
      <li><strong>Provide the four questions in advance:</strong> What was your situation before working with us? What made you choose us over other options? What results have you achieved? What would you say to someone considering using our service?</li>
      <li><strong>Film in their environment:</strong> their office, their home, their business location adds credibility and avoids the staged feeling of a plain background</li>
      <li><strong>Keep the final edit to 60&ndash;90 seconds:</strong> long enough for substance, short enough for website placement and social ads</li>
    </ul>

    <h2>Cost vs Conversion Value</h2>

    <p>A professionally produced video testimonial costs $300&ndash;$800 in Perth, depending on location and editing complexity. A written review costs nothing. The economic question is whether the conversion premium from video justifies the cost. In almost all cases, it does: if your average client is worth $2,000 in lifetime value, a single additional conversion driven by a video testimonial over its two-to-three year useful life breaks even many times over. Think of each testimonial video as a permanently deployed sales asset, not a production expense.</p>
""",
    },
    {
        "slug": "blog-film-talking-head-video-business",
        "title": "How to Film a Great Talking Head Video for Your Business",
        "tag": "Production",
        "read_time": 5,
        "meta": "Talking head videos are one of the most powerful and accessible formats for Perth businesses. Here's how to film one that actually looks professional.",
        "content": """
    <p>The talking head format &mdash; a person speaking directly to camera, either from a script or from natural delivery &mdash; is simultaneously the most accessible and most commonly botched video format in business content. Accessibility makes people underestimate it. A well-executed talking head video, with controlled framing, clean audio, and good lighting, is one of the highest-converting pieces of content a Perth business can produce. Here is how to get it right.</p>

    <h2>Camera Placement and Framing</h2>

    <p>Camera height is the single most important and most commonly ignored technical element in talking head video. The camera must be at eye level with the subject or very slightly above. A camera placed below eye level &mdash; a phone propped on a desk, a laptop camera looking up &mdash; is unflattering, creates an uncomfortable power dynamic, and reads as amateur regardless of lighting quality. Eye-level framing is non-negotiable for professional-looking results.</p>

    <p>Frame the subject using the rule of thirds: their eyes should sit on the upper horizontal third line of the frame, not in the dead centre. Leave a small amount of headroom above the crown of the head (about 10% of the frame). If the subject is speaking to an interviewer off-camera, frame them with their face slightly off-centre and looking toward the more open side of the frame. Looking room &mdash; space in front of the face rather than behind it &mdash; feels natural; the reverse feels claustrophobic.</p>

    <h2>Background and Environment</h2>

    <p>The background tells the viewer about the subject's context and professionalism before a single word is spoken. A branded wall, an office with visible branding or credentials, a well-lit bookcase, or a clean professional environment all communicate authority. An untidy background, a distracting poster, or a plain white wall with fluorescent overhead lighting communicate nothing useful and often communicate carelessness. The outdoors (in shade, never direct sun) can produce excellent results &mdash; it provides environmental context and typically has pleasing, diffused natural light.</p>

    <h2>Lighting for Talking Head Video</h2>

    <p>Lighting is where amateur and professional talking head video diverge most visibly. The simplest and cheapest effective lighting setup is a large window to the side of the subject, not behind them. A window behind the subject creates silhouette and blows out the background; a window to the side creates a soft, directional light that is flattering and professional. On overcast days, this window light is ideal; on sunny days, direct sunlight through a window is too harsh and requires diffusion.</p>

    <ul>
      <li>A simple ring light (around $60&ndash;150) provides even frontal fill light and is sufficient for indoor content in rooms without suitable windows</li>
      <li>Avoid mixed lighting: fluorescent office light plus daylight from a window creates an unflattering colour cast that is difficult to correct in post</li>
      <li>Turn off overhead fluorescent lights and use a single, well-placed LED panel or window as your primary light source</li>
      <li>A hair light or separation light placed behind and above the subject adds professional depth and prevents the subject from blending into the background</li>
    </ul>

    <h2>Audio: The Most Important Upgrade</h2>

    <p>Poor audio destroys a talking head video faster than poor visuals. Viewers will watch slightly soft or poorly framed video without complaint; they will abandon a video with echo, background noise, or low-quality audio within seconds. The single best upgrade a Perth business can make for talking head production quality is a wireless lapel microphone system. The Rode Wireless Go II (approximately $350) clips to the subject's lapel and transmits clean, close-mic audio regardless of room acoustics. It is by far the highest-return equipment investment for non-dedicated video setups.</p>

    <p>On-camera delivery tip: your energy and expression on camera need to be approximately 20% more animated than feels natural. The camera and the editing process both flatten emotional expression. If you feel like you are performing slightly too enthusiastically, you are probably right at the level that translates naturally on screen. Speak to the camera as if addressing one specific, friendly person &mdash; not a crowd, not an abstract audience. That mental frame produces the most conversational and authentic delivery.</p>
""",
    },
    {
        "slug": "blog-youtube-for-perth-businesses",
        "title": "YouTube for Perth Businesses &mdash; Is It Worth It in 2025?",
        "tag": "Strategy",
        "read_time": 5,
        "meta": "Is YouTube worth the investment for your Perth business in 2025? The honest answer with a practical guide to getting started.",
        "content": """
    <p>YouTube divides Perth business owners into two camps: those who dismissed it years ago as something for gamers and teenagers, and those who have quietly built one of their strongest lead generation channels on it. The misunderstanding is fundamental: YouTube is not a social network. It is a search engine &mdash; the second largest search engine in the world after Google, which owns it. The implications of that distinction are significant for how Perth businesses should think about it.</p>

    <h2>Why YouTube Is Different From Every Other Platform</h2>

    <p>On Instagram, TikTok, and LinkedIn, content has a shelf life measured in hours or days. An Instagram post from last week is effectively invisible. A TikTok from three months ago is ancient history. YouTube is the opposite. A well-optimised YouTube video about a specific topic will appear in search results for that topic months or years after it was uploaded. The video is indexed by both YouTube and Google, and it continues receiving views and generating leads without any additional promotion cost. This compound effect is what makes YouTube uniquely valuable as a long-term business asset.</p>

    <p>Perth-specific searches happen on YouTube with significant volume. &ldquo;Best plumber in Perth,&rdquo; &ldquo;how to choose a property manager Perth,&rdquo; &ldquo;Perth suburb review 2025&rdquo; &mdash; these searches happen daily on YouTube, and the businesses that have videos optimised for these queries are capturing leads that their competitors are entirely absent from.</p>

    <h2>Business Types That Benefit Most From YouTube</h2>

    <p>YouTube rewards businesses that can provide genuine informational value in their content. The best-performing business channels are those that answer the questions their potential clients are actually searching for. A Perth family lawyer who publishes regular videos answering common legal questions builds search authority and client trust simultaneously. A property manager who publishes suburb market update videos positions themselves as the local expert for every potential landlord watching. A building inspector who explains what to look for in a pre-purchase inspection answers the exact question their future clients are searching.</p>

    <ul>
      <li><strong>Professional services:</strong> lawyers, accountants, financial planners, mortgage brokers &mdash; educational content builds trust and search authority</li>
      <li><strong>Trades and services:</strong> plumbers, electricians, builders &mdash; &ldquo;how to&rdquo; content demonstrates expertise and generates organic leads</li>
      <li><strong>Real estate agents:</strong> suburb guide videos, market updates, first home buyer content</li>
      <li><strong>Health practitioners:</strong> condition explanations, treatment overviews, patient education</li>
      <li><strong>Coaches and educators:</strong> course preview content, tutorial snippets, client transformation stories</li>
    </ul>

    <h2>Getting Started: The Practical Minimum</h2>

    <p>YouTube does not require expensive production to get started. A smartphone with a lapel mic, good natural light, and a quiet room is sufficient for your first dozen videos. What matters far more than production quality in the early stage is topic selection and consistency. Choose specific, searchable topics that your target clients are already looking for. Include the keyword in the first three words of your video title. Write a description that includes your keyword naturally in the first 100 words. Create a custom thumbnail with a face, high contrast, and three to five words of text.</p>

    <p>The honest caveat on YouTube: it requires sustained commitment. Most business YouTube channels see meaningful traction only after 6&ndash;12 months of consistent weekly publishing. If your business cannot commit to that timeline, the short-term returns from Instagram or LinkedIn will be faster. But for businesses willing to invest in a long-term content strategy, YouTube is arguably the highest-returning video marketing channel available to Perth businesses today &mdash; precisely because so few competitors have done the work required to build a presence on it.</p>
""",
    },
]

# ── Articles 21–30 ────────────────────────────────────────────────────────────

ARTICLES += [
    {
        "slug": "blog-event-video-perth",
        "title": "How to Get Great Video From Your Perth Corporate Event",
        "tag": "Events",
        "read_time": 4,
        "meta": "Corporate events are a prime opportunity for video content. Here's how to plan and brief your videographer to capture the best footage from your Perth event.",
        "content": """
    <p>A corporate event &mdash; a conference, product launch, awards night, workshop, or company milestone celebration &mdash; represents a concentration of valuable video moments that will never be available again once the day is over. Speeches that resonate, genuine networking energy, crowd reactions, behind-the-scenes preparation, and key stakeholder moments are all perishable content. Capturing them requires a clear brief, an experienced operator, and a plan made well before the day of the event.</p>

    <h2>Build a Shot List Before the Event</h2>

    <p>Your videographer cannot know what matters most to your organisation unless you tell them. Before the event, create a priority shot list that identifies: the must-have moments (keynote speech, award presentations, key speakers), the should-capture moments (networking sessions, exhibitor interactions, audience engagement), and the nice-to-have moments (setup time-lapse, behind-scenes team preparation, sponsor signage). Give this list to your videographer at the briefing, not on the morning of the event.</p>

    <p>Identify VIPs and key stakeholders by name and, if possible, by photograph. Your videographer needs to be able to recognise the CEO, the award winner, and the keynote speaker in a crowd. A missed moment of a key stakeholder during a significant announcement cannot be reshot. Brief your videographer on the run sheet so they know exactly when each priority moment will occur and where in the venue to position themselves for it.</p>

    <h2>Audio Considerations for Event Video</h2>

    <p>The biggest technical challenge at corporate events is audio. A venue PA system is optimised for the room, not for camera microphones. If your videographer is capturing speakers from more than five metres away using only their camera's internal mic, you will have poor audio quality regardless of how good the camera is. Solutions: request a feed directly from the venue's mixing desk (a direct audio line into the camera), use a wireless lapel mic on key speakers, or position the camera close enough to the speaker for directional mic capture.</p>

    <ul>
      <li>Always test audio capture before the event starts &mdash; not after the first speaker is already on stage</li>
      <li>Brief venue AV staff in advance about the audio feed requirement; most venues are accustomed to this request</li>
      <li>For ambient footage (networking, crowd energy), camera audio is acceptable &mdash; the quality standard is lower for these sequences</li>
      <li>If a same-day edit is needed for presentation or social media, agree on this well in advance and factor the timeline into the brief</li>
    </ul>

    <h2>Maximising the Content You Get</h2>

    <p>The most common regret after a corporate event is not capturing enough audience reaction footage. A room full of engaged, laughing, or moved attendees is compelling social proof for your brand and your event quality. Brief your videographer explicitly to capture wide shots of the audience during key moments, close-up reactions, and candid networking conversations (with consent for public-facing content).</p>

    <p>Plan your content deliverables before the shoot: a 90-second highlight reel for social media is a different edit to a 5-minute internal event recap or a 15-minute post-event download for attendees who missed sessions. Knowing your deliverables shapes what footage is prioritised during the event. A highlight reel needs punchy, energetic moments; a full event recap needs comprehensive coverage of every session. Communicate both if you need both &mdash; your videographer will capture differently for each.</p>
""",
    },
    {
        "slug": "blog-video-linkedin-perth-b2b",
        "title": "How Perth B2B Businesses Should Use Video on LinkedIn",
        "tag": "Strategy",
        "read_time": 5,
        "meta": "LinkedIn is the highest-value video platform for Perth B2B businesses. Here's a practical strategy for using video content to generate leads and build authority.",
        "content": """
    <p>LinkedIn is the only major social platform where the audience is, by design, in a professional mindset. Users are not scrolling for entertainment &mdash; they are scanning for industry insights, business trends, and professional relationships. For Perth B2B businesses, this creates a video opportunity that no other platform replicates: the ability to reach decision-makers in your target industry while they are actively thinking about their professional challenges.</p>

    <h2>Why LinkedIn Rewards Video Differently</h2>

    <p>LinkedIn's algorithm explicitly prioritises native video over all other content formats, including shared articles, static images, and text-only posts. Native video &mdash; video uploaded directly to LinkedIn rather than linked from YouTube or Vimeo &mdash; receives approximately three times the organic reach of equivalent text posts from the same profile or company page. This algorithmic advantage is particularly significant for B2B businesses because reach on LinkedIn is more valuable per impression than on any other platform: your audience is self-selected as professionals, not anonymous consumers.</p>

    <p>LinkedIn also shows video to relevant second and third-degree connections when engagement is strong. A video that earns genuine comments &mdash; not just likes &mdash; is distributed well beyond your existing followers. This makes video the most effective organic reach strategy on LinkedIn for businesses trying to expand their professional network into new sectors or new seniority levels.</p>

    <h2>Video Content That Works for Perth B2B</h2>

    <p>The LinkedIn audience will not tolerate promotional video that reads as advertising. What they engage with is content that makes them more informed, more capable, or more aware of something that matters to their professional role. The best-performing video formats for B2B LinkedIn content are:</p>

    <ul>
      <li><strong>Thought leadership pieces:</strong> 60&ndash;90 second talking head videos where a senior person in your organisation shares a genuine perspective on an industry trend or challenge</li>
      <li><strong>Behind-the-scenes process videos:</strong> showing the substance and rigour of how your work is done builds credibility with business buyers who need to trust before they purchase</li>
      <li><strong>Case study summaries:</strong> a 90-second overview of a client problem, your solution, and the measurable outcome &mdash; the most direct form of sales content that LinkedIn audiences accept</li>
      <li><strong>Industry news commentary:</strong> a short response to a relevant news item or regulation change that affects your target industry</li>
      <li><strong>Team culture glimpses:</strong> humanise your organisation without being promotional; Perth business buyers want to know who they are hiring</li>
    </ul>

    <h2>Technical Approach for LinkedIn Video</h2>

    <p>LinkedIn displays video in 16:9 horizontal format in the feed by default, but 1:1 square video also performs well and takes up more feed space on mobile. Captions are essential &mdash; LinkedIn research shows over 80% of LinkedIn video is watched without sound, as users are typically browsing in office environments. Either burn captions into the video (open captions) or upload an SRT file to LinkedIn's native caption tool.</p>

    <p>Post consistency matters more than post perfection on LinkedIn. A polished brand video published once is far less effective than a series of authentic, 60-second thought leadership videos published weekly. Start with your phone and a lapel mic, post consistently for 90 days, and review your analytics before investing in higher production value. The Perth B2B businesses winning on LinkedIn are the ones that have built the habit of regular publishing &mdash; production quality is secondary to consistency and content substance.</p>
""",
    },
    {
        "slug": "blog-colour-grading-business-video",
        "title": "Why Colour Grading Matters for Your Perth Content",
        "tag": "Production",
        "read_time": 4,
        "meta": "Colour grading is one of the most impactful and least understood steps in video post-production. Here's why it matters for Perth business video.",
        "content": """
    <p>Many Perth business owners watching a polished corporate video cannot pinpoint exactly why it looks professional &mdash; they just know it does. In most cases, the answer is colour grading. Raw camera footage, even from professional cameras, requires colour correction and grading in post-production to produce the clean, consistent, visually coherent images that define professional video. Understanding what colour grading is and why it matters helps you brief your editor better and appreciate what the post-production stage of your project actually involves.</p>

    <h2>Colour Correction vs Colour Grading</h2>

    <p>Colour correction and colour grading are related but distinct processes. Colour correction is technical: it involves balancing the exposure, white balance, and contrast of footage so that all shots in a sequence look consistent with each other. When a corporate video cuts between an interview shot in warm morning light and B-roll captured under cool office fluorescent lighting, colour correction makes both shots look like they belong in the same scene.</p>

    <p>Colour grading is aesthetic: once the footage is corrected and consistent, grading applies a deliberate visual style &mdash; a &ldquo;look&rdquo; &mdash; that supports the emotional tone of the video. A brand video for a luxury real estate developer might use a warm, rich grade with lifted shadows. A tech startup brand film might use a cooler, high-contrast look with desaturated backgrounds. A restaurant video might push warm orange and teal tones to make food look more appetising. These decisions are creative, and they significantly affect how viewers feel while watching.</p>

    <h2>What Poor Colour Work Looks Like</h2>

    <p>Clients often cannot name colour grading as the problem when they watch a video that &ldquo;looks off.&rdquo; The symptoms of poor colour work include: shots in the same sequence that look like they were filmed on different days (inconsistent white balance), skin tones that look green, orange, or grey (poor white balance correction), footage that appears flat and washed out (lack of contrast), or an overall visual style that feels generic rather than intentional.</p>

    <ul>
      <li>Inconsistent colour between interior and drone footage is one of the most common quality markers in Perth real estate video</li>
      <li>Logo colours and brand colours in on-screen graphics should be matched to the grade &mdash; a warm-toned video with a cool-toned brand colour looks disjointed</li>
      <li>Skin tone accuracy is critical for testimonial and talking-head video; human skin tone errors are noticed immediately at a subconscious level</li>
      <li>DaVinci Resolve is the industry standard tool for professional colour work; editors who grade in Premiere Pro's Lumetri panels or iMovie are working with significantly less precision</li>
    </ul>

    <h2>How to Brief for Colour Style</h2>

    <p>The most useful thing you can provide an editor regarding colour style is reference videos. Find two or three examples whose overall visual tone resonates with your brand &mdash; from any industry, not just your own. Describe what you like about them in visual terms: &ldquo;warm tones, high contrast, rich blacks&rdquo; or &ldquo;clean, neutral, bright with no stylised look.&rdquo; If you have brand guidelines with primary brand colours, share them &mdash; a good colourist can pull colour reference from your brand palette and incorporate it subtly into the grade. This brief eliminates the guesswork that produces generic or mismatched colour grades.</p>
""",
    },
    {
        "slug": "blog-case-study-video-perth",
        "title": "How to Create a Client Case Study Video for Your Perth Business",
        "tag": "Production",
        "read_time": 5,
        "meta": "Case study videos are among the highest-converting content a Perth B2B business can produce. Here's how to create one that actually wins clients.",
        "content": """
    <p>A client case study video is the most powerful sales tool most Perth businesses have never produced. Written case studies are useful, but they require reading and active engagement. A two-to-three minute video case study &mdash; a real client, in their real environment, describing their real problem, your solution, and the measurable results they achieved &mdash; creates the kind of trust and social proof that written copy simply cannot match. Here is how to produce one that converts.</p>

    <h2>The Structure of an Effective Case Study Video</h2>

    <p>Every effective case study video follows the same narrative arc, because that arc mirrors the way business buyers evaluate their own decisions. The viewer is implicitly asking: &ldquo;Is this client's situation similar to mine? Did the solution work? What specifically changed? And do I trust the person telling me this?&rdquo; Your case study needs to answer all four questions.</p>

    <p><strong>The problem (30&ndash;45 seconds):</strong> The client describes their situation before working with you &mdash; the specific challenge they faced, the pain it caused, and why they needed help. This section is the most important for audience identification: viewers who recognise their own situation in the client's description will watch everything that follows with genuine interest.</p>

    <p><strong>The decision (15&ndash;20 seconds):</strong> Why did the client choose your business over the alternatives? This section handles objections implicitly. If the client mentions that they had considered other options and chose you for a specific reason, that reason addresses the doubts of viewers in the same decision-making process.</p>

    <p><strong>The solution and experience (30&ndash;45 seconds):</strong> What did working with you actually look like? How did the process feel? Was it smooth, professional, and delivered on time? This section builds process confidence &mdash; the viewer wants to know not just what you did but what it would be like to work with you.</p>

    <p><strong>The results (30&ndash;45 seconds):</strong> Specific, measurable outcomes are the most persuasive element of any case study. &ldquo;We were really happy with the result&rdquo; is vague and forgettable. &ldquo;Our enquiry rate increased by 40% in the first month after publishing the video&rdquo; is specific and memorable. Brief your client to prepare one or two concrete metrics before the interview.</p>

    <ul>
      <li>Film at the client's premises wherever possible &mdash; it adds context and authenticity that a neutral background cannot provide</li>
      <li>Use B-roll of the client's business in action to illustrate the context they describe on camera</li>
      <li>A two-to-three minute case study is the ideal length for website and LinkedIn placement</li>
      <li>A 30&ndash;45 second cut from the same footage is ideal for paid social advertising</li>
    </ul>

    <h2>Getting Your Client to Agree</h2>

    <p>Most satisfied clients will agree to participate in a case study video when the process is made easy and the ask is framed appropriately. &ldquo;We'd love to feature your results as a case study on our website &mdash; it's 30 minutes of your time, we come to you, and you have full approval over the final cut before anything is published&rdquo; is a low-resistance ask for a client who has seen strong results. The approval rights clause matters: it removes the client's main concern (that they will look foolish or say something they regret) and gives them confidence to participate authentically.</p>
""",
    },
    {
        "slug": "blog-music-licensing-business-video",
        "title": "Music Licensing for Perth Content — What You Need to Know",
        "tag": "Production",
        "read_time": 4,
        "meta": "Using the wrong music in your business video can result in copyright strikes or legal liability. A practical guide to music licensing for Perth businesses.",
        "content": """
    <p>Music is one of the most significant contributors to the emotional impact of a video, and one of the most legally misunderstood elements of video production. Perth businesses that use commercially released music in their videos &mdash; uploaded to YouTube, Instagram, or their website &mdash; without a proper licence are exposed to copyright strikes, content removal, and in some cases, legal liability. Understanding the licensing landscape before you brief your editor or choose your music saves significant problems later.</p>

    <h2>Why Popular Music Is Off-Limits for Business Video</h2>

    <p>When a Perth business publishes a promotional video on YouTube or Instagram with a commercially released song in the background, they are using that song for commercial purposes without a licence. The copyright holder &mdash; typically a music label or publisher &mdash; has every right to request content removal, monetise the content themselves (meaning ads run on your video and the revenue goes to the label), or, in persistent cases, pursue legal action.</p>

    <p>Both YouTube and Instagram have sophisticated content identification systems (YouTube's Content ID, Instagram's Rights Manager) that automatically detect commercially released music in uploaded video within minutes. Copyright strikes on YouTube can lead to demonetisation, channel restrictions, or permanent channel suspension. On Instagram, the video is typically muted automatically or removed. Neither outcome is acceptable for business content.</p>

    <h2>Licensing Options for Perth Content</h2>

    <p>The good news is that properly licensed music for business video is more accessible and affordable than it has ever been. The main options are:</p>

    <ul>
      <li><strong>Royalty-free music libraries:</strong> platforms like Epidemic Sound, Artlist, Musicbed, and Soundstripe offer subscription-based access to professional music libraries. An annual subscription ($200&ndash;$500) typically covers unlimited use of their entire catalogue across all your business video for the subscription period. Most platforms offer commercial licences that explicitly cover YouTube, social media, and website use.</li>
      <li><strong>YouTube Audio Library:</strong> Google's free music library, available within YouTube Studio. Tracks are free to use on YouTube and for general commercial purposes. Quality varies widely but there are genuinely excellent tracks available with patient searching.</li>
      <li><strong>One-time track licence:</strong> purchasing a synchronisation licence for a specific commercially released song. This is appropriate when a specific track is integral to your brand identity. Costs range from a few hundred dollars for emerging artists to thousands for established names.</li>
      <li><strong>Original composition:</strong> commissioning an original score for a brand film or campaign. Higher cost but produces music that is uniquely yours and carries no ongoing licensing obligations.</li>
    </ul>

    <h2>Practical Guidance for Perth Businesses</h2>

    <p>For most Perth business video production, a royalty-free library subscription is the right answer. Epidemic Sound and Artlist both have excellent Perth business video use cases covered explicitly in their commercial licences. Brief your editor on which library your business subscribes to, or ask whether their quote includes music licensing. Many Perth video professionals have their own Epidemic Sound or Artlist subscriptions and include track selection as part of their service &mdash; confirm this in your briefing conversation to avoid ambiguity about who is responsible for licensing compliance.</p>
""",
    },
    {
        "slug": "blog-video-for-perth-tradies",
        "title": "How Perth Tradies Can Use Video to Win More Work",
        "tag": "Strategy",
        "read_time": 4,
        "meta": "Perth tradespeople are sitting on a massive video opportunity most haven't tapped. Here's how video content wins trust, generates leads, and fills your calendar.",
        "content": """
    <p>Perth's trades sector is intensely competitive. Plumbers, electricians, builders, tilers, and landscapers all compete for the same pool of homeowners, and most of them are marketing in exactly the same way: a static website, Google Business Profile, and word of mouth. The ones pulling ahead are adding one thing to that mix: video. And the opportunity is substantial precisely because so few tradespeople have started.</p>

    <h2>Why Trades Businesses Are Ideal for Video</h2>

    <p>Trades work is visual. You take something that is broken, damaged, or missing and you make it right. That transformation &mdash; before and after, problem and solution &mdash; is inherently compelling video content. A Perth plumber who films a camera inspection of a blocked drain, shows the blockage, and explains what caused it has just produced content that answers one of the most common searches in their category. A landscaper who documents a backyard transformation from overgrown lawn to outdoor entertaining area has produced the most persuasive selling tool in their industry: proof of their work.</p>

    <p>Before-and-after videos perform exceptionally well on Instagram Reels, TikTok, and Facebook because the transformation narrative has universal appeal and the content is immediately legible without any context. You do not need to know the Perth trades market to understand and appreciate a satisfying kitchen renovation transformation video.</p>

    <h2>Content Ideas for Perth Tradespeople</h2>

    <ul>
      <li><strong>Before-and-after project videos:</strong> document the start, key moments, and finished result of representative projects; film with your phone as you work</li>
      <li><strong>Educational &ldquo;how to spot&rdquo; content:</strong> &ldquo;Three signs your hot water system needs replacing,&rdquo; &ldquo;How to tell if your roof needs immediate attention&rdquo; &mdash; these videos rank on YouTube and establish expertise without giving away your service</li>
      <li><strong>Behind-the-scenes daily content:</strong> on the job, driving between sites, tools of the trade &mdash; builds personality and humanises the business</li>
      <li><strong>FAQ videos:</strong> answer the top five questions your clients ask before booking; reduces time on phone calls and pre-qualifies enquiries</li>
      <li><strong>Testimonials from satisfied clients:</strong> filmed at their home immediately after a successful job; the setting adds immediate context and credibility</li>
    </ul>

    <h2>Practical Starting Point for Perth Tradies</h2>

    <p>You do not need a production company to start. A modern iPhone, a $50 tripod, and the natural light on a Perth job site is enough to start building a content library. The first week's content plan: film the start and finish of your next three jobs. Post one on Instagram, one on TikTok, one as a Facebook post. Watch which platform generates enquiries and double down there.</p>

    <p>When you are ready to invest in professional content &mdash; a brand overview video, a polished case study, a properly produced YouTube tutorial series &mdash; you will have a clearer sense of what content resonates with your audience and what your brand story actually is. Start raw and authentic, upgrade to professional production when you know what you are saying and who you are saying it to.</p>
""",
    },
    {
        "slug": "blog-video-production-timeline-perth",
        "title": "How Long Does a Business Video Take to Produce?",
        "tag": "Guides",
        "read_time": 4,
        "meta": "Understanding how long video production actually takes helps Perth businesses plan content calendars and avoid last-minute rushes. A realistic timeline guide.",
        "content": """
    <p>One of the most common miscalibrations Perth business owners have about video production is timeline expectations. &ldquo;We need this video for a campaign launching next Friday&rdquo; is a request that many editors hear, often on a Monday. Whether that timeline is achievable depends entirely on the scope of the project, and understanding what the production timeline actually involves helps you plan more effectively and avoid the quality compromises that come from rushed production.</p>

    <h2>Timeline by Project Type</h2>

    <p>A <strong>social media Reel edit</strong> from provided footage (editing only, no filming required) can realistically be completed in 24&ndash;48 hours by a professional editor with a clear brief. This is the fastest turnaround available for business video content.</p>

    <p>A <strong>short corporate promo video</strong> (1&ndash;2 minutes, requiring a half-day filming session plus editing) typically runs 5&ndash;10 business days from shoot to delivery: 1 day filming, 2&ndash;3 days for the first edit cut, 1&ndash;2 days for client review, 1&ndash;2 days for revisions, and final delivery. This timeline assumes a clear brief, footage delivered without issues, and prompt client feedback.</p>

    <p>A <strong>full corporate brand video</strong> (2&ndash;4 minutes, full-day shoot, multiple locations, motion graphics) should be budgeted at 3&ndash;5 weeks from brief confirmation to final delivery: scripting and pre-production (1 week), filming day, first edit cut (1&ndash;1.5 weeks), revision rounds (1 week), final delivery. Rush fees typically add 25&ndash;50% to the project cost for timelines compressed below this standard.</p>

    <ul>
      <li><strong>Animation and motion graphics video:</strong> add 1&ndash;2 weeks to any timeline that includes significant animation work</li>
      <li><strong>Multi-deliverable projects</strong> (brand video plus three social cuts plus YouTube thumbnail): add 3&ndash;5 business days for additional deliverables</li>
      <li><strong>Revision rounds:</strong> each revision round adds 2&ndash;3 business days; minimise rounds with a clear initial brief and consolidated feedback</li>
    </ul>

    <h2>What Causes Timeline Blowouts</h2>

    <p>The most common cause of delayed video delivery is slow client feedback. Many production timelines quote a delivery date that assumes the client reviews the first cut within 24&ndash;48 hours. When feedback takes four or five business days, every subsequent milestone slips. Agree on a feedback turnaround commitment when you brief your editor &mdash; most professionals will build this into the project agreement.</p>

    <p>Last-minute scope changes are the second most common cause. A brand video brief that expands to include an additional interview subject, a new filming location, or a fundamentally different key message after editing has started can add days or weeks to a project. Invest time in finalising the brief before work begins; changes after production starts cost disproportionately more than changes made at the brief stage. The clearer and more stable your brief, the more predictable your delivery date.</p>
""",
    },
    {
        "slug": "blog-hospitality-video-perth",
        "title": "Video Marketing for Perth Hospitality Businesses",
        "tag": "Strategy",
        "read_time": 4,
        "meta": "Perth cafes, restaurants and bars are using video to fill seats and build loyal audiences. Here's how hospitality businesses can use video content effectively.",
        "content": """
    <p>Perth's hospitality sector has undergone a genuine content revolution in the past three years. Cafes, restaurants, bars, and event venues that once relied on word of mouth and print advertising are now running sophisticated video content strategies on Instagram and TikTok &mdash; and the ones doing it well are consistently fuller and more booked than their competitors. The good news for Perth hospitality operators is that video content for food and beverage is uniquely accessible: your product is inherently visual, your space is designed to be experienced, and your story is personal and genuine.</p>

    <h2>What Video Content Works for Perth Hospitality</h2>

    <p>Behind-the-kitchen content consistently outperforms all other hospitality video formats. Perth diners are genuinely interested in the story behind their meal &mdash; the chefs who prepare it, the produce sourcing philosophy, the craft of the preparation. A 30-second time-lapse of bread being made, a 15-second clip of a dish being plated, or a 60-second behind-scenes look at a Sunday brunch prep sequence will reliably outperform a menu card photograph on any social platform.</p>

    <p>Atmosphere content &mdash; the feeling of a Friday evening service, the Saturday morning coffee rush, the sound of a full dining room &mdash; sells the experience of your venue more effectively than any promotional copy. Perth diners are often choosing between multiple comparable venues. The one that makes them feel something through video content wins the booking before the menu is even considered.</p>

    <ul>
      <li><strong>Dish hero videos:</strong> a macro lens on a signature dish being plated, garnished, and presented &mdash; appetising and shareable</li>
      <li><strong>Chef and owner story:</strong> the personal philosophy behind the food and the space builds emotional connection with your brand</li>
      <li><strong>Seasonal specials announcements:</strong> a short video introducing new menu items performs far better than a text post</li>
      <li><strong>Event and function promotion:</strong> a 30&ndash;60 second highlight from a recent function shows rather than tells the capabilities of your space</li>
      <li><strong>Team culture content:</strong> showing happy, skilled, engaged staff is both an attraction tool for talent and a trust signal for guests</li>
    </ul>

    <h2>Technical Tips for Perth Hospitality Video</h2>

    <p>Lighting is the primary challenge for restaurant video production. Dark, atmospheric dining rooms that feel intimate in person photograph and film poorly under standard conditions. Professional hospitality video often uses supplementary lighting &mdash; small LED panels positioned carefully to add light without changing the atmosphere of the space. Filming during service prep, before the dining room is at full capacity, gives more lighting control than filming during peak service.</p>

    <p>Golden hour natural light (early morning or late afternoon) produces the warmest, most appetising tones for food and beverage video. If your venue has strong natural light during quieter periods, schedule food hero shoots around that light. For Instagram Reels and TikTok, consistency of posting matters more than production perfection &mdash; a Perth cafe posting three authentic behind-scenes videos per week will build a more engaged following than one that posts a polished brand film quarterly.</p>
""",
    },
    {
        "slug": "blog-captions-subtitles-perth-business-video",
        "title": "Why Your Perth Contents Need Captions",
        "tag": "Production",
        "read_time": 3,
        "meta": "Captions are no longer optional for business video. Here's why every Perth business video should have captions, and the quickest ways to add them.",
        "content": """
    <p>Adding captions to your business videos is one of the highest-return, lowest-cost improvements you can make to your video content strategy. It takes 15&ndash;30 minutes with modern tools, and the benefits span accessibility, reach, engagement, and SEO. Yet most Perth businesses publish video without captions, leaving significant value on the table. Here is the case for making captions standard on everything you publish.</p>

    <h2>The Muted Viewing Reality</h2>

    <p>The majority of social media video is watched without sound. LinkedIn's own research indicates over 80% of their video content is consumed silently. Facebook reports similar figures. When you consider the environments in which people browse social media &mdash; offices, commutes, public transport, family homes &mdash; this makes obvious sense. A video with no captions is a silent picture for most of its viewers. A video with captions communicates fully to every viewer, regardless of their audio environment.</p>

    <p>Captions are not just an accessibility feature &mdash; they are a conversion tool. A viewer who can follow your argument in a captioned video without needing to unmute is far more likely to watch to completion and respond to your call to action than one who skips past because they cannot follow the audio in their current environment.</p>

    <h2>How to Add Captions Quickly</h2>

    <p>The barrier to captioning has collapsed in recent years. Modern tools make the process fast and largely automated:</p>

    <ul>
      <li><strong>CapCut</strong> (free) offers AI-powered auto-captions in one click, with style customisation. Suitable for short-form social content where captions are burned into the video.</li>
      <li><strong>YouTube Studio</strong> auto-generates captions for all uploaded videos. Review and correct the auto-generated captions before publishing; accuracy is typically 85&ndash;95% for clear speech.</li>
      <li><strong>Descript</strong> (subscription) transcribes video, allows text editing that automatically syncs to the timeline, and exports SRT files for platform upload. Excellent for longer interview and testimonial content.</li>
      <li><strong>Rev.com</strong> offers human captioning services at approximately $1.50&ndash;$3 per minute of audio; high accuracy for technical, industry-specific, or accented speech.</li>
      <li><strong>LinkedIn</strong> accepts SRT file uploads for native video; always upload an SRT file rather than relying on auto-captions for professional content.</li>
    </ul>

    <h2>Accessibility and Legal Considerations</h2>

    <p>Under Australia's Disability Discrimination Act, businesses have obligations around accessible communication. For video content produced by government agencies, educational institutions, and regulated service providers, captioning requirements are explicit. For private businesses, the DDA creates a reasonable obligation to make content accessible to the approximately 10&ndash;15% of Australians with some degree of hearing impairment. Beyond compliance, captions benefit non-native English speakers, viewers in noisy environments, and viewers with cognitive processing differences who benefit from reading along with speech. Adding captions is the simplest way to ensure your video content serves your full potential audience.</p>
""",
    },
    {
        "slug": "blog-perth-property-market-video-trends",
        "title": "Video Trends in Perth Real Estate Marketing for 2025",
        "tag": "Real Estate",
        "read_time": 4,
        "meta": "Perth real estate video marketing is evolving fast. Here are the key video trends shaping property marketing in Perth in 2025 and what agents and vendors need to know.",
        "content": """
    <p>Perth's property market has been one of the most active in Australia for the past several years, and the marketing practices that help properties sell quickly and at strong prices have evolved alongside that market energy. Video has moved from premium add-on to standard component of competitive property marketing. Here is where Perth real estate video is heading in 2025 and what the leading agents and vendors are doing differently.</p>

    <h2>Cinematic Walkthrough as the New Standard</h2>

    <p>The era of the basic video walkthrough &mdash; a single camera operator moving steadily from room to room with no music or editing &mdash; is effectively over in the premium Perth market. The new standard is a cinematic walkthrough: a carefully edited, music-scored video that moves fluidly through the property, uses gimbal stabilisation for smooth movement, leverages golden-hour natural light, and cuts between interior warmth and outdoor lifestyle in a way that creates emotional desire rather than simply cataloguing rooms.</p>

    <p>Perth agents who invested in cinematic walkthrough video early are reporting measurably shorter days-on-market for listings in the $800,000-plus bracket. Buyers who arrive at inspections having watched a three-minute video are warmer, more emotionally invested, and more likely to make offers. The video pre-sells the experience of the property before the inspection confirms it.</p>

    <h2>Social-First Property Video</h2>

    <p>A significant shift is occurring in how Perth real estate agents use video: rather than producing a video primarily for the property portal and hosting it there, leading agents are producing content primarily designed for Instagram Reels and TikTok. A 30-second Reel of a stunning Cottesloe property can reach 10,000 people organically; the same property on a portal page reaches only people actively searching that category.</p>

    <ul>
      <li>Short-form property content (15&ndash;45 seconds) optimised for Reels and TikTok is now an expected deliverable from many Perth real estate videographers</li>
      <li>Vertical format (9:16) property video is growing significantly; many agents now request both horizontal walkthrough and vertical social cuts from the same shoot</li>
      <li>Agent personal brand content &mdash; agents presenting properties to camera, doing suburb reviews, sharing market commentary &mdash; is growing as a lead generation strategy distinct from individual property marketing</li>
    </ul>

    <h2>Drone as a Standard Feature</h2>

    <p>Drone footage has completed its transition from luxury add-on to expected standard at the $700,000-plus price point. Perth buyers of premium properties expect aerial context as a basic component of the marketing package. Agents who are not offering drone as standard are at a presentational disadvantage during vendor selection. The question has shifted from &ldquo;should we include drone?&rdquo; to &ldquo;which drone operator do we use and how do we ensure the edit matches our brand standard?&rdquo;</p>

    <p>The next evolution is narrative drone video &mdash; not just an establishing aerial shot but a drone sequence that tells a story about the property's context: approach from the coast, reveal of the property, show of the outdoor entertaining area from above, pull back to establish the suburb. Perth videographers who can deliver this narrative quality of drone content are commanding premium rates in the current market.</p>
""",
    },
]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

for a in ARTICLES:
    slug = a["slug"]
    title = a["title"]
    meta = a["meta"]
    tag = a["tag"]
    read_time = a["read_time"]
    content = a["content"]

    html = make_head(slug, title, meta, tag, read_time) + content + make_foot()

    out_path = os.path.join(BASE_DIR, f"{slug}.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated: {slug}.html")

print(f"\nDone — {len(ARTICLES)} blog posts generated.")
