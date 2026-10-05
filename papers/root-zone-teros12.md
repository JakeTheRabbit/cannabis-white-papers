---
slug: "root-zone-teros12"
title: "TEROS-12 measurements and how to control irrigation with them"
eyebrow: "Precision · Root zone"
summary: "A TEROS-12 probe in your substrate gives three numbers: the quantity of water in the substrate, the salt concentration of the water, and the temperature. This guide gives information about each number. It shows that you must change the raw reading before it is the correct value. It also shows how to use the reading to make irrigation decisions that you can be sure of for a crop."
track: "Precision and automation"
read_time: "~18 min to read"
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

# TEROS-12 measurements and how to control irrigation with them

_Precision · Root zone · ~18 min to read_

> A TEROS-12 probe in your substrate gives three numbers: the quantity of water in the substrate, the salt concentration of the water, and the temperature. This guide gives information about each number. It shows that you must change the raw reading before it is the correct value. It also shows how to use the reading to make irrigation decisions that you can be sure of for a crop.

## Purpose and scope

A TEROS-12 is a small probe that you push into substrate: coco, rockwool or soil. It sends three numbers through one digital wire: the quantity of water in the substrate, the salt concentration of that water, and the temperature. This guide starts from zero. It gives information about each number and about how the probe gets the number. It also gives the cause of an important instruction: do not use only the raw reading to open a valve.

The probe measures a volume of approximately 1010 mL (34.2 fl oz) of substrate around its prongs. It does not measure all the root zone.[^meter-teros12-manual] The next sections show how to change that one local reading, which can have an error, into a number for irrigation control.

- The TEROS-12 gives **volumetric water content (VWC)**, **bulk electrical conductivity (EC)** and **substrate temperature** through the digital protocol SDI-12.
- The volume of influence of the probe is only approximately 1010 mL (34.2 fl oz) of substrate around the prongs. This volume is one local position. It is not the average of a tray or a zone.
- This guide changes that local reading, which has noise, into a good estimate of the quantity of water. The guide always gives the uncertainty of the estimate.
- It is not necessary to know about soil sensors before you read this guide. Each term has a definition where it first occurs.

> **Diagram.** The probe measures a small volume of substrate around the prongs, in the shape of an ellipsoid. It does not measure all the root zone.[^meter-teros12-manual]

> **NOTE: Persons for this guide**
>
> This guide is for a person who puts a moisture probe in a pot. The person wants to control irrigation with the probe and to include the uncertainty. Use this guide with the [guide to smart irrigation (VWC/EC)](smart-watering-vrwe.html) and the [paper on crop steering in coco](coco-crop-steering.html).

## Definitions

Six terms are necessary for all the information in this guide. Each term has an easy definition here. After this section, the guide uses each term with the same definition. The terms occur again in the next sections.

**Volumetric water content (VWC)**: The pot is a container with a volume that does not change. Some of the volume is solid substrate, some is air in the gaps, and some is liquid water. VWC is the fraction of the total volume that is liquid water. Its unit is cubic meters of water for each cubic meter of substrate (m³/m³). Thus a VWC of 0.34 shows that 34% of the total volume of the pot is liquid water. VWC is the primary number that you use to control irrigation.

**Permittivity (dielectric constant)**: An electric field has an effect on water that is approximately twenty times stronger than the effect on dry substrate. Permittivity is the property that shows this effect. The permittivity of water is approximately 80, of dry substrate approximately 3–5, and of air approximately 1. The probe uses this large difference to find water.[^topp-1980-dielectric-vwc]

**Capacitance sensor**: A sensor that measures permittivity. It applies a high-frequency electric field and measures how strongly the material around the sensor holds the field. The TEROS-12 is a capacitance sensor. It calculates VWC from the permittivity reading. It does not touch the water directly.

**Bulk EC and pore-water EC**: The probe measures the conductivity of all the wet substrate together: solids, water and air. This value is bulk EC (0–20000 µS/cm on this probe). The roots touch the water in the gaps between the particles of the substrate. The salt concentration of this water is the pore-water EC. The probe cannot measure pore-water EC directly. You calculate an estimate of it from bulk EC with the Hilhorst (2000) model.

