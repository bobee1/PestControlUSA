"""PestHalt static site framework: config, layout, schema helpers, writers.

Build: python3 tools/build.py  -> writes the static site into /public
"""
import json, os, re, html, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "public")

BRAND = "PestHalt"
DOMAIN = "pesthalt.us"
BASE = f"https://{DOMAIN}"
PHONE_DISPLAY = "(800) 555-0199"
PHONE_TEL = "+18005550199"
OWNER = "Anjam Javed"
TODAY = datetime.date(2026, 11, 26)
TODAY_ISO = TODAY.isoformat()
TODAY_LONG = TODAY.strftime("%B %-d, %Y")
ORG_ID = f"{BASE}/#organization"
BIZ_ID = f"{BASE}/#business"
SITE_ID = f"{BASE}/#website"

DISCLOSURE = (f"<strong>Service disclosure:</strong> {BRAND} is a pest control referral and scheduling service. "
              f"{BRAND} does not apply pesticides itself. Inspections and treatments are performed by independent, "
              "state-licensed pest control providers, who are responsible for their own licenses, insurance, pricing and work. "
              f"Calls may be recorded for quality and training, and {BRAND} may be compensated when a call is connected. "
              '<a href="/disclaimer/">Read the full disclaimer</a>.')

# --------------------------------------------------------------- icons
ICONS = {
 "phone": '<path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1A17 17 0 0 1 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1z"/>',
 "check": '<path d="M9 16.2 4.8 12l-1.4 1.4L9 19 21 7l-1.4-1.4z"/>',
 "shield": '<path d="M12 2 4 5v6c0 5 3.4 9.7 8 11 4.6-1.3 8-6 8-11V5z"/>',
 "pin": '<path d="M12 2a7 7 0 0 0-7 7c0 5.3 7 13 7 13s7-7.7 7-13a7 7 0 0 0-7-7zm0 9.5A2.5 2.5 0 1 1 12 6.5a2.5 2.5 0 0 1 0 5z"/>',
 "home": '<path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z"/>',
 "building": '<path d="M3 21V3h12v4h6v14h-8v-4h-2v4zm2-2h2v-2H5zm0-4h2v-2H5zm0-4h2V9H5zm0-4h2V5H5zm4 8h2v-2H9zm0-4h2V9H9zm0-4h2V5H9zm6 8h2v-2h-2zm0-4h2V9h-2z"/>',
 "search": '<path d="M15.5 14h-.8l-.3-.3a6.5 6.5 0 1 0-.7.7l.3.3v.8l5 5 1.5-1.5zm-6 0a4.5 4.5 0 1 1 0-9 4.5 4.5 0 0 1 0 9z"/>',
 "clipboard": '<path d="M19 3h-4.2A3 3 0 0 0 12 1a3 3 0 0 0-2.8 2H5a2 2 0 0 0-2 2v14c0 1.1.9 2 2 2h14a2 2 0 0 0 2-2V5a2 2 0 0 0-2-2zm-7 0a1 1 0 1 1 0 2 1 1 0 0 1 0-2zm-2 14-4-4 1.4-1.4L10 14.2l6.6-6.6L18 9z"/>',
 "leaf": '<path d="M17 8C8 10 5.9 16.2 3.8 21.3l1.9.7.9-2.3c.5.2 1 .3 1.4.3C19 20 22 3 22 3c-1 2-8 2.3-13 3.3S2 11.5 2 13.5 3.8 17.3 3.8 17.3C7 8 17 8 17 8z"/>',
 "clock": '<path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zm.5 11H7v-2h3.5V6h2z"/>',
 "chev": '<path d="M7 10l5 5 5-5z"/>',
}
def icon(name, size=20, cls="ic"):
    return (f'<svg class="{cls}" width="{size}" height="{size}" viewBox="0 0 24 24" aria-hidden="true" '
            f'focusable="false" fill="currentColor">{ICONS[name]}</svg>')

