---
slug: "scaling-high-light"
title: "Scaling light to the limiting factor"
eyebrow: "Advanced · Scaling to high light"
summary: "Light sets the demand. CO₂, water, airflow, feed and heat-removal have to supply it. Your yield ceiling is whichever one tops out first — so size every system to the light, find the wall, and dial the light down to meet it."
track: "Environment & climate"
read_time: "~16 min read"
diagrams: "1 diagram · 5 tables"
related: ["grow-room-systems", "co2-enrichment", "coco-crop-steering"]
url: "https://jaketherabbit.github.io/cannabis-white-papers/scaling-high-light.html"
md_url: "https://jaketherabbit.github.io/cannabis-white-papers/papers/scaling-high-light.md"
version: "1.2"
updated: "2026-07-18"
license: "CC BY-NC 4.0"
license_url: "https://creativecommons.org/licenses/by-nc/4.0/"
attribution: "The Cannabis White Papers"
refs: [{"id": "rm2021-light", "n": 1, "cite": "Rodriguez-Morrison V, Llewellyn D, Zheng Y (2021). Cannabis yield, potency, and leaf photosynthesis respond differently to increasing light levels in an indoor environment. Front. Plant Sci. 12:646020.", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8144505/", "peer": true}, {"id": "chandra2008-photo", "n": 2, "cite": "Chandra S, Lata H, Khan IA, ElSohly MA (2008). Photosynthetic response of Cannabis sativa L. to variations in photosynthetic photon flux densities, temperature and CO2 conditions. Physiol. Mol. Biol. Plants 14(4):299-306.", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3550641/", "peer": true}, {"id": "faust2018-dli", "n": 3, "cite": "Faust JE, Logan J (2018). Daily light integral: a research review and high-resolution maps of the United States. HortScience 53(9):1250-1257.", "url": "https://doi.org/10.21273/HORTSCI13144-18", "peer": true}, {"id": "collado2025-light", "n": 4, "cite": "Collado CE, Hernandez R (2025). Vegetative and reproductive stage lighting interactions on flower yield, water-use efficiency, terpenes and cannabinoids of Cannabis sativa. Scientific Reports 15:s41598-025-27437-4.", "url": "https://www.nature.com/articles/s41598-025-27437-4", "peer": true}]
---

# Scaling light to the limiting factor

_Advanced · Scaling to high light · ~16 min read_

> Light sets the demand. CO₂, water, airflow, feed and heat-removal have to supply it. Your yield ceiling is whichever one tops out first — so size every system to the light, find the wall, and dial the light down to meet it.

## Light is the throttle, not the engine

Photosynthesis runs at the speed of whatever is in shortest supply. Light can be the thing that sets the pace — but only up to the point where something else runs out. Past that point, more light does nothing except make heat and stress the plant.

This is an old rule with two names. Liebig's **law of the minimum** says a crop grows at the rate set by its scarcest resource, no matter how abundant everything else is. Blackman's **law of limiting factors** says the same about the moment-to-moment rate of photosynthesis: raise the input that is currently limiting and the rate climbs; raise anything else and nothing happens. Cannabis yield keeps rising with light to very high levels[^rm2021-light], but only because CO₂, warmth, water and feed rise with it[^chandra2008-photo]. A room at 1500 µmol on ambient CO₂ is really a room running at its 800 µmol ceiling, with 700 µmol of wasted, heat-making light on top.

So the job is not ‘turn the lights up.’ The job is to work out **which system tops out first**, and then either raise that ceiling or set the light to it. The companion paper [Grow-room systems](grow-room-systems.html) makes the case that the room is one machine; this paper puts numbers on it and shows you how to find the machine's weakest link.

> **KEY — The whole paper in one line**
>
> Light is a demand you create. CO₂, water, feed, airflow and heat-removal are the supply. Yield tracks light _only while every supply line keeps up_ — the first one that can't is your real ceiling.

## The words you need

