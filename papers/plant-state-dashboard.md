---
slug: "plant-state-dashboard"
title: "From telemetry to intelligence: the plant-state dashboard"
eyebrow: "Precision · Dashboards"
summary: "A grow-room screen should show what the plant is doing, not a wall of raw sensor numbers. Here is how to design one that does."
track: "Precision & automation"
read_time: "~13 min read"
diagrams: "11 diagrams"
related: ["signal-and-noise", "f2-crop-steering", "root-zone-teros12"]
url: "https://jaketherabbit.github.io/cannabis-white-papers/plant-state-dashboard.html"
md_url: "https://jaketherabbit.github.io/cannabis-white-papers/papers/plant-state-dashboard.md"
version: "1.0"
updated: "2026-06-24"
license: "CC BY-NC 4.0"
license_url: "https://creativecommons.org/licenses/by-nc/4.0/"
attribution: "The Cannabis White Papers"
refs: [{"id": "spc-signal-noise-ed", "n": 1, "cite": "Pimentel L, Barrueto F Jr. Statistical process control: separating signal from noise in emergency department operations. Journal of Emergency Medicine. 2015;48(5):628-638. doi:10.1016/j.jemermed.2014.12.019.", "url": "https://doi.org/10.1016/j.jemermed.2014.12.019", "peer": true}, {"id": "preattentive-dataviz", "n": 2, "cite": "Fusco R, Granata V, Setola SV, et al. Visual Perception and Pre-Attentive Attributes in Oncological Data Visualisation. Bioengineering. 2025;12(7):782. doi:10.3390/bioengineering12070782.", "url": "https://doi.org/10.3390/bioengineering12070782", "peer": true}, {"id": "vpd-plant-response", "n": 3, "cite": "Grossiord C, Buckley TN, Cernusak LA, Novick KA, Poulter B, Siegwolf RTW, Sperry JS, McDowell NG. Plant responses to rising vapor pressure deficit (Tansley review). New Phytologist. 2020;226(6):1550-1566. doi:10.1111/nph.16485.", "url": "https://doi.org/10.1111/nph.16485", "peer": true}, {"id": "capacitive-soil-moisture", "n": 4, "cite": "Briciu-Burghina C, Zhou J, Ali MI, Regan F. Demonstrating the Potential of a Low-Cost Soil Moisture Sensor Network. Sensors. 2022;22(3):987. doi:10.3390/s22030987.", "url": "https://doi.org/10.3390/s22030987", "peer": true}, {"id": "alarm-mgmt-isa182", "n": 5, "cite": "Engineering Equipment and Materials Users' Association (EEMUA). EEMUA Publication 191: Alarm Systems - A Guide to Design, Management and Procurement; and ANSI/ISA-18.2, Management of Alarm Systems for the Process Industries. (Industry standards; alarm-flood threshold ~10 alarms/10 min, <=3-4 priorities, <=5% high-priority.)", "url": "https://www.exida.com/articles/ALARM-MANAGEMENT-AND-ISA-18-A-JOURNEY-NOT-A-DESTINATION.pdf", "peer": false}]
---

# From telemetry to intelligence: the plant-state dashboard

_Precision · Dashboards · ~13 min read_

> A grow-room screen should show what the plant is doing, not a wall of raw sensor numbers. Here is how to design one that does.

## What this is, and why it matters

A modern grow room is wired with sensors measuring air temperature, humidity, VPD, CO₂, light, substrate moisture, EC, root-zone temperature, pH and power draw, second by second. The dashboards built to show all of this are walls of live numbers and graphs. They tell you _what_ is happening. They never tell you what it _means_, what is about to happen, or what to do about it.

This paper makes the case for a different design centre, which we will call **Plant-State Intelligence**: a screen that reasons about the plant instead of just displaying the room. The target is a ‘calm dashboard’: one that stays quiet most of the time and speaks only when it has something worth saying. A telemetry-dump dashboard forces the human to be the integrator, synthesising fifteen graphs into a judgement in real time, often while tired. A plant-state dashboard does that synthesis for you.

