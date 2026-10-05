# -*- coding: utf-8 -*-
"""ste_verify_all.py - run `ste_verify.py check` for every paper module and print one line each.

  C:\\Tools\\ste-lint\\.venv\\Scripts\\python.exe _build/ste100/ste_verify_all.py [--jobs 4] [--only a,b]

Exit code 1 when a paper fails.  Output: module, RESULT, parity errors/warnings, lint errors/warnings.
"""
import argparse
import concurrent.futures as cf
import glob
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.dirname(HERE)


def check(mod):
    r = subprocess.run([sys.executable, os.path.join(HERE, "ste_verify.py"), "check", mod],
                       capture_output=True, text=True, encoding="utf-8", errors="replace", cwd=BUILD)
    out = r.stdout + r.stderr
    res = re.search(r"RESULT:\s*(\w+)", out)
    par = re.search(r"parity:\s*(\d+) errors?,\s*(\d+) warnings?", out)
    lint = re.search(r"==\s*\d+ units \|\s*(\d+) errors?\s*\|\s*(\d+) warnings?", out)
    return mod, (res.group(1) if res else "NO-RESULT"), par.groups() if par else ("?", "?"), lint.groups() if lint else ("?", "?"), out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--only", default="")
    a = ap.parse_args()
    mods = sorted(os.path.basename(f)[:-3] for f in glob.glob(os.path.join(BUILD, "paper_*.py")))
    if a.only:
        mods = [m for m in mods if any(o in m for o in a.only.split(","))]
    bad = 0
    with cf.ThreadPoolExecutor(a.jobs) as ex:
        for mod, res, par, lint, out in ex.map(check, mods):
            flag = "" if res == "PASS" else "   <-- " + res
            print("%-38s %-6s parity E%s W%s | lint E%s W%s%s" % (mod, res, par[0], par[1], lint[0], lint[1], flag), flush=True)
            if res != "PASS":
                bad += 1
                for line in out.splitlines():
                    if re.match(r"\s*(E|W)\s", line) or line.startswith("  E ") or " E " in line[:6]:
                        print("     " + line[:200])
    print("\n%d of %d papers not PASS" % (bad, len(mods)))
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
