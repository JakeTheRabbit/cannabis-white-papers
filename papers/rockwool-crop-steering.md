---
slug: "rockwool-crop-steering"
title: "Crop steering in rockwool: drybacks, saturation and the breaking point"
eyebrow: "Feed · Rockwool steering"
summary: "Rockwool is the most controllable substrate there is, and the least forgiving. This is the guide to what water content really means, how to read and calculate dryback, how dry a block can get before it is gone, and how to hold the right saturation from clone to chop without ever hand-flushing or topping up a cube."
track: "Flowering"
read_time: "~18 min read"
diagrams: "7 diagrams"
related: ["coco-crop-steering", "root-zone-teros12", "f2-crop-steering", "irrigation-manual"]
url: "https://jaketherabbit.github.io/cannabis-white-papers/rockwool-crop-steering.html"
md_url: "https://jaketherabbit.github.io/cannabis-white-papers/papers/rockwool-crop-steering.md"
version: "1.2"
updated: "2026-07-18"
license: "CC BY-NC 4.0"
license_url: "https://creativecommons.org/licenses/by-nc/4.0/"
attribution: "The Cannabis White Papers"
refs: [{"id": "grodan-irrigation-medicinal", "n": 1, "cite": "Grodan (ROCKWOOL Group). Grodan research reveals new insights into optimal irrigation strategy for large-scale production of medicinal crops. Whitepaper, with B. Nikaj; trials in partnership with Wageningen University & Research, 2020-2022.", "url": "https://www.grodan.com/", "peer": false}, {"id": "owen-norden-preferential-flow-2024", "n": 2, "cite": "Owen, J., & Norden, D. (Profile Products). Understanding drainage in horticultural growing media. Greenhouse Management.", "url": "https://www.greenhousemag.com/article/growing-media-defining-drainage-improve-substrate/", "peer": false}, {"id": "hydrus-soilless-substrate-dynamics", "n": 3, "cite": "International Society for Horticultural Science (ISHS). Utilizing the HYDRUS model as a tool for understanding soilless substrate water dynamics. Acta Horticulturae 1168.", "url": "https://www.ishs.org/ishs-article/1168_41", "peer": true}, {"id": "moon-rootzone-ec-2018", "n": 4, "cite": "Moon T, Ahn TI, Son JE. Forecasting Root-Zone Electrical Conductivity of Nutrient Solutions in Closed-Loop Soilless Cultures via a Recurrent Neural Network Using Environmental and Cultivation Information. Frontiers in Plant Science. 2018;9:859.", "url": "https://doi.org/10.3389/fpls.2018.00859", "peer": true}, {"id": "nemali-2006-set-point-irrigation", "n": 5, "cite": "Nemali, K. S. & van Iersel, M. W. (2006). An automated system for controlling drought stress and irrigation in potted plants. Scientia Horticulturae, 110(3), 292-297.", "url": "https://doi.org/10.1016/j.scienta.2006.07.009", "peer": true}, {"id": "tavan-2021-sensor-irrigation-soilless", "n": 6, "cite": "Tavan, M., Wee, B., Brodie, G., Fuentes, S., Pang, A., & Gupta, D. (2021). Optimizing Sensor-Based Irrigation Management in a Soilless Vertical Farm for Growing Microgreens. Frontiers in Sustainable Food Systems, 4, 622720.", "url": "https://doi.org/10.3389/fsufs.2020.622720", "peer": true}, {"id": "caplan2019-drought", "n": 7, "cite": "Caplan D, Dixon M, Zheng Y (2019). Increasing inflorescence dry weight and cannabinoid content in medical cannabis using controlled drought stress. HortScience 54(5):964-969.", "url": "https://doi.org/10.21273/HORTSCI13510-18", "peer": true}, {"id": "malik2025-media", "n": 8, "cite": "Malik M, Tlustoš P (2025). Soilless growing media for cannabis cultivation. Agriculture 15(18):1955.", "url": "https://www.mdpi.com/2077-0472/15/18/1955", "peer": true}, {"id": "netafim-irrigation-maintenance", "n": 9, "cite": "Netafim. Complete Irrigation Maintenance Guide (driplines, flushing, filtration and system upkeep).", "url": "https://www.netafim.com/", "peer": false}, {"id": "athena-spacing-irrigation", "n": 10, "cite": "Athena Agriculture. Plant Spacing & Irrigation (metric), document A01.001 (pot, rockwool and pressure-compensating dripper selection).", "url": "https://athenaag.com/", "peer": false}]
---

