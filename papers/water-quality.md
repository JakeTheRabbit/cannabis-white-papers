---
slug: "water-quality"
title: "Source water, RO and alkalinity"
eyebrow: "Feed · Water"
summary: "What is in your water before nutrients ever go in: tap vs RO vs well, starting EC, alkalinity and carbonates, chlorine and chloramine, hardness, and when reverse osmosis is actually worth the money."
track: "Water, substrate & feed"
read_time: "~14 min read"
diagrams: ""
related: ["ph-management", "nutrient-mixing-athena", "irrigation-manual"]
url: "https://jaketherabbit.github.io/cannabis-white-papers/water-quality.html"
md_url: "https://jaketherabbit.github.io/cannabis-white-papers/papers/water-quality.md"
version: "1.2"
updated: "2026-07-18"
license: "CC BY-NC 4.0"
license_url: "https://creativecommons.org/licenses/by-nc/4.0/"
attribution: "The Cannabis White Papers"
refs: [{"id": "bevan-2021-npk-flowering-cannabis", "n": 1, "cite": "Bevan, L., Jones, M., & Zheng, Y. (2021). Optimisation of Nitrogen, Phosphorus, and Potassium for Soilless Production of Cannabis sativa in the Flowering Stage Using Response Surface Analysis. Frontiers in Plant Science, 12, 764103.", "url": "https://doi.org/10.3389/fpls.2021.764103", "peer": true}, {"id": "kpai-2024-mineral-nutrition-vegetative-cannabis", "n": 2, "cite": "Kpai, P., et al. (2024). Mineral nutrition for Cannabis sativa in the vegetative stage using response surface analysis. Frontiers in Plant Science, 15, 1501484.", "url": "https://doi.org/10.3389/fpls.2024.1501484", "peer": true}, {"id": "umass-water-quality-ph-alkalinity", "n": 3, "cite": "University of Massachusetts Amherst, Center for Agriculture, Food, and the Environment (Greenhouse & Floriculture Program). Water quality: pH and alkalinity (fact sheet). UMass Extension.", "url": "https://www.umass.edu/agriculture-food-environment/greenhouse-floriculture/fact-sheets/water-quality-ph-alkalinity", "peer": false}, {"id": "fisher-purdue-ho242-alkalinity-soilless", "n": 4, "cite": "Fisher, P., et al. (Purdue University Extension). HO-242-W: Alkalinity Management in Soilless Substrates. Purdue Extension.", "url": "https://www.extension.purdue.edu/extmedia/ho/ho-242-w.pdf", "peer": false}, {"id": "ferrarezi-2023-chlorine-phytotoxicity-rex-lettuce", "n": 5, "cite": "Ferrarezi, R. S., et al. (2023). Irrigation Sources with Chlorine Drinking Water Standard Limits Cause Phytotoxicity on 'Rex' Lettuce Grown in Hydroponic Systems. HortTechnology, 33(1), 125-130.", "url": "https://doi.org/10.21273/HORTTECH05091-22", "peer": true}, {"id": "date-2005-chloramines-lettuce-hydroponic", "n": 6, "cite": "Date, S., Terabayashi, S., Kobayashi, Y., & Fujime, Y. (2005). Effects of chloramines concentration in nutrient solution and exposure time on plant growth in hydroponically cultured lettuce. Scientia Horticulturae, 103(3), 257-265.", "url": "https://doi.org/10.1016/j.scienta.2004.06.005", "peer": true}, {"id": "sutton-2006-pythium-hydroponic-etiology", "n": 7, "cite": "Sutton, J. C., Sopher, C. R., Owen-Going, T. N., Liu, W., Grodzinski, B., Hall, J. C., & Benchimol, R. L. (2006). Etiology and epidemiology of Pythium root rot in hydroponic crops: current knowledge and perspectives. Summa Phytopathologica, 32(4), 307-321.", "url": "https://doi.org/10.1590/S0100-54052006000400001", "peer": true}, {"id": "fao-dissolved-oxygen-temperature", "n": 8, "cite": "FAO. Dissolved Oxygen (Section 4). In: Water Quality for Aquaculture / Inland Water Resources and Aquaculture Service. Food and Agriculture Organization of the United Nations.", "url": "https://www.fao.org/4/ac183e/ac183e04.htm", "peer": false}]
---

