# -*- coding: utf-8 -*-
"""Look up words in the ASD-STE100 Issue 9 dictionary data.

  python ste_lookup.py check test damage approximately       # status + alternatives
  python ste_lookup.py --entry follow                        # also print the dictionary page text
  python ste_lookup.py --alt big large quickly               # words -> approved alternatives only
  python ste_lookup.py --slug cloning mother root-zone       # use the TN/TV lists of one paper

Status lines:
  APPROVED       approved STE word (the part of speech shown is the ONLY one you may use)
  NOT-APPROVED   do not use; the alternatives are suggestions - check that the meaning fits
  TN / TV        technical noun / technical verb in the project lists (core, or the paper you chose with --slug)
  UNKNOWN        not in the dictionary: use an approved word, or (subject-field nouns/verbs only) list it.
For the approved MEANING of a word, always read its entry:  --entry <word>
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import ste_lint as SL  # noqa: E402

LAYOUT = os.path.join(HERE, "ref", "ASD-STE100_ISSUE9.layout.txt")


def entry_text(word, maxlines=28):
    """Raw dictionary page lines around the entry.  Columns: word | approved meaning / ALTERNATIVES |
    STE EXAMPLE | non-STE example.  Where several short entries are stacked, the meaning columns of the
    next entries follow below the headword lines."""
    if not os.path.exists(LAYOUT):
        return "(layout text not available)"
    lines = open(LAYOUT, encoding="utf-8", errors="replace").read().splitlines()
    pat = re.compile(r"^\s{0,3}" + re.escape(word) + r"\s*(\(|$|,)", re.I)
    i0 = next((i for i, l in enumerate(lines) if "Page 2-1-A1" in l), 0)
    out = []
    for i, l in enumerate(lines):
        if i > i0 and pat.match(l):
            out.append("--- dictionary page (columns: word | approved meaning/ALTERNATIVES | STE EXAMPLE | non-STE example)")
            out.extend(x[:170] for x in lines[max(i - 1, 0):i + maxlines])
            break
    return "\n".join(out) or "(entry text not found)"


def main(argv):
    if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
        sys.stdout.reconfigure(encoding="utf-8")
    entry = "--entry" in argv
    alt_only = "--alt" in argv
    slug = None
    if "--slug" in argv:
        k = argv.index("--slug")
        slug = argv[k + 1] if k + 1 < len(argv) else None
        argv = argv[:k] + argv[k + 2:]
    words = [a for a in argv if not a.startswith("--")]
    if not words:
        print(__doc__)
        return 2
    L = SL.lex(slug)
    mp = os.path.join(SL.DATA, "meanings.json")
    meanings = {}
    if os.path.exists(mp):
        import json
        meanings = json.load(open(mp, encoding="utf-8"))
    for w in words:
        w = w.lower()
        res = []
        if L.approved(w):
            pos = L.headwords.get(w)
            res.append("APPROVED %s%s" % (w, (" (" + "/".join(pos) + ")") if pos else " (inflected or derived form of an approved word)"))
            for p_, text in (meanings.get(w) or {}).items():
                res.append("   MEANING (%s): %s" % (p_, text))
        if w in L.not_approved:
            na = L.not_approved[w]
            res.append("NOT-APPROVED %s (%s) -> %s" % (w, "/".join(na["pos"]), ", ".join(na["alt"]) or "(no suggestion: recast the sentence)"))
        if L.is_tn(w):
            res.append("TN  %s  (technical noun list)" % w)
        if L.is_tv(w):
            res.append("TV  %s  (technical verb list)" % w)
        if "-" in w:
            c = SL.classify(w, L)
            res.append("hyphenated word: %s" % ("accepted by the linter" if c is None else
                                                 "rejected (%s: %s)" % (c[0], c[1] if isinstance(c[1], (list, str)) else "")))
        if not res:
            res.append("UNKNOWN %s: not in the dictionary and not listed as technical noun/verb" % w)
        if alt_only:
            na = L.not_approved.get(w)
            print("%s -> %s" % (w, ", ".join(na["alt"]) if na and na["alt"] else ("approved" if L.approved(w) else "(none)")))
            continue
        print("\n".join(res))
        if entry:
            print(entry_text(w))
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
