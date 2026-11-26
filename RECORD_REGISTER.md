# PestHalt — Record Register

Every build step is logged here: what was done before, what is being done now, and what comes next.

| # | Date | Step | Status | Details |
|---|------|------|--------|---------|
| 0 | 2026-11-16 | Planning | Done | Nationwide pest control build plan: Semrush market data, state tiers, URL architecture, monetization, rollout |
| 1.1 | 2026-11-26 | Intake & brand | Done | Brand **PestHalt**, domain **pesthalt.us** (backup bughalt.us); own call routing; temporary toll-free (800) 555-0199; legal pages name Anjam Javed; copy uses referral framing because pest control is state-licensed work |
| 1.2 | 2026-11-26 | Keyword research | Done | Semrush US (Nov 2026): primary keyword per page chosen for volume and low KD (see keyword map below) |
| 1.3 | 2026-11-26 | Source verification | Done | EPA (IPM, termites, bed bugs, mosquito), CDC (rodent seal-up / clean-up), NPIC, UF/IFAS, MSU Extension confirmed via search |
| 1.4 | 2026-11-26 | Images | Done | 25 Pexels candidates downloaded and visually checked; 22 converted to WebP (600w/1200w); 3 branded photos removed; 3 SVG illustrations created |
| 1.5 | 2026-11-26 | Generator + design system | Done | `tools/core.py` (layout, CSS, schema, sitemap, headers), `tools/build.py`; palette: forest green + amber; system fonts; inline CSS, 1.6 KB deferred JS |
| 1.6 | 2026-11-26 | Home page | Done | H1 "Pest Control Near You, in All 50 States"; 13 service cards; how it works; areas served; cost factors; warning signs; 8 FAQs; Organization/WebSite/HomeAndConstructionBusiness/WebPage/FAQPage schema |
| 1.7 | 2026-11-26 | Services hub + 13 service pages | Done | Each: quick answer, what's included, signs table, steps, competitor-gap sections, cost factors, DIY vs pro, licensing notes, local note, FAQ, sources, related services, state pills; WebPage+Service+FAQPage+BreadcrumbList schema |
| 1.8 | 2026-11-26 | Locations hub | Done | All 50 states + DC grouped by Census region with common pests; anchors per state (become links in Build 2) |
| 1.9 | 2026-11-26 | Trust & legal pages | Done | About, Contact (form + TCPA consent text), Disclaimer, Editorial policy, Privacy (CCPA/CPRA + state privacy laws, TCPA, COPPA, breach notice), Terms, Accessibility (WCAG 2.1 AA), 404 |
| 1.10 | 2026-11-26 | Contact form backend | Done | `functions/api/lead.js` (Cloudflare Pages Function → Resend), honeypot, validation |
| 1.11 | 2026-11-26 | Audit | Done | `tools/audit.py`: 24 pages, 0 issues; responsive 360/768/1280 OK; no console errors |
| 1.12 | 2026-11-26 | Push | Done | Committed to github.com/bobee1/PestControlUSA (main) |
| 2.1 | 2026-11-26 | City scope + dataset | Done | Owner chose cities 25,000+ first. Built `tools/data/places_25k.csv` (1,855 places: 1,553 incorporated, 300 CDPs, + Washington DC 689,545 added manually) from 2020 Census data (bdurand/us_geo mirror) |
| 2.2 | 2026-11-26 | State content | Done | Unique text for 50 states + DC: intro, local factors, 4–5 problem rows, tips, licensing agency, FAQ; season calendar per state; extra housing paragraph for 11 smaller states |
| 2.3 | 2026-11-26 | State pages | Done | 51 pages at /locations/{state}/ with city tables, WebPage + Service (areaServed State, containsPlace) + FAQPage + BreadcrumbList schema |
| 2.4 | 2026-11-26 | Glossary | Done | /glossary/ with 55 terms, DefinedTermSet schema, auto-links (max 4 per page) from service and state pages |
| 2.5 | 2026-11-26 | Navigation + links | Done | Locations dropdown (51 states), footer glossary, service pills → state pages, home areas → state pages, hub cards → state pages |
| 2.6 | 2026-11-26 | Audit | Done | 76 pages, 0 issues; location uniqueness lowest 62%, avg 73%; responsive + console checks OK |
| 2.7 | 2026-11-26 | Push | Done | Committed to main |
| 3.1 | 2026-11-26 | Batch 1 selection | Done | Owner asked for short, high-quality batches. 10 cities: Houston, San Antonio, Dallas, Austin, Fort Worth, Jacksonville, Miami, Tampa, Orlando, St. Petersburg |
| 3.2 | 2026-11-26 | City research | Done | Semrush city keywords (e.g. pest control Houston 3,600/mo, pest control Austin 2,400 KD 26, rodent control Miami 1,000 KD 18, termite treatment Tampa 720); 2020 ZCTA ZIP codes saved to `tools/data/city_zips_batch1.json` |
| 3.3 | 2026-11-26 | City content | Done | `tools/content/cities_b1.py`: neighborhoods, history, problems, topic section, calendar, tips, FAQs per city |
| 3.4 | 2026-11-26 | City builder + linking | Done | `tools/content/citypages.py`; nearby 25k+ places within 35 mi; state tables link cities; service pages link 3–5 cities each with varied anchors |
| 3.5 | 2026-11-26 | Audit | Done | 86 pages, 0 issues; city uniqueness 88–91%; every city 3+ in-text inbound links |
| 3.6 | 2026-11-26 | Push | Done | Committed to main |
| 4.1 | 2026-11-26 | Batch 2 research | Done | Semrush keywords for 10 cities (40 terms); ZIP codes for all 25k+ places saved to `tools/data/city_zips.json` |
| 4.2 | 2026-11-26 | Batch 2 content | Done | `tools/content/cities_b2.py`: El Paso, Arlington, Corpus Christi, Plano, Hialeah, Fort Lauderdale, Phoenix, Tucson, Mesa, Scottsdale |
| 4.3 | 2026-11-26 | Linking | Done | Service pages link up to 6 city guides each (keyword-matched first); new audit check enforces 3+ in-text inbound links per city |
| 4.4 | 2026-11-26 | Audit | Done | 96 pages, 0 issues; city uniqueness 82–91%; responsive and console checks clean |
| 4.5 | 2026-11-26 | Push | Done | Committed to main |
| 5 | Next | City pages batch 3 | Coming | California: Los Angeles, San Diego, San Jose, San Francisco, Fresno, Sacramento, Long Beach, Oakland, Bakersfield, Anaheim |
| 6+ | Later | Remaining city batches | Planned | Until all 1,855 places are live |
| 4+ | Later | Blog | Planned | Per Blog Post Criteria doc |

