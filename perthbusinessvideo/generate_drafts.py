"""
generate_drafts.py
Generates 28 draft blog post HTML files for perthbusinessvideo.com.au
Output goes to the drafts/ subdirectory.
Run: python3 generate_drafts.py
"""

import os


def make_head(slug, title, meta, tag, read_time):
    return f"""<!DOCTYPE html>
<html lang="en-AU">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | Perth Business Video</title>
  <meta name="description" content="{meta}">
  <link rel="canonical" href="https://perthbusinessvideo.com.au/{slug}.html">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../css/style.css">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "{title}",
    "description": "{meta}",
    "datePublished": "2025-01-15",
    "author": {{"@type": "Organization", "name": "Perth Business Video"}},
    "publisher": {{"@type": "Organization", "name": "Perth Business Video", "url": "https://perthbusinessvideo.com.au"}}
  }}
  </script>
</head>
<body>
<header class="site-header">
  <div class="container header-inner">
    <a href="../index.html" class="logo">Perth<span>Business</span>Video</a>
    <nav class="main-nav" id="main-nav">
      <a href="../index.html">Home</a>
      <a href="../services.html">Services</a>
      <div class="dropdown">
        <button class="dropdown-btn">Industries &#9660;</button>
        <div class="dropdown-menu">
          <a href="../corporate-video-production-perth.html">Corporate Video</a>
          <a href="../real-estate-video-perth.html">Real Estate Video</a>
          <a href="../social-media-video-editing-perth.html">Social Media Video</a>
          <a href="../event-highlight-video-perth.html">Event Video</a>
          <a href="../explainer-video-perth.html">Explainer Video</a>
          <a href="../drone-video-editing-perth.html">Drone Video</a>
          <a href="../restaurant-hospitality-video-perth.html">Restaurant Video</a>
          <a href="../youtube-video-editing-perth.html">YouTube Editing</a>
          <a href="../linkedin-video-content-perth.html">LinkedIn Video</a>
          <a href="../wedding-videography-editing-perth.html">Wedding Video</a>
        </div>
      </div>
      <a href="../about.html">About</a>
      <a href="../blog.html" class="active">Blog</a>
      <a href="../contact.html" class="btn btn-primary">Get a Quote</a>
    </nav>
    <div class="header-right">
      <button class="hamburger" id="hamburger" aria-label="Open menu" aria-expanded="false">&#9776;</button>
    </div>
  </div>
</header>
<main>
<div class="container" style="padding-top:2rem;padding-bottom:.5rem;">
  <nav class="breadcrumb"><a href="../index.html">Home</a> &rsaquo; <a href="../blog.html">Blog</a> &rsaquo; <span>{title}</span></nav>
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
      <a href="../contact.html" class="btn btn-primary btn-lg">Get a Free Quote &rarr;</a>
    </div>
  </div>
</article>
</main>
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <div class="footer-logo">Perth<span>Business</span>Video</div>
        <p class="footer-tagline">Connecting Perth businesses with expert video professionals.</p>
      </div>
      <div>
        <h4>Services</h4>
        <ul>
          <li><a href="../services.html">All Services</a></li>
          <li><a href="../corporate-video-production-perth.html">Corporate Video</a></li>
          <li><a href="../real-estate-video-perth.html">Real Estate Video</a></li>
          <li><a href="../social-media-video-editing-perth.html">Social Media Video</a></li>
        </ul>
      </div>
      <div>
        <h4>Company</h4>
        <ul>
          <li><a href="../about.html">About</a></li>
          <li><a href="../blog.html">Blog</a></li>
          <li><a href="../contact.html">Contact</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom"><p>&copy; 2025 Perth Business Video. All rights reserved.</p></div>
  </div>
</footer>
<script src="../js/main.js"></script>
</body>
</html>
"""


