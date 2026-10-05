# -*- coding: utf-8 -*-
"""Site navigation manifest. Drives sidebar, mobile drawer, landing grid, search."""

# Top-level links (above the grouped paper list)
TOP = [
    {"slug": "index",      "title": "Home",      "icon": "home"},
    {"slug": "curriculum", "title": "Start here", "icon": "seedling"},
    {"slug": "papers",     "title": "All papers", "icon": "grid"},
    {"slug": "glossary",   "title": "Glossary",   "icon": "book"},
]

# Paper groups, ordered by where the task sits in a grow. status: "live" | "soon".
GROUPS = [
    {"group": "Propagation", "items": [
        {"slug": "seeds-germination",  "title": "Seeds and germination",  "short": "Germinate seeds and keep the seedlings in good condition",            "icon": "seedling", "status": "live", "track": "Propagation"},
        {"slug": "cloning",            "title": "Cloning",              "short": "Cuttings that make roots each time",            "icon": "seedling", "status": "live", "track": "Propagation"},
        {"slug": "tissue-culture",     "title": "Tissue culture",       "short": "Clean genetics from a small piece of tissue", "icon": "spark",    "status": "live", "track": "Propagation"},
        {"slug": "cannabis-tissue-culture-playbook", "title": "TC method", "short": "All the steps of cannabis tissue culture", "icon": "flask", "status": "live", "track": "Propagation"},
        {"slug": "cannabis-tissue-culture-sop", "title": "TC SOP", "short": "Tasks, record sheets and a low-cost hood from China", "icon": "doc", "status": "live", "track": "Propagation"},
        {"slug": "transplanting",      "title": "Transplanting",        "short": "Move plants to larger pots and prevent slow growth",        "icon": "seedling", "status": "live", "track": "Propagation"},
        {"slug": "mother-plants",      "title": "Mother plants",        "short": "Stock plants, HpLVd control and replacement", "icon": "seedling", "status": "live", "track": "Propagation"},
    ]},
    {"group": "Vegetative growth", "items": [
        {"slug": "light-acclimation",    "title": "Light acclimation",     "short": "Increase light in steps and prevent damage to leaves",   "icon": "sun",      "status": "live", "track": "Veg"},
        {"slug": "defoliation-training", "title": "Defoliation and training", "short": "Canopy training for more yield",     "icon": "scissors", "status": "live", "track": "Veg"},
        {"slug": "veg-management",       "title": "Vegetative stage length",  "short": "Length from the number of plants, pot size and canopy area", "icon": "leaf", "status": "live", "track": "Veg"},
    ]},
    {"group": "Flowering", "items": [
        {"slug": "flowering-stages",   "title": "Flower week by week",  "short": "From the start of flowering to harvest",       "icon": "spark",   "status": "live", "track": "Flower"},
        {"slug": "coco-crop-steering", "title": "Coco and crop steering", "short": "Use water to control the plant",      "icon": "droplet", "status": "live", "track": "Flower"},
        {"slug": "rockwool-crop-steering", "title": "Rockwool and crop steering", "short": "Drybacks, saturation and the lowest safe water content", "icon": "droplet", "status": "live", "track": "Flower"},
        {"slug": "one-steering-law", "title": "One steering law", "short": "The same crop steering for coco, rockwool, soil and water", "icon": "droplet", "status": "live", "track": "Flower"},
        {"slug": "slab-irrigation-strategy", "title": "Slab irrigation", "short": "Blocks on slabs, from the first roots to harvest", "icon": "droplet", "status": "live", "track": "Flower"},
        {"slug": "ripening-harvest-timing", "title": "Ripening and harvest", "short": "Trichome checks, when to flush, and the harvest decision", "icon": "spark", "status": "live", "track": "Flower"},
    ]},
    {"group": "Harvest, dry, trim and cure", "items": [
        {"slug": "harvest-dry-trim-cure", "title": "Harvest, dry, trim, cure", "short": "All the steps after harvest", "icon": "leaf",  "status": "live", "track": "Harvest"},
        {"slug": "gmp-hash-lab",          "title": "GMP hash lab",             "short": "Make concentrate from flower", "icon": "flask", "status": "live", "track": "Harvest"},
        {"slug": "hash-rosin-pressing",   "title": "Hash rosin",      "short": "Heat, pressure, time and the micron screen", "icon": "flask", "status": "live", "track": "Harvest"},
        {"slug": "lab-testing-coas",      "title": "Lab testing and COAs",       "short": "Read a COA: calculate potency, know methods and limits", "icon": "flask", "status": "live", "track": "Harvest"},
    ]},
    {"group": "Environment and climate", "items": [
        {"slug": "grow-room-systems",    "title": "Grow room systems",     "short": "The grow room as one system",  "icon": "building", "status": "live", "track": "Environment"},
        {"slug": "lighting-fundamentals","title": "Basic lighting", "short": "Spectrum, PPFD and DLI",          "icon": "sun",      "status": "live", "track": "Environment"},
        {"slug": "airflow-design",       "title": "Airflow and fans",        "short": "How much air to move, and where to put the fans",        "icon": "wind",     "status": "live", "track": "Environment"},
        {"slug": "under-canopy-lighting","title": "Under-canopy lighting",  "short": "Photons at the floor: SCL and ICL",  "icon": "sun",      "status": "live", "track": "Environment"},
        {"slug": "co2-enrichment",       "title": "CO2 enrichment",        "short": "Supply carbon dioxide to the plant, safely", "icon": "spark",    "status": "live", "track": "Environment"},
        {"slug": "scaling-high-light",   "title": "Higher light levels", "short": "Find the supply that is the limit, then adjust the light", "icon": "gauge",  "status": "live", "track": "Environment"},
        {"slug": "temp-humidity-vpd",    "title": "Temperature, humidity and VPD",  "short": "Leaf VPD, dew point and targets for each stage",  "icon": "wave",   "status": "live", "track": "Environment"},
        {"slug": "hvac-dehumidification","title": "HVAC and dehumidifiers",  "short": "Heat load and vapor load, and the size of the equipment", "icon": "wind", "status": "live", "track": "Environment"},
    ]},
    {"group": "Water, substrate and feed", "items": [
        {"slug": "substrates-overview",  "title": "Substrates compared",     "short": "Coco, rockwool, soil and hydro",   "icon": "leaf",    "status": "live", "track": "Feed"},
        {"slug": "deep-water-culture",   "title": "Deep water culture",      "short": "Oxygen, ORP and the reservoir",   "icon": "droplet", "status": "live", "track": "Feed"},
        {"slug": "water-quality",        "title": "Water quality",           "short": "Source water, RO and alkalinity", "icon": "droplet", "status": "live", "track": "Feed"},
        {"slug": "ph-management",        "title": "pH control",           "short": "Keep pH in range for nutrient uptake",        "icon": "beaker",  "status": "live", "track": "Feed"},
        {"slug": "nutrient-mixing-athena","title": "Mix nutrients",       "short": "Mix salts correctly, in liters and kilograms",  "icon": "beaker",  "status": "live", "track": "Feed"},
        {"slug": "nutrient-deficiencies","title": "Nutrient deficiencies",    "short": "Read the leaves and change the feed", "icon": "leaf",    "status": "live", "track": "Feed"},
    ]},
    {"group": "Plant health", "items": [
        {"slug": "auckland-ipm-blueprint", "title": "Auckland medicinal IPM", "short": "Clean stock, NZ regulations, pest profiles and CAPA", "icon": "shield", "status": "live", "track": "Health"},
        {"slug": "mould-risk", "title": "Mold risk",        "short": "Find and stop bud rot",        "icon": "shield", "status": "live", "track": "Health"},
        {"slug": "ipm-sop",    "title": "IPM SOP","short": "Examine the crop, make a decision, apply a treatment",           "icon": "shield", "status": "live", "track": "Health"},
        {"slug": "pest-id",    "title": "Pest ID and control",  "short": "Mites, thrips, gnats and more", "icon": "shield", "status": "live", "track": "Health"},
        {"slug": "pppe",       "title": "PPE and biosecurity",  "short": "Gowns, gloves and clean personnel", "icon": "shield", "status": "live", "track": "Health"},
    ]},
    {"group": "Precision and automation", "items": [
        {"slug": "root-zone-teros12",  "title": "Root-zone condition · TEROS-12", "short": "How to read the values from the sensor",      "icon": "gauge",     "status": "live", "track": "Precision"},
        {"slug": "smart-watering-vrwe", "title": "Irrigation control · VRWE",     "short": "How the controller makes irrigation decisions", "icon": "dashboard", "status": "live", "track": "Precision"},
        {"slug": "signal-and-noise",   "title": "Signal and noise",           "short": "Find the difference between plant changes and sensor noise",      "icon": "wave",      "status": "live", "track": "Precision"},
        {"slug": "closed-loop",        "title": "The closed loop",          "short": "Levers, signals and plant state",     "icon": "loop",      "status": "live", "track": "Precision"},
        {"slug": "plant-state-dashboard","title": "Plant state dashboard",   "short": "From sensor data to a decision",   "icon": "dashboard", "status": "live", "track": "Precision"},
        {"slug": "f2-crop-steering",   "title": "F2 crop steering",         "short": "The P0-P3 cycle for each day",            "icon": "gauge",     "status": "live", "track": "Precision"},
        {"slug": "irrigation-manual",  "title": "Irrigation manual",        "short": "Install and operate the system",       "icon": "droplet",   "status": "live", "track": "Precision"},
        {"slug": "plant-biosignal-sensor", "title": "DIY plant-biosignal sensor", "short": "Read the electrical signals of a plant. Cost: approximately NZ$110", "icon": "wave", "status": "live", "track": "Precision"},
    ]},
    {"group": "Facility and quality", "items": [
        {"slug": "facility-3d",       "title": "3D facility model",  "short": "See the facility in 3D before you make it", "icon": "building", "status": "live", "track": "Facility"},
        {"slug": "daily-checks",       "title": "Checks each day",       "short": "Facility checks where sensors do most of the work", "icon": "dashboard", "status": "live", "track": "Facility"},
        {"slug": "compliance-track-trace", "title": "Compliance and traceability", "short": "Licenses and batch records, from mother plant to lot", "icon": "shield", "status": "live", "track": "Facility"},
        {"slug": "energy-sustainability", "title": "Energy and utilities",    "short": "Where the kWh go and how to use less energy",  "icon": "spark",  "status": "live", "track": "Facility"},
        {"slug": "unit-economics",     "title": "Yield and unit cost", "short": "Three methods to measure yield, and the cost of a gram", "icon": "gauge", "status": "live", "track": "Facility"},
    ]},
    {"group": "Know the plant", "items": [
        {"slug": "plant-biology",         "title": "Plant biology 101",     "short": "Plant parts, life cycle, photoperiod and hormones", "icon": "leaf",     "status": "live", "track": "Reference"},
        {"slug": "cannabinoids-terpenes", "title": "Cannabinoids and terpenes",    "short": "From the gland to the COA", "icon": "flask",    "status": "live", "track": "Reference"},
        {"slug": "genetics-phenohunting", "title": "Genetics and phenohunt", "short": "Seed genetics, selection and the phenohunt", "icon": "seedling", "status": "live", "track": "Reference"},
    ]},
]

def all_items():
    out = []
    for g in GROUPS:
        for it in g["items"]:
            out.append(it)
    return out

def find(slug):
    for it in all_items():
        if it["slug"] == slug:
            return it
    return None
