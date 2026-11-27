# PestHalt — Build Status

**Site:** PestHalt · nationwide pest control referral site · target domain **pesthalt.us** (not yet purchased)
**Repo:** github.com/bobee1/PestControlUSA · **Owner/operator:** Anjam Javed
**Phone (temporary):** (800) 555-0199 → replace with the real toll-free number before launch
**Last updated:** 2026-11-26 (Build 20)

## Previous step — Build 19: city pages batch 17 ✅
- Alexandria, Arlington VA, Newport News, Hampton, Cary, Fayetteville NC, Wilmington NC, High Point, Clarksville, Murfreesboro.

## Current step — Build 20: city pages batch 18 ✅ complete (Pacific Northwest second tier)
- **Cities live:** Vancouver, Bellevue, Kent, Everett, Renton and Spokane Valley (WA); Salem, Eugene, Gresham and Hillsboro (OR).
- **Keyword highlights (Semrush US):** pest control Gresham 260 (KD 4); pest control Hillsboro 320 (KD 6); exterminator Renton KD 6; pest control Bellevue 720 (KD 10); exterminator Everett KD 10; rodent control Hillsboro 140 (KD 11); pest control Renton KD 12; rodent control Eugene 320 (KD 18); pest control Everett 1,000 (KD 26).
- **City-specific topics:** roof rats vs Norway rats (Vancouver), moisture ants vs carpenter ants (Bellevue), giant house spider season (Kent), ravine wildlife (Everett), odorous house ants in the rainy season (Renton), voles (Spokane Valley), Oregon school IPM rules (Salem), rats, compost and backyard chickens (Eugene), bed bugs in apartments (Gresham), farm-edge rodents (Hillsboro).
- **Checks:** 256 pages, 0 issues; batch uniqueness 70–81%; responsive 360/768/1280 clean.

## Coming next — Build 21: city pages batch 19 (10 cities)
- Proposed: California third tier: Santa Clarita, Glendale, Huntington Beach, Garden Grove, Oxnard, Ontario, Rancho Cucamonga, Oceanside, Elk Grove, Santa Rosa.

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
