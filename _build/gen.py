#!/usr/bin/env python3
"""
Page generator for saltservicesusa.com — adapted from the local-business-website
skill's generate_pages.py.

Defines the shared chrome (head, header, footer, mobile call bar, Coraline form
section) ONCE, then generates every page from the specs in pages_content.py.

Run from the repo root:  python3 _build/gen.py
Writes <path>/index.html for every page + 404.html + sitemap.xml.

Enforced by construction:
- NAP identical on every page (single footer definition)
- BreadcrumbList JSON-LD generated from "crumbs" (never hand-written)
- Duplicate titles/descriptions refuse to build
"""
import hashlib, json, pathlib, sys, datetime

# cache-buster: short hash of the stylesheet, appended as ?v= to its link,
# so browsers always pick up CSS changes immediately after a deploy
CSS_VERSION = hashlib.md5(
    (pathlib.Path(__file__).parent.parent / "css" / "style.css").read_bytes()
).hexdigest()[:8]

sys.path.insert(0, str(pathlib.Path(__file__).parent))

DOMAIN = "https://www.saltservicesusa.com"  # no trailing slash

# ---------------- Business facts (must match site.config.json) ----------------
BIZ = {
    "name": "Salt Services",
    "phone_display": "(866) 721-7258",
    "phone_tel": "+18667217258",
    "email": "info@saltservicesusa.com",
    "city": "Kodak",
    "state": "TN",
    "areas": ["Kodak", "Sevierville", "Pigeon Forge", "Gatlinburg", "Knoxville",
              "Maryville", "Dandridge"],
}

# Coraline embed (client-specific — from the embed code Franklin provided)
CORALINE = {
    "iframe_src": "https://link.coraline-communication.com/widget/form/ZG2GvC7Xk9bF3bCMCEB1",
    "form_id": "ZG2GvC7Xk9bF3bCMCEB1",
    "embed_js": "https://link.coraline-communication.com/js/form_embed.js",
    "form_name": "Website | Inquiry Form",
    "form_height": "770",
}

# ---------------- Reusable SVG snippets (inline, never emoji) ----------------
SPRINKLE = """<svg class="sprinkle" width="132" height="16" viewBox="0 0 132 16" fill="currentColor" aria-hidden="true"><circle cx="6" cy="8" r="3"/><circle cx="24" cy="5" r="2.2"/><circle cx="40" cy="10" r="2.6"/><circle cx="57" cy="6" r="2"/><circle cx="72" cy="11" r="2.4"/><circle cx="88" cy="7" r="1.8"/><circle cx="103" cy="10" r="2.2"/><circle cx="118" cy="6" r="1.6"/><circle cx="129" cy="9" r="1.4"/></svg>"""

CHECK = """<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>"""

PHONE_SVG = """<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>"""

def icon(name):
    """Card icons — 24px stroke SVGs wrapped in the .card-icon chip."""
    paths = {
        "crm": '<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',
        "ai": '<rect x="4" y="4" width="16" height="16" rx="2"/><rect x="9" y="9" width="6" height="6"/><path d="M9 1v3M15 1v3M9 20v3M15 20v3M1 9h3M1 15h3M20 9h3M20 15h3"/>',
        "ads": '<path d="M3 11 21 4l-3 14-6-3-2 4-2-6z"/>',
        "web": '<rect x="2" y="3" width="20" height="18" rx="2"/><path d="M2 8h20M6 5.5h.01M9 5.5h.01"/>',
        "seo": '<circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/><path d="M8 12l2 2 4-5"/>',
        "map": '<path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/>',
    }
    return ('<div class="card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" '
            'stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" '
            f'aria-hidden="true">{paths[name]}</svg></div>')

def check_li(text):
    return f'<li>{CHECK}{text}</li>'

# ---------------- Chrome templates ----------------
HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<!-- TODO: paste Google Search Console verification meta tag here -->
<meta property="og:type" content="website">
<meta property="og:site_name" content="Salt Services">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{domain}/og-image.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="icon" href="/icon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,500;0,9..144,600;1,9..144,500&family=Instrument+Sans:wght@400;500;600;700&family=Space+Mono&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/style.css?v={css_v}">
{extra_head}{jsonld}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
"""

NAV_ITEMS = [("home", "/", "Home"),
             ("services", "/services/", "Services"),
             ("work", "/work/", "Our work"),
             ("areas", "/service-areas/", "Service areas"),
             ("about", "/about/", "About"),
             ("contact", "/contact/", "Contact")]

def header(nav_current):
    current_attr = ' aria-current="page"'
    links = "".join(
        f'<li><a href="{url}"{current_attr if key == nav_current else ""}>{label}</a></li>'
        for key, url, label in NAV_ITEMS)
    return f"""<header class="site-header">
  <div class="wrap">
    <a class="brand" href="/"><img src="/images/salt-logo.png" alt="" width="42" height="42">Salt&nbsp;Services</a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="site-nav" aria-label="Menu">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"/></svg>
    </button>
    <nav class="site-nav" id="site-nav" aria-label="Main">
      <ul>{links}</ul>
    </nav>
    <a class="btn btn-accent header-phone" href="tel:{BIZ['phone_tel']}">{BIZ['phone_display']}</a>
  </div>
