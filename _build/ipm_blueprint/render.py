# -*- coding: utf-8 -*-
"""Render structured Auckland IPM content into the repo's paper section model."""

from components import (
    p,
    lead,
    h,
    ul,
    ol,
    callout,
    defterm,
    table,
    figure,
    photo,
    term_gallery,
    stagecard,
    grid,
    card,
    kv,
    steps,
)
import figs_lib as L

from ipm_blueprint.content import (
    APPROVED_TOOL_FIELDS,
    ATLAS,
    BENEFICIAL_ROWS,
    CONTROL_LAYERS,
    GLOSSARY,
    LEGAL_GATES,
    REFERENCE_PLATES,
    REF_IDS,
    SCOUT_FIELDS,
    SEVERITY,
)


def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (
        rid,
        REF_IDS.index(rid) + 1,
    )


def _atlas_profile(entry, number):
    evidence = "".join(_c(rid) for rid in entry.get("refs", []))
    return "".join(
        [
            h(3, f"{number}. {entry['name']} ({entry['scientific']})"),
            photo(
                entry["image"],
                entry["identify"] + " <strong>Generated plate; not to scale and apparent magnification varies.</strong>",
                entry["alt"],
                "OpenAI image generation",
            ),
            kv(
                [
                    ("Earliest reliable signs", entry["signs"]),
                    ("Life cycle and spread", entry["biology"]),
                    ("Condition-qualified development", entry["development"]),
                    ("Size / inspection scale", entry["scale"]),
                    ("Where to inspect", entry["inspect"]),
                    ("Confirmation", entry["confirm"]),
                    ("Lookalikes", entry["lookalikes"]),
                    ("Internal threshold", entry["threshold"]),
                    ("First response", entry["response"]),
                    ("Layered control options", entry["controls"]),
                    ("Target stage and plant part", entry["targeting"]),
                    ("Crop, worker, residue and compatibility constraints", entry["constraints"]),
                    ("Specimen handling", entry["specimen"]),
                    ("Dated recheck and success criterion", entry["recheck"]),
                    ("Trace-back and CAPA trigger", entry["capa"]),
                ]
            ),
            p("Profile evidence: " + evidence),
        ]
    )


def _input(name, label, wide=False):
    cls = "facility-input wide" if wide else "facility-input"
    if wide:
        field = f"<textarea name='{name}' rows='3'>FACILITY INPUT</textarea>"
    else:
        field = f"<input name='{name}' value='FACILITY INPUT'>"
    return f"<label class='{cls}'><span>{label}</span>{field}</label>"


