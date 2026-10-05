---
slug: "smart-watering-vrwe"
title: "The VRWE automatic irrigation controller"
eyebrow: "Precision · Automatic irrigation"
summary: "This paper shows how VRWE uses some signals together to calculate the water in the root zone more accurately than one probe. You will know the cause when VRWE waits and does not apply water. You will also know how to read the confidence of VRWE and if you can accept the estimate."
track: "Precision and automation"
read_time: "~9 min to read"
diagrams: "9 diagrams"
related: ["root-zone-teros12", "signal-and-noise", "closed-loop"]
url: "https://www.growlabs.nz/wiki/smart-watering-vrwe.html"
md_url: "https://www.growlabs.nz/wiki/papers/smart-watering-vrwe.md"
version: "1.2"
updated: "2026-07-18"
license: "CC BY-NC 4.0"
license_url: "https://creativecommons.org/licenses/by-nc/4.0/"
attribution: "The Cannabis White Papers"
refs: [{"id": "szerement-seven-rod-2019", "n": 1, "cite": "Szerement, J., Woszczyk, A., Szypłowska, A., Kafarski, M., Lewandowski, A., Wilczek, A., & Skierucha, W. (2019). A Seven-Rod Dielectric Sensor for Determination of Soil Moisture in Well-Defined Sample Volumes. Sensors, 19(7), 1646.", "url": "https://doi.org/10.3390/s19071646", "peer": true}, {"id": "mane-dielectric-calibration-review-2024", "n": 2, "cite": "Mane, S., Das, N., Singh, G., Cosh, M., & Dong, Y. (2024). Advancements in dielectric soil moisture sensor calibration: A comprehensive review of methods and techniques. Computers and Electronics in Agriculture, 218, 108686.", "url": "https://doi.org/10.1016/j.compag.2024.108686", "peer": true}, {"id": "koehler-transpiration-vpd-2023", "n": 3, "cite": "Koehler, T., Wankmüller, F. J. P., Sadok, W., & Carminati, A. (2023). Transpiration response to soil drying versus increasing vapor pressure deficit in crops: physical and physiological mechanisms and key plant traits. Journal of Experimental Botany, 74(16), 4789-4807.", "url": "https://doi.org/10.1093/jxb/erad221", "peer": true}, {"id": "owen-norden-preferential-flow-2024", "n": 4, "cite": "Owen, J., & Norden, D. (Profile Products). Understanding drainage in horticultural growing media. Greenhouse Management.", "url": "https://www.greenhousemag.com/article/growing-media-defining-drainage-improve-substrate/", "peer": false}, {"id": "hydrus-soilless-substrate-dynamics", "n": 5, "cite": "International Society for Horticultural Science (ISHS). Utilizing the HYDRUS model as a tool for understanding soilless substrate water dynamics. Acta Horticulturae 1168.", "url": "https://www.ishs.org/ishs-article/1168_41", "peer": true}]
---

# The VRWE automatic irrigation controller

_Precision · Automatic irrigation · ~9 min to read_

> This paper shows how VRWE uses some signals together to calculate the water in the root zone more accurately than one probe. You will know the cause when VRWE waits and does not apply water. You will also know how to read the confidence of VRWE and if you can accept the estimate.

## Purpose and scope

> **EVIDENCE: Weak**
>
> **Limit of the data:** The method of VRWE is good. It uses more than one signal and it is careful. You cannot be sure that VRWE does not apply too much water or not sufficient water. The sensors must be in good condition, the calibration must be correct, and the fail-safe functions must operate. Keep the emergency minimum VWC values. Make sure that a person can override VRWE.

**Virtual Root-Zone Water Estimator** (VRWE) is a software controller that selects when to apply water to a plant and how much water to apply. VRWE uses some signals together and does not obey one sensor. The name includes ‘virtual’ because VRWE does not measure the water directly. VRWE calculates the quantity of water from some signals.

