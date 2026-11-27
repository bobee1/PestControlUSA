# PestHalt — Build Status

**Site:** PestHalt · nationwide pest control referral site · target domain **pesthalt.us** (not yet purchased)
**Repo:** github.com/bobee1/PestControlUSA · **Owner/operator:** Anjam Javed
**Phone (temporary):** (800) 555-0199 → replace with the real toll-free number before launch
**Last updated:** 2026-11-26 (Build 30)

## Previous step — Build 29: state page pass 2 + city pages batch 27 ✅
- State-specific sections for SC, PA, MO, IA, ME, VT, IN plus extra paragraphs for WY, KS, SD, WV, NH; Texas suburbs batch (Sugar Land to Wichita Falls).

## Current step — Build 30: city pages batch 28 ✅ complete
- **Cities live:** Dayton, Youngstown, Canton, Parma (OH); Erie, Reading, Scranton, Lancaster, Bethlehem, Harrisburg (PA).
- **Keyword highlights (Semrush US):** pest control Dayton 480 (KD 9); pest control Bethlehem PA 260 (KD 9) and exterminator Bethlehem PA 140 (KD 9); pest control Canton Ohio 320 (KD 10); termite inspection Dayton Ohio 50 (KD 11); pest control Parma 110 (KD 13); pest control Lancaster PA 1,000 (KD 37, biggest of the batch).
- **City-specific topics:** termite inspections for post-1913-flood historic homes (Dayton), ticks near Mill Creek MetroParks (Youngstown), yellowjackets/paper wasps/bald-faced hornets (Canton), mice in postwar bungalow kneewalls (Parma), lake-effect winters and mice (Erie), German cockroaches in divided rowhomes (Reading), wildlife in double-block homes (Scranton), termites in brick rowhouses (Lancaster), mosquitoes along the Lehigh and Monocacy (Bethlehem), bed bugs in apartments and hotels (Harrisburg).
- **Checks:** 356 pages, 0 issues; batch uniqueness 67–79%; Ohio and Pennsylvania state pages 68%; responsive 360/768/1280 clean.

## Coming next — Build 31: city pages batch 29 (10 cities)
- Proposed: California fourth tier: Lancaster, Palmdale, Salinas, Hayward, Corona, Sunnyvale, Roseville, Escondido, Pomona, Torrance.
- Flagged for a later build: Washington, DC (needs a district page instead of a state page) and Las Vegas-area unincorporated places (Enterprise, Spring Valley, Sunrise Manor, Paradise).
- Scope rule (owner, 2026-11-27): US states only, no overseas territories. Puerto Rico's 11 places removed from the city list (1,854 places remain).

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