# Source water, RO and alkalinity

_Feed · Water · ~14 min read_

> What is in your water before nutrients ever go in: tap vs RO vs well, starting EC, alkalinity and carbonates, chlorine and chloramine, hardness, and when reverse osmosis is actually worth the money.

## Your water is the first ingredient, not a blank slate

Every feed you give a cannabis plant starts with water, and that water is almost never pure. Tap, well, and rainwater all arrive carrying dissolved minerals, gases, and treatment chemicals that change pH, take up room in your nutrient recipe, and can harm roots or beneficial microbes before you add a single drop of fertiliser.

The plant never tastes your nutrients in isolation. It tastes water plus minerals plus nutrients combined. That is why two growers using the identical feed chart can get opposite results purely because of source-water differences. You cannot manage what you have not measured, so a water test comes before any nutrient decision.

> **Diagram.** Your source water and its dissolved load are the starting point. Mixing only adds to what is already there, so a problem in the first box follows the water all the way to the root.

> **NOTE — What this paper does**
>
> It walks an absolute beginner from understanding what is in their source water, to testing it, to deciding whether reverse osmosis is worth the cost. Pairs with the [pH management](ph-management.html) and [nutrient mixing](nutrient-mixing-athena.html) papers.

## The vocabulary, in plain words

Water-quality talk is full of jargon that hides simple ideas. Get the gist of these and the rest of the paper reads easily. The big one to grasp early: alkalinity is not the same thing as pH.

**EC (electrical conductivity)** — How well water conducts electricity, which rises with dissolved salts. Measured in mS/cm or uS/cm. Higher EC means more dissolved stuff.

**PPM / TDS (parts per million / total dissolved solids)** — The same idea as EC but expressed as a weight. Note that PPM pens use a conversion factor (a 500 or 700 scale), so two meters can disagree on the same water.

**pH** — Acidity on a 0-14 scale. Most cannabis nutrient uptake targets pH 5.8-6.2 in hydro and coco, and 6.2-6.8 in soil.

**Alkalinity** — The water's buffering capacity from carbonates and bicarbonates, reported as ppm CaCO3. High alkalinity pushes root-zone pH up over time even after you pH-down the tank. This is a different thing from pH itself.

**Hardness** — Dissolved calcium and magnesium, reported as ppm CaCO3 or grains per gallon (1 GPG = 17.1 mg/L).

**RO (reverse osmosis)** — Filtration that forces water through a membrane and strips most dissolved minerals, leaving near-zero PPM water.

> **Diagram.** pH is where the water sits at this moment. Alkalinity is the buffer that drags it back up afterwards, which is why a perfect tank reading can still drift in the root zone.[^umass-water-quality-ph-alkalinity]

## Tap, well, and rain: three very different starting points

Municipal tap water is treated and consistent but carries chlorine or chloramine and often moderate-to-high mineral content, sometimes 150-300+ ppm straight from the faucet[^umass-water-quality-ph-alkalinity]. Well water is the wild card: it can be very hard, high in iron, manganese, or sulfur, and it varies seasonally, so it must be tested. Rainwater is naturally low in dissolved minerals but offers little buffering and can pick up roof and storage contaminants.

> **Diagram.** Where your water starts on the PPM scale. RO and rain arrive near zero, soft tap is workable, and hard tap or well water can eat most of your nutrient headroom before you begin.[^umass-water-quality-ph-alkalinity]

Headroom is the point beginners miss. A working feed strength is commonly capped near your total EC budget (set targets in mS/cm), so hard tap water at 300+ ppm leaves almost no room before you hit that ceiling[^bevan-2021-npk-flowering-cannabis]. Rainwater typically arrives at only 0-20 ppm, which is closer to RO, but it brings little to no buffering and a risk of pathogens, roofing contaminants, or sodium near coasts.

> **TIP — Match the source to the habit**
>
> - **Tap:** consistent and convenient, but expect chlorine or chloramine and a starting EC that eats into your nutrient room.
> - **Well:** free and unmetered, but composition swings. Test at least twice a year and after heavy rain.
> - **Rain:** low starting PPM like RO, but low buffering. Filter it and watch for sodium and contaminants.

