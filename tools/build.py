#!/usr/bin/env python3
"""Build the PestHalt static site into /public.  Usage: python3 tools/build.py"""
import os, sys, shutil, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import core as S
from content.services_a import SERVICES_A, SRC, WIKI
from content.services_b import SERVICES_B, SRC_B
from content.states import STATES
from content import pages, legal, statepages, citypages

SRC.update(SRC_B)
S.SERVICES.extend(SERVICES_A + SERVICES_B)
S.STATE_NAV.extend((slug, name) for slug, name, ab, reg, p in STATES)
S.AUTOLINK = statepages.autolink
for _s in S.SERVICES:
    statepages.SVC_NAME[_s["slug"]] = _s["name"]
for _s in S.SERVICES:
    _sent = citypages.service_city_sentence(_s["slug"])
    if _sent:
        i = _s["local"].rindex("</p>")
        _s["local"] = _s["local"][:i] + _sent + _s["local"][i:]
statepages.CITY_LINKS.update(citypages.built_city_links())

# second, in-content photos per service (hero image is used as background)
SECOND = {
    "termite-inspection": ("home-exterior-2", "Two-story home with a long driveway, the kind of structure inspected for termites"),
    "cockroach-control": ("german-cockroach", "German cockroach feeding on sugar crystals"),
    "ant-control": ("ants-aphids", "Ants tending aphids on a plant stem"),
    "mosquito-control": ("mosquito-bite", "Mosquito feeding on human skin"),
    "wasp-bee-removal": ("yellow-jacket", "Yellow jacket wasp resting on a green leaf"),
    "spider-control": ("spider-web", "Spider web covered in dew drops"),
    "commercial-pest-control": ("housefly", "Close-up of a housefly"),
}


def thing(key):
    name = key.replace("ipm", "Integrated pest management").replace("fifra", "FIFRA")
    url = WIKI[key]
    return {"@type": "Thing", "name": url.rsplit("/", 1)[1].replace("_", " ").replace(",", ","), "sameAs": url}


