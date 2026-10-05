# -*- coding: utf-8 -*-
"""Paper: cloning, taking cannabis cuttings that root reliably (beginner)."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        stagecard, grid, card, chip, kv, steps)
import figs_lib as L

SLUG = "cloning"
TITLE = "How to make roots on cannabis cuttings"
EYEBROW = "Propagation · Cloning"
SUB = ("This guide shows you how to make roots on cannabis cuttings correctly each time. It gives a "
       "new grower all the steps, from the selection of a mother plant to a clone that you can "
       "transplant in 14 days.")
META = [("seedling", "Propagation"), ("image", "9 diagrams"),
        ("quote", "Citations · 7 sources"), ("clock", "~12 min read")]
RELATED = ["light-acclimation", "ipm-sop", "tissue-culture"]
REF_IDS = ["caplan-2018-stem-cuttings", "esposito-2026-morphology-predictors",
           "kim-2025-light-temp-rh", "landis-2022-iba-hemp-i3", "fattorini-2017-iba-to-iaa",
           "olympios-rootzone-temp", "punja-2023-fusarium-pythium-biocontrol",
           "msu-moisture-propagation", "liu-2023-shade-highlight-acclimation"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

SECTIONS.append({"id": "intro", "kicker": "01 · Start here", "title": "Purpose and scope",
  "blocks": [
    lead("A <strong>clone</strong> is a cutting from a plant. The cutting makes roots and becomes a "
         "new plant with the same genetics as the first plant. Cloning does not use flowers or "
         "seeds. You make roots on a piece of stem, and you do not germinate a seed."),
    p("Cloning gives each plant in a batch the same genetics as a known plant with good results. "
      "This plant is the <strong>mother plant</strong>. The same genetics gives the same speed of "
      "growth, the same yield and the same chemical properties. As a result, all the plants in the "
      "batch complete the crop cycle at the same time. The yield is the same as the yield of the "
      "last batch. Thus almost all commercial growers use clones and not seeds."),
    p("In a propagation room that operators control correctly, the rooting rate is frequently "
      "approximately 90 percent or more" + _c("caplan-2018-stem-cuttings") + ". Operators use this "
      "rate as a target. You can transplant the cuttings after approximately 10 to 14 days" +
      _c("kim-2025-light-temp-rh") + "."),
    figure(L.flow("From mother plant to transplant",
            [("Mother", "plant kept in good growth"), ("Take cutting", "cut at 45° below a node"),
             ("Stick in cube", "in a humidity dome"), ("Roots emerge", "day 7–14"),
             ("Transplant", "~day 14")]), 1,
      "The figure shows the five steps of the full procedure. You can see roots between day 7 and "
      "day 14. You can transplant the clone at approximately two weeks." + _c("kim-2025-light-temp-rh")),
    callout("note", "Who this is for",
      p("This guide is for a grower who wants to make a copy of a plant with the traits that the "
        "grower wants. The grower also wants a batch in which all the plants are the same, each "
        "time. Use the <a href='light-acclimation.html'>light acclimation</a> guide with this guide "
        "to move new clones into stronger light. Use the <a href='ipm-sop.html'>IPM hygiene</a> "
        "guide with this guide to keep the room clean.")),
  ]})

SECTIONS.append({"id": "key-terms", "kicker": "02 · The terms", "title": "Definitions",
  "blocks": [
    p("This guide uses these six terms many times. Make sure that you know the terms before you continue."),
    defterm("Node", "The point on a stem where the leaves and the side shoots attach. New roots and "
            "new growth start at the nodes. Thus you cut the stem near a node, and the new roots "
            "start at the node."),
    defterm("Mother plant", "A plant that you keep permanently in vegetative growth (growth of "
            "leaves). The plant does not make flowers. You keep the plant only to supply cuttings."),
    defterm("Cutting / clone", 'The shoot that you cut from the mother plant to make roots on it. '
            'After you cut the shoot, "cutting" and "clone" are two names for the same shoot.'),
    defterm("Rooting cube", "The cube of rockwool or peat that holds the cutting while the cutting "
            "makes roots. The cube holds water and air around the stem."),
    defterm("Dome", "The transparent plastic lid that holds the humidity in the air above the tray. "
            "A <strong>burp</strong> is a task in which you lift the dome for a short time. The "
            "task replaces the air in the dome with new air."),
    defterm("Hardening off", "The procedure in which you open the dome vents in stages and then "
            "remove the dome. The clones then adapt to the usual air of the room before the "
            "transplant."),
    figure(L.flow("Parts of a prepared cutting",
            [("Node", "where roots will start"), ("Internode", "stem between nodes"),
             ("45° basal cut", "new, directly below a node"), ("Lower leaves removed", "to keep more water"),
             ("Fan tips trimmed", "to ~50–70%"), ("Stem in cube", "1.5–2.5 cm (0.6–1.0 in) deep")]), 2,
      "The figure shows a cutting that you prepare for the cube. Cut the stem at an angle directly "
      "below a node, and make sure that the end is clean. Remove the bottom leaves. Cut the tips of "
      "the large fan leaves. Put the stem in the cube to the correct depth."),
  ]})

SECTIONS.append({"id": "mother-and-cut", "kicker": "03 · Selecting and cutting", "title": "Select and cut shoots",
  "blocks": [
    p("A good clone starts with a good shoot. Select vertical shoots from the top and middle parts "
      "of the canopy. Each shoot must be a minimum of 3 mm (0.1 in) thick and 15 cm (6 in) long. "
      "Thicker shoots that receive good light have larger energy reserves. These shoots make roots "
      "more quickly than thin shoots in the shade of the inner canopy" +
      _c("esposito-2026-morphology-predictors") + ". The thickness of the shoot and the color of "
      "the leaves are accurate indicators of the root growth of the cutting" +
      _c("esposito-2026-morphology-predictors") + "."),
    p("Apply sufficient water to the mother plant on the day before you cut the shoots. Then the "
      "cuttings are full of water and have turgor, and tissue that shows wilt does not easily make "
      "roots. Use a sterilized blade. At the start of the light cycle, cut each shoot at 45° "
      "directly below a node. Put each cutting immediately in a container with a weak solution. "
      "Make sure that the surface of the end is clean and that the end does not stay in the air."),
    callout("tip", "Cut at 45° and keep air out of the stem",
      ul(["If you cut the stem at <strong>45°</strong>, the surface at the end of the stem is larger than if you cut the stem flat. Thus more cells can become root cells.",
          "If the end of the stem dries in the air, a bubble of air goes into the stem. This bubble is an <strong>air embolism</strong>, and it stops the flow of water up the stem. Keep the end wet from the time that you cut the stem.",
          "Sterilize the blade between mother plants. Thus you do not move disease from one plant to the next." + _c("punja-2023-fusarium-pythium-biocontrol")], "tight")),
    figure(L.bars("Position of the shoot on the mother plant",
            [("Upper-mid (best)", 92), ("Lower interior", 58), ("Soft tip growth", 70)], unit="% root",
            note="Typical rooting results. Hard shoots with good light at the top and middle make the most roots.",
            maxv=100), 3,
      "Vertical shoots from the top and middle of the canopy, in good light, make roots at the "
      "highest rate. Weak shoots in the shade of the inner canopy have much lower rates." +
      _c("esposito-2026-morphology-predictors")),
  ]})

SECTIONS.append({"id": "hormone-and-cube", "kicker": "04 · Hormone and cube", "title": "Rooting hormone and propagation cubes",
  "blocks": [
    p("A cutting has no roots at the start. Thus you apply a <strong>rooting hormone</strong> to "
      "start the production of roots. A plant hormone is a chemical signal that gives instructions "
      "to the cells. The active ingredient in rooting hormones is usually <strong>IBA "
      "(indole-3-butyric acid)</strong>, an auxin, which is a type of plant growth signal" +
      _c("landis-2022-iba-hemp-i3") + ". In the stem, the plant changes IBA to IAA, and IAA is the "
      "signal that starts root growth" + _c("fattorini-2017-iba-to-iaa") + ". A rooting hormone is "
      "available as a gel or as a liquid."),
    p("Cut the stem again at 45° immediately before you put the cutting in the cube. Thus the end "
      "of the stem has new tissue. Apply rooting hormone gel to the bottom 1&ndash;2 cm "
      "(0.4&ndash;0.8 in) of the stem. Put the stem 1.5&ndash;2.5 cm (0.6&ndash;1.0 in) deep in a "
      "soaked cube. Push the cube lightly against the stem, but do not compress the cube. To do the "
      "<em>lift test</em>, lift the stem carefully, and make sure that the cube moves up with the "
      "stem."),
    steps([
      ("Soak the cube first", "Soak the rockwool or peat cubes in clone feed for a minimum of 15 minutes. Let the cubes drain freely. Do not compress the cubes to remove the water. If you compress a cube, you remove the air from the cube."),
      ("Cut the stem again", "Cut the stem again at 45° immediately before you put the cutting in the cube. Thus the tissue at the end is clean and has no air embolism."),
      ("Apply hormone", "For gel, put the bottom end of the stem approximately 1–2 cm (0.4–0.8 in) deep in the gel. For a liquid or alcohol hormone, soak the bottom end of the stem for approximately 30 seconds."),
      ("Put the stem in the cube and do the lift test", "Put the stem 1.5–2.5 cm (0.6–1.0 in) deep in the cube. Lift the stem carefully. The cube must move up with the stem."),
    ]),
    callout("warn", "Put the cutting in the cube in less than 30 seconds",
      p("After you cut the stem for the last time, put the cutting in the cube in approximately 30 "
        "seconds or less. When the stem end is in the air for a longer time, the risk of an air "
        "bubble increases. The bubble stops the uptake of water, and the cutting stops its growth.")),
    figure(L.line("Hormone concentration and rooting (typical IBA effect)",
            [(0, 55), (1, 74), (2, 88), (3, 90), (4, 78)],
            ["0 (none)", "low", "medium", "high", "too high"],
            ylab="% rooted", ymin=40, ymax=100,
            note="Rooting increases with the IBA dose to a maximum. A higher dose causes damage to the stem, and rooting decreases."), 4,
      "If the quantity of hormone is not sufficient, root growth is slow. Too much hormone causes "
      "damage to the bottom of the stem. The manufacturer mixes a rooting hormone gel to a "
      "concentration in the range for good rooting." + _c("landis-2022-iba-hemp-i3")),
  ]})

SECTIONS.append({"id": "dome-environment", "kicker": "05 · Environment", "title": "Dome, humidity, temperature and light",
  "blocks": [
    p("A cutting with no roots cannot pull water up the stem. Thus the cutting gets water from the "
      "humidity of the air until the roots start. The dome holds the humidity around the cutting. "
      "As a result, water goes directly from the air into the leaves while the stem makes roots."),
    p("Keep the air temperature at approximately 24&ndash;26&deg;C (75&ndash;79&deg;F). At the "
      "start, keep the humidity high (85&ndash;95% RH) in a closed dome. Then decrease the humidity "
      "in steps when the roots become longer" + _c("kim-2025-light-temp-rh") +
      ". Put a heat mat below the tray to keep the cube temperature at 22&ndash;24&deg;C "
      "(72&ndash;75&deg;F). The cube temperature has more effect on the speed of root growth than "
      "the air temperature has" + _c("olympios-rootzone-temp") + "."),
    p("VPD shows how much the air pulls water from the surface of a leaf. Air with less humidity "
      "and a higher temperature pulls more water from the leaf. When the VPD is higher, the surface "
      "of a leaf dries more quickly. Keep the VPD low (0.3&ndash;0.5 kPa) while the cuttings have "
      "no roots. Then increase the VPD in steps when the roots become longer. The clone can then "
      "replace the water that it transpires."),
    p("Keep the light intensity low in the first days, at approximately 60&ndash;100 PPFD (the "
      "intensity of the light at the plant). Increase the intensity to 150&ndash;200 PPFD at the "
      "time of hardening off" + _c("kim-2025-light-temp-rh") + ". Measure the intensity "
      "<strong>with the dome in position</strong>, because the plastic decreases the light "
      "intensity at the cutting below it."),
    figure(L.zones("Dome humidity in each root phase", 60, 100,
            [(85, 95, L.GL, "Initial heal (d1–4)"), (80, 85, L.GXL, "Early root (d5–7)"),
             (70, 80, L.AMBL, "Mid root (d8–10)"), (65, 75, L.BLUL, "Harden (d11–14)")],
            unit="% RH",
            note="Humidity is highest at the start. It decreases in steps when roots supply the water."), 5,
      "The target humidity in the dome decreases in stages during the cycle. The clone makes roots "
      "and then starts to get water with its roots." + _c("kim-2025-light-temp-rh")),
    table(["Phase", "Days", "RH", "VPD (kPa)", "Light (PPFD)"], [
      ["Initial healing", "1–4", "85–95%", "0.3–0.5", "60–100"],
      ["Start of root growth", "5–7", "80–85%", "0.5–0.7", "80–120"],
      ["Middle of root growth", "8–10", "70–80%", "0.6–0.8", "100–150"],
      ["Hardening off", "11–14", "65–75%", "0.8–1.0", "150–200"],
    ], cls="compact", caption="The table gives the environment targets for the four phases. In all phases, the air temperature is 24–26 °C (75–79 °F) and the cube temperature is 22–24 °C (72–75 °F). VPD shows how much the air pulls water from the surface of a leaf. A higher VPD value shows drier air." + _c("kim-2025-light-temp-rh")),
    callout("note", "Air movement: do not point a fan at the cuttings",
      p("A low airflow in the room is good. Do not point a fan directly at clones that have no "
        "roots. These clones cannot replace the water that they transpire. Air that flows directly "
        "on the clones dries them and quickly causes wilt.")),
  ]})

SECTIONS.append({"id": "timeline", "kicker": "06 · Do this", "title": "14-day cloning procedure",
  "blocks": [
    p("A large part of the work in cloning is to know when you must not touch the tray."),
    figure(L.flow("The 14-day arc",
            [("d1–4", "do not touch the dome"), ("d5–7", "first water and open vents"),
             ("d7", "examine for white roots"), ("d8–10", "prop vents wider"),
             ("d11", "hardening-off test"), ("d14", "transplant")]), 6,
      "At the start, the dome is closed and you do not touch the tray. Then you open the dome in "
      "stages when you see roots. The clone starts to get water with its roots."),
    p("<strong>Days 1&ndash;4:</strong> Keep the vents fully closed. Do not touch the tray. The "
      "humidity in the dome makes the cutting close its leaf pores. Then the cutting uses its "
      "energy to make roots.</p><p><strong>Days 5&ndash;7:</strong> It is usually necessary to "
      "apply water for the first time. Use the weight of the tray to find the time. Apply water "
      "when the weight of the tray is 40&ndash;50% less than its weight on Day 0. Do not apply "
      "water when the weight loss is less than 30%. Rot starts in a cube that is permanently wet" +
      _c("msu-moisture-propagation") + ". The color of the cube changes from dark brown to light "
      "brown, and this change is the same signal."),
    p("Start the clone feed at a low EC, approximately 0.6&ndash;1.2 mS/cm (the value is different "
      "for each product). Increase the EC only after you see roots. An EC of approximately 1.5 "
      "mS/cm can cause damage to soft cuttings. Keep the pH of the feed at 5.5&ndash;6.0 and the "
      "temperature of the water at 20&ndash;22&deg;C (68&ndash;72&deg;F).</p><p>From day 7, do one "
      "<strong>burp</strong> each day. Start to hold the vents open. Lift one cube at the edge of "
      "the tray and examine the cube for white roots.</p><p>On day 11, do the test for hardening "
      "off. Lift the dome from each tray and wait 10 minutes. If less than 5 clones in a tray show "
      "wilt, keep the dome off. If 5 or more clones in a tray show wilt, put the dome on the tray "
      "again. Do the test again on the next day. Transplant the clones at approximately day 14."),
    figure(L.zones("Vent opening in the cycle", 1, 14,
            [(1, 4, L.REDL, "Closed"), (5, 7, L.AMBL, "Burp 5–10 min/day"),
             (8, 10, L.GXL, "25–50% open"), (11, 14, L.GL, "50–100% open")],
            unit="day",
            note="You open the dome in stages, from fully closed to off, when the roots become longer."), 7,
      "The figure shows the opening of the dome vents on each day. At the start, closed vents keep "
      "the humidity high for cuttings that have no roots. At the end, fully open vents adapt the "
      "cuttings to the air of the room."),
    table(["Day", "Task", "Items to examine"], [
      ["1–4", "Keep the dome closed. Do not touch the tray.", "The cuttings have turgor and show no wilt."],
      ["5–7", "Use the tray weight to find the time for the first water. Start to open the vents.", "The color of the cube changes from dark brown to light brown. The weight loss of the tray is 40–50%."],
      ["7+", "Do one burp each day. Lift one cube at the edge of the tray.", "The first white roots show."],
      ["11", "Do the test for hardening off. Keep the dome off for 10 minutes.", "If less than 5 clones in a tray show wilt, keep the dome off."],
      ["14", "Transplant the keepers", "The roots are a minimum of 2–3 cm (0.8–1.2 in) long on more than one side of the cube. The cube stays in one piece."],
    ], cls="compact", caption="The table is a short list of the tasks for each day. The conditions for transplant at the end are the primary check for the decision to transplant the clones."),
  ]})

SECTIONS.append({"id": "troubleshooting", "kicker": "07 · When there is a problem", "title": "Troubleshooting",
  "blocks": [
    p("Most problems with clones have a small number of causes. Each cause shows different "
      "symptoms, thus you can find the cause quickly."),
    table(["Symptom", "Possible cause", "Task"], [
      ["Much wilt in days 1–2", "The RH in the dome is too low, the light intensity is too high, or the heat mat is off.", "Make sure that the RH is a minimum of 85%. Decrease the PPFD. Adjust the cube temperature to 22–24 °C (72–75 °F)."],
      ["Mold or slime on the cubes", "Water stays in the tray, the hygiene is bad, or the cubes are too warm.", "Remove the water that stays in the tray. Touch the cubes only with gloves. Keep the cubes at less than 26 °C (79 °F)."],
      ["Leaf tips that are dry and brown", "The feed EC or the VPD is too high (the air is too dry).", "Decrease the EC by 0.2–0.3. Increase the RH. Open the vents more slowly."],
      ["Yellow leaves before the roots show", "The mother plant had a nutrient deficiency, or the feed EC is too low.", "Examine the nutrition of the mother plant. In the next cycle, increase the EC by a small quantity."],
      ["White mold with fibers in the dome", "The humidity is too high and there is no air exchange.", "Do more burps. Always do the hygiene procedures for the dome."],
      ["Irregular rooting", "The moisture of the cubes or the quantity of hormone is different between cubes.", "Soak all the cubes equally. Put each cutting in the gel to the same depth."],
    ], cls="compact", caption="Find the cause from the symptom, then do the task. Many causes have the same symptoms. Thus correct the cause that is most possible first, and monitor the cuttings for one day."),
    callout("danger", "Tools and hands move disease",
      p("Sterilize the tools in 71% isopropyl alcohol for a minimum of 2 minutes (or in chlorine "
        "dioxide for a minimum of 180 seconds). Touch the cubes only with gloves. In a propagation "
        "room, tools and hands move disease from one cutting to the next. Hands without gloves move "
        "algae and pathogens" + _c("punja-2023-fusarium-pythium-biocontrol") +
        ". Good hygiene prevents the organisms of damping-off disease and root rot. These organisms "
        "kill all the cuttings in a tray" + _c("punja-2023-fusarium-pythium-biocontrol") +
        ".")),
  ]})

SECTIONS.append({"id": "expectations", "kicker": "08 · Typical results", "title": "Expected results and limitations",
  "blocks": [
    p("A first target of <strong>90 percent</strong> rooting is possible. Operators who do cloning "
      "frequently get 95 percent or more" + _c("caplan-2018-stem-cuttings") + ". The roots show in "
      "10 to 14 days. If a cutting has no roots after 21 days, there is a problem. Do an "
      "investigation of the cause. Do not wait for the cutting."),
    p("Some cuttings do not give a satisfactory result. At transplant, you select the cuttings to "
      "keep and the cuttings to discard. This <strong>culling</strong> is part of the "
      "procedure.</p><p>A <strong>keeper</strong> has strong roots and light green tops. A "
      "<strong>reject</strong> has only one to three weak roots. A <strong>kill</strong> has no "
      "roots, and you discard it.</p><p>Make 15 to 40 percent more cuttings than the necessary "
      "number of plants. Thus the number of plants is sufficient after you discard the weak "
      "cuttings."),
    figure(L.bars("A target of 100 plants with 40% more cuttings",
            [("Cuttings taken", 140), ("Veg (rooted)", 120), ("Flowered", 100)], unit=" plants",
            note="Make more cuttings than necessary. The batch is full after culling at each stage.",
            maxv=160), 8,
      "The figure starts with the number of plants for the flowering stage. Make more cuttings at "
      "the start. Thus you have the target number of plants after the culling at the rooting stage "
      "and at the vegetative stage."),
    figure(L.bars("Culling at transplant: keepers, rejects, kills",
            [("Keepers", 90), ("Rejects", 6), ("Kills", 4)], unit="%",
            note="In an adjusted room, approximately nine of ten are strong keepers",
            maxv=100), 9,
      "The figure shows a good tray after the culling. Most cuttings are strong keepers. A small "
      "number of cuttings are weak rejects, and a small number are kills." +
      _c("caplan-2018-stem-cuttings")),
    p("Some cultivars make roots more slowly. For these cultivars, make the cuttings some days "
      "before the usual date. Thus you can transplant the cuttings at the correct date. Record the "
      "tray weights, the EC and pH, and the rooting rate for each batch. Then, in the next cycle, "
      "you know the cultivars that you must cut before the usual date. You also know if there is a "
      "drift in the room conditions."),
    callout("key", "Three important items",
      ol(["<strong>90% is the minimum, not the maximum.</strong> A new grower who gets 90% has a good result, and an adjusted room gets 95% or more. If the rate is less than 80%, the environment or the hygiene is incorrect.",
          "<strong>Discard all the weak clones at transplant.</strong> When you discard the weak clones at the start, the batch keeps its uniformity.",
          "<strong>The environment has the largest effect.</strong> The humidity, the cube temperature and the light have more effect than the hormone product that you use. Adjust these items first."])),
    p("After the clones have roots and you complete the hardening off, the next task is to move the "
      "clones into stronger light. Do not cause stress to the clones. Refer to the <a "
      "href='light-acclimation.html'>light acclimation</a> guide. Use the <a "
      "href='ipm-sop.html'>IPM hygiene</a> procedure to keep the propagation room clean from the "
      "first day."),
  ]})
