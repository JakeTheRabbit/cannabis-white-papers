---
slug: "closed-loop"
title: "Closed-loop grow room: levers, signals and plant state"
eyebrow: "Precision · Closed loop"
summary: "Operate a grow room as one system that corrects its errors. This basic paper shows the levers that you change and how to read the condition of the plants. It also shows how to send this information back to the levers without oscillation."
track: "Precision and automation"
read_time: "~17 min to read"
diagrams: "9 diagrams"
related: ["signal-and-noise", "plant-state-dashboard", "f2-crop-steering"]
url: "https://www.growlabs.nz/wiki/closed-loop.html"
md_url: "https://www.growlabs.nz/wiki/papers/closed-loop.md"
version: "1.2"
updated: "2026-07-18"
license: "CC BY-NC 4.0"
license_url: "https://creativecommons.org/licenses/by-nc/4.0/"
attribution: "The Cannabis White Papers"
refs: [{"id": "mohammed-spc-2024", "n": 1, "cite": "Mohammed MA. Statistical Process Control. Cambridge University Press (Elements of Improving Quality and Safety in Healthcare); 2024.", "url": "https://doi.org/10.1017/9781009326834", "peer": true}, {"id": "isa-18-2-alarm-mgmt", "n": 2, "cite": "International Society of Automation. ANSI/ISA-18.2-2016, Management of Alarm Systems for the Process Industries. ISA; 2016.", "url": "https://www.isa.org/standards-and-publications/isa-standards/isa-18-series-of-standards", "peer": false}, {"id": "moon-rootzone-ec-2018", "n": 3, "cite": "Moon T, Ahn TI, Son JE. Forecasting Root-Zone Electrical Conductivity of Nutrient Solutions in Closed-Loop Soilless Cultures via a Recurrent Neural Network Using Environmental and Cultivation Information. Frontiers in Plant Science. 2018;9:859.", "url": "https://doi.org/10.3389/fpls.2018.00859", "peer": true}, {"id": "huber-dli-co2-2021", "n": 4, "cite": "Huber BM, Louws FJ, Hernandez R. Impact of Different Daily Light Integrals and Carbon Dioxide Concentrations on the Growth, Morphology, and Production Efficiency of Tomato Seedlings. Frontiers in Plant Science. 2021;12:615853.", "url": "https://doi.org/10.3389/fpls.2021.615853", "peer": true}, {"id": "kim-co2-temp-light-msu", "n": 5, "cite": "Runkle E, Kim WS. Interactions of light, CO2, and temperature on photosynthesis. Michigan State University Extension, Floriculture & Greenhouse Crop Production; 2017.", "url": "https://www.canr.msu.edu/resources/interactions-light-co2-and-temperature", "peer": false}, {"id": "szerement-dielectric-2019", "n": 6, "cite": "Szerement J, Woszczyk A, Szyplowska A, Kafarski M, Lewandowski A, Wilczek A, Skierucha W. A Seven-Rod Dielectric Sensor for Determination of Soil Moisture in Well-Defined Sample Volumes. Sensors (Basel). 2019;19(7):1646.", "url": "https://doi.org/10.3390/s19071646", "peer": true}, {"id": "tdr-fdr-soil-review-2024", "n": 7, "cite": "Advancements in dielectric soil moisture sensor calibration: A comprehensive review of methods and techniques. Computers and Electronics in Agriculture. 2024;218:108663.", "url": "https://doi.org/10.1016/j.compag.2024.108663", "peer": true}, {"id": "choi-ec-transpiration-2015", "n": 8, "cite": "Choi KY, et al. Changes in electrical conductivity and moisture content of substrate and their subsequent effects on transpiration rate, water use efficiency, and plant growth in the soilless culture of paprika (Capsicum annuum L.). Horticulture, Environment, and Biotechnology. 2015;56(2):209-217.", "url": "https://doi.org/10.1007/s13580-015-0154-6", "peer": true}, {"id": "saure-tipburn-calcium-2001", "n": 9, "cite": "Saure MC. Calcium localization and tipburn development in lettuce leaves during early enlargement. Journal of the American Society for Horticultural Science. 2001 / related work on localized calcium deficiency and tipburn.", "url": "https://pubmed.ncbi.nlm.nih.gov/11543566/", "peer": true}]
---

