# Page specs for saltservicesusa.com — bodies, titles, descriptions, FAQs.
# Edit copy here, then run: python3 _build/gen.py
from gen import (SPRINKLE, icon, check_li, coraline_section, faq_html, faq_ld,
                 service_ld, BIZ)

PHONE = BIZ["phone_display"]
TEL = BIZ["phone_tel"]

def cta_band(heading, blurb, btn_text="Get your free growth plan", btn_href="/contact/#form"):
    return f"""<section class="section section-navy cta-band">
  <div class="wrap">
    <div>
      <h2>{heading}</h2>
      <p>{blurb}</p>
    </div>
    <div><a class="btn btn-accent" href="{btn_href}">{btn_text}</a></div>
  </div>
</section>
"""

SERVICE_CARDS = f"""<ul class="card-grid">
  <li class="card">{icon('web')}
    <h3>Web design</h3>
    <p>Hand-built sites that load fast, rank on Google, and turn visitors into calls and form fills. Own it outright or rent it monthly.</p>
    <a class="card-link" href="/services/web-design/">Web design &rsaquo;</a>
  </li>
  <li class="card">{icon('seo')}
    <h3>SEO &amp; AEO</h3>
    <p>Three genuinely useful pages a month that win Google searches and get your business cited by AI assistants.</p>
    <a class="card-link" href="/services/seo-aeo/">SEO &amp; AEO &rsaquo;</a>
  </li>
  <li class="card">{icon('ads')}
    <h3>Digital advertising</h3>
    <p>Google and Meta campaigns with every dollar tracked to a real lead. We'll tell you plainly if your budget won't work.</p>
    <a class="card-link" href="/services/digital-advertising/">Digital advertising &rsaquo;</a>
  </li>
  <li class="card">{icon('crm')}
    <h3>CRM implementation</h3>
    <p>Every lead tracked, followed up, and closed. Pipelines, automations, missed-call text-back, and training for your team.</p>
    <a class="card-link" href="/services/crm-implementation/">CRM implementation &rsaquo;</a>
  </li>
  <li class="card">{icon('ai')}
    <h3>AI implementation</h3>
    <p>AI that answers leads in seconds, drafts follow-ups, and books appointments — wired into your CRM with a human in the loop.</p>
    <a class="card-link" href="/services/ai-implementation/">AI implementation &rsaquo;</a>
  </li>
  <li class="card">{icon('map')}
    <h3>East Tennessee, in person</h3>
    <p>Based in Kodak. We meet clients face to face from <a href="/service-areas/sevierville/">Sevierville</a> to <a href="/service-areas/knoxville/">Knoxville</a> and everywhere between.</p>
    <a class="card-link" href="/service-areas/">Service areas &rsaquo;</a>
  </li>
</ul>"""

# ============================================================ HOME
HOME_FAQS = [
    ("What does Salt Services actually do?",
     "We're a marketing and AI implementation agency. We build websites that rank on Google, run Google and Meta ad campaigns, set up CRMs so every lead gets tracked and followed up, and wire in AI to respond to leads faster than a human can. Most clients start with one service and add the rest as the leads pick up."),
    ("Do you only work with businesses near Kodak?",
     "East Tennessee is home turf — Kodak, Sevierville, Pigeon Forge, Gatlinburg, Knoxville, Maryville, Dandridge — and we like meeting clients face to face. Websites, SEO, and ad management travel well though, so we take on clients outside the area too."),
    ("How much does marketing with Salt Services cost?",
     "It depends on what you need, so we won't print a made-up number here. After the inquiry form and a short call, you get a written quote with a flat price and exactly what it covers. If we think you don't need something, we'll say so."),
    ("Why is the company called Salt Services?",
     "The name comes from Matthew 5:13 — \"you are the salt of the earth.\" We started this agency to help small businesses salt up their web presence and their cash flow. The story is on our about page."),
]

HOME_BODY = f"""<section class="hero hero-3d">
  <div id="hero-scene" aria-hidden="true"></div>
  <span class="hero-hud b1" aria-hidden="true">Now forming: <span id="shape">SPHERE</span> &middot; cursor repels</span>
  <span class="hero-hud b2" aria-hidden="true">N = 14,000</span>
  <div class="wrap">
    <span class="hero-kicker reveal" style="animation-delay:.2s">Marketing &amp; AI implementation &middot; Kodak, TN</span>
    <h1 class="reveal" style="animation-delay:.4s">Get found.<br>Get <span class="accent">answered</span>.<br>Get more leads.</h1><!-- accent word renders italic serif amber -->
    <p class="lead reveal" style="animation-delay:.6s">Salt Services is a marketing and AI implementation agency in Kodak, Tennessee. We build websites that rank on Google and get cited by AI, run ads that pay for themselves, and set up CRMs and AI so no lead ever slips through the cracks.</p>
    <p class="reveal" style="animation-delay:.8s">
      <a class="btn btn-accent" href="/contact/#form">Get your free growth plan</a>
      <a class="btn btn-ghost" href="tel:{TEL}">Call {PHONE}</a>
    </p>
    <p class="hero-note reveal" style="animation-delay:1s">The plan is a real audit — we review your website, your Google profile, and your top competitor, then tell you exactly what we'd fix. Free, and yours to keep either way.</p>
  </div>
</section>
<script type="importmap">
{{ "imports": {{ "three": "https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js" }} }}
</script>
<script type="module" src="/js/hero3d.js"></script>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <h2>Five services, one lead pipeline</h2>
      {SPRINKLE}
      <p>Everything we build feeds the same goal: more of the right people finding you, calling you, and becoming customers.</p>
    </div>
    {SERVICE_CARDS}
  </div>
</section>

<section class="section section-alt">
  <div class="wrap prose">
    <h2>Where do your customers actually look for you now?</h2>
    {SPRINKLE}
    <p>Two places. Google, same as the last twenty years — and AI assistants, which is newer than most marketing playbooks. When somebody in Sevier County needs a plumber, a cabin cleaner, or a dentist, they either search and call whoever ranks, or they ask ChatGPT and call whoever it names. Either way, most of the decision happens before the phone ever rings.</p>
    <p>That's the whole reason our services look the way they do. The <a href="/services/web-design/">website</a> and the monthly <a href="/services/seo-aeo/">SEO and AEO pages</a> win the searches and the AI citations. <a href="/services/digital-advertising/">Ads</a> buy the top spot while the free rankings compound. And the <a href="/services/crm-implementation/">CRM</a> and <a href="/services/ai-implementation/">AI follow-up</a> make sure a lead that took months to earn doesn't die in a voicemail box.</p>
  </div>
</section>

<section class="section section-navy">
  <div class="wrap">
    <div class="section-head">
      <h2>Why hire the young agency?</h2>
      {SPRINKLE}
      <p>We're new enough to care about every single client and old enough to know what we're doing. Here's what that gets you.</p>
    </div>
    <ul class="card-grid card-grid two">
      <li class="card">
        <h3>Hungry, and reachable</h3>
        <p>We're a young company with something to prove. Your calls get answered, your work gets shipped, and your account never gets handed down to whoever's newest.</p>
      </li>
      <li class="card">
        <h3>One system, not five vendors</h3>
        <p>Your website, ads, CRM, and AI are built by one team to work as one pipeline. Leads stop falling through the gaps between vendors, because there are no gaps.</p>
      </li>
      <li class="card">
        <h3>Local enough to shake hands</h3>
        <p>We're in Kodak — fifteen minutes from Sevierville, about twenty-five from Knoxville. If you'd rather talk across a table than a screen, we'll come to you.</p>
      </li>
      <li class="card">
        <h3>Reports you can actually read</h3>
        <p>Every month you'll know what got done, what it cost, and what it produced — in plain English, not a 40-page PDF of charts nobody opens.</p>
      </li>
    </ul>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <h2>Recent work</h2>
      {SPRINKLE}
      <p>We're a young agency, so instead of telling you our work is good, here it is — live sites you can click on right now. These are the local ones; we build for clients well beyond Sevier County too.</p>
    </div>
    <ul class="card-grid">
      <li class="card work-card">
        <a href="https://americanfireplaces.vercel.app/" target="_blank" rel="noopener">
          <img src="/images/work/american-fireplaces.webp" alt="American Fireplaces website — dark, ember-lit hero reading 'Gather around something extraordinary'" width="640" height="400" loading="lazy">
          <div class="work-body">
            <h3>American Fireplaces</h3>
            <p>A cinematic brand site for a Sevierville hearth showroom that has warmed the Smokies since 1990.</p>
            <span class="card-link">Visit the live site &rsaquo;</span>
          </div>
        </a>
      </li>
      <li class="card work-card">
        <a href="https://www.mtnlandscapers.com/" target="_blank" rel="noopener">
          <img src="/images/work/mountain-landscapers.webp" alt="Mountain Landscapers website — deep green hero with serif headline 'Landscaping Sevierville'" width="640" height="400" loading="lazy">
          <div class="work-body">
            <h3>Mountain Landscapers</h3>
            <p>Landscape design and hardscapes, built page by page to win Sevier County searches.</p>
            <span class="card-link">Visit the live site &rsaquo;</span>
          </div>
        </a>
      </li>
      <li class="card work-card">
        <a href="https://downtown-river-rentals.vercel.app/" target="_blank" rel="noopener">
          <img src="/images/work/downtown-river-rentals.webp" alt="Downtown River Rentals website — cottage porch photo under 'Vacation Homes in Pigeon Forge'" width="640" height="400" loading="lazy">
          <div class="work-body">
            <h3>Downtown River Rentals</h3>
            <p>A direct-booking site for Pigeon Forge vacation cottages — bookings without the platform commission.</p>
            <span class="card-link">Visit the live site &rsaquo;</span>
          </div>
        </a>
      </li>
    </ul>
    <p class="work-more"><a class="btn btn-navy" href="/work/">See all our work</a></p>
  </div>
</section>

<section class="section section-alt">
  <div class="wrap">
    <div class="section-head">
      <h2>How working with us starts</h2>
      {SPRINKLE}
    </div>
    <ul class="card-grid">
      <li class="card">
        <span class="step-num" aria-hidden="true">01</span>
        <h3>Tell us about your business</h3>
        <p>Fill out the inquiry form — it takes about two minutes and asks just enough for us to do real homework before we call.</p>
      </li>
      <li class="card">
        <span class="step-num" aria-hidden="true">02</span>
        <h3>Get a real plan, free</h3>
        <p>We look at your market, your competition, and your current web presence, then walk you through what we'd do and what it costs. Keep the plan either way.</p>
      </li>
      <li class="card">
        <span class="step-num" aria-hidden="true">03</span>
        <h3>Watch the pipeline fill</h3>
        <p>We build, you approve, and every lead lands in your CRM where you can see it. No guessing whether the marketing is working.</p>
      </li>
    </ul>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <h2>Who we're built for</h2>
      {SPRINKLE}
      <p>The pipeline is the same everywhere — website, visibility, follow-up. What changes is the local knowledge, and East Tennessee is the part we know cold.</p>
    </div>
    <ul class="card-grid">
      <li class="card">
        <h3>Tourism &amp; hospitality</h3>
        <p>Cabin companies, attractions, and restaurants on the corridors from Sevierville to Gatlinburg. Seasonal ad budgets, direct bookings, and pages that win trip-planning searches.</p>
      </li>
      <li class="card">
        <h3>Home-service trades</h3>
        <p>HVAC, plumbing, roofing, landscaping. Local search is the whole game here, and missed-call text-back rescues the jobs that used to go to whoever answered second.</p>
      </li>
      <li class="card">
        <h3>Health &amp; wellness</h3>
        <p>Dentists, chiropractors, therapists, med spas. Booking-first websites, review momentum, and follow-up that fills the calendar without burdening the front desk.</p>
      </li>
      <li class="card">
        <h3>Professional services</h3>
        <p>Law, accounting, insurance, real estate. Trust-first sites and neighborhood-level SEO, because nobody hires a professional from a thin, slow web page.</p>
      </li>
      <li class="card">
        <h3>Retail &amp; local shops</h3>
        <p>From Parkway storefronts to Knoxville boutiques. Google Maps presence, social advertising, and a site that answers the question every visitor has: is it worth the drive?</p>
      </li>
      <li class="card">
        <h3>Not on the list?</h3>
        <p>If your customers search for what you do — and they do — the same pipeline applies. <a href="/contact/">Tell us what you run</a> and we'll tell you honestly whether we can help.</p>
      </li>
    </ul>
  </div>
</section>

<section class="section section-alt">
  <div class="wrap">
    <div class="section-head">
      <h2>Where we work</h2>
      {SPRINKLE}
      <p>Based in Kodak, serving businesses across East Tennessee: <a href="/service-areas/sevierville/">Sevierville</a>, <a href="/service-areas/knoxville/">Knoxville</a>, Pigeon Forge, Gatlinburg, Maryville, Dandridge, and beyond. Websites and SEO clients come from anywhere. See all <a href="/service-areas/">service areas</a>.</p>
      <p>Kodak puts us fifteen minutes from Sevierville's Parkway, about twenty-five from downtown Knoxville, and roughly the same from Dandridge's courthouse square — close enough to meet every client face to face, and far enough into the county to know what a small-town budget actually looks like.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap prose">
    <h2>Promises we'll put in writing</h2>
    {SPRINKLE}
    <p>A young agency doesn't get to lean on a twenty-year track record, so we lean on terms instead:</p>
    <ul class="checklist">
      {check_li("A flat, written quote before any work starts — no hourly meter, no surprise line items")}
      {check_li("You own your ad accounts and your data, and on the buyout option, your website outright")}
      {check_li("Every new page ships on a private preview link you approve before it goes live")}
      {check_li("A monthly report in plain English: what got done, what it cost, what it produced")}
      {check_li("If we think you shouldn't buy something, we say so — including our own services")}
    </ul>
  </div>
</section>
""" + faq_html(HOME_FAQS) + cta_band(
    "Ready for step one?",
    "The inquiry form takes about two minutes, and it gets you a real growth plan — free, whether or not you hire us.",
    "Fill out the inquiry form", "/contact/#form")

