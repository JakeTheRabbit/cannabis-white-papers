# -*- coding: utf-8 -*-
"""Per-paper evidence tiers: solid / operational / provisional.

Injected by build.py as a standard 'How sure is this?' section so readers can
tell verified science from commercial practice and unverified folklore.
"""
from components import esc

# Tiers:
# solid       — strong plant physiology, standards, or multi-source consensus
# operational — commercial practice ranges; work well but cultivar/facility vary
# provisional — thin cannabis data, single studies, product design, or folklore

DEFAULT = {
    "solid": [
        "Core definitions and measurement units used in the paper",
        "Safety-critical limits where occupational or standards sources are cited",
    ],
    "operational": [
        "Numeric stage targets (light, climate, feed) as starting bands, not laws",
        "SOPs that work in many rooms but need your genetics and meters",
    ],
    "provisional": [
        "Any single-number 'guaranteed' yield or potency claim without a multi-site trial",
        "Controller setpoints copied from another facility without re-calibration",
    ],
}

# slug -> {solid, operational, provisional} lists of short strings
PAPERS = {
    "seeds-germination": {
        "solid": [
            "Seeds need water + warmth; damping-off is driven by overwet, stagnant conditions",
            "Feminised seed is XX×XX induction (STS/colloidal silver class methods), not 100% herm-proof",
            "Photoperiod plants respond to night length; autos flower largely by age/genetics",
        ],
        "operational": [
            "21–25 °C germination band and gentle seedling PPFD ramps",
            "Humidity-dome / high RH early, then ease humidity as roots establish",
            "Visual seed quality checks (colour/firmness) as a screen, not a lab viability assay",
        ],
        "provisional": [
            "Exact germination % for any seed lot (batch age and storage dominate)",
            "Paper-towel 'near-perfect' success rates — method is secondary to seed quality and moisture control",
        ],
    },
    "cloning": {
        "solid": [
            "Clones are genetic copies of the mother (barring rare somatic mutation)",
            "High humidity and gentle light reduce cutting stress until roots form",
            "Dirty tools and wet stagnant media raise soft-rot / pathogen risk",
        ],
        "operational": [
            "IBA gel/powder protocols and dome venting schedules used in commercial prop rooms",
            "90%+ rooting as a well-run room target, not a genetics guarantee",
            "Mild feed after roots show; over-strong EC burns soft cuttings",
        ],
        "provisional": [
            "Any single 'air embolism' story as the main soft-stem failure mode (desiccation usually dominates)",
            "Exact day-to-root tables that ignore cultivar and environment",
        ],
    },
    "tissue-culture": {
        "solid": [
            "Meristem tissue is often cleaner of systemic pathogens than nodal cuttings",
            "No spray cures a viroid-infected plant; free ≠ resistant after cleanup",
            "RT-qPCR (RNA) is the right class of test for HpLVd — not a casual 'DNA strip' alone",
        ],
        "operational": [
            "High first-run contamination losses for beginners (cannabis is recalcitrant)",
            "Timeline of months for verified clean mothers including indexing",
            "Aseptic technique quality dominates kit brand",
        ],
        "provisional": [
            "Facility infection prevalence surveys as permanent global rates (time/region-specific)",
            "Exact seed-transmission percentages for every cross (genotype-dependent)",
            "Claims that TC alone permanently clears every endophyte, mite, or surface pathogen without hygiene afterward",
        ],
    },
    "light-acclimation": {
        "solid": [
            "Sudden PPFD jumps cause photoinhibition / bleaching; ramps reduce that risk",
            "12/12 vs 18/6 at equal PPFD cuts DLI by one-third (~33%)",
        ],
        "operational": [
            "Multi-day dimmer or height ramps used in commercial rooms",
            "Ambient-CO₂ practical intensity ceilings as stress/ROI guidance",
        ],
        "provisional": [
            "Any single far-red % yield jump generalized across all cultivars",
            "Exact 'must hit X µmol by day Y' schedules without leaf-temp and VPD context",
        ],
    },
    "defoliation-training": {
        "solid": [
            "Leaves are carbon sources; removing them removes photosynthetic capacity",
            "Canopy structure affects light interception and airflow / mould risk",
        ],
        "operational": [
            "Topping, LST, SCROG, lollipop timing windows used by many indoor growers",
            "Stop heavy defoliation once bulk flower sets",
        ],
        "provisional": [
            "Fixed % yield gains from a specific defoliation recipe across all densities",
            "Day 5–7 topping as universal (clone multi-node vs seed starts differ)",
        ],
    },
    "flowering-stages": {
        "solid": [
            "Photoperiod cannabis needs long nights; light leaks can disrupt flowering",
            "Trichomes and pistils are maturity cues; calendar alone is weak",
            "Dense late canopies + high humidity raise Botrytis risk",
        ],
        "operational": [
            "8–10 week hybrid flowering maps and stage climate bands",
            "Stretch expectations that vary widely by cultivar and spectrum",
        ],
        "provisional": [
            "Amber trichomes = CBN = couch-lock as a clean pharmacological switch (multi-factor; human CBN evidence limited)",
            "Long plain-water 'flush' improving smoke quality (controlled tests often show little benefit)",
            "Phone-LED / tiny indicator light as a proven herm trigger (night integrity matters; genetics + multi-stress dominate herms)",
        ],
    },
    "coco-crop-steering": {
        "solid": [
            "Coco is relatively inert; root-zone EC and water content are highly operator-controlled",
            "Mild water deficit can alter secondary metabolism; severe drought stresses plants",
        ],
        "operational": [
            "Daily dryback + runoff EC as commercial steering levers",
            "Field-capacity / dryback point targets after media-specific sensor calibration",
        ],
        "provisional": [
            "Mapping Caplan-style single late drought directly onto multi-week daily dryback recipes",
            "Any fixed 'generative EC' band that ignores cultivar and light intensity",
        ],
    },
    "rockwool-crop-steering": {
        "solid": [
            "Rockwool holds almost no nutrient reserve; pore-water chemistry tracks feed closely",
            "Over-dry slabs can channel / rewet poorly",
        ],
        "operational": [
            "Industry dryback bands and multi-shot irrigation schedules (Grodan-class practice)",
            "Runoff management to limit salt accumulation",
        ],
        "provisional": [
            "Exact recovery-floor WC % as a universal physics constant across all products",
            "Pure inverse-EC maths as exact substrate EC without plant uptake",
        ],
    },
    "one-steering-law": {
        "solid": [
            "Wet–dry and feed strength are the shared steering language across media",
            "Soil buffers; coco/rockwool/water do not buffer the same way",
        ],
        "operational": [
            "Unified mental model (drive / brake) for different substrates",
        ],
        "provisional": [
            "Beginner coco recipes that import high-intensity rockwool substrate EC numbers",
            "DWC 'root rot within a day above 23 °C' as a universal timeline (DO + heat matter, timing varies)",
        ],
    },
    "harvest-dry-trim-cure": {
        "solid": [
            "Water activity predicts microbial risk better than moisture % alone (ASTM-style 0.55–0.65 for flower)",
            "Slow cool dark dry protects terpenes better than hot fast dry",
            "Light and heat accelerate cannabinoid/terpene degradation in storage",
        ],
        "operational": [
            "60 °F / 60% RH style hang-dry defaults and whole-plant hang practice",
            "Dry-trim preference for many quality-focused rooms",
        ],
        "provisional": [
            "Vendor '5–10% yield recovered' figures as multi-site peer results",
            "Exact aw drop from trimming as a universal constant",
        ],
    },
    "gmp-hash-lab": {
        "solid": [
            "Concentrates can enrich residues relative to input biomass depending on process yield and partitioning",
            "Documented, inspectable systems (records, CAPA, genealogy) are the core of GMP thinking",
        ],
        "operational": [
            "Room flow, gowning, and batch-record patterns used in regulated facilities",
        ],
        "provisional": [
            "ICH residual-solvent numbers as your cannabis licence limits (jurisdiction-specific)",
            "EU Annex 1 Grade A/B as default for all hash (product/licence dependent)",
            "Any fixed 'seven mandatory test families' without your regulator's panel",
        ],
    },
    "grow-room-systems": {
        "solid": [
            "Light, heat, humidity, CO₂, water and airflow couple; one dial moves others",
            "VPD is a useful plant-comfort framing of T + RH",
        ],
        "operational": [
            "0.8–1.5 kPa style VPD bands by stage as hort starting points",
            "Sealed vs vented room design choices",
        ],
        "provisional": [
            "Exact VPD optima from non-cannabis crops applied as hard cannabis law",
            "Tacoing always = VPD alone (often light + leaf heat + VPD)",
        ],
    },
    "lighting-fundamentals": {
        "solid": [
            "PAR/PPFD/DLI definitions and photoperiod night-length control of flowering",
            "More light raises yield only until another factor limits (Liebig)",
            "LED efficacy bands for modern fixtures (era-dependent; check current DLC/maps)",
        ],
        "operational": [
            "Stage PPFD tables for indoor cannabis without/with CO₂",
            "9-point map uniformity checks",
        ],
        "provisional": [
            "Inverse-square as exact hang-height math for multi-bar LED panels (use maps + meters)",
            "Red light 'drives flowering' as the primary mechanism (photoperiod does; R:FR affects morphology)",
            "UV-B as a reliable potency booster (evidence mixed; safety cost real)",
        ],
    },
    "airflow-design": {
        "solid": [
            "Boundary-layer thinning improves gas exchange; still air holds humidity at the leaf",
            "Mechanical flexure (thigmomorphogenesis) can affect stem strength",
        ],
        "operational": [
            "~0.3–1.0 m/s canopy flutter bands and HAF layout habits",
        ],
        "provisional": [
            "Hard disease/stress velocity cliffs without measurement height defined",
        ],
    },
    "under-canopy-lighting": {
        "solid": [
            "Upper canopy filters spectrum; understory is relatively green/FR-enriched vs blue/red-rich",
            "Lower sites often light-limited for grade/fill",
        ],
        "operational": [
            "SCL/ICL commercial installs and bleach-risk management at short range",
        ],
        "provisional": [
            "Any single 'minimum viability PPFD' for all lower flowers",
            "Sealed-room continuous high ACH recipes that dump CO₂",
        ],
    },
    "co2-enrichment": {
        "solid": [
            "C3 plants including cannabis respond to elevated CO₂ under strong light",
            "Inject in light only; NDIR sensors; occupational limits ~5,000 / 30,000 / 40,000 ppm class",
            "Sealed rooms retain enrichment; exhaust vents it",
        ],
        "operational": [
            "1,000–1,500 ppm enrichment bands and bottled delivery as standard sealed-room practice",
            "Dark-period purge / ethylene management concepts",
        ],
        "provisional": [
            "Exact % yield uplift for every room (genetics, light, seal quality dominate)",
            "Unmeasured drying-room CO₂ ceilings as percent-level facts (measure your room)",
            "Tomato greenhouse % gains mapped 1:1 to cannabis flower",
        ],
    },
    "scaling-high-light": {
        "solid": [
            "Raising PPFD raises demand for water, nutrients, cooling, and often CO₂",
            "Canopy yield can keep rising past single-leaf saturation points",
        ],
        "operational": [
            "Ladder tables as engineering sizing guides under strong control",
        ],
        "provisional": [
            "Extreme runoff EC / feed ladders as beginner defaults",
            "Simple PPFD × constant water-use formulas without VPD/LAI/CO₂ context",
        ],
    },
    "substrates-overview": {
        "solid": [
            "Air-filled porosity and water-holding differ by media class",
            "Soil buffers pH/nutrients; inert media do not",
        ],
        "operational": [
            "Beginner medium pick heuristics (forgiveness vs control)",
        ],
        "provisional": [
            "Living soil pH self-correcting 'within minutes for any water'",
            "Single AFP % as universal for all rockwool SKUs",
        ],
    },
    "water-quality": {
        "solid": [
            "Alkalinity ≠ hardness; chloramine ≠ free chlorine for removal methods",
            "DO saturation falls gently with temperature; warm low-O₂ systems raise root disease risk",
        ],
        "operational": [
            "RO decision thresholds and source-EC budgeting in mS/cm",
        ],
        "provisional": [
            "Fixed 800–900 ppm 'feed ceiling' independent of scale and stage",
            "Chlorine injury thresholds transferred from lettuce as cannabis hard limits",
        ],
    },
    "ph-management": {
        "solid": [
            "pH gates nutrient availability; lockout can look like deficiency",
            "Soilless sweet spots roughly mid-5s to mid-6s; soil higher/wider",
        ],
        "operational": [
            "Inflow pH discipline and two-point pen calibration habits",
        ],
        "provisional": [
            "Low-pH chemistry details from basil/lettuce applied without cannabis context",
            "Runoff EC always within 10% of feed as a universal law (steering may hold higher root-zone EC on purpose)",
        ],
    },
    "nutrient-mixing-athena": {
        "solid": [
            "A/B separation prevents Ca + sulphate/phosphate precipitation",
            "Stock concentration maths for stated bag-into-volume recipes",
        ],
        "operational": [
            "Athena Pro Line stock-and-dose workflow as one commercial system among many",
        ],
        "provisional": [
            "Any third-party dosing table not verified with your meter and water",
        ],
    },
    "nutrient-deficiencies": {
        "solid": [
            "Mobile vs immobile symptom position is a first-pass diagnostic rule",
            "pH lockout, overwatering, and light stress mimic nutrient issues",
        ],
        "operational": [
            "Field guides for N/P/K/Mg/Ca/Fe patterns on cannabis",
        ],
        "provisional": [
            "Visual diagnosis as lab-certainty without tissue/substrate tests",
            "Incomplete micronutrient atlas (Zn/B/Mn/Cu/Mo need extra care)",
        ],
    },
    "mould-risk": {
        "solid": [
            "Botrytis favours high humidity, dense tissue, poor air exchange",
            "In-canopy RH can exceed room sensor readings",
        ],
        "operational": [
            "Late-flower RH step-downs and bag-and-cut protocols",
        ],
        "provisional": [
            "Any fixed '60–70% flowering RH' as a safe late-flower target band",
            "Relative-risk multipliers from claims data without absolute rates (immunocompromised remain high-stakes)",
        ],
    },
    "auckland-ipm-blueprint": {
        "solid": [
            "Exclusion, clean stock, monitoring, and CAPA structure",
            "NZ pathway thinking: approval/status is not the same as 'someone used it once'",
        ],
        "operational": [
            "Threshold models and mother-room controls as facility SOPs",
        ],
        "provisional": [
            "Any named product/organism status without checking the live register today",
            "AI-generated diagnostic plates as confirmatory ID (training aids only)",
        ],
    },
    "ipm-sop": {
        "solid": [
            "IPM hierarchy: prevent → monitor → soft → hard",
            "Label rate and legal status rule any spray",
        ],
        "operational": [
            "Scouting cadences and example action thresholds",
        ],
        "provisional": [
            "Kitchen volumetric rates for pesticides (never; labels only)",
            "Day-21 foliar lockout as global science law (quality SOP, not universal regulation)",
            "Biocontrol agents assumed legal in every country",
        ],
    },
    "pest-id": {
        "solid": [
            "Loupe/scope confirmation before treating lookalikes",
            "Life-cycle awareness matters for timing controls",
        ],
        "operational": [
            "Common cannabis pest field signs and biocontrol pairings where legal",
        ],
        "provisional": [
            "Extreme life-cycle times (e.g. 3-day full generations) as typical rather than hot/dry extremes",
            "Sticky-card density rules of thumb as optimized science",
        ],
    },
    "pppe": {
        "solid": [
            "People are major contamination vectors; mechanical HpLVd spread on tools/hands is real",
            "Hand hygiene log reductions are log-scale (≈90/99/99.9% class under test conditions)",
            "Clean→dirty personnel flow; waste dirty→exit",
        ],
        "operational": [
            "Gowning order and two-kit models for cultivation vs post-harvest",
            "NZ HSWA PPE framing where applicable",
        ],
        "provisional": [
            "Exact '70–90% of cleanroom contamination is people' as a universal constant",
            "Phone-vs-toilet-seat rankings as rigorous biosecurity metrics",
        ],
    },
    "root-zone-teros12": {
        "solid": [
            "Capacitance probes estimate VWC via permittivity; media calibration matters",
            "Pore-water EC estimation has real limits (Hilhorst-class caveats)",
        ],
        "operational": [
            "Install depth, volume of influence, and multi-pot placement habits",
        ],
        "provisional": [
            "Manufacturer accuracy specs as guaranteed on every uncalibrated pack",
        ],
    },
    "smart-watering-vrwe": {
        "solid": [
            "Single moisture probes can lie; multi-signal caution is sound engineering",
        ],
        "operational": [
            "VRWE-style fusion as a safety architecture for automated irrigation",
        ],
        "provisional": [
            "Any claim the system 'never floods, never starves' in all failure modes",
            "Transpiration proxies as precise water-need models without crop coefficients",
        ],
    },
    "signal-and-noise": {
        "solid": [
            "Control charts and filtering reduce false alarms; sensors have noise",
        ],
        "operational": [
            "Sampling cadence and deadbands for grow-room automation",
        ],
        "provisional": [
            "Fixed '% of alerts are noise' figures cited to process-industry standards without your measured rate",
            "Mashed Western Electric / Nelson rule names without source attribution",
        ],
    },
    "closed-loop": {
        "solid": [
            "Act → measure → compare → adjust is valid control theory",
            "Coupled climate variables should not be tuned in isolation",
        ],
        "operational": [
            "Dashboard and automation design patterns for rooms",
        ],
        "provisional": [
            "Guaranteed tip-burn prediction lead times from non-cannabis analogies",
            "Whole-room health 'in under five seconds' as demonstrated hort performance",
        ],
    },
    "plant-state-dashboard": {
        "solid": [
            "Showing plant state beats raw sensor walls for operators",
        ],
        "operational": [
            "UX patterns and advisory wording examples",
        ],
        "provisional": [
            "Any on-screen clinical prognosis (e.g. tip burn in 48 h) as a validated model",
        ],
    },
    "f2-crop-steering": {
        "solid": [
            "Emergency stop ≠ disarm is a correct safety design principle",
            "Sensor-driven irrigation needs calibrated VWC, not raw factory %",
        ],
        "operational": [
            "Phase machines and Home Assistant entity patterns for one facility class",
        ],
        "provisional": [
            "Default VWC numbers as universal substrate truth",
            "Caplan drought as full proof of a specific P0–P3 recipe",
        ],
    },
    "irrigation-manual": {
        "solid": [
            "Missing safety sensors mean do not run unattended",
            "Vegetative vs generative dryback polarity (smaller vs larger controlled drybacks)",
        ],
        "operational": [
            "Install and maintenance procedures for a sensor-driven manifold",
        ],
        "provisional": [
            "Any facility's entity names and setpoints as plug-and-play for yours",
        ],
    },
    "plant-biosignal-sensor": {
        "solid": [
            "Plants generate measurable biopotentials; electrode noise is a real engineering problem",
        ],
        "operational": [
            "DIY AD8232 + ESPHome acquisition as a logging hobby build",
        ],
        "provisional": [
            "Inferring NPK, irrigation need, or stress state from DIY millivolts alone",
            "Commercial product model outputs reproduced without their trained library",
            "Emotional-state classification literature applied to cultivation decisions",
        ],
    },
    "facility-3d": {
        "solid": [
            "Layout clashes found in CAD cost less than clashes in concrete",
        ],
        "operational": [
            "3D planning workflow for rooms, doors, and equipment footprints",
        ],
        "provisional": [
            "WAC/IBC examples as your local licence rules",
            "Any model as engineering stamp / fire-life-safety approval",
        ],
    },
    "daily-checks": {
        "solid": [
            "Checklists improve process reliability in high-risk work",
        ],
        "operational": [
            "HA auto-tick + walk-around hybrid for grow ops",
        ],
        "provisional": [
            "Surgical mortality reductions as evidence of cannabis yield gains",
            "Home Assistant logs as default validated GxP/GACP audit systems",
            "Implementation-intention effect sizes as '2–3×' without base rates",
        ],
    },
}


