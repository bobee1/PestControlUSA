# PestHalt — Build Status

**Site:** PestHalt · nationwide pest control referral site · target domain **pesthalt.us** (not yet purchased)
**Repo:** github.com/bobee1/PestControlUSA · **Owner/operator:** Anjam Javed
**Phone (temporary):** (800) 555-0199 → replace with the real toll-free number before launch
**Last updated:** 2026-11-26 (Build 23)

## Previous step — Build 22: city pages batch 20 ✅
- Pasadena TX, Killeen, Denton, Waco, Round Rock, Carrollton, Midland, Odessa, Abilene, Beaumont.

## Current step — Build 23: city pages batch 21 ✅ complete (Southwest and Mountain third tier)
- **Cities live:** Tempe, Surprise, Goodyear, Yuma and Flagstaff (AZ); Las Cruces (NM); Provo, Orem, West Valley City and St. George (UT).
- **Keyword highlights (Semrush US):** pest control Provo 320 (KD 7); bee removal Tempe KD 9; pest control Goodyear AZ KD 11; pest control Surprise AZ 590 (KD 14); exterminator Orem KD 14; pest control Las Cruces NM KD 15; pest control Orem 480 (KD 16). Yuma and St. George head terms are harder (KD 38–48).
- **City-specific topics:** Tempe Town Lake midges and mosquitoes, West Valley roof rats (Surprise), river and lake mosquitoes (Goodyear), harvester and desert fire ants (Yuma), carpenter ants in pine country (Flagstaff), termites in adobe homes (Las Cruces), bed bugs in BYU-area housing (Provo), Utah Lake mosquitoes and midges (Orem), mice and deer mice (West Valley City), bark scorpions in Utah's Dixie (St. George).
- **Checks:** 286 pages, 0 issues; batch uniqueness 71–82%; responsive 360/768/1280 clean. Lowest state page is Wyoming at 65% (rule is 60%).

## Coming next — Build 24: city pages batch 22 (10 cities)
- Proposed: Illinois, Indiana and Kansas second tier: Aurora, Naperville, Joliet, Elgin, Rockford, Peoria and Springfield (IL); Evansville and South Bend (IN); Kansas City (KS).

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
