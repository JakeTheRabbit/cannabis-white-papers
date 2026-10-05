---
slug: "plant-state-dashboard"
title: "Design of a plant-state dashboard for your grow room"
eyebrow: "Precision · Dashboards"
summary: "We recommend that a grow-room screen shows the state of the plant, and not many numbers from the sensors. This paper shows how to make a screen that finds drift some days before it becomes damage, shows the cause and gives the next step."
track: "Precision and automation"
read_time: "~13 min to read"
diagrams: "11 diagrams"
related: ["signal-and-noise", "f2-crop-steering", "root-zone-teros12"]
url: "https://www.growlabs.nz/wiki/plant-state-dashboard.html"
md_url: "https://www.growlabs.nz/wiki/papers/plant-state-dashboard.md"
version: "1.2"
updated: "2026-07-18"
license: "CC BY-NC 4.0"
license_url: "https://creativecommons.org/licenses/by-nc/4.0/"
attribution: "The Cannabis White Papers"
refs: [{"id": "spc-signal-noise-ed", "n": 1, "cite": "Pimentel L, Barrueto F Jr. Statistical process control: separating signal from noise in emergency department operations. Journal of Emergency Medicine. 2015;48(5):628-638. doi:10.1016/j.jemermed.2014.12.019.", "url": "https://doi.org/10.1016/j.jemermed.2014.12.019", "peer": true}, {"id": "preattentive-dataviz", "n": 2, "cite": "Fusco R, Granata V, Setola SV, et al. Visual Perception and Pre-Attentive Attributes in Oncological Data Visualisation. Bioengineering. 2025;12(7):782. doi:10.3390/bioengineering12070782.", "url": "https://doi.org/10.3390/bioengineering12070782", "peer": true}, {"id": "vpd-plant-response", "n": 3, "cite": "Grossiord C, Buckley TN, Cernusak LA, Novick KA, Poulter B, Siegwolf RTW, Sperry JS, McDowell NG. Plant responses to rising vapor pressure deficit (Tansley review). New Phytologist. 2020;226(6):1550-1566. doi:10.1111/nph.16485.", "url": "https://doi.org/10.1111/nph.16485", "peer": true}, {"id": "capacitive-soil-moisture", "n": 4, "cite": "Briciu-Burghina C, Zhou J, Ali MI, Regan F. Demonstrating the Potential of a Low-Cost Soil Moisture Sensor Network. Sensors. 2022;22(3):987. doi:10.3390/s22030987.", "url": "https://doi.org/10.3390/s22030987", "peer": true}, {"id": "alarm-mgmt-isa182", "n": 5, "cite": "Engineering Equipment and Materials Users' Association (EEMUA). EEMUA Publication 191: Alarm Systems - A Guide to Design, Management and Procurement; and ANSI/ISA-18.2, Management of Alarm Systems for the Process Industries. (Industry standards; alarm-flood threshold ~10 alarms/10 min, <=3-4 priorities, <=5% high-priority.)", "url": "https://www.exida.com/articles/ALARM-MANAGEMENT-AND-ISA-18-A-JOURNEY-NOT-A-DESTINATION.pdf", "peer": false}]
---

# Design of a plant-state dashboard for your grow room

_Precision · Dashboards · ~13 min to read_

> We recommend that a grow-room screen shows the state of the plant, and not many numbers from the sensors. This paper shows how to make a screen that finds drift some days before it becomes damage, shows the cause and gives the next step.

## Purpose and scope

> **EVIDENCE: Weak**
>
> **Temporary:** The advisories on the screen (for example, the time before a tipburn risk) are examples of product design for operators. They are not a model for prediction that has validation.

A grow room has sensors for many values: the air temperature, the humidity, the VPD, the CO₂ and the light. The sensors also measure the moisture of the substrate, the EC, the root-zone temperature, the pH and the electrical power that the equipment uses. The sensors measure these values each second. The dashboards that show all of this have many numbers and graphs. They tell you the _values_ that occur. They do not tell you the _effect_ on the plant, the conditions that will occur next, or the task to do.

This paper shows a different method for the design of a dashboard. The name of this method is **Plant-State Intelligence**. The method gives a screen that calculates an estimate of the state of the plant, and does not only show the values for the room. The target is a ‘calm dashboard’: a dashboard that gives an advisory only when there is something important. Thus it has no signal for most of the time.A telemetry-dump dashboard makes the person put the information of fifteen graphs together and make a decision, frequently after a long day of work. A plant-state dashboard does this for you.

