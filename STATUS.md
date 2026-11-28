# PestHalt — Build Status

**Site:** PestHalt · nationwide pest control referral site · target domain **pesthalt.us** (not yet purchased)
**Repo:** github.com/bobee1/PestControlUSA · **Owner/operator:** Anjam Javed
**Phone (temporary):** (800) 555-0199 → replace with the real toll-free number before launch
**Last updated:** 2026-11-26 (Build 44)

## Previous step — Build 43: city pages batch 41 ✅
- Carson, Mission Viejo, South Gate, Santa Monica (CA), O'Fallon MO, Hoover AL, Bellingham and Kirkland WA, Norwalk CT, Nashua NH.

## Current step — Build 44: city pages batch 42 ✅ complete
- **Cities live:** Chino, Indio, Hemet, Merced (CA), Alafaya FL, Lawton OK, Avondale AZ, Germantown MD, Trenton NJ, Fort Smith AR.
- **Keyword highlights (Semrush US):** pest control Germantown MD 390 (KD 6); pest control Hemet 170 (KD 7); pest control Fort Smith 170 (KD 12); pest control Trenton NJ 210 (KD 18); pest control Indio 320 (KD 23). About 1,590 Semrush units left.
- **City-specific topics:** Prado Basin mosquitoes (Chino), red imported fire ants in the Coachella Valley (Indio), brown dog ticks indoors (Hemet), native southern fire ants (Merced), building-wide apartment treatments near UCF (Alafaya), hackberry psyllids (Lawton), black and brown widows (Avondale), Montgomery County's lawn pesticide rules (Germantown), Delaware River and D&R Canal mosquitoes (Trenton), brown recluse monitoring (Fort Smith).
- **Checks:** 495 pages, 0 issues; batch uniqueness 69–80%; responsive 360/768/1280 clean.

## Coming next — Build 45: city pages batch 43 (10 cities)
- Proposed: Westminster, San Leandro and Santa Barbara (CA), Clifton NJ, Waukegan and Champaign IL, Bloomington MN, Greenville NC, Newton MA, Santa Fe NM.
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
