---
slug: "f2-crop-steering"
title: "F2 crop steering: the daily operating manual"
eyebrow: "Precision · Crop steering"
summary: "Run an autonomous crop-steering irrigation controller day to day. This is the plain-language starter guide: the P0–P3 cycle, moisture and salt targets, the controls you actually touch, the safety fail-safes, and what to do when something looks wrong."
track: "Precision & automation"
read_time: "~18 min read"
diagrams: "12 diagrams"
related: ["coco-crop-steering", "root-zone-teros12", "smart-watering-vrwe"]
url: "https://jaketherabbit.github.io/cannabis-white-papers/f2-crop-steering.html"
md_url: "https://jaketherabbit.github.io/cannabis-white-papers/papers/f2-crop-steering.md"
version: "1.0"
updated: "2026-06-24"
license: "CC BY-NC 4.0"
license_url: "https://creativecommons.org/licenses/by-nc/4.0/"
attribution: "The Cannabis White Papers"
refs: [{"id": "caplan-drought-2019", "n": 1, "cite": "Caplan, D., Dixon, M., & Zheng, Y. (2019). Increasing Inflorescence Dry Weight and Cannabinoid Content in Medical Cannabis Using Controlled Drought Stress. HortScience, 54(5), 964-969.", "url": "https://doi.org/10.21273/HORTSCI13510-18", "peer": true}, {"id": "zawilski-calibration-2023", "n": 2, "cite": "Zawilski, B. M., Granouillac, F., Claverie, N., Lemaire, B., Brut, A., & Tallec, T. (2023). Calculation of soil water content using dielectric-permittivity-based sensors - benefits of soil-specific calibration. Geoscientific Instrumentation, Methods and Data Systems, 12, 45-56.", "url": "https://doi.org/10.5194/gi-12-45-2023", "peer": true}, {"id": "qi-salinity-2024", "n": 3, "cite": "Qi, Q., Yang, H., Zhou, Q., Han, X., Jia, Z., Jiang, Y., Chen, Z., Hou, L., & Mei, S. (2024). Performance of Soil Moisture Sensors at Different Salinity Levels: Comparative Analysis and Calibration. Sensors, 24(19), 6323.", "url": "https://doi.org/10.3390/s24196323", "peer": true}, {"id": "kang-rootgrowth-2019", "n": 4, "cite": "Kang, S., van Iersel, M. W., & Kim, J. (2019). Plant root growth affects FDR soil moisture sensor calibration. Scientia Horticulturae, 252, 208-211.", "url": "https://doi.org/10.1016/j.scienta.2019.03.052", "peer": true}, {"id": "mohammed-spc-2024", "n": 5, "cite": "Mohammed MA. Statistical Process Control. Cambridge University Press (Elements of Improving Quality and Safety in Healthcare); 2024.", "url": "https://doi.org/10.1017/9781009326834", "peer": true}]
---

# F2 crop steering: the daily operating manual

_Precision · Crop steering · ~18 min read_

> Run an autonomous crop-steering irrigation controller day to day. This is the plain-language starter guide: the P0–P3 cycle, moisture and salt targets, the controls you actually touch, the safety fail-safes, and what to do when something looks wrong.

## What this system is, and what crop steering means

F2 is an **autonomous irrigation controller** for a veg grow room. It is software that reads moisture and salt probes in the root zone and decides, on its own, when to fire a watering shot through a pump and valves. You set the targets. It does the watering.

**Crop steering** means pushing the plant toward one of two kinds of growth by controlling exactly how and when it waters. _Vegetative_ steering (bulking) keeps the medium wet with many small waterings and only a small drying-out. _Generative_ steering (the flower or stress push) uses a bigger drying-out, a saltier root zone, and fewer, larger waterings. Even a mild, deliberate water deficit applied at the right time shifts a cannabis plant generatively without losing yield.[^caplan-drought-2019]

The system runs in two cooperating layers. A **Home Assistant integration** gives you every on-screen control and reading. An **AppDaemon engine** (`master_crop_steering_app.py`) is the decision-making brain that fires the shots. The room is wired as **3 rows (zones)**, each with its own moisture and salt probe and its own valve, all fed from one shared tank, one pump, and one main line.

> **Diagram.** The two software layers and the hardware they drive. Controls flow down, probe readings flow back up.