# ============================================================ SERVICES HUB
SERVICES_HUB_BODY = f"""<section class="section">
  <div class="wrap">
    <div class="section-head">
      <h1>Marketing services built to work as <em>one system</em></h1>
      {SPRINKLE}
      <p>Most agencies sell you a website <em>or</em> ads <em>or</em> SEO and leave you to glue it together. We build the whole pipeline: a site that ranks, ads that fill it with visitors, a CRM that catches every lead, and AI that responds before your competitors wake up.</p>
    </div>
    {SERVICE_CARDS}
  </div>
</section>

<section class="section section-alt">
  <div class="wrap">
    <div class="prose">
      <h2>How the pieces fit together</h2>
      {SPRINKLE}
      <p>Think of it as a water system. Your <a href="/services/web-design/">website</a> is the well — everything else is worthless if it's dry. <a href="/services/seo-aeo/">SEO and AEO</a> keep it filling steadily and for free, month after month. <a href="/services/digital-advertising/">Advertising</a> is the pump you turn on when you want more volume right now. Your <a href="/services/crm-implementation/">CRM</a> is the tank that catches every drop, and <a href="/services/ai-implementation/">AI</a> makes sure none of it evaporates while you're busy running the business.</p>
      <p>You don't have to buy the whole system on day one. Most clients start where the leak is worst — usually the website or the follow-up — and add from there. On the first call we'll tell you which piece we'd fix first and why.</p>
    </div>
  </div>
</section>
""" + cta_band("Not sure which service you need?",
               f"That's what the free growth plan is for. Tell us about your business and we'll point at the leak. Or call {PHONE}.")

# ============================================================ CRM
CRM_FAQS = [
    ("How much does CRM implementation cost?",
     "It depends on how many pipelines, automations, and integrations your business needs, so we quote it flat and in writing after a short call. You'll know the full price before we start — no hourly meter running."),
    ("We're a two-person shop. Do we really need a CRM?",
     "If you've ever forgotten to call a lead back, yes. Small teams actually feel the benefit fastest, because one missed follow-up is a bigger share of your revenue. A basic setup — leads in, reminders out — is cheap insurance."),
    ("Can the CRM text customers for us?",
     "Yes. Texting is usually the highest-impact automation we set up: missed-call text-back alone rescues leads who would otherwise just call the next business on the list. Review requests and appointment reminders ride the same rails."),
    ("What happens to the contacts in our spreadsheet or old system?",
     "We migrate them. Part of every implementation is importing your existing contacts and job history so you start with your whole book of business in one place, not an empty database."),
]

CRM_BODY = f"""<section class="section">
  <div class="wrap prose">
    <h1>CRM implementation for <em>small businesses</em></h1>
    {SPRINKLE}
    <p>Right now, your leads probably live in five places: missed calls, text threads, a Facebook inbox, somebody's email, and a legal pad by the register. Every one of those is a place where a paying customer can quietly disappear. A CRM puts every lead in one pipeline where nothing gets forgotten — and we do the part nobody has time for: setting it up so it actually works.</p>

    <h2>What does CRM implementation include?</h2>
    <p>Everything between "we should get organized" and your team using it daily without thinking about it:</p>
    <ul class="checklist">
      {check_li("Pipeline design that matches how your business actually sells")}
      {check_li("Lead capture wired in from your website, Google Business Profile, and social pages")}
      {check_li("Missed-call text-back, so a call you can't take still becomes a conversation")}
      {check_li("Automated follow-up sequences by text and email")}
      {check_li("Review requests that go out automatically after a job wraps")}
      {check_li("Contact migration from spreadsheets or your old system")}
      {check_li("Training for your team, in person if you're in East Tennessee")}
    </ul>

    <h2>Which CRM do you set up?</h2>
    <p>Our go-to platform is <a href="/coraline/">Coraline</a>, the all-in-one CRM we run our own business on — calls, texts, email, pipelines, and automation in one place, priced for small businesses rather than enterprise sales teams. Already on something else? If it's working, we'll build around it. If it's the reason you're reading this page, we'll move you off it carefully.</p>

    <h2>How long does implementation take?</h2>
    <p>A standard setup takes weeks, not months. We start with the piece that recovers revenue fastest — usually lead capture and missed-call text-back — so the system starts paying for itself while the rest is still being built.</p>

    <h2>Where a CRM fits in the bigger picture</h2>
    <p>A CRM catches leads; it doesn't create them. That's what your <a href="/services/web-design/">website</a>, <a href="/services/seo-aeo/">SEO</a>, and <a href="/services/digital-advertising/">ad campaigns</a> are for. And once the pipeline is full, <a href="/services/ai-implementation/">AI</a> can work it faster than any human — answering new leads in seconds and drafting follow-ups your team just approves. We build all of it, which is exactly why the pieces fit.</p>
  </div>
</section>
""" + faq_html(CRM_FAQS, "CRM questions, answered straight") + cta_band(
    "Stop losing leads you already paid for",
    "Tell us how leads reach you today and we'll show you where they're leaking — before you spend a dollar on new marketing.")

# ============================================================ AI
AI_FAQS = [
    ("Will AI make my business sound robotic?",
     "Not if it's set up right. We train it on your services, your service area, and your tone — and we cap what it's allowed to say. The goal is answers that sound like your best employee on their best day, and a handoff to a human the moment a conversation needs one."),
    ("Is AI going to replace my staff?",
     "No — it covers the hours and gaps your staff can't. Nights, weekends, the middle of a job when nobody can grab the phone. Your people still close the deals; the AI just makes sure there's a warm lead waiting instead of a cold voicemail."),
    ("What if the AI gives a customer a wrong answer?",
     "We build guardrails for exactly this. The AI only answers from information you've approved, and anything outside its lane — pricing edge cases, complaints, emergencies — gets routed to a person immediately. You review transcripts, and its answers tighten up over time."),
    ("Do we need to buy new software for this?",
     "Usually not. Most of what we implement runs inside the CRM, which you likely need anyway. If you're already set up on a platform like our own Coraline, AI is an upgrade to what you have, not another subscription to babysit."),
]

