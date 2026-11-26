# PestHalt — Build Status

**Site:** PestHalt · nationwide pest control referral site · target domain **pesthalt.us** (not yet purchased)
**Repo:** github.com/bobee1/PestControlUSA · **Owner/operator:** Anjam Javed
**Phone (temporary):** (800) 555-0199 → replace with the real toll-free number before launch
**Last updated:** 2026-11-26 (Build 12)

## Previous step — Build 11: city pages batch 9 ✅
- Lexington, Knoxville, Chattanooga, Greensboro, Durham, Winston-Salem, Norfolk, Chesapeake, Tallahassee, Cape Coral.

## Current step — Build 12: city pages batch 10 ✅ complete (Texas second tier)
- **Cities live:** Laredo, Lubbock, Amarillo, Brownsville, McAllen, Garland, Irving, Grand Prairie, Frisco, McKinney.
- **Keyword highlights (Semrush US):** pest control Irving 260 (KD 10); exterminator Brownsville KD 10 and pest control Brownsville 480 (KD 15); pest control Garland TX KD 11; exterminator McAllen KD 14; pest control Frisco TX 590 (KD 15) and pest control Frisco 880 (KD 19); pest control McKinney 1,000 (KD 22); pest control Amarillo 390 (KD 21). Lubbock is hard (KD 61).
- **City-specific topics:** kissing bugs and Chagas (Laredo), cricket swarms (Lubbock), winterizing against mice (Amarillo), Aedes mosquitoes and dengue (Brownsville), fire ants (McAllen), lake mosquitoes and West Nile (Garland), apartment pest control (Irving), roof rats (Grand Prairie), builder termite warranties (Frisco), ticks, fleas and pets (McKinney). Scorpion topics avoided because four earlier pages already cover them.
- **Local facts used:** Port Laredo as the top U.S. land port, Texas A&M kissing bug testing, Cameron County local dengue cases, Brownsville resacas, Winter Texans in RV parks, Dallas County's 2012 West Nile outbreak, McKinney's historic district.
- **Checks:** 176 pages, 0 issues; batch uniqueness 78–84%; Texas state page 80%; responsive 360/768/1280 clean. South Dakota state page holding at 61%.

## Coming next — Build 13: city pages batch 11 (10 cities)
- Proposed: California second tier: Riverside, San Bernardino, Fontana, Moreno Valley, Santa Ana, Irvine, Chula Vista, Stockton, Modesto, Fremont.

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
