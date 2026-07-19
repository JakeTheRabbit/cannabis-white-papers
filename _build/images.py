# -*- coding: utf-8 -*-
"""Image manifest. Drives gen_images.py (generation) AND build.py (embedding).
Each entry: slug, n (per-paper index), sec (0-based section to append the photo to,
clamped), model, ar, res, prompt, caption, alt. File = img/<slug>-<n>.jpg."""

MODEL_LABEL = {
    "nano_banana_2": "Nano Banana 2",
    "gpt_image_2": "GPT Image 2 (OpenAI)",
    "cinematic_studio_2_5": "Cinema Studio",
    "factcheck_pack": "Fact-check pack",
    "code_diagram": "Educational diagram",
}

# NB = photoreal practical, GPT = labelled/diagram, CIN = epic/cinematic hero
# FC = fact-check educational pack (photo or code diagram)
NB, GPT, CIN, FC, CD = "nano_banana_2", "gpt_image_2", "cinematic_studio_2_5", "factcheck_pack", "code_diagram"

IMAGES = [
 # ---- tissue culture (photoreal step series; sec indices AFTER evidence panel insert) ----
 {"slug":"tissue-culture","n":1,"sec":6,"model":NB,"ar":"16:9","res":"2k",
  "prompt":"still-air box TC workstation","caption":"Step — lab setup: a still-air box, alcohol, tools and culture jars. You need clean air, sterile tools and a warm lit shelf — not a hospital lab.","alt":"Home tissue culture still-air box workstation"},
 {"slug":"tissue-culture","n":2,"sec":7,"model":NB,"ar":"16:9","res":"2k",
  "prompt":"aseptic tool sterilisation","caption":"Step — aseptic technique: flame or alcohol-wipe tools every time. Most beginner failures are contamination from hands, breath or dirty instruments.","alt":"Gloved hands sterilising TC tools"},
 {"slug":"tissue-culture","n":3,"sec":8,"model":NB,"ar":"16:9","res":"2k",
  "prompt":"pouring agar media into jars","caption":"Step — make and sterilise medium: pour warm agar-based medium into vessels after autoclaving. Sugar + salts + hormones is the plant’s sealed-jar diet.","alt":"Pouring tissue culture medium into jars"},
 {"slug":"tissue-culture","n":4,"sec":5,"model":FC,"ext":"jpg","ar":"16:9","res":"2k",
  "prompt":"(factcheck) meristem vs HpLVd","caption":"Why meristem works: Hop Latent Viroid rides vascular tissue and often cannot reach the undifferentiated dome you excise.","alt":"Annotated meristem cutaway with HpLVd"},
 {"slug":"tissue-culture","n":5,"sec":9,"model":NB,"ar":"16:9","res":"2k",
  "prompt":"healthy cannabis mother plant","caption":"Stage 0 — condition the donor: pick a vigorous, true-to-type mother and clean it up for 1–2 weeks before you cut. Garbage in, garbage out.","alt":"Healthy vegetative cannabis mother plant"},
 {"slug":"tissue-culture","n":6,"sec":10,"model":NB,"ar":"16:9","res":"2k",
  "prompt":"cutting nodal explant","caption":"Stage I — cut a nodal explant: for first runs, a ~1 cm stem piece with one bud is the most forgiving starting piece.","alt":"Cutting a cannabis nodal explant with scalpel"},
 {"slug":"tissue-culture","n":7,"sec":10,"model":NB,"ar":"16:9","res":"2k",
  "prompt":"surface sterilise explant bleach","caption":"Stage I — surface-sterilise: dilute bleach (or kit sterilant) kills microbes on the outside without cooking the tissue if timing is right.","alt":"Explant in sterilant solution"},
 {"slug":"tissue-culture","n":8,"sec":11,"model":NB,"ar":"16:9","res":"2k",
  "prompt":"plating explant on agar","caption":"Initiation — plate the explant: set the sterile piece onto fresh medium and seal the vessel. Now it must wake up without contamination.","alt":"Placing explant on agar in culture jar"},
 {"slug":"tissue-culture","n":9,"sec":11,"model":NB,"ar":"16:9","res":"2k",
  "prompt":"initiation culture shelf","caption":"Initiation — culture room: ~25 °C, long days of soft light, and daily eyes on every jar for the first weeks.","alt":"Tissue culture jars on growth shelf"},
 {"slug":"tissue-culture","n":10,"sec":12,"model":NB,"ar":"16:9","res":"2k",
  "prompt":"meristem excision under microscope","caption":"Cleanup — meristem dissection: under a stereo microscope, cut only the tiny dome. This is the step that actually leaves most systemic disease behind.","alt":"Meristem excision under microscope"},
 {"slug":"tissue-culture","n":11,"sec":13,"model":NB,"ar":"16:9","res":"2k",
  "prompt":"RT-qPCR sample prep","caption":"Indexing — prove it: a healthy-looking plant is not clean until an RT-qPCR (or equivalent lab test) says so. Send tissue; do not skip this.","alt":"Leaf tissue sample ready for viroid lab test"},
 {"slug":"tissue-culture","n":12,"sec":14,"model":NB,"ar":"16:9","res":"2k",
  "prompt":"multiplication shoots in jars","caption":"Stage II — multiplication: cytokinin media push multiple shoots so one clean line becomes many vessels.","alt":"Multiple cannabis shoots multiplying in TC jars"},
 {"slug":"tissue-culture","n":13,"sec":14,"model":NB,"ar":"16:9","res":"2k",
  "prompt":"hyperhydricity glassy shoots","caption":"Watch for hyperhydricity: glassy, waterlogged shoots that look lush but root and harden poorly. Cut hormone or humidity, not hope.","alt":"Hyperhydric glassy tissue culture shoots"},
 {"slug":"tissue-culture","n":14,"sec":15,"model":NB,"ar":"16:9","res":"2k",
  "prompt":"in vitro rooting","caption":"Stage III — rooting: auxin media (or a simpler ex-vitro rooting path) turns a shoot into a plant with white roots.","alt":"Tissue culture shoot rooting in agar"},
 {"slug":"tissue-culture","n":15,"sec":16,"model":NB,"ar":"16:9","res":"2k",
  "prompt":"acclimatisation under dome","caption":"Stage IV — acclimatisation: slowly lower humidity and raise light. Rushing weaning kills more plantlets than almost any other step.","alt":"TC plantlet hardening under humidity dome"},
 {"slug":"tissue-culture","n":16,"sec":17,"model":NB,"ar":"16:9","res":"2k",
  "prompt":"clean mother stock plant","caption":"Re-establish the clean mother: veg her under long days in a scrubbed space, then take ordinary cuttings from a tested line.","alt":"Young clean cannabis mother from tissue culture"},
 {"slug":"tissue-culture","n":17,"sec":19,"model":NB,"ar":"16:9","res":"2k",
  "prompt":"contamination vs clean jar","caption":"Troubleshooting — contamination: fuzzy mould or cloudy bacterial slime means that vessel is dead. Compare against a clean jar and throw out without opening if possible.","alt":"Contaminated tissue culture jar next to clean jar"},
 {"slug":"tissue-culture","n":18,"sec":4,"model":NB,"ar":"16:9","res":"2k",
  "prompt":"workflow overview bench",
  "caption":"The whole pipeline on one bench: clean workspace, media jars, culture vessels and a donor plant. Stages 0 through a hardened mother follow this order.","alt":"Tissue culture workflow overview on lab bench"},


 # ---- coco & crop steering ----
 {"slug":"coco-crop-steering","n":1,"sec":2,"model":NB,"ar":"16:9","res":"2k",
  "prompt":"Photorealistic close-up in a commercial cannabis grow: a rectangular open-top coco coir grow bag (a printed white coir grow bag, about one gallon) sitting on a bench with a healthy cannabis plant growing out of the open top; a flat white rectangular three-prong capacitance substrate sensor (thin polished steel needles, white body, thin black cable with a cylindrical ferrite bead) inserted into the coir at an angle; thin white 4mm drip-irrigation lines arch over the bag with drip stakes pushed into the coir surface; bright greenhouse lighting, sharp documentary detail. NOT a fabric pot, NOT a terracotta pot, NOT a handheld dial meter.",
  "caption":"A real root-zone capacitance probe and drip stakes in an open-top coir grow bag, the hardware behind reading and steering.","alt":"Capacitance sensor and drippers in a coir grow bag"},
 {"slug":"coco-crop-steering","n":2,"sec":4,"model":NB,"ar":"16:9","res":"2k",
  "prompt":"Photorealistic close-up: white pressure-compensating drip-emitter stakes fed by thin 4mm lines releasing water onto the surface of a rectangular open-top coco coir grow bag (printed white coir bag, about one gallon) with a cannabis plant growing from the open top, glistening wet patch spreading across the coir, greenhouse grow setting, ultra sharp detail. NOT a fabric pot, NOT a terracotta pot.",
  "caption":"A timed irrigation shot wetting the coir in an open-top bag, small pulses refill the root zone in stages.","alt":"Drip irrigation onto a coir grow bag"},

 # ---- grow-room systems ----
 {"slug":"grow-room-systems","n":1,"sec":0,"model":CIN,"ar":"16:9","res":"2k",
  "prompt":"Epic cinematic wide shot of a pristine indoor cannabis grow room at peak flower, uniform canopy of healthy plants under powerful LED bar lights, visible airflow, clean white walls, atmospheric haze, symmetrical composition, photoreal, high-end facility",
  "caption":"The room as one system: light, climate, airflow and water balanced over a uniform canopy.","alt":"Pristine indoor grow room under LED"},
 {"slug":"grow-room-systems","n":2,"sec":4,"model":NB,"ar":"16:9","res":"2k",
  "prompt":"Photorealistic: close-up of a digital climate sensor and controller unit mounted among cannabis plants in a grow room, reading temperature and humidity, LED light glow, condensation-free, crisp detail",
  "caption":"Climate sensing at canopy height, the inputs that drive the whole coupled system.","alt":"Climate sensor among plants"},

 # ---- airflow design ----
 {"slug":"airflow-design","n":1,"sec":6,"model":NB,"ar":"16:9","res":"2k",
  "prompt":"Photorealistic: oscillating wall fans and clip fans positioned around a cannabis canopy, leaves gently fluttering in the breeze, motion in the foliage, indoor grow room under LED, dynamic, sharp",
  "caption":"Fans placed to move air through the canopy, every leaf should gently flutter.","alt":"Fans creating airflow over canopy"},
 {"slug":"airflow-design","n":2,"sec":2,"model":GPT,"ar":"16:9","res":"1k",
  "prompt":"Clean labelled scientific cross-section diagram of a single leaf showing the boundary layer of still air, arrows of moving air thinning it, CO2 entering and water vapour leaving, minimalist white background, crisp vector style with clear small labels",
  "caption":"The leaf boundary layer and how moving air thins it (labelled schematic).","alt":"Leaf boundary layer diagram"},

 # ---- mould risk ----
 {"slug":"mould-risk","n":1,"sec":3,"model":NB,"ar":"16:9","res":"2k",
  "prompt":"Photorealistic macro: a dense cannabis flower bud with the early grey fuzzy rot of botrytis starting deep inside, a yellowing leaf pulling away, dramatic detail, slightly clinical documentary lighting, sharp focus on the affected cola",
  "caption":"Bud rot (Botrytis) starting inside a dense cola, caught early during scouting.","alt":"Botrytis bud rot close-up"},
 {"slug":"mould-risk","n":2,"sec":5,"model":NB,"ar":"16:9","res":"2k",
  "prompt":"Photorealistic: a grower in nitrile gloves inspecting cannabis buds with a bright LED loupe light during late flower scouting, focused close inspection, grow room background softly blurred, documentary realism",
  "caption":"Daily scouting in late flower, five minutes with a light catches rot before it spreads.","alt":"Scouting buds for mould"},

 # ---- root zone TEROS-12 ----
 {"slug":"root-zone-teros12","n":1,"sec":0,"model":NB,"ar":"16:9","res":"2k",
  "prompt":"Photorealistic product macro on a clean light-grey surface: a professional research-grade volumetric water content sensor, a flat white rectangular epoxy probe body about 9 cm long with three thin parallel polished stainless-steel needle prongs about 5 cm long extending from one end, and a thin black signal cable with a small black cylindrical ferrite choke bead near it; soft even studio lighting, crisp scientific product photography, ultra detailed. NOT a handheld dial meter, no round gauge, no screen.",
  "caption":"A research-grade capacitance probe: white body, three fine prongs, ferrite-beaded cable, not a cheap dial meter.","alt":"Capacitance root-zone sensor probe"},
 {"slug":"root-zone-teros12","n":2,"sec":2,"model":NB,"ar":"16:9","res":"2k",
  "prompt":"Photorealistic close-up in a commercial cannabis grow: a research-grade capacitance substrate sensor (white-and-black rectangular body with thin polished steel prongs and a thin black cable with a cylindrical ferrite bead) inserted at an angle into an open-top one-gallon coco coir grow bag, thin white 4mm drip-irrigation lines arching over the bag with drip stakes, green cannabis stems and foliage rising above, a small irrigation controller unit with a screen on the floor in the foreground, bright even greenhouse lighting, documentary realism, sharp focus",
  "caption":"The real-world install: a capacitance probe seated in a coir grow bag, drip lines overhead, wired to a controller.","alt":"Capacitance sensor installed in a coir grow bag with drip lines"},

 # ---- smart watering VRWE ----
 {"slug":"smart-watering-vrwe","n":1,"sec":0,"model":GPT,"ar":"16:9","res":"1k",
  "prompt":"Clean modern infographic-style illustration: multiple sensor signals (moisture, EC, temperature, light) flowing as arrows into a glowing central 'brain' node that outputs a single watering decision, minimalist tech aesthetic, soft greens and greys, clear small labels",
  "caption":"Sensor fusion as a 'watering brain', many noisy signals into one confident decision.","alt":"Sensor fusion brain illustration"},

 # ---- signal & noise ----
 {"slug":"signal-and-noise","n":1,"sec":3,"model":GPT,"ar":"16:9","res":"1k",
  "prompt":"Clean data-visualization style image: a noisy jittery sensor time-series line with statistical control limit bands, one clear point breaking out past the band highlighted as a real 'signal', minimalist chart, white background, crisp labels",
  "caption":"Control limits separate real signal (the breakout point) from meaningless noise.","alt":"Control chart signal vs noise"},

 # ---- closed loop ----
 {"slug":"closed-loop","n":1,"sec":2,"model":GPT,"ar":"16:9","res":"1k",
  "prompt":"Clean labelled control-loop diagram: levers (light, climate, water) feeding a plant, sensors reading plant state, feedback arrow returning to a controller and back to the levers, circular flow, minimalist, white background, small clear labels",
  "caption":"The closed loop: act, measure plant state, compare, adjust, round and round.","alt":"Closed-loop control diagram"},

 # ---- plant-state dashboard ----
 {"slug":"plant-state-dashboard","n":1,"sec":0,"model":GPT,"ar":"16:9","res":"1k",
  "prompt":"Clean modern dashboard UI mockup on a dark screen showing plant-state indicators (transpiration, stress, growth mode) as clear gauges and a canopy diagram instead of raw numbers, professional product design, crisp legible labels",
  "caption":"A dashboard that shows plant state, not just raw sensor numbers.","alt":"Plant-state dashboard mockup"},

 # ---- f2 crop steering ----
 {"slug":"f2-crop-steering","n":1,"sec":3,"model":GPT,"ar":"16:9","res":"1k",
  "prompt":"Clean infographic board: the daily irrigation cycle split into four phases P0 P1 P2 P3 along a 24-hour timeline with a root-zone moisture curve rising and falling, minimalist, white background, clear labels",
  "caption":"The P0–P3 daily cycle as one board, dry, refill, maintain, dry.","alt":"P0-P3 daily cycle board"},

 # ---- irrigation manual ----
 {"slug":"irrigation-manual","n":1,"sec":2,"model":NB,"ar":"16:9","res":"2k",
  "prompt":"Photorealistic: a tidy fertigation hardware setup, a pump, mixing tank, manifold and rows of drip lines feeding cannabis plants, clean tubing, professional installation, grow room, sharp technical detail",
  "caption":"A clean fertigation install, pump, tank, manifold and dripper lines.","alt":"Fertigation irrigation hardware"},

 # ---- cloning ----
 {"slug":"cloning","n":1,"sec":4,"model":NB,"ar":"16:9","res":"2k",
  "prompt":"Photorealistic: fresh cannabis cuttings standing in rockwool cubes inside a clear humidity dome propagator, tiny white roots just emerging, water droplets on the dome, soft propagation lighting, macro detail",
  "caption":"Cuttings in rockwool under a humidity dome, the first white roots emerging.","alt":"Cannabis clones in humidity dome"},
 {"slug":"cloning","n":2,"sec":3,"model":NB,"ar":"16:9","res":"2k",
  "prompt":"Photorealistic close-up: a freshly prepared cannabis cutting being dipped into a small pot of clear rooting gel, gloved hand holding the green stem, clean propagation bench with rockwool cubes and a humidity dome behind, soft propagation light, shallow depth of field, detailed",
  "caption":"Dipping a fresh cutting in rooting gel before it goes into a rockwool cube.","alt":"Cannabis cutting dipped in rooting gel"},

 # ---- nutrient mixing athena ----
 {"slug":"nutrient-mixing-athena","n":1,"sec":4,"model":NB,"ar":"16:9","res":"2k",
  "prompt":"Photorealistic: a 50 litre plastic tank of nutrient solution being mixed with a paint-mixer paddle on a cordless drill creating a vortex, white mineral salt powder dissolving, hot water steam, clean grow-room utility area, sharp detail",
  "caption":"A full bag going into a 50 L tank, paddle on a drill, hot water, mixed to clear.","alt":"Mixing a nutrient stock tank with a drill paddle"},

 # ---- light acclimation ----
 {"slug":"light-acclimation","n":1,"sec":3,"model":NB,"ar":"16:9","res":"2k",
  "prompt":"Photorealistic: a light meter / PAR sensor held over a healthy cannabis canopy under bright LED bar lights, reading on the meter, intense even lighting, grow room, crisp detail",
  "caption":"Measuring PPFD at the canopy, you ramp light to a number, not by eye.","alt":"PAR meter over canopy"},
 {"slug":"light-acclimation","n":2,"sec":2,"model":NB,"ar":"16:9","res":"2k",
  "prompt":"Photorealistic macro: cannabis fan leaves showing light bleaching, pale white-yellow tips on the topmost leaves closest to the lamp while lower leaves stay deep green, documentary clarity, sharp",
  "caption":"Light bleaching: pale tops nearest the lamp when intensity outran the plant's capacity.","alt":"Light-bleached cannabis tops"},

 # ---- defoliation & training ----
 {"slug":"defoliation-training","n":1,"sec":3,"model":NB,"ar":"16:9","res":"2k",
  "prompt":"Photorealistic top-down: a cannabis plant trained flat across a horizontal trellis net (SCROG), even canopy of shoot tips poking through the squares, lush green, grow-room lighting, sharp detail",
  "caption":"A SCROG net spreads the canopy flat so every site gets equal light.","alt":"SCROG trellis canopy from above"},
 {"slug":"defoliation-training","n":2,"sec":4,"model":NB,"ar":"16:9","res":"2k",
  "prompt":"Photorealistic: a defoliated and lollipopped cannabis plant in early flower, lower growth stripped to bare stem, open airy structure with clear bud sites up top, clean grow room, documentary realism",
  "caption":"Lollipopped and defoliated, energy and airflow pushed to the productive top sites.","alt":"Lollipopped cannabis plant"},

 # ---- IPM SOP ----
 {"slug":"ipm-sop","n":1,"sec":4,"model":NB,"ar":"16:9","res":"2k",
  "prompt":"Photorealistic: a yellow sticky trap among cannabis plants with a few fungus gnats stuck to it, and a grower's hand placing it, scouting context, grow room, sharp macro detail",
  "caption":"A yellow sticky card, cheap early-warning scouting that turns hunches into counts.","alt":"Yellow sticky pest trap in canopy"},
 {"slug":"ipm-sop","n":2,"sec":2,"model":NB,"ar":"16:9","res":"2k",
  "prompt":"Photorealistic macro: a sachet of predatory mites being sprinkled onto a cannabis leaf as biological control, tiny beneficial insects visible, soft natural light, documentary detail",
  "caption":"Releasing predatory mites, biocontrol that lives in the canopy and hunts pests.","alt":"Releasing predatory mites"},

 # ---- harvest / dry / trim / cure ----
 {"slug":"harvest-dry-trim-cure","n":1,"sec":1,"model":NB,"ar":"16:9","res":"2k",
  "prompt":"Photorealistic extreme macro: cannabis trichomes on a flower at harvest maturity, milky-cloudy heads with a few amber, viewed through a jeweller's loupe clarity, glistening resin, ultra sharp, scientific",
  "caption":"Trichomes at harvest: mostly cloudy with a touch of amber, the maturity signal.","alt":"Cannabis trichomes macro"},
 {"slug":"harvest-dry-trim-cure","n":2,"sec":4,"model":NB,"ar":"16:9","res":"2k",
  "prompt":"Photorealistic: whole cannabis branches hung upside down in a clean climate-controlled drying room, even spacing, soft low light, hygrometer on the wall, documentary facility photography",
  "caption":"A controlled dry: branches hung in a cool, dark, airflowed room near 60% humidity.","alt":"Cannabis drying room"},
 {"slug":"harvest-dry-trim-cure","n":3,"sec":6,"model":NB,"ar":"16:9","res":"2k",
  "prompt":"Photorealistic: cured cannabis flower in clear glass mason jars with a small hygrometer inside reading about 60 percent, being burped, clean shelf, warm soft light, premium detail",
  "caption":"Curing in sealed glass with a hygrometer, burping to hold the right water activity.","alt":"Curing cannabis in glass jars"},

 # ---- GMP hash lab ----
 {"slug":"gmp-hash-lab","n":1,"sec":0,"model":CIN,"ar":"16:9","res":"2k",
  "prompt":"Epic cinematic: a gowned technician in full cleanroom suit and gloves working stainless-steel solventless hash-wash equipment in a spotless GMP cleanroom, dramatic clean lighting, reflective surfaces, premium pharmaceutical facility, photoreal",
  "caption":"GMP processing: gowning and stainless steel in a controlled cleanroom.","alt":"Technician in GMP hash cleanroom"},
 {"slug":"gmp-hash-lab","n":2,"sec":3,"model":GPT,"ar":"16:9","res":"1k",
  "prompt":"Clean labelled facility floor-plan diagram showing cleanroom zoning by grade, one-directional material and personnel flow arrows, airlocks and gowning rooms, minimalist top-down schematic, white background, clear small labels",
  "caption":"Zoned material and personnel flow, clean shells nested by cleanroom grade.","alt":"GMP facility zoning diagram"},

 # ---- facility 3D ----
 {"slug":"facility-3d","n":1,"sec":0,"model":GPT,"ar":"16:9","res":"1k",
  "prompt":"Clean 3D architectural render: a top-down/isometric model of a cannabis grow facility floor plan with labelled rooms (veg, flower, dry, trim), equipment blocks and airflow, modern CAD visualization style, crisp labels",
  "caption":"Modelling the facility in 3D catches clashes before construction starts.","alt":"3D facility floor-plan render"},

 # ---- fact-check educational pack (2026-07) ----
 {"slug":"seeds-germination","n":1,"sec":5,"model":FC,"ext":"jpg","ar":"16:9","res":"2k",
  "prompt":"(factcheck) seedling roots drink under humidity dome in rockwool+coco",
  "caption":"Roots still take the water. A humidity dome cuts evaporative demand — it does not mean the seedling drinks through its leaves.","alt":"Seedling in rockwool and coco under humidity dome"},
 {"slug":"harvest-dry-trim-cure","n":4,"sec":4,"model":FC,"ext":"jpg","ar":"16:9","res":"2k",
  "prompt":"(factcheck) water activity meter and moisture meter on dried flower",
  "caption":"Same bulk moisture reading can span dry-to-mouldy water activity. Steer post-harvest with aw (here ~0.61) not a cheap moisture % alone.","alt":"Water activity and moisture meters with dried buds"},
 {"slug":"mould-risk","n":3,"sec":2,"model":FC,"ext":"jpg","ar":"16:9","res":"2k",
  "prompt":"(factcheck) cola room RH vs inside microclimate",
  "caption":"Room air can read safe while the dense cola interior stays wetter — where bud rot starts.","alt":"Cannabis cola exterior vs humid interior cutaway"},
 {"slug":"mould-risk","n":4,"sec":3,"model":FC,"ext":"jpg","ar":"16:9","res":"2k",
  "prompt":"(factcheck) late flower aisle climate meter",
  "caption":"Measure in the aisle and at canopy height. Late flower often targets roughly 45–55% RH with strong through-canopy air.","alt":"Thermo-hygrometer in late flower room"},
 {"slug":"under-canopy-lighting","n":1,"sec":2,"model":FC,"ext":"jpg","ar":"16:9","res":"2k",
  "prompt":"(factcheck) canopy spectrum filter green FR enriched",
  "caption":"Under the canopy, blue and red are depleted; green and far-red are relatively enriched — not a “red-rich” understory.","alt":"Above vs under canopy LED spectrum comparison"},
 {"slug":"scaling-high-light","n":1,"sec":1,"model":CD,"ext":"svg","ar":"16:9","res":"1k",
  "prompt":"(factcheck) leaf vs canopy light curves",
  "caption":"Leaf photosynthesis can plateau while whole-canopy flower yield still rises with light — ambient CO₂ is not a hard 800 µmol wall.","alt":"Leaf Anet vs canopy yield vs PPFD graphs"},
 {"slug":"lighting-fundamentals","n":1,"sec":3,"model":CD,"ext":"svg","ar":"16:9","res":"1k",
  "prompt":"(factcheck) leaf vs canopy light curves",
  "caption":"Intensity targets are canopy-scale. A single leaf gas-exchange curve is not the whole room’s yield ceiling.","alt":"Leaf vs canopy light response graphs"},
 {"slug":"coco-crop-steering","n":3,"sec":3,"model":CD,"ext":"svg","ar":"16:9","res":"1k",
  "prompt":"(factcheck) Caplan one drought vs daily drybacks",
  "caption":"A single carefully timed late drought is not the same experiment as daily generative dryback sawteeth.","alt":"Single drought vs daily dryback VWC traces"},
 {"slug":"coco-crop-steering","n":4,"sec":2,"model":CD,"ext":"svg","ar":"16:9","res":"1k",
  "prompt":"(factcheck) dryback percentage points",
  "caption":"Dryback is percentage points (peak minus trough), not “percent of peak” unless you say so.","alt":"Dryback points vs percent of peak"},
 {"slug":"rockwool-crop-steering","n":1,"sec":2,"model":CD,"ext":"svg","ar":"16:9","res":"1k",
  "prompt":"(factcheck) Caplan one drought vs daily drybacks",
  "caption":"Daily drybacks are a related idea to controlled deficit — not a copy of one late-flower drought trial.","alt":"Single drought vs daily dryback comparison"},
 {"slug":"one-steering-law","n":1,"sec":2,"model":CD,"ext":"svg","ar":"16:9","res":"1k",
  "prompt":"(factcheck) dryback percentage points",
  "caption":"Count dryback in percentage points: 78% down to 58% is 20 points.","alt":"Dryback points explanation gauge"},
 {"slug":"one-steering-law","n":2,"sec":4,"model":CD,"ext":"svg","ar":"16:9","res":"1k",
  "prompt":"(factcheck) Caplan vs daily drybacks",
  "caption":"One multi-day late drought ≠ multi-week daily steering pulses.","alt":"Drought study vs daily drybacks"},
 {"slug":"irrigation-manual","n":2,"sec":2,"model":CD,"ext":"svg","ar":"16:9","res":"1k",
  "prompt":"(factcheck) veg vs gen dryback phases",
  "caption":"Vegetative: smaller drybacks, stay wetter. Generative: larger controlled drybacks. Example VWC vs crop day.","alt":"Veg vs generative dryback VWC chart"},
 {"slug":"f2-crop-steering","n":2,"sec":2,"model":CD,"ext":"svg","ar":"16:9","res":"1k",
  "prompt":"(factcheck) veg vs gen dryback phases",
  "caption":"Phase polarity for autonomous steering: veg smaller drybacks, generative larger controlled drybacks.","alt":"Crop phase VWC dryback chart"},
 {"slug":"water-quality","n":1,"sec":3,"model":CD,"ext":"svg","ar":"16:9","res":"1k",
  "prompt":"(factcheck) DO saturation vs temperature",
  "caption":"Air-saturated DO is roughly ~9 mg/L at 20 °C and ~8 mg/L at 26 °C — not 5–6 / 3–4 ppm. Still chill and aerate for roots.","alt":"Dissolved oxygen saturation curve"},
 {"slug":"pppe","n":1,"sec":2,"model":CD,"ext":"svg","ar":"16:9","res":"1k",
  "prompt":"(factcheck) clean dirty two kit flow",
  "caption":"Two kits: cultivation gowning and a separate post-harvest gown-in. Flower coveralls do not walk into dry/trim.","alt":"Facility two-track gowning flow"},
 {"slug":"pppe","n":2,"sec":4,"model":CD,"ext":"svg","ar":"16:9","res":"1k",
  "prompt":"(factcheck) log reduction table",
  "caption":"Log reduction: 1 log ≈ 90%, 2 log ≈ 99%, 3 log ≈ 99.9%. Mapping 3 log to 83% is wrong.","alt":"Hand hygiene log reduction table"},

]

# Dropped AI diagram images (image-gen mangles labels; papers already have real SVG diagrams).
_SKIP = {("airflow-design", 2), ("smart-watering-vrwe", 1), ("signal-and-noise", 1),
         ("closed-loop", 1), ("plant-state-dashboard", 1), ("f2-crop-steering", 1),
         ("gmp-hash-lab", 2), ("facility-3d", 1)}
IMAGES = [im for im in IMAGES if (im["slug"], im["n"]) not in _SKIP]

def by_slug():
    d = {}
    for im in IMAGES:
        d.setdefault(im["slug"], []).append(im)
    return d
