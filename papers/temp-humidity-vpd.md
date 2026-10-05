---
slug: "temp-humidity-vpd"
title: "Temperature, humidity and VPD: stage targets, measurement and condensation control"
eyebrow: "Environment · Climate"
summary: "Vapor pressure deficit (VPD) is the value that shows how much water the air removes from the leaves. This paper gives the definition of VPD and shows how to calculate it. It shows that the leaf temperature gives the correct deficit. It gives the targets for each stage and the sources of the targets. It also gives the control of the dew point at night, which prevents mold. It shows how to put the sensors in the correct position and how to read them accurately."
track: "Environment and climate"
read_time: "~19 min to read"
diagrams: "12 diagrams"
related: ["grow-room-systems", "mould-risk", "airflow-design"]
url: "https://www.growlabs.nz/wiki/temp-humidity-vpd.html"
md_url: "https://www.growlabs.nz/wiki/papers/temp-humidity-vpd.md"
version: "1.2"
updated: "2026-07-18"
license: "CC BY-NC 4.0"
license_url: "https://creativecommons.org/licenses/by-nc/4.0/"
attribution: "The Cannabis White Papers"
refs: [{"id": "fao56-1998", "n": 1, "cite": "Allen RG, Pereira LS, Raes D, Smith M (1998). Crop evapotranspiration - guidelines for computing crop water requirements. FAO Irrigation and Drainage Paper 56, Chapter 3: meteorological data (Tetens saturation vapour pressure equation, vapour pressure deficit and dew point relations). Rome: FAO.", "url": "https://www.fao.org/4/x0490e/x0490e07.htm", "peer": false}, {"id": "grossiord2020-vpd", "n": 2, "cite": "Grossiord C, Buckley TN, Cernusak LA, et al. (2020). Plant responses to rising vapor pressure deficit. New Phytologist 226(6):1550-1566.", "url": "https://doi.org/10.1111/nph.16485", "peer": true}, {"id": "nelson2015-leaftemp", "n": 3, "cite": "Nelson JA, Bugbee B (2015). Analysis of environmental effects on leaf temperature under sunlight, high pressure sodium and light emitting diodes. PLoS ONE 10(10):e0138930 (well-watered leaves typically within ~2 °C of air; LED canopies ~1.3 °C cooler than HPS at equal photon flux; water-stressed leaves modelled 6-12 °C above air).", "url": "https://doi.org/10.1371/journal.pone.0138930", "peer": true}, {"id": "corredor2025-rh", "n": 4, "cite": "Corredor-Perilla IC, et al. (2025). Elevated relative humidity significantly decreases cannabinoid concentrations while delaying flowering development in Cannabis sativa L. Front. Plant Sci. 16:1678142 (flowering at 0.05-0.25 kPa VPD vs 0.92-1.29 kPa: -71% flower biomass, three-week flowering delay, multi-fold cannabinoid reductions).", "url": "https://doi.org/10.3389/fpls.2025.1678142", "peer": true}, {"id": "jin2019-cannabis-env", "n": 5, "cite": "Jin D, Jin S, Chen J (2019). Cannabis indoor growing conditions, management practices, and post-harvest treatment: a review. Am. J. Plant Sci. 10(6):925-946 (recommends ~75% RH for juvenile plants and 55-60% RH through vegetative growth and flowering at 25 °C).", "url": "https://doi.org/10.4236/ajps.2019.106067", "peer": true}, {"id": "pulse-vpd-guide", "n": 6, "cite": "Pulse Labs. The ultimate vapor pressure deficit (VPD) guide: leaf-basis VPD formula, leaf-offset calculator (leaves typically 1-3 °C below air) and stage bands (~0.8 kPa clones/seedlings, ~1.0 kPa veg, 1.2-1.5 kPa flower). Industry convention reference, not peer-reviewed.", "url": "https://pulsegrow.com/blogs/learn/vpd", "peer": false}, {"id": "chandra2008-photo", "n": 7, "cite": "Chandra S, Lata H, Khan IA, ElSohly MA (2008). Photosynthetic response of Cannabis sativa L. to variations in photosynthetic photon flux densities, temperature and CO2 conditions. Physiol. Mol. Biol. Plants 14(4):299-306.", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3550641/", "peer": true}, {"id": "inoue2021-vpd", "n": 8, "cite": "Inoue T, et al. (2021). Minimizing VPD fluctuations maintains higher stomatal conductance and photosynthesis, improving plant growth in lettuce. Front. Plant Sci. 12:646144.", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8049605/", "peer": true}, {"id": "caird2007-night", "n": 9, "cite": "Caird MA, Richards JH, Donovan LA (2007). Nighttime stomatal conductance and transpiration in C3 and C4 plants. Plant Physiol. 143(1):4-10 (night transpiration commonly 5-15% of daytime rates, at times up to ~30%).", "url": "https://doi.org/10.1104/pp.106.092940", "peer": true}, {"id": "moe1995-dif", "n": 10, "cite": "Myster J, Moe R (1995). Effect of diurnal temperature alternations on plant morphology in some greenhouse crops, a mini review. Scientia Horticulturae 62(4):205-215.", "url": "https://doi.org/10.1016/0304-4238(95)00783-P", "peer": true}, {"id": "punja2025-budrot-epi", "n": 11, "cite": "Punja ZK, et al. (2025). The epidemiology and management of Botrytis cinerea causing bud rot on greenhouse-cultivated cannabis. Can. J. Plant Pathol.", "url": "https://doi.org/10.1080/07060661.2025.2478250", "peer": true}, {"id": "zhang2020-canopy-rh", "n": 12, "cite": "Zhang D, et al. (2020). Substantial differences occur between canopy and ambient climate: quantification of interactions in a greenhouse-canopy system. PLoS ONE 15(5):e0233210 (in-canopy RH ~15-25% higher than surrounding air).", "url": "https://doi.org/10.1371/journal.pone.0233210", "peer": true}, {"id": "tarara2007-shield", "n": 13, "cite": "Tarara JM, Hoheisel G-A (2007). Low-cost shielding to minimize radiation errors of temperature sensors in the field. HortScience 42(6):1372-1379 (radiation loading drives whole-degree errors in unaspirated air-temperature measurement; shielding and aspiration recover accuracy).", "url": "https://doi.org/10.21273/HORTSCI.42.6.1372", "peer": true}, {"id": "hpac-latent", "n": 14, "cite": "HPAC Engineering. Latent loads matter: HVAC for cannabis grow facilities (transpiration returns most irrigation water to room air as vapour, the dominant dehumidification load; filters do not remove it).", "url": "https://www.hpac.com/industrial/article/21270796/latent-loads-matter-hvac-for-cannabis-grow-facilities", "peer": false}]
---

