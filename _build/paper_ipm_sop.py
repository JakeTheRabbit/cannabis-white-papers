# -*- coding: utf-8 -*-
"""Paper: integrated pest management, a working SOP (operational)."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        stagecard, grid, card, chip, kv, steps)
import figs_lib as L

SLUG = "ipm-sop"
TITLE = "Integrated pest management: a working SOP"
EYEBROW = "Plant health · IPM"
SUB = ("A plain-language standard operating procedure for keeping pests and disease out of an "
       "indoor cannabis grow. How to scout, when to act, how to use good bugs and sprays, and "
       "how to keep records that hold up.")
META = [("shield", "Operational"), ("doc", "Operational guide"),
        ("quote", "Peer-reviewed · 4 sources"), ("clock", "~14 min read")]
RELATED = ["mould-risk", "airflow-design", "harvest-dry-trim-cure"]
REF_IDS = ["punja-2021-emerging-diseases-cannabis", "scott-punja-2021-powdery-mildew-management",
           "elmoghazy-2024-swirskii-functional-response", "mumtaz-2023-californicus-functional-response",
           "koppert-persimilis-tech", "epa-wps-notice-to-workers"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

SECTIONS.append({"id": "intro", "kicker": "Start here", "title": "What IPM is and why a grow lives or dies by it",
  "blocks": [
    lead("Integrated Pest Management (IPM) is the routine of catching pests and diseases before they "
         "spread, using the lightest control that works and escalating only when you have to. It is "
         "not one spray or one bug release. It is a loop: evaluate, decide, control, repeat, "
         "run across every room from mothers and clones through veg and flower."),
    p("One missed mite colony or one powdery-mildew outbreak can destroy an entire harvest" +
      _c("punja-2021-emerging-diseases-cannabis") + ", and in a regulated facility "
      "a pesticide misstep can fail residue testing and bin the whole batch" + _c("scott-punja-2021-powdery-mildew-management") +
      ". This guide assumes you know nothing and defines every term as it appears."),
    figure(L.flow("The IPM loop",
            [("Scout", "walk the room, look closely"), ("Identify", "name the pest or disease"),
             ("Threshold", "compare to the action level"), ("Decide", "monitor, bug, spray, or pull"),
             ("Act", "apply the lightest control that works"), ("Record", "log it, then re-scout")]), 1,
      "IPM is a repeating loop, not a one-off treatment. Every finding runs around the circle and back "
      "to scouting."),
    callout("key", "The one idea to keep",
      p("Use the lightest effective control first and escalate to sprays only when thresholds force it. A small "
        "problem caught early is cheap. A missed one can cost the whole crop.")),
  ]})

SECTIONS.append({"id": "key-terms", "kicker": "Vocabulary", "title": "Every term you need, defined once",
  "blocks": [
    p("Here is the language before the procedure. You do not need to memorise it. Each term comes back in "
      "context below."),
    defterm("Scouting", "The deliberate visual inspection of plants for pests, damage, or disease."),
    defterm("Action threshold", "The pest level that triggers a specific, defined response."),
    defterm("Biological control (biocontrol)", "Releasing predatory insects or mites, the "
            "&lsquo;good bugs&rsquo;, to eat the pests."),
    defterm("Foliar spray vs drench", "A foliar spray is a liquid applied to leaves and stems. A "
            "drench is applied to the root zone."),
    defterm("REI (re-entry interval)", "How long after a spray before anyone may safely enter the "
            "room."),
    defterm("Withholding period", "How long after treatment before the crop can be harvested for sale."),
    defterm("Quarantine", "Holding new or suspect plants isolated under observation before they join "
            "the crop."),
    defterm("Frass", "Insect droppings. An early visual sign of a pest you may not have seen yet."),
    figure(L.flow("Spray to harvest, on the clock",
            [("Apply", "spray goes on, log it"), ("REI", "nobody enters until interval ends"),
             ("Withholding", "no harvest until period ends"), ("Clear", "safe to work and to cut")]), 2,
      "Two separate clocks start the moment you spray: one for people (REI), one for the crop "
      "(withholding period)."),
  ]})

SECTIONS.append({"id": "scouting", "kicker": "Core practice 1", "title": "Scouting: find it before it finds you",
  "blocks": [
    p("Scouting is the engine of IPM. Everything downstream depends on catching pests early. A "
      "practical baseline is for the room lead to visually inspect at least 5 percent of the room at "
      "every check, logging any finding immediately, while dedicated IPM scouts do deeper precision "
      "inspections" + _c("punja-2021-emerging-diseases-cannabis") + "."),
    p("Work a fixed route every time: scout the tables and substrate for frass and debris, then the "
      "trunk and stems, then the undersides of leaves (where mites and thrips hide), then leaf tops. "
      "Yellow sticky traps at the base of the stem and at canopy height give an early-warning catch of "
      "stray fungus gnats, aphids, and thrips."),
    figure(L.flow("The scout route (bottom to top)",
            [("1 Substrate", "trays for frass and debris"), ("2 Base trap", "sticky trap at stem base"),
             ("3 Trunk/stems", "check the stalk"), ("4 Leaf undersides", "where mites/thrips hide"),
             ("5 Leaf tops", "visible damage"), ("6 Canopy trap", "sticky trap at canopy height")]), 3,
      "Always scout the same order, low to high. A fixed route means nothing gets skipped under time "
      "pressure."),
    figure(L.line("Dated sticky traps catch a problem early",
            [(0, 2), (1, 3), (2, 4), (3, 9), (4, 18)],
            ["wk 1", "wk 2", "wk 3", "wk 4", "wk 5"],
            ylab="insects/trap", ymin=0, ymax=22,
            note="A rising trend (vs a flat one) is your early warning to act before damage shows."), 4,
      "Replace one trap weekly, write the date on it, and watch the trend. The jump from week 3 to "
      "week 5 is the signal to investigate."),
    callout("tip", "Carry a loupe",
      p("Russet mites and broad mites are invisible to the naked eye. Use a jeweler's loupe to "
        "confirm tiny pests before you decide what to do.")),
  ]})

SECTIONS.append({"id": "thresholds", "kicker": "Core practice 2", "title": "Action thresholds: knowing exactly when to act",
  "blocks": [
    p("A threshold turns observation into a decision so nobody has to guess. A workable two-tier model "
      "reflects a common commercial action approach" + _c("punja-2021-emerging-diseases-cannabis") +
      ". At the first sign of a single mite, aphid, or similar pest, assume there are more: "
      "scout the entire room, begin exclusion measures (limit who enters), and line up biological "
      "controls. Once more than 3 percent of a room is affected, escalate to approved pesticide "
      "applications, subject to growth stage and management sign-off."),
    p("Growth stage is itself a hard gate. In a regulated soilless facility, plants are treated only "
      "from mothering through day 21 of flower, with no foliar treatment after buds form (a light "
      "antimicrobial rinse may be the only exception)" + _c("scott-punja-2021-powdery-mildew-management") +
      ". For a serious infestation that appears after day 21 of flower, pull "
      "and destroy the affected plants rather than spray."),
    figure(L.flow("The threshold ladder",
            [("0 pests", "monitor, keep scouting"), ("1 pest seen", "scout room + exclude + order biocontrol"),
             (">3% affected", "add approved pesticide (with sign-off)"), ("Post-day-21 serious", "pull and destroy, do not spray")]), 5,
      "Each rung is a defined response. The level of pressure, not a gut feeling, decides which rung "
      "you are on."),
    figure(L.zones("The treatment window across the crop's life", 0, 100,
            [(0, 75, L.GL, "Mothering → flower day 21: treatable"),
             (75, 100, L.REDL, "Flower day 22 → harvest: no foliar")],
            unit="", note="Stage gates the decision: after buds form, escalation means removal, not spraying."), 6,
      "The green band is the only window for foliar treatment. The red band is harvest territory. "
      "Spraying here risks residue failure and crop loss."),
    callout("warn", "Sulphur is a veg-stage tool",
      p("Restrict sulphur to mothers and vegetative growth, not flowering" + _c("scott-punja-2021-powdery-mildew-management") +
        ". Applied late, it taints the finished flower.")),
  ]})

SECTIONS.append({"id": "biocontrol", "kicker": "Core practice 3", "title": "Biological controls: putting good bugs to work",
  "blocks": [
    p("Biocontrol releases predators that hunt your pests. They are harmless to the cannabis plant "
      "at every stage, and if they run out of prey they simply die off and fall away. The job is to match "
      "the predator to the pest and the conditions."),
    p("<em>Amblyseius swirskii</em> is a generalist that eats thrips larvae, whitefly, and broad mites "
      "and works best at 77 to 86 &deg;F with humidity above 70 percent" + _c("elmoghazy-2024-swirskii-functional-response") +
      ". <em>Phytoseiulus persimilis</em> is a spider-mite specialist that eats up to 5 adults or 20 "
      "eggs a day but needs cooler, humid conditions" + _c("koppert-persimilis-tech") + ". "
      "<em>Neoseiulus californicus</em> is the tougher spider-mite option that stays active across 60 "
      "to 90 &deg;F" + _c("mumtaz-2023-californicus-functional-response") + ". "
      "<em>Stratiolaelaps scimitus</em> is a soil-dwelling mite for fungus gnat larvae and thrips "
      "pupae, best deployed when pest pressure is still low" + _c("punja-2021-emerging-diseases-cannabis") + "."),
    figure(table(
      ["Predator", "Target pest", "Ideal temp", "Ideal humidity", "Type"],
      [["<em>A. swirskii</em>", "Thrips larvae, whitefly, broad mites", "77&ndash;86 &deg;F", ">70%", "Generalist"],
       ["<em>P. persimilis</em>", "Spider mites (fast knockdown)", "59&ndash;77 &deg;F", "High", "Specialist"],
       ["<em>N. californicus</em>", "Spider mites (hot/dry rooms)", "60&ndash;90 &deg;F", "Low&ndash;mod", "Specialist"],
       ["<em>S. scimitus</em>", "Fungus gnat larvae, thrips pupae", "Room temp", "Moist media", "Soil specialist"]],
      cls="compact", caption="Match the predator to both the pest and the room. Deploy via hanging "
      "sachets or boxes so predators and carrier media stay out of the irrigation system."), 7, ""),
    figure(L.zones("Pick a spider-mite predator by room temperature", 50, 95,
            [(59, 77, L.BLUL, "persimilis (cool, fast)"),
             (60, 90, L.AMBL, "californicus (hot/dry, hardy)"),
             (77, 86, L.GL, "swirskii (warm generalist)")],
            unit="&deg;F", note="Overlapping ranges, so choose by where your room actually sits day to day."), 8,
      "Read your room temperature, then pick the predator whose active band covers it. In a hot, dry "
      "room californicus holds up where persimilis fades."),
    callout("note", "Good bugs self-limit",
      p("Predators are harmless to the plant and to people. When the prey runs out they die off on "
        "their own. There is no residue and no withholding period.")),
  ]})

SECTIONS.append({"id": "spray-rotation", "kicker": "Core practice 4", "title": "Spray rotation and safe application",
  "blocks": [
    p("When thresholds force a spray, the rules are about residue safety and effective coverage, not "
      "improvisation. Use only products approved for cannabis in your jurisdiction, always follow the "
      "label dilution and withholding periods, and never freelance with off-list nutrients or "
      "supplements that could fail residue testing" + _c("scott-punja-2021-powdery-mildew-management") + "."),
    p("A preventative program can be as simple as a weekly foliar of an approved wash plus sulphur (1 "
      "to 3 tablespoons per litre, ideally 3, no more than once every 2 weeks, veg and mothers only), "
      "stepping up to 3 times a week curatively at low pest levels" + _c("scott-punja-2021-powdery-mildew-management") +
      ". Rotate chemistries and tank-mix only combinations the labels allow, adding products in the "
      "label-specified order. Spray when the media is fully saturated so the product is not pulled "
      "into the leaves and burns them."),
    figure(L.flow("Coverage order: media to leaf top",
            [("1 Media top", "soak the substrate surface"), ("2 Up the stalk", "trunk and lower stems"),
             ("3 Leaf undersides", "where pests hide"), ("4 Leaf tops", "finish the canopy")]), 9,
      "Coverage is everything. Use a fan tip and a dedicated sprayer per product to avoid "
      "cross-contamination."),
    figure(table(
      ["Day", "Product / tank-mix", "Target", "REI", "Withholding"],
      [["Mon", "Approved wash (foliar)", "General hygiene", "Per label", "Per label"],
       ["Wed", "Approved wash + sulphur*", "Powdery mildew, mites", "Per label", "Per label"],
       ["Fri", "Biocontrol release", "Mites / thrips", "None", "None"],
       ["As needed", "Approved curative (rotate class)", "Active outbreak", "Per label", "Per label"]],
      cls="compact", caption="Example weekly rotation (genericised, no brand recommendations). "
      "*Sulphur veg/mothers only, max once per 2 weeks. Always read the actual label for REI and "
      "withholding."), 10, ""),
    callout("warn", "Spray on saturated media",
      p("Spraying at full media saturation reduces foliar uptake and burn risk" + _c("scott-punja-2021-powdery-mildew-management") +
        ". Time it to the irrigation transition when the substrate is wettest.")),
  ]})

SECTIONS.append({"id": "sanitation-quarantine", "kicker": "Prevention", "title": "Sanitation and quarantine: stop pests at the door",
  "blocks": [
    p("Most pests are walked in, so the cheapest control is keeping them out. The biggest single entry "
      "point is footwear" + _c("punja-2021-emerging-diseases-cannabis") + ", so replace shoes or use "
      "overboots before entering grow rooms, wash hands on entry and after every break, and wear "
      "nitrile gloves at all times, changing them after breaks or after handling chemicals (when in "
      "doubt, change them)."),
    p("Every incoming plant goes through quarantine: dunk or wash it in an approved foliar solution on "
      "receipt, then hold it in a separate quarantine tent for 2 or more weeks under observation "
      "before it joins the crop" + _c("punja-2021-emerging-diseases-cannabis") + ". Treat all plant "
      "waste as hazardous: bag it in the room, weigh and log it, and move it straight to green waste. "
      "Keep equipment room-specific and cleaned after every task so a tool never carries pests between "
      "rooms."),
    figure(L.flow("Clean entry, every time",
            [("Change shoes", "overboots or dedicated footwear"), ("Wash hands", "on entry"),
             ("Glove up", "nitrile, always"), ("Foot bath", "step through"), ("Enter", "reverse + new gloves on exit")]), 11,
      "Footwear is the number-one route pests are walked in. The entry sequence is non-negotiable, and "
      "it runs in reverse on the way out."),
    figure(L.line("A new plant's quarantine journey",
            [(0, 1), (7, 1), (14, 1), (15, 0)],
            ["day 0 wash", "day 7", "day 14", "release"],
            ylab="in quarantine", ymin=0, ymax=2,
            note="Wash on receipt, observe 2+ weeks, release to the crop only if it stays clean."), 12,
      "New plants are isolated and watched for at least two weeks. A clean run is the only ticket into "
      "the main crop."),
    callout("danger", "Never share tools between rooms",
      p("Scissors, buckets, sprayers, and PPE stay with one room and get cleaned after every task. A "
        "shared tool is a highway for pests.")),
  ]})

SECTIONS.append({"id": "records-decision-flow", "kicker": "Step-by-step", "title": "The daily routine, the decision flow, and record-keeping",
  "blocks": [
    p("Put it together as a repeatable shift routine. The daily loop is short, and the decision flow "
      "handles whatever you find."),
    steps([
      ("Gear up and enter", "Change footwear, wash hands, glove up, step through the foot bath."),
      ("Walk the scout route", "Substrate, stems, leaf undersides, leaf tops, same order every day."),
      ("Check and date traps", "Read sticky-trap counts, write today's date, note the trend."),
      ("Log every finding", "Record pest IDs and damage. Uploading photos weekly is a good cadence."),
      ("Run the decision flow", "Identify, compare to threshold, choose monitor / biocontrol / spray / pull-and-destroy by stage and severity."),
      ("Record and re-scout", "Log any treatment, then compare before-and-after trap counts to confirm it worked."),
    ]),
    figure(L.flow("The master decision flow (from a finding)",
            [("Identify", "name the pest or disease"), ("Below threshold?", "monitor, keep scouting"),
             ("Tier 1?", "scout + exclude + biocontrol"), (">3% & in window?", "approved spray"),
             ("Post-window serious?", "pull and destroy"), ("Record + re-scout", "verify it worked")]), 13,
      "Every finding runs this path. Stage and severity decide the branch, and the loop always ends in a "
      "record and a re-scout."),
    figure(table(
      ["Field", "What to record"],
      [["Date", "Day of application"],
       ["Product", "Name as on the approved list"],
       ["Active ingredient", "What it actually is"],
       ["Dilution", "Rate per label"],
       ["Area / room", "Where it went on"],
       ["Applicator", "Who sprayed"],
       ["REI", "Posted on the door"],
       ["Withholding", "Harvest hold period"],
       ["Manager signature", "Sign-off on the log"]],
      cls="compact", caption="Blank pesticide-log template. Every application must be logged and the "
      "log signed by management."), 14, ""),
    callout("key", "Records are also a feedback loop",
      p("REI signage must be posted on the room door and removed only after the interval, with the "
        "room calendar marked during and after application" + _c("epa-wps-notice-to-workers") + ". "
        "Good records double as proof a treatment worked. Compare trap counts before and after.")),
  ]})

SECTIONS.append({"id": "pitfalls-expectations", "kicker": "Reality check", "title": "Common mistakes and what good IPM actually looks like",
  "blocks": [
    p("The frequent failures are predictable: skipping scouting until damage is visible, spraying "
      "without confirming the pest, ignoring the treatment window and spraying in late flower, sharing "
      "tools or PPE between rooms, and letting good bugs wash into the irrigation system."),
    figure(table(
      ["Common mistake", "Correct practice"],
      [["Scout only once damage shows", "Scout on a fixed route every check, before damage appears"],
       ["Spray an unidentified pest", "Confirm the pest with a loupe first, then act"],
       ["Spray in late flower", "Respect the window; after day 21 serious = pull and destroy"],
       ["Share tools / PPE between rooms", "Room-specific, cleaned equipment and gloves"],
       ["Biocontrol media into irrigation", "Deploy via hanging sachets / boxes"],
       ["Airborne fumigators in flower", "Avoid entirely, they drift into bud"],
       ["Metallic hose clamps in sprayers", "Use non-metallic fittings, rust fails heavy-metals tests"]],
      cls="compact", caption="Each failure has a one-line fix. Most are about discipline, not "
      "equipment."), 15, ""),
    p("Avoid airborne fumigators entirely in a flower facility. They can drift into bud and "
      "compromise the crop" + _c("scott-punja-2021-powdery-mildew-management") + ". Check "
      "sprayers for metallic hose clamps that can rust and fail heavy-metals testing" + _c("punja-2021-emerging-diseases-cannabis") + "."),
    figure(L.bars("Prevention is far cheaper than reactive cleanup",
            [("Prevention (scout, hygiene, bugs)", 25), ("Reactive cleanup after outbreak", 90)], unit=" effort",
            note="Relative effort and cost. Steady prevention vastly outperforms firefighting an outbreak.", maxv=100), 16,
      "A mature program is mostly quiet, steady prevention. Curative spraying is the rare exception, "
      "not the routine."),
    callout("key", "Realistic expectations",
      p("IPM does not mean zero pests ever. It means you detect early, keep populations under "
        "threshold, and never let a problem reach the harvest. A mature program is mostly weekly "
        "scouting, sticky-trap trends, clean entry, and light preventative foliar, with "
        "curative escalation as the exception.")),
    p("Build the quiet routine first and the dramatic rescues mostly disappear. Pair this SOP with the "
      "<a href='mould-risk.html'>mould-risk</a> guide for disease pressure and the "
      "<a href='airflow-design.html'>airflow design</a> guide. Clean, moving air is itself one "
      "of the best pest controls you have."),
  ]})