# Closed-loop grow room: levers, signals and plant state

_Precision · Closed loop · ~17 min to read_

> Operate a grow room as one system that corrects its errors. This basic paper shows the levers that you change and how to read the condition of the plants. It also shows how to send this information back to the levers without oscillation.

## Purpose and scope

> **EVIDENCE: Weak**
>
> **Limit of the data:** The examples of lead time (tip burn in N days, the condition of the room in seconds) are examples for the dashboard. They are not results of tests at many cannabis sites. Use the method of the coupled system. Use the predictions as examples only, until you measure the rate of false positives in your facility.

A grow room is a **loop**. It is not a panel of controls with no connection to each other. You do not set the controls one time and then ignore them. You change a control, and the room and the plants change as a result. The sensors measure the change, and you examine the data. Thus you know the next change to make, and the cycle continues each minute of each day.

A thermostat is an example of a **closed loop**. When the room becomes too warm, the sensor measures the temperature and the air conditioner (AC) starts. When the temperature is correct again, the AC stops. The output of the system goes back to control the input of the system, and the cycle starts again.In a grow room, all the controls operate with the same method. The plant shows you the next change to make. Then you monitor the effect of the change.This paper shows the full cycle as one system. The cycle has three tasks. The task of _cause_ is to make the lever change correct. The task of _perception_ is to make the measurement accurate. The task of _cognition_ is to find the information in the data.

**A change has an effect on more than one part of the room.** Each change of a lever changes four connected balances at the same time: heat, water vapor, CO2 and the salt in the root zone. A full loop is a room that senses its condition and knows the effect of each change. It corrects its drift before the drift causes damage.

> **Diagram.** Read the diagram as a cycle. Each step goes to the next step. The last arrow, from Prescription back to Change, closes the loop.

> **KEY: The value of a closed loop**
>
> When the dashboard is good, a full loop tells you the condition of the room. It also tells you if you must change a lever quickly. When no change is necessary, the loop gives no alarms. This operation is correct. It is not a fault.

## Definitions

Many terms in this paper are new. This section gives a definition of each term that is necessary before the primary content. Most of the terms are easy, but their names are not easy. It is not necessary to know all the terms at this time. Each term occurs again in the paper.

**Lever (actuator)**: A control that you can change: the light intensity, the cooling setpoint, irrigation and CO2 supplementation. Approximately eleven primary groups of levers control a room.

**Signal and noise**: Signal is the information about the condition of the plant and the room. Noise is jitter of the sensor, scatter in the biology, and spikes that occur one time and give no information. Each reading is the sum of signal and noise.

**Setpoint and target**: A setpoint is a number in a controller. The controller tries to make the measurement agree with this number. For example, the controller decreases the air temperature to 24 °C (75 °F). A target is the result that you want. For example, the plant transpires at a correct rate. A setpoint and a target are not the same.

**VPD (vapor pressure deficit)**: The air can always absorb more water vapor. This quantity is the gap, and it is larger when the air is hotter and drier. VPD is the measurement of the gap, in kilopascals (kPa). When the gap is larger, the air removes water from wet leaf surfaces at a higher rate. When the VPD is higher, water goes from the plants to the air more quickly and the root zone dries more quickly. If the VPD is too high, the plants close their stomata to keep water.

**EC, VWC, dryback**: EC (electrical conductivity) is a measurement of the dissolved salt in the feed or in the root zone. When the substrate dries between shots, the plant absorbs water but the dissolved salts stay in the substrate. Thus the EC increases in each cycle. VWC (volumetric water content) is the quantity of water in the substrate. Dryback is the quantity by which the water content of the substrate decreases between two irrigation events.

