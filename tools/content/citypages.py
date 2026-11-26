"""City pages: /locations/{state}/{city}/"""
import csv, os, math, json, html
import core as S
from content.statepages import BY_AB, load_places, display_name, fmt, SVC_NAME
from content.cities_b1 import CITIES_B1

CITIES = {}
CITIES.update(CITIES_B1)

WIKI_CITY = {"Houston": "Houston", "San Antonio": "San_Antonio", "Dallas": "Dallas", "Austin": "Austin,_Texas",
             "Fort Worth": "Fort_Worth,_Texas", "Jacksonville": "Jacksonville,_Florida", "Miami": "Miami",
             "Tampa": "Tampa,_Florida", "Orlando": "Orlando,_Florida", "Saint Petersburg": "St._Petersburg,_Florida"}
STATE_FULL = {"TX": "Texas", "FL": "Florida"}

ZIPS = json.load(open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "city_zips_batch1.json")))


def dist(a, b):
    la1, lo1, la2, lo2 = map(math.radians, [float(a["lat"]), float(a["lng"]), float(b["lat"]), float(b["lng"])])
    d = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return 3958.8 * 2 * math.asin(math.sqrt(d))


def city_url(key):
    c = CITIES[key]
    return f"/locations/{BY_AB[key[1]][0]}/{c['slug']}/"


def city_name(key):
    return CITIES[key].get("display", key[0])


def built_city_links():
    """(state_ab, dataset name) -> url, for linking from state tables and services."""
    return {k: city_url(k) for k in CITIES}


def city_page(key, row, allrows):
    c = CITIES[key]
    ab = key[1]
    sslug, sname = BY_AB[ab][0], BY_AB[ab][1]
    nm = city_name(key)
    url = city_url(key)
    crumbs = [("Home", "/"), ("Locations", "/locations/"), (sname, f"/locations/{sslug}/"), (nm, url)]
    zips = ZIPS.get(f"{'St. Petersburg' if key[0]=='Saint Petersburg' else key[0]}|{ab}", [])
    pop = int(row["population"])
    hu = int(row["housing_units"])
    # nearby 25k+ communities
    others = [r for r in allrows if r["geoid"] != row["geoid"]]
    near = sorted(((dist(row, r), r) for r in others), key=lambda x: x[0])
    near_local = [r for d, r in near if d <= 35][:10]
    built = {k: city_url(k) for k in CITIES if k != key}
    near_built = sorted(((dist(row, r), (r["name"], r["state"])) for r in allrows if (r["name"], r["state"]) in built), key=lambda x: x[0])[:3]

    def nlink(r):
        k = (r["name"], r["state"])
        label = CITIES[k].get("display", r["name"]) if k in CITIES else r["name"]
        return f'<a href="{built[k]}">{label}</a>' if k in built else label

    stats = (f"{nm} had {fmt(pop)} residents and about {fmt(hu)} housing units in the 2020 Census, spread across {c['county']}"
             + (f" and {len(zips)} ZIP codes" if zips else "") + f". {S.BRAND} connects callers in every part of the city, including {', '.join(c['hoods'][:5])} and {c['hoods'][5]}.")

    why = "".join(f"<p>{p}</p>" for p in c["why"])
    prow = "".join(f'<tr><td>{p}</td><td>{w}</td><td><a href="/services/{svc}/">{SVC_NAME[svc]} in {nm}</a></td></tr>' for p, w, svc in c["problems"])
    tips = "".join(f"<li>{t}</li>" for t in c["tips"])
    seasons = "".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a, b in zip(("Spring", "Summer", "Fall", "Winter"), c["seasons"]))
    zip_text = ", ".join(zips)
    cover = (f"Do you cover all of {nm}?",
             f"Yes. {S.BRAND} connects callers across {nm}, including {', '.join(c['hoods'][:-1])} and {c['hoods'][-1]}"
             + (f", in ZIP codes {zip_text}" if zips and len(zips) <= 60 else (f", in all {len(zips)} ZIP codes from {zips[0]} to {zips[-1]}" if zips else "")) + ".")
    faqs = c["faqs"] + [cover]
    near_txt = ", ".join(nlink(r) for r in near_local)
    pills = "".join(f'<li><a href="{built[k]}">Pest control in {CITIES[k].get("display", k[0])}</a></li>' for d, k in near_built)
    pills += f'<li><a href="/locations/{sslug}/">Pest control in {sname}</a></li><li><a href="/">{S.BRAND} home</a></li><li><a href="/locations/">All locations</a></li>'

    from content.pages import svc_cards
    body = f'''<div class="wrap"><div class="content">
<p class="quick"><strong>Quick answer:</strong> {c["quick"]} Call {S.PHONE_DISPLAY} to reach a licensed local provider.</p>
<p>{stats}</p>
<h2>Why pest control in {nm} is different</h2>
{why}
<h2>Common pest problems in {nm}</h2>
<div class="tbl-wrap"><table class="tbl"><thead><tr><th>Problem</th><th>Where it shows up</th><th>What helps</th></tr></thead><tbody>{prow}</tbody></table></div>
{S.cta_box(f"Pest trouble in {nm}?", f"Call to reach a licensed exterminator who works in {nm} and {c['county']}.")}
<h2>{c["topic"][0]}</h2>
{c["topic"][1]}
<h2>Pest calendar for {nm}</h2>
<div class="tbl-wrap"><table class="tbl"><thead><tr><th>Season</th><th>What {nm} homeowners usually see</th></tr></thead><tbody>{seasons}</tbody></table></div>
<h2>Pest control tips for {nm} residents</h2>
<ul class="checklist">{tips}</ul>
{S.faq_html(faqs, f"Pest control in {nm}: common questions")}
<h2>Pest control services in {nm}</h2>
<p>Licensed providers serving {nm} handle every service below, from one-time visits to year-round plans.</p>
{svc_cards()}
<h2>Nearby areas covered</h2>
<p>Providers who serve {nm} also cover nearby communities, including {near_txt}.</p>
<ul class="pills">{pills}</ul>
</div></div>
{S.call_band(f"Pest control in {nm}, {ab}", f"Call to reach a licensed provider serving {nm} and {c['county']}.")}'''

    hero = S.page_hero(crumbs, f"Pest Control in {nm}, {ab}", c["lead"], None, "", [c["county"], f"{len(zips)} ZIP codes" if zips else sname, "Licensed local providers"])
    title = f"Pest Control {nm}, {ab} | Exterminators | {S.BRAND}"
    if len(title) > 60:
        title = f"Pest Control {nm}, {ab} | {S.BRAND}"
    top3 = [p[0].split(" in ")[0].split(" after ")[0].lower() for p in c["problems"][:3]]
    meta = f"Pest control in {nm}, {ab}: {top3[0]}, {top3[1]} and {top3[2]}. Licensed local exterminators. Call {S.PHONE_DISPLAY}."
    if len(meta) > 155:
        meta = f"Pest control in {nm}, {ab}: {top3[0]} and {top3[1]}. Licensed local exterminators. Call {S.PHONE_DISPLAY}."
    if len(meta) > 155:
        meta = f"Pest control in {nm}, {ab} for termites, roaches, rodents and more. Licensed local exterminators. Call {S.PHONE_DISPLAY}."

    full = S.BASE + url
    county_wiki = "https://en.wikipedia.org/wiki/" + c["county"].replace(" ", "_") + "," + "_" + STATE_FULL[ab]
    city_node = {"@type": "City", "name": f"{nm}, {ab}", "sameAs": "https://en.wikipedia.org/wiki/" + WIKI_CITY[key[0]],
                 "containedInPlace": {"@type": "AdministrativeArea", "name": c["county"], "sameAs": county_wiki,
                                      "containedInPlace": {"@type": "State", "name": sname}}}
    schema = [
        {"@type": "WebPage", "@id": f"{full}#webpage", "url": full, "name": f"Pest Control in {nm}, {ab}", "isPartOf": {"@id": S.SITE_ID},
         "about": [{"@id": f"{full}#service"}, {"@type": "Thing", "name": "Pest control", "sameAs": "https://en.wikipedia.org/wiki/Pest_control"}],
         "mentions": [city_node], "dateModified": S.TODAY_ISO, "inLanguage": "en-US", "breadcrumb": {"@id": f"{full}#breadcrumb"}},
        {"@type": "Service", "@id": f"{full}#service", "name": f"Pest control in {nm}, {ab}", "serviceType": "Pest control", "url": full,
         "provider": {"@type": "HomeAndConstructionBusiness", "@id": S.BIZ_ID, "name": S.BRAND, "url": S.BASE + "/", "telephone": S.PHONE_TEL},
         "areaServed": city_node,
         "availableChannel": {"@type": "ServiceChannel", "servicePhone": {"@type": "ContactPoint", "telephone": S.PHONE_TEL, "contactType": "customer service", "areaServed": "US"}}},
        S.faq_schema(faqs, full),
    ]
    S.page(url, title, meta, hero, body, crumbs=crumbs, schema=schema, priority=0.8, kind="state", word_target=(800, 1600))


