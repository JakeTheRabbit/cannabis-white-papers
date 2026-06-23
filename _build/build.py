# -*- coding: utf-8 -*-
"""Build orchestrator. Emits the static site to the repo root.
Run:  cd /c/Github/white-papers/_build && python build.py
"""
import os, re, json, sys, html as _h
sys.path.insert(0, os.path.dirname(__file__))

import theme, app_js, shell
from components import icon, esc, photo, card, grid, term_gallery, photo_sequence, diagram
import images as IMG
try:
    import diagrams as DG
    _DIAGRAMS = DG.DIAGRAMS
except Exception as _de:
    _DIAGRAMS = {}
    print("diagrams registry not loaded:", repr(_de))
import links as LINKS
import data.nav as NAV
import data.glossary as GL
import data.refs as REFS
import importlib

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ASSETS = os.path.join(ROOT, "assets")

try:
    EMBED = json.load(open(os.path.join(os.path.dirname(__file__), "_gen", "embed_map.json"), encoding="utf-8"))
except Exception:
    EMBED = {}

# Papers in display order. Loaded defensively: a broken module is reported,
# not fatal, and only successfully-loaded papers go live in the nav.
PAPER_MODULES = [
    "paper_tissue_culture", "paper_coco_crop_steering", "paper_grow_room_systems",
    "paper_airflow_design", "paper_mould_risk",
    "paper_seeds_germination", "paper_lighting_fundamentals", "paper_substrates_overview",
    "paper_water_quality", "paper_ph_management", "paper_nutrient_deficiencies",
    "paper_flowering_stages", "paper_pest_id",
    "paper_root_zone_teros12", "paper_smart_watering_vrwe", "paper_signal_and_noise",
    "paper_closed_loop", "paper_plant_state_dashboard",
    "paper_f2_crop_steering", "paper_irrigation_manual",
    "paper_cloning", "paper_nutrient_mixing_athena", "paper_light_acclimation",
    "paper_defoliation_training", "paper_ipm_sop", "paper_harvest_dry_trim_cure",
    "paper_gmp_hash_lab", "paper_facility_3d",
    "paper_rockwool_crop_steering", "paper_daily_checks", "paper_pppe",
]
PAPERS, PAPER_ERRORS = [], []
for _m in PAPER_MODULES:
    try:
        PAPERS.append(importlib.import_module(_m))
    except Exception as _e:
        PAPER_ERRORS.append((_m, repr(_e)))

# Nav status reflects reality: live iff the module built.
_LIVE = {m.SLUG for m in PAPERS}
for _it in NAV.all_items():
    _it["status"] = "live" if _it["slug"] in _LIVE else "soon"