**DUL / container capacity**: Drained upper limit: the quantity of water that _this pot_ holds after gravity removes all the water that it can. It is the maximum value for your steering. It is a property of your pot and substrate, not a general constant. Thus you measure it from the runoff of your pot.

**Resolution and accuracy**: Resolution is the smallest change that the probe can show: 0.001 m³/m³ VWC. Accuracy shows how near the number is to the correct value: only ±0.03 m³/m³ with the generic calibration. The probe gives a number with high precision, but precision is not the same as accuracy. A number with high precision can be incorrect each time.[^meter-teros12-manual]

> **Diagram.** The permittivity of liquid water (approximately 80) is approximately twenty times the permittivity of dry substrate (approximately 3–5) and approximately eighty times the permittivity of air (approximately 1). A small quantity of water causes a large change in the reading of the probe.[^topp-1980-dielectric-vwc]

> **Diagram.** One unit of volume of substrate has three parts: solids, air and water. VWC is the fraction of the volume that is water.

## How the probe measures water and does not touch it

The TEROS-12 is a **capacitance probe**. Its prongs send a high-frequency electric field into the substrate around them. The probe measures how strongly the substrate holds the field. This property is **permittivity**.The permittivity of water (approximately 80) is approximately twenty times the permittivity of dry substrate (approximately 3–5) and approximately eighty times the permittivity of air (approximately 1). Thus a change in water content causes a large change in the bulk permittivity of the substrate. You can calculate the size of this change. As a result, you can use permittivity to find VWC.[^topp-1980-dielectric-vwc]

Then the probe uses a **calibration equation** to change the measured permittivity to a VWC number. The equation in the probe is a generic curve for mineral soil. The probe gives the VWC number with a resolution of 0.001 m³/m³. There is a problem from the start: the equation is different for different substrates, and the generic curve has an accuracy of only ±0.03 m³/m³.[^meter-teros12-manual]

- Permittivity is the _physical_ quantity that the probe measures. VWC is a _calculated and calibrated_ estimate. It is one more step after the measurement.
- The curve from permittivity to VWC is not a straight line. It is most different from a straight line near saturation. There the curve becomes flat. A substrate that is almost full can give a ‘full’ reading when it is not full.
- The temperature of the substrate changes the dielectric response. The change is a known physical effect. It can cause a change in the reading that is the same as a change in water content. Correct the reading for this effect.[^nasta-2024-teros12-temp-correction]
- The probe sends data through SDI-12. Three values show a fault in the equipment or the cable. The first is a constant value at 0 or at full scale. The second is a ‘NaN’ value (not a number). The third is an expired value (the probe sends the last value again). These values are not readings of data.

> **Diagram.** VWC increases when the permittivity increases, but the curve bends and becomes flat near saturation. The same step of VWC is a different step of permittivity in different parts of the curve.[^topp-1980-dielectric-vwc]

> **Diagram.** From electric field to a number: each output comes from the same measurement. The error for each substrate occurs in the calibration.

## Calibrate the probe to the substrate that you use

When you receive the TEROS-12, it has a generic calibration for mineral soil. This calibration has an accuracy of only ±0.03 m³/m³. A **substrate-specific** calibration for your coco or rockwool decreases the error to ±0.01–0.02 m³/m³.[^fragkos-2024-teros12-soils-ec] This difference is important when you use the probe. Frequently, the dryback windows in crop steering are _smaller_ than the error band of the generic calibration (±0.03). If you use a VWC without calibration for steering, the changes that you want are in the noise.

An example of safe headroom shows the result of this difference. An estimate that ignores the error gives 256 mL (8.7 fl oz) of ‘room to apply water’. When you include an accuracy of ±0.02, the safe quantity is approximately 109 mL (3.7 fl oz). With the generic calibration (accuracy ±0.03), the safe quantity is only approximately 54 mL (1.8 fl oz). The pot and the probe are the same. The only difference is how you include the error band when you calculate.[^nemali-2006-set-point-irrigation]

> **Diagram.** The safe headroom decreases by a large quantity when the calibration error increases. It decreases from 256 mL (8.7 fl oz) in the raw estimate to approximately 54 mL (1.8 fl oz) with the generic curve.[^nemali-2006-set-point-irrigation]

