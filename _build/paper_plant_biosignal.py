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
       "This guide shows how to make a sensor that records these signals, and how to change the "
       "signal into a water-status number of your own. The sensor has an M5Stack ESP32, a DC-coupled "
       "instrumentation amplifier and ESPHome, and the cost is approximately NZ$110. The sensor is "
       "not a validated meter for water or nutrients, but it shows the electrical activity of the "
       "plant in real time.")
META = [("wave", "Assembly guide"), ("gauge", "DIY hardware"),
        ("quote", "10 sources"), ("clock", "~18 min to read")]
RELATED = ["plant-state-dashboard", "signal-and-noise", "closed-loop"]
REF_IDS = ["pb_pmc_plantsignals", "pb_vivent", "pb_najdenovska_stress", "pb_ad8232_ds",
           "pb_mdpi_ad8232", "pb_ad623_ds", "pb_ads1115_ds", "pb_esphome_ads1115",
           "pb_hackster_flora", "pb_arxiv_esp32"]


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
    W, H = 760, 400
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
    pr.append(f'<text x="182" y="214" text-anchor="end" fill="{MUT}" font-size="10" style="{MN}">3V3 / G</text>')
    # hub
    pr.append(box(210, 150, 118, 74, "1-to-3 HUB", "I2C splitter"))
    pr.append(f'<path d="M174 186 H210" stroke="{BLU}" stroke-width="2" fill="none"/>')
    pr.append(f'<path d="M174 200 H210" stroke="{G}" stroke-width="2" fill="none"/>')
    pr.append(f'<path d="M174 214 H210" stroke="{RED}" stroke-width="2" fill="none"/>')
    # three branches
    pr.append(box(380, 26, 160, 60, "ENV IV Unit", "SHT40 / BMP280"))
    pr.append(box(380, 104, 160, 52, "DLight Unit", "BH1750 0x23"))
    pr.append(box(380, 176, 160, 84, "ADS1115  0x48", "16-bit ADC"))
    pr.append(f'<text x="392" y="228" fill="{MUT}" font-size="10" style="{MN}">A0 &#9668; amp output</text>')
    pr.append(f'<text x="392" y="246" fill="{MUT}" font-size="10" style="{MN}">A1 &#9668; bias 1.32 V</text>')
    pr.append(f'<path d="M328 176 C352 176 348 56 380 56" stroke="{BLU}" stroke-width="2" fill="none"/>')
    pr.append(f'<path d="M328 190 C356 190 352 130 380 130" stroke="{G}" stroke-width="2" fill="none"/>')
    pr.append(f'<path d="M328 200 C356 200 352 196 380 196" stroke="{BLU}" stroke-width="2" fill="none"/>')
    pr.append(f'<path d="M328 210 C356 210 352 206 380 206" stroke="{G}" stroke-width="2" fill="none"/>')
    # AD623 front-end board
    pr.append(box(584, 176, 152, 104, "AD623 board", "G = 10, RC filter"))
    pr.append(f'<text x="596" y="234" fill="{MUT}" font-size="10" style="{MN}">&#9668; OUT, BIAS</text>')
    pr.append(f'<text x="596" y="252" fill="{MUT}" font-size="10" style="{MN}">+IN / &#8722;IN / SOIL</text>')
    pr.append(f'<text x="596" y="270" fill="{MUT}" font-size="10" style="{MN}">3V3 / GND</text>')
    pr.append(f'<path d="M540 222 C562 222 562 228 584 228" stroke="{AMB}" stroke-width="2.5" fill="none"/>')
    pr.append(f'<path d="M540 240 C562 240 562 236 584 236" stroke="{AMB}" stroke-width="2.5" fill="none" stroke-dasharray="4 3"/>')
    pr.append(f'<text x="546" y="214" fill="{AMB}" font-size="9.5" style="{MN}">analog</text>')
    # electrodes
    pr.append(f'<circle cx="608" cy="318" r="6" fill="{AMB}"/><text x="620" y="322" fill="{INK2}" font-size="10.5" style="{FS}">+IN &#8594; upper stem</text>')
    pr.append(f'<circle cx="608" cy="340" r="6" fill="{AMB}"/><text x="620" y="344" fill="{INK2}" font-size="10.5" style="{FS}">&#8722;IN &#8594; lower stem</text>')
    pr.append(f'<circle cx="608" cy="362" r="6" fill="{RED}"/><text x="620" y="366" fill="{INK2}" font-size="10.5" style="{FS}">SOIL &#8594; root zone (bias)</text>')
    pr.append(f'<path d="M616 280 V312" stroke="{LINE}" stroke-width="1.5" fill="none"/>')
    # legend
    pr.append(f'<g><text x="24" y="340" fill="{MUT}" font-size="10" style="{FS}">Wires:</text>')
    pr.append(f'<line x1="70" y1="336" x2="98" y2="336" stroke="{BLU}" stroke-width="2"/><text x="104" y="340" fill="{MUT}" font-size="10" style="{FS}">SDA</text>')
    pr.append(f'<line x1="140" y1="336" x2="168" y2="336" stroke="{G}" stroke-width="2"/><text x="174" y="340" fill="{MUT}" font-size="10" style="{FS}">SCL</text>')
    pr.append(f'<line x1="206" y1="336" x2="234" y2="336" stroke="{RED}" stroke-width="2"/><text x="240" y="340" fill="{MUT}" font-size="10" style="{FS}">power</text>')
    pr.append(f'<line x1="286" y1="336" x2="314" y2="336" stroke="{AMB}" stroke-width="2.5"/><text x="320" y="340" fill="{MUT}" font-size="10" style="{FS}">analog</text></g>')
    pr.append("</svg>")
    return "".join(pr)


