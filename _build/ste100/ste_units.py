# -*- coding: utf-8 -*-
"""ste_units.py - prose "units" for the ASD-STE100 rewrite of the paper modules.

Agents must never edit Python or JSON.  This tool copies every human-readable string of a
target into a plain-text units file, and writes edited units back into the exact source span
each one came from.

TARGETS   (argument dotted or slashed, relative to _build/; ".py" optional)
  paper_<name>              a paper module                          prose, --svg-text
  ipm_blueprint.content     IPM blueprint data (dicts/tuples)       prose (selftest renders
  ipm_blueprint.render      IPM blueprint section builder           prose  paper_auckland_ipm_blueprint)
  data.glossary, data.glossary_gen, data.glossary_gen4 ... _gen9    prose: only the "defn" values
  data.evidence             PAPERS/DEFAULT phrases + panel_html() text   prose
  figs, figs_<name>         figure modules                          --svg-text only
  figs_<name>.json          SVG strings of a paper (path or name)   --svg-text only
  refused: data.nav (edited by hand), paper_slab_irrigation (HTML payload), the
  paper_auckland_ipm_blueprint wrapper (use the two ipm_blueprint targets).

MODES     prose (default)  state in  _build/ste100/work/<target>/
          --svg-text       state in  _build/ste100/work/<target>/svg/   (own units.txt, meta.json,
                           original snapshot taken at svg extract time, i.e. after the prose
                           rewrite was applied).  The two modes never invalidate each other.

COMMANDS  (relative paths are relative to the repo root; default work dir _build/ste100/work)

  extract  <target> [--svg-text] [--work DIR] [--force]
      -> units.txt (edit this), meta.json (never edit), original snapshot (kept once it
      exists).  Prints units by kind, misc / label counts and every slot skipped as
      unsupported.  Refuses to overwrite a units.txt that already holds edits; --force
      re-snapshots the current file and regenerates units.txt (edits are discarded).
  apply    <target> [--svg-text] [--work DIR] [--dry-run] [--force]
      Validates units.txt (errors print as 'U0012: message', exit 2, nothing written;
      warnings never block).  Rebuilds the target from the snapshot plus every edited unit
      (idempotent), keeps the replaced file as last_applied.*, py_compiles / json-parses it
      and imports it (and the paper that uses it) in a subprocess; puts the previous file
      back if that fails.  --dry-run = validate + test-import a temp copy, write nothing.
      Refuses when the target was changed outside this tool since extract/apply (--force
      overrides); that check ignores LF/CRLF (git core.autocrlf) and apply keeps the file's
      current line-ending style.  An edited string is re-wrapped at ~104 columns if the
      original string was wrapped.  Diagram text (svglabel units, and label / misc units
      whose ctx has in=Module.func) longer than 115% of the original gets a warning.
  selftest <target> [--svg-text] | --all [--svg-text | --prose-only]
      Losslessness proof: re-emits EVERY unit from its unchanged text into a temp copy and
      compares, in separate subprocesses, sha256 of the rendered result:
        paper modules ........ json.dumps(TITLE, EYEBROW, SUB, META, SECTIONS [+ RELATED,
                               REF_IDS, SLUG]) of the paper
        ipm_blueprint.* ...... the same for the wrapper paper_auckland_ipm_blueprint
        data.* ............... json.dumps(sort_keys) of all public UPPERCASE attributes
                               (data.evidence also every panel_html(slug) and community_note)
        figs modules ......... output of every zero-argument public function + UPPERCASE
                               attributes, and every paper rendered with the patched module
        figs_*.json .......... canonical json dump (sort_keys)
      and checks that the copy re-extracts to the same units.  Never touches real files.
      --all runs prose for every prose target and svg-text for every svg target, and writes
      <work>/extract_report.txt.
  status   <target> [--svg-text] [--work DIR]   units, edited, misc, validation summary
  report   [--work DIR]                          (re)write <work>/extract_report.txt only

UNITS FILE   (format shared with ste_lint / ste_merge through ste_common)
  # ste-units v1 | module: paper_x | slug: <SLUG>
  @@ U0002 | p | s:intro kind=key E1=L.name
  Text exactly as it lands in the HTML ⟦c:some-ref⟧ and more text ⟦e1⟧.
  - Edit only the text line, keep it on ONE line, never edit an '@@' line.
  - ⟦c:rid⟧ = citation _c("rid").  ⟦e1⟧, ⟦e2⟧ = other code; its source is shown as E1=...
    in the header (long sources shortened with ...).  Keep every placeholder exactly as
    many times as in the original; moving it is fine.  ⟦nl⟧ = newline inside the string.
  - Inline HTML (<strong>, <em>, <a href=...>, <br>) and entities (&deg;) stay as written.
    Close every tag you open; p / lead units may be split with </p><p>.
  - ctx '%-format': the string is a %-template, keep its %s / %d specifiers.
  kinds: title eyebrow sub meta kicker section.title p lead heading li callout.title
         callout.body defterm.term defterm.body th cell caption foot step.title step.body
         card.title card.body tag kv.key kv.val stage.title stage.dur stage.body chip
         label    figure text (rule f, ctx in=L.flow ...), photo alt text, photo_sequence
                  labels, short title-like data values, _input() labels
         text     prose sentences in data modules and in HTML strings (ctx d:... / html=...)
         svglabel text drawn inside an SVG figure (--svg-text; ctx svg=<function | json key>)
         misc     other text outside the helpers (optional to rewrite)

WHAT IS A UNIT
  prose, code targets (papers, ipm_blueprint.render): TITLE / EYEBROW / SUB, META labels,
    "kicker" / "title" of every dict with a "blocks" key, the prose arguments of the
    components.py helpers (by name, also X.helper(...)), descending into list / tuple
    literals and into the item template of list comprehensions.  Functions passing a
    parameter straight into a helper prose argument count as helpers; LOCAL_WRAPPERS maps
    the ones that build HTML themselves.  A module string constant used in a prose argument
    (JURISDICTION_NOTE) is extracted with that argument's kind.
    Rule (f): the TEXT parameters of the figs_lib generators (title, note, ylab, bar /
    x-axis labels, flow step texts, band labels; FIG_GENERATORS) become label units with
    ctx in=<call>, also inside _fig* functions; colours, numbers, units, keys, pure
    number/unit labels are never taken.
    Rule (e): any other string with >= 4 words that is not SVG / markup / CSS / URL / path /
    regex becomes kind misc.  Never: docstrings, dict keys, "id" values, REF_IDS / RELATED /
    SLUG, callout kind, cls, figure svg / num, photo src / model, stagecard num, print /
    raise / assert text, other strings inside _fig* / _g_* / SVG-building functions.
  prose, data targets: strings in the UPPERCASE structures: >= 4 words -> text; values of
    the keys title/name/label/heading/term with >= 2 words, and 2-3 word strings in
    tuples/lists -> label; never keys, ids, slugs, image paths, refs, tags, kind/enum values,
    scientific names.  Glossary files: only "defn" (kind defterm.body).  data.evidence:
    every phrase in PAPERS / DEFAULT (kind li) and the text of the leaf HTML elements built
    in panel_html() (text / label, ctx html=<tag>.<class>).
  --svg-text: the raw content of <text>, <tspan>, <title>, <desc> elements inside string
    literals / f-strings ({expr} -> ⟦eN⟧) or JSON string values, plus string literals that
    reach such an element through a local helper parameter (_t, _title, _wrap, _panel,
    box ..., inferred from <text>{param}</text>) or through the item list of a for-loop.
    Contents without letters, pure numbers / units and code-only text are skipped.
  Element text (svg, evidence HTML) is patched in place when it sits inside one string
  token; text that spans several tokens (implicit concatenation) or a raw string re-emits
  that whole literal.  Element text inside a "..." % x or "...".format(x) template is marked
  %-format / {}-format and must keep its specifier count.
  Every unit is re-emitted and re-parsed at extract time; a unit that does not round-trip
  is skipped and reported, never half-handled.
"""
import argparse
import ast
import bisect
import collections
import dataclasses
import datetime
import hashlib
import html as _html
import io
import json
import os
import py_compile
import re
import shutil
import subprocess
import sys
import tempfile
import tokenize
import unicodedata
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.dirname(HERE)
REPO = os.path.dirname(BUILD)
if HERE not in sys.path:
    sys.path.insert(0, HERE)
from ste_common import UNIT_HEADER, Unit, read_units, write_units  # noqa: E402

FORMAT = "ste-units v1"
DEFAULT_WORK = os.path.join(HERE, "work")
PY = sys.executable
WRAP_WIDTH = 104
LABEL_GROWTH = 1.15
IPM_WRAPPER = "paper_auckland_ipm_blueprint"

UNSUPPORTED = {
    "paper_slab_irrigation": "prose lives in _build/data/slab_irrigation_content.html (parsed at import)",
    "paper_auckland_ipm_blueprint": "3-line wrapper: use the targets ipm_blueprint.content and ipm_blueprint.render",
}
BLOCKED = {
    "data.nav": "data.nav is edited by hand by another agent: not extracted",
}

# components.py helpers -> [(parameter, role)].  role: kind string = prose slot of that kind;
# None = not prose (walked for misc strings only); "walk" = holds helper calls;
# ("list", k) = list/tuple literal of k slots; ("rows", k) = list of lists of k slots;
# ("pairs", k1, k2) = list of tuples, element 0 -> k1, element 1 -> k2 (None = not prose).
HELPERS = {
    "p": [("t", "p")],
    "lead": [("t", "lead")],
    "h": [("level", None), ("t", "heading"), ("_id", None)],
    "ul": [("items", ("list", "li")), ("cls", None)],
    "ol": [("items", ("list", "li")), ("cls", None)],
    "callout": [("kind", None), ("title", "callout.title"), ("body", "callout.body")],
    "defterm": [("term", "defterm.term"), ("body", "defterm.body")],
    "table": [("headers", ("list", "th")), ("rows", ("rows", "cell")), ("cls", None),
              ("caption", "caption"), ("foot", "foot")],
    "figure": [("svg", None), ("num", None), ("caption", "caption")],
    "diagram": [("svg", None), ("caption", "caption"), ("label", "label")],
    "photo": [("src", None), ("caption", "caption"), ("alt", "label"), ("model", None)],
    "photo_sequence": [("title", "label"), ("frames", ("pairs", "label", None)),
                       ("caption", "caption"), ("model", None)],
    "term_gallery": [("items", ("pairs", "label", None)), ("model", None)],
    "stagecard": [("num", None), ("title", "stage.title"), ("dur", "stage.dur"), ("body", "stage.body")],
    "grid": [("cards", "walk"), ("cols", None)],
    "card": [("title", "card.title"), ("body", "card.body"), ("tag", "tag")],
    "chip": [("t", "chip")],
    "kv": [("pairs", ("pairs", "kv.key", "kv.val"))],
    "steps": [("items", ("pairs", "step.title", "step.body"))],
}

# Module functions that build prose HTML themselves (not through a helper): param -> role.
LOCAL_WRAPPERS = {
    "paper_cannabis_tc_sop": {"form": {"title": "caption", "fields": ("list", "th"), "note": "foot"}},
    "paper_scaling_high_light": {"_tag": {"txt": "tag"}},
    "ipm_blueprint.render": {"_input": {"label": "label"}},
}

# Rule (f): figure generators -> [(parameter, role)].  role: "text" = drawn text;
# ("items", (i, ...)) = list of tuples whose elements i are drawn text; ("list",) = list of
# drawn texts; None = style / data (colours, numbers, units, ids): never extracted.
# From figs_lib.py: bars/hbars draw title, note and data[i][0]; line draws title, note, ylab,
# xlabels[i], bands[i][3] (pts[i][0] is never drawn); flow draws title, note, steps[i][0..1]
# (steps[i][2..3] are colours); zones draws title, note, bands[i][3].  The other figs modules
# only expose zero-argument figure functions (their text is handled by --svg-text).
FIG_GENERATORS = {
    "figs_lib": {
        "bars": [("title", "text"), ("data", ("items", (0,))), ("unit", None), ("note", "text"),
                 ("target", None), ("maxv", None)],
        "hbars": [("title", "text"), ("data", ("items", (0,))), ("unit", None), ("note", "text")],
        "line": [("title", "text"), ("pts", None), ("xlabels", ("list",)), ("ylab", "text"), ("note", "text"),
                 ("ymax", None), ("ymin", None), ("bands", ("items", (3,)))],
        "flow": [("title", "text"), ("steps", ("items", (0, 1))), ("note", "text")],
        "zones": [("title", "text"), ("lo", None), ("hi", None), ("bands", ("items", (3,))), ("unit", None),
                  ("note", "text")],
    },
}

MODULE_KINDS = {"TITLE": "title", "EYEBROW": "eyebrow", "SUB": "sub"}
SKIP_NAMES = {"SLUG", "RELATED", "REF_IDS"}
QUIET_CALLEES = {"_c", "open", "json.load", "os.path.join", "os.path.dirname", "REF_IDS.index",
                 "print", "len", "range", "isinstance", "int", "str", "getattr"}
TITLE_KEYS = {"title", "name", "label", "heading", "term"}
DATA_SKIP_KEYS = {"id", "slug", "image", "img", "src", "href", "url", "refs", "ref", "ref_ids", "tags",
                  "kind", "type", "icon", "scientific", "key", "file", "path", "color", "colour", "class",
                  "cls", "status", "track", "group", "model", "anchor"}
HTML_BLOCK = {"p", "div", "li", "td", "th", "h1", "h2", "h3", "h4", "h5", "h6", "caption", "figcaption",
              "dt", "dd", "section", "article", "header", "footer", "ul", "ol", "table", "tr", "thead",
              "tbody", "blockquote", "label", "button", "figure", "nav", "aside", "main", "summary"}
UNIT_WORDS = {"mm", "cm", "km", "ml", "kg", "mg", "ug", "ppm", "ppb", "kpa", "hpa", "mpa", "pa", "psi", "bar",
              "mbar", "kw", "kwh", "wh", "kv", "ma", "hz", "khz", "lux", "lx", "nm", "min", "mins", "hr", "hrs",
              "wk", "wks", "cfm", "fpm", "rh", "ec", "ph", "vpd", "ppfd", "dli", "in", "ft", "lb", "lbs", "oz",
              "gal", "mol", "mmol", "umol", "ms", "us", "ds", "btu", "kj", "mj", "kcal", "sec", "secs", "yr", "yrs"}

LB, RB = "⟦", "⟧"
NL_TOK, CR_TOK = LB + "nl" + RB, LB + "cr" + RB
PH_RE = re.compile(LB + r"(?:c:[^" + LB + RB + r"\s]+|e\d+)" + RB)   # citation / expression
ANY_TOK_RE = re.compile(LB + "[^" + LB + RB + "]*" + RB)             # incl. nl / cr
SVG_MARKERS = ("<svg", "<path", "<text", "<rect", "<line", "<circle", "<g ", "<g>", "viewbox",
               'style="', "style='", "<polygon", "<polyline", "<ellipse", "<marker", "<defs",
               "<tspan", "<lineargradient", "stroke-width", "text-anchor")
SVG_EL_RE = re.compile(r"<(text|tspan|title|desc)\b[^>]*>(.*?)</\1\s*>", re.S | re.I)
SVG_HINT_RE = re.compile(r"<(?:text|tspan|title|desc)\b", re.I)
TAG_RE = re.compile(r"<(/?)([A-Za-z][A-Za-z0-9]*)\b[^<>]*?(/?)>")
VOID_TAGS = {"br", "hr", "img", "wbr", "input", "meta", "link", "source", "col", "area", "base",
             "embed", "param", "track"}
PCT_RE = re.compile(r"%(?:\([^)]*\))?[#0 +\-]*(?:\*|\d+)?(?:\.(?:\*|\d+))?[hlL]?[diouxXeEfFgGcrsa%]")
NUM_RE = re.compile(r"\d+(?:[.,]\d+)*")
ENTITY_RE = re.compile(r"&#[xX]?[0-9a-fA-F]+;|&[A-Za-z][A-Za-z0-9]*;")
ATOMS = (ast.Name, ast.Attribute, ast.Call, ast.Subscript, ast.Constant, ast.JoinedStr, ast.List,
         ast.Tuple, ast.Dict, ast.Set, ast.ListComp, ast.SetComp, ast.DictComp, ast.GeneratorExp)
FIELD = ""   # stands for one f-string field while matching element content


class Unsupported(Exception):
    pass


# ============================================================================ small helpers
def _enc(s):
    return s.replace("\n", NL_TOK).replace("\r", CR_TOK)


def _dec(s):
    return s.replace(NL_TOK, "\n").replace(CR_TOK, "\r")


def _sha(data):
    return hashlib.sha256(data if isinstance(data, bytes) else data.encode("utf-8")).hexdigest()


