# PestHalt — Build Status

**Site:** PestHalt · nationwide pest control referral site · target domain **pesthalt.us** (not yet purchased)
**Repo:** github.com/bobee1/PestControlUSA · **Owner/operator:** Anjam Javed
**Phone (temporary):** (800) 555-0199 → replace with the real toll-free number before launch
**Last updated:** 2026-11-26 (Build 8)

## Previous step — Build 7: city pages batch 5 ✅
- Chicago, Indianapolis, Columbus OH, Kansas City, St. Louis, Louisville, Oklahoma City, Tulsa, Denver, Las Vegas.

## Current step — Build 8: city pages batch 6 ✅ complete (10 Northeast and Mid-Atlantic cities)
- **Cities live:** New York City (NY), Philadelphia and Pittsburgh (PA), Boston (MA), Baltimore (MD), Newark and Jersey City (NJ), Providence (RI), Virginia Beach and Richmond (VA).
- **Change from plan:** Washington, DC was swapped for Jersey City, because the DC page already serves as the city's page and a second DC page would cannibalize it.
- **Keyword highlights (Semrush US):** pest control Virginia Beach 1,900 (KD 14); pest control Philadelphia 1,600 (KD 16); bed bug exterminator Philadelphia KD 9; pest control Richmond VA 1,600; exterminator Pittsburgh 880 (KD 21); pest control NYC 1,900 (KD 61, page leans on borough terms like exterminator Brooklyn 1,000).
- **City-specific topics:** landlord responsibility and rats (NYC), rowhome block-wide control (Philadelphia), September 1 moving day and bed bugs (Boston), alleys and Rat Rubout (Baltimore), hillside damp basements (Pittsburgh), multi-family homes (Newark), waterfront construction and rats (Jersey City), triple-deckers and carpenter ants (Providence), coastal termite inspections (Virginia Beach), historic-home termites (Richmond).
- **Verified local events used:** NYC rodent mitigation director (2023), Sandy (2012) and Ida (2021) flooding, Lanternfly first U.S. detection in Berks County (2014), Great Baltimore Fire (1904), Hurricane Ivan flooding (2004) and 2018 landslides in Pittsburgh, Fox Point Hurricane Barrier after the 1938 and 1954 hurricanes, Hurricane Matthew (2016) in Virginia Beach, Tropical Storm Gaston (2004) in Richmond.
- **Linking fix:** the link planner now mirrors the exact "nearby communities" list each page shows (10 closest within 35 miles), which fixed Dallas.
- **Checks:** 136 pages, 0 issues; batch uniqueness 77–85%; responsive 360/768/1280 with no overflow or console errors. Watch item: South Dakota state page at 61% uniqueness (rule is 60%) as more location pages are added.

## Coming next — Build 9: city pages batch 7 (10 cities)
- Proposed: Pacific Northwest, Mountain West and Hawaii: Seattle, Portland, Spokane, Tacoma, Boise, Salt Lake City, Albuquerque, Colorado Springs, Anchorage, Honolulu.
- Brings carpenter ants and dampwood termites, rats in Seattle and Portland, hobo spiders and wasps in Boise and Spokane, hantavirus in Albuquerque, and Formosan termites in Honolulu.

## Later builds
- Remaining city batches until all 1,855 places are live; then towns under 25,000 if wanted.
- Blog hub + posts following the Blog Post Criteria doc.
- City × service pages for top metros where Semrush shows volume.

## Deploy (Cloudflare Pages, Git-connected)
- Build command: *(none)* · **Build output directory: `public`** · Functions directory: `functions` (auto-detected at repo root)
- Environment variables: `RESEND_API_KEY`, `LEAD_TO_EMAIL`, `LEAD_FROM_EMAIL`
- To rebuild locally after edits: `python3 tools/build.py && python3 tools/audit.py`

## Open decisions for the owner
1. Confirm pesthalt.us is free and buy it (or pick the backup).
2. Real phone number to replace (800) 555-0199.
3. ~~City scope~~ decided: 25,000+ population first (1,855 places).
4. Email address for the site (none shown until approved).
