# PestHalt — Build Status

**Site:** PestHalt · nationwide pest control referral site · target domain **pesthalt.us** (not yet purchased)
**Repo:** github.com/bobee1/PestControlUSA · **Owner/operator:** Anjam Javed
**Phone (temporary):** (800) 555-0199 → replace with the real toll-free number before launch
**Last updated:** 2026-11-26 (Build 7)

## Previous step — Build 6: city pages batch 4 ✅
- Atlanta, Charlotte, Raleigh, Nashville, Memphis, New Orleans, Baton Rouge, Birmingham, Charleston SC, Savannah; dataset fix (1,866 places).

## Current step — Build 7: city pages batch 5 ✅ complete (10 cities)
- **Cities live:** Chicago (IL), Indianapolis (IN), Columbus (OH), Kansas City and St. Louis (MO), Louisville (KY), Oklahoma City and Tulsa (OK), Denver (CO), Las Vegas (NV).
- **Keyword highlights (Semrush US):** pest control Las Vegas 2,900; pest control Chicago 2,400; pest control Kansas City 2,400; pest control Indianapolis 1,900; pest control Tulsa 1,900 (KD 26); pest control Denver 1,600 (KD 26, $33.47); rodent control Denver 880 (KD 25, $33.47); pest control St. Louis 1,300 (KD 15); exterminator Louisville KY KD 7.
- **City-specific topics:** alley rats (Chicago), termite inspections (Indianapolis), student rentals near Ohio State (Columbus), brown recluses (Kansas City), old brick and mortar gaps (St. Louis), Victorian and shotgun homes (Louisville), storm damage (Oklahoma City), oil-boom historic homes (Tulsa), mice and hail damage (Denver), desert-edge scorpions (Las Vegas).
- **Verified local events used:** Great Chicago Fire (1871), Chicago West Side floods (Jul 2023), Unigov (1970), Plaza flood (Sep 1977), Great Fire of 1849 and Great Flood of 1993 (St. Louis), Great Flood of 1937 and 2003 merger (Louisville), May 3 1999 tornado (OKC), Memorial Day flood (1984, Tulsa).
- **Linking upgrade:** city-to-city guide links are now planned up front with a guarantee: any city short of 3 in-text inbound links is added to its nearest neighbors' guide lists (fixed Denver and El Paso as service-page slots got more crowded).
- **Checks:** 126 pages, 0 issues; city uniqueness 77–87% this batch; responsive 360/768/1280 with no overflow or console errors.

## Coming next — Build 8: city pages batch 6 (10 cities)
- Proposed: Northeast and Mid-Atlantic: New York City, Philadelphia, Boston, Baltimore, Washington DC, Pittsburgh, Newark, Providence, Virginia Beach, Richmond.
- Brings NYC rats and bed bugs, Lyme ticks, stink bugs and spotted lanternflies, row-house rodents and Chesapeake mosquitoes.

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
