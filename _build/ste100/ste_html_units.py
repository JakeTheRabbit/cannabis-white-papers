# -*- coding: utf-8 -*-
"""Text units of an HTML file, for the ASD-STE100 rewrite.  Python 3 stdlib + ste_common.py only.

Agents may edit ONLY the human-readable text of an HTML page.  This tool pulls that text out into a
units file (same format as every other ste_* tool) and later writes the edited units back into the
exact byte spans they came from.  Markup, scripts, styles, SVG, comments and every other byte of
the file stay exactly as they are.

  PY = python    (any Python 3)
  PY _build/ste100/ste_html_units.py extract <html-file> [--work DIR] [--scope body|main|article|all] [--force]
  PY _build/ste100/ste_html_units.py apply    <html-file> [--work DIR] [--dry-run] [--force]
  PY _build/ste100/ste_html_units.py status   <html-file> [--work DIR]
  PY _build/ste100/ste_html_units.py selftest <html-file>... | --all-defaults

Paths: a relative <html-file> is tried against the repo root first, then the current directory.
--work DIR is the BASE folder (default _build/ste100/work; a relative DIR is relative to the repo root);
files go to DIR/<stem>/ where <stem> is the file name without extension (reading-the-root-zone,
slab_irrigation_content ...).

extract   Writes DIR/<stem>/units.txt, meta.json (per unit: id, kind, ctx, byte start/end of the inner
          HTML in the ORIGINAL file, original text) and original.html (a copy).  Prints unit counts per
          kind.  Run again on an unchanged file: nothing is touched (your edits in units.txt survive).
          If the file has changed since (applied edits, regeneration) or --scope differs, extract refuses
          (exit 3) unless --force, which re-extracts from the file as it is now and discards units.txt edits.
          --scope body (default): <title>/<meta> in <head> + everything in <body> (a fragment with no
          <body> counts as all body).  main / article: only inside <main> / <article>.  all: whole file.
apply     Validates units.txt, then rebuilds the file from original.html + the meta spans (so it is
          idempotent), replacing only the spans whose text changed.  Writes the file byte-exactly and
          keeps last_applied.html.  Putting every unit back to its extracted text and running apply
          restores the original bytes.  --dry-run validates and reports, writes nothing.  Exit codes:
          0 ok, 1 usage/IO error, 2 validation failed (list of "U0012: message", nothing written),
          3 the target file changed since extract/apply (use --force to overwrite anyway).
          LF/CRLF differences do not count as a change (git core.autocrlf rewrites working copies on
          checkout): apply keeps the line-ending style the file has now.
status    Work-folder state, edited units, validation result, whether the file equals the original.
selftest  Proves losslessness on scratch copies (never touches the real file; scratch is
          _build/ste100/work/html_selftest_<stem>/ and is removed on PASS):
            (a) extract -> apply with no edits gives the file back byte for byte;
            (b) force-rewrite every unit with its own (decoded) text, bytes identical;
            (c) html.parser start/end tag sequences (names + attributes) identical;
            (d) edit round-trip: every unit text edited (letters only), applied, tag sequence identical,
                re-extract returns exactly the edited texts, bytes outside the spans identical,
                second apply identical, restoring the texts restores the original bytes;
            (e) the file is flipped LF<->CRLF (what `git checkout` does under core.autocrlf=true):
                extract still says "already extracted", apply is accepted and keeps the new style.
          --all-defaults = reading-the-root-zone.html, FACT-CHECK-REVIEW.html,
          _build/data/slab_irrigation_content.html.

UNITS FILE  ("# ste-units v1 | file: <name>" then "@@ U0001 | <kind> | <ctx>" + ONE line of text)
  The text is the RAW inner HTML of the element: entities (&times; &mdash;) and inline tags (<strong>,
  <em>, <a ...>, <sup class="cite">..</sup>, <br>, <code>) are kept as written.  A newline inside a unit
  is written as the token  ⟦nl⟧  (CRLF files: ⟦nl⟧ = CRLF; the rare other forms are ⟦lf⟧ ⟦crlf⟧ ⟦cr⟧).
  Units are the inner HTML of text containers with no block-level descendants: p li td th caption
  figcaption h1-h6 dt dd summary blockquote label, and div/span with class ctitle defn-t defn-b step-t
  step-b card-title card-body card-tag kv-k kv-v stagetitle stagedur stagecard-b sec-kicker kicker
  eyebrow lead sub chip fignum meta-pill hero-sub note cbody-text; <title> (ctx "<title>"); the
  content="" value of <meta name=description>, og:title, og:description, twitter:title,
  twitter:description (kind meta, ctx "<meta name=description>" ...); and kind text = direct text
  between block children of a non-unit container (>= 2 words; a lone link or pill is unwrapped, a list
  of links/pills gives one unit each; one-word labels such as "Home" are ignored).
  Leading/trailing <svg>/<button>/<input> icons are trimmed off a unit; one in the middle stays in the
  text and must be kept.  Excluded: svg script style head noscript template pre button input select
  option textarea, and any element with hidden / aria-hidden="true" (an aria-hidden inline element
  inside a unit stays in its text).  A structure html.parser cannot place with certainty (unclosed or
  mismatched tags, stray end tags) is skipped and listed as a warning / skip in meta.json and on screen.
  Not extracted: attribute text other than <meta content> (aria-label, alt, title, placeholder), svg
  text, and the copies of the text inside scripts (SEARCH_INDEX / JSON-LD) - regenerate those later.
  kind : title meta h1-h6 p lead li cell th caption callout.title defterm.term defterm.body step.title
         step.body card.title card.body tag kv.key kv.val kicker label text misc
         (class -> kind: stagetitle=card.title, stagedur/chip/meta-pill/card-tag=tag, fignum=label,
          sub/hero-sub=lead, eyebrow/sec-kicker=kicker, cbody-text=p, note=misc, figcaption=caption,
          dt=defterm.term, dd=defterm.body, summary/label=label, blockquote=p)
  ctx  : sec:<id of nearest section/article with an id | -> [kind=warn|danger|note|tip|key|evidence]
         [in=nav|header|footer|aside|refs]   (nearest one; in=refs = the bibliography: do not rewrite)

APPLY CHECKS  (every error is printed as "U0012: message"; WARN lines never block)
  ids unchanged and complete; the @@ header (kind, ctx) unchanged; text not empty; no raw newline;
  only known ⟦..⟧ tokens; no block-level tag in the text (kind p/lead may split with </p><p>); inline
  tags balanced; no new stray < or >; the multiset of these is identical (order may change): whole
  <sup>..</sup> citations, whole span.fignum, whole <svg>/<button>/<input> elements, and every start tag
  that has attributes (<a href ..>, <img ..>, <span class=..>, hidden / aria-hidden ..).  Bare
  <strong> <em> <b> <i> <br> <code> are free.  An aria-hidden copy of the visible text (h1.text-fit)
  must stay equal to it.  kind meta/title: no < > and (meta) not the attribute's quote character.
  WARN: the numbers (\\d+(?:[.,]\\d+)*) differ; a bare & was added.
  Checks run only on units whose text changed.
"""
from __future__ import annotations

