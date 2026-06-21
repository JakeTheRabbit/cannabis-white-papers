# -*- coding: utf-8 -*-
"""Paper: the cannabis grow room, a systems guide (beginner)."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        stagecard, grid, card, chip, kv, steps)
import figs_lib as L

SLUG = "grow-room-systems"
TITLE = "The cannabis grow room: a systems guide"
EYEBROW = "Beginner · Grow-room systems"
SUB = ("A grow room is one connected system, not a list of gadgets. Light, heat, humidity, air and "
       "water all pull on each other. Learn to see the whole machine, so a fix in one place doesn't "
       "break another.")
META = [("building", "Beginner"), ("image", "4 diagrams"),
        ("quote", "Peer-reviewed · 10 sources"), ("clock", "~18 min read")]
RELATED = ["coco-crop-steering", "airflow-design", "mould-risk"]
REF_IDS = ["rm2021-light", "faust2018-dli", "collado2025-light", "chandra2008-photo",
           "inoue2021-vpd", "schymanski2016-wind", "malik2025-media", "caplan2019-drought",
           "punja2019-pathogens", "punja-budrot-cjb"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

SECTIONS.append({"id": "start", "kicker": "01 · Read this first", "title": "The room is one machine",
  "blocks": [
    lead("Those four things are one problem, not four. Beginners buy a light, a fan, a humidifier and "
         "a nutrient bottle and treat each as a separate job. Turn the light up and the room gets "
         "hotter, the plants drink more, the air gets more humid, and your dehumidifier works harder. "
         "Everything is connected."),
    p("This guide shows you those connections, so you set things up in the right order instead of "
      "chasing one problem into the next. No prior knowledge needed."),
  ]})

SECTIONS.append({"id": "terms", "kicker": "02 · The vocabulary", "title": "The words you need",
  "blocks": [
    defterm("PPFD", "How bright the usable light hitting the canopy is, measured in µmol/m²/s. "
            "Think &lsquo;brightness right now.&rsquo;"),
    defterm("DLI (daily light integral)", "Brightness × hours the light is on = the total light the "
            "plant gets in a day (mol/m²/day). This is the number that really drives growth" + _c("faust2018-dli") + "."),
    defterm("Transpiration", "The plant pulling water up from the roots and breathing it out through "
            "tiny leaf pores (stomata). It is how the plant stays cool and moves nutrients."),
    defterm("VPD (vapour pressure deficit)", "How &lsquo;thirsty&rsquo; the air is. A single number "
            "from temperature and humidity that sets how fast the plant transpires."),
    defterm("CO2", "Carbon dioxide, the raw material plants turn into sugar with light. More CO2 can "
            "raise growth if light is high enough."),
    defterm("Stomata", "Microscopic adjustable pores on leaves. They open to take in CO2 and let "
            "water out, and they close when the plant is stressed."),
    defterm("Substrate", "What the roots grow in (coco, rockwool, peat). It changes how water, air and "
            "salt behave at the root" + _c("malik2025-media") + "."),
  ]})

SECTIONS.append({"id": "one-system", "kicker": "03 · The big idea", "title": "How it's all coupled",
  "blocks": [
    p("One chain runs your room. Push the first link and every link after it moves:"),
    figure(L.flow("Push the light, and everything downstream moves",
            [("Light", "energy hits the leaf"), ("Leaf heat", "leaf warms, photosynthesis rises"),
             ("Transpiration", "plant drinks & breathes out water"),
             ("Room humidity", "that water vapour fills the room"),
             ("HVAC load", "AC + dehumidifier must remove it")],
            note="More light is more yield, but only if the rest of the chain can keep up."), 1,
      "The coupling chain. This is why &lsquo;just add more light&rsquo; fails if your climate and "
      "airflow can't carry the extra water the plants now transpire." + _c("collado2025-light")),
    callout("key", "The one rule that prevents most mistakes",
      p("Raise one input, then ask &lsquo;what must move with it?&rsquo; More light &rarr; more "
        "transpiration &rarr; more humidity &rarr; more dehumidification and more water and feed. "
        "Inputs travel in convoys, not alone.")),
  ]})

SECTIONS.append({"id": "light", "kicker": "04 · The biggest lever", "title": "Light: set the demand first",
  "blocks": [
    p("Light is the upstream lever: it sets how much of everything else the plant wants. In "
      "cannabis, flower yield climbs roughly <strong>linearly with light</strong> all the way up to "
      "very high intensities (~1800 µmol/m²/s in one study, about a 4.5× yield increase)" + _c("rm2021-light") +
      ". Bright works, as long as you can pay the bills downstream."),
    figure(L.bars("More light, more flower (roughly linear)",
            [("400", 30), ("800", 55), ("1200", 78), ("1600", 96)], unit="",
            note="PPFD (µmol/m²/s) vs relative flower yield. Yield keeps rising where a single leaf would have saturated.",
            maxv=110), 2,
      "Whole-plant yield rises far past where a single leaf stops responding. The canopy "
      "keeps using light the top leaves can't" + _c("rm2021-light") + ". Returns do taper, and very high "
      "light needs matching CO2, climate and water."),
    callout("warn", "Leaf vs canopy: the classic trap",
      p("Measure one leaf and photosynthesis &lsquo;maxes out&rsquo; at modest light, which tempts you to "
        "stop there. The whole canopy keeps converting more light into more flower well "
        "beyond that point" + _c("rm2021-light") + ". Don't set room light by leaf-level numbers.")),
  ]})

SECTIONS.append({"id": "climate", "kicker": "05 · The air", "title": "Climate: temperature, humidity & VPD",
  "blocks": [
    p("Temperature and humidity are not two separate dials. Together they make "
      "<strong>VPD</strong>, which controls how fast the plant transpires. There is a workable "
      "middle band. Too low and everything slows. Too high and the plant shuts its stomata to save "
      "water, stalling CO2 uptake and growth" + _c("inoue2021-vpd") + "."),
    figure(L.zones("VPD: aim for the workable middle", 0.4, 2.0,
            [(0.4, 0.8, L.BLUL, "humid / slow"), (0.8, 1.2, L.GL, "sweet spot"),
             (1.2, 1.6, L.GXL, "generative"), (1.6, 2.0, L.AMBL, "stress: stomata close")],
            unit=" kPa",
            note="Rough guide. The ideal shifts with stage and strain. Steady VPD beats a perfect but jumpy one."), 3,
      "Most growth happens around 0.8–1.2 kPa. Drier air pushes generative, but past ~1.5 kPa the "
      "plant closes up and stops working" + _c("inoue2021-vpd") + "."),
    p("<strong>CO2</strong> is the other climate lever. Adding CO2 raises photosynthesis and "
      "water-use efficiency, and, counter-intuitively, it makes the plant transpire "
      "<em>less</em> and partly close its stomata, not open them" + _c("chandra2008-photo") + ". It only "
      "pays off when light is already high."),
  ]})

SECTIONS.append({"id": "air", "kicker": "06 · Movement", "title": "Airflow ties it together",
  "blocks": [
    p("Moving air does two quiet but vital jobs. It strips away the thin film of still, humid air "
      "that clings to each leaf, and it cools the leaf by convection. Faster air thins that film, "
      "improving CO2 uptake and water-use efficiency while lowering water loss" + _c("schymanski2016-wind") +
      ". It also keeps every plant in the room living in the same climate."),
    callout("note", "Airflow has its own paper",
      p("Boundary layers, fan placement, velocity targets and dead zones are covered in depth in "
        "<a href='airflow-design.html'>Airflow design for indoor cultivation</a>. Here, just know "
        "that without air movement your light, climate and CO2 settings don't reach the leaf evenly.")),
  ]})

SECTIONS.append({"id": "rootzone", "kicker": "07 · The supply", "title": "Root zone: feeding the demand",
  "blocks": [
    p("Everything upstream creates <em>thirst</em>, and the root zone has to satisfy it. The brighter "
      "and drier the room, the more the plant transpires, and the more water and nutrient it needs at "
      "the roots. Your substrate and irrigation are the supply side of the same system" + _c("malik2025-media") + "."),
    p("The root zone is also a steering lever: a controlled root-zone dryback nudges the plant "
      "generative and can raise potency" + _c("caplan2019-drought") + ". The full mechanics are in the "
      "<a href='coco-crop-steering.html'>coco &amp; crop steering</a> paper. The point here is "
      "that irrigation must <em>match</em> the demand the rest of the room is creating, not run on a "
      "fixed timer."),
  ]})

SECTIONS.append({"id": "order", "kicker": "08 · The method", "title": "Set it up in the right order",
  "blocks": [
    p("Inputs are coupled, so the order you set them in matters. Work top-down:"),
    steps([
      ("1. Pick your light target", "Decide the DLI/PPFD you can actually support. This sets the demand for everything else."),
      ("2. Match the climate", "Set temperature and humidity to a sane VPD for that light level, with CO2 if light is high."),
      ("3. Provide the airflow", "Enough movement to mix the room and reach every leaf. See the airflow paper."),
      ("4. Feed to match", "Size irrigation and feed EC to the transpiration the above creates, then steer with dryback."),
      ("5. Then steer & refine", "Only now nudge generative or vegetative, one lever at a time, watching the whole chain."),
    ]),
  ]})

SECTIONS.append({"id": "disease", "kicker": "09 · The hidden cost", "title": "The system can breed disease",
  "blocks": [
    p("The same warm, humid, densely-planted room that grows big plants also grows mould. Bud rot "
      "(<em>Botrytis</em>) takes off above ~70% humidity at moderate temperatures, and a thick canopy "
      "traps humid, still air inside itself where your room sensor never sees it" + _c("punja-budrot-cjb") + "."),
    callout("danger", "Your room sensor is lying to you (a little)",
      p("A sensor in open air can read a comfortable 60% while the inside of a fat cola sits at 85% "
        "and rotting. Airflow through the canopy and sensible plant spacing, not just the room "
        "average, are what keep disease out" + _c("punja2019-pathogens") + ". Full detail in the "
        "<a href='mould-risk.html'>mould risk</a> paper.")),
  ]})

SECTIONS.append({"id": "trouble", "kicker": "10 · When it goes wrong", "title": "Troubleshooting the system",
  "blocks": [
    table(["Symptom", "Where the system broke", "What to do"], [
      ["Room humidity won't come down", "Light/transpiration outran your dehumidification", "Add dehumid capacity or trim light, and improve air exchange"],
      ["Leaf edges curling/taco at high light", "VPD too high, so the plant closed its stomata", "Lower VPD (cooler/more humid), add CO2, verify airflow"],
      ["Big light, disappointing yield", "Climate/CO2/water didn't scale with the light", "Match CO2, VPD and feed to the light level"],
      ["Hot canopy, slow growth", "Airflow too weak, so the leaf can't shed heat", "Increase canopy-level air movement"],
      ["Bud rot in week 6+", "Dense canopy + trapped humidity", "Defoliate/space plants, airflow through the canopy, lower RH"],
    ], cls="compact"),
  ]})

SECTIONS.append({"id": "expect", "kicker": "11 · Straight talk", "title": "Realistic expectations",
  "blocks": [
    callout("key", "The mindset that separates good growers from frustrated ones",
      ul(["Think in <strong>convoys</strong>: change one input and pre-empt what must move with it.",
          "<strong>Match, don't max.</strong> The best room is not the one with the biggest light. It is the one whose parts are balanced for the light it has" + _c("collado2025-light") + ".",
          "Substrate and strain change the right answer. Treat published numbers as starting points, not law."])),
    p("Read the <a href='coco-crop-steering.html'>crop steering</a>, "
      "<a href='airflow-design.html'>airflow</a> and <a href='mould-risk.html'>mould</a> papers next. "
      "They are the subsystems of this one machine."),
  ]})