Six terms carry the rest of the guide. If these are already second nature, skip to the ladder.

**PPFD** — The intensity of usable light landing on the canopy, in µmol/m²/s. This is the dial you are trying to turn up. Think ‘brightness right now.’

**DLI** — Daily light integral — the total light delivered over a day, in mol/m²/day. At a 12/12 flip, DLI = PPFD × 0.0432[^faust2018-dli]. Think ‘the day's total ration.’

**Light saturation** — The PPFD above which a leaf can't use any more light, so the extra just becomes heat. The saturation point _rises_ when you add CO₂ and warmth — which is the whole reason enrichment lets you run brighter[^chandra2008-photo].

**Limiting factor** — The single input in shortest supply relative to demand. It, and only it, sets the growth rate. Every plan in this paper is a hunt for this one thing.

**Sensible vs latent load** — Two kinds of heat your climate gear fights. **Sensible** is dry heat off the fixtures — the air-conditioner's job. **Latent** is heat locked in the water vapour the plants transpire — the dehumidifier's job. Light drives both.

**Mass flow** — Nutrients ride into the roots dissolved in the transpiration stream. Faster transpiration pulls more water — and more feed — through the plant, which is why [airflow](airflow-design.html), feed EC and light are all bolted together.

## The scaling ladder

Here is the whole system on two tables, rung by rung. Pick your light level on the left and read across: everything in that row has to be true at the same time, or the light in that row is a lie. The rungs run from an ambient-CO₂ room (600 µmol) up to a fully-supported sealed room (1500 µmol).

The first table is the **air and gas** side of the row — what the plant breathes and the climate it sits in.

| Light (PPFD) | DLI | CO₂ setpoint | Day air temp | VPD (RH) | Canopy airspeed | Verdict |
| --- | --- | --- | --- | --- | --- | --- |
| 600 | 26 | 400–450 ppm | 25 °C | 1.2 kPa (62%) | 0.3–0.5 m/s | Ambient air is fine |
| 800 | 35 | 600–800 ppm | 26 °C | 1.3 kPa (62%) | 0.4–0.6 m/s | Enrichment starts paying |
| 1000 | 43 | 800–1000 ppm | 27 °C | 1.3 kPa (63%) | 0.5–0.7 m/s | CO₂ now required |
| 1200 | 52 | 1000–1200 ppm | 28 °C | 1.4 kPa (63%) | 0.6–0.8 m/s | Heavy support |
| 1500 | 65 | 1200–1500 ppm | 29–30 °C | 1.4 kPa (65%) | 0.7–1.0 m/s | Everything maxed |
| VPD barely moves — it is a plant-comfort setpoint, not something that scales with light. What scales is the water you add and remove to _hold_ that VPD while transpiration climbs (Table 2). Temp is nudged up because CO₂ and warmth lift the light-saturation point together. |

*Table 1 · Climate & gas targets by light level (flowering, 12/12, per m² of canopy)*

The second table is the **water, feed and heat** side of the same row — what you have to pour in and pull out to sustain it. This is where the cost of high light lives.

| Light (PPFD) | Transpiration (water out) | Irrigation (water in) | Feed EC | Light heat | Sensible cooling | Dehumidification |
| --- | --- | --- | --- | --- | --- | --- |
| 600 | 2.2 L/m²/d | 3.0 L/m²/d | 2.0–2.4 | 222 W/m² | 0.6 ton /10 m² | 4.7 pt/m²/d |
| 800 | 3.0 L/m²/d | 4.0 L/m²/d | 2.4–2.8 | 296 W/m² | 0.8 ton /10 m² | 6.3 pt/m²/d |
| 1000 | 3.7 L/m²/d | 4.9 L/m²/d | 2.8–3.2 | 370 W/m² | 1.1 ton /10 m² | 7.8 pt/m²/d |
| 1200 | 4.4 L/m²/d | 5.9 L/m²/d | 3.2–3.6 | 444 W/m² | 1.3 ton /10 m² | 9.4 pt/m²/d |
| 1500 | 5.6 L/m²/d | 7.4 L/m²/d | 3.6–4.2 | 556 W/m² | 1.6 ton /10 m² | 11.7 pt/m²/d |
| Rules used: transpiration ≈ PPFD × 0.0037 L/m²/d; irrigation = transpiration ÷ 0.75; light heat = PPFD ÷ 2.7; dehu load = transpiration (1 L ≈ 2.1 US pints)[^collado2025-light]. Heavy CO₂ trims transpiration a little at the top. On HPS or 2.0 µmol/J LED, add ~35% to every heat, cooling and airflow figure. |