# Crop steering in rockwool: drybacks, saturation and the breaking point

_Feed · Rockwool steering · ~18 min read_

> Rockwool is the most controllable substrate there is, and the least forgiving. This is the guide to what water content really means, how to read and calculate dryback, how dry a block can get before it is gone, and how to hold the right saturation from clone to chop without ever hand-flushing or topping up a cube.

## Why rockwool rewards and punishes you

Rockwool (stone wool) is spun rock fibre. It holds no nutrients of its own and reacts with nothing you feed it, so **100% of what you put in goes straight to the plant**[^grodan-irrigation-medicinal]. That makes it the most precise substrate you can steer with. It also means the block has no buffer: get the water wrong and the plant feels it the same hour.

This guide is only about the water and salt in the block, the part most growers run on feel. By the end you will know exactly what a water-content percentage is, how to calculate a dryback, the minimum you must feed, the point past which a dried-out block cannot be saved by the dripper, and how to hold the slab in the right zone for the whole grow using sensors and an irrigation controller, never a hose.

> **KEY — The one-paragraph version**
>
> Saturate the block, then let it lose a controlled amount of water each day (the **dryback**). The size and timing of that dryback is your main steering lever. Feed enough each day to refresh the salts and get a little runoff, but never let the block fall below its recovery floor (around **25-30% water content**), because below that it channels and will not rewet from a dripper[^owen-norden-preferential-flow-2024].

> **NOTE — Written for your kit**
>
> Assumes a slab-and-cube setup on pressure-compensating drippers, with a substrate moisture and EC sensor and an irrigation controller, the Athena-style 4″ cube on a 3×6×36 slab being typical[^athena-spacing-irrigation]. The smaller the dripper, the finer your control of the root zone[^athena-spacing-irrigation].

## The words you need

**Water content (WC%)** — The share of the block's volume that is water right now, as a percentage. A slab at 70% WC is 70% full of water by volume. This single number is what you steer.

**Saturation / field capacity** — Saturation is the block as full as it can get just after irrigating. Field capacity is what it settles back to once free water has drained out. Your daily peak sits around field capacity.

**Dryback** — The drop in water content between the daily peak and the next low, caused by the plant drinking and by evaporation. Measured in percentage points of WC.

**Dryback %** — The size of that drop. Can be stated as _points_ (peak 75% to trough 55% = a 20-point dryback) or as a _fraction of the peak_. This guide uses points unless it says otherwise.

**Runoff (drain / leachate)** — The feed that exits the bottom of the block. A small daily runoff flushes built-up salt and tells you the EC inside the block.

**Substrate EC** — The salt strength of the water _inside_ the block. This, not the dripper or drain EC, is what the plant actually experiences[^grodan-irrigation-medicinal] and what you steer to[^moon-rootzone-ec-2018].

**Recovery floor** — The lowest water content a block can reach and still rewet evenly from the dripper. Below it the fibre channels and the core stays dry.

**Channeling / preferential flow** — When water runs down a few open paths instead of spreading through the fibre, so it exits as runoff while the core stays dry[^owen-norden-preferential-flow-2024].

**Generative vs vegetative steering** — Drier, bigger drybacks push the plant generative (toward flower and fruit). Wetter, smaller drybacks keep it vegetative (leafy growth)[^caplan2019-drought].

**Shot** — A single timed irrigation pulse. Shot size and spacing build the daily water-content curve.

## Where the water actually sits

A rockwool block is mostly air. Around 95% of its volume is space between the fibres; the fibre itself is a tiny fraction[^malik2025-media]. Water clings to the fibres as a film and fills the smaller gaps, while the larger gaps stay full of air. Water content is simply how much of that space is water versus air at any moment.