import argparse
import bisect
import hashlib
import html
import json
import os
import re
import shutil
import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
WORK_BASE = HERE / "work"
sys.path.insert(0, str(HERE))
from ste_common import UNIT_HEADER, Unit, html_to_text, read_units, write_units  # noqa: E402

DEFAULTS = ["reading-the-root-zone.html", "FACT-CHECK-REVIEW.html", "_build/data/slab_irrigation_content.html"]

# --------------------------------------------------------------------------- vocabulary
HEADINGS = {"h1", "h2", "h3", "h4", "h5", "h6"}
BLOCK = {"p", "div", "section", "article", "aside", "header", "footer", "nav", "ul", "ol", "li", "table",
         "thead", "tbody", "tfoot", "tr", "td", "th", "figure", "figcaption", "pre", "blockquote", "form",
         "details", "summary", "dl", "dt", "dd", "hr", "main", "address", "fieldset", "hgroup"} | HEADINGS
TAG_KIND = {"p": "p", "li": "li", "td": "cell", "th": "th", "caption": "caption", "figcaption": "caption",
            "dt": "defterm.term", "dd": "defterm.body", "summary": "label", "blockquote": "p", "label": "label"}
# div/span (and p) whose class list holds one of these is a text container; first match wins
CLASS_KIND = (
    ("ctitle", "callout.title"), ("defn-t", "defterm.term"), ("defn-b", "defterm.body"),
    ("step-t", "step.title"), ("step-b", "step.body"), ("card-title", "card.title"), ("card-body", "card.body"),
    ("card-tag", "tag"), ("kv-k", "kv.key"), ("kv-v", "kv.val"), ("stagetitle", "card.title"),
    ("stagecard-b", "card.body"), ("stagedur", "tag"), ("sec-kicker", "kicker"), ("kicker", "kicker"),
    ("eyebrow", "kicker"), ("lead", "lead"), ("sub", "lead"), ("hero-sub", "lead"), ("chip", "tag"),
    ("meta-pill", "tag"), ("fignum", "label"), ("note", "misc"), ("cbody-text", "p"),
)
EXCLUDE_TAGS = {"svg", "script", "style", "noscript", "template", "pre", "button", "input", "select", "option",
                "optgroup", "textarea"}
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track",
        "wbr", "command", "keygen", "basefont", "bgsound", "frame"}
OPTIONAL_END = {"p", "li", "dt", "dd", "tr", "td", "th", "thead", "tbody", "tfoot", "colgroup", "option", "optgroup",
                "html", "head", "body", "rt", "rp"}
P_CLOSERS = {"address", "article", "aside", "blockquote", "details", "div", "dl", "fieldset", "figcaption", "figure",
             "footer", "form", "header", "hgroup", "hr", "main", "menu", "nav", "ol", "p", "pre", "section", "table",
             "ul"} | HEADINGS
LITERAL_TAGS = {"code", "kbd", "samp", "var", "tt"}       # a run that is only code is not prose
WRAPPER_TAGS = {"a", "span"}                              # sibling links / pills in a run are separate units
CALLOUT_KINDS = ("warn", "danger", "note", "tip", "key", "evidence")
META_KEYS = {"description", "og:title", "og:description", "twitter:title", "twitter:description"}
NL = "\u27e6nl\u27e7"
TOKENS = {"nl", "lf", "crlf", "cr"}


class Fatal(Exception):
    def __init__(self, msg, code=1):
        super().__init__(msg)
        self.code = code


# --------------------------------------------------------------------------- small helpers
def sha256(b):
    return hashlib.sha256(b).hexdigest()


def rel(p):
    p = Path(p).resolve()
    try:
        return p.relative_to(REPO).as_posix()
    except ValueError:
        return str(p)


def resolve_file(arg):
    p = Path(arg)
    for c in ([p] if p.is_absolute() else [REPO / p, Path.cwd() / p]):
        if c.is_file():
            return c.resolve()
    raise Fatal("file not found: %s" % arg)


def work_base(arg):
    if not arg:
        return WORK_BASE
    p = Path(arg)
    return p if p.is_absolute() else (REPO / p)


def visible(raw):
    s = re.sub(r"<!--.*?-->", " ", raw, flags=re.S)
    return html.unescape(re.sub(r"<[^>]*>", " ", s))


def has_letters(raw):
    return any(c.isalpha() for c in visible(raw))


def word_count(raw):
    return sum(1 for t in visible(raw).split() if re.search(r"[^\W_]", t))


def lf(b):
    return b.replace(b"\r\n", b"\n")


def nl_style(b):
    """'lf' | 'crlf' (pure), 'mixed', or 'none'."""
    crlf = b.count(b"\r\n")
    lone = b.count(b"\n") - crlf
    return "crlf" if crlf and not lone else "lf" if lone and not crlf else "mixed" if crlf else "none"


def to_style(data, style):
    """Convert pure-LF / pure-CRLF data to the other pure style (git autocrlf flips working copies)."""
    return lf(data).replace(b"\n", b"\r\n") if style == "crlf" else lf(data)


def char_to_byte_map(text):
    if text.isascii():
        return None
    out = [0] * (len(text) + 1)
    acc = 0
    for i, ch in enumerate(text):
        out[i] = acc
        o = ord(ch)
        acc += 1 if o < 0x80 else 2 if o < 0x800 else 3 if o < 0x10000 else 4
    out[-1] = acc
    return out


_NLRE = re.compile(r"\r\n|\n|\r")
_TOKRE = re.compile("\u27e6([^\u27e7\u27e6]*)\u27e7")


def encode_text(raw, crlf):
    def r(m):
        g = m.group(0)
        if g == "\r\n":
            return NL if crlf else "\u27e6crlf\u27e7"
        if g == "\n":
            return "\u27e6lf\u27e7" if crlf else NL
        return "\u27e6cr\u27e7"
    return _NLRE.sub(r, raw)


def decode_text(enc, crlf):
    def r(m):
        t = m.group(1)
        return {"nl": "\r\n" if crlf else "\n", "lf": "\n", "crlf": "\r\n", "cr": "\r"}.get(t, m.group(0))
    return _TOKRE.sub(r, enc)


def bad_tokens(enc):
    """Message if enc holds an unknown or broken ⟦..⟧ token, else ''."""
    unknown = [t for t in _TOKRE.findall(enc) if t not in TOKENS]
    if unknown:
        return "unknown token \u27e6%s\u27e7 (only \u27e6nl\u27e7 is allowed)" % unknown[0]
    rest = _TOKRE.sub("", enc)
    if "\u27e6" in rest or "\u27e7" in rest:
        return "unbalanced \u27e6 \u27e7"
    return ""


# --------------------------------------------------------------------------- markup mini-scanner
_MARKUP_RE = re.compile(
    r"<!--.*?-->"
    r"|<![A-Za-z][^>]*>"
    r"|<(/?)([A-Za-z][A-Za-z0-9:_.-]*)((?:\"[^\"]*\"|'[^']*'|[^'\">])*)>", re.S)
