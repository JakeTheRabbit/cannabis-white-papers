# -*- coding: utf-8 -*-
"""Paper: the closed loop, levers, signal and plant state (beginner)."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        stagecard, grid, card, chip, kv, steps)
import figs_lib as L

SLUG = "closed-loop"
TITLE = "Closed-loop grow room: levers, signals and plant state"
EYEBROW = "Precision · Closed loop"
SUB = ("Operate a grow room as one system that corrects its errors. This basic paper shows the "
       "levers that you change and how to read the condition of the plants. It also shows how to "
       "send this information back to the levers without oscillation.")
META = [("gauge", "Precision"), ("image", "9 diagrams"),
        ("quote", "9 sources"), ("clock", "~17 min to read")]
RELATED = ["signal-and-noise", "plant-state-dashboard", "f2-crop-steering"]
REF_IDS = ["mohammed-spc-2024", "isa-18-2-alarm-mgmt", "moon-rootzone-ec-2018",
           "huber-dli-co2-2021", "kim-co2-temp-light-msu", "szerement-dielectric-2019",
           "tdr-fdr-soil-review-2024", "choi-ec-transpiration-2015", "saure-tipburn-calcium-2001"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

SECTIONS.append({"id": "what-this-is", "kicker": "Start here", "title": "Purpose and scope",
  "blocks": [
    callout("evidence", "Weak",
      "<p><strong>Limit of the data:</strong> The examples of lead time (tip burn in N days, the "
      "condition of the room in seconds) are examples for the dashboard. They are not results of "
      "tests at many cannabis sites. Use the method of the coupled system. Use the predictions as "
      "examples only, until you measure the rate of false positives in your facility.</p>"),
    lead("A grow room is a <strong>loop</strong>. It is not a panel of controls with no connection "
         "to each other. You do not set the controls one time and then ignore them. You change a "
         "control, and the room and the plants change as a result. The sensors measure the change, "
         "and you examine the data. Thus you know the next change to make, and the cycle continues "
         "each minute of each day."),
    p("A thermostat is an example of a <strong>closed loop</strong>. When the room becomes too "
      "warm, the sensor measures the temperature and the air conditioner (AC) starts. When the "
      "temperature is correct again, the AC stops. The output of the system goes back to control "
      "the input of the system, and the cycle starts again.</p><p>In a grow room, all the controls "
      "operate with the same method. The plant shows you the next change to make. Then you monitor "
      "the effect of the change.</p><p>This paper shows the full cycle as one system. The cycle has "
      "three tasks. The task of <em>cause</em> is to make the lever change correct. The task of "
      "<em>perception</em> is to make the measurement accurate. The task of <em>cognition</em> is "
      "to find the information in the data."),
    p("<strong>A change has an effect on more than one part of the room.</strong> Each change of a "
      "lever changes four connected balances at the same time: heat, water vapor, CO2 and the salt "
      "in the root zone. A full loop is a room that senses its condition and knows the effect of "
      "each change. It corrects its drift before the drift causes damage."),
    figure(L.flow("The closed loop, six steps",
            [("Change", "change a lever"), ("Room changes", "coupled effects"),
             ("Sense", "measure + noise"), ("Filter", "signal or noise"),
             ("Inference", "estimate of plant state"), ("Prescription", "lever + setpoint, back to Change")],
            note="The last arrow, from Prescription to Change, closes the loop."), 1,
      "Read the diagram as a cycle. Each step goes to the next step. The last arrow, from "
      "Prescription back to Change, closes the loop."),
    callout("key", "The value of a closed loop",
      p("When the dashboard is good, a full loop tells you the condition of the room. It also tells "
        "you if you must change a lever quickly. When no change is necessary, the loop gives no "
        "alarms. This operation is correct. It is not a fault.")),
  ]})

SECTIONS.append({"id": "key-terms", "kicker": "List of terms with easy definitions", "title": "Definitions",
  "blocks": [
    p("Many terms in this paper are new. This section gives a definition of each term that is "
      "necessary before the primary content. Most of the terms are easy, but their names are not "
      "easy. It is not necessary to know all the terms at this time. Each term occurs again in the "
      "paper."),
    defterm("Lever (actuator)", "A control that you can change: the light intensity, the cooling "
            "setpoint, irrigation and CO2 supplementation. Approximately eleven primary groups of "
            "levers control a room."),
    defterm("Signal and noise", "Signal is the information about the condition of the plant and the "
            "room. Noise is jitter of the sensor, scatter in the biology, and spikes that occur one "
            "time and give no information. Each reading is the sum of signal and noise."),
    defterm("Setpoint and target", "A setpoint is a number in a controller. The controller tries to "
            "make the measurement agree with this number. For example, the controller decreases the "
            "air temperature to 24 &deg;C (75 &deg;F). A target is the result that you want. For "
            "example, the plant transpires at a correct rate. A setpoint and a target are not the "
            "same."),
    defterm("VPD (vapor pressure deficit)", "The air can always absorb more water vapor. This "
            "quantity is the gap, and it is larger when the air is hotter and drier. VPD is the "
            "measurement of the gap, in kilopascals (kPa). When the gap is larger, the air removes "
            "water from wet leaf surfaces at a higher rate. When the VPD is higher, water goes from "
            "the plants to the air more quickly and the root zone dries more quickly. If the VPD is "
            "too high, the plants close their stomata to keep water."),
    defterm("EC, VWC, dryback", "EC (electrical conductivity) is a measurement of the dissolved "
            "salt in the feed or in the root zone. When the substrate dries between shots, the "
            "plant absorbs water but the dissolved salts stay in the substrate. Thus the EC "
            "increases in each cycle. VWC (volumetric water content) is the quantity of water in "
            "the substrate. Dryback is the quantity by which the water content of the substrate "
            "decreases between two irrigation events."),
    defterm("Plant state", "The condition of the plant, for example stress, generative steering or "
            "on-track. You calculate the plant state from many signals together. You do not read it "
            "from one sensor."),
  ]})

SECTIONS.append({"id": "the-levers", "kicker": "Primary content: the lever half", "title": "Control levers and coupled effects",
  "blocks": [
    p("The room is one <strong>coupled system</strong>. It is not a set of controls with no "
      "connection to each other. When you increase the light intensity, you add more than "
      "light.</p><p>You also add heat. The plants absorb and transpire water at higher rates, and "
      "the humidity increases. The plants use more CO2. The root zone dries more quickly, and the "
      "concentration of the salt in it increases more quickly" + _c("huber-dli-co2-2021") +
      ". Light is a source of heat, a cause of transpiration, a cause of CO2 uptake and a load on "
      "the HVAC at the same time" + _c("kim-co2-temp-light-msu") + "."),
    p("Each change that you make has an effect on one or more of four <strong>balances</strong>: "
      "energy (heat), moisture (water vapor), carbon (CO2) and salt (root-zone EC). Approximately "
      "eleven primary groups of levers have an effect on these balances" + _c("kim-co2-temp-light-msu") +
      ". Before a change, do not examine only the function of the lever. Find the balance on which "
      "the change has an effect. Make sure that all the other parts of the room can absorb the "
      "change."),
    figure(L.flow("One lever, four balances",
            [("More light / PPFD", "one change"), ("Energy", "hotter leaves, longer AC time"),
             ("Moisture", "transpiration, RH, dehumidifier load increases"),
             ("Carbon", "more CO2 uptake"), ("Salt / root zone", "faster dryback, higher EC"),
             ("Result", "load more than capacity: failure mode")],
            note="One lever changes all four balances at the same time."), 2,
      "One change has four effects. If you decrease the cooling setpoint, the humidity, the VPD, "
      "the dryback rate and the condensation risk also change together" +
      _c("choi-ec-transpiration-2015") + "."),
    figure(L.bars("Time for each balance to become stable after a change",
            [("Energy (heat)", 8), ("Moisture (RH)", 18), ("Carbon (CO2)", 6), ("Salt (root zone)", 240)],
            unit=" min",
            note="Salt becomes stable much more slowly than the air balances. It increases in each cycle.",
            maxv=280), 3,
      "The four balances become stable in very different times. As a result, the data can show no "
      "problem for some hours after a change to one lever. In this time, the change can add load to "
      "the slowest balance, with no sign that you can see" + _c("moon-rootzone-ec-2018") +
      "."),
    table(["Balance", "Inputs", "Outputs", "The levers to change"], [
      ["<strong>Energy</strong> (heat)", "Lights, equipment, sun load", "AC, air exchange", "Light intensity, cooling setpoint, airflow"],
      ["<strong>Moisture</strong> (vapor)", "Transpiration, irrigation", "Dehumidifier, exhaust", "Dehumidifier setpoint, VPD target, shot size"],
      ["<strong>Carbon</strong> (CO2)", "CO2 supplementation", "Plant uptake, exhaust", "CO2 setpoint, times of exhaust"],
      ["<strong>Salt</strong> (root zone)", "Feed EC, dryback", "Plant uptake, runoff", "Shot size and frequency, dryback target, feed EC, runoff %"],
    ], caption="The four balances and the levers that change each balance. The usual failures are failures of coupling. No part is defective."),
    callout("warn", "Usual failures occur when you do not set the levers together",
      p("Set the levers in the correct sequence. First, select the growth stage, the light "
        "intensity and the CO2 setpoint. These change the quantity of water and CO2 that the plants "
        "use. Then make the capacity of the climate system agree with this quantity. Then set the "
        "irrigation strategy for the root zone to agree with the climate.</p><p>The usual failures "
        "occur when you set each lever and do not think about the other levers. Cooling can "
        "increase the humidity. A dehumidifier can add heat to the room. The exhaust can remove the "
        "CO2 that you add. In each of these examples, no part is defective.")),
  ]})

SECTIONS.append({"id": "reading-plant-state", "kicker": "Primary content: sensors and information", "title": "Sensor readings and the inference of plant state",
  "blocks": [
    p("You must <em>measure</em> the changes in the room, and noise must not cause incorrect data. "
      "Then you must find the information in the data. Each measurement is signal plus noise. "
      "Usually, <strong>many alarms from raw data are noise</strong>. Remove this noise before you "
      "use an alarm for a decision" + _c("isa-18-2-alarm-mgmt") + "."),
    p("To read the plant state, go from a number to a decision. A number is &lsquo;The VWC "
      "decreased by 12% during the night&rsquo;. A decision is &lsquo;The plant is in the "
      "generative steering that you want, and no change is necessary&rsquo; or &lsquo;Decrease the "
      "dryback by 3% during the next night, or tip burn is possible in approximately 48 "
      "hours&rsquo;. The task is to find the plant state. It is not only to show the data of the "
      "room."),
    p("To get the plant state, do these three steps in this sequence:"),
    ul(["<strong>Set the correct speed of sampling</strong> for the biology. Make the speed "
        "sufficient to measure the change that an irrigation event causes in 30 minutes. Do not "
        "make the speed high, because you cannot use the jitter that you record.",
        "<strong>Remove the scatter</strong> with a rolling average or a median filter before you examine the data.",
        "<strong>Compare the data with control limits.</strong> The control limits are values on "
        "the chart that you calculate from the recorded data of the room. Usually the values are "
        "the mean and approximately &plusmn;3 standard deviations (sigma)" + _c("mohammed-spc-2024") +
        "."]),
    figure(L.line("Signal and noise in one reading",
            [(0, 50), (1, 49), (2, 52), (3, 48), (4, 51), (5, 50), (6, 53), (7, 49)],
            ["t0", "t1", "t2", "t3", "t4", "t5", "t6", "t7"], ylab="reading",
            note="The smooth trend is the signal. The jitter around the trend is noise that you must remove."), 4,
      "Raw data from a sensor change by a small quantity in each sample. The trend shows the "
      "changes in the room. The jitter does not show the changes in the room. If you change a lever "
      "because of jitter, you change it for a change in the room that did not occur."),
    figure(L.line("Control chart: when a small change is important",
            [(0, 50), (1, 51), (2, 49), (3, 50), (4, 52), (5, 48), (6, 51), (7, 49), (8, 50), (9, 52), (10, 49), (11, 78)],
            ["", "", "", "", "", "", "", "", "", "", "", "mark"], ylab="value",
            note="Eleven points show jitter only. Point 12 is more than the limit: special-cause variation.",
            ymax=90), 5,
      "A point between the control limits is common-cause variation, and you do not change a lever. "
      "A point that is more than a limit is special-cause variation. A group of points that are not "
      "random is also special-cause variation. Find the cause of each special-cause variation. "
      "Statistical process control is a method that finds the difference between common-cause "
      "variation and special-cause variation" + _c("mohammed-spc-2024") + "."),
    p("Then <strong>use many readings, because one reading is not sufficient</strong>. Use a group "
      "of 12 readings (n-of-12), not one reading (n-of-1). The only correct input to the inference "
      "is a clean signal with a classification.</p><p>The inference uses sensor fusion on some "
      "clean signals to make named conditions. Each named condition has a value of confidence and "
      "an evidence chain. The inference compares the signals with a <em>learned envelope</em> and "
      "not with a constant limit. A VPD of 1.4 kPa is correct at the end of flowering, but it "
      "causes stress at the start of vegetative growth."),
    figure(L.zones("The four-zone calm dashboard", 0, 4,
            [(0, 1, L.GL, "Zone 1: plant state"), (1, 2, L.AMBL, "Zone 2: list to monitor"),
             (2, 3, L.REDL, "Zone 3: advisory"), (3, 4, L.BLUL, "Zone 4: raw data")],
            note="Zone 1 has approximately 90% of the value. The graphs of raw data are at the end."), 6,
      "A calm dashboard starts with one green label for the plant state (&lsquo;Flower Day 24, "
      "on-track, no change is necessary&rsquo;). Yellow shows the precursors that drift. Orange is "
      "the only color that tells you to do a task. The graphs of raw data are last."),
  ]})

SECTIONS.append({"id": "closing-the-loop", "kicker": "Primary content: all the parts together", "title": "Closed-loop diagnosis and corrective action",
  "blocks": [
    p("In this section, the three tasks operate as one system. Follow one usual problem through the "
      "full loop. The problem is <strong>salt creep</strong>. In salt creep, the dissolved salts "
      "slowly increase in the root zone, because each dryback cycle removes water but the salt "
      "stays."),
    steps([
      ("Cause makes the conditions", "A long dryback and a constant feed increase the salt concentration by a small quantity in each cycle. Thus the load on the slowest balance increases."),
      ("Perception ignores noise", "Perception ignores one EC spike. But perception identifies a signal when the EC increases for four days and is more than the control limit."),
      ("Cognition finds the information in the signal", "Cognition uses sensor fusion on this trend, the feed data and the dryback data. The result is a precursor with a name: &lsquo;salt accumulation, tip-burn precursor&rsquo;. The precursor has a value of confidence and an evidence chain."),
      ("Prescription and change", "The loop sets the dryback lever to a smaller dryback. This change closes the loop approximately four days before you can see tip burn. The salt balance then starts to become correct again."),
    ]),
    figure(L.flow("Salt creep in the full loop",
            [("Cause", "long dryback, constant feed, salt increases"),
             ("Perception", "one spike: noise. EC 4 days more than limit: signal"),
             ("Cognition", "fusion of EC, feed, dryback: tip-burn precursor"),
             ("Prescription and change", "decrease dryback. The loop uses the same lever.")],
            note="The dryback lever caused the problem, and the loop uses the same lever to correct it."), 7,
      "The EC at the roots increases when the substrate dries, long before the leaves show a change" +
      _c("choi-ec-transpiration-2015") + ". Thus closed-loop correction finds salt accumulation in "
      "the root zone approximately four days before you can see tip burn" +
      _c("saure-tipburn-calcium-2001") + "."),
    callout("note", "No task finds it without the other tasks",
      ul(["A <strong>lever-only</strong> grower does not measure it.",
          "A <strong>signal-only</strong> grower monitors a number that changes, but does not know the plant state.",
          "A <strong>dashboard-only</strong> grower, with no model of cause and effect, gives a prescription for the incorrect lever.",
          "Only the full loop has <strong>self-correction</strong>. No part has it without the other parts. The loop senses its errors and corrects them."], "tight")),
    p("Bridge metrics let the three tasks send data to each other. The bridge metrics are dryback "
      "%, VPD, VPD-hours, pore-water EC and recovery slope. The system calculates each metric one "
      "time, with one definition. Each part of the loop reads the same value.</p><p>Always "
      "<strong>give a prescription with a number and show how you calculated it</strong>. Give the "
      "lever change, the setpoint, the time limit and the result that the change will cause. The "
      "person who reads the prescription can open the full evidence chain when necessary. Do not "
      "make a black box."),
    table(["Failure", "Cause or coupling", "Signal method that finds it", "Inference and prescription"], [
      ["Salt creep that you cannot see", "Long dryback and constant feed", "EC more than the limit for 4 days", "Tip-burn precursor → decrease the dryback"],
      ["The irrigation water does not go to the substrate", "Blockage, pump fault or tubing fault", "The VWC does not increase after the shot", "Shot with no effect → apply the shot again, give an alarm"],
      ["Morning stress that you cannot see", "VPD spike at lights-on", "VPD-hours more than the learned envelope", "Morning stress → change the climate slowly"],
      ["Slow failure of the dehumidifier", "The capacity to remove water decreases", "Drift trend of the RH, not a spike", "Capacity fade → do maintenance before the failure"],
      ["A sensor that does not measure the room", "A probe with a constant signal or with noise", "Very low variance, or jitter: special-cause variation", "Defective probe → put it in quarantine, do not use its data"],
    ], cls="compact", caption="Five failures and one method: sensor fusion. A probe with a constant signal, with drift or with noise is also a special-cause signal that you can find" + _c("szerement-dielectric-2019") + "."),
  ]})

SECTIONS.append({"id": "how-to", "kicker": "Do this first", "title": "Procedure for closed-loop control",
  "blocks": [
    p("Make the loop one stage at a time. Do not start the next stage until the previous stage "
      "operates correctly. For almost all of this, it is not necessary to get new equipment. Most "
      "of it is a method."),
    steps([
      ("Part I: know the coupled effects of each change", "Before each change, identify the balances on which the change has an effect, and the direction of each effect. Think that each failure is a problem of capacity, or a problem of levers that you do not set together. It is not the fault of one lever."),
      ("Part II: make your signals accurate", "Do not monitor each new reading, because it can cause you to change levers too much. Set a sampling cadence for each sensor. Put a rolling average on each chart that you use for decisions. Calculate the control limits from your recorded data."),
      ("Part III: make decisions with inference", "Compare the data with a learned envelope for each cultivar, each growth stage and each photoperiod. Use sensor fusion before you give an alarm, because one signal is not sufficient. Make each advisory give a number and show its evidence chain. Make the system give no alarm when there is no problem."),
      ("Close the loop last, and carefully", "At the start, let the system make only automatic changes with low risk. Make sure that you can change the lever back. For example, the system changes the dryback by 3 points after a person gives approval. A person must give approval for each change that has a high cost or that you cannot change back."),
    ]),
    callout("tip", "Method before equipment",
      p("The changes with the most value in this procedure have no cost: a sampling cadence, a "
        "rolling average and a control limit. Each of them is only a new method. Get equipment only "
        "after the method operates.")),
  ]})

SECTIONS.append({"id": "pitfalls", "kicker": "Causes of failure", "title": "Troubleshooting",
  "blocks": [
    p("Two failure modes make a loop defective: <strong>use of noise as a signal</strong> and "
      "<strong>oscillation</strong>. If you give noise (spikes, jitter and incorrect trends) to a "
      "controller, the controller changes levers for changes in the room that did not occur. The "
      "noise makes the room not stable. A loop that receives noise does not help. It makes the "
      "problem larger.</p><p>Oscillation occurs when you change a lever too quickly or too much, or "
      "for readings that are in the usual variation. As a result, the values in the room increase "
      "and decrease, and do not become stable" + _c("mohammed-spc-2024") + "."),
    figure(L.line("Oscillation from noise and one correction",
            [(0, 50), (1, 64), (2, 38), (3, 66), (4, 36), (5, 62), (6, 40), (7, 58), (8, 44), (9, 50)],
            ["", "", "", "", "", "", "", "", "", ""], ylab="setpoint",
            note="A change for each jitter causes large changes of the setpoint. One correction can keep the setpoint constant.",
            ymax=80), 8,
      "If you change a lever for each small change, oscillation starts in the room, and the room "
      "cannot become stable. A loop with a filter makes one correction, and only when the signal is "
      "more than a limit."),
    callout("danger", "Test before you change a lever",
      p("Change a lever only if all three of these conditions occur. First, the reading is not in "
        "its learned envelope (<em>cognition</em>). Second, this condition continues for more than "
        "one reading, and the sensors agree (<em>perception</em>). Third, you know a lever that "
        "corrects the reading without a change to a different balance (<em>cause</em>). If one "
        "condition does not occur, the reading is noise. Do not change a lever.")),
    ul(["<strong>Aliasing</strong>: if the sampling is too slow, you see incorrect trends. If the "
        "sampling is too frequent, you record jitter that you cannot use, and the jitter can cause "
        "tampering. Make the sampling cadence agree with the biology" + _c("tdr-fdr-soil-review-2024") +
        ".",
        "<strong>The Stage-2 trap</strong>: each new reading causes more stress for you than no "
        "data. The readings are a large quantity of noise, and they can cause you to make incorrect "
        "changes quickly.",
        "<strong>Follow the loop, not the small change</strong>: make the data sufficiently smooth "
        "to change levers with confidence. Do not make the data very smooth, because then you "
        "cannot see a fast change that is not noise. Keep the raw data available in one step."]),
  ]})

SECTIONS.append({"id": "expectations", "kicker": "The results that you will get", "title": "Expected results and limitations",
  "blocks": [
    callout("key", "The result is a smaller number of alarms, not more displays",
      p("When the loop operates correctly, you examine the dashboard at longer intervals. You have "
        "a smaller number of problems that occur without a sign, and the harvests have less "
        "variation. A screen with no alarms is the product, because it shows that no task is "
        "necessary. In the advisory-first stage, the loop gives you a prescription, but you change "
        "the lever. You can stay in this stage for the time that you want, because it is stable and "
        "it has value. Full automatic operation is optional and has approval steps.")),
    figure(L.flow("The five stages of maturity",
            [("1 No data", "by eye only"), ("2 Recorded", "data, no method, if spike, change"),
             ("3 Filtered", "sampling, filter, limits (Perception on)"),
             ("4 Inference", "plant state, prescription (Cognition on)"),
             ("5 Closed loop", "automatic changes, with predictions (Cause closes loop)")],
            note="Each stage adds function. Do not start a stage until the previous stage operates."), 9,
      "The one change that gives the most value is the change from Stage 2 to Stage 3. Do not "
      "change levers for each new reading. Change levers for filtered trends that are more than the "
      "control limits. The only cost of this change is a new method, and you must do the change "
      "before all the higher stages."),
    ul(["<strong>Automation is not necessary to get good results.</strong> The advisory is on the "
        "screen a long time before the system changes a lever without a person. If you stop at this "
        "point, the result is good and stable.",
        "<strong>The numbers are only a start point.</strong> The reference setpoints are values "
        "from commercial cultivation. Use them as a start point, and calibrate them with the "
        "recorded data of your facility. The method is correct for all facilities. You must find "
        "the setpoints for your facility.",
        "<strong>Start with a small test.</strong> Select one room and one type of failure. Operate "
        "the loop in shadow mode for one cycle. Measure the lead time of one advisory before you "
        "use the loop in more rooms."]),
    p("First, know the coupled effects of your changes, make your signals accurate, and make your "
      "decisions with inference. Then, and only then, think about how to close the loop. For more "
      "information about the perception half, read the <a href='signal-and-noise.html'>signal and "
      "noise</a> paper. For information about the cognition half and how it gives the results to "
      "you, read the <a href='plant-state-dashboard.html'>plant-state dashboard</a> paper."),
  ]})
