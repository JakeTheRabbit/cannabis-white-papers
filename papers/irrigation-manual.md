---
slug: "irrigation-manual"
title: "Automated irrigation system manual"
eyebrow: "Precision · Irrigation"
summary: "Install, run, and maintain a sensor-driven crop-steering irrigation system on Home Assistant, explained from zero."
track: "Precision & automation"
read_time: "~14 min read"
diagrams: "11 diagrams"
related: ["coco-crop-steering", "root-zone-teros12", "smart-watering-vrwe"]
url: "https://jaketherabbit.github.io/cannabis-white-papers/irrigation-manual.html"
md_url: "https://jaketherabbit.github.io/cannabis-white-papers/papers/irrigation-manual.md"
version: "1.2"
updated: "2026-07-18"
license: "CC BY-NC 4.0"
license_url: "https://creativecommons.org/licenses/by-nc/4.0/"
attribution: "The Cannabis White Papers"
refs: [{"id": "caplan-2019-drought-cannabis", "n": 1, "cite": "Caplan, D., Dixon, M., & Zheng, Y. (2019). Increasing inflorescence dry weight and cannabinoid content in medical cannabis using controlled drought stress. HortScience, 54(5), 964-969.", "url": "https://doi.org/10.21273/HORTSCI13510-18", "peer": true}, {"id": "yang-2022-rdi-review", "n": 2, "cite": "Yang, B., Fu, P., Lu, J., Ma, F., Sun, X., & Fang, Y. (2022). Regulated deficit irrigation: an effective way to solve the shortage of agricultural water for horticulture. Stress Biology, 2, 28.", "url": "https://doi.org/10.1007/s44154-022-00050-5", "peer": true}, {"id": "topp-1980-dielectric-vwc", "n": 3, "cite": "Topp, G. C., Davis, J. L., & Annan, A. P. (1980). Electromagnetic determination of soil water content: Measurements in coaxial transmission lines. Water Resources Research, 16(3), 574-582.", "url": "https://doi.org/10.1029/WR016i003p00574", "peer": true}, {"id": "mane-2024-sensor-calibration", "n": 4, "cite": "Mane, S., Das, N., Singh, G., Cosh, M., & Dong, Y. (2024). Advancements in dielectric soil moisture sensor calibration: A comprehensive review of methods and techniques. Computers and Electronics in Agriculture, 218, 108686.", "url": "https://doi.org/10.1016/j.compag.2024.108686", "peer": true}]
---

# Automated irrigation system manual

_Precision · Irrigation · ~14 min read_

> Install, run, and maintain a sensor-driven crop-steering irrigation system on Home Assistant, explained from zero.

## What this is and what it does

This is an automated watering system for plants grown in pots of soil-less media. Sensors buried in each pot measure how wet the media is and how much fertiliser salt it holds, and the software decides when and how much to water. That replaces watering by hand or on a ‘dumb’ timer.

The whole setup runs inside **Home Assistant**, free open-source home-automation software that you run yourself, with no cloud account required for the core system. It controls 6 grow tables at once. The system is built in three layers you can adopt in order: a time-based irrigation package and a sensor-driven crop-steering integration that both run today, plus an optional advanced layer (AppDaemon) for fully autonomous decisions.

The three-layer design lets you **start simple and add intelligence later** without rebuilding. Run it on a plain timer for the first week while you learn to trust the sensors, then switch on crop steering once the readings look sane.

- Replaces hand-watering and plain timers with sensor-driven decisions across 6 grow tables
- Runs on Home Assistant; no cloud account or extra software needed for the core system
- Three layers: time-based package, crop-steering integration, and optional AppDaemon autonomy
- Start timer-based and add intelligence later without rebuilding

> **Diagram.** The core idea of automation: read the root zone, decide, water, then re-read and repeat. Everything else in this manual is detail hung off this loop.

> **Diagram.** The three layers stack. Each one adds intelligence on top of the layer below, and you can stop at whichever level you trust.

## Key terms, defined from scratch

These are the words this manual uses constantly. You don't need to memorise them, each one comes back in context.

**VWC (volumetric water content)** — How wet the growing media is, shown as a percentage. 60% VWC means water fills 60% of the pot's volume.

**EC (electrical conductivity)** — How much dissolved fertiliser salt is in the water around the roots, measured in mS/cm. It is a proxy for feed strength.

**Dryback** — A deliberate, controlled drying-out of the media between waterings, measured as a drop in VWC. The main steering lever.

**Shot** — A single timed burst of irrigation. The system replaces one big daily soak with several small, sized shots.

**Field capacity** — The wettest the media can get before water just drains away. The default target in this system is 70%.

