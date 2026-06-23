---
slug: "lighting-fundamentals"
title: "Lighting: spectrum, PPFD and DLI"
eyebrow: "Beginner · Light"
summary: "A from-zero guide to how grow light actually works: what to measure, what to aim for at each stage, and how to avoid cooking your plants."
track: "Environment & climate"
read_time: "~14 min read"
diagrams: "9 diagrams"
related: ["light-acclimation", "cloning", "flowering-stages"]
url: "https://jaketherabbit.github.io/cannabis-white-papers/lighting-fundamentals.html"
md_url: "https://jaketherabbit.github.io/cannabis-white-papers/papers/lighting-fundamentals.md"
version: "1.0"
updated: "2026-06-24"
license: "CC BY-NC 4.0"
license_url: "https://creativecommons.org/licenses/by-nc/4.0/"
attribution: "The Cannabis White Papers"
refs: [{"id": "rodriguez-morrison-2021-light-levels-yield-photosynthesis", "n": 1, "cite": "Rodriguez-Morrison, V., Llewellyn, D., & Zheng, Y. (2021). Cannabis Yield, Potency, and Leaf Photosynthesis Respond Differently to Increasing Light Levels in an Indoor Environment. Frontiers in Plant Science, 12, 646020.", "url": "https://doi.org/10.3389/fpls.2021.646020", "peer": true}, {"id": "llewellyn-2022-light-intensity-proportional-uv-no-effect", "n": 2, "cite": "Llewellyn, D., Golem, S., Foley, E., Dinka, S., Jones, A.M.P., & Zheng, Y. (2022). Indoor grown cannabis yield increased proportionally with light intensity, but ultraviolet radiation did not affect yield or cannabinoid content. Frontiers in Plant Science, 13, 974018.", "url": "https://doi.org/10.3389/fpls.2022.974018", "peer": true}, {"id": "magagnini-2018-light-spectrum-morphology-cannabinoids", "n": 3, "cite": "Magagnini, G., Grassi, G., & Kotiranta, S. (2018). The Effect of Light Spectrum on the Morphology and Cannabinoid Content of Cannabis sativa L. Medical Cannabis and Cannabinoids, 1(1), 19-27.", "url": "https://doi.org/10.1159/000489030", "peer": true}, {"id": "kusuma-2021-nir-leds-delay-flowering-phytochrome", "n": 4, "cite": "Kusuma, P., Westmoreland, F.M., Zhen, S., & Bugbee, B. (2021). Photons from NIR LEDs can delay flowering in short-day soybean and Cannabis: Implications for phytochrome activity. PLOS ONE, 16(7), e0255232.", "url": "https://doi.org/10.1371/journal.pone.0255232", "peer": true}, {"id": "eichhorn-bilodeau-2019-photobiology-cannabis-review", "n": 5, "cite": "Eichhorn Bilodeau, S., Wu, B.-S., Rufyikiri, A.-S., MacPherson, S., & Lefsrud, M. (2019). An Update on Plant Photobiology and Implications for Cannabis Production. Frontiers in Plant Science, 10, 296.", "url": "https://doi.org/10.3389/fpls.2019.00296", "peer": true}, {"id": "nelson-bugbee-2014-efficacy-led-vs-hps", "n": 6, "cite": "Nelson, J.A., & Bugbee, B. (2014). Economic Analysis of Greenhouse Lighting: Light Emitting Diodes vs. High Intensity Discharge Fixtures. PLOS ONE, 9(6), e99010.", "url": "https://doi.org/10.1371/journal.pone.0099010", "peer": true}, {"id": "westmoreland-2021-blue-fraction-efficacy-cannabis", "n": 7, "cite": "Westmoreland, F.M., Kusuma, P., & Bugbee, B. (2021). Cannabis lighting: Decreasing blue photon fraction increases yield but efficacy is more important for cost effective production of cannabinoids. PLOS ONE, 16(3), e0248988.", "url": "https://doi.org/10.1371/journal.pone.0248988", "peer": true}, {"id": "chandra-2008-photosynthetic-response-ppfd-co2-temp", "n": 8, "cite": "Chandra, S., Lata, H., Khan, I.A., & ElSohly, M.A. (2008). Photosynthetic response of Cannabis sativa L. to variations in photosynthetic photon flux densities, temperature and CO2 conditions. Physiology and Molecular Biology of Plants, 14(4), 299-306.", "url": "https://doi.org/10.1007/s12298-008-0027-x", "peer": true}, {"id": "kotiranta-2024-high-light-specialized-metabolites-cannabis", "n": 9, "cite": "Kotiranta, S., Pihlava, J.-M., Kotilainen, T., & Palonen, P. (2024). High light intensity improves yield of specialized metabolites in medicinal cannabis (Cannabis sativa L.), resulting from both higher inflorescence mass and concentrations of metabolites. Industrial Crops and Products, 211, 118210.", "url": "https://doi.org/10.1016/j.indcrop.2024.118210", "peer": true}]
---

