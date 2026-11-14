# Showcase pieces: the sliding "what we build" card row under the home hero,
# the home-page software teaser, and the /software/ page body.
# Imported by pages_content.py. Plain HTML — no inline CSS or JS (see css/style.css
# "Showcase" block for the styles).
from gen import SPRINKLE


def _i(paths):
    """Small stroke icon for card labels."""
    return ('<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
            + paths + '</svg>')


IC_PIN = _i('<path d="M12 22s7-6.2 7-12a7 7 0 1 0-14 0c0 5.8 7 12 7 12z"/><circle cx="12" cy="10" r="2.5"/>')
IC_GLOBE = _i('<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.6 3 2.6 15 0 18M12 3c-2.6 3-2.6 15 0 18"/>')
IC_SPARK = _i('<path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8z"/><path d="M19 16l.7 2 2 .7-2 .7-.7 2-.7-2-2-.7 2-.7z"/>')
IC_MSG = _i('<path d="M4 5h16v11H9l-5 4z"/>')
IC_DOC = _i('<path d="M6 3h9l4 4v14H6z"/><path d="M9 12h7M9 16h5"/>')
IC_STAR = _i('<path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z"/>')
IC_CUBE = _i('<path d="M12 2l9 5v10l-9 5-9-5V7z"/><path d="M3 7l9 5 9-5M12 12v10"/>')
IC_GRID = _i('<rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="4" rx="1"/><rect x="14" y="10" width="7" height="11" rx="1"/><rect x="3" y="13" width="7" height="8" rx="1"/>')

STARS = '<span class="sc-stars" aria-hidden="true">&#9733;&#9733;&#9733;&#9733;&#9733;</span>'

# A mini site plan: house, hatched patio, fire pit, dimensions.
PATIO_SVG = """<svg class="sc-plan" viewBox="0 0 240 92" aria-hidden="true">
  <defs><pattern id="hatch" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="6" stroke="rgba(233,161,59,.45)" stroke-width="2"/></pattern></defs>
  <rect x="8" y="8" width="78" height="76" rx="3" fill="rgba(255,255,255,.05)" stroke="rgba(255,255,255,.25)"/>
  <text x="47" y="50" text-anchor="middle" class="sc-plan-t">House</text>
  <path d="M86 20 H200 V76 H86" fill="url(#hatch)" stroke="#e9a13b" stroke-width="1.5"/>
  <circle cx="172" cy="48" r="11" fill="rgba(14,8,31,.7)" stroke="#e9a13b" stroke-width="1.5"/>
  <text x="143" y="15" text-anchor="middle" class="sc-plan-t">20'</text>
  <text x="214" y="51" text-anchor="middle" class="sc-plan-t">16'</text>
  <circle cx="104" cy="28" r="2.4" fill="#f6e7b0"/><circle cx="104" cy="68" r="2.4" fill="#f6e7b0"/><circle cx="194" cy="28" r="2.4" fill="#f6e7b0"/>
</svg>"""

