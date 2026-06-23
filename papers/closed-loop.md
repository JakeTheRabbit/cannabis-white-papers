---
slug: "closed-loop"
title: "The closed loop: levers, signal and plant state"
eyebrow: "Precision · Closed loop"
summary: "Run a grow room as one self-correcting system. This beginner's guide covers the controls you pull, how to read what the plants are actually doing, and how to feed that back without the room chasing its own tail."
track: "Precision & automation"
read_time: "~17 min read"
diagrams: "9 diagrams"
related: ["signal-and-noise", "plant-state-dashboard", "f2-crop-steering"]
url: "https://jaketherabbit.github.io/cannabis-white-papers/closed-loop.html"
md_url: "https://jaketherabbit.github.io/cannabis-white-papers/papers/closed-loop.md"
version: "1.0"
updated: "2026-06-24"
license: "CC BY-NC 4.0"
license_url: "https://creativecommons.org/licenses/by-nc/4.0/"
attribution: "The Cannabis White Papers"
refs: [{"id": "mohammed-spc-2024", "n": 1, "cite": "Mohammed MA. Statistical Process Control. Cambridge University Press (Elements of Improving Quality and Safety in Healthcare); 2024.", "url": "https://doi.org/10.1017/9781009326834", "peer": true}, {"id": "isa-18-2-alarm-mgmt", "n": 2, "cite": "International Society of Automation. ANSI/ISA-18.2-2016, Management of Alarm Systems for the Process Industries. ISA; 2016.", "url": "https://www.isa.org/standards-and-publications/isa-standards/isa-18-series-of-standards", "peer": false}, {"id": "moon-rootzone-ec-2018", "n": 3, "cite": "Moon T, Ahn TI, Son JE. Forecasting Root-Zone Electrical Conductivity of Nutrient Solutions in Closed-Loop Soilless Cultures via a Recurrent Neural Network Using Environmental and Cultivation Information. Frontiers in Plant Science. 2018;9:859.", "url": "https://doi.org/10.3389/fpls.2018.00859", "peer": true}, {"id": "huber-dli-co2-2021", "n": 4, "cite": "Huber BM, Louws FJ, Hernandez R. Impact of Different Daily Light Integrals and Carbon Dioxide Concentrations on the Growth, Morphology, and Production Efficiency of Tomato Seedlings. Frontiers in Plant Science. 2021;12:615853.", "url": "https://doi.org/10.3389/fpls.2021.615853", "peer": true}, {"id": "kim-co2-temp-light-msu", "n": 5, "cite": "Runkle E, Kim WS. Interactions of light, CO2, and temperature on photosynthesis. Michigan State University Extension, Floriculture & Greenhouse Crop Production; 2017.", "url": "https://www.canr.msu.edu/resources/interactions-light-co2-and-temperature", "peer": false}, {"id": "szerement-dielectric-2019", "n": 6, "cite": "Szerement J, Woszczyk A, Szyplowska A, Kafarski M, Lewandowski A, Wilczek A, Skierucha W. A Seven-Rod Dielectric Sensor for Determination of Soil Moisture in Well-Defined Sample Volumes. Sensors (Basel). 2019;19(7):1646.", "url": "https://doi.org/10.3390/s19071646", "peer": true}, {"id": "tdr-fdr-soil-review-2024", "n": 7, "cite": "Advancements in dielectric soil moisture sensor calibration: A comprehensive review of methods and techniques. Computers and Electronics in Agriculture. 2024;218:108663.", "url": "https://doi.org/10.1016/j.compag.2024.108663", "peer": true}, {"id": "choi-ec-transpiration-2015", "n": 8, "cite": "Choi KY, et al. Changes in electrical conductivity and moisture content of substrate and their subsequent effects on transpiration rate, water use efficiency, and plant growth in the soilless culture of paprika (Capsicum annuum L.). Horticulture, Environment, and Biotechnology. 2015;56(2):209-217.", "url": "https://doi.org/10.1007/s13580-015-0154-6", "peer": true}, {"id": "saure-tipburn-calcium-2001", "n": 9, "cite": "Saure MC. Calcium localization and tipburn development in lettuce leaves during early enlargement. Journal of the American Society for Horticultural Science. 2001 / related work on localized calcium deficiency and tipburn.", "url": "https://pubmed.ncbi.nlm.nih.gov/11543566/", "peer": true}]
---

