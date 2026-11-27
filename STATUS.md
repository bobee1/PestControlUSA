# PestHalt — Build Status

**Site:** PestHalt · nationwide pest control referral site · target domain **pesthalt.us** (not yet purchased)
**Repo:** github.com/bobee1/PestControlUSA · **Owner/operator:** Anjam Javed
**Phone (temporary):** (800) 555-0199 → replace with the real toll-free number before launch
**Last updated:** 2026-11-26 (Build 35)

## Previous step — Build 34: city pages batch 32 ✅
- Orange, Victorville, Santa Clara, Simi Valley, Thousand Oaks, Vallejo, Concord, Clovis, Berkeley, Fairfield (CA).

## Current step — Build 35: city pages batch 33 ✅ complete
- **Cities live:** Lehigh Acres, Spring Hill, Brandon (FL); Arvada, Westminster (CO); Richardson TX; West Jordan UT; Broken Arrow OK; Antioch, Carlsbad (CA).
- **Keyword highlights (Semrush US):** exterminator West Jordan 70 (KD 6); pest control Arvada 210 (KD 7); termite inspection Carlsbad 110 (KD 7); pest control West Jordan 90 (KD 9); pest control Carlsbad 390 (KD 13); pest control Broken Arrow 390 (KD 22); pest control Spring Hill FL 480 (KD 26).
- **City-specific topics:** pests from vacant lots (Lehigh Acres), slab cracks and termites in sinkhole country (Spring Hill), chinch bugs and lawn pests (Brandon), elm seed bugs (Arvada), wildlife along open space (Westminster), alleys and rats (Richardson), European paper wasps (West Jordan), termite swarms vs. flying ants (Broken Arrow), Norway rats on the waterfront (Antioch), coastal termite inspections (Carlsbad).
- **Fix:** Utah 'Metro of Kearns/Magna' census names now show as Kearns and Magna.
- **Checks:** 405 pages, 0 issues; batch uniqueness 68–79%; responsive 360/768/1280 clean.

## Coming next — Build 36: city pages batch 34 (10 cities)
- Proposed: Richmond, East Los Angeles, Downey, Murrieta, Costa Mesa, Temecula and Ventura (CA); Pueblo and Greeley (CO); Miami Gardens (FL).
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
