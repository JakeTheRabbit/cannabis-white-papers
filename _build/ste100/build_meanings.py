# -*- coding: utf-8 -*-
"""Build data/meanings.json: the approved MEANING (dictionary column 2) of each approved headword.

Reads the local copy of the ASD-STE100 Issue 9 PDF (ref/, not committed) and writes a small lookup file
(gitignored with the other derived dictionary data).  Used by ste_lookup.py so that a writer can see the
approved meaning of a word before using it (Rules 1.3 and 9.2).

Method: for every approved headword (bold, upper case, left column) take the text in the second column
that starts at the headword's line; keep the first text block (blocks are separated by a vertical gap) plus a
following block that starts with '2.' / 'For other meanings'.
"""
import json
import os
import re
import sys

import pdfplumber

HERE = os.path.dirname(os.path.abspath(__file__))
PDF = os.path.join(HERE, "ref", "ASD-STE100_ISSUE9.pdf")
OUT = os.path.join(HERE, "data", "meanings.json")
POS = re.compile(r"^\((n|v|adj|adv|prep|pron|art|conj)\),?$")
POSNAME = {"n": "noun", "v": "verb", "adj": "adjective", "adv": "adverb", "prep": "preposition",
           "pron": "pronoun", "art": "article", "conj": "conjunction"}


def main():
    pdf = pdfplumber.open(PDF)
    start = next(i for i, p in enumerate(pdf.pages) if "Page 2-1-A1" in (p.extract_text() or ""))
    out = {}
    for pi in range(start, len(pdf.pages)):
        page = pdf.pages[pi]
        words = page.extract_words(extra_attrs=["fontname"], keep_blank_chars=False)
        col1 = [w for w in words if w["x0"] < 156 and 88 < w["top"] < 716 and "Bold" in w["fontname"]]
        col1.sort(key=lambda w: (round(w["top"] / 2.5), w["x0"]))
        col2 = [w for w in words if 156 <= w["x0"] < 286 and 88 < w["top"] < 716 and "Bold" not in w["fontname"]]
        col2.sort(key=lambda w: (round(w["top"]), w["x0"]))
        lines = {}
        for c in col2:
            lines.setdefault(round(c["top"]), []).append(c["text"])
        tops = sorted(lines)
        for i, w in enumerate(col1):
            t = w["text"]
            if not (t.isupper() and t.isalpha()):
                continue
            nxt = next((x for x in col1[i + 1:i + 3] if POS.match(x["text"])), None)
            if nxt is None:
                continue
            y0 = w["top"] - 3
            blocks, cur, last = [], [], None
            for top in tops:
                if top < y0:
                    continue
                if top > y0 + 110:
                    break
                s = " ".join(lines[top])
                if last is not None and top - last > 15:       # vertical gap = new block
                    blocks.append(cur)
                    cur = []
                last = top
                if s.isupper() or re.fullmatch(r"[A-Z ()/,\-\[\]]+", s):
                    cur.append("[alt: %s]" % s)
                else:
                    cur.append(s)
            if cur:
                blocks.append(cur)
            keep = []
            for bi, b in enumerate(blocks[:3]):
                text = " ".join(b)
                if bi == 0 or re.match(r"^(2\.|For other|Use this|Do not)", text):
                    keep.append(text)
            meaning = re.sub(r"\s+", " ", " ".join(keep)).strip()
            pos = POSNAME[POS.match(nxt["text"]).group(1)]
            key = t.lower()
            if meaning:
                out.setdefault(key, {})[pos] = meaning[:420]
    json.dump(out, open(OUT, "w", encoding="utf-8"), indent=0, ensure_ascii=False)
    print("meanings for", len(out), "approved headwords ->", OUT)


if __name__ == "__main__":
    main()