# Lighting: spectrum, PPFD and DLI

_Beginner · Light · ~14 min read_

> A from-zero guide to how grow light actually works: what to measure, what to aim for at each stage, and how to avoid cooking your plants.

## What this is (and why light is the engine)

Light is not just ‘on or off.’ It is the raw fuel a plant turns into sugar, and the single biggest lever on yield and quality you control indoors. This paper assumes you know nothing: it defines every term, gives concrete numbers to aim for at each growth stage, and explains the one switch that makes a plant flower.

Plants eat light. Photosynthesis converts light energy plus CO2 and water into sugar, so more usable light, up to a limit, means more growth[^chandra-2008-photosynthetic-response-ppfd-co2-temp]. The three numbers that matter most are PPFD (how bright, right now), DLI (how much total light per day), and spectrum (the color mix). Every term is defined the first time it appears.

> **Diagram.** Light is the input, but it only pays off when CO2, water and nutrients keep pace.

> **NOTE — This pairs with the acclimation paper**
> 
> Read this one for the targets. Read the [light acclimation](light-acclimation.html) paper for how to ramp up to them safely, so young plants adapt instead of bleaching.

## PAR, PPFD, DLI and umol/J in plain English

Get the gist of these five terms and the rest of the paper falls into place. They all describe the same thing from different angles: how much usable light a plant is getting.

**PAR (Photosynthetically Active Radiation)** — The slice of light from 400 to 700 nm that plants can use for photosynthesis[^eichhorn-bilodeau-2019-photobiology-cannabis-review]. Lumens and watts do not measure this, which is why a bright-looking bulb can be useless for plants.

**PPFD (Photosynthetic Photon Flux Density)** — How many usable photons land on one square meter each second, in micromoles (umol/m2/s). This is ‘how bright’ at the canopy. Measure it with a quantum/PAR meter, not a phone lux app.

**DLI (Daily Light Integral)** — The total photons delivered over a whole day, in moles per square meter (mol/m2/day). This is the number that actually drives yield. DLI = PPFD x seconds of light per day / 1,000,000[^rodriguez-morrison-2021-light-levels-yield-photosynthesis].

**Efficacy (umol/J)** — How many usable photons a fixture makes per joule of electricity. This is the headline efficiency number when shopping: higher means more light per dollar of power.

**Photoperiod** — Hours of light per 24 hours. ‘18/6’ means 18 on, 6 off.

> **Diagram.** Worked DLI examples: a lower PPFD over more hours can match a higher PPFD over fewer hours. The daily total is what counts.[^rodriguez-morrison-2021-light-levels-yield-photosynthesis]

> **Diagram.** PAR is the 400 to 700 nm band plants use. Lux meters weight toward green, so they are the wrong tool for plant light.[^eichhorn-bilodeau-2019-photobiology-cannabis-review]

## Spectrum: what each color does

Blue light, roughly 400 to 500 nm, keeps plants compact with tight internode spacing and is linked to denser growth and resin in flower[^magagnini-2018-light-spectrum-morphology-cannabinoids]. Red light, 600 to 700 nm, is the most photosynthetically efficient band and drives flowering and stretch[^westmoreland-2021-blue-fraction-efficacy-cannabis].

‘Full-spectrum white’ LEDs are rated by color temperature in Kelvin. Higher-K and bluer (around 4000 to 6500K) leans veg, lower-K and redder (around 3000 to 3500K) leans flower. A good broad white spectrum works fine across both stages for beginners. The practical takeaway: do not over-optimize spectrum early. Intensity matters far more for yield than chasing a perfect color recipe.

| Band (nm) | Name | Main effect | When it matters |
| --- | --- | --- | --- |
| 280-400 | UV | Stress response, possible resin; safety hazard | Optional, end of flower |
| 400-500 | Blue | Compact growth, tight internodes, thicker leaves | Veg |
| 500-600 | Green | Penetrates deeper into the canopy than expected | Minor lever, all stages |
| 600-700 | Red | Highest photosynthetic efficiency, drives flowering and stretch | Flower |
| 700-750 | Far-red | Speeds the dark response, adds stem stretch | Fine-tuning only |

