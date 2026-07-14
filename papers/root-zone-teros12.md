---
slug: "root-zone-teros12"
title: "Root-zone state estimation with the TEROS-12 sensor"
eyebrow: "Precision · Root zone"
summary: "A TEROS-12 capacitance probe measures three things in your pot. This guide explains what each number means, why the raw reading is not the truth, and how to turn it into safe irrigation decisions."
track: "Precision & automation"
read_time: "~18 min read"
diagrams: "12 diagrams"
related: ["smart-watering-vrwe", "coco-crop-steering", "signal-and-noise"]
url: "https://jaketherabbit.github.io/cannabis-white-papers/root-zone-teros12.html"
md_url: "https://jaketherabbit.github.io/cannabis-white-papers/papers/root-zone-teros12.md"
version: "1.1"
updated: "2026-07-15"
license: "CC BY-NC 4.0"
license_url: "https://creativecommons.org/licenses/by-nc/4.0/"
attribution: "The Cannabis White Papers"
refs: [{"id": "topp-1980-dielectric-vwc", "n": 1, "cite": "Topp, G. C., Davis, J. L., & Annan, A. P. (1980). Electromagnetic determination of soil water content: Measurements in coaxial transmission lines. Water Resources Research, 16(3), 574-582.", "url": "https://doi.org/10.1029/WR016i003p00574", "peer": true}, {"id": "hilhorst-2000-pore-water-ec", "n": 2, "cite": "Hilhorst, M. A. (2000). A Pore Water Conductivity Sensor. Soil Science Society of America Journal, 64(6), 1922-1925.", "url": "https://doi.org/10.2136/sssaj2000.6461922x", "peer": true}, {"id": "fragkos-2024-teros12-soils-ec", "n": 3, "cite": "Fragkos, A., Loukatos, D., Kargas, G., & Arvanitis, K. G. (2024). Response of the TEROS 12 Soil Moisture Sensor under Different Soils and Variable Electrical Conductivity. Sensors, 24(7), 2206.", "url": "https://doi.org/10.3390/s24072206", "peer": true}, {"id": "nasta-2024-teros12-temp-correction", "n": 4, "cite": "Nasta, P., Coccia, F., Lazzaro, U., Bogena, H. R., Huisman, J. A., Sica, B., Mazzitelli, C., Vereecken, H., & Romano, N. (2024). Temperature-Corrected Calibration of GS3 and TEROS-12 Soil Water Content Sensors. Sensors, 24(3), 952.", "url": "https://doi.org/10.3390/s24030952", "peer": true}, {"id": "kargas-temp-capacitance-correction-2012", "n": 5, "cite": "Kapilaratne, R. G. C. J. & Lu, M. (2012). Correcting the Temperature Influence on Soil Capacitance Sensors Using Diurnal Temperature and Water Content Cycles. Sensors, 12(7), 9773-9790.", "url": "https://doi.org/10.3390/s120709773", "peer": true}, {"id": "tavan-2021-sensor-irrigation-soilless", "n": 6, "cite": "Tavan, M., Wee, B., Brodie, G., Fuentes, S., Pang, A., & Gupta, D. (2021). Optimizing Sensor-Based Irrigation Management in a Soilless Vertical Farm for Growing Microgreens. Frontiers in Sustainable Food Systems, 4, 622720.", "url": "https://doi.org/10.3389/fsufs.2020.622720", "peer": true}, {"id": "nemali-2006-set-point-irrigation", "n": 7, "cite": "Nemali, K. S. & van Iersel, M. W. (2006). An automated system for controlling drought stress and irrigation in potted plants. Scientia Horticulturae, 110(3), 292-297.", "url": "https://doi.org/10.1016/j.scienta.2006.07.009", "peer": true}, {"id": "meter-teros12-manual", "n": 8, "cite": "METER Group, Inc. (2023). TEROS 11/12 User Manual & Specifications. METER Group, Pullman, WA.", "url": "https://metergroup.com/products/teros-12/", "peer": false}]
---

# Root-zone state estimation with the TEROS-12 sensor

_Precision · Root zone · ~18 min read_

