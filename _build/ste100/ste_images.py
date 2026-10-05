# -*- coding: utf-8 -*-
"""ste_images.py - text units of the photo manifest for the ASD-STE100 rewrite.

Target 1: _build/images.py     IMAGES[*]["caption"] and ["alt"], MODEL_LABEL values
Target 2: _build/_gen/embed_map.json   gallery term labels, sequence title / caption / frame labels

Never edited: "prompt" (image-generation prompt, not shown to readers), slug, n, sec, model, ar, res, ext.

  PY _build/ste100/ste_images.py extract [--force]   -> work/images/units.txt (+ meta.json, originals)
  PY _build/ste100/ste_images.py status
  PY _build/ste100/ste_images.py apply [--dry-run]    patches both files from the originals (idempotent)
  PY _build/ste100/ste_images.py selftest             extract+apply with no edits must be byte-identical

Units file = the same format as every ste_* tool (merge with:  ste_merge.py images ),
lint with:  ste_lint.py --units _build/ste100/work/images/units.txt   (no --slug: global lexicon)
"""
import argparse
import ast
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.dirname(HERE)
ROOT = os.path.dirname(BUILD)
WORK = os.path.join(HERE, "work", "images")
PY_FILE = os.path.join(BUILD, "images.py")
JSON_FILE = os.path.join(BUILD, "_gen", "embed_map.json")
sys.path.insert(0, HERE)
from ste_common import read_units, write_units, Unit  # noqa: E402

_TAG = re.compile(r"<[^>]+>")
_ENT = re.compile(r"&[#\w]+;")


def _line_starts(data):
    starts = [0]
    for m in re.finditer(rb"\n", data):
        starts.append(m.end())
    return starts


def _collect_py(data):
    """[(kind, ctx, byte_start, byte_end, text)] for images.py string literals."""
    tree = ast.parse(data.decode("utf-8"))
    starts = _line_starts(data)
    out = []

    def span(node):
        return starts[node.lineno - 1] + node.col_offset, starts[node.end_lineno - 1] + node.end_col_offset

    for node in tree.body:
        if isinstance(node, ast.AugAssign) and isinstance(node.target, ast.Name):
            name = node.target.id               # IMAGES += [ ... ]
        elif isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            name = node.targets[0].id
        else:
            continue
        if name == "IMAGES" and isinstance(node.value, ast.List):
            for d in node.value.elts:
                if not isinstance(d, ast.Dict):
                    continue
                kv = {k.value: v for k, v in zip(d.keys, d.values) if isinstance(k, ast.Constant)}
                slug = kv["slug"].value if "slug" in kv else "?"
                n = kv["n"].value if "n" in kv else "?"
                for key, kind in (("caption", "caption"), ("alt", "label")):
                    v = kv.get(key)
                    if isinstance(v, ast.Constant) and isinstance(v.value, str):
                        s, e = span(v)
                        out.append((kind, "py %s img=%s-%s" % (key, slug, n), s, e, v.value))
        elif name == "MODEL_LABEL" and isinstance(node.value, ast.Dict):
            for k, v in zip(node.value.keys, node.value.values):
                if isinstance(v, ast.Constant) and isinstance(v.value, str):
                    s, e = span(v)
                    out.append(("label", "py model=%s" % k.value, s, e, v.value))
    return out


def _collect_json(obj):
    """[(kind, ctx, path, text)] for embed_map.json (path = list of keys / indexes)."""
    out = []
    for slug, v in obj.items():
        for i, g in enumerate(v.get("gallery", [])):
            out.append(("label", "json gallery=%s" % slug, [slug, "gallery", i, 0], g[0]))
        for i, sq in enumerate(v.get("sequences", [])):
            if "title" in sq:
                out.append(("heading", "json sequence=%s title" % slug, [slug, "sequences", i, "title"], sq["title"]))
            if "caption" in sq:
                out.append(("caption", "json sequence=%s caption" % slug, [slug, "sequences", i, "caption"], sq["caption"]))
            for j, fr in enumerate(sq.get("frames", [])):
                out.append(("label", "json sequence=%s frame" % slug, [slug, "sequences", i, "frames", j, 0], fr[0]))
    return out


