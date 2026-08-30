# TEACHER_VOICE_LOG

## Pre-blocked (content not in paper_*.py)

### auckland-ipm-blueprint — BLOCKED
- blocker: content lives in _build/ipm_blueprint/content.py, not in a paper_*.py file
- file: _build/paper_auckland_ipm_blueprint.py

### slab-irrigation-strategy — BLOCKED
- blocker: body text lives in _build/data/slab_irrigation_content.html, which the job rules prohibit editing
- file: _build/paper_slab_irrigation.py

## Phase 1 Results

### airflow-design — DONE
- analogies added (mechanism → analogy used):
  - boundary layer — still air on skin analogy (body) in Section 03, before naming the term
  - transpiration — damp towel in sunlight analogy (household object) in defterm
  - entrainment — speedboat wake analogy (household/weather) in defterm Throw and entrainment
- units dual-labelled or flipped: 11
- file: _build/paper_airflow_design.py

### cannabinoids-terpenes — DONE
- headings renamed:
  - "The assembly line" → "The biosynthetic pathway" (section 3 kicker)
  - "The volatile half" → "Terpene classes" (section 7 kicker)
  - "The clock" → "Degradation rates" (section 10 kicker)
  - "Where potency goes to die" → "Where chemistry is lost" (section 13 kicker)
  - "Take this with you" → "The mental model" (section 15 kicker)
  - "Look at your frost with better eyes" → "What a loupe shows that a lab result cannot" (section 2 callout)
  - "Buying genetics with your eyes open" → "Verify chemotype before a cultivar earns bench space" (section 6 callout)
  - "Volatility is also why terpenes are the honesty test of a supply chain" → "Flat aroma on a passing THC number means the terpenes have already left" (section 7 callout)
  - "The display jar is a slow incinerator" → "A clear display jar is the worst storage environment you can choose" (section 10 callout)
  - "The mental model to keep" → "One principle: build once, then slow the decay" (section 15 callout)
- analogies added (mechanism → analogy used):
  - Decarboxylation defterm (section 0): baking powder in dough — heat triggers a one-way CO₂ release; kitchen analogy for irreversible heat-driven chemical change
  - Terpene evaporation (section 1): smell rising from a hot pan — the warmer the surface, the faster molecules leave it; kitchen analogy for volatility-with-heat
  - Cannabinoid oxidation (section 1): cut apple browning in a bowl — oxygen converts it slowly, no enzyme needed, no reversing it; household/kitchen analogy for irreversible oxygen-driven degradation
  - Chemotype genetics (section 6): blood type in humans — one locus decides the outcome and you cannot change it after the seed; body analogy for single-locus Mendelian inheritance
  - Vapour pressure / volatility (section 7): cold water versus steaming coffee — molecules with enough energy leave the surface and reach you across the room; kitchen analogy for differential volatility by compound class
- units dual-labelled or flipped: 14
- cuts that might have been content:
  - "the chemistry that matters" (TITLE colon-clause removed)
  - "keep the plant healthy enough to fill the warehouse, and then get out of chemistry's way" → replaced with specific language about filling trichomes and protecting chemistry (section 1 callout)
  - "and the COA will tell on you either way" → replaced with "the COA is the honest record of every choice above" (section 15 callout)
- file: _build/paper_cannabinoids_terpenes.py

### cannabis-tissue-culture-playbook — DONE
- analogies added (mechanism → analogy used):
  - acclimatisation – steam bath / cold air analogy added to section 15 lead (body; shares wet-to-dry too-fast constraint)
- units dual-labelled or flipped: 38
- claims left alone (scientific meaning could not be preserved if rewritten):
  - mL-per-litre concentration ratios (0.5–2 mL/L for PPM) not dual-labelled – denominator L is a concentration unit not a standalone volume, and 0.017–0.07 fl oz adds no practical meaning; left single per judgment call on recipe-ratio context
- file: _build/paper_cannabis_tc_playbook.py

### cannabis-tissue-culture-sop — DONE
- analogies added (mechanism → analogy used):
  - root section lead: acclimatisation introduced with steam-room analogy (speed of transition, not destination) — body/temperature category, shares the too-much-too-fast constraint
- units dual-labelled or flipped: 19
- file: _build/paper_cannabis_tc_sop.py

### cloning — DONE
- headings renamed:
  - TITLE: "Cloning: cuttings that root every time" → "How to root cannabis cuttings"
  - intro title: "Purpose and scope" → "What cloning is and why it works"
  - kicker mother-and-cut: "03 · The how & why" → "03 · Selecting and cutting"
  - kicker hormone-and-cube: "04 · The how & why" → "04 · Hormone and cube"
  - kicker dome-environment: "05 · The how & why" → "05 · Environment"
- analogies added (mechanism → analogy used):
  - air embolism (mother-and-cut callout): straw-bubble analogy — "the same way a bubble trapped in a drinking straw stops the flow"
  - rooting hormone / IBA (hormone-and-cube section): thermostat analogy — "like a thermostat telling a heater to run"
  - VPD (dome-environment section, new paragraph): thirst analogy — "Think of it as how thirsty the air is for water"
- units dual-labelled or flipped: 15
- cuts that might have been content:
  - key-terms warm-up sentence: "Most beginner mistakes come from not knowing what a term means. These six come up constantly." → "These six terms come up throughout this guide. Know them before reading on."
- file: _build/paper_cloning.py

### closed-loop — DONE
- headings renamed:
  - TITLE: 'The closed loop: levers, signal and plant state' → 'Closed-loop grow room: levers, signals and plant state' (removed forbidden 'The' opener)
  - Section 'reading-plant-state' title: 'Sensor and plant-state interpretation' → 'Reading sensors and inferring plant state' (imperative task form)
- analogies added (mechanism → analogy used):
  - Thermostat analogy for 'closed loop' (section what-this-is p()): 'works the way a thermostat does: the room gets too warm, the sensor reads it, the AC turns on...'
  - Weather analogy for VPD defterm: 'Think of clothes drying faster on a hot breezy day than a cold damp one: the air has a bigger gap to fill, so it pulls moisture harder' (wet vs dry constraint)
  - Kitchen analogy for EC drift in EC/VWC/dryback defterm: 'like soup getting saltier as it reduces on the stove' (water leaves, solutes concentrate)
  - Sponge analogy for dryback in EC/VWC/dryback defterm: 'think of it as how much of a sponge wrings out before the next shot'
- analogies removed (ornamental):
  - Figure 1 caption nervous-system analogy removed ('The room works like a nervous system: muscles (the levers), nerves (the sensors) and a mind') — redundant second analogy for closed loop after thermostat was added to the paragraph text; replaced with factual caption describing the diagram structure
- units dual-labelled or flipped: 1
- cuts that might have been content:
  - VPD defterm old body: 'How &lsquo;thirsty&rsquo; the air is. It drives how fast plants lose water. Measured in kilopascals (kPa).' — replaced with plain-English explanation + weather analogy + action guidance
  - EC/VWC/dryback defterm old body: three bare one-liners without analogy — replaced with EC kitchen analogy and dryback sponge analogy
  - Salt creep intro p() old: 'Watch a single ordinary problem, slow <strong>salt creep</strong> in the root zone, travel the whole loop.' — replaced with plain-English definition of salt creep inline before the steps
- file: _build/paper_closed_loop.py

### co2-enrichment — DONE
- headings renamed:
  - Section 03 title: 'CO2 assimilation and flower growth' → 'Leaf photosynthesis and why CO2 level matters' (removed jargon 'assimilation')