def _nsha(raw):
    """sha256 ignoring LF/CRLF (git core.autocrlf flips working-tree endings on checkout)."""
    return _sha(raw.replace(b"\r\n", b"\n"))


def _same_newlines(text, like):
    """Give `text` the newline style of the bytes `like` when that file is purely LF or CRLF."""
    if not like:
        return text
    lf_only = text.replace("\r\n", "\n")
    if b"\r\n" in like:
        return text if b"\n" in like.replace(b"\r\n", b"") else lf_only.replace("\n", "\r\n")
    return lf_only


def _is_str_const(n):
    return isinstance(n, ast.Constant) and isinstance(n.value, str)


def _flatten_add(n):
    if isinstance(n, ast.BinOp) and isinstance(n.op, ast.Add):
        return _flatten_add(n.left) + _flatten_add(n.right)
    return [n]


def is_str_expr(n):
    """Constant str, f-string, '+' chain holding a literal, or 'literal % x'."""
    if _is_str_const(n) or isinstance(n, ast.JoinedStr):
        return True
    if isinstance(n, ast.BinOp) and isinstance(n.op, ast.Add):
        return any(_is_str_const(o) or isinstance(o, ast.JoinedStr) for o in _flatten_add(n))
    if isinstance(n, ast.BinOp) and isinstance(n.op, ast.Mod):
        return _is_str_const(n.left)
    return False


def _callee(func):
    if isinstance(func, ast.Name):
        return func.id
    if isinstance(func, ast.Attribute):
        return func.attr
    return None


def _dotted(func):
    if isinstance(func, ast.Name):
        return func.id
    if isinstance(func, ast.Attribute):
        base = _dotted(func.value)
        return (base or "") + "." + func.attr
    return None


def _cite_rid(n):
    if (isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == "_c"
            and len(n.args) == 1 and not n.keywords and _is_str_const(n.args[0])
            and re.fullmatch(r"[^\s" + LB + RB + "]+", n.args[0].value)):
        return n.args[0].value
    return None


def _docstring_skip(body):
    return 1 if body and isinstance(body[0], ast.Expr) and _is_str_const(body[0].value) else 0


def _strip_markup(s):
    s = ANY_TOK_RE.sub(" ", s)
    s = TAG_RE.sub(" ", s)
    return ENTITY_RE.sub(" ", s)


def _words(s):
    return [w for w in _strip_markup(s).split() if re.search(r"[A-Za-z]", w)]


def label_ok(s):
    """True when the text holds at least one real word: not only digits, symbols, units,
    entities, tags or placeholders."""
    for tok in re.findall(r"[^\s\-–—/(),;:.+=×·*&#\[\]{}<>|]+", _strip_markup(s)):
        if re.search(r"\d", tok):
            continue
        letters = re.sub(r"[^A-Za-z]", "", tok)
        if len(letters) >= 2 and tok.lower().strip("'’\"%°µ") not in UNIT_WORDS:
            return True
    return False


def _vis_len(s):
    s = ANY_TOK_RE.sub("", s)
    return len(_html.unescape(TAG_RE.sub("", s)))


def _short(src, n=80):
    s = " ".join(src.split())
    return s if len(s) <= n else s[: n - 3] + "..."


def _preview(s, n=90):
    return _short(_enc(s), n)


def misc_reject(lit):
    """Why a non-helper string is NOT prose (None = keep as misc).  Conservative."""
    low = lit.lower()
    if any(m in low for m in SVG_MARKERS):
        return "svg"
    if "\n" in lit or "\r" in lit:
        return "multiline"
    if re.search(r"<[A-Za-z][^<>]*\b(?:class|id|src|style|width|height|data-[\w-]+)\s*=", lit) or \
            re.search(r"<(?:div|section|figure|figcaption|img|table|tr|td|th|thead|tbody|header|"
                      r"footer|style|script|pre|form|input|button|nav|main|html|body|head)\b", lit, re.I):
        return "markup"
    if re.search(r"\(\?[:=!<P]|\[\^|\\[dswbDSWB]|\.\*\??|\.\+\??", lit):
        return "regex"
    if len(re.findall(r"[\w-]+\s*:\s*[^;:]{1,40};", lit)) >= 2:
        return "css"
    if re.search(r"(?:https?|ftp)://", lit) and " " not in lit.strip():
        return "url"
    if len(_words(lit)) < 4:
        return "short"
    return None


def _prose_like(lit, n=3):
    return len(_words(lit)) >= n


def _slug_like(s):
    return bool(re.fullmatch(r"[a-z0-9_\-./#%:]*", s.strip()))


def _path_like(s):
    s = s.strip()
    return bool(re.fullmatch(r"[\w.\-]+(?:/[\w.\-]+)+", s) or re.search(r"\.(?:png|jpe?g|webp|svg|gif|json|py|html?)$", s))


def _count_pct(s):
    """(argument-consuming specifiers, stray '%' signs) of a %-template."""
    n, bad, i = 0, 0, s.find("%")
    while i != -1:
        m = PCT_RE.match(s, i)
        if not m:
            bad += 1
            i = s.find("%", i + 1)
            continue
        if m.group(0)[-1] != "%":
            n += 1
        i = s.find("%", m.end())
    return n, bad


def tag_residue(s, kind):
    """Unbalanced-tag signature of a text; compared original vs edited."""
    s = ANY_TOK_RE.sub(" ", s)
    if kind in ("p", "lead"):
        s = re.sub(r"</p>\s*<p>", " ", s, flags=re.I)
    stack, res = [], []
    for m in TAG_RE.finditer(s):
        close, name, selfc = m.group(1), m.group(2).lower(), m.group(3)
        if name in VOID_TAGS or selfc:
            continue
        if not close:
            stack.append(name)
        elif stack and stack[-1] == name:
            stack.pop()
        elif name in stack:
            while stack[-1] != name:
                res.append("<%s> not closed" % stack.pop())
            stack.pop()
        else:
            res.append("</%s> has no opening tag" % name)
    res += ["<%s> not closed" % n for n in stack]
    return res


def _tag_counts(s):
    return collections.Counter(m.group(2).lower() for m in TAG_RE.finditer(ANY_TOK_RE.sub(" ", s))
                               if not m.group(1))


def _numbers(s):
    s = ENTITY_RE.sub(" ", TAG_RE.sub(" ", ANY_TOK_RE.sub(" ", s)))
    return collections.Counter(NUM_RE.findall(s))


def _counter_diff(a, b):
    out = []
    for k in sorted(set(a) | set(b)):
        d = b[k] - a[k]
        if d < 0:
            out.extend(["-" + k] * -d)
        elif d > 0:
            out.extend(["+" + k] * d)
    return " ".join(out)


def _is_diagram_label(s):
    return s.kind == "svglabel" or (s.kind == "label" and " in=" in s.ctx) or \
        (s.kind == "misc" and re.search(r" in=\w+\.\w+", s.ctx) is not None)


# ============================================================================ source text
class Source:
    """Original text (line endings preserved) + AST position -> character offset."""

    def __init__(self, text):
        self.text = text
        self.starts = [0] + [m.end() for m in re.finditer(r"\r\n|\r|\n", text)]
        self._lines = {}

    def line(self, n):
        if n not in self._lines:
            a = self.starts[n - 1]
            b = self.starts[n] if n < len(self.starts) else len(self.text)
            self._lines[n] = self.text[a:b].rstrip("\r\n")
        return self._lines[n]

    def off(self, lineno, col):
        ln = self.line(lineno)
        if not ln.isascii():
            col = len(ln.encode("utf-8")[:col].decode("utf-8"))
        return self.starts[lineno - 1] + col

    def span(self, node):
        return self.off(node.lineno, node.col_offset), self.off(node.end_lineno, node.end_col_offset)

    def col(self, off):
        return off - self.starts[bisect.bisect_right(self.starts, off) - 1]

    def lineno(self, off):
        return bisect.bisect_right(self.starts, off)


def decode_source(raw):
    bom = raw.startswith(b"\xef\xbb\xbf")
    text = raw[3:].decode("utf-8") if bom else raw.decode("utf-8")
    nl = "\r\n" if "\r\n" in text else "\n"
    return text, bom, nl


def encode_source(text, bom):
    return (b"\xef\xbb\xbf" if bom else b"") + text.encode("utf-8")


# ============================================================================ slots
@dataclasses.dataclass
class PH:
    tok: str        # placeholder token as shown in the unit text
    ptype: str      # "op" (+ operand) | "field" (f-string field, src = text inside {}) | "mod"
    start: int      # span of src in the original text
    end: int
    src: str
    paren: bool     # wrap in () when emitted as an operand


@dataclasses.dataclass
class Slot:
    kind: str
    ctx: str
    start: int
    end: int
    line: int
    text: str       # unit text (encoded, whitespace-stripped)
    lead: str
    trail: str
    phs: list
    mod: object     # PH or None
    pct: int
    wrap: bool
    col0: int       # column where the slot starts
    expr: str       # str | concat | fstr | mod | inner (element text in a literal) | json
    indent: str = ""   # continuation-line indent used by the original (wrapped) slot
    uid: str = ""
    parent: str = None
    has_comment: bool = False
    carrier: str = None    # inner units: id of the literal (Carrier) holding the element
    vstart: int = 0        # inner units: content range in the carrier value (a field = 1 char)
    vend: int = 0
    exact: dict = None     # source range + string-token context for an in-place patch
    elem: str = ""         # inner units: element name

    def all_phs(self):
        return self.phs + ([self.mod] if self.mod else [])

    def to_meta(self):
        d = dataclasses.asdict(self)
        d["placeholders"] = d.pop("phs")
        return d

    @classmethod
    def from_meta(cls, d):
        d = dict(d)
        d["phs"] = [PH(**p) for p in d.pop("placeholders")]
        d["mod"] = PH(**d["mod"]) if d["mod"] else None
        return cls(**d)


@dataclasses.dataclass
class Carrier:
    """A string literal (Constant / f-string, implicit concatenation included) that holds
    inner units.  segs = [["t", text] | ["f", field index]]; fields = PH of each {...}."""
    cid: str
    start: int
    end: int
    col0: int
    indent: str
    wrap: bool
    segs: list
    fields: list
    exact_ok: bool

    def atoms(self):
        out = []
        for k, v in self.segs:
            if k == "t":
                out.extend(v)
            else:
                out.append(v)
        return out

    def to_meta(self):
        return dataclasses.asdict(self)

    @classmethod
    def from_meta(cls, d):
        d = dict(d)
        d["fields"] = [PH(**p) for p in d["fields"]]
        return cls(**d)


def _needs_paren(node, where):
    if isinstance(node, ATOMS):
        return False
    if where == "op" and isinstance(node, ast.BinOp) and isinstance(
            node.op, (ast.Mult, ast.Div, ast.FloorDiv, ast.Mod, ast.MatMult, ast.Pow)):
        return False
    return True


def parts_of(node, S):
    """Split a string expression into [("lit", str) | ("ph", PH, node)] and an optional
    %-operand PH.  Raises Unsupported for shapes the emitter cannot reproduce."""
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Mod):
        if not _is_str_const(node.left):
            raise Unsupported("%-format with a non-literal template")
        a, b = S.span(node.right)
        return [("lit", node.left.value)], PH(None, "mod", a, b, S.text[a:b], _needs_paren(node.right, "mod"))
    parts = []
    for op in _flatten_add(node):
        if _is_str_const(op):
            parts.append(("lit", op.value))
        elif isinstance(op, ast.JoinedStr):
            for v in op.values:
                if _is_str_const(v):
                    parts.append(("lit", v.value))
                elif isinstance(v, ast.FormattedValue):
                    a, b = S.span(v)
                    if S.text[a:a + 1] != "{" or S.text[b - 1:b] != "}":
                        raise Unsupported("f-string field position not recoverable")
                    parts.append(("ph", PH(None, "field", a + 1, b - 1, S.text[a + 1:b - 1], False), v))
                else:
                    raise Unsupported("unexpected f-string part " + type(v).__name__)
        else:
            a, b = S.span(op)
            parts.append(("ph", PH(None, "op", a, b, S.text[a:b], _needs_paren(op, "op")), op))
    return parts, None


def _parts_signature(parts, mod):
    out = []
    for p in parts:
        out.append(p[1] if p[0] == "lit" else "\0%s\0%s\0" % (p[1].ptype, p[1].src))
    return "".join(out), (mod.src if mod else None)


# ============================================================================ emitter
def _esc(s, q, is_f):
    out = []
    for ch in s:
        o = ord(ch)
        if ch == "\\":
            out.append("\\\\")
        elif ch == q:
            out.append("\\" + q)
        elif ch == "\n":
            out.append("\\n")
        elif ch == "\r":
            out.append("\\r")
        elif ch == "\t":
            out.append("\\t")
        elif is_f and ch in "{}":
            out.append(ch * 2)
        elif o < 0x20 or 0x7f <= o < 0xa0 or o in (0x2028, 0x2029, 0xfeff) or 0xd800 <= o < 0xe000:
            out.append("\\x%02x" % o if o < 0x100 else "\\u%04x" % o)
        else:
            out.append(ch)
    return "".join(out)


def _seg_text(segs):
    return "".join(s for k, s in segs if k == "text")


def _quote_for(segs):
    t = _seg_text(segs)
    return "'" if t.count('"') > t.count("'") else '"'


def _lit(segs, q):
    is_f = any(k == "field" for k, _ in segs)
    body = "".join(_esc(s, q, is_f) if k == "text" else "{" + s + "}" for k, s in segs)
    return ("f" if is_f else "") + q + body + q


def _split_piece(segs, q, first_room, room):
    """Split one string piece at spaces into chunks whose literal fits the room."""
    is_f = any(k == "field" for k, _ in segs)
    toks = []
    for k, s in segs:
        if k == "field":
            toks.append(("field", s))
        else:
            toks.extend(("text", w) for w in re.findall(r"\S+\s*|\s+", s))
    chunks, cur, used, limit = [], [], 3, first_room
    for t in toks:
        tl = len(_esc(t[1], q, is_f)) if t[0] == "text" else len(t[1]) + 2
        if cur and used + tl > limit:
            chunks.append(cur)
            cur, used, limit = [], 3, room
        cur.append(t)
        used += tl
    if cur:
        chunks.append(cur)
    merged = []
    for c in chunks:
        segs2 = []
        for k, s in c:
            if k == "text" and segs2 and segs2[-1][0] == "text":
                segs2[-1] = ("text", segs2[-1][1] + s)
            else:
                segs2.append((k, s))
        merged.append(segs2)
    return merged


def _layout(pieces, col0, nl, wrap, indent, width=WRAP_WIDTH):
    """pieces: ("str", segs) | ("op", code).  One line, or wrapped like the source style:
    first line continues at col0, continuation lines start with `indent`."""
    if not pieces:
        return '""'
    single = " + ".join(_lit(p[1], _quote_for(p[1])) if p[0] == "str" else p[1] for p in pieces)
    if not wrap or (col0 + len(single) <= width and "\n" not in single):
        return single
    ind = len(indent)
    out, col = [], col0
    for i, p in enumerate(pieces):
        lead = " + " if i else ""
        if p[0] == "op":
            code = p[1]
            if i and "\n" not in code and col + len(lead) + len(code) > width:
                out.append(" +" + nl + indent)
                col, lead = ind, ""
            out.append(lead + code)
            col = (col + len(lead) + len(code)) if "\n" not in code else len(code.rsplit("\n", 1)[-1])
            continue
        q = _quote_for(p[1])
        room = max(width - ind - 2, 24)
        first = width - col - len(lead) - 2
        if i and first < 24:
            out.append(" +" + nl + indent)
            col, lead, first = ind, "", room
        for j, ch in enumerate(_split_piece(p[1], q, first, room)):
            code = _lit(ch, q)
            if j == 0:
                out.append(lead + code)
                col += len(lead) + len(code)
            else:
                out.append(nl + indent + code)
                col = ind + len(code)
    return "".join(out)


def emit_code(slot, text, ph_srcs, mod_src, nl):
    """Python source for a slot whose unit text is `text` (encoded, stripped)."""
    value = _dec(slot.lead + text + slot.trail)
    queues = collections.defaultdict(collections.deque)
    for i, ph in enumerate(slot.phs):
        queues[ph.tok].append(i)
    pieces = []

    def add(kind, s):
        if kind == "text" and not s:
            return
        if pieces and pieces[-1][0] == "str":
            pieces[-1][1].append((kind, s))
        else:
            pieces.append(("str", [(kind, s)]))

    pos = 0
    for m in PH_RE.finditer(value):
        add("text", value[pos:m.start()])
        pos = m.end()
        i = queues[m.group(0)].popleft()
        ph = slot.phs[i]
        if ph.ptype == "field":
            add("field", ph_srcs[i])
        else:
            pieces.append(("op", "(" + ph_srcs[i] + ")" if ph.paren else ph_srcs[i]))
    add("text", value[pos:])
    indent = slot.indent or " " * slot.col0
    if slot.mod is not None:
        fmt = pieces[0][1] if pieces else [("text", "")]
        right = "(" + mod_src + ")" if slot.mod.paren else mod_src
        return _layout([("str", fmt)], slot.col0, nl, slot.wrap, indent) + " % " + right
    return _layout(pieces, slot.col0, nl, slot.wrap, indent)


