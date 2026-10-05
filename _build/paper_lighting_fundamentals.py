# -*- coding: utf-8 -*-
"""Paper: lighting fundamentals for cannabis (spectrum, PPFD, DLI) (beginner)."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        stagecard, grid, card, chip, kv, steps)
import figs_lib as L

SLUG = "lighting-fundamentals"
TITLE = "Lighting: spectrum, PPFD and DLI"
EYEBROW = "Basic · Light"
SUB = ("This paper gives basic information about how a grow light operates. It gives the "
       "definitions of the primary numbers and the targets for each stage. It also shows how to "
       "find problems before they cause very bad damage to a crop.")
META = [("sun", "Basic"), ("image", "9 diagrams"),
        ("quote", "9 sources"), ("clock", "~14 min to read")]
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

SECTIONS.append({"id": "intro", "kicker": "01 · Start here", "title": "Purpose and scope",
  "blocks": [
    lead("Light is the energy that a plant changes into sugar. Light is the parameter with the "
         "largest effect that you control in a grow room. This paper starts with the basic "
         "information. It gives the definition of each term and targets with numbers for each "
         "stage. It also gives information about the change of the light cycle that causes "
         "flowering."),
    p("The plant absorbs energy from light. The plant uses this energy to make sugar from CO2 in "
      "the air and water from the roots. This production of sugar is photosynthesis. Thus when the "
      "quantity of light that the plant can use increases, growth increases until CO2, water or "
      "temperature becomes the limiting factor." +
      _c("chandra-2008-photosynthetic-response-ppfd-co2-temp") + " The three primary numbers are "
      "PPFD (how bright the light is at this time), DLI (the total quantity of light each day) and "
      "spectrum (the colors in the light). This paper gives the definition of each term the first "
      "time that it occurs."),
    figure(L.flow("From light to growth",
            [("Light, CO2 and water", "photons hit the leaf"), ("Photosynthesis", "energy absorbed in the leaf"),
             ("Sugars", "food for plants"), ("Growth and buds", "leaves, stems, flower")],
            note="If CO2, water or nutrients are not sufficient, more light does not help. Light is only one input."), 1,
      "Light is an input, but more light gives a good result only when CO2, water and nutrients are sufficient."),
    callout("note", "The acclimation paper gives more information",
      p("This paper gives the targets. The <a href='light-acclimation.html'>light acclimation</a> "
        "paper shows how to increase the light slowly to these targets. Thus the new plants "
        "acclimate, and bleaching does not occur.")),
  ]})

SECTIONS.append({"id": "key-terms", "kicker": "02 · The terms", "title": "Definitions",
  "blocks": [
    p("When you know the basic information about these five terms, the other parts of this paper "
      "are easy. All five terms are about the same item: the quantity of light that a plant can use."),
    defterm("PAR (Photosynthetically Active Radiation)", "The part of the light from 400 to 700 nm "
            "that plants can use for photosynthesis." +
            _c("eichhorn-bilodeau-2019-photobiology-cannabis-review") + " Lumens and watts do not "
            "measure this part. Thus a lamp that looks bright can give no light that plants can use."),
    defterm("PPFD (Photosynthetic Photon Flux Density)", "The quantity of photons in the PAR range "
            "that a surface of one square meter receives each second, in micromoles (umol/m2/s). "
            "This value shows how bright the light is at the canopy. Measure it with a quantum "
            "meter or a PAR meter. Do not use a lux app on a phone."),
    defterm("DLI (Daily Light Integral)", "The total quantity of photons that a surface receives in "
            "one day, in moles for each square meter (mol/m2/day). This number has the primary "
            "effect on the yield. DLI = PPFD x seconds of light each day / 1,000,000." +
            _c("rodriguez-morrison-2021-light-levels-yield-photosynthesis")),
    defterm("Efficacy (umol/J)", "The quantity of photons in the PAR range that a fixture makes for "
            "each joule of electricity. This number is the primary value of efficiency when you "
            "select a fixture. A higher value gives more light for the same cost of electricity."),
    defterm("Photoperiod", "The number of hours of light in 24 hours. The value 18/6 is 18 hours of light and 6 hours of darkness."),
    figure(L.bars("Same dose each day, different PPFD and hours",
            [("200x18h", 13.0), ("400x18h", 25.9), ("600x12h", 25.9), ("800x12h", 34.6), ("900x12h", 38.9)],
            unit=" mol", note="DLI in mol/m2/day. 400 PPFD for 18 hours gives the same dose as 600 PPFD for 12 hours.",
            maxv=46), 2,
      "Examples of how to calculate the DLI. A lower PPFD for more hours can give the same DLI as a "
      "higher PPFD for a smaller number of hours. The total for each day is the primary value." +
      _c("rodriguez-morrison-2021-light-levels-yield-photosynthesis")),
    figure(L.zones("Where PAR is in the spectrum", 280, 750,
            [(280, 400, L.PURL, "UV"), (400, 500, L.BLUL, "Blue"), (500, 600, L.GL, "Green"),
             (600, 700, L.REDL, "Red"), (700, 750, L.AMBL, "Far-red")], unit=" nm",
            note="PAR: 400 to 700 nm. Lumens and lux have the peak at green (approximately 555 nm). Thus they are incorrect for plants."), 3,
      "PAR is the range from 400 to 700 nm that plants use. A lux meter gives a larger value to "
      "green light than to other colors. Thus it is the incorrect tool for plant light." +
      _c("eichhorn-bilodeau-2019-photobiology-cannabis-review")),
  ]})

SECTIONS.append({"id": "spectrum", "kicker": "03 · Primary information 1", "title": "Effect of each wavelength on the plant",
  "blocks": [
    p("Blue light, approximately 400 to 500 nm, keeps plants compact with short internodes. Growth "
      "with higher density and more resin in flower also has a relation to blue light." +
      _c("magagnini-2018-light-spectrum-morphology-cannabinoids") + " Red light, 600 to 700 nm, is "
      "the range with the highest efficiency for photosynthesis. It causes flowering and stretch." +
      _c("westmoreland-2021-blue-fraction-efficacy-cannabis")),
    p("&lsquo;Full-spectrum white&rsquo; LEDs have a color temperature in Kelvin. A higher "
      "temperature in K and light with more blue (approximately 4000 to 6500K) is better for the "
      "vegetative stage. A lower temperature in K and light with more red (approximately 3000 to "
      "3500K) is better for the flowering stage. A good white spectrum with a wide range is "
      "satisfactory for the two stages for a new grower. Do not try to find the best spectrum at "
      "the start. Intensity has a much larger effect on yield than the selection of the best colors."),
    table(["Range (nm)", "Name", "Primary effect", "When it is important"], [
      ["280 to 400", "UV", "Stress response and possible resin. Hazard to safety.", "Optional, at the end of the flowering stage"],
      ["400 to 500", "Blue", "Compact growth, short internodes, thicker leaves", "Vegetative stage"],
      ["500 to 600", "Green", "Goes deeper into the canopy than many growers think", "Small effect, all stages"],
      ["600 to 700", "Red", "Highest efficiency for photosynthesis. A low quantity of blue light and far-red light cause more stretch. The photoperiod causes flowering.", "Flowering stage"],
      ["700 to 750", "Far-red", "Makes the dark response faster. Adds stem stretch.", "Only for small adjustments"],
    ], caption="The effect of each part of the spectrum. Plants also use green light. It goes to the bottom leaves, but it has a small effect."),
    callout("tip", "Basic selection of the spectrum",
      p("A full-spectrum white LED of good quality is satisfactory for the vegetative stage and the "
        "flowering stage. Intensity has a larger effect than the adjustment of the spectrum. Thus "
        "control the PPFD and the DLI before you adjust the colors.")),
  ]})

SECTIONS.append({"id": "intensity-dli", "kicker": "04 · Primary information 2", "title": "PPFD and DLI targets at each growth stage",
  "blocks": [
    p("New tissue cannot use light of high intensity. Thus the targets increase when the plant is "
      "in a subsequent stage. The target for clones and seedlings is approximately 100 to 250 PPFD "
      "(DLI approximately 6 to 16 mol)." +
      _c("rodriguez-morrison-2021-light-levels-yield-photosynthesis") + " The target for the "
      "vegetative stage, from the first part to the last part, is approximately 300 to 600 PPFD "
      "(DLI approximately 20 to 35 mol). The target for the flowering stage without added CO2 is "
      "approximately 700 to 900 PPFD (DLI approximately 30 to 45 mol)." +
      _c("llewellyn-2022-light-intensity-proportional-uv-no-effect")),
    p("A PPFD of more than approximately 900 gives a good result only if you also increase the CO2 "
      "to 1000 to 1200 ppm. You must also control the temperature and the humidity more accurately." +
      _c("chandra-2008-photosynthetic-response-ppfd-co2-temp") + " If you do not do this, more "
      "light causes only stress and bleaching. The DLI includes the intensity and the hours "
      "together. Thus you can get the same dose each day with a lower PPFD for more hours "
      "(vegetative stage at 18/6). You can also use a higher PPFD for a smaller number of hours "
      "(flowering stage at 12/12)."),
    figure(L.zones("Flowering PPFD: where good results stop and risk starts", 0, 1500,
            [(700, 900, L.GL, "best range, no CO2"), (900, 1000, L.AMBL, "limit"),
             (1000, 1400, L.REDL, "CO2 and climate only")], unit="",
            note="More than approximately 900 PPFD without CO2 and accurate climate control gives stress and heat, not yield."), 4,
      "Intensity zones for flowering. The maximum in most rooms is approximately 700 to 900 PPFD. "
      "In the range of 1000 to 1400, CO2 and accurate climate control are necessary." +
      _c("kotiranta-2024-high-light-specialized-metabolites-cannabis")),
    figure(L.line("Yield and DLI: increase, then flat, then stress",
            [(0, 5), (1, 22), (2, 40), (3, 55), (4, 64), (5, 67), (6, 60)],
            ["5", "15", "25", "35", "45", "55", "65"],
            ylab="relative growth", ymin=0, ymax=80,
            note="x-axis: DLI (mol/m2/day). The result increases, is flat at saturation, then decreases. CO2 moves the flat point to the right."), 5,
      "Growth increases when the DLI increases. At light saturation, the growth becomes flat. Then "
      "growth decreases when stress and bleaching start. When you add CO2, the saturation point "
      "moves to the right." + _c("chandra-2008-photosynthetic-response-ppfd-co2-temp")),
    table(["Stage", "PPFD (umol/m2/s)", "DLI (mol/m2/day)", "Photoperiod"], [
      ["Clone / seedling", "100 to 250", "approximately 6 to 16", "18/6"],
      ["Vegetative stage, first part", "300 to 450", "approximately 20 to 29", "18/6"],
      ["Vegetative stage, last part", "450 to 600", "approximately 29 to 39", "18/6"],
      ["Flowering stage (no CO2)", "700 to 900", "approximately 30 to 39", "12/12"],
      ["Flowering stage (CO2 1000 to 1200 ppm)", "1000 to 1400", "approximately 40 to 60", "12/12"],
    ], cls="compact", caption="Targets for each stage. 600 PPFD for 18 hours (approximately 39 mol) is almost the same as approximately 900 PPFD for 12 hours. It is different from 800 PPFD for 12 hours."),
  ]})

SECTIONS.append({"id": "photoperiod-flip", "kicker": "05 · Primary information 3", "title": "How the length of the day causes flowering",
  "blocks": [
    p("Photoperiod cannabis stays in the vegetative stage in long days (usually 18/6). Flowering "
      "starts when you change the light cycle to 12 hours of light and 12 hours of continuous "
      "darkness." + _c("kusuma-2021-nir-leds-delay-flowering-phytochrome") + " This change is the "
      "start of the flowering stage."),
    p("The plant measures the darkness, not the hours of light. The plant counts only the hours "
      "when the lights are off. If light occurs in the middle of the dark period, also for a short "
      "time, the plant starts to count again from zero.</p><p>A pigment in the leaves causes this. "
      "The pigment is phytochrome. Phytochrome is Pr or Pfr. Light changes Pr to Pfr, and darkness "
      "slowly changes Pfr to Pr. The ratio of Pr to Pfr shows the plant the length of the "
      "night.</p><p>When the dark period has sufficient length, phytochrome causes the production "
      "of florigen. Florigen is a hormone that moves in the plant. It moves the signal from the "
      "leaves to the growing tips, to start the production of buds." +
      _c("eichhorn-bilodeau-2019-photobiology-cannabis-review") + "</p><p>A light leak makes the "
      "phytochrome start again in the middle of the cycle. Small lights can cause this: for example "
      "a phone screen, an indicator LED, or a pinhole in a tent when the lights are off. These "
      "lights can stop flowering, or cause the plant to go back to the vegetative stage. They can "
      "also cause hermaphrodites." + _c("kusuma-2021-nir-leds-delay-flowering-phytochrome")),
    figure(L.flow("How the dark period causes flowering",
            [("Lights on", "Pr changes to active Pfr: 'it is day'"),
             ("Lights off", "Pfr slowly changes to Pr"),
             ("Sufficient darkness", "leaves make the florigen signal"),
             ("Start", "growing tips start to make buds")],
            note="A leak of red or far-red light changes Pr back to Pfr and stops the cycle. Thus the plant receives the signal for day."), 6,
      "Phytochrome measures the dark period. A light leak when the lights are off makes the "
      "measurement start again and stops the start of flowering." +
      _c("kusuma-2021-nir-leds-delay-flowering-phytochrome")),
    callout("danger", "Prevent light leaks during the dark period",
      p("Close the pinholes. Put a cover on each indicator LED. Use light-proof ducts. If you can "
        "see light in the dark period, the plant can also receive it.</p><p>Light leaks in the dark "
        "period are the primary flowering problem for new growers. The problems are: flowering "
        "stops, the plant goes back to the vegetative stage, or hermaphrodites occur. Phytochrome "
        "senses far-red light and red light.")),
  ]})

SECTIONS.append({"id": "fixtures", "kicker": "06 · The equipment", "title": "Selection of a fixture: LED, HPS or CMH",
  "blocks": [
    p("An LED has the highest efficiency: approximately 2.7 to 3.0 umol/J for good fixtures (2.0 to "
      "2.3 for budget units). It also operates at a lower temperature and has a longer life." +
      _c("nelson-bugbee-2014-efficacy-led-vs-hps") + " HPS (high-pressure sodium) has approximately "
      "1.7 to 1.9 umol/J. It operates at a high temperature, but its cost is low. CMH/LEC (ceramic "
      "metal halide) has a lower efficacy, approximately 1.3 to 1.9 umol/J, but it has a good broad "
      "spectrum."),
    p("Compare the efficacy (umol/J). For the same cost of electricity, a 3.0 umol/J LED makes "
      "approximately 60% more light for plants than a double-ended HPS of approximately 1.85 umol/J." +
      _c("nelson-bugbee-2014-efficacy-led-vs-hps") + " For new growers, the selection with the "
      "lowest risk is a full-spectrum LED of good quality. It must have a PPFD map from the "
      "manufacturer and an efficacy of approximately 2.5 umol/J or more. Do not use the "
      "&lsquo;equivalent watt&rsquo; values of the supplier, because they are too high. Use the PPF "
      "(total umol/s) and the coverage."),
    figure(L.bars("Fixture efficacy (umol/J)",
            [("Budget LED", 2.1), ("Good LED", 2.85), ("HPS DE", 1.85), ("HPS SE", 1.7), ("CMH", 1.5)],
            unit="", target=2.5, note="A higher value is more light for each watt. The target line is the threshold for a good fixture.",
            maxv=3.4), 7,
      "Efficacy for each type of fixture. A good LED is more than the threshold of approximately "
      "2.5 umol/J by a large quantity. HPS and CMH are less than the threshold." +
      _c("nelson-bugbee-2014-efficacy-led-vs-hps")),
    table(["Type", "Efficacy (umol/J)", "Heat", "Cost at the start", "Best for"], [
      ["LED", "2.0 to 3.0", "Low", "Higher", "Standard selection, all stages"],
      ["HPS", "1.7 to 1.9", "High", "Low", "Systems with a low cost. Flowering stage with more red light."],
      ["CMH / LEC", "1.3 to 1.9", "Moderate", "Moderate", "Broad spectrum, with some UV"],
    ], cls="compact", caption="Compare the efficacy, the total PPF and a measured PPFD map. Do not compare the lumens or the 'equivalent watts.'"),
  ]})

SECTIONS.append({"id": "setup-by-stage", "kicker": "07 · Do this", "title": "Height and intensity for each stage",
  "blocks": [
    p("Intensity decreases when the distance increases. In the inverse-square law, the light is a "
      "quarter at two times the distance. This relation is for a point source. For an LED bar, the "
      "relation gives only an approximate result. Thus measure the PPFD with a meter. Do not use "
      "only the relation.</p><p>The height is the large adjustment of intensity, and the dimmer is "
      "the small adjustment. Hang the fixture at approximately 60 cm (24 in) for seedlings and "
      "clones. Hang it at approximately 45 cm (18 in) for the vegetative stage and at approximately "
      "30 to 40 cm (12 to 16 in) for the flowering stage. Then adjust with the dimmer and a PAR "
      "meter."),
    p("Make sure of the coverage: measure the PPFD at nine points. The points are the four corners, "
      "the four midpoints of the edges, and the center. The target for the ratio of the minimum to "
      "the average is more than 0.75. Thus the plants at the edge get sufficient light, and the "
      "center does not have bleaching. When you hang the fixture higher, the peak intensity "
      "decreases and the light is more equal in the area. Thus use the PPFD map of the manufacturer "
      "as the start point, and make sure with readings at the canopy height."),
    figure(L.bars("A PPFD grid of 9 points (example, umol/m2/s)",
            [("Corner", 560), ("Edge", 640), ("Center", 760), ("Edge", 650), ("Corner", 590)],
            unit="", note="Average approximately 640, lowest corner 560: min/avg = 0.875, more than 0.75. A weak corner is less than approximately 480.",
            maxv=900), 8,
      "An example of a grid of 9 points. Compare the lowest reading with the average. A ratio of "
      "the minimum to the average of more than 0.75 is satisfactory uniformity."),
    table(["Stage", "Height of the fixture", "Target PPFD", "Photoperiod"], [
      ["Clone / seedling", "approximately 60 cm (24 in)", "100 to 300", "18/6"],
      ["Vegetative stage", "approximately 45 cm (18 in)", "300 to 600", "18/6"],
      ["Flowering stage", "approximately 30 to 40 cm (12 to 16 in)", "700 to 900", "12/12"],
    ], cls="compact", caption="Start heights. Always make sure with the PPFD map of your fixture and a meter at the canopy height."),
    callout("tip", "Increase the light in steps",
      p("Use the <a href='light-acclimation.html'>light acclimation</a> paper with this paper. "
        "Increase the dimmer setting or lower the fixture in small steps during some days. Do not "
        "change a new clone immediately to the full intensity.")),
  ]})

SECTIONS.append({"id": "pitfalls", "kicker": "08 · When a problem occurs", "title": "Frequent problems with light",
  "blocks": [
    p("Too much light shows these symptoms: bleaching (white or yellow bud tips directly below the "
      "fixture), &lsquo;taco&rsquo; leaves (the edges are up), and faded color. The symptoms occur "
      "also when the nutrients are correct. To correct the problem, decrease the intensity of the "
      "light or increase the height of the fixture. Do not apply more feed."),
    p("Far-red light (approximately 730 nm) can make the change to darkness faster with the "
      "phytochrome system. It can also cause a small quantity of stretch in the plants." +
      _c("kusuma-2021-nir-leds-delay-flowering-phytochrome") + " Many growers use UV-B in the last "
      "1 to 2 weeks to increase potency. But the data do not show that UV-B always increases "
      "cannabinoids or yield." + _c("llewellyn-2022-light-intensity-proportional-uv-no-effect") +
      " UV-B also has risks for the eyes, for the skin and for stress in the plant. UV-B is "
      "optional, and it is for advanced growers."),
    table(["Symptom", "Possible cause", "Correction"], [
      ["Bleaching, white tops below the fixture", "Too much PPFD", "Increase the height of the light or decrease its intensity. Do not apply feed."],
      ["&lsquo;Taco&rsquo; leaves (the edges are up)", "Stress from light and heat", "Increase the height of the light. Measure the temperature of the leaf surface."],
      ["Growth with stretch and pale color", "Not sufficient light, or the fixture is too far above the plants", "Lower the fixture or increase the intensity"],
      ["Flowering stops, or the plant goes back to the vegetative stage", "Light leak during the dark period", "Make the room light-tight"],
      ["Tops with heat damage, PPFD is correct", "Radiant heat (mostly from HPS)", "Increase the height of the fixture. Monitor the leaf temperature."],
    ], cls="compact", caption="Prevent the largest errors. Do not increase the PPFD of a clone immediately to the PPFD of the flowering stage. Use a PAR meter. Do not use lux or watts. Do not ignore light leaks."),
  ]})

SECTIONS.append({"id": "expectations", "kicker": "09 · Possible results", "title": "Expected results and limitations",
  "blocks": [
    p("More light helps only until a different item (CO2, water, nutrients, temperature or "
      "genetics) becomes the limiting factor. After saturation, you have the cost of electricity "
      "and heat, but the yield does not increase. Then stress occurs." +
      _c("rodriguez-morrison-2021-light-levels-yield-photosynthesis")),
    figure(L.bars("Yield cannot be more than the lowest input",
            [("Light", 90), ("CO2", 45), ("Water", 80), ("Nutrients", 70), ("Temperature", 60), ("Genetics", 75)],
            unit="", target=45, note="Yield is the same as the lowest bar. Here CO2 is the limiting factor, thus more light does not help.",
            maxv=100), 9,
      "This diagram shows the limiting factor. When the light is much more than the other inputs, "
      "more light gives no result. First, increase the lowest input." +
      _c("chandra-2008-photosynthetic-response-ppfd-co2-temp")),
    callout("key", "Tasks that we recommend",
      ol(["<strong>Without CO2, a maximum of approximately 700 to 900 PPFD, or approximately 35 to 45 mol DLI, is correct in the flowering stage.</strong> In the range of 1000 to 1400 PPFD, CO2, cooling and humidity control are necessary in the full room. A brighter light is not sufficient.",
          "<strong>First, make the intensity, the dose and the photoperiod correct.</strong> Changes in the spectrum, for example far-red and UV, are small adjustments. They are not the primary control.",
          "<strong>Select a fixture for its efficacy and a measured PPFD map.</strong> Use the targets for each stage and prevent light leaks in the dark period. Then the lighting is not a limiting factor."])),
    p("When the lighting is correct, the other items are climate, feed and genetics. The <a "
      "href='light-acclimation.html'>light acclimation</a> paper shows how to increase the light "
      "safely. The <a href='flowering-stages.html'>flowering stages</a> paper gives information "
      "about the changes in the plant after the start of flowering."),
  ]})
