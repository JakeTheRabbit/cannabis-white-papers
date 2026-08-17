---
slug: "airflow-design"
title: "Airflow design for indoor cultivation"
eyebrow: "Beginner · Airflow design"
summary: "Every leaf sits inside a film of still air that limits how fast it can breathe. Airflow strips that film away. Done right it feeds the plant and dries the room. Done wrong it scorches leaves or breeds rot."
track: "Environment & climate"
read_time: "~26 min read"
diagrams: "8 diagrams · 8 photos"
related: ["grow-room-systems", "mould-risk", "coco-crop-steering"]
url: "https://jaketherabbit.github.io/cannabis-white-papers/airflow-design.html"
md_url: "https://jaketherabbit.github.io/cannabis-white-papers/papers/airflow-design.md"
version: "1.2"
updated: "2026-07-18"
license: "CC BY-NC 4.0"
license_url: "https://creativecommons.org/licenses/by-nc/4.0/"
attribution: "The Cannabis White Papers"
refs: [{"id": "schuepp1993-bl", "n": 1, "cite": "Schuepp PH (1993). Tansley Review No. 59: Leaf boundary layers. New Phytologist 125(3):477-507.", "url": "https://doi.org/10.1111/j.1469-8137.1993.tb03898.x", "peer": true}, {"id": "dupont2025-wind", "n": 2, "cite": "Dupont K, van den Berg TE, Zhang J, Moene AF, Vialet-Chabrand SRM (2025). Beyond the boundary: a new road to improve photosynthesis via wind. J. Exp. Bot. 76(20):5791-5813.", "url": "https://doi.org/10.1093/jxb/eraf325", "peer": true}, {"id": "kitaya2004-airvel", "n": 3, "cite": "Kitaya Y, Shibuya T, Yoshida M, Kiyota M (2004). Effects of air velocity on photosynthesis of plant canopies under elevated CO2 levels. Adv. Space Res. 34(7):1466-1469.", "url": "https://doi.org/10.1016/j.asr.2003.08.031", "peer": true}, {"id": "tjosvold2018-air", "n": 4, "cite": "Tjosvold SA (2018). Maximize photosynthesis with moving air. UC ANR Greenhouse & Floriculture (extension article).", "url": "https://ucanr.edu/blogs/blogcore/postdetail.cfm?postnum=28455", "peer": false}, {"id": "rm2021-light", "n": 5, "cite": "Rodriguez-Morrison V, Llewellyn D, Zheng Y (2021). Cannabis yield, potency, and leaf photosynthesis respond differently to increasing light levels in an indoor environment. Front. Plant Sci. 12:646020.", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8144505/", "peer": true}, {"id": "kitaya2010-circ", "n": 6, "cite": "Kitaya Y, Tsuruyama J, Shibuya T, Yoshida M, Kiyota M (2010). CO2 and air circulation effects on photosynthesis and transpiration of tomato seedlings. Scientia Horticulturae 126(2):326-330.", "url": "https://www.sciencedirect.com/science/article/abs/pii/S0304423810003316", "peer": true}, {"id": "gilliham2011-ca", "n": 7, "cite": "Gilliham M, et al. (2011). Calcium delivery and storage in plant leaves: exploring the link with water flow. J. Exp. Bot. 62(7):2233-2250.", "url": "https://doi.org/10.1093/jxb/err111", "peer": true}, {"id": "chehab2009-thigmo", "n": 8, "cite": "Chehab EW, Eich E, Braam J (2009). Thigmomorphogenesis: a complex plant response to mechano-stimulation. J. Exp. Bot. 60(1):43-56.", "url": "https://doi.org/10.1093/jxb/ern315", "peer": true}, {"id": "chandra2008-photo", "n": 9, "cite": "Chandra S, Lata H, Khan IA, ElSohly MA (2008). Photosynthetic response of Cannabis sativa L. to variations in photosynthetic photon flux densities, temperature and CO2 conditions. Physiol. Mol. Biol. Plants 14(4):299-306.", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3550641/", "peer": true}, {"id": "pipp2026-airflow", "n": 10, "cite": "Anderson K (2026). What cannabis growers can finally learn about airflow. Pipp Horticulture — controlled flower-room trials with Dr. Allison Justice and the Cannabis Research Coalition. (Preliminary: one replicate reported, second underway.)", "url": "https://pipphorticulture.com/what-cannabis-growers-can-finally-learn-about-airflow/", "peer": false}, {"id": "bartok-haf", "n": 11, "cite": "Bartok JW, Grubinger V. Horizontal air flow is best for greenhouse air circulation. UMass Extension Greenhouse & Floriculture / eXtension Farm Energy (extension fact sheet).", "url": "https://farm-energy.extension.org/horizontal-air-flow-is-best-for-greenhouse-air-circulation/", "peer": false}, {"id": "uconn-haf", "n": 12, "cite": "University of Connecticut Integrated Pest Management. Horizontal air flow systems. UConn CAHNR (extension fact sheet).", "url": "https://ipm.cahnr.uconn.edu/horizontal-air-flow-systems/", "peer": false}, {"id": "goto1992-tipburn", "n": 13, "cite": "Goto E, Takakura T (1992). Prevention of lettuce tipburn by supplying air to inner leaves. Transactions of the ASAE 35(2):641-645.", "url": "https://doi.org/10.13031/2013.28644", "peer": true}, {"id": "ahmed2020-multifan", "n": 14, "cite": "Ahmed HA, Tong YX, Yang QC (2020). Lettuce plant growth and tipburn occurrence as affected by airflow using a multi-fan system in a plant factory with artificial light. J. Thermal Biology 88:102496.", "url": "https://doi.org/10.1016/j.jtherbio.2019.102496", "peer": true}, {"id": "moosavi2025-vaf", "n": 15, "cite": "Moosavi-Nezhad M, Meng Q (2025). A calcium-mobilizing biostimulant provides tipburn control comparable to vertical airflow fans in greenhouse hydroponic lettuce 'Rex'. Front. Plant Sci. 16:1701667.", "url": "https://doi.org/10.3389/fpls.2025.1701667", "peer": true}, {"id": "perfduct2025", "n": 16, "cite": "Wang C, Fu J, Zhang Q, Sheng B, He F, Zhang G, Ding X, Cao N (2025). Optimizing perforated duct systems for energy-efficient ventilation in semi-closed greenhouses through process regulation. Processes (MDPI) 13(7):2253.", "url": "https://doi.org/10.3390/pr13072253", "peer": true}, {"id": "amca-fanlaws", "n": 17, "cite": "Air Movement and Control Association International (AMCA). Fan laws (affinity laws): airflow varies with fan speed, pressure with the square of speed, shaft power with the cube of speed. Standard fan-engineering relationship.", "url": "https://www.amca.org/", "peer": false}, {"id": "vas-inrack", "n": 18, "cite": "Vertical Air Solutions / Pipp Horticulture. In-rack airflow systems for vertical cannabis racking (manufacturer documentation).", "url": "https://pipphorticulture.com/in-rack-airflow-systems/", "peer": false}]
---

# Airflow design for indoor cultivation

_Beginner · Airflow design · ~26 min read_

> Every leaf sits inside a film of still air that limits how fast it can breathe. Airflow strips that film away. Done right it feeds the plant and dries the room. Done wrong it scorches leaves or breeds rot.

## Why airflow is not optional

Airflow is plumbing for gases, and it is as important as light and feed. Without moving air, even a perfect light and a perfect feed cannot reach the leaf properly. A still, humid canopy is exactly where bud rot begins.

This guide explains, from zero, what air movement does at the leaf, how much you want, which fans actually make that air, how to rank them, and where to hang them.

## The words you need

**Boundary layer** — The thin film of still air that clings to every leaf surface. Gases have to diffuse across it slowly, so it is the bottleneck airflow attacks.

**Air velocity** — How fast air is moving at the canopy, in metres per second (m/s). This is what matters, not how big your fan is.

**Laminar vs turbulent** — Laminar = smooth, layered airflow (like a calm jet). Turbulent = messy, mixing airflow. For leaves, messy is better.

**Transpiration** — The plant drinking water at the roots and releasing it as vapour from the leaves. Airflow speeds it up by clearing the humid film.

**Air exchange** — Swapping room air with fresh air (intake/exhaust). Different from recirculation, which only stirs the air already in the room.

**HAF / VAF** — The two main hanging fan types. **HAF** = horizontal airflow: hangs above the crop and blows sideways to drive a room-wide loop. **VAF** = vertical airflow: hangs above the crop and blows straight down through it.

**CFM and FPM** — Two different things people confuse. **CFM** (cubic feet per minute) is the _volume_ a fan shifts, which is what it is sold on. **FPM** (feet per minute) is the _speed_ air arrives at a leaf, which is what the plant feels. 200 FPM ≈ 1 m/s.

**Throw and entrainment** — **Throw** is how far a fan's jet stays useful. **Entrainment** is the jet dragging still room air along with it, which is why a modest hanging fan can stir far more air than it actually pushes through its own blades. It is the whole reason HAF loops work.

## The invisible skin of still air

Air right against a leaf barely moves. It forms a stagnant film called the **boundary layer**. CO2 going in, and water vapour and heat coming out, all have to crawl across that film by slow diffusion. The thicker it is, the more it slows the leaf[^schuepp1993-bl].

> **Diagram.** Still air insulates the leaf and slows every exchange. Moving air thins the boundary layer so CO2 gets in faster and water and heat get out faster[^dupont2025-wind].

Moving air thins that film. Even small breezes make a real difference: gentle wind (under ~0.2 m/s added) has been shown to lift daytime photosynthesis by 10–20%[^dupont2025-wind]. This is the reason fans belong in a grow room.

## How much air is the right amount?

More airflow helps, but with sharply diminishing returns. Photosynthesis climbs steeply as you go from dead-still up to a gentle breeze, then flattens out. Most of the benefit is won by the time leaves are gently fluttering[^kitaya2004-airvel].

> **Diagram.** Gas exchange rises fast then plateaus[^kitaya2004-airvel]. The practical target is a **gentle, constant breeze**. Leaves should flutter slightly, not thrash.

> **Diagram.** Below ~0.2 m/s, humid pockets and disease creep in. Above ~1.2 m/s you risk wind-stress and drying the plants out. Aim for the middle.[^tjosvold2018-air]

## Match airflow to your light

The brighter the room, the more the leaf needs air. High light drives high photosynthesis and high transpiration, and both depend on the boundary layer staying thin. Cannabis yield keeps rising with light to very high levels[^rm2021-light], but only if airflow and climate scale with it. A bright room with weak airflow wastes the light.

> **KEY — Airflow moves with the rest of the room**
>
> Light, CO2, temperature, humidity and airflow work together (see the [systems guide](grow-room-systems.html)). Turning up the light without turning up the air leaves hot leaves sitting in their own humid film[^chandra2008-photo].

## Faster air means a hungrier plant

Thinning the boundary layer feeds CO2 in and pulls water out faster. More airflow means more transpiration, which means the plant needs more water and nutrient at the roots. There are two beginner gotchas here:

- **Calcium tip-burn.** Calcium rides into the leaf on the transpiration stream, so uptake tracks water flow[^gilliham2011-ca]. Crank the airflow and under-feed, and you get calcium-deficiency tip-burn even with plenty in the tank. Fix: feed to match the airflow, not the other way round.
- **Sturdier plants (a good thing).** Air movement is a mechanical signal. Plants that feel a breeze grow shorter, thicker, stronger stems, an effect called thigmomorphogenesis[^chehab2009-thigmo]. A well-aired plant holds heavy colas without staking.

> **NOTE — The other half of the calcium story**
>
> Tip-burn cuts both ways, and the direction depends on _where_ the still air is. Too much airflow with too little feed starves the leaf of calcium. But so does a dead-still pocket _buried inside_ a dense canopy, because the leaves in there cannot transpire at all, so no calcium arrives. In lettuce, this is the classic result: blowing air directly into the inner leaves raises their calcium and largely stops tip-burn[^goto1992-tipburn]. That is the single best argument for the top-down fans in section 10.

## Three jobs, three sets of kit

“Add a fan” hides three separate jobs. Buying the wrong one for the job you actually have is the most common airflow mistake in a first room:

**Recirculation (mixing)**

Move the air that is already in the room so every leaf gets a gentle breeze and no humid dead-zones form. This is the boundary-layer job[^kitaya2010-circ], and it is what most of this paper is about.

**Exchange (in / out)**

Swap stale, humid, CO2-depleted room air for fresh air, or push it through a carbon filter. Inline duct fans and wall exhausts. This removes water; it does almost nothing for the leaf.

**Conditioning (heat / cool / dry)**

An air conditioner, dehumidifier or air-handling unit changes the air's temperature and moisture. It has to _deliver_ that treated air somewhere, which is a distribution problem of its own.

> **WARN — Mind the dead zones**
>
> Air takes the easy path and skips corners, the lower canopy, and the inside of dense plants. Those still, humid pockets are where bud rot starts. Place fans to push air _through_ the canopy, not just over the top of it, and defoliate enough to let air in.

## Messy air beats smooth air

Aiming one big fan straight down a row is tempting. Don't. A smooth, laminar jet builds its own thick boundary layer on whatever it hits, and leaves everything off-axis still. **Turbulent, mixing air**, from many fans at varied angles with oscillation, constantly disturbs the film on every leaf from every direction, which is exactly what thins it best[^schuepp1993-bl][^dupont2025-wind].

> **TIP — The flutter test**
>
> Walk the room. Every leaf, top to bottom and inside the plants, should be gently moving. Still leaves anywhere = a pocket you need to reach. A leaf that is flapping hard = back that fan off.

## What a controlled room trial shows

Everything above is leaf physiology. Does it actually move yield in a real flower room? A controlled trial by Pipp Horticulture with Dr. Allison Justice and the Cannabis Research Coalition tested exactly that: three identical flower rooms with VPD, temperature and humidity held constant, changing only the airflow[^pipp2026-airflow].

The rooms ran at different delivered air speeds, measured in feet per minute (FPM), the standard unit for room airflow. They compared near-still air against roughly 100, 200 and 400 FPM (about 0.5, 1.0 and 2.0 m/s). One clean result fell out:

> **Diagram.** The response was a **threshold, not a gentle slope**: below ~200 FPM little changed; above it, yield, plant shape and uniformity improved together[^pipp2026-airflow].

That looks like it fights the leaf-level plateau in Figure 2, but it does not. Figure 2 is the speed at a single _leaf_; FPM here is what the whole room _delivers_. Air slows as it pushes into the canopy, so a room has to move well over 1 m/s at the fans before the buried lower and interior leaves feel the gentle breeze Figure 3 asks for. Roughly 200 FPM delivered is about what it takes to land _every_ leaf in the sweet spot, not just the ones on the outside.

Above that threshold, the higher-airflow rooms showed three things:

- **More sellable flower.** Stems carried less biomass and more of the plant's energy went into bud. Trim ran about 42% in the still-air plants and was significantly lower with good airflow, so less of the harvest ended up as larf[^pipp2026-airflow].
- **Less stress.** Still-air plants had redder stems and more anthocyanin, a visible stress marker; the well-aired plants looked more uniform and less stressed.
- **Taller, not weaker.** Higher-airflow plants finished roughly 6 inches taller than the still-air controls, with most vertical growth done by the end of week three, while still putting _less_ into stem. Here the extra height is relief from still-air stress, not the mechanical dwarfing you would get under a harder, direct wind (see section 06).

> **KEY — Uniformity is the real lesson**
>
> Even in a tightly engineered room, the crew saw a positional bias: the first 1–2 feet of each row behaved differently from the rest. Their takeaway is the one to keep, **“if airflow isn’t uniform, neither is your crop.”** That is the dead-zone problem from section 07, now measured. Making sure no leaf is left in still air beats chasing a high average fan speed.

> **NOTE — How solid is this?**
>
> Treat it as strong early field evidence, not settled science: the results so far are one replicate, with a second run underway to firm up the statistics[^pipp2026-airflow]. The direction lines up cleanly with the leaf physiology in the rest of this paper.

## The fan types, one by one

Fans are not interchangeable. Each type makes a different _shape_ of air, and the shape decides which leaves get served. Pick by the shape you need, not by the price tag or the CFM on the box.

What each one looks likeGrok ImagineHAF fanVAF fanOscillating fanClip fanDrum / floor fanUnder-canopy fanAir sockInline duct fan

> **Diagram.** The eight types you will actually meet, drawn side-on with the air each one makes. The first six are recirculation kit; the air sock is a delivery method; the inline duct fan is exchange, not circulation at all.

**HAF — horizontal airflow fan**

A hanging basket fan, typically a 300–500 mm (12–20 inch) blade on a small 1/10–1/15 hp motor, hung above head height and aimed sideways down the room[^bartok-haf]. Several of them together drive one slow **racetrack loop**: air runs down one side of the room and back the other. Its jet drags surrounding still air along with it (entrainment), so a modest fan stirs a large volume.

**Where:** above the canopy, a quarter of the room width in from the wall. **The catch:** its air runs _over_ the top of the crop. In a dense canopy it never reaches the middle.

**VAF — vertical airflow fan**

Hangs above the canopy and blows **straight down through it**, usually with a flared diffuser on top so it draws air from a wide area and delivers a broad column rather than a narrow jet. This is the one type that reliably reaches leaves buried inside a plant.

**Where:** over the canopy on a grid, spacing set so the down-columns overlap. **The catch:** more expensive per unit, and it casts shade, so mind where you hang it relative to the lights.

**Oscillating wall or pole fan**

The classic grow-room fan: a head on a bracket that sweeps an arc. Cheap, everywhere, and genuinely good in a small room, because the sweep gives you the varied, turbulent air section 08 asks for.

**Where:** wall or pole mounted, aimed to _mix_ the room, never pointed straight at plants. **The catch:** it time-shares. Each leaf only gets air for part of each sweep, so at scale you need a lot of them to hold a constant breeze.

**Clip fan**

A miniature oscillating fan on a clamp, gripping a tent pole or frame. Moves roughly one plant's worth of air.

**Where:** tents and single-plant setups only. **The catch:** nothing about it scales. If you are running more than about 2 m² of canopy, clip fans are a false economy: you end up with six of them doing the job of one proper hanging fan, at higher total wattage and worse uniformity.

**Drum / pedestal floor fan**

A large, powerful head on a stand. Very high thrust, a narrow jet, and a lot of noise. This is a blunt instrument.

**Where:** temporarily, to break a specific dead corner or dry a room down fast after a spill. **The catch:** it is the single most common cause of wind-burn. Plants directly in front get a gale and everything off-axis gets nothing. Do not build a room's airflow on these.

**Under-canopy fan**

A low, flat, wide fan that sits at pot level and blows across the floor and up into the bottom of the plants. The zone it serves is the wettest and stillest in the room: cool air sinks, pots and floors evaporate into it, and no overhead fan reaches it.

**Where:** at floor or bench level, blowing along the rows. **The catch:** almost none, which is why it is such good value. Just keep it out of the way of irrigation lines and keep the intake clear of leaf litter.

**Air sock / perforated poly tube**

A long fabric or polythene tube, fed by a fan or an air handler, that leaks air through hundreds of small holes along its whole length. Because the holes are small and numerous, delivery is remarkably even and there is no single blast anywhere. Research design targets sit around 6–10 mm holes at 30–70 mm spacing, with the fan holding roughly 30–40 Pa of static pressure so the tube stays inflated and round[^perfduct2025].

**Where:** running the length of a row, over or under the bench. It is the standard way to deliver _conditioned_ air from an AC or dehumidifier without creating a draught in one corner and a dead zone in the other. **The catch:** you have to design it (tube diameter, hole size, hole spacing) and it needs a fan that can actually make the pressure.

**Inline duct fan**

A fan inside a length of ducting. This is an **exchange** device, not a circulation device: it pulls air out of the room, usually through a carbon filter, and dumps it outside. It is what controls humidity and refreshes CO2 in a vented room.

**Where:** ducted to a high point in the room (hot, humid air rises), with a passive or active intake low down. **The catch:** people count it as their airflow. It is not. A room with a big extractor and no circulation fans still has a still, humid canopy.

Three more you will meet in bigger rooms, listed here so you can place them correctly rather than mistake them for canopy airflow:

**HVLS / destratification fan**

A large, very slow ceiling fan. Its job is to break the warm layer that collects near the ceiling under lights and push it back down. Useful in tall rooms; pointless under a 2.4 m ceiling.

**Wall / shutter exhaust fan**

Bulk air exchange for greenhouses and large rooms, with gravity or motorised shutters. Same class as the inline duct fan, just much bigger. Sealed rooms usually do not have one.

**AHU / HVAC supply**

The air-handling unit that actually heats, cools and dries. It sets your VPD. It still needs a distribution method — typically ducting into socks — to get that treated air evenly across a canopy.

Recirculation · vertical rackingIn-rack airflow systems (vertical farms)If you grow on multi-tier racking, none of the above works on its own: each tier is a low, enclosed slot that overhead fans physically cannot reach. Purpose-built systems mount a ducted fan bar into the racking itself and push air along or down through every tier[^vas-inrack]. On racking this is not an upgrade, it is the only thing that works, and it is the setup the Pipp trial in section 09 was built to test.

## Which fans earn their place

A ranking is only honest if you say what it is ranking _for_. This one scores **crop-relevant airflow bought per dollar installed, in a sealed, single-tier indoor flower room** of roughly 20–200 m² of canopy. Change the room and the order changes; the callout below says how.

> **Diagram.** The backbone is cheap and the glamour is not. Note that the two lowest-ranked fans are the two most first-time growers actually buy.

| # | Fan type | What it buys you | Reach into the canopy | Verdict |
| --- | --- | --- | --- | --- |
| 1 | **HAF fan** | A room-wide loop, running 24/7 on very few watts | Over the top only | **Build the room on these.** Cheapest uniformity you can buy[^bartok-haf] |
| 2 | **Under-canopy fan** | Kills the wettest, stillest zone in the room | Bottom of the plant | **Best value add-on.** Targets exactly where bud rot starts |
| 3 | **VAF fan** | Air driven down into the middle of the plant | Full depth — the only one that gets there | **Buy once density rises.** Peer-reviewed for interior-leaf calcium[^goto1992-tipburn][^moosavi2025-vaf] |
| 4 | Oscillating wall fan | Cheap, varied, turbulent air | Over and around, in bursts | Fine as the backbone below ~20 m². Falls behind above it |
| 5 | Air sock off the AHU | Even delivery of _conditioned_ air, no draughts | Along the row, gentle | Excellent, but it is capex plus design work[^perfduct2025] |
| 6 | HVLS / destratification | Breaks the hot layer under the ceiling | Bulk mixing only | Only pays in tall rooms. Wasted under a low ceiling |
| 7 | Drum / pedestal fan | Raw thrust into one spot | A gale on-axis, nothing off it | Spot-fix only. Leading cause of wind-burn |
| 8 | Clip fan | One plant's worth of air | One plant | Tents only. Six of these lose to one hanging fan |
| Ranked on value per dollar for a sealed, single-tier indoor flower room. Exchange kit (inline duct and wall fans) is deliberately absent: it is mandatory, but it does a different job and cannot be traded against a circulation fan. |

> **KEY — When the ranking flips**
>
> - **Vertical racking:** in-rack systems move to #1 outright and HAF drops off the list. Overhead fans cannot physically reach inside a tier[^vas-inrack].
> - **Dense, un-defoliated canopies:** VAF overtakes HAF. Top-down airflow is measurably better than horizontal for getting air, and therefore calcium, into inner leaves[^goto1992-tipburn][^ahmed2020-multifan]. In greenhouse lettuce, vertical fans cut tip-burn ratings from 5.0 to under 0.1 and burnt leaves from 39% to under 7%[^moosavi2025-vaf].
> - **Tents and single-plant grows:** the whole table collapses to a clip fan or two plus the extractor, and that is genuinely the right answer at that scale.
> - **Greenhouses:** HAF stays #1 and the air sock rises, because you are also distributing heat[^uconn-haf].

> **WARN — The mistake the ranking is really about**
>
> Almost every underperforming room has the same shape of problem: **plenty of total CFM, badly distributed**. Two drum fans in the corners produce an impressive number on paper and a still, humid middle. Six small hanging fans on a loop produce a smaller number and a room where every leaf moves. Buy the pattern, not the peak.

## Where to actually put them

Fan placement is a pattern problem, not a coverage problem. You are not trying to hit every plant with a jet; you are trying to set the whole volume of air in the room turning slowly and consistently, then punch that moving air down into the canopy.

> **Diagram.** The horizontal loop, from above. Fans do not each cover a patch — they hand air to each other around a circuit. First fan roughly 3–4.5 m (10–15 ft) off the end wall, then 12–15 m (40–50 ft) apart, about a quarter of the room width in from the side[^bartok-haf][^uconn-haf].

Then cut the room the other way. Most rooms buy airflow for the top of the canopy only, and that is exactly why rot starts at the bottom and in the middle:

> **Diagram.** The same room in section. Three heights, three different jobs, three different fans. If you only own HAF fans you own the top band, and the two bands where disease actually starts are unserved.

1. **Set the loop first** — Pick a direction and commit. Hang HAF fans so that air runs down one side of the room and back the other, each fan feeding the next. Never point two fans at each other — you will cancel the loop and create a dead spot exactly where they meet[^bartok-haf].
2. **Get the height right** — Above head height, roughly 2.1–2.4 m (7–8 ft) off the floor for a floor-grown crop, so the jet clears the canopy rather than ploughing into it[^uconn-haf]. Where there are hanging baskets or a light rack in the way, go a clear distance above or below, not level with them.
3. **Punch down into the canopy** — Add top-down fans over the crop on a grid, spaced so their down-columns overlap. This is the step almost everyone skips, and it is the one that reaches the interior leaves[^goto1992-tipburn].
4. **Serve the floor** — Put low fans at pot level blowing along the rows. Cold, wet air pools down there and no overhead fan will move it.
5. **Aim to mix, never to blast** — Angle fans slightly off-parallel and let oscillation vary the direction. You want a room full of slow, turbulent, mixing air — not a set of jets[^schuepp1993-bl].
6. **Walk it and correct** — Run the flutter test at all three heights: over the tops, hand pushed into the middle of a plant, and down at pot level. Whichever height fails is the fan you are missing. A cheap anemometer, or a length of flagging tape taped to a cane, turns this from a guess into a reading.

> **TIP — Run them all the time**
>
> Circulation fans should run **24 hours a day**, lights on and lights off. The extension guidance is to run them continuously except when exhaust fans are running or vents are open, because that is when the room is being flushed anyway[^bartok-haf]. Lights-off is when leaf temperature drops toward dew point and condensation forms — precisely when you least want still air[^uconn-haf].

## Sizing the system

The greenhouse industry has been sizing horizontal airflow for decades and the rules of thumb transfer well to an indoor room. Start here, then measure and adjust:

| What | Rule of thumb | Where it comes from |
| --- | --- | --- |
| Total circulation capacity | **2 CFM per ft² of floor** (≈ 36.6 m³/h per m²). A 30 × 100 ft house needs ~6,000 CFM total. | Bartok & Grubinger, UConn/UVM Extension[^bartok-haf] |
| First fan position | 3–4.5 m (10–15 ft) in from the end wall, to catch air coming round the corner. | UConn IPM[^uconn-haf] |
| Fan spacing | 12–15 m (40–50 ft) apart along the loop. Scale down proportionally in a small room. | Bartok & Grubinger[^bartok-haf] |
| Horizontal position | About ¼ of the room width in from the side wall (or centre of the bay). | UConn IPM[^uconn-haf] |
| Mounting height | Above head height; ~2.1–2.4 m (7–8 ft) for floor crops. Clear of baskets and light racks. | Bartok & Grubinger[^bartok-haf] |
| Individual fan size | 300–500 mm (12–20 in) blade, 1/10–1/15 hp. Many small beats few large. | Bartok & Grubinger[^bartok-haf] |
| Greenhouse velocity target | 50–100 FPM (0.25–0.5 m/s) of general room movement. | UConn IPM[^uconn-haf] |
| Cannabis flower-room target | ~200 FPM (≈1.0 m/s) _delivered_, to land every leaf in the sweet spot. | Pipp / Justice trial[^pipp2026-airflow] |
| Run time | 24/7, except while exhaust fans run or vents are open. | Bartok & Grubinger[^bartok-haf] |
| Air sock design | 6–10 mm holes, 30–70 mm spacing, ~30–40 Pa static to hold the tube round. | Perforated-duct CFD study[^perfduct2025] |

> **NOTE — Why the two velocity targets disagree**
>
> The greenhouse standard (50–100 FPM) and the cannabis figure (~200 FPM) are not in conflict; they were set for different goals. The greenhouse number is aimed at temperature uniformity and stopping condensation on leaves overnight in a relatively open, lower-light crop[^uconn-haf]. The cannabis number comes from a dense, high-light flower canopy where the goal is driving air _into_ the plant[^pipp2026-airflow]. Denser canopy and brighter light both push the number up. Use the greenhouse rules for the layout and the cannabis number for the target.

One last number, and it is the one that saves the most money. Fan airflow rises in step with speed, but shaft power rises with the **cube** of speed[^amca-fanlaws]. Halving a fan's speed drops it to roughly one-eighth of the power. That has a direct design consequence:

> **KEY — More fans, slower, always wins**
>
> Two fans at full speed and eight fans at half speed can move similar air, but the eight fans draw around a quarter of the power _and_ give far better coverage, because the air arrives from more directions with fewer dead spots. This is why speed-controllable EC-motor fans are worth the premium over fixed-speed AC fans: an AC fan is effectively on or off, so to reduce airflow you have to switch fans off, which punches holes in your coverage exactly where the fan you killed used to be.

## Troubleshooting

| Symptom | Likely cause | What to do |
| --- | --- | --- |
| Bud rot starting deep in colas | Dead-zone: air not reaching the canopy interior | Add top-down (VAF) airflow, defoliate, lower RH |
| Tops flutter, middle and bottom dead still | All your airflow is above the canopy (HAF only) | Add VAF over the crop and under-canopy fans at pot level |
| Rot and mildew starting at the bottom | The floor zone is the wettest, stillest air in the room | Under-canopy fans blowing along the rows |
| Leaf-tip burn despite full tank | Airflow outran nutrient delivery (calcium) | Raise feed/EC to match transpiration |
| Tip-burn only on new inner growth | Inner leaves too still to transpire, so no calcium arrives | Get air into the canopy interior, not just over it |
| Leaves clawing / wind-burnt edges | Air velocity too high / fan pointed at plants | Reduce speed, aim fans to mix, not blast |
| One end of a row always behaves differently | Broken loop: fans spaced too far apart or facing each other | Re-set the racetrack; never point two fans head-on |
| Big fans, loud room, still stratified | Too few fans running flat out | More fans at lower speed — power rises with the cube of speed |
| Tall, weak, floppy stems | Too little air movement: no mechanical signal | Add gentle constant breeze across the canopy |
| Room humidity stuck high | Recirculation OK but not enough air exchange | Increase intake/exhaust / dehumidification |
| Cold or dry patch under the AC outlet | Conditioned air dumped in one spot instead of distributed | Duct it into an air sock along the row |

## Realistic expectations

> **KEY — What to remember**
>
> 1. Airflow's job is to **thin the boundary layer** on every leaf. That is the whole game.
> 2. Aim for a **gentle, turbulent breeze (~0.3–1.0 m/s)** everywhere, including inside the plants.
> 3. Buy the **pattern, not the peak**: many small fans on a loop beat two big ones in the corners.
> 4. Serve **all three heights** — above, through and below the canopy. Only the first is easy.
> 5. More air = more thirst: **feed and humidity must keep up**[^gilliham2011-ca].
> 6. Most benefit comes early. You do not need a wind tunnel[^kitaya2004-airvel].

Airflow is one subsystem of the room. Read it alongside the [systems guide](grow-room-systems.html) and the [mould risk](mould-risk.html) paper.

## References

[^schuepp1993-bl]: Schuepp PH (1993). Tansley Review No. 59: Leaf boundary layers. New Phytologist 125(3):477-507. https://doi.org/10.1111/j.1469-8137.1993.tb03898.x (peer-reviewed)
[^dupont2025-wind]: Dupont K, van den Berg TE, Zhang J, Moene AF, Vialet-Chabrand SRM (2025). Beyond the boundary: a new road to improve photosynthesis via wind. J. Exp. Bot. 76(20):5791-5813. https://doi.org/10.1093/jxb/eraf325 (peer-reviewed)
[^kitaya2004-airvel]: Kitaya Y, Shibuya T, Yoshida M, Kiyota M (2004). Effects of air velocity on photosynthesis of plant canopies under elevated CO2 levels. Adv. Space Res. 34(7):1466-1469. https://doi.org/10.1016/j.asr.2003.08.031 (peer-reviewed)
[^tjosvold2018-air]: Tjosvold SA (2018). Maximize photosynthesis with moving air. UC ANR Greenhouse & Floriculture (extension article). https://ucanr.edu/blogs/blogcore/postdetail.cfm?postnum=28455 (industry/manufacturer source)
[^rm2021-light]: Rodriguez-Morrison V, Llewellyn D, Zheng Y (2021). Cannabis yield, potency, and leaf photosynthesis respond differently to increasing light levels in an indoor environment. Front. Plant Sci. 12:646020. https://pmc.ncbi.nlm.nih.gov/articles/PMC8144505/ (peer-reviewed)
[^kitaya2010-circ]: Kitaya Y, Tsuruyama J, Shibuya T, Yoshida M, Kiyota M (2010). CO2 and air circulation effects on photosynthesis and transpiration of tomato seedlings. Scientia Horticulturae 126(2):326-330. https://www.sciencedirect.com/science/article/abs/pii/S0304423810003316 (peer-reviewed)
[^gilliham2011-ca]: Gilliham M, et al. (2011). Calcium delivery and storage in plant leaves: exploring the link with water flow. J. Exp. Bot. 62(7):2233-2250. https://doi.org/10.1093/jxb/err111 (peer-reviewed)
[^chehab2009-thigmo]: Chehab EW, Eich E, Braam J (2009). Thigmomorphogenesis: a complex plant response to mechano-stimulation. J. Exp. Bot. 60(1):43-56. https://doi.org/10.1093/jxb/ern315 (peer-reviewed)
[^chandra2008-photo]: Chandra S, Lata H, Khan IA, ElSohly MA (2008). Photosynthetic response of Cannabis sativa L. to variations in photosynthetic photon flux densities, temperature and CO2 conditions. Physiol. Mol. Biol. Plants 14(4):299-306. https://pmc.ncbi.nlm.nih.gov/articles/PMC3550641/ (peer-reviewed)
[^pipp2026-airflow]: Anderson K (2026). What cannabis growers can finally learn about airflow. Pipp Horticulture — controlled flower-room trials with Dr. Allison Justice and the Cannabis Research Coalition. (Preliminary: one replicate reported, second underway.) https://pipphorticulture.com/what-cannabis-growers-can-finally-learn-about-airflow/ (industry/manufacturer source)
[^bartok-haf]: Bartok JW, Grubinger V. Horizontal air flow is best for greenhouse air circulation. UMass Extension Greenhouse & Floriculture / eXtension Farm Energy (extension fact sheet). https://farm-energy.extension.org/horizontal-air-flow-is-best-for-greenhouse-air-circulation/ (industry/manufacturer source)
[^uconn-haf]: University of Connecticut Integrated Pest Management. Horizontal air flow systems. UConn CAHNR (extension fact sheet). https://ipm.cahnr.uconn.edu/horizontal-air-flow-systems/ (industry/manufacturer source)
[^goto1992-tipburn]: Goto E, Takakura T (1992). Prevention of lettuce tipburn by supplying air to inner leaves. Transactions of the ASAE 35(2):641-645. https://doi.org/10.13031/2013.28644 (peer-reviewed)
[^ahmed2020-multifan]: Ahmed HA, Tong YX, Yang QC (2020). Lettuce plant growth and tipburn occurrence as affected by airflow using a multi-fan system in a plant factory with artificial light. J. Thermal Biology 88:102496. https://doi.org/10.1016/j.jtherbio.2019.102496 (peer-reviewed)
[^moosavi2025-vaf]: Moosavi-Nezhad M, Meng Q (2025). A calcium-mobilizing biostimulant provides tipburn control comparable to vertical airflow fans in greenhouse hydroponic lettuce 'Rex'. Front. Plant Sci. 16:1701667. https://doi.org/10.3389/fpls.2025.1701667 (peer-reviewed)
[^perfduct2025]: Wang C, Fu J, Zhang Q, Sheng B, He F, Zhang G, Ding X, Cao N (2025). Optimizing perforated duct systems for energy-efficient ventilation in semi-closed greenhouses through process regulation. Processes (MDPI) 13(7):2253. https://doi.org/10.3390/pr13072253 (peer-reviewed)
[^amca-fanlaws]: Air Movement and Control Association International (AMCA). Fan laws (affinity laws): airflow varies with fan speed, pressure with the square of speed, shaft power with the cube of speed. Standard fan-engineering relationship. https://www.amca.org/ (industry/manufacturer source)
[^vas-inrack]: Vertical Air Solutions / Pipp Horticulture. In-rack airflow systems for vertical cannabis racking (manufacturer documentation). https://pipphorticulture.com/in-rack-airflow-systems/ (industry/manufacturer source)