def _encode_for_token(s, t):
    """Literal text `s` written inside an existing string token (context t).  None when the
    token cannot hold it (raw strings with quotes / backslashes / newlines)."""
    if t.get("json"):
        return json.dumps(s, ensure_ascii=False)[1:-1]
    qc = t["quote"][0]
    if t["raw"]:
        if qc in s or "\\" in s or "\r" in s or ("\n" in s and not t["triple"]):
            return None
        return s.replace("{", "{{").replace("}", "}}") if t["fstr"] else s
    return _esc(s, qc, t["fstr"])


def _unit_pieces(u, text):
    """Split a unit's new text into [("text", s) | ("ph", index into u.phs)]."""
    value = _dec(u.lead + text + u.trail)
    queues = collections.defaultdict(collections.deque)
    for i, ph in enumerate(u.phs):
        queues[ph.tok].append(i)
    out, pos = [], 0
    for m in PH_RE.finditer(value):
        if m.start() > pos:
            out.append(("text", value[pos:m.start()]))
        out.append(("ph", queues[m.group(0)].popleft()))
        pos = m.end()
    if pos < len(value):
        out.append(("text", value[pos:]))
    return out


def emit_inner_exact(u, text, ph_srcs):
    """Replacement for the source range u.exact (inside one string token), or None."""
    out = []
    for k, v in _unit_pieces(u, text):
        if k == "text":
            enc = _encode_for_token(v, u.exact)
            if enc is None:
                return None
            out.append(enc)
        else:
            if not u.exact.get("fstr"):
                return None
            out.append("{" + ph_srcs[v] + "}")
    return "".join(out)


def emit_carrier(c, changes, fsrc, nl):
    """Re-emit a whole carrier literal with the changed inner units spliced in."""
    atoms = c.atoms()
    fmap = {f.start: k for k, f in enumerate(c.fields)}
    chg = sorted(changes, key=lambda ut: ut[0].vstart)
    segs = []

    def add(kind, s):
        if kind == "text" and not s:
            return
        if segs and kind == "text" and segs[-1][0] == "text":
            segs[-1] = ("text", segs[-1][1] + s)
        else:
            segs.append((kind, s))

    i, ci = 0, 0
    while i < len(atoms):
        if ci < len(chg) and chg[ci][0].vstart == i:
            u, text = chg[ci]
            for k, v in _unit_pieces(u, text):
                add("text", v) if k == "text" else add("field", fsrc[fmap[u.phs[v].start]])
            i, ci = u.vend, ci + 1
            continue
        a = atoms[i]
        add("text", a) if isinstance(a, str) else add("field", fsrc[a])
        i += 1
    if not segs:
        segs = [("text", "")]
    return _layout([("str", segs)], c.col0, nl, c.wrap, c.indent or " " * c.col0)


def patch_source(text, slots, new_texts, nl, force=False, carriers=None):
    """Rebuild `text` with every changed unit re-emitted (nested units rendered first).
    Inner units are patched through their carrier literal."""
    cmap = {c.cid: c for c in (carriers or [])}
    plain = [s for s in slots if s.expr != "inner"]
    inner = collections.defaultdict(list)
    for s in slots:
        if s.expr == "inner":
            inner[s.carrier].append(s)
    nodes = plain + [cmap[cid] for cid in inner]
    order = sorted(nodes, key=lambda n: (n.start, -n.end))
    kids = {id(n): [] for n in order}
    top, stack = [], []
    for n in order:
        while stack and n.start >= stack[-1].end:
            stack.pop()
        if stack and n.end > stack[-1].end:
            raise RuntimeError("unit at offset %d overlaps another unit" % n.start)
        (kids[id(stack[-1])] if stack else top).append(n)
        stack.append(n)
    changed = {s.uid for s in slots if force or new_texts.get(s.uid, s.text) != s.text}

    def newt(s):
        return s.text if force else new_texts.get(s.uid, s.text)

    def rng(a, b, inner_nodes):
        out, pos = [], a
        for k in inner_nodes:
            if a <= k.start and k.end <= b:
                out.append(text[pos:k.start])
                out.append(one(k))
                pos = k.end
        out.append(text[pos:b])
        return "".join(out)

    def one(n):
        if isinstance(n, Carrier):
            return carrier_out(n)
        if n.uid not in changed:
            return rng(n.start, n.end, kids[id(n)])
        srcs = [rng(ph.start, ph.end, kids[id(n)]) for ph in n.phs]
        mod_src = rng(n.mod.start, n.mod.end, kids[id(n)]) if n.mod else None
        return emit_code(n, newt(n), srcs, mod_src, nl)

    def carrier_out(c):
        k = kids[id(c)]
        ch = [u for u in inner[c.cid] if u.uid in changed]
        if not ch:
            return rng(c.start, c.end, k)
        fsrc = [rng(f.start, f.end, k) for f in c.fields]
        fmap = {f.start: i for i, f in enumerate(c.fields)}
        if c.exact_ok and all(u.exact for u in ch):
            reps = []
            for u in ch:
                code = emit_inner_exact(u, newt(u), [fsrc[fmap[ph.start]] for ph in u.phs])
                if code is None:
                    break
                reps.append((u.exact["start"], u.exact["end"], code))
            else:
                out, pos = [], c.start
                for a, b, code in sorted(reps):
                    out.append(rng(pos, a, k))
                    out.append(code)
                    pos = b
                out.append(rng(pos, c.end, k))
                return "".join(out)
        return emit_carrier(c, [(u, newt(u)) for u in ch], fsrc, nl)

    return rng(0, len(text), top)


def patch_json(text, slots, new_texts, force=False):
    """JSON targets: every unit is an exact range inside one JSON string."""
    reps = []
    for s in slots:
        t = s.text if force else new_texts.get(s.uid, s.text)
        if force or t != s.text:
            reps.append((s.exact["start"], s.exact["end"], _encode_for_token(_dec(s.lead + t + s.trail), s.exact)))
    out, pos = [], 0
    for a, b, code in sorted(reps):
        out.append(text[pos:a])
        out.append(code)
        pos = b
    out.append(text[pos:])
    return "".join(out)


# ============================================================================ string decoders
_SIMPLE_ESC = {"\\": "\\", "'": "'", '"': '"', "a": "\a", "b": "\b", "f": "\f", "n": "\n",
               "r": "\r", "t": "\t", "v": "\v"}
_PREFIX_RE = re.compile(r"([A-Za-z]{0,2})('''|\"\"\"|'|\")")


def _py_escape(text, i):
    """Value and source length of the escape sequence at text[i] == '\\' (non-raw string)."""
    c = text[i + 1:i + 2]
    if c == "\n":
        return "", 2
    if c == "\r":
        return "", 3 if text[i + 2:i + 3] == "\n" else 2
    if c in _SIMPLE_ESC:
        return _SIMPLE_ESC[c], 2
    if c and c in "01234567":
        m = re.match(r"[0-7]{1,3}", text[i + 1:i + 4])
        return chr(int(m.group(0), 8)), 1 + len(m.group(0))
    n = {"x": 2, "u": 4, "U": 8}.get(c)
    if n:
        h = text[i + 2:i + 2 + n]
        if len(h) != n or not re.fullmatch(r"[0-9a-fA-F]+", h):
            return None, 0
        return chr(int(h, 16)), 2 + n
    if c == "N" and text[i + 2:i + 3] == "{":
        j = text.find("}", i)
        try:
            return unicodedata.lookup(text[i + 3:j]), j + 1 - i
        except KeyError:
            return None, 0
    return "\\" + c, 2


def _decode_py_token(text, a, b, fields):
    """Decode the string token text[a:b] -> ([(value, src_a, src_b)], ctx); value is a 1-char
    str or the int index of an f-string field (fields = [(span_a, span_b, index)])."""
    m = _PREFIX_RE.match(text, a)
    if not m:
        return None, None
    prefix, q = m.group(1).lower(), m.group(2)
    if "b" in prefix or text[b - len(q):b] != q:
        return None, None
    raw, isf = "r" in prefix, "f" in prefix
    ctx = {"quote": q, "raw": raw, "fstr": isf, "triple": len(q) == 3}
    fstarts = {fa: (fb, k) for fa, fb, k in fields}
    i, end, out = m.end(), b - len(q), []
    while i < end:
        if isf and i in fstarts:
            fb, k = fstarts[i]
            out.append((k, i, fb))
            i = fb
            continue
        ch = text[i]
        if isf and ch in "{}" and text[i + 1:i + 2] == ch:
            out.append((ch, i, i + 2))
            i += 2
            continue
        if ch == "\\" and not raw:
            val, n = _py_escape(text, i)
            if val is None:
                return None, None
            if len(val) == 1:
                out.append((val, i, i + n))
            elif len(val) == 2:
                out.append((val[0], i, i + 1))
                out.append((val[1], i + 1, i + 2))
            i += n
            continue
        if ch == "\r":
            n = 2 if text[i + 1:i + 2] == "\n" else 1
            out.append(("\n", i, i + n))
            i += n
            continue
        out.append((ch, i, i + 1))
        i += 1
    return out, ctx


def json_strings(text):
    """Every string VALUE of a JSON document: [(path, start, end, [(char, a, b)])]."""
    out = []

    def ws(i):
        while i < len(text) and text[i] in " \t\r\n":
            i += 1
        return i

    def string(i):
        atoms, j = [], i + 1
        while True:
            c = text[j]
            if c == '"':
                return atoms, j + 1
            if c == "\\":
                e = text[j + 1]
                if e == "u":
                    cp, n = int(text[j + 2:j + 6], 16), 6
                    if 0xD800 <= cp < 0xDC00 and text[j + 6:j + 8] == "\\u":
                        lo = int(text[j + 8:j + 12], 16)
                        if 0xDC00 <= lo < 0xE000:
                            cp, n = 0x10000 + ((cp - 0xD800) << 10) + (lo - 0xDC00), 12
                    atoms.append((chr(cp), j, j + n))
                    j += n
                    continue
                atoms.append(({'"': '"', "\\": "\\", "/": "/", "b": "\b", "f": "\f", "n": "\n", "r": "\r",
                               "t": "\t"}[e], j, j + 2))
                j += 2
                continue
            atoms.append((c, j, j + 1))
            j += 1

    def value(i, path):
        c = text[i]
        if c == "{":
            i = ws(i + 1)
            if text[i] == "}":
                return i + 1
            while True:
                katoms, i = string(i)
                key = "".join(a[0] for a in katoms)
                i = ws(i)
                if text[i] != ":":
                    raise ValueError("bad JSON at %d" % i)
                i = value(ws(i + 1), path + "/" + key if path else key)
                i = ws(i)
                if text[i] == ",":
                    i = ws(i + 1)
                    continue
                if text[i] != "}":
                    raise ValueError("bad JSON at %d" % i)
                return i + 1
        if c == "[":
            i, k = ws(i + 1), 0
            if text[i] == "]":
                return i + 1
            while True:
                i = ws(value(i, "%s/%d" % (path, k) if path else str(k)))
                k += 1
                if text[i] == ",":
                    i = ws(i + 1)
                    continue
                if text[i] != "]":
                    raise ValueError("bad JSON at %d" % i)
                return i + 1
        if c == '"':
            atoms, j = string(i)
            out.append((path, i, j, atoms))
            return j
        m = re.compile(r"-?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?|true|false|null").match(text, i)
        if not m:
            raise ValueError("bad JSON at %d" % i)
        return m.end()

    value(ws(0), "")
    return out


def html_leaf_elements(s):
    """Leaf block elements of an HTML fragment: [(content_start, content_end, 'tag.class')].
    Elements opened or closed outside the fragment are ignored."""
    stack, out = [], []
    for m in TAG_RE.finditer(s):
        close, name, selfc = m.group(1), m.group(2).lower(), m.group(3)
        if name in VOID_TAGS or selfc:
            continue
        if not close:
            if stack and name in HTML_BLOCK:
                stack[-1][2] = True
            stack.append([name, m.end(), False, m.group(0)])
            continue
        while stack and stack[-1][0] != name:
            stack.pop()
        if not stack:
            continue
        tag, oend, has_block, otext = stack.pop()
        if stack and tag in HTML_BLOCK:
            stack[-1][2] = True
        if tag in HTML_BLOCK and not has_block:
            cm = re.search(r"class=['\"]([^'\"\s]+)", otext)
            out.append((oend, m.start(), tag + ("." + cm.group(1) if cm else "")))
    return out


def svg_elements(s):
    return [(m.start(2), m.end(2), m.group(1).lower()) for m in SVG_EL_RE.finditer(s)]


# ============================================================================ extractor (prose)
@dataclasses.dataclass(frozen=True)
class Ctx:
    label: str = None       # fixed ctx (TITLE, META, d:path, svg=fn ...)
    section: str = None
    ckind: str = None
    fn: str = None
    var: str = None
    callee: str = None
    in_field: bool = False
    excluded: str = None
    gen: bool = False       # inside a figure-generator call (rule f)

    def w(self, **kw):
        return dataclasses.replace(self, **kw)

    def base(self):
        if self.label:
            s = self.label
        elif self.section is not None:
            s = "s:" + self.section
        elif self.var:
            s = "v:" + self.var
        elif self.fn:
            s = "fn:" + self.fn
        else:
            s = "top"
        return s + (" kind=" + self.ckind if self.ckind else "")


