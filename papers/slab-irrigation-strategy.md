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

## What this paper is

A measured field protocol for rooting blocks into metre slabs, programming the daily irrigation curve, managing root-zone EC and carrying the crop through finish.

The operating sequence is simple: establish roots with a vegetative bias, set flowers with a generative bias, return to vegetative bulking after stretch slows, then finish with lower root-zone EC and a controlled larger dryback. Calendar days are defaults. Plant response, representative runoff and comparable-VWC sensor readings decide when to move.[[13]](#ref-13)[[16]](#ref-16)

The operating ruleChange one steering lever at a time, then observe a complete photoperiod. Setting ends when vertical stretch clearly slows. Bulking ends when flower expansion slows and ripening signals dominate.

## The working setup

Program from measured volume and measured flow. Brand labels and nominal emitter ratings do not tell you what reached the plant.

Substrate6 in stone-wool blocks, approximately 3.6 L, on 1 m slabsWorking layoutThree 7.6 × 1.2 m tables; compare a clear-centre 14-slab / 42-plant layout with 21-slab / 63-plant three-row layoutsOrientationOne-metre slabs run along the table; Option 1 has two outside rows and a clear centre, while Options 2–5 use three rowsRoot-zone allocationApproximately 7.35 L per plant from a 3.6 L block plus one-third of an assumed 11.25 L slabDistributionPressure-compensating outlets, short feed tubes and a block-top ring or another catch-tested broad wetting patternControlIrrigation zones using substrate VWC and root-zone EC as feedback, with representative physical runoff checks

Seven slabs solve the length; verify the 1.2 m cross-section and airflowSeven one-metre slabs use **7.0 m** of a **7.6 m** table, leaving **300 mm** at each end when centred. The clear-centre option carries 14 slabs or **42 plants** per table—42 slabs or **126 plants** across three tables. The three-row options carry 21 slabs or **63 plants** per table—63 slabs or **189 plants** room-wide. At the working dimensions, two 150 mm slab rows plus one 203 mm inflated tube use about 503 mm; three slab rows plus two tubes use about **856 mm**, leaving about **344 mm** for gaps, edges, irrigation hardware and brackets. Every tube has a dedicated 200 mm inlet fan. Outlet-hole diameter and spacing are **site-balanced** from measured pressure and airflow; confirm actual wrappers, tube inflation, fan performance, light mounts and access before committing.

> **Diagram.** Figure 1. **Five per-table layout options.** Option 1 keeps a **clear centre**: two outside rows of **seven slabs**, one perforated FlowMax tube driven by its own **200 mm fan**, and two longitudinal under-canopy light runs. Options 2–5 use **three longitudinal rows** of seven slabs: slabs only; two fan-driven FlowMax tubes; tubes with longitudinal lighting; and tubes with evenly spaced transverse lighting. Arrows show fan direction and the small dots are schematic air-outlet holes. The selected option repeats on all three tables; balance perforations and confirm mounting details on site.

#### Illustrated hardware examples

These renders make the components easier to recognise. They are not as-built drawings; the scaled SVG, caught flow and tape measurements remain authoritative.

Illustration 1. Clear-centre hardware concept. The render shows the relationship between the outside plant rows, perforated air tube, inlet fan and longitudinal lights. Use the scaled layout above—not this AI render—for counts and dimensions.

Illustration 2. Dripper assembly concept. Punch point, pressure-compensating outlet, short feed tube, broad-wetting ring and catch vessel are all visible. Confirm the installed fittings and caught flow.

Illustration 3. Three-plant slab concept. The cutaway highlights block-to-slab contact, root entry, the wrapped slab and drain-side slits; actual wrapper and slit geometry remain site-specific.

Illustration 5. Sensor-placement concept. Use paired probes in representative rooted positions and reject edge, drain-end, emitter-adjacent or poorly contacted locations after a physical check.

#### Normal dripper configurations

Every runtime below delivers a 3% shot of about 221 mL or a 5% shot of about 368 mL into the assumed 7.35 L root-zone allocation. Nominal flow is only the first calculation. Catch-test representative outlets at operating pressure and replace the table runtime with the measured result.

Common per-plant emitter configurations. Runtime is rounded to the nearest second.ConfigurationTotal nominal flow3% shot · 221 mL5% shot · 368 mLUse and tradeoff1 × 2 L/h2.00 L/h6:3711:02Low-flow single outlet; long events and no emitter redundancy2 × 2 L/h4.00 L/h3:185:31Recommended starting pair where the block-top hardware supports two independent wetting points1 × 4 L/h4.00 L/h3:185:31Simple ring-fed layout; the emitter remains a single point of failure2 × 4 L/h8.00 L/h1:392:45Short events; verify pump ramp, pressure regulation and minimum reliable valve time2 × 0.3 GPH2.27 L/h5:509:43Common low-flow imperial pair with useful redundancy and long wetting time2 × 0.5 GPH3.79 L/h3:305:50Common imperial pair close to 4 L/h totalFormula: runtime seconds = shot mL ÷ (total measured L/h × 1000 ÷ 3600). At 4 L/h per plant, the 42-plant clear-centre layout requires 168 L/h per table or 504 L/h for three tables; a 63-plant layout requires 252 L/h per table or 756 L/h room-wide.

Uniformity is part of the recipeCatch-test outlets near and far from the manifold, at the start and end of the longest active zone. Inspect filters and flush laterals to the emitter manufacturer's specification. A single dry plant among normal neighbours is an outlet or contact fault until proven otherwise.

## Definitions that prevent bad programming

Field capacityThe stable VWC after free drainage. Measure it in this room; a printed guide value is not the sensor's field capacity.Absolute drybackDaily peak VWC minus trough VWC, in percentage points. Peak 70% and trough 50% equals a 20-point dryback. This is the controller unit used here.Relative drybackAbsolute dryback divided by starting VWC. A fall from 70% to 42% is a 28-point drop and a 40% relative dryback.P0 / P1 / P2 / P3P0 is the lights-on hold, P1 is the controlled refill, P2 maintains the daytime plateau and manages EC, and P3 is the lights-off-to-next-P1 dryback.Root-zone ECThe EC in the substrate solution, not the batch tank. Compare readings at similar VWC because EC rises automatically as water leaves.RunoffDrain volume divided by applied volume. Measure representative plants or slabs by irrigation zone; do not infer it from pump time.

Convert relative dryback before programmingA 40% relative dryback from a 60% peak is a 24-point controller dryback. From a 70% peak it is 28 points. Convert the unit, then enforce the room's recovery floor.

## Why a soaked slab pulls your block dry

The most counter-intuitive fact in slab growing: a fully saturated slab actively drains the block sitting on it.

Stone wool holds nearly all of its water at suctions of just a few centimetres of head, and its hydraulic conductivity near saturation is very high.[[5]](#ref-5)[[6]](#ref-6) The practical consequence is that water content stratifies sharply with height above the drain plane — wet at the bottom, dry at the top — in any connected column of fibre.[[7]](#ref-7)

Set a Hugo on a slab with full contact and you have created one connected column, and the block is now its highest point. At equilibrium the block must end up driest — the slab's extra height pulls the block's water down into itself. Grodan states this directly: the slab “extracts moisture from the block”, and this is precisely why drip must keep running on the block several times per day until roots have penetrated the slab.[[1]](#ref-1) Meanwhile the plant is transpiring out of that same block. The block is being drained from below and above at once.

> **Diagram.** Figure 1. Matric equilibrium in a block-on-slab column. The soaked slab and the light block are not a contradiction — they are the predicted equilibrium state. Nothing is wrong with the slab; the block simply sits higher above the drain.

This is why the stage you can see with your hands — top block feels light, slab feels soaked — is not a watering error to fix by irrigating the slab. It is the physics working as designed, and the answer is to feed the block, frequently, until the roots are established in the slab.[[1]](#ref-1)[[14]](#ref-14)

If the block dries outAll the roots are in the block. If the block crosses the recovery floor it channels and the dripper cannot fix it[[12]](#ref-12) — you lose root mass in the only substrate the plant currently occupies, and the transplant stalls exactly when it should be accelerating. The reference grower's words: “if you're not watering that cube, it doesn't matter about the slab… you got to keep that cube hydrated so you don't lose your root base.”[[14]](#ref-14)

Illustration 4. VWC cross-section concept. Blue indicates the wetter lower region expected after drainage; it is not a calibrated VWC scale.

## Slab prep: level, soak, charge, slit

Everything downstream inherits the slab's starting state. Get it wrong here and you chase it for eight weeks.

1. 1Level the traysWC stratifies with height — a tray tilted along its 7.6 m run becomes a wet end and a dry end that no schedule can equalise. Check fall with a level before slabs go down; only the deliberate drain fall should remain.
2. 2Fill the slabs inside the wrapperFill through the block holes with veg-strength feed — balanced feed at EC 2.5–3.0, pH ~5.5 — until the slab is visibly full with no air pockets, and let it sit **24 hours**.[[2]](#ref-2) The soak wets every fibre (dry stone wool is hydrophobic enough to channel from day one if skipped) and pre-charges the slab so roots enter feed, not water.
3. 3Cut drain slits after the soak, in stagesSmall slits first — 1–2 cm at 45° at the slab's lowest edge, offset from block positions, two or three per slab. Grodan cuts drainage in stages deliberately: a wetter slab early aids rooting-in; enlarge slits later when the generative phase needs faster drainage.[[3]](#ref-3) After slitting, the slab settles from saturation to field capacity.
4. 4Open the wrapper under each block positionCut the plastic slightly smaller than the block footprint so fibre touches fibre with no plastic bridging — hydraulic contact is the whole mechanism, and a strip of wrapper under one corner of a block is an invisible rooting failure.
5. 5Place blocks with full flat contactBlocks go down once roots are visible at the Hugo base, block at field capacity. Press down gently — no rocking. Contact area determines how fast the slab pulls the block dry _and_ how easily roots cross the boundary.[[1]](#ref-1)

## Rooting-in: measured shots, plant-led exit

Keep the block supplied while roots cross into the slab, but do not turn a published starting recipe into an unobserved timer.

The percentages below use the block plus that plant's allocated share of slab, approximately 7.35 L under the working dimensions. Treat 2-6% as the outside shot-size guardrail and 3-5% as the normal starting band after root-in. Recalculate from the wrapper dimensions and caught flow.[[13]](#ref-13)[[16]](#ref-16)

1. 1Pre-charge and drain correctlyFully hydrate the slab with balanced feed, let it soak, then open the drain-side slit. Place a fully hydrated block with complete fibre contact. Record block weight or VWC, slab VWC and feed EC at transplant.
2. 2Days 1-3: bridge irrigationBegin about one hour after lights-on. Apply two measured 3-5% shots about 20 minutes apart. Add later shots only while the block is demonstrably losing water and each event produces a clean wet-up response. At 7.35 L per plant, 3-5% is about 221-368 mL; use the configuration table for nominal runtimes and the catch test for the programmed runtime.
3. 3Remove late shots as roots enterOnce roots are visibly entering the slab, remove later events before removing the morning bridge. Let the combined root zone begin a controlled dryback. A published transition value is a reference point, not a universal sensor number.
4. 4Exit on evidenceStart normal P1 only when roots have entered the slab, daily uptake is visible in the trace, all outlets pass a catch test, and the slab can wet toward measured field capacity without the block remaining stagnant. The slab sensor informs the decision; it does not run the early events by itself.

One outlet is a single point of failureA single ring-fed outlet is simple, but a blockage gives that plant zero water. Prefer two independently catch-tested outlets where the wetting hardware supports them, or make visible flow at every ring part of the daily SOP and alarm on zone-flow deviation.

## P0-P3 on the controller

Daily phases after root-in. The target is a repeatable curve, not a fixed timer.PhasePurposeOperating ruleP0Lights-on transpiration before irrigationAllow 1-5% additional relative dryback after lights-on, normally 30 minutes to two hours. End early at the recovery floor or a climate/feed interlock.P1Refill without channellingUse 2-6% substrate-volume shots, normally 3-5%, spaced 15-30 minutes apart. Stop at the stage-specific peak and runoff response.P2Maintain VWC and steer root-zone ECAdd or extend P2 to lower EC and dryback. Remove or shorten P2 to raise EC and dryback. This is the main fast EC lever.P3Overnight oxygenation and drybackStop routine irrigation and allow the programmed dryback. Dark-period irrigation is rescue-only when the recovery floor or plant safety requires it.

VegetativeLarger wet-up, more drainagePeak at or slightly above measured field capacity, use the larger end of the validated shot band, add P2 events, and target 8-16% runoff. The objective is lower root-zone EC and a smaller dryback.GenerativeRestrict peak and drainagePeak at or below field capacity, use the smaller end of the shot band, shorten the irrigation window, and target 1-7% runoff. The objective is higher root-zone EC and a larger dryback.

A 3-5% normal shot on the assumed 7.35 L allocation is about 221-368 mL per plant. The outside 2-6% guardrail is about 147-441 mL. Runtime depends on total measured flow per plant, not the label on one emitter.[[13]](#ref-13)

#### Irrigation-cycle cross-section

Illustration 6. Irrigation-cycle concept. The four repeated cross-sections link the controller phases to VWC and pore-water EC direction. The base render is illustrative; the phase definitions and trend labels are editable overlays, not measured room history.

#### Model curves for comparison

Calculated exampleModel daily VWC traces for four absolute dryback depthsFour curves share a seventy percent peak and finish at sixty, fifty-five, fifty and forty-five percent VWC, representing ten, fifteen, twenty and twenty-five percentage-point drybacks.Daily VWC shape by absolute dryback depthSame 70% peak; trough changes by 10, 15, 20 or 25 absolute percentage pointsP0P1P2P340%50%60%70%10-point dryback15-point dryback20-point dryback25-point drybackModel photoperiod sequence · not room historyGraph 1. Representative model curves for the controller. Dryback is peak VWC minus trough VWC in absolute percentage points. These traces demonstrate shape and phase timing; replace them with room history before diagnosing a crop.Calculated exampleTeaching model comparing VWC and root-zone EC through drydown and refillAs volumetric water content falls, a simplified EC tendency rises. Refill restores VWC and dilutes the modelled root-zone concentration.VWC and EC must be compared at equivalent water contentTeaching model only · concentration tendency, not a substrate-sensor predictionrefillVWCEC tendencyDrydown → concentration → measured wet-up and dilutionGraph 2. A simplified teaching model: EC can rise automatically as water leaves, then fall as irrigation restores water and leaches ions. Compare actual EC readings at similar VWC; this curve is not a sensor prediction.

## Veg to chop: the operating arc

Set flowers early, bulk after stretch, then finish with a lower root-zone EC and a larger controlled dryback.

Starting targets for LED flower in stone wool. Dryback is absolute VWC points because that is the controller unit.StageSteerPeak and runoffController drybackRoot-zone ECSwitch signalEstablished vegVegetativeAt/above measured field capacity; 8-16% runoff10-15 points3-5Roots established, repeatable uptake, plant ready to flipFlower setting, nominal days 1-21GenerativeAt/below field capacity; 1-7% runoffStart near 15 points and move toward 20-25 over the first three weeks; never cross the recovery floor5-10Vertical stretch has clearly slowed or stoppedFlower bulk, nominal days 22-42VegetativeAt/above field capacity; 8-16% runoff10-15 points3.5-6Flower expansion slows and ripening signals dominateFinish, normally final 10-14 daysLower EC plus generative drybackAt/below field capacity; 1-7% unless correcting excess EC20-25 points initially; extend only from cultivar data and stay above the floor3-4Harvest readiness, not a fixed day numberThese are starting bands assembled from the cited technical sources. Advance one lever at a time and compare equivalent VWC points in the daily trace.

The phase switch is plant-ledUse the calendar to anticipate the change, then switch from generative setting to vegetative bulking when stretch actually slows. That prevents a fast cultivar being stressed for an extra week or a slow cultivar being bulked before flower set is complete.[[13]](#ref-13)[[16]](#ref-16)

## Sipkoi: simple measurements around a three-plant slab

A commercial grower described a deliberately simple slab-irrigation system on the We The Growers podcast. It is useful as an operating example, not as a recipe to copy unchanged.[[15]](#ref-15)

Reported practiceWhat the episode describesPlants move from 4 × 4 × 2.5 in blocks onto pre-saturated slabs after about 16 days of veg. One whole slab is raised over a runoff tray; applied and drained volume are divided by its three plants. Staff report daily in/out volume and check runoff pH and EC once or twice weekly.For the first 48 hours on slabs, the reported starting program is about 12 lights-on events, two minutes each through a 0.5 GPH outlet. The grower then allows a hard three-to-four-day dryback before building toward full irrigation. Around day 14, a typical reported pattern is 10-12 four-minute events, with frequency adjusted to cultivar demand and observed drainage.Adopted hereWhat transfers wellMeasure a complete three-plant slab instead of guessing runoff from pump time.Keep event duration stable after validation and tune frequency to uptake and drainage.Use a scheduled room walk to confirm slabs are wetting and drainage has begun.Record deviations when a room or cultivar drinks differently, then use that record for the next cycle.Site-specificWhat is not copied blindlyThe 48-hour wetting period and following multi-day dryback are aggressive and need block/slab VWC, root inspection and a recovery floor.One outlet per plant has no emitter redundancy.Exact feed EC, runoff and frequency belong to that facility's media, climate, light and cultivar.Physical checks complement sensors; they do not justify ignoring a verified fault in either system.

Podcast timestamps: slab placement 27:33-28:12; slab-scale runoff collection 31:43-32:33; initial flower irrigation 39:44-41:12; first-three-week adjustment 48:55-53:37.[[15]](#ref-15)

## Correct EC first; use a defined finish

There is no blanket day-45 dilution and no automatic plain-water week.

1. 1Verify a high EC readingCompare root-zone EC at equivalent VWC. A drier substrate reads higher even without added salt. Confirm with representative runoff volume and EC before changing the program.
2. 2Correct excess EC with controlled leachingUse balanced feed whose EC is below the root-zone EC, increase P2 and runoff temporarily, and watch the next complete trace. Stop when root-zone and runoff EC return toward the stage band. Do not stack a feed-EC change and a timing change on the same day unless plant safety requires it.
3. 3Final two weeksUse the cited two-part finish procedure at the scheduled EC rather than tapering by default. Recheck pH after the component change.[[17]](#ref-17)
4. 4Final clean-water periodThe cited procedure uses its line-cleaning product in RO water for the final one to three days and specifies one day in stone wool. Use root-zone or runoff EC to confirm the finish. This is a defined product procedure, not a standing instruction to plain-water flush every crop.[[17]](#ref-17)

## Climate defines how fast the irrigation curve moves

Irrigation targets only make sense beside PPFD, VPD and temperature. Published bands are operating envelopes, not permission to force a stressed cultivar to the top edge.[[13]](#ref-13)

Published environmental bands used as starting context for the irrigation program.StageAir temperatureRHVPDPPFDVeg22.2-27.7°C58-75%0.8-1.0 kPa300-600Flower stretch25.5-27.7°C60-72%1.0-1.2 kPa600-1000Flower bulk23.8-26.6°C60-70%1.0-1.2 kPa850-1200Flower finish18.3-22.2°C50-60%1.2-1.4 kPa600-900

DemandTreat light or VPD changes as irrigation changesAfter PPFD, under-canopy light, VPD or CO2 changes, expect a new uptake rate. Hold the steering target steady long enough to observe the new curve before deciding the irrigation program is wrong.UniformityInspect climate spread before steering the rowCompare paired sensors and representative runoff along the 7.6 m run. If front and back diverge, inspect airflow, drain fall, slit geometry and outlet output before steering the whole row around one bad position.

#### Air delivery and thermal scenarios

Calculated exampleRelative air-delivery comparison along a 7.6 metre tableDimensionless model curves compare baseline air movement, one central perforated tube and two perforated tubes.Additional under-canopy airflow along 7.6 mRelative air-delivery index · dimensionless scenario, not measured velocity0.00.40.81.2BaselineOne centre tubeTwo tubesfan end · 0 mfar end · 7.6 mFinal perforations must be site-balanced with static-pressure and traverse measurementsGraph 3. Relative air-delivery scenarios show the intended comparison, not promised performance. Hole diameter and spacing remain site-balanced; verify the installed tube with static pressure and an anemometer traverse.Calculated exampleUnder-canopy electrical input converted to eventual room heat loadA linear conversion from zero to eight hundred watts and zero to two thousand seven hundred thirty British thermal units per hour, plus normalized local temperature-rise scenarios for three air-exchange levels.Under-canopy electrical load becomes room heatExact conversion: BTU/h = watts × 3.412 · local temperature depends on air exchange06821,3652,0472,7300 W200 W400 W600 W800 WBTU/hLocal heat indexlow air · 1.00med · 0.65high · 0.40model envelope800 W = 2,730 BTU/hAir movement redistributes local heat; it does not remove the electrical load from the room.Graph 4. Electrical input is converted directly: 800 W is approximately 2,730 BTU/h. The local heat-index bars are modelled envelopes for low, medium and high under-canopy air exchange—not predicted leaf-temperature changes.

## Troubleshooting

Table 4. Diagnose from the trace and representative runoff before changing a setpoint.SymptomLikely causeFirst actionRunoff high, VWC barely risesChannelling, poor block-slab contact, or emitter placementInspect physically; slow the event or hand-rewet with balanced feed; do not increase volume blindlyRoot-zone EC climbs day over day outside the stage bandToo little leaching, too much dryback, feed mismatch, or excessive demandVerify at equal VWC, check feed EC and climate, then add P2/runoff with one bounded changeRoot-zone EC falls below targetPeak/runoff too high for the steering phaseReduce P2 or peak slightly and observe one full dayP1 never reaches its targetTarget above achievable Vmax, blocked emitter, bad flow assumption, or undersized rampCatch-test, verify Vmax and substrate volume, then adjust the modelFresh transplants stall while the slab stays wetHugo is draining into the slab faster than roots can replace uptakeResume measured bridge shots to the block and inspect roots/contact; do not run the slab sensor as the sole triggerDryback suddenly deepensMissed event or demand change from PPFD, VPD, CO2 or airflowCheck logs and climate first; compensate with P2 only after identifying the causeOne plant wilts while neighbours track normallySingle-emitter failure or local contact problemRestore flow and hand-rescue that block with balanced feed if required

## Combined setpoints

Substrate model3.6 L block + one-third of assumed 11.25 L slab = 7.35 L/plant; confirm the wrapperShot guardrail2-6% = about 147-441 mL; calculate time from total caught flow per plantNormal P1 shot3-5% = about 221-368 mL; normally spaced 15-30 minutes during the rampP0 after lights-on1-5% additional relative dryback, normally 30 minutes to two hoursVegetative runoff8-16%; peak at or slightly above measured field capacityGenerative runoff1-7%; peak at or below measured field capacityController drybackVeg/bulk 10-15 points; setting builds from 15 toward 20-25; finish starts 20-25; all bounded by the recovery floorRoot-zone ECVeg 3-5; flower setting 5-10; bulk 3.5-6; finish 3-4Flower arcGenerative until stretch ends; vegetative bulk until expansion slows; lower EC plus generative dryback to finishDefined finishUse the cited component-change and final clean-water procedure; verify the endpoint from root-zone or runoff EC

The five rulesConvert relative dryback to controller points before programming it.Change from setting to bulk when stretch ends, not because a calendar page turned.Use P2 and runoff as the fast root-zone EC control; keep feed EC as the slower recipe lever.Verify shot duration from actual outlet flow and total assigned substrate volume.Make one bounded change, observe a complete grow-day, then decide again.

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
