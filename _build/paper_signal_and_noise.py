# -*- coding: utf-8 -*-
"""Paper: signal and noise, telling a real change from sensor wobble (precision)."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        stagecard, grid, card, chip, kv, steps)
import figs_lib as L

SLUG = "signal-and-noise"
TITLE = "Find the difference between plant changes and sensor noise"
EYEBROW = "Precision · Signal and noise"
SUB = ("This paper shows you how to find the signal in your sensor data and how to ignore the "
       "random jitter. Thus you know when to adjust the room. It is equally important to know when "
       "to make no adjustment.")
META = [("gauge", "Precision"), ("image", "9 diagrams"),
        ("quote", "9 sources"), ("clock", "~14 min to read")]
RELATED = ["root-zone-teros12", "smart-watering-vrwe", "closed-loop"]
REF_IDS = ["shewhart-control-chart", "deming-funnel-tampering", "western-electric-rules-anhoj",
           "nyquist-shannon-sampling", "replication-reduces-variance", "bogena-soil-sensor-calibration",
           "roberts-ewma-1959", "greenhouse-uniformity-crop-growth", "snr-engineering-origin"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

SECTIONS.append({"id": "what-this-is", "kicker": "Start here",
  "title": "Purpose and scope",
  "blocks": [
    callout("evidence", "Weak",
      "<p><strong>Limit of the data:</strong> Replace the percentages of alarm noise and the "
      "control rules from this paper with <em>your</em> measured rate of false positives. If you "
      "use the Western Electric rules or the Nelson rules, use the correct name for each.</p>"),
    lead("Each sensor reading in your grow room is the total of two parts: the accurate information "
         "(the <strong>signal</strong>) and jitter that gives no information (the "
         "<strong>noise</strong>). Your task is to find the signal in the noise."),
    p("Sensors have a low cost, and dashboards are easy to make. But growers continue to make most "
      "decisions with no method. At this time, the task is to find the difference between the "
      "signal and the noise. This paper gives you a method for this task. The paper also gives you "
      "a method to know when to make no adjustment. This method is equally important."),
    p("One flower room can make hundreds of thousands of data points in a week" +
      _c("greenhouse-uniformity-crop-growth") + ". Thus a method to ignore most of them safely is "
      "necessary. More data does not give more information that you can use. It is less easy to use "
      "a large quantity of low-quality data for decisions than a small quantity of good data."),
    figure(L.line("The same data: the signal is in the noise",
            [(0, 60), (1, 55), (2, 58), (3, 51), (4, 53), (5, 47), (6, 49), (7, 43), (8, 45), (9, 40)],
            ["0h", "", "", "", "", "", "", "", "", "9h"],
            ylab="VWC %", note="The rough line is the sensor data. You want to adjust for each low point. The signal is the stable dryback below it."), 1,
      "The figure shows one smooth trend (a usual dryback) below a rough line of sensor jitter. The "
      "numbers are the same, but the information is different. Only the smooth trend is important "
      "for your decisions."),
    callout("key", "The problem in one sentence",
      p("A <strong>signal-to-noise problem</strong> is the primary cause of most alarm fatigue in "
        "grow rooms. In this problem, the jitter is too large, and the signal is not easy to see. "
        "Before tuning, most alarms are transients. A transient stops before an adjustment has an "
        "effect.")),
  ]})

SECTIONS.append({"id": "key-terms", "kicker": "Terms",
  "title": "Definitions",
  "blocks": [
    p("The terms in this paper are from radio engineering, manufacturing and statistics. "
      "<strong>Signal-to-noise ratio (SNR)</strong> is the strength of the signal that is important "
      "to you, compared with the strength of all other signals" + _c("snr-engineering-origin") +
      ". In a room with a high SNR, the decisions are easy and the room is stable. In a room with a "
      "low SNR, the decisions are not easy and you adjust the room too frequently."),
    defterm("Signal", "A change in the data that is accurate and important for your decisions. "
            "Examples are a trend that continues for many readings, a step change, or a rhythm that "
            "occurs again each day."),
    defterm("Noise", "Variation in the data that gives no information. Examples are a spike in one "
            "reading, jitter, or a transient from a door that opens or from an HVAC cycle."),
    defterm("Drift", "A slow error of a sensor in one direction. The error has the same shape as a "
            "trend in the plant. Drift is the type of noise that causes the most problems, because "
            "it looks the same as a signal."),
    defterm("Averaging / aggregation", "The average of many readings, or of many plants. The random "
            "differences of each reading become small, and the information that all readings have "
            "stays."),
    defterm("Control limits", "Limits that you calculate from the recorded data of the system. "
            "Variation in the limits is usual, and variation out of the limits is unusual."),
    defterm("Calibration", "The task in which you compare a probe with a known reference and "
            "correct the probe. Thus the readings stay accurate for a long time. <a "
            "href='glossary.html#gl-calibration'>Glossary &rarr;</a>"),
    table(["Signal: do something about it", "Noise: ignore it"], [
      ["A trend that continues for many readings", "A spike in one reading"],
      ["A step change that stays", "Jitter that is smaller than the accuracy of the sensor"],
      ["A rhythm of day and night", "A transient from a door, a vent or an HVAC cycle"],
      ["Some sensors agree on the change", "One probe that does not agree with the probes near it"],
      ["A trend that agrees with a reference", "Slow drift from a probe with no calibration"],
    ], cls="compact", caption="The table compares the shapes of signal and the shapes of noise."),
  ]})

SECTIONS.append({"id": "where-noise-comes-from", "kicker": "Primary item 1",
  "title": "Sources of measurement noise",
  "blocks": [
    p("You cannot decrease a source of noise if you cannot find it. Noise in a grow room comes from "
      "six sources. Three are <strong>physical sources</strong> that are part of the measurement. "
      "They are the sensor (electronic jitter, drift, no calibration), the position (a probe near a "
      "vent or a light, or a sample of one) and the biology (one plant is different from the next). "
      "The other three are <strong>procedural sources</strong>, and thus they have the lowest cost "
      "to correct. They are the environment (doors, HVAC cycles), the operator (manual sampling "
      "that is not the same each time) and the data pipeline (gaps in the data, incorrect units, "
      "clock skew)."),
    figure(L.flow("The six sources of the measured noise",
            [("Sensor", "jitter, drift, no calibration"), ("Position", "edges, vents, 1 probe"),
             ("Biology", "difference between plants"), ("Environment", "doors, HVAC cycles"),
             ("Operator", "sampling that changes"), ("Data pipeline", "gaps, units, clock skew")],
            note="The first three are physical. The last three are procedural and cost less to correct."), 2,
      "The figure is an Ishikawa diagram (fishbone diagram). Six sources cause the &lsquo;measured "
      "noise&rsquo; that you see on the dashboard. Correct the procedural sources, which cost less, "
      "before you think that the equipment has a fault."),
    callout("warn", "Drift is the noise that causes the most problems",
      p("Calibrate each probe with a known reference, because calibration is the only protection "
        "from drift. Drift moves slowly in one direction, the same as a trend in the plant. Thus "
        "drift can give you incorrect information for many weeks. A pH probe or an EC probe with no "
        "calibration can have drift. You can measure the drift in weeks to a month" +
        _c("bogena-soil-sensor-calibration") + ". One probe is not sufficient to make sure that the "
        "data are correct.")),
    p("A calibration for each sensor is necessary. In low-cost permittivity sensors for soil "
      "moisture, a calibration for each sensor decreased the error by approximately 70%, compared "
      "with the calibration of the manufacturer" + _c("bogena-soil-sensor-calibration") +
      ". When a grower thinks that the room is a problem, the noise is frequently the problem."),
    table(["Source", "Symptom", "Task", "Cost to correct"], [
      ["Data pipeline", "Gaps, incorrect units, clock skew", "Examine the data pipeline. Make sure that the units and the timestamps do not change.", "Low"],
      ["Operator", "Readings that change with the person who made them", "Write an SOP with the same time, the same method and the same position.", "Low"],
      ["Environment", "Spikes that agree with doors or HVAC cycles", "Make the dead-bands wider. Filter the transients.", "Low or medium"],
      ["Sensor", "Jitter, drift in one direction", "Calibrate at set intervals with a reference", "Medium"],
      ["Position", "One probe that is different from the probes near it", "Move the probes from the edges to the middle of the canopy", "Medium"],
      ["Biology", "Differences between plants", "Calculate the average of many plants (you cannot remove the differences)", "You cannot remove it"],
    ], cls="compact", caption="The six sources, with the source of lowest cost to correct first. Correct the procedural rows before the physical rows."),
  ]})

SECTIONS.append({"id": "averaging-and-sampling", "kicker": "Primary item 2",
  "title": "Sampling and averaging",
  "blocks": [
    p("The noise filter with the largest effect is to calculate the average of more sensors, and "
      "not to use only one sensor. Growers frequently ignore this filter. In your room, when you "
      "calculate the average of twelve plants across the bench, the differences of each plant "
      "become small. Only the information that all plants have stays.</p><p>The name of this method "
      "is <strong>replication</strong>. The error of an average decreases with the square root of "
      "the number of readings that you use" + _c("replication-reduces-variance") +
      ". Four probes decrease the noise to approximately one half, and nine probes decrease it to "
      "one third."),
    p("The frequency of the measurements is equally important. If the interval between the samples "
      "is too long, a fast pattern changes to a slow pattern that is not in the plant. The interval "
      "between the samples causes this incorrect trend. This error has the name "
      "<strong>aliasing</strong>.</p><p>The usual method comes from the Nyquist&ndash;Shannon "
      "sampling theorem" + _c("nyquist-shannon-sampling") + ". Use a sampling frequency of a "
      "minimum of two times the frequency of the fastest pattern that you must see. To see an "
      "irrigation response of 30 minutes, record the data at intervals of 10&ndash;15 minutes."),
    figure(L.line("Undersampling makes an incorrect trend",
            [(0, 60), (1, 42), (2, 58), (3, 44), (4, 59), (5, 43), (6, 57), (7, 45), (8, 60), (9, 44)],
            ["", "", "", "", "", "", "", "", "", ""],
            ylab="signal", note="The fast wave has an oscillation at each step. A sample from one step in two shows a slow drift that did not occur."), 3,
      "A fast oscillation, when the interval between the samples is too long, gives a slow "
      "incorrect wave. This incorrect trend can make you adjust the room for a change that does not "
      "occur."),
    callout("tip", "A high sampling rate has a cost",
      p("A sampling rate that is too high adds noise and storage cost. It also makes you want to "
        "adjust the room for each jitter. Use a sampling cadence that agrees with each channel.")),
    table(["Channel", "Cadence", "Because"], [
      ["Substrate VWC / EC", "1–5 min", "The irrigation responses are fast. The cadence must show the shape of the dryback."],
      ["Air temperature / RH / VPD", "1–5 min", "The HVAC changes quickly, and the VPD is the value for crop steering at this time."],
      ["CO₂", "1–5 min", "The CO₂ increases and decreases when doors open and when the system injects CO₂ for short periods."],
      ["Pour-through pH / EC", "1×/day, same time", "The indicator of slow drift. A reading each day at the same time is better than checks at random times that add noise."],
      ["Plant morphology", "2–3×/week", "The growth is slow. More frequent measurements add only noise from the operator."],
    ], cls="compact", caption="A correct cadence for each channel. Make the sampling rate agree with the rate of change of the quantity that you measure."),
  ]})

SECTIONS.append({"id": "control-limits-spc", "kicker": "Primary item 3",
  "title": "Control limits and adjustment thresholds",
  "blocks": [
    p("The most important method in this paper is from the work on quality in manufacturing: "
      "<strong>statistical process control (SPC)</strong>. Walter Shewhart, at Bell Laboratories, "
      "divided all variation into two types" + _c("shewhart-control-chart") + ". "
      "<strong>Common-cause</strong> variation is the jitter of a stable system. It stays in the "
      "control limits, and you must not adjust the system for it. <strong>Special-cause</strong> "
      "variation has a cause that you can find. It is out of the limits, and you must examine the "
      "cause."),
    p("You calculate the control limits from the recorded data of the system, and not from an "
      "estimate. The usual limits are the mean plus or minus three standard deviations" +
      _c("shewhart-control-chart") + ". W. Edwards Deming showed that <strong>tampering</strong> "
      "(an adjustment of the system for common-cause jitter) increases the variation of a system "
      "and does not decrease it" + _c("deming-funnel-tampering") + ". SPC lets you do a task in "
      "cultivation that is not easy: monitor a number that changes and, correctly, make no "
      "adjustment."),
    figure(L.zones("Control chart: most points are usual, one point is a signal", 30, 70,
            [(40, 60, L.GL, "±1σ: usual jitter"),
             (35, 65, L.AMBL, "±3σ: control limits"),
             (66, 70, L.REDL, "special cause: examine")],
            unit=" %VWC",
            note="Points in ±3σ are common-cause: ignore them. A point that is out of the limit is special-cause: find the cause."), 4,
      "The figure shows a mean line, a zone of ±1σ and control limits at ±3σ. Most readings have "
      "jitter in the limits, and this jitter does not cause a problem. One point above the top "
      "limit is the point that you must examine." + _c("shewhart-control-chart")),
    callout("note", "More than the limits: the Western Electric rules",
      ul(["<strong>Nelson trend (frequently 6 points)</strong> in which all the points go in the same direction. The trend shows a drift, also when the points are in the limits.",
          "<strong>Western Electric: 8 points</strong> on one side of the mean show that the system changed.",
          "<strong>Points too near the mean</strong> are unusual. They are frequently a sign that a filter is too strong, or that a person made the data and did not measure them."],
         "tight")),
    p("These Western Electric rules and Nelson rules find changes that you cannot find when you "
      "compare only one point with the limits. They do not cause false alarms for usual noise" +
      _c("western-electric-rules-anhoj") + ". A grower who adjusts a stable system many times in a "
      "day is usually the largest source of noise in the room."),
  ]})

SECTIONS.append({"id": "playbook", "kicker": "Start this week",
  "title": "Eight steps to decrease noise this week",
  "blocks": [
    p("It is not necessary to have new capital for the steps with the largest effect. For most "
      "steps, you must only do the same work each time. Do the steps in the sequence below."),
    steps([
      ("Do not monitor the values at all times", "A display that shows the values at all times causes tampering. Examine the decision charts at set times, and not the raw data all day."),
      ("Set a sampling cadence for each channel", "Use the table above. Use a high rate for fast channels and a low rate for slow channels. Do not use a sampling rate that is higher than the rate of your adjustments."),
      ("Add a rolling average to each decision chart", "Filter the line that you use for decisions. Keep a display of the raw data that you can show in one step. Then you can see an emergency."),
      ("Calculate the average of 6–12 probes", "Do not use only one source for a decision. Use the average, and let the one probe that is different have a small effect."),
      ("Write SOPs for manual readings", "Use the same time, the same method and the same position each time. The SOP removes the noise from the operator at no cost."),
      ("Calibrate at set intervals and keep a record", "In the next three months, set a calibration cadence with a reference. This calibration cadence is your only protection from drift."),
      ("Calculate the control limits for your 3 primary KPIs", "Calculate the mean ±3σ from your recorded data. Then you know which values are unusual."),
      ("Examine the positions and make dead-bands wider", "Move the probes from the edges, the vents and the lights to the middle of the canopy. Make a dead-band wider if the equipment starts and stops frequently."),
    ]),
    callout("key", "The test of one sentence before you do something about a number",
      p("&ldquo;Is this value <strong>out of its usual range</strong>, for <strong>more than one "
        "reading</strong>, and do my <strong>other sensors agree</strong>?&rdquo; If one of the "
        "three is no, it is noise. Ignore it.")),
    figure(L.flow("Adjust or ignore: three gates",
            [("Out of limits?", "out of ±3σ"), ("Stays?", "more than one reading"),
             ("Sensors agree?", "near sensors agree"), ("All yes → ADJUST", "it is signal"),
             ("One no → IGNORE", "it is noise")],
            note="Three yes/no gates are between an alarm and a decision."), 5,
      "The figure shows the decision flow. Each gate must be yes before you adjust the controls. If "
      "one gate is no, go to &lsquo;ignore&rsquo;."),
    p("Three filters are sufficient for almost all the data from a grow room. The <strong>moving "
      "average</strong> is easy. The <strong>EWMA</strong> (exponentially weighted) gives more "
      "weight to the last readings, and thus it has less lag for the same smoothing" +
      _c("roberts-ewma-1959") + ". The <strong>median filter</strong> removes spikes of one point. "
      "Start with a filter window of approximately 30&ndash;60 minutes, and then adjust it."),
    figure(L.line("Raw data and rolling average: the trend is clear",
            [(0, 58), (1, 49), (2, 56), (3, 47), (4, 52), (5, 44), (6, 50), (7, 41), (8, 47), (9, 39)],
            ["0h", "", "", "", "", "", "", "", "", "9h"],
            ylab="VWC %", note="The filtered trend (the middle of the line) shows a dryback that you cannot see in the spikes. The cost is a small lag."), 6,
      "The figure shows the raw data as a rough line, and the filtered trend through the middle of "
      "the line. The dryback is easy to see. The only cost is a small lag of a known size. Thus you "
      "keep a display of the raw data for an emergency."),
  ]})

SECTIONS.append({"id": "pitfalls", "kicker": "Problems to prevent",
  "title": "Troubleshooting",
  "blocks": [
    p("Two errors that are opposite are <strong>over-smoothing</strong> and "
      "<strong>tampering</strong>. A weak filter makes the data clear, but a filter that is too "
      "strong causes damage to the data. If the filter window is too wide, the filter removes a "
      "fast change that is not noise. Examples are a pump fault or an EC spike from a blocked "
      "dripper, and you must see these changes when they occur. The opposite error is to adjust the "
      "room for each small change. Such adjustments make the room less stable" +
      _c("deming-funnel-tampering") + "."),
    p("A feedback loop with data that have noise, or with a tuning that is too strong, makes "
      "corrections that are too large. The corrections go in one direction and then in the other "
      "direction, and the loop does not become stable. A thermostat that is too sensitive is an "
      "example. It starts the heater when it reads one degree low, and the temperature becomes too "
      "high. Then it starts the chiller, and the temperature becomes too low. As a result, the "
      "temperature of the room changes continuously.</p><p>This error has the name "
      "<strong>hunting</strong>. The symptom of hunting is a regular saw-tooth pattern in the "
      "temperature, the RH or the VWC. The day/night cycle <em>does not</em> cause this pattern. If "
      "your HVAC or fertigation system makes opposite corrections one after the other, the cause is "
      "frequently a sensor with noise. The cause can also be a dead-band that is too small. Think "
      "of an equipment fault only after you examine these two causes."),
    figure(L.flow("The feedback loop and the position where noise starts",
            [("Setpoint", "your target"), ("Controller", "makes decisions"),
             ("Actuator", "valve / fan / heater"), ("Plant / room", "the change that occurs"),
             ("Sensor", "← NOISE STARTS HERE")],
            note="The controller reads noise from the sensor as an error and makes a correction. Filter the input at the sensor."), 7,
      "The loop goes setpoint &rarr; controller &rarr; actuator &rarr; room &rarr; sensor and then "
      "back. Noise from the sensor causes the most problems. The controller cannot find the "
      "difference between this noise and an error in the room. Thus it makes a correction for an "
      "error that does not occur."),
    callout("danger", "Filter at the source and make the dead-band wider",
      p("Filter the input of the controller at the output of the sensor, before the controller "
        "makes a decision. If you do not filter the input, each control loop in the room adjusts "
        "for noise. A wider dead-band and a filtered input frequently correct climate equipment "
        "that you think has a fault. The equipment has no fault.")),
  ]})

SECTIONS.append({"id": "realistic-expectations", "kicker": "Results and limits",
  "title": "Expected results and limitations",
  "blocks": [
    p("Facilities go through stages in a set sequence. When you know your stage, you know the next "
      "step."),
    grid([
      card("1 · Blind", "No data and no method.", "stage"),
      card("2 · Logged", "Data but no method: much noise, and too many adjustments.", "stage"),
      card("3 · Filtered", "Filters and a sampling cadence. The change to this stage has the largest effect.", "stage"),
      card("4 · Controlled", "You adjust only for special causes.", "stage"),
      card("5 · Tuned", "Closed loop. The target is uniformity.", "stage"),
    ], cols=5),
    p("Most commercial rooms are at the <strong>Logged</strong> stage. A room at the Logged stage "
      "causes more stress to the grower than a room at the Blind stage, because the noise causes "
      "many alarms. The target is one stage up, and not the last stage in one step. The change from "
      "the Logged stage to the Filtered stage has the largest effect of all the steps in this "
      "paper. It uses only filters and a sampling cadence. It has almost no cost, and you must only "
      "do the same procedure each time."),
    p("Monitor <em>a small number of</em> KPIs that have a high signal, and not forty instruments. "
      "The indicator that is the most related to commercial success is frequently "
      "<strong>uniformity</strong>. You measure it as the coefficient of variation of the batch, "
      "and not as the peak yield. Tests show that, when the variation of the environment in space "
      "and in time decreases (a lower coefficient of variation), the growth and the quality of the "
      "crop increase" + _c("greenhouse-uniformity-crop-growth") + ".</p><p>Compare two batches. In "
      "the first batch, each plant has a yield of 95 g (3.4 oz). In the second batch, the average "
      "is 110 g (3.9 oz) and the range is 40 g (1.4 oz). The first batch has a higher commercial "
      "value."),
    table(["KPIs with a high signal: monitor these", "Indicators with no value for decisions: ignore these"], [
      ["Grams for each kWh", "Temperature from one sensor at one time"],
      ["Dryback trend", "Total quantity of data points recorded"],
      ["Time in range for the VPD", "Peak / record readings"],
      ["DLI supplied compared with the target", "Number of alarms"],
      ["Batch coefficient of variation", "Number of dashboards"],
    ], cls="compact", caption="The coefficient of variation measures the noise in your crop. In commercial production, uniformity is better than the peak yield."),
    callout("key", "Summary",
      p("The target is a higher signal-to-noise ratio, and not a room with no noise. One stage up "
        "is the correct target. Filter before you adjust the room, and let a number that stays in "
        "its control limits change with no adjustment.")),
    p("Next, read the paper <a href='smart-watering-vrwe.html'>smart watering with VWC and EC</a> "
      "to find how a clean, filtered signal controls the irrigation. Then read the paper <a "
      "href='closed-loop.html'>closed-loop control</a> to find how a closed loop operates with no "
      "hunting."),
  ]})