LOGO_SVG = ('<svg width="34" height="34" viewBox="0 0 48 48" aria-hidden="true" focusable="false">'
            '<path d="M24 3 6 10v12c0 11 7.6 20.4 18 23 10.4-2.6 18-12 18-23V10z" fill="#1d6b47"/>'
            '<path d="M24 8.5 11 13.6V22c0 8.3 5.5 15.6 13 17.9 7.5-2.3 13-9.6 13-17.9v-8.4z" fill="#0f2a1e"/>'
            '<rect x="14" y="21" width="20" height="6" rx="3" fill="#f5b301"/>'
            '<circle cx="24" cy="16" r="2.6" fill="#f5b301"/><circle cx="24" cy="32" r="2.6" fill="#f5b301"/></svg>')

# --------------------------------------------------------------- data shared by pages
SERVICES = []   # filled by content.services (list of dicts)
STATE_NAV = []  # (slug, name) filled by build
AUTOLINK = None  # glossary auto-link hook set by build

def svc(slug):
    for s in SERVICES:
        if s["slug"] == slug:
            return s
    raise KeyError(slug)

def phone_link(cls="btn btn-call", label=None):
    label = label or f"Call {PHONE_DISPLAY}"
    return f'<a class="{cls}" href="tel:{PHONE_TEL}">{icon("phone",18)}<span>{label}</span></a>'

def img(name, alt, w=1200, h=800, eager=False, cls="", sizes="(max-width: 760px) 100vw, 720px"):
    loading = 'fetchpriority="high" decoding="async"' if eager else 'loading="lazy" decoding="async"'
    return (f'<img class="{cls}" src="/assets/img/{name}-1200.webp" '
            f'srcset="/assets/img/{name}-600.webp 600w, /assets/img/{name}-1200.webp 1200w" sizes="{sizes}" '
            f'width="{w}" height="{h}" alt="{html.escape(alt)}" {loading}>')

def cta_box(title, text):
    return (f'<aside class="cta-box"><div><p class="cta-title">{title}</p><p>{text}</p></div>'
            f'{phone_link()}</aside>')

