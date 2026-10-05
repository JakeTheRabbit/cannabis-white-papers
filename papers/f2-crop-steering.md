---
slug: "f2-crop-steering"
title: "F2 crop steering: the manual for operation each day"
eyebrow: "Precision · Crop steering"
summary: "After you read this paper, you can prepare, calibrate and operate an automatic irrigation controller for a grow room for the vegetative stage. The paper gives information about the P0 to P3 cycle of each day and the targets for moisture and salt. It also gives information about the controls that you use each day and the safety fail-safes in the system. It shows how to find the cause of a fault."
track: "Precision and automation"
read_time: "~18 min to read"
diagrams: "12 diagrams"
related: ["coco-crop-steering", "root-zone-teros12", "smart-watering-vrwe"]
url: "https://www.growlabs.nz/wiki/f2-crop-steering.html"
md_url: "https://www.growlabs.nz/wiki/papers/f2-crop-steering.md"
version: "1.2"
updated: "2026-07-18"
license: "CC BY-NC 4.0"
license_url: "https://creativecommons.org/licenses/by-nc/4.0/"
attribution: "The Cannabis White Papers"
refs: [{"id": "caplan-drought-2019", "n": 1, "cite": "Caplan, D., Dixon, M., & Zheng, Y. (2019). Increasing Inflorescence Dry Weight and Cannabinoid Content in Medical Cannabis Using Controlled Drought Stress. HortScience, 54(5), 964-969.", "url": "https://doi.org/10.21273/HORTSCI13510-18", "peer": true}, {"id": "zawilski-calibration-2023", "n": 2, "cite": "Zawilski, B. M., Granouillac, F., Claverie, N., Lemaire, B., Brut, A., & Tallec, T. (2023). Calculation of soil water content using dielectric-permittivity-based sensors - benefits of soil-specific calibration. Geoscientific Instrumentation, Methods and Data Systems, 12, 45-56.", "url": "https://doi.org/10.5194/gi-12-45-2023", "peer": true}, {"id": "qi-salinity-2024", "n": 3, "cite": "Qi, Q., Yang, H., Zhou, Q., Han, X., Jia, Z., Jiang, Y., Chen, Z., Hou, L., & Mei, S. (2024). Performance of Soil Moisture Sensors at Different Salinity Levels: Comparative Analysis and Calibration. Sensors, 24(19), 6323.", "url": "https://doi.org/10.3390/s24196323", "peer": true}, {"id": "kang-rootgrowth-2019", "n": 4, "cite": "Kang, S., van Iersel, M. W., & Kim, J. (2019). Plant root growth affects FDR soil moisture sensor calibration. Scientia Horticulturae, 252, 208-211.", "url": "https://doi.org/10.1016/j.scienta.2019.03.052", "peer": true}, {"id": "mohammed-spc-2024", "n": 5, "cite": "Mohammed MA. Statistical Process Control. Cambridge University Press (Elements of Improving Quality and Safety in Healthcare); 2024.", "url": "https://doi.org/10.1017/9781009326834", "peer": true}]
---

# F2 crop steering: the manual for operation each day

_Precision · Crop steering · ~18 min to read_

> After you read this paper, you can prepare, calibrate and operate an automatic irrigation controller for a grow room for the vegetative stage. The paper gives information about the P0 to P3 cycle of each day and the targets for moisture and salt. It also gives information about the controls that you use each day and the safety fail-safes in the system. It shows how to find the cause of a fault.

## Purpose and scope

> **EVIDENCE: Weak**
>
> **Grower method and temporary values:** The default VWC values are the values of one facility. They are start points. They are the readings of the probes, in the units that the probes supply, after a person applies water by hand. The drought test of Caplan gives data for the general method of a controlled water deficit. It does not give data for the values of these setpoints. Calibrate the substrates before you arm the automation.

F2 is an **automatic irrigation controller** for a grow room for the vegetative stage. It is software that reads the probes for moisture and salt in the root zone. The software selects the time to start each shot of water automatically, and it supplies the water through a pump and valves. You set the targets. The software applies the water.