## Keyword map (Semrush US, Nov 2026)

| Page | Primary keyword | Volume | KD | Secondary |
|------|-----------------|--------|----|-----------|
| / | pest control near me | 201,000 | 52 | pest control (673K, KD 10), exterminator near me |
| /services/general-pest-control/ | general pest control | 1,600 | 36 | quarterly pest control (KD 7), pest inspection (KD 22) |
| /services/termite-control/ | termite control | 49,500 | 22 | termite exterminator (KD 19), termite treatment |
| /services/termite-inspection/ | termite inspection | 33,100 | 35 | signs of termites (KD 26), WDI report |
| /services/rodent-control/ | rodent control | 60,500 | 34 | mouse exterminator (KD 22), rat control |
| /services/bed-bug-treatment/ | bed bug exterminator | 27,100 | 53 | bed bug heat treatment (KD 15) |
| /services/cockroach-control/ | roach exterminator | 8,100 | 37 | cockroach control |
| /services/ant-control/ | ant exterminator | 14,800 | 43 | carpenter ant treatment (KD 21), fire ant control (KD 29) |
| /services/mosquito-control/ | mosquito control service | 4,400 | 46 | mosquito yard treatment (KD 33) |
| /services/wasp-bee-removal/ | wasp nest removal | 18,100 | 39 | wasp removal, bee removal, hornet nest removal |
| /services/spider-control/ | spider exterminator | 9,900 | 25 | spider control |
| /services/flea-tick-control/ | flea exterminator | 6,600 | 35 | flea and tick yard treatment (KD 17) |
| /services/wildlife-removal/ | wildlife removal | 8,100 | 48 | raccoon removal (KD 18), squirrel removal (KD 23), bat removal (KD 26) |
| /services/commercial-pest-control/ | commercial pest control | 18,100 | 28 | restaurant pest control (KD 7) |

## Image register (Pexels, converted to WebP)

| File | Pexels ID | Used on |
|------|-----------|---------|
| home-hero | 3958958 | Home hero |
| indoor-treatment | 4176550 | Services hub hero |
| general-pest-control | 4176549 | General pest control |
| termite-control | 18087296 | Termite control |
| termite-inspection / home-exterior-2 | 164558 / 3935333 | Termite inspection |
| rodent-control | 69221 | Rodent control |
| cockroach-control / german-cockroach | 19294665 / 27033323 | Cockroach control |
| ant-control / ants-aphids | 36498272 / 32681811 | Ant control |
| mosquito-control / mosquito-bite | 37020717 / 12972048 | Mosquito control |
| wasp-bee-removal / yellow-jacket | 38680283 / 34430734 | Wasp & bee removal |
| spider-control / spider-web | 34154708 / 42246 | Spider control |
| commercial-pest-control / housefly | 32055757 / 14512575 | Commercial pest control |
| about | 106399 | About |
| contact | 209296 | Contact |
| locations-hub | 1396132 | Locations hub |
| Removed (branding visible) | 19789837, 19789841, 16851694 | Not used |