> **NOTE — What this paper is, and isn't**
> 
> - This is an **operational and product-design guide**, not a horticulture-science paper. Most claims here are design opinions backed by worked examples.
> - The aim is a screen that **infers** the plant's state, **predicts** trouble days early, and **prescribes** the next step with its evidence and confidence attached.
> - The one-line thesis: _a cockpit full of gauges is not a co-pilot._

> **Diagram.** The telemetry-dump path (above) leaves all the reasoning to the human. Plant-State Intelligence moves that step into the software: sensors → fusion and inference → one plain-language judgement.

## Key terms, defined from zero

Here are the words before the argument. Don't memorise them. Each one comes back in context.

**Telemetry** — The raw measurements streamed off your sensors, second by second: temperature, humidity, moisture and the rest, before anything is done with them.

**VPD (vapour pressure deficit)** — How ‘thirsty’ the air is for moisture, which drives how fast a plant transpires. 1.4–1.6 kPa is fine in late flower but punishing in early veg. The same number means different things at different stages.

**Crop steering** — Deliberately pushing a plant **vegetative** (leafy growth) or **generative** (flower and resin) by controlling irrigation and dryback.

**Inference** — Estimating something you cannot measure directly, like plant stress, by combining several things you can measure.

**Sensor fusion** — Combining several signals over time into one conclusion. ‘Leaf temp up’ alone is noise. ‘Leaf temp up _and_ transpiration flat _and_ dryback unusually deep’ is a diagnosis.

**Dryback** — How much the substrate dries between irrigations. _Dryback depth_ and _dryback rate_ are derived crop-steering metrics that matter more than any raw moisture number.

**Leading vs lagging indicator** — A leading indicator is a precursor that warns early. A lagging indicator is a symptom that confirms damage already happened.

**Baseline / trajectory** — The expected envelope for this cultivar, at this stage and point in the photoperiod, learned from your own past runs.

**PPFD / DLI** — PPFD is instantaneous light intensity. DLI is the total daily light delivered. EC is the salt concentration in the feed or root-zone pore water.

## Why the sensor dashboard falls short

The conventional dashboard rests on one implicit theory: ‘expose every measurement and a skilled grower will know what to do.’ That fails in seven predictable ways. Every sensor measures the plant's **surroundings**, air, root zone, light, and none measures vigour, stress or transpiration directly. That leaves an inference gap the human must cross unaided. Capacitive moisture probes, for instance, report water content in the substrate, never the plant's own water status[^capacitive-soil-moisture].

It is also reactive. By the time a line crosses a threshold, salt accumulation or a stalled dryback has been accruing for hours or days. Its static high/low alarms ‘cry wolf’: they fire on transient blips like a door opening or a lights-on spike, so growers learn to ignore them. Alarm-management standards from process industries put the alarm-flood threshold at roughly ten alarms per ten minutes and cap high-priority alarms at about five percent. A grow-room dashboard that buzzes constantly has already lost the operator's trust[^alarm-mgmt-isa182].

> **Diagram.** The seven failure modes of a telemetry-dump dashboard. Each is a place where the human is left doing work the software could do.

> **Diagram.** Pore-water EC creeps up for four days while the grower notices nothing, until tip burn appears on Day 26. A single-channel chart shows the cause the whole time, but nobody is watching that one line at that moment. That is the lag a plant-state system is built to close[^spc-signal-noise-ed].

> **WARN — Single-channel widgets hide the truth**
> 
> The real story about plant health lives in cross-signal, multivariate patterns: moisture, EC, VPD and transpiration moving together. A wall of single-channel gauges structurally cannot express that pattern, no matter how many you add.

## Six inversions: from gauge cluster to calm dashboard

Plant-State Intelligence inverts six assumptions baked into the sensor dashboard. None of these throws the raw data away. It just moves to the ‘basement,’ still available on drill-down for the expert and the post-mortem.