AI_BODY = f"""<section class="section">
  <div class="wrap prose">
    <h1><em>AI</em> implementation for small businesses</h1>
    {SPRINKLE}
    <p>Forget the hype for a minute. For a local business, AI is useful for one plain reason: it answers in seconds, at 2 a.m., on a Sunday, while you're on a ladder. Speed wins leads — the first business to respond usually gets the job — and AI is how a small team responds first every single time.</p>

    <h2>What can AI actually do for a local business?</h2>
    <p>Here's what we implement most, in rough order of payoff:</p>
    <ul class="checklist">
      {check_li("Answer missed calls by text, qualify the lead, and book the appointment")}
      {check_li("Reply to website chats and Facebook messages instantly, any hour")}
      {check_li("Draft follow-up texts and emails your team approves with one tap")}
      {check_li("Answer the questions you get forty times a week — hours, pricing ranges, service area")}
      {check_li("Write first-draft responses to Google reviews, good and bad")}
      {check_li("Summarize calls and conversations so nothing gets lost between shifts")}
    </ul>

    <h2>How do you implement AI without breaking what already works?</h2>
    <p>Carefully, and one piece at a time. We start with an audit of how leads and questions flow through your business today. Then we pick the one or two spots where speed is costing you money — almost always missed calls and after-hours messages — and wire AI into just those. Every assistant gets guardrails: approved answers only, human handoff on anything sensitive, and transcripts you can read. Once the first piece is earning, we add the next.</p>

    <h2>What does AI implementation cost?</h2>
    <p>Less than a part-time receptionist, which is the honest comparison. The exact number depends on how many channels and automations you want, so we quote it flat after a short call — and if your lead volume is too low for AI to matter yet, we'll tell you to spend the money on <a href="/services/digital-advertising/">ads</a> or <a href="/services/seo-aeo/">SEO</a> first.</p>

    <h2>AI works best on top of a CRM</h2>
    <p>AI needs somewhere to put the leads it catches and a record of every conversation it has. That's a <a href="/services/crm-implementation/">CRM</a> — and if you don't have one yet, we implement both together so the whole thing works on day one. It's the same pipeline your <a href="/services/web-design/">website</a> feeds.</p>
  </div>
</section>
""" + faq_html(AI_FAQS, "The AI questions every owner asks") + cta_band(
    "Find out what AI could handle for you",
    "Tell us where your team loses the most time — we'll tell you honestly whether AI can take it, and what that would cost.")

# ============================================================ ADS
ADS_FAQS = [
    ("How fast do paid ads produce leads?",
     "Days to weeks, not months — that's the point of paying for placement. Google search ads can produce calls the first week. Meta campaigns usually need two to three weeks of data before they settle in. Either way, you'll see real numbers in the first month, not promises."),
    ("Who owns the ad accounts and the data?",
     "You do. We build campaigns in accounts registered to your business, so if we ever part ways, your history, your audiences, and your results stay yours. Agencies that keep clients hostage through account ownership give this industry a bad name."),
    ("What do you charge to manage ads?",
     "A flat management fee, quoted in writing before we start. Your ad budget goes to Google and Meta, not to us — we don't skim a percentage, so we have no reason to push you to overspend."),
    ("Can you fix a campaign another agency set up?",
     "Usually, yes. We start with an audit of your existing account — often the waste is obvious within an hour: broad keywords, no negative list, conversions counted twice. You get the findings straight, even if the finding is that things look fine."),
]

ADS_BODY = f"""<section class="section">
  <div class="wrap prose">
    <h1>Google &amp; Meta ads management in <em>East Tennessee</em></h1>
    {SPRINKLE}
    <p>Paid ads are the fastest way to put your business in front of people who are ready to buy — and the fastest way to burn money if nobody's watching the account. We run Google and Meta campaigns for East Tennessee businesses with one rule: every dollar gets tracked all the way to a lead in your CRM, so "is it working?" always has a real answer.</p>

    <h2>Should you run Google Ads or Facebook ads?</h2>
    <p>Google catches people who are searching for you right now — "plumber near me", "cabin cleaning sevierville". Meta (Facebook and Instagram) puts you in front of people who weren't searching but fit your customer exactly. If the phone needs to ring this month, we usually start with Google search and add Meta retargeting so visitors who didn't call keep seeing you. If you sell something people discover rather than search for, Meta leads. On the first call we'll tell you which fits your business — it's not the same answer for everyone.</p>

    <h2>What's included in ad management?</h2>
    <ul class="checklist">
      {check_li("Keyword and audience research for your actual service area, not the whole state")}
      {check_li("Ad copy and creative written for your business, not from a template")}
      {check_li("Landing pages built to convert the click into a call or form fill")}
      {check_li("Conversion and call tracking, wired into your CRM")}
      {check_li("Negative keywords and geo-fencing so you stop paying for junk clicks")}
      {check_li("A monthly plain-English report: spend, leads, cost per lead, next moves")}
    </ul>

    <h2>How much should a local business spend on ads?</h2>
    <p>Enough to get real data, and not a dollar more until the data says so. The honest minimum varies by industry — a click costs a lot more for a Knoxville roofer than a Dandridge boutique — so we'd rather give you a real number on the call than print a fake one here. And if your budget genuinely can't buy enough clicks to matter, we'll say so and point you at <a href="/services/seo-aeo/">SEO</a> instead. Ads only work as hard as the page they land on and the follow-up behind it — which is why we also build <a href="/services/web-design/">landing pages</a> and <a href="/services/crm-implementation/">CRM pipelines</a>, and why <a href="/services/ai-implementation/">AI</a> answering your leads in seconds makes the same ad budget close more jobs.</p>
  </div>
</section>
""" + faq_html(ADS_FAQS, "Straight answers about paid ads") + cta_band(
    "Get an honest read on your ad budget",
    "Tell us your market and your monthly number. We'll tell you what it can realistically buy — even if the answer is \"don't run ads yet.\"")

# ============================================================ WEB DESIGN
WEB_FAQS = [
    ("How long does it take to build a website?",
     "Most of our local business sites go live in two to four weeks. The usual bottleneck isn't the build — it's collecting your photos, licenses, and service details. Come with those ready and the fast end of that range is realistic."),
    ("Do I own the website?",
     "On the build-and-own option, completely — the code, the content, and the domain are yours. On the monthly plan, we own the build and you're renting it, which is exactly why the monthly plan costs less up front. We'll lay out both prices and you pick."),
    ("Will my website work on phones?",
     "Yes, and it's not optional — most local searches happen on a phone, often in a parking lot. Every site we build is designed for the phone first, with a tap-to-call button that follows the visitor down the page."),
    ("I already have a website. Can you rebuild it without losing my Google rankings?",
     "Yes. We map every page and search term your current site earns before touching anything, keep or redirect every URL, and move the site only when the new one is verified. Done right, rankings recover fast and then climb — the new site is faster and better structured than what it replaced."),
]

WEB_BODY = f"""<section class="section">
  <div class="wrap prose">
    <h1>Web design for <em>local businesses</em></h1>
    {SPRINKLE}
    <p>Your website has two jobs: get found, and get the phone to ring. Pretty matters — you should be proud to put the URL on your truck — but pretty is third on the list. We hand-build fast, lean sites structured so Google can rank them, AI assistants can cite them, and a visitor on a phone in a parking lot can call you in two taps.</p>

    <h2>What makes a website actually produce leads?</h2>
    <p>Structure, mostly. A site that produces leads has a dedicated page for every service you offer and every town you serve, because Google ranks pages, not businesses. It loads in about a second, because slow sites lose phone visitors before the headline appears. It answers real questions in plain text, because that's what AI search engines quote. And every page funnels to one action: call, or fill out the form.</p>
    <ul class="checklist">
      {check_li("A page per service and per town — each one built to win its own search")}
      {check_li("Hand-written code, no page-builder bloat: sites that load in about a second")}
      {check_li("Copy written for your business, in your voice, by a human standard")}
      {check_li("Schema markup and question-structured content for Google and AI search")}
      {check_li("Forms wired straight into your CRM, tap-to-call everywhere")}
      {check_li("Hosting setup, analytics, and a preview link for every future change")}
    </ul>

    <h2>How much does a website cost?</h2>
    <p>We offer it two ways. <strong>Build and own:</strong> one project price, and the site, code, and content are yours outright. <strong>Monthly plan:</strong> a lower monthly rate that covers the build, hosting, and ongoing edits — the site is ours, the leads are yours, and you can walk away without a big sunk cost. Which one makes sense depends on your cash flow and how long you plan to keep the business; we'll price both in the quote and you choose.</p>

    <h2>A website is the foundation, not the finish line</h2>
    <p>A great site with no visitors is a billboard in the woods. Once the foundation is up, <a href="/services/seo-aeo/">monthly SEO and AEO</a> grows the searches it can win, <a href="/services/digital-advertising/">Google and Meta ads</a> buy traffic while the SEO compounds, and a <a href="/services/crm-implementation/">CRM</a> makes sure every lead the site produces gets an answer — instantly, if you add <a href="/services/ai-implementation/">AI</a>.</p>
  </div>
</section>
""" + faq_html(WEB_FAQS, "Website questions owners ask us") + cta_band(
    "Get a website quote without a sales pitch",
    "Tell us about your business and your current site, if you have one. We'll come back with both prices — build-and-own and monthly — in writing.")

# ============================================================ SEO / AEO
SEO_FAQS = [
    ("Is SEO still worth it now that people ask AI instead of Google?",
     "Yes — the work just got a second audience. AI assistants recommend businesses by reading the same web pages Google ranks; they cite sites that answer questions clearly and specifically. One well-built page now wins in both places. That's the whole idea behind AEO."),
    ("Do you guarantee first-page rankings?",
     "No, and you should hang up on anyone who does. Nobody controls Google. What we guarantee is the work: pages built and published on schedule, each one targeting a real search, with reporting that shows exactly what's moving. That's what compounds into rankings."),
    ("Why only three pages a month? Can't you build fifty?",
     "We could, and Google would ignore all fifty. Search engines penalize thin, templated pages — fifty near-duplicates hurt the whole site. Three genuinely useful pages a month, each one different enough to deserve to exist, beats bulk content every time. That's not our opinion; it's Google's published spam policy."),
    ("What's the difference between the local pack and organic results?",
     "The local pack is the map with three businesses at the top of local searches — it's driven mostly by your Google Business Profile, reviews, and proximity. Organic results are the regular listings below, driven by your website's pages. They're different games with different levers, and a serious local strategy plays both."),
]

