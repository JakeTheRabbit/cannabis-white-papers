# -*- coding: utf-8 -*-
"""Paper: F2 crop steering, the daily operating manual (beginner, operational)."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        stagecard, grid, card, chip, kv, steps)
import figs_lib as L

SLUG = "f2-crop-steering"
TITLE = "F2 crop steering: the daily operating manual"
EYEBROW = "Precision · Crop steering"
SUB = ("Run an autonomous crop-steering irrigation controller day to day. This is the plain-language "
       "starter guide: the P0&ndash;P3 cycle, moisture and salt targets, the controls you actually "
       "touch, the safety fail-safes, and what to do when something looks wrong.")
META = [("gauge", "Precision"), ("image", "12 diagrams"),
        ("doc", "Operational guide"), ("clock", "~18 min read")]
RELATED = ["coco-crop-steering", "root-zone-teros12", "smart-watering-vrwe"]
REF_IDS = ["caplan-drought-2019", "zawilski-calibration-2023", "qi-salinity-2024",
           "kang-rootgrowth-2019", "mohammed-spc-2024"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

SECTIONS.append({"id": "what-this-is", "kicker": "Start here",
  "title": "What this system is, and what crop steering means",
  "blocks": [
    callout("evidence", "Grain of salt",
      "<p><strong>Operational / provisional:</strong> Default VWC numbers are one facility&rsquo;s probe-native "
      "placeholders after hand-watering. Caplan drought supports controlled deficit as a concept &mdash; not a "
      "copy-paste of these exact setpoints. Calibrate media before arming automation.</p>"),
    lead("F2 is an <strong>autonomous irrigation controller</strong> for a veg grow room. It is software "
         "that reads moisture and salt probes in the root zone and decides, on its own, when to fire "
         "a watering shot through a pump and valves. You set the targets. It does the watering."),
    p("<strong>Crop steering</strong> means pushing the plant toward one of two kinds of growth by "
      "controlling exactly how and when it waters. <em>Vegetative</em> steering (bulking) keeps the "
      "medium wet with many small waterings and only a small drying-out. <em>Generative</em> steering "
      "(the flower or stress push) uses a bigger drying-out, a saltier root zone, and fewer, larger "
      "waterings. Even a mild, deliberate water deficit applied at the right time shifts a cannabis "
      "plant generatively without losing yield." + _c("caplan-drought-2019")),
    p("The system runs in two cooperating layers. A <strong>Home Assistant integration</strong> gives "
      "you every on-screen control and reading. An <strong>AppDaemon engine</strong> "
      "(<code>master_crop_steering_app.py</code>) is the decision-making brain that fires the shots. "
      "The room is wired as <strong>3 rows (zones)</strong>, each with its own moisture and salt probe "
      "and its own valve, all fed from one shared tank, one pump, and one main line."),
    figure(grid([
        card("Home Assistant integration", "The dashboard. Every control, setting and readout you see and touch.", "Layer 1"),
        card("AppDaemon engine", "The autonomous brain. Reads probes, decides, fires shots through the hardware.", "Layer 2"),
        card("Hardware chain", "Pump &rarr; main line &rarr; 3 zone valves. 3 probe pairs feed readings back up.", "Layer 3"),
      ], cols=3), 1,
      "The two software layers and the hardware they drive. Controls flow down, probe readings flow back up."),
    figure(L.flow("Room layout: 3 rows from one tank",
            [("Veg tank", "shared water source"), ("Pump", "one pump for all rows"),
             ("Main line", "branches to each row"), ("Row 1/2/3 valves", "one VWC + EC probe each")],
            note="Only one row waters at a time."), 2,
      "One tank, one pump, one main line feeding three independently steered rows. Each row has its own probe pair and valve."),
    callout("key", "Two things to memorise",
      ul(["The <strong>&lsquo;Phase (manual set)&rsquo;</strong> dropdown is an <em>override</em>. It "
          "shows what you last picked, not the live phase. Read "
          "<code>sensor.crop_steering_current_phase</code> for the truth.",
          "Disarming is always safe by design. "
          "<code>switch.crop_steering_system_enabled = OFF</code> means nothing can fire, ever."], "tight")),
  ]})

SECTIONS.append({"id": "key-terms", "kicker": "Vocabulary", "title": "Key terms, defined",
  "blocks": [
    p("Three measurements run the whole system. Learn these first. Everything else builds on them."),
    defterm("VWC (volumetric water content)", "How wet the growing medium is, shown as a percent. "
            "60% VWC means water fills 60% of the medium's volume."),
    defterm("EC (electrical conductivity)", "How salty or strong the root zone, or the feed water, is, "
            "in mS/cm. Higher EC means a stronger, saltier solution."),
    defterm("Dryback", "The percent the medium dries down from its post-watering peak as the plant "
            "drinks. The single most important steering lever."),
    defterm("Shot", "One timed burst of water, sized as a percent of the medium's volume. The duration "
            "in seconds comes from substrate volume, dripper flow rate and shot size."),
    defterm("Field capacity", "The saturated peak VWC right after irrigation drains. The medium's "
            "&lsquo;full&rsquo; mark."),
    defterm("EC ratio", "Measured EC divided by target EC. Above 1 means too salty, so water more to "
            "dilute. Below 1 means too weak, so hold back."),
    defterm("Vegetative vs Generative", "The two steering modes. Each selects a different set of "
            "dryback and EC targets for the engine to chase."),
    defterm("Zone / phase", "A zone (row) is one of the 3 independently steered sections. A phase is "
            "where a row sits in its daily P0&ndash;P3 cycle."),
    figure(L.bars("Where the core numbers live (typical veg ranges)",
            [("VWC %", 30), ("Dryback %", 18), ("EC mS/cm", 3)], unit="",
            note="Illustrative magnitudes only. Your calibrated numbers replace these.", maxv=35), 3,
      "The three living numbers behind every decision: how wet, how far it dries, and how salty."),
  ]})

SECTIONS.append({"id": "p0-p3-cycle", "kicker": "The core loop", "title": "The P0&ndash;P3 daily cycle",
  "blocks": [
    p("Each row moves through four phases across the lights-on day, driven by the light schedule "
      "(defaults: lights on 10:00, off 22:00). The rhythm is always the same. Dry a little, refill, "
      "maintain, then wind down for the night."),
    ul([
      "<strong>P0 (morning dryback):</strong> after lights-on the system waters nothing and lets the "
      "medium dry a small amount (<code>p0_dryback_drop_percent</code>, e.g. 5&ndash;10%). Exits to P1 "
      "when that target is hit OR when <code>p0_maximum_wait_time</code> expires (default 120 min).",
      "<strong>P1 (ramp-up):</strong> shots start at <code>p1_initial_shot_size</code>, grow by "
      "<code>p1_shot_size_increment</code>, are capped at <code>p1_maximum_shot_size</code>, spaced by "
      "<code>p1_time_between_shots</code>, and bounded by min/max shot counts. Exits when "
      "VWC &ge; <code>p1_target_vwc</code>.",
      "<strong>P2 (maintenance):</strong> the bulk of the day. Waters whenever VWC drops below "
      "<code>p2_vwc_threshold</code>; if the EC ratio runs above ~1.2 it waters MORE (to dilute), "
      "below ~0.8 it holds back.",
      "<strong>P3 (overnight):</strong> normal irrigation stops a set number of minutes before "
      "lights-off (<code>p3_veg_last_irrigation</code> / <code>_gen_</code>); only emergency top-ups "
      "fire below <code>p3_emergency_vwc_threshold</code>. Zones hold P3 all night.",
    ]),
    figure(L.line("VWC across one lights-on day (P0&ndash;P3)",
            [(0, 30), (1, 26), (2, 29), (3, 30), (4, 28), (5, 30), (6, 27), (7, 23)],
            ["10:00 on", "P0", "P1", "P2", "P2", "P2", "22:00 off", "overnight"],
            ylab="VWC %", ymin=18, ymax=34,
            note="P0 gentle decline, P1 stair-step rise to target, P2 sawtooth maintenance, P3 overnight fall to the emergency floor."), 4,
      "One steered day: a small morning dryback, a refill to target, a maintenance band, then a controlled overnight wind-down."),
    figure(L.flow("Phase transitions around the day",
            [("P3 overnight", "lights-on"), ("P0 dryback", "target met / timeout"),
             ("P1 ramp-up", "VWC &ge; target"), ("P2 maintain", "before lights-off &rarr; back to P3")],
            note="The loop repeats every lights-on cycle."), 5,
      "How a row walks the loop: overnight P3 into P0 at lights-on, up through P1 to P2, then back to P3 before dark."),
    p("The two steering modes pick which targets the engine chases. <strong>Vegetative</strong> means "
      "high VWC, modest dryback (~10&ndash;20%), lower EC (~3.0 mS/cm), many small shots. "
      "<strong>Generative</strong> means lower VWC, bigger dryback (~25&ndash;50%), higher EC "
      "(~4.5&ndash;6.0 mS/cm), fewer larger shots. Set the mode globally with "
      "<code>select.crop_steering_steering_mode</code> or per row. A row override beats the global, and "
      "&lsquo;Follow Main&rsquo; means use the global."),
    table(["Mode", "VWC target", "Dryback", "EC target", "Shot pattern"], [
      ["<strong>Vegetative</strong>", "High", "Modest (10&ndash;20%)", "~3.0 mS/cm", "Many small shots"],
      ["<strong>Generative</strong>", "Lower", "Bigger (25&ndash;50%)", "4.5&ndash;6.0 mS/cm", "Fewer, larger shots"],
    ], cls="compact", caption="The two steering recipes. Choose one per row, or let a row follow the main setting."),
  ]})

SECTIONS.append({"id": "controls-and-targets", "kicker": "What you touch",
  "title": "The controls and targets that matter",
  "blocks": [
    p("Day to day you touch a handful of controls. Two arm switches set how &lsquo;on&rsquo; the system "
      "is. <strong>System enabled</strong> is the master arm. OFF means nothing irrigates ever, and the "
      "engine fails safe to OFF if it cannot read the switch. <strong>Auto irrigation</strong> only "
      "governs engine-driven shots. Turning it OFF still lets manual shots through, which is how you run "
      "&lsquo;watch mode.&rsquo;"),
    p("The targets that steer growth are the per-phase VWC numbers (<code>p1_target_vwc</code>, "
      "<code>p2_vwc_threshold</code>), the dryback targets, and the per-phase and per-mode EC targets "
      "(<code>ec_target_veg_p0..p3</code> and <code>ec_target_gen_p0..p3</code>). Per-row selects let "
      "you push one row generative while the others stay veg, set who waters first when only one row "
      "can fire, and group zones to coordinate them."),
    ul([
      "<strong>EC stacking switch</strong> ON lets the engine raise root-zone EC by reducing water, a "
      "generative push. Usually OFF for veg.",
      "<strong>Hardware you can see:</strong> the pump (Tuya plug, ~490&nbsp;W running), the main-line "
      "relay, and <code>switch.f2_row1/2/3</code> zone valves. Only one waters at a time.",
      "<strong>Per-row selects:</strong> steering_mode, crop_profile (Follow Main + 7 profiles), group "
      "(A&ndash;D), and priority (Critical / High / Normal / Low).",
      "<strong>Shot duration is computed</strong> from <code>substrate_volume</code>, "
      "<code>dripper_flow_rate</code>, <code>drippers_per_plant</code> and shot size %. Set these "
      "correctly or every shot is the wrong size.",
      "<strong>Per-row safety caps:</strong> <code>max_daily_volume</code> (L), "
      "<code>shot_size_multiplier</code>, and <code>plant_count</code>.",
    ]),
    table(["System enabled", "Auto irrigation", "What happens"], [
      ["ON", "ON", "Normal: autonomous shots fire AND manual shots work"],
      ["ON", "OFF", "<strong>Watch mode</strong>: armed but observe-only, manual shots only"],
      ["OFF", "either", "Fully disarmed. Every shot blocked at the gate"],
    ], cls="compact", caption="The two levels of &lsquo;off&rsquo;. Use ON/OFF together for watch mode while you calibrate."),
    callout("tip", "Watch mode is your friend",
      p("Run <strong>System enabled ON, Auto irrigation OFF</strong> while you confirm your numbers. "
        "The engine is armed and computing decisions but will not fire on its own. You can fire manual "
        "test shots and watch how the room responds before granting full autonomy.")),
  ]})

SECTIONS.append({"id": "decision-gates", "kicker": "How it decides",
  "title": "How a single irrigation decision is made (the gates)",
  "blocks": [
    p("When the engine decides a shot is needed, that shot only fires if it passes <strong>every "
      "safety gate in order</strong>. A single failed gate blocks it. This is what stops an autonomous "
      "system making a bad call."),
    figure(L.flow("The gate chain (all must pass)",
            [("System armed?", "fail-safe: unreadable = blocked"),
             ("Auto on?", "manual can bypass"),
             ("Zone enabled & no override?", "row must be in play"),
             ("Not dosing/filling, tank not empty?", "low float must read water"),
             ("Source pH/EC in range, safety limits OK?", "then fire the hardware")],
            note="Any failed gate blocks the shot."), 6,
      "Each check must pass before the next is tried. Only after the last gate does the hardware sequence run."),
    ul([
      "<strong>Order:</strong> system armed &rarr; auto-irrigation (manual bypasses) &rarr; zone "
      "enabled &rarr; no manual override &rarr; not dosing &rarr; tank not empty &rarr; source pH/EC in "
      "range (default pH 5.8&ndash;6.2) &rarr; safety limits (daily-volume cap, max-EC ceiling, "
      "max-frequency).",
      "<strong>pH/EC out of range</strong> blocks the shot and sends a phone alert with an "
      "&lsquo;Irrigate Anyway&rsquo; button.",
      "<strong>Tank guard</strong> blocks only when the low float reads empty, so the system can keep "
      "watering as the tank drains down.",
    ]),
    figure(L.flow("Hardware fire sequence (when all gates pass)",
            [("Pump ON", "2 s prime"), ("Main line ON", "1 s settle"),
             ("Zone valve ON", "hold calculated duration"), ("Shut down", "valve &rarr; main &rarr; pump OFF")],
            note="Components shut off in reverse order to avoid water hammer and dead-heading the pump."), 7,
      "The physical watering sequence: build pressure first, open the row, hold for the computed duration, then back out in reverse."),
    callout("note", "Why pH/EC gating matters",
      p("Source water that drifts out of the pH or EC window can lock out nutrients or burn roots. "
        "Gating on it, and alerting you rather than watering quietly, guards against feeding a bad "
        "solution to the whole room.")),
  ]})

SECTIONS.append({"id": "calibration-howto", "kicker": "Do this first",
  "title": "Calibration: getting the numbers right before you trust it",
  "blocks": [
    p("Calibration is the most important practical step. The system only behaves correctly if its "
      "number entities match your <em>actual</em> medium. The factory defaults are placeholders "
      "(50% VWC / 50% dryback), not your substrate. Dielectric moisture probes read differently in "
      "every medium, so a substrate-specific calibration is what makes the numbers mean anything." +
      _c("zawilski-calibration-2023")),
    steps([
      ("Observe", "Hand-water normally for a few days and watch each row's VWC. The reading just after "
       "watering is roughly field capacity (the peak). The reading just before the next watering is the "
       "trough. Together they define that row's operating band."),
      ("Set the band", "Set <code>field_capacity</code> just above the highest peak, "
       "<code>p1_target_vwc</code> to each row's post-water peak, and <code>p2_vwc_threshold</code> a "
       "few percent below that. A smaller gap means a tighter veg band."),
      ("Set the drybacks", "Veg ~15&ndash;20%, gen ~25&ndash;45%. <code>p0_dryback_drop_percent</code> "
       "5&ndash;15%. Set the emergency floor a few percent below the normal trough."),
      ("Set EC targets", "Slightly above feed EC for veg, well above for generative. "
       "<code>p2_ec_high/low_threshold</code> are multipliers on target (1.2 dilutes above 120%, "
       "0.8 conserves below 80%)."),
      ("Run and refine", "Let it run a few cycles in watch mode, compare predicted against actual, and "
       "tighten the numbers."),
    ]),
    figure(L.zones("Reading one row's operating band", 8, 34,
            [(8, 13, L.REDL, "P3 floor"), (13, 19, L.AMBL, "trough"),
             (19, 26, L.GL, "P2 band"), (26, 30, L.BLUL, "P1 target"), (30, 34, L.PURL, "field cap")],
            unit="% VWC",
            note="Peaks (after watering) and troughs (before next) from hand-watering set every threshold."), 8,
      "The band you read from hand-watering: the emergency floor sits below the trough; the P2 band sits "
      "below the P1 target; field capacity caps the top."),
    p("Root growth itself changes how the probe reads over a run, so re-check the band occasionally "
      "rather than calibrating once and forgetting it." + _c("kang-rootgrowth-2019")),
    table(["Setting", "Row 1", "Row 2", "Row 3", "What it does"], [
      ["p1_target_vwc", "26", "22", "18", "Peak VWC P1 refills to"],
      ["p2_vwc_threshold", "22", "19", "15", "Water when VWC drops below this"],
      ["vegetative_dryback_target", "18", "18", "18", "How far P0 dries (%)"],
      ["p0_dryback_drop", "8", "8", "8", "Morning dryback amount (%)"],
      ["emergency floor", "15", "14", "11", "P3 overnight top-up trigger"],
      ["field_capacity (global)", "30", "30", "30", "Saturated peak / &lsquo;full&rsquo; mark"],
    ], cls="compact", caption="The source's recommended F2 starting numbers, derived from its hand-watered ranges. Starting points, not final settings."),
    callout("warn", "Defaults are placeholders, not your substrate",
      p("If you skip calibration and run the 50%/50% factory defaults, the steering is meaningless. The "
        "engine chases numbers that have nothing to do with your medium. Calibrate first, then arm.")),
  ]})

SECTIONS.append({"id": "recipes", "kicker": "Everyday tasks", "title": "How-to recipes for common jobs",
  "blocks": [
    p("Most routine actions have a safe, prescribed method. Prefer the integration services over raw "
      "switch-flipping. The services run the full gated hardware sequence so you cannot skip a safety "
      "check by accident."),
    table(["Task", "Safe method", "Caution"], [
      ["Fire a manual shot", "Service <code>crop_steering.execute_irrigation_shot</code> (zone, duration_seconds, shot_type: manual)", "Runs the full gated sequence"],
      ["Raw hardware (last resort)", "Pump &rarr; main &rarr; valve ON; reverse to stop", "One row at a time only"],
      ["Force a phase", "Change <code>select.crop_steering_irrigation_phase</code>", "Immediate; bypasses normal transitions; selector then shows that phase"],
      ["Irrigate Anyway override", "Phone button after a pH/EC alert", "30-min bypass of the pH/EC gate ONLY; auto-clears when readings return in range"],
      ["Disable vs pause a row", "<code>zone_N_enabled</code> OFF (excluded) vs <code>zone_N_manual_override</code> ON (stays in steering)", "Pause = hand-water while steered"],
      ["Switch to generative", "Select &lsquo;Generative&rsquo; on steering mode (global or per-row)", "Per-row beats global"],
      ["Reset water counters", "Automatic: daily at midnight, weekly Monday", "Restart AppDaemon to re-init early"],
    ], cls="compact", caption="Quick-reference for the jobs you'll do most. When in doubt, use the service, not the raw switch."),
    callout("note", "&lsquo;Irrigate Anyway&rsquo; is narrow on purpose",
      p("It grants a 30-minute bypass of the <em>pH/EC gate only</em>. Every other interlock still "
        "applies: system armed, tank not empty, daily-volume cap. It auto-clears the moment pH/EC return "
        "in range.")),
  ]})

SECTIONS.append({"id": "safety-troubleshooting", "kicker": "When it goes wrong",
  "title": "Safety fail-safes, emergency stop, and troubleshooting",
  "blocks": [
    p("The system has layered fail-safes: the pH/EC source-water gate, a tank dry-run guard (blocks "
      "only when the low float reads empty), a blocked-dripper guard that parks a row for 2 hours after "
      "too many failed shots, fail-safe reads (an unconfirmed arm switch is treated as disabled), and "
      "persistent state saved every 5 minutes so zones come back in their saved phase after a restart."),
    callout("danger", "The EMERGENCY button does NOT disarm the engine",
      p("There are two ways to force-stop and they differ in a way that matters. The dashboard "
        "<strong>EMERGENCY, ALL OFF</strong> button (<code>script.f2_irrigation_all_off</code>) kills "
        "the three hardware pieces fast but leaves the engine <em>armed</em>. It may re-energise on its "
        "next ~60&nbsp;s phase-check. To truly disarm, flip <strong>System enabled OFF</strong>. For "
        "anything beyond a brief stop, use both.")),
    table(["Trigger", "What it touches", "Engine state after"], [
      ["Dashboard EMERGENCY button", "Kills pump, main, valves fast", "Still ARMED, can re-fire next ~60 s check"],
      ["System enabled OFF", "Blocks every shot at the gate", "Durably DISARMED"],
      ["Engine auto emergency stop", "Internal: parks the affected row", "Armed, but offending row held"],
    ], cls="compact", caption="Two ways to stop, and what each one leaves behind. Only System enabled OFF disarms durably."),
    steps([
      ("Fix the root cause", "Sort the physical problem first: empty tank, kinked line, bad probe, blocked dripper."),
      ("Confirm hardware off", "Verify pump, main line and all valves read off."),
      ("Check engine arm state", "Look at System enabled and Auto irrigation before re-arming."),
      ("Re-arm and sanity-check", "Re-arm, then read <code>sensor.crop_steering_current_phase</code> for the live phase."),
      ("Watch one cycle", "Do not walk away. Watch a full cycle fire correctly before trusting it again."),
    ]),
    table(["Symptom", "Likely cause", "What to do"], [
      ["Zones stuck in one phase", "Transition condition never met / bad target", "Check the phase's exit threshold against live VWC"],
      ["Valve open but no flow", "Pump off, kinked line, blocked dripper", "Check pump state and the line; clear the dripper"],
      ["Status / Water-today reads unknown", "Engine not running or sensors unpopulated", "Restart AppDaemon; confirm probes report"],
      ["Repeated pH/EC alerts", "Source water genuinely out of range, or sensor drift", "Test the solution; verify the pH/EC probe"],
      ["Row repeatedly parked as blocked dripper", "4+ failed shots in 30 min", "Clear the physical dripper; row auto-releases after 2 h"],
      ["&lsquo;Irrigation already in progress, skipping&rsquo; every cycle", "Stuck flag after a mid-shot kill", "Restart AppDaemon (<code>ha addons restart a0d7b954_appdaemon</code>). Phase + counters restore from disk"],
    ], cls="compact", caption="The troubleshooting list from the source. Most faults trace to a physical cause or a stale flag."),
    callout("warn", "A known data gap to watch",
      p("The source flags that <code>sensor.crop_steering_dryback_percentage</code> and substrate EC "
        "reads can be suspiciously low (Row&nbsp;1 at 0.48&nbsp;mS/cm). Salinity strongly affects how "
        "dielectric probes report." + _c("qi-salinity-2024") + " Check probe calibration before "
        "trusting EC steering.")),
  ]})

SECTIONS.append({"id": "expectations", "kicker": "Reality check", "title": "Realistic expectations",
  "blocks": [
    callout("key", "This is a controller, not a magic autopilot",
      ul(["<strong>Steering quality is bounded by calibration.</strong> The factory 50%/50% defaults "
          "are placeholders. Replace them with numbers from your own medium before you trust autonomous mode.",
          "<strong>Run watch mode first.</strong> Armed but observe-only, so you confirm thresholds and "
          "hand-test plumbing before granting full autonomy.",
          "<strong>Recommended numbers are starting points.</strong> Refine them over several cycles. "
          "Treating them as final is how rooms get over- or under-watered.",
          "<strong>Some sensors can mislead.</strong> Dryback-percentage may be unpopulated and EC can "
          "read suspiciously low. Verify probe calibration before trusting EC steering.",
          "<strong>Fail-safes guard hardware, but they trust the sensors.</strong> A bad probe or float "
          "can still cause a wrong decision well inside the &lsquo;safe&rsquo; envelope."], "tight")),
    p("Treat F2 like a sharp tool, not an oracle. Watching is a discipline worth keeping. Tracking "
      "your numbers over time the way a process-control chart does lets you tell a real signal from "
      "ordinary noise before you act on it." + _c("mohammed-spc-2024") + " For the cultivation theory "
      "behind the dryback and EC levers, read the "
      "<a href='coco-crop-steering.html'>coco crop steering</a> paper. To understand the probes the "
      "whole system trusts, read <a href='root-zone-teros12.html'>root-zone sensing</a> next."),
  ]})