# Temperature, humidity and VPD: stage targets, measurement and condensation control

_Environment · Climate · ~19 min to read_

> Vapor pressure deficit (VPD) is the value that shows how much water the air removes from the leaves. This paper gives the definition of VPD and shows how to calculate it. It shows that the leaf temperature gives the correct deficit. It gives the targets for each stage and the sources of the targets. It also gives the control of the dew point at night, which prevents mold. It shows how to put the sensors in the correct position and how to read them accurately.

## Purpose and scope

Two rooms show a relative humidity (RH) of 55%. One room is at 20 °C (68 °F), and the plants are in good condition. The other room is at 28 °C (82 °F). In this room, the growth of the same cultivar stops, the leaf edges bend up, and the plants use a large quantity of water.The number on the controller is the same, but the two rooms are very different. RH is a percentage of a value that changes with the temperature. A percentage has no effect on the plant. The **force** with which the air pulls water out of the leaves has an effect on the plant.

This force has a name: **vapor pressure deficit** (VPD). VPD is the value that the temperature and the humidity make together. Air can contain water vapor up to a maximum, and this maximum changes with the temperature of the air. VPD is the difference between this maximum and the vapor pressure of the water that is in the air[^fao56-1998].Each leaf transpires into this difference. When the difference is small, the force is weak. When the difference is large, the force is strong, until the plant closes its pores to keep the water in the plant[^grossiord2020-vpd].

This paper gives only the necessary information about the physics of moist air. It gives the definition of VPD and a formula that you can use in a calculator. It shows that the _leaf_ temperature is the correct value for the formula. It also shows how the type of light fixture changes the leaf temperature. It gives the VPD bands for each stage. A band is the range of VPD values for one stage.It also gives the sources of the bands, the targets for the day and the night, and the control of the dew point. This control prevents bud rot. It shows how to measure all these values and prevent incorrect sensor readings. It is not necessary to know physics before you read this paper. The paper gives the definition of each term.

## Definitions

**Water vapor**: Water as a gas, mixed in the air. You cannot see water vapor. You can see drops of liquid water in the air.

**Vapor pressure**: The part of the air pressure that the water vapor causes. The unit is the kilopascal (kPa). It is the accurate value for the quantity of water in the air.

**Saturation vapor pressure (es)**: The maximum vapor pressure that air can contain at a given temperature. At this value, water starts to condense. The value increases at a high rate when the temperature increases[^fao56-1998].

**Actual vapor pressure (ea)**: The vapor pressure of the water that is in the air at this time. This value is always equal to or less than the saturation vapor pressure.

**Relative humidity (RH)**: The actual vapor pressure as a percentage of the saturation vapor pressure: ea ÷ es × 100. RH without the temperature does not give sufficient information. The temperature is also necessary.

**Vapor pressure deficit (VPD)**: The difference: es − ea, in kPa. VPD shows how much water the air can remove from the leaves. This value has an effect on the plant.

**Leaf VPD**: The same difference, but you calculate it with the _leaf_ temperature and not with the air temperature. The air in a leaf is at saturation at the temperature of the leaf. Thus leaf VPD is the value that causes transpiration[^grossiord2020-vpd].

**Dew point**: The temperature at which water in the air starts to condense when you decrease the temperature of the air. When a surface is at a temperature less than the dew point, water condenses on the surface. The dew point shows the risk of mold.

**Transpiration**: Transpiration is the evaporation of water from the leaf, through the pores of the leaf. The water that leaves the leaf pulls water, and the dissolved nutrients in the water, up from the roots.

**Stomata**: The pores of the leaf, usually on the bottom side of the leaf. Water vapor leaves the leaf, and CO2 goes into the leaf, through these pores. The plant can change the size of each pore. Guard cells open and close the pores in minutes. One pore is a stoma.

## Basic information about VPD

The quantity of vapor that air can contain changes with the temperature. When the temperature of the air increases, the air can contain _more_ vapor. The quantity of water that is in the air does not change because the temperature of the room increases. Only the difference between the saturation vapor pressure (es) and the actual vapor pressure (ea) changes. This difference is VPD.

> **Diagram.** Two rooms with the same RH of 60%. The percentage is the same, but the difference that the plant transpires into is 60% larger in the warm room. Thus a value of RH does not give the full information about a climate.

VPD has an effect on plants, but RH does not. Water moves out of a leaf by diffusion. The difference in vapor pressure between the saturated air in the leaf and the air of the room around the leaf causes the diffusion. The ratio of the two vapor pressures does not cause the diffusion[^grossiord2020-vpd]. The air of two rooms with the same RH can remove water from the crop at very different rates. The air of two rooms with the same VPD removes water at the same rate, for all values of RH.