# --------------------------------------------------------------- CSS / JS
CSS = """
:root{--ink:#0f2a1e;--ink2:#1c3a2d;--brand:#1d6b47;--brand2:#155238;--amber:#f5b301;--amber2:#ffcd3c;--bg:#f5f7f2;--card:#fff;--line:#dfe6da;--muted:#4a5a51;--radius:14px;--shadow:0 6px 24px rgba(15,42,30,.08)}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%;scroll-behavior:smooth}body{margin:0;font:17px/1.65 system-ui,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;color:var(--ink);background:var(--bg)}
img{max-width:100%;height:auto;display:block}a{color:var(--brand2);text-underline-offset:2px}a:hover{color:var(--ink)}
.skip{position:absolute;left:-999px;top:8px;background:#fff;padding:8px 12px;z-index:99}.skip:focus{left:8px}
.wrap{max-width:1160px;margin:0 auto;padding:0 20px}.narrow{max-width:820px}
h1,h2,h3{line-height:1.2;color:var(--ink);letter-spacing:-.01em}h1{font-size:clamp(1.9rem,4.2vw,2.9rem);margin:.2em 0 .4em}h2{font-size:clamp(1.45rem,2.8vw,1.95rem);margin:1.8em 0 .6em}h3{font-size:1.18rem;margin:1.4em 0 .4em}
p{margin:0 0 1em}ul,ol{padding-left:1.25em}li{margin:.3em 0}
.ic{flex:none}
/* header */
.top{background:var(--ink);color:#fff;position:sticky;top:0;z-index:50;box-shadow:0 2px 10px rgba(0,0,0,.18)}
.top .wrap{display:flex;align-items:center;gap:16px;min-height:66px}
.logo{display:flex;align-items:center;gap:10px;color:#fff;text-decoration:none;font-weight:800;font-size:1.32rem;letter-spacing:-.02em}.logo b{color:var(--amber)}.logo:hover{color:#fff}
.nav{margin-left:auto;display:flex;align-items:center;gap:4px}
.nav>a,.nav .dd>button{color:#e9f1ec;text-decoration:none;font:inherit;font-size:.97rem;font-weight:600;background:none;border:0;padding:10px 12px;border-radius:8px;cursor:pointer;display:flex;align-items:center;gap:2px}
.nav>a:hover,.nav .dd>button:hover,.nav .dd>button:focus-visible{background:var(--ink2);color:#fff}
.dd{position:relative}.dd-menu{display:none;position:absolute;top:100%;left:0;background:#fff;border-radius:12px;box-shadow:var(--shadow);padding:10px;min-width:290px;border:1px solid var(--line)}
.dd-menu a{display:block;color:var(--ink);text-decoration:none;padding:8px 12px;border-radius:8px;font-size:.95rem}.dd-menu a:hover{background:var(--bg);color:var(--brand2)}
.dd.open .dd-menu,.dd:hover .dd-menu,.dd:focus-within .dd-menu{display:block}
.dd-menu.states{display:none;grid-template-columns:repeat(3,1fr);min-width:600px;left:auto;right:-170px;max-height:72vh;overflow:auto}.dd-menu.states a{padding:5px 10px;font-size:.9rem}.dd.open .dd-menu.states,.dd:hover .dd-menu.states,.dd:focus-within .dd-menu.states{display:grid}
dl.gloss dt{font-weight:800;margin-top:14px;scroll-margin-top:80px}dl.gloss dd{margin:4px 0 0}.pills-jump a{display:inline-block;padding:2px 8px;margin:2px;border:1px solid var(--line);border-radius:6px;text-decoration:none}
.state a{text-decoration:none;color:var(--ink)}.state a:hover strong{color:var(--brand2);text-decoration:underline}
.dd-menu.cols{display:none;grid-template-columns:1fr 1fr;min-width:520px}.dd.open .dd-menu.cols,.dd:hover .dd-menu.cols,.dd:focus-within .dd-menu.cols{display:grid}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;padding:12px 20px;border-radius:999px;font-weight:700;text-decoration:none;border:2px solid transparent;cursor:pointer;font-size:1rem;line-height:1.2}
.btn-call{background:var(--amber);color:#1b1400}.btn-call:hover{background:var(--amber2);color:#000}
.btn-ghost{border-color:#fff;color:#fff}.btn-ghost:hover{background:#fff;color:var(--ink)}
.btn-line{border-color:var(--brand);color:var(--brand2);background:#fff}.btn-line:hover{background:var(--brand);color:#fff}
.menu-btn{display:none;margin-left:auto;background:none;border:2px solid #3f5d4f;color:#fff;border-radius:10px;padding:8px 12px;font:inherit;font-weight:700;cursor:pointer}
.head-call{margin-left:8px}
@media (max-width:960px){.menu-btn{display:block}.head-call{display:none}.nav{display:none;position:absolute;top:66px;left:0;right:0;background:var(--ink);flex-direction:column;align-items:stretch;padding:10px 16px 18px;max-height:calc(100vh - 66px);overflow:auto}.nav.open{display:flex}.nav .dd-menu,.nav .dd-menu.cols,.nav .dd-menu.states{position:static;box-shadow:none;min-width:0;background:var(--ink2);border:0;grid-template-columns:1fr}.dd:hover .dd-menu{display:none}.dd:hover .dd-menu.cols,.dd:hover .dd-menu.states{display:none}.dd.open .dd-menu{display:block}.dd.open .dd-menu.cols{display:grid}.dd.open .dd-menu.states{display:grid;grid-template-columns:1fr 1fr;min-width:0;max-height:none}.dd-menu a{color:#e9f1ec}.dd-menu a:hover{background:var(--ink);color:#fff}}
/* hero */
.hero{position:relative;color:#fff;background:var(--ink);overflow:hidden}
.hero .bg{position:absolute;inset:0}.hero .bg img{width:100%;height:100%;object-fit:cover;opacity:.32}
.hero .wrap{position:relative;padding:64px 20px 56px}.hero h1{color:#fff;max-width:780px}.hero .lead{font-size:1.16rem;max-width:700px;color:#e8f0eb}
.hero-ctas{display:flex;flex-wrap:wrap;gap:12px;margin:22px 0}
.chips{display:flex;flex-wrap:wrap;gap:8px;padding:0;margin:14px 0 0;list-style:none}.chips li{background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.25);padding:6px 12px;border-radius:999px;font-size:.9rem;margin:0;display:flex;align-items:center;gap:6px}
.page-hero .wrap{padding:30px 20px 40px}
.crumbs{font-size:.88rem;color:#cfe0d6;margin:0 0 6px}.crumbs a{color:#fff}.crumbs ol{list-style:none;padding:0;margin:0;display:flex;flex-wrap:wrap;gap:6px}.crumbs li{margin:0}.crumbs li+li::before{content:"/";margin-right:6px;opacity:.7}
/* layout */
main{display:block}.section{padding:20px 0 30px}.band{background:#fff;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.grid{display:grid;gap:18px}.g2{grid-template-columns:repeat(auto-fit,minmax(280px,1fr))}.g3{grid-template-columns:repeat(auto-fit,minmax(250px,1fr))}.g4{grid-template-columns:repeat(auto-fit,minmax(210px,1fr))}
.card{background:var(--card);border:1px solid var(--line);border-radius:var(--radius);padding:20px;box-shadow:var(--shadow)}
.card h3{margin-top:0}.card a.more{font-weight:700}
.svc-card{display:flex;flex-direction:column;padding:0;overflow:hidden}.svc-card img{aspect-ratio:3/2;object-fit:cover;width:100%}.svc-card .in{padding:16px 18px 18px}.svc-card h3{margin:0 0 6px;font-size:1.08rem}.svc-card h3 a{text-decoration:none;color:var(--ink)}.svc-card h3 a:hover{color:var(--brand2);text-decoration:underline}.svc-card p{font-size:.95rem;color:var(--muted);margin:0}
.illus{aspect-ratio:3/2;width:100%;background:#eaf2ea;display:flex;align-items:center;justify-content:center}
.content{background:#fff;border:1px solid var(--line);border-radius:var(--radius);padding:28px clamp(18px,4vw,44px);margin:-26px auto 24px;position:relative;box-shadow:var(--shadow)}
.content>h2:first-child{margin-top:.3em}
.quick{background:#eef6ef;border-left:5px solid var(--brand);padding:16px 18px;border-radius:10px;margin:0 0 1.2em}
.checklist{list-style:none;padding:0}.checklist li{position:relative;padding-left:30px}.checklist li::before{content:"";position:absolute;left:0;top:.35em;width:18px;height:18px;border-radius:50%;background:var(--brand) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='%23fff'%3E%3Cpath d='M9 16.2 4.8 12l-1.4 1.4L9 19 21 7l-1.4-1.4z'/%3E%3C/svg%3E") center/14px no-repeat}
.cols2{columns:2 260px;column-gap:28px}
.tbl{width:100%;border-collapse:collapse;margin:0 0 1.2em;font-size:.95rem}.tbl th,.tbl td{border:1px solid var(--line);padding:10px 12px;text-align:left;vertical-align:top}.tbl th{background:#eef3ec}.tbl-wrap{overflow-x:auto}
ol.steps{counter-reset:s;list-style:none;padding:0}ol.steps li{counter-increment:s;position:relative;padding:0 0 4px 46px;margin:0 0 12px}ol.steps li::before{content:counter(s);position:absolute;left:0;top:0;width:32px;height:32px;border-radius:50%;background:var(--ink);color:var(--amber);font-weight:800;display:flex;align-items:center;justify-content:center}
.cta-box{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:14px;background:var(--ink);color:#fff;border-radius:var(--radius);padding:20px 22px;margin:1.6em 0}.cta-box p{margin:0;color:#dce8e1}.cta-box .cta-title{color:#fff;font-weight:800;font-size:1.12rem;margin-bottom:2px}
figure{margin:1.4em 0}figure img{border-radius:12px;width:100%}figcaption{font-size:.88rem;color:var(--muted);margin-top:6px}
details{border:1px solid var(--line);border-radius:10px;padding:12px 16px;margin:0 0 10px;background:#fff}details summary{font-weight:700;cursor:pointer;list-style:none;display:flex;justify-content:space-between;gap:10px}details summary::-webkit-details-marker{display:none}details summary::after{content:"+";font-size:1.3rem;line-height:1;color:var(--brand)}details[open] summary::after{content:"-"}details p{margin:.7em 0 0}
.pills{display:flex;flex-wrap:wrap;gap:8px;list-style:none;padding:0}.pills li{margin:0}.pills a,.pills span{display:inline-block;padding:7px 13px;border-radius:999px;background:#eef3ec;border:1px solid var(--line);text-decoration:none;font-size:.92rem;color:var(--ink)}.pills a:hover{background:var(--brand);color:#fff}
.sources{font-size:.92rem}.reviewed{font-size:.9rem;color:var(--muted);border-top:1px solid var(--line);padding-top:12px}
.steps-row{counter-reset:h}.step-card{position:relative}.step-card .num{display:inline-flex;width:36px;height:36px;border-radius:50%;background:var(--amber);color:#1b1400;font-weight:800;align-items:center;justify-content:center;margin-bottom:8px}
.state-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:12px}.state{background:#fff;border:1px solid var(--line);border-radius:12px;padding:12px 14px}.state strong{display:block}.state span{font-size:.88rem;color:var(--muted)}
.form label{display:block;font-weight:600;margin:12px 0 4px}.form input,.form select,.form textarea{width:100%;padding:12px;border:1px solid #b9c7bd;border-radius:10px;font:inherit;background:#fff}.form input:focus,.form select:focus,.form textarea:focus{outline:3px solid var(--amber);border-color:var(--brand)}.form .hp{position:absolute;left:-5000px}.form-note{font-size:.85rem;color:var(--muted)}.form-msg{font-weight:700;margin-top:10px}
.legal h2{font-size:1.3rem}.legal .doc{background:#eef3ec;padding:10px 14px;border-radius:10px;font-size:.95rem}
/* call band + footer */
.callband{background:var(--brand2);color:#fff;padding:34px 0}.callband .wrap{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:16px}.callband h2{color:#fff;margin:0 0 4px;font-size:1.5rem}.callband p{margin:0;color:#dff0e6}
footer{background:var(--ink);color:#cbd9d0;padding:44px 0 90px;font-size:.94rem}footer a{color:#fff}footer h2{color:#fff;font-size:1.02rem;margin:0 0 10px}footer ul{list-style:none;padding:0;margin:0}footer li{margin:6px 0}
.fgrid{display:grid;gap:26px;grid-template-columns:repeat(auto-fit,minmax(200px,1fr))}.disclosure{border-top:1px solid #2c4a3c;margin-top:28px;padding-top:18px;font-size:.86rem;color:#b9cbc0}
.mbar{position:fixed;left:0;right:0;bottom:0;z-index:60;background:var(--ink);padding:10px 14px;display:none;box-shadow:0 -4px 14px rgba(0,0,0,.2)}.mbar a{width:100%}
@media (max-width:960px){.mbar{display:block}}
@media (min-width:961px){footer{padding-bottom:44px}}
:focus-visible{outline:3px solid var(--amber);outline-offset:2px}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
"""