- analogies added (mechanism → analogy used):
  - Section 03 (photorespiration/Rubisco): lock-and-key analogy — Rubisco as a lock that fits CO2 perfectly but accepts oxygen as a loose copy; flooding with CO2 keeps the wrong key from getting a turn
  - Section 04 (day/night CO2 flip): drain-and-tap analogy — lights-on period is a fast drain pulling CO2 down with a small tap feeding respiration back; in the dark the drain closes and only the tap runs
  - Section 09 (transpiration, first introduction): slow-water-pump analogy — roots pull moisture up through stems, exits as vapour through leaf stomata; most irrigated water leaves this way
- units dual-labelled or flipped: 7
- cuts that might have been content:
  - Removed 'not X, it's Y' framing from danger callout title (section 12): 'CO2 is a poison, not just a smothering gas' replaced with 'Above 5%, CO2 directly poisons the blood'
  - Removed warm-up opening 'it was tempting to think CO2 crowds out oxygen' from callout body; replaced with direct statement of mechanism
- file: _build/paper_co2_enrichment.py

### coco-crop-steering — DONE
- headings renamed:
  - kicker '05 · The engine' → '05 · The dryback'
  - title 'Dryback: the steering mechanism' → 'Dryback: your main steering lever'
  - kicker '07 · The steering wheel' → '07 · Steering levers'
  - kicker '08 · The arc' → '08 · Week by week'
- analogies added (mechanism → analogy used):
  - EC drift (reading section): glass of seawater left on a sunny bench—same salt in less water tastes saltier
  - Dryback (dryback section): kitchen sponge—you choose how much to let it dry before topping it up
  - Transpiration (steering table caption): skin releasing sweat—faster the plant transpires, the more it drinks
  - VPD (steering paragraph): hot dry wind on skin after a swim—air draws moisture out faster
- units dual-labelled or flipped: 0
- cuts that might have been content:
  - SUB opening line 'Coco coir lets you talk to your plants through water.'
  - kicker '05 · The engine' (metaphor-only heading)
  - kicker '07 · The steering wheel' (metaphor-only heading)
  - kicker '08 · The arc' (metaphor-only heading)
  - title 'Dryback: the steering mechanism'
  - moral ending 'That discipline, not a magic number, is what makes coco repeatable.'
  - table caption 'Most levers act through transpiration, how fast the plant pulls water.'
- file: _build/paper_coco_crop_steering.py

### compliance-track-trace — DONE
- headings renamed:
  - kicker 'The relationship' → 'Regulator relationship'
  - kicker 'Core concept' → 'Batches and lots'
  - kicker 'Systems' → 'Track and trace'
  - kicker 'The test' → 'Audit day'
- units dual-labelled or flipped: 8
- file: _build/paper_compliance.py

### daily-checks — DONE
- headings renamed:
  - TITLE: 'Daily checks: the self-completing facility round' → 'Build a daily facility check that mostly fills itself in'
  - Section intro title: 'Purpose and scope' → 'What this paper covers'
  - Section science kicker: 'The science' → 'Research'
  - Section content kicker: 'The content' → 'What to check'
  - Section autocomplete kicker: 'The automation' → 'Automation setup'
  - Section ui kicker: 'The interface' → 'Interface design'
  - Section ui title: 'Daily-check user interface' → 'Design the check interface for fast logging'
  - Section audit-build kicker: 'Proof & build' → 'Build steps'
- units dual-labelled or flipped: 0
- cuts that might have been content:
  - Removed 'not a character problem' from opening of science section (it's-not-X-it's-Y construct)
  - Removed 'Research-backed · ' prefix from sources meta item
- file: _build/paper_daily_checks.py

### deep-water-culture — DONE
- headings renamed:
  - Section 4 kicker: 'The counter-intuitive part' → 'Aeration rate has a ceiling'
  - Section 5 kicker: 'The misread number' → 'What ORP actually measures'
  - Section 7 kicker: 'The live-reservoir argument' → 'Organics and oxygen headroom'
  - Section 9 kicker: 'The master dial' → 'Temperature first'
  - Section 4 callout title: 'The mechanism: you are stripping the rhizosphere' → 'Aeration strips the chemical layer roots build to feed themselves'
- analogies added (mechanism → analogy used):
  - Section 2 (dissolved oxygen): carbonation-in-a-cold-drink analogy — gas held in liquid up to a temperature-set ceiling, released when warmed or agitated
  - Section 4 (rhizosphere boundary layer): chef's prep-station analogy — seasoning kept right at hand, useless once a fan sweeps the bench
  - Section 5 (ORP): polished-silver-cutlery analogy — stays bright in clean oxidising water, tarnishes in water full of reducing compounds; ORP probe reads that same balance
- units dual-labelled or flipped: 24
- cuts that might have been content:
  - The counter-intuitive part → Aeration rate has a ceiling (section 4 kicker)
  - The misread number → What ORP actually measures (section 5 kicker)
  - The live-reservoir argument → Organics and oxygen headroom (section 7 kicker)
  - The master dial → Temperature first (section 9 kicker)
- file: _build/paper_deep_water_culture.py

### defoliation-training — DONE
- analogies added (mechanism → analogy used):
  - VPD: dry sponge vs saturated sponge — a dry sponge soaks up water fast; a saturated one can barely take any more (shares the absorption-capacity constraint)
- units dual-labelled or flipped: 10
- cuts that might have been content:
  - A beginner's guide to topping, low-stress training… (warm-up framing removed from SUB)
  - (vapour pressure deficit, a combined measure of how 'thirsty' the air is) (replaced with 5-step teacher voice treatment)
- claims left alone (scientific meaning could not be preserved if rewritten):
  - L.zones() title still reads 'density zones (sqft per plant)' — structure arg, untouchable
  - L.zones() note still reads 'Start around 2.3 sqft. Below ~1.8 sqft plants stretch and shade each other.' — structure arg, untouchable
  - L.flow() diagram label still reads 'Bottom 10-18in: remove' — structure arg, untouchable
- file: _build/paper_defoliation_training.py

### energy-sustainability — DONE
- analogies added (mechanism → analogy used):
  - Sensible vs latent load defterm: thermometer-reads-temperature / invisible-vapour analogy replacing sentence fragment
- units dual-labelled or flipped: 18
- file: _build/paper_energy.py

### f2-crop-steering — DONE
- headings renamed:
  - Section title 'Purpose and scope' → 'What the F2 controller is and how it is built'
  - Kicker 'The core loop' → 'Daily cycle'
  - Callout title 'Watch mode is your friend' → 'Use watch mode before going autonomous'
- analogies added (mechanism → analogy used):
  - VWC defterm: sponge analogy — medium holds water like a sponge, some space filled with liquid rest with air
  - EC defterm: body/salt-water analogy — drinking salt water leaves you thirstier despite the liquid; roots face same osmotic barrier
  - Dryback defterm: tidal cycle (weather) analogy — high mark right after a shot fires, low mark just before the next one; the distance between them is what the plant reads
  - Crop steering paragraph: drought/weather analogy — in the wild a plant reads drought as signal time is short and pivots toward reproduction; this system delivers that signal deliberately
- units dual-labelled or flipped: 0
- cuts that might have been content:
  - 'Watching is a discipline worth keeping.' — moral landing removed from expectations final paragraph
- file: _build/paper_f2_crop_steering.py

### facility-3d — DONE
- analogies added (mechanism → analogy used):
  - Leaf boundary layer — warm humid air settling around your face when standing still (body analogy): shares the still-vs-moving-air constraint that determines exchange rate at a surface
- units dual-labelled or flipped: 22
- file: _build/paper_facility_3d.py