</header>
<main id="main">
"""

def crumbs_bar(crumbs_html):
    return f'<div class="wrap crumbs" aria-label="Breadcrumb">{crumbs_html}</div>\n'

FOOTER = f"""</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <h3>Salt Services</h3>
        <p>Marketing and AI implementation for local businesses. Named for Matthew 5:13 — we help small businesses salt up their web presence, their pipeline, and their cash flow.</p>
        <address>
          Based in {BIZ['city']}, {BIZ['state']} &middot; serving East Tennessee<br>
          Phone: <a href="tel:{BIZ['phone_tel']}">{BIZ['phone_display']}</a><br>
          Email: <a href="mailto:{BIZ['email']}">{BIZ['email']}</a>
        </address>
      </div>
      <div>
        <h3>Services</h3>
        <ul>
          <li><a href="/services/crm-implementation/">CRM implementation</a></li>
          <li><a href="/services/ai-implementation/">AI implementation</a></li>
          <li><a href="/services/digital-advertising/">Digital advertising</a></li>
          <li><a href="/services/web-design/">Web design</a></li>
          <li><a href="/services/seo-aeo/">SEO &amp; AEO</a></li>
          <li><a href="/coraline/">Coraline CRM</a></li>
        </ul>
      </div>
      <div>
        <h3>Service areas</h3>
        <ul>
          <li><a href="/service-areas/sevierville/">Sevierville</a></li>
          <li><a href="/service-areas/knoxville/">Knoxville</a></li>
          <li><a href="/service-areas/">All service areas</a></li>
          <li><a href="/work/">Our work</a></li>
          <li><a href="/about/">About us</a></li>
          <li><a href="/contact/">Contact</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-legal">
      <span>&copy; 2026 Salt Services. All rights reserved.</span>
      <span><a href="/privacy-policy/">Privacy policy</a> &middot; <a href="/terms-of-service/">Terms of service</a> &middot; <a href="/accessibility/">Accessibility</a></span>
      <span>Kodak, Tennessee &middot; <a href="tel:{BIZ['phone_tel']}">{BIZ['phone_display']}</a></span>
    </div>
  </div>
</footer>
<div class="callbar">
  <a class="callbar-phone" href="tel:{BIZ['phone_tel']}">{PHONE_SVG} Call {BIZ['phone_display']}</a>
  <a class="callbar-form" href="/contact/#form">Get started</a>
</div>
<script src="/js/main.js" defer></script>
<script src="/js/cursor.js" defer></script>
<script defer src="/_vercel/insights/script.js"></script>
</body>
</html>
"""

def coraline_section(heading, blurb, aside=""):
    """Lazy-loading Coraline form section (contact page). Optional aside sits
    beside the form on desktop — objection-handling at the moment of hesitation."""
    aside_open = '<div class="coraline-cols"><div>' if aside else ""
    aside_close = f'</div><aside class="form-aside">{aside}</aside></div>' if aside else ""
    return f"""<section class="section" id="form">
  <div class="wrap">
    <div class="section-head">
      <h2>{heading}</h2>
      {SPRINKLE}
      <p>{blurb}</p>
    </div>
    {aside_open}<div class="coraline-form"
         data-iframe-src="{CORALINE['iframe_src']}"
         data-embed-js="{CORALINE['embed_js']}"
         data-form-id="{CORALINE['form_id']}"
         data-form-name="{CORALINE['form_name']}"
         data-form-height="{CORALINE['form_height']}">
      <div class="coraline-form__placeholder">
        <p><strong>Start with our lead form</strong></p>
        <p>A few quick questions about your business — we'll come back with real recommendations, not a canned pitch.</p>
        <button type="button" class="coraline-form__load-btn">Open the form</button>
        <noscript><p>Our form needs JavaScript. You can also call {BIZ['phone_display']} or email {BIZ['email']}.</p></noscript>
      </div>
    </div>{aside_close}
    <p class="hero-note">Rather talk? Call <a href="tel:{BIZ['phone_tel']}">{BIZ['phone_display']}</a> — you'll get a person, not a phone tree.</p>
  </div>