_PSPLIT_RE = re.compile(r"</p\s*>\s*<p\s*>", re.I)
_ATTR_RE = re.compile(r"""([^\s"'<>/=]+)(?:\s*=\s*(?:"([^"]*)"|'([^']*)'|([^\s"'=<>`]+)))?""")


def markup_tokens(s):
    """[(typ, name, start, end)] with typ open|close|self|comment (tags and comments only)."""
    out = []
    for m in _MARKUP_RE.finditer(s):
        name = m.group(2)
        if name is None:
            out.append(("comment", "", m.start(), m.end()))
            continue
        typ = "close" if m.group(1) else ("self" if m.group(0).endswith("/>") else "open")
        out.append((typ, name.lower(), m.start(), m.end()))
    return out


def stray_counts(s):
    pos, parts = 0, []
    for _, _, a, b in markup_tokens(s):
        parts.append(s[pos:a])
        pos = b
    parts.append(s[pos:])
    plain = "".join(parts)
    return plain.count("<"), plain.count(">")


def check_markup(s, allow_split=False):
    """Errors for markup that a text unit may not contain: block tags, unbalanced inline tags.
    allow_split: a bare </p><p> is legal between inline runs (not inside an open inline tag)."""
    errs = []
    toks = [t for t in markup_tokens(s) if t[0] != "comment"]
    stack, i = [], 0
    while i < len(toks):
        typ, name, a, b = toks[i]
        if (allow_split and typ == "close" and name == "p" and not stack and i + 1 < len(toks)
                and toks[i + 1][:2] == ("open", "p")
                and _PSPLIT_RE.fullmatch(_TOKRE.sub("\n", s[a:toks[i + 1][3]]))):
            i += 2
            continue
        i += 1
        if name in BLOCK:
            errs.append("block-level <%s> not allowed in a text unit" % name)
            continue
        if typ == "open":
            if name not in VOID:
                stack.append(name)
        elif typ == "close" and name not in VOID:
            if stack and stack[-1] == name:
                stack.pop()
            else:
                errs.append("unexpected </%s>" % name)
    if stack:
        errs.append("unclosed <%s>" % stack[-1])
    seen, out = set(), []
    for e in errs:
        if e not in seen:
            seen.add(e)
            out.append(e)
    return out[:3]


def _is_fignum(tag_text):
    m = re.search(r"""\bclass\s*=\s*(["'])(.*?)\1""", tag_text, re.S)
    return bool(m) and "fignum" in m.group(2).split()


def _is_protected_open(name, tag_text):
    return name == "sup" or name in EXCLUDE_TAGS or (name == "span" and _is_fignum(tag_text))


def _has_attrs(tag_text):
    m = re.match(r"<[^\s/>]+", tag_text)
    return bool(m) and _ATTR_RE.search(tag_text, m.end()) is not None


def protected_items(s):
    """Multiset of markup that must survive an edit unchanged: every start tag that carries attributes
    (<a href>, <img>, <span class=..>, hidden/aria-hidden ...) and the whole <sup>, span.fignum,
    <svg>/<button>/<input>/... elements.  Bare <strong>/<em>/<br> are free."""
    c = Counter()
    stack = []
    for typ, name, a, b in markup_tokens(s):
        if typ == "comment":
            continue
        tag = s[a:b]
        if typ in ("open", "self"):
            if _has_attrs(tag):
                c["tag|" + tag] += 1
            prot = _is_protected_open(name, tag)
            if typ == "open" and name not in VOID:
                stack.append((name, a, prot))
            elif prot:
                c["el|" + tag] += 1
        elif typ == "close" and stack and stack[-1][0] == name:
            _, a0, prot = stack.pop()
            if prot:
                c["el|" + s[a0:b]] += 1
    return c


def hidden_mirror(s):
    """(visible text, aria-hidden text) of a unit, normalised."""
    vis, hid, stack, depth, pos = [], [], [], 0, 0
    for typ, name, a, b in markup_tokens(s):
        (hid if depth else vis).append(s[pos:a])
        pos = b
        if typ == "open" and name not in VOID:
            h = bool(re.search(r"aria-hidden\s*=\s*[\"']?\s*true", s[a:b], re.I))
            stack.append((name, h))
            depth += h
        elif typ == "close" and stack and stack[-1][0] == name:
            depth -= stack.pop()[1]
    (hid if depth else vis).append(s[pos:])
    norm = lambda parts: re.sub(r"\s+", " ", html.unescape("".join(parts))).strip()   # noqa: E731
    return norm(vis), norm(hid)


_NUM_RE = re.compile(r"\d+(?:[.,]\d+)*")


def number_tokens(enc):
    return Counter(_NUM_RE.findall(html_to_text(enc)))


def attr_value_span(rawtag, name):
    """(start, end, quote) of an attribute value inside a raw start tag, or None."""
    m = re.match(r"<[^\s/>]+", rawtag)
    for am in _ATTR_RE.finditer(rawtag, m.end() if m else 0):
        if am.group(1).lower() == name:
            for gi, q in ((2, '"'), (3, "'"), (4, "")):
                if am.group(gi) is not None:
                    return am.start(gi), am.end(gi), q
            return None
    return None


# --------------------------------------------------------------------------- tokenizer + tree
class _Tok(HTMLParser):
    """Records every token with its absolute char offset; tokens tile the input."""

    def __init__(self, src):
        super().__init__(convert_charrefs=False)
        self.line_starts = [0] + [m.end() for m in re.finditer("\n", src)]
        self.toks = []

    def _p(self):
        ln, col = self.getpos()
        return self.line_starts[ln - 1] + col

    def handle_starttag(self, tag, attrs):
        self.toks.append(("start", self._p(), tag, attrs, self.get_starttag_text()))

    def handle_startendtag(self, tag, attrs):
        self.toks.append(("startend", self._p(), tag, attrs, self.get_starttag_text()))

    def handle_endtag(self, tag):
        self.toks.append(("end", self._p(), tag, None, None))

    def handle_data(self, data):
        self.toks.append(("text", self._p(), None, None, None))

    def handle_entityref(self, name):
        self.toks.append(("text", self._p(), None, None, None))

    def handle_charref(self, name):
        self.toks.append(("text", self._p(), None, None, None))

    def handle_comment(self, data):
        self.toks.append(("comment", self._p(), None, None, None))

    def handle_decl(self, decl):
        self.toks.append(("comment", self._p(), None, None, None))

    def handle_pi(self, data):
        self.toks.append(("comment", self._p(), None, None, None))

    def unknown_decl(self, data):
        self.toks.append(("comment", self._p(), None, None, None))


class Node:
    __slots__ = ("typ", "tag", "attrs", "cls", "s", "e", "ts", "ce", "kids", "parent", "amb", "hard", "excl",
                 "has_block", "has_excl")

    def __init__(self, typ, s, e, tag=None, attrs=None):
        self.typ, self.s, self.e, self.tag, self.attrs = typ, s, e, tag, attrs or {}
        self.ts = self.ce = e            # inner start / inner end (elements)
        self.kids, self.parent = [], None
        self.cls = frozenset()
        self.amb = self.hard = self.excl = self.has_block = self.has_excl = False