> **Diagram.** The saturation curve from the FAO-56 Tetens formula[^fao56-1998]. The saturation vapor pressure increases approximately 6% for each degree. It becomes two times larger between 14 °C (57 °F) and 25 °C (77 °F). Thus a change of temperature causes a larger change of VPD than most changes of humidity.

The curve is the most important physics for the control of the climate. It gives the cause of three problems with humidity in a grow room. First, the RH in the room increases quickly to 90% at lights-off. The cause is that the saturation vapor pressure decreases and the quantity of water stays the same. Second, a heater makes the air drier, but the heater does not remove a gram of water. Third, in summer the plants use much more water at the same RH.

> **Diagram.** The same maximum, in grams. A room at 30 °C (86 °F) can contain almost two times the quantity of water of a room at 20 °C (68 °F). Thus a decision about the temperature is also a decision about the humidity[^fao56-1998].

> **KEY: The short model**
>
> RH is a percentage of a maximum that changes. VPD _is_ the difference. The difference has an effect on the plant.

## How to calculate VPD

All the values in this paper use one formula for the saturation vapor pressure. The formula is the result of measurements, and it is accurate to a fraction of one percent at the temperatures of a grow room. It is the Tetens formula of FAO Irrigation and Drainage Paper 56[^fao56-1998]. T is the temperature in °C, and the result is in kPa:

> **NOTE: The saturation vapor pressure**
>
> **es(T) = 0.6108 × e(17.27 × T) / (T + 237.3)** kPa
> Then:  **ea = es(Tair) × RH / 100**  and  **VPDair = es(Tair) − ea = es(Tair) × (1 − RH/100)**

This example shows how to calculate the air VPD in steps. The air VPD is the VPD that you calculate with the air temperature. The numbers are the same as in all of this paper:

- **Air temperature:** 25.0 °C (77.0 °F)
- **Relative humidity:** 60%
- **Saturation vapor pressure es(25):** 0.6108 × e^(431.75 / 262.3) = 3.17 kPa
- **Actual vapor pressure ea:** 3.17 × 0.60 = 1.90 kPa
- **Air VPD:** 3.17 − 1.90 = 1.27 kPa

You can use a table and not the formula. The table gives the values of es for the temperatures of most rooms. Multiply the value of es by (1 − RH/100). The result is the VPD:

| Air temperature | es (kPa) | VPD at 50% RH | VPD at 60% RH | VPD at 70% RH |
| --- | --- | --- | --- | --- |
| 18 °C (64 °F) | 2.06 | 1.03 | 0.83 | 0.62 |
| 20 °C (68 °F) | 2.34 | 1.17 | 0.94 | 0.70 |
| 22 °C (72 °F) | 2.64 | 1.32 | 1.06 | 0.79 |
| 24 °C (75 °F) | 2.98 | 1.49 | 1.19 | 0.90 |
| 26 °C (79 °F) | 3.36 | 1.68 | 1.34 | 1.01 |
| 28 °C (82 °F) | 3.78 | 1.89 | 1.51 | 1.13 |
| 30 °C (86 °F) | 4.25 | 2.12 | 1.70 | 1.27 |

*Saturation vapor pressure and air VPD, calculated with the FAO-56 formula[^fao56-1998]. The values have two decimals.*

> **TIP: Units**
>
> 1 kPa = 10 mbar = 10 hPa. Some charts from the US use other units, for example psi or grains of moisture. Do not use these units. The cultivation literature and all good controllers use kPa. The values that you will see in a grow room are in the range of approximately 0.2 (air with a very high humidity) to 2.5 (air with a very low humidity).

## Leaf temperature and leaf VPD

This correction is important if you want to control VPD and not only record it. The air _in_ a leaf is at saturation at the temperature of the _leaf_. Thus the gradient that causes transpiration is not es(air) − ea. It is **es(leaf) − ea**[^grossiord2020-vpd]. When the leaf and the air are at the same temperature, the two values are the same. But the two temperatures are not always the same.

The temperature of a canopy in good condition that transpires is near the air temperature. The difference is usually a maximum of approximately 2 °C for all light sources. But the leaf temperature can be _higher or lower_ than the air temperature, and the radiation on the canopy is the primary cause[^nelson2015-leaftemp]. The difference between the leaf temperature and the air temperature is the leaf offset.An HPS lamp gives a large quantity of radiation to the canopy, and the temperature of the leaves becomes higher than the air temperature. An LED fixture removes most of its heat at the heat sink. A leaf that transpires removes heat by evaporation, and the temperature of this leaf is frequently _lower_ than the air temperature. At equal light intensity, a model gives a difference of approximately 1.3 °C between the two types of light[^nelson2015-leaftemp]. In the tools that growers use, the usual value for the temperature of an LED canopy is 1–3 °C less than the air temperature[^pulse-vpd-guide].

> **Diagram.** The room shows the same values, but the plant has different conditions. A difference of a small number of degrees between the leaf and the air changes the calculated VPD by the width of one stage band[^nelson2015-leaftemp].

Do the example again with the measured temperatures of the leaf. The result changes. Air at 25 °C (77 °F) and 60% RH gives 1.27 kPa. This VPD is usual for flowering.If the LED canopy is at 23 °C (73 °F), the leaf VPD is es(23) − 1.90 = **0.91 kPa**. This VPD is for the vegetative stage, and the climate is a third wetter than the dashboard shows. If the leaf in an HPS room is at 26 °C (79 °F), the leaf VPD is **1.46 kPa**. This VPD is at the top of the band for flowering. The room is the same, but there are three different results.

> **WARN: The problem in a room with LED fixtures**
>
> Most rooms that change from HPS to LED fixtures keep the targets for temperature and humidity of the HPS lamps. The air VPD looks correct, but the _leaf_ VPD is one band lower. As a result, the crop is wetter. The growth is softer, the drybacks are slower, and the room is nearer to condensation at night.
> If the mold pressure increased after you changed the fixtures, it is possible that the leaf offset is the cause. Increase the air temperature by one or two degrees, or decrease the RH. Then compare the values with the _leaf_ VPD.