> **Diagram.** One tank, one pump, one main line feeding three independently steered rows. Each row has its own probe pair and valve.

> **KEY — Two things to memorise**
> 
> - The **‘Phase (manual set)’** dropdown is an _override_. It shows what you last picked, not the live phase. Read `sensor.crop_steering_current_phase` for the truth.
> - Disarming is always safe by design. `switch.crop_steering_system_enabled = OFF` means nothing can fire, ever.

## Key terms, defined

Three measurements run the whole system. Learn these first. Everything else builds on them.

**VWC (volumetric water content)** — How wet the growing medium is, shown as a percent. 60% VWC means water fills 60% of the medium's volume.

**EC (electrical conductivity)** — How salty or strong the root zone, or the feed water, is, in mS/cm. Higher EC means a stronger, saltier solution.

**Dryback** — The percent the medium dries down from its post-watering peak as the plant drinks. The single most important steering lever.

**Shot** — One timed burst of water, sized as a percent of the medium's volume. The duration in seconds comes from substrate volume, dripper flow rate and shot size.

**Field capacity** — The saturated peak VWC right after irrigation drains. The medium's ‘full’ mark.

**EC ratio** — Measured EC divided by target EC. Above 1 means too salty, so water more to dilute. Below 1 means too weak, so hold back.

**Vegetative vs Generative** — The two steering modes. Each selects a different set of dryback and EC targets for the engine to chase.

**Zone / phase** — A zone (row) is one of the 3 independently steered sections. A phase is where a row sits in its daily P0–P3 cycle.

> **Diagram.** The three living numbers behind every decision: how wet, how far it dries, and how salty.

## The P0–P3 daily cycle

Each row moves through four phases across the lights-on day, driven by the light schedule (defaults: lights on 10:00, off 22:00). The rhythm is always the same. Dry a little, refill, maintain, then wind down for the night.

- **P0 (morning dryback):** after lights-on the system waters nothing and lets the medium dry a small amount (`p0_dryback_drop_percent`, e.g. 5–10%). Exits to P1 when that target is hit OR when `p0_maximum_wait_time` expires (default 120 min).
- **P1 (ramp-up):** shots start at `p1_initial_shot_size`, grow by `p1_shot_size_increment`, are capped at `p1_maximum_shot_size`, spaced by `p1_time_between_shots`, and bounded by min/max shot counts. Exits when VWC ≥ `p1_target_vwc`.
- **P2 (maintenance):** the bulk of the day. Waters whenever VWC drops below `p2_vwc_threshold`; if the EC ratio runs above ~1.2 it waters MORE (to dilute), below ~0.8 it holds back.
- **P3 (overnight):** normal irrigation stops a set number of minutes before lights-off (`p3_veg_last_irrigation` / `_gen_`); only emergency top-ups fire below `p3_emergency_vwc_threshold`. Zones hold P3 all night.

> **Diagram.** One steered day: a small morning dryback, a refill to target, a maintenance band, then a controlled overnight wind-down.

> **Diagram.** How a row walks the loop: overnight P3 into P0 at lights-on, up through P1 to P2, then back to P3 before dark.

The two steering modes pick which targets the engine chases. **Vegetative** means high VWC, modest dryback (~10–20%), lower EC (~3.0 mS/cm), many small shots. **Generative** means lower VWC, bigger dryback (~25–50%), higher EC (~4.5–6.0 mS/cm), fewer larger shots. Set the mode globally with `select.crop_steering_steering_mode` or per row. A row override beats the global, and ‘Follow Main’ means use the global.

| Mode | VWC target | Dryback | EC target | Shot pattern |
| --- | --- | --- | --- | --- |
| **Vegetative** | High | Modest (10–20%) | ~3.0 mS/cm | Many small shots |
| **Generative** | Lower | Bigger (25–50%) | 4.5–6.0 mS/cm | Fewer, larger shots |

*The two steering recipes. Choose one per row, or let a row follow the main setting.*

## The controls and targets that matter

Day to day you touch a handful of controls. Two arm switches set how ‘on’ the system is. **System enabled** is the master arm. OFF means nothing irrigates ever, and the engine fails safe to OFF if it cannot read the switch. **Auto irrigation** only governs engine-driven shots. Turning it OFF still lets manual shots through, which is how you run ‘watch mode.’

