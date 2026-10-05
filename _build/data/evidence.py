# -*- coding: utf-8 -*-
"""Per-paper evidence tiers: solid / operational / provisional.

Injected by build.py as a standard 'How sure is this?' section so readers can
tell verified science from commercial practice and unverified folklore.
"""
from components import esc

# Tiers:
# solid       — strong plant physiology, standards, or multi-source consensus
# operational — commercial practice ranges; work well but cultivar/facility vary
# provisional — thin cannabis data, single studies, product design, or folklore

DEFAULT = {
    "solid": [
        "The primary definitions and the units of measurement in the paper",
        "Safety limits that have a citation to a regulation or a specification",
    ],
    "operational": [
        "Target ranges for light, climate and feed in each stage. They are start values that you can change.",
        "SOPs that work in many rooms, but you must adjust them for your genetics and meters",
    ],
    "provisional": [
        "A number for yield or potency that you will always get, with no test at many sites",
        "Controller setpoints from a different facility, with no new calibration",
    ],
}

# slug -> {solid, operational, provisional} lists of short strings
PAPERS = {
    "seeds-germination": {
        "solid": [
            "Water and a warm temperature are necessary for seeds. Damping-off occurs because of conditions that are too wet and have no air movement.",
            "Feminized seed is the result of XX×XX induction with STS, colloidal silver or an equivalent method. The seed does not give 100% protection from hermaphrodites.",
            "The length of the night controls flowering in photoperiod plants. Autoflower plants make flowers mostly because of their age and genetics.",
        ],
        "operational": [
            "A germination temperature range of 21 to 25 °C, and slow PPFD ramps for seedlings.",
            "Use a humidity dome and a high RH at the start. Then decrease the humidity when the roots become longer.",
            "Visual checks of seed quality (color and firmness) as a first selection, and not as a laboratory test of viability.",
        ],
        "provisional": [
            "One germination percentage for all seed lots. The age of the batch and the storage have the largest effect.",
            "Very high germination rates for the paper towel method. The method is less important than the quality of the seed and the control of moisture.",
        ],
    },
    "cloning": {
        "solid": [
            "A clone has the same genetics as the mother plant. A somatic mutation, which is not frequent, can cause a difference.",
            "High humidity and a low light intensity decrease the stress on a cutting until the cutting makes roots.",
            "Dirty tools and wet media where the water does not move increase the risk of soft rot and of pathogens.",
        ],
        "operational": [
            "Procedures with IBA gel or powder, and procedures to open the dome vents, in commercial rooms for propagation.",
            "The target for a room with correct control is a rooting rate of 90% or more. Genetics do not make sure of this rate.",
            "Apply a feed with a low EC after the roots show. An EC that is too high causes damage to soft cuttings.",
        ],
        "provisional": [
            "Air embolism as the one primary cause of soft stems. Drying of the cutting usually has the largest effect.",
            "Tables with one number of days to roots that ignore the cultivar and the environment.",
        ],
    },
    "tissue-culture": {
        "solid": [
            "Meristem tissue frequently contains a smaller quantity of systemic pathogens than a nodal cutting contains.",
            "A spray cannot remove a viroid infection from a plant. After a cleanup, a plant without the viroid is not resistant to the viroid.",
            "RT-qPCR (RNA) is the correct type of test for HpLVd. A test with only a DNA strip is not correct.",
        ],
        "operational": [
            "In the first batch of a grower who is new to the work, contamination kills many cultures. Cannabis is a recalcitrant species.",
            "Some months are necessary to get mother plants that tests show are clean. This time includes the indexing.",
            "The quality of the aseptic technique has a larger effect than the manufacturer of the kit.",
        ],
        "provisional": [
            "Infection rates from investigations of facilities as permanent rates for all areas. An investigation gives a rate for one time and one area.",
            "One percentage of seed transmission for all crosses. The percentage changes with the genotype.",
            "Only tissue culture, with no hygiene after it, as a permanent method to remove all endophytes, mites and surface pathogens.",
        ],
    },
    "light-acclimation": {
        "solid": [
            "A large and sudden increase of PPFD causes photoinhibition and bleaching. A ramp of PPFD decreases this risk.",
            "At equal PPFD, a photoperiod of 12/12 gives a DLI that is one-third (approximately 33%) less than a photoperiod of 18/6.",
        ],
        "operational": [
            "Ramps of more than one day, with a dimmer or with the height of the fixture, in commercial rooms.",
            "The maximum light intensities that growers can use in a room with no CO₂ enrichment. They give information about stress and ROI.",
        ],
        "provisional": [
            "One percentage of yield increase from far-red light for all cultivars.",
            "Schedules with the instruction that the PPFD must be X µmol on day Y, with no data on the leaf temperature and the VPD.",
        ],
    },
    "defoliation-training": {
        "solid": [
            "Leaves are sources of carbon. When you remove leaves, you remove capacity for photosynthesis.",
            "The structure of the canopy has an effect on the light that the canopy absorbs, on the airflow, and on the risk of mold.",
        ],
        "operational": [
            "Periods for topping, LST, SCROG and lollipopping that many indoor growers use.",
            "Stop the removal of many leaves when flower bulking starts.",
        ],
        "provisional": [
            "One percentage of yield increase from one defoliation procedure for all plant densities.",
            "Topping on day 5 to 7 as the time for all plants. A clone starts with many nodes, and a plant from seed is different.",
        ],
    },
    "flowering-stages": {
        "solid": [
            "Long nights are necessary for photoperiod cannabis. A light leak can cause problems for flowering.",
            "Trichomes and pistils are signs of maturity. A calendar is a weak sign when it is the only sign.",
            "In the last weeks of flowering, the risk of Botrytis increases when the canopy has a high density and the humidity is high.",
        ],
        "operational": [
            "Week-by-week tables for the 8 to 10 weeks of flowering of hybrids, and climate ranges for each stage.",
            "The estimates of stretch are very different for each cultivar and each light spectrum.",
        ],
        "provisional": [
            "Amber trichomes, then CBN, then couch-lock, as one clear sequence. Many causes have an effect. The data on CBN in persons are small.",
            "A long period in which you flush the plants with only water to increase smoke quality. Controlled tests frequently show a small effect.",
            "A phone LED or a very small indicator light as a sure hermaphrodite trigger. Light leaks at night are important. Genetics and many stresses have the largest effect.",
        ],
    },
    "coco-crop-steering": {
        "solid": [
            "Coco is almost inert. The operator can control most of the EC and the water content of the root zone.",
            "A small water deficit can change the secondary metabolism of the plant. A large drought causes stress in plants.",
        ],
        "operational": [
            "The dryback of each day and the runoff EC, as the levers for steering in commercial rooms.",
            "Targets for field capacity and for the dryback point, after you calibrate the sensor for each medium.",
        ],
        "provisional": [
            "One drought in the last stage of the crop (the test of Caplan) directly as a procedure of dryback each day for many weeks.",
            "One range of EC for generative growth that ignores the cultivar and the light intensity.",
        ],
    },
    "rockwool-crop-steering": {
        "solid": [
            "Rockwool contains almost no nutrients. The pore water has almost the same chemical properties as the feed.",
            "A slab that is too dry can have channeling. The slab then does not become wet again correctly.",
        ],
        "operational": [
            "Dryback ranges and irrigation procedures with many shots that manufacturers use, as in the procedures of Grodan.",
            "Control of the runoff to keep the salt that collects in the substrate at a minimum.",
        ],
        "provisional": [
            "One value of the water content for the recovery floor as a constant of physics for all products.",
            "An inverse formula for EC that ignores plant uptake, as the accurate substrate EC.",
        ],
    },
    "one-steering-law": {
        "solid": [
            "The wet and dry cycle and the strength of the feed are the same steering controls in all media.",
            "Soil is a buffer. Coco, rockwool and water do not have the same buffer.",
        ],
        "operational": [
            "One model for all substrates, with a drive and a brake.",
        ],
        "provisional": [
            "Coco procedures for a new grower that use the high-intensity substrate EC values of rockwool.",
            "Root rot in DWC in one day or less at more than 23 °C as a time for all systems. DO and heat change the time.",
        ],
    },
    "harvest-dry-trim-cure": {
        "solid": [
            "Water activity is a better indicator of the risk from microbes than only the moisture percentage. For flower, an ASTM-type range is 0.55 to 0.65.",
            "Slow drying in darkness at a cool temperature keeps more terpenes than fast drying at a hot temperature.",
            "In storage, light and heat increase the rate of degradation of cannabinoids and terpenes.",
        ],
        "operational": [
            "Usual values of 60 °F and 60% RH for drying, and the procedure to hang all of the plant.",
            "Many rooms select dry trim when quality is important.",
        ],
        "provisional": [
            "A supplier value of 5 to 10% yield recovered as the result of tests at many sites with peer review.",
            "The quantity by which trimming decreases the water activity (aw) as one value for all conditions.",
        ],
    },
    "gmp-hash-lab": {
        "solid": [
            "A concentrate can have a higher concentration of residues than the input biomass. The difference changes with the extraction yield and the partitioning.",
            "Systems that you can examine, with records, CAPA and genealogy, are the primary part of GMP.",
        ],
        "operational": [
            "Procedures for room flow, for gowning and for batch records, in facilities that a regulator controls.",
        ],
        "provisional": [
            "ICH values for residual solvents as the limits of your cannabis license. The limits are different in each jurisdiction.",
            "EU Annex 1 Grade A or B for all hash. The grade changes with the product and with the license.",
            "A list of seven mandatory groups of tests that ignores the panel of your regulator.",
        ],
    },
    "grow-room-systems": {
        "solid": [
            "Light, heat, humidity, CO₂, water and airflow have an effect on each other. When you change one of them, all the other items change.",
            "VPD shows the effect of the temperature and the RH together on the plant, in one value.",
        ],
        "operational": [
            "VPD ranges of the type 0.8 to 1.5 kPa for each stage, as start values in horticulture.",
            "The decision to use a sealed room or a room with vents.",
        ],
        "provisional": [
            "Accurate VPD values that are best for crops other than cannabis as mandatory values for cannabis.",
            "VPD as the only cause of tacoing (leaf edges that bend up) in all conditions. Frequently, light, leaf heat and VPD together are the cause.",
        ],
    },
    "lighting-fundamentals": {
        "solid": [
            "The definitions of PAR, PPFD and DLI. The length of the night in the photoperiod controls flowering.",
            "More light increases the yield only until a different condition becomes the limit (Liebig).",
            "Efficacy ranges for new LED fixtures. The ranges change with time, thus examine the current DLC data and the PPFD maps.",
        ],
        "operational": [
            "Tables of PPFD for each stage for indoor cannabis, with CO₂ enrichment and without CO₂ enrichment.",
            "Checks of uniformity with a PPFD map of 9 points.",
        ],
        "provisional": [
            "The inverse-square law as an accurate formula for the height at which LED panels with many bars hang. Use maps and meters.",
            "Red light as the primary mechanism that causes flowering. The photoperiod is the primary mechanism, and R:FR has an effect on morphology.",
            "UV-B as a sure method to increase potency. The data are mixed, and UV-B has a risk to safety.",
        ],
    },
    "airflow-design": {
        "solid": [
            "When the boundary layer becomes thinner, gas exchange increases. Air that does not move keeps the humidity at the leaf.",
            "Mechanical movement of the stem (thigmomorphogenesis) can change the strength of the stem.",
        ],
        "operational": [
            "Ranges of air speed of approximately 0.3 to 1.0 m/s that make the canopy move, and the usual positions of HAF fans.",
        ],
        "provisional": [
            "A sudden change in disease or stress at one value of air velocity, with no specified height of measurement.",
        ],
    },
    "under-canopy-lighting": {
        "solid": [
            "The top canopy filters the spectrum. The light below it has more green and far-red, and less blue and red, than the light above it.",
            "The bottom flower sites frequently do not receive sufficient light for the grade and the fill of the flower.",
        ],
        "operational": [
            "SCL and ICL in commercial rooms, and control of the risk of bleaching when the distance to the plant is short.",
        ],
        "provisional": [
            "A minimum PPFD for viability that is the same for all bottom flowers.",
            "Procedures for a sealed room with a continuous high ACH, which remove the CO₂.",
        ],
    },
    "co2-enrichment": {
        "solid": [
            "In strong light, a higher CO₂ concentration increases the photosynthesis of C3 plants, for example cannabis.",
            "Inject CO₂ only when the light is on. Measure the CO₂ with NDIR sensors. The occupational limits are approximately 5,000, 30,000 and 40,000 ppm.",
            "A sealed room keeps the CO₂ enrichment. Exhaust removes it.",
        ],
        "operational": [
            "Enrichment ranges of 1,000 to 1,500 ppm, and CO₂ from bottles, as the standard procedure in a sealed room.",
            "Methods of air exchange in the dark period and of ethylene control.",
        ],
        "provisional": [
            "One percentage of yield increase for all rooms. The genetics, the light and the quality of the seal have the largest effect.",
            "Maximum CO₂ values in percent for a drying room, as facts with no measurement. Measure your room.",
            "Percentage increases for tomato in a greenhouse, with the same values (1:1) for cannabis flower.",
        ],
    },
    "scaling-high-light": {
        "solid": [
            "When you increase the PPFD, the plant uses more water and nutrients, and the heat load increases. Frequently the plant also uses more CO₂.",
            "The yield of the canopy can continue to increase at PPFD values higher than the saturation point of one leaf.",
        ],
        "operational": [
            "Ladder tables as engineering guides to the size of the equipment, in rooms with strong control.",
        ],
        "provisional": [
            "Ladder tables with a very high runoff EC and feed EC as start values for a new grower.",
            "Formulas that multiply the PPFD by a constant to find the quantity of water, with no data on VPD, LAI or CO₂.",
        ],
    },
    "substrates-overview": {
        "solid": [
            "Air-filled porosity and water-holding capacity are different for each type of medium.",
            "Soil is a buffer for pH and nutrients. Inert media are not buffers.",
        ],
        "operational": [
            "Easy methods for a new grower to select a medium for tolerance of errors or for control.",
        ],
        "provisional": [
            "The pH of a living soil corrects automatically in a small number of minutes, for all types of water.",
            "One percentage of air-filled porosity (AFP) for all rockwool products.",
        ],
    },
    "water-quality": {
        "solid": [
            "Alkalinity is not the same as hardness. For removal methods, chloramine is not the same as free chlorine.",
            "The saturation of dissolved oxygen (DO) decreases gradually when the temperature increases. Warm systems with a low O₂ content increase the risk of root disease.",
        ],
        "operational": [
            "Threshold values for the decision to use RO, and a procedure to calculate the EC of the source water (mS/cm) in the feed.",
        ],
        "provisional": [
            "One feed maximum of 800 to 900 ppm for all ppm scales and all stages.",
            "Threshold values of chlorine damage from lettuce as mandatory limits for cannabis.",
        ],
    },
    "ph-management": {
        "solid": [
            "The pH controls which nutrients are available to the plant. A lockout can show the same symptoms as a deficiency.",
            "In soilless media, the best pH values are approximately from the middle of the 5s to the middle of the 6s. In soil, the range is higher and wider.",
        ],
        "operational": [
            "Control of the feed pH, and the usual procedure for a two-point calibration of the pH meter.",
        ],
        "provisional": [
            "Chemical information at low pH from basil or lettuce for cannabis, with no cannabis data.",
            "A runoff EC that is always a maximum of 10% different from the feed EC. In steering, the operator can select a higher root-zone EC.",
        ],
    },
    "nutrient-mixing-athena": {
        "solid": [
            "When you keep part A and part B apart, calcium does not make a precipitate with sulfate or phosphate.",
            "The method to calculate the concentration of the stock solution, for procedures with a specified bag of fertilizer in a specified volume of water.",
        ],
        "operational": [
            "The Athena Pro Line procedure with stock solutions and doses, as one commercial system of many.",
        ],
        "provisional": [
            "A table of doses from a different manufacturer, with no check of the table with your meter and your water.",
        ],
    },
    "nutrient-deficiencies": {
        "solid": [
            "The position of a symptom on the plant, for a mobile nutrient or an immobile nutrient, is a good first step to find the cause.",
            "A pH lockout, too much water and light stress can show the same symptoms as nutrient problems.",
        ],
        "operational": [
            "Guides to the symptoms of N, P, K, Mg, Ca and Fe on cannabis.",
        ],
        "provisional": [
            "A visual identification of the problem as a result that is as sure as a laboratory test, with no test of tissue or substrate.",
            "An atlas of micronutrients with missing parts. Be more careful with Zn, B, Mn, Cu and Mo.",
        ],
    },
    "mould-risk": {
        "solid": [
            "Botrytis occurs more frequently when the humidity is high, the tissue has a high density and the air exchange is low.",
            "The RH in the canopy can be higher than the readings of the room sensors.",
        ],
        "operational": [
            "Procedures to decrease the RH in steps in the last stage of flowering, and procedures to put a bag on the rot and cut it.",
        ],
        "provisional": [
            "One RH range of 60 to 70% in flowering as a safe target for the last stage of flowering.",
            "Values of relative risk from claims data, with no absolute rates. The group of persons with a weak immune system stays at high risk.",
        ],
    },
    "auckland-ipm-blueprint": {
        "solid": [
            "The structure of exclusion, clean stock, monitoring and CAPA.",
            "In the NZ pathway, the approval status of a product is not the same as the fact that a person used the product one time.",
        ],
        "operational": [
            "Threshold models and controls for the mother room, as SOPs of the facility.",
        ],
        "provisional": [
            "The approval status of a specified product or organism, with no check of the register at this time.",
            "Figures that an AI system makes, as a method to make sure of the identification of a pest. The figures are only aids for training.",
        ],
    },
    "ipm-sop": {
        "solid": [
            "The IPM hierarchy is prevent, monitor, soft controls and hard controls.",
            "The rate on the label and the legal status of a product control each spray.",
        ],
        "operational": [
            "Intervals for scouting and examples of action thresholds.",
        ],
        "provisional": [
            "Rates for pesticides in kitchen volumes. Do not use them. Use only the rate on the label.",
            "A limit of day 21 for foliar sprays as a general fact. The limit is a quality SOP and not a regulation for all areas.",
            "Biocontrol agents that a grower thinks you can use in all countries.",
        ],
    },
    "pest-id": {
        "solid": [
            "Before you apply a treatment, use a loupe or microscope to identify the pest. Different pests can be almost the same visually.",
            "If you know the life cycle of the pest, you can select the correct time for each control.",
        ],
        "operational": [
            "The signs of frequent cannabis pests on plants, and the biocontrol agent for each pest where you can use it.",
        ],
        "provisional": [
            "Very short life-cycle times (for example, a life cycle of 3 days) as typical times. These times occur only in conditions that are very hot and dry.",
            "Estimates for the density of sticky traps as the best values that tests show.",
        ],
    },
    "pppe": {
        "solid": [
            "Persons are a primary vector of contamination. HpLVd can move on tools and on hands.",
            "The log reductions for hand hygiene use a log scale. In test conditions, they are approximately 90%, 99% and 99.9%.",
            "The flow of personnel is from clean to dirty areas. The flow of waste is from dirty areas to the exit.",
        ],
        "operational": [
            "The sequence of gowning, and models with two kits, for cultivation and for post-harvest.",
            "The NZ HSWA structure for PPE, where it is applicable.",
        ],
        "provisional": [
            "One value of 70 to 90% for the part of cleanroom contamination that persons cause, as a constant for all conditions.",
            "The contamination of a phone compared with a toilet seat, as an accurate measure of biosecurity.",
        ],
    },
    "root-zone-teros12": {
        "solid": [
            "Capacitance probes calculate the VWC from the permittivity. The calibration for the medium is important.",
            "The estimate of pore-water EC has limits, as for the Hilhorst model and models of the same type.",
        ],
        "operational": [
            "The depth of the installation, the volume of influence, and the usual positions of probes in many pots.",
        ],
        "provisional": [
            "The accuracy values of the manufacturer as values that you always get with no calibration for your medium.",
        ],
    },
    "smart-watering-vrwe": {
        "solid": [
            "One moisture probe can give an incorrect reading. A check of more than one signal is good engineering.",
        ],
        "operational": [
            "Sensor fusion of the VRWE type, as a safety structure for automatic irrigation.",
        ],
        "provisional": [
            "A system that, in all failure modes, always applies a sufficient quantity of water and does not apply too much water.",
            "Transpiration proxies as accurate models of the quantity of water that the crop uses, with no crop coefficients.",
        ],
    },
    "signal-and-noise": {
        "solid": [
            "Control charts and filters decrease the number of false alarms. Sensors have noise.",
        ],
        "operational": [
            "The sampling interval and the deadbands for automation in the grow room.",
        ],
        "provisional": [
            "One percentage of alerts that are noise, from standards of the process industry, with no rate that you measured.",
            "The names of the Western Electric rules and the Nelson rules in one mixture, with no reference to a source.",
        ],
    },
    "closed-loop": {
        "solid": [
            "A loop that operates, measures, compares and adjusts is correct control theory.",
            "Do not adjust one climate value at a time, because the climate values have an effect on each other.",
        ],
        "operational": [
            "Typical structures of the dashboard and of the automation for rooms.",
        ],
        "provisional": [
            "Sure values of the time before tipburn, from data on other crops and not from cannabis.",
            "A time of less than five seconds to know the condition of all the room, as performance that tests show in horticulture.",
        ],
    },
    "plant-state-dashboard": {
        "solid": [
            "A display of the plant state is better for operators than a display of many raw sensor readings.",
        ],
        "operational": [
            "UX structures and examples of advisories.",
        ],
        "provisional": [
            "An estimate on the screen of a problem that will occur (for example, tipburn in 48 h) as a model that tests show is correct.",
        ],
    },
    "f2-crop-steering": {
        "solid": [
            "An emergency stop and a procedure to disarm the system are different. This difference is correct for the safety of the system.",
            "Irrigation that a sensor controls must use a calibrated VWC, and not the percentage that the sensor gives with no calibration for the medium.",
        ],
        "operational": [
            "Phase machines and structures of entities in Home Assistant, for one type of facility.",
        ],
        "provisional": [
            "The VWC values that the system has at the start as correct values for all substrates.",
            "The Caplan drought as a full test that one P0–P3 procedure is correct.",
        ],
    },
    "irrigation-manual": {
        "solid": [
            "If the system has no safety sensors, do not operate it when no person monitors it.",
            "Vegetative growth uses smaller controlled drybacks. Generative growth uses larger controlled drybacks.",
        ],
        "operational": [
            "Procedures for installation and servicing of a manifold that sensors control.",
        ],
        "provisional": [
            "The entity names and setpoints of a different facility in your facility with no change.",
        ],
    },
    "plant-biosignal-sensor": {
        "solid": [
            "Plants make biopotentials that you can measure. Noise at the electrode is an important problem in engineering.",
        ],
        "operational": [
            "A DIY hobby system with an AD8232 and ESPHome to record data.",
        ],
        "provisional": [
            "The estimate of NPK, of the irrigation that is necessary, or of the stress condition, from only the signal in millivolts of a DIY system.",
            "The outputs of models of commercial products that you make again without the trained library of the product.",
            "Papers on the classification of emotional states for decisions about cultivation.",
        ],
    },
    "facility-3d": {
        "solid": [
            "The cost to correct a layout clash that you find in CAD is less than the cost to correct a clash in concrete.",
        ],
        "operational": [
            "A procedure with a 3D model to make the layout of the rooms, the doors and the floor area of the equipment.",
        ],
        "provisional": [
            "Examples from the WAC and the IBC as the conditions of your local license.",
            "A model as an engineering approval or as an approval for fire safety and life safety.",
        ],
    },
    "daily-checks": {
        "solid": [
            "Checklists increase the reliability of a procedure in work with a high risk.",
        ],
        "operational": [
            "A hybrid method for cultivation facilities: HA auto-tick and a walk-around.",
        ],
        "provisional": [
            "A smaller number of deaths in surgery as data that the yield of cannabis increases.",
            "Home Assistant logs as audit systems for GxP and GACP with no validation of the system.",
            "Effect sizes of 2 to 3 times for implementation intentions, with no base rates.",
        ],
    },
}


