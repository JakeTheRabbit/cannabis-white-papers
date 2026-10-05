---
slug: "irrigation-manual"
title: "Manual for an automatic irrigation system"
eyebrow: "Precision · Irrigation"
summary: "Install, operate, and do maintenance on an irrigation system with sensors for crop steering, on Home Assistant. The manual starts with the basic information."
track: "Precision and automation"
read_time: "~14 min to read"
diagrams: "11 diagrams"
related: ["coco-crop-steering", "root-zone-teros12", "smart-watering-vrwe"]
url: "https://www.growlabs.nz/wiki/irrigation-manual.html"
md_url: "https://www.growlabs.nz/wiki/papers/irrigation-manual.md"
version: "1.2"
updated: "2026-07-18"
license: "CC BY-NC 4.0"
license_url: "https://creativecommons.org/licenses/by-nc/4.0/"
attribution: "The Cannabis White Papers"
refs: [{"id": "caplan-2019-drought-cannabis", "n": 1, "cite": "Caplan, D., Dixon, M., & Zheng, Y. (2019). Increasing inflorescence dry weight and cannabinoid content in medical cannabis using controlled drought stress. HortScience, 54(5), 964-969.", "url": "https://doi.org/10.21273/HORTSCI13510-18", "peer": true}, {"id": "yang-2022-rdi-review", "n": 2, "cite": "Yang, B., Fu, P., Lu, J., Ma, F., Sun, X., & Fang, Y. (2022). Regulated deficit irrigation: an effective way to solve the shortage of agricultural water for horticulture. Stress Biology, 2, 28.", "url": "https://doi.org/10.1007/s44154-022-00050-5", "peer": true}, {"id": "topp-1980-dielectric-vwc", "n": 3, "cite": "Topp, G. C., Davis, J. L., & Annan, A. P. (1980). Electromagnetic determination of soil water content: Measurements in coaxial transmission lines. Water Resources Research, 16(3), 574-582.", "url": "https://doi.org/10.1029/WR016i003p00574", "peer": true}, {"id": "mane-2024-sensor-calibration", "n": 4, "cite": "Mane, S., Das, N., Singh, G., Cosh, M., & Dong, Y. (2024). Advancements in dielectric soil moisture sensor calibration: A comprehensive review of methods and techniques. Computers and Electronics in Agriculture, 218, 108686.", "url": "https://doi.org/10.1016/j.compag.2024.108686", "peer": true}]
---

# Manual for an automatic irrigation system

_Precision · Irrigation · ~14 min to read_

> Install, operate, and do maintenance on an irrigation system with sensors for crop steering, on Home Assistant. The manual starts with the basic information.

## Purpose and scope

This system is an automatic irrigation system for plants in pots of soilless substrate. Sensors in the substrate of each pot measure how wet the substrate is and the quantity of fertilizer salt in it. The software selects the time of each irrigation and the quantity of water. The system is an alternative to manual irrigation and to a timer that does not use sensor data.

The system operates in **Home Assistant**. Home Assistant is open-source software for home automation. The software has no cost. You operate it on your equipment. A cloud account is not necessary for the basic system. The system controls 6 grow tables at the same time.The system has three layers, and you can use the layers one after the other. The first two layers are in operation. They are an irrigation package that uses a timer and a crop steering integration that uses sensors. The third layer is optional and has more functions (AppDaemon). It makes all the decisions without a person.

The three layers let you **start with the timer and then add the sensor decisions**. It is not necessary to assemble the system again. For the first week, operate the system with a timer only, and monitor the sensor readings. When the readings are correct, start crop steering.

- The system is an alternative to manual irrigation and to timers. It uses sensor data for its decisions on 6 grow tables.
- The system operates on Home Assistant. A cloud account and more software are not necessary for the basic system.
- The three layers are the irrigation package with a timer, the crop steering integration, and the optional AppDaemon layer for decisions without a person.
- You can start with the irrigation package that uses a timer, and then add the other layers. It is not necessary to assemble the system again.

> **Diagram.** The primary part of automation is this loop. The system measures the root zone and makes a decision. Then it applies water and measures again. Each other part of this manual gives more information about this loop.

> **Diagram.** The three layers are one above the other. Each layer adds more automatic decisions to the layer below it. You can stop at a layer when you are sure that it operates correctly.

## Definitions

This section gives the terms that this manual uses frequently. It is not necessary to know the terms at this time. Each term occurs again in this manual.

**VWC (volumetric water content)**: The quantity of water in the substrate, in percent. If the VWC is 60%, water fills 60% of the volume of the pot.