The targets that steer growth are the per-phase VWC numbers (`p1_target_vwc`, `p2_vwc_threshold`), the dryback targets, and the per-phase and per-mode EC targets (`ec_target_veg_p0..p3` and `ec_target_gen_p0..p3`). Per-row selects let you push one row generative while the others stay veg, set who waters first when only one row can fire, and group zones to coordinate them.

- **EC stacking switch** ON lets the engine raise root-zone EC by reducing water, a generative push. Usually OFF for veg.
- **Hardware you can see:** the pump (Tuya plug, ~490 W running), the main-line relay, and `switch.f2_row1/2/3` zone valves. Only one waters at a time.
- **Per-row selects:** steering_mode, crop_profile (Follow Main + 7 profiles), group (A–D), and priority (Critical / High / Normal / Low).
- **Shot duration is computed** from `substrate_volume`, `dripper_flow_rate`, `drippers_per_plant` and shot size %. Set these correctly or every shot is the wrong size.
- **Per-row safety caps:** `max_daily_volume` (L), `shot_size_multiplier`, and `plant_count`.

| System enabled | Auto irrigation | What happens |
| --- | --- | --- |
| ON | ON | Normal: autonomous shots fire AND manual shots work |
| ON | OFF | **Watch mode**: armed but observe-only, manual shots only |
| OFF | either | Fully disarmed. Every shot blocked at the gate |

*The two levels of ‘off’. Use ON/OFF together for watch mode while you calibrate.*

> **TIP — Watch mode is your friend**
> 
> Run **System enabled ON, Auto irrigation OFF** while you confirm your numbers. The engine is armed and computing decisions but will not fire on its own. You can fire manual test shots and watch how the room responds before granting full autonomy.

## How a single irrigation decision is made (the gates)

When the engine decides a shot is needed, that shot only fires if it passes **every safety gate in order**. A single failed gate blocks it. This is what stops an autonomous system making a bad call.

> **Diagram.** Each check must pass before the next is tried. Only after the last gate does the hardware sequence run.

- **Order:** system armed → auto-irrigation (manual bypasses) → zone enabled → no manual override → not dosing → tank not empty → source pH/EC in range (default pH 5.8–6.2) → safety limits (daily-volume cap, max-EC ceiling, max-frequency).
- **pH/EC out of range** blocks the shot and sends a phone alert with an ‘Irrigate Anyway’ button.
- **Tank guard** blocks only when the low float reads empty, so the system can keep watering as the tank drains down.

> **Diagram.** The physical watering sequence: build pressure first, open the row, hold for the computed duration, then back out in reverse.

> **NOTE — Why pH/EC gating matters**
> 
> Source water that drifts out of the pH or EC window can lock out nutrients or burn roots. Gating on it, and alerting you rather than watering quietly, guards against feeding a bad solution to the whole room.

## Calibration: getting the numbers right before you trust it

Calibration is the most important practical step. The system only behaves correctly if its number entities match your _actual_ medium. The factory defaults are placeholders (50% VWC / 50% dryback), not your substrate. Dielectric moisture probes read differently in every medium, so a substrate-specific calibration is what makes the numbers mean anything.[^zawilski-calibration-2023]

1. **Observe** — Hand-water normally for a few days and watch each row's VWC. The reading just after watering is roughly field capacity (the peak). The reading just before the next watering is the trough. Together they define that row's operating band.
2. **Set the band** — Set `field_capacity` just above the highest peak, `p1_target_vwc` to each row's post-water peak, and `p2_vwc_threshold` a few percent below that. A smaller gap means a tighter veg band.
3. **Set the drybacks** — Veg ~15–20%, gen ~25–45%. `p0_dryback_drop_percent` 5–15%. Set the emergency floor a few percent below the normal trough.
4. **Set EC targets** — Slightly above feed EC for veg, well above for generative. `p2_ec_high/low_threshold` are multipliers on target (1.2 dilutes above 120%, 0.8 conserves below 80%).
5. **Run and refine** — Let it run a few cycles in watch mode, compare predicted against actual, and tighten the numbers.

> **Diagram.** The band you read from hand-watering: the emergency floor sits below the trough; the P2 band sits below the P1 target; field capacity caps the top.

