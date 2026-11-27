# PestHalt — Build Status

**Site:** PestHalt · nationwide pest control referral site · target domain **pesthalt.us** (not yet purchased)
**Repo:** github.com/bobee1/PestControlUSA · **Owner/operator:** Anjam Javed
**Phone (temporary):** (800) 555-0199 → replace with the real toll-free number before launch
**Last updated:** 2026-11-26 (Build 26)

## Previous step — Build 25: city pages batch 23 ✅
- Lansing, Ann Arbor, Warren, Sterling Heights, Dearborn, Green Bay, Kenosha, Duluth, Davenport, Independence.

## Current step — Build 26: city pages batch 24 ✅ complete (Northeast third tier)
- **Cities live:** Paterson and Elizabeth (NJ); Lowell, Cambridge, New Bedford and Brockton (MA); Stamford and Waterbury (CT); Manchester (NH); Portland (ME). First city guides for New Hampshire and Maine.
- **Keyword highlights (Semrush US):** pest control Elizabeth NJ KD 1 and exterminator Elizabeth NJ KD 2; pest control New Bedford KD 9; pest control Paterson NJ KD 11; exterminator Waterbury CT KD 12; exterminator Cambridge MA KD 13; pest control Lowell MA 260 (KD 15); pest control Brockton 170 (KD 15). Manchester NH head term is harder (KD 42).
- **City-specific topics:** Passaic River floods (Paterson), port and airport warehouses (Elizabeth), rats along the mill canals (Lowell), IPM for labs and campuses (Cambridge), seafood processing (New Bedford), bed bugs in triple-deckers (Brockton), North Stamford wildlife (Stamford), hillside three-families and mice (Waterbury), carpenter ants and ice dams (Manchester), browntail moths (Portland, ME).
- **Checks:** 316 pages, 0 issues; batch uniqueness 72–81%; responsive 360/768/1280 clean.

## Coming next — Build 27: city pages batch 25 (10 cities)
- Proposed: Florida fourth tier: Fort Myers, Sarasota, Daytona Beach, Melbourne, Pompano Beach, Boca Raton, Deltona, Palm Coast, Kissimmee, Ocala.

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
