# PestHalt — Build Status

**Site:** PestHalt · nationwide pest control referral site · target domain **pesthalt.us** (not yet purchased)
**Repo:** github.com/bobee1/PestControlUSA · **Owner/operator:** Anjam Javed
**Phone (temporary):** (800) 555-0199 → replace with the real toll-free number before launch
**Last updated:** 2026-11-26 (Build 36)

## Previous step — Build 35: city pages batch 33 ✅
- Lehigh Acres, Spring Hill, Brandon (FL); Arvada, Westminster (CO); Richardson TX; West Jordan UT; Broken Arrow OK; Antioch, Carlsbad (CA).

## Current step — Build 36: city pages batch 34 ✅ complete
- **Cities live:** Richmond, East Los Angeles, Downey, Murrieta, Costa Mesa, Temecula, Ventura (CA); Pueblo, Greeley (CO); Miami Gardens (FL).
- **Keyword highlights (Semrush US):** pest control Richmond CA 50 (KD 6); pest control Pueblo 320 (KD 10); pest control Costa Mesa 720 (KD 11); pest control Greeley CO 170 (KD 13); pest control Miami Gardens 170 (KD 15); pest control Murrieta 480 (KD 21); pest control Temecula 720 (KD 29).
- **City-specific topics:** rats and roaches in WWII-era housing (Richmond), pests in converted garages and backyard units (East LA), roof rats and backyard fruit trees (Downey), telling bees, yellowjackets and carpenter bees apart (Murrieta), mosquitoes near the Back Bay and Fairview Park (Costa Mesa), yellowjackets at patios and pools (Temecula), hillside rodent control (Ventura), black widows (Pueblo), flies near Weld County agriculture (Greeley), Aedes aegypti and dengue alerts (Miami Gardens).
- **Checks:** 415 pages, 0 issues; batch uniqueness 71–79%; responsive 360/768/1280 clean.

## Coming next — Build 37: city pages batch 35 (10 cities)
- Proposed: Santa Maria, West Covina, El Monte, Menifee, Jurupa Valley (CA); South Fulton (GA); Sparks (NV); Riverview (FL); Allen (TX); Centennial (CO).
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