class Extractor:
    """Prose units.  profile: paper (paper modules and ipm_blueprint.render), data,
    glossary, evidence."""

    def __init__(self, module, text, profile="paper"):
        self.module = module
        self.profile = profile
        self.S = Source(text)
        self.tree = ast.parse(text, filename=module + ".py")
        self.slots, self.skipped, self.uncaptured, self.short_labels = [], [], [], []
        self.carriers, self.gen_skipped, self.stats_fieldonly = [], [], []
        self.stats = collections.Counter()
        self.helper_units = self.loop_units = 0
        self.wrappers, self.wrapper_notes, self.local_defs = {}, [], set()
        self.deferred, self.deferred_uses = {}, {}
        self.mod_alias, self.name_from = {}, {}
        self._seen = set()
        self._offs, self._cum, self._comments, self._strtoks = self._scan_tokens(text)

    # ---------------------------------------------------------------- setup
    def _scan_tokens(self, text):
        offs, cum, comments, strs, fstack, d = [], [], [], [], [], 0
        try:
            for tok in tokenize.generate_tokens(io.StringIO(text).readline):
                a = self.S.starts[tok.start[0] - 1] + tok.start[1]
                if tok.type == tokenize.OP and tok.string in ("(", "[", "{", ")", "]", "}"):
                    d += 1 if tok.string in "([{" else -1
                    offs.append(a)
                    cum.append(d)
                elif tok.type == tokenize.COMMENT:
                    comments.append(a)
                elif tok.type == tokenize.STRING:
                    strs.append((a, self.S.starts[tok.end[0] - 1] + tok.end[1]))
                elif tok.type == getattr(tokenize, "FSTRING_START", -1):
                    fstack.append(a)
                elif tok.type == getattr(tokenize, "FSTRING_END", -1) and fstack:
                    strs.append((fstack.pop(), self.S.starts[tok.end[0] - 1] + tok.end[1]))
        except (tokenize.TokenError, SyntaxError):
            return None, None, [], None
        strs.sort()
        return offs, cum, comments, strs

    def _depth(self, off):
        if self._offs is None:
            return 0
        i = bisect.bisect_left(self._offs, off)
        return self._cum[i - 1] if i else 0

    def run(self):
        self._prepass()
        if self.profile == "paper":
            self._walk_module()
            self._finish_deferred()
        else:
            self._walk_data_module()
        self._number()
        return self

    def _imports(self):
        for st in ast.walk(self.tree):
            if isinstance(st, ast.Import):
                for a in st.names:
                    self.mod_alias[a.asname or a.name] = a.name
            elif isinstance(st, ast.ImportFrom) and st.module and not st.level:
                for a in st.names:
                    self.name_from[a.asname or a.name] = (st.module, a.name)

    def _prepass(self):
        self._imports()
        body = self.tree.body
        self.local_defs = {n.name for n in body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))}
        if self.profile != "paper":
            return
        overrides = LOCAL_WRAPPERS.get(self.module, {})
        for fn in body:
            if not isinstance(fn, ast.FunctionDef):
                continue
            params = [a.arg for a in fn.args.posonlyargs + fn.args.args + fn.args.kwonlyargs]
            roles = dict(overrides.get(fn.name, {}))
            if not roles:
                for sub in ast.walk(fn):
                    if not isinstance(sub, ast.Call):
                        continue
                    name = _callee(sub.func)
                    if name not in HELPERS or name in self.local_defs:
                        continue
                    for param, role, arg in self._bind(sub, HELPERS[name]):
                        if role is not None and role != "walk" and isinstance(arg, ast.Name) and arg.id in params:
                            roles.setdefault(arg.id, role)
            if roles:
                self.wrappers[fn.name] = [(p, roles.get(p)) for p in params]
                how = "hand-mapped" if fn.name in overrides else "inferred"
                self.wrapper_notes.append("%s(%s) %s" % (fn.name, ", ".join(
                    "%s=%s" % (p, r if isinstance(r, str) else "/".join(x for x in r if x))
                    for p, r in self.wrappers[fn.name] if r), how))
        counts = collections.Counter(t.id for st in body if isinstance(st, ast.Assign)
                                     for t in st.targets if isinstance(t, ast.Name))
        for st in body:
            if (isinstance(st, ast.Assign) and len(st.targets) == 1 and isinstance(st.targets[0], ast.Name)
                    and counts[st.targets[0].id] == 1 and is_str_expr(st.value)
                    and st.targets[0].id not in SKIP_NAMES and st.targets[0].id not in MODULE_KINDS):
                self.deferred[st.targets[0].id] = st.value

    @staticmethod
    def _bind(call, spec):
        params = [p for p, _ in spec]
        roles = dict(spec)
        out = []
        for i, a in enumerate(call.args):
            if isinstance(a, ast.Starred) or i >= len(params):
                out.append((None, None, a))
            else:
                out.append((params[i], roles[params[i]], a))
        for k in call.keywords:
            out.append((k.arg, roles.get(k.arg), k.value))
        return out

    def _generator(self, func):
        """Rule (f): figure-generator spec for a call, or None."""
        if isinstance(func, ast.Attribute) and isinstance(func.value, ast.Name) and func.value.id in self.mod_alias:
            return FIG_GENERATORS.get(self.mod_alias[func.value.id], {}).get(func.attr)
        if isinstance(func, ast.Name) and func.id in self.name_from and func.id not in self.local_defs:
            mod, attr = self.name_from[func.id]
            return FIG_GENERATORS.get(mod, {}).get(attr)
        return None

    # ---------------------------------------------------------------- walking
    def _walk_module(self):
        body = self.tree.body
        for st in body[_docstring_skip(body):]:
            if isinstance(st, ast.Assign) and len(st.targets) == 1 and isinstance(st.targets[0], ast.Name):
                name = st.targets[0].id
                if name in MODULE_KINDS:
                    self.take_prose(st.value, MODULE_KINDS[name], Ctx(label=name))
                    continue
                if name == "META":
                    self.take_pairs(st.value, None, "meta", Ctx(label="META"))
                    continue
                if name in SKIP_NAMES or name in self.deferred:
                    continue
                self.walk(st.value, Ctx(var=name))
                continue
            self.walk(st, Ctx())

    def walk(self, node, ctx):
        if node is None:
            return
        if isinstance(node, list):
            for n in node:
                self.walk(n, ctx)
            return
        if isinstance(node, ast.expr) and is_str_expr(node):
            self.misc(node, ctx)
            return
        handler = getattr(self, "w_" + type(node).__name__, None)
        if handler:
            handler(node, ctx)
            return
        for child in ast.iter_child_nodes(node):
            self.walk(child, ctx)

    def w_FunctionDef(self, node, ctx):
        reason = ctx.excluded
        if not reason and (node.name.startswith("_fig") or node.name.startswith("_g_")):
            reason = "inside %s()" % node.name
        if not reason:
            for sub in ast.walk(node):
                vals = [sub.value] if _is_str_const(sub) else []
                if any(m in v.lower() for v in vals for m in SVG_MARKERS):
                    reason = "inside %s() (SVG/markup builder)" % node.name
                    break
        c = ctx.w(fn=node.name, var=None, excluded=reason)
        self.walk(node.decorator_list, ctx)
        self.walk(node.args, c)
        for st in node.body[_docstring_skip(node.body):]:
            self.walk(st, c)

    w_AsyncFunctionDef = w_FunctionDef

    def w_ClassDef(self, node, ctx):
        for st in node.body[_docstring_skip(node.body):]:
            self.walk(st, ctx.w(fn=node.name))

    def w_Raise(self, node, ctx):
        return

    def w_Assert(self, node, ctx):
        return

    def w_Import(self, node, ctx):
        return

    w_ImportFrom = w_Import

    def w_FormattedValue(self, node, ctx):
        self.walk(node.value, ctx.w(in_field=True))

    def w_Dict(self, node, ctx):
        keys = [k.value if _is_str_const(k) else None for k in node.keys]
        if "blocks" in keys:
            sid = next((v.value for k, v in zip(keys, node.values) if k == "id" and _is_str_const(v)), "?")
            c = ctx.w(section=sid, ckind=None, callee=None, label=None, gen=False)
            for k, v in zip(keys, node.values):
                if k == "id":
                    continue
                if k == "kicker":
                    self.take_prose(v, "kicker", c)
                elif k == "title":
                    self.take_prose(v, "section.title", c)
                else:
                    self.walk(v, c)
            return
        for k, kname, v in zip(node.keys, keys, node.values):
            if k is not None and not isinstance(k, ast.Constant):
                self.walk(k, ctx)
            if kname != "id":
                self.walk(v, ctx)

    def w_Call(self, node, ctx):
        name = _callee(node.func)
        if name == "print" and isinstance(node.func, ast.Name):
            return
        gen = self._generator(node.func)
        if gen is not None:
            self._take_generator(node, gen, ctx)
            return
        spec = None
        if not ctx.excluded:
            if isinstance(node.func, ast.Name) and name in self.wrappers:
                spec = self.wrappers[name]
            elif name in HELPERS and name not in self.local_defs:
                spec = HELPERS[name]
        if spec is None:
            self.walk(node.func, ctx)
            c = ctx.w(callee=_dotted(node.func), gen=False)
            self.walk(node.args, c)
            for k in node.keywords:
                self.walk(k.value, c)
            return
        c = ctx.w(callee=None, gen=False)
        if name == "callout" and node.args and _is_str_const(node.args[0]):
            c = c.w(ckind=node.args[0].value)
        for _param, role, arg in self._bind(node, spec):
            if role is None:
                self.walk(arg, c.w(callee=name))
            elif role == "walk":
                self.walk(arg, c)
            elif isinstance(role, str):
                self.take_prose(arg, role, c)
            elif role[0] == "list":
                self.take_list(arg, role[1], c)
            elif role[0] == "rows":
                self.take_rows(arg, role[1], c)
            elif role[0] == "pairs":
                self.take_pairs(arg, role[1], role[2], c)

    # ---------------------------------------------------------------- rule (f)
    def _take_generator(self, node, spec, ctx):
        c = ctx.w(callee=_dotted(node.func), gen=True)
        self.walk(node.func, ctx)
        for _param, role, arg in self._bind(node, spec):
            if role is None:
                self.walk(arg, c)
            elif role == "text":
                self.take_label(arg, c)
            elif role[0] == "items":
                self.take_items(arg, role[1], c)
            elif role[0] == "list":
                self.take_label_list(arg, c)

    def take_label(self, node, ctx):
        if node is None:
            return
        if is_str_expr(node):
            lit = self._literal_preview(node)
            if label_ok(lit):
                self.make_slot(node, "label", ctx, allow_excluded=True)
            else:
                self.gen_skipped.append((node.lineno, ctx.callee, _preview(lit, 50)))
                self.walk_subnodes(node, ctx)
        elif isinstance(node, ast.IfExp):
            self.walk(node.test, ctx)
            self.take_label(node.body, ctx)
            self.take_label(node.orelse, ctx)
        else:
            self.walk(node, ctx)

    def take_label_list(self, node, ctx):
        if isinstance(node, (ast.List, ast.Tuple)):
            for e in node.elts:
                self.take_label(e, ctx) if not isinstance(e, ast.Starred) else self.walk(e, ctx)
        elif isinstance(node, (ast.ListComp, ast.GeneratorExp)):
            self.walk(node.generators, ctx)
            self.take_label(node.elt, ctx)
        else:
            self.walk(node, ctx)

    def take_items(self, node, idxs, ctx):
        if isinstance(node, (ast.ListComp, ast.GeneratorExp)):
            self.walk(node.generators, ctx)
            elts = [node.elt]
        elif isinstance(node, (ast.List, ast.Tuple)):
            elts = node.elts
        else:
            self.walk(node, ctx)
            return
        for e in elts:
            if isinstance(e, (ast.Tuple, ast.List)):
                for j, x in enumerate(e.elts):
                    self.take_label(x, ctx) if j in idxs else self.walk(x, ctx)
            else:
                self.walk(e, ctx)

    # ---------------------------------------------------------------- prose positions
    def take_prose(self, node, kind, ctx):
        if node is None:
            return
        if is_str_expr(node):
            self.make_slot(node, kind, ctx)
        elif isinstance(node, ast.IfExp):
            self.walk(node.test, ctx)
            self.take_prose(node.body, kind, ctx)
            self.take_prose(node.orelse, kind, ctx)
        elif isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
            for o in _flatten_add(node):
                self.take_prose(o, kind, ctx)
        elif isinstance(node, ast.Name) and node.id in self.deferred:
            self.deferred_uses.setdefault(node.id, (kind, ctx))
        else:
            self.walk(node, ctx)

    def take_list(self, node, kind, ctx):
        if isinstance(node, (ast.List, ast.Tuple)):
            for e in node.elts:
                if isinstance(e, ast.Starred):
                    self.walk(e, ctx)
                else:
                    self.take_prose(e, kind, ctx)
        elif isinstance(node, (ast.ListComp, ast.GeneratorExp)):
            self.walk(node.generators, ctx)
            self.take_prose(node.elt, kind, ctx)
        else:
            self.walk(node, ctx)

    def take_rows(self, node, kind, ctx):
        if isinstance(node, (ast.List, ast.Tuple)):
            for row in node.elts:
                self.take_list(row, kind, ctx)
        elif isinstance(node, (ast.ListComp, ast.GeneratorExp)):
            self.walk(node.generators, ctx)
            self.take_list(node.elt, kind, ctx)
        else:
            self.walk(node, ctx)

    def take_pairs(self, node, k1, k2, ctx):
        if isinstance(node, (ast.ListComp, ast.GeneratorExp)):
            self.walk(node.generators, ctx)
            elts = [node.elt]
        elif isinstance(node, (ast.List, ast.Tuple)):
            elts = node.elts
        else:
            self.walk(node, ctx)
            return
        for e in elts:
            if isinstance(e, (ast.Tuple, ast.List)) and len(e.elts) >= 2:
                for j, x in enumerate(e.elts):
                    role = k1 if j == 0 else (k2 if j == 1 else None)
                    if role is None:
                        self.walk(x, ctx)
                    else:
                        self.take_prose(x, role, ctx)
            else:
                self.walk(e, ctx)

    # ---------------------------------------------------------------- data modules
    def _walk_data_module(self):
        body = self.tree.body
        for st in body[_docstring_skip(body):]:
            if isinstance(st, ast.Assign) and len(st.targets) == 1 and isinstance(st.targets[0], ast.Name):
                name = st.targets[0].id
                if name in MODULE_KINDS:
                    self.take_prose(st.value, MODULE_KINDS[name], Ctx(label=name))
                elif name == "META":
                    self.take_pairs(st.value, None, "meta", Ctx(label="META"))
                elif name not in SKIP_NAMES and re.fullmatch(r"[A-Z][A-Z0-9_]*", name):
                    self._data(st.value, name, None, None)
            elif isinstance(st, ast.FunctionDef) and self.profile == "evidence" and st.name == "panel_html":
                self._html_function(st)

    def _data(self, node, path, key, term):
        if isinstance(node, ast.Dict):
            t = next((v.value for k, v in zip(node.keys, node.values)
                      if _is_str_const(k) and k.value == "term" and _is_str_const(v)), term)
            for k, v in zip(node.keys, node.values):
                if _is_str_const(k):
                    self._data(v, "%s.%s" % (path, k.value), k.value, t)
            return
        if isinstance(node, (ast.List, ast.Tuple)):
            for i, e in enumerate(node.elts):
                self._data(e, "%s[%d]" % (path, i), key, term)
            return
        if not is_str_expr(node):
            return
        lit = self._literal_preview(node)
        kind = self._data_kind(lit, key)
        if kind:
            extra = " term=%s" % _short(term, 40) if (self.profile == "glossary" and term) else ""
            self.make_slot(node, kind, Ctx(label="d:" + path + extra))

    def _data_kind(self, lit, key):
        if self.profile == "glossary":
            return "defterm.body" if key == "defn" else None
        if self.profile == "evidence":
            return "li" if _words(lit) else None
        if key in DATA_SKIP_KEYS or _path_like(lit):
            return None
        if misc_reject(lit) not in (None, "short"):
            return None
        n = len(_words(lit))
        if key in TITLE_KEYS:
            return "label" if n >= 2 else None
        if n >= 4:
            return "text"
        if key is None and n >= 2 and not _slug_like(lit):
            return "label"
        return None

    def _html_function(self, fn):
        """Text of the leaf HTML elements built by string literals of one function."""
        c = Ctx(label="fn:" + fn.name)
        for node in self._literal_nodes(fn.body[_docstring_skip(fn.body):]):
            self._inner_units(node, "html", c)

    @staticmethod
    def _literal_nodes(stmts):
        """String literal nodes (Constant / JoinedStr groups) in source order, skipping the
        Constant parts of f-strings, dict keys and docstrings of nested functions."""
        out = []

        def visit(n):
            if isinstance(n, ast.JoinedStr):
                out.append(n)
                for v in n.values:
                    if isinstance(v, ast.FormattedValue):
                        visit(v.value)
                return
            if _is_str_const(n):
                out.append(n)
                return
            if isinstance(n, ast.Dict):
                for v in n.values:
                    visit(v)
                return
            if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                for st in n.body[_docstring_skip(n.body):]:
                    visit(st)
                return
            for ch in ast.iter_child_nodes(n):
                visit(ch)

        for st in stmts:
            visit(st)
        return out

    # ---------------------------------------------------------------- inner units
    def _decode_carrier(self, node, start, end, fspans):
        if self._strtoks is None:
            return None, None
        i = bisect.bisect_left(self._strtoks, (start, -1))
        toks = []
        while i < len(self._strtoks) and self._strtoks[i][0] < end:
            a, b = self._strtoks[i]
            if b <= end and not any(fa <= a < fb for fa, fb in fspans):
                toks.append((a, b))
            i += 1
        atoms, ctxs = [], []
        for ti, (a, b) in enumerate(toks):
            tf = [(fa, fb, k) for k, (fa, fb) in enumerate(fspans) if a <= fa and fb <= b]
            got, c = _decode_py_token(self.S.text, a, b, tf)
            if got is None:
                return None, None
            atoms.extend((v, x, y, ti) for v, x, y in got)
            ctxs.append(c)
        want = node.value if _is_str_const(node) else "".join(v.value for v in node.values if _is_str_const(v))
        if "".join(v for v, *_ in atoms if isinstance(v, str)) != want:
            return None, None
        if [v for v, *_ in atoms if isinstance(v, int)] != list(range(len(fspans))):
            return None, None
        return atoms, ctxs

    def _inner_units(self, node, mode, ctx):
        """Units for the text of SVG elements (mode svg) or leaf HTML elements (mode html)
        inside one literal node."""
        S = self.S
        start, end = S.span(node)
        if (start, end) in self._seen:
            return
        fvs = [v for v in node.values if isinstance(v, ast.FormattedValue)] if isinstance(node, ast.JoinedStr) else []
        fspans = [S.span(v) for v in fvs]
        if any(S.text[a:a + 1] != "{" or S.text[b - 1:b] != "}" for a, b in fspans):
            self.skipped.append((node.lineno, mode, "f-string field position not recoverable", ""))
            return
        fields = [PH(None, "field", a + 1, b - 1, S.text[a + 1:b - 1], False) for a, b in fspans]
        atoms, ctxs = self._decode_carrier(node, start, end, fspans)
        exact_ok = atoms is not None
        if not exact_ok:
            atoms, k = [], 0
            for v in (node.values if isinstance(node, ast.JoinedStr) else [node]):
                if _is_str_const(v):
                    atoms.extend((ch, None, None, None) for ch in v.value)
                elif isinstance(v, ast.FormattedValue):
                    atoms.append((k, None, None, None))
                    k += 1
        mstr = "".join(a[0] if isinstance(a[0], str) else FIELD for a in atoms)
        spans = svg_elements(mstr) if mode == "svg" else html_leaf_elements(mstr)
        if not spans:
            return
        multiline = node.lineno != node.end_lineno
        wrap = multiline and self._offs is not None and self._depth(start) > 0 and not ctx.in_field
        indent = ""
        for ln in range(node.lineno + 1, node.end_lineno + 1) if wrap else ():
            lt = S.line(ln)
            ws = lt[:len(lt) - len(lt.lstrip())]
            o = S.starts[ln - 1] + len(ws)
            if lt.strip() and start < o < end and not any(a <= o < b for a, b in fspans):
                indent = ws
                break
        segs = []
        for a in atoms:
            if isinstance(a[0], str):
                if segs and segs[-1][0] == "t":
                    segs[-1][1] += a[0]
                else:
                    segs.append(["t", a[0]])
            else:
                segs.append(["f", a[0]])
        carrier = Carrier(cid="", start=start, end=end, col0=S.col(start), indent=indent, wrap=wrap,
                          segs=segs, fields=fields, exact_ok=exact_ok)
        tmpl = self._templates().get((start, end))       # literal used as "..." % x or "...".format(x)
        made = []
        for cs, ce, elem in spans:
            if cs >= ce:
                continue
            parts, phs, ecount, elabels = [], [], 0, []
            bad = False
            for a in atoms[cs:ce]:
                v = a[0]
                if isinstance(v, str):
                    if v in (LB, RB):
                        bad = True
                    parts.append(v)
                    continue
                fv = fvs[v]
                rid = _cite_rid(fv.value) if fv.conversion == -1 and fv.format_spec is None else None
                if rid:
                    tok = "%sc:%s%s" % (LB, rid, RB)
                else:
                    ecount += 1
                    tok = "%se%d%s" % (LB, ecount, RB)
                    elabels.append(" E%d=%s" % (ecount, _short(fields[v].src)))
                f = fields[v]
                phs.append(PH(tok, "field", f.start, f.end, f.src, False))
                parts.append(tok)
            raw = "".join(parts)
            if bad:
                self.skipped.append((node.lineno, mode, "element text contains %s or %s" % (LB, RB), _preview(raw)))
                continue
            encoded = _enc(raw)
            stripped = encoded.strip()
            if not label_ok(stripped):
                code_only = bool(PH_RE.search(stripped)) and not _words(stripped)
                self.stats["code-only" if code_only else "no-words"] += 1
                if code_only:
                    self.stats_fieldonly.append((node.lineno, _preview(raw, 50)))
                continue
            lead = encoded[:len(encoded) - len(encoded.lstrip())]
            trail = encoded[len(encoded.rstrip()):]
            exact = None
            if exact_ok and len({a[3] for a in atoms[cs:ce]}) == 1:
                exact = dict(ctxs[atoms[cs][3]], start=atoms[cs][1], end=atoms[ce - 1][2])
            ustart = atoms[cs][1] if exact_ok else start
            uend = atoms[ce - 1][2] if exact_ok else end
            if mode == "svg":
                kind = "svglabel"
                base = ctx.base()
            else:
                kind = "text" if len(_words(stripped)) >= 4 else "label"
                base = ctx.base() + " html=" + elem
            pct = 0
            if tmpl == "%":
                pct, stray = _count_pct(raw)
                if stray:
                    self.skipped.append((node.lineno, mode, "%-template text with a stray %", _preview(raw)))
                    continue
                base += " %-format"
            elif tmpl == "{}":
                pct = len(re.findall(r"\{[^{}]*\}", raw))
                base += " {}-format"
            made.append(Slot(kind=kind, ctx=base + "".join(elabels), start=ustart, end=uend,
                             line=S.lineno(ustart), text=stripped, lead=lead, trail=trail, phs=phs, mod=None,
                             pct=pct, wrap=False, col0=0, expr="inner", vstart=cs, vend=ce, exact=exact,
                             elem=elem))
        if not made:
            return
        if not self._carrier_roundtrip(node, carrier, made):
            self.skipped.append((node.lineno, mode, "literal does not round-trip after re-emission",
                                 _preview(made[0].text)))
            return
        carrier.cid = "C%04d" % (len(self.carriers) + 1)
        self.carriers.append(carrier)
        self._seen.add((start, end))
        for u in made:
            u.carrier = carrier.cid
            self.slots.append(u)

    def _templates(self):
        """Spans of string literals used as a %-template or as the receiver of .format()."""
        if not hasattr(self, "_tmpl"):
            self._tmpl = {}
            for n in ast.walk(self.tree):
                if isinstance(n, ast.BinOp) and isinstance(n.op, ast.Mod) and _is_str_const(n.left):
                    self._tmpl[self.S.span(n.left)] = "%"
                elif (isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) and n.func.attr == "format"
                      and _is_str_const(n.func.value)):
                    self._tmpl[self.S.span(n.func.value)] = "{}"
        return self._tmpl

    def _carrier_roundtrip(self, node, c, units):
        """Exact patches and whole-literal re-emission must both reproduce the literal."""
        S = self.S
        want = _parts_signature(*parts_of(node, S))
        fsrc = [f.src for f in c.fields]
        fmap = {f.start: i for i, f in enumerate(c.fields)}

        def same(code):
            wrapped = "(\n" + code + "\n)"
            try:
                n2 = ast.parse(wrapped, mode="eval").body
                return _parts_signature(*parts_of(n2, Source(wrapped))) == want
            except (SyntaxError, Unsupported):
                return False

        for u in units:
            if u.exact:
                code = emit_inner_exact(u, u.text, [fsrc[fmap[ph.start]] for ph in u.phs])
                if code is None or not same(S.text[c.start:u.exact["start"]] + code + S.text[u.exact["end"]:c.end]):
                    u.exact = None
        return same(emit_carrier(c, [(u, u.text) for u in units], fsrc, "\n"))

    # ---------------------------------------------------------------- slots
    def _literal_preview(self, node):
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Mod):
            return node.left.value
        out = []
        for op in _flatten_add(node):
            if _is_str_const(op):
                out.append(op.value)
            elif isinstance(op, ast.JoinedStr):
                out.extend(v.value if _is_str_const(v) else " " for v in op.values)
            else:
                out.append(" ")
        return "".join(out)

    def walk_subnodes(self, node, ctx):
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Mod) and _is_str_const(node.left):
            self.walk(node.right, ctx)
            return
        for op in _flatten_add(node):
            if _is_str_const(op):
                continue
            if isinstance(op, ast.JoinedStr):
                for v in op.values:
                    if isinstance(v, ast.FormattedValue):
                        self.walk(v.value, ctx.w(in_field=True))
            else:
                self.walk(op, ctx)

    def misc(self, node, ctx):
        lit = self._literal_preview(node)
        if ctx.excluded:
            if _prose_like(lit):
                self.uncaptured.append((node.lineno, ctx.excluded, _preview(_strip_markup(lit))))
            self.walk_subnodes(node, ctx)
            return
        reason = misc_reject(lit)
        if reason is None:
            self.make_slot(node, "misc", ctx)
            return
        if reason in ("svg", "markup", "multiline") and _prose_like(lit):
            self.uncaptured.append((node.lineno, reason + " string", _preview(_strip_markup(lit))))
        elif reason == "short" and ctx.gen and _words(lit):
            self.gen_skipped.append((node.lineno, ctx.callee, _preview(lit, 50)))
        elif (reason == "short" and ctx.callee and ctx.callee not in QUIET_CALLEES
              and ctx.callee not in HELPERS and ctx.callee not in self.wrappers
              and _words(lit) and not _slug_like(lit)):
            self.short_labels.append((node.lineno, ctx.callee, _preview(lit, 50)))
        self.walk_subnodes(node, ctx)

    def make_slot(self, node, kind, ctx, extra="", allow_excluded=False):
        if ctx.excluded and not allow_excluded:
            self.misc(node, ctx)
            return
        S = self.S
        start, end = S.span(node)
        if (start, end) in self._seen:
            return
        self._seen.add((start, end))
        base = ctx.base() + extra
        if kind in ("misc", "label", "svglabel") and ctx.callee and not extra:
            base += " in=" + ctx.callee
        try:
            slot = self._build(node, kind, base, ctx, start, end)
        except Unsupported as e:
            self.skipped.append((node.lineno, kind, str(e), _preview(self._literal_preview(node))))
            slot = None
        if slot is not None:
            self.slots.append(slot)
        self.walk_subnodes(node, ctx)

    def _build(self, node, kind, base, ctx, start, end):
        S = self.S
        parts, mod = parts_of(node, S)
        texts, phs, ecount, elabels = [], [], 0, []
        for p in parts:
            if p[0] == "lit":
                if LB in p[1] or RB in p[1]:
                    raise Unsupported("literal text contains %s or %s" % (LB, RB))
                texts.append(p[1])
                continue
            ph, n = p[1], p[2]
            rid = None
            if ph.ptype == "op":
                rid = _cite_rid(n)
            elif n.conversion == -1 and n.format_spec is None:
                rid = _cite_rid(n.value)
            if rid:
                ph.tok = "%sc:%s%s" % (LB, rid, RB)
            else:
                ecount += 1
                ph.tok = "%se%d%s" % (LB, ecount, RB)
                elabels.append(" E%d=%s" % (ecount, _short(ph.src)))
            phs.append(ph)
            texts.append(ph.tok)
        encoded = _enc("".join(texts))
        stripped = encoded.strip()
        if not stripped:
            return None
        lead = encoded[:len(encoded) - len(encoded.lstrip())]
        trail = encoded[len(encoded.rstrip()):]
        pct = 0
        if mod is not None:
            pct, bad = _count_pct(_dec(stripped))
            if bad:
                raise Unsupported("%-template with a stray %")
            mod.tok = LB + "mod" + RB          # kept in meta only, never shown in the text
            base += " %-format"
        expr = "mod" if mod else ("fstr" if any(p.ptype == "field" for p in phs) else
                                  ("concat" if phs or isinstance(node, ast.BinOp) else "str"))
        multiline = node.lineno != node.end_lineno
        wrap = multiline and self._offs is not None and self._depth(start) > 0 and not ctx.in_field
        holes = [(ph.start, ph.end) for ph in phs + ([mod] if mod else [])]
        indent = ""
        for ln in range(node.lineno + 1, node.end_lineno + 1) if wrap else ():
            lt = S.line(ln)
            ws = lt[:len(lt) - len(lt.lstrip())]
            o = S.starts[ln - 1] + len(ws)
            if lt.strip() and start < o < end and not any(a <= o < b for a, b in holes):
                indent = ws
                break
        slot = Slot(kind=kind, ctx=base + "".join(elabels), start=start, end=end, line=node.lineno,
                    text=stripped, lead=lead, trail=trail, phs=phs, mod=mod, pct=pct, wrap=wrap,
                    col0=S.col(start), expr=expr, indent=indent)
        slot.has_comment = any(start <= c < end and not any(a <= c < b for a, b in holes)
                               for c in self._comments)
        self._roundtrip(slot, parts, mod)
        return slot

    @staticmethod
    def _roundtrip(slot, parts, mod):
        """Re-emit the unchanged text, re-parse it, and demand identical parts."""
        code = emit_code(slot, slot.text, [p.src for p in slot.phs], mod.src if mod else None, "\n")
        wrapped = "(\n" + code + "\n)"
        try:
            node = ast.parse(wrapped, mode="eval").body
        except SyntaxError as e:
            raise Unsupported("re-emitted code does not parse (%s)" % e.msg)
        parts2, mod2 = parts_of(node, Source(wrapped))
        if _parts_signature(parts, mod) != _parts_signature(parts2, mod2):
            raise Unsupported("re-emitted code does not round-trip")

    def _finish_deferred(self):
        for name, value in self.deferred.items():
            use = self.deferred_uses.get(name)
            if use:
                self.make_slot(value, use[0], use[1].w(in_field=False, callee=None), extra=" v=" + name)
            else:
                self.walk(value, Ctx(var=name))

    def _number(self):
        self.slots.sort(key=lambda s: (s.start, -s.end, s.vstart))
        for i, s in enumerate(self.slots, 1):
            s.uid = "U%04d" % i
        nodes = [s for s in self.slots if s.expr != "inner"] + self.carriers
        nodes.sort(key=lambda n: (n.start, -n.end))
        stack = []
        for n in nodes:
            while stack and n.start >= stack[-1].end:
                stack.pop()
            if stack:
                p = stack[-1]
                holes = p.fields if isinstance(p, Carrier) else p.all_phs()
                if n.end > p.end or not any(h.start <= n.start and n.end <= h.end for h in holes):
                    raise RuntimeError("%s: unit at line %d overlaps another unit" % (self.module, self.S.lineno(n.start)))
                if isinstance(n, Slot):
                    n.parent = p.uid if isinstance(p, Slot) else p.cid
            stack.append(n)


