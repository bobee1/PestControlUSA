"""Home, hubs, about, contact pages."""

import core as S
from content.states import STATES, REGIONS


def svc_cards(slugs=None):
    items = [S.svc(x) for x in slugs] if slugs else S.SERVICES
    out = []
    for s in items:
        if s.get("image"):
            pic = S.img(s["image"], s["image_alt"], w=600, h=400, sizes="(max-width: 760px) 100vw, 360px")
        else:
            pic = f'<div class="illus">{ILLUS[s["illus"]]}</div>'
        out.append(f'<article class="card svc-card">{pic}<div class="in"><h3><a href="/services/{s["slug"]}/">{s["name"]}</a></h3><p>{s["card"]}</p></div></article>')
    return '<div class="grid g3">' + "".join(out) + "</div>"


ILLUS = {
 "bedbug": '<svg width="220" height="150" viewBox="0 0 220 150" role="img" aria-label="Illustration of a bed bug"><ellipse cx="110" cy="82" rx="46" ry="38" fill="#8a3b1e"/><ellipse cx="110" cy="82" rx="38" ry="31" fill="#a44a26"/><path d="M80 70h60M76 84h68M82 98h56" stroke="#6e2c14" stroke-width="3" fill="none"/><ellipse cx="110" cy="40" rx="16" ry="11" fill="#7a3319"/><path d="M98 33 86 18M122 33l12-15" stroke="#4a1f0e" stroke-width="3" stroke-linecap="round"/><path d="M68 66 42 52M66 84H36M70 102l-26 16M152 66l26-14M154 84h30M150 102l26 16" stroke="#4a1f0e" stroke-width="4" stroke-linecap="round"/></svg>',
 "flea": '<svg width="220" height="150" viewBox="0 0 220 150" role="img" aria-label="Illustration of a flea and a tick"><g transform="translate(20 20)"><ellipse cx="45" cy="62" rx="30" ry="40" fill="#5b3a1f" transform="rotate(-20 45 62)"/><circle cx="62" cy="22" r="10" fill="#4a2e17"/><path d="M30 92 8 118M44 98l-4 30M58 92l18 26" stroke="#3a2412" stroke-width="5" stroke-linecap="round"/></g><g transform="translate(118 30)"><ellipse cx="42" cy="52" rx="34" ry="38" fill="#7a2e1c"/><ellipse cx="42" cy="40" rx="20" ry="18" fill="#a25a30"/><path d="M42 14V2" stroke="#3a1a10" stroke-width="5" stroke-linecap="round"/><path d="M10 40H-8M8 58-10 66M10 74-4 88M74 40h18M76 58l18 8M74 74l14 14" stroke="#3a1a10" stroke-width="4" stroke-linecap="round"/></g></svg>',
 "raccoon": '<svg width="220" height="150" viewBox="0 0 220 150" role="img" aria-label="Illustration of a raccoon"><ellipse cx="110" cy="104" rx="62" ry="34" fill="#7d7d76"/><path d="M160 108c26-2 42 10 46 26" stroke="#4b4b46" stroke-width="16" stroke-linecap="round" fill="none"/><path d="M178 112l-4 22M194 118l-6 18" stroke="#d9d9d2" stroke-width="5"/><circle cx="96" cy="62" r="34" fill="#9a9a92"/><path d="M68 38 64 16l20 12M124 38l4-22-20 12" fill="#6b6b64"/><path d="M66 60c10-10 50-10 60 0-6 10-14 12-30 12s-24-2-30-12z" fill="#2d2d2a"/><circle cx="82" cy="61" r="4" fill="#fff"/><circle cx="110" cy="61" r="4" fill="#fff"/><ellipse cx="96" cy="80" rx="12" ry="8" fill="#e8e8e1"/><circle cx="96" cy="76" r="4" fill="#1f1f1d"/></svg>',
}


