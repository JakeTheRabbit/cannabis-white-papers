# -*- coding: utf-8 -*-
"""Paper: a DIY plant-biosignal sensor (Vivent-style) from M5Stack + ESPHome."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        grid, card, chip, kv, steps)
import figs_lib as L
from figs import INK, INK2, MUT, LINE, G, GD, GL, BLU, BLUL, AMB, RED, PAPER, FS, MN

SLUG = "plant-biosignal-sensor"
TITLE = "DIY plant-biosignal sensor: read a plant's electrical signals"
EYEBROW = "Build · Precision & automation"
SUB = ("Commercial plant-biosignal sensors clip electrodes to a plant, amplify the tiny voltages it "
       "makes, and log the drift for education — not as a validated water/nutrient/stress meter. You can build the acquisition side "
       "from an M5Stack ESP32, an ECG front-end chip and ESPHome for about NZ$110, and stream it "
       "straight into Home Assistant.")
META = [("wave", "Build guide"), ("gauge", "DIY hardware"),
        ("quote", "Evidence-linked · 4 sources"), ("clock", "~14 min read")]
RELATED = ["plant-state-dashboard", "signal-and-noise", "closed-loop"]
REF_IDS = ["pb_mdpi_ad8232", "pb_arxiv_esp32", "pb_pmc_plantsignals",
           "pb_hackster_flora", "pb_vivent", "pb_esphome_ads1115"]


def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)


# ---- code block that survives the auto-interlinker (wrapped in <code>) ----
def code(text):
    esc = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return ("<pre style=\"background:var(--surface-2);border:1px solid var(--line);"
            "border-radius:10px;padding:16px 18px;overflow:auto;font-family:var(--mono);"
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
    pr.append(f'<g><text x="24" y="330" fill="{MUT}" font-size="10" style="{FS}">Lines:</text>')
    pr.append(f'<line x1="70" y1="326" x2="98" y2="326" stroke="{BLU}" stroke-width="2"/><text x="104" y="330" fill="{MUT}" font-size="10" style="{FS}">SDA</text>')
    pr.append(f'<line x1="140" y1="326" x2="168" y2="326" stroke="{G}" stroke-width="2"/><text x="174" y="330" fill="{MUT}" font-size="10" style="{FS}">SCL</text>')
    pr.append(f'<line x1="206" y1="326" x2="234" y2="326" stroke="{RED}" stroke-width="2"/><text x="240" y="330" fill="{MUT}" font-size="10" style="{FS}">power</text>')
    pr.append(f'<line x1="286" y1="326" x2="314" y2="326" stroke="{AMB}" stroke-width="2.5"/><text x="320" y="330" fill="{MUT}" font-size="10" style="{FS}">analog</text></g>')
    pr.append("</svg>")
    return "".join(pr)


SECTIONS = []

SECTIONS.append({"id": "start", "kicker": "01 · Read this first", "title": "A plant is quietly electric",
  "blocks": [
    lead("Plants generate tiny electrical signals. Ions move across cell membranes when the plant "
         "responds to light, water, wounding or nutrient change, and that movement shows up as a "
         "sub-millivolt voltage you can read with electrodes on the stem" + _c("pb_pmc_plantsignals") + ". "
         "Commercial units like the Vivent VITA1 do exactly this, then use trained models to infer water and stress state "
         "from how the signal drifts" + _c("pb_vivent") + "."),
    p("Electrically, reading a plant is the same problem as reading a heartbeat: a small, noisy, "
      "high-impedance voltage you must amplify cleanly. That means the cheap, proven ECG front-end "
      "chip, the <strong>AD8232</strong>, works straight out of the box for plants" + _c("pb_mdpi_ad8232") +
      ". Bolt it to an ESP32 and ESPHome and you have a logging plant-biosignal sensor for the price "
      "of a night out."),
    callout("note", "What this build is, and isn't",
      ul(["<strong>It reproduces the acquisition</strong>: the raw signal, the daily rhythm, the "
          "big deflections after a stress event, light-on/off detection (one study reported ~85% under its protocol, not guaranteed on this exact "
          "hardware class)" + _c("pb_pmc_plantsignals") + ", all logged in Home Assistant.",
          "<strong>It does not reproduce the paid model.</strong> A VITA1's N/P/K/Ca read-outs come "
          "from a trained model on a curated signal library. You get the millivolts; you build your "
          "own correlations over time.",
          "<strong>ESPHome polls, it doesn't capture waveforms.</strong> Fast sub-second spikes need "
          "the high-rate sketch noted at the end. For trend work, polling is the right tool, and it "
          "already samples finer than a VITA1's 5-minute dashboard."])),
  ]})

SECTIONS.append({"id": "terms", "kicker": "02 · The vocabulary", "title": "The words you need",
  "blocks": [
    defterm("Biopotential", "A voltage a living thing makes across its tissue. In plants it is "
            "microvolts to a few millivolts, riding on a slowly-drifting baseline."),
    defterm("Variation potential", "The big, slow depolarisation that spreads after a wound or "
            "sharp stress. The clearest single event you will see on a DIY rig."),
    defterm("Action potential", "A fast, self-propagating electrical spike. Real but sub-second, so "
            "it needs high-rate sampling to catch, unlike the slow trends."),
    defterm("Electrode", "The metal contact that couples the plant's voltage into your circuit. "
            "Ag/AgCl with gel, or a stainless probe just under the skin."),
    defterm("Common-mode rejection", "An amplifier's ability to ignore noise that appears equally on "
            "both inputs (like mains hum) and keep only the difference. The whole reason to use an "
            "instrumentation front-end rather than a bare ADC."),
    defterm("ADC", "Analog-to-digital converter. Turns the amplifier's analog voltage into numbers a "
            "microcontroller can read. Here, a 16-bit ADS1115 over I2C."),
  ]})

SECTIONS.append({"id": "chain", "kicker": "03 · The idea", "title": "The signal chain",
  "blocks": [
    p("Everything is one line from plant to dashboard. Two electrodes sense the stem, one references "
      "the soil; the AD8232 amplifies and filters; the ADS1115 digitises; the ESP32 publishes."),
    figure(L.flow("From plant to Home Assistant",
            [("Electrodes", "two on the stem, one in the soil"),
             ("AD8232", "amplify ~1100x, band-pass, drive reference"),
             ("ADS1115", "16-bit ADC over I2C"),
             ("M5 ESP32", "read bus, compute, publish"),
             ("Home Assistant", "log, chart, alert")],
            note="The only analog wire in the build is AD8232 output into the ADS1115. Everything else is I2C."), 1,
      "The chain. Amplify first, digitise second, and the same I2C bus also carries the light, "
      "temperature and humidity sensors that give the plant trace its context."),
    callout("key", "Why not just wire electrodes to the ADC?",
      p("Plant signals are tiny and sit on a high-impedance source, so mains hum swamps them. The "
        "ADS1115 alone has no common-mode rejection and no reference drive. The AD8232 gives you the "
        "gain, the band-pass filter <em>and</em> a driven soil-reference electrode that holds the "
        "reading steady" + _c("pb_mdpi_ad8232") + ". It is the difference between a signal and a mess.")),
  ]})

SECTIONS.append({"id": "bom", "kicker": "04 · What to buy", "title": "Bill of materials",
  "blocks": [
    callout("evidence", "Community / evidence note",
      "<p><strong>Provisional / experimental:</strong> This build logs relative biopotentials for education and "
      "correlation hunting. It is <em>not</em> a validated water, nutrient, or stress meter. Do not irrigate or "
      "feed from this signal alone.</p>"),
    p("About NZ$110. M5Stack parts come as plug-together Grove modules; the two non-M5Stack parts "
      "(the AD8232 front-end and the ADS1115 ADC) are the standard cheap substitutes, because nobody "
      "sells a biopotential amplifier in the Grove ecosystem. Prices are indicative, mid-2026."),
    table(["Part", "Role", "Where to buy", "~NZD"], [
      ["<strong>M5StickC PLUS2</strong> ESP32 + screen + LiPo",
       "Controller &amp; display",
       "<a href='https://shop.m5stack.com/products/m5stickc-plus2-esp32-mini-iot-development-kit' target='_blank' rel='noopener'>shop.m5stack.com</a> <span style='color:var(--faint)'>(EOL; successor M5StampS3)</span>",
       "32"],
      ["<strong>ENV IV Unit</strong> (SHT40 + BMP280)",
       "Air temp, humidity, pressure",
       "<a href='https://shop.m5stack.com/products/env-iv-unit-with-temperature-humidity-air-pressure-sensor-sht40-bmp280' target='_blank' rel='noopener'>shop.m5stack.com</a>",
       "14"],
      ["<strong>DLight Unit</strong> (BH1750)",
       "Light level (lux)",
       "<a href='https://shop.m5stack.com/products/dlight-unit-ambient-light-sensor-bh1750fvi-tr' target='_blank' rel='noopener'>shop.m5stack.com</a>",
       "12"],
      ["<strong>1-to-3 HUB Unit</strong> (passive I2C splitter)",
       "Share one bus across three devices",
       "<a href='https://shop.m5stack.com/products/mini-hub-module' target='_blank' rel='noopener'>shop.m5stack.com</a>",
       "6"],
      ["<strong>AD8232 ECG module</strong> (SparkFun SEN-12650 or clone)",
       "Biopotential front-end <span style='color:var(--faint)'>[non-M5Stack]</span>",
       "<a href='https://www.sparkfun.com/sparkfun-single-lead-heart-rate-monitor-ad8232.html' target='_blank' rel='noopener'>sparkfun.com</a> · clone on AliExpress ~NZ$9",
       "9"],
      ["<strong>ADS1115 breakout</strong> (16-bit I2C ADC)",
       "Digitise the analog output <span style='color:var(--faint)'>[non-M5Stack]</span>",
       "<a href='https://www.adafruit.com/product/1085' target='_blank' rel='noopener'>adafruit.com/product/1085</a> · clone ~NZ$6",
       "6"],
      ["<strong>Electrodes</strong> — Ag/AgCl EEG cups <em>or</em> stainless probes + snap leads",
       "Skin contact <span style='color:var(--faint)'>[non-M5Stack]</span>",
       "<a href='https://www.sparkfun.com/products/12970' target='_blank' rel='noopener'>SparkFun sensor cable</a> + <a href='https://www.sparkfun.com/products/12969' target='_blank' rel='noopener'>electrode pads</a>, or medical Ag/AgCl set",
       "14"],
      ["<strong>Electrode gel</strong> (Ten20) + micropore tape",
       "Low-impedance contact",
       "Pharmacy",
       "9"],
      ["DuPont jumpers, small proto board, heatshrink",
       "Glue between AD8232 and ADS1115",
       "Junk box / any hobby shop",
       "8"],
    ], cls="compact", foot="Total &#8776; NZ$110. A bare M5StampS3 instead of the StickC drops it below NZ$95 at the cost of the on-board screen."),
    callout("warn", "Two parts are marked EOL",
      p("M5Stack has retired the StickC PLUS2 and ENV IV, but both are still stocked by resellers "
        "(RobotShop, Botland, TinyTronics) and have the most tutorials. If you want current parts, "
        "the <strong>M5StampS3</strong> replaces the controller and the <strong>ENV Pro</strong> "
        "replaces the ENV IV. The firmware only changes by two I2C pin numbers.")),
  ]})

SECTIONS.append({"id": "wiring", "kicker": "05 · Put it together", "title": "Wiring",
  "blocks": [
    p("Everything downstream of the controller is one I2C bus, fanned out by the HUB. The single "
      "analog wire in the whole build is the AD8232 output into the ADS1115's A0 pin. Electrodes plug "
      "into the AD8232's three-pin header."),
    figure(wiring_svg(), 2,
      "Wiring. One I2C bus (SDA blue, SCL green, power red) fans out through the HUB to three "
      "devices; the lone analog hop (amber) is AD8232 output into ADS1115 A0."),
    table(["From", "Pin", "To", "Pin / target"], [
      ["M5 Grove Port A", "SDA (G32)", "HUB &#8594; all I2C devices", "SDA"],
      ["M5 Grove Port A", "SCL (G33)", "HUB &#8594; all I2C devices", "SCL"],
      ["M5 Grove Port A", "5V / GND", "HUB &#8594; ENV/DLight; 3.3V to ADS1115 + AD8232", "VDD / GND"],
      ["AD8232", "OUTPUT", "ADS1115", "A0"],
      ["AD8232", "3.3V / GND", "controller 3.3V / GND", "&#8212;"],
      ["AD8232", "LA / RA / RL", "electrodes", "upper stem / lower stem / soil"],
    ], cls="compact"),
    callout("warn", "Power the AD8232 from clean 3.3 V",
      p("Its output centre-point and noise floor track the supply, so feed it the 3.3 V rail, not the "
        "noisy 5 V USB rail. Keep electrode leads short and twisted, and route them away from lights, "
        "ballasts and pumps. Battery power (the StickC's LiPo) beats USB for noise.")),
  ]})

SECTIONS.append({"id": "electrodes", "kicker": "06 · The hard part", "title": "Electrodes and placement",
  "blocks": [
    p("This is where a DIY rig lives or dies. The AD8232 is happy; your <strong>contact impedance</strong> "
      "is the enemy. Two workable options" + _c("pb_hackster_flora") + ":"),
    grid([
      card("Ag/AgCl EEG cups", p("Best signal quality. Fill the cup with conductive gel and tape it "
           "to the stem. Non-invasive, but the gel dries and must be refreshed every few days.")),
      card("Stainless probes / needles", p("Insert 2&#8211;3 mm just under the epidermis. More stable "
           "and closest to how commercial pin-contacts read &lsquo;inside&rsquo; the plant, but it "
           "wounds the plant, so use one clean, sterilised insertion.")),
    ], cols=2),
    steps([
      ("Place the pair along the stem", "LA (sense +) on the upper stem near a node; RA (sense &#8722;) "
       "5&#8211;15 cm lower on the same stem. This pair captures the travelling signal."),
      ("Reference into the soil", "RL (the driven reference) goes into the moist root-zone soil. It is "
       "what cancels common-mode hum, so don't skip it."),
      ("Gel and tape", "A dab of Ten20 under each surface contact, then micropore tape for light, "
       "steady pressure. A rising, noisy baseline is usually a drying electrode, not a sick plant."),
      ("Let it settle", "The baseline drifts for 10&#8211;30 minutes as the half-cell potentials "
       "equalise. Ignore that window."),
    ]),
    callout("danger", "Needle electrodes wound the plant",
      p("A fresh insertion itself triggers a variation potential, useful once as a known stimulus, "
        "then let it heal. Sterilise with alcohol and use a single clean insertion; don't ring-bark "
        "the stem with a row of holes.")),
  ]})

SECTIONS.append({"id": "firmware", "kicker": "07 · The code", "title": "ESPHome firmware",
  "blocks": [
    p("The full config. Put your Wi-Fi, API and OTA secrets in ESPHome's <code>secrets.yaml</code>, "
      "flash from the ESPHome dashboard, and it auto-discovers into Home Assistant. On a StampS3 or "
      "Core2, change the board line and, if needed, the two I2C pins."),
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
    callout("key", "First-boot calibration",
      p("With electrodes attached and settled, read <code>Plant Biopotential (raw)</code> in Home "
        "Assistant. Whatever steady voltage it sits at <em>is</em> your baseline, so replace the "
        "<code>1.5</code> in the lambda with that number. Then <code>Plant Biopotential</code> reads "
        "~0 mV at rest and swings signed around it" + _c("pb_esphome_ads1115") + ".")),
  ]})

SECTIONS.append({"id": "read", "kicker": "08 · Make sense of it", "title": "Reading the data",
  "blocks": [
    p("These are <em>changes</em> in potential, not a calibrated physiological unit. Compare a plant "
      "to itself over time, never plant-to-plant in raw millivolts."),
    table(["What you see", "Likely meaning"], [
      ["Smooth daily rise and fall tracking the light sensor", "Healthy circadian activity, the baseline rhythm of a happy plant"],
      ["Sharp deflection then slow recovery after you touch or move it", "A variation potential, the classic wound/stress signal"],
      ["Step change synced to lights on/off", "Light response (documented ~85% detectable on this hardware)" + _c("pb_pmc_plantsignals")],
      ["Baseline slowly climbing and getting noisier, no plant event", "Electrode drying out, re-gel it, not a plant problem"],
      ["50/60 Hz fuzz dominating everything", "Mains pickup, shorten and twist the leads, improve the soil reference"],
      ["Flat line at a rail (0 or full-scale)", "Lead-off or broken contact, check the binary sensor"],
    ], cls="compact"),
    p("To approach a commercial unit's <em>inference</em>, log the raw trace alongside VPD, light and "
      "irrigation events for a few weeks, then hunt for <strong>your own</strong> repeatable "
      "correlations, for example signal amplitude collapsing before visible wilt as an early "
      "water-stress warning. That correlation library is exactly what the paid product ships "
      "pre-built. Feed the trace into the <a href='plant-state-dashboard.html'>plant-state dashboard</a> "
      "to combine it with your other telemetry."),
  ]})

SECTIONS.append({"id": "limits", "kicker": "09 · Straight talk", "title": "Limits, calibration and safety",
  "blocks": [
    callout("key", "Set expectations before you solder",
      ul(["<strong>Relative, not absolute.</strong> Good for trends and events on one plant, not for "
          "comparing plants or reading a calibrated number.",
          "<strong>Re-baseline every reattach.</strong> Half-cell offsets differ each time you place "
          "electrodes, so redo the first-boot calibration.",
          "<strong>Higher noise floor than commercial rigs.</strong> Battery power, short shielded "
          "leads and a small enclosure help most.",
          "<strong>ESPHome is for trends.</strong> For actual waveforms, flash a plain Arduino sketch "
          "that samples the ADS1115 at its full 860 SPS (or the AD8232 off an ESP32 ADC pin at 400 Hz, "
          "the rate used in the published plant-signal study" + _c("pb_arxiv_esp32") + "). Same wiring, "
          "different firmware."])),
    callout("danger", "Keep it isolated",
      p("Keep the whole thing low-voltage and battery or USB powered. Never connect plant electrodes "
        "to anything mains-referenced, and use one common ground only, so you don't create a ground "
        "loop through the plant.")),
  ]})
