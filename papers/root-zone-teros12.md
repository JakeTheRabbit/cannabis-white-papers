---
slug: "root-zone-teros12"
title: "What your TEROS-12 measures and how to steer irrigation on it"
eyebrow: "Precision · Root zone"
summary: "A TEROS-12 probe buried in your growing media reports three numbers: how much water is stored, how salty that water is, and the temperature. This guide explains what each number means, why the raw reading is not yet the truth, and how to convert it into irrigation decisions you can stake a crop on."
track: "Precision & automation"
read_time: "~18 min read"
diagrams: "12 diagrams"
related: ["smart-watering-vrwe", "coco-crop-steering", "signal-and-noise"]
url: "https://www.growlabs.nz/wiki/root-zone-teros12.html"
md_url: "https://www.growlabs.nz/wiki/papers/root-zone-teros12.md"
version: "1.2"
updated: "2026-07-18"
license: "CC BY-NC 4.0"
license_url: "https://creativecommons.org/licenses/by-nc/4.0/"
attribution: "The Cannabis White Papers"
refs: [{"id": "topp-1980-dielectric-vwc", "n": 1, "cite": "Topp, G. C., Davis, J. L., & Annan, A. P. (1980). Electromagnetic determination of soil water content: Measurements in coaxial transmission lines. Water Resources Research, 16(3), 574-582.", "url": "https://doi.org/10.1029/WR016i003p00574", "peer": true}, {"id": "hilhorst-2000-pore-water-ec", "n": 2, "cite": "Hilhorst, M. A. (2000). A Pore Water Conductivity Sensor. Soil Science Society of America Journal, 64(6), 1922-1925.", "url": "https://doi.org/10.2136/sssaj2000.6461922x", "peer": true}, {"id": "fragkos-2024-teros12-soils-ec", "n": 3, "cite": "Fragkos, A., Loukatos, D., Kargas, G., & Arvanitis, K. G. (2024). Response of the TEROS 12 Soil Moisture Sensor under Different Soils and Variable Electrical Conductivity. Sensors, 24(7), 2206.", "url": "https://doi.org/10.3390/s24072206", "peer": true}, {"id": "nasta-2024-teros12-temp-correction", "n": 4, "cite": "Nasta, P., Coccia, F., Lazzaro, U., Bogena, H. R., Huisman, J. A., Sica, B., Mazzitelli, C., Vereecken, H., & Romano, N. (2024). Temperature-Corrected Calibration of GS3 and TEROS-12 Soil Water Content Sensors. Sensors, 24(3), 952.", "url": "https://doi.org/10.3390/s24030952", "peer": true}, {"id": "kargas-temp-capacitance-correction-2012", "n": 5, "cite": "Kapilaratne, R. G. C. J. & Lu, M. (2012). Correcting the Temperature Influence on Soil Capacitance Sensors Using Diurnal Temperature and Water Content Cycles. Sensors, 12(7), 9773-9790.", "url": "https://doi.org/10.3390/s120709773", "peer": true}, {"id": "tavan-2021-sensor-irrigation-soilless", "n": 6, "cite": "Tavan, M., Wee, B., Brodie, G., Fuentes, S., Pang, A., & Gupta, D. (2021). Optimizing Sensor-Based Irrigation Management in a Soilless Vertical Farm for Growing Microgreens. Frontiers in Sustainable Food Systems, 4, 622720.", "url": "https://doi.org/10.3389/fsufs.2020.622720", "peer": true}, {"id": "nemali-2006-set-point-irrigation", "n": 7, "cite": "Nemali, K. S. & van Iersel, M. W. (2006). An automated system for controlling drought stress and irrigation in potted plants. Scientia Horticulturae, 110(3), 292-297.", "url": "https://doi.org/10.1016/j.scienta.2006.07.009", "peer": true}, {"id": "meter-teros12-manual", "n": 8, "cite": "METER Group, Inc. (2023). TEROS 11/12 User Manual & Specifications. METER Group, Pullman, WA.", "url": "https://metergroup.com/products/teros-12/", "peer": false}]
---

# What your TEROS-12 measures and how to steer irrigation on it

_Precision · Root zone · ~18 min read_

> A TEROS-12 probe buried in your growing media reports three numbers: how much water is stored, how salty that water is, and the temperature. This guide explains what each number means, why the raw reading is not yet the truth, and how to convert it into irrigation decisions you can stake a crop on.

## Purpose and scope

