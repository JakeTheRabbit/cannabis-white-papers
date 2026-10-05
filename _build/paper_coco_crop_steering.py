# -*- coding: utf-8 -*-
"""Paper: precision coco cultivation, crop steering in coir (beginner)."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        stagecard, grid, card, chip, kv, steps)
import figs_lib as L

SLUG = "coco-crop-steering"
TITLE = "Precision coco cultivation: crop steering in coir"
EYEBROW = "Basic · Coco and crop steering"
SUB = ("Coco coir is the easiest substrate for crop steering, because the wet and dry cycles give "
       "the same result each time. This paper gives information about the numbers that a root-zone "
       "sensor shows. It shows how the wet and dry cycle of one day operates. It also shows how to "
       "use dryback to cause more leaf growth or more flower growth. It is not necessary to know "
       "about the root zone before you read this paper.")
META = [("droplet", "Basic"), ("image", "5 diagrams"),
        ("quote", "Data with sources · 10 sources"), ("clock", "Approximately 16 min to read")]
RELATED = ["root-zone-teros12", "grow-room-systems", "tissue-culture"]
REF_IDS = ["abad2005-coir", "noguera2003-cec", "malik2025-media", "hilhorst2000-ec",
           "caplan2019-drought", "stack2024-drought", "welling2025-aba",
           "grossiord2020-vpd", "moe1995-dif", "moher2023-photoperiod"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

SECTIONS.append({"id": "start", "kicker": "01 · Read this first", "title": "Purpose and scope",
  "blocks": [
    lead("&lsquo;Crop steering&rsquo; is an easy method. When you control <em>when</em> and <em>how "
         "much</em> water you apply, you can cause the plant to become larger with more leaves. Or "
         "you can cause the plant to make flowers with a high density and more resin. Coco coir is "
         "the easiest substrate for crop steering, because it becomes wet and dry quickly and the "
         "result is the same each time."),
    p("You can use this paper if you did not measure a root zone before. Each term has a "
      "definition. At the end, you will know how to read the numbers of a root-zone sensor. You "
      "will also know how to use the wet and dry rhythm of each day to control the plant."),
    callout("note", "Who this paper is for",
      p("This paper is for each grower who uses coco or thinks about coco. These growers want "
        "results that they can get again. They do not want to apply water &lsquo;when it feels "
        "dry.&rsquo; Use this paper with the <a href='root-zone-teros12.html'>root-zone sensor</a> "
        "paper and the <a href='grow-room-systems.html'>grow room systems</a> paper.")),
  ]})

SECTIONS.append({"id": "terms", "kicker": "02 · The terms", "title": "Definitions",
  "blocks": [
    p("It is not necessary to know all of these terms at this time. It is sufficient to know the basic information of each term. Each term occurs again in this paper, with more information."),
    defterm("Coco coir", "A substrate that comes from the fibers of coconut husk. It contains "
            "water, but it also keeps a large quantity of air around the roots."),
    defterm("Substrate", "The general name for each material that contains the roots. Examples are "
            "coco, rockwool, peat and soil. <a href='glossary.html#gl-substrate'>Glossary &rarr;</a>"),
    defterm("VWC (volumetric water content)", "The quantity of water in the root zone, as a "
            "percentage of the volume of the root zone. If the VWC is 60%, water fills 60% of the "
            "space in the pot."),
    defterm("EC (electrical conductivity)", "An approximate measurement of the quantity of "
            "fertilizer salt in the water of the root zone. When the EC is higher, the feed is "
            "stronger and contains more salt."),
    defterm("Field capacity", "The maximum quantity of water that the substrate contains "
            "immediately after it drains. This quantity is the &lsquo;full&rsquo; level for each "
            "day."),
    defterm("Dryback", "The quantity by which the VWC decreases between two irrigations. The plant "
            "uses water and the substrate becomes dry. Dryback is the most important control for "
            "crop steering."),
    defterm("Crop steering", "A method to cause vegetative growth (leaves) or generative growth "
            "(flowers and resin) in the plant. The method uses irrigation, climate and light."),
    defterm("Shot", "One short period of irrigation. Crop steering replaces one large irrigation "
            "each day with some small shots at set times."),
  ]})

SECTIONS.append({"id": "why-coco", "kicker": "03 · The substrate", "title": "Coco substrate properties",
  "blocks": [
    p("Coco contains a large quantity of water <strong>and</strong> a large quantity of air at the "
      "same time. At field capacity, approximately a fifth to a third of the volume of the coco is "
      "pore space that contains air" + _c("abad2005-coir") + ". This air supplies oxygen to the "
      "roots. As a result, the roots stay in good condition, and you can apply water frequently. "
      "The roots continue to get oxygen."),
    figure(L.bars("Air around the roots at field capacity",
            [("Coco coir", 25), ("Peat", 12), ("Rockwool", 18)], unit="%",
            note="Air-filled porosity: a higher value gives more oxygen at the roots when fully wet.",
            maxv=32), 1,
      "At field capacity, coco contains more air than peat. Thus the roots get oxygen when the "
      "substrate is wet. The values are not the same for all coco. They change with the ratio of "
      "pith to pieces of husk and with the size of the pot." + _c("abad2005-coir") +
      _c("malik2025-media")),
    p("The fibers of coco have a small electrical charge. The charge holds nutrients and releases "
      "them. This property is the <strong>cation exchange capacity</strong>" + _c("noguera2003-cec") +
      ". As a result, the nutrients in the root zone change less when the feed changes.</p><p>But "
      "new coco holds some of the calcium and magnesium of the feed. Thus the plant cannot use this "
      "calcium and magnesium. This continues until you soak the coco in a solution of calcium and "
      "magnesium."),
    callout("tip", "Soak new coco first",
      p("New coco can hold calcium and magnesium in the first one or two weeks, and the plant "
        "cannot use them. Before you put the plants in the coco, soak the coco in a solution of "
        "calcium and magnesium. If you do not, deficiency marks can occur on the leaves at the "
        "start of the crop, until the coco is stable.")),
  ]})

SECTIONS.append({"id": "reading", "kicker": "04 · The signals", "title": "Reading the root zone: VWC and EC",
  "blocks": [
    p("A root-zone sensor gives two numbers that change with time: <strong>VWC</strong> (the "
      "quantity of water) and <strong>EC</strong> (the quantity of salt). Together they show the "
      "condition of the plant and the next step for you."),
    p("New growers frequently do not know this fact. <strong>When the substrate dries, the "
      "concentration of salt in it increases and, as a result, the EC increases.</strong> The "
      "quantity of water decreases, but the quantity of fertilizer does not decrease.</p><p>The "
      "sensor uses the bulk EC reading, the moisture and the temperature to calculate an estimate "
      "of the &lsquo;pore-water EC&rsquo;" + _c("hilhorst2000-ec") + ". The pore-water EC is the EC "
      "of the water that touches the roots. Thus the EC readings are not accurate when the VWC is "
      "less than 10%."),
    figure(L.line("A usual day in coco: VWC falls, then increases",
            [(0, 60), (1, 57), (2, 53), (3, 49), (4, 47), (5, 60)],
            ["lights on", "+3h", "+6h", "+9h", "pre-dark", "next shot"],
            ylab="VWC %", ymin=40, ymax=66,
            note="During the day, the plant uses the water in the pot. Irrigation fills the pot again to field capacity."), 2,
      "This curve shows one day for a plant in good condition. The VWC falls by a controlled "
      "quantity (the dryback). Then irrigation increases the VWC to field capacity. The size and "
      "the time of the dryback are your steering control."),
    callout("key", "Read the two numbers together",
      ul(["<strong>When the VWC falls</strong>, the plant uses water. This effect is good until the VWC falls too far. Then the growth of the plant stops.",
          "It is usual when <strong>the EC increases slowly</strong> as the VWC falls. If the EC increases by a large quantity in a short time, the root zone has too much salt. Thus apply water.",
          "<strong>When the EC decreases slowly</strong> during some days, the plant uses the salt faster than the feed supplies it. Thus increase the EC of the feed."], "tight")),
  ]})

SECTIONS.append({"id": "dryback", "kicker": "05 · The dryback", "title": "Dryback: your primary control for crop steering",
  "blocks": [
    callout("evidence", "Be careful with this information",
      "<p><strong>Limit of the data:</strong> One drought in the last stage of the crop, as in the "
      "test of Caplan, is <em>related</em> to generative drybacks. But it is not the same test as "
      "dryback cycles each day for many weeks. Use dryback to cause a small change in the plant. Do "
      "not let wilt occur. The percentage values of your probe are not the same for all "
      "substrates.</p>"),
    p("A <strong>dryback</strong> is the quantity by which the root zone dries before you apply "
      "water again. You select this quantity. The effect on the plant is different for a small "
      "dryback and for a large dryback. A small, controlled water deficit changes the growth of the "
      "plant."),
    p("When the root zone dries by a small quantity, the plant makes a stress hormone. The name of "
      "this hormone is <strong>abscisic acid (ABA)</strong>. ABA decreases vegetative growth and "
      "increases the production of flowers and resin" + _c("welling2025-aba") +
      ". The data show that a controlled water deficit at the correct time <em>increases</em> the "
      "cannabinoid content, and the yield does not decrease" + _c("caplan2019-drought") +
      "."),
    callout("warn", "A dryback is not a drought",
      p("The difference is the dose and the time. <strong>Moderate</strong> drybacks keep the yield "
        "when you measure them and stop them at the correct time. A <strong>large</strong> drought "
        "that continues for too long decreases the yield and the cannabinoids by a large quantity" +
        _c("stack2024-drought") + ". Make small, careful changes. Always apply water before the "
        "plant shows wilt.")),
    p("Larger drybacks give more generative growth (flowers). Smaller drybacks, which keep the "
      "substrate wetter, give more vegetative growth (leaves and size). This one control is most of "
      "crop steering: the quantity by which you let the root zone dry."),
  ]})

SECTIONS.append({"id": "phases", "kicker": "06 · The rhythm of each day", "title": "Irrigation cycle of one day: P0–P3",
  "blocks": [
    p("Growers divide the lights-on day into four phases. You can use this method without special "
      "equipment. The rhythm of the phases is: dry, fill again, keep full, and dry."),
    figure(L.flow("The four phases of the irrigation day",
            [("P0", "first dryback at lights-on"), ("P1", "ramp: small shots fill again"),
             ("P2", "keep near field capacity"), ("P3", "overnight dryback")]), 3,
      "P0 is the short dryback after lights-on and before the first feed. It makes the plant start "
      "to use water. In P1, small shots increase the VWC again. In P2, the shots keep the root zone "
      "full during the day. P3 is the large dryback during the night."),
    figure(L.bars("The VWC in each phase",
            [("P0 end", 46), ("P1", 54), ("P2", 60), ("P3 start", 57)], unit="%", target=55,
            note="Generative steering keeps the VWC lower. Vegetative steering keeps it higher, with less change.", maxv=70), 4,
      "This chart shows a generative day. On a generative day, the dryback is larger and the shots "
      "are smaller. On a vegetative day, the VWC is higher and the dryback is smaller."),
    table(["Phase", "Definition", "Effect"], [
      ["<strong>P0</strong>", "The time after lights-on and before the first shot. You do not apply water.", "A short dryback. It makes the plant start to use water before the first feed."],
      ["<strong>P1</strong>", "A number of small shots after lights-on", "Fills the root zone again to field capacity, carefully"],
      ["<strong>P2</strong>", "Maintenance shots", "Keeps the VWC near full and flushes the salt that collects (EC control)"],
      ["<strong>P3</strong>", "The last shot, then the night", "The large dryback during the night. It sets the type of steering for the day: generative or vegetative."],
    ], caption="The P0–P3 phases. The numbers that you select for each phase are your steering method."),
  ]})

SECTIONS.append({"id": "steering", "kicker": "07 · Steering controls", "title": "Vegetative and generative steering",
  "blocks": [
    p("&lsquo;Generative&rsquo; growth is the growth of flowers, density and resin. "
      "&lsquo;Vegetative&rsquo; growth is the growth of leaves, stems and size. You change the "
      "growth of the plant with a small number of controls. All of these controls change how easily "
      "the plant gets water."),
    table(["Control", "For GENERATIVE growth (flower)", "For VEGETATIVE growth (leaves and size)"], [
      ["Dryback", "Drybacks that are larger and longer", "Smaller drybacks. The substrate stays wetter."],
      ["Feed EC", "Higher EC (more osmotic stress)", "Lower EC"],
      ["Shots", "A smaller number of shots, smaller shots, and a longer time before the first shot", "More frequent shots, larger shots, and a shorter time before the first shot"],
      ["Day and night temperature", "A lower night temperature and a larger difference between day and night", "Higher temperatures and a smaller difference between day and night"],
      ["VPD and humidity", "Drier air (higher VPD)", "Air with more humidity (lower VPD)"],
    ], caption="Most of these controls change the plant through <strong>transpiration</strong>. Transpiration occurs when a plant pulls water up from the roots and releases it through the surface of the leaves. When the plant transpires faster, it uses more water. Use one or two controls at a time. Do not use all of the controls at the same time."),
    p("When you increase the EC of the feed, the solution in the root zone has a higher "
      "concentration than the water in the plant. The plant must pull harder to get water because "
      "of the difference in concentration. This effect is <strong>osmotic stress</strong>. If you "
      "increase the EC by a moderate quantity, the generative growth becomes stronger. If you "
      "increase the EC too much, the growth stops."),
    p("Temperature is in the table above because the difference between day temperature and night "
      "temperature controls stretch. A warm day and a cool night give less stretch. A warm night "
      "gives more stretch" + _c("moe1995-dif") + ".</p><p>The air around the leaves controls the "
      "rate of transpiration. When the air is drier, the plant transpires faster. <strong>Vapor "
      "pressure deficit (VPD)</strong> is the measurement of how dry the air is. You measure VPD in "
      "kPa. VPD is the difference between the quantity of water vapor that the air can hold at that "
      "temperature and the quantity that it holds. When the VPD is higher, the air removes more "
      "water from the plant.</p><p>When the VPD is more than some value, the pores of the leaf "
      "close to keep the water in the leaf. Then the transpiration decreases, but the air continues "
      "to be dry" + _c("grossiord2020-vpd") + "."),
    callout("danger", "Change one control at a time",
      p("All controls have an effect on each other. Do not make large changes to the dryback, the "
        "EC, the humidity and the night temperature at the same time. Then you cannot know which "
        "change was good or bad, and the plant can get too much stress.</p><p>Change one control. "
        "Monitor the plant for some days. Then adjust the controls.")),
  ]})

SECTIONS.append({"id": "week", "kicker": "08 · Week by week", "title": "Flowering steering by week",
  "blocks": [
    p("The flowering stage in a grow room usually continues for approximately 8 to 10 weeks after "
      "you change the light cycle to a 12-hour night" + _c("moher2023-photoperiod") +
      ". The steering changes during these weeks:"),
    steps([
      ("End of the vegetative stage", "Use vegetative steering: keep the VWC high, keep the drybacks small, and keep the EC moderate. Make the plant and the root system large and in good condition."),
      ("Weeks 1 to 2 of flowering (stretch)", "The plants become almost two times as high. To decrease stretch, keep the night temperature lower and the difference between day and night temperature moderate. In this stage, start to use small generative drybacks."),
      ("Weeks 3 to 6 of flowering (flowers become larger)", "Use the maximum generative steering. Use strong drybacks and a higher EC. In P2, keep the root zone full to supply feed to the flowers while they become larger."),
      ("From week 7 of flowering (ripening)", "Use less steering. A controlled water deficit in this stage can increase the potency. But stop the deficit before the plant shows stress."),
      ("Finish (decrease the EC. The data that show better quality from a long flush with only water are weak)", "In the last part of the crop, apply feed with a lower EC. Let the plant complete its growth slowly and without problems."),
    ]),
  ]})

SECTIONS.append({"id": "trouble", "kicker": "09 · When a problem occurs", "title": "Troubleshooting",
  "blocks": [
    table(["Symptom", "Possible cause", "Correction"], [
      ["The EC increases each day, and the plant is not in good condition", "Salt collects. The drybacks are too large, or the flush is not sufficient.", "Use larger shots in P2 to flush the salt. Decrease the EC of the feed by a small quantity."],
      ["The VWC falls by only a small quantity during the day", "Too much irrigation, or the plant does not use water because of disease, low light, or a low temperature", "Use a smaller number of shots, or smaller shots. Do a check of the condition of the roots, the temperature and the light."],
      ["Damaged leaf tips and leaves that bend down", "The EC of the feed is too high for the conditions", "Decrease the EC. Make sure that each shot has a sufficient volume of water."],
      ["The plants are high, with too much stretch and weak stems", "The plants are too vegetative because the nights are warm and the drybacks are small", "Decrease the night temperature. Increase the difference between day and night temperature. Use larger drybacks."],
      ["Calcium and magnesium deficiency in the first weeks", "New coco that you did not soak in calcium and magnesium", "Before you use the coco, soak it in a solution of calcium and magnesium. Add calcium and magnesium to the first feeds."],
      ["The plant shows wilt between shots", "The dryback is too large. It is a drought and not crop steering.", "Apply water after a smaller dryback. Make P0 and P3 shorter. Do not let the plant show wilt."],
    ], cls="compact"),
  ]})

SECTIONS.append({"id": "expect", "kicker": "10 · Clear information", "title": "Expected results and limitations",
  "blocks": [
    callout("key", "Three important points",
      ol(["<strong>There is no one set of numbers that is correct for all rooms.</strong> The correct numbers for VWC, EC and dryback are different if the cultivar, the pot size, the climate or the light is different. Start with the ranges in this paper and adjust them for <em>your</em> plants.",
          "<strong>Steering makes a result more possible, but it does not give a fast change.</strong> The effect occurs during some days. You do not change a plant in one night.",
          "<strong>The root zone is only one control.</strong> Light, temperature, humidity and airflow all have an effect on the same plant. After this paper, read the <a href='grow-room-systems.html'>grow room systems</a> paper."])),
    p("Put a sensor in the root zone. Find the baseline, which is the values of one usual day in "
      "your system. Then change one control at a time. This method has three steps: a sensor first, "
      "a baseline second, and one change at a time. The method makes coco give the same results in "
      "each crop."),
  ]})