**Crop steering** is a method in which you select the water content and the salt content of the root zone. The selection changes the type of growth that is primary in the plant. For a plant that is not in cultivation, a drought is a signal that the time is short. The plant then changes to reproduction. The system gives this signal with a controlled dose, at a controlled time._Vegetative_ steering (bulking) keeps the substrate wet. It uses many small shots and a small dryback. _Generative_ steering (flower steering or stress steering) uses a larger dryback, more salt in the root zone, and a smaller number of larger shots. A small, controlled water deficit at the correct time is sufficient to cause a cannabis plant to change to generative growth. The yield does not decrease.[^caplan-drought-2019]

The system has two software layers that operate together. A **Home Assistant integration** gives you each control and each reading on the screen. An **AppDaemon engine** (`master_crop_steering_app.py`) makes the decisions and starts the shots. The room has **3 rows (zones)**. Each row has one probe for moisture and salt and one valve. One tank, one pump and one main line supply all the rows.

> **Diagram.** The two software layers and the hardware that they operate. The controls go from the dashboard to the hardware. The probe readings go back from the hardware to the dashboard.

> **Diagram.** One tank, one pump and one main line supply three rows. You control each row independently. Each row has one probe pair and one valve.

> **KEY: Two important facts**
>
> - The **‘Phase (manual set)’** list _overrides_ the automatic phase. It shows the phase that you selected last, not the phase that is in operation at this time. To see the correct phase, read `sensor.crop_steering_current_phase`.
> - It is always safe to disarm the system. When you set `switch.crop_steering_system_enabled = OFF`, no shot can start.

## Definitions

The system uses three measurements for all its operation. Read these definitions first, because all the other sections use them.

**VWC (volumetric water content)**: The substrate contains water and air. Water fills some of the space in the substrate, and air fills the remaining space. VWC is the quantity of water at this time, as a percentage of the volume of the substrate. If the VWC is 60%, water fills 60% of the volume of the substrate. All irrigation decisions start from this number.

**EC (electrical conductivity)**: When the water contains dissolved salt, the roots cannot absorb the water easily. The EC measurement gives the quantity of dissolved salt in the solution, in mS/cm. The sensor measures how easily electric current flows through the solution. A higher EC shows a stronger solution with more salt. A lower EC shows a weaker solution.

**Dryback**: After each shot, the plant uses water, and the substrate becomes dry slowly. The VWC is at its highest value (the peak) immediately after a shot and at its lowest value immediately before the next shot. Dryback is the difference between these two values, as a percentage of the peak. A larger dryback causes more generative growth. A smaller dryback causes the plant to continue vegetative growth. This difference is the primary control for steering.

**Shot**: One short period of water supply. The size of a shot is a percentage of the volume of the substrate. The system calculates the shot time in seconds from the substrate volume, the dripper flow rate and the shot size.

**Field capacity**: The peak VWC. The water saturates the substrate, and then the water that the substrate cannot hold flows out. It is the ‘full’ value of the substrate.

**EC ratio**: Divide the measured EC by the target EC. The result is the EC ratio. A ratio of more than 1 shows that the solution has too much salt. Thus apply more water to dilute the solution. A ratio of less than 1 shows that the solution is too weak. Thus apply less water.

**Vegetative mode and generative mode**: The two steering modes. Each mode has a different set of dryback targets and EC targets. The engine adjusts the irrigation to make the values the same as these targets.

**Zone and phase**: A zone (a row) is one of the 3 sections that you control independently. A phase is the part of the P0 to P3 cycle of each day that a row is in at this time.

> **Diagram.** The three numbers that the system reads for each decision: how much water, how much dryback, and how much salt.

## The P0–P3 cycle of each day

Each row has four phases during each day. The light schedule controls the phases (the default times are 10:00 for lights on and 22:00 for lights off). The sequence is always the same. First, the substrate dries a small quantity. Then the system fills the substrate again and keeps the VWC stable. At night, the VWC decreases.

- **P0 (morning dryback):** After the lights come on, the system does not apply water. The substrate dries a small quantity (`p0_dryback_drop_percent`, for example 5 to 10%). P1 starts when the dryback is equal to this target, or after the maximum time (`p0_maximum_wait_time`). The default is 120 min.
- **P1 (ramp-up):** The first shot has the size `p1_initial_shot_size`. Each shot is larger than the shot before by `p1_shot_size_increment`, to a maximum of `p1_maximum_shot_size`. The time between shots is `p1_time_between_shots`. The phase has a minimum number and a maximum number of shots. The phase stops when the VWC is equal to or more than `p1_target_vwc`.
- **P2 (maintenance):** This phase is most of the day. The system applies water when the VWC becomes less than `p2_vwc_threshold`. If the EC ratio is more than approximately 1.2, the system applies more water to dilute the solution. If the EC ratio is less than approximately 0.8, the system applies less water.
- **P3 (night):** Usual irrigation stops a number of minutes before the lights go off. You set this number with `p3_veg_last_irrigation` / `_gen_`. Only emergency shots start when the VWC is less than `p3_emergency_vwc_threshold`. The zones stay in P3 all night.

