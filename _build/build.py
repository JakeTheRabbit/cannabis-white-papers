# -*- coding: utf-8 -*-
"""Build orchestrator. Emits the static site to the repo root.
Run:  cd /c/Github/white-papers/_build && python build.py
"""
import os, re, json, sys, html as _h, hashlib, shutil
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

# Papers in display order. Import failures are recorded here and rejected by the
# first guard in main() before export or generated-file writes can occur.
PAPER_MODULES = [
    "paper_tissue_culture", "paper_cannabis_tc_playbook", "paper_cannabis_tc_sop",
    "paper_coco_crop_steering", "paper_grow_room_systems",
    "paper_airflow_design", "paper_co2_enrichment", "paper_scaling_high_light", "paper_mould_risk",
    "paper_auckland_ipm_blueprint",
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
    "paper_one_steering_law",
    "paper_under_canopy_lighting",
    "paper_plant_biosignal",
    "paper_slab_irrigation",
    "paper_hash_rosin",
    "paper_ripening",
    "paper_transplanting",
    "paper_veg_management",
    "paper_mother_plants",
    "paper_genetics_phenohunting",
    "paper_temp_humidity_vpd",
    "paper_lab_testing",
    "paper_unit_economics",
    "paper_compliance",
    "paper_hvac",
    "paper_cannabinoids_terpenes",
    "paper_energy",
    "paper_plant_biology",
    "paper_deep_water_culture",
]


def validate_paper_imports(module_names, papers, import_errors):
    """Return import/completeness diagnostics without importing or writing anything."""
    diagnostics = [
        f"paper import failed: {module_name}: {error}"
        for module_name, error in import_errors
    ]
    if len(papers) != len(module_names):
        diagnostics.append(
            f"paper import count mismatch: loaded {len(papers)} of "
            f"{len(module_names)} declared modules"
        )
    return diagnostics


def _run_import_guard_self_test():
    clean_papers = [object(), object()]
    cases = [
        (
            "clean imports",
            ["paper_a", "paper_b"],
            clean_papers,
            [],
            [],
        ),
        (
            "recorded import error",
            ["paper_a", "paper_b"],
            clean_papers[:1],
            [("paper_b", "RuntimeError('boom')")],
            [
                "paper import failed: paper_b: RuntimeError('boom')",
                "paper import count mismatch: loaded 1 of 2 declared modules",
            ],
        ),
        (
            "count mismatch without error record",
            ["paper_a", "paper_b"],
            clean_papers[:1],
            [],
            ["paper import count mismatch: loaded 1 of 2 declared modules"],
        ),
    ]
    for name, module_names, papers, errors, expected in cases:
        actual = validate_paper_imports(module_names, papers, errors)
        assert actual == expected, f"{name}: expected {expected!r}, got {actual!r}"


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

def fit_title(text, max_px=54, cls="title"):
    """A fit-to-width display heading: the title is duplicated (one visible, one
    aria-hidden for measurement) so CSS can scale it to fill the column exactly.
    See the .text-fit rules in theme.py. cls="" for the landing hero <h1>."""
    e = esc(text)
    c = (cls + " text-fit").strip()
    return (f'<h1 class="{c}" style="--max-font-size:{max_px}px">'
            f'<span><span>{e}</span></span>'
            f'<span aria-hidden="true">{e}</span></h1>')

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
def _legacy_image_target(source_secs, evidence_sec, section_index):
    """Resolve an image manifest's post-evidence index without coupling it to current placement."""
    legacy_secs = source_secs
    if evidence_sec is not None and source_secs:
        legacy_secs = [source_secs[0], evidence_sec, *source_secs[1:]]
    if not legacy_secs:
        return None
    legacy_index = max(0, min(section_index, len(legacy_secs) - 1))
    return legacy_secs[legacy_index]