> **Diagram.** Water held as a film on the fibres is your WC%. The air between fibres is root oxygen. Because the fibre carries almost no electrical charge (its cation-exchange capacity is near zero), dissolved salts stay in the water and nothing is held back from the plant[^grodan-irrigation-medicinal].

Two consequences fall straight out of this. First, when water leaves the block the salt does not, so the EC of the water left behind climbs as the block dries. Second, because the medium buffers nothing, the EC and water content you set are the EC and water content the roots get, which is why rockwool can be steered so precisely and why mistakes show up so fast.

## What a water-content percentage means

Everything in rockwool steering is a position on one vertical scale: how full the block is. Learn the band and where the danger is, and the rest is timing.

> **Diagram.** The working band runs roughly 55-92% WC. Vegetative and bulking phases sit high; generative pushes ride lower. The dashed line near 30% is the recovery floor, fall below it and the block channels.

> **NOTE — These are starting numbers, not laws**
>
> Grodan is explicit that medicinal cultivars are highly variable, so there is no single correct water content[^grodan-irrigation-medicinal]. Treat every figure here as a starting point you confirm against your own slabs and sensor.

Note where the headroom is. The block can sit happily anywhere from field capacity down into the mid-40s. The cliff is only at the bottom. That asymmetry is the whole reason a controlled dryback is safe but an uncontrolled one is fatal.

## Dryback: what it is, and how to calculate it

A dryback is the block losing water between its daily high and its next low. You create the high by irrigating to field capacity; the plant and evaporation create the low. The _size_ of that swing and _when_ you let it happen is the single biggest lever you have over how the plant grows.

> **Diagram.** One daily cycle. The trough never approaches the floor, the peak refreshes the block. The gap between peak and trough is the dryback.

> **KEY — How to calculate a dryback**
>
> Dryback in points = **peak WC − trough WC**. If the slab peaks at 78% and drops to 58% before the next irrigation, that is a **20-point dryback**. As a fraction of the peak it is 20 ÷ 78 = **26%**. Either way, your sensor gives you both numbers directly, read the high after the last shot and the low just before the next.

| Phase | Typical daily dryback | What it steers |
| --- | --- | --- |
| Propagation / early veg | 5-10 points | Roots chase water, gentle |
| Late veg / bulk (wet) | 10-15 points | Maximum growth, vegetative |
| Generative flower push | 20-30 points | Stacks flower, slows stretch |
| Overnight (any phase) | add 5-15 points | Re-oxygenates the root zone |

*Dryback sizes as a starting framework. Bigger and earlier is more generative; smaller and later is more vegetative.*

> **NOTE — Why the night dryback matters**
>
> As the block dries overnight, air refills the gaps and the roots and beneficial microbes get oxygen. Grodan's trials found that easing the standard night dryback by about 10% (a slightly wetter night) lifted yield in medicinal crops, because the root zone keeps working even while the canopy rests[^grodan-irrigation-medicinal]. Some night dryback is essential; too much is not.

## What happens to a block as it dries

A dryback is good up to a point and dangerous past it. The same process, water leaving the block, does four different things in sequence as it goes too far.

> **Diagram.** Stages 1-2 are the healthy dryback you want: water leaves, air and oxygen enter. Stage 3 is too far: with less water but the same salt, the EC inside the block climbs and the plant feels osmotic stress[^hydrus-soilless-substrate-dynamics]. Stage 4 is past the floor: a dry core forms and water channels around it.

The middle stage is the one that catches people out. Because rockwool holds no salt of its own, the salt that was dissolved in the water stays put while the water disappears. A block drying from 75% to 45% WC keeps only about three-fifths of its water (45 ÷ 75), so the salt left behind concentrates by the inverse, roughly two-thirds higher, because EC rises as 1 divided by the fraction of water remaining[^hydrus-soilless-substrate-dynamics]. A 3.0 EC feed can climb past 5.0 EC in the root zone by late afternoon. That is why big drybacks must be paired with enough volume and runoff to keep the salt in check, covered below.