A TEROS-12 is a small probe you push into growing media — coco, rockwool, or soil. It sends three numbers down a single digital wire: how much water the media holds, how salty that water is, and the temperature. This guide starts from zero, explains what each number actually represents, how the probe arrives at it, and why the raw reading alone should never open a valve.

The probe samples a pocket of roughly 1010 mL (34.2 fl oz) of media around its prongs, not the whole root zone.[^meter-teros12-manual] Everything that follows turns that one local, uncertain reading into a number you can actually steer irrigation on.

- The TEROS-12 reports **volumetric water content (VWC)**, **bulk electrical conductivity (EC)** and **substrate temperature** over a digital protocol called SDI-12.
- Its sensing volume is only about 1010 mL (34.2 fl oz) of media around the prongs — one local spot, not the average of a tray or a zone.
- The goal is to convert that noisy local reading into a trustworthy estimate of stored water, with the uncertainty stated openly rather than hidden.
- No prior knowledge of soil sensors is assumed. Every term is defined the first time it appears.

> **Diagram.** What the probe sees: a small ellipsoid of media around the prongs, not the whole root zone.[^meter-teros12-manual]

> **NOTE — Who this is for**
>
> This is for anyone putting a moisture probe in a pot who wants to steer on it honestly. It pairs with the [smart watering (VWC/EC) guide](smart-watering-vrwe.html) and the [coco crop-steering paper](coco-crop-steering.html).

## Definitions

Six words underpin everything in this field. Each is defined here in plain English first, then used precisely from that point on. They come back in context as you read.

**Volumetric water content (VWC)** — Think of your pot as a fixed container. Some of that container is solid media, some is air in the gaps, and some is liquid water. VWC is the liquid water's share of the whole, expressed in cubic metres of water per cubic metre of media (m³/m³). So 0.34 means 34% of the pot's total volume is liquid water. This is the primary number you steer irrigation on.

**Permittivity (dielectric constant)** — Water responds to an electric field roughly twenty times more strongly than dry growing media does — like how a wet sponge conducts electricity far better than a dry one, because the water is doing almost all the electrical work. Permittivity is the name for that responsiveness. Water’s is ~80; dry media is ~3–5; air is ~1. That contrast is the entire trick the probe uses to detect water.[^topp-1980-dielectric-vwc]

**Capacitance sensor** — A sensor that measures permittivity by applying a high-frequency electric field and reading how strongly the surrounding material stores it. The TEROS-12 is one of these. It infers VWC from that permittivity reading, without touching the water directly.

**Bulk EC vs pore-water EC** — The probe measures the conductivity of the whole wet-media mixture together — solids, water, and air — which is called bulk EC (0–20000 µS/cm on this probe). What the roots actually experience is pore-water EC: the salt concentration in the liquid sitting in the gaps between media particles. You cannot read pore-water EC directly; you estimate it from bulk EC using the Hilhorst (2000) model.

**DUL / container capacity** — Drained upper limit: how much water this _specific_ pot holds after gravity has pulled out all it can. It is your steering ceiling — and it is a property of your pot and media, not a textbook constant, so you measure it from your own runoff events.

**Resolution vs accuracy** — Resolution is the smallest change the probe can report: 0.001 m³/m³ VWC. Accuracy is how close that number is to reality: only ±0.03 m³/m³ with the generic calibration. The probe prints a precise-looking number, but precision is not the same as accuracy — a very precise number can still be consistently wrong.[^meter-teros12-manual]

> **Diagram.** Liquid water’s permittivity (~80) is roughly twenty times that of dry media (~3–5) and eighty times that of air (~1). Even a small amount of water swings the probe’s reading hard.[^topp-1980-dielectric-vwc]

> **Diagram.** A unit volume of media splits into solids, air and water. VWC is the water slice divided by the whole.

## How the probe measures water without touching it

The TEROS-12 is a **capacitance probe**. Its prongs push a high-frequency electric field into the surrounding media and read how strongly the media stores that field — a property called **permittivity**. Because water’s permittivity (~80) is roughly twenty times that of dry media (~3–5) and eighty times that of air (~1), the bulk permittivity of the media rises steeply and predictably as water content rises. That makes permittivity a reliable stand-in for VWC.[^topp-1980-dielectric-vwc]

The probe then applies a **calibration equation** — a generic mineral-soil curve by default — to map measured permittivity to a VWC number, reporting it to 0.001 m³/m³ resolution. The catch is built in from the start: the mapping is media-specific, and the generic curve is only accurate to ±0.03 m³/m³.[^meter-teros12-manual]

