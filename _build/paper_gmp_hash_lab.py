# -*- coding: utf-8 -*-
"""Paper: GMP hash manufacturing, facility flow and quality control (beginner)."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        stagecard, grid, card, chip, kv, steps)
import figs_lib as L

SLUG = "gmp-hash-lab"
TITLE = "GMP hash lab: zones, flows, and batch release"
EYEBROW = "Facility · GMP"
SUB = ("This paper gives the GMP requirements for a hash facility: the cleanroom grade zones, the "
       "flows of product and personnel, and the batch release. A batch must go through seven groups "
       "of tests and three release gates to get a signed Certificate of Analysis.")
META = [("building", "Facility"), ("image", "13 diagrams"),
        ("quote", "9 sources"), ("clock", "~18 min to read")]
RELATED = ["mould-risk", "facility-3d"]
REF_IDS = ["ecfr-21cfr211", "ich-q3c-r9-ema", "ehp-cannabis-contaminants-2019",
           "en1822-h14-hepa", "sciencedirect-cleanroom-personnel-emissions-2024",
           "pmc-capa-ich-q10-2024", "fda-process-validation-2011",
           "ispe-cleanroom-design-iso14644-16", "luca2020-pesticide-partition-hemp-extract"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

SECTIONS.append({"id": "what-this-is", "kicker": "Start here", "title": "Purpose and scope",
  "blocks": [
    lead("<strong>Good Manufacturing Practice</strong> (GMP) is a system with written records and "
         "audits. The system shows that a product agrees with its label, and that no dangerous "
         "material went into the product during production. A GMP hash lab makes purified resin "
         "concentrates (bubble hash, rosin, live resin, distillate) from cannabis biomass, with "
         "full control of contamination."),
    p("Extraction can increase the concentration of a contaminant, decrease it, or change where it "
      "is. The effect is different for each analyte, process, and mass yield" +
      _c("luca2020-pesticide-partition-hemp-extract") + ". A flower result that is in the limits "
      "does not show that the finished concentrate agrees with the requirements. Do a test of the "
      "incoming material and of the finished batch. Then use the two sets of results to calculate "
      "the transfer for each process. Material goes to the next step only when the release data "
      "show that it is safe and that its label is correct."),
    p("Two sets of regulations give most of the requirements for the facility. <strong>EU-GMP Annex "
      "1</strong> gives the cleanroom classifications and the contamination control strategy. The "
      "U.S. <strong>cGMP regulations in 21 CFR 210/211</strong> give the production controls, the "
      "records, and the authority of the quality unit to release product" + _c("ecfr-21cfr211") +
      ". This paper is a reference model. It is not legal advice. The limits and grades are "
      "different in each jurisdiction."),
    callout("key", "The one basic requirement of GMP",
      p("&lsquo;If there is no record, the task did not occur.&rsquo; GMP is a system with "
        "documents and validation, and an inspector can examine it. An auditor does not accept a "
        "very clean room that has no records. An auditor accepts a basic room that has full, signed "
        "records.")),
    figure(L.bars("The four primary numbers for this design",
            [("Cleanliness grades", 5), ("Release test groups", 7), ("Genealogy coverage", 100),
             ("Critical deviations at release", 0)], unit="",
            note="Primary values: 5 grades, 7 mandatory test groups, 100% traceability of batches, zero open critical deviations.",
            maxv=110), 1,
      "Four numbers are the primary values for the facility. There are five cleanliness grades. "
      "There are seven mandatory groups of release tests. The genealogy coverage is full. At the "
      "time of release, the number of open critical deviations must be zero."),
    table(["Standard", "Content", "Area of the facility that it controls"], [
      ["EU-GMP Annex 1", "Classification of cleanrooms and the contamination control strategy", "Each room that has a cleanroom class"],
      ["cGMP 21 CFR 210/211", "Production controls, records, and the authority of the QC unit to release product", "All the plant, and QA"],
      ["ICH Q7 / Q9 / Q10", "Quality system, risk management, and lifecycle", "Quality management system"],
      ["ISO 14644-1", "Particle-count classes of cleanrooms (ISO 5/7/8)", "Classification of air"],
      ["GACP", "Good Agricultural and Collection Practice for biomass", "Goods-in and intake"],
      ["NFPA 30 / C1D1", "Flammable liquids, and classified electrical areas", "Solvent extraction room"],
    ], cls="compact", caption="The standards and the part of the building that each standard controls."),
  ]})

SECTIONS.append({"id": "key-terms", "kicker": "Terms", "title": "Definitions",
  "blocks": [
    p("These terms occur many times in this paper. The paper gives the full information about each term where the term first occurs."),
    defterm("Cleanroom grade", "A symbol (CNC, D, C, B, A) that shows how clean the air of a room "
            "is. Each symbol agrees with an ISO 14644 particle class. Grade C is ISO 7, and Grade A "
            "is ISO 5."),
    defterm("Batch / lot", "One specified production run with one lot ID. Personnel record each "
            "event of the batch with that ID. The record is the genealogy of the batch."),
    defterm("Deviation", "Each difference from the approved process. Personnel record each "
            "deviation and do an investigation. The deviation must have the status Closed before "
            "the batch with the deviation can have the status Released."),
    defterm("CAPA", "Corrective And Preventive Action. It is the loop that corrects the problem "
            "(corrective) and makes sure that the problem does not occur again (preventive)."),
    defterm("Quarantine / Released / Rejected", "The three statuses of a material. Each material "
            "has only one of these three statuses at one time. No material is between two statuses. "
            "The status of a material is always one of these three."),
    defterm("CCP (Critical Control Point)", "A step in which a measured limit prevents a hazard "
            "(HACCP term). An example is wash water at less than 4&nbsp;&deg;C."),
    defterm("ALCOA+", "The properties that a good record must have: Attributable, Legible, "
            "Contemporaneous, Original, Accurate, plus Complete, Consistent, Enduring, Available."),
    defterm("Water activity (Aw)", "The free water that microbes can use, on a scale of 0 to 1. A "
            "low value prevents the growth of mold and bacteria. CoA is Certificate of Analysis. "
            "C1D1 is a classified room for flammable material."),
    p("QA is the Quality Assurance function. QA makes the last release decision, and QA operates "
      "independently of production" + _c("ecfr-21cfr211") + ". This difference between QA and "
      "production is the primary part of the system. The personnel who send product out of the "
      "facility must not give the approval for their work."),
    figure(L.flow("Statuses of a batch",
            [("Quarantine", "received, with no decision"), ("Released", "accepted, for sale"),
             ("Rejected", "not accepted, to disposition")],
            note="Each lot has only one of these three statuses at all times."), 2,
      "The three statuses. A material has only one status at a time. The location of the material and its status in the system must always agree."),
  ]})

SECTIONS.append({"id": "zoning", "kicker": "Basic information", "title": "Zones and cleanroom grades",
  "blocks": [
    p("The building is a set of shells of cleanliness. Each shell is in the next shell. The "
      "<strong>dirty</strong> tasks are intake, milling, and waste. They are at the outer edge. The "
      "<strong>clean</strong> tasks, with the highest cleanliness, are the collection, the fill, "
      "and the packaging of open product. They are in the inner zone."),
    p("The flow requirement is easy, and you must always obey it: <strong>Product moves to the "
      "zones with more cleanliness, to the inner zone. Personnel and waste move to the dirty edge. "
      "Do not let the two flows go through the same area without control.</strong> Between each "
      "pair of shells there is an airlock, and the grade changes by one step.</p><p>In EU-GMP Annex "
      "1, Grade C agrees with ISO 7 and Grade A agrees with ISO 5" +
      _c("ispe-cleanroom-design-iso14644-16") + ". Most hash facilities for recreational cannabis "
      "and for medicinal cannabis use grades D to C. They use Grade C for the fill point, with "
      "local protection. A full Grade A or B is necessary only for sterile dose forms or "
      "pharmaceutical dose forms."),
    figure(L.zones("Shells of cleanliness (outer = dirty, inner = clean)",
            0, 4, [(0, 1, L.REDL, "CNC intake"), (1, 2, L.AMBL, "Grade D"),
                   (2, 3, L.GL, "Grade C"), (3, 4, L.GXL, "Inner Grade A")],
            unit="", note="Product flows to the clean inner zone. Personnel and waste flow to the dirty edge."), 3,
      "Each zone is in the next zone, from the CNC outer shell through Grade D and Grade C to the "
      "clean inner zone. Product goes to the clean inner zone. Personnel and waste go to the dirty "
      "edge."),
    figure(L.bars("Air changes each hour increase with cleanliness",
            [("CNC", 5), ("Grade D", 15), ("Grade C", 30), ("Grade A", 240)], unit=" ACH",
            note="Higher grades change the air more frequently. Recommended rate for ISO 7: ~20 to 40 ACH.",
            maxv=270), 4,
      "The air-change rate increases with the grade. ISO 7 rooms (Grade C) have approximately 20 to "
      "40 changes each hour" + _c("ispe-cleanroom-design-iso14644-16") + ". A Grade A fill point "
      "with unidirectional airflow has a much higher rate."),
    table(["Room", "Grade", "ISO class", "Air changes each hour (ACH)", "Task"], [
      ["Goods-in and quarantine", "CNC", ", ", "4 to 6", "Personnel receive and hold the biomass."],
      ["Milling and dispensing", "Grade D", "ISO 8", "10 to 20", "Personnel make the biomass smaller and weigh it."],
      ["Wash and extraction", "Grade C", "ISO 7", "20 to 40", "Personnel remove the trichomes from the plant material."],
      ["Freeze-dry and press", "Grade C", "ISO 7", "20 to 40", "Personnel dry the material and press it to make rosin."],
      ["Solvent recovery", "Grade D (C1D1)", "ISO 8", "10 to 20", "Personnel recover the solvent and do an LEL purge."],
      ["Open-product fill", "Grade A", "ISO 5", "unidirectional", "Personnel fill open product (pharmaceutical use)."],
    ], cls="compact", caption="Each room with its grade, ISO class, air-change rate, and primary task."),
  ]})

SECTIONS.append({"id": "pressure-and-people", "kicker": "Basic information", "title": "Pressure cascade, HVAC, and gowning",
  "blocks": [
    p("The primary medium for the movement of contamination in a cleanroom is air. Air flows from a "
      "high pressure to a low pressure, and not in the opposite direction. A "
      "<strong>positive-pressure cascade</strong> uses this effect.</p><p>The clean rooms have a "
      "higher pressure than the adjacent dirtier spaces. Thus air always flows <em>out</em> from "
      "clean to dirty. When you open a door, clean air flows out. Dirty air cannot flow back to the "
      "product."),
    p("The pressure increases in steps, from shell to shell. EU-GMP Annex 1 recommends that the "
      "difference between adjacent classified zones is approximately 10 to 15&nbsp;Pa" +
      _c("ispe-cleanroom-design-iso14644-16") + ". This difference gives these values: 0&nbsp;Pa "
      "(CNC), +15 (D), +30 (C), +45 (B), and +60 (A). The solvent room is different: its pressure "
      "is <strong>negative</strong>, approximately -15&nbsp;Pa. As a result, the flammable vapor "
      "stays in the room and flows to the LEL exhaust. It does not flow into the building."),
    figure(L.flow("Pressure cascade: air flows from clean rooms to dirty rooms",
            [("CNC 0 Pa", "outer shell"), ("Grade D +15", "milling"),
             ("Grade C +30", "wash / dry"), ("Grade A +60", "fill zone"),
             ("Solvent -15", "negative: contains vapor")],
            note="Positive pressure keeps product clean. The solvent room is negative to contain flammable vapor."), 5,
      "Positive pressure that increases from CNC to the Grade A inner zone keeps the airflow from "
      "clean to dirty. The C1D1 solvent room has a negative pressure to contain vapor."),
    p("Personnel are the largest source of particles and microbes in a cleanroom" +
      _c("sciencedirect-cleanroom-personnel-emissions-2024") + ". Thus entry is a one-way sequence "
      "of airlocks, and the gowning increases when the grade increases.</p><p>Filtration also "
      "changes with the grade. The milling and dispensing rooms have F9 pre-filters. The wash and "
      "dry rooms have H13 HEPA filters. The fill point has H14 HEPA filters. An H14 HEPA filter "
      "stops a minimum of 99.995% of the particles at the most penetrating particle size" +
      _c("en1822-h14-hepa") + ". Thus this filter is at the point with the highest cleanliness."),
    figure(L.flow("Gowning airlock cascade (entry is one-way)",
            [("CNC entry", "street clothes off"), ("D airlock", "lab coat and one glove"),
             ("C airlock", "coverall and two gloves"), ("B/A airlock", "sterile one-piece and two gloves"),
             ("Cleanroom", "work, remove gown at the other exit")],
            note="Gowning increases with the grade. Personnel remove the gown in a different corridor at exit."), 6,
      "A one-way sequence of gowning from CNC entry, through the airlocks of each grade, to the "
      "work zone. A different exit, with a dashed line, is for the removal of the gown. Thus entry "
      "and exit do not use the same door."),
    callout("warn", "Health check at the door",
      p("Do not let a person with an open wound, a respiratory illness, or gastrointestinal "
        "symptoms go into the cleanroom. Do a health check at the entry, and record each person "
        "that you stop. Each airlock has an interlock. Thus the two doors cannot open at the same "
        "time.")),
    table(["Grade", "Temperature", "Relative humidity (RH)", "Filtration", "Pressure difference (&Delta;P)", "Air changes each hour (ACH)"], [
      ["CNC", "ambient", "less than 70%", "F7", "0 Pa", "4 to 6"],
      ["Grade D", "18 to 24&nbsp;&deg;C", "45 to 60%", "F9", "+15 Pa", "10 to 20"],
      ["Grade C", "18 to 22&nbsp;&deg;C", "45 to 55%", "H13 HEPA", "+30 Pa", "20 to 40"],
      ["Grade A fill", "18 to 22&nbsp;&deg;C", "45 to 55%", "H14 HEPA", "+60 Pa", "unidirectional"],
      ["Solvent (C1D1)", "18 to 24&nbsp;&deg;C", "less than 55%", "F9", "-15 Pa", "10 to 20"],
    ], cls="compact", caption="The HVAC control values for each grade: temperature, humidity, filtration, pressure, and air changes."),
  ]})

SECTIONS.append({"id": "process-flows", "kicker": "Basic information", "title": "Hash manufacturing process flow",
  "blocks": [
    p("Two processes start after the weigh-in. The <strong>solventless</strong> process removes the "
      "trichome heads (the resin glands) mechanically. The <strong>solvent extraction</strong> "
      "process dissolves the resin and then recovers the resin. The two processes make the same "
      "type of product, but their hazards are very different."),
    p("In the solventless process, personnel agitate fresh-frozen biomass in ice water. They sieve "
      "the resin through a stack of screens (220 to 25 micron). They freeze-dry the resin and press "
      "it to make rosin. The process has four <strong>critical control points</strong>: wash "
      "temperature (&le;4&nbsp;&deg;C (39&nbsp;&deg;F)), water quality (RO, &lt;10&nbsp;CFU/mL), "
      "water activity (Aw&nbsp;&le;0.55), and press temperature (&le;90&nbsp;&deg;C "
      "(194&nbsp;&deg;F)). A water activity of approximately 0.55 to 0.65 or less prevents the "
      "growth of microbes and fungi" + _c("ehp-cannabis-contaminants-2019") + "."),
    figure(L.flow("Solventless process with critical control points",
            [("Fresh-frozen", "weigh-in biomass"), ("Agitate &le;4&deg;C", "CCP: temperature"),
             ("Sieve 220-25um", "RO water <10 CFU"), ("Freeze-dry", "CCP: Aw &le;0.55"),
             ("Press &le;90&deg;C", "CCP: temperature")],
            note="Four CCPs control the process: wash temperature, water quality, water activity, press temperature."), 7,
      "The solventless process: personnel agitate fresh-frozen biomass, sieve the resin, freeze-dry "
      "it, and press it. The figure shows the four critical control points."),
    p("Solvent extraction is a closed loop that uses butane, propane, ethanol, or CO&#8322;. In "
      "this process, the primary hazards are <strong>flammability</strong> and <strong>residual "
      "solvent</strong>. Residual solvent is the trace of extraction solvent that stays in the "
      "product. The action limits for residual butane and propane are approximately 2000 to "
      "5000&nbsp;ppm, and the limit is different in each jurisdiction" + _c("ich-q3c-r9-ema") +
      ". Ethanol is an ICH Q3C Class&nbsp;3 solvent, and the usual limit for ethanol is "
      "approximately 5000&nbsp;ppm" + _c("ich-q3c-r9-ema") + ". Each batch must go through a "
      "headspace GC-MS test for residual solvent before the release of the batch."),
    figure(L.flow("Closed-loop solvent extraction with QC gate",
            [("Fill column", "add biomass"), ("Solvent flow", "dissolve resin"),
             ("Filter / winterize", "remove fats"), ("Recover solvent", "C1D1 + LEL purge"),
             ("Vacuum purge", "GC-MS gate before release")],
            note="C1D1 safety interlocks operate at the same time. The residual solvent test is the release gate."), 8,
      "Personnel fill the column, apply the solvent, filter and winterize, recover the solvent, and "
      "do a vacuum purge. The QC gate for residual solvent is the last step. The C1D1 safety "
      "interlocks operate at the same time."),
    callout("danger", "A hydrocarbon room must be a C1D1 room",
      p("Do butane and propane extraction only in a <strong>C1D1</strong> room (NFPA "
        "classification). The room must have LEL (lower explosive limit) gas sensors with an "
        "automatic purge. It must have explosion-proof electrical equipment, a two-person rule, and "
        "pressure vessels with an ASME rating. This area is the most dangerous area in the "
        "building. One source of ignition can cause very large damage.")),
    p("In the solventless process, water is an <strong>ingredient</strong> and not a utility. The "
      "water uses a loop that is only for water. The water goes from the mains to a carbon and "
      "sediment pre-filter.</p><p>Then it goes to RO/DI. Then it goes to a UV unit and a 0.2-micron "
      "last filter. Then it goes to a sanitized ice hopper, and then to the point of use. Personnel "
      "get samples at three points. Water that is out of specification goes to the quarantine area "
      "immediately."),
    figure(L.flow("Water treatment and ice loop (water is an ingredient)",
            [("Mains in", "S1 sample: feed"), ("Pre-filter", "carbon and sediment"),
             ("RO / DI", "S2 sample: after RO"), ("UV + 0.2um", "last filter"),
             ("Ice hopper", "S3 sample: point of use")],
            note="Three sampling points. A result out of specification puts the water in quarantine before it touches product."), 9,
      "The water treatment steps with their three sampling points and the quarantine procedure for water out of specification."),
  ]})

SECTIONS.append({"id": "qc-and-release", "kicker": "Procedure", "title": "Testing, sampling, and batch release",
  "blocks": [
    p("Personnel do tests at <strong>three stages</strong>: the incoming biomass, the process, and "
      "the release. The tests are at four sampling stations along the value stream. Personnel keep "
      "retained reference samples until 1 year after expiry. If a complaint occurs after the "
      "release, personnel can examine the kept material."),
    figure(L.flow("Four sampling stations along the value stream",
            [("S1 incoming", "microbials, pesticides"), ("S2 in-process", "moisture, visual"),
             ("S3 bulk concentrate", "potency, residual solvent"), ("S4 finished goods", "full release panel")],
            note="Each station has the tests for its stage. S4 is the full legal release panel."), 10,
      "The stations go from incoming biomass (S1), through in-process (S2) and bulk concentrate "
      "(S3), to finished goods (S4). The figure shows the tests of each station."),
    p("The release panel for finished goods is the legal gate to the market. The panel has "
      "<strong>seven groups of tests</strong>: potency, residual solvents, pesticides, microbials, "
      "heavy metals, mycotoxins, and water activity and moisture" + _c("ehp-cannabis-contaminants-2019") +
      ". Personnel measure the heavy metals (lead, cadmium, arsenic, mercury) with ICP-MS, the "
      "standard method" + _c("ehp-cannabis-contaminants-2019") + ". The mycotoxins in the "
      "regulations are aflatoxins B1/B2/G1/G2 and ochratoxin&nbsp;A. They are carcinogens, and "
      "their limits are in parts per billion."),
    callout("tip", "Test the finished concentrate",
      p("Extraction changes the distribution of the contaminants" +
        _c("luca2020-pesticide-partition-hemp-extract") + ". Thus a raw flower result in the limits "
        "does not make sure that the finished concentrate is in the limits. Make the release "
        "decision on the finished concentrate. Use the input results and the output results of the "
        "same batch to set the carryover factors for each process.")),
    table(["Group", "Analytes", "Method", "Used for"], [
      ["Potency", "THC, CBD, total cannabinoids", "HPLC-DAD", "Label accuracy"],
      ["Residual solvents", "Butane, propane, ethanol", "Headspace GC-MS", "Solvent safety"],
      ["Pesticides", "State pesticide list", "LC-MS/MS, GC-MS/MS", "Chemical safety"],
      ["Microbials", "TYMC, TAMC, E. coli, Salmonella, Aspergillus", "Plate or qPCR", "Pathogen control"],
      ["Heavy metals", "Pb, Cd, As, Hg", "ICP-MS", "Limits for toxic metals"],
      ["Mycotoxins", "Aflatoxins, ochratoxin A", "LC-MS/MS", "Carcinogen control"],
      ["Water activity", "Aw, moisture", "Aw meter or KF", "Mold prevention"],
    ], cls="compact", caption="The seven mandatory groups of release tests. Pathogens such as Salmonella and E. coli must not be in the product."),
    p("Then QA, and not production, operates three gates one after the other. If the result of a "
      "gate is &lsquo;no&rsquo;, the batch goes to remediation. Only a batch that all three gates "
      "accept gets the release. The release has a QP/QA signature and a Certificate of Analysis "
      "that QA gives" + _c("ecfr-21cfr211") + "."),
    steps([
      ("Gate 1: Records", "Make sure that the batch record is full and signed from start to end (ALCOA+). If it is not, the batch cannot go to the next gate."),
      ("Gate 2: Results", "Make sure that the results of all seven groups of tests are in the specification, with no pathogens. Each result out of specification (OOS) goes to an investigation."),
      ("Gate 3: Deviations", "Make sure that all deviations of the batch have the status Closed, with a CAPA. A critical deviation with the status Open stops the release."),
      ("Release", "When all three gates accept the batch, QA writes its signature and QA gives the CoA. Then the status changes to Released."),
    ]),
    figure(L.flow("Batch release decision tree (QA-owned)",
            [("Records signed?", "yes: next. no: hold"), ("Results in limits?", "yes: next. no: OOS"),
             ("Deviations closed?", "yes: next. no: remediation"), ("QA RELEASE", "sign, give CoA")],
            note="Three gates in sequence, each with yes or no. A no goes to hold, OOS, or remediation."), 11,
      "The three gates in sequence are records, results, and deviations. A batch goes to the QA "
      "release, or to hold, to OOS, or to remediation."),
  ]})

SECTIONS.append({"id": "deviations-and-pitfalls", "kicker": "Frequent problems", "title": "Deviations, CAPA, and troubleshooting",
  "blocks": [
    p("When the process is different from the approved process, the <strong>deviation "
      "system</strong> finds the difference. ICH Q10 gives the pharmaceutical quality system, with "
      "CAPA and change control, and this loop is part of it" + _c("pmc-capa-ich-q10-2024") +
      ". Each deviation has a CAPA loop of five stages. The deviation does <em>not</em> get the "
      "status Closed until the last effectiveness check gives a correct result."),
    figure(L.flow("Five-stage CAPA loop",
            [("Find", "record the deviation"), ("Contain", "quarantine, scope"),
             ("Examine", "root cause: 5-why / fishbone"), ("Correct", "repair the product"),
             ("Prevention, check", "SOP, training, effectiveness check")],
            note="Root-cause tools (5-why, Ishikawa) are for stage 3. The loop closes only when the check is correct."), 12,
      "The loop has five stages: find, contain, examine, correct, and prevention with a check. A "
      "feedback arrow closes the loop back to the process" + _c("pmc-capa-ich-q10-2024") +
      "."),
    p("The severity of the deviation sets the time limit and the person who gives the approval. A "
      "<strong>critical</strong> deviation has a risk to the safety of patients or a risk of a "
      "recall. It goes to the QA director, and containment must occur in less than 24&nbsp;hours. A "
      "<strong>major</strong> deviation goes to QA in a specified time. A <strong>minor</strong> "
      "deviation goes to a supervisor, and the supervisor examines the trend. Root-cause tools, for "
      "example 5-why and Ishikawa (fishbone) diagrams, are the standard methods to find the cause "
      "of the problem" + _c("pmc-capa-ich-q10-2024") + "."),
    callout("warn", "The three frequent errors",
      ul(["<strong>You use the biomass CoA for the concentrate.</strong> You think that the raw flower result shows that the concentrate is safe. You do not do a test of the concentrate. The important result is the result for the concentrate.",
          "<strong>You release a batch with a result for residual solvent near the limit.</strong> Do not release the batch. Do the test again, do the purge again, or reject the batch. Record the decision for the batch.",
          "<strong>The status of the material and the status in the system are not the same.</strong> Keep quarantine stock in a locked cage or on a controlled rack. The system and the shelf must always show the same status."], "tight")),
    figure(L.flow("Waste and reject disposition",
            [("Rejected, used", "into locked cage"), ("Quarantine cage", "controlled, recorded"),
             ("Make unusable", "denature / destroy"), ("Licensed disposal", "manifest, witness")],
            note="Solvent waste is a different stream of dangerous material. Cannabis waste becomes unusable, then goes with a manifest and a witness."), 13,
      "Rejected product and used biomass go into a locked quarantine cage. Personnel make them "
      "unusable. Then licensed disposal occurs with a manifest with a witness. Solvent waste is a "
      "different stream of dangerous material."),
  ]})

SECTIONS.append({"id": "realistic-expectations", "kicker": "The limits", "title": "Expected results and limitations",
  "blocks": [
    p("Compliance is a continuous process that personnel measure with data. It is not a task that "
      "you do one time. Management review monitors a small number of KPIs.</p><p>The target for the "
      "right-first-time release rate is a minimum of 98%. The target for the deviation rate for "
      "each batch is less than 5%. The target for the median time to close a CAPA is a maximum of "
      "30 days. The target for the results of environmental monitoring (EM) in the limits is a "
      "minimum of 95%. The target for the retrieval time in a mock recall is less than 24 hours."),
    figure(L.bars("Quality KPI targets for the system",
            [("Right-first-time %", 98), ("EM in-limit %", 95), ("CAPA closed <=30d", 90),
             ("Deviation rate %", 5)], unit="", target=90,
            note="First three: high values are the target. Deviation rate: a low value is the target.",
            maxv=110), 14,
      "The primary KPI targets with their thresholds. The system is in good condition when the "
      "right-first-time rate stays high and the deviation rate stays low."),
    p("Equipment must have a <strong>qualification</strong> before it makes product for release. "
      "The qualification follows the validation V-model: DQ (design), IQ (installation), OQ "
      "(operation), PQ (performance). Each of these stages makes sure that the stage on the "
      "opposite side of the V-model is correct.</p><p>The qualification follows the IQ, OQ, PQ "
      "sequence" + _c("fda-process-validation-2011") + ". Only then does the <strong>process "
      "validation</strong> start. Usually, it is three batches, one after the other, that agree "
      "with the specification. They show that the process gives the same result each time" +
      _c("fda-process-validation-2011") + "."),
    figure(L.flow("V-model qualification, then process validation",
            [("URS / design", "function list"), ("Assemble, install", "IQ: install check"),
             ("Operate", "OQ: function check"), ("Make", "PQ: check of output"),
             ("3 correct batches", "process validation")],
            note="Each right-hand stage is the test of the related design stage. Process validation follows PQ."), 15,
      "The design leg goes from the URS at the top to the assembly at the bottom. The qualification "
      "leg (IQ, OQ, PQ) goes from the bottom to the top, and it makes sure that the design leg is "
      "correct. Process validation of three batches that agree with the specification follows PQ" +
      _c("fda-process-validation-2011") + "."),
    p("Cleaning validation also uses a calculated <strong>MACO</strong> (Maximum Allowable "
      "Carryover) limit. Personnel measure the carryover with a swab sample or a rinse sample, with "
      "TOC or HPLC, and they use microbial acceptance criteria. &lsquo;Looks clean&rsquo; is not an "
      "acceptance criterion.</p><p>Select the gowning, the monitoring, and the grade for the "
      "process that you use. Grades D to C are usual for most hash operations. If Grade A or B is "
      "not necessary for the product, a facility with these grades is a waste of capital."),
    table(["Interval", "Items for review", "Owner"], [
      ["For each batch", "Batch record, release results, deviations", "QA reviewer"],
      ["Each week", "EM trends, open deviations, OOS log", "QA lead"],
      ["Each month", "CAPA status, KPI dashboard", "QA manager"],
      ["Each three months", "Management review, supplier performance", "QA director"],
      ["Each year", "Product Quality Review (PQR), self-inspection", "Quality and operations"],
    ], cls="compact", caption="The set review intervals, from each batch to each year."),
    callout("key", "Definition of 'compliant'",
      p("A compliant facility is not a building without faults. It is a building with "
        "<em>evidence</em>. In this building, each batch has traceability. For each limit, the "
        "result was in the limit, or the deviation had the status Closed.</p><p>An inspector can "
        "find all the events of the batch in the records only. The limits and grades are different "
        "in each jurisdiction. Before you make the facility, make sure that it agrees with the "
        "conditions of your license.")),
    p("When the system operates, most faults start on the contamination side. Next, read the paper "
      "<a href='mould-risk.html'>mold risk</a> for that side of the facility."),
  ]})
