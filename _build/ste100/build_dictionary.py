# -*- coding: utf-8 -*-
"""Build data/ste_words.json from the ASD-STE100 Issue 9 PDF (column 1 of the dictionary).

The PDF is copyrighted by ASD and stays local (ref/, gitignored). Only the word list is
derived: approved word forms, approved headword parts of speech, and not-approved words
with suggested alternatives. No definitions or examples are copied.

Usage:  python build_dictionary.py [path/to/ASD-STE100_ISSUE9.pdf]

Cross-checks printed at the end:
  - approved headword count vs the 875 that the specification states
  - every verb in the specification's "List of approved verbs" is present
"""
import json
import os
import re
import sys

import pdfplumber

HERE = os.path.dirname(os.path.abspath(__file__))
PDF = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "ref", "ASD-STE100_ISSUE9.pdf")
LAYOUT = os.path.join(HERE, "ref", "ASD-STE100_ISSUE9.layout.txt")
PROBELABS = os.path.join(HERE, "ref", "probelabs_ste100.json")   # alternatives hints only
OUT = os.path.join(HERE, "data", "ste_words.json")

POSMAP = {"n": "noun", "v": "verb", "adj": "adjective", "adv": "adverb", "prep": "preposition",
          "pron": "pronoun", "art": "article", "conj": "conjunction"}
POS_TOKEN = re.compile(r"^\((n|v|adj|adv|prep|pron|art|conj)\),?$")


def is_upper(s):
    letters = [c for c in s if c.isalpha()]
    return bool(letters) and all(c.isupper() for c in letters)


def col1_tokens(page):
    toks = [w for w in page.extract_words(extra_attrs=["fontname"], keep_blank_chars=False)
            if w["x0"] < 156 and 88 < w["top"] < 716 and "Bold" in w["fontname"]]
    toks.sort(key=lambda w: (round(w["top"] / 2.5), w["x0"]))
    return [w["text"] for w in toks]


def join_hyphen_splits(tokens):
    """electromag- netic -> electromagnetic (a soft line break inside a headword)."""
    out = []
    i = 0
    while i < len(tokens):
        t = tokens[i]
        if t.endswith("-") and len(t) > 3 and i + 1 < len(tokens) and tokens[i + 1].isalpha():
            out.append(t[:-1] + tokens[i + 1])
            i += 2
        else:
            out.append(t)
            i += 1
    return out


def main():
    pdf = pdfplumber.open(PDF)
    start = next(i for i, p in enumerate(pdf.pages) if "Page 2-1-A1" in (p.extract_text() or ""))
    tokens = []
    for pi in range(start, len(pdf.pages)):
        tokens += col1_tokens(pdf.pages[pi])
    tokens = join_hyphen_splits(tokens)

    approved_tokens = set()       # every upper-case word form seen in column 1
    heads = []                    # (word, pos, approved)
    cur = []
    in_also = False
    for t in tokens:
        if t == "(also":
            in_also = True
            continue
        if in_also:
            if t.endswith(")"):
                in_also = False
            w = t.strip("(),")
            if w:
                approved_tokens.add(w.lower())
            continue
        m = POS_TOKEN.match(t)
        if m:
            head = " ".join(cur).strip(" ,")
            cur = []
            if head:
                heads.append((head, POSMAP[m.group(1)]))
            continue
        w = t.strip("(),")
        if is_upper(w) and len(w) > 0:
            approved_tokens.add(w.lower())
        cur.append(t.strip(","))
    # Build headword tables. A run of tokens before a POS tag is: [verb forms of the previous
    # entry ...] + headword. Approved multi-word headwords are few and listed here.
    KNOWN_PHRASES = {"adjacent to", "aft of", "away from", "because of", "come on", "downstream of",
                     "each other", "forward of", "go off", "in front of", "in progress", "inboard of",
                     "make sure", "out of", "outboard of", "put on", "upstream of", "as ... as"}
    approved, unapproved = {}, {}
    for head, pos in heads:
        parts = [p for p in head.replace("(", " ").replace(")", " ").split() if p]
        if not parts:
            continue
        if is_upper(parts[-1]):
            # approved: last token, or a known multi-word phrase at the end
            word = parts[-1].lower()
            for n in (3, 2):
                cand = " ".join(parts[-n:]).lower()
                if len(parts) >= n and cand in KNOWN_PHRASES:
                    word = cand
                    break
            appr = True
        else:
            # not approved: the trailing lower-case run is the headword
            run = []
            for p in reversed(parts):
                if is_upper(p):
                    break
                run.append(p)
            run.reverse()
            word = " ".join(run).lower()
            appr = False
            if not word:
                continue
        word = re.sub(r"\s+", " ", word).strip(" ,")
        if not word or not any(c.isalpha() for c in word):
            continue
        (approved if appr else unapproved).setdefault(word, set()).add(pos)

    # alternatives for not-approved words (hints from the open probelabs extraction)
    alts = {}
    if os.path.exists(PROBELABS):
        for e in json.load(open(PROBELABS, encoding="utf-8"))["entries"]:
            if not e.get("approved") and e.get("alternatives"):
                alts.setdefault(e["word"].lower(), []).extend(e["alternatives"])

    # approved single-word forms
    forms = set(approved_tokens)
    for w in approved:
        for piece in w.split():
            forms.add(piece)
    forms.discard("")
    # numbers written as words and similar are technical nouns, handled by the linter.

    phrases = sorted(w for w in approved if " " in w)
    data = {
        "source": "ASD-STE100 Issue 9, 2025-01-15 (word list derived for checking only)",
        "approved_forms": sorted(forms),
        "approved_headwords": {w: sorted(p) for w, p in sorted(approved.items())},
        "approved_phrases": phrases,
        "not_approved": {w: {"pos": sorted(p), "alt": sorted(set(alts.get(w, [])))}
                         for w, p in sorted(unapproved.items())},
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump(data, open(OUT, "w", encoding="utf-8"), indent=1, ensure_ascii=False)

    # cross-checks
    n_app = sum(len(p) for p in approved.values())
    n_un = sum(len(p) for p in unapproved.values())
    print("approved headword+pos entries:", n_app, "(spec states 875)")
    print("not-approved headword+pos entries:", n_un, "(spec states 1274)")
    print("approved forms:", len(forms), " not-approved words:", len(unapproved))
    if os.path.exists(LAYOUT):
        lines = open(LAYOUT, encoding="utf-8", errors="replace").read().splitlines()
        i0 = next(i for i, l in enumerate(lines) if l.strip() == "List of approved verbs")
        verbs = set()
        for l in lines[i0 + 3:i0 + 60]:
            if l.strip().startswith("Issue 9"):
                break
            for cell in re.split(r"\s{2,}", l.strip()):
                if cell and len(cell) > 1 and cell.isupper():
                    verbs.add(cell.lower())
        missing = sorted(v for v in verbs if v not in forms and v.split()[0] not in forms)
        print("approved-verb table words:", len(verbs), " missing from forms:", missing)


if __name__ == "__main__":
    main()