SHOWCASE_CARDS = f"""
      <li class="sc">
        <span class="sc-label">{IC_PIN}Google Maps</span>
        <div class="sc-card">
          <div class="sc-search"><span>tire shop near me</span>{_i('<circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/>')}</div>
          <svg class="sc-map" viewBox="0 0 240 70" aria-hidden="true">
            <rect width="240" height="70" rx="8" fill="rgba(255,255,255,.04)"/>
            <path d="M-5 50 C60 40 90 62 150 44 S220 30 250 36" stroke="rgba(120,150,210,.35)" stroke-width="7" fill="none"/>
            <path d="M40 -5 L70 75 M150 -5 L130 75 M0 22 H240" stroke="rgba(255,255,255,.09)" stroke-width="4" fill="none"/>
            <circle cx="40" cy="40" r="4" fill="#7d73a0"/><circle cx="196" cy="18" r="4" fill="#7d73a0"/><circle cx="210" cy="54" r="4" fill="#7d73a0"/>
            <path d="M118 12a10 10 0 0 1 10 10c0 8-10 17-10 17s-10-9-10-17a10 10 0 0 1 10-10z" fill="#e9a13b"/><circle cx="118" cy="22" r="3.5" fill="#180f2f"/>
          </svg>
          <p class="sc-title">Blessed Beginnings Tire &amp; Service</p>
          <p class="sc-rating">5.0 {STARS} <span class="sc-dim">(15)</span></p>
          <p class="sc-dim">Tire shop &middot; Sevierville &middot; <span class="sc-green">By appointment</span></p>
          <div class="sc-actions"><span>Call</span><span>Directions</span><span>Website</span></div>
        </div>
      </li>
      <li class="sc">
        <span class="sc-label">{IC_GLOBE}Website</span>
        <div class="sc-card sc-flush">
          <div class="sc-browser"><i></i><i></i><i></i><span>mtnlandscapers.com</span></div>
          <img src="/images/work/mountain-landscapers.webp" alt="Mountain Landscapers home page" width="640" height="400" loading="lazy">
          <div class="sc-pad">
            <p class="sc-title">Mountain Landscapers</p>
            <p class="sc-dim">A page for every service and town they want to win, built to rank in Sevier County.</p>
          </div>
        </div>
      </li>
      <li class="sc">
        <span class="sc-label">{IC_SPARK}AI search</span>
        <div class="sc-card">
          <div class="sc-ai-q">Who builds paver patios near Sevierville?</div>
          <div class="sc-ai-a">
            <span class="sc-ai-dot">{IC_SPARK}</span>
            <p><b>Mountain Landscapers</b> in Sevierville designs and installs paver patios, walls and outdoor living spaces, and quotes with a drawing of your yard.</p>
          </div>
          <div class="sc-chips"><span>mtnlandscapers.com</span><span>Google reviews</span></div>
          <p class="sc-dim sc-foot">Pages written so ChatGPT, Gemini and Google's AI can name you.</p>
        </div>
      </li>
      <li class="sc">
        <span class="sc-label">{IC_MSG}Instant text-back</span>
        <div class="sc-card">
          <div class="sc-thread-head"><span class="sc-avatar">CR</span><div><p class="sc-title">C&amp;R Moving</p><p class="sc-dim">Text message</p></div></div>
          <div class="sc-bubble sc-in">Hi Dana, thanks for reaching out to C&amp;R Moving! Is Saturday morning good for a free walk-through?</div>
          <p class="sc-stamp">Sent 38 seconds after the form</p>
          <div class="sc-bubble sc-out">Saturday works, thank you!</div>
          <p class="sc-dim sc-foot">Every lead lands in the CRM and gets an answer, even at 11 pm.</p>
        </div>
      </li>
      <li class="sc">
        <span class="sc-label">{IC_DOC}Quotes with a drawing</span>
        <div class="sc-card">
          <p class="sc-title">Estimate &middot; Paver patio</p>
          {PATIO_SVG}
          <ul class="sc-lines">
            <li class="on">Paver patio, 320 sq ft</li>
            <li class="on">Fire pit</li>
            <li class="on">Patio lighting <span class="sc-tag">Recommended</span></li>
          </ul>
          <span class="sc-btn">Approve &amp; sign</span>
        </div>
      </li>
      <li class="sc">
        <span class="sc-label">{IC_STAR}Review requests</span>
        <div class="sc-card">
          <div class="sc-thread-head"><span class="sc-avatar">DR</span><div><p class="sc-title">Downtown River Rentals</p><p class="sc-dim">Text message</p></div></div>
          <div class="sc-bubble sc-in">Thanks for staying with us! Would you leave a quick review? It helps a small business a lot.</div>
          <span class="sc-btn sc-btn-ghost">Leave a review</span>
          <div class="sc-review">
            <span class="sc-stars sc-stars-lg" aria-hidden="true">&#9733;&#9733;&#9733;&#9733;&#9733;</span>
            <p class="sc-dim">5 stars, posted to Google</p>
          </div>
        </div>
      </li>
      <li class="sc">
        <span class="sc-label">{IC_CUBE}Interactive 3D</span>
        <div class="sc-card sc-center">
          <svg class="sc-wheel" viewBox="0 0 120 120" aria-hidden="true">
            <circle cx="60" cy="60" r="54" fill="#0b0717" stroke="rgba(255,255,255,.18)" stroke-width="2"/>
            <g class="sc-wheel-spin">
              <circle class="sc-rim" cx="60" cy="60" r="38" fill="none" stroke-width="7"/>
              <g class="sc-rim-s" stroke-width="6" stroke-linecap="round">
                <path d="M60 60 V24"/><path d="M60 60 L94 49"/><path d="M60 60 L81 89"/><path d="M60 60 L39 89"/><path d="M60 60 L26 49"/>
              </g>
              <circle cx="60" cy="60" r="9" fill="#1d1533" stroke="rgba(255,255,255,.3)"/>
            </g>
          </svg>
          <div class="sc-swatches" aria-hidden="true"><i class="s1"></i><i class="s2"></i><i class="s3"></i><i class="s4"></i></div>
          <p class="sc-title">Colortec Coatings</p>
          <p class="sc-dim">Pick a powder-coat finish and watch the wheel change color.</p>
        </div>
      </li>
      <li class="sc">
        <span class="sc-label">{IC_GRID}Client portal</span>
        <div class="sc-card">
          <p class="sc-title">Your month at a glance</p>
          <div class="sc-stats">
            <div><b>23</b><span>New leads</span></div>
            <div><b>41</b><span>Calls</span></div>
            <div><b>6</b><span>Reviews</span></div>
          </div>
          <svg class="sc-bars" viewBox="0 0 220 60" aria-hidden="true">
            <g fill="rgba(255,255,255,.14)"><rect x="4" y="34" width="18" height="26" rx="3"/><rect x="31" y="28" width="18" height="32" rx="3"/><rect x="58" y="38" width="18" height="22" rx="3"/><rect x="85" y="24" width="18" height="36" rx="3"/><rect x="112" y="20" width="18" height="40" rx="3"/><rect x="139" y="14" width="18" height="46" rx="3"/><rect x="166" y="10" width="18" height="50" rx="3"/></g>
            <rect x="193" y="4" width="18" height="56" rx="3" fill="#e9a13b"/>
          </svg>
          <div class="sc-row"><span>Website plan</span><span class="sc-green">Paid</span></div>
        </div>
      </li>"""

