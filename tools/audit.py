#!/usr/bin/env python3
"""Self-audit for the built site (rules: Local Service Site SEO Criteria, part 12).
Usage: python3 tools/audit.py   -> prints a check/status/issue table, exits 1 on failures."""
import os, re, json, sys, html
from html.parser import HTMLParser
from collections import defaultdict, Counter

ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "public")
BANNED = ["24/7", "24 hours a day", "24-hour", "around the clock", "day or night", "anytime", "any time of day", "open now",
          "live person", "live agent", "real person", "our crew", "our technician", "arrival window", "iicrc-certified",
          "licensed technicians", "insured and bonded", "5-star", "five-star", "award-winning", "minutes away", "60 minutes",
          "free estimate", "years in business", "10+ years", "placeholder", "lorem", "coming soon", "example.com", "guaranteed results"]


class P(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self.h, self.imgs, self.ld, self.text, self.title, self.meta = [], [], [], [], [], "", ""
        self._in = None; self._skip = 0; self._main = 0; self.main_text = []; self.paras = []; self._p = None; self.ids = set(); self._boiler = 0

    def handle_starttag(self, t, a):
        a = dict(a)
        if "id" in a: self.ids.add(a["id"])
        if t == "a" and a.get("href"): self.links.append(a["href"])
        if t in ("h1", "h2", "h3", "h4"): self._in = t; self.h.append([t, ""])
        if t == "img": self.imgs.append(a)
        if t == "script" and a.get("type") == "application/ld+json": self._in = "ld"; self.ld.append("")
        if t in ("script", "style"): self._skip += 1
        if t == "title": self._in = "title"
        if t == "meta" and a.get("name") == "description": self.meta = a.get("content", "")
        if t == "main": self._main = 1
        if t in ("footer",): self._main = 0
        if t == "p" and not self._boiler: self._p = []
        cls = a.get("class", "") or ""
        if self._boiler: self._boiler += (t in ("div","aside","section","article","footer"))
        elif t == "footer" or (t in ("div","aside","section","article") and any(c in cls.split() for c in ("svc-card","cta-box","callband","mbar"))): self._boiler = 1

    def handle_endtag(self, t):
        if t in ("h1", "h2", "h3", "h4", "title"): self._in = None
        if t == "script":
            self._skip -= 1
            if self._in == "ld": self._in = None
        if t == "style": self._skip -= 1
        if self._boiler and t in ("div","aside","section","article","footer"): self._boiler -= 1
        if t == "p" and self._p is not None:
            self.paras.append(" ".join("".join(self._p).split())); self._p = None

    def handle_data(self, d):
        if self._in == "ld": self.ld[-1] += d; return
        if self._in == "title": self.title += d
        if self._skip: return
        if self._in in ("h1", "h2", "h3", "h4"): self.h[-1][1] += d
        if self._main: self.main_text.append(d)
        if self._p is not None: self._p.append(d)
        self.text.append(d)


def url_of(path):
    rel = os.path.relpath(path, ROOT)
    if rel == "index.html": return "/"
    if rel == "404.html": return "/404/"
    return "/" + rel[:-len("index.html")]


def main():
    pages = {}
    for dp, dn, fn in os.walk(ROOT):
        for f in fn:
            if f.endswith(".html"):
                p = os.path.join(dp, f); pr = P(); s = open(p).read(); pr.feed(s)
                pages[url_of(p)] = (pr, s)
    issues = []
    def fail(check, url, msg): issues.append((check, url, msg))
    titles, metas = Counter(), Counter()
    inbound = defaultdict(set)
    para_seen = defaultdict(set)
    words = {}
    for url, (pr, s) in pages.items():
        titles[pr.title] += 1; metas[pr.meta] += 1
        if len(pr.title) > 60: fail("title length", url, len(pr.title))
        if len(pr.meta) > 155: fail("meta length", url, len(pr.meta))
        h1s = [h for h in pr.h if h[0] == "h1"]
        if len(h1s) != 1: fail("one h1", url, len(h1s))
        last = 1
        for t, _ in pr.h:
            lvl = int(t[1])
            if lvl > last + 1: fail("heading order", url, f"{t} after h{last}")
            last = lvl
        for href in pr.links:
            if href.startswith(("http", "tel:", "mailto:")): continue
            path, _, frag = href.partition("#")
            if not path: continue
            target = path if path.endswith("/") else path
            if target not in pages and not os.path.exists(os.path.join(ROOT, target.lstrip("/"))):
                fail("broken link", url, href)
            else:
                if frag and target in pages and frag not in pages[target][0].ids: fail("broken anchor", url, href)
                inbound[target].add(url)
        for im in pr.imgs:
            if "alt" not in im: fail("img alt", url, im.get("src"))
            if not im.get("width") or not im.get("height"): fail("img dims", url, im.get("src"))
            src = im.get("src", "")
            if src.startswith("/") and not os.path.exists(os.path.join(ROOT, src.lstrip("/"))): fail("img missing", url, src)
        for block in pr.ld:
            try:
                data = json.loads(block)
                faq = [n for n in data.get("@graph", []) if n.get("@type") == "FAQPage"]
                for f in faq:
                    for q in f["mainEntity"]:
                        if html.unescape(q["name"]) not in html.unescape(s): fail("faq visible", url, q["name"][:40])
                if any(n.get("@type") in ("Review", "AggregateRating") for n in data.get("@graph", [])): fail("ratings", url, "")
            except Exception as e:
                fail("json-ld", url, str(e))
        low = " ".join(pr.text).lower()
        for b in BANNED:
            if b in low: fail("banned wording", url, b)
        if len(s.encode()) > 100_000: fail("html size", url, len(s.encode()))
        main_words = len(re.findall(r"[A-Za-z0-9']+", " ".join(pr.main_text)))
        words[url] = main_words
        for para in pr.paras:
            if len(para.split()) >= 14 and url != "/404/":
                para_seen[para].add(url)
        if "rel=\"canonical\"" not in s: fail("canonical", url, "")
    for t, c in titles.items():
        if c > 1: fail("duplicate title", t, c)
    for m, c in metas.items():
        if c > 1: fail("duplicate meta", m[:50], c)
    for para, urls in para_seen.items():
        if len(urls) > 1 and not para.startswith(("Service disclosure",)):
            fail("duplicate paragraph", ",".join(sorted(urls))[:80], para[:60])
    for url in pages:
        if url not in ("/", "/404/") and not inbound.get(url): fail("orphan", url, "")
    # word count report
    print("WORD COUNTS (main content):")
    for url in sorted(words):
        print(f"  {words[url]:5d}  {url}")
    if os.path.isdir(os.path.join(ROOT, "locations")):
        u = uniqueness()
        if u:
            low = min(u.items(), key=lambda x: x[1])
            print(f"\nLOCATION UNIQUENESS (5-word shingles): lowest {low[0]} {low[1]:.0%}, average {sum(u.values())/len(u):.0%}")
            for k, v in u.items():
                if v < 0.60: issues.append(("location uniqueness", k, f"{v:.0%}"))
    # city pages need 3+ in-text (paragraph) inbound links
    for url, (pr, src) in pages.items():
        if url.startswith("/locations/") and url.count("/") == 4:
            n = 0
            for u2, (p2, s2) in pages.items():
                if u2 == url: continue
                m = re.search(r"<main.*?</main>", s2, re.S)
                if m and any(url in para for para in re.findall(r"<p[ >].*?</p>", m.group(0), re.S)): n += 1
            if n < 3: issues.append(("in-text inbound < 3", url, n))
    print(f"\nPAGES: {len(pages)}   ISSUES: {len(issues)}")
    for i in issues:
        print("  FAIL", *i)
    sys.exit(1 if issues else 0)



def uniqueness(prefix="/locations/", n=5, exclude_tables=False):
    """Share of each location page's 5-word shingles not found on any other location page."""
    import glob
    docs = {}
    for dp, dn, fn in os.walk(os.path.join(ROOT, "locations")):
        if dp == os.path.join(ROOT, "locations") or "index.html" not in fn: continue
        url = os.path.relpath(dp, os.path.join(ROOT, "locations"))
        p = os.path.join(dp, "index.html")
        s = open(p).read()
        s = re.sub(r'<(article|aside|section) class="(card svc-card|cta-box|callband)[^"]*".*?</\1>', " ", s, flags=re.S)
        m = re.search(r'<main.*?</main>', s, flags=re.S)
        txt = re.sub(r"<[^>]+>", " ", m.group(0)).lower()
        w = re.findall(r"[a-z0-9']+", txt)
        docs[url] = set(tuple(w[i:i + n]) for i in range(len(w) - n + 1))
    from collections import Counter
    cnt = Counter()
    for sh in docs.values(): cnt.update(sh)
    res = {u: sum(1 for x in sh if cnt[x] == 1) / max(1, len(sh)) for u, sh in docs.items()}
    return res


if __name__ == "__main__":
    main()
