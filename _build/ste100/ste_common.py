# -*- coding: utf-8 -*-
"""Shared helpers for the ASD-STE100 tooling: HTML->text, sentence split, STE word count,
units-file I/O.  No third-party imports (spaCy lives in ste_lint.py, optional)."""
import html as _html
import re

# --------------------------------------------------------------------------- units file
UNIT_HEADER = re.compile(r"^@@ (?P<id>U\d+) \| (?P<kind>[^|]+?) \| (?P<ctx>.*)$")


class Unit:
    __slots__ = ("id", "kind", "ctx", "text", "line")

    def __init__(self, id, kind, ctx, text, line=0):
        self.id, self.kind, self.ctx, self.text, self.line = id, kind, ctx, text, line

    def __repr__(self):
        return "Unit(%s,%s,%r)" % (self.id, self.kind, self.text[:30])


def read_units(path):
    """Parse a units file -> (header_lines, [Unit])."""
    units, header, cur = [], [], None
    with open(path, encoding="utf-8") as fh:
        for n, line in enumerate(fh, 1):
            line = line.rstrip("\n")
            m = UNIT_HEADER.match(line)
            if m:
                if cur:
                    units.append(cur)
                cur = Unit(m.group("id"), m.group("kind").strip(), m.group("ctx").strip(), "", n)
                continue
            if cur is None:
                header.append(line)
            else:
                cur.text = (cur.text + " " + line.strip()).strip() if cur.text else line.strip()
    if cur:
        units.append(cur)
    return header, units


def write_units(path, header, units):
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        for h in header:
            fh.write(h + "\n")
        for u in units:
            fh.write("@@ %s | %s | %s\n%s\n\n" % (u.id, u.kind, u.ctx, u.text))


# --------------------------------------------------------------------------- html -> text
_SUP_CITE = re.compile(r"<sup[^>]*class=['\"]cite['\"][^>]*>.*?</sup>", re.I | re.S)
_TAG = re.compile(r"<[^>]+>")
_PLACEHOLDER = re.compile(r"⟦[^⟧]*⟧")


_CODE = re.compile(r"<code\b[^>]*>.*?</code>", re.I | re.S)


def html_to_text(s):
    s = _PLACEHOLDER.sub(" ", s)          # citation / expression placeholders from the units file
    s = _SUP_CITE.sub(" ", s)
    s = _CODE.sub(" CODEX ", s)           # inline code (identifiers, entity ids) is not prose: one ALLCAPS token
    s = re.sub(r"<(br|/p|/li|/div)[^>]*>", " ", s, flags=re.I)
    s = _TAG.sub("", s)
    s = _html.unescape(s)
    s = s.replace("\u00a0", " ").replace("\u2009", " ").replace("\u202f", " ")
    return re.sub(r"\s+", " ", s).strip()


# --------------------------------------------------------------------------- masking
ABBREV = ["e.g.", "i.e.", "etc.", "vs.", "Fig.", "fig.", "No.", "no.", "approx.", "cf.", "Dr.", "St.",
          "sp.", "spp.", "var.", "ca.", "incl.", "al.", "Co.", "Ltd.", "Inc.", "Jr.", "a.m.", "p.m.",
          "Mr.", "Ms.", "Mrs.", "Vol.", "vol.", "pp.", "ed.", "eds.", "Ref.", "ref."]