## Alkalinity and carbonates: why your pH won't stay put

Alkalinity is the single most misunderstood water parameter for beginners. It is caused by dissolved carbonates and bicarbonates, and it acts like a chemical spring that drags root-zone pH back upward even after you adjust the tank to 5.8. A common acceptable range for container cannabis is roughly 40-100 ppm CaCO3, with many growers targeting 30-60 ppm as an optimum[^fisher-purdue-ho242-alkalinity-soilless]. The conversions to know: 1 meq/L equals 50 ppm CaCO3 equals 61 ppm bicarbonate[^umass-water-quality-ph-alkalinity].

> **Diagram.** A high-alkalinity water that you pH-down to 5.8 climbs back to 6.8+ within days. A corrected or naturally low-alkalinity water holds near 5.8-6.0 instead.[^fisher-purdue-ho242-alkalinity-soilless]

Above roughly 100-150 ppm CaCO3, alkalinity steadily raises substrate pH and locks out iron, manganese, and other micronutrients[^umass-water-quality-ph-alkalinity]. You correct excess alkalinity by adding acid, such as phosphoric, nitric, or citric, to neutralise the carbonates, not just to hit a pH number once. At the other extreme, very low alkalinity (RO, rain) means almost no buffer, so pH swings fast and small acid or base errors matter more.

> **Diagram.** The workable window. Below 30 ppm you lose your buffer, the 30-100 ppm band is comfortable, and above 150 ppm you fight rising pH and micronutrient lockout.[^fisher-purdue-ho242-alkalinity-soilless]

## Chlorine, chloramine, and hardness: what helps and what harms

Municipalities disinfect with chlorine or the more stable chloramine, and both can damage root tips and beneficial microbes. Root-tip injury has been reported at chlorine concentrations as low as 0.4 ppm[^ferrarezi-2023-chlorine-phytotoxicity-rex-lettuce], which matters most for living-soil and microbe-driven growers. Chlorine off-gasses if water sits and aerates for about 24 hours, but chloramine does not, and removing it requires a catalytic carbon filter or RO[^date-2005-chloramines-lettuce-hydroponic].

> **Diagram.** The removal path differs by chemical. Standing and aerating clears chlorine, but chloramine is stable and survives a night out, so it needs catalytic carbon or RO.[^date-2005-chloramines-lettuce-hydroponic]

|  | Stable in standing water | Removed by 24h aeration | Removed by carbon | Removed by RO |
| --- | --- | --- | --- | --- |
| **Chlorine** | No | Yes | Yes | Yes |
| **Chloramine** | Yes | No | Catalytic carbon only | Yes |

*Chlorine off-gasses overnight. Chloramine is stable and needs a catalytic carbon filter or RO.*

Hardness is the one part of your starting water that is genuinely useful. It is dissolved calcium and magnesium, and cannabis needs both[^kpai-2024-mineral-nutrition-vegetative-cannabis]. The catch: in hard water those minerals usually ride along with high alkalinity, so the helpful Ca and Mg arrive locked up with the carbonates that cause pH problems. Soft water at under 1 GPG (about 17 ppm) can be low in Ca and Mg and need a CalMag supplement regardless of whether you run RO.

| Class | Hardness | Cannabis-relevant note |
| --- | --- | --- |
| Soft | <1 GPG / <17 mg/L | May be low in Ca/Mg, add CalMag |
| Slightly hard | 1-3.5 GPG | Usually fine, check alkalinity |
| Moderately hard | 3.5-7 GPG | Watch alkalinity creeping up |
| Hard | 7-10.5 GPG | Ca/Mg useful but alkalinity likely high |
| Very hard | >10.5 GPG / >180 mg/L | Expect lockout and pH problems, consider RO |

*Hardness classes. Helpful minerals at the soft end, pH trouble at the hard end.*

## Why growers use RO, build back, and when you actually need it

