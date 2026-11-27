# PestHalt — Build Status

**Site:** PestHalt · nationwide pest control referral site · target domain **pesthalt.us** (not yet purchased)
**Repo:** github.com/bobee1/PestControlUSA · **Owner/operator:** Anjam Javed
**Phone (temporary):** (800) 555-0199 → replace with the real toll-free number before launch
**Last updated:** 2026-11-26 (Build 32)

## Previous step — Build 31: city pages batch 29 ✅
- Lancaster, Palmdale, Salinas, Hayward, Corona, Sunnyvale, Roseville, Escondido, Pomona, Torrance (CA).

## Current step — Build 32: DC page + city pages batch 30 ✅ complete
- **Washington, DC:** the existing district page (/locations/district-of-columbia/) was upgraded with a rodent control section based on DC Health's Rodent and Vector Control Division (311 reports, public-property baiting, private yards by petition, no commercial property), a ward-by-ward table of neighborhoods and pest issues, row house termites, and DOEE licensing rules (resident agent for Maryland/Virginia companies, IPM rules for schools). Now ~1,580 words, 88% unique.
- **Cities live:** Mesquite TX, Olathe KS, Thornton CO, Metairie LA, Fargo ND, Norman OK, Visalia, Fullerton, Pasadena CA.
- **Keyword highlights (Semrush US):** pest control Olathe KS 210 (KD 3); pest control Pasadena CA 320 (KD 9); rodent control Pasadena 480 (KD 9); mosquito control Metairie 110 (KD 10); pest control Fullerton 140 (KD 11); pest control DC 590 (KD 27); rodent control DC 260 (KD 21).
- **City-specific topics:** American cockroaches from drains in older homes (Mesquite), lone star ticks and alpha-gal (Olathe), prairie dogs near new development (Thornton), canals and mosquitoes (Metairie), Red River floods and mosquitoes (Fargo), chiggers and ticks near Lake Thunderbird (Norman), Turkestan cockroaches (Visalia), raccoons and skunks in the hills (Fullerton), rodent-proofing Craftsman homes (Pasadena).
- **Checks:** 375 pages, 0 issues; batch uniqueness 73–83%; responsive 360/768/1280 clean.

## Coming next — Build 33: city pages batch 31 (10 places)
- Proposed: Las Vegas Valley communities (Enterprise, Spring Valley, Sunrise Manor, Paradise), plus Columbia MO, Topeka KS, Meridian ID, Lafayette LA, Billings MT and Lewisville TX.
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