### flowering-stages — DONE
- headings renamed:
  - Purpose and scope → What this paper covers
  - Definitions → Six terms you will use throughout
  - Photoperiod change and floral initiation → What the 12/12 flip does to the plant
  - Harvest-readiness assessment → Reading trichomes to find the cut date
  - Expected results and limitations → First-grow expectations and limits
- analogies added (mechanism → analogy used):
  - VPD: wrung-out towel vs soaking-wet towel (dry warm air pulls hard; cool humid air barely pulls)
  - EC: cup of salt water — more dissolved minerals means higher number
  - Trichomes colour change: traffic light — clear means still building, milky means peak, amber means degradation started
- units dual-labelled or flipped: 12
- file: _build/paper_flowering_stages.py

### genetics-phenohunting — DONE
- headings renamed:
  - 'Genotype proposes, environment disposes' → 'One genotype, two environments, two phenotypes'
  - 'Variation is the raw material, not the flaw' → 'Variation is what makes selection possible'
  - 'Carry these three objects' → 'Three principles for the hunt'
- analogies added (mechanism → analogy used):
  - Ethylene as thermostat holding plant in female mode — 'think of it as a thermostat set to keep the plant female' — introduced before STS technical term in section seed-types
- units dual-labelled or flipped: 0
- cuts that might have been content:
  - Moral landing 'It does.' removed from final paragraph of section mental-model
  - Inbreeding depression term moved after plain-English explanation of the mechanism (harmful recessive alleles pairing up) in section stability; parenthetical-term style replaced with bold term after the plain explanation
- file: _build/paper_genetics_phenohunting.py

### gmp-hash-lab — DONE
- headings renamed:
  - 'Purpose and scope' → 'What GMP means for a hash lab'
  - 'Definitions' → 'Terms used throughout this paper'
- analogies added (mechanism → analogy used):
  - Balloon analogy for positive-pressure cascade in pressure-and-people section: 'Think of a balloon with a slow leak: air escapes toward lower pressure, never the reverse.'
- units dual-labelled or flipped: 2
- cuts that might have been content:
  - Removed warm-up sentence from key-terms section: 'A handful of terms do the heavy lifting before any diagram makes sense. You don't need to memorise them: each comes back in context.'
- file: _build/paper_gmp_hash_lab.py

### grow-room-systems — DONE
- headings renamed:
  - TITLE: "The cannabis grow room: a systems guide" → "Cannabis grow room: a systems guide"
  - kicker terms: "02 · The vocabulary" → "02 · Vocabulary"
  - kicker one-system: "03 · The big idea" → "03 · How the parts connect"
  - kicker light: "04 · The biggest lever" → "04 · Light: the main lever"
  - kicker climate: "05 · The air" → "05 · Climate: temperature, humidity, VPD"
  - kicker rootzone: "07 · The supply" → "07 · Root zone and water supply"
  - kicker order: "08 · The method" → "08 · Setup sequence"
  - kicker disease: "09 · The hidden cost" → "09 · Disease risk"
  - callout title one-system: "The one rule that prevents most mistakes" → "One rule that prevents most mistakes"
  - callout title expect: "The mindset that separates good growers from frustrated ones" → "Three habits that keep the system balanced"
- analogies added (mechanism → analogy used):
  - defterm Transpiration: body/sweating analogy — body moves water to skin surface and evaporates to stay cool; plant does the same and carries nutrients upward
  - defterm VPD: sponge analogy — dry warm air is a nearly empty sponge pulling hard; cool humid air is already full and pulls gently
- units dual-labelled or flipped: 0
- cuts that might have been content:
  - "The " opening from TITLE
  - "Those four things are one problem, not four." (unnamed referent in lead)
  - "02 · The vocabulary" → The dropped from kicker
  - "03 · The big idea" → The dropped from kicker
  - "04 · The biggest lever" → The dropped from kicker
  - "05 · The air" → replaced with descriptive kicker
  - "07 · The supply" → The dropped from kicker
  - "08 · The method" → The dropped from kicker
  - "09 · The hidden cost" → The dropped from kicker
  - "The one rule that prevents most mistakes" → The dropped from callout title
  - "The mindset that separates good growers from frustrated ones" → The dropped, rewritten
  - "The best room is not the one with the biggest light. It is the one whose parts are balanced for the light it has" → it's-not-X-it's-Y reframe removed
  - "you can pay the bills downstream" → replaced with explicit explanation
- file: _build/paper_grow_room_systems.py

### harvest-dry-trim-cure — DONE
- analogies added (mechanism → analogy used):
  - sponge analogy for water activity: 'Think of a squeezed sponge sitting in a closed drawer: the water trapped deep in the fibres is harmless; the free surface water is what microbes actually feed on.' Added to first p() of water-activity section, which is the first touchable location introducing the aw mechanism.
- units dual-labelled or flipped: 6
- claims left alone (scientific meaning could not be preserved if rewritten):
  - '60F / 60% RH, 10-14 days' inside L.flow() diagram data in the intro figure remains imperial-only — L.flow() arguments are part of the untouchable figure structure, not caption/text arguments.
- file: _build/paper_harvest_dry_trim_cure.py

### (unknown) — FAILED (null result from agent)
### hvac-dehumidification — DONE
- headings renamed:
  - TITLE: 'HVAC and dehumidification: the machinery of climate' → 'HVAC and dehumidification for grow rooms' (removed colon-then-poetry)
  - Callout heading: 'Engineer a soft landing, not a cliff' → 'Pre-dry the room and ramp the lights down slowly'
  - Callout heading: 'Condensation is the line' → 'Droplets on surfaces at lights-off: act the same night'
  - Callout heading: 'Where rule-of-thumb sizing genuinely breaks' → '…breaks down'
- analogies added (mechanism → analogy used):
  - Latent heat defterm: thunderstorm analogy — humid 26 °C vs dry 26 °C day; same thermometer reading, different energy content
  - Transpiration (section 03): sweat analogy — plant releases vapour through stomata the same way skin releases sweat to cool down; evaporation cools the leaf and pulls water upward
- units dual-labelled or flipped: 18
- cuts that might have been content:
  - SUB rewritten to drop 'survive the night it fails' drama; replaced with explicit reader-outcome statement
- file: _build/paper_hvac.py

### ipm-sop — DONE
- units dual-labelled or flipped: 5
- cuts that might have been content:
  - Replaced imperial-only 'high VPD' with plain English 'hot dry air' in spray-rotation section
- file: _build/paper_ipm_sop.py

### irrigation-manual — DONE
- headings renamed:
  - kicker: 'The physical kit' → 'Physical kit'
  - kicker: 'The core idea' → 'Core concept'
- analogies added (mechanism → analogy used):
  - Dryback defterm — sponge analogy added: always-saturated sponge vs. let-dry-then-refill maps the wet/dry constraint and root-deepening response
  - VPD defterm — body/weather analogy added: sweat evaporating faster on a hot dry day illustrates the air-pull mechanism; full teacher-voice structure applied (plain English → analogy → term defined → consequence)
- units dual-labelled or flipped: 7
- file: _build/paper_irrigation_manual.py

### lab-testing-coas — DONE
- headings renamed:
  - "The one big idea" → "One big idea"
  - "Why turnaround varies" → "Turnaround time varies by method"
  - "And the same factor family applies to CBD" → "CBD uses the same factor family"
  - "How analytical method affects results" → "HPLC versus GC for potency testing"
  - "A flower COA with no THCA row is telling you something" → "A flower COA without a THCA row"
  - "Why Aspergillus is presence/absence, not a count" → "Aspergillus limits use presence/absence, not a count"
  - "The mental model to keep" → "One mental model to keep"
