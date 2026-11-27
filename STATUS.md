# PestHalt — Build Status

**Site:** PestHalt · nationwide pest control referral site · target domain **pesthalt.us** (not yet purchased)
**Repo:** github.com/bobee1/PestControlUSA · **Owner/operator:** Anjam Javed
**Phone (temporary):** (800) 555-0199 → replace with the real toll-free number before launch
**Last updated:** 2026-11-26 (Build 24)

## Previous step — Build 23: city pages batch 21 ✅
- Tempe, Surprise, Goodyear, Yuma, Flagstaff, Las Cruces, Provo, Orem, West Valley City, St. George.

## Current step — Build 24: city pages batch 22 ✅ complete (Illinois, Indiana, Kansas)
- **Cities live:** Aurora, Naperville, Joliet, Elgin, Rockford, Peoria and Springfield (IL); Evansville and South Bend (IN); Kansas City (KS).
- **Keyword highlights (Semrush US):** pest control Elgin KD 10; exterminator Naperville KD 11; pest control Aurora IL 320 (KD 16); pest control Rockford IL 880 (KD 16); pest control South Bend 720 (KD 16); exterminator Joliet KD 15; pest control Naperville 390 (KD 18). Evansville, Peoria IL and Kansas City KS head terms are harder (KD 41–46).
- **City-specific topics:** balloon-frame homes and mice (Aurora), ticks near forest preserves (Naperville), rail and intermodal rodents (Joliet), cockroaches in converted Victorians (Elgin), bats and rabies testing (Rockford), brown recluses at the northern edge of their range (Peoria), termites in historic homes (Springfield), Ohio River mosquitoes (Evansville), game-weekend and student rentals (South Bend), rats in Armourdale's old industrial districts (Kansas City, KS).
- **Same-name fix:** body text on same-name city pages now includes the state ("Springfield, Illinois"), lifting those pages to 68–77% unique.
- **Checks:** 296 pages, 0 issues; responsive 360/768/1280 clean.

## Coming next — Build 25: city pages batch 23 (10 cities)
- Proposed: Michigan, Wisconsin, Minnesota, Iowa and Missouri third tier: Lansing, Ann Arbor, Warren, Sterling Heights and Dearborn (MI); Green Bay and Kenosha (WI); Duluth (MN); Davenport (IA); Independence (MO).

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