def get(slug: str) -> dict:
    d = PAPERS.get(slug)
    if not d:
        return DEFAULT
    # merge defaults for empty tiers
    out = {
        "solid": list(d.get("solid") or DEFAULT["solid"]),
        "operational": list(d.get("operational") or DEFAULT["operational"]),
        "provisional": list(d.get("provisional") or DEFAULT["provisional"]),
    }
    return out


def panel_html(slug: str) -> str:
    """Full evidence panel HTML for injection into a paper."""
    e = get(slug)
    def lis(items):
        return "<ul class='ev-list'>" + "".join(f"<li>{x}</li>" for x in items) + "</ul>"

    issues = (
        "https://github.com/JakeTheRabbit/cannabis-white-papers/issues/new"
        "?title=Accuracy%20report%3A%20" + slug +
        "&body=Paper%3A%20" + slug + "%0A%0AWhat%20looks%20wrong%3A%0A%0AWhat%20you%20expected%20%2F%20source%20if%20you%20have%20one%3A%0A"
    )

    return (
        "<div class='evidence-panel' id='evidence-notes'>"
        "<div class='evidence-h'>"
        "<div class='evidence-kicker'>How sure is this paper?</div>"
        "<p class='evidence-lead'>We've gone to great lengths to keep these guides honest. One of the main ways we do "
        "that is <strong>self-review</strong>: we actively look for claims that are subjective, only lightly backed by "
        "literature, or based on grower practice rather than a controlled study &mdash; and we <strong>call those out</strong> "
        "instead of dressing them up as settled science.</p>"
        "<p class='evidence-lead'>Often there simply is no paper for the decision you're making. In those cases we're "
        "drawing on what other growers report and what has worked in our own rooms. That can still be useful &mdash; "
        "but it is not a lab proof. <strong>Do what works for your plants, your room, and your meters.</strong> "
        "If a table disagrees with your crop, believe the crop and log the difference.</p>"
        "</div>"
        "<div class='evidence-grid'>"
        "<div class='evidence-col solid'>"
        "<div class='evidence-badge'>Solid</div>"
        "<div class='evidence-sub'>Well supported by plant science, standards, or broad multi-source consensus</div>"
        + lis(e["solid"]) +
        "</div>"
        "<div class='evidence-col operational'>"
        "<div class='evidence-badge'>Operational</div>"
        "<div class='evidence-sub'>What many growers and rooms actually run &mdash; start here, then tune</div>"
        + lis(e["operational"]) +
        "</div>"
        "<div class='evidence-col provisional'>"
        "<div class='evidence-badge'>Grain of salt</div>"
        "<div class='evidence-sub'>Subjective, thin literature, single studies, or &ldquo;this works for us&rdquo; practice</div>"
        + lis(e["provisional"]) +
        "</div>"
        "</div>"
        "<p class='evidence-foot'><strong>See something glaringly wrong?</strong> Tell us and we'll fix it. "
        "Please open a GitHub issue with the paper name and what looks off "
        f"(include a source if you have one): <a href='{issues}' target='_blank' rel='noopener'>Report an accuracy issue</a>. "
        "Local law, labels, and licences always override any recipe here. "
        "Inline notes labelled <span class='ev-tag'>grain of salt</span> flag the highest-risk over-trust points in the text.</p>"
        "</div>"
    )


def community_note(body: str, title: str = "Grain of salt") -> str:
    """Inline provisional callout (used from papers or build)."""
    from components import callout
    return callout("evidence", title, f"<p>{body}</p>")