def _dump_json(obj, eol):
    return (json.dumps(obj, indent=1, ensure_ascii=False)).replace("\n", eol).encode("utf-8")


def _one_line(t):
    return re.sub(r"\s+", " ", t).strip()


def extract(force=False):
    os.makedirs(WORK, exist_ok=True)
    up = os.path.join(WORK, "units.txt")
    if os.path.exists(up) and not force:
        sys.exit("units.txt exists (edits are kept); use --force to re-extract from the files as they are now")
    pydata = open(PY_FILE, "rb").read()
    raw = open(JSON_FILE, "rb").read()
    eol = "\r\n" if b"\r\n" in raw else "\n"
    obj = json.loads(raw.decode("utf-8"))
    if _dump_json(obj, eol) != raw:
        sys.exit("embed_map.json does not round-trip byte-identically: stop")
    shutil.copyfile(PY_FILE, os.path.join(WORK, "images.original.py"))
    shutil.copyfile(JSON_FILE, os.path.join(WORK, "embed_map.original.json"))
    units, meta = [], []
    for kind, ctx, s, e, text in _collect_py(pydata):
        uid = "U%04d" % (len(units) + 1)
        units.append(Unit(uid, kind, ctx, _one_line(text)))
        meta.append({"id": uid, "src": "py", "start": s, "end": e, "text": text})
    for kind, ctx, path, text in _collect_json(obj):
        uid = "U%04d" % (len(units) + 1)
        units.append(Unit(uid, kind, ctx, _one_line(text)))
        meta.append({"id": uid, "src": "json", "path": path, "text": text})
    header = ["# ste-units v1 | module: images | slug: ?",
              "# source: _build/images.py + _build/_gen/embed_map.json | units: %d" % len(units),
              "# Edit ONLY the text line under each '@@' header and keep it on ONE line. Never edit '@@' lines.",
              "# caption = text under a photo, label = alt text / short label. Keep inline HTML and entities as they are.",
              "# Lint with the GLOBAL lexicon (no --slug): the photos belong to 37 papers.",
              ""]
    write_units(up, header, units)
    json.dump(meta, open(os.path.join(WORK, "meta.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    print("extracted %d units -> %s" % (len(units), up))
    from collections import Counter
    print("  by kind:", dict(Counter(u.kind for u in units)))


def _validate(units, meta):
    errs, warns = [], []
    byid = {m["id"]: m for m in meta}
    seen = set()
    for u in units:
        if u.id in seen:
            errs.append("%s: duplicate id" % u.id)
        seen.add(u.id)
        m = byid.get(u.id)
        if not m:
            errs.append("%s: unknown unit" % u.id)
            continue
        old = _one_line(m["text"])
        if not u.text.strip():
            errs.append("%s: empty text" % u.id)
            continue
        if sorted(_TAG.findall(old)) != sorted(_TAG.findall(u.text)):
            errs.append("%s: HTML tags changed" % u.id)
        if sorted(_ENT.findall(old)) != sorted(_ENT.findall(u.text)):
            warns.append("%s: entities changed" % u.id)
        if "\n" in u.text:
            errs.append("%s: newline in text" % u.id)
        if u.kind == "label" and len(u.text) > 1.5 * max(len(old), 20):
            warns.append("%s: label is longer than 150%% of the original" % u.id)
    for m in meta:
        if m["id"] not in seen:
            errs.append("%s: unit missing from units.txt" % m["id"])
    return errs, warns


def _set_path(obj, path, value):
    for k in path[:-1]:
        obj = obj[k]
    obj[path[-1]] = value


def build(units, meta):
    """-> (py_bytes, json_bytes) built from the saved originals plus the edited units."""
    pydata = open(os.path.join(WORK, "images.original.py"), "rb").read()
    raw = open(os.path.join(WORK, "embed_map.original.json"), "rb").read()
    eol = "\r\n" if b"\r\n" in raw else "\n"
    obj = json.loads(raw.decode("utf-8"))
    byid = {u.id: u for u in units}
    edits = []
    for m in meta:
        u = byid[m["id"]]
        if u.text == _one_line(m["text"]):
            continue
        if m["src"] == "py":
            edits.append((m["start"], m["end"], json.dumps(u.text, ensure_ascii=False).encode("utf-8")))
        else:
            _set_path(obj, m["path"], u.text)
    for s, e, lit in sorted(edits, reverse=True):
        pydata = pydata[:s] + lit + pydata[e:]
    return pydata, _dump_json(obj, eol)


def apply(dry=False):
    units = read_units(os.path.join(WORK, "units.txt"))[1]
    meta = json.load(open(os.path.join(WORK, "meta.json"), encoding="utf-8"))
    errs, warns = _validate(units, meta)
    for w in warns:
        print("warning:", w)
    if errs:
        for e in errs:
            print(e)
        sys.exit(2)
    pydata, jdata = build(units, meta)
    tmp = tempfile.mkdtemp(prefix="ste_images_")
    try:
        tp = os.path.join(tmp, "images.py")
        open(tp, "wb").write(pydata)
        r = subprocess.run([sys.executable, "-c",
                            "import importlib.util as u,sys;s=u.spec_from_file_location('im',sys.argv[1]);m=u.module_from_spec(s);"
                            "s.loader.exec_module(m);print(len(m.IMAGES))", tp], capture_output=True, text=True)
        if r.returncode:
            print("images.py does not import:", r.stderr[-400:])
            sys.exit(3)
        json.loads(jdata.decode("utf-8"))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    changed = sum(1 for u, m in zip(units, meta) if u.text != _one_line(m["text"]))
    if dry:
        print("dry run OK: %d units changed, nothing written" % changed)
        return
    cur = open(PY_FILE, "rb").read()
    last = os.path.join(WORK, "last_applied.images.py")
    open(last, "wb").write(cur)
    open(PY_FILE, "wb").write(pydata)
    open(JSON_FILE, "wb").write(jdata)
    print("applied: %d of %d units changed" % (changed, len(units)))


def status():
    units = read_units(os.path.join(WORK, "units.txt"))[1]
    meta = json.load(open(os.path.join(WORK, "meta.json"), encoding="utf-8"))
    errs, warns = _validate(units, meta)
    changed = sum(1 for u, m in zip(units, meta) if u.text != _one_line(m["text"]))
    print("%d units, %d edited, %d errors, %d warnings" % (len(units), changed, len(errs), len(warns)))
    for e in errs[:20]:
        print(" ", e)


def selftest():
    if not os.path.exists(os.path.join(WORK, "units.txt")):
        extract()
    units = read_units(os.path.join(WORK, "units.txt"))[1]
    meta = json.load(open(os.path.join(WORK, "meta.json"), encoding="utf-8"))
    # no edits -> identical bytes
    pydata, jdata = build([Unit(u.id, u.kind, u.ctx, _one_line(m["text"])) for u, m in zip(units, meta)], meta)
    ok1 = pydata == open(os.path.join(WORK, "images.original.py"), "rb").read()
    ok2 = jdata == open(os.path.join(WORK, "embed_map.original.json"), "rb").read()
    print("selftest: images.py identical:", ok1, "| embed_map.json identical:", ok2)
    sys.exit(0 if ok1 and ok2 else 1)


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p1 = sub.add_parser("extract"); p1.add_argument("--force", action="store_true")
    sub.add_parser("status")
    p3 = sub.add_parser("apply"); p3.add_argument("--dry-run", action="store_true")
    sub.add_parser("selftest")
    a = ap.parse_args()
    if a.cmd == "extract":
        extract(a.force)
    elif a.cmd == "status":
        status()
    elif a.cmd == "apply":
        apply(a.dry_run)
    else:
        selftest()