def minify_css(css):
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    css = re.sub(r"\s+", " ", css)
    css = re.sub(r"\s*([{}:;,>])\s*", r"\1", css)
    return css.replace(";}", "}").strip()

JS = """(function(){var b=document.querySelector('.menu-btn'),n=document.getElementById('nav');if(b&&n){b.addEventListener('click',function(){var o=n.classList.toggle('open');b.setAttribute('aria-expanded',o)})}
document.querySelectorAll('.dd>button').forEach(function(t){t.addEventListener('click',function(e){var d=t.parentNode,o=d.classList.toggle('open');t.setAttribute('aria-expanded',o);document.querySelectorAll('.dd.open').forEach(function(x){if(x!==d){x.classList.remove('open');x.querySelector('button').setAttribute('aria-expanded','false')}})})});
document.addEventListener('keydown',function(e){if(e.key==='Escape'){document.querySelectorAll('.dd.open').forEach(function(x){x.classList.remove('open')})}});
var f=document.getElementById('lead-form');if(f){f.addEventListener('submit',function(e){e.preventDefault();var m=f.querySelector('.form-msg'),btn=f.querySelector('button');btn.disabled=true;m.textContent='Sending...';
fetch('/api/lead',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(Object.fromEntries(new FormData(f)))}).then(function(r){return r.json()}).then(function(d){m.textContent=d.ok?'Thanks. Your request was sent. For faster help, call the number above.':(d.error||'Something went wrong. Please call instead.');if(d.ok)f.reset();btn.disabled=false}).catch(function(){m.textContent='Something went wrong. Please call instead.';btn.disabled=false})})}})();"""