> **DANGER: A hot leaf shows a problem and not an offset**
>
> If your IR thermometer shows that a leaf is hot, examine the root zone before you change the climate. The offsets above are for a canopy that transpires and has sufficient water. A leaf with drought stress closes its stomata. As a result, evaporation does not decrease the temperature of the leaf. The temperature of this leaf can be 6–12 °C higher than the air temperature[^nelson2015-leaftemp]. The hot leaf shows that the plant does not transpire, and a correction of the chart does not help.

## Use of a VPD chart

The usual chart for growers shows the results of the formula. The temperature is on the side, the RH is at the top, and each cell shows the VPD. The colors show the stage bands of the next section:

> **Diagram.** Temperature × RH → kPa, for the air VPD. The chart shows the relation between temperature and RH. One degree of temperature changes the VPD by approximately the same quantity as two to three points of RH.

1. **Measure where the plants are**: Measure the air temperature and the RH at the height of the canopy, in the middle of the room. Do not measure at the controller on the wall. The position of the sensor is as important as the instrument (section 11).
2. **Measure the leaf temperature**: Use an IR thermometer or a canopy sensor on a leaf at the top of the canopy that receives light. If you cannot measure the leaf temperature, use these values. In an HPS room, the leaf temperature is approximately the same as the air temperature. In an LED room, the leaf temperature is 1–2 °C less than the air temperature[^nelson2015-leaftemp].
3. **Read the cell**: Find the row for your temperature and the column for your RH. The value in the cell, in kPa, shows how much water the air can remove from the crop.
4. **Correct the value for the leaf**: When the leaf is colder than the air, the correct VPD is lower than the value in the cell. When the leaf is hotter than the air, the correct VPD is higher. At 25 °C (77 °F) and 60%, a canopy that is 2 °C colder than the air changes 1.27 kPa to 0.91 kPa. Do not make an estimate of the correction. Use a calculator for the leaf offset or a controller that uses the leaf temperature[^pulse-vpd-guide].
5. **Move along one axis of the chart each time**: If the air is too dry, increase the RH (move left in the chart) before you increase the temperature (move up in the chart). Make one change. After fifteen minutes, read the values again.

> **TIP: Two different climates with the same VPD value**
>
> 27 °C (81 °F) with 65% RH and 21 °C (70 °F) with 45% RH give a VPD of approximately 1.3 kPa. But the two climates are not the same, because the temperature has effects on the plant that are different from the effects of VPD.
> The photosynthesis of cannabis has a maximum at approximately 25–30 °C (77–86 °F)[^chandra2008-photo]. The morphology and the stretch change with the difference between the day temperature and the night temperature[^moe1995-dif]. The disease pressure changes with the absolute humidity. First select the temperature that is necessary for your stage and your fixture. Then use the humidity to adjust the VPD at this temperature.

## VPD targets for each stage

The bands below are the usual method that growers use. Physics does not give these bands. The bands are the result of the methods of growers, which became almost the same in a period of ten years[^pulse-vpd-guide]. The bands are in the ranges that the literature on cannabis production recommends[^jin2019-cannabis-env].The only controlled test of the humidity for cannabis that we have shows the wet limit of the bands. In this test, the VPD for flowering was 0.05–0.25 kPa and not approximately 0.9–1.3 kPa. The flower biomass decreased by 71%, flowering started three weeks after the usual time, and the cannabinoid concentration decreased by a large quantity[^corredor2025-rh].Start in the middle of the band. Then use your cultivar, the light intensity and your mold limit to select the value in the band.

> **Diagram.** One axis for the full crop cycle. The bands become drier when the plant has more roots and more leaf area. The plant then has more capacity to move water and more tolerance to a high VPD[^pulse-vpd-guide][^jin2019-cannabis-env].

| Stage | Leaf VPD band | Because | Example of temperature and RH (air VPD) |
| --- | --- | --- | --- |
| Clones and new seedlings | 0.4–0.8 kPa | There are no roots or only a small number of roots. The shoot must not transpire more than the uptake of water. | 24 °C (75 °F) and 75–80% RH give approximately 0.6–0.7 kPa |
| First part of the vegetative stage | 0.8–1.1 kPa | The plant has roots. Increase the gas exchange, but do not cause stress to the plant. | 25 °C (77 °F) and 65–70% RH give approximately 1.0 kPa |
| Last part of the vegetative stage | 0.9–1.2 kPa | The canopy is full and the light intensity is high. Keep the flux of water high and stable. | 26 °C (79 °F) and 62–68% RH give approximately 1.1–1.3 kPa |
| First and middle part of flowering | 1.1–1.4 kPa | Make the flow of water and nutrients high during the peak of bulking. | 26 °C (79 °F) and 58–62% RH give approximately 1.3–1.4 kPa |
| Last part of flowering | 1.2–1.5 kPa | The buds have a high density. At this time, the mold limit is more important than the VPD target. | 24 °C (75 °F) and 50–55% RH give approximately 1.4–1.5 kPa |

*The usual method[^pulse-vpd-guide][^jin2019-cannabis-env][^corredor2025-rh]. The example values are for a leaf temperature that is approximately the same as the air temperature. In an LED room, make the air temperature higher or the RH lower to get the same leaf VPD.*

> **NOTE: Limits of the data for these bands**
>
> No dose–response curve of cannabis yield against VPD is available for all stages. The bands are estimates from the physiology of the plant, from the literature on production, and from the methods in many rooms.
> The data show three results clearly. A climate that is much too wet decreases the yield by a large quantity[^corredor2025-rh]. A climate that is much too dry closes the stomata and decreases photosynthesis[^grossiord2020-vpd]. A stable VPD is more important than a VPD at the best value. Plants at a stable VPD in the middle of the range become larger. Plants at a VPD that increases and decreases around the best value are smaller[^inoue2021-vpd].

