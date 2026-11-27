# PestHalt — Build Status

**Site:** PestHalt · nationwide pest control referral site · target domain **pesthalt.us** (not yet purchased)
**Repo:** github.com/bobee1/PestControlUSA · **Owner/operator:** Anjam Javed
**Phone (temporary):** (800) 555-0199 → replace with the real toll-free number before launch
**Last updated:** 2026-11-26 (Build 18)

## Previous step — Build 17: city pages batch 15 ✅
- Buffalo, Rochester NY, Syracuse, Yonkers, Worcester, Springfield MA, Hartford, New Haven, Bridgeport, Allentown.

## Current step — Build 18: city pages batch 16 ✅ complete (Deep South second tier)
- **Cities live:** Columbia and Greenville (SC), Augusta and Columbus (GA), Huntsville, Montgomery and Mobile (AL), Jackson (MS), Little Rock (AR), Shreveport (LA).
- **Keyword highlights (Semrush US):** termite control Huntsville 210 (KD 11); pest control Greenville SC 880 (KD 12); pest control Huntsville AL 880 (KD 14); pest control Jackson MS 390 (KD 15) and exterminator Jackson MS KD 15; termite control Columbia SC KD 17; pest control Columbia SC 1,300 (KD 25). Little Rock head terms are hard (KD 44–49).
- **City-specific topics:** river mosquitoes and Congaree (Columbia), kudzu bugs (Greenville), Masters Week rentals (Augusta), military move checklist (Columbus), termite baits vs liquid (Huntsville), pecan trees, squirrels and roof rats (Montgomery), fire ants' arrival through the Port of Mobile (Mobile), West Nile (Jackson), tick-borne illness in Arkansas (Little Rock), brown recluses (Shreveport).
- **Data fix:** removed a duplicate Columbus, GA row from the places file.
- **Checks:** 236 pages, 0 issues; batch uniqueness 73–81%; responsive 360/768/1280 clean.

## Coming next — Build 19: city pages batch 17 (10 cities)
- Proposed: Virginia and Carolinas third tier plus Tennessee suburbs: Alexandria and Arlington (VA), Newport News and Hampton (VA), Cary, Fayetteville, Wilmington and High Point (NC), Clarksville and Murfreesboro (TN).

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