# --------------------------------------------------------------- layout
def nav_html():
    svc_links = "".join(f'<a href="/services/{s["slug"]}/">{s["nav"]}</a>' for s in SERVICES)
    state_links = "".join(f'<a href="/locations/{slug}/">{name}</a>' for slug, name in STATE_NAV)
    return f'''<header class="top"><div class="wrap">
<a class="logo" href="/" aria-label="{BRAND} home">{LOGO_SVG}<span>Pest<b>Halt</b></span></a>
<button class="menu-btn" aria-expanded="false" aria-controls="nav">Menu</button>
<nav id="nav" class="nav" aria-label="Main">
<div class="dd"><button aria-expanded="false" aria-haspopup="true">Services{icon("chev",18)}</button><div class="dd-menu cols"><a href="/services/"><strong>All pest control services</strong></a>{svc_links}</div></div>
<div class="dd"><button aria-expanded="false" aria-haspopup="true">Locations{icon("chev",18)}</button><div class="dd-menu states"><a href="/locations/"><strong>All locations</strong></a>{state_links}</div></div>
<a href="/about/">About</a>
<a href="/contact/">Contact</a>
<span class="head-call">{phone_link("btn btn-call", PHONE_DISPLAY)}</span>
</nav></div></header>'''

def footer_html():
    svc_links = "".join(f'<li><a href="/services/{s["slug"]}/">{s["nav"]}</a></li>' for s in SERVICES[:7])
    svc_links2 = "".join(f'<li><a href="/services/{s["slug"]}/">{s["nav"]}</a></li>' for s in SERVICES[7:])
    return f'''<footer><div class="wrap">
<div class="fgrid">
<div><a class="logo" href="/" aria-label="{BRAND} home">{LOGO_SVG}<span>Pest<b>Halt</b></span></a>
<p style="margin-top:12px">Pest control help across the United States. One call connects you with a state-licensed local pest control provider.</p>
<p><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></p></div>
<div><h2>Pest control services</h2><ul>{svc_links}</ul></div>
<div><h2>More services</h2><ul>{svc_links2}<li><a href="/services/">All services</a></li></ul></div>
<div><h2>Company</h2><ul><li><a href="/about/">About {BRAND}</a></li><li><a href="/contact/">Contact</a></li><li><a href="/locations/">Locations</a></li><li><a href="/glossary/">Pest control glossary</a></li><li><a href="/editorial-policy/">Editorial policy</a></li><li><a href="/disclaimer/">Disclaimer</a></li><li><a href="/privacy-policy/">Privacy policy</a></li><li><a href="/terms/">Terms of use</a></li><li><a href="/accessibility/">Accessibility</a></li></ul></div>
</div>
<p class="disclosure">{DISCLOSURE}<br><br>&copy; {TODAY.year} {BRAND}. All rights reserved. Information on this site is general guidance, not professional advice.</p>
</div></footer>
<div class="mbar">{phone_link("btn btn-call", f"Call {PHONE_DISPLAY}")}</div>'''