def build_tree(src):
    tk = _Tok(src)
    try:
        tk.feed(src)
        tk.close()
    except Exception as e:       # html.parser raises AssertionError on some malformed declarations
        raise Fatal("html.parser could not tokenize the file: %s: %s" % (type(e).__name__, e))
    toks, n, ls = tk.toks, len(src), tk.line_starts
    root = Node("el", 0, n, "#root")
    root.ts, root.ce = 0, n
    stack, warns = [root], []

    def line_of(pos):
        return bisect.bisect_right(ls, pos)

    def warn(pos, msg):
        warns.append((line_of(pos), msg))

    def close_to(k, pos, why):
        for el in reversed(stack[k:]):
            el.ce = el.e = pos
            if el.tag not in OPTIONAL_END:
                el.amb = True
                warn(el.s, "<%s> not closed (%s): subtree skipped" % (el.tag, why))
        del stack[k:]

    def find_open(names, stop):
        for k in range(len(stack) - 1, 0, -1):
            tg = stack[k].tag
            if tg in names:
                return k
            if tg in stop:
                return None
        return None

    def add(node):
        node.parent = stack[-1]
        stack[-1].kids.append(node)

    prev = 0
    for i, t in enumerate(toks):
        typ, pos = t[0], t[1]
        if pos < prev or (i == 0 and pos != 0):
            raise Fatal("tokenizer offset drift at token %d (char %d); file not supported" % (i, pos))
        prev = pos
        end = toks[i + 1][1] if i + 1 < len(toks) else n
        if typ in ("text", "comment"):
            add(Node(typ, pos, end))
        elif typ in ("start", "startend"):
            tag, rawtag = t[2], t[4]
            if src[pos:end] != rawtag:
                raise Fatal("tokenizer offset mismatch for <%s> at line %d" % (tag, line_of(pos)))
            attrs = {}
            for k, v in t[3]:
                attrs.setdefault(k, v)
            if tag == "li":
                k = find_open({"li"}, {"ul", "ol", "menu"})
            elif tag in ("dt", "dd"):
                k = find_open({"dt", "dd"}, {"dl"})
            elif tag == "tr":
                k = find_open({"tr"}, {"table", "thead", "tbody", "tfoot"})
            elif tag in ("td", "th"):
                k = find_open({"td", "th"}, {"tr", "table"})
            elif tag in ("thead", "tbody", "tfoot"):
                k = find_open({"thead", "tbody", "tfoot"}, {"table"})
            elif tag == "option":
                k = find_open({"option"}, {"select", "datalist", "optgroup"})
            else:
                k = None
            if k:
                close_to(k, pos, "implied by <%s>" % tag)
            if tag in P_CLOSERS and len(stack) > 1 and stack[-1].tag == "p":
                close_to(len(stack) - 1, pos, "implied by <%s>" % tag)
            nd = Node("el", pos, end, tag, attrs)
            add(nd)
            if tag in VOID or typ == "startend":
                nd.ce = nd.e = end
                if typ == "startend" and tag not in VOID and (tag in BLOCK or tag in TAG_KIND or tag in ("span", "a")):
                    warn(pos, "self-closing <%s/> treated as an empty element" % tag)
            else:
                stack.append(nd)
        else:  # end tag
            tag = t[2]
            if src[pos:end][:2] != "</":
                raise Fatal("tokenizer offset mismatch for </%s> at line %d" % (tag, line_of(pos)))
            k = None
            for j in range(len(stack) - 1, 0, -1):
                if stack[j].tag == tag:
                    k = j
                    break
            if k is None:
                if tag not in VOID:
                    warn(pos, "stray </%s> ignored" % tag)
                add(Node("comment", pos, end))
                continue
            if k < len(stack) - 1:
                close_to(k + 1, pos, "closed by </%s> at line %d" % (tag, line_of(pos)))
            el = stack.pop()
            el.ce, el.e = pos, end
    close_to(1, n, "end of file")
    return root, warns, ls


def annotate(node):
    hb = he = False
    for ch in node.kids:
        if ch.typ != "el":
            continue
        ch.cls = frozenset((ch.attrs.get("class") or "").split())
        ch.hard = ch.tag in EXCLUDE_TAGS
        ch.excl = (ch.hard or "hidden" in ch.attrs
                   or (ch.attrs.get("aria-hidden") or "").strip().lower() == "true")
        annotate(ch)
        if ch.hard:
            he = True
            continue
        if ch.excl:
            continue
        if ch.tag in BLOCK or ch.has_block:
            hb = True
        if ch.has_excl:
            he = True
    node.has_block, node.has_excl = hb, he


def text_kind(el):
    """Kind of a text container (by tag, or div/span class), else None."""
    t = el.tag
    if t in HEADINGS:
        return t
    if t in ("p", "div", "span"):
        for c, k in CLASS_KIND:
            if c in el.cls:
                return k
        return "p" if t == "p" else None
    return TAG_KIND.get(t)


