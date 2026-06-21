# -*- coding: utf-8 -*-
"""Paper: the quality manual, a GMP quality system for cannabis (beginner)."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        stagecard, grid, card, chip, kv, steps)
import figs_lib as L

SLUG = "wso-quality-manual"
TITLE = "The quality manual: a GMP quality system for cannabis"
EYEBROW = "Facility · Quality"
SUB = ("How a medicinal-cannabis company proves, on paper, that every gram it grows and ships is "
       "safe, consistent, and traceable. A guide from zero.")
META = [("shield", "Quality"), ("image", "12 diagrams"),
        ("quote", "Peer-reviewed · 9 sources"), ("clock", "~18 min read")]
RELATED = ["gmp-hash-lab", "signal-and-noise", "root-zone-teros12"]
REF_IDS = ["ich-q10-pqs", "ich-q9-risk", "pics-pe009-ch1", "mhra-data-integrity",
           "pics-pi041-data", "eu-gmp-annex11", "nz-medcan-reg6",
           "rogers-data-integrity-2020", "arunagiri-capa-2024"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

SECTIONS.append({"id": "what-this-is", "kicker": "Start here", "title": "What a quality manual actually is",
  "blocks": [
    lead("A <strong>quality manual</strong> is the single top-level document that describes how a "
         "company controls quality across everything it does. It is not a list of work instructions. "
         "It is the apex of a documentation pyramid that sits above all the detailed procedures and "
         "points to them rather than repeating them."),
    p("The source document for this guide, <strong>WSO-QM-001 v1.0</strong>, is an 84-page manual for "
      "a New Zealand medicinal-cannabis company. It covers the whole product lifecycle: cultivation, "
      "harvesting, drying and curing, processing, manufacture, packaging, storage, distribution and "
      "recall." + _c("nz-medcan-reg6") + " Its job is to let a regulator, an auditor, or a new "
      "employee understand the entire system in one read."),
    p("Every controlled document looks like this one: it carries a document ID (WSO-QM-001), a version "
      "(1.0), a status (Active), an effective date (15 June 2026) and a fixed next-review date "
      "(15 June 2028). The manual is structured to the New Zealand Code of GMP, based on PIC/S "
      "PE009-14, and supports the Minimum Quality Standard under the Misuse of Drugs (Medicinal "
      "Cannabis) Regulations 2019." + _c("pics-pe009-ch1") + _c("nz-medcan-reg6")),
    callout("note", "An honest distinction",
      p("The company explicitly does <strong>not</strong> claim GMP certification. The manual describes "
        "a system <em>designed to meet</em> GMP, a normal and honest stance for a maturing facility, "
        "and one we come back to at the end.")),
    figure(grid([
        card("Tier 1: Apex", "Quality Policy + Quality Manual. The 'why' and the system overview. Points down to everything below.", "POL / QM"),
        card("Tier 2: SOPs", "Standard Operating Procedures: step-by-step instructions for how each task is done.", "SOP"),
        card("Tier 3: Specs", "Specifications: the acceptance criteria. What 'good' looks like for a material or product.", "SPEC"),
        card("Tier 4: Records", "Forms, logs and registers. The actual evidence that the work was done as written.", "FRM / REG"),
      ], cols=2), 1,
      "The documentation pyramid. The manual points downward to procedures; completed records flow "
      "back up as the evidence that the system works."),
    figure(L.flow("The product lifecycle the manual governs",
            [("Propagate", "genetics & clones"), ("Cultivate", "veg & flower"),
             ("Harvest", "cut & weigh"), ("Dry / Cure", "stabilise"),
             ("Process", "manufacture"), ("Package", "label & lot"),
             ("Store", "controlled"), ("Release", "QA decision"),
             ("Distribute", "ship & trace")],
            note="A recall loop runs backward across every stage. See the traceability section."), 2,
      "One manual governs the whole chain from a mother plant to a shipped, traceable product."),
  ]})

SECTIONS.append({"id": "key-terms", "kicker": "Vocabulary first", "title": "The acronyms you must know before anything else",
  "blocks": [
    p("GMP quality systems run on a dense layer of acronyms, and you genuinely cannot read a manual "
      "without them. Don't memorise the lot. The four load-bearing ideas are GMP (the rulebook), "
      "the QMS/PQS (the machine that delivers quality), the SOP (the instructions) and ALCOA+ (the test "
      "every record must pass). For plant material specifically, GACP governs the growing side, because "
      "cannabis starts as a botanical crop, not a factory chemical."),
    defterm("GMP: Good Manufacturing Practice", "The rulebook for making medicines safely and "
            "consistently. Here, the NZ Code of GMP based on PIC/S PE009."),
    defterm("GACP: Good Agricultural and Collection Practice", "The growing-side equivalent of GMP, "
            "covering cultivation and the starting plant material."),
    defterm("QMS / PQS: Quality (or Pharmaceutical) Management System", "The whole organised system "
            "that delivers quality, modelled on ICH Q10."),
    defterm("QA vs QC", "Quality Assurance sets and checks the system and makes release decisions, "
            "independent of production. Quality Control does the actual testing."),
    defterm("SOP: Standard Operating Procedure", "The approved step-by-step instructions for a task."),
    defterm("ALCOA+", "The nine-part data-integrity standard every record must meet: Attributable, "
            "Legible, Contemporaneous, Original, Accurate, plus Complete, Consistent, Enduring, "
            "Available." + _c("mhra-data-integrity")),
    defterm("CAPA / QRM / RP", "Corrective and Preventive Action, Quality Risk Management, and the "
            "Responsible Person who authorises release."),
    table(["Acronym", "Plain-English meaning"], [
      ["GMP", "Good Manufacturing Practice: the safe-medicine rulebook"],
      ["GACP", "Good Agricultural & Collection Practice: the growing-side rules"],
      ["QMS / PQS", "The whole quality system (PQS = the pharma name for it)"],
      ["QA", "Quality Assurance: sets/checks the system, decides release"],
      ["QC", "Quality Control: runs the lab tests"],
      ["SOP", "Standard Operating Procedure: the step-by-step instructions"],
      ["CAPA", "Corrective And Preventive Action: fix it and stop it recurring"],
      ["QRM", "Quality Risk Management: scale effort to actual patient risk"],
      ["RP", "Responsible Person: authorises release, the regulator's contact"],
      ["ALCOA+", "The 9-part data-integrity test for every record"],
      ["PIC/S", "Inspection scheme that publishes the PE009 GMP guide"],
      ["ICH", "Body that publishes Q9 (risk) and Q10 (quality system)"],
      ["MQS", "Minimum Quality Standard: the NZ medicinal-cannabis bar"],
      ["OOS", "Out Of Specification: a result that fails its acceptance criteria"],
    ], cls="compact", caption="The working vocabulary of a cannabis quality manual."),
    callout("tip", "Two bodies you'll see everywhere",
      p("<strong>PIC/S</strong> publishes the PE009 GMP guide that the NZ Code is built on. "
        "<strong>ICH</strong> publishes Q9 (how to manage risk) and Q10 (the quality-system model). "
        "The example manual is built on all three." + _c("ich-q9-risk") + _c("ich-q10-pqs") + _c("pics-pe009-ch1"))),
  ]})

SECTIONS.append({"id": "gmp-principles", "kicker": "Core idea 1", "title": "GMP principles: quality is built in, not tested in",
  "blocks": [
    p("The foundational GMP principle is blunt: <strong>you cannot inspect quality into a product at "
      "the end</strong>. It has to be designed and controlled at every step. The example system is "
      "built on the ICH Q10 Pharmaceutical Quality System model and PIC/S PE009 Part I Chapter 1, and "
      "it threads a few non-negotiables through everything: defined roles, written procedures, "
      "contemporaneous records, risk-based decisions and continual improvement." + _c("ich-q10-pqs") + _c("pics-pe009-ch1")),
    p("A second principle is <strong>independence</strong>. Quality Assurance must be able to make "
      "release and rejection decisions independent of production and cultivation, including the "
      "authority to halt operations or reject product if patient safety is at risk." + _c("pics-pe009-ch1") +
      " The third is the <strong>golden thread of traceability</strong>: every plant, batch and "
      "material must be followable forward and backward through its entire life."),
    ul(["Quality is the responsibility of every employee, but final authority for release sits with QA and the Responsible Person, never with production alone.",
        "The <strong>Responsible Person (RP)</strong> authorises product release, approves recalls, oversees security and reconciliation of controlled material, and is the regulator's point of contact.",
        "QA has the explicit authority to reject materials or products and to stop operations where quality or patient safety may be compromised.",
        "The system runs on a risk-based approach (ICH Q9): controls are scaled to the actual risk to the patient and product."]),
    figure(grid([
        card("Senior Management", "Owns the quality system, provides resources, chairs Management Review.", "Top"),
        card("Production / Cultivation", "Grows, harvests, processes, manufactures. Makes the product, but cannot release it.", "Operations"),
        card("Quality Assurance", "Independent branch. Holds the release/reject veto and the authority to stop the line. Does NOT report through Production.", "Veto"),
      ], cols=3), 3,
      "QA sits as a separate branch with an independent veto on release that does not pass through "
      "Production." + _c("pics-pe009-ch1")),
    figure(L.zones("Build-in vs test-in quality (where the checks happen)",
            0, 10,
            [(8, 10, L.REDL, "Test-in: one gate at the very end"),
             (0, 10, L.GL, "Build-in: a checkpoint at every stage")],
            unit=" lifecycle",
            note="Test-in catches failures only after all the cost is spent. Build-in controls quality the whole way through."), 4,
      "The core GMP idea, drawn. A single end-of-line inspection (red) cannot rescue a product; "
      "checkpoints at every stage (green) build quality in."),
    callout("key", "Who can say 'ship it'",
      p("Only QA and the Responsible Person. Production can make a perfect batch and still not release "
        "it. That separation of duties is the whole point, and it is what an auditor checks first.")),
  ]})

SECTIONS.append({"id": "documents-records", "kicker": "Core idea 2", "title": "SOPs, records and the documentation hierarchy",
  "blocks": [
    p("A quality system is, in practice, a documentation system, and its unofficial motto is "
      "<strong>&lsquo;if it isn't written down, it didn't happen.&rsquo;</strong> The hierarchy runs "
      "from the Quality Policy and Quality Manual at the apex, down through SOPs (how to do each task), "
      "Specifications (the acceptance criteria), and finally the Forms, Logs and Registers that capture "
      "the actual evidence." + _c("pics-pe009-ch1")),
    p("Every controlled document carries a unique ID, version number, owner, effective date and review "
      "date, and only the current approved version is available at the point of use. Superseded copies "
      "are withdrawn and marked. The <strong>Master Document Register (REG-QM-001)</strong> is the "
      "keystone: the single authoritative index where every controlled document has exactly one row."),
    defterm("Good Documentation Practice (GDP)", "Entries made at the time of the activity, in "
            "indelible form. Corrections are a single line through the error (still legible), "
            "initialled, dated and reasoned, never obliterated, overwritten or back-dated." + _c("mhra-data-integrity")),
    ul(["Documents follow a numbering convention by type and area, e.g. SOP-QM-001 (procedure), FRM-QM-001 (form), REG-QM-001 (register), SPEC-MF-001 (specification).",
        "Records are retained for a defined period, e.g. batch records kept at least one year after expiry, subject to regulation and licence conditions.",
        "Only one approved version exists at the point of use; the register makes the current version unambiguous."]),
    figure(L.flow("The controlled-document lifecycle",
            [("Draft", "author writes"), ("Review", "QA & owner check"),
             ("Approve", "authorised sign-off"), ("Issue", "version assigned"),
             ("Train", "staff trained"), ("Effective", "in use at the bench"),
             ("Review", "periodic re-check"), ("Revise", "or withdraw/archive")],
            note="The loop closes: a periodic review either confirms, revises (new version) or withdraws the document."), 5,
      "Every document moves through this loop. Nothing goes live until it is approved, issued and "
      "trained out."),
    figure(grid([
        card("TYPE", "SOP, FRM (form), REG (register), SPEC, POL (policy). What kind of document it is.", "SOP"),
        card("AREA", "QM = quality, MF = manufacturing, CU = cultivation, QC = quality control, SD = storage/distribution.", "QM"),
        card("NUMBER", "A sequential number allocated from the Master Document Register.", "001"),
      ], cols=3), 6,
      "Anatomy of a document ID: <strong>SOP-QM-001</strong> = a Standard Operating Procedure, in the "
      "Quality area, number 001."),
    callout("warn", "The bench copy must be current",
      p("The most common documentation slip is an out-of-date SOP left at the workstation. If the copy "
        "in someone's hand isn't the current approved version, the work done from it is non-compliant. "
        "That is exactly why the register exists.")),
  ]})

SECTIONS.append({"id": "traceability-data", "kicker": "Core idea 3", "title": "Traceability, batch records and data integrity",
  "blocks": [
    p("<strong>Traceability</strong> means any finished product can be traced <em>back</em> to the "
      "exact plants, materials, equipment, people and conditions that made it, and "
      "<em>forward</em> to where every unit went. The example system uses batch numbering and a "
      "Batch/Lot Traceability Register (REG-CU-001) that consolidates materials used, processing "
      "activities, personnel, equipment, in-process results and final disposition onto the batch "
      "record (FRM-MF-004)."),
    p("Data integrity is the modern frontier. All GxP data, paper or electronic, must "
      "meet ALCOA+, and electronic systems must add Annex 11 / PI 041 controls: unique user logins, "
      "role-based access, secure and reviewed audit trails, synchronised clocks and validated backups." + _c("mhra-data-integrity") + _c("eu-gmp-annex11") + _c("pics-pi041-data")),
    ul(["Batch records (FRM-MF-004) tie together every input and action for a batch; the Batch/Lot Traceability Register (REG-CU-001) consolidates the golden thread from plant to product.",
        "Electronic GMP records need Annex 11 / PI 041 controls: unique user IDs, role-based access, enabled and reviewed audit trails, controlled system time, tested backups, and validation for GMP use.",
        "Quarantine and status control keep untested or suspect material physically and/or electronically segregated until a release decision is made."]),
    callout("warn", "An honest flag about Home Assistant",
      p("The manual is candid that its Home Assistant sensor layer (temperature, humidity, CO2, VPD) "
        "is <strong>not</strong> a validated GMP records system in its standard configuration and "
        "cannot be presented as one until validated. Until then, HA-sourced records are backed by an "
        "independent verified control, recorded in REG-QM-008." + _c("eu-gmp-annex11"))),
    figure(L.flow("The golden thread: one batch ID, followed all the way",
            [("Mother", "genetics"), ("Clone", "propagated"),
             ("Cultivation batch", "veg & flower"), ("Harvest lot", "cut & weighed"),
             ("Dried / cured lot", "stabilised"), ("Processed batch", "manufactured"),
             ("Finished unit", "released & shipped")],
            note="A backward-trace arrow runs the other way: from any unit on the market, back to the exact mother plant."), 7,
      "Every step shares the batch ID, so any finished unit traces back to its source plant and "
      "forward to its destination."),
    table(["ALCOA+ attribute", "What it means for a record", "Fail example"], [
      ["<strong>Attributable</strong>", "You know who did it and when", "An unsigned, undated entry"],
      ["<strong>Legible</strong>", "Readable and permanent", "Scribble; pencil that can be erased"],
      ["<strong>Contemporaneous</strong>", "Recorded at the time of the activity", "Filled in at end of shift from memory"],
      ["<strong>Original</strong>", "The first record, or a verified true copy", "A re-written 'tidy' version, original binned"],
      ["<strong>Accurate</strong>", "Correct, no errors, matches reality", "A transcription typo on a result"],
      ["<strong>Complete</strong>", "Nothing left out, including reruns", "A failed test quietly omitted"],
      ["<strong>Consistent</strong>", "In sequence, dates/times in order", "Steps logged out of order"],
      ["<strong>Enduring</strong>", "Survives the full retention period", "Thermal paper that fades; lost file"],
      ["<strong>Available</strong>", "Retrievable for review/audit", "Archived where no one can find it"],
    ], cls="compact", caption="ALCOA+ as a checklist. Every record, paper or electronic, must pass all nine." + _c("mhra-data-integrity")),
  ]})

SECTIONS.append({"id": "how-to-build", "kicker": "Do it", "title": "How to stand up a quality system, step by step",
  "blocks": [
    p("Building a QMS is sequential, not all-at-once. You start with the apex documents, define the "
      "organisation and roles, then create the spine of operational quality: the core registers and "
      "their forms. Each register is a standalone controlled document that grows only by adding rows, "
      "never by restructuring, and that stability is exactly what makes it auditable over years."),
    steps([
      ("Approve the apex documents", "Sign off the Quality Policy and Quality Manual. These define intent and the system overview."),
      ("Publish the org chart and roles", "Define the Responsible Person, QA, QC and personnel responsibilities, and the QA independence line."),
      ("Stand up the Master Document Register", "REG-QM-001 becomes the single index; from here on, every document ID is allocated from it."),
      ("Build the core quality processes", "Document Control, Deviations, Change Control, CAPA, Risk Management and Management Review, each with its SOP, form and register."),
      ("Layer in operations", "Cultivation/GACP, manufacturing, QC testing, storage/distribution and supplier qualification, all pointing back to the same registers."),
      ("Train everyone, then run it", "Train staff out on the live procedures, run the system, and close the loop with Management Review at least annually."),
    ]),
    figure(L.flow("The build-out sequence",
            [("Policy & Manual", "apex"), ("Roles", "RP/QA/QC"),
             ("Master Register", "REG-QM-001"), ("Core processes", "the 6 quality SOPs"),
             ("Operations", "GACP/MF/QC/SD"), ("Train", "staff competent"),
             ("Run & Review", "annual cycle")],
            note="Each stage depends on the one before it. You can't allocate IDs before the Master Register exists."), 8,
      "Stand the system up in order. The Master Document Register has to exist before any other "
      "document can be numbered."),
    figure(grid([
        card("Master Document", "The keystone index of every controlled document.", "REG-QM-001"),
        card("Deviation", "Logs anything that didn't go to plan.", "REG-QM-004 / FRM-QM-001"),
        card("Change Control", "Gates any change to the validated state.", "REG-QM-005 / FRM-QM-003"),
        card("CAPA", "Drives fixes to root cause and prevents recurrence.", "REG-QM-006 / FRM-QM-002"),
        card("Risk", "Records risk assessments (ICH Q9).", "REG-QM-007"),
        card("Computerised Systems", "Tracks system validation status (incl. Home Assistant).", "REG-QM-008"),
        card("Audit", "Logs internal/external audits and findings.", "REG-QM-009 / FRM-QM-004"),
        card("Batch Traceability", "The golden thread from plant to product.", "REG-CU-001 / FRM-MF-004"),
      ], cols=2), 9,
      "The core register spine. Each register pairs with a form and grows only by adding rows."),
    callout("tip", "Registers grow by rows, not redesigns",
      p("A good register is boring on purpose. You add a numbered row for each event and never "
        "restructure the columns. Years later, an auditor can read the whole history in one stable, "
        "unbroken table.")),
  ]})

SECTIONS.append({"id": "pitfalls", "kicker": "Watch out", "title": "Common pitfalls that fail audits",
  "blocks": [
    p("Most GMP findings are not exotic. They are predictable documentation and discipline "
      "failures. In fact, analyses of regulatory inspections find that data-integrity and "
      "documentation problems dominate the warning letters issued." + _c("rogers-data-integrity-2020") +
      " The classic traps are records filled in later rather than contemporaneously, corrections that "
      "obliterate the original entry, superseded SOP versions left in use at the bench, and changes "
      "made to validated equipment or processes without formal change control."),
    p("A subtler trap is <strong>overclaiming</strong>: presenting an unvalidated system (like a stock "
      "sensor/automation platform) as a GMP records source. The example manual avoids this by "
      "explicitly declaring its Home Assistant layer non-validated and supporting it with an "
      "independent control until proven." + _c("eu-gmp-annex11")),
    ul(["<strong>Back-dating or end-of-shift batch-completing</strong> breaks 'Contemporaneous', the single most common data-integrity finding.",
        "<strong>Whiteout, overwriting, or a hidden correction</strong> violates GDP: corrections must leave the error legible.",
        "<strong>Old document versions at the point of use</strong>: if the bench copy isn't current, the work is non-compliant.",
        "<strong>Skipping the Change Control Request (FRM-QM-003)</strong> for facility, equipment, computerised-system or process changes puts the validated state at risk.",
        "<strong>Treating audits as a pass/fail exam</strong> rather than a source of CAPA: findings must be classified by impact and driven to root cause."]),
    figure(L.flow("From event to closure: deviation → CAPA",
            [("Detect", "something's off"), ("Contain", "protect product"),
             ("Deviation", "FRM-QM-001"), ("Classify", "minor/major/critical"),
             ("Investigate", "root cause"), ("QA decision", "product impact"),
             ("CAPA", "FRM-QM-002"), ("Effectiveness", "did it work?"),
             ("Close", "trend → review")],
            note="Trended deviations and CAPA feed Management Review, the loop that proves the system improves."), 10,
      "Deviations are classified, investigated to root cause, and driven through CAPA, the "
      "structured response auditors expect." + _c("arunagiri-capa-2024")),
    figure(L.zones("A failing record vs a compliant one",
            0, 10,
            [(0, 5, L.REDL, "Late entry, scribbled-out fix, old SOP version"),
             (5, 10, L.GL, "Contemporaneous, single-line correction, current version")],
            unit=" record",
            note="The same data, two outcomes: the red record fails an audit on data integrity alone."), 11,
      "What separates a finding from a clean record is rarely the science. It's the discipline "
      "of how the record was made." + _c("mhra-data-integrity")),
    callout("danger", "Change control is non-negotiable",
      p("Any change that touches a validated facility, piece of equipment, computerised system or "
        "process must go through a Change Control Request (FRM-QM-003) approved by QA <em>before</em> "
        "implementation. Skipping it silently invalidates the qualified state, and auditors look "
        "for exactly this.")),
  ]})

SECTIONS.append({"id": "expectations", "kicker": "Reality check", "title": "Realistic expectations: a manual is a starting point, not a finish line",
  "blocks": [
    p("A written quality manual proves <strong>intent and design</strong>, not yet proven performance. "
      "The example deliberately separates &lsquo;a system designed to meet GMP&rsquo; from "
      "&lsquo;GMP certification&rsquo;, and it is peppered with <strong>FACILITY INPUT</strong> "
      "placeholders, for retention periods, classification criteria, closure timeframes, "
      "validation status and named role-holders, that the facility must complete before the "
      "system is real." + _c("nz-medcan-reg6")),
    ul(["A v1.0 manual with open FACILITY INPUT items is normal: it defines the framework, and the facility populates the specifics (retention periods, KPIs, thresholds, named RP).",
        "Validation is ongoing work: computerised systems, equipment and processes need documented qualification before their records can be fully relied on as GMP records.",
        "The system only demonstrates effectiveness over time, through trended deviations/CAPA, completed audits, and at least annual Management Review.",
        "Continual improvement is the intended end-state, not a one-time project: the manual reviews on a fixed two-year cycle and updates via its own change control."]),
    figure(L.line("How demonstrated compliance matures after go-live",
            [(0, 10), (1, 22), (2, 33), (3, 45), (4, 58), (5, 68), (6, 78), (7, 86)],
            ["v1.0 issue", "+3mo", "+6mo", "+9mo", "+12mo", "+15mo", "+18mo", "+24mo"],
            ylab="demonstrated compliance %", ymin=0, ymax=100,
            note="The curve climbs as registers fill, validation completes and Management Reviews accumulate. The manual is the starting point, not the peak."), 12,
      "A v1.0 manual sits at the bottom of this curve. Demonstrated compliance is earned over months "
      "of evidence, not granted on the day the manual is signed."),
    table(["Open 'FACILITY INPUT' item", "What it needs", "Where it lives"], [
      ["Named Responsible Person", "An appointed, qualified RP", "Org chart / roles"],
      ["Record retention periods", "Defined durations per record type", "Document Control SOP"],
      ["Deviation classification & closure", "Minor/major/critical criteria + timeframes", "REG-QM-004 / SOP-QM-004"],
      ["Home Assistant validation", "Qualification status of the sensor layer", "REG-QM-008"],
      ["Quality KPIs and targets", "Measurable goals reviewed at Management Review", "Management Review SOP"],
    ], cls="compact", caption="Typical open items a facility must close to make the framework real."),
    callout("key", "The honest stance is itself a quality signal",
      p("Flagging open requirements, like the unvalidated Home Assistant data flow, "
        "rather than papering over them is a marker of a credible quality culture, not a weakness. A "
        "manual that admits what isn't done yet is more trustworthy than one that claims everything is "
        "finished.")),
    p("Treat the manual as the framework, then earn the evidence. From here, see how raw sensor data "
      "becomes a defensible signal in the <a href='signal-and-noise.html'>signal and noise</a> paper, "
      "and how a validated root-zone measurement chain is built in the "
      "<a href='root-zone-teros12.html'>root-zone sensor</a> guide."),
  ]})
