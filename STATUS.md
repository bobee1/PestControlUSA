# PestHalt — Build Status

**Site:** PestHalt · nationwide pest control referral site · target domain **pesthalt.us** (not yet purchased)
**Repo:** github.com/bobee1/PestControlUSA · **Owner/operator:** Anjam Javed
**Phone (temporary):** (800) 555-0199 → replace with the real toll-free number before launch
**Last updated:** 2026-11-26 (Build 4)

## Previous step — Build 3: city pages batch 1 ✅
- Houston, San Antonio, Dallas, Austin, Fort Worth, Jacksonville, Miami, Tampa, Orlando, St. Petersburg.

## Current step — Build 4: city pages batch 2 ✅ complete (10 cities)
- **Cities live:** El Paso, Arlington, Corpus Christi, Plano (TX); Hialeah, Fort Lauderdale (FL); Phoenix, Tucson, Mesa, Scottsdale (AZ). First Arizona city pages.
- **Keyword highlights (Semrush US):** pest control Phoenix 4,400/mo (KD 29); termite control Phoenix 1,600 ($32.33, KD 26); rodent control Phoenix 1,600 (KD 17); pest control Tucson 3,600; pest control El Paso 1,300 (KD 24); pest control Scottsdale 1,000 (KD 24); pest control Hialeah KD 9.
- **City-specific topics:** scorpions and the Franklin Mountains (El Paso), apartments and bed bugs near UTA (Arlington), coastal humidity and hurricanes (Corpus Christi), greenbelts and attic pests (Plano), dense shared-wall housing (Hialeah), termite tenting (Fort Lauderdale), bark scorpions in the Valley (Phoenix), pack rats and wiring damage (Tucson), snowbird seasonal homes (Mesa), desert-edge living (Scottsdale).
- **Verified local events used:** El Paso flood (Aug 2006), Hurricane Celia (1970) and Harvey (2017) for Corpus Christi, Fort Lauderdale record rainfall (Apr 2023), Phoenix 31 straight days at 110°F+ (Jul 2023), roof rats confirmed in Arcadia (~2001).
- **Data:** `tools/data/city_zips.json` now holds primary ZIP codes for all 1,795 places that have them (59 places have no primary ZIP in the data and will need a fallback).
- **Checks:** 96 pages, 0 issues; city uniqueness 82–91%; every city has 3–5 in-text inbound links (new audit check); responsive 360/768/1280 with no overflow or console errors.

## Coming next — Build 5: city pages batch 3 (10 cities)
- Proposed: California's largest cities: Los Angeles, San Diego, San Jose, San Francisco, Fresno, Sacramento, Long Beach, Oakland, Bakersfield, Anaheim.
- California adds drywood termite tenting, Argentine ants, roof rats and Structural Pest Control Board rules at city level.

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