> A TEROS-12 capacitance probe measures three things in your pot. This guide explains what each number means, why the raw reading is not the truth, and how to turn it into safe irrigation decisions.

## What this is, and who it's for

A TEROS-12 is a small probe you bury in growing media: coco, rockwool or soil. It reports three things down a single digital wire: how much water is in the media, how salty that water is, and the temperature. This guide explains, from zero, what each of those numbers means, how the probe arrives at them, and why you should never wire the probe straight to a valve.

A single probe is one noisy local witness. It samples a roughly 1010 mL pocket of one pot, not the whole zone.[^meter-teros12-manual] Everything that follows turns that one local, uncertain reading into a number you can actually steer irrigation on.

- The TEROS-12 reports **volumetric water content (VWC)**, **bulk electrical conductivity (EC)** and **substrate temperature** over a digital protocol called SDI-12.
- Its ‘volume of influence’ is only about 1010 mL of media around the prongs. It sees one local spot, not the average of a tray or a zone.
- The goal is to convert that noisy local reading into a trustworthy estimate of stored water, with the uncertainty stated openly rather than hidden.
- No prior knowledge of soil sensors is assumed. Every term is defined the first time it appears.

> **Diagram.** What the probe sees: a small ellipsoid of media around the prongs, not the whole root zone.[^meter-teros12-manual]

> **NOTE — Who this is for**
>
> This is for anyone putting a moisture probe in a pot who wants to steer on it honestly. It pairs with the [smart watering (VWC/EC) guide](smart-watering-vrwe.html) and the [coco crop-steering paper](coco-crop-steering.html).

## Key terms, defined once

Here is the small set of words this whole field hangs on. You don't need to memorise them. Each one comes back in context.

**Volumetric water content (VWC)** — The fraction of the media's total volume that is liquid water, in cubic metres of water per cubic metre of media (m³/m³). So 0.34 means 34% of the pot's volume is water. This is the headline irrigation number.

**Permittivity (dielectric constant)** — How strongly a material responds to an electric field. Water's is very high (~80), dry media is ~3–5 and air is ~1. That huge gap is the entire trick that lets a sensor ‘feel’ water it cannot see.[^topp-1980-dielectric-vwc]

**Capacitance sensor** — A sensor that measures permittivity, then infers VWC from it. The TEROS-12 is one of these.

**Bulk EC vs pore-water EC** — Bulk EC is the conductivity of the whole wet-media mixture (0–20000 µS/cm on this probe). Pore-water EC is the conductivity of just the nutrient solution in the pores, the salt the roots actually feel, estimated indirectly.

**DUL / container capacity** — Drained upper limit: how much water this _specific_ pot holds after it stops draining. It is your steering ceiling, and it is a property of your pot and media, not a textbook constant.

**Resolution vs accuracy** — Resolution is the smallest change reported (0.001 m³/m³ VWC). Accuracy is how close the number is to the truth (only ±0.03 m³/m³ with the generic calibration). A precise-looking number can still be wrong.[^meter-teros12-manual]

> **Diagram.** Liquid water has a permittivity around 80 versus ~3–5 for dry media and ~1 for air, so even a little water swings the bulk reading hard.[^topp-1980-dielectric-vwc]

> **Diagram.** A unit volume of media splits into solids, air and water. VWC is just the water slice divided by the whole.

## How the probe turns an electric field into a water number

The TEROS-12 is a **capacitance probe**. Its prongs create a high-frequency electric field in the surrounding media and measure how strongly the media stores that field, which is its permittivity. Because water's permittivity (~80) towers over dry media (~3–5) and air (~1), the bulk permittivity rises steeply and predictably as water content rises. That makes permittivity a stand-in for VWC.[^topp-1980-dielectric-vwc]

The sensor then applies a **calibration equation** (a generic mineral-soil curve by default) to map measured permittivity to a VWC number, reporting it to 0.001 m³/m³ resolution. The catch is baked in from the start: that mapping is media-specific, and the generic curve is only good to ±0.03 m³/m³.[^meter-teros12-manual]

