# PestHalt — Build Status

**Site:** PestHalt · nationwide pest control referral site · target domain **pesthalt.us** (not yet purchased)
**Repo:** github.com/bobee1/PestControlUSA · **Owner/operator:** Anjam Javed
**Phone (temporary):** (800) 555-0199 → replace with the real toll-free number before launch
**Last updated:** 2026-11-26 (Build 3)

## Previous step — Build 2: state pages + glossary ✅
- 51 state pages (`/locations/{state}/`) with unique local content and full 25k+ city tables; glossary (55 terms) with auto-links; Locations dropdown.

## Current step — Build 3: city pages, batch 1 ✅ complete (10 cities)
- Owner direction: short batches, no compromise on quality, fully relevant, optimized and semantic.
- **Cities live:** Houston, San Antonio, Dallas, Austin, Fort Worth (TX); Jacksonville, Miami, Tampa, Orlando, St. Petersburg (FL), at `/locations/{state}/{city}/`.
- **Research per city:** Semrush city keywords (primary + 3 secondary), 2020 Census population and housing units, primary ZIP codes (2020 ZCTA data), 12 named neighborhoods, landmarks and waterways, housing types and eras, verified local events (Harvey 2017, Imelda 2019, Dallas West Nile outbreak 2012, Winter Storm Uri 2021, Irma 2017 river flooding, Wynwood Zika 2016, Ian 2022, Helene and Milton 2024).
- **Each page:** H1 "Pest Control in {City}, {ST}", quick answer, census stats, "why pest control here is different", local problems table linking services, a city-specific topic section (e.g. Formosan termites and flooding in Houston, scorpions in West Austin, condo pest control in Miami, tent fumigation in Tampa), pest calendar, resident tips, 4 FAQs incl. "Do you cover all of {City}?" with ZIP codes, all service cards, nearby 25k+ communities within 35 miles, links to 3 nearest city guides + state page.
- **Schema:** WebPage (about Service + Pest control; mentions City with Wikipedia sameAs, containedInPlace county → state), Service (areaServed City), FAQPage, BreadcrumbList.
- **Internal links:** state pages link city names in their tables plus an in-text "city guides" sentence; service pages' Local note links 3–5 city guides with varied anchors; every city gets 3–5 in-text inbound links.
- **Quality checks:** uniqueness 88–91% per city (5-word shingles vs all 61 location pages); 960–1,100 words; audit 86 pages, 0 issues; responsive 360/1280 OK; no console errors.

## Coming next — Build 4: city pages, batch 2 (10 cities)
- Proposed: next-largest cities in Texas and Florida plus Arizona's top metros: El Paso, Arlington, Corpus Christi, Plano (TX); Hialeah, Fort Lauderdale (FL); Phoenix, Tucson, Mesa, Scottsdale (AZ).
- Same research depth and page structure; nearby-city links will interlink across batches automatically.

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
