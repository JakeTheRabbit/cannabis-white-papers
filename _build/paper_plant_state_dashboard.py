# -*- coding: utf-8 -*-
"""Paper: from telemetry to intelligence, the plant-state dashboard (operational)."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        stagecard, grid, card, chip, kv, steps)
import figs_lib as L

SLUG = "plant-state-dashboard"
TITLE = "Design of a plant-state dashboard for your grow room"
EYEBROW = "Precision · Dashboards"
SUB = ("We recommend that a grow-room screen shows the state of the plant, and not many numbers "
       "from the sensors. This paper shows how to make a screen that finds drift some days before "
       "it becomes damage, shows the cause and gives the next step.")
META = [("dashboard", "Precision"), ("image", "11 diagrams"),
        ("doc", "Operation guide"), ("clock", "~13 min to read")]
RELATED = ["signal-and-noise", "f2-crop-steering", "root-zone-teros12"]
REF_IDS = ["spc-signal-noise-ed", "preattentive-dataviz", "vpd-plant-response",
           "capacitive-soil-moisture", "alarm-mgmt-isa182"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

SECTIONS.append({"id": "intro", "kicker": "Start here", "title": "Purpose and scope",
  "blocks": [
    callout("evidence", "Weak",
      "<p><strong>Temporary:</strong> The advisories on the screen (for example, the time before a "
      "tipburn risk) are examples of product design for operators. They are not a model for "
      "prediction that has validation.</p>"),
    lead("A grow room has sensors for many values: the air temperature, the humidity, the VPD, the "
         "CO&#8322; and the light. The sensors also measure the moisture of the substrate, the EC, "
         "the root-zone temperature, the pH and the electrical power that the equipment uses. The "
         "sensors measure these values each second. The dashboards that show all of this have many "
         "numbers and graphs. They tell you the <em>values</em> that occur. They do not tell you "
         "the <em>effect</em> on the plant, the conditions that will occur next, or the task to do."),
    p("This paper shows a different method for the design of a dashboard. The name of this method "
      "is <strong>Plant-State Intelligence</strong>. The method gives a screen that calculates an "
      "estimate of the state of the plant, and does not only show the values for the room. The "
      "target is a &lsquo;calm dashboard&rsquo;: a dashboard that gives an advisory only when there "
      "is something important. Thus it has no signal for most of the time.</p><p>A telemetry-dump "
      "dashboard makes the person put the information of fifteen graphs together and make a "
      "decision, frequently after a long day of work. A plant-state dashboard does this for you."),
    callout("note", "Information about this paper",
      ul(["This paper is a <strong>guide for operations and product design</strong>. It is not a paper on horticulture. The examples of lead time show a design for operators. They are predictions that have no validation. We recommend most of the designs in this paper. Examples show these designs.",
          "The target is a screen with <strong>inference</strong> of the state of the plant, <strong>prediction</strong> of problems and <strong>prescription</strong> of the next step. The screen gives the prediction some days before the problems occur, with its evidence and confidence.",
          "The paper starts from this: <em>a screen full of gauges is not a second person that helps you.</em>"], "tight")),
    figure(L.flow("Where you make the decision",
            [("Sensors", "data from the room"),
             ("Many graphs", "15 graphs, no sensor fusion"),
             ("Person", "must put all the data together fast")],
            note="The usual method: the person puts the data together."), 1,
      "The telemetry-dump method (above) leaves all the work of the decision to the person. "
      "Plant-State Intelligence moves this work to the system: sensors &rarr; sensor fusion and "
      "inference &rarr; one decision that is easy to read."),
  ]})

SECTIONS.append({"id": "key-terms", "kicker": "The terms", "title": "Definitions",
  "blocks": [
    p("These terms come before the other sections. It is not necessary that you know the terms at this time. Each term occurs again in the paper."),
    defterm("Telemetry", "The measurements that your sensors send each second: temperature, "
            "humidity, moisture and other values. The data are as they come from the sensors, "
            "before you use them."),
    defterm("VPD (vapor pressure deficit)", "The quantity of water vapor that you must add to the "
            "air to saturate it. This quantity changes the rate of transpiration of a plant. A VPD "
            "of 1.4&ndash;1.6&nbsp;kPa is correct in the last stage of flowering. In the first "
            "stage of vegetative growth, it causes stress. The same number has a different effect "
            "at each stage."),
    defterm("Crop steering", "The control of irrigation and dryback to make a plant "
            "<strong>vegetative</strong> (growth of leaves) or <strong>generative</strong> (flower "
            "and resin)."),
    defterm("Inference", "An estimate of a value that you cannot measure directly, for example "
            "plant stress. You calculate the estimate from some values that you can measure."),
    defterm("Sensor fusion", "Some signals that you put together in a period of time to give one "
            "result. The signal &lsquo;leaf temperature is higher&rsquo; is only noise. The signals "
            "&lsquo;leaf temperature is higher <em>and</em> transpiration is flat <em>and</em> "
            "dryback is deeper than usual&rsquo; together are a diagnosis."),
    defterm("Dryback", "The quantity by which the substrate dries between two irrigations. Two "
            "values for crop steering are the <em>dryback depth</em> and the <em>dryback rate</em>. "
            "You calculate them from the sensor data. They are more important than a moisture "
            "number from a sensor."),
    defterm("Leading indicator and lagging indicator", "A leading indicator is a precursor that gives a signal "
            "before damage occurs. A lagging indicator is a symptom that shows damage that occurred "
            "before."),
    defterm("Baseline and trajectory", "The usual range of values for this cultivar, at this stage "
            "and at this time in the photoperiod. The range comes from the data of your previous "
            "cycles."),
    defterm("PPFD / DLI", "PPFD (photosynthetic photon flux density) is the light intensity at one "
            "time. DLI (daily light integral) is the total light that the plants receive each day. "
            "EC is the concentration of salt in the feed or in the pore water of the root zone."),
  ]})

SECTIONS.append({"id": "sensor-problem", "kicker": "The problem", "title": "Limits of dashboards with only sensor data",
  "blocks": [
    p("The usual dashboard uses one assumption that no person states: &lsquo;show each measurement, "
      "and a good grower will know the task to do.&rsquo; This assumption causes seven frequent "
      "problems. Each sensor measures the <strong>environment</strong> of the plant (air, root "
      "zone, light). No sensor measures vigor, stress or transpiration directly. Thus the person "
      "must make the inference without aid. For example, capacitive moisture probes give the water "
      "content in the substrate, and not the water condition of the plant" +
      _c("capacitive-soil-moisture") + "."),
    p("The usual dashboard also shows a problem after it occurs. When a value is more than a "
      "threshold, the accumulation of salt, or a dryback that stops, started hours or days before. "
      "The alarms have constant high limits and low limits, and they give false alarms. They start "
      "for short changes, for example when a door opens or when the lights come on. Thus growers "
      "start to ignore the alarms.</p><p>The alarm management standards of the process industry set "
      "the threshold of an alarm flood at approximately ten alarms in ten minutes. They set a "
      "maximum of approximately five percent for the most important alarms. The operator does not "
      "have trust in a grow-room dashboard that gives alarms continuously" + _c("alarm-mgmt-isa182") +
      "."),
    figure(L.flow("Seven problems of the sensor dashboard",
            [("1 Shows the room", "not the plant"),
             ("2 Slow", "shows stress after it occurs"),
             ("3 No record", "no baseline or reference"),
             ("4 False alarm", "constant limits, fatigue"),
             ("5 One signal at a time", "no view of other signals"),
             ("6 Too much work", "the work is a &lsquo;feature&rsquo;"),
             ("7 Only symptoms", "does not show the cause")],
            note="The result: we made instruments and gave them the name &lsquo;intelligence&rsquo;."), 2,
      "The seven problems of a telemetry-dump dashboard. In each problem, the person does a task "
      "that the system can do."),
    figure(L.line("The interval from cause to symptom",
            [(0, 2.6), (1, 2.9), (2, 3.3), (3, 3.8), (4, 4.4)],
            ["Day 22", "Day 23", "Day 24", "Day 25", "Day 26"],
            ylab="Pore-water EC", ymin=2, ymax=5,
            note="EC increases slowly for four days. Tipburn occurs only on Day 26."), 3,
      "The pore-water EC increases slowly for four days, and the grower does not find a problem, "
      "until tipburn occurs on Day 26. A graph of one signal shows the cause at all times, but no "
      "person monitors that one graph at that time. A plant-state system decreases this interval" +
      _c("spc-signal-noise-ed") + "."),
    callout("warn", "Gauges for one signal do not show the condition of the plant",
      p("Do not use only gauges for one signal. The information on the condition of the plant is in "
        "many signals together: moisture, EC, VPD and transpiration change together. Gauges for one "
        "signal cannot show these changes, also if you add many gauges.")),
  ]})

SECTIONS.append({"id": "six-inversions", "kicker": "The change", "title": "Six changes in the design of a plant-state dashboard",
  "blocks": [
    p("Plant-State Intelligence changes six assumptions of the sensor dashboard to the opposite. No "
      "change removes the sensor data. The data move to a lower position on the screen. You can "
      "continue to use the data when you want to examine a problem, also after the problem occurs."),
    table(["Axis", "From: group of gauges", "To: calm dashboard"], [
      ["<strong>Object</strong>", "Instruments: the dashboard shows the environment", "Inference: the dashboard calculates an estimate of the state of the plant"],
      ["<strong>Reference</strong>", "Thresholds that do not change", "Baselines from your data, for each cultivar, stage and photoperiod phase"],
      ["<strong>Inputs</strong>", "One signal for each gauge", "Sensor fusion of many signals"],
      ["<strong>Time</strong>", "Lagging indicators (symptoms)", "Leading indicators (precursors)"],
      ["<strong>Output</strong>", "Alarm: &lsquo;a number changed&rsquo;", "Prescription: task, time limit and result"],
      ["<strong>Mode</strong>", "Many graphs, always on", "A signal only for unusual values. The standard state has no signal."],
    ], caption="The six changes to the opposite. It is not easy to make the last change: the standard state has no signal."),
    callout("key", "The grower must monitor the plant, and not the screen",
      p("A screen that always shows many graphs causes the grower to monitor the screen and not the "
        "plant. The grower must monitor the plant first. Thus a prescription replaces an alarm that "
        "only tells you that a number changed. A prescription gives the task, the time limit and "
        "the result if you ignore it. Thus a screen with no signal, and not a full screen, is the "
        "standard state when there is no problem.")),
  ]})

SECTIONS.append({"id": "plant-state-model", "kicker": "Primary content", "title": "Plant-state inference model",
  "blocks": [
    p("The pipeline calculates estimates of four states that have an effect on each other. If you "
      "include the vision state, there are five states. The system shows the <strong>environment "
      "state</strong> (temperature, relative humidity, VPD, CO&#8322; and light) as totals in a "
      "period of time and as rates, and not as values at one time. Examples are the VPD-hours since "
      "the start of this day and the DLI to this time.</p><p>The effect of VPD on a plant does not "
      "change at a constant rate. The effect increases with time and does not come from one reading" +
      _c("vpd-plant-response") + ". Thus the total is the important quantity. The <strong>substrate "
      "state</strong> adds calculated values for crop steering. These calculated values are dryback "
      "depth, dryback rate, recovery to field capacity, and the change of the moisture after each "
      "shot."),
    p("No sensor measures the <strong>plant state</strong>. The system calculates an "
      "<strong>estimate</strong> of it with sensor fusion of the other states. The estimate has a "
      "transpiration proxy, a stress index, a vigor and stacking trajectory, and an output for the "
      "steering effect. The <strong>operation and equipment state</strong> and an optional "
      "<strong>vision state</strong> (canopy cameras) complete the model. The system uses the "
      "condition of the sensors as an important signal. Thus the system knows when the sensors give "
      "no correct data."),
    figure(L.flow("From the measured states to the plant state estimate",
            [("Environment", "VPD-hours, DLI, CO₂"),
             ("Substrate", "dryback depth + rate, recovery"),
             ("Equipment, vision", "pump and valve state, canopy"),
             ("Plant state (estimate)", "transpiration, stress, vigor, effect of steering")],
            note="The outer measured layers go to the plant state estimate in the middle."), 4,
      "The environment, substrate, equipment and vision states go to the plant state estimate. This "
      "estimate is the state that is important to the grower, and no sensor gives it."),
    table(["Value from the sensor", "Calculated value"], [
      ["WC = 42%", "Dryback depth 8%, slower than the baseline for this cultivar"],
      ["VPD = 1.5 kPa at this time", "VPD-hours 18% more than the baseline range for the day"],
      ["EC = 5.1 mS/cm", "Pore-water EC increased on 4 days in sequence: risk of tipburn"],
      ["Leaf temperature +0.6&deg;C", "Transpiration does not change, but the VPD is higher: the stomata close"],
    ], cls="compact", caption="The same number as a sensor value and as a calculated value. The values on the right are the information that a plant-state dashboard shows. The values on the left are at a lower position on the screen."),
    callout("tip", "The output is a short list of named conditions",
      p("This layer does not send fifteen numbers. It sends a short list of <strong>named "
        "conditions</strong>: &lsquo;a dryback that stops&rsquo;, &lsquo;salt accumulation&rsquo;, "
        "&lsquo;high transpiration&rsquo;. Each condition has a confidence and an evidence chain. "
        "Security cameras at the site can supply data for horticulture. They show the color and the "
        "uniformity of the canopy, and wilt at the start of the light period. They also show the "
        "height and the stacking in a period of some days, and a change of color in the first stage.")),
  ]})

SECTIONS.append({"id": "architecture", "kicker": "Primary content", "title": "Structure of a dashboard with six layers",
  "blocks": [
    p("The system is a pipeline with six layers. It agrees with a system that has Home Assistant in "
      "the middle. Most operations have layers 0 and 1, and the operators do not know it. The "
      "dashboard gets the inference a long time before the control of the equipment gets it. "
      "Autonomous control comes for one signal at a time, and only after the advisories for the "
      "signal are correct."),
    steps([
      ("Layer 0: Input", "Put all the data on the same timebase. Most rooms do this."),
      ("Layer 1: Values", "Calculate new values from the sensor data: VPD, dryback %, DLI, recovery rates and the effect of each shot."),
      ("Layer 2: Baseline", "Make baseline ranges for each cultivar, stage and photoperiod. Start with known values from horticulture, and make the ranges more accurate with the data of your cycles."),
      ("Layer 3: Inference", "Use sensor fusion to make named conditions, with confidence and evidence. The methods are the conditions that you set, and tests for unusual values. You can also add a step in which an LLM examines the data."),
      ("Layer 4: Prescription", "Connect each condition to a task with a time limit."),
      ("Layer 5: Display", "The calm dashboard. The optional Layer 5b has a gate. It gives closed-loop control only for tasks that have low risk and that have your approval."),
    ]),
    figure(L.flow("The six-layer pipeline",
            [("0 Input", "one timebase"), ("1 Values", "data → values"),
             ("2 Baseline", "baselines from data"), ("3 Inference", "named conditions"),
             ("4 Prescription", "task + time limit"), ("5 Display", "calm dashboard")],
            note="Optional 5b: closed loop from Display, only for low-risk tasks that have your approval."), 5,
      "The pipeline, layer by layer. You can start the baselines of Layer 2 with the targets for "
      "horticulture in papers (the Athena targets are one example), before you have data from your "
      "room."),
    callout("note", "Advisory-first is the design, not a limit",
      p("In this design, a person is in the loop. An operation can stay permanently at the "
        "&lsquo;advise only&rsquo; stage and get most of the results. Layer 5b makes changes "
        "automatically only for tasks that have low risk and that have your approval. A person must "
        "give approval for each task that has a permanent effect or a high cost.")),
  ]})

SECTIONS.append({"id": "dashboard-surface", "kicker": "Primary content", "title": "Structure of the dashboard and its four zones",
  "blocks": [
    p("The screen that the grower opens has four zones, and the first zone is the most important. "
      "When the condition of the plant is correct, three of the zones are empty. Zone&nbsp;1 is the "
      "<strong>Headline</strong>: one short sentence that is easy to read. It tells the condition "
      "of the plant, and it has a color that shows the condition. This sentence gives 90% of the "
      "information that a grower with much work must have, for 90% of the time.</p><p>Zone&nbsp;2 "
      "is the <strong>Watchlist</strong>, with the items that have drift but are not incorrect at "
      "this time (the precursors). The Watchlist makes advisories in the next zone not frequent. "
      "Zone&nbsp;3 is <strong>Advisories</strong>, the only zone that sends a signal to the grower. "
      "Each advisory has a prescription with a time limit. Zone&nbsp;4 is the zone for "
      "<strong>evidence and sensor data</strong>. It has a low position, but you do not remove it."),
    grid([
      card("Zone 1: Headline", "&lsquo;Flower Day 24 &middot; Room 3 &middot; Correct. The steering is generative, the same as the target. No task is necessary.&rsquo;", "always shown"),
      card("Zone 2: Watchlist", "Items with drift that are not incorrect at this time: the precursors. Each item is a sentence, and not a graph. Frequently empty.", "usually empty"),
      card("Zone 3: Advisories", "The only zone that sends a signal to the grower. Each advisory has a prescription with a time limit. It opens to show the evidence chain.", "not frequent, by design"),
      card("Zone 4: Evidence and sensor data", "The previous dashboard, at a lower position. It has the signals after sensor fusion, baselines and graphs of sensor data. You use them to examine a problem, also after the problem occurs.", "the lowest position"),
    ], cols=2),
    p("Color and layout are important here. You see the color, the position on the screen and the "
      "headline before you read the sentence. The name for this effect is pre-attentive processing" +
      _c("preattentive-dataviz") + ". It is the group of visual properties that you receive "
      "automatically, before you select an item to examine. Thus you can see the &lsquo;no "
      "problem&rsquo; state immediately, and you do not put the information from five panels "
      "together."),
    callout("key", "A full example of an advisory",
      p("&lsquo;Decrease the dryback target by 3% in Room 3 (Day 24)&hellip; Tipburn is possible "
        "soon (example) without this change. Confidence: high. <em>[Show evidence]</em>&rsquo;. The "
        "evidence opens to show the signals after sensor fusion, the baseline range and the values "
        "that are not in it, and a previous example. The previous dashboard was 100% Zone 4. The "
        "new dashboard starts with Zones 1&ndash;3 and keeps Zone 4 at a low position.")),
  ]})

SECTIONS.append({"id": "how-to", "kicker": "How to", "title": "Installation procedure",
  "blocks": [
    p("It is not necessary to assemble all the system again. Each stage gives results and makes the "
      "next stage possible. Most of the results occur by Stage&nbsp;3, a long time before "
      "closed-loop control."),
    figure(L.flow("The six stages of use",
            [("0 Telemetry", "the graphs you have"),
             ("1 Values", "calculated values, small work"),
             ("2 Baseline", "no false alarms, no alarm fatigue"),
             ("3 Fusion", "watchlist + advisories operate"),
             ("4 Prescription", "add tasks + time limits"),
             ("5 Closed loop", "gate, optional")],
            note="Most of the results occur by Stage 3. Stage 5 is optional."), 6,
      "Six stages from telemetry to closed loop. Stage 2 (the baseline, with no false alarms) is "
      "the largest step, because it stops alarm fatigue in one step."),
    steps([
      ("Select one room and one type of problem", "Select one type of problem (for example, a dryback that stops). Install Stages 1–3 in Home Assistant for only this type of problem."),
      ("Operate it in shadow mode for one cycle", "Operate the system with the dashboard that you have for a full cycle. Do not use its advisories to do tasks. Examine if each advisory is correct."),
      ("Show the lead time", "Measure the time between the advisory and the time at which you can see the problem. Show this on one advisory before you use the system in more rooms."),
      ("Add one type of problem at a time", "Add the next type of problem, then the next room. Stage 4 (prescription) and Stage 5 (closed loop) are optional, for one signal at a time."),
    ]),
    callout("tip", "Stage 4 is a stable last stage",
      p("You do not have to go from the advisory-first method to a different stage. An operation "
        "can stay at Stage&nbsp;4 permanently and get most of the results. Stage&nbsp;5 (closed "
        "loop) is optional, and it has a gate for tasks with low risk that have your approval.")),
  ]})

SECTIONS.append({"id": "pitfalls", "kicker": "Problems", "title": "Trust, confidence and types of problem",
  "blocks": [
    p("An advisory system that is incorrect <em>and</em> has high confidence is worse than no "
      "system. Trust is a balance. Each incorrect advisory decreases the trust, and each correct "
      "advisory increases it. Thus the <strong>precision</strong> of the advisories, and not the "
      "number of advisories, causes the grower to do a task. Five guardrails are necessary."),
    table(["Guardrail", "Problem that it prevents", "Mechanism"], [
      ["Show low confidence at cold start", "Too much confidence from the data of one cycle", "Start with known values from horticulture. Make the confidence ranges larger. Put the label &lsquo;data not sufficient&rsquo; on the outputs."],
      ["Easy to correct", "The grower does not want the system after incorrect advisories", "The grower can remove each advisory and identify it as a false positive. The identifications adjust the baselines."],
      ["Monitor precision", "A drift in quality with no signal", "The precision of the advisories and the false-positive rate are important values that the grower can see."],
      ["Person in the loop", "Errors with a permanent effect or a high cost", "A person gives approval for each task with a high cost or a permanent effect"],
      ["Not a black box", "No trust in the advisory", "Each advisory opens to show its evidence chain"],
    ], cls="compact", caption="The five guardrails. Each guardrail prevents one problem that decreases the trust of the grower in an advisory system."),
    callout("danger", "A sensor problem is an advisory",
      p("Make an advisory for a sensor that has drift, noise or a flat signal. For example: "
        "&lsquo;The EC probe in Room 2 gives a flat value, and this value is not possible: the "
        "probe can be defective, and the system stops the advisories from EC.&rsquo; If a grower "
        "cannot see the <em>cause</em> of an advisory, the grower will, correctly, have no trust in "
        "the <em>advisory</em>. The system must make the decision easy for the grower to see. A "
        "person must make the decision for a task with a permanent effect or a high cost.")),
  ]})

SECTIONS.append({"id": "expectations", "kicker": "The results", "title": "Expected results and limitations",
  "blocks": [
    p("When the new dashboard operates correctly, the grower monitors it <strong>less</strong>, has "
      "<strong>less</strong> damage with no advisory, and gets harvests with <strong>more "
      "uniformity</strong>. Six key performance indicators (KPIs) from one cycle to the next show "
      "this. For three of them, the target direction is <em>down</em>."),
    figure(L.bars("Six KPIs and their target direction (example)",
            [("Lead time ↑", 80), ("Damage ↓", 15), ("Precision ↑", 85),
             ("Screen time ↓", 25), ("Decisions ↑", 70), ("Result variance ↓", 20)],
            unit="", note="The bars show a target profile, not measured data. The direction is more important than the value.",
            maxv=100), 7,
      "A good target profile for the six KPIs. We recommend high values for lead time, precision "
      "and the number of decisions each week. We recommend low values for damage with no advisory, "
      "screen time and result variance."),
    ul(["<strong>Lead time</strong>: the time (hours or days) between an advisory and the time at which you can see the problem. Lead time is the primary KPI. The system must find drift before it causes damage.",
        "<strong>Damage with no advisory</strong>: damage that you can see, with no advisory before it. Decrease this to zero.",
        "<strong>Advisory precision</strong>: the number of advisories that the grower used for a task, divided by the total number of advisories. Also monitor the false-positive rate.",
        "<strong>Screen time</strong>: the time that the grower monitors the dashboard. A lower value is better. The grower must monitor the plants and not the screen.",
        "<strong>Decisions each week</strong>: the number of decisions that the dashboard gives in one week. The output is decisions, and not views of the screen.",
        "<strong>Result variance</strong>: the variation of yield and quality from one cycle to the next."]),
    callout("key", "Closed-loop control is optional",
      p("Most of the results occur by Stage&nbsp;3. It is possible that advisory-first is the "
        "correct permanent last stage. You do not have to use closed-loop control. The names in "
        "this paper (Plant-State Intelligence, &lsquo;calm dashboard&rsquo;) are only temporary "
        "names. The content is more important than the name.")),
    p("Start with a small system. Make the inference layer that finds drift in the first stage. "
      "Refer to the <a href='signal-and-noise.html'>signal-and-noise</a> paper for the statistics "
      "that it uses. Give the layer the calculated values for crop steering from <a "
      "href='f2-crop-steering.html'>f2 crop steering</a>. The dashboard is only as good as the "
      "states that it uses."),
  ]})