Each pot has only one moisture sensor. The sensor measures only a small part of the substrate[^szerement-seven-rod-2019]. If this part is dry, or if water flows around it, the sensor shows that the pot is dry. A controller that obeys only the sensor then applies too much water and can cause damage to the plant. VRWE uses the sensor reading as one signal that it examines. VRWE does not obey the sensor.

> **Diagram.** VRWE gets one signal from the sensor. The sensor measures a small area and can be incorrect. VRWE compares this signal with other data and calculates an estimate. Then VRWE makes a careful decision. All of this paper is about the ESTIMATE step.

> **NOTE: About this paper**
>
> This paper gives information on how the system _operates_. This paper is not a report of a laboratory test. Read this paper with the [root-zone sensor](root-zone-teros12.html) paper (the quantities that one probe measures) and the [signal and noise](signal-and-noise.html) paper (how to find if a change is in the plant or only sensor noise).

## Definitions

Five terms are important in all parts of this paper. This section gives the five definitions first. It is not necessary to know them at this time, because each term occurs again in the sections that follow.

**VWC (volumetric water content)**: The quantity of water in the substrate at the position of the sensor, as a percentage. VRWE compares this sensor reading with other data.

**Runoff / drain**: Water that flows out of the bottom of the pot. The plant does not use this water.

**Full pot (DUL, drained upper limit)**: The maximum quantity of water that the pot can hold after the drainage stops. The water that you add after this point flows out as runoff.

**Channeling**: Water that flows straight down one channel and does not touch the roots. An example is a gap between the pot and the liner. All the water uses this easy channel and not the substrate. The water flows out at the bottom, and the root zone near the channel stays dry. The water goes in at the top and out at the bottom, and it does not help the plant.

**Confidence**: The value that VRWE gives to show how accurate its estimate is at this time. High confidence lets VRWE apply more water. Low confidence makes VRWE careful.

| Term | Definition |
| --- | --- |
| **VWC** | The quantity of water in the substrate at the position of the sensor |
| **Runoff / drain** | Water that flows out of the bottom of the pot |
| **Full pot (DUL)** | The maximum quantity of water that the pot holds after the drainage stops |
| **Channeling** | Water that flows to the drain and does not touch the roots |
| **Confidence** | The value that shows how accurate the estimate of VRWE is at this time |

*The five terms that are important in this paper.*

## Some signals together correct one incorrect reading

VRWE keeps a **water balance** and does not obey one probe. IN is the water that the drippers supply. The quantity is accurate because you calibrate the drippers. Thus you know accurately how much water you apply. OUT is the water that the plant uses and the runoff. The balance is the quantity of water that is in the pot.

A plant continuously absorbs water through its roots and releases the water as vapor through small pores in the leaves. When the temperature and the light intensity increase, the plant releases the vapor at a higher rate. **Transpiration** is the movement of water from the roots through the stems and out through the leaf pores as vapor.You can measure temperature and light. Thus VRWE can calculate the rate at which the plant uses water, from these readings only[^koehler-transpiration-vpd-2023]. As a result, VRWE has an estimate of OUT that does not use the sensor. VRWE compares the sensor reading with the balance. The sensor is not the only source of correct data.

> **Diagram.** VRWE calculates the water balance again in each cycle. The last number is the best estimate of VRWE for the water in the root zone. VRWE gets this number before it examines the sensor reading.

> **Diagram.** Some signals go into one estimate. VRWE has more than one signal from different sources. Thus the other signals can correct one incorrect signal, and VRWE does not obey the incorrect signal.

> **KEY: Use more than one signal**
>
> If you use only one sensor, one incorrect reading becomes an incorrect decision. If the estimate uses some signals from different sources, the other signals correct one incorrect signal. The system stays correct when one input is incorrect.

## Confidence: how sure the estimate is

VRWE gives a **confidence meter** with each estimate. The meter shows how sure VRWE is. If you have only a number, for example ‘58% wet’, you do not know how accurate the number is.

