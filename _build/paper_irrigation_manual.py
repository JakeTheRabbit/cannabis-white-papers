# -*- coding: utf-8 -*-
"""Paper: automated irrigation system manual, sensor-driven crop steering on Home Assistant (operational)."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        stagecard, grid, card, chip, kv, steps)
import figs_lib as L

SLUG = "irrigation-manual"
TITLE = "Manual for an automatic irrigation system"
EYEBROW = "Precision · Irrigation"
SUB = ("Install, operate, and do maintenance on an irrigation system with sensors for crop "
       "steering, on Home Assistant. The manual starts with the basic information.")
META = [("gauge", "Precision"), ("image", "11 diagrams"),
        ("doc", "Operation manual"), ("clock", "~14 min to read")]
RELATED = ["coco-crop-steering", "root-zone-teros12", "smart-watering-vrwe"]
REF_IDS = ["caplan-2019-drought-cannabis", "yang-2022-rdi-review",
           "topp-1980-dielectric-vwc", "mane-2024-sensor-calibration"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

SECTIONS.append({"id": "what-this-is", "kicker": "Start here", "title": "Purpose and scope",
  "blocks": [
    lead("This system is an automatic irrigation system for plants in pots of soilless substrate. "
         "Sensors in the substrate of each pot measure how wet the substrate is and the quantity of "
         "fertilizer salt in it. The software selects the time of each irrigation and the quantity "
         "of water. The system is an alternative to manual irrigation and to a timer that does not "
         "use sensor data."),
    p("The system operates in <strong>Home Assistant</strong>. Home Assistant is open-source "
      "software for home automation. The software has no cost. You operate it on your equipment. A "
      "cloud account is not necessary for the basic system. The system controls 6 grow tables at "
      "the same time.</p><p>The system has three layers, and you can use the layers one after the "
      "other. The first two layers are in operation. They are an irrigation package that uses a "
      "timer and a crop steering integration that uses sensors. The third layer is optional and has "
      "more functions (AppDaemon). It makes all the decisions without a person."),
    p("The three layers let you <strong>start with the timer and then add the sensor "
      "decisions</strong>. It is not necessary to assemble the system again. For the first week, "
      "operate the system with a timer only, and monitor the sensor readings. When the readings are "
      "correct, start crop steering."),
    ul(["The system is an alternative to manual irrigation and to timers. It uses sensor data for its decisions on 6 grow tables.",
        "The system operates on Home Assistant. A cloud account and more software are not necessary for the basic system.",
        "The three layers are the irrigation package with a timer, the crop steering integration, and the optional AppDaemon layer for decisions without a person.",
        "You can start with the irrigation package that uses a timer, and then add the other layers. It is not necessary to assemble the system again."]),
    figure(L.flow("Control loop from sensor to valve",
            [("Probe reads", "VWC and EC in the pot"), ("Software decision", "time for irrigation?"),
             ("Valve opens", "shot for set time"), ("Water goes to plant", "wet substrate"),
             ("VWC increases", "loop again")],
            note="A closed loop: the system applies water, measures, and applies water again."), 1,
      "The primary part of automation is this loop. The system measures the root zone and makes a "
      "decision. Then it applies water and measures again. Each other part of this manual gives "
      "more information about this loop."),
    figure(grid([
        card("Layer 1: Irrigation package", "Irrigation at set times. The settings are the window, "
             "the interval, and the time of each shot. This layer is in operation. It is the stable "
             "baseline.", "In operation"),
        card("Layer 2: Crop steering integration", "Logic for the P0 to P3 phases that uses sensor "
             "data. It sets the size of each shot from the VWC and EC. This layer is in operation.", "In operation"),
        card("Layer 3: AppDaemon", "The software changes the phases and makes all the decisions "
             "without a person. This layer is optional. The basic system does not include it.", "Optional"),
      ], cols=3), 2,
      "The three layers are one above the other. Each layer adds more automatic decisions to the "
      "layer below it. You can stop at a layer when you are sure that it operates correctly."),
  ]})

SECTIONS.append({"id": "key-terms", "kicker": "Terms", "title": "Definitions",
  "blocks": [
    p("This section gives the terms that this manual uses frequently. It is not necessary to know "
      "the terms at this time. Each term occurs again in this manual."),
    defterm("VWC (volumetric water content)", "The quantity of water in the substrate, in percent. "
            "If the VWC is 60%, water fills 60% of the volume of the pot."),
    defterm("EC (electrical conductivity)", "The quantity of dissolved fertilizer salt in the water "
            "around the roots. You measure it in mS/cm. It is an approximate measurement of the "
            "strength of the feed."),
    defterm("Dryback", "The controlled drying of the substrate between two irrigations. You measure "
            "the dryback with the change of the VWC. If the substrate is always full of water, the "
            "roots do not go deeper. If you let the substrate dry to a set value and then fill it "
            "again, the roots go deeper. In the flowering stage, the plant also uses more energy "
            "for reproduction. The size of the dryback is the primary control for steering."),
    defterm("Shot", "One short period of irrigation for a set time. The system gives some small "
            "shots each day. It does not give one large irrigation. The system sets the size of "
            "each shot."),
    defterm("Field capacity", "The maximum quantity of water that the substrate can hold. More "
            "water than this quantity drains from the substrate. The default target in this system "
            "is 70%."),
    defterm("Substrate", "The material that contains the roots. Examples are coco and rockwool, and "
            "materials of the same type. <a href='glossary.html#gl-substrate'>Glossary &rarr;</a>"),
    defterm("Solenoid valve", "A valve that operates with electricity. The relay board opens or "
            "closes the valve to start or stop the flow of water to a table."),
    defterm("VPD and crop steering", "When the temperature of the air is higher and the air is "
            "drier, the air removes more moisture from the surface of the leaves. VPD (vapor "
            "pressure deficit) measures this effect. It is the difference between the moisture that "
            "the air contains at this time and the maximum moisture that it can contain at that "
            "temperature. When the VPD is higher, the plant transpires water more quickly, and you "
            "must supply water more quickly. Crop steering is a method to cause vegetative growth "
            "or generative growth in the plant with irrigation, climate, and light. <a "
            "href='glossary.html'>Glossary &rarr;</a>"),
    figure(grid([
        card("Vegetative", "Growth of leaves and size. The drybacks are smaller, the substrate stays wetter, and the EC is moderate.", "Steering"),
        card("Generative", "Flowers, density, and resin. The method uses larger controlled drybacks, a higher root-zone EC, or the two together.", "Steering"),
        card("Runoff", "Water that drains from the bottom of the pot during a shot. It shows that "
             "the substrate is at field capacity.", "Signal"),
      ], cols=3), 3,
      "A short reference for the three terms that cause the most problems for new personnel. These "
      "terms are the two types of steering and the information that runoff gives."),
  ]})

SECTIONS.append({"id": "hardware", "kicker": "Equipment", "title": "Equipment of the irrigation system",
  "blocks": [
    p("A <strong>KC868 E16S relay board</strong> controls the valves. The relay board has an "
      "Ethernet connection and operates with ESPHome firmware. It opens and closes each valve: the "
      "6 table valves, the mains water valve, the mainline valve, and the manifold valve."),
    p("Each table has a substrate probe. The probe measures the VWC, the EC, and the temperature. "
      "It sends the data with a basic digital protocol for soil sensors "
      "(<strong>SDI-12</strong>).</p><p>The room also has 4 environment sensors, 3 CO2 sensors, 4 "
      "AC units, a humidifier, and 4 relays for dehumidifiers. <strong>There is no pump "
      "switch</strong>. A pressure switch starts the pump when the mainline valve opens. Thus the "
      "water flows from the tank to the mainline, then to the dripper of the table, and then to the "
      "plant."),
    callout("note", "The mains water and manifold valves do not supply feed",
      p("The mains water valve and the manifold valve only fill the nutrient tank and mix the "
        "nutrient solution in it. The table valves are the only valves that supply feed to the "
        "plants. Some sensors have no connection at this time. This condition has effects on "
        "safety. The last section gives more information.")),
    table(["Device", "Function", "Connection"], [
      ["KC868 E16S relay board", "It opens and closes all the valves: the table valves, the mains water valve, the mainline valve, and the manifold valve.", "Ethernet and ESPHome"],
      ["Substrate probes (×6)", "Each probe measures VWC, EC, and temperature. There is one probe for each table.", "SDI-12"],
      ["Environment sensors (×4)", "They measure the temperature and the relative humidity (RH) of the room.", "ESPHome and Wi-Fi"],
      ["CO2 sensors (×3)", "They measure the CO2 of the room in ppm.", "ESPHome"],
      ["AC units (×4)", "They decrease the temperature of the room.", "Relay or IR"],
      ["Humidifier", "It increases the RH of the room.", "Relay"],
      ["Dehumidifiers (×4)", "They decrease the RH of the room. They start one after the other.", "Relay"],
      ["Lights", "They set the photoperiod and the lights-on window.", "Relay, with a timer"],
    ], cls="compact", caption="The equipment of the system. The relay board is the one point where "
      "a decision of the software opens or closes a valve."),
    figure(L.flow("The flow of water",
            [("Nutrient tank", "mixed feed waits"), ("Mainline valve", "opens, pump starts"),
             ("Mainline pipe", "pressurized"), ("Table valve", "opens for one table"),
             ("Drippers", "to each plant"), ("Runoff", "water drains")],
            note="No pump switch. The pressure switch starts the pump when the mainline valve opens."), 4,
      "Water moves only when the mainline valve and a table valve are open. The pump does not "
      "operate without water, because the pressure in the mainline starts the pump. A signal from "
      "the software does not start the pump."),
  ]})

SECTIONS.append({"id": "phases", "kicker": "Basic information", "title": "Irrigation phases P0 to P3",
  "blocks": [
    p("Crop steering divides each lights-on day into four phases. The phases control how the plant "
      "uses water and nutrients. A <strong>controlled dryback</strong> is a drying of the substrate "
      "by a set quantity before you apply water again. This dryback is the signal that causes "
      "vegetative root growth or generative flower production." + _c("yang-2022-rdi-review")),
    p("<strong>P0 (morning dryback)</strong> is the phase with no irrigation. The substrate dries "
      "after the night. The system changes to P1 when the VWC decreases by the target quantity (50% "
      "for vegetative steering, 40% for generative steering) or after a maximum of 120 "
      "minutes.</p><p><strong>P1 (ramp-up)</strong> gives shots that become larger. The first shot "
      "is 2% of the substrate volume, and the size increases by 0.5% for each shot. The time "
      "between two shots is 15 minutes. The phase continues until the VWC is approximately 65%, "
      "with a maximum of 10 shots."),
    p("<strong>P2 (maintenance)</strong> keeps the VWC stable with top-up shots. A top-up shot "
      "occurs when the VWC decreases to less than 60%. The system also increases or decreases this "
      "threshold with the EC ratio (the measured EC divided by the target EC). If the EC ratio is "
      "more than 1.2, the system applies more water to flush the salts. If the EC ratio is less "
      "than 0.8, the system lets the substrate dry. As a result, the concentration of the nutrients "
      "increases.</p><p><strong>P3 (before lights-off)</strong> is irrigation for emergencies only, "
      "when the VWC is less than 40%. The dryback in the night starts the cycle again."),
    callout("key", "Vegetative and generative steering",
      ul(["<strong>Vegetative</strong> steering uses smaller drybacks and a moderate EC to cause "
          "the growth of roots and leaves.",
          "<strong>Generative</strong> steering uses larger controlled drybacks, a higher root-zone "
          "EC, or the two together, to cause flowering." + _c("caplan-2019-drought-cannabis"),
          "The same P0 to P3 phases operate for the two types of steering. Only the dryback targets and the EC change."], "tight")),
    figure(L.flow("The phase cycle each day",
            [("P0", "dryback until target"), ("P1", "ramp-up &rarr; ~65% VWC"),
             ("P2", "keep VWC &rarr; lights-off near"), ("P3", "hold &rarr; lights-on")],
            note="Each change of phase has a trigger: dryback target, field capacity target, lights-off, lights-on."), 5,
      "The cycle starts again each day. P3 changes to P0 during the night, and lights-on starts the ramp again."),
    figure(L.line("One day of VWC: the steering sawtooth",
            [(0, 62), (1, 55), (2, 50), (3, 58), (4, 64), (5, 62), (6, 61), (7, 63), (8, 55)],
            ["lights on", "P0 end", "P1 start", "P1", "P1 end", "P2", "P2", "P2", "P3 / night"],
            ylab="VWC %", ymin=40, ymax=72,
            note="P0: VWC decreases. P1: VWC increases in steps. P2: stable sawtooth. P3: VWC decreases in the night."), 6,
      "You want this shape in the VWC trace. At the start of the day, the VWC decreases in a smooth "
      "dryback. Then the VWC increases in a controlled quantity. In the maintenance phase, the VWC "
      "is almost flat. Before the period of darkness, the VWC decreases."),
    figure(L.zones("EC ratio controls the P2 irrigation threshold", 0.5, 1.6, [
            (0.5, 0.8, L.BLUL, "dryback, EC increases"),
            (0.8, 1.2, L.GL, "keep stable"),
            (1.2, 1.6, L.REDL, "more water to flush salts"),
          ], unit=" ratio",
          note="EC ratio = measured EC ÷ target EC. In these zones, the system adjusts the P2 trigger without a person."), 7,
      "P2 does not have a constant threshold. The system measures the quantity of salt in the root "
      "zone. It lets the substrate dry to increase the concentration of the feed, or it applies "
      "more water to flush the salts. Thus the EC stays in the correct range." +
      _c("yang-2022-rdi-review")),
  ]})

SECTIONS.append({"id": "environment-and-safety", "kicker": "Climate and safety",
  "title": "Environment controls and safety interlocks",
  "blocks": [
    p("The system controls the climate of the room and the irrigation. The dehumidifiers start when "
      "the humidity is 5% more than the target. The 4 relays start one after the other, with 10 "
      "seconds between the starts, to prevent a current peak at start. The dehumidifiers stop when "
      "the humidity is 2% less than the target.</p><p>The humidifier uses the same logic in the "
      "opposite direction. The system injects CO2 when its concentration is 50 ppm less than the "
      "target, and only during lights-on. The injection always stops at lights-off."),
    p("Some safety layers operate independently and at the same time. Thus one fault cannot keep "
      "the valves open.</p><p>The <strong>master gate</strong> lets irrigation occur only if all "
      "these conditions occur at the same time. The Enabled toggle of the system is on, and "
      "maintenance mode is off. The leak sensor does not show a leak, and the tank is OK. The clock "
      "is in the time window.</p><p>A <strong>valve watchdog</strong> closes each table valve that "
      "is open for more than 3 minutes. Each day at 3 AM, an audit closes all valves and the CO2 "
      "injection. The audit is a reset. Maintenance mode closes all valves immediately."),
    callout("warn", "Safety in many layers",
      p("Do not set a safety layer to off to make the system easier. You must keep all the layers. "
        "The system uses more than one check. If the master gate gives an incorrect decision, the "
        "valve watchdog and the audit each day close the valves.")),
    table(["Protection", "Function", "Automatic?"], [
      ["Master gate", "It lets irrigation occur only if all these conditions occur at the same time. The Enabled toggle of the system is on, and maintenance mode is off. The leak sensor does not show a leak, and the tank is OK. The clock is in the time window.", "Yes"],
      ["Valve watchdog", "It closes each table valve that is open for more than 3 minutes.", "Yes"],
      ["Mains watchdog", "It closes the mainline valve if the valve is open for more than 24 minutes.", "Yes"],
      ["Leak abort", "It stops all irrigation if the leak sensor shows a leak.", "Yes (when the system has the sensor)"],
      ["Tank-low abort", "It stops irrigation if the tank float shows a low water level.", "Yes (when the system has the sensor)"],
      ["Maintenance mode", "It closes all valves immediately. It prevents new shots.", "Manual toggle"],
      ["Alert for an offline sensor", "It tells you when a probe or a device becomes offline.", "Yes"],
      ["Audit at 3 AM each day", "It is a reset each day. It closes all valves and the CO2 injection.", "Yes"],
      ["CO2 closes at lights-off", "It always stops the CO2 injection at lights-off.", "Yes"],
    ], cls="compact", caption="The safety layers. Two of them (leak, tank-low) operate only after "
      "you install their sensors. Read the last section."),
  ]})

SECTIONS.append({"id": "commissioning", "kicker": "One step at a time",
  "title": "Commissioning procedure",
  "blocks": [
    p("Start the system in sequence. Make sure that each layer operates correctly before you start "
      "the next layer. If you start crop steering on equipment that you did not examine, a table "
      "can have too much water."),
    steps([
      ("Examine the equipment", "Make sure that each probe and the relay board show "
       "<strong>Online</strong> in ESPHome. Make sure that the VWC value of a table is a correct "
       "number (for example, 47.4), and not a dash or zero."),
      ("Do a test of each valve", "Open each valve with the manual control. Then close the valve "
       "immediately. Make sure that each valve operates. Open the mainline valve for a short time. "
       "Make sure that the pump starts on pressure."),
      ("Set the window", "Set the irrigation window. For example, set the start to 08:30 (30 "
       "minutes after lights-on) and the end to 18:00 (2 hours before lights-off). Set the interval "
       "to 60 minutes and the time of each shot to 60 seconds."),
      ("Set the system to on", "In the Command Center, set the system to on. Set maintenance mode to "
       "off. Set the Enabled toggle to on for only the tables that you want to irrigate."),
      ("Do one test cycle", "Start one cycle. Monitor the valves while each valve opens and "
       "closes, one after the other. Make sure that water flows to the drippers and that runoff "
       "occurs."),
      ("Set the climate and the steering", "Set the temperature and humidity targets for day and night, "
       "and a CO2 target. After you make sure that the irrigation operates correctly, you can "
       "select a steering mode and a crop profile."),
    ]),
    table(["Setting", "Safe start value"], [
      ["Window start", "08:30 (30 minutes after lights-on)"],
      ["Window end", "18:00 (2 hours before lights-off)"],
      ["Interval", "60 minutes"],
      ["Shot time", "60 seconds"],
      ["Temperature for day and night", "26 °C (79 °F) in the day and 22 °C (72 °F) at night"],
      ["Relative humidity (RH)", "60%"],
      ["CO2 target", "1200 ppm"],
    ], cls="compact", caption="Safe start setpoints. We selected these values to be safe. Change "
      "them only after you monitor the trends for one week."),
  ]})

SECTIONS.append({"id": "daily-operation", "kicker": "Use each day",
  "title": "Operation each day and the dashboard",
  "blocks": [
    p("A check each day is short. When the system operates correctly, the Command Center shows "
      "these values for all 6 tables. The VWC is 30 to 70%. The EC is in your target range, and the "
      "substrate temperature is 20 to 26 °C (68 to 79 °F). The usual EC range is 2 to 6 mS/cm, and "
      "it is different for each stage. All the safety indicators are green."),
    p("On the Trends tab, the VWC graph must show a <strong>sawtooth</strong>. A sawtooth is a "
      "trace that decreases slowly and then increases quickly after each irrigation. A trace that "
      "is flat, or that only decreases, shows that irrigation does not occur. The graph gives you "
      "the first indication of a problem, before the system shows an error message."),
    ul(["Correct readings each day: VWC 30 to 70%, EC approximately 2 to 6 mS/cm, substrate temperature 20 to 26 °C (68 to 79 °F), and all safety indicators green",
        "A VWC trace that is not a sawtooth is your first signal of a problem",
        "To set a table to on or off, use the <strong>Enabled</strong> toggle in Zone Control",
        "To stop the system in an emergency, set Maintenance Mode to on (this closes all valves) or use the emergency-stop script"]),
    table(["Tab", "Information shown", "When to use it"], [
      ["Command Center", "All tables on one display: VWC, EC, temperature, and safety.", "Check of the condition each day"],
      ["Zone Control", "The Enabled toggle for each table, and the manual valve controls", "Add a table, or stop irrigation of a table"],
      ["Trends", "Graphs of VWC and EC with time", "Make sure that the VWC shows a sawtooth. Find the cause of a problem."],
      ["Environment", "The temperature, RH, and CO2 of the room, and their targets", "Tune the climate"],
      ["Schedule", "The settings for window, interval, and shot time", "Adjust the times of irrigation"],
    ], cls="compact", caption="The five dashboard tabs. On most days you open only Command Center "
      "and Trends. The other tabs are for changes."),
    figure(L.line("Correct sawtooth and problem trace",
            [(0, 62), (1, 54), (2, 63), (3, 55), (4, 64), (5, 56), (6, 63), (7, 55)],
            ["t0", "t1", "t2", "t3", "t4", "t5", "t6", "t7"],
            ylab="VWC %", ymin=30, ymax=72,
            note="When the trace increases quickly, a shot supplies water. If it only decreases, no water goes to the table."), 8,
      "The correct trace decreases and then increases after each irrigation, many times. If your "
      "trace only decreases and does not increase, it shows a fault. Use the troubleshooting table."),
  ]})

SECTIONS.append({"id": "troubleshooting", "kicker": "When a fault occurs", "title": "Troubleshooting",
  "blocks": [
    p("You can find the cause of most problems with a short checklist. Start at the top and "
      "continue to the bottom, because the easiest checks find the most problems. Two examples are "
      "a check that the system is on and a check that the window is open."),
    p("If irrigation does not operate, make sure that the system is on and that maintenance mode is "
      "off. Make sure that the clock is in the window. Make sure that the Enabled toggle of a "
      "minimum of one table is on. Make sure that the irrigation-allowed binary sensor shows "
      "<strong>on</strong>.</p><p>If the VWC or EC shows Unavailable, make sure that the ESPHome "
      "device is online. Then reload the template entities. If the system also has no raw probe "
      "value, the probe has no connection. A correct VWC is possible only if the dielectric sensor "
      "operates. Thus a raw value that does not change shows a problem with the probe, and not with "
      "the software." + _c("topp-1980-dielectric-vwc")),
    callout("tip", "Tune slowly",
      p("Operate the irrigation with set times for approximately one week, and monitor the VWC "
        "trends. Then change to crop steering that uses sensors. First make sure that the sensor "
        "readings are correct. Calibration drift in probes with a low cost is frequent. It causes "
        "errors in each decision that uses the readings." + _c("mane-2024-sensor-calibration"))),
    table(["Problem", "Possible cause", "First step"], [
      ["Irrigation does not operate", "The system is off, maintenance mode is on, the clock is not in the window, or no table has the Enabled toggle on.",
       "Make sure that the system is on and that maintenance mode is off. Make sure that the clock is in the window and that the Enabled toggle of a table is on. Make sure that the irrigation-allowed sensor is on."],
      ["The VWC or EC shows Unavailable", "The ESPHome device is offline, or the template entity has no new data.",
       "Make sure that the device is online. Reload the template entities. Then examine the connection of the probe."],
      ["The shots show 0.0 s", "The substrate volume or the dripper flow rate has no value, or the known prefix fault occurs.",
       "Set the substrate volume (10 L / 2.6 gal) and the dripper flow rate (2 L/hr / 0.5 gal/hr). Do a check for the crop_steering_ prefix fault."],
      ["A valve that stays open", "The relay stays on, or the watchdog does not operate.",
       "First, set maintenance mode to on. Then set the valve to off with a service in Home Assistant. Then remove the power from the relay board."],
      ["Entity not found", "The integration tries to find entities with the prefix crop_steering_.",
       "Make sure that the entity IDs agree. If the known prefix fault occurs, the system cannot find the inputs for volume and flow rate."],
    ], cls="compact", caption="The five frequent faults. The rows for the 0.0-second shot and for "
      "entity not found frequently have the same cause (a missing input or an input with an "
      "incorrect prefix)."),
    table(["Setting", "Definition", "Default", "How to measure"], [
      ["Substrate volume", "Liters of substrate for each pot", "10 L (2.6 gal)", "Volume of the pot × fill fraction"],
      ["Dripper flow rate", "The quantity of water that each dripper supplies in one hour", "2 L/hr (0.5 gal/hr)", "Read the number on the dripper, or do a catch test."],
      ["Drippers for each plant", "The number of emitters that supply feed to one plant", "1 to 2", "Count the emitters on the plant"],
      ["Field capacity", "The maximum VWC before runoff occurs", "70%", "Saturate the substrate. Let it drain. Read the sensor."],
    ], cls="compact", caption="The settings that you tune. The system calculates the shot time from "
      "these values. Thus an incorrect substrate volume or flow rate gives incorrect shot times, or "
      "a shot time of zero."),
  ]})

SECTIONS.append({"id": "expectations", "kicker": "The limits", "title": "Expected results and limitations",
  "blocks": [
    callout("key", "You cannot be sure of the results",
      p("The basic system gives automatic control of the irrigation times and automatic decisions "
        "from sensor data. The sensors and the plumbing set the limit for the performance of the "
        "system. The tank-low abort and the leak abort <strong>always show &lsquo;safe&rsquo; and "
        "will not operate</strong>, until you install the tank float switch and the leak sensor. In "
        "this condition, do not operate the system without a person to monitor it.")),
    p("There are two more limits. Without a leaf-temperature sensor, the system calculates the VPD "
      "from the air temperature of the room, and the VPD is less accurate. The optional AppDaemon "
      "layer is necessary for automatic changes between the P0 to P3 phases without a person. The "
      "basic system does not include this layer. Before you use the automation, operate the system "
      "with only a timer for approximately one week. Monitor the system in this time."),
    table(["Sensor that is not connected", "Effect when there is no sensor"], [
      ["Tank float switch", "There is no tank-low abort. The pump can operate when the tank is empty."],
      ["Leak sensor", "There is no leak abort. A leak does not stop irrigation."],
      ["Tank pH and EC probes", "The tank pH and EC show Unavailable. Mix the nutrient tank manually."],
      ["Leaf-temperature sensor", "The system calculates the VPD from the air temperature of the room and not from the leaf temperature. The steering is less accurate."],
    ], cls="compact", caption="These items are not safe at this time. Install the float switch and "
      "the leak sensor before you operate the system without a person to monitor it. Each other "
      "missing sensor has a smaller effect, and the system continues to operate. These two missing "
      "sensors remove a protection."),
    p("First, read one usual day on the Trends tab. Then change one setting at a time. To know the "
      "biology of the dryback and the P0 to P3 rhythm, read the <a "
      "href='coco-crop-steering.html'>crop steering in coir</a> paper. To know how the probe "
      "measures the root zone, read the <a href='root-zone-teros12.html'>root-zone sensor</a> guide."),
  ]})