**Plant state**: The condition of the plant, for example stress, generative steering or on-track. You calculate the plant state from many signals together. You do not read it from one sensor.

## Control levers and coupled effects

The room is one **coupled system**. It is not a set of controls with no connection to each other. When you increase the light intensity, you add more than light.You also add heat. The plants absorb and transpire water at higher rates, and the humidity increases. The plants use more CO2. The root zone dries more quickly, and the concentration of the salt in it increases more quickly[^huber-dli-co2-2021]. Light is a source of heat, a cause of transpiration, a cause of CO2 uptake and a load on the HVAC at the same time[^kim-co2-temp-light-msu].

Each change that you make has an effect on one or more of four **balances**: energy (heat), moisture (water vapor), carbon (CO2) and salt (root-zone EC). Approximately eleven primary groups of levers have an effect on these balances[^kim-co2-temp-light-msu]. Before a change, do not examine only the function of the lever. Find the balance on which the change has an effect. Make sure that all the other parts of the room can absorb the change.

> **Diagram.** One change has four effects. If you decrease the cooling setpoint, the humidity, the VPD, the dryback rate and the condensation risk also change together[^choi-ec-transpiration-2015].

> **Diagram.** The four balances become stable in very different times. As a result, the data can show no problem for some hours after a change to one lever. In this time, the change can add load to the slowest balance, with no sign that you can see[^moon-rootzone-ec-2018].

| Balance | Inputs | Outputs | The levers to change |
| --- | --- | --- | --- |
| **Energy** (heat) | Lights, equipment, sun load | AC, air exchange | Light intensity, cooling setpoint, airflow |
| **Moisture** (vapor) | Transpiration, irrigation | Dehumidifier, exhaust | Dehumidifier setpoint, VPD target, shot size |
| **Carbon** (CO2) | CO2 supplementation | Plant uptake, exhaust | CO2 setpoint, times of exhaust |
| **Salt** (root zone) | Feed EC, dryback | Plant uptake, runoff | Shot size and frequency, dryback target, feed EC, runoff % |

*The four balances and the levers that change each balance. The usual failures are failures of coupling. No part is defective.*

> **WARN: Usual failures occur when you do not set the levers together**
>
> Set the levers in the correct sequence. First, select the growth stage, the light intensity and the CO2 setpoint. These change the quantity of water and CO2 that the plants use. Then make the capacity of the climate system agree with this quantity. Then set the irrigation strategy for the root zone to agree with the climate.
> The usual failures occur when you set each lever and do not think about the other levers. Cooling can increase the humidity. A dehumidifier can add heat to the room. The exhaust can remove the CO2 that you add. In each of these examples, no part is defective.

## Sensor readings and the inference of plant state

You must _measure_ the changes in the room, and noise must not cause incorrect data. Then you must find the information in the data. Each measurement is signal plus noise. Usually, **many alarms from raw data are noise**. Remove this noise before you use an alarm for a decision[^isa-18-2-alarm-mgmt].

To read the plant state, go from a number to a decision. A number is ‘The VWC decreased by 12% during the night’. A decision is ‘The plant is in the generative steering that you want, and no change is necessary’ or ‘Decrease the dryback by 3% during the next night, or tip burn is possible in approximately 48 hours’. The task is to find the plant state. It is not only to show the data of the room.

To get the plant state, do these three steps in this sequence:

- **Set the correct speed of sampling** for the biology. Make the speed sufficient to measure the change that an irrigation event causes in 30 minutes. Do not make the speed high, because you cannot use the jitter that you record.
- **Remove the scatter** with a rolling average or a median filter before you examine the data.
- **Compare the data with control limits.** The control limits are values on the chart that you calculate from the recorded data of the room. Usually the values are the mean and approximately ±3 standard deviations (sigma)[^mohammed-spc-2024].

