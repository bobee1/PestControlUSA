# PestHalt — Build Status

**Site:** PestHalt · nationwide pest control referral site · target domain **pesthalt.us** (not yet purchased)
**Repo:** github.com/bobee1/PestControlUSA · **Owner/operator:** Anjam Javed
**Phone (temporary):** (800) 555-0199 → replace with the real toll-free number before launch
**Last updated:** 2026-11-26 (Build 2)

## Previous step — Build 1: core site + legal pages ✅
- Home, services hub, 13 service pages, locations hub, about, contact (+ Resend form), disclaimer, editorial policy, privacy, terms, accessibility, 404, sitemap, robots, headers, redirects.

## Current step — Build 2: state pages + glossary ✅ complete
- **City scope decided by owner:** cities with **25,000+ population** first (2020 Census). Dataset: `tools/data/places_25k.csv`, **1,855 places** (1,553 incorporated cities + 300 large census-designated places + Washington, DC), with county, population, housing units and coordinates. Source: 2020 Census place data via the bdurand/us_geo GitHub mirror (census.gov is unreachable from the build environment).
- **51 state pages** at `/locations/{state}/` (50 states + DC), each with: H1 "Pest Control in {State}", quick answer, city stats, "why pest control here is different" (unique local text), common-problems table linking services, pest season calendar, local tips, state licensing agency and rules, full table of every 25k+ city with county and population, 4 FAQs, all 13 service cards, neighboring-state links.
- **Uniqueness (5-word shingles vs all other state pages):** lowest 62% (New Hampshire), average 73%. Target was 60%+. Word counts 870–2,500.
- **Glossary** at `/glossary/`: 55 terms, A–Z jump links, anchors, DefinedTermSet schema; first mention of up to 4 terms on each service and state page auto-links to the glossary.
- **Navigation:** Locations dropdown with all 51 states; footer links the glossary; service-page "near you" pills, home "Areas served" and the locations hub now link to state pages.
- Audit: **76 pages, 0 issues** (location uniqueness check added to `tools/audit.py`). Responsive OK at 360/768/1280; no console errors.

## Coming next — Build 3: city pages, batch 1
- City pages at `/locations/{state}/{city}/` for the 1,855 places over 25,000, built in batches by state, starting with the highest-demand states (Texas, Florida, California, Georgia, Arizona, North Carolina).
- Each city page: 800–1,200 words, 60%+ unique, real local entities (county, ZIP codes, neighborhoods, landmarks, housing age), common-problems table, FAQ "Do you cover all of {City}?", links to 3 nearby cities.
- State pages' city tables will link to each city page as it goes live.
- Proposed batch size: about 25–40 cities per build, so each page gets real local research rather than templates.

## Later builds
- Remaining city batches until all 1,855 places are live; then towns under 25,000 if wanted.
- Blog hub + posts following the Blog Post Criteria doc.
- City × service pages for top metros where Semrush shows volume.

## Deploy (Cloudflare Pages, Git-connected)
- Build command: *(none)* · **Build output directory: `public`** · Functions directory: `functions` (auto-detected at repo root)
- Environment variables: `RESEND_API_KEY`, `LEAD_TO_EMAIL`, `LEAD_FROM_EMAIL`
- To rebuild locally after edits: `python3 tools/build.py && python3 tools/audit.py`

## Open decisions for the owner
1. Confirm pesthalt.us is free and buy it (or pick the backup).
2. Real phone number to replace (800) 555-0199.
3. ~~City scope~~ decided: 25,000+ population first (1,855 places).
4. Email address for the site (none shown until approved).
