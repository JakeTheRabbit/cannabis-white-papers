# -*- coding: utf-8 -*-
"""Paper: vegetative management and timing, sizing veg by plant count, pot size and canopy plan."""
import json, os
from components import (p, lead, h, ul, ol, callout, defterm, table, figure, grid, card, chip, kv, steps)
import figs_lib as L

_FIGS = json.load(open(os.path.join(os.path.dirname(__file__), "figs_veg_management.json"), encoding="utf-8"))

SLUG = "veg-management"
TITLE = "The vegetative stage: make the frame, then do the flip"
EYEBROW = "Vegetative · Flip time"
SUB = ("This paper shows you how to calculate the correct number of days of the vegetative stage "
       "for your room. You use the plant count, the pot size and the canopy area. The paper also "
       "shows that, in the vegetative stage, you prevent almost all problems in week 3 of "
       "flowering, or you cause them. At the end, you have a sequence of decisions that gives the "
       "flip day from a specification and not from an estimate.")
META = [("leaf", "Vegetative"), ("image", "11 diagrams"),
        ("quote", "14 sources"), ("clock", "~14 min to read")]
RELATED = ["defoliation-training", "light-acclimation"]
REF_IDS = ["dang-2022-photoperiod-switch-meta",
           "schober-2024-veg-duration-density",
           "danziger-2022-planting-density",
           "backer-2019-yield-gap",
           "poorter-2012-pot-size",
           "gwe-flowering-stretch",
           "ilgm-stretch-guide",
           "rqs-topping-guide",
           "moher-2022-cannabis-vegetative-light-intensity-morphology",
           "jin-2019-indoor-review",
           "chandra2008-photo",
           "moher2023-photoperiod",
           "saloner-2020-cannabis-nitrogen-supply",
           "grodan-growguide-steering"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

# ---------------------------------------------------------------- 1 · start here
SECTIONS.append({"id": "intro", "kicker": "Start here", "title": "Purpose and scope",
  "blocks": [
    lead("Before the flip to 12/12, the vegetative stage makes four items. These four items give "
         "most of the possible harvest. The first two items are the number of bud sites and the "
         "quantity of leaf that gives energy to the bud sites. The other two items are the "
         "uniformity of the canopy and the capacity of the roots to supply the water and nutrients "
         "for the stretch. Flowering does not make these items. Flowering uses the items that the "
         "vegetative stage made."),
    p("The vegetative stage has no buds and no product to weigh. Thus new growers wait in the "
      "vegetative stage, and operators use the stage as a buffer. These two methods have a high "
      "cost.</p><p>The data of tests of indoor cultivation in other papers show that growers keep "
      "plants in the vegetative stage for approximately 2 to 26 weeks. The median is approximately "
      "30 days" + _c("dang-2022-photoperiod-switch-meta") + ". The wide range is not an error. "
      "Different rooms have different correct numbers of days. This paper shows you how to "
      "calculate the number for your room, and not to make an estimate."),
    p("The function of the vegetative stage is to make a <strong>frame</strong>. The frame is the "
      "roots, the stems, the nodes and the leaves of the plant. The frame must have the correct "
      "size to fill the canopy area of each plant. The plant count, the pot size and the target "
      "canopy give the size of the frame.</p><p>The size of the frame gives the number of days. All "
      "other decisions in this paper start from the frame. These decisions are the maximum flip "
      "height, the time of the topping, the climate, the feed and the condition of the root zone."),
    figure(L.flow("Made in the vegetative stage",
            [("Roots", "fill the pot and absorb water"),
             ("Nodes", "each node can be a bud site"),
             ("Leaves", "use light for growth"),
             ("Frame", "holds the flowers")],
            note="Flowering fills the frame. Without a frame, there is no space to fill."), 1,
      "The four parts that the vegetative stage makes. We recommend that each day of the vegetative "
      "stage makes one of the four parts. A day that does not make one of them gives no result."),
    callout("note", "Growers who use this paper",
      p("This paper is for all growers who did the flip because they thought that the size of the "
        "plants was sufficient. The growers can have a first tent or a room that has a license. Use "
        "this paper with <a href='defoliation-training.html'>defoliation and training</a>, which "
        "tells you how to cut and bend the plants. Also use <a href='light-acclimation.html'>light "
        "acclimation</a>, which tells you how to increase the PPFD. This paper tells you "
        "<em>when</em> to do the flip and <em>for how many days</em> to continue the vegetative "
        "stage.")),
  ]})

# ---------------------------------------------------------------- 2 · glossary
SECTIONS.append({"id": "key-terms", "kicker": "Glossary with easy definitions", "title": "Definitions",
  "blocks": [
    p("This paper uses eight terms many times. Read the terms one time. Each term occurs again in the sections that follow."),
    defterm("Flip", "The change of the light cycle from long days (usually 18 hours of light) to "
            "12/12. The change starts flowering in photoperiod cannabis. The flip day completes the "
            "vegetative stage."),
    defterm("Node / internode", "A node is the point on a stem where the leaves and the side "
            "branches attach. The internode is the part of the stem between two nodes, and it has "
            "no leaves. You measure the age of the plant and the topping height with the node "
            "count. A plant with short internodes is a compact plant and is strong."),
    defterm("Apical dominance", "The primary tip of the plant has most of the growth. Thus the "
            "primary tip becomes longer more quickly than the side branches. Topping and training "
            "stop this effect."),
    defterm("Topping / FIM", "Topping removes all of the primary growing tip. As a result, two new "
            "leaders (primary stems) start at the node below the removed tip. FIM cuts through most "
            "of the tip, but it does not remove all of the tip. FIM gives 3 to 4 leaders with lower "
            "uniformity."),
    defterm("Stretch", "The fast growth in height in the first 1 to 3 weeks after the flip. In this "
            "time, many cultivars increase in height to 1.5 to 2&times; the height at the flip "
            "(some cultivars to 3&times;). Then the growth in height stops."),
    defterm("Canopy", "The top layer of the crop that receives the light. You measure the canopy by "
            "three values: the area (m&sup2;), the number of gaps (a full canopy has a small number "
            "of gaps) and the uniformity (the tops have the same height)."),
    defterm("Root-bound", "A root system that has no more space in the container. The roots go "
            "around the wall of the pot, you must apply water to the pot frequently, and the growth "
            "stops. A root-bound plant cannot supply the water and nutrients for the stretch."),
    defterm("EC (electrical conductivity)", "The strength of the nutrient solution, in mS/cm. When "
            "the EC is higher, the solution has more fertilizer. In the vegetative stage, you "
            "increase the EC of the feed when the plant becomes larger."),
  ]})

# ---------------------------------------------------------------- 3 · the why
SECTIONS.append({"id": "what-veg-is-for", "kicker": "Cause and effect", "title": "Function of vegetative growth",
  "blocks": [
    p("Flowering does not make structure. The buds start at the nodes and branch tips that the "
      "plant has at the flip. The buds also start at the new nodes and tips that the stretch adds "
      "in the first weeks. Thus the size of the frame at the flip is the maximum limit for the "
      "quantity of flower that one plant can hold.</p><p>The data from a test show this. In this "
      "controlled test, the time of the vegetative stage was different for each group, from 1 to 4 "
      "weeks. Each week more in the vegetative stage added approximately <strong>3.3 g of dry "
      "flower for each plant</strong>, and the relation was almost linear" +
      _c("schober-2024-veg-duration-density") + "."),
    figure(L.bars("More flower from a longer vegetative stage",
            [("+1 week", 3.3), ("+2 weeks", 6.6), ("+3 weeks", 9.9)],
            unit=" g", maxv=12,
            note="More flower, compared with 1 week of vegetative stage. CBD cultivar, controlled environment, test of 1 to 4 weeks."), 2,
      "In the range of the test, the yield for each plant increases almost linearly with the number "
      "of days of the vegetative stage" + _c("schober-2024-veg-duration-density") +
      ". A larger frame holds more flower. But the yield for each plant is not the same as the "
      "yield for each room."),
    p("The number of days of the vegetative stage is a decision, because more days are not always "
      "better. <strong>The room gives yield for each m&sup2; (sq ft), and not for each "
      "plant.</strong> A full canopy of many small plants and a full canopy of a small number of "
      "large plants receive approximately the same quantity of light. In test data, a higher plant "
      "density gives a lower yield for each plant, but the yield for each area stays the same or "
      "increases" + _c("danziger-2022-planting-density") + ". In the data of many tests, the plant "
      "density is a weak indicator of the yield for each m&sup2; (ft&sup2;)" +
      _c("backer-2019-yield-gap") + ".</p><p>A meta-analysis of the time of the flip gives the same "
      "result. For the same area, a short vegetative stage gives the maximum quantity of flower in "
      "each unit of time. The cause is that many small frames fill the canopy more quickly" +
      _c("dang-2022-photoperiod-switch-meta") + "."),
    p("The number of days of the vegetative stage is not a control that you use to increase the "
      "yield. The number of days must <em>agree with the plant count</em>. Each plant must make a "
      "frame that fills its part of the canopy, not more and not less.</p><p>A small number of "
      "plants has a large canopy area for each plant and a long vegetative stage. A large number of "
      "plants has a small canopy area for each plant and a short vegetative stage. The canopy is "
      "the same in the two conditions. The number of crop cycles each year, the work for the plant "
      "count and the risk are different. The section on the cost of the vegetative stage gives more "
      "information."),
    callout("key", "The primary instruction",
      p("<strong>Keep the plants in the vegetative stage until the canopy area of each plant is "
        "full. The height of each plant must be the maximum flip height or less. Then do the "
        "flip.</strong> Each day of the vegetative stage that is too short gives an area of the "
        "canopy that is not full in flowering. Each day that is too long removes a fraction of a "
        "crop cycle.")),
  ]})

# ---------------------------------------------------------------- 4 · the core decision
SECTIONS.append({"id": "veg-duration", "kicker": "The primary decision", "title": "Days of the vegetative stage: plant count, pot size and canopy",
  "blocks": [
    p("Do the steps in this sequence. The number of days is the last result. Do not use the number of days as an input."),
    steps([
      ("Find the plant count",
       "Use the lowest of these limits. The limits are the license condition, the number of tags, "
       "your risk limit, and the number that you select. You usually cannot change this number "
       "easily in the room."),
      ("Measure the canopy", "Measure the area of the bench or tray that you will fill from wall to "
       "wall, in m&sup2; (ft&sup2;). Divide the area by the plant count. The result is the canopy "
       "area of each plant. Each plant must make a frame for this area."),
      ("Select a pot for the frame", "The root zone has a limit for the size of the plant. For a "
       "small canopy area, use a pot of 4–6 L (1.1–1.6 gal). For a canopy area of half a square "
       "meter, use 10–30 L (2.6–7.9 gal). For large plants with a full square meter, use 30 L or "
       "more (7.9 gal or more) or beds. The next section gives more information."),
      ("Select the training that makes the shape", "For a small canopy area, use plants with one cola "
       "and no topping. For a usual canopy area, do the topping one time and low-stress training "
       "(bend the stems to the side and attach them). For large plants, do the topping in stages. "
       "Refer to <a href='defoliation-training.html'>defoliation and training</a>."),
      ("Continue until the conditions are correct, then do the flip", "Do the flip when the canopy is approximately 80 to 90% "
       "full and the tops have the same height. The height of the plants must be the maximum flip "
       "height or less (refer to the section on the stretch). Use this condition of the canopy and "
       "not a date. The number of days until this condition <em>is</em> the number of days of your "
       "vegetative stage. Record this number for the next crop cycle."),
    ]),
    figure(_FIGS["decision"], 3,
      "The sequence of decisions. The plant count, the canopy area and the pot size are the inputs. "
      "The number of days of the vegetative stage is the output. The three types at the bottom are "
      "correct for most grow rooms."),
    table(["Type", "Plants for each m²", "Pot or block", "Usual vegetative stage", "Training"], [
      ["Sea of green (SOG)", "10-20+", "4-6 L", "approximately 7 to 14 days", "No training. One cola for each plant."],
      ["Usual topped plants", "2-4", "10-30 L", "approximately 14 to 28 days", "One topping, low-stress training and a net"],
      ["Large plants, with a plant count that has a limit", "approximately 1", "30 L or more, or beds", "35 days or more", "Topping in stages and a net"],
    ], cls="compact", caption="These values are approximate grower methods and not accurate values "
       "from a laboratory. The growth rate of the cultivar, the environment and the size of the "
       "transplant change the number of days. The tests of plant density and of the days of the "
       "vegetative stage in other papers agree with the structure of this relation" +
       _c("schober-2024-veg-duration-density") + _c("danziger-2022-planting-density") +
       "."),
    p("The meta-analysis also gives this information. A short vegetative stage gave more flower "
      "<em>biomass</em>. But the <em>concentration</em> of cannabinoids was at the maximum with a "
      "longer vegetative stage (approximately 6 to 7 weeks) in the data from all the tests" +
      _c("dang-2022-photoperiod-switch-meta") + ".</p><p>This signal is weak and it is different "
      "for different cultivars. Do not use it as a target. The genetics and the conditions of "
      "flowering give most of the potency. If a limit of the plant count causes a long vegetative "
      "stage, the data do not show that the quality is lower."),
  ]})

# ---------------------------------------------------------------- 5 · pot size
SECTIONS.append({"id": "pot-size", "kicker": "The size of the container gives the time of the vegetative stage", "title": "Pot size and days of the vegetative stage",
  "blocks": [
    p("The roots are the half of the frame that you cannot see, and they give the limit for all the "
      "growth. Each leaf uses light to make sugar by photosynthesis. Photosynthesis supplies the "
      "energy for each gram of new tissue that the plant makes. When the root zone has no more "
      "space, photosynthesis is the first function that becomes slower. The leaf stays green, but "
      "it makes less sugar.</p><p>A meta-analysis of 65 container tests showed that, on average, "
      "<strong>two times the volume of the root zone increased the plant biomass by approximately "
      "43%</strong>. Roots in a small volume decrease the growth mostly because the photosynthesis "
      "for each unit of leaf area decreases. The lower supply of water is not the only cause" +
      _c("poorter-2012-pot-size") + ". A root-bound plant has a lower growth rate, but the plant "
      "does not always show a sign of the problem."),
    figure(L.bars("Two times the volume: approximately +43% plant",
            [("Pot volume V", 100), ("Pot volume 2V", 143)],
            unit="%", maxv=160,
            note="Average of a meta-analysis of 65 tests of root volume. The direction is important. The number is approximate."), 4,
      "The volume of the container is a limit for growth. In a small pot, the limit occurs more "
      "quickly, mostly because photosynthesis decreases. More fertilizer cannot correct this problem" +
      _c("poorter-2012-pot-size") + "."),
    p("<strong>Each pot size gives a maximum time of vegetative growth</strong> before the plant "
      "becomes too large for the pot. After this time, you can transplant the plant again, or you "
      "can do the flip with a root-bound plant. A second transplant is correct if it is in your "
      "procedure. Do not do the flip with a root-bound plant. The times below are usual methods of "
      "growers. Cultivars with a high growth rate in warm rooms use the time more quickly:"),
    table(["Container", "Correct time in the vegetative stage", "For these plants"], [
      ["4-6 L pot / 4&Prime; block", "approximately 1 to 2 weeks", "SOG plants with one cola"],
      ["10-15 L pot / block on slab", "approximately 2 to 4 weeks", "Usual topped plants"],
      ["25-30 L pot", "approximately 4 to 6 weeks", "Large topped plants and large plants"],
      ["45 L or more / beds", "6 weeks or more", "Very large plants and frames of the size of a mother plant"],
    ], cls="compact", caption="These times are grower methods. The time ends when the roots touch "
       "the walls of the pot and you must apply water more frequently than your system does. Select "
       "a pot for the number of days of the vegetative stage. You can also decrease the number of "
       "days for the pot that you have."),
    callout("danger", "Do not do the flip with a root-bound plant",
      p("Transplant the plant to a larger pot if the roots go around the wall of the pot. Also "
        "transplant the plant if the pot dries in a small number of hours. Do this transplant one "
        "week <em>before</em> the flip, and not after the flip.</p><p>The stretch increases the "
        "quantity of water and nutrients that the plant uses to approximately two times in three "
        "weeks. A root-bound pot cannot supply this quantity. The plant then shows wilt between the "
        "irrigations. A deficiency occurs in weeks 2 to 3 of flowering. The buds are small and have "
        "low density. The plant can be in good condition at the flip.")),
  ]})

# ---------------------------------------------------------------- 6 · stretch
SECTIONS.append({"id": "stretch", "kicker": "Height", "title": "Calculate the flip height from the clearance of the ceiling",
  "blocks": [
    p("The most frequent error in the vegetative stage is not a stage that is too short. The error "
      "is a flip at a height that is too large. After the flip, most cultivars increase quickly in "
      "height for 1 to 3 weeks. The stretch almost stops at approximately day 21 of flowering" +
      _c("ilgm-stretch-guide") + ".</p><p>The stretch is very different for each cultivar. "
      "Cultivars with low stretch and mostly indica genetics can add approximately 50% to their "
      "height. Usual hybrids increase their height to approximately two times. Cultivars with high "
      "stretch and mostly sativa genetics can increase their height to two times or more" +
      _c("gwe-flowering-stretch") + _c("ilgm-stretch-guide") + ".</p><p>For most plants, the height "
      "after the stretch is approximately 1.5 to 2 times the flip height. This number is the "
      "stretch ratio of the cultivar. Calculate the stretch before the flip. After the flip, you "
      "cannot decrease the height of the plant, and the ceiling does not move."),
    p("There are three steps. First, subtract the fixture, the gap above it and the clearance to "
      "the canopy from the height of the room. In total, these values are usually approximately "
      "60–90 cm (24–35 in) for LED, and more for HPS. Then subtract the height of the pot and the "
      "bench, approximately 30 cm (12 in). The result is the <strong>available plant height "
      "H</strong>.</p><p>Divide H by the stretch ratio of your cultivar. The result is the "
      "<strong>maximum flip height</strong>. If you do not know the stretch ratio of the cultivar, "
      "use &times;2. Growers usually do the flip at half of the available height" +
      _c("gwe-flowering-stretch") + "."),
    figure(_FIGS["stretch"], 5,
      "The procedure starts at the ceiling. Subtract the height of the fixture, the gaps and the "
      "bench. The result is the available height H. H divided by the stretch ratio is the maximum "
      "flip height. A flip at 45 cm (18 in) is safe at &times;1.5 to 2.0. At &times;2.5, the plant "
      "touches the fixture."),
    table(["Cultivar type", "Usual stretch ratio", "Maximum flip height (H = 100 cm)"], [
      ["Low stretch, mostly indica", "&times;1.5", "A maximum of 65 cm"],
      ["Usual hybrid", "&times;2.0", "A maximum of 50 cm"],
      ["High stretch, mostly sativa", "&times;2.5 or more", "A maximum of 40 cm"],
    ], cls="compact", caption="The stretch ratios are approximate grower methods" +
       _c("gwe-flowering-stretch") + _c("ilgm-stretch-guide") + ". The ratio is very different for "
       "different cultivars. The spectrum, the temperature conditions and the topping that you did "
       "before also change the stretch. The number that you measured in the last crop cycle is more "
       "accurate than a table."),
    callout("tip", "Measure the stretch ratio of your plants",
      p("Attach a label to one plant of each cultivar. Measure the height of the plant on the flip "
        "day and again on day 21 of flowering. Divide the second height by the first height. Write "
        "the ratio in the record of the cultivar. With this ratio, you know the stretch for the "
        "next crop cycle. After two crop cycles, we recommend that you use the ratio of your plants "
        "and not a range from other papers.")),
  ]})

# ---------------------------------------------------------------- 7 · topping
SECTIONS.append({"id": "topping", "kicker": "Cut at the correct time", "title": "Topping and FIM: time and number of nodes",
  "blocks": [
    p("Topping changes the one tip that has apical dominance into two equal leaders and a wider "
      "frame with a more level top. The paper <a href='defoliation-training.html'>defoliation and "
      "training</a> gives all the information about the procedure and the cause. This paper is "
      "about the <em>time</em> of the topping and its cost in days, because each topping uses days "
      "of the vegetative stage."),
    p("Do the topping when the plant has <strong>4 to 6 nodes</strong>. A clone that has roots, or "
      "a seedling, usually has this number of nodes 3 to 4 weeks after the start of the vegetative "
      "stage. Cut above node 4 (between node 4 and node 5). If you cut higher, the topping has less "
      "effect. If you cut lower, you remove too much of the plant, and it is possible that the "
      "growth stops" + _c("rqs-topping-guide") + ".</p><p>Count the nodes from the bottom. Do not "
      "count the cotyledons (the first leaves, which have a smooth, circular shape). The recovery "
      "after the topping is <strong>7 to 14 days</strong>. During the recovery, the growth rate is "
      "low. Add the days of the recovery to the days of the vegetative stage" + _c("rqs-topping-guide") +
      "."),
    figure(_FIGS["topping"], 6,
      "Left: you cut above node 4 on a plant that has 4 to 6 nodes. Right: two equal leaders make "
      "new growth from the top node that stays. The recovery of 7 to 14 days uses days of the "
      "vegetative stage" + _c("rqs-topping-guide") + ". Add these days to the days of the "
      "vegetative stage before you do the topping."),
    p("<strong>FIM</strong> cuts through approximately &frac34; of the tip, from the top. It does "
      "not cut below the tip. FIM is faster, but you know the result less accurately than with "
      "topping. FIM gives 3 to 4 leaders and not 2 leaders.</p><p>The plant keeps more height, but "
      "the new growth has less uniformity. FIM is good for tents and for large plants. Most "
      "commercial rooms use topping, because it gives two leaders that are equal."),
    ol([
      "<strong>SOG:</strong> Do not do the topping. The primary function of SOG is one fast cola for each plant.",
      "<strong>Usual topped plants:</strong> Do the topping one time at 4 to 6 nodes. Do it a "
      "minimum of 10 to 14 days before the flip. Then the plant completes the recovery in the "
      "vegetative stage" + _c("rqs-topping-guide") + ".",
      "<strong>Large plants:</strong> Do the topping in stages. Do the topping, wait for the "
      "recovery of the leaders, then do the topping of the leaders. Each stage adds approximately 1 "
      "to 2 weeks to the vegetative stage. Three stages are more than one month of time for the "
      "structure.",
      "<strong>Do not</strong> do the topping during the stretch. The plant changes its structure "
      "for flowering, and the new growth is different on different parts of the plant. Also, you "
      "use days of recovery that you do not have.",
    ]),
    callout("warn", "The last day for topping",
      p("Subtract 10 to 14 days from the flip day. <strong>The result is the last day to do the "
        "topping, or to cut a large part of the plant.</strong> If you do the topping after this "
        "day, there are two possible results. The first result: you wait before you do the flip. "
        "The second result: you do the flip during the recovery.</p><p>If you wait, you have a "
        "cost. Make this decision carefully. If you do the flip during the recovery, the leaders "
        "have different sizes. The stretch increases the difference, and the uniformity of the "
        "canopy is low for all of flowering.")),
  ]})

# ---------------------------------------------------------------- 8 · canopy plan
SECTIONS.append({"id": "canopy-plan", "kicker": "One height, one light", "title": "Canopy in vegetative growth",
  "blocks": [
    p("The height of the light is one setting for the room: one fixture height for all the plants "
      "below it. The height of the light must agree with the plant that has the <em>largest</em> "
      "height. If you increase the height of the light to prevent damage to this plant, all the "
      "shorter plants receive light that is not sufficient. If you keep the light at a low height, "
      "this plant shows bleaching and heat stress. At the flip, the canopy can have no uniformity. "
      "Then plants near each other have a PPFD difference of more than 100 &micro;mol for all the "
      "flowering cycle."),
    figure(_FIGS["uniformity"], 7,
      "One plant with a large height increases the height of the fixture. As a result, the PPFD map "
      "of the room has large differences. A canopy with equal height from the vegetative stage puts "
      "all the tops in the same range of PPFD. You make the uniformity before the flip and not "
      "after the flip."),
    p("Uniformity is also important for commercial rooms, and not only for the growth of the plant. "
      "A canopy with a higher density and a lower uniformity increases the variation of the "
      "cannabinoid content. The variation occurs between plants and in one plant, and you can "
      "measure it" + _c("danziger-2022-planting-density") + ". This variation is a risk to the "
      "grade when laboratory tests are necessary. To make the height of the canopy equal in the "
      "vegetative stage, use these easy methods in this sequence:"),
    ul([
      "<strong>Start with the same height.</strong> Use one cultivar in each light zone and clones "
      "from one group. The difference between the times when the clones made roots is a small "
      "number of days. Put plants of the same size together at the transplant. A plant that is 30% "
      "smaller than the group does not become the same size as the group. Remove this plant or put "
      "it on a different bench.",
      "<strong>Position:</strong> Put the cultivars with the largest height at the edges and the "
      "corners, where the PPFD decreases. Put the short plants in the middle, below the area with "
      "the highest PPFD.",
      "<strong>Bend the plants down and do not cut them.</strong> From the middle of the vegetative "
      "stage, bend the leaders with the largest height to the side. Attach them (low-stress "
      "training). Thus the short plants near them fill the gap, and you do not use recovery time.",
      "<strong>Install the net before the stretch.</strong> Put the trellis net above the canopy in "
      "the last part of the vegetative stage, or at the flip. All the plants are short at this "
      "time. In weeks 1 to 3 of flowering, put the tops through the openings of the net.",
    ]),
    callout("note", "A net is for the stretch, not for a correction",
      p("In week 3 of flowering, the plants have resin and many branches that touch each other. If "
        "you install a net at this time, the net breaks branches and the work uses many hours. The "
        "net must hold the plants while the stretch occurs. If you do not install the net on the "
        "flip day, you usually do not install it.")),
  ]})

# ---------------------------------------------------------------- 9 · environment
SECTIONS.append({"id": "environment", "kicker": "Targets with sources", "title": "Vegetative climate targets",
  "blocks": [
    p("In the vegetative stage, the room has a higher temperature, a higher humidity and less "
      "stress to the plant than in flowering. The differences are small. The cause is that the "
      "plant is almost all leaf, and the roots are not deep in the first stage. The plant makes "
      "tissue, and the ripening of the tissue does not start.</p><p>The table gives the ranges that "
      "you can use. The two figures below give more information about the temperature and the "
      "PPFD.</p><p>Read this information about the row for VPD before the numbers. At a given "
      "temperature, air can contain only a maximum quantity of water vapor. The difference between "
      "the vapor in the air and this maximum shows how much more vapor the air can receive at this "
      "time. This difference is the vapor pressure deficit (VPD), in kPa.</p><p>When the VPD "
      "increases, the air removes water from the leaf more quickly. The target VPD is approximately "
      "0.8 kPa at the start of the vegetative stage, and it increases to 1.0–1.3 kPa before the "
      "flip. The table below gives more information."),
    table(["Condition", "Start of the vegetative stage (new transplant)", "End of the vegetative stage (before the flip)", "Source"], [
      ["Air temperature, lights on", "25-28 &deg;C", "25-30 &deg;C",
       "The photosynthesis of cannabis leaves is at the maximum at approximately 25-30 &deg;C" +
       _c("chandra2008-photo") + _c("jin-2019-indoor-review")],
      ["Relative humidity", "65-75%", "55-65%",
       "The reference gives a target of approximately 75% for plants in the first stage. The target then decreases to approximately 55 to 60%" + _c("jin-2019-indoor-review")],
      ["VPD", "approximately 0.8 kPa", "1.0-1.3 kPa",
       "The same reference gives these values as vapor pressure deficit" + _c("jin-2019-indoor-review")],
      ["PPFD", "300-600 &micro;mol/m&sup2;/s, with a ramp", "600-900 &micro;mol/m&sup2;/s",
       "A test of 21 days of vegetative growth, with values from 135 to 1430 &micro;mol" + _c("moher-2022-cannabis-vegetative-light-intensity-morphology")],
      ["Photoperiod", "18/6 (grower method)", "18/6 until the flip day",
       "Long days keep the plants in the vegetative stage. Cultivars can start flowering at photoperiods of a maximum of approximately 14 h" + _c("moher2023-photoperiod")],
      ["CO2", "The usual air of the room (approximately 400-600 ppm) is sufficient", "700 to 800 ppm or more has an effect only with a high PPFD",
       "Photosynthesis increases when the CO2 increases to approximately 750 ppm or more, at high light" + _c("chandra2008-photo")],
    ], cls="compact", caption="These ranges are for photoperiod cultivars in soilless media. The "
       "numbers without a citation are approximate grower methods. Use all the numbers as start "
       "points, and make sure that they are correct for the canopy in your room."),
    figure(L.zones("Growth at each air temperature in the vegetative stage", 16, 36,
            [(16, 20, L.AMBL, "slow"), (20, 25, L.GXL, "good"), (25, 30, L.GL, "best"),
             (30, 32, L.AMBL, "edge"), (32, 36, L.REDL, "stress")],
            unit="&deg;C",
            note="Leaf photosynthesis is at the maximum at approximately 25-30 &deg;C. A hot room also makes the internodes longer, and you want a short frame."), 8,
      "The temperature zones for the vegetative stage" + _c("chandra2008-photo") +
      ". A room with a lower temperature is not safer. It is only slower, and a slow vegetative "
      "stage uses more days."),
    p("<strong>The light in the vegetative stage changes the shape of the plant and not only the "
      "speed of growth.</strong> In the test of 21 days, a higher PPFD made the plants shorter, "
      "with thicker stems and shorter internodes. The change was almost linear.</p><p>At "
      "approximately 600 &micro;mol, the frame was more open and had better airflow. At "
      "approximately 900 &micro;mol, the transplants were short and strong. There were no signs of "
      "light stress, also at the top of the range of the test" +
      _c("moher-2022-cannabis-vegetative-light-intensity-morphology") + ". Operators of commercial "
      "rooms want this type of transplant.</p><p>Low light (150-300 &micro;mol) in the vegetative "
      "stage is the cause of long and weak plants at the flip in tents. Increase the intensity in "
      "steps during some days, and not in one step. The paper <a "
      "href='light-acclimation.html'>light acclimation</a> gives the information about the ramp."),
    figure(L.bars("PPFD for targets",
            [("New transplant", 300), ("Open, with airflow", 600), ("Short and strong", 900)],
            unit="", maxv=1000,
            note="&micro;mol/m&sup2;/s at the canopy, 18 h photoperiod. Increase in steps during some days (refer to light acclimation)."), 9,
      "The PPFD in the vegetative stage controls the shape: more light gives shorter internodes and "
      "thicker stems" + _c("moher-2022-cannabis-vegetative-light-intensity-morphology") +
      "."),
    callout("warn", "Monitor the limit of the photoperiod",
      p("Keep the photoperiod of the vegetative stage at 16 to 18 h. Add the light cycle to your "
        "checks for each day. A cultivar can start flowering at a photoperiod that is longer than "
        "12 hours. In a test of ten cultivars, all the cultivars started flowering at photoperiods "
        "of a maximum of 14 h" + _c("moher2023-photoperiod") + ".</p><p>The days in a vegetative "
        "room can become shorter. Examples are a timer that does not operate correctly and a light "
        "controller with an incorrect setting. A long period with no electricity is also an "
        "example. In this condition, the plants that you want to keep in the vegetative stage can "
        "start the flip.")),
  ]})

# ---------------------------------------------------------------- 10 · nutrition
SECTIONS.append({"id": "nutrition", "kicker": "Feed for growth", "title": "Vegetative nutrition",
  "blocks": [
    p("In the vegetative stage, the plant makes mostly protein and chlorophyll, and the two contain "
      "much nitrogen. Thus each feed for the vegetative stage has a higher proportion of nitrogen "
      "(N) than the feed for flowering.</p><p>The data show the relation between the dose of N and "
      "the growth accurately. In tests of fertigation on medical cannabis, the vegetative growth "
      "was at the maximum at approximately <strong>160 mg/L N</strong>. Plants at 30 mg/L had "
      "nitrogen deficiency that you can see, and plants at 320 mg/L had less growth than the maximum" +
      _c("saloner-2020-cannabis-nitrogen-supply") + ". More nitrogen does not give more growth. The "
      "curve has a peak."),
    p("In coco or rockwool with drain to waste, the primary control is the feed EC. Increase the "
      "feed EC when the plant size increases. The values below are approximate grower methods. Do a "
      "check of the values with the runoff EC and the color of the leaves:"),
    table(["Stage", "Feed EC (mS/cm)", "Task"], [
      ["New transplant, week 1", "approximately 1.5 to 1.8", "A careful start, while the roots go into the new volume"],
      ["Middle of the vegetative stage", "approximately 2.0 to 2.4", "Full feed with a high proportion of N. The plant makes new tissue at the maximum rate."],
      ["Last week of the vegetative stage, until the flip", "approximately 2.4 to 3.0", "Increase the EC. The plant has reserves when the stretch starts."],
    ], cls="compact", caption="These values are a grower method for soilless systems with drain to "
       "waste. They agree with the information of the manufacturer of stone wool" +
       _c("grodan-growguide-steering") + ". The numbers are different for different products and "
       "water. Monitor the trend of the runoff EC. If the runoff EC increases quickly, the feed is "
       "stronger than the quantity that the plant uses."),
    p("Two methods do most of the work. <strong>Use the color and not the date.</strong> In the "
      "vegetative stage, the plant must have an equal medium-green color. If the bottom leaves are "
      "light green or yellow, the supply of N is less than the growth rate. If the leaves are "
      "blue-green and almost black, with claw tips, the supply of N is more than the growth "
      "rate.</p><p><strong>Do not decrease the N before the flip.</strong> The stretch uses mostly "
      "nitrogen that the plant moves from the tissue of the vegetative stage. Thus a plant with "
      "light green or yellow leaves at the start of 12/12 has a strong fade by week 3 of flowering. "
      "The fade goes from the bottom to the top."),
    callout("warn", "Light green leaves at the flip cause a problem in flowering",
      p("Correct light green leaves in the vegetative stage. At the flip day, the plant then has "
        "most of the nitrogen for the stretch. Growers frequently think that the nutrients for "
        "flowering cause yellow bottom leaves in week 3 of flowering. The cause is usually in the "
        "time two weeks before. The plant had feed that was not sufficient, a root zone that was "
        "too small, or light stress. The plant then started the stretch with no nitrogen reserve.")),
  ]})

# ---------------------------------------------------------------- 11 · root zone
SECTIONS.append({"id": "rootzone", "kicker": "Root zone before the flip", "title": "Growth of the roots before flowering",
  "blocks": [
    p("The fastest method to stop the growth for one week is to apply too much water to a new "
      "transplant. A new transplant has a small root ball in a large volume of wet substrate. If "
      "the volume stays saturated, the roots have no cause to go into the volume, and the volume "
      "has no oxygen for them.</p><p>The manufacturer of stone wool gives information for the "
      "vegetative stage. Apply small, frequent shots of approximately 3% of the substrate volume, "
      "with a small runoff fraction of 5 to 15%. The information also shows that drybacks must not "
      "be large. A water content of less than approximately 25 to 30% in blocks stops new roots" +
      _c("grodan-growguide-steering") + ". The substrate must have sufficient water for the roots. "
      "The substrate must also dry, and then the roots continue to go in the direction of the water."),
    p("The root zone, and not the date, shows the result of the vegetative stage on the flip day. "
      "The night dryback is the quantity by which the substrate moisture decreases from the last "
      "irrigation shot to the start of the next light period. The roots continue to absorb water "
      "during the night. Thus the weight of the pot is lower at the start of the next light period, "
      "and you can measure the difference.</p><p>When the night dryback is the same on two or three "
      "nights in sequence, the roots are in good condition and go into the substrate. Three checks "
      "show that the roots are correct for the flip. First, you can see roots at the walls of the "
      "container and at the drain holes (or on the face of the slab). Second, the night dryback is "
      "<em>stable</em>: the sensor shows the same decrease each day at the start of the light "
      "period. Third, the plant uses more water each day.</p><p>A root system in good condition "
      "that goes into the substrate supplies the water and nutrients for the stretch. In the "
      "stretch, the quantity of water and nutrients that the plant uses increases to approximately "
      "two times in three weeks. If you do the flip before the roots are in this condition, the "
      "stretch stops. If you wait for a long time, the plant becomes root-bound (refer to the "
      "section on pot size)."),
    figure(_FIGS["timeline"], 10,
      "An approximate example of 18 days from a clone to the flip, for a topped plant in 10–11 L "
      "(2.6–2.9 gal). The sequence is the growth of the roots, the topping, the recovery, the "
      "uniformity of the canopy, and then the pre-flip check. SOG makes the same sequence shorter, "
      "in approximately 7–10 days. Large plants make the sequence longer, in 5 to 8 weeks. The "
      "pre-flip check gives the day of the flip. A date that you select before the check gives only "
      "an estimate."),
    steps([
      ("Roots at the walls", "Make sure that white roots are at the walls and the drain holes of "
       "the pot. For a block, make sure that white roots are around the face of the block. Make "
       "sure that the plant uses more water each day."),
      ("Height less than the limit", "Make sure that the top with the largest height is at the maximum "
       "flip height or lower (the available height divided by the stretch ratio)."),
      ("Uniformity and a full canopy", "Make sure that the height difference between the tops is "
       "approximately 10 cm (4 in) or less. Make sure that approximately 80 to 90% of the canopy "
       "area of each plant is full. Install the net."),
      ("Recovery after the topping", "Make sure that the last topping was a minimum of 10 to 14 days before the "
       "flip. Make sure that the leaders are equal. Make sure that you do not cut a large part of "
       "the plant when the stretch starts" + _c("rqs-topping-guide") + "."),
      ("Feed and green color", "Make sure that there is no deficiency. Use the feed EC for the end of the "
       "vegetative stage. Make sure that the plant has an equal medium-green color and has N "
       "reserves for the stretch."),
    ]),
    callout("key", "The pre-flip check",
      p("Do the flip only when all five conditions are correct. If one condition is not correct, "
        "correct it first. If you wait two days to complete the growth of the roots, you use two "
        "days. If you do the flip when one condition is not correct, the result is a weak flowering "
        "cycle.")),
  ]})

# ---------------------------------------------------------------- 12 · economics
SECTIONS.append({"id": "economics", "kicker": "Days of the vegetative stage and the cost of the room", "title": "Cost of the vegetative stage",
  "blocks": [
    p("The genetics gives the time of flowering. It is approximately 56 to 63 days, and you cannot "
      "change it easily. Thus the number of days of the vegetative stage is <em>the</em> time that "
      "you control. It changes three quantities: " + chip("crop cycles each year") +
      ", " + chip("plants for each gram") + " and " + chip("risk for each plant") +
      "."),
    figure(L.bars("Crop cycles each year and vegetative days",
            [("10 days", 5.0), ("21 days", 4.3), ("35 days", 3.7)],
            unit="", maxv=6,
            note="Example: 365 / (vegetative days + 56 days of flowering + 7 days between crops). A different flowering time changes all bars."), 11,
      "A longer vegetative stage decreases the number of crop cycles. For 35 days of vegetative "
      "stage and not 10 days in the same room, the room has approximately one crop cycle less each "
      "year. This cost gives larger plants and a smaller number of plants. The result can be good "
      "or bad for you. If the plant count has a limit, the result is good. If time has a limit, the "
      "result is not good."),
    p("<strong>If the plant count has a limit, the number of days of the vegetative stage is the "
      "control that you can use.</strong> A license condition, an agreement or your risk model can "
      "limit the number of plants. In this condition, the yield for each plant is the important "
      "value. The yield for each plant increases with the days of the vegetative stage and with the "
      "size of the frame" + _c("schober-2024-veg-duration-density") + ".</p><p>A smaller number of "
      "large plants also decreases the cost of operation. This condition gives a smaller number of "
      "tags and records for each gram in a traceability system. It gives a smaller number of "
      "transplants and a smaller number of plants to examine for IPM. It also gives a lower risk of "
      "variation between plants than a canopy with a high density" +
      _c("danziger-2022-planting-density") + ".</p><p>If the plant count has no limit, time is the "
      "limit. Then use a short vegetative stage, a high density and more crop cycles" +
      _c("dang-2022-photoperiod-switch-meta") + "."),
    p("<strong>The days of the vegetative stage must also agree with the size of your vegetative "
      "room.</strong> When the production is stable, a flowering room gets a new group of plants "
      "each N weeks. The vegetative area must hold each group for all the days of the vegetative "
      "stage. When the vegetative stage is longer, more groups are on the vegetative benches at the "
      "same time.</p><p>A long vegetative stage gives three results. The vegetative room is larger, "
      "and it has more light. The plants have more weeks of risk from a large number of pests in "
      "the vegetative room. The cost for each m&sup2; (ft&sup2;) is low, but it is not zero."),
    kv([
      ("Flowering period", "56 to 63 days. The genetics gives this period, and you cannot change it."),
      ("Vegetative stage of approximately 10 days", "Approximately 5 crop cycles each year. The most plants and tags. The lowest risk for each plant."),
      ("Vegetative stage of approximately 21 days", "Approximately 4.3 crop cycles each year. This vegetative stage is the usual balance in commercial rooms."),
      ("Vegetative stage of 35 days or more", "Approximately 3.7 crop cycles each year. The smallest number of plants for each gram. This vegetative stage is the method for a plant count that has a limit."),
    ]),
    callout("note", "Two methods: time or frame",
      p("When the plant count has no limit, the method is time: a short vegetative stage, a high "
        "density and the maximum number of crop cycles. When the plant count has a limit, the "
        "method is frame: a long vegetative stage, large pots and large plants. The worst condition "
        "is the middle: plants of medium size and medium density that growers select without a "
        "check. This condition is not the best for time, and it is not the best for frame.")),
  ]})

# ---------------------------------------------------------------- 13 · mistakes
SECTIONS.append({"id": "mistakes", "kicker": "Errors in the vegetative stage", "title": "Frequent errors in vegetative growth",
  "blocks": [
    p("Each of these errors has a low cost to prevent in the vegetative stage, and a high cost to "
      "find in flowering. Most rooms with problems in week 3 of flowering had one of these errors "
      "one month before."),
    grid([
      card("The flip of a root-bound plant",
        p("The pot dries in a small number of hours, the roots go around the walls, and the growth "
          "stops. The grower does the flip with these signs. The stretch uses a quantity of water "
          "and nutrients that is more than the root system can supply. Then the plant shows wilt, a "
          "fade in the first stage of flowering, and buds with low density. "
          "<strong>Correction:</strong> Select a pot for the number of days of the vegetative "
          "stage. If you are not sure, transplant the plant to a larger pot and add one week "
          "<em>before</em> the flip."), tag="root zone"),
      card("A flip at a height that is too large",
        p("After the stretch, the height of the plant is more than the available height. The tops "
          "touch the fixture and show bleaching and heat damage. If you decrease the light to "
          "prevent damage to the tops, the other plants in the room receive light that is not "
          "sufficient. <strong>Correction:</strong> The maximum flip height is the available height "
          "divided by the stretch ratio. Apply this limit on the flip day for all plants."), tag="height"),
      card("A canopy with no uniformity at the flip",
        p("One cultivar with a large height can increase the height of the fixture. Plants that "
          "stayed too long in the vegetative stage can have the same effect. The other plants "
          "receive light that is not sufficient for nine weeks.</p><p><strong>Correction:</strong> "
          "Make the height of the canopy equal in the vegetative stage. Use clones of the same "
          "size. Bend the plants that have the largest height down, and put them at the edges. "
          "Remove the smallest plants. Install the net at the flip."),
        tag="uniformity"),
      card("Topping after the last day",
        p("If you cut the plant ten days before the flip, the flip is during the recovery. The "
          "leaders have different sizes, and the stretch increases the difference. The canopy then "
          "has a low uniformity. <strong>Correction:</strong> Do the last topping 10 to 14 days "
          "before the flip. Write this date in your record on the day that you do the topping."), tag="time"),
      card("Too much water at a new transplant",
        p("The grower keeps a large new pot saturated to help the plant. The roots do not have "
          "sufficient oxygen, they do not go into the substrate, fungus gnats occur, and the growth "
          "stops for one week. <strong>Correction:</strong> Apply small, frequent shots with a "
          "small runoff. Let the roots go to the water in the new volume."),
        tag="irrigation"),
      card("A vegetative stage with no target",
        p("The grower adds 'one more week' with no data, no canopy specification and no pre-flip "
          "check. Each week that is not in the procedure removes a fraction of a crop cycle. This "
          "method has the highest cost in the room. <strong>Correction:</strong> Before the "
          "transplant, write the specification: the plant count, the canopy area of each plant and "
          "the maximum height. Do the flip when the pre-flip check is correct."),
        tag="target"),
    ], cols=2),
  ]})

# ---------------------------------------------------------------- 14 · troubleshooting
SECTIONS.append({"id": "troubleshooting", "kicker": "Examine and correct", "title": "Troubleshooting",
  "blocks": [
    p("If you compare the plant with the specification, you see the first signs of a problem in the "
      "vegetative stage. The frequent problems are in the table below:"),
    table(["Sign", "Possible cause", "Correction"], [
      ["No growth of the transplant for one week or more", "Too much water at the start. The roots do not go into the substrate.",
       "Decrease the shot sizes. Let air go into the substrate between the shots. Do a check of the drainage" + _c("grodan-growguide-steering")],
      ["Long internodes and weak stems", "The PPFD is too low for the frame that you want",
       "Increase the light in the vegetative stage in steps to approximately 600–900 &micro;mol" +
       _c("moher-2022-cannabis-vegetative-light-intensity-morphology") + ". Add airflow to make the "
       "stems strong."],
      ["Light green color on all leaves, with the bottom leaves first", "The supply of nitrogen is less than the growth rate",
       "Increase the feed EC or the N to the value for maximum growth in the vegetative stage" + _c("saloner-2020-cannabis-nitrogen-supply") + ". Examine the plant again in 4 to 5 days."],
      ["Blue-green color, almost black, with claw tips", "The supply of nitrogen is more than the growth rate",
       "Decrease the feed EC. Keep the ratio with a high proportion of N, but decrease the dose."],
      ["Pistils or flowers in the vegetative room", "A fault in the photoperiod: a timer, a controller or a light leak, with a day of 14 h or less",
       "Do an audit of the light cycle and of the procedure for the door" + _c("moher2023-photoperiod") + ". Preflowers (one calyx at a node) are usual maturity. Full flowering is not usual."],
      ["One plant has a much larger height than the group", "Different cultivars below one light, or clones of different ages",
       "Bend the plant down and put it at the edge of the bench at this time. In the next crop cycle, make groups of plants of the same cultivar that made roots at the same time."],
      ["You must apply water to the pot 3&times; each day", "The plant is root-bound: the time for this pot is at the end",
       "Transplant the plant to a larger pot and wait one week. Or do the flip at this time if all the other conditions of the pre-flip check are correct. Do not let a root-bound plant start the stretch" + _c("poorter-2012-pot-size")],
    ], cls="compact", caption="Compare the signs with the specification (target frame and target "
       "days). Do not use one sign only. A yellow leaf on day 5 and a yellow leaf on day 25 of the "
       "vegetative stage show different conditions."),
    callout("key", "The model for the vegetative stage",
      p("<strong>The function of the vegetative stage is to make a canopy that agrees with the "
        "specification. It is not a time in which you wait.</strong> Write the specification before "
        "the transplant. The specification gives N plants. The canopy area of each plant is full, "
        "and the plant has the maximum flip height or less.</p><p>The canopy has equal height, the "
        "roots are at the walls, and the leaves are green. Each day of the vegetative stage must "
        "make the room agree more with the specification, or the day gives no result. When the room "
        "agrees with the specification, do the flip on that day.")),
    p("The paper <a href='defoliation-training.html'>defoliation and training</a> gives the "
      "procedures to cut and bend the plants. The paper <a href='light-acclimation.html'>light "
      "acclimation</a> gives the safe procedure to increase the PPFD from clone light to a "
      "vegetative canopy of 900 &micro;mol."),
  ]})
