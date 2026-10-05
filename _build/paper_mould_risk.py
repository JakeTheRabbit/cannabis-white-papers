# -*- coding: utf-8 -*-
"""Paper: mould risk, preventing and stopping bud rot (beginner)."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        stagecard, grid, card, chip, kv, steps)
import figs_lib as L
from figs import GL, GXL, AMBL, REDL, BLUL

SLUG = "mould-risk"
TITLE = "Mold risk: how to prevent and stop bud rot"
EYEBROW = "Basic · Mold risk"
SUB = ("Mold is the disease with the highest risk of damage to all the crop in the last weeks. It "
       "can also make your flower dangerous to use. This paper shows the conditions that mold must "
       "have, how to prevent these conditions, and the procedure to use immediately when you find "
       "mold.")
META = [("shield", "Basic"), ("image", "3 diagrams"),
        ("quote", "10 sources"), ("clock", "~15 min to read")]
RELATED = ["grow-room-systems", "airflow-design", "tissue-culture"]
REF_IDS = ["punja-budrot-cjb", "punja2025-budrot-epi", "scott2021-pm", "buirs2024-idm",
           "mckernan2016-micro", "alubeed2022-postharvest", "sun2025-drying",
           "benedict2020-cdc", "gwinn2023-mycotoxin", "punja2019-pathogens"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

SECTIONS.append({"id": "start", "kicker": "01, Read this first", "title": "Purpose and scope",
  "blocks": [
    lead("You can do all the tasks correctly for ten weeks, and then in the last two weeks gray "
         "mold causes damage to all the crop. Mold increases most quickly in warm air with a high "
         "humidity and in a canopy with a high density of flowers. The same conditions also make "
         "large buds. The mold is most dangerous in the <em>inner</em> part of the bud. You cannot "
         "see the mold there until it increases in size."),
    p("There is also a risk to health. One set of claims data shows that persons who use cannabis "
      "have fungal infections approximately <strong>3.5× more frequently</strong> than persons who "
      "do not use cannabis. The absolute rates are small, and persons with a weak immune system "
      "have the highest risk" + _c("benedict2020-cdc") + ". Some molds make mycotoxins that stay in "
      "the flower after drying" + _c("gwinn2023-mycotoxin") + ".</p><p>The mold risk is not only "
      "about yield. It is also about safe medicine. It is not necessary to know about mold before "
      "you read this paper. The paper gives the definition of each term."),
  ]})

SECTIONS.append({"id": "terms", "kicker": "02, The terms", "title": "Definitions",
  "blocks": [
    defterm("Bud rot (Botrytis)", "<em>Botrytis cinerea</em> is a gray mold. It causes rot in the "
            "flowers, from the inner part to the external part. It is the primary cause of damage "
            "to the crop in the last part of flowering."),
    defterm("Powdery mildew (PM)", "A white fungus on the surface of leaves, with a layer of "
            "powder. It is a different fungus with different symptoms, but it is also a very bad "
            "problem."),
    defterm("Relative humidity (RH)", "Air can contain only a maximum quantity of water vapor, and "
            "water starts to condense on cold surfaces at this limit. RH shows how near the air is "
            "to this limit, as a percentage. An RH of 100% shows that the air is at the limit. An "
            "RH of 50% shows half of the limit. Keep the RH in flowering rooms in the range of "
            "45–65%. When the RH is more than 70%, the risk of bud rot increases quickly."),
    defterm("Wet leaf / free moisture", "Liquid water on the plant, from condensation or from "
            "spray. Many mold spores must have this water to germinate."),
    defterm("Water activity", "Dry flower also contains moisture, but mold cannot use all of this "
            "moisture. The sugars, the salts and the cell walls hold some of the moisture. This "
            "moisture is in the flower, but it cannot move. Water activity (Aw) measures only the "
            "free fraction, on a scale of 0 to 1. When Aw is less than approximately 0.65, most "
            "molds cannot increase in number. If you cure the flower and keep it in storage at an "
            "Aw less than this threshold, the risk of storage mold is very small."),
    defterm("Mycotoxin", "A poison that some molds make, for example <em>Aspergillus</em>. It can "
            "stay in the flower, also when there is no mold" + _c("gwinn2023-mycotoxin") +
            "."),
  ]})

SECTIONS.append({"id": "the-two", "kicker": "03, Two disease types", "title": "Frequent mold diseases of cannabis",
  "blocks": [
    grid([
      card("Bud rot, Botrytis", p("Bud rot starts deep in a cola with a high density, frequently at "
        "a stem or where a leaf attaches to the bud. One leaf has a yellow or brown color, and you "
        "can pull it from the bud easily. The inner part of the bud is gray and soft, and it breaks "
        "into small pieces. Bud rot increases quickly in the last weeks" + _c("punja-budrot-cjb") +
        "."),
        tag="Inner part of the bud"),
      card("Powdery mildew, PM", p("PM makes white areas of powder on the top of the leaves. You "
        "can rub the leaf to remove the powder, but then the powder is on the leaf again. PM is "
        "most frequent at moderate temperatures, and in air with a high humidity that does not "
        "move. PM makes a layer on the leaves and decreases photosynthesis" + _c("scott2021-pm") +
        "."), tag="On the leaves"),
    ], cols=2),
    callout("note", "Other mold species in grow rooms",
      p("Cannabis in grow rooms can also have <em>Penicillium</em>, <em>Cladosporium</em>, "
        "<em>Fusarium</em> and <em>Aspergillus</em>" + _c("punja2019-pathogens") +
        ". Botrytis and PM are the two species that you will see first and most frequently.")),
  ]})

SECTIONS.append({"id": "conditions", "kicker": "04, Causes and conditions", "title": "Conditions that help mold",
  "blocks": [
    p("Bud rot does not occur at random. It must have a set of conditions. The humidity is more "
      "than approximately <strong>70%</strong>, the temperatures are moderate (approximately "
      "17–24&nbsp;°C (63–75&nbsp;°F)), and there is free moisture on the surfaces of the plant. The "
      "air also does not move" + _c("punja2025-budrot-epi") + ". If you remove one of these "
      "conditions, you prevent the mold."),
    figure(L.zones("Bud-rot risk increases with humidity", 40, 90,
            [(40, 60, GL, "low risk"), (60, 70, GXL, "monitor"),
             (70, 80, AMBL, "high risk"), (80, 90, REDL, "rot is very possible")],
            unit="% RH",
            note="Canopy humidity, not only the room average. Keep flowering rooms in the green or monitor band."), 1,
      "The risk increases quickly at more than approximately 70% RH" + _c("punja2025-budrot-epi") +
      ". The room sensor can show 60% when the humidity in a large cola is much higher."),
    figure(L.flow("How bud rot starts",
            [("Spore comes to bud", "high humidity, no air movement"), ("Germinates", "must have high RH and moisture"),
             ("Inner growth", "rot in the bud, no sign"), ("Makes spores", "gray mold, moves in the air")],
            note="When you see gray mold, the spores are in the air. Prevent the conditions before the mold starts."), 2,
      "The steps of the infection. Almost all of the steps occur where you cannot see them. Thus it "
      "is better to prevent mold than to apply a treatment" + _c("punja-budrot-cjb") +
      "."),
    callout("danger", "The problem of a canopy with a high density",
      p("If the canopy has a high density and no defoliation, warm air with a high humidity stays "
        "in the canopy. The air does not move, and the microclimate is much wetter than the reading "
        "of the room sensor" + _c("punja-budrot-cjb") + ". If you put the plants near each other to "
        "increase the yield, the risk of rot increases. Defoliation and space between the plants "
        "are good methods to control mold. They change the airflow and the humidity of the canopy.")),
  ]})

SECTIONS.append({"id": "prevention", "kicker": "05, Steps to prevent mold", "title": "How to prevent mold each day",
  "blocks": [
    p("To prevent mold, do a small number of easy tasks with the same procedure each time:"),
    steps([
      ("Keep the humidity low", "Keep the RH in flowering at approximately 45–65%, with a value that is correct for the stage. In the middle and last parts of flowering, the value is frequently approximately 45–55%. Use a lower value in the last part. Select a size for the dehumidifier that is correct for the transpiration load" + _c("buirs2024-idm") + "."),
      ("Move air through the canopy", "Make a weak airflow with turbulence. Make the air move at approximately 0.5–1.0 m/s in the plants and not only above the canopy" + _c("buirs2024-idm") + ". Read the airflow paper."),
      ("Open the canopy", "Defoliate the plants and make space between the plants. Thus air and light go into the canopy. A high plant density increases the other risks, and you cannot see this effect."),
      ("Prevent free moisture", "Do not apply water from above and do not spray the plants in flowering. Prevent condensation at lights-off. Do not let the temperature decrease by a large quantity. Then the surface temperatures stay higher than the dew point."),
      ("Keep the room clean", "Sanitize the tools, the surfaces and your hands. Use a HEPA filter on the air that comes into the room. Thus the number of spores in the air decreases" + _c("buirs2024-idm") + "."),
      ("Scouting each day", "In the last weeks, examine the plants each day. If you find one bud with rot at the first stage, you can prevent damage to all the other buds."),
    ]),
  ]})

SECTIONS.append({"id": "scouting", "kicker": "06, Scouting each day", "title": "Scouting to find mold at the first stage",
  "blocks": [
    p("Each day in the last part of flowering, use a bright light for five minutes. Look "
      "<em>into</em> the plants and not only at the plants:"),
    ul([
      "<strong>The first sign.</strong> One leaf blade comes out of a bud. The leaf is yellow or "
      "brown, and you can pull it from the bud easily. Pull the leaf from the bud, and examine the "
      "bud below it for gray mold.",
      "<strong>Where to look.</strong> Examine the largest colas at the top, which have the highest "
      "density. Examine the positions where a leaf petiole goes into the bud. Examine all the "
      "positions where the airflow is weak.",
      "<strong>Powdery mildew.</strong> White powder on the top surfaces of the leaves. You can rub the leaf to remove the powder.",
      "<strong>Smell the plants.</strong> Before you can see the rot, the plants can smell of mold, smell of hay, or smell different from usual.",
    ]),
  ]})

SECTIONS.append({"id": "when-found", "kicker": "07, Control of damage", "title": "Procedure when you find mold",
  "blocks": [
    steps([
      ("Stop and contain the mold", "Do not move air onto the mold. Put a bag around the bud with rot. Cut the stem at a large distance below the rot. Remove the bag from the room before you open the bag."),
      ("Cut a large area", "The area of bud rot in the bud is larger than the area that you can see. Remove the full bud with rot and some tissue in good condition around it."),
      ("Sanitize", "Clean your tools and your hands before you touch a different plant. Spores can move on tools, surfaces and hands."),
      ("Remove the cause", "When you find rot, the conditions of humidity, airflow or density are not correct. Decrease the RH. Make more airflow through the canopy. Open the canopy."),
      ("Think about the time of harvest", "If the rot increases quickly in the last part of flowering, harvest the clean material before the usual time. This harvest can be better than damage to all the crop."),
    ]),
    callout("warn", "Do not try to make flower with rot safe with a &lsquo;treatment&rsquo;",
      p("A bud with rot is waste. Drying decreases the quantity of microbes, but it does not remove "
        "the rot or the mycotoxins" + _c("sun2025-drying") + ". No procedure makes the bud safe to "
        "use.")),
  ]})

SECTIONS.append({"id": "drying", "kicker": "08, After harvest", "title": "How to prevent mold during drying and storage",
  "blocks": [
    p("Mold can occur in clean flower during a drying procedure that is not correct, or in storage. "
      "The protection is to decrease the quantity of available water:"),
    ul([
      "<strong>Dry the flower in controlled conditions:</strong> cool and moderate, with airflow. "
      "Drying decreases the number of yeasts and molds by a large quantity" + _c("sun2025-drying") +
      ".",
      "<strong>Cure and keep the flower dry.</strong> Make the water activity low and stable. A "
      "cure at approximately 18&nbsp;°C (64&nbsp;°F) and approximately 50–55% RH is a target with a "
      "source in the literature" + _c("alubeed2022-postharvest") + ".",
      "<strong>Glass is better than plastic.</strong> Sealed glass jars give better results than "
      "bags: they keep the quantity of microbes low and the cannabinoids stable" + _c("sun2025-drying") +
      ".",
    ]),
  ]})

SECTIONS.append({"id": "health", "kicker": "09, Health risk", "title": "Limits of a visual inspection for mold",
  "blocks": [
    p("Flower can have dangerous fungi when it looks clean, smells clean, and also when a "
      "<em>test</em> shows that it is clean. A standard test for mold with a culture cannot always "
      "find some <em>Aspergillus</em> that make mycotoxins" + _c("mckernan2016-micro") +
      ". The rates of contamination in commercial products are high, and the regulations are not "
      "the same" + _c("gwinn2023-mycotoxin") + "."),
    callout("key", "The most important information about safety",
      p("The tasks to prevent mold in the grow room are your primary protection for safety. A "
        "laboratory test is a second protection. It has limits, and it does not make you sure that "
        "the flower is safe. For persons who are at high risk, cannabis with mold is a risk to "
        "health" + _c("benedict2020-cdc") + ". Thus clean genetics (read <a "
        "href='tissue-culture.html'>tissue culture</a>) and a clean room are important from the "
        "first day.")),
  ]})

SECTIONS.append({"id": "trouble", "kicker": "10, Reference", "title": "Troubleshooting",
  "blocks": [
    table(["Symptom", "Possible cause", "Correction"], [
      ["The inner part of the bud is gray and soft, and it breaks into small pieces", "Botrytis bud rot", "Put a bag around the mold. Cut a large area. Remove the bag from the room. Sanitize the tools and your hands. Decrease the RH and increase the airflow."],
      ["White powder on the top of the leaves", "Powdery mildew", "Increase the airflow and decrease the RH. Remove the leaves with the most powder. Apply a treatment at the first stage" + _c("scott2021-pm")],
      ["Rot occurs in each crop cycle in the last part of flowering", "A high humidity in the canopy for a long time, or plants with a high density", "Use a dehumidifier with a larger capacity. Defoliate the plants. Make an airflow through the canopy."],
      ["Condensation at lights-off", "Surfaces that become colder than the dew point when the temperature decreases at night", "Make the temperature decrease by a smaller quantity at night. Keep the air in movement."],
      ["Mold in the jars after the cure", "The flower is too wet when you put it in storage", "Dry or cure the flower to decrease the water activity. Use sealed glass jars" + _c("alubeed2022-postharvest")],
    ], cls="compact"),
  ]})

SECTIONS.append({"id": "expect", "kicker": "11, Important facts", "title": "Expected results and limitations",
  "blocks": [
    callout("key", "Important facts",
      ol(["Mold must have a <strong>set of conditions (humidity + air that does not move + density + moisture)</strong>. If you remove one condition, you remove the risk.",
          "The mold is in the <strong>inner</strong> parts of the buds. When you can see it, the spores are in the air. Examine the plants each day in the last part of flowering.",
          "<strong>You cannot make flower with rot or mycotoxins safe after the damage occurs.</strong> No treatment removes mycotoxins or makes a bud with rot good again" + _c("sun2025-drying") + ".",
          "<strong>Cannabis can have dangerous contamination when it looks clean, smells clean and a test shows that it is clean</strong>" + _c("mckernan2016-micro") + "."])),
    p("Mold risk is a result of your climate and your airflow. Read the <a "
      "href='grow-room-systems.html'>systems paper</a> and the <a "
      "href='airflow-design.html'>airflow</a> paper. They show how to remove the causes and not "
      "only the symptoms."),
  ]})
