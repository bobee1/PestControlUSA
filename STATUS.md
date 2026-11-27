# PestHalt — Build Status

**Site:** PestHalt · nationwide pest control referral site · target domain **pesthalt.us** (not yet purchased)
**Repo:** github.com/bobee1/PestControlUSA · **Owner/operator:** Anjam Javed
**Phone (temporary):** (800) 555-0199 → replace with the real toll-free number before launch
**Last updated:** 2026-11-26 (Build 29)

## Previous step — Build 28: city pages batch 26 ✅
- Athens, Macon, Sandy Springs, Roswell, Johns Creek, North Charleston, Mount Pleasant, Rock Hill, Concord NC, Tuscaloosa.

## Current step — Build 29: state page pass 2 + city pages batch 27 ✅ complete
- **State pass:** new state-specific sections for South Carolina, Pennsylvania, Missouri, Iowa, Maine, Vermont and Indiana, plus an extra paragraph for Wyoming, Kansas, South Dakota, West Virginia and New Hampshire. Facts used include Clemson's role as SC pesticide regulator, the stink bug's first U.S. find near Allentown, Pennsylvania's lanternfly quarantine, Missouri tick-borne illness rates, Iowa floods and the 2020 derecho, Maine's browntail moth and Board of Pesticides Control, Vermont cluster flies. All state pages now 66%+.
- **Cities live:** Sugar Land, The Woodlands, Pearland, League City, Conroe, New Braunfels, San Marcos, College Station, Tyler, Wichita Falls.
- **Keyword highlights (Semrush US):** mosquito control The Woodlands 140 (KD 2); exterminator Sugar Land KD 7; mosquito control League City 170 (KD 9); exterminator The Woodlands KD 10; mosquito control Sugar Land 170 (KD 10); pest control Sugar Land 720 (KD 12); pest control The Woodlands 720 (KD 14); pest control Conroe KD 16; pest control New Braunfels 390 (KD 17).
- **City-specific topics:** Brazos floods and pests (Sugar Land), rats and squirrels in the pine canopy (The Woodlands), tawny crazy ants (Pearland), Galveston Bay mosquitoes (League City), lakefront docks and termites (Conroe), river cabins and vacation rentals (New Braunfels), leafcutter ants (San Marcos), student housing (College Station), Piney Woods termites (Tyler), drought-driven pests (Wichita Falls).
- **Checks:** 346 pages, 0 issues; batch uniqueness 73–82%; responsive 360/768/1280 clean.

## Coming next — Build 30: city pages batch 28 (10 cities)
- Proposed: Ohio and Pennsylvania third tier: Dayton, Youngstown, Canton and Parma (OH); Erie, Reading, Scranton, Lancaster, Bethlehem and Harrisburg (PA).

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
