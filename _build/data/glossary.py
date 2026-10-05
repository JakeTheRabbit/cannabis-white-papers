# -*- coding: utf-8 -*-
"""Site-wide glossary. term -> plain-English definition. Powers the Glossary page,
in-text tooltips, and search. Keep definitions beginner-first and jargon-free."""

GLOSSARY = [
    {"term": "Tissue culture (TC)", "defn": "Tissue culture (TC) is the growth of plant cells, tissues or organs in a vessel without microbes. The plant material stays on a gel with nutrients and not in soil. When you use tissue culture to make many copies of a plant, the name of the method is also micropropagation.", "tags": ["tissue culture"]},
    {"term": "Micropropagation", "defn": "Micropropagation is a method that uses tissue culture to make many copies of one plant. All the copies have the same genes.", "tags": ["tissue culture"]},
    {"term": "In vitro", "defn": "In vitro is a Latin term for 'in glass'. It is the term for all that occurs in the culture vessel without microbes. The opposite term is ex vitro, which is for all that occurs out of the vessel.", "tags": ["tissue culture"]},
    {"term": "Explant", "defn": "An explant is a small piece of a plant. You cut it from the plant and put it in the culture vessel to start a new culture.", "tags": ["tissue culture"]},
    {"term": "Meristem", "defn": "A meristem is a dome of new cells that divide continuously at the tip of each shoot. No other tissue on the plant is as clean as the meristem, because it is too new to contain most diseases.", "tags": ["tissue culture"]},
    {"term": "Node", "defn": "A node is the point on a stem where a leaf and a bud attach to the stem. A nodal segment is a short piece of stem that contains one bud.", "tags": ["tissue culture", "propagation"]},
    {"term": "Totipotency", "defn": "Totipotency is a property of plant cells. One plant cell can make a new plant with all its parts, when the cell gets the correct nutrients and hormones.", "tags": ["tissue culture"]},
    {"term": "Aseptic technique", "defn": "Aseptic technique is the method to keep bacteria, fungi and yeast out of your culture. It is the most important method in tissue culture.", "tags": ["tissue culture"]},
    {"term": "Medium (media)", "defn": "A medium is the material that holds a culture and gives nutrients to it. It is a gel of mineral salts, sugar, vitamins and optional hormones. A gelling agent makes the gel solid.", "tags": ["tissue culture"]},
    {"term": "PGR (plant growth regulator)", "defn": "A PGR (plant growth regulator) is a plant hormone that you add to the medium to control growth. Cytokinins increase the growth of shoots. Auxins increase the growth of roots.", "tags": ["tissue culture"]},
    {"term": "Cytokinin", "defn": "A cytokinin is a type of plant hormone that increases the growth of shoots and buds. The examples are meta-topolin, BAP and TDZ.", "tags": ["tissue culture"]},
    {"term": "Auxin", "defn": "An auxin is a type of plant hormone that increases the growth of roots. IBA is the best auxin for cannabis.", "tags": ["tissue culture", "propagation"]},
    {"term": "Subculture", "defn": "Subculture is the task to move the tissue of a culture to new medium. You do the task again at intervals of a small number of weeks. Thus the cultures do not die and continue to increase in number.", "tags": ["tissue culture"]},
    {"term": "Hyperhydricity (vitrification)", "defn": "Hyperhydricity (vitrification) is a problem of tissue culture. A culture with this problem makes glassy shoots that contain too much water and are larger than usual. The shoots make roots badly, do not acclimatize correctly, and usually die when you transplant them.", "tags": ["tissue culture"]},
    {"term": "Acclimatisation (hardening)", "defn": "Acclimatization (hardening) is the task to make a plantlet from tissue culture stronger. You decrease the humidity and increase the light gradually. Thus the plantlet does not die in usual air.", "tags": ["tissue culture"]},
    {"term": "Indexing", "defn": "Indexing is a laboratory test of a plant, for example with RT-qPCR, to make sure that the plant has no specified disease. The test shows that the plant is clean.", "tags": ["tissue culture", "disease"]},
    {"term": "Hop Latent Viroid (HpLVd)", "defn": "Hop Latent Viroid (HpLVd) is a very small loop of RNA that is smaller than a virus. It causes 'dudding' in cannabis. Plants with dudding stay small and make smaller buds, and they contain much smaller quantities of cannabinoids and terpenes.", "tags": ["disease"]},
    {"term": "Viroid", "defn": "A viroid is a pathogen with a smaller number of parts than a virus. It is only a short loop of RNA, and it has no protein shell.", "tags": ["disease"]},
    {"term": "Clone", "defn": "A clone is a copy of a plant that has the same genes as the plant. You can make a clone from a cutting or with tissue culture.", "tags": ["propagation"]},
    {"term": "Mother plant", "defn": "A mother plant is a stock plant in good condition. You keep it in vegetative growth, and you remove cuttings or explants from it.", "tags": ["propagation"]},
    {"term": "VWC (volumetric water content)", "defn": "VWC is the quantity of water in the substrate of the root zone, as a percentage of the volume of the substrate. It is a primary signal for crop steering.", "tags": ["crop steering", "sensors"]},
    {"term": "EC (electrical conductivity)", "defn": "EC gives an estimate of the quantity of fertilizer salt that is in solution in the root zone. When the EC is higher, the feed is stronger.", "tags": ["crop steering", "sensors"]},
    {"term": "VPD (vapour pressure deficit)", "defn": "VPD shows how strongly the air pulls moisture from plants. It is one number that you calculate from the temperature and the humidity. This number changes the rate at which plants transpire.", "tags": ["environment"]},
    {"term": "Dryback", "defn": "Dryback is the quantity by which the moisture in the root zone decreases between irrigations. A grower sets the dryback to cause generative growth or vegetative growth in the plant.", "tags": ["crop steering"]},
    {"term": "Crop steering", "defn": "Crop steering is a method to cause a plant to make more vegetative growth (leaves) or more generative growth (flowers and fruit). You control the irrigation, the climate and the light.", "tags": ["crop steering"]},
    {"term": "Substrate", "defn": "A substrate is the material in which the roots stay. The examples are coco coir, rockwool, peat and soil.", "tags": ["cultivation"]},
    {"term": "Generative vs vegetative", "defn": "The two growth modes of a plant are vegetative growth (leaves, stems and size) and generative growth (flowers, fruit and density). Crop steering changes the balance between the two modes.", "tags": ["crop steering"]},
    {"term": "PPFD", "defn": "PPFD is photosynthetic photon flux density. It is the quantity of light on the canopy that the plant can use, in µmol/m²/s.", "tags": ["environment", "light"]},
    {"term": "GMP (good manufacturing practice)", "defn": "GMP is a quality system of procedures and records. It makes sure that a manufacturer makes products safely, with the same result each time, and with records that let you trace each product.", "tags": ["quality"]},
    {"term": "Endophyte", "defn": "An endophyte is a microbe that is in the tissue of a plant that looks in good condition. It is the contaminant that you cannot easily remove in tissue culture, because bleach on the surface cannot touch it.", "tags": ["tissue culture", "disease"]},
    {"term": "Capacitance sensor", "defn": "A capacitance sensor is a probe that measures the quantity of water in the substrate. It senses the electrical 'permittivity' of the substrate. Water changes the permittivity much more than soil or air does.", "tags": ["sensors"]},
    {"term": "Permittivity (dielectric)", "defn": "Permittivity is a property of a material that shows how strong the effect of an electric field is on the material. Water has a very high value of permittivity. Thus a moisture probe measures the permittivity and changes it to the water content.", "tags": ["sensors"]},
    {"term": "Calibration", "defn": "Calibration is the adjustment of the reading of a sensor, to make it agree with the correct value for the substrate that you use. Without calibration, the percentage on the screen can be incorrect.", "tags": ["sensors"]},
    {"term": "Pore-water EC", "defn": "Pore-water EC is the salt strength of the water that touches the roots (not the bulk EC). It is the EC that the plant gets.", "tags": ["sensors", "crop steering"]},
    {"term": "Sensor fusion", "defn": "Sensor fusion is a method to use the signals of some sensors together. Each signal has errors. The method makes one better estimate of the condition, and it gives a confidence value that shows how accurate the estimate is.", "tags": ["sensors", "control"]},
    {"term": "Telemetry", "defn": "Telemetry is the sequence of numbers that your sensors send. The numbers include the temperature, the humidity and the moisture.", "tags": ["control"]},
    {"term": "Setpoint vs target", "defn": "A setpoint is the specified value that a controller tries to keep at this time. A target is the wider result that you want to get for a period of days.", "tags": ["control"]},
    {"term": "Closed-loop control", "defn": "Closed-loop control is a system that measures a result, compares the result with the value that you want, and makes adjustments automatically. A thermostat is a typical example.", "tags": ["control"]},
    {"term": "Feedback", "defn": "In feedback, a system uses the measured result of an operation to select the next operation. Feedback is the primary part of each closed-loop system, which makes corrections automatically.", "tags": ["control"]},
    {"term": "Signal vs noise", "defn": "A signal is a change that occurs in the plant or in the root zone. Noise is a small random change from the sensor or from the environment, and it does not show a change in the plant. Good control uses the signal and ignores the noise.", "tags": ["control", "sensors"]},
    {"term": "Control limits (SPC)", "defn": "Control limits are limits around the usual variation, and you calculate them with statistics. A reading in the limits is only noise, and a reading out of the limits is a signal for a correction. SPC is the short name of 'statistical process control'.", "tags": ["control"]},
    {"term": "Cleanroom grade", "defn": "A cleanroom grade shows the maximum number of airborne particles that a room can have. To control the contamination of the product, you use a grade with a smaller maximum number of particles, and you use gowning.", "tags": ["quality", "facility"]},
    {"term": "SOP (standard operating procedure)", "defn": "An SOP (standard operating procedure) is a written instruction, with steps, for a task. It lets all personnel do the task with the same correct steps each time.", "tags": ["quality"]},
    {"term": "Traceability", "defn": "Traceability is the property of a product that lets you trace it back and forward through each step and input. It is necessary for recalls and audits.", "tags": ["quality"]},
    {"term": "CAPA", "defn": "CAPA (Corrective And Preventive Action) is the standard procedure to repair a problem and to make sure that it does not occur again. It is one of the primary procedures of GMP.", "tags": ["quality"]},
    {"term": "Batch release", "defn": "Batch release is the controlled decision that a completed batch is safe and agrees with the specification. Test results and records give the data for the decision. The batch can go to a customer only after the decision.", "tags": ["quality"]},
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

# Stamp each term with the paper slug that teaches it (None when no paper does).
try:
    from data.glossary_slugs import TERM_SLUGS
except Exception:
    TERM_SLUGS = {}
for _g in GLOSSARY:
    _g["slug"] = TERM_SLUGS.get(_g["term"])

def by_letter():
    buckets = {}
    for g in sorted(GLOSSARY, key=lambda x: x["term"].lower()):
        k = g["term"][0].upper()
        buckets.setdefault(k, []).append(g)
    return buckets
