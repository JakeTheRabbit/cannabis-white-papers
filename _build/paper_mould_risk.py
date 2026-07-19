# -*- coding: utf-8 -*-
"""Paper: mould risk, preventing and stopping bud rot (beginner)."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        stagecard, grid, card, chip, kv, steps)
import figs_lib as L
from figs import GL, GXL, AMBL, REDL, BLUL

SLUG = "mould-risk"
TITLE = "Mould risk: preventing and stopping bud rot"
EYEBROW = "Beginner · Mould risk"
SUB = ("Mould is the disease most likely to wipe out a harvest in the final weeks, and the one "
       "that can quietly make your flower unsafe to consume. Learn the conditions it needs, how to "
       "deny them, and what to do the moment you find it.")
META = [("shield", "Beginner"), ("image", "3 diagrams"),
        ("quote", "Evidence-linked · 10 sources"), ("clock", "~15 min read")]
RELATED = ["grow-room-systems", "airflow-design", "tissue-culture"]
REF_IDS = ["punja-budrot-cjb", "punja2025-budrot-epi", "scott2021-pm", "buirs2024-idm",
           "mckernan2016-micro", "alubeed2022-postharvest", "sun2025-drying",
           "benedict2020-cdc", "gwinn2023-mycotoxin", "punja2019-pathogens"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

SECTIONS.append({"id": "start", "kicker": "01, Read this first", "title": "Why mould is the harvest-killer",
  "blocks": [
    lead("You can do everything right for ten weeks and lose it all to grey fuzz in the last two. "
         "Mould thrives in exactly the warm, humid, densely-flowered conditions that also grow big "
         "buds. The worst of it hides <em>inside</em> the bud, where you can't see it until "
         "it's spreading."),
    p("There is also a health stake. Cannabis users have been found to get fungal infections at "
      "about <strong>3.5× more often</strong> than non-users in one claims analysis (absolute rates still low; immunocompromised patients are the high-stakes group)" + _c("benedict2020-cdc") + ", and some "
      "moulds leave behind toxins that survive drying" + _c("gwinn2023-mycotoxin") + ". This isn't "
      "only about yield. It is about safe medicine. This guide assumes you know nothing. Every "
      "term is defined."),
  ]})

SECTIONS.append({"id": "terms", "kicker": "02, The vocabulary", "title": "The words you need",
  "blocks": [
    defterm("Bud rot (Botrytis)", "<em>Botrytis cinerea</em>, a grey mould that rots flowers from "
            "the inside out. The number-one late-flower killer."),
    defterm("Powdery mildew (PM)", "A white, flour-like fungus that coats leaf surfaces. Different "
            "fungus, different look, also serious."),
    defterm("Relative humidity (RH)", "How much water vapour the air holds versus the most it could "
            "hold, as a percentage. High RH is mould's best friend."),
    defterm("Leaf wetness / free moisture", "Actual liquid water on the plant (condensation, "
            "spray). Many mould spores need it to germinate."),
    defterm("Water activity", "How much &lsquo;free&rsquo; water is available in dried flower for "
            "microbes to use. Keep it low in storage and mould can't grow."),
    defterm("Mycotoxin", "A poison made by some moulds (e.g. <em>Aspergillus</em>). It can remain in "
            "the flower even after the mould itself is gone" + _c("gwinn2023-mycotoxin") + "."),
  ]})

SECTIONS.append({"id": "the-two", "kicker": "03, Know the enemy", "title": "The two moulds you'll meet",
  "blocks": [
    grid([
      card("Bud rot, Botrytis", p("Starts deep in a dense cola, often at a stem or where a leaf "
        "meets the bud. You'll see a single leaf go yellow or brown and pull out easily. Inside, the "
        "bud is grey, fluffy and crumbling. Spreads fast in the final weeks" + _c("punja-budrot-cjb") + "."),
        tag="Inside the bud"),
      card("Powdery mildew, PM", p("White, dusty patches on the tops of leaves that wipe off like "
        "flour, then return. Loves moderate temps and stagnant, humid air. Coats leaves and chokes "
        "photosynthesis" + _c("scott2021-pm") + "."), tag="On the leaves"),
    ], cols=2),
    callout("note", "They're not the only ones",
      p("Indoor cannabis also hosts <em>Penicillium</em>, <em>Cladosporium</em>, <em>Fusarium</em> "
        "and <em>Aspergillus</em>" + _c("punja2019-pathogens") + ". Botrytis and PM are the two you'll "
        "meet first and most.")),
  ]})

SECTIONS.append({"id": "conditions", "kicker": "04, The trigger", "title": "The conditions that invite mould",
  "blocks": [
    p("Mould isn't bad luck. It is a recipe. Bud rot takes off when humidity climbs above "
      "about <strong>70%</strong> at moderate temperatures (~17–24&nbsp;°C), especially when there's "
      "free moisture and still air" + _c("punja2025-budrot-epi") + ". Deny the recipe and you deny the "
      "mould."),
    figure(L.zones("Bud-rot risk climbs with humidity", 40, 90,
            [(40, 60, GL, "low risk"), (60, 70, GXL, "watch"),
             (70, 80, AMBL, "high risk"), (80, 90, REDL, "rot likely")],
            unit="% RH",
            note="Canopy humidity, not just the room average. Keep flowering rooms in the green or watch band."), 1,
      "Risk rises steeply past ~70% RH" + _c("punja2025-budrot-epi") + ". The trap: your room sensor can "
      "read 60% while the inside of a fat cola sits much higher."),
    figure(L.flow("How bud rot takes hold",
            [("Spore lands", "in a humid, still bud"), ("Germinates", "needs high RH / moisture"),
             ("Hidden growth", "rots the bud core unseen"), ("Sporulates", "grey fluff, spreads on air")],
            note="By the time you see grey fluff, spores are already airborne. Denying the conditions early is everything."), 2,
      "The infection chain. Almost all of it happens out of sight, which is why prevention beats "
      "cure" + _c("punja-budrot-cjb") + "."),
    callout("danger", "The dense-canopy trap",
      p("A thick, undefoliated canopy traps warm, humid, still air inside itself, a private "
        "climate far wetter than your room reading" + _c("punja-budrot-cjb") + ". Packing plants tight for "
        "yield directly raises rot risk. Spacing and defoliation are mould control, not just tidiness.")),
  ]})

SECTIONS.append({"id": "prevention", "kicker": "05, The routine", "title": "Prevention: the daily routine",
  "blocks": [
    p("Prevention is a handful of boring habits done consistently. This is the whole job:"),
    steps([
      ("Hold humidity down", "Keep flowering RH in the ~45–65% stage-dependent band (mid/late flower often ~45–55%), lower in late flower. A dehumidifier sized to your transpiration load is non-negotiable" + _c("buirs2024-idm") + "."),
      ("Move air through the canopy", "Aim for ~0.5–1.0 m/s of gentle, turbulent air reaching inside the plants, not just over the top" + _c("buirs2024-idm") + ". See the airflow paper."),
      ("Open the canopy", "Defoliate and space plants so air and light penetrate. Density is the silent risk multiplier."),
      ("Avoid free moisture", "No overhead watering or spraying in flower. Prevent condensation by avoiding big temperature swings at lights-off, so surfaces never hit dew point."),
      ("Keep it clean", "Sanitise tools, surfaces and hands. HEPA-filter incoming air to cut the airborne spore count" + _c("buirs2024-idm") + "."),
      ("Scout every day", "In the last few weeks, inspect daily. Catching one rotten bud early can save the room."),
    ]),
  ]})

SECTIONS.append({"id": "scouting", "kicker": "06, The habit", "title": "Scouting: find it before it spreads",
  "blocks": [
    p("Spend five minutes a day in late flower with a bright light, looking <em>into</em> the plants, "
      "not just at them:"),
    ul([
      "<strong>The tell-tale.</strong> A single leaf blade poking from a bud that's gone yellow or "
      "brown and slips out with a gentle tug. Pull it and check the bud beneath for grey fluff.",
      "<strong>Where to look.</strong> The biggest, densest top colas. Spots where a leaf petiole "
      "buries into the bud. Anywhere airflow is weak.",
      "<strong>Powdery mildew.</strong> White dust on upper leaf surfaces that smears like flour.",
      "<strong>Smell.</strong> A musty, hay-like or &lsquo;off&rsquo; smell can precede visible rot.",
    ]),
  ]})

SECTIONS.append({"id": "when-found", "kicker": "07, Damage control", "title": "What to do when you find it",
  "blocks": [
    steps([
      ("Stop and isolate", "Don't fan it around. Hold a bag over the spot, cut well below the rot, and remove it from the room before opening the bag."),
      ("Cut generously", "Bud rot runs further inside than it looks. Take the whole affected bud and a margin of healthy tissue."),
      ("Sanitise", "Clean your tools and hands before touching another plant. Spores travel on everything."),
      ("Fix the cause", "Finding rot means your humidity, airflow or density recipe failed somewhere. Drop RH, add through-canopy air, open the canopy."),
      ("Consider harvest timing", "If rot is spreading fast late in flower, an early harvest of clean material can beat losing it all."),
    ]),
    callout("warn", "Don't try to &lsquo;treat&rsquo; rotted flower into safety",
      p("Once a bud has rotted, it's waste, not something to dry and smoke. Drying lowers "
        "microbe levels but won't undo rot or remove mycotoxins" + _c("sun2025-drying") + ". Prevention is "
        "the only real cure.")),
  ]})

SECTIONS.append({"id": "drying", "kicker": "08, After harvest", "title": "Drying & storage: don't lose it at the finish",
  "blocks": [
    p("Mould can still strike clean flower during a sloppy dry or in storage. The defence is to "
      "drive down available water:"),
    ul([
      "<strong>Dry in controlled conditions:</strong> cool and moderate, with airflow. Drying "
      "itself cuts yeast-and-mould counts substantially" + _c("sun2025-drying") + ".",
      "<strong>Cure and store dry.</strong> Aim for a stable, low water activity. Curing around "
      "~18&nbsp;°C and ~50–55% RH is a defensible target" + _c("alubeed2022-postharvest") + ".",
      "<strong>Glass beats plastic.</strong> Sealed glass jars outperform bags for keeping microbes "
      "down and cannabinoids stable" + _c("sun2025-drying") + ".",
    ]),
  ]})

SECTIONS.append({"id": "health", "kicker": "09, The stakes", "title": "Why &lsquo;looks fine&rsquo; isn't proof",
  "blocks": [
    p("Flower can carry dangerous fungi while looking, smelling and even "
      "<em>testing</em> clean. Standard culture-based mould tests can miss some toxin-producing "
      "<em>Aspergillus</em>" + _c("mckernan2016-micro") + ", and contamination rates across the market are "
      "high and inconsistently regulated" + _c("gwinn2023-mycotoxin") + "."),
    callout("key", "Bottom line on safety",
      p("Prevention in the grow room is your real safety system. Lab testing is a backstop with "
        "real blind spots, not a guarantee. For vulnerable users, mouldy cannabis is a genuine health "
        "risk" + _c("benedict2020-cdc") + ", which is why clean genetics (see "
        "<a href='tissue-culture.html'>tissue culture</a>) and a clean room matter from day one.")),
  ]})

SECTIONS.append({"id": "trouble", "kicker": "10, Quick reference", "title": "Troubleshooting",
  "blocks": [
    table(["You see…", "Likely cause", "Do this"], [
      ["Grey, fluffy, crumbling bud interior", "Botrytis bud rot", "Bag, cut wide, remove from room, sanitise, drop RH + add airflow"],
      ["White flour on leaf tops", "Powdery mildew", "Improve airflow and lower RH, remove worst leaves, treat early" + _c("scott2021-pm")],
      ["Rot appears every run, late flower", "Chronic high canopy humidity / dense plants", "Bigger dehumidifier, defoliate, through-canopy airflow"],
      ["Condensation at lights-off", "Surfaces hitting dew point on the night drop", "Soften the temperature drop, keep air moving"],
      ["Mould in jars after cure", "Stored too wet", "Dry or cure to lower water activity, use sealed glass" + _c("alubeed2022-postharvest")],
    ], cls="compact"),
  ]})

SECTIONS.append({"id": "expect", "kicker": "11, Straight talk", "title": "Realistic expectations",
  "blocks": [
    callout("key", "What to remember",
      ol(["Mould is a <strong>recipe (humidity + still air + density + moisture)</strong>. Remove an ingredient and you remove the risk.",
          "It hides <strong>inside</strong> buds. By the time it's visible, spores are already spreading. Scout daily in late flower.",
          "<strong>Prevention is the only cure.</strong> You cannot make rotted or mycotoxic flower safe after the fact" + _c("sun2025-drying") + ".",
          "<strong>Clean looks and passing tests aren't proof</strong> of safety" + _c("mckernan2016-micro") + "."])),
    p("Mould risk is downstream of your climate and airflow. Read the "
      "<a href='grow-room-systems.html'>systems guide</a> and "
      "<a href='airflow-design.html'>airflow</a> papers to fix the causes, not just the symptoms."),
  ]})
