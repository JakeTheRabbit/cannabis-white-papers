# -*- coding: utf-8 -*-
"""Paper: substrates compared - coco, rockwool, soil, hydro (beginner)."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        stagecard, grid, card, chip, kv, steps)
import figs_lib as L

SLUG = "substrates-overview"
TITLE = "Substrates compared: coco, rockwool, soil, hydro"
EYEBROW = "Beginner · Substrate"
SUB = ("A from-zero guide to what cannabis roots grow in: how each medium holds water and air, "
       "how it handles nutrients, how forgiving it is, and how to pick one.")
META = [("seedling", "Beginner"), ("image", "11 diagrams"),
        ("quote", "Peer-reviewed · 9 sources"), ("clock", "~11 min read")]
RELATED = ["coco-crop-steering", "ph-management", "water-quality"]
REF_IDS = ["xiong-2017-coir-rockwool-peat-tomato", "abad-2002-coir-dust-peat-substitute",
           "bevan-2021-cannabis-npk-soilless", "cockson-2019-cannabis-nutrient-disorders",
           "le-pythium-hydroponic-epidemiology-review", "frontiers-2026-do-pythium-strawberry-nft",
           "raviv-lieth-soilless-culture-afp", "joseph-2024-rockwool-recovery-composting",
           "abad-2017-peat-use-horticulture"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

SECTIONS.append({"id": "what-this-is", "kicker": "Start here", "title": "What this is (and who it's for)",
  "blocks": [
    lead("A <strong>substrate</strong> (also called a growing medium) is just the material a plant's "
         "roots live in. It holds the plant up and acts as the reservoir for water, air and dissolved "
         "nutrients. This guide compares the five materials cannabis growers actually use, assuming "
         "you know nothing yet."),
    p("By the end you will understand the two trade-offs that decide everything: how much water "
      "versus air a medium holds, and how much it cushions your nutrient mistakes. With those two "
      "ideas you can pick the right medium for your setup."),
    figure(L.flow("Where do the roots live?",
            [("In a solid medium", "coco, rockwool, peat, living soil hold the roots"),
             ("In water and air", "DWC: roots dangle in oxygenated nutrient water")],
            note="Five options, two families. The rest of this guide is about telling them apart."), 1,
      "The whole field splits into media that physically hold the roots and water culture where the "
      "roots hang in the solution itself."),
    callout("note", "Who this is for",
      p("Total beginners choosing a first medium, and anyone who wants to know why their setup "
        "behaves the way it does. It pairs with the "
        "<a href='coco-crop-steering.html'>coco crop-steering paper</a>, which goes deep on driving "
        "one specific medium hard once you have picked it.")),
  ]})

SECTIONS.append({"id": "key-terms", "kicker": "Vocabulary", "title": "Key terms, defined once",
  "blocks": [
    p("Two numbers describe how any medium behaves when wet. The rest are about nutrients. You do "
      "not need to memorise these, just get the gist."),
    defterm("Water-holding capacity", "The share of the pore space that still holds water after the "
            "medium drains. Higher means it stays wetter for longer."),
    defterm("Air-filled porosity", "The share of the pore space holding air at that same drained "
            "moment. Water and air share one fixed total, so more water means less air."),
    defterm("EC (electrical conductivity)", "How much dissolved nutrient salt is in the water, in "
            "milliSiemens per centimetre (mS/cm). Higher EC is a stronger, saltier feed."),
    defterm("pH", "Acidity on a 0-14 scale. The cannabis root-zone sweet spot is about 5.5-6.5, "
            "tightening to 5.8-6.2 for precise soilless control." + _c("cockson-2019-cannabis-nutrient-disorders")),
    defterm("CEC (cation exchange capacity)", "A medium's ability to grab and hold nutrient ions in "
            "reserve, measured in meq/100g." + _c("abad-2002-coir-dust-peat-substitute") +
            " High CEC means the medium buffers (cushions) your feeding mistakes."),
    defterm("Buffering", "The medium absorbing your errors. A buffered medium forgives a bad mix. "
            "An inert one passes it straight to the roots."),
    defterm("Dryback", "How far a medium dries between waterings. It is the lever crop steering uses, "
            "covered in the <a href='coco-crop-steering.html'>coco paper</a>."),
    figure(L.zones("One fixed pore space, split between water and air", 0, 100,
            [(0, 78, L.BLUL, "Water-holding"), (78, 100, L.GL, "Air")], unit="%",
            note="Saturate the medium and the slider shoves toward water, starving roots of oxygen."), 2,
      "Total pore space is a fixed bar. Wetting the medium pushes the split toward water and squeezes "
      "out the air the roots need to breathe."),
  ]})

SECTIONS.append({"id": "water-vs-air", "kicker": "Core concept 1", "title": "Water versus air: the porosity trade-off",
  "blocks": [
    p("Roots need oxygen as much as water. A medium that stays saturated drowns the roots and invites "
      "rot, while one that holds too little water dries out and stresses the plant. The five media sit "
      "at different points on that see-saw."),
    p("Rockwool is roughly 96% total porosity but only about 11% air-filled, with around 91% "
      "water-holding, so it holds a lot of water and releases it freely" + _c("raviv-lieth-soilless-culture-afp") +
      ". Peat sits near 90-95% total porosity with a higher 18-25% air fraction" + _c("abad-2017-peat-use-horticulture") +
      ". Coco coir is the standout: even saturated it can keep around 22% air, beating rockwool's "
      "~10%, which is why coco resists drowning" + _c("abad-2002-coir-dust-peat-substitute") +
      ". DWC is the extreme case, where roots dangle in nutrient water and get oxygen only from a "
      "pump."),
    figure(L.bars("Air-filled porosity when fully wet",
            [("Coco coir", 22), ("Peat", 21), ("Rockwool", 11)], unit="%",
            note="Air at the roots when saturated. Higher means harder to overwater.", maxv=30), 3,
      "Coco keeps the most air when wet, which is why it is hard to overwater. Peat is naturally "
      "airier than rockwool." + _c("abad-2002-coir-dust-peat-substitute") + _c("raviv-lieth-soilless-culture-afp")),
    table(["Medium", "Total porosity", "Air-filled", "Water-holding", "Air when saturated"], [
      ["Rockwool", "~96%", "~11%", "~91%", "~10%"],
      ["Coco coir", "~94-96%", "high", "high", "~22%"],
      ["Peat", "~90-95%", "18-25%", "high", "moderate"],
    ], cls="compact", caption="After draining, irrigated rockwool holds roughly 80% solution, 15% air "
      "and 5% fibre by volume." + _c("raviv-lieth-soilless-culture-afp")),
    callout("key", "The whole game in one line",
      p("More water means less air. The medium that keeps air around the roots even when wet is the "
        "one that forgives a heavy hand on the watering.")),
  ]})

SECTIONS.append({"id": "ec-buffering", "kicker": "Core concept 2", "title": "How each medium handles nutrients",
  "blocks": [
    p("An inert medium like rockwool holds almost no nutrients of its own. Its native EC is "
      "negligible and its pH is alkaline, around 8, so whatever you feed is exactly what the roots "
      "get" + _c("raviv-lieth-soilless-culture-afp") + ". That is precise, but unforgiving of a bad "
      "mix."),
    p("Coco is the opposite. Its high CEC, roughly 40-100 meq/100g, buffers EC swings, but raw "
      "coco's exchange sites come pre-loaded with potassium and sodium and will strip calcium and "
      "magnesium out of your feed" + _c("abad-2002-coir-dust-peat-substitute") + ". That causes a "
      "cal-mag deficiency unless the coco is buffered (pre-soaked in cal-mag) or bought "
      "pre-buffered" + _c("cockson-2019-cannabis-nutrient-disorders") + "."),
    p("Living soil is the most forgiving of all. Microbes, organic matter and minerals hold the "
      "root zone near pH 5.2-6.5 within minutes of watering regardless of your water's pH, so you "
      "generally do not pH your input at all. In DWC there is no buffer at all: the reservoir is the "
      "only thing standing between your plants and a mistake."),
    figure(L.zones("The forgiveness scale: how much each medium cushions", 0, 100,
            [(0, 30, L.REDL, "Inert: DWC, rockwool"), (30, 65, L.AMBL, "Buffered: coco"),
             (65, 100, L.GL, "Self-regulating: living soil")], unit="",
            note="Left absorbs nothing. Right corrects your pH for you. Coco buffers EC but needs pre-buffering for Ca/Mg."), 4,
      "From no cushion (DWC, rockwool) through coco's EC buffering to living soil, which self-regulates "
      "pH after every watering."),
    callout("tip", "Match the cushion to your patience",
      p("If you cannot promise a perfect feed every time, pick a medium that forgives you. The more "
        "control a medium gives, the less it protects you from yourself.")),
  ]})

SECTIONS.append({"id": "reuse-cost", "kicker": "Core concept 3", "title": "Re-use, cost and footprint",
  "blocks": [
    p("Media differ enormously in how many runs you get. Rockwool can be re-used for up to about "
      "three years with proper sanitation, but it is energy-intensive to make and banned from "
      "landfill in some countries, which is why it has declined in parts of Europe and "
      "Japan" + _c("joseph-2024-rockwool-recovery-composting") + ". Coco can be rinsed, re-buffered "
      "and re-used for a few cycles, then composted into garden soil, though most is shipped from "
      "overseas."),
    p("Living soil is the re-use champion. A recycled organic living soil (ROLS) bed is amended "
      "between runs and grows indefinitely, getting better with age. DWC has no medium to dispose "
      "of, but you replace the nutrient reservoir constantly and depend on continuous electricity "
      "for the pumps. Peat is cheap and effective but is a slowly renewing resource with a real "
      "carbon cost, which pushes many growers toward coco" + _c("abad-2017-peat-use-horticulture") + "."),
    table(["Medium", "Typical re-use", "End-of-life", "Cost tier", "Environmental note"], [
      ["Living soil", "Indefinite (ROLS, amend)", "Stays in service", "Low after setup", "Lowest waste once established"],
      ["Coco coir", "A few re-buffered cycles", "Composts into soil", "Low-medium", "High shipping footprint"],
      ["Peat", "Single use typical", "Compostable", "Low", "Slow to renew, carbon cost"],
      ["Rockwool", "~3 years with sanitation", "Landfill-restricted in places", "Medium", "Energy-heavy to make"],
      ["DWC", "No medium", "Nothing to discard", "Medium (gear + power)", "Constant reservoir + 24/7 power"],
    ], cls="compact", caption="There is no clean winner. The lowest-waste option (living soil) needs "
      "the most up-front work."),
  ]})

SECTIONS.append({"id": "choose-by-stage", "kicker": "Decide", "title": "How to choose: a beginner's decision path",
  "blocks": [
    p("Match the medium to your tolerance for fiddling, not to what wins a yield contest. The right "
      "answer is the one whose daily demands you will actually keep up with."),
    figure(L.flow("Pick by how hands-on you want to be",
            [("Water-only, low-tech", "living soil or quality peat-based soil mix"),
             ("Feed daily, watch EC/pH", "pre-buffered coco, also the on-ramp to crop steering"),
             ("Parameters already dialed", "rockwool, after irrigation is consistent"),
             ("Constant monitoring OK", "DWC, highest reward and lowest safety margin")],
            note="Start at the top. Drop down a step only when you are ready for more daily tech."), 5,
      "A simple ladder from most forgiving to most demanding. Most beginners should start at the top "
      "two rungs."),
    figure(L.bars("Beginner forgiveness score",
            [("Living soil", 9), ("Peat / soil mix", 8), ("Coco (pre-buffered)", 6),
             ("Rockwool", 4), ("DWC", 2)], unit="/10",
            note="How much daily slack the medium gives a beginner. Higher is safer to learn on.", maxv=10), 6,
      "Living soil and quality soil mixes forgive the most. DWC forgives the least, so it is not a "
      "first grow."),
    callout("warn", "Skip DWC for your first run",
      p("DWC can give explosive growth, but a warm reservoir or a dead air pump can kill a plant in "
        "a day" + _c("frontiers-2026-do-pythium-strawberry-nft") + ". Learn the basics in a more "
        "forgiving medium first.")),
  ]})

SECTIONS.append({"id": "by-stage-setup", "kicker": "Do it", "title": "Setting up and running each, step by step",
  "blocks": [
    p("Every medium has one non-negotiable prep step. Get that right and the rest is routine."),
    steps([
      ("Coco", "Rinse and pre-buffer: soak 8-24h in a cal-mag solution unless bought pre-buffered. Then feed every watering at pH 5.8-6.2 and low EC, watering little and often."),
      ("Rockwool", "Pre-soak the cubes or slabs at pH ~5.5 before transplanting, because dry rockwool sits near pH 8. After that, never let it go bone-dry."),
      ("Living soil", "Build or buy the bed, let it cycle a few weeks, then water-only. Leave pH alone unless symptoms appear."),
      ("DWC", "Hold the reservoir at 18-20C (65-68F), dissolved oxygen at 7-9 mg/L, pH 5.5-6.0, and run the air pump 24/7."),
    ]),
    table(["Medium", "Prep step", "Feed / water routine", "pH target", "Do not skip"], [
      ["Coco", "Rinse + cal-mag buffer", "Feed every watering, low EC", "5.8-6.2", "The pre-buffer soak"],
      ["Rockwool", "Pre-soak at pH ~5.5", "Frequent, never dry out", "5.5-6.0", "Conditioning before planting"],
      ["Living soil", "Cycle a few weeks", "Water-only", "Leave alone", "Not pH-ing the water"],
      ["DWC", "Set up pump + chiller", "Recirculating reservoir", "5.5-6.0", "Air pump on 24/7"],
    ], cls="compact", caption="The single thing most beginners skip is the prep column. Each one is "
      "the difference between a smooth start and an early problem." + _c("cockson-2019-cannabis-nutrient-disorders")),
    figure(L.zones("DWC reservoir: the kill-zone made visible", 14, 28,
            [(14, 18, L.AMBL, "cool"), (18, 20, L.GL, "target 18-20C"),
             (20, 23, L.AMBL, "caution"), (23, 28, L.REDL, "root-rot risk >23C")], unit="C",
            note="Pythium root rot climbs sharply above ~23C reservoir temperature. Keep dissolved oxygen 7-9 mg/L."), 7,
      "Keep the reservoir in the green band. Above about 23C the dissolved oxygen drops and Pythium "
      "root rot takes hold." + _c("le-pythium-hydroponic-epidemiology-review") + _c("frontiers-2026-do-pythium-strawberry-nft")),
  ]})

SECTIONS.append({"id": "pitfalls", "kicker": "Avoid", "title": "Common pitfalls and how to dodge them",
  "blocks": [
    p("The classic beginner mistakes are medium-specific, and most look like something they are not."),
    table(["Medium", "Classic mistake", "What you see", "The fix"], [
      ["Coco", "Skipping the buffer step", "Cal-mag deficiency: rusty spots, yellowing", "Pre-buffer the coco, add cal-mag to early feeds"],
      ["Rockwool", "Planting into dry cubes", "Pale, locked-out plant (pH-8 lockout)", "Pre-soak at pH ~5.5 before transplant"],
      ["Rockwool", "Overwatering low-air matrix", "Slow, soggy, suffocating roots", "Fewer shots, let it breathe between"],
      ["Living soil", "pH-ing water or adding salts", "Stalled growth, dying microbes", "Water-only, leave the pH alone"],
      ["DWC", "Warm water or dead air pump", "Root rot within ~24h", "Chill below 23C, keep the pump running"],
    ], cls="compact", caption="The coco and rockwool rows are misread as feeding problems. They are "
      "really prep problems." + _c("cockson-2019-cannabis-nutrient-disorders") + _c("le-pythium-hydroponic-epidemiology-review")),
    callout("danger", "The number one DWC killer",
      p("A warm reservoir above 23C or a failed air pump crashes dissolved oxygen and brings on root "
        "rot within a day" + _c("frontiers-2026-do-pythium-strawberry-nft") + ". If you run DWC, a "
        "chiller and a backup air pump are not optional.")),
  ]})

SECTIONS.append({"id": "expectations", "kicker": "Reality check", "title": "Realistic expectations",
  "blocks": [
    p("No medium grows the plant for you. They differ in where the difficulty sits, not in whether "
      "there is difficulty. Living soil front-loads the work of building the bed, then runs "
      "hands-off. Coco and rockwool spread the work across daily feeding and monitoring. DWC "
      "concentrates the risk into a few parameters that must never slip."),
    figure(L.line("Daily effort versus the ceiling for yield and speed",
            [(0, 5), (1, 6), (2, 8), (3, 8), (4, 9)],
            ["Living soil", "Peat / soil", "Coco", "Rockwool", "DWC"],
            ylab="ceiling", ymin=0, ymax=10,
            note="Left to right is rising daily effort and risk. Height is the ceiling you can reach when dialed in."), 8,
      "Effort and risk climb from left to right. The ceiling rises too, but only the disciplined "
      "grower reaches it. A tidy soil grow beats a sloppy hydro one every time."),
    p("Fed precisely, inert media like coco and rockwool can edge out soil on yield and speed in "
      "research comparisons" + _c("xiong-2017-coir-rockwool-peat-tomato") +
      ", and soilless cannabis responds strongly to dialed-in feeding" + _c("bevan-2021-cannabis-npk-soilless") +
      ". But that only holds once your environment and irrigation are consistent."),
    callout("key", "How to actually get good",
      ol(["<strong>Pick the failure mode you can live with.</strong> Every medium fails differently. Choose the one whose worst case you can prevent.",
          "<strong>Run one full cycle before you judge it.</strong> You learn a medium by living a whole grow in it, not by reading about it.",
          "<strong>Change one variable next time.</strong> Do not switch everything at once, or you will never know what helped."])),
    p("Get one full run under your belt, then refine. When you are ready to drive a medium hard, the "
      "<a href='coco-crop-steering.html'>coco crop-steering paper</a> picks up where this one leaves "
      "off, and the <a href='ph-management.html'>pH guide</a> covers the number that quietly decides "
      "whether your feed even reaches the roots."),
  ]})