# ---------------------------------------------------------------- HOME
def build_home():
    crumbs = None
    regions_html = ""
    for r in REGIONS:
        names = ", ".join(f'<a href="/locations/{sl}/">{n}</a>' for sl, n, _, reg, _ in STATES if reg == r)
        regions_html += f"<li><strong>{r}:</strong> {names}</li>"
    hero = f'''<section class="hero"><div class="bg">{S.img("home-hero", "Two-story suburban home with a front lawn at dusk", eager=True, sizes="100vw")}</div><div class="wrap">
<h1>Pest Control Near You, in All 50 States</h1>
<p class="lead">Termites, mice, roaches, bed bugs or wasps: call {S.BRAND} to reach a state-licensed local pest control provider who can inspect your home and treat the problem at its source.</p>
<div class="hero-ctas">{S.phone_link()}<a class="btn btn-ghost" href="/services/">See all services</a></div>
<ul class="chips"><li>{S.icon("pin",16)}All 50 states + DC</li><li>{S.icon("home",16)}Homes, apartments &amp; businesses</li><li>{S.icon("shield",16)}State-licensed local providers</li><li>{S.icon("leaf",16)}IPM-based treatment</li></ul>
</div></section>'''

    faqs = [
        ("How do I find pest control near me?", f"Call {S.PHONE_DISPLAY}. {S.BRAND} connects you with a state-licensed pest control provider who serves your city or county, so you skip the search and the round of callbacks."),
        ("How much does pest control cost?", "Prices depend on the pest, the size of the home, how established the problem is, the treatment method and whether you choose a one-time visit or a recurring plan. Get a written estimate after an inspection before any work begins."),
        ("What pests do you help with?", "General household insects such as ants, roaches and spiders, plus termites, rodents, bed bugs, mosquitoes, wasps and bees, fleas and ticks, wildlife and commercial pest programs."),
        ("Are pest control treatments safe for kids and pets?", "Registered products applied according to the label are designed to be low risk once dry. Providers following integrated pest management favor baits, traps and targeted crack-and-crevice treatments indoors. Tell the technician about children, pets and anyone with health concerns."),
        ("How quickly can someone come out?", "Scheduling depends on the provider in your area and the time of year. When you call, explain how urgent the problem is, such as stinging insects near a door or rodents in a kitchen, so it can be prioritized."),
        ("Is the pest control provider licensed?", "Pest control is a licensed trade in every state. Providers in our network hold the license their state requires, and you can verify any license number with your state pest control regulator."),
        ("Do I need a recurring plan or a one-time treatment?", "One-time visits suit a single problem like a wasp nest. Ants, roaches and spiders tend to return from outside, so quarterly plans are common. Termites and bed bugs follow their own treatment programs."),
        ("What should I do before the technician arrives?", "Note where and when you see pests, keep pets secured, clear access to sinks, the garage, attic and crawl space, and do not spray store products right before an inspection, which can hide activity."),
    ]
    signs = ["Droppings in cabinets, drawers or along baseboards", "Mud tubes on the foundation or discarded insect wings on windowsills",
             "Scratching or scurrying in walls or the attic at night", "Rusty spots on mattress seams or unexplained bites after sleeping",
             "Ant trails that return every day", "Cockroaches seen in daylight", "Gnawed wires, food packaging or wood", "Wasps flying in and out of a gap in siding or the ground"]
    body = f'''
<div class="wrap"><div class="content">
<p class="quick"><strong>Pest control, one call away:</strong> {S.BRAND} helps homeowners, renters and businesses across the United States find pest control fast. Call {S.PHONE_DISPLAY} and you're connected with a licensed local pest control provider who inspects, identifies the pest and recommends treatment that targets the source rather than the symptoms.</p>
<p>Pest problems rarely fix themselves. A few ants become a trail, one mouse becomes a nest in the insulation, and termites can work for years before anyone notices. Searching for "pest control near me" usually means calling several companies, waiting for callbacks and comparing quotes you can't easily judge. {S.BRAND} shortens that. We cover thirteen pest control services, from <a href="/services/general-pest-control/">general pest control plans</a> to <a href="/services/termite-control/">termite treatment</a> and <a href="/services/commercial-pest-control/">commercial programs</a>, in every state and the District of Columbia.</p>

<h2>Pest control services</h2>
<p>Every pest has its own biology, so every service on this list follows its own method. Choose a service to learn how professionals handle it, what it costs to fix, and when it's worth calling.</p>
{svc_cards()}

<h2>How {S.BRAND} works</h2>
<div class="grid g3 steps-row">
<div class="card step-card"><span class="num">1</span><h3>Call and describe the problem</h3><p>Tell us what you're seeing, where, and for how long. Photos and notes about droppings, damage or bites help.</p></div>
<div class="card step-card"><span class="num">2</span><h3>Get connected locally</h3><p>Your call goes to a state-licensed pest control provider who serves your area and handles your pest.</p></div>
<div class="card step-card"><span class="num">3</span><h3>Inspection and a written plan</h3><p>The provider inspects, identifies the pest, explains the treatment and gives you pricing before work starts.</p></div>
</div>
<p>{S.BRAND} does not apply pesticides itself. The provider you're connected with is responsible for the inspection, treatment, pricing and guarantee. Read <a href="/about/">how {S.BRAND} works</a> for details.</p>

{S.cta_box("Seeing pests right now?", "Call to reach a licensed pest control provider near you.")}

<h2>Pest control near you, across the United States</h2>
<p>Pest pressure is local. Formosan termites swarm along the Gulf Coast in spring, bark scorpions hide in Arizona block walls, brown recluse spiders fill storage rooms in Missouri and Oklahoma, and Northeast homes fight mice and blacklegged ticks. A provider who works in your area knows the local species, the season and the building styles that let pests in, which is why local expertise matters more than a national logo.</p>
<p>Whether you're in a high-rise apartment, a farmhouse, a ranch-style home on a slab or a restaurant kitchen, the goal is the same: find where pests are getting in and what's feeding them, treat them where they live, and keep them out.</p>

<h2>What professional pest control looks like</h2>
<ol class="steps">
<li><strong>Inspection.</strong> A licensed technician checks inside and out for activity, entry points and conditions such as leaks, clutter or mulch against siding.</li>
<li><strong>Identification.</strong> The correct species decides the method. Pharaoh ants, German cockroaches and drywood termites each need a different approach.</li>
<li><strong>Targeted treatment.</strong> Following <a href="https://www.epa.gov/ipm" rel="noopener">integrated pest management</a>, products go where pests live: baits, crack-and-crevice treatments, soil barriers or traps.</li>
<li><strong>Exclusion and prevention.</strong> Sealing gaps, fixing moisture and adjusting storage keep new pests out.</li>
<li><strong>Follow-up.</strong> Monitoring and return visits confirm the problem is solved.</li>
</ol>

<h2>Areas served</h2>
<p>{S.BRAND} connects callers with local providers in all 50 states and Washington, D.C., from large metro areas to small towns and rural counties.</p>
<ul>{regions_html}</ul>
<p>Visit the <a href="/locations/">pest control locations page</a> to see the most common pests in each state.</p>

<h2>What affects the cost of pest control</h2>
<ul class="checklist">
<li>The pest: termites, bed bugs and wildlife usually cost more than ants or spiders</li>
<li>How established the infestation is and how many rooms or units are affected</li>
<li>Home size, foundation type, and access to crawl spaces and attics</li>
<li>Treatment method, such as bait stations versus liquid barriers or heat versus chemical</li>
<li>One-time service versus a recurring plan with re-service included</li>
<li>Exclusion repairs, cleanup and warranties</li>
</ul>
<p>Ask for a written estimate that lists the pests covered, products and methods, the number of visits and any guarantee before you agree to service. The <a href="https://www.epa.gov/safepestcontrol/tips-selecting-pest-control-service" rel="noopener">EPA advises</a> that cost should not be the only factor when choosing a pest control service.</p>

<h2>Warning signs you need an exterminator</h2>
<ul class="checklist cols2">{"".join(f"<li>{x}</li>" for x in signs)}</ul>
<p>Spotting any of these more than once is a good reason to call. Early treatment is usually simpler and less expensive than dealing with an established colony, nest or infestation.</p>

<h2>Choosing a pest control company</h2>
<p>Whoever you hire, a few checks protect you. Confirm the company holds the license your state requires. Ask which products they'll use and request the labels. Make sure the estimate is in writing, and understand what the guarantee covers. The <a href="https://www.npic.orst.edu/pest/selectpco.html" rel="noopener">National Pesticide Information Center</a> recommends asking for references and checking your state pesticide regulatory office for complaints. Every provider in the {S.BRAND} network is expected to meet these basics.</p>

{S.faq_html(faqs, "Pest control questions")}
</div></div>
{S.call_band("Ready to get rid of pests?", "Call to reach a licensed local pest control provider in your area.")}
'''
    schema = S.org_nodes() + [
        {"@type": "HomeAndConstructionBusiness", "@id": S.BIZ_ID, "name": S.BRAND, "url": S.BASE + "/",
         "telephone": S.PHONE_TEL, "image": f"{S.BASE}/assets/img/home-hero-1200.webp", "parentOrganization": {"@id": S.ORG_ID},
         "description": f"{S.BRAND} is a pest control referral and scheduling service that connects callers with state-licensed local pest control providers across the United States.",
         "areaServed": {"@type": "Country", "name": "United States", "sameAs": "https://en.wikipedia.org/wiki/United_States"},
         "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Pest control services",
                             "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "@id": f"{S.BASE}/services/{s['slug']}/#service", "name": s["name"]}} for s in S.SERVICES]}},
        {"@type": "WebPage", "@id": f"{S.BASE}/#webpage", "url": S.BASE + "/", "name": "Pest Control Near Me", "isPartOf": {"@id": S.SITE_ID},
         "about": [{"@id": S.BIZ_ID}, {"@type": "Thing", "name": "Pest control", "sameAs": "https://en.wikipedia.org/wiki/Pest_control"}],
         "mentions": [{"@type": "Thing", "name": "Integrated pest management", "sameAs": "https://en.wikipedia.org/wiki/Integrated_pest_management"},
                      {"@type": "Thing", "name": "Termite", "sameAs": "https://en.wikipedia.org/wiki/Termite"},
                      {"@type": "Thing", "name": "Bed bug", "sameAs": "https://en.wikipedia.org/wiki/Bed_bug"},
                      {"@type": "Country", "name": "United States", "sameAs": "https://en.wikipedia.org/wiki/United_States"}],
         "inLanguage": "en-US", "dateModified": S.TODAY_ISO},
        S.faq_schema(faqs, S.BASE + "/"),
    ]
    S.page("/", "Pest Control Near Me | Local Exterminators | PestHalt",
           "Pest control near you in all 50 states. Call (800) 555-0199 to reach a licensed local exterminator for termites, rodents, roaches, bed bugs and more.",
           hero, body, schema=schema, priority=1.0, kind="home", word_target=(1200, 1800))


# ---------------------------------------------------------------- SERVICES HUB
def build_services_hub():
    crumbs = [("Home", "/"), ("Services", "/services/")]
    hero = S.page_hero(crumbs, "Pest Control Services", "Thirteen pest control services, each built around how the pest actually lives, from quarterly plans to termite treatment and commercial programs.", "indoor-treatment", "Technician in protective gear treating a room with a hand sprayer", ["All 50 states + DC", "Residential & commercial", "State-licensed local providers"])
    body = f'''<div class="wrap"><div class="content">
<p>Whether you need a single wasp nest removed or a long-term termite warranty, the right method depends on the pest. Pest control companies often bundle services differently, so this page lays out each one on its own: what's included, how it works and what affects the price. Call {S.PHONE_DISPLAY} and {S.BRAND} will connect you with a licensed provider for any of them.</p>
<h2>Residential and commercial pest control services</h2>
{svc_cards()}
<h2>Choosing the right pest control service</h2>
<div class="tbl-wrap"><table class="tbl"><thead><tr><th>If you're seeing...</th><th>Start with</th></tr></thead><tbody>
<tr><td>Ants, spiders, silverfish or occasional roaches</td><td><a href="/services/general-pest-control/">General pest control</a></td></tr>
<tr><td>Mud tubes, swarmers or hollow wood</td><td><a href="/services/termite-control/">Termite control</a> or a <a href="/services/termite-inspection/">termite inspection</a></td></tr>
<tr><td>Droppings, gnawing or noises in walls</td><td><a href="/services/rodent-control/">Rodent control</a></td></tr>
<tr><td>Bites after sleeping and rusty spots on sheets</td><td><a href="/services/bed-bug-treatment/">Bed bug treatment</a></td></tr>
<tr><td>Roaches in daylight or in the kitchen</td><td><a href="/services/cockroach-control/">Cockroach control</a></td></tr>
<tr><td>Ant trails, sawdust-like frass or fire ant mounds</td><td><a href="/services/ant-control/">Ant control</a></td></tr>
<tr><td>Biting insects in the yard</td><td><a href="/services/mosquito-control/">Mosquito control</a> or <a href="/services/flea-tick-control/">flea and tick control</a></td></tr>
<tr><td>Wasps, hornets or a bee swarm</td><td><a href="/services/wasp-bee-removal/">Wasp and bee removal</a></td></tr>
<tr><td>Webs, widows or recluse spiders</td><td><a href="/services/spider-control/">Spider control</a></td></tr>
<tr><td>Animals in the attic, chimney or crawl space</td><td><a href="/services/wildlife-removal/">Wildlife removal</a></td></tr>
<tr><td>Pests in a restaurant, warehouse or office</td><td><a href="/services/commercial-pest-control/">Commercial pest control</a></td></tr>
</tbody></table></div>
<h2>How pest control companies approach treatment</h2>
<p>Most reputable pest control companies follow integrated pest management (IPM): inspect, identify, set a threshold for action, fix the conditions that attract pests, and use the lowest-risk effective treatment. That approach is why you'll often see baits and traps instead of broad spraying, and why the provider will point out leaks, gaps and clutter. Learn more on each service page or <a href="/contact/">contact {S.BRAND}</a> with questions.</p>
</div></div>{S.call_band("Not sure which service you need?", "Describe the problem on the phone and get matched with the right licensed provider.")}'''
    schema = [{"@type": "CollectionPage", "@id": f"{S.BASE}/services/#webpage", "url": f"{S.BASE}/services/", "name": "Pest Control Services",
               "isPartOf": {"@id": S.SITE_ID}, "about": {"@type": "Thing", "name": "Pest control", "sameAs": "https://en.wikipedia.org/wiki/Pest_control"},
               "hasPart": [{"@type": "WebPage", "url": f"{S.BASE}/services/{s['slug']}/", "name": s["name"]} for s in S.SERVICES]}]
    S.page("/services/", "Pest Control Services & Exterminators | PestHalt",
           "All pest control services in one place: general pest plans, termites, rodents, bed bugs, roaches, ants, mosquitoes, wildlife and commercial programs.",
           hero, body, crumbs=crumbs, schema=schema, priority=0.8, kind="hub", og_image="indoor-treatment")


# ---------------------------------------------------------------- LOCATIONS HUB
def build_locations_hub():
    crumbs = [("Home", "/"), ("Locations", "/locations/")]
    hero = S.page_hero(crumbs, "Pest Control Locations: All 50 States", f"{S.BRAND} connects callers with licensed pest control providers in every state and Washington, D.C. Choose your state to see local pests, licensing and every city over 25,000 people we serve.", "locations-hub", "Modern suburban home with a lawn and wet driveway at dusk", ["All 50 states + DC", "Cities, towns & rural areas"])
    blocks = ""
    for r in REGIONS:
        cards = "".join(f'<div class="state" id="{slug}"><a href="/locations/{slug}/"><strong>Pest control in {name}</strong></a><span>{pests}</span></div>'
                        for slug, name, ab, reg, pests in STATES if reg == r)
        blocks += f"<h2>Pest control in the {r}</h2><div class=\"state-grid\">{cards}</div>"
    body = f'''<div class="wrap"><div class="content">
<p>Pest control needs change from state to state. Climate, humidity, soil, building styles and local species decide which pests you're most likely to face and when. Choose your state below for local pests, licensing rules and the cities we serve, or call {S.PHONE_DISPLAY} to reach a licensed pest control provider who serves your city or county.</p>
<p class="quick"><strong>Licensing note:</strong> Each state licenses pest control applicators through its own agency, usually the department of agriculture or a structural pest control board. Ask for the provider's license number and check it with your state regulator.</p>
{blocks}
<h2>How regional pest pressure differs</h2>
<p>The <strong>South</strong> and Gulf Coast have the longest pest seasons, with subterranean and Formosan termites, fire ants, large outdoor cockroaches and mosquitoes active most of the year. The <strong>West</strong> ranges from drywood termites and roof rats on the coast to scorpions and black widows in the desert. The <strong>Midwest</strong> sees fall rodent invasions, stink bugs and boxelder bugs, with brown recluse spiders in the south-central states. The <strong>Northeast</strong> deals with mice, carpenter ants, bed bugs in dense cities and blacklegged ticks that carry Lyme disease.</p>
<p>Not sure which service you need? Start with the <a href="/services/">pest control services</a> page or <a href="/services/general-pest-control/">general pest control</a>.</p>
</div></div>{S.call_band("Pest control in your state", "Call to reach a licensed provider who serves your city or county.")}'''
    schema = [{"@type": "CollectionPage", "@id": f"{S.BASE}/locations/#webpage", "url": f"{S.BASE}/locations/", "name": "Pest Control Locations",
               "isPartOf": {"@id": S.SITE_ID}, "about": {"@type": "Thing", "name": "Pest control", "sameAs": "https://en.wikipedia.org/wiki/Pest_control"},
               "spatialCoverage": {"@type": "Country", "name": "United States"}}]
    S.page("/locations/", "Pest Control Locations in All 50 States | PestHalt",
           "Pest control locations across all 50 states and DC. See the most common pests in your state and call (800) 555-0199 for a licensed local provider.",
           hero, body, crumbs=crumbs, schema=schema, priority=0.8, kind="hub", og_image="locations-hub")


# ---------------------------------------------------------------- ABOUT
def build_about():
    crumbs = [("Home", "/"), ("About", "/about/")]
    hero = S.page_hero(crumbs, f"About {S.BRAND}", "A faster way for homeowners and businesses to reach a licensed local pest control provider, anywhere in the United States.", "about", "Two-story home with lights on at dusk")
    body = f'''<div class="wrap"><div class="content narrow" style="max-width:860px">
<h2>What {S.BRAND} is</h2>
<p>{S.BRAND} is a pest control referral and scheduling service founded by {S.OWNER}. We built it for a simple reason: when you have termites in a door frame or mice in the pantry, you want a qualified local professional, not an afternoon of searching, voicemail and comparing quotes you can't easily judge.</p>
<p>When you call {S.PHONE_DISPLAY}, your call is connected to an independent, state-licensed pest control provider who serves your area and handles the pest you describe. That provider inspects your property, explains the options and gives you pricing. You decide whether to go ahead.</p>
<h2>What {S.BRAND} does not do</h2>
<p>{S.BRAND} does not apply pesticides, set traps or perform treatments. Pest control is a licensed trade in every state, and the work is done by the providers in our network, who are responsible for their own licenses, insurance, pricing, guarantees and workmanship. We may be compensated when a call is connected. Our <a href="/disclaimer/">disclaimer</a> explains this in full.</p>
<h2>How we write this website</h2>
<p>The guides on {S.BRAND} explain how each pest control service works, using public sources such as the U.S. Environmental Protection Agency, the Centers for Disease Control and Prevention, the National Pesticide Information Center and university extension programs. We cite sources on every service page and review pages on a regular schedule. Read our <a href="/editorial-policy/">editorial policy</a> for how content is researched, reviewed and corrected.</p>
<h2>Our standards for providers</h2>
<ul class="checklist">
<li>Hold the pest control license their state requires for the work performed</li>
<li>Inspect before treating and explain findings in plain language</li>
<li>Give written pricing before starting work</li>
<li>Use EPA-registered products according to the label</li>
<li>Follow integrated pest management practices that favor targeted treatment</li>
</ul>
<p>If a provider falls short of these standards, <a href="/contact/">tell us</a>.</p>
<h2>Where we help</h2>
<p>{S.BRAND} connects callers in all 50 states and Washington, D.C. See the <a href="/locations/">locations page</a> for pests common in each state and the <a href="/services/">services page</a> for everything we cover.</p>
</div></div>{S.call_band("Talk to a pest control provider", "One call connects you with a state-licensed provider near you.")}'''
    schema = [{"@type": "AboutPage", "@id": f"{S.BASE}/about/#webpage", "url": f"{S.BASE}/about/", "name": f"About {S.BRAND}", "isPartOf": {"@id": S.SITE_ID}, "about": {"@id": S.ORG_ID}}] + S.org_nodes()[:1]
    S.page("/about/", f"About {S.BRAND} | How Our Pest Control Network Works",
           f"About {S.BRAND}: a pest control referral service that connects callers in all 50 states with state-licensed local pest control providers.",
           hero, body, crumbs=crumbs, schema=schema, priority=0.5, og_image="about")


# ---------------------------------------------------------------- CONTACT
def build_contact():
    crumbs = [("Home", "/"), ("Contact", "/contact/")]
    hero = S.page_hero(crumbs, f"Contact {S.BRAND}", f"The fastest way to get help is to call {S.PHONE_DISPLAY}. You can also send a request using the form below.", "contact", "Large suburban home with a wide front lawn")
    opts = "".join(f"<option>{s['name']}</option>" for s in S.SERVICES)
    states = "".join(f"<option>{n}</option>" for _, n, _, _, _ in STATES)
    body = f'''<div class="wrap"><div class="content">
<div class="grid g2">
<div>
<h2>Call for pest control help</h2>
<p>Calling is the quickest way to reach a licensed pest control provider who serves your area.</p>
<p>{S.phone_link("btn btn-call", f"Call {S.PHONE_DISPLAY}")}</p>
<p>When you call, be ready to share:</p>
<ul class="checklist"><li>Your ZIP code or city</li><li>The pest you're seeing and where</li><li>How long it has been going on</li><li>Whether it's a home, rental or business</li></ul>
<p>Questions about this website, our <a href="/privacy-policy/">privacy policy</a> or a provider experience? Use the form and choose "Other".</p>
</div>
<div>
<h2>Request a callback</h2>
<form id="lead-form" class="form" novalidate>
<label for="f-name">Name</label><input id="f-name" name="name" autocomplete="name" required>
<label for="f-phone">Phone</label><input id="f-phone" name="phone" type="tel" autocomplete="tel" required>
<label for="f-zip">ZIP code</label><input id="f-zip" name="zip" inputmode="numeric" autocomplete="postal-code" maxlength="10" required>
<label for="f-state">State</label><select id="f-state" name="state"><option value="">Select your state</option>{states}</select>
<label for="f-service">Service needed</label><select id="f-service" name="service">{opts}<option>Other</option></select>
<label for="f-msg">What are you seeing?</label><textarea id="f-msg" name="message" rows="4"></textarea>
<div class="hp" aria-hidden="true"><label for="f-web">Website</label><input id="f-web" name="website" tabindex="-1" autocomplete="off"></div>
<p class="form-note">By submitting, you agree that {S.BRAND} and a pest control provider serving your area may contact you at the number provided about your request, including by call or text. Consent is not a condition of purchase. Message and data rates may apply. See our <a href="/privacy-policy/">privacy policy</a>.</p>
<button class="btn btn-call" type="submit">Send request</button>
<p class="form-msg" role="status" aria-live="polite"></p>
</form>
</div></div>
</div></div>{S.call_band("Prefer to talk it through?", "Calling is the fastest way to reach a licensed provider in your area.")}'''
    schema = [{"@type": "ContactPage", "@id": f"{S.BASE}/contact/#webpage", "url": f"{S.BASE}/contact/", "name": f"Contact {S.BRAND}", "isPartOf": {"@id": S.SITE_ID},
               "about": {"@id": S.ORG_ID}}]
    S.page("/contact/", f"Contact {S.BRAND} | Pest Control Help (800) 555-0199",
           f"Contact {S.BRAND} for pest control help. Call (800) 555-0199 or send a callback request to reach a licensed local pest control provider.",
           hero, body, crumbs=crumbs, schema=schema, priority=0.5, og_image="contact")


def build_404():
    hero = f'<section class="hero page-hero"><div class="wrap"><h1>Page not found</h1><p class="lead">The page you were looking for has moved or does not exist.</p><div class="hero-ctas">{S.phone_link()}</div></div></section>'
    body = f'''<div class="wrap"><div class="content"><h2>Try one of these</h2><ul><li><a href="/">{S.BRAND} home</a></li><li><a href="/services/">All pest control services</a></li><li><a href="/locations/">Pest control locations</a></li><li><a href="/contact/">Contact {S.BRAND}</a></li></ul></div></div>'''
    S.page("/404/", f"Page Not Found | {S.BRAND}", "The page you requested could not be found. Browse pest control services or call (800) 555-0199.", hero, body, noindex=True, priority=0.1)
