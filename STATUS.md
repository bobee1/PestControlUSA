# PestHalt — Build Status

**Site:** PestHalt · nationwide pest control referral site · target domain **pesthalt.us** (not yet purchased)
**Repo:** github.com/bobee1/PestControlUSA · **Owner/operator:** Anjam Javed
**Phone (temporary):** (800) 555-0199 → replace with the real toll-free number before launch
**Last updated:** 2026-11-26 (Build 31)

## Previous step — Build 30: city pages batch 28 ✅
- Dayton, Youngstown, Canton, Parma (OH); Erie, Reading, Scranton, Lancaster, Bethlehem, Harrisburg (PA). Scope set: 50 states plus DC, no territories (Puerto Rico removed, 1,854 places remain).

## Current step — Build 31: city pages batch 29 ✅ complete
- **Cities live:** Lancaster, Palmdale, Salinas, Hayward, Corona, Sunnyvale, Roseville, Escondido, Pomona, Torrance (CA).
- **Keyword highlights (Semrush US):** rodent control Torrance 590 (KD 6); pest control Palmdale 210 (KD 7); pest control Hayward 260 (KD 7); termite control Escondido 90 (KD 5); exterminator Torrance 590 (KD 11); pest control Corona 480 (KD 11); pest control Torrance 880 (KD 13); termite inspection Torrance 390 (KD 14).
- **City-specific topics:** harvester ants (Lancaster), pack rats in hillside neighborhoods (Palmdale), pocket gophers in valley soils (Salinas), salt marsh mosquitoes from the bay shoreline (Hayward), subterranean termites in tract homes (Corona), pest-proofing Eichler homes (Sunnyvale), ticks on creek and oak trails (Roseville), historic homes and crawlspaces in Old Escondido (Escondido), fleas, opossums and flea-borne typhus (Pomona), roof rats vs. Norway rats (Torrance).
- **Checks:** 366 pages, 0 issues; batch uniqueness 79–83%; responsive 360/768/1280 clean.

## Coming next — Build 32: DC page + city pages batch 30
- Proposed: a Washington, DC district page, plus Mesquite TX, Olathe KS, Thornton CO, Metairie LA, Fargo ND, Norman OK, Visalia, Fullerton and Pasadena CA.
- Still held: Las Vegas-area unincorporated places (Enterprise, Spring Valley, Sunrise Manor, Paradise).
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