> **NOTE: Information about this paper**
>
> - This paper is a **guide for operations and product design**. It is not a paper on horticulture. The examples of lead time show a design for operators. They are predictions that have no validation. We recommend most of the designs in this paper. Examples show these designs.
> - The target is a screen with **inference** of the state of the plant, **prediction** of problems and **prescription** of the next step. The screen gives the prediction some days before the problems occur, with its evidence and confidence.
> - The paper starts from this: _a screen full of gauges is not a second person that helps you._

> **Diagram.** The telemetry-dump method (above) leaves all the work of the decision to the person. Plant-State Intelligence moves this work to the system: sensors → sensor fusion and inference → one decision that is easy to read.

## Definitions

These terms come before the other sections. It is not necessary that you know the terms at this time. Each term occurs again in the paper.

**Telemetry**: The measurements that your sensors send each second: temperature, humidity, moisture and other values. The data are as they come from the sensors, before you use them.

**VPD (vapor pressure deficit)**: The quantity of water vapor that you must add to the air to saturate it. This quantity changes the rate of transpiration of a plant. A VPD of 1.4–1.6 kPa is correct in the last stage of flowering. In the first stage of vegetative growth, it causes stress. The same number has a different effect at each stage.

**Crop steering**: The control of irrigation and dryback to make a plant **vegetative** (growth of leaves) or **generative** (flower and resin).

**Inference**: An estimate of a value that you cannot measure directly, for example plant stress. You calculate the estimate from some values that you can measure.

**Sensor fusion**: Some signals that you put together in a period of time to give one result. The signal ‘leaf temperature is higher’ is only noise. The signals ‘leaf temperature is higher _and_ transpiration is flat _and_ dryback is deeper than usual’ together are a diagnosis.

**Dryback**: The quantity by which the substrate dries between two irrigations. Two values for crop steering are the _dryback depth_ and the _dryback rate_. You calculate them from the sensor data. They are more important than a moisture number from a sensor.

**Leading indicator and lagging indicator**: A leading indicator is a precursor that gives a signal before damage occurs. A lagging indicator is a symptom that shows damage that occurred before.

**Baseline and trajectory**: The usual range of values for this cultivar, at this stage and at this time in the photoperiod. The range comes from the data of your previous cycles.

**PPFD / DLI**: PPFD (photosynthetic photon flux density) is the light intensity at one time. DLI (daily light integral) is the total light that the plants receive each day. EC is the concentration of salt in the feed or in the pore water of the root zone.

## Limits of dashboards with only sensor data

The usual dashboard uses one assumption that no person states: ‘show each measurement, and a good grower will know the task to do.’ This assumption causes seven frequent problems. Each sensor measures the **environment** of the plant (air, root zone, light). No sensor measures vigor, stress or transpiration directly. Thus the person must make the inference without aid. For example, capacitive moisture probes give the water content in the substrate, and not the water condition of the plant[^capacitive-soil-moisture].

The usual dashboard also shows a problem after it occurs. When a value is more than a threshold, the accumulation of salt, or a dryback that stops, started hours or days before. The alarms have constant high limits and low limits, and they give false alarms. They start for short changes, for example when a door opens or when the lights come on. Thus growers start to ignore the alarms.The alarm management standards of the process industry set the threshold of an alarm flood at approximately ten alarms in ten minutes. They set a maximum of approximately five percent for the most important alarms. The operator does not have trust in a grow-room dashboard that gives alarms continuously[^alarm-mgmt-isa182].

> **Diagram.** The seven problems of a telemetry-dump dashboard. In each problem, the person does a task that the system can do.

> **Diagram.** The pore-water EC increases slowly for four days, and the grower does not find a problem, until tipburn occurs on Day 26. A graph of one signal shows the cause at all times, but no person monitors that one graph at that time. A plant-state system decreases this interval[^spc-signal-noise-ed].

> **WARN: Gauges for one signal do not show the condition of the plant**
>
> Do not use only gauges for one signal. The information on the condition of the plant is in many signals together: moisture, EC, VPD and transpiration change together. Gauges for one signal cannot show these changes, also if you add many gauges.

## Six changes in the design of a plant-state dashboard

Plant-State Intelligence changes six assumptions of the sensor dashboard to the opposite. No change removes the sensor data. The data move to a lower position on the screen. You can continue to use the data when you want to examine a problem, also after the problem occurs.