# --------------------------------------------------------------------------- unit extraction
class Extractor:
    def __init__(self, src, scope):
        self.src, self.scope = src, scope
        self.root, self.warns, self.ls = build_tree(src)
        annotate(self.root)
        self.found, self.skips, self.stats = [], [], Counter()

    # ---- bookkeeping
    def line(self, pos):
        return bisect.bisect_right(self.ls, pos)

    def skip(self, pos, kind, why, raw=""):
        self.skips.append({"line": self.line(pos), "kind": kind, "why": why, "text": raw[:70]})

    def ctx_for(self, owner):
        sec, ck, area, n = "-", None, None, owner
        while n is not None:
            if n.typ == "el":
                if sec == "-" and n.tag in ("section", "article") and n.attrs.get("id"):
                    sec = n.attrs["id"]
                if ck is None and "callout" in n.cls:
                    ck = next((k for k in CALLOUT_KINDS if k in n.cls), None)
                if area is None:
                    if n.tag in ("nav", "header", "footer", "aside"):
                        area = n.tag
                    elif "refs" in n.cls:
                        area = "refs"
            n = n.parent
        return " ".join(["sec:" + sec] + (["kind=" + ck] if ck else []) + (["in=" + area] if area else []))

    def add_unit(self, s, e, kind, owner, min_words=0, ctx=None, extra=None, check=True):
        src = self.src
        while s < e and src[s].isspace():
            s += 1
        while e > s and src[e - 1].isspace():
            e -= 1
        if s >= e:
            return
        raw = src[s:e]
        if not has_letters(raw):
            self.stats["ignored: no letters"] += 1
            return
        if min_words and word_count(raw) < min_words:
            self.stats["ignored: run under %d words" % min_words] += 1
            return
        if "\u27e6" in raw or "\u27e7" in raw:
            self.skip(s, kind, "text contains the characters U+27E6/U+27E7", raw)
            return
        if check:
            if re.search(r"<(script|style)\b", raw, re.I):
                self.skip(s, kind, "script/style inside the text", raw)
                return
            errs = check_markup(raw)
            if errs:
                self.skip(s, kind, "markup: " + "; ".join(errs), raw)
                return
        self.found.append((s, e, kind, ctx or self.ctx_for(owner), extra))

    # ---- walk
    def run(self):
        sc = self.scope
        if sc == "all":
            self.visit(self.root)
        elif sc == "body":
            body = self.first(self.root, "body")
            if body is None:
                self.visit(self.root)
            else:
                head = self.first(self.root, "head")
                if head is not None:
                    self.visit(head)
                self.visit(body)
        else:
            tops = self.tops(self.root, sc)
            if not tops:
                raise Fatal("no <%s> element in the file (scope %s)" % (sc, sc))
            for r in tops:
                self.visit(r)

    def first(self, node, tag):
        for ch in node.kids:
            if ch.typ == "el":
                if ch.tag == tag:
                    return ch
                r = self.first(ch, tag)
                if r is not None:
                    return r
        return None

    def tops(self, node, tag):
        out = []
        for ch in node.kids:
            if ch.typ == "el":
                out.extend([ch] if ch.tag == tag else self.tops(ch, tag))
        return out

    def visit(self, el):
        if el.excl:
            return
        if el.amb:
            self.skip(el.s, el.tag, "ambiguous structure (see warnings)")
            return
        t = el.tag
        if t == "head":
            for ch in el.kids:
                if ch.typ == "el" and ch.tag in ("title", "meta"):
                    self.visit(ch)
            return
        if t == "title":
            raw = self.src[el.ts:el.ce]
            if "<" in raw or ">" in raw:
                self.skip(el.s, "title", "markup inside <title>", raw)
            else:
                self.add_unit(el.ts, el.ce, "title", el, ctx="<title>", check=False)
            return
        if t == "meta":
            self.visit_meta(el)
            return
        k = text_kind(el)
        if k is not None and not el.has_block:
            self.emit_container(el, k)
        else:
            self.visit_children(el)

    def visit_meta(self, el):
        key_attr = next((a for a in ("name", "property") if (el.attrs.get(a) or "").strip().lower() in META_KEYS), None)
        if key_attr is None:
            return
        key = el.attrs[key_attr].strip().lower()
        span = attr_value_span(self.src[el.s:el.ts], "content")
        if span is None:
            return
        vs, ve, q = span
        self.add_unit(el.s + vs, el.s + ve, "meta", el, ctx="<meta %s=%s>" % (key_attr, key), extra={"q": q},
                      check=False)

    def edge(self, n):
        return (n.typ == "comment" or (n.typ == "text" and self.src[n.s:n.e].isspace())
                or (n.typ == "el" and n.hard))

    def emit_container(self, el, kind):
        kids = el.kids
        i, j = 0, len(kids)
        while i < j and self.edge(kids[i]):
            i += 1
        while j > i and self.edge(kids[j - 1]):
            j -= 1
        if i < j:
            self.add_unit(kids[i].s, kids[j - 1].e, kind, el)

    def visit_children(self, el):
        run = []
        for ch in el.kids:
            if ch.typ != "el":
                run.append(ch)
                continue
            if ch.hard or (ch.excl and ch.tag in BLOCK):
                self.flush(run, el)
                run = []
                continue
            separate = (ch.amb or ch.tag in BLOCK or text_kind(ch) is not None or ch.has_block or ch.has_excl)
            if separate:
                self.flush(run, el)
                run = []
                self.visit(ch)
            else:
                run.append(ch)          # inline (a hidden inline element stays raw inside the run)
        self.flush(run, el)

    def flush(self, run, owner):
        i, j = 0, len(run)
        ws = lambda n: n.typ == "comment" or (n.typ == "text" and self.src[n.s:n.e].isspace())   # noqa: E731
        while i < j and ws(run[i]):
            i += 1
        while j > i and ws(run[j - 1]):
            j -= 1
        nodes = run[i:j]
        if not nodes:
            return
        sig = [n for n in nodes if not ws(n)]
        if len(sig) > 1 and all(n.typ == "el" and n.tag in WRAPPER_TAGS for n in sig):
            for n in sig:                # a list of links / pills: one unit each
                self.flush([n], owner)
            return
        if len(sig) == 1 and sig[0].typ == "el":
            el = sig[0]                  # a lone inline wrapper: the unit is its content
            if el.tag not in LITERAL_TAGS and el.tag not in VOID:
                self.visit(el)
            return
        self.add_unit(nodes[0].s, nodes[-1].e, "text", owner, min_words=2)

    def finish(self):
        self.found.sort(key=lambda f: f[0])
        out, prev = [], -1
        for f in self.found:
            if f[0] < prev:
                raise Fatal("internal error: overlapping units at char %d" % f[0])
            prev = f[1]
            out.append(f)
        return out


# --------------------------------------------------------------------------- work folder
def load_meta(wd):
    p = Path(wd) / "meta.json"
    if not p.is_file():
        raise Fatal("no extraction in %s - run extract first" % rel(wd))
    return json.loads(p.read_text(encoding="utf-8"))


def source_path(meta):
    p = Path(meta["source"])
    return (p if p.is_absolute() else REPO / p).resolve()


def do_extract(src, base, scope="body", force=False):
    data = src.read_bytes()
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError as e:
        raise Fatal("%s is not valid UTF-8: %s" % (rel(src), e))
    wd = Path(base) / src.stem
    if (wd / "meta.json").is_file() and (wd / "original.html").is_file() and not force:
        meta = load_meta(wd)
        if lf(data) != lf((wd / "original.html").read_bytes()):       # LF/CRLF flips are not changes
            raise Fatal("%s already holds an extraction and the file now differs from its original.html "
                        "(edits applied, or changed outside).  --force re-extracts from the file as it is now "
                        "and discards units.txt edits." % rel(wd), 3)
        if meta["scope"] != scope:
            raise Fatal("%s was extracted with --scope %s; --force to extract with --scope %s "
                        "(discards units.txt edits)." % (rel(wd), meta["scope"], scope), 3)
        if (wd / "units.txt").is_file():
            return {"status": "already", "meta": meta, "wd": wd}
    ex = Extractor(text, scope)
    ex.run()
    found = ex.finish()
    crlf = text.count("\r\n") > text.count("\n") - text.count("\r\n")
    offs = char_to_byte_map(text)
    b = (lambda i: i) if offs is None else (lambda i: offs[i])
    units = []
    for k, (s, e, kind, ctx, extra) in enumerate(found, 1):
        u = {"id": "U%04d" % k, "kind": kind, "ctx": ctx, "start": b(s), "end": b(e),
             "text": encode_text(text[s:e], crlf)}
        if extra:
            u.update(extra)
        units.append(u)
    meta = {"version": 1, "source": rel(src), "stem": src.stem, "scope": scope,
            "newline": "crlf" if crlf else "lf", "original_sha256": sha256(data), "original_size": len(data),
            "stats": dict(ex.stats),
            "warnings": ["line %d: %s" % w for w in ex.warns], "skipped": ex.skips, "units": units}
    wd.mkdir(parents=True, exist_ok=True)
    (wd / "original.html").write_bytes(data)
    if (wd / "last_applied.html").exists():
        (wd / "last_applied.html").unlink()
    (wd / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=1), encoding="utf-8")
    header = ["# ste-units v1 | file: %s" % src.name,
              "# source: %s | scope: %s | units: %d | sha256: %s" % (meta["source"], scope, len(units), meta["original_sha256"][:16]),
              "# Edit only the text lines. Keep ids and '@@' headers. Keep every tag, entity and \u27e6nl\u27e7 token the markup needs."]
    write_units(str(wd / "units.txt"), header, [Unit(u["id"], u["kind"], u["ctx"], u["text"]) for u in units])
    return {"status": "extracted", "meta": meta, "wd": wd}


