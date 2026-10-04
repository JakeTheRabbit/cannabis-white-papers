# -*- coding: utf-8 -*-
"""Progress table for the STE rewrite: one row per paper module.

  ste_dashboard.py [--only substr] [--json]

Columns: changed (module differs from git HEAD), words (rendered prose words), E / W (linter),
parity (structure/figures/citations vs baseline: ok/ERR n), REPORT (agent report present).
"""
import argparse
import importlib
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.dirname(HERE)
REPO = os.path.dirname(BUILD)
sys.path.insert(0, HERE)
sys.path.insert(0, BUILD)

import ste_lint as SL  # noqa: E402
import ste_verify as SV  # noqa: E402
from collections import Counter  # noqa: E402


def changed(module):
    r = subprocess.run(["git", "-C", REPO, "diff", "--quiet", "HEAD", "--", "_build/%s.py" % module])
    return r.returncode != 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
        sys.stdout.reconfigure(encoding="utf-8")
    from build import PAPER_MODULES
    rows = []
    ns = argparse.Namespace(no_spacy=True, level="W", max=0, summary=True, words=False, json=False, slug=None)
    for m in PAPER_MODULES:
        if a.only and a.only not in m:
            continue
        row = {"module": m, "changed": changed(m)}
        try:
            for k in [k for k in sys.modules if k == m]:
                del sys.modules[k]
            mod = importlib.import_module(m)
            ns.slug = getattr(mod, "SLUG", None)
            units = SL.units_from_module(m)
            findings, _ = SL.run(units, ns)
            row["E"] = sum(1 for f in findings if f.sev == "E")
            row["W"] = sum(1 for f in findings if f.sev == "W")
            row["words"] = sum(len(u.text.split()) for u in units)
            bp = os.path.join(SV.BASELINE_DIR, m + ".json")
            if os.path.exists(bp):
                base = json.load(open(bp, encoding="utf-8"))
                new = SV.signature(mod)
                errs = 0
                for key in ("slug", "related", "ref_ids", "meta_icons"):
                    errs += base[key] != new[key]
                if [s["id"] for s in base["sections"]] != [s["id"] for s in new["sections"]]:
                    errs += 1
                for b, n in zip(base["sections"], new["sections"]):
                    errs += (b["n_blocks"] != n["n_blocks"]) or (b["skeleton"] != n["skeleton"]) \
                        or (b["cites"] != n["cites"]) or (b["figures"] != n["figures"])
                row["parity"] = "ok" if not errs else "ERR %d" % errs
            else:
                row["parity"] = "-"
        except Exception as e:  # noqa: BLE001
            row.update(E="!", W="!", words=0, parity="IMPORT FAIL: %s" % str(e)[:40])
        row["report"] = os.path.exists(os.path.join(HERE, "work", m, "REPORT.md"))
        rows.append(row)
    if a.json:
        print(json.dumps(rows, indent=1))
        return
    print("%-34s %-4s %7s %6s %5s  %-10s %s" % ("module", "chg", "words", "E", "W", "parity", "report"))
    for r in rows:
        print("%-34s %-4s %7s %6s %5s  %-10s %s" % (r["module"], "yes" if r["changed"] else "-", r["words"], r["E"], r["W"],
                                                    r["parity"], "yes" if r["report"] else "-"))
    done = [r for r in rows if r["changed"] and r["E"] == 0]
    print("\n%d modules, %d changed, %d changed with E=0" % (len(rows), sum(r["changed"] for r in rows), len(done)))


if __name__ == "__main__":
    main()
