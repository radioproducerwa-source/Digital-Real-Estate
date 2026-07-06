#!/usr/bin/env python3
"""Generate 30 new draft blog posts for Perth MC and append them to the queue."""

import json
import os

DRAFTS_DIR = os.path.join(os.path.dirname(__file__), "drafts")
QUEUE_FILE = os.path.join(DRAFTS_DIR, "queue.json")

POSTS = [
    {
        "slug": "mc-for-hybrid-virtual-events-perth",
        "title": "MC for Hybrid and Virtual Events in Perth",
        "tag": "Corporate",
        "read_time": 6,
        "excerpt": "Hosting a hybrid event — part live, part virtual — creates unique challenges for any MC. What works for in-room audiences often falls flat on screen, and vice versa.",
        "description": "How Perth MCs adapt their hosting style for hybrid and virtual events — audience engagement, camera presence, and keeping both rooms connected.",
        "body": """<p>Hybrid events — where some guests attend in person and others join online — have become a permanent fixture in Perth's corporate calendar. Managing both audiences simultaneously is one of the most technically demanding things an MC can do.</p>
<h2>The Two-Audience Challenge</h2>
<p>In a hybrid event, you're effectively hosting two separate experiences at once. In-room guests need energy, eye contact, and physical presence. Virtual attendees need the MC to acknowledge the camera, speak at a measured pace, and provide context for anything visual that's happening on stage. Ignoring either audience for too long causes both to disengage.</p>
<h2>Camera Technique for MCs</h2>
<p>Unlike presenting to a room, addressing a camera requires a different kind of focus. Look directly into the lens when speaking to virtual attendees — not at the monitor beside it. Keep energy slightly higher than feels natural; screens flatten performance. Brief pauses that feel natural in a room often feel like dead air on a stream.</p>
<h2>Transitions That Work for Both</h2>
<p>Every transition needs to be explicitly announced for virtual attendees, who can't read the room the same way. "We're now moving to our next session — for those joining online, we'll be sharing the slides on screen now" keeps remote guests oriented. Develop a habit of narrating action as well as announcing it.</p>
<h2>Technical Briefing Is Non-Negotiable</h2>
<p>Before any hybrid event, an MC should walk through the full technical setup: which cameras are live when, how audience questions from virtual attendees will be received, what the signal is when a virtual speaker is ready, and what happens if the stream drops. Improvising these decisions under pressure, mid-event, costs time and credibility.</p>
<h2>Engaging the Virtual Room</h2>
<p>Virtual attendees disengage faster than in-room guests. Building in deliberate virtual touchpoints — polling, Q&A segments, shoutouts to people watching — keeps remote participation active. An experienced MC treats the virtual room as a co-equal part of the event, not an afterthought.</p>
<h2>Perth's Hybrid Event Landscape</h2>
<p>Perth's geographic isolation has accelerated hybrid event adoption — interstate and international attendees are increasingly joining virtually rather than flying in. An MC who's comfortable in the hybrid format adds genuine value to Perth organisations running national or international-facing events.</p>"""
    },
    {
        "slug": "mc-retirement-party-perth",
        "title": "MC for a Retirement Party in Perth — Making It Memorable",
        "tag": "Events",
        "read_time": 5,
        "excerpt": "Retirement parties honour a career's worth of contribution. Getting the program structure right — stories, tributes, roast-friendly humour — makes the difference between memorable and forgettable.",
        "description": "How to structure a retirement party program in Perth, including tributes, roast moments, and how an MC keeps the celebration on track.",
        "body": """<p>A retirement party is a celebration of a career, a life chapter, and the people who shaped it. It's also, very often, the highest-pressure event a workplace has hosted all year. An MC brings structure, warmth, and the discipline to keep tributes focused.</p>
<h2>The Structure of a Great Retirement Celebration</h2>
<p>The most effective retirement party programs move through three emotional arcs: celebration of the past (career highlights, achievements, formative moments), connection to people (colleagues, family, shared memories), and excitement for what's next. An MC's job is to hold that arc across the evening without letting any single section run too long.</p>
<h2>Managing the Tribute Speakers</h2>
<p>Well-meaning colleagues often speak too long. Brief every speaker before the event with a hard time limit — three minutes is usually right — and agree on a gentle signal for when they're approaching it. An MC who can gracefully redirect an overrunning speaker saves the room from the collective discomfort of watching someone unable to wrap up.</p>
<h2>The Roast Question</h2>
<p>Retirement parties often include roast-style humour — gentle teasing of the retiree's quirks, habits, and legendary stories. Done well, it's the highlight of the night. Done poorly, it alienates the retiree or goes too far. An experienced MC sets the tone for what's appropriate, and can intervene if it tips over. The guest of honour should always be in on the joke.</p>
<h2>Involving Family</h2>
<p>If the retiree's family is present, deliberately including them in the program — a few words from a partner, a tribute from a child — deepens the emotional resonance of the evening. Coordinate this in advance and give family members the same briefing that speakers get.</p>
<h2>Closing on a High</h2>
<p>The final moment should be the guest of honour speaking — sharing gratitude, stories, or whatever feels right. The MC's job is to set that up with enough warmth that the retiree can step into a room that's genuinely with them. Don't rush the close. This is the moment the whole evening was building to.</p>"""
    },
    {
        "slug": "mc-for-boat-cruise-perth",
        "title": "MC for a Boat Cruise Event in Perth",
        "tag": "Events",
        "read_time": 5,
        "excerpt": "Perth's Swan River and harbour make boat cruises a popular corporate and social event format. Hosting on water requires a different set of MC skills than a ballroom.",
        "description": "What makes hosting a boat cruise event different — and how an experienced Perth MC handles acoustics, movement, and the unique energy of events on water.",
        "body": """<p>Perth's location on the Swan River and its proximity to the harbour make boat cruises a genuinely compelling event format — and one with a distinct set of challenges for anyone at the microphone.</p>
<h2>Acoustics and PA on the Water</h2>
<p>Sound on a vessel behaves unpredictably. Engine noise, wind, and the shape of a boat's interior can create dead spots, feedback, and intelligibility problems that wouldn't exist in a fixed venue. Before any boat cruise event, an experienced MC does a full PA walkthrough with the vessel's crew or the hired AV team, identifies problem zones, and establishes a fallback if technical issues arise mid-cruise.</p>
<h2>Movement and Audience Location</h2>
<p>Unlike a ballroom, guests on a boat cruise move. They're on the deck, at the bar, at tables inside — the MC can't rely on a single fixed audience position. Programming structured elements (speeches, presentations, key announcements) during moments when guests are naturally gathered — departing the dock, at sunset, over a seated course — makes a significant difference to engagement.</p>
<h2>Weather Contingencies</h2>
<p>Perth's weather is generally kind, but the Swan River and Fremantle waters can be unpredictable. An MC should know the vessel's weather policy, the indoor fallback if guests need to move inside, and how to manage a program shift mid-event without it feeling like a problem. Framing contingencies as part of the adventure keeps the mood buoyant.</p>
<h2>Timing Around Scenery</h2>
<p>The venue itself is part of the experience. Acknowledge it. Build moments in the program around the city skyline, the river passage, or the sunset. An MC who ignores the setting and treats the cruise like any other ballroom event misses what makes a boat cruise special.</p>
<h2>Suitability for Boat Cruise Events</h2>
<p>Corporate Christmas parties, end-of-year celebrations, milestone birthdays, and private social gatherings all work well in the cruise format. The program needs to be lighter and more flexible than a fixed-venue event — but that flexibility, managed by an experienced MC, is what makes boat cruises so enjoyable.</p>"""
    },
    {
        "slug": "mc-for-garden-wedding-perth",
        "title": "MC for a Garden Wedding in Perth",
        "tag": "Weddings",
        "read_time": 5,
        "excerpt": "Garden weddings in Perth are spectacular — and they require an MC who knows how to manage open-air acoustics, natural light, and the unexpected.",
        "description": "What to know before booking an MC for a Perth garden wedding — outdoor acoustics, weather planning, and keeping the program flowing in an open-air setting.",
        "body": """<p>Perth's climate makes garden weddings genuinely beautiful — and genuinely unpredictable. An experienced MC brings structure to the outdoor setting without dampening the relaxed atmosphere that makes a garden wedding worth having.</p>
<h2>Outdoor Acoustics</h2>
<p>Sound outdoors disperses differently than in a venue. A PA system that sounds fine in a room may need significantly more power — or more carefully placed speakers — to carry across a garden. Before confirming any garden wedding MC, check that they've worked in outdoor settings and understand the importance of an early sound check. Without adequate amplification, speeches simply can't be heard, which diminishes one of the reception's core elements.</p>
<h2>Wind and Ambient Noise</h2>
<p>Even a gentle breeze creates microphone handling challenges. An experienced MC knows to position themselves — and to position a handheld mic relative to their face — to minimise wind noise. They'll also brief speech-givers on mic technique before the program starts.</p>
<h2>Light and Visibility</h2>
<p>Late afternoon sun, changing light as evening approaches, and the transition from natural to artificial lighting all affect how a garden wedding looks and feels. An MC who acknowledges the light — comments on the sunset, adjusts the energy as the day shifts to evening — works with the setting rather than against it.</p>
<h2>Weather Contingency Planning</h2>
<p>Every Perth garden wedding needs a wet weather plan. The MC should be briefed on it: where guests move, how the program changes, what the MC announces and when. Coordinating the contingency calmly and quickly, without alarming guests, is part of what an experienced outdoor MC does.</p>
<h2>Perth's Garden Wedding Venues</h2>
<p>Popular garden wedding locations in Perth include properties in the Swan Valley, Margaret River event spaces, properties in the Hills, and private estate venues across the metro area. Each has different acoustics, guest flow, and program constraints. An MC who knows the venue — or makes a point of visiting it before the day — will always perform better than one walking in cold.</p>"""
    },
    {
        "slug": "mc-for-micro-wedding-perth",
        "title": "MC for a Micro Wedding in Perth",
        "tag": "Weddings",
        "read_time": 5,
        "excerpt": "Micro weddings — 20 to 50 guests — are intimate by design. An MC for a micro wedding needs a completely different energy to one hosting a 200-person reception.",
        "description": "How an MC adapts their style for a Perth micro wedding — intimate hosting, personalised program, and making a small guest list feel like the perfect size.",
        "body": """<p>Micro weddings have become a genuine first choice — not a compromise — for many Perth couples. Twenty to fifty guests, a carefully curated venue, and a program built around connection rather than scale. The MC role in a micro wedding is different in every meaningful way.</p>
<h2>Intimacy Over Performance</h2>
<p>At a micro wedding, the MC is essentially hosting dinner for close friends and family. The style should reflect that. Large-room projection, theatrical energy, and the kind of announcements designed to carry to a back table 20 metres away all feel wrong in a room where everyone can hear a normal voice. The best micro wedding MCs shift into a conversational, warm register that matches the setting.</p>
<h2>Personalised at Every Turn</h2>
<p>With a small guest list, an MC has the opportunity — and the obligation — to know the room. Every guest is likely to know the couple well. Generic content, borrowed lines, and impersonal program segments are more obvious and more jarring at a micro wedding than at a large reception. A thorough pre-wedding briefing with the couple is non-negotiable.</p>
<h2>Program Structure at Micro Scale</h2>
<p>Micro weddings typically have fewer formal program elements: no bridal party introductions, no table-by-table acknowledgements, no mass coordination of 15 tables. This creates freedom, but also requires MC judgment about what actually needs formal structure and what can be left organic.</p>
<h2>Speech Management</h2>
<p>At a micro wedding, every guest knows who's speaking. There's less pressure to introduce speakers with biographical detail — the room already knows them. The MC's role in speech transitions is lighter: gentle framing, smooth handoffs, and a warm reception for each speaker.</p>
<h2>Why Micro Weddings Still Need a Professional MC</h2>
<p>Some couples assume a micro wedding is small enough to self-manage. The opposite is true: in a small, intimate setting, an awkward pause or a program that stalls is immediately obvious to everyone. A professional MC who matches their energy to the scale of the event makes a micro wedding feel exactly as it should — effortlessly perfect.</p>"""
    },
    {
        "slug": "mc-for-sports-club-presentation-perth",
        "title": "MC for a Sports Club Presentation Night in Perth",
        "tag": "Events",
        "read_time": 5,
        "excerpt": "Sports club presentation nights are a fixture of Perth's community calendar — and they benefit enormously from a professional MC who understands the culture.",
        "description": "How to get the most out of a Perth sports club presentation night with a professional MC — award pacing, roast content, and keeping the evening running to time.",
        "body": """<p>Sports club presentation nights are among the most high-energy — and least formal — event formats an MC will work. The crowd is passionate, opinionated, and almost certainly there for a big night. Getting it right requires reading the room well from the opening welcome.</p>
<h2>Know the Culture First</h2>
<p>Every sports club has its own culture, traditions, and running gags. A football club is different from a tennis club, a surf club different again from a cricket association. Before taking on any sports presentation night, a professional MC invests time in understanding the club: its history, its personalities, its in-jokes, its award traditions. Nothing kills a sports club room faster than an MC who's clearly phoning it in with generic content.</p>
<h2>Award Pacing and Volume</h2>
<p>Presentation nights typically have a large number of awards — best and fairest, most improved, coaches' award, best rookie, club person of the year, and often player-voted awards across every grade. Moving through them at pace is essential. Each presentation should take 2–3 minutes maximum. An MC who lets every winner run long will have a restless room by the midpoint of the program.</p>
<h2>Roast-Style Humour</h2>
<p>The roast element of a sports club presentation — affectionate ribbing of players, coaches, and committee members — is usually expected and appreciated. The MC sets the tone: warm, self-aware, never punching down. The best lines celebrate the club's year while acknowledging the characters who made it what it was.</p>
<h2>Managing the Bar and Energy</h2>
<p>By the time formal proceedings start at a presentation night, the room has usually been at the bar for a while. An experienced MC builds that energy rather than fighting it. Start with something that acknowledges the crowd, get the room settled quickly, and keep the program moving. Long, earnest speeches are death at a sports club night.</p>
<h2>Ending on the High Note</h2>
<p>Close the formal program before the energy peaks and tips over. Leave guests wanting more of the celebration, not relieved that the formalities are done. The last award should land with maximum excitement, and the transition to the open part of the evening should feel like a reward.</p>"""
    },
    {
        "slug": "mc-for-corporate-breakfast-perth",
        "title": "MC for a Corporate Breakfast Event in Perth",
        "tag": "Corporate",
        "read_time": 5,
        "excerpt": "Corporate breakfast events demand a different MC skill set — early starts, sharp time management, and an audience that needs to be fully engaged before the coffee has kicked in.",
        "description": "What makes a corporate breakfast event unique for an MC — energy at 7am, tight time management, and how to open a room of pre-caffeinated professionals.",
        "body": """<p>Corporate breakfast events are popular in Perth's business community — networking breakfasts, industry briefings, keynote mornings, and leadership forums all run in the 7am to 9:30am window. For an MC, it's the most technically demanding time of day to work.</p>
<h2>Energy Management at Dawn</h2>
<p>Guests at a breakfast event are typically not yet fully awake, which means the MC's opening energy sets the room's energy for the entire program. Coming in too loud and theatrical feels jarring. Coming in flat and low-key leaves guests firmly in their own heads. The sweet spot is purposeful and warm — professional, but human.</p>
<h2>Time Is the Non-Negotiable</h2>
<p>Business breakfast guests have morning commitments. They know the event ends at 9:30, and they've planned their day around it. An MC who lets a breakfast event run long doesn't get the same latitude as one at a gala dinner. Strict adherence to the program, assertive management of speaker time, and a clean close at the advertised time is the baseline expectation.</p>
<h2>Program Structure That Works</h2>
<p>Effective corporate breakfast programs minimise standing up and sitting down. Welcome, housekeeping, and introduction — then straight into the content. Networking works better at the end than at the start: most guests arrive at different times, and forced networking before coffee has been consumed is rarely productive.</p>
<h2>Microphone and Technical Setup</h2>
<p>Breakfast venues often have more ambient noise than evening event spaces — coffee service, clattering crockery, passing foot traffic. An MC needs to establish audio early and clearly, and be ready to cut through the noise when announcing transitions or speaker introductions.</p>
<h2>The Value of a Breakfast MC</h2>
<p>Smaller business events sometimes dispense with a dedicated MC, asking a committee member or speaker to double as host. At a breakfast event, where energy and time management are critical and the window is tight, a professional MC pays for themselves in a program that runs crisply and a room that's engaged throughout.</p>"""
    },
    {
        "slug": "mc-for-graduation-ceremony-perth",
        "title": "MC for a Graduation Ceremony in Perth",
        "tag": "Events",
        "read_time": 5,
        "excerpt": "Graduation ceremonies are among the most formal and protocol-driven events an MC will host — but they can still be warm, engaging, and memorable.",
        "description": "How a professional MC approaches Perth graduation ceremonies — name calling, protocol, managing long program lists, and keeping families engaged throughout.",
        "body": """<p>Graduation ceremonies are a once-in-a-degree moment for graduates and their families. They're also, structurally, among the most demanding events an MC hosts: long lists of names, rigid protocol, and audiences whose attention fades across a two-hour ceremony.</p>
<h2>Protocol First</h2>
<p>Graduation ceremonies have formal structure — the order of procession, the role of the presiding officer, when to stand and when to sit, how awards and degrees are conferred. A professional MC learns the institution's specific protocols in advance and can brief guests on what to expect before the ceremony begins. Deviating from protocol, even accidentally, can disrupt a carefully choreographed event.</p>
<h2>Name Calling and Pronunciation</h2>
<p>Calling graduate names is the most technically demanding part of a graduation MC's role. A list of 300 names, many from diverse cultural backgrounds, must be pronounced accurately and confidently. The standard approach: receive the name list in advance, flag names that need phonetic guidance, and confirm pronunciation with faculty or with graduates directly. Mispronouncing a graduate's name at their graduation is a memorable failure.</p>
<h2>Keeping Families Engaged</h2>
<p>Families attending a graduation are there for one or two moments — when their person walks across the stage. In between, they're waiting. An MC who can hold a room warmly through long name lists, brief the audience on upcoming sections, and acknowledge the significance of the occasion provides genuine value to both the institution and the attendees.</p>
<h2>Managing a Long Program</h2>
<p>Many graduation ceremonies run two hours or longer. The MC should have a clear brief on every element: award presentations, honorary degrees, keynote address, institutional acknowledgements, and any musical elements. Understanding the program architecture allows confident navigation when things run over.</p>
<h2>The Tone Balance</h2>
<p>Graduation ceremonies are formal enough to require composure but joyful enough that they shouldn't feel stiff. A professional MC finds the register that honours the occasion — measured and clear in delivery, warm in acknowledgement, and able to hold a large audience through what is genuinely a significant life event.</p>"""
    },
    {
        "slug": "mc-for-themed-party-perth",
        "title": "MC for a Themed Party in Perth",
        "tag": "Events",
        "read_time": 5,
        "excerpt": "Themed events — from Great Gatsby galas to 80s nights to masquerade balls — succeed or fail on how completely the theme is committed to. A great MC makes the theme live.",
        "description": "How a professional MC enhances a Perth themed party — committing to the aesthetic, adapting hosting style, and making the theme part of every announcement.",
        "body": """<p>Themed events work when everyone — guests, venue, entertainment, and the MC — commits to the aesthetic. A half-hearted MC who stands at the front in ordinary clothes making generic announcements breaks the spell a themed event is designed to cast.</p>
<h2>Committing to the Theme</h2>
<p>An MC at a themed event is a character within it. Whether the event is a 1920s Gatsby night, a masquerade ball, a Hollywood red carpet, or a tropical luau, the MC's presentation, language, and energy should reflect the theme. This includes attire, vocabulary, and the way transitions and announcements are framed. "Ladies and gentlemen" becomes something else at a pirate-themed corporate party.</p>
<h2>Script Adaptation</h2>
<p>The MC's script — including welcomes, transitions, and program announcements — can be adapted for the theme without becoming a distraction. Brief character flourishes, period-appropriate language, or themed framing for segments all deepen the experience. The test: does the theme feel richer because the MC is in it, or does it feel forced?</p>
<h2>Keeping the Program Running</h2>
<p>The most important role of an MC at a themed event is the same as at any other event: keeping the program on time, transitions smooth, and the energy managed. Themed content should enhance that function, not replace it. An MC who loses the program because they're too focused on the character work fails the event.</p>
<h2>Types of Themed Events in Perth</h2>
<p>Corporate themed events in Perth span a wide range — end-of-year parties, gala fundraisers, networking nights, client entertainment events, and private celebrations. The MC brief varies significantly depending on the formality of the program within the theme. A fundraiser gala with a Venetian theme still needs serious auction management; a corporate 80s Christmas party is purely entertainment.</p>
<h2>Working with Event Stylists</h2>
<p>When events are designed by a professional event stylist or production company, the MC should receive a creative brief covering the aesthetic, the colour palette, the intended guest experience, and any specific moments where the MC's positioning within the theme matters. Alignment between the MC and the creative team produces a significantly more coherent event.</p>"""
    },
    {
        "slug": "last-minute-mc-booking-perth",
        "title": "Last-Minute MC Booking in Perth — What to Know",
        "tag": "Planning",
        "read_time": 5,
        "excerpt": "Sometimes you need an MC on short notice. What's possible, what to look for, and how to brief a late-booked MC so the event still runs perfectly.",
        "description": "A guide to booking a Perth MC on short notice — what's realistic, how to brief quickly, and what experienced MCs can deliver with limited preparation time.",
        "body": """<p>It happens: the MC you booked has a last-minute conflict, or the decision to hire a professional MC comes later in the planning process than it should. Last-minute bookings are possible, but they require a different approach to get the best outcome.</p>
<h2>What 'Last-Minute' Means in Practice</h2>
<p>For most Perth events, 'last-minute' means anything under four weeks out. At that point, calendar options narrow and the briefing window compresses. Under two weeks is tight but workable for an experienced MC. Under a week requires an MC who is highly experienced in quickly absorbing brief material — and a client who can provide it promptly.</p>
<h2>Why Experienced MCs Handle Late Bookings Better</h2>
<p>An experienced MC has a large bank of event knowledge, crowd-reading skills, and adaptability that allows them to perform well with less preparation time. A less experienced MC needs more lead time to build confidence and material. When time is short, experience matters more, not less.</p>
<h2>What You Need to Prepare Immediately</h2>
<p>To brief a late-booked MC effectively, you need: the event program and run sheet, names and pronunciations for all key personnel being introduced, specific moments requiring scripted content (toasts, award presentations), the venue details and AV setup, and any sensitivities to be aware of. The sooner this is compiled and sent, the better the result.</p>
<h2>What a Good Late Brief Looks Like</h2>
<p>A clear, single-document brief — even a well-structured email — is more useful than a scattered collection of messages. Include the timeline, the names, the key moments, and any preferences about tone or style. A professional MC will digest it quickly and confirm what they need before the event.</p>
<h2>Checking Availability</h2>
<p>Perth has a relatively small pool of professional MCs, and weekend dates fill quickly — especially in the October to April busy season. If you need a MC with less than a month's notice, move quickly. Contact multiple options and be transparent about your timeline. Most professional MCs appreciate honesty about the situation far more than vague enquiries that become urgent later.</p>"""
    },
    {
        "slug": "how-to-handle-drunk-guests-mc",
        "title": "How to Handle Drunk Guests as an MC",
        "tag": "Craft",
        "read_time": 5,
        "excerpt": "Every event MC will eventually face guests who've had too much to drink. How you handle it — and whether it becomes a moment or a problem — depends entirely on technique.",
        "description": "Practical MC techniques for managing intoxicated guests — staying calm, maintaining crowd respect, and handling disruptions without derailing the event.",
        "body": """<p>It's one of the situations no MC likes to anticipate but every experienced MC has navigated: a guest who's had too much to drink is becoming a distraction. How the MC handles it shapes how the rest of the room feels about the event.</p>
<h2>Prevention Is the First Layer</h2>
<p>Experienced MCs manage event energy proactively. Keeping the program moving, keeping structured segments focused, and building a clear rhythm that guests orient to reduces the window for disruption. The longer a program sits in unstructured downtime with open bar service, the greater the likelihood of issues.</p>
<h2>When It Becomes Visible</h2>
<p>If a guest becomes disruptive enough to affect the room — talking loudly during speeches, heckling, or drawing negative attention — the MC's first tool is not the microphone. Signal to the venue or event staff immediately; they're trained to manage this without creating a scene. The MC continues the program and redirects audience attention back to the stage.</p>
<h2>Direct Mic Response (When Necessary)</h2>
<p>If venue staff aren't available and the disruption is escalating, a brief, warm, non-confrontational acknowledgement from the microphone can reset the room. "We'll save the commentary for the bar later" — said with a smile and light tone — signals to the room that the MC is in control without escalating the situation. Never match the energy of a disruptive guest; always stay lighter and more composed.</p>
<h2>After the Moment</h2>
<p>Once a disruption has been managed — whether by staff or by the MC — the most important thing is an immediate return to normal programming. Don't dwell on it, reference it, or let it become the story of the evening. Move forward with energy and purpose, and the room will follow.</p>
<h2>Protecting the Event's Tone</h2>
<p>The MC's authority in the room comes from consistent composure. Guests read the MC's body language and energy throughout the event. An MC who handles difficulty smoothly and maintains warmth and control throughout earns genuine trust from the crowd — which makes every other aspect of the event work better.</p>"""
    },
    {
        "slug": "mc-contracts-what-to-look-for",
        "title": "MC Contracts — What to Look for Before You Sign",
        "tag": "Planning",
        "read_time": 5,
        "excerpt": "Booking an MC without a proper contract leaves both parties exposed. Here's what every MC agreement should include — and the clauses that matter most.",
        "description": "A guide to MC contracts for event organisers — deposit terms, cancellation clauses, rider requirements, and what to check before signing.",
        "body": """<p>A professional MC booking should always be accompanied by a written agreement. Understanding what to look for protects both the event organiser and the MC — and avoids misunderstandings that are costly and difficult to resolve once an event has passed.</p>
<h2>The Essential Elements</h2>
<p>Every MC contract should include: the event date, start and end times, venue address, the agreed fee, payment terms (deposit amount, balance due date, payment method), and a clear description of what the MC's engagement covers — hours of service, number of event elements, preparation time included.</p>
<h2>Deposit and Payment Terms</h2>
<p>Most professional MCs require a deposit to secure a booking — typically 25% to 50% of the fee, paid on signing. The balance is usually due on or before the event date. Understand when payments are due and what payment methods are accepted before signing. Late payment provisions — if any — should be clearly stated.</p>
<h2>Cancellation Clauses</h2>
<p>What happens if you need to cancel? And what happens if the MC cancels? A fair contract specifies notice periods, whether the deposit is refundable at various stages, and what obligations the MC has if they cannot fulfil the booking. Read this section carefully — it's the most consequential if anything goes wrong.</p>
<h2>Rider and Requirements</h2>
<p>Some MCs include a rider — requirements for the performance environment. This might include a specific microphone type, a clear sightline to the program AV, a quiet space for briefing before the event, or refreshments. Know what you're agreeing to provide, and confirm it's achievable at your venue before signing.</p>
<h2>Scope of Service</h2>
<p>What is and isn't included in the fee? Is the MC available for venue walk-through and AV check? Does the fee cover a pre-event briefing call? Are script preparation and research included? Scope ambiguity causes friction. A well-written contract eliminates it.</p>"""
    },
    {
        "slug": "how-to-time-speeches-wedding",
        "title": "How to Time Speeches at a Wedding Reception",
        "tag": "Weddings",
        "read_time": 5,
        "excerpt": "Speech timing is one of the most common ways a wedding reception gets off track. Here's how to plan, brief, and execute the speeches segment without it running long.",
        "description": "A practical guide to timing wedding speeches — placement in the program, speaker briefing, time limits, and how an MC keeps everything on track.",
        "body": """<p>Wedding speeches are simultaneously the most personal and most unpredictable part of a reception program. A well-managed speeches segment is one of the highlights of the evening. An unmanaged one can cost 45 minutes and leave guests exhausted before the first dance.</p>
<h2>How Many Speeches Is Too Many?</h2>
<p>The answer depends on your guest count and program length, but a general guide: three to five speeches is ideal. More than five, and attention fades noticeably between them regardless of speaker quality. If the couple wants more people involved, consider a group toast rather than individual speeches.</p>
<h2>Where to Place Speeches in the Program</h2>
<p>The most effective placement for wedding speeches is after entrée or main course — not at the start of the reception, when guests are still arriving and settling, and not at the very end, when energy has ebbed. Some couples prefer speeches before the meal to get them done early; this works if the run time is kept tight.</p>
<h2>Briefing Speakers Beforehand</h2>
<p>Every wedding speaker should know their time limit before the event. Three to five minutes is right for most speeches — long enough to be meaningful, short enough to keep the room engaged. Ask speakers to time themselves in rehearsal. A gentle, specific briefing from the MC ("we're aiming for about four minutes each") delivered warmly is more effective than a vague instruction to "keep it short".</p>
<h2>The MC's Role During Speeches</h2>
<p>A professional MC introduces each speaker with a brief, warm framing — who they are, their relationship to the couple — then hands the microphone and steps back. During the speech, the MC watches the program clock and has a pre-agreed signal ready for speakers who need a gentle redirect. After each speech, the MC receives the mic, leads the toast, and transitions to the next speaker or program element.</p>
<h2>Managing Overruns</h2>
<p>Some speakers will run long despite briefing. The MC needs a subtle, pre-agreed signal — often simply stepping toward the stage — that communicates 'wrap up' without publicly embarrassing the speaker. Most speakers respond well to a gentle cue. An experienced MC never interrupts a speech mid-sentence unless the situation is genuinely problematic.</p>"""
    },
    {
        "slug": "audience-participation-corporate-events",
        "title": "Audience Participation at Corporate Events — Getting It Right",
        "tag": "Corporate",
        "read_time": 5,
        "excerpt": "Poorly executed audience participation is among the most cringe-inducing experiences at corporate events. Done well, it's the highlight everyone remembers.",
        "description": "How to design and facilitate audience participation at corporate events in Perth — what works, what backfires, and how an MC makes it land.",
        "body": """<p>Audience participation — polling, Q&A, group activities, or interactive segments — can be the most engaging element of a corporate event, or the most excruciating. The difference is almost entirely in the design and facilitation.</p>
<h2>The Risk of Forced Participation</h2>
<p>Nothing makes a corporate room close faster than participation that feels mandatory, embarrassing, or arbitrary. Activities designed to "get people involved" without a clear purpose signal to the audience that the program is being padded. The test: if you can't explain in one sentence why this participatory element makes the event better, it probably doesn't.</p>
<h2>Polling and Voting</h2>
<p>Live audience polling — via app-based tools, show of hands, or branded voting cards — works well when the question is genuinely interesting and the result is used in the program. "Show of hands: how many of you have experienced this?" before a keynote segment warms the room, creates a shared data point, and signals that the content is relevant to this specific audience.</p>
<h2>Q&A Sessions</h2>
<p>Open Q&A formats are the most common participatory element at corporate events — and the most vulnerable to awkward silences, long-winded questions, and the one attendee who uses the microphone to make a speech. An experienced MC manages Q&A by seeding questions in advance, having backup questions ready, keeping a hand signal with the roving mic handler, and setting a clear time limit per question.</p>
<h2>Group Activities</h2>
<p>For conferences and team events, structured group activities — table discussions, collaborative challenges, peer teaching moments — create engagement that a passive program cannot. These work best when they're time-boxed, outcomes-focused, and directly connected to the event theme. The MC's role is to set up the activity clearly, manage the time, and debrief in a way that captures the group's energy.</p>
<h2>Reading the Room</h2>
<p>The best participatory elements are those the MC reads the room into — sensing when an audience is ready to be engaged versus when they need to absorb content passively. Participation at the wrong moment, however well-designed, lands flat. Participation at the right moment, however simple, creates genuine energy.</p>"""
    },
    {
        "slug": "mc-cultural-sensitivity-perth",
        "title": "Cultural Sensitivity for MCs in Perth's Diverse Event Market",
        "tag": "Craft",
        "read_time": 6,
        "excerpt": "Perth's cultural diversity means MCs regularly work events where multiple cultural backgrounds are represented. What every professional MC needs to know.",
        "description": "How Perth MCs navigate cultural diversity at events — appropriate acknowledgements, avoiding assumptions, and creating inclusive programs for multicultural guest lists.",
        "body": """<p>Perth is one of Australia's most culturally diverse cities, with large communities from Southeast Asia, South Asia, East Asia, Europe, and the Middle East. A professional MC working in this market needs genuine cultural awareness — not just awareness of etiquette, but sensitivity to how events are shaped by cultural values.</p>
<h2>Research Before Every Event</h2>
<p>Cultural preparation starts with the briefing. For any event where the guest list includes significant representation from a specific cultural background, an experienced MC researches that community's event expectations: how welcome is delivered, how elders or senior figures are acknowledged, whether humour is appropriate and what kind, how family members are referenced. This isn't about performing cultural knowledge — it's about avoiding inadvertent offence.</p>
<h2>Acknowledgements and Honorifics</h2>
<p>Different cultural communities have different expectations around how people are addressed. Some expect formal honorifics (Dr, Professor, Reverend); others expect specific acknowledgement of community leadership. Confirm the naming and introduction conventions for VIPs and key guests before the event, and do not improvise honorifics under pressure.</p>
<h2>Religious Considerations</h2>
<p>Events that include religious communities — whether Christian, Muslim, Buddhist, Hindu, or Sikh, among others — may have specific program elements: prayers, blessings, or observances that the MC needs to introduce and frame appropriately. Understand what's expected, how to introduce it respectfully, and how to transition out of it in a way that maintains the atmosphere.</p>
<h2>Humour and Its Limits</h2>
<p>What's funny in one cultural context is offensive in another. An MC working a multicultural event should default to humour that's observational, warm, and targeted at universal experiences — not humour that relies on cultural stereotypes, no matter how benign the intent. When in doubt, leave it out.</p>
<h2>Language and Pace</h2>
<p>For events where some attendees may have English as a second language, adjust pace, reduce idiom, and avoid slang-heavy commentary. Clear, unhurried delivery benefits every attendee and ensures the program content lands as intended across the full room.</p>"""
    },
    {
        "slug": "how-mcs-work-with-photographers",
        "title": "How MCs Work with Photographers and Videographers",
        "tag": "Craft",
        "read_time": 5,
        "excerpt": "An experienced MC actively supports the photography and videography team — and it makes a measurable difference to the shots you get.",
        "description": "How professional MCs coordinate with event photographers and videographers to protect key shots, manage timing, and improve the visual record of any event.",
        "body": """<p>The photographer and the MC are both trying to capture the best version of an event's key moments. When they work together, both do their jobs better. When they don't, critical shots get missed and program timing gets disrupted.</p>
<h2>The Pre-Event Conversation</h2>
<p>A professional MC will seek out the lead photographer or videographer before the event begins. The goal: understand their shot list, identify the moments where they need the room positioned a specific way, and establish a signal for when they need a brief pause or repeat. This conversation takes five minutes and prevents problems that would otherwise surface mid-program.</p>
<h2>Positioning and Sightlines</h2>
<p>An MC who understands photography will naturally consider where guests are looking and how they're framed when announcing key moments. Positioning the couple, the award recipient, or the guest of honour in a way that gives the photographer a clear, well-lit sightline isn't difficult — but it requires awareness that the shot matters.</p>
<h2>Managing the First Dance and Key Moments</h2>
<p>At weddings, the first dance is one of the most photographed moments of the evening. An MC who introduces it and then immediately withdraws from the stage — rather than standing in the background of every shot — is serving the couple's interests. Similarly, managing guest positioning, ensuring the couple has space, and giving the photographers time to move into position before the music starts all contribute to better results.</p>
<h2>Awards and Presentations</h2>
<p>At corporate and gala events, award presentations are often the primary photography subject. Pausing the program for 30 seconds to allow the photographer to get the handshake shot, the winner receiving the trophy, and the group photograph isn't dead time — it's the event's visual record being made. An MC who rushes through presentations without considering the photography gets lower-quality event coverage.</p>
<h2>The Videography Specific</h2>
<p>For events being filmed, additional considerations apply. Speaking clearly and at a measured pace for audio capture, avoiding talking over music during transitions, and ensuring microphone handoffs are clean all contribute to a better final video. Confirm with the videographer before the event whether they need any specific adjustments.</p>"""
    },
    {
        "slug": "pre-event-mc-checklist",
        "title": "Pre-Event MC Checklist — What to Confirm Before Any Event",
        "tag": "Planning",
        "read_time": 5,
        "excerpt": "A professional MC's pre-event checklist — the confirmations, walk-throughs, and briefings that prevent problems from materialising during the event.",
        "description": "The complete pre-event checklist for professional MCs and event organisers — from AV walk-throughs to run sheet confirmation and last-minute briefings.",
        "body": """<p>The work an MC does before the event is what makes the event itself feel effortless. Here's the pre-event checklist that separates professional event hosting from amateur hour.</p>
<h2>48 Hours Before</h2>
<p>Confirm the run sheet is finalised and in your possession. Verify all speaker names and pronunciations — email the organiser a list of any you're uncertain about. Confirm venue arrival time and parking. Read through the complete program, noting any segment that needs scripted material and any moment where you'll need to improvise around a scheduled element.</p>
<h2>The Day Before</h2>
<p>Brief call or message with the event organiser: confirm any last-minute changes, check if any speakers have dropped out or been added, confirm AV arrangements. Prepare your key materials: opening remarks, speaker introductions, transitions, and any specific scripted segments (toasts, award introductions). Print or load the run sheet in a format you can reference at the podium.</p>
<h2>On Arrival at the Venue</h2>
<p>Arrive early enough to do a full venue walk. Identify: the stage position, the AV control desk location, who you're working with on AV, where the microphone is and whether it needs a battery change, the stage stairs and whether they're well-lit, the entrance guests will come through, and any physical hazards or issues to be aware of. Do a sound check before any guest arrives.</p>
<h2>MC to Organiser Final Check</h2>
<p>Immediately before the event begins, do a final five-minute check with the event organiser. Any late changes? Any VIPs who've arrived who need specific acknowledgement? Any program adjustments? A brief, structured final check eliminates surprises that would otherwise surface during the event.</p>
<h2>The Mindset Before You Take the Stage</h2>
<p>In the final minutes before opening, run through your first 60 seconds. Know exactly how you're opening, what energy you're bringing in with, and what your first three sentences are. The opening sets the tone for everything that follows — a confident, well-prepared MC who steps up knowing exactly how they're starting creates immediate trust with the room.</p>"""
    },
    {
        "slug": "how-to-introduce-award-winners",
        "title": "How to Introduce Award Winners — A Guide for MCs",
        "tag": "Craft",
        "read_time": 5,
        "excerpt": "Award introductions are among the most formulaic — and most improvable — elements of any corporate or gala event. Here's how to make them land.",
        "description": "Techniques for introducing award winners at corporate events and galas — what to say, what to avoid, and how to build anticipation without losing the room.",
        "body": """<p>Award introductions are a craft. Done well, they build genuine anticipation and give winners a moment that feels like a proper celebration. Done poorly, they're a list of corporate titles that the room stops listening to after the second sentence.</p>
<h2>The Structure That Works</h2>
<p>A strong award introduction has three parts: context (what this award represents and why it matters), evidence (a brief, specific example of what the recipient did to earn it), and the reveal (their name — clearly, confidently, with a pause before it). Reversing the order — name first, then rationale — removes all the anticipation.</p>
<h2>What to Cut</h2>
<p>Cut job titles unless they're directly relevant to the award. Cut company history that the room already knows. Cut qualifications that aren't connected to the award criteria. A two-minute introduction that contains 90 seconds of filler teaches the room to stop listening. A 60-second introduction that's precisely relevant keeps them with you.</p>
<h2>The Reveal Moment</h2>
<p>The winner's name should land at the peak of the introduction — with a slight pause before it, spoken clearly and slightly slower than the preceding text, and at slightly higher volume. This is one moment where deliberate stagecraft serves the event. The room should feel the reveal, not just hear it.</p>
<h2>Working with Presenters</h2>
<p>At many awards events, the MC introduces the award category and then a guest presenter introduces the specific winner. Coordinate this clearly before the event: the MC introduces the presenter and the category, the presenter introduces the criteria and announces the winner. Overlap and duplication waste time and confuse the room.</p>
<h2>After the Acceptance Speech</h2>
<p>The MC receives the microphone, leads the applause warmly for a beat, transitions the winner off stage with a brief acknowledgement, and then cleanly introduces the next element. This transition — brief, warm, forward-moving — is what keeps the awards night's energy up across a long program of categories.</p>"""
    },
    {
        "slug": "mc-for-elopement-reception-perth",
        "title": "MC for an Elopement Reception in Perth",
        "tag": "Weddings",
        "read_time": 5,
        "excerpt": "Elopement receptions — intimate celebrations after a private ceremony — have a distinctive emotional register that requires a different MC approach than a traditional wedding.",
        "description": "How an MC creates the perfect atmosphere for a Perth elopement reception — intimate hosting, celebrating the couple's choice, and making a small gathering feel complete.",
        "body": """<p>Elopement receptions are growing in popularity in Perth — a private ceremony, often in a stunning location, followed by an intimate gathering of close family and friends. The reception program is smaller, the guest list tighter, and the emotional register entirely its own.</p>
<h2>Celebrating the Choice</h2>
<p>Couples who elope do so with intention. They've chosen a specific kind of experience — private, personal, on their own terms. An MC at an elopement reception should honour and celebrate that choice, not treat the event as a reduced version of a 'real wedding'. Frame the gathering as exactly what it is: a deliberate and beautiful decision by the couple.</p>
<h2>The Intimacy Advantage</h2>
<p>With 10 to 30 guests, an elopement reception allows for genuine personalisation that a 150-person wedding simply can't achieve. Stories, details, and moments that would be lost in a large room become the centrepiece. An MC with a deep couple briefing and a willingness to personalise every element creates an evening that guests will remember vividly.</p>
<h2>Program Structure</h2>
<p>Elopement receptions are typically dinner-focused, with a lighter formal program. Welcome and couple introduction, a small number of speeches from the closest family or friends, the couple's first dance or a shared toast, and an open evening. The MC's role is to frame each moment warmly without overloading a small gathering with formal structure.</p>
<h2>Tone and Energy</h2>
<p>The energy at an elopement reception is intimate and warm — not theatrical. An MC who projects across a large room brings the wrong energy to a setting where everyone is within five metres. Conversational, warm, and present is the register. Think host rather than performer.</p>
<h2>Why Use a Professional MC</h2>
<p>Some couples question whether an elopement reception needs a professional MC at all. The answer is yes — not because the event is complex, but because having someone whose role is specifically to manage the program, hold the atmosphere, and ensure the couple can simply enjoy their celebration rather than coordinate it, is genuinely valuable regardless of guest count.</p>"""
    },
    {
        "slug": "mc-for-afternoon-tea-perth",
        "title": "MC for an Afternoon Tea Event in Perth",
        "tag": "Events",
        "read_time": 4,
        "excerpt": "Afternoon tea events — charity fundraisers, milestone birthdays, corporate networking — are growing in Perth. An MC who matches the format makes them genuinely special.",
        "description": "How a Perth MC adapts their style for afternoon tea events — managing a lighter program, maintaining elegance, and keeping the occasion feeling refined.",
        "body": """<p>Afternoon tea events have a distinct register: elegant, unhurried, warm, and unequivocally daytime. An MC who brings night-event energy to an afternoon tea disrupts the very atmosphere that makes the format work.</p>
<h2>The Afternoon Tea Program</h2>
<p>Afternoon tea events are typically 90 minutes to two hours and built around light programming: a welcome, brief speeches or acknowledgements, a guest speaker or entertainment, and a close. The MC's role is to hold that structure lightly — creating moments without over-programming a format that's designed to feel relaxed.</p>
<h2>Charity Afternoon Teas</h2>
<p>Perth's charity sector regularly uses the afternoon tea format for fundraising events — High Tea for a cause, Mother's Day fundraisers, and community celebrations. At these events, the MC is managing both the social atmosphere and the fundraising element: introduction of the cause, impact storytelling, the ask, and the acknowledgement of donations. Getting the emotional arc right in a 90-minute window requires experience.</p>
<h2>Corporate Afternoon Teas</h2>
<p>Some Perth businesses use afternoon tea formats for client entertainment, team recognition events, or networking occasions. The MC role at a corporate afternoon tea is lighter than at a full conference — more about creating a welcoming atmosphere and managing any brief formal program than about high-energy audience facilitation.</p>
<h2>Milestone Celebrations</h2>
<p>Milestone birthday afternoon teas — 60th, 70th, 80th celebrations — work beautifully with an MC who understands the format. Warm speeches, personalised acknowledgements of the guest of honour, a relaxed program arc that builds to a toast and celebration. The register is gentle, celebratory, and unhurried.</p>
<h2>Tone and Presentation</h2>
<p>An MC at an afternoon tea should dress appropriately for the formality of the event, speak at a measured pace that suits the setting, and resist the impulse to inject energy that the format doesn't need. The goal is to make the occasion feel effortless and well-held — not high-energy and driven.</p>"""
    },
    {
        "slug": "perth-waterfront-wedding-venues-mc",
        "title": "Perth Waterfront Wedding Venues — An MC's Perspective",
        "tag": "Venues",
        "read_time": 6,
        "excerpt": "Perth has some of Australia's most spectacular waterfront wedding venues. What each location is like to host from the stage — and what couples should know.",
        "description": "A professional MC's guide to Perth's waterfront wedding venues — what makes each one unique, the acoustic challenges, and what couples should brief their MC about.",
        "body": """<p>Perth's position on the Indian Ocean and the Swan River gives it a remarkable collection of waterfront wedding venues. From the working character of Fremantle to the formal elegance of riverside venues, each location brings its own atmosphere — and its own hosting considerations.</p>
<h2>The Fremantle Waterfront</h2>
<p>Fremantle's working harbour gives waterfront venues a character that more polished locations lack. Venues along the Fremantle waterfront tend to attract couples who want relaxed, authentic atmosphere — and the program should reflect that. Expect wind, variable acoustics, and a guest energy that leans toward celebration rather than formality. An experienced outdoor MC is essential.</p>
<h2>Swan River Riverside Venues</h2>
<p>Riverside venues along the Swan — from Crawley to Applecross — offer some of Perth's most photogenic backdrops. Evening light on the water, the city skyline, and protected settings make these venues versatile for both intimate and larger receptions. Indoor venues with river views typically offer better acoustic control than fully outdoor settings.</p>
<h2>Hillarys and the Northern Beaches</h2>
<p>Venues along Perth's northern coast trade the river backdrop for the Indian Ocean. These settings are typically more casual in atmosphere and better suited to beach-adjacent program styles: relaxed ceremonies, sunset ceremonies, and receptions with an emphasis on the natural setting over formal program structure.</p>
<h2>What Every Waterfront MC Brief Should Include</h2>
<p>For any waterfront wedding, the MC needs to know: the venue's wet weather plan, the PA setup and any wind mitigation in place, the sunset timing if the ceremony or key moments are planned around it, and any specific venue protocols around noise or curfews. Perth's coastal venues often have sound restrictions that affect program timing.</p>
<h2>Making the Setting Part of the Program</h2>
<p>A skilled MC uses the waterfront setting as part of the event's narrative. Acknowledging the view, framing sunset moments, building atmosphere around the location rather than ignoring it — these choices make a waterfront wedding feel like it could only have happened exactly where it did.</p>"""
    },
    {
        "slug": "mc-for-perth-hills-wedding",
        "title": "MC for a Perth Hills Wedding — What to Know",
        "tag": "Weddings",
        "read_time": 6,
        "excerpt": "Perth Hills weddings — in the Darling Ranges, Swan Valley, and Bickley Valley — have a distinct character. Here's what makes them different from metropolitan venue weddings.",
        "description": "A guide to hosting Perth Hills weddings as an MC — unique venue characteristics, outdoor considerations, and why the Hills setting changes how an MC works.",
        "body": """<p>The Perth Hills — stretching from the Darling Ranges through the Swan Valley to Bickley and the Avon Valley — offer a style of wedding that the metropolitan area simply can't replicate. Estate properties, valley vineyards, bush settings, and sweeping views create events with a distinct atmosphere.</p>
<h2>Why Hills Weddings Are Different</h2>
<p>Hills properties tend to be larger, more spread out, and more reliant on natural beauty than built infrastructure. This creates beautiful photographs and relaxed atmospheres — and specific challenges for event management. Guests move across the property rather than staying in a single room. Acoustic management outdoors requires real expertise. Venue curfews are often stricter due to residential proximity.</p>
<h2>The Acoustic Environment</h2>
<p>Many Perth Hills wedding venues — estate lawns, orchard settings, pergola receptions — are partially or fully outdoor. An MC who hasn't worked outdoor settings before needs extra preparation here. Line check, speaker placement, wind management, and establishing audio early in the evening all matter more in a natural setting than in a purpose-built venue.</p>
<h2>Distance from the City and Timing</h2>
<p>Perth Hills venues can be 40 to 60 minutes from the CBD. This affects everything: supplier arrival times, the MC's own travel, and the evening curfew that determines when formal programming must close. Build transit time into the day's schedule and confirm the venue's end time well in advance.</p>
<h2>Weather and Season</h2>
<p>Hills weddings are most popular in spring and autumn, when the Darling Ranges are at their most beautiful and temperature is manageable. Summer evenings can be warm, and winter carries risk of rain and cold. An MC should be briefed on the venue's contingency plan and be ready to adjust the program if conditions change.</p>
<h2>The Register That Fits</h2>
<p>Hills weddings typically have a warm, relaxed, nature-connected atmosphere. An MC who works this setting well brings that same quality: unhurried, genuine, celebrating the setting as part of the event rather than working against it. The tone should feel like you're among friends, not performing on a stage.</p>"""
    },
    {
        "slug": "how-to-write-mc-script-template",
        "title": "How to Write an MC Script — A Template for Any Event",
        "tag": "Craft",
        "read_time": 6,
        "excerpt": "A well-structured MC script prevents blank moments, keeps transitions smooth, and gives you a framework to work from no matter how the event shifts.",
        "description": "A practical MC script template for any event type — structure, key sections, what to script word-for-word versus improvise, and how to make it sound natural.",
        "body": """<p>A great MC script isn't a word-for-word transcript — it's a structured framework that captures the essential scripted moments and leaves room for the natural adaptation that makes live hosting feel alive.</p>
<h2>What to Script Word-for-Word</h2>
<p>Four sections of any MC engagement benefit from precise scripting: the opening welcome (your first impression sets every expectation), formal introductions (names, titles, and context that must be accurate), award or toaster introductions (where precision and build-up matter), and the close (your last words should land with intention, not tail off). Everything else can be notes and bullet points.</p>
<h2>Opening Welcome Template</h2>
<p>Structure: warm welcome and acknowledgement of the occasion → brief housekeeping (exits, phones, dietary) → program overview → first program element introduction. Length: 90 seconds to two minutes. Tone: set it here. The room takes its cue from the MC's opening energy.</p>
<h2>Speaker Introduction Template</h2>
<p>Structure: frame the segment → introduce the speaker's relevant background (briefly) → handoff. "We're now moving to our keynote session. Our next speaker has spent the past fifteen years working in [field], and tonight they're going to share [specific insight]. Please welcome [full name]." Under 45 seconds. Practice it so it sounds read naturally, not read.</p>
<h2>Transition Lines</h2>
<p>Every gap between program elements needs a bridge. Build a library of transition lines that suit your event type. "Before we continue, I want to take a moment to acknowledge..." — "Coming up next, we have something a little different..." — "We'll take a short break and be back at [time]..." These are two to three sentences. Script them for each transition and adjust on the night.</p>
<h2>The Close Template</h2>
<p>Structure: final acknowledgements (couple, organisers, speakers, venue as applicable) → summary of the evening's achievement or significance → send-off. Don't rush the close — it's the room's last impression. "Tonight has been..." followed by something specific and true, followed by "On behalf of [hosts], thank you for being here." Clean, warm, final.</p>"""
    },
    {
        "slug": "mc-for-nonprofit-fundraiser-perth",
        "title": "MC for a Nonprofit Fundraiser in Perth",
        "tag": "Events",
        "read_time": 6,
        "excerpt": "Nonprofit fundraisers have specific MC requirements that commercial events don't. Understanding the cause, managing the ask, and maintaining energy through the giving moments.",
        "description": "What makes a nonprofit fundraiser MC different — cause briefing, managing the ask, auction facilitation, and keeping emotional energy aligned with the giving goal.",
        "body": """<p>Nonprofit fundraisers are among the most purpose-driven events an MC works. Every element of the program — the stories, the entertainment, the program structure — is designed around a single goal: inspiring generosity. The MC is central to whether that goal is achieved.</p>
<h2>Deep Cause Briefing</h2>
<p>An MC at a nonprofit fundraiser needs to understand the cause at a level of genuine depth — not just the name of the organisation, but the specific impact stories, the people served, and the tangible difference that funds raised will make. This knowledge shows. An MC who speaks about a cause with authentic understanding moves a room more effectively than one reading prepared copy.</p>
<h2>The Emotional Arc</h2>
<p>The most effective nonprofit event programs build emotional engagement before making any financial ask. Open with context and celebration, build through impact stories and personal testimony, allow guests to feel genuinely connected to the cause, and then make the ask at the moment of maximum emotional resonance. The MC guides this arc — not rushing to the ask, not letting the energy dissipate before it arrives.</p>
<h2>Facilitating the Live Ask</h2>
<p>Whether the financial ask is via live auction, pledge moment, or direct donation, the MC's framing determines how it lands. Language that celebrates giving — that positions generosity as positive action rather than obligation — consistently outperforms pressure-based appeals. Brief the MC on the specific ask amounts and mechanisms so they can reinforce them naturally during the program.</p>
<h2>Auction Management</h2>
<p>Many nonprofit events include a live auction. A professional MC who can facilitate the auction (or hand to an auctioneer and support the process) is more valuable than one who steps back and lets the auction happen. Key skills: building excitement for each lot, managing the bidding pace, acknowledging winners warmly, and maintaining energy across a long auction program.</p>
<h2>Closing With Gratitude</h2>
<p>The close of a nonprofit fundraiser should land with warmth and genuine thanks. Acknowledge the cause, the donors, the volunteers, and the committee — briefly, specifically, and sincerely. Leave guests feeling that their evening was well spent and their generosity mattered. This is the MC's final contribution to the fundraising goal.</p>"""
    },
    {
        "slug": "difference-between-emcee-and-host",
        "title": "The Difference Between an Emcee and an Event Host",
        "tag": "Planning",
        "read_time": 4,
        "excerpt": "The terms 'emcee' and 'host' are used interchangeably — but they describe genuinely different roles. Understanding the distinction helps you hire the right person.",
        "description": "What's the difference between a professional emcee and an event host — role definitions, skill sets, and which one your Perth event actually needs.",
        "body": """<p>Event organisers sometimes use 'emcee' and 'host' as interchangeable terms. They're closely related but different in emphasis — and understanding the distinction helps you hire the right person for your event.</p>
<h2>What an Emcee Does</h2>
<p>An emcee (MC — Master of Ceremonies) is responsible for the formal structure of an event's program. They open the event, introduce speakers and segments, manage transitions, make announcements, and close the program. Their primary role is procedural: keeping the event on time and on track while maintaining the atmosphere. At corporate events, galas, conferences, and weddings with significant formal content, the MC function is primary.</p>
<h2>What a Host Does</h2>
<p>An event host's primary function is atmosphere — creating warmth, engaging guests, facilitating connection, and making the room feel welcome throughout the event. The host role is less procedurally focused and more relationally focused. At networking events, cocktail receptions, and events with minimal formal program, the host role dominates.</p>
<h2>Where They Overlap</h2>
<p>The best MCs are also excellent hosts — they do both. They manage the procedural elements of the event with precision and also bring genuine warmth and connection to every interaction. Similarly, a skilled host who can also run a formal program when needed is more versatile. In practice, most events need both functions, and most professional MCs provide them.</p>
<h2>Which Does Your Event Need?</h2>
<p>If your event has significant structured content — speeches, awards, presentations, formal program elements — you need MC function. If your event is primarily social and atmospheric — cocktail party, casual networking event, community celebration — host function is more relevant. Most events need some of both, with the balance depending on the program complexity.</p>
<h2>What to Ask When Booking</h2>
<p>When enquiring about a professional MC or host for your Perth event, describe the event structure clearly: how much formal program content exists, how large the audience is, whether there are specific scripted moments, and what the overall tone should be. This helps match the right person to the right event.</p>"""
    },
    {
        "slug": "how-mc-works-with-band-dj",
        "title": "How an MC Works with a Band or DJ",
        "tag": "Craft",
        "read_time": 5,
        "excerpt": "The MC and the music — band or DJ — are the two biggest influences on a reception's energy. When they work together, the result is seamless.",
        "description": "How professional MCs coordinate with wedding bands and DJs — transitions, handoffs, energy matching, and why pre-event coordination is non-negotiable.",
        "body": """<p>The relationship between the MC and the music act is one of the most important dynamics of any event that includes both. When it works, transitions are seamless, energy builds naturally, and the room flows from one experience to the next. When it doesn't, guests notice.</p>
<h2>The Pre-Event Coordination Call</h2>
<p>A professional MC should make contact with the band or DJ before the event — ideally at least a week out. The purpose: coordinate the program, align on transition cues, agree on who starts each segment and how, and identify any musical moments that require specific MC framing (first dance announcement, entrance music, final song). This call takes 20 minutes and prevents ten separate problems on the night.</p>
<h2>Entrance Timing and Music Cues</h2>
<p>The single most common MC-music coordination failure is the entrance: the MC is still talking when the music starts, or the music starts too early and drowns the introduction. Agree on a specific cue — a hand signal to the DJ, a word signal to the band — that initiates the music at exactly the right moment. Rehearse if the venue allows it.</p>
<h2>Energy Matching</h2>
<p>A skilled MC reads the energy of the room after a musical segment and adjusts accordingly. Coming in immediately after a high-energy band set with a slow, formal announcement kills the room's momentum. The best MCs build their transitions out of the existing energy — acknowledging what just happened before redirecting to what's next.</p>
<h2>Who Owns the Mic</h2>
<p>Clarity about who holds the microphone at any given point eliminates confusion. At a wedding, when the DJ/band has the floor, the MC doesn't interrupt unnecessarily. When the program requires MC content, the music makes way. This handoff protocol should be agreed in advance — not improvised in the moment.</p>
<h2>Supporting Each Other's Performance</h2>
<p>A great MC sets up the music act well — builds anticipation for the band's entrance, acknowledges their performance warmly after a set, and creates the emotional conditions in which live music lands best. In return, a professional band or DJ who understands the MC's program needs will deliver their sets with that context in mind. The best events feel collaborative.</p>"""
    },
    {
        "slug": "mc-for-company-agm-perth",
        "title": "MC for a Company AGM in Perth",
        "tag": "Corporate",
        "read_time": 5,
        "excerpt": "Annual General Meetings are formal events with specific procedural requirements. An experienced MC keeps proceedings on track and ensures compliance with protocol.",
        "description": "What to look for in an MC for a Perth company AGM — formal protocol, shareholder engagement, managing Q&A, and keeping proceedings to time.",
        "body": """<p>Annual General Meetings are among the most procedurally specific events an MC will be asked to host. They're formal by nature, often legally constrained in how proceedings must unfold, and include Q&A sessions that can be unpredictable. The right MC brings structure, authority, and composure.</p>
<h2>Understanding the AGM Format</h2>
<p>An AGM program typically includes: the opening and quorum confirmation, welcome and chairperson introduction, financial report presentation, consideration of ordinary and special resolutions, director elections if applicable, appointment of auditors, general business and Q&A, and close. The MC needs to understand the order and the specific protocol for each element — these are not informal events where improvisation serves well.</p>
<h2>Formal Language and Tone</h2>
<p>The language of an AGM has a specific register: formal, measured, procedurally precise. "I now call the meeting to order" is not the same as "Let's get started." A professional MC who has worked AGM environments knows this register instinctively and shifts into it appropriately. An MC who brings casual energy to a shareholder meeting creates immediate credibility problems.</p>
<h2>Managing Shareholder Q&A</h2>
<p>The Q&A segment of an AGM is where MCs earn their fee. Shareholders can ask challenging questions, and the dynamics can be adversarial. An experienced AGM MC manages the Q&A with a firm but fair process: clear instructions for how questions are submitted, orderly management of the speaking list, time management per questioner, and a clean close when the time is up.</p>
<h2>Procedural Compliance</h2>
<p>AGMs are legally required events for public companies and many incorporated entities. Procedural errors — in the order of business, the calling of votes, or the management of resolutions — can have legal consequences. The MC should work closely with the company secretary or legal counsel to understand any procedural requirements specific to the organisation.</p>
<h2>Keeping the Meeting to Time</h2>
<p>Shareholders and board members attending an AGM have busy schedules. Managing the program to the advised time is important. An MC who lets the meeting run long without evident cause reduces confidence in the governance of the event. Set clear time expectations at the opening and manage them throughout.</p>"""
    },
    {
        "slug": "tips-nervous-speakers-mc-support",
        "title": "How an MC Supports Nervous Speakers",
        "tag": "Craft",
        "read_time": 5,
        "excerpt": "Many event speakers are nervous — some severely so. An experienced MC provides support that makes the difference between a speaker who delivers and one who struggles.",
        "description": "Practical techniques for MCs supporting nervous event speakers — pre-event preparation, warm introductions, and creating conditions for confident delivery.",
        "body": """<p>Public speaking anxiety is widespread. An experienced MC creates conditions in which nervous speakers can deliver their best — and when that support is well-delivered, the entire event benefits from it.</p>
<h2>The Pre-Event Briefing</h2>
<p>For speakers who are visibly anxious before an event, a calm, private conversation with the MC before proceedings begin makes a significant difference. Cover the practical details: how they'll be introduced, where they should stand, how the microphone works, what the expected duration is, and that the MC will manage their transition on and off stage. Removing uncertainty reduces anxiety.</p>
<h2>The Power of a Strong Introduction</h2>
<p>A warm, specific, well-prepared introduction does two things: it tells the room why the speaker is worth listening to, and it tells the speaker that the MC has taken their role seriously. A speaker who walks to the podium in the wake of a genuine, well-delivered introduction steps up with more confidence than one introduced with minimal preparation.</p>
<h2>Creating a Welcoming Room</h2>
<p>The MC's tone before a speaker takes the stage sets the audience's emotional disposition toward them. A room that's warm, attentive, and positively oriented is easier to speak to than one that's flat or distracted. An MC who brings genuine warmth to the room before a speaker's introduction is creating the conditions for that speaker's success.</p>
<h2>Microphone Management</h2>
<p>For speakers unfamiliar with a handheld microphone, a brief (30-second) practical tutorial backstage — how to hold it, how close to speak, what to do if they hear feedback — prevents the technical panic that compounds speech anxiety. An MC who takes two minutes to run this before the event saves the room from the visible discomfort of watching someone fight with a microphone.</p>
<h2>After the Speech</h2>
<p>How the MC receives a speech affects both the speaker and the room. A warm, brief acknowledgement — "Thank you so much to [name]" — followed by genuine applause management, gives the speaker a clear landing moment and closes their segment with positive energy. Never rush this transition. The speaker deserves a clean close as much as a clean start.</p>"""
    },
    {
        "slug": "how-to-get-crowd-energy-up-mc",
        "title": "How to Get Crowd Energy Up as an MC",
        "tag": "Craft",
        "read_time": 5,
        "excerpt": "Every event has a moment where energy dips. The techniques experienced MCs use to raise it — without cheap tricks or forced enthusiasm.",
        "description": "Practical MC techniques for raising crowd energy at events — reading the dip, proven recovery techniques, and how to rebuild momentum without losing the room.",
        "body": """<p>Every event hits a low-energy moment. After a long lunch, mid-afternoon at a conference, late in a gala dinner — the room dips. An experienced MC knows how to bring it back without forcing it.</p>
<h2>Reading the Energy Drop</h2>
<p>Before you can raise energy, you need to recognise it. Signs: cross-talk increases, guests start checking phones, applause becomes perfunctory, eye contact reduces. These signals appear before the energy drop is obvious to the whole room. The MC who catches the dip early has more options than the one who lets it compound.</p>
<h2>Movement and Stand-Up</h2>
<p>Asking an audience to stand — for a toast, a standing ovation, or a transition — resets physical posture and increases blood flow. Used deliberately at the right moment (not randomly, not too often), it's one of the fastest and most reliable energy resets available. "Before we continue, I'd like everyone on their feet for a moment."</p>
<h2>Compression and Pace</h2>
<p>A lagging energy often signals that the pace has slowed too much. Compress the next few segments: tighten the transitions, move briskly between elements, reduce dead air. The room responds to an MC who increases their own energy and pace — it creates momentum through modelling.</p>
<h2>Genuine Humour</h2>
<p>A well-timed, genuine, earned laugh at the right moment can reset a room completely. This is not joke-telling — it's reading the room for the observation that's already in the air and giving it voice. Forced humour when the room is flat makes the flat worse. Genuine, specific humour — a line that only works for this room, this event, this moment — lifts the energy authentically.</p>
<h2>The Reset Technique</h2>
<p>For a significant energy drop, an explicit reset works better than subtle adjustment. Acknowledge the moment with warmth: "We've had a big program — there's one more section to go and it's the one you've been waiting for." Setting up anticipation explicitly gives the audience a reason to re-engage, and signals that the MC is in control and steering toward the best part of the night.</p>"""
    },
    {
        "slug": "mc-for-wedding-with-children-perth",
        "title": "MC for a Wedding with Children in Perth",
        "tag": "Weddings",
        "read_time": 5,
        "excerpt": "Weddings with children in the guest list — or as part of the bridal party — require an MC who can include them without letting them derail the program.",
        "description": "How an experienced Perth MC handles weddings with children — inclusive program moments, managing the unexpected, and keeping both adults and kids engaged.",
        "body": """<p>Weddings with children present are simultaneously more joyful and less predictable than adults-only events. An MC who knows how to work with children in the room creates moments of genuine delight — while also knowing how to manage the unexpected.</p>
<h2>Including Children in the Program</h2>
<p>Children who are part of the bridal party — flower girls, ring bearers, young attendants — deserve acknowledgement in the program. A brief, warm mention by the MC ("and a special thank you to our flower girls, [names], for doing such a wonderful job today") includes them in the celebration in a way that the whole room responds to positively.</p>
<h2>The Unexpected Interruption</h2>
<p>A child who makes an unexpected noise, wanders into frame, or otherwise creates an unplanned moment is a feature of weddings, not a problem. An experienced MC responds with warmth rather than ignoring it. A light, genuine acknowledgement — "I think we have a volunteer for next year's event" — lands the moment without making parents feel embarrassed.</p>
<h2>Program Pacing for Families</h2>
<p>When the guest list includes families with young children, the program benefits from moving briskly. Long, slow sections — extended speeches, lengthy formalities — are harder on children and harder on parents managing them. An MC who understands the guest list can flag this to the couple during briefing and suggest pacing adjustments.</p>
<h2>Managing Noise During Speeches</h2>
<p>Children making noise during speeches is the most likely disruption at a wedding with families. An experienced MC normalises this gently — "We're very family-friendly tonight" — and ensures speakers are briefed to continue speaking through minor background noise rather than stopping and waiting. Stopping and waiting creates tension; continuing creates warmth.</p>
<h2>The Tone That Lands</h2>
<p>Weddings with children present have a specific warmth and energy — alive, generous, occasionally chaotic in the best possible way. An MC who embraces that atmosphere, rather than trying to maintain the atmosphere of a childless formal event, creates a celebration that genuinely reflects the couple's community.</p>"""
    },
]

TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="{description}" />
  <meta name="robots" content="noindex, nofollow" />
  <title>{title} | Perth MC</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../css/style.css" />
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "{title}",
    "description": "{description}",
    "url": "https://perthmc.com/blog-{slug}.html",
    "publisher": {{
      "@type": "Organization",
      "name": "Perth MC",
      "url": "https://perthmc.com"
    }}
  }}
  </script>
</head>
<body>

<header class="site-header">
  <div class="container header-inner">
    <a href="../index.html" class="logo">Perth<span>MC</span></a>
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
    <h1>{title}</h1>
    <div class="blog-meta">{tag} &nbsp;&middot;&nbsp; {read_time} min read</div>
  </div>
</section>
<div class="blog-body">
{body}
<div class="blog-cta-box">
  <h3>Need a Professional MC for Your Event?</h3>
  <p>Perth-based, experienced across all event types, and available to discuss your date.</p>
  <a href="../contact.html" class="btn btn-primary">Check Availability</a>
</div></div>
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
        <a href="../index.html" class="logo">Perth<span>MC</span></a>
        <p>Perth\'s professional MC for weddings, corporate events, galas, conferences, and milestone celebrations.</p>
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
      <p>&copy; 2026 Perth MC. All rights reserved.</p>
    </div>
  </div>