SHOWCASE = f"""
<section class="showcase" aria-labelledby="showcase-h">
  <div class="wrap showcase-head">
    <span class="showcase-kicker">What we build</span>
    <h2 id="showcase-h">Everywhere your next customer <em>looks</em></h2>
    <p>Real work for East Tennessee businesses, from the Google listing to the text that goes out before they&rsquo;ve closed the tab.</p>
  </div>
  <div class="showcase-viewport">
    <div class="showcase-track">
      <ul class="showcase-set">{SHOWCASE_CARDS}
      </ul>
      <ul class="showcase-set" aria-hidden="true">{SHOWCASE_CARDS}
      </ul>
    </div>
  </div>
</section>
"""

# ------------------------------------------------------------------ real screenshots
# Captured from each app running locally on made-up sample data (no real
# customers). Files live in images/software/.

def shot(src, alt, url, w, h, cls=""):
    return f"""<figure class="shot{(' ' + cls) if cls else ''}">
  <div class="shot-bar" aria-hidden="true"><i></i><i></i><i></i>{("<span>" + url + "</span>") if url else ""}</div>
  <img src="/images/software/{src}" alt="{alt}" width="{w}" height="{h}" loading="lazy">
</figure>"""

def scroll_shot(src, alt, w, h, cls=""):
    """A tall page in a short window; it scrolls itself on hover."""
    return f"""<figure class="shot shot-scroll{(' ' + cls) if cls else ''}" tabindex="0">
  <img src="/images/software/{src}" alt="{alt}" width="{w}" height="{h}" loading="lazy">
</figure>"""

def phone_shot(src, alt, w, h, cls=""):
    return f"""<figure class="phone-shot{(' ' + cls) if cls else ''}">
  <img src="/images/software/{src}" alt="{alt}" width="{w}" height="{h}" loading="lazy">
</figure>"""