> **Diagram.** The curve shows one day with steering. The VWC has a small dryback in the morning and then increases to the target. Then it stays in a maintenance range, and at night it decreases at a controlled rate.

> **Diagram.** A row operates in the loop in this sequence: P3 at night, P0 at lights on, P1, P2, and then P3 again before lights off.

The two steering modes select the targets that the engine uses. **Vegetative** steering has a high VWC, a small dryback (approximately 10 to 20%), a lower EC (approximately 3.0 mS/cm), and many small shots. **Generative** steering has a lower VWC, a larger dryback (approximately 25 to 50%), a higher EC (approximately 4.5 to 6.0 mS/cm), and a smaller number of larger shots. Set the mode for all rows with `select.crop_steering_steering_mode`, or set the mode for each row. A setting for one row overrides the setting for all rows. With ‘Follow Main’, the row uses the setting for all rows.

| Mode | VWC target | Dryback | EC target | Shots |
| --- | --- | --- | --- | --- |
| **Vegetative** | High | Small (10 to 20%) | Approximately 3.0 mS/cm | Many small shots |
| **Generative** | Lower | Large (25 to 50%) | 4.5 to 6.0 mS/cm | A smaller number of larger shots |

*The two modes of steering. Select one mode for each row, or set a row to use the setting for all rows.*

## Irrigation controls and targets

Each day, you use some controls. Two arm switches set how much of the system operates. **System enabled** is the primary arm switch. When it is OFF, no irrigation can occur. If the engine cannot read the switch, it uses OFF as a fail-safe.**Auto irrigation** controls only the shots that the engine starts. When it is OFF, you can continue to start manual shots. These two settings give ‘watch mode’.

Some targets control the growth: the VWC values for each phase (`p1_target_vwc`, `p2_vwc_threshold`) and the dryback targets. The EC targets for each phase and each mode (`ec_target_veg_p0..p3` and `ec_target_gen_p0..p3`) also control the growth. The selection lists for each row let you use generative steering in one row and vegetative steering in the other rows. They also let you select the row that receives water first when only one row can start a shot. You can also make groups of zones to control the zones together.

- When the **EC stacking switch** is ON, the engine can apply less water to increase the EC of the root zone. This setting gives generative steering. The switch is usually OFF for vegetative steering.
- **Hardware that you can see:** the pump (Tuya plug, approximately 490 W when it operates), the relay of the main line, and the zone valves `switch.f2_row1/2/3`. Only one zone receives water at a time.
- **Selection lists for each row:** steering_mode, crop_profile (Follow Main and 7 profiles), group (A to D), and ‘priority’ (‘Critical’, ‘High’, ‘Normal’ or ‘Low’).
- **The system calculates the shot time** from `substrate_volume`, `dripper_flow_rate`, `drippers_per_plant` and the shot size in %. Set these values correctly. If you do not, each shot has an incorrect size.
- **Safety limits for each row:** `max_daily_volume` (L), `shot_size_multiplier`, and `plant_count`.

| System enabled | Auto irrigation | Result |
| --- | --- | --- |
| ON | ON | Usual operation. The engine starts automatic shots, and manual shots also operate. |
| ON | OFF | **Watch mode**: The system is armed, but it only monitors. Only manual shots operate. |
| OFF | ON or OFF | The system is fully disarmed. The gate stops each shot. |

*The two types of ‘off’. For watch mode, set System enabled to ON and Auto irrigation to OFF. Do this while you calibrate.*

> **TIP: Use watch mode before automatic operation**
>
> Set **System enabled to ON and Auto irrigation to OFF** while you make sure that your numbers are correct. The engine is armed and calculates its decisions, but it does not start shots automatically. You can start manual test shots and monitor the changes in the room before you let the engine operate with full automatic control.

## Irrigation decision gates

When the engine makes the decision that a shot is necessary, the shot starts only if **all the safety gates, in sequence,** let it start. Each gate can stop the shot. The gates prevent an incorrect decision of the automatic system.

