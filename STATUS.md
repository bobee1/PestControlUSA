# PestHalt — Build Status

**Site:** PestHalt · nationwide pest control referral site · target domain **pesthalt.us** (not yet purchased)
**Repo:** github.com/bobee1/PestControlUSA · **Owner/operator:** Anjam Javed
**Phone (temporary):** (800) 555-0199 → replace with the real toll-free number before launch
**Last updated:** 2026-11-26 (Build 5)

## Previous step — Build 4: city pages batch 2 ✅
- El Paso, Arlington, Corpus Christi, Plano, Hialeah, Fort Lauderdale, Phoenix, Tucson, Mesa, Scottsdale.

## Current step — Build 5: city pages batch 3 ✅ complete (10 California cities)
- **Cities live:** Los Angeles, San Diego, San Jose, San Francisco, Fresno, Sacramento, Long Beach, Oakland, Bakersfield, Anaheim.
- **Keyword highlights (Semrush US):** pest control Sacramento 2,400 (KD 28); pest control San Diego 2,400 (KD 34); pest control Los Angeles 1,900 (KD 37); pest control San Jose 1,300 (KD 20); pest control Fresno 1,300 (KD 16); termite control Los Angeles $32.88/click; termite inspection San Diego 390 ($34.57).
- **City-specific topics:** termite tenting (LA), canyon wildlife (San Diego), orchards and roof rats (San Jose), attached-building pests (San Francisco), black widows in the Valley (Fresno), WDO Section 1/Section 2 reports (Sacramento), historic homes and drywood termites (Long Beach), hillside wildlife and yellow jackets (Oakland), heat and harvest (Bakersfield), hotels and bed bugs (Anaheim).
- **Verified local events used:** LA flea-borne typhus outbreak (2018), San Diego floods (Jan 2024), Coyote Creek flood (Feb 2017), SF IPM ordinance (1996), Oakland Hills firestorm (1991), Canyon Fire 2 in Anaheim Hills (2017), Anaheim founding as a vineyard colony (1857).
- **Linking upgrade:** each city page now links the 3 nearest same-state city guides in-text, so every city keeps 3+ in-text inbound links as batches grow (audit check caught Fresno, Bakersfield and San Diego at 2 before the fix).
- **Checks:** 106 pages, 0 issues; California city uniqueness 82–87%; responsive 360/768/1280 with no overflow or console errors.

## Coming next — Build 6: city pages batch 4 (10 cities)
- Proposed: Southeast metros: Atlanta, Charlotte, Raleigh, Nashville, Memphis, New Orleans, Baton Rouge, Birmingham, Charleston (SC), Savannah.
- Brings Formosan termites in New Orleans and Charleston, fire ants, brown recluses in Memphis and Nashville, and crawl-space homes across the Carolinas.

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