SHOT_CRM = shot("crm-inbox.webp", "The lead inbox for a sample lawn company: a website lead gets an automatic text within the minute and books an estimate", "", 1600, 1000)
SHOT_QUOTE = shot("quote-drawing.webp", "The drawing pad: a back yard plan with a paver patio, fire pit, planting beds and a retaining wall", "", 1600, 1000)
SHOT_QUOTE_CUSTOMER = scroll_shot("quote-customer.webp", "The estimate the customer receives: the drawing, everything on the plan, the price and the payment schedule", 720, 2155, "shot-overlap")
SHOT_CRM_2 = shot("crm-pipeline.webp", "The sales pipeline: jobs moving from new lead to quote sent, accepted, scheduled and won", "", 1600, 1000, "shot-overlap shot-small shot-left")
SHOT_PORTAL = shot("portal-dashboard.webp", "The client portal: a sample roofing company&rsquo;s leads from its website", "", 1600, 1000)
SHOT_PORTAL_2 = shot("portal-billing.webp", "Billing in the client portal: plans, paid invoices and the signed services agreement", "", 1600, 1000, "shot-overlap shot-small")
SHOT_CAL = shot("cal-month.webp", "The family calendar for a sample family: a busy month of school, sports, church and date nights", "", 1600, 1000)
SHOT_CAL_MILES = shot("cal-mileage.webp", "The mileage log: trips grouped by day with route, vehicle, odometer, miles and the running tax deduction", "", 1600, 1000)
SHOT_CAL_ASK = shot("cal-assistant.webp", "The calendar assistant adding what is missing for taco night to the grocery list", "", 1600, 1000)
SHOT_CAL_GROCERY = phone_shot("cal-grocery.webp", "The shared grocery list on an iPhone, with a colored dot for who added each item", 780, 1688)
SHOT_CAL_PHONE = phone_shot("cal-phone.webp", "The family calendar on an iPhone", 780, 1688)
SHOT_CRM_PHONE = phone_shot("crm-phone.webp", "The lead inbox on an iPhone", 780, 1688)
SHOT_PORTAL_PHONE = phone_shot("portal-phone.webp", "The client portal on an iPhone", 780, 1688)

# ------------------------------------------------------------------ home-page teaser

SOFTWARE_TEASER = f"""
<section class="section section-navy software-teaser">
  <div class="wrap">
    <div class="section-head">
      <h2>We build <em>software</em>, too</h2>
      {SPRINKLE}
      <p>Not plug-ins or a monthly subscription to somebody else&rsquo;s app. Tools we wrote ourselves and run every day: a CRM our clients answer leads from, an estimating app crews price jobs with in the driveway, and a family calendar for life at home.</p>
    </div>
    <ul class="sw-tiles">
      <li><a href="/software/#crm"><div class="sw-tile-shot">{SHOT_CRM}</div><span class="sw-kicker">01</span><h3>CRM</h3><p>Every lead in one inbox, a pipeline to won, and a portal where each client sees their numbers.</p></a></li>
      <li><a href="/software/#estimating"><div class="sw-tile-shot">{SHOT_QUOTE}</div><span class="sw-kicker">02</span><h3>Estimating</h3><p>Draw the job, price it from your own price book, and let the customer sign and pay online.</p></a></li>
      <li><a href="/software/#lifestyle"><div class="sw-tile-shot">{SHOT_CAL}</div><span class="sw-kicker">03</span><h3>Lifestyle</h3><p>A shared family calendar with the grocery list, mileage log and event planner built in.</p></a></li>
    </ul>
    <p class="sw-more"><a class="btn btn-accent" href="/software/">See the software we&rsquo;ve built</a></p>
  </div>
</section>
"""

# ------------------------------------------------------------------ /software/ page