## The effect of VPD on transpiration

Transpiration moves water from the root zone to the air. Water evaporates from the walls of the cells in the leaf. The water vapor leaves the leaf through the stomata, by diffusion, into the drier air of the room. The water that leaves the leaf causes tension in the water column in the plant. The tension pulls water, and all the materials that the water contains, up from the roots. VPD is the size of this deficit.A larger difference pulls with more force. Calcium moves only with this flow of water. Thus, when the VPD is low for a long time, weak tissue and tipburn occur after some time in fast growth. Evaporation also removes heat. As a result, the temperature of a canopy in good condition that transpires is lower than the temperature of the air around the canopy[^nelson2015-leaftemp].

> **Diagram.** The pore and the gradient. For a flux of water vapor, two conditions are necessary: a difference of vapor pressure and an open pore. The plant controls the pore[^grossiord2020-vpd].

The effect of VPD on the plant does not increase at a constant rate. This fact is important. When VPD increases to a value more than the range without stress for the plant, the guard cells close the stomata more and more. This prevents damage to the water column in the plant.Transpiration does not increase, and it can decrease. The intake of CO2 decreases, and photosynthesis decreases with it. These changes occur when the light intensity makes more gas exchange necessary[^grossiord2020-vpd]. A very high VPD does not increase growth. It decreases photosynthesis.

- **Too low (less than 0.4 kPa):** the pores are open, but there is no gradient. The growth becomes soft, with a large stretch. The supply of calcium decreases. Films of water stay on the tissue. Guttation occurs at night. A test shows that the effect on flowering is very large[^corredor2025-rh].
- **In the band:** the air removes water at a stable rate, the leaf is cool, the stomata are open, and the nutrients move. The other sections of this paper help you to keep this condition.
- **Too high (more than 2.0 kPa):** the stomata close, the leaf becomes hotter, and photosynthesis decreases. In the afternoon, the plant keeps the water in its leaves and does not increase in size[^grossiord2020-vpd].

> **KEY: A stable VPD is a target**
>
> Tests in controlled environments show the same result each time. When the _variation_ of the VPD is small, the stomata stay open. Photosynthesis is then higher than with a VPD that changes up and down around the best setpoint[^inoue2021-vpd]. A room at a VPD of 1.1 for the full day is better than a room with an average VPD of 1.2. The VPD in the second room changes in the range of 0.8 to 1.6.

## Climate targets for the day and for the night

During the day, VPD control is for growth. Keep the VPD in the stage band, and keep it stable. At night, VPD control is for _protection_. Most rooms have problems at night, because all the values in the formula change at the same time at lights-off. The heat load becomes zero, the air temperature decreases, and the saturation vapor pressure decreases with it. The RH increases quickly, although no water goes into the room.

> **Diagram.** Two days that are the same, and two nights that are different. In the controlled room, the dehumidifier continues to operate at lights-off, and the VPD decreases in steps to a minimum value. In the room with no control, the conditions go into the range of condensation in two hours or less.

1. **A ramp at the start of the day**: The plant starts to operate before the transpiration starts. Let the VPD increase from the minimum at night to the day band in the first 1–2 hours of light. Do not start the dehumidifier and the heater at full power at one time. A slow change is better than a fast change[^inoue2021-vpd].
2. **Keep the VPD in the band at the peak**: In the middle of the photoperiod, the transpiration and the drift of the sensors are at their peak. At this time, use the values of the canopy sensor and not the values of the controller on the wall.
3. **Dehumidify before lights-off**: Start the dehumidification before the temperature decreases. It is easier to remove water from warm air. Thus the RH is less than the risk limit when the night starts. You do not have to decrease the RH after the night starts.
4. **Keep a minimum VPD at night**: The usual method is as follows. Do not let the VPD at night decrease to much less than approximately 0.7–1.0 kPa. Do not let the canopy RH stay at more than 70%. Plants continue to transpire at night, usually at 5–15% of the rates in the day[^caird2007-night]. Thus the quantity of water in the air continues to increase when the lights are off.

> **NOTE: Night temperature changes the length of the internodes**
>
> The difference between the day temperature and the night temperature (‘DIF’) controls the stretch of the internodes in greenhouse crops. When the day temperature is higher than the night temperature, the plants stretch. When the night temperature is equal to or higher than the day temperature, the internodes are short[^moe1995-dif]. Decrease the temperature at night by only 2–4 °C. Then the morphology is easy to control, _and_ the RH increases by a smaller quantity at night. If the night temperature is much lower than the day temperature, the internodes are short, but there is a problem of condensation.

## Dew point and the risk of condensation at night

RH shows the quantity of water in the air, compared with the maximum. **Dew point** shows the temperature at which this water becomes liquid water. At the dew point, the actual vapor pressure is equal to the saturation vapor pressure[^fao56-1998].Liquid water collects on a surface that is at a temperature equal to or less than the dew point. Examples are an external wall, bare steel, port glass and the surface of a large cola that sends heat by radiation to a cold ceiling. Liquid water and spores together cause bud rot. The risk of botrytis increases quickly when the humidity at the canopy is more than approximately 70%[^punja2025-budrot-epi].

> **Diagram.** The room did not receive water. The temperature of the room decreased in the direction of the dew point of the air. The surfaces with the lowest temperatures became colder than the dew point first. Control of the RH at night is control of condensation.

