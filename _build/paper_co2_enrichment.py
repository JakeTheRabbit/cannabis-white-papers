# -*- coding: utf-8 -*-
"""Paper: CO2 enrichment for cannabis, how it works and how to do it safely (beginner to advanced)."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        stagecard, grid, card, chip, kv, steps)
import figs_lib as L

SLUG = "co2-enrichment"
TITLE = "CO2 enrichment: feeding the plant carbon, safely"
EYEBROW = "Environment & climate · CO2"
SUB = ("Carbon dioxide is the raw material a plant turns into sugar. Under strong light an indoor crop "
       "can use far more CO2 than the air provides, so adding it can lift yield by around a third. But CO2 "
       "only helps in the light, it is easy to waste, and at the wrong concentration it will erase the "
       "plants' returns or kill the people in the room. This is how it works, how much to add and when, "
       "and how to do it without hurting anyone.")
META = [("spark", "Core concept to safe setup"), ("image", "6 diagrams"),
        ("quote", "Peer-reviewed + safety standards · 24 sources"), ("clock", "~26 min read")]
RELATED = ["grow-room-systems", "airflow-design", "harvest-dry-trim-cure"]
REF_IDS = [
    "chandra2008-photo", "tolbert1995-compensation", "noaa2024-co2", "chandra2011-co2",
    "rm2021-light", "westmoreland2023-usu", "doddrell2023-co2", "amthor2024-respiration",
    "collalti2019-npp", "atkin2003-q10", "ahdb-co2", "wang2022-co2cue", "lv2022-topt",
    "kitaya2004-airvel", "kader2002-respiration", "permentier2017-co2poison", "osha-pel-co2",
    "niosh-co2", "worksafenz-co2", "azuma2018-cognition", "ifc5307", "sensirion-scd",
    "winsen-mq", "okstate-co2",
]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

# ---------------------------------------------------------------- 01
SECTIONS.append({"id": "start", "kicker": "01 · Read this first", "title": "CO2 is food, but only in the light",
  "blocks": [
    lead("A plant builds itself out of air. The carbon in every leaf, stem and flower comes from carbon "
         "dioxide (CO2) pulled out of the room and welded to water using the energy in light. Give a "
         "bright canopy more CO2 than the ~420 ppm in normal air and it can build faster, which is why "
         "growers add it. But CO2 enrichment is one of the easiest things in the room to get dangerously "
         "wrong."),
    callout("key", "The five things this paper comes down to",
      ul(["<strong>CO2 is only used in the light.</strong> In the dark the plant does the opposite, it "
          "breathes CO2 out. Injecting at night is pure waste and a safety risk.",
          "<strong>It only pays under strong light.</strong> CO2 and light limit each other. Under weak "
          "light, adding CO2 does almost nothing" + _c("chandra2008-photo") + ".",
          "<strong>There is a target band, roughly 1,000&ndash;1,500 ppm.</strong> Below it you leave "
          "yield on the table, above it you waste gas for no gain" + _c("westmoreland2023-usu") + ".",
          "<strong>You have to seal the room.</strong> In a vented room the CO2 you pay for is blown "
          "straight outside" + _c("wang2022-co2cue") + ".",
          "<strong>It can kill people.</strong> The gas that grows the plant is odourless and, at high "
          "concentration, lethal, and a sealed enrichment room or a drying room can reach that "
          "concentration" + _c("permentier2017-co2poison") + "."])),
    p("Everything below builds on those five. If you only take one thing away: <strong>enrich in the "
      "light, seal the room, and put a CO2 alarm on the wall.</strong>"),
  ]})

# ---------------------------------------------------------------- 02
SECTIONS.append({"id": "terms", "kicker": "02 · The vocabulary", "title": "The words you need",
  "blocks": [
    defterm("CO2 (carbon dioxide)", "The gas plants turn into sugar using light. Normal outdoor air is "
            "about 420 ppm today" + _c("noaa2024-co2") + "."),
    defterm("ppm", "Parts per million. 1,000 ppm means one part CO2 in a thousand of air (0.1%). All the "
            "numbers in this paper are in ppm, and 10,000 ppm = 1%."),
    defterm("Photosynthesis", "The light-powered reaction that combines CO2 and water into sugar. This is "
            "the only process that pulls CO2 <em>into</em> the plant, and it needs light to run."),
    defterm("Respiration", "The plant burning that sugar to live and grow, which releases CO2 back out. It "
            "runs day and night, in every living cell" + _c("amthor2024-respiration") + "."),
    defterm("C3 plant", "Cannabis is a C3 plant, the plant type whose photosynthesis is held back by "
            "today's CO2 level, which is exactly why enrichment helps it."),
    defterm("Photorespiration", "A wasteful side-reaction where the plant's carbon-fixing enzyme grabs "
            "oxygen instead of CO2. More CO2 (and cooler leaves) starves this waste out" + _c("tolbert1995-compensation") + "."),
    defterm("Compensation point", "The CO2 level (~50 ppm for a C3 plant) at which photosynthesis exactly "
            "cancels respiration and the plant makes no net gain" + _c("tolbert1995-compensation") + "."),
    defterm("Saturation point", "The CO2 level above which extra CO2 stops helping. For enrichment this "
            "sits near 1,000&ndash;1,500 ppm."),
    defterm("NDIR sensor", "Non-dispersive infrared, the only cheap sensor type that actually measures CO2 "
            "correctly. Cheap &lsquo;MQ&rsquo; gas sensors do not" + _c("sensirion-scd") + "."),
    defterm("TWA / STEL / IDLH", "Worker-safety limits: the 8-hour average you may breathe (TWA), the "
            "15-minute short spike (STEL), and the level that is Immediately Dangerous to Life or Health "
            "(IDLH)" + _c("niosh-co2") + "."),
  ]})

# ---------------------------------------------------------------- 03
SECTIONS.append({"id": "how", "kicker": "03 · The mechanism", "title": "How CO2 becomes flower",
  "blocks": [
    p("Inside a lit leaf, an enzyme called Rubisco grabs CO2 out of the air and fixes it into sugar. The "
      "trouble is Rubisco is sloppy: it also grabs oxygen by mistake, and when it does it kicks off "
      "<strong>photorespiration</strong>, a reaction that burns energy and throws carbon away. The more "
      "CO2 there is relative to oxygen, the more often Rubisco does its real job instead of the wasteful "
      "one" + _c("tolbert1995-compensation") + "."),
    p("Today's air, at ~420 ppm CO2" + _c("noaa2024-co2") + ", is not enough to keep Rubisco busy. A C3 "
      "plant like cannabis is <strong>CO2-limited</strong>: raise the CO2 and photosynthesis climbs. In "
      "the one classic cannabis gas-exchange study, lifting CO2 from 350 to 750 ppm raised leaf net "
      "photosynthesis by about <strong>50%</strong>" + _c("chandra2008-photo") + ", and a later study "
      "across four high-THC cultivars found gains of <strong>38&ndash;48%</strong> going from 390 to 700 "
      "ppm" + _c("chandra2011-co2") + "."),
    figure(L.bars("More CO2, more photosynthesis (cannabis leaf)",
            [("250 ppm", 50), ("350 ppm", 100), ("750 ppm", 150)], unit="",
            note="Cannabis leaf net photosynthesis, relative to the 350 ppm baseline = 100. Starve it of CO2 and it halves; enrich it and it climbs by half.",
            maxv=170), 1,
      "Cannabis leaf net photosynthesis against CO2. Dropping to 250 ppm cuts it ~50%; raising to 750 ppm "
      "lifts it ~50%" + _c("chandra2008-photo") + ". The response is steep at first, then flattens as other "
      "limits take over."),
    p("The climb does not go on forever. As CO2 rises, photosynthesis stops being limited by CO2 and "
      "starts being limited by how fast the leaf can use the light, so the curve <strong>flattens into a "
      "saturation point</strong>. For most greenhouse C3 crops that plateau is around 1,000&ndash;1,300 "
      "ppm" + _c("doddrell2023-co2") + "."),
    callout("key", "The rule that decides whether CO2 is worth anything",
      p("CO2 and light limit each other, so the weaker one caps the plant (Liebig's law of the minimum). "
        "Adding CO2 under weak light is like flooring the accelerator with the handbrake on, nothing "
        "happens. Cannabis flower yield keeps climbing with light all the way to very high intensity" + _c("rm2021-light") +
        ", so CO2 only earns its keep once the light is already strong.")),
  ]})

# ---------------------------------------------------------------- 04
SECTIONS.append({"id": "daynight", "kicker": "04 · Day and night", "title": "The plant breathes both ways",
  "blocks": [
    p("Here is the fact that trips up beginners. Photosynthesis, the CO2-<em>consuming</em> reaction, only "
      "runs in the light. <strong>Respiration</strong>, the CO2-<em>releasing</em> one, never stops, day "
      "and night, in every living cell" + _c("amthor2024-respiration") + ". During the light period the "
      "big inward pull of photosynthesis swamps the small outward push of respiration, so the canopy is a "
      "net CO2 <em>sink</em>. When the lights go off, photosynthesis stops dead and only respiration is "
      "left, so the same canopy flips to a net CO2 <em>source</em>."),
    figure(L.line("Day and night: the plant breathes both ways",
            [("", 2), ("", 2), ("", 2), ("", -17), ("", -21), ("", -20), ("", -20), ("", -20),
             ("", -19), ("", 3), ("", 2), ("", 2), ("", 2)],
            ["0h", "", "", "06", "", "", "12", "", "", "18", "", "", "24h"],
            ylab="net CO2 flux", ymin=-24, ymax=8,
            note="Schematic canopy net CO2 exchange, lights on 06:00-18:00. Below zero = net uptake (light); above zero = net release (dark)."), 2,
      "The canopy's net CO2 flux over a day. In the light it pulls CO2 in hard; in the dark it gives a "
      "little back. The deep daytime trough dwarfs the shallow night-time bump, and that gap is the whole "
      "point of the next section."),
    p("Respiration also speeds up when it is warm, roughly doubling for every 10&nbsp;&deg;C rise (a Q10 "
      "of about 2)" + _c("atkin2003-q10") + ", and in soil or coco there is extra CO2 from microbes and "
      "roots in the root zone. But none of that changes the headline: <strong>the plant only takes CO2 in "
      "while the lights are on.</strong> That single fact is why you inject in the light and never in the "
      "dark."),
  ]})

# ---------------------------------------------------------------- 05
SECTIONS.append({"id": "massbalance", "kicker": "05 · The mass balance", "title": "Day use vs night release: they don't balance",
  "blocks": [
    p("Growers often ask: if the plant uses CO2 all day and gives it back all night, doesn't it even out? "
      "<strong>No, and the reason it doesn't is the reason enrichment works.</strong> The carbon a plant "
      "fixes in the light does not all get burnt again. Across a season only about half of the carbon "
      "captured by photosynthesis is respired back out; the rest, roughly <strong>46%</strong>, is locked "
      "up as sugar, stem, leaf and flower" + _c("collalti2019-npp") + " (the respired fraction is put at "
      "30&ndash;60% by crop-physiology reviews" + _c("amthor2024-respiration") + "). That retained carbon "
      "<em>is</em> the crop. So the CO2 pulled in during the day always exceeds the CO2 breathed out at "
      "night, by the amount that became plant."),
    p("You can see the asymmetry in a sealed room. With the lights on and no CO2 added, a hungry canopy "
      "strips the air below ambient fast: a tightly sealed glasshouse can fall to <strong>~200 ppm</strong> "
      "within hours, which itself cuts canopy photosynthesis by about <strong>26%</strong>" + _c("ahdb-co2") +
      ". Overnight the same room drifts back up as the plants respire, but the rise is gentle and leakage "
      "caps it."),
    figure(L.line("A sealed room with no added CO2, over 24 hours",
            [("", 620), ("", 520), ("", 450), ("", 430), ("", 230), ("", 205), ("", 200), ("", 200),
             ("", 205), ("", 270), ("", 440), ("", 560), ("", 630)],
            ["0h", "", "", "06", "", "", "12", "", "", "18", "", "", "24h"],
            ylab="room CO2 (ppm)", ymax=720,
            note="Sealed room, no CO2 added. Lights on 06:00. Photosynthesis crashes CO2 toward ~200 ppm; overnight respiration lifts it back over ambient."), 3,
      "Room CO2 in a sealed, unenriched flower room. The lights-on crash is deep and fast; the overnight "
      "recovery is slow and modest. Enrichment exists to fill that daytime hole" + _c("ahdb-co2") + "."),
    callout("note", "The numbers, for a mid-size room",
      ul(["<strong>Lights-on drawdown.</strong> A ~45&nbsp;m&sup2; canopy pulling 15&ndash;25 &micro;mol "
          "CO2 m&sup2;/s strips a sealed ~160&nbsp;m&sup3; room at roughly <strong>350&ndash;600 ppm per "
          "hour</strong> at first, taking 420 down to ~200 ppm in 20&ndash;40 minutes, then slowing as "
          "CO2 runs low.",
          "<strong>Lights-off rise.</strong> The same canopy respiring in the dark adds only about "
          "<strong>25&ndash;70 ppm per hour</strong>, a few hundred ppm over the whole night before "
          "leakage stops it.",
          "<strong>The gap is the crop.</strong> The daytime pull is many times the night-time push, "
          "because about half the fixed carbon stays in the plant instead of being breathed back out" + _c("collalti2019-npp") + "."])),
    p("This is the deeper answer to &lsquo;how much do I need?&rsquo;. Enrichment is not topping up a tank "
      "that empties overnight, it is holding CO2 <em>up</em> during the light hours against a canopy that "
      "would otherwise strip the room bare."),
  ]})

# ---------------------------------------------------------------- 06
SECTIONS.append({"id": "howmuch", "kicker": "06 · The dose", "title": "How much, and what it buys you",
  "blocks": [
    p("The best cannabis-specific yield data come from controlled work at Utah State University: raising a "
      "sealed room from ambient (~420 ppm) to about 1,200 ppm lifted dry flower yield by roughly "
      "<strong>40%</strong>, and 1,200 ppm captured about <strong>95%</strong> of the achievable gain, so "
      "there is little point going higher" + _c("westmoreland2023-usu") + ". General greenhouse crops tell "
      "the same story: tomato yield rises up to ~80% at 1,000 ppm" + _c("doddrell2023-co2") + ", and most "
      "C3 crops saturate around 1,000&ndash;1,300 ppm" + _c("doddrell2023-co2") + "."),
    figure(L.zones("Where to hold CO2 while the lights are on", 200, 2000,
            [(200, 400, L.BLUL, "sub-ambient: starved"), (400, 800, L.GL, "ambient: gains begin"),
             (800, 1500, L.GXL, "enrichment target"), (1500, 2000, L.AMBL, "diminishing / wasteful")],
            unit=" ppm",
            note="Hold roughly 1,000-1,500 ppm during the light period. Below ambient the plant starves; above ~1,500 ppm you pay for gas the plant can't use."), 4,
      "The working band. Aim for roughly 1,000&ndash;1,500 ppm in the light. The plateau above ~1,500 ppm "
      "is real, so pushing to 2,000 ppm mostly buys wasted gas and a bigger safety and cooling "
      "burden" + _c("westmoreland2023-usu") + "."),
    callout("tip", "What CO2 does and doesn't change",
      p("CO2 is a <strong>yield</strong> lever, not a <strong>potency</strong> lever. It grows more flower "
        "mass, so grams of cannabinoid per plant go up, but it does not meaningfully raise %THC or %CBD, "
        "and its effect on terpenes is minor. Expect a bigger harvest, not stronger flower.")),
    callout("warn", "About the &lsquo;39% biomass, 43% flower&rsquo; figures you'll see quoted",
      p("Those exact numbers, and most &lsquo;20&ndash;40% uplift&rsquo; claims, circulate on vendor blogs "
        "without a controlled trial behind them. The trustworthy primary source is the Utah State work "
        "above, which lands around a ~40% flower-yield gain at 1,200&ndash;1,400 ppm" + _c("westmoreland2023-usu") +
        ". Treat anything more precise from a seller as marketing until you see the study.")),
  ]})

# ---------------------------------------------------------------- 07
SECTIONS.append({"id": "delivery", "kicker": "07 · Getting it in", "title": "Delivery and dosing",
  "blocks": [
    p("There are four common ways to put CO2 in a room, and for a sealed indoor cannabis room one of them "
      "clearly wins:"),
    table(["Method", "How it works", "Watch out for"], [
      ["Compressed / bottled CO2", "Cylinder &rarr; regulator &rarr; solenoid valve, gated by an NDIR controller",
       "Cleanest option, no heat or byproducts, precise. Preferred for sealed rooms. Cylinders run out, so plan swaps"],
      ["Propane / gas burner", "Burns fuel to make CO2 (~3&nbsp;lb CO2 per lb fuel)",
       "Cheap gas, but adds heat and water vapour, and a poor flame makes carbon monoxide, ethylene and NOx that harm plants and people. Needs a CO alarm"],
      ["Fermentation / yeast", "Sugar + yeast &rarr; CO2 + alcohol",
       "Tiny, uncontrolled output. Hobby scale only"],
      ["Dry ice", "Solid CO2 sublimes into gas",
       "Uncontrolled, short-lived, and a cold-burn / confined-space hazard"],
    ], cls="compact", caption="For a sealed licensed room, compressed CO2 on a sensor-driven controller is the standard choice."),
    callout("key", "The dosing formula",
      p("To raise a sealed room, work in milligrams: <strong>mass of CO2 (mg) = room volume (m&sup3;) "
        "&times; rise wanted (ppm) &times; 1.8</strong>. The 1.8 is the mass of CO2 in a cubic metre per "
        "ppm at room temperature (CO2 is 1.799&nbsp;g/L at 25&nbsp;&deg;C, so 1 ppm = 1.8&nbsp;mg/m&sup3;)" + _c("niosh-co2") +
        ". <em>Worked example:</em> a 30&nbsp;m&sup3; room from 420 to 1,200 ppm (a 780 ppm rise) needs "
        "30 &times; 780 &times; 1.8 = 42,120&nbsp;mg &asymp; <strong>42&nbsp;g</strong> of CO2, about "
        "23&nbsp;litres of gas. That is only the one-time charge, a room that leaks needs continuous "
        "top-up on top of it.")),
    p("<strong>Timing and distribution.</strong> Inject only during the light period, typically starting "
      "about an hour after lights-on and stopping before lights-off" + _c("wang2022-co2cue") + ". Drive it "
      "from an NDIR CO2 sensor at canopy height holding a setpoint, not a blind timer. Because CO2 is "
      "denser than air it sinks, so run the supply line above the canopy and use horizontal airflow (HAF) "
      "fans to mix it down and thin the still, CO2-starved layer that forms right at the leaf" + _c("kitaya2004-airvel") + "."),
    figure(L.flow("Closed-loop CO2 control, lights-on only",
            [("NDIR sensor", "reads CO2 at canopy"), ("Controller", "compares to setpoint"),
             ("Solenoid", "opens if below target"), ("Injection", "CO2 from the cylinder"),
             ("HAF fans", "mix down to the leaf")],
            note="The loop runs only during the photoperiod. In the dark it stays shut, the plant isn't using CO2."), 5,
      "A sensor-driven enrichment loop. The controller injects to hold the setpoint during the light "
      "period and shuts off in the dark."),
  ]})

# ---------------------------------------------------------------- 08
SECTIONS.append({"id": "sealed", "kicker": "08 · Holding it in", "title": "Sealed vs vented: why the room matters more than the gas",
  "blocks": [
    p("Here is where most CO2 money is wasted. An exhaust fan replaces room air with ~420 ppm outdoor air, "
      "so any CO2 you have added decays straight back toward ambient. The loss follows a simple curve: the "
      "richer the room and the faster the air changes, the faster the CO2 leaves. Run an exhaust fan and "
      "the injector at the same time and you are heating money and blowing it out the wall."),
    p("Even a room with the fans off leaks. In measured commercial greenhouses, more than half of the "
      "injected CO2 was lost to structural leakage, with CO2 use efficiency below "
      "<strong>50&ndash;60%</strong> at a 1,000 ppm setpoint" + _c("wang2022-co2cue") + ". That is why "
      "enrichment demands a <strong>sealed room</strong>: instead of exhausting for heat and humidity, you "
      "handle them <em>inside</em> the room, with a recirculating mini-split air conditioner for heat and a "
      "standalone dehumidifier for moisture, so the door stays shut and the CO2 stays in."),
    table(["", "Vented room", "Sealed room"], [
      ["Heat / humidity", "Removed by exhausting air outside", "Removed in-room by AC + dehumidifier"],
      ["CO2 enrichment", "Pointless, blown out with the exhaust", "Holds, so enrichment works"],
      ["Air exchange", "High, many changes per hour", "Low, only leakage"],
      ["When to use it", "No CO2, or CO2 only to prevent daytime depletion", "Any serious enrichment programme"],
    ], cls="compact", caption="Enrichment and exhaust ventilation are opposites. Pick a sealed design before you buy a gram of CO2."),
    callout("tip", "Purge in the dark",
      p("You still need to flush the room sometimes, to reset humidity or clear stale air. Do it at "
        "<strong>lights-off</strong>, when the plants aren't using CO2 anyway, so you never vent gas you "
        "just paid to inject. CO2 pools low, so a floor-level exhaust clears it fastest.")),
  ]})

# ---------------------------------------------------------------- 09
SECTIONS.append({"id": "climate", "kicker": "09 · The knock-on effects", "title": "CO2 changes everything else in the room",
  "blocks": [
    p("Raising CO2 does not act alone, it pulls on the rest of the room. This is the same "
      "&lsquo;inputs travel in convoys&rsquo; idea from the "
      "<a href='grow-room-systems.html'>grow-room systems</a> paper. Change CO2 and three other things "
      "want to move with it:"),
    table(["Lever", "What elevated CO2 does", "What to do about it"], [
      ["Temperature", "Shifts the plant's ideal temperature up a few degrees" + _c("lv2022-topt"),
       "Run warmer, ~28&ndash;30&nbsp;&deg;C instead of ~25&nbsp;&deg;C, <em>if</em> light supports it. Cannabis photosynthesis peaks near 30&nbsp;&deg;C" + _c("chandra2008-photo")],
      ["Stomata &amp; water", "Partly closes the leaf pores: ~42% less stomatal conductance, ~29% less transpiration" + _c("chandra2008-photo"),
       "The plant drinks less per unit growth. Re-check your VPD target, irrigation volume and feed EC"],
      ["Light", "Nothing, unless light is already high" + _c("rm2021-light"),
       "Only enrich rooms running strong light. Otherwise CO2 is wasted"],
      ["Feed", "Less transpiration can let salts concentrate at the root",
       "Watch runoff EC and adjust feed strength"],
    ], cls="compact", caption="Raise CO2, then ask what must move with it. The temperature and water changes are the ones growers most often miss."),
    callout("note", "Why enriched rooms drink less",
      p("Because CO2 partly closes the stomata, the plant loses less water for the same amount of "
        "photosynthesis, so its water-use efficiency roughly <strong>doubles</strong>" + _c("chandra2008-photo") +
        ". Practically, an enriched crop can transpire noticeably less, which changes your humidity load "
        "and can leave substrate wetter than you expect. Don't just copy your old irrigation schedule.")),
  ]})

# ---------------------------------------------------------------- 10
SECTIONS.append({"id": "drying", "kicker": "10 · The hidden hazard", "title": "The drying room: CO2 with no light to burn it",
  "blocks": [
    p("A drying room is the dark side of everything above, literally. You fill a sealed, dark, low-airflow "
      "room with tens or hundreds of kilos of freshly cut biomass, and that biomass keeps "
      "<strong>respiring</strong> for days after harvest, releasing CO2 the whole time, with no "
      "photosynthesis to soak any of it back up" + _c("kader2002-respiration") + "."),
    p("Cut leaf and flower is a fast-respiring tissue, in the same postharvest class as leafy greens and "
      "cut herbs, and warmth speeds it up (that Q10-of-2 again)" + _c("kader2002-respiration") + ". A drying "
      "room held at 15&ndash;18&nbsp;&deg;C with the air barely moving is a near-perfect CO2 trap. Sealed, "
      "planted greenhouses already climb to 600&ndash;1,000+ ppm overnight from living plants" + _c("ahdb-co2") +
      "; a room packed with cut biomass and almost no ventilation can go substantially higher, into the "
      "thousands of ppm and, in the worst unventilated cases, potentially toward percent-level "
      "concentrations."),
    callout("danger", "Treat an unventilated drying room as a confined space",
      p("CO2 is heavier than air, so it pools low, exactly where a person stands, and you cannot smell it. "
        "A sealed drying room that has been shut overnight can hold a dangerous atmosphere at floor level. "
        "Ventilate it before anyone enters, fit a CO2 alarm, and never let someone walk into a closed, "
        "full drying room to &lsquo;just check on it&rsquo; without air exchange running.")),
    callout("note", "An honest limit on the numbers",
      p("No peer-reviewed study has directly measured CO2 inside a cannabis drying room. The mechanism "
        "(respiring biomass in the dark) and the human-safety limits below are rock solid, but the exact "
        "ceiling a given room reaches is an engineering inference, not a measured cannabis value. The right "
        "response is not to guess, it is to <strong>put a meter in your own drying room and find out</strong>. "
        "The full drying environment is covered in the <a href='harvest-dry-trim-cure.html'>harvest, dry, "
        "trim &amp; cure</a> paper.")),
  ]})

# ---------------------------------------------------------------- 11
SECTIONS.append({"id": "safety", "kicker": "11 · The part that can kill you", "title": "CO2 and people: the numbers that matter most",
  "blocks": [
    lead("Read this section even if you skip the rest. Your enrichment setpoint of 1,000&ndash;1,500 ppm is "
         "well below any worker limit and safe for brief occupancy. The danger is not the setpoint, it is a "
         "leaking regulator, an overfilled room, a burner fault, or a sealed drying room, any of which can "
         "reach lethal CO2 while you notice nothing."),
    figure(L.zones("Enrichment sits far below the worker limit", 0, 5000,
            [(0, 420, L.BLUL, "outdoor air"), (420, 1500, L.GL, "enrichment target"),
             (1500, 5000, L.AMBL, "toward the 5,000 ppm 8-hour worker limit")],
            unit=" ppm",
            note="Your grow-room setpoint (green) is 3-5x below the 5,000 ppm worker exposure limit. The problem is never the setpoint, it's a leak that runs away past it."), 6,
      "The normal enrichment band against the occupational limit. Correctly run, enrichment is nowhere "
      "near the danger zone, which is exactly why a runaway leak is so easy to ignore until it isn't" + _c("osha-pel-co2") + "."),
    p("Every major safety authority agrees on the headline number: the 8-hour average a worker may breathe "
      "is <strong>5,000 ppm (0.5%)</strong>, from OSHA in the US" + _c("osha-pel-co2") + ", NIOSH and "
      "ACGIH" + _c("niosh-co2") + ", and WorkSafe New Zealand" + _c("worksafenz-co2") + ". Above that, effects "
      "climb steeply:"),
    table(["CO2 level", "What happens", "Reference point"], [
      ["~420 ppm", "Normal outdoor air", "Baseline" + _c("noaa2024-co2")],
      ["1,000&ndash;1,500 ppm", "Typical enrichment target, safe for short work", "3&ndash;5&times; below the worker limit"],
      ["1,000&ndash;2,500 ppm", "Measurable dip in concentration and decision-making", "Cognition, not danger" + _c("azuma2018-cognition")],
      ["5,000 ppm (0.5%)", "8-hour worker exposure limit (TWA)", "OSHA / NIOSH / ACGIH / WorkSafe NZ" + _c("worksafenz-co2")],
      ["30,000 ppm (3%)", "15-minute short-term limit (STEL); headache, fast breathing", "NIOSH / ACGIH / WorkSafe NZ" + _c("niosh-co2")],
      ["40,000 ppm (4%)", "IDLH, immediately dangerous to life or health", "Escape-impairing" + _c("niosh-co2")],
      ["50,000 ppm (5%)", "Hypercapnia and respiratory acidosis within ~30 min", "Direct poisoning, not just low oxygen" + _c("permentier2017-co2poison")],
      ["70,000&ndash;100,000 ppm (7&ndash;10%)", "Unconsciousness within minutes", "Cannot self-rescue" + _c("permentier2017-co2poison")],
      ["&gt;300,000 ppm (&gt;30%)", "Loss of consciousness in seconds", "Fatal-scene cases 14&ndash;26% CO2" + _c("permentier2017-co2poison")],
    ], cls="compact", caption="The CO2 effect ladder. Note the jump: the enrichment band is safe, but the levels a leak can reach in a sealed room are not."),
    callout("danger", "CO2 is a poison, not just a smothering gas",
      p("It is tempting to think CO2 just crowds out oxygen. It does that, but it is also directly toxic: "
        "above ~5% it acidifies the blood, and forensic reviews conclude the cause of death in CO2 "
        "incidents is the poisoning itself, not the lack of oxygen" + _c("permentier2017-co2poison") + ". "
        "That is why it drops people so fast they can't open a door, and why rescuers who rush in without "
        "protection are so often the second victims. A sealed, high-CO2 room is a confined space. Ventilate "
        "and test the air before entry, every time.")),
  ]})

# ---------------------------------------------------------------- 12
SECTIONS.append({"id": "monitoring", "kicker": "12 · Measuring and alarming", "title": "Sensors, alarms and the MQ trap",
  "blocks": [
    p("You cannot manage or survive CO2 you cannot measure, and the sensor market is full of parts that "
      "don't actually measure it. The correct technology is <strong>NDIR</strong> (non-dispersive "
      "infrared), which reads CO2 by its specific infrared fingerprint" + _c("sensirion-scd") + ". The cheap "
      "&lsquo;MQ&rsquo; metal-oxide sensors sold as CO2 sensors are a trap:"),
    table(["Sensor", "Does it measure CO2?", "Verdict"], [
      ["NDIR (SCD30, SCD41, MH-Z19&hellip;)", "Yes, infrared, CO2-specific", "Correct for both control and safety" + _c("sensirion-scd")],
      ["MQ-135", "No, it infers &lsquo;equivalent CO2&rsquo; from a mix of VOCs", "Not a real CO2 reading, unsuitable" + _c("winsen-mq")],
      ["MQ-5", "No, it's built for LPG / combustible gas", "Wrong gas entirely" + _c("winsen-mq")],
    ], cls="compact", caption="If a &lsquo;CO2 node&rsquo; is built on an MQ-135 or MQ-5, it is not measuring CO2. Only trust NDIR for control and for life safety."),
    callout("warn", "The sealed-room calibration trap",
      p("NDIR sensors drift, so they self-calibrate by assuming the lowest CO2 they ever see is fresh "
        "400&nbsp;ppm air (Automatic Baseline Calibration). In a continuously enriched sealed room the "
        "sensor <em>never</em> sees 400 ppm, so ABC slowly mis-calibrates it downward" + _c("sensirion-scd") +
        ". <strong>Disable ABC and calibrate manually</strong> against fresh air or a reference gas on a "
        "schedule.")),
    p("<strong>Two sensors, two jobs.</strong> Put a control sensor at canopy height to run the setpoint, "
      "and a separate <em>life-safety</em> sensor low on the wall (~30&nbsp;cm off the floor) because CO2 "
      "settles. For larger systems the International Fire Code (Section 5307) makes this mandatory: any "
      "installation over 100&nbsp;lb of CO2 needs gas detection that alarms at 5,000&nbsp;ppm, alarms hard "
      "at 30,000&nbsp;ppm, and automatically shuts off the CO2 and starts ventilation" + _c("ifc5307") + ". "
      "Even below that threshold, an alarm plus an occupancy interlock is cheap insurance."),
  ]})

# ---------------------------------------------------------------- 13
SECTIONS.append({"id": "worth", "kicker": "13 · Straight talk", "title": "Is it worth it, and when it isn't",
  "blocks": [
    p("CO2 is one of the highest-return upgrades in a sealed, high-light room, and a waste of money in any "
      "other" + _c("okstate-co2") + ". The gas itself is cheap; the room around it is what decides the payback."),
    grid([
      card("Enrich when&hellip;",
           ul(["The room is <strong>sealed</strong> (AC + dehumidifier, not exhaust)",
               "Light is already <strong>strong</strong> (high PPFD / DLI)" + _c("rm2021-light"),
               "Temperature, water and feed are dialled in",
               "You have a CO2 <strong>alarm and interlock</strong> fitted"]), tag="worth it"),
      card("Don't bother when&hellip;",
           ul(["The room is <strong>vented</strong>, you'll blow it outside" + _c("wang2022-co2cue"),
               "Light is <strong>low</strong>, CO2 can't be used" + _c("chandra2008-photo"),
               "You'd push past ~1,500 ppm chasing more" + _c("westmoreland2023-usu"),
               "You can't monitor it safely yet"]), tag="skip it"),
    ], cols=2),
    table(["Problem", "Likely cause", "Fix"], [
      ["Added CO2, no extra yield", "Light too low, or the room isn't sealed", "Raise PPFD and seal the room before blaming the gas"],
      ["CO2 won't hold at setpoint", "Room leaks, or exhaust is running during injection", "Seal leaks; only exhaust at lights-off"],
      ["Plants wilting / substrate staying wet", "Enriched plants transpire less, old irrigation is now too much", "Re-tune VPD and cut irrigation volume" + _c("chandra2008-photo")],
      ["Leaf damage with a burner", "Incomplete combustion making CO / ethylene / NOx", "Service the burner, fit a CO alarm, or switch to bottled CO2"],
      ["Sensor reads lower over weeks", "ABC mis-calibrating in a sealed room", "Disable ABC, calibrate manually" + _c("sensirion-scd")],
    ], cls="compact", caption="The usual CO2 failures. Almost all of them are the room, the light or the sensor, not the CO2."),
    callout("key", "The mindset",
      ul(["<strong>Light first, CO2 second.</strong> CO2 amplifies strong light; it can't replace it.",
          "<strong>Seal before you enrich.</strong> An unsealed enrichment room is a money leak.",
          "<strong>Measure with NDIR, alarm for people.</strong> Control and safety are two sensors, not one.",
          "<strong>Enrich in the light, purge in the dark.</strong> The plant only breathes CO2 in while the lights are on."])),
    p("Read the <a href='grow-room-systems.html'>grow-room systems</a>, "
      "<a href='airflow-design.html'>airflow</a> and <a href='harvest-dry-trim-cure.html'>harvest and "
      "dry</a> papers alongside this one, CO2 only makes sense as part of that whole machine."),
  ]})