</footer>
<script src="../js/main.js"></script>
</body>
</html>'''


def main():
    os.makedirs(DRAFTS_DIR, exist_ok=True)

    # Load existing queue
    with open(QUEUE_FILE, "r", encoding="utf-8") as f:
        queue_data = json.load(f)

    existing_slugs = {entry["slug"] for entry in queue_data["queue"]}
    generated = []
    skipped = []

    for post in POSTS:
        slug = post["slug"]
        full_slug = f"blog-{slug}"
        filename = f"blog-{slug}.html"
        filepath = os.path.join(DRAFTS_DIR, filename)

        # Write HTML file
        html = TEMPLATE.format(
            slug=slug,
            title=post["title"],
            tag=post["tag"],
            read_time=post["read_time"],
            description=post["description"],
            body=post["body"].strip(),
        )

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)

        # Add to queue if not already present
        if full_slug not in existing_slugs:
            queue_data["queue"].append({
                "slug": full_slug,
                "title": post["title"],
                "tag": post["tag"],
                "read_time": post["read_time"],
                "excerpt": post["excerpt"],
            })
            existing_slugs.add(full_slug)
            generated.append(full_slug)
        else:
            skipped.append(full_slug)

    # Save updated queue
    with open(QUEUE_FILE, "w", encoding="utf-8") as f:
        json.dump(queue_data, f, ensure_ascii=False, indent=2)

    print(f"Generated: {len(generated)} new posts")
    for s in generated:
        print(f"  + {s}")
    if skipped:
        print(f"Skipped (already in queue): {len(skipped)}")
        for s in skipped:
            print(f"  - {s}")
    print(f"\nQueue now contains {len(queue_data['queue'])} entries.")
    print("Done.")


if __name__ == "__main__":
    main()