def kind_counts(meta):
    return Counter(u["kind"] for u in meta["units"])


def print_extract(info):
    meta, wd = info["meta"], info["wd"]
    if info["status"] == "already":
        print("already extracted (file unchanged): %s - nothing touched" % rel(wd))
    else:
        print("extracted %s -> %s" % (meta["source"], rel(wd / "units.txt")))
    print("  scope %s | newline %s | %d units | %d warning(s) | %d skipped" % (
        meta["scope"], meta["newline"], len(meta["units"]), len(meta["warnings"]), len(meta["skipped"])))
    for kind, n in sorted(kind_counts(meta).items(), key=lambda kv: (-kv[1], kv[0])):
        print("    %-14s %5d" % (kind, n))
    for w in meta["warnings"][:15]:
        print("  warn  " + w)
    for s in meta["skipped"][:15]:
        print("  skip  line %d %s: %s | %s" % (s["line"], s["kind"], s["why"], s["text"]))
    for k, v in sorted(meta["stats"].items()):
        print("  %s: %d" % (k, v))


# --------------------------------------------------------------------------- apply: validation
def scan_multiline(path):
    bad, cur, n = set(), None, 0
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.rstrip("\n")
            m = UNIT_HEADER.match(line)
            if m:
                cur, n = m.group("id"), 0
            elif cur is not None and line.strip():
                n += 1
                if n > 1:
                    bad.add(cur)
    return bad


def _describe(counter, limit=3):
    items = ["%s" % (k.split("|", 1)[1][:70]) for k in list(counter)[:limit]]
    return ", ".join(items) + (" ..." if len(counter) > limit else "")


def check_unit(o, new):
    """(errors, warnings) for one changed unit; o = meta unit dict, new = encoded new text."""
    errs, warns, old, kind = [], [], o["text"], o["kind"]
    if not new.strip():
        return ["empty text"], warns
    tok = bad_tokens(new)
    if tok:
        return [tok], warns
    if kind in ("title", "meta"):
        bad = [c for c in "<>" if c in new]
        if kind == "meta":
            q = o.get("q", '"')
            if '"' in new:
                bad.append('"')
            if q == "'" and "'" in new:
                bad.append("'")
            elif not q and re.search(r"[\s'=`]", new):
                bad.append("whitespace/quote")
        if bad:
            errs.append("%s value must not contain %s" % (kind, " ".join(repr(c) for c in bad)))
    else:
        errs += check_markup(new, allow_split=(kind in ("p", "lead")))
        olt, ogt = stray_counts(old)
        nlt, ngt = stray_counts(new)
        if nlt > olt:
            errs.append("stray '<' created (write &lt; or close the tag)")
        if ngt > ogt:
            errs.append("stray '>' created (write &gt; or open the tag)")
        po, pn = protected_items(old), protected_items(new)
        if po != pn:
            lost, added = po - pn, pn - po
            errs.append("protected markup changed (citations, links, figure numbers, images, icons): lost [%s] added [%s]"
                        % (_describe(lost), _describe(added)))
        ov, oh = hidden_mirror(old)
        if oh and oh == ov:
            nv, nh = hidden_mirror(new)
            if nv != nh:
                errs.append("the aria-hidden copy of the text no longer equals the visible text (edit both)")
    if len(re.findall(r"&(?!#?\w+;)", new)) > len(re.findall(r"&(?!#?\w+;)", old)):
        warns.append("bare '&' added (write &amp;)")
    no, nn = number_tokens(old), number_tokens(new)
    if no != nn:
        warns.append("numbers differ - lost [%s] added [%s]" % (
            ", ".join(sorted((no - nn).elements())) or "-", ", ".join(sorted((nn - no).elements())) or "-"))
    return errs, warns


def validate(meta, file_units, multiline):
    """-> (errors [(id, msg)], warnings [(id, msg)], new_enc {id: text})."""
    errs, warns, new = [], [], {}
    old = {u["id"]: u for u in meta["units"]}
    for u in file_units:
        if u.id in new:
            errs.append((u.id, "duplicate id"))
            continue
        o = old.get(u.id)
        if o is None:
            errs.append((u.id, "unknown id (not in meta.json)"))
            continue
        new[u.id] = u.text
        if u.kind != o["kind"]:
            errs.append((u.id, "header kind changed: %r -> %r (copy the @@ header exactly)" % (o["kind"], u.kind)))
        if u.ctx != o["ctx"]:
            errs.append((u.id, "header ctx changed: %r -> %r (copy the @@ header exactly)" % (o["ctx"], u.ctx)))
        if u.id in multiline:
            errs.append((u.id, "raw newline in the text: keep one line and write \u27e6nl\u27e7 for a line break"))
    for uid in old:
        if uid not in new:
            errs.append((uid, "missing from the units file"))
    bad = {e[0] for e in errs}
    for uid, o in old.items():
        if uid not in new or new[uid] == o["text"] or uid in bad:
            continue
        e, w = check_unit(o, new[uid])
        errs += [(uid, m) for m in e]
        warns += [(uid, m) for m in w]
    return errs, warns, new


def compose(orig, meta, new_enc, force_all=False):
    """Original bytes with the changed unit spans replaced."""
    crlf = meta["newline"] == "crlf"
    out, pos = bytearray(), 0
    for u in sorted(meta["units"], key=lambda x: x["start"]):
        enc = new_enc[u["id"]]
        if force_all or enc != u["text"]:
            out += orig[pos:u["start"]]
            out += decode_text(enc, crlf).encode("utf-8")
            pos = u["end"]
    out += orig[pos:]
    return bytes(out)


def check_integrity(orig, meta):
    crlf = meta["newline"] == "crlf"
    for u in meta["units"]:
        try:
            ok = encode_text(orig[u["start"]:u["end"]].decode("utf-8"), crlf) == u["text"]
        except UnicodeDecodeError:
            ok = False
        if not ok:
            raise Fatal("meta.json does not match original.html at %s - re-extract with --force" % u["id"])


def load_for_apply(src, base, force):
    wd = Path(base) / src.stem
    meta = load_meta(wd)
    orig = (wd / "original.html").read_bytes()
    if sha256(orig) != meta["original_sha256"]:
        raise Fatal("original.html does not match meta.json (edited by hand?) - re-extract with --force")
    if source_path(meta) != src.resolve() and not force:
        raise Fatal("%s was extracted from %s, not from %s (--force to ignore)" % (rel(wd), meta["source"], rel(src)), 3)
    cur = src.read_bytes()
    if file_state(cur, wd) == "outside" and not force:
        raise Fatal("%s changed since extract/apply (it matches neither original.html nor last_applied.html; "
                    "LF/CRLF differences are ignored).  Re-extract with --force, or apply with --force to "
                    "overwrite it." % rel(src), 3)
    check_integrity(orig, meta)
    return wd, meta, orig, cur


