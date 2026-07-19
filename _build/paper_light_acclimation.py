# -*- coding: utf-8 -*-
"""Paper: light acclimation, ramping onto high light without bleaching (beginner)."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        stagecard, grid, card, chip, kv, steps)
import figs_lib as L

SLUG = "light-acclimation"
TITLE = "Light acclimation: raise PPFD in steps so plants don't bleach"
EYEBROW = "Beginner · Light"
SUB = ("Light is a curve, not a switch. Raise PPFD in steps the plant can keep up with, "
       "and match CO2 to set how high you can go. Updated with the latest research (2024-2026) "
       "on high-light quality gains, far-red, and UV.")
META = [("sun", "Beginner"), ("image", "10 diagrams"),
        ("quote", "Evidence-linked · 12 sources"), ("clock", "~11 min read")]
RELATED = ["coco-crop-steering", "signal-and-noise", "plant-state-dashboard"]
REF_IDS = ["rodriguez-morrison-2021-cannabis-light-intensity-yield",
           "chandra-2008-cannabis-photosynthesis-ppfd-co2-temperature",
           "llewellyn-2022-cannabis-yield-proportional-light-uv",
           "moher-2022-cannabis-vegetative-light-intensity-morphology",
           "takahashi-murata-2008-environmental-stress-photoinhibition",
           "pospisil-2016-ros-photosystem-ii-light-temperature",
           "gjindali-johnson-2023-photosynthetic-acclimation",
           "sun-shade-leaf-thickness-chloroplast-acclimation",
           "saetang2024-high-light-metabolites",
           "farred2025-scirep",
           "rfr2024-yield-vs-metabolites",
           "huebner2024-uv-spectra"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

SECTIONS.append({"id": "intro", "kicker": "Start here", "title": "Light is a ramp, not a switch",
  "blocks": [
    lead("Two beginner mistakes cause most light damage in a grow room: blasting weak, "
         "freshly-rooted clones with full-power light, and the opposite, under-lighting "
         "flowering plants out of fear of burning them" + _c("rodriguez-morrison-2021-cannabis-light-intensity-yield") + "."),
    p("Both have the same fix. Light intensity is not an on/off control. It is "
      "something the plant <em>adapts to</em> over weeks. As light rises gradually, the plant "
      "physically rebuilds its light-harvesting machinery to keep pace. Push the intensity up too "
      "fast, or push it too high without enough CO2, and the excess energy stops growing the plant "
      "and starts damaging it: pale, bleached tips and stalled growth."),
    p("The light a plant can take ranges enormously across a full cycle: roughly 80 "
      "&micro;mol/m&sup2;/s for a tender clone up to around 1500 &micro;mol/m&sup2;/s for a "
      "mature, CO2-supplemented flowering canopy" + _c("llewellyn-2022-cannabis-yield-proportional-light-uv") +
      ". This guide covers how plants acclimate, a week-by-week intensity schedule, how high "
      "you can safely go, and how to read the warning signs."),
    figure(L.line("Light is a ramp, not a switch",
            [(0, 90), (1, 250), (2, 400), (3, 550), (4, 700), (5, 850), (6, 1000)],
            ["clone", "veg 1", "veg 2", "veg 3", "flip", "flower", "peak"],
            ylab="PPFD &micro;mol/m&sup2;/s", ymax=1100,
            note="The healthy approach: intensity climbs in steps the plant can keep up with."), 1,
      "A gradual ramp lets the plant build capacity ahead of each new increment of light. A hard "
      "jump to full power, an on/off &lsquo;switch&rsquo;, outruns the plant's ability "
      "to use the photons." + _c("gjindali-johnson-2023-photosynthetic-acclimation")),
    callout("note", "Who this is for",
      p("Anyone who has cooked a clone or been afraid to turn the lights up. Pairs with the "
        "<a href='coco-crop-steering.html'>crop-steering</a> and "
        "<a href='plant-state-dashboard.html'>plant-state dashboard</a> papers.")),
  ]})

SECTIONS.append({"id": "key-terms", "kicker": "Plain-language glossary", "title": "The words you need before we start",
  "blocks": [
    p("These five terms carry the whole guide. Read them once and the rest reads easily. "
      "Each one comes back in context."),
    defterm("PPFD (Photosynthetic Photon Flux Density)", "How bright the usable light is right at "
            "the canopy, measured in &micro;mol/m&sup2;/s (micromoles of light particles per square "
            "metre per second). This is the &lsquo;intensity now&rsquo; number."),
    defterm("DLI (Daily Light Integral)", "The total usable light a plant receives over a whole "
            "day, in mol/m&sup2;/day. It combines intensity (PPFD) with how many hours the lights "
            "are on. It is the day's total &lsquo;dose.&rsquo;"),
    defterm("Photoperiod", "The daily light/dark schedule. 18/6 (18 hours on) is typical for "
            "vegetative growth; switching to 12/12 triggers flowering."),
    defterm("Photoinhibition / bleaching", "Damage that happens when the leaf captures more light "
            "energy than it can use. The surplus energy creates reactive oxygen species that attack "
            "the leaf, leaving pale or white tips."),
    defterm("Acclimation", "The multi-week process where a plant builds more chloroplasts, thicker "
            "protective leaf surfaces, and protective enzymes so it can safely handle higher light."),
    figure(L.flow("PPFD is intensity now; DLI is the day's total",
            [("PPFD", "brightness at the leaf, right now"),
             ("hours on", "how long the lights run"),
             ("DLI", "PPFD x hours = total daily dose")],
            note="Same PPFD on 12/12 delivers far less daily light (DLI) than on 18/6."), 2,
      "PPFD is a snapshot of intensity. DLI is the accumulated total over the day. Changing the "
      "photoperiod changes DLI even when PPFD stays the same."),
  ]})

SECTIONS.append({"id": "how-acclimation-works", "kicker": "The why", "title": "What the plant builds as it adapts",
  "blocks": [
    p("The plant invests in hardware to match rising light. Week over week it builds "
      "more chloroplasts (the tiny green factories that catch light), thicker protective leaf "
      "surfaces, and a higher density of the enzymes that turn captured energy into sugar" +
      _c("sun-shade-leaf-thickness-chloroplast-acclimation") + ". Each new increment of light then "
      "has machinery ready and waiting to use it."),
    p("A plant built only for moderate light cannot absorb a sudden flood of "
      "photons. The light-harvesting side keeps catching energy, but there is nowhere for it to "
      "go. The surplus is converted into <strong>reactive oxygen species</strong>, unstable "
      "molecules that damage the leaf from the inside" + _c("takahashi-murata-2008-environmental-stress-photoinhibition") +
      ". In effect the leaf attacks itself: you see bleached tips and growth grinds to a halt" +
      _c("pospisil-2016-ros-photosystem-ii-light-temperature") + "."),
    p("This is the whole case for incremental ramping. Add light in small steps the plant can keep "
      "pace with, and capacity scales alongside intensity, so every photon becomes sugar instead of "
      "damage" + _c("gjindali-johnson-2023-photosynthetic-acclimation") + "."),
    figure(L.flow("Acclimation climbs in a safe loop",
            [("Small light step", "raise PPFD a notch"),
             ("Build hardware", "more chloroplasts + enzymes"),
             ("Higher capacity", "ready for more light"),
             ("Next step", "repeat, climbing safely")],
            note="Each increment is small enough that the plant's machinery catches up before the next one."), 3,
      "The safe ramp is a loop: a small rise, the plant builds capacity, then the next small rise. " +
      _c("sun-shade-leaf-thickness-chloroplast-acclimation")),
    figure(L.bars("Too fast vs incremental: usable light captured",
            [("Hard jump to full", 35), ("Incremental ramp", 95)], unit="%", maxv=110,
            note="Same final PPFD; the hard jump wastes most of it as damage instead of growth."), 4,
      "A plant flooded before it has acclimated converts much of the light into damage rather than "
      "sugar. A ramped plant captures nearly all of it." + _c("takahashi-murata-2008-environmental-stress-photoinhibition")),
    callout("warn", "Bleaching is self-inflicted damage",
      p("Pale, white-tipped upper leaves are not &lsquo;light hunger&rsquo;. They are the leaf "
        "burning itself with energy it can't use. The cure is less light or more capacity, never more "
        "light.")),
  ]})

SECTIONS.append({"id": "co2-partnership", "kicker": "The why, part two", "title": "Light is the accelerator, CO2 is the fuel",
  "blocks": [
    p("Photosynthesis has two halves. The <strong>light reactions</strong> capture energy from "
      "photons. The <strong>Calvin cycle</strong> then uses CO2 from the air to turn that captured "
      "energy into sugar. Both halves have to scale together" +
      _c("chandra-2008-cannabis-photosynthesis-ppfd-co2-temperature") + "."),
    p("Raise light but leave CO2 low and you trip the same trap as ramping too fast. The light "
      "reactions keep capturing "
      "energy that the Calvin cycle has no CO2 to fix onto anything. The energy backs up and "
      "causes the <em>exact same</em> oxidative bleaching as ramping too fast. You cannot "
      "tell the two mistakes apart by looking at the leaf" + _c("pospisil-2016-ros-photosystem-ii-light-temperature") + "."),
    p("High-light setups demand matched CO2. On ambient air (around 400&ndash;600 ppm "
      "CO2), pushing much above ~850 &micro;mol/m&sup2;/s mostly burns electricity instead of making "
      "sugar" + _c("chandra-2008-cannabis-photosynthesis-ppfd-co2-temperature") + ". To run "
      "1200 &micro;mol/m&sup2;/s you need roughly 1000&ndash;1200 ppm CO2; for 1500, around "
      "1200&ndash;1500 ppm" + _c("rodriguez-morrison-2021-cannabis-light-intensity-yield") + "."),
    figure(L.flow("Low CO2 backs energy up into damage",
            [("Light reactions full", "photons captured fast"),
             ("Calvin cycle starved", "no CO2 to build sugar"),
             ("Energy backs up", "surplus has nowhere to go"),
             ("Bleached leaf", "oxidative damage, pale tips")],
            note="High light + low CO2 produces identical damage to ramping intensity too fast."), 5,
      "When CO2 is the bottleneck, extra light just feeds the damage pathway." +
      _c("takahashi-murata-2008-environmental-stress-photoinhibition")),
    figure(L.zones("Useful PPFD ceiling rises with CO2", 400, 1600,
            [(400, 950, L.GL, "ambient ~950"),
             (950, 1200, L.AMBL, "+CO2 to 1200"),
             (1200, 1500, L.GXL, "full stack 1500")],
            unit="", note="Each higher PPFD band needs the matching CO2 below it, or it just bleaches."), 6,
      "CO2 sets how high PPFD can usefully go. Past your CO2's ceiling, more light is wasted "
      "or harmful." + _c("chandra-2008-cannabis-photosynthesis-ppfd-co2-temperature")),
    callout("key", "One sentence to remember",
      p("Light is the accelerator, CO2 is the fuel. Flooring the pedal with an empty tank doesn't go "
        "faster. It stalls and overheats.")),
  ]})

SECTIONS.append({"id": "ppfd-schedule", "kicker": "The practical schedule", "title": "A week-by-week PPFD ramp by growth stage",
  "blocks": [
    p("A representative indoor cycle runs about 14 weeks (~98 days) and ramps light stage by stage" +
      _c("moher-2022-cannabis-vegetative-light-intensity-morphology") + ". Clones start soft, veg "
      "climbs steadily, and after the flip to flower the plant rebuilds toward its peak before "
      "tapering at the end."),
    p("The 12/12 flip cuts total daily light (DLI) by about one-third (~33%) even at the same PPFD, "
      "simply because the lights are on "
      "fewer hours" + _c("rodriguez-morrison-2021-cannabis-light-intensity-yield") + ". Plan for that "
      "dip rather than panicking and over-cranking the dimmer."),
    figure(L.bars("Daily Light Integral across the cycle",
            [("Clone", 6), ("Veg 1", 16), ("Veg 2", 26), ("Veg 3", 36),
             ("Flip 12/12", 26), ("Flower", 40), ("Peak", 52), ("Ripen", 46)],
            unit="", target=None, maxv=58,
            note="DLI in mol/m2/day. Note the visible dip at the 12/12 flip even though PPFD rose."), 7,
      "DLI climbs through veg, dips at the flip (fewer light hours), then climbs again as flower "
      "PPFD rebuilds." + _c("moher-2022-cannabis-vegetative-light-intensity-morphology")),
    table(["Stage", "Photoperiod", "PPFD range (&micro;mol/m&sup2;/s)", "Notes"], [
      ["Clone", "18/6", "80 &rarr; 300", "Soft and gentle while roots and machinery form"],
      ["Vegetative bulking", "18/6", "300 &rarr; 650", "Ramp roughly +100 per week"],
      ["Flower acclimation", "12/12", "600 &rarr; 950", "Rebuild after the flip's DLI dip"],
      ["Peak flower", "12/12", "950 / 1200 / 1500", "Hold at your control tier's ceiling"],
      ["Maturation", "12/12", "950 &rarr; 850", "Taper slightly as the plant ripens"],
    ], cls="compact", caption="A stage-by-stage ramp. Treat these as starting ranges, not laws. "
       "The peak you hold depends on your CO2 and climate." + _c("rodriguez-morrison-2021-cannabis-light-intensity-yield")),
    callout("tip", "Mind the flip",
      p("The DLI drop at 12/12 is normal and expected. Let early flower re-acclimate from ~600 back "
        "up toward 950 rather than slamming the lights to peak the day you flip.")),
  ]})

SECTIONS.append({"id": "how-high", "kicker": "Setting your ceiling", "title": "How high you push depends on what you control",
  "blocks": [
    p("Your environment sets your safe peak PPFD, not your ambition. The number you can hold is "
      "whatever your CO2, climate and cooling actually support today. Raising the ceiling "
      "means raising the whole system, not just the dimmer."),
    p("On ambient air the honest ceiling is about 950 &micro;mol/m&sup2;/s, with real diminishing "
      "returns above ~850 because there isn't enough CO2 to use the extra light" +
      _c("chandra-2008-cannabis-photosynthesis-ppfd-co2-temperature") + ". A matched intermediate "
      "system supports 1200. The 1500 tier is expert-only and demands the full environmental stack" +
      _c("llewellyn-2022-cannabis-yield-proportional-light-uv") + "."),
    table(["", "Tier 1, Beginner", "Tier 2, Intermediate", "Tier 3, Expert"], [
      ["Peak PPFD", "~950", "1200", "1500"],
      ["CO2 required", "400&ndash;600 ppm (ambient)", "1000&ndash;1200 ppm", "1200&ndash;1500 ppm"],
      ["Prerequisites", "None, just don't exceed ~850 usefully", "Tight VPD + CO2 supplementation",
       "Leaf-temp control + substrate strategy + capable strain"],
    ], cls="compact", caption="Pick the tier your environment actually supports. Below the listed CO2, "
       "the higher PPFD just bleaches for nothing." + _c("rodriguez-morrison-2021-cannabis-light-intensity-yield")),
    figure(L.bars("Peak PPFD each tier can actually use",
            [("Beginner (ambient)", 950), ("Intermediate (+CO2)", 1200), ("Expert (full stack)", 1500)],
            unit="", maxv=1650,
            note="The bar is only useful light if the matching CO2 sits underneath it."), 8,
      "Each tier's ceiling is a whole-system commitment, not just a brighter setting." +
      _c("llewellyn-2022-cannabis-yield-proportional-light-uv")),
    callout("warn", "Don't buy a ceiling you can't fuel",
      p("Running Tier-3 light on Tier-1 air is the most expensive way to bleach plants. Max out the "
        "honest ceiling you can fuel before chasing a higher one.")),
  ]})

SECTIONS.append({"id": "hanging-and-dimming", "kicker": "Doing it physically", "title": "Hanging height and dimming: how you deliver the ramp",
  "blocks": [
    p("Two levers set canopy PPFD: the fixture's <strong>dimmer</strong> and its "
      "<strong>hanging height</strong> above the plants. Both change how much light lands on the "
      "leaves, but they don't behave the same way."),
    p("Dimming is the cleaner lever for fine, repeatable steps. It changes intensity "
      "without changing how widely the light spreads or how much radiant heat reaches the canopy. "
      "Raising or lowering the fixture also shifts the spread and the heat, so it's a coarser "
      "adjustment."),
    p("Whichever lever you use, <strong>verify the real number.</strong> Measure PPFD at the canopy "
      "with a meter, or read it off the fixture's distance chart. Don't trust a wattage or a "
      "dial position. The same fixture reads very differently at different heights. And re-check "
      "whenever the canopy grows toward the light: as plants stretch they get closer to the source, "
      "raising effective PPFD even if you changed nothing."),
    figure(L.flow("Two levers, one verified number",
            [("Dimmer", "fine, repeatable intensity"),
             ("Hanging height", "coarser; shifts spread + heat"),
             ("Measure at canopy", "meter or distance chart"),
             ("Re-check on growth", "stretch raises PPFD on its own")],
            note="Never trust a dial position or wattage; confirm PPFD where the leaves are."), 9,
      "Set intensity with the dimmer, height for spread and heat, and always confirm the canopy "
      "number rather than guessing."),
    callout("tip", "The canopy moves",
      p("A plant that stretched 15 cm toward the light this week is getting noticeably more PPFD even "
        "though you touched nothing. Re-measure after every growth spurt.")),
  ]})

SECTIONS.append({"id": "troubleshooting", "kicker": "Reading the plant", "title": "Signs of too much light, and the traps that cause it",
  "blocks": [
    p("Too much light shows up as <strong>bleached or white tips on the upper canopy</strong>, "
      "the leaves closest to the source, together with stalled growth" +
      _c("pospisil-2016-ros-photosystem-ii-light-temperature") + ". The catch: the same symptom comes "
      "from two different mistakes, and you cannot tell which from the leaf alone."),
    p("Mistake one is ramping intensity too fast. Mistake two is high light with low CO2. Both back "
      "energy up into the same oxidative damage, so they look identical" +
      _c("takahashi-murata-2008-environmental-stress-photoinhibition") + ". Don't try to diagnose by "
      "eye. Prevent both: ramp incrementally <em>and</em> keep CO2 matched to your intensity."),
    table(["Symptom", "Likely cause", "What to do"], [
      ["Bleached / white upper-canopy tips", "Ramped too fast OR high light + low CO2", "Back PPFD down a step; confirm CO2 matches your intensity"],
      ["Bleaching despite &lsquo;safe&rsquo; PPFD", "Out-of-range leaf temp or VPD", "Fix climate first: heat and dry air bleach at safe light"],
      ["Stalled growth at high light", "Capacity hasn't caught up, or CO2 limited", "Hold intensity; let the plant acclimate; check CO2"],
      ["Pale, stretchy, sparse flower", "Chronically under-lit out of fear", "Raise PPFD in steps: under-lighting wastes yield too"],
    ], cls="compact", caption="Same damage, different causes. Prevent both rather than guessing after the fact."),
    callout("danger", "Don't over-correct in fear",
      p("After one bleaching scare, growers often crank flower light far too low and leave yield on "
        "the table. Chronic under-lighting wastes a crop just as surely as bleaching wastes plants" +
        _c("rodriguez-morrison-2021-cannabis-light-intensity-yield") + ". Back down one step, then "
        "climb again deliberately.")),
  ]})

SECTIONS.append({"id": "latest-research", "kicker": "Latest research · 2024-2026", "title": "What the newest studies add",
  "blocks": [
    lead("Acclimation and CO2 matching are the foundation, and they haven't changed. Recent work "
         "(2024-2026) sharpens three things: how much a high ceiling actually buys you, and two "
         "spectrum levers, far-red and UV, that get oversold."),
    p("<strong>A well-fuelled high ceiling improves quality, not just weight.</strong> A 2024 trial "
      "pushing PPFD from 600 to 1200 &micro;mol/m&sup2;/s raised cannabinoid content by about "
      "<strong>60%</strong> and terpenoid content by about <strong>40%</strong>, from <em>both</em> a "
      "heavier inflorescence and higher concentrations, at roughly constant light-use efficiency" +
      _c("saetang2024-high-light-metabolites") + ". Alongside the older result that dry flower yield "
      "rises roughly linearly with PPFD up to ~1800 &micro;mol" + _c("rodriguez-morrison-2021-cannabis-light-intensity-yield") +
      ", the message is consistent: a clean ramp to a high ceiling pays in grade as well as mass "
      "&mdash; <em>provided</em> CO2 and climate keep pace. Without that fuel, the extra light still "
      "just bleaches (Section above)."),
    figure(L.bars("Pushing PPFD 600 -> 1200 (with matched CO2): metabolite gains",
            [("Cannabinoid content", 60), ("Terpenoid content", 40)], unit="%", maxv=70,
            note="From a 2024 trial; gains came from both more inflorescence mass and higher concentrations."), 10,
      "More light, properly fuelled, lifts concentration as well as weight &mdash; it is a quality lever, "
      "not only a yield one." + _c("saetang2024-high-light-metabolites")),
    p("<strong>Far-red is a dosed scalpel, with a trade-off.</strong> End-of-day far-red can shorten the "
      "photoperiod (12 to 10 hours, around 5.5% energy saving) and lift cannabinoid yield in <em>some</em> "
      "cultivars &mdash; one strain showed roughly a 70% jump in total cannabinoid yield" +
      _c("farred2025-scirep") + ". But pushing far-red across the whole spectrum (a lower red-to-far-red "
      "ratio) tends to <em>raise inflorescence mass while diluting</em> cannabinoid and terpene "
      "concentration &mdash; taller, bigger, looser, weaker bud" + _c("rfr2024-yield-vs-metabolites") + ". "
      "Far-red also drives stretch. Treat it as a deliberate, strain-by-strain tool, never a default "
      "&lsquo;more is better&rsquo; spectrum component."),
    p("<strong>UV rarely adds potency in modern cultivars.</strong> Earlier work found supplemental "
      "UV-B did not raise yield or cannabinoid content" + _c("llewellyn-2022-cannabis-yield-proportional-light-uv") +
      ", and a 2024 UV-spectra trial confirmed no cannabinoid gain &mdash; high UV-B actually <em>cut</em> "
      "THC and scorched leaves. Only the lowest UV-A dose nudged the terpene profile (linalool +29%, "
      "limonene +25%, myrcene +22%) while holding yield" + _c("huebner2024-uv-spectra") + ". Modern "
      "high-THC genetics already run near their ceiling, so don't expect UV to boost potency; at most a "
      "careful low UV-A dose tweaks aroma, and supplemental UV usually costs efficiency."),
    callout("key", "Intensity first, spectrum second",
      p("Get the ramp and the CO2 right before touching spectrum. Far-red and UV are marginal, "
        "trade-off-laden add-ons on top of a dialled-in intensity programme &mdash; not shortcuts around "
        "it. A clean, fully-fuelled climb to your honest ceiling beats any spectrum trick on a "
        "half-acclimated, CO2-starved plant.")),
  ]})

SECTIONS.append({"id": "expectations", "kicker": "Realistic expectations", "title": "What to actually expect from your setup",
  "blocks": [
    p("Light is the schedule, not the whole system. Every PPFD target in this guide assumes the rest "
      "of the environment is in range: leaf temperature around 26&ndash;28&deg;C, VPD of "
      "1.2&ndash;1.5 kPa, adequate root-zone capacity, and a strain that can handle the load" +
      _c("chandra-2008-cannabis-photosynthesis-ppfd-co2-temperature") + ". Push light and CO2 without "
      "those and you get heated, stressed plants, not bigger yields."),
    table(["Required for all tiers", "Target"], [
      ["Leaf temperature", "~26&ndash;28&deg;C"],
      ["VPD (air dryness)", "1.2&ndash;1.5 kPa"],
      ["Root-zone capacity", "Adequate water + oxygen for the demand"],
      ["Strain", "Capable of the intended light load"],
    ], cls="compact", caption="These hold for every tier. Light only pays off when temperature, "
       "humidity and the root zone are also in range."),
    callout("key", "Be honest about your tier",
      p("A clean run at the honest ceiling beats a sloppy run at a higher one. Most beginners are "
        "best served maxing out the ~950 ambient ceiling cleanly, nailing acclimation and CO2 "
        "matching first, before ever chasing 1200 or 1500.")),
    p("Treat light as one input among several. It works only when the rest of the environment "
      "cooperates. Learn to read the whole picture in the "
      "<a href='plant-state-dashboard.html'>plant-state dashboard</a> paper, and how to act on real "
      "signals instead of noise in <a href='signal-and-noise.html'>signal and noise</a>."),
  ]})