SECTIONS = []

SECTIONS.append({"id": "start", "kicker": "01 · Read this first", "title": "Purpose and scope",
  "blocks": [
    lead("Plants make small electrical signals. When a plant changes in response to light, water, a "
         "wound or a change in nutrients, ions move across the cell membranes. This movement makes "
         "a voltage of less than one millivolt to some millivolts. You can read this voltage with "
         "electrodes on the stem" + _c("pb_pmc_plantsignals") + ". Commercial units, for example "
         "the Vivent VITA1, do the same. They then use trained models to calculate the water "
         "condition and the stress condition from the signal" + _c("pb_vivent") + _c("pb_najdenovska_stress") + "."),
    p("The water signal is slow. It is a drift of the baseline over minutes and hours. Thus the "
      "amplifier must be <strong>DC-coupled</strong>: it must pass a voltage that changes slowly, "
      "and also a voltage that does not change. An ECG chip such as the AD8232 is not correct for "
      "this work. Its high-pass filter removes all the signal that is slower than approximately "
      "0.5 Hz" + _c("pb_ad8232_ds") + ". This guide uses an AD623 instrumentation amplifier "
      "with no high-pass filter, and a 16-bit ADS1115 ADC" + _c("pb_ad623_ds") + ". The cost is "
      "approximately NZ$110."),
    callout("note", "Functions and limits of this sensor",
      ul(["<strong>This sensor does the same data acquisition.</strong> It records the raw signal, "
          "the slow drift, the rhythm of each day, the large deflections after a stress event and "
          "the change when the light starts and stops. It records all of this in Home Assistant.",
          "<strong>This sensor does not give the model of the commercial product.</strong> The "
          "water, N, P, K and Ca readings of a VITA1 come from a trained model and a library of "
          "signals. Section 10 shows how to train a model of your own with the sensors that you "
          "have now.",
          "<strong>ESPHome reads the sensor at set intervals. It does not record fast "
          "waveforms.</strong> This sensor records trends and events of some seconds or longer. "
          "For spikes of less than one second, refer to section 11."])),
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
            "along the tissue. Action potentials occur in plants, but each action potential is "
            "shorter than one second. Thus a high sampling rate is necessary to record them. This "
            "sensor measures slow trends and not action potentials."),
    defterm("DC-coupled", "An amplifier that is DC-coupled passes all the frequencies down to 0 Hz. "
            "A voltage that does not change goes through it. An AC-coupled amplifier has a "
            "high-pass filter, which removes the slow part of the signal. The slow part is the "
            "part that shows the water condition of the plant."),
    defterm("Instrumentation amplifier", "An amplifier that measures the difference between two "
            "inputs. It removes the part of the signal that is the same on the two inputs, for "
            "example the mains hum. This is <strong>common-mode rejection</strong>. The inputs "
            "have a very high impedance, thus they take almost no current from the plant."),
    defterm("Electrode", "The metal contact that connects the voltage of the plant to your circuit. "
            "The contact is a stainless needle in the stem, or an Ag/AgCl cup with gel on the "
            "surface."),
    defterm("Half-cell potential", "When metal touches wet tissue, ions move at the surface and make "
            "a small voltage. The voltage can be tens of millivolts, and it is different for each "
            "electrode. It is larger than the plant signal. The circuit and the software in this "
            "guide must accept it and then remove it."),
    defterm("ADC", "Analog-to-digital converter. It changes the analog voltage of the amplifier "
            "into numbers that a microcontroller can read. In this sensor, the ADC is a 16-bit "
            "ADS1115 that connects through I2C."),
  ]})

