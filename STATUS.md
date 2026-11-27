# PestHalt — Build Status

**Site:** PestHalt · nationwide pest control referral site · target domain **pesthalt.us** (not yet purchased)
**Repo:** github.com/bobee1/PestControlUSA · **Owner/operator:** Anjam Javed
**Phone (temporary):** (800) 555-0199 → replace with the real toll-free number before launch
**Last updated:** 2026-11-26 (Build 25)

## Previous step — Build 24: city pages batch 22 ✅
- Aurora IL, Naperville, Joliet, Elgin, Rockford, Peoria IL, Springfield IL, Evansville, South Bend, Kansas City KS; same-name city fix.

## Current step — Build 25: city pages batch 23 ✅ complete (Great Lakes and Upper Midwest third tier)
- **Cities live:** Lansing, Ann Arbor, Warren, Sterling Heights and Dearborn (MI); Green Bay and Kenosha (WI); Duluth (MN); Davenport (IA); Independence (MO).
- **Keyword highlights (Semrush US):** pest control Warren MI 210 (KD 6); bat removal Ann Arbor KD 7; pest control Sterling Heights KD 8; pest control Dearborn KD 8; exterminator Davenport 260 (KD 9); exterminator Duluth KD 14; mosquito control Kenosha 140 (KD 15); pest control Independence MO 390 (KD 19); pest control Ann Arbor 720 (KD 22).
- **City-specific topics:** old basements and mice (Lansing), bats in historic homes (Ann Arbor), skunks and raccoons under postwar porches (Warren), pavement ants (Sterling Heights), rats behind food corridors (Dearborn), carpenter ants (Green Bay), mosquito season (Kenosha), cluster flies on the hillside (Duluth), river floods, moisture and termites (Davenport), termites in historic homes (Independence).
- **Overlap fix:** reworded Ann Arbor and Rockford bat text so Grand Rapids stays above 65%.
- **Checks:** 306 pages, 0 issues; batch uniqueness 67–81%; responsive 360/768/1280 clean.

## Coming next — Build 26: city pages batch 24 (10 cities)
- Proposed: Northeast third tier: Paterson and Elizabeth (NJ); Lowell, Cambridge, New Bedford and Brockton (MA); Stamford and Waterbury (CT); Manchester (NH); Portland (ME).

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
