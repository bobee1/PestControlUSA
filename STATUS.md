# PestHalt — Build Status

**Site:** PestHalt · nationwide pest control referral site · target domain **pesthalt.us** (not yet purchased)
**Repo:** github.com/bobee1/PestControlUSA · **Owner/operator:** Anjam Javed
**Phone (temporary):** (800) 555-0199 → replace with the real toll-free number before launch
**Last updated:** 2026-11-26 (Build 17)

## Previous step — Build 16: state uniqueness pass + city pages batch 14 ✅
- 13 state pages got a state-specific section (lowest state now 66%); Fort Wayne, Toledo, Akron, Grand Rapids, Lincoln, Sioux Falls, Overland Park, Springfield MO, Rochester MN, Cedar Rapids.

## Current step — Build 17: city pages batch 15 ✅ complete (Northeast second tier)
- **Cities live:** Buffalo, Rochester, Syracuse and Yonkers (NY); Worcester and Springfield (MA); Hartford, New Haven and Bridgeport (CT); Allentown (PA).
- **Keyword highlights (Semrush US):** exterminator New Haven KD 14; exterminator Bridgeport CT KD 15 and rodent control Bridgeport KD 15; exterminator Springfield MA KD 16; pest control Syracuse NY 480 (KD 16); pest control Yonkers KD 23; exterminator Buffalo NY 480 (KD 25); pest control Worcester 590 (KD 29). Rochester NY head terms are hard (KD 55–56).
- **City-specific topics:** ice dams and carpenter ants (Buffalo), rats along the Genesee (Rochester), bats (Syracuse), mice and roaches in apartment buildings (Yonkers), EEE and mosquitoes (Worcester), squirrels in McKnight Victorians (Springfield), perfect sixes (Hartford), ticks and Lyme disease (New Haven), rats and multi-family trash (Bridgeport), spotted lanternflies (Allentown).
- **Local facts used:** Snowvember 2014 and the December 2022 blizzard; Syracuse snowfall; EEE cases in Worcester County in 2019–2020 and the Central Massachusetts Mosquito Control Project; the 2008 Asian longhorned beetle find in Worcester; the June 2011 Springfield tornado; Hartford's perfect sixes; Lyme disease named for Lyme, CT; lanternfly first found in Berks County in 2014.
- **Same-name fix:** the services paragraph on every city page now names the state, so Rochester MN/NY and Springfield MO/MA no longer share an identical paragraph.
- **Checks:** 226 pages, 0 issues; batch uniqueness 68–83%; responsive 360/768/1280 clean.

## Coming next — Build 18: city pages batch 16 (10 cities)
- Proposed: Deep South second tier: Columbia and Greenville (SC), Augusta and Columbus (GA), Huntsville, Montgomery and Mobile (AL), Jackson (MS), Little Rock (AR), Shreveport (LA).

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