def render_service(s):
    url = f"/services/{s['slug']}/"
    crumbs = [("Home", "/"), ("Services", "/services/"), (s["name"], url)]
    hero = S.page_hero(crumbs, s["h1"], s["lead"], s.get("image"), s.get("image_alt", ""), s["chips"])
    if not s.get("image"):
        hero = hero.replace('<section class="hero page-hero">', '<section class="hero page-hero">', 1)
    name = s["name"]
    lname = name[0] + name[1:].lower() if name.isupper() else name

    included = "".join(f"<li>{x}</li>" for x in s["included"])
    head = "".join(f"<th>{h}</th>" for h in s["signs_head"])
    rows = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in s["signs"])
    steps = "".join(f"<li><strong>{a}.</strong> {b}</li>" for a, b in s["process"])
    cost = "".join(f"<li>{x}</li>" for x in s["cost"])
    gaps = ""
    for i, (h, c) in enumerate(s["gaps"]):
        gaps += f"<h2>{h}</h2>{c}"
        if i == 0 and len(s["gaps"]) > 1:
            gaps += S.cta_box(f"Need {name.lower()}?", f"Call to reach a licensed local provider for {name.lower()}.")
    if s.get("image") is None and s.get("illus"):
        figure = f'<figure><div class="illus" style="border-radius:12px">{pages.ILLUS[s["illus"]]}</div></figure>'
    else:
        figure = ""
    sec = SECOND.get(s["slug"])
    if sec:
        figure = f'<figure>{S.img(sec[0], sec[1])}<figcaption>{sec[1]}.</figcaption></figure>'
    sources = "".join(f'<li><a href="{SRC[k][1]}" rel="noopener">{SRC[k][0]}</a></li>' for k in s["sources"])
    related = pages.svc_cards(s["related"])
    pills = "".join(f'<li><a href="/locations/{slug}/">{s["nav"].capitalize()} in {nm}</a></li>' for slug, nm, ab, reg, p in STATES)
    illus_hero = ""

    body = f'''<div class="wrap"><div class="content">
<p class="quick">{s["quick"]}</p>
{figure}
<h2>What's included in {name.lower()}</h2>
<ul class="checklist cols2">{included}</ul>
<h2>{s["signs_title"]}</h2>
<div class="tbl-wrap"><table class="tbl"><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table></div>
{S.cta_box("Spotted these signs?", f"Call {S.PHONE_DISPLAY} to reach a licensed provider for {name.lower()} near you.")}
<h2>How {name.lower()} works, step by step</h2>
<ol class="steps">{steps}</ol>
{gaps}
<h2>What affects the cost of {name.lower()}</h2>
<ul class="checklist">{cost}</ul>
<p>{s["cost_note"] if s.get("cost_note") else f"Before any {name.lower()} work begins, get a written estimate covering {s['cost'][0][0].lower() + s['cost'][0][1:].split(',')[0]}, the method, visits and guarantee."}</p>
<h2>DIY vs. calling a professional</h2>
{s["diy"]}
<h2>Licensing and legal notes</h2>
{s["legal"]}
{s["local"]}
{S.cta_box(f"Ready to book {name.lower()}?", "One call connects you with a state-licensed local provider.")}
{S.faq_html(s["faqs"], f"{name} questions")}
<h2>Sources</h2>
<ul class="sources">{sources}</ul>
<p class="reviewed">Last reviewed {S.TODAY_LONG}. General information only, not professional advice.</p><p class="reviewed" style="border:0;padding-top:0">How we write: <a href="/editorial-policy/">editorial policy</a>.</p>
<h2>Related pest control services</h2>
{related}
<h2>{name} near you</h2>
<ul class="pills">{pills}</ul>
</div></div>
{S.call_band(f"Get {name.lower()} help today", f"Call to reach a licensed local provider for {name.lower()}.")}'''

    full = S.BASE + url
    schema = [
        {"@type": "WebPage", "@id": f"{full}#webpage", "url": full, "name": s["h1"], "isPartOf": {"@id": S.SITE_ID},
         "about": [{"@id": f"{full}#service"}, thing(s["about"])], "mentions": [thing(m) for m in s["mentions"]],
         "citation": [SRC[k][1] for k in s["sources"]], "dateModified": S.TODAY_ISO, "inLanguage": "en-US",
         "breadcrumb": {"@id": f"{full}#breadcrumb"}},
        {"@type": "Service", "@id": f"{full}#service", "name": name, "serviceType": name, "url": full,
         "description": s["meta"].replace(f" Call {S.PHONE_DISPLAY}.", ""),
         "provider": {"@type": "HomeAndConstructionBusiness", "@id": S.BIZ_ID, "name": S.BRAND, "url": S.BASE + "/", "telephone": S.PHONE_TEL},
         "areaServed": {"@type": "Country", "name": "United States", "sameAs": "https://en.wikipedia.org/wiki/United_States"},
         "availableChannel": {"@type": "ServiceChannel", "servicePhone": {"@type": "ContactPoint", "telephone": S.PHONE_TEL, "contactType": "customer service", "areaServed": "US"}}},
        S.faq_schema(s["faqs"], full),
    ]
    og = s.get("image") or "indoor-treatment"
    S.page(url, s["title"], s["meta"], hero, body, crumbs=crumbs, schema=schema, priority=0.9, kind="service", og_image=og,
           word_target=(1000, 1600))


def icons():
    pub = S.OUT
    svg = S.LOGO_SVG.replace('width="34" height="34"', 'width="48" height="48" xmlns="http://www.w3.org/2000/svg"')
    open(os.path.join(pub, "favicon.svg"), "w").write(svg)
    try:
        from PIL import Image
        import cairosvg  # noqa
    except Exception:
        pass
    for size, name in [(32, "favicon-32.png"), (180, "apple-touch-icon.png"), (192, "icon-192.png"), (512, "assets/logo-512.png")]:
        out = os.path.join(pub, name)
        subprocess.run(["convert", "-background", "none", "-density", "600", os.path.join(pub, "favicon.svg"),
                        "-resize", f"{size}x{size}", out], check=True)


def main():
    keep = os.path.join(S.OUT, "assets", "img")
    for item in os.listdir(S.OUT) if os.path.isdir(S.OUT) else []:
        p = os.path.join(S.OUT, item)
        if item == "assets":
            for sub in os.listdir(p):
                if sub != "img":
                    sp = os.path.join(p, sub)
                    shutil.rmtree(sp) if os.path.isdir(sp) else os.remove(sp)
            continue
        shutil.rmtree(p) if os.path.isdir(p) else os.remove(p)
    pages.build_home()
    pages.build_services_hub()
    for s in S.SERVICES:
        render_service(s)
    pages.build_locations_hub()
    statepages.build_states()
    statepages.build_glossary()
    citypages.build_cities()
    pages.build_about()
    pages.build_contact()
    legal.build_legal()
    pages.build_404()
    S.write_all()
    icons()
    print(f"Built {len(S.PAGES)} pages into {S.OUT}")


if __name__ == "__main__":
    main()