SECTIONS.append({"id": "chain", "kicker": "03 · How the sensor operates", "title": "The signal chain",
  "blocks": [
    p("The sensor is a chain from the plant to the dashboard. Two needle electrodes measure the "
      "stem. One electrode in the root zone holds the plant at a bias voltage. A low-pass filter "
      "removes the fast noise. The AD623 amplifies the difference 10 times. The ADS1115 digitizes "
      "it. The ESP32 sends it to Home Assistant."),
    figure(L.flow("From plant to Home Assistant",
            [("Electrodes", "two in the stem, one in the root zone"),
             ("RC filter", "10 kΩ + 1 µF, cut-off ~8 Hz"),
             ("AD623", "gain 10, DC-coupled, 2 GΩ inputs"),
             ("ADS1115", "differential, 8 samples/s"),
             ("M5 ESP32", "average, detrend, send")],
            note="There is no high-pass filter in the chain. The slow drift goes through to Home Assistant."), 1,
      "The signal chain. Filter, amplify and then digitize. The same I2C bus also connects the light "
      "sensor, the temperature sensor and the humidity sensor. These sensors give information about "
      "the conditions at the time of the plant trace."),
    callout("key", "Why not the AD8232 module?",
      p("Many DIY plant sensors use the AD8232 heart-rate module, because it is cheap and it has "
        "good common-mode rejection" + _c("pb_mdpi_ad8232") + ". But the AD8232 is an ECG chip. "
        "Its high-pass filter removes the half-cell potential of the electrodes, and it also "
        "removes all the plant signal that is slower than approximately 0.5 Hz" + _c("pb_ad8232_ds") +
        ". A change in water condition occurs over minutes or hours. Thus the AD8232 removes the "
        "signal that you want.</p><p>The AD8232 is correct for fast events: a light step, a touch, "
        "a wound. It is not correct for the water trend. For this work, use a DC-coupled amplifier.")),
  ]})