def render_paper(mod):
    # Render from a disposable copy so injected panels and file-gated media do not
    # mutate the module's authoritative sections across repeated render calls.
    secs = [dict(sec, blocks=list(sec.get("blocks", []))) for sec in mod.SECTIONS]
    source_secs = list(secs)
    evidence_sec = None
    # Inject per-paper evidence confidence panel (solid / operational / provisional)
    try:
        from data import evidence as EV
        _ep = EV.panel_html(mod.SLUG)
        if _ep and secs:
            _definitions = next((i for i, sec in enumerate(secs)
                                 if sec.get("title") == "Definitions"), None)
            _ei = (_definitions + 1) if _definitions is not None else 1
            evidence_sec = {
                "id": "evidence-notes",
                "kicker": "Quality of the information",
                "title": "Evidence and limitations",
                "blocks": [_ep],
            }
            secs.insert(_ei, evidence_sec)
    except Exception as _ee:
        print("evidence panel skipped for", getattr(mod, "SLUG", "?"), repr(_ee))
    # embed any generated example images into their target sections (file-gated)
    for im in IMG.by_slug().get(mod.SLUG, []):
        # Prefer explicit ext, else try jpg then svg (fact-check pack uses both)
        candidates = []
        if im.get("ext"):
            candidates.append(f"{im['slug']}-{im['n']}.{im['ext']}")
        else:
            candidates.extend([
                f"{im['slug']}-{im['n']}.jpg",
                f"{im['slug']}-{im['n']}.svg",
                f"{im['slug']}-{im['n']}.png",
            ])
        fn = next((c for c in candidates
                   if os.path.exists(os.path.join(ASSETS, "img", c))), None)
        if fn and secs:
            target_sec = _legacy_image_target(source_secs, evidence_sec, im["sec"])
            target_sec["blocks"].append(
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
        f'{fit_title(mod.TITLE, getattr(mod, "TITLE_MAX_PX", 54))}'
        f'<p class="sub">{esc(mod.SUB)}</p>'
        f'<div class="metarow">{"".join(pills)}</div>'
        f'<div class="divider"></div>'
    )
    # index card
    toc_items = ""
    for i, s in enumerate(secs, 1):
        toc_items += f'<a href="#{s["id"]}"><span class="n">{i:02d}</span> {esc(s["title"])}</a>'
    toc_items += (
        f'<a href="#references"><span class="n">{len(secs) + 1:02d}</span> References</a>'
    )
    index_card = (f'<div class="toc-card"><div class="kicker">{icon("list",14)} In this paper</div>'
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
        npc = "" if r.get("peer") else " <span style='color:var(--faint)'>(source not from a journal, for example from a manufacturer)</span>"
        link = f' <a href="{r["url"]}" target="_blank" rel="noopener">{r["url"]}</a>' if r.get("url") else ""
        cls = "" if r.get("peer") else " class='np'"
        ref_lis += f'<li id="ref-{rid}"{cls}>{r["cite"]}{npc}{link}</li>'
    refs = (f'<div class="refs" id="references"><h2>References</h2><ol>{ref_lis}</ol>'
            f'<p class="foot">Each citation in the paper, for example [1], refers to an item in this list. '
            f'Each item is a primary source or an instruction from an authority, unless the item shows a different type. '
            f'The results of cannabis tissue culture change much with the genotype. Before you use the '
            f'dilutions, hormone doses and local regulations, make sure that they agree with the primary sources.</p></div>') if ref_lis else ""

    body = (hero + index_card + "".join(body_secs) + related + refs
            + getattr(mod, "RAW_REFERENCES", ""))
    rail_toc = [(s["id"], s["title"]) for s in secs] + [("references", "References")]
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
            soon = "" if live else '<span class="soon-tag">in production</span>'
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
    """Landing = a filterable tree index: text filter + stage pills + grouped rows with blurbs."""
    n = len(NAV.all_items())
    # per-paper blurb (first sentence of SUB) + read-time, from the live modules
    meta = {}
    for m in PAPERS:
        sub = getattr(m, "SUB", "") or ""
        blurb = sub.split(". ")[0].strip()
        if blurb and not blurb.endswith("."):
            blurb += "."
        if len(blurb) > 165:
            blurb = blurb[:162].rstrip(" ,;") + "…"
        rt = ""
        for _ic, txt in getattr(m, "META", []):
            if "read" in txt.lower():
                rt = txt.replace("~", "").strip()
        meta[m.SLUG] = (blurb, rt)
    hero = (
        '<div class="hero-land tight">'
        '<div class="eyebrow">A reference for growers, from the first step</div>'
        + fit_title("The Cannabis White Papers", 60, cls="") +
        f'<p class="sub">Each paper is a cultivation reference for a new grower. '
        f'Each term has a definition, each fact has a citation, and diagrams show the method. '
        f'We examine each paper and show the quality of the information. '
        f'The information is <strong>solid</strong>, a <strong>grower method</strong>, '
        f'or <strong>weak</strong> when the data are thin. If you find an error, '
        f'<a href="https://github.com/JakeTheRabbit/cannabis-white-papers/issues/new" target="_blank" rel="noopener">make a report on GitHub</a>. '
        f'Use the filter below for the {n} papers, or push <strong>Ctrl&nbsp;K</strong> to find a paper or a term.</p></div>'
    )
    pills = [f'<button class="fpill on" data-filter="all">All <span>{n}</span></button>']
    groups = []
    for g in NAV.GROUPS:
        gs = slugify(g["group"])
        pills.append(f'<button class="fpill" data-filter="{gs}">{esc(g["group"])} <span>{len(g["items"])}</span></button>')
        rows = []
        for it in g["items"]:
            live = it["status"] == "live"
            blurb, rt = meta.get(it["slug"], ("", ""))
            if not blurb:
                blurb = it["short"]
            dt = re.sub(r"[^a-z0-9 ]+", " ", (it["title"] + " " + blurb + " " + it["short"]).lower())
            dt = re.sub(r"\s+", " ", dt).strip()
            if live and rt:
                metah = f'<span class="trow-meta">{esc(rt)}</span>'
            elif not live:
                metah = '<span class="trow-meta soon">in production</span>'
            else:
                metah = ''
            inner = (f'<span class="trow-ic">{icon(it["icon"], 18)}</span>'
                     f'<span class="trow-main"><span class="trow-t">{esc(it["title"])}</span>'
                     f'<span class="trow-b">{esc(blurb)}</span></span>{metah}')
            tag = "a" if live else "div"
            href = f' href="{it["slug"]}.html"' if live else ''
            cls = "trow" if live else "trow soon"
            rows.append(f'<{tag} class="{cls}" data-group="{gs}" data-text="{dt}"{href}>{inner}</{tag}>')
        groups.append(f'<section class="treegroup" data-group="{gs}">'
                      f'<div class="tg-h"><h2>{esc(g["group"])}</h2><span class="tg-ct">{len(g["items"])}</span></div>'
                      f'<div class="tg-rows">{"".join(rows)}</div></section>')
    tools = ('<div class="dirtools">'
             '<input id="treeFilter" class="treefilter" type="text" '
             'placeholder="Filter papers by name or term…" autocomplete="off" spellcheck="false">'
             f'<div class="filterbar" id="filterbar">{"".join(pills)}</div></div>')
    tree = (f'<div id="paperdir">{"".join(groups)}'
            '<div class="dir-empty" id="dirEmpty" style="display:none">There are no papers for that filter.</div></div>')
    body = hero + tools + tree
    return shell.page("index", "Home", body, desc="Cannabis cultivation papers with citations, for each growth stage.", wide=True, mobile_active="index")

def render_papers():
    head = ('<div class="eyebrow">Papers by group</div>' + fit_title("All papers", 54) +
            '<p class="sub">Each group shows its papers. You cannot open a paper that is '
            'in production.</p><div class="divider"></div>')
    body = head + track_grid()
    return shell.page("papers", "All papers", body, desc="The full list of the papers.", wide=True, mobile_active="papers")

# ---------------------------------------------------------------- glossary
def render_glossary():
    head = ('<div class="eyebrow">Reference</div>' + fit_title("Glossary", 54) +
            '<p class="sub">Each term in the papers has a definition here. '
            'The definitions are for new growers.</p><div class="divider"></div>')
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
    return shell.page("glossary", "Glossary", body, desc="Definitions of each term in the papers.", wide=True, mobile_active="glossary")

# ---------------------------------------------------------------- curriculum tree
CURRICULUM = [
 ("1 · Propagation", "Start the plants.", [
   ("Seeds, germination and seedlings", "seeds-germination"), ("Cloning", "cloning"),
   ("Tissue culture: clean genetics", "tissue-culture"),
   ("Tissue culture method", "cannabis-tissue-culture-playbook"),
   ("Tissue culture SOP", "cannabis-tissue-culture-sop"),
   ("Mother plants (stock plants)", "mother-plants"), ("Transplanting to larger pots", "transplanting")]),
 ("2 · Vegetative growth", "Make a large plant in good condition.", [
   ("Light acclimation", "light-acclimation"), ("Defoliation and plant training", "defoliation-training"),
   ("Vegetative stage length", "veg-management")]),
 ("3 · Flowering", "Control the plant for yield and quality.", [
   ("The flower cycle, week by week", "flowering-stages"),
   ("Precision coco cultivation: crop steering", "coco-crop-steering"),
   ("Rockwool crop steering with drybacks and saturation", "rockwool-crop-steering"),
   ("One steering method for coco, rockwool, soil and water", "one-steering-law"),
   ("Ripening, how to flush, and when to harvest", "ripening-harvest-timing")]),
 ("4 · Harvest, dry, trim and cure", "Make product from flower.", [
   ("Harvest, dry, trim and cure", "harvest-dry-trim-cure"), ("GMP hash production", "gmp-hash-lab"),
   ("Hash rosin without solvents", "hash-rosin-pressing"), ("Lab testing, potency and COAs", "lab-testing-coas")]),
 ("For all stages · Environment and climate", "The conditions around the plant.", [
   ("The grow room as a system", "grow-room-systems"), ("Lighting: spectrum, PPFD and DLI", "lighting-fundamentals"),
   ("Airflow and fans", "airflow-design"), ("Lower-canopy and inner-canopy lighting", "under-canopy-lighting"),
   ("Temperature, humidity and VPD", "temp-humidity-vpd"),
   ("CO2 enrichment", "co2-enrichment"), ("HVAC and dehumidification", "hvac-dehumidification")]),
 ("For all stages · Water, substrate and feed", "The water and feed that the roots get.", [
   ("Substrates compared: coco, rockwool, soil and hydro", "substrates-overview"),
   ("Source water, RO and alkalinity", "water-quality"), ("pH: keep it stable", "ph-management"),
   ("Mix an Athena Pro Line stock tank", "nutrient-mixing-athena"),
   ("Nutrient deficiencies and toxicity", "nutrient-deficiencies")]),
 ("For all stages · Plant health", "Keep the plants clean.", [
   ("IPM for medical cannabis in Auckland", "auckland-ipm-blueprint"),
   ("Mold risk with bud rot and PM", "mould-risk"), ("IPM SOP", "ipm-sop"),
   ("Pest identification and control", "pest-id"), ("PPE and biosecurity (PPPE)", "pppe"),
   ("Root diseases: pythium and fusarium", "auckland-ipm-blueprint")]),
 ("For all stages · Precision and automation", "Set the values and let the system operate.", [
   ("Root-zone condition (TEROS-12)", "root-zone-teros12"), ("Signal and noise", "signal-and-noise"),
   ("Irrigation control (VRWE)", "smart-watering-vrwe"), ("The closed loop", "closed-loop"),
   ("Plant state dashboard", "plant-state-dashboard"), ("F2 crop steering", "f2-crop-steering"),
   ("Irrigation manual", "irrigation-manual"),
   ("DIY plant-biosignal sensor", "plant-biosignal-sensor")]),
 ("The operation · Facility and quality", "Control the quality and the cost of the operation.", [
   ("3D facility model", "facility-3d"),
   ("Checks each day: sensors do most of the work", "daily-checks"),
   ("Compliance, licenses and traceability", "compliance-track-trace"),
   ("Energy and utilities", "energy-sustainability"), ("Yield and unit cost", "unit-economics")]),
 ("Reference · Know the plant", "Basic information about the plant.", [
   ("Cannabis plant biology and life cycle", "plant-biology"), ("Cannabinoids and terpenes", "cannabinoids-terpenes"),
   ("Genetics, seeds and the phenohunt", "genetics-phenohunting")]),
]

def render_curriculum():
    total = sum(len(items) for _, _, items in CURRICULUM)
    live = sum(1 for _, _, items in CURRICULUM for _, slug in items if slug in _LIVE)
    head = (
        '<div class="eyebrow">Papers in sequence</div>'
        + fit_title("Start here: the growth stages, one by one", 46) +
        '<p class="sub">This list shows all the papers in groups. The first four groups follow the '
        'growth stages, from propagation to harvest. The other groups are for all stages. '
        'A row that you can open is a paper that is available at this time. '
        'The other rows are papers in production.</p>'
        f'<div class="hero-stats" style="justify-content:flex-start;gap:28px;margin:22px 0 0">'
        f'<div class="s"><b>{live}</b><span>available</span></div>'
        f'<div class="s"><b>{total}</b><span>in the full list</span></div>'
        f'<div class="s"><b>{round(live/total*100)}%</b><span>done</span></div></div>'
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
                            f'<span>{esc(label)}</span><span class="soon-tag">in production</span></div>')
        parts.append(f'<div class="curtier"><div class="curtier-h"><h3>{esc(title)}</h3>'
                     f'<span class="d">{esc(desc)}</span></div><div class="curlist">{"".join(rows)}</div></div>')
    return shell.page("curriculum", "Start here", "".join(parts),
                      desc="All the cultivation papers, in the sequence of the growth stages.",
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
    pages = list(NAV.TOP) + [{"slug": "curriculum", "title": "Papers in sequence", "icon": "list"}]
    for t in pages:
        url = "index.html" if t["slug"] == "index" else f'{t["slug"]}.html'
        idx.append({"type": "index", "title": t["title"], "url": url, "text": "", "kw": ""})
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
        idx.append({"type": "in production", "title": it["title"], "url": "papers.html",
                    "text": it["short"], "kw": ""})
    for g in GL.GLOSSARY:
        idx.append({"type": "term", "title": g["term"],
                    "url": f'glossary.html#gl-{slugify(g["term"])}',
                    "text": _plain(g["defn"]), "kw": " ".join(g.get("tags", []))})
    return ("window.SEARCH_INDEX=" + json.dumps(idx, ensure_ascii=False) + ";\n"
            "window.SEARCH_SYN=" + json.dumps(SEARCH_SYN, ensure_ascii=False) + ";")

# ---------------------------------------------------------------- main
def main():
    # Fail closed on incomplete imports before export or any generated-file write.
    import_diagnostics = validate_paper_imports(PAPER_MODULES, PAPERS, PAPER_ERRORS)
    if import_diagnostics:
        for diagnostic in import_diagnostics:
            print(diagnostic)
        raise SystemExit(1)
    # Validate the source dictionaries before export/rendering writes artifacts.
    from check_section_structure import validate_modules
    section_diagnostics = validate_modules(PAPERS)
    if section_diagnostics:
        for diagnostic in section_diagnostics:
            print(diagnostic)
        raise SystemExit(1)
    # Export the clean machine-readable corpus FIRST, before render_paper() mutates
    # SECTIONS by appending galleries/diagrams (keeps the corpus prose-only).
    try:
        import export_corpus
        export_corpus.main()
    except SystemExit:
        raise
    except Exception as _ce:
        print("corpus export skipped:", repr(_ce))
    # cache-bust: version assets by a hash of the CSS+JS so deploys always show fresh
    shell.ASSET_VER = hashlib.md5((theme.CSS + app_js.JS).encode("utf-8")).hexdigest()[:8]
    sizes = {}
    sizes["assets/app.css"] = w("assets/app.css", theme.CSS)
    sizes["assets/app.js"] = w("assets/app.js", app_js.JS)
    sizes["assets/search-index.js"] = w("assets/search-index.js", build_search_index())
    static_assets = os.path.join(os.path.dirname(__file__), "static")
    if os.path.isdir(static_assets):
        shutil.copytree(static_assets, ASSETS, dirs_exist_ok=True)
    sizes["index.html"] = w("index.html", render_index())
    sizes["curriculum.html"] = w("curriculum.html", render_curriculum())
    sizes["papers.html"] = w("papers.html", render_papers())
    sizes["glossary.html"] = w("glossary.html", render_glossary())
    for mod in PAPERS:
        sizes[f"{mod.SLUG}.html"] = w(f"{mod.SLUG}.html", render_paper(mod))
    w(".nojekyll", "")
    try:
        import standalone_ipm
        standalone_ipm.build()
    except Exception as _se:
        print("standalone IPM build failed:", repr(_se))
        raise
    from check_generated_structure import validate_generated_structure
    generated_diagnostics = validate_generated_structure(ROOT, PAPERS)
    if generated_diagnostics:
        for diagnostic in generated_diagnostics:
            print(diagnostic)
        raise SystemExit(1)
    print(f"generated-structure OK: {len(PAPERS)} papers")
    for k, v in sizes.items():
        print(f"  {k:28} {v//1024 if v>1024 else v}{'K' if v>1024 else 'B'}")
    print("build OK ->", ROOT, "| live papers:", len(PAPERS))
    if PAPER_ERRORS:
        print("!! MODULE ERRORS (not built):")
        for m, e in PAPER_ERRORS:
            print("   ", m, "->", e)

if __name__ == "__main__":
    if sys.argv[1:] == ["--self-test-import-guard"]:
        _run_import_guard_self_test()
        print("paper-import guard self-test OK")
    else:
        main()
