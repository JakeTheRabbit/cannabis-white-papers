# -*- coding: utf-8 -*-
"""Auto-interlinking: concept phrase -> paper slug. The build links the first mention
of each concept in body prose to the matching paper (never self, never in headings/code/
existing links). Curated to distinctive multi-word phrases to avoid noise/mis-links."""

# slug -> phrases that should link to it (case-insensitive, whole-word)
LINK_PHRASES = {
    "tissue-culture": ["tissue culture", "micropropagation", "meristem culture", "meristem", "hop latent viroid", "HpLVd", "clean stock"],
    "coco-crop-steering": ["crop steering", "coco coir", "dryback", "field capacity", "generative steering", "vegetative steering"],
    "rockwool-crop-steering": ["rockwool crop steering", "recovery floor", "stone wool", "preferential flow", "channeling"],
    "grow-room-systems": ["grow room as one", "coupled system", "vapour pressure deficit", "VPD", "daily light integral", "DLI"],
    "airflow-design": ["airflow design", "boundary layer", "air velocity", "leaf boundary"],
    "mould-risk": ["bud rot", "botrytis", "powdery mildew", "mould risk", "water activity"],
    "root-zone-teros12": ["root-zone sensor", "capacitance sensor", "capacitance probe", "volumetric water content", "pore-water EC", "permittivity", "TEROS-12", "TEROS 12"],
    "smart-watering-vrwe": ["smart watering", "sensor fusion", "VRWE", "watering brain"],
    "signal-and-noise": ["signal and noise", "control limits", "statistical process control", "sensor noise"],
    "closed-loop": ["closed loop", "closed-loop control", "feedback loop", "setpoint"],
    "plant-state-dashboard": ["plant-state dashboard", "plant state", "telemetry"],
    "f2-crop-steering": ["P0–P3", "P0-P3", "irrigation phases", "daily irrigation cycle"],
    "irrigation-manual": ["irrigation system", "fertigation", "drip emitters", "drip lines"],
    "cloning": ["taking cuttings", "rooting hormone", "humidity dome", "clone", "cutting"],
    "nutrient-mixing-athena": ["stock tank", "stock solution", "Athena Pro Line", "nutrient mixing", "pore-water", "electrical conductivity"],
    "light-acclimation": ["light acclimation", "photoinhibition", "light bleaching", "PPFD ramp", "PPFD"],
    "defoliation-training": ["defoliation", "plant training", "lollipopping", "low-stress training", "SCROG", "trellis"],
    "ipm-sop": ["integrated pest management", "IPM", "scouting", "biological control", "action threshold"],
    "harvest-dry-trim-cure": ["harvest", "drying", "curing", "trimming", "trichome"],
    "gmp-hash-lab": ["GMP", "cleanroom", "good manufacturing practice", "solventless", "hash"],
    "facility-3d": ["3D model", "facility design", "floor plan"],
    "wso-quality-manual": ["quality management system", "quality manual", "standard operating procedure", "batch release", "traceability"],
    "seeds-germination": ["germination", "seedling", "feminised seeds", "autoflower", "popping seeds"],
    "lighting-fundamentals": ["light spectrum", "photoperiod", "grow lights", "umol/J", "PAR"],
    "substrates-overview": ["rockwool", "living soil", "hydroponics", "air-filled porosity", "growing media"],
    "water-quality": ["water quality", "reverse osmosis", "RO water", "alkalinity", "source water", "chloramine"],
    "ph-management": ["pH lockout", "pH pen", "pH up", "pH down"],
    "nutrient-deficiencies": ["nutrient deficiency", "nutrient toxicity", "nutrient lockout", "mobile nutrients"],
    "flowering-stages": ["flowering cycle", "the stretch", "bud set", "the flip", "12/12"],
    "pest-id": ["spider mites", "russet mites", "broad mites", "thrips", "fungus gnats", "aphids"],
}

# Flat (phrase, slug) list, longest phrase first so multi-word wins over substrings.
def phrase_list():
    pairs = [(p, slug) for slug, ph in LINK_PHRASES.items() for p in ph]
    pairs.sort(key=lambda x: len(x[0]), reverse=True)
    return pairs
