# -*- coding: utf-8 -*-
"""Paper: automated irrigation system manual, sensor-driven crop steering on Home Assistant (operational)."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        stagecard, grid, card, chip, kv, steps)
import figs_lib as L

SLUG = "irrigation-manual"
TITLE = "Automated irrigation system manual"
EYEBROW = "Precision · Irrigation"
SUB = ("Install, run, and maintain a sensor-driven crop-steering irrigation system on "
       "Home Assistant, explained from zero.")
META = [("gauge", "Precision"), ("image", "11 diagrams"),
        ("doc", "Operational guide"), ("clock", "~14 min read")]
RELATED = ["coco-crop-steering", "root-zone-teros12", "smart-watering-vrwe"]
REF_IDS = ["caplan-2019-drought-cannabis", "yang-2022-rdi-review",
           "topp-1980-dielectric-vwc", "mane-2024-sensor-calibration"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

SECTIONS.append({"id": "what-this-is", "kicker": "Start here", "title": "What this is and what it does",
  "blocks": [
    lead("This is an automated watering system for plants grown in pots of soil-less media. "
         "Sensors buried in each pot measure how wet the media is and how much fertiliser salt it "
         "holds, and the software decides when and how much to water. That replaces watering by hand "
         "or on a &lsquo;dumb&rsquo; timer."),
    p("The whole setup runs inside <strong>Home Assistant</strong>, free open-source "
      "home-automation software that you run yourself, with no cloud account required for the core "
      "system. It controls 6 grow tables at once. The system is built in three layers you can "
      "adopt in order: a time-based irrigation package and a sensor-driven crop-steering integration "
      "that both run today, plus an optional advanced layer (AppDaemon) for fully autonomous decisions."),
    p("The three-layer design lets you <strong>start simple and add intelligence later</strong> "
      "without rebuilding. Run it on a plain timer for the first week while you learn to trust the "
      "sensors, then switch on crop steering once the readings look sane."),
    ul(["Replaces hand-watering and plain timers with sensor-driven decisions across 6 grow tables",
        "Runs on Home Assistant; no cloud account or extra software needed for the core system",
        "Three layers: time-based package, crop-steering integration, and optional AppDaemon autonomy",
        "Start timer-based and add intelligence later without rebuilding"]),
    figure(L.flow("The sensor-to-valve control loop",
            [("Probe reads", "VWC + EC in the pot"), ("Software decides", "is it time to water?"),
             ("Valve opens", "a timed shot runs"), ("Water reaches plant", "media wets up"),
             ("Moisture rises", "loop repeats")],
            note="A closed loop: the system acts, measures the result, and acts again."), 1,
      "The core idea of automation: read the root zone, decide, water, then re-read and repeat. "
      "Everything else in this manual is detail hung off this loop."),
    figure(grid([
        card("Layer 1: Irrigation package", "Time-based scheduling: window, interval, and "
             "shot duration. Runs today. The dependable baseline.", "Runs now"),
        card("Layer 2: Crop-steering integration", "Sensor-driven P0&ndash;P3 phase logic "
             "that sizes shots from VWC and EC. Runs today.", "Runs now"),
        card("Layer 3: AppDaemon", "Fully autonomous phase transitions and decisions. "
             "Optional and not deployed by default.", "Optional"),
      ], cols=3), 2,
      "The three layers stack. Each one adds intelligence on top of the layer below, and you can "
      "stop at whichever level you trust."),
  ]})

SECTIONS.append({"id": "key-terms", "kicker": "Vocabulary", "title": "Key terms, defined from scratch",
  "blocks": [
    p("These are the words this manual uses constantly. You don't need to memorise them, each one "
      "comes back in context."),
    defterm("VWC (volumetric water content)", "How wet the growing media is, shown as a percentage. "
            "60% VWC means water fills 60% of the pot's volume."),
    defterm("EC (electrical conductivity)", "How much dissolved fertiliser salt is in the water "
            "around the roots, measured in mS/cm. It is a proxy for feed strength."),
    defterm("Dryback", "A deliberate, controlled drying-out of the media between waterings, measured "
            "as a drop in VWC. The main steering lever."),
    defterm("Shot", "A single timed burst of irrigation. The system replaces one big daily soak with "
            "several small, sized shots."),
    defterm("Field capacity", "The wettest the media can get before water just drains away. The "
            "default target in this system is 70%."),
    defterm("Substrate", "The growing media itself: coco, rockwool or similar. "
            "<a href='glossary.html#gl-substrate'>Glossary &rarr;</a>"),
    defterm("Solenoid valve", "An electrically operated valve. The relay board switches it on or off "
            "to start and stop water flow to a table."),
    defterm("VPD &amp; crop steering", "VPD (vapour pressure deficit) is how &lsquo;thirsty&rsquo; "
            "the air is. Crop steering is biasing the plant vegetative or generative using irrigation, "
            "climate and light. <a href='glossary.html'>Glossary &rarr;</a>"),
    figure(grid([
        card("Vegetative", "Leafy growth and size. Longer drybacks held wetter overall, lower EC.", "Steer"),
        card("Generative", "Flower, density and resin. Shorter, firmer drybacks, higher EC.", "Steer"),
        card("Runoff", "Water that drains out the bottom of the pot during a shot. Confirms the media "
             "reached field capacity.", "Signal"),
      ], cols=3), 3,
      "A quick reference for the three terms that trip up beginners most: the two steering directions "
      "and what runoff is telling you."),
  ]})

SECTIONS.append({"id": "hardware", "kicker": "The physical kit", "title": "The hardware: what gets wired up",
  "blocks": [
    p("The brain of the valve control is a <strong>KC868 E16S relay board</strong> connected over "
      "Ethernet and running ESPHome firmware. It physically switches every valve: the 6 tables "
      "plus the mains, mainline, and manifold valves."),
    p("Each table has a substrate probe that reads VWC, EC, and temperature over <strong>SDI-12</strong>, "
      "a simple digital protocol for soil sensors. The room is also covered by 4 environmental "
      "sensors, 3 CO2 sensors, 4 AC units, a humidifier, and 4 dehumidifier relays. "
      "<strong>There is no pump switch</strong>: the pump auto-starts on a pressure switch the moment "
      "the mainline valve opens, so water flows tank &rarr; mainline &rarr; table dripper &rarr; plant."),
    callout("note", "Mains and manifold valves are not for feeding",
      p("The mains-water and manifold valves exist only to fill and mix the nutrient tank. The plants "
        "are fed exclusively through the table valves. A few sensors are intentionally not yet "
        "connected, which has safety consequences covered in the last section.")),
    table(["Device", "What it does", "Connection"], [
      ["KC868 E16S relay board", "Switches all valves (tables, mains, mainline, manifold)", "Ethernet / ESPHome"],
      ["Substrate probes (×6)", "Read VWC, EC, temperature, one per table", "SDI-12"],
      ["Environmental sensors (×4)", "Room temperature and humidity", "ESPHome / Wi-Fi"],
      ["CO2 sensors (×3)", "Room CO2 in ppm", "ESPHome"],
      ["AC units (×4)", "Cooling", "Relay / IR"],
      ["Humidifier", "Raises room RH", "Relay"],
      ["Dehumidifiers (×4)", "Lower room RH, staggered", "Relay"],
      ["Lights", "Photoperiod, sets lights-on window", "Relay / schedule"],
    ], cls="compact", caption="The physical kit. The relay board is the single point that turns "
      "software decisions into open and closed valves."),
    figure(L.flow("The water-flow path",
            [("Nutrient tank", "mixed feed waits"), ("Mainline valve", "opens, pump auto-starts"),
             ("Mainline pipe", "pressurised"), ("Table valve", "opens for one table"),
             ("Drippers", "to each plant"), ("Runoff", "drains away")],
            note="No pump switch: the pressure switch starts the pump when the mainline opens."), 4,
      "Water only moves when both the mainline and a table valve are open. The pump never runs dry "
      "because it keys off mainline pressure, not a software command."),
  ]})

SECTIONS.append({"id": "phases", "kicker": "The core idea", "title": "The phase logic: P0 to P3",
  "blocks": [
    p("Crop steering splits each lights-on day into four phases that control how the plant uses water "
      "and nutrients. A <strong>controlled dryback</strong>, letting the media dry by a set amount "
      "before watering again, is the signal that steers the plant toward vegetative root growth or "
      "generative flower production." + _c("yang-2022-rdi-review")),
    p("<strong>P0 (morning dryback)</strong> is no watering at all, letting the media dry from "
      "overnight. It moves to P1 once VWC drops by the target amount (50% in vegetative, 40% in "
      "generative) or after a 120-minute cap. <strong>P1 (ramp-up)</strong> gives progressively "
      "larger shots, starting at 2% of substrate volume and rising 0.5% each shot, 15 minutes apart, "
      "up to 10 shots, until VWC hits roughly 65%."),
    p("<strong>P2 (maintenance)</strong> holds the media steady with top-up shots when VWC drops "
      "below 60%, and nudges that threshold up or down based on EC: if the EC ratio exceeds "
      "1.2 it waters more to flush salts, and below 0.8 it lets the media dry to concentrate nutrients. "
      "<strong>P3 (pre-lights-off)</strong> is emergency-only watering below 40% VWC before an "
      "overnight dryback resets the cycle."),
    callout("key", "Vegetative vs generative steering",
      ul(["<strong>Vegetative</strong> steering uses shorter drybacks and lower EC to encourage root "
          "and leaf growth.",
          "<strong>Generative</strong> steering uses longer drybacks and higher EC to apply more "
          "water and osmotic stress. The cited cannabis trial used one cultivar and one 11-day "
          "late-flower drought event, so it supports the direction of the response, not universal "
          "daily targets." + _c("caplan-2019-drought-cannabis"),
          "The same P0&ndash;P3 framework runs both. Only the dryback targets and EC change."], "tight")),
    figure(L.flow("The daily phase cycle",
            [("P0", "dryback &rarr; hit target"), ("P1", "ramp up &rarr; ~65% VWC"),
             ("P2", "maintain &rarr; lights-off nears"), ("P3", "hold &rarr; lights-on")],
            note="Each arrow fires on a trigger: dryback target, field-capacity target, lights-off, lights-on."), 5,
      "The cycle loops every day. P3 hands back to P0 overnight, and lights-on restarts the ramp."),
    figure(L.line("A day of VWC: the steering sawtooth",
            [(0, 62), (1, 55), (2, 50), (3, 58), (4, 64), (5, 62), (6, 61), (7, 63), (8, 55)],
            ["lights on", "P0 end", "P1 start", "P1", "P1 end", "P2", "P2", "P2", "P3 / dark"],
            ylab="VWC %", ymin=40, ymax=72,
            note="Morning dip (P0), stepped rise (P1), steady sawtooth (P2), then overnight decline (P3)."), 6,
      "The shape you are steering for: a clean morning dryback, a controlled refill, a flat-ish "
      "maintenance band, then a fall before dark."),
    figure(L.zones("EC ratio decides the P2 watering threshold", 0.5, 1.6, [
            (0.5, 0.8, L.BLUL, "dry down, concentrate"),
            (0.8, 1.2, L.GL, "hold, steady"),
            (1.2, 1.6, L.REDL, "water more, flush salts"),
          ], unit=" ratio",
          note="EC ratio = measured EC ÷ target EC. The system self-adjusts the P2 trigger inside these bands."), 7,
      "P2 is not a fixed threshold: the system reads how salty the root zone is and lets it dry to "
      "concentrate feed, or waters extra to flush, keeping EC in range." + _c("yang-2022-rdi-review")),
  ]})

SECTIONS.append({"id": "environment-and-safety", "kicker": "Climate and protection",
  "title": "Environment control and the safety net",
  "blocks": [
    p("The system manages room climate as well as watering. Dehumidifiers turn on when humidity is 5% "
      "above target (the 4 relays stagger on with 10-second delays to avoid an inrush spike) and off "
      "2% below. The humidifier mirrors that logic. CO2 injects when 50 ppm below target and only "
      "during lights-on, always closing at lights-off."),
    p("Several independent safety layers run in parallel so that one failure never leaves valves open. "
      "The <strong>master gate</strong> only allows irrigation when the system is enabled, not in "
      "maintenance mode, no leak detected, tank OK, and the clock is inside the time window. A "
      "<strong>valve watchdog</strong> force-closes any table valve open longer than 3 minutes, a "
      "daily 3 AM audit closes everything as a reset, and maintenance mode shuts all valves instantly."),
    callout("warn", "Defence in depth",
      p("No single check is trusted on its own. If the master gate logic ever passed a bad decision, "
        "the valve watchdog and the daily audit would still close the valves. Treat these layers as "
        "non-negotiable and do not disable them to &lsquo;simplify&rsquo; the system.")),
    table(["Protection", "What it does", "Automatic?"], [
      ["Master gate", "Blocks all irrigation unless enabled + not-maintenance + no-leak + tank-OK + in-window", "Yes"],
      ["Valve watchdog", "Force-closes any table valve open over 3 minutes", "Yes"],
      ["Mains watchdog", "Force-closes the mainline valve open over 24 minutes", "Yes"],
      ["Leak abort", "Stops all irrigation if a leak is detected", "Yes (when sensor fitted)"],
      ["Tank-low abort", "Stops irrigation if the tank float reads low", "Yes (when sensor fitted)"],
      ["Maintenance mode", "Closes all valves instantly; blocks new shots", "Manual toggle"],
      ["Sensor-offline alert", "Warns when a probe or device drops offline", "Yes"],
      ["Daily 3 AM audit", "Force-closes all valves and CO2 as a daily reset", "Yes"],
      ["CO2 lights-off close", "Always stops CO2 injection at lights-off", "Yes"],
    ], cls="compact", caption="The safety layers. Two of them (leak, tank-low) only fire once their "
      "physical sensors are installed. See the final section."),
  ]})

SECTIONS.append({"id": "commissioning", "kicker": "Step by step",
  "title": "Commissioning: getting it running from scratch",
  "blocks": [
    p("Bring the system up in order so each layer is proven before the next one is switched on. "
      "Rushing straight to crop steering on unverified hardware is the fastest way to flood a table."),
    steps([
      ("Verify hardware", "Confirm every probe and the relay board show <strong>Online</strong> in "
       "ESPHome. Check a table VWC sensor reads a sensible number (e.g. 47.4), not a dash or zero."),
      ("Test every valve", "Manually click each valve on, then immediately off, to confirm it "
       "responds. Toggle the mainline briefly to confirm the pump auto-starts on pressure."),
      ("Set the window", "Set the irrigation window (e.g. start 08:30, 30 min after lights-on; end "
       "18:00, 2 hours before lights-off), interval 60 minutes, duration 60 seconds."),
      ("Enable the system", "From the Command Center, enable the system, switch maintenance mode off, "
       "and enable only the tables you actually want to water."),
      ("Run one test cycle", "Run a single cycle and watch the valves open and close one at a time. "
       "Confirm water reaches the drippers and runoff appears."),
      ("Set climate &amp; steering", "Set day/night temp and humidity targets and a CO2 target. "
       "Optionally choose a steering mode and crop profile once watering is proven."),
    ]),
    table(["Setting", "Conservative starting value"], [
      ["Window start", "08:30 (30 min after lights-on)"],
      ["Window end", "18:00 (2 h before lights-off)"],
      ["Interval", "60 minutes"],
      ["Shot duration", "60 seconds"],
      ["Day / night temp", "26 °C day / 22 °C night"],
      ["Humidity (RH)", "60%"],
      ["CO2 target", "1200 ppm"],
    ], cls="compact", caption="Safe starting setpoints. These are intentionally cautious; tighten "
      "them only after a week of watching the trends."),
  ]})

SECTIONS.append({"id": "daily-operation", "kicker": "Living with it",
  "title": "Day-to-day operation and the dashboard",
  "blocks": [
    p("Daily checks are quick. On the Command Center, all 6 tables should read VWC between 30 and 70%, "
      "EC in your target range (typically 2 to 6 mS/cm by stage), and substrate temperatures 20 to "
      "26 °C, with every safety indicator green."),
    p("On the Trends tab the VWC graph should show a <strong>sawtooth</strong>: a gradual drop, then a "
      "sharp rise after each irrigation. A flat or only-falling line means watering is not actually "
      "happening. That is your first warning sign, before any error message appears."),
    ul(["Healthy daily readings: VWC 30&ndash;70%, EC ~2&ndash;6 mS/cm, substrate temp 20&ndash;26 °C, safety all green",
        "A non-sawtooth VWC trace is your earliest signal that something is wrong",
        "Enable or skip tables via the <strong>Enabled</strong> toggle in Zone Control",
        "Durable stop: enable Maintenance Mode and disarm the system; an output-off script alone is not a latched emergency stop"]),
    table(["Tab", "What it shows", "When to use it"], [
      ["Command Center", "All tables at a glance: VWC, EC, temp, safety", "Daily health check"],
      ["Zone Control", "Per-table enable toggles and manual valves", "Add or skip a table"],
      ["Trends", "VWC / EC graphs over time", "Confirm the sawtooth; diagnose"],
      ["Environment", "Room temp, RH, CO2 and their targets", "Tune climate"],
      ["Schedule", "Window, interval, duration settings", "Adjust timing"],
    ], cls="compact", caption="The five dashboard tabs. Most days you only open Command Center and "
      "Trends; the rest are for changes."),
    figure(L.line("Healthy sawtooth vs a problem trace",
            [(0, 62), (1, 54), (2, 63), (3, 55), (4, 64), (5, 56), (6, 63), (7, 55)],
            ["t0", "t1", "t2", "t3", "t4", "t5", "t6", "t7"],
            ylab="VWC %", ymin=30, ymax=72,
            note="Each sharp rise is a successful shot. A line that only falls means no water is reaching the table."), 8,
      "The healthy pattern: repeated drop-then-refill. If your trace falls steadily with no rises, "
      "treat it as a fault and check the troubleshooting matrix."),
  ]})

SECTIONS.append({"id": "troubleshooting", "kicker": "When it breaks", "title": "Troubleshooting and tuning",
  "blocks": [
    p("Most problems are diagnosable from a short checklist. Work top to bottom, because the cheapest "
      "checks (is it on? is the window open?) catch the most cases."),
    p("If irrigation will not run, confirm the system is on, maintenance mode is off, the clock is "
      "inside the window, at least one table is enabled, and the irrigation-allowed binary sensor "
      "reads <strong>on</strong>. If VWC or EC shows Unavailable, check the ESPHome device is online "
      "and reload template entities. If the raw probe value is also missing, the probe has lost its "
      "connection. Reliable VWC depends on a working dielectric sensor, so a flatlined raw value "
      "points at the probe, not the software." + _c("topp-1980-dielectric-vwc")),
    callout("tip", "Tune slowly",
      p("Run time-based scheduling for about a week while watching VWC trends before switching to "
        "sensor-driven crop steering. Confirm the sensors track reality first. Calibration "
        "drift in cheap probes is common and skews every decision built on top of it." + _c("mane-2024-sensor-calibration"))),
    table(["Symptom", "Likely cause", "First action"], [
      ["Irrigation won't run", "System off, maintenance on, outside window, or no table enabled",
       "Check system on, maintenance off, inside window, a table enabled, irrigation-allowed sensor on"],
      ["VWC / EC Unavailable", "ESPHome device offline or template entity stale",
       "Confirm device online, reload template entities, then suspect a lost probe connection"],
      ["Shots show 0.0 s", "Substrate volume or dripper flow not set; known prefix bug",
       "Set substrate volume (10 L) and dripper flow (2 L/hr); check for crop_steering_ prefix bug"],
      ["Stuck-open valve", "Relay latched or watchdog not firing",
       "Maintenance mode first, turn the valve off via service, then cut power to the relay board"],
      ["Entity not found", "Integration looking for crop_steering_ prefixed entities",
       "Verify entity IDs match; the known prefix bug can hide volume / flow-rate inputs"],
    ], cls="compact", caption="The five common failures. The 0.0-second-shot and entity-not-found "
      "rows often share the same root cause (a missing or mis-prefixed input)."),
    table(["Parameter", "Meaning", "Default", "How to measure"], [
      ["Substrate volume", "Litres of media per pot", "10 L", "Pot volume × fill fraction"],
      ["Dripper flow rate", "Water delivered per dripper per hour", "2 L/hr", "Stamped on the dripper / catch test"],
      ["Drippers per plant", "How many emitters feed one plant", "1&ndash;2", "Count physically"],
      ["Field capacity", "Wettest VWC before runoff", "70%", "Saturate, drain, read the sensor"],
    ], cls="compact", caption="The tuning parameters. Shot duration is computed from these, so a wrong "
      "substrate volume or flow rate produces wrong (or zero) shot times."),
  ]})

SECTIONS.append({"id": "expectations", "kicker": "Reality check", "title": "Realistic expectations and limits",
  "blocks": [
    callout("key", "This is guidance, not a guarantee",
      p("The core system automates timing and sensor-driven decisions, but it is only as good as its "
        "sensors and plumbing. Until the tank float switch and leak sensor are physically installed, "
        "the tank-low and leak emergency aborts are <strong>hardcoded permissive and will not "
        "trigger</strong>. This is fail-open behaviour, not a safety layer, so do not run the system "
        "unattended in that state.")),
    p("Two more honest limits. Without a leaf-temperature sensor, VPD falls back to room air "
      "temperature and is less accurate. The fully autonomous P0&ndash;P3 phase transitions need "
      "the optional AppDaemon layer, which is not deployed by default. Budget about a week of "
      "supervised, timer-based running before you trust the automation."),
    table(["Not-yet-connected sensor", "Impact while missing"], [
      ["Tank float switch", "No tank-low abort: pump can run a dry tank"],
      ["Leak sensor", "No leak abort: a leak will not stop irrigation"],
      ["Tank pH / EC probes", "Tank pH and EC show Unavailable; mix by hand"],
      ["Leaf-temperature sensor", "VPD falls back to room air temp; less accurate steering"],
    ], cls="compact", caption="What is not safe yet. Install the float and leak sensors before any "
      "unattended run. Everything else degrades gracefully, but these two remove real protection."),
    p("Start by reading one normal day on the Trends tab, then change one thing at a time. For the "
      "biology behind the dryback and the P0&ndash;P3 rhythm, read the "
      "<a href='coco-crop-steering.html'>crop steering in coir</a> paper; for how the probe actually "
      "measures the root zone, see the <a href='root-zone-teros12.html'>root-zone sensor</a> guide."),
  ]})