SECTIONS.append({"id": "bom", "kicker": "04 · Parts to get", "title": "Bill of materials",
  "blocks": [
    callout("evidence", "Weak",
      "<p><strong>Provisional and experimental:</strong> This sensor records biopotentials as "
      "relative values, for education and to find correlations. It is <em>not</em> a validated "
      "meter for water, nutrients or stress. Do not use only this signal to make a decision about "
      "irrigation or feed.</p>"),
    p("The cost is approximately NZ$110. The M5Stack parts are Grove modules that you connect "
      "together. The front-end is a small board that you solder. All its parts are through-hole "
      "parts, thus a beginner can solder them. The prices are approximate values for the middle "
      "of 2026."),
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
      ["<strong>AD623ANZ</strong> (8-pin DIP) and an 8-pin socket",
       "DC-coupled instrumentation amplifier <span style='color:var(--faint)'>[not from M5Stack]</span>",
       "Electronics distributors (RS, Digi-Key, Mouser, element14)",
       "12"],
      ["<strong>ADS1115 breakout</strong> (16-bit I2C ADC)",
       "Digitize the amplifier output <span style='color:var(--faint)'>[not from M5Stack]</span>",
       "<a href='https://www.adafruit.com/product/1085' target='_blank' rel='noopener'>Adafruit product 1085</a> · equivalent, approximately NZ$6",
       "6"],
      ["Resistors: 11 kΩ (1), 10 kΩ (3), 1.5 kΩ (1), 1 kΩ (1). Capacitors: 1 µF film (1), 10 µF (1), 100 nF (1)",
       "Gain, input filter, bias voltage, supply decoupling",
       "Any electronics shop",
       "4"],
      ["<strong>Electrodes</strong>: stainless needles (acupuncture type) with snap leads, <em>or</em> Ag/AgCl EEG cups",
       "Contact with the plant <span style='color:var(--faint)'>[not from M5Stack]</span>",
       "<a href='https://www.sparkfun.com/products/12970' target='_blank' rel='noopener'>SparkFun sensor cable</a>, or a medical set of electrodes",
       "14"],
      ["Small prototype board, DuPont jumper wires, heatshrink, shielded twin cable",
       "Front-end board and electrode leads",
       "Your spare parts, or an electronics shop",
       "10"],
    ], cls="compact", foot="Total: approximately NZ$110. If the controller is an M5StampS3 and not the StickC, the total is less than NZ$95. The alternative does not have the screen that is on the board of the StickC."),
    callout("warn", "Two parts are at the end of their life (EOL)",
      p("M5Stack stopped the production of the StickC PLUS2 and the ENV IV. But resellers "
        "(RobotShop, Botland, TinyTronics) continue to have them in stock, and they have the most "
        "tutorials. If you want current parts, the <strong>M5StampS3</strong> replaces the "
        "controller and the <strong>ENV Pro</strong> replaces the ENV IV. In the firmware, only two "
        "I2C pin numbers change.")),
  ]})

SECTIONS.append({"id": "frontend", "kicker": "05 · Solder the front-end", "title": "The front-end circuit",
  "blocks": [
    p("The front-end has three parts: a bias voltage, an input filter and the amplifier. Solder "
      "them on one small prototype board. Put the AD623 in a socket."),
    steps([
      ("Make the bias voltage", "Connect a 1.5 kΩ resistor from 3.3 V to a point that is the "
       "<strong>BIAS</strong> node, and a 1 kΩ resistor from BIAS to GND. Put the 10 µF capacitor "
       "from BIAS to GND. BIAS is 3.3 × 1 / 2.5 = 1.32 V. This voltage is in the input range of "
       "the AD623 on a 3.3 V supply, which goes up to 3.3 − 1.5 = 1.8 V" + _c("pb_ad623_ds") + "."),
      ("Make the input filter", "Put a 10 kΩ resistor in series with each stem electrode lead. "
       "After the resistors, put the 1 µF film capacitor between the two leads. The cut-off is "
       "1 / (2π × 20 kΩ × 1 µF) ≈ 8 Hz. The filter removes radio noise and much of the mains hum. "
       "It does not touch the slow plant signal."),
      ("Connect the amplifier", "Make the connections in the table below. The 11 kΩ resistor sets "
       "the gain: G = 1 + 100 kΩ / 11 kΩ = 10.09" + _c("pb_ad623_ds") + ". Put the 100 nF "
       "capacitor from pin 7 to pin 4, near the chip."),
      ("Connect the soil electrode", "Connect the root-zone electrode to BIAS through a 10 kΩ "
       "resistor. This holds the plant at 1.32 V, in the input range of the amplifier. It also "
       "gives a path for the small input current of the AD623."),
    ]),
    table(["AD623 pin", "Name", "Connect to"], [
      ["1 and 8", "&#8722;RG, +RG", "11 kΩ resistor between the two pins (gain 10.09)"],
      ["2", "&#8722;IN", "Lower-stem electrode, after its 10 kΩ resistor"],
      ["3", "+IN", "Upper-stem electrode, after its 10 kΩ resistor"],
      ["4", "&#8722;VS", "GND"],
      ["5", "REF", "BIAS (1.32 V)"],
      ["6", "OUTPUT", "ADS1115 A0"],
      ["7", "+VS", "3.3 V"],
      ["&#8212;", "BIAS node", "ADS1115 A1, and the soil electrode through 10 kΩ"],
    ], cls="compact", caption="AD623 connections (8-pin DIP)."),
    callout("key", "The numbers: why gain 10 is correct",
      p("The half-cell potential of the electrodes can be tens of millivolts. Together with the "
        "plant signal, the input can be up to approximately ±100 mV. At gain 10, the output moves "
        "±1 V around BIAS. The AD623 output can go from 0.01 V up to approximately 3.15 V on a "
        "3.3 V supply" + _c("pb_ad623_ds") + ". Thus there is space for the offset, and the output "
        "does not stop at a rail.</p><p>The ADS1115 measures A0 minus A1 at the ±2.048 V range. "
        "One bit is 62.5 µV at the ADC, thus 6.2 µV at the electrodes" + _c("pb_ads1115_ds") +
        ". This resolution is sufficient for the slow plant signal. A higher gain gives more "
        "resolution, but then a large electrode offset can push the output to a rail.")),
    callout("tip", "Why the ADC does not connect directly to the electrodes",
      p("The ADS1115 has an input impedance of some megohms, and the impedance decreases at its "
        "small input ranges" + _c("pb_ads1115_ds") + ". A needle in a stem has a high source "
        "impedance. The ADC takes current from the plant and the reading decreases and drifts. The "
        "AD623 has an input impedance of 2 GΩ and an input current of a maximum of 25 nA" +
        _c("pb_ad623_ds") + ". Thus it takes almost no current from the plant.")),
  ]})