def sw_feature(kicker, title, blurb, bullets, who, shot, flip=False):
    lis = "".join(f"<li>{b}</li>" for b in bullets)
    return f"""<div class="sw-feature{' flip' if flip else ''}">
      <div class="sw-copy">
        <span class="sw-kicker">{kicker}</span>
        <h2>{title}</h2>
        <p>{blurb}</p>
        <ul class="sw-checks">{lis}</ul>
        {f'<p class="sw-who">{who}</p>' if who else ""}
      </div>
      <div class="sw-shot">{shot}</div>
    </div>"""

def sw_small(icon_html, title, blurb, href=None, link_text="See it live"):
    if href:
        ext = ' target="_blank" rel="noopener"' if href.startswith("http") else ""
        link = f'<a class="card-link" href="{href}"{ext}>{link_text} &rsaquo;</a>'
    else:
        link = '<span class="sw-soon">In testing</span>'
    return f"""<li class="card sw-small"><span class="sw-small-ic">{icon_html}</span><h3>{title}</h3><p>{blurb}</p>{link}</li>"""

_BIG = lambda s: s.replace('width="12" height="12"', 'width="22" height="22"')

def sw_category(cid, num, name, title_html, intro, inner, alt=False):
    return f"""<section class="section sw-cat{' section-alt' if alt else ''}" id="{cid}" aria-labelledby="{cid}-h">
  <div class="wrap">
    <header class="sw-cat-head">
      <span class="sw-cat-num">{num}</span>
      <div>
        <span class="sw-kicker">{name}</span>
        <h2 id="{cid}-h">{title_html}</h2>
        <p>{intro}</p>
      </div>
    </header>
    {inner}
  </div>
</section>
"""

CAT_CRM = sw_category("crm", "01", "CRM", "Every lead answered, every client <em>in the loop</em>",
    "The tools that catch a lead the moment it comes in, keep the job moving, and show the client exactly what their marketing is doing.",
    sw_feature("Lead inbox", "One inbox for every lead",
               "Website forms, calls, texts, email and Google reviews all land in one place, and nothing sits unanswered. Shown with a sample lawn company.",
               ["Missed-call text-back within seconds, day or night",
                "Calls and texts from the browser, iPhone or iPad, from the business number",
                "A sales pipeline from new lead to won, with the next step on every card",
                "Reminders that keep coming back until the job is done",
                "Review requests by text or email, with follow-ups",
                "A built-in assistant you can ask: who&rsquo;s waiting on a callback?"],
               "Built and run by Salt Services for our clients.", f'<div class="shot-stack">{SHOT_CRM}{SHOT_CRM_2}</div>')
    + sw_feature("Client portal", "A login for every client",
               "Where every client logs in to see what their marketing is doing and pay for it, without emailing anyone for a report. Shown with a sample roofing company.",
               ["Sign in with a code to your phone or email, no password to forget",
                "Every lead from the website in one list, with the message they sent",
                "Visitors, top pages and Google search performance, month by month",
                "The SEO roadmap and monthly reports, so you can see what was done",
                "Plans, invoices and the signed agreement, with a card on file"],
               "Every Salt Services client gets a login.", f'<div class="shot-stack">{SHOT_PORTAL}{SHOT_PORTAL_2}</div>', flip=True)
    + sw_feature("On the phone", "Built for the truck, not the desk",
               "All of it works on an iPhone or iPad, so the owner can run the day from a job site.",
               ["Reply by text, email or note, or start a call, from one bar",
                "Keep a call going while you look something up",
                "Clients check their own leads and numbers from their phone"],
               "The lead inbox (left) and the client portal (right). An iPhone and iPad app is on the way.", f'<div class="phone-pair">{SHOT_CRM_PHONE}{SHOT_PORTAL_PHONE}</div>'))

CAT_EST = sw_category("estimating", "02", "Estimating", "Quote the job <em>in the driveway</em>",
    "Built first for a Sevier County landscaping company and now running a fence company too. The crew draws the job, the price book does the math, and the customer approves on their phone.",
    sw_feature("Drawing &amp; pricing", "Draw it once, price it automatically",
               "Sketch the yard on a tablet and every patio, bed, plant and wall turns into a priced line on the estimate. The customer gets a clean copy with the drawing on top. Hover the estimate to scroll it.",
               ["Sketch the yard, patio or fence line and drop gates and plants right on the plan",
                "Price from your own price book, with optional add-ons the customer can tick",
                "Customer reviews, signs and pays the deposit online",
                "Payment schedules, bills, late fees and account credit handled for you",
                "Pick up where you left off; it reopens the exact customer and estimate",
                "One tap to ask for a review when the job is finished"],
               "In use by a landscaping crew and a fence crew in East Tennessee.", f'<div class="shot-stack">{SHOT_QUOTE}{SHOT_QUOTE_CUSTOMER}</div>'),
    alt=True)