def call_band(title="Pests won't leave on their own", text="Call to reach a licensed local pest control provider and set up an inspection."):
    return (f'<section class="callband" aria-label="Call {BRAND}"><div class="wrap"><div><h2>{title}</h2><p>{text}</p></div>'
            f'{phone_link("btn btn-call", f"Call {PHONE_DISPLAY}")}</div></section>')

def crumbs_html(crumbs):
    items = []
    for i, (name, url) in enumerate(crumbs):
        if i == len(crumbs) - 1:
            items.append(f'<li aria-current="page">{name}</li>')
        else:
            items.append(f'<li><a href="{url}">{name}</a></li>')
    return f'<nav class="crumbs" aria-label="Breadcrumb"><ol>{"".join(items)}</ol></nav>'

def breadcrumb_schema(crumbs, url):
    return {"@type": "BreadcrumbList", "@id": f"{url}#breadcrumb",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": re.sub("<[^>]+>", "", n), "item": BASE + u}
                                for i, (n, u) in enumerate(crumbs)]}

def faq_schema(faqs, url):
    return {"@type": "FAQPage", "@id": f"{url}#faq",
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub("<[^>]+>", "", a)}} for q, a in faqs]}

def faq_html(faqs, title):
    return f'<h2 id="faq">{title}</h2>' + "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)

