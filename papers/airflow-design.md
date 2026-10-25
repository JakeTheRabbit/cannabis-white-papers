---
slug: "airflow-design"
title: "Airflow design for indoor cultivation"
eyebrow: "Basic · Airflow design"
summary: "Each leaf has a layer of still air that decreases the rate of gas exchange. Airflow removes this layer. After you read this paper, you will know how much air to move and which fans supply the air. You will also know where to put the fans, to give each leaf a light airflow."
track: "Environment and climate"
read_time: "~29 min to read"
diagrams: "8 diagrams · 8 photos"
related: ["grow-room-systems", "mould-risk", "coco-crop-steering"]
url: "https://www.growlabs.nz/wiki/airflow-design.html"
md_url: "https://www.growlabs.nz/wiki/papers/airflow-design.md"
version: "1.2"
updated: "2026-07-18"
license: "CC BY-NC 4.0"
license_url: "https://creativecommons.org/licenses/by-nc/4.0/"
attribution: "The Cannabis White Papers"
refs: [{"id": "schuepp1993-bl", "n": 1, "cite": "Schuepp PH (1993). Tansley Review No. 59: Leaf boundary layers. New Phytologist 125(3):477-507.", "url": "https://doi.org/10.1111/j.1469-8137.1993.tb03898.x", "peer": true}, {"id": "dupont2025-wind", "n": 2, "cite": "Dupont K, van den Berg TE, Zhang J, Moene AF, Vialet-Chabrand SRM (2025). Beyond the boundary: a new road to improve photosynthesis via wind. J. Exp. Bot. 76(20):5791-5813.", "url": "https://doi.org/10.1093/jxb/eraf325", "peer": true}, {"id": "kitaya2004-airvel", "n": 3, "cite": "Kitaya Y, Shibuya T, Yoshida M, Kiyota M (2004). Effects of air velocity on photosynthesis of plant canopies under elevated CO2 levels. Adv. Space Res. 34(7):1466-1469.", "url": "https://doi.org/10.1016/j.asr.2003.08.031", "peer": true}, {"id": "tjosvold2018-air", "n": 4, "cite": "Tjosvold SA (2018). Maximize photosynthesis with moving air. UC ANR Greenhouse & Floriculture (extension article).", "url": "https://ucanr.edu/blogs/blogcore/postdetail.cfm?postnum=28455", "peer": false}, {"id": "rm2021-light", "n": 5, "cite": "Rodriguez-Morrison V, Llewellyn D, Zheng Y (2021). Cannabis yield, potency, and leaf photosynthesis respond differently to increasing light levels in an indoor environment. Front. Plant Sci. 12:646020.", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8144505/", "peer": true}, {"id": "kitaya2010-circ", "n": 6, "cite": "Kitaya Y, Tsuruyama J, Shibuya T, Yoshida M, Kiyota M (2010). CO2 and air circulation effects on photosynthesis and transpiration of tomato seedlings. Scientia Horticulturae 126(2):326-330.", "url": "https://www.sciencedirect.com/science/article/abs/pii/S0304423810003316", "peer": true}, {"id": "gilliham2011-ca", "n": 7, "cite": "Gilliham M, et al. (2011). Calcium delivery and storage in plant leaves: exploring the link with water flow. J. Exp. Bot. 62(7):2233-2250.", "url": "https://doi.org/10.1093/jxb/err111", "peer": true}, {"id": "chehab2009-thigmo", "n": 8, "cite": "Chehab EW, Eich E, Braam J (2009). Thigmomorphogenesis: a complex plant response to mechano-stimulation. J. Exp. Bot. 60(1):43-56.", "url": "https://doi.org/10.1093/jxb/ern315", "peer": true}, {"id": "chandra2008-photo", "n": 9, "cite": "Chandra S, Lata H, Khan IA, ElSohly MA (2008). Photosynthetic response of Cannabis sativa L. to variations in photosynthetic photon flux densities, temperature and CO2 conditions. Physiol. Mol. Biol. Plants 14(4):299-306.", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3550641/", "peer": true}, {"id": "pipp2026-airflow", "n": 10, "cite": "Anderson K (2026). What cannabis growers can finally learn about airflow. Pipp Horticulture — controlled flower-room trials with Dr. Allison Justice and the Cannabis Research Coalition. (Preliminary: one replicate reported, second underway.)", "url": "https://pipphorticulture.com/what-cannabis-growers-can-finally-learn-about-airflow/", "peer": false}, {"id": "bartok-haf", "n": 11, "cite": "Bartok JW, Grubinger V. Horizontal air flow is best for greenhouse air circulation. UMass Extension Greenhouse & Floriculture / eXtension Farm Energy (extension fact sheet).", "url": "https://farm-energy.extension.org/horizontal-air-flow-is-best-for-greenhouse-air-circulation/", "peer": false}, {"id": "uconn-haf", "n": 12, "cite": "University of Connecticut Integrated Pest Management. Horizontal air flow systems. UConn CAHNR (extension fact sheet).", "url": "https://ipm.cahnr.uconn.edu/horizontal-air-flow-systems/", "peer": false}, {"id": "goto1992-tipburn", "n": 13, "cite": "Goto E, Takakura T (1992). Prevention of lettuce tipburn by supplying air to inner leaves. Transactions of the ASAE 35(2):641-645.", "url": "https://doi.org/10.13031/2013.28644", "peer": true}, {"id": "ahmed2020-multifan", "n": 14, "cite": "Ahmed HA, Tong YX, Yang QC (2020). Lettuce plant growth and tipburn occurrence as affected by airflow using a multi-fan system in a plant factory with artificial light. J. Thermal Biology 88:102496.", "url": "https://doi.org/10.1016/j.jtherbio.2019.102496", "peer": true}, {"id": "moosavi2025-vaf", "n": 15, "cite": "Moosavi-Nezhad M, Meng Q (2025). A calcium-mobilizing biostimulant provides tipburn control comparable to vertical airflow fans in greenhouse hydroponic lettuce 'Rex'. Front. Plant Sci. 16:1701667.", "url": "https://doi.org/10.3389/fpls.2025.1701667", "peer": true}, {"id": "perfduct2025", "n": 16, "cite": "Wang C, Fu J, Zhang Q, Sheng B, He F, Zhang G, Ding X, Cao N (2025). Optimizing perforated duct systems for energy-efficient ventilation in semi-closed greenhouses through process regulation. Processes (MDPI) 13(7):2253.", "url": "https://doi.org/10.3390/pr13072253", "peer": true}, {"id": "amca-fanlaws", "n": 17, "cite": "Air Movement and Control Association International (AMCA). Fan laws (affinity laws): airflow varies with fan speed, pressure with the square of speed, shaft power with the cube of speed. Standard fan-engineering relationship.", "url": "https://www.amca.org/", "peer": false}, {"id": "vas-inrack", "n": 18, "cite": "Vertical Air Solutions / Pipp Horticulture. In-rack airflow systems for vertical cannabis racking (manufacturer documentation).", "url": "https://pipphorticulture.com/in-rack-airflow-systems/", "peer": false}, {"id": "cockson2019-nutr", "n": 19, "cite": "Cockson P, Landis H, Smith T, Hicks K, Whipker BE (2019). Characterization of nutrient disorders of Cannabis sativa. Applied Sciences (MDPI) 9(20):4432.", "url": "https://doi.org/10.3390/app9204432", "peer": true}, {"id": "llewellyn2023-def", "n": 20, "cite": "Llewellyn D, Golem S, et al. (2023). Foliar symptomology, nutrient content, yield, and secondary metabolite variability of cannabis grown hydroponically with different single-element nutrient deficiencies. Plants (MDPI) 12(3):422.", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9920212/", "peer": true}, {"id": "cbt-marginburn", "n": 21, "cite": "Feel the (cannabis leaf margin) burn. Cannabis Business Times, Cultivation Matters column (trade article): leaf margin burn from high EC, drought, potassium and calcium deficiency.", "url": "https://www.cannabisbusinesstimes.com/columns/cultivation-matters/news/15750558/feel-the-cannabis-leaf-margin-burn", "peer": false}, {"id": "nelson2015-leaftemp", "n": 22, "cite": "Nelson JA, Bugbee B (2015). Analysis of environmental effects on leaf temperature under sunlight, high pressure sodium and light emitting diodes. PLoS ONE 10(10):e0138930 (well-watered leaves typically within ~2 °C of air; LED canopies ~1.3 °C cooler than HPS at equal photon flux; water-stressed leaves modelled 6-12 °C above air).", "url": "https://doi.org/10.1371/journal.pone.0138930", "peer": true}, {"id": "dupont2026-lowwind", "n": 23, "cite": "Dupont K, Frati R, Vialet-Chabrand SRM (2026). Low wind, high impact: sustained low airflow alters water use efficiency and shapes plant acclimation. J. Exp. Bot. 77(16):5225-5243. (Lettuce, 0.22 vs 0.65 m/s.)", "url": "https://academic.oup.com/jxb/article/77/16/5225/8656750", "peer": true}, {"id": "zhang2016-cfd", "n": 24, "cite": "Zhang Y, Kacira M, An L (2016). A CFD study on improving air flow uniformity in indoor plant factory system. Biosystems Engineering 147:193-205.", "url": "https://www.researchgate.net/publication/302972809_A_CFD_study_on_improving_air_flow_uniformity_in_indoor_plant_factory_system", "peer": true}, {"id": "ashrae2023-roomair", "n": 25, "cite": "ASHRAE (2023). Room air distribution. ASHRAE Handbook: HVAC Applications, Chapter 58 (fully mixed, stratified and partially mixed systems; supply airflow and supply-return temperature difference).", "url": "https://handbook.ashrae.org/Handbooks/A23/IP/A23_Ch58/a23_ch58_ip.aspx", "peer": false}, {"id": "rii2022-hvac", "n": 26, "cite": "Resource Innovation Institute (2022). HVAC Best Practices Guide for controlled environment agriculture (USDA NRCS funded): airflow at crop level, fan motors as internal sensible heat, canopy-level sensing.", "url": "https://resourceinnovation.org/wp-content/uploads/2022/06/RII-HvacBPG-2022-v4-1.pdf", "peer": false}, {"id": "quest-airflow", "n": 27, "cite": "How to ensure proper airflow at your indoor cannabis cultivation facility (G. Brown, Quest). Cannabis Business Times (sponsored trade article).", "url": "https://www.cannabisbusinesstimes.com/article/how-to-ensure-proper-airflow-indoor-cannabis-cultivation-quest/", "peer": false}, {"id": "vostermans-vflo", "n": 28, "cite": "Vostermans Ventilation. Multifan V-FloFan vertical circulation fan (manufacturer documentation): moving lamp heat from the greenhouse ridge down to the crop.", "url": "https://www.vostermans.com/ventilation/axial-fans/v-flofan", "peer": false}, {"id": "tmu2026-vfarm", "n": 29, "cite": "Optimization of thermal performance and microclimate in vertical farms using computational fluid dynamics (2026). ICTEA proceedings, Toronto Metropolitan University. (CFD validated on a two-tier raspberry prototype.)", "url": "https://journals.library.torontomu.ca/index.php/ictea/article/view/2869", "peer": false}]
---

# Airflow design for indoor cultivation

_Basic · Airflow design · ~29 min to read_

> Each leaf has a layer of still air that decreases the rate of gas exchange. Airflow removes this layer. After you read this paper, you will know how much air to move and which fans supply the air. You will also know where to put the fans, to give each leaf a light airflow.

## Purpose and scope

Airflow keeps the gases at the leaf in movement. This paper shows the effect of airflow, how much airflow is necessary, which fans supply it, and where to put the fans. Thus each part of the canopy has a light airflow. The parts include the inner leaves in the middle of the canopy, where bud rot starts.

This paper starts with the basic facts. It shows the effect of air movement at the leaf and how much airflow you want. It also shows which fans make this airflow, how to compare the fans, and where to hang them.

## Definitions

**Boundary layer**: The thin layer of still air on the surface of each leaf. Gases must go across this layer by diffusion, and diffusion is slow. Thus the layer decreases the rate of gas exchange. Airflow makes the layer thinner.

**Air velocity**: The speed of the air at the canopy, in meters for each second (m/s). The air velocity is the value that is important for the plant. The size of the fan is not important.

**Laminar and turbulent airflow**: Laminar airflow is smooth airflow that moves in layers (for example, a stable jet of air). Turbulent airflow is airflow in which the air changes direction frequently and mixes. Turbulent airflow is better for leaves.

**Transpiration**: In transpiration, the plant absorbs water at the roots and releases the water as vapor through pores on the leaves. When the air is drier and the air temperature is higher, the water leaves the plant more quickly. Moving air makes transpiration faster because it removes the moist air near the leaf. If a layer of moist air stays on the leaf, the rate of transpiration decreases. Airflow removes this layer.

**Air exchange**: The replacement of the room air with external air (intake and exhaust). Air exchange is different from recirculation. Recirculation only mixes the air that is in the room.

**HAF / VAF**: The two primary types of fan that hang. A **HAF** (horizontal airflow) fan hangs above the crop and blows air to the side. Thus it makes a loop of air around the room. A **VAF** (vertical airflow) fan hangs above the crop and blows air straight down through the crop.

**CFM and FPM**: CFM and FPM are two different values. Some persons think that they are the same. **CFM** (cubic feet for each minute) is the _volume_ of air that a fan moves, and the supplier of the fan gives this value. **FPM** (feet for each minute) is the _speed_ of the air at a leaf, and this speed is important for the plant. 1 m/s is approximately 200 FPM.

**Throw and entrainment**: **Throw** is the distance from the fan to the point where the jet has the same speed as the air in the room. **Entrainment** is not easy to see. In entrainment, the jet pulls the still air of the room along with it. Thus a small fan can move much more air than its blades push. HAF loops operate because of entrainment.

## Leaf boundary layers

The air on the surface of a leaf almost does not move. Thus a thin layer of still air with high humidity stays on the leaf. The air in this layer almost does not mix with the air in the room. This layer is the **boundary layer**.CO2 must go into the leaf, and water vapor and heat must go out of the leaf. They must go across the boundary layer by diffusion, which is slow. When the boundary layer is thicker, they move more slowly[^schuepp1993-bl].

> **Diagram.** Still air decreases the rate of movement of gases and heat into and out of the leaf. Moving air makes the boundary layer thinner. Thus CO2 moves into the leaf more quickly, and water and heat move out of the leaf more quickly[^dupont2025-wind].

Moving air makes the boundary layer thinner. A small airflow has an important effect. Tests show that an added air velocity of less than approximately 0.2 m/s increases the photosynthesis in the day by 10 to 20%[^dupont2025-wind]. Thus fans are necessary in a grow room.

## Airflow targets

More airflow helps, but the effect becomes much smaller each time that the airflow increases. When the airflow increases from still air to a light airflow, photosynthesis increases quickly. After this, the curve is flat. Most of the effect occurs when the leaves move a small distance[^kitaya2004-airvel].

> **Diagram.** Gas exchange increases quickly and then becomes flat[^kitaya2004-airvel]. The target is a **light, constant airflow**. At this target, the leaves move a small distance. They do not shake.

> **Diagram.** When the air velocity is less than approximately 0.2 m/s, disease can start in areas with still air and high humidity. When the velocity is more than approximately 1.2 m/s, there is a risk of wind damage, and the plants can become dry. Select a velocity in the middle of this range.[^tjosvold2018-air]

## Airflow and light intensity

When the light is brighter, the leaf must have more air. High light intensity causes a high rate of photosynthesis and a high rate of transpiration. These two rates are high only if the boundary layer is thin. The yield of cannabis continues to increase when the light increases, to very high values[^rm2021-light]. But this occurs only if the airflow and the climate control also increase. A bright room that has weak airflow cannot use all the light.

> **KEY: Airflow must agree with the other conditions in the room**
>
> Light, CO2, temperature, humidity and airflow have an effect on each other (refer to the [systems guide](grow-room-systems.html)). If you increase the light and do not increase the airflow, the leaves become hot and stay in the boundary layer of moist air[^chandra2008-photo].

## Airflow, transpiration and nutrient uptake

When the boundary layer is thinner, CO2 moves into the leaf more quickly and water moves out of the leaf more quickly. More airflow causes more transpiration. Thus the plant must have more water and more nutrient at the roots. Two effects are important:

- **Calcium tipburn:** Calcium moves into the leaf in the transpiration stream. Thus the uptake of calcium changes with the flow of water[^gilliham2011-ca]. If the airflow is very high and the feed is too low, calcium deficiency causes tipburn. Tipburn occurs also when the tank contains a large quantity of calcium. To correct this, make the feed agree with the airflow. Do not make the airflow agree with the feed.
- **Stronger plants (a good effect).** Air movement is a mechanical signal. When a plant has a light airflow, it makes stems that are shorter, thicker and stronger. This effect is thigmomorphogenesis[^chehab2009-thigmo]. A plant that has good airflow can hold heavy colas without stakes.

> **NOTE: Calcium and still air**
>
> Calcium moves to the leaves in the transpiration stream, and it almost does not move out of a leaf again[^gilliham2011-ca]. Thus a leaf that transpires slowly gets little calcium. A leaf in a dead zone _in_ a dense canopy is an example.
> In cannabis, the position of calcium deficiency symptoms is not always the same. In young plants, the growth tips and the leaves that expand were stunted and distorted[^cockson2019-nutr]. But in a test with flowering cannabis, the first spots were on the _lower_ fan leaves in week three. Then the symptoms moved up the plant, to the edges and tips of the upper leaves[^llewellyn2023-def]. Thus the position of the symptom alone does not identify calcium deficiency in flower.
> Burnt tips and edges also come from a high EC (salt), from drought stress and from potassium deficiency[^cbt-marginburn]. Before you change the fans or the feed, do a leaf tissue test, and examine the EC and the irrigation records.
> Most data for this mechanism come from lettuce. Air that goes directly to the closed inner leaves of a lettuce head stops calcium tipburn[^goto1992-tipburn][^ahmed2020-multifan][^moosavi2025-vaf]. A cannabis plant does not have a closed head. Thus these data support the mechanism, but they do not show the size of the effect in cannabis or which fan type is best. No cannabis study has tested this.

## Airflow system functions and equipment

The instruction “Add a fan” includes three different tasks. In a first room, the most frequent airflow problem is a fan that is incorrect for the task that you have:

**Recirculation (to mix the air)**

Move the air that is in the room. Thus each leaf has a light airflow and no dead zones occur. A dead zone is an area where the air does not move and the humidity is high. This task is for the boundary layer[^kitaya2010-circ]. Most of this paper is about this task.

**Air exchange (in and out)**

Replace the room air with external air. The room air has high humidity and a low CO2 concentration. You can also push the room air through a carbon filter. Inline duct fans and wall exhaust fans do this task. Air exchange removes water from the room, but it has almost no effect on the leaf.

**Conditioning (heating, cooling, drying)**

An air conditioner, a dehumidifier or an air handling unit (AHU) changes the temperature and the moisture of the air. The unit must supply this conditioned air to the correct positions in the room. This supply of the air to all positions is a different problem.

> **WARN: Prevent dead zones**
>
> Put the fans where they push air _through_ the canopy, not only along its top. Defoliate the plants until air can go into the canopy. Air goes where the resistance is low. It does not go into corners, the bottom of the canopy or the inner part of a dense canopy. Bud rot starts in these dead zones, where the air does not move and the humidity is high.

## Turbulent airflow and canopy mixing

Do not point one large fan straight along a row. A jet of laminar airflow makes a thick boundary layer on each surface that it touches. The air that is not on the axis of the jet does not move. **Turbulent airflow** comes from many fans that point in different directions, with oscillation. It changes the boundary layer on each leaf from all directions at all times. Turbulent airflow makes the boundary layer thinner more than other types of airflow[^schuepp1993-bl][^dupont2025-wind].

> **TIP: The leaf movement test**
>
> Walk through the room. Examine each leaf, from the top to the bottom and in the plants. Each leaf must move a small distance. A leaf that does not move is in a dead zone. Supply air to this area. If a leaf shakes strongly, decrease the speed of that fan.

## Data from tests in controlled rooms

The sections above are about the physiology of the leaf. This section shows if airflow changes the yield in a flower room. Pipp Horticulture, with Dr. Allison Justice and the Cannabis Research Coalition, did a controlled test in three flower rooms that were the same. The VPD, the temperature and the humidity were constant in all the rooms. Only the airflow was different[^pipp2026-airflow].

The three rooms had different supplied air speeds. The test gives these values in feet for each minute (FPM), a frequent unit in commercial horticulture. The values that the test compared were approximately 0.5, 1.0 and 2.0 m/s (approximately 100, 200 and 400 FPM). The test gave one clear result:

> **Diagram.** The effect was a **threshold and not a continuous change**. When the speed was less than approximately 1.0 m/s (approximately 200 FPM), the crop almost did not change. When the speed was more than this, the yield, the plant shape and the uniformity became better together[^pipp2026-airflow].

It is possible to think that this result does not agree with the flat curve at the leaf in Figure 2. But the two agree. Figure 2 gives the air velocity at one _leaf_. The FPM here is the air speed that the room _supplies_ in total.The speed of the air decreases when the air goes into the canopy. Thus the room must supply an air speed of much more than 1 m/s at the fans. This air speed gives the bottom leaves and the inner leaves the light airflow in Figure 3. A supplied air speed of approximately 1.0 m/s (approximately 200 FPM) is approximately the value that gives _each_ leaf an air velocity in the target range. It gives this velocity not only to the leaves on the external side of the canopy.

The rooms with an airflow more than this threshold showed three effects:

- **More flower and less larf.** The stems had less biomass, and the plant used more of its energy for the bud. The trim was approximately 42% in the plants with still air, and it was much lower with good airflow. Thus less of the harvest became larf[^pipp2026-airflow].
- **Less stress.** The plants with still air had stems with more red color and more anthocyanin. Anthocyanin is a sign of stress that you can see. The plants with good airflow had a higher uniformity and less stress.
- **More height, not weaker plants.** At the end, plants with higher airflow had a height approximately 15 cm (6 in) more than the control plants with still air. Most of the vertical growth occurred before the end of week three, and the plants put _less_ into the stem. This difference of height is an effect of less stress from still air. A stronger airflow that goes straight at the plants has a mechanical effect: it makes the plants shorter (refer to section 06).

> **KEY: The primary result: uniformity**
>
> The personnel who did the test controlled the room very accurately, but they found a difference of position. The first 30 to 60 cm (1 to 2 ft) of each row was different from the remaining part of the row. Their important result is this: **“if airflow is not uniform, neither is your crop.”** The dead zone problem from section 07 is the same problem, and the test measured it. It is more important to make sure that no leaf stays in still air than to get a high fan speed on average.

> **NOTE: The strength of this result**
>
> Think of this result as strong first data from a flower room. At this time, the result is not sure. The data are from one replicate. A second test is in progress, to make the statistics stronger[^pipp2026-airflow]. The direction of the result agrees with the physiology of the leaf in the other sections of this paper.

## Fan types

Fans are not the same. Each type makes a different _shape_ of airflow, and the shape controls which leaves get air. Select a fan for the shape of airflow that you want. Do not select a fan for its cost or for its CFM value.

A photo of each type Grok ImagineHAF fanVAF fanOscillating fanClip fanDrum / floor fanUnder-canopy fanAir sockInline duct fan

> **Diagram.** The eight types of fan in a grow room, shown from the side with the air that each type makes. The first six are equipment for recirculation. The air sock is a method to supply air. The inline duct fan is for air exchange and not for circulation.

**HAF, horizontal airflow fan**

A HAF fan is a basket fan that hangs above head height and points to the side along the room. Typically, the blade is 300 to 500 mm (12 to 20 in) and the motor is small (1/10 to 1/15 hp)[^bartok-haf]. Some HAF fans together make one slow **racetrack loop**: the air goes along one side of the room and back along the other side. The jet of each fan pulls the still air around it along with it (entrainment). Thus a small fan moves a large volume of air.
**Where:** above the canopy, at a quarter of the room width from the wall. **The problem:** the air of the fan goes _along_ the top of the crop. In a dense canopy, it does not go to the middle.

**VAF, vertical airflow fan**

A VAF fan hangs above the canopy and blows air **straight down through the canopy**. Usually, it has a wide diffuser on top. Thus it gets air from a large area and supplies a wide flow of air, and not a jet with a small width. The VAF fan is the only type of fan that always supplies air to the leaves in the inner part of a plant.
**Where:** above the canopy in a grid. Put the fans at a distance that gives an overlap of their flows of air. **The problem:** each fan has a higher cost and makes shade. Put the fan in a position where its shade is not on the crop. Also, the fan takes in the warm air from the level of the lights and pushes it into the canopy. In a sealed room that you cool, this adds heat to the canopy (refer to “Top-down fans and heat” in section 11).

**Oscillating fan (wall or pole)**

The oscillating fan is the usual fan for a grow room: a head on a bracket that oscillates. It has a low cost and it is easy to find. It is good in a small room, because the head oscillates and thus gives the turbulent airflow that section 08 recommends.
**Where:** on a wall or a pole, pointed to _mix_ the air in the room. Do not point it straight at the plants. **The problem:** its air goes to one part of the room at a time. Each leaf gets air for only a part of each movement of the head. Thus a large number of fans is necessary to keep a constant airflow in a large room.

**Clip fan**

A clip fan is a very small oscillating fan on a clamp. The clamp attaches to the pole or the frame of a tent. The fan moves approximately the quantity of air for one plant.
**Where:** in tents and in setups for one plant only. **The problem:** a clip fan does not operate correctly in a larger canopy. When the canopy is more than approximately 2 m² (22 ft²), clip fans are not a good selection. You get six clip fans that do the task of one hung fan, with a higher total power and a worse uniformity.

**Drum / pedestal floor fan**

A drum or pedestal floor fan has a large head with high power on a stand. The jet has a small width, the speed of the air is very high, and the fan makes much noise.
**Where:** for a short time only, to remove a dead zone in a corner or to dry a room quickly after water spills. **The problem:** it is the most frequent cause of wind damage. The plants on the axis of the fan get a very strong airflow, and the plants that are not on the axis get no airflow. Do not use these fans as the primary source of the airflow in a room.

**Under-canopy fan**

An under-canopy fan is a flat, wide fan at the level of the pots. It blows air across the floor and up into the bottom of the plants. The zone below the canopy has the most water and the minimum air movement in the room. Cool air moves down, the pots and the floors release water vapor into this zone, and no fan above the canopy supplies air to it.
**Where:** at the level of the floor or the bench. Point the fan along the rows. **The problem:** there is almost none, and thus this fan gives a very good result for its cost. Keep the fan away from irrigation pipes. Make sure that the intake is clear of leaves on the floor.

**Air sock (tube with holes)**

An air sock is a long tube of fabric or plastic. A fan or an air handler supplies air to the tube. The air flows out through many small holes along the full length of the tube. Because the holes are small and many, the air supply along the tube is very equal, with no strong jet at one point. An investigation of this system gives approximate target values: holes of 6 to 10 mm with a spacing of 30 to 70 mm. The fan keeps a static pressure of approximately 30 to 40 Pa, and thus the tube stays inflated and circular[^perfduct2025].
**Where:** along the length of a row, above or below the bench. An air sock is the standard method to supply _conditioned_ air from an air conditioner or a dehumidifier. It prevents a strong flow of air in one corner and a dead zone in the other corner. **The problem:** you must calculate the tube diameter, the hole size and the hole spacing, and the fan must make the necessary pressure.

**Inline duct fan**

An inline duct fan is a fan in a duct. It is a device for **air exchange** and not a device for circulation. It pulls air out of the room, usually through a carbon filter, and sends the air outdoors. It controls the humidity and gives new CO2 to a room with vents.
**Where:** on a duct to the top of the room (hot air with high humidity moves up). Put an intake at the bottom of the room (with or without a fan). **The problem:** some persons think that this fan makes the airflow for the canopy, but it does not. A room that has a large inline duct fan and no recirculation fans has a canopy with still air and high humidity.

Three more types of fan are for larger rooms. Use them for the correct task and not for canopy airflow:

**HVLS / destratification fan**

An HVLS fan is a large ceiling fan with a very low speed. In a room with lights, a layer of warm air collects near the ceiling. The task of the fan is to break this layer and to push the air down again. It operates correctly in rooms with a large ceiling height. It has no effect in a room with a ceiling height of 2.4 m.

**Wall / shutter exhaust fan**

This fan does air exchange for large volumes of air in greenhouses and large rooms. The shutters open by gravity or with a motor. It is the same type as the inline duct fan, but it is much larger. A sealed room usually does not have this fan.

**AHU / HVAC supply**

The AHU is the unit that does the heating, the cooling and the drying of the air. It controls the VPD. It must also have a method to supply this conditioned air equally across a canopy. Typically, this method is a duct that connects to air socks.

Recirculation · vertical racksIn-rack airflow systems (vertical farms)If the plants are on racks with many tiers, no other fan type operates correctly. Each tier is a closed space with a small height, and fans that hang above the racks cannot supply air to it. In-rack systems have a fan bar with ducts, and you install the fan bar in the rack. The fan bar pushes air along each tier or down through each tier[^vas-inrack]. On racks, an in-rack system is the only system that operates correctly. The Pipp test in section 09 was a test of this setup.

## Select fans for canopy airflow

A ranking is correct only for one condition, and you must give this condition. This ranking is for **the airflow that is important for the crop, for each dollar of installed cost**. The room is **a sealed indoor flower room with one tier**, with a canopy of approximately 20 to 200 m² (215 to 2,150 ft²). When the room is different, the sequence of the fans is different. The points after the table show how.

> **Diagram.** The primary fans of the room have a low cost. The two fans at the bottom of the ranking are the two fans that most new growers get.

| # | Fan type | Effect of the fan | Depth in the canopy | Selection |
| --- | --- | --- | --- | --- |
| 1 | **HAF fan** | A loop of air around the room. It operates 24/7 with very low power. | Only along the top | **Make these fans the primary fans of the room.** The minimum cost for uniformity[^bartok-haf] |
| 2 | **Under-canopy fan** | Removes the zone with the most water and the minimum air movement in the room | Bottom of the plant | **The best fan to add, for the cost.** It is for the area where bud rot starts |
| 3 | **VAF fan** | Air that moves down into the middle of the plant | The full depth. The VAF fan is the only fan that supplies air at this depth. | **Use with care in a sealed room that you cool.** The fan pushes the warm air from the level of the lights into the canopy. Measure the vertical temperature difference first (refer to the box after the table). No cannabis study shows an effect on calcium. |
| 4 | Oscillating fan | Low cost. Turbulent airflow that changes direction. | Along the canopy and around it, for short times | It is good as the primary fan for a canopy of less than approximately 20 m² (215 ft²). For a larger canopy, other fans are better. |
| 5 | Air sock from the AHU | Equal supply of _conditioned_ air, with no strong flow of air at one point | Along the row, with a light airflow | Very good, but it has a capital cost, and you must calculate the sizes of the system[^perfduct2025] |
| 6 | HVLS / destratification | Breaks the layer of hot air near the ceiling | It mixes only the large volume of air. | It operates correctly in rooms with a large ceiling height. It has no effect when the ceiling height is small. |
| 7 | Drum / pedestal fan | Air with a very high speed at one point | A very strong airflow on the axis and no airflow in the other areas | Use only to correct one area. The most frequent cause of wind damage. |
| 8 | Clip fan | The air for one plant | One plant | Use only in tents. Six clip fans give a worse result than one hung fan. |
| The ranking is for the airflow for each dollar in a sealed indoor flower room with one tier. The ranking does not include equipment for air exchange (inline duct fans and wall fans). This equipment is necessary, but it does a different task, and you cannot use it as a recirculation fan. |

> **KEY: When the ranking changes**
>
> - **Vertical racks:** in-rack systems become #1, and HAF fans are not in the list. Fans that hang above the racks cannot supply air to the inner part of a tier[^vas-inrack].
> - **Dense canopy with no defoliation:** first open the canopy (defoliation), then add under-canopy fans. Plant factories for lettuce add vertical airflow onto the canopy to help stop tipburn[^zhang2016-cfd], but no test shows this effect in cannabis. Add VAF fans only where the air above the canopy is not warmer than the air in the canopy.
> - **Sealed room that you cool, with returns at the ceiling:** if the air at the level of the lights is clearly warmer than the canopy, the air sock (or another supply of conditioned air at or below the canopy) gets a higher position than the VAF fan. Top-down fans mix the heat from the lights into the canopy[^ashrae2023-roomair][^quest-airflow].
> - **Tents and setups for one plant:** all the table changes to one or two clip fans and the inline duct fan. This selection is correct at this size.
> - **Greenhouses:** HAF fans stay #1, and the air sock gets a higher position, because you also move heat in the greenhouse[^uconn-haf].

> **WARN: Top-down fans and heat**
>
> A VAF fan does not make cool air. It takes in the air above the canopy and pushes this air down. In a grow room, the lights are the largest load of sensible heat. The energy that an LED fixture does not release as light goes from its heat sinks and its driver into the air at the fixture. Warm air rises. Thus, in a room without strong mixing, the air at the level of the lights is warmer than the air in the canopy.
> HVAC engineers use this effect. ASHRAE divides air distribution into fully mixed, stratified and partially mixed systems. In a stratified system, the warm air rises to returns at the ceiling, and the occupied zone stays cooler than the return air[^ashrae2023-roomair]. In a grow room, the canopy is the occupied zone. Designers of cannabis rooms recommend that you supply the air at or below the canopy and pull it up through the plants to returns at the ceiling[^quest-airflow]. Then the HVAC removes the hottest air first.
> Top-down fans change this room into a fully mixed room. The results are:
> - The warm air from the lights goes into the canopy, and the air temperature in the canopy increases.
> - The return air is not warmer than the canopy. The airflow that the HVAC must supply increases when the temperature difference between the supply and the return decreases[^ashrae2023-roomair].
> - The fan motors are a source of sensible heat in the room[^rii2022-hvac]. The HVAC must also remove this heat.
> Greenhouses use vertical fans for the opposite task. The fans move the heat of the lamps from the top of the greenhouse down to the crop[^vostermans-vflo]. This is good when you want heat at the crop. It is bad when you cool the room.
> Moving air removes heat from a leaf in two ways. By convection, the air takes heat from the leaf only when the air is cooler than the leaf. By transpiration, the water that evaporates from the leaf cools it, and this can occur also in air that is warmer than the leaf, if the plant has sufficient water and the air is not saturated[^nelson2015-leaftemp]. When a plant has sufficient water and the air moves, the leaf usually stays within approximately 2 °C of the air temperature. With low air movement and water stress, the leaf can become much hotter than the air[^nelson2015-leaftemp]. In lettuce, an airflow of 0.65 m/s made the leaves approximately 1.3 °C cooler than an airflow of 0.22 m/s[^dupont2026-lowwind]. Thus, warm air from the lights does not always make the leaf hotter, but it increases the air temperature in the canopy and the load on the HVAC. To find the net effect on the leaf, measure the leaf temperature (with an IR thermometer) and the humidity before and after you add the fans.
> Vertical airflow can operate correctly when the air that goes down is **conditioned supply air** from the HVAC, and not air from the level of the lights. In a model of a vertical farm, conditioned air that went vertically into the canopy decreased the average canopy air temperature by 2.43 °C, compared with usual fans. It also made the temperature and the humidity more uniform[^tmu2026-vfarm].
> **Test before you install VAF fans:** when the lights are on, measure the air temperature at the height where the fan takes in air. Then measure it in the middle of the canopy. If the air at the intake is warmer, the fan will increase the air temperature in the canopy. Use sensors at canopy level and at more than one point, not one sensor on a wall[^rii2022-hvac].

> **WARN: The problem that the ranking prevents**
>
> Select the airflow pattern and not the peak value. Almost all rooms with low performance have the same problem. **The total CFM is large, but the airflow is not the same in all areas.** Two drum fans in the corners give a high CFM value on paper. The middle of the room has still air and high humidity. Six small hung fans in a loop give a lower CFM value, but each leaf moves.

## Fan position

The position of the fans is a problem of airflow pattern and not a problem of area. Do not try to put a jet of air on each plant. Make all the air in the room move slowly and constantly in a loop. Then get this moving air into the canopy, without adding heat to it.

> **Diagram.** The horizontal loop from above. The fans do not each supply air to one area only. The fans give air to each other around a circuit. The first fan is approximately 3 to 4.5 m (10 to 15 ft) from the end wall. The other fans are 12 to 15 m (40 to 50 ft) apart, and approximately a quarter of the room width from the side wall[^bartok-haf][^uconn-haf].

Then examine the room in a vertical section. In most rooms, the airflow is only at the top of the canopy. This condition causes rot to start at the bottom and in the middle:

> **Diagram.** The same room in a vertical section. There are three heights, three different tasks, and three different fans. If the room has only HAF fans, the airflow is in the top zone only. The two zones in which disease starts have no airflow.

1. **Make the loop first**: Select one direction. Do not change it. Hang the HAF fans to make the air go along one side and back along the other side. Each fan gives air to the next fan. Do not point two fans at each other. The loop stops, and a dead zone occurs where the two jets touch[^bartok-haf].
2. **Set the correct height**: Hang the fans above head height, approximately 2.1 to 2.4 m (7 to 8 ft) from the floor for a crop at floor level. Thus the jet goes above the canopy and does not push into the canopy[^uconn-haf]. If hung baskets or a rack for lights are at this height, hang the fans above them or below them. Do not hang the fans at the same height.
3. **Get air into the canopy without adding heat**: First, open the canopy with defoliation. Then add under-canopy fans (step 4). If you can, supply conditioned air at or below the canopy, for example with air socks, and return it at the ceiling[^quest-airflow][^tmu2026-vfarm]. Install top-down fans only where the air above the canopy is not warmer than the canopy (refer to “Top-down fans and heat” in section 11).
4. **Supply air to the floor**: Put fans at the level of the pots. Point the fans along the rows. Cold air with high humidity collects at this level, and no fan above the canopy moves it.
5. **Mix the air, with no strong jets**: Point each fan in a direction with a small difference from the next fan. Let the oscillation change the direction. The room must have slow, turbulent airflow that mixes the air, and not a set of jets[^schuepp1993-bl].
6. **Walk through the room and correct**: Do the leaf movement test at three heights. The heights are above the tops, in the middle of a plant and at the level of the pots. In the middle of a plant, put your hand into the plant. If the leaves do not move at one height, you do not have the fan for that height. A strip of tape on a stake, or a low-cost anemometer, gives a reading and not an estimate.

> **TIP: Operate the fans at all times**
>
> Operate the circulation fans for **24 hours each day**, when the lights are on and when the lights are off. The extension service recommends that the fans operate continuously. The fans can be off when the exhaust fans operate or the vents are open, because the room has air exchange at these times[^bartok-haf]. When the lights are off, the leaf temperature decreases and becomes almost the same as the dew point, and condensation starts. At this time, you must not have still air[^uconn-haf].

## Size of the system

For many years, the greenhouse industry calculated the size of horizontal airflow. Its approximate values are also correct for an indoor room. Start with these values. Then measure the airflow. Adjust the fans:

| Item | Approximate value | Source |
| --- | --- | --- |
| Total circulation capacity | **Approximately 36.6 m³/h for each m² of floor** (approximately 2 CFM/ft²). A greenhouse of 9 × 30 m (30 × 100 ft) must have a total of approximately 10,000 m³/h (approximately 6,000 CFM). | Bartok and Grubinger, UConn/UVM Extension[^bartok-haf] |
| First fan position | 3 to 4.5 m (10 to 15 ft) from the end wall, to get the air that turns at the corner. | UConn IPM[^uconn-haf] |
| Fan spacing | 12 to 15 m (40 to 50 ft) apart along the loop. In a small room, decrease the distance in the same ratio. | Bartok and Grubinger[^bartok-haf] |
| Horizontal position | Approximately ¼ of the room width from the side wall (or the middle of the bay). | UConn IPM[^uconn-haf] |
| Installation height | Above head height. Approximately 2.1 to 2.4 m (7 to 8 ft) for crops at floor level. Keep a distance from baskets and racks for lights. | Bartok and Grubinger[^bartok-haf] |
| Size of each fan | Blade of 300 to 500 mm (12 to 20 in), motor of 1/10 to 1/15 hp. A large number of small fans is better than a small number of large fans. | Bartok and Grubinger[^bartok-haf] |
| Greenhouse velocity target | 0.25 to 0.5 m/s (50 to 100 FPM) for the general movement of air in the room. | UConn IPM[^uconn-haf] |
| Minimum at crop level (all CEA crops) | At least 0.25 m/s (50 FPM) at the crop. Some crops need 0.75 m/s (150 FPM) or more for maximum production. Measure with a hot-wire anemometer. | Resource Innovation Institute HVAC guide[^rii2022-hvac] |
| Cannabis flower-room target | Approximately 1.0 m/s (approximately 200 FPM) that the room _supplies_, to give each leaf an air velocity in the target range. | Pipp / Justice test[^pipp2026-airflow] |
| Operation time | 24/7, but not while the exhaust fans operate or the vents are open. | Bartok and Grubinger[^bartok-haf] |
| Air sock specification | Holes of 6 to 10 mm with a spacing of 30 to 70 mm. A static pressure of approximately 30 to 40 Pa keeps the tube circular. | Investigation of a duct with holes (CFD)[^perfduct2025] |

> **NOTE: The two velocity targets are different**
>
> The greenhouse value (0.25 to 0.5 m/s, or 50 to 100 FPM) and the value for cannabis (approximately 1.0 m/s, or approximately 200 FPM) are correct for different tasks. The greenhouse value is for temperature uniformity and to stop condensation on the leaves during the night. The crop has a more open canopy and less light[^uconn-haf]. The value for cannabis is from a flower canopy with a high density and high light. In this canopy, the task is to push air _into_ the plant[^pipp2026-airflow].
> A higher canopy density increases the value, and a higher light intensity also increases the value. Use the greenhouse values for the position of the fans and the value for cannabis for the target.

The last number is the number that decreases the cost the most. The airflow of a fan increases in the same ratio as the speed, but the shaft power increases with the **cube** of the speed[^amca-fanlaws]. When the speed of a fan becomes half, the power becomes approximately one eighth. This fact has an effect on the selection of fans:

> **KEY: More fans at a lower speed is always better**
>
> Two fans at full speed and eight fans at half speed can move almost the same quantity of air. But the eight fans use approximately a quarter of the power _and_ give a much better airflow in all areas. The air comes from more directions, and there is a smaller number of dead zones.
> Fans with an EC motor have a speed control. They have a higher cost than fans with an AC motor that has one speed, but the higher cost gives a better result. A fan with an AC motor is usually on or off. To decrease the airflow, you must set some fans to off. The result is areas without airflow at the positions of the fans that you stopped.

## Troubleshooting

| Symptom | Possible cause | To correct it |
| --- | --- | --- |
| Bud rot starts in the inner part of the colas | Dead zone: the air does not go to the inner part of the canopy | Defoliate the plants. Add under-canopy airflow. Decrease the RH. Add VAF fans only if the air above the canopy is not warmer than the canopy. |
| The tops of the plants move, but the middle and the bottom do not move | All the airflow is above the canopy (HAF fans only) | Defoliate. Add under-canopy fans at the level of the pots. Then add VAF fans if the vertical temperature test permits. |
| The canopy becomes hotter after you add top-down fans | The VAF fans push the warm air from the level of the lights into the canopy | Measure the temperature above and in the canopy. Decrease the speed of the VAF fans or remove them. Supply conditioned air low and return it high. |
| Rot and mildew start at the bottom of the plants | The zone at the floor has the most water and the minimum air movement in the room | Install under-canopy fans that blow along the rows. |
| Leaf tipburn, but the tank is full | The airflow is too high for the supply of nutrient (calcium) | Increase the feed EC to agree with the transpiration |
| Tipburn only on new growth in the inner part | Possible calcium deficiency: the inner leaves are in still air and transpire slowly. But first make sure that the cause is not high EC, drought or potassium deficiency. | Do a leaf tissue test. The position of the symptom alone is not sufficient. Open the canopy and add under-canopy airflow before you add top-down fans. |
| Leaves with the claw, or edges with wind damage | The air velocity is too high, or a fan points at the plants | Decrease the speed. Point the fans to mix the air and not to make strong jets. |
| One end of a row is always different | The loop does not operate: the fans are too far apart or they point at each other | Set the racetrack loop again. Do not point two fans at each other. |
| Large fans and much noise, but the air continues to be in layers | The number of fans is too small, and they operate at full speed | Use more fans at a lower speed. The power increases with the cube of the speed. |
| Plants with a large height and weak stems that bend | Air movement is too low, and thus there is no mechanical signal | Add a light, constant airflow across the canopy |
| The humidity of the room stays high | Recirculation is correct, but air exchange is not sufficient | Increase the intake and the exhaust. Increase the dehumidification. |
| A cold or dry area below the outlet of the air conditioner | The conditioned air goes to one point only | Send the air through a duct to an air sock along the row |

## Expected results and limitations

> **KEY: The primary points**
>
> 1. The task of airflow is to **make the boundary layer thinner** on each leaf.
> 2. Make a **light, turbulent airflow (approximately 0.3 to 1.0 m/s)** in all areas, and also in the inner part of the plants.
> 3. Select the **airflow pattern and not the peak value**. Many small fans in a loop are better than two large fans in the corners.
> 4. Supply air at **all three heights**: above, through and below the canopy. Only the first height is easy.
> 5. More airflow causes more use of water: **the feed and the humidity control must increase also**[^gilliham2011-ca].
> 6. Most of the effect occurs at low air velocity. A very high air velocity is not necessary[^kitaya2004-airvel].

Airflow is one part of the system of the room. Read this paper with the [systems guide](grow-room-systems.html) and the [mold risk](mould-risk.html) paper.

## References

[^schuepp1993-bl]: Schuepp PH (1993). Tansley Review No. 59: Leaf boundary layers. New Phytologist 125(3):477-507. https://doi.org/10.1111/j.1469-8137.1993.tb03898.x (source with peer review)
[^dupont2025-wind]: Dupont K, van den Berg TE, Zhang J, Moene AF, Vialet-Chabrand SRM (2025). Beyond the boundary: a new road to improve photosynthesis via wind. J. Exp. Bot. 76(20):5791-5813. https://doi.org/10.1093/jxb/eraf325 (source with peer review)
[^kitaya2004-airvel]: Kitaya Y, Shibuya T, Yoshida M, Kiyota M (2004). Effects of air velocity on photosynthesis of plant canopies under elevated CO2 levels. Adv. Space Res. 34(7):1466-1469. https://doi.org/10.1016/j.asr.2003.08.031 (source with peer review)
[^tjosvold2018-air]: Tjosvold SA (2018). Maximize photosynthesis with moving air. UC ANR Greenhouse & Floriculture (extension article). https://ucanr.edu/blogs/blogcore/postdetail.cfm?postnum=28455 (source from a manufacturer or industry)
[^rm2021-light]: Rodriguez-Morrison V, Llewellyn D, Zheng Y (2021). Cannabis yield, potency, and leaf photosynthesis respond differently to increasing light levels in an indoor environment. Front. Plant Sci. 12:646020. https://pmc.ncbi.nlm.nih.gov/articles/PMC8144505/ (source with peer review)
[^kitaya2010-circ]: Kitaya Y, Tsuruyama J, Shibuya T, Yoshida M, Kiyota M (2010). CO2 and air circulation effects on photosynthesis and transpiration of tomato seedlings. Scientia Horticulturae 126(2):326-330. https://www.sciencedirect.com/science/article/abs/pii/S0304423810003316 (source with peer review)
[^gilliham2011-ca]: Gilliham M, et al. (2011). Calcium delivery and storage in plant leaves: exploring the link with water flow. J. Exp. Bot. 62(7):2233-2250. https://doi.org/10.1093/jxb/err111 (source with peer review)
[^chehab2009-thigmo]: Chehab EW, Eich E, Braam J (2009). Thigmomorphogenesis: a complex plant response to mechano-stimulation. J. Exp. Bot. 60(1):43-56. https://doi.org/10.1093/jxb/ern315 (source with peer review)
[^chandra2008-photo]: Chandra S, Lata H, Khan IA, ElSohly MA (2008). Photosynthetic response of Cannabis sativa L. to variations in photosynthetic photon flux densities, temperature and CO2 conditions. Physiol. Mol. Biol. Plants 14(4):299-306. https://pmc.ncbi.nlm.nih.gov/articles/PMC3550641/ (source with peer review)
[^pipp2026-airflow]: Anderson K (2026). What cannabis growers can finally learn about airflow. Pipp Horticulture — controlled flower-room trials with Dr. Allison Justice and the Cannabis Research Coalition. (Preliminary: one replicate reported, second underway.) https://pipphorticulture.com/what-cannabis-growers-can-finally-learn-about-airflow/ (source from a manufacturer or industry)
[^bartok-haf]: Bartok JW, Grubinger V. Horizontal air flow is best for greenhouse air circulation. UMass Extension Greenhouse & Floriculture / eXtension Farm Energy (extension fact sheet). https://farm-energy.extension.org/horizontal-air-flow-is-best-for-greenhouse-air-circulation/ (source from a manufacturer or industry)
[^uconn-haf]: University of Connecticut Integrated Pest Management. Horizontal air flow systems. UConn CAHNR (extension fact sheet). https://ipm.cahnr.uconn.edu/horizontal-air-flow-systems/ (source from a manufacturer or industry)
[^goto1992-tipburn]: Goto E, Takakura T (1992). Prevention of lettuce tipburn by supplying air to inner leaves. Transactions of the ASAE 35(2):641-645. https://doi.org/10.13031/2013.28644 (source with peer review)
[^ahmed2020-multifan]: Ahmed HA, Tong YX, Yang QC (2020). Lettuce plant growth and tipburn occurrence as affected by airflow using a multi-fan system in a plant factory with artificial light. J. Thermal Biology 88:102496. https://doi.org/10.1016/j.jtherbio.2019.102496 (source with peer review)
[^moosavi2025-vaf]: Moosavi-Nezhad M, Meng Q (2025). A calcium-mobilizing biostimulant provides tipburn control comparable to vertical airflow fans in greenhouse hydroponic lettuce 'Rex'. Front. Plant Sci. 16:1701667. https://doi.org/10.3389/fpls.2025.1701667 (source with peer review)
[^perfduct2025]: Wang C, Fu J, Zhang Q, Sheng B, He F, Zhang G, Ding X, Cao N (2025). Optimizing perforated duct systems for energy-efficient ventilation in semi-closed greenhouses through process regulation. Processes (MDPI) 13(7):2253. https://doi.org/10.3390/pr13072253 (source with peer review)
[^amca-fanlaws]: Air Movement and Control Association International (AMCA). Fan laws (affinity laws): airflow varies with fan speed, pressure with the square of speed, shaft power with the cube of speed. Standard fan-engineering relationship. https://www.amca.org/ (source from a manufacturer or industry)
[^vas-inrack]: Vertical Air Solutions / Pipp Horticulture. In-rack airflow systems for vertical cannabis racking (manufacturer documentation). https://pipphorticulture.com/in-rack-airflow-systems/ (source from a manufacturer or industry)
[^cockson2019-nutr]: Cockson P, Landis H, Smith T, Hicks K, Whipker BE (2019). Characterization of nutrient disorders of Cannabis sativa. Applied Sciences (MDPI) 9(20):4432. https://doi.org/10.3390/app9204432 (source with peer review)
[^llewellyn2023-def]: Llewellyn D, Golem S, et al. (2023). Foliar symptomology, nutrient content, yield, and secondary metabolite variability of cannabis grown hydroponically with different single-element nutrient deficiencies. Plants (MDPI) 12(3):422. https://pmc.ncbi.nlm.nih.gov/articles/PMC9920212/ (source with peer review)
[^cbt-marginburn]: Feel the (cannabis leaf margin) burn. Cannabis Business Times, Cultivation Matters column (trade article): leaf margin burn from high EC, drought, potassium and calcium deficiency. https://www.cannabisbusinesstimes.com/columns/cultivation-matters/news/15750558/feel-the-cannabis-leaf-margin-burn (source from a manufacturer or industry)
[^nelson2015-leaftemp]: Nelson JA, Bugbee B (2015). Analysis of environmental effects on leaf temperature under sunlight, high pressure sodium and light emitting diodes. PLoS ONE 10(10):e0138930 (well-watered leaves typically within ~2 °C of air; LED canopies ~1.3 °C cooler than HPS at equal photon flux; water-stressed leaves modelled 6-12 °C above air). https://doi.org/10.1371/journal.pone.0138930 (source with peer review)
[^dupont2026-lowwind]: Dupont K, Frati R, Vialet-Chabrand SRM (2026). Low wind, high impact: sustained low airflow alters water use efficiency and shapes plant acclimation. J. Exp. Bot. 77(16):5225-5243. (Lettuce, 0.22 vs 0.65 m/s.) https://academic.oup.com/jxb/article/77/16/5225/8656750 (source with peer review)
[^zhang2016-cfd]: Zhang Y, Kacira M, An L (2016). A CFD study on improving air flow uniformity in indoor plant factory system. Biosystems Engineering 147:193-205. https://www.researchgate.net/publication/302972809_A_CFD_study_on_improving_air_flow_uniformity_in_indoor_plant_factory_system (source with peer review)
[^ashrae2023-roomair]: ASHRAE (2023). Room air distribution. ASHRAE Handbook: HVAC Applications, Chapter 58 (fully mixed, stratified and partially mixed systems; supply airflow and supply-return temperature difference). https://handbook.ashrae.org/Handbooks/A23/IP/A23_Ch58/a23_ch58_ip.aspx (source from a manufacturer or industry)
[^rii2022-hvac]: Resource Innovation Institute (2022). HVAC Best Practices Guide for controlled environment agriculture (USDA NRCS funded): airflow at crop level, fan motors as internal sensible heat, canopy-level sensing. https://resourceinnovation.org/wp-content/uploads/2022/06/RII-HvacBPG-2022-v4-1.pdf (source from a manufacturer or industry)
[^quest-airflow]: How to ensure proper airflow at your indoor cannabis cultivation facility (G. Brown, Quest). Cannabis Business Times (sponsored trade article). https://www.cannabisbusinesstimes.com/article/how-to-ensure-proper-airflow-indoor-cannabis-cultivation-quest/ (source from a manufacturer or industry)
[^vostermans-vflo]: Vostermans Ventilation. Multifan V-FloFan vertical circulation fan (manufacturer documentation): moving lamp heat from the greenhouse ridge down to the crop. https://www.vostermans.com/ventilation/axial-fans/v-flofan (source from a manufacturer or industry)
[^tmu2026-vfarm]: Optimization of thermal performance and microclimate in vertical farms using computational fluid dynamics (2026). ICTEA proceedings, Toronto Metropolitan University. (CFD validated on a two-tier raspberry prototype.) https://journals.library.torontomu.ca/index.php/ictea/article/view/2869 (source from a manufacturer or industry)
