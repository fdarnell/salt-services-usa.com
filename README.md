# saltservicesusa.com

Static marketing site for Salt Services (Kodak, TN). Plain HTML/CSS/JS — no frameworks, no build tools required to deploy. Deployed on Vercel from this repo.

## How the site is organized

| What | Where |
|------|-------|
| Page content & copy | `_build/pages_content.py` (source of truth) → generated HTML in `/`, `/services/…`, `/service-areas/…`, `/about/`, `/contact/` |
| Shared header/footer/chrome, business facts | `_build/gen.py` (the `BIZ` dict) |
| Business facts reference | `site.config.json` |
| Styles (colors in the `:root` block at the top) | `css/style.css` |
| Mobile menu + Coraline form loader | `js/main.js` |
| 3D hero scene (home page, desktop only) | `js/hero3d.js` — 14k-particle morph (sphere → SALT → ring), Three.js from CDN; skipped on mobile, reduced-motion, and no-WebGL |
| Signature cursor (site-wide, desktop only) | `js/cursor.js` |
| SEO roadmap for the monthly program | `content-plan.md` |

## Making edits

**Copy/content changes:** edit `_build/pages_content.py`, then regenerate every page:

```bash
python3 _build/gen.py
```

(Small one-off fixes directly in a page's `index.html` are fine too — but the next regeneration will overwrite them, so prefer editing `_build/`.)

**Changing a business fact (phone, email, towns):** update `site.config.json` AND the `BIZ` dict in `_build/gen.py`, regenerate, then confirm no stale copies remain:

```bash
grep -ril "old value" . --include='*.html'
```

## Preview before publishing

1. **Local preview:** from the repo folder run `python3 -m http.server 8000` and open http://localhost:8000
2. **Staging:** never edit `main` directly. Make changes on a branch (e.g. `edits`) and push it — Vercel gives the branch its own private preview URL to review and share. Merging the branch into `main` is what publishes to the live site.

The loop: **edit → local preview → push branch → check/share the Vercel preview URL → merge to publish.**

## Deploying (one-time setup)

vercel.com/new → import this GitHub repo → Framework Preset: **Other** → Deploy. No settings changes needed; `404.html` and clean URLs work automatically. Point the `saltservicesusa.com` domain at the project in Vercel's Domains tab (add both `www` and the bare domain).

## Monthly SEO installments

`content-plan.md` is the roadmap — 3 new pages per month. Each installment updates `sitemap.xml`, `llms.txt`, internal links, and the plan's Status column.
