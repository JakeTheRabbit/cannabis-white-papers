---
slug: "plant-biosignal-sensor"
title: "Make a plant-biosignal sensor with M5Stack and ESPHome"
eyebrow: "Assembly · Precision and automation"
summary: "Plants make small electrical signals, from microvolts to some millivolts. The signals change when the light comes on, when the water becomes low, or when the plant has stress. This guide shows how to make a sensor that records these signals, and how to change the signal into a water-status number of your own. The sensor has an M5Stack ESP32, a DC-coupled instrumentation amplifier and ESPHome, and the cost is approximately NZ$110. The sensor is not a validated meter for water or nutrients, but it shows the electrical activity of the plant in real time."
track: "Precision and automation"
read_time: "~18 min to read"
diagrams: ""
related: ["plant-state-dashboard", "signal-and-noise", "closed-loop"]
url: "https://www.growlabs.nz/wiki/plant-biosignal-sensor.html"
md_url: "https://www.growlabs.nz/wiki/papers/plant-biosignal-sensor.md"
version: "1.2"
updated: "2026-07-18"
license: "CC BY-NC 4.0"
license_url: "https://creativecommons.org/licenses/by-nc/4.0/"
attribution: "The Cannabis White Papers"
refs: [{"id": "pb_pmc_plantsignals", "n": 1, "cite": "Plant bioelectrical signals for environmental and emotional state classification (2024). PMC. (AD8232 at 400 Hz; ~85% lamp on/off detection accuracy.)", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12649952/", "peer": true}, {"id": "pb_vivent", "n": 2, "cite": "Vivent Biosignals, VITA1 plant-driven cultivation sensor (manufacturer documentation).", "url": "https://vivent-biosignals.com/plant-driven-cultivation/", "peer": false}, {"id": "pb_najdenovska_stress", "n": 3, "cite": "Najdenovska E et al. (2021). Identifying general stress in commercial tomatoes based on machine learning applied to plant electrophysiology. Applied Sciences, 11(12):5640.", "url": "https://doi.org/10.3390/app11125640", "peer": true}, {"id": "pb_ad8232_ds", "n": 4, "cite": "Analog Devices, AD8232 single-lead heart rate monitor front end (data sheet). High-pass and low-pass filter design.", "url": "https://www.analog.com/media/en/technical-documentation/data-sheets/ad8232.pdf", "peer": false}, {"id": "pb_mdpi_ad8232", "n": 5, "cite": "Marques JAL et al. (2023). From AD8232 to biopotentials sensors: open-source project and benchmark. Electronics (MDPI), 12(4):833.", "url": "https://www.mdpi.com/2079-9292/12/4/833", "peer": true}, {"id": "pb_ad623_ds", "n": 6, "cite": "Analog Devices, AD623 single-supply, rail-to-rail, low cost instrumentation amplifier (data sheet).", "url": "https://www.analog.com/media/en/technical-documentation/data-sheets/ad623.pdf", "peer": false}, {"id": "pb_ads1115_ds", "n": 7, "cite": "Texas Instruments, ADS111x ultra-small, low-power, I2C-compatible, 16-bit ADCs (data sheet SBAS444).", "url": "https://www.ti.com/lit/ds/symlink/ads1115.pdf", "peer": false}, {"id": "pb_esphome_ads1115", "n": 8, "cite": "ESPHome, ADS1115 4-channel 16-bit A/D converter component (documentation).", "url": "https://esphome.io/components/sensor/ads1115/", "peer": false}, {"id": "pb_hackster_flora", "n": 9, "cite": "Verma A. Interacting with the Flora: an ESP32 + AD8232 + BH1750 + DS18B20 plant-signal rig. Hackster.io.", "url": "https://www.hackster.io/ankurverma608/interacting-with-the-flora-7ef65f", "peer": false}, {"id": "pb_arxiv_esp32", "n": 10, "cite": "AD8232 bioelectric signal processing with ESP32 (2025). arXiv:2505.18173.", "url": "https://arxiv.org/pdf/2505.18173", "peer": false}]
---

# Make a plant-biosignal sensor with M5Stack and ESPHome

_Assembly · Precision and automation · ~18 min to read_

> Plants make small electrical signals, from microvolts to some millivolts. The signals change when the light comes on, when the water becomes low, or when the plant has stress. This guide shows how to make a sensor that records these signals, and how to change the signal into a water-status number of your own. The sensor has an M5Stack ESP32, a DC-coupled instrumentation amplifier and ESPHome, and the cost is approximately NZ$110. The sensor is not a validated meter for water or nutrients, but it shows the electrical activity of the plant in real time.

## Purpose and scope

Plants make small electrical signals. When a plant changes in response to light, water, a wound or a change in nutrients, ions move across the cell membranes. This movement makes a voltage of less than one millivolt to some millivolts. You can read this voltage with electrodes on the stem[^pb_pmc_plantsignals]. Commercial units, for example the Vivent VITA1, do the same. They then use trained models to calculate the water condition and the stress condition from the signal[^pb_vivent][^pb_najdenovska_stress].

The water signal is slow. It is a drift of the baseline over minutes and hours. Thus the amplifier must be **DC-coupled**: it must pass a voltage that changes slowly, and also a voltage that does not change. An ECG chip such as the AD8232 is not correct for this work. Its high-pass filter removes all the signal that is slower than approximately 0.5 Hz[^pb_ad8232_ds]. This guide uses an AD623 instrumentation amplifier with no high-pass filter, and a 16-bit ADS1115 ADC[^pb_ad623_ds]. The cost is approximately NZ$110.

> **NOTE: Functions and limits of this sensor**
>
> - **This sensor does the same data acquisition.** It records the raw signal, the slow drift, the rhythm of each day, the large deflections after a stress event and the change when the light starts and stops. It records all of this in Home Assistant.
> - **This sensor does not give the model of the commercial product.** The water, N, P, K and Ca readings of a VITA1 come from a trained model and a library of signals. Section 10 shows how to train a model of your own with the sensors that you have now.
> - **ESPHome reads the sensor at set intervals. It does not record fast waveforms.** This sensor records trends and events of some seconds or longer. For spikes of less than one second, refer to section 11.

## Definitions

**Biopotential**: Each living cell has a difference of electrical charge across its membrane. The membrane has a positive side and a negative side, as a small battery has. When ions move because of light, water or stress, this difference changes. Then you can measure the voltage from the outer side of the tissue. In plants, the voltage is from some microvolts to some millivolts. It is on a baseline that changes slowly.

**Variation potential**: A part of a plant can have a wound or a strong stress. Then the balance of electrical charge across the cell membranes in that area changes quickly. This change moves along the plant as an electrical wave. This wave is a variation potential. It is the large, slow deflection that you see on your trace after a stress event. It is the event that is the easiest to see on a DIY sensor.

**Action potential**: A fast electrical spike. After it starts, it continues to move along the tissue. Action potentials occur in plants, but each action potential is shorter than one second. Thus a high sampling rate is necessary to record them. This sensor measures slow trends and not action potentials.

**DC-coupled**: An amplifier that is DC-coupled passes all the frequencies down to 0 Hz. A voltage that does not change goes through it. An AC-coupled amplifier has a high-pass filter, which removes the slow part of the signal. The slow part is the part that shows the water condition of the plant.

**Instrumentation amplifier**: An amplifier that measures the difference between two inputs. It removes the part of the signal that is the same on the two inputs, for example the mains hum. This is **common-mode rejection**. The inputs have a very high impedance, thus they take almost no current from the plant.

**Electrode**: The metal contact that connects the voltage of the plant to your circuit. The contact is a stainless needle in the stem, or an Ag/AgCl cup with gel on the surface.

**Half-cell potential**: When metal touches wet tissue, ions move at the surface and make a small voltage. The voltage can be tens of millivolts, and it is different for each electrode. It is larger than the plant signal. The circuit and the software in this guide must accept it and then remove it.

**ADC**: Analog-to-digital converter. It changes the analog voltage of the amplifier into numbers that a microcontroller can read. In this sensor, the ADC is a 16-bit ADS1115 that connects through I2C.

## The signal chain

The sensor is a chain from the plant to the dashboard. Two needle electrodes measure the stem. One electrode in the root zone holds the plant at a bias voltage. A low-pass filter removes the fast noise. The AD623 amplifies the difference 10 times. The ADS1115 digitizes it. The ESP32 sends it to Home Assistant.

> **Diagram.** The signal chain. Filter, amplify and then digitize. The same I2C bus also connects the light sensor, the temperature sensor and the humidity sensor. These sensors give information about the conditions at the time of the plant trace.

> **KEY: Why not the AD8232 module?**
>
> Many DIY plant sensors use the AD8232 heart-rate module, because it is cheap and it has good common-mode rejection[^pb_mdpi_ad8232]. But the AD8232 is an ECG chip. Its high-pass filter removes the half-cell potential of the electrodes, and it also removes all the plant signal that is slower than approximately 0.5 Hz[^pb_ad8232_ds]. A change in water condition occurs over minutes or hours. Thus the AD8232 removes the signal that you want.
> The AD8232 is correct for fast events: a light step, a touch, a wound. It is not correct for the water trend. For this work, use a DC-coupled amplifier.

## Bill of materials

> **EVIDENCE: Weak**
>
> **Provisional and experimental:** This sensor records biopotentials as relative values, for education and to find correlations. It is _not_ a validated meter for water, nutrients or stress. Do not use only this signal to make a decision about irrigation or feed.

The cost is approximately NZ$110. The M5Stack parts are Grove modules that you connect together. The front-end is a small board that you solder. All its parts are through-hole parts, thus a beginner can solder them. The prices are approximate values for the middle of 2026.

| Part | Function | Where to get it | Approximate NZD |
| --- | --- | --- | --- |
| **M5StickC PLUS2** ESP32 with screen and LiPo battery | Controller and display | [M5Stack shop](https://shop.m5stack.com/products/m5stickc-plus2-esp32-mini-iot-development-kit) (end of life, EOL: M5StampS3 replaces it) | 32 |
| **ENV IV Unit** (SHT40 + BMP280) | Air temperature, humidity, pressure | [M5Stack shop](https://shop.m5stack.com/products/env-iv-unit-with-temperature-humidity-air-pressure-sensor-sht40-bmp280) | 14 |
| **DLight Unit** (BH1750) | Light intensity (lux) | [M5Stack shop](https://shop.m5stack.com/products/dlight-unit-ambient-light-sensor-bh1750fvi-tr) | 12 |
| **1-to-3 HUB Unit** (passive I2C splitter) | Connect three devices to one bus | [M5Stack shop](https://shop.m5stack.com/products/mini-hub-module) | 6 |
| **AD623ANZ** (8-pin DIP) and an 8-pin socket | DC-coupled instrumentation amplifier [not from M5Stack] | Electronics distributors (RS, Digi-Key, Mouser, element14) | 12 |
| **ADS1115 breakout** (16-bit I2C ADC) | Digitize the amplifier output [not from M5Stack] | [Adafruit product 1085](https://www.adafruit.com/product/1085) · equivalent, approximately NZ$6 | 6 |
| Resistors: 11 kΩ (1), 10 kΩ (3), 1.5 kΩ (1), 1 kΩ (1). Capacitors: 1 µF film (1), 10 µF (1), 100 nF (1) | Gain, input filter, bias voltage, supply decoupling | Any electronics shop | 4 |
| **Electrodes**: stainless needles (acupuncture type) with snap leads, _or_ Ag/AgCl EEG cups | Contact with the plant [not from M5Stack] | [SparkFun sensor cable](https://www.sparkfun.com/products/12970), or a medical set of electrodes | 14 |
| Small prototype board, DuPont jumper wires, heatshrink, shielded twin cable | Front-end board and electrode leads | Your spare parts, or an electronics shop | 10 |
| Total: approximately NZ$110. If the controller is an M5StampS3 and not the StickC, the total is less than NZ$95. The alternative does not have the screen that is on the board of the StickC. |

> **WARN: Two parts are at the end of their life (EOL)**
>
> M5Stack stopped the production of the StickC PLUS2 and the ENV IV. But resellers (RobotShop, Botland, TinyTronics) continue to have them in stock, and they have the most tutorials. If you want current parts, the **M5StampS3** replaces the controller and the **ENV Pro** replaces the ENV IV. In the firmware, only two I2C pin numbers change.

## The front-end circuit

The front-end has three parts: a bias voltage, an input filter and the amplifier. Solder them on one small prototype board. Put the AD623 in a socket.

1. **Make the bias voltage**: Connect a 1.5 kΩ resistor from 3.3 V to a point that is the **BIAS** node, and a 1 kΩ resistor from BIAS to GND. Put the 10 µF capacitor from BIAS to GND. BIAS is 3.3 × 1 / 2.5 = 1.32 V. This voltage is in the input range of the AD623 on a 3.3 V supply, which goes up to 3.3 − 1.5 = 1.8 V[^pb_ad623_ds].
2. **Make the input filter**: Put a 10 kΩ resistor in series with each stem electrode lead. After the resistors, put the 1 µF film capacitor between the two leads. The cut-off is 1 / (2π × 20 kΩ × 1 µF) ≈ 8 Hz. The filter removes radio noise and much of the mains hum. It does not touch the slow plant signal.
3. **Connect the amplifier**: Make the connections in the table below. The 11 kΩ resistor sets the gain: G = 1 + 100 kΩ / 11 kΩ = 10.09[^pb_ad623_ds]. Put the 100 nF capacitor from pin 7 to pin 4, near the chip.
4. **Connect the soil electrode**: Connect the root-zone electrode to BIAS through a 10 kΩ resistor. This holds the plant at 1.32 V, in the input range of the amplifier. It also gives a path for the small input current of the AD623.

| AD623 pin | Name | Connect to |
| --- | --- | --- |
| 1 and 8 | −RG, +RG | 11 kΩ resistor between the two pins (gain 10.09) |
| 2 | −IN | Lower-stem electrode, after its 10 kΩ resistor |
| 3 | +IN | Upper-stem electrode, after its 10 kΩ resistor |
| 4 | −VS | GND |
| 5 | REF | BIAS (1.32 V) |
| 6 | OUTPUT | ADS1115 A0 |
| 7 | +VS | 3.3 V |
| — | BIAS node | ADS1115 A1, and the soil electrode through 10 kΩ |

*AD623 connections (8-pin DIP).*

> **KEY: The numbers: why gain 10 is correct**
>
> The half-cell potential of the electrodes can be tens of millivolts. Together with the plant signal, the input can be up to approximately ±100 mV. At gain 10, the output moves ±1 V around BIAS. The AD623 output can go from 0.01 V up to approximately 3.15 V on a 3.3 V supply[^pb_ad623_ds]. Thus there is space for the offset, and the output does not stop at a rail.
> The ADS1115 measures A0 minus A1 at the ±2.048 V range. One bit is 62.5 µV at the ADC, thus 6.2 µV at the electrodes[^pb_ads1115_ds]. This resolution is sufficient for the slow plant signal. A higher gain gives more resolution, but then a large electrode offset can push the output to a rail.

> **TIP: Why the ADC does not connect directly to the electrodes**
>
> The ADS1115 has an input impedance of some megohms, and the impedance decreases at its small input ranges[^pb_ads1115_ds]. A needle in a stem has a high source impedance. The ADC takes current from the plant and the reading decreases and drifts. The AD623 has an input impedance of 2 GΩ and an input current of a maximum of 25 nA[^pb_ad623_ds]. Thus it takes almost no current from the plant.

## Wiring

After the controller, the sensor has one I2C bus. The HUB connects this bus to three devices. Two analog wires go from the front-end board to the ADS1115: the amplifier output to A0, and BIAS to A1. The ADS1115 measures the difference between them, thus the 1.32 V bias does not show in the reading.

> **Diagram.** The wiring. One I2C bus (SDA blue, SCL green, power red) connects the controller to three devices through the HUB. The two analog connections (amber) go from the AD623 board to A0 and A1 of the ADS1115.

| From | Pin | To | Pin or target |
| --- | --- | --- | --- |
| M5 Grove Port A | SDA (G32) | HUB → all I2C devices | SDA |
| M5 Grove Port A | SCL (G33) | HUB → all I2C devices | SCL |
| M5 Grove Port A | 5V / GND | HUB → ENV and DLight | VDD / GND |
| M5 3V3 pin | 3.3V / GND | ADS1115 and AD623 board | VDD / GND |
| AD623 board | OUTPUT (pin 6) | ADS1115 | A0 |
| AD623 board | BIAS | ADS1115 | A1 |
| AD623 board | +IN / −IN / SOIL | electrodes | upper stem, lower stem, root zone |

> **WARN: Supply the front-end with clean 3.3 V**
>
> Use the 3.3 V rail for the AD623, the bias divider and the ADS1115. Do not use the 5 V USB rail, because it has more noise, and because an output above 3.3 V can damage the ADS1115 inputs. Keep the electrode leads short. Use shielded twin cable, and connect the shield to GND at the board end only. Put the leads away from lights, ballasts and pumps. A battery (the LiPo of the StickC) gives less noise than USB power.

## Electrodes and their position

**Contact impedance** is the resistance between the metal of the electrode and the tissue of the plant. A bad connection decreases the signal and lets noise go in. The quality of the electrode contact is the one variable that you control. You can use one of these two alternatives[^pb_hackster_flora]:

**Stainless needles (recommended)**

Put the needle 2 to 3 mm (0.08 to 0.12 in) into the stem. This alternative is the most stable over weeks, and it is the method of commercial units. But it causes a wound in the plant. Thus put the needle in the plant one time only, and use a clean sterilized needle.

**Ag/AgCl EEG cups**

Fill the cup with conductive gel and attach it to the stem with tape. It does not cause a wound in the plant. But the gel becomes dry, and each new gel changes the offset. This alternative is better for a short test than for a full grow.

1. **Put the pair of electrodes along the stem**: Put +IN on the upper stem near a node. Put −IN 5 to 15 cm (2 to 6 in) below +IN on the same stem. This pair of electrodes records the signal that moves along the stem.
2. **Put the soil electrode in the root zone**: Put the SOIL electrode in the moist substrate. It holds the plant at the bias voltage. Without it, the inputs float and the reading goes to a rail.
3. **Fix the leads**: Attach each lead to the stem or the stake with tape, so that the leads do not pull the needles. A lead that moves gives a large deflection that is not from the plant.
4. **Wait until the signal is stable**: The half-cell potential of a new electrode drifts. Wait at least one hour, and for needles one day, before you use the trace. The first drift comes from the chemistry of the electrode and from the wound, not from the condition of the plant.

> **DANGER: Needle electrodes cause a wound in the plant**
>
> Make one clean insertion only, with a needle that you sterilized with alcohol. Do not make a row of holes around the stem, because a row of holes can girdle the stem. A new insertion causes a variation potential. You can use it one time as a known stimulus. Then let the wound close.

## ESPHome firmware

The full configuration follows. Put your Wi-Fi, API and OTA secrets in the file `secrets.yaml` of ESPHome. Install the firmware from the ESPHome dashboard. Home Assistant then finds the sensor automatically. For a StampS3 or a Core2, change the board setting. If it is necessary, also change the two I2C pins. The configuration passes `esphome config` on ESPHome 2026.7.

esphome:
  name: plant-biosignal
  friendly_name: Plant Biosignal

esp32:
  board: m5stick-c            # Core2 -> m5stack-core2 ; Stamp S3 -> m5stack-stamps3
  framework: { type: arduino }

logger:
api:
  encryption: { key: !secret api_key }
ota:
  - platform: esphome
    password: !secret ota_pw
wifi:
  ssid: !secret wifi_ssid
  password: !secret wifi_password

# ---- I2C bus (Grove Port A on StickC PLUS2 / Core2) ----
i2c:
  sda: 32
  scl: 33
  frequency: 400kHz
  scan: true

# ---- 16-bit ADC ----
ads1115:
  - address: 0x48

substitutions:
  amp_gain: "10.09"           # AD623 gain = 1 + 100k / 11k

sensor:
  # === PLANT BIOPOTENTIAL (DC-coupled) ===
  # A0 = AD623 output, A1 = bias node (1.32 V). Differential, so the bias cancels.
  - platform: ads1115
    multiplexer: 'A0_A1'
    gain: 2.048                 # +/-2.048 V FSR = 62.5 uV per bit at the ADC
    sample_rate: 8              # slowest rate = most mains rejection
    name: "Plant Biosignal ADC"
    id: bio_adc
    unit_of_measurement: "V"
    accuracy_decimals: 5
    update_interval: 1s
    internal: true

  # Voltage at the electrodes, in mV. 10-second mean.
  - platform: template
    name: "Plant Biopotential"
    id: bio_mv
    unit_of_measurement: "mV"
    accuracy_decimals: 3
    update_interval: 1s
    lambda: |-
      return id(bio_adc).state * 1000.0 / ${amp_gain};
    filters:
      - sliding_window_moving_average: { window_size: 10, send_every: 10 }

  # 5-minute mean: the slow drift that carries the water signal.
  - platform: copy
    source_id: bio_mv
    name: "Plant Biopotential 5 min"
    filters:
      - sliding_window_moving_average: { window_size: 30, send_every: 30 }

  # Signal minus its own 30-minute baseline: events and daily rhythm,
  # without the electrode offset.
  - platform: template
    name: "Plant Biopotential Detrended"
    id: bio_detrend
    unit_of_measurement: "mV"
    accuracy_decimals: 3
    update_interval: 10s
    lambda: |-
      static float base = NAN;
      float x = id(bio_mv).state;
      if (isnan(x)) return NAN;
      if (isnan(base)) base = x;
      base += 0.0056f * (x - base);   // time constant = 10 s / 0.0056 = ~30 min
      return x - base;

  # === ENVIRONMENT (ENV IV Unit) ===
  - platform: sht4x
    address: 0x44
    temperature: { name: "Grow Air Temp", id: air_t }
    humidity:    { name: "Grow Humidity", id: air_rh }
  - platform: bmp280_i2c
    address: 0x76
    temperature: { name: "Grow Baro Temp" }
    pressure:    { name: "Grow Pressure" }

  # === LIGHT (DLight Unit) ===
  - platform: bh1750
    address: 0x23
    name: "Grow Light"
    update_interval: 10s

  # === DERIVED: VPD (kPa) ===
  - platform: template
    name: "Grow VPD"
    unit_of_measurement: "kPa"
    accuracy_decimals: 2
    update_interval: 10s
    lambda: |-
      float t = id(air_t).state;
      float rh = id(air_rh).state;
      float es = 0.6108 * exp(17.27 * t / (t + 237.3));  // saturation vapour pressure
      return es * (1.0 - rh / 100.0);

# === Electrode fault: amplifier output at a rail (lead off or dry contact) ===
binary_sensor:
  - platform: template
    name: "Electrode Fault"
    device_class: problem
    lambda: |-
      float v = id(bio_adc).state;
      return isnan(v) || v < -1.25 || v > 1.75;
    filters:
      - delayed_on: 30s

| Entity | What it shows | Use it for |
| --- | --- | --- |
| Plant Biopotential | Voltage at the electrodes in mV, 10-second mean, offset included | Events: light steps, touch, wound |
| Plant Biopotential 5 min | The same value, 5-minute mean | The slow drift, and the input to the model in section 10 |
| Plant Biopotential Detrended | The signal minus its own 30-minute baseline | The rhythm of each day and the response to each irrigation, without the electrode offset |
| Electrode Fault | On when the amplifier output stays near a rail for 30 s | An alert: a lead is off or an electrode has no contact |

> **KEY: No calibration at the first start**
>
> The ADS1115 measures A0 minus A1, thus the 1.32 V bias does not show in the reading[^pb_esphome_ads1115]. `Plant Biopotential` shows the true voltage at the electrodes, which includes the half-cell offset. The offset is different each time that you attach the electrodes. Do not try to set it to zero. Use the detrended entity, or the changes in the 5-minute entity.

## How to read plant-biosignal data

The values are _changes_ of the potential. They are not a calibrated physiological unit. Compare a plant with the same plant at other times. Do not compare plants with each other in raw millivolts.

| Signal that you see | Possible condition |
| --- | --- |
| The detrended signal increases and decreases smoothly each day, at the same time as the light sensor | The circadian rhythm of a plant in good condition. This rhythm is the baseline. |
| A step change at the same time as the lights come on or go off | Response to light. One investigation detected the light state with approximately 85% accuracy[^pb_pmc_plantsignals] |
| A response some minutes after each irrigation, that becomes smaller or larger over the day | The response of the plant to water. Compare this response with your substrate readings in section 10. |
| A fast deflection, then the signal goes back to the baseline slowly, after you touch or move the plant | A variation potential. It is the usual signal of a wound or stress. |
| A slow drift over some days, in one direction, with no change in the grow | Usually electrode drift. Needles drift less than gel cups after the first day. |
| 50/60 Hz noise that is larger than all the other signals | Mains pickup. Make the leads shorter, use shielded cable, and examine the soil electrode. |
| Electrode Fault is on | A lead is off, an electrode has no contact, or the offset is too large for gain 10. Examine the electrodes. |

## From millivolts to a water-status estimate

A commercial unit changes the signal into a water status with a trained model. The model learns which features of the signal occur with each plant condition[^pb_najdenovska_stress]. You can do the same at a small scale. You need the biosignal and a **label**: a measured value that you want the model to estimate. A substrate moisture sensor in the same pot or slab is a good label, because it gives a number all the time.

1. **Record for 3 to 4 weeks**: Put the sensor on a plant that has a substrate moisture sensor near its roots. Keep the Home Assistant recorder (or InfluxDB) on for the biosignal, the substrate moisture, the light and the irrigation events. Do not move the electrodes in this period.
2. **Export the data**: In the Home Assistant History panel, select each entity and download the data as CSV. You get one file for each entity, with the columns `entity_id`, `state` and `last_changed`.
3. **Calculate features in windows**: Cut the biosignal into 10-minute windows. For each window, calculate the spread, the slope, the range and the mean minus the median of the last 24 hours. Do not use the raw mean, because the electrode offset is in it.
4. **Train and test**: Train a simple model to estimate the substrate moisture from the features. Test it on full days that the model did not see. Compare the error with a model that always gives the average value. If your model is not better, the signal does not carry the water information on your plant and your electrodes.
5. **Use it as an advisory only**: If the model is better, show its estimate in Home Assistant next to the substrate sensor. Do not let it control irrigation until it agrees with the substrate sensor for a full crop cycle.

import numpy as np, pandas as pd
from sklearn.linear_model import RidgeCV
from sklearn.model_selection import GroupKFold, cross_val_predict

def load(path):
    df = pd.read_csv(path, parse_dates=["last_changed"])
    s = pd.to_numeric(df["state"], errors="coerce")
    return pd.Series(s.values, index=df["last_changed"]).dropna().sort_index()

bio = load("plant_biopotential.csv")      # sensor.plant_biopotential (10 s)
vwc = load("substrate_moisture.csv")      # your substrate sensor, % VWC
lux = load("grow_light.csv")

w = bio.resample("10min")
X = pd.DataFrame({
    "spread": w.std(),
    "slope":  w.apply(lambda s: np.polyfit(np.arange(len(s)), s.values, 1)[0]
                      if len(s) > 2 else np.nan),
    "range":  w.max() - w.min(),
    "level":  w.mean() - w.mean().rolling("24h").median(),
    "lux":    lux.resample("10min").mean(),
})
d = X.join(vwc.resample("10min").mean().rename("vwc")).dropna()

days = d.index.date                       # test on full days the model did not see
pred = cross_val_predict(RidgeCV(alphas=np.logspace(-3, 3, 13)),
                         d.drop(columns="vwc"), d["vwc"],
                         groups=days, cv=GroupKFold(n_splits=5))
print("model error,    % VWC:", round(np.abs(pred - d["vwc"]).mean(), 2))
print("average-only error, % VWC:", round(np.abs(d["vwc"] - d["vwc"].mean()).mean(), 2))

> **WARN: A good score on one plant is not a general model**
>
> The model learns your plant, your electrodes and your substrate. When you move the electrodes or change the cultivar, train it again. The commercial models use data from many plants and many grows. Your first model uses data from one plant.

## Limits, calibration and safety

> **KEY: Limits to know before you solder**
>
> - **Relative values, not absolute values.** The values are good for trends and events on one plant. They are not good to compare plants or to read a calibrated number.
> - **Electrode drift.** A DC-coupled sensor also records the slow drift of the electrodes. Use needles, let them become stable, and use the detrended entity or the 24-hour median in the model.
> - **The noise floor is higher than in commercial units.** The items that give the largest decrease in noise are a battery supply, short shielded leads and a small enclosure.
> - **ESPHome is for trends.** To record spikes of less than one second, add an AD8232 module as a second channel on A2, and install an Arduino sketch that samples it at 400 Hz. The investigation of plant signals used this rate[^pb_arxiv_esp32]. Use the AD8232 channel for fast events and the AD623 channel for the trend.

> **DANGER: Keep the sensor isolated**
>
> Keep the sensor at a low voltage. Supply it with a battery or with USB. Do not connect the plant electrodes to an item that has a connection to the mains. Use one common ground only. Thus there is no ground loop through the plant.

## References

[^pb_pmc_plantsignals]: Plant bioelectrical signals for environmental and emotional state classification (2024). PMC. (AD8232 at 400 Hz; ~85% lamp on/off detection accuracy.) https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12649952/ (source with peer review)
[^pb_vivent]: Vivent Biosignals, VITA1 plant-driven cultivation sensor (manufacturer documentation). https://vivent-biosignals.com/plant-driven-cultivation/ (source from a manufacturer or industry)
[^pb_najdenovska_stress]: Najdenovska E et al. (2021). Identifying general stress in commercial tomatoes based on machine learning applied to plant electrophysiology. Applied Sciences, 11(12):5640. https://doi.org/10.3390/app11125640 (source with peer review)
[^pb_ad8232_ds]: Analog Devices, AD8232 single-lead heart rate monitor front end (data sheet). High-pass and low-pass filter design. https://www.analog.com/media/en/technical-documentation/data-sheets/ad8232.pdf (source from a manufacturer or industry)
[^pb_mdpi_ad8232]: Marques JAL et al. (2023). From AD8232 to biopotentials sensors: open-source project and benchmark. Electronics (MDPI), 12(4):833. https://www.mdpi.com/2079-9292/12/4/833 (source with peer review)
[^pb_ad623_ds]: Analog Devices, AD623 single-supply, rail-to-rail, low cost instrumentation amplifier (data sheet). https://www.analog.com/media/en/technical-documentation/data-sheets/ad623.pdf (source from a manufacturer or industry)
[^pb_ads1115_ds]: Texas Instruments, ADS111x ultra-small, low-power, I2C-compatible, 16-bit ADCs (data sheet SBAS444). https://www.ti.com/lit/ds/symlink/ads1115.pdf (source from a manufacturer or industry)
[^pb_esphome_ads1115]: ESPHome, ADS1115 4-channel 16-bit A/D converter component (documentation). https://esphome.io/components/sensor/ads1115/ (source from a manufacturer or industry)
[^pb_hackster_flora]: Verma A. Interacting with the Flora: an ESP32 + AD8232 + BH1750 + DS18B20 plant-signal rig. Hackster.io. https://www.hackster.io/ankurverma608/interacting-with-the-flora-7ef65f (source from a manufacturer or industry)
[^pb_arxiv_esp32]: AD8232 bioelectric signal processing with ESP32 (2025). arXiv:2505.18173. https://arxiv.org/pdf/2505.18173 (source from a manufacturer or industry)