SECTIONS.append({"id": "wiring", "kicker": "06 · Assemble the sensor", "title": "Wiring",
  "blocks": [
    p("After the controller, the sensor has one I2C bus. The HUB connects this bus to three "
      "devices. Two analog wires go from the front-end board to the ADS1115: the amplifier output "
      "to A0, and BIAS to A1. The ADS1115 measures the difference between them, thus the 1.32 V "
      "bias does not show in the reading."),
    figure(wiring_svg(), 2,
      "The wiring. One I2C bus (SDA blue, SCL green, power red) connects the controller to three "
      "devices through the HUB. The two analog connections (amber) go from the AD623 board to A0 "
      "and A1 of the ADS1115."),
    table(["From", "Pin", "To", "Pin or target"], [
      ["M5 Grove Port A", "SDA (G32)", "HUB &#8594; all I2C devices", "SDA"],
      ["M5 Grove Port A", "SCL (G33)", "HUB &#8594; all I2C devices", "SCL"],
      ["M5 Grove Port A", "5V / GND", "HUB &#8594; ENV and DLight", "VDD / GND"],
      ["M5 3V3 pin", "3.3V / GND", "ADS1115 and AD623 board", "VDD / GND"],
      ["AD623 board", "OUTPUT (pin 6)", "ADS1115", "A0"],
      ["AD623 board", "BIAS", "ADS1115", "A1"],
      ["AD623 board", "+IN / &#8722;IN / SOIL", "electrodes", "upper stem, lower stem, root zone"],
    ], cls="compact"),
    callout("warn", "Supply the front-end with clean 3.3 V",
      p("Use the 3.3 V rail for the AD623, the bias divider and the ADS1115. Do not use the 5 V USB "
        "rail, because it has more noise, and because an output above 3.3 V can damage the ADS1115 "
        "inputs. Keep the electrode leads short. Use shielded twin cable, and connect the shield to "
        "GND at the board end only. Put the leads away from lights, ballasts and pumps. A battery "
        "(the LiPo of the StickC) gives less noise than USB power.")),
  ]})

