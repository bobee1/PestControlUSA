# PestHalt — Build Status

**Site:** PestHalt · nationwide pest control referral site · target domain **pesthalt.us** (not yet purchased)
**Repo:** github.com/bobee1/PestControlUSA · **Owner/operator:** Anjam Javed
**Phone (temporary):** (800) 555-0199 → replace with the real toll-free number before launch
**Last updated:** 2026-11-26 (Build 9)

## Previous step — Build 8: city pages batch 6 ✅
- New York City, Philadelphia, Pittsburgh, Boston, Baltimore, Newark, Jersey City, Providence, Virginia Beach, Richmond.

## Current step — Build 9: city pages batch 7 ✅ complete (Pacific Northwest, Mountain West, Southwest, Alaska, Hawaii)
- **Cities live:** Seattle, Spokane and Tacoma (WA), Portland (OR), Boise (ID), Salt Lake City (UT), Albuquerque (NM), Colorado Springs (CO), Anchorage (AK), Honolulu (HI).
- **Dataset notes:** Census names "Boise City" and "Urban Honolulu" (a CDP) display as Boise and Honolulu. Anchorage has no other 25k+ place within 35 miles, so its nearby paragraph names Eagle River, Chugiak, Girdwood, Wasilla and Palmer.
- **Keyword highlights (Semrush US):** pest control Tacoma 1,000 (KD 18); pest control Anchorage 320 (KD 20); exterminator Honolulu KD 13; mosquito control Boise 140 (KD 9); spider control Boise 210 (KD 15); termite control Albuquerque KD 8; rodent control Seattle 880 and rodent control Portland 720; pest control Seattle and Portland 1,900 each.
- **City-specific topics:** moisture and wood-destroying pests (Seattle), older homes and moisture pests (Portland), the fall pest rush (Spokane), gulches and rats (Tacoma), new-home pests and black widows (Boise), window wells and old foundations (Salt Lake City), hantavirus and safe rodent cleanup (Albuquerque), miller moths and fall invaders (Colorado Springs), cold-climate pest control and bear-safe trash (Anchorage), subterranean vs drywood termite treatment (Honolulu).
- **Local facts used:** Multnomah County vector control, Ada County mosquito abatement, Salt Lake City Mosquito Abatement District, NM hantavirus guidance, Front Range miller moth migration and elm seed bugs, Anchorage trash rules for bears, rat lungworm disease and Hawaii Department of Agriculture invasive-pest reporting (little fire ants, coconut rhinoceros beetle). Hobo spider claims were left out because the bite risk is disputed.
- **Template updates:** state pages show display names for all built cities; optional `nearby` list for isolated cities; nearby lists read "A, B and C".
- **Checks:** 146 pages, 0 issues; batch uniqueness 82–88%; responsive 360/768/1280 clean. South Dakota state page holding at 61%.

## Coming next — Build 10: city pages batch 8 (10 cities)
- Proposed: Great Lakes and Plains: Detroit, Milwaukee, Minneapolis, St. Paul, Cleveland, Cincinnati, Omaha, Wichita, Madison, Des Moines.

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
