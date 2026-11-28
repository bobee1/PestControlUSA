# PestHalt — Build Status

**Site:** PestHalt · nationwide pest control referral site · target domain **pesthalt.us** (not yet purchased)
**Repo:** github.com/bobee1/PestControlUSA · **Owner/operator:** Anjam Javed
**Phone (temporary):** (800) 555-0199 → replace with the real toll-free number before launch
**Last updated:** 2026-11-26 (Build 41)

## Previous step — Build 40: city pages batch 38 ✅
- Lynn MA, Norwalk, Hesperia, Vista (CA), Carmel IN, Buckeye AZ, San Angelo TX, Federal Way WA, Longmont CO, Roanoke VA.

## Current step — Build 41: city pages batch 39 ✅ complete
- **Cities live:** Beaverton OR, Portsmouth and Suffolk VA, Fayetteville AR, Yakima WA, Sunrise FL, Edmond OK, Lawrence KS, Sandy UT, Asheville NC.
- **Keyword highlights (Semrush US):** pest control Sandy Utah 70 (KD 5); pest control Beaverton 320 (KD 6); exterminator Suffolk VA 170 (KD 7); pest control Fayetteville AR 320 (KD 10); pest control Portsmouth VA 140 (KD 16); pest control Asheville 720 (KD 35). Semrush list trimmed to core terms to save units (~2,170 left).
- **City-specific topics:** nutria along creeks (Beaverton), smokybrown cockroaches (Portsmouth), copperheads (Suffolk), flying squirrels in attics (Fayetteville AR), fruit flies and drain flies (Yakima), condo termite responsibilities (Sunrise), pests in storm shelters (Edmond), raccoons in historic homes (Lawrence), ground squirrels on foothill lots (Sandy), pests after Hurricane Helene flood damage (Asheville).
- **Checks:** 465 pages, 0 issues; batch uniqueness 72–80%; responsive 360/768/1280 clean.

## Coming next — Build 42: city pages batch 40 (10 cities)
- Proposed: Arden-Arcade, Tracy, San Marcos, Compton and Redding (CA), Livonia MI, Plantation FL, Atascocita TX, Toms River NJ, Fall River MA.
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