# The closed loop: levers, signal and plant state

_Precision · Closed loop · ~17 min read_

> Run a grow room as one self-correcting system. This beginner's guide covers the controls you pull, how to read what the plants are actually doing, and how to feed that back without the room chasing its own tail.

## What this is (and why a grow room is a loop)

A grow room is a **loop**, not a panel of independent dials you set and forget. You change a control, the room and plants respond, sensors measure that response, you work out what it means, and that tells you what to change next. Around and around, every minute of every day.

A **closed loop** means the output feeds back to the input: what the plant tells you decides your next move, and then you watch what that move actually did. This guide teaches the whole circle as one thing, with three jobs sitting on it: getting the action right (_cause_), getting the measurement honest (_perception_), and getting the meaning out (_cognition_).

**You never move just one thing.** Every control pushes on four linked balances at once: heat, water vapour, CO2 and the salt in the root zone. The finished version of this loop is a room that senses its own state, knows what its actions will do, and corrects its own drift before that drift becomes damage.

> **Diagram.** Read it as a circle. The room works like a nervous system: muscles (the levers), nerves (the sensors) and a mind (the inference that decides what it all means).

> **KEY — What 'closed' buys you**
> 
> A mature loop tells you whole-room health and whether to act in under five seconds, and it stays quiet when nothing needs you. Silence is a feature, not a fault.

## Key terms, defined once

This field is loaded with jargon, so here is every term you need before the real content. Most are everyday ideas with intimidating names. Don't memorise them. Each one comes back in context.

**Lever (actuator)** — A control you can move: light brightness, cooling setpoint, irrigation, CO2 dosing. Around eleven main lever families run a room.

**Signal vs noise** — Signal is what the plant and room are truly doing. Noise is sensor jitter, biological scatter and one-off spikes that mean nothing. Every reading is signal + noise added together.

**Setpoint vs target** — A setpoint is the literal number a machine chases (e.g. cool to 24°C). A target is the outcome you actually want (e.g. keep the plant transpiring healthily). They are not the same thing.

**VPD (vapour pressure deficit)** — How ‘thirsty’ the air is. It drives how fast plants lose water. Measured in kilopascals (kPa).

**EC, VWC, dryback** — EC (electrical conductivity) = how salty the feed or root zone is. VWC = how wet the growing medium is. Dryback = how much the medium dries between waterings.

**Plant state** — The plant's actual condition (stressed, steering generative, on-track), inferred from many signals together rather than read off one gauge.

## The levers: every control moves four things at once

The room is one **coupled** system, not a set of independent knobs. Turn up the light and you have not just added light: you have added heat, made the plants drink and sweat faster (raising humidity), increased CO2 demand, and sped up how fast the root zone dries and concentrates salt[^huber-dli-co2-2021]. Light is at once a heat source, a transpiration driver, a CO2-demand creator and an HVAC load[^kim-co2-temp-light-msu].

Everything you can do sorts into four **balances** you are always disturbing: energy (heat), moisture (water vapour), carbon (CO2) and salt (root-zone EC), with around eleven primary lever families acting across them[^kim-co2-temp-light-msu]. The right question before any change is not ‘what does this lever do?’ but ‘which balance am I disturbing, and can the rest of the room absorb it?’

> **Diagram.** One move, four consequences. Lowering the cooling setpoint is the same story: it changes humidity, VPD, dryback rate and condensation risk together[^choi-ec-transpiration-2015].

> **Diagram.** The four balances respond on very different timescales, which is why a single lever change can look fine for hours and still be quietly loading the slowest balance[^moon-rootzone-ec-2018].