| Axis | From: gauge cluster | To: calm dashboard |
| --- | --- | --- |
| **Object** | Instrumentation: show the environment | Inference: estimate the plant's state |
| **Reference** | Fixed thresholds | Learned baselines per cultivar × stage × photoperiod phase |
| **Breadth** | One signal per widget | Multi-input fusion across signals |
| **Timing** | Lagging symptoms | Leading precursors |
| **Output** | Alert: ‘a number moved’ | Prescription: action, deadline, consequence |
| **Posture** | Always-on wall of graphs | Exception-based, quiet by default |

*The six inversions. The hardest shift is the last one: silence becomes the default state.*

> **KEY — The plant should win the fight for attention**
> 
> An always-on wall of graphs competes with the plant for the grower's attention, and the plant should win. That is why a prescription replaces a bare alert. It names the action, the deadline, and the consequence of ignoring it. And it is why silence, not a full screen, is the healthy resting state.

## What the system actually infers

The pipeline estimates four (really five) interacting states. **Environmental state**, temperature, RH, VPD, CO₂, light, is reframed as integrals and rates: VPD-hours accumulated today, DLI to date, not instants. Plant response to VPD is non-linear and cumulative rather than tied to any single reading[^vpd-plant-response], so the accumulated quantity is the meaningful one. **Substrate state** adds derived crop-steering metrics: dryback depth and rate, field-capacity recovery, and shot-to-shot moisture response.

The **plant physiological state** is the whole point. It is not measured but **estimated**, by fusing the others into a transpiration proxy, a stress index, a vigour/stacking trajectory and a steering-response readout. **Operational/equipment state** and an optional **vision state** (canopy cameras) round it out. Sensor health itself is treated as a first-class signal, so the system knows when it is blind.

> **Diagram.** Environmental, substrate and equipment/vision states feed inward into the inferred plant physiological state. That centre is what the grower actually cares about, and the only thing no sensor reports.

| Raw value | Derived, meaningful form |
| --- | --- |
| WC = 42% | Dryback depth 8%, slower than this cultivar's baseline |
| VPD = 1.5 kPa right now | VPD-hours 18% above the in-range envelope for the day |
| EC = 5.1 mS/cm | Pore-water EC rising 4 days straight, tip-burn risk |
| Leaf temp +0.6°C | Transpiration flat despite higher VPD: stomata closing |

*The same number, raw vs derived. The right column is what a plant-state dashboard shows. The left is in the basement.*

> **TIP — The output is a short list of named conditions**
> 
> This layer does not emit fifteen numbers. It emits a short list of **named conditions**: ‘dryback stalling,’ ‘salt accumulating,’ ‘over-transpiring,’ each with a confidence and an evidence chain. Cameras already on site for security become a horticultural input: canopy colour and uniformity, lights-on wilt, height and stacking over days, early discoloration.

## The six-layer pipeline

The system is a six-layer pipeline that maps cleanly onto a Home Assistant–centred stack. Most operations already have layers 0 and 1 without realising it. The intelligence moves to the dashboard long before the actuation does: autonomous control is earned channel by channel, after advisories prove correct.

1. **Layer 0: Ingest** — Pull every raw stream onto one shared timebase. Most rooms already do this.
2. **Layer 1: Derive** — Turn raw into meaningful: VPD, dryback %, DLI, recovery slopes, shot response.
3. **Layer 2: Baseline** — Build per-cultivar / stage / photoperiod envelopes, seeded from horticultural priors and refined on your own runs.
4. **Layer 3: Infer** — Fuse everything into named conditions with confidence and evidence: rules plus anomaly detection, optionally an LLM reasoning pass.
5. **Layer 4: Prescribe** — Map each condition to a concrete action with a deadline.
6. **Layer 5: Present** — The calm dashboard. Optional gated Layer 5b closes the loop on low-risk, explicitly-licensed actions only.

> **Diagram.** The pipeline, layer by layer. Layer 2 baselines can be seeded from published horticultural targets (Athena targets are one example) before you have any history of your own.