| Axis | From: group of gauges | To: calm dashboard |
| --- | --- | --- |
| **Object** | Instruments: the dashboard shows the environment | Inference: the dashboard calculates an estimate of the state of the plant |
| **Reference** | Thresholds that do not change | Baselines from your data, for each cultivar, stage and photoperiod phase |
| **Inputs** | One signal for each gauge | Sensor fusion of many signals |
| **Time** | Lagging indicators (symptoms) | Leading indicators (precursors) |
| **Output** | Alarm: ‘a number changed’ | Prescription: task, time limit and result |
| **Mode** | Many graphs, always on | A signal only for unusual values. The standard state has no signal. |

*The six changes to the opposite. It is not easy to make the last change: the standard state has no signal.*

> **KEY: The grower must monitor the plant, and not the screen**
>
> A screen that always shows many graphs causes the grower to monitor the screen and not the plant. The grower must monitor the plant first. Thus a prescription replaces an alarm that only tells you that a number changed. A prescription gives the task, the time limit and the result if you ignore it. Thus a screen with no signal, and not a full screen, is the standard state when there is no problem.

## Plant-state inference model

The pipeline calculates estimates of four states that have an effect on each other. If you include the vision state, there are five states. The system shows the **environment state** (temperature, relative humidity, VPD, CO₂ and light) as totals in a period of time and as rates, and not as values at one time. Examples are the VPD-hours since the start of this day and the DLI to this time.The effect of VPD on a plant does not change at a constant rate. The effect increases with time and does not come from one reading[^vpd-plant-response]. Thus the total is the important quantity. The **substrate state** adds calculated values for crop steering. These calculated values are dryback depth, dryback rate, recovery to field capacity, and the change of the moisture after each shot.

No sensor measures the **plant state**. The system calculates an **estimate** of it with sensor fusion of the other states. The estimate has a transpiration proxy, a stress index, a vigor and stacking trajectory, and an output for the steering effect. The **operation and equipment state** and an optional **vision state** (canopy cameras) complete the model. The system uses the condition of the sensors as an important signal. Thus the system knows when the sensors give no correct data.

> **Diagram.** The environment, substrate, equipment and vision states go to the plant state estimate. This estimate is the state that is important to the grower, and no sensor gives it.

| Value from the sensor | Calculated value |
| --- | --- |
| WC = 42% | Dryback depth 8%, slower than the baseline for this cultivar |
| VPD = 1.5 kPa at this time | VPD-hours 18% more than the baseline range for the day |
| EC = 5.1 mS/cm | Pore-water EC increased on 4 days in sequence: risk of tipburn |
| Leaf temperature +0.6°C | Transpiration does not change, but the VPD is higher: the stomata close |

*The same number as a sensor value and as a calculated value. The values on the right are the information that a plant-state dashboard shows. The values on the left are at a lower position on the screen.*

> **TIP: The output is a short list of named conditions**
>
> This layer does not send fifteen numbers. It sends a short list of **named conditions**: ‘a dryback that stops’, ‘salt accumulation’, ‘high transpiration’. Each condition has a confidence and an evidence chain. Security cameras at the site can supply data for horticulture. They show the color and the uniformity of the canopy, and wilt at the start of the light period. They also show the height and the stacking in a period of some days, and a change of color in the first stage.

## Structure of a dashboard with six layers

The system is a pipeline with six layers. It agrees with a system that has Home Assistant in the middle. Most operations have layers 0 and 1, and the operators do not know it. The dashboard gets the inference a long time before the control of the equipment gets it. Autonomous control comes for one signal at a time, and only after the advisories for the signal are correct.

1. **Layer 0: Input**: Put all the data on the same timebase. Most rooms do this.
2. **Layer 1: Values**: Calculate new values from the sensor data: VPD, dryback %, DLI, recovery rates and the effect of each shot.
3. **Layer 2: Baseline**: Make baseline ranges for each cultivar, stage and photoperiod. Start with known values from horticulture, and make the ranges more accurate with the data of your cycles.
4. **Layer 3: Inference**: Use sensor fusion to make named conditions, with confidence and evidence. The methods are the conditions that you set, and tests for unusual values. You can also add a step in which an LLM examines the data.
5. **Layer 4: Prescription**: Connect each condition to a task with a time limit.
6. **Layer 5: Display**: The calm dashboard. The optional Layer 5b has a gate. It gives closed-loop control only for tasks that have low risk and that have your approval.