Root growth itself changes how the probe reads over a run, so re-check the band occasionally rather than calibrating once and forgetting it.[^kang-rootgrowth-2019]

| Setting | Row 1 | Row 2 | Row 3 | What it does |
| --- | --- | --- | --- | --- |
| p1_target_vwc | 26 | 22 | 18 | Peak VWC P1 refills to |
| p2_vwc_threshold | 22 | 19 | 15 | Water when VWC drops below this |
| vegetative_dryback_target | 18 | 18 | 18 | How far P0 dries (%) |
| p0_dryback_drop | 8 | 8 | 8 | Morning dryback amount (%) |
| emergency floor | 15 | 14 | 11 | P3 overnight top-up trigger |
| field_capacity (global) | 30 | 30 | 30 | Saturated peak / ‘full’ mark |

*The source's recommended F2 starting numbers, derived from its hand-watered ranges. Starting points, not final settings.*

> **WARN — Defaults are placeholders, not your substrate**
> 
> If you skip calibration and run the 50%/50% factory defaults, the steering is meaningless. The engine chases numbers that have nothing to do with your medium. Calibrate first, then arm.

## How-to recipes for common jobs

Most routine actions have a safe, prescribed method. Prefer the integration services over raw switch-flipping. The services run the full gated hardware sequence so you cannot skip a safety check by accident.

| Task | Safe method | Caution |
| --- | --- | --- |
| Fire a manual shot | Service `crop_steering.execute_irrigation_shot` (zone, duration_seconds, shot_type: manual) | Runs the full gated sequence |
| Raw hardware (last resort) | Pump → main → valve ON; reverse to stop | One row at a time only |
| Force a phase | Change `select.crop_steering_irrigation_phase` | Immediate; bypasses normal transitions; selector then shows that phase |
| Irrigate Anyway override | Phone button after a pH/EC alert | 30-min bypass of the pH/EC gate ONLY; auto-clears when readings return in range |
| Disable vs pause a row | `zone_N_enabled` OFF (excluded) vs `zone_N_manual_override` ON (stays in steering) | Pause = hand-water while steered |
| Switch to generative | Select ‘Generative’ on steering mode (global or per-row) | Per-row beats global |
| Reset water counters | Automatic: daily at midnight, weekly Monday | Restart AppDaemon to re-init early |

*Quick-reference for the jobs you'll do most. When in doubt, use the service, not the raw switch.*

> **NOTE — ‘Irrigate Anyway’ is narrow on purpose**
> 
> It grants a 30-minute bypass of the _pH/EC gate only_. Every other interlock still applies: system armed, tank not empty, daily-volume cap. It auto-clears the moment pH/EC return in range.

## Safety fail-safes, emergency stop, and troubleshooting

The system has layered fail-safes: the pH/EC source-water gate, a tank dry-run guard (blocks only when the low float reads empty), a blocked-dripper guard that parks a row for 2 hours after too many failed shots, fail-safe reads (an unconfirmed arm switch is treated as disabled), and persistent state saved every 5 minutes so zones come back in their saved phase after a restart.

> **DANGER — The EMERGENCY button does NOT disarm the engine**
> 
> There are two ways to force-stop and they differ in a way that matters. The dashboard **EMERGENCY, ALL OFF** button (`script.f2_irrigation_all_off`) kills the three hardware pieces fast but leaves the engine _armed_. It may re-energise on its next ~60 s phase-check. To truly disarm, flip **System enabled OFF**. For anything beyond a brief stop, use both.

| Trigger | What it touches | Engine state after |
| --- | --- | --- |
| Dashboard EMERGENCY button | Kills pump, main, valves fast | Still ARMED, can re-fire next ~60 s check |
| System enabled OFF | Blocks every shot at the gate | Durably DISARMED |
| Engine auto emergency stop | Internal: parks the affected row | Armed, but offending row held |

*Two ways to stop, and what each one leaves behind. Only System enabled OFF disarms durably.*

1. **Fix the root cause** — Sort the physical problem first: empty tank, kinked line, bad probe, blocked dripper.
2. **Confirm hardware off** — Verify pump, main line and all valves read off.
3. **Check engine arm state** — Look at System enabled and Auto irrigation before re-arming.
4. **Re-arm and sanity-check** — Re-arm, then read `sensor.crop_steering_current_phase` for the live phase.
5. **Watch one cycle** — Do not walk away. Watch a full cycle fire correctly before trusting it again.

