# -*- coding: utf-8 -*-
"""Paper: CO2 enrichment for cannabis, how it works and how to do it safely (beginner to advanced)."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        stagecard, grid, card, chip, kv, steps)
import figs_lib as L

SLUG = "co2-enrichment"
TITLE = "CO2 enrichment: a safe supply of carbon to the plant"
EYEBROW = "Environment and climate · CO2"
SUB = ("A plant changes carbon dioxide (CO2) into sugar. In strong light, a crop in a building can "
       "use much more CO2 than the air supplies. Added CO2 can increase the dry yield by "
       "approximately one third. The plant uses CO2 only in the light period, and in a ventilated "
       "room the exhaust air removes the CO2. At an incorrect concentration, CO2 can kill a person "
       "in the room. This paper gives the target range, the method to seal a room, and the safety "
       "limits and alarms to install before a person goes in.")
META = [("spark", "From facts to a safe setup"), ("image", "7 diagrams"),
        ("quote", "38 sources"), ("clock", "~30 min to read")]
RELATED = ["grow-room-systems", "airflow-design", "harvest-dry-trim-cure"]
REF_IDS = [
    "chandra2008-photo", "tolbert1995-compensation", "noaa2024-co2", "chandra2011-co2",
    "rm2021-light", "westmoreland2023-usu", "doddrell2023-co2", "amthor2024-respiration",
    "collalti2019-npp", "atkin2003-q10", "ahdb-co2", "wang2022-co2cue", "lv2022-topt",
    "kitaya2004-airvel", "kader2002-respiration", "permentier2017-co2poison", "osha-pel-co2",
    "niosh-co2", "worksafenz-co2", "azuma2018-cognition", "ifc5307", "sensirion-scd",
    "winsen-mq", "okstate-co2",
    "epa-hepa", "souza2024-carbon-ethylene", "alvarez2024-ethylene", "abeles1992-ethylene",
    "cornell-ethylene", "wheeler1996-ethylene", "hudelson2023-ethylene", "monthony2026-ethylene",
    "osha-oxygen", "hpac-latent", "zhang2020-canopy-rh", "baptista2012-ventilation",
    "liang2026-cannabis-ach", "punja2019-pathogens",
]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

# ---------------------------------------------------------------- 01
SECTIONS.append({"id": "start", "kicker": "01 · Read this first", "title": "Purpose and scope",
  "blocks": [
    lead("A plant makes its structure from air. The carbon in each leaf, stem and flower is from "
         "carbon dioxide (CO2). The plant absorbs the CO2 from the room air. It uses the energy of "
         "light to make sugar from the CO2 and water.</p><p>If you give a canopy in bright light "
         "more CO2 than the approximately 420 ppm of usual air, the canopy can increase its rate of "
         "growth. Thus growers add CO2. But CO2 enrichment is one of the tasks in the room in which "
         "it is easiest to make a dangerous error."),
    callout("key", "The five primary facts of this paper",
      ul(["<strong>The plant uses CO2 only in the light period.</strong> In the dark period, the "
          "CO2 moves in the opposite direction. The plant releases CO2. CO2 that you add at night "
          "is waste, and it is a risk to safety.",
          "<strong>CO2 increases the yield only in strong light.</strong> CO2 and light are each a "
          "limit for photosynthesis. In weak light, more CO2 has almost no effect" +
          _c("chandra2008-photo") + ".",
          "<strong>The target range is approximately 1,000&ndash;1,500 ppm.</strong> If the "
          "concentration is less than this range, the yield is less than the maximum. If the "
          "concentration is more than this range, the gas that you add is waste. It does not "
          "increase the yield" + _c("westmoreland2023-usu") + ".",
          "<strong>You must seal the room.</strong> In a ventilated room, the exhaust air removes "
          "the CO2 that you add, and the CO2 goes directly out of the room. The cost of this CO2 is "
          "waste" + _c("wang2022-co2cue") + ".",
          "<strong>CO2 can kill a person.</strong> You cannot smell the gas. A sealed room with CO2 "
          "enrichment, or a drying room, can have a high concentration that kills a person" +
          _c("permentier2017-co2poison") + "."])),
    p("The remaining sections of this paper give more information about these five facts. "
      "<strong>Add CO2 in the light period. Seal the room. Install a CO2 alarm on the "
      "wall.</strong> These three instructions are the most important."),
  ]})

# ---------------------------------------------------------------- 02
SECTIONS.append({"id": "terms", "kicker": "02 · The terms", "title": "Definitions",
  "blocks": [
    defterm("CO2 (carbon dioxide)", "The gas that plants change into sugar with the energy of "
            "light. At this time, usual outdoor air contains approximately 420 ppm of CO2" +
            _c("noaa2024-co2") + "."),
    defterm("ppm", "One part in a million parts. 1,000 ppm is one part of CO2 in a thousand parts "
            "of air (0.1%). All the CO2 values in this paper are in ppm. 10,000 ppm is 1%."),
    defterm("Photosynthesis", "The reaction that changes CO2 and water into sugar with the energy "
            "of light. It is the only reaction that moves CO2 <em>into</em> the plant. The reaction "
            "cannot operate without light."),
    defterm("Respiration", "The reaction in which the plant uses the sugar as energy for growth and "
            "for its other functions. This reaction releases CO2. It operates day and night in each "
            "living cell" + _c("amthor2024-respiration") + "."),
    defterm("C3 plant", "Cannabis is a C3 plant. In a C3 plant, the CO2 concentration of usual air "
            "is the limit for photosynthesis. Thus CO2 enrichment helps cannabis."),
    defterm("Photorespiration", "A side reaction that is a waste of energy. In this reaction, the "
            "enzyme that makes sugar from CO2 absorbs oxygen and not CO2. When the CO2 increases, "
            "this waste decreases. A lower leaf temperature also decreases this waste" +
            _c("tolbert1995-compensation") + "."),
    defterm("Compensation point", "The CO2 concentration (approximately 50 ppm for a C3 plant) at "
            "which the rate of photosynthesis is equal to the rate of respiration. At this "
            "concentration, the plant does not make more sugar than it uses" +
            _c("tolbert1995-compensation") + "."),
    defterm("Saturation point", "The CO2 concentration at which more CO2 does not help the plant. "
            "For CO2 enrichment, this value is approximately 1,000&ndash;1,500 ppm."),
    defterm("NDIR sensor", "Non-dispersive infrared. It is the only type of low-cost sensor that "
            "measures CO2 correctly. Low-cost &lsquo;MQ&rsquo; gas sensors do not measure CO2 "
            "correctly" + _c("sensirion-scd") + "."),
    defterm("TWA / STEL / IDLH", "Limits for the safety of workers. TWA is the limit for the "
            "average CO2 concentration for 8 hours. STEL is the limit for a short period of 15 "
            "minutes. IDLH is the concentration that is immediately dangerous to life or health" +
            _c("niosh-co2") + "."),
  ]})

# ---------------------------------------------------------------- 03
SECTIONS.append({"id": "how", "kicker": "03 · How the plant uses CO2", "title": "Photosynthesis in the leaf and the effect of the CO2 concentration",
  "blocks": [
    p("In a leaf in the light, an enzyme with the name Rubisco absorbs CO2 from the air and changes "
      "it into sugar. Rubisco does not absorb only CO2. It also absorbs oxygen. When Rubisco "
      "absorbs oxygen and not CO2, <strong>photorespiration</strong> starts. Photorespiration is a "
      "reaction that is a waste of energy and carbon. It does not make a product that the plant can "
      "use.</p><p>When the ratio of CO2 to oxygen increases, photorespiration occurs at a lower rate" +
      _c("tolbert1995-compensation") + "."),
    p("At this time, the air contains approximately 420 ppm of CO2" + _c("noaa2024-co2") +
      ". This concentration is not sufficient for Rubisco to operate at the maximum rate. In a C3 "
      "plant, for example cannabis, the <strong>CO2 concentration is the limit</strong> for "
      "photosynthesis. When the CO2 increases, photosynthesis increases.</p><p>In the one primary "
      "investigation of gas exchange in cannabis, the CO2 increased from 350 to 750 ppm. The net "
      "photosynthesis of the leaf increased by approximately <strong>50%</strong>" +
      _c("chandra2008-photo") + ". A subsequent investigation of four cultivars with high THC found "
      "that the net photosynthesis increased by <strong>38&ndash;48%</strong> when the CO2 "
      "increased from 390 to 700 ppm" + _c("chandra2011-co2") + "."),
    figure(L.bars("More CO2 causes more photosynthesis (cannabis leaf)",
            [("250 ppm", 50), ("350 ppm", 100), ("750 ppm", 150)], unit="",
            note="Net photosynthesis of a cannabis leaf. The 350 ppm baseline = 100. With less CO2, the value decreases by half. With more CO2, it increases by half.",
            maxv=170), 1,
      "Net photosynthesis of a cannabis leaf at different CO2 concentrations. If the CO2 decreases "
      "to 250 ppm, the net photosynthesis decreases by approximately 50%. If the CO2 increases to "
      "750 ppm, it increases by approximately 50%" + _c("chandra2008-photo") +
      ". At first, the net photosynthesis increases quickly with the CO2. Then the curve becomes "
      "horizontal, because other limits become the maximum for the rate."),
    p("Photosynthesis has a maximum value. When the CO2 increases, the rate at which the leaf can "
      "use the light becomes the limit for photosynthesis. Thus the curve <strong>becomes "
      "horizontal at a saturation point</strong>. For most C3 crops in greenhouses, the horizontal "
      "part of the curve starts at approximately 1,000&ndash;1,300 ppm" + _c("doddrell2023-co2") +
      "."),
    callout("key", "When CO2 has an effect",
      p("CO2 and light are each a limit for the plant. The lower of the two limits is the maximum "
        "for the plant (Liebig's law of the minimum). In weak light, more CO2 has no effect. The "
        "flower yield of cannabis continues to increase with the light, to a very high intensity" +
        _c("rm2021-light") + ". Thus CO2 has an effect only when the light is strong.")),
  ]})

# ---------------------------------------------------------------- 04
SECTIONS.append({"id": "daynight", "kicker": "04 · Day and night", "title": "Photosynthesis and respiration in the light cycle",
  "blocks": [
    p("Persons who start CO2 enrichment frequently make an error with this fact. Photosynthesis is "
      "the reaction that <em>uses</em> CO2. It operates only in the light. "
      "<strong>Respiration</strong> is the reaction that <em>releases</em> CO2. It does not stop, "
      "day and night, in each living cell" + _c("amthor2024-respiration") + ".</p><p>In the light "
      "period, photosynthesis absorbs much more CO2 than respiration releases. Thus the canopy has "
      "a net CO2 <em>uptake</em>. When the lights go off, photosynthesis stops and only respiration "
      "continues. Thus the same canopy has a net CO2 <em>emission</em>. At night, the rate of CO2 "
      "emission is much lower than the rate of CO2 uptake in the day."),
    figure(L.line("Day and night: CO2 flows in and out of the plant",
            [("", 2), ("", 2), ("", 2), ("", -17), ("", -21), ("", -20), ("", -20), ("", -20),
             ("", -19), ("", 3), ("", 2), ("", 2), ("", 2)],
            ["0h", "", "", "06", "", "", "12", "", "", "18", "", "", "24h"],
            ylab="net CO2 flux", ymin=-24, ymax=8,
            note="Example of the net CO2 flux of the canopy. Lights on 06:00-18:00. Less than zero: net uptake (light). More than zero: net emission (night)."), 2,
      "The net CO2 flux of the canopy in one day. In the light period, the canopy absorbs much CO2. "
      "In the dark period, it releases a small quantity of CO2. The trough in the day is much "
      "larger than the peak at night. The next section gives more information about this difference."),
    p("The rate of respiration also increases when the temperature is higher. When the temperature "
      "increases by 10&nbsp;&deg;C (18&nbsp;&deg;F), the rate becomes approximately two times "
      "higher (a Q10 of approximately 2)" + _c("atkin2003-q10") + ". In soil or coco, microbes and "
      "roots in the root zone also make more CO2. But these facts do not change the primary fact: "
      "<strong>the plant absorbs CO2 only while the lights are on.</strong> Because of this one "
      "fact, you add CO2 in the light period and do not add CO2 in the dark period."),
  ]})

# ---------------------------------------------------------------- 05
SECTIONS.append({"id": "massbalance", "kicker": "05 · The mass balance", "title": "CO2 uptake in the day and CO2 emission at night",
  "blocks": [
    p("Growers frequently think that the plant uses CO2 in the day and releases the same quantity "
      "of CO2 at night. The two quantities are not the same. <strong>The cause of this difference "
      "is the cause of the effect of CO2 enrichment.</strong></p><p>The plant does not release "
      "again all the carbon that it absorbs in the light. In one growing season, respiration "
      "releases only approximately half of the carbon that photosynthesis absorbs. The remaining "
      "carbon, approximately <strong>46%</strong>, stays in the plant as sugar, stem, leaf and "
      "flower" + _c("collalti2019-npp") + ". Review papers on crop physiology give a range of "
      "30&ndash;60% for the fraction that respiration releases" + _c("amthor2024-respiration") +
      ".</p><p>This carbon in the plant <em>is</em> the crop. Thus the CO2 that the plant absorbs "
      "in the day is always more than the CO2 that it releases at night. The difference is the "
      "quantity of carbon that became plant tissue."),
    p("You can find this difference in a sealed room. When the lights are on and you do not add "
      "CO2, the canopy quickly decreases the CO2 in the air. The concentration becomes lower than "
      "the concentration of outdoor air. In a greenhouse with good seals, the CO2 can decrease to "
      "approximately <strong>200 ppm</strong> in some hours. This low concentration decreases the "
      "photosynthesis of the canopy by approximately <strong>26%</strong>" + _c("ahdb-co2") +
      ".</p><p>During the night, the CO2 in the same room increases again, because the respiration "
      "of the plants releases CO2. But the CO2 increases slowly. The CO2 does not increase to a "
      "high value, because the room has leaks."),
    figure(L.line("A sealed room with no added CO2, for 24 hours",
            [("", 620), ("", 520), ("", 450), ("", 430), ("", 230), ("", 205), ("", 200), ("", 200),
             ("", 205), ("", 270), ("", 440), ("", 560), ("", 630)],
            ["0h", "", "", "06", "", "", "12", "", "", "18", "", "", "24h"],
            ylab="room CO2 (ppm)", ymax=720,
            note="Sealed room, no CO2 added. Lights on 06:00. Photosynthesis decreases the CO2 to approximately 200 ppm. At night, respiration increases the CO2 again."), 3,
      "Room CO2 in a sealed flower room without CO2 enrichment. When the lights come on, the CO2 "
      "decreases quickly to a very low value. At night, the CO2 increases slowly and by a small "
      "quantity. CO2 enrichment replaces the CO2 that the canopy removes in the day" + _c("ahdb-co2") +
      "."),
    callout("note", "The numbers for a room of medium size",
      ul(["<strong>When the lights come on.</strong> A canopy of approximately 45&nbsp;m&sup2; "
          "(484&nbsp;ft&sup2;) absorbs 15&ndash;25 &micro;mol CO2 m&sup2;/s. In a sealed room of "
          "approximately 160&nbsp;m&sup3;, the CO2 decreases at first by approximately "
          "<strong>350&ndash;600 ppm for each hour</strong>. The CO2 decreases from 420 to "
          "approximately 200 ppm in 20&ndash;40 minutes. Then the rate becomes lower, because the "
          "CO2 is low.",
          "<strong>When the lights go off.</strong> In the dark period, the respiration of the same "
          "canopy adds only approximately <strong>25&ndash;70 ppm for each hour</strong>. During "
          "the night, the CO2 increases by two hundred ppm or more. Then the CO2 stays at that "
          "value because of the leaks of the room.",
          "<strong>The difference is the crop.</strong> Approximately half of the carbon that the "
          "plant absorbs stays in the plant, and respiration does not release it again. Thus the "
          "CO2 uptake in the day is many times the CO2 emission at night" + _c("collalti2019-npp") +
          "."])),
    p("This balance gives the primary information about the quantity of CO2 that is necessary. CO2 "
      "enrichment is not for the night. It keeps the CO2 <em>high</em> in the light hours. Without "
      "CO2 enrichment, the canopy removes most of the CO2 from the room."),
  ]})

# ---------------------------------------------------------------- 06
SECTIONS.append({"id": "howmuch", "kicker": "06 · The dose", "title": "CO2 targets and the effect on the yield",
  "blocks": [
    p("The best yield data for cannabis come from controlled tests at Utah State University. In "
      "these tests, the CO2 concentration of a sealed room increased from the concentration of "
      "outdoor air (approximately 420 ppm) to approximately 1,200 ppm. The dry flower yield "
      "increased by approximately <strong>40%</strong>. The concentration of 1,200 ppm gave "
      "approximately <strong>95%</strong> of the possible yield gain. Thus a higher concentration "
      "gives almost no more yield" + _c("westmoreland2023-usu") + ".</p><p>Other crops in "
      "greenhouses show the same result. Many C3 crops in greenhouses have a yield gain of ten "
      "percent or more at approximately 800&ndash;1,200 ppm (the very high yield gains in reports "
      "change with the control treatment, which can have a low CO2 concentration, and with the "
      "system)" + _c("doddrell2023-co2") + ". For most C3 crops, the saturation point is "
      "approximately 1,000&ndash;1,300 ppm" + _c("doddrell2023-co2") + "."),
    figure(L.zones("Where to hold CO2 while the lights are on", 200, 2000,
            [(200, 400, L.BLUL, "low CO2: deficit"), (400, 800, L.GL, "outdoor air: yield gain"),
             (800, 1500, L.GXL, "enrichment target"), (1500, 2000, L.AMBL, "small yield gain: waste")],
            unit=" ppm",
            note="Hold approximately 1,000-1,500 ppm in the light period. Less than outdoor air: the plant has a deficit. More than 1,500 ppm: the gas is waste."), 4,
      "The range for operation. Keep the CO2 at approximately 1,000&ndash;1,500 ppm in the light "
      "period. The curve is horizontal at more than approximately 1,500 ppm. Thus, if you increase "
      "the CO2 to 2,000 ppm, most of the gas that you add is waste. Also, the risk to safety and "
      "the cooling load are higher" + _c("westmoreland2023-usu") + "."),
    callout("tip", "The effect of CO2 on yield and potency",
      p("CO2 is a lever for <strong>yield</strong>, not a lever for <strong>potency</strong>. CO2 "
        "causes the plant to make more flower mass. Thus the quantity of cannabinoid for each plant "
        "(in grams) increases. But CO2 does not increase %THC or %CBD by a large quantity, and its "
        "effect on terpenes is small. The result is a larger harvest, and the flower is not "
        "stronger.")),
    callout("warn", "The figures &lsquo;39% biomass, 43% flower&rsquo; from other sources",
      p("These numbers, and most of the &lsquo;20&ndash;40% uplift&rsquo; values, are on vendor "
        "blogs. There is no controlled test for these numbers. The test at Utah State University is "
        "the primary source with controlled data. It gives a yield gain of approximately 40% for "
        "the flowers at 1,200&ndash;1,400 ppm" + _c("westmoreland2023-usu") + ". If a vendor gives "
        "a more accurate number, do not accept it until you examine the test.")),
  ]})

# ---------------------------------------------------------------- 07
SECTIONS.append({"id": "delivery", "kicker": "07 · Supply of CO2", "title": "CO2 supply and dosing",
  "blocks": [
    p("There are four usual methods to put CO2 into a room. One method is clearly the best for a "
      "sealed cannabis room:"),
    table(["Method", "Operation", "Information"], [
      ["Compressed CO2 in a cylinder", "Cylinder &rarr; regulator &rarr; solenoid valve. An NDIR controller operates the valve.",
       "This method is more clean than the other methods. It makes no heat and no unwanted products, and it is accurate. We recommend that you use it for sealed rooms. A cylinder becomes empty, thus you must replace it."],
      ["Propane or gas burner", "The burner burns fuel to make CO2 (approximately 3&nbsp;lb of CO2 for each lb of fuel)",
       "The cost of the gas is low, but the burner adds heat and water vapor. If the fuel does not burn fully, the burner makes carbon monoxide (CO), ethylene and NOx. These gases cause damage to plants and injury to persons. A CO alarm is necessary."],
      ["Fermentation with yeast", "Sugar + yeast &rarr; CO2 + alcohol",
       "The output is very small, and you cannot control it. This method is only for hobby growers."],
      ["Dry ice", "Solid CO2 changes directly into gas",
       "You cannot control it. It continues for a short time. It also causes a risk of cold burn and a risk in a confined space."],
    ], cls="compact", caption="In a sealed room with a license, the standard selection is a cylinder of CO2 and a controller that uses a sensor."),
    callout("key", "How to calculate the dose",
      p("To increase the CO2 concentration of a sealed room, calculate the mass of CO2 in "
        "milligrams. <strong>Mass of CO2 (mg) = room volume (m&sup3;) &times; ppm to add &times; "
        "1.8.</strong> The value 1.8 is the mass of CO2 in one m&sup3; for each ppm at room "
        "temperature. The density of CO2 is 1.799&nbsp;g/L at 25&nbsp;&deg;C (77&nbsp;&deg;F). Thus "
        "1 ppm is 1.8&nbsp;mg/m&sup3;" + _c("niosh-co2") + ".</p><p><em>Example:</em> For a room of "
        "30&nbsp;m&sup3;, you add CO2 from 420 to 1,200 ppm (780 ppm). The result is 30 &times; 780 "
        "&times; 1.8 = 42,120&nbsp;mg &asymp; <strong>42&nbsp;g</strong> of CO2, approximately "
        "23&nbsp;liters of gas. This quantity is only for the first fill of the room. In a room "
        "with leaks, you must also add CO2 continuously.")),
    p("<strong>Time and airflow.</strong> Add CO2 only in the light period. Typically, start "
      "approximately one hour after the lights come on, and stop before the lights go off" +
      _c("wang2022-co2cue") + ". Use an NDIR CO2 sensor at the height of the canopy to control the "
      "CO2 at a setpoint. Do not use a timer without a sensor.</p><p>CO2 is heavier than air, thus "
      "it flows down. Install the supply pipe above the canopy. Use horizontal airflow (HAF) fans "
      "to mix the CO2 down. The fans decrease the thickness of the boundary layer at the leaf (a "
      "layer of air without movement and with a deficit of CO2)" + _c("kitaya2004-airvel") +
      "."),
    figure(L.flow("Closed-loop CO2 control, lights-on only",
            [("NDIR sensor", "reads CO2 at canopy"), ("Controller", "compares to setpoint"),
             ("Solenoid", "opens if CO2 is low"), ("CO2 supply", "CO2 from the cylinder"),
             ("HAF fans", "move CO2 to the leaf")],
            note="The loop operates only in the light period. At night it is closed. The plant does not use CO2."), 5,
      "A CO2 enrichment loop that uses a sensor. The controller adds CO2 to hold the setpoint in "
      "the light period. In the dark period, the controller stops the CO2 supply."),
  ]})

# ---------------------------------------------------------------- 08
SECTIONS.append({"id": "sealed", "kicker": "08 · Keep the CO2 in the room", "title": "Sealed rooms and ventilated rooms",
  "blocks": [
    p("In a ventilated room, most of the cost of the CO2 is waste. An exhaust fan replaces the air "
      "of the room with outdoor air of approximately 420 ppm. Thus the CO2 that you added decreases "
      "to the concentration of the outdoor air. The CO2 decreases in a curve. When the CO2 in the "
      "room is higher and the air changes at a higher rate, the CO2 decreases more quickly. If the "
      "exhaust fan and the CO2 supply operate at the same time, the exhaust fan removes the CO2 "
      "that you add."),
    p("A room with the fans off also has leaks. Measurements in commercial greenhouses show that "
      "more than half of the CO2 that the growers added went out through leaks in the structure. "
      "The CO2 use efficiency was less than <strong>50&ndash;60%</strong> at a setpoint of 1,000 ppm" +
      _c("wang2022-co2cue") + ".</p><p>Thus a <strong>sealed room</strong> is necessary for CO2 "
      "enrichment. Do not remove the heat and the humidity with exhaust air. Control them "
      "<em>in</em> the room. Use a recirculating mini-split air conditioner (AC) for the heat and a "
      "dehumidifier for the moisture. Thus the door stays closed and the CO2 stays in the room."),
    table(["", "Ventilated room", "Sealed room"], [
      ["Heat and humidity", "Exhaust air removes them from the room", "The AC and the dehumidifier remove them in the room"],
      ["CO2 enrichment", "The exhaust air removes the CO2, and the enrichment has no effect", "The room keeps the CO2. Thus the enrichment has an effect."],
      ["Air exchange", "High. There are many air changes for each hour.", "Low. The air changes only through leaks."],
      ["When to use it", "Use when you add no CO2, or only to prevent low CO2 in the day", "Use for all CO2 enrichment where the result is important"],
    ], cls="compact", caption="CO2 enrichment and exhaust airflow have opposite effects. Select a sealed room before you get the first gram of CO2."),
    callout("tip", "Air exchange in the dark period",
      p("It is necessary to do an air exchange in some conditions, to adjust the humidity or to "
        "remove stale air. Do it at <strong>lights-off</strong>, when the plants do not use CO2. "
        "Thus you do not remove the gas that you added. CO2 collects near the floor. Thus an "
        "exhaust near the floor removes it the most quickly.")),
  ]})

# ---------------------------------------------------------------- 09
SECTIONS.append({"id": "purge", "kicker": "09 · Outdoor air", "title": "Air exchange in sealed rooms",
  "blocks": [
    lead("You seal the room to keep the CO2 in the room. Then you must let outdoor air come in. The "
         "two instructions have opposite effects. Carbon filters and HEPA filters clean the air all "
         "the time. Thus a grower can think that an air exchange is not necessary.</p><p>Filters "
         "<em>clean</em> the air, but they do not <em>replace</em> it. The waste gases that the "
         "plants make cause most of the stale air. Heat and moisture also cause stale air. A carbon "
         "filter and a HEPA filter remove almost no part of the waste gases, the heat or the "
         "moisture."),
    p("The table shows the items that these filters remove and the items that they do not remove:"),
    table(["Filter", "Removes", "Does NOT remove"], [
      ["HEPA", "Particulates &ge;0.3&nbsp;&micro;m: mold spores, dust and pollen (99.97%)" + _c("epa-hepa"),
       "All gases, water vapor, heat, CO2, ethylene and oxygen"],
      ["Activated carbon", "Odor, and heavy VOCs and terpenes. Adsorption on the carbon removes them.",
       "CO2, humidity, heat and oxygen. Carbon holds ethylene only weakly, and it becomes full" + _c("souza2024-carbon-ethylene") + "."],
    ], cls="compact", caption="The two filters do not replace the air. They do not remove the gases that collect in a sealed room. They also do not remove the heat or the moisture."),
    p("The gas that makes an air exchange necessary is <strong>ethylene</strong> (C2H4). It is a "
      "plant hormone. <em>The plants</em> make it and release it. They release a small quantity all "
      "the time. They release much more when they have stress or wounds, after defoliation, or in "
      "the flowering stage" + _c("wheeler1996-ethylene") + ".</p><p>Ethylene has an effect on "
      "plants at very low concentrations. Sensitive crops show damage at <strong>10 ppb</strong> "
      "(0.01 ppm). In greenhouses, growers keep the ethylene at less than approximately 20 ppb" +
      _c("abeles1992-ethylene") + _c("cornell-ethylene") + "."),
    p("In a sealed space, the ethylene increases because of the plants only. NASA sealed a chamber "
      "with wheat, soybean, lettuce and potato plants. The ethylene increased to "
      "<strong>40&ndash;120 ppb</strong>. The plants made all this ethylene. This concentration was "
      "sufficient to cause a change in the shape of the wheat that you can see" +
      _c("wheeler1996-ethylene") + ".</p><p>In a controlled test on tomato, a stable <strong>20 ppb "
      "decreased the fruit yield to approximately half</strong>, and 40 ppb decreased it by "
      "approximately 90%. At the same time, the foliage showed almost no damage" +
      _c("hudelson2023-ethylene") + ". Ethylene also has an effect on cannabis. Cannabis has a full "
      "ethylene signaling system. The system is very sensitive. Thus ethylene changes the sex of "
      "the flower" + _c("monthony2026-ethylene") + "."),
    figure(L.zones("Ethylene: damage starts at very low values (ppb)", 0, 400,
            [(0, 10, L.GL, "clean air"), (10, 20, L.GXL, "maximum 20 ppb"),
             (20, 100, L.AMBL, "slow: stunting, bud abortion"), (100, 400, L.REDL, "fast: epinasty, abscission")],
            unit=" ppb",
            note="Ethylene has an effect on plants at 10 ppb. A sealed room makes 40-120 ppb. Carbon and HEPA filters do not remove it correctly. Air exchange or a KMnO4 scrubber does."), 6,
      "The scale of ethylene damage. The unit is ppb, one part in a <em>billion</em> parts. In a "
      "sealed room, the ethylene that the plants make increases to the range of slow damage" +
      _c("wheeler1996-ethylene") + _c("hudelson2023-ethylene") + "."),
    callout("warn", "Filters do not give protection from ethylene",
      p("A molecule of ethylene is small and light. Its width is approximately 0.4 nm. A HEPA "
        "filter cannot catch a gas. Activated carbon holds ethylene only weakly, and it becomes "
        "full quickly" + _c("souza2024-carbon-ethylene") + ". A carbon filter and a HEPA filter can "
        "operate all day. The ethylene from the plants increases more quickly than the carbon holds "
        "it.</p><p>Only two methods remove ethylene correctly. Do an <strong>air exchange</strong>, "
        "or install an <strong>ethylene scrubber</strong>. Use potassium permanganate media or a UV "
        "/ TiO2 photocatalytic unit. These scrubbers change the ethylene chemically. They "
        "<em>break</em> its molecules. They do not hold it for a short time" +
        _c("alvarez2024-ethylene") + ".")),
    callout("note", "Incorrect information about oxygen",
      p("Growers frequently think that an air exchange gives oxygen to the plants. It is not "
        "necessary for you to supply oxygen to the plants from the room air. The air in the room "
        "contains approximately 21% oxygen (approximately 209,000 ppm). For workers, the minimum "
        "oxygen concentration is 19.5%. This concentration is approximately 14,500 ppm less than "
        "usual air. A plant canopy removes much less oxygen than this quantity" + _c("osha-oxygen") +
        ".</p><p>Oxygen in the room air is not a problem. The oxygen that <em>is</em> important is "
        "in the <strong>root zone</strong>. The oxygen is in the water (dissolved oxygen) and in "
        "the air-filled porosity of the <a href='substrates-overview.html'>substrate</a>. "
        "Irrigation and the substrate change this oxygen. Air exchange does not change it. The only "
        "cause that decreases the oxygen and increases the CO2 of a room is the <em>persons</em> in "
        "the room.")),
    p("Ethylene is the primary cause for an air exchange, but stale air also has these items:"),
    ul(["<strong>Humidity.</strong> The roots of a plant move water up through the stems, and the "
        "water moves out of each leaf as vapor through small pores (stomata). This movement is "
        "<strong>transpiration</strong>. Transpiration moves most of the water that you irrigate "
        "out of the plant" + _c("hpac-latent") + ". A dehumidifier removes this vapor, and a filter "
        "does not. After the lights go off, the vapor continues to come if the transpiration is "
        "more than the dehumidifier can remove.",
        "<strong>Heat.</strong> The air conditioner removes the heat. The carbon filter does not remove it.",
        "<strong>The terpenes of the plants</strong> and other VOCs. Carbon catches them for some "
        "time. When the carbon is full, they go through it.",
        "<strong>Mold spores.</strong> A HEPA filter on the recirculation loop decreases the number "
        "of spores in the air" + _c("punja2019-pathogens") + ", but it cleans only the air that "
        "flows through it. In the inner part of a thick canopy, the humidity is 15&ndash;25% higher "
        "than the reading of your room sensor" + _c("zhang2020-canopy-rh") + ". This area of air "
        "without movement and with high humidity is where bud rot starts. An air exchange, and air "
        "movement <em>through</em> the canopy, decrease the disease. A filter on the average air of "
        "the room is not sufficient" + _c("baptista2012-ventilation") + " (the <a "
        "href='mould-risk.html'>mold</a> paper and the <a href='airflow-design.html'>airflow</a> "
        "paper give more information)."]),
    callout("key", "How to do an air exchange and keep the CO2",
      ul(["<strong>Do the air exchange at lights-off.</strong> The plants do not use CO2 in the "
          "dark period. Thus an air exchange at specified times in the dark period removes the "
          "ethylene, the VOCs and the humidity that collected. It does not remove CO2 that you "
          "supplied for the plants.",
          "<strong>Or use a scrubber and not an air exchange.</strong> A scrubber that uses "
          "potassium permanganate, or a photocatalytic unit, lets a fully sealed room keep its CO2. "
          "At the same time, it removes the ethylene" + _c("alvarez2024-ethylene") +
          ".",
          "<strong>Circulation is not the same as air exchange.</strong> HAF fans mix the air of "
          "the room. They decrease the thickness of the boundary layer at the leaf, which helps the "
          "CO2 to go to the stomata" + _c("kitaya2004-airvel") + ". But the fans move only the "
          "<em>same</em> air. Only outdoor air (or a scrubber) changes the gases that are in the "
          "air."])),
    p("Do an air exchange that is sufficient to keep the ethylene and the humidity low. It must not "
      "remove too much CO2 or dry the media. Closed plant environments have from less than 1 to "
      "approximately 15 air changes for each hour. One investigation of cannabis micropropagation "
      "found that approximately 4.4 air changes for each hour gave the best result. A higher rate "
      "dries the substrate and causes stress to the plants" + _c("liang2026-cannabis-ach") +
      " (that investigation was at plantlet scale. Thus the value is an indication, not a setpoint "
      "for a flower room). A sealed room is not a room without air exchange."),
  ]})

# ---------------------------------------------------------------- 10
SECTIONS.append({"id": "climate", "kicker": "10 · Other effects of CO2", "title": "Room conditions with CO2 enrichment",
  "blocks": [
    p("A change of the CO2 concentration causes changes in the other conditions of the room. The <a "
      "href='grow-room-systems.html'>grow-room systems</a> paper gives the same fact: the inputs of "
      "a room change at the same time. Three other conditions change with the CO2:"),
    table(["Lever", "Effect of high CO2", "Procedure"], [
      ["Temperature", "The best temperature for the plant increases by some degrees" + _c("lv2022-topt"),
       "<em>If</em> the light is strong, use approximately 28&ndash;30&nbsp;&deg;C (82&ndash;86&nbsp;&deg;F) and not approximately 25&nbsp;&deg;C (77&nbsp;&deg;F). The photosynthesis of cannabis has its peak at approximately 30&nbsp;&deg;C (86&nbsp;&deg;F)" + _c("chandra2008-photo")],
      ["Stomata and water", "High CO2 closes the stomata in part (the pores of the leaf for gas exchange). It decreases the stomatal conductance (how easily vapor moves through the pores) by approximately 42%. It decreases the leaf transpiration by approximately 29% for each leaf" + _c("chandra2008-photo"),
        "Each leaf uses less water. The total quantity of water that the crop uses can decrease, stay the same or increase. It changes with the leaf area, the PPFD, the temperature and the VPD (VPD is the capacity of the air to absorb moisture. When the temperature is higher and the humidity is lower, the air removes water from the leaf more quickly.) Measure the quantity of water that the crop uses."],
      ["Light", "No effect if the light is not high" + _c("rm2021-light"),
       "Use CO2 enrichment only in rooms with strong light. In other rooms, the CO2 is waste."],
      ["Feed", "When there is less transpiration, the concentration of salts at the root can increase",
       "Monitor the runoff EC and adjust the feed strength"],
    ], cls="compact", caption="When you increase the CO2, find the other conditions that must change. Growers frequently do not know about the changes of temperature and water."),
    callout("note", "Measure the quantity of water that all the crop uses",
      p("Chandra measured the leaf with 750 ppm CO2 and with 350 ppm CO2. With the higher "
        "concentration, the stomatal conductance was approximately 42% lower and the leaf "
        "transpiration was 29% lower. The instantaneous water-use efficiency of the leaf was 111% "
        "higher" + _c("chandra2008-photo") + ".</p><p>These measurements of the leaf do not give "
        "the total irrigation or the humidity load of the room. The result can change with the leaf "
        "area, the PPFD, the temperature, the VPD and the length of the crop cycle. The total "
        "quantity of water that the crop uses can increase or decrease. After you start CO2 "
        "enrichment, measure the irrigation input, the drainage, the substrate water content and "
        "the dehumidifier condensate. Do not think that the crop will use more water or less water.")),
  ]})

# ---------------------------------------------------------------- 11
SECTIONS.append({"id": "drying", "kicker": "11 · A risk that you cannot see", "title": "High CO2 concentration in drying rooms",
  "blocks": [
    p("A drying room has conditions that are opposite to the conditions of the flower rooms in this "
      "paper. You fill a sealed room with a large mass of biomass that you cut, from ten kilograms "
      "to many hundred kilograms. The room has no light and low airflow. The biomass continues "
      "<strong>respiration</strong> for days after the harvest. It releases CO2 all the time, and "
      "there is no photosynthesis to absorb the CO2 again" + _c("kader2002-respiration") +
      "."),
    p("Cut leaf and flower have a high rate of respiration. After the harvest, they are in the same "
      "group as leafy greens and cut herbs. A high temperature increases the rate (the same Q10 of "
      "2 again)" + _c("kader2002-respiration") + ".</p><p>A drying room at 15&ndash;18&nbsp;&deg;C "
      "(59&ndash;64&nbsp;&deg;F) with almost no air movement is a CO2 trap that holds almost all "
      "the CO2. In sealed greenhouses with plants, the CO2 concentration increases at night to "
      "600&ndash;1,000 ppm or more because of the living plants" + _c("ahdb-co2") +
      ". A room with much cut biomass and almost no airflow can have a much higher concentration. "
      "The concentration can be many thousand ppm. In the worst conditions, in a room without "
      "airflow, it can possibly increase to a concentration that you measure in percent."),
    callout("danger", "A drying room without airflow is a confined space",
      p("Ventilate a drying room before a person goes into it. Install a CO2 alarm. Do not let a "
        "person go into a full, closed drying room if the air exchange does not operate. The "
        "instruction is the same for a short check.</p><p>CO2 is heavier than air, and you cannot "
        "smell it. It collects near the floor, where a person stays. A sealed drying room that "
        "stays closed for one night can have a dangerous atmosphere near the floor.")),
    callout("note", "A limit of the data",
      p("No investigation with peer review measured the CO2 in a cannabis drying room directly. We "
        "know the cause (the respiration of the biomass in the dark period) and the safety limits "
        "for persons in the next section. But the maximum CO2 concentration in a given room is an "
        "estimate. It is not a measured value for cannabis.</p><p>The correct procedure is to "
        "<strong>install a meter in your drying room and measure the CO2</strong>. Do not use an "
        "estimate for your room. The <a href='harvest-dry-trim-cure.html'>harvest, dry, trim and "
        "cure</a> paper gives all the information about the drying environment.")),
  ]})

# ---------------------------------------------------------------- 12
SECTIONS.append({"id": "safety", "kicker": "12 · The risk that can kill a person", "title": "CO2 exposure limits and worker safety",
  "blocks": [
    lead("If you read only one section of this paper, read this section. Your CO2 enrichment "
         "setpoint of 1,000&ndash;1,500 ppm is much less than each worker limit. It is safe for a "
         "person who stays in the room for a short time.</p><p>The risk is in these conditions: a "
         "regulator with a leak, or a room with too much CO2 from the supply. Other conditions are "
         "a burner fault and a sealed drying room. Each of these conditions can cause a CO2 "
         "concentration that kills a person, and you get no indication of it."),
    figure(L.zones("Enrichment is much less than the worker limit", 0, 5000,
            [(0, 420, L.BLUL, "outdoor air"), (420, 1500, L.GL, "enrichment target"),
             (1500, 5000, L.AMBL, "to the 5,000 ppm 8-hour worker limit")],
            unit=" ppm",
            note="Your grow-room setpoint (green) is 3 to 5 times less than the 5,000 ppm worker exposure limit. The setpoint is not the problem. A leak that increases the CO2 is the problem."), 7,
      "The usual enrichment range and the worker exposure limit. When you operate enrichment "
      "correctly, the CO2 is much less than the dangerous values. Thus it is easy to ignore a leak "
      "that increases the CO2 without control, until the CO2 is dangerous" + _c("osha-pel-co2") +
      "."),
    p("Each primary safety authority gives the same limit. The limit for the 8-hour average CO2 "
      "concentration that a worker can breathe is <strong>5,000 ppm (0.5%)</strong>. These "
      "authorities are OSHA in the US" + _c("osha-pel-co2") + ", NIOSH and ACGIH" + _c("niosh-co2") +
      ", and WorkSafe New Zealand" + _c("worksafenz-co2") + ". When the concentration is more than "
      "this limit, the effects increase quickly:"),
    table(["CO2 concentration", "Effect", "Reference"], [
      ["approximately 420 ppm", "Usual outdoor air", "Baseline" + _c("noaa2024-co2")],
      ["1,000&ndash;1,500 ppm", "Usual enrichment target. It is safe for short tasks.", "3 to 5 times less than the worker limit"],
      ["1,000&ndash;2,500 ppm", "Some reports show small effects on cognition. The reports do not agree with each other.", "An effect on cognition. It is not dangerous" + _c("azuma2018-cognition")],
      ["5,000 ppm (0.5%)", "8-hour worker exposure limit (TWA)", "OSHA / NIOSH / ACGIH / WorkSafe NZ" + _c("worksafenz-co2")],
      ["30,000 ppm (3%)", "The 15-minute short-term limit (STEL). A person has a headache and breathes quickly.", "NIOSH / ACGIH / WorkSafe NZ" + _c("niosh-co2")],
      ["40,000 ppm (4%)", "IDLH, immediately dangerous to life or health", "A person cannot easily go away from the area" + _c("niosh-co2")],
      ["50,000 ppm (5%)", "Hypercapnia and respiratory acidosis in approximately 30 min", "The CO2 is directly poisonous. It is not only low oxygen" + _c("permentier2017-co2poison")],
      ["70,000&ndash;100,000 ppm (7&ndash;10%)", "Unconsciousness occurs in some minutes", "A person cannot do self-rescue" + _c("permentier2017-co2poison")],
      ["&gt;300,000 ppm (&gt;30%)", "Loss of consciousness occurs in seconds", "In accidents that killed persons, the CO2 was 14&ndash;26%" + _c("permentier2017-co2poison")],
    ], cls="compact", caption="The effects of CO2 at different concentrations. The difference is large: the enrichment range is safe, but the concentrations that a leak can cause in a sealed room are not safe."),
    callout("danger", "At more than 5%, CO2 is directly poisonous to the blood",
      p("Ventilate a sealed room with a high CO2 concentration before you go into it. Do a test of "
        "the air before you go in. Do this each time. A sealed room with a high CO2 concentration "
        "is a confined space.</p><p>CO2 at more than approximately 5% is directly poisonous. It "
        "makes the blood acid. Papers that examine CO2 accidents show that this poisonous effect "
        "kills the person. It occurs before the oxygen concentration is dangerously low" +
        _c("permentier2017-co2poison") + ". Thus unconsciousness can occur very quickly, and the "
        "person cannot open a door. The CO2 frequently kills persons who go in without protection "
        "to help the first person.")),
  ]})

# ---------------------------------------------------------------- 13
SECTIONS.append({"id": "monitoring", "kicker": "13 · Measurement and alarms", "title": "CO2 sensors, alarms and the limits of MQ sensors",
  "blocks": [
    p("You cannot control CO2, and you cannot be safe from CO2, if you do not measure it. Many "
      "sensors that you can get do not measure CO2. The correct sensor type is "
      "<strong>NDIR</strong> (non-dispersive infrared). It reads the CO2 from its infrared signature" +
      _c("sensirion-scd") + ".</p><p>Vendors give the name &lsquo;CO2 sensors&rsquo; to low-cost "
      "&lsquo;MQ&rsquo; metal-oxide sensors. These sensors are not correct. The table shows this:"),
    table(["Sensor", "Does it measure CO2?", "Result"], [
      ["NDIR (SCD30, SCD41, MH-Z19 and other models)", "Yes. It uses infrared light for CO2 only.", "Correct for control and for safety" + _c("sensirion-scd")],
      ["MQ-135", "No. It calculates an &lsquo;equivalent CO2&rsquo; from a mixture of VOCs.", "The reading is not a correct CO2 value. Do not use it" + _c("winsen-mq")],
      ["MQ-5", "No. It is for LPG and for gases that can burn.", "It is for a different gas" + _c("winsen-mq")],
    ], cls="compact", caption="If a &lsquo;CO2 node&rsquo; uses an MQ-135 or MQ-5 sensor, it does not measure CO2. Use only NDIR sensors for control and for the safety of persons."),
    callout("warn", "Calibration in a sealed room",
      p("<strong>Do not use Automatic Baseline Calibration (ABC). Calibrate the sensor "
        "manually</strong> with outdoor air or a reference gas at specified times.</p><p>NDIR "
        "sensors have drift. Thus they calibrate automatically with ABC. ABC uses the lowest CO2 "
        "value that the sensor measures as the value of outdoor air, 400&nbsp;ppm. In a sealed room "
        "with continuous CO2 enrichment, the sensor <em>does not</em> measure 400 ppm. Thus ABC "
        "slowly causes an incorrect calibration, and the readings become lower than the correct "
        "value" + _c("sensirion-scd") + ".")),
    p("<strong>Two sensors, two tasks.</strong> Install a control sensor at the height of the "
      "canopy. This sensor controls the CO2 at the setpoint. Install a second sensor low on the "
      "wall, approximately 30&nbsp;cm (12&nbsp;in) from the floor. This sensor is for the "
      "<em>safety of persons</em>. CO2 collects near the floor.</p><p>For larger systems, the "
      "International Fire Code (Section 5307) makes this mandatory. Each installation with more "
      "than 100&nbsp;lb of CO2 must have gas detection. The system gives an alarm at 5,000&nbsp;ppm "
      "and a strong alarm at 30,000&nbsp;ppm. It also stops the CO2 supply automatically and starts "
      "the exhaust airflow" + _c("ifc5307") + ". Also for installations with less than this "
      "quantity, an alarm and an occupancy interlock give protection at a low cost."),
  ]})

# ---------------------------------------------------------------- 14
SECTIONS.append({"id": "worth", "kicker": "14 · The facts", "title": "Expected results and limitations",
  "blocks": [
    p("In a sealed room with strong light, CO2 enrichment is one of the changes that give the "
      "largest yield gain for the cost. In all other rooms, the cost is waste" + _c("okstate-co2") +
      ". The cost of the gas is low. The payback changes with the condition of the room."),
    grid([
      card("Use CO2 enrichment when:",
           ul(["The room is <strong>sealed</strong> (AC and dehumidifier, not exhaust)",
               "The light is <strong>strong</strong> (high PPFD and DLI)" + _c("rm2021-light"),
               "The temperature, the water and the feed are correct",
               "The room has a CO2 <strong>alarm and interlock</strong>"]), tag="recommended"),
      card("Do not use CO2 enrichment when:",
           ul(["The room has an <strong>exhaust fan</strong>. The exhaust air removes the CO2" + _c("wang2022-co2cue"),
               "The light is <strong>low</strong>. The plants cannot use the CO2" + _c("chandra2008-photo"),
               "You want to increase the CO2 to more than approximately 1,500 ppm to get more yield" + _c("westmoreland2023-usu"),
               "You cannot monitor the CO2 safely at this time"]), tag="not recommended"),
    ], cols=2),
    table(["Problem", "Possible cause", "Correction"], [
      ["More CO2, but the yield is not higher", "The light is too low, or the room is not sealed", "Increase the PPFD. Seal the room. Do this before you think that the gas is the cause."],
      ["The CO2 does not stay at the setpoint", "The room has leaks, or the exhaust fan operates when you add CO2", "Seal the leaks. Use the exhaust only at lights-off."],
      ["The plants show wilt, or the substrate stays wet", "Plants with CO2 enrichment have a lower transpiration rate. The irrigation quantity that you used before the CO2 enrichment is too high at this time.", "Adjust the VPD. Decrease the irrigation volume" + _c("chandra2008-photo")],
      ["Damage to the leaves when you use a burner", "The fuel does not burn fully. The burner makes CO, ethylene and NOx.", "Do maintenance on the burner. Install a CO alarm. Or use CO2 from a cylinder."],
      ["The sensor reading becomes lower in some weeks", "ABC causes an incorrect calibration in a sealed room", "Do not use ABC. Calibrate the sensor manually" + _c("sensirion-scd")],
    ], cls="compact", caption="The usual CO2 problems. Almost always, the cause is the room, the light or the sensor, not the CO2."),
    callout("key", "The four primary instructions",
      ul(["<strong>Light first, CO2 second.</strong> CO2 increases the effect of strong light. It cannot replace light.",
          "<strong>Seal the room before you add CO2.</strong> If you do not seal a room with CO2 enrichment, the CO2 is waste.",
          "<strong>Measure with NDIR. Use an alarm for the safety of persons.</strong> Control and safety use two sensors, not one.",
          "<strong>Add CO2 in the light period. Do an air exchange in the dark period.</strong> The plant absorbs CO2 only while the lights are on."])),
    p("Read the <a href='grow-room-systems.html'>grow-room systems</a> paper, the <a "
      "href='airflow-design.html'>airflow</a> paper and the <a "
      "href='harvest-dry-trim-cure.html'>harvest and dry</a> paper with this paper. CO2 enrichment "
      "gives a good result only as part of the full system."),
  ]})