> **WARN — Dryback stress is partly salt stress**
>
> When you push a generative dryback, you are not only making the plant work for water, you are also concentrating its food. Watch substrate EC, not just water content. If EC climbs faster than you intend on the dryback, shrink the dryback or lower the feed EC.

## The breaking point: when a block is gone

There is a water content below which a rockwool block will not rewet from the dripper no matter how long you run it. This is the single most important thing in this guide, because it is invisible until it has already happened.

> **Diagram.** A block still in the working band rewets evenly: water spreads through the moist fibre. A block taken too dry develops a dry core that the fibre can no longer pull water into. New water finds the few open channels, runs straight down them and exits as runoff while the core stays bone dry[^owen-norden-preferential-flow-2024].

Below roughly **25-30% WC** the dry fibre stops wicking and preferential flow takes over[^owen-norden-preferential-flow-2024][^hydrus-soilless-substrate-dynamics]. The drip rate that kept a healthy block topped up cannot re-saturate a dry one, because the water never contacts the dry interior. Your runoff reads high and your sensor barely moves, the classic signature of a channeling block.

> **DANGER — If a block has gone too dry**
>
> - Stop trusting the dripper to fix it. More drip just makes more runoff.
> - Rehydrate by hand or by flooding: a long, slow, low-volume soak (or sitting the block in shallow feed) until the core takes water back, sometimes over hours.
> - Then return to a normal schedule and find out why it dried out: a clogged dripper, a missed P1 ramp, a dead controller, or a dryback set too deep.
> - A block that has been to the floor repeatedly develops permanent dry pockets and uneven wetting. Replace it rather than fight it.

> **KEY — The rule that prevents all of this**
>
> Set a hard minimum water content in your controller and never let the trough cross it. The dryback is steering; the floor is a safety limit. They are not the same number and you should know both for every slab.

## The minimum you must feed

Feeding rockwool is a balance of two jobs: put back the water the plant drank, and flush enough fresh feed through to stop salt stacking. Underfeed and EC climbs and the block trends toward the floor; overfeed and you drown the roots and lose your dryback.

1. **Size each shot to a few points of WC** — A single shot should lift water content by roughly 2-5 points. Big enough to register on the sensor, small enough not to blow straight to runoff.
2. **Reach field capacity in the P1 ramp** — Stack several shots after lights-on to climb from the overnight low back up to field capacity, then hold it.
3. **Get a small daily runoff** — Aim for around 10-20% runoff once the block is at field capacity. That runoff is how you flush stacked salt and how you read substrate EC[^grodan-irrigation-medicinal].
4. **Use runoff EC as the feedback** — If substrate or runoff EC is climbing day over day, you are not flushing enough, increase shot size or frequency. If EC is falling below target, cut runoff back.
5. **Never let the trough hit the floor** — Whatever the dryback, the pre-irrigation low must stay above the recovery floor with margin.

> **Diagram.** Runoff is not waste, it is your salt-management and measurement tool. Size the daily feed so a controlled fraction drains.

> **NOTE — Minimum feed is a floor, not a target**
>
> The minimum is whatever volume keeps the block above its recovery floor and substrate EC on target. In heavy flower under high light that can be a lot of small shots; in propagation it is very little. Let the sensor and the runoff EC set the number, not a fixed clock[^nemali-2006-set-point-irrigation].

## Generative vs vegetative, in rockwool

You steer the plant by choosing where the block sits in the band, how big the daily dryback is, and when you let it happen. Drier and bigger and earlier is generative; wetter and smaller and later is vegetative[^caplan2019-drought].

| Lever | Vegetative (leafy growth) | Generative (flower / fruit) |
| --- | --- | --- |
| Daily peak WC | High, near field capacity | Lower, mid-band |
| Dryback size | Small, 5-15 points | Large, 20-30 points |
| First shot after lights-on | Early, short ramp | Delayed, longer overnight dryback |
| Substrate EC | Lower end of target | Higher, concentrated by the dryback |
| When to use | Early flower, bulking, recovery | Stretch control, flower set, ripening |