The confidence is high when the signals from different sources agree. This occurs when the sensor, the water balance and the uptake estimate show the same result. The confidence decreases when the signals do not agree. For example, the sensor shows that the substrate is dry, but the water balance shows that the pot is full.A defective sensor can only make VRWE _more careful_. The sensor cannot cause VRWE to find more room for water than the water balance shows. The water balance gives protection to the plant.

> **Diagram.** Confidence is a value on a scale. It is not a yes or no. A shot is the quantity of water that you apply in one irrigation. When the confidence is high, VRWE applies a full shot. When the confidence is moderate, VRWE applies only a small safe shot. When the confidence is low, VRWE waits or tells a person.

> **TIP: The system stays safe with a defective sensor**
>
> - Each estimate has a confidence value, and not only a number.
> - When signals from different sources agree, the confidence increases. When they do not agree, the confidence decreases.
> - Low confidence makes VRWE careful. VRWE does not apply a full shot.
> - A defective sensor causes VRWE to wait. It does not cause too much water or not sufficient water.

## Irrigation decisions

VRWE makes one of only three decisions. The decision uses two values: the **confidence** and the **headroom** (the quantity of water that you can add before the pot is full).

> **Diagram.** VRWE makes only three decisions. In all three decisions, a small temporary deficit is better than too much water when VRWE is not sure.

When the confidence is high and there is headroom, VRWE applies a full shot. When VRWE is not sure, it waits or applies a small safe shot, and it does not apply a full shot. When the signals do not agree and VRWE cannot find which signal is correct, it tells a person. In all three decisions, **a small temporary deficit of water is better than too much water if VRWE is not sure. The emergency minimum VWC is also necessary.**

> **KEY: The safe decision**
>
> Apply more water only when the confidence is high. If VRWE is not sure, it makes the safe decision. This one instruction makes automatic irrigation safe.

## How to read shared-drain measurements

In a facility, the conditions are not as easy as for one pot. Frequently, **three grow rooms drain into one shared sump** (a bucket that collects the water, with a pump). The condensate from the air conditioner (AC) and from the dehumidifier also goes into the same bucket. The pump removes the water from the bucket in a pump cycle. After a pump cycle, you cannot know if the water is from too much irrigation in a room or only from the AC condensate. VRWE finds the cause in three steps.

1. **Find the background drip**: At night, irrigation is off. The only water that goes into the sump is the condensate from the AC and from the dehumidifier. VRWE finds the quantity of this stable background drip. Then VRWE subtracts it from each reading that follows.
2. **Use different irrigation times**: Each room has a different irrigation time. Thus the time of each pump cycle agrees with the irrigation time of one room. As a result, VRWE can find which room caused each pump cycle.
3. **Show ‘not sure’ when VRWE cannot find the cause**: If two irrigations occur at the same time, VRWE cannot find the cause of a pump cycle. Then VRWE shows ‘not sure’ for the reading and gives no cause. VRWE uses the same fail-safe method in all other parts of the system.

> **Diagram.** Three rooms, the AC and the dehumidifier all send water to one sump. Thus you cannot know the cause of one pump cycle. The three steps find which room caused each pump cycle.

> **Diagram.** The rooms have different irrigation times. Thus each peak in the drain rate occurs at the time of the room that caused it. A pump cycle immediately after the irrigation of a room shows that the pots of the room are full or have too much water.

> **NOTE: The information from a pump cycle after irrigation**
>
> A pump cycle _immediately after_ the irrigation of a room shows that the pots of the room are at ‘full pot’ and that water flows out. You can use this information. It is not a fault.

## Troubleshooting

The problems below can occur. VRWE must continue to operate correctly when they occur. VRWE is the solution to these problems. The protection is the same for each problem. VRWE compares the reading with the water balance and decreases the confidence. VRWE does not do a task because of one reading that is possibly incorrect.

> **Diagram.** Three usual problems. In each problem, one signal is incorrect. None of the problems causes VRWE to make an incorrect decision. The water balance and the confidence meter show that the signals do not agree.

