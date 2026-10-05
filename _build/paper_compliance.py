# -*- coding: utf-8 -*-
"""Paper: compliance, licensing and track-and-trace — the paperwork spine of a licensed grow."""
import json, os
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        grid, card, chip, kv, steps)
import figs_lib as L

_FIGS = json.load(open(os.path.join(os.path.dirname(__file__), "figs_compliance.json"), encoding="utf-8"))

SLUG = "compliance-track-trace"
TITLE = "Compliance, licensing and track-and-trace"
EYEBROW = "Facility · Compliance"
SUB = ("A cultivation facility with a license must have many documents and records. After you read "
       "this paper, you will know how to read and examine your license. You will know how to trace "
       "a batch from the mother plant to the package lot. You will know how to do an inventory "
       "reconciliation, find the cause of each variance and write records that an auditor accepts. "
       "You will also know how to record a deviation. Then the deviation does not become a large "
       "problem.")
META = [("shield", "Compliance"), ("image", "9 diagrams"),
        ("quote", "14 sources"), ("clock", "~24 min to read")]
RELATED = ["gmp-hash-lab", "daily-checks", "auckland-ipm-blueprint"]
REF_IDS = ["eu-gmp-vol4", "nz-mca-activities", "au-odc-single-licence", "au-odc-medcan",
           "nz-mca-scheme", "pics-pe009-guide", "metrc-platform", "ca-dcc-ctt",
           "or-sos-audit-2019", "fda-data-integrity-2018", "who-gacp-2003",
           "ema-gacp-rev1", "au-tga-mc-quality", "nz-mc-regs-2019"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

# ---------------------------------------------------------------- 1. start here
SECTIONS.append({"id": "start-here", "kicker": "Start here", "title": "Purpose and scope",
  "blocks": [
    callout("danger", "Information, not legal advice",
      p("This paper shows <em>in general terms</em> how licensing, traceability and records operate "
        "for cannabis. Thus you know the terms, and how the system operates, before you read the "
        "documents of your regime. This paper is not legal advice and is not regulatory advice. It "
        "does not give information on a specified facility.</p><p>Regimes are different in each "
        "country and they change with time. In <strong>August 2026</strong>, we examined the "
        "information about each regime in this paper. The regimes will change, and then this "
        "information will not be correct. Your license and the information that your regulator "
        "gives at this time are more important than this paper. The legal advice from your lawyer "
        "is also more important than this paper.")),
    lead("Plant growth is one half of the task. The other half is to <em>show</em> facts to a "
         "person who was not there. You must show, on paper and at all times, where each gram came "
         "from and where it went. You must also show that you obeyed the written procedures of your "
         "facility. This paper is about the system of records that shows these facts."),
    p("This paper is for a person who has new compliance tasks and also applies water to the "
      "plants. Examples are an operator with a first license and a small group of personnel in "
      "which the head grower is also the quality manager. A technician who speaks with an auditor "
      "for the first time can also use this paper. It is not necessary to know compliance before "
      "you read this paper. This paper gives information about each term before it uses the term."),
    p("This paper shows the license and its life. It shows the communication between your facility "
      "and the regulator. It shows batches and lots, and the genealogy that connects all records. "
      "It shows seed-to-sale traceability and the regular reconciliation of the inventory. It shows "
      "records that an auditor accepts. It shows how to record deviations with a minimum of "
      "documents.</p><p>It gives information about the boundary between GACP and GMP, and about "
      "quality agreements. It shows security and destruction. It shows how to prepare for a recall. "
      "It shows the steps of an audit day. At the end, there are two worked examples in general "
      "terms, from New Zealand and Australia."),
  ]})

# ---------------------------------------------------------------- 3. vocabulary
SECTIONS.append({"id": "key-terms", "kicker": "Terms", "title": "Definitions",
  "blocks": [
    p("When two persons use the same term for different items, a problem occurs in the compliance "
      "work. These definitions are general. The definitions in the regulations of your regime are "
      "more important than these definitions. When you start a facility, one task is to write the "
      "definitions that <em>you</em> use."),
    defterm("License and permit", "A license gives approval for an operation. It gives the name of "
            "the licensee, the activities and the conditions. Many regimes add permits. A permit is "
            "a secondary approval in the limits of the license. It is for a specified time and a "
            "specified quantity. For example, a permit can give approval to cultivate this crop, in "
            "this period, in this quantity."),
    defterm("Condition", "A condition is an instruction that the license contains. A condition is "
            "not optional. If you operate against a condition, you operate without the approval of "
            "the license."),
    defterm("Batch", "A batch is a specified quantity of material that you make in one operation. "
            "The material must be the same in all parts. In cultivation, a batch is a group of "
            "plants that you start together and that receive the same treatment."),
    defterm("Lot", "A lot is a batch or one part of a batch. Some regimes use the terms batch and "
            "lot for the same item. In your documents, write the definition that you use and do not "
            "change it."),
    defterm("Genealogy", "The genealogy is the sequence of batches and lots, in which each one "
            "comes from the one before it. The sequence is: the mother plant, the cuttings, the "
            "vegetative batch, the flower batch, the harvest lot and the package lot. The records "
            "of each batch or lot are also part of the records of all the batches and lots that "
            "follow it."),
    defterm("Seed-to-sale / track-and-trace", "Seed-to-sale and track-and-trace are two names for a "
            "continuous inventory system for a controlled substance. Each plant and each package "
            "has an identification. The system records each movement, each change of the material "
            "and each destruction as an event."),
    defterm("UID and tag", "A UID is an identification that is different for each plant or package. "
            "It stays attached to the plant or package. It can be a barcode, an RFID tag or a "
            "number in a logbook. The UID connects the item to its record."),
    defterm("Manifest", "A manifest is the document for a movement of material between two sites. "
            "It gives the material, the quantity, who sends it, who receives it, the carrier and "
            "the times. It is the chain of custody while the material is in movement."),
    defterm("Reconciliation", "In a reconciliation, you compare two numbers that you record "
            "independently and that must agree. One example is the stock in the ledger and the "
            "stock that you count. A second example is the wet weight, and the dry weight plus the "
            "weight of the water and the waste. Drift between the two numbers is the usual audit "
            "finding."),
    defterm("Deviation", "A deviation is each difference between your work and your written "
            "procedure. You record the deviation, examine its effect and complete it. CAPA "
            "(corrective and preventive action) is the loop that corrects the cause and not only "
            "the symptom."),
    defterm("ALCOA+", "The properties of a good record in ALCOA+ are Attributable, Legible, "
            "Contemporaneous, Original and Accurate, plus Complete, Consistent, Enduring and "
            "Available."),
    defterm("GACP / GMP", "GACP (Good Agricultural and Collection Practice) is for cultivation and "
            "primary processing. GMP (Good Manufacturing Practice) is for the change of plant "
            "material into a medicine. In your documents, the boundary between the two is clear."),
    defterm("CoA", "A CoA is a Certificate of Analysis. It is a document with the signature of a "
            "laboratory and the results of the tests on a specified lot. It goes with the lot."),
    defterm("Quality agreement", "A quality agreement is a document with the signatures of two "
            "parties, for example a grower and a processor, or a licensee and a laboratory. It "
            "divides the quality tasks between the two parties. It tells who does the tests. It "
            "tells who gives approval for the lot to go from the site, and who tells the other "
            "party about a problem."),
  ]})

# ---------------------------------------------------------------- 2. core answer
SECTIONS.append({"id": "spine", "kicker": "In short", "title": "Primary task of compliance: control with records",
  "blocks": [
    lead("Each regulation in each cannabis regime tells you to do one primary task: <strong>show "
         "control</strong>. Control of the material is the first part. Material comes into the "
         "facility, moves in the facility and moves out of the facility only when the records show "
         "it. Control of the work is the second part. The work on the plant obeys written "
         "procedures. The records must show this control to a person who was not there and who "
         "accepts only the records."),
    figure(L.flow("Layers of compliance",
            [("License", "approval to operate, with conditions attached"),
             ("Quality system", "the written procedures of your facility"),
             ("Records", "records show that you obeyed the procedures"),
             ("Audit", "an auditor compares records to procedures")],
            note="Each layer is important because of the layer before it. Records without procedures, or procedures without records, do not show compliance."), 1,
      "The four layers of compliance. The license gives approval to operate. The quality system "
      "gives the procedures for your work. The records show that you obeyed the procedures. An "
      "audit compares the records with the procedures."),
    p("Most new operators give too much work to layer one, the license. They do not give sufficient "
      "work to layer three, the records. This method is incorrect. A regulator does not usually "
      "remove a license on the day that it gives the license. The regulator removes it after some "
      "years, in layer three, when an auditor wants a basic fact that the documents cannot "
      "show.</p><p>In GMP for medicines, documents are not a secondary task. The quality system "
      "includes the documents" + _c("eu-gmp-vol4") + ". Cannabis regimes use the same structure."),
    callout("key", "Test with a person who was not there",
      p("Write each record for a person who was not there. This person does not know the facts, "
        "examines the record carefully and accepts only the facts that the record shows. If this "
        "person can find the facts from your records only, your records are correct. The facts are "
        "the person, the task, the time, the quantity and the cause. If you must stay near the "
        "record and tell the facts, it is not a record. It is a note for you.")),
  ]})

# ---------------------------------------------------------------- 4. licence anatomy
SECTIONS.append({"id": "licence-anatomy", "kicker": "The license", "title": "License activities, conditions and renewals",
  "blocks": [
    p("A cannabis license is not one approval. It is a <strong>group of activities with "
      "names</strong>. The activities have conditions. For example, the regime of New Zealand makes "
      "each license from some of these activities: cultivation, nursery (the supply of seeds and "
      "propagation material), research, possession for manufacture, and supply" +
      _c("nz-mca-activities") + ".</p><p>In December 2021, Australia changed its Commonwealth "
      "structure to one medicinal cannabis license. This license can include cultivation, "
      "production, manufacture and research, with permits in the limits of the license" +
      _c("au-odc-single-licence") + ". The names are different in the two regimes. The structure is "
      "the same in almost all regimes: <em>activities plus conditions plus quantities</em>."),
    p("Read your license as a system with these parts:"),
    kv([
      ("Licensee and site", "A license connects a legal person to a site. For a new legal person, a new "
       "site or new rooms, you usually make a variation or a new application. Make the variation or "
       "the new application before the change, not after the change."),
      ("Activities", "The license gives the activities that you can do. If you do an activity that "
       "the license does not give, you operate without a license. Examples are extraction and "
       "supply when the license is only for cultivation. The certificate on the wall does not "
       "change this fact."),
      ("Conditions", "Conditions include the security of the facility and the persons who have "
       "access to the material. They include the tasks to keep records and to send reports. Some "
       "licenses also give the names of responsible persons. The conditions are the license."),
      ("Quantities and permits", "Many regimes set a maximum quantity in the license. They give "
       "permits for each crop, each period or each quantity, in the limits of the license" +
       _c("au-odc-medcan") + "."),
      ("End date and renewal", "A license or a permit ends on a specified date. When it ends, the "
       "operation must stop. The operation must stop also if a crop is in progress."),
    ]),
    figure(L.flow("Life of a license",
            [("Application", "fit-and-proper checks, site, security, procedures"),
             ("Approval", "with activities and conditions attached"),
             ("Operation", "records, notification of changes, reports"),
             ("Inspection", "document or site, findings to complete"),
             ("Renewal", "always on time, or stop the operation")],
            note="The license has a life cycle. It is not a certificate that you get one time."), 2,
      "The life cycle of a license. The primary work is in the steps after approval: operation in "
      "the limits of the conditions, notifications, inspections and renewal before the end date."),
    p("Two methods prevent most problems with a license. The first method is a <strong>compliance "
      "calendar</strong>. The compliance calendar has each end date, each renewal period, each date "
      "for a report and each fee. Set alerts for 90, 60 and 30 days before each date. A renewal is "
      "an easy task. If you do not make the renewal on time, the operation stops.</p><p>The second "
      "method is to make <strong>variations before the change, not documents after the "
      "change</strong>. If you want to add a room, an activity or a key person, the general "
      "instruction is the same in all regimes. Get the approval of the regulator first. Then do the "
      "change. Operators who do this incorrectly usually know the instruction. They think that no "
      "person will find the error."),
    callout("tip", "Read your license each three months",
      p("Make a paper copy of the license. Read each condition to the personnel who operate the "
        "rooms. Operators frequently find conditions in the license that they did not know. The "
        "usual cause is that the person who made the application is not at the facility at this "
        "time. No other person knows the conditions.")),
  ]})

# ---------------------------------------------------------------- 5. regulator
SECTIONS.append({"id": "regulator", "kicker": "The regulator", "title": "Inspections, notifications and variations",
  "blocks": [
    p("The regulator is not a customer. The regulator is not against you. The regulator is "
      "<strong>external quality assurance with the authority of the regulations</strong>. The task "
      "of the regulator is to make sure that you have control. Each item that the regulator wants "
      "to examine is for this task.</p><p>In New Zealand, this function is in a dedicated agency in "
      "the Ministry of Health. The agency operates the scheme and its licensing" + _c("nz-mca-scheme") +
      ". In Australia, the function is in the Office of Drug Control at the Commonwealth level" +
      _c("au-odc-medcan") + ". In all regimes, there are three types of communication between you "
      "and the regulator:"),
    table(["Type", "Direction", "Typical triggers", "Primary instruction"], [
      ["<strong>Notification</strong>", "You &rarr; them", "Theft of material, missing material, "
       "security incidents, important deviations, changes to key persons or to other facts about "
       "the licensee",
       "Tell the regulator before the regulator wants the information. For the regulator, concealment is much worse than an error."],
      ["<strong>Inspection</strong>", "Them &rarr; you", "A scheduled cycle, the approval or "
       "renewal of a license, a complaint, or the same problem in many of your reports",
       "Tell the inspector only the facts that you know. If you are not sure, tell the inspector: &lsquo;I will examine this and write to you.&rsquo;"],
      ["<strong>Variation</strong>", "You &rarr; them", "New rooms, new activities, new responsible "
       "persons, or changes to the security or to the procedures",
       "Get approval before you make the change. A variation after the change is a breach."],
    ], cls="compact", caption="The three types of communication with the regulator."),
    p("Your communication with the inspector during an inspection is more important than most "
      "operators think. Do not tell the inspector during the inspection that a finding is "
      "incorrect. If you think that a finding is incorrect, write to the regulator after the "
      "inspection. Give records that show the facts. Write notes of all the information that the "
      "inspector tells you.</p><p>Make sure that you can correct each finding. If a finding is too "
      "general, tell the inspector and continue until you can correct it. Write to the regulator "
      "before the date that the regulator gives. Give a date for each task that you will do. Then "
      "do the tasks.</p><p>A finding that occurs again at the next inspection is worse than the "
      "first finding, because it shows if your system corrects its errors. Regulators want to know "
      "this fact most of all."),
    callout("warn", "The term &lsquo;usually&rsquo; causes the most problems in an inspection",
      p("An example is &lsquo;we usually record that&rsquo;. The term &lsquo;usually&rsquo; shows "
        "that the written procedure and the work are different, and then the inspector knows the "
        "difference. If the work is different from the SOP, correct the SOP or the work. Use a "
        "change note. Do this before a different person finds the difference.")),
  ]})

# ---------------------------------------------------------------- 6. batches
SECTIONS.append({"id": "batches", "kicker": "Batches and lots", "title": "Batch and lot traceability",
  "blocks": [
    lead("A batch is a specified quantity of material that comes from the same procedure at the "
         "same time. Thus the material is the same in all parts. One test result, one record and "
         "one decision are then correct for all of the batch. Traceability is correct only when "
         "each batch is the same in all parts."),
    p("In a grow room, <strong>plants that you start together and that get the same treatment are a "
      "batch</strong>. When the treatment is different, you have two batches. Examples are a "
      "different room, a different feed, or a spray on some plants and not on other plants. You "
      "have two batches also if you do not record the difference. Make the documents agree with the "
      "plants, and not the plants with the documents.</p><p>GMP quality systems give a careful "
      "definition of batch and lot. In these systems, the traceability must include all material "
      "that goes into each batch" + _c("pics-pe009-guide") + ". Small operators frequently have "
      "problems not because their definitions of batches are incorrect, but because they <em>put "
      "batches together and divide batches without a record</em>."),
    figure(_FIGS["genealogy"], 3,
      "The genealogy from one mother plant to the package lots and the waste. The amber marks show "
      "which batches and lots have one record. An IPM spray that you record for the mother plant on "
      "1 March is in the records of each gram from that plant, always."),
    p("Thus the records of one plant are important. In the genealogy, each record is also part of "
      "the records of <strong>all the batches and lots that follow it</strong>. The spray on the "
      "mother plant is part of the pesticide records of the package lot, four steps after the "
      "mother plant. A CoA for a package lot shows the facts about the lot only if the sequence "
      "before it has no gap.</p><p>The opposite is also correct. A <em>missing</em> record causes a "
      "problem for all the material after it, because you cannot show that an event did not occur. "
      "If the spray log has a gap of three weeks, you cannot show that you did not spray that crop."),
    ul([
      "<strong>Make IDs that a person can read and that are different for each batch.</strong> An "
      "example is the ID CL-2603 (clones, week 26, batch number 2003). This ID is better than "
      "&lsquo;the back table&rsquo; and better than a UUID. You can use a different system for IDs. "
      "Write your system for IDs in your documents.",
      "<strong>To divide a batch, or to put batches together, is an event.</strong> If you put two "
      "harvest lots together in one dry lot, record the change. Record the weight before the change "
      "and the weight after the change. Do not do it without a record.",
      "<strong>Do not let material stay without an ID</strong>, also for a short time. Containers "
      "of wet trim with no label are where traceability stops.",
    ]),
    callout("key", "Small batches decrease the damage",
      p("When a problem occurs, for example a test with an unsatisfactory result, a pest or a "
        "possible contamination, the full batch has the problem. The cause is that the batch is the "
        "largest unit that your records can show. Small batches with a correct definition decrease "
        "the damage. With small batches, you discard only the small batch. With one large batch "
        "that has a general definition, one unsatisfactory test can cause you to discard the full "
        "room.")),
  ]})

# ---------------------------------------------------------------- 7. track and trace
SECTIONS.append({"id": "track-trace", "kicker": "Track-and-trace", "title": "Seed-to-sale traceability and reconciliation",
  "blocks": [
    p("Track-and-trace is a continuous inventory system for a controlled substance. It has three "
      "parts: <strong>identification</strong>, <strong>events</strong> and a "
      "<strong>ledger</strong>. Each plant and each package has an identification, which is a tag "
      "or a UID. You record each event when it occurs. The events are each movement, each change of "
      "the material, each sample and each destruction.</p><p>The ledger contains all of the "
      "records. The ledger can be a system that the regulator tells you to use, commercial "
      "software, or a paper logbook. The method is the same for all of them."),
    p("The US state model is a good worked example. Some systems, for example METRC, give tags for "
      "plants and tags for packages. Licensees record growth stages, harvests, changes of the "
      "material, transfers and destructions with these IDs, in the time periods that the system "
      "gives" + _c("metrc-platform") + ". In California, each licensee with a commercial license "
      "must record all cannabis activity, from cultivation to sale, in the track-and-trace system "
      "of the state, CCTT-Metrc. The system uses an identification that is different for each plant "
      "and package" + _c("ca-dcc-ctt") + ".</p><p>In New Zealand and Australia (in 2026), there is "
      "no ledger of this type that the state operates. The same functions are in your records and "
      "in the reports that you send to the regulator. The software is different in each regime. The "
      "terms and the structure are the same for all regimes."),
    figure(_FIGS["movemap"], 4,
      "The seed-to-sale diagram of movements. The identification changes with the material: plant "
      "tags, then harvest batches, then package UIDs. The diamonds mark the reconciliation points, "
      "where two numbers that you record independently must agree."),
    p("These methods are correct for all software:"),
    ul([
      "<strong>The stock in the room must be equal to the ledger.</strong> The room and the ledger "
      "must show the same facts at all times. A gap between them, in each direction, is a finding.",
      "<strong>Record each event when it occurs</strong>, at the location where it occurs. If you "
      "record the movements of the day at 5 pm, and you did not record them when they occurred, you "
      "cause drift.",
      "<strong>Weigh the material at each change.</strong> Record the wet weight at harvest and the "
      "dry weight after drying. Record the weight of waste at trim and the net weight at packaging. "
      "The differences show the quantity of moisture and the quantity of waste. Auditors examine "
      "these differences carefully.",
      "<strong>Material goes from the facility only as a recorded transfer, a recorded sample or a "
      "recorded destruction.</strong> There is no fourth type. &lsquo;I gave some to the person at "
      "the laboratory&rsquo; is a sample with an entry in the log, or it is diversion.",
      "<strong>Write the manifest before the material moves.</strong> The manifest gives the "
      "material, the quantity, who sends it, who receives it and the carrier. When the material "
      "comes to the site that receives it, the two sites compare the material with the manifest.",
    ]),
    callout("note", "A spreadsheet is permitted. A spreadsheet with no new data is not permitted.",
      p("A spreadsheet or a paper ledger can be correct in a small facility if you obey these "
        "conditions. You make each entry at the time of the event. You know who made each entry. "
        "You keep a copy of the ledger. No person changes an entry without a record.</p><p>The tool "
        "is not usually the problem. A track-and-trace system with no new data until Friday causes "
        "risk, also if the cost of the system was high.")),
  ]})

# ---------------------------------------------------------------- 8. reconciliation
SECTIONS.append({"id": "reconciliation", "kicker": "The #1 finding", "title": "Inventory reconciliation and drift",
  "blocks": [
    lead("Inventory reconciliation is an audit test. Each person can do the test and read the "
         "result. The ledger shows one quantity, the scales show a different quantity, and you must "
         "find the cause of the difference. Thus a variance with no known cause is a primary cause "
         "of an unsatisfactory audit for a small operator. The test is very easy to do, and "
         "falsification of the result after the event is not easy."),
    p("The causes of drift are not unusual. One cause is that the moisture in the flower decreases "
      "during curing and no person records the change of moisture. A second cause is that personnel "
      "put trim in the bin and do not record the weight. A third cause is that QC samples and "
      "laboratory samples do not go into the ledger. A fourth cause is that personnel record the "
      "wet weight in one unit and the dry weight in a different unit. A fifth cause is that, on the "
      "harvest day, material moves between rooms faster than personnel write the "
      "movements.</p><p>No cause in this list is diversion. In the records, diversion and each "
      "cause in this list <em>show the same data</em>. In a regime for controlled substances, "
      "missing material with no known cause is possible diversion, until you show that it is not. "
      "When the state auditors of Oregon examined their system for recreational cannabis, they "
      "found two primary problems when the system must find diversion. The system uses data from "
      "reports that the operators write, and the quality of the data in the track-and-trace system "
      "is unsatisfactory" + _c("or-sos-audit-2019") + "."),
    table(["Item", "Quantity", "Source"], [
      ["Opening stock (dried flower)", "12.40 kg (27.3 lb)", "Last stock count that you examined"],
      ["+ In: dried flower from the new harvest", "9.60 kg (21.2 lb)", "Dry-room log with dates"],
      ["&minus; Out: transfers to the processor", "4.80 kg (10.6 lb)", "Manifests with the signatures of the two sites"],
      ["&minus; Out: destruction of waste", "1.20 kg (2.6 lb)", "Destruction records, witnessed"],
      ["&minus; Out: lab samples", "0.03 kg (1.1 oz)", "Sample log with lot IDs"],
      ["<strong>= Calculated stock</strong>", "<strong>15.97 kg (35.2 lb)</strong>", "Calculated from the items above"],
      ["Counted stock", "15.71 kg (34.6 lb)", "Two persons, on the same day"],
      ["<strong>Variance</strong>", "<strong>&minus;0.26 kg (9.2 oz), &minus;1.6%</strong>",
       "Examine, find the cause and record it, on the same day"],
    ], cls="compact", caption="An example of a reconciliation. It is easy to calculate the numbers. The primary task is to do the reconciliation at regular intervals and to record each variance as an event that has a written result. The figures are examples."),
    p("The correction is a regular schedule and correct records. <strong>Count one area each "
      "week</strong> and count the full inventory each month. Write an investigation for each "
      "variance on the day that you find it. Do this also if the result is: &lsquo;The moisture "
      "decreased in the typical range. We changed the typical value.&rsquo; Give the ledger one "
      "owner.</p><p>Also write the value that you use for the change of moisture. For example, you "
      "can write that the weight decreases by 75&ndash;80% from the wet weight to the dry weight. "
      "Then the largest change of weight with a known cause is not a gap in your records."),
    callout("warn", "Do not adjust the ledger without a record",
      p("Do not change the ledger to agree with the stock count without a recorded investigation. A "
        "person can think that this change is a correction. In a ledger for controlled substances, "
        "it is falsification.</p><p>You remove the record of the difference. You replace it with a "
        "record that shows that all numbers agreed. An auditor accepts small variances that have a "
        "written cause. An auditor does not accept a ledger that you made clean.")),
  ]})

# ---------------------------------------------------------------- 9. records
SECTIONS.append({"id": "records", "kicker": "Records", "title": "Records for an audit and ALCOA+",
  "blocks": [
    p("Regulators in all countries use the same definition of a good record. The usual name of this "
      "definition is <strong>ALCOA</strong>. The properties are Attributable, Legible, "
      "Contemporaneous, Original and Accurate. Personnel also add Complete, Consistent, Enduring "
      "and Available (ALCOA+). The US FDA uses these properties in its document about data "
      "integrity for the manufacture of medicines" + _c("fda-data-integrity-2018") +
      ". Cannabis auditors use the same structure without a change."),
    figure(_FIGS["record"], 5,
      "One entry in a log, with notes. Each ALCOA+ property is a small task. Write your initials. "
      "Use permanent ink. Write at the time of the event. Keep the first record. Make a "
      "strike-through on an error and do not erase it."),
    p("These methods are for a small facility:"),
    ul([
      "<strong>Use a logbook with a number on each sheet</strong>, or a digital system that records "
      "each change. Loose sheets of paper, and spreadsheets that a person can change without a "
      "record, make an auditor think that you changed the records.",
      "<strong>Write in the work area, not in a different room.</strong> A log that hangs in the "
      "work area is better than good software in a different room. It makes the correct procedure "
      "the easiest procedure.",
      "<strong>To correct an entry: make a strike-through with one line, write your initials, the "
      "date and the cause.</strong> You can read the incorrect value below the strike-through. Do "
      "not use a pencil or correction fluid. Do not remove sheets from the logbook. Do not put a "
      "copy of records with errors in a new logbook. The first record with the errors is the record.",
      "<strong>Do not keep a field empty.</strong> Make a strike-through on each field that does "
      "not apply. An auditor can think of the worst cause for an empty field.",
      "<strong>Keep records for years, not for months.</strong> The minimum period is different in "
      "each regime. It is usually in the conditions of your license. The storage of records must "
      "continue to be available when personnel change and when a device does not operate.",
    ]),
    p("The property Contemporaneous causes the most problems. The cause is that a backfilled record "
      "shows signs. An example is a week of entries that one person wrote with one pen, in one "
      "handwriting and at one time. The sheets are clean and the times are all round numbers. A "
      "second example is a digital log in which twenty entries have almost the same system time on "
      "the night before the inspection.</p><p>Auditors use the methods of forensic document "
      "examination when they examine logbooks. If an auditor finds a backfilled record, the result "
      "is worse than for a gap that you tell the auditor about. A gap causes one finding. A "
      "backfilled record causes the auditor to reject all your other records."),
    callout("tip", "Prepare the record before the task",
      p("For each usual task, select the minimum correct record, which is one entry with five "
        "fields. Make the form short. You can then complete it in less than one minute. A "
        "compliance system is defective at the point where the work for the record is more than the "
        "work for the task.")),
  ]})

# ---------------------------------------------------------------- 10. deviations
SECTIONS.append({"id": "deviations", "kicker": "If a problem occurs", "title": "Deviations and corrective actions",
  "blocks": [
    p("A deviation is each difference between your work and your written procedure. Some examples: "
      "the dehumidifier stopped in the night, or the feed mixture had an incorrect EC. Other "
      "examples: personnel sprayed the incorrect room, or a supply of material came with no "
      "documents. The deviation is not the primary problem. <strong>The primary problem is a "
      "deviation that you did not record</strong>, because then your system does not find its "
      "deviations. To find deviations is the primary task of a quality system" + _c("pics-pe009-guide") +
      "."),
    figure(L.flow("Steps of a deviation",
            [("Find", "work is different from the written procedure"),
             ("Record", "on the same day, in the log"),
             ("Examine", "effect on the product and the batches"),
             ("Correct", "correct the problem immediately"),
             ("Prevent", "change to prevent it again"),
             ("Check", "examine it after a time")],
            note="CAPA for a small group: the full loop. A small deviation can stop at 'Correct'. Record that decision too."), 6,
      "The deviation loop. A corrective action corrects this deviation. A preventive action changes "
      "the system. The last step is a check, some weeks after the correction, to make sure that the "
      "problem does not occur again."),
    table(["Field", "Contents"], [
      ["The event", "Write only the facts. Do not write who is at fault."],
      ["Who found it, and when", "Date, time, initials"],
      ["Batches and material with the deviation", "Always write the IDs. The IDs connect the log to the product."],
      ["First correction", "The tasks that you did in the first hour"],
      ["Effect on the product", "Decision for each batch: continue, hold, lower the grade, or send to destruction."],
      ["Root cause", "For an important deviation: find the cause in the system that let it occur."],
      ["Change to prevent a new deviation", "SOP changed, alarm added, training completed, with dates"],
      ["Completed by and examined by", "A second person makes sure, some weeks after, that the problem does not occur again"],
    ], cls="compact", caption="A minimum deviation log. Eight fields on one sheet are better than a procedure that no person uses."),
    p("Set the depth of the record for the size of the deviation. A check that you did not do on "
      "one day gets a record of three lines, and you complete it on the same day. A feed from the "
      "incorrect tank that touched two flowering batches gets a check of the effect on the product, "
      "and a root cause.</p><p>In your procedure, give each deviation a type: small, important or "
      "very important. Then the procedure gives the depth of the record. The depth does not change "
      "with the decision of a person at that time. An auditor does not want a facility with no "
      "deviations. The auditor wants <em>records that show that you find deviations, examine the "
      "effect on the product and complete the loops</em>."),
    callout("key", "An empty deviation log is a bad sign, not a good sign",
      p("Each facility has deviations. A log with no entries does not show a facility with no "
        "errors. It shows that &lsquo;no person examines the facility&rsquo;, or that "
        "&lsquo;personnel correct problems without a record&rsquo;. A good log with many small "
        "deviations that personnel completed correctly is one of the best documents that you can "
        "give to an inspector.")),
  ]})

# ---------------------------------------------------------------- 11. gacp/gmp + quality agreements
SECTIONS.append({"id": "gacp-gmp", "kicker": "The boundary", "title": "GACP, GMP and quality agreements",
  "blocks": [
    p("Two systems apply from seed to medicine. <strong>GACP</strong> (Good Agricultural and "
      "Collection Practice) is for the cultivation, harvest and primary processing of plants for "
      "medicine. It includes the identification of the plant, hygiene, the materials that you apply "
      "to the plants, documents, and traceability at the cultivation site. The primary document is "
      "the guideline of the WHO of 2003" + _c("who-gacp-2003") + ".</p><p>The European medicines "
      "regulator has a GACP guideline for herbal starting materials. In 2025, the regulator changed "
      "this guideline. The new guideline includes cultivation in a room with a controlled "
      "environment" + _c("ema-gacp-rev1") + ".</p><p><strong>GMP</strong> (Good Manufacturing "
      "Practice) is for the change of this material into a medicine. It includes validated "
      "processes, batch manufacturing records, QC release, and a quality unit that operates "
      "independently" + _c("eu-gmp-vol4") + ". The PIC/S GMP guide aligns the GMP procedures of the "
      "inspection authorities of many countries. These include the authorities of New Zealand and "
      "Australia" + _c("pics-pe009-guide") + "."),
    figure(_FIGS["boundary"], 7,
      "The boundary between GACP and GMP. The tasks of cultivation are on the left side. The tasks "
      "of manufacture are on the right side. Three documents let material go across the boundary: "
      "lot records, CoAs and the quality agreement."),
    p("The position of the boundary is different in each regime, and it is important for your "
      "business. Cultivation, drying and trimming are usually in GACP. Extraction, formulation and "
      "packaging of the medicine are in GMP. For example, the TGA of Australia uses GMP for the "
      "manufacture of the product. Cannabis cultivation supplies starting material, and GACP is the "
      "system for it. A mandatory quality standard, TGO 93, sets the product quality" +
      _c("au-tga-mc-quality") + ".</p><p>In 2026, examine the information from your regulator about "
      "the position of the boundary. The position of the boundary gives the system for your dry "
      "room. An error in each direction has a high cost."),
    p("For a grower, the result of the boundary is that <strong>you are a supplier of starting "
      "material to a GMP site</strong>. GMP tells that site to do a qualification of each supplier. "
      "Auditors of the processor, and auditors of the regulator, can examine your facility. Your "
      "GACP documents (genealogy, records of the materials that you apply, drying logs and CoAs) "
      "show to the processor that you control the starting material.</p><p>The <strong>quality "
      "agreement</strong> is the document for this. It divides the quality tasks between the two "
      "parties, with the signature of each party. Thus no task is missing because each party thinks "
      "that the other party has the task."),
    table(["Clause", "Information in the clause"], [
      ["Specifications and CoA tasks", "The specification of the material, who does each test, and which laboratory does it"],
      ["Sampling and retained samples", "Who collects the samples and how, who keeps the retained samples, and for how long"],
      ["Deviation notification", "Who must tell the other party, how fast, if a problem occurs at one of the two parties"],
      ["Change notification", "Changes to the cultivar, the materials that you apply, the site and the procedures. No change to the supplied material without a notification."],
      ["Complaints and recall tasks", "Who is the primary person, who tells the regulator, the time limits, and the persons to contact when personnel are not at work"],
      ["Approval for an audit", "The processor can do an audit of the grower. The clause gives the areas that the audit includes and how long before the audit the processor must tell the grower."],
      ["Records and storage", "Who keeps each record, for how long, and access to the records when the other party wants them"],
      ["Approval of lots", "The persons: who gives approval for the lot to go from the site, and who gives approval for the product to go to the market"],
    ], cls="compact", caption="Typical clauses of a quality agreement between a grower and a processor. The same structure is for your testing laboratory: methods, custody of samples, procedures for results out of specification, and who sees the results first."),
    callout("note", "The same applies to a laboratory",
      p("A quality agreement with a testing laboratory is the same type of document. It includes "
        "the methods and the detection limits that the two parties accept. It includes the chain of "
        "custody for samples. It includes the procedure for a result out of specification, with a "
        "second test and notification. It includes the time to get the results.</p><p>If you have "
        "no quality agreement with the laboratory, an unusual result is a large problem. With a "
        "good quality agreement, the same result is a step in a procedure.")),
  ]})

# ---------------------------------------------------------------- 12. security + destruction
SECTIONS.append({"id": "security-waste", "kicker": "Custody", "title": "Security, access and destruction records",
  "blocks": [
    p("Each regime gives its security instructions in the conditions of the license. Examples are "
      "safes, the type of alarm, and the number of days that you keep the camera records. Thus this "
      "section gives only general information. The same fact is correct in all regimes: "
      "<strong>controlled material must stay in controlled custody</strong>. You show custody with "
      "records, and you show all other facts with records."),
    ul([
      "<strong>Use layers, not one large lock.</strong> The layers are the site, the building, the "
      "room and the container. Each layer decreases the speed of an intruder, and decreases the "
      "number of persons who have approval to be in it.",
      "<strong>Access has two lists.</strong> The first list shows who <em>has approval</em> to go "
      "in. It is a list of approvals that you keep and sign. The second list shows who <em>did</em> "
      "go in. It has the entry logs, the logbooks of keys and codes, and the visitor logbook with "
      "the name of the escort. Auditors compare the two lists.",
      "<strong>Personnel who start and personnel who stop work at the facility.</strong> The usual "
      "finding is a code of a person who stopped work at the facility, and the code continues to "
      "operate some months after. When a person stops work at the facility, do these tasks on the "
      "same day. Cancel the codes, collect the keys and change the lists. Make a record.",
      "<strong>Each visitor must have an escort, and you must record each visitor.</strong> "
      "Contractors are also visitors. An electrician in the flower room is in your chain of custody "
      "while the door is open.",
    ]),
    p("<strong>Waste is also controlled material.</strong> Waste includes trim, fan leaves from "
      "flowering plants, rejected lots, and plants with no life. In most regimes, cannabis waste "
      "stays in the custody of the licensee until you destroy it and record the destruction. The "
      "bin is not an exit from track-and-trace. The destruction is an <em>event</em>, and a "
      "transfer is also an event."),
    table(["Parts of a destruction record that an auditor accepts", "Function"], [
      ["Date, time, location", "Shows when and where the event occurred"],
      ["Material and batch or lot IDs", "Connects the destruction to the genealogy"],
      ["Weight before destruction", "Completes the mass balance"],
      ["Method", "How you destroyed the waste. After this, no person can use it or get it again."],
      ["Done by and witnessed by", "Two persons and two signatures are the best control against diversion."],
      ["Approval", "A responsible person makes sure that the record has all the data"],
    ], cls="compact", caption="Destruction records complete the loop for each gram that does not become product."),
    callout("warn", "Flower that you can identify, in an open container",
      p("Buds that you can identify, in an open container, with no destruction and no record, are a "
        "diversion finding. A photo from a drone can show them.</p><p>Destroy the waste with a "
        "method that your regime accepts. Weigh the waste. Witness the destruction. Record the "
        "destruction. After the destruction, the material is only waste. Before the destruction, "
        "the material is stock.")),
  ]})

# ---------------------------------------------------------------- 13. recall
SECTIONS.append({"id": "recall", "kicker": "Recall", "title": "How to prepare for a recall, and mock recalls",
  "blocks": [
    p("A recall is traceability in an emergency. Material that went from the facility can be "
      "defective, and you must find all of it quickly. You must also show that you found all of it. "
      "A GMP system must have a recall procedure, and personnel must do a test of the procedure" +
      _c("pics-pe009-guide") + ". The smallest grower with a license can use the same method. The "
      "task is the same at all sizes: you must find <em>where each gram of that lot went</em>."),
    p("To prepare for a recall, you must use the genealogy in the two directions. <strong>Trace "
      "back</strong> from a product in the market to each material, room, person and procedure that "
      "touched it. <strong>Trace forward</strong> from a possible source of the problem to each lot "
      "and each customer that received material from it. The source can be one mother plant, one "
      "supply of nutrients, or one dry room. We recommend that you use only records for the two "
      "directions, and that you do it in hours."),
    figure(_FIGS["recall"], 8,
      "The traceability test for one lot with an unsatisfactory result. You trace forward to each "
      "destination: the processor, other lots from the same mother plants, the retained sample, and "
      "the waste with its destruction record. You find each destination and record its status. At "
      "the end, you complete the mass balance."),
    p("The <strong>mock recall</strong> is the test of the recall procedure. Select a lot randomly. "
      "Simulate an unsatisfactory test result for the lot. Do all the steps of the recall on paper, "
      "and measure the time. No material moves. The output is a report with the time.</p><p>In many "
      "quality schemes for supply chains, the usual target is a reconciliation of almost all of the "
      "quantity on the same day. The time is hours, not weeks. Write your target in a document, and "
      "measure against it."),
    figure(L.flow("The mock recall test",
            [("Select a lot", "random, not your best lot"),
             ("Trace forward", "each destination from records only"),
             ("Find and hold", "simulate quarantine at each site"),
             ("Mass balance", "sent + held + samples + waste = 100%"),
             ("Report", "time and gaps in a report"),
             ("Correct gaps", "the gaps are the result")],
            note="Do this test before a regulator, a customer or a journalist does it for you. The report is a good record for an audit."), 9,
      "The mock recall as a test that you can do again. Do not do the test to get a good result. Do "
      "the test to find the part of the sequence of records that is weak when time is short. No "
      "material is at risk."),
    p("In most first tests, these problems occur. A transfer has no lot ID, and then the manifest "
      "cannot show <em>which</em> lot the processor received. A retained sample is in the SOP, but "
      "is not on the shelf. The weight of waste is not accurate, and then you cannot complete the "
      "mass balance. Each problem is easy to correct on a usual day, at a low cost. It is very bad "
      "to find the problem during a recall that is not a test."),
  ]})

# ---------------------------------------------------------------- 14. audit day
SECTIONS.append({"id": "audit-day", "kicker": "Audit day", "title": "The steps of an audit day",
  "blocks": [
    p("Inspections are different. An inspection can be with or without a notification. It can be a "
      "document inspection or an on-site inspection. It can be usual or because of a "
      "trigger.</p><p>The structure of a good audit day is always the same. You complete 90% of the "
      "work before the inspector comes. The audit day follows a sequence of steps."),
    steps([
      ("Notification received",
       "Write to the regulator. Make sure that you know the areas, the date, the time and the "
       "persons who will come. Tell your key persons the date. If the regulations tell a "
       "responsible person to be at the inspection, make sure that the person is there."),
      ("Inspection before the audit",
       "Examine your facility against your SOP index and the conditions of your license. Correct "
       "each problem that you can correct, and record the facts. Do not backfill records. A gap "
       "that the auditor finds is one finding. A backfilled record that the auditor finds is a "
       "large problem."),
      ("Prepare the front room",
       "Prepare these documents: the license and its conditions, the chart of the personnel, the "
       "SOP index and the training records. Prepare the logs, the findings of the last inspection "
       "and the records that show how you completed them. Make sure that you can find each document "
       "in minutes."),
      ("Opening meeting",
       "Make sure that you and the inspector have the same information about the areas, the time "
       "and the sequence. Select one person for all communication with the inspector. This person "
       "records each document that you give to the inspector. All other personnel tell the "
       "inspector only the facts that the inspector wants. They do not tell facts that they do not "
       "know."),
      ("The walk",
       "The inspectors monitor your work and compare it with the procedures. They examine gowning, "
       "logs in the work area, labels on containers, and locks that operate. Tell only the facts "
       "that you know. If you are not sure, tell the inspector: &lsquo;I will examine this and "
       "write to you.&rsquo; Write the task in your notes. Do not tell the inspector that the "
       "inspector is incorrect."),
      ("The document room",
       "Record each document that the inspector wants. Identify each copy as a copy. Keep the "
       "initial documents. If there is no record, tell the inspector. Tell the inspector how you "
       "will correct the gap. The correction is more important than the gap."),
      ("Closing meeting",
       "Write each finding with the information that the inspector gives. Make sure that you know "
       "each finding. If a finding is too general, tell the inspector and continue until you can "
       "correct it. Do not tell the inspector at this time that a finding is incorrect. If you "
       "think that a finding is incorrect, write to the regulator after the inspection. Give "
       "records that show the facts."),
      ("The report to the regulator",
       "Write to the regulator before the date that the regulator gives. For each finding, give the "
       "corrective action, the preventive action, the date and the owner. Then do these tasks and "
       "keep the records that show them. The next audit starts with these records."),
    ]),
    h(3, "The usual problems of small operators"),
    p("Operators usually do not want to cause damage. Operators do not frequently have problems "
      "because they do not know cultivation. The problems occur again and again, and they come from "
      "the structure of the facility. You can find each problem before it occurs:"),
    grid([
      card("The backfilled logbook",
        p("A person writes three weeks of checks for each day on the night before the inspection, "
          "with one pen, in one handwriting, on clean sheets. An auditor identifies this "
          "immediately. It changes a small gap into a large problem of data integrity. "
          "<strong>Correction:</strong> record the gaps correctly, with a note that gives the date "
          "and the cause."), tag="records"),
      card("The change of the ledger without a record",
        p("A person changes the ledger to agree with the stock count, with no investigation and no "
          "note. It shows concealment, because it is concealment. <strong>Correction:</strong> each "
          "variance gets a written result, also if the variance is small."), tag="inventory"),
      card("The &lsquo;usually&rsquo; that is not in the SOP",
        p("The work changed during some years, and it is different from the SOP. All personnel know "
          "the procedure that they use. The inspector then has a record that shows that your system "
          "is not correct. <strong>Correction:</strong> change the SOP or the work, with a change "
          "note, this month."), tag="procedure"),
      card("The SOP that no person uses",
        p("The procedures are good, and a person wrote them for the license application. No person "
          "opened them after that. The personnel did not read them. <strong>Correction:</strong> "
          "short SOPs that personnel use, a check of the SOPs on the compliance calendar, and "
          "records of training."), tag="procedure"),
      card("The code of a person who stopped work at the facility",
        p("Alarm codes and keys continue to operate for months after a person stops work at the "
          "facility. On paper, a person without approval has access to the facility. That access is "
          "a breach of a security condition. <strong>Correction:</strong> a checklist for the same "
          "day when a person stops work at the facility, with a record."), tag="security"),
      card("The loop that no person completed",
        p("Personnel accept the findings of the last audit and give dates for the corrections. Then "
          "no person does the corrections. A finding that occurs again is worse, because it shows "
          "that the system does not correct its errors. <strong>Correction:</strong> keep the "
          "findings on the compliance calendar until a second person examines the corrections."), tag="follow-up"),
    ], cols=2),
  ]})

# ---------------------------------------------------------------- 15. worked examples
SECTIONS.append({"id": "worked-examples", "kicker": "Two regimes", "title": "Worked examples: NZ and Australia",
  "blocks": [
    callout("warn", "Information with a date: make sure that it is correct before you make a decision",
      p("This section shows two regimes in general terms. The information is from <strong>August "
        "2026</strong>. The examples show the general terms of this paper in two regimes. Regimes "
        "change.</p><p>The regulations change, the regulator gives new information, and agencies "
        "change their structure. Before you make a decision, read the information that the "
        "regulator gives at this time. The documents of the regulator are at the end of this "
        "section. Get legal advice.")),
    h(3, "New Zealand, the Medicinal Cannabis Scheme"),
    p("The Medicinal Cannabis Agency, in the Ministry of Health, operates the scheme of New "
      "Zealand. The regulations for the scheme are the Misuse of Drugs (Medicinal Cannabis) "
      "Regulations 2019. They started on 1 April 2020" + _c("nz-mc-regs-2019") +
      ". The license has activities with names: cultivation, nursery, research, possession for "
      "manufacture and supply. An operator makes an application for the activities that the "
      "facility must have" + _c("nz-mca-activities") + ".</p><p>A product must have a minimum "
      "quality standard before the operator supplies it. Thus cultivation records that obey GACP, "
      "and manufacture that obeys GMP, are important for an operator that wants to supply the "
      "market for medicines" + _c("nz-mca-scheme") + ". A license has conditions for security, "
      "records and reports, and it has renewal cycles. The Agency gives the documents with "
      "information for the application, and the Agency does the inspections."),
    h(3, "Australia, ODC licensing, TGA quality"),
    p("Australia divides the task at the Commonwealth level. The Office of Drug Control gives "
      "licenses for cultivation, production, manufacture and research. The Narcotic Drugs Act 1967 "
      "gives the regulations for these licenses" + _c("au-odc-medcan") + ". Since 24 December 2021, "
      "one medicinal cannabis license can include these activities, with permits for quantities in "
      "the limits of the license" + _c("au-odc-single-licence") + ".</p><p>The product quality is "
      "the task of the Therapeutic Goods Administration. GMP is the system for manufacture. "
      "Cultivation supplies starting material, and GACP is the system for it. Medicinal cannabis "
      "products that you supply in Australia must obey a mandatory quality standard, TGO 93" +
      _c("au-tga-mc-quality") + ". The regulations of the states and territories add more layers to "
      "the Commonwealth regulations."),
    p("The two regimes show the general structure of this paper. There is a <strong>license with "
      "activities</strong> and conditions. There are <strong>permits or controls of "
      "quantity</strong> in the limits of the license. There is a <strong>quality standard</strong> "
      "that makes GACP and GMP necessary for decisions about cultivation. <strong>Tasks for "
      "security, records and reports</strong> are conditions of the license. When you know this "
      "structure, you can read the documents of your regime with it."),
    ul([
      "<a href='https://www.health.govt.nz/regulation-legislation/medicinal-cannabis/information-for-industry/about-the-medicinal-cannabis-scheme'>NZ Medicinal Cannabis Agency, about the scheme</a>",
      "<a href='https://www.health.govt.nz/regulation-legislation/medicinal-cannabis/information-for-industry/licence-activities'>NZ, license activities</a>",
      "<a href='https://www.legislation.govt.nz/regulation/public/2019/0321/latest/LMS285243.html'>NZ, Misuse of Drugs (Medicinal Cannabis) Regulations 2019</a>",
      "<a href='https://www.odc.gov.au/medicinal-cannabis'>AU Office of Drug Control, medicinal cannabis</a>",
      "<a href='https://www.tga.gov.au/resources/guidance/complying-quality-requirements-medicinal-cannabis'>AU TGA, quality standard for medicinal cannabis</a>",
    ]),
  ]})

# ---------------------------------------------------------------- 16. field guide
SECTIONS.append({"id": "field-guide", "kicker": "Reference", "title": "Troubleshooting and the basic facts of control",
  "blocks": [
    table(["Symptom", "Possible cause", "Correction"], [
      ["Variance in the stock count each month", "Moisture and waste that you did not record",
       "Write the value for the change of moisture. Weigh all waste. Count one area each week."],
      ["The inspector finds gaps between the SOP and the work", "The work changed and the documents did not change",
       "Read the SOPs with the personnel each three months. Use change notes. Do not let the work change without a record."],
      ["No records for some days", "One person had the task and was not at work",
       "Give training to more than one person for each task. Write the minimum set of records for each day. Record gaps correctly."],
      ["The site that receives the material does not accept the transfer", "The manifest is too general. It has no lot IDs and no weights for the transfer.",
       "Weigh the material at the two sites and compare it with the manifest. Write your signature on the manifest. Make photos of the seals."],
      ["You cannot connect the laboratory result to a batch", "No record of the sampling",
       "Sample log with the lot ID, the weight, the date, who collected the sample, and the chain of custody"],
      ["A renewal that you did not make on time, or a permit that stopped", "No compliance calendar",
       "One compliance calendar with each date, alerts at 90, 60 and 30 days, and one owner"],
      ["The deviation log has no entries for one year", "Personnel think that a deviation record causes a bad result for them, or no person examines the log",
       "Do not give a bad result to a person who records a deviation. Count each near-miss. Examine the log each month with all personnel."],
      ["The auditor does not accept the destruction", "No witness, no method and no weights",
       "Two persons for each destruction. The method is always the same. The weight before the destruction. An approval."],
    ], cls="compact", caption="The compliance symptoms that occur again and again, and their easy and good corrections."),
    callout("key", "The structure of compliance",
      p("Operate your facility for an audit on the next day. The auditor is a person who was not "
        "there and who accepts only paper. The <strong>license</strong> gives the activities that "
        "you can do. The <strong>records</strong> show the work that you did.</p><p>The "
        "<strong>reconciliation</strong> shows that no material is missing. The "
        "<strong>genealogy</strong> shows the connection between all records. A gram, an hour or a "
        "decision that the records do not show is a finding. The methods in this paper make these "
        "four facts correct.")),
    p("Read these papers next. The paper <em>Daily checks</em> goes with this paper. It shows how "
      "to make the set of records for each day. This set decreases the cost of all the work in this "
      "paper.</p><p>The paper about <em>GMP hash manufacturing</em> gives information about the "
      "work on the GMP side of the boundary. There your lots become the starting material of a "
      "different party. The IPM papers show that the spray log that you keep for compliance also "
      "helps to prevent damage to your crop."),
  ]})