*What each part of the spectrum does. Green is not wasted: it reaches lower leaves, but it is a minor lever.*

> **TIP — Beginner rule on spectrum**
> 
> A quality full-spectrum white LED covers veg and flower. Intensity beats spectrum tuning, so spend your attention on PPFD and DLI before you chase color recipes.

## Intensity and the daily dose: targets by stage

Young tissue cannot process intense light, so targets climb as the plant matures. Clones and seedlings want about 100-300 PPFD (DLI ~10-15 mol)[^rodriguez-morrison-2021-light-levels-yield-photosynthesis], early-to-late veg about 300-600 PPFD (DLI ~20-35 mol), and flower about 700-900 PPFD without added CO2 (DLI ~30-45 mol)[^llewellyn-2022-light-intensity-proportional-uv-no-effect].

Pushing past about 900 PPFD only pays off if you also raise CO2 to 1000-1200 ppm and tighten temperature and humidity[^chandra-2008-photosynthetic-response-ppfd-co2-temp]. Otherwise extra light just causes stress and bleaching. Because DLI bundles intensity and hours together, you can hit the same daily dose with lower PPFD over more hours (veg at 18/6) or higher PPFD over fewer hours (flower at 12/12).

> **Diagram.** Flower intensity zones. Most rooms top out around 700-900 PPFD. The 1000-1400 band needs CO2 and serious climate control.[^kotiranta-2024-high-light-specialized-metabolites-cannabis]

> **Diagram.** Growth rises with DLI, levels off at light saturation, then falls as stress and bleaching set in. Adding CO2 moves the saturation point to the right.[^chandra-2008-photosynthetic-response-ppfd-co2-temp]

| Stage | PPFD (umol/m2/s) | DLI (mol/m2/day) | Photoperiod |
| --- | --- | --- | --- |
| Clone / seedling | 100-300 | ~10-15 | 18/6 |
| Early veg | 300-450 | ~20-29 | 18/6 |
| Late veg | 450-600 | ~29-39 | 18/6 |
| Flower (no CO2) | 700-900 | ~30-45 | 12/12 |
| Flower (CO2 1000-1200 ppm) | 1000-1400 | ~40-60 | 12/12 |

*Stage targets. 600 PPFD x 18h (veg) is roughly the same daily dose as 800 PPFD x 12h (flower).*

## The photoperiod flip that triggers flowering

Photoperiod-type cannabis stays vegetative under long days (commonly 18/6) and is forced to flower by switching to 12 hours light and 12 hours uninterrupted dark[^kusuma-2021-nir-leds-delay-flowering-phytochrome]. This is ‘the flip.’

The plant does not count light hours. It measures the length of the unbroken dark period using a pigment called phytochrome, which flips between an active form (Pfr) and an inactive form (Pr). Once nights are long enough it produces a flowering signal, florigen, in the leaves[^eichhorn-bilodeau-2019-photobiology-cannabis-review]. This is why light leaks matter so much: even a phone screen, an indicator LED, or a pinhole in a tent during lights-off can reset phytochrome and stall or revert flowering, cause re-vegging, or trigger hermaphrodites[^kusuma-2021-nir-leds-delay-flowering-phytochrome].

> **Diagram.** Phytochrome tracks the dark period. A light leak during lights-off resets the clock and stalls the flip.[^kusuma-2021-nir-leds-delay-flowering-phytochrome]

> **DANGER — Seal your dark period**
> 
> Light leaks during the dark period are the number one beginner flowering failure: stalled bloom, re-veg, or hermaphrodites. Far-red and red are exactly what phytochrome senses. Seal pinholes, cover indicator LEDs, use light-proof ducting. If you can see in the dark, so can the plant.

## LED vs HPS vs CMH, and reading efficacy

Modern LED is the efficiency leader at roughly 2.7-3.0 umol/J for good fixtures (budget units 2.0-2.3), runs cooler, and lasts longer[^nelson-bugbee-2014-efficacy-led-vs-hps]. HPS (high-pressure sodium) sits around 1.7-1.9 umol/J and runs hot but is cheap to buy. CMH/LEC (ceramic metal halide) lands lower, around 1.3-1.9 umol/J, but has a pleasant broad spectrum.