SEO_BODY = f"""<section class="section">
  <div class="wrap prose">
    <h1>SEO and <em>AEO</em> services in East Tennessee</h1>
    {SPRINKLE}
    <p>SEO is how your business shows up when someone searches Google. AEO — answer engine optimization — is how you show up when someone asks ChatGPT or another AI assistant for a recommendation instead. Same goal, new referee. We do both at once, because the pages that win them are built the same way: specific, useful, and honest.</p>

    <h2>What is AEO, and why should you care?</h2>
    <p>AEO means structuring your website so AI assistants cite <em>you</em> when someone asks "who's a good marketing agency near Sevierville?" AI engines don't rank ten blue links — they give one answer, drawn from pages that answer questions directly and specifically. Getting into that answer is the new version of ranking first, and most of your competitors haven't even heard the term yet. Being early is the advantage.</p>

    <h2>How does the monthly program work?</h2>
    <p>You get a written content plan up front — every page we intend to build, what search it targets, and when it ships. Then, every month:</p>
    <ul class="checklist">
      {check_li("Three new pages: town pages for the places you serve, and guides that answer the questions your customers actually ask")}
      {check_li("Every page written from scratch — no swapped-city-name templates, ever")}
      {check_li("You review each page on a private preview link before it goes live")}
      {check_li("Sitemap, internal links, and AI-crawler files updated with every release")}
      {check_li("A plain-English monthly report: what shipped, what's ranking, what's next")}
    </ul>

    <h2>How long until SEO produces leads?</h2>
    <p>Months, not days — usually three to six before the movement is obvious, faster in small-town markets like Dandridge and slower in crowded ones like <a href="/service-areas/knoxville/">Knoxville</a>. That runway is exactly why the roadmap exists: you can see the work compounding page by page instead of taking it on faith. Need the phone ringing before then? That's the case for running <a href="/services/digital-advertising/">ads</a> alongside — paid traffic now, free traffic forever after.</p>

    <h2>It starts with the site under the SEO</h2>
    <p>Publishing great pages on a slow, tangled website is pouring good water into a cracked well. If your current site can't support the program, we'll tell you before taking your money — <a href="/services/web-design/">rebuilding the foundation</a> first is cheaper than paying for SEO that can't work. And every lead the rankings produce should land in a <a href="/services/crm-implementation/">CRM</a>, or you're winning searches just to lose the follow-up.</p>
  </div>
</section>
""" + faq_html(SEO_FAQS, "SEO and AEO, without the snake oil") + cta_band(
    "See what searches you're missing",
    "Tell us your business and your towns. We'll look at what your customers search for, what you currently win, and send back the honest gap.")

# ============================================================ SERVICE AREAS HUB
AREAS_BODY = f"""<section class="section">
  <div class="wrap">
    <div class="section-head">
      <h1>Serving East Tennessee, <em>from Kodak out</em></h1>
      {SPRINKLE}
      <p>Salt Services is based in Kodak, right where Sevier, Knox, and Jefferson counties meet — which puts most of East Tennessee within a half-hour handshake. Websites and SEO work travels anywhere, but this is home, and these are the markets we know street by street.</p>
    </div>
    <ul class="card-grid two">
      <li class="card">{icon('map')}
        <h3>Sevierville</h3>
        <p>Parkway retail, cabin companies, and the local businesses that serve Sevier County year-round — fifteen minutes from our door.</p>
        <a class="card-link" href="/service-areas/sevierville/">Marketing in Sevierville &rsaquo;</a>
      </li>
      <li class="card">{icon('map')}
        <h3>Knoxville</h3>
        <p>The big market. More customers, more competition — and more reward for businesses that get specific about who they serve.</p>
        <a class="card-link" href="/service-areas/knoxville/">Marketing in Knoxville &rsaquo;</a>
      </li>
    </ul>
    <div class="prose" style="margin-top:2rem">
      <h2>Also serving</h2>
      <p>Pigeon Forge, Gatlinburg, Maryville, Dandridge, Seymour, Jefferson City, Newport, and the rest of East Tennessee. Dedicated pages for these towns are on the way as part of our own monthly content program — the same one we <a href="/services/seo-aeo/">sell to clients</a>, practiced on ourselves. Don't see your town? <a href="/contact/">We almost certainly still serve it.</a></p>
    </div>
  </div>
</section>
""" + cta_band("Closer than you think",
               f"If you're anywhere in East Tennessee, we'll meet you at your shop, your job site, or a coffee shop in between. Call {PHONE} or start below.")

# ============================================================ SEVIERVILLE
SEV_FAQS = [
    ("Can you help my cabin rental company compete with the big booking sites?",
     "On the head terms — \"gatlinburg cabin rentals\" — honestly, no one outranks the giants quickly. But travelers also search specific things the big sites answer badly: pet-friendly cabins with fenced yards, cabins near a specific attraction, midweek winter deals. We win you those searches, then use your CRM to turn one-time guests into direct repeat bookings that pay no commission."),
    ("Do tourists actually use AI to plan Sevierville trips?",
     "More every season. People ask ChatGPT things like \"best pancakes in Sevierville\" or \"what should we do with kids near Dollywood?\" — and the AI answers by citing websites that answer clearly. Getting your business into those answers is exactly what our AEO work does."),
    ("My shop depends on foot traffic from the Parkway. Why do I need a website?",
     "Because the decision happens before the drive. Visitors plan from the cabin the night before — searching, checking maps, reading reviews. A thin web presence means you've lost them before they ever hit traffic. Your site and Google profile are the sign they see first."),
    ("Will you actually come to Sevierville, or is everything over Zoom?",
     "We'll be there in about fifteen minutes — Kodak is just up Highway 66. First meetings usually happen at your business, because seeing how customers actually reach you tells us more than any form."),
]

SEV_BODY = f"""<section class="section">
  <div class="wrap prose">
    <h1>Marketing agency serving <em>Sevierville, TN</em></h1>
    {SPRINKLE}
    <p>Sevierville sits in a strange, wonderful market: a county seat of under twenty thousand people that hosts millions of visitors a year on their way to Pigeon Forge, Gatlinburg, and the Smokies. That means two completely different customers — tourists planning from a cabin or a couch three states away, and locals who live here year-round — and most Sevierville businesses need to win both. We're fifteen minutes up Highway 66 in Kodak, and this is the market we know best.</p>

    <h2>Marketing to tourists is a different sport</h2>
    <p>Tourist money is searched for in advance. Families pick restaurants, attractions, and outfitters from the cabin the night before — on their phones, on Google Maps, and increasingly by just asking an AI assistant. Winning that moment takes a fast website that answers specific questions, a Google Business Profile with fresh reviews, and ads timed to the seasons — dialed up for summer and the fall color rush, trimmed back in the January lull. We build all three to work together, and we track it to actual calls and bookings, not clicks.</p>

    <h2>The year-round Sevierville economy matters just as much</h2>
    <p>Behind the Parkway there's a whole county of HVAC companies, dentists, realtors, landscapers, and shops that serve people who live here. For them the game is local search: showing up when somebody in a Sevierville zip code searches for what you do, answering the phone when they call, and following up when you can't. That's website, <a href="/services/seo-aeo/">SEO</a>, <a href="/services/crm-implementation/">CRM</a>, and <a href="/services/ai-implementation/">AI</a> working as one pipeline — our whole catalog, pointed at your block.</p>

    <h2>What we do for Sevierville businesses</h2>
    <ul class="checklist">
      {check_li("Websites built to win both tourist searches and local ones")}
      {check_li("Google and Meta ads with seasonal budgets that match visitor flow")}
      {check_li("AEO so AI trip-planners cite your business, not just the big aggregators")}
      {check_li("CRM and AI follow-up, because a lead answered in seconds books; one answered tomorrow already booked elsewhere")}
    </ul>
    <p>We serve all of Sevier County from here — <a href="/service-areas/">Pigeon Forge, Gatlinburg, Seymour</a>, and the communities between.</p>
  </div>
</section>
""" + faq_html(SEV_FAQS, "Sevierville questions we get asked") + cta_band(
    "Talk to a marketing team fifteen minutes away",
    "Tell us about your Sevierville business and we'll come back with a plan built for this market — tourist season, off season, and everything between.")

# ============================================================ KNOXVILLE
KNOX_FAQS = [
    ("Can a small business actually rank in a market as big as Knoxville?",
     "Yes — by refusing to compete for the whole city at once. \"Plumber Knoxville\" is a bloodbath, but \"tankless water heater installation Farragut\" is winnable in months. We stack up the specific wins — by neighborhood, by service, by question — until the broad terms start following. That's how small sites beat big budgets."),
    ("Knoxville has dozens of agencies. Why hire one from Kodak?",
     "Because at a lot of established agencies, a small business gets the junior team and the recycled strategy. We're young, we're twenty-five minutes east, and your account is genuinely important to us — the people you meet are the people doing the work. Ask any agency you're comparing: who, specifically, will touch my campaigns?"),
    ("How expensive are Google Ads in Knoxville?",
     "Meaningfully pricier than in the surrounding counties — legal, HVAC, and roofing clicks especially can run to painful numbers. That's not a reason to skip ads; it's a reason tracking matters more. When a click costs that much, knowing which keywords produce actual booked jobs is the whole game."),
    ("Do you work with businesses in Knoxville's suburbs?",
     "All of them — Farragut, Powell, Halls, Karns, Hardin Valley, and out to Maryville and Oak Ridge. Suburb-level targeting is usually where we start anyway, because that's where the winnable searches are."),
]

