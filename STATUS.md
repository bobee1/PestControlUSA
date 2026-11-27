# PestHalt — Build Status

**Site:** PestHalt · nationwide pest control referral site · target domain **pesthalt.us** (not yet purchased)
**Repo:** github.com/bobee1/PestControlUSA · **Owner/operator:** Anjam Javed
**Phone (temporary):** (800) 555-0199 → replace with the real toll-free number before launch
**Last updated:** 2026-11-26 (Build 22)

## Previous step — Build 21: city pages batch 19 ✅
- Santa Clarita, Glendale CA, Huntington Beach, Garden Grove, Oxnard, Ontario CA, Rancho Cucamonga, Oceanside, Elk Grove, Santa Rosa.

## Current step — Build 22: city pages batch 20 ✅ complete (Texas third tier)
- **Cities live:** Pasadena, Killeen, Denton, Waco, Round Rock, Carrollton, Midland, Odessa, Abilene, Beaumont.
- **Keyword highlights (Semrush US):** exterminator Abilene KD 0 and pest control Abilene KD 9; mosquito control Beaumont KD 6; pest control Carrollton 320 (KD 12); exterminator Killeen KD 13; pest control Denton 390 (KD 18); pest control Round Rock 720 (KD 19); pest control Killeen 480 (KD 20). Beaumont and Odessa head terms are harder (KD 43–46).
- **City-specific topics:** rats along the Ship Channel (Pasadena), move-out inspections for rentals near Fort Hood (Killeen), paper wasps and yellowjackets (Denton), termite damage found during renovations (Waco), creek-greenbelt wildlife (Round Rock), brown recluses in garages and attics (Carrollton), oilfield offices and yards (Midland), mice and pack rats in RVs and manufactured homes (Odessa), pack rats around ranchettes (Abilene), floods and the Jefferson County Mosquito Control District (Beaumont).
- **Checks:** 276 pages, 0 issues; batch uniqueness 73–81%; responsive 360/768/1280 clean.

## Coming next — Build 23: city pages batch 21 (10 cities)
- Proposed: Southwest and Mountain third tier: Tempe, Surprise, Goodyear, Yuma and Flagstaff (AZ); Las Cruces (NM); Provo, Orem, West Valley City and St. George (UT).

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