UNIT_WORDS = (
    r"%|‰|°\s?[CF]|℃|℉|degrees?(?:\s+(?:Celsius|Fahrenheit|C|F))?|percent|"
    r"[kKmMµμnN]?[gGLl]\b|mL|ml|kg|mg|µg|μg|[kcmµμ]?m(?:\u00b2|\u00b3|2|3)?|"
    r"ppm|ppb|ppt|mS/cm|µS/cm|μS/cm|dS/m|mS|"
    r"kPa|MPa|Pa|hPa|mbar|bar|psi|mmHg|W|kW|MW|Wh|kWh|mA|V|kV|A|Hz|kHz|MHz|lux|lx|"
    r"µmol(?:/m²/s|·m⁻²·s⁻¹|/m2/s)?|μmol(?:/m²/s)?|mol|mmol|nm|"
    r"L/h|l/h|L/min|mL/min|mL/h|mL/L|g/L|mg/L|g/m²|kg/m²|kg/m3|g/m2|"
    r"min(?:utes?)?|hours?|hrs?|h|seconds?|secs?|s|days?|d|weeks?|wks?|months?|years?|yrs?|"
    r"litres?|liters?|metres?|meters?|grams?|kilograms?|millilit(?:re|er)s?|millimet(?:re|er)s?|"
    r"centimet(?:re|er)s?|kilomet(?:re|er)s?|inch(?:es)?|in|ft|feet|foot|lb|lbs|oz|gal|gallons?|"
    r"a\.m\.|p\.m\.|am|pm|cfm|CFM|PPFD|DLI|VPD|kcal|MJ|J|kJ|mV|ohms?|Ω|mm\u00b2|cc"
)
NUM = r"[-+−–]?\d+(?:[.,]\d+)*"
NUMRANGE = NUM + r"(?:\s?(?:[–—-]|to)\s?" + r"\d+(?:[.,]\d+)*)?"
NUMUNIT = re.compile(r"(?<![\w.])(" + NUMRANGE + r")(?:\s?(?:" + UNIT_WORDS + r")(?![A-Za-z]))?")
QUOTED = re.compile(r"\"[^\"]*\"|“[^”]*”|‘[^’]{3,}’")
ALNUM_ID = re.compile(r"\b(?=[A-Za-z0-9\-]*\d)(?=[A-Za-z0-9\-]*[A-Za-z])[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*\b")
SLASHED = re.compile(r"\b[A-Za-z]+(?:/[A-Za-z]+)+\b")

PAREN_TOKEN = "§P§"
QUOTE_TOKEN = "§Q§"
NUM_TOKEN = "§N§"
ABBR_TOKEN = "§A§"
ID_TOKEN = "§I§"


def extract_parens(s):
    """Return (outer_text_with_PAREN_TOKEN, [inner_texts]) for top-level parentheses."""
    out, inners, depth, buf = [], [], 0, []
    for ch in s:
        if ch == "(":
            if depth == 0:
                buf = []
            else:
                buf.append(ch)
            depth += 1
        elif ch == ")" and depth > 0:
            depth -= 1
            if depth == 0:
                inner = "".join(buf).strip()
                # citation-like or numeric identifiers only -> single token, no sentence
                inners.append(inner)
                out.append(" " + PAREN_TOKEN + " ")
            else:
                buf.append(ch)
        else:
            (buf if depth > 0 else out).append(ch)
    if depth > 0:   # unbalanced: keep the text
        out.append("".join(buf))
    return re.sub(r"\s+", " ", "".join(out)).strip(), inners


_ABBR_ALWAYS = ["e.g.", "i.e.", "vs.", "Fig.", "fig.", "approx.", "cf.", "viz.", "Dr.", "Mr.", "Ms.", "Mrs.",
                "St.", "Co.", "Ltd.", "Inc.", "Jr.", "spp.", "a.m.", "p.m.", "incl."]
# these also end ordinary words ("closed.", "feed.", "red."): protect them only as whole abbreviations
# that are followed by a lower-case word, a digit, a bracket or a quote.
_ABBR_COND = ["etc.", "No.", "no.", "Vol.", "vol.", "Ref.", "ref.", "sp.", "var.", "ca.", "al.", "ed.", "eds.", "pp."]
_ABBR_ALWAYS_RE = re.compile(r"(?<![A-Za-z])(" + "|".join(re.escape(a) for a in _ABBR_ALWAYS) + r")")
_ABBR_COND_RE = re.compile(r"(?<![A-Za-z0-9])(" + "|".join(re.escape(a) for a in _ABBR_COND) + r")(?=\s+[0-9a-z(\[\"“‘])")
_DOT = chr(0x2024)          # one-dot leader: stands in for a full stop that does not end a sentence