The dew point changes only when the quantity of water in the air changes. When you dehumidify the air, the dew point decreases. When you irrigate or when the plants transpire, the dew point increases. When the room temperature decreases, the dew point does not change. The difference between the room temperature and the dew point decreases.You can calculate the dew point from the vapor pressure: **Td = 237.3 × ln(ea/0.6108) ÷ (17.27 − ln(ea/0.6108))**[^fao56-1998]. You can also read the dew point from a table:

| Night air at 24 °C (75 °F) | 50% RH | 55% RH | 60% RH | 65% RH | 70% RH |
| --- | --- | --- | --- | --- | --- |
| Dew point | 12.9 °C (55.2 °F) | 14.4 °C (57.9 °F) | 15.8 °C (60.4 °F) | 17.0 °C (62.6 °F) | 18.2 °C (64.8 °F) |
| Surfaces with condensation | Almost no surface in the room | Cold external corners | Walls with no insulation, steel | Most surfaces that have no heat source | All cool surfaces and the buds |

*Calculated with the FAO-56 relations[^fao56-1998]. At 24 °C (75 °F) and 70% RH, a surface that is only 6 °C colder than the air stays wet for all the night.*

> **Diagram.** The limit that is more important than all the VPD targets in the last part of flowering. The botrytis pressure increases quickly at more than approximately 70% canopy RH[^punja2025-budrot-epi].

> **DANGER: The canopy is wetter than the sensor shows**
>
> A canopy with a high density has transpiration and air that does not move. As a result, the humidity in the canopy is 15–25% higher than the reading of the room sensor[^zhang2020-canopy-rh]. A room with a record of 60% at night can have a microclimate of 80% or more in the colas. The rot starts in this microclimate. Defoliation and airflow through the canopy are tools to control the humidity. Read the [airflow paper](airflow-design.html) and the [mold paper](mould-risk.html).

## Position of the sensors at the height of the canopy

The climate control has all the errors of its sensors. Three conditions give a correct VPD value. The sensor is in the correct _position_. Radiation does not heat the sensor. You have a measurement of the leaf temperature.

> **Diagram.** One sensor with a shield and a fan, in the row at the height of the canopy, gives better results. Five sensors in positions that are easy to use give worse results. Each incorrect position causes a different typical error. The controller then follows the error.

- **Position.** Put the sensor at the height of the canopy, in the area of the crop. Keep the sensor away from doors, the air from the dehumidifier and the outlets of ducts. The average of the room is not correct for the crop. The crop is in a microclimate that the sensor on the wall cannot measure[^zhang2020-canopy-rh].
- **Shield and air flow.** A sensor in the light of a fixture absorbs radiation, and it shows a temperature that is higher than the air temperature. When the air does not move and the light is strong, the radiation error is some degrees and not a fraction of a degree[^tarara2007-shield]. A sensor with no shield below a fixture shows a high temperature. As a result, the controller calculates a VPD that is too high and humidifies a room that has sufficient humidity. Put a shield on the sensor and, if possible, a small fan to move air across it (an ‘aspirated’ sensor).
- **Leaf temperature.** An IR thermometer is the best tool to add for the measurement of VPD, for a cost of less than NZ$50. Point it at a leaf that receives light, at the canopy top, and not at benches, pots or your hand. Keep it near the leaf and at a right angle to the leaf. Measure some leaves and calculate the average. IR canopy sensors for this task measure all the time and send the leaf VPD to the controller.
- **More than one sensor.** Two sensors that agree give better data than one sensor with a value that you cannot compare. Record the values at night as carefully as the values in the day. Section 10 is about the conditions at 3 a.m.

> **TIP: A low-cost method for calibration**
>
> Put all your RH sensors together in a sealed container for one night. Put a saturated mixture of table salt and water in the container. The air above the mixture becomes stable at approximately 75% RH. Compare the value of each sensor with this RH. If the difference is more than a small number of points, correct the offset or remove the sensor. Do this each quarter, because RH sensors that use capacitance have drift.

## Equipment to humidify and to dehumidify

Almost all the irrigation water goes into the air of the room, because the plants transpire the water as vapor. This latent load, and not the lights, is the load that the dehumidification must remove[^hpac-latent]. Select the size of the dehumidification equipment for this load. A room that receives 100 L/day of irrigation water must have equipment that can remove most of the 100 L/day as vapor. The dehumidification has the most work in the hours immediately after lights-off. A dehumidification system that is too small is the most frequent cause of high humidity at night when growers do not know the cause.

- **Dehumidifier:** the primary equipment. Select a size that is sufficient for the volume of irrigation water each day, with headroom. Connect the condensate to a drain through a pipe. Point the air from the dehumidifier away from the sensors[^hpac-latent].
- **Air conditioning:** an air conditioner also dehumidifies the air, but dehumidification is not its primary task. The condensate on its coil is water that leaves the room. This function is satisfactory until the air conditioner starts and stops in short cycles at night. Then it does not dehumidify when the RH increases quickly.
- **Humidifier:** a tool for clones and for the first part of vegetative growth in most sealed rooms. Use clean water. Keep the plume away from the leaves and the sensors. A large canopy humidifies the room air.
- **Heater:** a heater increases the saturation vapor pressure. As a result, the RH decreases and the VPD increases, with no movement of water. A heater is frequently the method with the lowest cost for a small room that has a high humidity for a long time.
- **Circulation fans:** these fans do not change the VPD of the room. But the fans remove the saturated boundary layer of air that does not move around the leaves, and the microclimate of the canopy[^zhang2020-canopy-rh]. The boundary layer and the microclimate cause the difference between the VPD that you set and the VPD that the leaf has.

A frequent error is an overlap of the humidity setpoints of the humidifier and the dehumidifier. As a result, the humidifier causes the dehumidifier to operate, and the dehumidifier causes the humidifier to operate. The two items of equipment use power, and the humidity of the room does not change. Give the humidifier and the dehumidifier a dead band. A dead band is a minimum difference of 5% RH between the setpoint of the humidifier and the setpoint of the dehumidifier. Change only one control each time:

