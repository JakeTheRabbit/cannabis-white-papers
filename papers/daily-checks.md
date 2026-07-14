---
slug: "daily-checks"
title: "Daily checks: the self-completing facility round"
eyebrow: "Operations · Daily checks"
summary: "The best daily check is the one that mostly fills itself in. Let Home Assistant confirm everything it can measure, leave the human only the physical walk-around, make the rest one tap, and the check gets done every day, honestly, with an audit trail that holds up."
track: "Facility & quality"
read_time: "~16 min read"
diagrams: "7 diagrams"
related: ["plant-state-dashboard", "closed-loop", "grow-room-systems"]
url: "https://jaketherabbit.github.io/cannabis-white-papers/daily-checks.html"
md_url: "https://jaketherabbit.github.io/cannabis-white-papers/papers/daily-checks.md"
version: "1.1"
updated: "2026-07-15"
license: "CC BY-NC 4.0"
license_url: "https://creativecommons.org/licenses/by-nc/4.0/"
attribution: "The Cannabis White Papers"
refs: [{"id": "gawande-checklist-manifesto", "n": 1, "cite": "Gawande A (2009). The Checklist Manifesto: How to Get Things Right. Metropolitan Books. (read-do vs do-confirm, pause points, 5-9 killer items.)", "url": "https://atulgawande.com/book/the-checklist-manifesto/", "peer": false}, {"id": "fogg-behavior-model", "n": 2, "cite": "Fogg BJ. The Fogg Behavior Model: B = MAP (behaviour occurs when Motivation, Ability and a Prompt converge). Stanford Behavior Design Lab.", "url": "https://behaviormodel.org/", "peer": false}, {"id": "gollwitzer-implementation-intentions", "n": 3, "cite": "Gollwitzer PM, Sheeran P (2006). Implementation intentions and goal achievement: a meta-analysis of effects and processes. Advances in Experimental Social Psychology 38:69-119 (medium-to-large effect, d=0.65).", "url": "https://doi.org/10.1016/S0065-2601(06)38002-1", "peer": true}, {"id": "checklist-compliance-illusion", "n": 4, "cite": "Observational study of surgical-checklist use: high recorded compliance did not guarantee the items were actually performed (records showed 100% adherence; observers found 4 of 13 items done). PMC4484042.", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC4484042/", "peer": true}, {"id": "haynes-surgical-checklist-2009", "n": 5, "cite": "Haynes AB, Weiser TG, Berry WR, et al. (2009). A surgical safety checklist to reduce morbidity and mortality in a global population. New England Journal of Medicine 360(5):491-499.", "url": "https://www.nejm.org/doi/full/10.1056/NEJMsa0810119", "peer": true}, {"id": "ha-todo-integration", "n": 6, "cite": "Home Assistant: To-do list (todo) and Local to-do (local_todo) integrations, todo entity and todo.update_item action used to auto-complete checklist items.", "url": "https://www.home-assistant.io/integrations/todo/", "peer": false}, {"id": "ha-template-alert-statistics", "n": 7, "cite": "Home Assistant: Template (binary_sensor), Alert, Statistics/Recorder, Tag (NFC) and Schedule integrations used to define 'in range', escalate, log the audit trail and prove presence.", "url": "https://www.home-assistant.io/integrations/template/", "peer": false}, {"id": "aroya-rootzone-steering", "n": 8, "cite": "AROYA. Crop-steering and drip-and-drain root-zone monitoring (substrate VWC, EC, pH, dryback, runoff) as the daily root-zone measurement.", "url": "https://aroya.io/", "peer": false}, {"id": "eu-gmp-annex1", "n": 9, "cite": "EU GMP Annex 1 / EMA environmental-monitoring guidance: define alert and action limits, trend routine monitoring data, require corrective action on excursions.", "url": "https://health.ec.europa.eu/medicinal-products/eudralex/eudralex-volume-4_en", "peer": false}, {"id": "who-gacp-2003", "n": 10, "cite": "World Health Organization (2003). WHO guidelines on good agricultural and collection practices (GACP) for medicinal plants.", "url": "https://www.who.int/publications/i/item/9241546271", "peer": false}, {"id": "globalgap-cpcc", "n": 11, "cite": "GLOBALG.A.P. Integrated Farm Assurance, Crops / Fruit & Vegetables control points and compliance criteria (hygiene competence, maintained irrigation equipment, record retention).", "url": "https://www.globalgap.org/", "peer": false}, {"id": "haccp-prerequisite-ssop", "n": 12, "cite": "HACCP prerequisite programmes / Sanitation Standard Operating Procedures: daily sanitation checklists, hygiene checks and pest-control logs (what, how, how-often, who-verifies).", "url": "https://www.fda.gov/food/hazard-analysis-critical-control-point-haccp/haccp-principles-application-guidelines", "peer": false}, {"id": "digital-checklist-adherence", "n": 13, "cite": "Industry analyses of digital vs paper inspection checklists: higher completion rates, faster rounds and fewer documentation errors, driven by lower friction and enforced completeness.", "url": "https://www.fiixsoftware.com/cmms/mobile-cmms/", "peer": false}]
---

# Daily checks: the self-completing facility round

_Operations · Daily checks · ~16 min read_

> The best daily check is the one that mostly fills itself in. Let Home Assistant confirm everything it can measure, leave the human only the physical walk-around, make the rest one tap, and the check gets done every day, honestly, with an audit trail that holds up.

## Why daily checks fail, and the fix

Every facility has a daily check sheet. Most are half-fiction. Not because staff don't care, but because the sheet is slow, nobody owns it, and nothing visibly happens with it. The fix is not more discipline. It is better design: make the check fast, make most of it complete itself, and make the part a human does almost effortless.

A famous surgical study found records showing **100% checklist compliance** while observers watched only 4 of 13 items actually get done[^checklist-compliance-illusion]. A ticked box is not proof of a done check. This guide builds a daily check where the ticks are earned: the measurable items are confirmed by your sensors, and the human items are so quick there is no reason to fake them.

> **KEY — The whole idea in one line**
>
> Home Assistant auto-ticks every check it can measure (climate, lights, irrigation, doors, power), the grower does only the physical walk-around, one tap or an NFC scan logs the rest, and a missed or out-of-range item escalates on its own. The sheet becomes a short list of real, human-only items, on a calm green dashboard.

> **NOTE — Who this is for**
>
> Any indoor or controlled-environment grow with sensors and an irrigation controller, scaling from a tent to a licensed medical facility. The behaviour and checklist principles hold even with no automation at all, the Home Assistant section is how you remove the busywork.

## The words you need

**Pause point** — A named moment a short checklist runs at (lights-on, first irrigation, pre-dark), instead of one long sheet done whenever[^gawande-checklist-manifesto].

**Killer item** — A check that is both easy to skip and dangerous to miss. The few items a list must force, like dehumidification ramping at lights-off.

**Read-do vs do-confirm** — Two checklist styles. Read-do: perform each step as you read it, for setup and calibration. Do-confirm: do the round from memory, then pause to confirm nothing critical was missed, for the experienced daily walk[^gawande-checklist-manifesto].

**Auto-tick (self-completing check)** — A check item a system marks done by itself once its telemetry confirms the condition, so the human only handles what a sensor cannot judge.

**Alert vs action limit** — Two thresholds per reading: a softer alert limit that warns, and an action limit that, when crossed, forces a defined response and a corrective-action note[^eu-gmp-annex1].

**Pencil-whipping** — Signing off a check without doing it. A predictable response to a check that is slow, unowned, or never acted on, not simply carelessness.

**Implementation intention** — An if-then plan tying a task to a fixed time and person, which makes follow-through far more likely[^gollwitzer-implementation-intentions].

## What makes a check actually get done

Adherence is a design problem, not a character problem. Decades of checklist and behaviour research point at the same handful of levers.

> **Diagram.** The Fogg behaviour model: a behaviour happens only when motivation, ability and a prompt line up at once[^fogg-behavior-model]. Motivation swings day to day, so the durable lever is **ability**: make the check easy and fast, do not rely on staff being keen.

#### The levers, in order of impact

- **Cut the friction.** Get each check under about 30 seconds, mobile, one tap. Every field you remove raises completion; auto-filling what the system already knows is the single biggest win[^digital-checklist-adherence].
- **Short lists at pause points.** Five to nine killer items per list, one screen, run at a trigger moment, not one giant sheet[^gawande-checklist-manifesto].
- **Fixed time, one named owner.** Tie each check to a person and a moment ('at lights-on the AM tech does X'); this if-then framing lifts follow-through two to three fold[^gollwitzer-implementation-intentions]. Name a backup for the owner-absent case.
- **Close the loop.** Show the worker their data was used and acted on. The top cause of disengaged faking is submitting into a void where nothing ever happens.
- **Make completion visible.** A team board of who did and did not do their checks lifts adherence sharply, as long as it reads as shared transparency, not surveillance.

> **NOTE — Checks can move real outcomes**
>
> When genuinely performed, the WHO Surgical Safety Checklist cut deaths from 3.7% to 1.4% and lifted adherence to key steps from 18.6% to 50.7%[^haynes-surgical-checklist-2009]. The gain comes from the check actually happening, never from the mandate or the tick-rate alone.

## What to actually check, and when

Split the day into a few short pause-point lists, each tied to the moment it matters. Each line has a pre-set green / amber / red limit so the judgement is already made.

> **Diagram.** Five short lists beat one long sheet: each is tied to a moment, fits on a screen, and stays under about 90 seconds[^gawande-checklist-manifesto].

| Pause point | Style | Killer items |
| --- | --- | --- |
| Lights-on / opening | do-confirm | climate in band, photoperiod on schedule, no flower light leaks, equipment online |
| At first irrigation | read-do | root-zone VWC / EC / pH, overnight dryback, runoff EC/pH, feed vs recipe[^aroya-rootzone-steering] |
| Mid-day | do-confirm | crop walk, IPM scout (type/place/severity/photo), anything off |
| Pre-dark / closing | do-confirm | dehumidification ramped, night airflow on, doors/vault secure, waste logged |
| On alarm | read-do | the specific response steps for that alarm |

*A complete daily structure. Read-do for measured/calibration tasks, do-confirm for the experienced rounds.*

> **Diagram.** Pre-set the limits so the call is already made, and force a corrective-action note on any red so a problem can never simply be ticked away[^eu-gmp-annex1].

> **NOTE — The environment killer item people miss**
>
> Confirm dehumidification ramps within minutes of lights-off and air keeps moving all night. A quiet failure here is how a clean late-flower room turns into a bud-rot room overnight.

## Auto-complete it with Home Assistant

Most of a daily check is data the building already knows. Let Home Assistant confirm those items so the human never re-types what a sensor can prove.

> **Diagram.** The pattern: sensors feed a template `binary_sensor` that defines 'in range'; an automation calls `todo.update_item` to tick the item once that holds true through the check window[^ha-todo-integration][^ha-template-alert-statistics].

> **Diagram.** Split every item up front: telemetry-confirmable ones tick themselves; only the genuinely physical ones need a human, as a one-tap toggle or an NFC tag scan at the station.

#### The building blocks

- **The list:** a `local_todo` to-do list is the daily sheet; items are ticked by automation via `todo.update_item`[^ha-todo-integration].
- **The 'pass' test:** a template `binary_sensor` per item that is on only when every reading is in band (climate, photoperiod, doors-closed, tank, runoff, all-online).
- **Counters for the record:** an integration (Riemann) sensor plus a daily `utility_meter` for DLI and runoff volume; `history_stats` for light and pump run-time.
- **The nag:** the `alert` integration repeats and needs acknowledging, ideal for 'fridge out of range' or 'checks not all done by 09:00'[^ha-template-alert-statistics].
- **Proof of presence:** an NFC `tag` at each station ticks its walk-around item when scanned, so a physical visit is logged, not just claimed.
- **The audit trail, free:** long-term statistics keep every reading, so the daily environmental and irrigation record exists with no extra logging[^ha-template-alert-statistics].

> **KEY — Worked example, in words**
>
> Build `binary_sensor.environment_ok` = temp, RH, VPD and CO2 all in their stage bands. An automation watches it; once it has held true across the lights-on window, it calls `todo.update_item` to complete 'Environment in range' on today's list. The grower opens the list and that line is already green, with the numbers in the history for the record.

## Make the human part almost nothing

For the items a person must do, design for the lowest possible interaction. The happy path should be nearly empty; effort appears only where there is a problem.

> **Diagram.** Default every item to pass and submit with one control; only a flagged exception expands to demand a photo and a note[^digital-checklist-adherence]. Hold every common action to three taps or fewer.

- **Default to pass.** Items start OK; the operator only ever touches one to flag an exception. A passing day is a few taps end to end.
- **Exception-only evidence.** A fail expands to require a photo plus a short note; passing items capture nothing. The audit trail is richest exactly where there is a problem.
- **NFC primary, QR fallback.** An NFC tap auto-logs checkpoint, time and identity and is hard to spoof; print a QR on the same placard for phones without NFC.
- **Route, don't hunt.** Model the walk-around as an ordered route; let the next station's card come up on arrival rather than scrolling a list.
- **Voice for the note.** Spoken exception notes are the fast path when hands are gloved or on the plant, and they measurably increase how often observations get logged.

## Getting people to do it, honestly

Two failure modes remain even with a great list: it gets skipped, or it gets faked. Design against both directly.

> **Diagram.** A missed item or a red reading escalates on a tiered path: owner first, supervisor next, management only if unresolved. Design the owner-absent branch explicitly so it never silently dead-ends.

#### Anti-pencil-whip, by design

- **Auto-capture who, where and when.** Pre-stamp timestamp, identity and station (and any sensor reading). This removes a typing step and makes fabrication detectable, the worker cannot claim a presence or a value the system contradicts.
- **Do not weaponise the tick-rate.** Auditing box-count and attaching sanctions to it manufactures faking, the 100%-recorded, 4-of-13-done trap[^checklist-compliance-illusion]. Spot-audit the _reality_ of a sample instead.
- **Embed in the workflow.** Time checks so they do not collide with the busiest moments; make the check a natural step, not a resented interruption.
- **Kill perverse incentives.** No volume quotas that reward rushing; make it safe to report a real failure rather than soften or hide it.

> **WARN — The owner-absent branch**
>
> The most common escalation bug is no path when the owner is on leave or sick. Name a backup and route to them automatically, or the safety net quietly fails on exactly the days you need it.

## The audit trail, and how to build it

Because the data entry is near zero but the system stamps who, where, when and what on every action, you get the easiest-to-fill check and a defensible record from the same design.

- **The record is automatic.** Long-term statistics hold every environmental, light and irrigation reading as the daily log[^ha-template-alert-statistics], the human items carry a timestamp, identity and any exception photo.
- **Roll up for compliance.** Feed the daily fields into per-lot records (inputs, conditions, deviations, corrective actions) for a seed-to-harvest trail under GACP and GMP[^who-gacp-2003][^eu-gmp-annex1].
- **Trend, don't just file.** Set alert and action limits from your own history and review them weekly so drift is caught before it becomes a deviation[^eu-gmp-annex1]. Sanitation, hygiene and pest logs follow the same record discipline[^haccp-prerequisite-ssop][^globalgap-cpcc].

1. **Make the list** — One local_todo list = today's sheet, seeded each morning with the day's items.
2. **Define 'pass' in software** — A template binary_sensor per measurable item: the machine definition of in-range.
3. **Auto-tick** — One automation per item: when its binary_sensor holds true through the window, complete the to-do item.
4. **Add the human items** — input_boolean toggles or NFC tags for the physical walk-around; default-to-pass UI.
5. **Escalate & record** — Alert on overdue or red items; rely on statistics for the audit trail; review trends weekly.

> **KEY — Treat the check as living**
>
> Pilot for about two weeks, watch where it is skipped or breaks, cut non-killer items, fix wording in growers' terms, and re-issue. Re-test after any facility or automation change. A daily check is a product you maintain, not a form you laminate.

## References

[^gawande-checklist-manifesto]: Gawande A (2009). The Checklist Manifesto: How to Get Things Right. Metropolitan Books. (read-do vs do-confirm, pause points, 5-9 killer items.) https://atulgawande.com/book/the-checklist-manifesto/ (industry/manufacturer source)
[^fogg-behavior-model]: Fogg BJ. The Fogg Behavior Model: B = MAP (behaviour occurs when Motivation, Ability and a Prompt converge). Stanford Behavior Design Lab. https://behaviormodel.org/ (industry/manufacturer source)
[^gollwitzer-implementation-intentions]: Gollwitzer PM, Sheeran P (2006). Implementation intentions and goal achievement: a meta-analysis of effects and processes. Advances in Experimental Social Psychology 38:69-119 (medium-to-large effect, d=0.65). https://doi.org/10.1016/S0065-2601(06)38002-1 (peer-reviewed)
[^checklist-compliance-illusion]: Observational study of surgical-checklist use: high recorded compliance did not guarantee the items were actually performed (records showed 100% adherence; observers found 4 of 13 items done). PMC4484042. https://pmc.ncbi.nlm.nih.gov/articles/PMC4484042/ (peer-reviewed)
[^haynes-surgical-checklist-2009]: Haynes AB, Weiser TG, Berry WR, et al. (2009). A surgical safety checklist to reduce morbidity and mortality in a global population. New England Journal of Medicine 360(5):491-499. https://www.nejm.org/doi/full/10.1056/NEJMsa0810119 (peer-reviewed)
[^ha-todo-integration]: Home Assistant: To-do list (todo) and Local to-do (local_todo) integrations, todo entity and todo.update_item action used to auto-complete checklist items. https://www.home-assistant.io/integrations/todo/ (industry/manufacturer source)
[^ha-template-alert-statistics]: Home Assistant: Template (binary_sensor), Alert, Statistics/Recorder, Tag (NFC) and Schedule integrations used to define 'in range', escalate, log the audit trail and prove presence. https://www.home-assistant.io/integrations/template/ (industry/manufacturer source)
[^aroya-rootzone-steering]: AROYA. Crop-steering and drip-and-drain root-zone monitoring (substrate VWC, EC, pH, dryback, runoff) as the daily root-zone measurement. https://aroya.io/ (industry/manufacturer source)
[^eu-gmp-annex1]: EU GMP Annex 1 / EMA environmental-monitoring guidance: define alert and action limits, trend routine monitoring data, require corrective action on excursions. https://health.ec.europa.eu/medicinal-products/eudralex/eudralex-volume-4_en (industry/manufacturer source)
[^who-gacp-2003]: World Health Organization (2003). WHO guidelines on good agricultural and collection practices (GACP) for medicinal plants. https://www.who.int/publications/i/item/9241546271 (industry/manufacturer source)
[^globalgap-cpcc]: GLOBALG.A.P. Integrated Farm Assurance, Crops / Fruit & Vegetables control points and compliance criteria (hygiene competence, maintained irrigation equipment, record retention). https://www.globalgap.org/ (industry/manufacturer source)
[^haccp-prerequisite-ssop]: HACCP prerequisite programmes / Sanitation Standard Operating Procedures: daily sanitation checklists, hygiene checks and pest-control logs (what, how, how-often, who-verifies). https://www.fda.gov/food/hazard-analysis-critical-control-point-haccp/haccp-principles-application-guidelines (industry/manufacturer source)
[^digital-checklist-adherence]: Industry analyses of digital vs paper inspection checklists: higher completion rates, faster rounds and fewer documentation errors, driven by lower friction and enforced completeness. https://www.fiixsoftware.com/cmms/mobile-cmms/ (industry/manufacturer source)