KNOX_BODY = f"""<section class="section">
  <div class="wrap prose">
    <h1>Digital marketing for <em>Knoxville</em> businesses</h1>
    {SPRINKLE}
    <p>Knoxville is where East Tennessee's customers are — nearly a million people across the metro — and where its competition is. You're not up against four other plumbers like you would be in Dandridge; you're up against fifty, plus the private-equity rollups with billboards on I-40. Competing here on volume is a rich company's game. Competing on <em>specificity</em> is ours.</p>

    <h2>How a small business wins in a big market</h2>
    <p>You stop trying to be "the best in Knoxville" and start being the obvious choice for something narrower: a neighborhood, a service, a customer type. Search engines and AI assistants both reward the site that most precisely matches what was asked. A remodeler who owns "kitchen remodel Hardin Valley" beats a giant's generic page for that search every time — and twenty of those wins add up to a full calendar. That's the strategy we execute: page by page, suburb by suburb, question by question.</p>

    <h2>Everything gets measured, because everything here costs more</h2>
    <p>Knoxville clicks are expensive and Knoxville SEO takes longer — which makes flying blind the one unaffordable strategy. Every campaign we run is wired for tracking end to end:</p>
    <ul class="checklist">
      {check_li("Call tracking and form tracking on every campaign, tied to your CRM")}
      {check_li("Neighborhood-level ad targeting — Bearden is not Powell is not Farragut")}
      {check_li("Landing pages per service and suburb, not one generic page for the metro")}
      {check_li("Monthly reporting that names the number that matters: cost per booked job")}
    </ul>

    <h2>The follow-up edge is bigger in Knoxville</h2>
    <p>When a customer has fifty choices, they don't wait for a callback — they just dial the next listing. Speed is the cheapest advantage in a crowded market: a <a href="/services/crm-implementation/">CRM</a> that catches every lead and <a href="/services/ai-implementation/">AI</a> that responds in seconds means you win the jobs your slower competitors already paid to attract. Pair that with a <a href="/services/web-design/">site built to convert</a> and <a href="/services/seo-aeo/">content that compounds</a>, and the size of the market starts working for you instead of against you.</p>
  </div>
</section>
""" + faq_html(KNOX_FAQS, "Knoxville marketing, asked and answered") + cta_band(
    "Bring us your Knoxville market and we'll find the gap",
    "Tell us your industry and your part of town. We'll come back with the specific searches and neighborhoods we'd attack first — that plan is free either way.")

# ============================================================ CORALINE
CORALINE_CHECKOUT = "https://coraline.saltservicesusa.com"

CORALINE_FAQS = [
    ("Do I have to set Coraline up myself?",
     "No — that's the point of buying it from us. Every Coraline plan can come with our implementation: pipelines built for how you sell, your contacts migrated, automations wired, and your team trained. You log in to a working system, not an empty one."),
    ("Do I need Coraline to work with Salt Services?",
     "No. Our web design, SEO, and advertising work stands on its own. Coraline is simply the platform we recommend when a client needs a CRM, because it's the one we run our own business on and can support the deepest."),
    ("What's actually different between the three plans?",
     "Starter is the full core platform for a single account. Unlimited removes the ceilings — unlimited contacts and users — and adds a branded desktop app. Pro adds the operator tools: email, phone, and text rebilling, split testing, agent reporting, and advanced API access."),
    ("Will Coraline work with my existing website?",
     "Yes. Coraline's forms, chat, and booking calendars embed into any site — including sites we didn't build. If we built yours, the wiring is already our standard practice."),
]

CORALINE_BODY = f"""<section class="hero">
  <div class="wrap">
    <span class="hero-kicker">Coraline &middot; the platform behind our client work</span>
    <h1>One login for your <span class="accent">whole</span> pipeline.</h1>
    {SPRINKLE}
    <p class="lead">Coraline is the all-in-one CRM and marketing platform we run our own business on and implement for clients: lead capture, pipelines, booking, text and email automation, and an AI conversation bot — in one place, priced for small businesses.</p>
    <p>
      <a class="btn btn-accent" href="{CORALINE_CHECKOUT}">Sign up for Coraline</a>
      <a class="btn btn-ghost" href="/contact/#form">Talk to us first</a>
    </p>
    <p class="hero-note">Not sure which plan fits? Start with the form and we'll tell you honestly — including if the answer is the cheapest one.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <h2>What's inside</h2>
      {SPRINKLE}
      <p>Most businesses run this stack as four or five separate subscriptions that don't talk to each other. Coraline is the same stack as one system.</p>
    </div>
    <ul class="card-grid">
      <li class="card">{icon('crm')}
        <h3>Leads &amp; pipelines</h3>
        <p>Every lead from your website, ads, and Google profile lands in one pipeline — tracked from first contact to closed job.</p>
      </li>
      <li class="card">{icon('ads')}
        <h3>Marketing automation</h3>
        <p>Text and email follow-up sequences, review requests, and appointment reminders that run themselves.</p>
      </li>
      <li class="card">{icon('map')}
        <h3>Online booking</h3>
        <p>Calendars your customers book directly, synced to your team, with reminders that cut no-shows.</p>
      </li>
      <li class="card">{icon('ai')}
        <h3>AI conversation bot</h3>
        <p>Answers missed calls and website chats in seconds, qualifies the lead, and books the appointment — with a human handoff.</p>
      </li>
      <li class="card">{icon('web')}
        <h3>Website &amp; funnel builder</h3>
        <p>Landing pages and funnels with split testing on the Pro plan — or keep the site you have and just embed the forms.</p>
      </li>
      <li class="card">{icon('seo')}
        <h3>Reporting</h3>
        <p>Contact management, social calendar, agent reporting, and API access — so you can see what's working without exporting spreadsheets.</p>
      </li>
    </ul>
  </div>
</section>

<section class="section section-alt">
  <div class="wrap">
    <div class="section-head">
      <h2>Plans and pricing</h2>
      {SPRINKLE}
      <p>Flat monthly pricing, no per-seat surprises. Every plan links to the same secure checkout.</p>
    </div>
    <ul class="card-grid">
      <li class="card price-card">
        <h3>Starter</h3>
        <p class="price-tag">$197<span class="per">/month</span></p>
        <p class="price-note">The core platform, single account.</p>
        <ul class="checklist">
          {check_li("Lead capture, pipelines, and contact management")}
          {check_li("Text and email marketing automation")}
          {check_li("Online booking and calendars")}
          {check_li("Website and funnel builder")}
        </ul>
        <a class="btn btn-navy" href="{CORALINE_CHECKOUT}">Choose Starter</a>
      </li>
      <li class="card price-card price-featured">
        <span class="price-badge">Our recommendation</span>
        <h3>Unlimited</h3>
        <p class="price-tag">$297<span class="per">/month</span></p>
        <p class="price-note">Everything in Starter, without ceilings.</p>
        <ul class="checklist">
          {check_li("Unlimited contacts and users")}
          {check_li("Branded desktop app on your own domain")}
          {check_li("Everything in Starter, unrestricted")}
        </ul>
        <a class="btn btn-accent" href="{CORALINE_CHECKOUT}">Choose Unlimited</a>
      </li>
      <li class="card price-card">
        <h3>Pro</h3>
        <p class="price-tag">$497<span class="per">/month</span></p>
        <p class="price-note">Everything in Unlimited, plus operator tools.</p>
        <ul class="checklist">
          {check_li("Email, phone, and text rebilling")}
          {check_li("Split testing and agent reporting")}
          {check_li("Advanced API access")}
        </ul>
        <a class="btn btn-navy" href="{CORALINE_CHECKOUT}">Choose Pro</a>
      </li>
    </ul>
  </div>
</section>

<section class="section">
  <div class="wrap prose">
    <h2>Software plus the people who set it up</h2>
    {SPRINKLE}
    <p>Plenty of platforms can do what Coraline does on paper. What makes it work in practice is implementation — and that's the difference between buying Coraline from a website and buying it from us. We <a href="/services/crm-implementation/">build your pipelines, migrate your contacts, and train your team</a>, wire in <a href="/services/ai-implementation/">AI that answers in seconds</a>, and stay fifteen minutes away when you'd rather talk across a table. The software comes with a team.</p>
  </div>
</section>
""" + faq_html(CORALINE_FAQS, "Coraline questions, answered") + cta_band(
    "Ready to run your business from one login?",
    f"Sign up and we'll take it from there — or call {PHONE} and we'll help you pick a plan.",
    "Sign up for Coraline", CORALINE_CHECKOUT)

# ============================================================ OUR WORK
def work_entry(href, img, alt, name, blurb):
    return f"""<li class="card work-card">
        <a href="{href}" target="_blank" rel="noopener">
          <img src="/images/work/{img}.webp" alt="{alt}" width="640" height="400" loading="lazy">
          <div class="work-body">
            <h3>{name}</h3>
            <p>{blurb}</p>
            <span class="card-link">Visit the live site &rsaquo;</span>
          </div>
        </a>
      </li>"""

