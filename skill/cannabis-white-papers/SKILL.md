---
name: cannabis-white-papers
description: "Beginner-friendly, evidence-linked cannabis cultivation reference: 55 white papers on propagation (seeds, cloning, tissue culture), crop steering (coco, rockwool, dryback, P0-P3), environment (VPD, lighting, airflow, CO2), water and nutrition (pH, EC, substrates, Athena mixing, deficiencies), plant health (mould, IPM, pest ID, PPE and biosecurity), precision irrigation (root-zone sensors, smart watering, F2, the closed loop), and facility and quality (GMP, QMS, daily checks). Use when answering questions about growing cannabis, crop steering, irrigation, drybacks, water content, nutrients, pests, mould, environment/VPD, or cultivation facility setup; read the relevant papers/<slug>.md for detail and citations."
---

# The Cannabis White Papers

A library of 55 evidence-linked, beginner-friendly cannabis cultivation field guides. Every paper is a clean markdown file in `papers/` with sources preserved as `[^id]` footnotes.

Licensed CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/). Attribution: The Cannabis White Papers.

## How to use

1. Match the user's question to a paper below (or grep `papers/` / read `manifest.json`).
2. Read only the relevant `papers/<slug>.md` (progressive disclosure, do not load all 55).
3. Answer from it and cite the paper's footnoted sources. Look up terms in `glossary.json`.

## Papers by stage

### Propagation
- **Tissue culture for clean cannabis genetics** (`papers/tissue-culture.md`): Clean genetics from a small piece of tissue
- **Cannabis tissue culture from start to end** (`papers/cannabis-tissue-culture-playbook.md`): All the steps of cannabis tissue culture
- **Cannabis tissue culture SOP** (`papers/cannabis-tissue-culture-sop.md`): Tasks, record sheets and a low-cost hood from China
- **Seeds, germination and seedlings** (`papers/seeds-germination.md`): Germinate seeds and keep the seedlings in good condition
- **How to make roots on cannabis cuttings** (`papers/cloning.md`): Cuttings that make roots each time
- **Transplanting: how to put a plant in a larger pot without transplant shock** (`papers/transplanting.md`): Move plants to larger pots and prevent slow growth
- **Mother plants: environment, feed, pruning and protection against pathogens** (`papers/mother-plants.md`): Stock plants, HpLVd control and replacement

### Vegetative growth
- **Increase the PPFD in steps to prevent bleaching** (`papers/light-acclimation.md`): Increase light in steps and prevent damage to leaves
- **Defoliation and plant training for maximum yield** (`papers/defoliation-training.md`): Canopy training for more yield
- **The vegetative stage: make the frame, then do the flip** (`papers/veg-management.md`): Length from the number of plants, pot size and canopy area

### Flowering
- **Precision coco cultivation: crop steering in coir** (`papers/coco-crop-steering.md`): Use water to control the plant
- **The flower cycle, one week at a time** (`papers/flowering-stages.md`): From the start of flowering to harvest
- **Crop steering in rockwool: water content, drybacks, and the recovery floor** (`papers/rockwool-crop-steering.md`): Drybacks, saturation and the lowest safe water content
- **One steering law: coco, rockwool, soil and water** (`papers/one-steering-law.md`): The same crop steering for coco, rockwool, soil and water
- **Rockwool Slab Irrigation** (`papers/slab-irrigation-strategy.md`): Blocks on slabs, from the first roots to harvest
- **Ripening, flush, and the time to harvest** (`papers/ripening-harvest-timing.md`): Trichome checks, when to flush, and the harvest decision

### Harvest, dry, trim and cure
- **Harvest, drying, trimming and curing** (`papers/harvest-dry-trim-cure.md`): All the steps after harvest
- **GMP hash lab: zones, flows, and batch release** (`papers/gmp-hash-lab.md`): Make concentrate from flower
- **Hash rosin: heat, pressure and a micron screen** (`papers/hash-rosin-pressing.md`): Heat, pressure, time and the micron screen
- **Laboratory testing, potency and the COA** (`papers/lab-testing-coas.md`): Read a COA: calculate potency, know methods and limits

