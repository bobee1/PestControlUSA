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
| 5.1 | 2026-11-26 | Batch 3 research | Done | Semrush keywords for 10 California cities (40 terms); ZIP codes from `tools/data/city_zips.json` (7–102 per city) |
| 5.2 | 2026-11-26 | Batch 3 content | Done | `tools/content/cities_b3.py`: LA, San Diego, San Jose, San Francisco, Fresno, Sacramento, Long Beach, Oakland, Bakersfield, Anaheim |
| 5.3 | 2026-11-26 | Linking upgrade | Done | City pages link the 3 nearest same-state city guides in-text; fixes cities without nearby guides |
| 5.4 | 2026-11-26 | Audit | Done | 106 pages, 0 issues; CA city uniqueness 82–87%; responsive and console checks clean |
| 5.5 | 2026-11-26 | Push | Done | Committed to main |
| 6.1 | 2026-11-26 | Dataset fix | Done | Found consolidated city-counties missing from the census mirror (Nashville, Louisville, Indianapolis, Augusta, Columbus GA, Athens GA, Butte) plus blank populations (Methuen, Watertown, Penn Hills, Mount Lebanon). Added with 2020 Census counts; dataset now 1,866 places; ZIPs added where available |
| 6.2 | 2026-11-26 | Batch 4 research | Done | Semrush keywords for 10 Southeast cities (40 terms) |
| 6.3 | 2026-11-26 | Batch 4 content | Done | `tools/content/cities_b4.py`: Atlanta, Charlotte, Raleigh, Nashville, Memphis, New Orleans, Baton Rouge, Birmingham, Charleston SC, Savannah |
| 6.4 | 2026-11-26 | Linking upgrade | Done | Cross-state nearest-guide fallback for states with fewer than 3 city guides (fixed Birmingham, Charleston) |
| 6.5 | 2026-11-26 | Audit | Done | 116 pages, 0 issues; city uniqueness 80–85%; responsive and console checks clean |
| 6.6 | 2026-11-26 | Push | Done | Committed to main |
| 7.1 | 2026-11-26 | Batch 5 research | Done | Semrush keywords for 10 cities (40 terms); ZIP codes 18–57 per city |
| 7.2 | 2026-11-26 | Batch 5 content | Done | `tools/content/cities_b5.py`: Chicago, Indianapolis, Columbus OH, Kansas City, St. Louis, Louisville, Oklahoma City, Tulsa, Denver, Las Vegas |
| 7.3 | 2026-11-26 | Linking guarantee | Done | `plan_guides()` precomputes city guide links and tops up any city with fewer than 3 in-text inbound links |
| 7.4 | 2026-11-26 | Audit | Done | 126 pages, 0 issues; responsive and console checks clean |
| 7.5 | 2026-11-26 | Push | Done | Committed to main |
| 8.1 | 2026-11-26 | Batch 6 scope | Done | Washington DC replaced with Jersey City (DC state page already serves as the city page) |
| 8.2 | 2026-11-26 | Batch 6 research | Done | Semrush keywords for 10 cities (40 terms); ZIP codes 7–181 per city |
| 8.3 | 2026-11-26 | Batch 6 content | Done | `tools/content/cities_b6.py`: NYC, Philadelphia, Boston, Baltimore, Pittsburgh, Newark, Jersey City, Providence, Virginia Beach, Richmond |
| 8.4 | 2026-11-26 | Link planner fix | Done | Planner uses each page's actual 10-closest nearby list; fixed Dallas inbound count |
| 8.5 | 2026-11-26 | Audit | Done | 136 pages, 0 issues; South Dakota state page 61% uniqueness flagged as watch item |
| 8.6 | 2026-11-26 | Push | Done | Committed to main |
| 9.1 | 2026-11-26 | Batch 7 data check | Done | Dataset names "Boise City" and "Urban Honolulu" (CDP) shown as Boise and Honolulu; ZIPs 8–27 per city |
| 9.2 | 2026-11-26 | Batch 7 research | Done | Semrush keywords for 10 cities (40 terms) |
| 9.3 | 2026-11-26 | Batch 7 content | Done | `tools/content/cities_b7.py`: Seattle, Portland, Spokane, Tacoma, Boise, Salt Lake City, Albuquerque, Colorado Springs, Anchorage, Honolulu |
| 9.4 | 2026-11-26 | Template updates | Done | Display names now used on state pages for every built city; optional `nearby` list fills the nearby-areas paragraph for isolated cities (Anchorage, Spokane); nearby lists now read "A, B and C" |
| 9.5 | 2026-11-26 | Audit | Done | 146 pages, 0 issues; batch uniqueness 82–88%; responsive 360/768/1280 clean |
| 9.6 | 2026-11-26 | Push | Done | Committed to main |
| 10.1 | 2026-11-26 | Batch 8 data check | Done | Dataset name "Saint Paul" shown as St. Paul; ZIPs 11–30 per city |
| 10.2 | 2026-11-26 | Batch 8 research | Done | Semrush keywords for 10 cities (40 terms) |
| 10.3 | 2026-11-26 | Batch 8 content | Done | `tools/content/cities_b8.py`: Detroit, Milwaukee, Minneapolis, St. Paul, Cleveland, Cincinnati, Omaha, Wichita, Madison, Des Moines |
| 10.4 | 2026-11-26 | Audit | Done | 156 pages, 0 issues; batch uniqueness 77–86%; responsive 360/768/1280 clean |
| 10.5 | 2026-11-26 | Push | Done | Committed to main |
| 11.1 | 2026-11-26 | Batch 9 data check | Done | Dataset name "Lexington-Fayette Urban County" shown as Lexington; Norfolk and Chesapeake use independent-city county text; ZIPs 6–15 per city |
| 11.2 | 2026-11-26 | Batch 9 research | Done | Semrush keywords for 10 cities (40 terms) |
| 11.3 | 2026-11-26 | Batch 9 content | Done | `tools/content/cities_b9.py`: Lexington, Knoxville, Chattanooga, Greensboro, Durham, Winston-Salem, Norfolk, Chesapeake, Tallahassee, Cape Coral |
| 11.4 | 2026-11-26 | Template fix | Done | Nearby paragraph reads "also cover the rest of {county}" when no nearby towns exist; nearby lists added for Knoxville, Chattanooga, Tallahassee |
| 11.5 | 2026-11-26 | Audit | Done | 166 pages, 0 issues; batch uniqueness 76–87%; responsive 360/768/1280 clean |
| 11.6 | 2026-11-26 | Push | Done | Committed to main |
| 12.1 | 2026-11-26 | Batch 10 data check | Done | All 10 names match the dataset; ZIPs 3–14 per city |
| 12.2 | 2026-11-26 | Batch 10 research | Done | Semrush keywords for 10 cities (40 terms) |
| 12.3 | 2026-11-26 | Batch 10 content | Done | `tools/content/cities_b10.py`: Laredo, Lubbock, Amarillo, Brownsville, McAllen, Garland, Irving, Grand Prairie, Frisco, McKinney; topics chosen to avoid overlap with earlier Texas pages (no new scorpion topics) |
| 12.4 | 2026-11-26 | Nearby lists | Done | Smaller towns added for Laredo, Lubbock, Amarillo, Brownsville |
| 12.5 | 2026-11-26 | Audit | Done | 176 pages, 0 issues; batch uniqueness 78–84%; responsive 360/768/1280 clean |
| 12.6 | 2026-11-26 | Push | Done | Committed to main |
| 13.1 | 2026-11-26 | Batch 11 data check | Done | All 10 names match the dataset; ZIPs 3–11 per city |
| 13.2 | 2026-11-26 | Batch 11 research | Done | Semrush keywords for 10 cities (40 terms) |
| 13.3 | 2026-11-26 | Batch 11 content | Done | `tools/content/cities_b11.py`: Riverside, San Bernardino, Fontana, Moreno Valley, Santa Ana, Irvine, Chula Vista, Stockton, Modesto, Fremont; topics chosen to avoid overlap with Build 3 California pages |
| 13.4 | 2026-11-26 | Audit | Done | 186 pages, 0 issues; batch uniqueness 80–84%; responsive 360/768/1280 clean |
| 13.5 | 2026-11-26 | Push | Done | Committed to main |
| 14.1 | 2026-11-26 | Batch 12 data check | Done | All 10 names match the dataset; ZIPs 4–13 per city |
| 14.2 | 2026-11-26 | Batch 12 research | Done | Semrush keywords for 10 cities (40 terms) |
| 14.3 | 2026-11-26 | Batch 12 content | Done | `tools/content/cities_b12.py`: Chandler, Gilbert, Glendale AZ, Peoria AZ, Henderson, North Las Vegas, Reno, Aurora, Fort Collins, Lakewood CO; no new scorpion topics |
| 14.4 | 2026-11-26 | Audit | Done | 196 pages, 0 issues; batch uniqueness 76–82%; Nevada state page now 64% (watch); responsive clean |
| 14.5 | 2026-11-26 | Push | Done | Committed to main |
| 15.1 | 2026-11-26 | Batch 13 data check | Done | Dataset name "Port Saint Lucie" shown as Port St. Lucie; ZIPs 2–10 per city |
| 15.2 | 2026-11-26 | Batch 13 research | Done | Semrush keywords for 10 cities (40 terms) |
| 15.3 | 2026-11-26 | Batch 13 content | Done | `tools/content/cities_b13.py`: Port St. Lucie, Pembroke Pines, Hollywood, Miramar, Coral Springs, West Palm Beach, Clearwater, Lakeland, Gainesville, Palm Bay; topics chosen to avoid overlap with the 12 earlier Florida pages |
| 15.4 | 2026-11-26 | Audit | Done | 206 pages, 0 issues; batch uniqueness 77–83%; Florida state page 83%; responsive clean |
| 15.5 | 2026-11-26 | Push | Done | Committed to main |
| 16.1 | 2026-11-26 | State page uniqueness pass | Done | New `tools/content/states_extra.py`: an extra state-specific section for the 13 lowest states (SD, KS, NH, WY, WV, ND, NV, OK, KY, NE, RI, MT, NM); all state pages now 66%+ (were 61–66%) |
| 16.2 | 2026-11-26 | Batch 14 research | Done | Semrush keywords for 10 cities (40 terms); all names match the dataset |
| 16.3 | 2026-11-26 | Batch 14 content | Done | `tools/content/cities_b14.py`: Fort Wayne, Toledo, Akron, Grand Rapids, Lincoln, Sioux Falls, Overland Park, Springfield MO, Rochester MN, Cedar Rapids; South Dakota gets its first city guide |
| 16.4 | 2026-11-26 | Audit | Done | 216 pages, 0 issues; batch uniqueness 74–81%; responsive clean |
| 16.5 | 2026-11-26 | Push | Done | Committed to main |
| 17.1 | 2026-11-26 | Batch 15 data check | Done | Connecticut rows use 2022 planning regions; pages use the historic counties (Hartford, New Haven, Fairfield) for county text and schema |
| 17.2 | 2026-11-26 | Batch 15 research | Done | Semrush keywords for 10 cities (40 terms) |
| 17.3 | 2026-11-26 | Batch 15 content | Done | `tools/content/cities_b15.py`: Buffalo, Rochester NY, Syracuse, Yonkers, Worcester, Springfield MA, Hartford, New Haven, Bridgeport, Allentown |
| 17.4 | 2026-11-26 | Same-name fix | Done | Rochester (MN/NY) and Springfield (MO/MA) produced identical service paragraphs; the paragraph now names the state ("Licensed {State} providers serving…") on every city page |
| 17.5 | 2026-11-26 | Audit | Done | 226 pages, 0 issues; batch uniqueness 68–83% (same-name pairs lowest); responsive clean |
| 17.6 | 2026-11-26 | Push | Done | Committed to main |
| 18.1 | 2026-11-26 | Dataset fix | Done | Removed a duplicate Columbus, GA row (manual Build 6 entry, GEOID 1319007) that duplicated the Census row 1319000; Georgia table now lists Columbus once |
| 18.2 | 2026-11-26 | Batch 16 research | Done | Semrush keywords for 10 cities (40 terms) |
| 18.3 | 2026-11-26 | Batch 16 content | Done | `tools/content/cities_b16.py`: Columbia SC, Greenville SC, Augusta, Columbus GA, Huntsville, Montgomery, Mobile, Jackson MS, Little Rock, Shreveport; base names checked (Fort Benning and Fort Gordon restored in 2025) |
| 18.4 | 2026-11-26 | Audit | Done | 236 pages, 0 issues; batch uniqueness 73–81%; responsive clean |
| 18.5 | 2026-11-26 | Push | Done | Committed to main |
| 19 | Next | City pages batch 17 | Coming | Alexandria VA, Arlington VA, Newport News, Hampton, Cary, Fayetteville NC, Wilmington NC, High Point, Clarksville, Murfreesboro |
| 10+ | Later | Remaining city batches | Planned | Until all 1,866 places are live |
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
