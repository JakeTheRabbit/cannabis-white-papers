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
SUB = ("A licensed grow is a paperwork machine with a garden attached. This guide maps the spine: "
       "what a licence actually is, how batches and lots connect every gram to its history, how "
       "seed-to-sale tracking works, and how to keep records an auditor believes.")
META = [("shield", "Compliance"), ("image", "9 diagrams"),
        ("quote", "Evidence-linked · 14 sources"), ("clock", "~24 min read")]
RELATED = ["gmp-hash-lab", "daily-checks", "auckland-ipm-blueprint"]
REF_IDS = ["eu-gmp-vol4", "nz-mca-activities", "au-odc-single-licence", "au-odc-medcan",
           "nz-mca-scheme", "pics-pe009-guide", "metrc-platform", "ca-dcc-ctt",
           "or-sos-audit-2019", "fda-data-integrity-2018", "who-gacp-2003",
           "ema-gacp-rev1", "au-tga-mc-quality", "nz-mc-regs-2019"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

# ---------------------------------------------------------------- 1. start here
SECTIONS.append({"id": "start-here", "kicker": "Start here", "title": "What This Is. And What It Is Not",
  "blocks": [
    callout("danger", "Education, not legal advice",
      p("This paper explains how cannabis licensing, traceability and record-keeping work <em>in "
        "general terms</em>, so the vocabulary and the logic make sense before you read your own "
        "regime's documents. It is not legal advice, it is not regulatory advice, and it describes "
        "no specific facility. Regimes differ by country and change over time; the regime "
        "descriptions here were checked in <strong>August 2026</strong> and will drift. Your "
        "licence, your regulator's current guidance and your lawyer outrank every sentence on "
        "this page.")),
    lead("Growing the plant is half the job. The other half is being able to <em>prove</em>, to a "
         "stranger, on paper, at any moment, where every gram came from, where it went, and that "
         "you did what your own rules say you do. That proof system is what this paper is about."),
    p("It is written for the person who just got handed &lsquo;compliance&rsquo; along with the "
      "watering: the first-licence operator, the small team where the head grower is also the "
      "quality manager, the technician who has never met an auditor. No prior knowledge is "
      "assumed. Every term is defined before it is used."),
    p("The route: what a licence actually is and how it lives; how to deal with the regulator; "
      "batch and lot thinking (the genealogy that connects everything); seed-to-sale tracking and "
      "the reconciliation habit; records that survive an audit; deviations without the "
      "bureaucracy; the GACP/GMP boundary and quality agreements; security and destruction; "
      "recall readiness; a walkthrough of audit day; and two real regimes, New Zealand and "
      "Australia, described from altitude as worked examples."),
  ]})

# ---------------------------------------------------------------- 2. core answer
SECTIONS.append({"id": "spine", "kicker": "Core answer", "title": "The Core Answer: Prove Control, to a Stranger, on Paper",
  "blocks": [
    lead("Every rule in every cannabis regime compresses to one demand: <strong>demonstrate "
         "control</strong>. Control of the material, nothing enters, moves, or leaves except as "
         "recorded. Control of the process. What happens to the plant follows written rules. And "
         "the demonstration must work for someone who was not there and trusts nothing but the "
         "record."),
    figure(L.flow("The paperwork spine",
            [("Licence", "permission to operate, with conditions attached"),
             ("Quality system", "the rules you wrote for your own operation"),
             ("Records", "proof that you followed your own rules"),
             ("Audit", "a stranger tests proof against rules")],
            note="Each layer only means something because of the layer before it. Records without rules prove nothing; rules without records are decoration."), 1,
      "The four layers of compliance. The licence grants permission, the quality system defines "
      "how you operate, records evidence that you did, and audits test the records against the "
      "rules."),
    p("Most new operators obsess over layer one, getting the licence, and starve layer three. "
      "That is backwards. Licences are rarely lost on the day they are granted; they are lost "
      "years later, at the records layer, when an auditor asks a simple question the paperwork "
      "cannot answer. In pharmaceutical GMP, documentation is not admin support for the real "
      "work; it is defined as part of the quality system itself" + _c("eu-gmp-vol4") + ", and "
      "cannabis regimes borrow that DNA directly."),
    callout("key", "The stranger test",
      p("Write every record for a reader who was not in the room, knows nothing, and is mildly "
        "suspicious. If a competent stranger can reconstruct what happened (who, what, when, how "
        "much, why) from your records alone, you pass. If the record only makes sense with you "
        "standing next to it explaining, it is not a record; it is a memory aid.")),
  ]})

# ---------------------------------------------------------------- 3. vocabulary
SECTIONS.append({"id": "key-terms", "kicker": "Vocabulary", "title": "Key Terms: The Words That Do the Work",
  "blocks": [
    p("Compliance conversations fail when two people use the same word for different things. These "
      "definitions are generic; your regime's legal definitions override them, and part of setting "
      "up a facility is writing down which definitions <em>you</em> use."),
    defterm("Licence vs permit", "A licence authorises an operation (the who and the what, with "
            "conditions). Many regimes add permits: time-boxed, quantity-boxed authorisations "
            "under the licence, e.g. permission to grow this crop, this season, this much."),
    defterm("Condition", "A requirement written on or into the licence. Conditions are not "
            "suggestions; operating outside a condition is operating outside the licence."),
    defterm("Batch", "A defined quantity of material intended to be uniform, produced in one "
            "run of a process. In cultivation: a group of plants started together and treated "
            "the same."),
    defterm("Lot", "A batch or a subdivision of one. Some regimes use the words "
            "interchangeably; define your own usage in your documents and never drift."),
    defterm("Genealogy", "The parent-child chain of batches: mother to cuttings to veg batch to "
            "flower batch to harvest lot to packaged lot. Records inherit downward along it."),
    defterm("Seed-to-sale / track-and-trace", "A perpetual inventory system for a controlled "
            "substance: every plant and package carries an identity, and every movement, "
            "transformation and destruction is a recorded event."),
    defterm("UID / tag", "Unique identifier physically attached to a plant or package (barcode, "
            "RFID, or a number in a book). The bridge between the physical thing and its record."),
    defterm("Manifest", "The transport document for a movement between sites: what, how much, "
            "from whom, to whom, carrier, times. Chain of custody on wheels."),
    defterm("Reconciliation", "Comparing two independently recorded numbers that must agree, "
            "book stock vs counted stock, wet weight vs dry weight plus losses. Drift between "
            "them is the classic audit finding."),
    defterm("Deviation", "Any departure from your written process. Logged, assessed for impact, "
            "closed. CAPA (corrective and preventive action) is the loop that fixes the cause, "
            "not just the symptom."),
    defterm("ALCOA+", "What a trustworthy record is: Attributable, Legible, Contemporaneous, "
            "Original, Accurate, plus Complete, Consistent, Enduring, Available."),
    defterm("GACP / GMP", "Good Agricultural and Collection Practice governs growing and primary "
            "processing; Good Manufacturing Practice governs turning plant material into a "
            "medicine. The boundary between them is a real line in your paperwork."),
    defterm("CoA", "Certificate of Analysis: a lab's signed statement of what a specific lot "
            "tested as. Travels with the lot."),
    defterm("Quality agreement", "A signed document splitting quality responsibilities between "
            "two parties (grower and processor, licensee and lab): who tests, who releases, who "
            "tells whom when something goes wrong."),
  ]})

# ---------------------------------------------------------------- 4. licence anatomy
SECTIONS.append({"id": "licence-anatomy", "kicker": "The licence", "title": "Licence Anatomy: Activities, Conditions, Renewals",
  "blocks": [
    p("A cannabis licence is not one permission; it is a <strong>bundle of named activities</strong> "
      "with strings attached. New Zealand's scheme, for example, builds each licence from "
      "activities such as cultivation, nursery (supplying seeds and propagation material), "
      "research, possession for manufacture, and supply" + _c("nz-mca-activities") + ". Australia "
      "consolidated its federal structure in December 2021 into a single medicinal cannabis "
      "licence that can cover cultivation, production, manufacture and research, with permits "
      "underneath it" + _c("au-odc-single-licence") + ". The naming differs; the pattern, "
      "<em>activities plus conditions plus quantities</em>, repeats almost everywhere."),
    p("Read your licence as a machine with parts:"),
    kv([
      ("Holder + site", "A licence binds a legal person to a physical address. New entity, new "
       "premises, new rooms, usually a variation or a new application, before the change, "
       "not after."),
      ("Activities", "The named things you may do. Doing an unlisted activity, extracting "
       "when licensed only to cultivate, supplying when licensed only to grow, is operating "
       "unlicensed, even with the framed certificate on the wall."),
      ("Conditions", "Security arrangements, who may handle material, record-keeping and "
       "reporting duties, sometimes named responsible persons. Conditions are the licence."),
      ("Quantities / permits", "Many regimes cap what a licence alone allows and issue permits "
       "per crop, per period, or per quantity underneath it" + _c("au-odc-medcan") + "."),
      ("Expiry + renewal", "Licences and permits lapse. A lapsed licence does not wind down "
       "gracefully; it stops you, mid-crop if necessary."),
    ]),
    figure(L.flow("Life of a licence",
            [("Apply", "fit-and-proper checks, site, security, procedures"),
             ("Granted", "with activities and conditions attached"),
             ("Operate", "keep records, notify changes, report"),
             ("Inspected", "desk or on-site; findings to close"),
             ("Renew", "on time, every time, or stop work")],
            note="The licence is a relationship with a lifecycle, not a certificate you win once."), 2,
      "The licence lifecycle. Everything after &lsquo;granted&rsquo; is the actual job: operating "
      "inside the conditions, notifying, being inspected, renewing before expiry."),
    p("Two habits prevent most licence trouble. First, a <strong>compliance calendar</strong>: "
      "every expiry, renewal window, report deadline and fee, with alerts at 90, 60 and 30 days. "
      "Renewals are administratively boring and operationally fatal to miss. Second, treat "
      "<strong>variations as prerequisites, not paperwork catch-up</strong>: if you want to add a "
      "room, an activity, or a key person, the general rule across regimes is ask first, act "
      "after, and the operators who get this wrong usually knew the rule and gambled on "
      "nobody looking."),
    callout("tip", "Read your own licence quarterly",
      p("Print it. Read every condition aloud with the people who run the rooms. Operators are "
        "routinely surprised by what is actually written on the document they operate under, "
        "usually because the person who applied for it has left, and the conditions live in "
        "nobody's head.")),
  ]})

# ---------------------------------------------------------------- 5. regulator
SECTIONS.append({"id": "regulator", "kicker": "The relationship", "title": "The Regulator: Inspections, Notifications, Variations",
  "blocks": [
    p("The regulator is not a customer, not a mate, and not an enemy. The productive mental model "
      "is <strong>external quality assurance with statutory power</strong>: they exist to verify "
      "control, and everything they ask maps back to that. In New Zealand that function sits with "
      "a dedicated agency inside the Ministry of Health that administers the scheme and its "
      "licensing" + _c("nz-mca-scheme") + "; in Australia, with the Office of Drug Control at the "
      "federal layer" + _c("au-odc-medcan") + ". Whoever it is, the relationship runs on three "
      "channels:"),
    table(["Channel", "Direction", "Typical triggers", "The golden rule"], [
      ["<strong>Notification</strong>", "You &rarr; them", "Theft or loss of material, security "
       "incidents, significant deviations, changes to key people or circumstances",
       "Notify early and voluntarily. Regulators grade concealment far more harshly than error."],
      ["<strong>Inspection</strong>", "Them &rarr; you", "Scheduled cycle, licence grant or "
       "renewal, a complaint, a pattern in your reporting",
       "Never bluff. &lsquo;I will check and confirm in writing&rsquo; is a strong answer."],
      ["<strong>Variation</strong>", "You &rarr; them", "New rooms, new activities, new "
       "responsible persons, changed security or process scope",
       "Ask before acting. Retrospective variations read as breaches, because they are."],
    ], cls="compact", caption="The three channels of the regulator relationship."),
    p("Inspection posture matters more than most operators think. Findings are contested in "
      "writing, with evidence, after the visit, not argued in the corridor. Take your own notes "
      "of everything said, ask clarifying questions until each finding is specific enough to act "
      "on, and respond by the deadline with dated commitments. Then actually do them: a repeat "
      "finding at the next inspection is graded harder than the original, because it demonstrates "
      "the thing regulators care most about, whether your system self-corrects."),
    callout("warn", "The most expensive word in an inspection",
      p("&lsquo;Usually.&rsquo; As in &lsquo;we usually log that&rsquo;. Usually means the written "
        "procedure and the actual practice have separated, and the inspector now knows it. If "
        "practice has drifted from the SOP, fix one of them (formally, via a change note) "
        "before someone else finds the gap.")),
  ]})

# ---------------------------------------------------------------- 6. batches
SECTIONS.append({"id": "batches", "kicker": "Core concept", "title": "Batch and Lot Thinking: the Genealogy",
  "blocks": [
    lead("A batch is a promise of uniformity: a defined quantity of material that went through the "
         "same process at the same time, so one test result, one record, one decision can honestly "
         "speak for all of it. Everything in traceability hangs off that promise."),
    p("In a grow room the practical translation is: <strong>plants started together and treated "
      "the same are a batch</strong>; the moment treatment diverges, different room, different "
      "feed, a spray applied to some and not others. You have two batches, whether or not you "
      "wrote it down. The paperwork should follow the biology, not the other way round. Formal "
      "quality systems define batch and lot carefully and expect full traceability of what went "
      "into each one" + _c("pics-pe009-guide") + "; small operators mostly get in trouble not by "
      "defining batches badly but by <em>merging and splitting them silently</em>."),
    figure(_FIGS["genealogy"], 3,
      "Batch genealogy from one mother plant to packaged lots and waste. The amber dots mark the "
      "reach of a single record: an IPM spray logged against the mother on 1 March sits in the "
      "history of every descendant gram, forever."),
    p("This is why one plant's records matter. Genealogy means records <strong>inherit "
      "downward</strong>: the spray on the mother is part of the pesticide history of the packaged "
      "lot four generations later; the CoA on the packaged lot is only meaningful because the "
      "chain above it is unbroken. It cuts the other way too, a <em>missing</em> record poisons "
      "everything downstream, because you can no longer prove the negative. &lsquo;We never "
      "sprayed that crop&rsquo; is unprovable if the spray log has a three-week hole in it."),
    ul([
      "<strong>Make IDs human-readable and unique.</strong> A scheme like CL-2603 (clones, week "
      "26, 2003rd batch. Whatever your convention is) beats both &lsquo;the back table&rsquo; "
      "and a bare UUID. Write the convention down.",
      "<strong>Splits and merges are events.</strong> Two harvest lots combined into one dry lot "
      "is a recorded transformation with weights on both sides, not a quiet tidy-up.",
      "<strong>Never let a physical thing exist without an ID</strong>, even for an afternoon. "
      "Unlabelled totes of wet trim are where traceability actually dies.",
    ]),
    callout("key", "The batch is the unit of forgiveness",
      p("When something goes wrong (a failed test, a pest found, a contamination scare) you "
        "lose material at batch granularity, because the batch is the largest unit your records "
        "can vouch for. Small, honestly defined batches turn disasters into write-offs. One big "
        "vague batch turns a single failed test into losing the room.")),
  ]})

# ---------------------------------------------------------------- 7. track and trace
SECTIONS.append({"id": "track-trace", "kicker": "Systems", "title": "Seed-to-Sale: Tags, Movements, Reconciliation Points",
  "blocks": [
    p("Track-and-trace is perpetual inventory for a controlled substance. Three ingredients: "
      "<strong>identity</strong> (every plant and package carries a tag or UID), "
      "<strong>events</strong> (every movement, transformation, sample and destruction is "
      "recorded when it happens), and a <strong>ledger</strong> that holds it all. The ledger can "
      "be a government-mandated platform, commercial software, or a paper book. The logic is "
      "identical."),
    p("The most instructive worked example is the US state model. Systems like METRC issue "
      "physical plant tags and package tags, and licensees report growth stages, harvests, "
      "conversions, transfers and disposals against those IDs within set windows" +
      _c("metrc-platform") + ". California requires every commercial licensee to record all "
      "cannabis activity, cultivation through sale, in its state track-and-trace system, "
      "CCTT-Metrc, built on unique identifiers assigned to each plant and package" +
      _c("ca-dcc-ctt") + ". New Zealand and Australia (as at 2026) run no such state-operated "
      "ledger; the same functions live in your own records plus regulator reporting. The software "
      "is jurisdictional; the concepts transfer completely."),
    figure(_FIGS["movemap"], 4,
      "The seed-to-sale movement map. Identity changes shape with the material, plant tags "
      "become harvest batches become package UIDs, and the diamonds mark reconciliation points "
      "where two independently recorded numbers must agree."),
    p("Principles that survive any software choice:"),
    ul([
      "<strong>Physical equals digital.</strong> The room and the ledger must say the same thing "
      "at all times. Any gap between them, in either direction, is a finding.",
      "<strong>Record at the moment of the event</strong>, at the place of the event. Batch-entering "
      "the day's movements from memory at 5 pm is how drift is manufactured.",
      "<strong>Weigh at every transformation.</strong> Wet weight at harvest, dry weight after "
      "drying, waste weight at trim, net weight at packaging. The differences are your moisture "
      "and waste story, and auditors read that story closely.",
      "<strong>Nothing leaves except as a recorded transfer, sample, or destruction.</strong> "
      "There is no fourth category. &lsquo;Gave some to the lab guy&rsquo; is a sample with a "
      "log entry, or it is diversion.",
      "<strong>Movements get paper before wheels roll.</strong> The manifest (what, how much, "
      "from, to, carrier) exists before the material moves, and both ends reconcile against it "
      "on arrival.",
    ]),
    callout("note", "Spreadsheets are legal; neglected spreadsheets are not",
      p("At small scale a disciplined spreadsheet or paper ledger can satisfy the concepts, if "
        "entries are contemporaneous, attributable (who made this entry?), backed up, and never "
        "silently edited. The tool is rarely the problem. A track-and-trace system nobody updates "
        "until Friday is a liability generator regardless of what it cost.")),
  ]})

# ---------------------------------------------------------------- 8. reconciliation
SECTIONS.append({"id": "reconciliation", "kicker": "The #1 finding", "title": "Inventory Drift: the Finding That Writes Itself",
  "blocks": [
    lead("Inventory reconciliation is the audit test that needs no skill to run and no judgement "
         "to interpret: the book says X, the scales say Y, explain the difference. That is exactly "
         "why unexplained variance is the most reliable way for a small operator to fail. It is "
         "the easiest thing to check and the hardest to fake after the fact."),
    p("Drift has boring causes: moisture loss nobody logged as the flower cured; trim swept up "
      "and binned without a weight; QC pinches and lab samples that never hit the ledger; wet "
      "weight recorded in one unit and dry in another; harvest-day chaos where material moved "
      "rooms faster than anyone wrote it down. None of these are diversion. All of them "
      "<em>look like</em> diversion on paper, and controlled-substance regimes are built to treat "
      "unexplained loss as possible diversion until you demonstrate otherwise. When Oregon's "
      "state auditors reviewed their recreational system, they flagged reliance on self-reported "
      "data and poor data quality in the tracking system as core weaknesses in detecting exactly "
      "that" + _c("or-sos-audit-2019") + "."),
    table(["Line", "Amount", "Where it comes from"], [
      ["Opening stock (dried flower)", "12.40 kg", "Last verified count"],
      ["+ In: new harvest dried", "9.60 kg", "Dry-room log, dated"],
      ["&minus; Out: transfers to processor", "4.80 kg", "Manifests, signed both ends"],
      ["&minus; Out: destroyed waste", "1.20 kg", "Destruction records, witnessed"],
      ["&minus; Out: lab samples", "0.03 kg", "Sample log with lot IDs"],
      ["<strong>= Expected on hand</strong>", "<strong>15.97 kg</strong>", "Arithmetic"],
      ["Physical count", "15.71 kg", "This morning, two people"],
      ["<strong>Variance</strong>", "<strong>&minus;0.26 kg (&minus;1.6%)</strong>",
       "Investigate, explain, document, today"],
    ], cls="compact", caption="A worked reconciliation. The arithmetic is trivial; the discipline is doing it on a schedule and treating every variance as an incident with a written outcome. Figures illustrative."),
    p("The fix is cadence plus honesty. Small operations do well with a <strong>weekly cycle "
      "count</strong> of one area and a monthly full count; every variance gets a written "
      "investigation the day it is found, even when the conclusion is &lsquo;moisture loss, "
      "within expected range, convention updated&rsquo;. Give the ledger one owner. And log your "
      "moisture-loss convention explicitly (e.g. wet-to-dry expected 75&ndash;80% loss) so the "
      "biggest legitimate shrink in the building stops looking like a hole."),
    callout("warn", "Never true-up silently",
      p("Adjusting the book to match the count without a recorded investigation feels like "
        "tidying. In a controlled-substance ledger it is falsification. You have destroyed the "
        "evidence of a discrepancy and replaced it with a fiction that everything reconciled. "
        "Small visible variances with written explanations are survivable. Clean books that were "
        "made clean are not.")),
  ]})

# ---------------------------------------------------------------- 9. records
SECTIONS.append({"id": "records", "kicker": "Evidence", "title": "Records That Survive an Audit: ALCOA+",
  "blocks": [
    p("Regulators worldwide converge on the same definition of a trustworthy record, usually "
      "abbreviated <strong>ALCOA</strong>: Attributable, Legible, Contemporaneous, Original, "
      "Accurate, extended in practice with Complete, Consistent, Enduring and Available "
      "(ALCOA+). The US FDA's data-integrity guidance for drug manufacturing is built explicitly "
      "on these attributes" + _c("fda-data-integrity-2018") + ", and cannabis auditors inherit "
      "the framework wholesale."),
    figure(_FIGS["record"], 5,
      "One log entry, annotated. Every ALCOA+ attribute is a small physical habit: initials, "
      "permanent ink, writing at the time, keeping the first capture, striking through errors "
      "instead of erasing them."),
    p("The mechanics for a small operation:"),
    ul([
      "<strong>Bound books with numbered pages</strong>, or a digital system with locked history. "
      "Loose leaf paper and editable spreadsheets invite exactly the suspicion you are trying to "
      "kill.",
      "<strong>Write at the bench, not the office.</strong> The clipboard hanging at the point of "
      "work beats better software in the wrong room, because it makes the compliant path the "
      "lazy path.",
      "<strong>Corrections: single line through, initial, date, reason.</strong> The wrong value "
      "stays readable underneath. No pencil, no correction fluid, no torn-out pages, no "
      "recopying messy originals into a &lsquo;neat&rsquo; book. The messy original is the "
      "record.",
      "<strong>No blank fields.</strong> Strike through what does not apply. A blank is a "
      "question mark an auditor fills with their imagination.",
      "<strong>Retention:</strong> keep records for years, not seasons. Exact minimums are "
      "regime-specific and usually written into your licence conditions. Storage that survives "
      "staff turnover and a dead laptop is part of the requirement.",
    ]),
    p("Contemporaneous is the attribute that kills, because backfilling has a signature: a week "
      "of entries in one pen, one handwriting, one sitting, with no coffee rings, no wear, and "
      "suspiciously round timestamps, or a digital log where twenty entries share one burst of "
      "system time the night before the inspection. Auditors read logbooks the way forensic "
      "examiners read documents, because that is literally the discipline they are borrowing "
      "from. A backfilled record discovered is worse than a gap admitted: the gap costs you a "
      "finding; the fake costs you your credibility on every other page."),
    callout("tip", "Design the record before the task",
      p("For every routine task, decide what the minimum honest record is, one line, five "
        "fields, and build the form so completing it takes less than a minute. Compliance "
        "systems fail at the exact point where recording became more effort than the task "
        "itself.")),
  ]})

# ---------------------------------------------------------------- 10. deviations
SECTIONS.append({"id": "deviations", "kicker": "When it goes wrong", "title": "Deviations and CAPA-lite for Small Operators",
  "blocks": [
    p("A deviation is any departure from your written process: the dehumidifier died overnight, "
      "the feed was mixed at the wrong EC, the wrong room got sprayed, a delivery arrived with "
      "no paperwork. The deviation is not the failure. <strong>The unrecorded deviation is the "
      "failure</strong>, because it means your system does not notice its own departures, and "
      "noticing is the entire point of a quality system" + _c("pics-pe009-guide") + "."),
    figure(L.flow("Deviation to closure",
            [("Detect", "something departed from the written process"),
             ("Record", "same day, in the log, plainly"),
             ("Assess", "impact on product, batches affected"),
             ("Correct", "fix the immediate problem"),
             ("Prevent", "change so it cannot recur"),
             ("Verify", "check later that the fix held")],
            note="CAPA-lite: the full loop, sized for a small team. Minor deviations may stop after 'correct', write down that decision too."), 6,
      "The deviation loop. Corrective action fixes this instance; preventive action changes the "
      "system; verification closes the loop weeks later, when you check the fix actually held."),
    table(["Field", "What goes in it"], [
      ["What happened", "Plain factual description, no blame language"],
      ["When found / by whom", "Date, time, initials"],
      ["Batches / material affected", "IDs, always. This is what links the log to product"],
      ["Immediate action", "What you did in the first hour"],
      ["Impact assessment", "Can affected batches proceed? Held? Downgraded? Destroyed?"],
      ["Root cause", "For anything major: why did the system allow it?"],
      ["Preventive change", "SOP edited, alarm added, training done, with dates"],
      ["Closed by / verified", "A second person, later, confirming the fix held"],
    ], cls="compact", caption="A minimal deviation log. Eight fields on one page beats a procedure nobody uses."),
    p("Calibrate the depth. A missed daily check gets three lines and a same-day close. A "
      "wrong-tank feed that touched two flowering batches gets impact assessment and a root "
      "cause. Classify minor / major / critical in your own procedure so the depth decision is "
      "rule-based, not mood-based. What an auditor wants to see is not perfection; it is "
      "<em>evidence that you notice, assess product impact, and close loops</em>."),
    callout("key", "An empty deviation log is a red flag, not a badge",
      p("Every real operation deviates. A log with nothing in it does not read as &lsquo;flawless "
        "facility&rsquo;; it reads as &lsquo;nobody is looking&rsquo;, or worse, &lsquo;problems "
        "get handled off the books&rsquo;. A healthy log full of small, honestly closed "
        "deviations is one of the strongest documents you can put in front of an inspector.")),
  ]})

# ---------------------------------------------------------------- 11. gacp/gmp + quality agreements
SECTIONS.append({"id": "gacp-gmp", "kicker": "The boundary", "title": "GACP vs GMP, and the Quality Agreements That Bridge Them",
  "blocks": [
    p("Two rule-sets govern the journey from seed to medicine. <strong>GACP</strong>, Good "
      "Agricultural and Collection Practice, covers growing, harvesting and primary processing "
      "of medicinal plants: identity, hygiene, inputs, documentation, traceability at the farm "
      "layer. The foundational text is the WHO's 2003 guideline" + _c("who-gacp-2003") + ", and "
      "the European medicines regulator maintains a GACP guideline for herbal starting materials "
      "whose 2025 revision explicitly accounts for indoor, controlled-environment growing" +
      _c("ema-gacp-rev1") + ". <strong>GMP</strong>, Good Manufacturing Practice, covers "
      "turning that material into a medicine: validated processes, batch manufacturing records, "
      "QC release, an independent quality unit" + _c("eu-gmp-vol4") + ". The PIC/S GMP guide "
      "harmonises these expectations across dozens of national inspectorates, including New "
      "Zealand's and Australia's" + _c("pics-pe009-guide") + "."),
    figure(_FIGS["boundary"], 7,
      "The GACP/GMP boundary. Cultivation duties on the left, manufacturing duties on the right, "
      "and the three documents (lot records, CoAs, the quality agreement) that let material "
      "cross the line."),
    p("Where exactly the line sits is regime-specific, and it matters commercially. Cultivation "
      "through drying and trimming commonly sits under GACP; extraction, formulation and "
      "packaging of the medicine sit under GMP. Australia's TGA, for instance, applies GMP to "
      "manufacture while cannabis cultivation feeds it as GACP-governed starting material, with "
      "product quality pinned by a statutory standard (TGO 93)" + _c("au-tga-mc-quality") + ". "
      "As at 2026, check where your regulator draws it, the answer decides which rule-set your "
      "dry room lives under, and getting it wrong in either direction is expensive."),
    p("For a grower the boundary has a practical meaning: <strong>you are a starting-material "
      "supplier to a GMP site</strong>, and GMP obliges that site to qualify its suppliers. "
      "Expect the processor's auditors as well as the regulator's. Your GACP documentation ("
      "genealogy, input records, drying logs, CoAs) is their evidence that their starting "
      "material is controlled. This is where the <strong>quality agreement</strong> comes in: a "
      "signed split of responsibilities so nothing falls between two companies each assuming the "
      "other had it."),
    table(["Clause", "The question it answers"], [
      ["Specifications + CoA duties", "What the material must meet, who tests what, whose lab"],
      ["Sampling + retained samples", "Who pulls samples, how, who keeps the retains and for how long"],
      ["Deviation notification", "Who must tell whom, how fast, when something goes wrong on either side"],
      ["Change notification", "Cultivar, inputs, site, process changes, no silent changes to supplied material"],
      ["Complaints + recall roles", "Who leads, who notifies the regulator, timelines, out-of-hours contacts"],
      ["Audit rights", "The processor may audit the grower; scope and notice"],
      ["Records + retention", "Who holds which records, for how long, and access on request"],
      ["Release authority", "Named roles: who releases the lot to ship, who releases the product to market"],
    ], cls="compact", caption="Typical quality-agreement clauses between a cultivator and a processor. The same logic applies to your testing lab: methods, sample custody, out-of-specification handling, who sees results first."),
    callout("note", "Labs are partners in the same sense",
      p("A testing-lab agreement is a quality agreement too: agreed methods and detection limits, "
        "chain of custody for samples, what happens on an out-of-specification result (retest "
        "rules, notification), and turnaround. A surprise result from a lab you have no agreement "
        "with is a crisis; the same result under a good agreement is a procedure.")),
  ]})

# ---------------------------------------------------------------- 12. security + destruction
SECTIONS.append({"id": "security-waste", "kicker": "Custody", "title": "Security, Access and Destruction Records",
  "blocks": [
    p("Every regime writes its own security prescriptions (safes, alarm standards, camera "
      "retention days) into licence conditions, so this section stays deliberately generic. The "
      "underlying logic is constant: <strong>controlled material demands controlled custody</strong>, "
      "and custody is proven the same way as everything else, with records."),
    ul([
      "<strong>Layers, not one big lock.</strong> Site, building, room, container: each layer "
      "slows an intruder and narrows who can be inside it legitimately.",
      "<strong>Access is two lists.</strong> Who <em>may</em> enter (an authorisation list, "
      "maintained, signed) and who <em>did</em> (entry logs, key/code registers, visitor book "
      "with escort). Auditors cross-check the two.",
      "<strong>Joiners and leavers.</strong> The classic finding is an ex-staffer's code still "
      "live months after they left. Offboarding (codes killed, keys returned, lists updated) "
      "is a same-day task with a record.",
      "<strong>Visitors are escorted and logged</strong>, contractors included. The electrician "
      "in the flower room is inside your custody chain while the door is open.",
    ]),
    p("<strong>Waste is still controlled material.</strong> Trim, fan leaves from flowering "
      "plants, failed lots, dead plants, in most regimes cannabis waste remains within the "
      "licence's custody obligations until it is rendered unusable and its destruction is "
      "recorded. The bin is not an exit from track-and-trace; destruction is an <em>event</em>, "
      "with the same dignity as a transfer."),
    table(["Element of a defensible destruction record", "Why it is there"], [
      ["Date, time, location", "Anchors the event"],
      ["Material + batch/lot IDs", "Links the destruction into the genealogy"],
      ["Weight before destruction", "Closes the mass balance"],
      ["Method", "How it was rendered unusable and unrecoverable"],
      ["Done by + witnessed by", "Two people, two signatures, the single strongest anti-diversion control"],
      ["Sign-off", "A responsible person confirms the record complete"],
    ], cls="compact", caption="Destruction records close the loop on every gram that does not become product."),
    callout("warn", "Recognisable flower in an open skip",
      p("Whole buds visibly discarded, unrendered and unrecorded, is a diversion finding waiting "
        "for a drone photo. Render waste unusable by whatever method your regime accepts, weigh "
        "it, witness it, record it. Then it is rubbish. Before that, it is stock.")),
  ]})

# ---------------------------------------------------------------- 13. recall
SECTIONS.append({"id": "recall", "kicker": "Readiness", "title": "Recall Readiness and the Mock Recall",
  "blocks": [
    p("A recall is traceability run under stress: something already released turns out to be "
      "suspect, and you must find all of it, fast, and prove you found all of it. Formal GMP "
      "systems require a recall procedure and expect it to be tested" + _c("pics-pe009-guide") +
      "; the concept scales down to the smallest licensed grower, because the question, "
      "<em>where did every gram of that lot go?</em>, is the same at every scale."),
    p("Readiness is the ability to run the genealogy in both directions. <strong>Trace back</strong>: "
      "from a product in the market to every input, room, person and process that touched it. "
      "<strong>Trace forward</strong>: from a suspect input, one mother, one nutrient delivery, "
      "one dry room, to every lot and customer it reached. Both directions should run from "
      "records alone, in hours."),
    figure(_FIGS["recall"], 8,
      "The fan-out of a traceability test: one failed result on one lot, traced forward to every "
      "destination (the processor, sibling lots, the retained sample, verified waste) each one "
      "located and statused, with the mass balance closed."),
    p("The <strong>mock recall</strong> is the drill version: pick a lot at random, pretend its "
      "test result just failed, and run the whole exercise on paper against the clock. No "
      "material moves; the output is a timed report. A common expectation across supply-chain "
      "quality schemes is same-day reconciliation of essentially all of the affected quantity, "
      "hours, not weeks. Whatever target you adopt, write it down and measure against it."),
    figure(L.flow("The mock recall drill",
            [("Pick a lot", "random, not your tidiest one"),
             ("Trace forward", "every destination from records only"),
             ("Locate + hold", "simulate quarantine at each stop"),
             ("Mass balance", "shipped + held + samples + waste = 100%"),
             ("Report", "timed write-up, gaps named"),
             ("Fix gaps", "the gaps are the deliverable")],
            note="Run it before a regulator, customer or journalist runs it for you. The write-up is audit gold either way."), 9,
      "The mock recall as a repeatable drill. The purpose is not to pass; it is to find which "
      "link of the paper chain snaps under time pressure while nothing real is at stake."),
    p("What breaks in most first attempts: transfers recorded without lot IDs (so the manifest "
      "cannot say <em>which</em> lot the processor got); retained samples that exist in the SOP "
      "but not on the shelf; and waste weights too vague to close the mass balance. Every one of "
      "those is cheap to fix on a Tuesday afternoon and ruinous to discover during a real "
      "event."),
  ]})

# ---------------------------------------------------------------- 14. audit day
SECTIONS.append({"id": "audit-day", "kicker": "The test", "title": "Audit Day: a Walkthrough",
  "blocks": [
    p("Inspections vary (announced or not, desk or on-site, routine or triggered) but the shape "
      "of a survivable audit day is consistent. The work is 90% done before the knock on the "
      "door; the day itself is choreography."),
    steps([
      ("Notification received",
       "Confirm scope, date, duration and who is attending, in writing. Book your own key people. "
       "If a named responsible person is legally required to be present, make sure they are."),
      ("Pre-audit sweep",
       "Self-inspect against your own SOP index and licence conditions. Close what you can close "
       "honestly. Do not backfill records. A gap found is a finding; a fake found is a crisis."),
      ("Stage the front room",
       "Licence and conditions, org chart, SOP index, training records, current logs, last "
       "inspection's findings and their closure evidence, findable in minutes, not archaeology."),
      ("Opening meeting",
       "Agree scope and logistics. Appoint one person to route all requests and log every "
       "document handed over. Everyone else answers what is asked, nothing more, nothing "
       "invented."),
      ("The walk",
       "Inspectors watch practice against procedure: gowning, logs at the bench, labels on "
       "totes, locks locking. Answer truthfully; where unsure, say &lsquo;I will check and "
       "confirm&rsquo; and write it down. Never guess, never bluff, never argue."),
      ("The document room",
       "Requests get logged, copies get marked as copies, originals stay yours. If a record does "
       "not exist, say so, the recovery plan you offer matters more than the gap."),
      ("Closing meeting",
       "Capture every finding verbatim and ask questions until each is specific enough to act "
       "on. Clarify; do not contest. The place to contest is your written response, with "
       "evidence."),
      ("The response",
       "Written, by the deadline: for each finding, the correction, the preventive change, the "
       "date, the owner. Then do them and keep the evidence, the next audit opens exactly "
       "here."),
    ]),
    h(3, "How small operators actually fail"),
    p("Almost never through malice, and rarely through ignorance of growing. The recurring "
      "failure modes are structural. And every one is visible in advance:"),
    grid([
      card("The backfilled logbook",
        p("Three weeks of daily checks written the night before, one pen, one handwriting, no "
          "wear. Instantly recognisable, and it converts a small gap into a data-integrity "
          "crisis. <strong>Fix:</strong> log gaps honestly, with a dated note explaining them."), tag="records"),
      card("The silent true-up",
        p("Book adjusted to match the count, no investigation, no note. Reads as concealment "
          "because it is. <strong>Fix:</strong> every variance gets a written outcome, however "
          "boring."), tag="inventory"),
      card("The undocumented &lsquo;usually&rsquo;",
        p("Practice drifted from the SOP years ago; everyone knows the real way. The inspector "
          "now holds proof your system is fiction. <strong>Fix:</strong> change the SOP or the "
          "practice, via a change note, this month."), tag="process"),
      card("The dead SOP binder",
        p("Procedures written beautifully for the licence application, never opened since; staff "
          "have never read them. <strong>Fix:</strong> short SOPs people actually use, reviewed "
          "on a calendar, training recorded."), tag="process"),
      card("The ex-staffer&rsquo;s keycode",
        p("Alarm codes and keys outlive employment by months. On paper, an unauthorised person "
          "has facility access, a security condition breach. <strong>Fix:</strong> same-day "
          "offboarding checklist, with a record."), tag="security"),
      card("The unclosed loop",
        p("Last audit&rsquo;s findings acknowledged, promised, forgotten. Repeat findings are "
          "graded harder because they prove the system does not self-correct. "
          "<strong>Fix:</strong> findings live on the compliance calendar until verified "
          "closed."), tag="follow-up"),
    ], cols=2),
  ]})

# ---------------------------------------------------------------- 15. worked examples
SECTIONS.append({"id": "worked-examples", "kicker": "Two regimes", "title": "Worked Examples: New Zealand and Australia, From Altitude",
  "blocks": [
    callout("warn", "Date-stamped description, verify before acting",
      p("What follows describes two real regimes at a high level <strong>as at August 2026</strong>, "
        "purely to show the generic concepts wearing real clothes. Regimes change: rules are "
        "amended, guidance is reissued, agencies restructure. Before any real decision, read the "
        "regulator's current pages (linked below) and take proper advice.")),
    h(3, "New Zealand, the Medicinal Cannabis Scheme"),
    p("New Zealand's scheme is administered by the Medicinal Cannabis Agency within the Ministry "
      "of Health, under the Misuse of Drugs (Medicinal Cannabis) Regulations 2019, in force "
      "since 1 April 2020" + _c("nz-mc-regs-2019") + ". The licence is built from named "
      "activities (cultivation, nursery, research, possession for manufacture, supply) and an "
      "operator applies for the combination their operation needs" + _c("nz-mca-activities") +
      ". Products must meet a minimum quality standard before they can be supplied, which is "
      "what pulls GACP-grade cultivation records and GMP manufacture into the picture for "
      "anyone aiming at the medicinal market" + _c("nz-mca-scheme") + ". Licences carry "
      "conditions (security, record-keeping, reporting) and renewal cycles; the Agency "
      "publishes application guidance and holds the inspection relationship."),
    h(3, "Australia, ODC licensing, TGA quality"),
    p("Australia splits the job at the federal layer: the Office of Drug Control licenses "
      "cultivation, production, manufacture and research under the Narcotic Drugs Act 1967" +
      _c("au-odc-medcan") + ", and since 24 December 2021 a single medicinal cannabis licence "
      "can cover those activities together, with permits authorising quantities beneath it" +
      _c("au-odc-single-licence") + ". Product quality is the Therapeutic Goods "
      "Administration's territory: manufacture happens under GMP, cultivation feeds it as "
      "GACP-governed starting material, and medicinal cannabis products supplied in Australia "
      "must comply with a statutory quality standard, TGO 93" + _c("au-tga-mc-quality") + ". "
      "State and territory law adds further layers on top of the Commonwealth ones."),
    p("Look at the two side by side and the generic pattern of this whole paper reappears: an "
      "<strong>activity-based licence</strong> with conditions; <strong>permits or quantity "
      "controls</strong> underneath; a <strong>quality standard</strong> that drags GACP and GMP "
      "into cultivation decisions; and <strong>security, record and reporting obligations</strong> "
      "carried as licence conditions. Learn the pattern once, then read your own regime's "
      "current documents with it."),
    ul([
      "<a href='https://www.health.govt.nz/regulation-legislation/medicinal-cannabis/information-for-industry/about-the-medicinal-cannabis-scheme'>NZ Medicinal Cannabis Agency, about the scheme</a>",
      "<a href='https://www.health.govt.nz/regulation-legislation/medicinal-cannabis/information-for-industry/licence-activities'>NZ, licence activities</a>",
      "<a href='https://www.legislation.govt.nz/regulation/public/2019/0321/latest/LMS285243.html'>NZ, Misuse of Drugs (Medicinal Cannabis) Regulations 2019</a>",
      "<a href='https://www.odc.gov.au/medicinal-cannabis'>AU Office of Drug Control, medicinal cannabis</a>",
      "<a href='https://www.tga.gov.au/resources/guidance/complying-quality-requirements-medicinal-cannabis'>AU TGA, quality requirements for medicinal cannabis</a>",
    ]),
  ]})

# ---------------------------------------------------------------- 16. field guide
SECTIONS.append({"id": "field-guide", "kicker": "Reference", "title": "Troubleshooting and the Mental Model",
  "blocks": [
    table(["Symptom", "Likely cause", "Fix"], [
      ["Stocktake variance every month", "Unlogged moisture loss and waste",
       "Write a moisture-loss convention; weigh all waste; weekly cycle counts"],
      ["Inspector finds SOP&ndash;practice gaps", "Process drifted, documents froze",
       "Quarterly SOP read-through with the crew; change notes, not silent drift"],
      ["Records missing for a stretch of days", "One person owned it; they were away",
       "Cross-train; define the daily minimum record set; log gaps honestly"],
      ["Transfer disputed by receiver", "Manifest vague, no lot IDs, no weights at handover",
       "Weigh and sign at both ends against the manifest; photograph seals"],
      ["Lab result cannot be tied to a batch", "Sampling never recorded",
       "Sample log: lot ID, weight, date, who pulled it, chain of custody"],
      ["Renewal scramble / lapsed permit", "No compliance calendar",
       "One calendar, every date, alerts at 90/60/30 days, one owner"],
      ["Deviation log empty for a year", "Fear, or nobody looking",
       "No-blame logging; count near-misses; review the log monthly as a team"],
      ["Destruction challenged in audit", "No witness, no method, no weights",
       "Two-person rule, fixed method wording, weights before, sign-off"],
    ], cls="compact", caption="Field guide: the recurring compliance symptoms and their boring, effective fixes."),
    callout("key", "The mental model to keep",
      p("Run the operation as if the audit is tomorrow and the auditor is a stranger who trusts "
        "nothing but paper. The <strong>licence</strong> says what you may do. The "
        "<strong>records</strong> say what you did. <strong>Reconciliation</strong> proves no "
        "material leaked. <strong>Genealogy</strong> proves it is all connected. Any gram, any "
        "hour, any decision you cannot explain from the records alone. That is the finding. "
        "Everything in this paper is just machinery for making those four sentences true.")),
    p("Where to next: <em>Daily checks</em> is the operational twin of this paper. It builds the "
      "daily record set that makes everything here cheap. <em>GMP hash manufacturing</em> "
      "describes life on the far side of the GACP/GMP boundary, where your lots become someone "
      "else's starting material. And the IPM papers show why the spray log you keep for "
      "compliance is the same one that saves your crop."),
  ]})
