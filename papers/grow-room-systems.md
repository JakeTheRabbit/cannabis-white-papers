---
slug: "grow-room-systems"
title: "The cannabis grow room: a systems guide"
eyebrow: "Beginner · Grow-room systems"
summary: "A grow room is one connected system, not a list of gadgets. Light, heat, humidity, air and water all pull on each other. Learn to see the whole machine, so a fix in one place doesn't break another."
track: "Environment & climate"
read_time: "~18 min read"
diagrams: "4 diagrams"
related: ["coco-crop-steering", "airflow-design", "mould-risk"]
url: "https://jaketherabbit.github.io/cannabis-white-papers/grow-room-systems.html"
md_url: "https://jaketherabbit.github.io/cannabis-white-papers/papers/grow-room-systems.md"
version: "1.2"
updated: "2026-07-18"
license: "CC BY-NC 4.0"
license_url: "https://creativecommons.org/licenses/by-nc/4.0/"
attribution: "The Cannabis White Papers"
refs: [{"id": "rm2021-light", "n": 1, "cite": "Rodriguez-Morrison V, Llewellyn D, Zheng Y (2021). Cannabis yield, potency, and leaf photosynthesis respond differently to increasing light levels in an indoor environment. Front. Plant Sci. 12:646020.", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8144505/", "peer": true}, {"id": "faust2018-dli", "n": 2, "cite": "Faust JE, Logan J (2018). Daily light integral: a research review and high-resolution maps of the United States. HortScience 53(9):1250-1257.", "url": "https://doi.org/10.21273/HORTSCI13144-18", "peer": true}, {"id": "collado2025-light", "n": 3, "cite": "Collado CE, Hernandez R (2025). Vegetative and reproductive stage lighting interactions on flower yield, water-use efficiency, terpenes and cannabinoids of Cannabis sativa. Scientific Reports 15:s41598-025-27437-4.", "url": "https://www.nature.com/articles/s41598-025-27437-4", "peer": true}, {"id": "chandra2008-photo", "n": 4, "cite": "Chandra S, Lata H, Khan IA, ElSohly MA (2008). Photosynthetic response of Cannabis sativa L. to variations in photosynthetic photon flux densities, temperature and CO2 conditions. Physiol. Mol. Biol. Plants 14(4):299-306.", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3550641/", "peer": true}, {"id": "inoue2021-vpd", "n": 5, "cite": "Inoue T, et al. (2021). Minimizing VPD fluctuations maintains higher stomatal conductance and photosynthesis, improving plant growth in lettuce. Front. Plant Sci. 12:646144.", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8049605/", "peer": true}, {"id": "schymanski2016-wind", "n": 6, "cite": "Schymanski SJ, Or D (2016). Wind increases leaf water use efficiency. Plant, Cell & Environment 39(7):1448-1459.", "url": "https://onlinelibrary.wiley.com/doi/10.1111/pce.12700", "peer": true}, {"id": "malik2025-media", "n": 7, "cite": "Malik M, Tlustoš P (2025). Soilless growing media for cannabis cultivation. Agriculture 15(18):1955.", "url": "https://www.mdpi.com/2077-0472/15/18/1955", "peer": true}, {"id": "caplan2019-drought", "n": 8, "cite": "Caplan D, Dixon M, Zheng Y (2019). Increasing inflorescence dry weight and cannabinoid content in medical cannabis using controlled drought stress. HortScience 54(5):964-969.", "url": "https://doi.org/10.21273/HORTSCI13510-18", "peer": true}, {"id": "punja2019-pathogens", "n": 9, "cite": "Punja ZK, Collyer D, Scott C, Lung S, Holmes J, Sutton D (2019). Pathogens and molds affecting production and quality of Cannabis sativa L. Front. Plant Sci. 10:1120.", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC6811654/", "peer": true}, {"id": "punja-budrot-cjb", "n": 10, "cite": "Mahmoud M, BenRejeb I, Punja ZK, Buirs L, Jabaji S (2023). Understanding bud rot development, caused by Botrytis cinerea, on cannabis grown under greenhouse conditions. Botany / Can. J. Bot. 101(8).", "url": "https://doi.org/10.1139/cjb-2022-0139", "peer": true}]
---

# The cannabis grow room: a systems guide

_Beginner · Grow-room systems · ~18 min read_

> A grow room is one connected system, not a list of gadgets. Light, heat, humidity, air and water all pull on each other. Learn to see the whole machine, so a fix in one place doesn't break another.

## The room is one machine

Those four things are one problem, not four. Beginners buy a light, a fan, a humidifier and a nutrient bottle and treat each as a separate job. Turn the light up and the room gets hotter, the plants drink more, the air gets more humid, and your dehumidifier works harder. Everything is connected.

This guide shows you those connections, so you set things up in the right order instead of chasing one problem into the next. No prior knowledge needed.

## The words you need

**PPFD** — How bright the usable light hitting the canopy is, measured in µmol/m²/s. Think ‘brightness right now.’

**DLI (daily light integral)** — Brightness × hours the light is on = the total light the plant gets in a day (mol/m²/day). This is the number that really drives growth[^faust2018-dli].

**Transpiration** — The plant pulling water up from the roots and breathing it out through tiny leaf pores (stomata). It is how the plant stays cool and moves nutrients.

**VPD (vapour pressure deficit)** — How ‘thirsty’ the air is. A single number from temperature and humidity that sets how fast the plant transpires.

**CO2** — Carbon dioxide, the raw material plants turn into sugar with light. More CO2 can raise growth if light is high enough.

**Stomata** — Microscopic adjustable pores on leaves. They open to take in CO2 and let water out, and they close when the plant is stressed.

**Substrate** — What the roots grow in (coco, rockwool, peat). It changes how water, air and salt behave at the root[^malik2025-media].

## How it's all coupled

One chain runs your room. Push the first link and every link after it moves:

> **Diagram.** The coupling chain. This is why ‘just add more light’ fails if your climate and airflow can't carry the extra water the plants now transpire.[^collado2025-light]

> **KEY — The one rule that prevents most mistakes**
>
> Raise one input, then ask ‘what must move with it?’ More light → more transpiration → more humidity → more dehumidification and more water and feed. Inputs travel in convoys, not alone.

## Light: set the demand first

Light is the upstream lever: it sets how much of everything else the plant wants. In cannabis, flower yield climbs roughly **linearly with light** all the way up to very high intensities (~1800 µmol/m²/s in one study, about a 4.5× yield increase)[^rm2021-light]. Bright works, as long as you can pay the bills downstream.

> **Diagram.** Whole-plant yield rises far past where a single leaf stops responding. The canopy keeps using light the top leaves can't[^rm2021-light]. Returns do taper, and very high light needs matching CO2, climate and water.

> **WARN — Leaf vs canopy: the classic trap**
>
> Measure one leaf and photosynthesis ‘maxes out’ at modest light, which tempts you to stop there. The whole canopy keeps converting more light into more flower well beyond that point[^rm2021-light]. Don't set room light by leaf-level numbers.

## Climate: temperature, humidity & VPD

Temperature and humidity are not two separate dials. Together they make **VPD**, which controls how fast the plant transpires. There is a workable middle band. Too low and everything slows. Too high and the plant shuts its stomata to save water, stalling CO2 uptake and growth[^inoue2021-vpd].

> **Diagram.** Most growth happens around 0.8–1.2 kPa. Drier air pushes generative, but past ~1.5 kPa the plant closes up and stops working[^inoue2021-vpd].

**CO2** is the other climate lever. Adding CO2 raises photosynthesis and water-use efficiency, and, counter-intuitively, it makes the plant transpire _less_ and partly close its stomata, not open them[^chandra2008-photo]. It only pays off when light is already high.

## Airflow ties it together

Moving air does two quiet but vital jobs. It strips away the thin film of still, humid air that clings to each leaf, and it cools the leaf by convection. Faster air thins that film, improving CO2 uptake and water-use efficiency while lowering water loss[^schymanski2016-wind]. It also keeps every plant in the room living in the same climate.

> **NOTE — Airflow has its own paper**
>
> Boundary layers, fan placement, velocity targets and dead zones are covered in depth in [Airflow design for indoor cultivation](airflow-design.html). Here, just know that without air movement your light, climate and CO2 settings don't reach the leaf evenly.

## Root zone: feeding the demand

Everything upstream creates _thirst_, and the root zone has to satisfy it. The brighter and drier the room, the more the plant transpires, and the more water and nutrient it needs at the roots. Your substrate and irrigation are the supply side of the same system[^malik2025-media].

The root zone is also a steering lever: a controlled root-zone dryback nudges the plant generative and can raise potency[^caplan2019-drought]. The full mechanics are in the [coco & crop steering](coco-crop-steering.html) paper. The point here is that irrigation must _match_ the demand the rest of the room is creating, not run on a fixed timer.

## Set it up in the right order

Inputs are coupled, so the order you set them in matters. Work top-down:

1. **1. Pick your light target** — Decide the DLI/PPFD you can actually support. This sets the demand for everything else.
2. **2. Match the climate** — Set temperature and humidity to a sane VPD for that light level, with CO2 if light is high.
3. **3. Provide the airflow** — Enough movement to mix the room and reach every leaf. See the airflow paper.
4. **4. Feed to match** — Size irrigation and feed EC to the transpiration the above creates, then steer with dryback.
5. **5. Then steer & refine** — Only now nudge generative or vegetative, one lever at a time, watching the whole chain.

## The system can breed disease

The same warm, humid, densely-planted room that grows big plants also grows mould. Bud rot (_Botrytis_) takes off above ~70% humidity at moderate temperatures, and a thick canopy traps humid, still air inside itself where your room sensor never sees it[^punja-budrot-cjb].

> **DANGER — Your room sensor is lying to you (a little)**
>
> A sensor in open air can read a comfortable 60% while the inside of a fat cola sits at 85% and rotting. Airflow through the canopy and sensible plant spacing, not just the room average, are what keep disease out[^punja2019-pathogens]. Full detail in the [mould risk](mould-risk.html) paper.

## Troubleshooting the system

| Symptom | Where the system broke | What to do |
| --- | --- | --- |
| Room humidity won't come down | Light/transpiration outran your dehumidification | Add dehumid capacity or trim light, and improve air exchange |
| Leaf edges curling/taco at high light | VPD too high, so the plant closed its stomata | Lower VPD (cooler/more humid), add CO2, verify airflow |
| Big light, disappointing yield | Climate/CO2/water didn't scale with the light | Match CO2, VPD and feed to the light level |
| Hot canopy, slow growth | Airflow too weak, so the leaf can't shed heat | Increase canopy-level air movement |
| Bud rot in week 6+ | Dense canopy + trapped humidity | Defoliate/space plants, airflow through the canopy, lower RH |

## Realistic expectations

> **KEY — The mindset that separates good growers from frustrated ones**
>
> - Think in **convoys**: change one input and pre-empt what must move with it.
> - **Match, don't max.** The best room is not the one with the biggest light. It is the one whose parts are balanced for the light it has[^collado2025-light].
> - Substrate and strain change the right answer. Treat published numbers as starting points, not law.

Read the [crop steering](coco-crop-steering.html), [airflow](airflow-design.html) and [mould](mould-risk.html) papers next. They are the subsystems of this one machine.

## References

[^rm2021-light]: Rodriguez-Morrison V, Llewellyn D, Zheng Y (2021). Cannabis yield, potency, and leaf photosynthesis respond differently to increasing light levels in an indoor environment. Front. Plant Sci. 12:646020. https://pmc.ncbi.nlm.nih.gov/articles/PMC8144505/ (peer-reviewed)
[^faust2018-dli]: Faust JE, Logan J (2018). Daily light integral: a research review and high-resolution maps of the United States. HortScience 53(9):1250-1257. https://doi.org/10.21273/HORTSCI13144-18 (peer-reviewed)
[^collado2025-light]: Collado CE, Hernandez R (2025). Vegetative and reproductive stage lighting interactions on flower yield, water-use efficiency, terpenes and cannabinoids of Cannabis sativa. Scientific Reports 15:s41598-025-27437-4. https://www.nature.com/articles/s41598-025-27437-4 (peer-reviewed)
[^chandra2008-photo]: Chandra S, Lata H, Khan IA, ElSohly MA (2008). Photosynthetic response of Cannabis sativa L. to variations in photosynthetic photon flux densities, temperature and CO2 conditions. Physiol. Mol. Biol. Plants 14(4):299-306. https://pmc.ncbi.nlm.nih.gov/articles/PMC3550641/ (peer-reviewed)
[^inoue2021-vpd]: Inoue T, et al. (2021). Minimizing VPD fluctuations maintains higher stomatal conductance and photosynthesis, improving plant growth in lettuce. Front. Plant Sci. 12:646144. https://pmc.ncbi.nlm.nih.gov/articles/PMC8049605/ (peer-reviewed)
[^schymanski2016-wind]: Schymanski SJ, Or D (2016). Wind increases leaf water use efficiency. Plant, Cell & Environment 39(7):1448-1459. https://onlinelibrary.wiley.com/doi/10.1111/pce.12700 (peer-reviewed)
[^malik2025-media]: Malik M, Tlustoš P (2025). Soilless growing media for cannabis cultivation. Agriculture 15(18):1955. https://www.mdpi.com/2077-0472/15/18/1955 (peer-reviewed)
[^caplan2019-drought]: Caplan D, Dixon M, Zheng Y (2019). Increasing inflorescence dry weight and cannabinoid content in medical cannabis using controlled drought stress. HortScience 54(5):964-969. https://doi.org/10.21273/HORTSCI13510-18 (peer-reviewed)
[^punja2019-pathogens]: Punja ZK, Collyer D, Scott C, Lung S, Holmes J, Sutton D (2019). Pathogens and molds affecting production and quality of Cannabis sativa L. Front. Plant Sci. 10:1120. https://pmc.ncbi.nlm.nih.gov/articles/PMC6811654/ (peer-reviewed)
[^punja-budrot-cjb]: Mahmoud M, BenRejeb I, Punja ZK, Buirs L, Jabaji S (2023). Understanding bud rot development, caused by Botrytis cinerea, on cannabis grown under greenhouse conditions. Botany / Can. J. Bot. 101(8). https://doi.org/10.1139/cjb-2022-0139 (peer-reviewed)