> **Diagram.** The next gate operates only after the gate before it lets the shot start. The hardware sequence starts only after the last gate.

- **Sequence of the gates for a shot:** First, the system is armed. Then Auto irrigation is ON (manual shots bypass this gate). Then the zone is ON and has no manual override. Then no dose is in progress, and the tank is not empty. Then the source pH and EC are in range (default pH 5.8 to 6.2). The last gates are the safety limits: the limit of volume for each day, the maximum EC and the maximum frequency.
- **pH or EC not in range:** The gate stops the shot and sends an alert to the phone. The alert has an ‘Irrigate Anyway’ button.
- **Tank guard:** The guard stops a shot only when the low float reads empty. As a result, the system can continue to apply water while the quantity of water in the tank decreases.

> **Diagram.** The sequence of the hardware when the system applies water. First the pump makes pressure. Then the system opens the valve of the row and keeps it open for the calculated time. At the end, the components stop in the opposite sequence.

> **NOTE: The effect of source water without a gate**
>
> Source water can change slowly to a pH or an EC that is not in the range of the gate. This water can cause nutrient lockout or cause damage to the roots. The gate stops the shot and sends an alert to you. Thus the system does not apply a solution with an incorrect pH or EC to the room without an alert.

## Calibration procedure

Calibration is the most important step in the procedure. The system operates correctly only if its number entities agree with the values of _your_ substrate. The factory defaults are temporary values (50% VWC and 50% dryback). They are not values for your substrate. Dielectric probes for moisture give different readings in each substrate. Thus a calibration for the substrate is necessary before the numbers give correct information about the substrate.[^zawilski-calibration-2023]

1. **Monitor**: Use your usual procedure to apply water by hand for a small number of days. Monitor the VWC of each row. The reading immediately after you apply water is approximately the field capacity (the peak). The reading immediately before the next time that you apply water is the trough. Together they show the range of operation of that row.
2. **Set the range**: Set `field_capacity` to a value that is a small quantity more than the highest peak. Set `p1_target_vwc` to the peak of each row after you apply water. Set `p2_vwc_threshold` to a value that is less than this peak by a small number of percent. A smaller difference between these two values gives a smaller range for vegetative steering.
3. **Set the drybacks**: For vegetative steering, set the dryback to approximately 15 to 20%. For generative steering, set the dryback to approximately 25 to 45%. Set `p0_dryback_drop_percent` to 5 to 15%. Set the emergency floor to a value that is less than the usual trough by a small number of percent.
4. **Set EC targets**: For vegetative steering, set the EC target to a value that is a small quantity more than the feed EC. For generative steering, set it to a value that is much more than the feed EC. The values `p2_ec_high/low_threshold` are multipliers of the target. At 1.2, the engine dilutes the solution when the EC is more than 120% of the target. At 0.8, the engine applies less water when the EC is less than 80% of the target.
5. **Operate and adjust**: Let the system operate for some cycles in watch mode. Compare the values that the system calculates with the values that the probes measure. Adjust the numbers to make them more accurate.

> **Diagram.** The range that you read when you apply water by hand. The emergency floor is below the trough. The P2 range is below the P1 target. Field capacity is the limit at the top.

The growth of the roots changes the readings of the probe during a crop. Thus examine the range at intervals. Do not calibrate one time only.[^kang-rootgrowth-2019]

| Setting | Row 1 | Row 2 | Row 3 | Function |
| --- | --- | --- | --- | --- |
| p1_target_vwc | 26 | 22 | 18 | The peak VWC. P1 fills the substrate again to this value. |
| p2_vwc_threshold | 22 | 19 | 15 | Apply water when the VWC becomes less than this value. |
| vegetative_dryback_target | 18 | 18 | 18 | The quantity by which P0 dries the substrate (%) |
| p0_dryback_drop | 8 | 8 | 8 | The quantity of dryback in the morning (%) |
| emergency floor | 15 | 14 | 11 | The VWC that starts an emergency shot in P3 at night |
| field_capacity (for all rows) | 30 | 30 | 30 | The VWC peak at saturation (the ‘full’ value) |

*The start numbers for F2 that the source recommends. The source calculated these numbers from the ranges that it recorded when it applied water by hand. They are start points, not permanent settings.*