- Capacitance and permittivity are the _physical_ quantity. VWC is a _derived, calibrated_ estimate sitting on top of it.
- The permittivity-to-VWC curve is nonlinear, especially near saturation, where the response flattens and can fake a ‘full’ reading.
- Substrate temperature is read as a useful output and because temperature shifts the dielectric response, a known effect that can masquerade as a water swing.[^nasta-2024-teros12-temp-correction]
- The probe outputs over SDI-12. A stale, NaN, or railed value (pinned at 0 or full-scale) is a hardware fault, not data.

> **Diagram.** VWC rises with permittivity but the curve bends and flattens near saturation, so the same VWC step covers very different permittivity steps.[^topp-1980-dielectric-vwc]

> **Diagram.** From electric field to a number: every output is downstream of the same physical measurement.

## Calibration: why the default number lies a little

Out of the box the TEROS-12 uses a generic mineral-soil calibration, which makes VWC accurate to only ±0.03 m³/m³. A **substrate-specific** calibration for your exact coco or rockwool tightens that to ±0.01–0.02 m³/m³.[^fragkos-2024-teros12-soils-ec] That difference is not academic. Crop-steering dryback windows are often _narrower_ than the ±0.03 generic error band, so steering on uncalibrated VWC means steering inside the noise.

A worked headroom example shows the consequence directly. A naive 256 mL of ‘room to water’ shrinks to a safe ~109 mL once you account for ±0.02 accuracy, and to just ~54 mL under the generic ±0.03. Same pot, same probe. The only thing that changed is how honestly you treat the error band.[^nemali-2006-set-point-irrigation]

> **Diagram.** Usable ‘safe headroom’ collapses as calibration error grows: from 256 mL naive to ~54 mL on the generic curve.[^nemali-2006-set-point-irrigation]

| Calibration type | VWC accuracy | Resolution | Tight steering? |
| --- | --- | --- | --- |
| Generic mineral (default) | ±0.03 m³/m³ | 0.001 m³/m³ | No. Error wider than dryback window |
| Substrate-specific | ±0.01–0.02 m³/m³ | 0.001 m³/m³ | Yes. Required for tight steering |

*Resolution is identical. Accuracy is what changes. Calibrate to your media.*

> **WARN — Calibration is not a cure-all**
>
> Calibration corrects an additive _offset_, but gain error and nonlinearity near saturation persist and do not cancel out in later math. Treat substrate-specific calibration as **mandatory** for tight steering, not optional, and still respect the residual error.

## What EC tells you, and what the probe cannot see

The TEROS-12 measures **bulk EC**, the conductivity of the whole wet-media mixture, 0–20000 µS/cm. What growers care about is **pore-water EC**: the salt concentration in the solution actually touching the roots. You get pore-water EC by combining bulk EC, VWC and temperature through the Hilhorst (2000) model.[^hilhorst-2000-pore-water-ec]

That model is genuinely useful, but it is parameter-sensitive at roughly ±20% and unreliable below VWC 0.10 m³/m³, where it should not be used at all. The deeper limit is **representativeness**. The probe integrates one ~1010 mL spot, so channeling, dry pockets, or poor probe-to-media contact can make a perfectly healthy probe report a number that is simply not true of the zone.[^fragkos-2024-teros12-soils-ec]

- Bulk EC is the raw measurement (0–20000 µS/cm). Pore-water EC is the derived quantity the roots experience.
- Hilhorst (2000) converts bulk EC + VWC + temp to pore-water EC, but is ~±20% sensitive and invalid below VWC 0.10 m³/m³.[^hilhorst-2000-pore-water-ec]
- Representativeness fault: the probe can be fine while its 1010 mL is _not_ representative of the zone (channeling, air gap, pulled probe).
- The sensor cannot see per-pot runoff, effective substrate volume (it shrinks as roots grow), or whether a commanded irrigation shot was truly delivered.

> **Diagram.** Bulk EC is measured. Pore-water EC is inferred through Hilhorst (2000) and degrades fast in dry media.[^hilhorst-2000-pore-water-ec]

| The probe CAN see | The probe CANNOT see | Workaround |
| --- | --- | --- |
| VWC (local spot) | True zone average across pots | Multiple probes, a cohort model |
| Bulk EC | Per-pot runoff volume | Runoff trays / drain sensors |
| Substrate temperature | Effective substrate volume (shrinks with roots) | Periodic re-learning of DUL |
| Derived pore-water EC | Whether an emitter actually fired | Flow meter or load-cell weight jump |

