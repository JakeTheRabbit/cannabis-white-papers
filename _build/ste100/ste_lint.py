# -*- coding: utf-8 -*-
"""ASD-STE100 Issue 9 linter for the Cannabis White Papers.

Checks text against the writing rules (sentence/paragraph length with the Rule 8 word count,
verb forms, -ing forms, passive voice, semicolons, contractions, American spelling, gendered
pronouns, Latin abbreviations ...) and against the Issue 9 dictionary word list plus the
project's technical-noun (TN) / technical-verb (TV) lists.

It is an aid, not a certification: a clean run means "no automated finding".

Inputs (pick one):
  --units FILE      a units file (see ste_units.py)           <- what rewriting agents use
  --module NAME     a paper module, e.g. paper_cloning        <- rendered text of SECTIONS
  --md FILE         a markdown file (papers/*.md)
  --text "..."      a snippet
  --stdin           text on stdin (one unit per blank-line-separated paragraph)

Options:
  --level E|W       minimum severity to print (default W)
  --max N           stop printing after N findings (default 200)
  --summary         counts only
  --words           also list every distinct unknown word with its context count
  --no-spacy        skip the spaCy layer (faster)
  --json            machine-readable output

Technical nouns / verbs (Rules 1.5, 1.12):
  data/tn_core.txt, data/tn_<slug>.txt, data/tv_core.txt, data/tv_<slug>.txt (one entry per line,
  '#' comments, 'term | note').  Add entries with:
      ste_lint.py --add-tn  <slug> "dryback" "slab"
      ste_lint.py --add-tv  <slug> "irrigate"
Exit code: 1 if any E finding, else 0.
"""
import argparse
import glob
import json
import os
import re
import sys
from collections import Counter, OrderedDict, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from ste_common import (Unit, read_units, html_to_text, extract_parens, split_sentences, count_words,  # noqa: E402
                        tokenize_for_vocab, is_acronym, stem_variants, plural_bases, verb_bases, QUOTED, NUMUNIT, SLASHED,
                        PAREN_TOKEN, protect_abbrev, restore_abbrev)

DATA = os.path.join(HERE, "data")

# --------------------------------------------------------------------------- static word sets
NUMBER_WORDS = set("""zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen
fifteen sixteen seventeen eighteen nineteen twenty thirty forty fifty sixty seventy eighty ninety hundred thousand
million billion first second third fourth fifth sixth seventh eighth ninth tenth half quarter third thirds
fifths tenths dozen""".split())

MODAL_BAD = {"may": "can", "might": "can", "could": "can (possibility) / was able", "should": "must / (recast)",
             "would": "will / (recast)", "shall": "must", "ought": "must"}
GENDER = {"he", "she", "his", "her", "him", "hers", "himself", "herself", "he's", "she's"}
GENDER_WARN = {"man", "men", "woman", "women", "male", "female", "guys", "mankind", "manpower"}
LATIN = re.compile(r"\b(e\.g\.|i\.e\.|etc\.?|vs\.?|cf\.|viz\.|et al\.|n\.b\.|ca\.)", re.I)
CONTRACTION = re.compile(r"\b[A-Za-z]+(?:n['’]t|['’](?:re|ll|ve|m|d))\b|\b(?:it|that|there|here|what|who|let)['’]s\b", re.I)
PHRASAL = re.compile(r"\b(set up|carry out|carried out|turn on|turn off|turns on|turns off|find out|check out|look at|looks at|"
                     r"go up|goes up|go down|goes down|build up|builds up|dry out|dries out|flush out|wash out|break down|"
                     r"breaks down|take up|takes up|pick up|cut back|top up|tops up|leave out|make up|makes up|come up|"
                     r"comes up|give off|gives off|put off|point out|pull out|pulls out|work out|works out|bring about|"
                     r"back off|ramp up|ramps up|speed up|speeds up|slow down|slows down|shut down|shuts down|"
                     r"line up|lines up|fill up|fills up|mix up|mixes up|run out|runs out|run off|runs off|"
                     r"drop off|drops off|level off|levels off|sit in|sits in|stand by|hold on|holds on|"
                     r"clean up|cleans up|wipe down|wipe off|rub off|use up|uses up|add up|adds up|show up|shows up)\b", re.I)
ING_OK = {"lighting", "opening", "routing", "servicing", "mating", "missing", "remaining", "something", "during",
          "ring", "spring", "string", "thing", "things", "ceiling", "nothing", "anything", "everything", "evening",
          "morning", "king", "wing", "bearing", "bearings", "sibling", "darling", "sing", "bring", "swing", "sting",
          "pudding", "building", "buildings"}
BE = r"(?:is|are|was|were|be|been|being|am)"
PASSIVE_BY = re.compile(r"\b" + BE + r"\s+(?:\w+ly\s+)?\w+(?:ed|en|wn|nt|ld|ht|id|ut|et|it)\s+by\b", re.I)
MODAL_BE_PP = re.compile(r"\b(?:can|must|will|cannot|do not|does not)\s+(?:not\s+)?be\s+(?:\w+ly\s+)?(\w+(?:ed|en|wn|nt|ld|ht|id|ut|et|it)|made|done|set|put|cut|run|kept|held|shown|given|seen|found|known|used|taken)\b", re.I)
PERFECT = re.compile(r"\b(?:has|have|had)\s+(?:not\s+|never\s+|already\s+|just\s+|also\s+)?(?:been|\w+ed|\w+en|done|made|gone|shown|seen|taken|given|kept|held|set|put|cut|run|become|come|found|known|grown|got|gotten|read|left|lost|built|sent|spent|told|thought|brought|bought|caught|taught|sought|won|written|chosen|begun|drunk|swum|sung|rung)\b", re.I)
PROGRESSIVE = re.compile(r"\b(?:is|are|was|were|am|be|been|being)\s+(?:not\s+|still\s+|also\s+|always\s+|currently\s+)?\w+ing\b", re.I)
BE_PP = re.compile(r"\b" + BE + r"\s+(?:not\s+|also\s+|then\s+|always\s+|only\s+|usually\s+)?(?:\w+ly\s+)?(\w+(?:ed|wn)|made|done|set|put|cut|run|kept|held|shown|given|seen|found|known|taken|grown|built|lost|left|sent|spent|told|written|broken|chosen|driven|drawn|eaten|fallen|hidden|spoken|thrown|worn)\b", re.I)
GR1_THAT = re.compile(r"\b(make sure|makes sure|recommends?)\s+(?!that\b)(the|a|an|all|each|there|it|you|your|no|these|this)\b", re.I)
AGAINST_LIMIT = re.compile(r"\b(above|below)\s+(?:about\s+|approximately\s+)?(?:\d|a\s+\d|[0-9])", re.I)
ABOUT_NUM = re.compile(r"\babout\s+(?:\d|one\b|two\b|three\b|four\b|five\b|six\b|seven\b|eight\b|nine\b|ten\b|half\b)", re.I)
FOLLOW_OBJ = re.compile(r"\bfollow(?:s|ed)?\s+(?:the|these|this|your|all|each|its|our|any)\s+(?:\w+\s+)?(?:steps?|instructions?|procedures?|directions?|guidance|protocols?|recommendations?|rules?|manual|sop|advice|plan|schedule|guidelines?)\b", re.I)
SEE_IF = re.compile(r"\bsee(?:s|ing)?\s+(?:if|whether|how|what|why|that)\b", re.I)
WEAR_GO = re.compile(r"\b(?:wear(?:s)?|goes? (?:up|down|through|wrong|bad|out|off)|went (?:up|down|wrong))\b", re.I)
TURN_COLOR = re.compile(r"\bturn(?:s|ed)?\s+(?:to\s+)?(?:red|green|yellow|brown|white|black|blue|purple|orange|pink|gray|grey|dark|pale|light|pink|cloudy|soft|hard|slimy)\b", re.I)
SEMICOLON = re.compile(r";")
AND_OR = re.compile(r"\band/or\b", re.I)
DASH_BREAK = re.compile(r"\s[—–]\s|—")

