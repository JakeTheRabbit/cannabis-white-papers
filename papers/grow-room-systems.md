---
slug: "grow-room-systems"
title: "Cannabis grow room systems"
eyebrow: "Basic · Grow-room systems"
summary: "A grow room is one connected system, and not a list of devices. Light, heat, humidity, air, and water have an effect on each other. This paper shows these connections. Then you can install and adjust the systems in the correct sequence and prevent problems before one problem causes the next."
track: "Environment and climate"
read_time: "~18 min to read"
diagrams: "4 diagrams"
related: ["coco-crop-steering", "airflow-design", "mould-risk"]
url: "https://www.growlabs.nz/wiki/grow-room-systems.html"
md_url: "https://www.growlabs.nz/wiki/papers/grow-room-systems.md"
version: "1.2"
updated: "2026-07-18"
license: "CC BY-NC 4.0"
license_url: "https://creativecommons.org/licenses/by-nc/4.0/"
attribution: "The Cannabis White Papers"
refs: [{"id": "rm2021-light", "n": 1, "cite": "Rodriguez-Morrison V, Llewellyn D, Zheng Y (2021). Cannabis yield, potency, and leaf photosynthesis respond differently to increasing light levels in an indoor environment. Front. Plant Sci. 12:646020.", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8144505/", "peer": true}, {"id": "faust2018-dli", "n": 2, "cite": "Faust JE, Logan J (2018). Daily light integral: a research review and high-resolution maps of the United States. HortScience 53(9):1250-1257.", "url": "https://doi.org/10.21273/HORTSCI13144-18", "peer": true}, {"id": "collado2025-light", "n": 3, "cite": "Collado CE, Hernandez R (2025). Vegetative and reproductive stage lighting interactions on flower yield, water-use efficiency, terpenes and cannabinoids of Cannabis sativa. Scientific Reports 15:s41598-025-27437-4.", "url": "https://www.nature.com/articles/s41598-025-27437-4", "peer": true}, {"id": "chandra2008-photo", "n": 4, "cite": "Chandra S, Lata H, Khan IA, ElSohly MA (2008). Photosynthetic response of Cannabis sativa L. to variations in photosynthetic photon flux densities, temperature and CO2 conditions. Physiol. Mol. Biol. Plants 14(4):299-306.", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3550641/", "peer": true}, {"id": "inoue2021-vpd", "n": 5, "cite": "Inoue T, et al. (2021). Minimizing VPD fluctuations maintains higher stomatal conductance and photosynthesis, improving plant growth in lettuce. Front. Plant Sci. 12:646144.", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8049605/", "peer": true}, {"id": "schymanski2016-wind", "n": 6, "cite": "Schymanski SJ, Or D (2016). Wind increases leaf water use efficiency. Plant, Cell & Environment 39(7):1448-1459.", "url": "https://onlinelibrary.wiley.com/doi/10.1111/pce.12700", "peer": true}, {"id": "malik2025-media", "n": 7, "cite": "Malik M, Tlustoš P (2025). Soilless growing media for cannabis cultivation. Agriculture 15(18):1955.", "url": "https://www.mdpi.com/2077-0472/15/18/1955", "peer": true}, {"id": "caplan2019-drought", "n": 8, "cite": "Caplan D, Dixon M, Zheng Y (2019). Increasing inflorescence dry weight and cannabinoid content in medical cannabis using controlled drought stress. HortScience 54(5):964-969.", "url": "https://doi.org/10.21273/HORTSCI13510-18", "peer": true}, {"id": "punja2019-pathogens", "n": 9, "cite": "Punja ZK, Collyer D, Scott C, Lung S, Holmes J, Sutton D (2019). Pathogens and molds affecting production and quality of Cannabis sativa L. Front. Plant Sci. 10:1120.", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC6811654/", "peer": true}, {"id": "punja-budrot-cjb", "n": 10, "cite": "Mahmoud M, BenRejeb I, Punja ZK, Buirs L, Jabaji S (2023). Understanding bud rot development, caused by Botrytis cinerea, on cannabis grown under greenhouse conditions. Botany / Can. J. Bot. 101(8).", "url": "https://doi.org/10.1139/cjb-2022-0139", "peer": true}]
---

# Cannabis grow room systems

_Basic · Grow-room systems · ~18 min to read_

> A grow room is one connected system, and not a list of devices. Light, heat, humidity, air, and water have an effect on each other. This paper shows these connections. Then you can install and adjust the systems in the correct sequence and prevent problems before one problem causes the next.

## Purpose and scope

Light, heat, humidity, and water are one problem and not four different tasks. A new grower gets a light, a fan, a humidifier, and a nutrient bottle, and thinks that each is a different task. When you increase the light, the room becomes hotter and the plants use more water. Then the humidity of the air increases, and the dehumidifier must remove more water. Each part has a connection to the other parts.

This paper shows these connections. Thus you can install and adjust the systems in the correct sequence. Then one problem does not cause the next problem. It is not necessary to know about cultivation before you read this paper.

## Definitions

**PPFD**: The quantity of light that falls on the canopy at this time, and that the plant can use. The unit is µmol/m²/s.

**DLI (daily light integral)**: The total quantity of light that the plant gets in one day (mol/m²/day). DLI = PPFD × the hours that the light is on. This value has the primary effect on growth.[^faust2018-dli]

**Transpiration**: The plant moves water up from the roots and releases it as vapor through small pores in the leaves (stomata). The water that moves up also moves the nutrients that are in the water, from the roots to the leaves. The evaporation of the water decreases the temperature of the leaf. With transpiration, the plant keeps a stable temperature and gets its nutrients.

**VPD (vapor pressure deficit)**: VPD shows how strongly the air removes water from the plant. The temperature and the humidity together set VPD, and not only the humidity. Dry, warm air removes water strongly. Cool, humid air is almost full of water, and it removes water weakly. VPD is one number that gives the strength of this removal, and it shows the rate of transpiration of the plant.

**CO2**: Carbon dioxide. The plant uses it with light to make sugar. More CO2 can increase growth if the light is sufficiently high.

**Stomata**: Small pores on leaves that you can see only with a microscope. The plant can open and close them. They open to absorb CO2 and to release water. They close when the plant has stress.

**Substrate**: The material that contains the roots (coco, rockwool, peat). The substrate has an effect on the water, the air, and the salt at the root.[^malik2025-media]

## Connections between the systems of a grow room

One sequence of parts operates your room. When you change the first part, each part after it changes:

> **Diagram.** The sequence of a coupled system. Thus the step ‘add more light’ does not give a good result if your climate and airflow cannot remove the larger quantity of water from the plants.[^collado2025-light]

> **KEY: One procedure that prevents most errors**
>
> When you increase one input, find the other inputs that must change with it. More light → more transpiration → more humidity → more dehumidification and more water and feed. The inputs change in groups, and not only one at a time.

## Quantity of light

Light is the first lever: it sets the quantity of all the other inputs that the plant uses. In cannabis, the yield of flowers has an approximately **linear increase with the light**, up to very high intensities (approximately 1800 µmol/m²/s in one test, a yield increase of approximately 4.5×).[^rm2021-light] Bright light gives good results. But the other parts of the room must control the heat, the humidity, and the water use that the light causes.

> **Diagram.** The yield of the whole plant continues to increase at light intensities much higher than the saturation of one leaf. The canopy uses light that the top leaves cannot use.[^rm2021-light] The yield increases more slowly at very high intensities. At these intensities, the CO2, the climate, and the water must agree with the light.

> **WARN: Leaf and canopy: a frequent error**
>
> Do not set the room light with values from one leaf. When you measure one leaf, photosynthesis has its maximum at a moderate light intensity. Then you can stop to increase the light at this point. The whole canopy continues to use more light to make more flower at much higher intensities.[^rm2021-light]

## Climate: temperature, humidity and VPD

Temperature and humidity have one effect together: **VPD**. VPD has a large effect on the rate of transpiration of the plant. There is a middle range in which the conditions are satisfactory. If VPD is too low, the plant becomes slower. If VPD is too high, the plant closes its stomata to keep water. As a result, the CO2 uptake and the growth stop.[^inoue2021-vpd]

> **Diagram.** A middle range that you can use is approximately 0.8–1.2 kPa (the range is different for each cultivar, and in the last stage of flowering it is frequently approximately 1.2–1.5). Drier air can cause generative growth. But at more than approximately 1.5 kPa, the plant closes its stomata and its growth stops.[^inoue2021-vpd]

**CO2** is the other lever for the climate. When you add CO2, photosynthesis and water-use efficiency increase. But the plant also transpires _less_. It closes part of its stomata, and it does not open them.[^chandra2008-photo] Growth increases only when the light is high.

## Airflow in the connected system

Air that moves has two important tasks. It removes the thin film of air with high humidity that does not move and stays on each leaf. It also decreases the temperature of the leaf by convection.Faster air makes this film thinner. As a result, the CO2 uptake and the water-use efficiency increase (more carbon fixation for each unit of water). But the total water use frequently increases in bright rooms.[^schymanski2016-wind] Air that moves also keeps all the plants in the room in the same climate.

> **NOTE: More information on airflow**
>
> The paper [Airflow design for indoor cultivation](airflow-design.html) gives the full information on boundary layers, fan positions, velocity targets, and dead zones. In this paper, it is sufficient to know one fact. Without air movement, your light, climate, and CO2 settings do not have the same effect on each leaf.

## Root-zone supply

All the parts before the root zone cause the plant to use _much water_, and the root zone must supply this water. When the room has more light and drier air, the plant transpires more and uses more water and nutrients at the roots. Your substrate and your irrigation are the supply part of the same system.[^malik2025-media]

The root zone is also a lever for crop steering: a controlled dryback in the root zone causes generative growth and can increase potency.[^caplan2019-drought] The paper on [coco and crop steering](coco-crop-steering.html) gives the full information on the mechanisms. The irrigation must _agree with_ the water use that the other parts of the room cause. The irrigation must not operate with a timer that does not change.

## System setup sequence

The inputs have connections to each other. Thus the sequence in which you set them is important. Do the steps in this sequence:

1. **1. Select your light target**: Select the DLI and the PPFD that your room can supply. This sets the necessary quantity for all the other systems.
2. **2. Set the climate for the light**: Set the temperature and the humidity to a correct VPD for that light intensity. If the light is high, add CO2.
3. **3. Supply the airflow**: Use sufficient air movement to mix the air in the room and to move air to each leaf. Refer to the airflow paper.
4. **4. Apply the correct feed**: Set the irrigation and the feed EC for the transpiration that the previous steps cause. Then use dryback for crop steering.
5. **5. Crop steering and adjustment**: Only at this time, cause more generative growth or more vegetative growth. Change one lever at a time, and monitor all the parts of the sequence.

## Disease risk in connected systems

A room that is warm and humid, with a high density of plants, gives large plants, and it also gives mold. Bud rot (_Botrytis_) starts and increases quickly at a humidity of more than approximately 70% and at moderate temperatures. A thick canopy keeps humid air that does not move in its inner part, and your room sensor does not measure this air.[^punja-budrot-cjb]

> **DANGER: A room sensor can show an incorrect value**
>
> Do not use only the average value of the room. A sensor in open air can show a good value of 60%. At the same time, the inner part of a large cola can be at 85% humidity, and the cola rots. Airflow through the canopy and correct spacing between plants prevent the disease.[^punja2019-pathogens] The paper on [mold risk](mould-risk.html) gives the full information.

## Troubleshooting

| Symptom | Cause in the system | Procedure |
| --- | --- | --- |
| The room humidity does not decrease | The light and the transpiration cause more water than your dehumidifier can remove | Add dehumidification capacity, or decrease the light. Also increase the air exchange. |
| Leaf curl at the edges, at high light | The cause is frequently light, leaf heat, and VPD together, and not only VPD | First, examine the PPFD and the leaf temperature. Then examine the VPD (use a lower temperature and more humidity). Add CO2. Make sure that the airflow is correct. |
| A high light intensity and a low yield | The climate, the CO2, and the water did not increase with the light | Set the CO2, the VPD, and the feed for the light intensity |
| Hot canopy, slow growth | The airflow is too weak, and the leaf cannot release heat | Increase the air movement at the canopy |
| Bud rot in week 6 and the weeks after it | A canopy with a high density and humidity that stays in the canopy | Defoliate the plants and increase the space between them. Increase the airflow through the canopy. Decrease the RH. |

## Expected results and limitations

> **KEY: Three procedures that keep the system in balance**
>
> - Think in **groups**: when you change one input, find the other inputs that must change with it.
> - **Balance the inputs. Do not use the maximum.** A balanced room at moderate light gives a better result than a bright room with a climate that cannot agree with the light.[^collado2025-light]
> - The substrate and the cultivar change the correct value. Use the numbers from the references as start points only.

Next, read the papers on [crop steering](coco-crop-steering.html), [airflow](airflow-design.html), and [mold](mould-risk.html). They are parts of this system.

## References

[^rm2021-light]: Rodriguez-Morrison V, Llewellyn D, Zheng Y (2021). Cannabis yield, potency, and leaf photosynthesis respond differently to increasing light levels in an indoor environment. Front. Plant Sci. 12:646020. https://pmc.ncbi.nlm.nih.gov/articles/PMC8144505/ (source with peer review)
[^faust2018-dli]: Faust JE, Logan J (2018). Daily light integral: a research review and high-resolution maps of the United States. HortScience 53(9):1250-1257. https://doi.org/10.21273/HORTSCI13144-18 (source with peer review)
[^collado2025-light]: Collado CE, Hernandez R (2025). Vegetative and reproductive stage lighting interactions on flower yield, water-use efficiency, terpenes and cannabinoids of Cannabis sativa. Scientific Reports 15:s41598-025-27437-4. https://www.nature.com/articles/s41598-025-27437-4 (source with peer review)
[^chandra2008-photo]: Chandra S, Lata H, Khan IA, ElSohly MA (2008). Photosynthetic response of Cannabis sativa L. to variations in photosynthetic photon flux densities, temperature and CO2 conditions. Physiol. Mol. Biol. Plants 14(4):299-306. https://pmc.ncbi.nlm.nih.gov/articles/PMC3550641/ (source with peer review)
[^inoue2021-vpd]: Inoue T, et al. (2021). Minimizing VPD fluctuations maintains higher stomatal conductance and photosynthesis, improving plant growth in lettuce. Front. Plant Sci. 12:646144. https://pmc.ncbi.nlm.nih.gov/articles/PMC8049605/ (source with peer review)
[^schymanski2016-wind]: Schymanski SJ, Or D (2016). Wind increases leaf water use efficiency. Plant, Cell & Environment 39(7):1448-1459. https://onlinelibrary.wiley.com/doi/10.1111/pce.12700 (source with peer review)
[^malik2025-media]: Malik M, Tlustoš P (2025). Soilless growing media for cannabis cultivation. Agriculture 15(18):1955. https://www.mdpi.com/2077-0472/15/18/1955 (source with peer review)
[^caplan2019-drought]: Caplan D, Dixon M, Zheng Y (2019). Increasing inflorescence dry weight and cannabinoid content in medical cannabis using controlled drought stress. HortScience 54(5):964-969. https://doi.org/10.21273/HORTSCI13510-18 (source with peer review)
[^punja2019-pathogens]: Punja ZK, Collyer D, Scott C, Lung S, Holmes J, Sutton D (2019). Pathogens and molds affecting production and quality of Cannabis sativa L. Front. Plant Sci. 10:1120. https://pmc.ncbi.nlm.nih.gov/articles/PMC6811654/ (source with peer review)
[^punja-budrot-cjb]: Mahmoud M, BenRejeb I, Punja ZK, Buirs L, Jabaji S (2023). Understanding bud rot development, caused by Botrytis cinerea, on cannabis grown under greenhouse conditions. Botany / Can. J. Bot. 101(8). https://doi.org/10.1139/cjb-2022-0139 (source with peer review)