- Permittivity is the _physical_ quantity the probe measures. VWC is a _derived, calibrated_ estimate — one layer of math on top of that measurement.
- The permittivity-to-VWC curve is nonlinear, especially near saturation, where the response flattens. Near-full media can report a ‘full’ reading even when it is not.
- Substrate temperature shifts the dielectric response — a known physical effect that can look like a change in water content if you do not account for it.[^nasta-2024-teros12-temp-correction]
- The probe outputs data over SDI-12. A stale, NaN, or railed value (pinned at 0 or full-scale) is a hardware or cable fault, not a data reading.

> **Diagram.** VWC rises with permittivity but the curve bends and flattens near saturation. The same VWC step covers very different permittivity steps depending on where you are on the curve.[^topp-1980-dielectric-vwc]

> **Diagram.** From electric field to a number: every output is downstream of the same physical measurement. Calibration is where media-specific error enters.

## Why you must calibrate to your exact substrate

Out of the box the TEROS-12 uses a generic mineral-soil calibration, accurate to only ±0.03 m³/m³. A **substrate-specific** calibration for your exact coco or rockwool tightens that to ±0.01–0.02 m³/m³.[^fragkos-2024-teros12-soils-ec] That difference matters in practice. Crop-steering dryback windows are often _narrower_ than the ±0.03 generic error band. Steering on uncalibrated VWC means steering inside the noise.

A worked headroom example makes the consequence concrete. A naive 256 mL (8.7 fl oz) of ‘room to water’ shrinks to a safe ~109 mL (3.7 fl oz) once you account for ±0.02 accuracy, and to just ~54 mL (1.8 fl oz) under the generic ±0.03. Same pot, same probe — the only thing that changed is how honestly you treat the error band.[^nemali-2006-set-point-irrigation]

> **Diagram.** Usable safe headroom collapses as calibration error grows: from 256 mL (8.7 fl oz) naive to ~54 mL (1.8 fl oz) on the generic curve.[^nemali-2006-set-point-irrigation]

| Calibration type | VWC accuracy | Resolution | Tight steering? |
| --- | --- | --- | --- |
| Generic mineral (default) | ±0.03 m³/m³ | 0.001 m³/m³ | No — error band wider than a typical dryback window |
| Substrate-specific | ±0.01–0.02 m³/m³ | 0.001 m³/m³ | Yes — required for tight steering |

*Resolution is the same either way. Accuracy is what changes. Calibrate to your media before you steer on it.*

> **WARN — Calibration does not fix everything**
>
> Calibration corrects an additive _offset_ in the reading, but gain error and nonlinearity near saturation remain and do not cancel in later math. Treat substrate-specific calibration as **mandatory** for tight steering, not optional — and still respect the residual error that remains after you calibrate.

## What the EC reading tells you and where it breaks down

The probe measures **bulk EC** — the conductivity of the whole wet-media mixture, 0–20000 µS/cm. What growers care about is **pore-water EC**: the salt concentration in the solution actually in contact with the roots. To get pore-water EC from what the probe reports, you combine bulk EC, VWC, and temperature using the Hilhorst (2000) model.[^hilhorst-2000-pore-water-ec] Think of it like measuring the saltiness of a wet sponge by pushing current through the whole thing — sponge fibre and water together. The Hilhorst model then estimates the saltiness of the water alone.

That model is useful but parameter-sensitive — roughly ±20% — and unreliable below VWC 0.10 m³/m³, where you should not use it at all. The deeper limit is **representativeness**: the probe integrates one ~1010 mL (34.2 fl oz) spot. Channeling, dry pockets, or poor probe-to-media contact can make a perfectly functioning probe report a number that does not represent the zone.[^fragkos-2024-teros12-soils-ec]

- Bulk EC (0–20000 µS/cm) is what the probe measures directly. Pore-water EC is estimated from it — they are not the same thing.
- The Hilhorst (2000) conversion is ~±20% sensitive and invalid below VWC 0.10 m³/m³.[^hilhorst-2000-pore-water-ec]
- A representativeness fault: the probe’s 1010 mL (34.2 fl oz) pocket can be unrepresentative of the zone due to channeling, an air gap, or a pulled probe — while the probe itself is working perfectly.
- The sensor cannot see per-pot runoff volume, effective substrate volume (which shrinks as roots fill the pot), or whether a commanded irrigation shot was actually delivered.

> **Diagram.** Bulk EC is measured directly. Pore-water EC is derived through Hilhorst (2000) and degrades fast as the media dries.[^hilhorst-2000-pore-water-ec]

