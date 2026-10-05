# -*- coding: utf-8 -*-
"""ste_site_lint.py - residual STE scan of a BUILT site (root with <slug>.html pages).

  python ste_site_lint.py SITE_ROOT [--only slug,slug] [--top 25] [--spacy] [--keep DIR]

For every page it extracts the human-readable text units of <main> / <body> with ste_html_units.py
(markup, scripts, styles and SVG are not text units), lints them with the GLOBAL lexicon
(all paper technical-noun lists together) and prints errors / warnings per page plus the
words that are flagged most often.  This is a residual scan, not a certificate: it finds text
that no rewriting agent saw (generator strings, injected diagrams, evidence panel, photo credits,
index and curriculum pages ...).
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
PY = sys.executable


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("root")
    ap.add_argument("--only", default="")
    ap.add_argument("--top", type=int, default=25)
    ap.add_argument("--spacy", action="store_true", help="enable the spaCy layer (slower)")
    ap.add_argument("--keep", default="", help="keep the units files in this folder")
    ap.add_argument("--list", action="store_true", help="print every flagged unit (page, id, first finding)")
    a = ap.parse_args()
    root = os.path.abspath(a.root)
    man = json.load(open(os.path.join(root, "manifest.json"), encoding="utf-8"))
    pages = [p["slug"] for p in man["papers"]] + ["index", "curriculum", "glossary"]
    if a.only:
        pages = [p for p in pages if p in a.only.split(",")]
    work = a.keep or tempfile.mkdtemp(prefix="ste_site_")
    words = Counter()
    rows = []
    for slug in pages:
        html = os.path.join(root, slug + ".html")
        if not os.path.exists(html):
            rows.append((slug, -1, -1, 0))
            continue
        r = run([PY, os.path.join(HERE, "ste_html_units.py"), "extract", html, "--work", work, "--scope", "body", "--force"])
        up = os.path.join(work, slug, "units.txt")
        if not os.path.exists(up):
            rows.append((slug, -1, -1, 0))
            continue
        cmd = [PY, os.path.join(HERE, "ste_lint.py"), "--units", up, "--slug", "ALL", "--json", "--max", "100000"]
        if not a.spacy:
            cmd.append("--no-spacy")
        out = run(cmd).stdout
        try:
            j = json.loads(out[out.index("{"):])
        except Exception:
            rows.append((slug, -2, -2, 0))
            continue
        fs = j["findings"]
        units = len(re.findall(r"^@@ U", open(up, encoding="utf-8").read(), re.M))
        rows.append((slug, j["errors"], j["warnings"], units))
        for f in fs:
            if f["sev"] == "E" and f["rule"] == "R1.1":
                m = re.match(r"'([^']+)'", f.get("msg", ""))
                if m:
                    words[m.group(1).lower()] += 1
        if a.list:
            seen = set()
            for f in fs:
                if f["sev"] == "E" and f["unit"] not in seen:
                    seen.add(f["unit"])
                    print("  %s %s: %s | %s" % (slug, f["unit"], f["rule"], f.get("msg", "")[:90]))
    print("%-38s %6s %6s %6s" % ("page", "units", "E", "W"))
    tot = [0, 0, 0]
    for slug, e, w, n in rows:
        flag = "" if e == 0 else "  <--"
        print("%-38s %6d %6d %6d%s" % (slug, n, e, w, flag))
        if e > 0:
            tot[0] += n; tot[1] += e; tot[2] += w
    print("\npages with errors: %d of %d | errors %d" % (sum(1 for r in rows if r[1] > 0), len(rows), tot[1]))
    if words:
        print("\nmost frequent unknown / not-approved words (R1.1):")
        print(", ".join("%s(%d)" % kv for kv in words.most_common(a.top)))
    if not a.keep:
        shutil.rmtree(work, ignore_errors=True)


if __name__ == "__main__":
    main()