WORK_ENTRIES = "".join([
    work_entry("https://americanfireplaces.vercel.app/", "american-fireplaces",
        "American Fireplaces website — dark, ember-lit hero reading 'Gather around something extraordinary'",
        "American Fireplaces",
        "A Sevierville hearth showroom that has warmed the Smokies since 1990 needed a site that felt like standing in front of one of their fireplaces. We built a cinematic brand experience — ember particles included — around their story, their process, and their brands."),
    work_entry("https://www.mtnlandscapers.com/", "mountain-landscapers",
        "Mountain Landscapers website — deep green hero with serif headline 'Landscaping Sevierville'",
        "Mountain Landscapers",
        "Landscape design, hardscapes, and grounds care for the Smoky Mountain foothills. The site is organized page by page around the searches Sevier County homeowners actually type, from retaining walls to outdoor living."),
    work_entry("https://downtown-river-rentals.vercel.app/", "downtown-river-rentals",
        "Downtown River Rentals website — cottage porch photo under 'Vacation Homes in Pigeon Forge'",
        "Downtown River Rentals",
        "Vacation cottages a short walk from the Pigeon Forge Parkway. The site has one job: direct bookings that skip the booking platforms and their commission."),
    work_entry("https://www.ahappyhost.com/", "a-happy-host",
        "A Happy Host website — concierge services hero for short-term rental owners",
        "A Happy Host",
        "A services hub for the short-term rental owners who keep the Smokies' cabins running — cleaning, concierge, and project work, presented so owners can act fast."),
    work_entry("https://smoky-mountain-espresso.vercel.app/", "smoky-mountain-espresso",
        "Smoky Mountain Espresso website — warm coffee shop home page for Sevierville",
        "Smoky Mountain Espresso",
        "A Sevierville coffee shop with regulars to match. Fast, warm, and built to show up when travelers on the Parkway corridor search for coffee worth stopping for."),
    work_entry("https://www.cpaservicessevierville.com/", "sevier-cpas",
        "Sevier CPAs website — courthouse photo behind 'Local CPA and Accounting Services here in Sevierville'",
        "Sevier CPAs",
        "Tax prep, bookkeeping, and accounting for Sevier County. Professional-services sites live or die on trust, so this one leads with credentials, clarity, and a straight path to a conversation."),
    work_entry("https://www.colorteccoatings.com/", "colortec-coatings",
        "Colortec Powder Coating website — technician spraying a part in the coating booth",
        "Colortec Powder Coating",
        "Sandblasting and powder coating out of Sevierville, serving everyone from gearheads with a single part to industrial contractors with a full run. A working site for a working shop."),
])

WORK_LD = {
    "@context": "https://schema.org",
    "@type": "ItemList",
    "name": "Client websites built by Salt Services",
    "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "url": u}
        for i, (n, u) in enumerate([
            ("American Fireplaces", "https://americanfireplaces.vercel.app/"),
            ("Mountain Landscapers", "https://www.mtnlandscapers.com/"),
            ("Downtown River Rentals", "https://downtown-river-rentals.vercel.app/"),
            ("A Happy Host", "https://www.ahappyhost.com/"),
            ("Smoky Mountain Espresso", "https://smoky-mountain-espresso.vercel.app/"),
            ("Sevier CPAs", "https://www.cpaservicessevierville.com/"),
            ("Colortec Powder Coating", "https://www.colorteccoatings.com/"),
        ])
    ],
}

WORK_BODY = f"""<section class="section">
  <div class="wrap">
    <div class="section-head">
      <h1>Our work, live and <em>clickable</em></h1>
      {SPRINKLE}
      <p>Every site below belongs to a real client and is live right now — click through and judge for yourself. Most are here in Sevier County, because that's home turf; we build for clients well beyond it too.</p>
    </div>
    <ul class="card-grid two">
      {WORK_ENTRIES}
    </ul>
  </div>
</section>

<section class="section section-alt">
  <div class="wrap prose">
    <h2>How these sites get built</h2>
    {SPRINKLE}
    <p>Every one of them follows the same playbook we'd use for you: hand-built code that loads fast, a page for every service and town that matters, copy written in the owner's voice, and structure that Google can rank and AI assistants can cite. The details are on our <a href="/services/web-design/">web design</a> and <a href="/services/seo-aeo/">SEO &amp; AEO</a> pages.</p>
    <p>And a promise about this page: as our monthly SEO program stacks up real rankings data for these clients, these entries will grow into full case studies with numbers — searches won, calls produced. We'd rather show you results than adjectives, and we'd rather wait for real ones than invent them.</p>
  </div>
</section>
""" + cta_band("Want yours on this page?",
               f"Tell us about your business and we'll show you exactly what we'd build — and what it would take to rank. Or call {PHONE}.")

# ============================================================ ABOUT
ABOUT_BODY = f"""<section class="section">
  <div class="wrap prose">
    <h1>The <em>story</em> behind Salt Services</h1>
    {SPRINKLE}
    <p>Salt Services started with something our founder noticed growing up in an entrepreneurial family: the businesses that marketed themselves grew, and the ones that didn't — even the genuinely better ones — stayed stuck. The good-at-the-work business losing to the good-at-being-found business never sat right. Salt Services exists to fix that mismatch for small businesses in East Tennessee.</p>
    <!-- TODO: founder name, photo, and year founded — awaiting owner confirmation -->

    <h2>Why "Salt"?</h2>
    <p>The name comes from Matthew 5:13 — <em>"You are the salt of the earth."</em> Salt preserves, seasons, and makes people thirsty; it changes everything it touches, in small amounts. That's the job description: we're not the meal, we're what makes your business impossible to overlook. It's also a daily reminder of the standard we're held to — be genuinely useful, or be nothing.</p>

    <h2>Young company, and honest about it</h2>
    <p>We won't pretend to be a decades-old firm with a skyscraper office. We're a young agency, and that's precisely the deal: you get people with something to prove, working with current tools instead of habits from 2015, on an account that genuinely matters to their future. Every client we take on is a reference we can't afford to lose. Established agencies sell you their track record; we're building ours on your results.</p>

    <h2>What we believe about this work</h2>
    <ul class="checklist">
      {check_li("Straight answers beat impressive ones — if something won't work for your budget, we say so")}
      {check_li("Everything gets measured, and you see the numbers we see")}
      {check_li("One team building one pipeline beats five vendors pointing at each other")}
      {check_li("Show up in person — East Tennessee business still runs on handshakes")}
    </ul>
    <p>The tools we use on ourselves are the ones we sell: this website is built exactly the way we <a href="/services/web-design/">build client sites</a>, and our own leads run through the same <a href="/services/crm-implementation/">CRM</a> and <a href="/services/ai-implementation/">AI follow-up</a> we implement for you. If you fill out our form, you'll experience the product before you buy it.</p>
  </div>
</section>
""" + cta_band("Put us to work proving ourselves",
               f"Tell us what you're trying to grow. We'll show you exactly how we'd help — and you'll keep the plan whether you hire us or not.")

# ============================================================ CONTACT
CONTACT_BODY = f"""<section class="section">
  <div class="wrap">
    <div class="section-head">
      <h1>Let's talk about <em>growing</em> your business</h1>
      {SPRINKLE}
      <p>Three ways to reach us — pick whichever you'd actually use. The form gives us the most to work with, so if you want a real plan on the first call, start there.</p>
    </div>
    <ul class="card-grid">
      <li class="card">
        <h3>Call</h3>
        <p><a href="tel:{TEL}">{PHONE}</a></p>
        <p>Weekdays, Eastern time. If we're with a client, leave a message — we return calls the same business day.</p>
      </li>
      <li class="card">
        <h3>Email</h3>
        <p><a href="mailto:{BIZ['email']}">{BIZ['email']}</a></p>
        <p>Good for sending over existing logins, screenshots of your current setup, or questions you want answered in writing.</p>
      </li>
      <li class="card">
        <h3>Visit</h3>
        <p>Based in Kodak, TN.</p>
        <p>We come to you — your shop, your job site, or a halfway coffee shop anywhere in East Tennessee.</p>
      </li>
    </ul>
  </div>
</section>
""" + coraline_section(
    "The inquiry form — two minutes, zero obligation",
    "Answer a few questions about your business and your goals. We'll review your web presence and your market before we ever get on the phone, so the first conversation is already about specifics.",
    aside="""<h3>What happens after you submit</h3>
      <ol>
        <li><strong>A real person reads it</strong> — usually the same day.</li>
        <li><strong>We do our homework:</strong> your current site, your Google profile, your competition, what your customers search for.</li>
        <li><strong>You get a call and a flat written quote.</strong> Not the right fit? We'll say so, and tell you what to do anyway. The plan is yours to keep either way.</li>
      </ol>
      <p class="aside-note">We work with businesses across <a href="/service-areas/sevierville/">Sevierville</a>, <a href="/service-areas/knoxville/">Knoxville</a>, and the rest of <a href="/service-areas/">East Tennessee</a>.</p>""")

# ============================================================ LEGAL PAGES
PRIVACY_BODY = f"""<section class="section">
  <div class="wrap prose">
    <h1>Privacy policy</h1>
    {SPRINKLE}
    <p><em>Effective July 18, 2026</em></p>
    <p>This policy describes how Salt Services ("we," "us"), a marketing agency based in Kodak, Tennessee, collects and uses information through saltservicesusa.com and our related services. Short version: we collect what you send us so we can respond and do our work, we don't sell it, and we don't share your mobile number with anyone for their marketing.</p>

    <h2>Information you give us</h2>
    <p>When you fill out a form, start a chat, call, email, or sign up for Coraline, you may provide your name, email address, phone number, business name, address, and details about your business and goals. We use this to respond to you, prepare recommendations and quotes, provide services you've engaged us for, and communicate with you about them.</p>

    <h2>Information collected automatically</h2>
    <p>Like nearly every website, our hosting provider (Vercel) keeps standard server logs, which include IP addresses, browser type, and pages requested. Our chat and form widgets (provided by our CRM platform) may set functional cookies so a conversation can continue across pages. We do not currently run advertising trackers or third-party ad pixels on this site. Fonts and a graphics library are loaded from content-delivery networks (Google Fonts, jsDelivr), which receive your IP address as a technical necessity of serving the files.</p>

    <h2>Text messaging (SMS) terms</h2>
    <p>If you provide your phone number, you consent to receive calls and text messages from us about your inquiry and our services. Message frequency varies; message and data rates may apply. Reply STOP at any time to opt out of texts, or HELP for help. <strong>No mobile information will be shared with third parties or affiliates for marketing or promotional purposes.</strong> Opt-in data and consent are not shared with any third party.</p>

    <h2>How we share information</h2>
    <p>We share information only with service providers who help us operate — our CRM and communications platform (Coraline, built on LeadConnector/HighLevel infrastructure), our hosting provider (Vercel), and similar processors bound to use it only on our behalf — or when the law requires it, or as part of a business transfer. We do not sell personal information, and we do not share it with anyone for their own marketing.</p>

    <h2>Cookies and your choices</h2>
    <p>The cookies on this site are functional (chat and form continuity), not advertising cookies. You can block or delete cookies in your browser settings; the site will still work, though chat conversations may not persist across visits.</p>

    <h2>Retention and security</h2>
    <p>We keep contact and client records for as long as we have a business need — responding to your inquiry, serving you as a client, and meeting our legal and accounting obligations — and we use reasonable technical and organizational safeguards to protect them. No method of transmission or storage is completely secure, and we can't guarantee absolute security.</p>

    <h2>Children</h2>
    <p>This site is for businesses and is not directed to children under 13. We do not knowingly collect personal information from children.</p>

    <h2>Your rights</h2>
    <p>You may request a copy of the personal information we hold about you, ask us to correct it, or ask us to delete it, by emailing <a href="mailto:{BIZ['email']}">{BIZ['email']}</a> or calling <a href="tel:{TEL}">{PHONE}</a>. We honor such requests regardless of where you live, subject to records we're required to keep.</p>

    <h2>Third-party links</h2>
    <p>Our site links to other websites — including client websites in our portfolio and the Coraline sign-up service — which have their own privacy practices. This policy covers only saltservicesusa.com.</p>

    <h2>Changes and contact</h2>
    <p>If we change this policy, we'll update it here with a new effective date. Questions: <a href="mailto:{BIZ['email']}">{BIZ['email']}</a>, <a href="tel:{TEL}">{PHONE}</a>, Salt Services, Kodak, TN.</p>
  </div>
</section>
"""