Efficacy (umol/J) is the number to compare. A 3.0 umol/J LED makes about 60% more usable light than a ~1.85 umol/J double-ended HPS for the same power bill[^nelson-bugbee-2014-efficacy-led-vs-hps]. For beginners, a reputable full-spectrum LED with a published PPFD map and efficacy at or above ~2.5 umol/J is the safe default. Ignore inflated ‘equivalent watt’ marketing and look at actual PPF (total umol/s) and coverage.

> **Diagram.** Efficacy by fixture type. Good LED clears the ~2.5 umol/J threshold comfortably; HPS and CMH fall short.[^nelson-bugbee-2014-efficacy-led-vs-hps]

| Type | Efficacy (umol/J) | Heat | Upfront cost | Best for |
| --- | --- | --- | --- | --- |
| LED | 2.0-3.0 | Low | Higher | Default choice, all stages |
| HPS | 1.7-1.9 | High | Low | Budget builds, red-heavy flower |
| CMH / LEC | 1.3-1.9 | Medium | Medium | Broad natural spectrum incl. some UV |

*Compare on efficacy and total PPF plus a real PPFD map, never on lumens or 'equivalent watts.'*

## Hanging height, coverage, and a stage-by-stage setup

Light obeys the inverse-square law: roughly doubling the distance from the canopy cuts PPFD by about 75%. Height is your coarse intensity dial, the dimmer is the fine dial. Hang about 24 in for seedlings and clones, ~18 in for veg, and ~12-16 in for flower, then fine-tune with the dimmer and a PAR meter.

Verify coverage by taking PPFD readings at nine points: four corners, four edge-midpoints, and the center. Aim for a min-to-average ratio above 0.75 so edge plants are not starved while the center bleaches. Hanging higher trades peak intensity for more even spread, so use a manufacturer PPFD map as your starting point and confirm with real readings at canopy height.

> **Diagram.** Sample of a 9-point grid. Compare the lowest reading to the average: a min-to-average ratio above 0.75 is acceptable uniformity.

| Stage | Hang height | Target PPFD | Photoperiod |
| --- | --- | --- | --- |
| Clone / seedling | ~24 in | 100-300 | 18/6 |
| Veg | ~18 in | 300-600 | 18/6 |
| Flower | ~12-16 in | 700-900 | 12/12 |

*Starting heights. Always confirm against your fixture's PPFD map and a meter at canopy height.*

> **TIP — Ramp, do not slam**
> 
> Pair this with the [light acclimation](light-acclimation.html) paper: raise the dimmer or lower the fixture over several days rather than jumping a fresh clone to full intensity.

## Light stress, far-red and UV, and common mistakes

Too much light shows as bleaching (white or yellow bud tips directly under the fixture), upward-cupping or ‘taco’ leaves, and faded color even when nutrients are fine. The fix is to dim or raise the light, not to feed more.

Far-red (~730 nm) can speed the transition to dark via the phytochrome system and slightly stretch plants[^kusuma-2021-nir-leds-delay-flowering-phytochrome]. UV-B in the final 1-2 weeks is a popular potency play, but the evidence that UV-B reliably raises cannabinoids or yield is mixed[^llewellyn-2022-light-intensity-proportional-uv-no-effect], and it carries real eye, skin and plant-stress risks. Treat it as optional and advanced.

| Symptom | Likely cause | What to do |
| --- | --- | --- |
| Bleached / white tops under the fixture | Too much PPFD | Raise or dim the light, do not feed |
| Taco / upward-cupping leaves | Light plus heat stress | Raise the light, check leaf-surface temp |
| Stretchy, pale growth | Too little light or hung too far | Lower the fixture or boost intensity |
| Stalled flowering, re-veg | Light leak during the dark period | Seal the room light-tight |
| Scorched tops, PPFD looks fine | Radiant heat (esp. HPS) | Raise the fixture, watch leaf temp |

*The biggest avoidable errors: jumping a clone to flower-level PPFD, trusting lux/wattage over a PAR meter, and ignoring light leaks.*

## Realistic expectations

More light only helps up to the point where something else (CO2, water, nutrients, temperature or genetics) becomes the limiting factor. Past saturation you pay for electricity and heat with no extra yield, and eventually with stress[^rodriguez-morrison-2021-light-levels-yield-photosynthesis].

> **Diagram.** The limiting-factor idea: pushing light far above the other inputs wastes effort. Lift the shortest stave first.[^chandra-2008-photosynthetic-response-ppfd-co2-temp]