**EC (electrical conductivity)**: The quantity of dissolved fertilizer salt in the water around the roots. You measure it in mS/cm. It is an approximate measurement of the strength of the feed.

**Dryback**: The controlled drying of the substrate between two irrigations. You measure the dryback with the change of the VWC. If the substrate is always full of water, the roots do not go deeper. If you let the substrate dry to a set value and then fill it again, the roots go deeper. In the flowering stage, the plant also uses more energy for reproduction. The size of the dryback is the primary control for steering.

**Shot**: One short period of irrigation for a set time. The system gives some small shots each day. It does not give one large irrigation. The system sets the size of each shot.

**Field capacity**: The maximum quantity of water that the substrate can hold. More water than this quantity drains from the substrate. The default target in this system is 70%.

**Substrate**: The material that contains the roots. Examples are coco and rockwool, and materials of the same type. [Glossary →](glossary.html#gl-substrate)

**Solenoid valve**: A valve that operates with electricity. The relay board opens or closes the valve to start or stop the flow of water to a table.

**VPD and crop steering**: When the temperature of the air is higher and the air is drier, the air removes more moisture from the surface of the leaves. VPD (vapor pressure deficit) measures this effect. It is the difference between the moisture that the air contains at this time and the maximum moisture that it can contain at that temperature. When the VPD is higher, the plant transpires water more quickly, and you must supply water more quickly. Crop steering is a method to cause vegetative growth or generative growth in the plant with irrigation, climate, and light. [Glossary →](glossary.html)

> **Diagram.** A short reference for the three terms that cause the most problems for new personnel. These terms are the two types of steering and the information that runoff gives.

## Equipment of the irrigation system

A **KC868 E16S relay board** controls the valves. The relay board has an Ethernet connection and operates with ESPHome firmware. It opens and closes each valve: the 6 table valves, the mains water valve, the mainline valve, and the manifold valve.

Each table has a substrate probe. The probe measures the VWC, the EC, and the temperature. It sends the data with a basic digital protocol for soil sensors (**SDI-12**).The room also has 4 environment sensors, 3 CO2 sensors, 4 AC units, a humidifier, and 4 relays for dehumidifiers. **There is no pump switch**. A pressure switch starts the pump when the mainline valve opens. Thus the water flows from the tank to the mainline, then to the dripper of the table, and then to the plant.

> **NOTE: The mains water and manifold valves do not supply feed**
>
> The mains water valve and the manifold valve only fill the nutrient tank and mix the nutrient solution in it. The table valves are the only valves that supply feed to the plants. Some sensors have no connection at this time. This condition has effects on safety. The last section gives more information.

| Device | Function | Connection |
| --- | --- | --- |
| KC868 E16S relay board | It opens and closes all the valves: the table valves, the mains water valve, the mainline valve, and the manifold valve. | Ethernet and ESPHome |
| Substrate probes (×6) | Each probe measures VWC, EC, and temperature. There is one probe for each table. | SDI-12 |
| Environment sensors (×4) | They measure the temperature and the relative humidity (RH) of the room. | ESPHome and Wi-Fi |
| CO2 sensors (×3) | They measure the CO2 of the room in ppm. | ESPHome |
| AC units (×4) | They decrease the temperature of the room. | Relay or IR |
| Humidifier | It increases the RH of the room. | Relay |
| Dehumidifiers (×4) | They decrease the RH of the room. They start one after the other. | Relay |
| Lights | They set the photoperiod and the lights-on window. | Relay, with a timer |

*The equipment of the system. The relay board is the one point where a decision of the software opens or closes a valve.*

> **Diagram.** Water moves only when the mainline valve and a table valve are open. The pump does not operate without water, because the pressure in the mainline starts the pump. A signal from the software does not start the pump.

## Irrigation phases P0 to P3

Crop steering divides each lights-on day into four phases. The phases control how the plant uses water and nutrients. A **controlled dryback** is a drying of the substrate by a set quantity before you apply water again. This dryback is the signal that causes vegetative root growth or generative flower production.[^yang-2022-rdi-review]

**P0 (morning dryback)** is the phase with no irrigation. The substrate dries after the night. The system changes to P1 when the VWC decreases by the target quantity (50% for vegetative steering, 40% for generative steering) or after a maximum of 120 minutes.**P1 (ramp-up)** gives shots that become larger. The first shot is 2% of the substrate volume, and the size increases by 0.5% for each shot. The time between two shots is 15 minutes. The phase continues until the VWC is approximately 65%, with a maximum of 10 shots.

**P2 (maintenance)** keeps the VWC stable with top-up shots. A top-up shot occurs when the VWC decreases to less than 60%. The system also increases or decreases this threshold with the EC ratio (the measured EC divided by the target EC). If the EC ratio is more than 1.2, the system applies more water to flush the salts. If the EC ratio is less than 0.8, the system lets the substrate dry. As a result, the concentration of the nutrients increases.**P3 (before lights-off)** is irrigation for emergencies only, when the VWC is less than 40%. The dryback in the night starts the cycle again.

> **KEY: Vegetative and generative steering**
>
> - **Vegetative** steering uses smaller drybacks and a moderate EC to cause the growth of roots and leaves.
> - **Generative** steering uses larger controlled drybacks, a higher root-zone EC, or the two together, to cause flowering.[^caplan-2019-drought-cannabis]
> - The same P0 to P3 phases operate for the two types of steering. Only the dryback targets and the EC change.

> **Diagram.** The cycle starts again each day. P3 changes to P0 during the night, and lights-on starts the ramp again.

> **Diagram.** You want this shape in the VWC trace. At the start of the day, the VWC decreases in a smooth dryback. Then the VWC increases in a controlled quantity. In the maintenance phase, the VWC is almost flat. Before the period of darkness, the VWC decreases.

> **Diagram.** P2 does not have a constant threshold. The system measures the quantity of salt in the root zone. It lets the substrate dry to increase the concentration of the feed, or it applies more water to flush the salts. Thus the EC stays in the correct range.[^yang-2022-rdi-review]

## Environment controls and safety interlocks

The system controls the climate of the room and the irrigation. The dehumidifiers start when the humidity is 5% more than the target. The 4 relays start one after the other, with 10 seconds between the starts, to prevent a current peak at start. The dehumidifiers stop when the humidity is 2% less than the target.The humidifier uses the same logic in the opposite direction. The system injects CO2 when its concentration is 50 ppm less than the target, and only during lights-on. The injection always stops at lights-off.

Some safety layers operate independently and at the same time. Thus one fault cannot keep the valves open.The **master gate** lets irrigation occur only if all these conditions occur at the same time. The Enabled toggle of the system is on, and maintenance mode is off. The leak sensor does not show a leak, and the tank is OK. The clock is in the time window.A **valve watchdog** closes each table valve that is open for more than 3 minutes. Each day at 3 AM, an audit closes all valves and the CO2 injection. The audit is a reset. Maintenance mode closes all valves immediately.

> **WARN: Safety in many layers**
>
> Do not set a safety layer to off to make the system easier. You must keep all the layers. The system uses more than one check. If the master gate gives an incorrect decision, the valve watchdog and the audit each day close the valves.

| Protection | Function | Automatic? |
| --- | --- | --- |
| Master gate | It lets irrigation occur only if all these conditions occur at the same time. The Enabled toggle of the system is on, and maintenance mode is off. The leak sensor does not show a leak, and the tank is OK. The clock is in the time window. | Yes |
| Valve watchdog | It closes each table valve that is open for more than 3 minutes. | Yes |
| Mains watchdog | It closes the mainline valve if the valve is open for more than 24 minutes. | Yes |
| Leak abort | It stops all irrigation if the leak sensor shows a leak. | Yes (when the system has the sensor) |
| Tank-low abort | It stops irrigation if the tank float shows a low water level. | Yes (when the system has the sensor) |
| Maintenance mode | It closes all valves immediately. It prevents new shots. | Manual toggle |
| Alert for an offline sensor | It tells you when a probe or a device becomes offline. | Yes |
| Audit at 3 AM each day | It is a reset each day. It closes all valves and the CO2 injection. | Yes |
| CO2 closes at lights-off | It always stops the CO2 injection at lights-off. | Yes |

*The safety layers. Two of them (leak, tank-low) operate only after you install their sensors. Read the last section.*

## Commissioning procedure

Start the system in sequence. Make sure that each layer operates correctly before you start the next layer. If you start crop steering on equipment that you did not examine, a table can have too much water.

1. **Examine the equipment**: Make sure that each probe and the relay board show **Online** in ESPHome. Make sure that the VWC value of a table is a correct number (for example, 47.4), and not a dash or zero.
2. **Do a test of each valve**: Open each valve with the manual control. Then close the valve immediately. Make sure that each valve operates. Open the mainline valve for a short time. Make sure that the pump starts on pressure.
3. **Set the window**: Set the irrigation window. For example, set the start to 08:30 (30 minutes after lights-on) and the end to 18:00 (2 hours before lights-off). Set the interval to 60 minutes and the time of each shot to 60 seconds.
4. **Set the system to on**: In the Command Center, set the system to on. Set maintenance mode to off. Set the Enabled toggle to on for only the tables that you want to irrigate.
5. **Do one test cycle**: Start one cycle. Monitor the valves while each valve opens and closes, one after the other. Make sure that water flows to the drippers and that runoff occurs.
6. **Set the climate and the steering**: Set the temperature and humidity targets for day and night, and a CO2 target. After you make sure that the irrigation operates correctly, you can select a steering mode and a crop profile.

| Setting | Safe start value |
| --- | --- |
| Window start | 08:30 (30 minutes after lights-on) |
| Window end | 18:00 (2 hours before lights-off) |
| Interval | 60 minutes |
| Shot time | 60 seconds |
| Temperature for day and night | 26 °C (79 °F) in the day and 22 °C (72 °F) at night |
| Relative humidity (RH) | 60% |
| CO2 target | 1200 ppm |

*Safe start setpoints. We selected these values to be safe. Change them only after you monitor the trends for one week.*

## Operation each day and the dashboard

A check each day is short. When the system operates correctly, the Command Center shows these values for all 6 tables. The VWC is 30 to 70%. The EC is in your target range, and the substrate temperature is 20 to 26 °C (68 to 79 °F). The usual EC range is 2 to 6 mS/cm, and it is different for each stage. All the safety indicators are green.

On the Trends tab, the VWC graph must show a **sawtooth**. A sawtooth is a trace that decreases slowly and then increases quickly after each irrigation. A trace that is flat, or that only decreases, shows that irrigation does not occur. The graph gives you the first indication of a problem, before the system shows an error message.

- Correct readings each day: VWC 30 to 70%, EC approximately 2 to 6 mS/cm, substrate temperature 20 to 26 °C (68 to 79 °F), and all safety indicators green
- A VWC trace that is not a sawtooth is your first signal of a problem
- To set a table to on or off, use the **Enabled** toggle in Zone Control
- To stop the system in an emergency, set Maintenance Mode to on (this closes all valves) or use the emergency-stop script

| Tab | Information shown | When to use it |
| --- | --- | --- |
| Command Center | All tables on one display: VWC, EC, temperature, and safety. | Check of the condition each day |
| Zone Control | The Enabled toggle for each table, and the manual valve controls | Add a table, or stop irrigation of a table |
| Trends | Graphs of VWC and EC with time | Make sure that the VWC shows a sawtooth. Find the cause of a problem. |
| Environment | The temperature, RH, and CO2 of the room, and their targets | Tune the climate |
| Schedule | The settings for window, interval, and shot time | Adjust the times of irrigation |

*The five dashboard tabs. On most days you open only Command Center and Trends. The other tabs are for changes.*

> **Diagram.** The correct trace decreases and then increases after each irrigation, many times. If your trace only decreases and does not increase, it shows a fault. Use the troubleshooting table.

## Troubleshooting

You can find the cause of most problems with a short checklist. Start at the top and continue to the bottom, because the easiest checks find the most problems. Two examples are a check that the system is on and a check that the window is open.

If irrigation does not operate, make sure that the system is on and that maintenance mode is off. Make sure that the clock is in the window. Make sure that the Enabled toggle of a minimum of one table is on. Make sure that the irrigation-allowed binary sensor shows **on**.If the VWC or EC shows Unavailable, make sure that the ESPHome device is online. Then reload the template entities. If the system also has no raw probe value, the probe has no connection. A correct VWC is possible only if the dielectric sensor operates. Thus a raw value that does not change shows a problem with the probe, and not with the software.[^topp-1980-dielectric-vwc]

> **TIP: Tune slowly**
>
> Operate the irrigation with set times for approximately one week, and monitor the VWC trends. Then change to crop steering that uses sensors. First make sure that the sensor readings are correct. Calibration drift in probes with a low cost is frequent. It causes errors in each decision that uses the readings.[^mane-2024-sensor-calibration]

| Problem | Possible cause | First step |
| --- | --- | --- |
| Irrigation does not operate | The system is off, maintenance mode is on, the clock is not in the window, or no table has the Enabled toggle on. | Make sure that the system is on and that maintenance mode is off. Make sure that the clock is in the window and that the Enabled toggle of a table is on. Make sure that the irrigation-allowed sensor is on. |
| The VWC or EC shows Unavailable | The ESPHome device is offline, or the template entity has no new data. | Make sure that the device is online. Reload the template entities. Then examine the connection of the probe. |
| The shots show 0.0 s | The substrate volume or the dripper flow rate has no value, or the known prefix fault occurs. | Set the substrate volume (10 L / 2.6 gal) and the dripper flow rate (2 L/hr / 0.5 gal/hr). Do a check for the crop_steering_ prefix fault. |
| A valve that stays open | The relay stays on, or the watchdog does not operate. | First, set maintenance mode to on. Then set the valve to off with a service in Home Assistant. Then remove the power from the relay board. |
| Entity not found | The integration tries to find entities with the prefix crop_steering_. | Make sure that the entity IDs agree. If the known prefix fault occurs, the system cannot find the inputs for volume and flow rate. |

*The five frequent faults. The rows for the 0.0-second shot and for entity not found frequently have the same cause (a missing input or an input with an incorrect prefix).*

| Setting | Definition | Default | How to measure |
| --- | --- | --- | --- |
| Substrate volume | Liters of substrate for each pot | 10 L (2.6 gal) | Volume of the pot × fill fraction |
| Dripper flow rate | The quantity of water that each dripper supplies in one hour | 2 L/hr (0.5 gal/hr) | Read the number on the dripper, or do a catch test. |
| Drippers for each plant | The number of emitters that supply feed to one plant | 1 to 2 | Count the emitters on the plant |
| Field capacity | The maximum VWC before runoff occurs | 70% | Saturate the substrate. Let it drain. Read the sensor. |

*The settings that you tune. The system calculates the shot time from these values. Thus an incorrect substrate volume or flow rate gives incorrect shot times, or a shot time of zero.*

## Expected results and limitations

> **KEY: You cannot be sure of the results**
>
> The basic system gives automatic control of the irrigation times and automatic decisions from sensor data. The sensors and the plumbing set the limit for the performance of the system. The tank-low abort and the leak abort **always show ‘safe’ and will not operate**, until you install the tank float switch and the leak sensor. In this condition, do not operate the system without a person to monitor it.

There are two more limits. Without a leaf-temperature sensor, the system calculates the VPD from the air temperature of the room, and the VPD is less accurate. The optional AppDaemon layer is necessary for automatic changes between the P0 to P3 phases without a person. The basic system does not include this layer. Before you use the automation, operate the system with only a timer for approximately one week. Monitor the system in this time.

| Sensor that is not connected | Effect when there is no sensor |
| --- | --- |
| Tank float switch | There is no tank-low abort. The pump can operate when the tank is empty. |
| Leak sensor | There is no leak abort. A leak does not stop irrigation. |
| Tank pH and EC probes | The tank pH and EC show Unavailable. Mix the nutrient tank manually. |
| Leaf-temperature sensor | The system calculates the VPD from the air temperature of the room and not from the leaf temperature. The steering is less accurate. |

*These items are not safe at this time. Install the float switch and the leak sensor before you operate the system without a person to monitor it. Each other missing sensor has a smaller effect, and the system continues to operate. These two missing sensors remove a protection.*

First, read one usual day on the Trends tab. Then change one setting at a time. To know the biology of the dryback and the P0 to P3 rhythm, read the [crop steering in coir](coco-crop-steering.html) paper. To know how the probe measures the root zone, read the [root-zone sensor](root-zone-teros12.html) guide.

## References

[^caplan-2019-drought-cannabis]: Caplan, D., Dixon, M., & Zheng, Y. (2019). Increasing inflorescence dry weight and cannabinoid content in medical cannabis using controlled drought stress. HortScience, 54(5), 964-969. https://doi.org/10.21273/HORTSCI13510-18 (source with peer review)
[^yang-2022-rdi-review]: Yang, B., Fu, P., Lu, J., Ma, F., Sun, X., & Fang, Y. (2022). Regulated deficit irrigation: an effective way to solve the shortage of agricultural water for horticulture. Stress Biology, 2, 28. https://doi.org/10.1007/s44154-022-00050-5 (source with peer review)
[^topp-1980-dielectric-vwc]: Topp, G. C., Davis, J. L., & Annan, A. P. (1980). Electromagnetic determination of soil water content: Measurements in coaxial transmission lines. Water Resources Research, 16(3), 574-582. https://doi.org/10.1029/WR016i003p00574 (source with peer review)
[^mane-2024-sensor-calibration]: Mane, S., Das, N., Singh, G., Cosh, M., & Dong, Y. (2024). Advancements in dielectric soil moisture sensor calibration: A comprehensive review of methods and techniques. Computers and Electronics in Agriculture, 218, 108686. https://doi.org/10.1016/j.compag.2024.108686 (source with peer review)
