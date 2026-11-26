"""State hub pages (/locations/{state}/) and the glossary page."""
import csv, os, re, html
import core as S
from content.states import STATES
from content.states_south import SOUTH
from content.states_west import WEST
from content.states_north import NORTH
from content.glossary import TERMS
from content.states_seasons import SEASONS

STATE_TEXT = {**SOUTH, **WEST, **NORTH}
BY_AB = {ab: (slug, name, ab, reg, pests) for slug, name, ab, reg, pests in STATES}

NEIGHBORS = {
 "AL": "FL GA TN MS", "AK": "WA OR HI", "AZ": "CA NV UT NM CO", "AR": "MO TN MS LA TX OK", "CA": "OR NV AZ HI",
 "CO": "WY NE KS OK NM AZ UT", "CT": "NY MA RI", "DE": "MD PA NJ", "DC": "MD VA", "FL": "GA AL",
 "GA": "FL AL TN NC SC", "HI": "CA AK", "ID": "WA OR NV UT WY MT", "IL": "WI IA MO KY IN", "IN": "IL MI OH KY",
 "IA": "MN WI IL MO NE SD", "KS": "NE MO OK CO", "KY": "IL IN OH WV VA TN MO", "LA": "TX AR MS", "ME": "NH",
 "MD": "PA DE VA WV DC", "MA": "NH VT NY CT RI", "MI": "OH IN WI", "MN": "WI IA SD ND", "MS": "LA AR TN AL",
 "MO": "IA IL KY TN AR OK KS NE", "MT": "ND SD WY ID", "NE": "SD IA MO KS CO WY", "NV": "CA OR ID UT AZ",
 "NH": "VT ME MA", "NJ": "NY PA DE", "NM": "AZ UT CO OK TX", "NY": "NJ PA CT MA VT", "NC": "VA TN GA SC",
 "ND": "MN SD MT", "OH": "PA WV KY IN MI", "OK": "KS MO AR TX NM CO", "OR": "WA ID NV CA", "PA": "NY NJ DE MD WV OH",
 "RI": "CT MA", "SC": "NC GA", "SD": "ND MN IA NE WY MT", "TN": "KY VA NC GA AL MS AR MO", "TX": "NM OK AR LA",
 "UT": "ID WY CO NM AZ NV", "VT": "NY NH MA", "VA": "MD DC WV KY TN NC", "WA": "ID OR AK", "WV": "OH PA MD VA KY",
 "WI": "MI MN IA IL", "WY": "MT SD NE CO UT ID",
}
WIKI_STATE = {"GA": "Georgia_(U.S._state)", "WA": "Washington_(state)", "NY": "New_York_(state)", "DC": "Washington,_D.C."}

SVC_NAME = {}


def load_places():
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "places_25k.csv")
    rows = list(csv.DictReader(open(path)))
    by = {}
    for r in rows:
        r["population"] = int(r["population"])
        by.setdefault(r["state"], []).append(r)
    return by


def display_name(ab, name):
    return "Washington, DC" if ab == "DC" else name


def fmt(n):
    return f"{n:,}"


def short_county(c):
    return c.replace(" County", "").replace(" Parish", " Parish").replace(" city", " City")


QUICK = [
 "<strong>Quick answer:</strong> Pest control in {dn} most often means dealing with {p}. {B} connects callers anywhere in {dn} with a local provider licensed through the {ag}. Call {ph} to set up an inspection.",
 "<strong>Quick answer:</strong> The pests {dn} homeowners call about most are {p}. One call to {ph} reaches a pest control provider licensed by the {ag} who serves your area.",
 "<strong>Quick answer:</strong> Across {dn}, the biggest pest problems are {p}. {B} links you with licensed local exterminators, regulated by the {ag}, at {ph}.",
 "<strong>Quick answer:</strong> If you live in {dn}, expect {p}. {B} puts you in touch with a provider holding a license from the {ag}; call {ph}.",
]
CTA = ["Call to reach a licensed pest control provider in {dn}.", "One call connects you with a licensed exterminator near you in {dn}.",
       "Talk to a licensed {dn} provider about an inspection.", "Get connected with licensed local pest control in {dn}."]
SVC_INTRO = ["Every service below is available to callers across {dn} through licensed local providers.",
             "These services are available throughout {dn}; choose one to see how it works.",
             "Licensed providers in {dn} handle each of these pest problems.",
             "Here's every pest control service {B} can connect you with in {dn}."]
FIND = ["Call {ph}. Share your city or ZIP code and the pest you're seeing, and you'll be connected with a licensed provider who serves your part of {dn}.",
        "Skip the search and call {ph}. Tell us your ZIP code and the problem, and we'll connect you with a licensed {dn} provider.",
        "The fastest way is to call {ph} with your location and what you're seeing; a licensed local provider in {dn} takes it from there.",
        "Call {ph} and describe the pest. {B} routes the call to a licensed exterminator who works in your {dn} community."]


