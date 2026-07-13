# Salt Services — Design System

Derived with the ui-ux-pro-max design skill (github.com/nextlevelbuilder/ui-ux-pro-max-skill), pattern: **Trust & Authority + Conversion** (navy/grey corporate, accent reserved for CTAs). All tokens live in the `:root` block of `css/style.css` — rebranding is a one-block edit.

## Tokens

| Group | Values |
|-------|--------|
| Brand | deep violet `#180f2f`, elevated `#2b1d52`, darkest `#0e081f`, amber accent `#e9a13b` (CTAs + accent words only) |
| Light surfaces | warm ivory `#f5f3ed`, deep ivory `#ece9e0`, bone cards `#fbfaf6` |
| Text | ink `#201439` headings, body `#3d3357`, muted `#635a7d` (all WCAG AA verified) |
| Dark surfaces | hairline `rgba(255,255,255,.08)`, top-edge sheen `rgba(255,255,255,.06)` |
| Spacing | 8px rhythm: `--space-1` (4px) … `--space-16` (64px) |
| Radius | 6 / 10 / 16px |
| Elevation | `--shadow-1/2/3`, navy-tinted; cards rest at 1, hover to 2 |
| Motion | 150ms fast / 250ms standard, ease `cubic-bezier(.16,1,.3,1)`; all animation behind `prefers-reduced-motion` |
| Z-index | header 50, callbar 60, cursor fx 9998/9999 |

## Typography (editorial — influenced by americanfireplaces + mtnlandscapers)

- **Headings:** Fraunces 500/600 serif (Google Fonts, `display=swap`, preconnected), tight tracking. Every h1 carries one *italic amber accent word* (`<em>`), echoing the reference sites.
- **Body:** Instrument Sans 400–700.
- **Mono labels** (hero kicker with em-dash flourishes, HUD, footer column headings): Space Mono.
- Headings hyphenate below 640px (`hyphens:auto`) so long words never cause horizontal scroll.

## Signature elements

- Particle-morph hero (Weblove Template 20): 14k grains, sphere → SALT (serif Fraunces letterforms) → ring, amber sparks, corner HUD. Desktop-only; gradient fallback for mobile/reduced-motion/crawlers.
- Salt-sprinkle SVG divider under section headings.
- Amber signature cursor (dot + trailing ring + ripple), desktop-only, reduced-motion-safe.
- Pill CTA buttons: amber glow on hover, press-scale feedback.
- Numbered process steps: italic serif amber numerals (01/02/03) with hairline underline.

## Rules honored (from the skill's checklist)

One primary CTA per screen; SVG icons only (no emoji); 4.5:1 contrast everywhere; visible focus rings; 44px+ touch targets; no horizontal scroll 320–1920px; reduced-motion respected; semantic tokens, no raw hex in components.
