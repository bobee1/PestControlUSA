# PestHalt — Build Status

**Site:** PestHalt · nationwide pest control referral site · target domain **pesthalt.us** (not yet purchased)
**Repo:** github.com/bobee1/PestControlUSA · **Owner/operator:** Anjam Javed
**Phone (temporary):** (800) 555-0199 → replace with the real toll-free number before launch
**Last updated:** 2026-11-26 (Build 13)

## Previous step — Build 12: city pages batch 10 ✅
- Laredo, Lubbock, Amarillo, Brownsville, McAllen, Garland, Irving, Grand Prairie, Frisco, McKinney.

## Current step — Build 13: city pages batch 11 ✅ complete (California second tier)
- **Cities live:** Riverside, San Bernardino, Fontana, Moreno Valley, Santa Ana, Irvine, Chula Vista, Stockton, Modesto, Fremont.
- **Keyword highlights (Semrush US):** pest control San Bernardino 210 (KD 8); exterminator Fontana KD 4 and pest control Fontana KD 11; exterminator Moreno Valley 170 (KD 9); bee removal Riverside KD 4 and termite control Riverside 480 (KD 15); pest control Irvine 480 (KD 12) and ant control Irvine KD 12; termite control Santa Ana KD 10; pest control Santa Ana 1,000 (KD 21); pest control Modesto 880 (KD 24).
- **City-specific topics:** bee swarms and Africanized bees (Riverside), wildfire and foothill pests (San Bernardino), warehouse pest programs (Fontana), green pools and mosquitoes (Moreno Valley), German cockroaches in apartments (Santa Ana), Argentine ant supercolonies (Irvine), termites and HOAs in attached homes (Chula Vista), Delta waterways and mosquitoes (Stockton), irrigation and perimeter pests (Modesto), rat-proofing older tract homes (Fremont).
- **Local facts used:** Riverside's navel orange heritage, Fontana's Kaiser Steel past and logistics hub, Irvine Ranch villages, San Joaquin County Mosquito and Vector Control District and Port of Stockton, Modesto Irrigation District flood irrigation, Fremont's 1956 merger of five towns.
- **Checks:** 186 pages, 0 issues; batch uniqueness 80–84%; California state page 87%; responsive 360/768/1280 clean. South Dakota state page holding at 61%.

## Coming next — Build 14: city pages batch 12 (10 cities)
- Proposed: Southwest and Mountain suburbs: Chandler, Gilbert, Glendale and Peoria (AZ), Henderson, North Las Vegas and Reno (NV), Aurora, Fort Collins and Lakewood (CO).

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