def build_sections():
    sections = []

    sections.append(
        {
            "id": "how-to-use",
            "kicker": "01 · Read this first",
            "title": "What this blueprint is, and what it refuses to pretend",
            "blocks": [
                lead(
                    "This is an operating blueprint for an indoor medicinal-cannabis facility in Auckland. "
                    "It joins pest and disease identification to clean stock, New Zealand input legality, "
                    "worker safety, residue release, traceability and CAPA. The point is not to own the most "
                    "sprays. The point is to keep biology and compliance from cornering you at the same time."
                ),
                p(
                    "The supplied 128-page IPM Book V15 was used as a coverage benchmark: IPM principles, "
                    "cultural/environmental/biological/chemical controls, programme construction, eight "
                    "arthropod profiles, six disease profiles, identification resources, glossary and operator "
                    "tools" + _c("athena-ipm-book-v15") + ". Its branded programmes, artwork, rates and prose "
                    "are not reproduced. New Zealand official sources and primary literature control this paper."
                ),
                callout(
                    "danger",
                    "Generated photographs are educational reconstructions",
                    p(
                        "Every photographic plate in this guide was generated for the paper. Use it to decide "
                        "where to look and what to sample, never to claim species-level confirmation. Broad and "
                        "russet mites require microscopy; HLVd requires RT-qPCR or RT-PCR; root and leaf diseases "
                        "often require a diagnostic laboratory. A convincing image is not a test result."
                    ),
                ),
                ul(
                    [
                        "<strong>Live status wins.</strong> Re-check the current Ministry, ACVM, EPA, label, SDS and WorkSafe position at procurement and use.",
                        "<strong>Facility thresholds are controlled values.</strong> Numbers in this blueprint are examples or planning defaults unless your approved SOP adopts them.",
                        "<strong>Old damage does not heal.</strong> Verify success with live organisms, new lesions, new growth, traps, roots or laboratory results - not cosmetic recovery.",
                        "<strong>Clean stock is the centre.</strong> A mother-room failure compounds through every daughter lot. Treat it accordingly.",
                    ]
                ),
                figure(
                    L.flow(
                        "Evidence to action",
                        [
                            ("Observe", "mapped scout, trap, environment or test"),
                            ("Confirm", "microscopy or laboratory where required"),
                            ("Classify", "room, incidence, severity, trend, zero-tolerance"),
                            ("Select", "legal + effective + compatible + residue-defensible"),
                            ("Verify", "recheck, record, close or CAPA"),
                        ],
                    ),
                    1,
                    "The control path. Skipping confirmation or the legal gate is how a small biological problem becomes a batch problem.",
                ),
            ],
        }
    )

    sections.append(
        {
            "id": "ipm-system",
            "kicker": "02 · System",
            "title": "Six principles, four layers, one closed loop",
            "blocks": [
                p(
                    "IPM is a loop: prevent entry, monitor consistently, identify correctly, compare the "
                    "finding with a controlled threshold, combine compatible controls, then record and verify. "
                    "If the recheck fails, the loop runs again at a higher response level. The arthropod review "
                    "and the existing cannabis literature support layered indoor management rather than a single "
                    "calendar product" + _c("ahmed-2024-hemp-pests-florida-jipm") + "."
                ),
                figure(
                    L.flow(
                        "The IPM decision loop",
                        [
                            ("Prevent", "exclusion, sanitation, clean stock"),
                            ("Monitor", "fixed route, traps, roots, environment"),
                            ("Identify", "organism + life stage + source"),
                            ("Threshold", "risk + incidence + severity + trend"),
                            ("Control + verify", "layer tactics, recheck, record"),
                        ],
                    ),
                    2,
                    "Every intervention returns to monitoring. Without the recheck, it is activity rather than control.",
                ),
                table(
                    ["Layer", "Purpose", "Rule"],
                    [[name, body, "Build from this layer before moving upward"] for name, body in CONTROL_LAYERS],
                    cls="compact",
                    caption="The control pyramid in operating form. Chemical and reduced-risk inputs sit last, not because they never work, but because they carry the narrowest legal and compatibility envelope.",
                ),
                callout(
                    "key",
                    "Zero tolerance is not the same as eradication everywhere",
                    p(
                        "HLVd in clean stock, broad/russet mites in quarantine, root aphids in propagation, "
                        "powdery mildew on flowers and Botrytis inside a bud are exclusion or quality events. "
                        "A low fungus-gnat adult count in an established vegetative room may be a trend-management "
                        "problem. Use organism and room consequence, not one universal number."
                    ),
                ),
                table(
                    ["Severity", "Name", "Definition", "Default response"],
                    [[n, name, definition, "Monitor" if n == "0" else "Escalate by the approved decision matrix"] for n, name, definition in SEVERITY],
                    cls="compact",
                    caption="A site severity scale. Incidence, trend and zero-tolerance overrides still apply.",
                ),
            ],
        }
    )

    sections.append(
        {
            "id": "nz-legal-gate",
            "kicker": "03 · New Zealand gate",
            "title": "A control is not usable until the whole pathway is lawful",
            "blocks": [
                lead(
                    "New Zealand medicinal cannabis does not have one pest-rule book. The decision sits across "
                    "the medicinal-cannabis regulations and minimum quality standard, ACVM, HSNO/EPA controls, "
                    "WorkSafe, analytical release, and Auckland trade-waste/environmental requirements."
                ),
                p(
                    "Regulation 18 restricts pesticide treatment of cannabis crops, while Regulation 7 defines "
                    "residues that must be tested and their limits. The Ministry's current guidance distinguishes "
                    "inhalation from non-inhalation pathways and explicitly retains ACVM and HSNO obligations" +
                    _c("moh-nz-pesticide-use-2024") + _c("moh-nz-mqs-2026") + ". The presence of abamectin, "
                    "spinosad, pyrethrins or another analyte in a residue panel is not permission to apply it."
                ),
                p(
                    "Most agricultural compounds require ACVM registration; some product classes are exempt, "
                    "but the exemption conditions and other laws still apply" + _c("mpi-nz-acvm-exempt") + ". "
                    "EPA approvals and controls must be confirmed, including the approval information in section "
                    "15 of the current New Zealand SDS" + _c("epa-nz-hsno-approvals") + "."
                ),
                steps(LEGAL_GATES),
                callout(
                    "warn",
                    "Do not hard-code SKUs, rates, PHIs or REIs in a general paper",
                    p(
                        "Those values belong in the version-controlled approved-input register beside the current "
                        "label and SDS. WorkSafe says REIs vary by product, crop/use and exposure; off-label use "
                        "requires its own risk assessment. Indoor REI areas require signs and controlled entry" +
                        _c("worksafe-nz-rei") + "."
                    ),
                ),
                table(
                    ["Input class", "Planning position", "What still must be verified"],
                    [
                        ["Fatty-acid soaps / permitted salts", "Potential reduced-risk contact option", "Exact medicinal-cannabis pathway, product authority, crop site, residue/quality, PPE/REI"],
                        ["Sulphur", "Potential inhalation-capable active pathway", "Product authority, indoor exposure, crop-stage/quality limits, compatibility and current label"],
                        ["Hydrogen peroxide", "Potential active pathway for defined uses", "Crop contact vs line/surface sanitation, concentration, worker exposure, phytotoxicity and discharge route"],
                        ["Food / permitted food-additive actives", "Possible pathway only where every condition is met", "Novel-food/composition caveats, product ACVM/HSNO position, actual use and analytical route"],
                        ["Microbial actives", "Several named species/strains appear in the regulation pathway", "Exact species/strain/product, viable use, ACVM/HSNO status, non-target/beneficial effects and label"],
                        ["Conventional food-crop pesticide", "Not automatically inhalation-capable", "Whether a lawful non-inhalation or specific medicinal-cannabis pathway exists; residue calculation and testing"],
                        ["Beneficial organism", "Not the same as a pesticide active", "Current organism status, import/release route, supplier, cold chain, containment and facility compatibility"],
                    ],
                    cls="compact",
                    caption="A pathway screen, not a product recommendation. The approved-input register holds the current answer.",
                ),
                p(
                    "Testing of pesticides and other non-critical minimum-quality-standard attributes may be "
                    "performed by appropriately scoped GMP or ISO/IEC 17025:2017 laboratories, while critical "
                    "tests require GMP capability. Confirm the laboratory scope and method before relying on a "
                    "release plan" + _c("moh-nz-mqs-2026") + "."
                ),
            ],
        }
    )

    sections.append(
        {
            "id": "clean-stock",
            "kicker": "04 · Exclusion",
            "title": "Build the programme around clean stock, not rescue sprays",
            "blocks": [
                lead(
                    "The mother room is not just where clones come from. It is a source-material system. Its "
                    "failures multiply through every cutting, room and batch downstream."
                ),
                p(
                    "HLVd can be asymptomatic, moves efficiently with vegetative propagation and contaminated "
                    "tools, and research supports transmission risk through roots and recirculating hydroponic "
                    "solution" + _c("hlvd_threat2023") + _c("hlvd_mgmt2025") +
                    _c("hlvd-transmission-2025") + ". Visual health is therefore not a release test."
                ),
                figure(
                    L.flow(
                        "Genetics admission",
                        [
                            ("Receive", "approved source + accession ID"),
                            ("Quarantine", "separate air/water/tools/staff flow"),
                            ("Inspect + trap", "arthropods, roots, symptoms"),
                            ("Molecular index", "validated HLVd method and tissue"),
                            ("Promote or destroy", "trace tree begins before release"),
                        ],
                    ),
                    3,
                    "No genetics bypass quarantine, and no accession is promoted on appearance alone.",
                ),
                ul(
                    [
                        "Foundation mothers are created only from released material and retain the cleanest controls.",
                        "Production mothers, cutting lots and rooms inherit a traceable parent-child relationship.",
                        "Tools are sanitised between defined plant units, not merely at the end of the shift.",
                        "Quarantine, foundation stock and production stock do not share nutrient solution or unvalidated return water.",
                        "A positive or inconclusive test has a written hold, repeat, destruction and traceback rule before the first sample is collected.",
                    ]
                ),
                table(
                    ["Plant class", "Planning cadence", "Sampling rule", "Decision rule"],
                    [
                        ["Incoming accession", "At entry and again before promotion where risk warrants", "Individual plant; validated tissue/method", "No promotion until release criteria are met"],
                        ["Foundation mother", "At creation and risk-based recurring schedule", "Individual, no routine pooling unless validated", "Positive = destroy, hold linked daughters, investigate"],
                        ["Production mother", "Before major cutting campaigns or site-defined recurring schedule", "Individual or validated pool with reflex testing", "Positive = stop clone movement and trace since last verified negative"],
                        ["Clone lot", "Risk-based verification linked to mother status", "Lot-based plan with controls", "Hold linked rooms when source status is compromised"],
                        ["Hydro environment", "Investigation / sentinel use where system risk exists", "Tank, return, root interface under validated method", "Positive environmental signal triggers cohort investigation, not automatic plant diagnosis"],
                    ],
                    cls="compact",
                    caption="Planning cadence only. The controlled sampling plan must match the laboratory method, plant age, tissue, risk and facility history.",
                ),
                callout(
                    "danger",
                    "A monthly test is not protection if the genealogy is broken",
                    p(
                        "If you cannot identify every daughter lot since the last verified negative, a positive "
                        "mother turns into a building-wide guessing exercise. Build the trace tree first."
                    ),
                ),
            ],
        }
    )

    sections.append(
        {
            "id": "facility-pathways",
            "kicker": "05 · Contamination pathways",
            "title": "Control people, tools, air, water and waste as one system",
            "blocks": [
                p(
                    "Pests and pathogens do not care which department owns a vector. A clean-stock programme "
                    "fails if workers backtrack, scissors cross mothers, return air connects quarantine, or a "
                    "shared reservoir moves root pathogens. Cannabis disease reviews repeatedly identify stock, "
                    "tools, water, debris, density and environmental conditions as interacting routes" +
                    _c("punja-2021-emerging-diseases-cannabis") + "."
                ),
                figure(
                    L.flow(
                        "One-way hygiene gradient",
                        [
                            ("Clean support", "stores, clean PPE, released inputs"),
                            ("Foundation", "clean stock, restricted staff/tools"),
                            ("Production", "mothers, clones, veg, flower"),
                            ("Containment", "quarantine, suspect and treated areas"),
                            ("Waste exit", "bagged, logged, no return path"),
                        ],
                    ),
                    4,
                    "Movement normally goes clean to dirty. Any authorised backtracking requires full decontamination and a recorded exception.",
                ),
                grid(
                    [
                        card("People", "Room-class gowning, clean-to-dirty shift order, no unrecorded backtracking, treated-area controls and site-specific training records."),
                        card("Tools", "Room or plant-class ownership, verified sanitizer concentration/contact time, between-unit rules and a clean/dirty state that is obvious."),
                        card("Air", "Quarantine separation, pressure intent, filtered supply, no shared contaminated return, canopy/dead-zone mapping and condensation checks."),
                        card("Water", "Segregated tanks/circuits where consequence demands it, no unvalidated recirculation, biofilm control, drain mapping and backflow prevention."),
                        card("Plant/material", "Approved sources, sealed waste, clean media/pots, controlled beneficial receipt and no cardboard/packaging wandering through clean rooms."),
                        card("Waste", "Bag and log crop waste in the room; contain rinse/spill liquids; use approved disposal and trade-waste pathways, never stormwater."),
                    ],
                    cols=2,
                ),
                p(
                    "Watercare requires a trade-waste agreement when a business discharge is not low risk, with "
                    "site controls and monitoring defined by the agreement" + _c("watercare-nz-trade-waste") + ". "
                    "Auckland's E33 framework prioritises avoiding contaminant discharge and requires appropriate "
                    "onsite management, containment, treatment or lawful disposal" +
                    _c("auckland-unitary-plan-e33") + ". Site address, drainage and activity classification remain facility inputs."
                ),
            ],
        }
    )

    sections.append(
        {
            "id": "cultural-environmental",
            "kicker": "06 · Prevention",
            "title": "Cultural and environmental controls do the heavy lifting",
            "blocks": [
                p(
                    "The quiet controls are the ones that scale: eliminate weeds, algae and plant debris; keep "
                    "doors/screens/barriers functional; quarantine every genetic source; use one-way work; maintain "
                    "a fixed scouting route; and commission root-zone and canopy conditions. They reduce both the "
                    "chance of entry and the rate of spread after entry."
                ),
                table(
                    ["Control point", "Minimum check", "Failure signal", "Correction"],
                    [
                        ["Exterior/interior reservoirs", "Weeds, algae, drains, debris and standing water", "Repeated small-fly pressure or pest reservoirs", "Remove source, repair drainage/leaks, clean and verify"],
                        ["Sanitizer", "Product, concentration, contact time, surface cleanliness", "No concentration record, dirty surface or premature wipe-off", "Remix, pre-clean, repeat full contact time"],
                        ["Canopy air", "Representative airspeed/dead zones and leaf movement", "Still dense pockets, condensation or repeated Botrytis/PM zone", "Rebalance fans/HVAC and canopy density"],
                        ["Night transition", "Leaf/surface temperature, RH, dew-point margin", "Condensation or a narrow margin during lights-off", "Change humidity removal, air movement, temperature ramp and irrigation timing"],
                        ["Root zone", "Temperature, DO where relevant, moisture pattern, drain, biofilm/algae", "Warm saturated roots, poor drainage, sloughing or shared-cohort symptoms", "Correct irrigation/oxygen/heat, isolate and diagnose"],
                        ["Sticky cards", "ID, colour, height, date, clean readable surface", "Unmapped cards or counts without position/history", "Replace, map and standardise reading"],
                    ],
                    cls="compact",
                    caption="Prevention checks must produce an observable pass/fail, not a vague instruction to keep the room clean.",
                ),
                callout(
                    "note",
                    "Room RH is not the leaf microclimate",
                    p(
                        "Dense canopy, cold surfaces, irrigation timing and lights-off transitions can create wet "
                        "or near-condensing tissue while the wall sensor looks acceptable. Commission the actual "
                        "risk locations and record the correction trigger."
                    ),
                ),
                figure(
                    L.flow(
                        "Weekly scouting route",
                        [
                            ("Prepare", "clean kit, map, prior trends, room order"),
                            ("Trap line", "read IDs, preserve unknowns, replace"),
                            ("Plant line", "top, underside, meristem, stem, flower"),
                            ("Root line", "media, crown, drain, roots where sampled"),
                            ("Close", "photos, samples, threshold, owner, recheck"),
                        ],
                    ),
                    5,
                    "Same route, same points, same plant parts. Consistency makes trend data comparable.",
                ),
            ],
        }
    )

    sections.append(
        {
            "id": "biological-controls",
            "kicker": "07 · Living controls",
            "title": "Biological control is a managed population, not a box of good bugs",
            "blocks": [
                p(
                    "A biological programme succeeds when the right organism arrives alive, is released into a "
                    "suitable crop and climate, survives existing residues, finds the target stage, establishes "
                    "where needed and is verified. Generalist and specialist predators are not interchangeable; "
                    "neither are aphid or whitefly parasitoids" + _c("lopez-2023-amblyseius-swirskii-review-jipm") +
                    _c("vanmaanen-2010-broad-mite-swirskii-biocontrol") + "."
                ),
                table(
                    ["Control group", "Typical role", "Release-plan checks"],
                    BENEFICIAL_ROWS,
                    cls="compact",
                    caption="Functional groups only. Verify current New Zealand organism status, supplier availability and product law before naming a deployable agent.",
                ),
                steps(
                    [
                        ("Approve", "Confirm organism/product identity, NZ legal status, supplier, compatibility and target stage."),
                        ("Receive", "Record lot, arrival time/temperature, packaging condition and expiry/use window."),
                        ("Verify viability", "Use the supplier method to check movement, counts, nematode survival or microbial condition; reject failed material."),
                        ("Release", "Map rate and location against crop stage, pest distribution and environmental conditions."),
                        ("Establish", "Check predators, parasitised hosts/mummies, prey-stage decline or other defined evidence."),
                        ("Correct", "If establishment fails, find whether the cause was dead stock, wrong species/stage, climate, residues, timing or application."),
                    ]
                ),
                p(
                    "Imported invertebrates require species eligibility, permits/facilities where applicable and "
                    "biosecurity/HSNO compliance. Do not turn a global supplier catalogue into an NZ release list" +
                    _c("mpi-nz-invertebrate-import") + "."
                ),
            ],
        }
    )

    sections.append(
        {
            "id": "input-application",
            "kicker": "08 · Controlled exception",
            "title": "Select and apply inputs without creating the next failure",
            "blocks": [
                p(
                    "Once a finding crosses threshold, select the fewest controls that cover the confirmed "
                    "organism, life stage and plant part without breaking law, worker safety, beneficials or "
                    "release. Rotate IRAC/FRAC modes where relevant; physical modes and living controls still need "
                    "compatibility planning."
                ),
                table(
                    ["Mode", "What it does", "Common failure"],
                    [
                        ["Contact kill", "Acts only where spray reaches the organism", "Poor underside/flower coverage or protected life stages"],
                        ["Smothering/desiccation", "Disrupts soft-bodied pests physically", "Crop-stage injury, incomplete coverage or incompatibility"],
                        ["Microbial insect pathogen", "Infects susceptible pest stage under suitable conditions", "Wrong stage, low viability, unsuitable humidity or incompatible residue"],
                        ["Predator/parasitoid", "Consumes or develops in a target pest", "Released too late, wrong host, dead arrival or no establishment"],
                        ["Root-zone antagonist", "Suppresses pathogen establishment/pressure", "Asked to cure dead roots or mixed with a sanitiser that kills it"],
                        ["Oxidation/sanitation", "Reduces contamination on the validated use site", "Assuming line/surface sanitation rate is safe or effective on living crop"],
                        ["Environmental correction", "Removes a condition supporting the problem", "Treating room average while the microclimate remains wrong"],
                    ],
                    cls="compact",
                    caption="Product-agnostic modes. The actual product, use site and rate come from the controlled register and current label/SDS.",
                ),
                callout(
                    "warn",
                    "Application quality is part of efficacy",
                    p(
                        "Calibrate output, check water and mixing order, verify agitation, select nozzle/pressure, "
                        "define target coverage, manage lights/HVAC, contain runoff, clean equipment, post REI "
                        "signage and perform a phytotoxicity test patch when the approved SOP requires it. A legal "
                        "product applied badly is still a failed treatment."
                    ),
                ),
                table(
                    ["Approved-input register field", "Required"],
                    [[field, "Yes"] for field in APPROVED_TOOL_FIELDS],
                    cls="compact",
                    caption="Do not release an input to stores until every applicable field is complete and approved.",
                ),
            ],
        }
    )

    arthropods = [entry for entry in ATLAS if entry["kind"] == "arthropod"]
    sections.append(
        {
            "id": "arthropod-atlas",
            "kicker": "09 · Field atlas",
            "title": "Arthropods: identify the organism and the life stage",
            "blocks": [
                lead(
                    "The plate is the start of the diagnosis. Confirm morphology, sample the right plant part, "
                    "separate lookalikes, then choose controls that reach the actual life stage."
                ),
                p(
                    "Cannabis supports diverse piercing/sucking and root-zone pests; primary reviews emphasise "
                    "that indoor management depends on accurate identification, life cycle and plant location" +
                    _c("ahmed-2024-hemp-pests-florida-jipm") +
                    _c("pulkoski-burrack-2023-piercing-sucking-hemp") + "."
                ),
            ]
            + [_atlas_profile(entry, i + 1) for i, entry in enumerate(arthropods)],
        }
    )

    diseases = [entry for entry in ATLAS if entry["kind"] == "disease"]
    sections.append(
        {
            "id": "disease-atlas",
            "kicker": "10 · Field atlas",
            "title": "Diseases: symptoms point to the sample, not the answer",
            "blocks": [
                lead(
                    "Disease symptoms overlap. Use them to choose tissue, environmental records and the right "
                    "laboratory route. Do not convert a picture match into a release decision."
                ),
                p(
                    "Cannabis disease literature supports distinct management for powdery mildew, Botrytis, "
                    "Pythium, Fusarium and systemic propagation threats" +
                    _c("scott-punja-2021-powdery-mildew-management") +
                    _c("mahmoud-2023-botrytis-budrot") +
                    _c("punja-2023-fusarium-pythium-biocontrol") + ". Septoria diagnosis is complicated by "
                    "closely related species and requires more than lesion colour" +
                    _c("rahnama-2021-septoria-cannabis") + _c("ujata-2024-septoria-cannabicola") + "."
                ),
            ]
            + [_atlas_profile(entry, i + 1) for i, entry in enumerate(diseases)],
        }
    )

    sections.append(
        {
            "id": "lookalikes",
            "kicker": "11 · Diagnostic controls",
            "title": "Healthy references and the lookalikes that waste treatments",
            "blocks": [
                p(
                    "A diagnostic atlas without healthy controls trains people to see disease everywhere. Compare "
                    "like with like: underside to underside, opened flower to opened flower, new meristem to new "
                    "meristem, and roots at the same age and substrate."
                ),
                term_gallery(REFERENCE_PLATES, "OpenAI image generation"),
                table(
                    ["Confusion", "Separating feature", "Next step"],
                    [
                        ["Fungus gnat adult vs winged root aphid", "Gnat has fly-like legs/antennae and wing venation; aphid has pear-shaped body and cornicles", "Preserve low-card specimen and use microscopy"],
                        ["Broad/russet mites vs heat/light tacoing", "Mites/eggs on sampled leading edge; abiotic stress follows exposure pattern without organisms", "Microscope multiple tips before changing feed or climate"],
                        ["Powdery mildew vs dried foliar residue", "PM forms raised growing colonies and fungal structures; residue follows droplets/rings and spray history", "Angled light, microscopy or lab if flower disposition depends on it"],
                        ["Pythium vs abiotic root stress", "Water-soaked sloughing and linked disease pattern vs dry/tan stressed roots without pathogen proof", "Sample roots/water before sanitation and send to a diagnostic lab"],
                        ["HLVd vs everything that stunts", "No visual feature is confirmatory", "RT-qPCR/RT-PCR with traceable sample and controls"],
                    ],
                    cls="compact",
                    caption="The generated comparison plates are training aids, not reference specimens.",
                ),
            ],
        }
    )

    sections.append(
        {
            "id": "build-programme",
            "kicker": "12 · Runtime",
            "title": "Turn findings into a controlled weekly programme",
            "blocks": [
                steps(
                    [
                        ("Score consequence", "Room class, clean-stock status, target organism, crop stage and product-quality consequence."),
                        ("Measure pressure", "Incidence, severity 0-4, life stages, spatial pattern, trap/root/lab trend and beneficial density."),
                        ("Apply override", "Zero-tolerance findings bypass a numeric threshold and move directly to containment."),
                        ("Find the source", "Incoming stock, staff/tool movement, air, water, media, packaging, weeds/algae or crop carryover."),
                        ("Select layers", "Cultural and environmental correction, then compatible biological and lawful input options."),
                        ("Schedule", "Target life stage, application/release date, room controls, mode rotation, recheck date and stop/escalate rule."),
                        ("Verify", "Measure live organisms/new lesions/new growth, establishment, injury, residue implication and recurrence."),
                        ("Close or CAPA", "Close only when the success criterion is met; otherwise revise cause and escalate."),
                    ]
                ),
                table(
                    ["Weekly meeting input", "Decision output"],
                    [
                        ["Trap and scouting trends", "Room/zone action, owner and recheck"],
                        ["HLVd/pathogen results", "Release, hold, repeat, destroy and trace decision"],
                        ["Beneficial receipt/release/establishment", "Continue, supplement, replace or investigate incompatibility"],
                        ["Environmental and root-zone excursions", "Engineering/cultural correction with due date"],
                        ["Input applications and treated-area status", "REI release, efficacy check and residue review"],
                        ["Open CAPA and linked batches", "Containment status, evidence gap, quality disposition and effectiveness check"],
                    ],
                    cls="compact",
                    caption="The weekly meeting produces room-specific actions, not a narrative report nobody uses.",
                ),
                h(3, "Control-strategy decision worksheet"),
                table(
                    ["Decision field", "Controlled entry"],
                    [
                        ["Confirmed target, life stage and plant part", "FACILITY INPUT"],
                        ["Current pressure: incidence, severity, trend and distribution", "FACILITY INPUT"],
                        ["Source/pathway hypothesis and evidence", "FACILITY INPUT"],
                        ["Cultural and environmental corrections", "FACILITY INPUT"],
                        ["Biological option, establishment evidence and compatibility", "FACILITY INPUT"],
                        ["Input option, legal gate, mode group and residue route", "FACILITY INPUT"],
                        ["Crop/worker constraints, REI and treated-area release", "FACILITY INPUT"],
                        ["Owner, action date, recheck date, success and stop/escalate rule", "FACILITY INPUT"],
                    ],
                    cls="compact",
                    caption="Complete against the current approved-input and beneficial registers; product names and rates do not belong in an uncontrolled paper.",
                ),
                h(3, "Dated intervention and beneficial-release planner"),
                table(
                    ["Date/time", "Room/zone", "Target stage", "Action or release", "Mode / organism", "Compatibility and REI", "Recheck"],
                    [["FACILITY INPUT"] * 7 for _ in range(4)],
                    cls="compact",
                    caption="Use enough rows to cover the target's condition-dependent development window; revise after each recheck.",
                ),
                h(3, "Target-by-approved-tool matrix"),
                table(
                    ["Target", "Currently approved tool", "Target stage/site", "Evidence grade/source", "Legal verification date", "Compatibility", "Success measure"],
                    [["FACILITY INPUT"] * 7 for _ in range(3)],
                    cls="compact",
                    caption="A planning interface to the controlled registers, not a substitute for them.",
                ),
                figure(
                    L.flow(
                        "Finding to closure",
                        [
                            ("Confirm", "organism, life stage, location"),
                            ("Contain", "movement, plants, water, treated area"),
                            ("Control", "layered lawful plan"),
                            ("Recheck", "defined evidence and date"),
                            ("Close / CAPA", "criterion met or root cause revised"),
                        ],
                    ),
                    6,
                    "The minimum operational record for every threshold-triggering event.",
                ),
            ],
        }
    )

    sections.append(
        {
            "id": "crop-cycle",
            "kicker": "13 · Crop cycle",
            "title": "Operate from receiving through release, not room by room in isolation",
            "blocks": [
                table(
                    ["Stage", "Daily standard work", "Weekly / scheduled work", "Hard decision"],
                    [
                        ["Receiving / quarantine", "Accession, source/legal check, visual/root inspection, dedicated tools and waste", "Traps, HLVd/pathogen plan, reassessment", "Promote only when legal and biological release criteria are met"],
                        ["Foundation / production mothers", "Health walk, tool control, irrigation and environment", "Molecular schedule, full scout, pruning-hygiene audit", "Positive HLVd or systemic/high-consequence pest = stop, hold, trace"],
                        ["Cuttings / rooting", "Sanitary cutting, humidity/airflow, dead cutting and root review", "Root development, traps, fungus/root-disease check", "Patterned failure triggers source, water and diagnostic investigation"],
                        ["Vegetative", "Environment/root-zone review and visible pest walk", "Full scout, cards, biological release/establishment", "Single high-risk hotspot or rising trend triggers targeted action"],
                        ["Flower", "Climate/dew-point/air movement and dense-canopy inspection", "Full scout, late-flower destructive bud checks by risk, residue/use review", "Any PM on flowers or Botrytis in a bud is immediate action"],
                        ["Harvest / dry / hold", "Hygienic handling, waste segregation, dry-room condition and mould checks", "Residue/microbial/foreign-matter sampling and deviation review", "Release, continue hold, remediate if lawful/validated, or reject"],
                    ],
                    cls="compact",
                    caption="A complete crop-cycle control model. Exact timing follows cultivar, facility and approved production plan.",
                ),
                callout(
                    "key",
                    "Post-harvest is still IPM",
                    p(
                        "Contaminated tools, slow or uneven drying, dense uninspected flowers and dirty processing "
                        "equipment can erase a clean cultivation run. Product remains on hold until the required "
                        "quality evidence and deviation review are complete."
                    ),
                ),
            ],
        }
    )

    sections.append(
        {
            "id": "capa-release",
            "kicker": "14 · Quality system",
            "title": "Contain the crop, then investigate the system",
            "blocks": [
                p(
                    "Classify events as local, room-wide or systemic. Containment comes first; root cause and "
                    "batch impact follow while evidence is preserved. CAPA is incomplete until the effectiveness "
                    "check proves the change worked."
                ),
                table(
                    ["Event", "Immediate containment", "Batch/crop assessment", "CAPA focus"],
                    [
                        ["HLVd-positive mother", "Stop clone movement, isolate/bag under SOP, hold linked daughters", "All daughter lots since last verified negative plus connected tools/water", "Source, test cadence, sample integrity, tool sanitation, hydro segregation and traceability"],
                        ["Powdery mildew on flower", "Isolate zone/room, bag affected tissue, intensify scouting", "Extent, crop stage, lawful options, residue and market disposition", "Night microclimate, density, airflow, scouting sensitivity and programme compatibility"],
                        ["Botrytis inside flower", "Controlled removal without spore spread, inspect neighbours", "Lot hold/extent, cultivar/zone pattern, environmental history", "Humidity removal, condensation, flower architecture, handling injury and debris"],
                        ["Root disease linked to shared water", "Isolate circuit, stop transfer, sample before sanitation", "All connected cohorts and source stock", "Reservoir/return design, biofilm, temperature/DO, cleaning validation and water segregation"],
                        ["Worker enters during REI", "Remove worker, exposure response, secure area/signage", "Assess crop contact/contamination and treatment status", "Lockout, sign placement, training, supervision and access control"],
                    ],
                    cls="compact",
                    caption="CAPA joins biological cause, worker/system cause and product-quality consequence.",
                ),
                ol(
                    [
                        "<strong>Release:</strong> required analytical results, treatment history, traceability and deviation review are satisfactory.",
                        "<strong>Continue hold:</strong> result, investigation, repeat sample or linked-lot status is incomplete.",
                        "<strong>Reject or validated remediation:</strong> the lot fails a limit, has an indefensible treatment history, or is linked to a systemic contamination failure. Remediation is not a substitute for prevention.",
                    ]
                ),
            ],
        }
    )

    sections.append(
        {
            "id": "controlled-toolkit",
            "kicker": "15 · Working tools",
            "title": "The forms must make the right action easier than the shortcut",
            "blocks": [
                h(3, "Facility approval sheet"),
                "<style>.facility-input{display:grid;gap:6px}.facility-input input,.facility-input textarea{width:100%;padding:10px;border:1px solid var(--line);border-radius:6px;background:var(--paper);color:var(--ink);font:inherit}.facility-form{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}.facility-input.wide{grid-column:1/-1}@media(max-width:720px){.facility-form{grid-template-columns:1fr}}</style>",
                "<form class='facility-form'>"
                + _input("site_address", "Facility address / Auckland zone")
                + _input("licence_scope", "Licence and intended product lines")
                + _input("room_map", "Controlled room-map revision")
                + _input("quality_owner", "Quality/IPM approver")
                + _input("diagnostic_lab", "Approved diagnostic laboratory and scope")
                + _input("release_lab", "Release laboratory and pesticide method/LOQ")
                + _input("watercare_status", "Trade-waste classification / agreement")
                + _input("review_date", "Document review date")
                + _input("sampling_density", "Controlled scouting density / representative-site method and rationale", True)
                + _input("zero_tolerance", "Site zero-tolerance organisms and room classes", True)
                + _input("thresholds", "Controlled numeric/trend thresholds and evidence source", True)
                + "</form>",
                h(3, "Weekly scouting record"),
                table(
                    ["Required field", "Entry"],
                    [[field, "FACILITY INPUT"] for field in SCOUT_FIELDS]
                    + [["Planned sites, completed sites and missed/inaccessible-site exception", "FACILITY INPUT"]],
                    cls="compact",
                    caption="Use one row/set per mapped site or exception. Unknown organisms receive a specimen/photo reference, not a guessed name.",
                ),
                h(3, "Quarantine and clean-to-dirty movement log"),
                table(
                    ["Date/time", "Person or material", "From", "To", "Release/status evidence", "PPE/tool change", "Exception approval"],
                    [["FACILITY INPUT"] * 7 for _ in range(4)],
                    cls="compact",
                    caption="Record every accession transfer and every authorised backtrack across the hygiene gradient.",
                ),
                h(3, "Beneficial release and establishment record"),
                table(
                    ["Field", "Entry"],
                    [
                        ["Species/strain, supplier and lot", "FACILITY INPUT"],
                        ["NZ legal-status evidence and approval date", "FACILITY INPUT"],
                        ["Arrival time, temperature and condition", "FACILITY INPUT"],
                        ["Viability/count check and rejection decision", "FACILITY INPUT"],
                        ["Target pest/stage, room map and release rate", "FACILITY INPUT"],
                        ["Climate and incompatible residue review", "FACILITY INPUT"],
                        ["Establishment/recheck date and evidence", "FACILITY INPUT"],
                        ["Corrective action or close-out", "FACILITY INPUT"],
                    ],
                    cls="compact",
                ),
                h(3, "Spray / application quality checklist"),
                table(
                    ["Check", "Controlled entry"],
                    [
                        ["Event ID; approved product/lot; target; room/zone; crop stage", "FACILITY INPUT"],
                        ["Current label/SDS, medicinal-cannabis, ACVM and HSNO evidence checked", "FACILITY INPUT"],
                        ["Applicator, calibration, output, nozzle/pressure and target coverage", "FACILITY INPUT"],
                        ["Water quality, mixing order, agitation and prepared volume", "FACILITY INPUT"],
                        ["HVAC/lights controls, containment, weather/external-discharge risk", "FACILITY INPUT"],
                        ["PPE, signage, access control, REI start/end and treated-area release", "FACILITY INPUT"],
                        ["Unused mix, rinse, spill/waste disposition and equipment clean-down", "FACILITY INPUT"],
                        ["Phytotoxicity, efficacy and residue recheck dates / results", "FACILITY INPUT"],
                    ],
                    cls="compact",
                ),
                h(3, "Outbreak, batch-impact and CAPA record"),
                table(
                    ["Field", "Entry"],
                    [
                        ["Event ID, first detection and detector", "FACILITY INPUT"],
                        ["Confirmed organism / evidence / uncertainty", "FACILITY INPUT"],
                        ["Room, zone, plants, mothers, clone lots and batches", "FACILITY INPUT"],
                        ["Linked staff, tools, air, water, media and input lots", "FACILITY INPUT"],
                        ["Immediate containment and treated-area controls", "FACILITY INPUT"],
                        ["Product-quality and residue impact assessment", "FACILITY INPUT"],
                        ["Hold, destruction, remediation or release decision", "FACILITY INPUT"],
                        ["Root cause and contributing conditions", "FACILITY INPUT"],
                        ["Corrective and preventive actions, owners and dates", "FACILITY INPUT"],
                        ["Effectiveness evidence and quality close-out", "FACILITY INPUT"],
                    ],
                    cls="compact",
                ),
                h(3, "Population-trend dashboard worksheet"),
                table(
                    ["Week/date", "Room/zone", "Target", "Trap or sampled units", "Live count / incidence", "Severity 0-4", "Beneficial density", "Action line", "Decision"],
                    [["FACILITY INPUT"] * 9 for _ in range(5)],
                    cls="compact",
                    caption="Graph or trend these same controlled fields in the site's validated record system; record denominator and missed sites so the line means something.",
                ),
                h(3, "Spill and waste control"),
                ul(
                    [
                        "Current drain map distinguishes sanitary sewer/trade waste from stormwater.",
                        "Secondary containment and spill kits match the stored substances and credible spill volume.",
                        "No pesticide, sanitiser, nutrient concentrate, contaminated rinse water or spill enters stormwater.",
                        "Watercare and Auckland pollution-response triggers are posted and trained.",
                        "Waste contractors and disposal records are current; annual drill findings enter CAPA.",
                    ]
                ),
            ],
        }
    )

    sections.append(
        {
            "id": "training",
            "kicker": "16 · Competency",
            "title": "Attendance is not competence",
            "blocks": [
                table(
                    ["Module", "Audience", "Demonstrated outcome"],
                    [
                        ["NZ medicinal-cannabis input gate", "QA, procurement, IPM/cultivation leads", "Reject or approve a candidate input with the correct evidence trail"],
                        ["Hygiene zoning and movement", "All cultivation, sanitation, maintenance and contractors", "Execute room order, tool/PPE changes and exception process"],
                        ["Scouting and specimen handling", "Scouts and room leads", "Follow fixed route, identify plant parts, record incidence/severity, preserve unknown"],
                        ["Mother stock and HLVd", "Nursery, mother and QA staff", "Collect traceable sample, place hold, trace daughters and execute positive response"],
                        ["Beneficial control", "IPM team and receiving", "Verify delivery, viability, release map, compatibility and establishment"],
                        ["Application, REI and PPE", "Applicators, supervisors, QA/EHS", "Calibrate, mix, apply, contain waste, post signs and release treated area"],
                        ["CAPA and batch impact", "QA, cultivation management, IPM lead", "Run mock event from containment through effectiveness check"],
                    ],
                    cls="compact",
                    caption="WorkSafe requires site-specific information, instruction, training and records; a prior course does not remove the site's duty" + _c("worksafe-nz-hs-training") + ".",
                ),
                callout(
                    "note",
                    "Drill the ugly events",
                    p(
                        "Run at least: HLVd-positive mother, Botrytis cluster in late flower, root disease on a "
                        "shared circuit, unlawful input discovered after application, REI entry breach and a spill "
                        "threatening a drain. A plan only earns trust after someone has tried to use it under pressure."
                    ),
                ),
            ],
        }
    )

    sections.append(
        {
            "id": "glossary",
            "kicker": "17 · Reference",
            "title": "Glossary",
            "blocks": [
                p("The biological, diagnostic, operational and New Zealand regulatory terms used in this blueprint."),
                grid([defterm(term, definition) for term, definition in GLOSSARY], cols=2),
            ],
        }
    )

    sections.append(
        {
            "id": "revision-register",
            "kicker": "18 · Governance",
            "title": "Evidence and revision register",
            "blocks": [
                table(
                    ["Claim class", "Minimum evidence", "Review trigger"],
                    [
                        ["NZ legal / regulatory", "Current official Ministry, MPI, EPA, WorkSafe, Watercare or Auckland source", "Any law/guidance revision, new product/organism, annual review"],
                        ["Pest/disease biology", "Primary paper or strong technical review; species caveat", "New diagnostic result, organism not behaving as assumed"],
                        ["Product/organism status", "Current register/approval, label, SDS, supplier and site approval", "Every purchase/use and any document revision"],
                        ["Facility threshold", "Site history, risk rationale and quality approval", "Trend miss, crop loss, false alarm, process or market change"],
                        ["Operational setpoint", "Named facility SOP/validation and measured data", "Equipment, cultivar, room, substrate or process change"],
                        ["Generated image", "Final prompt, generation tool, human diagnostic review and disclosure", "Morphology error, confusion in training or better verified reference"],
                    ],
                    cls="compact",
                    caption="This blueprint is controlled guidance, not a frozen truth. Review the volatile parts before the static prose.",
                ),
                callout(
                    "key",
                    "Implementation judgement",
                    p(
                        "The resilient programme is the one that keeps unlawful inputs out, infected genetics out, "
                        "water and air from becoming transport systems, staff movement legible, and release logic "
                        "visible at the moment a control is chosen. Everything else is decoration."
                    ),
                ),
            ],
        }
    )

    return sections
