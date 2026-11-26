# PestHalt — Build Status

**Site:** PestHalt · nationwide pest control referral site · target domain **pesthalt.us** (not yet purchased)
**Repo:** github.com/bobee1/PestControlUSA · **Owner/operator:** Anjam Javed
**Phone (temporary):** (800) 555-0199 → replace with the real toll-free number before launch
**Last updated:** 2026-11-26 (Build 6)

## Previous step — Build 5: city pages batch 3 ✅
- Los Angeles, San Diego, San Jose, San Francisco, Fresno, Sacramento, Long Beach, Oakland, Bakersfield, Anaheim.

## Current step — Build 6: city pages batch 4 ✅ complete (10 Southeast cities)
- **Cities live:** Atlanta, Savannah (GA); Charlotte, Raleigh (NC); Nashville, Memphis (TN); New Orleans, Baton Rouge (LA); Birmingham (AL); Charleston (SC).
- **Keyword highlights (Semrush US):** pest control Atlanta 2,900 (KD 32); pest control Nashville 1,900 (KD 23); pest control Baton Rouge 1,900; pest control Raleigh 1,600 (KD 28); termite control Atlanta KD 9; mosquito control Atlanta 590 (KD 11); termite control New Orleans 390 (KD 19).
- **City-specific topics:** canopy and crawl spaces (Atlanta), new construction (Charlotte), historic-district termite inspections (Raleigh), brown recluses (Nashville), heat and termites (Memphis), Formosan termites in historic homes (New Orleans), flood recovery (Baton Rouge), hillside drainage (Birmingham), tidal flooding (Charleston), live oaks and marsh (Savannah).
- **Verified local events used:** Atlanta floods (Sept 2009), Hurricane Hugo (1989), Hurricane Fran (1996), Nashville flood (May 2010) and tornado (Mar 2020), Mississippi River crest at Memphis (May 2011), Formosan arrival after WWII, Katrina (2005) and Ida (2021), Baton Rouge flood (Aug 2016), Apr 27 2011 tornado outbreak, Matthew (2016) and Irma (2017) in Savannah.
- **Dataset fix:** the census mirror omitted consolidated city-counties and had blank populations for some cities. Added 11 places with 2020 Census counts: Nashville, Louisville, Indianapolis, Augusta, Columbus (GA), Athens (GA), Butte, Methuen, Watertown, Penn Hills, Mount Lebanon. Dataset now 1,866 places; affected state pages updated automatically.
- **Linking upgrade:** if a state has fewer than 3 other city guides, city pages link the nearest guides in neighboring states.
- **Checks:** 116 pages, 0 issues; Southeast city uniqueness 80–85%; responsive 360/768/1280 with no overflow or console errors.

## Coming next — Build 7: city pages batch 5 (10 cities)
- Proposed: Midwest and Mountain metros: Chicago, Indianapolis, Columbus (OH), Kansas City (MO), St. Louis, Louisville, Oklahoma City, Tulsa, Denver, Las Vegas.
- Brings rats and bed bugs in Chicago, brown recluses in Kansas City, St. Louis and Oklahoma, stink bugs, miller moths in Denver and desert scorpions in Las Vegas.

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
