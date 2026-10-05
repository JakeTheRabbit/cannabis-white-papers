# -*- coding: utf-8 -*-
"""Paper: root-zone pH management for beginners."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        stagecard, grid, card, chip, kv, steps)
import figs_lib as L

SLUG = "ph-management"
TITLE = "pH: the definition and how to keep it stable"
EYEBROW = "Feed · pH"
SUB = ("The pH of the root zone controls which nutrients your plant can absorb. This paper shows "
       "how the scale from 0 to 14 operates. It shows the cause of the different target ranges for "
       "each substrate. It also shows how to measure and adjust the pH, and how to keep it stable "
       "for each feed.")
META = [("flask", "Feed"), ("image", "8 diagrams"),
        ("quote", "6 sources"), ("clock", "~14 min to read")]
RELATED = ["nutrient-deficiencies", "water-quality", "nutrient-mixing-athena"]
REF_IDS = ["veazie-2025-substrate-ph-micronutrient-cannabis",
           "gillespie-kubota-2020-low-ph-basil-nutrient-uptake",
           "kpai-2024-cannabis-nutrient-solution-ph-cation-uptake",
           "malik-tlustos-2025-soilless-media-cannabis",
           "kudirka-2023-precise-hydroponic-ph-mes-buffer",
           "saloner-bernstein-2022-nitrogen-source-cannabis",
           "umass-water-quality-ph-alkalinity",
           "unl-passel-soil-ph-definition"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

SECTIONS.append({"id": "what-this-is", "kicker": "Start here",
  "title": "Purpose and scope",
  "blocks": [
    lead("pH is a scale from 0 to 14. It shows how acidic or alkaline a liquid is. A pH of 7 is "
         "neutral. A lower pH is acidic and a higher pH is alkaline. For a grower, the pH is the "
         "one setting that controls if the nutrients that you give to the plant can go into the "
         "roots. If the pH is incorrect, a plant that has all the nutrients can have a deficiency."),
    p("Pure water has a pH of 7. Lemon juice has a pH of approximately 2 (strongly acidic). A "
      "solution of baking soda has a pH of approximately 8.5 (weakly alkaline)."),
    p("A grower frequently makes errors with the scale, because the scale is logarithmic. Each "
      "whole number is a change of ten times in acidity. A pH of 5 is ten times more acidic than a "
      "pH of 6, and a hundred times more acidic than a pH of 7." + _c("unl-passel-soil-ph-definition") +
      " Thus a reading that is almost correct can be far from the range that is necessary for your "
      "roots."),
    figure(L.zones("The pH scale and the target for a grower",
            0, 14,
            [(0, 2, L.REDL, "lemon ~2"), (5.5, 6.5, L.GL, "grower target 5.5-6.5"),
             (7, 7, L.BLUL, "pure water 7"), (8, 9, L.AMBL, "baking soda ~8.5")],
            unit="", note="The target of most root-zone feed is the small green area, not neutral."), 1,
      "The figure shows liquids on the pH scale. It also shows the range of 5.5 to 6.5, in which "
      "most growers apply feed. Neutral water (7) is too high for coco and hydroponics."),
    callout("key", "The most important information",
      p("Your nutrients and your light can be correct, and the plant can have deficiencies because "
        "of an incorrect pH. The pH value controls all the next steps.")),
  ]})

SECTIONS.append({"id": "key-terms", "kicker": "Terms", "title": "Definitions",
  "blocks": [
    defterm("pH", "A value on a scale of 0 to 14 that shows how acidic or alkaline the water around the roots is."),
    defterm("Root zone", "The wet substrate around the roots, where uptake occurs."),
    defterm("Lockout", "The nutrients are in the root zone, but they are not available chemically. "
            "Thus the plant shows a deficiency, but it receives feed."),
    defterm("EC (electrical conductivity)", "The quantity of salts in the nutrient solution. EC is "
            "a different setting from pH. <a href='nutrient-mixing-athena.html'>Guide to mix "
            "nutrients &rarr;</a>"),
    defterm("Substrate or medium", "The material that holds the roots: coco coir, rockwool, soil, or "
            "water in hydroponics."),
    defterm("Buffering", "The resistance of a medium or of water to a change of pH. A medium with "
            "buffering absorbs small changes before the reading changes. Soil has high buffering. "
            "Coco and hydroponics have almost none. Thus the pH changes immediately at each feed."),
    defterm("Alkalinity", "The capacity of the water to absorb acid, caused mostly by bicarbonates. "
            "Alkalinity and pH are different measurements. Water can have a usual pH and a very "
            "high alkalinity. The first reading is correct, but acid that you add to this water "
            "does not change the pH easily."),
    defterm("Runoff", "The solution that drains from the bottom of the pot after you apply water."),
  ]})

SECTIONS.append({"id": "why-ph-controls-availability", "kicker": "Basic information",
  "title": "pH, nutrient availability and lockout",
  "blocks": [
    p("Each nutrient stays dissolved, and the roots can absorb it, only in a specified pH range. If "
      "the pH is not in this range, the nutrient reacts with other ions and changes to chemical "
      "compounds that the roots cannot absorb. The nutrient is in the solution, but the roots "
      "cannot absorb it. Lockout is the name of this condition. The plant has nutrients around it "
      "that it cannot use, because the pH of the root zone is not in the correct range."),
    p("If the pH is too high, more than approximately 6.5 in inert media such as coco or "
      "hydroponics, the micronutrients precipitate first. The micronutrients are iron, manganese, "
      "zinc and boron." + _c("veazie-2025-substrate-ph-micronutrient-cannabis") +
      " If the pH is too low, less than approximately 5.5, the availability of calcium, magnesium "
      "and phosphorus can decrease. At the same time, iron and manganese can cause toxicity." +
      _c("gillespie-kubota-2020-low-ph-basil-nutrient-uptake")),
    p("Phosphorus is a clear example. It is most available at a pH of 6.0 to 7.0. At a pH of less "
      "than 5.5, it binds with iron and aluminum. At a pH of more than 7.5, it binds with calcium." +
      _c("kpai-2024-cannabis-nutrient-solution-ph-cation-uptake") + " The &lsquo;sweet spot&rsquo; "
      "is the pH at which the largest number of nutrients are available at the same time."),
    figure(L.zones("The pH range in which each nutrient is available",
            4, 8,
            [(5.5, 6.5, L.GL, "all overlap 5.5-6.5"),
             (4.0, 5.5, L.REDL, "Ca / Mg / P lockout, low pH"),
             (6.5, 8.0, L.AMBL, "Fe / Mn / Zn / B lockout, high pH")],
            unit="", note="The green area is where the micronutrients and the primary cations are available at the same time."), 2,
      "Calcium, magnesium and phosphorus are not available at a low pH. Iron, manganese, zinc and "
      "boron are not available at a high pH. The overlap of 5.5 to 6.5 is the only range in which "
      "all are available." + _c("veazie-2025-substrate-ph-micronutrient-cannabis")),
    callout("warn", "Lockout and a deficiency show the same symptoms",
      p("Before you add more nutrients, examine the pH. The symptoms of lockout and of a deficiency "
        "are the same. Thus growers frequently add more nutrients and the problem becomes worse.")),
  ]})

SECTIONS.append({"id": "targets-by-substrate", "kicker": "Your numbers",
  "title": "Target ranges for each substrate: coco, hydroponics, soil",
  "blocks": [
    p("There is not one correct pH. The correct target is different for each substrate. You set the "
      "pH of the inflow, which is the solution that you apply. You do not set the pH of the runoff."),
    p("In soil, organic matter and microbes give buffering to the root zone. Thus the target for "
      "the inflow water is approximately 6.0 to 7.0, and the sweet spot is 6.2 to 6.8." +
      _c("unl-passel-soil-ph-definition") + "</p><p>Coco coir is almost inert and has almost no "
      "buffering. Set the pH of the inflow nutrient solution to 5.5 to 6.5. Many growers use 5.8 to "
      "6.2." + _c("malik-tlustos-2025-soilless-media-cannabis") + "</p><p>In hydroponics, the "
      "target is 5.5 to 6.5. The sweet spot for all nutrients is 5.8 to 6.2." +
      _c("kudirka-2023-precise-hydroponic-ph-mes-buffer")),
    table(["Substrate", "Buffering", "Full range", "Sweet spot", "Cause"], [
      ["<strong>Soil</strong>", "High", "6.0-7.0", "6.2-6.8", "Microbes and organic matter keep the pH stable"],
      ["<strong>Coco coir</strong>", "Very low", "5.5-6.5", "5.8-6.2", "Almost inert. The pH changes fast. Set it for each feed."],
      ["<strong>Hydroponics</strong>", "None", "5.5-6.5", "5.8-6.2", "Only water. The pH changes immediately. Monitor it carefully."],
    ], cls="compact", caption="In coco and hydroponics, the pH changes almost immediately because they have no buffering. Soil has more buffering, but you correct it more slowly."),
    p("Some growers change the target by a small quantity in the range during the week, to increase "
      "the availability of specified nutrients. If you are a new grower, select one value in the "
      "sweet spot and keep it."),
  ]})

SECTIONS.append({"id": "measuring-calibrating", "kicker": "The instrument",
  "title": "pH measurement, calibration and meter maintenance",
  "blocks": [
    p("A pH pen is correct only if the last calibration is correct. A probe that you did not "
      "calibrate, or that is dry, is worse than no reading. It shows an incorrect value and gives "
      "no sign of the problem."),
    p("Calibrate the pen with new two-point buffer solutions: first pH 7.0 and then pH 4.0. Do this "
      "approximately one time each month. A calibration with one point is not sufficient for the "
      "complete range that you use." + _c("umass-water-quality-ph-alkalinity") +
      "</p><p>Keep the tip of the probe wet in KCl storage solution. Do not keep it dry. Do not "
      "keep it in plain water, because plain water removes the reference electrolyte. This "
      "decreases the accuracy permanently. Replace the probe when the drift between calibrations is "
      "more than approximately 0.2 pH. Also replace it when the reading is not stable in "
      "approximately 30 seconds."),
    figure(L.flow("Calibrate and measure, in sequence",
            [("Clean", "clean tip with distilled water"),
             ("Calibrate 7.0", "put the tip in pH 7.0 buffer"),
             ("Clean", "between buffers"),
             ("Calibrate 4.0", "put the tip in pH 4.0 buffer"),
             ("Measure", "read your sample"),
             ("Keep wet", "put a cap with KCl solution")]), 3,
      "Do a two-point calibration each time. Clean the tip between the steps. Then keep the tip "
      "wet. Dry storage is the most frequent cause of a defective pen."),
    callout("tip", "Wait until the reading is stable",
      p("Wait until the reading stops before you use it. A change of temperature changes the value. "
        "If you mix the solution, the value also changes. Thus read the pH at room temperature and "
        "wait until the reading is stable.")),
  ]})

SECTIONS.append({"id": "adjusting-and-water", "kicker": "Mixing and adjusting",
  "title": "pH adjustment and the effects of source water",
  "blocks": [
    p("First mix your nutrients, then adjust the pH. When you add nutrients, the pH changes. Thus "
      "if you set the pH before you mix the nutrients, you must set it again."),
    steps([
      ("Mix nutrients", "First add all your feed to the water and mix it."),
      ("Measure", "Read the pH of the mixed solution when the reading is stable."),
      ("Adjust in small steps", "Add a small quantity of pH Down or pH Up, some drops each time."),
      ("Mix and wait", "Mix the solution and wait a short time."),
      ("Measure again", "Read the pH again. Do the steps again with small quantities. Do not add a large quantity at one time."),
    ]),
    p("The usual pH Down products contain phosphoric acid, nitric acid, sulfuric acid or organic "
      "acids. The usual pH Up products contain KOH or potassium carbonate. Each product adds "
      "nutrients. Include these nutrients when you calculate the feed." +
      _c("saloner-bernstein-2022-nitrogen-source-cannabis") + "</p><p>Your source water is more "
      "important than many new growers think. Tap water has a quantity of dissolved bicarbonates "
      "that absorb acid before the pH reading changes. This quantity is the alkalinity. The unit is "
      "ppm CaCO3." + _c("umass-water-quality-ph-alkalinity") + " Water with high alkalinity will "
      "increase in pH again after you set the pH. The remaining bicarbonates continue to react with "
      "the acid that you added."),
    figure(L.bars("The same pH, but very different work to change it",
            [("Low alkalinity (soft water)", 3), ("Example range for a small container", 8), ("High alkalinity (hard water)", 22)],
            unit=" drops", note="The correct alkalinity range changes with the container volume, the media, the crop and the fertilizer.",
            maxv=26), 4,
      "The alkalinity, and not the pH reading, gives the quantity of acid that is necessary to "
      "change the pH of the water. Hard water, which has high alkalinity, does not change its pH "
      "easily when you adjust it, and the pH increases again." + _c("umass-water-quality-ph-alkalinity")),
    callout("note", "The alkalinity must agree with the container system",
      p("UMass gives different alkalinity ranges for different volumes of containers. Approximately "
        "40 to 80 ppm CaCO3 can be correct for small containers, and larger pots can have a higher "
        "alkalinity. You set the range for your system with the media, the fertilizer, the crop and "
        "the pH drift that you monitor. For very hard water, an acid treatment or filtration can be "
        "necessary." + _c("umass-water-quality-ph-alkalinity"))),
  ]})

SECTIONS.append({"id": "runoff-and-routine", "kicker": "Procedure for each day",
  "title": "Runoff pH and the procedure for each stage",
  "blocks": [
    p("Runoff is the solution that drains from the pot. New growers use it too much. In inert media "
      "such as coco, the runoff does not measure the root zone directly. It is a sample from one "
      "time only. Salt buildup and the local changes that the roots make change the value. The "
      "runoff is not a soil test." + _c("malik-tlustos-2025-soilless-media-cannabis")),
    p("The correct lever is the pH of the inflow that you set. For the root zone, monitor the "
      "runoff EC for salt buildup and not the runoff pH. When the runoff EC is much higher than "
      "your feed EC, a flush is necessary. Think that a difference between the runoff EC and the "
      "feed EC that becomes larger is salt buildup. But in crop steering, you can select a higher "
      "root-zone EC." + _c("kpai-2024-cannabis-nutrient-solution-ph-cation-uptake")),
    table(["Stage", "Inflow pH target", "EC to monitor", "Calibration", "Flush trigger"], [
      ["Seedling", "5.8-6.2", "Low feed EC, careful feed", "Each month", "Runoff EC much higher than the feed EC"],
      ["Vegetative stage", "5.8-6.2", "If the EC increases, there is salt buildup", "Each month", "Runoff EC that becomes much higher than the feed EC"],
      ["Flowering stage", "5.8-6.2", "Monitor the runoff EC and the feed EC (new grower: prevent a large increase of salts)", "Each month", "Runoff EC that increases each day"],
    ], cls="compact", caption="The values are for coco and hydroponics. In soil, the runoff gives some more information, but it is slower and it has buffering. Set the inflow at each feed. Do not apply feed with a pH that is not in the range to correct a runoff value."),
    callout("tip", "The procedure in five tasks",
      ul(["Calibrate the pen each month with new two-point buffer.",
          "Mix the nutrients, then set the pH, for each batch.",
          "Set the pH of the inflow in the range at each feed.",
          "Record the inflow pH and EC. Then you can see the drift.",
          "Adjust slowly, with drops. Thus the buffering has time to operate."], "tight")),
  ]})

SECTIONS.append({"id": "pitfalls", "kicker": "Do not do this",
  "title": "Troubleshooting",
  "blocks": [
    p("The grower causes most pH problems. The usual error is to apply nutrient solution that is "
      "not in the safe range, to correct a runoff reading. This error causes the lockout that the "
      "grower wants to prevent." + _c("malik-tlustos-2025-soilless-media-cannabis") +
      " The other problems are about tools and about the time that you wait."),
    table(["Frequent error", "Correct procedure"], [
      ["You try to correct the runoff pH and you apply feed that is not in the range", "Set the inflow in the range at each feed. Monitor the runoff EC and not the runoff pH."],
      ["You do not calibrate the probe, or you keep it dry or in plain water", "Do a two-point calibration each month. Keep the probe wet in KCl."],
      ["You adjust the pH before you mix the nutrients", "First mix the nutrients, then set the pH."],
      ["You add a large quantity of acid at one time, and the pH becomes lower than the target", "Add some drops, mix, wait, and measure again."],
      ["You add more nutrients to correct a deficiency", "First examine the pH. The cause is frequently lockout and not a low quantity of nutrients."],
      ["You do not examine the alkalinity of the source water", "Do a test of the alkalinity. Apply a treatment to hard water before the pH increases slowly."],
    ], cls="compact"),
  ]})

SECTIONS.append({"id": "expectations", "kicker": "Usual results", "title": "Expected results and limitations",
  "blocks": [
    p("The pH changes between feeds. This change is usual, and it is not a problem. The target is "
      "to keep the root zone in a range. It is not necessary to keep one accurate decimal value. "
      "Soil has buffering, thus the pH corrects slowly. In coco and hydroponics, the pH changes "
      "quickly and you must monitor it at each feed."),
    figure(L.line("Root-zone pH in one week: small changes are usual, large changes are not",
            [(0, 6.0), (1, 5.9), (2, 6.1), (3, 5.8), (4, 6.2), (5, 6.8), (6, 6.0)],
            ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
            ylab="pH", ymin=5.0, ymax=7.5,
            bands=[(5.8, 6.2, L.GL, "target range")],
            note="Small changes in the range are correct. On Saturday the value is not in the range: correct it."), 5,
      "In a usual week, the pH stays in the target range (the green area) with small changes. The "
      "one value that is higher than the range is the signal to examine the pen, the water and the "
      "feed."),
    callout("key", "The correct result",
      ul(["The target is a range such as 5.8 to 6.2, and not one accurate value.",
          "A change of the pH between feeds is usual. In coco and hydroponics, you must do a check at each feed. Soil is slower.",
          "A pen has a short life. Calibrate it each month. Replace the probe after some time.",
          "Record each feed. The data for some weeks show more than one reading."], "tight")),
    p("When a deficiency symptom shows, read the <a href='nutrient-deficiencies.html'>nutrient "
      "deficiencies</a> guide. Make sure that the pH is correct before you change the feed formula. "
      "If the alkalinity of the source water is the problem, the <a href='water-quality.html'>water "
      "quality</a> guide shows how to apply a treatment to it."),
  ]})