Look carefully at channeling, because it is not easy to find. In a container, water can flow in a **preferential flow path**, a fast channel that sends the irrigation water around the root zone[^owen-norden-preferential-flow-2024]. The volume of irrigation water that you apply is correct, but the water does not touch the roots and shows only as drain. The properties of a soilless substrate change the speed at which water flows through the substrate and out of it[^hydrus-soilless-substrate-dynamics]. Thus VRWE monitors the time of the drain and not only the volume of the drain.

> **Diagram.** A cross-section of channeling: the water goes in at the top and out at the bottom, and it does not touch the roots. In the water balance, a channel shows as a large quantity of water in and a large quantity of drain immediately after it. VRWE uses this sign to decrease the confidence.

> **WARN: The protection is always the same**
>
> VRWE does not obey a reading that is possibly incorrect. VRWE compares the reading with the water balance. If the two do not agree, VRWE decreases the confidence and is careful. One incorrect sensor reading does not cause too much water or not sufficient water for the plant.

## Expected results and limitations

> **KEY: The results that VRWE gives and the results that it does not give**
>
> 1. **The safe decision.** VRWE applies more water only when the confidence is high. When the confidence is not high, VRWE makes the safe decision. VRWE calculates estimates from signals, and it cannot know more than the signals show.
> 2. **The worst result is that VRWE is too careful.** A defective sensor makes VRWE careful. The defective sensor does not cause very bad damage. VRWE will wait or tell a person before it applies too much water or not sufficient water.
> 3. **It is usual that VRWE waits or tells a person.** VRWE must make these decisions when it is not sure. They show that the system operates correctly. They do not show a fault.
> 4. **Incorrect input gives incorrect output.** The estimate is only as good as the inputs. It is important that the volumes of the drippers are accurate and that VRWE has the drain baseline. Drift in the calibration of the sensor slowly decreases the accuracy of each estimate that uses the sensor.[^mane-dielectric-calibration-review-2024]

VRWE is slower than a timer by a small quantity, but it is much safer. At some times, VRWE waits and a controller with only a timer applies water. This difference is the correct operation of VRWE.For more information about the measurements of one probe, read the [root-zone sensor](root-zone-teros12.html) paper. VRWE finds if a change is in the plant or only sensor noise before it makes a decision. For information on this check, read the [signal and noise](signal-and-noise.html) paper.

## References

[^szerement-seven-rod-2019]: Szerement, J., Woszczyk, A., Szypłowska, A., Kafarski, M., Lewandowski, A., Wilczek, A., & Skierucha, W. (2019). A Seven-Rod Dielectric Sensor for Determination of Soil Moisture in Well-Defined Sample Volumes. Sensors, 19(7), 1646. https://doi.org/10.3390/s19071646 (source with peer review)
[^mane-dielectric-calibration-review-2024]: Mane, S., Das, N., Singh, G., Cosh, M., & Dong, Y. (2024). Advancements in dielectric soil moisture sensor calibration: A comprehensive review of methods and techniques. Computers and Electronics in Agriculture, 218, 108686. https://doi.org/10.1016/j.compag.2024.108686 (source with peer review)
[^koehler-transpiration-vpd-2023]: Koehler, T., Wankmüller, F. J. P., Sadok, W., & Carminati, A. (2023). Transpiration response to soil drying versus increasing vapor pressure deficit in crops: physical and physiological mechanisms and key plant traits. Journal of Experimental Botany, 74(16), 4789-4807. https://doi.org/10.1093/jxb/erad221 (source with peer review)
[^owen-norden-preferential-flow-2024]: Owen, J., & Norden, D. (Profile Products). Understanding drainage in horticultural growing media. Greenhouse Management. https://www.greenhousemag.com/article/growing-media-defining-drainage-improve-substrate/ (source from a manufacturer or industry)
[^hydrus-soilless-substrate-dynamics]: International Society for Horticultural Science (ISHS). Utilizing the HYDRUS model as a tool for understanding soilless substrate water dynamics. Acta Horticulturae 1168. https://www.ishs.org/ishs-article/1168_41 (source with peer review)