**Substrate** — The growing media itself: coco, rockwool or similar. [Glossary →](glossary.html#gl-substrate)

**Solenoid valve** — An electrically operated valve. The relay board switches it on or off to start and stop water flow to a table.

**VPD & crop steering** — VPD (vapour pressure deficit) is how ‘thirsty’ the air is. Crop steering is biasing the plant vegetative or generative using irrigation, climate and light. [Glossary →](glossary.html)

> **Diagram.** A quick reference for the three terms that trip up beginners most: the two steering directions and what runoff is telling you.

## The hardware: what gets wired up

The brain of the valve control is a **KC868 E16S relay board** connected over Ethernet and running ESPHome firmware. It physically switches every valve: the 6 tables plus the mains, mainline, and manifold valves.

Each table has a substrate probe that reads VWC, EC, and temperature over **SDI-12**, a simple digital protocol for soil sensors. The room is also covered by 4 environmental sensors, 3 CO2 sensors, 4 AC units, a humidifier, and 4 dehumidifier relays. **There is no pump switch**: the pump auto-starts on a pressure switch the moment the mainline valve opens, so water flows tank → mainline → table dripper → plant.

> **NOTE — Mains and manifold valves are not for feeding**
>
> The mains-water and manifold valves exist only to fill and mix the nutrient tank. The plants are fed exclusively through the table valves. A few sensors are intentionally not yet connected, which has safety consequences covered in the last section.

| Device | What it does | Connection |
| --- | --- | --- |
| KC868 E16S relay board | Switches all valves (tables, mains, mainline, manifold) | Ethernet / ESPHome |
| Substrate probes (×6) | Read VWC, EC, temperature, one per table | SDI-12 |
| Environmental sensors (×4) | Room temperature and humidity | ESPHome / Wi-Fi |
| CO2 sensors (×3) | Room CO2 in ppm | ESPHome |
| AC units (×4) | Cooling | Relay / IR |
| Humidifier | Raises room RH | Relay |
| Dehumidifiers (×4) | Lower room RH, staggered | Relay |
| Lights | Photoperiod, sets lights-on window | Relay / schedule |

*The physical kit. The relay board is the single point that turns software decisions into open and closed valves.*

> **Diagram.** Water only moves when both the mainline and a table valve are open. The pump never runs dry because it keys off mainline pressure, not a software command.

## The phase logic: P0 to P3

Crop steering splits each lights-on day into four phases that control how the plant uses water and nutrients. A **controlled dryback**, letting the media dry by a set amount before watering again, is the signal that steers the plant toward vegetative root growth or generative flower production.[^yang-2022-rdi-review]

**P0 (morning dryback)** is no watering at all, letting the media dry from overnight. It moves to P1 once VWC drops by the target amount (50% in vegetative, 40% in generative) or after a 120-minute cap. **P1 (ramp-up)** gives progressively larger shots, starting at 2% of substrate volume and rising 0.5% each shot, 15 minutes apart, up to 10 shots, until VWC hits roughly 65%.

**P2 (maintenance)** holds the media steady with top-up shots when VWC drops below 60%, and nudges that threshold up or down based on EC: if the EC ratio exceeds 1.2 it waters more to flush salts, and below 0.8 it lets the media dry to concentrate nutrients. **P3 (pre-lights-off)** is emergency-only watering below 40% VWC before an overnight dryback resets the cycle.

> **KEY — Vegetative vs generative steering**
>
> - **Vegetative** steering uses longer drybacks and lower EC to encourage root and leaf growth.
> - **Generative** steering uses shorter drybacks and higher EC to push flowering.[^caplan-2019-drought-cannabis]
> - The same P0–P3 framework runs both. Only the dryback targets and EC change.

> **Diagram.** The cycle loops every day. P3 hands back to P0 overnight, and lights-on restarts the ramp.

> **Diagram.** The shape you are steering for: a clean morning dryback, a controlled refill, a flat-ish maintenance band, then a fall before dark.

> **Diagram.** P2 is not a fixed threshold: the system reads how salty the root zone is and lets it dry to concentrate feed, or waters extra to flush, keeping EC in range.[^yang-2022-rdi-review]

## Environment control and the safety net

The system manages room climate as well as watering. Dehumidifiers turn on when humidity is 5% above target (the 4 relays stagger on with 10-second delays to avoid an inrush spike) and off 2% below. The humidifier mirrors that logic. CO2 injects when 50 ppm below target and only during lights-on, always closing at lights-off.

Several independent safety layers run in parallel so that one failure never leaves valves open. The **master gate** only allows irrigation when the system is enabled, not in maintenance mode, no leak detected, tank OK, and the clock is inside the time window. A **valve watchdog** force-closes any table valve open longer than 3 minutes, a daily 3 AM audit closes everything as a reset, and maintenance mode shuts all valves instantly.

> **WARN — Defence in depth**
>
> No single check is trusted on its own. If the master gate logic ever passed a bad decision, the valve watchdog and the daily audit would still close the valves. Treat these layers as non-negotiable and do not disable them to ‘simplify’ the system.

| Protection | What it does | Automatic? |
| --- | --- | --- |
| Master gate | Blocks all irrigation unless enabled + not-maintenance + no-leak + tank-OK + in-window | Yes |
| Valve watchdog | Force-closes any table valve open over 3 minutes | Yes |
| Mains watchdog | Force-closes the mainline valve open over 24 minutes | Yes |
| Leak abort | Stops all irrigation if a leak is detected | Yes (when sensor fitted) |
| Tank-low abort | Stops irrigation if the tank float reads low | Yes (when sensor fitted) |
| Maintenance mode | Closes all valves instantly; blocks new shots | Manual toggle |
| Sensor-offline alert | Warns when a probe or device drops offline | Yes |
| Daily 3 AM audit | Force-closes all valves and CO2 as a daily reset | Yes |
| CO2 lights-off close | Always stops CO2 injection at lights-off | Yes |

*The safety layers. Two of them (leak, tank-low) only fire once their physical sensors are installed. See the final section.*

## Commissioning: getting it running from scratch

Bring the system up in order so each layer is proven before the next one is switched on. Rushing straight to crop steering on unverified hardware is the fastest way to flood a table.

1. **Verify hardware** — Confirm every probe and the relay board show **Online** in ESPHome. Check a table VWC sensor reads a sensible number (e.g. 47.4), not a dash or zero.
2. **Test every valve** — Manually click each valve on, then immediately off, to confirm it responds. Toggle the mainline briefly to confirm the pump auto-starts on pressure.
3. **Set the window** — Set the irrigation window (e.g. start 08:30, 30 min after lights-on; end 18:00, 2 hours before lights-off), interval 60 minutes, duration 60 seconds.
4. **Enable the system** — From the Command Center, enable the system, switch maintenance mode off, and enable only the tables you actually want to water.
5. **Run one test cycle** — Run a single cycle and watch the valves open and close one at a time. Confirm water reaches the drippers and runoff appears.
6. **Set climate & steering** — Set day/night temp and humidity targets and a CO2 target. Optionally choose a steering mode and crop profile once watering is proven.

| Setting | Conservative starting value |
| --- | --- |
| Window start | 08:30 (30 min after lights-on) |
| Window end | 18:00 (2 h before lights-off) |
| Interval | 60 minutes |
| Shot duration | 60 seconds |
| Day / night temp | 26 °C day / 22 °C night |
| Humidity (RH) | 60% |
| CO2 target | 1200 ppm |

*Safe starting setpoints. These are intentionally cautious; tighten them only after a week of watching the trends.*

## Day-to-day operation and the dashboard

Daily checks are quick. On the Command Center, all 6 tables should read VWC between 30 and 70%, EC in your target range (typically 2 to 6 mS/cm by stage), and substrate temperatures 20 to 26 °C, with every safety indicator green.

On the Trends tab the VWC graph should show a **sawtooth**: a gradual drop, then a sharp rise after each irrigation. A flat or only-falling line means watering is not actually happening. That is your first warning sign, before any error message appears.

- Healthy daily readings: VWC 30–70%, EC ~2–6 mS/cm, substrate temp 20–26 °C, safety all green
- A non-sawtooth VWC trace is your earliest signal that something is wrong
- Enable or skip tables via the **Enabled** toggle in Zone Control
- Emergency stop: toggle Maintenance Mode on (closes all valves) or call the emergency-stop script

| Tab | What it shows | When to use it |
| --- | --- | --- |
| Command Center | All tables at a glance: VWC, EC, temp, safety | Daily health check |
| Zone Control | Per-table enable toggles and manual valves | Add or skip a table |
| Trends | VWC / EC graphs over time | Confirm the sawtooth; diagnose |
| Environment | Room temp, RH, CO2 and their targets | Tune climate |
| Schedule | Window, interval, duration settings | Adjust timing |

*The five dashboard tabs. Most days you only open Command Center and Trends; the rest are for changes.*

> **Diagram.** The healthy pattern: repeated drop-then-refill. If your trace falls steadily with no rises, treat it as a fault and check the troubleshooting matrix.

## Troubleshooting and tuning

Most problems are diagnosable from a short checklist. Work top to bottom, because the cheapest checks (is it on? is the window open?) catch the most cases.

If irrigation will not run, confirm the system is on, maintenance mode is off, the clock is inside the window, at least one table is enabled, and the irrigation-allowed binary sensor reads **on**. If VWC or EC shows Unavailable, check the ESPHome device is online and reload template entities. If the raw probe value is also missing, the probe has lost its connection. Reliable VWC depends on a working dielectric sensor, so a flatlined raw value points at the probe, not the software.[^topp-1980-dielectric-vwc]

> **TIP — Tune slowly**
>
> Run time-based scheduling for about a week while watching VWC trends before switching to sensor-driven crop steering. Confirm the sensors track reality first. Calibration drift in cheap probes is common and skews every decision built on top of it.[^mane-2024-sensor-calibration]

| Symptom | Likely cause | First action |
| --- | --- | --- |
| Irrigation won't run | System off, maintenance on, outside window, or no table enabled | Check system on, maintenance off, inside window, a table enabled, irrigation-allowed sensor on |
| VWC / EC Unavailable | ESPHome device offline or template entity stale | Confirm device online, reload template entities, then suspect a lost probe connection |
| Shots show 0.0 s | Substrate volume or dripper flow not set; known prefix bug | Set substrate volume (10 L) and dripper flow (2 L/hr); check for crop_steering_ prefix bug |
| Stuck-open valve | Relay latched or watchdog not firing | Maintenance mode first, turn the valve off via service, then cut power to the relay board |
| Entity not found | Integration looking for crop_steering_ prefixed entities | Verify entity IDs match; the known prefix bug can hide volume / flow-rate inputs |

*The five common failures. The 0.0-second-shot and entity-not-found rows often share the same root cause (a missing or mis-prefixed input).*

| Parameter | Meaning | Default | How to measure |
| --- | --- | --- | --- |
| Substrate volume | Litres of media per pot | 10 L | Pot volume × fill fraction |
| Dripper flow rate | Water delivered per dripper per hour | 2 L/hr | Stamped on the dripper / catch test |
| Drippers per plant | How many emitters feed one plant | 1–2 | Count physically |
| Field capacity | Wettest VWC before runoff | 70% | Saturate, drain, read the sensor |

*The tuning parameters. Shot duration is computed from these, so a wrong substrate volume or flow rate produces wrong (or zero) shot times.*

## Realistic expectations and limits

> **KEY — This is guidance, not a guarantee**
>
> The core system automates timing and sensor-driven decisions, but it is only as good as its sensors and plumbing. Until the tank float switch and leak sensor are physically installed, the tank-low and leak emergency aborts are **hardcoded to ‘safe’ and will not trigger**, so do not run the system unattended in that state.

Two more honest limits. Without a leaf-temperature sensor, VPD falls back to room air temperature and is less accurate. The fully autonomous P0–P3 phase transitions need the optional AppDaemon layer, which is not deployed by default. Budget about a week of supervised, timer-based running before you trust the automation.

| Not-yet-connected sensor | Impact while missing |
| --- | --- |
| Tank float switch | No tank-low abort: pump can run a dry tank |
| Leak sensor | No leak abort: a leak will not stop irrigation |
| Tank pH / EC probes | Tank pH and EC show Unavailable; mix by hand |
| Leaf-temperature sensor | VPD falls back to room air temp; less accurate steering |

*What is not safe yet. Install the float and leak sensors before any unattended run. Everything else degrades gracefully, but these two remove real protection.*

Start by reading one normal day on the Trends tab, then change one thing at a time. For the biology behind the dryback and the P0–P3 rhythm, read the [crop steering in coir](coco-crop-steering.html) paper; for how the probe actually measures the root zone, see the [root-zone sensor](root-zone-teros12.html) guide.

## References

[^caplan-2019-drought-cannabis]: Caplan, D., Dixon, M., & Zheng, Y. (2019). Increasing inflorescence dry weight and cannabinoid content in medical cannabis using controlled drought stress. HortScience, 54(5), 964-969. https://doi.org/10.21273/HORTSCI13510-18 (peer-reviewed)
[^yang-2022-rdi-review]: Yang, B., Fu, P., Lu, J., Ma, F., Sun, X., & Fang, Y. (2022). Regulated deficit irrigation: an effective way to solve the shortage of agricultural water for horticulture. Stress Biology, 2, 28. https://doi.org/10.1007/s44154-022-00050-5 (peer-reviewed)
[^topp-1980-dielectric-vwc]: Topp, G. C., Davis, J. L., & Annan, A. P. (1980). Electromagnetic determination of soil water content: Measurements in coaxial transmission lines. Water Resources Research, 16(3), 574-582. https://doi.org/10.1029/WR016i003p00574 (peer-reviewed)
[^mane-2024-sensor-calibration]: Mane, S., Das, N., Singh, G., Cosh, M., & Dong, Y. (2024). Advancements in dielectric soil moisture sensor calibration: A comprehensive review of methods and techniques. Computers and Electronics in Agriculture, 218, 108686. https://doi.org/10.1016/j.compag.2024.108686 (peer-reviewed)