def state_page(ab, places):
    slug, name, _, region, pest_summary = BY_AB[ab]
    vi = [x[2] for x in STATES].index(ab) % 4
    T = STATE_TEXT[ab]
    dn = display_name(ab, name)
    url = f"/locations/{slug}/"
    crumbs = [("Home", "/"), ("Locations", "/locations/"), (dn, url)]
    rows = sorted(places, key=lambda r: -r["population"])
    n = len(rows)
    total = sum(r["population"] for r in rows)
    top = [r["name"] for r in rows[:8]]
    counties = []
    for r in rows:
        for c in r["county"].split("; "):
            if c and c not in counties:
                counties.append(c)
    n_cdp = sum(1 for r in rows if r["kind"] == "cdp")

    first = pest_summary.split()[0]
    pests_lc = pest_summary if first in ("Formosan", "Africanized", "Argentine", "German", "Asian", "Rocky", "Norway") else pest_summary[0].lower() + pest_summary[1:]
    quick = QUICK[vi].format(dn=dn, p=pests_lc, B=S.BRAND, ag=T["agency"], ph=S.PHONE_DISPLAY)

    if ab == "DC":
        stats = (f"Washington is a single city of about {fmt(total)} residents (2020 Census), and {S.BRAND} covers every ward and neighborhood, "
                 "from Georgetown and Dupont Circle to Anacostia, Brookland and Navy Yard.")
    elif n == 1:
        r0 = rows[0]
        stats = (f"{r0['name']} ({fmt(r0['population'])} residents in the 2020 Census) is the only {dn} city above 25,000 people, but most of {dn} lives in smaller towns and rural communities, "
                 f"and {S.BRAND} connects callers across all of them, county by county.")
    else:
        biggest = rows[0]
        stats = (f"{dn} has {n} cities and communities with 25,000 or more residents, home to about {fmt(total)} people combined according to the 2020 Census. "
                 f"The largest is {biggest['name']} ({fmt(biggest['population'])}), followed by "
                 + (", ".join(top[1:3]) + " and " + top[3] if len(top) >= 4 else " and ".join(top[1:])) + f". These places span {len(counties)} {'parishes' if ab == 'LA' else 'counties' if ab != 'AK' else 'boroughs'}, "
                 f"and {S.BRAND} also connects callers in smaller towns and rural areas across the state.")
        if n_cdp:
            stats += f" {n_cdp} of the communities listed below are unincorporated census-designated places, which local residents usually know by name."

    why = "".join(f"<p>{p}</p>" for p in T["why"])
    prow = "".join(
        f'<tr><td>{p}</td><td>{w}</td><td><a href="/services/{svc}/">{SVC_NAME[svc]} in {dn}</a></td></tr>' for p, w, svc in T["pests"])
    tips = "".join(f"<li>{t}</li>" for t in T["tips"])
    seasons = "".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a, b in zip(("Spring", "Summer", "Fall", "Winter"), SEASONS[ab]))

    if ab == "DC":
        city_table = ""
    else:
        trs = "".join(
            f'<tr><td>{html.escape(r["name"])}{"*" if r["kind"] == "cdp" else ""}</td><td>{html.escape("; ".join(short_county(c) for c in r["county"].split("; ")))}</td><td>{fmt(r["population"])}</td></tr>'
            for r in rows)
        cnt_label = "Parish" if ab == "LA" else "Borough" if ab == "AK" else "County"
        city_table = (f'<h2>Cities we serve in {dn}</h2><p>{S.BRAND} connects callers in every {dn} city with 25,000 or more people, listed here by 2020 Census population, '
                      f'and in the smaller towns around them.</p>'
                      f'<div class="tbl-wrap"><table class="tbl"><thead><tr><th>City or community</th><th>{cnt_label}</th><th>Population (2020)</th></tr></thead><tbody>{trs}</tbody></table></div>'
                      + ('<p class="form-note">* Unincorporated census-designated place.</p>' if n_cdp else ""))

    top_list = ", ".join(top[:6])
    if ab == "DC":
        cover = (f"Do you cover all of Washington, DC?", "Yes. Calls from every ward, from Georgetown and Capitol Hill to Anacostia and Brookland, are connected with licensed providers who serve the District.")
    else:
        cover = (f"Do you cover all of {dn}?",
                 (f"Yes. {S.BRAND} connects callers in all {n} {dn} cities and communities over 25,000 people, including {top_list}, and in smaller towns and rural areas served by local providers." if n > 1 else f"Yes. {S.BRAND} connects callers in {top_list} and in every smaller {dn} town and rural community served by local providers."))
    faqs = [
        T["faq"],
        cover,
        (f"Who licenses pest control companies in {dn}?", f"Pest control in {dn} is licensed by the {T['agency']}. Ask any provider for its license number and verify it with the agency before work begins."),
        (f"How do I find pest control near me in {dn}?", FIND[vi].format(ph=S.PHONE_DISPLAY, dn=dn, B=S.BRAND)),
    ]

    nb = [BY_AB[x] for x in NEIGHBORS[ab].split()]
    pills = "".join(f'<li><a href="/locations/{b[0]}/">Pest control in {display_name(b[2], b[1])}</a></li>' for b in nb)
    pills += f'<li><a href="/">{S.BRAND} home</a></li><li><a href="/locations/">All states</a></li>'

    from content.pages import svc_cards
    body = f'''<div class="wrap"><div class="content">
<p class="quick">{quick}</p>
<p>{stats}</p>
<h2>Why pest control in {dn} is different</h2>
{why}
<h2>Common pest problems in {dn}</h2>
<div class="tbl-wrap"><table class="tbl"><thead><tr><th>Problem</th><th>Where it shows up</th><th>What helps</th></tr></thead><tbody>{prow}</tbody></table></div>
{S.cta_box(f"Pests in your {dn} home?", CTA[vi].format(dn=dn))}
<h2>Pest seasons in {dn}</h2>
<div class="tbl-wrap"><table class="tbl"><thead><tr><th>Season</th><th>What to expect</th></tr></thead><tbody>{seasons}</tbody></table></div>
<h2>Pest control tips for {dn} residents</h2>
<ul class="checklist">{tips}</ul>
<h2>Pest control licensing in {dn}</h2>
<p>{T["law"]}</p>
{city_table}
{S.faq_html(faqs, f"Pest control in {dn}: questions")}
<h2>Pest control services in {dn}</h2>
<p>{SVC_INTRO[vi].format(dn=dn, B=S.BRAND)}</p>
{svc_cards()}
<h2>Nearby states</h2>
<ul class="pills">{pills}</ul>
</div></div>
{S.call_band(f"Pest control in {dn}", f"Call to reach a licensed provider who serves your {dn} city or county.")}'''

    lead = T["intro"]
    hero = S.page_hero(crumbs, f"Pest Control in {dn}", lead, None, "",
                       [(f"{n} cities over 25,000" if n > 1 else "Every town and county") if ab != "DC" else "Every ward and neighborhood", "Licensed local providers", region])

    title = f"Pest Control in {dn} | Exterminators | {S.BRAND}"
    if len(title) > 60:
        title = f"Pest Control in {dn} | {S.BRAND}"
    meta = f"Pest control in {dn} for {pests_lc}. Licensed local exterminators in {', '.join(top[:2]) if ab != 'DC' else 'every ward'} and statewide. Call {S.PHONE_DISPLAY}."
    if ab == "DC":
        meta = meta.replace(" and statewide", "")
    if len(meta) > 155:
        meta = f"Pest control in {dn}: {pests_lc}. Licensed local exterminators. Call {S.PHONE_DISPLAY}."
    if len(meta) > 155:
        meta = f"Pest control in {dn}. Licensed local exterminators in {', '.join(top[:2])} and statewide. Call {S.PHONE_DISPLAY}."

    full = S.BASE + url
    wiki = "https://en.wikipedia.org/wiki/" + WIKI_STATE.get(ab, name.replace(" ", "_"))
    area = {"@type": "State" if ab != "DC" else "City", "name": dn, "sameAs": wiki}
    if ab != "DC":
        area["containsPlace"] = [{"@type": "City", "name": r["name"]} for r in rows[:10]]
    schema = [
        {"@type": "WebPage", "@id": f"{full}#webpage", "url": full, "name": f"Pest Control in {dn}", "isPartOf": {"@id": S.SITE_ID},
         "about": [{"@id": f"{full}#service"}, {"@type": "Thing", "name": "Pest control", "sameAs": "https://en.wikipedia.org/wiki/Pest_control"}],
         "mentions": [{"@type": "Place", "name": dn, "sameAs": wiki}], "dateModified": S.TODAY_ISO, "inLanguage": "en-US",
         "breadcrumb": {"@id": f"{full}#breadcrumb"}},
        {"@type": "Service", "@id": f"{full}#service", "name": f"Pest control in {dn}", "serviceType": "Pest control", "url": full,
         "provider": {"@type": "HomeAndConstructionBusiness", "@id": S.BIZ_ID, "name": S.BRAND, "url": S.BASE + "/", "telephone": S.PHONE_TEL},
         "areaServed": area,
         "availableChannel": {"@type": "ServiceChannel", "servicePhone": {"@type": "ContactPoint", "telephone": S.PHONE_TEL, "contactType": "customer service", "areaServed": "US"}}},
        S.faq_schema(faqs, full),
    ]
    S.page(url, title, meta, hero, body, crumbs=crumbs, schema=schema, priority=0.8, kind="state", word_target=(800, 1600))


