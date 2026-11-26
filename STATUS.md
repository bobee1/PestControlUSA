# PestHalt — Build Status

**Site:** PestHalt · nationwide pest control referral site · target domain **pesthalt.us** (not yet purchased)
**Repo:** github.com/bobee1/PestControlUSA · **Owner/operator:** Anjam Javed
**Phone (temporary):** (800) 555-0199 → replace with the real toll-free number before launch
**Last updated:** 2026-11-26 (Build 10)

## Previous step — Build 9: city pages batch 7 ✅
- Seattle, Portland, Spokane, Tacoma, Boise, Salt Lake City, Albuquerque, Colorado Springs, Anchorage, Honolulu.

## Current step — Build 10: city pages batch 8 ✅ complete (Great Lakes and Plains)
- **Cities live:** Detroit (MI), Milwaukee and Madison (WI), Minneapolis and St. Paul (MN), Cleveland and Cincinnati (OH), Omaha (NE), Wichita (KS), Des Moines (IA).
- **Keyword highlights (Semrush US):** pest control St. Paul 1,000 (KD 20) and exterminator St. Paul KD 19; pest control Detroit 1,000 (KD 21) and rodent control Detroit 210 (KD 0); termite control Cincinnati KD 12; bed bug exterminator Milwaukee KD 5; mouse exterminator Minneapolis 170 (KD 7); wasp removal Minneapolis KD 6; mosquito control Omaha 140 (KD 13); pest control Omaha 1,900.
- **City-specific topics:** vacant lots, demolitions and rats (Detroit), fall invaders in attics and wall voids (Milwaukee), lakes and the Metropolitan Mosquito Control District (Minneapolis), bats and squirrels in Victorian homes (St. Paul), Cleveland doubles (Cleveland), Ohio Valley termites (Cincinnati), river floods and mosquitoes (Omaha), brown recluse spiders (Wichita), ticks and Lyme risk (Madison), damp basements and moisture pests (Des Moines).
- **Local facts used:** Detroit's 2014 and June 2021 basement floods and blight demolitions; Milwaukee duplexes and Polish flats; Minnesota's first emerald ash borer find in St. Paul (2009); Missouri River flooding in March 2019; Planeview built for aircraft workers; Madison's mid-August lease turnover and lake flies; Des Moines floods of 1993 and 2008.
- **Checks:** 156 pages, 0 issues; batch uniqueness 77–86%; responsive 360/768/1280 clean. South Dakota state page holding at 61%.

## Coming next — Build 11: city pages batch 9 (10 cities)
- Proposed: Upper South and Southeast second tier: Lexington (KY), Knoxville and Chattanooga (TN), Greensboro, Durham and Winston-Salem (NC), Norfolk and Chesapeake (VA), Tallahassee and Cape Coral (FL).

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
