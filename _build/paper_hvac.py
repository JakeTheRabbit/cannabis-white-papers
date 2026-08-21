# -*- coding: utf-8 -*-
"""Paper: HVAC, cooling and dehumidification for grow rooms (beginner-first, operator-grade)."""
import json, os
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        grid, card, chip, kv, steps)
import figs_lib as L

_FIGS = json.load(open(os.path.join(os.path.dirname(__file__), "figs_hvac.json"), encoding="utf-8"))

SLUG = "hvac-dehumidification"
TITLE = "HVAC and dehumidification: the machinery of climate"
EYEBROW = "Environment · Plant"
SUB = ("Every watt you put into a grow room comes back out as heat, and nearly every litre you "
       "irrigate comes back out as vapour. The climate plant is the return path for both. This is "
       "how to size it, choose it, run it, and survive the night it fails.")
META = [("wind", "Climate plant"), ("image", "11 diagrams"),
        ("quote", "Evidence-linked · 14 sources"), ("clock", "~22 min read")]
RELATED = ["grow-room-systems", "temp-humidity-vpd", "airflow-design"]
REF_IDS = ["rii-hvac-bpg", "desertaire-an25-load", "streit2023-hvacd", "hpac-latent",
           "grossiord2020-vpd", "hydrobuilder-ac-sizing", "streit2023-water",
           "quest-perfect-dehu", "quest-dehu101", "sylvane-desiccant",
           "punja-budrot-cjb", "ncia-condensate", "chandra2008-photo", "summers2021-ghg"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

# ---------------------------------------------------------------- 01 start here
SECTIONS.append({"id": "start", "kicker": "01 · Read this first", "title": "Purpose and scope",
  "blocks": [
    lead("A grow room is a machine that turns electricity into light, light into plant, and water "
         "into vapour. The lights are the half everyone budgets for. The climate plant, "
         "cooling, heating, dehumidification, is the half that hauls the heat and the water "
         "back out, every hour of every day, and it typically eats 30&ndash;60% of an indoor "
         "facility&rsquo;s energy bill" + _c("rii-hvac-bpg") + "."),
    p("When it&rsquo;s sized right you barely think about it. When it&rsquo;s guessed, a "
      "mini-split off a BTU chart and a dehumidifier that looked big in the shop. You find "
      "out in week 6 of flower, at 2 a.m., when the room is cold, saturated, and growing "
      "<em>Botrytis</em> instead of flower."),
    p("This paper is written for someone speccing their first serious room or sanity-checking a "
      "mechanical quote. No refrigeration background assumed. By the end you should be able to do "
      "your own load arithmetic, read a dehumidifier spec sheet with suspicion, and explain exactly "
      "why the humidity pins to 85% the moment the lights go out."),
    callout("key", "The two conservation laws that do all the work",
      p("<strong>1. Every watt in becomes heat.</strong> Lights, fans, pumps and dehumidifiers: "
        "in a sealed insulated room, all of it ends up as heat the cooling has to remove. "
        "<strong>2. Every litre in must leave.</strong> As runoff down the drain, a little as plant "
        "tissue, and the rest as vapour your equipment must condense back to liquid. Sizing a "
        "climate system is just doing this accounting honestly.")),
  ]})

# ---------------------------------------------------------------- 02 vocabulary
SECTIONS.append({"id": "terms", "kicker": "02 · The vocabulary", "title": "Definitions",
  "blocks": [
    defterm("Sensible heat", "Heat that changes air <em>temperature</em>, the kind a thermometer "
            "sees. Lights are almost entirely a sensible load."),
    defterm("Latent heat", "Heat hidden in water vapour. Evaporating 1 L of water absorbs about "
            "0.68 kWh; that energy sits in the air as humidity until a cold coil condenses it back "
            "out and releases the heat again. Latent load = moisture load."),
    defterm("BTU and ton", "Imperial heat units the HVAC trade still quotes. 1 kW = 3,412 BTU/h. "
            "1 &ldquo;ton&rdquo; of cooling = 12,000 BTU/h &asymp; 3.5 kW. A &ldquo;5-ton unit&rdquo; "
            "moves ~17.6 kW of heat."),
    defterm("Pint (dehumidifier rating)", "US dehumidifier capacity unit: pints of water removed per "
            "day. 1 US pint = 0.473 L, so a &ldquo;500-pint&rdquo; unit removes ~237 L/day, at "
            "its rating conditions, not necessarily at yours."),
    defterm("Relative humidity (RH)", "How full the air is of vapour, as a % of what it could hold "
            "at its current temperature. Capacity roughly halves for every ~10 &deg;C drop, "
            "which is the entire lights-off story in one sentence."),
    defterm("Dew point", "The temperature at which air becomes saturated and water condenses on any "
            "surface at or below it. Unlike RH, dew point tracks the actual grams of water in the "
            "air, which makes it the better control target."),
    defterm("VPD", "Vapour pressure deficit, the drying power of the air, combining "
            "temperature and RH. It drives transpiration rate, which means it drives your latent "
            "load. Covered fully in the <a href='temp-humidity-vpd.html'>temperature, humidity and "
            "VPD paper</a>."),
    defterm("COP", "Coefficient of performance: kW of heat moved per kW of electricity used. Modern "
            "compressors run COP 3&ndash;4; electric resistance heaters are stuck at 1.0. This one "
            "number explains most HVAC efficiency arguments."),
  ]})

# ---------------------------------------------------------------- 03 core answer
SECTIONS.append({"id": "two-loads", "kicker": "03 · The core idea", "title": "Sensible and latent loads",
  "blocks": [
    p("A comfort air conditioner in an office does one job: remove dry heat. A grow room asks for "
      "two: remove heat <em>and</em> remove water. Engineers split these as the <strong>sensible "
      "load</strong> (temperature) and the <strong>latent load</strong> (moisture), and grow rooms "
      "are unusual because the latent side rivals or exceeds the sensible side for much of the "
      "cycle, a ratio almost no comfort-cooling equipment is built for"
      + _c("desertaire-an25-load") + _c("hpac-latent") + "."),
    figure(_FIGS["split"], 1,
      "The two exits. Lights drive the sensible channel; the crop&rsquo;s transpiration drives the "
      "latent channel. Different loads, different equipment, different failure modes."),
    p("<strong>Where the sensible load comes from:</strong> the lights, overwhelmingly. In an "
      "insulated, sealed room, essentially every watt of electrical input becomes heat that the "
      "cooling plant must remove, and lighting is the single largest share"
      + _c("desertaire-an25-load") + _c("streit2023-hvacd") + ". Dehumidifiers, fan motors, pumps "
      "and people add the rest."),
    p("<strong>Where the latent load comes from:</strong> the plants. Transpiration <em>is</em> the "
      "latent load: of the water delivered to the root zone, roughly 95%+ passes up through the "
      "plant and out the stomata as vapour, Desert Aire&rsquo;s engineering note puts it "
      "near 99% of water taken up by the roots" + _c("desertaire-an25-load") + ", and facility "
      "engineers design on 80&ndash;95% of total irrigation returning to the air"
      + _c("streit2023-water") + ". Your crop is not decoration sitting inside the climate "
      "system. Your crop <em>is</em> the humidifier, running at hundreds of litres a day, powered "
      "by your lights and throttled by VPD" + _c("grossiord2020-vpd") + "."),
    callout("note", "The twist: plants convert sensible into latent",
      p("Evaporating water absorbs heat. A transpiring canopy is a giant evaporative cooler. "
        "So the air temperature rises <em>less</em> than the lights&rsquo; wattage suggests, and "
        "beginners conclude the heat &ldquo;wasn&rsquo;t that bad&rdquo;. It didn&rsquo;t leave. "
        "It moved into the vapour, and you pay it back with interest at the coil that condenses "
        "that vapour out. Total heat rejected always equals total watts in; the plants only decide "
        "how it&rsquo;s split between the two channels.")),
  ]})

# ---------------------------------------------------------------- 04 the loads
SECTIONS.append({"id": "loads", "kicker": "04 · The loads", "title": "Calculating room heat loads",
  "blocks": [
    p("Everything from here on uses one worked room so the numbers stay honest: <strong>40 m&sup2; "
      "of flowering canopy</strong> (~430 sq ft), 10 &times; 700 W LED fixtures, sealed and "
      "CO&#8322;-enriched, insulated internal walls, two 800 W dehumidifiers, ~500 W of "
      "circulation fans and pumps, two crew working in it. Swap in your own numbers, the "
      "method is the point."),
    figure(L.hbars("Where the day's sensible heat comes from (example 40 m² room)",
            [("Lights (10 × 700 W LED)", 7.0), ("Dehumidifiers (2 × 800 W)", 1.6),
             ("Fans + pumps", 0.5), ("People (2 crew)", 0.2)], unit=" kW",
            note="Sealed, insulated room. Every electrical watt inside ends up as heat the cooling plant must remove."), 2,
      "9.3 kW of connected sensible load. Note the second bar: your dehumidifiers are heaters"
      ", nearly 100% of their draw lands in the room as heat, plus the latent heat of every "
      "litre they condense" + _c("hydrobuilder-ac-sizing") + "."),
    table(["Load", "Type", "In the example room", "Notes"], [
      ["Grow lights", "Sensible", "7.0 kW", "The dominant load; scales with installed W" + _c("streit2023-hvacd")],
      ["Dehumidifiers", "Sensible", "1.6 kW draw + condensing heat", "Run mostly at night. They are the night heater"],
      ["Fans, pumps, controls", "Sensible", "~0.5 kW", "Small individually, never zero"],
      ["People", "Sensible + latent", "~0.1 kW each", "&asymp;400 BTU/h per person" + _c("hydrobuilder-ac-sizing")],
      ["Envelope (walls, roof)", "Sensible", "&asymp;0 (insulated internal room)", "Real for containers, sheds, top floors, do not assume zero there"],
      ["Transpiration", "Latent", "~175 L/day (next section)", "The latent load, full stop" + _c("desertaire-an25-load")],
      ["Media + wet surfaces", "Latent", "Small share", "Evaporation from slab faces, trays, wet floors" + _c("desertaire-an25-load")],
      ["Ventilation air", "Both", "&asymp;0 (sealed room)", "In vented rooms, humid outside air is a real latent load"],
    ], cls="compact", caption="The load inventory. Sensible scales with kilowatts installed; latent scales with litres irrigated."),
    callout("warn", "CO₂ burners are a double load",
      p("A propane or natural-gas CO&#8322; burner adds heat <em>and</em> water, combustion "
        "produces roughly 1.5 kg of water vapour per kg of propane burned, straight into your "
        "latent load. Bottled or bulk CO&#8322; adds neither. If you run burners, both sides of "
        "your load calc grow.")),
  ]})

# ---------------------------------------------------------------- 05 water balance
SECTIONS.append({"id": "water-balance", "kicker": "05 · The water balance", "title": "Water balance and dehumidification load",
  "blocks": [
    p("Here is the single most useful sizing fact in this paper: <strong>your dehumidification "
      "requirement is written by your irrigation schedule</strong>. Not by room volume, not by "
      "plant count charts, by litres per day. Water that goes in and doesn&rsquo;t leave "
      "down the drain leaves through the air" + _c("quest-perfect-dehu") + _c("streit2023-water") + "."),
    figure(_FIGS["waterbal"], 3,
      "The water balance for the example room. 240 L irrigated, 60 L captured as runoff, ~5 L "
      "retained in tissue, leaving ~175 L/day that the climate plant must condense back to "
      "liquid. Water in &asymp; water out" + _c("quest-perfect-dehu") + "."),
    steps([
      ("Count the water in", "40 m&sup2; of canopy &times; 6 L/m&sup2;/day at mid-flower = "
       "<strong>240 L/day</strong>. Your irrigation controller already knows this number exactly."),
      ("Subtract collected runoff", "25% runoff captured to drain = 60 L that never touches the "
       "air. 240 &minus; 60 = <strong>180 L/day stays in the room</strong>. (Runoff left standing "
       "in trays evaporates, then it&rsquo;s latent load again. Drain it.)"),
      ("Subtract what the plant keeps", "Plant tissue holds only a few percent of uptake, "
       "call it 5 L/day. The rest transpires" + _c("desertaire-an25-load") + ". "
       "<strong>&asymp;175 L/day becomes vapour.</strong>"),
      ("Convert for spec sheets", "175 L &divide; 0.473 = <strong>&asymp;370 US pints/day</strong>. "
       "Quest&rsquo;s shortcut (gallons fed minus drained, times 8) lands on the "
       "same answer" + _c("quest-perfect-dehu") + "."),
    ]),
    figure(L.line("Example irrigation across a flower cycle - the latent load follows it",
            [("w1", 2.5), ("w2", 3.0), ("w3", 4.0), ("w4", 5.0), ("w5", 6.0), ("w6", 6.0),
             ("w7", 5.5), ("w8", 5.0), ("w9", 4.0)],
            ["wk 1", "wk 2", "wk 3", "wk 4", "wk 5", "wk 6", "wk 7", "wk 8", "wk 9"],
            ylab="L per m² per day", ymin=0, ymax=7,
            note="Example drip schedule. Dehumidification duty tracks this curve week by week: peak latent load lands mid-to-late flower."), 4,
      "The latent load is not constant. It ramps with the crop, peaking exactly when the canopy is "
      "densest and mould risk is highest. Size for the peak week, not the average."),
    callout("tip", "The free load calculation",
      p("You do not need to model transpiration. You already meter it. Litres in (controller "
        "log) minus litres of runoff (measure it for one representative day) is your daily latent "
        "load, per room, per crop stage. It is better data than any consultant&rsquo;s estimate, "
        "and it&rsquo;s free. Log it every cycle; it also tells you when the crop is drinking "
        "abnormally, which is a plant-health signal, not just an HVAC one.")),
  ]})

# ---------------------------------------------------------------- 06 folklore vs load calc
SECTIONS.append({"id": "rules-of-thumb", "kicker": "06 · Sizing the cooling", "title": "Cooling-load calculation",
  "blocks": [
    p("Every forum will tell you &ldquo;3,000&ndash;4,000 BTU per 1,000 W of light&rdquo;. "
      "Here&rsquo;s the secret: that isn&rsquo;t horticultural wisdom, it&rsquo;s a unit "
      "conversion. 1 W of electricity makes 3.412 BTU/h of heat, always, by physics"
      + _c("hydrobuilder-ac-sizing") + ". The folklore is roughly right about the lights and "
      "silent about everything else. Which is how rooms end up 20&ndash;30% short."),
    figure(L.bars("What the folklore counts vs what the room makes",
            [("3 BTU/W folklore", 6.2), ("4 BTU/W folklore", 8.2),
             ("all equipment", 9.3), ("+25% margin", 11.6)], unit=" kW", maxv=13,
            note="10 × 700 W LED example room. 1 kW of electricity = 3,412 BTU/h of heat. The folklore only ever counted the lights."), 5,
      "The folklore band (left two bars) covers the lights and nothing else. The dehumidifiers, "
      "fans and people are real heat; the margin is what keeps you from running at 100% duty on a "
      "35 &deg;C day."),
    steps([
      ("List every watt in the room", "Lights 7,000 W. Dehumidifiers 1,600 W. Fans and pumps "
       "500 W. Two crew &asymp;240 W" + _c("hydrobuilder-ac-sizing") + ". Envelope gain: ~0 here, "
       "real if your room has a hot roof or sun-struck wall."),
      ("Sum it", "7,000 + 1,600 + 500 + 240 &asymp; <strong>9.3 kW of sensible load</strong>."),
      ("Convert to trade units", "9.3 kW &times; 3,412 = &asymp;31,700 BTU/h = &asymp;2.6 tons of "
       "cooling."),
      ("Add margin, not hope", "20&ndash;25% covers hot ambients, dirty coils and derate with age"
       + _c("hydrobuilder-ac-sizing") + ": spec &asymp;<strong>11.6 kW (&asymp;40,000 BTU/h, "
       "&asymp;3.3 tons)</strong>."),
      ("Split it across units", "Two smaller units beat one big one: staged capacity for light "
       "loads, and a failure loses half your cooling, not all of it (Section 12)."),
    ]),
    callout("warn", "Where rule-of-thumb sizing genuinely breaks",
      ul(["<strong>Rooms that exhaust air through the lights or to outside</strong>, part of "
          "the heat never enters the room, so folklore oversizes. (This is where the old "
          "&ldquo;3 BTU/W for vented HPS&rdquo; number came from.)",
          "<strong>Non-insulated spaces</strong>, containers, garages, top floors under hot "
          "roofs. Envelope load can add kilowatts the folklore never saw.",
          "<strong>Forgetting the dehumidifiers</strong>. They add their draw <em>and</em> "
          "return the latent heat of every condensed litre as sensible heat. An AC sized without "
          "them fights the dehus all afternoon.",
          "<strong>Treating cooling capacity as latent capacity</strong>, a nameplate kW of "
          "cooling is sensible + latent combined; how much of it does moisture work depends on coil "
          "temperature and airflow. The next section sizes moisture properly."])),
  ]})

# ---------------------------------------------------------------- 07 dehu sizing
SECTIONS.append({"id": "dehu-sizing", "kicker": "07 · Sizing the dehumidification", "title": "Dehumidifier sizing",
  "blocks": [
    p("Dehumidifier sizing is the water balance from Section 05 plus two corrections everyone "
      "skips: <strong>when</strong> the moisture arrives, and <strong>what the machine actually "
      "removes at your conditions</strong> rather than at the rating point on the box."),
    steps([
      ("Start from the vapour load", "Example room: &asymp;175 L/day &asymp; 370 pints/day total."),
      ("Split day from night", "Transpiration doesn&rsquo;t stop in the dark, stomata close "
       "partially, media keeps evaporating. Assume 70/30: day 122 L over 12 h (&asymp;10 L/h), "
       "<strong>night 53 L over 12 h (&asymp;4.4 L/h)</strong>. Check the split against your own "
       "condensate volumes and correct it. It varies with cultivar and night climate."),
      ("Day duty", "With lights on, the AC coils condense a share of the moisture while cooling; "
       "dehumidifiers top up. This is the easy shift."),
      ("Night duty, the sizing case", "With lights off there is no sensible load, the AC "
       "stops, and its incidental moisture removal stops with it" + _c("desertaire-an25-load") +
       ". <strong>The dehumidifiers alone must carry 4.4 L/h.</strong> That is 105 L/day of "
       "removal <em>rate</em>."),
      ("Derate the nameplate", "Ratings are quoted warm, commonly 26.7 &deg;C / 60% RH "
       "(80 &deg;F), and refrigerant units remove less as the room cools"
       + _c("sylvane-desiccant") + ". If the manufacturer&rsquo;s curve shows ~&#8532; of "
       "nameplate at your 19 &deg;C night, you need &asymp;160 L/day of nameplate <em>running</em> "
       "to hold the night: e.g. two 80 L/day units flat out."),
      ("Then apply N+1", "Two units exactly covering the night means one failure ends the crop. "
       "Fit three 80s (or two 120s) so any single unit can die on a Saturday night without "
       "drama (Section 12)."),
    ]),
    table(["Canopy", "Water in (6 L/m²/day)", "Vapour to remove", "In pints"], [
      ["10 m² (tent-to-small room)", "60 L/day", "&asymp;44 L/day", "&asymp;92 ppd"],
      ["20 m²", "120 L/day", "&asymp;87 L/day", "&asymp;185 ppd"],
      ["40 m² (example room)", "240 L/day", "&asymp;175 L/day", "&asymp;370 ppd"],
      ["80 m²", "480 L/day", "&asymp;349 L/day", "&asymp;738 ppd"],
    ], cls="compact", caption="Pure arithmetic at 6 L/m²/day irrigation, 25% collected runoff, ~97% of retained water transpired. "
       "Scale linearly for your own schedule; then derate nameplates to your night temperature and add N+1."),
    p("Per fixture, the example works out to 17.5 L (&asymp;37 pints) per light per day, a "
      "handy pub-quote number, but notice it&rsquo;s downstream of the irrigation schedule, not a "
      "property of the light. Quest&rsquo;s field guidance of 0.5&ndash;2 pints per square foot of "
      "canopy per day brackets the same range" + _c("quest-dehu101") + ", our room computes "
      "to ~0.86 pints/sq ft. When a rule of thumb and your arithmetic agree, you can trust the "
      "arithmetic; when they disagree, trust the arithmetic anyway."),
    callout("note", "Sealed vs vented changes the answer",
      p("Everything above assumes a sealed, recirculating room, the norm for CO&#8322;-"
        "enriched flower. A vented room exhausts moist air instead of condensing it, so dehu "
        "requirements drop but you inherit the outdoor climate: in a humid summer (Auckland in "
        "February, most of Queensland) intake air can <em>add</em> latent load rather than remove "
        "it. Vented sizing starts from your local psychrometrics, not from this table.")),
  ]})

# ---------------------------------------------------------------- 08 equipment classes
SECTIONS.append({"id": "equipment", "kicker": "08 · The hardware", "title": "HVAC equipment classes",
  "blocks": [
    p("Four families of cooling, plus the dehumidifiers that bolt onto all of them. Engineering "
      "firms describe the same ladder: packaged DX with standalone dehus at entry level, DX with "
      "hot-gas reheat in the middle, chilled water at scale" + _c("streit2023-hvacd") + "."),
    figure(_FIGS["equipment"], 6,
      "The four classes. Capex rises left to right and top to bottom; so does control quality and "
      "the ease of building in redundancy" + _c("streit2023-hvacd") + "."),
    grid([
      card("Mini-split / multi-split",
        p("Refrigerant line to a wall or ceiling head. Cheap, available everywhere, installed in a "
          "day. Cooling-biased: latent removal is incidental, control is a &plusmn;1&ndash;2 &deg;C "
          "wall thermostat, and there&rsquo;s no reheat, so it overcools while dehumidifying. "
          "Right answer for veg rooms, dry rooms and small flower rooms <em>with</em> standalone "
          "dehus doing the moisture work."), tag="entry"),
      card("Packaged / rooftop unit (RTU)",
        p("One factory cabinet outside the envelope, ducted supply and return. Direct-expansion "
          "(DX) cooling, real airflow, service access without entering the grow. The workhorse "
          "tier for single rooms and small facilities, still pair it with dehumidifiers, "
          "and prefer staged or inverter compressors over single-stage" + _c("streit2023-hvacd") + "."), tag="workhorse"),
      card("Chilled water + fan coils",
        p("A central chiller makes cold water; insulated loops feed fan-coil units in each room. "
          "Scales across many rooms, concentrates redundancy at the plant (two chillers backing "
          "the whole facility), and with heating-water or reheat coils gives genuine independent "
          "temperature and humidity control" + _c("streit2023-hvacd") + ". Needs real mechanical "
          "design. This is an engineered system, not a purchase."), tag="scale"),
      card("Integrated grow unit (HVACD)",
        p("Purpose-built cabinets that cool, dehumidify and reheat in one sequenced box, sized "
          "from your load calc and controlled on dew point. Built precisely for the lights-off "
          "problem. Premium capex; strongest case in tightly controlled flower and drying rooms "
          "where climate misses cost real money" + _c("rii-hvac-bpg") + "."), tag="precision"),
    ], cols=2),
    p("<strong>Standalone vs ducted dehumidifiers.</strong> Standalone (hang-above-canopy or "
      "floor) units are cheap, movable and simple, but they dump their heat and noise in "
      "the room and their condensate wants managing. Ducted/inline units sit outside the canopy, "
      "plumb their drains properly, and share the air-handling path, at higher install cost. "
      "Either way: <strong>plumb the drain</strong>. A bucket is a humidifier with extra steps."),
    table(["", "Refrigerant dehumidifier", "Desiccant dehumidifier"], [
      ["How it works", "Pulls air over a cold coil; vapour condenses; drains as liquid", "Adsorbs vapour into a desiccant wheel; regenerated with a heater"],
      ["Sweet spot", "Warm rooms, 18&ndash;30 &deg;C, i.e. flower rooms", "Cool rooms, keeps full capacity where coils frost" + _c("sylvane-desiccant")],
      ["Cold behaviour", "Capacity falls as the room cools; coils can ice below ~15 &deg;C", "Unbothered by cold; works to near-freezing" + _c("sylvane-desiccant")],
      ["Heat added to room", "Compressor draw + latent heat of condensed water", "More, regeneration heat lands in the airstream (+3&ndash;5 &deg;C typical)" + _c("sylvane-desiccant")],
      ["Typical grow use", "Flower and veg rooms, the default", "Cold drying/curing rooms (16&ndash;18 &deg;C), winter spaces"],
    ], cls="compact", caption="Refrigerant for the grow, desiccant for the cold dry room is the usual split."),
  ]})

# ---------------------------------------------------------------- 09 lights-off
SECTIONS.append({"id": "lights-off", "kicker": "09 · The hard part", "title": "Lights-off humidity spike",
  "blocks": [
    p("Watch any grow room&rsquo;s trend graph and you&rsquo;ll see the same signature: the moment "
      "the lights cut, RH leaps 15&ndash;25 points in under an hour. Three things happen at once, "
      "and every one of them pushes the same direction:"),
    ol([
      "<strong>The sensible load vanishes.</strong> 7 kW of light heat disappears in one second. "
      "The AC, which was condensing moisture as a side effect of cooling, ramps to "
      "zero and takes its moisture removal with it" + _c("desertaire-an25-load") + _c("quest-dehu101") + ".",
      "<strong>The air cools, so RH rises with no new water at all.</strong> Air&rsquo;s capacity "
      "to hold vapour roughly halves per 10 &deg;C drop. Cool the example room&rsquo;s 26 &deg;C / "
      "55% air to 19 &deg;C and it sits at &asymp;84% RH, same grams of water, smaller "
      "container. (Quest&rsquo;s version of the same arithmetic: 24 &deg;C at 57% becomes "
      "&asymp;80% at 18 &deg;C" + _c("quest-dehu101") + ".)",
      "<strong>The crop keeps transpiring.</strong> Slower in the dark, but far from zero, and wet "
      "media keeps evaporating all night. In the example room that&rsquo;s still &asymp;4.4 L of "
      "new vapour every hour.",
    ]),
    figure(_FIGS["lightsoff"], 7,
      "The lights-off signature. Temperature falls, RH spikes toward the mould window, and the "
      "gap between the spike and your night target is exactly the dehumidification capacity you "
      "did, or didn&rsquo;t, install."),
    figure(L.zones("Flowering-room humidity, and where the trouble starts", 30, 80,
            [(30, 40, L.AMBL, "too dry"), (40, 60, L.GL, "flowering band"),
             (60, 70, L.AMBL, "watch zone"), (70, 80, L.REDL, "mould territory")], unit="% RH",
            note="Room sensor values. The canopy interior runs wetter than any wall-mounted sensor, so the margin is thinner than it looks."), 8,
      "Late flower wants the low half of the band. Every hour spent above ~70% at night is time in "
      "<em>Botrytis</em>&rsquo; preferred climate" + _c("punja-budrot-cjb") + "."),
    p("<strong>Why this window matters so much:</strong> bud rot (<em>Botrytis cinerea</em>) "
      "thrives in cool, near-saturated, still air, and dense late-flower colas hold exactly that "
      "microclimate internally" + _c("punja-budrot-cjb") + ". The room hits its highest RH at its "
      "lowest temperature, dew forms on whatever surface sits below the dew point (at 26 &deg;C / "
      "55%, that&rsquo;s any surface under ~16 &deg;C, duct skins, exterior walls, cold "
      "glass), and the crop is at its most vulnerable stage. The night latent capacity you sized "
      "in Section 07 is not a comfort feature. It is mould control."),
    callout("tip", "Engineer a soft landing, not a cliff",
      ul(["<strong>Pre-dry the room:</strong> run dehumidifiers hard for the final hour of "
          "lights-on so the room enters the night at the bottom of its RH band, with headroom.",
          "<strong>Ramp, don&rsquo;t step:</strong> if your controller supports it, stage the "
          "lights down over 15&ndash;30 minutes so the AC and dehus track the transition instead "
          "of getting ambushed by it.",
          "<strong>Use the dehu heat:</strong> a dehumidifier returns ~0.68 kWh per litre plus its "
          "own draw as heat, in the example room that&rsquo;s ~4.6 kW through the night, "
          "usually most of what&rsquo;s needed to hold 19 &deg;C. Free night heating, already "
          "paid for.",
          "<strong>Alarm on rate-of-rise:</strong> RH climbing faster than your modelled spike "
          "means a dehu has dropped out. You want that text at 22:10, not the smell at 07:00."])),
    callout("danger", "Condensation is the line",
      p("If you ever see droplets on walls, ducts or fixtures at lights-off, you are past "
        "warnings: liquid water in a <em>Botrytis</em> room. That night: raise the night "
        "temperature setpoint a degree (warmer air holds the same water at lower RH), run every "
        "dehu you own, and open the canopy with airflow. Then fix the capacity shortfall before "
        "the next dark period, not before the next crop.")),
  ]})

# ---------------------------------------------------------------- 10 airflow integration
SECTIONS.append({"id": "airflow", "kicker": "10 · Air distribution", "title": "HVAC supply, return and circulation",
  "blocks": [
    p("The climate plant conditions air; the room still has to <em>distribute</em> it. Two "
      "systems, two jobs: the air handling loop delivers conditioned air and drags moist warm air "
      "back to the coils, sealed grow rooms typically turn the room&rsquo;s air over "
      "20&ndash;40 times per hour, recirculating ~100% of it to keep CO&#8322; and keep outside "
      "contaminants out" + _c("streit2023-hvacd") + ", while circulation fans stir the "
      "canopy so no leaf sits in its own humid boundary layer (that story is the "
      "<a href='airflow-design.html'>airflow design paper</a>)."),
    figure(_FIGS["crosssection"], 9,
      "Supply high on one side, return low on the other, so conditioned air is forced through the "
      "canopy zone rather than over it. Circulation fans handle the last metre; the dehumidifier "
      "drains to a plumbed line, not a bucket."),
    ul([
      "<strong>Supply high, return low.</strong> Dry supply air is less dense paths matter less "
      "than geometry: pushing supply across the ceiling and pulling return at floor level forces "
      "air through the canopy, where the load actually is.",
      "<strong>Don&rsquo;t short-circuit the air path.</strong> A supply diffuser blowing straight "
      "into a nearby return conditions the duct, not the room. Sensors near that path read "
      "beautifully while the far corner rots.",
      "<strong>Place dehumidifiers deliberately.</strong> Discharge aimed along a wall or aisle, "
      "not blasting one bench of plants with hot dry air; intake sitting in the moist zone, not "
      "in its own dry plume, a unit re-breathing its own discharge reads a dry room and "
      "idles while the canopy stays wet.",
      "<strong>Watch compressor short-cycling.</strong> A grossly oversized single-stage AC "
      "satisfies the thermostat in minutes and shuts down before the coil ever gets cold and wet "
      "enough to condense much. You get temperature control and no dehumidification, plus "
      "compressor wear. Staged or inverter capacity, plus minimum-run timers, is the fix.",
    ]),
  ]})

# ---------------------------------------------------------------- 11 condensate
SECTIONS.append({"id": "condensate", "kicker": "11 · The water coming back", "title": "Condensate management and reuse",
  "blocks": [
    p("Everything the coils and dehumidifiers condense has to go somewhere, in the example "
      "room, ~175 L/day of it. That flow is a maintenance liability, a free instrument, and a "
      "potential water resource, in that order."),
    ul([
      "<strong>A maintenance liability:</strong> every unit needs a trapped, sloped drain or a "
      "reliable condensate pump with a float cut-out. Pans and trays grow biofilm and drip on "
      "canopy; blocked drains shut units down (good ones) or overflow into ceilings (the rest). "
      "Tray and drain cleaning is an IPM task, not optional housekeeping.",
      "<strong>A free instrument:</strong> metered condensate is your measured latent load. "
      "Falling condensate at constant irrigation means either runoff went up or removal capacity "
      "went down, both worth knowing by breakfast.",
      "<strong>A resource:</strong> most of the irrigation water you paid for comes back as "
      "near-distilled condensate, and it can be captured and reused" + _c("streit2023-water") + ".",
    ]),
    figure(L.flow("Condensate reuse, done properly",
            [("Collect", "Coil + dehu trays to one tank"),
             ("Filter", "Sediment + carbon for organics"),
             ("Disinfect", "UV or AOP - tray water is not sterile"),
             ("Polish", "RO or blend to target EC"),
             ("Reuse", "Back into irrigation makeup")],
            note="Treat condensate as raw water, not as RO permeate - it has been across coils, trays and drain lines."), 10,
      "The reuse path. Condensate is low-EC with pH typically 5.5&ndash;6.5, but it can carry "
      "VOCs, metals picked up from coils (copper, zinc, lead) and microbial load from wet trays"
      ", treat before it touches the crop" + _c("ncia-condensate") + "."),
    callout("note", "Compliance angle",
      p("Under GACP-style quality systems and most medicinal licensing regimes, irrigation water "
        "quality must be controlled and documented. If condensate re-enters the crop, its "
        "treatment train and test results belong in your water SOP alongside the source water"
        ", decide and document <em>before</em> the auditor asks" + _c("ncia-condensate") + ".")),
  ]})

# ---------------------------------------------------------------- 12 redundancy
SECTIONS.append({"id": "redundancy", "kicker": "12 · When it breaks", "title": "Redundancy planning",
  "blocks": [
    p("Run the failure before it runs you. Example room, week 6, 23:00: two 80 L/day units are "
      "carrying the night at &asymp;⅔ nameplate. One trips on a failed capacitor. Do the "
      "arithmetic: the room&rsquo;s ~150 m&sup3; of air at 19 &deg;C / 60% RH can only absorb "
      "about <strong>one more litre of water</strong> before saturation. And the crop is "
      "adding &asymp;4.4 L every hour. The surviving unit removes barely half of that. RH is "
      "against the ceiling within the hour, condensation starts on the coldest surfaces, and "
      "nothing else in the room can help because the AC has no sensible load to run against. "
      "This is not a slow drift you catch at the morning walk-through. It runs away in minutes."),
    p("<strong>N+1</strong> is the fix, and it&rsquo;s exactly what it sounds like: N units cover "
      "the design load; you install one more, so any single failure leaves the room fully served. "
      "Apply it in order of what kills the crop fastest:"),
    ol([
      "<strong>Night dehumidification first.</strong> No fallback exists, when a dehu dies "
      "at night, nothing else removes water. Three 80s where two carry the load.",
      "<strong>Cooling second.</strong> Day cooling failure has a fallback: shed the load. "
      "Interlock the lights so a cooling fault dims them to 50% or kills them. You can "
      "afford a lost day of photosynthesis; you cannot afford 40 &deg;C over a full photoperiod. "
      "Two smaller ACs also beat one big one here.",
      "<strong>Controls and alarms last but not least</strong>, the redundancy you "
      "don&rsquo;t know has failed doesn&rsquo;t exist. Alarms must reach a human who can act, "
      "and must survive the same power event that caused the fault.",
    ]),
    grid([
      card("Night dehu dies", p("RH runs away in minutes (arithmetic above). <strong>Detect:</strong> "
        "RH rate-of-rise alarm. <strong>Survive:</strong> N+1 capacity, auto-restart after trip, a "
        "spare capacitor on the shelf."), tag="worst case"),
      card("Day AC dies", p("9 kW keeps arriving with nowhere to go; a sealed room climbs degrees "
        "per hour. <strong>Detect:</strong> temp alarm + current sensor on the unit. "
        "<strong>Survive:</strong> lights interlock sheds the load automatically; second unit "
        "carries a de-rated day."), tag="has a fallback"),
      card("Condensate drain blocks", p("Water where it shouldn&rsquo;t be; float switch stops the "
        "unit. Which quietly becomes a capacity failure. <strong>Detect:</strong> unit-"
        "stopped alarm, weekly tray inspection. <strong>Survive:</strong> plumbed drains, floats "
        "tested monthly, trays on the cleaning roster."), tag="sneaky"),
      card("Coil ices up", p("Starved airflow (dirty filter), low charge, or a too-cold room. Unit "
        "runs, removes nothing, then dumps meltwater. <strong>Detect:</strong> runtime with no "
        "condensate flow. <strong>Survive:</strong> filter schedule, defrost-capable units, "
        "desiccant in genuinely cold spaces" + _c("sylvane-desiccant") + "."), tag="slow burn"),
      card("Sensor drifts or lies", p("The controller faithfully chases fiction; the room follows. "
        "<strong>Detect:</strong> monthly cross-check against a decent handheld at canopy height. "
        "<strong>Survive:</strong> two sensors per room and control on the worse reading."), tag="quiet killer"),
      card("Power blip", p("Everything stops; what restarts? Compressors need delay timers, some "
        "dehus wake in standby. A room can look powered and be doing nothing. "
        "<strong>Detect:</strong> post-outage checklist, alarms on a UPS. <strong>Survive:</strong> "
        "test the black-start on purpose, once, before summer does it for you."), tag="test it"),
    ], cols=2),
    callout("key", "Break it on purpose",
      p("Once per cycle, in early veg when stakes are low: kill each climate unit for an hour and "
        "watch the trends. You&rsquo;ll learn your real runway (minutes? hours?), whether the "
        "alarms fire, and whether the auto-restarts work. Cheap insurance, and the only way to "
        "know your N+1 is real rather than nameplate.")),
  ]})

# ---------------------------------------------------------------- 13 controls
SECTIONS.append({"id": "controls", "kicker": "13 · Controls", "title": "HVAC staging and deadbands",
  "blocks": [
    p("A grow room runs heating, cooling and dehumidification within metres of each other, and "
      "two of the three make the third&rsquo;s job worse: cooling raises RH; dehumidifying adds "
      "heat. Un-coordinated, they fight, the AC overcools, RH climbs, the dehu heats, the "
      "AC returns, around and around, burning power and cycling compressors. The cure is "
      "sequencing, not bigger hardware."),
    figure(L.flow("The control loop, staged",
            [("Sense", "Aspirated T + RH probe at canopy height"),
             ("Compare", "Against day or night setpoint and deadband"),
             ("Stage", "Cool, then dehu, then heat - one leads"),
             ("Hold", "Minimum run + rest timers stop short-cycling"),
             ("Log", "Trend everything - the graph is the tuning tool")],
            note="One writer per variable: a single controller owns each decision, or your AC and dehu will fight each other all night."), 11,
      "The loop every decent controller implements. The deadband, the tolerance around the "
      "setpoint where nothing switches. Is what gives each machine room to finish its job "
      "before the next one starts."),
    ul([
      "<strong>Deadbands:</strong> control to a band, not a knife-edge. Day 26 &deg;C &plusmn;0.5, "
      "RH 55&ndash;60% is a structure (yours will differ, setpoints belong to the crop, "
      "see the <a href='temp-humidity-vpd.html'>VPD paper</a>; cannabis photosynthesis runs "
      "happily around 25&ndash;30 &deg;C" + _c("chandra2008-photo") + "). Tight bands feel "
      "professional and mostly buy you equipment cycling.",
      "<strong>Sequencing:</strong> heat and cool must never run together (lockout between them); "
      "dehumidification may run alongside either, but its reheat should come from the machine"
      ", hot-gas reheat, not from the heaters fighting the AC" + _c("streit2023-hvacd") + ".",
      "<strong>Day/night setpoints with ramps:</strong> separate targets for lights-on and "
      "lights-off, connected by 15&ndash;30 minute ramps so the transition is driven, not endured "
      "(Section 09).",
      "<strong>Control moisture on dew point where you can:</strong> %RH swings with every "
      "temperature wobble even when the water content hasn&rsquo;t changed; dew point tracks the "
      "actual grams. At the day/night transition, dew-point control is dramatically calmer.",
      "<strong>Sensor placement is a control decision:</strong> an aspirated or well-shielded "
      "sensor at canopy height, out of any supply jet or dehu plume. The controller can only be "
      "as honest as its sensor (Section 12&rsquo;s quiet killer).",
    ]),
  ]})

# ---------------------------------------------------------------- 14 efficiency
SECTIONS.append({"id": "efficiency", "kicker": "14 · The power bill", "title": "HVAC efficiency, reheat and heat recovery",
  "blocks": [
    p("Climate is where the money goes. Energy runs 30&ndash;60% of indoor operating expense"
      + _c("rii-hvac-bpg") + ", and life-cycle analysis of US indoor production found "
      "environmental control the dominant driver of both energy use and emissions, "
      "2,300&ndash;5,200 kg CO&#8322;e per kg of dried flower depending on location"
      + _c("summers2021-ghg") + ". Every design choice in this section moves that number."),
    kv([
      ("1 kW of electricity", "3,412 BTU/h of heat, always"),
      ("1 ton of cooling", "12,000 BTU/h &asymp; 3.52 kW"),
      ("1 US pint", "0.473 L"),
      ("Condensing 1 L of vapour", "&asymp;0.68 kWh of latent heat released at the coil"),
      ("Resistance heater", "COP 1.0 &mdash; the most expensive heat you can buy"),
      ("Modern compressor", "COP 3&ndash;4 &mdash; moves 3&ndash;4 kW of heat per kW consumed"),
    ]),
    ul([
      "<strong>Hot-gas reheat is the flagship move.</strong> Dehumidification means cooling air "
      "below its dew point, then warming it back so you don&rsquo;t overcool the room. Electric "
      "reheat pays full price (COP 1) for heat you just paid to remove. Hot-gas reheat recycles "
      "the compressor&rsquo;s own rejected heat to do the rewarming, near-free reheat, "
      "standard on mid-tier DX and integrated units" + _c("streit2023-hvacd") + ".",
      "<strong>Right-size rather than oversize.</strong> Oversized single-stage equipment "
      "short-cycles: worse dehumidification, worse efficiency, shorter compressor life. Margin "
      "belongs in <em>staged</em> capacity (two circuits, inverter drive), not in one heroic unit.",
      "<strong>LEDs shift the ratio, not the rules.</strong> At equal PPFD, LEDs draw fewer watts, "
      "so the sensible load drops, but the crop transpires much the same, so the latent "
      "load doesn&rsquo;t. LED rooms are latent-dominated rooms: expect the dehumidifier spec, "
      "and the winter heating question, to matter <em>more</em>, not less.",
      "<strong>Reuse heat you already own.</strong> Dehu heat holds the night temperature "
      "(Section 09); condenser heat can pre-warm dry rooms or water. Rejecting heat outside all "
      "winter while running COP-1 heaters inside is a bill you chose.",
      "<strong>Maintenance is an efficiency program:</strong> dirty filters and fouled coils "
      "quietly tax capacity and COP for months before anything actually fails. Filters monthly; "
      "coils each cycle.",
    ]),
  ]})

# ---------------------------------------------------------------- 15 troubleshooting
SECTIONS.append({"id": "trouble", "kicker": "15 · When it goes wrong", "title": "Troubleshooting",
  "blocks": [
    table(["Symptom", "Likely cause", "First moves"], [
      ["RH pins 80%+ every lights-off", "Night latent load exceeds real (derated) dehu capacity; AC idle at night", "Measure water-in minus runoff vs installed capacity at night temp (Sections 05&ndash;07); pre-dry the last hour; add nameplate"],
      ["Room creeps hot all afternoon, AC never stops", "Undersized vs full equipment load, dirty coil/filter, or low refrigerant", "Redo the watt count (Section 06); wash coils, change filters; then call the fridgie"],
      ["AC cycles fast; temp fine, RH never falls", "Oversized single-stage unit short-cycling. Coil never stays cold long enough to condense", "Minimum-run timers; staged/inverter capacity; let dehus own the moisture"],
      ["Room cold <em>and</em> humid (clammy)", "Cooling running without reheat, classic mini-split-as-dehumidifier", "Raise cooling setpoint; add dehu with reheat (or hot-gas reheat unit); heat and dehumidify separately"],
      ["Condensation on ducts/walls at night", "Surfaces below the air's dew point", "More night dehu capacity; raise night temp a touch; insulate cold surfaces; verify with an IR thermometer"],
      ["Dehu runs constantly, tank barely fills", "Room colder than rating point, iced coil, or unit re-breathing its own dry plume", "Check coil for frost and filter for dust; read the capacity curve at your temp; reposition; desiccant if the space is genuinely cold"],
      ["Musty smell, stains below units", "Blocked condensate pans/traps, biofilm in trays", "Clean and disinfect trays; flush drains; float switch working? add to weekly roster"],
      ["One corner always wetter, mould starts there", "Air-distribution dead zone", "Fix supply/return geometry (Section 10); add circulation; thin the canopy; verify with a handheld meter"],
      ["Sensors read fine but buds still rot", "Wall sensor lying about the canopy microclimate", "Measure inside the canopy at cola height; control on dew point; more through-canopy airflow" + _c("punja-budrot-cjb")],
    ], cls="compact", caption="Work top to bottom: measure before replacing hardware. Most &lsquo;broken HVAC&rsquo; is an honest machine obeying a wrong assumption."),
  ]})

# ---------------------------------------------------------------- 16 mental model
SECTIONS.append({"id": "remember", "kicker": "16 · Keep this", "title": "Heat and moisture balance",
  "blocks": [
    callout("key", "The mental model",
      p("A grow room is an accounting problem wearing a plant costume. <strong>Follow the "
        "watt:</strong> every kilowatt of equipment becomes a kilowatt of heat; count them and "
        "you have the sensible load. <strong>Follow the litre:</strong> every litre irrigated, "
        "minus drain, becomes vapour; count them and you have the latent load. The climate plant "
        "is just the return path for both, and it must work at 02:00 in the dark as well as at "
        "14:00 under full light.")),
    ol([
      "Count watts &rarr; sensible load. Folklore counts only the lights; you count everything (Section 06).",
      "Count litres &rarr; latent load. Water in minus runoff, converted to pints for the spec sheet (Sections 05, 07).",
      "Night is the design case: no sensible load, no AC help, transpiration continuing. Size dehumidification for lights-off at <em>your</em> night temperature, derated from nameplate.",
      "N+1 the night dehumidification; interlock the lights to the cooling. Then break each unit on purpose once, and watch what happens.",
      "Control moisture (dew point) with deadbands and sequencing so the machines cooperate; ramp the day/night transition.",
      "Meter irrigation, runoff and condensate, the free, continuous load calculation that also tells you when the crop changes.",
    ]),
    p("The climate plant is one subsystem of the room. Read it alongside the "
      "<a href='grow-room-systems.html'>grow-room systems guide</a>, the "
      "<a href='temp-humidity-vpd.html'>temperature, humidity and VPD paper</a> for what the "
      "setpoints should actually be, and the <a href='airflow-design.html'>airflow design "
      "paper</a> for the last metre of air movement."),
  ]})