> **Diagram.** Raw data from a sensor change by a small quantity in each sample. The trend shows the changes in the room. The jitter does not show the changes in the room. If you change a lever because of jitter, you change it for a change in the room that did not occur.

> **Diagram.** A point between the control limits is common-cause variation, and you do not change a lever. A point that is more than a limit is special-cause variation. A group of points that are not random is also special-cause variation. Find the cause of each special-cause variation. Statistical process control is a method that finds the difference between common-cause variation and special-cause variation[^mohammed-spc-2024].

Then **use many readings, because one reading is not sufficient**. Use a group of 12 readings (n-of-12), not one reading (n-of-1). The only correct input to the inference is a clean signal with a classification.The inference uses sensor fusion on some clean signals to make named conditions. Each named condition has a value of confidence and an evidence chain. The inference compares the signals with a _learned envelope_ and not with a constant limit. A VPD of 1.4 kPa is correct at the end of flowering, but it causes stress at the start of vegetative growth.

> **Diagram.** A calm dashboard starts with one green label for the plant state (‘Flower Day 24, on-track, no change is necessary’). Yellow shows the precursors that drift. Orange is the only color that tells you to do a task. The graphs of raw data are last.

## Closed-loop diagnosis and corrective action

In this section, the three tasks operate as one system. Follow one usual problem through the full loop. The problem is **salt creep**. In salt creep, the dissolved salts slowly increase in the root zone, because each dryback cycle removes water but the salt stays.

1. **Cause makes the conditions**: A long dryback and a constant feed increase the salt concentration by a small quantity in each cycle. Thus the load on the slowest balance increases.
2. **Perception ignores noise**: Perception ignores one EC spike. But perception identifies a signal when the EC increases for four days and is more than the control limit.
3. **Cognition finds the information in the signal**: Cognition uses sensor fusion on this trend, the feed data and the dryback data. The result is a precursor with a name: ‘salt accumulation, tip-burn precursor’. The precursor has a value of confidence and an evidence chain.
4. **Prescription and change**: The loop sets the dryback lever to a smaller dryback. This change closes the loop approximately four days before you can see tip burn. The salt balance then starts to become correct again.

> **Diagram.** The EC at the roots increases when the substrate dries, long before the leaves show a change[^choi-ec-transpiration-2015]. Thus closed-loop correction finds salt accumulation in the root zone approximately four days before you can see tip burn[^saure-tipburn-calcium-2001].

> **NOTE: No task finds it without the other tasks**
>
> - A **lever-only** grower does not measure it.
> - A **signal-only** grower monitors a number that changes, but does not know the plant state.
> - A **dashboard-only** grower, with no model of cause and effect, gives a prescription for the incorrect lever.
> - Only the full loop has **self-correction**. No part has it without the other parts. The loop senses its errors and corrects them.

Bridge metrics let the three tasks send data to each other. The bridge metrics are dryback %, VPD, VPD-hours, pore-water EC and recovery slope. The system calculates each metric one time, with one definition. Each part of the loop reads the same value.Always **give a prescription with a number and show how you calculated it**. Give the lever change, the setpoint, the time limit and the result that the change will cause. The person who reads the prescription can open the full evidence chain when necessary. Do not make a black box.

| Failure | Cause or coupling | Signal method that finds it | Inference and prescription |
| --- | --- | --- | --- |
| Salt creep that you cannot see | Long dryback and constant feed | EC more than the limit for 4 days | Tip-burn precursor → decrease the dryback |
| The irrigation water does not go to the substrate | Blockage, pump fault or tubing fault | The VWC does not increase after the shot | Shot with no effect → apply the shot again, give an alarm |
| Morning stress that you cannot see | VPD spike at lights-on | VPD-hours more than the learned envelope | Morning stress → change the climate slowly |
| Slow failure of the dehumidifier | The capacity to remove water decreases | Drift trend of the RH, not a spike | Capacity fade → do maintenance before the failure |
| A sensor that does not measure the room | A probe with a constant signal or with noise | Very low variance, or jitter: special-cause variation | Defective probe → put it in quarantine, do not use its data |