SECTIONS.append({"id": "electrodes", "kicker": "07 · How to attach the electrodes", "title": "Electrodes and their position",
  "blocks": [
    p("<strong>Contact impedance</strong> is the resistance between the metal of the electrode and "
      "the tissue of the plant. A bad connection decreases the signal and lets noise go in. The "
      "quality of the electrode contact is the one variable that you control. You can use one of "
      "these two alternatives" + _c("pb_hackster_flora") + ":"),
    grid([
      card("Stainless needles (recommended)", p("Put the needle 2 to 3 mm (0.08 to 0.12&nbsp;in) "
           "into the stem. This alternative is the most stable over weeks, and it is the method of "
           "commercial units. But it causes a wound in the plant. Thus put the needle in the plant "
           "one time only, and use a clean sterilized needle.")),
      card("Ag/AgCl EEG cups", p("Fill the cup with conductive gel and attach it to the stem with "
           "tape. It does not cause a wound in the plant. But the gel becomes dry, and each new "
           "gel changes the offset. This alternative is better for a short test than for a full "
           "grow.")),
    ], cols=2),
    steps([
      ("Put the pair of electrodes along the stem", "Put +IN on the upper stem near a node. Put "
       "&#8722;IN 5 to 15 cm (2 to 6&nbsp;in) below +IN on the same stem. This pair of electrodes "
       "records the signal that moves along the stem."),
      ("Put the soil electrode in the root zone", "Put the SOIL electrode in the moist substrate. "
       "It holds the plant at the bias voltage. Without it, the inputs float and the reading goes "
       "to a rail."),
      ("Fix the leads", "Attach each lead to the stem or the stake with tape, so that the leads do "
       "not pull the needles. A lead that moves gives a large deflection that is not from the "
       "plant."),
      ("Wait until the signal is stable", "The half-cell potential of a new electrode drifts. Wait "
       "at least one hour, and for needles one day, before you use the trace. The first drift "
       "comes from the chemistry of the electrode and from the wound, not from the condition of "
       "the plant."),
    ]),
    callout("danger", "Needle electrodes cause a wound in the plant",
      p("Make one clean insertion only, with a needle that you sterilized with alcohol. Do not make "
        "a row of holes around the stem, because a row of holes can girdle the stem. A new "
        "insertion causes a variation potential. You can use it one time as a known stimulus. Then "
        "let the wound close.")),
  ]})