| Calibration type | VWC accuracy | Resolution | Accurate steering? |
| --- | --- | --- | --- |
| Generic calibration for mineral soil (in the probe) | ±0.03 m³/m³ | 0.001 m³/m³ | No. The error band is wider than a usual dryback window. |
| Substrate-specific calibration | ±0.01–0.02 m³/m³ | 0.001 m³/m³ | Yes. It is necessary for accurate steering. |

*The resolution is the same for the two types. The accuracy is different. Calibrate the probe to your substrate before you use it for steering.*

> **WARN: Calibration does not correct all errors**
>
> Make sure that you use a substrate-specific calibration: it is **necessary** for accurate steering. Calibration corrects only an additive _offset_ in the reading. The gain error and the nonlinearity near saturation stay, and they do not cancel when you calculate with the reading. Include the residual error that stays after the calibration.

## The EC reading and its limits

The probe measures **bulk EC**, the conductivity of all the wet substrate (0–20000 µS/cm). Growers must know **pore-water EC**: the salt concentration of the solution that touches the roots. To calculate pore-water EC, use the Hilhorst (2000) model with bulk EC, VWC and temperature.[^hilhorst-2000-pore-water-ec] The bulk EC is the conductivity of the water and the substrate together. The Hilhorst model then gives an estimate of the conductivity of the water only.

The model gives a good estimate, but its sensitivity to its parameters is approximately ±20%. It does not give correct results when the VWC is less than 0.10 m³/m³. Do not use it in this condition.A more important limit is **representativeness**: the probe measures one position of approximately 1010 mL (34.2 fl oz). Channeling, dry areas or bad contact between the probe and the substrate can cause a number that is different from the value of the zone. The probe operates correctly at this time.[^fragkos-2024-teros12-soils-ec]

- The probe measures bulk EC (0–20000 µS/cm) directly. You calculate an estimate of pore-water EC from bulk EC. The two values are not the same.
- The conversion of Hilhorst (2000) has a sensitivity of approximately ±20%. It does not give correct results when the VWC is less than 0.10 m³/m³.[^hilhorst-2000-pore-water-ec]
- A representativeness fault: the 1010 mL (34.2 fl oz) of substrate that the probe measures can have a value that is different from the value of the zone. Channeling, an air gap or a probe that is not fully in the substrate can cause the difference. The probe operates correctly at the same time.
- The sensor cannot measure the volume of runoff from each pot. It cannot measure the effective substrate volume. This volume decreases when the roots fill the pot. It cannot find if the system supplied an irrigation shot that the controller started.

> **Diagram.** The probe measures bulk EC directly. You calculate pore-water EC with the model of Hilhorst (2000). This estimate becomes less accurate quickly when the substrate becomes dry.[^hilhorst-2000-pore-water-ec]

| The probe CAN measure | The probe CANNOT measure | Other method |
| --- | --- | --- |
| VWC (local position) | The correct average of the zone for all the pots | Many probes, a cohort model |
| Bulk EC | Runoff volume for each pot | Runoff trays / drain sensors |
| Substrate temperature | Effective substrate volume (decreases when the roots fill the pot) | Measure DUL again at intervals |
| Calculated pore-water EC | If an emitter operated | Flow meter, or a sudden change of the weight from a load cell |

*The information that one TEROS-12 can and cannot give, and the second witness (a second measurement with a different method) that fills each gap.*

## Steering of irrigation with TEROS-12 readings

The method has two parts. **Make the raw VWC reading less important.** Do not use it as a correct value. Use it as one witness that has noise, with a confidence score (a number that shows how accurate the reading is).**Make a small water-balance model more important.** The model holds the best estimate of the water in the substrate. A reading with a high confidence score can change the estimate only by a _small_ quantity.

Monitor **dryback** (the quantity by which the VWC decreases between shots) and **specific yield** (the quantity by which the VWC increases for each mL supplied). Specific yield shows when the pot comes near to its capacity. Set the capacity anchor (the DUL value that the system uses) from the DUL that you measured, and not from a number without a measurement. Control irrigation with _trends_ (the shape and the slope of the dryback) more than with the absolute value, because an additive calibration offset does not change trends.[^tavan-2021-sensor-irrigation-soilless] Do not use only a trend. Always use a second witness, for example the time of runoff or the weight of the pot.