def build_states():
    for s in S.SERVICES:
        SVC_NAME[s["slug"]] = s["name"]
    places = load_places()
    for slug, name, ab, reg, pests in STATES:
        state_page(ab, places.get(ab, []))


# ------------------------------------------------------------------ glossary
def slugify(t):
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")


def build_glossary():
    url = "/glossary/"
    crumbs = [("Home", "/"), ("Glossary", url)]
    terms = sorted(TERMS, key=lambda t: t[0].lower())
    letters = sorted({t[0][0].upper() for t in terms})
    jump = " ".join(f'<a href="#letter-{l.lower()}">{l}</a>' for l in letters)
    dl = ""
    cur = ""
    for term, d, best in terms:
        L = term[0].upper()
        if L != cur:
            if cur:
                dl += "</dl>"
            dl += f'<h2 id="letter-{L.lower()}">{L}</h2><dl class="gloss">'
            cur = L
        dl += f'<dt id="{slugify(term)}">{term}</dt><dd>{d} <a href="{best}">Related: {SVC_NAME.get(best.strip("/").split("/")[-1], "guide")}</a></dd>'
    dl += "</dl>"
    hero = S.page_hero(crumbs, "Pest Control Glossary", f"{len(terms)} pest control terms in plain English, from action threshold to yellow jacket.")
    body = f'''<div class="wrap"><div class="content">
<p>Pest control reports, contracts and product labels use a lot of technical words. This glossary explains them simply and links each term to the service page where it matters most. For anything else, browse <a href="/services/">all pest control services</a>.</p>
<p class="pills-jump"><strong>Jump to:</strong> {jump}</p>
{dl}
</div></div>{S.call_band("Have a question about a pest?", "Call to talk it through with a licensed local provider.")}'''
    full = S.BASE + url
    schema = [
        {"@type": "WebPage", "@id": f"{full}#webpage", "url": full, "name": "Pest Control Glossary", "isPartOf": {"@id": S.SITE_ID},
         "mainEntity": {"@id": f"{full}#terms"}, "inLanguage": "en-US"},
        {"@type": "DefinedTermSet", "@id": f"{full}#terms", "name": f"{S.BRAND} Pest Control Glossary",
         "hasDefinedTerm": [{"@type": "DefinedTerm", "@id": f"{full}#{slugify(t)}", "name": t, "description": d,
                             "inDefinedTermSet": {"@id": f"{full}#terms"}, "url": f"{full}#{slugify(t)}"} for t, d, b in terms]},
    ]
    S.page(url, f"Pest Control Glossary: {len(terms)} Terms Explained | {S.BRAND}"[:60] if len(f"Pest Control Glossary: {len(terms)} Terms Explained | {S.BRAND}") <= 60 else "Pest Control Glossary | PestHalt",
           f"Plain-English pest control glossary: {len(terms)} terms from integrated pest management to termite bonds, each linked to the service where it matters.",
           hero, body, crumbs=crumbs, schema=schema, priority=0.6, kind="glossary")