ARTICLES = [
    {
        "slug": "blog-video-marketing-stats-perth",
        "title": "Video Marketing Statistics Perth Businesses Need to Know in 2025",
        "tag": "Strategy",
        "read_time": 4,
        "meta": "The hard numbers behind video marketing in 2025 — and what they mean for your Perth business content strategy.",
        "content": """
    <p>Data-driven decision-making is how smart Perth businesses allocate their marketing budgets. If you are still debating whether video deserves a line item in your 2025 marketing plan, the statistics below should settle the question. These are the numbers that matter most for businesses operating in the Australian market.</p>

    <h2>The Numbers Behind Video in 2025</h2>

    <p>Video now accounts for more than 80% of all internet traffic in Australia, according to Cisco's Visual Networking Index data. This figure has grown consistently year on year and shows no sign of plateauing. For Perth businesses whose marketing strategy does not include video, that statistic represents a significant gap between where they are investing and where their audience's attention actually is.</p>

    <p>Mobile video consumption is particularly dominant. Australians consume more video on smartphones than on any other device, and the time spent per session is increasing. Perth's commuter culture &mdash; long drives, train commutes between suburbs &mdash; creates predictable windows of mobile content consumption that video content slots into naturally.</p>

    <ul>
      <li>Landing pages with video convert at rates 80% or more above equivalent pages without video, based on multiple CRO studies</li>
      <li>LinkedIn native video generates 3x more engagement than text-only posts from the same profile</li>
      <li>Email campaigns with &ldquo;video&rdquo; in the subject line achieve open rates approximately 19% higher than those without</li>
      <li>Businesses that use video in their marketing grow revenue 49% faster than those that don't, according to Aberdeen Group research</li>
      <li>Social video generates 1,200% more shares than text and image content combined</li>
      <li>85% of Facebook video is watched without sound &mdash; making captions a functional necessity rather than a nice-to-have</li>
    </ul>

    <h2>What These Stats Mean for Perth SMBs</h2>

    <p>Each statistic points toward the same strategic conclusion: video is where attention is, and attention is where marketing investment belongs. The landing page conversion figure is immediately actionable &mdash; adding a 90-second explainer video to your key service page is one of the fastest ways to increase enquiry rate without changing anything else. The LinkedIn video engagement stat matters for any Perth B2B business trying to grow its professional network. The email open rate figure means video-teaser emails should be tested in any email marketing programme.</p>

    <p>The 49% faster revenue growth statistic is the most significant for long-term planning. It reflects not just the direct conversion uplift from individual videos but the compound effect of brand awareness, SEO performance, and social reach that a consistent video strategy builds over time. Perth businesses that start investing in video seriously in 2025 will have a compounding content asset in 2027 that late adopters cannot quickly replicate.</p>

    <p>Apply each statistic directly to your own business: identify your highest-traffic page with no video and add one. Identify your best-performing LinkedIn content and create a video version. Identify the email in your welcome sequence that has the lowest open rate and test a subject line with &ldquo;[Video]&rdquo; added. Data is most valuable when it moves you from awareness to action.</p>
""",
    },
    {
        "slug": "blog-how-to-get-views-youtube-perth",
        "title": "How to Get More Views on Your Perth Business YouTube Channel",
        "tag": "Strategy",
        "read_time": 5,
        "meta": "Growing a business YouTube channel takes more than uploading good videos. Here's a practical guide to YouTube SEO, thumbnails and channel strategy for Perth businesses.",
        "content": """
    <p>Most Perth business YouTube channels have more potential than they are currently realising. Uploading a well-produced video is only the starting point &mdash; the metadata, thumbnail, channel architecture, and posting consistency determine whether that video gets discovered by the right people. Here is a practical guide to the factors that drive YouTube views for business channels.</p>

    <h2>YouTube SEO: The Fundamentals</h2>

    <p>YouTube is the second largest search engine in the world. Optimising your videos for search is the single most impactful thing you can do to grow views over time, because search-driven views compound &mdash; a well-optimised video from six months ago continues receiving views today without additional effort.</p>

    <p>The most important placement for your target keyword is the first three words of the video title. YouTube's algorithm places heavy weight on title-start keywords. &ldquo;Perth plumber costs 2025&rdquo; will outperform &ldquo;Everything you need to know about plumber costs in Perth&rdquo; for the search query &ldquo;Perth plumber costs,&rdquo; even though both titles target the same keyword. Put the keyword first.</p>

    <p>The video description should include your primary keyword naturally within the first 100 words &mdash; YouTube indexes the description and uses it to understand video content. Write a genuine 150&ndash;300 word description that describes what the video covers, includes the keyword two to three times, and ends with a call to action and relevant links. Tags should be keyword phrases (two to four words each), not single words. Include your primary keyword, three to five related keyword variations, and your business name.</p>

    <h2>Thumbnail Strategy</h2>

    <p>Your thumbnail's only job is to earn the click. YouTube's own data shows that thumbnails featuring human faces significantly outperform scene-only thumbnails across almost all content categories. The face should be expressive &mdash; a neutral expression is less clickable than a curious, surprised, or engaged expression. Text overlay should be three to five words maximum, large enough to read on a mobile screen, and in high-contrast colours against the background.</p>

    <ul>
      <li>Use consistent thumbnail design across your channel &mdash; viewers should recognise your brand at a glance while browsing</li>
      <li>Click-through rate (CTR) is the metric to watch: a healthy business channel CTR is 5&ndash;10%; below 3% indicates a thumbnail or title problem</li>
      <li>Average view duration (AVD) target: aim for 50% or higher; if viewers consistently leave before halfway, the video's opening needs reworking</li>
      <li>Playlists organise your content thematically and improve session watch time (viewers watch the next video in the playlist automatically)</li>
    </ul>

    <h2>Optimising for Perth Local Search</h2>

    <p>For Perth service businesses, including your location in titles and descriptions drives highly targeted local views. &ldquo;Best coffee roasters in Perth,&rdquo; &ldquo;Perth mortgage broker explains,&rdquo; and &ldquo;How to [action] in Perth&rdquo; structures all capture local search intent effectively. Perth-specific content also performs well in Google search results &mdash; Google often features YouTube videos for local service queries, giving you a second position in the results page alongside your website listing.</p>

    <p>Post consistently and review your YouTube Analytics monthly. The two metrics that matter most for a growing channel are CTR (thumbnail and title effectiveness) and AVD (content quality and audience retention). Build a simple monthly routine: review the previous month's best-performing video, identify why it outperformed, and replicate those elements in the next month's content plan.</p>
""",
    },
    {
        "slug": "blog-product-demo-video-convert",
        "title": "How to Create a Product Demo Video That Converts",
        "tag": "Production",
        "read_time": 4,
        "meta": "A product demo video that actually converts has a specific structure. Here's how to plan, produce and place a demo video that drives action for your Perth business.",
        "content": """
    <p>A product demo video is one of the highest-converting pieces of content a product or service business can publish &mdash; but only when it is built around the viewer's decision-making process, not around the product's feature list. Most demo videos fail because they are structured as tours rather than arguments. Here is how to build a demo video that actually converts.</p>

    <h2>What Makes a Demo Video Convert</h2>

    <p>A converting demo video addresses a specific pain point before it demonstrates anything. Viewers who feel their problem being described accurately will lean forward; viewers who encounter a product introduction without context will scroll past. Open with the problem, not the product. &ldquo;If you've ever spent hours trying to reconcile your monthly invoices&rdquo; earns the attention of every accounting software user before the software has appeared on screen.</p>

    <p>Show, do not tell. A demo video that shows the product in real use is more persuasive than one that describes its features in voiceover. For digital products, a clean screen recording showing the actual workflow is more effective than stock footage of people looking at computers. For physical products, show the product being used in a real context by a real person, not in a sterile studio with perfect lighting and no human element.</p>

    <h2>The Converting Demo Structure</h2>

    <p>A 90-second to 2-minute demo video should follow this structure: problem (15 seconds) that names the specific frustration or gap your product solves; solution demo (60&ndash;90 seconds) showing the product or service in genuine use, focused on the two or three most impactful features rather than a comprehensive tour; social proof (15 seconds) with a brief quote or result from a real customer; and CTA (10 seconds) with one clear, specific next step.</p>

    <ul>
      <li>Keep the demo focused on the outcome the viewer wants, not the features you are proud of</li>
      <li>For digital products: Loom and OBS are excellent screen recording tools for DIY demos; clean up your desktop and browser before recording</li>
      <li>For physical products: a smartphone with a gimbal and good natural light is sufficient for a strong product demo</li>
      <li>Where to use it: product page (primary), email sequences after sign-up or trial, paid social ads (cut a 30-second version), sales proposals</li>
    </ul>

    <h2>Testing and Improving Your Demo</h2>

    <p>A demo video is not a set-and-forget asset. Track its performance with embedded analytics: Wistia, Vimeo, and YouTube all show you exactly where viewers stop watching. If 60% of viewers leave at the 45-second mark, something at that point is losing them &mdash; whether it is a pacing issue, a confusing feature explanation, or a loss of relevance. Use that data to edit and improve.</p>

    <p>A/B testing your demo is genuinely worth doing for high-traffic product pages. Create two versions with different hooks or different CTA placements, split traffic between them, and let data determine which performs better. Even a 10% improvement in demo completion rate on a product page with 500 monthly visitors can meaningfully move conversion rates. Treat your demo video as a living asset that improves over time, not a one-time production expense.</p>
""",
    },
    {
        "slug": "blog-conference-event-video-capture",
        "title": "What to Capture at Your Perth Conference or Event (Video Guide)",
        "tag": "Events",
        "read_time": 4,
        "meta": "A practical shot list and briefing guide for getting great video footage from your Perth conference or corporate event.",
        "content": """
    <p>Corporate events are time-limited opportunities. Once the conference ends, the keynote is over, and the attendees have gone home, the footage you captured is all you have. A poorly briefed videographer will return with technically competent footage that misses the moments that actually mattered to your organisation. The solution is not a better videographer &mdash; it is a better brief. This guide gives you the shot list and preparation framework to get everything you need.</p>

    <h2>The Essential Shot List</h2>

    <p>Every Perth corporate event video brief should include these non-negotiable elements: wide establishing shots of the venue exterior and interior before the event fills with people; keynote and key speaker footage from both wide angle (showing the speaker in context with the screen or stage) and a tighter head-and-shoulders shot for emotional connection; audience reaction shots during high-energy or emotionally significant moments; networking session footage capturing the energy and density of the room; signage, branding, and sponsor logo coverage; and any awards or recognition moments, from both the presenter and the recipient.</p>

    <p>Beyond these essentials, the most valuable and most commonly missed footage is candid attendee interaction. Two colleagues animatedly discussing a session, a first-time attendee looking around at the scale of the event, a speaker signing a book for an attendee &mdash; these unscripted human moments are what transform a competent event recap into a compelling brand story. Brief your videographer explicitly to hunt for these moments between scheduled items.</p>

    <h2>Attendee Interviews</h2>

    <p>On-camera attendee interviews are among the most powerful content you can capture at a corporate event. A 30-second comment from a delegate describing what they took from a session, or why they attended, provides authentic social proof that no promotional copy can replicate. Brief your videographer to approach four to six attendees during breaks for short, informal interview segments. Provide a suggested question: &ldquo;What's the most valuable thing you've got from today's event?&rdquo; works in almost every context.</p>

    <ul>
      <li>Provide the run sheet to your videographer at least 48 hours before the event, not on the morning itself</li>
      <li>Identify VIPs and key speakers by name and photograph so they cannot be missed in a crowd</li>
      <li>Multi-camera setups (two cameras minimum) are recommended for keynote capture: one wide, one close</li>
      <li>Confirm the audio feed arrangement with venue AV staff well before the event day</li>
      <li>If a same-day highlight reel is needed for social media or closing plenary, agree on this explicitly and confirm the editing timeline</li>
    </ul>

    <h2>What to Prepare Post-Event</h2>

    <p>Brief your editor on the hierarchy of deliverables before they start: a 60&ndash;90 second social highlight reel typically has different priorities to a 5-minute internal recap or a 15-minute full session recording. Each deliverable needs different footage prioritised. Transfer and back up all event footage immediately &mdash; event footage is genuinely irreplaceable, and data loss in this context is a significant organisational problem. Provide your editor with the run sheet and a list of key moments with approximate timestamps so they can find priority footage efficiently.</p>
""",
    },
    {
        "slug": "blog-video-email-marketing-perth",
        "title": "How to Use Video in Your Perth Business Email Marketing",
        "tag": "Strategy",
        "read_time": 4,
        "meta": "Video in email marketing increases open rates, click rates and conversions for Perth businesses. Here's how to do it correctly and avoid the technical pitfalls.",
        "content": """
    <p>Video and email marketing are a powerful combination for Perth businesses &mdash; but there is a technical reality that trips up most first attempts: email clients do not natively play video. If you try to embed an MP4 directly into an email, most of your subscribers will see a broken image. The solution is simpler and more effective than a workaround, and it still delivers the video engagement lift you are looking for.</p>

    <h2>The Technical Problem and the Correct Solution</h2>

    <p>Email clients including Gmail, Outlook, Apple Mail, and most corporate email systems do not support in-email video playback. An embedded video file either displays as a broken image, triggers security warnings, or inflates the email size to the point of triggering spam filters. The industry-standard solution is to use a static image (a screenshot of the video with a play button overlaid) that links to the video hosted on YouTube, Vimeo, or your website.</p>

    <p>This approach actually outperforms true embedded video in most A/B tests. The static thumbnail with play button creates a clear visual affordance (the viewer knows there is a video to watch) and the click takes them to your website or YouTube channel, where you can track engagement, show them related content, and present conversion opportunities. An in-email video player offers none of these advantages even when it works correctly.</p>

    <h2>How to Implement Video in Email</h2>

    <p>Take a high-quality screenshot from your video at a visually compelling moment &mdash; ideally a frame showing a face, a key result, or the most visually arresting image in the video. In your email design tool, add a red or white play button icon overlaid in the centre of the image. This is the standard pattern audiences recognise immediately as &ldquo;click to watch video.&rdquo;</p>

    <ul>
      <li>Add <strong>[Video]</strong> to your email subject line: &ldquo;[Video] How we cut our client's editing time in half&rdquo; consistently achieves 15&ndash;20% higher open rates than equivalent subject lines without the tag</li>
      <li>Mailchimp, Klaviyo, and ActiveCampaign all support this thumbnail-link approach natively; Klaviyo specifically generates video thumbnails from YouTube links automatically</li>
      <li>Use UTM parameters on the video link: <code>?utm_source=email&amp;utm_medium=newsletter&amp;utm_campaign=april2025</code> so you can attribute video views and downstream conversions to the specific email campaign</li>
      <li>Track click-through rate on the video thumbnail as your primary success metric; benchmark against your typical email CTR to measure the video lift</li>
    </ul>

    <h2>Video Types That Work in Email</h2>

    <p>Not every video type earns its place in an email campaign. The formats that perform best are: a personal founder or team message (warm, direct to camera, 60&ndash;90 seconds), a product or service demo (particularly effective in post-purchase or onboarding sequences), a customer testimonial (excellent for mid-funnel lead nurture campaigns), and an event recap or announcement (drives attendance for upcoming events or recap engagement after them).</p>

    <p>The video should feel relevant to the specific email it appears in &mdash; not a generic brand video dropped into every campaign. A subscriber who opened an email about your new service offering and finds a two-year-old brand overview video will feel the disconnect. Match the video content to the email's specific purpose and you will see the engagement lift video is capable of delivering.</p>
""",
    },
    {
        "slug": "blog-aerial-drone-footage-perth-property",
        "title": "Aerial Drone Footage for Perth Property Marketing &mdash; A Complete Guide",
        "tag": "Real Estate",
        "read_time": 4,
        "meta": "Everything Perth real estate agents and vendors need to know about drone footage — what it shows, the legal requirements, costs and when it's worth the investment.",
        "content": """
    <p>Aerial drone footage has shifted from a premium differentiator to a standard expectation in Perth's competitive real estate market. The unique visual perspective that drone provides &mdash; suburb context, lot clarity, proximity to landmarks, and cinematic reveal shots &mdash; addresses buyer questions that ground-level photography simply cannot answer. This guide covers everything you need to know about commissioning, using, and getting value from real estate drone footage in Perth.</p>

    <h2>What Drone Footage Adds to Perth Property Marketing</h2>

    <p>Perth's suburban geography makes drone footage unusually valuable compared to markets with denser, more uniform housing. In Perth, a property's value is often heavily influenced by features only visible from the air: proximity to the coast or Swan River, the size and shape of the lot relative to neighbours, the quality of the street and suburb, and access to parks and open spaces. A family considering a property in Duncraig wants to see that the beach is genuinely a 12-minute drive away; a drone shot over the suburb can show this in a single, compelling image.</p>

    <p>For large lots in the Hills, rural residential in Chittering or Mundaring, or acreage properties in the outer metro area, drone footage is the only way to convey the scale and character of the land. A property photograph shows the house; drone footage shows the context in which the house sits. For buyers making significant financial decisions, that context matters enormously.</p>

    <h2>CASA Licensing Requirements for Commercial Drone Work in WA</h2>

    <p>Commercial drone operations in Australia require the operator to hold a Remote Pilot Licence (RePL) issued by CASA and to operate under a registered operator certificate. There are no exceptions for &ldquo;small&rdquo; commercial jobs &mdash; any drone flight conducted for commercial gain requires both certifications. Ask your drone operator to confirm their RePL number and operator certificate before booking.</p>

    <ul>
      <li>Perth Airport has a controlled airspace zone (CTR) that requires specific CASA authorisation for any commercial drone operation within it; properties near Perth Airport, Jandakot, or Gnangara are affected</li>
      <li>RAAF Pearce near Bullsbrook is a restricted area requiring special CASA approval</li>
      <li>Standard operating conditions require drone flights to remain below 120m AGL and within visual line of sight at all times</li>
      <li>Residential area flights require operators to maintain certain distances from people who have not consented to be overflown</li>
    </ul>

    <h2>Costs, Timing, and Editing Tips</h2>

    <p>A standard Perth real estate drone session including flight and post-production typically runs $350&ndash;$700, depending on location, session length, and whether advanced colour grading to match interior footage is included. Budget the higher end for premium properties where cinematic quality is expected. The best time of day for Perth real estate drone is golden hour &mdash; roughly 6&ndash;8am or 5&ndash;7pm in summer &mdash; when the sun is low, shadows are dramatic, and the warm light quality flatters both the property and the suburb.</p>

    <p>In post-production, colour grading drone footage to match interior camera footage is essential for a polished result. Drone cameras shoot in a different colour profile to most ground-level cameras, and unmatched footage looks jarring in a property video. A good real estate video editor will handle this matching as standard; confirm it is included in the quote. The drone sequence should be used as the hero opening shot of the property video, establishing context before the ground-level walkthrough begins.</p>
""",
    },
    {
        "slug": "blog-anatomy-corporate-video",
        "title": "The Anatomy of a Great Corporate Video",
        "tag": "Production",
        "read_time": 4,
        "meta": "What separates an effective corporate video from an expensive one that nobody watches? The five structural elements every great corporate video shares.",
        "content": """
    <p>The Perth business landscape is full of corporate videos that look professional but do nothing for the business that paid for them. Polished colour grade, clean typography, impressive B-roll &mdash; and zero clarity about who the video is for, what it is asking them to do, or why they should care. Effectiveness in corporate video is about structure, not production value. Here are the five elements that every great corporate video shares.</p>

    <h2>Element 1: The Hook</h2>

    <p>The first three to five seconds of a corporate video determine whether the next 90 seconds get watched. The hook must answer the viewer's implicit question &mdash; &ldquo;Is this relevant to me?&rdquo; &mdash; immediately and clearly. The weakest possible hook is a logo animation. The second weakest is &ldquo;Hi, we're [Company Name] and we've been helping Perth businesses since [year].&rdquo; The strongest hooks lead with the viewer's problem, a surprising statistic, a bold claim, or a compelling visual that creates immediate curiosity.</p>

    <h2>Element 2: The Story</h2>

    <p>Great corporate video is narrative, not descriptive. A features list is descriptive &mdash; it tells the viewer what you do. A story shows a problem, a human experiencing it, a solution, and a resolution. Even a 90-second brand video can follow this arc: the problem your ideal client faces (the viewer identifies), the way your business solves it (relevant and specific), the outcome your clients experience (desired and believable). When viewers see their own situation in your story, they stop watching as passive consumers and start watching as active prospects.</p>

    <h2>Element 3: Credibility</h2>

    <p>Credibility elements give the viewer permission to believe the story you are telling. This does not mean listing your credentials &mdash; it means showing evidence. A client result stated specifically (&ldquo;we increased their website enquiries by 60% in 90 days&rdquo;) is more credible than a general capability claim (&ldquo;we deliver great results for our clients&rdquo;). A brief client quote, a recognisable logo, a before-and-after result &mdash; each of these adds a layer of trust without requiring the viewer to simply take your word for it.</p>

    <ul>
      <li><strong>Element 4: The CTA.</strong> One clear, specific next step. Not &ldquo;Contact us to learn more&rdquo; &mdash; that is passive and vague. &ldquo;Book a free 20-minute strategy call at the link below&rdquo; is specific, low-friction, and tells the viewer exactly what they will get. One CTA per video; multiple CTAs split attention and reduce conversion from all of them.</li>
      <li><strong>Element 5: Production quality.</strong> Production quality is last because it supports the other four elements rather than replacing them. The minimum threshold is: audio must be clean (no echo, no background noise), colour must be consistent, and pacing must earn each second. Beyond that threshold, additional production investment returns diminishing results.</li>
    </ul>

    <h2>What Makes Corporate Video Fail</h2>

    <p>The most common failure mode for Perth corporate video is producing a beautiful video with no clear purpose. It looks impressive, it represents the brand visually, and it sits on a homepage &mdash; but it was never designed to make the viewer do anything specific. Define the one action you want viewers to take before you brief a single frame. Every creative decision in the production should serve that action. A 90-second video with a clear purpose and a direct CTA will consistently outperform a three-minute production values showcase built around brand aesthetics alone.</p>
""",
    },
    {
        "slug": "blog-vertical-video-perth-business",
        "title": "Why Vertical Video Matters for Perth Business Social Media",
        "tag": "Strategy",
        "read_time": 3,
        "meta": "Vertical video is no longer just for TikTok. Why Perth businesses need to plan for 9:16 format video across their entire social media strategy in 2025.",
        "content": """
    <p>Vertical video &mdash; the 9:16 aspect ratio native to smartphone screens &mdash; has moved from a TikTok quirk to the dominant format for social media video across every major platform. Perth businesses that are still producing only horizontal (16:9) video for their social channels are consistently underperforming against competitors who plan for vertical from the shoot stage. Here is why format matters and how to plan for it correctly.</p>

    <h2>The Mobile Reality</h2>

    <p>More than 75% of social media video is watched on mobile devices, where the screen is held vertically for the overwhelming majority of use. When a horizontal video plays in a vertical mobile feed, it fills roughly 35% of the screen, flanked by black bars. A vertical video fills the entire screen. The visual difference in attention-capture potential is enormous, and the platforms reflect this: Instagram, TikTok, YouTube Shorts, and Facebook Stories all display vertical video as the full-screen native experience, while horizontal video is reduced and disadvantaged.</p>

    <h2>Platform Requirements in 2025</h2>

    <p>TikTok is built entirely around vertical video &mdash; there is no horizontal feed. Instagram Reels and Stories are both native vertical formats, and Instagram has explicitly stated that Reels in 9:16 format receive preferential algorithm treatment over repurposed horizontal content. YouTube Shorts requires vertical 9:16 content. Facebook Stories is vertical. LinkedIn is the primary professional platform where horizontal video still performs well in the feed, though square (1:1) content also works effectively.</p>

    <ul>
      <li>Horizontal 16:9 remains correct for: YouTube main channel, LinkedIn article embedding, broadcast advertising, website hero video</li>
      <li>Vertical 9:16 is required for: TikTok, Instagram Reels, Instagram Stories, YouTube Shorts, Facebook Stories</li>
      <li>Square 1:1 is a useful middle ground for Instagram grid posts and LinkedIn feed posts</li>
    </ul>

    <h2>How to Shoot for Both Formats</h2>

    <p>The smart approach is to shoot in 4K horizontal (16:9) and plan your composition for dual-format output in post. Frame your subject in the centre horizontal third of the frame, leaving clear space on both sides. When the editor crops to 9:16, the subject remains properly framed. This &ldquo;safe zone&rdquo; approach requires no additional shooting time and produces properly composed vertical content from a single horizontal shoot.</p>

    <p>Both DaVinci Resolve and Adobe Premiere Pro include smart reframing tools that automate the crop and composition adjustment for different aspect ratios. Brief your editor to deliver both 16:9 and 9:16 exports as standard deliverables for any social-bound content. The marginal editing cost is minimal; the social media reach benefit of properly formatted vertical video is significant.</p>
""",
    },
    {
        "slug": "blog-testimonial-video-builds-trust",
        "title": "How to Create a Testimonial Video That Actually Builds Trust",
        "tag": "Production",
        "read_time": 4,
        "meta": "A testimonial video only builds trust when it feels genuine. Here's how to plan, film and edit customer testimonial videos for Perth businesses that actually convert.",
        "content": """
    <p>The difference between a testimonial video that converts and one that merely fills a website page comes down to a single quality: authenticity. Viewers have calibrated, highly sensitive detectors for scripted, coached, or hollow praise. When a testimonial video feels performed, it damages trust rather than building it. Here is how to produce testimonial video that feels &mdash; and is &mdash; genuinely credible.</p>

    <h2>Who to Ask and How to Approach Them</h2>

    <p>The best testimonial subjects are clients with specific, measurable results who have expressed genuine satisfaction unprompted &mdash; the person who referred a colleague to you, who left a glowing Google review without being asked, or who mentioned their results enthusiastically in a follow-up conversation. Specificity is the key quality marker: a client who can say &ldquo;our website enquiries doubled in the first month&rdquo; is far more valuable as a testimonial subject than one who can only say &ldquo;they did a great job.&rdquo;</p>

    <p>Frame the ask as easy and low-risk: 15 minutes of their time, at their location or on a video call, no preparation required (you will ask all the questions), and they have full approval over the final cut. Most happy clients will say yes to this. The full approval clause is the key objection-handler &mdash; it removes the fear of saying something awkward or being misrepresented.</p>

    <h2>The Five Questions That Produce Great Testimonials</h2>

    <p>Send these questions in advance so the client can think &mdash; not memorise answers, just think. Ask them on camera in a conversational way, and give the client space to respond naturally without rushing:</p>

    <ul>
      <li>What was your situation or challenge before you worked with us?</li>
      <li>What made you choose us over other options you were considering?</li>
      <li>What was the experience of working with us actually like?</li>
      <li>What specific results have you seen since working with us?</li>
      <li>What would you say to someone considering using our service?</li>
    </ul>

    <h2>Filming and Editing for Authenticity</h2>

    <p>Film at the client's workplace or home rather than a neutral studio background. Their environment provides context that adds credibility &mdash; a lawyer's office, a restaurant kitchen, a retail floor all tell a story before the client speaks. Position the camera at a slight angle (not straight-on like a police interview) with natural light from a window on one side. Use a lapel mic for clean audio regardless of room acoustics.</p>

    <p>In the edit, preserve the moments that feel human: a pause before a strong answer, a genuine laugh, a moment where the client searches for the right word before finding it. These &ldquo;imperfections&rdquo; are authenticity signals. Cut the padding &mdash; the &ldquo;ums&rdquo; before answers, the lengthy setup to short points &mdash; but do not over-polish to the point where the delivery sounds like a scripted advertisement. Target 60&ndash;90 seconds for the final website version and 20&ndash;30 seconds for a social or advertising cut.</p>
""",
    },
    {
        "slug": "blog-video-for-perth-restaurants",
        "title": "Video Production for Perth Restaurants &mdash; What Works and What Doesn't",
        "tag": "Industry",
        "read_time": 4,
        "meta": "Perth restaurants using video are filling tables faster than those that aren't. Here's what video content works for hospitality businesses and how to produce it well.",
        "content": """
    <p>Perth has one of the most vibrant and competitive restaurant and cafe scenes in Australia. New venues open constantly, dining habits shift seasonally, and customer attention is spread across more channels than ever. The restaurants building loyal audiences and consistent bookings in 2025 are the ones using video to tell their story and showcase their experience &mdash; not just their menu. Here is what works for Perth hospitality video and what consistently falls flat.</p>

    <h2>What Works</h2>

    <p><strong>Behind-kitchen content</strong> is the single most effective video format for Perth restaurants. Diners are genuinely curious about the people and processes behind their meals, and content that shows the craft, care, and personality of a kitchen team builds an emotional connection that no static food photograph can replicate. A 30-second video of a chef preparing a signature dish, a time-lapse of bread making, or a behind-scenes look at a Sunday morning prep sequence consistently outperforms polished promotional content on Instagram and TikTok.</p>

    <p><strong>Atmosphere and energy content</strong> sells the experience of dining at your venue. A Friday evening service in full swing, the sound of a coffee machine and the warmth of a morning cafe, the energy of a full Saturday lunch &mdash; these atmospheric videos answer the question every diner asks before choosing a venue: &ldquo;What will it actually feel like to be there?&rdquo; Film these moments with your phone during your busiest service and post them without overthinking the production quality.</p>

    <p><strong>Chef and owner story</strong> content builds the kind of personal brand that turns casual diners into regulars. Perth diners respond strongly to the personal philosophy behind a restaurant &mdash; sourcing decisions, culinary influences, what the owner is trying to create. A 2&ndash;3 minute founder story video, professionally produced and placed on your website's about page, is one of the most durable brand assets a hospitality business can have.</p>

    <h2>What Doesn't Work</h2>

    <ul>
      <li>Generic promotional voiceover with no personality (&ldquo;At [Restaurant Name], we pride ourselves on quality ingredients and exceptional service&rdquo;) is indistinguishable from every other restaurant's marketing and earns no attention</li>
      <li>Filming without considering the specific lighting of your space: dark, atmospheric dining rooms film poorly under standard camera settings and require specific lighting knowledge or golden-hour scheduling</li>
      <li>Over-produced video that looks like a TV commercial loses the authenticity that hospitality audiences on Instagram and TikTok actively seek</li>
    </ul>

    <h2>Where to Use Restaurant Video</h2>

    <p>Instagram and TikTok are your primary channels &mdash; they are where Perth diners discover new venues and decide whether to try them. Your Google Business Profile accepts video uploads and this is an under-utilised channel for hospitality: a short atmosphere video here appears to people actively searching for dining options near your location. Your website's homepage hero section benefits enormously from a 60&ndash;90 second atmosphere and story video. For functions and events, video content that shows a previous event in your space is the strongest possible sales tool when venue-shopping clients make enquiries.</p>
""",
    },
    {
        "slug": "blog-motion-graphics-vs-live-footage",
        "title": "Motion Graphics vs Live Footage &mdash; Which Is Right for Your Perth Business?",
        "tag": "Production",
        "read_time": 4,
        "meta": "Should your Perth business video use motion graphics, live footage, or both? A practical guide to choosing the right visual approach for your goals and budget.",
        "content": """
    <p>When Perth businesses brief a video project, one of the first creative questions is whether to use live footage, motion graphics, or a combination of both. This decision affects cost, production timeline, visual style, and ultimately how effectively the video communicates its message. Here is a practical framework for making the right choice for your specific brief.</p>

    <h2>When Motion Graphics Win</h2>

    <p>Motion graphics excel at communicating abstract, intangible, or complex concepts that are difficult to film. Software products, financial services, insurance policies, supply chain processes, and multi-step workflows are all categories where animation can communicate clearly what live footage would struggle to show. If your service is fundamentally invisible &mdash; if what you do happens in a computer, in a spreadsheet, or in a strategic conversation &mdash; motion graphics let you visualise it in a way that live footage cannot.</p>

    <p>Data visualisation is another area where motion graphics are superior to any live footage approach. Animated charts, graphs, and infographics communicate numerical information with clarity and visual interest that a talking head describing numbers simply cannot match. For Perth financial services, accounting, and data-driven B2B businesses, animated data elements are a natural addition to any video brief.</p>

    <h2>When Live Footage Wins</h2>

    <p>Live footage wins whenever trust and authenticity are the primary communication objectives. A testimonial video must feature a real person speaking genuinely &mdash; animation would be absurd and counterproductive. A brand story video for a professional services firm needs real people, real environments, and real human presence to build the personal trust that converts business clients. Physical products, trade services, hospitality venues, and health practitioners all communicate more effectively through live footage because the product or service is tangible and human.</p>

    <ul>
      <li>Live footage cost range: $1,000&ndash;$5,000 for a typical Perth corporate video including filming and editing</li>
      <li>Basic motion graphics cost range: $500&ndash;$1,500 for title animations, data graphics, and icon-based explainers</li>
      <li>Complex character animation cost range: $2,000&ndash;$8,000+ depending on length and complexity</li>
      <li>Animation takes longer to produce than equivalent live footage: no filming day, but design and animation time is significant</li>
    </ul>

    <h2>The Hybrid Approach</h2>

    <p>The most versatile and commonly used approach for Perth corporate video is the hybrid: live footage as the primary storytelling vehicle with motion graphics elements added for data, process steps, key statistics, and branded text overlays. A corporate case study video might use live interview footage as the narrative spine with animated charts showing the client's results. A product overview might use live demonstration footage with motion graphic labels highlighting key features.</p>

    <p>For most Perth businesses, the recommendation is to begin with live action to establish authenticity and personal connection, adding motion graphic elements as your brand and messaging mature. An experienced editor can introduce branded motion graphic elements without a full animation production process &mdash; lower thirds, animated stats, and text reveals are within the capabilities of Premiere Pro and DaVinci Resolve without specialist animation tools.</p>
""",
    },
    {
        "slug": "blog-facebook-instagram-video-ads-perth",
        "title": "How to Use Video Ads on Facebook and Instagram for Perth Businesses",
        "tag": "Strategy",
        "read_time": 5,
        "meta": "Video ads on Meta platforms can be highly effective for Perth businesses. Here's a practical guide to formats, best practices, targeting and budget strategy.",
        "content": """
    <p>Facebook and Instagram video advertising is one of the most accessible and measurable paid marketing channels available to Perth businesses. The Meta advertising platform allows you to reach highly specific audiences with video content, track performance at the individual creative level, and optimise in real time based on data. But video ads on Meta follow different rules to organic content, and understanding those rules is the difference between effective spend and wasted budget.</p>

    <h2>Video Ad Format Options</h2>

    <p>Meta offers several video placement options, each with distinct technical requirements and audience behaviour patterns. <strong>In-Feed video</strong> appears in the news feed as a user scrolls; it can be horizontal or square (1:1 performs best for feed), with a recommended length of 15&ndash;60 seconds. <strong>Stories ads</strong> are full-screen vertical (9:16), 15 seconds per card, highly immersive. <strong>Reels ads</strong> appear between organic Reels; vertical 9:16, up to 60 seconds, and must feel native to the Reels environment to avoid immediate skip behaviour. <strong>In-Stream ads</strong> play before or during other videos; 15&ndash;30 seconds maximum before viewers can skip.</p>

    <h2>Video Ad Creative Best Practices</h2>

    <p>The most critical principle for Meta video ads is: design for mute first, audio as enhancement. Over 85% of Facebook video is watched silently. Your visual story must make complete sense without sound. Captions are not optional for Meta video ads &mdash; they are essential. Without captions, a talking-head testimonial or product demo is a silent, context-free video that loses most of its persuasive potential.</p>

    <p>The first three seconds of a Meta video ad determine whether the viewer continues watching or scrolls past. There is no warm-up period, no goodwill from familiarity, no brand recognition buffer. Your hook must be in the first frame: a problem stated, a surprising claim, a visually arresting image, or a result that creates curiosity. Logo splash screens, slow reveals, and brand introductions in the opening seconds perform poorly in every test across every category.</p>

    <ul>
      <li>Your call to action should be visible within the first 10 seconds &mdash; not just at the end; many viewers will not watch to completion</li>
      <li>Include captions that are legible on mobile screen sizes (minimum 20pt equivalent, high contrast)</li>
      <li>Square (1:1) ads take up more vertical feed space than horizontal and consistently outperform 16:9 in feed placement tests</li>
      <li>Run 3&ndash;5 creative variations per campaign to identify which hook style resonates with your Perth audience</li>
    </ul>

    <h2>Targeting Perth Audiences and Budget Strategy</h2>

    <p>For Perth-focused businesses, set your location targeting to Perth Metropolitan area (or specific suburbs for hyper-local campaigns) and layer demographic, interest, and behavioural targeting on top. Use custom audiences from your website visitor pixel to retarget people who have already shown interest. Lookalike audiences built from your existing customer list are often the highest-converting targeting approach available.</p>

    <p>Start with $10&ndash;20 per day during the testing phase, running multiple creative variations. Once you identify a creative that achieves positive return on ad spend (ROAS), scale the daily budget incrementally. Aggressive scaling too early, before identifying a winning creative, is the most common cause of wasted Meta advertising budget. Let data, not enthusiasm, drive spend increases.</p>
""",
    },
    {
        "slug": "blog-video-accessibility-perth",
        "title": "Video Accessibility for Perth Businesses &mdash; Captions, Audio Description and More",
        "tag": "Production",
        "read_time": 3,
        "meta": "Video accessibility is both a legal consideration and a business opportunity for Perth companies. A practical guide to making your video content accessible to all audiences.",
        "content": """
    <p>Video accessibility is too often treated as a compliance checkbox rather than a genuine business improvement. The reality is that accessible video content serves a broader audience, performs better on platforms that reward caption-equipped content, and demonstrates a standard of professional care that reflects well on Perth businesses. Here is what accessibility means in practice for business video and how to implement it without significant additional cost.</p>

    <h2>Captions and Subtitles: The Non-Negotiable Baseline</h2>

    <p>Captions are the most important accessibility feature for video. Approximately 10&ndash;15% of Australians have some degree of hearing impairment, but the benefits of captions extend well beyond this group. Viewers in noisy environments, non-native English speakers, people with processing differences who benefit from reading along with speech, and the majority of social media users who watch video with sound off all benefit from accurate captions.</p>

    <p>The distinction between captions and subtitles is worth understanding: captions include non-speech audio information (such as &ldquo;[upbeat music]&rdquo; or &ldquo;[crowd applause]&rdquo;) and are designed for viewers who cannot hear the audio track. Subtitles translate speech for viewers who can hear but cannot understand the language. For business video in Australia, captions are the standard requirement.</p>

    <ul>
      <li><strong>Open captions</strong> are burned into the video file itself and display on every platform automatically; ideal for social media where SRT upload is not supported</li>
      <li><strong>Closed captions</strong> are separate SRT or VTT files uploaded alongside the video; viewers can toggle them on or off; YouTube, Vimeo, and LinkedIn all support SRT upload</li>
      <li><strong>Auto-captions</strong> generated by YouTube or social platforms are approximately 85&ndash;95% accurate; always review and correct before publishing professional content</li>
      <li><strong>Descript</strong>, <strong>Kapwing</strong>, and <strong>Rev.com</strong> all offer caption generation at low cost with high accuracy</li>
    </ul>

    <h2>Legal Obligations and the DDA</h2>

    <p>Australia's Disability Discrimination Act creates obligations for businesses to ensure their communications are accessible to people with disabilities where it is reasonably practicable. For government agencies, educational institutions, and regulated service providers, captioning requirements for video content are explicit. For private businesses, the DDA creates a reasonable obligation to provide accessible alternatives. Adding captions to your video content is both straightforward and low-cost with modern tools &mdash; it is difficult to argue that providing them is not reasonably practicable.</p>

    <p>Audio description &mdash; an additional audio track that describes visual-only content for visually impaired viewers &mdash; is required for government and public sector video but is less commonly required for general business content. If your video includes important information conveyed only visually (graphs, on-screen text, visual demonstrations), ensure that information is also communicated verbally in the main audio track. This serves accessibility and often improves the clarity of the content for all viewers.</p>
""",
    },
    {
        "slug": "blog-how-long-corporate-video-perth",
        "title": "How Long Should a Corporate Video Be?",
        "tag": "Production",
        "read_time": 3,
        "meta": "The right length for a corporate video depends on its purpose and audience context. Here's a practical guide to video lengths for different business use cases.",
        "content": """
    <p>The honest answer to &ldquo;how long should my corporate video be?&rdquo; is: as long as it needs to be to deliver its message completely &mdash; and not one second longer. This sounds obvious, but it is the answer that most businesses need to hear, because the instinct is usually in the wrong direction: either too short (trying to cram a complex service into a 30-second format that serves it poorly) or too long (producing a comprehensive five-minute overview when a focused 90-second version would convert better).</p>

    <h2>Recommended Lengths by Use Case</h2>

    <p>Different contexts bring different audience mindsets, and length should serve the context first. <strong>Homepage hero video:</strong> 60&ndash;90 seconds. Visitors who land on your homepage are typically in early consideration; they want orientation, not comprehensive information. Give them the essence of who you are and what you do, and invite them deeper into the site. <strong>About page / founder story:</strong> 2&ndash;3 minutes. Visitors who reach the about page are actively interested; they came with intent to learn more. A 2-minute video serves this intent well. <strong>Service page explainer:</strong> 60&ndash;90 seconds. One service, one benefit, one CTA. Brevity signals confidence and respect for the viewer's time.</p>

    <p><strong>Case study video:</strong> 2&ndash;4 minutes. Case study viewers are in research or consideration mode; they want the full narrative arc of problem, solution, and result. Two to four minutes is appropriate for this engaged audience context. <strong>Social media promo:</strong> 15&ndash;45 seconds. Optimise for completion rate and platform algorithm preference. <strong>Paid advertising:</strong> 15&ndash;30 seconds for most Meta and YouTube pre-roll placements. <strong>Training and education video:</strong> 3&ndash;10 minutes per topic module; longer is appropriate when the viewer is actively learning and has committed to the content.</p>

    <ul>
      <li>YouTube and Vimeo analytics show exact audience drop-off points; use this data to edit future videos and identify dead-weight sections</li>
      <li>50% completion rate is a reasonable benchmark for untargeted content; targeted, relevant content should achieve 65&ndash;80%</li>
      <li>The editing rule: if cutting a section does not change the video's ability to achieve its objective, cut it</li>
    </ul>

    <h2>The Production Cost Relationship</h2>

    <p>Longer videos cost more to produce &mdash; more editing time, more footage required, higher music licensing duration, more caption work. The question is not &ldquo;can we afford a longer video&rdquo; but &ldquo;does the audience context justify the length?&rdquo; A longer video that holds its audience serves both the communication objective and the production investment. A longer video that loses 70% of viewers at the one-minute mark wastes both. Know your drop-off data before deciding on length, and use it to make evidence-based decisions about future productions.</p>
""",
    },
]