> **WARN: The defaults are temporary values, not values for your substrate**
>
> Calibrate first, then arm the system. If you use the factory defaults (50% and 50%) without calibration, the engine uses numbers that are not related to your substrate. As a result, the steering has no value.

## Procedures for usual operation

Most usual tasks have a safe procedure. We recommend that you use the services of the integration and not the hardware switches directly. The services start the full hardware sequence with all the gates. As a result, the system always does the safety checks.

| Task | Safe method | Information |
| --- | --- | --- |
| Start a manual shot | Use the service `crop_steering.execute_irrigation_shot` (zone, duration_seconds, shot_type: manual) | Starts the full sequence with all the gates |
| Hardware directly (use it only if no other method is possible) | Pump → main line → valve ON. To stop, set the components OFF in the opposite sequence. | Only one row at a time |
| Set a phase by hand | Change `select.crop_steering_irrigation_phase` | The change occurs immediately. It bypasses the usual changes of phase. The list then shows that phase. |
| ‘Irrigate Anyway’ override | The button on the phone after an alert for pH or EC | It bypasses only the pH/EC gate, for 30 min. It stops automatically when the readings are again in range. |
| Remove a row from the steering, or set a row to manual override | `zone_N_enabled` OFF (the row is not in the steering), or `zone_N_manual_override` ON (the row stays in the steering) | Manual override: you apply water by hand while the row stays in the steering |
| Use generative steering | Select ‘Generative’ in the steering mode (for all rows or for one row) | The setting for one row overrides the setting for all rows |
| Set the water counters to zero | Automatic: each day at midnight and each week on Monday | To set the counters to zero before this time, stop AppDaemon and start it again |

*A reference for the tasks that you do most frequently. If you are not sure, use the service and not the hardware switch.*

> **NOTE: ‘Irrigate Anyway’ bypasses only one gate**
>
> It bypasses the _pH/EC gate only_ for 30 minutes. All the other interlocks continue to operate: system armed, tank not empty, and the limit of volume for each day. It stops automatically when the pH and EC are in range again.

## Safety interlocks and troubleshooting

The system has some fail-safes: the pH/EC gate for the source water, a tank dry-run guard, and a blocked-dripper guard. The system also has a fail-safe for the arm switch and a recorded condition. The tank dry-run guard stops a shot only when the low float reads empty. The blocked-dripper guard stops a row for 2 hours after too many shots that fail.If the system cannot make sure of the condition of the arm switch, it uses the value OFF. The system records its condition at intervals of 5 minutes. After the system starts again, each zone starts in its recorded phase.

> **DANGER: The EMERGENCY button does NOT disarm the engine**
>
> To stop the system for more than a short time, use the EMERGENCY button and set **System enabled** to OFF. The dashboard button **EMERGENCY, ALL OFF** (`script.f2_irrigation_all_off`) quickly stops the three hardware components, but the engine stays _armed_. The engine can start the components again at its next check of the phase, in approximately 60 s. To disarm the engine, set **System enabled** to OFF.

| Trigger | Effect | Condition of the engine after |
| --- | --- | --- |
| Dashboard EMERGENCY button | Quickly stops the pump, the main line and the valves | The engine is ARMED. It can start shots again at the next check in approximately 60 s |
| System enabled OFF | The gate stops each shot | DISARMED, and the engine stays in this condition |
| Automatic emergency stop of the engine | Internal. The engine stops the row that has the fault | ARMED. The row with the fault stays stopped |

*Two methods to stop, and the condition of the engine after each method. Only System enabled OFF keeps the engine disarmed.*

1. **Repair the cause**: First, repair the problem in the hardware. Examples are an empty tank, a bent line, a defective probe and a blockage in a dripper.
2. **Make sure that the hardware is OFF**: Make sure that the pump, the main line and all the valves show OFF.
3. **Examine the arm condition of the engine**: Examine System enabled and Auto irrigation before you arm the engine again.
4. **Arm the engine again and do a check**: Arm the engine again. Then read `sensor.crop_steering_current_phase` to see the phase that is in operation.
5. **Monitor one cycle**: Do not go away. Monitor a full cycle. Make sure that each shot starts correctly. Then you can use the system in automatic operation again.