def org_nodes():
    return [
        {"@type": "Organization", "@id": ORG_ID, "name": BRAND, "url": BASE + "/",
         "logo": {"@type": "ImageObject", "url": f"{BASE}/assets/logo-512.png", "width": 512, "height": 512},
         "telephone": PHONE_TEL, "publishingPrinciples": f"{BASE}/editorial-policy/",
         "founder": {"@type": "Person", "name": OWNER}},
        {"@type": "WebSite", "@id": SITE_ID, "url": BASE + "/", "name": BRAND, "publisher": {"@id": ORG_ID}, "inLanguage": "en-US"},
    ]

PAGES = {}  # url -> dict(title, meta, html, priority, kind)

def page(url, title, meta, h1_hero, body, crumbs=None, schema=None, priority=0.5, kind="page",
         noindex=False, og_image="home-hero", word_target=None):
    """Assemble a full HTML page and register it."""
    assert len(title) <= 60, f"title too long ({len(title)}): {title}"
    assert len(meta) <= 155, f"meta too long ({len(meta)}): {meta}"
    canonical = BASE + url
    if AUTOLINK and kind in ("service", "state"):
        body = AUTOLINK(body, url)
    graph = []
    if url == "/":
        pass
    graph += schema or []
    if crumbs:
        graph.append(breadcrumb_schema(crumbs, canonical))
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, separators=(",", ":"))
    robots = "noindex,follow" if noindex else "index,follow,max-image-preview:large"
    og = f"{BASE}/assets/img/{og_image}-1200.webp"
    doc = f'''<!doctype html>
<html lang="en-US">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(meta)}">
<link rel="canonical" href="{canonical}">
<meta name="robots" content="{robots}">
<meta name="theme-color" content="#0f2a1e">
<meta property="og:type" content="website"><meta property="og:site_name" content="{BRAND}"><meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(meta)}"><meta property="og:url" content="{canonical}"><meta property="og:image" content="{og}"><meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{html.escape(title)}"><meta name="twitter:description" content="{html.escape(meta)}"><meta name="twitter:image" content="{og}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="icon" href="/favicon-32.png" sizes="32x32" type="image/png"><link rel="apple-touch-icon" href="/apple-touch-icon.png"><link rel="manifest" href="/site.webmanifest">
<style>{minify_css(CSS)}</style>
<script type="application/ld+json">{ld}</script>
<script src="/assets/app.js" defer></script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
{nav_html()}
<main id="main">
{h1_hero}
{body}
</main>
{footer_html()}
</body>
</html>'''
    PAGES[url] = dict(title=title, meta=meta, html=doc, priority=priority, kind=kind, noindex=noindex, word_target=word_target)
    return doc

