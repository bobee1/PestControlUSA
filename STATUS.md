# PestHalt — Build Status

**Site:** PestHalt · nationwide pest control referral site · target domain **pesthalt.us** (not yet purchased)
**Repo:** github.com/bobee1/PestControlUSA · **Owner/operator:** Anjam Javed
**Phone (temporary):** (800) 555-0199 → replace with the real toll-free number before launch
**Last updated:** 2026-11-26 (Build 14)

## Previous step — Build 13: city pages batch 11 ✅
- Riverside, San Bernardino, Fontana, Moreno Valley, Santa Ana, Irvine, Chula Vista, Stockton, Modesto, Fremont.

## Current step — Build 14: city pages batch 12 ✅ complete (Arizona, Nevada, Colorado suburbs)
- **Cities live:** Chandler, Gilbert, Glendale and Peoria (AZ); Henderson, North Las Vegas and Reno (NV); Aurora, Fort Collins and Lakewood (CO).
- **Keyword highlights (Semrush US):** exterminator Aurora CO KD 8 and pest control Aurora CO 390 (KD 11); bed bug exterminator Aurora KD 5; exterminator Glendale AZ KD 9; termite control Chandler KD 10; bee removal Chandler 140 (KD 11) and Gilbert 110 (KD 12); pest control Reno NV 480 (KD 16); pest control Lakewood CO KD 17; pest control Fort Collins 590 (KD 27). Henderson and Chandler head terms are hard (KD 50–53).
- **City-specific topics:** desert subterranean termites (Chandler), flood irrigation pests (Gilbert), sewer roaches and monsoon (Glendale), Africanized bees (Peoria), desert mosquitoes and Aedes aegypti (Henderson), roof rats in palms and tile roofs (North Las Vegas), yellowjackets (Reno), bed bugs in apartments (Aurora), West Nile monitoring (Fort Collins), Front Range termites (Lakewood).
- **Local facts used:** Intel Ocotillo campus; Gilbert as the former "Hay Shipping Capital of the World"; Southern Nevada Health District mosquito surveillance; Colorado's rental bed bug law; Northern Colorado's 2003 West Nile outbreak and Fort Collins mosquito testing.
- **Checks:** 196 pages, 0 issues; batch uniqueness 76–82%; responsive 360/768/1280 clean. Watch items: South Dakota 61%, Nevada state page 64% (now has 4 city guides).

## Coming next — Build 15: city pages batch 13 (10 cities)
- Proposed: Florida second tier: Port St. Lucie, Pembroke Pines, Hollywood, Miramar, Coral Springs, West Palm Beach, Clearwater, Lakeland, Gainesville, Palm Bay.

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