| Balance | What adds to it | What removes it | The lever you reach for |
| --- | --- | --- | --- |
| **Energy** (heat) | Lights, equipment, sun load | AC, ventilation | Light level, cooling setpoint, airflow |
| **Moisture** (vapour) | Transpiration, irrigation | Dehumidifier, exhaust | Dehumid setpoint, VPD target, shot size |
| **Carbon** (CO2) | Dosing | Plant uptake, exhaust | CO2 setpoint, exhaust timing |
| **Salt** (root zone) | Feed EC, dryback | Plant uptake, runoff | Shot size/frequency, dryback target, feed EC, runoff % |

*The four balances and the levers that move each. Every classic failure is a coupling failure, not a broken part.*

> **WARN — Classic failures are coordination failures**
> 
> Cooling that creates humidity, dehumidification that overheats the room, CO2 fighting the exhaust: nothing broke. The levers were just set as if they were independent. The fix is order of operations: set biological demand first (stage, light, CO2), then size climate capacity to match, then set the root-zone strategy to that.

## Reading the signal, then reading the plant

You have to _see_ the room's response without being fooled, then turn it into meaning. Every measurement is signal plus noise, and in practice around **70% of raw alerts are noise** that must be rejected before they ever reach a decision[^isa-18-2-alarm-mgmt].

Reading plant state is the leap from ‘VWC fell 12% overnight’ (a number) to ‘the plant is steering generative as intended, no action needed’ or ‘reduce dryback 3% tonight or expect tip burn in about 48 hours’ (a decision). The goal is to infer the plant, not just display the room.

Three signal habits, in order, get you there:

- **Sample at the right speed** for the biology: fast enough to catch a 30-minute irrigation response, slow enough not to log useless jitter.
- **Filter out scatter** with rolling or median averages before you look.
- **Judge with control limits**, lines drawn from the process's own history, conventionally the mean and roughly ±3 standard deviations (sigma)[^mohammed-spc-2024].

> **Diagram.** A raw sensor reading wobbles every sample. The trend is what the room is doing; the jitter is not. Acting on the jitter is acting on events that never happened.

> **Diagram.** Inside the band = the room being a room, do nothing. A point past the limit, or a non-random run, is a special cause to investigate. Distinguishing common-cause from special-cause variation is the whole basis of statistical process control[^mohammed-spc-2024].

Then **aggregate, don't trust one reading**: believe n-of-12, not n-of-1. A clean, classified signal is the only acceptable input to inference. Inference then fuses several cleaned signals into named conditions, each with a confidence level and an evidence chain, judged against a _learned envelope_ rather than a fixed line. 1.4 kPa VPD is fine in late flower but punishing in early veg.

> **Diagram.** A calm dashboard leads with one green plant-truth headline (‘Flower Day 24, on-track, no action needed’). Yellow is drifting precursors, orange is the only interrupt, and the raw graphs sit last.

## Closing the loop: one problem, traced all the way round

The three jobs become one machine here. Watch a single ordinary problem, slow **salt creep** in the root zone, travel the whole loop.

1. **Cause sets the conditions** — A long dryback plus a flat feed concentrates salt a little more each cycle. The slowest balance is loading.
2. **Perception refuses to overreact** — It ignores any single EC spike, but flags a sustained four-day rising run past the control limit as a true signal.
3. **Cognition gives it meaning** — It fuses that run with feed and dryback data into a named precursor, 'salt accumulation, tip-burn precursor', with confidence and evidence.
4. **Prescribe and act** — It pulls the dryback lever back, closing the loop about four days before tip burn would appear, and the salt balance starts recovering.

> **Diagram.** Closed-loop correction catches root-zone salt accumulation roughly four days before visible tip burn would show[^saure-tipburn-calcium-2001], because the EC the roots feel rises as the medium dries, well before leaves react[^choi-ec-transpiration-2015].

> **NOTE — No single job catches it alone**
> 
> - A **lever-only** grower never measures it.
> - A **signal-only** grower sees a number move but not what it means.
> - A **dashboard-only** grower, without the causal map, prescribes the wrong lever.
> - Only the whole loop has the emergent property of **self-correction**: sensing its own mistakes and undoing them.