def w(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    return len(content)

def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

# ---------------------------------------------------------------- auto-interlinking
_XRE = [(re.compile(r'(?<![\w-])(' + re.escape(p) + r')(?![\w-])', re.I), slug)
        for p, slug in LINKS.phrase_list()]
_S0, _S1 = "", ""

def autolink(html, current_slug, linked):
    """Link the first mention of each concept phrase to its paper. Skips the page's own
    slug, anything already linked on the page, and text inside tags/links/svg/code."""
    spans = []
    def stash(m):
        spans.append(m.group(0)); return f"{_S0}{len(spans)-1}{_S1}"
    masked = re.sub(r'<a\b[^>]*>.*?</a>|<svg\b[^>]*>.*?</svg>|<code\b[^>]*>.*?</code>|<[^>]+>',
                    stash, html, flags=re.S)
    for rx, slug in _XRE:
        if slug == current_slug or slug in linked:
            continue
        done = [False]
        def repl(m):
            if done[0]:
                return m.group(0)
            done[0] = True; linked.add(slug)
            spans.append(f'<a class="xref" href="{slug}.html">{m.group(1)}</a>')
            return f"{_S0}{len(spans)-1}{_S1}"
        masked = rx.sub(repl, masked, count=1)
    for _ in range(3):
        masked, n = re.subn(_S0 + r'(\d+)' + _S1, lambda m: spans[int(m.group(1))], masked)
        if not n:
            break
    return masked

# ---------------------------------------------------------------- paper page
def render_paper(mod):
    secs = mod.SECTIONS
    # embed any generated example images into their target sections (file-gated)
    for im in IMG.by_slug().get(mod.SLUG, []):
        fn = f"{im['slug']}-{im['n']}.jpg"
        if os.path.exists(os.path.join(ASSETS, "img", fn)) and secs:
            si = max(0, min(im["sec"], len(secs) - 1))
            secs[si]["blocks"].append(
                photo(f"assets/img/{fn}", im["caption"], im.get("alt", ""),
                      IMG.MODEL_LABEL.get(im["model"], "")))
    # embed term-image gallery + progression sequences (file-gated)
    em = EMBED.get(mod.SLUG, {})
    _ex = lambda src: os.path.exists(os.path.join(ROOT, src))
    gal = [(t, s) for t, s in em.get("gallery", []) if _ex(s)]
    if gal and secs:
        ki = next((i for i, s in enumerate(secs)
                   if "term" in s["id"].lower() or "vocab" in s["id"].lower()
                   or any(w in s["title"].lower() for w in ("term", "word", "vocab"))),
                  1 if len(secs) > 1 else 0)
        secs[ki]["blocks"].append(term_gallery(gal, "Nano Banana 2"))
    for seq in em.get("sequences", []):
        frames = [(l, s) for l, s in seq["frames"] if _ex(s)]
        if not frames:
            continue
        idx = next((i for i, s in enumerate(secs) if s["id"] == seq.get("section_id")), None)
        if idx is None:
            idx = min(2, len(secs) - 1)
        secs[idx]["blocks"].append(photo_sequence(seq["title"], frames, seq["caption"], "Nano Banana 2"))
    # embed bespoke SVG concept diagrams (registry; placed by section hint, fallback to terms section)
    def _find_sec(hint):
        if hint:
            h = hint.lower()
            i = next((i for i, s in enumerate(secs) if h in s["id"].lower() or h in s["title"].lower()), None)
            if i is not None:
                return i
        i = next((i for i, s in enumerate(secs)
                  if "term" in s["id"].lower() or "vocab" in s["id"].lower()
                  or any(w in s["title"].lower() for w in ("term", "word", "vocab"))), None)
        return i if i is not None else (1 if len(secs) > 1 else 0)
    for entry in _DIAGRAMS.get(mod.SLUG, []):
        hint, fn, cap = entry
        try:
            svg = fn()
        except Exception as _xe:
            print(f"  diagram fail [{mod.SLUG}] {cap[:40]}: {_xe!r}")
            continue
        if secs:
            secs[_find_sec(hint)]["blocks"].append(diagram(svg, cap))
    # hero
    pills = []
    for i, (ic, txt) in enumerate(mod.META):
        cls = "pill solid" if i == 0 else "pill"
        pills.append(f'<span class="{cls}">{icon(ic,14)}{esc(txt)}</span>')
    hero = (
        f'<div class="crumb"><a href="index.html">Home</a><span class="sep">{icon("chevright",12)}</span>'
        f'<span>{esc(mod.EYEBROW.split("·")[0].strip())}</span><span class="sep">{icon("chevright",12)}</span>'
        f'<span>{esc(mod.TITLE)}</span></div>'
        f'<div class="eyebrow">{esc(mod.EYEBROW)}</div>'
        f'<h1 class="title">{esc(mod.TITLE)}</h1>'
        f'<p class="sub">{esc(mod.SUB)}</p>'
        f'<div class="metarow">{"".join(pills)}</div>'
        f'<div class="divider"></div>'
    )
    # index card
    toc_items = ""
    for i, s in enumerate(secs, 1):
        toc_items += f'<a href="#{s["id"]}"><span class="n">{i:02d}</span> {esc(s["title"])}</a>'
    index_card = (f'<div class="toc-card"><div class="kicker">{icon("list",14)} In this guide</div>'
                  f'<div class="toc">{toc_items}</div></div>')
    # sections (with auto-interlinking across the page)
    body_secs = []
    linked = set()
    for s in secs:
        blocks = autolink("".join(s["blocks"]), mod.SLUG, linked)
        body_secs.append(
            f'<section class="sec" id="{s["id"]}"><div class="sec-kicker">{esc(s.get("kicker",""))}</div>'
            f'<h2>{esc(s["title"])}</h2>{blocks}</section>')
    # related
    rel_cards = []
    for slug in getattr(mod, "RELATED", []):
        it = NAV.find(slug)
        if not it:
            continue
        live = it["status"] == "live"
        href = f'{slug}.html' if live else "papers.html"
        rel_cards.append(
            f'<a class="relcard" href="{href}">{icon(it["icon"],20)}'
            f'<div class="tt">{esc(it["title"])}</div><div class="dd">{esc(it["short"])}</div></a>')
    related = (f'<div class="kicker" style="margin-top:46px">{icon("arrowright",14)} Related papers</div>'
               f'<div class="rel">{"".join(rel_cards)}</div>') if rel_cards else ""
    # references
    ref_lis = ""
    for rid in mod.REF_IDS:
        r = REFS.REFS.get(rid)
        if not r:
            continue
        npc = "" if r.get("peer") else " <span style='color:var(--faint)'>(manufacturer source, not peer-reviewed)</span>"
        link = f' <a href="{r["url"]}" target="_blank" rel="noopener">{r["url"]}</a>' if r.get("url") else ""
        cls = "" if r.get("peer") else " class='np'"
        ref_lis += f'<li id="ref-{rid}"{cls}>{r["cite"]}{npc}{link}</li>'
    refs = (f'<div class="refs"><h3>References</h3><ol>{ref_lis}</ol>'
            f'<p class="foot">Citations marked in-text as [n] map to this list. Peer-reviewed sources '
            f'except where noted. Cannabis tissue culture is strongly genotype-dependent, verify '
            f'dilutions, hormone doses and local regulations against the primary sources before relying on them.</p></div>')

    body = hero + index_card + "".join(body_secs) + related + refs
    rail_toc = [(s["id"], s["title"]) for s in secs]
    return shell.page(mod.SLUG, mod.TITLE, body, desc=mod.SUB, rail_toc=rail_toc, mobile_active="papers")

# ---------------------------------------------------------------- track grid
def track_grid(only_live=False):
    out = []
    for g in NAV.GROUPS:
        items = g["items"]
        live_ct = sum(1 for it in items if it["status"] == "live")
        out.append(f'<div class="track"><div class="track-h"><h2>{esc(g["group"])}</h2>'
                   f'<span class="ct">{live_ct} of {len(items)} available</span></div><div class="pgrid">')
        for it in items:
            live = it["status"] == "live"
            soon = "" if live else '<span class="soon-tag">soon</span>'
            cls = "pcard" if live else "pcard soon"
            inner = (f'<div class="pic">{icon(it["icon"],20)}</div>'
                     f'<div><div class="pt">{esc(it["title"])}</div>'
                     f'<div class="ps">{esc(it["short"])}</div></div>{soon}')
            if live:
                out.append(f'<a class="{cls}" href="{it["slug"]}.html">{inner}</a>')
            else:
                out.append(f'<div class="{cls}">{inner}</div>')
        out.append('</div></div>')
    return "".join(out)

# ---------------------------------------------------------------- landing
def render_index():
    n_total = len(NAV.all_items())
    n_live = sum(1 for it in NAV.all_items() if it["status"] == "live")
    hero = (
        '<div class="hero-land"><div class="eyebrow">A field guide to growing, from zero</div>'
        '<h1>The Cannabis White Papers</h1>'
        '<p class="sub">Cultivation science from the journals, rewritten so a first-time grower can '
        'actually follow it. Every paper defines its terms, shows its working in diagrams and tables, '
        'and cites its sources.</p>'
        f'<div class="hero-stats">'
        f'<div class="s"><b>{n_total}</b><span>white papers</span></div>'
        f'<div class="s"><b>{n_live}</b><span>available now</span></div>'
        f'<div class="s"><b>100%</b><span>cited &amp; diagrammed</span></div></div></div>'
    )
    intro = (
        '<div class="track" style="margin-top:10px"><div class="track-h"><h2>What these are</h2>'
        '<span class="ct">and the point of them</span></div>'
        '<p style="max-width:780px;color:var(--muted);font-size:17px;line-height:1.6;margin:0 0 16px">'
        'Each one is a white paper: a deep, single-topic grow guide written from absolute zero, '
        'with every term defined, every claim cited to peer-reviewed research, and the working shown '
        'in diagrams, charts and tables. Together they cover a whole grow, ordered below by the stage '
        'you use them in: propagation, vegetative growth, flower, then harvest through to cure, plus '
        'the systems that run across all of them. Follow the <a href="curriculum.html">grow order</a>, '
        'jump to a stage below, or press <strong>Ctrl&nbsp;K</strong> to search anything.</p>'
        + grid([
            card("Deep, not shallow", "One topic per paper, taken from beginner to genuinely useful. No filler, no hype.", tag="What it is"),
            card("Cited and honest", "Every factual claim links to peer-reviewed research. Where the science is uncertain, it says so.", tag="Why trust it"),
            card("Ordered by the grow", "Grouped by task: propagation, veg, flower, harvest, and the systems that span every stage.", tag="How to use it"),
        ], cols=3) + '</div>')
    body = hero + intro + render_directory()
    return shell.page("index", "Home", body, desc="Peer-reviewed cannabis cultivation white papers, by grow stage.", wide=True, mobile_active="index")

def render_directory():
    """Compact, filterable one-screen directory: stage pills + dense card grid."""
    n = len(NAV.all_items())
    pills = [f'<button class="fpill on" data-filter="all">All <span>{n}</span></button>']
    cards = []
    for g in NAV.GROUPS:
        gs = slugify(g["group"])
        pills.append(f'<button class="fpill" data-filter="{gs}">{esc(g["group"])} <span>{len(g["items"])}</span></button>')
        for it in g["items"]:
            cards.append(
                f'<a class="pcard sm" data-group="{gs}" href="{it["slug"]}.html">'
                f'<div class="pic">{icon(it["icon"],17)}</div>'
                f'<div><div class="pt">{esc(it["title"])}</div>'
                f'<div class="ps">{esc(it["short"])}</div></div></a>')
    return (f'<div class="filterbar" id="filterbar">{"".join(pills)}</div>'
            f'<div class="pgrid compact" id="paperdir">{"".join(cards)}</div>'
            f'<div class="dir-empty" id="dirEmpty" style="display:none">Nothing in this stage yet.</div>')

def render_papers():
    head = ('<div class="eyebrow">Library</div><h1 class="title">All papers</h1>'
            '<p class="sub">Every white paper in the collection, grouped by track. Greyed cards are '
            'in production and coming soon.</p><div class="divider"></div>')
    body = head + track_grid()
    return shell.page("papers", "All papers", body, desc="The full white-paper library.", wide=True, mobile_active="papers")

# ---------------------------------------------------------------- glossary
def render_glossary():
    head = ('<div class="eyebrow">Reference</div><h1 class="title">Glossary</h1>'
            '<p class="sub">Every bit of jargon used across the papers, in plain English. '
            'No prior knowledge assumed.</p><div class="divider"></div>')
    buckets = GL.by_letter()
    parts = [head]
    for letter in sorted(buckets):
        parts.append(f'<div class="gl-letter">{letter}</div>')
        for g in buckets[letter]:
            tags = "".join(f'<span class="chip">{esc(t)}</span>' for t in g.get("tags", []))
            parts.append(
                f'<div class="gl-item" id="gl-{slugify(g["term"])}">'
                f'<div class="gl-term">{g["term"]}</div>'
                f'<div class="gl-defn">{g["defn"]}</div>'
                f'<div class="gl-tags">{tags}</div></div>')
    body = "".join(parts)
    return shell.page("glossary", "Glossary", body, desc="Plain-English definitions of every grow term used in the papers.", wide=True, mobile_active="glossary")

# ---------------------------------------------------------------- curriculum tree
CURRICULUM = [
 ("1 · Propagation", "Start the plants.", [
   ("Seeds, germination & seedlings", "seeds-germination"), ("Cloning", "cloning"),
   ("Tissue culture: clean genetics", "tissue-culture"),
   ("Mother / stock-plant management", None), ("Transplanting & potting up", None)]),
 ("2 · Vegetative growth", "Build a big, healthy plant.", [
   ("Light acclimation", "light-acclimation"), ("Defoliation & plant training", "defoliation-training"),
   ("Vegetative management & timing", None)]),
 ("3 · Flowering", "Steer the plant to yield and quality.", [
   ("The flower cycle, week by week", "flowering-stages"),
   ("Precision coco cultivation: crop steering", "coco-crop-steering"),
   ("Rockwool crop steering: drybacks & saturation", "rockwool-crop-steering"),
   ("Ripening, flush & harvest timing", None)]),
 ("4 · Harvest, dry, trim & cure", "Turn flower into finished product.", [
   ("Harvest, dry, trim & cure", "harvest-dry-trim-cure"), ("GMP hash manufacturing", "gmp-hash-lab"),
   ("Extraction & concentrates", None), ("Lab testing, potency & COAs", None)]),
 ("Runs every stage · Environment & climate", "The conditions the plant lives in.", [
   ("The grow room: a systems guide", "grow-room-systems"), ("Lighting: spectrum, PPFD & DLI", "lighting-fundamentals"),
   ("Airflow design", "airflow-design"), ("Temperature, humidity & VPD", None),
   ("CO2 enrichment", None), ("HVAC, cooling & dehumidification", None)]),
 ("Runs every stage · Water, substrate & feed", "What the roots get.", [
   ("Substrates compared: coco, rockwool, soil, hydro", "substrates-overview"),
   ("Source water, RO & alkalinity", "water-quality"), ("pH: hold it steady", "ph-management"),
   ("Mixing an Athena Pro Line stock tank", "nutrient-mixing-athena"),
   ("Nutrient deficiency & toxicity diagnosis", "nutrient-deficiencies")]),
 ("Runs every stage · Plant health", "Keep them clean.", [
   ("Mould risk: bud rot & PM", "mould-risk"), ("IPM: a working SOP", "ipm-sop"),
   ("Pest identification & control", "pest-id"), ("PPE & biosecurity (PPPE)", "pppe"),
   ("Root diseases: pythium & fusarium", None)]),
 ("Runs every stage · Precision & automation", "Dial it in and let it run.", [
   ("Root-zone state (TEROS-12)", "root-zone-teros12"), ("Signal & noise", "signal-and-noise"),
   ("Smart watering (VRWE)", "smart-watering-vrwe"), ("The closed loop", "closed-loop"),
   ("Plant-state dashboard", "plant-state-dashboard"), ("F2 crop steering", "f2-crop-steering"),
   ("Irrigation manual", "irrigation-manual")]),
 ("The operation · Facility & quality", "Run it as a business.", [
   ("Designing a facility in 3D", "facility-3d"),
   ("Daily checks: the self-completing round", "daily-checks"),
   ("Compliance, licensing & track-and-trace", None),
   ("Energy, utilities & sustainability", None), ("Yield per watt & unit economics", None)]),
 ("Reference · Know the plant", "Background worth having.", [
   ("Cannabis plant biology & life cycle", None), ("Cannabinoids & terpenes", None),
   ("Genetics, seeds & phenotype hunting", None)]),
]

def render_curriculum():
    total = sum(len(items) for _, _, items in CURRICULUM)
    live = sum(1 for _, _, items in CURRICULUM for _, slug in items if slug in _LIVE)
    head = (
        '<div class="eyebrow">The grow, in order</div>'
        '<h1 class="title">Start here: the whole grow, stage by stage</h1>'
        '<p class="sub">Every paper, grouped by where it sits in a grow: propagation, vegetative '
        'growth, flowering, then harvest through to cure, plus the systems that run across every '
        'stage. Green dots are published now. Greyed rows are written and on the way.</p>'
        f'<div class="hero-stats" style="justify-content:flex-start;gap:28px;margin:22px 0 0">'
        f'<div class="s"><b>{live}</b><span>published</span></div>'
        f'<div class="s"><b>{total}</b><span>in the full guide</span></div>'
        f'<div class="s"><b>{round(live/total*100)}%</b><span>complete</span></div></div>'
        '<div class="divider"></div>')
    parts = [head]
    for title, desc, items in CURRICULUM:
        rows = []
        for label, slug in items:
            if slug in _LIVE:
                rows.append(f'<a class="curitem" href="{slug}.html"><span class="dot"></span>'
                            f'<span>{esc(label)}</span><span class="arr">{icon("arrowright",15)}</span></a>')
            else:
                rows.append(f'<div class="curitem soon"><span class="dot"></span>'
                            f'<span>{esc(label)}</span><span class="soon-tag">soon</span></div>')
        parts.append(f'<div class="curtier"><div class="curtier-h"><h3>{esc(title)}</h3>'
                     f'<span class="d">{esc(desc)}</span></div><div class="curlist">{"".join(rows)}</div></div>')
    return shell.page("curriculum", "Start here", "".join(parts),
                      desc="The complete cannabis cultivation guide, ordered as a learning path.",
                      wide=True, mobile_active="curriculum")

# ---------------------------------------------------------------- search index
def _plain(html_str):
    t = re.sub(r"<[^>]+>", " ", html_str)
    return re.sub(r"\s+", " ", _h.unescape(t)).strip()

# Concept -> related terms. Powers semantic-lite query expansion (search "bugs" finds IPM).
SEARCH_SYN = {
    "feed": ["nutrient", "ec", "fertiliser", "dose", "ppm", "feeding"],
    "feeding": ["nutrient", "ec", "feed", "dose"],
    "nutrients": ["nutrient", "ec", "feed", "ppm", "deficiency", "athena"],
    "water": ["irrigation", "dryback", "vwc", "drip", "watering", "moisture"],
    "watering": ["irrigation", "dryback", "vwc", "drip", "water"],
    "bugs": ["pest", "mites", "thrips", "ipm", "scouting", "insect"],
    "pests": ["mites", "thrips", "fungus gnats", "ipm", "scouting", "biocontrol"],
    "mold": ["mould", "botrytis", "bud rot", "powdery mildew", "fungus"],
    "mould": ["botrytis", "bud rot", "powdery mildew", "fungus"],
    "rot": ["botrytis", "bud rot", "mould"],
    "light": ["ppfd", "dli", "par", "spectrum", "bleaching", "acclimation", "lighting"],
    "lighting": ["ppfd", "dli", "par", "light"],
    "humidity": ["vpd", "rh", "climate", "dehumidifier"],
    "climate": ["vpd", "temperature", "humidity", "co2"],
    "clean": ["tissue culture", "meristem", "viroid", "sterile", "disease-free"],
    "clone": ["cloning", "cutting", "propagation", "rooting"],
    "clones": ["cloning", "cutting", "propagation"],
    "cutting": ["cloning", "propagation"],
    "dry": ["drying", "cure", "harvest", "trichome"],
    "cure": ["curing", "drying", "harvest", "water activity"],
    "harvest": ["trichome", "drying", "curing", "ripening"],
    "sensor": ["teros", "capacitance", "vwc", "ec", "probe", "root-zone"],
    "steer": ["crop steering", "dryback", "generative", "vegetative"],
    "steering": ["crop steering", "dryback", "vwc", "ec"],
    "yield": ["defoliation", "training", "scrog", "light", "crop steering"],
    "train": ["defoliation", "training", "lollipop", "scrog", "topping"],
    "soil": ["substrate", "coco", "rockwool", "media"],
    "substrate": ["coco", "rockwool", "media", "root zone"],
    "automation": ["closed loop", "controller", "home assistant", "f2", "vrwe"],
    "ph": ["alkalinity", "acidity", "nutrient"],
    "extract": ["hash", "rosin", "solventless", "concentrate", "gmp"],
    "testing": ["coa", "potency", "contaminant", "lab"],
    "compliance": ["gmp", "quality", "sop", "licensing", "traceability"],
}

def build_search_index():
    idx = []
    pages = list(NAV.TOP) + [{"slug": "curriculum", "title": "Curriculum", "icon": "list"}]
    for t in pages:
        url = "index.html" if t["slug"] == "index" else f'{t["slug"]}.html'
        idx.append({"type": "page", "title": t["title"], "url": url, "text": "", "kw": ""})
    for mod in PAPERS:
        kw = " ".join(LINKS.LINK_PHRASES.get(mod.SLUG, []))
        idx.append({"type": "paper", "title": mod.TITLE, "url": f"{mod.SLUG}.html",
                    "text": _plain(mod.SUB), "kw": kw, "paper": mod.TITLE})
        for s in mod.SECTIONS:
            txt = _plain("".join(s["blocks"]))[:1200]
            idx.append({"type": "section", "title": s["title"],
                        "url": f'{mod.SLUG}.html#{s["id"]}', "text": txt,
                        "kw": kw, "paper": mod.TITLE})
    live_slugs = {m.SLUG for m in PAPERS}
    for it in NAV.all_items():
        if it["slug"] in live_slugs:
            continue
        idx.append({"type": "coming soon", "title": it["title"], "url": "papers.html",
                    "text": it["short"], "kw": ""})
    for g in GL.GLOSSARY:
        idx.append({"type": "term", "title": g["term"],
                    "url": f'glossary.html#gl-{slugify(g["term"])}',
                    "text": _plain(g["defn"]), "kw": " ".join(g.get("tags", []))})
    return ("window.SEARCH_INDEX=" + json.dumps(idx, ensure_ascii=False) + ";\n"
            "window.SEARCH_SYN=" + json.dumps(SEARCH_SYN, ensure_ascii=False) + ";")

# ---------------------------------------------------------------- main
def main():
    # Export the clean machine-readable corpus FIRST, before render_paper() mutates
    # SECTIONS by appending galleries/diagrams (keeps the corpus prose-only).
    try:
        import export_corpus
        export_corpus.main()
    except SystemExit:
        raise
    except Exception as _ce:
        print("corpus export skipped:", repr(_ce))
    sizes = {}
    sizes["assets/app.css"] = w("assets/app.css", theme.CSS)
    sizes["assets/app.js"] = w("assets/app.js", app_js.JS)
    sizes["assets/search-index.js"] = w("assets/search-index.js", build_search_index())
    sizes["index.html"] = w("index.html", render_index())
    sizes["curriculum.html"] = w("curriculum.html", render_curriculum())
    sizes["papers.html"] = w("papers.html", render_papers())
    sizes["glossary.html"] = w("glossary.html", render_glossary())
    for mod in PAPERS:
        sizes[f"{mod.SLUG}.html"] = w(f"{mod.SLUG}.html", render_paper(mod))
    w(".nojekyll", "")
    for k, v in sizes.items():
        print(f"  {k:28} {v//1024 if v>1024 else v}{'K' if v>1024 else 'B'}")
    print("build OK ->", ROOT, "| live papers:", len(PAPERS))
    if PAPER_ERRORS:
        print("!! MODULE ERRORS (not built):")
        for m, e in PAPER_ERRORS:
            print("   ", m, "->", e)

if __name__ == "__main__":
    main()
