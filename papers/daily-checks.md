---
slug: "daily-checks"
title: "Make a facility check for each day that completes most items automatically"
eyebrow: "Operations · Checks for each day"
summary: "This paper shows you how to make a facility check for each day in which sensors automatically complete all items that they can measure. The walk-around by a person stays short. At the end of this paper, you will have a Home Assistant structure that operates correctly. You will also have a set of five checklists, one for each pause point. The system makes an accurate audit trail without more input from a person."
track: "Facility and quality"
read_time: "~16 min to read"
diagrams: "7 diagrams"
related: ["plant-state-dashboard", "closed-loop", "grow-room-systems"]
url: "https://www.growlabs.nz/wiki/daily-checks.html"
md_url: "https://www.growlabs.nz/wiki/papers/daily-checks.md"
version: "1.2"
updated: "2026-07-18"
license: "CC BY-NC 4.0"
license_url: "https://creativecommons.org/licenses/by-nc/4.0/"
attribution: "The Cannabis White Papers"
refs: [{"id": "gawande-checklist-manifesto", "n": 1, "cite": "Gawande A (2009). The Checklist Manifesto: How to Get Things Right. Metropolitan Books. (read-do vs do-confirm, pause points, 5-9 killer items.)", "url": "https://atulgawande.com/book/the-checklist-manifesto/", "peer": false}, {"id": "fogg-behavior-model", "n": 2, "cite": "Fogg BJ. The Fogg Behavior Model: B = MAP (behaviour occurs when Motivation, Ability and a Prompt converge). Stanford Behavior Design Lab.", "url": "https://behaviormodel.org/", "peer": false}, {"id": "gollwitzer-implementation-intentions", "n": 3, "cite": "Gollwitzer PM, Sheeran P (2006). Implementation intentions and goal achievement: a meta-analysis of effects and processes. Advances in Experimental Social Psychology 38:69-119 (medium-to-large effect, d=0.65).", "url": "https://doi.org/10.1016/S0065-2601(06)38002-1", "peer": true}, {"id": "checklist-compliance-illusion", "n": 4, "cite": "Observational study of surgical-checklist use: high recorded compliance did not guarantee the items were actually performed (records showed 100% adherence; observers found 4 of 13 items done). PMC4484042.", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC4484042/", "peer": true}, {"id": "haynes-surgical-checklist-2009", "n": 5, "cite": "Haynes AB, Weiser TG, Berry WR, et al. (2009). A surgical safety checklist to reduce morbidity and mortality in a global population. New England Journal of Medicine 360(5):491-499.", "url": "https://www.nejm.org/doi/full/10.1056/NEJMsa0810119", "peer": true}, {"id": "ha-todo-integration", "n": 6, "cite": "Home Assistant: To-do list (todo) and Local to-do (local_todo) integrations, todo entity and todo.update_item action used to auto-complete checklist items.", "url": "https://www.home-assistant.io/integrations/todo/", "peer": false}, {"id": "ha-template-alert-statistics", "n": 7, "cite": "Home Assistant: Template (binary_sensor), Alert, Statistics/Recorder, Tag (NFC) and Schedule integrations used to define 'in range', escalate, log the audit trail and prove presence.", "url": "https://www.home-assistant.io/integrations/template/", "peer": false}, {"id": "aroya-rootzone-steering", "n": 8, "cite": "AROYA. Crop-steering and drip-and-drain root-zone monitoring (substrate VWC, EC, pH, dryback, runoff) as the daily root-zone measurement.", "url": "https://aroya.io/", "peer": false}, {"id": "eu-gmp-annex1", "n": 9, "cite": "EU GMP Annex 1 / EMA environmental-monitoring guidance: define alert and action limits, trend routine monitoring data, require corrective action on excursions.", "url": "https://health.ec.europa.eu/medicinal-products/eudralex/eudralex-volume-4_en", "peer": false}, {"id": "who-gacp-2003", "n": 10, "cite": "World Health Organization (2003). WHO guidelines on good agricultural and collection practices (GACP) for medicinal plants.", "url": "https://www.who.int/publications/i/item/9241546271", "peer": false}, {"id": "globalgap-cpcc", "n": 11, "cite": "GLOBALG.A.P. Integrated Farm Assurance, Crops / Fruit & Vegetables control points and compliance criteria (hygiene competence, maintained irrigation equipment, record retention).", "url": "https://www.globalgap.org/", "peer": false}, {"id": "haccp-prerequisite-ssop", "n": 12, "cite": "HACCP prerequisite programmes / Sanitation Standard Operating Procedures: daily sanitation checklists, hygiene checks and pest-control logs (what, how, how-often, who-verifies).", "url": "https://www.fda.gov/food/hazard-analysis-critical-control-point-haccp/haccp-principles-application-guidelines", "peer": false}, {"id": "digital-checklist-adherence", "n": 13, "cite": "Industry analyses of digital vs paper inspection checklists: higher completion rates, faster rounds and fewer documentation errors, driven by lower friction and enforced completeness.", "url": "https://www.fiixsoftware.com/cmms/mobile-cmms/", "peer": false}]
---

# Make a facility check for each day that completes most items automatically

_Operations · Checks for each day · ~16 min to read_

> This paper shows you how to make a facility check for each day in which sensors automatically complete all items that they can measure. The walk-around by a person stays short. At the end of this paper, you will have a Home Assistant structure that operates correctly. You will also have a set of five checklists, one for each pause point. The system makes an accurate audit trail without more input from a person.

## Purpose and scope

Each facility has a checklist for each day. Approximately half of the records on most checklists are not correct. The cause is not that the personnel do not want a correct checklist. The checklist is slow, the checklist has no owner, and no person sees a result from it. An instruction to the personnel to be more careful does not correct this. The correction is a better system: make the check fast, make most of it automatic, and make the task for a person very easy.

An investigation of checklists in surgery found records that showed **100% checklist compliance**. In the same investigation, persons who examined the work saw that the personnel did only 4 of the 13 items[^checklist-compliance-illusion]. A mark on the checklist does not show that a person did the check. In this paper, you make a check in which each mark is correct. Your sensors make sure that the items they can measure are correct. Personnel have no cause to record an item that they did not do, because the items for a person are very fast to do.

> **KEY: The system in short**
>
> Home Assistant completes each item that it can measure (the climate, the lights, the irrigation, the doors and the power). A person does only the walk-around. To record each other item, the person touches the screen one time or taps an NFC tag. If a person does not do an item, or a reading is out of range, the system sends an alert to the next person automatically. The checklist becomes a short list of the items that only a person can do, on a dashboard that stays green.

> **NOTE: Who can use this paper**
>
> This paper is for each cultivation facility that has sensors and an irrigation controller. The facility can be in a building or can be a controlled-environment facility. The size can be from a tent to a medical facility that has a license. The information about behavior and checklists is also correct if you have no automation. The Home Assistant section shows you how to remove the manual tasks that are not necessary.

## Definitions

**Pause point**: A pause point is a time with a name, at which you do a short checklist. Examples are lights-on, the first irrigation and pre-dark. A pause point replaces one long checklist that you do at a time that you select[^gawande-checklist-manifesto].

**Killer item**: A killer item is a check that a person can easily ignore. If the person ignores the check, the result is dangerous. A checklist has only a small number of killer items. It must make sure that a person does each one. An example is a check that dehumidification increases at lights-off.

**Read-do and do-confirm**: There are two types of checklist. With read-do, you read each step and then do it. Use this type for setup and calibration. With do-confirm, you do the walk-around first and you do not read the checklist. Then you stop and make sure that you did all important steps. Use this type for the usual walk-around each day of a person who knows the task[^gawande-checklist-manifesto].

**Auto-tick (automatic check)**: An auto-tick is a check item that the system completes automatically. The system does this when the sensor data show that the condition is correct. Thus a person does only the items that a sensor cannot examine.

**Alert limit and action limit**: Each reading has two thresholds. The alert limit is the first threshold. When a reading is out of the alert limit, the system sends an alert. When a reading is out of the action limit, the person must do a specified procedure. The person must also write a note about the corrective action[^eu-gmp-annex1].

**Pencil-whipping**: Pencil-whipping is a record that shows a check as done, when the person did not do the check. Pencil-whipping usually occurs when the check is slow, when the check has no owner, or when no result follows. The cause is not only that the personnel are not careful.

**Implementation intention**: An implementation intention is an if-then decision. In this decision, one person does one task at one specified time. A person with an implementation intention does the task much more frequently than a person without one[^gollwitzer-implementation-intentions].

## How to make sure that personnel complete the checks

Personnel complete a check regularly when the check has a good structure. Investigations of checklists and of behavior for many years show the same small number of methods.

> **Diagram.** The Fogg behavior model shows that a behavior occurs only when motivation, ability and a prompt occur at the same time[^fogg-behavior-model]. Motivation changes from day to day. Thus **ability** gives a stable result. Make the check easy and fast. Then high motivation is not necessary.

#### The methods, with the largest effect first

- **Decrease the work for each check.** Make each check shorter than approximately 30 seconds. The person does the check on a mobile device and taps the screen one time. Each input that you remove increases the number of checks that personnel complete. The system causes the largest effect when it records automatically the data that it has[^digital-checklist-adherence].
- **Use short checklists at pause points.** Put five to nine killer items in each checklist. Keep each checklist on one screen. Do each checklist at its pause point, not as one very long checklist[^gawande-checklist-manifesto].
- **Give each check an owner and a specified time.** Make an implementation intention for each check, for example 'At lights-on, the AM operator does X'. An implementation intention increases goal attainment by a medium effect (d≈0.65 in a meta-analysis)[^gollwitzer-implementation-intentions]. Give the name of a second person for the time when the owner is not at work.
- **Use the data and show the result.** Show each person that you used the data from the person, and that you did a task because of it. The primary cause of pencil-whipping is that personnel send data and no result follows.
- **Show who completed the checks.** A display shows which persons did a check and which persons did not do a check. This display increases the number of completed checks by a large quantity. The display has this effect only if the personnel think that it is information for all persons, and not a method to monitor them.

> **NOTE: A check can change the result**
>
> When personnel did the checks correctly, the WHO Surgical Safety Checklist decreased the death rate from 3.7% to 1.4%. It also increased the percentage of important steps that personnel did, from 18.6% to 50.7%[^haynes-surgical-checklist-2009]. The check that personnel do causes the result. An instruction to do the check, or a high number of marks, does not cause the result without the check.

## Times and contents of the checks for each day

Divide the day into a small number of short checklists, one for each pause point. For each item, set the limits for the colors green, amber and red before the check. Thus the person does not make a decision during the check.

> **Diagram.** Five short checklists are better than one long checklist. Each checklist is for one pause point and is on one screen. The time for each checklist is less than approximately 90 seconds[^gawande-checklist-manifesto].

| Pause point | Type | Killer items |
| --- | --- | --- |
| Lights-on / opening | Do-Confirm | climate in range, photoperiod correct, no light leaks in the flower room, all equipment connected |
| At first irrigation | Read-Do | root-zone VWC, EC and pH, dryback in the night, runoff EC and pH, feed compared with the recipe[^aroya-rootzone-steering] |
| Mid-day | Do-Confirm | crop walk-around, IPM inspection (the type, the location, the severity and a photo), each unusual condition |
| Pre-dark / end of the day | Do-Confirm | dehumidification increased, night airflow on, doors locked, vault locked, waste recorded |
| On alarm | Read-Do | the steps for that alarm |

*A full structure for each day. For tasks of measurement and calibration, use read-do. For the walk-around of persons who know the tasks, use do-confirm.*

> **Diagram.** Set the limits before the check. Thus the person does not make the decision. For each red reading, the person must write a note about the corrective action. Thus a person cannot remove a problem with only a mark[^eu-gmp-annex1].

> **NOTE: The killer item for the environment that personnel ignore**
>
> Make sure that dehumidification increases in the first minutes after lights-off. Make sure that the air continues to move all night. A malfunction without an alarm can change a clean room in the last flowering stage into a room with bud rot in one night.

## Home Assistant check automation

Most of the items in the check for each day are data that sensors in the building measure. Let Home Assistant make sure that these items are correct. Thus a person does not write again the data that a sensor can show.

> **Diagram.** This diagram shows the sequence. Sensors send data to a template `binary_sensor`. This sensor is on when the readings are in range. An automation uses `todo.update_item` to complete the item when that sensor stays on for all of the check period[^ha-todo-integration][^ha-template-alert-statistics].

> **Diagram.** At the start, divide the items into two groups. The system completes the items for which sensor data show that the condition is correct. A person does only the items that a sensor cannot examine. The person records these items with a one-tap toggle or an NFC tag at the location.

#### The components

- **The to-do list:** a `local_todo` to-do list is the checklist for each day. An automation completes the items with `todo.update_item`[^ha-todo-integration].
- **The 'OK' test:** a template `binary_sensor` for each item. It is on only when all readings are in range (the climate, the photoperiod, closed doors, the tank, the runoff and connected equipment).
- **Totals for the record:** use a Riemann integration sensor and a `utility_meter` for each day to get the DLI and the runoff volume. Use `history_stats` to get the operation time of the lights and the pumps.
- **The alert:** the `alert` integration sends the alert again and again until a person stops it. Use it for 'refrigerator out of range' or 'not all checks done by 09:00'[^ha-template-alert-statistics].
- **A record that the person was at the location.** An NFC `tag` at each location completes the walk-around item for that location when a person touches it with a mobile device. Thus the system records where the person was. The person does not only tell you this fact.
- **The audit trail without more work:** long-term statistics keep each reading. Thus the record of the environment and of the irrigation for each day is available without more input from the person[^ha-template-alert-statistics].

> **KEY: Example of the steps**
>
> Make `binary_sensor.environment_ok`. It is on when all of these values are in the ranges for the growth stage. The values are the temperature, the relative humidity (RH), the vapor pressure deficit (VPD) and the CO2. An automation monitors this sensor. When the sensor stays on for all of the lights-on period, the automation uses `todo.update_item` to complete 'Environment in range' on the checklist. The person opens the checklist for this day, and this item is green, with the numbers in the history as a record.

## Make a check interface for fast input

For the items that a person must do, make the input from the person as small as possible. When all items are OK, the person does only a very small number of steps. The person does more steps only where there is a problem.

> **Diagram.** Set each item to OK at the start. The person sends the checklist with one control. Only for an item that is not OK, the system shows a screen where the person must add a photo and a note[^digital-checklist-adherence]. Make sure that each usual task has a maximum of three taps.

- **Set items to OK at the start.** The person touches an item only to show that the item is not OK. A day on which all items are OK has only a small number of taps from the start to the end.
- **A photo and a note only for items that are not OK.** For an item that is not OK, the person must add a photo and a short note. OK items have no photo and no note. The audit trail has the most information where there is a problem.
- **Use NFC as the primary method and QR as the second method.** An NFC tap automatically records the location, the time and the name of the person. A person cannot easily use it to record a location where the person was not. Put a QR code on the same label for mobile devices that do not have NFC.
- **Show one location at a time.** Put the locations of the walk-around in a sequence. When the person is at the next location, the screen shows the checks for that location. The person does not read a long list.
- **Voice for the note.** A person can speak the note for an item that is not OK. This method is the fastest when the person has gloves on or touches the plant. Measurements show that voice notes increase the number of notes that personnel record.

## Checks that are not done, pencil-whipping and escalation

Two problems continue to occur although the checklist is good. In the first problem, personnel do not do the check. The second problem is pencil-whipping. Prevent the two problems directly.

> **Diagram.** If a person does not do an item, or a reading is red, the system starts an escalation. The system sends the alert to the owner first and then to the supervisor. It sends the alert to a manager only if the problem continues. Make sure that the escalation continues when the owner is not at work. Thus the escalation does not stop without an alert.

#### How to prevent pencil-whipping

- **Record who, where and when automatically.** Let the system record the time, the name of the person and the location. Let it also record the sensor reading, if there is one. Thus the person does not write these data. The person cannot tell you that the person was at a location, or give a value, if the data of the system are different.
- **Do not give a bad result to personnel for a low number of marks.** If an audit examines only the number of marks, and a low number causes a bad result, you cause pencil-whipping. In the investigation, 100% of the records had a mark, and the personnel did only 4 of 13 items[^checklist-compliance-illusion]. Do an audit of a sample of the checks. Examine _the work that personnel did_.
- **Put the check in the usual work.** Do not set a check at a time when personnel have much other work. Make the check a usual step of the work, not a task that stops the work.
- **Remove the causes of incorrect behavior.** Do not set a target for the number of checks, because a target makes personnel do the checks too fast. Make sure that it is safe for a person to tell you about a problem. Then the person tells you about the problem and does not tell you that it is small or that there is no problem.

> **WARN: When the owner is not at work**
>
> The most frequent problem of an escalation is that it stops when the owner is not at work. Give the name of a second person for each owner. Send the alert automatically to the second person. If you do not do this, the escalation does not operate on the days when it is necessary.

## Audit trail and steps to make the system

The input from a person is almost zero. The system records, for each task, the name of the person, the location and the time. Thus the same system gives you a check that is very easy to do and a record that you can show in an audit.

- **The record is automatic.** Long-term statistics keep each reading of the environment, the lights and the irrigation as the log for each day[^ha-template-alert-statistics]. Each item that a person does has the time, the name of the person and, if the item is not OK, a photo.
- **Collect the data for compliance.** Put the data of each day in the records for each lot (inputs, conditions, deviations and corrective actions). Thus you get records for the operation from seed to harvest. If you must obey GACP or GMP regulations, the systems must also have validation[^who-gacp-2003][^eu-gmp-annex1].
- **Examine the trend. Do not only keep the records.** Set the alert limits and the action limits from the history of your facility. Examine them each week. Thus you find drift before it becomes a deviation[^eu-gmp-annex1]. The logs for sanitation, hygiene and pests use the same record method[^haccp-prerequisite-ssop][^globalgap-cpcc].

1. **Make the list**: One local_todo list is the checklist for the day. At the start of each day, put the items for that day in the list.
2. **Set the condition for 'OK' in the system**: Make one template binary_sensor for each item that a sensor can measure. The system uses it to know when the item is in range.
3. **Auto-tick**: Make one automation for each item. When the binary_sensor of the item stays on for all of the check period, the automation completes the to-do item.
4. **Add the items for a person**: For the walk-around, use input_boolean toggles or NFC tags. Make the interface set each item to OK at the start.
5. **Escalate and record**: Send an alert when an item is red or is not done by the specified time. Use the long-term statistics for the audit trail. Examine the trends each week.

> **KEY: Change the check when it is necessary**
>
> Do a test of the check for approximately two weeks. Monitor where personnel do not do the check or where the system has a malfunction. Remove the items that are not killer items, and change the check to use the terms of the growers. Then give the new check to the personnel. After a change to the facility or the automation, do the test again. The check is a product that you keep correct, not a laminated sheet.

## References

[^gawande-checklist-manifesto]: Gawande A (2009). The Checklist Manifesto: How to Get Things Right. Metropolitan Books. (read-do vs do-confirm, pause points, 5-9 killer items.) https://atulgawande.com/book/the-checklist-manifesto/ (source from a manufacturer or industry)
[^fogg-behavior-model]: Fogg BJ. The Fogg Behavior Model: B = MAP (behaviour occurs when Motivation, Ability and a Prompt converge). Stanford Behavior Design Lab. https://behaviormodel.org/ (source from a manufacturer or industry)
[^gollwitzer-implementation-intentions]: Gollwitzer PM, Sheeran P (2006). Implementation intentions and goal achievement: a meta-analysis of effects and processes. Advances in Experimental Social Psychology 38:69-119 (medium-to-large effect, d=0.65). https://doi.org/10.1016/S0065-2601(06)38002-1 (source with peer review)
[^checklist-compliance-illusion]: Observational study of surgical-checklist use: high recorded compliance did not guarantee the items were actually performed (records showed 100% adherence; observers found 4 of 13 items done). PMC4484042. https://pmc.ncbi.nlm.nih.gov/articles/PMC4484042/ (source with peer review)
[^haynes-surgical-checklist-2009]: Haynes AB, Weiser TG, Berry WR, et al. (2009). A surgical safety checklist to reduce morbidity and mortality in a global population. New England Journal of Medicine 360(5):491-499. https://www.nejm.org/doi/full/10.1056/NEJMsa0810119 (source with peer review)
[^ha-todo-integration]: Home Assistant: To-do list (todo) and Local to-do (local_todo) integrations, todo entity and todo.update_item action used to auto-complete checklist items. https://www.home-assistant.io/integrations/todo/ (source from a manufacturer or industry)
[^ha-template-alert-statistics]: Home Assistant: Template (binary_sensor), Alert, Statistics/Recorder, Tag (NFC) and Schedule integrations used to define 'in range', escalate, log the audit trail and prove presence. https://www.home-assistant.io/integrations/template/ (source from a manufacturer or industry)
[^aroya-rootzone-steering]: AROYA. Crop-steering and drip-and-drain root-zone monitoring (substrate VWC, EC, pH, dryback, runoff) as the daily root-zone measurement. https://aroya.io/ (source from a manufacturer or industry)
[^eu-gmp-annex1]: EU GMP Annex 1 / EMA environmental-monitoring guidance: define alert and action limits, trend routine monitoring data, require corrective action on excursions. https://health.ec.europa.eu/medicinal-products/eudralex/eudralex-volume-4_en (source from a manufacturer or industry)
[^who-gacp-2003]: World Health Organization (2003). WHO guidelines on good agricultural and collection practices (GACP) for medicinal plants. https://www.who.int/publications/i/item/9241546271 (source from a manufacturer or industry)
[^globalgap-cpcc]: GLOBALG.A.P. Integrated Farm Assurance, Crops / Fruit & Vegetables control points and compliance criteria (hygiene competence, maintained irrigation equipment, record retention). https://www.globalgap.org/ (source from a manufacturer or industry)
[^haccp-prerequisite-ssop]: HACCP prerequisite programmes / Sanitation Standard Operating Procedures: daily sanitation checklists, hygiene checks and pest-control logs (what, how, how-often, who-verifies). https://www.fda.gov/food/hazard-analysis-critical-control-point-haccp/haccp-principles-application-guidelines (source from a manufacturer or industry)
[^digital-checklist-adherence]: Industry analyses of digital vs paper inspection checklists: higher completion rates, faster rounds and fewer documentation errors, driven by lower friction and enforced completeness. https://www.fiixsoftware.com/cmms/mobile-cmms/ (source from a manufacturer or industry)