### Environment and climate
- **Cannabis grow room systems** (`papers/grow-room-systems.md`): The grow room as one system
- **Airflow design for indoor cultivation** (`papers/airflow-design.md`): How much air to move, and where to put the fans
- **CO2 enrichment: a safe supply of carbon to the plant** (`papers/co2-enrichment.md`): Supply carbon dioxide to the plant, safely
- **Set the light to the limiting factor** (`papers/scaling-high-light.md`): Find the supply that is the limit, then adjust the light
- **Lighting: spectrum, PPFD and DLI** (`papers/lighting-fundamentals.md`): Spectrum, PPFD and DLI
- **Under-canopy and inter-canopy lighting for cannabis in grow rooms** (`papers/under-canopy-lighting.md`): Photons at the floor: SCL and ICL
- **Temperature, humidity and VPD: stage targets, measurement and condensation control** (`papers/temp-humidity-vpd.md`): Leaf VPD, dew point and targets for each stage
- **HVAC and dehumidification for grow rooms** (`papers/hvac-dehumidification.md`): Heat load and vapor load, and the size of the equipment

### Water, substrate and feed
- **Substrates compared: coco, rockwool, soil and hydroponics** (`papers/substrates-overview.md`): Coco, rockwool, soil and hydro
- **Testing and treatment of source water for cannabis** (`papers/water-quality.md`): Source water, RO and alkalinity
- **pH: the definition and how to keep it stable** (`papers/ph-management.md`): Keep pH in range for nutrient uptake
- **Diagnosis of nutrient deficiency and toxicity** (`papers/nutrient-deficiencies.md`): Read the leaves and change the feed
- **Dissolve Athena Pro Line powder into a 50 L stock tank** (`papers/nutrient-mixing-athena.md`): Mix salts correctly, in liters and kilograms
- **Deep water culture: the basic physics and chemistry** (`papers/deep-water-culture.md`): Oxygen, ORP and the reservoir

### Plant health
- **Mold risk: how to prevent and stop bud rot** (`papers/mould-risk.md`): Find and stop bud rot
- **Integrated pest management blueprint for indoor medicinal cannabis in Auckland** (`papers/auckland-ipm-blueprint.md`): Clean stock, NZ regulations, pest profiles and CAPA
- **Pest identification and control** (`papers/pest-id.md`): Mites, thrips, gnats and more
- **Integrated pest management: an SOP** (`papers/ipm-sop.md`): Examine the crop, make a decision, apply a treatment
- **PPPE: plant and personal protective equipment** (`papers/pppe.md`): Gowns, gloves and clean personnel

### Precision and automation
- **TEROS-12 measurements and how to control irrigation with them** (`papers/root-zone-teros12.md`): How to read the values from the sensor
- **The VRWE automatic irrigation controller** (`papers/smart-watering-vrwe.md`): How the controller makes irrigation decisions
- **Find the difference between plant changes and sensor noise** (`papers/signal-and-noise.md`): Find the difference between plant changes and sensor noise
- **Closed-loop grow room: levers, signals and plant state** (`papers/closed-loop.md`): Levers, signals and plant state
- **Design of a plant-state dashboard for your grow room** (`papers/plant-state-dashboard.md`): From sensor data to a decision
- **F2 crop steering: the manual for operation each day** (`papers/f2-crop-steering.md`): The P0-P3 cycle for each day
- **Manual for an automatic irrigation system** (`papers/irrigation-manual.md`): Install and operate the system
- **Make a plant-biosignal sensor with M5Stack and ESPHome** (`papers/plant-biosignal-sensor.md`): Read the electrical signals of a plant. Cost: approximately NZ$110

### Facility and quality
- **A 3D model of a grow facility before construction** (`papers/facility-3d.md`): See the facility in 3D before you make it
- **Make a facility check for each day that completes most items automatically** (`papers/daily-checks.md`): Facility checks where sensors do most of the work
- **Yield for each watt and the cost of a gram** (`papers/unit-economics.md`): Three methods to measure yield, and the cost of a gram
- **Compliance, licensing and track-and-trace** (`papers/compliance-track-trace.md`): Licenses and batch records, from mother plant to lot
- **Energy, utilities and sustainability** (`papers/energy-sustainability.md`): Where the kWh go and how to use less energy

### Know the plant
- **Genetics, seeds and the phenotype hunt** (`papers/genetics-phenohunting.md`): Seed genetics, selection and the phenohunt
- **Cannabinoids and Terpenes** (`papers/cannabinoids-terpenes.md`): From the gland to the COA
- **Cannabis plant biology and the life cycle** (`papers/plant-biology.md`): Plant parts, life cycle, photoperiod and hormones

