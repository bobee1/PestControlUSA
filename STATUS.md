# PestHalt — Build Status

**Site:** PestHalt · nationwide pest control referral site · target domain **pesthalt.us** (not yet purchased)
**Repo:** github.com/bobee1/PestControlUSA · **Owner/operator:** Anjam Javed
**Phone (temporary):** (800) 555-0199 → replace with the real toll-free number before launch
**Last updated:** 2026-11-26 (Build 21)

## Previous step — Build 20: city pages batch 18 ✅
- Vancouver WA, Bellevue, Kent, Everett, Renton, Spokane Valley, Salem, Eugene, Gresham, Hillsboro.

## Current step — Build 21: city pages batch 19 ✅ complete (California third tier)
- **Cities live:** Santa Clarita, Glendale, Huntington Beach, Garden Grove, Oxnard, Ontario, Rancho Cucamonga, Oceanside, Elk Grove, Santa Rosa.
- **Keyword highlights (Semrush US):** termite control Oceanside KD 3, bee removal Oceanside KD 3, exterminator Oceanside KD 5; exterminator Ontario CA KD 8 and pest control Ontario CA KD 9; pest control Oceanside 320 (KD 9); rodent control Glendale CA KD 9; ant control Elk Grove KD 9; rodent control Santa Clarita 140 (KD 13); pest control Elk Grove 720 (KD 15); rodent control Santa Rosa 390 (KD 19).
- **City-specific topics:** ground squirrels and gophers on slopes (Santa Clarita), roof rats in ivy and palms (Glendale), invasive Aedes mosquitoes (Huntington Beach), restaurant and market pest control in Little Saigon (Garden Grove), coastal moisture pests (Oxnard), former dairies and new neighborhoods (Ontario), brown widow spiders (Rancho Cucamonga), live bee removal (Oceanside), wetlands and West Nile (Elk Grove), pest-proofing homes rebuilt after the Tubbs and Glass fires (Santa Rosa).
- **Checks:** 266 pages, 0 issues; batch uniqueness 72–81%; responsive 360/768/1280 clean.

## Coming next — Build 22: city pages batch 20 (10 cities)
- Proposed: Texas third tier: Pasadena, Killeen, Denton, Waco, Round Rock, Carrollton, Midland, Odessa, Abilene, Beaumont.

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
