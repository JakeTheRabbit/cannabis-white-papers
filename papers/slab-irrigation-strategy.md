---
slug: "slab-irrigation-strategy"
title: "Rockwool Slab Irrigation"
eyebrow: "Water and substrate"
summary: "Rockwool blocks and slabs: substrate volume, emitter flow, drainage, root establishment, P0–P3 irrigation phases and root-zone EC."
track: "Flowering"
read_time: "~18 min read"
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

# Rockwool Slab Irrigation

_Water and substrate · ~18 min read_

> Rockwool blocks and slabs: substrate volume, emitter flow, drainage, root establishment, P0–P3 irrigation phases and root-zone EC.

## Purpose and scope

Calculate water delivery from measured emitter flow. Confirm that water reaches the block, roots reach the slab, and runoff leaves the tray. Use VWC and EC trends to adjust irrigation after those checks.

Vegetative irrigation uses more frequent refilling and less dryback. Generative irrigation uses a shorter irrigation window and more dryback. Athena and CCI describe changing these conditions through crop development; the numerical ranges below are examples from their guidance.[[13]](#ref-13)[[16]](#ref-16)

Changes to irrigationFor routine adjustments, change one irrigation variable and record its effect over a full light–dark cycle. Correct blocked emitters, missed events and acute water stress immediately. Record the action and check the plant response.

## Definitions

Field capacityWater content remaining after a saturated substrate has drained under the specified conditions. In a slab, the measured value depends on substrate properties, geometry, drainage openings and sensor position.Absolute drybackThe difference between peak and trough volumetric water content (VWC), expressed in percentage points. A fall from 70% to 50% VWC is a 20-point dryback.Relative drybackThe VWC decrease divided by the starting VWC, multiplied by 100. A fall from 70% to 42% is 28 percentage points, or 40% of the starting value.P0 / P1 / P2 / P3P0: lights-on to first irrigation. P1: refill. P2: maintenance irrigations. P3: final irrigation to next lights-on. Total dryback between irrigation windows spans P3 and the following P0. Controller terminology varies.Root-zone ECFeed and runoff EC are measured in solution. Bulk EC is measured through the substrate; pore-water EC may be estimated from sensor data. Compare the same measurement method at similar VWC. Units: mS/cm, numerically equal to dS/m.[[18]](#ref-18)RunoffDrain volume divided by applied volume, expressed as a percentage. Catch it from representative plants or slabs in each irrigation zone; do not infer it from pump time.

A fall from 70% to 50% VWC is 20 percentage points, or approximately 28.6% of the starting water content. These values illustrate the calculation. Field capacity requires a separate drainage measurement.Scroll the diagram sideways for full-size labels.

## Slab layout and emitter flow

Runtime = required volume ÷ measured flow. Each 7.6 × 1.2 m table carries three rows of seven slabs, with three plants per slab: 63 plants under seven overhead lights, nine plants per light. Three tables carry 189 plants.

Substrate15 cm (6 in) stone-wool blocks, approximately 3.6 L (0.95 gal), on 1 m (39 in) slabsRoot-zone allocationApproximately 7.35 L (1.9 gal) per plant from a 3.6 L (0.95 gal) block plus one-third of an assumed 11.25 L (3.0 gal) slabDistributionPressure-compensating outlets, short feed tubes and a block-top ring or another catch-tested broad wetting pattern

Side section through a three-plant slab. Substrate remains continuous beneath every block; roots are conceptual. The slab dimensions give 11.25 L. A 150 mm cube is 3.375 L; the calculation uses a separately assumed 3.6 L product volume. Drain openings must follow the selected wrapper/product procedure. [[2]](#ref-2)Scroll the diagram sideways for full-size labels.

Table dimensions and plant countSeven 1 m slabs leave 300 mm at each end of the table. Two air socks run between the three slab rows, each connected to a dedicated 200 mm fan. Under-canopy LEDs run either lengthwise above both socks or crosswise at even intervals. Mount fixtures on independent supports above the fabric. Three 150 mm slab rows plus two assumed 203 mm inflated socks occupy 856 mm of the 1.2 m width, leaving 344 mm for gaps and hardware. Confirm actual inflated diameters, fixture clearances and measured airflow.

Each table has three rows of seven slabs: 63 plants under seven overhead lights, nine plants per light. Two perforated air socks run between the rows, each connected to a dedicated 200 mm fan. Option A uses two lengthwise LED runs above the socks. Option B uses crosswise bars evenly spaced along the table; the seven bars shown illustrate spacing, not a specified fixture count. Both options direct light upward beneath the canopy. Support fixtures independently of the sock fabric and check inflated sock clearance. Seven 1 m slabs leave 300 mm at each end of the 7.6 m table. Dimensions and light bays describe the requested layout; light coverage and airflow require measurements.Scroll the diagram sideways for full-size labels.

#### Emitter configurations and runtime

A shot is one irrigation event. On the assumed 7.35 L allocation, 3% is 220.5 mL and 5% is 367.5 mL. The table uses nominal emitter flow; replace it with collected volume divided by collection time.

Supply passes through the emitter and microtube to a supported distributor at the block. The distributor is schematic; outlet count and dimensions depend on the product. Match the actual ring/stake model, operating pressure and block fit to its documentation; measure the combined output delivered to each plant. [[19]](#ref-19)Scroll the diagram sideways for full-size labels.

Common per-plant emitter configurations. Runtime is rounded to the nearest second.ConfigurationTotal nominal flow3% shot · 221 mL (7.5 fl oz)5% shot · 368 mL (12.4 fl oz)Use and tradeoff1 × 2 L/h2.00 L/h6:3711:02Low-flow single outlet; long events and no emitter redundancy2 × 2 L/h4.00 L/h3:185:31Two outlets where the block-top hardware supports independent wetting points1 × 4 L/h4.00 L/h3:185:31Simple ring-fed layout; the emitter remains a single point of failure2 × 4 L/h8.00 L/h1:392:45Short events; verify pump ramp, pressure regulation and minimum reliable valve time2 × 0.3 GPH2.27 L/h5:509:43Common low-flow imperial pair with useful redundancy and long wetting time2 × 0.5 GPH3.79 L/h3:305:50Common imperial pair close to 4 L/h totalRuntime seconds = shot mL ÷ (total measured L/h × 1000 ÷ 3600). At 4 L/h per plant, 63 plants require 252 L/h per table, or 756 L/h if all three tables irrigate together.

Use labelled graduated vessels or tared weighing cups at representative outlets across the active zone. Compare collections made over the same time at operating pressure. The vessels illustrate collection positions. The runtime uses unrounded 220.5 mL and an assumed 7.35 L allocation; replace both allocation and flow with verified values.Scroll the diagram sideways for full-size labels.

Outlet-flow variationCatch-test outlets near and far from the manifold, at the start and end of the longest active zone. Inspect filters and flush laterals to the emitter manufacturer's specification. For a dry plant among normally hydrated neighbours, check outlet flow, block contact and root condition.

## Water movement between block and slab

A wet slab can sit beneath a dry block. Check the block itself during root establishment.

Water moves through connected rockwool under hydraulic gradients. Upper regions may retain less water after drainage; substrate properties, irrigation and root uptake determine the actual distribution.[[5]](#ref-5)[[6]](#ref-6)[[7]](#ref-7)

Full fibre contact allows exchange between block and slab. Grodan describes slab-induced block drying in its staged-drainage guidance, and also explains that retaining water initially can reduce that effect. The drainage opening changes how much water the slab retains and how the block drains.[[3]](#ref-3)

Block and slab exchange water through their contact face. Under draining conditions the upper media can become drier while the slab remains wet; irrigation and uptake also affect the profile. The profile varies with irrigation and drainage conditions. Grodan describes retained water changing block drying in its staged-drainage method. [[3]](#ref-3)Scroll the diagram sideways for full-size labels.

MT22: insert through the long side beside the middle block, outside its footprint. The 88 mm body runs along the slab; all three 53 mm rods enter across its width at one height. Keep the housing flush and support the cable. The template proposes centreline heights of 37.5 mm for a 75 mm slab and 50 mm for a 100 mm slab, measured from the substrate base. These are comparison positions requiring local validation. [Download the two-page A4 template](assets/slab-sensor/MT22-placement-template-A4-actual-size.pdf). Print at 100% / Actual size and verify both 100 mm scale bars. Transfer pin spacing from the actual sensor. [Open full-size drawing](assets/slab-sensor/mt22-placement.svg) · [TDR-Sensor placement notes](https://github.com/JakeTheRabbit/TDR-Sensor/blob/main/docs/PLACEMENT.md) · [AGPL-3.0 license](assets/slab-sensor/LICENSE).Scroll the diagram sideways for full-size labels.

If the block dries outIf the block dries, check outlet flow, fibre contact and root condition. During rewetting, confirm water enters the block rather than running around it. Check hydration and plant response afterwards.

## Slab saturation and drainage openings

Saturate slabs evenly, establish drainage and seat each block directly on exposed fibre.

1. 1Check the support planeCheck the tray and the intended drain route before placing slabs. Keep the slab support consistent while allowing runoff to reach its collector.
2. 2Saturate and charge togetherSaturate with nutrient solution through the specified openings. Record EC and pH. Grodan’s staged-drainage method specifies a hold of at least 24 hours.[[2]](#ref-2)[[3]](#ref-3)
3. 3Select the drainage procedureGrodan’s staged method first opens the wrapper above the seal for partial drainage, then adds lower openings later. Follow the chosen product procedure for position and timing.[[3]](#ref-3)
4. 4Open the planting positionsFollow the wrapper instructions so each block seats on exposed slab fibre without a plastic bridge under the contact face.[[2]](#ref-2)
5. 5Place and inspect the blocksSeat established blocks with flat fibre contact. Check block hydration and roots before using the selected rooting-in procedure.

## Irrigation after transplanting

Roots initially occupy the transplant block. Irrigation must keep that block hydrated while roots grow into the slab.

The 7.35 L allocation used for runtime calculations includes slab volume that new roots may not yet occupy. Base early irrigation on block hydration and root growth.

1. 1Record the transplant stateRecord block hydration, slab VWC, feed EC, contact and visible roots at transplant.
2. 2Check block hydrationConfirm water reaches the block and wets it evenly. Check the block between events as well as after irrigation.
3. 3Inspect root growthInspect roots at the block–slab interface. Record whether water uptake increases as roots enter the slab.
4. 4Confirm root establishmentUse the established-root daily cycle once roots have entered the slab and measured uptake is repeatable. Confirm delivery and drainage before increasing irrigation.

The same assembly is shown at three establishment stages. Roots are drawn within continuous substrate, with multiple roots appropriate to a clone-based example. Root inspection and water uptake determine when the crop can move to its established irrigation programme.Scroll the diagram sideways for full-size labels.

## P0–P3 irrigation phases

Daily irrigation phases after root establishment.PhasePurposeDescriptionP0Lights-on transpiration before irrigationTrigger the first irrigation from measured water loss and block hydration, within the crop’s established minimum VWC.P1Refill without channellingThe example programme uses 2–6% substrate-volume events, commonly 3–5%, spaced 15–30 minutes apart. These are guidance ranges requiring local validation.P2Maintain VWC and steer root-zone ECReplace water lost during the light period. Drainage removes dissolved salts; measure EC and runoff to assess the response.P3Final irrigation to next lights-onDryback begins after the final event, often before lights-off. Here P3 ends at the next lights-on.

A constructed 24-hour example with a 12-hour light period. P0 is lights-on to first irrigation; P1 refills; P2 maintains; P3 runs from the final event to the next lights-on. Total between-irrigation dryback spans P3 plus the following P0. Values and timings are illustrative.Scroll the diagram sideways for full-size labels.

Plot VWC, irrigation events and EC on the same time axis. Label the EC method and record sensor position, calibration and crop stage.[[18]](#ref-18)

## Irrigation by growth stage

These example ranges combine Athena and CCI guidance. Match EC methods before comparing values; establish a minimum VWC for the crop and substrate before using dryback targets.[[13]](#ref-13)[[16]](#ref-16)

Example ranges for established plants in rockwool. Dryback is expressed in VWC percentage points. EC comparisons require the same measurement method.StageSteerPeak and runoffController drybackRoot-zone EC (mS/cm; method-specific)Switch signalEstablished vegVegetativeAt/above measured field capacity; 8-16% runoff10-15 points3-5Roots established, repeatable uptake, plant ready to flipFlower setting, nominal days 1-21GenerativeAt/below field capacity; 1-7% runoffStart near 15 points and move toward 20-25 over the first three weeks; never cross the locally established minimum VWC5-10Vertical stretch has clearly slowed or stoppedFlower bulk, nominal days 22-42VegetativeAt/above field capacity; 8-16% runoff10-15 points3.5-6Flower expansion slows and ripening signals dominateFinish, normally final 10-14 daysLower EC plus generative drybackAt/below field capacity; 1-7% unless correcting excess EC20-25 points initially; extend only from cultivar data and stay above that minimum3-4Cultivar-specific maturity observationsDays are approximate. Record stretch, flower expansion and maturity to identify stage changes.

## Three-plant slab measurements

Sipkoi describes collecting irrigation and runoff from a complete three-plant slab in We The Growers, episode 31. Dividing by three gives an average per plant; it cannot identify an individual blocked emitter.[[15]](#ref-15)

Three blocks sit on one slab supported above a runoff tray. Gold shows the complete drain path to a graduated collector; blue shows feed tubing. Slit positions depend on the product and drainage procedure. Capture all relevant drainage without allowing the slab to sit in standing runoff. Dividing slab totals by three gives an average, not individual plant measurements. [[15]](#ref-15)Scroll the diagram sideways for full-size labels.

Reported schedule, specific to that facilityPlants move from 10 × 10 × 6.4 cm (4 × 4 × 2.5 in) blocks onto pre-saturated slabs after about 16 days of veg. One whole slab is raised over a runoff tray; applied and drained volume are divided by its three plants. Staff report daily in/out volume and check runoff pH and EC once or twice weekly.For the first 48 hours on slabs, the reported starting program is about 12 lights-on events, two minutes each through a 1.9 L/h (0.5 GPH) outlet. The grower then allows a three-to-four-day period without irrigation before building toward full irrigation. Around day 14, a typical reported pattern is 10-12 four-minute events, with frequency adjusted to cultivar demand and observed drainage.

Podcast timestamps: slab placement 27:33-28:12; slab-scale runoff collection 31:43-32:33; initial flower irrigation 39:44-41:12; first-three-week adjustment 48:55-53:37.[[15]](#ref-15)

## Root-zone EC and preharvest nutrition

Check measurement method and water delivery before correcting high EC. Keep preharvest product schedules separate from salt-accumulation diagnosis.

1. 1Check the EC measurementIdentify feed, runoff, bulk substrate or estimated pore-water EC. Check calibration and probe contact; compare substrate readings at similar VWC.[[18]](#ref-18)
2. 2Salt accumulationIf comparable readings keep rising, measure feed EC, delivered volume and collected drainage. Leaching removes dissolved salts. After adjusting feed or irrigation, check the next runoff and substrate readings.
3. 3Athena Fade programmeAthena’s nine-week example replaces Pro Core with Fade in weeks 8 and 9 while continuing Pro Bloom. It specifies maintaining feed EC and checking pH after the substitution. This is a procedure for those products; the document does not establish a general requirement for rockwool-grown cannabis.[[17]](#ref-17)
4. 4Athena’s final irrigation stepThe same document specifies Cleanse in reverse-osmosis water for the final day in rockwool, with EC checks to assess the result. This product procedure alone does not demonstrate that preharvest flushing improves flower quality.[[17]](#ref-17)

## Climate and water uptake

Light, temperature, humidity and air movement affect transpiration. After a climate or lighting change, compare the rate of VWC decline, irrigation volume and runoff with the previous conditions. Measure at the near, middle and far ends of the table. If one area dries faster, check local climate and emitter delivery before changing the whole zone.

#### Plant clearance and early skirting

For the under-canopy layout shown here, plants must be tall enough to keep retained foliage and branches clear of the bars and their mounts. Skirt or lollipop early: remove low growth that would contact fixtures, obstruct the air socks or crowd the space below the retained canopy. Keep productive foliage above the lights. Recheck clearance as branches spread and flowers gain weight; use the fixture manufacturer’s minimum crop clearance.

Foliage pressed against fixtures or exposed at very short distance can suffer local heat or light injury. Crowded lower growth also obstructs airflow and inspection. If plants cannot clear the bars, delay their use or reposition them.

#### Redistributing light between top and bottom

Under-canopy lighting can be used to redistribute part of the lighting input from above to below. Reduce the top-light setting in steps while measuring illumination through the crop. Equal electrical watts maintain the same lighting power budget, but do not guarantee equal photon output or crop response: fixture efficacy, spectrum and interception differ.

PPFD is measured at a surface and in a direction. A reading below the canopy cannot simply be subtracted from a reading above it. Map upper, middle and lower foliage with consistent sensor positions and orientations, and account for photoperiod. Cannabis studies of supplemental subcanopy lighting do not establish a universal one-for-one replacement for top light.[[20]](#ref-20)

#### Heat and root-zone temperature

Adding lighting power increases the heat that the room must remove. Reducing top-light watts by the same amount can keep total lighting power similar, while moving heat closer to the slabs. Air socks redistribute heat; cooling or exhaust must remove it. Keep fixtures off the slab wrappers and provide airflow around the bars without blocking their cooling surfaces.

Log temperature inside representative rooted slabs, including positions closest to the bars and cooler comparison positions. Record lower-canopy air and leaf temperatures as well; a room sensor above the crop can miss a hot spot below it. Compare the full lights-on temperature trend before and after each lighting change, alongside VWC, EC and runoff.

Excess root-zone heat increases root and microbial oxygen demand while warm water holds less dissolved oxygen. In rockwool, oxygen supply also depends on air-filled pores and drainage. Warm, persistently wet slabs can therefore leave roots oxygen-limited. Water and nutrient uptake can decline, causing wilting despite wet substrate, poor growth and loss of yield. Warm conditions can favour some Pythium species when the pathogen is present; heat alone does not create an infection.[[21]](#ref-21)

If slab temperature exceeds the crop’s established limit, or plants show injury after the lighting change, dim or switch off the under-canopy bars and check cooling, clearance, airflow and drainage. Inspect roots and confirm recovery. Adding irrigation without checking the cause can worsen oxygen limitation in an already wet slab.

## Irrigation faults

Irrigation symptoms, possible causes and checks.SymptomPossible causesFirst actionRunoff high, VWC barely risesChannelling, poor block-slab contact, or emitter placementInspect physically; slow the event or hand-rewet with balanced feed; do not increase volume blindlyRoot-zone EC climbs day over day outside the stage bandToo little leaching, too much dryback, feed mismatch, or excessive demandVerify at equal VWC, check feed EC and climate, then add P2/runoff with one recorded adjustmentRoot-zone EC falls below targetPeak/runoff too high for the steering phaseReduce P2 or peak slightly and observe one full dayP1 never reaches its targetTarget set above the peak VWC this slab can actually reach, blocked emitter, wrong flow assumption, or too few ramp eventsCatch-test, confirm the achievable peak VWC and the substrate volume, then adjust the modelFresh transplants stall while the slab stays wetInadequate block hydration, poor contact, delivery failure or impaired rootsInspect the block, roots, contact and caught outlet flow; do not use the slab sensor as the sole triggerDryback suddenly deepensMissed event or demand change from PPFD, VPD, CO2 or airflowCheck logs and climate first; compensate with P2 only after identifying the causeOne plant wilts while neighbours track normallySingle-emitter failure or local contact problemRestore flow and water that block manually with balanced feed if required

## Daily irrigation record

Record values by irrigation zone and sampling position.RecordIncludeCrop and substrateCultivar, growth stage, block/slab product and dimensions, plants per slabWater deliveryCaught flow per plant, event duration, event count, first and last irrigationWater contentPeak and pre-irrigation VWC, dryback in percentage points, sensor positionDrainageApplied and drained volume from the same slab over the same interval; runoff percentageEC and pHFeed and runoff results; substrate EC method, VWC and sampling timeUnder-canopy lightingTop and lower fixture settings and watts, PPFD sampling position/orientation, slab temperature near bars and at comparison positions, leaf temperature and clearanceChanges and faultsMissed events, blocked outlets, manual watering, climate changes, corrective action and subsequent response

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

Subcanopy and Inter-Canopy Supplemental Light Enhances and Standardizes Yields in Medicinal Cannabis (Cannabis sativa L.). Plants 14(10):1469 (2025). [Research paper](https://doi.org/10.3390/plants14101469)

Sutton JC et al. (2006). Etiology and epidemiology of Pythium root rot in hydroponic crops: current knowledge and perspectives. Summa Phytopathologica 32(4). Evidence from hydroponic crops; not a cannabis-specific temperature threshold. [Research review](https://doi.org/10.1590/S0100-54052006000400001)


