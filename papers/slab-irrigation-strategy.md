---
slug: "slab-irrigation-strategy"
title: "Slab irrigation, end to end"
eyebrow: "Feed · Slab steering"
summary: "A measured slab-irrigation field guide: room layout, common dripper runtimes, rooting-in, P0-P3 control, crop-stage steering, EC management and finish."
track: "Flowering"
read_time: "~30 min read"
diagrams: ""
related: ["rockwool-crop-steering", "irrigation-manual", "root-zone-teros12", "f2-crop-steering"]
url: "https://jaketherabbit.github.io/cannabis-white-papers/slab-irrigation-strategy.html"
md_url: "https://jaketherabbit.github.io/cannabis-white-papers/papers/slab-irrigation-strategy.md"
version: "1.2"
updated: "2026-07-18"
license: "CC BY-NC 4.0"
license_url: "https://creativecommons.org/licenses/by-nc/4.0/"
attribution: "The Cannabis White Papers"
refs: []
---

# Slab irrigation, end to end

_Feed · Slab steering · ~30 min read_

> A measured slab-irrigation field guide: room layout, common dripper runtimes, rooting-in, P0-P3 control, crop-stage steering, EC management and finish.

## Purpose and scope

A measured field protocol for rooting stone-wool blocks into 1 m (39 in) slabs, programming the daily irrigation curve, managing root-zone EC and carrying the crop through finish.