*What one TEROS-12 can and cannot tell you, and the second witness that fills each gap.*

## Using it to steer irrigation, step by step

The practical recipe is one demotion and one promotion. **Demote** the raw VWC reading from ‘truth’ to ‘one noisy witness with a confidence score’. **Promote** a small running water-balance model that holds the belief about stored water and is only _nudged_ by trusted readings.

You track **dryback** (the VWC fall between shots), watch **specific yield** (S = change in VWC per delivered mL) to sense when the pot is filling, and anchor your ceiling on the observed DUL rather than a guessed number. Steer on _derivatives_, the shape and slope of the dryback, more than the absolute level, because trends shrug off additive calibration error[^tavan-2021-sensor-irrigation-soilless]. Never act on a derivative alone without a second witness such as runoff timing or pot weight.

1. **Calibrate to your substrate** — Substrate-specific calibration is mandatory for tight steering. Without it you steer inside the error band.
2. **Verify probe contact and position** — Good media contact and a fixed, representative spot. A loose probe reports its air gap, not your root zone.
3. **Learn this pot's DUL** — Anchor the ceiling on ~5 corroborated runoff/weight events, not one, and prefer water-volume space over a raw VWC number.
4. **Steer on shape, gated by safe headroom** — Act on dryback slope and specific yield, bounded by a lower-confidence headroom estimate, not the naive point estimate.
5. **Require a second witness** — Runoff onset or load-cell mass must confirm before any signal moves a valve. The reading never reaches the valve alone.

> **Diagram.** Irrigation shots refill toward the DUL ceiling; the slope of the fall between shots is the steering signal, not the absolute level.

> **Diagram.** Every reading passes through a confidence score, a belief model and a second-witness gate before it is allowed to move water.[^tavan-2021-sensor-irrigation-soilless]

## Troubleshooting and pitfalls

Most TEROS-12 disappointments are not the sensor breaking. They are the sensor being _believed_ when it shouldn't be. Make the first distinction clearly. A **wrong reading** (the probe is fine but its 1010 mL isn't the zone) is a representativeness fault that should lower your trust in absolute VWC. A **railed, flatline, NaN or stale value** is a hardware or cable fault that should stop you acting entirely.

Watch for VWC that tracks the daily substrate-temperature swing. That is a contact or calibration artifact, not a real storage change[^kargas-temp-capacitance-correction-2012]. Watch for wetting-versus-drying paths that diverge abnormally (channeling or hydrophobic media), and for one pot that drifts away from its identically-treated siblings (a dud probe or blocked emitter).

> **DANGER — The cardinal safety rule**
>
> Temperature and EC should move your **trust** in the reading, never the stored-water number directly. A diurnal-temperature artifact can drive a real dielectric shift in dry media that mimics a water change[^nasta-2024-teros12-temp-correction]. If you let it write VWC, you will chase ghosts.

> **Diagram.** A simple decision order: rule out hardware first, then artifacts, then local faults, before believing the number.

| Symptom | Likely cause | What it is NOT | Response |
| --- | --- | --- | --- |
| VWC railed / flatline / NaN / stale | Hardware or cable fault | Real water reading | Stop steering. Run a bounded safe routine. Page a human |
| VWC swings with diurnal temp | Poor contact / cal artifact | A real water change | Down-trust absolute VWC; check contact[^kargas-temp-capacitance-correction-2012] |
| Wetting vs drying diverge oddly | Channeling / hydrophobic media | Sensor failure | Inspect media; re-wet; check probe seating |
| One pot unlike its siblings | Dud probe or blocked emitter | A plant problem (yet) | Inspect emitter and probe before blaming the plant |

*Symptom to cause to response. Note the ‘what it is NOT’ column, because misdiagnosis is the real cost.*

> **WARN — Never hard-write your anchors**
>
> Never let one manual reading or a single human observation hard-write your capacity anchor or override a safety interlock. Anchors earn their place from corroborated events, not from one good look.

## Realistic expectations