*Table 2 · Water, feed & heat-removal by light level (per m² of canopy, ~25% runoff, LED @ 2.7 µmol/J)*

Read the two tables together and the shape of the problem jumps out. Going from 600 to 1500 µmol is 2.5× the light — but also 2.5× the transpiration, feed and heat. And because you now raise _both_ feed EC and irrigation volume, the actual nutrient you push through the plant each day climbs roughly **five-fold**, not 2.5-fold. High-light plants are not a bit hungrier. They are dramatically hungrier, wetter and hotter, all at once.

## One room, five light levels

Per-m² numbers are abstract, so put them in a real box. Take a **50 m² flowering canopy** — a 10 m × 5 m room, roughly 35 × 650 W fixtures, about 150 m³ of air. Multiply the ladder through and you get the actual gear list.

| Light (PPFD) | Fixture load | Sensible cooling | Air-handler airflow | Dehumidification | Irrigation | CO₂ to hold |
| --- | --- | --- | --- | --- | --- | --- |
| 600 | 11.1 kW | 3.1 tons | ~1,250 CFM | 235 pt/day (111 L) | 148 L/day | ambient |
| 800 | 14.8 kW | 4.2 tons | ~1,680 CFM | 313 pt/day (148 L) | 197 L/day | ~700 ppm |
| 1000 | 18.5 kW | 5.3 tons | ~2,120 CFM | 391 pt/day (185 L) | 247 L/day | ~1000 ppm |
| 1200 | 22.2 kW | 6.3 tons | ~2,520 CFM | 469 pt/day (222 L) | 296 L/day | ~1200 ppm |
| 1500 | 27.8 kW | 7.9 tons | ~3,160 CFM | 587 pt/day (278 L) | 370 L/day | ~1400 ppm |
| Sensible cooling covers the fixtures only — add the dehumidifier's reject heat and pumps in a sealed room. Air-handler airflow at ~400 CFM/ton is _separate_ from the in-canopy fans that keep 0.5–1.0 m/s moving through the leaves. First CO₂ charge of a sealed 150 m³ room to 1000 ppm is only ~90 L of gas; daily burn depends mostly on how well the room seals. |

*Table 3 · What a 50 m² canopy demands at each light level*

Notice the last two columns between 1000 and 1500 µmol. The fixtures rise 50%, but dehumidification jumps from 391 to 587 pints a day — two grow dehumidifiers to three — and cooling goes from about five tons to eight. **The photons are the cheap part.** The tonnage and the pints are where the money and the failures live, and they are almost always what caps a real room before the lights do.

## EC climbs with light

