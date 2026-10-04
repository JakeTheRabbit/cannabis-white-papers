# -*- coding: utf-8 -*-
"""Structure/number/citation parity of a rewritten paper against its pristine baseline, plus STE lint.

  ste_verify.py baseline <module>|--all [--force]   snapshot of the ORIGINAL module (git 1de7cb2)
  ste_verify.py check <module> [--no-lint] [--level E|W] [--max N]

`check` fails (exit 1) when
  - section ids / order / block counts / HTML skeleton / figures / citations changed (E)
  - the STE linter reports an error
and warns about numbers that appear/disappear, and big word-count changes (W).
A block-level `<p>` may be split into several `<p>` (allowed); nothing else may change shape.
"""
import argparse
import hashlib
import importlib
import importlib.util
import json
import os
import re
import subprocess
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.dirname(HERE)
REPO = os.path.dirname(BUILD)
sys.path.insert(0, HERE)
sys.path.insert(0, BUILD)
BASE_COMMIT = "1de7cb2"
BASELINE_DIR = os.path.join(HERE, "baseline")
WORK = os.path.join(HERE, "work")

from ste_common import html_to_text  # noqa: E402

_NUM = re.compile(r"(?<![\w.])\d+(?:[.,]\d+)*")
_CITE_RE = re.compile(r"href=['\"]#ref-([^'\"]+)['\"]")
_SVG_RE = re.compile(r"<svg\b.*?</svg>", re.S)
_TAGS = re.compile(r"<(/?)([a-zA-Z][a-zA-Z0-9]*)([^>]*)>")


def _skeleton(html):
    """Tag/class skeleton of an HTML string; text collapsed to T; svg bodies collapsed."""
    h = _SVG_RE.sub("<svg/>", html)
    out = []
    pos = 0
    for m in _TAGS.finditer(h):
        if h[pos:m.start()].strip():
            out.append("T")
        pos = m.end()
        close, tag, attrs = m.group(1), m.group(2).lower(), m.group(3)
        if tag in ("strong", "em", "b", "i", "sup", "sub", "a", "span", "code", "abbr", "br", "mark", "small", "img"):
            continue          # inline markup is free
        cls = re.search(r"class=['\"]([^'\"]*)['\"]", attrs)
        out.append("<%s%s%s>" % (close, tag, ("." + ".".join(cls.group(1).split())) if (cls and not close) else ""))
    if h[pos:].strip():
        out.append("T")
    s = "".join(out)
    s = re.sub(r"(?:T)+", "T", s)
    # allow one paragraph to become several paragraphs
    s = re.sub(r"(<p(?:\.[\w.-]+)?>T</p>)(?:<p>T</p>)+", r"\1", s)
    return s


_SVG_TEXT = re.compile(r"(<(?:text|tspan|title|desc)\b[^>]*>)(.*?)(</(?:text|tspan|title|desc)>)", re.S)
_SVG_ARIA = re.compile(r"(aria-label=)(\"[^\"]*\"|'[^']*')")


def _svg_norm(svg):
    """SVG with its words removed: the drawing (shapes, positions, colours) must stay identical, the label
    text may change (labels are rewritten as prose).  The number of text elements still has to match."""
    s = _SVG_TEXT.sub(lambda m: m.group(1) + "~" + m.group(3), svg)
    return _SVG_ARIA.sub(lambda m: m.group(1) + '""', s)


def _numbers(text):
    return Counter(n.replace(",", "") for n in _NUM.findall(text))


_STOP_CAPS = {"the", "a", "an", "this", "that", "these", "those", "if", "when", "it", "you", "we", "they", "in", "on",
              "for", "to", "and", "but", "or", "so", "as", "at", "by", "with", "figure", "table", "note", "warning"}


