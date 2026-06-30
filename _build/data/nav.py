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
        {"slug": "seeds-germination",  "title": "Seeds & germination",  "short": "Pop seeds and raise seedlings",            "icon": "seedling", "status": "live", "track": "Propagation"},
        {"slug": "cloning",            "title": "Cloning",              "short": "Cuttings that root every time",            "icon": "seedling", "status": "live", "track": "Propagation"},
        {"slug": "tissue-culture",     "title": "Tissue culture",       "short": "Clean up genetics from a speck of tissue", "icon": "spark",    "status": "live", "track": "Propagation"},
    ]},
    {"group": "Vegetative growth", "items": [
        {"slug": "light-acclimation",    "title": "Light acclimation",     "short": "Ramp light without bleaching",   "icon": "sun",      "status": "live", "track": "Veg"},
        {"slug": "defoliation-training", "title": "Defoliation & training", "short": "Train the canopy for yield",     "icon": "scissors", "status": "live", "track": "Veg"},
    ]},
    {"group": "Flowering", "items": [
        {"slug": "flowering-stages",   "title": "Flower week by week",  "short": "The flip through to ripe",       "icon": "spark",   "status": "live", "track": "Flower"},
        {"slug": "coco-crop-steering", "title": "Coco & crop steering", "short": "Steer the plant with water",      "icon": "droplet", "status": "live", "track": "Flower"},
        {"slug": "rockwool-crop-steering", "title": "Rockwool & crop steering", "short": "Drybacks, saturation, the breaking point", "icon": "droplet", "status": "live", "track": "Flower"},
        {"slug": "one-steering-law", "title": "The one steering law", "short": "Coco, rockwool, soil and water, one way to steer", "icon": "droplet", "status": "live", "track": "Flower"},
    ]},
    {"group": "Harvest, dry, trim & cure", "items": [
        {"slug": "harvest-dry-trim-cure", "title": "Harvest, dry, trim, cure", "short": "The whole post-harvest run", "icon": "leaf",  "status": "live", "track": "Harvest"},
        {"slug": "gmp-hash-lab",          "title": "GMP hash lab",             "short": "Turn flower into concentrate", "icon": "flask", "status": "live", "track": "Harvest"},
    ]},
    {"group": "Environment & climate", "items": [
        {"slug": "grow-room-systems",    "title": "Grow-room systems",     "short": "The whole room as one system",  "icon": "building", "status": "live", "track": "Environment"},
        {"slug": "lighting-fundamentals","title": "Lighting fundamentals", "short": "Spectrum, PPFD & DLI",          "icon": "sun",      "status": "live", "track": "Environment"},
        {"slug": "airflow-design",       "title": "Airflow design",        "short": "Move air like the pros",        "icon": "wind",     "status": "live", "track": "Environment"},
        {"slug": "under-canopy-lighting","title": "Under-canopy lighting",  "short": "Photons at the floor: SCL & ICL",  "icon": "sun",      "status": "live", "track": "Environment"},
    ]},
    {"group": "Water, substrate & feed", "items": [
        {"slug": "substrates-overview",  "title": "Substrates compared",     "short": "Coco, rockwool, soil, hydro",   "icon": "leaf",    "status": "live", "track": "Feed"},
        {"slug": "water-quality",        "title": "Water quality",           "short": "Source water, RO & alkalinity", "icon": "droplet", "status": "live", "track": "Feed"},
        {"slug": "ph-management",        "title": "pH management",           "short": "Hold pH, avoid lockout",        "icon": "beaker",  "status": "live", "track": "Feed"},
        {"slug": "nutrient-mixing-athena","title": "Mixing nutrients",       "short": "Salts, in metric, done right",  "icon": "beaker",  "status": "live", "track": "Feed"},
        {"slug": "nutrient-deficiencies","title": "Deficiency diagnosis",    "short": "Read the leaves, fix the feed", "icon": "leaf",    "status": "live", "track": "Feed"},
    ]},
    {"group": "Plant health", "items": [
        {"slug": "mould-risk", "title": "Mould risk",        "short": "Spot and stop bud rot",        "icon": "shield", "status": "live", "track": "Health"},
        {"slug": "ipm-sop",    "title": "IPM: pest management","short": "Scout, decide, act",           "icon": "shield", "status": "live", "track": "Health"},
        {"slug": "pest-id",    "title": "Pest ID & control",  "short": "Mites, thrips, gnats and more", "icon": "shield", "status": "live", "track": "Health"},
        {"slug": "pppe",       "title": "PPE & biosecurity",  "short": "Gowning, gloves, keeping humans clean", "icon": "shield", "status": "live", "track": "Health"},
    ]},
    {"group": "Precision & automation", "items": [
        {"slug": "root-zone-teros12",  "title": "Root-zone state · TEROS-12", "short": "What the sensor really sees",      "icon": "gauge",     "status": "live", "track": "Precision"},
        {"slug": "smart-watering-vrwe", "title": "Smart watering · VRWE",     "short": "The watering brain, plain English", "icon": "dashboard", "status": "live", "track": "Precision"},
        {"slug": "signal-and-noise",   "title": "Signal & noise",           "short": "Real signal vs sensor noise",      "icon": "wave",      "status": "live", "track": "Precision"},
        {"slug": "closed-loop",        "title": "The closed loop",          "short": "Levers, signal & plant state",     "icon": "loop",      "status": "live", "track": "Precision"},
        {"slug": "plant-state-dashboard","title": "Plant-state dashboard",   "short": "From telemetry to intelligence",   "icon": "dashboard", "status": "live", "track": "Precision"},
        {"slug": "f2-crop-steering",   "title": "F2 crop steering",         "short": "The daily P0-P3 cycle",            "icon": "gauge",     "status": "live", "track": "Precision"},
        {"slug": "irrigation-manual",  "title": "Irrigation manual",        "short": "Install and run the system",       "icon": "droplet",   "status": "live", "track": "Precision"},
    ]},
    {"group": "Facility & quality", "items": [
        {"slug": "facility-3d",       "title": "3D facility model",  "short": "See the build before you build it", "icon": "building", "status": "live", "track": "Facility"},
        {"slug": "daily-checks",       "title": "Daily checks",       "short": "The self-completing facility round", "icon": "dashboard", "status": "live", "track": "Facility"},
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