# ------------------------------------------------------------------ glossary auto-links
def autolink(body, page_url, maxn=4):
    """Link the first mention of up to `maxn` glossary terms, inside <p> text only."""
    terms = sorted(TERMS, key=lambda t: -len(t[0]))
    parts = re.split(r"(<[^>]+>)", body)
    in_p = in_a = 0
    done = set()
    used = 0
    for i, part in enumerate(parts):
        if part.startswith("<"):
            tag = part[1:].split()[0].rstrip(">").lower() if len(part) > 1 else ""
            if tag == "p":
                in_p = 1
            elif tag == "/p":
                in_p = 0
            elif tag == "a":
                in_a = 1
            elif tag == "/a":
                in_a = 0
            continue
        if not in_p or in_a or used >= maxn or not part.strip():
            continue
        for term, d, best in terms:
            if used >= maxn:
                break
            if term in done or best == page_url:
                continue
            m = re.search(r"(?<![\w-])(" + re.escape(term) + r")(s?)(?![\w-])", part, flags=re.I)
            if m:
                link = f'<a href="/glossary/#{slugify(term)}">{m.group(1)}{m.group(2)}</a>'
                part = part[:m.start()] + link + part[m.end():]
                done.add(term)
                used += 1
                # don't link inside the link we just made: split off
                break
        parts[i] = part
    return "".join(parts)