TERMS_BODY = f"""<section class="section">
  <div class="wrap prose">
    <h1>Terms of service</h1>
    {SPRINKLE}
    <p><em>Effective July 18, 2026</em></p>
    <p>These terms govern your use of saltservicesusa.com and set the baseline for how Salt Services ("we," "us") does business. By using this site, you accept them. If you sign a service agreement or proposal with us, that signed document controls wherever it differs from these terms.</p>

    <h2>What we do</h2>
    <p>Salt Services provides marketing services — website design, SEO and AEO, digital advertising management, CRM implementation, and AI implementation — and offers subscriptions to Coraline, our CRM and marketing platform. The specifics of any engagement (scope, price, timeline, deliverables) are defined in the written quote or agreement for that engagement, not on this website.</p>

    <h2>No guarantee of results</h2>
    <p>Marketing outcomes depend on factors nobody fully controls — search engines change algorithms, advertising costs fluctuate, markets shift. We commit to doing the work we agree to, skillfully and on schedule. We do not guarantee specific rankings, traffic, lead volume, or revenue, and nothing on this site is a promise of specific results. Examples of client work shown on this site illustrate what we build; every business and market is different.</p>

    <h2>Coraline subscriptions</h2>
    <p>Coraline plans are billed as described at sign-up through our checkout at coraline.saltservicesusa.com. The pricing, billing cycle, and cancellation terms presented at checkout govern your subscription. Coraline is built on third-party infrastructure, and its availability depends in part on those providers; we'll always do our part to keep your account running and your data accessible.</p>

    <h2>Intellectual property</h2>
    <p>The content of this website — text, design, graphics, and code — belongs to Salt Services and may not be copied for commercial use without permission. Ownership of client deliverables (websites, content, campaigns) is defined in each client's agreement. Client names and screenshots shown in our portfolio are used to describe our own work; the underlying businesses and their trademarks belong to their owners.</p>

    <h2>Acceptable use</h2>
    <p>Don't misuse this site: no attempts to breach security, scrape at abusive volume, submit forms with false identities, or use our contact channels to spam us or others. AI systems are welcome to read and cite this site; that's what it's for.</p>

    <h2>Disclaimers and limitation of liability</h2>
    <p>This website and its content are provided "as is," without warranties of any kind, express or implied, including fitness for a particular purpose. To the maximum extent permitted by law, Salt Services will not be liable for indirect, incidental, consequential, or punitive damages arising from your use of this site, and our total liability arising out of any engagement is limited to the amounts you paid us for that engagement in the twelve months before the claim arose. Some jurisdictions don't allow certain limitations, so parts of this section may not apply to you.</p>

    <h2>Indemnification</h2>
    <p>If you use our site or services in violation of these terms or the law and it gets us sued, you agree to defend and indemnify us against the resulting claims and costs.</p>

    <h2>Governing law and disputes</h2>
    <p>These terms are governed by the laws of the State of Tennessee, without regard to conflict-of-law rules. Any dispute arising from these terms or your use of this site will be brought in the state or federal courts serving Sevier County, Tennessee, and you consent to their jurisdiction. Before either of us files anything, we agree to try first to resolve the dispute with a direct, good-faith conversation — it's cheaper and it usually works.</p>

    <h2>Changes and contact</h2>
    <p>We may update these terms; the version posted here with the latest effective date is the one in force. If any provision is found unenforceable, the rest remain in effect. Questions: <a href="mailto:{BIZ['email']}">{BIZ['email']}</a>, <a href="tel:{TEL}">{PHONE}</a>, Salt Services, Kodak, TN.</p>
  </div>
</section>
"""

A11Y_BODY = f"""<section class="section">
  <div class="wrap prose">
    <h1>Accessibility statement</h1>
    {SPRINKLE}
    <p><em>Last reviewed July 18, 2026</em></p>
    <p>Salt Services wants every visitor to be able to use this website, including people who rely on assistive technology. We build toward the Web Content Accessibility Guidelines (WCAG) 2.1 Level AA and treat accessibility as part of construction, not an add-on.</p>

    <h2>What we've built in</h2>
    <ul class="checklist">
      {check_li("Color contrast at or above the 4.5:1 AA standard, verified programmatically for every text/background pair")}
      {check_li("Full keyboard navigation with visible focus indicators and a skip-to-content link")}
      {check_li("Semantic HTML landmarks, one heading hierarchy per page, and descriptive alt text on images")}
      {check_li("Motion respect: animations, the 3D home graphic, and the custom cursor all disable automatically for visitors with reduced-motion enabled")}
      {check_li("Readable defaults: 17px base text, generous line height, no text locked inside images")}
      {check_li("Touch targets sized for real hands, and a layout tested from 320px phones to large desktops")}
    </ul>

    <h2>Known limitations</h2>
    <p>Our contact form and chat are provided by a third-party platform and load inside their own frames; we've configured them for accessibility but don't control every detail of their markup. If either gives you trouble, every page lists our phone and email — you'll reach the same people either way.</p>

    <h2>Tell us if something's in your way</h2>
    <p>If any part of this site is difficult for you to use, we want to know and we'll fix what we can, promptly. Call <a href="tel:{TEL}">{PHONE}</a> or email <a href="mailto:{BIZ['email']}">{BIZ['email']}</a> and tell us what happened and what browser or assistive technology you were using.</p>
  </div>
</section>
"""

# ============================================================ FORM COMPLETION (thank-you)
FORM_DONE_BODY = f"""<section class="hero">
  <div class="wrap">
    <span class="hero-kicker">Inquiry received &middot; you're in the pipeline</span>
    <h1>Got it — you're <span class="accent">in</span>.</h1>
    {SPRINKLE}
    <p class="lead">Your inquiry just landed in our CRM — the same kind we build for clients, so you're already watching the product work. A real person reads it today, does their homework on your business and your market, and comes back to you with a real plan.</p>
    <p>
      <a class="btn btn-accent" href="tel:{TEL}">Skip the line — call {PHONE} now</a>
      <a class="btn btn-ghost" href="/work/">Browse our work while you wait</a>
    </p>
    <p class="hero-note">Seriously — if you'd rather talk right now, call. Mention you just sent the form and we'll pull it up while we're on the phone.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <h2>What happens next</h2>
      {SPRINKLE}
    </div>
    <ul class="card-grid">
      <li class="card">
        <span class="step-num" aria-hidden="true">01</span>
        <h3>Today: a human reads it</h3>
        <p>Not an autoresponder — a person. Your inquiry gets eyes on it the same business day it arrives.</p>
      </li>
      <li class="card">
        <span class="step-num" aria-hidden="true">02</span>
        <h3>We do our homework</h3>
        <p>Your current website, your Google profile, your competition, and what your customers actually search for — so the first call is about specifics, not introductions.</p>
      </li>
      <li class="card">
        <span class="step-num" aria-hidden="true">03</span>
        <h3>You get a plan and a price</h3>
        <p>A call to walk through what we found, what we'd do, and a flat written quote. The plan is yours to keep whether or not you hire us.</p>
      </li>
    </ul>
  </div>
</section>
""" + cta_band("Curious what you just signed up for?",
               "Poke around while you wait — the services, the platform, the story behind the salt.",
               "See how we work", "/services/")

# ============================================================ 404
NOTFOUND_BODY = f"""<section class="section">
  <div class="wrap prose">
    <h1>This page <em>wandered off</em> the trail</h1>
    {SPRINKLE}
    <p>The address you followed doesn't exist on our site — the page may have moved, or the link had a typo. No harm done. Here's where you probably meant to go:</p>
    <ul>
      <li><a href="/">Home</a></li>
      <li><a href="/services/">Our services</a> — web design, SEO &amp; AEO, advertising, CRM, and AI</li>
      <li><a href="/service-areas/">Service areas</a> — Sevierville, Knoxville, and East Tennessee</li>
      <li><a href="/contact/">Contact us</a></li>
    </ul>
    <p>Or skip the clicking: call <a href="tel:{TEL}">{PHONE}</a> and just ask.</p>
  </div>
</section>
"""