def page_hero(crumbs, h1, lead, image=None, image_alt="", chips=None):
    bg = f'<div class="bg">{img(image, image_alt, eager=True, sizes="100vw")}</div>' if image else ""
    chips_html = ""
    if chips:
        chips_html = '<ul class="chips">' + "".join(f"<li>{icon('check',16)}{c}</li>" for c in chips) + "</ul>"
    return (f'<section class="hero page-hero">{bg}<div class="wrap">{crumbs_html(crumbs) if crumbs else ""}'
            f'<h1>{h1}</h1><p class="lead">{lead}</p><div class="hero-ctas">{phone_link()}</div>{chips_html}</div></section>')

def write_all():
    for url, p in PAGES.items():
        path = os.path.join(OUT, url.strip("/"), "index.html") if url != "/404/" else os.path.join(OUT, "404.html")
        if url == "/":
            path = os.path.join(OUT, "index.html")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as f:
            f.write(p["html"])
    # app.js
    os.makedirs(os.path.join(OUT, "assets"), exist_ok=True)
    open(os.path.join(OUT, "assets", "app.js"), "w").write(JS)
    # sitemap
    urls = [(u, p) for u, p in PAGES.items() if not p["noindex"]]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u, p in sorted(urls, key=lambda x: -x[1]["priority"]):
        sm.append(f"<url><loc>{BASE}{u}</loc><lastmod>{TODAY_ISO}</lastmod><priority>{p['priority']:.1f}</priority></url>")
    sm.append("</urlset>")
    open(os.path.join(OUT, "sitemap.xml"), "w").write("\n".join(sm))
    open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nDisallow: /api/\n\nSitemap: {BASE}/sitemap.xml\n")
    manifest = {"name": BRAND, "short_name": BRAND, "start_url": "/", "display": "standalone", "background_color": "#f5f7f2",
                "theme_color": "#0f2a1e", "icons": [{"src": "/icon-192.png", "sizes": "192x192", "type": "image/png"},
                                                    {"src": "/assets/logo-512.png", "sizes": "512x512", "type": "image/png"}]}
    open(os.path.join(OUT, "site.webmanifest"), "w").write(json.dumps(manifest))
    open(os.path.join(OUT, "_headers"), "w").write(
"""/*
  X-Content-Type-Options: nosniff
  X-Frame-Options: SAMEORIGIN
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: camera=(), microphone=(), geolocation=()
  Strict-Transport-Security: max-age=31536000; includeSubDomains
  Content-Security-Policy: default-src 'self'; img-src 'self' data:; style-src 'self' 'unsafe-inline'; script-src 'self' 'unsafe-inline'; connect-src 'self'; frame-ancestors 'self'; base-uri 'self'; form-action 'self'
  Cache-Control: public, max-age=600, must-revalidate
/assets/*
  Cache-Control: public, max-age=31536000, immutable
/*.png
  Cache-Control: public, max-age=2592000
/favicon.svg
  Cache-Control: public, max-age=2592000
""")
    open(os.path.join(OUT, "_redirects"), "w").write(
"""/index.html / 301
/home / 301
/services/pest-control/ /services/general-pest-control/ 301
/services/exterminator/ /services/general-pest-control/ 301
/services/bed-bugs/ /services/bed-bug-treatment/ 301
/services/termites/ /services/termite-control/ 301
/services/rodents/ /services/rodent-control/ 301
""")
