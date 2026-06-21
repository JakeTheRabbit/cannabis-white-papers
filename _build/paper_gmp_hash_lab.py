# -*- coding: utf-8 -*-
"""Paper: GMP hash manufacturing, facility flow and quality control (beginner)."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        stagecard, grid, card, chip, kv, steps)
import figs_lib as L

SLUG = "gmp-hash-lab"
TITLE = "GMP hash manufacturing: facility flow and quality control"
EYEBROW = "Facility · GMP"
SUB = ("How to design a clean, compliant hash and extract factory from scratch: what GMP "
       "means, how rooms and people and product move, and how a batch earns its way to market.")
META = [("building", "Facility"), ("image", "13 diagrams"),
        ("quote", "Peer-reviewed · 8 sources"), ("clock", "~18 min read")]
RELATED = ["mould-risk", "wso-quality-manual", "facility-3d"]
REF_IDS = ["ecfr-21cfr211", "ich-q3c-r9-ema", "ehp-cannabis-contaminants-2019",
           "en1822-h14-hepa", "sciencedirect-cleanroom-personnel-emissions-2024",
           "pmc-capa-ich-q10-2024", "fda-process-validation-2011",
           "ispe-cleanroom-design-iso14644-16"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

SECTIONS.append({"id": "what-this-is", "kicker": "Start here", "title": "What This Is: GMP and the Hash Lab From Zero",
  "blocks": [
    lead("GMP stands for <strong>Good Manufacturing Practice</strong>: a written, audited "
         "system that proves a product is exactly what its label says and that nothing harmful rode "
         "along. A GMP hash lab turns cannabis biomass into purified resin concentrates (bubble hash, "
         "rosin, live resin, distillate) under tight contamination control."),
    p("The same physics that concentrate the cannabinoids you want also "
      "concentrate the contaminants you don't. Extraction multiplies both the good and the bad "
      "roughly five- to ten-fold" + _c("ehp-cannabis-contaminants-2019") + ", so a pesticide or mould "
      "level that looked fine on the raw flower can fail badly once it is squeezed into a gram of "
      "resin. Every step in the building is designed to answer one question: <em>can we prove this "
      "material is safe and correctly labelled?</em> If yes, it moves forward. If not, it holds."),
    p("Two rule-sets do most of the governing. <strong>EU-GMP Annex 1</strong> sets the cleanroom "
      "classifications and the contamination-control strategy, and the U.S. <strong>cGMP rules in 21 "
      "CFR 210/211</strong> set the production controls, the records, and the authority of the quality "
      "unit to release product" + _c("ecfr-21cfr211") + ". This paper is a reference architecture, not "
      "legal advice. The exact limits and grades vary by jurisdiction."),
    callout("key", "The one rule under all the others",
      p("&lsquo;If it isn't written down, it didn't happen.&rsquo; GMP is a documented, validated, "
        "inspectable system. A spotless room with no records fails an audit. A modest room with "
        "complete, signed records passes.")),
    figure(L.bars("The four headline numbers this design hits",
            [("Cleanliness grades", 5), ("Release-test families", 7), ("Genealogy coverage", 100),
             ("Critical deviations at release", 0)], unit="",
            note="Anchor stats: 5 grades, 7 mandatory test families, 100% batch traceability, zero open critical deviations.",
            maxv=110), 1,
      "Four numbers anchor the whole facility: five cleanliness grades, seven mandatory release-test "
      "families, full genealogy coverage, and zero open critical deviations permitted at the point of "
      "release."),
    table(["Standard", "What it covers", "Facility area it governs"], [
      ["EU-GMP Annex 1", "Cleanroom classification & contamination-control strategy", "All classified rooms"],
      ["cGMP 21 CFR 210/211", "Production controls, records, QC-unit release authority", "Whole plant + QA"],
      ["ICH Q7 / Q9 / Q10", "Quality system, risk management, lifecycle", "Quality management system"],
      ["ISO 14644-1", "Cleanroom particle-count classes (ISO 5/7/8)", "Air classification"],
      ["GACP", "Good Agricultural & Collection Practice for biomass", "Goods-in / intake"],
      ["NFPA 30 / C1D1", "Flammable liquids & classified electrical areas", "Solvent extraction room"],
    ], cls="compact", caption="The governing standards and which part of the building each one rules."),
  ]})

SECTIONS.append({"id": "key-terms", "kicker": "Vocabulary", "title": "Key Terms: The Words You Need First",
  "blocks": [
    p("A handful of terms do the heavy lifting before any diagram makes sense. You don't need to memorise them: "
      "each comes back in context."),
    defterm("Cleanroom grade", "A letter (CNC, D, C, B, A) describing how clean a room's air is, "
            "mapped to ISO 14644 particle classes. Grade C = ISO 7, Grade A = ISO 5."),
    defterm("Batch / lot", "One defined production run with a single lot ID. Everything that happens "
            "to it is recorded against that ID. That record is its genealogy."),
    defterm("Deviation", "Any departure from the approved process. Every deviation is logged, "
            "investigated, and closed before the affected batch can be released."),
    defterm("CAPA", "Corrective And Preventive Action: the loop that fixes the immediate "
            "problem (corrective) and stops it recurring (preventive)."),
    defterm("Quarantine / Released / Rejected", "The three exclusive status states every material "
            "sits in. Nothing is &lsquo;in between&rsquo;. Status is always one of these three."),
    defterm("CCP (Critical Control Point)", "A step where a measured limit prevents a hazard "
            "(HACCP language). One example: wash water below 4&nbsp;&deg;C."),
    defterm("ALCOA+", "What a good record must be: Attributable, Legible, Contemporaneous, Original, "
            "Accurate, plus Complete, Consistent, Enduring, Available."),
    defterm("Water activity (Aw)", "Free water available to microbes, on a 0&ndash;1 scale. Keeping "
            "it low starves mould and bacteria. CoA = Certificate of Analysis. C1D1 = a "
            "flammable-rated room."),
    p("QA, the Quality Assurance function, owns the final release decision, and QA is independent of "
      "production" + _c("ecfr-21cfr211") + ". That separation is the spine "
      "of the whole system: the people paid to ship product never get to sign off their own work."),
    figure(L.flow("Status a batch can be in",
            [("Quarantine", "received, not yet judged"), ("Released", "passed all gates, shippable"),
             ("Rejected", "failed; off to disposition")],
            note="Every lot sits in exactly one of these three states at all times."), 2,
      "The three exclusive status states. Physical location and computer status must always agree."),
  ]})

SECTIONS.append({"id": "zoning", "kicker": "Core concept", "title": "Zoning and Cleanroom Grades: Nested Shells",
  "blocks": [
    p("The building is a set of nested cleanliness shells, like the layers of an onion. The "
      "<strong>dirty</strong> operations, intake, milling and waste, sit at the outer "
      "perimeter. The <strong>cleanest</strong> operations, collection, filling and packaging "
      "of open product, sit at the protected core."),
    p("The flow rule is simple and absolute: <strong>product moves inward toward purity; people and "
      "waste move outward toward the dirty edge, and the two never cross uncontrolled.</strong> Each "
      "shell boundary is an airlock plus a one-grade cleanliness step. Under EU-GMP Annex 1, Grade C "
      "corresponds to ISO 7 and Grade A to ISO 5" + _c("ispe-cleanroom-design-iso14644-16") + ". Most "
      "recreational and medical hash operations run a D-to-C envelope and treat the fill point as "
      "Grade C with local protection. Full Grade A/B is only needed for sterile or "
      "pharma-grade dose forms."),
    figure(L.zones("Nested cleanliness shells (outer = dirty, inner = clean)",
            0, 4, [(0, 1, L.REDL, "CNC intake"), (1, 2, L.AMBL, "Grade D"),
                   (2, 3, L.GL, "Grade C"), (3, 4, L.GXL, "Grade A core")],
            unit="", note="Product flows inward to the clean core; people and waste flow outward to the dirty edge."), 3,
      "Concentric zoning from the CNC outer shell through Grade D and C to the clean core. Inward = "
      "product to purity; outward = personnel and waste to the dirty edge."),
    figure(L.bars("Air changes per hour climb with cleanliness",
            [("CNC", 5), ("Grade D", 15), ("Grade C", 30), ("Grade A", 240)], unit=" ACH",
            note="Cleaner rooms flush their air far more often. Recommended ISO 7 rates are ~20-40 ACH.",
            maxv=270), 4,
      "Air-change rate scales with grade: ISO 7 (Grade C) rooms run roughly 20&ndash;40 changes per "
      "hour" + _c("ispe-cleanroom-design-iso14644-16") + ", and a unidirectional Grade A fill point far higher."),
    table(["Room", "Grade", "ISO class", "ACH", "Activity"], [
      ["Goods-in / quarantine", "CNC", ", ", "4&ndash;6", "Receive & hold biomass"],
      ["Milling / dispensing", "Grade D", "ISO 8", "10&ndash;20", "Size-reduce, weigh"],
      ["Wash / extraction", "Grade C", "ISO 7", "20&ndash;40", "Separate trichomes"],
      ["Freeze-dry / press", "Grade C", "ISO 7", "20&ndash;40", "Dry & press to rosin"],
      ["Solvent recovery", "Grade D (C1D1)", "ISO 8", "10&ndash;20", "Recover solvent, LEL purge"],
      ["Open-product fill", "Grade A", "ISO 5", "unidirectional", "Fill open product (pharma)"],
    ], cls="compact", caption="Each room with its grade, ISO class, air-change rate, and key activity."),
  ]})

SECTIONS.append({"id": "pressure-and-people", "kicker": "Core concept", "title": "Pressure Cascade, HVAC, and Gowning",
  "blocks": [
    p("Air is the main way contamination travels, so the building runs a <strong>positive-pressure "
      "cascade</strong>: clean rooms are held at higher pressure than dirtier ones, so air always "
      "blows <em>outward</em> from clean to dirty. Open a door and clean air rushes out. It can "
      "never suck dirty air toward the product."),
    p("Pressures step up shell by shell. EU-GMP Annex 1 recommends roughly a 10&ndash;15&nbsp;Pa "
      "difference between adjacent classified zones" + _c("ispe-cleanroom-design-iso14644-16") + ", giving "
      "a ladder like 0&nbsp;Pa (CNC), +15 (D), +30 (C), +45 (B), +60 (A). The solvent room is the one "
      "exception: it runs <strong>negative</strong>, around -15&nbsp;Pa, so flammable vapour is "
      "contained and pulled toward the LEL exhaust rather than pushed into the building."),
    figure(L.flow("Pressure cascade: clean rooms push air to dirty rooms",
            [("CNC 0 Pa", "outer shell"), ("Grade D +15", "milling"),
             ("Grade C +30", "wash / dry"), ("Grade A +60", "fill core"),
             ("Solvent -15", "negative: contains vapour")],
            note="Positive ladder protects product; the solvent room inverts to trap flammable vapour."), 5,
      "Rising positive pressure from CNC to the Grade A core keeps airflow running clean-to-dirty; the "
      "C1D1 solvent room runs negative to contain vapour."),
    p("People are the single largest source of particles and microbes in a cleanroom" + _c("sciencedirect-cleanroom-personnel-emissions-2024") +
      ", so entry is a one-way airlock sequence that escalates gowning as the grade rises. Filtration "
      "scales with grade too: F9 pre-filters in prep, H13 HEPA in wash and dry, and H14 HEPA at "
      "the fill point. An H14 HEPA filter retains at least 99.995% of particles at the most-penetrating "
      "size" + _c("en1822-h14-hepa") + ", which is why it guards the cleanest air."),
    figure(L.flow("Gowning airlock cascade (entry is one-way)",
            [("CNC entry", "street clothes off"), ("D airlock", "lab coat + single glove"),
             ("C airlock", "coverall + double glove"), ("B/A airlock", "sterile one-piece + double glove"),
             ("Cleanroom", "work; de-gown via separate exit")],
            note="Gowning escalates with grade. A physically separate corridor handles de-gowning on exit."), 6,
      "A one-way gowning sequence from CNC entry through grade airlocks to the work zone, with a "
      "separate dashed de-gown exit so entry and egress never share a door."),
    callout("warn", "Health check at the door",
      p("Anyone with open wounds, respiratory illness, or gastrointestinal symptoms is excluded at the "
        "entry health check, and the exclusion is recorded. Airlocks are interlocked so both "
        "doors can never open at once.")),
    table(["Grade", "Temp", "RH", "Filtration", "&Delta;P", "ACH"], [
      ["CNC", "ambient", "&lt;70%", "F7", "0 Pa", "4&ndash;6"],
      ["Grade D", "18&ndash;24&nbsp;&deg;C", "45&ndash;60%", "F9", "+15 Pa", "10&ndash;20"],
      ["Grade C", "18&ndash;22&nbsp;&deg;C", "45&ndash;55%", "H13 HEPA", "+30 Pa", "20&ndash;40"],
      ["Grade A fill", "18&ndash;22&nbsp;&deg;C", "45&ndash;55%", "H14 HEPA", "+60 Pa", "unidir."],
      ["Solvent (C1D1)", "18&ndash;24&nbsp;&deg;C", "&lt;55%", "F9", "-15 Pa", "10&ndash;20"],
    ], cls="compact", caption="HVAC control matrix: temperature, humidity, filtration, pressure and air changes per grade."),
  ]})

SECTIONS.append({"id": "process-flows", "kicker": "Core concept", "title": "How the Product Is Actually Made",
  "blocks": [
    p("Two routes leave the weigh-in. <strong>Solventless</strong> separates the trichome heads (the "
      "resin glands) mechanically. <strong>Solvent extraction</strong> dissolves the resin and then "
      "recovers it. They share a goal but carry very different hazards."),
    p("The solventless route agitates fresh-frozen biomass in ice water, sieves the resin through a "
      "stack of screens (220 down to 25 micron), freeze-dries it, and presses it to rosin. Its four "
      "<strong>critical control points</strong> are wash temperature (&le;4&nbsp;&deg;C), water "
      "quality (RO, &lt;10&nbsp;CFU/mL), water activity (Aw&nbsp;&le;0.55), and press temperature "
      "(&le;90&nbsp;&deg;C). Keeping water activity at or below about 0.55&ndash;0.65 starves microbes "
      "and fungi before they can grow" + _c("ehp-cannabis-contaminants-2019") + "."),
    figure(L.flow("Solventless route with critical control points",
            [("Fresh-frozen", "weigh-in biomass"), ("Agitate &le;4&deg;C", "CCP: wash temp"),
             ("Sieve 220-25um", "RO water <10 CFU"), ("Freeze-dry", "CCP: Aw &le;0.55"),
             ("Press &le;90&deg;C", "CCP: press temp")],
            note="Four CCPs gate the solventless line: wash temp, water quality, water activity, press temp."), 7,
      "The solventless flow from fresh-frozen biomass through agitation, sieving, freeze-drying and "
      "pressing, with the four critical control points called out."),
    p("Solvent extraction is a closed loop using butane, propane, ethanol, or CO&#8322;. Here the "
      "dominant hazards shift to <strong>flammability</strong> and <strong>residual solvent</strong>, "
      "the trace of extraction solvent left in the product. Residual butane and propane action "
      "limits run roughly 2000&ndash;5000&nbsp;ppm depending on the jurisdiction" + _c("ich-q3c-r9-ema") +
      ", and ethanol, an ICH Q3C Class&nbsp;3 solvent, is typically capped near 5000&nbsp;ppm" + _c("ich-q3c-r9-ema") +
      ". Every batch is gated hard by a headspace GC-MS residual-solvent test before it can be released."),
    figure(L.flow("Closed-loop solvent extraction with QC gate",
            [("Charge column", "load biomass"), ("Solvent pass", "dissolve resin"),
             ("Filter / winterize", "remove fats"), ("Recover solvent", "C1D1 + LEL purge"),
             ("Vacuum purge", "GC-MS gate before release")],
            note="C1D1 safety interlocks run in parallel; the residual-solvent test is the release gate."), 8,
      "Charge to solvent pass to winterize to recovery to vacuum purge, with the residual-solvent QC "
      "gate and a parallel C1D1 safety overlay."),
    callout("danger", "Hydrocarbon rooms are C1D1 for a reason",
      p("Butane and propane extraction must run in an NFPA-classified <strong>C1D1</strong> room: LEL "
        "(lower-explosive-limit) gas detection with auto-purge, explosion-proof electrics, a two-person "
        "rule, and ASME-rated pressure vessels. This is the highest-consequence area in the building. "
        "A single ignition source is catastrophic.")),
    p("For the solventless line, water is treated as an <strong>ingredient</strong>, not a utility. It "
      "runs its own loop: mains to carbon/sediment pre-filter, to RO/DI, to a UV + 0.2-micron "
      "polish, to a sanitised ice hopper, to the point of use, with sampling at three points "
      "and out-of-spec water sent straight to quarantine."),
    figure(L.flow("Treated water and ice loop (water is an ingredient)",
            [("Mains in", "S1 sample: feed"), ("Pre-filter", "carbon + sediment"),
             ("RO / DI", "S2 sample: post-RO"), ("UV + 0.2um", "final polish"),
             ("Ice hopper", "S3 sample: point of use")],
            note="Three sampling points; any out-of-spec result quarantines the water before it touches product."), 9,
      "The linear water-treatment train with its three sampling points and out-of-spec quarantine logic."),
  ]})

SECTIONS.append({"id": "qc-and-release", "kicker": "How-to", "title": "Step-by-Step: Testing, Sampling, and Batch Release",
  "blocks": [
    p("Testing happens at <strong>three tiers</strong>, incoming biomass, in-process, and "
      "release, across four sampling stations along the value stream. Retained reference "
      "samples are kept to expiry + 1 year so any later complaint can be investigated against the "
      "actual material."),
    figure(L.flow("Four sampling stations along the value stream",
            [("S1 incoming", "biomass: micro, pesticides"), ("S2 in-process", "moisture, visual"),
             ("S3 bulk concentrate", "potency, residual solvent"), ("S4 finished goods", "full release panel")],
            note="Each station tests what matters at that stage; S4 is the full legal release panel."), 10,
      "From incoming biomass (S1) through in-process (S2) and bulk concentrate (S3) to finished goods "
      "(S4), with what each station tests."),
    p("The finished-goods release panel is the legal gate to market. It covers <strong>seven "
      "families</strong>: potency, residual solvents, pesticides, microbials, heavy metals, "
      "mycotoxins, and water activity/moisture" + _c("ehp-cannabis-contaminants-2019") + ". Heavy metals "
      "(lead, cadmium, arsenic, mercury) are quantified by ICP-MS, the standard method" + _c("ehp-cannabis-contaminants-2019") +
      ", and the regulated mycotoxins, aflatoxins B1/B2/G1/G2 and ochratoxin&nbsp;A, are "
      "carcinogens controlled at parts-per-billion levels."),
    callout("tip", "Always test the concentrate, never just the flower",
      p("A pesticide or metal level that passes comfortably on raw flower can fail once it is "
        "concentrated five- to ten-fold into resin" + _c("ehp-cannabis-contaminants-2019") + ". Release decisions "
        "are made on the <em>finished concentrate</em>, full stop.")),
    table(["Family", "Analytes", "Method", "Why"], [
      ["Potency", "THC, CBD, total cannabinoids", "HPLC-DAD", "Label accuracy"],
      ["Residual solvents", "Butane, propane, ethanol", "Headspace GC-MS", "Solvent safety"],
      ["Pesticides", "State pesticide list", "LC-MS/MS, GC-MS/MS", "Chemical safety"],
      ["Microbials", "TYMC, TAMC, E. coli, Salmonella, Aspergillus", "Plate / qPCR", "Pathogen control"],
      ["Heavy metals", "Pb, Cd, As, Hg", "ICP-MS", "Toxic-metal limits"],
      ["Mycotoxins", "Aflatoxins, ochratoxin A", "LC-MS/MS", "Carcinogen control"],
      ["Water activity", "Aw, moisture", "Aw meter / KF", "Mould prevention"],
    ], cls="compact", caption="The seven mandatory release families. Pathogens such as Salmonella and E. coli must be absent."),
    p("QA, not production, then runs three sequential gates. Any &lsquo;no&rsquo; "
      "diverts the batch to remediation. Only a clean pass on all three reaches release with a QP/QA "
      "signature and an issued Certificate of Analysis" + _c("ecfr-21cfr211") + "."),
    steps([
      ("Gate 1: Records", "Is the batch record complete and signed end to end (ALCOA+)? If not, the batch cannot proceed."),
      ("Gate 2: Results", "Are all seven test families within spec, pathogens absent? Any out-of-spec result routes to OOS investigation."),
      ("Gate 3: Deviations", "Are all deviations on this batch closed with CAPA? Any open critical deviation blocks release."),
      ("Release", "All three gates pass: QA signs, the CoA is issued, status flips to Released."),
    ]),
    figure(L.flow("Batch release decision tree (QA-owned)",
            [("Records signed?", "yes -> on; no -> hold"), ("Results in spec?", "yes -> on; no -> OOS"),
             ("Deviations closed?", "yes -> on; no -> remediate"), ("QA RELEASE", "sign + issue CoA")],
            note="Three sequential yes/no gates; any no routes to hold, OOS, or remediation."), 11,
      "The three sequential gates, records, results and deviations, routing to QA release or "
      "to the return/OOS/hold lanes."),
  ]})

SECTIONS.append({"id": "deviations-and-pitfalls", "kicker": "Pitfalls", "title": "When It Goes Wrong: Deviations, CAPA, and Common Traps",
  "blocks": [
    p("When reality departs from the approved process, the <strong>deviation system</strong> catches "
      "it. ICH Q10 establishes the pharmaceutical quality system, including CAPA and change "
      "control, that this loop sits inside" + _c("pmc-capa-ich-q10-2024") + ". Every deviation runs "
      "through a five-stage CAPA loop, and it is <em>not</em> closed until the final effectiveness "
      "check passes."),
    figure(L.flow("Five-stage CAPA loop",
            [("Detect / log", "capture the deviation"), ("Contain", "quarantine & scope"),
             ("Investigate", "root cause: 5-why / fishbone"), ("Correct", "fix the affected batch"),
             ("Prevent + verify", "SOP/training + effectiveness check")],
            note="Root-cause tools (5-why, Ishikawa) drive stage 3. The loop closes only when verification passes."), 12,
      "Detect, contain, investigate, correct, then prevent-and-verify, with a feedback arrow closing "
      "the loop back into the process" + _c("pmc-capa-ich-q10-2024") + "."),
    p("Severity triage sets the urgency and the sign-off level. A <strong>critical</strong> deviation, "
      "one with patient-safety or recall risk, goes to the QA director with under "
      "24&nbsp;hours to containment. A <strong>major</strong> goes to QA on a defined timeline. A "
      "<strong>minor</strong> goes to a supervisor to be trended. Root-cause tools such as 5-why and "
      "Ishikawa (fishbone) diagrams are the standard ways to find what actually went wrong" + _c("pmc-capa-ich-q10-2024") + "."),
    callout("warn", "The three classic traps",
      ul(["<strong>Trusting the biomass CoA.</strong> Extrapolating safety from the raw-flower result instead of testing the concentrate. The number that matters is the one after concentration.",
          "<strong>Releasing on a borderline residual-solvent result.</strong> Never. Re-test, re-purge, or reject, and document the disposition.",
          "<strong>Letting physical and system status disagree.</strong> Quarantine stock must sit behind a locked cage or controlled rack; the computer and the shelf must always tell the same story."], "tight")),
    figure(L.flow("Waste and reject disposition",
            [("Off-spec / spent", "into locked cage"), ("Quarantine cage", "controlled, logged"),
             ("Render unusable", "denature / destroy"), ("Licensed disposal", "witnessed manifest")],
            note="Solvent waste is a separate hazmat stream. Cannabis waste is rendered unusable, then hauled under a witnessed manifest."), 13,
      "Off-spec product and spent biomass into a locked quarantine cage, rendered unusable, then "
      "licensed disposal with a witnessed manifest; solvent waste runs as a separate hazmat stream."),
  ]})

SECTIONS.append({"id": "realistic-expectations", "kicker": "Reality check", "title": "Realistic Expectations: Cost, Cadence, and What 'Compliant' Really Means",
  "blocks": [
    p("Compliance is a continuous program measured by data, not a one-time build. Management review "
      "tracks a handful of KPIs: right-first-time release rate (target &ge;98%), deviation rate per "
      "batch (&lt;5%), median CAPA closure (&le;30 days), environmental-monitoring results within "
      "limits (&ge;95%), and mock-recall retrieval (&lt;24h)."),
    figure(L.bars("Quality KPI targets that run the system",
            [("Right-first-time %", 98), ("EM in-limit %", 95), ("CAPA closed <=30d", 90),
             ("Deviation rate %", 5)], unit="", target=90,
            note="Higher is better for the first three; deviation rate is the one you want LOW.",
            maxv=110), 14,
      "The headline KPI targets shown against their thresholds. The system is healthy when "
      "right-first-time stays high and deviation rate stays low."),
    p("Equipment must be <strong>qualified</strong> before it ever makes releasable product, through "
      "the validation V-model: DQ (design), IQ (installation), OQ (operational), PQ (performance), "
      "each verifying the leg opposite it. Qualification follows that IQ/OQ/PQ progression" + _c("fda-process-validation-2011") +
      ", and only then does <strong>process validation</strong> begin: conventionally three "
      "consecutive conforming batches to prove the process is reproducible" + _c("fda-process-validation-2011") + "."),
    figure(L.flow("V-model qualification, then process validation",
            [("URS / design", "what it must do"), ("Build / install", "IQ verifies install"),
             ("Operate", "OQ verifies function"), ("Perform", "PQ verifies real output"),
             ("3 conformance batches", "process validation")],
            note="Each right-hand stage verifies the matching design stage; PQ leads into process validation."), 15,
      "The descending design leg (URS to build) is verified by the ascending qualification leg "
      "(IQ/OQ/PQ), with process validation of three conformance batches following PQ" + _c("fda-process-validation-2011") + "."),
    p("Cleaning is validated too, against a calculated <strong>MACO</strong> (Maximum Allowable "
      "Carryover) limit measured by swab or rinse with TOC/HPLC and micro acceptance criteria, never "
      "&lsquo;looks clean.&rsquo; Scale the gowning, monitoring, and grade to what you actually "
      "run: a D-to-C envelope is normal for most hash operations, and over-building to Grade A/B that "
      "the product doesn't require simply wastes capital."),
    table(["Cadence", "What is reviewed", "Owner"], [
      ["Per batch", "Batch record, release results, deviations", "QA reviewer"],
      ["Weekly", "EM trends, open deviations, OOS log", "QA lead"],
      ["Monthly", "CAPA status, KPI dashboard", "QA manager"],
      ["Quarterly", "Management review, supplier performance", "QA director"],
      ["Annually", "Product Quality Review (PQR), self-inspection", "Quality + ops"],
    ], cls="compact", caption="The fixed review cadence, from per-batch through annual."),
    callout("key", "What 'compliant' actually means",
      p("Not a perfect building: a <em>provable</em> one. Compliant means every batch can be "
        "traced, every limit was met or the deviation was closed, and an inspector could reconstruct "
        "the whole story from the records alone. Specific limits and grades vary by jurisdiction, so "
        "validate against your own licence before you build.")),
    p("Once the system runs, the contamination side of the picture is where most failures actually "
      "originate. Read the <a href='mould-risk.html'>mould-risk</a> paper next, and see the "
      "<a href='wso-quality-manual.html'>WSO quality manual</a> for a worked example of the documented "
      "system this architecture demands."),
  ]})