# imperative detection: leading subordinate clause then a verb in base form
LEAD_CLAUSE = re.compile(r"^(?:if|when|whenever|before|after|once|while|until|unless|as soon as|as|for|to|during|in|on|at|with|"
                         r"without|by|from|because|since|where|between|throughout|under|after|then|thus)\b[^,]{0,120},\s+", re.I)

# US spelling: British -> American
UK_US = {
    "colour": "color", "colours": "colors", "coloured": "colored", "metre": "meter", "metres": "meters",
    "litre": "liter", "litres": "liters", "centre": "center", "centres": "centers", "fibre": "fiber",
    "fibres": "fibers", "grey": "gray", "analyse": "analyze", "analysed": "analyzed", "analyses": "analyzes",
    "organise": "organize", "organised": "organized", "behaviour": "behavior", "behaviours": "behaviors",
    "favour": "favor", "favourable": "favorable", "programme": "program", "programmes": "programs",
    "tyre": "tire", "aluminium": "aluminum", "sulphur": "sulfur", "sulphate": "sulfate", "labour": "labor",
    "defence": "defense", "licence": "license", "licences": "licenses", "practise": "practice",
    "recognise": "recognize", "recognised": "recognized", "minimise": "minimize", "minimised": "minimized",
    "maximise": "maximize", "maximised": "maximized", "optimise": "optimize", "optimised": "optimized",
    "stabilise": "stabilize", "stabilised": "stabilized", "sterilise": "sterilize", "sterilised": "sterilized",
    "sanitise": "sanitize", "sanitised": "sanitized", "oxidise": "oxidize", "oxidised": "oxidized",
    "utilise": "utilize", "utilised": "utilized", "normalise": "normalize", "normalised": "normalized",
    "standardise": "standardize", "standardised": "standardized", "synchronise": "synchronize",
    "characterise": "characterize", "characterised": "characterized", "summarise": "summarize",
    "summarised": "summarized", "categorise": "categorize", "categorised": "categorized",
    "crystallise": "crystallize", "mineralise": "mineralize", "pressurise": "pressurize", "pressurised": "pressurized",
    "ventilate": "ventilate", "catalogue": "catalog", "dialogue": "dialog", "enrol": "enroll", "fulfil": "fulfill",
    "gaol": "jail", "jewellery": "jewelry", "mould": "mold", "moulds": "molds", "moulding": "molding",
    "moult": "molt", "plough": "plow", "skilful": "skillful", "smoulder": "smolder", "speciality": "specialty",
    "storey": "story", "towards": "toward", "whilst": "while", "amongst": "among", "learnt": "learned",
    "spelt": "spelled", "burnt": "burned", "dreamt": "dreamed", "leant": "leaned", "oestrogen": "estrogen",
    "haemoglobin": "hemoglobin", "anaemia": "anemia", "foetus": "fetus", "diarrhoea": "diarrhea",
    "paediatric": "pediatric", "orientated": "oriented", "artefact": "artifact", "artefacts": "artifacts",
    "tonne": "metric ton", "tonnes": "metric tons", "kerb": "curb", "draught": "draft", "cheque": "check",
    "cosy": "cozy", "vigour": "vigor", "odour": "odor", "odours": "odors", "rigour": "rigor", "humour": "humor",
    "honour": "honor", "neighbour": "neighbor", "neighbours": "neighbors", "harbour": "harbor", "rumour": "rumor",
    "saviour": "savior", "splendour": "splendor", "tumour": "tumor", "vapour": "vapor", "vapours": "vapors",
    "flavour": "flavor", "flavours": "flavors", "endeavour": "endeavor", "armour": "armor", "clamour": "clamor",
    "demeanour": "demeanor", "fervour": "fervor", "glamour": "glamor", "parlour": "parlor", "valour": "valor",
    "manoeuvre": "maneuver", "theatre": "theater", "calibre": "caliber", "litter": "litter", "lustre": "luster",
    "sombre": "somber", "spectre": "specter", "sabre": "saber", "meagre": "meager", "goitre": "goiter",
    "sepulchre": "sepulcher", "reconnoitre": "reconnoiter", "mitre": "miter", "nitre": "niter",
    "ageing": "aging", "acknowledgement": "acknowledgment", "judgement": "judgment", "cancelled": "canceled",
    "cancelling": "canceling", "travelled": "traveled", "levelled": "leveled", "labelled": "labeled",
    "modelled": "modeled", "fuelled": "fueled", "signalled": "signaled", "channelled": "channeled",
    "counsellor": "counselor", "instalment": "installment", "enrolment": "enrollment", "skilfully": "skillfully",
    "wilful": "willful", "willingly": "willingly", "fulfilment": "fulfillment", "grey-green": "gray-green",
    "decolourise": "decolorize", "decolourised": "decolorized", "photosynthesise": "photosynthesize",
    "photosynthesises": "photosynthesizes", "capitalise": "capitalize", "hypothesise": "hypothesize",
    "generalise": "generalize", "generalised": "generalized", "specialise": "specialize", "specialised": "specialized",
    "emphasise": "emphasize", "emphasised": "emphasized", "realise": "realize", "realised": "realized",
    "apologise": "apologize", "criticise": "criticize", "customise": "customize", "customised": "customized",
    "digitise": "digitize", "harmonise": "harmonize", "itemise": "itemize", "localise": "localize",
    "mobilise": "mobilize", "neutralise": "neutralize", "neutralised": "neutralized", "penalise": "penalize",
    "prioritise": "prioritize", "prioritised": "prioritized", "randomise": "randomize", "randomised": "randomized",
    "revolutionise": "revolutionize", "scrutinise": "scrutinize", "visualise": "visualize", "visualised": "visualized",
    "vaporise": "vaporize", "vaporised": "vaporized", "homogenise": "homogenize", "homogenised": "homogenized",
    "pasteurise": "pasteurize", "caramelise": "caramelize", "deionised": "deionized", "ionise": "ionize",
    "ionised": "ionized", "chlorinated": "chlorinated", "polarised": "polarized", "oxygenated": "oxygenated",
    "mineralised": "mineralized", "desiccate": "desiccate", "colourless": "colorless", "colourful": "colorful",
    "discolouration": "discoloration", "discoloured": "discolored", "decolouration": "decoloration",
    "aeration": "aeration", "aerate": "aerate", "aerated": "aerated",
}
UK_US = {k: v for k, v in UK_US.items() if k != v}