> **KEY — What one probe can and cannot earn**
>
> A single TEROS-12 will not give you a per-zone, ground-truth picture of your root zone, and treating it as one is the most common and most expensive mistake. With substrate-specific calibration you can realistically resolve dryback _trends_ and approximate stored water to about ±0.01–0.02 m³/m³ in the spot the probe occupies. That is good enough to steer if you account for the uncertainty and cross-check it.[^fragkos-2024-teros12-soils-ec]

> **Diagram.** A lone probe sits in a wide, caveat-heavy uncertainty band. Calibration plus an independent witness earns a tighter, steering-ready band.[^nemali-2006-set-point-irrigation]

- Best case with calibration: trustworthy dryback shape and ~±0.01–0.02 m³/m³ stored-water estimate for the probe's local spot.
- Not achievable alone: per-zone runoff, delivery verification, or a true zone average across pots.
- A **load cell** (pot weight) is the highest-value add-on because it is the one measurement that does not route through dielectric physics.
- Expect, and design for, explicit ‘I cannot tell’ outputs rather than false precision. Control authority should be earned, not assumed.

The mature stance is to demand that the system say _when it cannot tell_, rather than emit a confident number it has not earned. Get the probe calibrated, add one independent witness, and read the [smart watering (VWC/EC) guide](smart-watering-vrwe.html) for how those signals drive shots, and the [signal-and-noise paper](signal-and-noise.html) for separating a real trend from sensor noise.

## References

[^topp-1980-dielectric-vwc]: Topp, G. C., Davis, J. L., & Annan, A. P. (1980). Electromagnetic determination of soil water content: Measurements in coaxial transmission lines. Water Resources Research, 16(3), 574-582. https://doi.org/10.1029/WR016i003p00574 (peer-reviewed)
[^hilhorst-2000-pore-water-ec]: Hilhorst, M. A. (2000). A Pore Water Conductivity Sensor. Soil Science Society of America Journal, 64(6), 1922-1925. https://doi.org/10.2136/sssaj2000.6461922x (peer-reviewed)
[^fragkos-2024-teros12-soils-ec]: Fragkos, A., Loukatos, D., Kargas, G., & Arvanitis, K. G. (2024). Response of the TEROS 12 Soil Moisture Sensor under Different Soils and Variable Electrical Conductivity. Sensors, 24(7), 2206. https://doi.org/10.3390/s24072206 (peer-reviewed)
[^nasta-2024-teros12-temp-correction]: Nasta, P., Coccia, F., Lazzaro, U., Bogena, H. R., Huisman, J. A., Sica, B., Mazzitelli, C., Vereecken, H., & Romano, N. (2024). Temperature-Corrected Calibration of GS3 and TEROS-12 Soil Water Content Sensors. Sensors, 24(3), 952. https://doi.org/10.3390/s24030952 (peer-reviewed)
[^kargas-temp-capacitance-correction-2012]: Kapilaratne, R. G. C. J. & Lu, M. (2012). Correcting the Temperature Influence on Soil Capacitance Sensors Using Diurnal Temperature and Water Content Cycles. Sensors, 12(7), 9773-9790. https://doi.org/10.3390/s120709773 (peer-reviewed)
[^tavan-2021-sensor-irrigation-soilless]: Tavan, M., Wee, B., Brodie, G., Fuentes, S., Pang, A., & Gupta, D. (2021). Optimizing Sensor-Based Irrigation Management in a Soilless Vertical Farm for Growing Microgreens. Frontiers in Sustainable Food Systems, 4, 622720. https://doi.org/10.3389/fsufs.2020.622720 (peer-reviewed)
[^nemali-2006-set-point-irrigation]: Nemali, K. S. & van Iersel, M. W. (2006). An automated system for controlling drought stress and irrigation in potted plants. Scientia Horticulturae, 110(3), 292-297. https://doi.org/10.1016/j.scienta.2006.07.009 (peer-reviewed)
[^meter-teros12-manual]: METER Group, Inc. (2023). TEROS 11/12 User Manual & Specifications. METER Group, Pullman, WA. https://metergroup.com/products/teros-12/ (industry/manufacturer source)