# ── Final 14 drafts ──────────────────────────────────────────────────────────

ARTICLES += [
    {
        "slug": "blog-perth-business-brand-video-guide",
        "title": "The Perth Business Owner's Guide to Brand Video",
        "tag": "Guides",
        "read_time": 5,
        "meta": "A brand video is the most important piece of video content most Perth businesses will ever produce. Here's how to plan, brief and create one that works.",
        "content": """
    <p>A brand video is different from a promotional video, a product demo, or a case study. It is the video that answers the question: &ldquo;What is this business actually about?&rdquo; Done well, it functions as the single most persuasive piece of content on your website &mdash; more effective than your best written copy, more trusted than your reviews, more memorable than any static visual. Done poorly, it is an expensive homepage ornament that nobody watches twice. Here is how to produce a brand video that earns its investment.</p>

    <h2>What a Brand Video Is (and Is Not)</h2>

    <p>A brand video is not a company overview reel. It is not a features tour. It is not a mission statement dressed up with B-roll. A brand video is a story about why your business exists, who it serves, and what changes for your clients when they work with you. The best brand videos make the viewer feel something &mdash; a recognition, an aspiration, a trust &mdash; that positions your business as the right choice before a single feature has been mentioned.</p>

    <p>The ideal brand video for a Perth SMB runs 90 seconds to 2.5 minutes. It opens with the audience's world &mdash; their challenge, their aspiration, their context &mdash; before introducing your business as the answer. It features real people (the founder, the team, ideally a client) rather than stock footage and voiceover. It ends with a clear, single call to action.</p>

    <h2>The Brief That Produces a Strong Brand Video</h2>

    <p>Your brand video brief should answer these questions before a camera is turned on: Who is this video for (specific person, not demographic description)? What do they feel before watching, and what should they feel after? What is the one thing you want them to do immediately after watching? What makes your approach different &mdash; not your features, but your philosophy and method? Who should be on camera, and why should the viewer find them compelling?</p>

    <ul>
      <li>Reference videos are essential for brand video briefs; collect three to five examples whose tone and emotional register feel right for your brand</li>
      <li>The filming location should reflect your brand; an office with character says more than a neutral studio</li>
      <li>A good brand video brief includes a one-sentence version of what the video must communicate, even before the creative brief is developed</li>
      <li>Budget range for a professional Perth brand video: $3,000&ndash;$8,000 depending on production scope</li>
    </ul>

    <h2>Distributing and Measuring Your Brand Video</h2>

    <p>A brand video should live on your website homepage, on your YouTube channel, on your LinkedIn company page, and as a pinned post across your social channels. It is the piece of content you direct people to when they ask what your business does. Track website session duration on the homepage before and after the video is added &mdash; a meaningful increase confirms the video is earning its placement. Ask new enquiries whether they watched the video; many will say yes.</p>
""",
    },
    {
        "slug": "blog-social-proof-video-perth",
        "title": "Using Social Proof Video to Win More Clients in Perth",
        "tag": "Strategy",
        "read_time": 4,
        "meta": "Social proof in video form is the most persuasive content a Perth business can produce. Here's how to use case studies, testimonials and reviews as video content.",
        "content": """
    <p>Social proof &mdash; evidence that other people have trusted your business and benefited from doing so &mdash; is one of the most powerful conversion tools in marketing. In video form, social proof becomes dramatically more persuasive than written reviews or static case studies. A real client, in their own words, describing their real experience and results builds trust in a way that no amount of self-promotion achieves. Here is how Perth businesses can build and deploy a social proof video strategy.</p>

    <h2>The Three Types of Social Proof Video</h2>

    <p><strong>Testimonial videos</strong> are direct client endorsements. A satisfied client speaks to camera about their experience with your business &mdash; the problem they faced, the solution you provided, and the results they achieved. These are the most commonly produced social proof video format and, when produced authentically with real clients in real environments, consistently among the highest-converting pieces of content a business can publish.</p>

    <p><strong>Case study videos</strong> go deeper than testimonials. They tell the full story of a client engagement: the context, the challenge, the strategy, the implementation, and the measured result. Case study videos typically run 2&ndash;4 minutes and are most effective at the consideration stage of the buyer journey &mdash; when a prospect is already interested but needs confidence before committing. For Perth B2B businesses, a portfolio of three to five video case studies is one of the most powerful sales assets available.</p>

    <p><strong>Review showcase videos</strong> aggregate multiple pieces of social proof into a single edited piece. Quotes from Google reviews, testimonial snippets from multiple clients, before-and-after results from a range of projects &mdash; compiled into a 60&ndash;90 second highlight reel. This format works well for businesses with many similar clients who would benefit from seeing a breadth of satisfied customers rather than one deep story.</p>

    <ul>
      <li>Film testimonials at the client's location: their office, their home, their business premises adds context and authenticity</li>
      <li>Specific results convert better than general praise: &ldquo;we increased bookings by 35%&rdquo; beats &ldquo;they did fantastic work&rdquo;</li>
      <li>Collect social proof video consistently &mdash; one testimonial per quarter creates a meaningful library over two years</li>
      <li>Use social proof video across your website, LinkedIn, email nurture sequences, and paid advertising</li>
    </ul>

    <h2>Making Social Proof Systematic</h2>

    <p>The businesses with the strongest social proof libraries treat testimonial collection as a business process, not an ad hoc activity. Create a simple post-project checklist: has the client expressed satisfaction? Would they be open to a 15-minute video testimonial? Flag this to your account manager at each project close. A consistent process of filming one testimonial per month, without heroic effort, produces 12 new pieces of social proof video per year. After two years, that library is a significant competitive advantage &mdash; a set of assets that new competitors simply cannot replicate quickly.</p>
""",
    },
    {
        "slug": "blog-perth-small-business-video-budget",
        "title": "How to Plan a Video Budget for Your Perth Small Business",
        "tag": "Guides",
        "read_time": 4,
        "meta": "Budgeting for video doesn't have to be complicated. Here's a practical framework for Perth small businesses to plan their annual video marketing spend.",
        "content": """
    <p>Most Perth small businesses approach video production reactively: a need arises, a quote is obtained, and the cost is absorbed or avoided based on the available budget at that moment. A better approach &mdash; and one that produces significantly better value for money &mdash; is to plan an annual video budget in advance, based on your marketing objectives and the types of content that serve them. Here is how to build that plan.</p>

    <h2>Start With Your Annual Content Objectives</h2>

    <p>Before assigning a dollar figure, define what your video content needs to achieve over the next 12 months. Common objectives for Perth SMBs include: establishing credibility with a brand story video, generating leads through an SEO-optimised YouTube presence, building social media following through regular short-form content, increasing website conversion rates with explainer and testimonial video, or supporting sales conversations with case study content. Each objective has different content requirements and different production budgets.</p>

    <h2>A Tiered Budget Framework</h2>

    <p>The following tiered framework provides a starting point for Perth small businesses at different investment levels:</p>

    <ul>
      <li><strong>Starter tier ($2,000&ndash;$5,000 per year):</strong> one professionally produced hero video (brand overview or key service explainer, $1,500&ndash;$3,000), regular DIY social content using templates built by your editor. Focus on one or two platforms. Suitable for early-stage businesses establishing their video presence.</li>
      <li><strong>Growth tier ($5,000&ndash;$12,000 per year):</strong> brand video plus two to three case study or testimonial videos, monthly professionally edited social content, YouTube channel setup and regular video. Builds a meaningful content library over 12 months.</li>
      <li><strong>Scale tier ($12,000&ndash;$25,000+ per year):</strong> ongoing content partnership with a video professional, weekly social content, regular YouTube publishing, quarterly brand and campaign videos, video advertising on Meta and Google. Suitable for businesses with video as a primary customer acquisition channel.</li>
    </ul>

    <h2>Getting Maximum Value From Your Video Budget</h2>

    <p>Regardless of budget tier, the principle of repurposing maximises value. Every professionally produced video should generate multiple content pieces across formats and platforms. A $3,000 brand video that produces the hero piece, three social cuts, a YouTube version, and a LinkedIn post series effectively costs $300&ndash;400 per deliverable &mdash; excellent value compared to producing each piece independently.</p>

    <p>Plan your annual production calendar in advance and brief your editor on the full year's objectives at the start. An editor who understands your full content plan for the year can make recommendations about when to consolidate shoots, what B-roll to capture for future use, and how to structure each project to maximise multi-use value. Reactive, individual project briefings miss these efficiency opportunities entirely.</p>
""",
    },
    {
        "slug": "blog-video-for-perth-professional-services",
        "title": "Video Marketing for Perth Professional Services Firms",
        "tag": "Strategy",
        "read_time": 4,
        "meta": "Lawyers, accountants, consultants and financial advisers in Perth are using video to build trust and win clients. Here's what works in professional services video.",
        "content": """
    <p>Professional services firms &mdash; law firms, accounting practices, consulting businesses, financial advisers, mortgage brokers &mdash; have historically been among the slowest to adopt video marketing. The reasons are understandable: professional reputation is conservative, compliance requirements are stringent, and the instinct is to present formality rather than approachability. The reality in 2025 is that professional services video, done correctly, builds the kind of trust that formal marketing copy cannot &mdash; and Perth firms that have adopted it are consistently winning clients from competitors that have not.</p>

    <h2>Why Video Works for Professional Services</h2>

    <p>Clients of professional services firms are making high-stakes decisions. They are choosing who to trust with their legal matter, their financial future, their business strategy. The decision is fundamentally about personal trust &mdash; and trust is built through familiarity, transparency, and evidence of competence. Video provides all three: a client who watches a 90-second video of a Perth lawyer explaining an area of law they care about has, in that 90 seconds, begun to know, like, and trust that lawyer. No website biography achieves that in the same timeframe.</p>

    <h2>Content Formats That Work for Perth Professional Services</h2>

    <p><strong>Educational explainer videos</strong> are the highest-value content format for most professional services firms. A financial planner who publishes a series of YouTube videos explaining superannuation strategies, tax implications, or investment options positions themselves as the most credible expert in their category for every Perth viewer of that content. The key is that the videos must be genuinely useful &mdash; not promotional overviews of the firm's services, but actual educational content that helps the viewer understand their situation better.</p>

    <ul>
      <li>A family law firm producing videos on &ldquo;what to expect during a divorce in WA&rdquo; or &ldquo;how property settlement works in Western Australia&rdquo; captures search intent from their exact target audience</li>
      <li>A mortgage broker explaining &ldquo;how to get a home loan with a small deposit in Perth&rdquo; reaches first-home buyers at the exact moment of their highest search intent</li>
      <li>An accountant publishing content on &ldquo;Perth small business tax obligations 2025&rdquo; attracts clients who need precisely that expertise</li>
      <li>Compliance note: always include appropriate disclaimers (general advice not specific financial or legal advice) as required by your regulatory framework</li>
    </ul>

    <h2>The Founder and Team Video</h2>

    <p>For professional services firms, the most persuasive single piece of content is a short video introducing the principal or team. Not a corporate overview, but a genuine personal introduction: who you are, why you work in this field, what you believe about how professional services should be delivered, and what your clients typically come to you with. Perth professional services clients are choosing a person as much as a firm. A video introduction that communicates genuine expertise, warmth, and professionalism converts interest into enquiries faster than any written profile.</p>
""",
    },
    {
        "slug": "blog-make-video-go-viral-perth",
        "title": "How to Give Your Perth Business Video the Best Chance of Going Viral",
        "tag": "Strategy",
        "read_time": 4,
        "meta": "Can Perth business videos go viral? Here's what actually drives shares and reach, and how to maximise the organic distribution of your video content.",
        "content": """
    <p>The word &ldquo;viral&rdquo; is overused and often misunderstood as a business content goal, but the underlying question is legitimate: how do you create video content that people genuinely want to share, that platforms reward with organic reach, and that spreads beyond your existing audience? The answer is not luck or formula &mdash; it is a combination of specific content characteristics and distribution decisions that are entirely within your control.</p>

    <h2>What Makes Content Shareable</h2>

    <p>Content gets shared when it makes the sharer look good to their audience, when it is useful enough that sharing it is genuinely helpful, when it is surprising or unexpected enough to create a &ldquo;you have to see this&rdquo; response, or when it creates a strong enough emotional reaction (positive or thought-provoking) that people want to share the feeling. Business video that is purely promotional &mdash; &ldquo;look at our great service&rdquo; &mdash; has no shareable quality whatsoever. Business video that is genuinely useful, entertaining, or emotionally resonant has all the raw material for organic distribution.</p>

    <p>For Perth businesses, the most reliable shareable content formats are: genuinely useful educational content that solves a real problem, surprising results or transformations (before-and-after, case studies with remarkable numbers), content that speaks specifically to the Perth experience (local references, recognisable locations, Perth-specific problems), and content that humanises the business through personality rather than promotion.</p>

    <h2>The Distribution Decisions That Multiply Reach</h2>

    <p>Even excellent content needs help with initial distribution. The first hour after posting is when most platforms make their algorithmic decision about whether to distribute your video to non-followers. Concentrate your engagement activity in that window: notify your team, send to relevant contacts, and post at the time when your specific audience is most active (for Perth B2B, Tuesday&ndash;Thursday mornings; for B2C hospitality and lifestyle, Friday evenings and Saturday mornings).</p>

    <ul>
      <li>Post natively on every platform rather than sharing a link from another platform &mdash; native video always receives priority over external links</li>
      <li>Cross-post to your personal profile (not just your business page) &mdash; personal profiles typically have significantly higher organic reach</li>
      <li>Engage genuinely with every comment in the first 60 minutes &mdash; comment activity signals to the algorithm that the content is driving conversation worth amplifying</li>
      <li>A small amount of paid promotion ($20&ndash;50) on a strong organic post can trigger algorithmic amplification that far exceeds the paid reach itself</li>
    </ul>

    <h2>The Realistic Frame for Perth Business Video</h2>

    <p>Truly viral content &mdash; millions of views, national pickup, organic distribution beyond all reasonable expectations &mdash; is rare and unpredictable for business video. The more useful goal is &ldquo;significantly beyond your existing audience.&rdquo; A Perth trades business with 500 Instagram followers that produces a compelling before-and-after video and reaches 15,000 people has had a meaningfully successful video moment. Design for genuine shareability, distribute intelligently, and measure success in terms of new audience reach rather than viral benchmarks that most business video will never reach.</p>
""",
    },
    {
        "slug": "blog-video-analytics-perth-business",
        "title": "How to Use Video Analytics to Improve Your Perth Business Content",
        "tag": "Strategy",
        "read_time": 4,
        "meta": "Video analytics tell you exactly what your audience is doing with your content. Here's how Perth businesses can use data to make better video decisions.",
        "content": """
    <p>Most Perth businesses that invest in video production publish the result and then check the view count occasionally. This is the video equivalent of running a shop and never looking at which products sell. Every video platform &mdash; YouTube, Instagram, LinkedIn, Vimeo &mdash; provides detailed analytics that tell you exactly how your audience is engaging with your content. Understanding and acting on this data is what separates businesses that improve their video performance over time from those that keep producing content with inconsistent results.</p>

    <h2>The Metrics That Actually Matter</h2>

    <p>View count is the least useful primary metric for business video. A million views that drive zero enquiries is worth nothing; a hundred views from your exact target audience that generate five new clients is exceptional. The metrics that actually tell you something useful are: completion rate (what percentage of viewers watch to the end), audience retention graph (where exactly viewers stop watching), click-through rate from video to your CTA link, and for YouTube specifically, the traffic source breakdown (how did viewers find the video?).</p>

    <p>On YouTube, the audience retention graph is the single most actionable data point. It shows you, second by second, where viewers are staying and where they are leaving. A sharp drop at the 45-second mark in a 3-minute video tells you exactly what to fix. A section where viewers consistently rewatch tells you what is most valuable and should be the model for future content.</p>

    <h2>Platform-by-Platform Analytics Guide</h2>

    <ul>
      <li><strong>YouTube Studio:</strong> watch time, average view duration, impressions CTR (target 5&ndash;10%), traffic sources, audience demographics, subscriber activity tied to specific videos</li>
      <li><strong>Instagram Insights:</strong> reach (unique accounts), plays, watch time, saves (strongest signal of high-value content), shares, follows driven by specific Reels</li>
      <li><strong>LinkedIn Video Analytics:</strong> unique views, view rate, likes, comments, shares, and follower changes tied to specific posts</li>
      <li><strong>Vimeo Analytics:</strong> play rate, finish rate, engagement graph, geographic and device breakdown, link click tracking</li>
      <li><strong>Website video (via heatmaps or Google Analytics):</strong> session duration comparison between pages with and without video, bounce rate impact</li>
    </ul>

    <h2>Building a Monthly Analytics Review Habit</h2>

    <p>Set aside 30 minutes per month to review your video analytics across platforms. Ask three questions: Which video performed best this month, and why? Which video performed below expectations, and what does the retention data suggest about why? What does the data suggest I should do differently next month? Document your answers and use them to directly inform your next content brief. After six months of consistent review, you will have a clear, data-derived understanding of what works for your specific Perth audience &mdash; an understanding no amount of general advice can replace.</p>
""",
    },
    {
        "slug": "blog-outsource-video-editing-perth",
        "title": "How to Outsource Your Video Editing in Perth",
        "tag": "Guides",
        "read_time": 4,
        "meta": "Outsourcing video editing frees up your time and raises your content quality. Here's a practical guide to finding, briefing and working with video editors in Perth.",
        "content": """
    <p>For Perth business owners who are currently editing their own social media content, the moment when outsourcing video editing makes sense usually arrives before they realise it. When you are spending three hours per week in CapCut producing Reels that you are not entirely happy with, and your hourly rate is $80 or above, the economic case for outsourcing is already made. Here is a practical guide to making the transition successfully.</p>

    <h2>What to Outsource (and What to Keep In-House)</h2>

    <p>The smart division of labour for most Perth SMBs is: outsource everything that represents your brand publicly, keep in-house the raw content capture and day-to-day Stories. This means a professional editor handles your Reels, YouTube videos, testimonials, website video, and advertising content. Your team or founder captures raw footage on phones for Stories and ephemeral content. This division delivers professional quality where it matters and maintains the volume and authenticity of day-to-day content without scaling your editing costs proportionally.</p>

    <h2>Finding the Right Editor</h2>

    <p>The most reliable way to find a quality video editor in Perth is through referral from a business whose video content you admire. Look at Instagram accounts of Perth businesses in adjacent industries (same target market, non-competing) and message them asking who edits their content. Most will tell you. Referral-sourced editors come with a relevant portfolio you have already seen and a recommendation from a trusted source.</p>

    <ul>
      <li>Perth Business Video connects businesses with pre-vetted editors matched to their specific content type and budget &mdash; removing the research burden entirely</li>
      <li>For social content editing, a per-edit pricing model ($150&ndash;$300 per Reel or short video) is typically more predictable than hourly</li>
      <li>Request a paid test edit before committing to an ongoing arrangement: provide your brief, your raw footage, and your brand guidelines, and evaluate the result</li>
      <li>A good editor will ask questions before starting &mdash; an editor who starts without clarifying the brief is a risk</li>
    </ul>

    <h2>Setting Up the Working Relationship for Success</h2>

    <p>Create a simple brand guide document for your editor: your logo files, brand colours (hex codes), preferred fonts, tone descriptors, reference videos you like, and any content that must never appear. This document, provided once, eliminates recurring briefing conversations about brand consistency. Establish a clear workflow: how raw footage is delivered (Dropbox, Google Drive, WeTransfer), how feedback is provided (frame-specific timestamps via a tool like Frame.io or simply in a shared document), and your expected turnaround time for each content type.</p>

    <p>Review your editor's work formally every three months. Share your analytics data: which pieces performed well, which underperformed, and what you observe about why. A good editor treats this feedback as valuable input and adjusts their approach accordingly. The working relationship gets better over time as the editor builds familiarity with your brand, your audience, and what works &mdash; which is why consistency with one skilled editor typically delivers better results than rotating between multiple options.</p>
""",
    },
    {
        "slug": "blog-video-content-calendar-perth",
        "title": "How to Build a Video Content Calendar for Your Perth Business",
        "tag": "Strategy",
        "read_time": 4,
        "meta": "A video content calendar turns sporadic publishing into a consistent strategy. Here's how to plan your Perth business video content 90 days in advance.",
        "content": """
    <p>The businesses producing video consistently are not the ones who are most creative or most motivated &mdash; they are the ones who have removed the decision-making friction from their content process. A content calendar answers &ldquo;what do we post this week?&rdquo; three months before the question arises. For Perth businesses trying to build a consistent video presence, planning ahead is the single most impactful operational change they can make.</p>

    <h2>The 90-Day Planning Framework</h2>

    <p>Begin your content calendar with your marketing objectives for the quarter: a product launch, a seasonal promotion, an industry event, a new service offering, or simply a general awareness goal. These anchor points anchor specific content pieces around real business moments. Between anchor points, fill the calendar with evergreen content &mdash; educational videos, behind-the-scenes content, and testimonials that are not time-sensitive and can be produced and scheduled in advance.</p>

    <p>A practical structure for a Perth SMB publishing three videos per week across two platforms: one educational piece (answers a question your target audience searches for), one social proof piece (testimonial, result, case study), and one brand or culture piece (behind-the-scenes, team, personality). This mix serves awareness, trust, and conversion objectives simultaneously without over-investing in any single content type.</p>

    <h2>The Production Batching Approach</h2>

    <p>Trying to produce each video the week it needs to go live is exhausting and inconsistent. The most sustainable approach is batching: dedicate one day per month to filming four to eight raw content pieces, then distribute editing across the following month. Perth businesses that batch their filming report dramatically lower content stress and significantly more consistent publishing records.</p>

    <ul>
      <li>Book one filming day per month in your calendar three months in advance; treat it as immovable</li>
      <li>Prepare a shot list of four to eight specific content ideas before the filming day; do not decide on the day</li>
      <li>Deliver raw footage to your editor within 24 hours of filming with a brief for each piece</li>
      <li>Schedule published content at least two weeks ahead using Buffer, Later, or your platform's native scheduling tool</li>
      <li>Review the previous month's analytics before planning the next content batch &mdash; let performance data inform topics and formats</li>
    </ul>

    <h2>Staying Consistent When Life Intervenes</h2>

    <p>The most common content calendar failure mode is the one where a busy week leads to no filming, which leads to a content gap, which leads to guilt, which leads to a longer gap. Build a &ldquo;reserve&rdquo; of three to five evergreen pieces that can be published at any time. These are your safety net for busy weeks. A single extra filming session producing five additional pieces takes less than a day and can sustain four to six weeks of emergency cover. Consistency, not perfection, is what builds an audience over time &mdash; and a reserve protects your consistency when your schedule does not cooperate.</p>
""",
    },
    {
        "slug": "blog-wedding-video-perth-guide",
        "title": "Wedding Videography in Perth &mdash; A Complete Guide for Couples",
        "tag": "Industry",
        "read_time": 5,
        "meta": "Planning your Perth wedding video? Everything you need to know about choosing a videographer, styles, packages and getting a film you'll love.",
        "content": """
    <p>A wedding video is the only way to re-experience your wedding day after it is over. The speeches, the first dance, the candid moments between the ceremony and reception &mdash; a well-shot wedding film captures not just what happened but how it felt. Perth has a strong wedding videography community, and the range of styles, packages, and price points available means there is an option for every couple's vision and budget. Here is what you need to know before booking.</p>

    <h2>Wedding Video Styles in Perth</h2>

    <p><strong>Cinematic documentary</strong> is the most popular style among Perth couples: a stylised, editorial approach that combines beautiful imagery with genuine moments to produce a film that feels more like a short cinematic piece than a simple recording. Music is carefully chosen, colour grading is intentional, and the edit tells the emotional story of the day rather than cataloguing it chronologically.</p>

    <p><strong>Traditional/documentary</strong> is a more comprehensive, chronological capture of the day's events. Less stylised, longer runtime, and focused on completeness rather than curation. Suitable for couples who want every moment captured rather than an edited highlight experience.</p>

    <p><strong>Same-day edit (SDE)</strong> is a short highlight film delivered at the reception, often played during the dinner. It requires a second editor working off-site while filming continues. A unique and impressive feature for couples who want their guests to experience the day's highlights together in the evening.</p>

    <h2>What to Look for When Choosing a Perth Wedding Videographer</h2>

    <ul>
      <li>Watch full films, not just highlight reels &mdash; a highlight reel shows their best moments; a full film shows their ability to sustain quality and tell a complete story</li>
      <li>Confirm their audio setup: clear ceremony vows and speech audio requires a dedicated wireless microphone, not just camera audio</li>
      <li>Ask about their backup plan for equipment failure &mdash; professional operators carry backup cameras and audio equipment</li>
      <li>Review their delivery timeline: most Perth wedding videographers deliver within 8&ndash;16 weeks; confirm this in writing before booking</li>
      <li>Perth price ranges: highlight film only $1,500&ndash;$2,500; full day with highlights and full edit $2,500&ndash;$5,000; premium cinematic packages $5,000&ndash;$8,000+</li>
    </ul>

    <h2>Preparing Your Videographer for Your Perth Wedding Day</h2>

    <p>Provide your videographer with a detailed run sheet at least two weeks before the wedding. Include ceremony timing, photo session schedule, reception program, and any specific moments that are non-negotiable (the surprise speech, the choreographed first dance, the moment your parent sees you in the dress for the first time). Perth light is exceptional for outdoor ceremony footage &mdash; early afternoon ceremonies in autumn and winter produce beautiful warm light; summer midday ceremonies require shade consideration. Communicate your venue layout and any access restrictions so your videographer can plan their positioning in advance.</p>
""",
    },
    {
        "slug": "blog-perth-real-estate-agent-personal-brand-video",
        "title": "How Perth Real Estate Agents Can Use Video to Build a Personal Brand",
        "tag": "Real Estate",
        "read_time": 4,
        "meta": "Perth real estate agents who invest in personal brand video are winning listings and building referral networks faster than those who don't. Here's the playbook.",
        "content": """
    <p>In Perth real estate, the most consistent predictor of long-term success is not the agency you work for &mdash; it is the strength of your personal brand. Buyers and sellers choose agents they know, like, and trust. Video is the most efficient tool available for building that know-like-trust relationship at scale, with people who have not yet met you in person. Perth agents who have invested in personal brand video consistently report shorter listing conversion timelines and higher referral rates than those who have not.</p>

    <h2>Why Personal Brand Video Works for Perth Agents</h2>

    <p>A Perth homeowner considering selling will typically shortlist two or three agents before requesting appraisals. The agents on that shortlist are almost always the ones they have seen most frequently &mdash; in their suburb, in their social media feed, in their inbox. An agent who publishes consistent, useful video content is present in front of their target audience week after week, building familiarity before the listing decision is ever made. When the seller calls, they are not choosing between unknowns &mdash; they are calling the agent they feel they already know.</p>

    <h2>Content That Builds Agent Personal Brand</h2>

    <p>The most effective personal brand content for Perth agents is hyper-local and genuinely useful. Suburb market update videos (monthly, two to three minutes, covering recent sales, current listings, and market commentary) position the agent as the acknowledged local expert. Lifestyle suburb guides (&ldquo;five things to love about living in [suburb]&rdquo;) attract buyers researching areas and introduce the agent as the go-to local voice. First home buyer education content reaches the next generation of property owners before they have formed existing agent relationships.</p>

    <ul>
      <li>Publish suburb market updates on YouTube for SEO value and on Instagram Reels and LinkedIn for reach</li>
      <li>A 60-second &ldquo;just listed&rdquo; or &ldquo;just sold&rdquo; video from each property is low-effort, high-visibility content that keeps you active in followers' feeds</li>
      <li>Behind-scenes content from an appraisal, an open home, or a settlement day humanises the process and demonstrates activity</li>
      <li>Testimonial video from past vendors and buyers is the most powerful trust-builder available; film one per quarter as a minimum</li>
    </ul>

    <h2>The Consistency Commitment</h2>

    <p>Personal brand video only delivers results when published consistently over a sustained period. An agent who posts one suburb video and then nothing for three months gains nothing from the exercise. The agents building strong personal brands through video in Perth are publishing two to four pieces of content per week, every week, across the year. This is not as demanding as it sounds when content is batched: a single filming session per fortnight can produce a week's worth of content if planned and executed efficiently. Start with one platform, establish the habit, then expand as the workflow becomes routine.</p>
""",
    },
    {
        "slug": "blog-interview-on-camera-tips-perth",
        "title": "How to Look and Sound Great on Camera for Your Perth Business Video",
        "tag": "Production",
        "read_time": 4,
        "meta": "Being on camera is a skill, and it can be learned. Practical tips for Perth business owners and team members who want to perform confidently in business video.",
        "content": """
    <p>Most business owners are not natural on-camera performers &mdash; and that is completely normal. The ability to look relaxed, speak clearly, and connect with a camera lens is a skill that can be learned and improved, and a small amount of preparation and awareness goes a long way. Whether you are filming a founder story, a product demo, or a testimonial series, these practical tips will improve your on-camera performance immediately.</p>

    <h2>Before the Camera Turns On</h2>

    <p>Preparation is the biggest single contributor to on-camera confidence. Know your key points, but do not memorise a script word for word &mdash; memorised scripts produce wooden, unnatural delivery. Instead, know the three to five things you need to communicate and trust yourself to find the words on the day. If you are reading from a teleprompter, rehearse the script aloud at least twice before the shoot so the words feel familiar and natural when you deliver them on camera.</p>

    <p>Wardrobe decisions should be made the day before, not on the morning of the shoot. Solid colours film better than patterns or fine stripes. Navy, teal, burgundy, and forest green all look excellent on camera. Avoid pure white (overexposes and draws the eye away from your face), pure black (flattens detail in the torso area), and fine horizontal stripes (create a strobing moire effect on screen). Wear something you are genuinely comfortable in &mdash; physical discomfort creates visible tension on camera.</p>

    <h2>During the Shoot</h2>

    <ul>
      <li>Look at the lens, not the screen &mdash; connecting with the lens is connecting with the viewer; the screen is not your audience</li>
      <li>Speak slightly more slowly than feels natural &mdash; adrenaline speeds up delivery; the edit pace will feel right at a slightly slower-than-comfortable speech rate</li>
      <li>Energy matters: your delivery on camera needs to be approximately 20% more animated than feels comfortable &mdash; the camera absorbs energy and the screen returns less than was delivered</li>
      <li>If you stumble over a line, pause, take a breath, and restart the sentence from the beginning &mdash; do not apologise, just reset; the editor will use the clean take</li>
      <li>Posture: sit or stand slightly forward, with your weight distributed evenly; slumping signals discomfort and reads poorly on screen</li>
    </ul>

    <h2>Managing Nerves</h2>

    <p>Camera nervousness is extremely common among business owners who are excellent at their work but unaccustomed to being filmed. The most effective technique for managing it is to shift your mental frame: instead of thinking &ldquo;I am being filmed,&rdquo; think &ldquo;I am talking to one person who has a specific problem I can help with.&rdquo; Every video has a specific ideal viewer. Speak directly to that person. The nervousness of performance disappears when you are genuinely trying to help someone &mdash; and that intention comes through on screen in a way that is more compelling than any amount of polished delivery.</p>
""",
    },
    {
        "slug": "blog-perth-startup-video-marketing",
        "title": "Video Marketing for Perth Startups &mdash; Where to Begin",
        "tag": "Strategy",
        "read_time": 4,
        "meta": "Perth startups with limited budgets can still build powerful video marketing strategies. Here's where to start and what to prioritise at each stage of growth.",
        "content": """
    <p>Video marketing for startups requires a different strategic approach than established businesses. Budget is constrained, the brand identity is still forming, and the priority is speed-to-learning rather than polished production. The goal for a Perth startup's early video strategy is not to produce the perfect brand film &mdash; it is to start building audience, testing messaging, and learning what resonates with your target market as cheaply and quickly as possible.</p>

    <h2>Pre-Revenue: Minimum Viable Video</h2>

    <p>Before you have revenue to invest in professional production, your phone is your studio. Perth startups in this stage should focus entirely on authenticity and consistency rather than production quality. A founder speaking directly to camera about the problem they are solving, the journey they are on, and the people they are trying to serve is compelling content &mdash; and it is content that polished corporate video cannot replicate. Authenticity is a genuine competitive advantage for early-stage businesses, and a smartphone captures it perfectly well.</p>

    <p>The content to prioritise at this stage: founder story (why you are building this, what problem you personally experienced), build-in-public updates (share the journey, the challenges, the milestones), educational content about the problem space you are addressing (positions you as a knowledgeable founder before the product exists), and customer discovery interviews shared with permission (shows you are listening and validates demand).</p>

    <h2>Early Revenue: First Professional Investment</h2>

    <p>When the first professional video budget becomes available, the priority should be a product or service explainer and a founder brand story. These two pieces anchor your website, give your sales conversations a shareable asset, and give potential investors and partners a fast way to understand what you are building. Budget $1,500&ndash;$3,500 for both, professionally produced by a Perth video editor experienced in startup and tech content.</p>

    <ul>
      <li>A well-produced 90-second explainer on your homepage will immediately improve conversion rates for paid traffic campaigns</li>
      <li>A founder story video gives you a human credibility piece for LinkedIn, pitch decks, and media outreach</li>
      <li>Continue DIY social content alongside professional hero pieces &mdash; the combination of authentic daily content and polished anchor pieces is more effective than either alone</li>
      <li>Perth startup community events (Spacecubed, Curtin University startup programs, Unearthed) are excellent filming opportunities; capture testimonials and event content at every appearance</li>
    </ul>

    <h2>Growth Stage: Building a Content Engine</h2>

    <p>At the growth stage, video should become a systematic part of your marketing operations rather than a series of one-off productions. This means a content calendar, a regular production schedule, an analytics review process, and a clear attribution framework for video-driven leads. The transition from tactical video production to strategic content engine is where Perth startups with strong early video foundations begin to compound their advantage over competitors who have not invested in the same foundation.</p>
""",
    },
    {
        "slug": "blog-video-editing-software-perth-business",
        "title": "Which Video Editing Software Is Right for Your Perth Business?",
        "tag": "Production",
        "read_time": 4,
        "meta": "There are more video editing options than ever in 2025. Here's a practical comparison of the main tools for Perth businesses handling their own video editing.",
        "content": """
    <p>Choosing video editing software is one of the first decisions Perth businesses face when starting to produce their own content. The options range from free mobile apps to professional-grade desktop platforms, and the right choice depends on your content type, technical comfort level, and how much time you are willing to invest in learning a new tool. Here is a practical breakdown of the main options available in 2025.</p>

    <h2>Free Options That Are Genuinely Useful</h2>

    <p><strong>CapCut</strong> (free, iOS, Android, desktop) is the strongest free editing option for short-form social content. Its auto-caption tool, built-in trending audio library, and aspect ratio conversion features are directly purpose-built for Instagram Reels and TikTok. The learning curve is minimal &mdash; most first-time users produce publishable content within their first hour. Limitations: basic colour tools, no multi-track audio mixing, not suitable for long-form or complex productions.</p>

    <p><strong>DaVinci Resolve</strong> (free desktop version, Mac, Windows, Linux) is the most powerful free video editing tool available &mdash; it is the same software used by professional film and television colourists worldwide. The free version has no meaningful capability limitations compared to the paid Studio version for most business use cases. The trade-off is a steep learning curve: a beginner should budget 10&ndash;15 hours of tutorial time before they are productive in Resolve. If you are willing to invest in learning, DaVinci Resolve is the best long-term free option available.</p>

    <h2>Paid Options Worth Considering</h2>

    <p><strong>Adobe Premiere Pro</strong> (approximately $60/month, or $85/month for Creative Cloud) is the industry standard for professional video production. If your business already uses Adobe Creative Cloud (Photoshop, Illustrator, InDesign), Premiere Pro is the natural addition. Its integration with After Effects (motion graphics), Audition (audio mixing), and Media Encoder (export) creates a powerful creative suite. The monthly cost is justified when Premiere is used regularly; harder to justify for occasional editing.</p>

    <ul>
      <li><strong>Final Cut Pro</strong> ($599 one-time, Mac only): excellent for Mac-based businesses that prioritise editing speed and have no need for cross-platform compatibility; highly optimised for Apple Silicon chips</li>
      <li><strong>Adobe Premiere Rush</strong> ($10/month): simplified Premiere for mobile-first workflows; good for social content when CapCut is insufficient but full Premiere is excessive</li>
      <li><strong>Descript</strong> ($12&ndash;$24/month): uniquely useful for talking-head and interview content; edits video by editing the transcript text; excellent for businesses producing podcast-style or interview content regularly</li>
    </ul>

    <h2>The Practical Recommendation</h2>

    <p>Start with CapCut for short-form social content &mdash; free, fast, and produces professional results for its content category. If you want to develop professional editing skills for longer-form content, invest the time to learn DaVinci Resolve (free). If you are already in the Adobe ecosystem or are producing content professionally enough to justify the subscription, Premiere Pro is the natural professional choice. Resist the temptation to buy expensive software before you have established the habit of regular editing &mdash; the best software is the one you will actually use consistently.</p>
""",
    },
    {
        "slug": "blog-construction-tradie-video-perth",
        "title": "Video Marketing for Perth Construction and Building Businesses",
        "tag": "Industry",
        "read_time": 4,
        "meta": "Perth construction companies and builders are using video to win more tenders and generate more enquiries. Here's a practical video strategy for building businesses.",
        "content": """
    <p>Perth's construction industry is one of the most active in the country, driven by strong population growth, infrastructure investment, and the ongoing demand for residential and commercial building. In this competitive environment, construction businesses that use video to demonstrate their work, build credibility, and establish project portfolio visibility are consistently winning tenders and enquiries over competitors with equal capabilities but no visual evidence of them. Here is how Perth construction and building businesses can use video effectively.</p>

    <h2>The Project Documentation Opportunity</h2>

    <p>Construction businesses generate extraordinary visual content as a byproduct of their normal operations. Every project involves a transformation from blank site or dilapidated structure to finished, quality construction. Documenting that transformation &mdash; from site establishment through structure, skin, fit-out, and practical completion &mdash; is the most authentic and compelling portfolio content a construction business can produce. And most of it can be captured on a smartphone by someone who is already on site every day.</p>

    <p>A time-lapse of a project from slab pour to completion, compressed into 60 seconds, is one of the most shareable and impressive pieces of content a Perth builder can publish. It communicates scale, capability, and pace in a single video. Monthly progress documentation of a major project &mdash; published as a series on YouTube or LinkedIn &mdash; builds anticipation and demonstrates project management quality to potential tender clients who are watching over time.</p>

    <h2>Content for Different Construction Audiences</h2>

    <p>Construction businesses typically have multiple distinct audiences, each requiring different video content: residential clients need to see finished project quality, team approachability, and process transparency; commercial and government clients need to see project scale, HSE practices, and subcontractor management quality; architect and developer partners need to see construction methodology, problem-solving capability, and collaboration approach.</p>

    <ul>
      <li>Finished project showcase videos (2&ndash;3 minutes, cinematic quality) for website portfolio and award submissions</li>
      <li>Project progress updates for LinkedIn &mdash; targets commercial clients and project partners who are researching capability</li>
      <li>Safety culture and quality management content demonstrates HSE commitment for tender evaluation processes</li>
      <li>Team and culture content attracts skilled tradespeople and project managers in a tight labour market</li>
      <li>Client testimonial video from completed project handovers &mdash; film immediately after practical completion when satisfaction is highest</li>
    </ul>

    <h2>The Tender and Proposal Advantage</h2>

    <p>A polished project portfolio video included in a tender response or capability statement is a genuine differentiator in Perth's construction market. Most tender submissions are document-heavy and text-dense; a two-minute video that takes the evaluator on a visual tour of your best recent work stands out immediately. Brief your estimating team to include a video link (YouTube or Vimeo) in every significant tender response. Track which opportunities result in shortlisting and whether video-supported submissions outperform text-only responses &mdash; most Perth construction businesses that start doing this find the correlation significant.</p>
""",
    },
]

DRAFTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "drafts")
os.makedirs(DRAFTS_DIR, exist_ok=True)

for a in ARTICLES:
    slug = a["slug"]
    title = a["title"]
    meta = a["meta"]
    tag = a["tag"]
    read_time = a["read_time"]
    content = a["content"]

    html = make_head(slug, title, meta, tag, read_time) + content + make_foot()

    out_path = os.path.join(DRAFTS_DIR, f"{a['slug']}.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated: drafts/{slug}.html")

print(f"\nDone — {len(ARTICLES)} draft blog posts generated.")