> **Diagram.** The pipeline, layer by layer. You can start the baselines of Layer 2 with the targets for horticulture in papers (the Athena targets are one example), before you have data from your room.

> **NOTE: Advisory-first is the design, not a limit**
>
> In this design, a person is in the loop. An operation can stay permanently at the ‘advise only’ stage and get most of the results. Layer 5b makes changes automatically only for tasks that have low risk and that have your approval. A person must give approval for each task that has a permanent effect or a high cost.

## Structure of the dashboard and its four zones

The screen that the grower opens has four zones, and the first zone is the most important. When the condition of the plant is correct, three of the zones are empty. Zone 1 is the **Headline**: one short sentence that is easy to read. It tells the condition of the plant, and it has a color that shows the condition. This sentence gives 90% of the information that a grower with much work must have, for 90% of the time.Zone 2 is the **Watchlist**, with the items that have drift but are not incorrect at this time (the precursors). The Watchlist makes advisories in the next zone not frequent. Zone 3 is **Advisories**, the only zone that sends a signal to the grower. Each advisory has a prescription with a time limit. Zone 4 is the zone for **evidence and sensor data**. It has a low position, but you do not remove it.

**Zone 1: Headline**

‘Flower Day 24 · Room 3 · Correct. The steering is generative, the same as the target. No task is necessary.’

**Zone 2: Watchlist**

Items with drift that are not incorrect at this time: the precursors. Each item is a sentence, and not a graph. Frequently empty.

**Zone 3: Advisories**

The only zone that sends a signal to the grower. Each advisory has a prescription with a time limit. It opens to show the evidence chain.

**Zone 4: Evidence and sensor data**

The previous dashboard, at a lower position. It has the signals after sensor fusion, baselines and graphs of sensor data. You use them to examine a problem, also after the problem occurs.

Color and layout are important here. You see the color, the position on the screen and the headline before you read the sentence. The name for this effect is pre-attentive processing[^preattentive-dataviz]. It is the group of visual properties that you receive automatically, before you select an item to examine. Thus you can see the ‘no problem’ state immediately, and you do not put the information from five panels together.

> **KEY: A full example of an advisory**
>
> ‘Decrease the dryback target by 3% in Room 3 (Day 24)… Tipburn is possible soon (example) without this change. Confidence: high. _[Show evidence]_’. The evidence opens to show the signals after sensor fusion, the baseline range and the values that are not in it, and a previous example. The previous dashboard was 100% Zone 4. The new dashboard starts with Zones 1–3 and keeps Zone 4 at a low position.

## Installation procedure

It is not necessary to assemble all the system again. Each stage gives results and makes the next stage possible. Most of the results occur by Stage 3, a long time before closed-loop control.

> **Diagram.** Six stages from telemetry to closed loop. Stage 2 (the baseline, with no false alarms) is the largest step, because it stops alarm fatigue in one step.

1. **Select one room and one type of problem**: Select one type of problem (for example, a dryback that stops). Install Stages 1–3 in Home Assistant for only this type of problem.
2. **Operate it in shadow mode for one cycle**: Operate the system with the dashboard that you have for a full cycle. Do not use its advisories to do tasks. Examine if each advisory is correct.
3. **Show the lead time**: Measure the time between the advisory and the time at which you can see the problem. Show this on one advisory before you use the system in more rooms.
4. **Add one type of problem at a time**: Add the next type of problem, then the next room. Stage 4 (prescription) and Stage 5 (closed loop) are optional, for one signal at a time.

> **TIP: Stage 4 is a stable last stage**
>
> You do not have to go from the advisory-first method to a different stage. An operation can stay at Stage 4 permanently and get most of the results. Stage 5 (closed loop) is optional, and it has a gate for tasks with low risk that have your approval.

## Trust, confidence and types of problem

An advisory system that is incorrect _and_ has high confidence is worse than no system. Trust is a balance. Each incorrect advisory decreases the trust, and each correct advisory increases it. Thus the **precision** of the advisories, and not the number of advisories, causes the grower to do a task. Five guardrails are necessary.

| Guardrail | Problem that it prevents | Mechanism |
| --- | --- | --- |
| Show low confidence at cold start | Too much confidence from the data of one cycle | Start with known values from horticulture. Make the confidence ranges larger. Put the label ‘data not sufficient’ on the outputs. |
| Easy to correct | The grower does not want the system after incorrect advisories | The grower can remove each advisory and identify it as a false positive. The identifications adjust the baselines. |
| Monitor precision | A drift in quality with no signal | The precision of the advisories and the false-positive rate are important values that the grower can see. |
| Person in the loop | Errors with a permanent effect or a high cost | A person gives approval for each task with a high cost or a permanent effect |
| Not a black box | No trust in the advisory | Each advisory opens to show its evidence chain |