> **Diagram.** The sequence of adjustment that prevents oscillation: humidity is the control for small changes, and temperature is the control for large changes.

## Frequent errors in VPD control

**Use of temperature to control VPD**

The chart shows that a higher temperature gives a higher VPD. Thus a grower sets the room to 30 °C (86 °F) to get a VPD of 1.4 kPa. Then the temperature is more than the best temperature for the photosynthesis of the plants[^chandra2008-photo]. The biology of the root zone and of the disease changes, and the plants use too much water.
The VPD is in the range, but the other conditions are not correct. Set the temperature for the stage. Then control the VPD with the humidity.

**No correction for the leaf offset**

The air VPD in an LED room is 1.3, and this value looks correct. But the cool canopy has a VPD of 0.9[^nelson2015-leaftemp]. After some weeks, the growth is soft and the mold pressure increases. Then the grower thinks that the ‘perfect climate’ is the cause. Measure the temperature of a leaf. Correct the chart.

**No control at night**

The curves for the day are correct, but there is no procedure for the night. At lights-off, the saturation vapor pressure decreases and the RH stays at 80% or more. Dew collects on the coldest surfaces, and the conditions are correct for botrytis[^punja2025-budrot-epi]. The dehumidifier must operate with the largest capacity at night.

**One sensor with no shield**

One sensor with no shield above the canopy measures the effect of the light, the air from the door and the air from the dehumidifier. It does not measure the crop[^tarara2007-shield]. The controller then makes the error automatic. Put a shield on the sensor, and move air across the sensor with a small fan. Put the sensor at the height of the canopy. Compare it with a second sensor.

**A band used as one accurate value**

A grower can use the heater, the humidifier and the dehumidifier frequently to hold a VPD of 1.25 accurately. This method gives plants in a worse condition than a stable VPD of 1.1. Frequent changes of the VPD have a bad effect on the stomata[^inoue2021-vpd]. Use the middle of the band as the target. Make a stable VPD the primary target. Make one adjustment for each photoperiod, and not one adjustment for each hour.

**Use of humidity to correct wilt**

The plants show wilt, and as a result the grower increases the RH. But wilt is frequently a problem of water supply (a dry root zone or a root zone with too much water), and not a problem of demand. Then the root zone continues to have the problem, _and_ the canopy is wet. Examine the moisture of the substrate before you change the air. A hot leaf on the IR thermometer shows that the plant does not transpire[^nelson2015-leaftemp].

## Troubleshooting

| Symptom | Possible cause in the climate | Correction |
| --- | --- | --- |
| The edges of the leaves bend up and become dry, and the growth stops in the middle of the day | VPD is too high (the temperature is high for short periods, and the RH decreases) | Increase the RH first. Measure the leaf temperature to make sure that the VPD is correct. If the leaves are hot, examine the irrigation before you change the climate[^grossiord2020-vpd] |
| Soft growth with a large stretch, ‘praying’ leaves that are flat, and tipburn in fast vegetative growth | A low VPD for a long time, with weak transpiration and a weak flux of calcium | Decrease the RH or increase the temperature by one degree. Make sure that the canopy sensor does not measure a wet microclimate[^corredor2025-rh] |
| The RH increases quickly to 85% or more in one hour or less after lights-off | A latent load and no dehumidification at night | Start the dehumidifier before lights-off. Compare the capacity that the dehumidifier has in the room with the liters of irrigation water each day[^hpac-latent] |
| Condensation on walls, port glass or the skin of the tent at night | Surface temperatures that are less than the dew point | Decrease the RH at night (dehumidifier) or decrease the drop of temperature at night. Put insulation on the cold surface[^fao56-1998] |
| Botrytis in the largest colas although the room sensor shows 60% | The microclimate of the canopy is 15–25% wetter than the value of the room sensor | Make sure that air flows through the canopy. Defoliate the canopy. Use the RH at the canopy at night, and not the RH at the wall[^zhang2020-canopy-rh][^punja2025-budrot-epi] |
| Two sensors show values with a difference of 5% RH or more, or a difference of 1 °C or more | An error of position or of radiation, or drift | Put a shield on the sensor and move air across it. Move the sensor away from strong light and from strong air flow. Do the salt test each quarter[^tarara2007-shield] |
| The VPD is correct on paper, but the plants show wilt | A problem on the supply side (roots, substrate, EC), or the leaf temperature that you use is incorrect | Measure the canopy with an IR thermometer. Weigh the substrate or measure it with a probe. Calculate the VPD again with the leaf temperature[^nelson2015-leaftemp] |

## Important facts about VPD control

> **KEY: Five important facts about climate control in a grow room**
>
> 1. **The difference has an effect on the plant. The percentage does not.** VPD = saturation vapor pressure minus actual vapor pressure, in kPa. The same RH at two different temperatures gives two different climates[^fao56-1998].
> 2. **The saturation vapor pressure increases by a constant percentage.** The value increases by approximately 6% for each degree, and the value becomes two times larger when the temperature increases by approximately 11 °C. A decision about the temperature is always also a decision about the humidity. Thus lights-off is the most dangerous hour of the day.
> 3. **The leaf temperature gives the correct value.** LED canopies are colder and wetter than the chart shows. HPS canopies are hotter and drier. A leaf with stress is much hotter. The temperature of this leaf shows a problem and is not an offset[^nelson2015-leaftemp].
> 4. **VPD in the day causes growth, and RH at night keeps the crop in good condition.** Keep the stage band stable through the photoperiod[^inoue2021-vpd]. Keep the canopy RH less than approximately 70%. Keep all surfaces at a temperature higher than the dew point at night[^punja2025-budrot-epi].
> 5. **Measure where the plant is.** Put the sensor at the height of the canopy, with a shield and a flow of air. Compare it with a second sensor. Use a correct leaf temperature. If you do not do this, the controller makes an incorrect value automatic[^tarara2007-shield][^zhang2020-canopy-rh].

