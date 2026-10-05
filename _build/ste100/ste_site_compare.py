# -*- coding: utf-8 -*-
"""ste_site_compare.py - structure parity of the BUILT pages: baseline site vs rewritten site.

  python ste_site_compare.py BASE_ROOT NEW_ROOT [--only slug,slug] [--numbers] [--brief]

BASE_ROOT / NEW_ROOT are site roots (the folder that holds index.html and <slug>.html), for example a
build of the original commit and a build of the rewritten tree.  For every paper page it compares

  * section ids and order, kickers' numbers, h2 count
  * per section: counts of element kinds (tag + first class) outside <svg>: paragraphs, list items, table
    rows/cells, callouts, definitions, steps, cards, figures, photos, images ...
  * per section: citation targets (sup.cite hrefs), internal links (hrefs), SVG count and viewBoxes
  * where each injected diagram / photo landed (section id)
  * numbers in the text (a multiset difference: "added" / "removed" tokens), with --numbers the tokens

It does NOT judge wording.  Exit code 1 when a structural difference is found.
"""
import argparse
import json
import os
import re
import sys
from collections import Counter

from bs4 import BeautifulSoup

INLINE = {"em", "strong", "b", "i", "sub", "sup", "span", "br", "code", "a", "small", "mark", "abbr"}
NUM = re.compile(r"(?<![\w.])\d+(?:[.,]\d+)?")


def _text(el):
    if el is None:
        return ""
    for s in el.find_all("svg"):
        s.decompose()
    return re.sub(r"\s+", " ", el.get_text(" ")).strip()


def load(path):
    html = open(path, encoding="utf-8").read()
    return BeautifulSoup(html, "html.parser")


def kinds(sec):
    c = Counter()
    for el in sec.find_all(True):
        if el.find_parent("svg") is not None or el.name == "svg" and False:
            continue
        cls = el.get("class") or []
        if "xref" in cls or el.name in INLINE:
            continue
        key = el.name + ("." + cls[0] if cls else "")
        c[key] += 1
    return c


def signature(soup):
    sig = {"sections": []}
    main = soup.find("article") or soup.find("main") or soup
    for sec in main.select("section.sec"):
        sid = sec.get("id")
        h2 = sec.find("h2")
        kick = sec.select_one(".sec-kicker")
        k = kinds(sec)
        cites = sorted(a.get("href") for a in sec.select("sup.cite a"))
        links = sorted(a.get("href") for a in sec.find_all("a")
                       if a.get("href") and not a.find_parent("sup") and "xref" not in (a.get("class") or [])
                       and "/issues/new" not in a.get("href"))
        xrefs = sorted((a.get("href"), a.get_text(strip=True)) for a in sec.find_all("a", class_="xref"))
        svgs = [s.get("viewBox") for s in sec.find_all("svg")]
        figs = []
        for f in sec.find_all("figure"):
            fn = f.select_one(".fignum")
            figs.append((" ".join(f.get("class") or []), fn.get_text(strip=True) if fn else "", "img" if f.find("img") else ("svg" if f.find("svg") else "")))
        imgs = sorted((i.get("src") or "") for i in sec.find_all("img"))
        # text without svg
        clone = BeautifulSoup(str(sec), "html.parser")
        txt = _text(clone)
        sig["sections"].append({
            "id": sid, "h2": _text(h2) if h2 else "", "kicker": _text(kick) if kick else "",
            "kinds": dict(k), "cites": cites, "links": links, "xrefs": xrefs, "svgs": svgs, "figs": figs, "imgs": imgs,
            "numbers": NUM.findall(re.sub(r"^\s*\d+\s*", "", txt)), "words": len(txt.split()),
        })
    return sig