CAT_LIFE = sw_category("lifestyle", "03", "Lifestyle", "Software for home, <em>not just work</em>",
    "The same care, pointed at the kitchen table. A family calendar we built for our own household, shown here with a sample family.",
    sw_feature("Family calendar", "One calendar the whole house shares",
               "Everybody&rsquo;s plans in one place, color-coded by person, on every phone. Shown with a sample family.",
               ["One shared month, week and agenda view for the whole family",
                "Each person gets a color, so you can tell whose night it is at a glance",
                "A note for the day and sticky notes for the things that aren&rsquo;t events",
                "Works on the computer and the phone"],
               "Built for our own household and headed to the App Store.",
               f'<div class="cal-stack">{SHOT_CAL}{SHOT_CAL_PHONE}</div>')
    + sw_feature("Assistant &amp; lists", "Ask for it in plain words",
               "Type what you need in plain words. The assistant checks the calendar and the lists and offers to do it, and nothing changes until you tap Do it.",
               ["A shared grocery list anyone in the house can add to",
                "&ldquo;Add what we need for taco night&rdquo; checks what&rsquo;s already on the list",
                "Every change waits for a yes before it happens"],
               "", f'<div class="cal-stack phone-left">{SHOT_CAL_ASK}{SHOT_CAL_GROCERY}</div>', flip=True)
    + sw_feature("Mileage", "Mileage that adds itself up",
               "Start a trip, save the spots you go often, and the log fills itself in by day, with the odometer and the deduction estimate kept for tax time.",
               ["Trips grouped by day with the route and the reason",
                "Odometer start and end on every trip, per vehicle",
                "Business, charity and personal miles kept apart, with a running deduction"],
               "", SHOT_CAL_MILES))

SOFTWARE_BODY = f"""<section class="hero sw-hero">
  <div class="wrap">
    <span class="hero-kicker">Custom software &middot; built in Kodak, TN</span>
    <h1>Software we&rsquo;ve built, in use <em>every day</em></h1>
    {SPRINKLE}
    <p class="lead">Most small businesses glue five subscriptions together and still copy things by hand. We write the tool instead. Everything on this page is ours, built line by line, and it&rsquo;s running right now.</p>
    <nav class="sw-jump" aria-label="Software categories">
      <a href="#crm"><span>01</span>CRM</a>
      <a href="#estimating"><span>02</span>Estimating</a>
      <a href="#lifestyle"><span>03</span>Lifestyle</a>
    </nav>
  </div>
</section>
{CAT_CRM}{CAT_EST}{CAT_LIFE}
<section class="section section-alt">
  <div class="wrap">
    <div class="section-head">
      <h2>Plus smaller tools built into <em>client websites</em></h2>
      {SPRINKLE}
      <p>Not every problem needs a whole app. A few one-job tools we&rsquo;ve built:</p>
    </div>
    <ul class="card-grid sw-small-grid">
      {sw_small(_BIG(IC_DOC), "Online equipment rental booking", "Pick the machine, pick the days, book it. Check-in reminders go out by text automatically.", "https://www.mtnlandscapers.com/rent/")}
      {sw_small(_BIG(IC_PIN), "Penny tread check &amp; tire size reader", "A tire shop&rsquo;s visitors check their own tread and read their sidewall size before they call.", "https://www.blessedbeginningstire.com/")}
      {sw_small(_BIG(IC_CUBE), "3D finish picker", "Spin a wheel in 3D and try powder-coat colors before you ever bring it in.", "https://www.colorteccoatings.com/")}
    </ul>
  </div>
</section>
"""
