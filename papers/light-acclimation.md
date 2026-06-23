---
slug: "light-acclimation"
title: "Light acclimation: raise PPFD in steps so plants don't bleach"
eyebrow: "Beginner · Light"
summary: "Light is a curve, not a switch. Raise PPFD in steps the plant can keep up with, and match CO2 to set how high you can go."
track: "Vegetative growth"
read_time: "~9 min read"
diagrams: "9 diagrams"
related: ["coco-crop-steering", "signal-and-noise", "plant-state-dashboard"]
url: "https://jaketherabbit.github.io/cannabis-white-papers/light-acclimation.html"
md_url: "https://jaketherabbit.github.io/cannabis-white-papers/papers/light-acclimation.md"
version: "1.0"
updated: "2026-06-24"
license: "CC BY-NC 4.0"
license_url: "https://creativecommons.org/licenses/by-nc/4.0/"
attribution: "The Cannabis White Papers"
refs: [{"id": "rodriguez-morrison-2021-cannabis-light-intensity-yield", "n": 1, "cite": "Rodriguez-Morrison, V., Llewellyn, D., & Zheng, Y. (2021). Cannabis Yield, Potency, and Leaf Photosynthesis Respond Differently to Increasing Light Levels in an Indoor Environment. Frontiers in Plant Science, 12, 646020. https://doi.org/10.3389/fpls.2021.646020", "url": "https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2021.646020/full", "peer": true}, {"id": "chandra-2008-cannabis-photosynthesis-ppfd-co2-temperature", "n": 2, "cite": "Chandra, S., Lata, H., Khan, I. A., & ElSohly, M. A. (2008). Photosynthetic response of Cannabis sativa L. to variations in photosynthetic photon flux densities, temperature and CO2 conditions. Physiology and Molecular Biology of Plants, 14(4), 299-306. https://doi.org/10.1007/s12298-008-0027-x", "url": "https://pubmed.ncbi.nlm.nih.gov/23572895/", "peer": true}, {"id": "llewellyn-2022-cannabis-yield-proportional-light-uv", "n": 3, "cite": "Llewellyn, D., Golem, S., Foley, E., Dinka, S., Jones, A. M. P., & Zheng, Y. (2022). Indoor grown cannabis yield increased proportionally with light intensity, but ultraviolet radiation did not affect yield or cannabinoid content. Frontiers in Plant Science, 13, 974018. https://doi.org/10.3389/fpls.2022.974018", "url": "https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2022.974018/full", "peer": true}, {"id": "moher-2022-cannabis-vegetative-light-intensity-morphology", "n": 4, "cite": "Moher, M., Llewellyn, D., Jones, M., & Zheng, Y. (2022). Light intensity can be used to modify the growth and morphological characteristics of cannabis during the vegetative stage of indoor production. Industrial Crops and Products, 183, 114909. https://doi.org/10.1016/j.indcrop.2022.114909", "url": "https://www.sciencedirect.com/science/article/abs/pii/S0926669022003922", "peer": true}, {"id": "takahashi-murata-2008-environmental-stress-photoinhibition", "n": 5, "cite": "Takahashi, S., & Murata, N. (2008). How do environmental stresses accelerate photoinhibition? Trends in Plant Science, 13(4), 178-182. https://doi.org/10.1016/j.tplants.2008.01.005", "url": "https://pubmed.ncbi.nlm.nih.gov/18328775/", "peer": true}, {"id": "pospisil-2016-ros-photosystem-ii-light-temperature", "n": 6, "cite": "Pospisil, P. (2016). Production of Reactive Oxygen Species by Photosystem II as a Response to Light and Temperature Stress. Frontiers in Plant Science, 7, 1950. https://doi.org/10.3389/fpls.2016.01950", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5183610/", "peer": true}, {"id": "gjindali-johnson-2023-photosynthetic-acclimation", "n": 7, "cite": "Gjindali, A., & Johnson, G. N. (2023). Photosynthetic acclimation to changing environments. Biochemical Society Transactions, 51(2), 473-486. https://doi.org/10.1042/BST20211245", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10212544/", "peer": true}, {"id": "sun-shade-leaf-thickness-chloroplast-acclimation", "n": 8, "cite": "Schumann, T., Paul, S., Melzer, M., Doermann, P., & Jahns, P. (2017). Plant Growth under Natural Light Conditions Provides Highly Flexible Short-Term Acclimation Properties toward High Light Stress. Frontiers in Plant Science, 8, 681. https://doi.org/10.3389/fpls.2017.00681", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5413563/", "peer": true}]
---

# Light acclimation: raise PPFD in steps so plants don't bleach

_Beginner · Light · ~9 min read_

> Light is a curve, not a switch. Raise PPFD in steps the plant can keep up with, and match CO2 to set how high you can go.

## Light is a ramp, not a switch

Two beginner mistakes cause most light damage in a grow room: blasting weak, freshly-rooted clones with full-power light, and the opposite, under-lighting flowering plants out of fear of burning them[^rodriguez-morrison-2021-cannabis-light-intensity-yield].

Both have the same fix. Light intensity is not an on/off control. It is something the plant _adapts to_ over weeks. As light rises gradually, the plant physically rebuilds its light-harvesting machinery to keep pace. Push the intensity up too fast, or push it too high without enough CO2, and the excess energy stops growing the plant and starts damaging it: pale, bleached tips and stalled growth.

The light a plant can take ranges enormously across a full cycle: roughly 80 µmol/m²/s for a tender clone up to around 1500 µmol/m²/s for a mature, CO2-supplemented flowering canopy[^llewellyn-2022-cannabis-yield-proportional-light-uv]. This guide covers how plants acclimate, a week-by-week intensity schedule, how high you can safely go, and how to read the warning signs.

> **Diagram.** A gradual ramp lets the plant build capacity ahead of each new increment of light. A hard jump to full power, an on/off ‘switch’, outruns the plant's ability to use the photons.[^gjindali-johnson-2023-photosynthetic-acclimation]

> **NOTE — Who this is for**
> 
> Anyone who has cooked a clone or been afraid to turn the lights up. Pairs with the [crop-steering](coco-crop-steering.html) and [plant-state dashboard](plant-state-dashboard.html) papers.

## The words you need before we start

These five terms carry the whole guide. Read them once and the rest reads easily. Each one comes back in context.

**PPFD (Photosynthetic Photon Flux Density)** — How bright the usable light is right at the canopy, measured in µmol/m²/s (micromoles of light particles per square metre per second). This is the ‘intensity now’ number.

**DLI (Daily Light Integral)** — The total usable light a plant receives over a whole day, in mol/m²/day. It combines intensity (PPFD) with how many hours the lights are on. It is the day's total ‘dose.’

**Photoperiod** — The daily light/dark schedule. 18/6 (18 hours on) is typical for vegetative growth; switching to 12/12 triggers flowering.

**Photoinhibition / bleaching** — Damage that happens when the leaf captures more light energy than it can use. The surplus energy creates reactive oxygen species that attack the leaf, leaving pale or white tips.

**Acclimation** — The multi-week process where a plant builds more chloroplasts, thicker protective leaf surfaces, and protective enzymes so it can safely handle higher light.

> **Diagram.** PPFD is a snapshot of intensity. DLI is the accumulated total over the day. Changing the photoperiod changes DLI even when PPFD stays the same.

## What the plant builds as it adapts

The plant invests in hardware to match rising light. Week over week it builds more chloroplasts (the tiny green factories that catch light), thicker protective leaf surfaces, and a higher density of the enzymes that turn captured energy into sugar[^sun-shade-leaf-thickness-chloroplast-acclimation]. Each new increment of light then has machinery ready and waiting to use it.

A plant built only for moderate light cannot absorb a sudden flood of photons. The light-harvesting side keeps catching energy, but there is nowhere for it to go. The surplus is converted into **reactive oxygen species**, unstable molecules that damage the leaf from the inside[^takahashi-murata-2008-environmental-stress-photoinhibition]. In effect the leaf attacks itself: you see bleached tips and growth grinds to a halt[^pospisil-2016-ros-photosystem-ii-light-temperature].

This is the whole case for incremental ramping. Add light in small steps the plant can keep pace with, and capacity scales alongside intensity, so every photon becomes sugar instead of damage[^gjindali-johnson-2023-photosynthetic-acclimation].

> **Diagram.** The safe ramp is a loop: a small rise, the plant builds capacity, then the next small rise. [^sun-shade-leaf-thickness-chloroplast-acclimation]

> **Diagram.** A plant flooded before it has acclimated converts much of the light into damage rather than sugar. A ramped plant captures nearly all of it.[^takahashi-murata-2008-environmental-stress-photoinhibition]

> **WARN — Bleaching is self-inflicted damage**
> 
> Pale, white-tipped upper leaves are not ‘light hunger’. They are the leaf burning itself with energy it can't use. The cure is less light or more capacity, never more light.

## Light is the accelerator, CO2 is the fuel

Photosynthesis has two halves. The **light reactions** capture energy from photons. The **Calvin cycle** then uses CO2 from the air to turn that captured energy into sugar. Both halves have to scale together[^chandra-2008-cannabis-photosynthesis-ppfd-co2-temperature].

Raise light but leave CO2 low and you trip the same trap as ramping too fast. The light reactions keep capturing energy that the Calvin cycle has no CO2 to fix onto anything. The energy backs up and causes the _exact same_ oxidative bleaching as ramping too fast. You cannot tell the two mistakes apart by looking at the leaf[^pospisil-2016-ros-photosystem-ii-light-temperature].

High-light setups demand matched CO2. On ambient air (around 400–600 ppm CO2), pushing much above ~850 µmol/m²/s mostly burns electricity instead of making sugar[^chandra-2008-cannabis-photosynthesis-ppfd-co2-temperature]. To run 1200 µmol/m²/s you need roughly 1000–1200 ppm CO2; for 1500, around 1200–1500 ppm[^rodriguez-morrison-2021-cannabis-light-intensity-yield].

> **Diagram.** When CO2 is the bottleneck, extra light just feeds the damage pathway.[^takahashi-murata-2008-environmental-stress-photoinhibition]

> **Diagram.** CO2 sets how high PPFD can usefully go. Past your CO2's ceiling, more light is wasted or harmful.[^chandra-2008-cannabis-photosynthesis-ppfd-co2-temperature]

> **KEY — One sentence to remember**
> 
> Light is the accelerator, CO2 is the fuel. Flooring the pedal with an empty tank doesn't go faster. It stalls and overheats.

## A week-by-week PPFD ramp by growth stage

A representative indoor cycle runs about 14 weeks (~98 days) and ramps light stage by stage[^moher-2022-cannabis-vegetative-light-intensity-morphology]. Clones start soft, veg climbs steadily, and after the flip to flower the plant rebuilds toward its peak before tapering at the end.

The 12/12 flip cuts total daily light (DLI) by about 28% even at the same PPFD, simply because the lights are on fewer hours[^rodriguez-morrison-2021-cannabis-light-intensity-yield]. Plan for that dip rather than panicking and over-cranking the dimmer.

> **Diagram.** DLI climbs through veg, dips at the flip (fewer light hours), then climbs again as flower PPFD rebuilds.[^moher-2022-cannabis-vegetative-light-intensity-morphology]

| Stage | Photoperiod | PPFD range (µmol/m²/s) | Notes |
| --- | --- | --- | --- |
| Clone | 18/6 | 80 → 300 | Soft and gentle while roots and machinery form |
| Vegetative bulking | 18/6 | 300 → 650 | Ramp roughly +100 per week |
| Flower acclimation | 12/12 | 600 → 950 | Rebuild after the flip's DLI dip |
| Peak flower | 12/12 | 950 / 1200 / 1500 | Hold at your control tier's ceiling |
| Maturation | 12/12 | 950 → 850 | Taper slightly as the plant ripens |

*A stage-by-stage ramp. Treat these as starting ranges, not laws. The peak you hold depends on your CO2 and climate.[^rodriguez-morrison-2021-cannabis-light-intensity-yield]*

> **TIP — Mind the flip**
> 
> The DLI drop at 12/12 is normal and expected. Let early flower re-acclimate from ~600 back up toward 950 rather than slamming the lights to peak the day you flip.

## How high you push depends on what you control

Your environment sets your safe peak PPFD, not your ambition. The number you can hold is whatever your CO2, climate and cooling actually support today. Raising the ceiling means raising the whole system, not just the dimmer.

On ambient air the honest ceiling is about 950 µmol/m²/s, with real diminishing returns above ~850 because there isn't enough CO2 to use the extra light[^chandra-2008-cannabis-photosynthesis-ppfd-co2-temperature]. A matched intermediate system supports 1200. The 1500 tier is expert-only and demands the full environmental stack[^llewellyn-2022-cannabis-yield-proportional-light-uv].

|  | Tier 1, Beginner | Tier 2, Intermediate | Tier 3, Expert |
| --- | --- | --- | --- |
| Peak PPFD | ~950 | 1200 | 1500 |
| CO2 required | 400–600 ppm (ambient) | 1000–1200 ppm | 1200–1500 ppm |
| Prerequisites | None, just don't exceed ~850 usefully | Tight VPD + CO2 supplementation | Leaf-temp control + substrate strategy + capable strain |

*Pick the tier your environment actually supports. Below the listed CO2, the higher PPFD just bleaches for nothing.[^rodriguez-morrison-2021-cannabis-light-intensity-yield]*

> **Diagram.** Each tier's ceiling is a whole-system commitment, not just a brighter setting.[^llewellyn-2022-cannabis-yield-proportional-light-uv]

> **WARN — Don't buy a ceiling you can't fuel**
> 
> Running Tier-3 light on Tier-1 air is the most expensive way to bleach plants. Max out the honest ceiling you can fuel before chasing a higher one.

## Hanging height and dimming: how you deliver the ramp

Two levers set canopy PPFD: the fixture's **dimmer** and its **hanging height** above the plants. Both change how much light lands on the leaves, but they don't behave the same way.

Dimming is the cleaner lever for fine, repeatable steps. It changes intensity without changing how widely the light spreads or how much radiant heat reaches the canopy. Raising or lowering the fixture also shifts the spread and the heat, so it's a coarser adjustment.

Whichever lever you use, **verify the real number.** Measure PPFD at the canopy with a meter, or read it off the fixture's distance chart. Don't trust a wattage or a dial position. The same fixture reads very differently at different heights. And re-check whenever the canopy grows toward the light: as plants stretch they get closer to the source, raising effective PPFD even if you changed nothing.

> **Diagram.** Set intensity with the dimmer, height for spread and heat, and always confirm the canopy number rather than guessing.

> **TIP — The canopy moves**
> 
> A plant that stretched 15 cm toward the light this week is getting noticeably more PPFD even though you touched nothing. Re-measure after every growth spurt.

## Signs of too much light, and the traps that cause it

Too much light shows up as **bleached or white tips on the upper canopy**, the leaves closest to the source, together with stalled growth[^pospisil-2016-ros-photosystem-ii-light-temperature]. The catch: the same symptom comes from two different mistakes, and you cannot tell which from the leaf alone.

Mistake one is ramping intensity too fast. Mistake two is high light with low CO2. Both back energy up into the same oxidative damage, so they look identical[^takahashi-murata-2008-environmental-stress-photoinhibition]. Don't try to diagnose by eye. Prevent both: ramp incrementally _and_ keep CO2 matched to your intensity.

| Symptom | Likely cause | What to do |
| --- | --- | --- |
| Bleached / white upper-canopy tips | Ramped too fast OR high light + low CO2 | Back PPFD down a step; confirm CO2 matches your intensity |
| Bleaching despite ‘safe’ PPFD | Out-of-range leaf temp or VPD | Fix climate first: heat and dry air bleach at safe light |
| Stalled growth at high light | Capacity hasn't caught up, or CO2 limited | Hold intensity; let the plant acclimate; check CO2 |
| Pale, stretchy, sparse flower | Chronically under-lit out of fear | Raise PPFD in steps: under-lighting wastes yield too |

*Same damage, different causes. Prevent both rather than guessing after the fact.*

> **DANGER — Don't over-correct in fear**
> 
> After one bleaching scare, growers often crank flower light far too low and leave yield on the table. Chronic under-lighting wastes a crop just as surely as bleaching wastes plants[^rodriguez-morrison-2021-cannabis-light-intensity-yield]. Back down one step, then climb again deliberately.

## What to actually expect from your setup

Light is the schedule, not the whole system. Every PPFD target in this guide assumes the rest of the environment is in range: leaf temperature around 26–28°C, VPD of 1.2–1.5 kPa, adequate root-zone capacity, and a strain that can handle the load[^chandra-2008-cannabis-photosynthesis-ppfd-co2-temperature]. Push light and CO2 without those and you get heated, stressed plants, not bigger yields.

| Required for all tiers | Target |
| --- | --- |
| Leaf temperature | ~26–28°C |
| VPD (air dryness) | 1.2–1.5 kPa |
| Root-zone capacity | Adequate water + oxygen for the demand |
| Strain | Capable of the intended light load |

*These hold for every tier. Light only pays off when temperature, humidity and the root zone are also in range.*

> **KEY — Be honest about your tier**
> 
> A clean run at the honest ceiling beats a sloppy run at a higher one. Most beginners are best served maxing out the ~950 ambient ceiling cleanly, nailing acclimation and CO2 matching first, before ever chasing 1200 or 1500.

Treat light as one input among several. It works only when the rest of the environment cooperates. Learn to read the whole picture in the [plant-state dashboard](plant-state-dashboard.html) paper, and how to act on real signals instead of noise in [signal and noise](signal-and-noise.html).

## References

[^rodriguez-morrison-2021-cannabis-light-intensity-yield]: Rodriguez-Morrison, V., Llewellyn, D., & Zheng, Y. (2021). Cannabis Yield, Potency, and Leaf Photosynthesis Respond Differently to Increasing Light Levels in an Indoor Environment. Frontiers in Plant Science, 12, 646020. https://doi.org/10.3389/fpls.2021.646020 https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2021.646020/full (peer-reviewed)
[^chandra-2008-cannabis-photosynthesis-ppfd-co2-temperature]: Chandra, S., Lata, H., Khan, I. A., & ElSohly, M. A. (2008). Photosynthetic response of Cannabis sativa L. to variations in photosynthetic photon flux densities, temperature and CO2 conditions. Physiology and Molecular Biology of Plants, 14(4), 299-306. https://doi.org/10.1007/s12298-008-0027-x https://pubmed.ncbi.nlm.nih.gov/23572895/ (peer-reviewed)
[^llewellyn-2022-cannabis-yield-proportional-light-uv]: Llewellyn, D., Golem, S., Foley, E., Dinka, S., Jones, A. M. P., & Zheng, Y. (2022). Indoor grown cannabis yield increased proportionally with light intensity, but ultraviolet radiation did not affect yield or cannabinoid content. Frontiers in Plant Science, 13, 974018. https://doi.org/10.3389/fpls.2022.974018 https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2022.974018/full (peer-reviewed)
[^moher-2022-cannabis-vegetative-light-intensity-morphology]: Moher, M., Llewellyn, D., Jones, M., & Zheng, Y. (2022). Light intensity can be used to modify the growth and morphological characteristics of cannabis during the vegetative stage of indoor production. Industrial Crops and Products, 183, 114909. https://doi.org/10.1016/j.indcrop.2022.114909 https://www.sciencedirect.com/science/article/abs/pii/S0926669022003922 (peer-reviewed)
[^takahashi-murata-2008-environmental-stress-photoinhibition]: Takahashi, S., & Murata, N. (2008). How do environmental stresses accelerate photoinhibition? Trends in Plant Science, 13(4), 178-182. https://doi.org/10.1016/j.tplants.2008.01.005 https://pubmed.ncbi.nlm.nih.gov/18328775/ (peer-reviewed)
[^pospisil-2016-ros-photosystem-ii-light-temperature]: Pospisil, P. (2016). Production of Reactive Oxygen Species by Photosystem II as a Response to Light and Temperature Stress. Frontiers in Plant Science, 7, 1950. https://doi.org/10.3389/fpls.2016.01950 https://pmc.ncbi.nlm.nih.gov/articles/PMC5183610/ (peer-reviewed)
[^gjindali-johnson-2023-photosynthetic-acclimation]: Gjindali, A., & Johnson, G. N. (2023). Photosynthetic acclimation to changing environments. Biochemical Society Transactions, 51(2), 473-486. https://doi.org/10.1042/BST20211245 https://pmc.ncbi.nlm.nih.gov/articles/PMC10212544/ (peer-reviewed)
[^sun-shade-leaf-thickness-chloroplast-acclimation]: Schumann, T., Paul, S., Melzer, M., Doermann, P., & Jahns, P. (2017). Plant Growth under Natural Light Conditions Provides Highly Flexible Short-Term Acclimation Properties toward High Light Stress. Frontiers in Plant Science, 8, 681. https://doi.org/10.3389/fpls.2017.00681 https://pmc.ncbi.nlm.nih.gov/articles/PMC5413563/ (peer-reviewed)