SECTIONS.append({"id": "firmware", "kicker": "08 · The code", "title": "ESPHome firmware",
  "blocks": [
    p("The full configuration follows. Put your Wi-Fi, API and OTA secrets in the file "
      "<code>secrets.yaml</code> of ESPHome. Install the firmware from the ESPHome dashboard. Home "
      "Assistant then finds the sensor automatically. For a StampS3 or a Core2, change the board "
      "setting. If it is necessary, also change the two I2C pins. The configuration passes "
      "<code>esphome config</code> on ESPHome 2026.7."),
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
      - delayed_on: 30s"""),
    table(["Entity", "What it shows", "Use it for"], [
      ["Plant Biopotential", "Voltage at the electrodes in mV, 10-second mean, offset included", "Events: light steps, touch, wound"],
      ["Plant Biopotential 5 min", "The same value, 5-minute mean", "The slow drift, and the input to the model in section 10"],
      ["Plant Biopotential Detrended", "The signal minus its own 30-minute baseline", "The rhythm of each day and the response to each irrigation, without the electrode offset"],
      ["Electrode Fault", "On when the amplifier output stays near a rail for 30 s", "An alert: a lead is off or an electrode has no contact"],
    ], cls="compact"),
    callout("key", "No calibration at the first start",
      p("The ADS1115 measures A0 minus A1, thus the 1.32 V bias does not show in the reading" +
        _c("pb_esphome_ads1115") + ". <code>Plant Biopotential</code> shows the true voltage at "
        "the electrodes, which includes the half-cell offset. The offset is different each time "
        "that you attach the electrodes. Do not try to set it to zero. Use the detrended entity, "
        "or the changes in the 5-minute entity.")),
  ]})

SECTIONS.append({"id": "read", "kicker": "09 · How to read the output", "title": "How to read plant-biosignal data",
  "blocks": [
    p("The values are <em>changes</em> of the potential. They are not a calibrated physiological "
      "unit. Compare a plant with the same plant at other times. Do not compare plants with each "
      "other in raw millivolts."),
    table(["Signal that you see", "Possible condition"], [
      ["The detrended signal increases and decreases smoothly each day, at the same time as the light sensor", "The circadian rhythm of a plant in good condition. This rhythm is the baseline."],
      ["A step change at the same time as the lights come on or go off", "Response to light. One investigation detected the light state with approximately 85% accuracy" + _c("pb_pmc_plantsignals")],
      ["A response some minutes after each irrigation, that becomes smaller or larger over the day", "The response of the plant to water. Compare this response with your substrate readings in section 10."],
      ["A fast deflection, then the signal goes back to the baseline slowly, after you touch or move the plant", "A variation potential. It is the usual signal of a wound or stress."],
      ["A slow drift over some days, in one direction, with no change in the grow", "Usually electrode drift. Needles drift less than gel cups after the first day."],
      ["50/60 Hz noise that is larger than all the other signals", "Mains pickup. Make the leads shorter, use shielded cable, and examine the soil electrode."],
      ["Electrode Fault is on", "A lead is off, an electrode has no contact, or the offset is too large for gain 10. Examine the electrodes."],
    ], cls="compact"),
  ]})

SECTIONS.append({"id": "model", "kicker": "10 · Make your own water-status number", "title": "From millivolts to a water-status estimate",
  "blocks": [
    p("A commercial unit changes the signal into a water status with a trained model. The model "
      "learns which features of the signal occur with each plant condition" + _c("pb_najdenovska_stress") +
      ". You can do the same at a small scale. You need the biosignal and a <strong>label</strong>: "
      "a measured value that you want the model to estimate. A substrate moisture sensor in the "
      "same pot or slab is a good label, because it gives a number all the time."),
    steps([
      ("Record for 3 to 4 weeks", "Put the sensor on a plant that has a substrate moisture sensor "
       "near its roots. Keep the Home Assistant recorder (or InfluxDB) on for the biosignal, the "
       "substrate moisture, the light and the irrigation events. Do not move the electrodes in this "
       "period."),
      ("Export the data", "In the Home Assistant History panel, select each entity and download "
       "the data as CSV. You get one file for each entity, with the columns "
       "<code>entity_id</code>, <code>state</code> and <code>last_changed</code>."),
      ("Calculate features in windows", "Cut the biosignal into 10-minute windows. For each window, "
       "calculate the spread, the slope, the range and the mean minus the median of the last 24 "
       "hours. Do not use the raw mean, because the electrode offset is in it."),
      ("Train and test", "Train a simple model to estimate the substrate moisture from the "
       "features. Test it on full days that the model did not see. Compare the error with a model "
       "that always gives the average value. If your model is not better, the signal does not "
       "carry the water information on your plant and your electrodes."),
      ("Use it as an advisory only", "If the model is better, show its estimate in Home Assistant "
       "next to the substrate sensor. Do not let it control irrigation until it agrees with the "
       "substrate sensor for a full crop cycle."),
    ]),
    code(
"""import numpy as np, pandas as pd
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
print("average-only error, % VWC:", round(np.abs(d["vwc"] - d["vwc"].mean()).mean(), 2))"""),
    callout("warn", "A good score on one plant is not a general model",
      p("The model learns your plant, your electrodes and your substrate. When you move the "
        "electrodes or change the cultivar, train it again. The commercial models use data from "
        "many plants and many grows. Your first model uses data from one plant.")),
  ]})

SECTIONS.append({"id": "limits", "kicker": "11 · Limits and calibration", "title": "Limits, calibration and safety",
  "blocks": [
    callout("key", "Limits to know before you solder",
      ul(["<strong>Relative values, not absolute values.</strong> The values are good for trends "
          "and events on one plant. They are not good to compare plants or to read a calibrated "
          "number.",
          "<strong>Electrode drift.</strong> A DC-coupled sensor also records the slow drift of the "
          "electrodes. Use needles, let them become stable, and use the detrended entity or the "
          "24-hour median in the model.",
          "<strong>The noise floor is higher than in commercial units.</strong> The items that give "
          "the largest decrease in noise are a battery supply, short shielded leads and a small "
          "enclosure.",
          "<strong>ESPHome is for trends.</strong> To record spikes of less than one second, add an "
          "AD8232 module as a second channel on A2, and install an Arduino sketch that samples it "
          "at 400 Hz. The investigation of plant signals used this rate" + _c("pb_arxiv_esp32") +
          ". Use the AD8232 channel for fast events and the AD623 channel for the trend."])),
    callout("danger", "Keep the sensor isolated",
      p("Keep the sensor at a low voltage. Supply it with a battery or with USB. Do not connect the "
        "plant electrodes to an item that has a connection to the mains. Use one common ground "
        "only. Thus there is no ground loop through the plant.")),
  ]})
