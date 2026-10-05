# -*- coding: utf-8 -*-
"""Paper: F2 crop steering, the daily operating manual (beginner, operational)."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        stagecard, grid, card, chip, kv, steps)
import figs_lib as L

SLUG = "f2-crop-steering"
TITLE = "F2 crop steering: the manual for operation each day"
EYEBROW = "Precision · Crop steering"
SUB = ("After you read this paper, you can prepare, calibrate and operate an automatic irrigation "
       "controller for a grow room for the vegetative stage. The paper gives information about the "
       "P0 to P3 cycle of each day and the targets for moisture and salt. It also gives information "
       "about the controls that you use each day and the safety fail-safes in the system. It shows "
       "how to find the cause of a fault.")
META = [("gauge", "Precision"), ("image", "12 diagrams"),
        ("doc", "Manual for operation"), ("clock", "~18 min to read")]
RELATED = ["coco-crop-steering", "root-zone-teros12", "smart-watering-vrwe"]
REF_IDS = ["caplan-drought-2019", "zawilski-calibration-2023", "qi-salinity-2024",
           "kang-rootgrowth-2019", "mohammed-spc-2024"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

SECTIONS.append({"id": "what-this-is", "kicker": "Start here",
  "title": "Purpose and scope",
  "blocks": [
    callout("evidence", "Weak",
      "<p><strong>Grower method and temporary values:</strong> The default VWC values are the "
      "values of one facility. They are start points. They are the readings of the probes, in the "
      "units that the probes supply, after a person applies water by hand. The drought test of "
      "Caplan gives data for the general method of a controlled water deficit. It does not give "
      "data for the values of these setpoints. Calibrate the substrates before you arm the "
      "automation.</p>"),
    lead("F2 is an <strong>automatic irrigation controller</strong> for a grow room for the "
         "vegetative stage. It is software that reads the probes for moisture and salt in the root "
         "zone. The software selects the time to start each shot of water automatically, and it "
         "supplies the water through a pump and valves. You set the targets. The software applies "
         "the water."),
    p("<strong>Crop steering</strong> is a method in which you select the water content and the "
      "salt content of the root zone. The selection changes the type of growth that is primary in "
      "the plant. For a plant that is not in cultivation, a drought is a signal that the time is "
      "short. The plant then changes to reproduction. The system gives this signal with a "
      "controlled dose, at a controlled time.</p><p><em>Vegetative</em> steering (bulking) keeps "
      "the substrate wet. It uses many small shots and a small dryback. <em>Generative</em> "
      "steering (flower steering or stress steering) uses a larger dryback, more salt in the root "
      "zone, and a smaller number of larger shots. A small, controlled water deficit at the correct "
      "time is sufficient to cause a cannabis plant to change to generative growth. The yield does "
      "not decrease." + _c("caplan-drought-2019")),
    p("The system has two software layers that operate together. A <strong>Home Assistant "
      "integration</strong> gives you each control and each reading on the screen. An "
      "<strong>AppDaemon engine</strong> (<code>master_crop_steering_app.py</code>) makes the "
      "decisions and starts the shots. The room has <strong>3 rows (zones)</strong>. Each row has "
      "one probe for moisture and salt and one valve. One tank, one pump and one main line supply "
      "all the rows."),
    figure(grid([
        card("Home Assistant integration", "The dashboard. It has all the controls, settings and readings that you see and use.", "Layer 1"),
        card("AppDaemon engine", "The automatic decision software. It reads the probes, makes the decisions, and starts the shots through the hardware.", "Layer 2"),
        card("Hardware components", "Pump &rarr; main line &rarr; 3 zone valves. 3 probe pairs send readings back to the engine.", "Layer 3"),
      ], cols=3), 1,
      "The two software layers and the hardware that they operate. The controls go from the dashboard to the hardware. The probe readings go back from the hardware to the dashboard."),
    figure(L.flow("The room: 3 rows from one tank",
            [("Vegetative tank", "water for all rows"), ("Pump", "one pump for all rows"),
             ("Main line", "a branch to each row"), ("Row 1/2/3 valves", "one VWC + EC probe each")],
            note="Only one row receives water at a time."), 2,
      "One tank, one pump and one main line supply three rows. You control each row independently. Each row has one probe pair and one valve."),
    callout("key", "Two important facts",
      ul(["The <strong>&lsquo;Phase (manual set)&rsquo;</strong> list <em>overrides</em> the "
          "automatic phase. It shows the phase that you selected last, not the phase that is in "
          "operation at this time. To see the correct phase, read "
          "<code>sensor.crop_steering_current_phase</code>.",
          "It is always safe to disarm the system. When you set "
          "<code>switch.crop_steering_system_enabled = OFF</code>, no shot can start."], "tight")),
  ]})

SECTIONS.append({"id": "key-terms", "kicker": "Terms", "title": "Definitions",
  "blocks": [
    p("The system uses three measurements for all its operation. Read these definitions first, because all the other sections use them."),
    defterm("VWC (volumetric water content)", "The substrate contains water and air. Water fills "
            "some of the space in the substrate, and air fills the remaining space. VWC is the "
            "quantity of water at this time, as a percentage of the volume of the substrate. If the "
            "VWC is 60%, water fills 60% of the volume of the substrate. All irrigation decisions "
            "start from this number."),
    defterm("EC (electrical conductivity)", "When the water contains dissolved salt, the roots "
            "cannot absorb the water easily. The EC measurement gives the quantity of dissolved "
            "salt in the solution, in mS/cm. The sensor measures how easily electric current flows "
            "through the solution. A higher EC shows a stronger solution with more salt. A lower EC "
            "shows a weaker solution."),
    defterm("Dryback", "After each shot, the plant uses water, and the substrate becomes dry "
            "slowly. The VWC is at its highest value (the peak) immediately after a shot and at its "
            "lowest value immediately before the next shot. Dryback is the difference between these "
            "two values, as a percentage of the peak. A larger dryback causes more generative "
            "growth. A smaller dryback causes the plant to continue vegetative growth. This "
            "difference is the primary control for steering."),
    defterm("Shot", "One short period of water supply. The size of a shot is a percentage of the "
            "volume of the substrate. The system calculates the shot time in seconds from the "
            "substrate volume, the dripper flow rate and the shot size."),
    defterm("Field capacity", "The peak VWC. The water saturates the substrate, and then the water "
            "that the substrate cannot hold flows out. It is the &lsquo;full&rsquo; value of the "
            "substrate."),
    defterm("EC ratio", "Divide the measured EC by the target EC. The result is the EC ratio. A "
            "ratio of more than 1 shows that the solution has too much salt. Thus apply more water "
            "to dilute the solution. A ratio of less than 1 shows that the solution is too weak. "
            "Thus apply less water."),
    defterm("Vegetative mode and generative mode", "The two steering modes. Each mode has a different set of "
            "dryback targets and EC targets. The engine adjusts the irrigation to make the values "
            "the same as these targets."),
    defterm("Zone and phase", "A zone (a row) is one of the 3 sections that you control "
            "independently. A phase is the part of the P0 to P3 cycle of each day that a row is in "
            "at this time."),
    figure(L.bars("The primary numbers (usual ranges, vegetative stage)",
            [("VWC %", 30), ("Dryback %", 18), ("EC mS/cm", 3)], unit="",
            note="These numbers are examples only. Replace them with your calibrated numbers.", maxv=35), 3,
      "The three numbers that the system reads for each decision: how much water, how much dryback, and how much salt."),
  ]})

SECTIONS.append({"id": "p0-p3-cycle", "kicker": "Cycle of each day",
  "title": "The P0&ndash;P3 cycle of each day",
  "blocks": [
    p("Each row has four phases during each day. The light schedule controls the phases (the "
      "default times are 10:00 for lights on and 22:00 for lights off). The sequence is always the "
      "same. First, the substrate dries a small quantity. Then the system fills the substrate again "
      "and keeps the VWC stable. At night, the VWC decreases."),
    ul([
      "<strong>P0 (morning dryback):</strong> After the lights come on, the system does not apply "
      "water. The substrate dries a small quantity (<code>p0_dryback_drop_percent</code>, for "
      "example 5 to 10%). P1 starts when the dryback is equal to this target, or after the maximum "
      "time (<code>p0_maximum_wait_time</code>). The default is 120 min.",
      "<strong>P1 (ramp-up):</strong> The first shot has the size "
      "<code>p1_initial_shot_size</code>. Each shot is larger than the shot before by "
      "<code>p1_shot_size_increment</code>, to a maximum of <code>p1_maximum_shot_size</code>. The "
      "time between shots is <code>p1_time_between_shots</code>. The phase has a minimum number and "
      "a maximum number of shots. The phase stops when the VWC is equal to or more than "
      "<code>p1_target_vwc</code>.",
      "<strong>P2 (maintenance):</strong> This phase is most of the day. The system applies water "
      "when the VWC becomes less than <code>p2_vwc_threshold</code>. If the EC ratio is more than "
      "approximately 1.2, the system applies more water to dilute the solution. If the EC ratio is "
      "less than approximately 0.8, the system applies less water.",
      "<strong>P3 (night):</strong> Usual irrigation stops a number of minutes before the lights go "
      "off. You set this number with <code>p3_veg_last_irrigation</code> / <code>_gen_</code>. Only "
      "emergency shots start when the VWC is less than <code>p3_emergency_vwc_threshold</code>. The "
      "zones stay in P3 all night.",
    ]),
    figure(L.line("VWC in one day (P0&ndash;P3)",
            [(0, 30), (1, 26), (2, 29), (3, 30), (4, 28), (5, 30), (6, 27), (7, 23)],
            ["10:00 on", "P0", "P1", "P2", "P2", "P2", "22:00 off", "night"],
            ylab="VWC %", ymin=18, ymax=34,
            note="VWC: P0 decreases slowly. P1 increases in steps. P2 stays near the target. P3 decreases to the emergency floor."), 4,
      "The curve shows one day with steering. The VWC has a small dryback in the morning and then increases to the target. Then it stays in a maintenance range, and at night it decreases at a controlled rate."),
    figure(L.flow("How the phase changes in one day",
            [("P3 night", "lights-on"), ("P0 dryback", "target or maximum time"),
             ("P1 ramp-up", "VWC &ge; target"), ("P2 maintenance", "before lights-off &rarr; back to P3")],
            note="The loop starts again each day."), 5,
      "A row operates in the loop in this sequence: P3 at night, P0 at lights on, P1, P2, and then P3 again before lights off."),
    p("The two steering modes select the targets that the engine uses. <strong>Vegetative</strong> "
      "steering has a high VWC, a small dryback (approximately 10 to 20%), a lower EC "
      "(approximately 3.0 mS/cm), and many small shots. <strong>Generative</strong> steering has a "
      "lower VWC, a larger dryback (approximately 25 to 50%), a higher EC (approximately 4.5 to 6.0 "
      "mS/cm), and a smaller number of larger shots. Set the mode for all rows with "
      "<code>select.crop_steering_steering_mode</code>, or set the mode for each row. A setting for "
      "one row overrides the setting for all rows. With &lsquo;Follow Main&rsquo;, the row uses the "
      "setting for all rows."),
    table(["Mode", "VWC target", "Dryback", "EC target", "Shots"], [
      ["<strong>Vegetative</strong>", "High", "Small (10 to 20%)", "Approximately 3.0 mS/cm", "Many small shots"],
      ["<strong>Generative</strong>", "Lower", "Large (25 to 50%)", "4.5 to 6.0 mS/cm", "A smaller number of larger shots"],
    ], cls="compact", caption="The two modes of steering. Select one mode for each row, or set a row to use the setting for all rows."),
  ]})

SECTIONS.append({"id": "controls-and-targets", "kicker": "Controls that you use",
  "title": "Irrigation controls and targets",
  "blocks": [
    p("Each day, you use some controls. Two arm switches set how much of the system operates. "
      "<strong>System enabled</strong> is the primary arm switch. When it is OFF, no irrigation can "
      "occur. If the engine cannot read the switch, it uses OFF as a fail-safe.</p><p><strong>Auto "
      "irrigation</strong> controls only the shots that the engine starts. When it is OFF, you can "
      "continue to start manual shots. These two settings give &lsquo;watch mode&rsquo;."),
    p("Some targets control the growth: the VWC values for each phase (<code>p1_target_vwc</code>, "
      "<code>p2_vwc_threshold</code>) and the dryback targets. The EC targets for each phase and "
      "each mode (<code>ec_target_veg_p0..p3</code> and <code>ec_target_gen_p0..p3</code>) also "
      "control the growth. The selection lists for each row let you use generative steering in one "
      "row and vegetative steering in the other rows. They also let you select the row that "
      "receives water first when only one row can start a shot. You can also make groups of zones "
      "to control the zones together."),
    ul([
      "When the <strong>EC stacking switch</strong> is ON, the engine can apply less water to "
      "increase the EC of the root zone. This setting gives generative steering. The switch is "
      "usually OFF for vegetative steering.",
      "<strong>Hardware that you can see:</strong> the pump (Tuya plug, approximately 490&nbsp;W "
      "when it operates), the relay of the main line, and the zone valves "
      "<code>switch.f2_row1/2/3</code>. Only one zone receives water at a time.",
      "<strong>Selection lists for each row:</strong> steering_mode, crop_profile (Follow Main and "
      "7 profiles), group (A to D), and &lsquo;priority&rsquo; (&lsquo;Critical&rsquo;, "
      "&lsquo;High&rsquo;, &lsquo;Normal&rsquo; or &lsquo;Low&rsquo;).",
      "<strong>The system calculates the shot time</strong> from <code>substrate_volume</code>, "
      "<code>dripper_flow_rate</code>, <code>drippers_per_plant</code> and the shot size in %. Set "
      "these values correctly. If you do not, each shot has an incorrect size.",
      "<strong>Safety limits for each row:</strong> <code>max_daily_volume</code> (L), "
      "<code>shot_size_multiplier</code>, and <code>plant_count</code>.",
    ]),
    table(["System enabled", "Auto irrigation", "Result"], [
      ["ON", "ON", "Usual operation. The engine starts automatic shots, and manual shots also operate."],
      ["ON", "OFF", "<strong>Watch mode</strong>: The system is armed, but it only monitors. Only manual shots operate."],
      ["OFF", "ON or OFF", "The system is fully disarmed. The gate stops each shot."],
    ], cls="compact", caption="The two types of &lsquo;off&rsquo;. For watch mode, set System enabled to ON and Auto irrigation to OFF. Do this while you calibrate."),
    callout("tip", "Use watch mode before automatic operation",
      p("Set <strong>System enabled to ON and Auto irrigation to OFF</strong> while you make sure "
        "that your numbers are correct. The engine is armed and calculates its decisions, but it "
        "does not start shots automatically. You can start manual test shots and monitor the "
        "changes in the room before you let the engine operate with full automatic control.")),
  ]})

SECTIONS.append({"id": "decision-gates", "kicker": "How the system makes decisions",
  "title": "Irrigation decision gates",
  "blocks": [
    p("When the engine makes the decision that a shot is necessary, the shot starts only if "
      "<strong>all the safety gates, in sequence,</strong> let it start. Each gate can stop the "
      "shot. The gates prevent an incorrect decision of the automatic system."),
    figure(L.flow("Sequence of the gates (all must let the shot start)",
            [("System armed?", "fail-safe: no reading stops the shot"),
             ("Auto irrigation ON?", "manual shots bypass this gate"),
             ("Zone ON, no override?", "the row must be in the steering"),
             ("Low float reads water?", "no dose or fill, tank not empty"),
             ("Source pH/EC in range, safety limits OK?", "then start the hardware")],
            note="Each gate can stop the shot."), 6,
      "The next gate operates only after the gate before it lets the shot start. The hardware sequence starts only after the last gate."),
    ul([
      "<strong>Sequence of the gates for a shot:</strong> First, the system is armed. Then Auto "
      "irrigation is ON (manual shots bypass this gate). Then the zone is ON and has no manual "
      "override. Then no dose is in progress, and the tank is not empty. Then the source pH and EC "
      "are in range (default pH 5.8 to 6.2). The last gates are the safety limits: the limit of "
      "volume for each day, the maximum EC and the maximum frequency.",
      "<strong>pH or EC not in range:</strong> The gate stops the shot and sends an alert to the "
      "phone. The alert has an &lsquo;Irrigate Anyway&rsquo; button.",
      "<strong>Tank guard:</strong> The guard stops a shot only when the low float reads empty. As "
      "a result, the system can continue to apply water while the quantity of water in the tank "
      "decreases.",
    ]),
    figure(L.flow("Hardware sequence (after the last gate)",
            [("Pump ON", "2 s pressure"), ("Main line ON", "wait 1 s"),
             ("Zone valve ON", "ON for the calculated time"), ("Stop", "valve &rarr; main line &rarr; pump OFF")],
            note="The components stop in the opposite sequence. This prevents water hammer and a pump that operates against a closed valve."), 7,
      "The sequence of the hardware when the system applies water. First the pump makes pressure. Then the system opens the valve of the row and keeps it open for the calculated time. At the end, the components stop in the opposite sequence."),
    callout("note", "The effect of source water without a gate",
      p("Source water can change slowly to a pH or an EC that is not in the range of the gate. This "
        "water can cause nutrient lockout or cause damage to the roots. The gate stops the shot and "
        "sends an alert to you. Thus the system does not apply a solution with an incorrect pH or "
        "EC to the room without an alert.")),
  ]})

SECTIONS.append({"id": "calibration-howto", "kicker": "Do this first",
  "title": "Calibration procedure",
  "blocks": [
    p("Calibration is the most important step in the procedure. The system operates correctly only "
      "if its number entities agree with the values of <em>your</em> substrate. The factory "
      "defaults are temporary values (50% VWC and 50% dryback). They are not values for your "
      "substrate. Dielectric probes for moisture give different readings in each substrate. Thus a "
      "calibration for the substrate is necessary before the numbers give correct information about "
      "the substrate." + _c("zawilski-calibration-2023")),
    steps([
      ("Monitor", "Use your usual procedure to apply water by hand for a small number of days. "
       "Monitor the VWC of each row. The reading immediately after you apply water is approximately "
       "the field capacity (the peak). The reading immediately before the next time that you apply "
       "water is the trough. Together they show the range of operation of that row."),
      ("Set the range", "Set <code>field_capacity</code> to a value that is a small quantity more "
       "than the highest peak. Set <code>p1_target_vwc</code> to the peak of each row after you "
       "apply water. Set <code>p2_vwc_threshold</code> to a value that is less than this peak by a "
       "small number of percent. A smaller difference between these two values gives a smaller "
       "range for vegetative steering."),
      ("Set the drybacks", "For vegetative steering, set the dryback to approximately 15 to 20%. "
       "For generative steering, set the dryback to approximately 25 to 45%. Set "
       "<code>p0_dryback_drop_percent</code> to 5 to 15%. Set the emergency floor to a value that "
       "is less than the usual trough by a small number of percent."),
      ("Set EC targets", "For vegetative steering, set the EC target to a value that is a small "
       "quantity more than the feed EC. For generative steering, set it to a value that is much "
       "more than the feed EC. The values <code>p2_ec_high/low_threshold</code> are multipliers of "
       "the target. At 1.2, the engine dilutes the solution when the EC is more than 120% of the "
       "target. At 0.8, the engine applies less water when the EC is less than 80% of the target."),
      ("Operate and adjust", "Let the system operate for some cycles in watch mode. Compare the values "
       "that the system calculates with the values that the probes measure. Adjust the numbers to "
       "make them more accurate."),
    ]),
    figure(L.zones("Read the range of operation of one row", 8, 34,
            [(8, 13, L.REDL, "P3 floor"), (13, 19, L.AMBL, "trough"),
             (19, 26, L.GL, "P2 range"), (26, 30, L.BLUL, "P1 target"), (30, 34, L.PURL, "field capacity")],
            unit="% VWC",
            note="Peaks (after water) and troughs (before the next water) when you apply water by hand set each threshold."), 8,
      "The range that you read when you apply water by hand. The emergency floor is below the "
      "trough. The P2 range is below the P1 target. Field capacity is the limit at the top."),
    p("The growth of the roots changes the readings of the probe during a crop. Thus examine the "
      "range at intervals. Do not calibrate one time only." + _c("kang-rootgrowth-2019")),
    table(["Setting", "Row 1", "Row 2", "Row 3", "Function"], [
      ["p1_target_vwc", "26", "22", "18", "The peak VWC. P1 fills the substrate again to this value."],
      ["p2_vwc_threshold", "22", "19", "15", "Apply water when the VWC becomes less than this value."],
      ["vegetative_dryback_target", "18", "18", "18", "The quantity by which P0 dries the substrate (%)"],
      ["p0_dryback_drop", "8", "8", "8", "The quantity of dryback in the morning (%)"],
      ["emergency floor", "15", "14", "11", "The VWC that starts an emergency shot in P3 at night"],
      ["field_capacity (for all rows)", "30", "30", "30", "The VWC peak at saturation (the &lsquo;full&rsquo; value)"],
    ], cls="compact", caption="The start numbers for F2 that the source recommends. The source calculated these numbers from the ranges that it recorded when it applied water by hand. They are start points, not permanent settings."),
    callout("warn", "The defaults are temporary values, not values for your substrate",
      p("Calibrate first, then arm the system. If you use the factory defaults (50% and 50%) "
        "without calibration, the engine uses numbers that are not related to your substrate. As a "
        "result, the steering has no value.")),
  ]})

SECTIONS.append({"id": "recipes", "kicker": "Tasks for each day", "title": "Procedures for usual operation",
  "blocks": [
    p("Most usual tasks have a safe procedure. We recommend that you use the services of the "
      "integration and not the hardware switches directly. The services start the full hardware "
      "sequence with all the gates. As a result, the system always does the safety checks."),
    table(["Task", "Safe method", "Information"], [
      ["Start a manual shot", "Use the service <code>crop_steering.execute_irrigation_shot</code> (zone, duration_seconds, shot_type: manual)", "Starts the full sequence with all the gates"],
      ["Hardware directly (use it only if no other method is possible)", "Pump &rarr; main line &rarr; valve ON. To stop, set the components OFF in the opposite sequence.", "Only one row at a time"],
      ["Set a phase by hand", "Change <code>select.crop_steering_irrigation_phase</code>", "The change occurs immediately. It bypasses the usual changes of phase. The list then shows that phase."],
      ["&lsquo;Irrigate Anyway&rsquo; override", "The button on the phone after an alert for pH or EC", "It bypasses only the pH/EC gate, for 30 min. It stops automatically when the readings are again in range."],
      ["Remove a row from the steering, or set a row to manual override", "<code>zone_N_enabled</code> OFF (the row is not in the steering), or <code>zone_N_manual_override</code> ON (the row stays in the steering)", "Manual override: you apply water by hand while the row stays in the steering"],
      ["Use generative steering", "Select &lsquo;Generative&rsquo; in the steering mode (for all rows or for one row)", "The setting for one row overrides the setting for all rows"],
      ["Set the water counters to zero", "Automatic: each day at midnight and each week on Monday", "To set the counters to zero before this time, stop AppDaemon and start it again"],
    ], cls="compact", caption="A reference for the tasks that you do most frequently. If you are not sure, use the service and not the hardware switch."),
    callout("note", "&lsquo;Irrigate Anyway&rsquo; bypasses only one gate",
      p("It bypasses the <em>pH/EC gate only</em> for 30 minutes. All the other interlocks continue "
        "to operate: system armed, tank not empty, and the limit of volume for each day. It stops "
        "automatically when the pH and EC are in range again.")),
  ]})

SECTIONS.append({"id": "safety-troubleshooting", "kicker": "When a fault occurs",
  "title": "Safety interlocks and troubleshooting",
  "blocks": [
    p("The system has some fail-safes: the pH/EC gate for the source water, a tank dry-run guard, "
      "and a blocked-dripper guard. The system also has a fail-safe for the arm switch and a "
      "recorded condition. The tank dry-run guard stops a shot only when the low float reads empty. "
      "The blocked-dripper guard stops a row for 2 hours after too many shots that fail.</p><p>If "
      "the system cannot make sure of the condition of the arm switch, it uses the value OFF. The "
      "system records its condition at intervals of 5 minutes. After the system starts again, each "
      "zone starts in its recorded phase."),
    callout("danger", "The EMERGENCY button does NOT disarm the engine",
      p("To stop the system for more than a short time, use the EMERGENCY button and set "
        "<strong>System enabled</strong> to OFF. The dashboard button <strong>EMERGENCY, ALL "
        "OFF</strong> (<code>script.f2_irrigation_all_off</code>) quickly stops the three hardware "
        "components, but the engine stays <em>armed</em>. The engine can start the components again "
        "at its next check of the phase, in approximately 60&nbsp;s. To disarm the engine, set "
        "<strong>System enabled</strong> to OFF.")),
    table(["Trigger", "Effect", "Condition of the engine after"], [
      ["Dashboard EMERGENCY button", "Quickly stops the pump, the main line and the valves", "The engine is ARMED. It can start shots again at the next check in approximately 60 s"],
      ["System enabled OFF", "The gate stops each shot", "DISARMED, and the engine stays in this condition"],
      ["Automatic emergency stop of the engine", "Internal. The engine stops the row that has the fault", "ARMED. The row with the fault stays stopped"],
    ], cls="compact", caption="Two methods to stop, and the condition of the engine after each method. Only System enabled OFF keeps the engine disarmed."),
    steps([
      ("Repair the cause", "First, repair the problem in the hardware. Examples are an empty tank, a bent line, a defective probe and a blockage in a dripper."),
      ("Make sure that the hardware is OFF", "Make sure that the pump, the main line and all the valves show OFF."),
      ("Examine the arm condition of the engine", "Examine System enabled and Auto irrigation before you arm the engine again."),
      ("Arm the engine again and do a check", "Arm the engine again. Then read <code>sensor.crop_steering_current_phase</code> to see the phase that is in operation."),
      ("Monitor one cycle", "Do not go away. Monitor a full cycle. Make sure that each shot starts correctly. Then you can use the system in automatic operation again."),
    ]),
    table(["Symptom", "Possible cause", "Procedure"], [
      ["Zones stay in one phase", "The condition for the change to the next phase does not occur, or the target is incorrect", "Compare the exit threshold of the phase with the VWC at this time"],
      ["The valve is open, but there is no flow", "The pump is OFF, the line is bent, or there is a blockage in a dripper", "Examine the pump and the line. Remove the blockage in the dripper."],
      ["The Status value or the Water-today value is &lsquo;unknown&rsquo;", "The engine does not operate, or the sensors have no data", "Stop AppDaemon and start it again. Make sure that the probes send readings."],
      ["Frequent alerts for pH or EC", "The source water is not in range, or the sensor has drift", "Do a test of the solution. Make sure that the pH/EC probe is correct."],
      ["The blocked-dripper guard stops a row many times", "4 or more shots that fail in 30 min", "Remove the blockage in the dripper. The row starts again automatically after 2 h."],
      ["&lsquo;Irrigation already in progress, skipping&rsquo; in each cycle", "A flag stays ON after a shot stops before its end", "Stop AppDaemon and start it again (<code>ha addons restart a0d7b954_appdaemon</code>). The system reads the phase and the counters from the disk."],
    ], cls="compact", caption="The list of troubleshooting steps from the source. Most faults have a cause in the hardware or a flag that stays ON."),
    callout("warn", "A gap in the data to monitor",
      p("Examine the calibration of the probe before you use EC steering. The source shows that "
        "<code>sensor.crop_steering_dryback_percentage</code> and the substrate EC can give values "
        "that are too low to be correct (Row&nbsp;1 at 0.48&nbsp;mS/cm). Salinity has a strong "
        "effect on the readings of dielectric probes." + _c("qi-salinity-2024"))),
  ]})

SECTIONS.append({"id": "expectations", "kicker": "The limits", "title": "Expected results and limitations",
  "blocks": [
    callout("key", "This is a controller, not a system that does all tasks",
      ul(["<strong>The limit of the quality of the steering is the quality of the "
          "calibration.</strong> The factory defaults of 50% and 50% are temporary values. Before "
          "you use automatic operation, replace them with numbers from your substrate.",
          "<strong>Use watch mode first.</strong> In watch mode, the system is armed but it only "
          "monitors. Thus you can make sure that the thresholds are correct. You can also do a test "
          "of the pipes and valves by hand, before you let the system operate with full automatic "
          "control.",
          "<strong>The recommended numbers are start points.</strong> Adjust them in some cycles. "
          "If you do not adjust them, the rooms can receive too much water or not sufficient water.",
          "<strong>Some sensors can give incorrect information.</strong> The dryback percentage can "
          "have no data, and the EC can show values that are too low to be correct. Make sure that "
          "the probe calibration is correct before you use EC steering.",
          "<strong>Fail-safes give protection to the hardware, but they use the sensor readings as "
          "correct values.</strong> A defective probe or float can cause an incorrect decision, and "
          "the values can stay in the &lsquo;safe&rsquo; range."], "tight")),
    p("F2 is an accurate controller. It does not give results that are always correct. Monitor your "
      "numbers with time on a process-control chart. With this chart, you can find the difference "
      "between a signal and the usual variation, before you make a change." + _c("mohammed-spc-2024") +
      "</p><p>For the cultivation information about the dryback and EC controls, read the paper on "
      "<a href='coco-crop-steering.html'>coco crop steering</a>. Next, read the paper on the <a "
      "href='root-zone-teros12.html'>root-zone sensor</a>. It gives information about the probes "
      "that the system uses for all its decisions."),
  ]})
