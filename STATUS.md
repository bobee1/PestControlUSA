# PestHalt — Build Status

**Site:** PestHalt · nationwide pest control referral site · target domain **pesthalt.us** (not yet purchased)
**Repo:** github.com/bobee1/PestControlUSA · **Owner/operator:** Anjam Javed
**Phone (temporary):** (800) 555-0199 → replace with the real toll-free number before launch
**Last updated:** 2026-11-26 (Build 27)

## Previous step — Build 26: city pages batch 24 ✅
- Paterson, Elizabeth, Lowell, Cambridge, New Bedford, Brockton, Stamford, Waterbury, Manchester NH, Portland ME.

## Current step — Build 27: city pages batch 25 ✅ complete (Florida fourth tier)
- **Cities live:** Fort Myers, Sarasota, Daytona Beach, Melbourne, Pompano Beach, Boca Raton, Deltona, Palm Coast, Kissimmee, Ocala.
- **Keyword highlights (Semrush US):** rodent control Sarasota 480 (KD 9); pest control Deltona KD 12; pest control Daytona Beach 590 (KD 14); rodent control Boca Raton KD 14; termite control Sarasota 170 (KD 15) and termite control Boca Raton KD 15; pest control Palm Coast 320 (KD 16); exterminator Ocala KD 16; pest control Kissimmee 590 (KD 21). Ocala head terms are hard (KD 42–43).
- **City-specific topics:** seasonal homes (Fort Myers), roof rats in tropical landscaping (Sarasota), lovebugs (Daytona Beach), salt marsh mosquitoes and lagoon impoundments (Melbourne), big-headed ants (Pompano Beach), drywood termites in Mizner-era homes (Boca Raton), fire ants in sandy yards (Deltona), ticks and fleas on wooded lots (Palm Coast), Lake Toho midges (Kissimmee), flies on horse farms (Ocala).
- **Link planner fix:** the inbound-link top-up now skips neighbours that already list the city as nearby (fixed Fort Myers).
- **Checks:** 326 pages, 0 issues; batch uniqueness 73–83%; responsive 360/768/1280 clean.

## Coming next — Build 28: city pages batch 26 (10 cities)
- Proposed: Georgia, Carolinas and Alabama fourth tier: Athens, Macon, Sandy Springs, Roswell and Johns Creek (GA); North Charleston, Mount Pleasant and Rock Hill (SC); Concord (NC); Tuscaloosa (AL).

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
