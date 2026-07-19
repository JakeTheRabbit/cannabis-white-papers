# -*- coding: utf-8 -*-
"""Site-wide glossary. term -> plain-English definition. Powers the Glossary page,
in-text tooltips, and search. Keep definitions beginner-first and jargon-free."""

GLOSSARY = [
    {"term": "Tissue culture (TC)", "defn": "Growing plant cells, tissues or organs in a sterile container on a jelly-like food, instead of in soil. Also called micropropagation when used to multiply a plant.", "tags": ["tissue culture"]},
    {"term": "Micropropagation", "defn": "Using tissue culture to make many genetically identical copies of one plant.", "tags": ["tissue culture"]},
    {"term": "In vitro", "defn": "Latin for 'in glass', anything happening inside the sterile culture vessel. Opposite of ex vitro (out in the real world).", "tags": ["tissue culture"]},
    {"term": "Explant", "defn": "The small piece of plant you cut off and place into the culture vessel to start a new culture.", "tags": ["tissue culture"]},
    {"term": "Meristem", "defn": "The dome of forever-young, constantly dividing cells at the very tip of every shoot. The cleanest tissue on the plant, too new to carry most diseases.", "tags": ["tissue culture"]},
    {"term": "Node", "defn": "The point on a stem where a leaf and a bud join. A nodal segment is a short stem piece containing one bud.", "tags": ["tissue culture", "propagation"]},
    {"term": "Totipotency", "defn": "The remarkable ability of a single plant cell to regrow into a whole new plant, given the right food and hormones.", "tags": ["tissue culture"]},
    {"term": "Aseptic technique", "defn": "Working so that no bacteria, fungi or yeast get into your culture. The single most important skill in tissue culture.", "tags": ["tissue culture"]},
    {"term": "Medium (media)", "defn": "The food a culture grows on: a jelly of mineral salts, sugar, vitamins and (optionally) hormones, set firm with a gelling agent.", "tags": ["tissue culture"]},
    {"term": "PGR (plant growth regulator)", "defn": "A plant hormone added to the medium to steer growth, cytokinins push shoots, auxins push roots.", "tags": ["tissue culture"]},
    {"term": "Cytokinin", "defn": "A class of plant hormone that promotes shoot and bud growth. Examples: meta-topolin, BAP, TDZ.", "tags": ["tissue culture"]},
    {"term": "Auxin", "defn": "A class of plant hormone that promotes root growth. IBA is the best one for cannabis.", "tags": ["tissue culture", "propagation"]},
    {"term": "Subculture", "defn": "Moving growing tissue onto fresh medium. Repeated every few weeks to keep cultures alive and multiplying.", "tags": ["tissue culture"]},
    {"term": "Hyperhydricity (vitrification)", "defn": "A disorder where shoots turn glassy, swollen and water-soaked. They root and harden poorly and usually die at transplant.", "tags": ["tissue culture"]},
    {"term": "Acclimatisation (hardening)", "defn": "Gradually toughening a tissue-cultured plantlet up, lowering humidity and raising light, so it can survive in normal air.", "tags": ["tissue culture"]},
    {"term": "Indexing", "defn": "Lab-testing a plant (e.g. by RT-qPCR) to confirm it is free of a specific disease. Proving a plant is clean.", "tags": ["tissue culture", "disease"]},
    {"term": "Hop Latent Viroid (HpLVd)", "defn": "A tiny loop of RNA, smaller than a virus, that causes 'dudding' in cannabis: stunted plants, smaller buds and big losses in cannabinoids and terpenes.", "tags": ["disease"]},
    {"term": "Viroid", "defn": "An infectious agent even simpler than a virus: just a short circle of RNA with no protein shell.", "tags": ["disease"]},
    {"term": "Clone", "defn": "A genetically identical copy of a plant, whether made by a cutting or by tissue culture.", "tags": ["propagation"]},
    {"term": "Mother plant", "defn": "A healthy stock plant kept in vegetative growth, from which cuttings or explants are taken.", "tags": ["propagation"]},
    {"term": "VWC (volumetric water content)", "defn": "How much water is in the root-zone substrate, as a percentage of its volume. A core crop-steering signal.", "tags": ["crop steering", "sensors"]},
    {"term": "EC (electrical conductivity)", "defn": "A proxy for how much fertiliser salt is dissolved in the root zone. Higher EC = stronger feed.", "tags": ["crop steering", "sensors"]},
    {"term": "VPD (vapour pressure deficit)", "defn": "How 'thirsty' the air is, combines temperature and humidity into one number that drives how fast plants transpire.", "tags": ["environment"]},
    {"term": "Dryback", "defn": "The deliberate drop in root-zone moisture between irrigations, used to steer the plant generative or vegetative.", "tags": ["crop steering"]},
    {"term": "Crop steering", "defn": "Nudging a plant toward vegetative (leafy) or generative (flower/fruit) growth by controlling irrigation, climate and light.", "tags": ["crop steering"]},
    {"term": "Substrate", "defn": "The growing medium roots live in, coco coir, rockwool, peat or soil.", "tags": ["cultivation"]},
    {"term": "Generative vs vegetative", "defn": "Two growth modes: vegetative = leaves and stems and size; generative = flowers, fruit and density. Crop steering shifts the balance.", "tags": ["crop steering"]},
    {"term": "PPFD", "defn": "Photosynthetic photon flux density, the amount of usable light hitting the canopy, in µmol/m²/s.", "tags": ["environment", "light"]},
    {"term": "GMP (good manufacturing practice)", "defn": "A quality framework of rules and records that ensures products are made safely, consistently and traceably.", "tags": ["quality"]},
    {"term": "Endophyte", "defn": "A microbe that lives inside healthy-looking plant tissue. The hardest contaminant in tissue culture because surface bleach can't reach it.", "tags": ["tissue culture", "disease"]},
    {"term": "Capacitance sensor", "defn": "A probe that measures how much water is in the substrate by sensing its electrical 'permittivity', water changes it far more than soil or air do.", "tags": ["sensors"]},
    {"term": "Permittivity (dielectric)", "defn": "How strongly a material responds to an electric field. Water has a very high value, so a moisture probe is really measuring permittivity and converting it to water content.", "tags": ["sensors"]},
    {"term": "Calibration", "defn": "Adjusting a sensor's raw reading so it matches reality for your specific substrate, without it, the percentage on screen can be off.", "tags": ["sensors"]},
    {"term": "Pore-water EC", "defn": "The salt strength of the water actually touching the roots (as opposed to the bulk average). It's what the plant really 'tastes'.", "tags": ["sensors", "crop steering"]},
    {"term": "Sensor fusion", "defn": "Combining several imperfect sensor signals into one better estimate of what's really happening, with a sense of how much to trust it.", "tags": ["sensors", "control"]},
    {"term": "Telemetry", "defn": "The stream of numbers your sensors send back, temperature, humidity, moisture and so on, over time.", "tags": ["control"]},
    {"term": "Setpoint vs target", "defn": "A setpoint is the exact value a controller aims to hold right now; a target is the broader goal you're steering toward over days.", "tags": ["control"]},
    {"term": "Closed-loop control", "defn": "When a system measures a result, compares it to a goal, and adjusts itself automatically, a thermostat is the classic example.", "tags": ["control"]},
    {"term": "Feedback", "defn": "Using the measured result of an action to decide the next action. The heart of any self-correcting (closed-loop) system.", "tags": ["control"]},
    {"term": "Signal vs noise", "defn": "Signal is a real change in the plant or root zone; noise is meaningless jitter from the sensor or environment. Good control acts on signal, ignores noise.", "tags": ["control", "sensors"]},
    {"term": "Control limits (SPC)", "defn": "Statistically-set lines around normal variation. A reading inside them is just noise; one outside is a real signal worth acting on. From 'statistical process control'.", "tags": ["control"]},
    {"term": "Cleanroom grade", "defn": "A rating for how few airborne particles a room allows. Stricter grades (and gowning) are used where product contamination must be controlled.", "tags": ["quality", "facility"]},
    {"term": "SOP (standard operating procedure)", "defn": "A written, step-by-step instruction for a task, so it's done the same correct way every time by anyone.", "tags": ["quality"]},
    {"term": "Traceability", "defn": "Being able to follow a product backward and forward through every step and input, essential for recalls and audits.", "tags": ["quality"]},
    {"term": "CAPA", "defn": "Corrective And Preventive Action: the formal process of fixing a problem and stopping it from happening again. A core GMP habit.", "tags": ["quality"]},
    {"term": "Batch release", "defn": "The controlled decision, backed by test results and records, that a finished batch is safe and meets spec before it can be sold.", "tags": ["quality"]},
]

# Merge generated terms (skip any term already defined).
_seen = {g["term"].strip().lower() for g in GLOSSARY}
for _genmod in ("data.glossary_gen", "data.glossary_gen4", "data.glossary_gen5", "data.glossary_gen6", "data.glossary_gen7", "data.glossary_gen8", "data.glossary_gen9"):
    try:
        _m = __import__(_genmod, fromlist=["GLOSSARY_ADD"])
        for _g in _m.GLOSSARY_ADD:
            _t = _g.get("term", "").strip().lower()
            if _t and _t not in _seen:
                GLOSSARY.append(_g); _seen.add(_t)
    except Exception:
        pass

def by_letter():
    buckets = {}
    for g in sorted(GLOSSARY, key=lambda x: x["term"].lower()):
        k = g["term"][0].upper()
        buckets.setdefault(k, []).append(g)
    return buckets
