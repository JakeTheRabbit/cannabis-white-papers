---
slug: "signal-and-noise"
title: "Signal and noise: precision cultivation"
eyebrow: "Precision · Signal & noise"
summary: "Tell a real change in your plants and root zone apart from random sensor wobble, and act only when it matters."
track: "Precision & automation"
read_time: "~14 min read"
diagrams: "9 diagrams"
related: ["root-zone-teros12", "smart-watering-vrwe", "closed-loop"]
url: "https://jaketherabbit.github.io/cannabis-white-papers/signal-and-noise.html"
md_url: "https://jaketherabbit.github.io/cannabis-white-papers/papers/signal-and-noise.md"
version: "1.2"
updated: "2026-07-18"
license: "CC BY-NC 4.0"
license_url: "https://creativecommons.org/licenses/by-nc/4.0/"
attribution: "The Cannabis White Papers"
refs: [{"id": "shewhart-control-chart", "n": 1, "cite": "Control chart. Wikipedia. Describes Walter A. Shewhart's development of statistical process control at Bell Telephone Laboratories (1924), the distinction between common-cause and special-cause variation, and the convention of setting control limits at ±3 standard deviations from the process mean.", "url": "https://en.wikipedia.org/wiki/Control_chart", "peer": false}, {"id": "deming-funnel-tampering", "n": 2, "cite": "The Funnel Experiment. The W. Edwards Deming Institute. Demonstrates that adjusting (tampering with) a stable process in response to individual outcomes increases its variation rather than reducing it; leaving a stable process alone (Rule 1) yields the least variation.", "url": "https://deming.org/explore/the-funnel-experiment/", "peer": false}, {"id": "western-electric-rules-anhoj", "n": 3, "cite": "Anhoej J, Wentzel-Larsen T. Sense and sensibility: on the diagnostic value of control chart rules for detection of shifts in time series data. BMC Medical Research Methodology. 2018;18:100. doi:10.1186/s12874-018-0564-0. Evaluates the Western Electric SPC control-chart rules for detecting non-random (special-cause) variation in sequential data.", "url": "https://doi.org/10.1186/s12874-018-0564-0", "peer": true}, {"id": "nyquist-shannon-sampling", "n": 4, "cite": "Nyquist-Shannon sampling theorem. Wikipedia. States that perfect reconstruction of a band-limited continuous signal requires a sampling rate greater than twice the highest frequency present in the signal; under-sampling causes aliasing and irrecoverable information loss.", "url": "https://en.wikipedia.org/wiki/Nyquist%E2%80%93Shannon_sampling_theorem", "peer": false}, {"id": "replication-reduces-variance", "n": 5, "cite": "Blainey P, Krzywinski M, Altman N. Points of significance: Replication. Variation: use it or misuse it - replication and its variants. PMC3424707. Explains that the standard error of an estimate decreases with the square root of the number of replicates, so replication reduces measurement variance in proportion to sample size.", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3424707/", "peer": true}, {"id": "bogena-soil-sensor-calibration", "n": 6, "cite": "Bogena HR, Huisman JA, Schilling B, Weuthen A, Vereecken H. Effective Calibration of Low-Cost Soil Water Content Sensors. Sensors (Basel). 2017;17(1):208. doi:10.3390/s17010208. Documents sensor-to-sensor variability and drift in low-cost permittivity-based soil moisture sensors, the two-step permittivity-to-water-content calibration, and large accuracy gains (RMSE reduced ~70%) from sensor-specific calibration.", "url": "https://doi.org/10.3390/s17010208", "peer": true}, {"id": "roberts-ewma-1959", "n": 7, "cite": "Roberts SW. Control Chart Tests Based on Geometric Moving Averages. Technometrics. 1959;1(3):239-250. doi:10.1080/00401706.1959.10489860. Introduces the exponentially-weighted (geometric) moving average chart and shows it responds faster to small persistent process shifts than an ordinary moving average of equivalent smoothing.", "url": "https://doi.org/10.1080/00401706.1959.10489860", "peer": true}, {"id": "greenhouse-uniformity-crop-growth", "n": 8, "cite": "Story of a paper: A Study of the Effects of Enhanced Uniformity Control of Greenhouse Environment Variables on Crop Growth. Energies. 2019;12(9):1749. doi:10.3390/en12091749. Shows that reducing spatial/temporal fluctuation (improving uniformity, i.e., lower coefficient of variation) of environment variables improves crop growth and quality.", "url": "https://doi.org/10.3390/en12091749", "peer": true}, {"id": "snr-engineering-origin", "n": 9, "cite": "Signal-to-noise ratio. Wikipedia. Defines SNR as the ratio of signal power to background-noise power, a measure that originated in electrical/communications engineering and is now applied across telecommunications, imaging, and scientific measurement.", "url": "https://en.wikipedia.org/wiki/Signal-to-noise_ratio", "peer": false}]
---

# Signal and noise: precision cultivation

_Precision · Signal & noise · ~14 min read_

> Tell a real change in your plants and root zone apart from random sensor wobble, and act only when it matters.

## What this is, and why a grow room is really a listening problem

> **EVIDENCE — Grain of salt**
>
> **Borderline:** Alarm-noise percentages and control-rule mashups should be replaced with _your_ measured false-positive rate. Name Western Electric vs Nelson rules correctly if you implement them.

Every sensor reading in your grow room is two things added together: the real story (the **signal**) and meaningless jitter (the **noise**). Your whole job is seeing the first through the second.

The hard part of growing has moved from collecting data to reading it. Sensors are cheap and dashboards are pretty, yet most decisions still run on gut feel. Collecting _data_ used to be the work. Now the work is separating the meaningful pattern from the meaningless wobble. This paper teaches you to hear what your plants are telling you above the static, and, just as important, when to do nothing.

A single flower room can generate hundreds of thousands of datapoints a week[^greenhouse-uniformity-crop-growth], so a method for safely ignoring most of them is not optional. More data is not more insight. A firehose of low-quality data is harder to act on than a trickle of good data.

> **Diagram.** One smooth trend (a normal dry-down) lives under a jagged line of sensor jitter. Same numbers, two completely different stories. Only one of them is worth acting on.

> **KEY — The one-line reframe**
>
> You don't have a data problem. You have a **signal-to-noise problem**. Most grow-room ‘alerts’, are often noise until tuned: transients that fix themselves before any action would have mattered.

## Key terms, defined once

The vocabulary comes from radio engineering, manufacturing and statistics, so the words can sound intimidating. They are not. **Signal-to-noise ratio (SNR)** is how loud the thing you care about is compared to everything else competing for your attention[^snr-engineering-origin]. A high-SNR room is calm and decisive. A low-SNR room is anxious and reactive.

**Signal** — A real, meaningful change worth acting on: a sustained trend, a step change, or a repeating daily rhythm.

**Noise** — Meaningless fluctuation: single-reading spikes, jitter, or a transient from a door opening or an HVAC cycle.

**Drift** — A slow, one-way sensor error that masquerades as a real trend. The most dangerous kind of noise, because it looks exactly like signal.

**Averaging / aggregation** — Combining many readings, or many plants, so random quirks cancel out and the shared story remains.

**Control limits** — The boundary, drawn from a process's own history, that separates normal variation from abnormal.

**Calibration** — Checking a probe against a known reference and correcting it, so its readings stay honest over time. [Glossary →](glossary.html#gl-calibration)

| Signal: react to this | Noise: ignore this |
| --- | --- |
| Sustained trend over many readings | A single-reading spike |
| Step change that holds | Jitter smaller than the sensor's accuracy |
| Diurnal (day/night) rhythm | Transient from a door, vent or HVAC cycle |
| Several sensors agree on the move | One lone probe disagreeing with its neighbours |
| A trend confirmed against a reference | Slow drift from an uncalibrated probe |

*At a glance: the shapes of signal versus the shapes of noise.*

## Where the noise comes from

You cannot reduce what you cannot name. Grow-room noise enters through six channels. Three are **physical and inherent**: the sensor itself (electronic jitter, drift, no calibration), placement (a probe near a vent or light, or a sample of one), and biology (one plant differs from the next). The other three are **procedural**, and therefore the cheapest to fix: the environment (doors, HVAC cycling), the operator (inconsistent manual sampling) and the data pipeline (logging gaps, mixed-up units, clock skew).

> **Diagram.** An Ishikawa (fishbone) view: six bones feed the ‘measured noise’ you see on the dashboard. Start with the cheap procedural ones before you blame the hardware.

> **WARN — Drift is the assassin**
>
> Drift moves slowly in one direction, exactly like a real trend, so it fools you for weeks. Uncalibrated pH and EC probes can drift measurably over weeks to a month[^bogena-soil-sensor-calibration]. A single probe is a rumour. Calibration against a known reference is the only defence.

Sensor-specific calibration is not a nicety. In low-cost permittivity soil-moisture sensors, applying a sensor-by-sensor calibration cut error by roughly 70% versus the factory default[^bogena-soil-sensor-calibration]. Most ‘the room is fighting me’ stories are really ‘I am fighting the noise’ stories.

| Source | Signature | Fix | Cost to fix |
| --- | --- | --- | --- |
| Data / process | Gaps, wrong units, clock skew | Audit the pipeline, lock units & timestamps | Low |
| Operator | Readings that jump with who took them | Write an SOP: same time, method, spot | Low |
| Environment | Spikes tied to doors / HVAC cycles | Wider dead-bands, filter transients | Low–med |
| Sensor | Jitter, one-way drift | Calibrate on a schedule against a reference | Med |
| Placement | One probe off from its neighbours | Move off edges into the canopy core | Med |
| Biology | Plant-to-plant spread | Aggregate across many plants (can't remove) | Inherent |

*Six sources, cheapest fix first. Attack the procedural rows before the physical ones.*

## Averaging and how often to measure

The most powerful, most ignored noise filter in horticulture is **replication**. Ask one plant how the room is doing and you get a rumour. Average twelve plants across the bench and the individual quirks cancel, leaving only the shared room signal. The maths is friendly: the error of an average shrinks with the square root of how many readings you combine[^replication-reduces-variance]. Four probes roughly halve the noise, nine cut it to a third.

How often you measure matters just as much. Sample too slowly and a fast pattern folds into a slow one that was never there. Engineers call this **aliasing**: the wagon-wheel-spinning-backwards effect from old films. The rule of thumb, from the Nyquist–Shannon sampling theorem, is to sample at least twice as fast as the fastest pattern you need to see[^nyquist-shannon-sampling]. To catch a 30-minute irrigation response, log every 10–15 minutes.

> **Diagram.** A true fast oscillation, sampled too sparsely, reconstructs as a slow phantom wave. That fake trend will tempt you to act on nothing at all.

> **TIP — Faster is not free**
>
> Over-sampling adds noise, storage cost and the constant temptation to react to jitter. You don't weigh yourself every hour and panic at each wobble. Don't do it to your room either. Match the cadence to the channel.

| Channel | Cadence | Why |
| --- | --- | --- |
| Substrate VWC / EC | 1–5 min | Fast irrigation responses, needs to resolve dryback shape |
| Air temp / RH / VPD | 1–5 min | HVAC swings fast, and VPD is the live steering number |
| CO₂ | 1–5 min | Cycles with doors and injection bursts |
| Pour-through pH / EC | 1×/day, fixed time | A slow drift metric, daily at the same time beats noisy spot checks |
| Plant morphology | 2–3×/week | Growth is slow, more often just adds operator noise |

*A sensible cadence per channel. Match the sample rate to how fast the thing actually moves.*

## Control limits: knowing when a wiggle deserves a response

The most valuable idea in the paper comes from manufacturing's quality revolution: **statistical process control (SPC)**. Walter Shewhart, working at Bell Laboratories, split all variation into two kinds[^shewhart-control-chart]. **Common-cause** variation is the natural jitter of a stable process: it lives inside the control limits and should be left alone. **Special-cause** variation is a real, assignable event that breaks outside the limits and earns investigation.

Control limits are computed from the process's own history, conventionally the mean plus or minus three standard deviations[^shewhart-control-chart], not from a guess. Here is the hard part: W. Edwards Deming proved that **tampering** (reacting to common-cause jitter) amplifies a process's variation rather than reducing it[^deming-funnel-tampering]. SPC gives you permission to do the hardest thing in cultivation: watch a number move and correctly do nothing.

> **Diagram.** A mean line with a ±1σ band and control limits at ±3σ. Most readings jitter harmlessly inside. A lone point past the upper limit is the one that earns a response.[^shewhart-control-chart]

> **NOTE — Beyond the limits: the Western Electric rules**
>
> - **Nelson trend (often 6 points)** all trending the same way: a real drift, even inside the limits
> - **Western Electric: 8 points** on one side of the mean: the process has shifted
> - Abnormal **hugging of the mean**: often a sign the data is being over-smoothed or faked

These pattern rules catch real shifts that a single out-of-limits point would miss, and they do it without raising false alarms on ordinary noise[^western-electric-rules-anhoj]. The lesson is blunt: the over-reactive grower, nudging a stable process all day, is usually the room's single biggest noise source.

## The operator's playbook, step by step

None of the highest-return moves needs new capital. Most need only discipline, tackled top-down. Here is the order to do it in.

1. **Stop watching live numbers** — A live ticker invites tampering. Look at decision charts on a schedule, not the raw feed all day.
2. **Set a sampling cadence per channel** — Use the table above. Fast channels fast, slow channels slow, no faster than you'll act on.
3. **Add a rolling average to every decision chart** — Smooth the line you decide from, but keep a raw view one click away so a real emergency isn't hidden.
4. **Aggregate across 6–12 probes** — Never single-source a decision. Report the average and let one weird probe be outvoted.
5. **Write SOPs for manual readings** — Same time, same method, same spot, every time. That kills operator noise for free.
6. **Calibrate on a logged schedule** — This quarter: a fixed calibration cadence against a reference is your only defence against drift.
7. **Compute control limits for your top 3 KPIs** — Mean ±3σ from your own history. Now you know what 'abnormal' actually means.
8. **Audit placement and widen twitchy dead-bands** — Move probes off edges, vents and lights into the canopy core, and loosen dead-bands that chatter.

> **KEY — The one-sentence test before reacting to any number**
>
> “Has this moved **beyond its normal range**, for **longer than one reading**, and do my **other sensors agree**?” If not all three are yes, it's noise. Walk away.

> **Diagram.** The decision flow drawn out: every gate must pass before you touch a dial. One failed gate sends you to ‘do nothing’.

Three workhorse filters cover almost all grow data: the **moving average** (simple), the **EWMA** (exponentially-weighted, leaning on recent readings so it lags less for the same smoothing[^roberts-ewma-1959]), and the **median filter** (which deletes single-point spikes). Start with a window spanning roughly 30–60 minutes and adjust.

> **Diagram.** A noisy raw line with the smoothed trend running through its centre. The dry-down is now obvious. The only price is a small, predictable lag, which is why you keep the raw view handy for genuine emergencies.

## Common pitfalls

The two opposite failures are **over-smoothing** and **tampering**. Filtering is sugar: a little clarifies, too much rots. Crank the window too wide and you erase a real fast event, a pump failure or an EC spike from a clogged dripper, at exactly the moment you needed to see it. The opposite mistake is reacting to every twitch, which destabilises the very room you were trying to steady[^deming-funnel-tampering].

A specific systems failure is **hunting**. A feedback loop fed noisy data, or tuned too tight, over-corrects one way. The noisy measurement says it overshot, so it slams back the other way, and the room oscillates instead of settling. The fingerprint is a regular saw-tooth in temperature, RH or VWC that _isn't_ driven by day/night. If your HVAC or fertigation seems to ‘fight itself’, suspect a noisy sensor or a too-tight dead-band before you suspect broken equipment.

> **Diagram.** The loop runs setpoint → controller → actuator → room → sensor and back. Noise injected at the sensor is the dangerous one: the controller cannot tell it from a real error, so it acts on a phantom.

> **DANGER — Filter at the source, widen the dead-band**
>
> A wider dead-band plus a filtered input often fixes ‘broken’ climate gear that was never broken. Filter the controller's input right at the sensor's output, before it decides anything. Otherwise every loop in the room is reacting to static.

## Realistic expectations

Facilities climb a predictable ladder, and knowing which rung you're on tells you what to do next.

**1 · Blind**

Gut only. No data, no method.

**2 · Logged**

Data but no method: a wall of noise to panic at.

**3 · Filtered**

Smoothing and sampling rules. The big leap.

**4 · Controlled**

Acting only on special cause.

**5 · Tuned**

Closed-loop, consistency-driven.

Most commercial rooms sit at **Logged**, which is paradoxically more stressful than flying blind, because now there's a wall of noise to panic about. The goal is not the summit overnight. It's one rung up. The jump from Logged to Filtered, just smoothing plus sampling rules, is the highest-return move in this whole paper, and it costs almost nothing but habit.

Track _few_ high-signal KPIs, not forty gauges. The metric most tied to commercial success is often **uniformity**, measured as the batch coefficient of variation, not peak yield. Reducing the spatial and temporal fluctuation of your environment (a lower coefficient of variation) has been shown to improve crop growth and quality[^greenhouse-uniformity-crop-growth]. A batch where every plant yields 95g sells better than one averaging 110g with a 40g spread.

| Signal-rich KPIs: track these | Vanity metrics: ignore these |
| --- | --- |
| Grams per kWh | Instantaneous single-sensor temperature |
| Dryback trend | Total datapoints logged |
| VPD time-in-range | Peak / record readings |
| DLI delivered vs planned | Alert count |
| Batch coefficient of variation | Number of dashboards |

*Coefficient of variation literally measures the noise in your crop. Consistency beats peak performance commercially.*

> **KEY — The honest summary**
>
> You're chasing a higher signal-to-noise ratio, not a perfect room. Aim for one rung up the ladder, smooth before you steer, and earn the right to do nothing when a number wobbles.

Next: see how a clean, filtered signal actually drives irrigation in [smart watering by VWC & EC](smart-watering-vrwe.html), and how that closes the loop without hunting in [closed-loop control](closed-loop.html).

## References

[^shewhart-control-chart]: Control chart. Wikipedia. Describes Walter A. Shewhart's development of statistical process control at Bell Telephone Laboratories (1924), the distinction between common-cause and special-cause variation, and the convention of setting control limits at ±3 standard deviations from the process mean. https://en.wikipedia.org/wiki/Control_chart (industry/manufacturer source)
[^deming-funnel-tampering]: The Funnel Experiment. The W. Edwards Deming Institute. Demonstrates that adjusting (tampering with) a stable process in response to individual outcomes increases its variation rather than reducing it; leaving a stable process alone (Rule 1) yields the least variation. https://deming.org/explore/the-funnel-experiment/ (industry/manufacturer source)
[^western-electric-rules-anhoj]: Anhoej J, Wentzel-Larsen T. Sense and sensibility: on the diagnostic value of control chart rules for detection of shifts in time series data. BMC Medical Research Methodology. 2018;18:100. doi:10.1186/s12874-018-0564-0. Evaluates the Western Electric SPC control-chart rules for detecting non-random (special-cause) variation in sequential data. https://doi.org/10.1186/s12874-018-0564-0 (peer-reviewed)
[^nyquist-shannon-sampling]: Nyquist-Shannon sampling theorem. Wikipedia. States that perfect reconstruction of a band-limited continuous signal requires a sampling rate greater than twice the highest frequency present in the signal; under-sampling causes aliasing and irrecoverable information loss. https://en.wikipedia.org/wiki/Nyquist%E2%80%93Shannon_sampling_theorem (industry/manufacturer source)
[^replication-reduces-variance]: Blainey P, Krzywinski M, Altman N. Points of significance: Replication. Variation: use it or misuse it - replication and its variants. PMC3424707. Explains that the standard error of an estimate decreases with the square root of the number of replicates, so replication reduces measurement variance in proportion to sample size. https://pmc.ncbi.nlm.nih.gov/articles/PMC3424707/ (peer-reviewed)
[^bogena-soil-sensor-calibration]: Bogena HR, Huisman JA, Schilling B, Weuthen A, Vereecken H. Effective Calibration of Low-Cost Soil Water Content Sensors. Sensors (Basel). 2017;17(1):208. doi:10.3390/s17010208. Documents sensor-to-sensor variability and drift in low-cost permittivity-based soil moisture sensors, the two-step permittivity-to-water-content calibration, and large accuracy gains (RMSE reduced ~70%) from sensor-specific calibration. https://doi.org/10.3390/s17010208 (peer-reviewed)
[^roberts-ewma-1959]: Roberts SW. Control Chart Tests Based on Geometric Moving Averages. Technometrics. 1959;1(3):239-250. doi:10.1080/00401706.1959.10489860. Introduces the exponentially-weighted (geometric) moving average chart and shows it responds faster to small persistent process shifts than an ordinary moving average of equivalent smoothing. https://doi.org/10.1080/00401706.1959.10489860 (peer-reviewed)
[^greenhouse-uniformity-crop-growth]: Story of a paper: A Study of the Effects of Enhanced Uniformity Control of Greenhouse Environment Variables on Crop Growth. Energies. 2019;12(9):1749. doi:10.3390/en12091749. Shows that reducing spatial/temporal fluctuation (improving uniformity, i.e., lower coefficient of variation) of environment variables improves crop growth and quality. https://doi.org/10.3390/en12091749 (peer-reviewed)
[^snr-engineering-origin]: Signal-to-noise ratio. Wikipedia. Defines SNR as the ratio of signal power to background-noise power, a measure that originated in electrical/communications engineering and is now applied across telecommunications, imaging, and scientific measurement. https://en.wikipedia.org/wiki/Signal-to-noise_ratio (industry/manufacturer source)
