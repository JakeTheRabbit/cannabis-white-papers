# -*- coding: utf-8 -*-
"""ste_aria.py - the aria-label text of the SVG figures, for the ASD-STE100 rewrite.

`ste_units.py --svg-text` copies the text drawn INSIDE an SVG; it does not copy the aria-label
attribute of the <svg> element (the text a screen reader speaks).  This tool does.

Sources scanned (literal text only; `{expr}` and f-string holes are skipped):
    _build/*.py        string literals that contain  aria-label="..."  or  aria-label='...'
    _build/figs_*.json SVG strings that contain  aria-label="..."

  PY _build/ste100/ste_aria.py extract [--force]   -> work/aria/units.txt (+ meta.json)
  PY _build/ste100/ste_aria.py status
  PY _build/ste100/ste_aria.py apply [--dry-run]   exact substitution in the CURRENT files, so edits made
                                                   to the same files by other tools are kept
  PY _build/ste100/ste_aria.py selftest            apply with no edits must change nothing

Units file = the usual format (merge with  ste_merge.py aria --no-check ; lint with
ste_lint.py --units _build/ste100/work/aria/units.txt --slug ALL).  kind = `caption` (a description
sentence or two), ctx = `file=<name> n=<k>`.

New text rules checked by `apply`: no  "  '  <  >  {  }  \\  characters ; `&` only as an entity
(&amp; &deg; ...) ; not empty ; one line.
"""
import argparse
import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.dirname(HERE)
WORK = os.path.join(HERE, "work", "aria")
sys.path.insert(0, HERE)
from ste_common import read_units, write_units, Unit  # noqa: E402

PAT_DQ = re.compile(r'aria-label\s*=\s*(\\?)"([^"\\{}]*)\1"')
PAT_SQ = re.compile(r"aria-label\s*=\s*(\\?)'([^'\\{}]*)\1'")
BAD = re.compile(r"[\"'<>{}\\]|&(?!#?\w+;)")


def sources():
    out = []
    for f in sorted(glob.glob(os.path.join(BUILD, "*.py"))):
        if os.path.basename(f) in ("shell.py",):          # chrome strings: done by hand
            continue
        out.append(f)
    out += sorted(glob.glob(os.path.join(BUILD, "figs_*.json")))
    return out


def _find(path):
    """[(text, count)] for each distinct literal aria-label text in the file as it is now."""
    raw = open(path, encoding="utf-8", errors="replace").read()
    if path.endswith(".json"):
        try:
            obj = json.loads(raw)
        except Exception:
            return []
        strings = []

        def walk(o):
            if isinstance(o, str):
                strings.append(o)
            elif isinstance(o, dict):
                for v in o.values():
                    walk(v)
            elif isinstance(o, list):
                for v in o:
                    walk(v)
        walk(obj)
        raw = "\n".join(strings)
    found = {}
    for pat in (PAT_DQ, PAT_SQ):
        for m in pat.finditer(raw):
            t = m.group(2)
            if t.strip() and re.search(r"[A-Za-z]{3,}", t):
                found[t] = found.get(t, 0) + 1
    return sorted(found.items(), key=lambda kv: raw.find(kv[0]))


