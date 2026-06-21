# -*- coding: utf-8 -*-
"""Site navigation manifest. Drives sidebar, mobile drawer, landing grid, search."""

# Top-level links (above the grouped paper list)
TOP = [
    {"slug": "index",      "title": "Home",      "icon": "home"},
    {"slug": "curriculum", "title": "Start here", "icon": "seedling"},
    {"slug": "papers",     "title": "All papers", "icon": "grid"},
    {"slug": "glossary",   "title": "Glossary",   "icon": "book"},
]

# Paper groups. status: "live" (built) | "soon" (planned, shown greyed in nav)
GROUPS = [
    {"group": "Start here · beginner", "items": [
        {"slug": "tissue-culture",   "title": "Tissue culture",       "short": "Clean up genetics from a speck of tissue", "icon": "spark",   "status": "live", "track": "Beginner"},
        {"slug": "coco-crop-steering", "title": "Coco & crop steering", "short": "Precision watering in coir",              "icon": "droplet", "status": "live", "track": "Beginner"},
        {"slug": "grow-room-systems", "title": "Grow-room systems",    "short": "The whole room as one system",           "icon": "building", "status": "live", "track": "Beginner"},
        {"slug": "airflow-design",    "title": "Airflow design",       "short": "Move air like the pros",                 "icon": "wind",    "status": "live", "track": "Beginner"},
        {"slug": "mould-risk",        "title": "Mould risk",           "short": "Spot and stop bud rot",                  "icon": "shield",  "status": "live", "track": "Beginner"},
    ]},
    {"group": "Foundations & fundamentals", "items": [
        {"slug": "seeds-germination",    "title": "Seeds & germination",     "short": "Pop seeds and raise seedlings",     "icon": "seedling", "status": "soon", "track": "Foundations"},
        {"slug": "lighting-fundamentals","title": "Lighting fundamentals",   "short": "Spectrum, PPFD & DLI",             "icon": "sun",      "status": "soon", "track": "Foundations"},
        {"slug": "substrates-overview",  "title": "Substrates compared",     "short": "Coco, rockwool, soil, hydro",       "icon": "leaf",     "status": "soon", "track": "Foundations"},
        {"slug": "water-quality",        "title": "Water quality",           "short": "Source water, RO & alkalinity",     "icon": "droplet",  "status": "soon", "track": "Foundations"},
        {"slug": "ph-management",        "title": "pH management",           "short": "Hold pH, avoid lockout",            "icon": "beaker",   "status": "soon", "track": "Foundations"},
        {"slug": "nutrient-deficiencies","title": "Deficiency diagnosis",    "short": "Read the leaves, fix the feed",     "icon": "leaf",     "status": "soon", "track": "Foundations"},
        {"slug": "flowering-stages",     "title": "Flower week by week",     "short": "The flip to harvest",              "icon": "spark",    "status": "soon", "track": "Foundations"},
        {"slug": "pest-id",              "title": "Pest ID & control",       "short": "Mites, thrips, gnats and more",     "icon": "shield",   "status": "soon", "track": "Foundations"},
    ]},
    {"group": "Grow craft & post-harvest", "items": [
        {"slug": "cloning",               "title": "Cloning",               "short": "Cuttings that root every time",    "icon": "seedling", "status": "soon", "track": "Craft"},
        {"slug": "nutrient-mixing-athena", "title": "Mixing Athena nutrients", "short": "Salts, in metric, done right",     "icon": "beaker",  "status": "soon", "track": "Craft"},
        {"slug": "light-acclimation",     "title": "Light acclimation",     "short": "Ramp light without bleaching",     "icon": "sun",     "status": "soon", "track": "Craft"},
        {"slug": "defoliation-training",  "title": "Defoliation & training", "short": "Train the canopy for yield",       "icon": "scissors", "status": "soon", "track": "Craft"},
        {"slug": "ipm-sop",               "title": "IPM: pest management",   "short": "Scout, decide, act",              "icon": "shield",  "status": "soon", "track": "Craft"},
        {"slug": "harvest-dry-trim-cure", "title": "Harvest, dry, trim, cure","short": "The whole post-harvest process",   "icon": "leaf",    "status": "soon", "track": "Craft"},
    ]},
    {"group": "Precision & sensors", "items": [
        {"slug": "root-zone-teros12",  "title": "Root-zone state · TEROS-12", "short": "What the sensor really sees",      "icon": "gauge",    "status": "soon", "track": "Precision"},
        {"slug": "smart-watering-vrwe", "title": "Smart watering · VRWE",     "short": "The watering brain, plain English", "icon": "dashboard", "status": "soon", "track": "Precision"},
        {"slug": "signal-and-noise",   "title": "Signal & noise",           "short": "Precision cultivation",            "icon": "wave",     "status": "soon", "track": "Precision"},
        {"slug": "closed-loop",        "title": "The closed loop",          "short": "Levers, signal & plant state",     "icon": "loop",     "status": "soon", "track": "Precision"},
        {"slug": "plant-state-dashboard","title": "Plant-state dashboard",   "short": "From telemetry to intelligence",   "icon": "dashboard", "status": "soon", "track": "Precision"},
        {"slug": "f2-crop-steering",   "title": "F2 crop steering",         "short": "The daily P0–P3 cycle",            "icon": "gauge",    "status": "soon", "track": "Precision"},
        {"slug": "irrigation-manual",  "title": "Irrigation manual",        "short": "Install and run the system",       "icon": "droplet",  "status": "soon", "track": "Precision"},
    ]},
    {"group": "Facility & GMP", "items": [
        {"slug": "gmp-hash-lab",      "title": "GMP hash lab",           "short": "Facility flow & quality control",    "icon": "flask",   "status": "soon", "track": "Facility"},
        {"slug": "facility-3d",       "title": "3D facility model",      "short": "See the build before you build it",   "icon": "building", "status": "soon", "track": "Facility"},
        {"slug": "wso-quality-manual", "title": "WSO quality manual",     "short": "GMP quality management system",       "icon": "doc",     "status": "soon", "track": "Facility"},
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
