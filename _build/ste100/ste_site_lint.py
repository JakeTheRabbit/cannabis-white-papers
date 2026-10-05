# -*- coding: utf-8 -*-
"""ste_site_lint.py - residual STE scan of a BUILT site (root with <slug>.html pages).

  python ste_site_lint.py SITE_ROOT [--only slug,slug] [--top 25] [--spacy] [--keep DIR] [--list] [--jobs 4]

For every page it extracts the human-readable text units of <body> with ste_html_units.py
(markup, scripts, styles and SVG are not text units), lints them with the GLOBAL lexicon
(all paper technical-noun lists together) and prints errors / warnings per page plus the
words that are flagged most often.  This is a residual scan, not a certificate: it finds text
that no rewriting agent saw (generator strings, injected diagrams, evidence panel, photo credits,
index and curriculum pages ...).

Known artifacts: the fit-to-width page title is drawn twice (the second copy is aria-hidden), so
the extractor glues the title to the text after it ("cuttingshow"); these are not page text.
"""
import argparse
import concurrent.futures as cf
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


def scan(args):
    slug, root, work, spacy = args
    html = os.path.join(root, slug + ".html")
    if not os.path.exists(html):
        return slug, -1, -1, 0, Counter(), []
    run([PY, os.path.join(HERE, "ste_html_units.py"), "extract", html, "--work", work, "--scope", "body", "--force"])
    up = os.path.join(work, slug, "units.txt")
    if not os.path.exists(up):
        return slug, -1, -1, 0, Counter(), []
    cmd = [PY, os.path.join(HERE, "ste_lint.py"), "--units", up, "--slug", "ALL", "--json", "--max", "100000"]
    if not spacy:
        cmd.append("--no-spacy")
    out = run(cmd).stdout
    try:
        j = json.loads(out[out.index("{"):])
    except Exception:
        return slug, -2, -2, 0, Counter(), []
    words, lines, seen = Counter(), [], set()
    for f in j["findings"]:
        if f["sev"] == "E":
            if f["rule"] == "R1.1":
                m = re.match(r"'([^']+)'", f.get("msg", ""))
                if m:
                    words[m.group(1).lower()] += 1
            if f["unit"] not in seen:
                seen.add(f["unit"])
                lines.append("  %s %s: %s | %s | %s" % (slug, f["unit"], f["rule"], f.get("msg", "")[:80], (f.get("ctx") or "")[:90]))
    n = len(re.findall(r"^@@ U", open(up, encoding="utf-8").read(), re.M))
    return slug, j["errors"], j["warnings"], n, words, lines


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("root")
    ap.add_argument("--only", default="")
    ap.add_argument("--top", type=int, default=25)
    ap.add_argument("--spacy", action="store_true", help="enable the spaCy layer (slower)")
    ap.add_argument("--keep", default="", help="keep the units files in this folder")
    ap.add_argument("--list", action="store_true", help="print every flagged unit (page, id, first finding)")
    ap.add_argument("--jobs", type=int, default=4)
    a = ap.parse_args()
    root = os.path.abspath(a.root)
    man = json.load(open(os.path.join(root, "manifest.json"), encoding="utf-8"))
    pages = [p["slug"] for p in man["papers"]] + ["index", "curriculum", "glossary"]
    if a.only:
        pages = [p for p in pages if p in a.only.split(",")]
    work = a.keep or tempfile.mkdtemp(prefix="ste_site_")
    os.makedirs(work, exist_ok=True)
    words = Counter()
    rows = []
    with cf.ThreadPoolExecutor(a.jobs) as ex:
        for slug, e, w, n, wc, lines in ex.map(scan, [(p, root, work, a.spacy) for p in pages]):
            rows.append((slug, e, w, n))
            words.update(wc)
            if a.list:
                for ln in lines:
                    print(ln, flush=True)
    print("%-38s %6s %6s %6s" % ("page", "units", "E", "W"))
    tot = [0, 0]
    for slug, e, w, n in rows:
        print("%-38s %6d %6d %6d%s" % (slug, n, e, w, "" if e == 0 else "  <--"))
        if e > 0:
            tot[0] += 1
            tot[1] += e
    print("\npages with errors: %d of %d | errors %d" % (tot[0], len(rows), tot[1]))
    if words:
        print("\nmost frequent unknown / not-approved words (R1.1):")
        print(", ".join("%s(%d)" % kv for kv in words.most_common(a.top)))
    if not a.keep:
        shutil.rmtree(work, ignore_errors=True)


if __name__ == "__main__":
    main()