Bridge metrics let the three jobs talk to each other. Dryback %, VPD and VPD-hours, pore-water EC and recovery slope are each computed once on a consistent definition and read by every part. Always **prescribe with a number and show your work**: name the action, the setpoint, the deadline and the expected outcome, expandable to the full evidence on demand. Never be a black box.

| Failure | Cause / coupling at fault | Signal discipline that catches it | Inference & prescription |
| --- | --- | --- | --- |
| Silent salt creep | Long dryback + flat feed | 4-day run past EC limit | Tip-burn precursor → ease dryback |
| Irrigation didn't land | Clog / pump / line fault | Expected VWC step absent | Failed shot → re-fire, alert |
| Stealth morning stress | VPD spike at lights-on | VPD-hours over envelope | Morning stress → ramp climate gently |
| Dehumidifier dying slowly | Falling removal capacity | RH drift trend, not spike | Capacity fade → service before failure |
| The blind sensor | Flatlined / noisy probe | Variance collapse or jitter = special cause | Bad probe → quarantine, don't trust |

*Five failures, one fusion. A flatlined, drifting or noisy probe is itself a detectable special-cause signal[^szerement-dielectric-2019].*

## How to build the loop, step by step

You build the loop one rung at a time, and you do not earn the next rung until the previous one is genuinely running. Almost none of this needs new capital. Most of it is discipline.

1. **Arc I: get your actions coupling-aware** — Before any change, name which of the four balances it moves and in which direction. Treat every failure as a capacity or coordination problem, not one bad lever.
2. **Arc II: get your signals honest** — Stop watching live numbers (they invite over-reaction). Set a sampling cadence per channel, put a rolling average on every decision chart, and compute control limits from your own history.
3. **Arc III: get your decisions inferred** — Judge against an envelope per cultivar/stage/photoperiod. Fuse before you flag, because no signal stands alone. Make every advisory prescribe a number and show its evidence, and go quiet by default.
4. **Close the loop last, and gently** — Gate the first automated write-back to a low-risk, reversible move, for example a 3-point dryback nudge behind a confirm. Keep expensive or irreversible actions human-approved.

> **TIP — Discipline before capital**
> 
> The most valuable upgrades on this list cost nothing but habit: a sampling cadence, a rolling average and a control limit are free. Buy hardware only once the discipline is in place to use it.

## Pitfalls: oscillation and chasing noise

Two failure modes ruin a loop: **chasing noise** and **oscillation**. Feed a controller noise, meaning single spikes, jitter and ghost trends, and it acts on events that never happened, actively destabilising the room. A loop fed noise doesn't help, it amplifies. Oscillation comes from reacting too fast, too hard, or to readings still inside normal variation, so the room swings back and forth instead of settling[^mohammed-spc-2024].

> **Diagram.** Reacting to each wiggle drives the room into a swing it can never settle out of. A filtered loop makes one decisive correction only when the signal truly crosses a limit.

> **DANGER — The one-sentence test before reacting**
> 
> Has the reading moved beyond its learned envelope (_meaning_), for longer than one reading with sensors in agreement (_signal_), and do you know which lever answers it without disturbing another balance (_cause_)? If it fails any of the three, it's noise. Do nothing.

- **Aliasing**: sampling too slowly invents phantom trends, and over-sampling logs jitter you can't act on and tempts you to tamper. Match cadence to the biology[^tdr-fdr-soil-review-2024].
- **The Stage-2 trap**: reacting to live numbers is more stressful than flying blind. It's a wall of noise to panic at.
- **Walk the loop, not the wiggle**: smooth enough to act calmly, but never so smooth you go blind to a real fast event. Keep raw data one click away.

## Realistic expectations

> **KEY — The end state is quieter, not flashier**
> 
> A working loop means you look at the dashboard less, are surprised less, and harvest more consistently. Silence is the product: a blank screen means nothing needs you. The advisory-first stage, where the loop tells you what to do but you still pull the lever, is a stable, valuable place to stop indefinitely. Full autonomy is opt-in, gated, and never obligatory.

