# PestHalt — Build Status

**Site:** PestHalt · nationwide pest control referral site · target domain **pesthalt.us** (not yet purchased)
**Repo:** github.com/bobee1/PestControlUSA · **Owner/operator:** Anjam Javed
**Phone (temporary):** (800) 555-0199 → replace with the real toll-free number before launch
**Last updated:** 2026-11-26 (Build 15)

## Previous step — Build 14: city pages batch 12 ✅
- Chandler, Gilbert, Glendale AZ, Peoria AZ, Henderson, North Las Vegas, Reno, Aurora CO, Fort Collins, Lakewood CO.

## Current step — Build 15: city pages batch 13 ✅ complete (Florida second tier)
- **Cities live:** Port St. Lucie, Pembroke Pines, Hollywood, Miramar, Coral Springs, West Palm Beach, Clearwater, Lakeland, Gainesville, Palm Bay.
- **Keyword highlights (Semrush US):** pest control Hollywood FL KD 8; pest control Miramar 170 (KD 9); termite control Port St. Lucie 140 (KD 9); mosquito control Coral Springs KD 8; exterminator Palm Bay KD 8; pest control Gainesville FL 590 (KD 16); pest control Pembroke Pines 390 (KD 19); pest control Clearwater FL 880 (KD 20); rodent control West Palm Beach 590 (KD 27).
- **City-specific topics:** renewing termite protection (Port St. Lucie), ghost and white-footed ants (Pembroke Pines), iguanas and seawalls (Hollywood), Everglades-edge mosquitoes (Miramar), Asian and Formosan termites (Coral Springs), rats in historic neighborhoods (West Palm Beach), no-see-ums (Clearwater), armadillos and wildlife (Lakeland), integrated pest management (Gainesville), palmetto bugs (Palm Bay).
- **Local facts used:** General Development Corporation origins of Port St. Lucie and Port Malabar; Hollywood's 1920s founding; Florida's iguana removal guidance; Broward County's two invasive subterranean termites; UF entomology and IPM.
- **Checks:** 206 pages, 0 issues; batch uniqueness 77–83%; responsive 360/768/1280 clean. Watch items: South Dakota 61%, Nevada 64%.

## Coming next — Build 16: state page uniqueness pass + city batch 14
- First, add state-specific content to South Dakota, Nevada and any other state page under 66% so they stay well above the 60% rule.
- Then 10 Midwest second-tier cities: Fort Wayne (IN), Toledo and Akron (OH), Grand Rapids (MI), Lincoln (NE), Sioux Falls (SD), Overland Park (KS), Springfield (MO), Rochester (MN), Cedar Rapids (IA). Sioux Falls also helps the South Dakota page.

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
