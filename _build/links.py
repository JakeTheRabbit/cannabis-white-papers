# -*- coding: utf-8 -*-
"""Auto-interlinking: concept phrase -> paper slug. The build links the first mention
of each concept in body prose to the matching paper (never self, never in headings/code/
existing links). Curated to distinctive multi-word phrases to avoid noise/mis-links."""

# slug -> phrases that should link to it (case-insensitive, whole-word)
LINK_PHRASES = {
    "auckland-ipm-blueprint": ["Auckland medicinal IPM", "medicinal-cannabis input gate", "approved-input register", "rice root aphid", "Septoria leaf spot"],
    "tissue-culture": ["tissue culture", "micropropagation", "meristem culture", "meristem", "hop latent viroid", "HpLVd", "clean stock"],
    "coco-crop-steering": ["crop steering", "coco coir", "dryback", "field capacity", "generative steering", "vegetative steering"],
    "rockwool-crop-steering": ["rockwool crop steering", "recovery floor", "stone wool", "preferential flow", "channeling"],
    "slab-irrigation-strategy": ["slab irrigation", "block-on-slab", "rooting-in", "block on slab", "drain slits", "matric suction"],
    "one-steering-law": ["one steering law", "the steering law", "steering law"],
    "under-canopy-lighting": ["under-canopy lighting", "subcanopy lighting", "inter-canopy lighting", "intracanopy lighting", "photobleaching", "SCL", "ICL"],
    "grow-room-systems": ["grow room as one", "coupled system", "daily light integral", "DLI"],
    "airflow-design": ["airflow design", "boundary layer", "air velocity", "leaf boundary"],
    "co2-enrichment": ["CO2 enrichment", "CO2 supplementation", "carbon dioxide enrichment", "CO2 injection", "dark respiration", "CO2 compensation point", "photorespiration", "sealed grow room"],
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
    "gmp-hash-lab": ["GMP", "cleanroom", "good manufacturing practice", "hash lab"],
    "hash-rosin-pressing": ["hash rosin", "rosin press", "bubble hash", "dry sift", "live rosin", "solventless", "full-melt", "micron bag", "cold cure", "THCa diamonds", "rosin pressing"],
    "facility-3d": ["3D model", "facility design", "floor plan"],
    "daily-checks": ["daily checks", "daily check", "pause point", "killer item", "pencil-whipping", "action limit", "self-completing"],
    "seeds-germination": ["germination", "seedling", "feminised seeds", "autoflower", "popping seeds"],
    "lighting-fundamentals": ["light spectrum", "photoperiod", "grow lights", "umol/J", "PAR"],
    "substrates-overview": ["rockwool", "living soil", "hydroponics", "air-filled porosity", "growing media"],
    "water-quality": ["water quality", "reverse osmosis", "RO water", "alkalinity", "source water", "chloramine"],
    "ph-management": ["pH lockout", "pH pen", "pH up", "pH down"],
    "nutrient-deficiencies": ["nutrient deficiency", "nutrient toxicity", "nutrient lockout", "mobile nutrients"],
    "flowering-stages": ["flowering cycle", "the stretch", "bud set", "the flip", "12/12"],
    "pest-id": ["spider mites", "russet mites", "broad mites", "thrips", "fungus gnats", "aphids"],
    "pppe": ["PPPE", "gowning", "de-gowning", "personal protective equipment", "biosecurity", "fomite", "cross-contamination", "hierarchy of controls"],
    "ripening-harvest-timing": ["harvest window", "trichome maturity", "amber trichomes", "flushing", "when to harvest", "staggered harvest", "the fade"],
    "transplanting": ["transplant shock", "potting up", "ready to transplant", "root ball", "air pruning", "root-bound", "transplant-ready clone"],
    "veg-management": ["vegetative management", "veg duration", "flip height", "flowering stretch", "topping timing", "canopy levelling", "veg EC ramp"],
    "mother-plants": ["mother plant", "mother plants", "stock plant", "mother room", "clone-from-clone", "dudding disease", "cutting factory"],
    "genetics-phenohunting": ["pheno hunt", "phenotype hunt", "feminised seed", "keeper cut", "chemotype", "strain name", "S1 seed"],
    "temp-humidity-vpd": ["vapour pressure deficit", "VPD", "leaf VPD", "dew point", "relative humidity", "night humidity"],
    "lab-testing-coas": ["certificate of analysis", "COA", "total THC", "potency testing", "HPLC", "lab testing"],
    "unit-economics": ["cost per gram", "grams per watt", "unit economics", "cycles per year", "break-even", "blended price", "hand-trim labour"],
    "compliance-track-trace": ["seed-to-sale", "batch genealogy", "quality agreement", "mock recall", "inventory reconciliation", "GACP", "deviation log", "chain of custody"],
    "hvac-dehumidification": ["sensible and latent", "dehumidifier sizing", "lights-off humidity spike", "climate plant", "hot-gas reheat", "condensate", "N+1 redundancy"],
    "cannabinoids-terpenes": ["cannabinoids", "terpenes", "decarboxylation", "CBN", "entourage effect", "THCA"],
    "energy-sustainability": ["kWh per gram", "lighting efficacy", "double dividend", "demand charges", "heat-recovery dehumidification", "condensate reuse", "submetering", "energy benchmarking"],
}

# Flat (phrase, slug) list, longest phrase first so multi-word wins over substrings.
def phrase_list():
    pairs = [(p, slug) for slug, ph in LINK_PHRASES.items() for p in ph]
    pairs.sort(key=lambda x: len(x[0]), reverse=True)
    return pairs
