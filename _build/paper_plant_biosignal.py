# -*- coding: utf-8 -*-
"""Paper: a DIY plant-biosignal sensor (Vivent-style) from M5Stack + ESPHome."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        grid, card, chip, kv, steps)
import figs_lib as L
from figs import INK, INK2, MUT, LINE, G, GD, GL, BLU, BLUL, AMB, RED, PAPER, FS, MN

SLUG = "plant-biosignal-sensor"
TITLE = "Make a plant-biosignal sensor with M5Stack and ESPHome"
EYEBROW = "Assembly · Precision and automation"
SUB = ("Plants make small electrical signals, from microvolts to some millivolts. The signals "
       "change when the light comes on, when the water becomes low, or when the plant has stress. "
       "This guide shows how to make the sensor that records these signals. The sensor has an "
       "M5Stack ESP32, an ECG front-end chip and ESPHome, and the cost is approximately NZ$110. You "
       "will record the raw trace in Home Assistant and know how to read the rhythm of each day and "
       "the stress events. The sensor is not a validated meter for water or nutrients, but it shows "
       "the electrical activity of the plant in real time.")
META = [("wave", "Assembly guide"), ("gauge", "DIY hardware"),
        ("quote", "4 sources"), ("clock", "~14 min to read")]
RELATED = ["plant-state-dashboard", "signal-and-noise", "closed-loop"]
REF_IDS = ["pb_mdpi_ad8232", "pb_arxiv_esp32", "pb_pmc_plantsignals",
           "pb_hackster_flora", "pb_vivent", "pb_esphome_ads1115"]


def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)


# ---- code block that survives the auto-interlinker (wrapped in <code>) ----
def code(text):
    esc = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return ("<pre style=\"background:var(--surface-2);border:1px solid var(--line); "
            "border-radius:10px;padding:16px 18px;overflow:auto;font-family:var(--mono); "
            "font-size:12.5px;line-height:1.55;color:var(--ink)\"><code>" + esc + "</code></pre>")


# ---------------------------------------------------------------- wiring SVG (themed)
def wiring_svg():
    W, H = 760, 380
    box = lambda x, y, w, hh, t, s, fill=None: (
        f'<rect x="{x}" y="{y}" width="{w}" height="{hh}" rx="10" fill="{fill or PAPER}" stroke="{LINE}" stroke-width="1.5"/>'
        f'<text x="{x+w/2:.0f}" y="{y+22}" text-anchor="middle" fill="{INK}" font-size="13" font-weight="700" style="{FS}">{t}</text>'
        f'<text x="{x+w/2:.0f}" y="{y+39}" text-anchor="middle" fill="{MUT}" font-size="10.5" style="{MN}">{s}</text>')
    pr = []
    pr.append(f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Wiring diagram">')
    pr.append(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')
    # controller
    pr.append(box(24, 150, 150, 74, "M5 ESP32", "ESPHome"))
    pr.append(f'<text x="182" y="182" text-anchor="end" fill="{MUT}" font-size="10" style="{MN}">G32 SDA</text>')
    pr.append(f'<text x="182" y="198" text-anchor="end" fill="{MUT}" font-size="10" style="{MN}">G33 SCL</text>')
    pr.append(f'<text x="182" y="214" text-anchor="end" fill="{MUT}" font-size="10" style="{MN}">5V / G</text>')
    # hub
    pr.append(box(210, 150, 118, 74, "1-to-3 HUB", "I2C splitter"))
    pr.append(f'<path d="M174 186 H210" stroke="{BLU}" stroke-width="2" fill="none"/>')
    pr.append(f'<path d="M174 200 H210" stroke="{G}" stroke-width="2" fill="none"/>')
    pr.append(f'<path d="M174 214 H210" stroke="{RED}" stroke-width="2" fill="none"/>')
    # three branches
    pr.append(box(400, 26, 176, 60, "ENV IV Unit", "SHT40 0x44 / BMP280 0x76"))
    pr.append(box(400, 104, 176, 52, "DLight Unit", "BH1750 0x23"))
    pr.append(box(400, 176, 176, 78, "ADS1115  0x48", "16-bit ADC"))
    pr.append(f'<text x="412" y="228" fill="{MUT}" font-size="10" style="{MN}">A0 &#9668; analog in</text>')
    pr.append(f'<path d="M328 176 C368 176 360 56 400 56" stroke="{BLU}" stroke-width="2" fill="none"/>')
    pr.append(f'<path d="M328 190 C372 190 366 130 400 130" stroke="{G}" stroke-width="2" fill="none"/>')
    pr.append(f'<path d="M328 200 C376 200 372 205 400 205" stroke="{BLU}" stroke-width="2" fill="none"/>')
    pr.append(f'<path d="M328 210 C380 210 380 218 400 218" stroke="{G}" stroke-width="2" fill="none"/>')
    # AD8232
    pr.append(box(604, 176, 132, 96, "AD8232", "ECG front-end"))
    pr.append(f'<text x="616" y="232" fill="{MUT}" font-size="10" style="{MN}">OUTPUT &#9658;</text>')
    pr.append(f'<text x="616" y="250" fill="{MUT}" font-size="10" style="{MN}">LA / RA / RL</text>')
    pr.append(f'<path d="M576 215 C592 215 590 210 604 210" stroke="{AMB}" stroke-width="2.5" fill="none"/>')
    pr.append(f'<text x="590" y="205" fill="{AMB}" font-size="9.5" style="{MN}">analog</text>')
    # electrodes
    pr.append(f'<circle cx="628" cy="300" r="6" fill="{AMB}"/><text x="640" y="304" fill="{INK2}" font-size="10.5" style="{FS}">LA &#8594; upper stem</text>')
    pr.append(f'<circle cx="628" cy="322" r="6" fill="{AMB}"/><text x="640" y="326" fill="{INK2}" font-size="10.5" style="{FS}">RA &#8594; lower stem</text>')
    pr.append(f'<circle cx="628" cy="344" r="6" fill="{RED}"/><text x="640" y="348" fill="{INK2}" font-size="10.5" style="{FS}">RL &#8594; soil (reference)</text>')
    pr.append(f'<path d="M636 272 V296" stroke="{LINE}" stroke-width="1.5" fill="none"/>')
    # legend
    pr.append(f'<g><text x="24" y="330" fill="{MUT}" font-size="10" style="{FS}">Wires:</text>')
    pr.append(f'<line x1="70" y1="326" x2="98" y2="326" stroke="{BLU}" stroke-width="2"/><text x="104" y="330" fill="{MUT}" font-size="10" style="{FS}">SDA</text>')
    pr.append(f'<line x1="140" y1="326" x2="168" y2="326" stroke="{G}" stroke-width="2"/><text x="174" y="330" fill="{MUT}" font-size="10" style="{FS}">SCL</text>')
    pr.append(f'<line x1="206" y1="326" x2="234" y2="326" stroke="{RED}" stroke-width="2"/><text x="240" y="330" fill="{MUT}" font-size="10" style="{FS}">power</text>')
    pr.append(f'<line x1="286" y1="326" x2="314" y2="326" stroke="{AMB}" stroke-width="2.5"/><text x="320" y="330" fill="{MUT}" font-size="10" style="{FS}">analog</text></g>')
    pr.append("</svg>")
    return "".join(pr)


SECTIONS = []

SECTIONS.append({"id": "start", "kicker": "01 · Read this first", "title": "Purpose and scope",
  "blocks": [
    lead("Plants make small electrical signals. When a plant changes in response to light, water, a "
         "wound or a change in nutrients, ions move across the cell membranes. This movement makes "
         "a voltage of less than one millivolt. You can read this voltage with electrodes on the "
         "stem" + _c("pb_pmc_plantsignals") + ". Commercial units, for example the Vivent VITA1, do "
         "the same. They then use trained models to calculate the water condition and the stress "
         "condition from the drift of the signal" + _c("pb_vivent") + "."),
    p("To read a plant is the same electrical problem as to read a heartbeat. The voltage is small, "
      "it has noise, and it has high impedance. You must amplify it and not increase the noise. "
      "Thus the <strong>AD8232</strong>, a standard ECG front-end chip with a low cost, is correct "
      "for plants without changes" + _c("pb_mdpi_ad8232") + ". Connect this chip to an ESP32 and "
      "ESPHome, and you have a plant-biosignal sensor that records data. The cost is approximately "
      "NZ$110."),
    callout("note", "Functions and limits of this sensor",
      ul(["<strong>This sensor does the same data acquisition.</strong> It records the raw signal "
          "and the rhythm of each day. It also records the large deflections after a stress event "
          "and the change when the light starts and stops. One investigation gave a detection rate "
          "of approximately 85% for the light changes, with its protocol. It is not sure that you "
          "get the same value with this type of hardware" + _c("pb_pmc_plantsignals") +
          ". The sensor records all of this in Home Assistant.",
          "<strong>This sensor does not give the model of the commercial product.</strong> The N, "
          "P, K and Ca readings of a VITA1 come from a trained model and a library of selected "
          "signals. You get the millivolts. With time, you can find your correlations.",
          "<strong>ESPHome reads the sensor at set intervals. It does not record "
          "waveforms.</strong> To see fast spikes of less than one second, you must have the "
          "high-rate sketch at the end of this guide. For trends, the reading at set intervals is "
          "the correct method. It samples at a higher rate than the dashboard of a VITA1, which "
          "shows a value each 5 minutes."])),
  ]})

SECTIONS.append({"id": "terms", "kicker": "02 · The terms", "title": "Definitions",
  "blocks": [
    defterm("Biopotential", "Each living cell has a difference of electrical charge across its "
            "membrane. The membrane has a positive side and a negative side, as a small battery "
            "has. When ions move because of light, water or stress, this difference changes. Then "
            "you can measure the voltage from the outer side of the tissue. In plants, the voltage "
            "is from some microvolts to some millivolts. It is on a baseline that changes slowly."),
    defterm("Variation potential", "A part of a plant can have a wound or a strong stress. Then the "
            "balance of electrical charge across the cell membranes in that area changes quickly. "
            "This change moves along the plant as an electrical wave. This wave is a variation "
            "potential. It is the large, slow deflection that you see on your trace after a stress "
            "event. It is the event that is the easiest to see on a DIY sensor."),
    defterm("Action potential", "A fast electrical spike. After it starts, it continues to move "
            "along the tissue. It is almost the same as the nerve signals of animals, but it is "
            "slower, and different ion channels cause it. Action potentials occur in plants, but "
            "each action potential is shorter than one second. Thus a high sampling rate is "
            "necessary to record them. This sensor measures slow trends and not action potentials."),
    defterm("Electrode", "The metal contact that connects the voltage of the plant to your circuit. "
            "The contact is Ag/AgCl with gel, or a stainless probe below the skin."),
    defterm("Common-mode rejection", "An instrumentation amplifier compares the signal on its two "
            "inputs. It removes the part of the signal that is the same on the two inputs, for "
            "example the mains hum. It amplifies only the difference between the two inputs. Thus "
            "you use a front-end chip and not an ADC without an amplifier."),
    defterm("ADC", "Analog-to-digital converter. It changes the analog voltage of the amplifier "
            "into numbers that a microcontroller can read. In this sensor, the ADC is a 16-bit "
            "ADS1115 that connects through I2C."),
  ]})

SECTIONS.append({"id": "chain", "kicker": "03 · How the sensor operates", "title": "The signal chain",
  "blocks": [
    p("The sensor is a chain from the plant to the dashboard. Two electrodes measure the stem and "
      "one electrode is the reference in the soil. The AD8232 amplifies and filters the signal. The "
      "ADS1115 digitizes it. The ESP32 sends it to Home Assistant."),
    figure(L.flow("From plant to Home Assistant",
            [("Electrodes", "two on the stem, one in the soil"),
             ("AD8232", "amplify ~1100x, band-pass, reference drive"),
             ("ADS1115", "16-bit ADC with I2C"),
             ("M5 ESP32", "read bus, calculate, send"),
             ("Home Assistant", "logs, charts, alerts")],
            note="The only analog wire is from the AD8232 output to the ADS1115. All other connections use I2C."), 1,
      "The signal chain. Amplify the signal first and digitize it second. The same I2C bus also "
      "connects the light sensor, the temperature sensor and the humidity sensor. These sensors "
      "give information about the conditions at the time of the plant trace."),
    callout("key", "Do not connect the electrodes directly to the ADC",
      p("Plant signals are a maximum of some millivolts. The plant cannot supply much current. Thus "
        "each resistance between the plant and the ADC decreases the signal before it goes to the "
        "ADC. The ADS1115 without an amplifier has no common-mode rejection and no reference drive. "
        "Thus the mains hum is larger than the plant signal in the reading.</p><p>The AD8232 gives "
        "you the gain. It has a band-pass filter that lets only the frequencies of the plant "
        "signals go through. It <em>also</em> has a driven reference electrode in the soil, and "
        "this electrode holds the reading stable" + _c("pb_mdpi_ad8232") + ". Thus the reading "
        "shows the signal and not only noise.")),
  ]})

SECTIONS.append({"id": "bom", "kicker": "04 · Parts to get", "title": "Bill of materials",
  "blocks": [
    callout("evidence", "Weak",
      "<p><strong>Provisional and experimental:</strong> This sensor records biopotentials as "
      "relative values, for education and to find correlations. It is <em>not</em> a validated "
      "meter for water, nutrients or stress. Do not use only this signal to make a decision about "
      "irrigation or feed.</p>"),
    p("The cost is approximately NZ$110. The M5Stack parts are Grove modules that you connect "
      "together. The two parts that are not from M5Stack are the AD8232 front-end and the ADS1115 "
      "ADC. These two parts are the usual alternatives with a low cost, because there is no "
      "biopotential amplifier in the Grove modules. The prices are approximate values for the "
      "middle of 2026."),
    table(["Part", "Function", "Where to get it", "Approximate NZD"], [
      ["<strong>M5StickC PLUS2</strong> ESP32 with screen and LiPo battery",
       "Controller and display",
       "<a href='https://shop.m5stack.com/products/m5stickc-plus2-esp32-mini-iot-development-kit' target='_blank' rel='noopener'>M5Stack shop</a> <span style='color:var(--faint)'>(end of life, EOL: M5StampS3 replaces it)</span>",
       "32"],
      ["<strong>ENV IV Unit</strong> (SHT40 + BMP280)",
       "Air temperature, humidity, pressure",
       "<a href='https://shop.m5stack.com/products/env-iv-unit-with-temperature-humidity-air-pressure-sensor-sht40-bmp280' target='_blank' rel='noopener'>M5Stack shop</a>",
       "14"],
      ["<strong>DLight Unit</strong> (BH1750)",
       "Light intensity (lux)",
       "<a href='https://shop.m5stack.com/products/dlight-unit-ambient-light-sensor-bh1750fvi-tr' target='_blank' rel='noopener'>M5Stack shop</a>",
       "12"],
      ["<strong>1-to-3 HUB Unit</strong> (passive I2C splitter)",
       "Connect three devices to one bus",
       "<a href='https://shop.m5stack.com/products/mini-hub-module' target='_blank' rel='noopener'>M5Stack shop</a>",
       "6"],
      ["<strong>AD8232 ECG module</strong> (SparkFun SEN-12650 or an equivalent)",
       "Biopotential front-end <span style='color:var(--faint)'>[not from M5Stack]</span>",
       "<a href='https://www.sparkfun.com/sparkfun-single-lead-heart-rate-monitor-ad8232.html' target='_blank' rel='noopener'>SparkFun</a> · equivalent on AliExpress, approximately NZ$9",
       "9"],
      ["<strong>ADS1115 breakout</strong> (16-bit I2C ADC)",
       "Digitize the analog output <span style='color:var(--faint)'>[not from M5Stack]</span>",
       "<a href='https://www.adafruit.com/product/1085' target='_blank' rel='noopener'>Adafruit product 1085</a> · equivalent, approximately NZ$6",
       "6"],
      ["<strong>Electrodes</strong>: Ag/AgCl EEG cups <em>or</em> stainless probes with snap leads",
       "Skin contact <span style='color:var(--faint)'>[not from M5Stack]</span>",
       "<a href='https://www.sparkfun.com/products/12970' target='_blank' rel='noopener'>SparkFun sensor cable</a> and <a href='https://www.sparkfun.com/products/12969' target='_blank' rel='noopener'>electrode pads</a>, or a medical set of Ag/AgCl electrodes",
       "14"],
      ["<strong>Electrode gel</strong> (Ten20) and micropore tape",
       "Contact with low impedance",
       "Pharmacy",
       "9"],
      ["DuPont jumper wires, a small prototype board, heatshrink",
       "Connections between the AD8232 and the ADS1115",
       "Your spare parts, or an electronics shop",
       "8"],
    ], cls="compact", foot="Total: approximately NZ$110. If the controller is an M5StampS3 and not the StickC, the total is less than NZ$95. The alternative does not have the screen that is on the board of the StickC."),
    callout("warn", "Two parts are at the end of their life (EOL)",
      p("M5Stack stopped the production of the StickC PLUS2 and the ENV IV. But resellers "
        "(RobotShop, Botland, TinyTronics) continue to have them in stock, and they have the most "
        "tutorials. If you want current parts, the <strong>M5StampS3</strong> replaces the "
        "controller and the <strong>ENV Pro</strong> replaces the ENV IV. In the firmware, only two "
        "I2C pin numbers change.")),
  ]})

SECTIONS.append({"id": "wiring", "kicker": "05 · Assemble the sensor", "title": "Wiring",
  "blocks": [
    p("After the controller, the sensor has one I2C bus. The HUB connects this bus to three "
      "devices. The only analog wire in the sensor goes from the output of the AD8232 to the A0 pin "
      "of the ADS1115. The electrodes connect to the header with three pins of the AD8232."),
    figure(wiring_svg(), 2,
      "The wiring. One I2C bus (SDA blue, SCL green, power red) connects the controller to three "
      "devices through the HUB. The only analog connection (amber) is the output of the AD8232 to "
      "A0 of the ADS1115."),
    table(["From", "Pin", "To", "Pin or target"], [
      ["M5 Grove Port A", "SDA (G32)", "HUB &#8594; all I2C devices", "SDA"],
      ["M5 Grove Port A", "SCL (G33)", "HUB &#8594; all I2C devices", "SCL"],
      ["M5 Grove Port A", "5V / GND", "HUB &#8594; ENV and DLight. 3.3V to ADS1115 and AD8232", "VDD / GND"],
      ["AD8232", "OUTPUT", "ADS1115", "A0"],
      ["AD8232", "3.3V / GND", "controller 3.3V / GND", "&#8212;"],
      ["AD8232", "LA / RA / RL", "electrodes", "upper stem, lower stem, soil"],
    ], cls="compact"),
    callout("warn", "Supply the AD8232 with clean 3.3 V",
      p("Use the 3.3 V rail for the chip. Do not use the 5 V USB rail, because it has more noise. "
        "The center point of the output and the noise floor change when the supply changes. Keep "
        "the electrode leads short and twisted. Put the leads away from lights, ballasts and pumps. "
        "A battery (the LiPo of the StickC) gives less noise than USB power.")),
  ]})

SECTIONS.append({"id": "electrodes", "kicker": "06 · How to attach the electrodes", "title": "Electrodes and their position",
  "blocks": [
    p("<strong>Contact impedance</strong> is the resistance between the metal of the electrode and "
      "the tissue of the plant. A bad connection decreases the signal and lets noise go in before "
      "the signal goes to the amplifier. The AD8232 does all the work after this point. The quality "
      "of the electrode contact is the one variable that you control. You can use one of these two "
      "alternatives" + _c("pb_hackster_flora") + ":"),
    grid([
      card("Ag/AgCl EEG cups", p("This alternative gives the best signal quality. Fill the cup with "
           "conductive gel and attach it to the stem with tape. It does not cause a wound in the "
           "plant, but the gel becomes dry. Replace the gel after some days.")),
      card("Stainless probes or needles", p("Put the probe 2 to 3 mm (0.08 to 0.12&nbsp;in) below "
           "the epidermis. This alternative is more stable. It is almost the same as the method of "
           "commercial pin contacts, which measure the signal in the plant. But it causes a wound "
           "in the plant. Thus put the probe in the plant one time only, and use a clean sterilized "
           "probe.")),
    ], cols=2),
    steps([
      ("Put the pair of electrodes along the stem", "Put LA (sense +) on the upper stem near a node. Put RA "
       "(sense &#8722;) 5 to 15 cm (2 to 6&nbsp;in) below LA on the same stem. This pair of "
       "electrodes records the signal that moves along the stem."),
      ("Put the reference in the soil", "Put RL (the driven reference) in the moist soil of the root "
       "zone. It removes the common-mode hum. Make sure that you connect RL."),
      ("Gel and tape", "Put a small quantity of Ten20 below each surface contact. Then attach the "
       "contact with micropore tape, which gives a light and stable pressure. If the baseline "
       "increases slowly and has more noise, the cause is usually that the electrode becomes dry. "
       "The cause is not usually a problem in the plant."),
      ("Wait until the signal is stable", "When metal touches wet tissue, ion exchange occurs at the surface and "
       "makes a small voltage. This voltage is a <strong>half-cell potential</strong>. Wait 10 to "
       "30 minutes for the voltage to become stable. The first drift comes from the chemistry of "
       "the electrode and not from the plant."),
    ]),
    callout("danger", "Needle electrodes cause a wound in the plant",
      p("Make one clean insertion only, with a probe that you sterilized with alcohol. Do not make "
        "a row of holes around the stem, because a row of holes can girdle the stem. A new "
        "insertion causes a variation potential. You can use it one time as a known stimulus. Then "
        "let the wound close.")),
  ]})

SECTIONS.append({"id": "firmware", "kicker": "07 · The code", "title": "ESPHome firmware",
  "blocks": [
    p("The full configuration follows. Put your Wi-Fi, API and OTA secrets in the file "
      "<code>secrets.yaml</code> of ESPHome. Install the firmware from the ESPHome dashboard. Home "
      "Assistant then finds the sensor automatically. For a StampS3 or a Core2, change the board "
      "setting. If it is necessary, also change the two I2C pins."),
    code(
"""esphome:
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
    device_class: problem"""),
    callout("key", "Calibration at the first start",
      p("Attach the electrodes and wait until they are stable. Then read <code>Plant Biopotential "
        "(raw)</code> in Home Assistant. The stable voltage that you read <em>is</em> your "
        "baseline. Replace the <code>1.5</code> in the lambda with this number. Then <code>Plant "
        "Biopotential</code> reads approximately 0 mV when there is no stimulus. It gives positive "
        "and negative values around this value" + _c("pb_esphome_ads1115") + ".")),
  ]})

SECTIONS.append({"id": "read", "kicker": "08 · How to read the output", "title": "How to read plant-biosignal data",
  "blocks": [
    p("The values are <em>changes</em> of the potential. They are not a calibrated physiological "
      "unit. Compare a plant with the same plant at other times. Do not compare plants with each "
      "other in raw millivolts."),
    table(["Signal that you see", "Possible condition"], [
      ["The signal increases and decreases smoothly each day, at the same time as the light sensor", "The circadian rhythm of a plant in good condition. This rhythm is the baseline."],
      ["A fast deflection, then the signal goes back to the baseline slowly, after you touch or move the plant", "A variation potential. It is the usual signal of a wound or stress."],
      ["A step change at the same time as the lights come on or go off", "Response to light. The data in the reference show a detection rate of approximately 85% with this hardware" + _c("pb_pmc_plantsignals")],
      ["The baseline increases slowly and has more noise, and there is no plant event", "The electrode becomes dry. Put new gel on it. It is not a plant problem."],
      ["50/60 Hz noise that is larger than all the other signals", "Mains pickup. Make the leads shorter, twist them, and make the soil reference better."],
      ["A signal that does not change, at a rail (0 or full scale)", "A lead is off or a contact has no connection. Examine the binary sensor."],
    ], cls="compact"),
    p("To get close to the <em>inference</em> of a commercial unit, record data for some weeks. "
      "Record the raw trace, the VPD, the light and the irrigation events. Then find "
      "<strong>your</strong> correlations that occur again. For example, the amplitude of the "
      "signal can decrease strongly before you see wilt, as a first sign of water stress. The "
      "commercial product includes this library of correlations. Send the trace to the <a "
      "href='plant-state-dashboard.html'>plant-state dashboard</a> to use it together with your "
      "other telemetry."),
  ]})

SECTIONS.append({"id": "limits", "kicker": "09 · Limits and calibration", "title": "Limits, calibration and safety",
  "blocks": [
    callout("key", "Limits to know before you solder",
      ul(["<strong>Relative values, not absolute values.</strong> The values are good for trends "
          "and events on one plant. They are not good to compare plants or to read a calibrated "
          "number.",
          "<strong>Set the baseline again each time that you attach the electrodes.</strong> The "
          "half-cell offsets are different each time that you put the electrodes in position. Thus "
          "do the calibration at the first start again.",
          "<strong>The noise floor is higher than in commercial units.</strong> The items that give "
          "the largest decrease in noise are a battery supply, short shielded leads and a small "
          "enclosure.",
          "<strong>ESPHome is for trends.</strong> To record waveforms, install an Arduino sketch "
          "on the controller. The sketch must sample the ADS1115 at its maximum rate of 860 SPS. Or "
          "it must sample the AD8232 on an ESP32 ADC pin at 400 Hz. The investigation of plant "
          "signals used this rate" + _c("pb_arxiv_esp32") + ". The wiring is the same and the "
          "firmware is different."])),
    callout("danger", "Keep the sensor isolated",
      p("Keep the sensor at a low voltage. Supply it with a battery or with USB. Do not connect the "
        "plant electrodes to an item that has a connection to the mains. Use one common ground "
        "only. Thus there is no ground loop through the plant.")),
  ]})
