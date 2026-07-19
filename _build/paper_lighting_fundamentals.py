# -*- coding: utf-8 -*-
"""Paper: lighting fundamentals for cannabis (spectrum, PPFD, DLI) (beginner)."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        stagecard, grid, card, chip, kv, steps)
import figs_lib as L

SLUG = "lighting-fundamentals"
TITLE = "Lighting: spectrum, PPFD and DLI"
EYEBROW = "Beginner · Light"
SUB = ("A from-zero guide to how grow light actually works: what to measure, what to aim for "
       "at each stage, and how to avoid cooking your plants.")
META = [("sun", "Beginner"), ("image", "9 diagrams"),
        ("quote", "Evidence-linked · 9 sources"), ("clock", "~14 min read")]
RELATED = ["light-acclimation", "cloning", "flowering-stages"]
REF_IDS = ["rodriguez-morrison-2021-light-levels-yield-photosynthesis",
           "llewellyn-2022-light-intensity-proportional-uv-no-effect",
           "magagnini-2018-light-spectrum-morphology-cannabinoids",
           "kusuma-2021-nir-leds-delay-flowering-phytochrome",
           "eichhorn-bilodeau-2019-photobiology-cannabis-review",
           "nelson-bugbee-2014-efficacy-led-vs-hps",
           "westmoreland-2021-blue-fraction-efficacy-cannabis",
           "chandra-2008-photosynthetic-response-ppfd-co2-temp",
           "kotiranta-2024-high-light-specialized-metabolites-cannabis"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

SECTIONS.append({"id": "intro", "kicker": "01 · Start here", "title": "What this is (and why light is the engine)",
  "blocks": [
    lead("Light is not just &lsquo;on or off.&rsquo; It is the raw fuel a plant turns into sugar, "
         "and the single biggest lever on yield and quality you control indoors. This paper assumes "
         "you know nothing: it defines every term, gives concrete numbers to aim for at each growth "
         "stage, and explains the one switch that makes a plant flower."),
    p("Plants eat light. Photosynthesis converts light energy plus CO2 and water into sugar, so more "
      "usable light, up to a limit, means more growth" + _c("chandra-2008-photosynthetic-response-ppfd-co2-temp") +
      ". The three numbers that matter most are PPFD (how bright, right now), DLI (how much total "
      "light per day), and spectrum (the color mix). Every term is defined the first time it appears."),
    figure(L.flow("From light to growth",
            [("Light + CO2 + water", "photons hit the leaf"), ("Photosynthesis", "energy captured in the leaf"),
             ("Sugars", "the plant's food"), ("Growth + buds", "leaves, stems, flower")],
            note="If CO2, water or nutrients run short, extra light stops helping. Light is one input among several."), 1,
      "Light is the input, but it only pays off when CO2, water and nutrients keep pace."),
    callout("note", "This pairs with the acclimation paper",
      p("Read this one for the targets. Read the "
        "<a href='light-acclimation.html'>light acclimation</a> paper for how to ramp up to them "
        "safely, so young plants adapt instead of bleaching.")),
  ]})

SECTIONS.append({"id": "key-terms", "kicker": "02 · The vocabulary", "title": "PAR, PPFD, DLI and umol/J in plain English",
  "blocks": [
    p("Get the gist of these five terms and the rest of the paper falls into place. They all describe "
      "the same thing from different angles: how much usable light a plant is getting."),
    defterm("PAR (Photosynthetically Active Radiation)", "The slice of light from 400 to 700 nm that "
            "plants can use for photosynthesis" + _c("eichhorn-bilodeau-2019-photobiology-cannabis-review") +
            ". Lumens and watts do not measure this, which is why a bright-looking bulb can be useless for plants."),
    defterm("PPFD (Photosynthetic Photon Flux Density)", "How many usable photons land on one square "
            "meter each second, in micromoles (umol/m2/s). This is &lsquo;how bright&rsquo; at the "
            "canopy. Measure it with a quantum/PAR meter, not a phone lux app."),
    defterm("DLI (Daily Light Integral)", "The total photons delivered over a whole day, in moles per "
            "square meter (mol/m2/day). This is the number that actually drives yield. "
            "DLI = PPFD x seconds of light per day / 1,000,000" + _c("rodriguez-morrison-2021-light-levels-yield-photosynthesis") + "."),
    defterm("Efficacy (umol/J)", "How many usable photons a fixture makes per joule of electricity. "
            "This is the headline efficiency number when shopping: higher means more light per dollar of power."),
    defterm("Photoperiod", "Hours of light per 24 hours. &lsquo;18/6&rsquo; means 18 on, 6 off."),
    figure(L.bars("Same daily dose, different bright/hours mix",
            [("200x18h", 13.0), ("400x18h", 25.9), ("600x12h", 25.9), ("800x12h", 34.6), ("900x12h", 38.9)],
            unit=" mol", note="DLI in mol/m2/day. 400 PPFD over 18h gives the same dose as 600 PPFD over 12h.",
            maxv=46), 2,
      "Worked DLI examples: a lower PPFD over more hours can match a higher PPFD over fewer hours. "
      "The daily total is what counts." + _c("rodriguez-morrison-2021-light-levels-yield-photosynthesis")),
    figure(L.zones("Where PAR sits on the spectrum", 280, 750,
            [(280, 400, L.PURL, "UV"), (400, 500, L.BLUL, "Blue"), (500, 600, L.GL, "Green"),
             (600, 700, L.REDL, "Red"), (700, 750, L.AMBL, "Far-red")], unit=" nm",
            note="PAR is the 400-700 nm window. Lumens/lux instead peak near green (~555 nm), which is why they mislead."), 3,
      "PAR is the 400 to 700 nm band plants use. Lux meters weight toward green, so they are the wrong "
      "tool for plant light." + _c("eichhorn-bilodeau-2019-photobiology-cannabis-review")),
  ]})

SECTIONS.append({"id": "spectrum", "kicker": "03 · Core concept 1", "title": "Spectrum: what each color does",
  "blocks": [
    p("Blue light, roughly 400 to 500 nm, keeps plants compact with tight internode spacing and is "
      "linked to denser growth and resin in flower" + _c("magagnini-2018-light-spectrum-morphology-cannabinoids") +
      ". Red light, 600 to 700 nm, is the most photosynthetically efficient band and drives flowering "
      "and stretch" + _c("westmoreland-2021-blue-fraction-efficacy-cannabis") + "."),
    p("&lsquo;Full-spectrum white&rsquo; LEDs are rated by color temperature in Kelvin. Higher-K and "
      "bluer (around 4000 to 6500K) leans veg, lower-K and redder (around 3000 to 3500K) leans flower. "
      "A good broad white spectrum works fine across both stages for beginners. The practical "
      "takeaway: do not over-optimize spectrum early. Intensity matters far more for yield than "
      "chasing a perfect color recipe."),
    table(["Band (nm)", "Name", "Main effect", "When it matters"], [
      ["280-400", "UV", "Stress response, possible resin; safety hazard", "Optional, end of flower"],
      ["400-500", "Blue", "Compact growth, tight internodes, thicker leaves", "Veg"],
      ["500-600", "Green", "Penetrates deeper into the canopy than expected", "Minor lever, all stages"],
      ["600-700", "Red", "Highest photosynthetic efficiency, is highly photosynthetic (stretch is more about low blue and far-red; flowering is photoperiod)", "Flower"],
      ["700-750", "Far-red", "Speeds the dark response, adds stem stretch", "Fine-tuning only"],
    ], caption="What each part of the spectrum does. Green is not wasted: it reaches lower leaves, but it is a minor lever."),
    callout("tip", "Beginner rule on spectrum",
      p("A quality full-spectrum white LED covers veg and flower. Intensity beats spectrum tuning, so "
        "spend your attention on PPFD and DLI before you chase color recipes.")),
  ]})

SECTIONS.append({"id": "intensity-dli", "kicker": "04 · Core concept 2", "title": "Intensity and the daily dose: targets by stage",
  "blocks": [
    p("Young tissue cannot process intense light, so targets climb as the plant matures. "
      "Clones and seedlings want about 100-250 PPFD (DLI roughly ~6-16 mol)" + _c("rodriguez-morrison-2021-light-levels-yield-photosynthesis") +
      ", early-to-late veg about 300-600 PPFD (DLI ~20-35 mol), and flower about 700-900 PPFD without "
      "added CO2 (DLI ~30-45 mol)" + _c("llewellyn-2022-light-intensity-proportional-uv-no-effect") + "."),
    p("Pushing past about 900 PPFD only pays off if you also raise CO2 to 1000-1200 ppm and tighten "
      "temperature and humidity" + _c("chandra-2008-photosynthetic-response-ppfd-co2-temp") +
      ". Otherwise extra light just causes stress and bleaching. Because DLI bundles intensity and "
      "hours together, you can hit the same daily dose with lower PPFD over more hours (veg at 18/6) "
      "or higher PPFD over fewer hours (flower at 12/12)."),
    figure(L.zones("Flowering PPFD: where useful ends and risk begins", 0, 1500,
            [(700, 900, L.GL, "no-CO2 sweet spot"), (900, 1000, L.AMBL, "marginal"),
             (1000, 1400, L.REDL, "CO2 + climate only")], unit="",
            note="Above ~900 PPFD without CO2 and tight climate control, you buy stress and heat, not yield."), 4,
      "Flower intensity zones. Most rooms top out around 700-900 PPFD. The 1000-1400 band needs CO2 "
      "and serious climate control." + _c("kotiranta-2024-high-light-specialized-metabolites-cannabis")),
    figure(L.line("Yield response to DLI: rising, then flat, then stressed",
            [(0, 5), (1, 22), (2, 40), (3, 55), (4, 64), (5, 67), (6, 60)],
            ["5", "15", "25", "35", "45", "55", "65"],
            ylab="relative growth", ymin=0, ymax=80,
            note="DLI (mol/m2/day) on the x-axis. Returns rise, flatten at saturation, then bend down into stress. CO2 shifts the flat point right."), 5,
      "Growth rises with DLI, levels off at light saturation, then falls as stress and bleaching set "
      "in. Adding CO2 moves the saturation point to the right." + _c("chandra-2008-photosynthetic-response-ppfd-co2-temp")),
    table(["Stage", "PPFD (umol/m2/s)", "DLI (mol/m2/day)", "Photoperiod"], [
      ["Clone / seedling", "100-250", "~6-16", "18/6"],
      ["Early veg", "300-450", "~20-29", "18/6"],
      ["Late veg", "450-600", "~29-39", "18/6"],
      ["Flower (no CO2)", "700-900", "~30-39", "12/12"],
      ["Flower (CO2 1000-1200 ppm)", "1000-1400", "~40-60", "12/12"],
    ], cls="compact", caption="Stage targets. 600 PPFD x 18h (~39 mol) is closer to ~900 PPFD x 12h than to 800 PPFD x 12h."),
  ]})

SECTIONS.append({"id": "photoperiod-flip", "kicker": "05 · Core concept 3", "title": "The photoperiod flip that triggers flowering",
  "blocks": [
    p("Photoperiod-type cannabis stays vegetative under long days (commonly 18/6) and is forced to "
      "flower by switching to 12 hours light and 12 hours uninterrupted dark" + _c("kusuma-2021-nir-leds-delay-flowering-phytochrome") +
      ". This is &lsquo;the flip.&rsquo;"),
    p("The plant does not count light hours. It measures the length of the unbroken dark period using "
      "a pigment called phytochrome, which flips between an active form (Pfr) and an inactive form "
      "(Pr). Once nights are long enough it produces a flowering signal, florigen, in the leaves" + _c("eichhorn-bilodeau-2019-photobiology-cannabis-review") +
      ". This is why light leaks matter so much: even a phone screen, an indicator LED, or a pinhole "
      "in a tent during lights-off can reset phytochrome and stall or revert flowering, cause "
      "re-vegging, or trigger hermaphrodites" + _c("kusuma-2021-nir-leds-delay-flowering-phytochrome") + "."),
    figure(L.flow("How the dark period triggers flowering",
            [("Lights on", "Pr converts to active Pfr: 'it is day'"),
             ("Lights off", "Pfr slowly reverts to Pr"),
             ("Long enough night", "florigen signal made in leaves"),
             ("Flip", "growing tips switch to bud production")],
            note="A red or far-red light leak re-converts Pr back to Pfr and breaks the cycle, so the plant 'thinks' it is still day."), 6,
      "Phytochrome tracks the dark period. A light leak during lights-off resets the clock and stalls "
      "the flip." + _c("kusuma-2021-nir-leds-delay-flowering-phytochrome")),
    callout("danger", "Seal your dark period",
      p("Light leaks during the dark period are the number one beginner flowering failure: stalled "
        "bloom, re-veg, or hermaphrodites. Far-red and red are exactly what phytochrome senses. Seal "
        "pinholes, cover indicator LEDs, use light-proof ducting. If you can see in the dark, so can the plant.")),
  ]})

SECTIONS.append({"id": "fixtures", "kicker": "06 · The hardware", "title": "LED vs HPS vs CMH, and reading efficacy",
  "blocks": [
    p("Modern LED is the efficiency leader at roughly 2.7-3.0 umol/J for good fixtures (budget units "
      "2.0-2.3), runs cooler, and lasts longer" + _c("nelson-bugbee-2014-efficacy-led-vs-hps") +
      ". HPS (high-pressure sodium) sits around 1.7-1.9 umol/J and runs hot but is cheap to buy. "
      "CMH/LEC (ceramic metal halide) lands lower, around 1.3-1.9 umol/J, but has a pleasant broad spectrum."),
    p("Efficacy (umol/J) is the number to compare. A 3.0 umol/J LED makes about 60% more usable light "
      "than a ~1.85 umol/J double-ended HPS for the same power bill" + _c("nelson-bugbee-2014-efficacy-led-vs-hps") +
      ". For beginners, a reputable full-spectrum LED with a published PPFD map and efficacy at or "
      "above ~2.5 umol/J is the safe default. Ignore inflated &lsquo;equivalent watt&rsquo; marketing "
      "and look at actual PPF (total umol/s) and coverage."),
    figure(L.bars("Fixture efficacy (umol/J)",
            [("Budget LED", 2.1), ("Good LED", 2.85), ("HPS DE", 1.85), ("HPS SE", 1.7), ("CMH", 1.5)],
            unit="", target=2.5, note="Higher is more light per watt. The target line marks a sensible 'good buy' threshold.",
            maxv=3.4), 7,
      "Efficacy by fixture type. Good LED clears the ~2.5 umol/J threshold comfortably; HPS and CMH "
      "fall short." + _c("nelson-bugbee-2014-efficacy-led-vs-hps")),
    table(["Type", "Efficacy (umol/J)", "Heat", "Upfront cost", "Best for"], [
      ["LED", "2.0-3.0", "Low", "Higher", "Default choice, all stages"],
      ["HPS", "1.7-1.9", "High", "Low", "Budget builds, red-heavy flower"],
      ["CMH / LEC", "1.3-1.9", "Medium", "Medium", "Broad natural spectrum incl. some UV"],
    ], cls="compact", caption="Compare on efficacy and total PPF plus a real PPFD map, never on lumens or 'equivalent watts.'"),
  ]})

SECTIONS.append({"id": "setup-by-stage", "kicker": "07 · Do this", "title": "Hanging height, coverage, and a stage-by-stage setup",
  "blocks": [
    p("Intensity falls with distance, but inverse-square (quarter at 2&times; distance) is a point-source ideal for LEDs. Use a PPFD map and meter. About hang height:  Height is your coarse intensity dial, the dimmer is the fine dial. Hang about 24 in "
      "for seedlings and clones, ~18 in for veg, and ~12-16 in for flower, then fine-tune with the "
      "dimmer and a PAR meter."),
    p("Verify coverage by taking PPFD readings at nine points: four corners, four edge-midpoints, and "
      "the center. Aim for a min-to-average ratio above 0.75 so edge plants are not starved while the "
      "center bleaches. Hanging higher trades peak intensity for more even spread, so use a "
      "manufacturer PPFD map as your starting point and confirm with real readings at canopy height."),
    figure(L.bars("A 9-point PPFD grid (example, umol/m2/s)",
            [("Corner", 560), ("Edge", 640), ("Center", 760), ("Edge", 650), ("Corner", 590)],
            unit="", note="Average ~640, lowest corner 560: min/avg = 0.875, above the 0.75 floor. A reading under ~480 here would flag a weak corner.",
            maxv=900), 8,
      "Sample of a 9-point grid. Compare the lowest reading to the average: a min-to-average ratio "
      "above 0.75 is acceptable uniformity."),
    table(["Stage", "Hang height", "Target PPFD", "Photoperiod"], [
      ["Clone / seedling", "~24 in", "100-300", "18/6"],
      ["Veg", "~18 in", "300-600", "18/6"],
      ["Flower", "~12-16 in", "700-900", "12/12"],
    ], cls="compact", caption="Starting heights. Always confirm against your fixture's PPFD map and a meter at canopy height."),
    callout("tip", "Ramp, do not slam",
      p("Pair this with the <a href='light-acclimation.html'>light acclimation</a> paper: raise the "
        "dimmer or lower the fixture over several days rather than jumping a fresh clone to full intensity.")),
  ]})

SECTIONS.append({"id": "pitfalls", "kicker": "08 · When it goes wrong", "title": "Light stress, far-red and UV, and common mistakes",
  "blocks": [
    p("Too much light shows as bleaching (white or yellow bud tips directly under the fixture), "
      "upward-cupping or &lsquo;taco&rsquo; leaves, and faded color even when nutrients are fine. The "
      "fix is to dim or raise the light, not to feed more."),
    p("Far-red (~730 nm) can speed the transition to dark via the phytochrome system and slightly "
      "stretch plants" + _c("kusuma-2021-nir-leds-delay-flowering-phytochrome") +
      ". UV-B in the final 1-2 weeks is a popular potency play, but the evidence that UV-B reliably "
      "raises cannabinoids or yield is mixed" + _c("llewellyn-2022-light-intensity-proportional-uv-no-effect") +
      ", and it carries real eye, skin and plant-stress risks. Treat it as optional and advanced."),
    table(["Symptom", "Likely cause", "What to do"], [
      ["Bleached / white tops under the fixture", "Too much PPFD", "Raise or dim the light, do not feed"],
      ["Taco / upward-cupping leaves", "Light plus heat stress", "Raise the light, check leaf-surface temp"],
      ["Stretchy, pale growth", "Too little light or hung too far", "Lower the fixture or boost intensity"],
      ["Stalled flowering, re-veg", "Light leak during the dark period", "Seal the room light-tight"],
      ["Scorched tops, PPFD looks fine", "Radiant heat (esp. HPS)", "Raise the fixture, watch leaf temp"],
    ], cls="compact", caption="The biggest avoidable errors: jumping a clone to flower-level PPFD, trusting lux/wattage over a PAR meter, and ignoring light leaks."),
  ]})

SECTIONS.append({"id": "expectations", "kicker": "09 · Reality check", "title": "Realistic expectations",
  "blocks": [
    p("More light only helps up to the point where something else (CO2, water, nutrients, temperature "
      "or genetics) becomes the limiting factor. Past saturation you pay for electricity and heat with "
      "no extra yield, and eventually with stress" + _c("rodriguez-morrison-2021-light-levels-yield-photosynthesis") + "."),
    figure(L.bars("Yield is capped by the shortest input",
            [("Light", 90), ("CO2", 45), ("Water", 80), ("Nutrients", 70), ("Temp", 60), ("Genetics", 75)],
            unit="", target=45, note="Yield is held to the level of the lowest stave. Here CO2 is the bottleneck, so adding more light is wasted.",
            maxv=100), 9,
      "The limiting-factor idea: pushing light far above the other inputs wastes effort. Lift the "
      "shortest stave first." + _c("chandra-2008-photosynthetic-response-ppfd-co2-temp")),
    callout("key", "What to actually do",
      ol(["<strong>Without CO2, ~700-900 PPFD / ~35-45 mol DLI in flower is a sensible ceiling.</strong> The 1000-1400 PPFD regime needs CO2, cooling and humidity control: a whole-room commitment, not just a brighter light.",
          "<strong>Nail intensity, dose and photoperiod first.</strong> Spectrum tweaks like far-red and UV are fine-tuning, not the main lever.",
          "<strong>Buy on efficacy and a real PPFD map.</strong> Hit the stage targets, seal your dark period, and lighting stops being your bottleneck."])),
    p("Once lighting is handled, the rest is climate, feed and genetics. Read the "
      "<a href='light-acclimation.html'>light acclimation</a> paper for how to ramp safely, and the "
      "<a href='flowering-stages.html'>flowering stages</a> paper for what happens after the flip."),
  ]})