Reverse osmosis strips water to near-zero PPM, typically 0-10 ppm TDS, giving a blank canvas so every mineral the plant gets is one you chose[^umass-water-quality-ph-alkalinity]. Because RO removes calcium and magnesium too, you must build back. That usually means adding a CalMag supplement plus your base nutrients to reach a target of roughly 100-200 ppm with good Ca and Mg before the rest of the feed[^kpai-2024-mineral-nutrition-vegetative-cannabis].

> **Diagram.** RO gives you a clean slate, but a clean slate is not a feed. Build back CalMag first, then base nutrients, so the plant gets the minerals it needs and a working buffer.[^kpai-2024-mineral-nutrition-vegetative-cannabis]

> **Diagram.** A simple decision path. RO is recommended when alkalinity is high, sodium is elevated, chloramine is present, or starting EC is high. Otherwise clean tap is usually fine.[^umass-water-quality-ph-alkalinity]

> **KEY — When RO is worth it, and when it is not**
>
> - **Worth it when:** starting EC is high, sodium is elevated, alkalinity is high, or chloramine is present.
> - **Often skippable when:** tap is soft, low-alkalinity, chlorine-only (off-gassable), and under about 150 ppm.
> - **The cost:** a wastewater ratio of often 1-4 gallons wasted per gallon made, membrane replacement, and a slower fill rate.

## Testing your source water, step by step

Before buying any equipment, get real numbers for your water. A cheap EC/PPM pen and pH pen tell you starting strength and acidity in seconds, but they will not reveal alkalinity, sodium, or specific minerals. For that, send a sample to a lab or read your municipal water report, which lists EC/TDS, pH, alkalinity, calcium, magnesium, sodium, chloride, and any chlorine or chloramine note.

> **Diagram.** The parameters worth pulling off a lab test or city report. EC and pH are quick pen readings, but alkalinity, sodium and the individual minerals only come from a fuller test.

1. **Buy and calibrate pens** — Get an EC/PPM pen and a pH pen first. Calibrate with fresh calibration solution, never with tap water.
2. **Get the full picture** — For alkalinity, sodium, Ca, Mg and micronutrients, use a lab test or your city's annual water-quality report.
3. **Record starting EC** — Note how much room you have before the ~your total EC budget (set targets in mS/cm) feed ceiling, so you know your nutrient headroom.
4. **Mix in the right order** — Fill water, let chlorine off-gas or filter it, add CalMag if RO or soft, add base nutrients, then adjust pH last.
5. **Re-test seasonally** — Re-check well and rain sources through the year. Municipal supplies can also switch chlorine to chloramine periodically.

> **Diagram.** Order matters because each addition shifts pH. Adjust pH last, once the full recipe is mixed, then verify both EC and pH before you feed.[^bevan-2021-npk-flowering-cannabis]

## Water temperature and the mistakes beginners make

Water temperature quietly controls dissolved oxygen and disease risk. Aim for roughly 18-22 C (65-72 F), because warm, poorly aerated water raises pathogen risk even though saturation DO is still roughly ~9 mg/L at 20 C and ~8 mg/L at 26 C. Target at 26 C[^fao-dissolved-oxygen-temperature], and root pathogens like Pythium accelerate above about 23 C[^sutton-2006-pythium-hydroponic-etiology]. Warm water plus low oxygen is an open invitation to root rot.