- analogies added (mechanism → analogy used):
  - decarboxylation — baking soda releasing bubbles in a hot pan (section 5 opening paragraph)
  - HPLC — pigments separating on wet paper, some colours travelling further than others (section 6 opening paragraph)
  - qPCR — photocopier for DNA, amplifies target whether organism is alive or dead (section 9 defterm)
  - water activity — sponge held in a fist vs sitting in a bowl, same water content but different availability (section 13 opening paragraph)
- analogies removed (ornamental):
  - Photography/landscape metaphor in section 1 key callout body (replaced with plain-language restatement)
  - Photography/landscape/sunnier metaphor in section 15 key callout body (replaced with plain-language restatement)
- units dual-labelled or flipped: 14
- cuts that might have been content:
  - Extended photography metaphor across both key callouts reduced to single plain-English statement each
- file: _build/paper_lab_testing.py

### light-acclimation — DONE
- headings renamed:
  - TITLE: 'Light acclimation: raise PPFD in steps so plants don't bleach' → 'Raise PPFD in steps so plants don't bleach'
  - kicker how-acclimation-works: 'The why' → 'How the plant adapts to more light'
  - kicker co2-partnership: 'The why, part two' → 'Why CO2 sets your light ceiling'
  - kicker hanging-and-dimming: 'Doing it physically' → 'Adjusting height and output'
  - far-red bold sub-heading: 'Far-red is a dosed scalpel, with a trade-off' → 'Far-red can boost cannabinoid yield in some cultivars but dilute potency in others'
- analogies added (mechanism → analogy used):
  - defterm Acclimation: training-load body analogy added — 'Like gradually increasing a training load: the body adapts to each step before the next one comes'
  - defterm Photoinhibition/bleaching: sunburn analogy added — 'Like sunburn — where UV intensity outpaces your skin's repair rate and oxidises the cells — surplus light drives a damaging chemical reaction inside the leaf'
- units dual-labelled or flipped: 3
- cuts that might have been content:
  - 'Light intensity is not an on/off control. It is' — not-X-it's-Y framing removed from intro
  - 'Light is a curve, not a switch' — metaphor opening removed from SUB
  - 'The why' kicker removed
  - 'The why, part two' kicker removed
  - 'Doing it physically' kicker removed
  - 'Pale, white-tipped upper leaves are not light hunger. They are the leaf burning itself' — not-X-it's-Y framing removed from callout body
  - 'Light is the schedule, not the whole system' — not-X-it's-Y framing removed from expectations intro
  - 'Far-red is a dosed scalpel, with a trade-off' — metaphor-only bold sub-heading removed
- file: _build/paper_light_acclimation.py

### lighting-fundamentals — DONE
- headings renamed:
  - Purpose and scope → What this paper covers
  - Definitions → Five terms that describe plant light
  - Spectrum and plant responses → What each wavelength does to the plant
  - Light intensity and daily light integral: targets by stage → PPFD and DLI targets at each growth stage
  - Photoperiod and floral initiation → How day length triggers flowering
  - LED, HPS and CMH fixtures: efficacy and selection → Choosing a fixture: LED, HPS or CMH
  - Lighting setup by growth stage → Setting height and intensity at each stage
  - Troubleshooting → Diagnosing common light problems
  - Expected results and limitations → What more light can and cannot do
- analogies added (mechanism → analogy used):
  - Sand timer analogy for phytochrome dark-period tracking (photoperiod-flip section): 'think of it as a sand timer that runs only while the lights are off — if anything resets it mid-run, it starts from zero'
  - Solar panel analogy for photosynthesis in intro: 'like a solar panel that makes its own fuel instead of storing electricity'
- units dual-labelled or flipped: 6
- cuts that might have been content:
  - Removed opening 'Light is not just on or off' reframing construct from lead
  - Removed 'This paper assumes you know nothing' (replaced with intelligence-assuming framing)
  - Removed 'Plants eat light' metaphor-only opener from body paragraph
- file: _build/paper_lighting_fundamentals.py

### mother-plants — DONE
- headings renamed:
  - TITLE: 'Mother plants: stock management that never runs dry' → 'Mother plants: environment, feeding, pruning and pathogen defence'
  - Kicker 16: '16 · Take this with you' → '16 · Summary'
- analogies added (mechanism → analogy used):
  - Section 06 apical dominance: thermostat analogy added before technical term — 'Think of a thermostat: one sensor holds multiple heating zones off; the moment it is removed, all zones are free to fire.'
  - Section 08 somatic mutation: photocopy analogy added before mechanism name — 'Think of a photocopy of a photocopy: each generation can carry forward a flaw the original did not have.'
- units dual-labelled or flipped: 5
- cuts that might have been content:
  - Section 03 lead warm-up sentence removed: 'If you only read one section, read this one. Everything after it is the why and the how.' → replaced with direct content pointer
  - SUB tagline ending removed: 'So every batch starts from a plant you can actually trust.'
- file: _build/paper_mother_plants.py

### mould-risk — DONE
- headings renamed:
  - kicker 02: 'The vocabulary' → 'Key vocabulary'
  - kicker 03: 'Know the enemy' → 'Two disease types'
  - callout title: 'They're not the only ones' → 'Other indoor mould species'
  - kicker 04: 'The trigger' → 'Causes and conditions'
  - kicker 05: 'The routine' → 'Prevention steps'
  - kicker 06: 'The habit' → 'Daily scouting'
  - kicker 09: 'The stakes' → 'Health risk'
  - kicker 11: 'Straight talk' → 'Key takeaways'
- analogies added (mechanism → analogy used):
  - RH defterm: sponge that drips once full (RH = how close air is to its water-vapour limit)
  - Water activity defterm: dye locked into fabric — present but not free to move (Aw = only the free moisture fraction)
- units dual-labelled or flipped: 2
- cuts that might have been content:
  - 'Mould isn't bad luck. It is a recipe.' (not-X/is-Y opener) → replaced with direct statement of conditions
  - 'Deny the recipe and you deny the mould.' → 'Remove any one of those and you deny the mould.'
  - RH defterm: 'High RH is mould's best friend.' → expanded into full teacher-voice definition with analogy and action number
  - Water activity defterm: one-liner replaced with plain-English + analogy + threshold number
  - Callout body: 'Spacing and defoliation are mould control, not just tidiness.' → 'Defoliation and plant spacing are effective mould control — they change canopy airflow and humidity directly.'
  - when-found callout: 'it's waste, not something to dry and smoke' → 'it is waste'
  - when-found callout: 'Prevention is the only real cure.' removed → replaced with 'There is no remediation step that makes it safe to use.'
  - expect ol item 3: 'Prevention is the only cure.' removed; sentence recast as positive factual claim
  - expect ol item 4: 'Clean looks and passing tests aren't proof of safety' → 'Cannabis can carry dangerous contamination while looking, smelling, and testing clean'
- claims left alone (scientific meaning could not be preserved if rewritten):
  - Bud rot risk threshold ~70% RH (punja2025-budrot-epi)
  - Flowering RH target 45–65%
  - Canopy air speed ~0.5–1.0 m/s
  - Curing target ~18 °C (64 °F) / 50–55% RH (alubeed2022-postharvest)
  - Water activity threshold ~0.65 for mould inhibition
  - Cannabis users ~3.5× fungal-infection rate vs non-users (benedict2020-cdc)
  - Drying reduces yeast-and-mould counts substantially (sun2025-drying)
  - Standard culture tests can miss Aspergillus (mckernan2016-micro)
- file: _build/paper_mould_risk.py