> **NOTE — Advisory-first is the design, not a limitation**
> 
> The human-in-the-loop posture is deliberate. An operation can run permanently at ‘advise only’ and capture most of the value. Layer 5b auto-applies only the low-risk, explicitly-licensed actions. Anything irreversible or expensive stays human-approved.

## The new dashboard surface: four zones

What the grower opens has four zones, in priority order, and on a good day, three of them are empty. Zone 1 is the **Headline**: one line of plant truth in plain language with a status colour, which is 90% of what a busy grower needs 90% of the time. Zone 2 is the **Watchlist** of things drifting but not yet wrong, the precursors, and it exists precisely to make the next zone rare. Zone 3 is **Advisories**, the only zone that should ever interrupt, each prescriptive and time-bound. Zone 4 is the **Evidence and raw basement**, demoted but never deleted.

**Zone 1: Headline**

‘Flower Day 24 · Room 3 · On-track. Steering generative as intended. No action needed.’

**Zone 2: Watchlist**

Drifting but not yet wrong: the precursors. Each item is a sentence, not a graph. Often empty.

**Zone 3: Advisories**

The only zone that interrupts. Prescriptive and time-bound. Expands to its evidence chain.

**Zone 4: Evidence / raw**

The old dashboard, demoted. Fused signals, baselines, raw graphs, for drill-down and the post-mortem.

Colour and layout do real work here. A calm dashboard leans on pre-attentive cues, a single status colour, position, one bold line, that the eye reads before conscious attention engages, so the ‘all clear’ state is grasped at a glance[^preattentive-dataviz].

> **KEY — A sample advisory, in full**
> 
> ‘Reduce dryback target 3% in Room 3 (Day 24)… Tip burn likely within ~48h if unaddressed. Confidence: high. _[Show evidence]_’, and the evidence expands to the fused signals, the baseline it violated, and the historical precedent. The old dashboard was 100% Zone 4. The new one leads with Zones 1–3 and keeps 4 in the basement.

## The adoption path: crawl, walk, run

This is not a boil-the-ocean rebuild. Each stage ships value and earns the next, and most of the payoff lands by Stage 3, long before any closed-loop control.

> **Diagram.** Six rungs from telemetry to closed-loop. Stage 2, baseline and go quiet, is the single biggest step, because it ends alarm fatigue in one move.

1. **Pick one room, one pattern** — Choose a single failure pattern (say, stalling dryback) and implement Stages 1–3 for just that pattern in Home Assistant.
2. **Run it shadow-mode for a cycle** — Run alongside the existing dashboard for a full cycle. Don't act on it yet. Watch whether it would have been right.
3. **Prove the lead time** — Measure the gap between the advisory firing and when the problem would have become visible. Prove it on one advisory before scaling.
4. **Scale pattern by pattern** — Add the next failure pattern, then the next room. Stage 4 (prescribe) and Stage 5 (closed-loop) are opt-in, channel by channel.

> **TIP — Stage 4 is a stable, valuable end state**
> 
> Advisory-first is not a stepping stone you are obligated to leave. An operation can sit at Stage 4 forever and capture most of the value. Stage 5 closed-loop is optional and gated to low-risk, licensed actions only.

## Trust, confidence, and failure modes

An advisory system that is wrong _and_ confident is worse than no system at all. Trust is a balance: you spend it with every wrong call and earn it with every right one, so advisory **precision**, not raw volume, is what drives action. Five guardrails are non-negotiable.

| Guardrail | Failure it prevents | Mechanism |
| --- | --- | --- |
| Cold-start honestly | False certainty from one cycle | Seed from horticultural priors, widen confidence bands, label outputs ‘still learning’ |
| Cheap to correct | Resentment at wrong calls | Every advisory is dismissable and markable as a false positive, and the marks tune the baselines |
| Track precision | Silent quality drift | Advisory precision and false-positive rate are first-class, visible metrics |
| Human in the loop | Irreversible or costly mistakes | Anything expensive or irreversible stays human-approved |
| Never a black box | Loss of trust in the WHAT | Every conclusion expands to its evidence chain |

