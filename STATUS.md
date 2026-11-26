# PestHalt — Build Status

**Site:** PestHalt · nationwide pest control referral site · target domain **pesthalt.us** (not yet purchased)
**Repo:** github.com/bobee1/PestControlUSA · **Owner/operator:** Anjam Javed
**Phone (temporary):** (800) 555-0199 → replace with the real toll-free number before launch
**Last updated:** 2026-11-26 (Build 11)

## Previous step — Build 10: city pages batch 8 ✅
- Detroit, Milwaukee, Minneapolis, St. Paul, Cleveland, Cincinnati, Omaha, Wichita, Madison, Des Moines.

## Current step — Build 11: city pages batch 9 ✅ complete (Upper South and Southeast second tier)
- **Cities live:** Lexington (KY), Knoxville and Chattanooga (TN), Greensboro, Durham and Winston-Salem (NC), Norfolk and Chesapeake (VA), Tallahassee and Cape Coral (FL).
- **Keyword highlights (Semrush US):** pest control Durham 480 (KD 14); pest control Norfolk 390 (KD 15) and rodent control Norfolk 170 (KD 14); pest control Greensboro NC 880 (KD 21) and termite control Greensboro KD 10; pest control Chattanooga 1,300 (KD 24); pest control Winston-Salem NC KD 16; mosquito control Tallahassee KD 9; exterminator Cape Coral KD 23 (pest control Cape Coral 1,600, KD 41). Lexington KY is hard (KD 58).
- **City-specific topics:** carpenter bees (Lexington), crawlspace moisture and termites (Knoxville), wildlife from wooded ridges (Chattanooga), NC Wood-Destroying Insect Information Report in home sales (Greensboro), mill houses and termites (Durham), stink bugs (Winston-Salem), tidal flooding and rats (Norfolk), Great Dismal Swamp and the Mosquito Control Commission (Chesapeake), live oak canopy roads and smokybrown roaches (Tallahassee), termites after Hurricane Ian (Cape Coral).
- **Local facts used:** Lexington–Fayette merger (1974) and urban growth boundary; Naval Station Norfolk; Lee County Mosquito Control District; Cape Coral's 400+ miles of canals and protected burrowing owls; Hurricane Ian (Sept 2022).
- **Template fix:** nearby paragraph no longer reads "including the rest of…" when a city has no 25k+ neighbours.
- **Checks:** 166 pages, 0 issues; batch uniqueness 76–87%; responsive 360/768/1280 clean. South Dakota state page holding at 61%.

## Coming next — Build 12: city pages batch 10 (10 cities)
- Proposed: Texas second tier: Laredo, Lubbock, Amarillo, Brownsville, McAllen, and DFW suburbs Garland, Irving, Grand Prairie, Frisco, McKinney.

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
