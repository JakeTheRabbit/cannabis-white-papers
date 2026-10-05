# -*- coding: utf-8 -*-
"""Paper: temperature, humidity and VPD — psychrometrics for growers without the textbook."""
import json, os
from components import (p, lead, h, ul, ol, callout, defterm, table, figure, grid, card,
                        chip, kv, steps)
import figs_lib as L

_FIGS = json.load(open(os.path.join(os.path.dirname(__file__), "figs_temp_humidity_vpd.json"),
                       encoding="utf-8"))

SLUG = "temp-humidity-vpd"
TITLE = "Temperature, humidity and VPD: stage targets, measurement and condensation control"
EYEBROW = "Environment · Climate"
SUB = ("Vapor pressure deficit (VPD) is the value that shows how much water the air removes from "
       "the leaves. This paper gives the definition of VPD and shows how to calculate it. It shows "
       "that the leaf temperature gives the correct deficit. It gives the targets for each stage "
       "and the sources of the targets. It also gives the control of the dew point at night, which "
       "prevents mold. It shows how to put the sensors in the correct position and how to read them "
       "accurately.")
META = [("wave", "Climate"), ("image", "12 diagrams"),
        ("quote", "14 sources"), ("clock", "~19 min to read")]
RELATED = ["grow-room-systems", "mould-risk", "airflow-design"]
REF_IDS = ["fao56-1998", "grossiord2020-vpd", "nelson2015-leaftemp", "corredor2025-rh",
           "jin2019-cannabis-env", "pulse-vpd-guide", "chandra2008-photo", "inoue2021-vpd",
           "caird2007-night", "moe1995-dif", "punja2025-budrot-epi", "zhang2020-canopy-rh",
           "tarara2007-shield", "hpac-latent"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

# ---------------------------------------------------------------- 01 start here
SECTIONS.append({"id": "start-here", "kicker": "01 · Start here", "title": "Purpose and scope",
  "blocks": [
    lead("Two rooms show a relative humidity (RH) of 55%. One room is at 20&nbsp;°C (68&nbsp;°F), "
         "and the plants are in good condition. The other room is at 28&nbsp;°C (82&nbsp;°F). In "
         "this room, the growth of the same cultivar stops, the leaf edges bend up, and the plants "
         "use a large quantity of water.</p><p>The number on the controller is the same, but the "
         "two rooms are very different. RH is a percentage of a value that changes with the "
         "temperature. A percentage has no effect on the plant. The <strong>force</strong> with "
         "which the air pulls water out of the leaves has an effect on the plant."),
    p("This force has a name: <strong>vapor pressure deficit</strong> (VPD). VPD is the value that "
      "the temperature and the humidity make together. Air can contain water vapor up to a maximum, "
      "and this maximum changes with the temperature of the air. VPD is the difference between this "
      "maximum and the vapor pressure of the water that is in the air" + _c("fao56-1998") +
      ".</p><p>Each leaf transpires into this difference. When the difference is small, the force "
      "is weak. When the difference is large, the force is strong, until the plant closes its pores "
      "to keep the water in the plant" + _c("grossiord2020-vpd") + "."),
    p("This paper gives only the necessary information about the physics of moist air. It gives the "
      "definition of VPD and a formula that you can use in a calculator. It shows that the "
      "<em>leaf</em> temperature is the correct value for the formula. It also shows how the type "
      "of light fixture changes the leaf temperature. It gives the VPD bands for each stage. A band "
      "is the range of VPD values for one stage.</p><p>It also gives the sources of the bands, the "
      "targets for the day and the night, and the control of the dew point. This control prevents "
      "bud rot. It shows how to measure all these values and prevent incorrect sensor readings. It "
      "is not necessary to know physics before you read this paper. The paper gives the definition "
      "of each term."),
  ]})

# ---------------------------------------------------------------- 02 vocabulary
SECTIONS.append({"id": "vocabulary", "kicker": "02 · The terms", "title": "Definitions",
  "blocks": [
    defterm("Water vapor", "Water as a gas, mixed in the air. You cannot see water vapor. You can "
            "see drops of liquid water in the air."),
    defterm("Vapor pressure", "The part of the air pressure that the water vapor causes. The unit "
            "is the kilopascal (kPa). It is the accurate value for the quantity of water in the air."),
    defterm("Saturation vapor pressure (es)", "The maximum vapor pressure that air can contain at "
            "a given temperature. At this value, water starts to condense. The value increases at a "
            "high rate when the temperature increases" + _c("fao56-1998") + "."),
    defterm("Actual vapor pressure (ea)", "The vapor pressure of the water that is in the air at "
            "this time. This value is always equal to or less than the saturation vapor pressure."),
    defterm("Relative humidity (RH)", "The actual vapor pressure as a percentage of the saturation "
            "vapor pressure: ea &divide; es &times; 100. RH without the temperature does not give "
            "sufficient information. The temperature is also necessary."),
    defterm("Vapor pressure deficit (VPD)", "The difference: es &minus; ea, in kPa. VPD shows how "
            "much water the air can remove from the leaves. This value has an effect on the plant."),
    defterm("Leaf VPD", "The same difference, but you calculate it with the <em>leaf</em> "
            "temperature and not with the air temperature. The air in a leaf is at saturation at "
            "the temperature of the leaf. Thus leaf VPD is the value that causes transpiration" +
            _c("grossiord2020-vpd") + "."),
    defterm("Dew point", "The temperature at which water in the air starts to condense when you "
            "decrease the temperature of the air. When a surface is at a temperature less than the "
            "dew point, water condenses on the surface. The dew point shows the risk of mold."),
    defterm("Transpiration", "Transpiration is the evaporation of water from the leaf, through the "
            "pores of the leaf. The water that leaves the leaf pulls water, and the dissolved "
            "nutrients in the water, up from the roots."),
    defterm("Stomata", "The pores of the leaf, usually on the bottom side of the leaf. Water vapor "
            "leaves the leaf, and CO2 goes into the leaf, through these pores. The plant can change "
            "the size of each pore. Guard cells open and close the pores in minutes. One pore is a "
            "stoma."),
  ]})

# ---------------------------------------------------------------- 03 what VPD is
SECTIONS.append({"id": "what-vpd-is", "kicker": "03 · The physics", "title": "Basic information about VPD",
  "blocks": [
    p("The quantity of vapor that air can contain changes with the temperature. When the "
      "temperature of the air increases, the air can contain <em>more</em> vapor. The quantity of "
      "water that is in the air does not change because the temperature of the room increases. Only "
      "the difference between the saturation vapor pressure (es) and the actual vapor pressure (ea) "
      "changes. This difference is VPD."),
    figure(_FIGS["vpd-anatomy"], 1,
      "Two rooms with the same RH of 60%. The percentage is the same, but the difference that the "
      "plant transpires into is 60% larger in the warm room. Thus a value of RH does not give the "
      "full information about a climate."),
    p("VPD has an effect on plants, but RH does not. Water moves out of a leaf by diffusion. The "
      "difference in vapor pressure between the saturated air in the leaf and the air of the room "
      "around the leaf causes the diffusion. The ratio of the two vapor pressures does not cause "
      "the diffusion" + _c("grossiord2020-vpd") + ". The air of two rooms with the same RH can "
      "remove water from the crop at very different rates. The air of two rooms with the same VPD "
      "removes water at the same rate, for all values of RH."),
    figure(_FIGS["es-curve"], 2,
      "The saturation curve from the FAO-56 Tetens formula" + _c("fao56-1998") +
      ". The saturation vapor pressure increases approximately 6% for each degree. It becomes two "
      "times larger between 14&nbsp;°C (57&nbsp;°F) and 25&nbsp;°C (77&nbsp;°F). Thus a change of "
      "temperature causes a larger change of VPD than most changes of humidity."),
    p("The curve is the most important physics for the control of the climate. It gives the cause "
      "of three problems with humidity in a grow room. First, the RH in the room increases quickly "
      "to 90% at lights-off. The cause is that the saturation vapor pressure decreases and the "
      "quantity of water stays the same. Second, a heater makes the air drier, but the heater does "
      "not remove a gram of water. Third, in summer the plants use much more water at the same RH."),
    figure(L.bars("Water that saturated air can contain",
        [("10 °C (50 °F)", 9.4), ("15 °C (59 °F)", 12.8), ("20 °C (68 °F)", 17.3), ("25 °C (77 °F)", 23.0), ("30 °C (86 °F)", 30.4)],
        unit=" g/m³",
        note="Grams of water for each cubic meter of air at 100% RH, calculated from the FAO-56 saturation values."), 3,
      "The same maximum, in grams. A room at 30&nbsp;°C (86&nbsp;°F) can contain almost two times "
      "the quantity of water of a room at 20&nbsp;°C (68&nbsp;°F). Thus a decision about the "
      "temperature is also a decision about the humidity" + _c("fao56-1998") +
      "."),
    callout("key", "The short model",
      p("RH is a percentage of a maximum that changes. VPD <em>is</em> the difference. The difference has an effect on the plant.")),
  ]})

# ---------------------------------------------------------------- 04 the equation
SECTIONS.append({"id": "equation", "kicker": "04 · The formula", "title": "How to calculate VPD",
  "blocks": [
    p("All the values in this paper use one formula for the saturation vapor pressure. The formula "
      "is the result of measurements, and it is accurate to a fraction of one percent at the "
      "temperatures of a grow room. It is the Tetens formula of FAO Irrigation and Drainage Paper 56" +
      _c("fao56-1998") + ". T is the temperature in &deg;C, and the result is in kPa:"),
    callout("note", "The saturation vapor pressure",
      p("<strong>es(T) = 0.6108 &times; e<sup>(17.27 &times; T) / (T + 237.3)</sup></strong> kPa"
        "<br>Then: &nbsp;<strong>ea = es(T<sub>air</sub>) &times; RH / 100</strong> &nbsp;and&nbsp; "
        "<strong>VPD<sub>air</sub> = es(T<sub>air</sub>) &minus; ea = es(T<sub>air</sub>) &times; "
        "(1 &minus; RH/100)</strong>")),
    p("This example shows how to calculate the air VPD in steps. The air VPD is the VPD that you calculate with the air temperature. The numbers are the same as in all of this paper:"),
    kv([("Air temperature", "25.0 °C (77.0 °F)"),
        ("Relative humidity", "60%"),
        ("Saturation vapor pressure es(25)", "0.6108 × e^(431.75 / 262.3) = 3.17 kPa"),
        ("Actual vapor pressure ea", "3.17 × 0.60 = 1.90 kPa"),
        ("Air VPD", "3.17 − 1.90 = 1.27 kPa")]),
    p("You can use a table and not the formula. The table gives the values of es for the "
      "temperatures of most rooms. Multiply the value of es by (1 &minus; RH/100). The result is "
      "the VPD:"),
    table(["Air temperature", "es (kPa)", "VPD at 50% RH", "VPD at 60% RH", "VPD at 70% RH"], [
      ["18 °C (64 °F)", "2.06", "1.03", "0.83", "0.62"],
      ["20 °C (68 °F)", "2.34", "1.17", "0.94", "0.70"],
      ["22 °C (72 °F)", "2.64", "1.32", "1.06", "0.79"],
      ["24 °C (75 °F)", "2.98", "1.49", "1.19", "0.90"],
      ["26 °C (79 °F)", "3.36", "1.68", "1.34", "1.01"],
      ["28 °C (82 °F)", "3.78", "1.89", "1.51", "1.13"],
      ["30 °C (86 °F)", "4.25", "2.12", "1.70", "1.27"],
    ], cls="compact", caption="Saturation vapor pressure and air VPD, calculated with the FAO-56 formula" + _c("fao56-1998") + ". The values have two decimals."),
    callout("tip", "Units",
      p("1 kPa = 10 mbar = 10 hPa. Some charts from the US use other units, for example psi or "
        "grains of moisture. Do not use these units. The cultivation literature and all good "
        "controllers use kPa. The values that you will see in a grow room are in the range of "
        "approximately 0.2 (air with a very high humidity) to 2.5 (air with a very low humidity).")),
  ]})

# ---------------------------------------------------------------- 05 leaf VPD
SECTIONS.append({"id": "leaf-vpd", "kicker": "05 · The correct value", "title": "Leaf temperature and leaf VPD",
  "blocks": [
    p("This correction is important if you want to control VPD and not only record it. The air "
      "<em>in</em> a leaf is at saturation at the temperature of the <em>leaf</em>. Thus the "
      "gradient that causes transpiration is not es(air) &minus; ea. It is <strong>es(leaf) &minus; "
      "ea</strong>" + _c("grossiord2020-vpd") + ". When the leaf and the air are at the same "
      "temperature, the two values are the same. But the two temperatures are not always the same."),
    p("The temperature of a canopy in good condition that transpires is near the air temperature. "
      "The difference is usually a maximum of approximately 2&nbsp;°C for all light sources. But "
      "the leaf temperature can be <em>higher or lower</em> than the air temperature, and the "
      "radiation on the canopy is the primary cause" + _c("nelson2015-leaftemp") +
      ". The difference between the leaf temperature and the air temperature is the leaf "
      "offset.</p><p>An HPS lamp gives a large quantity of radiation to the canopy, and the "
      "temperature of the leaves becomes higher than the air temperature. An LED fixture removes "
      "most of its heat at the heat sink. A leaf that transpires removes heat by evaporation, and "
      "the temperature of this leaf is frequently <em>lower</em> than the air temperature. At equal "
      "light intensity, a model gives a difference of approximately 1.3&nbsp;°C between the two "
      "types of light" + _c("nelson2015-leaftemp") + ". In the tools that growers use, the usual "
      "value for the temperature of an LED canopy is 1&ndash;3&nbsp;°C less than the air temperature" +
      _c("pulse-vpd-guide") + "."),
    figure(_FIGS["leaf-offset"], 4,
      "The room shows the same values, but the plant has different conditions. A difference of a "
      "small number of degrees between the leaf and the air changes the calculated VPD by the width "
      "of one stage band" + _c("nelson2015-leaftemp") + "."),
    p("Do the example again with the measured temperatures of the leaf. The result changes. Air at "
      "25&nbsp;°C (77&nbsp;°F) and 60% RH gives 1.27 kPa. This VPD is usual for flowering.</p><p>If "
      "the LED canopy is at 23&nbsp;°C (73&nbsp;°F), the leaf VPD is es(23) &minus; 1.90 = "
      "<strong>0.91 kPa</strong>. This VPD is for the vegetative stage, and the climate is a third "
      "wetter than the dashboard shows. If the leaf in an HPS room is at 26&nbsp;°C (79&nbsp;°F), "
      "the leaf VPD is <strong>1.46 kPa</strong>. This VPD is at the top of the band for flowering. "
      "The room is the same, but there are three different results."),
    callout("warn", "The problem in a room with LED fixtures",
      p("Most rooms that change from HPS to LED fixtures keep the targets for temperature and "
        "humidity of the HPS lamps. The air VPD looks correct, but the <em>leaf</em> VPD is one "
        "band lower. As a result, the crop is wetter. The growth is softer, the drybacks are "
        "slower, and the room is nearer to condensation at night.</p><p>If the mold pressure "
        "increased after you changed the fixtures, it is possible that the leaf offset is the "
        "cause. Increase the air temperature by one or two degrees, or decrease the RH. Then "
        "compare the values with the <em>leaf</em> VPD.")),
    callout("danger", "A hot leaf shows a problem and not an offset",
      p("If your IR thermometer shows that a leaf is hot, examine the root zone before you change "
        "the climate. The offsets above are for a canopy that transpires and has sufficient water. "
        "A leaf with drought stress closes its stomata. As a result, evaporation does not decrease "
        "the temperature of the leaf. The temperature of this leaf can be 6&ndash;12&nbsp;°C higher "
        "than the air temperature" + _c("nelson2015-leaftemp") + ". The hot leaf shows that the "
        "plant does not transpire, and a correction of the chart does not help.")),
  ]})

# ---------------------------------------------------------------- 06 the chart
SECTIONS.append({"id": "the-chart", "kicker": "06 · The chart", "title": "Use of a VPD chart",
  "blocks": [
    p("The usual chart for growers shows the results of the formula. The temperature is on the "
      "side, the RH is at the top, and each cell shows the VPD. The colors show the stage bands of "
      "the next section:"),
    figure(_FIGS["vpd-chart"], 5,
      "Temperature &times; RH &rarr; kPa, for the air VPD. The chart shows the relation between "
      "temperature and RH. One degree of temperature changes the VPD by approximately the same "
      "quantity as two to three points of RH."),
    steps([
      ("Measure where the plants are", "Measure the air temperature and the RH at the height of the canopy, in the middle of the room. Do not measure at the controller on the wall. The position of the sensor is as important as the instrument (section 11)."),
      ("Measure the leaf temperature", "Use an IR thermometer or a canopy sensor on a leaf at the top of the canopy that receives light. If you cannot measure the leaf temperature, use these values. In an HPS room, the leaf temperature is approximately the same as the air temperature. In an LED room, the leaf temperature is 1–2 °C less than the air temperature" + _c("nelson2015-leaftemp") + "."),
      ("Read the cell", "Find the row for your temperature and the column for your RH. The value in the cell, in kPa, shows how much water the air can remove from the crop."),
      ("Correct the value for the leaf", "When the leaf is colder than the air, the correct VPD is lower than the value in the cell. When the leaf is hotter than the air, the correct VPD is higher. At 25 °C (77 °F) and 60%, a canopy that is 2 °C colder than the air changes 1.27 kPa to 0.91 kPa. Do not make an estimate of the correction. Use a calculator for the leaf offset or a controller that uses the leaf temperature" + _c("pulse-vpd-guide") + "."),
      ("Move along one axis of the chart each time", "If the air is too dry, increase the RH (move left in the chart) before you increase the temperature (move up in the chart). Make one change. After fifteen minutes, read the values again."),
    ]),
    callout("tip", "Two different climates with the same VPD value",
      p("27&nbsp;°C (81&nbsp;°F) with 65% RH and 21&nbsp;°C (70&nbsp;°F) with 45% RH give a VPD of "
        "approximately 1.3 kPa. But the two climates are not the same, because the temperature has "
        "effects on the plant that are different from the effects of VPD.</p><p>The photosynthesis "
        "of cannabis has a maximum at approximately 25&ndash;30&nbsp;°C (77&ndash;86&nbsp;°F)" +
        _c("chandra2008-photo") + ". The morphology and the stretch change with the difference "
        "between the day temperature and the night temperature" + _c("moe1995-dif") +
        ". The disease pressure changes with the absolute humidity. First select the temperature "
        "that is necessary for your stage and your fixture. Then use the humidity to adjust the VPD "
        "at this temperature.")),
  ]})

# ---------------------------------------------------------------- 07 stage targets
SECTIONS.append({"id": "stage-targets", "kicker": "07 · The targets", "title": "VPD targets for each stage",
  "blocks": [
    p("The bands below are the usual method that growers use. Physics does not give these bands. "
      "The bands are the result of the methods of growers, which became almost the same in a period "
      "of ten years" + _c("pulse-vpd-guide") + ". The bands are in the ranges that the literature "
      "on cannabis production recommends" + _c("jin2019-cannabis-env") + ".</p><p>The only "
      "controlled test of the humidity for cannabis that we have shows the wet limit of the bands. "
      "In this test, the VPD for flowering was 0.05&ndash;0.25 kPa and not approximately "
      "0.9&ndash;1.3 kPa. The flower biomass decreased by 71%, flowering started three weeks after "
      "the usual time, and the cannabinoid concentration decreased by a large quantity" +
      _c("corredor2025-rh") + ".</p><p>Start in the middle of the band. Then use your cultivar, the "
      "light intensity and your mold limit to select the value in the band."),
    figure(L.zones("Stage bands on one axis (leaf VPD, kPa)", 0, 2.4,
        [(0, 0.4, "var(--fig-waterl)", "too wet"),
         (0.4, 0.8, "var(--fig-blue-l)", "clone 0.4–0.8"),
         (0.8, 1.2, "var(--fig-green-l)", "vegetative 0.8–1.2"),
         (1.2, 1.6, "var(--fig-dryl)", "flower 1.2–1.5"),
         (1.6, 2.0, "var(--fig-amber-l)", "monitor"),
         (2.0, 2.4, "var(--fig-red-l)", "stress")],
        unit=" kPa",
        note="The bands are a usual method. Start at the middle. Then adjust for the plant and the night mold limit."), 6,
      "One axis for the full crop cycle. The bands become drier when the plant has more roots and "
      "more leaf area. The plant then has more capacity to move water and more tolerance to a high "
      "VPD" + _c("pulse-vpd-guide") + _c("jin2019-cannabis-env") + "."),
    table(["Stage", "Leaf VPD band", "Because", "Example of temperature and RH (air VPD)"], [
      ["Clones and new seedlings", "0.4–0.8 kPa", "There are no roots or only a small number of roots. The shoot must not transpire more than the uptake of water.",
       "24 °C (75 °F) and 75–80% RH give approximately 0.6–0.7 kPa"],
      ["First part of the vegetative stage", "0.8–1.1 kPa", "The plant has roots. Increase the gas exchange, but do not cause stress to the plant.",
       "25 °C (77 °F) and 65–70% RH give approximately 1.0 kPa"],
      ["Last part of the vegetative stage", "0.9–1.2 kPa", "The canopy is full and the light intensity is high. Keep the flux of water high and stable.",
       "26 °C (79 °F) and 62–68% RH give approximately 1.1–1.3 kPa"],
      ["First and middle part of flowering", "1.1–1.4 kPa", "Make the flow of water and nutrients high during the peak of bulking.",
       "26 °C (79 °F) and 58–62% RH give approximately 1.3–1.4 kPa"],
      ["Last part of flowering", "1.2–1.5 kPa", "The buds have a high density. At this time, the mold limit is more important than the VPD target.",
       "24 °C (75 °F) and 50–55% RH give approximately 1.4–1.5 kPa"],
    ], cls="compact",
      caption="The usual method" + _c("pulse-vpd-guide") + _c("jin2019-cannabis-env") +
      _c("corredor2025-rh") + ". The example values are for a leaf temperature that is "
      "approximately the same as the air temperature. In an LED room, make the air temperature "
      "higher or the RH lower to get the same leaf VPD."),
    callout("note", "Limits of the data for these bands",
      p("No dose&ndash;response curve of cannabis yield against VPD is available for all stages. "
        "The bands are estimates from the physiology of the plant, from the literature on "
        "production, and from the methods in many rooms.</p><p>The data show three results clearly. "
        "A climate that is much too wet decreases the yield by a large quantity" + _c("corredor2025-rh") +
        ". A climate that is much too dry closes the stomata and decreases photosynthesis" +
        _c("grossiord2020-vpd") + ". A stable VPD is more important than a VPD at the best value. "
        "Plants at a stable VPD in the middle of the range become larger. Plants at a VPD that "
        "increases and decreases around the best value are smaller" + _c("inoue2021-vpd") +
        ".")),
  ]})

# ---------------------------------------------------------------- 08 transpiration
SECTIONS.append({"id": "transpiration", "kicker": "08 · Transpiration and growth", "title": "The effect of VPD on transpiration",
  "blocks": [
    p("Transpiration moves water from the root zone to the air. Water evaporates from the walls of "
      "the cells in the leaf. The water vapor leaves the leaf through the stomata, by diffusion, "
      "into the drier air of the room. The water that leaves the leaf causes tension in the water "
      "column in the plant. The tension pulls water, and all the materials that the water contains, "
      "up from the roots. VPD is the size of this deficit.</p><p>A larger difference pulls with "
      "more force. Calcium moves only with this flow of water. Thus, when the VPD is low for a long "
      "time, weak tissue and tipburn occur after some time in fast growth. Evaporation also removes "
      "heat. As a result, the temperature of a canopy in good condition that transpires is lower "
      "than the temperature of the air around the canopy" + _c("nelson2015-leaftemp") +
      "."),
    figure(_FIGS["stomata-three"], 7,
      "The pore and the gradient. For a flux of water vapor, two conditions are necessary: a "
      "difference of vapor pressure and an open pore. The plant controls the pore" +
      _c("grossiord2020-vpd") + "."),
    p("The effect of VPD on the plant does not increase at a constant rate. This fact is important. "
      "When VPD increases to a value more than the range without stress for the plant, the guard "
      "cells close the stomata more and more. This prevents damage to the water column in the "
      "plant.</p><p>Transpiration does not increase, and it can decrease. The intake of CO2 "
      "decreases, and photosynthesis decreases with it. These changes occur when the light "
      "intensity makes more gas exchange necessary" + _c("grossiord2020-vpd") +
      ". A very high VPD does not increase growth. It decreases photosynthesis."),
    ul([
      "<strong>Too low (less than 0.4 kPa):</strong> the pores are open, but there is no gradient. "
      "The growth becomes soft, with a large stretch. The supply of calcium decreases. Films of "
      "water stay on the tissue. Guttation occurs at night. A test shows that the effect on "
      "flowering is very large" + _c("corredor2025-rh") + ".",
      "<strong>In the band:</strong> the air removes water at a stable rate, the leaf is cool, the "
      "stomata are open, and the nutrients move. The other sections of this paper help you to keep "
      "this condition.",
      "<strong>Too high (more than 2.0 kPa):</strong> the stomata close, the leaf becomes hotter, "
      "and photosynthesis decreases. In the afternoon, the plant keeps the water in its leaves and "
      "does not increase in size" + _c("grossiord2020-vpd") + ".",
    ]),
    callout("key", "A stable VPD is a target",
      p("Tests in controlled environments show the same result each time. When the "
        "<em>variation</em> of the VPD is small, the stomata stay open. Photosynthesis is then "
        "higher than with a VPD that changes up and down around the best setpoint" + _c("inoue2021-vpd") +
        ". A room at a VPD of 1.1 for the full day is better than a room with an average VPD of "
        "1.2. The VPD in the second room changes in the range of 0.8 to 1.6.")),
  ]})

# ---------------------------------------------------------------- 09 day / night
SECTIONS.append({"id": "day-night", "kicker": "09 · The time of day", "title": "Climate targets for the day and for the night",
  "blocks": [
    p("During the day, VPD control is for growth. Keep the VPD in the stage band, and keep it "
      "stable. At night, VPD control is for <em>protection</em>. Most rooms have problems at night, "
      "because all the values in the formula change at the same time at lights-off. The heat load "
      "becomes zero, the air temperature decreases, and the saturation vapor pressure decreases "
      "with it. The RH increases quickly, although no water goes into the room."),
    figure(_FIGS["day-night-trace"], 8,
      "Two days that are the same, and two nights that are different. In the controlled room, the "
      "dehumidifier continues to operate at lights-off, and the VPD decreases in steps to a minimum "
      "value. In the room with no control, the conditions go into the range of condensation in two "
      "hours or less."),
    steps([
      ("A ramp at the start of the day", "The plant starts to operate before the transpiration starts. Let the VPD increase from the minimum at night to the day band in the first 1–2 hours of light. Do not start the dehumidifier and the heater at full power at one time. A slow change is better than a fast change" + _c("inoue2021-vpd") + "."),
      ("Keep the VPD in the band at the peak", "In the middle of the photoperiod, the transpiration and the drift of the sensors are at their peak. At this time, use the values of the canopy sensor and not the values of the controller on the wall."),
      ("Dehumidify before lights-off", "Start the dehumidification before the temperature decreases. It is easier to remove water from warm air. Thus the RH is less than the risk limit when the night starts. You do not have to decrease the RH after the night starts."),
      ("Keep a minimum VPD at night", "The usual method is as follows. Do not let the VPD at night decrease to much less than approximately 0.7–1.0 kPa. Do not let the canopy RH stay at more than 70%. Plants continue to transpire at night, usually at 5–15% of the rates in the day" + _c("caird2007-night") + ". Thus the quantity of water in the air continues to increase when the lights are off."),
    ]),
    callout("note", "Night temperature changes the length of the internodes",
      p("The difference between the day temperature and the night temperature (&lsquo;DIF&rsquo;) "
        "controls the stretch of the internodes in greenhouse crops. When the day temperature is "
        "higher than the night temperature, the plants stretch. When the night temperature is equal "
        "to or higher than the day temperature, the internodes are short" + _c("moe1995-dif") +
        ". Decrease the temperature at night by only 2&ndash;4&nbsp;°C. Then the morphology is easy "
        "to control, <em>and</em> the RH increases by a smaller quantity at night. If the night "
        "temperature is much lower than the day temperature, the internodes are short, but there is "
        "a problem of condensation.")),
  ]})

# ---------------------------------------------------------------- 10 dew point
SECTIONS.append({"id": "night-dew", "kicker": "10 · Condensation and mold risk", "title": "Dew point and the risk of condensation at night",
  "blocks": [
    p("RH shows the quantity of water in the air, compared with the maximum. <strong>Dew "
      "point</strong> shows the temperature at which this water becomes liquid water. At the dew "
      "point, the actual vapor pressure is equal to the saturation vapor pressure" + _c("fao56-1998") +
      ".</p><p>Liquid water collects on a surface that is at a temperature equal to or less than "
      "the dew point. Examples are an external wall, bare steel, port glass and the surface of a "
      "large cola that sends heat by radiation to a cold ceiling. Liquid water and spores together "
      "cause bud rot. The risk of botrytis increases quickly when the humidity at the canopy is "
      "more than approximately 70%" + _c("punja2025-budrot-epi") + "."),
    figure(_FIGS["dewpoint-night"], 9,
      "The room did not receive water. The temperature of the room decreased in the direction of "
      "the dew point of the air. The surfaces with the lowest temperatures became colder than the "
      "dew point first. Control of the RH at night is control of condensation."),
    p("The dew point changes only when the quantity of water in the air changes. When you "
      "dehumidify the air, the dew point decreases. When you irrigate or when the plants transpire, "
      "the dew point increases. When the room temperature decreases, the dew point does not change. "
      "The difference between the room temperature and the dew point decreases.</p><p>You can "
      "calculate the dew point from the vapor pressure: <strong>T<sub>d</sub> = 237.3 &times; "
      "ln(ea/0.6108) &divide; (17.27 &minus; ln(ea/0.6108))</strong>" + _c("fao56-1998") +
      ". You can also read the dew point from a table:"),
    table(["Night air at 24 °C (75 °F)", "50% RH", "55% RH", "60% RH", "65% RH", "70% RH"], [
      ["Dew point", "12.9 °C (55.2 °F)", "14.4 °C (57.9 °F)", "15.8 °C (60.4 °F)", "17.0 °C (62.6 °F)", "18.2 °C (64.8 °F)"],
      ["Surfaces with condensation", "Almost no surface in the room", "Cold external corners", "Walls with no insulation, steel", "Most surfaces that have no heat source", "All cool surfaces and the buds"],
    ], cls="compact",
      caption="Calculated with the FAO-56 relations" + _c("fao56-1998") + ". At 24 °C (75 °F) and 70% RH, a surface that is only 6 °C colder than the air stays wet for all the night."),
    figure(L.zones("Night RH at the canopy: the mold axis", 40, 90,
        [(40, 60, "var(--fig-green-l)", "satisfactory"),
         (60, 70, "var(--fig-dryl)", "monitor"),
         (70, 80, "var(--fig-amber-l)", "high risk"),
         (80, 90, "var(--fig-red-l)", "rot / condensation")],
        unit="% RH",
        note="Use the canopy value at night, not the room average in the day."), 10,
      "The limit that is more important than all the VPD targets in the last part of flowering. The "
      "botrytis pressure increases quickly at more than approximately 70% canopy RH" +
      _c("punja2025-budrot-epi") + "."),
    callout("danger", "The canopy is wetter than the sensor shows",
      p("A canopy with a high density has transpiration and air that does not move. As a result, "
        "the humidity in the canopy is 15&ndash;25% higher than the reading of the room sensor" +
        _c("zhang2020-canopy-rh") + ". A room with a record of 60% at night can have a microclimate "
        "of 80% or more in the colas. The rot starts in this microclimate. Defoliation and airflow "
        "through the canopy are tools to control the humidity. Read the <a "
        "href='airflow-design.html'>airflow paper</a> and the <a href='mould-risk.html'>mold "
        "paper</a>.")),
  ]})

# ---------------------------------------------------------------- 11 measurement
SECTIONS.append({"id": "measurement", "kicker": "11 · The instruments", "title": "Position of the sensors at the height of the canopy",
  "blocks": [
    p("The climate control has all the errors of its sensors. Three conditions give a correct VPD "
      "value. The sensor is in the correct <em>position</em>. Radiation does not heat the sensor. "
      "You have a measurement of the leaf temperature."),
    figure(_FIGS["sensor-placement"], 11,
      "One sensor with a shield and a fan, in the row at the height of the canopy, gives better "
      "results. Five sensors in positions that are easy to use give worse results. Each incorrect "
      "position causes a different typical error. The controller then follows the error."),
    ul([
      "<strong>Position.</strong> Put the sensor at the height of the canopy, in the area of the "
      "crop. Keep the sensor away from doors, the air from the dehumidifier and the outlets of "
      "ducts. The average of the room is not correct for the crop. The crop is in a microclimate "
      "that the sensor on the wall cannot measure" + _c("zhang2020-canopy-rh") +
      ".",
      "<strong>Shield and air flow.</strong> A sensor in the light of a fixture absorbs radiation, "
      "and it shows a temperature that is higher than the air temperature. When the air does not "
      "move and the light is strong, the radiation error is some degrees and not a fraction of a "
      "degree" + _c("tarara2007-shield") + ". A sensor with no shield below a fixture shows a high "
      "temperature. As a result, the controller calculates a VPD that is too high and humidifies a "
      "room that has sufficient humidity. Put a shield on the sensor and, if possible, a small fan "
      "to move air across it (an &lsquo;aspirated&rsquo; sensor).",
      "<strong>Leaf temperature.</strong> An IR thermometer is the best tool to add for the "
      "measurement of VPD, for a cost of less than NZ$50. Point it at a leaf that receives light, "
      "at the canopy top, and not at benches, pots or your hand. Keep it near the leaf and at a "
      "right angle to the leaf. Measure some leaves and calculate the average. IR canopy sensors "
      "for this task measure all the time and send the leaf VPD to the controller.",
      "<strong>More than one sensor.</strong> Two sensors that agree give better data than one "
      "sensor with a value that you cannot compare. Record the values at night as carefully as the "
      "values in the day. Section 10 is about the conditions at 3 a.m.",
    ]),
    callout("tip", "A low-cost method for calibration",
      p("Put all your RH sensors together in a sealed container for one night. Put a saturated "
        "mixture of table salt and water in the container. The air above the mixture becomes stable "
        "at approximately 75% RH. Compare the value of each sensor with this RH. If the difference "
        "is more than a small number of points, correct the offset or remove the sensor. Do this "
        "each quarter, because RH sensors that use capacitance have drift.")),
  ]})

# ---------------------------------------------------------------- 12 the kit
SECTIONS.append({"id": "kit", "kicker": "12 · The equipment", "title": "Equipment to humidify and to dehumidify",
  "blocks": [
    p("Almost all the irrigation water goes into the air of the room, because the plants transpire "
      "the water as vapor. This latent load, and not the lights, is the load that the "
      "dehumidification must remove" + _c("hpac-latent") + ". Select the size of the "
      "dehumidification equipment for this load. A room that receives 100 L/day of irrigation water "
      "must have equipment that can remove most of the 100 L/day as vapor. The dehumidification has "
      "the most work in the hours immediately after lights-off. A dehumidification system that is "
      "too small is the most frequent cause of high humidity at night when growers do not know the "
      "cause."),
    ul([
      "<strong>Dehumidifier:</strong> the primary equipment. Select a size that is sufficient for "
      "the volume of irrigation water each day, with headroom. Connect the condensate to a drain "
      "through a pipe. Point the air from the dehumidifier away from the sensors" + _c("hpac-latent") +
      ".",
      "<strong>Air conditioning:</strong> an air conditioner also dehumidifies the air, but "
      "dehumidification is not its primary task. The condensate on its coil is water that leaves "
      "the room. This function is satisfactory until the air conditioner starts and stops in short "
      "cycles at night. Then it does not dehumidify when the RH increases quickly.",
      "<strong>Humidifier:</strong> a tool for clones and for the first part of vegetative growth "
      "in most sealed rooms. Use clean water. Keep the plume away from the leaves and the sensors. "
      "A large canopy humidifies the room air.",
      "<strong>Heater:</strong> a heater increases the saturation vapor pressure. As a result, the "
      "RH decreases and the VPD increases, with no movement of water. A heater is frequently the "
      "method with the lowest cost for a small room that has a high humidity for a long time.",
      "<strong>Circulation fans:</strong> these fans do not change the VPD of the room. But the "
      "fans remove the saturated boundary layer of air that does not move around the leaves, and "
      "the microclimate of the canopy" + _c("zhang2020-canopy-rh") + ". The boundary layer and the "
      "microclimate cause the difference between the VPD that you set and the VPD that the leaf has.",
    ]),
    p("A frequent error is an overlap of the humidity setpoints of the humidifier and the "
      "dehumidifier. As a result, the humidifier causes the dehumidifier to operate, and the "
      "dehumidifier causes the humidifier to operate. The two items of equipment use power, and the "
      "humidity of the room does not change. Give the humidifier and the dehumidifier a dead band. "
      "A dead band is a minimum difference of 5% RH between the setpoint of the humidifier and the "
      "setpoint of the dehumidifier. Change only one control each time:"),
    figure(L.flow("Change VPD in this sequence",
        [("Leaf temperature", "IR thermometer, top canopy, some leaves"),
         ("Calculate leaf VPD", "es(leaf) minus ea"),
         ("Set RH first", "dehumidifier or humidifier: fast, low cost"),
         ("Then temperature", "only if RH is in range"),
         ("Measure at 15 min", "one change each time")],
        note="Humidity changes are fast and you can change them back. Temperature changes cause problems for the HVAC, lights and plant biology."), 12,
      "The sequence of adjustment that prevents oscillation: humidity is the control for small "
      "changes, and temperature is the control for large changes."),
  ]})

# ---------------------------------------------------------------- 13 mistakes
SECTIONS.append({"id": "mistakes", "kicker": "13 · Frequent errors", "title": "Frequent errors in VPD control",
  "blocks": [
    grid([
      card("Use of temperature to control VPD",
        p("The chart shows that a higher temperature gives a higher VPD. Thus a grower sets the "
          "room to 30&nbsp;°C (86&nbsp;°F) to get a VPD of 1.4 kPa. Then the temperature is more "
          "than the best temperature for the photosynthesis of the plants" + _c("chandra2008-photo") +
          ". The biology of the root zone and of the disease changes, and the plants use too much "
          "water.</p><p>The VPD is in the range, but the other conditions are not correct. Set the "
          "temperature for the stage. Then control the VPD with the humidity."),
        tag="A room that is too hot"),
      card("No correction for the leaf offset",
        p("The air VPD in an LED room is 1.3, and this value looks correct. But the cool canopy has "
          "a VPD of 0.9" + _c("nelson2015-leaftemp") + ". After some weeks, the growth is soft and "
          "the mold pressure increases. Then the grower thinks that the &lsquo;perfect "
          "climate&rsquo; is the cause. Measure the temperature of a leaf. Correct the chart.")),
      card("No control at night",
        p("The curves for the day are correct, but there is no procedure for the night. At "
          "lights-off, the saturation vapor pressure decreases and the RH stays at 80% or more. Dew "
          "collects on the coldest surfaces, and the conditions are correct for botrytis" +
          _c("punja2025-budrot-epi") + ". The dehumidifier must operate with the largest capacity "
          "at night.")),
      card("One sensor with no shield",
        p("One sensor with no shield above the canopy measures the effect of the light, the air "
          "from the door and the air from the dehumidifier. It does not measure the crop" +
          _c("tarara2007-shield") + ". The controller then makes the error automatic. Put a shield "
          "on the sensor, and move air across the sensor with a small fan. Put the sensor at the "
          "height of the canopy. Compare it with a second sensor.")),
      card("A band used as one accurate value",
        p("A grower can use the heater, the humidifier and the dehumidifier frequently to hold a "
          "VPD of 1.25 accurately. This method gives plants in a worse condition than a stable VPD "
          "of 1.1. Frequent changes of the VPD have a bad effect on the stomata" + _c("inoue2021-vpd") +
          ". Use the middle of the band as the target. Make a stable VPD the primary target. Make "
          "one adjustment for each photoperiod, and not one adjustment for each hour.")),
      card("Use of humidity to correct wilt",
        p("The plants show wilt, and as a result the grower increases the RH. But wilt is "
          "frequently a problem of water supply (a dry root zone or a root zone with too much "
          "water), and not a problem of demand. Then the root zone continues to have the problem, "
          "<em>and</em> the canopy is wet. Examine the moisture of the substrate before you change "
          "the air. A hot leaf on the IR thermometer shows that the plant does not transpire" +
          _c("nelson2015-leaftemp") + ".")),
    ], cols=2),
  ]})

# ---------------------------------------------------------------- 14 troubleshooting
SECTIONS.append({"id": "troubleshooting", "kicker": "14 · Reference", "title": "Troubleshooting",
  "blocks": [
    table(["Symptom", "Possible cause in the climate", "Correction"], [
      ["The edges of the leaves bend up and become dry, and the growth stops in the middle of the day",
       "VPD is too high (the temperature is high for short periods, and the RH decreases)",
       "Increase the RH first. Measure the leaf temperature to make sure that the VPD is correct. If the leaves are hot, examine the irrigation before you change the climate" + _c("grossiord2020-vpd")],
      ["Soft growth with a large stretch, &lsquo;praying&rsquo; leaves that are flat, and tipburn in fast vegetative growth",
       "A low VPD for a long time, with weak transpiration and a weak flux of calcium",
       "Decrease the RH or increase the temperature by one degree. Make sure that the canopy sensor does not measure a wet microclimate" + _c("corredor2025-rh")],
      ["The RH increases quickly to 85% or more in one hour or less after lights-off",
       "A latent load and no dehumidification at night",
       "Start the dehumidifier before lights-off. Compare the capacity that the dehumidifier has in the room with the liters of irrigation water each day" + _c("hpac-latent")],
      ["Condensation on walls, port glass or the skin of the tent at night",
       "Surface temperatures that are less than the dew point",
       "Decrease the RH at night (dehumidifier) or decrease the drop of temperature at night. Put insulation on the cold surface" + _c("fao56-1998")],
      ["Botrytis in the largest colas although the room sensor shows 60%",
       "The microclimate of the canopy is 15–25% wetter than the value of the room sensor",
       "Make sure that air flows through the canopy. Defoliate the canopy. Use the RH at the canopy at night, and not the RH at the wall" + _c("zhang2020-canopy-rh") + _c("punja2025-budrot-epi")],
      ["Two sensors show values with a difference of 5% RH or more, or a difference of 1 °C or more",
       "An error of position or of radiation, or drift",
       "Put a shield on the sensor and move air across it. Move the sensor away from strong light and from strong air flow. Do the salt test each quarter" + _c("tarara2007-shield")],
      ["The VPD is correct on paper, but the plants show wilt",
       "A problem on the supply side (roots, substrate, EC), or the leaf temperature that you use is incorrect",
       "Measure the canopy with an IR thermometer. Weigh the substrate or measure it with a probe. Calculate the VPD again with the leaf temperature" + _c("nelson2015-leaftemp")],
    ], cls="compact"),
  ]})

# ---------------------------------------------------------------- 15 mental model
SECTIONS.append({"id": "mental-model", "kicker": "15 · The facts", "title": "Important facts about VPD control",
  "blocks": [
    callout("key", "Five important facts about climate control in a grow room",
      ol([
        "<strong>The difference has an effect on the plant. The percentage does not.</strong> VPD = "
        "saturation vapor pressure minus actual vapor pressure, in kPa. The same RH at two "
        "different temperatures gives two different climates" + _c("fao56-1998") +
        ".",
        "<strong>The saturation vapor pressure increases by a constant percentage.</strong> The "
        "value increases by approximately 6% for each degree, and the value becomes two times "
        "larger when the temperature increases by approximately 11&nbsp;°C. A decision about the "
        "temperature is always also a decision about the humidity. Thus lights-off is the most "
        "dangerous hour of the day.",
        "<strong>The leaf temperature gives the correct value.</strong> LED canopies are colder and "
        "wetter than the chart shows. HPS canopies are hotter and drier. A leaf with stress is much "
        "hotter. The temperature of this leaf shows a problem and is not an offset" +
        _c("nelson2015-leaftemp") + ".",
        "<strong>VPD in the day causes growth, and RH at night keeps the crop in good "
        "condition.</strong> Keep the stage band stable through the photoperiod" + _c("inoue2021-vpd") +
        ". Keep the canopy RH less than approximately 70%. Keep all surfaces at a temperature "
        "higher than the dew point at night" + _c("punja2025-budrot-epi") + ".",
        "<strong>Measure where the plant is.</strong> Put the sensor at the height of the canopy, "
        "with a shield and a flow of air. Compare it with a second sensor. Use a correct leaf "
        "temperature. If you do not do this, the controller makes an incorrect value automatic" +
        _c("tarara2007-shield") + _c("zhang2020-canopy-rh") + ".",
      ])),
    p("VPD is the demand side of the supply and demand of water. The <a "
      "href='grow-room-systems.html'>systems paper</a> gives information about the equipment for "
      "VPD. The <a href='airflow-design.html'>airflow</a> paper shows how to move the air with the "
      "setpoint conditions into the canopy. The <a href='mould-risk.html'>mold risk</a> paper is "
      "about the problem that this control prevents."),
  ]})
