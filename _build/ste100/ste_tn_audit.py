# -*- coding: utf-8 -*-
"""Audit the technical-noun / technical-verb lists that rewriting agents added.

  ste_tn_audit.py            list per-paper additions, flag doubtful ones
  ste_tn_audit.py --promote  merge all per-paper lists (except core) into data/tn_promoted.txt / tv_promoted.txt
                             (dedup; flagged words are NOT promoted)

Flags:
  GENERAL   common English word (Zipf >= 4.4) that is not in tn_core*: usually not a technical noun (Rule 1.5)
  ALT       the dictionary lists approved alternatives for it (try those first)
  APPROVED  the word is already an approved STE word
  JARGON    slang/jargon list (Rule 1.10)
"""
import glob
import os
import sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import ste_lint as SL  # noqa: E402

JARGON = {"veg", "flip", "dehu", "temp", "rh", "hlvd", "dryback", "flower", "gear", "stuff", "bud", "buds",
          "cola", "nug", "nugs", "chop", "dank", "sticky", "frosty", "cure"}
JARGON_OK = {"dryback", "cola", "bud", "buds", "cure"}      # defined technical terms in this subject field


def read(path):
    return SL._read_list(path)


def main():
    if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
        sys.stdout.reconfigure(encoding="utf-8")
    promote = "--promote" in sys.argv
    try:
        from wordfreq import zipf_frequency
    except Exception:
        zipf_frequency = lambda w, l: 0.0  # noqa: E731
    L = SL.lex()
    core = set()
    for f in glob.glob(os.path.join(SL.DATA, "tn_core*.txt")) + glob.glob(os.path.join(SL.DATA, "tv_core*.txt")):
        core.update(read(f))
    seen = defaultdict(list)
    for kind in ("tn", "tv"):
        for f in sorted(glob.glob(os.path.join(SL.DATA, kind + "_*.txt"))):
            name = os.path.basename(f)[len(kind) + 1:-4]
            if name.startswith("core") or name == "promoted":
                continue
            for w in read(f):
                seen[(kind, w)].append(name)
    flagged, ok = [], []
    for (kind, w), papers in sorted(seen.items()):
        flags = []
        if w in core:
            continue
        z = zipf_frequency(w.split()[0], "en") if " " not in w else 0
        if " " not in w and z >= 4.4:
            flags.append("GENERAL(z=%.1f)" % z)
        if " " not in w and w in L.not_approved and L.not_approved[w]["alt"]:
            flags.append("ALT:" + "/".join(L.not_approved[w]["alt"][:3]))
        if " " not in w and w in L.forms:
            flags.append("APPROVED")
        if w in JARGON and w not in JARGON_OK:
            flags.append("JARGON")
        (flagged if flags else ok).append((kind, w, papers, flags))
    print("== %d additions: %d flagged, %d ok" % (len(seen), len(flagged), len(ok)))
    for kind, w, papers, flags in flagged:
        print("  %s %-28s %-40s %s" % (kind.upper(), w, " ".join(flags), ",".join(papers)))
    print("\nOK additions:")
    print("  " + ", ".join("%s%s" % (w, "*" if len(p) > 1 else "") for k, w, p, f in ok))
    if promote:
        for kind in ("tn", "tv"):
            words = sorted({w for k, w, p, f in ok if k == kind})
            path = os.path.join(SL.DATA, "%s_promoted.txt" % kind)
            with open(path, "w", encoding="utf-8") as fh:
                fh.write("# promoted from per-paper lists by ste_tn_audit.py\n" + "\n".join(words) + "\n")
            print("wrote", path, len(words))


if __name__ == "__main__":
    main()