1. **Calibrate to your substrate first**: A substrate-specific calibration is the first necessary step. If you do not have it, your steering is in the error band. You cannot be sure that the reading is sufficiently accurate.
2. **Make sure that the probe contact and position are correct**: Put the probe tightly in the substrate, in a representative position that does not change. A loose probe or an air gap gives the reading of the substrate around it. It does not give the reading of your root zone.
3. **Measure the DUL of this pot from irrigation events with a second witness**: Set the capacity anchor from approximately five irrigation events with runoff or weight data. Do not use only one irrigation event. Give the capacity anchor as a volume of water, and not as a raw VWC number.
4. **Steering with the slope of the dryback, with a limit from the safe headroom**: Use the slope of the dryback and the specific yield. Use a limit from a headroom estimate that includes the calibration error, and not from the raw estimate.
5. **Use a second witness before you apply water**: A second witness (the start of runoff or the mass from a load cell) must give the same result before a signal goes to a valve. The probe reading must not operate a valve if there is no second witness.

> **Diagram.** Irrigation shots increase the VWC to the DUL. The steering signal is the slope of the VWC when it decreases between shots, and not the absolute value at one time.

> **Diagram.** Each reading has three steps before the system can apply water: a confidence score, a water-balance model and a check by a second witness.[^tavan-2021-sensor-irrigation-soilless]

## Find the cause of a bad reading before you think that the sensor is defective

Most problems with the TEROS-12 do not occur because the sensor is defective. The problem is that a person _thinks_ that the reading is correct when it is not. First, find the difference between two conditions. An **incorrect reading** is a representativeness fault. The probe operates correctly, but the 1010 mL (34.2 fl oz) that it measures has a different value from the zone. With an incorrect reading, decrease your confidence in the absolute VWC number.A **constant, NaN or expired value** is a fault in the equipment or the cable. With this value, stop all automatic operation.

Monitor for a VWC that changes with the temperature cycle of the substrate each day. This change is not a change in the quantity of water. It is an artifact: the probe does not touch the substrate correctly, or the calibration is incorrect.[^kargas-temp-capacitance-correction-2012] Monitor the wetting curve and the drying curve of each pot. If they are different from the usual curves, the cause is possibly hydrophobic substrate or channeling.Monitor each pot that is different from the pots near it that have the same treatment. The cause is possibly a blocked emitter or a defective probe. It is not a problem of the plant.

> **DANGER: Temperature and EC change your confidence, not the water number**
>
> Do not let temperature and EC change the estimate of stored water directly. Let them change your **confidence** in the reading. The temperature cycle of each day can cause a dielectric change in dry substrate. This change is a physical effect. It has the same effect on the reading as a change in water content.[^nasta-2024-teros12-temp-correction]
> Do not let that change write the VWC. If you do, a physical effect causes the irrigation, and not the water uptake of the plant.

> **Diagram.** Do the checks in sequence: first for equipment faults, then for artifacts and then for local faults. Use the number only after these checks.

| Symptom | Possible cause | It is NOT | Task |
| --- | --- | --- | --- |
| The VWC is at the limit of the range, is constant, is ‘NaN’ or is an expired value | Fault in the equipment or the cable | A correct reading of water | Stop steering. Operate a safe procedure with limits. Tell a person. |
| The VWC changes with the temperature each day | Bad contact, or an artifact of the calibration | A change in the quantity of water | Decrease the confidence in the absolute VWC. Examine the position of the probe.[^kargas-temp-capacitance-correction-2012] |
| The wetting curve and the drying curve are very different | Channeling, or hydrophobic substrate | Defective sensor | Examine the substrate. Make the substrate wet again. Examine the position of the probe. |
| One pot is different from the pots near it | Blocked emitter or defective probe | A problem of the plant, at this time | Examine the emitter and the probe before you think that the plant has a problem. |

*From symptom to cause to task. The ‘It is NOT’ column is the most important. The primary cost is an incorrect diagnosis.*

> **WARN: Use more than one irrigation event to set a capacity anchor**
>
> Do not let one manual reading or one observation by a person set a capacity anchor. Do not let it override a safety interlock. A capacity anchor must come from more than one irrigation event, with a second witness for each irrigation event. One good observation is not sufficient.

## Expected results and limitations