*The same three controls (peak, dryback, timing) produce both behaviours. You are not changing the feed, you are changing the water curve.*

> **NOTE — Feed generously through the front half of flower**
>
> Grodan's trials found a consistently wetter daytime strategy produced higher yield with the same cannabinoid levels, especially across the first six of eight flowering weeks[^grodan-irrigation-medicinal]. Steer generative with timing and dryback, but do not starve the plant of water and feed while it is still building the crop.

## Holding saturation the whole grow, no hand-flushing

The goal is to never touch a hose: the controller holds the block in the right zone from clone to chop, flushing salt with daily runoff so you never have to manually leach or top up a dry cube. The strategy is a planned arc of water content and dryback across the grow.

> **Diagram.** An indicative dryback arc. Stay wet and gentle early to build the plant, push drier and more generative once flower is established, then steady it for ripening[^grodan-irrigation-medicinal].

| Stage | Daily peak WC | Dryback | Substrate EC | Runoff |
| --- | --- | --- | --- | --- |
| Clone / prop | High, gentle | 5-10 pts | Start higher than you'd think | Minimal |
| Veg | High | 10-15 pts | Step up | Low, 5-10% |
| Flower wk 1-3 | High (wet, bulking) | 10-18 pts | Step up again | 10-15% |
| Flower wk 4-6 | Mid | 20-30 pts | Highest | 15-20% to flush |
| Flower wk 7-8 | Mid, steady | 18-25 pts | Ease / as planned | Maintain |

*A complete arc. EC climbs by stage because rockwool is inert and the plant's appetite rises with light[^grodan-irrigation-medicinal]. Runoff rises to flush the higher salt load.*

> **KEY — Why this removes hand-flushing**
>
> A daily controlled runoff continuously replaces the salty water in the block with fresh feed, so EC never stacks to the point of needing a manual leach. And because the trough never crosses the recovery floor, no cube ever dries out enough to need a manual soak. The system holds the equilibrium for you, every day, if you set the limits correctly.

## Running it on sensors and a controller

None of this works on a timer alone. Steering rockwool means measuring the block and letting the controller act on the measurement, closing the loop[^nemali-2006-set-point-irrigation][^tavan-2021-sensor-irrigation-soilless].

- **Measure inside the block.** A substrate sensor reads water content and EC where the roots are. Steer to substrate EC, not dripper or drain EC[^grodan-irrigation-medicinal][^moon-rootzone-ec-2018].
- **Let the controller hold the curve.** The irrigation controller runs the P1 ramp to field capacity, the P2 maintenance shots, and the P0/P3 dryback windows automatically, to water-content set-points rather than fixed times[^nemali-2006-set-point-irrigation].
- **Set the safety floor in software.** A hard minimum water content the controller will always irrigate to defend, so the block can never reach the channeling point even if a dryback is set too deep.
- **Watch the runoff EC daily.** It is your early warning that salt is stacking or that you are over-flushing.

The companion papers cover the hardware and the daily cycle in depth: what the substrate sensor actually sees, how the watering brain decides, the P0-P3 cycle itself, and how to install and run the system.

> **NOTE — The point of precision**
>
> Because rockwool buffers nothing, a closed-loop controller can steer it to a tighter tolerance than any buffered medium[^grodan-irrigation-medicinal]. The inertness that makes it unforgiving is exactly what makes it the best substrate to automate.

## Reading the block's symptoms

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| Runoff high, sensor barely moves | Block channeling, core too dry | Hand-soak to rewet, then raise the floor and check drippers |
| Substrate EC climbing day over day | Not enough runoff, salt stacking | Bigger or more frequent shots to lift daily runoff |
| Substrate EC falling below target | Over-flushing, too much runoff | Cut shot size or frequency |
| WC won't reach field capacity | Shots too small, clogged dripper, or P1 too short | Check drippers, lengthen the P1 ramp[^netafim-irrigation-maintenance] |
| Dryback far bigger than set | Plant drinking hard under high light, or a missed shot | Add P2 shots; verify controller and sensor |
| Slabs uneven across the room | Dripper flow or placement varies | Flush and check lines[^netafim-irrigation-maintenance]; match dripper count to slab[^athena-spacing-irrigation] |