| Symptom | Likely cause | What to do |
| --- | --- | --- |
| Zones stuck in one phase | Transition condition never met / bad target | Check the phase's exit threshold against live VWC |
| Valve open but no flow | Pump off, kinked line, blocked dripper | Check pump state and the line; clear the dripper |
| Status / Water-today reads unknown | Engine not running or sensors unpopulated | Restart AppDaemon; confirm probes report |
| Repeated pH/EC alerts | Source water genuinely out of range, or sensor drift | Test the solution; verify the pH/EC probe |
| Row repeatedly parked as blocked dripper | 4+ failed shots in 30 min | Clear the physical dripper; row auto-releases after 2 h |
| ‘Irrigation already in progress, skipping’ every cycle | Stuck flag after a mid-shot kill | Restart AppDaemon (`ha addons restart a0d7b954_appdaemon`). Phase + counters restore from disk |

*The troubleshooting list from the source. Most faults trace to a physical cause or a stale flag.*

> **WARN — A known data gap to watch**
> 
> The source flags that `sensor.crop_steering_dryback_percentage` and substrate EC reads can be suspiciously low (Row 1 at 0.48 mS/cm). Salinity strongly affects how dielectric probes report.[^qi-salinity-2024] Check probe calibration before trusting EC steering.

## Realistic expectations

> **KEY — This is a controller, not a magic autopilot**
> 
> - **Steering quality is bounded by calibration.** The factory 50%/50% defaults are placeholders. Replace them with numbers from your own medium before you trust autonomous mode.
> - **Run watch mode first.** Armed but observe-only, so you confirm thresholds and hand-test plumbing before granting full autonomy.
> - **Recommended numbers are starting points.** Refine them over several cycles. Treating them as final is how rooms get over- or under-watered.
> - **Some sensors can mislead.** Dryback-percentage may be unpopulated and EC can read suspiciously low. Verify probe calibration before trusting EC steering.
> - **Fail-safes guard hardware, but they trust the sensors.** A bad probe or float can still cause a wrong decision well inside the ‘safe’ envelope.

Treat F2 like a sharp tool, not an oracle. Watching is a discipline worth keeping. Tracking your numbers over time the way a process-control chart does lets you tell a real signal from ordinary noise before you act on it.[^mohammed-spc-2024] For the cultivation theory behind the dryback and EC levers, read the [coco crop steering](coco-crop-steering.html) paper. To understand the probes the whole system trusts, read [root-zone sensing](root-zone-teros12.html) next.

## References

[^caplan-drought-2019]: Caplan, D., Dixon, M., & Zheng, Y. (2019). Increasing Inflorescence Dry Weight and Cannabinoid Content in Medical Cannabis Using Controlled Drought Stress. HortScience, 54(5), 964-969. https://doi.org/10.21273/HORTSCI13510-18 (peer-reviewed)
[^zawilski-calibration-2023]: Zawilski, B. M., Granouillac, F., Claverie, N., Lemaire, B., Brut, A., & Tallec, T. (2023). Calculation of soil water content using dielectric-permittivity-based sensors - benefits of soil-specific calibration. Geoscientific Instrumentation, Methods and Data Systems, 12, 45-56. https://doi.org/10.5194/gi-12-45-2023 (peer-reviewed)
[^qi-salinity-2024]: Qi, Q., Yang, H., Zhou, Q., Han, X., Jia, Z., Jiang, Y., Chen, Z., Hou, L., & Mei, S. (2024). Performance of Soil Moisture Sensors at Different Salinity Levels: Comparative Analysis and Calibration. Sensors, 24(19), 6323. https://doi.org/10.3390/s24196323 (peer-reviewed)
[^kang-rootgrowth-2019]: Kang, S., van Iersel, M. W., & Kim, J. (2019). Plant root growth affects FDR soil moisture sensor calibration. Scientia Horticulturae, 252, 208-211. https://doi.org/10.1016/j.scienta.2019.03.052 (peer-reviewed)
[^mohammed-spc-2024]: Mohammed MA. Statistical Process Control. Cambridge University Press (Elements of Improving Quality and Safety in Healthcare); 2024. https://doi.org/10.1017/9781009326834 (peer-reviewed)