def extract(force=False):
    os.makedirs(WORK, exist_ok=True)
    up = os.path.join(WORK, "units.txt")
    if os.path.exists(up) and not force:
        sys.exit("units.txt exists (edits are kept); use --force to re-extract from the files as they are now")
    units, meta = [], []
    for path in sources():
        name = os.path.basename(path)
        for k, (text, n) in enumerate(_find(path), 1):
            uid = "U%04d" % (len(units) + 1)
            units.append(Unit(uid, "caption", "file=%s n=%d" % (name, k), text))
            meta.append({"id": uid, "file": name, "text": text, "count": n})
    header = ["# ste-units v1 | module: aria | slug: ?",
              "# source: aria-label attributes of the SVG figures | units: %d" % len(units),
              "# Edit ONLY the text line under each '@@' header and keep it on ONE line. Never edit '@@' lines.",
              "# Each text describes a figure for a screen reader: 1 to 3 short sentences (max 25 words each), approved",
              "# words / technical nouns, same facts, same numbers. No quotes, <, >, braces or backslashes.",
              "# Use the terms of the paper the figure belongs to (read the figure file / the paper). Lint: --slug ALL.",
              ""]
    write_units(up, header, units)
    json.dump(meta, open(os.path.join(WORK, "meta.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    print("extracted %d aria-label texts from %d files -> %s" % (len(units), len(set(m["file"] for m in meta)), up))


def _validate(units, meta):
    errs = []
    byid = {m["id"]: m for m in meta}
    for u in units:
        m = byid.get(u.id)
        if not m:
            errs.append("%s: unknown unit" % u.id)
            continue
        if u.text == m["text"]:
            continue                      # unchanged units are not checked
        if not u.text.strip():
            errs.append("%s: empty" % u.id)
        elif BAD.search(u.text):
            errs.append("%s: forbidden character (quote, <, >, brace, backslash or bare &) in: %s" % (u.id, u.text[:60]))
    return errs


def _json_roundtrip(raw):
    obj = json.loads(raw)
    eol = "\r\n" if "\r\n" in raw else "\n"
    for kw in (dict(indent=1, ensure_ascii=False), dict(indent=1, ensure_ascii=True),
               dict(indent=2, ensure_ascii=False), dict(indent=2, ensure_ascii=True),
               dict(indent=None, ensure_ascii=False), dict(indent=None, ensure_ascii=True),
               dict(indent=None, ensure_ascii=False, separators=(",", ":")),
               dict(indent=None, ensure_ascii=True, separators=(",", ":"))):
        for tail in ("", "\n"):
            if json.dumps(obj, **kw).replace("\n", eol) + tail == raw:
                return obj, kw, tail, eol
    return obj, None, "", eol


def apply(dry=False):
    units = read_units(os.path.join(WORK, "units.txt"))[1]
    meta = json.load(open(os.path.join(WORK, "meta.json"), encoding="utf-8"))
    errs = _validate(units, meta)
    if errs:
        print("\n".join(errs))
        sys.exit(2)
    byfile = {}
    for u, m in zip(units, meta):
        if u.text != m["text"]:
            byfile.setdefault(m["file"], []).append((m["text"], u.text))
    done = skipped = 0
    for name, pairs in sorted(byfile.items()):
        path = os.path.join(BUILD, name)
        raw = open(path, "rb").read().decode("utf-8")
        if name.endswith(".json"):
            out = raw
            for old, new in pairs:
                hit = False
                for ascii_only in (False, True):
                    eo = json.dumps(old, ensure_ascii=ascii_only)[1:-1]
                    en = json.dumps(new, ensure_ascii=ascii_only)[1:-1]
                    for q in ('\\"', "'"):                      # aria-label=\"...\" inside a JSON string, or '...'
                        a_ = "aria-label=" + q + eo + q
                        b_ = "aria-label=" + q + en + q
                        if a_ in out:
                            out = out.replace(a_, b_)
                            done += 1
                            hit = True
                if not hit:
                    skipped += 1
                    print("%s: text not found now (already changed?): %s" % (name, old[:60]))
            if not dry:
                json.loads(out)
                open(path, "wb").write(out.encode("utf-8"))
        else:
            out = raw
            for old, new in pairs:
                hit = False
                for q in ('"', "'"):
                    for bs in ("", "\\"):
                        a = "aria-label=%s%s%s%s" % (bs, q, old, bs + q if False else q)
                        a = "aria-label=" + bs + q + old + bs + q
                        b = "aria-label=" + bs + q + new + bs + q
                        if a in out:
                            out = out.replace(a, b)
                            done += 1
                            hit = True
                if not hit:
                    skipped += 1
                    print("%s: text not found now (already changed?): %s" % (name, old[:60]))
            if not dry:
                open(path, "wb").write(out.encode("utf-8"))
                import subprocess
                r = subprocess.run([sys.executable, "-m", "py_compile", path]).returncode
                if r:
                    print("py_compile FAILED for %s: restore it from git or last_applied before you go on" % name)
                    sys.exit(3)
    print(("dry run: " if dry else "") + "%d substitution(s) in %d file(s); %d skipped" % (done, len(byfile), skipped))


def status():
    units = read_units(os.path.join(WORK, "units.txt"))[1]
    meta = json.load(open(os.path.join(WORK, "meta.json"), encoding="utf-8"))
    errs = _validate(units, meta)
    ch = sum(1 for u, m in zip(units, meta) if u.text != m["text"])
    print("%d units, %d edited, %d errors" % (len(units), ch, len(errs)))
    for e in errs[:20]:
        print(" ", e)


def selftest():
    if not os.path.exists(os.path.join(WORK, "units.txt")):
        extract()
    apply(dry=True)
    print("selftest ok")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p1 = sub.add_parser("extract"); p1.add_argument("--force", action="store_true")
    sub.add_parser("status")
    p3 = sub.add_parser("apply"); p3.add_argument("--dry-run", action="store_true")
    sub.add_parser("selftest")
    a = ap.parse_args()
    {"extract": lambda: extract(a.force), "status": status, "apply": lambda: apply(a.dry_run), "selftest": selftest}[a.cmd]()