*The five guardrails. Each guardrail prevents one problem that decreases the trust of the grower in an advisory system.*

> **DANGER: A sensor problem is an advisory**
>
> Make an advisory for a sensor that has drift, noise or a flat signal. For example: ‘The EC probe in Room 2 gives a flat value, and this value is not possible: the probe can be defective, and the system stops the advisories from EC.’ If a grower cannot see the _cause_ of an advisory, the grower will, correctly, have no trust in the _advisory_. The system must make the decision easy for the grower to see. A person must make the decision for a task with a permanent effect or a high cost.

## Expected results and limitations

When the new dashboard operates correctly, the grower monitors it **less**, has **less** damage with no advisory, and gets harvests with **more uniformity**. Six key performance indicators (KPIs) from one cycle to the next show this. For three of them, the target direction is _down_.

> **Diagram.** A good target profile for the six KPIs. We recommend high values for lead time, precision and the number of decisions each week. We recommend low values for damage with no advisory, screen time and result variance.

- **Lead time**: the time (hours or days) between an advisory and the time at which you can see the problem. Lead time is the primary KPI. The system must find drift before it causes damage.
- **Damage with no advisory**: damage that you can see, with no advisory before it. Decrease this to zero.
- **Advisory precision**: the number of advisories that the grower used for a task, divided by the total number of advisories. Also monitor the false-positive rate.
- **Screen time**: the time that the grower monitors the dashboard. A lower value is better. The grower must monitor the plants and not the screen.
- **Decisions each week**: the number of decisions that the dashboard gives in one week. The output is decisions, and not views of the screen.
- **Result variance**: the variation of yield and quality from one cycle to the next.

> **KEY: Closed-loop control is optional**
>
> Most of the results occur by Stage 3. It is possible that advisory-first is the correct permanent last stage. You do not have to use closed-loop control. The names in this paper (Plant-State Intelligence, ‘calm dashboard’) are only temporary names. The content is more important than the name.

Start with a small system. Make the inference layer that finds drift in the first stage. Refer to the [signal-and-noise](signal-and-noise.html) paper for the statistics that it uses. Give the layer the calculated values for crop steering from [f2 crop steering](f2-crop-steering.html). The dashboard is only as good as the states that it uses.

## References

[^spc-signal-noise-ed]: Pimentel L, Barrueto F Jr. Statistical process control: separating signal from noise in emergency department operations. Journal of Emergency Medicine. 2015;48(5):628-638. doi:10.1016/j.jemermed.2014.12.019. https://doi.org/10.1016/j.jemermed.2014.12.019 (source with peer review)
[^preattentive-dataviz]: Fusco R, Granata V, Setola SV, et al. Visual Perception and Pre-Attentive Attributes in Oncological Data Visualisation. Bioengineering. 2025;12(7):782. doi:10.3390/bioengineering12070782. https://doi.org/10.3390/bioengineering12070782 (source with peer review)
[^vpd-plant-response]: Grossiord C, Buckley TN, Cernusak LA, Novick KA, Poulter B, Siegwolf RTW, Sperry JS, McDowell NG. Plant responses to rising vapor pressure deficit (Tansley review). New Phytologist. 2020;226(6):1550-1566. doi:10.1111/nph.16485. https://doi.org/10.1111/nph.16485 (source with peer review)
[^capacitive-soil-moisture]: Briciu-Burghina C, Zhou J, Ali MI, Regan F. Demonstrating the Potential of a Low-Cost Soil Moisture Sensor Network. Sensors. 2022;22(3):987. doi:10.3390/s22030987. https://doi.org/10.3390/s22030987 (source with peer review)
[^alarm-mgmt-isa182]: Engineering Equipment and Materials Users' Association (EEMUA). EEMUA Publication 191: Alarm Systems - A Guide to Design, Management and Procurement; and ANSI/ISA-18.2, Management of Alarm Systems for the Process Industries. (Industry standards; alarm-flood threshold ~10 alarms/10 min, <=3-4 priorities, <=5% high-priority.) https://www.exida.com/articles/ALARM-MANAGEMENT-AND-ISA-18-A-JOURNEY-NOT-A-DESTINATION.pdf (source from a manufacturer or industry)