*The five guardrails. Each prevents a specific way an advisory system loses the grower's trust.*

> **DANGER — Treat the system's own blindness as a signal**
> 
> A drifted, noisy or flatlined sensor is itself an advisory. For example: ‘EC probe in Room 2 reads implausibly flat: suspect failure, EC-derived advisories paused.’ A grower who can't see _why_ will, correctly, stop trusting the _what_. The system's job is to make the decision obvious, not to make it alone on anything irreversible or expensive.

## Measuring success and realistic expectations

If the new dashboard is working, the grower looks at it **less**, is surprised **less**, and harvests **more consistently**. Six run-over-run metrics make that concrete, and for half of them, the success direction is _down_.

> **Diagram.** A healthy target profile across the six KPIs. Lead time, precision and decisions-per-week should be high. Surprises, dashboard dwell time and outcome variance should be low.

- **Lead time**: hours or days between an advisory and when the problem would have become visible. The core KPI. The whole point is catching drift before it becomes damage.
- **Surprises**: visible damage with no prior advisory. Drive this to zero.
- **Advisory precision**: acted-upon advisories over total, plus the false-positive rate.
- **Dashboard dwell time**: lower is better. Attention should return to the plants, not the screen.
- **Decisions surfaced per week**: the output is decisions, not pageviews.
- **Outcome variance**: yield and quality consistency, cycle over cycle.

> **KEY — The honest framing**
> 
> Most of the payoff lands by Stage 3, and advisory-first may well be the right permanent end state. You are never obligated to chase closed-loop control. The working names (Plant-State Intelligence, ‘calm dashboard’) are explicitly placeholders: substance over branding.

Start small. Build the inference layer that catches drift early, see the [signal-and-noise](signal-and-noise.html) paper for the statistics underneath it, and feed it the derived crop-steering metrics from [f2 crop steering](f2-crop-steering.html). The dashboard is only as good as the states it reasons over.

## References

[^spc-signal-noise-ed]: Pimentel L, Barrueto F Jr. Statistical process control: separating signal from noise in emergency department operations. Journal of Emergency Medicine. 2015;48(5):628-638. doi:10.1016/j.jemermed.2014.12.019. https://doi.org/10.1016/j.jemermed.2014.12.019 (peer-reviewed)
[^preattentive-dataviz]: Fusco R, Granata V, Setola SV, et al. Visual Perception and Pre-Attentive Attributes in Oncological Data Visualisation. Bioengineering. 2025;12(7):782. doi:10.3390/bioengineering12070782. https://doi.org/10.3390/bioengineering12070782 (peer-reviewed)
[^vpd-plant-response]: Grossiord C, Buckley TN, Cernusak LA, Novick KA, Poulter B, Siegwolf RTW, Sperry JS, McDowell NG. Plant responses to rising vapor pressure deficit (Tansley review). New Phytologist. 2020;226(6):1550-1566. doi:10.1111/nph.16485. https://doi.org/10.1111/nph.16485 (peer-reviewed)
[^capacitive-soil-moisture]: Briciu-Burghina C, Zhou J, Ali MI, Regan F. Demonstrating the Potential of a Low-Cost Soil Moisture Sensor Network. Sensors. 2022;22(3):987. doi:10.3390/s22030987. https://doi.org/10.3390/s22030987 (peer-reviewed)
[^alarm-mgmt-isa182]: Engineering Equipment and Materials Users' Association (EEMUA). EEMUA Publication 191: Alarm Systems - A Guide to Design, Management and Procurement; and ANSI/ISA-18.2, Management of Alarm Systems for the Process Industries. (Industry standards; alarm-flood threshold ~10 alarms/10 min, <=3-4 priorities, <=5% high-priority.) https://www.exida.com/articles/ALARM-MANAGEMENT-AND-ISA-18-A-JOURNEY-NOT-A-DESTINATION.pdf (industry/manufacturer source)