# Words that are approved in one part of speech but not in another: filled from the dictionary.

# --------------------------------------------------------------------------- loading
def _read_list(path):
    out = []
    if os.path.exists(path):
        for line in open(path, encoding="utf-8"):
            line = line.split("#", 1)[0].split("|", 1)[0].strip().lower()
            if line:
                out.append(line)
    return out


class Lexicon:
    """Dictionary + technical nouns/verbs.  With slug=None every data/tn_*.txt and tv_*.txt is loaded (global
    view).  With a slug only the shared lists (core*, promoted) and that paper's own tn_<slug>.txt /
    tv_<slug>.txt are loaded, so one paper's additions never legitimise words in another paper."""

    def __init__(self, slug=None):
        p = os.path.join(DATA, "ste_words.json")
        if not os.path.exists(p):
            sys.exit("data/ste_words.json is missing. Run:  python _build/ste100/build_dictionary.py")
        d = json.load(open(p, encoding="utf-8"))
        self.slug = slug
        self.forms = set(w for w in d["approved_forms"] if w and w != "...")
        self.headwords = d["approved_headwords"]
        self.not_approved = d["not_approved"]
        self.tn_words, tn_phrases = set(), set()
        self.tv_words = set()
        self.tn_files, self.tv_files = [], []
        shared = ("core", "promoted")
        for kind in ("tn", "tv"):
            for f in sorted(glob.glob(os.path.join(DATA, kind + "_*.txt"))):
                name = os.path.basename(f)[len(kind) + 1:-4]
                if slug is not None and not (name.startswith(shared) or name == slug):
                    continue
                if kind == "tn":
                    self.tn_files.append(f)
                    for t in _read_list(f):
                        if " " in t:
                            tn_phrases.add(t)
                        else:
                            self.tn_words.add(t)
                else:
                    self.tv_files.append(f)
                    self.tv_words.update(_read_list(f))
        # multi-word entries cover the words inside them when the whole phrase matches
        self.tn_phrases = sorted(tn_phrases, key=lambda s: -len(s.split()))
        # words that are approved as one POS and not approved as another (homographs)
        self.homographs = {}
        for w, info in self.not_approved.items():
            ap = self.headwords.get(w)
            if ap:
                self.homographs[w] = (set(ap), set(info["pos"]))

    def is_tn(self, w):
        """Technical noun: listed word or its plural. -ed / -ing forms are NOT accepted (Rules 1.7, 3.5)."""
        return any(v in self.tn_words for v in plural_bases(w))

    def is_tv(self, w):
        """Technical verb: listed base form or its -s / -ed forms (no -ing)."""
        return any(v in self.tv_words for v in verb_bases(w))

    def approved(self, w):
        if w in self.forms or w in NUMBER_WORDS:
            return True
        # plural of an approved noun
        if w.endswith("s") and w[:-1] in self.forms and "noun" in self.headwords.get(w[:-1], ["noun"]):
            return True
        if w.endswith("es") and w[:-2] in self.forms and "noun" in self.headwords.get(w[:-2], ["noun"]):
            return True
        if w.endswith("ies") and (w[:-3] + "y") in self.forms:
            return True
        # adverb from an approved adjective
        if w.endswith("ly") and (w[:-2] in self.forms and "adjective" in self.headwords.get(w[:-2], ["adjective"])):
            return True
        if w.endswith("ily") and (w[:-3] + "y") in self.forms:
            return True
        # a hyphenated word with the "-s" possessive etc. handled by caller
        return False


_LEX = {}


def lex(slug=None):
    if slug not in _LEX:
        _LEX[slug] = Lexicon(slug)
    return _LEX[slug]


# --------------------------------------------------------------------------- spaCy (optional)
_NLP = None


def nlp():
    global _NLP
    if _NLP is None:
        try:
            import spacy
            _NLP = spacy.load("en_core_web_sm", disable=["ner", "lemmatizer"])
        except Exception:
            _NLP = False
    return _NLP or None


# --------------------------------------------------------------------------- findings
class Finding:
    __slots__ = ("unit", "sev", "rule", "msg", "ctx")

    def __init__(self, unit, sev, rule, msg, ctx=""):
        self.unit, self.sev, self.rule, self.msg, self.ctx = unit, sev, rule, msg, ctx

    def asdict(self):
        return {"unit": self.unit, "sev": self.sev, "rule": self.rule, "msg": self.msg, "ctx": self.ctx}