| Symptom | Possible cause | Procedure |
| --- | --- | --- |
| Zones stay in one phase | The condition for the change to the next phase does not occur, or the target is incorrect | Compare the exit threshold of the phase with the VWC at this time |
| The valve is open, but there is no flow | The pump is OFF, the line is bent, or there is a blockage in a dripper | Examine the pump and the line. Remove the blockage in the dripper. |
| The Status value or the Water-today value is ‘unknown’ | The engine does not operate, or the sensors have no data | Stop AppDaemon and start it again. Make sure that the probes send readings. |
| Frequent alerts for pH or EC | The source water is not in range, or the sensor has drift | Do a test of the solution. Make sure that the pH/EC probe is correct. |
| The blocked-dripper guard stops a row many times | 4 or more shots that fail in 30 min | Remove the blockage in the dripper. The row starts again automatically after 2 h. |
| ‘Irrigation already in progress, skipping’ in each cycle | A flag stays ON after a shot stops before its end | Stop AppDaemon and start it again (`ha addons restart a0d7b954_appdaemon`). The system reads the phase and the counters from the disk. |

*The list of troubleshooting steps from the source. Most faults have a cause in the hardware or a flag that stays ON.*

> **WARN: A gap in the data to monitor**
>
> Examine the calibration of the probe before you use EC steering. The source shows that `sensor.crop_steering_dryback_percentage` and the substrate EC can give values that are too low to be correct (Row 1 at 0.48 mS/cm). Salinity has a strong effect on the readings of dielectric probes.[^qi-salinity-2024]

## Expected results and limitations

> **KEY: This is a controller, not a system that does all tasks**
>
> - **The limit of the quality of the steering is the quality of the calibration.** The factory defaults of 50% and 50% are temporary values. Before you use automatic operation, replace them with numbers from your substrate.
> - **Use watch mode first.** In watch mode, the system is armed but it only monitors. Thus you can make sure that the thresholds are correct. You can also do a test of the pipes and valves by hand, before you let the system operate with full automatic control.
> - **The recommended numbers are start points.** Adjust them in some cycles. If you do not adjust them, the rooms can receive too much water or not sufficient water.
> - **Some sensors can give incorrect information.** The dryback percentage can have no data, and the EC can show values that are too low to be correct. Make sure that the probe calibration is correct before you use EC steering.
> - **Fail-safes give protection to the hardware, but they use the sensor readings as correct values.** A defective probe or float can cause an incorrect decision, and the values can stay in the ‘safe’ range.

F2 is an accurate controller. It does not give results that are always correct. Monitor your numbers with time on a process-control chart. With this chart, you can find the difference between a signal and the usual variation, before you make a change.[^mohammed-spc-2024]For the cultivation information about the dryback and EC controls, read the paper on [coco crop steering](coco-crop-steering.html). Next, read the paper on the [root-zone sensor](root-zone-teros12.html). It gives information about the probes that the system uses for all its decisions.

## References

[^caplan-drought-2019]: Caplan, D., Dixon, M., & Zheng, Y. (2019). Increasing Inflorescence Dry Weight and Cannabinoid Content in Medical Cannabis Using Controlled Drought Stress. HortScience, 54(5), 964-969. https://doi.org/10.21273/HORTSCI13510-18 (source with peer review)
[^zawilski-calibration-2023]: Zawilski, B. M., Granouillac, F., Claverie, N., Lemaire, B., Brut, A., & Tallec, T. (2023). Calculation of soil water content using dielectric-permittivity-based sensors - benefits of soil-specific calibration. Geoscientific Instrumentation, Methods and Data Systems, 12, 45-56. https://doi.org/10.5194/gi-12-45-2023 (source with peer review)
[^qi-salinity-2024]: Qi, Q., Yang, H., Zhou, Q., Han, X., Jia, Z., Jiang, Y., Chen, Z., Hou, L., & Mei, S. (2024). Performance of Soil Moisture Sensors at Different Salinity Levels: Comparative Analysis and Calibration. Sensors, 24(19), 6323. https://doi.org/10.3390/s24196323 (source with peer review)
[^kang-rootgrowth-2019]: Kang, S., van Iersel, M. W., & Kim, J. (2019). Plant root growth affects FDR soil moisture sensor calibration. Scientia Horticulturae, 252, 208-211. https://doi.org/10.1016/j.scienta.2019.03.052 (source with peer review)
[^mohammed-spc-2024]: Mohammed MA. Statistical Process Control. Cambridge University Press (Elements of Improving Quality and Safety in Healthcare); 2024. https://doi.org/10.1017/9781009326834 (source with peer review)
