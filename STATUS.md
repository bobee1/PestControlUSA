# PestHalt — Build Status

**Site:** PestHalt · nationwide pest control referral site · target domain **pesthalt.us** (not yet purchased)
**Repo:** github.com/bobee1/PestControlUSA · **Owner/operator:** Anjam Javed
**Phone (temporary):** (800) 555-0199 → replace with the real toll-free number before launch
**Last updated:** 2026-11-26 (Build 38)

## Previous step — Build 37: city pages batch 35 ✅
- Santa Maria, West Covina, El Monte, Menifee, Jurupa Valley (CA); South Fulton GA; Sparks NV; Riverview FL; Allen TX; Centennial CO.

## Current step — Build 38: city pages batch 36 ✅ complete
- **Cities live:** Rio Rancho NM, Davie FL, Nampa ID, Boulder CO, Columbia MD, Inglewood, Burbank, El Cajon, Rialto, San Mateo (CA).
- **Keyword highlights (Semrush US):** rodent control El Cajon 110 (KD 4); termite control El Cajon 70 (KD 4); pest control Nampa 480 (KD 10); pest control El Cajon 260 (KD 10); pest control San Mateo 210 (KD 11); rodent control San Mateo 260 (KD 14); pest control Columbia MD 170 (KD 15).
- **City-specific topics:** kissing bugs and pack rats (Rio Rancho), cane toads and pets (Davie), canals and West Nile (Nampa), bears and trash rules (Boulder), camel crickets in basements (Columbia), rats displaced by stadium-area construction (Inglewood), pantry moths and beetles (Burbank), heat treatment for drywood termites (El Cajon), checking California pest control licenses (Rialto), attic cleanup after rats (San Mateo).
- **Checks:** 435 pages, 0 issues; batch uniqueness 68–83%; responsive 360/768/1280 clean.

## Coming next — Build 39: city pages batch 37 (10 cities)
- Proposed: Lee's Summit MO, Edinburg TX, Daly City, Vacaville and Chico (CA), Bend OR, Highlands Ranch CO, Quincy MA, Fishers IN, Albany NY.
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
