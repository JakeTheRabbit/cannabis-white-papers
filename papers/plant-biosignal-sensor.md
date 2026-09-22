---
slug: "plant-biosignal-sensor"
title: "Build a plant-biosignal sensor with M5Stack and ESPHome"
eyebrow: "Build · Precision & automation"
summary: "Plants produce tiny electrical signals — microvolts to a few millivolts — that shift when light turns on, water runs low, or the plant is stressed. This guide walks you through building the sensor that captures those signals: an M5Stack ESP32, an ECG front-end chip, and ESPHome for about NZ$110. You will log the raw trace into Home Assistant and learn to read the daily rhythm and stress events — not as a validated water or nutrient meter, but as a real-time window into plant electrical activity."
track: "Precision & automation"
read_time: "~14 min read"
diagrams: ""
related: ["plant-state-dashboard", "signal-and-noise", "closed-loop"]
url: "https://www.growlabs.nz/whitepapers/plant-biosignal-sensor.html"
md_url: "https://www.growlabs.nz/whitepapers/papers/plant-biosignal-sensor.md"
version: "1.2"
updated: "2026-07-18"
license: "CC BY-NC 4.0"
license_url: "https://creativecommons.org/licenses/by-nc/4.0/"
attribution: "The Cannabis White Papers"
refs: [{"id": "pb_mdpi_ad8232", "n": 1, "cite": "Marques JAL et al. (2023). From AD8232 to biopotentials sensors: open-source project and benchmark. Electronics (MDPI), 12(4):833.", "url": "https://www.mdpi.com/2079-9292/12/4/833", "peer": true}, {"id": "pb_arxiv_esp32", "n": 2, "cite": "AD8232 bioelectric signal processing with ESP32 (2025). arXiv:2505.18173.", "url": "https://arxiv.org/pdf/2505.18173", "peer": false}, {"id": "pb_pmc_plantsignals", "n": 3, "cite": "Plant bioelectrical signals for environmental and emotional state classification (2024). PMC. (AD8232 at 400 Hz; ~85% lamp on/off detection accuracy.)", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12649952/", "peer": true}, {"id": "pb_hackster_flora", "n": 4, "cite": "Verma A. Interacting with the Flora: an ESP32 + AD8232 + BH1750 + DS18B20 plant-signal rig. Hackster.io.", "url": "https://www.hackster.io/ankurverma608/interacting-with-the-flora-7ef65f", "peer": false}, {"id": "pb_vivent", "n": 5, "cite": "Vivent Biosignals, VITA1 plant-driven cultivation sensor (manufacturer documentation).", "url": "https://vivent-biosignals.com/plant-driven-cultivation/", "peer": false}, {"id": "pb_esphome_ads1115", "n": 6, "cite": "ESPHome, ADS1115 4-channel 16-bit A/D converter component (documentation).", "url": "https://esphome.io/components/sensor/ads1115/", "peer": false}]
---

# Build a plant-biosignal sensor with M5Stack and ESPHome

_Build · Precision & automation · ~14 min read_

> Plants produce tiny electrical signals — microvolts to a few millivolts — that shift when light turns on, water runs low, or the plant is stressed. This guide walks you through building the sensor that captures those signals: an M5Stack ESP32, an ECG front-end chip, and ESPHome for about NZ$110. You will log the raw trace into Home Assistant and learn to read the daily rhythm and stress events — not as a validated water or nutrient meter, but as a real-time window into plant electrical activity.

## Purpose and scope

Plants generate tiny electrical signals. Ions move across cell membranes when the plant responds to light, water, wounding or nutrient change, and that movement shows up as a sub-millivolt voltage you can read with electrodes on the stem[^pb_pmc_plantsignals]. Commercial units like the Vivent VITA1 do exactly this, then use trained models to infer water and stress state from how the signal drifts[^pb_vivent].

Electrically, reading a plant is the same problem as reading a heartbeat: a small, noisy, high-impedance voltage you must amplify cleanly. That means the cheap, proven ECG front-end chip, the **AD8232**, works straight out of the box for plants[^pb_mdpi_ad8232]. Bolt it to an ESP32 and ESPHome and you have a logging plant-biosignal sensor for about NZ$110.

> **NOTE — What this build is, and isn't**
>
> - **It reproduces the acquisition**: the raw signal, the daily rhythm, the big deflections after a stress event, light-on/off detection (one study reported ~85% under its protocol, not guaranteed on this exact hardware class)[^pb_pmc_plantsignals], all logged in Home Assistant.
> - **It does not reproduce the paid model.** A VITA1's N/P/K/Ca read-outs come from a trained model on a curated signal library. You get the millivolts; you build your own correlations over time.
> - **ESPHome polls, it doesn't capture waveforms.** Fast sub-second spikes need the high-rate sketch noted at the end. For trend work, polling is the right tool, and it already samples finer than a VITA1's 5-minute dashboard.

## Definitions

**Biopotential** — Every living cell maintains a charge difference across its membrane — like a tiny battery, with a positive side and a negative side. When ions move in response to light, water, or stress, that charge difference shifts, and you can measure the resulting voltage from outside the tissue. In plants it runs microvolts to a few millivolts, riding on a slowly-drifting baseline.

**Variation potential** — When part of a plant is wounded or sharply stressed, the charge balance across cell membranes in that region shifts rapidly, and that shift spreads along the plant as an electrical wave. This is a variation potential — the big, slow deflection that shows up on your trace after a clear stress event, and the clearest single event you will see on a DIY rig.

**Action potential** — A fast, self-propagating electrical spike — similar in concept to the nerve signals animals use, but slower and driven by different ion channels. Real in plants but sub-second, so it needs high-rate sampling to catch, unlike the slow trends this build is designed to log.

**Electrode** — The metal contact that couples the plant's voltage into your circuit. Ag/AgCl with gel, or a stainless probe just under the skin.

**Common-mode rejection** — Noise-cancelling headphones compare the sound on both sides of the earcup and subtract what they share, leaving only what differs. An instrumentation amplifier does the same electrically: it discards anything that appears equally on both inputs — mains hum, for example — and amplifies only the difference between them. This is the whole reason to use a front-end chip rather than a bare ADC.

**ADC** — Analog-to-digital converter. Turns the amplifier's analog voltage into numbers a microcontroller can read. Here, a 16-bit ADS1115 over I2C.

## The signal chain

Everything is one line from plant to dashboard. Two electrodes sense the stem, one references the soil; the AD8232 amplifies and filters; the ADS1115 digitises; the ESP32 publishes.

> **Diagram.** The chain. Amplify first, digitise second, and the same I2C bus also carries the light, temperature and humidity sensors that give the plant trace its context.

> **KEY — Why not just wire electrodes to the ADC?**
>
> Plant signals are a few millivolts at most, and the plant cannot supply much current — any resistance in the measurement path drains the signal before it arrives. The ADS1115 alone has no common-mode rejection and no reference drive, so mains hum swamps the reading. The AD8232 gives you the gain, a band-pass filter that passes only the frequencies plant signals occupy, _and_ a driven soil-reference electrode that holds the reading steady[^pb_mdpi_ad8232]. It is the difference between a signal and a mess.

## Bill of materials

> **EVIDENCE — Grain of salt**
>
> **Provisional / experimental:** This build logs relative biopotentials for education and correlation hunting. It is _not_ a validated water, nutrient, or stress meter. Do not irrigate or feed from this signal alone.

About NZ$110. M5Stack parts come as plug-together Grove modules; the two non-M5Stack parts (the AD8232 front-end and the ADS1115 ADC) are the standard cheap substitutes, because nobody sells a biopotential amplifier in the Grove ecosystem. Prices are indicative, mid-2026.

| Part | Role | Where to buy | ~NZD |
| --- | --- | --- | --- |
| **M5StickC PLUS2** ESP32 + screen + LiPo | Controller & display | [shop.m5stack.com](https://shop.m5stack.com/products/m5stickc-plus2-esp32-mini-iot-development-kit) (EOL; successor M5StampS3) | 32 |
| **ENV IV Unit** (SHT40 + BMP280) | Air temp, humidity, pressure | [shop.m5stack.com](https://shop.m5stack.com/products/env-iv-unit-with-temperature-humidity-air-pressure-sensor-sht40-bmp280) | 14 |
| **DLight Unit** (BH1750) | Light level (lux) | [shop.m5stack.com](https://shop.m5stack.com/products/dlight-unit-ambient-light-sensor-bh1750fvi-tr) | 12 |
| **1-to-3 HUB Unit** (passive I2C splitter) | Share one bus across three devices | [shop.m5stack.com](https://shop.m5stack.com/products/mini-hub-module) | 6 |
| **AD8232 ECG module** (SparkFun SEN-12650 or clone) | Biopotential front-end [non-M5Stack] | [sparkfun.com](https://www.sparkfun.com/sparkfun-single-lead-heart-rate-monitor-ad8232.html) · clone on AliExpress ~NZ$9 | 9 |
| **ADS1115 breakout** (16-bit I2C ADC) | Digitise the analog output [non-M5Stack] | [adafruit.com/product/1085](https://www.adafruit.com/product/1085) · clone ~NZ$6 | 6 |
| **Electrodes**, Ag/AgCl EEG cups _or_ stainless probes + snap leads | Skin contact [non-M5Stack] | [SparkFun sensor cable](https://www.sparkfun.com/products/12970) + [electrode pads](https://www.sparkfun.com/products/12969), or medical Ag/AgCl set | 14 |
| **Electrode gel** (Ten20) + micropore tape | Low-impedance contact | Pharmacy | 9 |
| DuPont jumpers, small proto board, heatshrink | Glue between AD8232 and ADS1115 | Junk box / any hobby shop | 8 |
| Total ≈ NZ$110. A bare M5StampS3 instead of the StickC drops it below NZ$95 at the cost of the on-board screen. |

> **WARN — Two parts are marked EOL**
>
> M5Stack has retired the StickC PLUS2 and ENV IV, but both are still stocked by resellers (RobotShop, Botland, TinyTronics) and have the most tutorials. If you want current parts, the **M5StampS3** replaces the controller and the **ENV Pro** replaces the ENV IV. The firmware only changes by two I2C pin numbers.

## Wiring

Everything downstream of the controller is one I2C bus, fanned out by the HUB. The single analog wire in the whole build is the AD8232 output into the ADS1115's A0 pin. Electrodes plug into the AD8232's three-pin header.

> **Diagram.** Wiring. One I2C bus (SDA blue, SCL green, power red) fans out through the HUB to three devices; the lone analog hop (amber) is AD8232 output into ADS1115 A0.

| From | Pin | To | Pin / target |
| --- | --- | --- | --- |
| M5 Grove Port A | SDA (G32) | HUB → all I2C devices | SDA |
| M5 Grove Port A | SCL (G33) | HUB → all I2C devices | SCL |
| M5 Grove Port A | 5V / GND | HUB → ENV/DLight; 3.3V to ADS1115 + AD8232 | VDD / GND |
| AD8232 | OUTPUT | ADS1115 | A0 |
| AD8232 | 3.3V / GND | controller 3.3V / GND | — |
| AD8232 | LA / RA / RL | electrodes | upper stem / lower stem / soil |

> **WARN — Power the AD8232 from clean 3.3 V**
>
> Its output centre-point and noise floor track the supply, so feed it the 3.3 V rail, not the noisy 5 V USB rail. Keep electrode leads short and twisted, and route them away from lights, ballasts and pumps. Battery power (the StickC's LiPo) beats USB for noise.

## Electrodes and placement

**Contact impedance** is the resistance between the electrode metal and the plant's tissue. Think of it like a loose headphone jack — a poor connection weakens the signal and lets noise in before it reaches the amplifier. The AD8232 handles everything downstream; your electrode contact quality is the one variable you control. Two workable options[^pb_hackster_flora]:

**Ag/AgCl EEG cups**

Best signal quality. Fill the cup with conductive gel and tape it to the stem. Non-invasive, but the gel dries and must be refreshed every few days.

**Stainless probes / needles**

Insert 2–3 mm (0.08–0.12 in) just under the epidermis. More stable and closest to how commercial pin-contacts read ‘inside’ the plant, but it wounds the plant, so use one clean, sterilised insertion.

1. **Place the pair along the stem** — LA (sense +) on the upper stem near a node; RA (sense −) 5–15 cm (2–6 in) lower on the same stem. This pair captures the travelling signal.
2. **Reference into the soil** — RL (the driven reference) goes into the moist root-zone soil. It is what cancels common-mode hum, so don't skip it.
3. **Gel and tape** — A dab of Ten20 under each surface contact, then micropore tape for light, steady pressure. A rising, noisy baseline is usually a drying electrode, not a sick plant.
4. **Let it settle** — When metal contacts wet tissue, ions exchange at the surface and build a small voltage of their own — a **half-cell potential**, the same effect that makes a lemon and two different coins into a battery. Allow 10–30 minutes for this to stabilise. The initial drift is electrode chemistry settling, not plant activity.

> **DANGER — Needle electrodes wound the plant**
>
> A fresh insertion itself triggers a variation potential, useful once as a known stimulus, then let it heal. Sterilise with alcohol and use a single clean insertion; don't ring-bark the stem with a row of holes.

## ESPHome firmware

The full config. Put your Wi-Fi, API and OTA secrets in ESPHome's `secrets.yaml`, flash from the ESPHome dashboard, and it auto-discovers into Home Assistant. On a StampS3 or Core2, change the board line and, if needed, the two I2C pins.

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

> **KEY — First-boot calibration**
>
> With electrodes attached and settled, read `Plant Biopotential (raw)` in Home Assistant. Whatever steady voltage it sits at _is_ your baseline, so replace the `1.5` in the lambda with that number. Then `Plant Biopotential` reads ~0 mV at rest and swings signed around it[^pb_esphome_ads1115].

## Interpreting plant-biosignal data

These are _changes_ in potential, not a calibrated physiological unit. Compare a plant to itself over time, never plant-to-plant in raw millivolts.

| What you see | Likely meaning |
| --- | --- |
| Smooth daily rise and fall tracking the light sensor | Healthy circadian activity, the baseline rhythm of a happy plant |
| Sharp deflection then slow recovery after you touch or move it | A variation potential, the classic wound/stress signal |
| Step change synced to lights on/off | Light response (documented ~85% detectable on this hardware)[^pb_pmc_plantsignals] |
| Baseline slowly climbing and getting noisier, no plant event | Electrode drying out, re-gel it, not a plant problem |
| 50/60 Hz fuzz dominating everything | Mains pickup, shorten and twist the leads, improve the soil reference |
| Flat line at a rail (0 or full-scale) | Lead-off or broken contact, check the binary sensor |

To approach a commercial unit's _inference_, log the raw trace alongside VPD, light and irrigation events for a few weeks, then hunt for **your own** repeatable correlations, for example signal amplitude collapsing before visible wilt as an early water-stress warning. That correlation library is exactly what the paid product ships pre-built. Feed the trace into the [plant-state dashboard](plant-state-dashboard.html) to combine it with your other telemetry.

## Limitations, calibration and safety

> **KEY — Set expectations before you solder**
>
> - **Relative, not absolute.** Good for trends and events on one plant, not for comparing plants or reading a calibrated number.
> - **Re-baseline every reattach.** Half-cell offsets differ each time you place electrodes, so redo the first-boot calibration.
> - **Higher noise floor than commercial rigs.** Battery power, short shielded leads and a small enclosure help most.
> - **ESPHome is for trends.** For actual waveforms, flash a plain Arduino sketch that samples the ADS1115 at its full 860 SPS (or the AD8232 off an ESP32 ADC pin at 400 Hz, the rate used in the published plant-signal study[^pb_arxiv_esp32]). Same wiring, different firmware.

> **DANGER — Keep it isolated**
>
> Keep the whole thing low-voltage and battery or USB powered. Never connect plant electrodes to anything mains-referenced, and use one common ground only, so you don't create a ground loop through the plant.

## References

[^pb_mdpi_ad8232]: Marques JAL et al. (2023). From AD8232 to biopotentials sensors: open-source project and benchmark. Electronics (MDPI), 12(4):833. https://www.mdpi.com/2079-9292/12/4/833 (peer-reviewed)
[^pb_arxiv_esp32]: AD8232 bioelectric signal processing with ESP32 (2025). arXiv:2505.18173. https://arxiv.org/pdf/2505.18173 (industry/manufacturer source)
[^pb_pmc_plantsignals]: Plant bioelectrical signals for environmental and emotional state classification (2024). PMC. (AD8232 at 400 Hz; ~85% lamp on/off detection accuracy.) https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12649952/ (peer-reviewed)
[^pb_hackster_flora]: Verma A. Interacting with the Flora: an ESP32 + AD8232 + BH1750 + DS18B20 plant-signal rig. Hackster.io. https://www.hackster.io/ankurverma608/interacting-with-the-flora-7ef65f (industry/manufacturer source)
[^pb_vivent]: Vivent Biosignals, VITA1 plant-driven cultivation sensor (manufacturer documentation). https://vivent-biosignals.com/plant-driven-cultivation/ (industry/manufacturer source)
[^pb_esphome_ads1115]: ESPHome, ADS1115 4-channel 16-bit A/D converter component (documentation). https://esphome.io/components/sensor/ads1115/ (industry/manufacturer source)