# ============================================================================ extractor (svg-text)
class SvgExtractor(Extractor):
    """--svg-text units of a Python module: element text in literals, literal arguments of
    text-drawing helpers, and literal items of for-loops that draw text."""
    _helper_cache = {}

    def __init__(self, module, text):
        super().__init__(module, text, profile="svg")
        self.helpers = {}

    def walk_subnodes(self, node, ctx):
        """Sub-expressions of a slot are walked with the svg rules, never the prose rules."""
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Mod) and _is_str_const(node.left):
            self._svg_walk(node.right, ctx, None)
            return
        for op in _flatten_add(node):
            if _is_str_const(op):
                continue
            if isinstance(op, ast.JoinedStr):
                for v in op.values:
                    if isinstance(v, ast.FormattedValue):
                        self._svg_walk(v.value, ctx.w(in_field=True), None)
            else:
                self._svg_walk(op, ctx, None)

    def run(self):
        self._imports()
        self._infer_helpers()
        self._svg_walk(self.tree, Ctx(label="svg=top"), None)
        self._number()
        return self

    # ---------------------------------------------------------------- helper inference
    @staticmethod
    def _funcs(tree):
        funcs = {}
        for n in ast.walk(tree):
            if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)):
                funcs[n.name] = ([a.arg for a in n.args.posonlyargs + n.args.args + n.args.kwonlyargs], n)
            elif (isinstance(n, ast.Assign) and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name)
                  and isinstance(n.value, ast.Lambda)):
                a = n.value.args
                funcs[n.targets[0].id] = ([x.arg for x in a.posonlyargs + a.args + a.kwonlyargs], n.value)
        return funcs

    @staticmethod
    def _content_fields(node):
        """Names used as f-string fields inside the content of SVG text elements."""
        names = set()
        for js in ast.walk(node):
            if not isinstance(js, ast.JoinedStr):
                continue
            fvs = [v for v in js.values if isinstance(v, ast.FormattedValue)]
            mstr, k = [], 0
            for v in js.values:
                if _is_str_const(v):
                    mstr.append(v.value)
                elif isinstance(v, ast.FormattedValue):
                    mstr.append(FIELD)
            mstr = "".join(mstr)
            idx = [i for i, ch in enumerate(mstr) if ch == FIELD]
            for cs, ce, _e in svg_elements(mstr):
                for k, pos in enumerate(idx):
                    if cs <= pos < ce and isinstance(fvs[k].value, ast.Name):
                        names.add(fvs[k].value.id)
        return names

    def _sinks(self, nodes, names, helpers):
        """(text sinks, list sinks) among `names` inside the statements / expression `nodes`."""
        wrapper = ast.Module(body=nodes if isinstance(nodes, list) else [ast.Expr(nodes)], type_ignores=[])
        text_s = self._content_fields(wrapper) & names
        list_s = set()
        draws = bool(text_s) or bool(self._content_fields(wrapper))
        for n in ast.walk(wrapper):
            if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id in helpers:
                h = helpers[n.func.id]
                draws = draws or bool(h["text"] or h["list"])
                for param, _role, arg in self._bind(n, [(p, None) for p in h["params"]]):
                    if param in h["text"] and isinstance(arg, ast.Name) and arg.id in names:
                        text_s.add(arg.id)
                    if param in h["list"]:
                        if isinstance(arg, ast.Name) and arg.id in names:
                            list_s.add(arg.id)
                        elif isinstance(arg, (ast.List, ast.Tuple)):
                            text_s |= {e.id for e in arg.elts if isinstance(e, ast.Name) and e.id in names}
        for n in ast.walk(wrapper):
            if (draws and isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) and n.func.attr == "split"
                    and not n.args and isinstance(n.func.value, ast.Name) and n.func.value.id in names):
                text_s.add(n.func.value.id)
            if isinstance(n, ast.For):
                it, tgt = n.iter, n.target
                if (isinstance(it, ast.Call) and isinstance(it.func, ast.Name) and it.func.id == "enumerate"
                        and it.args and isinstance(tgt, ast.Tuple) and len(tgt.elts) == 2):
                    it, tgt = it.args[0], tgt.elts[1]
                if isinstance(it, ast.Name) and it.id in names:
                    inner = {x.id for x in ast.walk(tgt) if isinstance(x, ast.Name)}
                    if self._sinks(n.body, inner, helpers)[0]:
                        list_s.add(it.id)
        return text_s, list_s

    def _infer_helpers(self):
        funcs = self._funcs(self.tree)
        info = {}
        for local, (mod, name) in self.name_from.items():
            if mod.startswith("figs"):
                h = self._module_helpers(mod).get(name)
                if h:
                    info[local] = h
        mine = {k: {"params": p, "text": set(), "list": set()} for k, (p, _n) in funcs.items()}
        info.update(mine)
        for _ in range(8):
            changed = False
            for k, (params, node) in funcs.items():
                body = node.body if isinstance(node.body, list) else node.body
                t, l = self._sinks(body, set(params), info)
                if t - mine[k]["text"] or l - mine[k]["list"]:
                    mine[k]["text"] |= t
                    mine[k]["list"] |= l
                    changed = True
            if not changed:
                break
        self.helpers = {k: v for k, v in info.items() if v["text"] or v["list"]}

    @classmethod
    def _module_helpers(cls, mod):
        if mod not in cls._helper_cache:
            cls._helper_cache[mod] = {}
            path = os.path.join(BUILD, mod.replace(".", os.sep) + ".py")
            try:
                text, _b, _n = decode_source(open(path, "rb").read())
                sx = SvgExtractor(mod, text)
                sx._imports()
                sx._infer_helpers()
                cls._helper_cache[mod] = sx.helpers
            except (OSError, SyntaxError):
                pass
        return cls._helper_cache[mod]

    # ---------------------------------------------------------------- walk
    def _svg_walk(self, node, ctx, fn):
        if isinstance(node, ast.Module):
            for st in node.body[_docstring_skip(node.body):]:
                self._svg_walk(st, ctx, fn)
            return
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            c = ctx.w(label="svg=" + node.name)
            for d in node.decorator_list:
                self._svg_walk(d, ctx, fn)
            for d in node.args.defaults + [x for x in node.args.kw_defaults if x is not None]:
                self._svg_walk(d, ctx, fn)
            for st in node.body[_docstring_skip(node.body):]:
                self._svg_walk(st, c, node)
            return
        if isinstance(node, ast.ClassDef):
            for st in node.body[_docstring_skip(node.body):]:
                self._svg_walk(st, ctx, fn)
            return
        if isinstance(node, ast.For):
            self._loop_units(node, ctx, fn)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in self.helpers:
            h = self.helpers[node.func.id]
            for param, _r, arg in self._bind(node, [(p, None) for p in h["params"]]):
                if param in h["text"] and is_str_expr(arg):
                    self._svg_slot(arg, ctx, "in=" + node.func.id)
                elif param in h["list"] and isinstance(arg, (ast.List, ast.Tuple)):
                    for e in arg.elts:
                        if is_str_expr(e):
                            self._svg_slot(e, ctx, "in=" + node.func.id)
                        else:
                            self._svg_walk(e, ctx, fn)
                else:
                    self._svg_walk(arg, ctx, fn)
            return
        if isinstance(node, ast.Dict):
            for v in node.values:
                self._svg_walk(v, ctx, fn)
            return
        if _is_str_const(node) or isinstance(node, ast.JoinedStr):
            self._svg_carrier(node, ctx)
            if isinstance(node, ast.JoinedStr):
                for v in node.values:
                    if isinstance(v, ast.FormattedValue):
                        self._svg_walk(v.value, ctx.w(in_field=True), fn)
            return
        for ch in ast.iter_child_nodes(node):
            self._svg_walk(ch, ctx, fn)

    def _svg_slot(self, node, ctx, extra):
        if not label_ok(self._literal_preview(node)):
            self.stats["no-words"] += 1
            return
        n0 = len(self.slots)
        self.make_slot(node, "svglabel", ctx.w(callee=None), extra=" " + extra)
        if len(self.slots) > n0:
            if extra == "in=for":
                self.loop_units += 1
            else:
                self.helper_units += 1

    def _svg_carrier(self, node, ctx):
        val = node.value if _is_str_const(node) else "".join(v.value for v in node.values if _is_str_const(v))
        if SVG_HINT_RE.search(val):
            self._inner_units(node, "svg", ctx)

    def _resolve_iter(self, it, fn, before, depth=0):
        if depth > 4:
            return []
        if isinstance(it, (ast.List, ast.Tuple)):
            return [it]
        if isinstance(it, ast.IfExp):
            return self._resolve_iter(it.body, fn, before, depth + 1) + self._resolve_iter(it.orelse, fn, before, depth + 1)
        if isinstance(it, ast.Name):
            scopes = ([fn] if fn is not None else []) + [self.tree]
            for scope in scopes:
                found = None
                for n in ast.walk(scope):
                    if (isinstance(n, ast.Assign) and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name)
                            and n.targets[0].id == it.id and n.lineno < before):
                        if scope is self.tree and n not in self.tree.body:
                            continue
                        if found is None or n.lineno > found.lineno:
                            found = n
                if found is not None:
                    return self._resolve_iter(found.value, fn, found.lineno, depth + 1)
        return []

    def _loop_units(self, node, ctx, fn):
        tgt, it = node.target, node.iter
        if (isinstance(it, ast.Call) and isinstance(it.func, ast.Name) and it.func.id == "enumerate" and it.args
                and isinstance(tgt, ast.Tuple) and len(tgt.elts) == 2):
            tgt, it = tgt.elts[1], it.args[0]
        pos = {}

        def collect(t, path):
            if isinstance(t, ast.Name):
                pos[t.id] = path
            elif isinstance(t, (ast.Tuple, ast.List)):
                for i, e in enumerate(t.elts):
                    collect(e, path + (i,))

        collect(tgt, ())
        if not pos:
            return
        sinks = self._sinks(node.body, set(pos), self.helpers)[0]
        if not sinks:
            return
        for src in self._resolve_iter(it, fn, node.lineno):
            for item in src.elts:
                for name in sorted(sinks):
                    elt = item
                    for k in pos[name]:
                        if isinstance(elt, (ast.Tuple, ast.List)) and k < len(elt.elts):
                            elt = elt.elts[k]
                        else:
                            elt = None
                            break
                    if elt is not None and is_str_expr(elt):
                        self._svg_slot(elt, ctx, "in=for")


