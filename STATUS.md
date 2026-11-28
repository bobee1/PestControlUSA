# PestHalt — Build Status

**Site:** PestHalt · nationwide pest control referral site · target domain **pesthalt.us** (not yet purchased)
**Repo:** github.com/bobee1/PestControlUSA · **Owner/operator:** Anjam Javed
**Phone (temporary):** (800) 555-0199 → replace with the real toll-free number before launch
**Last updated:** 2026-11-26 (Build 43)

## Previous step — Build 42: city pages batch 40 ✅
- Arden-Arcade, Tracy, San Marcos, Compton, Redding (CA), Livonia MI, Plantation FL, Atascocita TX, Toms River NJ, Fall River MA.

## Current step — Build 43: city pages batch 41 ✅ complete
- **Cities live:** Carson, Mission Viejo, South Gate, Santa Monica (CA), O'Fallon MO, Hoover AL, Bellingham and Kirkland WA, Norwalk CT, Nashua NH.
- **Keyword highlights (Semrush US):** pest control Carson CA 90 (KD 10); pest control Mission Viejo 590 (KD 12); pest control Nashua NH 260 (KD 13); pest control Kirkland 110 (KD 14); exterminator Santa Monica 720 (KD 21); pest control Santa Monica 880 (KD 25). About 1,790 Semrush units left.
- **City-specific topics:** pests under mobile homes (Carson), HOA slopes, gophers and roof rats (Mission Viejo), termites in 1920s–40s homes (South Gate), California bed bug rules for rentals (Santa Monica), wolf spiders in new subdivisions (O'Fallon), yellowjacket super nests (Hoover), moisture pests in the rainy season (Bellingham), English ivy and rats (Kirkland), spotted lanternflies in Connecticut (Norwalk), deer ticks along Mine Falls Park (Nashua).
- **Fix:** 'Saint' Census names now show as 'St.' sitewide.
- **Checks:** 485 pages, 0 issues; batch uniqueness 67–81%; responsive 360/768/1280 clean.

## Coming next — Build 44: city pages batch 42 (10 cities)
- Proposed: Chino, Indio, Hemet and Merced (CA), Alafaya FL, Lawton OK, Avondale AZ, Germantown MD, Trenton NJ, Fort Smith AR.
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