def excerpt(s, m=None, width=70):
    if m is None:
        return s[:width * 2]
    a = max(0, m.start() - width // 2)
    b = min(len(s), m.end() + width // 2)
    return ("…" if a else "") + s[a:b] + ("…" if b < len(s) else "")


# --------------------------------------------------------------------------- core checks
HEADING_KINDS = {"title", "kicker", "heading", "section.title", "eyebrow", "callout.title", "defterm.term",
                 "th", "card.title", "step.title", "kv.key", "stage.title", "meta", "tag", "stage.dur", "stage.num",
                 "table.header", "figure.label", "label", "chip", "stage.num", "svglabel",
                 "h1", "h2", "h3", "h4", "h5", "h6"}
PROCEDURAL_KINDS = {"step", "step.title", "step.body"}
SAFETY_CTX = re.compile(r"\bkind=(?:warn|danger|caution)\b")
LABEL_CTX = re.compile(r"\bin=\S*L\.")        # diagram labels (misc units found inside figure-generator calls)


def is_imperative(sentence, L):
    s = sentence.strip()
    s = LEAD_CLAUSE.sub("", s, count=1)
    toks = re.findall(r"[A-Za-z][A-Za-z\-']*", s)
    if not toks:
        return False
    w = toks[0].lower()
    second = toks[1].lower() if len(toks) > 1 else ""
    if second in ("of", "is", "are", "was", "were", "has", "have", "will", "can", "must", "does", "did", "and", "or",
                  "that", "which", "who", "cannot"):
        return False                      # "Record of the visit ...", "Use is ...": a noun phrase, not a command
    if w in ("do", "make", "let", "be", "never", "always"):
        return True
    if w in L.headwords and "verb" in L.headwords[w]:
        # sentence-initial approved verb in base form (not 3rd person / past)
        return not (w.endswith("s") and w[:-1] in L.headwords) and w not in ("is", "are", "was", "were", "has", "can", "will", "must", "cannot")
    if w in L.tv_words:
        return True
    return False


def count_sentence_words(sent):
    return count_words(sent)


def spacy_pos_map(text):
    n = nlp()
    if not n:
        return {}
    out = {}
    for t in n(text):
        out[t.idx] = (t.text, t.pos_, t.dep_, t.tag_)
    return out


def check_unit(u, L, use_spacy, unknown_counter, findings):
    """Run all checks on one unit (kind decides which rules apply)."""
    raw = u.text
    kind = u.kind
    if "in=refs" in (u.ctx or ""):
        return                              # bibliography: quoted material, not STE prose
    text = html_to_text(raw)
    if not text:
        return
    uid = u.id
    heading = kind in HEADING_KINDS
    procedural_unit = kind in PROCEDURAL_KINDS or bool(SAFETY_CTX.search(u.ctx or ""))
    if kind == "misc" and LABEL_CTX.search(u.ctx or ""):
        heading = True                      # diagram label: vocabulary rules apply, sentence rules do not

    def add(sev, rule, msg, ctx=""):
        findings.append(Finding(uid, sev, rule, msg, ctx))

    # --- punctuation / char level (applies to all)
    for m in SEMICOLON.finditer(text):
        add("E", "R8.1", "semicolon: write two sentences", excerpt(text, m))
    for m in CONTRACTION.finditer(text):
        add("E", "R4.2", "contraction: write the words in full", excerpt(text, m))
    for m in LATIN.finditer(text):
        add("E", "GR-6", "Latin abbreviation '%s': use English words" % m.group(0), excerpt(text, m))
    for m in AND_OR.finditer(text):
        add("W", "R4.1", "'and/or': choose 'and' or 'or', or write two sentences", excerpt(text, m))
    for m in re.finditer(r"\s&\s", text):
        add("W", "R1.1", "'&': write 'and'", excerpt(text, m))
    for m in DASH_BREAK.finditer(text):
        add("W", "R8", "dash used as a break: write two short sentences", excerpt(text, m))
    for m in re.finditer(r"\b(?:" + "|".join(sorted(GENDER, key=len, reverse=True)) + r")\b", text, re.I):
        add("E", "GR-7", "gendered pronoun '%s': use 'the grower', 'the operator', 'they' is not approved: recast" % m.group(0), excerpt(text, m))
    for m in re.finditer(r"\b(" + "|".join(GENDER_WARN) + r")\b", text, re.I):
        add("W", "GR-7", "gendered word '%s'" % m.group(0), excerpt(text, m))

    # --- spelling (US)
    for m in re.finditer(r"\b[A-Za-z]+\b", text):
        w = m.group(0).lower()
        if w in UK_US:
            add("E", "R1.14", "British spelling '%s' -> '%s'" % (m.group(0), UK_US[w]), excerpt(text, m))

    if heading:
        sentences_masked = [(text, False)]
    else:
        sentences_masked = None

    # --- sentence level
    outer, inners = extract_parens(text)
    sent_list = []
    for s in split_sentences(outer):
        sent_list.append((s, False))
    for inn in inners:
        # inner parenthetical text is its own sentence; skip pure identifiers/numbers/units/abbr
        if re.fullmatch(r"[\w .,/%°+\-–−×=<>≥≤:°µμ*]*", inn) and len(re.findall(r"[A-Za-z]{4,}", inn)) == 0:
            continue
        if re.fullmatch(r"(?:refer to )?(?:figure|fig\.|table|section|paper)\s*\w*", inn, re.I):
            continue
        for s in split_sentences(inn):
            sent_list.append((s, True))

    # paragraph length: every <p> inside the unit counts on its own (a long unit can be split with </p><p>)
    if kind in ("p", "lead", "callout.body", "defterm.body", "card.body", "step.body", "li", "note", "text"):
        for part in re.split(r"</p>\s*<p[^>]*>", raw):
            ptxt = html_to_text(part)
            if not ptxt:
                continue
            n_sent = len(split_sentences(extract_parens(ptxt)[0]))
            if n_sent > 6:
                add("E", "R6.6", "paragraph has %d sentences (max 6): split it with </p><p>" % n_sent, ptxt[:80])

    for sent, in_paren in sent_list:
        words = count_sentence_words(sent)
        if heading and kind in ("title", "sub", "kicker", "section.title", "eyebrow"):
            if words > 20:
                add("W", "R5.1", "heading has %d words" % words, sent[:90])
        # Procedural or descriptive?
        imp = (not heading) and is_imperative(sent, L)
        proc = procedural_unit or imp
        limit = 20 if proc else 25
        if not heading or kind in ("callout.title",):
            if words > limit:
                add("E", "R5.1" if proc else "R6.3",
                    "%s sentence has %d words (max %d)" % ("procedural" if proc else "descriptive", words, limit), sent[:110])
        if sent.rstrip().endswith("?") and not heading:
            add("W", "R4.1", "question: state the fact or give the instruction", sent[:90])

    # --- pattern checks on the full text (no parentheses issues)
    for m in PASSIVE_BY.finditer(text):
        add("E", "R3.6", "passive voice with an agent: put the agent first", excerpt(text, m))
    for m in MODAL_BE_PP.finditer(text):
        add("E", "R3.4", "modal + be + participle: write the active form ('you can adjust ...') or an imperative", excerpt(text, m))
    if uid in DOCS:             # spaCy: real auxiliary + participle only ("has green limits" is not a tense)
        for t in DOCS[uid]:
            low = t.text.lower()
            if t.dep_ == "aux" and low in ("have", "has", "had") and t.head.tag_ == "VBN":
                add("E", "R3.2", "perfect tense not allowed: use simple present or simple past",
                    text[max(0, t.idx - 25):t.idx + 45])
            elif t.dep_ in ("aux", "auxpass") and low in ("is", "are", "was", "were", "am", "be", "been", "being") \
                    and t.head.tag_ == "VBG":
                add("E", "R3.2", "progressive tense not allowed: use simple present",
                    text[max(0, t.idx - 25):t.idx + 45])
    else:
        for m in PERFECT.finditer(text):
            add("E", "R3.2", "perfect tense not allowed: use simple present or simple past", excerpt(text, m))
        for m in PROGRESSIVE.finditer(text):
            add("E", "R3.2", "progressive tense not allowed: use simple present", excerpt(text, m))
    if not heading:
        if uid in DOCS:
            for head, has_agent in spacy_passives(uid):
                if not has_agent:
                    add("W", "R3.6", "passive voice ('%s'): use active voice unless the agent is unknown" % head.text,
                        text[max(0, head.idx - 40):head.idx + len(head.text) + 25])
        else:
            for m in BE_PP.finditer(text):
                if not PASSIVE_BY.search(text[m.start():m.end() + 12]):
                    add("W", "R3.6", "possible passive voice (be + participle): use active voice unless it only states a condition", excerpt(text, m))
    for m in PHRASAL.finditer(text):
        add("W", "R9.3", "phrasal verb '%s': use a single approved verb" % m.group(0), excerpt(text, m))
    for m in GR1_THAT.finditer(text):
        add("W", "GR-1", "add 'that' after '%s'" % m.group(1), excerpt(text, m))
    for m in AGAINST_LIMIT.finditer(text):
        add("E", "R9.2", "'above/below' only for physical position: use 'more than' / 'less than' for limits", excerpt(text, m))
    for m in FOLLOW_OBJ.finditer(text):
        add("E", "R9.2", "'follow' only means 'come after': use 'obey' for instructions", excerpt(text, m))
    for m in SEE_IF.finditer(text):
        add("W", "R9.2", "'see' only means 'look at with the eyes': use 'make sure' / 'find' / 'examine'", excerpt(text, m))
    for m in WEAR_GO.finditer(text):
        add("W", "R9.2", "restricted meaning ('%s'): read the dictionary entry (ste_lookup.py --entry)" % m.group(0).strip(), excerpt(text, m))
    for m in TURN_COLOR.finditer(text):
        add("E", "R9.2", "'turn' only means 'rotate': write 'changes color to …' / 'becomes …'", excerpt(text, m))
    for m in ABOUT_NUM.finditer(text):
        add("E", "R9.2", "'about' only means 'concerned with': use 'approximately' with numbers", excerpt(text, m))
    for m in re.finditer(r"\b(this|these|those)\s+(is|are|was|were|can|will|means|shows|gives|helps|causes|lets|makes|allows|explains|affects|reduces|increases|leads|ensures)\b", text, re.I):
        if not heading:
            add("W", "GR-4", "'%s' without a noun: name the thing" % m.group(1), excerpt(text, m))

    # --- vocabulary
    check_vocab(u, text, heading, kind, L, unknown_counter, findings)

    # --- multi-word nouns (dictionary-based approximation; hyphenated groups count as 1)
    stripped = mask_text(text)
    if not heading:
        run, runstart, prev_end = 0, None, 0
        NOT_NOUNISH = {"the", "a", "an", "this", "that", "these", "those", "each", "all", "more", "most", "no", "not",
                       "one", "two", "out", "up", "down", "off", "on", "in", "over", "again", "then", "thus", "also",
                       "only", "very", "too", "much", "many", "some", "other", "same", "such", "than", "if", "when"}
        for m in re.finditer(r"[A-Za-z][A-Za-z'’\-]*", stripped):
            w = m.group(0).lower()
            nounish = (L.is_tn(w) or "noun" in L.headwords.get(w, []) or "adjective" in L.headwords.get(w, [])) \
                and w not in NOT_NOUNISH \
                and "verb" not in L.headwords.get(w, []) and "preposition" not in L.headwords.get(w, []) \
                and "conjunction" not in L.headwords.get(w, []) and "pronoun" not in L.headwords.get(w, [])
            between = stripped[prev_end:m.start()]
            if run and between.strip(" "):       # punctuation (comma, colon, parenthesis ...) ends the run
                run = 0
            prev_end = m.end()
            if nounish:
                if run == 0:
                    runstart = m.start()
                run += 1
                if run == 4:
                    add("W", "R2.1", "multi-word noun of 4+ words: shorten it or use 'of/for/in'",
                        stripped[runstart:m.end() + 12].strip())
            else:
                run = 0


_UNIT_PARTS = {"cm", "m", "s", "h", "l", "kg", "g", "mg", "ml", "min", "d", "day", "hr", "hour", "week", "w", "kw", "kwh",
               "plant", "pot", "m2", "block", "slab", "shot", "event", "cycle", "tray", "room", "ppm", "ec", "mol", "mmol"}


def _mask_slash(m):
    """Unit-like slash groups (mS/cm, g/plant, N/A) are masked; word lists (cold/dark/sick) stay visible."""
    t = m.group(0)
    parts = t.split("/")
    if any(p != p.lower() for p in parts) or any(p.lower() in _UNIT_PARTS for p in parts):
        return " " * len(t)
    return t


def mask_text(text):
    s = LATIN.sub(lambda m: " " * len(m.group(0)), text)      # reported once by GR-6, not word by word
    s = QUOTED.sub(lambda m: " " * len(m.group(0)), s)
    s = NUMUNIT.sub(lambda m: " " * len(m.group(0)), s)
    s = SLASHED.sub(_mask_slash, s)
    # parentheses holding only identifiers, numbers or abbreviations are not checked
    for pm in list(re.finditer(r"\(([^()]*)\)", s)):
        if not re.findall(r"[a-z]{3,}", pm.group(1)):
            s = s[:pm.start()] + " " * (pm.end() - pm.start()) + s[pm.end():]
    return s


def classify(w, L):
    """None if the word is acceptable, else (code, detail)."""
    if w in MODAL_BAD:
        return ("modal", MODAL_BAD[w])
    if "-" in w:
        if w in L.tn_words or w in L.forms:
            return None
        bad = []
        for part in [x for x in w.split("-") if x]:
            if re.fullmatch(r"\d+|[a-z]", part) or part in ING_OK or part in NUMBER_WORDS:
                continue
            if part.endswith("ing") and len(part) > 4 and not L.approved(part):
                bad.append(part)
            elif not (L.approved(part) or L.is_tn(part) or L.is_tv(part)):
                bad.append(part)
        return ("hyphen", bad) if bad else None
    if w.endswith("ing") and len(w) > 4 and w not in ING_OK:
        return None if (w in L.tn_words or L.approved(w)) else ("ing", None)
    if L.approved(w) or L.is_tn(w) or L.is_tv(w):
        return None
    na = L.not_approved.get(w)
    if na is None:
        for v in stem_variants(w):
            if v != w and v in L.not_approved:
                na = L.not_approved[v]
                break
    return ("na", na) if na is not None else ("unknown", None)


def check_vocab(u, text, heading, kind, L, unknown_counter, findings):
    uid = u.id

    def add(sev, rule, msg, ctx=""):
        findings.append(Finding(uid, sev, rule, msg, ctx))

    stripped = mask_text(text)
    low = stripped.lower()
    covered = []
    for ph in L.tn_phrases:
        for m in re.finditer(r"(?<![\w-])" + re.escape(ph) + r"(?:s|es)?(?![\w-])", low):
            covered.append((m.start(), m.end()))
    toks = [(m.group(0), m.start(), m.end()) for m in re.finditer(r"[A-Za-z][A-Za-z'’\-]*[A-Za-z]|[A-Za-z]", stripped)]
    seen = set()
    for i, (tok, a, b) in enumerate(toks):
        if any(x <= a < y for x, y in covered):
            continue
        if CONTRACTION.fullmatch(tok):
            continue
        pre = stripped[:a].rstrip()
        initial = (pre == "" or pre[-1] in ".!?:")
        w = tok.lower().replace("’", "'")
        if w.endswith("'s"):
            w = w[:-2]
        elif w.endswith("s'"):
            w = w[:-1]
        if is_acronym(tok) or re.fullmatch(r"[A-Z]", tok) or w in ("a", "i"):
            continue
        if tok[0].isupper() and not initial and not heading:
            continue                      # proper noun or name
        if kind in ("title", "section.title", "kicker", "heading", "eyebrow") and w.endswith("ing") and len(w) > 4:
            continue                      # Rule 3.5: -ing allowed as technical noun in titles
        if len(w) == 1:
            continue                      # symbols such as d, x, n
        res = classify(w, L)
        if res is None:
            near_hyphen = (a > 0 and stripped[a - 1] == "-") or (b < len(stripped) and stripped[b] == "-")
            if (not heading) and "-" not in w and not near_hyphen:
                tctx = excerpt(text, re.search(r"(?<![A-Za-z])" + re.escape(tok) + r"(?![A-Za-z])", text))
                # Rule 1.7: a technical noun must not be used as a verb
                if L.is_tn(w) and not L.is_tv(w) and w not in L.forms and uid in DOCS \
                        and spacy_pos_at(uid, a) == "verb" and w not in seen:
                    cue = verb_context(toks, i, stripped)
                    if cue:
                        seen.add(w)
                        add("E" if cue == "strong" else "W", "R1.7",
                            "technical noun '%s' used as a verb: use an approved verb + the noun ('apply water', 'make roots')" % w, tctx)
                # Rule 1.2: an approved word used as another part of speech
                ap_all = set(L.headwords.get(w, []))
                if (ap_all == {"verb"} or ap_all == {"noun"} or w in L.homographs) and not L.is_tn(w):
                    bad = None
                    if w in L.homographs:
                        bad = L.homographs[w][1] - ap_all
                    if bad is None or not bad:
                        bad = {"verb", "noun"} - ap_all
                    guess = guess_pos(toks, i, stripped, L)
                    if guess in bad and guess in ("verb", "noun"):
                        add("W", "R1.2", "'%s' is approved only as %s, not as %s" % (w, "/".join(sorted(ap_all)), guess), tctx)
            continue
        if w in seen:
            continue
        seen.add(w)
        code, detail = res
        ctx = excerpt(text, re.search(r"(?<![A-Za-z])" + re.escape(tok) + r"(?![A-Za-z])", text))
        if code == "modal":
            add("E", "R3.2", "modal '%s' is not approved: use %s" % (w, detail), ctx)
        elif code == "ing":
            unknown_counter[w] += 1
            add("E", "R3.5", "-ing form '%s': recast with a simple verb form, or list it as a technical noun" % w, ctx)
        elif code == "hyphen":
            unknown_counter[w] += 1
            add("E", "R1.1", "hyphenated '%s': part not allowed (%s). Rewrite, or list the whole compound as a technical noun" % (w, ", ".join(detail)), ctx)
        elif code == "na":
            unknown_counter[w] += 1
            alt = ", ".join(detail["alt"][:5]) if detail["alt"] else "(no suggestion: recast)"
            add("E", "R1.1", "'%s' (%s) is not approved -> %s" % (w, "/".join(detail["pos"]), alt), ctx)
        else:
            unknown_counter[w] += 1
            add("E", "R1.1", "'%s' is not in the dictionary: use an approved word, or list it as a technical noun/verb" % w, ctx)


DOCS = {}          # unit id -> spaCy Doc (filled by prepare_docs when spaCy is used)
_CUR_UNIT = [None]


def prepare_docs(units):
    n = nlp()
    if not n:
        return False
    texts = [html_to_text(u.text) or " " for u in units]
    for u, doc in zip(units, n.pipe(texts, batch_size=64)):
        DOCS[u.id] = doc
    return True


def spacy_pos_at(uid, offset):
    doc = DOCS.get(uid)
    if doc is None:
        return None
    for t in doc:
        if t.idx == offset:
            return {"VERB": "verb", "AUX": "verb", "NOUN": "noun", "PROPN": "noun", "ADJ": "adjective",
                    "ADV": "adverb"}.get(t.pos_)
    return None


def spacy_passives(uid):
    """[(text_of_verb, has_agent)] for true passive constructions in the unit."""
    doc = DOCS.get(uid)
    out = []
    if doc is None:
        return out
    for t in doc:
        if t.dep_ in ("auxpass", "nsubjpass") and t.head.pos_ == "VERB":
            head = t.head
            if all(o[0] is not head for o in out):
                has_agent = any(c.dep_ == "agent" for c in head.children)
                out.append((head, has_agent))
    return out


_VERB_CUES = {"to", "will", "can", "must", "cannot", "not", "do", "does", "did", "you", "we", "they"}
_DET_NEXT = {"the", "a", "an", "each", "all", "your", "this", "these", "those", "any", "every", "both", "it", "them"}


def verb_context(toks, i, text):
    """'strong' when the word follows to/will/can/must/not/do/you/we/they; 'weak' for an imperative start."""
    a = toks[i][1]
    prev = toks[i - 1][0].lower() if i > 0 else ""
    nxt = toks[i + 1][0].lower() if i + 1 < len(toks) else ""
    pre = text[:a].rstrip()
    if prev in _VERB_CUES and (not pre or pre[-1] not in ".,;:()"):
        return "strong"
    if (pre == "" or pre[-1] in ".!?:") and nxt in _DET_NEXT:
        return "weak"
    return None


def guess_pos(toks, i, text, L):
    """POS guess for a word: 'verb' / 'noun' / '?'.  The context heuristic decides; spaCy can veto it."""
    h = _heuristic_pos(toks, i, text)
    sp = spacy_pos_at(_CUR_UNIT[0], toks[i][1]) if _CUR_UNIT[0] else None
    if h in ("verb", "noun") and sp in ("verb", "noun") and sp != h:
        return "?"
    return h


def _heuristic_pos(toks, i, text):
    w, a, b = toks[i]
    prev = toks[i - 1][0].lower() if i > 0 else ""
    nxt = toks[i + 1][0].lower() if i + 1 < len(toks) else ""
    pre = text[:a].rstrip()
    if prev in ("to", "will", "can", "must", "cannot", "not", "do", "does", "did", "you", "we", "they"):
        return "verb"
    if pre == "" or pre[-1] in ".!?:,":
        if nxt in ("the", "a", "an", "all", "each", "your", "this", "that", "these", "those", "it", "them", "any", "every", "both"):
            return "verb"
    if prev in ("the", "a", "an", "this", "that", "these", "those", "each", "every", "no", "of", "for", "in", "on", "by", "with", "after", "before", "during", "your", "its", "their", "our"):
        return "noun"
    return "?"


# --------------------------------------------------------------------------- inputs
def units_from_module(modname):
    import importlib
    sys.path.insert(0, os.path.dirname(HERE))
    mod = importlib.import_module(modname)
    from bs4 import BeautifulSoup
    units, n = [], 0

    def add(kind, ctx, text):
        nonlocal n
        if text and text.strip():
            n += 1
            units.append(Unit("U%04d" % n, kind, ctx, text.strip()))
    add("title", "TITLE", getattr(mod, "TITLE", ""))
    add("eyebrow", "EYEBROW", getattr(mod, "EYEBROW", ""))
    add("p", "SUB", getattr(mod, "SUB", ""))
    for it in getattr(mod, "META", []) or []:
        add("meta", "META", it[1] if isinstance(it, (tuple, list)) and len(it) > 1 else str(it))
    for sec in getattr(mod, "SECTIONS", []):
        sid = sec.get("id", "?")
        add("kicker", "s:%s" % sid, sec.get("kicker", ""))
        add("section.title", "s:%s" % sid, sec.get("title", ""))
        for blk in sec.get("blocks", []):
            units.extend(_block_units(blk, sid, BeautifulSoup))
    # renumber
    for i, u in enumerate(units, 1):
        u.id = "U%04d" % i
    return units


_CONTAINERS = {"p": "p", "li": "li", "td": "cell", "th": "th", "caption": "caption", "figcaption": "caption",
               "h1": "heading", "h2": "heading", "h3": "heading", "h4": "heading", "h5": "heading"}
_CLASS_KIND = {"ctitle": "callout.title", "defn-t": "defterm.term", "defn-b": "defterm.body", "step-t": "step.title",
               "step-b": "step.body", "card-title": "card.title", "card-body": "card.body", "card-tag": "tag",
               "kv-k": "kv.key", "kv-v": "kv.val", "stagetitle": "stage.title", "stagedur": "stage.dur",
               "stagenum": "stage.num", "stagecard-b": "card.body", "chip": "tag", "fignum": "figure.label",
               "kicker": "kicker"}


def _block_units(blk, sid, BS):
    soup = BS(blk, "html.parser")
    for s in soup.find_all("svg"):
        s.decompose()
    for img in soup.find_all("img"):
        img.decompose()
    out = []

    def kind_of(el):
        for c in el.get("class", []) or []:
            if c in _CLASS_KIND:
                return _CLASS_KIND[c]
        return _CONTAINERS.get(el.name)

    def own_text(el):
        parts = []
        for ch in el.children:
            if getattr(ch, "name", None) is None:
                parts.append(str(ch))
            else:
                if kind_of(ch) and ch.name not in ("sup", "em", "strong", "span", "a", "b", "i", "code", "abbr", "sub", "mark", "small"):
                    continue
                if kind_of(ch) in ("tag",) or (ch.get("class") and any(c in _CLASS_KIND for c in ch.get("class"))):
                    continue
                parts.append(own_text(ch) if ch.name not in ("sup",) else str(ch))
        return "".join(parts)

    callout_kind = ""
    for el in soup.find_all(True):
        k = kind_of(el)
        if not k:
            continue
        if "callout" in (el.get("class") or []):
            continue
        txt = own_text(el)
        if not txt.strip():
            continue
        ctx = "s:%s" % sid
        parent_call = el.find_parent("div", class_="callout")
        if parent_call:
            cls = parent_call.get("class", [])
            ck = next((c for c in cls if c in ("warn", "danger", "note", "tip", "key", "evidence")), "")
            ctx += " kind=%s" % ck
        if el.find_parent("ol", class_="steps") and k == "li":
            continue
        if k == "li" and el.find_parent("ol") is not None and not el.find_parent("ol", class_="steps"):
            k = "li"
        out.append(Unit("U0", k, ctx, txt))
    return out


def units_from_markdown(path):
    text = open(path, encoding="utf-8").read()
    text = re.sub(r"^---.*?---\s*", "", text, flags=re.S)
    m_ref = re.search(r"^#{1,3}\s*References\b", text, flags=re.M)
    if m_ref:
        text = text[:m_ref.start()]          # bibliographic text is quoted material, not STE prose
    units, n = [], 0
    for para in re.split(r"\n\s*\n", text):
        p = para.strip()
        if not p:
            continue
        if p.startswith("```"):
            continue
        for line in p.splitlines():
            ln = line.strip()
            if not ln or ln.startswith("|---") or ln.startswith("```"):
                continue
            kind = "p"
            if ln.startswith("#"):
                kind = "heading"
                ln = ln.lstrip("# ").strip()
            elif ln.startswith(("- ", "* ")) or re.match(r"^\d+[.)] ", ln):
                kind = "li"
                ln = re.sub(r"^(?:[-*]|\d+[.)])\s+", "", ln)
            elif ln.startswith("|"):
                for cell in [c.strip() for c in ln.strip("|").split("|")]:
                    if cell:
                        n += 1
                        units.append(Unit("U%04d" % n, "cell", "md", re.sub(r"[*_`]", "", cell)))
                continue
            ln = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", ln)
            ln = re.sub(r"\[\d+(?:[,–-]\s?\d+)*\]", "", ln)
            ln = re.sub(r"[*_`]", "", ln)
            n += 1
            units.append(Unit("U%04d" % n, kind, "md", ln))
    return units


# --------------------------------------------------------------------------- driver
def _slug_of_module(modname):
    """SLUG of a paper module (None if it cannot be imported)."""
    try:
        import importlib
        sys.path.insert(0, os.path.dirname(HERE))
        return getattr(importlib.import_module(modname), "SLUG", None)
    except Exception:
        return None


def run(units, args):
    L = lex(getattr(args, "slug", None))
    findings, unknown = [], Counter()
    DOCS.clear()
    use_spacy = (not args.no_spacy) and prepare_docs(units)
    for u in units:
        _CUR_UNIT[0] = u.id if use_spacy else None
        check_unit(u, L, use_spacy, unknown, findings)
    _CUR_UNIT[0] = None
    return findings, unknown


def report(units, findings, unknown, args):
    by_unit = OrderedDict()
    for f in findings:
        if f.sev == "W" and args.level == "E":
            continue
        by_unit.setdefault(f.unit, []).append(f)
    umap = {u.id: u for u in units}
    counts = Counter((f.sev, f.rule) for f in findings)
    nE = sum(1 for f in findings if f.sev == "E")
    nW = sum(1 for f in findings if f.sev == "W")
    if args.json:
        print(json.dumps({"errors": nE, "warnings": nW, "findings": [f.asdict() for f in findings]}, ensure_ascii=False))
        return nE
    printed = 0
    if not args.summary:
        for uid, fl in by_unit.items():
            u = umap.get(uid)
            head = "%s [%s] %s" % (uid, u.kind if u else "?", (u.ctx if u else "")[:40])
            print(head)
            print("    | " + (html_to_text(u.text)[:170] if u else ""))
            for f in fl:
                print("    %s %-6s %s" % (f.sev, f.rule, f.msg))
                if f.ctx:
                    print("        > " + f.ctx.replace("\n", " ")[:150])
                printed += 1
            if printed >= args.max:
                print("... stopped after %d findings (use --max)" % args.max)
                break
    print("\n== %d units | %d errors | %d warnings" % (len(units), nE, nW))
    if counts:
        print("   " + "  ".join("%s:%s=%d" % (s, r, c) for (s, r), c in sorted(counts.items())))
    if args.words and unknown:
        print("\nDistinct flagged words (%d):" % len(unknown))
        print("  " + ", ".join("%s(%d)" % (w, c) for w, c in unknown.most_common()))
    return nE


def add_list(kind, slug, words):
    path = os.path.join(DATA, "%s_%s.txt" % (kind, slug))
    existing = set(_read_list(path))
    new = [w.strip().lower() for w in words if w.strip() and w.strip().lower() not in existing]
    os.makedirs(DATA, exist_ok=True)
    with open(path, "a", encoding="utf-8") as fh:
        for w in new:
            fh.write(w + "\n")
    print("%s: added %d (%s)" % (os.path.basename(path), len(new), ", ".join(new)))


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--units")
    ap.add_argument("--module")
    ap.add_argument("--md")
    ap.add_argument("--text")
    ap.add_argument("--stdin", action="store_true")
    ap.add_argument("--level", default="W", choices=["E", "W"])
    ap.add_argument("--max", type=int, default=200)
    ap.add_argument("--summary", action="store_true")
    ap.add_argument("--words", action="store_true")
    ap.add_argument("--no-spacy", action="store_true")
    ap.add_argument("--slug", help="use only core + this paper's own TN/TV lists (default: detected from the input)")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--add-tn", nargs="+", metavar=("SLUG", "WORD"))
    ap.add_argument("--add-tv", nargs="+", metavar=("SLUG", "WORD"))
    args = ap.parse_args(argv)
    if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
        sys.stdout.reconfigure(encoding="utf-8")
    if args.add_tn:
        return add_list("tn", args.add_tn[0], args.add_tn[1:])
    if args.add_tv:
        return add_list("tv", args.add_tv[0], args.add_tv[1:])
    args.slug = getattr(args, "slug", None)
    if args.units:
        header, units = read_units(args.units)
        m = re.search(r"slug:\s*([\w\-]+)", " ".join(header)) or re.search(r"file:\s*(?:.*[/\\])?([\w\-]+)\.html", " ".join(header))
        if m:
            args.slug = args.slug or m.group(1)
        elif not args.slug:       # path .../work/<module>/units.txt: look the slug up in the paper module
            args.slug = _slug_of_module(os.path.basename(os.path.dirname(os.path.abspath(args.units))))
    elif args.module:
        units = units_from_module(args.module)
        args.slug = args.slug or _slug_of_module(args.module)
    elif args.md:
        units = units_from_markdown(args.md)
        args.slug = args.slug or os.path.splitext(os.path.basename(args.md))[0]
    elif args.text:
        units = [Unit("U0001", "p", "text", args.text)]
    elif args.stdin:
        sys.stdin.reconfigure(encoding="utf-8")
        data = sys.stdin.read()
        units = [Unit("U%04d" % i, "p", "stdin", p.strip()) for i, p in enumerate(re.split(r"\n\s*\n", data), 1) if p.strip()]
    else:
        ap.print_help()
        return 2
    findings, unknown = run(units, args)
    nE = report(units, findings, unknown, args)
    return 1 if nE else 0


if __name__ == "__main__":
    sys.exit(main())