class JsonSvgExtractor:
    """--svg-text units of a figs_*.json file (text of SVG elements in string values)."""

    def __init__(self, module, text):
        self.module, self.text = module, text
        self.slots, self.carriers, self.skipped, self.uncaptured = [], [], [], []
        self.short_labels, self.gen_skipped, self.wrapper_notes = [], [], []
        self.stats = collections.Counter()
        self.stats_fieldonly = []
        self.loop_units = self.helper_units = 0

    def run(self):
        S = Source(self.text)
        for path, _a, _b, atoms in json_strings(self.text):
            mstr = "".join(a[0] for a in atoms)
            for cs, ce, elem in svg_elements(mstr):
                if cs >= ce:
                    continue
                raw = mstr[cs:ce]
                if LB in raw or RB in raw:
                    self.skipped.append((S.lineno(atoms[cs][1]), "svglabel", "text contains %s or %s" % (LB, RB),
                                         _preview(raw)))
                    continue
                encoded = _enc(raw)
                stripped = encoded.strip()
                if not label_ok(stripped):
                    self.stats["no-words"] += 1
                    continue
                a, b = atoms[cs][1], atoms[ce - 1][2]
                self.slots.append(Slot(
                    kind="svglabel", ctx="svg=" + path, start=a, end=b, line=S.lineno(a), text=stripped,
                    lead=encoded[:len(encoded) - len(encoded.lstrip())], trail=encoded[len(encoded.rstrip()):],
                    phs=[], mod=None, pct=0, wrap=False, col0=0, expr="json",
                    exact={"start": a, "end": b, "json": True}, elem=elem))
        for i, s in enumerate(self.slots, 1):
            s.uid = "U%04d" % i
        return self


# ============================================================================ targets / files
@dataclasses.dataclass
class Target:
    name: str          # canonical: paper_cloning, ipm_blueprint.content, data.glossary, figs_lib, figs_x.json
    path: str
    profile: str       # paper | code | data | glossary | evidence | figs | json
    render: str        # paper | wrapper | upper | evidence | figs | json

    @property
    def json(self):
        return self.profile == "json"

    def modes(self):
        if self.profile in ("figs", "json"):
            return ("svg",)
        if self.profile in ("paper", "code"):
            return ("prose", "svg")
        return ("prose",)

    def unsupported(self):
        return UNSUPPORTED.get(self.name)


def resolve_target(arg):
    s = arg.strip().replace("\\", "/")
    if os.path.isabs(s) or re.match(r"[A-Za-z]:/", s):
        s = os.path.relpath(s, BUILD).replace("\\", "/")
    for pre in ("./", "_build/"):
        if s.startswith(pre):
            s = s[len(pre):]
    if s.endswith(".json"):
        name = s.rsplit("/", 1)[-1]
        path = os.path.join(BUILD, name)
        if not re.fullmatch(r"figs_[\w\-]+\.json", name) or not os.path.exists(path):
            raise SystemExit("not a figure JSON file in _build/: %s" % arg)
        return Target(name, path, "json", "json")
    if s.endswith(".py"):
        s = s[:-3]
    dotted = s.replace("/", ".")
    if dotted in BLOCKED:
        raise SystemExit("%s: %s" % (dotted, BLOCKED[dotted]))
    if re.fullmatch(r"paper_\w+", dotted):
        t = Target(dotted, "", "paper", "paper")
    elif dotted == "ipm_blueprint.content":
        t = Target(dotted, "", "data", "wrapper")
    elif dotted == "ipm_blueprint.render":
        t = Target(dotted, "", "code", "wrapper")
    elif re.fullmatch(r"data\.glossary(?:_gen\d*)?", dotted):
        t = Target(dotted, "", "glossary", "upper")
    elif dotted == "data.evidence":
        t = Target(dotted, "", "evidence", "evidence")
    elif re.fullmatch(r"figs(?:_\w+)?", dotted):
        t = Target(dotted, "", "figs", "figs")
    else:
        raise SystemExit("unsupported target: %s (paper_*, ipm_blueprint.content/render, data.glossary*, "
                         "data.evidence, figs*, figs_*.json)" % arg)
    t.path = os.path.join(BUILD, *dotted.split(".")) + ".py"
    if not os.path.exists(t.path):
        raise SystemExit("no such module: %s" % _rel(t.path))
    return t


def module_stem(arg):
    """Backwards-compatible name of a target."""
    return resolve_target(arg).name


def module_path(stem):
    return resolve_target(stem).path


def work_root(args):
    w = getattr(args, "work", None) or DEFAULT_WORK
    return w if os.path.isabs(w) else os.path.join(REPO, w)


def all_modules():
    return sorted(f[:-3] for f in os.listdir(BUILD) if f.startswith("paper_") and f.endswith(".py"))


def all_targets():
    """(target, mode) pairs covered by selftest --all."""
    out = []
    for stem in all_modules():
        t = resolve_target(stem)
        out += [(t, "prose"), (t, "svg")]
    for name in ("ipm_blueprint.content", "ipm_blueprint.render"):
        out.append((resolve_target(name), "prose"))
    for f in sorted(os.listdir(os.path.join(BUILD, "data"))):
        if re.fullmatch(r"glossary(?:_gen\d*)?\.py", f) or f == "evidence.py":
            out.append((resolve_target("data." + f[:-3]), "prose"))
    for f in sorted(os.listdir(BUILD)):
        if re.fullmatch(r"figs(?:_\w+)?\.py", f):
            out.append((resolve_target(f[:-3]), "svg"))
        elif re.fullmatch(r"figs_[\w\-]+\.json", f):
            out.append((resolve_target(f), "svg"))
    return out


def _rel(path):
    try:
        return os.path.relpath(path, REPO).replace("\\", "/")
    except ValueError:
        return path


def _module_slug(tree):
    for st in tree.body:
        if (isinstance(st, ast.Assign) and len(st.targets) == 1 and isinstance(st.targets[0], ast.Name)
                and st.targets[0].id == "SLUG" and _is_str_const(st.value)):
            return st.value.value
    return "?"


def units_header(stem, slug, slots, svg=False, source=None):
    misc = sum(s.kind == "misc" for s in slots)
    head = [
        "# %s | module: %s | slug: %s%s" % (FORMAT, stem, slug, " | mode: svg-text" if svg else ""),
        "# source: %s | units: %d | misc: %d | written by ste_units.py extract %s"
        % (source or "_build/%s.py" % stem, len(slots), misc, datetime.date.today().isoformat()),
        "# Edit ONLY the text line under each '@@' header and keep it on ONE line. Never edit '@@' lines.",
        "# %sc:id%s = citation, %se1%s = code (EN=... in the header). Keep each one (moving is fine). %s = newline."
        % (LB, RB, LB, RB, NL_TOK),
        "# Keep inline HTML (<strong>, <em>, <a href=...>, <br>) and entities (&deg;) intact. misc units are optional.",
    ]
    if svg or any(_is_diagram_label(s) for s in slots):
        head.append("# Diagram text (svglabel, label/misc with in=Mod.func): the figure has a fixed size, keep each "
                    "one within ~115% of its original length.")
    return head + [""]


def kind_counts(slots):
    c = collections.Counter(s.kind for s in slots)
    return " ".join("%s=%d" % kv for kv in sorted(c.items(), key=lambda kv: (-kv[1], kv[0])))


def analyze_target(t, text, svg=False):
    if t.json:
        return JsonSvgExtractor(t.name, text).run()
    if svg:
        return SvgExtractor(t.name, text).run()
    profile = {"paper": "paper", "code": "paper", "data": "data", "glossary": "glossary",
               "evidence": "evidence"}[t.profile]
    return Extractor(t.name, text, profile).run()


def analyze(stem, text):
    """Backwards-compatible: prose units of a paper module."""
    return Extractor(stem, text).run()


# ============================================================================ subprocess runner
RUNNER = r'''
import sys, os, json, hashlib, types, importlib, inspect, re
spec = json.load(open(sys.argv[1], encoding="utf-8"))
sys.path.insert(0, spec["build"])

def _default(o):
    if isinstance(o, (set, frozenset)):
        return sorted(repr(x) for x in o)
    if callable(o) or isinstance(o, types.ModuleType):
        return "<%s %s>" % (type(o).__name__, getattr(o, "__qualname__", getattr(o, "__name__", "")))
    return repr(o)

def inject(name, src, real):
    parent = name.rpartition(".")[0]
    if parent:
        importlib.import_module(parent)
    with open(src, encoding="utf-8-sig") as fh:
        code = fh.read()
    m = types.ModuleType(name)
    m.__file__ = real
    if parent:
        m.__package__ = parent
    sys.modules[name] = m
    exec(compile(code, real, "exec"), m.__dict__)
    if parent:
        setattr(sys.modules[parent], name.rpartition(".")[2], m)

def upper(m):
    return {k: v for k, v in vars(m).items() if re.fullmatch(r"[A-Z][A-Z0-9_]*", k)}

def dump(m, how):
    if how == "paper":
        data = {k: getattr(m, k) for k in ("TITLE", "EYEBROW", "SUB", "META", "SECTIONS")}
        for k in ("RELATED", "REF_IDS", "SLUG"):
            if hasattr(m, k):
                data[k] = getattr(m, k)
        return json.dumps(data, ensure_ascii=False, default=_default)
    if how == "upper":
        return json.dumps(upper(m), ensure_ascii=False, sort_keys=True, default=_default)
    if how == "evidence":
        slugs = sorted(m.PAPERS) + ["slab-irrigation-strategy", "zz-no-such-paper"]
        data = {"upper": upper(m), "panel": {s: m.panel_html(s) for s in slugs},
                "note": m.community_note("probe body", "Probe")}
        return json.dumps(data, ensure_ascii=False, sort_keys=True, default=_default)
    if how == "figs":
        out = {}
        for k, f in sorted(vars(m).items()):
            if k.startswith("_") or not inspect.isfunction(f) or f.__module__ != m.__name__:
                continue
            ps = inspect.signature(f).parameters.values()
            if any(p.default is p.empty and p.kind in (p.POSITIONAL_ONLY, p.POSITIONAL_OR_KEYWORD, p.KEYWORD_ONLY)
                   for p in ps):
                continue
            out[k] = f()
        return json.dumps({"funcs": out, "upper": upper(m)}, ensure_ascii=False, sort_keys=True, default=_default)
    raise ValueError(how)

res = {}
try:
    for inj in spec.get("inject", []):
        inject(inj["name"], inj["src"], inj["real"])
except BaseException as e:
    print(json.dumps({"__inject__": "ERROR %s: %s" % (type(e).__name__, str(e)[:300])}))
    sys.exit(0)
for t in spec["targets"]:
    key = t["name"] + ":" + t["dump"]
    try:
        m = sys.modules.get(t["name"]) or importlib.import_module(t["name"])
        blob = dump(m, t["dump"])
        if t.get("out"):
            with open(t["out"], "w", encoding="utf-8") as fh:
                fh.write(blob)
        res[key] = hashlib.sha256(blob.encode("utf-8")).hexdigest()
    except BaseException as e:
        res[key] = "ERROR %s: %s" % (type(e).__name__, str(e)[:300])
print(json.dumps(res))
'''


