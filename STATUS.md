# PestHalt — Build Status

**Site:** PestHalt · nationwide pest control referral site · target domain **pesthalt.us** (not yet purchased)
**Repo:** github.com/bobee1/PestControlUSA · **Owner/operator:** Anjam Javed
**Phone (temporary):** (800) 555-0199 → replace with the real toll-free number before launch
**Last updated:** 2026-11-26 (Build 37)

## Previous step — Build 36: city pages batch 34 ✅
- Richmond, East Los Angeles, Downey, Murrieta, Costa Mesa, Temecula, Ventura (CA); Pueblo, Greeley (CO); Miami Gardens FL.

## Current step — Build 37: city pages batch 35 ✅ complete
- **Cities live:** Santa Maria, West Covina, El Monte, Menifee, Jurupa Valley (CA); South Fulton GA; Sparks NV; Riverview FL; Allen TX; Centennial CO.
- **Keyword highlights (Semrush US):** pest control Jurupa Valley 70 (KD 6); pest control Menifee 320 (KD 7); termite control West Covina 70 (KD 8); exterminator Allen TX 210 (KD 10); pest control Allen TX 320 (KD 12); pest control Riverview FL 590 (KD 22); pest control Sparks 480 (KD 28).
- **City-specific topics:** field rodents at harvest (Santa Maria), liquid vs. bait termite treatments (West Covina), backyard ponds and mosquitofish (El Monte), pest plans for 55+ communities (Menifee), ground squirrels on horse properties (Jurupa Valley), kudzu bugs (South Fulton), Truckee River and marina mosquitoes (Sparks), retention ponds and midges (Riverview), striped bark scorpions (Allen), bats in attics (Centennial).
- **Checks:** 425 pages, 0 issues; batch uniqueness 70–81%; responsive 360/768/1280 clean.

## Coming next — Build 38: city pages batch 36 (10 cities)
- Proposed: Rio Rancho NM, Davie FL, Nampa ID, Boulder CO, Columbia MD, and Inglewood, Burbank, El Cajon, Rialto and San Mateo (CA).
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