def _terms(text):
    """Names, acronyms and hyphenated/compound subject words that a rewrite must not lose:
    capitalised words inside sentences, ALLCAPS/mixed-case acronyms, and words with digits."""
    out = set()
    for sent in re.split(r"(?<=[.!?])\s+", text):
        toks = re.findall(r"[A-Za-z][A-Za-z0-9µμ\-]*", sent)
        for i, t in enumerate(toks):
            if len(t) < 2:
                continue
            if (t.isupper() and len(t) >= 2) or (any(c.isdigit() for c in t) and any(c.isalpha() for c in t)):
                out.add(t.lower())
            # (capitalised names are not tracked: rewrites legitimately change case and word choice)
    return out


def signature(mod):
    sig = {
        "slug": getattr(mod, "SLUG", ""),
        "title": getattr(mod, "TITLE", ""),
        "related": list(getattr(mod, "RELATED", []) or []),
        "ref_ids": list(getattr(mod, "REF_IDS", []) or []),
        "meta_icons": [m[0] for m in getattr(mod, "META", []) or []],
        "n_meta": len(getattr(mod, "META", []) or []),
        "sections": [],
    }
    all_terms = set()
    for sec in getattr(mod, "SECTIONS", []):
        blocks = sec.get("blocks", [])
        html = "".join(blocks)
        text = html_to_text(re.sub(r"<svg\b.*?</svg>", " ", html, flags=re.S))
        bounded = re.sub(r"</(?:td|th|li|div|p|h\d|dd|dt|caption|figcaption|span)>|<br\s*/?>", ". ",
                         re.sub(r"<svg\b.*?</svg>", " ", html, flags=re.S))
        all_terms |= _terms(html_to_text(bounded))
        s = {
            "id": sec.get("id"),
            "kicker": sec.get("kicker", ""),
            "title": sec.get("title", ""),
            "n_blocks": len(blocks),
            "skeleton": [_skeleton(b) for b in blocks],
            "cites": sorted(_CITE_RE.findall(html)),
            "figures": [hashlib.sha1(_svg_norm(m).encode("utf-8")).hexdigest()[:12] for m in _SVG_RE.findall(html)],
            "images": sorted(re.findall(r"<img[^>]*src=['\"]([^'\"]+)['\"]", html)),
            "links": sorted(h for h in re.findall(r"<a\b[^>]*href=['\"]([^'\"]+)['\"]", html) if not h.startswith("#ref-")),
            "numbers": dict(_numbers(text)),
            "words": len(text.split()),
        }
        sig["sections"].append(s)
    sig["terms"] = sorted(all_terms)
    return sig


def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def original_source(module):
    r = subprocess.run(["git", "-C", REPO, "show", "%s:_build/%s.py" % (BASE_COMMIT, module)],
                       capture_output=True)
    if r.returncode != 0:
        raise SystemExit("cannot read %s from git %s: %s" % (module, BASE_COMMIT, r.stderr.decode()))
    return r.stdout


