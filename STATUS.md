# PestHalt — Build Status

**Site:** PestHalt · nationwide pest control referral site · target domain **pesthalt.us** (not yet purchased)
**Repo:** github.com/bobee1/PestControlUSA · **Owner/operator:** Anjam Javed
**Phone (temporary):** (800) 555-0199 → replace with the real toll-free number before launch
**Last updated:** 2026-11-26 (Build 19)

## Previous step — Build 18: city pages batch 16 ✅
- Columbia SC, Greenville SC, Augusta, Columbus GA, Huntsville, Montgomery, Mobile, Jackson MS, Little Rock, Shreveport.

## Current step — Build 19: city pages batch 17 ✅ complete (Virginia, Carolinas, Tennessee)
- **Cities live:** Alexandria, Arlington, Newport News and Hampton (VA); Cary, Fayetteville, Wilmington and High Point (NC); Clarksville and Murfreesboro (TN).
- **Keyword highlights (Semrush US):** pest control Cary NC KD 7 and mosquito control Cary NC 110 (KD 7); termite control Newport News KD 9; mosquito control Murfreesboro 140 (KD 9); pest control Newport News 880 (KD 14); pest control High Point NC KD 14; pest control Arlington VA KD 16; pest control Murfreesboro TN 720 (KD 16); rodent control Alexandria VA 210 (KD 20); pest control Clarksville TN 880 (KD 22).
- **City-specific topics:** rodents in Old Town rowhouses (Alexandria), WWII-era garden apartments (Arlington), Hilton Village cottages and termites (Newport News), storms and crawlspace moisture pests (Hampton), Asian tiger mosquitoes (Cary), VA loans and termite inspections (Fayetteville), Formosan termites on the Cape Fear coast (Wilmington), showrooms and the High Point Market (High Point), lone star ticks and alpha-gal (Clarksville), MTSU student rentals (Murfreesboro).
- **Local facts used:** Hilton Village (1918), Aberdeen Gardens New Deal community, Hurricane Isabel (2003), Hurricane Florence (2018), High Point Market, Fort Bragg and Fort Campbell, the December 2023 Clarksville tornado.
- **Checks:** 246 pages, 0 issues; batch uniqueness 68–80%; responsive 360/768/1280 clean.

## Coming next — Build 20: city pages batch 18 (10 cities)
- Proposed: Pacific Northwest second tier: Vancouver, Bellevue, Kent, Everett, Renton and Spokane Valley (WA); Salem, Eugene, Gresham and Hillsboro (OR).

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