| The probe CAN see | The probe CANNOT see | Workaround |
| --- | --- | --- |
| VWC (local spot) | True zone average across pots | Multiple probes, a cohort model |
| Bulk EC | Per-pot runoff volume | Runoff trays / drain sensors |
| Substrate temperature | Effective substrate volume (shrinks with roots) | Periodic re-learning of DUL |
| Derived pore-water EC | Whether an emitter actually fired | Flow meter or load-cell weight jump |

*What one TEROS-12 can and cannot tell you, and the second witness that fills each gap.*

## Steering irrigation from TEROS-12 readings

The practical method is one demotion and one promotion. **Demote** the raw VWC reading from ‘truth’ to ‘one noisy witness with a confidence score’. **Promote** a small running water-balance model that holds the best estimate of stored water and is only _nudged_ by trusted readings.

You track **dryback** — the VWC fall between shots — watch **specific yield** (how much VWC rises per mL delivered) to sense when the pot is approaching capacity, and anchor your ceiling on the observed DUL rather than a guessed number. Steer on _trends_ — the shape and slope of the dryback — more than the absolute level, because trends are insensitive to additive calibration offset.[^tavan-2021-sensor-irrigation-soilless] Never act on a trend alone without a second witness such as runoff timing or pot weight.

1. **Calibrate to your substrate first** — Substrate-specific calibration is the first requirement. Without it you are steering inside the error band — the reading cannot be trusted tightly enough.
2. **Verify probe contact and position** — The probe must be seated firmly in the media at a representative, fixed spot. A loose probe or an air gap reports its surroundings, not your root zone.
3. **Learn this pot's DUL from corroborated events** — Anchor the capacity ceiling on approximately five runoff or weight events — not one — and express it as water-volume space rather than a raw VWC number.
4. **Steer on the dryback slope, bounded by safe headroom** — Act on dryback slope and specific yield, bounded by a headroom estimate that accounts for calibration error, not the naive point estimate.
5. **Confirm with a second witness before moving water** — Runoff onset or load-cell mass must confirm before any signal reaches a valve. The probe reading never drives a valve on its own.

> **Diagram.** Irrigation shots push VWC up toward the DUL ceiling; the slope of the fall between shots is the steering signal, not the absolute level at any one moment.

> **Diagram.** Every reading passes through a confidence score, a belief model, and a second-witness gate before it is allowed to move water.[^tavan-2021-sensor-irrigation-soilless]

## Diagnosing a bad reading before blaming the sensor

Most TEROS-12 problems are not the sensor failing. They are the sensor being _believed_ when it should not be. Draw the first distinction clearly: a **wrong reading** — where the probe is working but its 1010 mL (34.2 fl oz) does not represent the zone — is a representativeness fault. It should lower your trust in the absolute VWC number. A **railed, flatline, NaN, or stale value** is a hardware or cable fault. It should stop all automated action.

Watch for VWC that tracks the daily substrate-temperature cycle. That is a contact or calibration artifact, not a real change in stored water.[^kargas-temp-capacitance-correction-2012] Watch for wetting and drying paths that diverge abnormally — a sign of channeling or hydrophobic media. Watch for one pot drifting away from identically-treated neighbours — likely a blocked emitter or a dud probe, not a plant problem.

> **DANGER — Temperature and EC should move your trust, not the water number**
>
> Temperature and EC should move your **trust** in the reading, not the stored-water estimate directly. A diurnal temperature cycle can produce a real dielectric shift in dry media that looks like a change in water content.[^nasta-2024-teros12-temp-correction] Let that shift write VWC and you will be irrigating in response to physics, not plant need.

> **Diagram.** Work down the list in order: rule out hardware faults first, then artifacts, then local faults, before accepting the number as usable.

| Symptom | Likely cause | What it is NOT | Response |
| --- | --- | --- | --- |
| VWC railed / flatline / NaN / stale | Hardware or cable fault | Real water reading | Stop steering. Run a bounded safe routine. Alert a human |
| VWC swings with diurnal temp | Poor contact / calibration artifact | A real water change | Down-trust absolute VWC; check probe seating[^kargas-temp-capacitance-correction-2012] |
| Wetting vs drying diverge oddly | Channeling / hydrophobic media | Sensor failure | Inspect media; re-wet; check probe seating |
| One pot unlike its siblings | Blocked emitter or dud probe | A plant problem (yet) | Inspect emitter and probe before blaming the plant |

