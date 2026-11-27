# PestHalt — Build Status

**Site:** PestHalt · nationwide pest control referral site · target domain **pesthalt.us** (not yet purchased)
**Repo:** github.com/bobee1/PestControlUSA · **Owner/operator:** Anjam Javed
**Phone (temporary):** (800) 555-0199 → replace with the real toll-free number before launch
**Last updated:** 2026-11-26 (Build 28)

## Previous step — Build 27: city pages batch 25 ✅
- Fort Myers, Sarasota, Daytona Beach, Melbourne, Pompano Beach, Boca Raton, Deltona, Palm Coast, Kissimmee, Ocala; link planner fix.

## Current step — Build 28: city pages batch 26 ✅ complete (Georgia, Carolinas, Alabama fourth tier)
- **Cities live:** Athens, Macon, Sandy Springs, Roswell and Johns Creek (GA); North Charleston, Mount Pleasant and Rock Hill (SC); Concord (NC); Tuscaloosa (AL).
- **Keyword highlights (Semrush US):** pest control Roswell GA KD 2; termite control Athens GA KD 5; mosquito control Johns Creek 210 (KD 6); pest control Mount Pleasant SC KD 7; exterminator Macon GA KD 8; termite control Rock Hill 110 (KD 8); pest control North Charleston 320 (KD 9); mosquito control Roswell GA 140 (KD 9); pest control Concord NC KD 11; pest control Tuscaloosa 390 (KD 14).
- **City-specific topics:** Joro spiders (Athens), powderpost beetles in historic homes (Macon), rats in wooded neighborhoods (Sandy Springs), ticks on greenways (Roswell), seasonal mosquito programs (Johns Creek), Navy Yard-era cottages and termites (North Charleston), docks, marshes, rats and raccoons (Mount Pleasant), what to do about termite swarms (Rock Hill), race-week lodging and campgrounds (Concord), flying squirrels in attics (Tuscaloosa).
- **Checks:** 336 pages, 0 issues; batch uniqueness 70–79%; responsive 360/768/1280 clean. Watch item: South Carolina state page now 65%.

## Coming next — Build 29: state page pass 2 + city pages batch 27
- First, add state-specific content to South Carolina, Wyoming and any other state page under 66%.
- Then 10 Texas suburbs and Hill Country cities: Sugar Land, The Woodlands, Pearland, League City, Conroe, New Braunfels, San Marcos, College Station, Tyler, Wichita Falls.

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
