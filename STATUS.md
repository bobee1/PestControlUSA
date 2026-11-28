# PestHalt — Build Status

**Site:** PestHalt · nationwide pest control referral site · target domain **pesthalt.us** (not yet purchased)
**Repo:** github.com/bobee1/PestControlUSA · **Owner/operator:** Anjam Javed
**Phone (temporary):** (800) 555-0199 → replace with the real toll-free number before launch
**Last updated:** 2026-11-26 (Build 40)

## Previous step — Build 39: city pages batch 37 ✅
- Lee's Summit MO, Edinburg TX, Daly City, Vacaville, Chico (CA), Bend OR, Highlands Ranch CO, Quincy MA, Fishers IN, Albany NY.

## Current step — Build 40: city pages batch 38 ✅ complete
- **Cities live:** Lynn MA, Norwalk, Hesperia, Vista (CA), Carmel IN, Buckeye AZ, San Angelo TX, Federal Way WA, Longmont CO, Roanoke VA.
- **Keyword highlights (Semrush US):** exterminator Hesperia 90 (KD 8); pest control Federal Way 260 (KD 11); pest control Buckeye AZ 170 (KD 11); rodent control Vista CA 70 (KD 12); pest control Longmont 480 (KD 18); pest control San Angelo 320 (KD 26).
- **City-specific topics:** carpenter ants in triple-decker porches (Lynn), Oriental cockroaches (Norwalk), tarantulas and tarantula hawks (Hesperia), ants farming aphids on citrus and avocado (Vista), cicada killers and ground-nesting bees (Carmel), rattlesnakes in new desert-edge neighborhoods (Buckeye), Concho River mosquitoes (San Angelo), moles and Washington trapping limits (Federal Way), clover mites (Longmont), stink bugs in the Roanoke Valley (Roanoke).
- **Checks:** 455 pages, 0 issues; batch uniqueness 70–80%; responsive 360/768/1280 clean.

## Coming next — Build 41: city pages batch 39 (10 cities)
- Proposed: Beaverton OR, Portsmouth and Suffolk VA, Fayetteville AR, Yakima WA, Sunrise FL, Edmond OK, Lawrence KS, Sandy UT, Asheville NC.
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
