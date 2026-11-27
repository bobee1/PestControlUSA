# PestHalt — Build Status

**Site:** PestHalt · nationwide pest control referral site · target domain **pesthalt.us** (not yet purchased)
**Repo:** github.com/bobee1/PestControlUSA · **Owner/operator:** Anjam Javed
**Phone (temporary):** (800) 555-0199 → replace with the real toll-free number before launch
**Last updated:** 2026-11-26 (Build 34)

## Previous step — Build 33: city pages batch 31 ✅
- Paradise, Enterprise, Spring Valley, Sunrise Manor (NV); Columbia MO, Topeka KS, Meridian ID, Lafayette LA, Billings MT, Lewisville TX.

## Current step — Build 34: city pages batch 32 ✅ complete
- **Cities live:** Orange, Victorville, Santa Clara, Simi Valley, Thousand Oaks, Vallejo, Concord, Clovis, Berkeley, Fairfield (CA).
- **Keyword highlights (Semrush US):** pest control Santa Clara 210 (KD 5); pest control Concord CA 210 (KD 7); pest control Vallejo 170 (KD 8); rodent control Thousand Oaks 110 (KD 9); pest control Berkeley 140 (KD 10); termite inspection Orange County 260 (KD 21).
- **City-specific topics:** termite inspections for Old Towne historic homes (Orange), moisture pests in irrigated desert yards (Victorville), rodent control for offices and data centers (Santa Clara), rodents drawing rattlesnakes (Simi Valley), wildlife-safe rodent control and California's rodenticide limits (Thousand Oaks), dampwood termites (Vallejo), backyard chicken coops and rats (Concord), canals and mosquitoes (Clovis), IPM and low-toxicity methods (Berkeley), move-in pest checks for Travis AFB families (Fairfield).
- **Checks:** 395 pages, 0 issues; batch uniqueness 73–80%; responsive 360/768/1280 clean.

## Coming next — Build 35: city pages batch 33 (10 cities)
- Proposed: Lehigh Acres, Spring Hill and Brandon (FL); Arvada and Westminster (CO); Richardson TX; West Jordan UT; Broken Arrow OK; Antioch and Carlsbad (CA).
- Scope rule (owner, 2026-11-27): all 50 states (Alaska and Hawaii stay) plus Washington, DC; no overseas territories.

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