def protect_abbrev(s):
    s = _ABBR_ALWAYS_RE.sub(lambda m: m.group(1).replace(".", _DOT), s)
    s = _ABBR_COND_RE.sub(lambda m: m.group(1).replace(".", _DOT), s)
    return s


def restore_abbrev(s):
    return s.replace(_DOT, ".")


# a sentence ends at . ! ? (optionally followed by a closing quote or bracket) and a space, when
# the next sentence starts with a capital letter, digit, quote or bracket
SENT_SPLIT = re.compile(r"(?:(?<=[.!?])|(?<=[.!?][\"'’”)\]]))\s+(?=[A-Z0-9§\"“'‘(\[])")


def split_sentences(s):
    s = protect_abbrev(s)
    # protect decimals and version-like numbers
    s = re.sub(r"(\d)\.(\d)", "\\1\u2024\\2", s)
    parts = [restore_abbrev(p).strip() for p in SENT_SPLIT.split(s) if p.strip()]
    return parts


def count_words(sentence):
    """STE word count (rules 8.4-8.7): masked units count as one word each."""
    s = sentence
    s = QUOTED.sub(" " + QUOTE_TOKEN + " ", s)
    s = NUMUNIT.sub(" " + NUM_TOKEN + " ", s)
    s = SLASHED.sub(" " + ABBR_TOKEN + " ", s)
    toks = re.findall(r"§[A-Z]§|[A-Za-z0-9µμ°%][\w'’\-µμ°%.]*", s)
    n = 0
    for t in toks:
        if t.strip("-.'’") == "":
            continue
        n += 1
    return n


def tokenize_for_vocab(sentence):
    """Return list of (token, is_sentence_initial) for vocabulary checking.  Quoted text,
    numbers+units, alphanumeric ids and ALLCAPS abbreviations are removed."""
    s = QUOTED.sub(" ", sentence)
    s = NUMUNIT.sub(" ", s)
    s = SLASHED.sub(" ", s)
    s = s.replace(PAREN_TOKEN, " ")
    toks = re.findall(r"[A-Za-z][A-Za-z'’\-]*[A-Za-z]|[A-Za-z]", s)
    return toks


def is_acronym(tok):
    letters = [c for c in tok if c.isalpha()]
    if len(letters) < 2:
        return False
    up = sum(c.isupper() for c in letters)
    return up >= 2 and (up == len(letters) or up >= 2)


def plural_bases(w):
    """Singular candidates for a plural noun (plural only: never -ed / -ing forms)."""
    yield w
    if w.endswith("ies") and len(w) > 4:
        yield w[:-3] + "y"
    if w.endswith("ves") and len(w) > 4:
        yield w[:-3] + "f"
        yield w[:-3] + "fe"
    if w.endswith("es") and len(w) > 3:
        yield w[:-2]
    if w.endswith("s") and len(w) > 2:
        yield w[:-1]
    if w.endswith("a") and len(w) > 3:        # stomata / criteria style plurals
        yield w[:-1] + "um"
        yield w[:-1] + "on"


def verb_bases(w):
    """Base-form candidates for -s / -ed / -d verb forms (never -ing)."""
    yield w
    if w.endswith("ies") and len(w) > 4:
        yield w[:-3] + "y"
    if w.endswith("es") and len(w) > 3:
        yield w[:-2]
    if w.endswith("s") and len(w) > 2:
        yield w[:-1]
    if w.endswith("ied") and len(w) > 4:
        yield w[:-3] + "y"
    if w.endswith("ed") and len(w) > 3:
        yield w[:-2]
        yield w[:-1]


def stem_variants(w):
    """All base-form candidates (used for the not-approved lookup only)."""
    seen = set()
    for gen in (plural_bases(w), verb_bases(w)):
        for v in gen:
            if v not in seen:
                seen.add(v)
                yield v
    if w.endswith("ing") and len(w) > 4:
        yield w[:-3]
        yield w[:-3] + "e"
