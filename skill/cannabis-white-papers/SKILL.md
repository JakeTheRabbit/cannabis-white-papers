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
- **Cleaning up cannabis genetics with tissue culture** (`papers/tissue-culture.md`): Clean up genetics from a speck of tissue
- **Cannabis tissue culture, start to finish** (`papers/cannabis-tissue-culture-playbook.md`): Start-to-finish cannabis tissue culture
- **Cannabis tissue culture SOP** (`papers/cannabis-tissue-culture-sop.md`): Jobs, forms, and a cheap hood from China
- **Seeds, germination and seedlings** (`papers/seeds-germination.md`): Pop seeds and raise seedlings
- **How to root cannabis cuttings** (`papers/cloning.md`): Cuttings that root every time
- **Transplanting: potting up without the stall** (`papers/transplanting.md`): Pot up without stalling the plant
- **Mother plants: environment, feeding, pruning and pathogen defence** (`papers/mother-plants.md`): Stock plants, HpLVd control & succession

### Vegetative growth
- **Raise PPFD in steps so plants don't bleach** (`papers/light-acclimation.md`): Ramp light without bleaching
- **Defoliation and plant training for maximum yield** (`papers/defoliation-training.md`): Train the canopy for yield
- **Vegetative management: build the frame, then flip** (`papers/veg-management.md`): Size veg by count, pot and canopy, then flip

### Flowering
- **Precision coco cultivation: crop steering in coir** (`papers/coco-crop-steering.md`): Steer the plant with water
- **The flower cycle, week by week** (`papers/flowering-stages.md`): The flip through to ripe
- **Crop steering in rockwool: water content, drybacks, and the recovery floor** (`papers/rockwool-crop-steering.md`): Drybacks, saturation, the breaking point
- **One steering law: coco, rockwool, soil and water** (`papers/one-steering-law.md`): Coco, rockwool, soil and water, one way to steer
- **Slab irrigation, end to end** (`papers/slab-irrigation-strategy.md`): Blocks on slabs, rooting-in to chop
- **Ripening, flush, and harvest timing** (`papers/ripening-harvest-timing.md`): Trichome reads, flush truth, the harvest call

### Harvest, dry, trim & cure
- **Harvest, dry, trim and cure** (`papers/harvest-dry-trim-cure.md`): The whole post-harvest run
- **GMP hash lab: zones, flows, and batch release** (`papers/gmp-hash-lab.md`): Turn flower into concentrate
- **Hash rosin: heat, pressure, and a micron screen** (`papers/hash-rosin-pressing.md`): Heat, pressure, time & the micron screen
- **Lab testing, potency and the COA** (`papers/lab-testing-coas.md`): Reading COAs: potency math, methods, limits

### Environment & climate
- **Cannabis grow room: a systems guide** (`papers/grow-room-systems.md`): The whole room as one system
- **Airflow design for indoor cultivation** (`papers/airflow-design.md`): Move air like the pros
- **CO2 enrichment: feeding the plant carbon, safely** (`papers/co2-enrichment.md`): Feed the plant carbon, safely
- **Scaling light to the limiting factor** (`papers/scaling-high-light.md`): Find the limiting factor, dial to it
- **Lighting: spectrum, PPFD and DLI** (`papers/lighting-fundamentals.md`): Spectrum, PPFD & DLI
- **Under-canopy and inter-canopy lighting for indoor cannabis** (`papers/under-canopy-lighting.md`): Photons at the floor: SCL & ICL
- **Temperature, humidity and VPD: stage targets, measurement and condensation control** (`papers/temp-humidity-vpd.md`): Leaf VPD, dew point and stage bands
- **HVAC and dehumidification for grow rooms** (`papers/hvac-dehumidification.md`): Sensible vs latent: sizing the climate plant

### Water, substrate & feed
- **Substrates compared: coco, rockwool, soil, hydro** (`papers/substrates-overview.md`): Coco, rockwool, soil, hydro
- **Testing and treating source water for cannabis** (`papers/water-quality.md`): Source water, RO & alkalinity
- **pH: what it is and how to hold it** (`papers/ph-management.md`): Hold pH, avoid lockout
- **Nutrient deficiency and toxicity diagnosis** (`papers/nutrient-deficiencies.md`): Read the leaves, fix the feed
- **Dissolve Athena Pro Line powder into a 50 L stock tank** (`papers/nutrient-mixing-athena.md`): Salts, in metric, done right
- **Deep water culture, from first principles** (`papers/deep-water-culture.md`): Oxygen, ORP & the reservoir

### Plant health
- **Mould risk: preventing and stopping bud rot** (`papers/mould-risk.md`): Spot and stop bud rot
- **Integrated pest management blueprint for indoor medicinal cannabis in Auckland** (`papers/auckland-ipm-blueprint.md`): Clean stock, NZ law, atlas & CAPA
- **Pest identification and control** (`papers/pest-id.md`): Mites, thrips, gnats and more
- **Integrated pest management: a working SOP** (`papers/ipm-sop.md`): Scout, decide, act
- **PPPE: plant and personal protective equipment** (`papers/pppe.md`): Gowning, gloves, keeping humans clean

### Precision & automation
- **What your TEROS-12 measures and how to steer irrigation on it** (`papers/root-zone-teros12.md`): What the sensor really sees
- **The smart watering brain (VRWE), in plain English** (`papers/smart-watering-vrwe.md`): The watering brain, plain English
- **Tell real plant changes from sensor noise** (`papers/signal-and-noise.md`): Real signal vs sensor noise
- **Closed-loop grow room: levers, signals and plant state** (`papers/closed-loop.md`): Levers, signal & plant state
- **Designing a plant-state dashboard for your grow room** (`papers/plant-state-dashboard.md`): From telemetry to intelligence
- **F2 crop steering: the daily operating manual** (`papers/f2-crop-steering.md`): The daily P0-P3 cycle
- **Automated irrigation system manual** (`papers/irrigation-manual.md`): Install and run the system
- **Build a plant-biosignal sensor with M5Stack and ESPHome** (`papers/plant-biosignal-sensor.md`): Read a plant's electrical signals for ~NZ$110

### Facility & quality
- **Designing a grow facility in 3D before you build it** (`papers/facility-3d.md`): See the build before you build it
- **Build a daily facility check that mostly fills itself in** (`papers/daily-checks.md`): The self-completing facility round
- **Yield per watt and the cost of a gram** (`papers/unit-economics.md`): g/m², g/W, g/kWh and the true cost of a gram
- **Compliance, licensing and track-and-trace** (`papers/compliance-track-trace.md`): Licences, batch records and seed-to-sale
- **Energy, utilities and sustainability** (`papers/energy-sustainability.md`): Where the kWh go and how to spend fewer

### Know the plant
- **Genetics, seeds and the pheno hunt** (`papers/genetics-phenohunting.md`): Seed genetics, selection and the pheno hunt
- **Cannabinoids and Terpenes** (`papers/cannabinoids-terpenes.md`): Cannabinoids & terpenes, from gland to COA
- **Cannabis plant biology and the life cycle** (`papers/plant-biology.md`): Anatomy, life cycle, photoperiod, hormones