VPD is the demand side of the supply and demand of water. The [systems paper](grow-room-systems.html) gives information about the equipment for VPD. The [airflow](airflow-design.html) paper shows how to move the air with the setpoint conditions into the canopy. The [mold risk](mould-risk.html) paper is about the problem that this control prevents.

## References

[^fao56-1998]: Allen RG, Pereira LS, Raes D, Smith M (1998). Crop evapotranspiration - guidelines for computing crop water requirements. FAO Irrigation and Drainage Paper 56, Chapter 3: meteorological data (Tetens saturation vapour pressure equation, vapour pressure deficit and dew point relations). Rome: FAO. https://www.fao.org/4/x0490e/x0490e07.htm (source from a manufacturer or industry)
[^grossiord2020-vpd]: Grossiord C, Buckley TN, Cernusak LA, et al. (2020). Plant responses to rising vapor pressure deficit. New Phytologist 226(6):1550-1566. https://doi.org/10.1111/nph.16485 (source with peer review)
[^nelson2015-leaftemp]: Nelson JA, Bugbee B (2015). Analysis of environmental effects on leaf temperature under sunlight, high pressure sodium and light emitting diodes. PLoS ONE 10(10):e0138930 (well-watered leaves typically within ~2 °C of air; LED canopies ~1.3 °C cooler than HPS at equal photon flux; water-stressed leaves modelled 6-12 °C above air). https://doi.org/10.1371/journal.pone.0138930 (source with peer review)
[^corredor2025-rh]: Corredor-Perilla IC, et al. (2025). Elevated relative humidity significantly decreases cannabinoid concentrations while delaying flowering development in Cannabis sativa L. Front. Plant Sci. 16:1678142 (flowering at 0.05-0.25 kPa VPD vs 0.92-1.29 kPa: -71% flower biomass, three-week flowering delay, multi-fold cannabinoid reductions). https://doi.org/10.3389/fpls.2025.1678142 (source with peer review)
[^jin2019-cannabis-env]: Jin D, Jin S, Chen J (2019). Cannabis indoor growing conditions, management practices, and post-harvest treatment: a review. Am. J. Plant Sci. 10(6):925-946 (recommends ~75% RH for juvenile plants and 55-60% RH through vegetative growth and flowering at 25 °C). https://doi.org/10.4236/ajps.2019.106067 (source with peer review)
[^pulse-vpd-guide]: Pulse Labs. The ultimate vapor pressure deficit (VPD) guide: leaf-basis VPD formula, leaf-offset calculator (leaves typically 1-3 °C below air) and stage bands (~0.8 kPa clones/seedlings, ~1.0 kPa veg, 1.2-1.5 kPa flower). Industry convention reference, not peer-reviewed. https://pulsegrow.com/blogs/learn/vpd (source from a manufacturer or industry)
[^chandra2008-photo]: Chandra S, Lata H, Khan IA, ElSohly MA (2008). Photosynthetic response of Cannabis sativa L. to variations in photosynthetic photon flux densities, temperature and CO2 conditions. Physiol. Mol. Biol. Plants 14(4):299-306. https://pmc.ncbi.nlm.nih.gov/articles/PMC3550641/ (source with peer review)
[^inoue2021-vpd]: Inoue T, et al. (2021). Minimizing VPD fluctuations maintains higher stomatal conductance and photosynthesis, improving plant growth in lettuce. Front. Plant Sci. 12:646144. https://pmc.ncbi.nlm.nih.gov/articles/PMC8049605/ (source with peer review)
[^caird2007-night]: Caird MA, Richards JH, Donovan LA (2007). Nighttime stomatal conductance and transpiration in C3 and C4 plants. Plant Physiol. 143(1):4-10 (night transpiration commonly 5-15% of daytime rates, at times up to ~30%). https://doi.org/10.1104/pp.106.092940 (source with peer review)
[^moe1995-dif]: Myster J, Moe R (1995). Effect of diurnal temperature alternations on plant morphology in some greenhouse crops, a mini review. Scientia Horticulturae 62(4):205-215. https://doi.org/10.1016/0304-4238(95)00783-P (source with peer review)
[^punja2025-budrot-epi]: Punja ZK, et al. (2025). The epidemiology and management of Botrytis cinerea causing bud rot on greenhouse-cultivated cannabis. Can. J. Plant Pathol. https://doi.org/10.1080/07060661.2025.2478250 (source with peer review)
[^zhang2020-canopy-rh]: Zhang D, et al. (2020). Substantial differences occur between canopy and ambient climate: quantification of interactions in a greenhouse-canopy system. PLoS ONE 15(5):e0233210 (in-canopy RH ~15-25% higher than surrounding air). https://doi.org/10.1371/journal.pone.0233210 (source with peer review)
[^tarara2007-shield]: Tarara JM, Hoheisel G-A (2007). Low-cost shielding to minimize radiation errors of temperature sensors in the field. HortScience 42(6):1372-1379 (radiation loading drives whole-degree errors in unaspirated air-temperature measurement; shielding and aspiration recover accuracy). https://doi.org/10.21273/HORTSCI.42.6.1372 (source with peer review)
[^hpac-latent]: HPAC Engineering. Latent loads matter: HVAC for cannabis grow facilities (transpiration returns most irrigation water to room air as vapour, the dominant dehumidification load; filters do not remove it). https://www.hpac.com/industrial/article/21270796/latent-loads-matter-hvac-for-cannabis-grow-facilities (source from a manufacturer or industry)