### nutrient-deficiencies — DONE
- analogies added (mechanism → analogy used):
  - nutrient remobilization (mobility-why-position §1 p): body-breaks-down-muscle-for-vital-organs analogy for how mobile nutrients are stripped from old leaves and redirected to new growth
  - pH lockout (deficiency-vs-toxicity-vs-lockout §1 p): stomach-acid-wrong-strength analogy for why uptake stops regardless of nutrient presence when pH is out of range
  - nutrient antagonism (pitfalls p): sponge-saturated-with-one-liquid analogy for competitive uptake-site blockage by excess potassium
- units dual-labelled or flipped: 0
- cuts that might have been content:
  - SUB: removed warm-up label framing ('A beginner's visual guide to...'); replaced with direct statement of what the paper teaches and what the reader can do
  - Fig 10 caption: removed moral-landing aphorism 'Prevention beats diagnosis every time'; replaced with factual cost comparison
- file: _build/paper_nutrient_deficiencies.py

### nutrient-mixing-athena — DONE
- headings renamed:
  - Purpose and scope → What this paper covers
  - Separate part A and part B stock solutions → Keep Part A and Part B in separate tanks
  - Solubility and mixing conditions → Getting 227 g/L fully into solution
- analogies added (mechanism → analogy used):
  - Osmotic stress — cucumber-in-salt analogy added to callout danger in section targets: 'Picture rubbing coarse salt into a cucumber: the salt draws moisture out through the skin and the cucumber shrivels. Excessive salt in the root zone works the same way — it pulls water out of roots rather than letting the plant take water in.'
- units dual-labelled or flipped: 4
- cuts that might have been content:
  - Removed '(metric)' tag from title — redundant once file uses metric-first throughout
  - Trimmed 'Your whole job is' to 'Your job is' in key callout
  - Removed 'This guide' phrasing in favour of 'This paper'
- file: _build/paper_nutrient_mixing_athena.py

### one-steering-law — DONE
- headings renamed:
  - TITLE: 'The one steering law: coco, rockwool, soil & water' → 'One steering law: coco, rockwool, soil and water' (removed opening 'The'; & → and)
  - kicker 'The one spine image' → 'One spine image'
  - kicker 'The wheel and the engine' → 'Wheel and engine'
  - kicker 'The second dial' → 'Second dial'
  - kicker 'The two limits' → 'Two limits'
  - kicker 'The daily rhythm' → 'Daily rhythm'
  - kicker 'The keystone' → 'Keystone'
- units dual-labelled or flipped: 4
- cuts that might have been content:
  - SUB: removed 'not X, it's Y' construction — 'are not four separate skills. They are one way' → 'share one way of steering a plant with water'
- file: _build/paper_one_steering_law.py

### pest-id — DONE
- units dual-labelled or flipped: 2
- file: _build/paper_pest_id.py

### ph-management — DONE
- headings renamed:
  - Section title 'Purpose and scope' → 'What pH is and why it controls nutrient uptake'
  - Section title 'Definitions' → 'Terms used in this guide'
  - Section kicker 'Making the number' → 'Mixing and adjusting'
  - SUB rewritten: removed 'A beginner's guide to...' framing and 'without chasing ghosts' metaphor; now states what the paper teaches and what the reader will be able to do
- analogies added (mechanism → analogy used):
  - Lockout (why-ph-controls-availability first p): body analogy — supplement tablet that never dissolves passes through the stomach without helping; nutrient is present but in the wrong form for absorption
  - Buffering (key-terms defterm): thermostat analogy — like a thermostat with a wide deadband, the medium absorbs small shifts before the reading moves
  - Alkalinity (adjusting-and-water second p): antacid analogy — like antacid neutralising stomach acid without any change on a pH strip until the antacid is used up; reserve absorbs acid before the reading moves
- units dual-labelled or flipped: 0
- cuts that might have been content:
  - Warm-up sentence removed from what-this-is p(): 'This guide assumes you know nothing about chemistry and builds up from the scale itself to a daily routine you can run.'
  - Warm-up p() removed from key-terms section: 'These words come back through the rest of the guide. Read them once and the troubleshooting section will read cleanly.'
  - Moral-landing bullet removed from expectations callout: 'Consistency over weeks beats chasing perfection on any single reading.'
  - Moral-landing sentence removed from expectations final p(): 'Hold the inflow steadily in range over weeks and most mystery deficiencies never appear.'
- claims left alone (scientific meaning could not be preserved if rewritten):
  - Grower practice pH targets (5.8-6.2 sweet spot for coco/hydro) preserved unchanged
  - Runoff EC monitoring guidance preserved as grower practice
  - Calibration frequency (monthly, two-point) preserved
  - 40-80 ppm CaCO3 alkalinity range for small containers preserved with citation
- file: _build/paper_ph_management.py

### plant-biology — DONE
- headings renamed:
  - kicker '07 · The arc' → '07 · Stage by stage'
  - kicker '08 · The trigger' → '08 · Flowering trigger'
  - kicker '12 · The engine' → '12 · Photosynthesis'
  - kicker '13 · The hidden half' → '13 · Root zone'
  - kicker '14 · The levers' → '14 · Plant hormones'
  - callout title 'The mental model to keep' → 'Mental model to keep'
- analogies added (mechanism → analogy used):
  - Section 04 (transpiration): sponge analogy — 'same effect as a wet sponge releasing moisture from one face while drawing it in from the other' — constraint: moisture moving through a medium due to differential pressure
  - Section 08 (phytochrome): household object analogy — 'slow-draining hourglass: red daylight fills the glass through the day, and darkness drains it slowly overnight' — constraint: capacity drains slowly over time
  - Section 12 (photosynthesis): kitchen analogy — 'more heat under a kitchen pan only speeds cooking until the chef can't keep up; add CO2 and you raise that ceiling' — constraint: capacity ceiling
  - Section 12 (source-sink): household analogy — 'think of it as a household where some members earn income and the rest spend it' — constraint: fixed income, competing demands
- units dual-labelled or flipped: 2
- cuts that might have been content:
  - Removed rhetorical warm-up question 'How does a plant with no eyes measure the seasons?' from section 08 phytochrome opening
  - Removed implicit parenthetical introduction of transpiration '(driven by transpiration from the leaves)' in section 04
- file: _build/paper_plant_biology.py

### plant-biosignal-sensor — DONE
- headings renamed:
  - kicker "03 · The idea" → "03 · How the sensor works"
  - kicker "06 · The hard part" → "06 · Electrode attachment"
  - kicker "08 · Make sense of it" → "08 · Reading the output"
  - kicker "09 · Straight talk" → "09 · Limitations and calibration"
- analogies added (mechanism → analogy used):
  - Biopotential: cell membrane as a tiny battery (positive/negative side)
  - Variation potential: charge shift spreading as an electrical wave (plain-English expansion, no analogy object needed)
  - Action potential: compared to animal nerve signals so first-timers have a reference frame
  - Common-mode rejection: noise-cancelling headphones subtract shared sound, leaving only the difference
  - Contact impedance: loose headphone jack — poor connection weakens signal and lets noise in
  - Half-cell potential: lemon and two different coins making a battery — ions exchanging at the surface build a small voltage that settles over time
- units dual-labelled or flipped: 2
- cuts that might have been content:
  - "for the price of a night out" → "for about NZ$110"
- file: _build/paper_plant_biosignal.py

### plant-state-dashboard — DONE
- headings renamed:
  - TITLE: "From telemetry to intelligence: the plant-state dashboard" → "Designing a plant-state dashboard for your grow room" (marketing tagline removed; replaced with task-label a beginner can use)
- analogies added (mechanism → analogy used):
  - dashboard-surface p(): plain-English introduction of pre-attentive processing added before the technical term — "Before you consciously focus on any text, your eye has already picked up the status colour, the position on screen, and the one bold line" — then the term is named and defined
- units dual-labelled or flipped: 0
- cuts that might have been content:
  - "Here is how to design one that does." (SUB — replaced with sentence stating what reader will be able to do)
  - "This is not a boil-the-ocean rebuild. Each stage ships value and earns the next" (how-to p — idiom removed, replaced with plain phrasing)
  - "A calm dashboard leans on pre-attentive cues, a single status colour, position, one bold line, that the eye reads before conscious attention engages, so the 'all clear' state is grasped at a glance" (dashboard-surface p — technical term was leading; rewritten to put plain English first, then name the term)
- file: _build/paper_plant_state_dashboard.py

### pppe — DONE
- units dual-labelled or flipped: 2
- cuts that might have been content:
  - Removed warm-up sentence: 'It is worth sitting with the numbers, because they are the entire argument for gowning up.'
- file: _build/paper_pppe.py

### ripening-harvest-timing — DONE
- headings renamed:
  - Flushing: evidence and limitations → Flushing and what testing found
- analogies added (mechanism → analogy used):
  - cut-apple browning (oxidation, THC→CBN, sec 04)
  - body pulling blood from fingers to core (nutrient remobilisation / the fade, sec 04)
  - air-as-sponge: warm holds more vapour, cool holds less (RH rises when temperature drops, sec 08)
- units dual-labelled or flipped: 8
- file: _build/paper_ripening.py

### rockwool-crop-steering — DONE
- headings renamed:
  - TITLE: 'Crop steering in rockwool: drybacks, saturation and the breaking point' → 'Crop steering in rockwool: water content, drybacks, and the recovery floor'
  - kicker 'The main lever' → 'Daily dryback' (section id: dryback)
  - kicker 'The cliff' → 'Recovery floor' (section id: breaking-point)
  - kicker 'The lever in use' → 'Steering in practice' (section id: steering)
- analogies added (mechanism → analogy used):
  - dryback (section 5 lead paragraph): wet sponge left on the bench — starts soaked, air and plant draw water out through the day, the amount lost is the dryback
  - cation-exchange capacity (section 3 figure caption): soil particles act like a magnet holding iron filings — rockwool fibres carry almost no such charge, so salts stay dissolved and fully available
  - EC concentration during dryback (section 6 paragraph): pot of stock reducing on the stove — as liquid goes down, flavour concentrates
  - osmotic stress (section 6 figure caption): salting a cucumber pulls moisture through the skin in the wrong direction — when root-zone EC is too high, the same reversal occurs across the root cell wall
  - channeling / preferential flow (section 7 figure caption): pouring water onto very dry cracked soil — it runs in rivulets to the drain while the earth between cracks stays dry
- units dual-labelled or flipped: 0
- file: _build/paper_rockwool_crop_steering.py

### root-zone-teros12 — DONE
- headings renamed:
  - TITLE: 'Root-zone state estimation with the TEROS-12 sensor' → 'What your TEROS-12 measures and how to steer irrigation on it'
  - section 'what-this-is' title: 'Purpose and scope' → 'What this guide covers'
  - section 'key-terms' title: 'Definitions' → 'Terms defined once, used throughout'
  - section 'how-it-measures' title: 'TEROS-12 measurement principle' → 'How the probe measures water without touching it'
  - section 'calibration' title: 'TEROS-12 calibration' → 'Why you must calibrate to your exact substrate'
  - section 'ec-and-limits' title: 'Root-zone EC and sensor limitations' → 'What the EC reading tells you and where it breaks down'
  - section 'steering' title: 'Irrigation steering with TEROS-12' → 'Steering irrigation from TEROS-12 readings'
  - section 'troubleshooting' title: 'Troubleshooting' → 'Diagnosing a bad reading before blaming the sensor'
  - section 'expectations' title: 'Expected results and limitations' → 'What one probe can earn and what it cannot'
  - callout title: 'The cardinal safety rule' → 'Temperature and EC should move your trust, not the water number'
  - callout title: 'Never hard-write your anchors' → 'Anchors must be earned from multiple events'
  - callout title: 'What one probe can and cannot earn' → 'The honest account'
  - steps title: 'Require a second witness' → 'Confirm with a second witness before moving water'
  - steps title: 'Steer on shape, gated by safe headroom' → 'Steer on the dryback slope, bounded by safe headroom'
- analogies added (mechanism → analogy used):
  - Permittivity (key-terms defterm): wet sponge conducts electricity far better than a dry one — water does almost all the electrical work
  - Permittivity (how-it-measures section p): same wet-sponge contrast restated in measurement context
  - Bulk EC vs pore-water EC (ec-and-limits section p): measuring saltiness of a wet sponge by pushing current through the whole thing — sponge fibre and water together — then Hilhorst estimates saltiness of water alone
- units dual-labelled or flipped: 11
- cuts that might have been content:
  - Warm-up sentence 'Here is the small set of words this whole field hangs on. You don't need to memorise them.' → replaced with direct statement of what the section does
  - Redundant 'from zero' in lead (kept the meaning, trimmed the phrasing)
  - Original callout title 'The cardinal safety rule' (opaque) replaced with content-stating title
  - Moral-landing phrasing 'Get the probe calibrated...' replaced with direct instructional close
  - Original troubleshooting callout body had 'chase ghosts' idiom — rewritten as 'irrigating in response to physics, not plant need' (concrete, no idiom)
- file: _build/paper_root_zone_teros12.py

### scaling-high-light — DONE
- analogies added (mechanism → analogy used):
  - hot humid day (sensible vs latent heat — defterm Sensible vs latent load)
  - straw-pull evaporation (transpiration stream / mass flow — defterm Mass flow)
  - salt on cucumber slice (osmotic pressure — EC section p)
  - still water at riverbed (boundary layer — airflow section p)
- units dual-labelled or flipped: 38
- file: _build/paper_scaling_high_light.py

### seeds-germination — DONE
- analogies added (mechanism → analogy used):
  - VPD: air-as-sponge analogy in seedling-care p() — dry sponge pulls hard, humid sponge pulls gently
  - EC: salt-in-water analogy in seedling-care p() — too little starves, too much burns
- units dual-labelled or flipped: 9
- file: _build/paper_seeds_germination.py

### signal-and-noise — DONE
- headings renamed:
  - Signal and noise: precision cultivation → Tell real plant changes from sensor noise
  - Purpose and scope → What you will learn to do
  - Definitions → Key terms in plain language
  - Operating procedure → Eight steps to reduce noise this week
- analogies added (mechanism → analogy used):
  - replication: asking passersby on a rainy street (weather analogy, 20 people outvoting the outlier) — placed before technical term
  - aliasing: wagon wheel spinning backwards in an old film (restructured from after the technical term to before it, per sequence rule)
  - hunting: thermostat set too sensitive, overshoots heat then cool continuously (thermostat analogy) — new, placed before technical term
- units dual-labelled or flipped: 3
- cuts that might have been content:
  - Warm-up sentence 'The hard part of growing has moved from collecting data to reading it' from intro paragraph
  - Reassurance filler 'so the words can sound intimidating. They are not.' from key-terms opening paragraph
  - Not-X-it's-Y reframe 'You don't have a data problem. You have a signal-to-noise problem.' from one-line-reframe callout
- file: _build/paper_signal_and_noise.py

### smart-watering-vrwe — DONE
- headings renamed:
  - Signal fusion for root-zone water estimation → Combining sensors to outvote one lying reading
- analogies added (mechanism → analogy used):
  - Transpiration — sweating analogy: body loses more water when hot and active, estimate from temperature and effort; shares the real constraint of invisible continuous water loss driven by ambient conditions
  - Channeling — pot-liner-gap analogy: water finds the gap between pot wall and liner and runs straight down while the substrate beside it stays dry; shares the wet-vs-dry constraint of water bypassing the intended medium
- units dual-labelled or flipped: 0
- file: _build/paper_smart_watering_vrwe.py

### substrates-overview — DONE
- headings renamed:
  - 'Purpose and scope' → 'What a substrate is'
- analogies added (mechanism → analogy used):
  - CEC: sponge analogy — 'hold nutrient ions the way a sponge holds water'
  - Buffering: thick-walls analogy — 'room with thick walls where a cold draught outside barely registers inside'
  - Dryback: garden-tap analogy — 'briefly turning off a garden tap so the plant reaches further'
- units dual-labelled or flipped: 4
- cuts that might have been content:
  - Removed bare 'come pre-loaded with potassium and sodium and will strip calcium and magnesium out of your feed' — replaced with causal chain explaining the swap mechanism
  - Removed 'Purpose and scope' section title — replaced with beginner-usable label
- file: _build/paper_substrates_overview.py

### temp-humidity-vpd — DONE
- headings renamed:
  - TITLE subtitle: 'the air the plant feels' → 'stage targets, measurement and condensation control'
  - kicker s08: '08 · The engine' → '08 · Transpiration and growth'
  - kicker s10: '10 · The mould lever' → '10 · Condensation and mould risk'
  - callout s06: 'Two roads to the same number are not the same room' → 'Same VPD number, two different climates'
  - callout s09: 'Night temperature is also a shape lever' → 'Night temperature also affects internode length'
  - callout s15: 'Five things, and you understand grow-room climate' → 'Five principles of grow-room climate control'
- units dual-labelled or flipped: 38
- cuts that might have been content:
  - Section 15 moral-landing sentence: 'Get the gap right, keep it steady, and most of what growers call magic touch turns out to be psychrometrics.'
- file: _build/paper_temp_humidity_vpd.py

### tissue-culture — DONE
- headings renamed:
  - kicker 04: The map → 04: Workflow overview
  - kicker 05: The clever bit → 05: How the meristem stays clean
  - kicker 08: The food → 08: Preparing the medium
  - kicker 12: The cleanup → 12: Meristem dissection
  - kicker 13: The proof → 13: Disease testing
  - kicker 17: The payoff → 17: The clean mother plant
  - h3 Why HpLVd is such a big deal → HpLVd: spread, cost and impact
  - callout Why you can't just spray it away → Sprays cannot cure a viroid infection
  - h3 How long does the whole thing take? → Realistic timelines
  - h3 How well does it actually work? → HpLVd clearance rates by strain
  - callout How to index properly: timing is everything → Indexing: when and what to test
  - callout Why losses are high here, and that's OK → High initiation losses are normal
  - callout Totipotency: the property that makes all of this work → Totipotency: why a tiny piece can grow a whole plant
  - h3 What success rates to actually expect → Success rates: published best-case vs beginner first run
  - h3 What it costs → Cost overview
- analogies added (mechanism → analogy used):
  - Totipotency (section 2): sealed-copy-of-building-instructions analogy — every cell holds the full blueprint but most only use one page; the right signals open it and restart from page one
  - Hyperhydricity (section 14): sponge-in-still-water analogy — permanently saturated, never forced to drain, never developing structure that lets it hold shape in open air; constraint shared is wet vs dry
- units dual-labelled or flipped: 11
- cuts that might have been content:
  - Warm-up paragraph in section 05 ('This is the single most important concept in the whole guide. Once it clicks…') removed — content starts directly with the mechanism
  - Opening p in section 20 ('So you can decide with eyes open.') replaced with a direct action sentence
- claims left alone (scientific meaning could not be preserved if rewritten):
  - ~90% facility infection rate in one California testing programme
  - ~40% HpLVd positives in Canadian retail flower
  - up to ~50% cannabinoid loss in severe dud outbreaks
  - 100% seed transmission reported in 2025 North American study
  - RT-qPCR spread timing: roots ~2–3 weeks, foliage ~4–6 weeks
  - ~55% usable explants published initiation survival / 90–95% loss in some varieties
  - IBA ~2.5 µM gives ~95% rooting, ~5 roots per shoot
  - 5 of 13 cultivars cleared in the 13-cultivar thermotherapy+meristem study
  - Cryo recovery ~55–63% of tips
  - Mutation accumulation near-linear with subculture count (Torkamaneh 2024)
  - 5-subculture reset rule
- file: _build/paper_tissue_culture.py

### transplanting — DONE
- analogies added (mechanism → analogy used):
  - Transpiration as a pump (sec 08): 'like a slow continuous pump: the hotter and drier the air, the faster the pump runs'
  - VPD as thirst (sec 08 step 8): 'how thirsty the air is for water — a hot dry room pulls hard on every leaf surface, a cooler, moister room pulls gently'
  - Capillary flow as wicking (sec 09): 'works like water wicking up a paper towel'
  - Osmotic stress as raisin-in-saltwater (sec 11): 'like a raisin in saltwater; this is osmotic stress'
- units dual-labelled or flipped: 18
- cuts that might have been content:
  - Removed 'it's not X, it's Y' reframe in sec 03: 'A container isn't just a bucket that holds media. It's a hard limit' → 'A container is a hard limit'
  - Replaced 'capillarity' with 'capillary flow' throughout secs 09 and 12 to match the defined term
  - Revised sec 02 warm-up close: 'every later section reads in plain English' → 'the rest of the paper uses them freely'
  - SUB revised to add action framing: 'how to read and prevent transplant shock' replaces 'transplant shock from cause to recovery'
- file: _build/paper_transplanting.py

### under-canopy-lighting — DONE
- headings renamed:
  - TITLE: 'Under-canopy lighting: photons at the floor' → 'Under-canopy and inter-canopy lighting for indoor cannabis'
  - Section light-history title: 'Light acclimation in the lower canopy' → 'How leaves adjust to their light environment'
  - Callout 'Photobleaching' → 'Photobleaching risk'
  - Callout 'Proven vs plausible' → 'Solid science vs grower practice'
  - Section evidence: 'TL vs SCL vs ICL head to head' → 'top-light vs SCL vs ICL head to head'
  - Section training sub-heading: 'The gyping reversal' → 'The lollipopping reversal'
- analogies added (mechanism → analogy used):
  - Photosynthesis (section 1): 'like a coloured filter — upper leaves pull out red and blue before the beam reaches the next layer'
  - Photoacclimation (section 5): 'like training for altitude — a body that trained at sea level does not perform the same at elevation'
  - Transpiration (section 8): 'like sweating — cools the leaf but loads moisture into the room air'
  - VPD (section 9): 'the air's thirst for moisture — dry warm air has high VPD and pulls strongly; cool humid air pulls less'
  - Photobleaching (section 3): 'like a photograph left in the sun — pigments break down and tissue loses colour and function'
  - Far-red shade-avoidance (section 3): plain-English explanation of the shade detection signal and stretch response replacing jargon-only treatment
- units dual-labelled or flipped: 9
- cuts that might have been content:
  - Removed abstract use of 'larf' without definition (replaced with 'sparse, underweight bud'; larf still defined on first use in section 1)
  - 'PSI and PSII' acronyms replaced with 'the two photosynthetic reaction centres (photosystems I and II)'
  - Removed 'Tons = total BTU/hr ÷ 12,000' imperial-only cooling formula, replaced with metric kW formula
  - Removed 'the part most guides skip, the thermal and airflow bill that comes due' run-on structure; clarified with em-dash
- file: _build/paper_under_canopy_lighting.py

### unit-economics — DONE
- headings renamed:
  - 06 kicker: 'The aging metric' → 'g/W as a dated metric'
  - 09 kicker: 'The sneaky #1' → 'Labour costs in detail'
  - 10 kicker: 'The hidden multiplier' → 'Cycles per year'
  - 16 kicker: 'The mental model' → 'Control variables'
- units dual-labelled or flipped: 8
- cuts that might have been content:
  - Removed warm-up opener 'Beginner-first, as always.' from section 01 final paragraph
- file: _build/paper_unit_economics.py

### veg-management — DONE
- headings renamed:
  - kicker 'The clock inside the pot' → 'Container size sets the veg window'
  - kicker 'Below the deck' → 'Root zone before the flip'
  - kicker 'The business of days' → 'Veg length and room economics'
- analogies added (mechanism → analogy used):
  - Photosynthesis: kitchen-in-reverse analogy (leaf uses light to make sugar, like a kitchen burning fuel for heat but reversed)
  - VPD: wet sponge on a warm counter (dries fast on a dry day, stays damp on a humid day — the plant leaf is the sponge)
  - Dryback: sponge after washing dishes (keeps releasing water long after you put it down — healthy roots do the same overnight)
  - Root-bound thermostat: thermostat stuck at a lower setting — plant looks fine on the outside but growth rate is quietly throttled
- analogies removed (ornamental):
  - Root-bound as 'a solar array running at part load' (technology analogy not on the approved list; replaced with thermostat)
- units dual-labelled or flipped: 12
- file: _build/paper_veg_management.py

### water-quality — DONE
- headings renamed:
  - title: 'Purpose and scope' → 'What this paper covers'
  - title: 'Definitions' → 'Key terms'
- analogies added (mechanism → analogy used):
  - Alkalinity defterm: thermostat analogy — 'like a thermostat wired to push the water back toward neutral: after you dose acid to reach pH 5.8, dissolved carbonates slowly neutralise the acid and pH climbs back up over hours to days'
- analogies removed (ornamental):
  - Section alkalinity-carbonates body: 'acts like a chemical spring' removed — not on approved analogy list; replaced with direct factual language
- units dual-labelled or flipped: 17
- cuts that might have been content:
  - 'absolute beginner' → 'beginner' in intro callout (warm-up qualifier removed)
  - 'home growers' → 'growers' in expectations callout (unwarranted narrowing removed)
  - 'bad genetics, poor light' → 'poor genetics, insufficient light' in expectations body
  - Hyphen ranges replaced with en-dashes throughout (numeric ranges: 0-20, 40-100, 30-60, 100-150, 0-10, 100-200, 1-4, 5.8-6.2, 6.2-6.8, 150-300, 0-14, 5.8-6.0, 30-100)
- file: _build/paper_water_quality.py

## PHASE 2
Both files valid. Final report:

---

**glossary terms total:** 388
**terms with slug:** 388
**terms null (orphaned):** 0

**null-slug terms:** none

**total new phrases added to links.py:** 569 total entries, up from ~253 original entries — approximately **316 new phrases** added. One new slug entry created: `scaling-high-light`.

**phrase collisions found and resolved:** 1
- `"shade avoidance"` appeared in both `defoliation-training` and `lighting-fundamentals`. Removed from `defoliation-training`; retained in `lighting-fundamentals` (matches the term "Shade avoidance response" slug assignment).

**collisions intentionally avoided (phrases not added due to pre-existing assignment in another slug):**
- `"humidity dome"` — already in `cloning`; not added to `seeds-germination`
- `"DLI"` — already in `grow-room-systems`; not added to `lighting-fundamentals`
- `"PPFD"` — already in `light-acclimation`; not added to `lighting-fundamentals` (added `"PPFD map"` instead, which is longer and resolves first)
- `"life cycle"` — already in `plant-biology`; not added to `pest-id`
- `"dissolved oxygen"` — already in `deep-water-culture`; not added to `water-quality`
- `"photoperiod"` — already in `lighting-fundamentals`; used `"photoperiod plant"` for `flowering-stages` instead
- `"trichome"` — already in `harvest-dry-trim-cure`; used `"trichome color change"` for `ripening-harvest-timing` instead
- files touched: glossary.json, _build/links.py

## Post-workflow manual fixes (section title gate)

The build gate in check_section_structure.py requires the first section title be exactly "Purpose and scope". Agents renamed these, which was correct per the heading rules but violated the structural gate. Fixed by restoring first section title only (body content kept as rewritten):

- cloning: "What cloning is and why it works" → "Purpose and scope"
- daily-checks: "What this paper covers" → "Purpose and scope"
- f2-crop-steering: "What the F2 controller is and how it is built" → "Purpose and scope"
- flowering-stages: "What this paper covers" → "Purpose and scope"
- gmp-hash-lab: "What GMP means for a hash lab" → "Purpose and scope"
- lighting-fundamentals: "What this paper covers" → "Purpose and scope"
- nutrient-mixing-athena: "What this paper covers" → "Purpose and scope"
- ph-management: "What pH is and why it controls nutrient uptake" → "Purpose and scope"
- root-zone-teros12: "What this guide covers" → "Purpose and scope"
- signal-and-noise: "What you will learn to do" → "Purpose and scope"
- substrates-overview: "What a substrate is" → "Purpose and scope"
- water-quality: "What this paper covers" → "Purpose and scope"

Additional canonical title fixes:
- water-quality section 'key-terms': "Key terms" → "Definitions"
- signal-and-noise section 'key-terms': "Key terms in plain language" → "Definitions"
- nutrient-mixing-athena section 'cardinal-rule': "Keep Part A and Part B..." → "Keep part A and part B..." (sentence case)
- lab-testing-coas section 'methods': Added "HPLC", "GC", "UPLC", "LC-MS", "GC-MS" to ACRONYMS in check_section_structure.py (these are standard analytical chemistry acronyms omitted from the original list)

hash-rosin-pressing: Phase 1 agent failed (32K output token limit). Reprocessing via separate agent.

## Post-review corrections

### Canonical section titles — reverted (8 strings, 5 papers)
`"Definitions"` and `"Expected results and limitations"` are load-bearing identifiers, not prose.
build.py:202 locates the section titled exactly "Definitions" and inserts the evidence/provenance
panel after it, falling back to position 1 when not found. Renaming them silently relocated the
evidence panel above the vocabulary in 5 papers, and disabled two ordering gates in
check_section_structure.py:203-214 (both guard on `is not None`, so a missed lookup skips the check
rather than failing it).

Reverted to canonical: flowering-stages, gmp-hash-lab, lighting-fundamentals, ph-management,
root-zone-teros12. All other teacher-voice heading renames in those papers were kept.

### Glossary slugs — rebuilt against the correct source
glossary.json is a BUILD ARTIFACT, regenerated by export_corpus.py:376 from data/glossary.py on
every build. The first slug pass wrote to it directly and was overwritten by the next build.

Fix: slugs now live in `_build/data/glossary_slugs.py` (TERM_SLUGS dict, 388 entries), applied by
a merge block in `data/glossary.py` after the glossary_gen* merge. Verified to survive a rebuild.

- 388/388 terms mapped, 0 orphans, 0 invalid slugs, 0 dead targets (every slug resolves to a real page)
- 45 distinct home papers
- 3 corrected after review — mapped to papers with ZERO mentions of the term:
    Calvin cycle             co2-enrichment    -> light-acclimation
    Reactive oxygen species  scaling-high-light -> light-acclimation
    Bleaching                scaling-high-light -> light-acclimation
- links.py: removed "Calvin cycle" from co2-enrichment (same dead-destination bug); 568 phrases

### Verification
build OK, 55 papers, all gates clean; evidence panel correctly after Definitions in all 5 papers;
every glossary slug resolves; links.py imports.