def get(slug: str) -> dict:
    d = PAPERS.get(slug)
    if not d:
        return DEFAULT
    # merge defaults for empty tiers
    out = {
        "solid": list(d.get("solid") or DEFAULT["solid"]),
        "operational": list(d.get("operational") or DEFAULT["operational"]),
        "provisional": list(d.get("provisional") or DEFAULT["provisional"]),
    }
    return out


def panel_html(slug: str) -> str:
    """Full evidence panel HTML for injection into a paper."""
    if slug == "slab-irrigation-strategy":
        return """<div class="evidence-panel"><p>The sources are journal papers, manufacturer instructions and grower reports. The product instructions are for the specified products. The irrigation procedures in the reports are for the facilities in the paper.</p><p><strong>CORPUS / INFERRED:</strong> the diagrams, the calculated examples and the assembled irrigation ranges are only for information. <strong>OPERATIONAL:</strong> controller values must come from a specified local procedure or from a measured crop record. This paper gives no setpoints that are correct for your location.</p></div>"""
    e = get(slug)
    def lis(items):
        return "<ul class='ev-list'>" + "".join(f"<li>{x}</li>" for x in items) + "</ul>"

    issues = (
        "https://github.com/JakeTheRabbit/cannabis-white-papers/issues/new"
        "?title=Accuracy%20report%3A%20" + slug +
        "&body=Paper%3A%20" + slug + "%0A%0AIncorrect%20information%3A%0A%0ACorrect%20information%20and%20the%20source%2C%20if%20you%20have%20one%3A%0A"
    )

    return (
        "<div class='evidence-panel'>"
        "<div class='evidence-h'>"
        "<div class='evidence-kicker'>Three types of information</div>"
        "<p class='evidence-lead'>We want each paper to be correct. Thus we <strong>examine each paper</strong> for information that is not solid. "
        "This information comes from the view of one grower, from a small number of sources, or from grower "
        "methods that have no controlled test. We <strong>identify</strong> this information, and we do not show it "
        "as solid.</p>"
        "<p class='evidence-lead'>Frequently there is no paper for the decision that you must make. Then we use the "
        "reports of other growers and the methods that work in the rooms that we know. This information can help you, "
        "but it is not the result of a laboratory test. <strong>Use the methods that work for your plants, for your room "
        "and for your meters.</strong> If a table does not agree with your crop, use the data from your crop and record "
        "the difference.</p>"
        "</div>"
        "<div class='evidence-grid'>"
        "<div class='evidence-col solid'>"
        "<div class='evidence-badge'>Solid</div>"
        "<div class='evidence-sub'>Tests of plants, specifications or many sources that agree show that the information is correct</div>"
        + lis(e["solid"]) +
        "</div>"
        "<div class='evidence-col operational'>"
        "<div class='evidence-badge'>Grower method</div>"
        "<div class='evidence-sub'>Many growers use this method in their rooms. Start with it, then change it for your room.</div>"
        + lis(e["operational"]) +
        "</div>"
        "<div class='evidence-col provisional'>"
        "<div class='evidence-badge'>Weak</div>"
        "<div class='evidence-sub'>The view of one grower, a small number of sources, one test, or a method that works in one room</div>"
        + lis(e["provisional"]) +
        "</div></div><p class='evidence-foot'><strong>If you find an error, make a report.</strong> "
        "We will correct it. Make the report on GitHub, with the name of the paper and the "
        f"information that is incorrect. If you have a source, include it: <a href='{issues}' "
        "target='_blank' rel='noopener'>Make a report of an accuracy problem</a>. The regulations, "
        "labels and licenses of your area always override each procedure in these papers. The label "
        "<span class='ev-tag'>weak</span> in a paper shows the points where the risk of an error is "
        "highest.</p></div>"
    )


def community_note(body: str, title: str = "Weak") -> str:
    """Inline provisional callout (used from papers or build)."""
    from components import callout
    return callout("evidence", title, f"<p>{body}</p>")