*Five failures and one method: sensor fusion. A probe with a constant signal, with drift or with noise is also a special-cause signal that you can find[^szerement-dielectric-2019].*

## Procedure for closed-loop control

Make the loop one stage at a time. Do not start the next stage until the previous stage operates correctly. For almost all of this, it is not necessary to get new equipment. Most of it is a method.

1. **Part I: know the coupled effects of each change**: Before each change, identify the balances on which the change has an effect, and the direction of each effect. Think that each failure is a problem of capacity, or a problem of levers that you do not set together. It is not the fault of one lever.
2. **Part II: make your signals accurate**: Do not monitor each new reading, because it can cause you to change levers too much. Set a sampling cadence for each sensor. Put a rolling average on each chart that you use for decisions. Calculate the control limits from your recorded data.
3. **Part III: make decisions with inference**: Compare the data with a learned envelope for each cultivar, each growth stage and each photoperiod. Use sensor fusion before you give an alarm, because one signal is not sufficient. Make each advisory give a number and show its evidence chain. Make the system give no alarm when there is no problem.
4. **Close the loop last, and carefully**: At the start, let the system make only automatic changes with low risk. Make sure that you can change the lever back. For example, the system changes the dryback by 3 points after a person gives approval. A person must give approval for each change that has a high cost or that you cannot change back.

> **TIP: Method before equipment**
>
> The changes with the most value in this procedure have no cost: a sampling cadence, a rolling average and a control limit. Each of them is only a new method. Get equipment only after the method operates.

## Troubleshooting

Two failure modes make a loop defective: **use of noise as a signal** and **oscillation**. If you give noise (spikes, jitter and incorrect trends) to a controller, the controller changes levers for changes in the room that did not occur. The noise makes the room not stable. A loop that receives noise does not help. It makes the problem larger.Oscillation occurs when you change a lever too quickly or too much, or for readings that are in the usual variation. As a result, the values in the room increase and decrease, and do not become stable[^mohammed-spc-2024].

> **Diagram.** If you change a lever for each small change, oscillation starts in the room, and the room cannot become stable. A loop with a filter makes one correction, and only when the signal is more than a limit.

> **DANGER: Test before you change a lever**
>
> Change a lever only if all three of these conditions occur. First, the reading is not in its learned envelope (_cognition_). Second, this condition continues for more than one reading, and the sensors agree (_perception_). Third, you know a lever that corrects the reading without a change to a different balance (_cause_). If one condition does not occur, the reading is noise. Do not change a lever.

- **Aliasing**: if the sampling is too slow, you see incorrect trends. If the sampling is too frequent, you record jitter that you cannot use, and the jitter can cause tampering. Make the sampling cadence agree with the biology[^tdr-fdr-soil-review-2024].
- **The Stage-2 trap**: each new reading causes more stress for you than no data. The readings are a large quantity of noise, and they can cause you to make incorrect changes quickly.
- **Follow the loop, not the small change**: make the data sufficiently smooth to change levers with confidence. Do not make the data very smooth, because then you cannot see a fast change that is not noise. Keep the raw data available in one step.

## Expected results and limitations

> **KEY: The result is a smaller number of alarms, not more displays**
>
> When the loop operates correctly, you examine the dashboard at longer intervals. You have a smaller number of problems that occur without a sign, and the harvests have less variation. A screen with no alarms is the product, because it shows that no task is necessary. In the advisory-first stage, the loop gives you a prescription, but you change the lever. You can stay in this stage for the time that you want, because it is stable and it has value. Full automatic operation is optional and has approval steps.

> **Diagram.** The one change that gives the most value is the change from Stage 2 to Stage 3. Do not change levers for each new reading. Change levers for filtered trends that are more than the control limits. The only cost of this change is a new method, and you must do the change before all the higher stages.

