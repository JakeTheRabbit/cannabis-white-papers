# -*- coding: utf-8 -*-
"""Paper: mother plants & stock-plant management — running a cutting factory that never runs dry."""
import json, os
from components import (p, lead, h, ul, ol, callout, defterm, table, figure, grid, card, chip, kv, steps)
import figs_lib as L

_FIGS = json.load(open(os.path.join(os.path.dirname(__file__), "figs_mother_plants.json"), encoding="utf-8"))

SLUG = "mother-plants"
TITLE = "Mother plants: environment, feed, pruning and protection against pathogens"
EYEBROW = "Propagation · Stock"
SUB = ("This paper gives information about the environment, feed, pruning, protection against "
       "viroid, tests and replacement of plants in a cannabis mother bank. After you read this "
       "paper, you will know how to prepare a mother room and schedule the cuttings. You will also "
       "know how to prevent an infection of your stock with hop latent viroid.")
META = [("seedling", "Propagation"), ("image", "13 diagrams"),
        ("quote", "14 sources"), ("clock", "~20 min to read")]
RELATED = ["cloning", "tissue-culture"]
REF_IDS = ["mp-ahrens-2023-photoperiod", "mp-saloner-2020-nitrogen", "mp-tumi-hlvd-testing",
           "mp-moher-2022-veg-light", "mp-druege-2004-stockplant-n", "mp-caplan-2018-cuttings",
           "mp-adamek-2022-mosaicism", "mp-adamek-2024-subcultures", "mp-punja-2025-hplvd-mgmt",
           "mp-warren-2019-hplvd-ca", "mp-adkar-2023-hidden-threat", "mp-medgen-hlvd",
           "mp-monthony-2021-tc", "mp-kurtz-2022-retip"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

# ---------------------------------------------------------------- 01 start here
SECTIONS.append({"id": "start-here", "kicker": "01 · Start here",
  "title": "Purpose and scope",
  "blocks": [
    lead("A <strong>mother plant</strong> is a plant that you keep permanently in vegetative growth "
         "(growth of leaves). The plant does not make flowers. The only task of the plant is to "
         "supply <strong>cuttings</strong> at the correct times. A cutting is a copy of the mother "
         "plant and has the same genetics. Each plant that goes into your flower room started as a "
         "piece of a mother plant."),
    p("The name in horticulture is <strong>stock plant</strong>. Growers use the name mother plant. "
      "For a mother plant or a stock plant, you keep one plant out of production. You use light, "
      "space and work for this plant. As a result, all the plants of a batch are the same. You know "
      "the genetics of the plants, and the plants are available on time.</p><p>All the mother "
      "plants of a facility are the <strong>mother bank</strong>."),
    p("The mother plant is upstream of all other plants. Thus it is important to do the work with "
      "mother plants correctly. If a mother plant is weak, has a disease or has an incorrect label, "
      "the problem is not in one plant only. The problem is in each cutting that the mother plant "
      "supplies.</p><p>Usually you find the problem after some weeks or months. At that time, the "
      "problem is in all the plants of a room. A problem in a mother plant is small and has no "
      "signs at first. When you can see the problem, the damage can be very large."),
    figure(L.flow("From mother bank to flower crop",
            [("Mother bank", "tests, vegetative"), ("Cut", "a batch each 2–3 weeks"),
             ("Rooting", "10–14 days"), ("Vegetative", "2–4 weeks"), ("Flower", "the room for harvest")]), 1,
      "The figure shows the propagation system. Each stage downstream gets the vigor and the "
      "genetics of the mother plant. Each stage also gets each pathogen that the mother plant has, "
      "with or without symptoms."),
    callout("note", "Who this is for",
      p("This paper is for growers who keep a first mother plant and for operators of a stock room "
        "who schedule production. The paper is about the plant that you cut <em>from</em>. The <a "
        "href='cloning.html'>cloning paper</a> gives information about the cutting method (blades, "
        "gel, domes and humidity). The <a href='ipm-sop.html'>IPM hygiene</a> paper shows how to "
        "keep the room clean.")),
  ]})

# ---------------------------------------------------------------- 02 vocabulary
SECTIONS.append({"id": "vocab", "kicker": "02 · The terms",
  "title": "Definitions",
  "blocks": [
    p("The terms for a mother room are from horticulture, virology and production control. This "
      "section gives the definitions of eight terms. The paper gives the definition of each other "
      "term where the term first occurs."),
    defterm("Mother plant / stock plant", 'A plant that you keep permanently in vegetative growth (growth '
            'of leaves). The plant does not make flowers. You keep the plant only as a source of '
            'cuttings. "Mother plant" and "stock plant" are two names for the same plant.'),
    defterm("Photoperiod", "The number of hours of light in each day. Photoperiod cannabis starts "
            "to make flowers when the nights become long. You keep mother plants on long days with "
            "18 h of light. Thus the mother plants do not start to make flowers."),
    defterm("PPFD", "Photosynthetic photon flux density. PPFD is the quantity of light that the "
            "leaves receive and can use, in µmol·m⁻²·s⁻¹. Use a moderate PPFD for mother plants. Do "
            "not use the PPFD of a flower room."),
    defterm("Node", "The point on a stem where the leaves and the side shoots attach. You cut the "
            "stem at a position in relation to a node. A stub is the part of the stem that stays on "
            "the plant after you cut the stem. A stub that has a node can make new shoots."),
    defterm("EC", "Electrical conductivity of the feed water, in mS/cm. EC is an indicator of the "
            "total strength of the nutrients in the water. Use a moderate EC for mother plants. A "
            "high EC causes soft growth that contains a large quantity of salt."),
    defterm("Viroid", "The smallest known agent of infection. A viroid is a bare loop of RNA "
            "without a protein coat. The size of a viroid is a fraction of the size of a virus. Hop "
            "latent viroid (HpLVd) is the viroid that is important in cannabis."),
    defterm("Dudding", "The disease that HpLVd causes. The plants show no symptoms at first. At "
            "harvest, the plants are small and weak and they break easily. The plants have a low "
            "density of trichomes and a much lower potency."),
    defterm("Indexing", "A procedure in which you do tests on stock plants for pathogens at regular "
            "intervals. A clean result is a result in which the test finds no pathogen. A positive "
            "result is a result in which the test finds a pathogen. Thus each clean result shows "
            "the condition of the plant at this time. The procedure is from the horticulture of "
            "certified clean stock."),
  ]})

# ---------------------------------------------------------------- 03 core answer
SECTIONS.append({"id": "core-answer", "kicker": "03 · The important items",
  "title": "Mother-plant procedures in one table",
  "blocks": [
    lead("The table below shows each procedure that is important for a mother bank with a constant supply of cuttings. Sections 04 to 16 give the data and more information for each row."),
    kv([
      ("Photoperiod", "18 h of light and 6 h of darkness. Make sure that the photoperiod is always correct. Some cultivars start to make flowers at photoperiods as long as 14 to 15 h" + _c("mp-ahrens-2023-photoperiod") + ". Thus an 18 h photoperiod is safe because it is longer than this limit."),
      ("Light", "Moderate: approximately 300 to 500 µmol·m⁻²·s⁻¹ PPFD. This PPFD is sufficient for stable regrowth. A higher PPFD can make the shoots short and thick."),
      ("Feed", "Use a feed for vegetative growth with a high nitrogen content. The optimum from a test is approximately 160 mg/L N" + _c("mp-saloner-2020-nitrogen") + ". Use a moderate EC of approximately 1.4 to 2.0 mS/cm (grower method). Do not cause soft growth."),
      ("Shape", "A flat and wide canopy with an open middle. The permanent frame has 4 to 6 scaffolds (primary branches). Harvest the vertical shoots at an interval of 2 to 3 weeks."),
      ("Harvest procedure", "Harvest a maximum of approximately half of the shoots each time. Cut above the first node. Then each stub makes two new shoots."),
      ("Testing", "Do an HpLVd qPCR test on root tissue of each mother plant at an interval of 4 to 6 weeks" + _c("mp-tumi-hlvd-testing") + ". Put new genetics in quarantine. Before the new plants go into the mother bank, do two tests."),
      ("Tools", "Use a new blade or a sanitized blade for each plant, each time. The blade is the primary method by which HpLVd moves from one plant to the next plant. HpLVd can cause the end of a mother room."),
      ("Replacement", "Replace a mother plant because of data: a positive result of a test or a rooting rate that decreases. Do not replace a mother plant only because of its age. Always use an overlap of the replacement plant and the mother plant that you replace."),
      ("Second copy", "Keep two copies of each cultivar that is important to you, if possible in different rooms or in tissue culture."),
    ]),
    p("These five procedures are the most important:"),
    ol([
      "<strong>Make the photoperiod longer than the photoperiod at which flowers start.</strong> Tests show that cultivars start to make flowers at photoperiods as long as 14 h, and some cultivars start at 15 h" + _c("mp-ahrens-2023-photoperiod") + ". The 18/6 photoperiod lets the mother plants stay in vegetative growth when there is a timer fault or a light leak.",
      "<strong>Give feed for rigid shoots, not for large dark green leaves.</strong> The target is rigid regrowth with thick stems. A plant with too much feed has dark green leaves that hang from the stems. The cuttings of this plant show wilt and stop growth.",
      "<strong>Make the frame one time, then harvest the regrowth.</strong> The shape of the plant has more effect on the number of cuttings than the feed or the light.",
      "<strong>Think that hop latent viroid can infect your stock.</strong> In a report on California facilities, approximately 90% of the facilities had the viroid" + _c("mp-adkar-2023-hidden-threat") + ". Use a correct procedure for blades. Do tests at regular intervals. These two procedures are the complete protection.",
      "<strong>Replace because of data, and use an overlap.</strong> Keep the replacement plant together with the mother plant that you replace. Do not discard the mother plant that you replace before the data show that the replacement plant is satisfactory.",
    ]),
    callout("key", "The primary task",
      p("Keep a plant with known genetics and a clean test result in permanent vegetative growth. "
        "The plant must supply a constant quantity of cuttings each week. Make sure that you always "
        "know the correct condition of the plant.")),
  ]})

# ---------------------------------------------------------------- 04 the room
SECTIONS.append({"id": "room-setup", "kicker": "04 · Method and data",
  "title": "Mother-room environment",
  "blocks": [
    p("The photoperiod is the most important control in a mother room. Photoperiod cannabis starts "
      "to make flowers when the period of darkness is sufficiently long. The threshold photoperiod "
      "is longer than most growers think.</p><p>In a test with six photoperiods, all the cultivars "
      "started to make flowers at photoperiods as long as 14 h. Some cultivars started at 15 h" +
      _c("mp-ahrens-2023-photoperiod") + ". The 18 h photoperiod has no special value. It is 3 to 4 "
      "h longer than the longest photoperiod at which the plants start to make flowers."),
    p("If a mother plant starts to make flowers, the result is a large problem. The change back to "
      "vegetative growth is slow. It is a waste of some weeks. The regrowth has a twisted shape. "
      "Cuttings that you cut while the plant changes to the flowering stage make roots irregularly "
      "and increase in size irregularly.</p><p>Photoperiod faults in mother rooms are accidental. "
      "There are three causes. A timer output does not operate. A contactor stays in the off "
      "position. Light comes through a door from a flower room next to the mother room.</p><p>Do a "
      "check of the period of darkness each month. Stay in the room for five minutes with the "
      "lights off. Repair each light leak that you can see."),
    p("Two photoperiods are in frequent use in mother rooms: 18/6 and 24/0 (continuous light). The "
      "first number is the hours of light, and the second number is the hours of darkness. The two "
      "photoperiods keep photoperiod cultivars in vegetative growth. Continuous light uses "
      "approximately one third more energy.</p><p>Some growers think that a period of darkness is "
      "good for root growth and for the condition of the plant after the harvest of cuttings. The "
      "data are weak. They do not show that a period of darkness helps or does not help. Thus the "
      "data do not show a fact, and you can select one of the two photoperiods. The 18/6 "
      "photoperiod is the usual selection because it is sufficient and it uses less "
      "energy.</p><p>There is one important limit: <strong>you cannot use autoflower genetics for "
      "mother plants</strong>. Autoflower plants start to make flowers because of their age, not "
      "because of the photoperiod. No photoperiod can stop this effect."),
    figure(L.zones("Light target, mother room", 0, 800,
            [(0, 150, L.REDL, "too low"), (150, 300, L.AMBL, "slow"),
             (300, 500, L.GL, "target"), (500, 650, L.GXL, "small effect"),
             (650, 800, L.AMBL, "no effect")],
            unit="",
            note="Canopy PPFD in µmol·m⁻²·s⁻¹. Grower method. The paper gives references for this target."), 2,
      "Moderate light is the correct selection for a mother plant. The target is regrowth that you "
      "can cut. A PPFD of 300 to 500 µmol keeps the shoots sufficiently long to cut and "
      "sufficiently thick to make roots."),
    p("Use a moderate PPFD for a mother plant, not the PPFD of a flower room. Vegetative cannabis "
      "can use much more light. In a test with PPFD values from 135 to 1430 µmol, the growth "
      "continued to increase when the light increased. But light also changes the shape of the "
      "plant. When the light intensity increases, the length of the internodes and the size of the "
      "leaves decrease gradually" + _c("mp-moher-2022-veg-light") + ".</p><p>If you use more than "
      "900 µmol for a mother plant, the regrowth is short and thick, and the internodes are short. "
      "A plant with short internodes is good for production. But it is not easy to cut shoots of "
      "8–15 cm (3–6 in) from this plant.</p><p>If you use less than approximately 150 µmol, the "
      "shoots are thin and weak, and they have long internodes. These shoots have a low quantity of "
      "carbohydrate and a low rooting rate. A PPFD of 300 to 500 µmol is the correct range. In this "
      "range, the regrowth is fast <em>and</em> has the correct shape for cuttings."),
    p("The climate in a mother room is usual. The values are grower methods. When the lights are "
      "on, use approximately 22 to 26 °C (72 to 79 °F). Use approximately 55 to 70% relative "
      "humidity. Use a small, continuous movement of the air.</p><p>The mother room must be the "
      "most stable room in the facility. Stress in the mother room causes a batch of cuttings with "
      "a rooting rate of 60% and not 90%. The effect occurs after two weeks. It is not easy to find "
      "the connection between the stress and the rooting rate."),
  ]})

# ---------------------------------------------------------------- 05 feeding
SECTIONS.append({"id": "nutrition", "kicker": "05 · Method and data",
  "title": "Mother-plant nutrition",
  "blocks": [
    p("The nutrition of a mother plant has a different target from the nutrition of a flower plant. "
      "The target is not buds, and it is not a large plant. The target is <em>stems and growing "
      "tips</em>. The plant makes them continuously from the same root system for months. Thus use "
      "a feed for vegetative growth with a high nitrogen content and a moderate strength."),
    p("A test gives data for the nitrogen value. The test used five doses of nitrogen on medical "
      "cannabis with long days. The optimum for vegetative growth was <strong>160 mg/L N</strong>. "
      "At 30 mg/L N, the plants had a large nitrogen deficiency, stayed small and became yellow. At "
      "240 to 320 mg/L N, the growth decreased, and the plants were smaller and dark green. The "
      "plants showed typical signs of too much nitrogen" + _c("mp-saloner-2020-nitrogen") +
      ".</p><p>More nitrogen does not make more shoots. The growth is at a maximum at a nitrogen "
      "value that is less than the value in most feed charts."),
    p("<strong>The primary limit for the rooting of a cutting is carbohydrate, not "
      "nitrogen.</strong> A test of stock plants showed that the quantity of carbohydrate in the "
      "cutting is the primary limit for rooting. Nitrogen is a secondary limit" +
      _c("mp-druege-2004-stockplant-n") + ".</p><p>A mother plant with too much feed makes soft "
      "shoots that contain much water and are dark green. The leaves are large and hang from the "
      "stems, and the stems have a hole in the middle. These cuttings show wilt in the dome and "
      "make roots only after a long time, or do not make roots. The correct regrowth is rigid and "
      "thick. The plant can show a small deficiency of feed."),
    figure(L.zones("Feed strength, mother plants", 0.5, 3.0,
            [(0.5, 1.0, L.AMBL, "low"), (1.0, 1.4, L.GXL, "weak"),
             (1.4, 2.0, L.GL, "target"), (2.0, 2.4, L.AMBL, "high"),
             (2.4, 3.0, L.REDL, "soft growth")],
            unit="",
            note="Feed EC in mS/cm (grower method). The values change with the product. The N optimum is from a test."), 3,
      "A moderate EC keeps the regrowth rigid. When the EC is more than approximately 2.4 mS/cm, "
      "most mother plants change to soft growth. This growth has a low rooting rate. The plant can "
      "look better, but the rooting rate of the cuttings is lower."),
    table(["Item", "Range for use", "Source"], [
      ["Nitrogen", "150–200 mg/L, with the middle at approximately 160", "Optimum from a test with different doses" + _c("mp-saloner-2020-nitrogen")],
      ["Feed EC", "1.4–2.0 mS/cm", "Grower method. Monitor the plant, not the chart."],
      ["pH", "5.8–6.2 (coco / rockwool)", "Grower method"],
      ["Irrigation", "Stable, small drybacks. No cycles of drought.", "Stress at this time causes a low rooting rate after 2 weeks"],
      ["The day before a harvest", "Apply sufficient water. Do not apply foliar sprays.", "Shoots that are full of water and have dry leaves are easy to use and have the highest rooting rate."],
    ], cls="compact", caption="The table shows the feed of a mother plant. Only the nitrogen row has a value from a test. The other rows are grower methods."),
    callout("tip", "Monitor the mother plant, not the chart",
      p("The correct feedback for the mother plant is the <strong>rooting rate of its cuttings, "
        "batch after batch</strong>. If the rooting rate decreases in two or three batches, and "
        "pests and viroid are not the cause, examine the feed first. The correction is usually "
        "<em>less</em>: less N, less EC, and more rigid shoots.")),
  ]})

# ---------------------------------------------------------------- 06 architecture
SECTIONS.append({"id": "architecture", "kicker": "06 · Do this",
  "title": "Shape and regrowth of the mother plant",
  "blocks": [
    p("The shape of the plant has more effect on the number of cuttings than the vigor of the "
      "plant. A mother plant with no pruning makes one top shoot that is much larger than the side "
      "shoots. It also makes a small number of weak side shoots. This shape gives a low number of "
      "cuttings. Growers of fruit and hedge plants use the same method. They remove the top shoot "
      "in the first weeks, make the plant wide, and keep the plant flat."),
    p("The top shoot makes a hormone. The hormone flows down in the stem and prevents the growth of "
      "each side shoot below it. This effect is <strong>apical dominance</strong>: the top bud "
      "controls the growth of each node below it. When you cut the top of the shoot "
      "(<strong>topping</strong>), the quantity of hormone decreases. Then each side shoot that is "
      "below the top starts to increase in size at the same time.</p><p>Cut the top of the young "
      "plant one time. Then cut the top of each side shoot that starts to increase in size one "
      "time. As a result, you change one growing point into eight to twelve growing points. These "
      "growing points become the <strong>permanent frame</strong>. All the shoots above the frame "
      "are crop."),
    steps([
      ("Start (weeks 0–2)", "Start with your best clone that has a <em>clean test result</em>. The mother plant has all the properties of the clone, good and bad. Transplant the clone. Give the clone time to make roots in the new substrate."),
      ("First topping (week 2–3)", "Cut the top of the plant above node 4 or node 5. As a result, the plant makes 4 to 6 strong side shoots."),
      ("Make the scaffolds (weeks 3–5)", "Select the best 4 to 6 side shoots as permanent scaffolds. Cut the top of each scaffold one time. Then each scaffold divides into two branches. Remove the other side shoots."),
      ("Open the middle (continuous)", "Remove the weak shoots that point to the middle of the plant. Then the middle of the plant receives light and air. A middle that is in shade makes thin, long shoots, and these shoots have the lowest rooting rate."),
      ("First harvest (week 5–6)", "The tips that you remove in the pruning are your first cuttings. After the first harvest, the plant is in production."),
    ]),
    figure(_FIGS["architecture"], 4,
      "The figure shows the shape of a plant in production. The plant has a short stem with a "
      "topping at the young plant stage, 4 to 6 permanent scaffolds, and a flat harvest zone of "
      "vertical shoots. You make the frame one time and you do not cut it. You harvest the shoots "
      "above the frame at an interval of two to three weeks."),
    p("Procedures for the harvest keep the supply of cuttings stable. Cut each shoot <strong>above "
      "its first node</strong>. Then the stub makes two shoots, and the canopy has more shoots at "
      "each harvest.</p><p>Harvest a maximum of approximately half of the canopy at one time. Keep "
      "leaves on each scaffold. A scaffold with no leaves stops growth and does not make new "
      "shoots. The regrowth cycle between full harvests is usually 2 to 3 weeks (grower method)."),
    p("The shoot that you cut must be a good cutting. A test of propagation showed that a cannabis "
      "cutting has the highest rooting rate with <strong>three or more fully expanded leaves on the "
      "cutting</strong>. The same test showed that cutting the tips of the leaves, the usual method "
      "in plant nurseries, decreased the rooting rate from 71% to 53%" + _c("mp-caplan-2018-cuttings") +
      ".</p><p>The test also showed that the position of the shoot on the plant has almost no "
      "effect. Cuttings from top shoots and cuttings from bottom shoots had approximately the same "
      "rooting rate" + _c("mp-caplan-2018-cuttings") + ". Thus harvest the shoots of the canopy, "
      "not only the tips. But let the shoots increase in size until they can have three leaves of "
      "full size."),
    figure(L.line("Output of one middle-size mother after transplant",
            [("w0", 0), ("w2", 0), ("w4", 6), ("w6", 14), ("w8", 22), ("w10", 28), ("w12", 32), ("w14", 34), ("w16", 35)],
            ["w0", "w2", "w4", "w6", "w8", "w10", "w12", "w14", "w16"],
            ylab="cuttings / week", ymax=40,
            note="Approximate curve (grower method). The cultivar and size change it. The frame is complete in approximately 6 weeks."), 5,
      "The first six weeks of a mother plant are for the frame. Include these weeks when you "
      "schedule production. A new mother plant is not a source of cuttings on the first day."),
    callout("note", "Number of cuttings for each mother plant",
      p("No paper gives a good number for this. The number changes with the cultivar, the size of "
        "the pot and the frame. Growers give these estimates: a small mother plant in a pot of "
        "10–15 L (2.6–4.0 gal) gives approximately 15 to 30 cuttings in each harvest. A large "
        "mother plant for production in a pot of 30–50 L (7.9–13.2 gal) can give 50 to 100 cuttings "
        "or more.</p><p>We recommend that you use these estimates as first values and that you "
        "measure your plants. After two months, your records are better than the estimates of other "
        "growers.")),
  ]})

# ---------------------------------------------------------------- 07 scheduling
SECTIONS.append({"id": "scheduling", "kicker": "07 · Do this",
  "title": "Number of mother plants for production",
  "blocks": [
    p("Calculate the number of mother plants. Start at the flower room. Find the number of plants "
      "for each batch and the date when you must have each batch. Then increase the number for the "
      "plants that you do not use.</p><p>Some cuttings do not make roots. Some clones with roots "
      "are not good for the vegetative stage. Thus make 15% to 40% more cuttings than the number of "
      "plants that you must have. The <a href='cloning.html'>cloning paper</a> gives the same value."),
    table(["Step", "Number", "Information"], [
      ["Plants for the flower room", "100", "The number that the room must have"],
      ["Discard in the vegetative stage (approximately 10%)", "keep 110", "Discard the weak and slow clones at transplant"],
      ["Rooting rate (approximately 85%)", "make a minimum of 130", "110 ÷ 0.85. The rooting rate is a correct value, not a value that a supplier gives."],
      ["Increase and add a buffer", "make 140", "The cost of the cuttings that are more than the minimum is small. A flower room that is not full is a waste of one crop cycle."],
    ], cls="compact", caption="The table shows how to calculate the number of cuttings for a batch of 100 plants for the flower room. Change the two percentages in the table to the values that you measure, when you have the values."),
    figure(L.bars("Numbers for 100 flower-room plants",
            [("Cut", 140), ("With roots", 119), ("Vegetative", 110), ("To flower", 100)], unit="",
            note="140 cuttings at 85% rooting ≈ 119. Discard to 110. 100 fill the room, and more are available.",
            maxv=160), 6,
      "It is usual that some plants do not continue at each stage. The numbers in the table include "
      "these plants. The cuttings that are more than the minimum number let you discard many plants "
      "at each stage. Then the flower room is full at the correct time."),
    p("Then divide the number of cuttings for each batch by the output of one mother plant in each "
      "harvest. For example, a middle-size mother plant gives approximately 35 cuttings in each "
      "harvest, and you must have 140 cuttings for each batch. Thus the result is four mother "
      "plants. Use <strong>five</strong> mother plants.</p><p>The fifth mother plant is necessary. "
      "With this plant, you can remove a plant from production. You can keep a plant out of "
      "production for a time. You can put a plant in quarantine. Then you have sufficient cuttings "
      "for each batch."),
    p("Do not harvest all the mother plants at the same time. Divide the mother bank into two "
      "groups, A and B. Harvest group A, then group B, then group A again. Thus you do not harvest "
      "most of the shoots of the same mother plant two times one after the other. Each harvest "
      "stays in the limit of approximately half of the canopy.</p><p>The two groups also give you a "
      "test of the cause of a problem. If the rooting rate of the two groups decreases at the same "
      "time, it is possible that the room is the cause. If the rooting rate of only one group "
      "decreases, it is possible that the plants of that group are the cause."),
    callout("tip", "Cuttings at the correct times are better than many plants",
      p("A small mother bank gives more cuttings than a large number of plants with no correct "
        "procedure. The small mother bank has a correct procedure, tests at regular intervals and "
        "harvests in two groups. Each plant that you add is more work for water, pruning and tests "
        "at regular intervals" + _c("mp-tumi-hlvd-testing") + ". Select the size of the mother bank "
        "because of the dates when the flower rooms must have plants. Do not select a larger size "
        "only for safety.")),
  ]})

# ---------------------------------------------------------------- 08 age & drift
SECTIONS.append({"id": "age-drift", "kicker": "08 · Two views",
  "title": "Mother-plant age and genetic stability",
  "blocks": [
    p("Some growers think that a mother plant becomes worse with time and that you must replace it "
      "each 6 to 12 months. Many operators keep the same mother plant for five years or more. They "
      "think that the plant is the same as at the start. The two groups see an effect that occurs. "
      "But the mechanisms are different."),
    p("<strong>Somatic mutation occurs.</strong> Each time that a cell divides, the cell copies the "
      "DNA, and the copy can have small errors. Each new generation of copies can have an error "
      "that the first plant did not have. In an animal, the reproductive cells stay apart from the "
      "other cells. In a plant, the reproductive cells do not stay apart from the other cells. Thus "
      "a mutation in a growing tip goes into each cutting that you cut from the tip.</p><p>A test "
      "used deep whole-genome sequencing on one cannabis plant. The test measured <strong>genetic "
      "mosaicism</strong> in the plant. The top, the middle and the bottom of the plant did not "
      "have the same genetics" + _c("mp-adamek-2022-mosaicism") + ". Reports from growers show that "
      "clonal lines have lower vigor and lower potency with time. These reports were the cause of "
      "the test" + _c("mp-adamek-2022-mosaicism") + "."),
    p("But the next test changed the view. The test used 70 clones from micropropagation. The "
      "mutation load had an almost linear relation with <strong>the number of propagation "
      "cycles</strong> (r &gt; 0.92). It did <em>not</em> have this relation with the age of the "
      "clones" + _c("mp-adamek-2024-subcultures") + ". Clones of the same age had very different "
      "mutation loads, because they had different numbers of propagation cycles. Each cycle of "
      "cutting and regrowth includes many cell divisions, and the errors in the copies of the DNA "
      "occur when the cells divide."),
    figure(L.line("Mutation load increases with propagation cycles, not with age",
            [("0", 0), ("1", 1), ("2", 2), ("3", 3), ("4", 4), ("5", 5), ("6", 6)],
            ["0", "1", "2", "3", "4", "5", "6"],
            ylab="mutation load (ratio)", ymax=8,
            note="Approximate shape. In micropropagation of cannabis, variants increased linearly with the subculture number (r > 0.92)."), 7,
      "The horizontal axis shows the number of propagation cycles and not the number of months. A "
      "mother plant that you keep for two years, with no new propagation cycle, has a smaller "
      "number of mutations. A sequence of clones from clones, with one cycle each month, has a "
      "larger number." + _c("mp-adamek-2024-subcultures")),
    p("The genome is usually not the cause when a mother plant that you keep for a long time "
      "becomes worse. The causes are usually pathogens that increase in number (refer to the next "
      "two sections). Other causes are a pot that is full of roots, a woody frame that is weak, or "
      "work procedures that change. You can do tests and corrections for each cause, and none of "
      "the causes is age.</p><p>Reports also show epigenetic change in groups of cannabis clones. "
      "Epigenetic change is a change in the expression of genes that goes to the next plants, with "
      "no change in the sequence of the DNA. The data are not sufficient. They do not show that "
      "this change causes lower vigor. Do not use epigenetic change to select the time of "
      "replacement."),
    callout("key", "The decision",
      p("Keep a mother plant when two conditions are correct. (a) The tests show clean results. (b) "
        "In your records, the rooting rate of its cuttings and the performance of the plants "
        "downstream stay stable. Replace a mother plant because of data, not because of a date. "
        "When you make a new mother plant, start with material that has a low generation number and "
        "clean test results. Do not start with material from the far end of a long sequence of "
        "clones from clones" + _c("mp-adamek-2024-subcultures") + ".")),
  ]})

# ---------------------------------------------------------------- 09 pathogen amplifier
SECTIONS.append({"id": "pathogen-risk", "kicker": "09 · The risk",
  "title": "Multiplication of pathogens in mother rooms",
  "blocks": [
    p("Each organism that is in the mother room goes to each room downstream with the cuttings, at "
      "the correct time. The organisms are spider mites, root aphids, fungus gnats, powdery mildew "
      "and root-rot organisms. The mother room is the source that supplies these pests to all other "
      "rooms. Thus the work for IPM in the mother room has an effect in all other rooms (refer to "
      "the <a href='ipm-sop.html'>IPM SOP</a>)."),
    ul([
      "<strong>Blades and cutting tools.</strong> Sap goes from one plant to the next plant on the tool. For the most important pathogen, this movement is the primary method of infection.",
      "<strong>Hands and gloves.</strong> On days when you cut, change the gloves between plants, not between rooms.",
      "<strong>Irrigation with one supply for many plants, or with a recirculating loop.</strong> Tests found pathogens that moved from one plant to the next plant in the nutrient solution and in the runoff" + _c("mp-punja-2025-hplvd-mgmt") + ". Do not connect mother plants to a recirculating loop or a flood table.",
      "<strong>Benches, trays and watering cans.</strong> Tests found viroid RNA on the surfaces of benches and on watering cans in facilities that were in operation" + _c("mp-punja-2025-hplvd-mgmt") + ".",
      "<strong>The cuttings.</strong> The cuttings are the product of the room, and they move the pathogens to all other rooms.",
    ], "tight"),
    p("Three procedures prevent most of the movement of pathogens from one plant to the next plant. "
      "Use <strong>dedicated tools</strong> for mother plants. Do not use these tools in other "
      "rooms. Work in the sequence of the rooms <strong>from clean to dirty</strong>: mother "
      "plants, then vegetative plants, then flower plants. Do not move in the opposite direction "
      "through a dirty room. Sanitize or replace each item that touches sap <strong>between "
      "plants</strong>, not between benches.</p><p>The next section gives information about the "
      "organism that makes these procedures necessary."),
  ]})

# ---------------------------------------------------------------- 10 HpLVd
SECTIONS.append({"id": "hplvd", "kicker": "10 · The primary risk",
  "title": "Hop latent viroid in mother stock",
  "blocks": [
    p("<strong>Hop latent viroid (HpLVd)</strong> is a bare, circular molecule of RNA with a length "
      "of approximately 256 nucleotides. It has no protein coat and no cell. Its size is a fraction "
      "of the size of a virus" + _c("mp-punja-2025-hplvd-mgmt") + ". In 2019, a test in California "
      "first connected HpLVd with defective cannabis crops. Growers use the name "
      "<strong>dudding</strong> for the problem that HpLVd causes" + _c("mp-warren-2019-hplvd-ca") +
      ".</p><p>The plants have no symptoms in the vegetative stage. At harvest, the plants are "
      "small and weak, and they break easily. The plants have a low density of trichomes and a much "
      "lower potency."),
    p("This paper gives much information about HpLVd because the problem is large. A report from "
      "2021 uses data from approximately 200,000 tissue tests. The report shows that approximately "
      "<strong>90% of the cannabis facilities in California</strong> had HpLVd. In the sites that "
      "had HpLVd, approximately 30% of the plants had it" + _c("mp-adkar-2023-hidden-threat") +
      ".</p><p>Reports show that plants with dudding can have a THC content that is 50% to 70% lower" +
      _c("mp-adkar-2023-hidden-threat") + ". An estimate of the industry gives a cost of "
      "approximately US$4 billion for each year" + _c("mp-medgen-hlvd") + ". A test of samples of "
      "flower from dispensaries in Canada found a positive result in approximately 40% of the "
      "samples" + _c("mp-medgen-hlvd") + ". This disease is frequent. It is the usual condition of "
      "stock with no tests."),
    p("The term <em>latent</em> shows the problem: <strong>most infected plants show no "
      "symptoms</strong>" + _c("mp-adkar-2023-hidden-threat") + ". A mother plant is a very good "
      "host for the viroid. The plant stays in the room for a long time, and thus the viroid has "
      "much time to infect it. You cut the plant many times in each year, and thus the sap touches "
      "a tool at each harvest. The plant is upstream of all other plants, and thus each cutting "
      "gets the viroid.</p><p>Tests found the viroid in stock plants with no symptoms and in the "
      "cuttings with roots from these plants" + _c("mp-punja-2025-hplvd-mgmt") +
      ". One infected mother plant with no symptoms supplies infected clones for months, and you "
      "cannot see the infection."),
    figure(_FIGS["hlvd_tools"], 8,
      "The primary method by which the viroid moves is mechanical: sap that can infect goes from "
      "one plant to the next plant on the blade. Sap on tools and surfaces can infect other plants "
      "for approximately 7 days. Sap in dried plant material can infect other plants for a maximum "
      "of 4 weeks" + _c("mp-punja-2025-hplvd-mgmt") + ". A new or sanitized blade for each plant "
      "keeps the infection in one plant."),
    p("Tests measured how HpLVd moves from one plant to the next plant. The primary method is "
      "mechanical: sap and tools move the viroid" + _c("mp-adkar-2023-hidden-threat") +
      _c("mp-punja-2025-hplvd-mgmt") + ". But the viroid also moved <strong>from the roots of one "
      "plant to the roots of the next plant</strong>. This occurred <strong>when the plants had the "
      "same hydroponic nutrient solution, in a maximum of approximately two weeks</strong>. Tests "
      "also found the viroid in recirculating solution, in runoff, on the surfaces of benches and "
      "on watering cans" + _c("mp-punja-2025-hplvd-mgmt") + ".</p><p>When the viroid went into a "
      "stem that a tool cut, it went to the roots in 2 to 3 weeks and to the leaves only after 4 to "
      "6 weeks" + _c("mp-punja-2025-hplvd-mgmt") + ". Thus a test of a leaf can give a clean result "
      "for a plant with a new infection. Thus you must use samples of roots and do the test again "
      "(refer to the next section)."),
    figure(L.hbars("Worst effect of dudding (reports)",
            [("THC content", 70), ("Cannabinoid production", 50), ("Terpene production", 50)],
            unit="%", note="Highest values of ranges in reports, for plants with dudding compared with clean plants."), 9,
      "The figure shows the effect of infection at harvest. Reports show that the THC content of an "
      "infected plant can be lower by 50% to 70%. The production of cannabinoids and terpenes can "
      "be lower by a maximum of half. The plant had no symptoms when it was a source of cuttings." +
      _c("mp-adkar-2023-hidden-threat")),
    p("The best procedure for tools is <strong>a new blade that you use one time for one mother "
      "plant</strong>. If you cannot use a new blade for each plant, put the blade in 10% household "
      "bleach between plants" + _c("mp-medgen-hlvd") + ". In tests, bleach and hypochlorous acid "
      "broke the RNA of the viroid in sap. Quaternary ammonium compounds and most of the other "
      "sanitizers, which are weaker, did not break the RNA each time" + _c("mp-punja-2025-hplvd-mgmt") +
      ".</p><p>Two facts are important. No disinfectant helps a plant that has an infection. "
      "Discard an infected plant" + _c("mp-punja-2025-hplvd-mgmt") + ". No test shows that "
      "isopropyl alcohol breaks the RNA of the viroid when it is the only treatment. Thus a flame "
      "and alcohol do not prevent infection with the viroid."),
    callout("warn", "Long days show no symptoms and do not stop the viroid",
      p("Do not think that a mother plant is clean because it looks clean. Only a test shows the "
        "difference. In tests, HpLVd moved through the plant <em>more quickly</em> with a 12/12 "
        "flowering photoperiod than with continuous light" + _c("mp-punja-2025-hplvd-mgmt") +
        ". A mother plant with 18 h days can have a low, slow infection that is not easy to find. "
        "The symptoms occur only in the downstream plants in the flowering stage.")),
  ]})

# ---------------------------------------------------------------- 11 indexing
SECTIONS.append({"id": "indexing", "kicker": "11 · Do this",
  "title": "Tests at regular intervals for mother stock",
  "blocks": [
    p("<strong>Indexing</strong> is the procedure of clean-stock horticulture in which you do a "
      "test on each stock plant at regular intervals. Thus each clean result has a date. In "
      "cannabis, the usual test for HpLVd is RT-qPCR, which uses a small sample of tissue" +
      _c("mp-medgen-hlvd") + ". The cost of the test is low at this time. Thus the primary task is "
      "the interval between the tests, not the test."),
    p("Laboratories of the industry use this interval: do a test on <strong>each mother plant at an "
      "interval of 4 to 6 weeks</strong>" + _c("mp-tumi-hlvd-testing") + ". Always do the test "
      "<strong>before a large harvest of cuttings</strong>, not after the harvest" +
      _c("mp-medgen-hlvd") + ".</p><p>If it is possible, use a sample of <strong>root "
      "tissue</strong>. The viroid concentrates in the roots first and most equally. Thus roots are "
      "the most accurate sample" + _c("mp-tumi-hlvd-testing") + _c("mp-punja-2025-hplvd-mgmt") +
      ". Use material from more than one point on the plant. The concentration of the viroid is not "
      "the same in all parts of the plant. Thus one sample can give a clean result for an infected "
      "plant" + _c("mp-tumi-hlvd-testing") + "."),
    figure(_FIGS["testcal"], 10,
      "The figure shows one year of indexing. Each mother plant has an HpLVd qPCR test at short "
      "intervals. Each three months, there is a deep inspection of pests, hygiene and records. Each "
      "new plant goes into quarantine and has two tests" + _c("mp-tumi-hlvd-testing") +
      "."),
    p("<strong>The entry of new plants is the primary risk for a mother bank.</strong> New genetics "
      "(a clone from a supplier or from a different grower) is the most frequent source of HpLVd in "
      "a facility.</p><p>Put each new plant in quarantine. Use a room that is apart from the mother "
      "room. If you do not have this room, use a bench that is apart from the other benches. Use "
      "tools only for this bench.</p><p>When the plant comes into the facility, do a test. Keep the "
      "plant in quarantine for 2 to 4 weeks. Before the plant touches the mother bank, do a test "
      "again.</p><p>The second test is necessary. The viroid goes to all parts of the plant only "
      "after approximately six weeks. Thus a sample from a plant with a new infection can give a "
      "clean result" + _c("mp-medgen-hlvd") + "."),
    figure(L.flow("Quarantine: no plant goes into the bank without tests",
            [("Entry", "record, keep apart"), ("Quarantine", "special area, tools"),
             ("Test 1", "qPCR at entry"), ("Hold", "2–4 weeks"),
             ("Test 2", "roots, before release"), ("Into bank", "two clean results")]), 11,
      "The figure shows the procedure for new genetics. Two clean tests with a time in quarantine "
      "between them are better than one clean test at entry. A new infection can stay at a "
      "concentration that the test cannot find, for some weeks" + _c("mp-medgen-hlvd") +
      "."),
    p("Keep a record for each mother plant. The record has the ID, the dates and results of the "
      "tests, the number of cuttings, and the rooting rate of each batch. The trend of the rooting "
      "rate is a continuous test that has no cost. If the rooting rate of the clones from a mother "
      "plant decreases by ten percentage points in three batches, there is a problem. The last test "
      "does not show this problem at this time."),
    callout("warn", "Procedure for a positive result",
      p("Move the plant away from the other plants immediately. Do a test again to make sure that "
        "the result is correct. Use a new sample of roots.</p><p>Find each plant that the same "
        "tools touched after the last clean test. Do a test on each of these plants.</p><p>Discard "
        "each plant that has a positive result in the two tests. Put the plant in a bag <em>at the "
        "bench</em>. Seal the bag. Move the sealed bag out of the facility. Do not move infected "
        "material in the facility with no bag.</p><p>In some conditions, meristem tissue culture "
        "can make plants with no pathogen from important genetics. The average result is "
        "approximately 41% of the plants with no pathogen. The result is from 0% to 100% for "
        "different genotypes" + _c("mp-punja-2025-hplvd-mgmt") + ". But this procedure is work in "
        "the laboratory for some months (refer to <a href='tissue-culture.html'>tissue "
        "culture</a>). It is not a method to keep production stock in this cycle.")),
  ]})

# ---------------------------------------------------------------- 12 replacement
SECTIONS.append({"id": "replacement", "kicker": "12 · Do this",
  "title": "Replacement of mother plants with a constant supply of cuttings",
  "blocks": [
    p("There are five causes for the replacement of a mother plant. The first cause is a pathogen "
      "that two tests find. For this cause, replace the plant immediately. The second cause is a "
      "rooting rate that decreases in three or more batches when you find no other cause.</p><p>The "
      "third cause is a woody frame that is slow after many months of harvest. The fourth cause is "
      "a pot full of roots that more feed cannot correct. The fifth cause is the cost of the space. "
      "For each other cause, schedule the replacement. A replacement has a sequence of steps."),
    steps([
      ("Select the source plant", "Cut the replacement cutting from the best scaffold of a mother plant that has clean results. You can also use your second copy that has the lowest generation number and clean results. The replacement plant gets all the properties of the source."),
      ("Make the replacement plant", "Make roots on the cutting. Make the frame with the procedure of section 06. After approximately 6 weeks, the plant supplies a sufficient number of cuttings."),
      ("Do two tests while you make the frame", "When the cutting has roots, do a qPCR test. Before the plant goes into production, do a qPCR test again. A replacement plant is not a mother plant until it has two clean results."),
      ("Overlap", "Keep the mother plant that you replace and the replacement plant together for a minimum of one full cutting cycle. Compare the rooting rate of the cuttings of the two plants."),
      ("Remove the mother plant that you replace", "Discard the plant. Put the plant in a bag. Remove the bag. Before you use the equipment of the plant (pot, tray, stakes and drippers) for a different plant, clean and sanitize it."),
    ]),
    figure(_FIGS["succession"], 12,
      "The figure shows the steps of a replacement in the sequence of time. You make the "
      "replacement plant and do tests on it while the mother plant that you replace continues to "
      "supply cuttings. The two plants have an overlap of a full cycle. Then you remove the mother "
      "plant that you replace. The second copy is available during all the steps."),
    p("The overlap is a protection. Do not replace a mother plant without an overlap. If the "
      "cuttings of the replacement plant give worse results, you have the mother plant that you "
      "replace. If the replacement plant gives the same results, you can discard the other "
      "plant.</p><p>Always keep a <strong>second copy of each cultivar that is important to "
      "you</strong>. Keep it as a second mother plant in a different room, or as a culture in a "
      "tissue culture bank" + _c("mp-monthony-2021-tc") + ". A cultivar with only one copy has a "
      "risk. One pot with fusarium or one positive result can cause the end of the cultivar."),
    p("Two procedures extend the life of a mother plant. Put the plant in a new pot, or do a "
      "pruning of the roots, at regular intervals. Do not wait for symptoms of a pot full of roots "
      "(grower method).</p><p><strong>Re-mothering</strong> is the procedure in which you start a "
      "new mother plant from the best shoot of a mother plant. Re-mothering gives a new shape and a "
      "new pot. But it does <em>not</em> remove the pathogens or the mutations of the mother plant. "
      "The new plant has all that the mother plant has" + _c("mp-adamek-2024-subcultures") +
      ". Before the new plant goes into the bank, do a test."),
  ]})

# ---------------------------------------------------------------- 13 clone-from-clone
SECTIONS.append({"id": "clone-from-clone", "kicker": "13 · The alternative",
  "title": "Clone-from-clone propagation",
  "blocks": [
    p("Some operations do not use dedicated mother plants. For each batch, they cut the cuttings "
      "from production plants. These plants are young plants in the vegetative stage. The "
      "operations cut the cuttings immediately before the plants change to the flowering stage. The "
      "cuttings make roots while the source plants go to harvest.</p><p>There is no mother room and "
      "no work for mother plants. The operation has one room more for other use. This system "
      "operates, but it has costs and it has risks."),
    p("The data show that the system operates. Retip cuttings are cuttings that growers cut from "
      "cuttings with new roots. In a test, retip cuttings made roots at a rate of 76% to 81% with "
      "no hormone. The plants gave approximately the same result as plants from stem cuttings, and "
      "the cannabinoid content did not change" + _c("mp-kurtz-2022-retip") + ". One generation step "
      "does not cause damage to a crop."),
    p("The problem is not one generation step. The problem is the effect of a long sequence of steps:"),
    ul([
      "<strong>More mutations.</strong> The mutation load increases with each propagation cycle" + _c("mp-adamek-2024-subcultures") + ". In a mother bank, each batch is at generation 1. In one year of clone-from-clone propagation, there are 15 to 25 generations. Each generation has a new risk of mutation. There is no reference plant to compare with the drift.",
      "<strong>More pathogens.</strong> There is no plant that stays for a long time, and thus you cannot do indexing. Your stock is always two weeks from the flowering stage. Thus there is no time for quarantine and a second test. An HpLVd infection in one plant of the sequence goes to all the next generations, and you cannot see it" + _c("mp-adkar-2023-hidden-threat") + ".",
      "<strong>Selection drift.</strong> The person who cuts the cuttings selects the largest source plants and the source plants with the fastest growth. In many generations, this selection is for stretch and speed and not for quality. Many growers give reports of this effect (grower method), but no test data show it.",
      "<strong>No reference to start from.</strong> A mother bank can start each batch again from the reference plant. If a sequence of clones has an infection, has drift, or has an incorrect label, you cannot start it again. You cannot keep the cultivar.",
    ], "tight"),
    figure(_FIGS["lineage"], 13,
      "The figure shows a mother bank and a sequence of clones. The two systems make cuttings, but "
      "only the mother bank has a reference plant. In the mother bank, each batch is generation 1 "
      "from a plant with a clean test result. In the sequence of clones, generation 5 has all that "
      "generations 1 to 4 have. No test compared the plants with an initial plant that you know is "
      "good."),
    p("The decision: clone-from-clone propagation is correct as a <strong>temporary "
      "method</strong>. Use it while you increase the size of the facility, for short crops, or for "
      "cultivars that you will stop. Do a test on each group of source plants. Do not use it as the "
      "<em>permanent</em> method for genetics that are important to you. Permanent use of this "
      "method causes damage slowly.</p><p>Many operators use two methods together. They use a "
      "tissue culture bank, or one small mother plant with clean test results for each keeper "
      "cultivar, as the reference" + _c("mp-monthony-2021-tc") + ". They also use clone-from-clone "
      "propagation to supply the large number of plants in the time between."),
  ]})

# ---------------------------------------------------------------- 14 failure modes
SECTIONS.append({"id": "failure-modes", "kicker": "14 · When there is a problem",
  "title": "Problems of mother stock",
  "blocks": [
    p("A mother bank usually stops production without a sign that you can see. There are six "
      "causes. Procedures in this paper prevent most of them."),
    grid([
      card("Movement of HpLVd with no signs",
           p("A mother plant has latent HpLVd, and you use the same tools on many plants. Each "
             "harvest infects the next plant. No sign shows a problem until a flower room has "
             "dudding after some months. <strong>Correction:</strong> Use a blade for each plant. "
             "Do a qPCR test of a root sample at an interval of 4 to 6 weeks" +
             _c("mp-tumi-hlvd-testing") + "."),
           tag="viroid"),
      card("Only one copy",
           p("There is one mother plant for each cultivar. One pot with root rot, one positive "
             "result, or one tray that falls can cause the end of the genetics. "
             "<strong>Correction:</strong> Keep two copies in different rooms, or keep a culture in "
             "a tissue culture bank" + _c("mp-monthony-2021-tc") + "."),
           tag="supply"),
      card("The soft growth problem",
           p("A mother plant has dark green leaves and too much feed. Its cuttings show wilt in the "
             "dome and show rot. The rooting of a cutting uses the carbohydrate of the cutting, not "
             "the nitrogen" + _c("mp-druege-2004-stockplant-n") + ". <strong>Correction:</strong> "
             "Use a moderate N and EC. Make rigid shoots. Monitor the rooting rate."),
           tag="nutrition"),
      card("The pot full of roots",
           p("A mother plant stays for eighteen months in a pot of 12 L (3.2 gal). The vigor "
             "decreases slowly, and no person sees the change. Growers think that the cause is age. "
             "<strong>Correction:</strong> Put the plant in a new pot or do a pruning of the roots "
             "at regular intervals. Record the number of cuttings for each week. Then you see the "
             "change as a number."),
           tag="roots"),
      card("Clones from clones with no reference",
           p("A year of clone-from-clone propagation with no tests and no reference plant. The "
             "cultivar is not the same as before, and no person can find the cause or get the same "
             "cultivar again" + _c("mp-adamek-2024-subcultures") + ". <strong>Correction:</strong> "
             "Keep a reference, a mother plant or a culture, for each keeper cultivar."),
           tag="drift"),
      card("Replacement because of a date",
           p("A grower replaces mother plants that are clean and give good results each six months, "
             "with no data. At the same time, the grower has no procedure for the hygiene of "
             "blades. Blades are the primary cause of the end of stock. "
             "<strong>Correction:</strong> Replace because of data" + _c("mp-adamek-2024-subcultures") +
             ". Do tests with the work that you do not use for replacements."),
           tag="procedure"),
    ], cols=2),
  ]})

# ---------------------------------------------------------------- 15 troubleshooting
SECTIONS.append({"id": "troubleshooting", "kicker": "15 · When there is a problem",
  "title": "Troubleshooting",
  "blocks": [
    p("Start with the symptom. Examine the possible cause. Then do the correction. Wait one batch "
      "cycle before you make a decision about the correction. In most conditions, the cuttings show "
      "a problem of the mother plant first."),
    table(["Symptom", "Possible cause", "Correction"], [
      ["The rooting rate decreases batch after batch, and the mother plant has no symptoms", "A new HpLVd infection, soft growth because of too much feed, or a pot full of roots", "First, do a qPCR test of a root sample" + _c("mp-tumi-hlvd-testing") + ". Then examine the feed. Decrease the EC and the N. Then do a check of the pot."],
      ["Pistils or the first flowers on a mother plant", "Photoperiod fault: a timer that does not operate, a light leak, or a photoperiod of less than approximately 15 h", "Make sure that the photoperiod is 18 h. Do a check of the darkness in the room. Do not cut cuttings until the new growth has no flower structures" + _c("mp-ahrens-2023-photoperiod")],
      ["The cuttings are soft and long and show wilt quickly in the dome", "The feed is too high, the light is too low, the growth is soft, and the quantity of carbohydrate is low", "Decrease the EC by 0.2 to 0.4. Increase the PPFD to a value of 400–500. After 1 to 2 harvests, the shoots are rigid again." + _c("mp-druege-2004-stockplant-n")],
      ["The leaves of the mother plant are light green, the shoots are thin, and the regrowth is slow", "Not sufficient N, a pot full of roots, or root disease", "Increase the N to approximately 160 mg/L" + _c("mp-saloner-2020-nitrogen") + ". Examine the roots at the same time."],
      ["The downstream flower rooms have dudding, and the tests of leaves of the mother plants give clean results", "Latent HpLVd at a concentration that a test of leaves cannot find", "Do the test again with roots, with samples from more than one point on each plant" + _c("mp-tumi-hlvd-testing") + _c("mp-punja-2025-hplvd-mgmt") + ". A clean result from a leaf does not show that the plant has no HpLVd."],
      ["Pests come again in each batch of clones", "The mother room is the source of the pests", "Apply a treatment to the mother plants first. Monitor the mother plants. Before each harvest of cuttings, do an inspection. Refer to the <a href='ipm-sop.html'>IPM SOP</a>."],
      ["The only copy of a mother plant is a dead plant, or the only copy has a positive result", "There was no second copy", "If the genetics are very important, use meristem culture. Meristem culture is work in the laboratory for some months" + _c("mp-punja-2025-hplvd-mgmt") + ". Then correct the system: always keep two copies."],
    ], cls="compact", caption="The cuttings are a test of the mother plant. A problem of a mother plant shows in the numbers of its clones before it shows on its leaves."),
  ]})

# ---------------------------------------------------------------- 16 mental model
SECTIONS.append({"id": "mental-model", "kicker": "16 · The primary items",
  "title": "Constant supply of mother stock and a new start",
  "blocks": [
    p("Do not think that a mother plant is correct because it looks good. Use tests to make sure of "
      "its condition. Use four checks.</p><p>The first check is the <strong>rooting rate</strong> "
      "of the cuttings, batch after batch. It shows if the mother plant operates correctly. The "
      "second check is the <strong>qPCR test</strong> at regular intervals. It shows if the plant "
      "has HpLVd.</p><p>The third check is the <strong>second copy</strong>: a second mother plant "
      "or a tissue culture bank. The fourth check is <strong>replacement because of data, with an "
      "overlap</strong>. With these four checks, the supply of cuttings does not stop."),
    callout("key", "The five primary items",
      ol([
        "<strong>The 18/6 photoperiod is a safety interval, not a special number.</strong> Tests show initiation of flowers at photoperiods as long as 14 to 15 h" + _c("mp-ahrens-2023-photoperiod") + ". Make sure that the timer operates. Find each light leak.",
        "<strong>Use moderate values for all controls.</strong> Use approximately 300 to 500 µmol, approximately 160 mg/L N" + _c("mp-saloner-2020-nitrogen") + ", and a moderate EC. A mother plant that looks very good is frequently not the mother plant with the best results.",
        "<strong>The shape of the plant gives the output.</strong> Cut the top of the young plant. Make 4 to 6 scaffolds. Harvest approximately half of the canopy above the first node at an interval of 2 to 3 weeks.",
        "<strong>The blade moves the viroid from one plant to the next plant, and the test is the protection.</strong> Use a new blade for each plant. Do a qPCR test of a root sample at an interval of 4 to 6 weeks" + _c("mp-tumi-hlvd-testing") + ". Put each new plant in quarantine. Do two tests" + _c("mp-medgen-hlvd") + ".",
        "<strong>The number of propagation cycles changes the genetics of a sequence of clones, but time does not.</strong> The mutation load increases with the propagation cycles" + _c("mp-adamek-2024-subcultures") + ". Keep mother plants that have clean results and good records. Replace because of data. Always keep a second copy.",
      ])),
    p("The <a href='cloning.html'>cloning paper</a> shows how to change each shoot that you harvest "
      "into a plant with roots. The <a href='tissue-culture.html'>tissue culture</a> paper shows "
      "how to do the same work in the laboratory. It gives information about a bank of clean stock, "
      "meristem rescue, and storage for a long time" + _c("mp-monthony-2021-tc") +
      "."),
  ]})
