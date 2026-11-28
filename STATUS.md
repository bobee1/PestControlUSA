# PestHalt — Build Status

**Site:** PestHalt · nationwide pest control referral site · target domain **pesthalt.us** (not yet purchased)
**Repo:** github.com/bobee1/PestControlUSA · **Owner/operator:** Anjam Javed
**Phone (temporary):** (800) 555-0199 → replace with the real toll-free number before launch
**Last updated:** 2026-11-26 (Build 42)

## Previous step — Build 41: city pages batch 39 ✅
- Beaverton OR, Portsmouth and Suffolk VA, Fayetteville AR, Yakima WA, Sunrise FL, Edmond OK, Lawrence KS, Sandy UT, Asheville NC.

## Current step — Build 42: city pages batch 40 ✅ complete
- **Cities live:** Arden-Arcade, Tracy, San Marcos, Compton, Redding (CA), Livonia MI, Plantation FL, Atascocita TX, Toms River NJ, Fall River MA.
- **Keyword highlights (Semrush US):** pest control Fall River 90 (KD 10); pest control Tracy 210 (KD 13); pest control Livonia 320 (KD 13); exterminator San Marcos CA 320 (KD 15); pest control San Marcos CA 390 (KD 16); pest control Toms River 320 (KD 30). About 1,970 Semrush units left.
- **City-specific topics:** tree squirrels in attics under big oaks (Arden-Arcade), ground squirrels along canals (Tracy), fire-safe vents that also block pests (San Marcos), illegal dumping and rats (Compton), rodents in stored boats and RVs (Redding), cluster flies (Livonia), big-headed ants under pavers (Plantation), Lake Houston mosquitoes (Atascocita), pests under raised post-Sandy homes (Toms River), carpet beetles and clothes moths (Fall River).
- **Checks:** 475 pages, 0 issues; batch uniqueness 69–79%; responsive 360/768/1280 clean.

## Coming next — Build 43: city pages batch 41 (10 cities)
- Proposed: Carson, Mission Viejo, South Gate and Santa Monica (CA), O'Fallon MO, Hoover AL, Bellingham and Kirkland WA, Norwalk CT, Nashua NH.
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
