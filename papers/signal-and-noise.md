---
slug: "signal-and-noise"
title: "Find the difference between plant changes and sensor noise"
eyebrow: "Precision · Signal and noise"
summary: "This paper shows you how to find the signal in your sensor data and how to ignore the random jitter. Thus you know when to adjust the room. It is equally important to know when to make no adjustment."
track: "Precision and automation"
read_time: "~14 min to read"
diagrams: "9 diagrams"
related: ["root-zone-teros12", "smart-watering-vrwe", "closed-loop"]
url: "https://www.growlabs.nz/wiki/signal-and-noise.html"
md_url: "https://www.growlabs.nz/wiki/papers/signal-and-noise.md"
version: "1.2"
updated: "2026-07-18"
license: "CC BY-NC 4.0"
license_url: "https://creativecommons.org/licenses/by-nc/4.0/"
attribution: "The Cannabis White Papers"
refs: [{"id": "shewhart-control-chart", "n": 1, "cite": "Control chart. Wikipedia. Describes Walter A. Shewhart's development of statistical process control at Bell Telephone Laboratories (1924), the distinction between common-cause and special-cause variation, and the convention of setting control limits at ±3 standard deviations from the process mean.", "url": "https://en.wikipedia.org/wiki/Control_chart", "peer": false}, {"id": "deming-funnel-tampering", "n": 2, "cite": "The Funnel Experiment. The W. Edwards Deming Institute. Demonstrates that adjusting (tampering with) a stable process in response to individual outcomes increases its variation rather than reducing it; leaving a stable process alone (Rule 1) yields the least variation.", "url": "https://deming.org/explore/the-funnel-experiment/", "peer": false}, {"id": "western-electric-rules-anhoj", "n": 3, "cite": "Anhoej J, Wentzel-Larsen T. Sense and sensibility: on the diagnostic value of control chart rules for detection of shifts in time series data. BMC Medical Research Methodology. 2018;18:100. doi:10.1186/s12874-018-0564-0. Evaluates the Western Electric SPC control-chart rules for detecting non-random (special-cause) variation in sequential data.", "url": "https://doi.org/10.1186/s12874-018-0564-0", "peer": true}, {"id": "nyquist-shannon-sampling", "n": 4, "cite": "Nyquist-Shannon sampling theorem. Wikipedia. States that perfect reconstruction of a band-limited continuous signal requires a sampling rate greater than twice the highest frequency present in the signal; under-sampling causes aliasing and irrecoverable information loss.", "url": "https://en.wikipedia.org/wiki/Nyquist%E2%80%93Shannon_sampling_theorem", "peer": false}, {"id": "replication-reduces-variance", "n": 5, "cite": "Blainey P, Krzywinski M, Altman N. Points of significance: Replication. Variation: use it or misuse it - replication and its variants. PMC3424707. Explains that the standard error of an estimate decreases with the square root of the number of replicates, so replication reduces measurement variance in proportion to sample size.", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3424707/", "peer": true}, {"id": "bogena-soil-sensor-calibration", "n": 6, "cite": "Bogena HR, Huisman JA, Schilling B, Weuthen A, Vereecken H. Effective Calibration of Low-Cost Soil Water Content Sensors. Sensors (Basel). 2017;17(1):208. doi:10.3390/s17010208. Documents sensor-to-sensor variability and drift in low-cost permittivity-based soil moisture sensors, the two-step permittivity-to-water-content calibration, and large accuracy gains (RMSE reduced ~70%) from sensor-specific calibration.", "url": "https://doi.org/10.3390/s17010208", "peer": true}, {"id": "roberts-ewma-1959", "n": 7, "cite": "Roberts SW. Control Chart Tests Based on Geometric Moving Averages. Technometrics. 1959;1(3):239-250. doi:10.1080/00401706.1959.10489860. Introduces the exponentially-weighted (geometric) moving average chart and shows it responds faster to small persistent process shifts than an ordinary moving average of equivalent smoothing.", "url": "https://doi.org/10.1080/00401706.1959.10489860", "peer": true}, {"id": "greenhouse-uniformity-crop-growth", "n": 8, "cite": "Story of a paper: A Study of the Effects of Enhanced Uniformity Control of Greenhouse Environment Variables on Crop Growth. Energies. 2019;12(9):1749. doi:10.3390/en12091749. Shows that reducing spatial/temporal fluctuation (improving uniformity, i.e., lower coefficient of variation) of environment variables improves crop growth and quality.", "url": "https://doi.org/10.3390/en12091749", "peer": true}, {"id": "snr-engineering-origin", "n": 9, "cite": "Signal-to-noise ratio. Wikipedia. Defines SNR as the ratio of signal power to background-noise power, a measure that originated in electrical/communications engineering and is now applied across telecommunications, imaging, and scientific measurement.", "url": "https://en.wikipedia.org/wiki/Signal-to-noise_ratio", "peer": false}]
---

# Find the difference between plant changes and sensor noise

_Precision · Signal and noise · ~14 min to read_

> This paper shows you how to find the signal in your sensor data and how to ignore the random jitter. Thus you know when to adjust the room. It is equally important to know when to make no adjustment.

## Purpose and scope

> **EVIDENCE: Weak**
>
> **Limit of the data:** Replace the percentages of alarm noise and the control rules from this paper with _your_ measured rate of false positives. If you use the Western Electric rules or the Nelson rules, use the correct name for each.

Each sensor reading in your grow room is the total of two parts: the accurate information (the **signal**) and jitter that gives no information (the **noise**). Your task is to find the signal in the noise.

Sensors have a low cost, and dashboards are easy to make. But growers continue to make most decisions with no method. At this time, the task is to find the difference between the signal and the noise. This paper gives you a method for this task. The paper also gives you a method to know when to make no adjustment. This method is equally important.

One flower room can make hundreds of thousands of data points in a week[^greenhouse-uniformity-crop-growth]. Thus a method to ignore most of them safely is necessary. More data does not give more information that you can use. It is less easy to use a large quantity of low-quality data for decisions than a small quantity of good data.

> **Diagram.** The figure shows one smooth trend (a usual dryback) below a rough line of sensor jitter. The numbers are the same, but the information is different. Only the smooth trend is important for your decisions.

> **KEY: The problem in one sentence**
>
> A **signal-to-noise problem** is the primary cause of most alarm fatigue in grow rooms. In this problem, the jitter is too large, and the signal is not easy to see. Before tuning, most alarms are transients. A transient stops before an adjustment has an effect.

## Definitions

The terms in this paper are from radio engineering, manufacturing and statistics. **Signal-to-noise ratio (SNR)** is the strength of the signal that is important to you, compared with the strength of all other signals[^snr-engineering-origin]. In a room with a high SNR, the decisions are easy and the room is stable. In a room with a low SNR, the decisions are not easy and you adjust the room too frequently.

**Signal**: A change in the data that is accurate and important for your decisions. Examples are a trend that continues for many readings, a step change, or a rhythm that occurs again each day.

**Noise**: Variation in the data that gives no information. Examples are a spike in one reading, jitter, or a transient from a door that opens or from an HVAC cycle.

**Drift**: A slow error of a sensor in one direction. The error has the same shape as a trend in the plant. Drift is the type of noise that causes the most problems, because it looks the same as a signal.

**Averaging / aggregation**: The average of many readings, or of many plants. The random differences of each reading become small, and the information that all readings have stays.

**Control limits**: Limits that you calculate from the recorded data of the system. Variation in the limits is usual, and variation out of the limits is unusual.

**Calibration**: The task in which you compare a probe with a known reference and correct the probe. Thus the readings stay accurate for a long time. [Glossary →](glossary.html#gl-calibration)

| Signal: do something about it | Noise: ignore it |
| --- | --- |
| A trend that continues for many readings | A spike in one reading |
| A step change that stays | Jitter that is smaller than the accuracy of the sensor |
| A rhythm of day and night | A transient from a door, a vent or an HVAC cycle |
| Some sensors agree on the change | One probe that does not agree with the probes near it |
| A trend that agrees with a reference | Slow drift from a probe with no calibration |

*The table compares the shapes of signal and the shapes of noise.*

## Sources of measurement noise

You cannot decrease a source of noise if you cannot find it. Noise in a grow room comes from six sources. Three are **physical sources** that are part of the measurement. They are the sensor (electronic jitter, drift, no calibration), the position (a probe near a vent or a light, or a sample of one) and the biology (one plant is different from the next). The other three are **procedural sources**, and thus they have the lowest cost to correct. They are the environment (doors, HVAC cycles), the operator (manual sampling that is not the same each time) and the data pipeline (gaps in the data, incorrect units, clock skew).

> **Diagram.** The figure is an Ishikawa diagram (fishbone diagram). Six sources cause the ‘measured noise’ that you see on the dashboard. Correct the procedural sources, which cost less, before you think that the equipment has a fault.

> **WARN: Drift is the noise that causes the most problems**
>
> Calibrate each probe with a known reference, because calibration is the only protection from drift. Drift moves slowly in one direction, the same as a trend in the plant. Thus drift can give you incorrect information for many weeks. A pH probe or an EC probe with no calibration can have drift. You can measure the drift in weeks to a month[^bogena-soil-sensor-calibration]. One probe is not sufficient to make sure that the data are correct.

A calibration for each sensor is necessary. In low-cost permittivity sensors for soil moisture, a calibration for each sensor decreased the error by approximately 70%, compared with the calibration of the manufacturer[^bogena-soil-sensor-calibration]. When a grower thinks that the room is a problem, the noise is frequently the problem.

| Source | Symptom | Task | Cost to correct |
| --- | --- | --- | --- |
| Data pipeline | Gaps, incorrect units, clock skew | Examine the data pipeline. Make sure that the units and the timestamps do not change. | Low |
| Operator | Readings that change with the person who made them | Write an SOP with the same time, the same method and the same position. | Low |
| Environment | Spikes that agree with doors or HVAC cycles | Make the dead-bands wider. Filter the transients. | Low or medium |
| Sensor | Jitter, drift in one direction | Calibrate at set intervals with a reference | Medium |
| Position | One probe that is different from the probes near it | Move the probes from the edges to the middle of the canopy | Medium |
| Biology | Differences between plants | Calculate the average of many plants (you cannot remove the differences) | You cannot remove it |

*The six sources, with the source of lowest cost to correct first. Correct the procedural rows before the physical rows.*

## Sampling and averaging

The noise filter with the largest effect is to calculate the average of more sensors, and not to use only one sensor. Growers frequently ignore this filter. In your room, when you calculate the average of twelve plants across the bench, the differences of each plant become small. Only the information that all plants have stays.The name of this method is **replication**. The error of an average decreases with the square root of the number of readings that you use[^replication-reduces-variance]. Four probes decrease the noise to approximately one half, and nine probes decrease it to one third.

The frequency of the measurements is equally important. If the interval between the samples is too long, a fast pattern changes to a slow pattern that is not in the plant. The interval between the samples causes this incorrect trend. This error has the name **aliasing**.The usual method comes from the Nyquist–Shannon sampling theorem[^nyquist-shannon-sampling]. Use a sampling frequency of a minimum of two times the frequency of the fastest pattern that you must see. To see an irrigation response of 30 minutes, record the data at intervals of 10–15 minutes.

> **Diagram.** A fast oscillation, when the interval between the samples is too long, gives a slow incorrect wave. This incorrect trend can make you adjust the room for a change that does not occur.

> **TIP: A high sampling rate has a cost**
>
> A sampling rate that is too high adds noise and storage cost. It also makes you want to adjust the room for each jitter. Use a sampling cadence that agrees with each channel.

| Channel | Cadence | Because |
| --- | --- | --- |
| Substrate VWC / EC | 1–5 min | The irrigation responses are fast. The cadence must show the shape of the dryback. |
| Air temperature / RH / VPD | 1–5 min | The HVAC changes quickly, and the VPD is the value for crop steering at this time. |
| CO₂ | 1–5 min | The CO₂ increases and decreases when doors open and when the system injects CO₂ for short periods. |
| Pour-through pH / EC | 1×/day, same time | The indicator of slow drift. A reading each day at the same time is better than checks at random times that add noise. |
| Plant morphology | 2–3×/week | The growth is slow. More frequent measurements add only noise from the operator. |

*A correct cadence for each channel. Make the sampling rate agree with the rate of change of the quantity that you measure.*

## Control limits and adjustment thresholds

The most important method in this paper is from the work on quality in manufacturing: **statistical process control (SPC)**. Walter Shewhart, at Bell Laboratories, divided all variation into two types[^shewhart-control-chart]. **Common-cause** variation is the jitter of a stable system. It stays in the control limits, and you must not adjust the system for it. **Special-cause** variation has a cause that you can find. It is out of the limits, and you must examine the cause.

You calculate the control limits from the recorded data of the system, and not from an estimate. The usual limits are the mean plus or minus three standard deviations[^shewhart-control-chart]. W. Edwards Deming showed that **tampering** (an adjustment of the system for common-cause jitter) increases the variation of a system and does not decrease it[^deming-funnel-tampering]. SPC lets you do a task in cultivation that is not easy: monitor a number that changes and, correctly, make no adjustment.

> **Diagram.** The figure shows a mean line, a zone of ±1σ and control limits at ±3σ. Most readings have jitter in the limits, and this jitter does not cause a problem. One point above the top limit is the point that you must examine.[^shewhart-control-chart]

> **NOTE: More than the limits: the Western Electric rules**
>
> - **Nelson trend (frequently 6 points)** in which all the points go in the same direction. The trend shows a drift, also when the points are in the limits.
> - **Western Electric: 8 points** on one side of the mean show that the system changed.
> - **Points too near the mean** are unusual. They are frequently a sign that a filter is too strong, or that a person made the data and did not measure them.

These Western Electric rules and Nelson rules find changes that you cannot find when you compare only one point with the limits. They do not cause false alarms for usual noise[^western-electric-rules-anhoj]. A grower who adjusts a stable system many times in a day is usually the largest source of noise in the room.

## Eight steps to decrease noise this week

It is not necessary to have new capital for the steps with the largest effect. For most steps, you must only do the same work each time. Do the steps in the sequence below.

1. **Do not monitor the values at all times**: A display that shows the values at all times causes tampering. Examine the decision charts at set times, and not the raw data all day.
2. **Set a sampling cadence for each channel**: Use the table above. Use a high rate for fast channels and a low rate for slow channels. Do not use a sampling rate that is higher than the rate of your adjustments.
3. **Add a rolling average to each decision chart**: Filter the line that you use for decisions. Keep a display of the raw data that you can show in one step. Then you can see an emergency.
4. **Calculate the average of 6–12 probes**: Do not use only one source for a decision. Use the average, and let the one probe that is different have a small effect.
5. **Write SOPs for manual readings**: Use the same time, the same method and the same position each time. The SOP removes the noise from the operator at no cost.
6. **Calibrate at set intervals and keep a record**: In the next three months, set a calibration cadence with a reference. This calibration cadence is your only protection from drift.
7. **Calculate the control limits for your 3 primary KPIs**: Calculate the mean ±3σ from your recorded data. Then you know which values are unusual.
8. **Examine the positions and make dead-bands wider**: Move the probes from the edges, the vents and the lights to the middle of the canopy. Make a dead-band wider if the equipment starts and stops frequently.

> **KEY: The test of one sentence before you do something about a number**
>
> “Is this value **out of its usual range**, for **more than one reading**, and do my **other sensors agree**?” If one of the three is no, it is noise. Ignore it.

> **Diagram.** The figure shows the decision flow. Each gate must be yes before you adjust the controls. If one gate is no, go to ‘ignore’.

Three filters are sufficient for almost all the data from a grow room. The **moving average** is easy. The **EWMA** (exponentially weighted) gives more weight to the last readings, and thus it has less lag for the same smoothing[^roberts-ewma-1959]. The **median filter** removes spikes of one point. Start with a filter window of approximately 30–60 minutes, and then adjust it.

> **Diagram.** The figure shows the raw data as a rough line, and the filtered trend through the middle of the line. The dryback is easy to see. The only cost is a small lag of a known size. Thus you keep a display of the raw data for an emergency.

## Troubleshooting

Two errors that are opposite are **over-smoothing** and **tampering**. A weak filter makes the data clear, but a filter that is too strong causes damage to the data. If the filter window is too wide, the filter removes a fast change that is not noise. Examples are a pump fault or an EC spike from a blocked dripper, and you must see these changes when they occur. The opposite error is to adjust the room for each small change. Such adjustments make the room less stable[^deming-funnel-tampering].

A feedback loop with data that have noise, or with a tuning that is too strong, makes corrections that are too large. The corrections go in one direction and then in the other direction, and the loop does not become stable. A thermostat that is too sensitive is an example. It starts the heater when it reads one degree low, and the temperature becomes too high. Then it starts the chiller, and the temperature becomes too low. As a result, the temperature of the room changes continuously.This error has the name **hunting**. The symptom of hunting is a regular saw-tooth pattern in the temperature, the RH or the VWC. The day/night cycle _does not_ cause this pattern. If your HVAC or fertigation system makes opposite corrections one after the other, the cause is frequently a sensor with noise. The cause can also be a dead-band that is too small. Think of an equipment fault only after you examine these two causes.

> **Diagram.** The loop goes setpoint → controller → actuator → room → sensor and then back. Noise from the sensor causes the most problems. The controller cannot find the difference between this noise and an error in the room. Thus it makes a correction for an error that does not occur.

> **DANGER: Filter at the source and make the dead-band wider**
>
> Filter the input of the controller at the output of the sensor, before the controller makes a decision. If you do not filter the input, each control loop in the room adjusts for noise. A wider dead-band and a filtered input frequently correct climate equipment that you think has a fault. The equipment has no fault.

## Expected results and limitations

Facilities go through stages in a set sequence. When you know your stage, you know the next step.

**1 · Blind**

No data and no method.

**2 · Logged**

Data but no method: much noise, and too many adjustments.

**3 · Filtered**

Filters and a sampling cadence. The change to this stage has the largest effect.

**4 · Controlled**

You adjust only for special causes.

**5 · Tuned**

Closed loop. The target is uniformity.

Most commercial rooms are at the **Logged** stage. A room at the Logged stage causes more stress to the grower than a room at the Blind stage, because the noise causes many alarms. The target is one stage up, and not the last stage in one step. The change from the Logged stage to the Filtered stage has the largest effect of all the steps in this paper. It uses only filters and a sampling cadence. It has almost no cost, and you must only do the same procedure each time.

Monitor _a small number of_ KPIs that have a high signal, and not forty instruments. The indicator that is the most related to commercial success is frequently **uniformity**. You measure it as the coefficient of variation of the batch, and not as the peak yield. Tests show that, when the variation of the environment in space and in time decreases (a lower coefficient of variation), the growth and the quality of the crop increase[^greenhouse-uniformity-crop-growth].Compare two batches. In the first batch, each plant has a yield of 95 g (3.4 oz). In the second batch, the average is 110 g (3.9 oz) and the range is 40 g (1.4 oz). The first batch has a higher commercial value.

| KPIs with a high signal: monitor these | Indicators with no value for decisions: ignore these |
| --- | --- |
| Grams for each kWh | Temperature from one sensor at one time |
| Dryback trend | Total quantity of data points recorded |
| Time in range for the VPD | Peak / record readings |
| DLI supplied compared with the target | Number of alarms |
| Batch coefficient of variation | Number of dashboards |

*The coefficient of variation measures the noise in your crop. In commercial production, uniformity is better than the peak yield.*

> **KEY: Summary**
>
> The target is a higher signal-to-noise ratio, and not a room with no noise. One stage up is the correct target. Filter before you adjust the room, and let a number that stays in its control limits change with no adjustment.

Next, read the paper [smart watering with VWC and EC](smart-watering-vrwe.html) to find how a clean, filtered signal controls the irrigation. Then read the paper [closed-loop control](closed-loop.html) to find how a closed loop operates with no hunting.

## References

[^shewhart-control-chart]: Control chart. Wikipedia. Describes Walter A. Shewhart's development of statistical process control at Bell Telephone Laboratories (1924), the distinction between common-cause and special-cause variation, and the convention of setting control limits at ±3 standard deviations from the process mean. https://en.wikipedia.org/wiki/Control_chart (source from a manufacturer or industry)
[^deming-funnel-tampering]: The Funnel Experiment. The W. Edwards Deming Institute. Demonstrates that adjusting (tampering with) a stable process in response to individual outcomes increases its variation rather than reducing it; leaving a stable process alone (Rule 1) yields the least variation. https://deming.org/explore/the-funnel-experiment/ (source from a manufacturer or industry)
[^western-electric-rules-anhoj]: Anhoej J, Wentzel-Larsen T. Sense and sensibility: on the diagnostic value of control chart rules for detection of shifts in time series data. BMC Medical Research Methodology. 2018;18:100. doi:10.1186/s12874-018-0564-0. Evaluates the Western Electric SPC control-chart rules for detecting non-random (special-cause) variation in sequential data. https://doi.org/10.1186/s12874-018-0564-0 (source with peer review)
[^nyquist-shannon-sampling]: Nyquist-Shannon sampling theorem. Wikipedia. States that perfect reconstruction of a band-limited continuous signal requires a sampling rate greater than twice the highest frequency present in the signal; under-sampling causes aliasing and irrecoverable information loss. https://en.wikipedia.org/wiki/Nyquist%E2%80%93Shannon_sampling_theorem (source from a manufacturer or industry)
[^replication-reduces-variance]: Blainey P, Krzywinski M, Altman N. Points of significance: Replication. Variation: use it or misuse it - replication and its variants. PMC3424707. Explains that the standard error of an estimate decreases with the square root of the number of replicates, so replication reduces measurement variance in proportion to sample size. https://pmc.ncbi.nlm.nih.gov/articles/PMC3424707/ (source with peer review)
[^bogena-soil-sensor-calibration]: Bogena HR, Huisman JA, Schilling B, Weuthen A, Vereecken H. Effective Calibration of Low-Cost Soil Water Content Sensors. Sensors (Basel). 2017;17(1):208. doi:10.3390/s17010208. Documents sensor-to-sensor variability and drift in low-cost permittivity-based soil moisture sensors, the two-step permittivity-to-water-content calibration, and large accuracy gains (RMSE reduced ~70%) from sensor-specific calibration. https://doi.org/10.3390/s17010208 (source with peer review)
[^roberts-ewma-1959]: Roberts SW. Control Chart Tests Based on Geometric Moving Averages. Technometrics. 1959;1(3):239-250. doi:10.1080/00401706.1959.10489860. Introduces the exponentially-weighted (geometric) moving average chart and shows it responds faster to small persistent process shifts than an ordinary moving average of equivalent smoothing. https://doi.org/10.1080/00401706.1959.10489860 (source with peer review)
[^greenhouse-uniformity-crop-growth]: Story of a paper: A Study of the Effects of Enhanced Uniformity Control of Greenhouse Environment Variables on Crop Growth. Energies. 2019;12(9):1749. doi:10.3390/en12091749. Shows that reducing spatial/temporal fluctuation (improving uniformity, i.e., lower coefficient of variation) of environment variables improves crop growth and quality. https://doi.org/10.3390/en12091749 (source with peer review)
[^snr-engineering-origin]: Signal-to-noise ratio. Wikipedia. Defines SNR as the ratio of signal power to background-noise power, a measure that originated in electrical/communications engineering and is now applied across telecommunications, imaging, and scientific measurement. https://en.wikipedia.org/wiki/Signal-to-noise_ratio (source from a manufacturer or industry)