def compare(slug, a, b, show_numbers):
    out = []
    ia = [s["id"] for s in a["sections"]]
    ib = [s["id"] for s in b["sections"]]
    if ia != ib:
        out.append("SECTIONS differ: base=%s new=%s" % (ia, ib))
    bmap = {s["id"]: s for s in b["sections"]}
    amap = {s["id"]: s for s in a["sections"]}
    nadd, nrem = Counter(), Counter()
    for sid in ia:
        if sid not in bmap:
            continue
        x, y = amap[sid], bmap[sid]
        # a paragraph may be split into several
        kx, ky = Counter(x["kinds"]), Counter(y["kinds"])
        kx.pop("p", None), ky.pop("p", None)
        for key in set(kx) | set(ky):
            if key.startswith("div.kicker"):
                continue
            if kx.get(key, 0) != ky.get(key, 0):
                out.append("  [%s] element count %s: %d -> %d" % (sid, key, kx.get(key, 0), ky.get(key, 0)))
        if x["cites"] != y["cites"]:
            la, lb = Counter(x["cites"]), Counter(y["cites"])
            out.append("  [%s] citations: lost=%s added=%s" % (sid, sorted((la - lb).elements()), sorted((lb - la).elements())))
        if x["links"] != y["links"]:
            la, lb = Counter(x["links"]), Counter(y["links"])
            out.append("  [%s] links: lost=%s added=%s" % (sid, sorted((la - lb).elements()), sorted((lb - la).elements())))
        if x["svgs"] != y["svgs"]:
            out.append("  [%s] svg viewBoxes: %s -> %s" % (sid, x["svgs"], y["svgs"]))
        if x["figs"] != y["figs"]:
            out.append("  [%s] figures: %s -> %s" % (sid, x["figs"], y["figs"]))
        if x["imgs"] != y["imgs"]:
            out.append("  [%s] images: %s -> %s" % (sid, x["imgs"], y["imgs"]))
        nx, ny = Counter(x["numbers"]), Counter(y["numbers"])
        nadd.update(ny - nx)
        nrem.update(nx - ny)
    xa = {h: t for sid in ia for (h, t) in amap[sid]["xrefs"]}
    xb = {h: t for sid in ib for (h, t) in bmap[sid]["xrefs"]} if ib else {}
    lost = sorted(set(xa) - set(xb))
    gained = sorted(set(xb) - set(xa))
    xnote = ""
    if lost or gained:
        xnote = "  xref lost=%s gained=%s" % (["%s(%s)" % (h[:-5], xa[h]) for h in lost], ["%s(%s)" % (h[:-5], xb[h]) for h in gained])
    struct = len(out)
    note = "numbers: +%d / -%d" % (sum(nadd.values()), sum(nrem.values())) + xnote
    if show_numbers and (nadd or nrem):
        note += "  added=%s removed=%s" % (sorted(nadd.elements())[:40], sorted(nrem.elements())[:40])
    return out, struct, note


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("base")
    ap.add_argument("new")
    ap.add_argument("--only", default="")
    ap.add_argument("--numbers", action="store_true")
    ap.add_argument("--brief", action="store_true")
    a = ap.parse_args()
    man = json.load(open(os.path.join(a.new, "manifest.json"), encoding="utf-8"))
    slugs = [p["slug"] for p in man["papers"]]
    if a.only:
        slugs = [s for s in slugs if s in a.only.split(",")]
    bad = 0
    for slug in slugs:
        pa, pb = os.path.join(a.base, slug + ".html"), os.path.join(a.new, slug + ".html")
        if not (os.path.exists(pa) and os.path.exists(pb)):
            print("%-36s MISSING page" % slug)
            bad += 1
            continue
        out, struct, note = compare(slug, signature(load(pa)), signature(load(pb)), a.numbers)
        status = "OK  " if not struct else "DIFF"
        print("%s %-36s %s" % (status, slug, note))
        if struct:
            bad += 1
            if not a.brief:
                for line in out:
                    print("     " + line)
    print("\n%d of %d pages with structural differences" % (bad, len(slugs)))
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