*Symptom to cause to response. The ‘what it is NOT’ column is the most useful — misdiagnosis is the real cost.*

> **WARN — Anchors must be earned from multiple events**
>
> A single manual reading or one human observation should never hard-write a capacity anchor or override a safety interlock. Anchors earn their place from corroborated events across multiple fills, not from one good look.

## Expected results and limitations

> **KEY — The honest account**
>
> A single TEROS-12 will not give you a per-zone, ground-truth picture of your root zone. Treating it as one is the most common and most expensive mistake. With substrate-specific calibration you can realistically resolve dryback _trends_ and approximate stored water to about ±0.01–0.02 m³/m³ in the spot the probe occupies. That is enough to steer on — if you account for the uncertainty and cross-check it.[^fragkos-2024-teros12-soils-ec]

> **Diagram.** A lone probe sits in a wide, caveat-heavy uncertainty band. Add substrate-specific calibration and one independent witness and the band tightens to a range you can steer from.[^nemali-2006-set-point-irrigation]

- Best case with substrate-specific calibration: trustworthy dryback shape and ~±0.01–0.02 m³/m³ stored-water accuracy for the probe’s local spot.
- Not achievable with one probe alone: per-zone runoff, delivery verification, or a true zone average across pots.
- A **load cell** (pot weight) is the highest-value add-on because it measures water stored directly, without routing through dielectric physics.
- Design for explicit ‘I cannot tell’ outputs rather than false precision. Control authority should be earned from the data, not assumed.

The mature approach is to require the system to say _when it cannot tell_, rather than emit a confident number it has not earned. Calibrate first, add one independent witness, then read the [smart watering (VWC/EC) guide](smart-watering-vrwe.html) for how those signals drive shots, and the [signal-and-noise paper](signal-and-noise.html) for separating a real trend from sensor noise.

## References

[^topp-1980-dielectric-vwc]: Topp, G. C., Davis, J. L., & Annan, A. P. (1980). Electromagnetic determination of soil water content: Measurements in coaxial transmission lines. Water Resources Research, 16(3), 574-582. https://doi.org/10.1029/WR016i003p00574 (peer-reviewed)
[^hilhorst-2000-pore-water-ec]: Hilhorst, M. A. (2000). A Pore Water Conductivity Sensor. Soil Science Society of America Journal, 64(6), 1922-1925. https://doi.org/10.2136/sssaj2000.6461922x (peer-reviewed)
[^fragkos-2024-teros12-soils-ec]: Fragkos, A., Loukatos, D., Kargas, G., & Arvanitis, K. G. (2024). Response of the TEROS 12 Soil Moisture Sensor under Different Soils and Variable Electrical Conductivity. Sensors, 24(7), 2206. https://doi.org/10.3390/s24072206 (peer-reviewed)
[^nasta-2024-teros12-temp-correction]: Nasta, P., Coccia, F., Lazzaro, U., Bogena, H. R., Huisman, J. A., Sica, B., Mazzitelli, C., Vereecken, H., & Romano, N. (2024). Temperature-Corrected Calibration of GS3 and TEROS-12 Soil Water Content Sensors. Sensors, 24(3), 952. https://doi.org/10.3390/s24030952 (peer-reviewed)
[^kargas-temp-capacitance-correction-2012]: Kapilaratne, R. G. C. J. & Lu, M. (2012). Correcting the Temperature Influence on Soil Capacitance Sensors Using Diurnal Temperature and Water Content Cycles. Sensors, 12(7), 9773-9790. https://doi.org/10.3390/s120709773 (peer-reviewed)
[^tavan-2021-sensor-irrigation-soilless]: Tavan, M., Wee, B., Brodie, G., Fuentes, S., Pang, A., & Gupta, D. (2021). Optimizing Sensor-Based Irrigation Management in a Soilless Vertical Farm for Growing Microgreens. Frontiers in Sustainable Food Systems, 4, 622720. https://doi.org/10.3389/fsufs.2020.622720 (peer-reviewed)
[^nemali-2006-set-point-irrigation]: Nemali, K. S. & van Iersel, M. W. (2006). An automated system for controlling drought stress and irrigation in potted plants. Scientia Horticulturae, 110(3), 292-297. https://doi.org/10.1016/j.scienta.2006.07.009 (peer-reviewed)
[^meter-teros12-manual]: METER Group, Inc. (2023). TEROS 11/12 User Manual & Specifications. METER Group, Pullman, WA. https://metergroup.com/products/teros-12/ (industry/manufacturer source)