> **Diagram.** Saturation dissolved oxygen declines gently as water warms (roughly ~9 mg/L near 20 C toward ~8 mg/L saturation at 26 C. Above roughly 23 C you also enter Pythium risk.[^fao-dissolved-oxygen-temperature][^sutton-2006-pythium-hydroponic-etiology]

| Common mistake | What actually happens, and the fix |
| --- | --- |
| Comparing PPM across meters | A 500 vs 700 scale makes two pens disagree on the same water. Pick one scale and stick to it |
| pH the tank, ignore alkalinity | Root-zone pH creeps up within days. Correct the alkalinity, not just the one reading |
| Feeding plain RO or rain | Calcium and magnesium deficiency. Add CalMag before base nutrients |
| Leaving chloramine to sit out | Chloramine is stable and survives the night. Use catalytic carbon or RO |
| Water too warm | Low oxygen and root rot. Cool the reservoir to 18-22 C |

*The five beginner traps, and what to do instead.*

## What good water gets you, and what it doesn't

Sorting out your water removes a whole category of mystery problems: stable pH, no chlorine damage, predictable feed strength. It will not fix bad genetics, poor light, or a broken nutrient schedule. Good water quality is a foundation, not a yield button. It prevents problems more than it boosts numbers.

> **Diagram.** A plain-language verdict. Soft low-alkalinity tap usually needs no RO. Hard, high-sodium, high-alkalinity, or chloraminated water is where RO earns its cost.

> **KEY — The honest summary**
>
> 1. **Most home growers on clean, soft, low-alkalinity tap** can succeed with simple dechlorination and pH control, and never need RO.
> 2. **RO matters most** for very hard, high-sodium, or high-alkalinity sources, for chloramine, and for precision hydro.
> 3. **You still manage pH, EC, temperature and CalMag** regardless of which water source you choose.

Spend on a water test first, and let the numbers, not marketing, decide whether RO is worth it. Then take your clean starting water into the [pH management](ph-management.html) and [nutrient mixing](nutrient-mixing-athena.html) papers to build the rest of the feed.

## References

[^bevan-2021-npk-flowering-cannabis]: Bevan, L., Jones, M., & Zheng, Y. (2021). Optimisation of Nitrogen, Phosphorus, and Potassium for Soilless Production of Cannabis sativa in the Flowering Stage Using Response Surface Analysis. Frontiers in Plant Science, 12, 764103. https://doi.org/10.3389/fpls.2021.764103 (peer-reviewed)
[^kpai-2024-mineral-nutrition-vegetative-cannabis]: Kpai, P., et al. (2024). Mineral nutrition for Cannabis sativa in the vegetative stage using response surface analysis. Frontiers in Plant Science, 15, 1501484. https://doi.org/10.3389/fpls.2024.1501484 (peer-reviewed)
[^umass-water-quality-ph-alkalinity]: University of Massachusetts Amherst, Center for Agriculture, Food, and the Environment (Greenhouse & Floriculture Program). Water quality: pH and alkalinity (fact sheet). UMass Extension. https://www.umass.edu/agriculture-food-environment/greenhouse-floriculture/fact-sheets/water-quality-ph-alkalinity (industry/manufacturer source)
[^fisher-purdue-ho242-alkalinity-soilless]: Fisher, P., et al. (Purdue University Extension). HO-242-W: Alkalinity Management in Soilless Substrates. Purdue Extension. https://www.extension.purdue.edu/extmedia/ho/ho-242-w.pdf (industry/manufacturer source)
[^ferrarezi-2023-chlorine-phytotoxicity-rex-lettuce]: Ferrarezi, R. S., et al. (2023). Irrigation Sources with Chlorine Drinking Water Standard Limits Cause Phytotoxicity on 'Rex' Lettuce Grown in Hydroponic Systems. HortTechnology, 33(1), 125-130. https://doi.org/10.21273/HORTTECH05091-22 (peer-reviewed)
[^date-2005-chloramines-lettuce-hydroponic]: Date, S., Terabayashi, S., Kobayashi, Y., & Fujime, Y. (2005). Effects of chloramines concentration in nutrient solution and exposure time on plant growth in hydroponically cultured lettuce. Scientia Horticulturae, 103(3), 257-265. https://doi.org/10.1016/j.scienta.2004.06.005 (peer-reviewed)
[^sutton-2006-pythium-hydroponic-etiology]: Sutton, J. C., Sopher, C. R., Owen-Going, T. N., Liu, W., Grodzinski, B., Hall, J. C., & Benchimol, R. L. (2006). Etiology and epidemiology of Pythium root rot in hydroponic crops: current knowledge and perspectives. Summa Phytopathologica, 32(4), 307-321. https://doi.org/10.1590/S0100-54052006000400001 (peer-reviewed)
[^fao-dissolved-oxygen-temperature]: FAO. Dissolved Oxygen (Section 4). In: Water Quality for Aquaculture / Inland Water Resources and Aquaculture Service. Food and Agriculture Organization of the United Nations. https://www.fao.org/4/ac183e/ac183e04.htm (industry/manufacturer source)