def cmd_baseline(modules, force):
    os.makedirs(BASELINE_DIR, exist_ok=True)
    for module in modules:
        out = os.path.join(BASELINE_DIR, module + ".json")
        if os.path.exists(out) and not force:
            print("baseline exists:", module)
            continue
        src = original_source(module)
        tmp = os.path.join(BUILD, "_orig_%s.py" % module)       # next to siblings so __file__-relative paths work
        try:
            with open(tmp, "wb") as fh:
                fh.write(src)
            mod = load_module(tmp, "_orig_" + module)
            sig = signature(mod)
        finally:
            if os.path.exists(tmp):
                os.remove(tmp)
            sys.modules.pop("_orig_" + module, None)
        json.dump(sig, open(out, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
        print("baseline:", module, "%d sections" % len(sig["sections"]))


def cmd_check(module, no_lint, level, maxn):
    base_path = os.path.join(BASELINE_DIR, module + ".json")
    if not os.path.exists(base_path):
        cmd_baseline([module], False)
    base = json.load(open(base_path, encoding="utf-8"))
    for k in list(sys.modules):
        if k == module:
            del sys.modules[k]
    mod = importlib.import_module(module)
    new = signature(mod)
    errs, warns = [], []

    for key in ("slug", "related", "ref_ids", "meta_icons"):
        if base[key] != new[key]:
            errs.append("%s changed: %r -> %r" % (key, base[key], new[key]))
    bs, ns = base["sections"], new["sections"]
    if [s["id"] for s in bs] != [s["id"] for s in ns]:
        errs.append("section ids/order changed: %r -> %r" % ([s["id"] for s in bs], [s["id"] for s in ns]))
    for b, n in zip(bs, ns):
        sid = b["id"]
        if b["n_blocks"] != n["n_blocks"]:
            errs.append("[%s] block count %d -> %d" % (sid, b["n_blocks"], n["n_blocks"]))
        else:
            for i, (x, y) in enumerate(zip(b["skeleton"], n["skeleton"])):
                if x != y:
                    errs.append("[%s] block %d changed shape:\n      was %s\n      now %s" % (sid, i, x[:160], y[:160]))
        if b["cites"] != n["cites"]:
            cb, cn = Counter(b["cites"]), Counter(n["cites"])
            errs.append("[%s] citations changed: lost %s, added %s" % (sid, dict(cb - cn), dict(cn - cb)))
        if b["figures"] != n["figures"]:
            errs.append("[%s] figure SVG changed (%d -> %d figures)" % (sid, len(b["figures"]), len(n["figures"])))
        if b["images"] != n["images"]:
            errs.append("[%s] images changed" % sid)
        if b.get("links") != n.get("links"):
            lb, ln = Counter(b.get("links", [])), Counter(n.get("links", []))
            warns.append("[%s] links to other pages changed: lost %s, added %s" % (sid, dict(lb - ln) or "-", dict(ln - lb) or "-"))
        nb, nn = Counter(b["numbers"]), Counter(n["numbers"])
        lost, added = nb - nn, nn - nb
        if lost or added:
            warns.append("[%s] numbers: lost %s | added %s" % (sid, dict(lost) or "-", dict(added) or "-"))
        if b["words"] >= 120 and not (0.55 <= n["words"] / b["words"] <= 3.0):
            warns.append("[%s] word count %d -> %d (check that no content was dropped)" % (sid, b["words"], n["words"]))
    if len(bs) != len(ns):
        errs.append("section count %d -> %d" % (len(bs), len(ns)))
    lost_terms = sorted(set(base.get("terms", [])) - set(new.get("terms", [])))
    if lost_terms:
        warns.append("names/acronyms in the original that no longer appear anywhere (%d): %s" % (
            len(lost_terms), ", ".join(lost_terms[:60])))

    print("== parity: %d errors, %d warnings (%s)" % (len(errs), len(warns), module))
    for e in errs[:maxn]:
        print("  E", e)
    for w in warns[:maxn]:
        print("  W", w)

    nE = 0
    if not no_lint:
        import ste_lint as SL
        units = SL.units_from_module(module)
        ns_ = argparse.Namespace(no_spacy=False, level=level, max=maxn, summary=False, words=True, json=False,
                                 slug=getattr(mod, "SLUG", None))
        findings, unknown = SL.run(units, ns_)
        nE = SL.report(units, findings, unknown, ns_)
    ok = (not errs) and nE == 0
    print("== RESULT:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("baseline")
    b.add_argument("module", nargs="?")
    b.add_argument("--all", action="store_true")
    b.add_argument("--force", action="store_true")
    c = sub.add_parser("check")
    c.add_argument("module")
    c.add_argument("--no-lint", action="store_true")
    c.add_argument("--level", default="E", choices=["E", "W"])
    c.add_argument("--max", type=int, default=60)
    a = ap.parse_args()
    if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
        sys.stdout.reconfigure(encoding="utf-8")
    if a.cmd == "baseline":
        if a.all:
            from build import PAPER_MODULES
            mods = [m for m in PAPER_MODULES if m not in ("paper_slab_irrigation", "paper_auckland_ipm_blueprint")]
        else:
            mods = [a.module]
        cmd_baseline(mods, a.force)
        return 0
    return cmd_check(a.module, a.no_lint, a.level, a.max)


if __name__ == "__main__":
    sys.exit(main())
