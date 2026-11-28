# PestHalt — Build Status

**Site:** PestHalt · nationwide pest control referral site · target domain **pesthalt.us** (not yet purchased)
**Repo:** github.com/bobee1/PestControlUSA · **Owner/operator:** Anjam Javed
**Phone (temporary):** (800) 555-0199 → replace with the real toll-free number before launch
**Last updated:** 2026-11-26 (Build 39)

## Previous step — Build 38: city pages batch 36 ✅
- Rio Rancho NM, Davie FL, Nampa ID, Boulder CO, Columbia MD, Inglewood, Burbank, El Cajon, Rialto, San Mateo (CA).

## Current step — Build 39: city pages batch 37 ✅ complete
- **Cities live:** Lee's Summit MO, Edinburg TX, Daly City, Vacaville, Chico (CA), Bend OR, Highlands Ranch CO, Quincy MA, Fishers IN, Albany NY.
- **Keyword highlights (Semrush US):** pest control Lee's Summit 170 (KD 5); exterminator Highlands Ranch 110 (KD 5); pest control Daly City 50 (KD 7); pest control Quincy MA 110 (KD 12); pest control Highlands Ranch 210 (KD 13); mosquito control Fishers 110 (KD 15); pest control Albany NY 720 (KD 30).
- **City-specific topics:** Asian lady beetles (Lee's Summit), Africanized bees' first U.S. detection in Hidalgo County (Edinburg), rodents in attached Westlake-style homes (Daly City), heat-wave ant invasions (Vacaville), rice fields and West Nile (Chico), pest-proofing vacation rentals (Bend), Japanese beetles (Highlands Ranch), deer ticks near the Blue Hills (Quincy), mosquitoes around Geist Reservoir (Fishers), mice through rowhouse party walls (Albany).
- **Fix:** Census ' Town' suffixes (Braintree Town, Weymouth Town) now display as plain town names.
- **Checks:** 445 pages, 0 issues; batch uniqueness 70–79%; responsive 360/768/1280 clean.

## Coming next — Build 40: city pages batch 38 (10 cities)
- Proposed: Lynn MA, Norwalk, Hesperia and Vista (CA), Carmel IN, Buckeye AZ, San Angelo TX, Federal Way WA, Longmont CO, Roanoke VA.
- Scope rule (owner, 2026-11-27): all 50 states (Alaska and Hawaii stay) plus Washington, DC; no overseas territories.

## Later builds
- Remaining city batches until all 1,866 places are live; then towns under 25,000 if wanted.
- Blog hub + posts following the Blog Post Criteria doc.
- City × service pages for top metros where Semrush shows volume.

## Deploy (Cloudflare Pages, Git-connected)
- Build command: *(none)* · **Build output directory: `public`** · Functions directory: `functions` (auto-detected at repo root)
- Environment variables: `RESEND_API_KEY`, `LEAD_TO_EMAIL`, `LEAD_FROM_EMAIL`
- To rebuild locally after edits: `python3 tools/build.py && python3 tools/audit.py`

## Open decisions for the owner
1. Confirm pesthalt.us is free and buy it (or pick the backup).
2. Real phone number to replace (800) 555-0199.
3. ~~City scope~~ decided: 25,000+ population first (1,866 places).
4. Email address for the site (none shown until approved).
