# -*- coding: utf-8 -*-
"""Paper: the cannabis grow room, a systems guide (beginner)."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        stagecard, grid, card, chip, kv, steps)
import figs_lib as L

SLUG = "grow-room-systems"
TITLE = "Cannabis grow room systems"
EYEBROW = "Basic · Grow-room systems"
SUB = ("A grow room is one connected system, and not a list of devices. Light, heat, humidity, air, "
       "and water have an effect on each other. This paper shows these connections. Then you can "
       "install and adjust the systems in the correct sequence and prevent problems before one "
       "problem causes the next.")
META = [("building", "Basic"), ("image", "4 diagrams"),
        ("quote", "10 sources"), ("clock", "~18 min to read")]
RELATED = ["coco-crop-steering", "airflow-design", "mould-risk"]
REF_IDS = ["rm2021-light", "faust2018-dli", "collado2025-light", "chandra2008-photo",
           "inoue2021-vpd", "schymanski2016-wind", "malik2025-media", "caplan2019-drought",
           "punja2019-pathogens", "punja-budrot-cjb"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

SECTIONS.append({"id": "start", "kicker": "01 · Read this first", "title": "Purpose and scope",
  "blocks": [
    lead("Light, heat, humidity, and water are one problem and not four different tasks. A new "
         "grower gets a light, a fan, a humidifier, and a nutrient bottle, and thinks that each is "
         "a different task. When you increase the light, the room becomes hotter and the plants use "
         "more water. Then the humidity of the air increases, and the dehumidifier must remove more "
         "water. Each part has a connection to the other parts."),
    p("This paper shows these connections. Thus you can install and adjust the systems in the "
      "correct sequence. Then one problem does not cause the next problem. It is not necessary to "
      "know about cultivation before you read this paper."),
  ]})

SECTIONS.append({"id": "terms", "kicker": "02 · Terms", "title": "Definitions",
  "blocks": [
    defterm("PPFD", "The quantity of light that falls on the canopy at this time, and that the "
            "plant can use. The unit is µmol/m²/s."),
    defterm("DLI (daily light integral)", "The total quantity of light that the plant gets in one "
            "day (mol/m²/day). DLI = PPFD × the hours that the light is on. This value has the "
            "primary effect on growth." + _c("faust2018-dli")),
    defterm("Transpiration", "The plant moves water up from the roots and releases it as vapor "
            "through small pores in the leaves (stomata). The water that moves up also moves the "
            "nutrients that are in the water, from the roots to the leaves. The evaporation of the "
            "water decreases the temperature of the leaf. With transpiration, the plant keeps a "
            "stable temperature and gets its nutrients."),
    defterm("VPD (vapor pressure deficit)", "VPD shows how strongly the air removes water from the "
            "plant. The temperature and the humidity together set VPD, and not only the humidity. "
            "Dry, warm air removes water strongly. Cool, humid air is almost full of water, and it "
            "removes water weakly. VPD is one number that gives the strength of this removal, and "
            "it shows the rate of transpiration of the plant."),
    defterm("CO2", "Carbon dioxide. The plant uses it with light to make sugar. More CO2 can "
            "increase growth if the light is sufficiently high."),
    defterm("Stomata", "Small pores on leaves that you can see only with a microscope. The plant "
            "can open and close them. They open to absorb CO2 and to release water. They close when "
            "the plant has stress."),
    defterm("Substrate", "The material that contains the roots (coco, rockwool, peat). The "
            "substrate has an effect on the water, the air, and the salt at the root." +
            _c("malik2025-media")),
  ]})

SECTIONS.append({"id": "one-system", "kicker": "03 · How the parts connect", "title": "Connections between the systems of a grow room",
  "blocks": [
    p("One sequence of parts operates your room. When you change the first part, each part after it changes:"),
    figure(L.flow("A change of the light changes all the next parts",
            [("Light", "energy goes to the leaf"), ("Leaf heat", "leaf hotter, more photosynthesis"),
             ("Transpiration", "plant absorbs and releases water"),
             ("Room humidity", "that water vapor then fills the room"),
             ("HVAC load", "AC and dehumidifier must remove it")],
            note="More light gives more yield, but only if the other parts operate at the same rate."), 1,
      "The sequence of a coupled system. Thus the step &lsquo;add more light&rsquo; does not give a "
      "good result if your climate and airflow cannot remove the larger quantity of water from the "
      "plants." + _c("collado2025-light")),
    callout("key", "One procedure that prevents most errors",
      p("When you increase one input, find the other inputs that must change with it. More light "
        "&rarr; more transpiration &rarr; more humidity &rarr; more dehumidification and more water "
        "and feed. The inputs change in groups, and not only one at a time.")),
  ]})

SECTIONS.append({"id": "light", "kicker": "04 · Light: the primary lever", "title": "Quantity of light",
  "blocks": [
    p("Light is the first lever: it sets the quantity of all the other inputs that the plant uses. "
      "In cannabis, the yield of flowers has an approximately <strong>linear increase with the "
      "light</strong>, up to very high intensities (approximately 1800 µmol/m²/s in one test, a "
      "yield increase of approximately 4.5×)." + _c("rm2021-light") + " Bright light gives good "
      "results. But the other parts of the room must control the heat, the humidity, and the water "
      "use that the light causes."),
    figure(L.bars("More light, more flower (approximately linear)",
            [("400", 30), ("800", 55), ("1200", 78), ("1600", 96)], unit="",
            note="PPFD (µmol/m²/s) and relative flower yield. The yield increases at more than the saturation PPFD of one leaf.",
            maxv=110), 2,
      "The yield of the whole plant continues to increase at light intensities much higher than the "
      "saturation of one leaf. The canopy uses light that the top leaves cannot use." +
      _c("rm2021-light") + " The yield increases more slowly at very high intensities. At these "
      "intensities, the CO2, the climate, and the water must agree with the light."),
    callout("warn", "Leaf and canopy: a frequent error",
      p("Do not set the room light with values from one leaf. When you measure one leaf, "
        "photosynthesis has its maximum at a moderate light intensity. Then you can stop to "
        "increase the light at this point. The whole canopy continues to use more light to make "
        "more flower at much higher intensities." + _c("rm2021-light"))),
  ]})

SECTIONS.append({"id": "climate", "kicker": "05 · Climate: temperature, humidity, VPD", "title": "Climate: temperature, humidity and VPD",
  "blocks": [
    p("Temperature and humidity have one effect together: <strong>VPD</strong>. VPD has a large "
      "effect on the rate of transpiration of the plant. There is a middle range in which the "
      "conditions are satisfactory. If VPD is too low, the plant becomes slower. If VPD is too "
      "high, the plant closes its stomata to keep water. As a result, the CO2 uptake and the growth "
      "stop." + _c("inoue2021-vpd")),
    figure(L.zones("VPD: use the middle range", 0.4, 2.0,
            [(0.4, 0.8, L.BLUL, "humid / slow"), (0.8, 1.2, L.GL, "best range"),
             (1.2, 1.6, L.GXL, "generative"), (1.6, 2.0, L.AMBL, "stress: stomata close")],
            unit=" kPa",
            note="Approximate. The best range changes with stage and cultivar. A stable VPD is better than a VPD that changes."), 3,
      "A middle range that you can use is approximately 0.8–1.2 kPa (the range is different for "
      "each cultivar, and in the last stage of flowering it is frequently approximately 1.2–1.5). "
      "Drier air can cause generative growth. But at more than approximately 1.5 kPa, the plant "
      "closes its stomata and its growth stops." + _c("inoue2021-vpd")),
    p("<strong>CO2</strong> is the other lever for the climate. When you add CO2, photosynthesis "
      "and water-use efficiency increase. But the plant also transpires <em>less</em>. It closes "
      "part of its stomata, and it does not open them." + _c("chandra2008-photo") +
      " Growth increases only when the light is high."),
  ]})

SECTIONS.append({"id": "air", "kicker": "06 · Movement", "title": "Airflow in the connected system",
  "blocks": [
    p("Air that moves has two important tasks. It removes the thin film of air with high humidity "
      "that does not move and stays on each leaf. It also decreases the temperature of the leaf by "
      "convection.</p><p>Faster air makes this film thinner. As a result, the CO2 uptake and the "
      "water-use efficiency increase (more carbon fixation for each unit of water). But the total "
      "water use frequently increases in bright rooms." + _c("schymanski2016-wind") +
      " Air that moves also keeps all the plants in the room in the same climate."),
    callout("note", "More information on airflow",
      p("The paper <a href='airflow-design.html'>Airflow design for indoor cultivation</a> gives "
        "the full information on boundary layers, fan positions, velocity targets, and dead zones. "
        "In this paper, it is sufficient to know one fact. Without air movement, your light, "
        "climate, and CO2 settings do not have the same effect on each leaf.")),
  ]})

SECTIONS.append({"id": "rootzone", "kicker": "07 · Root zone and water supply", "title": "Root-zone supply",
  "blocks": [
    p("All the parts before the root zone cause the plant to use <em>much water</em>, and the root "
      "zone must supply this water. When the room has more light and drier air, the plant "
      "transpires more and uses more water and nutrients at the roots. Your substrate and your "
      "irrigation are the supply part of the same system." + _c("malik2025-media")),
    p("The root zone is also a lever for crop steering: a controlled dryback in the root zone "
      "causes generative growth and can increase potency." + _c("caplan2019-drought") +
      " The paper on <a href='coco-crop-steering.html'>coco and crop steering</a> gives the full "
      "information on the mechanisms. The irrigation must <em>agree with</em> the water use that "
      "the other parts of the room cause. The irrigation must not operate with a timer that does "
      "not change."),
  ]})

SECTIONS.append({"id": "order", "kicker": "08 · Setup sequence", "title": "System setup sequence",
  "blocks": [
    p("The inputs have connections to each other. Thus the sequence in which you set them is important. Do the steps in this sequence:"),
    steps([
      ("1. Select your light target", "Select the DLI and the PPFD that your room can supply. This sets the necessary quantity for all the other systems."),
      ("2. Set the climate for the light", "Set the temperature and the humidity to a correct VPD for that light intensity. If the light is high, add CO2."),
      ("3. Supply the airflow", "Use sufficient air movement to mix the air in the room and to move air to each leaf. Refer to the airflow paper."),
      ("4. Apply the correct feed", "Set the irrigation and the feed EC for the transpiration that the previous steps cause. Then use dryback for crop steering."),
      ("5. Crop steering and adjustment", "Only at this time, cause more generative growth or more vegetative growth. Change one lever at a time, and monitor all the parts of the sequence."),
    ]),
  ]})

SECTIONS.append({"id": "disease", "kicker": "09 · Disease risk", "title": "Disease risk in connected systems",
  "blocks": [
    p("A room that is warm and humid, with a high density of plants, gives large plants, and it "
      "also gives mold. Bud rot (<em>Botrytis</em>) starts and increases quickly at a humidity of "
      "more than approximately 70% and at moderate temperatures. A thick canopy keeps humid air "
      "that does not move in its inner part, and your room sensor does not measure this air." +
      _c("punja-budrot-cjb")),
    callout("danger", "A room sensor can show an incorrect value",
      p("Do not use only the average value of the room. A sensor in open air can show a good value "
        "of 60%. At the same time, the inner part of a large cola can be at 85% humidity, and the "
        "cola rots. Airflow through the canopy and correct spacing between plants prevent the "
        "disease." + _c("punja2019-pathogens") + " The paper on <a href='mould-risk.html'>mold "
        "risk</a> gives the full information.")),
  ]})

SECTIONS.append({"id": "trouble", "kicker": "10 · When a problem occurs", "title": "Troubleshooting",
  "blocks": [
    table(["Symptom", "Cause in the system", "Procedure"], [
      ["The room humidity does not decrease", "The light and the transpiration cause more water than your dehumidifier can remove", "Add dehumidification capacity, or decrease the light. Also increase the air exchange."],
      ["Leaf curl at the edges, at high light", "The cause is frequently light, leaf heat, and VPD together, and not only VPD", "First, examine the PPFD and the leaf temperature. Then examine the VPD (use a lower temperature and more humidity). Add CO2. Make sure that the airflow is correct."],
      ["A high light intensity and a low yield", "The climate, the CO2, and the water did not increase with the light", "Set the CO2, the VPD, and the feed for the light intensity"],
      ["Hot canopy, slow growth", "The airflow is too weak, and the leaf cannot release heat", "Increase the air movement at the canopy"],
      ["Bud rot in week 6 and the weeks after it", "A canopy with a high density and humidity that stays in the canopy", "Defoliate the plants and increase the space between them. Increase the airflow through the canopy. Decrease the RH."],
    ], cls="compact"),
  ]})

SECTIONS.append({"id": "expect", "kicker": "11 · Facts and limits", "title": "Expected results and limitations",
  "blocks": [
    callout("key", "Three procedures that keep the system in balance",
      ul(["Think in <strong>groups</strong>: when you change one input, find the other inputs that must change with it.",
          "<strong>Balance the inputs. Do not use the maximum.</strong> A balanced room at moderate light gives a better result than a bright room with a climate that cannot agree with the light." + _c("collado2025-light"),
          "The substrate and the cultivar change the correct value. Use the numbers from the references as start points only."])),
    p("Next, read the papers on <a href='coco-crop-steering.html'>crop steering</a>, <a "
      "href='airflow-design.html'>airflow</a>, and <a href='mould-risk.html'>mold</a>. They are "
      "parts of this system."),
  ]})