def file_state(cur, wd):
    """'original' | 'applied' | 'outside': how the file on disk relates to the work folder (LF/CRLF ignored)."""
    c = lf(cur)
    if c == lf((wd / "original.html").read_bytes()):
        return "original"
    la = wd / "last_applied.html"
    return "applied" if la.is_file() and c == lf(la.read_bytes()) else "outside"


def read_edit_file(wd, src_name):
    path = wd / "units.txt"
    if not path.is_file():
        raise Fatal("%s missing" % rel(path))
    header, units = read_units(str(path))
    fname = next((m.group(1) for h in header for m in [re.search(r"file:\s*(\S+)", h)] if m), None)
    if fname and fname != src_name:
        raise Fatal("units.txt belongs to %s, not %s" % (fname, src_name), 2)
    return units, scan_multiline(str(path))


def do_apply(src, base, dry_run=False, force=False, quiet=False):
    wd, meta, orig, cur = load_for_apply(src, base, force)
    units, multiline = read_edit_file(wd, src.name)
    errs, warns, new = validate(meta, units, multiline)
    out = print if not quiet else (lambda *a, **k: None)
    for uid, m in sorted(errs):
        out("%s: %s" % (uid, m))
    for uid, m in sorted(warns):
        out("WARN %s: %s" % (uid, m))
    if errs:
        out("%d validation error(s) in %s; nothing written" % (len(errs), rel(wd / "units.txt")))
        return 2
    data = compose(orig, meta, new)
    changed = [u["id"] for u in meta["units"] if new[u["id"]] != u["text"]]
    delta = len(data) - len(orig)
    so, sc = nl_style(orig), nl_style(cur)
    if so != sc and so in ("lf", "crlf") and sc in ("lf", "crlf"):
        data = to_style(data, sc)          # keep the line endings the working copy has now
    if dry_run:
        out("dry run: %d unit(s) changed%s, %+d bytes; %s not touched" % (
            len(changed), (" (%s)" % " ".join(changed[:12]) + (" ..." if len(changed) > 12 else "")) if changed else "",
            delta, meta["source"]))
        return 0
    if cur != data:
        tmp = src.with_name(src.name + ".ste-tmp")
        try:
            tmp.write_bytes(data)
            os.replace(tmp, src)
        except OSError as e:
            if tmp.exists():
                tmp.unlink()
            raise Fatal("cannot write %s: %s" % (rel(src), e))
    (wd / "last_applied.html").write_bytes(data)
    out("applied %s: %d unit(s) changed%s, %+d bytes vs original (%s)" % (
        meta["source"], len(changed), (" (%s)" % " ".join(changed[:12]) + (" ..." if len(changed) > 12 else "")) if changed else "",
        delta, "file rewritten" if cur != data else "file already identical"))
    return 0


def do_status(src, base):
    wd = Path(base) / src.stem
    if not (wd / "meta.json").is_file():
        print("%s: not extracted (no %s)" % (src.name, rel(wd)))
        return 0
    meta = load_meta(wd)
    orig = (wd / "original.html").read_bytes()
    state = {"original": "identical to original.html", "applied": "equals last_applied.html",
             "outside": "CHANGED outside the tool (matches neither original.html nor last_applied.html)"
             }[file_state(src.read_bytes(), wd)]
    state += " (LF/CRLF ignored)"
    print("%s | work %s | scope %s | %d units | file: %s" % (src.name, rel(wd), meta["scope"], len(meta["units"]), state))
    units, multiline = read_edit_file(wd, src.name)
    errs, warns, new = validate(meta, units, multiline)
    changed = [u["id"] for u in meta["units"] if new.get(u["id"], u["text"]) != u["text"]]
    print("units.txt: %d of %d unit(s) edited | %d error(s) | %d warning(s)%s" % (
        len(changed), len(meta["units"]), len(errs), len(warns), " | would write %+d bytes" % (len(compose(orig, meta, new)) - len(orig)) if not errs else ""))
    if changed:
        print("  edited: " + " ".join(changed[:30]) + (" ..." if len(changed) > 30 else ""))
    for uid, m in sorted(errs)[:10]:
        print("  %s: %s" % (uid, m))
    for uid, m in sorted(warns)[:10]:
        print("  WARN %s: %s" % (uid, m))
    return 0


