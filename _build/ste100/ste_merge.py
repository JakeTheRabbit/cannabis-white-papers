# -*- coding: utf-8 -*-
"""Merge rewritten part files into a paper's units.txt.

  ste_merge.py <module> [--work DIR] [--status]

Reads  work/<module>/units.txt  (the base) and every  part_*.txt  then  fix_*.txt  file in the
same folder (a part file holds a run of units: header line copied exactly, new text below).
For each unit in a part file the id must exist in the base and the header (kind, ctx) must be
identical; the text then replaces the base text.  Applied part files move to  applied/.
A copy of the very first base is kept as  units.original.txt  (never overwritten).
--status prints how many units are still unchanged.
"""
import argparse
import glob
import os
import shutil
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from ste_common import read_units, write_units  # noqa: E402


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("module")
    ap.add_argument("--work")
    ap.add_argument("--status", action="store_true")
    ap.add_argument("--html", help="repo-relative HTML file when the work folder belongs to ste_html_units.py")
    ap.add_argument("--no-check", action="store_true", help="skip the apply --dry-run validation after the merge")
    a = ap.parse_args()
    if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
        sys.stdout.reconfigure(encoding="utf-8")
    work = os.path.join(a.work, a.module) if a.work else os.path.join(HERE, "work", a.module)   # same --work meaning as ste_units.py
    base_path = os.path.join(work, "units.txt")
    orig_path = os.path.join(work, "units.original.txt")
    if not os.path.exists(base_path):
        print("no units.txt in", work, "- run ste_units.py extract first")
        return 2
    if not os.path.exists(orig_path):
        shutil.copyfile(base_path, orig_path)
    header, units = read_units(base_path)
    by_id = {u.id: u for u in units}
    _, orig_units = read_units(orig_path)
    orig = {u.id: u.text for u in orig_units}

    files = sorted(glob.glob(os.path.join(work, "part_*.txt"))) + sorted(glob.glob(os.path.join(work, "fix_*.txt")))
    errors, merged = [], 0
    pending = []
    for f in files:
        _, pu = read_units(f)
        if not pu:
            errors.append("%s: no '@@ Uxxxx | kind | ctx' headers found" % os.path.basename(f))
        for u in pu:
            b = by_id.get(u.id)
            if b is None:
                errors.append("%s: %s is not a unit of this module" % (os.path.basename(f), u.id))
                continue
            if (u.kind, u.ctx) != (b.kind, b.ctx):
                errors.append("%s: %s header changed (%s | %s) != (%s | %s) - copy the header exactly" % (
                    os.path.basename(f), u.id, u.kind, u.ctx, b.kind, b.ctx))
                continue
            if not u.text.strip():
                errors.append("%s: %s has empty text" % (os.path.basename(f), u.id))
                continue
            pending.append((u.id, u.text))
        pending_files = f
    if errors:
        print("MERGE FAILED (nothing written):")
        for e in errors:
            print("  ", e)
        return 1
    if not a.status:
        for uid, text in pending:
            by_id[uid].text = text
            merged += 1
        if files:
            shutil.copyfile(base_path, os.path.join(work, "units.bak"))
            write_units(base_path, header, units)
            os.makedirs(os.path.join(work, "applied"), exist_ok=True)
            stamp = time.strftime("%H%M%S")
            for f in files:
                shutil.move(f, os.path.join(work, "applied", stamp + "_" + os.path.basename(f)))
    same = [u.id for u in units if orig.get(u.id) == u.text]
    print("merged %d unit texts from %d file(s); %d of %d units still identical to the original%s" % (
        merged, len(files), len(same), len(units), " (status only)" if a.status else ""))
    if same and len(same) <= 25:
        print("unchanged:", " ".join(same))
    elif same:
        print("unchanged (first 25):", " ".join(same[:25]), "...")
    if files and not a.status and not a.no_check:
        # validate the merged texts the same way `apply` does (placeholders, HTML tags, % specifiers, numbers)
        import subprocess
        tool, target = ("ste_html_units.py", a.html) if a.html else ("ste_units.py", a.module)
        if not a.html and not (a.module.startswith(("paper_", "data.", "ipm_blueprint")) or "/" in a.module):
            return 0
        cmd = [sys.executable, os.path.join(HERE, tool), "apply", target, "--dry-run"]
        if a.work:
            cmd += ["--work", a.work]
        r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
        out = (r.stdout + r.stderr).strip()
        print("-- validation (apply --dry-run): %s" % ("OK" if r.returncode == 0 else "PROBLEMS - fix these before apply"))
        if out:
            print("   " + out.replace("\n", "\n   "))
        return 0 if r.returncode == 0 else 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
