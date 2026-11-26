# PestHalt — Build Status

**Site:** PestHalt · nationwide pest control referral site · target domain **pesthalt.us** (not yet purchased)
**Repo:** github.com/bobee1/PestControlUSA · **Owner/operator:** Anjam Javed
**Phone (temporary):** (800) 555-0199 → replace with the real toll-free number before launch
**Last updated:** 2026-11-26 (Build 16)

## Previous step — Build 15: city pages batch 13 ✅
- Port St. Lucie, Pembroke Pines, Hollywood, Miramar, Coral Springs, West Palm Beach, Clearwater, Lakeland, Gainesville, Palm Bay.

## Current step — Build 16: state uniqueness pass + city pages batch 14 ✅ complete
- **State pass:** added a state-specific section to 13 state pages (South Dakota, Kansas, New Hampshire, Wyoming, West Virginia, North Dakota, Nevada, Oklahoma, Kentucky, Nebraska, Rhode Island, Montana, New Mexico) with verified local facts, e.g. Black Hills pine beetle outbreak and Sturgis rally lodging, Flint Hills burns, Seacoast browntail moth, Red River floods and the Bakken, Mormon crickets in northern Nevada, the July 2022 eastern Kentucky floods, New Mexico plague and hantavirus. Lowest state page is now 66% (was 61%).
- **Cities live:** Fort Wayne (IN), Toledo and Akron (OH), Grand Rapids (MI), Lincoln (NE), Sioux Falls (SD), Overland Park (KS), Springfield (MO), Rochester (MN), Cedar Rapids (IA).
- **Keyword highlights (Semrush US):** bat removal Grand Rapids KD 7; mosquito control Overland Park 210 (KD 15); termite control Overland Park KD 19; exterminator Toledo KD 20; pest control Grand Rapids 880 (KD 23); exterminator Rochester MN KD 24; pest control Akron Ohio KD 25; pest control Sioux Falls 720 (KD 31).
- **City-specific topics:** river wildlife (Fort Wayne), Lake Erie mayflies (Toledo), company-built rubber-worker homes (Akron), bats in Heritage Hill (Grand Rapids), termites vs carpenter ants (Lincoln), West Nile and mosquitoes (Sioux Falls), termite protection (Overland Park), Ozark ticks and chiggers (Springfield), hotels, clinics and long-stay rentals near Mayo (Rochester), derecho and flood damage and attic wildlife (Cedar Rapids).
- **Checks:** 216 pages, 0 issues; batch uniqueness 74–81%; responsive 360/768/1280 clean.

## Coming next — Build 17: city pages batch 15 (10 cities)
- Proposed: Northeast second tier: Buffalo, Rochester and Syracuse (NY), Yonkers (NY), Worcester and Springfield (MA), Hartford, New Haven and Bridgeport (CT), Allentown (PA).

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
