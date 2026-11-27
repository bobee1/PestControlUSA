# PestHalt — Build Status

**Site:** PestHalt · nationwide pest control referral site · target domain **pesthalt.us** (not yet purchased)
**Repo:** github.com/bobee1/PestControlUSA · **Owner/operator:** Anjam Javed
**Phone (temporary):** (800) 555-0199 → replace with the real toll-free number before launch
**Last updated:** 2026-11-26 (Build 33)

## Previous step — Build 32: DC page + city pages batch 30 ✅
- Washington, DC page upgraded (rodent program, wards, row house termites, DOEE licensing); Mesquite, Olathe, Thornton, Metairie, Fargo, Norman, Visalia, Fullerton, Pasadena CA.

## Current step — Build 33: city pages batch 31 ✅ complete
- **Places live:** Paradise, Enterprise, Spring Valley and Sunrise Manor (NV; each page explains it's an unincorporated Clark County town with a Las Vegas mailing address), plus Columbia MO, Topeka KS, Meridian ID, Lafayette LA, Billings MT and Lewisville TX.
- **Keyword highlights (Semrush US):** pest control Paradise NV 70 (KD 4); roach exterminator Las Vegas 140 (KD 9); exterminator Billings MT 90 (KD 15); scorpion control Las Vegas 210 (KD 16); pest control Lewisville 390 (KD 18). The NV town names themselves get little search volume, so those pages also target Las Vegas service terms the main Las Vegas page doesn't (commercial, termites, bee removal, bed bugs).
- **Place-specific topics:** commercial pest control on the Strip (Paradise), subterranean termites in new homes (Enterprise), bee swarms and Africanized bees (Spring Valley), bed bugs in apartments and weekly motels (Sunrise Manor), carpenter bees (Columbia), brown recluse vs. wolf spider ID (Topeka), voles in lawns (Meridian), fire ant rafts and floods (Lafayette), deer mice and hantavirus (Billings), spiders and lake insects (Lewisville).
- **Checks:** 385 pages, 0 issues; batch uniqueness 74–79%; Columbia MO and Columbia SC both fine; responsive 360/768/1280 clean.

## Coming next — Build 34: city pages batch 32 (10 cities)
- Proposed: California fifth tier: Orange, Victorville, Santa Clara, Simi Valley, Thousand Oaks, Vallejo, Concord, Clovis, Berkeley, Fairfield.
- Scope rule (owner, 2026-11-27): all 50 states (Alaska and Hawaii stay) plus Washington, DC; no overseas territories.

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
