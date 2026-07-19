# Salt Services — Website Handoff

*Prepared July 2026. Written for the owner — no jargon, promise.*

## What was built

A 12-page website (plus a branded error page) designed to do three jobs, in this order:

1. **Get found** — by Google searches and by AI assistants (ChatGPT, Claude, Perplexity) when people ask for marketing help in East Tennessee.
2. **Load fast** — the whole site is hand-built code with no bloat. Pages weigh less than a single photo on most competitors' sites. The one deliberate exception: the home page's interactive 3D hero (14,000 salt-grain particles that morph between a sphere, the word "SALT", and a ring — and scatter away from the cursor) loads a 3D engine on desktop. It's worth the wow — and it's skipped entirely on phones, for visitors who prefer reduced motion, and by search/AI crawlers, so it costs nothing where it matters most.
3. **Convert visitors** — every page funnels to the Step One lead form or a phone call. Leads land in Coraline automatically.

## Which search each page targets

| Page | Built to win |
|------|--------------|
| Home | "marketing agency Kodak TN" and brand searches |
| CRM implementation | "CRM implementation/setup for small business" |
| AI implementation | "AI implementation/AI for small business" |
| Digital advertising | "Google Ads management East Tennessee" |
| Web design | "web design for local business East TN" |
| SEO & AEO | "SEO services East Tennessee", "what is AEO" |
| Sevierville | "marketing agency Sevierville TN" |
| Knoxville | "digital marketing Knoxville" |
| Our work | (proof page — live client sites; graduates to case studies as rankings data arrives) |

The remaining towns (Pigeon Forge, Gatlinburg, Maryville, Dandridge, and more) arrive at 3 pages per month — the full schedule is in `content-plan.md`. This is the same monthly program Salt Services sells, practiced on its own site.

## Where the conversion elements sit, and why

- **Phone number**: top-right of every page, and a sticky call bar on phones — thumb-reachable without scrolling.
- **Step One form**: lives on the contact page only, loaded lazily so it never slows the page down. Every other page ends in a call-to-action band that links straight to it (`/contact/#form`) — one clear conversion path instead of a heavy form repeated on every page.
- **Coraline chat widget**: on every page, bottom-right. It loads a moment after the page renders (or on first scroll/tap) so it costs nothing on page speed, and on phones it sits above the call bar instead of covering it. Chats land in Coraline.
- **Trust signals**: the "young agency, honest about it" positioning, plain-cost answers in every FAQ, and the Matthew 5:13 story on the About page.

## Launch checklist (in order)

1. ~~Import the GitHub repo into Vercel~~ (you're doing this) — Framework Preset: **Other**, no settings changes.
2. Point `saltservicesusa.com` (both `www` and bare) at the Vercel project under Domains.
3. **Submit a test lead** through the Step One form on the live site and confirm it appears in Coraline.
4. Replace the TODOs (all marked in the files):
   - Founder name / photo / year founded on the About page (`_build/pages_content.py`)
   - Business hours in `site.config.json`
   - Google Search Console verification tag (see below)
5. Claim/confirm the **Google Business Profile** for Salt Services (Kodak, TN service-area business, hide street address). Once live, add a "Leave us a review" link to the site footer.
6. **Google Search Console**: add the property, paste the verification meta tag into `_build/gen.py` (the marked TODO slot), regenerate, push. Then submit `https://www.saltservicesusa.com/sitemap.xml`.
7. When the first testimonials come in, send them over — real quotes with names convert far better than anything written for you, and they're deliberately absent rather than invented.

## Draft copy flagged for your review

Everything on the site was written fresh. A few statements are *plausible but unconfirmed* — read these pages once and correct anything that isn't exactly true:

- "You own your ad accounts and your data" and "flat management fee, no percentage of spend" (digital advertising page)
- "We return calls the same business day" (contact page)
- "Weeks, not months" implementation timelines (CRM + web design pages)
- The founder story framing on the About page (based on your old site's wording)

## Making changes

**Edit your site with Claude** (recommended): open this link, describe the change in plain English, and Claude will make it on a preview branch you approve before it goes live:

https://claude.ai/code?repositories=fdarnell/salt-services-usa.com&prompt=I%20want%20to%20make%20a%20change%20to%20my%20business%20website%20in%20this%20repo.%20Ask%20me%20what%20I%27d%20like%20to%20change%2C%20then%20make%20the%20edit.%20Keep%20the%20site%27s%20existing%20design%2C%20follow%20the%20conventions%20in%20README.md%2C%20and%20never%20edit%20main%20directly%20%E2%80%94%20put%20changes%20on%20a%20branch%20so%20I%20get%20a%20preview%20link%20to%20approve.

How it works: every change goes on a branch → Vercel generates a private preview link → nothing touches the live site until the branch is merged. Keep merge rights with whoever should approve changes.

Manual editing is documented in `README.md`.

## Screenshots

Desktop and mobile screenshots of every page are in `_build/screenshots/` in the repo.
