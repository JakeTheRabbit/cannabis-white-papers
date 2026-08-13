# -*- coding: utf-8 -*-
"""Paper: temperature, humidity and VPD — psychrometrics for growers without the textbook."""
import json, os
from components import (p, lead, h, ul, ol, callout, defterm, table, figure, grid, card,
                        chip, kv, steps)
import figs_lib as L

_FIGS = json.load(open(os.path.join(os.path.dirname(__file__), "figs_temp_humidity_vpd.json"),
                       encoding="utf-8"))

SLUG = "temp-humidity-vpd"
TITLE = "Temperature, humidity and VPD: the air the plant feels"
EYEBROW = "Environment · Climate"
SUB = ("VPD is the one climate number the plant actually feels. What it is, the equation in a form "
       "you can use, why leaf temperature — not air — sets the real number, stage bands you can "
       "defend, the night-time dew-point discipline that keeps mould out, and how to measure it "
       "all without lying to yourself.")
META = [("wave", "Climate"), ("image", "12 diagrams"),
        ("quote", "Evidence-linked · 14 sources"), ("clock", "~19 min read")]
RELATED = ["grow-room-systems", "mould-risk", "airflow-design"]
REF_IDS = ["fao56-1998", "grossiord2020-vpd", "nelson2015-leaftemp", "corredor2025-rh",
           "jin2019-cannabis-env", "pulse-vpd-guide", "chandra2008-photo", "inoue2021-vpd",
           "caird2007-night", "moe1995-dif", "punja2025-budrot-epi", "zhang2020-canopy-rh",
           "tarara2007-shield", "hpac-latent"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

# ---------------------------------------------------------------- 01 start here
SECTIONS.append({"id": "start-here", "kicker": "01 · Start here", "title": "The air the plant feels",
  "blocks": [
    lead("Two rooms both read 55% humidity. One is at 20&nbsp;°C and the plants are coasting. The "
         "other is at 28&nbsp;°C and the same cultivar is stalled, leaf edges curling, drinking hard. "
         "Same number on the controller, completely different rooms &mdash; because relative humidity "
         "is a percentage of a moving target, and the plant doesn&rsquo;t feel percentages. It feels "
         "the <strong>pull</strong>: how hard the air is trying to drag water out of its leaves."),
    p("That pull has a name &mdash; <strong>vapour pressure deficit</strong>, VPD &mdash; and it is "
      "the number your temperature and humidity actually combine into. Air holds water vapour up to "
      "a ceiling set by its temperature; VPD is the gap between that ceiling and what&rsquo;s "
      "actually in the air" + _c("fao56-1998") + ". Every leaf transpires into that gap. Small gap, "
      "weak pull. Big gap, hard pull &mdash; until the plant slams its pores shut in self-defence" +
      _c("grossiord2020-vpd") + "."),
    p("This paper is the psychrometrics you need without the textbook: what VPD is, the equation in "
      "a form you can punch into a phone, why <em>leaf</em> temperature is the real number and how "
      "your fixture type skews it, stage bands and where they come from, the day/night strategy, the "
      "dew-point discipline that keeps bud rot out, and how to measure it all without the sensor "
      "lying to you. No prior physics assumed. Every term is defined."),
  ]})

# ---------------------------------------------------------------- 02 vocabulary
SECTIONS.append({"id": "vocabulary", "kicker": "02 · The vocabulary", "title": "Ten terms and you can read any climate chart",
  "blocks": [
    defterm("Water vapour", "Water as a gas, mixed invisibly into the air. Steam you can see is "
            "droplets; vapour you can&rsquo;t."),
    defterm("Vapour pressure", "The share of air pressure contributed by water vapour, measured in "
            "kilopascals (kPa). It is the honest way to say &lsquo;how much water is in this air&rsquo;."),
    defterm("Saturation vapour pressure (es)", "The ceiling: the most vapour pressure air can hold "
            "at a given temperature before water starts condensing out. Rises steeply with "
            "temperature" + _c("fao56-1998") + "."),
    defterm("Actual vapour pressure (ea)", "What&rsquo;s really in the air right now. Always at or "
            "below the ceiling."),
    defterm("Relative humidity (RH)", "Actual as a percentage of the ceiling: ea &divide; es &times; 100. "
            "Useful, but meaningless without the temperature next to it."),
    defterm("Vapour pressure deficit (VPD)", "The gap: es &minus; ea, in kPa. The drying power of the "
            "air &mdash; the number the plant feels."),
    defterm("Leaf VPD", "The same gap computed from <em>leaf</em> temperature instead of air "
            "temperature, because the air inside a leaf is saturated at the leaf&rsquo;s own "
            "temperature. This is the real driver of transpiration" + _c("grossiord2020-vpd") + "."),
    defterm("Dew point", "The temperature at which the air you have becomes saturated. Cool any "
            "surface below it and water condenses there. The mould number."),
    defterm("Transpiration", "Water evaporating out of the leaf through its pores, pulling the water "
            "column &mdash; and dissolved nutrients &mdash; up from the roots behind it."),
    defterm("Stomata", "The adjustable pores (mostly on the leaf underside) where vapour leaves and "
            "CO2 enters. Guard cells open and close them by the minute. Singular: stoma."),
  ]})

# ---------------------------------------------------------------- 03 what VPD is
SECTIONS.append({"id": "what-vpd-is", "kicker": "03 · The core idea", "title": "A ceiling, a level, and the gap between them",
  "blocks": [
    p("Think of air as a tank whose height changes with temperature. Warm the air and the tank gets "
      "taller &mdash; it <em>can</em> hold more vapour. The water already in it doesn&rsquo;t change "
      "just because you warmed the room; only the headroom changes. That headroom &mdash; the gap "
      "between the ceiling (es) and the level (ea) &mdash; is VPD."),
    figure(_FIGS["vpd-anatomy"], 1,
      "Same 60% RH, two different rooms. The percentage is identical; the gap the plant transpires "
      "into is 60% bigger in the warm room. This is why RH alone cannot describe a climate."),
    p("This is the whole reason plants respond to VPD and not RH: water moves out of a leaf by "
      "diffusion, and diffusion is driven by the absolute difference in vapour pressure between the "
      "saturated air inside the leaf and the room air outside it &mdash; not by a ratio" +
      _c("grossiord2020-vpd") + ". Two rooms at the same RH can pull on the crop completely "
      "differently. Two rooms at the same VPD pull the same, whatever their RH says."),
    figure(_FIGS["es-curve"], 2,
      "The saturation curve from the FAO-56 Tetens formula" + _c("fao56-1998") + ". The ceiling "
      "climbs about 6% per degree and doubles between 14 and 25&nbsp;°C &mdash; which is why "
      "temperature moves VPD harder than most humidity adjustments do."),
    p("The curve is the single most useful piece of physics in climate control, because everything "
      "annoying about grow-room humidity falls out of it: why the room spikes to 90% RH at "
      "lights-off (the ceiling dropped, the water stayed), why a heater &lsquo;dries&rsquo; the air "
      "without removing a gram of water, and why summer rooms drink so much harder at the same RH."),
    figure(L.bars("How much water saturated air can carry",
        [("10 °C", 9.4), ("15 °C", 12.8), ("20 °C", 17.3), ("25 °C", 23.0), ("30 °C", 30.4)],
        unit=" g/m³",
        note="Grams of water per cubic metre of air at 100% RH, derived from the FAO-56 saturation values."), 3,
      "The same ceiling expressed in grams. A 30&nbsp;°C room can carry nearly double the water of a "
      "20&nbsp;°C room &mdash; every degree of temperature is also a humidity decision" + _c("fao56-1998") + "."),
    callout("key", "The one-line mental model",
      p("RH is a percentage of a moving ceiling. VPD <em>is</em> the gap. The plant lives in the gap.")),
  ]})

# ---------------------------------------------------------------- 04 the equation
SECTIONS.append({"id": "equation", "kicker": "04 · The maths", "title": "The equation, in a form you can actually use",
  "blocks": [
    p("Everything runs on one empirical formula for the ceiling, good to a fraction of a percent "
      "over grow-room temperatures. It is the Tetens equation as standardised in FAO Irrigation and "
      "Drainage Paper 56" + _c("fao56-1998") + ", with T in &deg;C and the result in kPa:"),
    callout("note", "The saturation ceiling",
      p("<strong>es(T) = 0.6108 &times; e<sup>(17.27 &times; T) / (T + 237.3)</sup></strong> kPa"
        "<br>Then: &nbsp;<strong>ea = es(T<sub>air</sub>) &times; RH / 100</strong> &nbsp;and&nbsp; "
        "<strong>VPD<sub>air</sub> = es(T<sub>air</sub>) &minus; ea = es(T<sub>air</sub>) &times; "
        "(1 &minus; RH/100)</strong>")),
    p("Worked once, slowly, with the numbers you&rsquo;ll see all through this paper:"),
    kv([("Air temperature", "25.0 °C"),
        ("Relative humidity", "60%"),
        ("Ceiling es(25)", "0.6108 × e^(431.75 / 262.3) = 3.17 kPa"),
        ("Actual ea", "3.17 × 0.60 = 1.90 kPa"),
        ("Air VPD", "3.17 − 1.90 = 1.27 kPa")]),
    p("If you&rsquo;d rather not raise e to anything before coffee, a lookup row of ceilings covers "
      "most rooms &mdash; multiply by (1 &minus; RH/100) and you&rsquo;re done:"),
    table(["Air temp", "es (kPa)", "VPD @ 50% RH", "VPD @ 60% RH", "VPD @ 70% RH"], [
      ["18 °C", "2.06", "1.03", "0.83", "0.62"],
      ["20 °C", "2.34", "1.17", "0.94", "0.70"],
      ["22 °C", "2.64", "1.32", "1.06", "0.79"],
      ["24 °C", "2.98", "1.49", "1.19", "0.90"],
      ["26 °C", "3.36", "1.68", "1.34", "1.01"],
      ["28 °C", "3.78", "1.89", "1.51", "1.13"],
      ["30 °C", "4.25", "2.12", "1.70", "1.27"],
    ], cls="compact", caption="Saturation vapour pressure and air-basis VPD, computed from the FAO-56 formula" + _c("fao56-1998") + ". Full precision kept to two decimals."),
    callout("tip", "Units, quickly",
      p("1 kPa = 10 mbar = 10 hPa. Some US charts use pounds per square inch or grains of moisture "
        "&mdash; ignore them, the cultivation literature and every serious controller speak kPa. "
        "Ranges you will meet in a grow room: roughly 0.2 (fog) to 2.5 (desert).")),
  ]})

# ---------------------------------------------------------------- 05 leaf VPD
SECTIONS.append({"id": "leaf-vpd", "kicker": "05 · The real number", "title": "Leaf temperature, not air temperature, sets the pull",
  "blocks": [
    p("Here is the correction that separates people who chart VPD from people who control it. The "
      "air <em>inside</em> a leaf is saturated at the <em>leaf&rsquo;s</em> temperature. So the "
      "gradient driving transpiration is not es(air) &minus; ea &mdash; it is "
      "<strong>es(leaf) &minus; ea</strong>" + _c("grossiord2020-vpd") + ". If leaf and air were "
      "always the same temperature the distinction wouldn&rsquo;t matter. They aren&rsquo;t."),
    p("A healthy, transpiring canopy runs close to air temperature &mdash; typically within about "
      "2&nbsp;°C under any light source &mdash; but which <em>side</em> of air it sits on depends "
      "mostly on the radiation hitting it" + _c("nelson2015-leaftemp") + ". An HPS lamp throws a "
      "large radiant load onto the canopy and pushes leaves above air temperature. An LED fixture "
      "convects most of its heat away at the heatsink, so a transpiring leaf &mdash; cooling itself "
      "by evaporation &mdash; commonly sits <em>below</em> air temperature. At equal light levels "
      "the modelled difference is about 1.3&nbsp;°C between the two technologies" +
      _c("nelson2015-leaftemp") + ", and grower tooling conventionally assumes LED canopies run "
      "1&ndash;3&nbsp;°C cool" + _c("pulse-vpd-guide") + "."),
    figure(_FIGS["leaf-offset"], 4,
      "Identical room readout, different plant reality. A couple of degrees of leaf offset moves the "
      "computed deficit by a full stage band" + _c("nelson2015-leaftemp") + "."),
    p("Run the worked example again with real leaf temperatures and watch the answer move. Air "
      "25&nbsp;°C / 60% RH says 1.27 kPa &mdash; textbook flower climate. If the LED canopy sits at "
      "23&nbsp;°C, the leaf feels es(23) &minus; 1.90 = <strong>0.91 kPa</strong> &mdash; veg "
      "territory, a third wetter than the dashboard claims. Under HPS with the leaf at 26&nbsp;°C "
      "it feels <strong>1.46 kPa</strong> &mdash; top of the flower band. Same room. Three answers."),
    callout("warn", "The LED-room trap",
      p("Most rooms that converted HPS &rarr; LED kept their old temperature and humidity targets. "
        "Their air VPD looks right while their <em>leaf</em> VPD runs a band low &mdash; a quietly "
        "wetter crop: softer growth, slower drybacks, more condensation margin eaten at night. If "
        "you converted fixtures and mould pressure rose, this arithmetic is probably why. Raise air "
        "temperature a degree or two, or drop RH, and re-check against <em>leaf</em> numbers.")),
    callout("danger", "A hot leaf is a warning, not an offset",
      p("The offsets above assume a transpiring, well-watered canopy. A drought-stressed leaf that "
        "has shut its stomata loses its evaporative cooling and can climb 6&ndash;12&nbsp;°C above "
        "air temperature" + _c("nelson2015-leaftemp") + ". If your IR thermometer reads a leaf "
        "running hot, the plant isn&rsquo;t asking for a chart correction &mdash; it&rsquo;s telling "
        "you transpiration has stopped. Check the root zone before you touch the climate.")),
  ]})

# ---------------------------------------------------------------- 06 the chart
SECTIONS.append({"id": "the-chart", "kicker": "06 · The lookup", "title": "The VPD chart and how to read it",
  "blocks": [
    p("The classic grower chart is just the equation pre-computed: temperature down the side, RH "
      "across the top, the deficit in every cell. Here it is, coloured by the stage bands from the "
      "next section:"),
    figure(_FIGS["vpd-chart"], 5,
      "Temperature &times; RH &rarr; kPa, air-basis. One glance shows the exchange rate of the "
      "whole game: a degree of temperature moves the answer about as far as two to three points "
      "of RH."),
    steps([
      ("Measure where the plants live", "Air temperature and RH at canopy height, mid-room — not at the controller on the wall. Placement is half the battle (section 11)."),
      ("Get a leaf temperature", "IR thermometer or canopy sensor on a lit, upper leaf. No reading? Assume leaf ≈ air under HPS, 1–2 °C below air under LED" + _c("nelson2015-leaftemp") + "."),
      ("Read the cell", "Find your temperature row and RH column. That number, in kPa, is what your air is asking of the crop."),
      ("Correct for the leaf", "Cooler leaf = real VPD lower than the cell; warmer leaf = higher. At 25 °C / 60%, a 2 °C-cool canopy turns 1.27 into 0.91 kPa — don't guess, use a leaf-offset calculator or a controller that takes leaf temperature" + _c("pulse-vpd-guide") + "."),
      ("Move along one axis at a time", "Too dry? Slide left (raise RH) before you slide up the temperature column. One change, fifteen minutes, re-read."),
    ]),
    callout("tip", "Two roads to the same number are not the same room",
      p("27&nbsp;°C / 65% and 21&nbsp;°C / 45% both land near 1.3 kPa, but they are not "
        "interchangeable climates: temperature has its own biology on top of VPD. Cannabis "
        "photosynthesis peaks around 25&ndash;30&nbsp;°C" + _c("chandra2008-photo") + ", "
        "morphology and stretch respond to the day/night temperature difference" + _c("moe1995-dif") +
        ", and disease pressure rides on absolute humidity. Pick the temperature your stage and "
        "fixture want first; use humidity to dial the VPD around it.")),
  ]})

# ---------------------------------------------------------------- 07 stage targets
SECTIONS.append({"id": "stage-targets", "kicker": "07 · The targets", "title": "Stage bands: convention, hedged honestly",
  "blocks": [
    p("The bands below are the industry&rsquo;s working convention, not a law of nature. They come "
      "from grower practice converging over a decade" + _c("pulse-vpd-guide") + ", they sit inside "
      "the ranges recommended by the cannabis production literature" + _c("jin2019-cannabis-env") +
      ", and the one controlled cannabis humidity experiment we have brackets them from the wet "
      "side: flowering at 0.05&ndash;0.25 kPa instead of ~0.9&ndash;1.3 kPa cost 71% of flower "
      "biomass, delayed flowering three weeks and slashed cannabinoid concentration" +
      _c("corredor2025-rh") + ". Treat the band as the middle of the road; your cultivar, light "
      "intensity and mould ceiling steer within it."),
    figure(L.zones("Stage bands on one axis (leaf-basis, kPa)", 0, 2.4,
        [(0, 0.4, "var(--fig-waterl)", "too wet"),
         (0.4, 0.8, "var(--fig-blue-l)", "clone 0.4–0.8"),
         (0.8, 1.2, "var(--fig-green-l)", "veg 0.8–1.2"),
         (1.2, 1.6, "var(--fig-dryl)", "flower 1.2–1.5"),
         (1.6, 2.0, "var(--fig-amber-l)", "watch"),
         (2.0, 2.4, "var(--fig-red-l)", "stress")],
        unit=" kPa",
        note="Bands are convention: start mid-band, then let the plant and your night mould ceiling move you."), 6,
      "One axis, whole grow. The bands drift drier as the plant builds roots and leaf area &mdash; "
      "more plumbing, more tolerance for pull" + _c("pulse-vpd-guide") + _c("jin2019-cannabis-env") + "."),
    table(["Stage", "Leaf VPD band", "Why", "Example combo (air-basis)"], [
      ["Clones / fresh seedlings", "0.4–0.8 kPa", "Little or no root; the shoot must not out-transpire uptake",
       "24 °C / 75–80% RH → ~0.6–0.7"],
      ["Early veg", "0.8–1.1 kPa", "Roots established; push gas exchange without stressing",
       "25 °C / 65–70% RH → ~1.0"],
      ["Late veg", "0.9–1.2 kPa", "Full canopy, high light; keep flux strong and steady",
       "26 °C / 62–68% RH → ~1.1–1.3"],
      ["Early–mid flower", "1.1–1.4 kPa", "Drive water and nutrient throughput through peak bulk",
       "26 °C / 58–62% RH → ~1.3–1.4"],
      ["Late flower", "1.2–1.5 kPa", "Dense buds: the mould ceiling now outranks the VPD target",
       "24 °C / 50–55% RH → ~1.4–1.5"],
    ], cls="compact",
      caption="Working convention" + _c("pulse-vpd-guide") + _c("jin2019-cannabis-env") + _c("corredor2025-rh") +
      ". Combos assume leaf ≈ air; in an LED room run the air warmer or the RH lower to land the same leaf VPD."),
    callout("note", "Why the hedge matters",
      p("Nobody has published a dose&ndash;response curve of cannabis yield against VPD across "
        "stages; the bands interpolate physiology, production reviews and fleet practice. What the "
        "evidence does say clearly: far too wet is expensive" + _c("corredor2025-rh") + ", far too "
        "dry shuts stomata and throttles photosynthesis" + _c("grossiord2020-vpd") + ", and stable "
        "beats perfect &mdash; plants held at a steady moderate VPD out-grow ones yo-yoing around "
        "the &lsquo;ideal&rsquo; number" + _c("inoue2021-vpd") + ".")),
  ]})

# ---------------------------------------------------------------- 08 transpiration
SECTIONS.append({"id": "transpiration", "kicker": "08 · The engine", "title": "Transpiration: what the deficit actually drives",
  "blocks": [
    p("VPD matters because transpiration is the crop&rsquo;s engine, and VPD is its throttle. Water "
      "evaporates from cell walls inside the leaf and diffuses out of the stomata into the deficit. "
      "That loss puts the whole water column under tension, pulling water &mdash; and everything "
      "dissolved in it &mdash; from the root zone up through the plant. Calcium in particular only "
      "travels with this stream, which is why chronically wet, low-VPD air shows up later as weak "
      "tissue and tip burn in fast growth. Evaporation also carries heat away: transpiration is the "
      "plant&rsquo;s own air-conditioner, the reason a healthy LED canopy reads cooler than the room" +
      _c("nelson2015-leaftemp") + "."),
    figure(_FIGS["stomata-three"], 7,
      "The valve and the gradient. Flux needs both a gap to diffuse into and an open pore &mdash; "
      "and the plant controls the pore" + _c("grossiord2020-vpd") + "."),
    p("The crucial subtlety: the response is not linear. As VPD climbs past the plant&rsquo;s "
      "comfort range, guard cells progressively close the stomata to protect the water column. "
      "Transpiration stops rising and can fall; CO2 intake &mdash; and photosynthesis with it &mdash; "
      "throttles down at exactly the moment your lights are begging for gas exchange" +
      _c("grossiord2020-vpd") + ". Cranking the deficit does not crank the engine. It floods the "
      "clutch."),
    ul([
      "<strong>Too low (&lt;0.4 kPa):</strong> open pores, no gradient. Growth goes soft and "
      "stretchy, calcium delivery sags, water films sit on tissue, guttation overnight &mdash; and "
      "the flowering cost is documented and brutal" + _c("corredor2025-rh") + ".",
      "<strong>In the band:</strong> steady pull, cool leaf, open stomata, nutrients moving. This "
      "is the state everything else in this paper exists to protect.",
      "<strong>Too high (&gt;2.0 kPa):</strong> stomata close, leaf heats, photosynthesis throttles; "
      "the plant spends the afternoon defending itself instead of growing" + _c("grossiord2020-vpd") + ".",
    ]),
    callout("key", "Stability is a target of its own",
      p("Work in controlled environments keeps finding the same thing: minimising VPD "
        "<em>fluctuation</em> holds stomata open and photosynthesis higher than chasing an ideal "
        "set-point through swings" + _c("inoue2021-vpd") + ". A room that holds 1.1 all day beats a "
        "room that averages 1.2 by bouncing between 0.8 and 1.6.")),
  ]})

# ---------------------------------------------------------------- 09 day / night
SECTIONS.append({"id": "day-night", "kicker": "09 · The clock", "title": "Day and night are two different jobs",
  "blocks": [
    p("Daytime VPD control is about growth: hold the stage band, keep it stable, let the engine "
      "run. Night-time VPD control is about <em>protection</em> &mdash; and it is where most rooms "
      "actually get hurt, because the moment the lights cut out, every term in the equation moves "
      "at once: the heat load vanishes, air temperature falls, the ceiling drops with it, and RH "
      "rockets even though not a gram of water entered the room."),
    figure(_FIGS["day-night-trace"], 8,
      "Two identical days, two different nights. The controlled room lets its dehumidifier ride "
      "through lights-off and eases onto a floor; the uncontrolled room collapses into condensation "
      "territory within two hours."),
    steps([
      ("Ramp into the day", "Plants wake before transpiration does. Let VPD climb from its night floor to the day band over the first 1–2 hours of light rather than snapping the dehu and heat on at full tilt — stability beats shock" + _c("inoue2021-vpd") + "."),
      ("Hold the band through peak", "Mid-photoperiod is peak transpiration and peak sensor drift. This is when to trust your canopy sensor over the wall controller."),
      ("Pre-empt lights-off", "Start dehumidification before the temperature falls — pulling water out of warm air is easier, and you enter the night below the danger line instead of chasing it."),
      ("Hold a night floor", "Convention: keep night VPD from collapsing much below ~0.7–1.0 kPa, and never let canopy RH camp above 70%. Plants still transpire at night — commonly 5–15% of daytime rates" + _c("caird2007-night") + " — so the air keeps loading even in the dark."),
    ]),
    callout("note", "Night temperature is also a shape lever",
      p("The day&ndash;night temperature difference (&lsquo;DIF&rsquo;) steers internode stretch in "
        "greenhouse crops &mdash; warmer days than nights stretch, flat or negative DIF compacts" +
        _c("moe1995-dif") + ". Keep the night drop modest (2&ndash;4&nbsp;°C) and you get "
        "manageable morphology <em>and</em> a smaller RH spike to fight. A big macho night drop "
        "buys you compact plants and a condensation problem.")),
  ]})

# ---------------------------------------------------------------- 10 dew point
SECTIONS.append({"id": "night-dew", "kicker": "10 · The mould lever", "title": "Dew point: where night humidity turns into liquid",
  "blocks": [
    p("RH tells you how full the air is. <strong>Dew point</strong> tells you where that fullness "
      "becomes free water: it is the temperature at which your actual vapour content saturates" +
      _c("fao56-1998") + ". Any surface at or below the dew point &mdash; an exterior wall, bare "
      "steel, port glass, the outside of a fat cola radiating heat to a cold ceiling &mdash; "
      "collects liquid water. And free water plus spores is the bud-rot recipe: botrytis risk "
      "climbs steeply once canopy humidity passes about 70%" + _c("punja2025-budrot-epi") + "."),
    figure(_FIGS["dewpoint-night"], 9,
      "Nothing added water. The room cooled toward the dew point it already carried, and the "
      "coldest surfaces crossed it first. Night RH discipline is condensation discipline."),
    p("Dew point moves only when the actual water content moves &mdash; dehumidify and it falls, "
      "irrigate/transpire and it rises. Cooling the room doesn&rsquo;t touch it; cooling just "
      "closes the distance. From the vapour pressure: "
      "<strong>T<sub>d</sub> = 237.3 &times; ln(ea/0.6108) &divide; (17.27 &minus; ln(ea/0.6108))</strong>" +
      _c("fao56-1998") + ". Or read it from a table:"),
    table(["Night air 24 °C at…", "50% RH", "55% RH", "60% RH", "65% RH", "70% RH"], [
      ["Dew point", "12.9 °C", "14.4 °C", "15.8 °C", "17.0 °C", "18.2 °C"],
      ["What condenses", "Almost nothing indoors", "Cold exterior corners", "Uninsulated walls, steel", "Most unwarmed surfaces", "Everything cool — including buds"],
    ], cls="compact",
      caption="Computed from the FAO-56 relations" + _c("fao56-1998") + ". At 24 °C / 70% RH a surface only needs to sit 6 °C below air temperature to run wet all night."),
    figure(L.zones("Night RH at the canopy: the mould axis", 40, 90,
        [(40, 60, "var(--fig-green-l)", "comfortable"),
         (60, 70, "var(--fig-dryl)", "watch"),
         (70, 80, "var(--fig-amber-l)", "high risk"),
         (80, 90, "var(--fig-red-l)", "rot / condensation")],
        unit="% RH",
        note="Judge it at the canopy, at night, not on the daytime room average."), 10,
      "The ceiling that outranks every VPD target in late flower: botrytis pressure rises steeply "
      "past ~70% canopy RH" + _c("punja2025-budrot-epi") + "."),
    callout("danger", "The canopy is wetter than your sensor says",
      p("Inside a dense canopy, transpiration and still air hold humidity 15&ndash;25% above the "
        "room reading" + _c("zhang2020-canopy-rh") + ". A room logging a smug 60% at night can be "
        "carrying an 80%+ microclimate inside the colas &mdash; which is exactly where the rot "
        "starts. Defoliation and through-canopy airflow are humidity tools; see the "
        "<a href='airflow-design.html'>airflow paper</a> and <a href='mould-risk.html'>mould "
        "paper</a>.")),
  ]})

# ---------------------------------------------------------------- 11 measurement
SECTIONS.append({"id": "measurement", "kicker": "11 · The instruments", "title": "Measure where the plant lives, not where the wall is",
  "blocks": [
    p("Climate control inherits every sin of its sensors. Three questions decide whether your VPD "
      "number is real: <em>where</em> the sensor sits, whether radiation is heating it, and whether "
      "you know the leaf temperature at all."),
    figure(_FIGS["sensor-placement"], 11,
      "One aspirated, shielded sensor at canopy height in the row out-performs five convenient ones. "
      "Every bad position has a signature bias &mdash; and a controller will faithfully chase it."),
    ul([
      "<strong>Placement.</strong> Canopy height, inside the crop footprint, away from doors, "
      "dehumidifier discharge and duct outlets. The room average is a fiction; the crop lives in a "
      "microclimate the wall sensor cannot see" + _c("zhang2020-canopy-rh") + ".",
      "<strong>Shielding and aspiration.</strong> Any sensor in direct light absorbs radiation and "
      "reads above true air temperature &mdash; radiation error is worth whole degrees, not "
      "decimals, in still air under strong sources" + _c("tarara2007-shield") + ". A bare sensor "
      "under a fixture reads hot, so its computed VPD reads dry, so your controller humidifies a "
      "room that never asked for it. Shield it, and ideally pull air across it with a small fan "
      "(&lsquo;aspirated&rsquo;).",
      "<strong>Leaf temperature.</strong> A cheap IR thermometer is the single best VPD upgrade "
      "under NZ$50: shoot a lit, upper leaf from close range at a square angle, several leaves, "
      "average them. Dedicated IR canopy sensors do it continuously and feed leaf VPD straight "
      "into the controller. Aim at closed canopy, never at benches, pots or your own hand.",
      "<strong>Redundancy.</strong> Two cheap sensors that agree beat one expensive number nobody "
      "can check. Log night as carefully as day &mdash; section 10 is decided at 3 a.m.",
    ]),
    callout("tip", "Calibrate the cheap way",
      p("Park all your RH sensors together overnight in a sealed box with a saturated table-salt "
        "slurry: the air above it settles at ~75% RH. Anything reading more than a few points off "
        "gets offset or binned. Do it quarterly; capacitive RH elements drift.")),
  ]})

# ---------------------------------------------------------------- 12 the kit
SECTIONS.append({"id": "kit", "kicker": "12 · The kit", "title": "Humidification and dehumidification: make the hardware pull together",
  "blocks": [
    p("Almost all the water you irrigate ends up in the room air &mdash; transpiration returns it "
      "as vapour, and that latent load, not the lights, is what your dehumidification actually "
      "fights" + _c("hpac-latent") + ". Size for it: a room feeding 100 L/day must be able to "
      "remove the better part of 100 L/day of vapour, with the hardest hours right after "
      "lights-off. Undersized dehumidification is the single most common root cause behind "
      "&lsquo;mystery&rsquo; night humidity."),
    ul([
      "<strong>Dehumidifier:</strong> the workhorse. Sized to daily irrigation volume with headroom, "
      "condensate plumbed away, discharge pointed away from sensors" + _c("hpac-latent") + ".",
      "<strong>Air conditioning:</strong> an accidental dehumidifier &mdash; condensate on its coil "
      "is water leaving the room. Fine, until it short-cycles at night and dumps its dehumidifying "
      "role just as RH spikes.",
      "<strong>Humidifier:</strong> a clone and early-veg tool in most sealed rooms; use clean "
      "water and keep the plume off leaves and sensors. Mature canopies humidify themselves.",
      "<strong>Heater:</strong> raises the ceiling, so RH falls and VPD rises with zero water "
      "moved. Often the cheapest fix for a chronically damp small room.",
      "<strong>Circulation fans:</strong> they don&rsquo;t change the room&rsquo;s VPD, but they "
      "destroy the still, saturated boundary layer around leaves and the canopy microclimate" +
      _c("zhang2020-canopy-rh") + " &mdash; the difference between the VPD you set and the VPD the "
      "leaf gets.",
    ]),
    p("The classic self-inflicted wound is the humidifier and dehumidifier duelling: humidity "
      "set-points overlapping so one machine feeds the other, burning power to hold the room in a "
      "tug-of-war. Give them a dead band &mdash; a gap of at least 5% RH between humidify-below and "
      "dehumidify-above &mdash; and change one thing at a time:"),
    figure(L.flow("Fix VPD in the right order",
        [("Read leaf temp", "IR gun on upper canopy, several leaves"),
         ("Compute leaf VPD", "es(leaf) minus actual vapour"),
         ("Move RH first", "dehu / humidifier: fast and cheap"),
         ("Then temperature", "only if RH is already in range"),
         ("Re-check at 15 min", "one change at a time")],
        note="Moisture moves are quick and reversible; temperature moves fight the HVAC, the lights and the plant's own biology."), 12,
      "The adjustment order that keeps you out of oscillation: humidity is the fine dial, "
      "temperature the coarse one."),
  ]})

# ---------------------------------------------------------------- 13 mistakes
SECTIONS.append({"id": "mistakes", "kicker": "13 · The classics", "title": "Common mistakes, named and shamed",
  "blocks": [
    grid([
      card("Chasing VPD with temperature",
        p("The chart shows hotter = higher VPD, so the room gets cranked to 30&nbsp;°C to hit 1.4 "
          "kPa. Now the plants are past their photosynthetic optimum" + _c("chandra2008-photo") +
          ", root-zone and disease biology shifted, and the room drinks absurdly. VPD was in range; "
          "everything else broke. Set temperature for the stage, steer VPD with moisture."),
        tag="Cooking the room"),
      card("Ignoring the leaf offset",
        p("Air-basis VPD under LED reads a comfortable 1.3 while the cool canopy feels 0.9" +
          _c("nelson2015-leaftemp") + ". Weeks of soft growth and rising mould pressure later, the "
          "&lsquo;perfect climate&rsquo; gets the blame. Measure a leaf; correct the chart.")),
      card("Night neglect",
        p("Immaculate daytime curves, no night plan. Lights-off drops the ceiling, RH pins in the "
          "80s, dew forms on the coldest surfaces, and botrytis gets its window" +
          _c("punja2025-budrot-epi") + ". The dehumidifier must work hardest when the room looks "
          "asleep.")),
      card("Trusting one bare sensor",
        p("A single unshielded sensor above the canopy reads the light, the door draught and the "
          "dehu blast &mdash; everything except the crop" + _c("tarara2007-shield") + ". The "
          "controller then automates the error. Shield it, aspirate it, put it at canopy height, "
          "cross-check it.")),
      card("Treating the band as a bullseye",
        p("Hammering the room between heat, humidifier and dehu to hold 1.25 exactly produces "
          "worse plants than parking calmly at 1.1: stomata hate the ride" + _c("inoue2021-vpd") +
          ". Aim mid-band, prize stability, adjust once per photoperiod, not once per hour.")),
      card("Fixing wilt with humidity",
        p("Plants droop, so RH goes up &mdash; but wilt is usually a supply problem (dry or "
          "drowned root zone), not a demand problem. Now the root zone is still broken <em>and</em> "
          "the canopy is wet. Check substrate moisture before touching the air; a hot leaf on the "
          "IR gun is the tell that transpiration already stopped" + _c("nelson2015-leaftemp") + ".")),
    ], cols=2),
  ]})

# ---------------------------------------------------------------- 14 troubleshooting
SECTIONS.append({"id": "troubleshooting", "kicker": "14 · Quick reference", "title": "Troubleshooting table",
  "blocks": [
    table(["You see…", "Likely climate cause", "Do this"], [
      ["Leaf edges curl up, margins crisp, growth stalls mid-day",
       "VPD too high (heat spikes, RH sagging)",
       "Raise RH first; verify with leaf temp — if leaves run hot, check irrigation before climate" + _c("grossiord2020-vpd")],
      ["Soft stretchy growth, leaves praying flat, tip burn in fast veg",
       "Chronic low VPD — weak transpiration and calcium flux",
       "Drop RH or add a degree; confirm canopy sensor isn't reading a wet microclimate" + _c("corredor2025-rh")],
      ["RH spikes to 85%+ within an hour of lights-off",
       "Latent load with no night removal",
       "Start dehu before lights-off; check its real capacity against daily irrigation litres" + _c("hpac-latent")],
      ["Condensation on walls, port glass or tent skin at night",
       "Surfaces below dew point",
       "Lower night RH (dehu) or soften the night temperature drop; insulate the cold surface" + _c("fao56-1998")],
      ["Botrytis in the fattest colas despite a 60% room reading",
       "Canopy microclimate 15–25% wetter than the room sensor",
       "Through-canopy airflow, defoliate, judge night RH at the canopy, not the wall" + _c("zhang2020-canopy-rh") + _c("punja2025-budrot-epi")],
      ["Two sensors disagree by 5%+ RH or 1 °C+",
       "Placement or radiation error, or drift",
       "Shield and aspirate, move out of beams and blasts, salt-test quarterly" + _c("tarara2007-shield")],
      ["VPD perfect on paper, plants limp anyway",
       "It's not the air — supply side (roots, substrate, EC) or leaf temp assumption wrong",
       "IR the canopy, weigh or probe the substrate, re-derive VPD from leaf temperature" + _c("nelson2015-leaftemp")],
    ], cls="compact"),
  ]})

# ---------------------------------------------------------------- 15 mental model
SECTIONS.append({"id": "mental-model", "kicker": "15 · Straight talk", "title": "The model to keep in your head",
  "blocks": [
    callout("key", "Five things, and you understand grow-room climate",
      ol([
        "<strong>The plant feels the gap, not the percentage.</strong> VPD = ceiling minus actual, "
        "in kPa. Same RH at two temperatures is two different climates" + _c("fao56-1998") + ".",
        "<strong>The ceiling is exponential.</strong> ~6% more per degree, double per ~11&nbsp;°C. "
        "Temperature is always also a humidity decision — this is why lights-off is the most "
        "dangerous hour of the day.",
        "<strong>Leaf temperature sets the real number.</strong> LED canopies run cool and wetter "
        "than the chart; HPS canopies hot and drier; a stressed leaf runs way hot and is a red "
        "alert, not an offset" + _c("nelson2015-leaftemp") + ".",
        "<strong>Day VPD grows the plant, night RH keeps it.</strong> Hold the stage band steady "
        "through the photoperiod" + _c("inoue2021-vpd") + "; hold the canopy under ~70% RH and "
        "every surface above dew point through the dark" + _c("punja2025-budrot-epi") + ".",
        "<strong>Measure where the plant lives.</strong> Canopy height, shielded, aspirated, "
        "cross-checked, with a real leaf temperature — or the controller automates a fiction" +
        _c("tarara2007-shield") + _c("zhang2020-canopy-rh") + ".",
      ])),
    p("VPD is the demand side of the water equation; the <a href='grow-room-systems.html'>systems "
      "guide</a> covers the hardware that serves it, <a href='airflow-design.html'>airflow</a> "
      "delivers the set-point into the canopy, and <a href='mould-risk.html'>mould risk</a> is what "
      "this discipline is ultimately protecting. Get the gap right, keep it steady, and most of "
      "what growers call &lsquo;magic touch&rsquo; turns out to be psychrometrics."),
  ]})