# --------------------------------------------------------------------------- selftest
class _TagSeq(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.seq = []

    def _a(self, tag, attrs):
        a = tuple(attrs)
        if tag == "meta":       # <meta content> is a unit: its text may change
            d = dict(a)
            if (d.get("name") or d.get("property") or "").strip().lower() in META_KEYS:
                a = tuple((k, v) for k, v in a if k != "content")
        return a

    def handle_starttag(self, tag, attrs):
        self.seq.append(("s", tag, self._a(tag, attrs)))

    def handle_startendtag(self, tag, attrs):
        self.seq.append(("se", tag, self._a(tag, attrs)))

    def handle_endtag(self, tag):
        self.seq.append(("e", tag))

    def handle_comment(self, data):
        self.seq.append(("c", data))

    def handle_decl(self, decl):
        self.seq.append(("d", decl))

    def handle_pi(self, data):
        self.seq.append(("p", data))


def tag_sequence(data):
    p = _TagSeq()
    p.feed(data.decode("utf-8"))
    p.close()
    return p.seq


def mutate(enc):
    """Change letters in plain text only (not tags, entities, tokens or protected elements)."""
    def plain(seg):
        parts = re.split(r"(&#?\w+;|\u27e6[^\u27e7]*\u27e7)", seg)
        return "".join(p if i % 2 else p.replace("e", "ee") for i, p in enumerate(parts))
    out, pos, stack, depth = [], 0, [], 0
    for typ, name, a, b in markup_tokens(enc):
        seg = enc[pos:a]
        out += [seg if depth else plain(seg), enc[a:b]]
        pos = b
        if typ == "open" and name not in VOID:
            prot = _is_protected_open(name, enc[a:b])
            stack.append((name, prot))
            depth += prot
        elif typ == "close" and stack and stack[-1][0] == name:
            depth -= stack.pop()[1]
    seg = enc[pos:]
    out.append(seg if depth else plain(seg))
    return "".join(out)


def skeleton(data, meta_units):
    out, pos = [], 0
    for u in sorted(meta_units, key=lambda x: x["start"]):
        out.append(data[pos:u["start"]])
        pos = u["end"]
    out.append(data[pos:])
    return b"\x00".join(out)


def selftest_one(src):
    orig = src.read_bytes()
    stem = src.stem
    scratch = WORK_BASE / ("html_selftest_" + stem)
    if scratch.exists():
        shutil.rmtree(scratch)
    tgt = scratch / "t" / src.name
    tgt.parent.mkdir(parents=True)
    tgt.write_bytes(orig)
    base = scratch / "w"
    res = {"file": rel(src), "bytes": len(orig), "ok": {}, "notes": [], "units": 0, "kinds": Counter()}
    try:
        info = do_extract(tgt, base, "body", True)
        meta, wd = info["meta"], info["wd"]
        res["units"], res["kinds"] = len(meta["units"]), kind_counts(meta)
        res["notes"].append("%d warning(s), %d skipped structure(s)" % (len(meta["warnings"]), len(meta["skipped"])))
        texts = {u["id"]: u["text"] for u in meta["units"]}
        # (a) extract -> apply, no edits
        rc = do_apply(tgt, base, quiet=True)
        res["ok"]["a"] = rc == 0 and tgt.read_bytes() == orig and (wd / "last_applied.html").read_bytes() == orig
        # (b) force-rewrite every unit with its own decoded text
        out_b = compose(orig, meta, texts, force_all=True)
        res["ok"]["b"] = out_b == orig
        # (c) tag sequences
        res["ok"]["c"] = tag_sequence(out_b) == tag_sequence(orig) == tag_sequence(tgt.read_bytes())
        # (d) edit round-trip
        mut = {k: mutate(v) for k, v in texts.items()}
        n_mut = sum(1 for k in mut if mut[k] != texts[k])
        res["notes"].append("(d) edited %d of %d units" % (n_mut, len(texts)))
        errs = []
        for u in meta["units"]:
            if mut[u["id"]] != u["text"]:
                e, _ = check_unit(u, mut[u["id"]])
                errs += ["%s: %s" % (u["id"], m) for m in e]
        header, units = read_units(str(wd / "units.txt"))
        for u in units:
            u.text = mut[u.id]
        write_units(str(wd / "units.txt"), header, units)
        rc1 = do_apply(tgt, base, quiet=True)
        out_d = tgt.read_bytes()
        t2 = scratch / "t2" / src.name
        t2.parent.mkdir(parents=True)
        t2.write_bytes(out_d)
        meta2 = do_extract(t2, scratch / "w2", "body", True)["meta"]
        same_units = ([(u["id"], u["kind"], u["ctx"], u["text"]) for u in meta2["units"]]
                      == [(u["id"], u["kind"], u["ctx"], mut[u["id"]]) for u in meta["units"]])
        rc2 = do_apply(tgt, base, quiet=True)
        again = tgt.read_bytes()
        for u in units:
            u.text = texts[u.id]
        write_units(str(wd / "units.txt"), header, units)
        rc3 = do_apply(tgt, base, quiet=True)
        ok_d = [not errs, rc1 == 0, n_mut > 0 or not texts, out_d != orig or n_mut == 0,
                tag_sequence(out_d) == tag_sequence(orig), same_units,
                skeleton(out_d, meta2["units"]) == skeleton(orig, meta["units"]),
                rc2 == 0 and again == out_d, rc3 == 0 and tgt.read_bytes() == orig]
        res["ok"]["d"] = all(ok_d)
        if not all(ok_d):
            res["notes"].append("(d) sub-checks %s %s" % ("".join("1" if x else "0" for x in ok_d), errs[:3]))
        # (e) git core.autocrlf flips LF<->CRLF on checkout: the file must still be accepted and keep that style
        so = nl_style(orig)
        if so in ("lf", "crlf"):
            flip = "crlf" if so == "lf" else "lf"
            tgt.write_bytes(to_style(orig, flip))
            still = do_extract(tgt, base, "body", False)["status"] == "already"
            for u in units:
                u.text = mut[u.id]
            write_units(str(wd / "units.txt"), header, units)
            rc4 = do_apply(tgt, base, quiet=True)
            flipped = tgt.read_bytes()
            for u in units:
                u.text = texts[u.id]
            write_units(str(wd / "units.txt"), header, units)
            rc5 = do_apply(tgt, base, quiet=True)
            res["ok"]["e"] = (still and rc4 == 0 and nl_style(flipped) in (flip, "none") and lf(flipped) == lf(out_d)
                              and rc5 == 0 and tgt.read_bytes() == to_style(orig, flip))
        else:
            res["ok"]["e"] = True
            res["notes"].append("(e) n/a: newlines are %s" % so)
    except Exception as e:          # one bad file must not abort the whole table
        res["ok"].setdefault("a", False)
        res["notes"].append("ERROR: %s: %s" % (type(e).__name__, e))
    res["pass"] = all(res["ok"].get(k) for k in "abcde")
    if src.read_bytes() != orig:
        res["pass"] = False
        res["notes"].append("REAL FILE CHANGED")
    if res["pass"]:
        shutil.rmtree(scratch, ignore_errors=True)
    else:
        res["notes"].append("scratch kept: %s" % rel(scratch))
    return res


def cmd_selftest(files, all_defaults):
    paths = [resolve_file(f) for f in files] + ([resolve_file(f) for f in DEFAULTS] if all_defaults else [])
    if not paths:
        raise Fatal("selftest: give a file or --all-defaults")
    results = [selftest_one(p) for p in paths]
    print("%-46s %9s %6s  %-4s %-4s %-4s %-4s %-4s  %s" % ("file", "bytes", "units", "(a)", "(b)", "(c)", "(d)", "(e)", "result"))
    for r in results:
        ok = lambda k: "ok" if r["ok"].get(k) else "FAIL"   # noqa: E731
        print("%-46s %9d %6d  %-4s %-4s %-4s %-4s %-4s  %s" % (r["file"], r["bytes"], r["units"], ok("a"), ok("b"),
                                                               ok("c"), ok("d"), ok("e"), "PASS" if r["pass"] else "FAIL"))
    for r in results:
        print("\n%s: %s" % (r["file"], "; ".join(r["notes"])))
        print("  " + ", ".join("%s %d" % kv for kv in sorted(r["kinds"].items(), key=lambda kv: (-kv[1], kv[0]))))
    return 0 if all(r["pass"] for r in results) else 1


# --------------------------------------------------------------------------- CLI
def main(argv=None):
    for stream in (sys.stdout, sys.stderr):
        if stream.encoding and stream.encoding.lower() != "utf-8":
            stream.reconfigure(encoding="utf-8", errors="replace")
    sys.setrecursionlimit(8000)
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    e = sub.add_parser("extract")
    e.add_argument("file")
    e.add_argument("--work")
    e.add_argument("--scope", default="body", choices=["body", "main", "article", "all"])
    e.add_argument("--force", action="store_true")
    a = sub.add_parser("apply")
    a.add_argument("file")
    a.add_argument("--work")
    a.add_argument("--dry-run", action="store_true")
    a.add_argument("--force", action="store_true")
    s = sub.add_parser("status")
    s.add_argument("file")
    s.add_argument("--work")
    t = sub.add_parser("selftest")
    t.add_argument("files", nargs="*")
    t.add_argument("--all-defaults", action="store_true")
    ns = ap.parse_args(argv)
    try:
        if ns.cmd == "selftest":
            return cmd_selftest(ns.files, ns.all_defaults)
        src = resolve_file(ns.file)
        base = work_base(ns.work)
        if ns.cmd == "extract":
            print_extract(do_extract(src, base, ns.scope, ns.force))
            return 0
        if ns.cmd == "apply":
            return do_apply(src, base, ns.dry_run, ns.force)
        return do_status(src, base)
    except Fatal as ex:
        print("error: %s" % ex, file=sys.stderr)
        return ex.code
    except RecursionError:
        print("error: HTML nesting is too deep for this tool", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