def _env():
    env = dict(os.environ)
    env.update(PYTHONHASHSEED="0", PYTHONIOENCODING="utf-8", PYTHONDONTWRITEBYTECODE="1")
    return env


def run_runner(targets, inject=(), timeout=900):
    """targets: [(module name, dump kind, out path or None)]; inject: [(module name, source file)].
    -> {"name:dump": sha | "ERROR ..."}"""
    spec = {"build": BUILD,
            "inject": [{"name": n, "src": src, "real": os.path.join(BUILD, *n.split(".")) + ".py"}
                       for n, src in inject],
            "targets": [{"name": n, "dump": d, "out": o} for n, d, o in targets]}
    fd, path = tempfile.mkstemp(prefix="ste_spec_", suffix=".json")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            json.dump(spec, fh)
        r = subprocess.run([PY, "-B", "-c", RUNNER, path], cwd=REPO, env=_env(), capture_output=True,
                           text=True, encoding="utf-8", timeout=timeout)
    finally:
        os.remove(path)
    if r.returncode != 0:
        msg = (r.stderr.strip().splitlines() or ["exit %d" % r.returncode])[-1]
        return {"%s:%s" % (n, d): "ERROR " + msg for n, d, _o in targets}
    res = json.loads(r.stdout.strip().splitlines()[-1])
    if "__inject__" in res:
        return {"%s:%s" % (n, d): res["__inject__"] for n, d, _o in targets}
    return res


def render(stem, src_path, out_path="-"):
    """Backwards-compatible: sha of a paper module rendered from src_path. -> (sha, error)"""
    real = os.path.join(BUILD, stem + ".py")
    inject = [] if os.path.abspath(src_path) == os.path.abspath(real) else [(stem, src_path)]
    res = run_runner([(stem, "paper", None if out_path == "-" else out_path)], inject)
    v = res.get(stem + ":paper", "ERROR no result")
    return (None, v[6:]) if v.startswith("ERROR") else (v, None)


def _render_targets(t):
    """What to render to prove a target loads / renders: [(module, dump)]."""
    if t.render == "paper":
        return [(t.name, "paper")]
    if t.render == "wrapper":
        return [(IPM_WRAPPER, "paper")]
    if t.render in ("upper", "evidence"):
        return [(t.name, t.render)]
    if t.render == "figs":
        return [(t.name, "figs")] + [(p, "paper") for p in all_modules()]
    if t.render == "json":
        return [(p, "paper") for p in all_modules() if t.name in open(os.path.join(BUILD, p + ".py"), encoding="utf-8").read()]
    return []


def import_check(t):
    """Load the (already written) target and whatever renders it; None or an error message."""
    if isinstance(t, str):
        t = resolve_target(t)
    res = run_runner([(n, d, None) for n, d in _render_targets(t)])
    errs = ["%s: %s" % (k, v) for k, v in sorted(res.items()) if v.startswith("ERROR")]
    return "; ".join(errs)[:500] or None


def _first_difference(a_path, b_path):
    try:
        a = json.load(open(a_path, encoding="utf-8"))
        b = json.load(open(b_path, encoding="utf-8"))
    except (OSError, ValueError) as e:
        return "cannot compare: %s" % e

    def walk(x, y, path):
        if type(x) is not type(y):
            return path, repr(x)[:120], repr(y)[:120]
        if isinstance(x, dict):
            for k in sorted(set(x) | set(y), key=str):
                if x.get(k) != y.get(k):
                    return walk(x.get(k), y.get(k), path + "/" + str(k))
        elif isinstance(x, list):
            for i, (p, q) in enumerate(zip(x, y)):
                if p != q:
                    return walk(p, q, path + "/%d" % i)
            if len(x) != len(y):
                return path, "len %d" % len(x), "len %d" % len(y)
        elif x != y:
            i = next((i for i, (p, q) in enumerate(zip(x, y)) if p != q), min(len(x), len(y)))
            return path, repr(x[max(0, i - 40):i + 60]), repr(y[max(0, i - 40):i + 60])
        return None

    d = walk(a, b, "")
    return "no difference found" if d is None else "%s: original %s | patched %s" % d


# ============================================================================ validation
def _multiline_units(path):
    bad, cur, n = set(), None, 0
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.rstrip("\n")
            m = UNIT_HEADER.match(line)
            if m:
                cur, n = m.group("id"), 0
            elif cur and line.strip():
                n += 1
                if n > 1:
                    bad.add(cur)
    return bad


def validate(slots, units, multiline):
    """-> (errors, warnings, {uid: new text})"""
    errors, warnings, new = [], [], {}
    by_id, meta_ids = {}, {s.uid for s in slots}
    for u in units:
        if u.id in by_id:
            errors.append("%s: duplicate unit id in units file" % u.id)
            continue
        by_id[u.id] = u
        if u.id not in meta_ids:
            errors.append("%s: unknown unit id (not in meta.json)" % u.id)
    for s in slots:
        u = by_id.get(s.uid)
        if u is None:
            errors.append("%s: missing from units file" % s.uid)
            continue
        e0 = len(errors)
        if u.kind != s.kind or u.ctx != s.ctx:
            errors.append("%s: '@@' header was edited; it must stay '%s | %s'" % (s.uid, s.kind, s.ctx))
        if s.uid in multiline:
            errors.append("%s: text spans several lines; keep it on one line (newline = %s)" % (s.uid, NL_TOK))
        t = u.text
        if not t:
            errors.append("%s: text is empty" % s.uid)
        if t.count(LB) != t.count(RB) or len(ANY_TOK_RE.findall(t)) != t.count(LB):
            errors.append("%s: broken placeholder bracket %s...%s" % (s.uid, LB, RB))
        unknown = [x for x in ANY_TOK_RE.findall(t) if x not in (NL_TOK, CR_TOK) and not PH_RE.fullmatch(x)]
        if unknown:
            errors.append("%s: unknown placeholder %s" % (s.uid, " ".join(unknown)))
        have = collections.Counter(PH_RE.findall(t))
        want = collections.Counter(ph.tok for ph in s.phs)
        if have != want:
            errors.append("%s: placeholders changed (%s); each original placeholder must appear exactly "
                          "as often as before" % (s.uid, _counter_diff(want, have)))
        if s.mod is not None or (s.expr == "inner" and " %-format" in s.ctx):
            n, bad = _count_pct(_dec(t))
            if n != s.pct or bad:
                errors.append("%s: %%-template needs exactly %d %%-specifier(s) and no bare %% "
                              "(found %d, %d stray; write %%%% for a literal %%)" % (s.uid, s.pct, n, bad))
        elif s.expr == "inner" and " {}-format" in s.ctx:
            n = len(re.findall(r"\{[^{}]*\}", t))
            if n != s.pct or t.count("{") != t.count("}"):
                errors.append("%s: .format() template needs exactly %d {...} field(s) and no single brace "
                              "(found %d)" % (s.uid, s.pct, n))
        r0, r1 = tag_residue(s.text, s.kind), tag_residue(t, s.kind)
        if r0 != r1:
            errors.append("%s: HTML tags unbalanced: %s" % (s.uid, "; ".join(r1) or "differs from original"))
        if len(errors) > e0:
            continue
        if t != s.text:
            new[s.uid] = t
            if t.count(NL_TOK) != s.text.count(NL_TOK):
                warnings.append("%s: warning: %s count changed" % (s.uid, NL_TOK))
            if _tag_counts(s.text) != _tag_counts(t):
                warnings.append("%s: warning: inline tags changed: %s"
                                % (s.uid, _counter_diff(_tag_counts(s.text), _tag_counts(t))))
            if _numbers(s.text) != _numbers(t):
                warnings.append("%s: warning: numbers changed: %s"
                                % (s.uid, _counter_diff(_numbers(s.text), _numbers(t))))
            if _is_diagram_label(s):
                a, b = _vis_len(s.text), _vis_len(t)
                if a and b > LABEL_GROWTH * a:
                    warnings.append("%s: warning: diagram label is %d%% of its original length (%d -> %d chars); "
                                    "the figure has a fixed size" % (s.uid, round(100.0 * b / a), a, b))
    return errors, warnings, new


# ============================================================================ work dir state
class Work:
    def __init__(self, args, target, svg=False):
        if isinstance(target, str):
            target = resolve_target(target)
        self.target = target
        self.stem = target.name
        self.svg = svg
        base = os.path.join(work_root(args), target.name)
        self.dir = os.path.join(base, "svg") if svg else base
        ext = ".json" if target.json else ".py"
        self.units = os.path.join(self.dir, "units.txt")
        self.meta = os.path.join(self.dir, "meta.json")
        self.original = os.path.join(self.dir, "original" + ext)
        self.last = os.path.join(self.dir, "last_applied" + ext)
        self.applied = os.path.join(self.dir, "applied.json")
        self.other_applied = os.path.join(base, "applied.json") if svg else os.path.join(base, "svg", "applied.json")

    def applied_sha(self, path=None):
        """Newline-insensitive sha of the target as last written by apply."""
        try:
            return json.load(open(path or self.applied, encoding="utf-8"))["sha256_norm"]
        except (OSError, ValueError, KeyError):
            return None

    def known(self):
        """Newline-insensitive shas the target may have without being 'changed outside'."""
        return {_nsha(open(self.original, "rb").read()), self.applied_sha()} - {None}

    def load(self):
        if not (os.path.exists(self.meta) and os.path.exists(self.original)):
            raise SystemExit("%s: no meta.json/original snapshot in %s; run extract%s first"
                             % (self.stem, _rel(self.dir), " --svg-text" if self.svg else ""))
        meta = json.load(open(self.meta, encoding="utf-8"))
        raw = open(self.original, "rb").read()
        if _sha(raw) != meta["sha256_original"]:
            raise SystemExit("%s: original snapshot does not match meta.json; re-run extract --force" % self.stem)
        text, _bom, _nl = decode_source(raw)
        carriers = [Carrier.from_meta(c) for c in meta.get("carriers", [])]
        return meta, text, [Slot.from_meta(u) for u in meta["units"]], carriers


def _mode_check(t, svg):
    mode = "svg" if svg else "prose"
    if t.unsupported():
        return "%s: unsupported (%s)" % (t.name, t.unsupported())
    if mode not in t.modes():
        return "%s: %s mode is not available for this target (use %s)" % (
            t.name, mode, "--svg-text" if mode == "prose" else "prose mode")
    return None


