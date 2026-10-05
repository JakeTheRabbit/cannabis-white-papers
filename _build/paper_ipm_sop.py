# -*- coding: utf-8 -*-
"""Paper: integrated pest management, a working SOP (operational)."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        stagecard, grid, card, chip, kv, steps)
import figs_lib as L

SLUG = "ipm-sop"
TITLE = "Integrated pest management: an SOP"
EYEBROW = "Plant health · IPM"
SUB = ("This standard operating procedure (SOP) shows how to prevent pests and diseases in a "
       "cannabis grow room. It also shows how to scout and when to start a treatment. It shows how "
       "to use predators and sprays and how to keep complete and correct records.")
META = [("shield", "Operations"), ("doc", "Guide for operations"),
        ("quote", "5 sources"), ("clock", "~14 min to read")]
RELATED = ["mould-risk", "airflow-design", "harvest-dry-trim-cure"]
REF_IDS = ["punja-2021-emerging-diseases-cannabis", "scott-punja-2021-powdery-mildew-management",
           "elmoghazy-2024-swirskii-functional-response", "mumtaz-2023-californicus-functional-response",
           "koppert-persimilis-tech", "epa-wps-notice-to-workers", "moh-nz-pesticide-use-2024"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

# Fact-check jurisdiction banner
JURISDICTION_NOTE = "Jurisdiction note: The approval of products, the approval of organisms, the REI and the PHI (pre-harvest interval) are local. For example, NZ uses ACVM, HSNO and WorkSafe, and the US uses EPA WPS. Before you spray or release predators, examine the current regulations and the labels."


SECTIONS.append({"id": "intro", "kicker": "Start here", "title": "Purpose and scope",
  "blocks": [
    callout("NOTE", "Jurisdiction", JURISDICTION_NOTE),
    
    lead("Integrated pest management (IPM) is the regular procedure in which you find pests and "
         "diseases before they move to more plants. You use the weakest treatment that gives a good "
         "result. You use a stronger treatment only when it is necessary.</p><p>IPM is not one "
         "spray. IPM is not one task to release predators. It is a loop: examine the plants, make a "
         "decision, do a treatment, and do the loop again. Do the loop in each room. Start with the "
         "mother plants and the clones. Continue to the vegetative stage and the flowering stage."),
    p("One mite colony that you do not find, or one outbreak of powdery mildew, can destroy all the "
      "harvest" + _c("punja-2021-emerging-diseases-cannabis") + ". In a regulated facility, an "
      "error when you use a pesticide can cause an unsatisfactory result in the residue test. As a "
      "result, you discard all the batch" + _c("scott-punja-2021-powdery-mildew-management") +
      ". This guide is for a person who does not know IPM. The guide gives the definition of each "
      "term where the term first occurs."),
    figure(L.flow("The IPM loop",
            [("Scout", "walk and examine the plants"), ("Identify", "find the pest or disease name"),
             ("Threshold", "compare with the threshold"), ("Select", "scout, release, spray, remove"),
             ("Apply", "use the weakest treatment that is sufficient"), ("Record", "record, then scout again")]), 1,
      "IPM is a loop that you do again and again. It is not one treatment. Each finding goes around "
      "the loop and then back to the step Scout."),
    callout("key", "The most important information",
      p("Use the weakest treatment that gives a good result. Use a spray only when the action "
        "threshold makes it necessary. If you find a problem when it is small, the correction is "
        "easy. A problem that you do not find can destroy all the crop.")),
  ]})

SECTIONS.append({"id": "key-terms", "kicker": "Terms", "title": "Definitions",
  "blocks": [
    p("This section gives the terms before the procedure. It is not necessary to know all of the "
      "terms at this time. Each term occurs again in the sections that follow."),
    defterm("Scouting", "A careful visual inspection of the plants for pests, damage or disease."),
    defterm("Action threshold", "The quantity of pests at which you start a specified treatment."),
    defterm("Biological control (biocontrol)", "A method in which you release predators (insects or "
            "mites) to eat the pests."),
    defterm("Foliar spray and drench", "A foliar spray is a liquid that you apply to the leaves and "
            "stems. A drench is a liquid that you apply to the root zone."),
    defterm("REI (re-entry interval)", "The time after a spray before a person can safely go into "
            "the room."),
    defterm("Withholding period", "The time after a treatment before you can harvest the crop for sale."),
    defterm("Quarantine", "The procedure in which you keep new plants, or plants that can have a "
            "pest or disease, isolated from the crop. You monitor the plants before you move them "
            "to the crop."),
    defterm("Frass", "The waste of insects. It is a visual sign of a pest, and you can see it before you see the pest."),
    figure(L.flow("Time from the spray to the harvest",
            [("Apply", "spray, then record it"), ("REI", "no person goes in until the interval ends"),
             ("Withholding period", "no harvest until the period ends"), ("Safe", "you can go in and harvest")]), 2,
      "Two time periods start at the time that you spray. One time period is for persons (REI) and "
      "one time period is for the crop (withholding period)."),
  ]})

SECTIONS.append({"id": "scouting", "kicker": "Primary procedure 1", "title": "Scouting procedure",
  "blocks": [
    p("Scouting is the primary task of IPM. All the next steps give a good result only if you find "
      "the pests when the problem is small. A good baseline is a visual inspection of a minimum of "
      "5% of the room at each check. The room lead does the inspection and records each finding "
      "immediately. IPM scouts, who do only this task, do inspections with higher precision" +
      _c("punja-2021-emerging-diseases-cannabis") + "."),
    p("Scout in the same sequence each time. First, examine the tables and the substrate for frass "
      "and debris. Then examine the stalk and the stems. Then examine the bottom side of the "
      "leaves, where mites and thrips stay out of view. Last, examine the top side of the "
      "leaves.</p><p>Yellow sticky traps at the bottom of the stem and at the height of the canopy "
      "catch fungus gnats, aphids and thrips. These traps give a first sign of a problem."),
    figure(L.flow("Scouting sequence (bottom to top)",
            [("1 Substrate", "trays for frass and debris"), ("2 Bottom trap", "sticky trap at stem bottom"),
             ("3 Stalk, stems", "examine them"), ("4 Leaf bottoms", "where mites and thrips stay out of view"),
             ("5 Leaf tops", "visual damage"), ("6 Canopy trap", "sticky trap at canopy height")]), 3,
      "Always scout in the same sequence, from the bottom to the top. A sequence that is always the "
      "same makes sure that you examine all the areas when you have a short time."),
    figure(L.line("Sticky traps with dates show a problem at the start",
            [(0, 2), (1, 3), (2, 4), (3, 9), (4, 18)],
            ["wk 1", "wk 2", "wk 3", "wk 4", "wk 5"],
            ylab="insects/trap", ymin=0, ymax=22,
            note="A trend that increases (not a stable one) is the first sign. Start a treatment before damage shows."), 4,
      "Replace one trap each week. Write the date on the trap. Monitor the trend. From week 3 to "
      "week 5, the number of insects increases. This change is the signal for an investigation."),
    callout("tip", "Have a loupe with you",
      p("You cannot see russet mites and broad mites without a loupe. Use a jeweler's loupe to "
        "identify very small pests before you select a treatment.")),
  ]})

SECTIONS.append({"id": "thresholds", "kicker": "Primary procedure 2", "title": "Action thresholds",
  "blocks": [
    p("An action threshold changes a finding into a decision. Thus each decision uses data. A model "
      "with two parts agrees with a method that commercial growers frequently use" +
      _c("punja-2021-emerging-diseases-cannabis") + ".</p><p>In the first part, you find the first "
      "sign of one mite, one aphid or one other pest of the same type. Think that there are more "
      "pests. Scout all areas of the room. Start exclusion (limit who goes into the room). Get "
      "biocontrol.</p><p>In the second part, apply an approved pesticide when more than 3% of the "
      "room has pests. This value is an example to start with. Apply the pesticide only if the "
      "growth stage and the approval of the manager let you do this. For a zero-tolerance organism, "
      "the percentage is not important."),
    p("The growth stage also gives a limit for a treatment. Many regulated facilities with soilless "
      "substrate control the residue. These facilities apply a treatment to the plants only up to "
      "the first stage of flowering. For example, the limit is day 21. Your SOP for PHI and for QA "
      "gives the correct limit. After this limit, a weak antimicrobial solution that you use to "
      "clean the plants can be the only possible treatment" +
      _c("scott-punja-2021-powdery-mildew-management") + ".</p><p>If a large infestation occurs "
      "after day 21 of flowering, remove and destroy the plants that have the infestation. Do not "
      "spray."),
    figure(L.flow("Four conditions of the action threshold",
            [("0 pests", "monitor, scout again"), ("1 pest found", "scout the room, start exclusion, get biocontrol"),
             (">3% have pests", "apply approved pesticide, with approval"), ("Large, after day 21", "remove and destroy, do not spray")]), 5,
      "Each condition has a specified treatment. Data on the pest pressure select the condition "
      "that applies."),
    figure(L.zones("The treatment window in the crop cycle", 0, 100,
            [(0, 75, L.GL, "Mother plants to flower day 21: you can apply a treatment"),
             (75, 100, L.REDL, "Day 22 to harvest: no foliar spray")],
            unit="", note="The growth stage selects the treatment: when the plants have buds, remove them. Do not spray."), 6,
      "The green area is the treatment window. It is the only time when you can apply a foliar "
      "spray. The red area is the time to harvest. A spray in the red area can cause an "
      "unsatisfactory result in the residue test and crop loss."),
    callout("warn", "Use sulfur only in the vegetative stage",
      p("Use sulfur only on mother plants and in vegetative growth. Do not use sulfur in flowering" +
        _c("scott-punja-2021-powdery-mildew-management") + ". Sulfur on flowering plants causes "
        "contamination of the harvested flower.")),
  ]})

SECTIONS.append({"id": "biocontrol", "kicker": "Primary procedure 3", "title": "Biological control",
  "blocks": [
    p("In biocontrol, you release predators that eat your pests, if the regulations in your "
      "jurisdiction let you do this. The predators usually do not cause chemical residue on the "
      "cannabis plant at all stages. When there are no more pests to eat, the predators die. Select "
      "the correct predator for the pest and for the conditions."),
    p("<em>Amblyseius swirskii</em> is a generalist predator. It eats thrips larvae, whitefly and "
      "broad mites. It gives the best result at 25 to 30 &deg;C (77 to 86 &deg;F) with humidity of "
      "more than 70%" + _c("elmoghazy-2024-swirskii-functional-response") + ".</p><p><em>Phytoseiulus "
      "persimilis</em> is a specialist predator for spider mites. It eats a maximum of 5 adults or "
      "20 eggs each day. Cool conditions with high humidity are necessary for it" +
      _c("koppert-persimilis-tech") + ".</p><p><em>Neoseiulus californicus</em> is an alternative "
      "predator for spider mites, for a wide range of temperatures. It stays active at 16 to 32 "
      "&deg;C (60 to 90 &deg;F)" + _c("mumtaz-2023-californicus-functional-response") +
      ".</p><p><em>Stratiolaelaps scimitus</em> is a mite that stays in the soil. It eats fungus "
      "gnat larvae and thrips pupae. Release it when the pest pressure is low, for the best result" +
      _c("punja-2021-emerging-diseases-cannabis") + "."),
    figure(table(
      ["Predator", "Target pest", "Best temperature", "Best humidity", "Type"],
      [["<em>A. swirskii</em>", "Thrips larvae, whitefly, broad mites", "25&ndash;30 &deg;C (77&ndash;86 &deg;F)", ">70%", "Generalist"],
       ["<em>P. persimilis</em>", "Spider mites (the pest number decreases quickly)", "15&ndash;25 &deg;C (59&ndash;77 &deg;F)", "High", "Specialist"],
       ["<em>N. californicus</em>", "Spider mites (hot, dry rooms)", "16&ndash;32 &deg;C (60&ndash;90 &deg;F)", "Low or medium", "Specialist"],
       ["<em>S. scimitus</em>", "Fungus gnat larvae, thrips pupae", "Room temperature", "Moist media", "Soil specialist"]],
      cls="compact", caption="Select the predator that is correct for the pest and for the room. "
      "Hang sachets or release boxes with the predators in the room. Thus the predators and the "
      "material that holds them do not go into the irrigation system."), 7, ""),
    figure(L.zones("Select a spider mite predator for the room temperature", 50, 95,
            [(59, 77, L.BLUL, "persimilis (cool, fast)"),
             (60, 90, L.AMBL, "californicus (hot, dry, wide range)"),
             (77, 86, L.GL, "swirskii (warm generalist)")],
            unit="&deg;F", note="The ranges overlap. Select the predator for the usual temperature of your room."), 8,
      "Read the temperature of your room. Then select the predator that has your temperature in its "
      "active range. In a hot, dry room, californicus stays active and persimilis becomes less "
      "active."),
    callout("note", "Predators limit their number",
      p("Predators usually do not cause chemical residue. But the regulations in your jurisdiction "
        "must let you use the predators, and the predators must be compatible. When there are no "
        "more pests to eat, the predators die without a task from you. There is no residue and no "
        "withholding period.")),
  ]})

SECTIONS.append({"id": "spray-rotation", "kicker": "Primary procedure 4", "title": "Spray rotation and how to spray safely",
  "blocks": [
    p("When the action threshold makes a spray necessary, make sure that the residue is safe and "
      "the coverage is good. Do not change the procedure. Use only products that have an approval "
      "for cannabis in your jurisdiction. Always obey the dilution and the withholding periods on "
      "the label. Do not use a nutrient or supplement that is not on the list of approved products. "
      "It can cause an unsatisfactory result in the residue test" +
      _c("scott-punja-2021-powdery-mildew-management") + "."),
    p("Find each value on the current registered label of the product. The values are the spray "
      "rate, the interval between sprays, the crop stage, the REI and the pre-harvest interval. Use "
      "the label that is correct for the product, the pest and the jurisdiction" +
      _c("moh-nz-pesticide-use-2024") + ". A result in an investigation does not give approval for "
      "a spray each week or for a spray three times each week.</p><p>Use sulfur only when the "
      "product has a registration for cannabis. Use it only when the label lets you use it at the "
      "crop stage. Do not change a rate to kitchen tablespoons" +
      _c("scott-punja-2021-powdery-mildew-management") + ".</p><p>Change the chemical group of the "
      "product from one spray to the next. Make a tank mix only of products that the labels let you "
      "mix. Add the products in the sequence that the labels give.</p><p>Do not spray in these "
      "conditions: high light intensity, hot and dry air, or drought stress. A spray causes more "
      "damage to leaves that have stress."),
    figure(L.flow("Coverage sequence: media to leaf top",
            [("1 Media top", "soak the substrate surface"), ("2 Up the stalk", "stalk and bottom stems"),
             ("3 Leaf bottoms", "where pests stay"), ("4 Leaf tops", "complete the canopy")]), 9,
      "Good coverage is very important. Use a fan tip and a different sprayer for each product. "
      "Thus there is no cross-contamination."),
    figure(table(
      ["Day", "Product or tank mix", "Target", "REI", "Withholding period"],
      [["Monday", "Approved foliar solution", "General hygiene", "As on the label", "As on the label"],
       ["Wednesday", "Approved foliar solution + sulfur*", "Powdery mildew, mites", "As on the label", "As on the label"],
       ["Friday", "Biocontrol: release predators", "Mites and thrips", "None", "None"],
       ["When necessary", "Approved curative product (change the chemical group)", "Active outbreak", "As on the label", "As on the label"]],
      cls="compact", caption="Example of a spray rotation for one week. The table gives types of "
      "products and does not give brand names. Sulfur* is for mother plants and for the vegetative "
      "stage only, a maximum of one time in 2 weeks. Always read the label for the REI and the "
      "withholding period."), 10, ""),
    callout("warn", "Spray when the media is saturated",
      p("Spray when the media is at full saturation. At this time, a spray decreases the foliar "
        "uptake and the risk of leaf burn" + _c("scott-punja-2021-powdery-mildew-management") +
        ". Spray at the change in the irrigation, when the substrate is wettest.")),
  ]})

SECTIONS.append({"id": "sanitation-quarantine", "kicker": "Protection", "title": "Sanitation and quarantine",
  "blocks": [
    p("Most pests move into the room with persons. Thus the easiest control is to stop the pests "
      "before they go into the room. Shoes are the primary item that moves pests into the room" +
      _c("punja-2021-emerging-diseases-cannabis") + ".</p><p>Before you go into a grow room, change "
      "your shoes or put on overboots. Clean your hands when you go in and after each work break. "
      "Keep nitrile gloves on your hands at all times. Replace the gloves after each work break and "
      "after you touch chemicals. If you are not sure, replace the gloves."),
    p("Each new plant that comes into the facility goes to quarantine. On the day that you receive "
      "the plant, clean it with an approved foliar solution. You can also put the plant in the "
      "solution. Then keep the plant in a quarantine tent, isolated from the crop, for a minimum of "
      "2 weeks. Monitor the plant during this time, before you move it to the crop" +
      _c("punja-2021-emerging-diseases-cannabis") + ".</p><p>Think that all plant waste is "
      "dangerous material. Put the waste in a bag in the room. Weigh the waste and record the "
      "weight. Then move the bag directly to the green waste.</p><p>Use the equipment for one room "
      "only. Clean the equipment after each task. Thus a tool does not move pests from one room to "
      "a different room."),
    figure(L.flow("Steps to go into the room, each time",
            [("Change shoes", "overboots or shoes for the room"), ("Clean hands", "when you go in"),
             ("Put on gloves", "nitrile, always"), ("Foot bath", "go through it"), ("Go in and out", "new gloves when you go out")]), 11,
      "Shoes are the primary item that moves pests into the room. Use the sequence each time that "
      "you go in. Do the steps in the opposite sequence when you go out."),
    figure(L.line("Quarantine of a new plant",
            [(0, 1), (7, 1), (14, 1), (15, 0)],
            ["day 0: clean it", "day 7", "day 14", "to the crop"],
            ylab="in quarantine", ymin=0, ymax=2,
            note="Clean it when you receive it. Monitor it for 2 weeks or more. Move it to the crop only if it stays clean."), 12,
      "Keep new plants isolated for a minimum of two weeks and monitor them. Only a plant that "
      "stays clean can go to the crop."),
    callout("danger", "Do not use a tool in more than one room",
      p("Keep scissors, buckets, sprayers and PPE in one room only. Clean these items after each "
        "task. A tool that you use in more than one room can move pests from one room to a "
        "different room.")),
  ]})

SECTIONS.append({"id": "records-decision-flow", "kicker": "Step by step", "title": "IPM tasks for each day, decision flow and records",
  "blocks": [
    p("Use the sections before this section to make one procedure. Do the procedure again in each "
      "shift. The loop for each day is short. The decision flow gives the treatment for each "
      "finding."),
    steps([
      ("Prepare and go into the room", "Change your shoes. Clean your hands. Put on gloves. Go through the foot bath."),
      ("Scout in the same sequence", "Examine the substrate, the stems, the bottom side of the leaves and the top side of the leaves. Use the same sequence each day."),
      ("Read the traps and write the date", "Count the insects on each sticky trap. Write the date of the check on the trap. Record the trend."),
      ("Record each finding", "Record the name of each pest and the damage. We recommend that you add photos to the record each week."),
      ("Use the decision flow", "Identify the pest. Compare the quantity of pests with the threshold. Select one treatment: monitor, biocontrol, spray, or remove and destroy. Use the growth stage and how large the problem is to select the treatment."),
      ("Record, then scout again", "Record each treatment. Then compare the trap counts before and after the treatment. Make sure that the treatment gave a good result."),
    ]),
    figure(L.flow("The primary decision flow (from a finding)",
            [("Identify", "find the pest or disease name"), ("Less than threshold?", "monitor, scout again"),
             ("First sign?", "scout, exclusion and biocontrol"), (">3% and in window?", "approved spray"),
             ("Large after window?", "remove, destroy"), ("Record, scout again", "examine result")]), 13,
      "Use this sequence for each finding. The growth stage and how large the problem is select the "
      "next step. The loop always ends with a record. Then you scout again."),
    figure(table(
      ["Item", "Information to record"],
      [["Date", "Day of the spray"],
       ["Product", "Name on the approved list"],
       ["Active ingredient", "The name of the active chemical"],
       ["Dilution", "Rate on the label"],
       ["Area or room", "The area where you applied the product"],
       ["Applicator", "The person who sprayed"],
       ["REI", "The REI, shown on the door"],
       ["Withholding period", "The time before you can harvest"],
       ["Signature of the manager", "Approval on the log"]],
      cls="compact", caption="Template of a pesticide log, with no entries. You must record each "
      "spray in the log. The manager must write a signature on the log."), 14, ""),
    callout("key", "Records are also a feedback loop",
      p("Put a notice of the REI on the door of the room. Remove the notice only after the interval "
        "ends. Make an entry on the calendar of the room during the spray and after the spray" +
        _c("epa-wps-notice-to-workers") + ". Good records also show that a treatment gave a good "
        "result. Compare the numbers of insects on the traps before and after the treatment.")),
  ]})

SECTIONS.append({"id": "pitfalls-expectations", "kicker": "Problems and results", "title": "Troubleshooting and usual results",
  "blocks": [
    p("The frequent errors are always the same. You do not scout until you see damage. You spray a "
      "pest that you did not identify. You ignore the treatment window and spray in the last stage "
      "of flowering. You use the same tools or PPE in different rooms. You let predators go into "
      "the irrigation system."),
    figure(table(
      ["Frequent error", "Correct procedure"],
      [["Scout only when damage shows", "Scout in the same sequence at each check, before damage shows"],
       ["Spray a pest that you did not identify", "Use a loupe to identify the pest. Then select a treatment."],
       ["Spray in the last stage of flowering", "Use the treatment window. After day 21, remove and destroy plants with a large infestation."],
       ["Use the same tools and PPE in different rooms", "Use equipment and gloves for one room only, and clean them"],
       ["Biocontrol media in the irrigation system", "Hang sachets or release boxes"],
       ["Airborne fumigators in flowering", "Do not use them. They move into the buds."],
       ["Metal hose clamps in sprayers", "Use fittings that are not metal. Rust causes an unsatisfactory result in the test for heavy metals."]],
      cls="compact", caption="Each error has a short correction. Most errors occur because "
      "personnel do not obey the procedure. Equipment is not the cause."), 15, ""),
    p("Do not use airborne fumigators in a flowering facility. They can move into the buds and "
      "cause damage to the crop" + _c("scott-punja-2021-powdery-mildew-management") +
      ". Examine the sprayers for corrosion of the parts that touch the product and of the "
      "fertigation parts. This corrosion can cause metals contamination in some conditions" +
      _c("punja-2021-emerging-diseases-cannabis") + "."),
    figure(L.bars("Work to prevent pests is much less than work after an outbreak",
            [("Prevent pests (scout, hygiene, predators)", 25), ("Work after an outbreak", 90)], unit=" effort",
            note="Work and cost, compared. Stable work to prevent pests is much better than work after an outbreak.", maxv=100), 16,
      "After a long time of operation, the work in an IPM system is mostly stable work to prevent "
      "pests. A curative spray is not frequent."),
    callout("key", "Usual results",
      p("IPM does not give a room with no pests at all times. With IPM, you find pests when the "
        "problem is small. You keep the pest populations less than the threshold. You do not let a "
        "problem continue to the harvest.</p><p>After a long time of operation, the work in an IPM "
        "system is mostly preventative. You scout each week. You monitor the trends of the sticky "
        "traps. You use the clean procedure to go into the room. You apply a weak preventative "
        "foliar spray. A curative treatment is not frequent.")),
    p("Make the regular procedure first. Then most of the emergency treatments are not necessary. "
      "Use this SOP with the <a href='mould-risk.html'>mold risk</a> guide for disease pressure and "
      "with the <a href='airflow-design.html'>airflow design</a> guide. Clean air that moves is one "
      "of the best controls for pests."),
  ]})
