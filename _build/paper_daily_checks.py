# -*- coding: utf-8 -*-
"""Paper: daily checks that mostly fill themselves in."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        grid, card, chip, kv, steps)
import figs_lib as L
import figs_dailychecks as D

SLUG = "daily-checks"
TITLE = "Daily checks: the self-completing facility round"
EYEBROW = "Operations · Daily checks"
SUB = ("The best daily check is the one that mostly fills itself in. Let Home Assistant confirm "
       "everything it can measure, leave the human only the physical walk-around, make the rest one "
       "tap, and the check gets done every day, honestly, with an audit trail that holds up.")
META = [("dashboard", "Operations & SOPs"), ("image", "7 diagrams"),
        ("quote", "Research-backed · 13 sources"), ("clock", "~16 min read")]
RELATED = ["plant-state-dashboard", "closed-loop", "grow-room-systems"]
REF_IDS = ["gawande-checklist-manifesto", "fogg-behavior-model", "gollwitzer-implementation-intentions",
           "checklist-compliance-illusion", "haynes-surgical-checklist-2009",
           "ha-todo-integration", "ha-template-alert-statistics", "aroya-rootzone-steering",
           "eu-gmp-annex1", "who-gacp-2003", "globalgap-cpcc", "haccp-prerequisite-ssop",
           "digital-checklist-adherence"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

# 1 -----------------------------------------------------------------
SECTIONS.append({"id": "intro", "kicker": "Start here", "title": "Why daily checks fail, and the fix",
  "blocks": [
    lead("Every facility has a daily check sheet. Most are half-fiction. Not because staff don't care, "
         "but because the sheet is slow, nobody owns it, and nothing visibly happens with it. The fix is "
         "not more discipline. It is better design: make the check fast, make most of it complete itself, "
         "and make the part a human does almost effortless."),
    p("A famous surgical study found records showing <strong>100% checklist compliance</strong> while "
      "observers watched only 4 of 13 items actually get done" + _c("checklist-compliance-illusion") +
      ". A ticked box is not proof of a done check. This guide builds a daily check where the ticks are "
      "earned: the measurable items are confirmed by your sensors, and the human items are so quick there "
      "is no reason to fake them."),
    callout("key", "The whole idea in one line",
      p("Home Assistant auto-ticks every check it can measure (climate, lights, irrigation, doors, power), "
        "the grower does only the physical walk-around, one tap or an NFC scan logs the rest, and a "
        "missed or out-of-range item escalates on its own. The sheet becomes a short list of real, "
        "human-only items, on a calm green dashboard.")),
    callout("note", "Who this is for",
      p("Any indoor or controlled-environment grow with sensors and an irrigation controller, scaling from "
        "a tent to a licensed medical facility. The behaviour and checklist principles hold even with no "
        "automation at all, the Home Assistant section is how you remove the busywork.")),
  ]})

# 2 -----------------------------------------------------------------
SECTIONS.append({"id": "terms", "kicker": "Vocabulary", "title": "The words you need",
  "blocks": [
    defterm("Pause point", "A named moment a short checklist runs at (lights-on, first irrigation, "
            "pre-dark), instead of one long sheet done whenever" + _c("gawande-checklist-manifesto") + "."),
    defterm("Killer item", "A check that is both easy to skip and dangerous to miss. The few items a list "
            "must force, like dehumidification ramping at lights-off."),
    defterm("Read-do vs do-confirm", "Two checklist styles. Read-do: perform each step as you read it, "
            "for setup and calibration. Do-confirm: do the round from memory, then pause to confirm nothing "
            "critical was missed, for the experienced daily walk" + _c("gawande-checklist-manifesto") + "."),
    defterm("Auto-tick (self-completing check)", "A check item a system marks done by itself once its "
            "telemetry confirms the condition, so the human only handles what a sensor cannot judge."),
    defterm("Alert vs action limit", "Two thresholds per reading: a softer alert limit that warns, and an "
            "action limit that, when crossed, forces a defined response and a corrective-action note" + _c("eu-gmp-annex1") + "."),
    defterm("Pencil-whipping", "Signing off a check without doing it. A predictable response to a check "
            "that is slow, unowned, or never acted on, not simply carelessness."),
    defterm("Implementation intention", "An if-then plan tying a task to a fixed time and person, which "
            "makes follow-through far more likely" + _c("gollwitzer-implementation-intentions") + "."),
  ]})

# 3 -----------------------------------------------------------------
SECTIONS.append({"id": "science", "kicker": "The science", "title": "What makes a check actually get done",
  "blocks": [
    p("Adherence is a design problem, not a character problem. Decades of checklist and behaviour research "
      "point at the same handful of levers."),
    figure(D.bmap(), 1,
      "The Fogg behaviour model: a behaviour happens only when motivation, ability and a prompt line up at "
      "once" + _c("fogg-behavior-model") + ". Motivation swings day to day, so the durable lever is "
      "<strong>ability</strong>: make the check easy and fast, do not rely on staff being keen."),
    h(3, "The levers, in order of impact"),
    ul([
      "<strong>Cut the friction.</strong> Get each check under about 30 seconds, mobile, one tap. Every "
      "field you remove raises completion; auto-filling what the system already knows is the single biggest "
      "win" + _c("digital-checklist-adherence") + ".",
      "<strong>Short lists at pause points.</strong> Five to nine killer items per list, one screen, run at "
      "a trigger moment, not one giant sheet" + _c("gawande-checklist-manifesto") + ".",
      "<strong>Fixed time, one named owner.</strong> Tie each check to a person and a moment ('at lights-on "
      "the AM tech does X'); this if-then framing lifts follow-through two to three fold" + _c("gollwitzer-implementation-intentions") + ". Name a backup for the owner-absent case.",
      "<strong>Close the loop.</strong> Show the worker their data was used and acted on. The top cause of "
      "disengaged faking is submitting into a void where nothing ever happens.",
      "<strong>Make completion visible.</strong> A team board of who did and did not do their checks lifts "
      "adherence sharply, as long as it reads as shared transparency, not surveillance.",
    ]),
    callout("note", "Checks can move real outcomes",
      p("When genuinely performed, the WHO Surgical Safety Checklist cut deaths from 3.7% to 1.4% and lifted "
        "adherence to key steps from 18.6% to 50.7%" + _c("haynes-surgical-checklist-2009") + ". The gain comes "
        "from the check actually happening, never from the mandate or the tick-rate alone.")),
  ]})

# 4 -----------------------------------------------------------------
SECTIONS.append({"id": "content", "kicker": "The content", "title": "What to actually check, and when",
  "blocks": [
    p("Split the day into a few short pause-point lists, each tied to the moment it matters. Each line has a "
      "pre-set green / amber / red limit so the judgement is already made."),
    figure(D.pause_timeline(), 2,
      "Five short lists beat one long sheet: each is tied to a moment, fits on a screen, and stays under "
      "about 90 seconds" + _c("gawande-checklist-manifesto") + "."),
    table(["Pause point", "Style", "Killer items"],
      [["Lights-on / opening", "do-confirm", "climate in band, photoperiod on schedule, no flower light leaks, equipment online"],
       ["At first irrigation", "read-do", "root-zone VWC / EC / pH, overnight dryback, runoff EC/pH, feed vs recipe" + _c("aroya-rootzone-steering")],
       ["Mid-day", "do-confirm", "crop walk, IPM scout (type/place/severity/photo), anything off"],
       ["Pre-dark / closing", "do-confirm", "dehumidification ramped, night airflow on, doors/vault secure, waste logged"],
       ["On alarm", "read-do", "the specific response steps for that alarm"]],
      caption="A complete daily structure. Read-do for measured/calibration tasks, do-confirm for the experienced rounds."),
    figure(D.limit_bands(), 3,
      "Pre-set the limits so the call is already made, and force a corrective-action note on any red so a "
      "problem can never simply be ticked away" + _c("eu-gmp-annex1") + "."),
    callout("note", "The environment killer item people miss",
      p("Confirm dehumidification ramps within minutes of lights-off and air keeps moving all night. A quiet "
        "failure here is how a clean late-flower room turns into a bud-rot room overnight.")),
  ]})

# 5 -----------------------------------------------------------------
SECTIONS.append({"id": "autocomplete", "kicker": "The automation", "title": "Auto-complete it with Home Assistant",
  "blocks": [
    p("Most of a daily check is data the building already knows. Let Home Assistant confirm those items so the "
      "human never re-types what a sensor can prove."),
    figure(D.autotick(), 4,
      "The pattern: sensors feed a template <code>binary_sensor</code> that defines 'in range'; an automation "
      "calls <code>todo.update_item</code> to tick the item once that holds true through the check "
      "window" + _c("ha-todo-integration") + _c("ha-template-alert-statistics") + "."),
    figure(D.auto_vs_human(), 5,
      "Split every item up front: telemetry-confirmable ones tick themselves; only the genuinely physical "
      "ones need a human, as a one-tap toggle or an NFC tag scan at the station."),
    h(3, "The building blocks"),
    ul([
      "<strong>The list:</strong> a <code>local_todo</code> to-do list is the daily sheet; items are ticked "
      "by automation via <code>todo.update_item</code>" + _c("ha-todo-integration") + ".",
      "<strong>The 'pass' test:</strong> a template <code>binary_sensor</code> per item that is on only when "
      "every reading is in band (climate, photoperiod, doors-closed, tank, runoff, all-online).",
      "<strong>Counters for the record:</strong> an integration (Riemann) sensor plus a daily "
      "<code>utility_meter</code> for DLI and runoff volume; <code>history_stats</code> for light and pump "
      "run-time.",
      "<strong>The nag:</strong> the <code>alert</code> integration repeats and needs acknowledging, ideal "
      "for 'fridge out of range' or 'checks not all done by 09:00'" + _c("ha-template-alert-statistics") + ".",
      "<strong>Proof of presence:</strong> an NFC <code>tag</code> at each station ticks its walk-around item "
      "when scanned, so a physical visit is logged, not just claimed.",
      "<strong>The audit trail, free:</strong> long-term statistics keep every reading, so the daily "
      "environmental and irrigation record exists with no extra logging" + _c("ha-template-alert-statistics") + ".",
    ]),
    callout("key", "Worked example, in words",
      p("Build <code>binary_sensor.environment_ok</code> = temp, RH, VPD and CO2 all in their stage bands. "
        "An automation watches it; once it has held true across the lights-on window, it calls "
        "<code>todo.update_item</code> to complete 'Environment in range' on today's list. The grower opens "
        "the list and that line is already green, with the numbers in the history for the record.")),
  ]})

# 6 -----------------------------------------------------------------
SECTIONS.append({"id": "ui", "kicker": "The interface", "title": "Make the human part almost nothing",
  "blocks": [
    p("For the items a person must do, design for the lowest possible interaction. The happy path should be "
      "nearly empty; effort appears only where there is a problem."),
    figure(D.default_pass(), 6,
      "Default every item to pass and submit with one control; only a flagged exception expands to demand a "
      "photo and a note" + _c("digital-checklist-adherence") + ". Hold every common action to three taps or "
      "fewer."),
    ul([
      "<strong>Default to pass.</strong> Items start OK; the operator only ever touches one to flag an "
      "exception. A passing day is a few taps end to end.",
      "<strong>Exception-only evidence.</strong> A fail expands to require a photo plus a short note; passing "
      "items capture nothing. The audit trail is richest exactly where there is a problem.",
      "<strong>NFC primary, QR fallback.</strong> An NFC tap auto-logs checkpoint, time and identity and is "
      "hard to spoof; print a QR on the same placard for phones without NFC.",
      "<strong>Route, don't hunt.</strong> Model the walk-around as an ordered route; let the next station's "
      "card come up on arrival rather than scrolling a list.",
      "<strong>Voice for the note.</strong> Spoken exception notes are the fast path when hands are gloved or "
      "on the plant, and they measurably increase how often observations get logged.",
    ]),
  ]})

# 7 -----------------------------------------------------------------
SECTIONS.append({"id": "adherence", "kicker": "Make it stick", "title": "Getting people to do it, honestly",
  "blocks": [
    p("Two failure modes remain even with a great list: it gets skipped, or it gets faked. Design against "
      "both directly."),
    figure(D.escalation(), 7,
      "A missed item or a red reading escalates on a tiered path: owner first, supervisor next, management "
      "only if unresolved. Design the owner-absent branch explicitly so it never silently dead-ends."),
    h(3, "Anti-pencil-whip, by design"),
    ul([
      "<strong>Auto-capture who, where and when.</strong> Pre-stamp timestamp, identity and station (and any "
      "sensor reading). This removes a typing step and makes fabrication detectable, the worker cannot claim "
      "a presence or a value the system contradicts.",
      "<strong>Do not weaponise the tick-rate.</strong> Auditing box-count and attaching sanctions to it "
      "manufactures faking, the 100%-recorded, 4-of-13-done trap" + _c("checklist-compliance-illusion") +
      ". Spot-audit the <em>reality</em> of a sample instead.",
      "<strong>Embed in the workflow.</strong> Time checks so they do not collide with the busiest moments; "
      "make the check a natural step, not a resented interruption.",
      "<strong>Kill perverse incentives.</strong> No volume quotas that reward rushing; make it safe to "
      "report a real failure rather than soften or hide it.",
    ]),
    callout("warn", "The owner-absent branch",
      p("The most common escalation bug is no path when the owner is on leave or sick. Name a backup and route "
        "to them automatically, or the safety net quietly fails on exactly the days you need it.")),
  ]})

# 8 -----------------------------------------------------------------
SECTIONS.append({"id": "audit-build", "kicker": "Proof & build", "title": "The audit trail, and how to build it",
  "blocks": [
    p("Because the data entry is near zero but the system stamps who, where, when and what on every action, "
      "you get the easiest-to-fill check and a defensible record from the same design."),
    ul([
      "<strong>The record is automatic.</strong> Long-term statistics hold every environmental, light and "
      "irrigation reading as the daily log" + _c("ha-template-alert-statistics") + ", the human items carry a "
      "timestamp, identity and any exception photo.",
      "<strong>Roll up for compliance.</strong> Feed the daily fields into per-lot records (inputs, "
      "conditions, deviations, corrective actions) for a seed-to-harvest trail under GACP and GMP" + _c("who-gacp-2003") + _c("eu-gmp-annex1") + ".",
      "<strong>Trend, don't just file.</strong> Set alert and action limits from your own history and review "
      "them weekly so drift is caught before it becomes a deviation" + _c("eu-gmp-annex1") + ". Sanitation, "
      "hygiene and pest logs follow the same record discipline" + _c("haccp-prerequisite-ssop") + _c("globalgap-cpcc") + ".",
    ]),
    steps([
      ("Make the list", "One local_todo list = today's sheet, seeded each morning with the day's items."),
      ("Define 'pass' in software", "A template binary_sensor per measurable item: the machine definition of in-range."),
      ("Auto-tick", "One automation per item: when its binary_sensor holds true through the window, complete the to-do item."),
      ("Add the human items", "input_boolean toggles or NFC tags for the physical walk-around; default-to-pass UI."),
      ("Escalate & record", "Alert on overdue or red items; rely on statistics for the audit trail; review trends weekly."),
    ]),
    callout("key", "Treat the check as living",
      p("Pilot for about two weeks, watch where it is skipped or breaks, cut non-killer items, fix wording in "
        "growers' terms, and re-issue. Re-test after any facility or automation change. A daily check is a "
        "product you maintain, not a form you laminate.")),
  ]})
