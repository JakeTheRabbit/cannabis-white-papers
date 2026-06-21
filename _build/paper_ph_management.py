# -*- coding: utf-8 -*-
"""Paper: root-zone pH management for beginners."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        stagecard, grid, card, chip, kv, steps)
import figs_lib as L

SLUG = "ph-management"
TITLE = "pH: what it is and how to hold it"
EYEBROW = "Feed · pH"
SUB = ("A beginner's guide to root-zone pH: why one number decides which nutrients your plant can "
       "actually eat, what to aim for in coco, hydro and soil, and how to measure, adjust and hold "
       "it without chasing ghosts.")
META = [("flask", "Feed"), ("image", "8 diagrams"),
        ("quote", "Peer-reviewed · 6 sources"), ("clock", "~14 min read")]
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
  "title": "What this is (and why one number matters so much)",
  "blocks": [
    lead("pH is a 0-14 scale for how acidic or alkaline a liquid is. 7 is neutral, lower is acidic, "
         "higher is alkaline. For a grower it is the single setting that decides whether the "
         "nutrients you already paid for can actually enter the roots. Get it wrong and a fully fed "
         "plant can still starve."),
    p("This guide assumes you know nothing about chemistry and builds up from the scale itself to a "
      "daily routine you can run. Pure water sits at 7. Lemon juice is around 2 (strongly acidic). "
      "Baking soda solution is around 8.5 (mildly alkaline)."),
    p("One thing trips people up: the scale is logarithmic, so each whole number is a tenfold change "
      "in acidity. pH 5 is ten times more acidic than pH 6, and a hundred times more acidic than "
      "pH 7." + _c("unl-passel-soil-ph-definition") + " That is why a reading that looks &lsquo;close "
      "enough&rsquo; can still be far outside the window your roots need."),
    figure(L.zones("The pH scale and your grower target",
            0, 14,
            [(0, 2, L.REDL, "lemon ~2"), (5.5, 6.5, L.GL, "grower target 5.5-6.5"),
             (7, 7, L.BLUL, "pure water 7"), (8, 9, L.AMBL, "baking soda ~8.5")],
            unit="", note="Most root-zone feeding aims at the narrow green band, not at neutral."), 1,
      "Everyday liquids on the pH scale, with the 5.5-6.5 band most growers feed inside. Neutral "
      "water (7) is already too high for coco and hydro."),
    callout("key", "The whole point in one line",
      p("You can have perfect nutrients and perfect light and still get deficiencies purely from bad "
        "pH. The number gates everything downstream.")),
  ]})

SECTIONS.append({"id": "key-terms", "kicker": "Vocabulary", "title": "Key terms in plain English",
  "blocks": [
    p("These words come back through the rest of the guide. Read them once and the troubleshooting "
      "section will read cleanly."),
    defterm("pH", "How acidic or alkaline the water around the roots is, on a 0-14 scale."),
    defterm("Root zone", "The wet substrate immediately around the roots, where uptake actually "
            "happens."),
    defterm("Lockout", "Nutrients are present but chemically unavailable, so the plant shows a "
            "deficiency even though it is being fed."),
    defterm("EC (electrical conductivity)", "How strong or salty the nutrient solution is. A "
            "separate dial from pH. <a href='nutrient-mixing-athena.html'>Mixing guide &rarr;</a>"),
    defterm("Substrate / medium", "What the roots grow in: coco coir, rockwool or water in hydro, "
            "or soil."),
    defterm("Buffering", "A medium or water's resistance to pH change. High buffering is stubborn, "
            "low buffering swings fast."),
    defterm("Alkalinity", "The water's built-in acid-absorbing capacity, mostly bicarbonates. Not "
            "the same thing as a high pH reading."),
    defterm("Runoff", "The solution that drains out the bottom of the pot after watering."),
  ]})

SECTIONS.append({"id": "why-ph-controls-availability", "kicker": "The core idea",
  "title": "Why pH controls availability (and causes lockout)",
  "blocks": [
    p("Each nutrient stays dissolved, and therefore absorbable, only across a certain pH band. "
      "Outside that band it binds into forms the roots cannot take up. That is lockout: the plant is "
      "surrounded by food it cannot eat because the root-zone chemistry drifted out of the window."),
    p("Push pH too high, above about 6.5 in inert media like coco or hydro, and the micronutrients "
      "drop out of solution first: iron, manganese, zinc and boron." + _c("veazie-2025-substrate-ph-micronutrient-cannabis") +
      " Drop it too low, below about 5.5, and calcium, magnesium and phosphorus lock out "
      "instead." + _c("gillespie-kubota-2020-low-ph-basil-nutrient-uptake")),
    p("Phosphorus is the clearest example. It is most available around pH 6.0-7.0, binds with iron "
      "and aluminium below 5.5, and binds with calcium above 7.5." + _c("kpai-2024-cannabis-nutrient-solution-ph-cation-uptake") +
      " The &lsquo;sweet spot&rsquo; exists because it is the pH where the most nutrients overlap as "
      "available at once."),
    figure(L.zones("Where each nutrient is available across pH",
            4, 8,
            [(5.5, 6.5, L.GL, "all overlap 5.5-6.5"),
             (4.0, 5.5, L.REDL, "Ca / Mg / P lock low"),
             (6.5, 8.0, L.AMBL, "Fe / Mn / Zn / B lock high")],
            unit="", note="The green band is where micros and the big cations are available together."), 2,
      "Calcium, magnesium and phosphorus fail at low pH; iron, manganese, zinc and boron fail at "
      "high pH. The 5.5-6.5 overlap is the only band where all are available." + _c("veazie-2025-substrate-ph-micronutrient-cannabis")),
    callout("warn", "Lockout looks exactly like a deficiency",
      p("Because the symptoms match, growers often add more nutrients and make it worse. Check pH "
        "first, before reaching for the bottle.")),
  ]})

SECTIONS.append({"id": "targets-by-substrate", "kicker": "Your numbers",
  "title": "Target ranges by substrate: coco, hydro, soil",
  "blocks": [
    p("There is no single correct pH, because the right target depends on what the roots are sitting "
      "in. The number you control is the inflow, what you pour in, not the runoff."),
    p("In soil, organic matter and microbes buffer the root zone, so aim for inflow water at roughly "
      "6.0-7.0 with a sweet spot of 6.2-6.8." + _c("unl-passel-soil-ph-definition") +
      " In coco coir, which is nearly inert with almost no buffering, set the inflow nutrient "
      "solution to 5.5-6.5, and many growers run 5.8-6.2." + _c("malik-tlustos-2025-soilless-media-cannabis") +
      " In hydroponics, target 5.5-6.5 with 5.8-6.2 as the all-nutrient sweet spot." + _c("kudirka-2023-precise-hydroponic-ph-mes-buffer")),
    table(["Substrate", "Buffering", "Full range", "Sweet spot", "Why"], [
      ["<strong>Soil</strong>", "High", "6.0-7.0", "6.2-6.8", "Microbes and organic matter hold it steady"],
      ["<strong>Coco coir</strong>", "Very low", "5.5-6.5", "5.8-6.2", "Nearly inert, swings fast, set it per feed"],
      ["<strong>Hydro</strong>", "None", "5.5-6.5", "5.8-6.2", "Water only, moves immediately, watch closely"],
    ], cls="compact", caption="Coco and hydro respond to pH swings almost instantly because they cannot buffer. Soil is more forgiving but slower to correct."),
    p("Some growers nudge the target slightly within range across the week to favour specific "
      "nutrients. As a beginner, pick one number in the sweet spot and hold it."),
  ]})

SECTIONS.append({"id": "measuring-calibrating", "kicker": "The tool",
  "title": "Measuring it: pen, calibration and care",
  "blocks": [
    p("A pH pen is only as honest as its last calibration. An uncalibrated or dried-out probe is "
      "worse than no reading, because it lies with confidence."),
    p("Calibrate with fresh two-point buffers, pH 7.0 first then pH 4.0, about once a month. A "
      "single-point calibration is not enough to trust across your whole working range." + _c("umass-water-quality-ph-alkalinity") +
      " Store the probe tip wet in KCl storage solution, never dry and never in plain water, which "
      "strips the reference electrolyte and permanently kills accuracy. Retire the probe when drift "
      "exceeds about 0.2 pH between calibrations or it cannot settle within about 30 seconds."),
    figure(L.flow("Calibrate and measure, in order",
            [("Rinse", "clean tip with distilled water"),
             ("Cal 7.0", "set in pH 7.0 buffer"),
             ("Rinse", "between buffers"),
             ("Cal 4.0", "set in pH 4.0 buffer"),
             ("Measure", "read your sample"),
             ("Store wet", "cap in KCl solution")]), 3,
      "Two-point calibration every time, rinsing between steps, then store the tip wet. Dry storage "
      "is the most common way pens die."),
    callout("tip", "Let it settle",
      p("Give the reading time to stop moving before you trust it. Temperature and stirring both "
        "shift the number, so read at room temperature and wait for it to hold steady.")),
  ]})

SECTIONS.append({"id": "adjusting-and-water", "kicker": "Making the number",
  "title": "Adjusting with pH up/down, and the water you start with",
  "blocks": [
    p("Mix your nutrients first, then adjust pH last. Adding nutrients shifts pH on its own, so if "
      "you set pH before mixing you will have to redo it."),
    steps([
      ("Mix nutrients", "Add and stir all your feed into the water first."),
      ("Measure", "Take a settled pH reading of the mixed solution."),
      ("Adjust small", "Add pH Down or pH Up a few drops at a time."),
      ("Stir and wait", "Mix it in and give it a moment to react."),
      ("Re-measure", "Read again. Repeat in small steps, never dump and chase."),
    ]),
    p("pH Down is usually phosphoric acid and pH Up is usually potassium hydroxide." + _c("saloner-bernstein-2022-nitrogen-source-cannabis") +
      " Your starting water matters more than beginners expect. Alkalinity is the water's built-in "
      "acid-absorbing capacity, mostly bicarbonates, reported as ppm CaCO3, and it is distinct from a "
      "high pH reading." + _c("umass-water-quality-ph-alkalinity") + " High-alkalinity water fights "
      "your acid and creeps the pH back up after you set it."),
    figure(L.bars("Same pH, very different effort to move it",
            [("Low alkalinity (soft)", 3), ("Target (60-100 ppm)", 8), ("High alkalinity (hard)", 22)],
            unit=" drops", note="Two waters can read pH 7 yet need wildly different amounts of acid to shift.",
            maxv=26), 4,
      "Alkalinity, not the pH reading, sets how much acid it takes to move the water. Hard, "
      "high-alkalinity tap water resists adjustment and drifts back up." + _c("umass-water-quality-ph-alkalinity")),
    callout("note", "Aim for 60-100 ppm CaCO3",
      p("Ideal irrigation alkalinity is roughly 60-100 ppm CaCO3. Very hard water may need more acid "
        "or pre-treatment before it will hold a target." + _c("umass-water-quality-ph-alkalinity"))),
  ]})

SECTIONS.append({"id": "runoff-and-routine", "kicker": "Daily practice",
  "title": "Runoff pH and a by-stage routine",
  "blocks": [
    p("Runoff is the solution that drains from the pot, and beginners over-rely on it. In inert "
      "media like coco it is a momentary, indirect sample distorted by salt buildup and what the "
      "roots have done locally. It is not a soil test." + _c("malik-tlustos-2025-soilless-media-cannabis")),
    p("The reliable lever is the inflow pH you set going in. For the root zone itself, watch runoff "
      "EC for salt accumulation rather than runoff pH: a flush is due when runoff EC climbs well "
      "above your feed EC. Aim to keep feed and runoff EC within about 10 percent of each "
      "other." + _c("kpai-2024-cannabis-nutrient-solution-ph-cation-uptake")),
    table(["Stage", "Inflow pH target", "EC watch", "Calibration", "Flush trigger"], [
      ["Seedling", "5.8-6.2", "Low feed EC, gentle", "Monthly", "Runoff EC well above feed"],
      ["Veg", "5.8-6.2", "Rising EC means salt buildup", "Monthly", "Runoff EC > feed by >10%"],
      ["Flower", "5.8-6.2", "Hold feed and runoff within ~10%", "Monthly", "Runoff EC climbing day on day"],
    ], cls="compact", caption="Coco and hydro figures. Soil runoff is a little more meaningful but still lags and is buffered. Set inflow every feed and do not feed out of range to fix a runoff number."),
    callout("tip", "The routine in five habits",
      ul(["Calibrate the pen monthly with fresh two-point buffer.",
          "Mix nutrients, then set pH, every batch.",
          "Set inflow pH inside the band every feed.",
          "Log inflow pH and EC so you can see drift.",
          "Adjust slowly, in drops, and let buffering work."], "tight")),
  ]})

SECTIONS.append({"id": "pitfalls", "kicker": "Don't do this",
  "title": "Common mistakes and how to avoid them",
  "blocks": [
    p("Most pH problems are self-inflicted. The classic error is feeding nutrient solution outside "
      "the safe range to fix a runoff reading, which causes the very lockout the grower fears." + _c("malik-tlustos-2025-soilless-media-cannabis") +
      " The rest are about tools and patience."),
    table(["Common mistake", "Do this instead"], [
      ["Chasing runoff pH and feeding out of range to correct it", "Set inflow in range every feed, watch runoff EC not runoff pH"],
      ["Never calibrating, or storing the probe dry or in plain water", "Two-point calibrate monthly, store wet in KCl"],
      ["Adjusting pH before mixing nutrients", "Mix nutrients first, set pH last"],
      ["Dumping acid then overshooting", "Add a few drops, stir, wait, re-measure"],
      ["Adding more nutrients to fix a deficiency", "Check pH first; it is often lockout, not a shortage"],
      ["Ignoring source-water alkalinity", "Test alkalinity; treat hard water before it creeps pH up"],
    ], cls="compact"),
  ]})

SECTIONS.append({"id": "expectations", "kicker": "Reality check", "title": "Realistic expectations",
  "blocks": [
    p("pH will drift between feeds, and that is normal, not a crisis. The goal is to keep the root "
      "zone inside a band, not to pin a single decimal. Soil buffers and corrects slowly. Coco and "
      "hydro move fast and need checking every feed."),
    figure(L.line("Root-zone pH over a week: wobble is fine, excursions need action",
            [(0, 6.0), (1, 5.9), (2, 6.1), (3, 5.8), (4, 6.2), (5, 6.8), (6, 6.0)],
            ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
            ylab="pH", ymin=5.0, ymax=7.5,
            bands=[(5.8, 6.2, L.GL, "target band")],
            note="Small wobbles inside the band are healthy. The Saturday spike out of band is what you act on."), 5,
      "A normal week stays inside the shaded target band with minor wobbles. The one excursion above "
      "the band is the signal to check the pen, the water and the feed."),
    callout("key", "What good looks like",
      ul(["A band like 5.8-6.2 is the target, not one exact number.",
          "Drift between feeds is expected; coco and hydro need per-feed checks, soil is slower.",
          "Pens are consumables: calibrate monthly, replace probes over time.",
          "Consistency over weeks beats chasing perfection on any single reading."], "tight")),
    p("Hold the inflow steadily in range over weeks and most &lsquo;mystery&rsquo; deficiencies "
      "never appear. When a symptom does show, read the "
      "<a href='nutrient-deficiencies.html'>nutrient deficiencies</a> guide and check pH before you "
      "change the feed, and sort your source water with the "
      "<a href='water-quality.html'>water quality</a> guide first."),
  ]})