def build_cities():
    places = load_places()
    for key in CITIES:
        rows = places[key[1]]
        row = [r for r in rows if r["name"] == key[0]][0]
        city_page(key, row, rows)


_ALLOC = {}


def _allocate():
    """Spread city links across services so every city gets in-text links from 3+ service pages."""
    from collections import Counter
    count = Counter()
    services = sorted({p[2] for c in CITIES.values() for p in c["problems"]},
                      key=lambda sl: sum(1 for c in CITIES.values() if any(p[2] == sl for p in c["problems"])))
    for sl in services:
        hits = [k for k, c in CITIES.items() if any(p[2] == sl for p in c["problems"])]
        word = SVC_NAME.get(sl, sl).split()[0].lower()
        hits.sort(key=lambda k: (not any(word in x.lower() for x in CITIES[k]["secondary"]), count[k], list(CITIES).index(k)))
        pick = hits[:5]
        for k in pick:
            count[k] += 1
        _ALLOC[sl] = pick
    return count


def service_city_sentence(slug):
    """In-text links from a service page to built city pages where that service is a top local problem."""
    if not _ALLOC:
        _allocate()
    hits = _ALLOC.get(slug, [])
    if not hits:
        return ""
    anchors = ["{svc} in {city}", "{city} {svc_l}", "{svc} for {city} homes", "{city}, {ab}"]
    links = []
    for i, k in enumerate(hits):
        a = anchors[i % len(anchors)].format(svc=SVC_NAME[slug].lower(), svc_l=SVC_NAME[slug].lower(), city=city_name(k), ab=k[1])
        links.append(f'<a href="{city_url(k)}">{a}</a>')
    joined = ", ".join(links[:-1]) + " and " + links[-1] if len(links) > 1 else links[0]
    return f" Local city guides: {joined}."
