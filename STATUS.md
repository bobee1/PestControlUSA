# PestHalt — Build Status

**Site:** PestHalt · nationwide pest control referral site · target domain **pesthalt.us** (not yet purchased)
**Repo:** github.com/bobee1/PestControlUSA · **Owner/operator:** Anjam Javed
**Phone (temporary):** (800) 555-0199 → replace with the real toll-free number before launch
**Last updated:** 2026-11-26

## Previous step
- Planning (2026-11-16): nationwide pest control build plan doc: market data, state tiers, architecture, rollout.

## Current step — Build 1: core site + legal pages ✅ complete
- Brand chosen: **PestHalt** (pesthalt.us). No pest control business found using the name. Confirm .us availability at Spaceship before buying; backup **bughalt.us**.
- Python static generator in `/tools` builds the site into `/public`.
- 24 pages: home, services hub, 13 service pages, locations hub (all 50 states + DC), about, contact (with callback form), disclaimer, editorial policy, privacy policy, terms, accessibility, 404.
- Utility files: sitemap.xml, robots.txt, web manifest, favicons, Cloudflare `_headers` (security + caching) and `_redirects`.
- Contact form → Cloudflare Pages Function `/functions/api/lead.js` → Resend.
- Images: 22 Pexels photos converted to WebP (600w + 1200w, all under 200 KB) + 3 SVG illustrations (bed bug, flea/tick, raccoon). Photos showing company logos or branding were removed.
- Self-audit (`python3 tools/audit.py`): **0 issues**: links, anchors, titles, metas, H1s, heading order, JSON-LD, FAQ visibility, banned wording, duplicate paragraphs, orphans, image alt/dimensions.
- Responsive checked at 360 / 768 / 1280 px: no horizontal scroll, no console errors.

## Coming next — Build 2: state pages + glossary
- 51 state pages at `/locations/{state}/` (50 states + DC): state licensing agency, climate and season, top pests, termite risk, laws, and major cities list.
- Switch every "near you" pill and hub card from anchors to the new state pages.
- Glossary (`/glossary/`, 50+ terms) with auto-links from service pages.
- Add Locations dropdown to the main nav.

## Later builds
- Build 3+: city pages in batches by state (largest-demand cities first), 800–1,200 words each, 60%+ unique, following the location-page rules.
- Blog hub + posts following the Blog Post Criteria doc (cost guides, signs-of guides, DIY vs pro).
- City × service pages for the top metros where Semrush shows volume.

## Deploy (Cloudflare Pages, Git-connected)
- Build command: *(none)* · **Build output directory: `public`** · Functions directory: `functions` (auto-detected at repo root)
- Environment variables: `RESEND_API_KEY`, `LEAD_TO_EMAIL`, `LEAD_FROM_EMAIL`
- To rebuild locally after edits: `python3 tools/build.py && python3 tools/audit.py`

## Open decisions for the owner
1. Confirm pesthalt.us is free and buy it (or pick the backup).
2. Real phone number to replace (800) 555-0199.
3. City scope for "all cities": e.g. every incorporated place, or every place above a population floor (recommended: start with 25,000+, about 1,500 places).
4. Email address for the site (none shown until approved).