> **KEY: The facts**
>
> One TEROS-12 cannot give you the correct condition of the root zone for each zone. If you think that it can, you make the most frequent error and the error with the highest cost. With a substrate-specific calibration, you can find the _trends_ of dryback. You can also calculate an estimate of the water in the substrate with an accuracy of approximately ±0.01–0.02 m³/m³ in the position of the probe. This accuracy is sufficient for steering if you include the uncertainty in your decisions and compare the data with a second witness.[^fragkos-2024-teros12-soils-ec]

> **Diagram.** Only one probe has a wide error band and many limits. When you add a substrate-specific calibration and a second witness, the error band becomes smaller. You can use this range for steering.[^nemali-2006-set-point-irrigation]

- With a substrate-specific calibration, the best result is a correct shape of the dryback. The accuracy for the stored water in the local position of the probe is approximately ±0.01–0.02 m³/m³.
- One probe cannot give the runoff for each zone. It cannot show that the system supplied water. It cannot give the correct average of the zone for all the pots.
- A **load cell** (pot weight) is the most important sensor to add, because it measures the water in the substrate directly. It does not use the dielectric properties of the substrate.
- Make the system give a clear ‘I cannot tell’ output. Do not give a precision that is higher than the accuracy. Let the system control only when the data show that it can.

The best method is to make the system show _when it cannot tell_. The system must not give a number with more confidence than the data give. Calibrate first and add a second witness. Then read the [guide to smart irrigation (VWC/EC)](smart-watering-vrwe.html) for information on how those signals control the shots. Read the [paper on signal and noise](signal-and-noise.html) for information on the difference between a trend and sensor noise.

## References

[^topp-1980-dielectric-vwc]: Topp, G. C., Davis, J. L., & Annan, A. P. (1980). Electromagnetic determination of soil water content: Measurements in coaxial transmission lines. Water Resources Research, 16(3), 574-582. https://doi.org/10.1029/WR016i003p00574 (source with peer review)
[^hilhorst-2000-pore-water-ec]: Hilhorst, M. A. (2000). A Pore Water Conductivity Sensor. Soil Science Society of America Journal, 64(6), 1922-1925. https://doi.org/10.2136/sssaj2000.6461922x (source with peer review)
[^fragkos-2024-teros12-soils-ec]: Fragkos, A., Loukatos, D., Kargas, G., & Arvanitis, K. G. (2024). Response of the TEROS 12 Soil Moisture Sensor under Different Soils and Variable Electrical Conductivity. Sensors, 24(7), 2206. https://doi.org/10.3390/s24072206 (source with peer review)
[^nasta-2024-teros12-temp-correction]: Nasta, P., Coccia, F., Lazzaro, U., Bogena, H. R., Huisman, J. A., Sica, B., Mazzitelli, C., Vereecken, H., & Romano, N. (2024). Temperature-Corrected Calibration of GS3 and TEROS-12 Soil Water Content Sensors. Sensors, 24(3), 952. https://doi.org/10.3390/s24030952 (source with peer review)
[^kargas-temp-capacitance-correction-2012]: Kapilaratne, R. G. C. J. & Lu, M. (2012). Correcting the Temperature Influence on Soil Capacitance Sensors Using Diurnal Temperature and Water Content Cycles. Sensors, 12(7), 9773-9790. https://doi.org/10.3390/s120709773 (source with peer review)
[^tavan-2021-sensor-irrigation-soilless]: Tavan, M., Wee, B., Brodie, G., Fuentes, S., Pang, A., & Gupta, D. (2021). Optimizing Sensor-Based Irrigation Management in a Soilless Vertical Farm for Growing Microgreens. Frontiers in Sustainable Food Systems, 4, 622720. https://doi.org/10.3389/fsufs.2020.622720 (source with peer review)
[^nemali-2006-set-point-irrigation]: Nemali, K. S. & van Iersel, M. W. (2006). An automated system for controlling drought stress and irrigation in potted plants. Scientia Horticulturae, 110(3), 292-297. https://doi.org/10.1016/j.scienta.2006.07.009 (source with peer review)
[^meter-teros12-manual]: METER Group, Inc. (2023). TEROS 11/12 User Manual & Specifications. METER Group, Pullman, WA. https://metergroup.com/products/teros-12/ (source from a manufacturer or industry)
