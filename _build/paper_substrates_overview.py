# -*- coding: utf-8 -*-
"""Paper: substrates compared - coco, rockwool, soil, hydro (beginner)."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        stagecard, grid, card, chip, kv, steps)
import figs_lib as L

SLUG = "substrates-overview"
TITLE = "Substrates compared: coco, rockwool, soil and hydroponics"
EYEBROW = "Basic · Substrate"
SUB = ("This paper compares the substrates for cannabis roots and shows how to select one. It gives "
       "information about the water and air in each medium, the effect of each medium on the "
       "nutrients, and the tolerance for errors. It is not necessary to know about substrates "
       "before you read this paper.")
META = [("seedling", "Basic"), ("image", "11 diagrams"),
        ("quote", "9 sources"), ("clock", "~11 min to read")]
RELATED = ["coco-crop-steering", "ph-management", "water-quality"]
REF_IDS = ["xiong-2017-coir-rockwool-peat-tomato", "abad-2002-coir-dust-peat-substitute",
           "bevan-2021-cannabis-npk-soilless", "cockson-2019-cannabis-nutrient-disorders",
           "le-pythium-hydroponic-epidemiology-review", "frontiers-2026-do-pythium-strawberry-nft",
           "raviv-lieth-soilless-culture-afp", "joseph-2024-rockwool-recovery-composting",
           "abad-2017-peat-use-horticulture"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

SECTIONS.append({"id": "what-this-is", "kicker": "Start here", "title": "Purpose and scope",
  "blocks": [
    lead("A <strong>substrate</strong> (a growing medium) is the material that contains the roots "
         "of a plant. It holds the plant in position, and it is the reservoir for water, air and "
         "dissolved nutrients. This paper compares the five media that cannabis growers use: coco, "
         "rockwool, peat, living soil and deep water culture (DWC). It is not necessary to know "
         "about substrates before you read this paper."),
    p("At the end of this paper, you will know the two properties of a medium that have the largest "
      "effect on the result. The first property is the quantity of water and the quantity of air "
      "that the medium holds. The second property is the tolerance of the medium for your errors. "
      "When the tolerance is high, an error in the nutrients or in the water has a small effect on "
      "the plant. With this information, you can select the correct medium for your setup."),
    figure(L.flow("The position of the roots",
            [("In a solid medium", "coco, rockwool, peat and living soil hold the roots"),
             ("In water and air", "DWC: roots in water with nutrients and oxygen")],
            note="Five alternatives in two groups. This paper shows how they are different."), 1,
      "The alternatives are in two groups: the media that hold the roots in position, and water "
      "culture. In water culture, the roots hang in the nutrient solution."),
    callout("note", "Who this paper is for",
      p("This paper is for a person who selects a first medium and does not know about substrates. "
        "It is also for a person who wants to know the cause of the results in a setup. The <a "
        "href='coco-crop-steering.html'>coco crop-steering paper</a> gives full information about "
        "the accurate control of coco, after you select it. You can use the two papers together.")),
  ]})

SECTIONS.append({"id": "key-terms", "kicker": "Terms", "title": "Definitions",
  "blocks": [
    p("Two values give the condition of a medium when it is wet. The other terms are about "
      "nutrients. It is not necessary to know all these terms at this time. It is sufficient to "
      "know the basic information about each term."),
    defterm("Water-holding capacity", "The part of the pore space that contains water after the "
            "medium drains. When the value is higher, the medium stays wet for a longer time."),
    defterm("Air-filled porosity", "The part of the pore space that contains air after the medium "
            "drains. Water and air fill the same pore space, and the total does not change. Thus "
            "when the quantity of water increases, the quantity of air decreases."),
    defterm("EC (electrical conductivity)", "The quantity of dissolved nutrient salt in the water, "
            "in milliSiemens per centimeter (mS/cm). A higher EC is a stronger feed with more salt."),
    defterm("pH", "A measurement of acidity on a scale of 0 to 14. The best pH range in the root "
            "zone of cannabis is approximately 5.5 to 6.5. For accurate control in soilless media, "
            "the range becomes smaller: 5.8 to 6.2." + _c("cockson-2019-cannabis-nutrient-disorders")),
    defterm("CEC (cation exchange capacity)", "Some media hold nutrient ions. They absorb the ions "
            "when the feed is strong and release them slowly when the feed is weak. The capacity of "
            "a medium to hold ions is its cation exchange capacity, in meq/100g." +
            _c("abad-2002-coir-dust-peat-substitute") + " When the CEC is high, the medium buffers "
            "your errors in the feed. But when the CEC is high, raw coco also removes some ions "
            "from the feed, and not other ions. Refer to the definition of Buffering below."),
    defterm("Buffering", "When you make an error in the dose, a buffered medium absorbs a part of "
            "the effect before the effect goes to the roots. Thus a buffered medium has a high "
            "tolerance for a feed that you mix incorrectly. An inert medium, for example rockwool, "
            "does not absorb the effect. Each change goes directly to the roots."),
    defterm("Dryback", "When you let the medium become dry between two irrigations, but not fully "
            "dry, the plant receives a weak stress signal. This signal causes the roots to go "
            "deeper in the medium. The quantity by which the medium dries between two irrigations "
            "is the dryback. Dryback is the primary control in crop steering. The <a "
            "href='coco-crop-steering.html'>coco paper</a> gives more information."),
    figure(L.zones("One total pore space, divided between water and air", 0, 100,
            [(0, 78, L.BLUL, "Water-holding"), (78, 100, L.GL, "Air")], unit="%",
            note="When the medium is saturated, the part for water increases. The roots get less oxygen."), 2,
      "The bar shows the total pore space, and the size of the bar does not change. When the "
      "quantity of water in the medium increases, the part for water becomes larger and the part "
      "for air becomes smaller. The roots use this air to get oxygen."),
  ]})

SECTIONS.append({"id": "water-vs-air", "kicker": "Primary information 1", "title": "Porosity: more water gives less air",
  "blocks": [
    p("Oxygen is as necessary for the roots as water. If a medium stays saturated, the roots do not "
      "get sufficient oxygen and root rot can occur. If a medium does not hold sufficient water, it "
      "becomes dry and causes stress in the plant. The five media are at different positions "
      "between these two conditions."),
    p("Rockwool has a total porosity of approximately 96%, but the air-filled porosity is only "
      "approximately 11%. The water-holding capacity is approximately 91%. Thus rockwool holds a "
      "large quantity of water and releases it easily." + _c("raviv-lieth-soilless-culture-afp") +
      " Peat has a total porosity of approximately 90 to 95% and a higher air-filled porosity of 18 "
      "to 25%." + _c("abad-2017-peat-use-horticulture") + "</p><p>Coco coir is different from the "
      "other media. Saturated coco coir can keep approximately 22% air, and saturated rockwool "
      "keeps approximately 10%. As a result, it is not easy to apply too much water to coco." +
      _c("abad-2002-coir-dust-peat-substitute") + " DWC is at the end of this range. The roots hang "
      "in nutrient water and get oxygen only from a pump."),
    figure(L.bars("Air-filled porosity when saturated",
            [("Coco coir", 22), ("Peat", 21), ("Rockwool", 11)], unit="%",
            note="More air at the roots when saturated gives less risk of too much water.", maxv=30), 3,
      "Coco keeps the most air when it is wet. Thus it is not easy to apply too much water to coco. "
      "Peat has more air than rockwool." + _c("abad-2002-coir-dust-peat-substitute") +
      _c("raviv-lieth-soilless-culture-afp")),
    table(["Medium", "Total porosity", "Air-filled porosity", "Water-holding capacity", "Air when saturated"], [
      ["Rockwool", "approximately 96%", "approximately 11%", "approximately 91%", "approximately 10%"],
      ["Coco coir", "approximately 94 to 96%", "high", "high", "approximately 22%"],
      ["Peat", "approximately 90 to 95%", "18 to 25%", "high", "moderate"],
    ], cls="compact", caption="After irrigation, when the rockwool drains, approximately 80% of the "
      "volume is solution, 15% is air and 5% is fiber." + _c("raviv-lieth-soilless-culture-afp")),
    callout("key", "The primary fact",
      p("When there is more water, there is less air. A medium that keeps air around the roots when "
        "it is wet has a high tolerance for too much water.")),
  ]})

SECTIONS.append({"id": "ec-buffering", "kicker": "Primary information 2", "title": "Buffering of nutrients in each substrate",
  "blocks": [
    p("An inert medium, for example rockwool, contains almost no nutrients. The EC of the medium is "
      "very low, and its pH is alkaline: approximately 8. Thus the feed that you apply is the feed "
      "that the roots get." + _c("raviv-lieth-soilless-culture-afp") + " The control of the feed is "
      "accurate, but the tolerance for an incorrect mix is low."),
    p("Coco is the opposite of rockwool. Coco has a high CEC of approximately 40 to 100 meq/100g, "
      "and this CEC buffers the changes in EC. But raw coco has exchange sites that hold potassium "
      "and sodium. When the feed water flows through the coco, the sites release potassium and "
      "sodium into the water. At the same time, they absorb calcium and magnesium from the water. "
      "Calcium and magnesium are the nutrients that are the most necessary for the plant, and the "
      "sites remove them before they go to the roots." + _c("abad-2002-coir-dust-peat-substitute") +
      "</p><p>The result is a deficiency of calcium and magnesium, unless you buffer the coco (soak "
      "it in a solution of calcium and magnesium) or you use pre-buffered coco." +
      _c("cockson-2019-cannabis-nutrient-disorders")),
    p("Living soil has the highest tolerance for errors of all the media. Microbes, organic matter "
      "and minerals keep the pH of the root zone at approximately 5.2 to 6.5 for hours to days. "
      "This effect occurs when the soil biology is in good condition. Many organic growers do not "
      "decrease the pH of the water for usual irrigations. But they do not use very alkaline water, "
      "and they monitor the pH if problems occur.</p><p>In DWC there is no buffer. The reservoir is "
      "the only protection from an error."),
    figure(L.zones("Scale of tolerance for errors in each medium", 0, 100,
            [(0, 30, L.REDL, "Inert: DWC, rockwool"), (30, 65, L.AMBL, "Buffered: coco"),
             (65, 100, L.GL, "Corrects its pH: living soil")], unit="",
            note="Left: no buffer. Right: soil corrects the pH. Coco buffers EC. Pre-buffering is necessary for calcium and magnesium."), 4,
      "The scale goes from no buffer (DWC and rockwool), to the EC buffering of coco, and then to "
      "living soil. Living soil corrects its pH after each irrigation."),
    callout("tip", "Select a medium for the work that you do",
      p("If you cannot make the feed correct each time, select a medium with a high tolerance for "
        "errors. When a medium gives more control, it gives less protection from your errors.")),
  ]})

SECTIONS.append({"id": "reuse-cost", "kicker": "Primary information 3", "title": "Number of uses, cost and effect on the environment",
  "blocks": [
    p("The media are very different in the number of crops that you can get from each medium. You "
      "can use rockwool again for a maximum of approximately three years, if you do the sanitation "
      "correctly. But much energy is necessary to make rockwool, and in some areas the regulations "
      "do not let you put it in a landfill. As a result, growers in parts of Europe and Japan use "
      "less rockwool." + _c("joseph-2024-rockwool-recovery-composting") + "</p><p>You can clean "
      "coco with water, buffer it again and use it again for some cycles. Then you can make compost "
      "from it for garden soil. But most coco moves a long distance to the grower."),
    p("You can use living soil again more times than all the other media. You add amendments to a "
      "bed of recycled organic living soil (ROLS) between two crops. The bed has no limit on the "
      "number of crops, and it becomes better with time.</p><p>DWC has no medium to discard. But "
      "you replace the nutrient reservoir frequently, and the pumps must have continuous "
      "electricity. Peat has a low cost and gives good results. But it becomes available again only "
      "after a very long time, and it has a carbon cost. As a result, many growers select coco." +
      _c("abad-2017-peat-use-horticulture")),
    table(["Medium", "Typical number of uses", "End of life", "Cost group", "Effect on the environment"], [
      ["Living soil", "No limit (ROLS, with amendments)", "The soil stays in the bed", "Low after the setup", "Lowest waste after the setup"],
      ["Coco coir", "Some cycles, with buffering again", "Becomes compost for soil", "Low to moderate", "Large effect on the environment, because the coco moves a long distance"],
      ["Peat", "Usually one cycle", "Can become compost", "Low", "Becomes available again slowly. Has a carbon cost."],
      ["Rockwool", "Approximately 3 years, with sanitation", "Some areas do not let you put it in a landfill", "Moderate", "Much energy to make"],
      ["DWC", "No medium", "No medium to discard", "Moderate (equipment and power)", "Frequent replacement of the reservoir, power for 24 hours each day, 7 days each week"],
    ], cls="compact", caption="No medium is the best in all columns. Living soil has the lowest "
      "waste, but it has the most work at the start."),
  ]})

SECTIONS.append({"id": "choose-by-stage", "kicker": "Make a decision", "title": "Substrate selection",
  "blocks": [
    p("Select a medium for the quantity of work that you accept. Do not select a medium because it "
      "gives the highest yield. The correct medium has tasks that you can continue to do each day."),
    figure(L.flow("Select by how much work you accept",
            [("Water only, easy setup", "living soil or soil mix with good-quality peat"),
             ("Feed and EC/pH checks", "pre-buffered coco, also the first step to crop steering"),
             ("Known correct settings", "rockwool, after the irrigation is stable"),
             ("You do constant checks", "DWC: highest possible yield, lowest tolerance for errors")],
            note="Start at the top. Select the next step only when you can do more tasks each day."), 5,
      "The steps go from the medium with the highest tolerance for errors to the medium with the "
      "most work each day. We recommend that most new growers start at the top two steps."),
    figure(L.bars("Tolerance for errors",
            [("Living soil", 9), ("Peat / soil mix", 8), ("Coco (pre-buffered)", 6),
             ("Rockwool", 4), ("DWC", 2)], unit="/10",
            note="How much tolerance for errors the medium gives a new grower. A higher value is safer.", maxv=10), 6,
      "Living soil and soil mixes of good quality have the highest tolerance for errors. DWC has "
      "the lowest tolerance. Thus DWC is not a good medium for a first crop."),
    callout("warn", "Do not use DWC for your first crop",
      p("DWC can cause very fast growth. But a warm reservoir or an air pump that stops can kill a "
        "plant in one day." + _c("frontiers-2026-do-pythium-strawberry-nft") +
        " First, use a medium with a higher tolerance for errors. Then you will know the basic "
        "procedures.")),
  ]})

SECTIONS.append({"id": "by-stage-setup", "kicker": "Do this", "title": "Setup and procedures for each substrate",
  "blocks": [
    p("Each medium has one step to prepare the medium. You must do this step. When you do it correctly, the other tasks are easy."),
    steps([
      ("Coco", "Clean the coco with water. If the coco is not pre-buffered, soak it for 8 to 24 hours in a solution of calcium and magnesium. Then apply feed in each irrigation, at pH 5.8 to 6.2 and a low EC. Apply small quantities of water frequently."),
      ("Rockwool", "Before you transplant, soak the cubes or slabs in a solution at pH approximately 5.5. Dry rockwool has a pH of approximately 8. After this, do not let the rockwool become fully dry."),
      ("Living soil", "Make the bed, or get a bed from a supplier. Let the bed cycle for some weeks. Then apply only water. Do not adjust the pH, unless symptoms occur."),
      ("DWC", "Keep the reservoir at 18 to 20 °C (65 to 68 °F), the dissolved oxygen at 7 to 9 mg/L, and the pH at 5.5 to 6.0. Operate the air pump 24 hours each day, 7 days each week."),
    ]),
    table(["Medium", "Step to prepare", "Procedure for feed and water", "pH target", "Do not ignore"], [
      ["Coco", "Clean with water. Buffer with calcium and magnesium.", "Apply feed in each irrigation, low EC", "5.8 to 6.2", "The pre-buffering step"],
      ["Rockwool", "Soak at pH approximately 5.5", "Frequent irrigation. Do not let the rockwool become dry.", "5.5 to 6.0", "Soak the rockwool before you put plants in it"],
      ["Living soil", "Cycle for some weeks", "Only water", "Do not adjust", "Do not adjust the pH of the water"],
      ["DWC", "Install the pump and the temperature control", "Recirculating reservoir", "5.5 to 6.0", "Operate the air pump 24 hours each day, 7 days each week"],
    ], cls="compact", caption="Most new growers do not do the step to prepare the medium. For each "
      "medium, this step is the difference between an easy start and a problem at the start." +
      _c("cockson-2019-cannabis-nutrient-disorders")),
    figure(L.zones("DWC reservoir: the zone of risk", 14, 28,
            [(14, 18, L.AMBL, "cool"), (18, 20, L.GL, "target 18–20 °C"),
             (20, 23, L.AMBL, "less oxygen headroom"), (23, 28, L.REDL, "warm-water risk")], unit="C",
            note="Temperature, dissolved oxygen, crop and pathogen have effects on each other. 23 °C is not a threshold for all diseases."), 7,
      "Warm water holds less dissolved oxygen. But the risk of Pythium does not have one threshold "
      "of 23 °C for all conditions. Select the range of operation for the crop and the system. Then "
      "monitor the temperature, the dissolved oxygen and the condition of the roots." +
      _c("le-pythium-hydroponic-epidemiology-review") + _c("frontiers-2026-do-pythium-strawberry-nft")),
  ]})

SECTIONS.append({"id": "pitfalls", "kicker": "When a problem occurs", "title": "Troubleshooting",
  "blocks": [
    p("The usual errors of a new grower are different for each medium. Most of these errors show symptoms of a different problem."),
    table(["Medium", "Usual error", "The effect that you see", "Correction"], [
      ["Coco", "No buffering step", "Deficiency of calcium and magnesium: orange-brown marks on the leaves, and leaves with a yellow color", "Do the pre-buffering of the coco. Add calcium and magnesium to the first feeds."],
      ["Rockwool", "You put the plants in dry cubes", "Pale plant with pH-8 lockout", "Soak at pH approximately 5.5 before you transplant"],
      ["Rockwool", "Too much water in a medium with a small quantity of air", "Slow growth. Wet roots that do not get sufficient oxygen.", "Apply a smaller number of shots. Let air go into the rockwool between the shots."],
      ["Living soil", "You adjust the pH of the water or add salts", "Growth stops, and the quantity of microbes decreases", "Apply only water. Do not adjust the pH."],
      ["DWC", "Warm water, or an air pump that stops", "The condition of the roots can become very bad in a short time", "Keep the temperature and the aeration in the range that is correct for your system. Monitor the dissolved oxygen."],
    ], cls="compact", caption="Growers read the problems in the coco and rockwool rows incorrectly "
      "as problems with the feed. The cause of these problems is an error in the step to prepare "
      "the medium." + _c("cockson-2019-cannabis-nutrient-disorders") +
      _c("le-pythium-hydroponic-epidemiology-review")),
    callout("danger", "DWC temperature and aeration",
      p("Monitor the temperature, the dissolved oxygen and the roots. Make sure that a second air "
        "pump is available. If the system cannot keep the correct range, add a chiller.</p><p>Warm "
        "water decreases the headroom of dissolved oxygen. An air pump that stops removes the "
        "aeration from the pump. Root rot does not occur because of only one of these conditions. "
        "The risk of disease also changes with the crop, the pathogen, the inoculum and the "
        "exposure time." + _c("le-pythium-hydroponic-epidemiology-review") +
        _c("frontiers-2026-do-pythium-strawberry-nft"))),
  ]})

SECTIONS.append({"id": "expectations", "kicker": "Possible results", "title": "Expected results and limitations",
  "blocks": [
    p("No medium does the work for you. In each medium, some tasks are not easy, and the media are "
      "different in the part of the procedure where these tasks occur. In living soil, most of the "
      "work is at the start, when you make the bed. After this, the bed operates with a very small "
      "quantity of work from you. In coco and rockwool, the work is the feed and the checks each "
      "day. In DWC, the risk is in a small number of parameters, and these parameters must stay in "
      "the correct range."),
    figure(L.line("Work each day and the maximum for yield and speed",
            [(0, 5), (1, 6), (2, 8), (3, 8), (4, 9)],
            ["Living soil", "Peat / soil", "Coco", "Rockwool", "DWC"],
            ylab="maximum", ymin=0, ymax=10,
            note="The work and the risk each day increase from left to right. Height is the maximum with correct settings."), 8,
      "The work and the risk increase from left to right. The maximum also increases, but only a "
      "careful grower gets it. A soil crop that you control correctly gives better results than a "
      "hydroponic crop that you control incorrectly, each time."),
    p("If the feed is accurate, inert media, for example coco and rockwool, can give a better yield "
      "and speed than soil. Tests that compare media show this result." +
      _c("xiong-2017-coir-rockwool-peat-tomato") + " The difference is small. In soilless cannabis, "
      "an accurate feed has a large effect on the results." + _c("bevan-2021-cannabis-npk-soilless") +
      " But this result is possible only when your environment and your irrigation are stable."),
    callout("key", "How to become a good grower",
      ol(["<strong>Select the problem that you can accept.</strong> Each medium causes a different problem. Select a medium when you can prevent the worst problem of that medium.",
          "<strong>Do one full crop cycle in a medium before you make a decision about it.</strong> You know a medium when you do one full crop in the medium. You do not know it when you only read about it.",
          "<strong>Change one parameter in the next crop.</strong> Do not change all the parameters at the same time, because you cannot know which change helped."])),
    p("First, do one full crop. Then make your procedures better. The <a "
      "href='coco-crop-steering.html'>coco crop-steering paper</a> continues from this paper when "
      "you want accurate control of a medium. The <a href='ph-management.html'>pH paper</a> gives "
      "information about the pH value. If the pH value is not correct, the feed does not go to the "
      "roots."),
  ]})