*Most rockwool problems are a water-content or EC reading drifting from plan. The sensor tells you which, and the fix follows.*

## The numbers, in one place

- **Working band:** ~55-92% WC
- **Recovery floor (do not cross):** ~25-30% WC
- **Shot size:** lift WC ~2-5 points
- **Daily runoff:** ~10-20% at field capacity
- **Vegetative dryback:** 5-15 points
- **Generative dryback:** 20-30 points
- **EC by stage:** rises prop -> veg -> flower
- **Steer EC to:** the substrate reading, not drain

> **KEY — The whole method in five lines**
>
> - Saturate to field capacity each morning with a P1 ramp.
> - Hold it through the day with P2 maintenance shots and a small runoff.
> - Let a planned dryback happen, sized to how generative you want to steer.
> - Never let the trough cross the recovery floor.
> - Steer to substrate EC and water content, read off the sensor, run by the controller.

## References

[^grodan-irrigation-medicinal]: Grodan (ROCKWOOL Group). Grodan research reveals new insights into optimal irrigation strategy for large-scale production of medicinal crops. Whitepaper, with B. Nikaj; trials in partnership with Wageningen University & Research, 2020-2022. https://www.grodan.com/ (industry/manufacturer source)
[^owen-norden-preferential-flow-2024]: Owen, J., & Norden, D. (Profile Products). Understanding drainage in horticultural growing media. Greenhouse Management. https://www.greenhousemag.com/article/growing-media-defining-drainage-improve-substrate/ (industry/manufacturer source)
[^hydrus-soilless-substrate-dynamics]: International Society for Horticultural Science (ISHS). Utilizing the HYDRUS model as a tool for understanding soilless substrate water dynamics. Acta Horticulturae 1168. https://www.ishs.org/ishs-article/1168_41 (peer-reviewed)
[^moon-rootzone-ec-2018]: Moon T, Ahn TI, Son JE. Forecasting Root-Zone Electrical Conductivity of Nutrient Solutions in Closed-Loop Soilless Cultures via a Recurrent Neural Network Using Environmental and Cultivation Information. Frontiers in Plant Science. 2018;9:859. https://doi.org/10.3389/fpls.2018.00859 (peer-reviewed)
[^nemali-2006-set-point-irrigation]: Nemali, K. S. & van Iersel, M. W. (2006). An automated system for controlling drought stress and irrigation in potted plants. Scientia Horticulturae, 110(3), 292-297. https://doi.org/10.1016/j.scienta.2006.07.009 (peer-reviewed)
[^tavan-2021-sensor-irrigation-soilless]: Tavan, M., Wee, B., Brodie, G., Fuentes, S., Pang, A., & Gupta, D. (2021). Optimizing Sensor-Based Irrigation Management in a Soilless Vertical Farm for Growing Microgreens. Frontiers in Sustainable Food Systems, 4, 622720. https://doi.org/10.3389/fsufs.2020.622720 (peer-reviewed)
[^caplan2019-drought]: Caplan D, Dixon M, Zheng Y (2019). Increasing inflorescence dry weight and cannabinoid content in medical cannabis using controlled drought stress. HortScience 54(5):964-969. https://doi.org/10.21273/HORTSCI13510-18 (peer-reviewed)
[^malik2025-media]: Malik M, Tlustoš P (2025). Soilless growing media for cannabis cultivation. Agriculture 15(18):1955. https://www.mdpi.com/2077-0472/15/18/1955 (peer-reviewed)
[^netafim-irrigation-maintenance]: Netafim. Complete Irrigation Maintenance Guide (driplines, flushing, filtration and system upkeep). https://www.netafim.com/ (industry/manufacturer source)
[^athena-spacing-irrigation]: Athena Agriculture. Plant Spacing & Irrigation (metric), document A01.001 (pot, rockwool and pressure-compensating dripper selection). https://athenaag.com/ (industry/manufacturer source)