Two words carry most of the steering vocabulary used here. A vegetative setting keeps the root zone wetter and refills it sooner, which favours leaf and stem growth. A generative setting lets the root zone dry further before each refill, which favours flower development. The sequence is then straightforward: establish roots on a vegetative setting, set flowers on a generative setting, return to vegetative bulking after stretch slows, then finish with a lower root-zone EC and a controlled larger dryback. Calendar days are defaults. Plant response, representative runoff and comparable-VWC sensor readings decide when to move.[[13]](#ref-13)[[16]](#ref-16)

The operating ruleChange one steering lever at a time, then observe a complete photoperiod. Setting ends when vertical stretch clearly slows. Bulking ends when flower expansion slows and ripening signals dominate.

## Definitions

Field capacityThe VWC a soaked substrate settles at once free water has finished draining out of it. Measure it in this room, on this sensor; a printed guide value is not your field capacity.Absolute drybackPicture a water bottle you fill each morning: how far the level drops by evening tells you how much was used. Dryback is that drop, measured inside the substrate. Absolute dryback is daily peak VWC minus trough VWC, in percentage points. Peak 70% and trough 50% equals a 20-point dryback. This is the controller unit used here.Relative drybackAbsolute dryback divided by the starting VWC, so it is a share of what was there rather than a count of points. A fall from 70% to 42% is a 28-point drop and a 40% relative dryback.P0 / P1 / P2 / P3This guide uses non-overlapping phases: P0 runs from lights-on to first irrigation; P1 refills; P2 maintains; P3 runs from the final irrigation to the next lights-on. Total dryback between irrigation windows includes P3 and the following P0. Other controllers may name these intervals differently.Root-zone ECIdentify the measurement before comparing numbers: feed and runoff are solution samples; bulk EC is the substrate sensor measurement; pore-water EC may be estimated from sensor data. Water loss can concentrate the pore solution, but uptake, feed, drainage and the conversion method also matter. Report EC in mS/cm (equal numerically to dS/m) and compare like methods at comparable VWC.[[18]](#ref-18)RunoffDrain volume divided by applied volume, expressed as a percentage. Catch it from representative plants or slabs in each irrigation zone; do not infer it from pump time.

Convert relative dryback before programmingA 40% relative dryback from a 60% peak is a 24-point controller dryback. From a 70% peak it is 28 points. Convert the unit first, then check the result against the room's recovery floor — the lowest VWC this substrate may reach and still take water up normally at the next irrigation.

A fall from 70% to 50% VWC is 20 percentage points, or approximately 28.6% of the starting water content. These example readings are not crop targets; the peak is not automatically field capacity.Scroll the diagram sideways for full-size labels.

## System layout and measured inputs

Program from measured volume and measured flow. Brand labels and nominal emitter ratings do not tell you what reached the plant.

Substrate15 cm (6 in) stone-wool blocks, approximately 3.6 L (0.95 gal), on 1 m (39 in) slabsWorking layoutThree 7.6 × 1.2 m (25 × 4 ft) tables; compare two rows (14 slabs / 42 plants) and three rows (21 slabs / 63 plants) per table; equipment lanes sit below a continuous canopyOrientationOne-metre (39 in) slabs run along the table; the two-row option has an equipment lane beneath the canopy; the alternative uses three rowsRoot-zone allocationApproximately 7.35 L (1.9 gal) per plant from a 3.6 L (0.95 gal) block plus one-third of an assumed 11.25 L (3.0 gal) slabDistributionPressure-compensating outlets, short feed tubes and a block-top ring or another catch-tested broad wetting patternControlIrrigation zones using substrate VWC and root-zone EC as feedback, with representative physical runoff checks

Side section through a three-plant slab. Substrate remains continuous beneath every block; roots are conceptual. The slab dimensions give 11.25 L. The runtime example separately assumes a 3.6 L block: a literal 150 mm cube is 3.375 L, so use the actual product volume. Drain openings must follow the selected wrapper/product procedure. [[2]](#ref-2)Scroll the diagram sideways for full-size labels.

Seven slabs fit the length; check the cross-section and airflowSeven one-metre slabs use **7.0 m (23 ft)** of a **7.6 m (25 ft)** table, leaving **300 mm (12 in)** at each end when centred. The two-row option carries 14 slabs or **42 plants** per table, 42 slabs or **126 plants** across three tables. The three-row options carry 21 slabs or **63 plants** per table, 63 slabs or **189 plants** room-wide. Across the table width, two 150 mm (6 in) slab rows plus one 203 mm (8 in) inflated tube use about 503 mm (19.8 in); three slab rows plus two tubes use about **856 mm (33.7 in)**, leaving about **344 mm (13.5 in)** of the 1.2 m (4 ft) width for gaps, edges, irrigation hardware and brackets. Every tube has a dedicated 200 mm (8 in) inlet fan. Outlet-hole diameter and spacing are **site-balanced** from measured pressure and airflow; confirm actual wrappers, tube inflation, fan performance, light mounts and access before committing.

Two outside root rows carry 14 slabs and 42 plants. Dots mark plants; gold bars mark upward-directed lights. The central perforated tube has a dedicated inlet fan and capped far end; outlet sizing is intentionally unspecified. Cross-section heights and mounting are schematic. Canopy closure depends on cultivar, veg time and training. Three-row layouts carry 21 slabs / 63 plants; use them if the centre cannot close uniformly. Confirm clearances and airflow on the installation.Scroll the diagram sideways for full-size labels.

#### Normal dripper configurations

A shot is one timed irrigation event, sized as a percentage of the plant's total substrate volume. Every runtime below delivers a 3% shot of about 221 mL (7.5 fl oz) or a 5% shot of about 368 mL (12.4 fl oz) into the assumed 7.35 L (1.9 gal) root-zone allocation. A printed flow rating is only the first calculation. Catch-test representative outlets at operating pressure and replace the table runtime with the measured result.

Supply passes through the emitter and microtube to a supported distributor at the block. Branches are symbols, not a NetBow construction drawing or a specified outlet count. Match the actual ring/stake model, operating pressure and block fit to its documentation; measure the combined output delivered to each plant. [[19]](#ref-19)Scroll the diagram sideways for full-size labels.

Common per-plant emitter configurations. Runtime is rounded to the nearest second.ConfigurationTotal nominal flow3% shot · 221 mL (7.5 fl oz)5% shot · 368 mL (12.4 fl oz)Use and tradeoff1 × 2 L/h2.00 L/h6:3711:02Low-flow single outlet; long events and no emitter redundancy2 × 2 L/h4.00 L/h3:185:31Recommended starting pair where the block-top hardware supports two independent wetting points1 × 4 L/h4.00 L/h3:185:31Simple ring-fed layout; the emitter remains a single point of failure2 × 4 L/h8.00 L/h1:392:45Short events; verify pump ramp, pressure regulation and minimum reliable valve time2 × 0.3 GPH2.27 L/h5:509:43Common low-flow imperial pair with useful redundancy and long wetting time2 × 0.5 GPH3.79 L/h3:305:50Common imperial pair close to 4 L/h totalFormula: runtime seconds = shot mL ÷ (total measured L/h × 1000 ÷ 3600). At 4 L/h per plant, the 42-plant two-row layout requires 168 L/h per table or 504 L/h for three tables; a 63-plant layout requires 252 L/h per table or 756 L/h room-wide.

Use labelled graduated vessels or tared weighing cups at representative outlets across the active zone. Compare collections made over the same time at operating pressure. No measured uniformity result is asserted here. The runtime uses unrounded 220.5 mL and an assumed 7.35 L allocation; replace both allocation and flow with verified values.Scroll the diagram sideways for full-size labels.

Uniformity is part of the recipeCatch-test outlets near and far from the manifold, at the start and end of the longest active zone. Inspect filters and flush laterals to the emitter manufacturer's specification. A single dry plant among normal neighbours is an outlet or contact fault until proven otherwise.

## Block-to-slab water movement

A wet slab and a drying block can coexist. The outcome depends on contact, drainage, water retention and plant uptake.

Water moves through connected stone-wool fibres under hydraulic gradients. After drainage, upper regions can be drier than lower regions, but product properties, irrigation and roots affect the actual distribution. A colour gradient is a conceptual explanation, not a measured profile.[[5]](#ref-5)[[6]](#ref-6)[[7]](#ref-7)

Full fibre contact allows exchange between block and slab. Grodan describes slab-induced block drying in its staged-drainage guidance, and also explains that retaining water initially can reduce that effect. The drainage boundary therefore matters; a saturated slab does not inevitably pull every block dry.[[3]](#ref-3)

Block and slab exchange water through their contact face. Under draining conditions the upper media can become drier while the slab remains wet; irrigation and uptake also affect the profile. This is not a fixed gradient or guaranteed day-by-day outcome. Grodan describes retained water changing block drying in its staged-drainage method. [[3]](#ref-3)Scroll the diagram sideways for full-size labels.

During establishment, inspect the block as well as the slab. Check contact, delivered water and root penetration before adjusting irrigation. A slab probe alone cannot establish whether the block is adequately supplied. Use a documented procedure appropriate to the crop and slab.[[3]](#ref-3)

Three-needle probe symbol; dimensions and sensing outline are schematic. Place representative control probes in comparable rooted zones, recording depth and distance from drippers and drains. Use additional locations for diagnosis when appropriate. METER warns that air gaps bias VWC low; orientation changes the depth sampled. [[18]](#ref-18)Scroll the diagram sideways for full-size labels.

If the block dries outA severely dry block may rewet unevenly. Verify delivery, contact and root condition, and confirm the response to any rescue action. Neither a pale block nor a single slab reading proves irreversible damage. Avoid increasing volume blindly when water is bypassing the root zone.

## Slab preparation: levelling, soaking, charging and slitting

Record the starting state. Uneven saturation, poor contact or an unsuitable drainage opening can make later irrigation readings difficult to interpret.

Charging happens with the saturation solution, not as an unexplained later step. Grodan’s staged method uses an initial opening above the seal and later definitive drainage; it is not the same as a generic set of bottom slits. Select and record one applicable procedure rather than combining their cut patterns. [[2]](#ref-2) [[3]](#ref-3)Scroll the diagram sideways for full-size labels.

1. 1Check the support planeCheck the tray and the intended drain route before placing slabs. Keep the slab support consistent while allowing runoff to reach its collector.
2. 2Saturate and charge togetherUse the selected product procedure and documented feed recipe to saturate through the intended openings. Record solution EC, pH and the required hold. Grodan’s cited staged method specifies at least 24 hours; this is manufacturer guidance for that method.[[2]](#ref-2)[[3]](#ref-3)
3. 3Select the drainage procedureGrodan’s staged method starts with an opening above the seal for partial drainage and adds definitive openings later. This differs from cutting all final bottom slits immediately. Do not combine the methods or infer a universal slit count, angle or size from a diagram.[[3]](#ref-3)
4. 4Open the planting positionsFollow the wrapper instructions so each block seats on exposed slab fibre without a plastic bridge under the contact face.[[2]](#ref-2)
5. 5Place and inspect the blocksSeat established blocks with flat fibre contact. Check block hydration and roots before using the selected rooting-in procedure.

## Rooting-in irrigation and transition criteria

Keep the block supplied while roots cross into the slab, but do not turn a published starting recipe into an unobserved timer.

The later runtime examples use the block plus that plant's allocated share of slab, approximately 7.35 L (1.9 gal) under the working dimensions. The cited practitioner bands are starting hypotheses, not validated limits for this room or newly transplanted roots. Recalculate from the wrapper dimensions and caught flow.[[13]](#ref-13)[[16]](#ref-16)

1. 1Record the transplant stateUse the selected slab preparation and drainage procedure. Record block hydration, slab VWC, feed EC, contact and visible roots.
2. 2Bridge from observationsUse a documented crop- and product-specific rooting-in programme. Verify water delivery to the block and its response. The full block-plus-slab allocation used in later runtime examples is not proof of the volume occupied by roots at transplant.
3. 3Inspect the transitionTrack root penetration and hydration before changing event frequency. Grodan’s staged procedure and the practitioner case study use different schedules; they must not be blended into a universal timer.[[3]](#ref-3)[[15]](#ref-15)
4. 4Exit on evidenceStart the established-root daily cycle when root inspection, plant response and repeatable uptake support it. Confirm outlets and drainage, and log the transition.

The same assembly is shown at three establishment stages. Roots are drawn within continuous substrate, with multiple roots appropriate to a clone-based example. Root inspection and observed uptake inform the transition; these panels do not prescribe a transplant irrigation schedule.Scroll the diagram sideways for full-size labels.

One outlet is a single point of failureA single ring-fed outlet is simple, but a blockage gives that plant zero water. Prefer two independently catch-tested outlets where the wetting hardware supports them, or make visible flow at every ring part of the daily SOP and alarm on zone-flow deviation.

## P0-P3 irrigation phases

Daily phases after root-in. The target is a repeatable curve rather than a fixed timer.PhasePurposeOperating ruleP0Lights-on transpiration before irrigationFrom lights-on to first irrigation. The earlier 1–5% relative band is an unvalidated guide assumption, not a controller instruction. Use the site’s approved trigger and plant-safety limits. Relative percent must be converted to VWC points before programming.P1Refill without channellingUse 2-6% substrate-volume shots, normally 3-5%, spaced 15-30 minutes apart. Stop at the stage-specific peak and runoff response.P2Maintain VWC and steer root-zone ECAdd or extend P2 to lower EC and dryback. Remove or shorten P2 to raise EC and dryback. This is the main fast EC lever.P3Final irrigation to next lights-onDryback begins after the final event, which can precede lights-off. This guide ends P3 at lights-on, when P0 begins. Rescue/interlock actions take precedence over the example phase sequence.

A constructed 24-hour example with a 12-hour light period. P0 is lights-on to first irrigation; P1 refills; P2 maintains; P3 runs from the final event to the next lights-on. Total between-irrigation dryback spans P3 plus the following P0. The trace and event timing illustrate this convention only. EC requires its own measured trace and method; no universal inverse EC curve is asserted.Scroll the diagram sideways for full-size labels.

VegetativeLarger wet-up, more drainagePeak at or slightly above measured field capacity, use the larger end of the locally validated shot band, add P2 events, and target 8-16% runoff. The objective is lower root-zone EC and a smaller dryback.GenerativeRestrict peak and drainagePeak at or below field capacity, use the smaller end of the shot band, shorten the irrigation window, and target 1-7% runoff. The objective is higher root-zone EC and a larger dryback.

A 3-5% normal shot on the assumed 7.35 L (1.9 gal) allocation is about 221-368 mL (7.5-12.4 fl oz) per plant. The outside 2-6% guardrail is about 147-441 mL (5.0-14.9 fl oz). Runtime depends on total measured flow per plant, not the rating printed on one emitter.[[13]](#ref-13)

**Plot EC separately.** Use a common time axis with VWC and irrigation events, but identify bulk, estimated pore-water, feed or runoff EC. A synthetic inverse curve cannot predict a sensor response. Label measured records with sensor, calibration, crop and sampling context.[[18]](#ref-18)

## Crop-stage irrigation program

Set flowers early, bulk after stretch, then finish with a lower root-zone EC and a larger controlled dryback.

Stage labels describe observations. They do not prove that a particular irrigation bias will produce the pictured outcome. Yellow leaves alone do not establish harvest readiness. Apply the separately attributed programme only within validated room and cultivar limits. [[13]](#ref-13) [[16]](#ref-16)Scroll the diagram sideways for full-size labels.

Starting targets for LED flower in stone wool. Dryback is absolute VWC points because that is the controller unit.StageSteerPeak and runoffController drybackRoot-zone EC (mS/cm; method-specific)Switch signalEstablished vegVegetativeAt/above measured field capacity; 8-16% runoff10-15 points3-5Roots established, repeatable uptake, plant ready to flipFlower setting, nominal days 1-21GenerativeAt/below field capacity; 1-7% runoffStart near 15 points and move toward 20-25 over the first three weeks; never cross the recovery floor5-10Vertical stretch has clearly slowed or stoppedFlower bulk, nominal days 22-42VegetativeAt/above field capacity; 8-16% runoff10-15 points3.5-6Flower expansion slows and ripening signals dominateFinish, normally final 10-14 daysLower EC plus generative drybackAt/below field capacity; 1-7% unless correcting excess EC20-25 points initially; extend only from cultivar data and stay above the floor3-4Harvest readiness, not a fixed day numberThese are starting bands assembled from the cited technical sources. Advance one lever at a time and compare equivalent VWC points in the daily trace.

The phase switch is plant-ledUse the calendar to anticipate the change, then switch from generative setting to vegetative bulking when stretch actually slows. That prevents a fast cultivar being stressed for an extra week or a slow cultivar being bulked before flower set is complete.[[13]](#ref-13)[[16]](#ref-16)

## Case study: three-plant slab measurements

A commercial grower described a deliberately simple slab-irrigation system on the We The Growers podcast. It is useful as an operating example, not as a recipe to copy unchanged.[[15]](#ref-15)

Three blocks sit on one slab supported above a runoff tray. Gold shows the complete drain path to a graduated collector; blue shows feed tubing. Slit positions are schematic, not a cutting specification. Capture all relevant drainage without allowing the slab to sit in standing runoff. Dividing slab totals by three gives an average, not individual plant measurements. [[15]](#ref-15)Scroll the diagram sideways for full-size labels.

Reported practiceWhat the episode describesPlants move from 10 × 10 × 6.4 cm (4 × 4 × 2.5 in) blocks onto pre-saturated slabs after about 16 days of veg. One whole slab is raised over a runoff tray; applied and drained volume are divided by its three plants. Staff report daily in/out volume and check runoff pH and EC once or twice weekly.For the first 48 hours on slabs, the reported starting program is about 12 lights-on events, two minutes each through a 1.9 L/h (0.5 GPH) outlet. The grower then allows a hard three-to-four-day dryback before building toward full irrigation. Around day 14, a typical reported pattern is 10-12 four-minute events, with frequency adjusted to cultivar demand and observed drainage.Adopted hereWhat transfers wellMeasure a complete three-plant slab instead of guessing runoff from pump time.Keep event duration stable after validation and tune frequency to uptake and drainage.Use a scheduled room walk to confirm slabs are wetting and drainage has begun.Record deviations when a room or cultivar drinks differently, then use that record for the next cycle.Site-specificWhat is not copied blindlyThe 48-hour wetting period and following multi-day dryback are aggressive and need block/slab VWC, root inspection and a recovery floor.One outlet per plant has no emitter redundancy.Exact feed EC, runoff and frequency belong to that facility's media, climate, light and cultivar.Physical checks complement sensors; they do not justify ignoring a verified fault in either system.

Podcast timestamps: slab placement 27:33-28:12; slab-scale runoff collection 31:43-32:33; initial flower irrigation 39:44-41:12; first-three-week adjustment 48:55-53:37.[[15]](#ref-15)

## EC correction and finishing strategy

Correct root-zone EC from what you measure, and treat the finish as a defined procedure with an endpoint. There is no blanket day-45 dilution and no automatic plain-water week.

EC is reported in mS/cm (numerically equal to dS/m); solution colour is not an EC measurement. A substrate sensor’s bulk EC and estimated pore-water EC are different quantities. The cited Athena finish is a product procedure, not a universal flushing requirement. [[18]](#ref-18) [[17]](#ref-17)Scroll the diagram sideways for full-size labels.

1. 1Verify a high EC readingCompare root-zone EC at equivalent VWC. Pore-water EC may increase as water is removed, but bulk EC also depends on water content and does not follow a universal inverse curve. Identify the measurement method. Confirm with representative runoff volume and EC before changing the program.
2. 2Correct excess EC with controlled leachingUse balanced feed whose EC is below the root-zone EC, increase P2 and runoff temporarily, and watch the next complete trace. Stop when root-zone and runoff EC return toward the stage band. Do not combine a feed-EC change and a timing change on the same day unless plant safety requires it.
3. 3Final two weeksUse the cited two-part finish procedure at the scheduled EC rather than tapering by default. Recheck pH after the component change.[[17]](#ref-17)
4. 4Final clean-water periodThe cited procedure uses its line-cleaning product in RO water for the final one to three days and specifies one day in stone wool. Use root-zone or runoff EC to confirm the finish. This is a defined product procedure, not a standing instruction to plain-water flush every crop.[[17]](#ref-17)

## Climate demand and irrigation response

Irrigation targets only make sense alongside the conditions that create the demand, and two of those are worth naming. PPFD is the light intensity actually arriving at the canopy. VPD is how much more water vapour the air could still hold before it saturates, so the higher it runs, the harder the air pulls water out of the leaf. The bands below are published operating envelopes, not permission to push a stressed cultivar to the top edge.[[13]](#ref-13)

Higher environmental demand does not guarantee higher uptake in a stressed plant. Use comparable observations before changing irrigation. For perforated air tubes, measure static pressure and air movement at repeatable positions; a second tube has no quantified benefit here without measurements or a specified model.Scroll the diagram sideways for full-size labels.

Published environmental bands used as starting context for the irrigation program.StageAir temperatureRHVPDPPFDVeg22.2-27.7 °C (72-82 °F)58-75%0.8-1.0 kPa300-600Flower stretch25.5-27.7 °C (78-82 °F)60-72%1.0-1.2 kPa600-1000Flower bulk23.8-26.6 °C (75-80 °F)60-70%1.0-1.2 kPa850-1200Flower finish18.3-22.2 °C (65-72 °F)50-60%1.2-1.4 kPa600-900

DemandTreat light or VPD changes as irrigation changesAfter PPFD, under-canopy light, VPD or CO2 changes, expect a new uptake rate. Hold the steering target steady long enough to observe the new curve before deciding the irrigation program is wrong.UniformityInspect climate spread before steering the rowCompare paired sensors and representative runoff along the 7.6 m (25 ft) run. If front and back diverge, inspect airflow, drain fall, slit geometry and outlet output before steering the whole row around one bad position.

This conversion assumes the electrical input ultimately remains as heat within the room boundary. Account separately for remote drivers or energy leaving that boundary. No leaf-temperature reduction or local heat-index benefit is predicted from fan count.Scroll the diagram sideways for full-size labels.

## Troubleshooting

These checks narrow possibilities rather than proving one cause from a symptom. Restore a failed outlet or address acute plant stress promptly. Observe a complete grow-day after elective steering changes when appropriate; do not wait a day to correct a verified failure.Scroll the diagram sideways for full-size labels.

Table 4. Diagnose from the trace and representative runoff before changing a setpoint.SymptomLikely causeFirst actionRunoff high, VWC barely risesChannelling, poor block-slab contact, or emitter placementInspect physically; slow the event or hand-rewet with balanced feed; do not increase volume blindlyRoot-zone EC climbs day over day outside the stage bandToo little leaching, too much dryback, feed mismatch, or excessive demandVerify at equal VWC, check feed EC and climate, then add P2/runoff with one bounded changeRoot-zone EC falls below targetPeak/runoff too high for the steering phaseReduce P2 or peak slightly and observe one full dayP1 never reaches its targetTarget set above the peak VWC this slab can actually reach, blocked emitter, wrong flow assumption, or too few ramp eventsCatch-test, confirm the achievable peak VWC and the substrate volume, then adjust the modelFresh transplants stall while the slab stays wetInadequate block hydration, poor contact, delivery failure or impaired rootsInspect the block, roots, contact and caught outlet flow; do not use the slab sensor as the sole triggerDryback suddenly deepensMissed event or demand change from PPFD, VPD, CO2 or airflowCheck logs and climate first; compensate with P2 only after identifying the causeOne plant wilts while neighbours track normallySingle-emitter failure or local contact problemRestore flow and hand-rescue that block with balanced feed if required

## Combined irrigation setpoints

Guide values and their status. None is established here as a site-validated OPERATIONAL setpoint.QuantityValue / conditionEvidence statusSubstrate model3.6 L (0.95 gal) block + one-third of an assumed 11.25 L (3.0 gal) slab = 7.35 L (1.9 gal) per plant; confirm the wrapperINFERRED · assumed geometry; verify productShot guardrail2-6% = about 147-441 mL (5.0-14.9 fl oz); calculate time from total caught flow per plantCORPUS · guide synthesis; validate before useNormal P1 shot3-5% = about 221-368 mL (7.5-12.4 fl oz); normally spaced 15-30 minutes during the rampCORPUS · guide synthesis; validate before useP0 after lights-onSite-approved trigger required. The former 1–5% relative band has no verified site source here. Arithmetic example: 5% relative from 70% VWC = 3.5 points.INFERRED · do not copy into a controllerVegetative runoff8-16%; peak at or slightly above measured field capacityCORPUS · guide synthesis; validate before useGenerative runoff1-7%; peak at or below measured field capacityCORPUS · guide synthesis; validate before useController drybackVeg/bulk 10-15 points; setting builds from 15 toward 20-25; finish starts 20-25; all bounded by the recovery floorCORPUS · guide synthesis; validate before useRoot-zone ECVeg 3-5; flower setting 5-10; bulk 3.5-6; finish 3-4 mS/cm; identify the measurement methodCORPUS · guide synthesis; validate before useFlower arcGenerative until stretch ends; vegetative bulk until expansion slows; lower EC plus generative dryback to finishCORPUS · guide synthesis; validate before useDefined finishUse the cited component-change and final clean-water procedure; verify the endpoint from root-zone or runoff ECManufacturer procedure · Athena [17]; product-specific

The five rulesConvert relative dryback to controller points before programming it.Change from setting to bulk when stretch ends, not because a calendar page turned.Use P2 and runoff as the fast root-zone EC control; keep feed EC as the slower recipe lever.Verify shot duration from actual outlet flow and total assigned substrate volume.For elective steering, make one bounded change and observe a complete grow-day. Correct verified failures promptly and confirm recovery.

## References

Grodan (ROCKWOOL Group). The right block–slab interaction ensures healthy plants. Grodan crop guidance. (non-peer-reviewed source) [https://www.grodan.com/global/crops/sweet-pepper/the-right-block-slab-interaction-ensures-healthy-plants/](https://www.grodan.com/global/crops/sweet-pepper/the-right-block-slab-interaction-ensures-healthy-plants/)

Grodan (ROCKWOOL Group). Handling and placing of the slabs. Technical sheet TS 3.3. (non-peer-reviewed source) [https://www.grodan.com/syssiteassets/downloads/tools--services/english/ts-3-3-handling-the-slabs-en.pdf](https://www.grodan.com/syssiteassets/downloads/tools--services/english/ts-3-3-handling-the-slabs-en.pdf)

Grodan (ROCKWOOL Group). Cutting drainage holes in stages is good for plants and saves water. Grodan knowledge base. (non-peer-reviewed source) [https://www.grodan.com/global/knowledge/root-zone-management/irrigation-and-nutrients/Cutting-drainage-holes-in-stages-is-good-for-plants-and-saves-water/](https://www.grodan.com/global/knowledge/root-zone-management/irrigation-and-nutrients/Cutting-drainage-holes-in-stages-is-good-for-plants-and-saves-water/)

Grodan (ROCKWOOL Group), with B. Nikaj; trials with Wageningen University & Research (2020–2022). Grodan research reveals new insights into optimal irrigation strategy for large-scale production of medicinal crops. Whitepaper. (non-peer-reviewed source) [https://www.grodan.com/](https://www.grodan.com/)

Bougoul S, Boulard T (2006). Water dynamics in two rockwool slab growing substrates of contrasting densities. Scientia Horticulturae 107(4):399–404. [https://doi.org/10.1016/j.scienta.2005.11.007](https://doi.org/10.1016/j.scienta.2005.11.007)

Bougoul S, Ruy S, de Groot F, Boulard T (2005). Hydraulic and physical properties of stonewool substrates in horticulture. Scientia Horticulturae 104(4):391–405. [https://doi.org/10.1016/j.scienta.2005.01.018](https://doi.org/10.1016/j.scienta.2005.01.018)

da Silva FF, Wallach R, Polak A, Chen Y (1998). Distribution of nutrients and water in rockwool slabs. Scientia Horticulturae 72(3–4):277–285. [https://www.sciencedirect.com/science/article/abs/pii/S0304423897001441](https://www.sciencedirect.com/science/article/abs/pii/S0304423897001441)

International Society for Horticultural Science (ISHS). Utilizing the HYDRUS model as a tool for understanding soilless substrate water dynamics. Acta Horticulturae 1168. [https://www.ishs.org/ishs-article/1168_41](https://www.ishs.org/ishs-article/1168_41)

Caplan D, Dixon M, Zheng Y (2019). Increasing inflorescence dry weight and cannabinoid content in medical cannabis using controlled drought stress. HortScience 54(5):964–969. [https://doi.org/10.21273/HORTSCI13510-18](https://doi.org/10.21273/HORTSCI13510-18)

Malik M, Tlustoš P (2025). Soilless growing media for cannabis cultivation. Agriculture 15(18):1955. [https://www.mdpi.com/2077-0472/15/18/1955](https://www.mdpi.com/2077-0472/15/18/1955)

Nemali KS, van Iersel MW (2006). An automated system for controlling drought stress and irrigation in potted plants. Scientia Horticulturae 110(3):292–297. [https://doi.org/10.1016/j.scienta.2006.07.009](https://doi.org/10.1016/j.scienta.2006.07.009)

Owen J, Norden D (Profile Products). Understanding drainage in horticultural growing media. Greenhouse Management. (non-peer-reviewed source) [https://www.greenhousemag.com/article/growing-media-defining-drainage-improve-substrate/](https://www.greenhousemag.com/article/growing-media-defining-drainage-improve-substrate/)

Athena Agriculture. _Precision Irrigation Strategy_, metric edition, document A01.002. (manufacturer technical guidance) [Official Athena procedure](https://support.athenaag.com/hc/en-us/articles/25975395644315-Precision-Irrigation-Strategy)

We The Growers podcast, E.37 — Bones Grows (ZBRA / Wow Town). Practitioner discussion of block-on-slab irrigation and root-zone management. (non-peer-reviewed practitioner source) [Official episode](https://www.youtube.com/watch?v=l8WU-sRxNnI)

We The Growers podcast, E.31 — Sipkoi, published 13 August 2024. Slab placement 27:33-28:12; runoff collection 31:43-32:33; initial flower irrigation 39:44-41:12; first-three-week adjustment 48:55-53:37. (non-peer-reviewed practitioner source; timestamps checked against episode captions) [Official episode](https://www.youtube.com/watch?v=Fv2jqkHsaBM)

Whipple J. _The CCI Black Book_, first edition, 2023, Garden Management chapter, pp. 56-63. (commercial cultivation guidance) [Publisher](https://ccibook.com/)

Athena Agriculture. _Fade Procedure_. Replace Core with Fade for the final two weeks, feed Fade + Bloom at full EC, then use Cleanse in RO water for the final 1-3 days, one day in rockwool. (manufacturer product procedure) [Official Athena Fade procedure](https://support.athenaag.com/hc/en-us/article_attachments/14949498083739)

METER Group. TEROS 11/12 manual. Sensor installation, measurement volume and bulk-to-pore-water EC conversion. (manufacturer technical guidance) [Manufacturer documentation](https://publications.metergroup.com/Manuals/20587_TEROS11-12_Manual_Web.pdf)

Netafim. NetBow product information. Consult the selected model and assembly instructions. (manufacturer technical guidance) [Manufacturer documentation](https://www.netafim.com/en/products-and-solutions/product-offering/drip-irrigation-products/netbow/)