# ============================================================ PAGE SPECS
PAGES = [
    {
        "path": "/", "nav": "home",
        "title": "Salt Services | Marketing & AI Agency in Kodak, TN",
        "desc": "Marketing and AI implementation for East Tennessee small businesses — websites, Google & Meta ads, CRM, SEO and AEO. Call (866) 721-7258.",
        "jsonld": [faq_ld(HOME_FAQS)],
        "body": HOME_BODY,
    },
    {
        "path": "/services/", "nav": "services",
        "title": "Marketing Services for Local Businesses | Salt Services",
        "desc": "CRM implementation, AI, Google & Meta ads, web design, and SEO/AEO — five services that work as one lead pipeline for East Tennessee businesses.",
        "crumbs": [["Home", "/"], ["Services", "/services/"]],
        "body": SERVICES_HUB_BODY,
    },
    {
        "path": "/services/crm-implementation/", "nav": "services",
        "title": "CRM Implementation for Small Businesses | Salt Services",
        "desc": "We set up your CRM so every lead gets tracked, followed up, and closed — pipelines, automations, missed-call text-back, and team training included.",
        "crumbs": [["Home", "/"], ["Services", "/services/"], ["CRM implementation", "/services/crm-implementation/"]],
        "jsonld": [service_ld("CRM implementation",
                              "CRM setup and implementation for small businesses: pipeline design, lead capture, automated follow-up, missed-call text-back, contact migration, and team training.",
                              "/services/crm-implementation/"),
                   faq_ld(CRM_FAQS)],
        "body": CRM_BODY,
    },
    {
        "path": "/services/ai-implementation/", "nav": "services",
        "title": "AI Implementation for Small Businesses | Salt Services",
        "desc": "Practical AI for local businesses: answer missed calls, reply to leads in seconds, draft follow-ups, and book appointments — wired into your CRM.",
        "crumbs": [["Home", "/"], ["Services", "/services/"], ["AI implementation", "/services/ai-implementation/"]],
        "jsonld": [service_ld("AI implementation",
                              "Practical AI implementation for local businesses: AI that answers missed calls and messages, qualifies leads, drafts follow-ups, and books appointments, with human handoff and guardrails.",
                              "/services/ai-implementation/"),
                   faq_ld(AI_FAQS)],
        "body": AI_BODY,
    },
    {
        "path": "/services/digital-advertising/", "nav": "services",
        "title": "Google & Meta Ads Management in East TN | Salt Services",
        "desc": "We run Google Ads and Meta campaigns for East Tennessee businesses and track every dollar to a real lead — with honest budget advice before you spend.",
        "crumbs": [["Home", "/"], ["Services", "/services/"], ["Digital advertising", "/services/digital-advertising/"]],
        "jsonld": [service_ld("Digital advertising management",
                              "Google Ads and Meta (Facebook and Instagram) advertising management for local businesses: research, creative, landing pages, conversion and call tracking, and plain-English reporting.",
                              "/services/digital-advertising/"),
                   faq_ld(ADS_FAQS)],
        "body": ADS_BODY,
    },
    {
        "path": "/services/web-design/", "nav": "services",
        "title": "Web Design for Local Businesses in East TN | Salt Services",
        "desc": "Hand-built websites that load fast, rank on Google, get cited by AI search, and feed every lead into your CRM. Own it outright or rent it monthly.",
        "crumbs": [["Home", "/"], ["Services", "/services/"], ["Web design", "/services/web-design/"]],
        "jsonld": [service_ld("Web design",
                              "Hand-built, fast-loading websites for local businesses, structured for Google rankings and AI search citations, with CRM-integrated forms. Build-and-own or monthly plans.",
                              "/services/web-design/"),
                   faq_ld(WEB_FAQS)],
        "body": WEB_BODY,
    },
    {
        "path": "/services/seo-aeo/", "nav": "services",
        "title": "SEO & AEO Services in East Tennessee | Salt Services",
        "desc": "Monthly SEO and AEO program: three genuinely useful pages a month that win Google searches and AI citations. You approve every page before it's live.",
        "crumbs": [["Home", "/"], ["Services", "/services/"], ["SEO & AEO", "/services/seo-aeo/"]],
        "jsonld": [service_ld("SEO and AEO",
                              "Monthly SEO and answer engine optimization program for local businesses: three unique pages per month targeting real searches, with preview approval and plain-English reporting.",
                              "/services/seo-aeo/"),
                   faq_ld(SEO_FAQS)],
        "body": SEO_BODY,
    },
    {
        "path": "/service-areas/", "nav": "areas",
        "title": "Serving Sevierville, Knoxville & East TN | Salt Services",
        "desc": "Salt Services works with businesses across East Tennessee — Kodak, Sevierville, Pigeon Forge, Gatlinburg, Knoxville, Maryville, and Dandridge.",
        "crumbs": [["Home", "/"], ["Service areas", "/service-areas/"]],
        "body": AREAS_BODY,
    },
    {
        "path": "/service-areas/sevierville/", "nav": "areas",
        "title": "Marketing Agency Serving Sevierville, TN | Salt Services",
        "desc": "Fifteen minutes from Sevierville, we help Parkway shops, cabin companies, and year-round local businesses win tourist searches and local ones alike.",
        "crumbs": [["Home", "/"], ["Service areas", "/service-areas/"], ["Sevierville", "/service-areas/sevierville/"]],
        "jsonld": [service_ld("Marketing services in Sevierville, TN",
                              "Marketing, advertising, web design, SEO/AEO, CRM, and AI implementation for businesses in Sevierville, Tennessee — tourist-facing and local alike.",
                              "/service-areas/sevierville/"),
                   faq_ld(SEV_FAQS)],
        "body": SEV_BODY,
    },
    {
        "path": "/service-areas/knoxville/", "nav": "areas",
        "title": "Digital Marketing for Knoxville Businesses | Salt Services",
        "desc": "Knoxville is a crowded market. We help small businesses out-rank bigger competitors by getting specific — neighborhood by neighborhood, page by page.",
        "crumbs": [["Home", "/"], ["Service areas", "/service-areas/"], ["Knoxville", "/service-areas/knoxville/"]],
        "jsonld": [service_ld("Digital marketing in Knoxville, TN",
                              "Digital marketing for Knoxville businesses: neighborhood-level advertising, SEO/AEO content, conversion-focused websites, and CRM/AI follow-up systems.",
                              "/service-areas/knoxville/"),
                   faq_ld(KNOX_FAQS)],
        "body": KNOX_BODY,
    },
    {
        "path": "/coraline/", "nav": "",
        "title": "Coraline | All-in-One CRM from Salt Services",
        "desc": "Coraline is the CRM and marketing platform behind our client work — pipelines, automation, booking, and AI chat. Plans from $197/month, set up by us.",
        "crumbs": [["Home", "/"], ["Coraline", "/coraline/"]],
        "jsonld": [{
            "@context": "https://schema.org",
            "@type": "Product",
            "name": "Coraline",
            "description": "All-in-one CRM and marketing platform: lead capture, pipelines, text and email automation, online booking, website builder, and AI conversation bot.",
            "brand": {"@type": "Brand", "name": "Coraline"},
            "url": "https://www.saltservicesusa.com/coraline/",
            "offers": [
                {"@type": "Offer", "name": "Starter", "price": "197.00", "priceCurrency": "USD", "url": CORALINE_CHECKOUT},
                {"@type": "Offer", "name": "Unlimited", "price": "297.00", "priceCurrency": "USD", "url": CORALINE_CHECKOUT},
                {"@type": "Offer", "name": "Pro", "price": "497.00", "priceCurrency": "USD", "url": CORALINE_CHECKOUT},
            ],
        }, faq_ld(CORALINE_FAQS)],
        "body": CORALINE_BODY,
    },
    {
        "path": "/work/", "nav": "work",
        "title": "Our Work — Live Client Sites | Salt Services",
        "desc": "Real client websites, live and clickable — tourism, trades, CPA, coffee. Built by Salt Services in Kodak, TN for businesses across East Tennessee.",
        "crumbs": [["Home", "/"], ["Our work", "/work/"]],
        "jsonld": [WORK_LD],
        "body": WORK_BODY,
    },
    {
        "path": "/about/", "nav": "about",
        "title": "About Salt Services | Marketing Agency in Kodak, TN",
        "desc": "Named for Matthew 5:13, Salt Services exists to give East Tennessee small businesses the online visibility that big companies buy their way into.",
        "crumbs": [["Home", "/"], ["About", "/about/"]],
        "body": ABOUT_BODY,
    },
    {
        "path": "/contact/", "nav": "contact",
        "title": "Contact Salt Services | (866) 721-7258 | Kodak, TN",
        "desc": "Call (866) 721-7258, email info@saltservicesusa.com, or start with our two-minute inquiry form. Based in Kodak, serving all of East Tennessee.",
        "crumbs": [["Home", "/"], ["Contact", "/contact/"]],
        "body": CONTACT_BODY,
    },
    {
        "path": "/form-completion/", "nav": "",
        "title": "Got It — Your Inquiry Is In | Salt Services",
        "desc": "Your inquiry landed in our pipeline. A real person reads it today — or skip the line and call (866) 721-7258 right now.",
        "noindex": True,
        "extra_head": '<meta name="robots" content="noindex">\n',
        "body": FORM_DONE_BODY,
    },
    {
        "path": "/privacy-policy/", "nav": "",
        "title": "Privacy Policy | Salt Services",
        "desc": "How Salt Services collects and uses information: what you send us, what's automatic, SMS terms, cookies, sharing, retention, and your rights.",
        "crumbs": [["Home", "/"], ["Privacy policy", "/privacy-policy/"]],
        "body": PRIVACY_BODY,
    },
    {
        "path": "/terms-of-service/", "nav": "",
        "title": "Terms of Service | Salt Services",
        "desc": "The terms that govern use of saltservicesusa.com and Salt Services engagements: scope, results, Coraline subscriptions, liability, and Tennessee law.",
        "crumbs": [["Home", "/"], ["Terms of service", "/terms-of-service/"]],
        "body": TERMS_BODY,
    },
    {
        "path": "/accessibility/", "nav": "",
        "title": "Accessibility Statement | Salt Services",
        "desc": "Our WCAG 2.1 AA commitment: verified contrast, keyboard navigation, reduced-motion support, known limitations, and how to report a barrier.",
        "crumbs": [["Home", "/"], ["Accessibility", "/accessibility/"]],
        "body": A11Y_BODY,
    },
    {
        "path": "/404.html", "nav": "",
        "title": "Page Not Found | Salt Services",
        "desc": "That page doesn't exist. Head back to the Salt Services home page, browse our services, or call (866) 721-7258.",
        "body": NOTFOUND_BODY,
    },
]