# ============================================================================ commands
def cmd_extract(args):
    t = resolve_target(args.module)
    svg = bool(getattr(args, "svg_text", False))
    msg = _mode_check(t, svg)
    if msg:
        print(msg)
        return 3
    w = Work(args, t, svg)
    os.makedirs(w.dir, exist_ok=True)
    cur_raw = open(t.path, "rb").read()
    if args.force or not os.path.exists(w.original):
        shutil.copyfile(t.path, w.original)
        if os.path.exists(w.applied):
            os.remove(w.applied)
    raw = open(w.original, "rb").read()
    if _nsha(cur_raw) not in w.known():
        print("warning: %s differs from the snapshot and from the last apply; units come from the snapshot "
              "(extract --force re-snapshots the current file)" % _rel(t.path))
    text, bom, nl = decode_source(raw)
    ex = analyze_target(t, text, svg)
    if os.path.exists(w.units) and not args.force:
        try:
            _h, old = read_units(w.units)
        except (OSError, UnicodeDecodeError):
            old = None
        fresh = {s.uid: s.text for s in ex.slots}
        if old is None or {u.id for u in old} != set(fresh) or any(u.text != fresh[u.id] for u in old):
            print("%s: units.txt already holds edits (or differs); not overwritten. Use --force to "
                  "discard them." % _rel(w.units))
            return 2
    slug = "?" if t.json else _module_slug(ex.tree)
    meta = {"format": FORMAT, "module": t.name, "target": t.name, "profile": t.profile,
            "mode": "svg-text" if svg else "prose", "source": _rel(t.path), "slug": slug,
            "newline": nl, "bom": bom, "sha256_original": _sha(raw),
            "extracted": datetime.datetime.now().isoformat(timespec="seconds"),
            "carriers": [c.to_meta() for c in ex.carriers],
            "units": [s.to_meta() for s in ex.slots]}
    with open(w.meta, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(meta, fh, ensure_ascii=False, indent=1)
    write_units(w.units, units_header(t.name, slug, ex.slots, svg, _rel(t.path)),
                [Unit(s.uid, s.kind, s.ctx, s.text) for s in ex.slots])
    print_extract_summary(t.name, ex, _rel(w.units), svg)
    return 0


def print_extract_summary(stem, ex, where, svg=False):
    misc = sum(s.kind == "misc" for s in ex.slots)
    print("%s: %d units%s -> %s" % (stem, len(ex.slots), " (svg-text)" if svg else "", where))
    print("  by kind: %s" % (kind_counts(ex.slots) or "-"))
    if svg:
        inner = sum(s.expr in ("inner", "json") for s in ex.slots)
        print("  element text: %d, helper arguments: %d, loop items: %d; skipped element texts without words: %d, "
              "code-only: %d" % (inner, ex.helper_units, ex.loop_units, ex.stats["no-words"], ex.stats["code-only"]))
    else:
        labels = sum(s.kind == "label" and " in=" in s.ctx for s in ex.slots)
        print("  misc units: %d; figure labels (rule f): %d; figure strings not taken (numbers/units/style): %d"
              % (misc, labels, len(ex.gen_skipped)))
    if ex.wrapper_notes:
        print("  local helper wrappers: %s" % "; ".join(ex.wrapper_notes))
    print("  skipped as unsupported: %d" % len(ex.skipped))
    for line, kind, reason, prev in ex.skipped:
        print("    line %d %s: %s | %s" % (line, kind, reason, prev))
    if ex.uncaptured:
        print("  uncaptured prose-like strings (SVG/markup/excluded functions): %d (see extract_report.txt)"
              % len(ex.uncaptured))
    comments = [s for s in ex.slots if s.has_comment]
    if comments:
        print("  units with a comment inside the span (dropped if the unit is edited): %s"
              % " ".join(s.uid for s in comments))


def _patched_text(t, text, slots, carriers, new, nl, force=False):
    if t.json:
        return patch_json(text, slots, new, force=force)
    return patch_source(text, slots, new, nl, force=force, carriers=carriers)


def _syntax_check(t, text, path):
    try:
        if t.json:
            json.loads(text)
        else:
            compile(text, path, "exec")
    except SyntaxError as e:
        return "%s (line %s)" % (e.msg, e.lineno)
    except ValueError as e:
        return str(e)
    return None


def cmd_apply(args):
    t = resolve_target(args.module)
    svg = bool(getattr(args, "svg_text", False))
    msg = _mode_check(t, svg)
    if msg:
        print(msg, file=sys.stderr)
        return 3
    w = Work(args, t, svg)
    meta, text, slots, carriers = w.load()
    if not os.path.exists(w.units):
        raise SystemExit("%s: no units.txt" % _rel(w.units))
    _header, units = read_units(w.units)
    errors, warnings, new = validate(slots, units, _multiline_units(w.units))
    for m in warnings:
        print(m)
    if errors:
        for m in errors:
            print(m, file=sys.stderr)
        print("%s: %d error(s), %d warning(s); nothing written" % (t.name, len(errors), len(warnings)),
              file=sys.stderr)
        return 2
    nl = meta["newline"]
    new_text = _patched_text(t, text, slots, carriers, new, nl)
    err = _syntax_check(t, new_text, t.path)
    if err:
        print("%s: patched source does not parse: %s; nothing written" % (t.name, err), file=sys.stderr)
        return 1
    cur_raw = open(t.path, "rb").read() if os.path.exists(t.path) else b""
    new_raw = encode_source(_same_newlines(new_text, cur_raw), meta["bom"])   # keep LF/CRLF as found
    if _nsha(cur_raw) not in w.known() and not args.force:
        why = ""
        if w.applied_sha(w.other_applied) == _nsha(cur_raw):
            why = (" (it was last written by %s apply; applying this mode now would discard those edits)"
                   % ("prose" if svg else "--svg-text"))
        print("%s: %s was changed outside ste_units since extract/apply%s; refusing to overwrite "
              "(apply --force, or extract --force to re-snapshot)" % (t.name, _rel(t.path), why), file=sys.stderr)
        return 1
    changed = sorted(new)
    if args.dry_run:
        if t.json:
            print("%s: dry run OK: %d unit(s) changed, %d warning(s); nothing written" % (t.name, len(changed), len(warnings)))
            return 0
        with tempfile.TemporaryDirectory() as td:
            tmp = os.path.join(td, os.path.basename(t.path))
            open(tmp, "wb").write(new_raw)
            res = run_runner([(n, d, None) for n, d in _render_targets(t)], [(t.name, tmp)])
        errs = ["%s: %s" % (k, v) for k, v in sorted(res.items()) if v.startswith("ERROR")]
        if errs:
            print("%s: dry run: patched target fails to load: %s" % (t.name, "; ".join(errs)[:500]), file=sys.stderr)
            return 1
        print("%s: dry run OK: %d unit(s) changed, %d warning(s); nothing written" % (t.name, len(changed), len(warnings)))
        return 0
    if new_raw == cur_raw:
        print("%s: %d unit(s) differ from original; target already up to date" % (t.name, len(changed)))
        _write_applied(w, new_raw, changed)
        return 0
    open(w.last, "wb").write(cur_raw)
    open(t.path, "wb").write(new_raw)
    err = None
    if not t.json:
        try:
            with tempfile.TemporaryDirectory() as td:
                py_compile.compile(t.path, cfile=os.path.join(td, "x.pyc"), doraise=True)
        except py_compile.PyCompileError as e:
            err = "py_compile: %s" % e.msg.strip().splitlines()[-1]
    if err is None:
        err = import_check(t)
    if err:
        open(t.path, "wb").write(cur_raw)
        print("%s: patched target failed (%s); previous file restored" % (t.name, err), file=sys.stderr)
        return 1
    _write_applied(w, new_raw, changed)
    print("%s: applied %d changed unit(s) -> %s (previous copy: %s); %d warning(s)"
          % (t.name, len(changed), _rel(t.path), _rel(w.last), len(warnings)))
    return 0


def _write_applied(w, raw, changed):
    with open(w.applied, "w", encoding="utf-8", newline="\n") as fh:
        json.dump({"sha256": _sha(raw), "sha256_norm": _nsha(raw),
                   "applied": datetime.datetime.now().isoformat(timespec="seconds"), "changed": changed},
                  fh, indent=1)


def cmd_status(args):
    t = resolve_target(args.module)
    svg = bool(getattr(args, "svg_text", False))
    w = Work(args, t, svg)
    meta, _text, slots, _c = w.load()
    if not os.path.exists(w.units):
        raise SystemExit("%s: no units.txt; run extract" % _rel(w.units))
    _header, units = read_units(w.units)
    errors, warnings, new = validate(slots, units, _multiline_units(w.units))
    cur = _nsha(open(t.path, "rb").read())
    state = ("original" if cur == _nsha(open(w.original, "rb").read()) else
             "applied" if cur == w.applied_sha() else
             "written by %s apply (apply in this mode would discard that)" % ("prose" if svg else "--svg-text")
             if cur == w.applied_sha(w.other_applied) else "changed outside ste_units")
    print("%s: %d units, %d edited, %d misc; %d validation error(s), %d warning(s); module file: %s"
          % (t.name, len(slots), len(new), sum(s.kind == "misc" for s in slots), len(errors), len(warnings), state))
    by_kind = collections.Counter(s.kind for s in slots if s.uid in new)
    if by_kind:
        print("  edited by kind: %s" % " ".join("%s=%d" % kv for kv in sorted(by_kind.items())))
    for m in errors[:20]:
        print("  " + m)
    return 0


def selftest_one(t, mode, tmpdir, baseline=None):
    """-> (status, detail, extractor or None)"""
    if t.unsupported():
        return "UNSUPPORTED", t.unsupported(), None
    svg = mode == "svg"
    try:
        raw = open(t.path, "rb").read()
        text, bom, nl = decode_source(raw)
        ex = analyze_target(t, text, svg)
        patched = _patched_text(t, text, ex.slots, ex.carriers, {}, nl, force=True)
        err = _syntax_check(t, patched, t.path)
        if err:
            return "FAIL", "patched copy does not parse: %s" % err, ex
        again = analyze_target(t, patched, svg)
    except Exception as e:  # noqa: BLE001 - report any tool failure as FAIL
        return "FAIL", "tool error: %s: %s" % (type(e).__name__, e), None
    a = [(s.kind, s.text) for s in ex.slots]
    b = [(s.kind, s.text) for s in again.slots]
    if a != b:
        i = next((i for i, (x, y) in enumerate(zip(a, b)) if x != y), min(len(a), len(b)))
        return "FAIL", "re-extract differs at unit %d: %r vs %r" % (
            i + 1, a[i] if i < len(a) else None, b[i] if i < len(b) else None), ex
    if not ex.slots:
        return "PASS", "no units", ex
    if t.json:
        canon = lambda s: json.dumps(json.loads(s), ensure_ascii=False, sort_keys=True)  # noqa: E731
        h1, h2 = _sha(canon(text)), _sha(canon(patched))
        return ("PASS", "sha256 %s..." % h1[:12], ex) if h1 == h2 else ("FAIL", "canonical JSON differs", ex)
    tag = "%s.%s" % (t.name, mode)
    tmp = os.path.join(tmpdir, tag, os.path.basename(t.path))
    os.makedirs(os.path.dirname(tmp), exist_ok=True)
    open(tmp, "wb").write(encode_source(patched, bom))
    targets = _render_targets(t)
    outs_a = [(n, d, os.path.join(tmpdir, "%s__%s.%s.orig.json" % (tag, n, d))) for n, d in targets]
    outs_b = [(n, d, os.path.join(tmpdir, "%s__%s.%s.patched.json" % (tag, n, d))) for n, d in targets]
    ra = baseline if (baseline is not None and t.render == "figs") else run_runner(outs_a)
    rb = run_runner(outs_b, [(t.name, tmp)])
    for (n, d, oa), (_n, _d, ob) in zip(outs_a, outs_b):
        key = "%s:%s" % (n, d)
        va, vb = ra.get(key, "ERROR missing"), rb.get(key, "ERROR missing")
        if va.startswith("ERROR"):
            return "FAIL", "original does not render (%s): %s" % (key, va), ex
        if vb.startswith("ERROR"):
            return "FAIL", "patched copy does not render (%s): %s" % (key, vb), ex
        if va != vb:
            detail = _first_difference(oa, ob) if os.path.exists(oa) else "hash differs"
            return "FAIL", "rendered output differs (%s): %s" % (key, detail), ex
    first = ra.get("%s:%s" % targets[0], "")
    return "PASS", "sha256 %s...%s" % (first[:12], " (+%d renders)" % (len(targets) - 1) if len(targets) > 1 else ""), ex


def cmd_selftest(args):
    svg_only = bool(getattr(args, "svg_text", False))
    if args.all:
        jobs = all_targets()
        if svg_only:
            jobs = [(t, m) for t, m in jobs if m == "svg"]
        elif args.prose_only:
            jobs = [(t, m) for t, m in jobs if m == "prose"]
    else:
        t = resolve_target(args.module)
        jobs = [(t, "svg" if svg_only else "prose")]
    with tempfile.TemporaryDirectory(prefix="ste_selftest_") as td:
        baseline = None
        if any(t.render == "figs" for t, _m in jobs):
            figs = sorted({t.name for t, _m in jobs if t.render == "figs"})
            outs = [(f, "figs", os.path.join(td, "base__%s.figs.json" % f)) for f in figs] + \
                   [(p, "paper", os.path.join(td, "base__%s.paper.json" % p)) for p in all_modules()]
            baseline = run_runner(outs)
        with ThreadPoolExecutor(max_workers=min(8, os.cpu_count() or 2)) as pool:
            results = list(zip(jobs, pool.map(lambda j: selftest_one(j[0], j[1], td, baseline), jobs)))
    counts = collections.Counter()
    for (t, mode), (status, detail, ex) in results:
        counts[status] += 1
        n = "%5d units %4d misc" % (len(ex.slots), sum(s.kind == "misc" for s in ex.slots)) if ex else " " * 20
        print("%-11s %-5s %-34s %s  %s" % (status, mode, t.name, n, detail))
    print("selftest: %d PASS, %d FAIL, %d UNSUPPORTED (of %d)"
          % (counts["PASS"], counts["FAIL"], counts["UNSUPPORTED"], len(results)))
    if args.all:
        path = write_report(args, [(t, mode, status, detail, ex) for (t, mode), (status, detail, ex) in results])
        print("report: %s" % _rel(path))
    return 0 if counts["FAIL"] == 0 else 1


def cmd_report(args):
    rows = []
    for t, mode in all_targets():
        if t.unsupported():
            rows.append((t, mode, "UNSUPPORTED", t.unsupported(), None))
            continue
        text, _bom, _nl = decode_source(open(t.path, "rb").read())
        rows.append((t, mode, "-", "", analyze_target(t, text, mode == "svg")))
    print("report: %s" % _rel(write_report(args, rows)))
    return 0


def write_report(args, rows):
    root = work_root(args)
    os.makedirs(root, exist_ok=True)
    path = os.path.join(root, "extract_report.txt")
    out = ["ste_units extract report - %s" % datetime.datetime.now().isoformat(timespec="seconds"),
           "PROSE: units = units.txt entries; misc = text outside the helpers (optional); labels = rule (f) figure",
           "labels (kind label, in=L.*); fig-skip = strings in figure calls not taken (numbers, units, style);",
           "skipped = units that did not round-trip (left untouched); uncaptured = prose-like strings inside",
           "SVG/markup builders (see --svg-text); short = 1-3 word strings passed to other non-helper calls.",
           "SVG-TEXT: elem = text of <text>/<tspan>/<title>/<desc>; helper = literal arguments of text helpers;",
           "loop = literal items of loops that draw text; code-only = element texts made only by code ({expr}),",
           "not extractable; no-words = numbers / units / symbols only.", ""]
    out.append("== PROSE")
    out.append("%-34s %-11s %6s %5s %6s %8s %7s %10s %6s  %s" % ("target", "selftest", "units", "misc", "labels",
                                                                "fig-skip", "skipped", "uncaptured", "short", "notes"))
    tot = collections.Counter()
    for t, mode, status, detail, ex in rows:
        if mode != "prose":
            continue
        if ex is None:
            out.append("%-34s %-11s %6s %5s %6s %8s %7s %10s %6s  %s" % (t.name, status, "-", "-", "-", "-", "-", "-", "-",
                                                                         detail))
            continue
        misc = sum(s.kind == "misc" for s in ex.slots)
        labels = sum(s.kind == "label" and " in=" in s.ctx for s in ex.slots)
        notes = []
        if ex.wrapper_notes:
            notes.append("wrappers: " + "; ".join(ex.wrapper_notes))
        if any(s.has_comment for s in ex.slots):
            notes.append("comment inside units " + " ".join(s.uid for s in ex.slots if s.has_comment))
        if status == "FAIL":
            notes.append(detail)
        out.append("%-34s %-11s %6d %5d %6d %8d %7d %10d %6d  %s" % (
            t.name, status, len(ex.slots), misc, labels, len(ex.gen_skipped), len(ex.skipped), len(ex.uncaptured),
            len(ex.short_labels), " | ".join(notes)))
        tot.update(units=len(ex.slots), misc=misc, labels=labels, gen=len(ex.gen_skipped), skipped=len(ex.skipped),
                   unc=len(ex.uncaptured), short=len(ex.short_labels))
    out.append("%-34s %-11s %6d %5d %6d %8d %7d %10d %6d" % ("TOTAL", "", tot["units"], tot["misc"], tot["labels"],
                                                            tot["gen"], tot["skipped"], tot["unc"], tot["short"]))
    out.append("")
    out.append("== SVG-TEXT")
    out.append("%-34s %-11s %6s %6s %6s %6s %9s %8s %7s" % ("target", "selftest", "units", "elem", "helper", "loop",
                                                            "code-only", "no-words", "skipped"))
    tot = collections.Counter()
    for t, mode, status, detail, ex in rows:
        if mode != "svg":
            continue
        if ex is None:
            out.append("%-34s %-11s %s" % (t.name, status, detail))
            continue
        elem = sum(s.expr in ("inner", "json") for s in ex.slots)
        out.append("%-34s %-11s %6d %6d %6d %6d %9d %8d %7d%s" % (
            t.name, status, len(ex.slots), elem, ex.helper_units, ex.loop_units, ex.stats["code-only"],
            ex.stats["no-words"], len(ex.skipped), ("  " + detail) if status == "FAIL" else ""))
        tot.update(units=len(ex.slots), elem=elem, helper=ex.helper_units, loop=ex.loop_units,
                   code=ex.stats["code-only"], nowords=ex.stats["no-words"], skipped=len(ex.skipped))
    out.append("%-34s %-11s %6d %6d %6d %6d %9d %8d %7d" % ("TOTAL", "", tot["units"], tot["elem"], tot["helper"],
                                                            tot["loop"], tot["code"], tot["nowords"], tot["skipped"]))
    out.append("")
    for t, mode, status, detail, ex in rows:
        if ex is None:
            continue
        if not (ex.slots or ex.skipped or ex.uncaptured or ex.gen_skipped or ex.stats_fieldonly):
            continue
        out.append("== %s  [%s] (%s)" % (t.name, mode, status))
        out.append("   kinds: %s" % (kind_counts(ex.slots) or "-"))
        for line, kind, reason, prev in ex.skipped:
            out.append("   SKIPPED line %d %s: %s | %s" % (line, kind, reason, prev))
        groups = collections.defaultdict(list)
        for line, reason, prev in ex.uncaptured:
            groups[reason].append((line, prev))
        for reason, items in sorted(groups.items()):
            out.append("   UNCAPTURED %d x %s" % (len(items), reason))
            for line, prev in items[:8]:
                out.append("      line %d: %s" % (line, prev))
            if len(items) > 8:
                out.append("      ... %d more" % (len(items) - 8))
        if ex.gen_skipped:
            out.append("   FIGURE STRINGS NOT TAKEN %d e.g. %s" % (
                len(ex.gen_skipped), "; ".join(p for _l, _c, p in ex.gen_skipped[:8])))
        if ex.short_labels:
            callees = collections.Counter(c for _l, c, _p in ex.short_labels)
            out.append("   SHORT STRINGS IN OTHER CALLS %d (by call: %s) e.g. %s" % (
                len(ex.short_labels), ", ".join("%s=%d" % kv for kv in callees.most_common(6)),
                "; ".join(p for _l, _c, p in ex.short_labels[:6])))
        if ex.stats_fieldonly:
            out.append("   CODE-ONLY ELEMENT TEXT %d e.g. %s" % (
                len(ex.stats_fieldonly), "; ".join("l.%d %s" % x for x in ex.stats_fieldonly[:6])))
        out.append("")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(out) + "\n")
    return path


def main(argv=None):
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8")
        except (AttributeError, ValueError):
            pass
    ap = argparse.ArgumentParser(prog="ste_units.py", description="ASD-STE100 units: extract / apply / selftest "
                                 "(prose, and SVG text with --svg-text)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("extract", help="write units.txt / meta.json / original snapshot")
    p.add_argument("module")
    p.add_argument("--work")
    p.add_argument("--force", action="store_true")
    p.add_argument("--svg-text", action="store_true")
    p = sub.add_parser("apply", help="validate units.txt and patch the target")
    p.add_argument("module")
    p.add_argument("--work")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--force", action="store_true")
    p.add_argument("--svg-text", action="store_true")
    p = sub.add_parser("selftest", help="prove extract+emit is lossless")
    p.add_argument("module", nargs="?")
    p.add_argument("--all", action="store_true")
    p.add_argument("--svg-text", action="store_true")
    p.add_argument("--prose-only", action="store_true")
    p.add_argument("--work")
    p = sub.add_parser("status", help="unit / edit counts")
    p.add_argument("module")
    p.add_argument("--work")
    p.add_argument("--svg-text", action="store_true")
    p = sub.add_parser("report", help="write extract_report.txt")
    p.add_argument("--work")
    args = ap.parse_args(argv)
    if args.cmd == "selftest" and not args.all and not args.module:
        ap.error("selftest needs a target or --all")
    return {"extract": cmd_extract, "apply": cmd_apply, "selftest": cmd_selftest,
            "status": cmd_status, "report": cmd_report}[args.cmd](args)


if __name__ == "__main__":
    sys.exit(main())