> **KEY — What to actually do**
> 
> 1. **Without CO2, ~700-900 PPFD / ~35-45 mol DLI in flower is a sensible ceiling.** The 1000-1400 PPFD regime needs CO2, cooling and humidity control: a whole-room commitment, not just a brighter light.
> 2. **Nail intensity, dose and photoperiod first.** Spectrum tweaks like far-red and UV are fine-tuning, not the main lever.
> 3. **Buy on efficacy and a real PPFD map.** Hit the stage targets, seal your dark period, and lighting stops being your bottleneck.

Once lighting is handled, the rest is climate, feed and genetics. Read the [light acclimation](light-acclimation.html) paper for how to ramp safely, and the [flowering stages](flowering-stages.html) paper for what happens after the flip.

## References

[^rodriguez-morrison-2021-light-levels-yield-photosynthesis]: Rodriguez-Morrison, V., Llewellyn, D., & Zheng, Y. (2021). Cannabis Yield, Potency, and Leaf Photosynthesis Respond Differently to Increasing Light Levels in an Indoor Environment. Frontiers in Plant Science, 12, 646020. https://doi.org/10.3389/fpls.2021.646020 (peer-reviewed)
[^llewellyn-2022-light-intensity-proportional-uv-no-effect]: Llewellyn, D., Golem, S., Foley, E., Dinka, S., Jones, A.M.P., & Zheng, Y. (2022). Indoor grown cannabis yield increased proportionally with light intensity, but ultraviolet radiation did not affect yield or cannabinoid content. Frontiers in Plant Science, 13, 974018. https://doi.org/10.3389/fpls.2022.974018 (peer-reviewed)
[^magagnini-2018-light-spectrum-morphology-cannabinoids]: Magagnini, G., Grassi, G., & Kotiranta, S. (2018). The Effect of Light Spectrum on the Morphology and Cannabinoid Content of Cannabis sativa L. Medical Cannabis and Cannabinoids, 1(1), 19-27. https://doi.org/10.1159/000489030 (peer-reviewed)
[^kusuma-2021-nir-leds-delay-flowering-phytochrome]: Kusuma, P., Westmoreland, F.M., Zhen, S., & Bugbee, B. (2021). Photons from NIR LEDs can delay flowering in short-day soybean and Cannabis: Implications for phytochrome activity. PLOS ONE, 16(7), e0255232. https://doi.org/10.1371/journal.pone.0255232 (peer-reviewed)
[^eichhorn-bilodeau-2019-photobiology-cannabis-review]: Eichhorn Bilodeau, S., Wu, B.-S., Rufyikiri, A.-S., MacPherson, S., & Lefsrud, M. (2019). An Update on Plant Photobiology and Implications for Cannabis Production. Frontiers in Plant Science, 10, 296. https://doi.org/10.3389/fpls.2019.00296 (peer-reviewed)
[^nelson-bugbee-2014-efficacy-led-vs-hps]: Nelson, J.A., & Bugbee, B. (2014). Economic Analysis of Greenhouse Lighting: Light Emitting Diodes vs. High Intensity Discharge Fixtures. PLOS ONE, 9(6), e99010. https://doi.org/10.1371/journal.pone.0099010 (peer-reviewed)
[^westmoreland-2021-blue-fraction-efficacy-cannabis]: Westmoreland, F.M., Kusuma, P., & Bugbee, B. (2021). Cannabis lighting: Decreasing blue photon fraction increases yield but efficacy is more important for cost effective production of cannabinoids. PLOS ONE, 16(3), e0248988. https://doi.org/10.1371/journal.pone.0248988 (peer-reviewed)
[^chandra-2008-photosynthetic-response-ppfd-co2-temp]: Chandra, S., Lata, H., Khan, I.A., & ElSohly, M.A. (2008). Photosynthetic response of Cannabis sativa L. to variations in photosynthetic photon flux densities, temperature and CO2 conditions. Physiology and Molecular Biology of Plants, 14(4), 299-306. https://doi.org/10.1007/s12298-008-0027-x (peer-reviewed)
[^kotiranta-2024-high-light-specialized-metabolites-cannabis]: Kotiranta, S., Pihlava, J.-M., Kotilainen, T., & Palonen, P. (2024). High light intensity improves yield of specialized metabolites in medicinal cannabis (Cannabis sativa L.), resulting from both higher inflorescence mass and concentrations of metabolites. Industrial Crops and Products, 211, 118210. https://doi.org/10.1016/j.indcrop.2024.118210 (peer-reviewed)