</section>
"""

# ---------------- JSON-LD builders ----------------
def local_business_ld():
    return {
        "@context": "https://schema.org",
        "@type": "ProfessionalService",
        "@id": DOMAIN + "/#business",
        "name": "Salt Services",
        "description": "Marketing and AI implementation agency in Kodak, Tennessee. CRM implementation, AI implementation, Google and Meta advertising, web design, and SEO/AEO for local businesses in East Tennessee.",
        "url": DOMAIN + "/",
        "telephone": BIZ["phone_tel"],
        "email": BIZ["email"],
        "image": DOMAIN + "/og-image.png",
        "logo": DOMAIN + "/images/salt-logo.png",
        "address": {"@type": "PostalAddress", "addressLocality": "Kodak",
                    "addressRegion": "TN", "addressCountry": "US"},
        "areaServed": [{"@type": "City", "name": c + ", TN"} for c in BIZ["areas"]],
    }

def service_ld(name, desc, url):
    return {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": name,
        "description": desc,
        "url": DOMAIN + url,
        "provider": {"@id": DOMAIN + "/#business"},
        "areaServed": [{"@type": "City", "name": c + ", TN"} for c in BIZ["areas"]],
    }

def faq_ld(faqs):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q,
                        "acceptedAnswer": {"@type": "Answer", "text": a}}
                       for q, a in faqs],
    }

def faq_html(faqs, heading="Questions we hear a lot"):
    items = "".join(
        f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)
    return f"""<section class="section section-alt">
  <div class="wrap">
    <div class="section-head"><h2>{heading}</h2>{SPRINKLE}</div>
    <div class="faq">{items}</div>
  </div>
</section>
"""

def crumb_ld(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1,
                                 "name": n, "item": DOMAIN + u}
                                for i, (n, u) in enumerate(items)]}

# ---------------- Build ----------------
def build(spec, seen_titles, seen_descs, outdir="."):
    p = spec["path"]
    assert p.startswith("/") and (p.endswith("/") or p == "/404.html"), f"bad path: {p}"
    if spec["title"] in seen_titles: raise SystemExit(f"DUPLICATE TITLE: {p}")
    if spec["desc"] in seen_descs: raise SystemExit(f"DUPLICATE DESC: {p}")
    assert len(spec["title"]) <= 62, f"title too long ({len(spec['title'])}): {p}"
    assert len(spec["desc"]) <= 158, f"desc too long ({len(spec['desc'])}): {p}"
    seen_titles.add(spec["title"]); seen_descs.add(spec["desc"])
    url = DOMAIN + p
    lds = [local_business_ld()] + spec.get("jsonld", [])
    crumbs = spec.get("crumbs")
    crumbs_html = ""
    if crumbs:
        lds.append(crumb_ld(crumbs))
        crumbs_html = " &rsaquo; ".join(
            f'<a href="{u}">{n}</a>' if u != p else n for n, u in crumbs)
    jsonld = "\n".join(
        '<script type="application/ld+json">' + json.dumps(l, ensure_ascii=False) + "</script>"
        for l in lds)
    html = HEAD.format(title=spec["title"], desc=spec["desc"], url=url,
                       domain=DOMAIN, jsonld=jsonld, css_v=CSS_VERSION,
                       extra_head=spec.get("extra_head", ""))
    html += header(spec.get("nav", ""))
    if crumbs_html:
        html += crumbs_bar(crumbs_html)
    html += spec["body"]
    html += FOOTER
    out = pathlib.Path(outdir + p + ("index.html" if p.endswith("/") else ""))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html)
    print(f"wrote {out}")
    return p

def write_sitemap(paths, outdir="."):
    today = datetime.date.today().isoformat()
    urls = "\n".join(
        f"  <url><loc>{DOMAIN}{p}</loc><lastmod>{today}</lastmod></url>"
        for p in sorted(paths) if p != "/404.html")
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls}
</urlset>
"""
    pathlib.Path(outdir + "/sitemap.xml").write_text(xml)
    print("wrote sitemap.xml")

if __name__ == "__main__":
    from pages_content import PAGES
    seen_t, seen_d = set(), set()
    written = [build(spec, seen_t, seen_d) for spec in PAGES]
    write_sitemap([p for spec, p in zip(PAGES, written) if not spec.get("noindex")])
    print(f"{len(written)} pages built")
