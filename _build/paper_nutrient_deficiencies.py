# -*- coding: utf-8 -*-
"""Paper: nutrient deficiency and toxicity diagnosis (beginner)."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        stagecard, grid, card, chip, kv, steps)
import figs_lib as L

SLUG = "nutrient-deficiencies"
TITLE = "Diagnosis of nutrient deficiency and toxicity"
EYEBROW = "Plant health · Diagnosis"
SUB = ("This paper shows you how to read the symptoms on cannabis leaves from the position, color "
       "and shape. You will know how to find the difference between mobile and immobile nutrient "
       "deficiencies. You will also know how to find the difference between a deficiency, a "
       "toxicity and a pH lockout. Before you change your feed, you will know how to make sure of "
       "the diagnosis with a pH meter and an EC meter.")
META = [("leaf", "Plant health"), ("image", "12 figures"),
        ("quote", "7 sources"), ("clock", "~14 min to read")]
RELATED = ["ph-management", "nutrient-mixing-athena", "water-quality"]
REF_IDS = ["cockson-2019-nutrient-disorders-cannabis", "maillard-2015-leaf-nutrient-remobilization",
           "bevan-2021-npk-soilless-cannabis-flowering", "morad-2023-cannabis-magnesium-supply",
           "saloner-2020-cannabis-nitrogen-supply", "neilsen-1993-rhizosphere-ph-fe-mn-zn",
           "vyn-2007-ufl-nutrient-mobility-diagnosis", "hawkesford-2012-marschner-mineral-nutrition",
           "fageria-2001-nutrient-interactions-antagonism"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

SECTIONS.append({"id": "what-this-is", "kicker": "Start here", "title": "Purpose and scope",
  "blocks": [
    lead("A cannabis plant shows you the nutrients that it does not have in sufficient quantity, "
         "and the nutrients that it has too much of. It shows them through the color, the shape and "
         "the position of the symptoms on its leaves. This paper shows you how to read these "
         "signals with a method. Thus you find the cause, and you do not add fertilizer when it is "
         "not necessary."),
    p("The most important fact comes first: <strong>where</strong> a symptom shows on the plant is "
      "usually more important than the color of the symptom. A symptom shows on the old leaves at "
      "the bottom or on the new leaves at the top. If you use this one method, you decrease the "
      "list of possible causes to approximately half."),
    p("A nutrient is one of the approximately 17 chemical elements that a plant must absorb for "
      "growth" + _c("hawkesford-2012-marschner-mineral-nutrition") + ". The nutrients that you "
      "change most frequently are nitrogen (N), phosphorus (P) and potassium (K). Other nutrients "
      "are calcium (Ca), magnesium (Mg), sulfur (S), and small quantities of micronutrients, for "
      "example iron and zinc."),
    p("Three different problems can have almost the same symptoms on a leaf. A deficiency is the "
      "condition when the plant does not have a sufficient quantity of an element. A toxicity is "
      "the condition when the plant has too much of an element. A pH lockout is the condition when "
      "the element is in the water, but the roots cannot absorb it. The primary task is to find the "
      "difference between these problems."),
    figure(L.flow("How to read a leaf",
            [("Position", "bottom leaf or top leaf?"),
             ("Color pattern", "all the leaf, between veins, or edges?"),
             ("Shape", "flat, bent, with the claw, or tip burn?")],
            note="Three checks, in this sequence, for each leaf with a problem."), 1,
      "The plant shows its condition. Examine the position and the color of the leaf, and think of "
      "a possible cause. Then make sure of the cause with two measurements that have a low cost, "
      "before you make a change."),
    table(["Problem", "Definition", "The sign that identifies it"], [
      ["<strong>Deficiency</strong>", "The plant does not have a sufficient quantity of an element", "The green color decreases gradually. New growth has less green color."],
      ["<strong>Toxicity</strong>", "The plant has too much of an element or salt", "Dark green leaves with the claw, and tip burn"],
      ["<strong>pH lockout</strong>", "The element is in the water, but the roots cannot absorb it", "Symptoms of a deficiency when the feed is correct"],
    ], cls="compact", caption="A yellow leaf does not always show a deficiency. The same color can have three causes that are very different."),
    callout("warn", "A leaf with damage does not become green again",
      p("Examine the new growth, not the old leaves, to know if the plant is in good condition "
        "again. A leaf that has damage does not become green again after you correct the cause. "
        "When a leaf shows damage, the plant did not have a sufficient quantity of the nutrient for "
        "some days. A diagnosis from the symptoms is not fast.")),
  ]})

SECTIONS.append({"id": "key-terms", "kicker": "List of terms", "title": "Definitions",
  "blocks": [
    p("Before you do a diagnosis, you must know some terms that growers use frequently. The "
      "definitions are easy. Read this section one time, and go back to it when necessary."),
    defterm("Macronutrient", "An element that the plant uses in large quantities: N, P, K, Ca, Mg, S."),
    defterm("Micronutrient", "An element that the plant uses in small quantities: iron (Fe), "
            "manganese (Mn), zinc (Zn), copper (Cu), boron (B), molybdenum (Mo)."),
    defterm("Mobile nutrient", "A nutrient that the plant can remove from an old leaf and send to "
            "new growth when the supply is not sufficient. The nutrients are N, P, K and Mg."),
    defterm("Immobile nutrient", "A nutrient that stays in the position where the plant first puts "
            "it, and that the plant cannot move. The nutrients are Ca, S, Fe, Mn, Zn, B, Cu and Mo."),
    defterm("Chlorosis", "Chlorosis is the condition when a leaf becomes yellow because the green "
            "chlorophyll decreases. Interveinal chlorosis is chlorosis between the veins, while the "
            "veins stay green. This symptom is very frequent, and it is easy to identify."),
    defterm("Necrosis", "Necrosis is dead tissue that is brown and dry. The tissue does not become green again."),
    defterm("pH", "pH is a scale from 0 to 14. It shows if the water in the root zone is acid or "
            "alkaline. The pH has an effect on the nutrients that dissolve in the water and that "
            "the plant can absorb."),
    defterm("EC (electrical conductivity)", "EC is a measurement of the quantity of dissolved salt "
            "or fertilizer in the water. It shows the strength of the feed. PPM is the same "
            "measurement in different units."),
    defterm("Runoff", "Runoff is the water that drains from the bottom of the pot. You can measure "
            "the runoff to know the condition in the root zone."),
    figure(L.flow("Mobile or immobile: where to look",
            [("Mobile: N P K Mg", "symptoms on old leaves at the bottom first"),
             ("Immobile: Ca S Fe Mn Zn B Cu Mo", "symptoms on new top leaves first")],
            note="Mobility is the cause of the position of the problem."), 2,
      "Each usual element is a mobile nutrient or an immobile nutrient. As a result, the old leaves "
      "or the new leaves show the symptoms first." + _c("vyn-2007-ufl-nutrient-mobility-diagnosis")),
  ]})

SECTIONS.append({"id": "mobility-why-position", "kicker": "Primary fact 1", "title": "Leaf position and nutrient mobility",
  "blocks": [
    p("When a plant does not have a sufficient quantity of a mobile nutrient, the plant removes the "
      "element from its old leaves. Then the plant sends the element to the new growth at the top. "
      "The damage shows first at the bottom of the plant, and then at higher leaves. Immobile "
      "nutrients stay in the cell walls where the plant puts them, and the plant cannot remove "
      "them. Thus, when the plant does not have a sufficient quantity of an immobile nutrient, the "
      "new growth at the top shows the damage first. The old leaves stay in good condition." +
      _c("maillard-2015-leaf-nutrient-remobilization")),
    p("This one method decreases the list of possible causes to approximately half before you examine the color."),
    ul([
      "<strong>Chlorosis and then necrosis on the bottom leaves or the old leaves, that continue to the higher leaves,</strong> are a sign of a mobile nutrient. The nutrient is nitrogen, phosphorus, potassium or magnesium.",
      "<strong>New leaves at the top with a twisted shape, with less green color, or with bent tips</strong> are a sign of an immobile nutrient. The bottom leaves are in good condition. The nutrient is calcium, sulfur, iron, zinc, manganese or boron.",
      "<strong>Equal symptoms on all the plant, or damage on the two ends at the same time,</strong> are not a sign of one deficiency. They are a sign of a pH lockout, a root problem or stress from the environment.",
    ]),
    figure(L.flow("First step: find where the symptom shows first",
            [("Bottom: old leaves", "mobile nutrients: N P K Mg"),
             ("Top: new leaves", "immobile nutrients: Ca S Fe Zn Mn B"),
             ("All the plant, or the two ends", "pH lockout, or a problem of the environment")],
            note="Find the position first, then the color."), 3,
      "The symptoms of mobile nutrients show on the old leaves at the bottom. The symptoms of "
      "immobile nutrients show on the new growth at the top." +
      _c("cockson-2019-nutrient-disorders-cannabis")),
    callout("note", "Compare the symptoms with the growth stage",
      p("At the end of flowering, the plant moves the nitrogen to the buds. As a result, it is "
        "usual that the green color of the leaves decreases from the bottom up. The same symptom is "
        "usual at week 7, and it is a problem at week 2. Thus the week of the growth stage is "
        "necessary information before you make a change.")),
  ]})

SECTIONS.append({"id": "deficiency-vs-toxicity-vs-lockout", "kicker": "Primary fact 2", "title": "Deficiency, toxicity and pH lockout",
  "blocks": [
    p("The most frequent error of a new grower is this. The grower sees yellow leaves and thinks "
      "that the plant does not have sufficient nutrients. Then the grower adds more fertilizer. "
      "More fertilizer makes a toxicity or a lockout much worse. A toxicity shows as dark green "
      "leaves with the claw, and tip burn. This symptom is the opposite of leaves with less green "
      "color.</p><p>In a pH lockout, the nutrient is in the water at the roots, but the roots "
      "cannot absorb it. The cause is the pH, and the uptake stops when the nutrient is in the "
      "water. Only a correction of the pH lets the roots absorb the nutrient again."),
    ul([
      "<strong>Deficiency:</strong> The green color decreases gradually and the leaves become yellow. The new growth is smaller. After some time, the leaves fall from the plant. The plant has less and less green color.",
      "<strong>Toxicity (too much feed):</strong> The leaves become dark green and glossy. The tips have tip burn: they become brown and bend. If the nitrogen is very high, the leaf tips bend down. This shape is the claw." + _c("saloner-2020-cannabis-nitrogen-supply"),
      "<strong>pH lockout:</strong> The usual symptoms of a deficiency show, frequently of iron, or of calcium and magnesium. They show when the feed is correct, because the pH is not in the range where the roots can absorb the nutrients." + _c("neilsen-1993-rhizosphere-ph-fe-mn-zn"),
    ]),
    table(["Symptom that you see", "If it is a deficiency", "If it is a toxicity", "If it is a lockout", "First task"], [
      ["Yellow leaves", "The plant does not have a sufficient quantity of an element", "Too much salt. The roots do not get sufficient nutrients", "The pH stops the uptake", "Measure the pH before you apply feed"],
      ["Brown tips that are dry", "Not sufficient potassium (edges)", "Nutrient burn, or damage from salt", "Not sufficient micronutrients, frequently because of the pH", "Measure the EC of the runoff"],
      ["Dark green leaves with the claw", "Not frequent", "Too much nitrogen", "Not usual", "Decrease the feed strength"],
    ], cls="compact", caption="One symptom has three causes. For almost all of these problems, more fertilizer is not the correct first task."),
    figure(L.zones("The range from deficiency to toxicity", 0, 100,
            [(0, 33, L.AMBL, "deficiency: less green, leaves fall"),
             (33, 67, L.GL, "correct: good green color"),
             (67, 100, L.REDL, "toxicity: dark green, claw, tip burn")],
            unit="", note="The two ends are not good, with different symptoms."), 4,
      "The correct condition is the middle range. A deficiency is one failure mode: the leaves have "
      "less green color and they fall from the plant. A toxicity is the opposite failure mode: the "
      "leaves are dark green and have the claw. If you change the feed in the incorrect direction, "
      "the problem becomes worse."),
    callout("key", "Always measure the pH first",
      p("Before you apply a treatment for a deficiency, measure the pH. If the pH is not in the "
        "range, correct the pH. Then monitor the plant again for some days, before you think that "
        "the plant does not have a sufficient quantity of a nutrient. A pH that is not in the range "
        "causes lockout when the feed is correct." + _c("neilsen-1993-rhizosphere-ph-fe-mn-zn"))),
  ]})

SECTIONS.append({"id": "ph-windows", "kicker": "Primary fact 3", "title": "pH targets for each substrate",
  "blocks": [
    p("Each nutrient dissolves, and the plant can absorb it, only in one range of pH. If the pH in "
      "the root zone is not in the correct range, some nutrients do not stay dissolved at the same "
      "time. Then the plant does not have sufficient nutrients, but the substrate contains the "
      "nutrients. A correct pH prevents more deficiencies than a fertilizer corrects."),
    p("The correct target pH is different for each substrate. Soil has a buffer, and its target "
      "range is higher. Coco and hydroponics have no buffer. Thus you must adjust the pH with high "
      "precision."),
    figure(L.zones("Available nutrients and pH", 4.5, 8.0,
            [(5.5, 6.5, L.GL, "coco / hydro range"),
             (6.0, 7.0, L.BLUL, "soil range")],
            unit="", note="If the pH is not in these ranges, some nutrients do not stay dissolved."), 5,
      "The areas with color show the ranges where the roots can absorb the nutrients. The range for "
      "soil is higher by a small quantity, and it is wider. The ranges for coco and hydro are lower "
      "and have a smaller width." + _c("neilsen-1993-rhizosphere-ph-fe-mn-zn")),
    table(["Substrate", "Target pH", "Good range", "Frequency of measurement", "Buffering"], [
      ["Soil", "6.0-7.0", "6.2-6.8", "Each week", "High. Small errors do not cause a problem."],
      ["Coco", "5.5-6.5", "5.8-6.2", "With each feed", "None"],
      ["Hydro", "5.5-6.5", "5.8-6.2", "Each day", "None"],
    ], cls="compact", caption="Soil is the substrate that has the highest tolerance for pH errors. Coco and hydro have no buffer. Thus you must measure the pH much more frequently."),
    callout("tip", "The direction of pH drift shows the nutrients in lockout",
      ul([
        "<strong>More than approximately 6.5</strong> in coco or hydro: iron, manganese, zinc and boron do not stay dissolved. Chlorosis in the new growth is possible, with the symptoms of a micronutrient deficiency." + _c("neilsen-1993-rhizosphere-ph-fe-mn-zn"),
        "<strong>Less than approximately 5.5:</strong> calcium, magnesium and phosphorus are in lockout.",
        "A small change of the pH in the range (for example 5.8-6.2) gives each nutrient a time when the plant can absorb the maximum quantity. But keep the pH in the range for your substrate.",
      ], "tight")),
  ]})

SECTIONS.append({"id": "field-guide", "kicker": "Reference for use at the plant", "title": "Reference table of symptoms for each nutrient",
  "blocks": [
    p("Use the reference table at the plant. For each nutrient, the table gives the position on the "
      "leaf and the color or shape of the symptom. It also gives the one sign that shows the "
      "difference from problems with almost the same symptoms. Use the method of old leaves and new "
      "leaves, from the section before, to find the correct row quickly."),
    table(["Nutrient", "Mobile?", "Position", "Color or shape", "The sign that shows the difference"], [
      ["Nitrogen (N)", "Mobile", "Old leaves at the bottom", "All the leaf has less green color equally, then it becomes yellow and falls from the plant", "The most frequent deficiency. Too much N gives dark green leaves with the claw."],
      ["Phosphorus (P)", "Mobile", "Old leaves at the bottom", "Dark leaves, matt, with bronze, gray or purple patches", "Some cultivars are purple without a deficiency. Do not use only the stems to make a decision."],
      ["Potassium (K)", "Mobile", "Old leaves at the bottom", "Tip burn: the tips and the edges are brown and dry. The middle of the leaf stays green.", "The damage is at the edges. Nitrogen gives a fade of all the leaf."],
      ["Magnesium (Mg)", "Mobile", "Old leaves at the bottom", "Interveinal chlorosis. The veins stay green.", "Starts in the middle of the leaf, and goes slowly to the other parts of the leaf"],
      ["Calcium (Ca)", "Immobile", "New leaves at the top", "New growth with a twisted shape and brown patches", "A change of shape, not only of color"],
      ["Sulfur (S)", "Low mobility", "New leaves at the top", "New leaves with less green color, or yellow", "All of the new leaf has less green color. It is not interveinal chlorosis."],
      ["Iron (Fe)", "Immobile", "New leaves at the top", "Interveinal chlorosis with a very strong yellow color. The veins stay green.", "Very frequent when the pH is high. The symptom is on the top leaves."],
    ], cls="compact", caption="The table of leaf symptoms. First the position, then the color or shape, then the sign that shows the difference."),
    p("Two of these nutrients give almost the same symptoms, and these symptoms cause errors for "
      "new growers frequently. Magnesium and iron cause interveinal chlorosis with green veins." +
      _c("morad-2023-cannabis-magnesium-supply") + " The position shows the difference. Magnesium "
      "causes it on the old leaves at the bottom. Iron causes it on the new growth at the top."),
    figure(L.flow("Iron and magnesium: same symptom, opposite ends",
            [("Magnesium", "interveinal chlorosis, old leaf, bottom"),
             ("Iron", "interveinal chlorosis, new leaf, top")],
            note="The color pattern is the same. The position is the sign."), 6,
      "Magnesium deficiency is interveinal chlorosis on the old leaves. Iron deficiency is the same "
      "symptom on the new growth." + _c("morad-2023-cannabis-magnesium-supply") +
      _c("cockson-2019-nutrient-disorders-cannabis")),
    figure(L.bars("Quantity of each macronutrient that the leaves use (flowering)",
            [("Nitrogen", 100), ("Potassium", 95), ("Phosphorus", 45), ("Magnesium", 35)],
            unit="", note="Approximate values. The leaves use more potassium during flowering.", maxv=110), 7,
      "Nitrogen and potassium are the largest part of the uptake in flowering. Thus their "
      "deficiencies are the deficiencies that you will see most frequently." +
      _c("bevan-2021-npk-soilless-cannabis-flowering")),
  ]})

SECTIONS.append({"id": "confirm-and-fix", "kicker": "The steps", "title": "How to make sure of the diagnosis with pH, EC and runoff",
  "blocks": [
    p("A diagnosis is a loop, and not a decision without data. Examine the leaves. Then make sure "
      "of the cause with two meters that have a low cost, before you make a change. Measure the EC "
      "and the pH of the input and of the runoff from the pot. The measurements show if the root "
      "zone has a deficiency, a toxicity or a lockout."),
    steps([
      ("Step 1: measure the input pH and EC", "Make sure that the feed pH is correct for your substrate: 5.8-6.2 in coco or hydro, approximately 6.5 in soil. Make sure that the strength is correct for the growth stage."),
      ("Step 2: measure the runoff", "In coco, the runoff EC is usually approximately equal to the input EC. If the runoff EC is more than the feed EC by approximately 0.3&ndash;0.5 mS/cm (or more) for some days, the salt increases. The feed is too strong. Plants with less green color and a low runoff EC show that the feed is too weak."),
      ("Step 3: select the correction for the cause", "If there is a lockout or too much salt, flush the root zone with water that has the correct pH. Use water with no nutrients, or with a low feed strength. Do this until the runoff EC is usual, and then start the feed again. If the feed is too weak, increase the EC gradually. If one nutrient is not sufficient, correct the pH first. Then add that nutrient."),
      ("Step 4: monitor the new growth", "Examine the new leaves, and not the leaves with damage, for 5-10 days. The new leaves show if the plant is in good condition again. A leaf with damage does not become green again."),
    ]),
    figure(L.line("Target feed strength for each stage (coco / hydro)",
            [(0, 0.6), (1, 1.4), (2, 2.0), (3, 2.7), (4, 1.2)],
            ["seedling", "vegetative", "start of flowering", "peak of flowering", "flush"],
            ylab="EC", ymin=0, ymax=3.2, bands=[(1.0, 2.4, L.GL, "usual range")],
            note="The target increases. Use the trend, not one value. Compare it with your nutrient product."), 8,
      "The target EC increases from the seedling stage to the peak of flowering, and then it "
      "decreases for the end of the crop. Seedling: approximately 0.4-0.8 (approximately 250-400 "
      "PPM). Vegetative growth: 1.0-1.8. Flowering: 1.6-2.4, that increases to 2.4-3.0 at the end "
      "of flowering."),
    callout("note", "The runoff EC is an indicator of salt",
      p("The runoff EC in coco is usually approximately equal to the input EC. If the runoff EC is "
        "more than the feed EC by approximately 0.3&ndash;0.5 mS/cm for some days, the salt "
        "increases faster than the plant uses it. The correct task is a flush. More feed is not "
        "correct.")),
  ]})

SECTIONS.append({"id": "pitfalls", "kicker": "Troubleshooting", "title": "Troubleshooting",
  "blocks": [
    p("Most of the deficiencies that new growers find are pH lockout, too much water, or damage "
      "from light. These problems have the symptoms of a deficiency. If you know these problems, "
      "you do not add fertilizer to a plant that has too much water, damage from light or a "
      "lockout. When you are not sure, make only one change at a time and wait."),
    table(["Problem", "Same symptoms as", "Sign that shows it", "Examine this, not the feed"], [
      ["Too much water", "Nitrogen toxicity (leaves bend down, with the claw)", "The substrate is wet, and the plant uses water slowly", "The moisture of the soil, the drainage of the pot"],
      ["Root rot", "Many deficiencies at the same time", "Brown roots that are soft and wet, and an unwanted odor", "The condition of the roots, the oxygen at the roots"],
      ["Stress from light or heat", "Nutrient burn, or a deficiency", "Damage only on the top of the canopy, near the lamp", "The distance to the light, the canopy temperature"],
      ["pH lockout", "A deficiency of iron, or of calcium and magnesium", "Symptoms of a deficiency when the feed is correct", "The pH of the input and of the runoff"],
      ["Nutrient antagonism", "A deficiency of calcium and magnesium", "It occurs after too much of one element", "If you added too much K"],
    ], cls="compact", caption="The five problems. Each problem has the symptoms of a deficiency, and each problem becomes worse if you add feed."),
    p("Nutrient antagonism is the problem that is not easy to find. Too much of one element stops "
      "the uptake of a different element at the uptake sites of the root. Too much potassium "
      "decreases the uptake of calcium and magnesium. Thus a deficiency of calcium and magnesium "
      "can be a result of too much potassium. Because of this, too much of one element in the feed "
      "makes the problem worse." + _c("fageria-2001-nutrient-interactions-antagonism")),
    figure(L.flow("Sequence of checks before a deficiency diagnosis",
            [("pH check", "pH in range for substrate?"),
             ("EC / runoff check", "not sufficient or too much?"),
             ("Water / root check", "too much water or rot?"),
             ("Light / heat check", "damage at the top?"),
             ("Deficiency", "only then add nutrient")],
            note="Complete each check before you add fertilizer."), 9,
      "Too much water and stress from light give the same symptoms as nutrient problems. Thus a "
      "deficiency of one nutrient is the last diagnosis, not the first." +
      _c("fageria-2001-nutrient-interactions-antagonism")),
  ]})

SECTIONS.append({"id": "realistic-expectations", "kicker": "The limits of diagnosis", "title": "Expected results and limitations",
  "blocks": [
    p("A diagnosis gives you a list of possible causes with confidence. It is not as accurate as a "
      "laboratory test. The symptoms that you see are almost the same for some problems, and only a "
      "test of the tissue or of the substrate is accurate." +
      _c("cockson-2019-nutrient-disorders-cannabis") + " Leaves with damage do not become green "
      "again. Thus the correct result is new growth in good condition, not damaged leaves that "
      "become green again."),
    ul([
      "You will find the correct type of problem (mobile or immobile, and deficiency, toxicity or lockout) more frequently than the correct element. This information is usually sufficient to make a correct change.",
      "After you make a correct change, examine the new growth. The new growth is in good condition in a maximum of approximately 5-10 days. The leaves that have damage do not become green again. You can keep them on the plant or remove them.",
      "One correct procedure for the measurement of pH and EC prevents most nutrient problems. If you apply a correction for each element, the procedure is not correct.",
      "For crops with a high value, or for commercial crops, use a test of the leaf tissue or of the substrate. The test makes sure of the diagnosis when the symptoms can have more than one cause. Do not make a decision only from the symptoms that you see.",
    ]),
    figure(L.bars("Work to prevent a problem and to correct it",
            [("Stable pH / EC procedure", 25), ("Diagnosis and correction", 80), ("Less yield from damage", 60)],
            unit="", note="A small procedure has a much lower cost than the correction of problems.", maxv=100), 10,
      "The procedure with a low cost on the left prevents most of the tasks with a high cost on the right. A stable pH and EC procedure is much less work than the correction of a problem."),
    callout("key", "Prevent problems before the diagnosis",
      p("The visual method is a fast first check. It is not the last diagnosis. Most problems do "
        "not occur if the pH and the feed strength stay stable. Thus make the procedure first, and "
        "use the diagnosis as a second check.")),
    p("Next, make the two procedures correct, because they prevent most of these problems. Read the "
      "<a href='ph-management.html'>pH management</a> paper. Then read the <a "
      "href='nutrient-mixing-athena.html'>nutrient mixing</a> paper, to make the feed correct from "
      "the start."),
  ]})