> **Diagram.** The single highest-return move is getting from rung 2 to rung 3: stop reacting to live numbers, start reacting to filtered trends past control limits. It costs nothing but habit and is the precondition for everything above it.

- **You don't have to automate to win.** Intelligence reaches the screen long before autonomous actuation, and stopping there is a fine, stable outcome.
- **Numbers are starting points, not gospel.** Reference setpoints are commercial-cultivation starting points to calibrate against your own facility's history. The method is universal; the setpoints are yours.
- **Prove it small.** Pick one room and one failure pattern, run it in shadow-mode for one cycle, and prove the lead time on a single advisory before you scale.

Get your actions coupling-aware, your signals honest, and your decisions inferred. Then, and only then, consider closing the loop. To go deeper on the perception half, read the [signal and noise](signal-and-noise.html) paper. For the cognition half and how it reaches you, read the [plant-state dashboard](plant-state-dashboard.html) guide.

## References

[^mohammed-spc-2024]: Mohammed MA. Statistical Process Control. Cambridge University Press (Elements of Improving Quality and Safety in Healthcare); 2024. https://doi.org/10.1017/9781009326834 (peer-reviewed)
[^isa-18-2-alarm-mgmt]: International Society of Automation. ANSI/ISA-18.2-2016, Management of Alarm Systems for the Process Industries. ISA; 2016. https://www.isa.org/standards-and-publications/isa-standards/isa-18-series-of-standards (industry/manufacturer source)
[^moon-rootzone-ec-2018]: Moon T, Ahn TI, Son JE. Forecasting Root-Zone Electrical Conductivity of Nutrient Solutions in Closed-Loop Soilless Cultures via a Recurrent Neural Network Using Environmental and Cultivation Information. Frontiers in Plant Science. 2018;9:859. https://doi.org/10.3389/fpls.2018.00859 (peer-reviewed)
[^huber-dli-co2-2021]: Huber BM, Louws FJ, Hernandez R. Impact of Different Daily Light Integrals and Carbon Dioxide Concentrations on the Growth, Morphology, and Production Efficiency of Tomato Seedlings. Frontiers in Plant Science. 2021;12:615853. https://doi.org/10.3389/fpls.2021.615853 (peer-reviewed)
[^kim-co2-temp-light-msu]: Runkle E, Kim WS. Interactions of light, CO2, and temperature on photosynthesis. Michigan State University Extension, Floriculture & Greenhouse Crop Production; 2017. https://www.canr.msu.edu/resources/interactions-light-co2-and-temperature (industry/manufacturer source)
[^szerement-dielectric-2019]: Szerement J, Woszczyk A, Szyplowska A, Kafarski M, Lewandowski A, Wilczek A, Skierucha W. A Seven-Rod Dielectric Sensor for Determination of Soil Moisture in Well-Defined Sample Volumes. Sensors (Basel). 2019;19(7):1646. https://doi.org/10.3390/s19071646 (peer-reviewed)
[^tdr-fdr-soil-review-2024]: Advancements in dielectric soil moisture sensor calibration: A comprehensive review of methods and techniques. Computers and Electronics in Agriculture. 2024;218:108663. https://doi.org/10.1016/j.compag.2024.108663 (peer-reviewed)
[^choi-ec-transpiration-2015]: Choi KY, et al. Changes in electrical conductivity and moisture content of substrate and their subsequent effects on transpiration rate, water use efficiency, and plant growth in the soilless culture of paprika (Capsicum annuum L.). Horticulture, Environment, and Biotechnology. 2015;56(2):209-217. https://doi.org/10.1007/s13580-015-0154-6 (peer-reviewed)
[^saure-tipburn-calcium-2001]: Saure MC. Calcium localization and tipburn development in lettuce leaves during early enlargement. Journal of the American Society for Horticultural Science. 2001 / related work on localized calcium deficiency and tipburn. https://pubmed.ncbi.nlm.nih.gov/11543566/ (peer-reviewed)
