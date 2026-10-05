# -*- coding: utf-8 -*-
"""Paper: defoliation and plant training for maximum yield (beginner)."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        stagecard, grid, card, chip, kv, steps)
import figs_lib as L

SLUG = "defoliation-training"
TITLE = "Defoliation and plant training for maximum yield"
EYEBROW = "Canopy · Training"
SUB = ("Topping, low-stress training, trellising, lollipopping and defoliation each have a "
       "different effect on the shape of the plant. This paper gives information about the effect "
       "of each method and the time to use it in the cycle of the crop. It also shows how to know "
       "when you do too much.")
META = [("scissors", "Canopy"), ("image", "12 diagrams"),
        ("quote", "8 sources"), ("clock", "~12 min to read")]
RELATED = ["airflow-design", "mould-risk", "harvest-dry-trim-cure"]
REF_IDS = ["sikora-2019-apical-bud-hemp", "massuela-2022-pruning-cbd-yield",
           "rodriguez-morrison-2021-ppfd-yield", "danziger-2022-planting-density",
           "wang-2020-shade-avoidance", "mahmoud-2023-budrot-botrytis",
           "anthony-2020-training-light-interception", "massuela-springer-2026-topping-hemp"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

SECTIONS.append({"id": "intro", "kicker": "Start here", "title": "Purpose and scope",
  "blocks": [
    lead("Plant training and defoliation change the shape of a cannabis plant. You bend and attach "
         "branches, and you remove some leaves and branches. As a result, more of the energy of the "
         "plant goes into the flowers that you harvest."),
    p("Without training, a plant has a large height and one primary top. The bottom growth is weak "
      "and in shade, and it makes flowers that have a low density and a low value. "
      "<strong>Training</strong> makes the canopy flat and wide. The canopy is the layer of leaves "
      "at the top of the plant. Thus more bud sites get light "
      "equally.</p><p><strong>Defoliation</strong> removes some leaves and opens the middle of the "
      "canopy. Thus the middle of the plant gets light and air, and the leaves do not stop them. If "
      "you do these methods correctly, they increase the yield and the quality. If you do them "
      "incorrectly or too much, they cause stress to the plant and decrease the quantity of flower."),
    ul(["<strong>Two groups of methods:</strong> training (to change the shape of the plant, you "
        "bend branches, attach branches and cut the growing tips) and defoliation (you remove "
        "leaves and bottom growth).",
        "Make the canopy flat and level, with strong light and airflow at each bud site.",
        "You do these tasks on set days in the cycle of the crop. You do not do them one time only.",
        "If you do too much, there is a risk of damage. This paper shows the parts that you must <em>not</em> remove."]),
    figure(L.flow("Plant without training and plant with a flat canopy",
            [("Without training", "one high cola, bottom growth in shade"),
             ("Training and spreading", "branches bent flat across a trellis"),
             ("After training", "many tops, same height, light on each site")],
            note="A flat canopy changes one top that gets all the light into many bud sites at the same height."), 1,
      "In a plant without training, one top uses most of the light. The inner part of the plant "
      "stays in shade, with flowers of low density. A flat canopy after training gives strong light "
      "to many bud sites at the same height."),
    callout("note", "Who this paper is for",
      p("This paper is for each cannabis grower who wants a yield that is the same each time. Use "
        "this paper with the <a href='airflow-design.html'>airflow design</a> and <a "
        "href='mould-risk.html'>mold risk</a> papers. The work on the canopy changes the quantity "
        "of light and the airflow.")),
  ]})

SECTIONS.append({"id": "key-terms", "kicker": "Terms", "title": "Definitions",
  "blocks": [
    p("Read these terms before the procedures. The paper uses these terms in all sections. Growers "
      "use these terms frequently, and many new growers do not know the difference between them. "
      "You do not have to know all the terms at this time. Each term occurs again, with more "
      "information."),
    defterm("Node", "The point on a stem where leaves and branches start. You count the nodes to "
            "measure the training (&lsquo;keep the top 3 nodes&rsquo;)."),
    defterm("Topping", "You cut the growing tip at the top of the plant. The growth in height "
            "stops, and two new tops start from the node below it."),
    defterm("FIM", "A topping that is not full: you cut most of the tip, but not all of it. This "
            "type of topping can cause more than two new tops to start."),
    defterm("Apical dominance", "A plant usually makes one primary top that is higher than the side "
            "branches. Topping and LST stop this effect. Thus the side branches can become as high "
            "as the primary top."),
    defterm("LST (Low-Stress Training)", "You bend the branches down carefully and attach them, to "
            "make the branches flat. You do not cut the plant."),
    defterm("Trellis / SCROG (Screen of Green)", "A horizontal net. The branches become higher "
            "through the openings of the net. The net holds the branches apart, at equal distances."),
    defterm("Lollipopping", "You remove the small branches, nodes and leaves from the bottom of the "
            "plant. The result is a bare stem at the bottom and the canopy at the top."),
    defterm("Defanning / defoliation", "You remove some large fan leaves to open the canopy for "
            "light and air."),
    defterm("Fan leaves", "The large leaves of the cannabis plant that absorb light. They are not "
            "the small sugar leaves in the buds."),
    defterm("Source and sink", "A &lsquo;source&rsquo; leaf makes more sugar than it uses. A "
            "&lsquo;sink&rsquo; (a flower, or a leaf in shade) uses more sugar than it makes."),
    figure(L.flow("The parts of a plant, from bottom to top",
            [("Lollipop zone", "bottom third: removed"),
             ("Lateral branches", "side branches, bent flat"),
             ("Nodes and fan leaves", "top 3 nodes stay"),
             ("Growing tip", "cut to make new tops")],
            note="Use training on the tip, lollipopping on the bottom, and defanning on the middle."), 2,
      "The parts of the plant where you use each method, from the bare &lsquo;lollipop zone&rsquo; "
      "at the bottom to the growing tip that topping removes."),
  ]})

SECTIONS.append({"id": "training-light", "kicker": "Basic information",
  "title": "Yield effects of training and defoliation",
  "blocks": [
    p("The basic effect is easy: <strong>more of the plant gets light and air</strong>. A flat, "
      "wide canopy has many bud sites at the same height, in strong light. Without training, one "
      "top gets all the light, and the other parts of the plant stay in shade."),
    p("You measure the intensity of light in <strong>PPFD</strong> (photosynthetic photon flux "
      "density: the quantity of light that the plant can use and that the canopy receives each "
      "second). In a flowering room, the light is approximately 400 to 800 PPFD at the start of "
      "flowering. The light increases to a maximum of approximately 1000 to 1200 PPFD in the middle "
      "of bloom." + _c("rodriguez-morrison-2021-ppfd-yield") + " This intensity increases the yield "
      "only if the bud receives the light. Thus you must open the middle of the canopy. The yield "
      "of cannabis continues to increase with higher light, up to this range, if the canopy can use "
      "the light." + _c("rodriguez-morrison-2021-ppfd-yield")),
    figure(L.line("Target canopy light (PPFD) during the crop",
            [(0, 350), (1, 450), (2, 600), (3, 800), (4, 1000), (5, 1150), (6, 1200), (7, 1050), (8, 900)],
            ["vegetative", "wk1", "wk2", "wk3", "wk4", "wk5", "wk6", "wk7", "wk8"],
            ylab="PPFD", ymin=0, ymax=1300,
            note="The light increases to a plateau of 1000 to 1200 in the middle of bloom, then decreases at the end."), 3,
      "A usual light curve for a flowering room: 400 to 800 PPFD in week 1, a plateau of 1000 to "
      "1200 PPFD in weeks 4 to 7, and then the light decreases. When you open the canopy, the "
      "bottom buds also get the light of the plateau." + _c("rodriguez-morrison-2021-ppfd-yield")),
    p("The <strong>source and sink</strong> model shows the effect of light on a leaf. A leaf in "
      "good light makes sugar and supplies it to the buds. This leaf is a source. But a leaf in "
      "shade, deep in the canopy, becomes a sink. It uses more sugar than it makes." +
      _c("massuela-2022-pruning-cbd-yield") + "</p><p>When you open the canopy, the leaves in shade "
      "can become sources again. At the same time, the airflow becomes better."),
    figure(L.flow("Sources and sinks, and the effect of an open canopy",
            [("Fan leaf in light", "SOURCE: makes sugar"),
             ("Sugar flow", "goes to flowers"),
             ("Flower", "SINK: uses the sugar"),
             ("Leaf in an open canopy", "SINK becomes SOURCE again")],
            note="A leaf in light makes more sugar than it uses. A leaf in shade uses more than it makes. Open the canopy."), 4,
      "Fan leaves in good light supply sugar to the flowers. Inner leaves in shade become sinks. "
      "When you open the canopy, they become sources again, and the humidity around the buds "
      "decreases." + _c("massuela-2022-pruning-cbd-yield")),
    p("Better airflow through an open canopy decreases the humidity around buds with high density. "
      "This directly decreases the risk of bud rot. The air can absorb only a maximum quantity of "
      "moisture. When the air has almost this maximum, it does not remove humidity from the "
      "surfaces of the plant. Thus the humidity stays around the buds.</p><p><strong>VPD</strong> "
      "(vapor pressure deficit) measures how much more moisture the air can absorb. Keep the VPD in "
      "the range of 0.8 to 1.2 kPa. Air with high humidity that does not move, in a closed canopy, "
      "lets gray mold start in a thick cola." + _c("mahmoud-2023-budrot-botrytis")),
    callout("key", "Results of the work",
      ul(["A flat, wide canopy lets many bud sites get the strongest light, and not only one top.",
          "An open middle lets the bottom buds and the inner buds get this high light. Without the light, these buds have low density.",
          "Better airflow decreases the humidity around buds with high density and decreases the "
          "risk of mold and bud rot." + _c("mahmoud-2023-budrot-botrytis"),
          "Keep the VPD at approximately 0.8 to 1.2 kPa. The airflow from defoliation helps to keep it in this range."], "tight")),
  ]})

SECTIONS.append({"id": "topping-lst", "kicker": "Basic information",
  "title": "Topping, FIM and low-stress training in the vegetative stage",
  "blocks": [
    p("Topping and LST decrease <strong>apical dominance</strong>. With apical dominance, one top "
      "becomes high quickly, and the side branches stay behind. Topping removes that tip. Thus the "
      "growth hormones go to the side branches, and one primary top becomes two or more tops. The "
      "plant becomes wider and has more branches." + _c("sikora-2019-apical-bud-hemp") +
      " A test shows that the removal of the apical bud changes the parts of all of the plant where "
      "growth and yield occur." + _c("sikora-2019-apical-bud-hemp")),
    p("<strong>LST</strong> has the same effect, and you do not cut the plant. You bend the high "
      "middle stem down and attach it to the side. Thus the bottom branches become as high as the "
      "middle stem, and the canopy becomes level.</p><p>Because you do not cut the plant, there is "
      "no recovery time. Thus LST is the careful method that is best for new growers and for a home "
      "tent. Topping is the stronger method. It is best for longer vegetative stages or for "
      "genetics with much stretch." + _c("massuela-springer-2026-topping-hemp")),
    figure(L.flow("Topping: one tip becomes two tops",
            [("One primary top", "that goes straight up"),
             ("Cut the tip", "remove the top node"),
             ("Two new tops", "start from the node below")],
            note="When you cut the tip, apical dominance stops for the side shoots."), 5,
      "Topping removes the primary tip. The node below the tip makes two new tops. Thus the number "
      "of bud sites at that height becomes two times larger." + _c("sikora-2019-apical-bud-hemp")),
    figure(L.flow("LST: bend, do not cut",
            [("High middle stem", "primary, vertical"),
             ("Bend down and attach", "pull it to the edge of the pot"),
             ("Level canopy", "side branches become wide and level")],
            note="The result is the same as topping, with no damage and no recovery time."), 6,
      "With low-stress training, you change the shape of the plant when you bend and attach "
      "branches, and you do not cut. The stress is lower, there is no recovery time, and it is easy "
      "for new growers."),
    p("In commercial rooms, the first topping is usually at approximately <strong>day 5 to "
      "7</strong> of the vegetative stage. Growers remove 2 to 3 nodes from plants that are much "
      "higher than the other plants. The removal makes the height the same as the height of the "
      "remaining canopy. In a usual vegetative stage of 14 days, growers do only one topping, or no "
      "topping. In a vegetative stage of 21 days, topping is the usual procedure." +
      _c("massuela-springer-2026-topping-hemp")),
    table(["Height group", "Usual length of the vegetative stage", "Method of topping"], [
      ["Genetics with large height and much stretch", "Approximately 8 to 10 days", "Do the topping at the start of the vegetative stage. Remove 2 to 3 nodes from plants that are much higher than the other plants."],
      ["Genetics with average height", "Approximately 10 to 14 days", "Do the topping one time at approximately day 5 to 7, or use only LST"],
      ["Genetics with small height", "Approximately 14 to 21 days", "Frequently use only LST. Topping is not necessary."],
    ], cls="compact",
    caption="Select the method for the length of the vegetative stage and the height of the "
            "genetics. For a shorter vegetative stage, use LST. For a longer vegetative stage, "
            "topping is a good procedure." + _c("massuela-springer-2026-topping-hemp")),
    callout("tip", "New growers: start with LST",
      p("If you are new, do not use topping in your first crop. Use LST. When you bend and attach "
        "branches, you get most of the result of a flat canopy, and the plant does not have to "
        "recover. After you know the stretch of your genetics, you can use topping.")),
  ]})

SECTIONS.append({"id": "trellis-spread", "kicker": "Basic information",
  "title": "Trellising and canopy control",
  "blocks": [
    p("A <strong>trellis</strong> is a horizontal net above the table, and the plants become higher "
      "through the net. The trellis has two tasks. At the start, it holds a wide canopy in "
      "position. After this, it prevents damage to the branches because of the weight of the heavy "
      "buds. When you do the spreading of the branches, all of the table gets light. Thus the high "
      "PPFD in the middle of bloom gives a higher yield." +
      _c("anthony-2020-training-light-interception")),
    p("A usual procedure is to set all three trellis layers on <strong>day 1 of flowering</strong>. "
      "The first net is 2.5 to 5 cm (1 to 2 in) below the top of the canopy. At approximately day 5 "
      "to 7, the plants are through that first net. Then the personnel do the "
      "<strong>spreading</strong> of the branches. They pull the branches away from the middle "
      "stalk and put them in the openings of the net. Thus the middle gets light, and the branches "
      "fill all of the table equally."),
    figure(L.flow("Three trellis layers, three tasks",
            [("Net 1 (low)", "spreading: light in the middle"),
             ("Net 2 (middle)", "hold the branches during stretch"),
             ("Net 3 (high)", "hold the heavy weight of the flowers")],
            note="The first net does the spreading. The primary task of the top nets is to hold the weight of the flowers."), 7,
      "The side of a table in the flowering stage, with three nets one above the other. The lowest "
      "net does the spreading of the canopy. The top two nets hold the weight of the flowers when "
      "they become larger." + _c("anthony-2020-training-light-interception")),
    figure(L.flow("Spreading: fill each opening",
            [("Middle stalk", "all branches in the middle"),
             ("Pull away from the stalk", "put each branch in an empty opening"),
             ("Equal spacing", "each opening filled, light in the middle")],
            note="Spreading at the start opens the middle. Thus you remove a smaller number of leaves after this."), 8,
      "From above: the spreading moves the branches away from the middle stalk into the empty "
      "openings of the trellis. Thus the branches fill the table equally, and the middle is not in "
      "shade."),
    ul(["Set all trellis levels on day 1 of flowering. The first net is 2.5 to 5 cm (1 to 2 in) below the top of the canopy.",
        "At approximately day 5, the plants are through the first net. Then you do the spreading of the branches away from the middle stalk.",
        "Spreading opens the middle to light and airflow. Thus you remove a smaller number of fan leaves after this.",
        "The number of nets changes with the height of the plants. For short plants, use approximately 2 layers. For genetics with large height, use 3 layers."]),
    callout("note", "Better spreading, less defoliation",
      p("When you do the spreading of the canopy at the start, you remove a smaller number of fan "
        "leaves after this. A table with good spreading is open to light. Thus defoliation is a "
        "small task and not a large task.")),
  ]})

SECTIONS.append({"id": "schedule", "kicker": "Do this",
  "title": "Times for defoliation and training",
  "blocks": [
    p("This section gives a procedure with times for a flowering room. Use it as a default, and "
      "adjust it to your genetics. The procedure starts with trellising on day 1. The last task is "
      "a defanning, if necessary, in the last part of bloom."),
    figure(L.flow("Times of the work in the flowering room",
            [("Day 1", "set the trellis on the tables"),
             ("Day 5-14", "spreading with the first net"),
             ("Day 7-10", "Phase 1: lollipopping of the bottom"),
             ("Day 21-28", "Phase 2: bottom defanning"),
             ("Day 42-49", "Phase 3: last defanning, if necessary")],
            note="The heavy work is in the first part of flowering. The last work is not necessary, and you make the decision for each cultivar."), 9,
      "The default procedure with times for the flowering stage, from day 1 to week 7. The heavy "
      "work on the structure of the canopy is in the first part. The only task in the last part is "
      "a defanning that is not always necessary, and you make the decision for each cultivar."),
    steps([
      ("Day 1: Trellis", "Set all trellis levels. Put the first net 2.5 to 5 cm (1 to 2 in) below the top of the canopy."),
      ("Day 5&ndash;14: Spreading", "When the plants are through the first net, pull the branches away from the middle stalk. Put the branches in the openings to fill the table equally."),
      ("Day 7&ndash;10: Phase 1 lollipopping", "Remove the small branches, nodes and leaves from the bottom half or the bottom third of the plant. Keep a minimum of the top 3 nodes on each primary branch."),
      ("Day 21&ndash;28: Phase 2 defanning", "Remove the bottom fan leaves on all the plants. Thus more light and air go into the inner part of the canopy."),
      ("Day 42&ndash;49: Phase 3 defanning", "A last defanning, if necessary. You make the decision for each cultivar. Do it only if more light or air is necessary in the canopy for that cultivar."),
    ]),
    table(["Day of flowering", "Task", "Result"], [
      ["Day 1", "Trellis (all levels)", "Set the structure of the canopy before the plants fill the space"],
      ["Day 5&ndash;14", "Spreading with the first net", "Open the middle to light. Fill the table equally."],
      ["Day 7&ndash;10", "Phase 1 lollipopping", "Remove the bottom larf. It cannot make good flower."],
      ["Day 21&ndash;28", "Phase 2 defanning", "Light and airflow to the bottom and inner buds"],
      ["Day 42&ndash;49", "Phase 3 defanning (if necessary)", "Only if more light or air is necessary for that cultivar"],
    ], cls="compact",
    caption="A default procedure with times for the flowering room. The lollipop zone is "
            "approximately the bottom 25 to 45 cm (10 to 18 in), the bottom third. In this zone, "
            "the growth makes small larf that does not get full maturity."),
    figure(L.flow("The lollipop zone",
            [("Top: keep", "top 3 nodes of each branch stay"),
             ("Middle: defanning", "defanning for light and air"),
             ("Bottom 10-18in: remove", "bottom third removed, bare stem")],
            note="Remove the bottom third. Keep the top 3 nodes on each primary branch."), 10,
      "Lollipopping removes approximately the bottom 25 to 45 cm (10 to 18 in), the bottom third. "
      "It keeps a minimum of the top 3 nodes on each primary branch. Thus the plant uses its energy "
      "for the flowers that get full maturity."),
    callout("warn", "Do lollipopping in the first stage",
      p("Do Phase 1 lollipopping in the first week or the first two weeks of flowering. At this "
        "time, the plant can recover and send its energy to the other parts. Do not remove much of "
        "the bottom in the last stage of bloom. The removal causes damage to the plant, because the "
        "plant must make the flowers larger in this stage.")),
  ]})

SECTIONS.append({"id": "pitfalls", "kicker": "Problems to prevent",
  "title": "Troubleshooting",
  "blocks": [
    p("The largest problem is that you <strong>remove too many fan leaves</strong>. Fan leaves are "
      "&lsquo;sources&rsquo;: they make more energy than they use. Thus keep as many fan leaves on "
      "the plant as possible, and get sufficient light and airflow in the canopy. If you remove too "
      "many leaves, the buds do not get sufficient energy. Too much pruning can decrease the yield "
      "and the cannabinoid content, and it does not help." + _c("massuela-2022-pruning-cbd-yield")),
    figure(L.flow("Too much defoliation and correct defoliation",
            [("Too much removed", "bare stems, low energy"),
             ("Select", "keep source leaves"),
             ("Correct defoliation", "open middle, many fan leaves: ENERGY AND AIRFLOW")],
            note="Open the canopy, but keep the leaves that supply energy. More bare stem is not better."), 11,
      "Left: a plant with too much defoliation, with a small leaf area to supply the flowers. "
      "Right: a plant with correct defoliation, with an open middle and many fan-leaf sources that "
      "stay on the plant." + _c("massuela-2022-pruning-cbd-yield")),
    p("The second problem is <strong>overcrowding</strong>. Plants that are too near each other "
      "cause a <strong>shade avoidance response</strong>. The plants sense the shade of the plants "
      "near them. Then they use energy to make the weak inner branches longer, in the direction of "
      "the light, and not to make flowers." + _c("wang-2020-shade-avoidance") +
      " With correct spacing, much less defoliation is necessary. The canopy has a correct density "
      "from the start."),
    p("A usual start point is approximately 0.21 m² (2.3 ft²) for each plant. The usual range is "
      "0.17 to 0.28 m² (1.8 to 3.0 ft²). A higher plant density can increase the total yield for "
      "each area, but it decreases the uniformity. Thus you cannot get the highest yield and the "
      "highest uniformity together, and there is no one &lsquo;correct&rsquo; number." +
      _c("danziger-2022-planting-density")),
    figure(L.zones("Plant spacing: density zones (sqft for each plant)",
            1.0, 3.5,
            [(1.0, 1.8, L.REDL, "high density: shade avoidance"),
             (1.8, 3.0, L.GL, "usual range"),
             (3.0, 3.5, L.AMBL, "waste of space")],
            unit=" sqft",
            note="Start at approximately 2.3 sqft. With less than 1.8 sqft, plants have more stretch and make shade for each other."), 12,
      "Spacing zones. A density that is too high causes shade avoidance." +
      _c("wang-2020-shade-avoidance") + " The usual range is 0.17 to 0.28 m² (1.8 to 3.0 ft²). With "
      "correct spacing, you do much less work on the plants." + _c("danziger-2022-planting-density")),
    table(["Problem", "Effect", "Correct procedure"], [
      ["Too much defoliation", "You remove the leaves that supply the buds. The yield and the potency decrease.", "Keep as many fan-leaf sources as possible. Open the canopy only as much as necessary."],
      ["Overcrowding", "Shade avoidance: the inner growth is weak and has much stretch", "Use approximately 0.21 m² (2.3 ft²) for each plant. The range is 0.17 to 0.28 m²."],
      ["Topping in the flowering stage", "It causes damage to the plant when the plant must make the flowers larger", "Do all the topping in the vegetative stage"],
      ["Heavy defanning in the last stage of bloom", "Stress, with no time to recover", "Do the heavy work in the first stage of flowering"],
      ["A smell of mold, and inner leaves that die", "The canopy is too closed, and the risk of bud rot increases", "First, increase the airflow. Do not remove all the leaves."],
    ], cls="compact",
    caption="The usual problems of new growers. In the last row, the correct procedure for a canopy "
            "with air that does not move is more airflow. It is not the removal of all the leaves." +
            _c("mahmoud-2023-budrot-botrytis")),
    callout("danger", "Leaves are not the problem",
      p("Do not continue to cut until the plant is &lsquo;clean&rsquo;. Each fan leaf that you "
        "remove supplies energy to the flowers. Open the canopy sufficiently for light and air, and "
        "then stop. If the room continues to have a smell of mold, increase the airflow. Do not cut "
        "more. Read the <a href='airflow-design.html'>airflow design</a> paper." +
        _c("massuela-2022-pruning-cbd-yield"))),
  ]})

SECTIONS.append({"id": "expectations", "kicker": "The limits",
  "title": "Expected results and limitations",
  "blocks": [
    p("Training and defoliation are controls for the yield and the quality, but they have limits. "
      "The numbers change if your genetics, light or environment change. Use the data of each crop "
      "to adjust the method for the next crop. It is possible that you must adjust the method in "
      "approximately three crops of the same cultivar, to get its best yield and quality."),
    figure(L.line("Adjust the method for a cultivar in three crops",
            [(0, 100), (1, 118), (2, 128)],
            ["crop 1", "crop 2", "crop 3"],
            ylab="yield and quality index", ymin=90, ymax=140,
            note="Same cultivar, same room: you adjust the training and the defoliation in each crop."), 13,
      "The yield and the quality usually increase in the first three crops of a cultivar. During "
      "these crops, you find the stretch of the cultivar and the quantity of work on the canopy "
      "that is necessary."),
    p("Good selection of the genetics and the spacing gives a better result at low cost. The "
      "correct number of plants and the correct layout change the yield for each area and the "
      "uniformity. The effect can be larger than the effect of equipment with a high cost, and the "
      "cost does not increase. The effect occurs because the uniformity and the light interception "
      "increase." + _c("danziger-2022-planting-density") +
      _c("anthony-2020-training-light-interception")),
    ul(["It is possible that you must adjust the method in approximately 3 crops of a cultivar, to get its best yield and quality.",
        "Good selection of the genetics and the spacing can increase the profit by 15 to 30%, and "
        "the cost does not increase." + _c("danziger-2022-planting-density"),
        "It is not necessary to do all the phases for each cultivar. You make the decision about the Phase 3 defanning for each cultivar, from the condition of the plants.",
        "Record each crop and make photos of the canopy. Then use your data for the changes, and do not use general instructions.",
        "For genetics with slow growth, use careful methods and remove a smaller quantity."]),
    callout("key", "Three important facts",
      ol(["<strong>No procedure is correct for all rooms.</strong> Start from this procedure with "
          "times. Adjust the day ranges and the quantity that you remove for <em>your</em> "
          "genetics, light and room.",
          "<strong>A small quantity of removal is usually better.</strong> Keep the leaves that "
          "supply the plant. Open the canopy only sufficiently for light and air, and then stop.",
          "<strong>Your camera is the best tool.</strong> Make photos of the canopy in each crop. "
          "Use these photos for your decisions in the next crop, and do not use a general method "
          "for all rooms."])),
    p("Make the canopy flat, and do the spreading at the start. Use lollipopping on the bottom of "
      "the plant. Use defanning only as much as is necessary for light and air. Record your tasks. "
      "This procedure, and not one task only, gives the result of training and "
      "defoliation.</p><p>To prepare for the next stage, read the paper on <a "
      "href='harvest-dry-trim-cure.html'>harvest, dry, trim and cure</a>. During bloom, use the <a "
      "href='mould-risk.html'>mold risk</a> paper."),
  ]})