- **Automation is not necessary to get good results.** The advisory is on the screen a long time before the system changes a lever without a person. If you stop at this point, the result is good and stable.
- **The numbers are only a start point.** The reference setpoints are values from commercial cultivation. Use them as a start point, and calibrate them with the recorded data of your facility. The method is correct for all facilities. You must find the setpoints for your facility.
- **Start with a small test.** Select one room and one type of failure. Operate the loop in shadow mode for one cycle. Measure the lead time of one advisory before you use the loop in more rooms.

First, know the coupled effects of your changes, make your signals accurate, and make your decisions with inference. Then, and only then, think about how to close the loop. For more information about the perception half, read the [signal and noise](signal-and-noise.html) paper. For information about the cognition half and how it gives the results to you, read the [plant-state dashboard](plant-state-dashboard.html) paper.

## References

[^mohammed-spc-2024]: Mohammed MA. Statistical Process Control. Cambridge University Press (Elements of Improving Quality and Safety in Healthcare); 2024. https://doi.org/10.1017/9781009326834 (source with peer review)
[^isa-18-2-alarm-mgmt]: International Society of Automation. ANSI/ISA-18.2-2016, Management of Alarm Systems for the Process Industries. ISA; 2016. https://www.isa.org/standards-and-publications/isa-standards/isa-18-series-of-standards (source from a manufacturer or industry)
[^moon-rootzone-ec-2018]: Moon T, Ahn TI, Son JE. Forecasting Root-Zone Electrical Conductivity of Nutrient Solutions in Closed-Loop Soilless Cultures via a Recurrent Neural Network Using Environmental and Cultivation Information. Frontiers in Plant Science. 2018;9:859. https://doi.org/10.3389/fpls.2018.00859 (source with peer review)
[^huber-dli-co2-2021]: Huber BM, Louws FJ, Hernandez R. Impact of Different Daily Light Integrals and Carbon Dioxide Concentrations on the Growth, Morphology, and Production Efficiency of Tomato Seedlings. Frontiers in Plant Science. 2021;12:615853. https://doi.org/10.3389/fpls.2021.615853 (source with peer review)
[^kim-co2-temp-light-msu]: Runkle E, Kim WS. Interactions of light, CO2, and temperature on photosynthesis. Michigan State University Extension, Floriculture & Greenhouse Crop Production; 2017. https://www.canr.msu.edu/resources/interactions-light-co2-and-temperature (source from a manufacturer or industry)
[^szerement-dielectric-2019]: Szerement J, Woszczyk A, Szyplowska A, Kafarski M, Lewandowski A, Wilczek A, Skierucha W. A Seven-Rod Dielectric Sensor for Determination of Soil Moisture in Well-Defined Sample Volumes. Sensors (Basel). 2019;19(7):1646. https://doi.org/10.3390/s19071646 (source with peer review)
[^tdr-fdr-soil-review-2024]: Advancements in dielectric soil moisture sensor calibration: A comprehensive review of methods and techniques. Computers and Electronics in Agriculture. 2024;218:108663. https://doi.org/10.1016/j.compag.2024.108663 (source with peer review)
[^choi-ec-transpiration-2015]: Choi KY, et al. Changes in electrical conductivity and moisture content of substrate and their subsequent effects on transpiration rate, water use efficiency, and plant growth in the soilless culture of paprika (Capsicum annuum L.). Horticulture, Environment, and Biotechnology. 2015;56(2):209-217. https://doi.org/10.1007/s13580-015-0154-6 (source with peer review)
[^saure-tipburn-calcium-2001]: Saure MC. Calcium localization and tipburn development in lettuce leaves during early enlargement. Journal of the American Society for Horticultural Science. 2001 / related work on localized calcium deficiency and tipburn. https://pubmed.ncbi.nlm.nih.gov/11543566/ (source with peer review)