The feed column deserves its own look, because raising EC with light is the step growers most often skip — and the one that quietly caps yield. The logic is mass flow: brighter light means faster growth, which means the plant pulls more nutrient every day. It gets that nutrient two ways at once, and **both** scale with light — more water moves through the plant (Table 2's transpiration column)[^collado2025-light], and each millilitre of that water carries more salt (higher EC). Under-feed a bright canopy and it fades from the bottom up; the light is there but the raw material isn't.

| Light (PPFD) | Feed EC (mS/cm) | Target runoff EC | Daily feed per m² | Shot strategy | If you get it wrong |
| --- | --- | --- | --- | --- | --- |
| 600 | 2.0–2.4 | 3–4 | ~3.0 L | Fewer, larger shots; wider dryback | Under: slow, pale new growth |
| 800 | 2.4–2.8 | 4–5 | ~4.0 L | Build shot frequency with canopy | Balanced feed shows here |
| 1000 | 2.8–3.2 | 5–6 | ~4.9 L | Multiple shots, tighter window | Under: lower-canopy fade |
| 1200 | 3.2–3.6 | 6–7 | ~5.9 L | Frequent shots, watch runoff EC | Over: tip burn, crispy margins |
| 1500 | 3.6–4.2 | 7–8 | ~7.4 L | High frequency + volume, daily EC checks | Either error bites fast |
| Assumes a clean source (<0.4 EC), a balanced high-ratio nutrient and an inert substrate. Coir buffers cations, so run the lower half of each band. See [Coco & crop steering](coco-crop-steering.html) and [Nutrient deficiencies](nutrient-deficiencies.html). Raise EC as a lever _after_ irrigation volume is right, never instead of it. |

*Table 4 · Feed EC and root-zone strategy by light level (managed substrate, clean source water)*

There is a second reason EC and light move together: EC is also a [steering](one-steering-law.html) lever. A higher root-zone EC raises osmotic pressure and gently reins in water uptake, pushing the plant generative — useful in flower. So at high light you raise EC for two jobs at once: to feed the faster growth, and to hold generative balance against all that extra irrigation. The trap is raising EC to steer while forgetting volume has to rise too; starve the volume and the salts simply concentrate and burn.

## Find your limiting factor

Now the payoff. Every support system can sustain some maximum light level — a PPFD ceiling of its own. Work out the ceiling for each, and **the lowest number is your room's real ceiling.** Everything above it is wasted light. Here is how to turn each piece of installed gear into a PPFD number, per m² of canopy.

| System | What you have | Its PPFD ceiling |
| --- | --- | --- |
| **CO₂** | Your setpoint | Ambient 420 ppm → ~800 µmol · 800 ppm → ~1000 · 1200 ppm → ~1300 · 1500 ppm → ~1500 |
| **Cooling** | Installed sensible tons | PPFD ≤ 9,500 × tons ÷ m² |
| **Dehumidification** | Rated pints/day | PPFD ≤ 128 × pints/day ÷ m² |
| **Irrigation** | Max deliverable L/day | PPFD ≤ 200 × L/day ÷ m² |
| **Feed / EC** | Highest EC you can run | Match the EC to its rung in Table 4 |
| **Airflow** | Canopy air movement | A _gate_, not a dial — see below |
| All at LED 2.7 µmol/J; scale the cooling constant down for less efficient fixtures. Airflow gives no clean number because it is a prerequisite: if you can't hold 0.3–1.0 m/s _through_ the whole canopy, gas exchange stalls and every other ceiling drops to roughly 900–1000 µmol. |

*Table 5 · Turn each system into its PPFD ceiling (per m² of canopy)*

Airflow is the odd one out on purpose. You can have 1500 ppm of CO₂ in the room and still starve the leaf if the [boundary layer](airflow-design.html) — the film of still air on every leaf surface — never gets stripped away. Dead air inside a dense canopy is a CO₂ ceiling you can't see on the room sensor. Treat airflow as a pass/fail gate you clear _before_ reading any other ceiling.

Run the six numbers, take the minimum, and you have found the wall. The diagram makes it concrete for a real room.

> **Diagram.** Four systems, four different ceilings. Cooling could take 1140 and CO₂ could feed 1500, but the dehumidifier tops out at 1050 µmol — the amber line. That is the room's real ceiling. Run the lights at 1300 and the extra 250 µmol just makes humidity the dehu can't remove. Dial to 1050, or buy more dehu.

## Four rooms, four walls

The same method, four common rooms. Each has plenty of everything except one thing — and that one thing is the yield. The fix is never ‘more light.’

> **NOTE — Case A · The dehumidifier is the wall most common**
>
> **The room:** 50 m², 6 tons of cooling, CO₂ to 1500 ppm, good fans, two 205-pint dehumidifiers (410 pints/day). **The math:** cooling ceiling 9,500×6÷50 = **1140**; dehu ceiling 128×410÷50 = **1050**; CO₂ ceiling **1500**. **The wall:** dehumidification, at ~1050 µmol. **The fix:** run the lights at 1050, _or_ add a third dehumidifier to unlock the 1140 the cooling already allows — then cooling becomes the next wall.

> **NOTE — Case B · The ambient-air ceiling cheap to fix**
>
> **The room:** big cooling and dehu, but _no_ CO₂ supplementation — ambient 420 ppm. **The math:** cooling and dehu might support 1200, but at ambient CO₂ the leaf light-saturates around **800** µmol[^chandra2008-photo]. **The wall:** CO₂, at ~800. **The fix:** above 800 the extra light just bleaches tops and adds heat — dial down to 800, or add CO₂ and suddenly all that cooling and dehu headroom means something. The cheapest ceiling in the building to raise.

> **NOTE — Case C · The stagnant canopy hidden**
>
> **The room:** CO₂ to 1200, strong cooling and dehu — but a thick canopy with dead, laminar air in the lower half. **The math:** no clean number; the boundary layer isn't stripped, so CO₂ can't reach the stomata inside the canopy. Effective ceiling collapses to ~**900–1000** even though the room ‘has’ 1200 ppm. **The wall:** airflow gate. **The tell:** lush outer buds, larfy damp interior. **The fix:** [defoliate](defoliation-training.html) and add under-canopy air _before_ touching the lights or the CO₂.

> **NOTE — Case D · The root zone can't keep up self-inflicted**
>
> **The room:** climate and gas all support 1300, but irrigation is a couple of short shots and feed EC is stuck at 2.4. **The math:** the canopy wants 4.5+ L/m²/day and 3.4 EC; it's getting ~3 L and 2.4. Water ceiling 200×(deliverable L)÷m² lands near **900**, and the low EC caps the same rung. **The wall:** irrigation volume + EC. **The tell:** midday wilt and a pale, fading lower canopy. **The fix:** get shot volume and frequency right first, _then_ climb EC up Table 4 — not the other way round.

## Dial the light to the wall

Once you know your lowest ceiling, you have exactly two honest moves.

**Move one: set the light to the wall.** If your ceiling is 1050 µmol, run 1050. The photons above it were never converting to yield — they were converting to heat, humidity and stress. Dialling down to the wall costs nothing in growth and hands back power, cooling headroom and a calmer room. On dimmable fixtures this is free and immediate.

**Move two: raise the wall, then re-check.** Spend on the _limiting_ system and nothing else. Adding CO₂ to a Case-B room is transformative; adding CO₂ to a Case-A room does nothing, because dehu — not CO₂ — is the wall. And the part people miss: **the moment you raise one ceiling, a different system becomes the wall.** Fix the dehu in Case A and cooling caps you at 1140. Chase the ceiling in the wrong order and you buy gear that changes nothing.

> **WARN — Running light above the wall is worse than wasteful**
>
> It isn't neutral. Excess light past your limiting factor bleaches and foxtails tops, drives leaf temp and VPD up, and — when the dehu is the wall — pushes humidity into [bud-rot](mould-risk.html) territory. You pay for the extra electricity _and_ lose quality. The dial-down is the rare free lunch.

There is also an economic ceiling below the biological one. Yield keeps climbing toward 1500–1800 µmol[^rm2021-light], but the tons and pints needed to support the top rungs climb faster than the yield does. The last 300 µmol might cost a third dehumidifier and a bigger AC to buy a single-digit-percent bump. Find your _economic_ wall — where the next 100 µmol stops paying for its own climate gear — and it often sits a rung below what the plants could theoretically use.

## Troubleshooting

Every row here is a limiting factor showing itself. The symptom tells you which wall you hit.

| Symptom | Which wall you hit | What to do |
| --- | --- | --- |
| Bleached, foxtailed tops under big light | Light above your CO₂ ceiling; tops light-saturated | Add CO₂, or dial light to the ambient ceiling (~800) |
| RH won't come down; VPD collapses midday | Transpiration outran dehumidification | Add dehu capacity or trim light — usually the real ceiling |
| Big light, flat yield | CO₂, water or feed didn't scale with the light | Find the lowest ceiling; raise it or dial light to it |
| Midday wilt at peak light | Irrigation volume < transpiration | Bigger/more shots; fix volume before touching EC |
| Pale, fading lower canopy late in flower | Feed EC too low for the light level | Step EC up Table 4; check runoff EC |
| Tip burn, crispy leaf margins | Feed EC too high for the light (above the rung) | Drop EC a step, or raise light/volume to match |
| Lush outside, larfy damp interior | Airflow gate — boundary layer not stripped inside | Defoliate + under-canopy air; CO₂ can't work in dead air |

## Realistic expectations

Cannabis yield really does track light almost linearly, up to roughly 1500–1800 µmol[^rm2021-light] — but that finding comes with fine print those studies never hide: it holds _only_ when CO₂, temperature, water and feed are all lifted to match. Strip the support away and the same lights give you bleached tops and a heat problem. The linear curve is a promise conditional on the whole convoy keeping up.

So spend your attention where the wall is, not where the catalogue is. The most common real ceilings, in rough order, are dehumidification, then cooling, then CO₂, then root-zone delivery — and the cheapest yield you will ever buy is usually removing your current limiting factor, not adding another kilowatt of light. Measure the things that reveal the wall: leaf temperature, runoff EC, canopy-level RH and airspeed, room CO₂ under the canopy. A gauge at the room's edge won't show you the dead, humid air where the plant actually lives.

> **KEY — What to remember**
>
> 1. Light is a demand. **Size CO₂, water, feed, airflow and heat-removal to supply it** (Tables 1–2).
> 2. Turn each installed system into a **PPFD ceiling**; the **lowest wins** (Table 5).
> 3. **Set the light to that wall** — running above it wastes power and costs quality.
> 4. To go higher, **raise the limiting system, then re-check** — the wall moves.

This paper is one lever of the room. Read it alongside [Grow-room systems](grow-room-systems.html), [CO₂ enrichment](co2-enrichment.html) and [Airflow design](airflow-design.html).

## References

[^rm2021-light]: Rodriguez-Morrison V, Llewellyn D, Zheng Y (2021). Cannabis yield, potency, and leaf photosynthesis respond differently to increasing light levels in an indoor environment. Front. Plant Sci. 12:646020. https://pmc.ncbi.nlm.nih.gov/articles/PMC8144505/ (peer-reviewed)
[^chandra2008-photo]: Chandra S, Lata H, Khan IA, ElSohly MA (2008). Photosynthetic response of Cannabis sativa L. to variations in photosynthetic photon flux densities, temperature and CO2 conditions. Physiol. Mol. Biol. Plants 14(4):299-306. https://pmc.ncbi.nlm.nih.gov/articles/PMC3550641/ (peer-reviewed)
[^faust2018-dli]: Faust JE, Logan J (2018). Daily light integral: a research review and high-resolution maps of the United States. HortScience 53(9):1250-1257. https://doi.org/10.21273/HORTSCI13144-18 (peer-reviewed)
[^collado2025-light]: Collado CE, Hernandez R (2025). Vegetative and reproductive stage lighting interactions on flower yield, water-use efficiency, terpenes and cannabinoids of Cannabis sativa. Scientific Reports 15:s41598-025-27437-4. https://www.nature.com/articles/s41598-025-27437-4 (peer-reviewed)
