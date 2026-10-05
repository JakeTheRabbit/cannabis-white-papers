---
slug: "plant-biosignal-sensor"
title: "Make a plant-biosignal sensor with M5Stack and ESPHome"
eyebrow: "Assembly · Precision and automation"
summary: "Plants make small electrical signals, from microvolts to some millivolts. The signals change when the light comes on, when the water becomes low, or when the plant has stress. This guide shows how to make the sensor that records these signals. The sensor has an M5Stack ESP32, an ECG front-end chip and ESPHome, and the cost is approximately NZ$110. You will record the raw trace in Home Assistant and know how to read the rhythm of each day and the stress events. The sensor is not a validated meter for water or nutrients, but it shows the electrical activity of the plant in real time."
track: "Precision and automation"
read_time: "~14 min to read"
diagrams: ""
related: ["plant-state-dashboard", "signal-and-noise", "closed-loop"]
url: "https://www.growlabs.nz/wiki/plant-biosignal-sensor.html"
md_url: "https://www.growlabs.nz/wiki/papers/plant-biosignal-sensor.md"
version: "1.2"
updated: "2026-07-18"
license: "CC BY-NC 4.0"
license_url: "https://creativecommons.org/licenses/by-nc/4.0/"
attribution: "The Cannabis White Papers"
refs: [{"id": "pb_mdpi_ad8232", "n": 1, "cite": "Marques JAL et al. (2023). From AD8232 to biopotentials sensors: open-source project and benchmark. Electronics (MDPI), 12(4):833.", "url": "https://www.mdpi.com/2079-9292/12/4/833", "peer": true}, {"id": "pb_arxiv_esp32", "n": 2, "cite": "AD8232 bioelectric signal processing with ESP32 (2025). arXiv:2505.18173.", "url": "https://arxiv.org/pdf/2505.18173", "peer": false}, {"id": "pb_pmc_plantsignals", "n": 3, "cite": "Plant bioelectrical signals for environmental and emotional state classification (2024). PMC. (AD8232 at 400 Hz; ~85% lamp on/off detection accuracy.)", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12649952/", "peer": true}, {"id": "pb_hackster_flora", "n": 4, "cite": "Verma A. Interacting with the Flora: an ESP32 + AD8232 + BH1750 + DS18B20 plant-signal rig. Hackster.io.", "url": "https://www.hackster.io/ankurverma608/interacting-with-the-flora-7ef65f", "peer": false}, {"id": "pb_vivent", "n": 5, "cite": "Vivent Biosignals, VITA1 plant-driven cultivation sensor (manufacturer documentation).", "url": "https://vivent-biosignals.com/plant-driven-cultivation/", "peer": false}, {"id": "pb_esphome_ads1115", "n": 6, "cite": "ESPHome, ADS1115 4-channel 16-bit A/D converter component (documentation).", "url": "https://esphome.io/components/sensor/ads1115/", "peer": false}]
---

# Make a plant-biosignal sensor with M5Stack and ESPHome

_Assembly · Precision and automation · ~14 min to read_

> Plants make small electrical signals, from microvolts to some millivolts. The signals change when the light comes on, when the water becomes low, or when the plant has stress. This guide shows how to make the sensor that records these signals. The sensor has an M5Stack ESP32, an ECG front-end chip and ESPHome, and the cost is approximately NZ$110. You will record the raw trace in Home Assistant and know how to read the rhythm of each day and the stress events. The sensor is not a validated meter for water or nutrients, but it shows the electrical activity of the plant in real time.

## Purpose and scope

Plants make small electrical signals. When a plant changes in response to light, water, a wound or a change in nutrients, ions move across the cell membranes. This movement makes a voltage of less than one millivolt. You can read this voltage with electrodes on the stem[^pb_pmc_plantsignals]. Commercial units, for example the Vivent VITA1, do the same. They then use trained models to calculate the water condition and the stress condition from the drift of the signal[^pb_vivent].

To read a plant is the same electrical problem as to read a heartbeat. The voltage is small, it has noise, and it has high impedance. You must amplify it and not increase the noise. Thus the **AD8232**, a standard ECG front-end chip with a low cost, is correct for plants without changes[^pb_mdpi_ad8232]. Connect this chip to an ESP32 and ESPHome, and you have a plant-biosignal sensor that records data. The cost is approximately NZ$110.

> **NOTE: Functions and limits of this sensor**
>
> - **This sensor does the same data acquisition.** It records the raw signal and the rhythm of each day. It also records the large deflections after a stress event and the change when the light starts and stops. One investigation gave a detection rate of approximately 85% for the light changes, with its protocol. It is not sure that you get the same value with this type of hardware[^pb_pmc_plantsignals]. The sensor records all of this in Home Assistant.
> - **This sensor does not give the model of the commercial product.** The N, P, K and Ca readings of a VITA1 come from a trained model and a library of selected signals. You get the millivolts. With time, you can find your correlations.
> - **ESPHome reads the sensor at set intervals. It does not record waveforms.** To see fast spikes of less than one second, you must have the high-rate sketch at the end of this guide. For trends, the reading at set intervals is the correct method. It samples at a higher rate than the dashboard of a VITA1, which shows a value each 5 minutes.

## Definitions

**Biopotential**: Each living cell has a difference of electrical charge across its membrane. The membrane has a positive side and a negative side, as a small battery has. When ions move because of light, water or stress, this difference changes. Then you can measure the voltage from the outer side of the tissue. In plants, the voltage is from some microvolts to some millivolts. It is on a baseline that changes slowly.

**Variation potential**: A part of a plant can have a wound or a strong stress. Then the balance of electrical charge across the cell membranes in that area changes quickly. This change moves along the plant as an electrical wave. This wave is a variation potential. It is the large, slow deflection that you see on your trace after a stress event. It is the event that is the easiest to see on a DIY sensor.

**Action potential**: A fast electrical spike. After it starts, it continues to move along the tissue. It is almost the same as the nerve signals of animals, but it is slower, and different ion channels cause it. Action potentials occur in plants, but each action potential is shorter than one second. Thus a high sampling rate is necessary to record them. This sensor measures slow trends and not action potentials.

**Electrode**: The metal contact that connects the voltage of the plant to your circuit. The contact is Ag/AgCl with gel, or a stainless probe below the skin.

**Common-mode rejection**: An instrumentation amplifier compares the signal on its two inputs. It removes the part of the signal that is the same on the two inputs, for example the mains hum. It amplifies only the difference between the two inputs. Thus you use a front-end chip and not an ADC without an amplifier.

**ADC**: Analog-to-digital converter. It changes the analog voltage of the amplifier into numbers that a microcontroller can read. In this sensor, the ADC is a 16-bit ADS1115 that connects through I2C.

## The signal chain

The sensor is a chain from the plant to the dashboard. Two electrodes measure the stem and one electrode is the reference in the soil. The AD8232 amplifies and filters the signal. The ADS1115 digitizes it. The ESP32 sends it to Home Assistant.

> **Diagram.** The signal chain. Amplify the signal first and digitize it second. The same I2C bus also connects the light sensor, the temperature sensor and the humidity sensor. These sensors give information about the conditions at the time of the plant trace.

> **KEY: Do not connect the electrodes directly to the ADC**
>
> Plant signals are a maximum of some millivolts. The plant cannot supply much current. Thus each resistance between the plant and the ADC decreases the signal before it goes to the ADC. The ADS1115 without an amplifier has no common-mode rejection and no reference drive. Thus the mains hum is larger than the plant signal in the reading.
> The AD8232 gives you the gain. It has a band-pass filter that lets only the frequencies of the plant signals go through. It _also_ has a driven reference electrode in the soil, and this electrode holds the reading stable[^pb_mdpi_ad8232]. Thus the reading shows the signal and not only noise.

## Bill of materials

> **EVIDENCE: Weak**
>
> **Provisional and experimental:** This sensor records biopotentials as relative values, for education and to find correlations. It is _not_ a validated meter for water, nutrients or stress. Do not use only this signal to make a decision about irrigation or feed.

The cost is approximately NZ$110. The M5Stack parts are Grove modules that you connect together. The two parts that are not from M5Stack are the AD8232 front-end and the ADS1115 ADC. These two parts are the usual alternatives with a low cost, because there is no biopotential amplifier in the Grove modules. The prices are approximate values for the middle of 2026.

| Part | Function | Where to get it | Approximate NZD |
| --- | --- | --- | --- |
| **M5StickC PLUS2** ESP32 with screen and LiPo battery | Controller and display | [M5Stack shop](https://shop.m5stack.com/products/m5stickc-plus2-esp32-mini-iot-development-kit) (end of life, EOL: M5StampS3 replaces it) | 32 |
| **ENV IV Unit** (SHT40 + BMP280) | Air temperature, humidity, pressure | [M5Stack shop](https://shop.m5stack.com/products/env-iv-unit-with-temperature-humidity-air-pressure-sensor-sht40-bmp280) | 14 |
| **DLight Unit** (BH1750) | Light intensity (lux) | [M5Stack shop](https://shop.m5stack.com/products/dlight-unit-ambient-light-sensor-bh1750fvi-tr) | 12 |
| **1-to-3 HUB Unit** (passive I2C splitter) | Connect three devices to one bus | [M5Stack shop](https://shop.m5stack.com/products/mini-hub-module) | 6 |
| **AD8232 ECG module** (SparkFun SEN-12650 or an equivalent) | Biopotential front-end [not from M5Stack] | [SparkFun](https://www.sparkfun.com/sparkfun-single-lead-heart-rate-monitor-ad8232.html) · equivalent on AliExpress, approximately NZ$9 | 9 |
| **ADS1115 breakout** (16-bit I2C ADC) | Digitize the analog output [not from M5Stack] | [Adafruit product 1085](https://www.adafruit.com/product/1085) · equivalent, approximately NZ$6 | 6 |
| **Electrodes**: Ag/AgCl EEG cups _or_ stainless probes with snap leads | Skin contact [not from M5Stack] | [SparkFun sensor cable](https://www.sparkfun.com/products/12970) and [electrode pads](https://www.sparkfun.com/products/12969), or a medical set of Ag/AgCl electrodes | 14 |
| **Electrode gel** (Ten20) and micropore tape | Contact with low impedance | Pharmacy | 9 |
| DuPont jumper wires, a small prototype board, heatshrink | Connections between the AD8232 and the ADS1115 | Your spare parts, or an electronics shop | 8 |
| Total: approximately NZ$110. If the controller is an M5StampS3 and not the StickC, the total is less than NZ$95. The alternative does not have the screen that is on the board of the StickC. |

> **WARN: Two parts are at the end of their life (EOL)**
>
> M5Stack stopped the production of the StickC PLUS2 and the ENV IV. But resellers (RobotShop, Botland, TinyTronics) continue to have them in stock, and they have the most tutorials. If you want current parts, the **M5StampS3** replaces the controller and the **ENV Pro** replaces the ENV IV. In the firmware, only two I2C pin numbers change.

## Wiring

After the controller, the sensor has one I2C bus. The HUB connects this bus to three devices. The only analog wire in the sensor goes from the output of the AD8232 to the A0 pin of the ADS1115. The electrodes connect to the header with three pins of the AD8232.

> **Diagram.** The wiring. One I2C bus (SDA blue, SCL green, power red) connects the controller to three devices through the HUB. The only analog connection (amber) is the output of the AD8232 to A0 of the ADS1115.

| From | Pin | To | Pin or target |
| --- | --- | --- | --- |
| M5 Grove Port A | SDA (G32) | HUB → all I2C devices | SDA |
| M5 Grove Port A | SCL (G33) | HUB → all I2C devices | SCL |
| M5 Grove Port A | 5V / GND | HUB → ENV and DLight. 3.3V to ADS1115 and AD8232 | VDD / GND |
| AD8232 | OUTPUT | ADS1115 | A0 |
| AD8232 | 3.3V / GND | controller 3.3V / GND | — |
| AD8232 | LA / RA / RL | electrodes | upper stem, lower stem, soil |

> **WARN: Supply the AD8232 with clean 3.3 V**
>
> Use the 3.3 V rail for the chip. Do not use the 5 V USB rail, because it has more noise. The center point of the output and the noise floor change when the supply changes. Keep the electrode leads short and twisted. Put the leads away from lights, ballasts and pumps. A battery (the LiPo of the StickC) gives less noise than USB power.

## Electrodes and their position

**Contact impedance** is the resistance between the metal of the electrode and the tissue of the plant. A bad connection decreases the signal and lets noise go in before the signal goes to the amplifier. The AD8232 does all the work after this point. The quality of the electrode contact is the one variable that you control. You can use one of these two alternatives[^pb_hackster_flora]:

**Ag/AgCl EEG cups**

This alternative gives the best signal quality. Fill the cup with conductive gel and attach it to the stem with tape. It does not cause a wound in the plant, but the gel becomes dry. Replace the gel after some days.

**Stainless probes or needles**

Put the probe 2 to 3 mm (0.08 to 0.12 in) below the epidermis. This alternative is more stable. It is almost the same as the method of commercial pin contacts, which measure the signal in the plant. But it causes a wound in the plant. Thus put the probe in the plant one time only, and use a clean sterilized probe.

1. **Put the pair of electrodes along the stem**: Put LA (sense +) on the upper stem near a node. Put RA (sense −) 5 to 15 cm (2 to 6 in) below LA on the same stem. This pair of electrodes records the signal that moves along the stem.
2. **Put the reference in the soil**: Put RL (the driven reference) in the moist soil of the root zone. It removes the common-mode hum. Make sure that you connect RL.
3. **Gel and tape**: Put a small quantity of Ten20 below each surface contact. Then attach the contact with micropore tape, which gives a light and stable pressure. If the baseline increases slowly and has more noise, the cause is usually that the electrode becomes dry. The cause is not usually a problem in the plant.
4. **Wait until the signal is stable**: When metal touches wet tissue, ion exchange occurs at the surface and makes a small voltage. This voltage is a **half-cell potential**. Wait 10 to 30 minutes for the voltage to become stable. The first drift comes from the chemistry of the electrode and not from the plant.

> **DANGER: Needle electrodes cause a wound in the plant**
>
> Make one clean insertion only, with a probe that you sterilized with alcohol. Do not make a row of holes around the stem, because a row of holes can girdle the stem. A new insertion causes a variation potential. You can use it one time as a known stimulus. Then let the wound close.

## ESPHome firmware

The full configuration follows. Put your Wi-Fi, API and OTA secrets in the file `secrets.yaml` of ESPHome. Install the firmware from the ESPHome dashboard. Home Assistant then finds the sensor automatically. For a StampS3 or a Core2, change the board setting. If it is necessary, also change the two I2C pins.

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

# ---- 16-bit ADC hub ----
ads1115:
  - address: 0x48

sensor:
  # === PLANT BIOPOTENTIAL ===
  - platform: ads1115
    multiplexer: 'A0_GND'       # AD8232 OUTPUT on A0, single-ended
    gain: 4.096                 # FSR covers the 0-3.3V swing
    name: "Plant Biopotential (raw)"
    id: bio_raw
    unit_of_measurement: "V"
    accuracy_decimals: 4
    update_interval: 1s
    filters:
      - median: { window_size: 5, send_every: 1 }   # kill spikes

  # Centre on the ~1.5V bias -> signed millivolts (the number you watch)
  - platform: template
    name: "Plant Biopotential"
    id: bio_mv
    unit_of_measurement: "mV"
    accuracy_decimals: 2
    update_interval: 1s
    lambda: |-
      return (id(bio_raw).state - 1.5) * 1000.0;   // trim 1.5 to your measured baseline

  # Slow envelope = the "trend" a commercial unit charts every 5 min
  - platform: template
    name: "Plant Signal Trend"
    unit_of_measurement: "mV"
    accuracy_decimals: 2
    lambda: |- return id(bio_mv).state;
    filters:
      - exponential_moving_average: { alpha: 0.02, send_every: 30 }

  # === ENVIRONMENT (ENV IV Unit) ===
  - platform: sht4x
    address: 0x44
    temperature: { name: "Grow Air Temp", id: air_t }
    humidity:    { name: "Grow Humidity", id: air_rh }
  - platform: bmp280_i2c        # older ESPHome: use "bmp280"
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

# === OPTIONAL: electrode lead-off detection ===
binary_sensor:
  - platform: gpio
    pin: 26                       # AD8232 LO+ ; pick a free GPIO for your board
    name: "Electrode Lead-off"
    device_class: problem

> **KEY: Calibration at the first start**
>
> Attach the electrodes and wait until they are stable. Then read `Plant Biopotential (raw)` in Home Assistant. The stable voltage that you read _is_ your baseline. Replace the `1.5` in the lambda with this number. Then `Plant Biopotential` reads approximately 0 mV when there is no stimulus. It gives positive and negative values around this value[^pb_esphome_ads1115].

## How to read plant-biosignal data

The values are _changes_ of the potential. They are not a calibrated physiological unit. Compare a plant with the same plant at other times. Do not compare plants with each other in raw millivolts.

| Signal that you see | Possible condition |
| --- | --- |
| The signal increases and decreases smoothly each day, at the same time as the light sensor | The circadian rhythm of a plant in good condition. This rhythm is the baseline. |
| A fast deflection, then the signal goes back to the baseline slowly, after you touch or move the plant | A variation potential. It is the usual signal of a wound or stress. |
| A step change at the same time as the lights come on or go off | Response to light. The data in the reference show a detection rate of approximately 85% with this hardware[^pb_pmc_plantsignals] |
| The baseline increases slowly and has more noise, and there is no plant event | The electrode becomes dry. Put new gel on it. It is not a plant problem. |
| 50/60 Hz noise that is larger than all the other signals | Mains pickup. Make the leads shorter, twist them, and make the soil reference better. |
| A signal that does not change, at a rail (0 or full scale) | A lead is off or a contact has no connection. Examine the binary sensor. |

To get close to the _inference_ of a commercial unit, record data for some weeks. Record the raw trace, the VPD, the light and the irrigation events. Then find **your** correlations that occur again. For example, the amplitude of the signal can decrease strongly before you see wilt, as a first sign of water stress. The commercial product includes this library of correlations. Send the trace to the [plant-state dashboard](plant-state-dashboard.html) to use it together with your other telemetry.

## Limits, calibration and safety

> **KEY: Limits to know before you solder**
>
> - **Relative values, not absolute values.** The values are good for trends and events on one plant. They are not good to compare plants or to read a calibrated number.
> - **Set the baseline again each time that you attach the electrodes.** The half-cell offsets are different each time that you put the electrodes in position. Thus do the calibration at the first start again.
> - **The noise floor is higher than in commercial units.** The items that give the largest decrease in noise are a battery supply, short shielded leads and a small enclosure.
> - **ESPHome is for trends.** To record waveforms, install an Arduino sketch on the controller. The sketch must sample the ADS1115 at its maximum rate of 860 SPS. Or it must sample the AD8232 on an ESP32 ADC pin at 400 Hz. The investigation of plant signals used this rate[^pb_arxiv_esp32]. The wiring is the same and the firmware is different.

> **DANGER: Keep the sensor isolated**
>
> Keep the sensor at a low voltage. Supply it with a battery or with USB. Do not connect the plant electrodes to an item that has a connection to the mains. Use one common ground only. Thus there is no ground loop through the plant.

## References

[^pb_mdpi_ad8232]: Marques JAL et al. (2023). From AD8232 to biopotentials sensors: open-source project and benchmark. Electronics (MDPI), 12(4):833. https://www.mdpi.com/2079-9292/12/4/833 (source with peer review)
[^pb_arxiv_esp32]: AD8232 bioelectric signal processing with ESP32 (2025). arXiv:2505.18173. https://arxiv.org/pdf/2505.18173 (source from a manufacturer or industry)
[^pb_pmc_plantsignals]: Plant bioelectrical signals for environmental and emotional state classification (2024). PMC. (AD8232 at 400 Hz; ~85% lamp on/off detection accuracy.) https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12649952/ (source with peer review)
[^pb_hackster_flora]: Verma A. Interacting with the Flora: an ESP32 + AD8232 + BH1750 + DS18B20 plant-signal rig. Hackster.io. https://www.hackster.io/ankurverma608/interacting-with-the-flora-7ef65f (source from a manufacturer or industry)
[^pb_vivent]: Vivent Biosignals, VITA1 plant-driven cultivation sensor (manufacturer documentation). https://vivent-biosignals.com/plant-driven-cultivation/ (source from a manufacturer or industry)
[^pb_esphome_ads1115]: ESPHome, ADS1115 4-channel 16-bit A/D converter component (documentation). https://esphome.io/components/sensor/ads1115/ (source from a manufacturer or industry)
