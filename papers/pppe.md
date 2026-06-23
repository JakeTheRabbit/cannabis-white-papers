---
slug: "pppe"
title: "PPPE: plant and personal protective equipment"
eyebrow: "Plant health · PPE & biosecurity"
summary: "Coveralls, hairnets, gloves and shoe covers do two jobs at once: they keep the human safe, and they keep the human's particles, microbes and pests off the crop. People are the number-one contamination source in any clean space. This is the full rundown: how bad we are, the bare minimum, the room-by-room kit, and the procedures that actually work."
track: "Plant health"
read_time: "~17 min read"
diagrams: "9 diagrams"
related: ["ipm-sop", "mould-risk", "tissue-culture", "daily-checks"]
url: "https://jaketherabbit.github.io/cannabis-white-papers/pppe.html"
md_url: "https://jaketherabbit.github.io/cannabis-white-papers/papers/pppe.md"
version: "1.0"
updated: "2026-06-24"
license: "CC BY-NC 4.0"
license_url: "https://creativecommons.org/licenses/by-nc/4.0/"
attribution: "The Cannabis White Papers"
refs: [{"id": "cleanroom-humans-source", "n": 1, "cite": "Cleanroom contamination analyses: personnel account for roughly 70-90% of contamination; a gowned worker emits ~100,000 particles/min at rest, ~1,000,000 walking, up to ~5,000,000 in active work.", "url": "https://www.precgroup.com/70-percent-of-cleanroom-contamination/", "peer": false}, {"id": "cdc-skin-squames", "n": 2, "cite": "Noble / CDC Emerging Infectious Diseases: humans disseminate ~10^7 skin squames per day, of which roughly 10% carry viable bacteria.", "url": "https://wwwnc.cdc.gov/eid/article/7/2/70-0225_article", "peer": true}, {"id": "human-microbial-cloud", "n": 3, "cite": "Human microbial-emissions research: an occupied space gains roughly 37 million bacterial and 7 million fungal genome copies per person per hour above the unoccupied baseline.", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7950481/", "peer": true}, {"id": "phone-fomite", "n": 4, "cite": "Mobile phones as fomites: cultured phones average far higher bacterial loads than a public toilet seat (order-of-magnitude), isolates including S. aureus, E. coli and Candida.", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3939586/", "peer": true}, {"id": "shoe-floor-contamination", "n": 5, "cite": "Shoe-sole and floor contamination: soles carry MRSA, C. difficile, E. coli and other organisms; walking re-disperses settled organisms, contributing a meaningful share of airborne CFU.", "url": "https://www.infectioncontroltoday.com/view/shoe-sole-and-floor-contamination-new-consideration-environmental-hygiene", "peer": true}, {"id": "hlvd-transmission-2025", "n": 6, "cite": "Mechanical transmission and management of Hop Latent Viroid (HLVd) in cannabis: spread via contaminated tools and cuttings, up to 100% transmission within four weeks; controls include fresh gloves per plant, tool sterilisation and footbaths. Plants (MDPI) 2025, 14:830.", "url": "https://www.mdpi.com/2223-7747/14/5/830", "peer": true}, {"id": "hand-hygiene-logreduction", "n": 7, "cite": "Comparative hand-hygiene efficacy: alcohol-based handrub achieves a larger log reduction (~3 log, ~83%) than plain soap-and-water washing (~2 log, ~58%); neither sterilises.", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC117885/", "peer": true}, {"id": "toilet-plume", "n": 8, "cite": "Toilet-flush bioaerosol ('toilet plume'): a flush lofts aerosols to ~1.5 m within seconds; particles remain viable for minutes to hours, and a closed lid produces markedly less aerosol.", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9732293/", "peer": true}, {"id": "fda-21cfr117-personnel", "n": 9, "cite": "US FDA. 21 CFR 117.10, Personnel (current good manufacturing practice for food): clean outer garments, personal cleanliness, hand washing, hair restraints, glove integrity.", "url": "https://www.ecfr.gov/current/title-21/chapter-I/subchapter-B/part-117/subpart-B", "peer": false}, {"id": "who-gacp-2003", "n": 10, "cite": "World Health Organization (2003). WHO guidelines on good agricultural and collection practices (GACP) for medicinal plants.", "url": "https://www.who.int/publications/i/item/9241546271", "peer": false}, {"id": "who-hand-hygiene", "n": 11, "cite": "World Health Organization. Hand hygiene: the Five Moments and recommended technique (soap-and-water 40-60s; alcohol-based handrub 20-30s, ≥60% alcohol).", "url": "https://www.who.int/teams/integrated-health-services/infection-prevention-control/hand-hygiene", "peer": false}, {"id": "cdc-glove-removal", "n": 12, "cite": "US CDC. How to safely remove gloves: glove-to-glove then skin-to-skin, peeling inside-out so bare skin never contacts the contaminated exterior; hand hygiene before and after.", "url": "https://www.cdc.gov/ebola/media/pdfs/2024/05/poster-how-to-remove-gloves.pdf", "peer": false}, {"id": "gmp-gowning-procedure", "n": 13, "cite": "GMP / cleanroom gowning and de-gowning procedures: top-to-bottom donning order across a clean/dirty demarcation bench, reverse dirtiest-first removal.", "url": "https://www.pharmanow.live/pharma-manufacturing/cleanroom-gowning-procedures-guide", "peer": false}, {"id": "hswa-2015", "n": 14, "cite": "Health and Safety at Work Act 2015 (NZ): s36 PCBU primary duty of care; s45 worker duties; s27 PCBU must provide what is required (including PPE) and must not charge workers for it.", "url": "https://www.legislation.govt.nz/act/public/2015/0070/latest/DLM5976894.html", "peer": false}, {"id": "worksafe-grwm", "n": 15, "cite": "WorkSafe New Zealand and the Health and Safety at Work (General Risk and Workplace Management) Regulations 2016, reg 6: control risk by the hierarchy of controls, with PPE as the last resort.", "url": "https://www.worksafe.govt.nz/managing-health-and-safety/getting-started/introduction-hswa-special-guide/", "peer": false}]
---

# PPPE: plant and personal protective equipment

_Plant health · PPE & biosecurity · ~17 min read_

> Coveralls, hairnets, gloves and shoe covers do two jobs at once: they keep the human safe, and they keep the human's particles, microbes and pests off the crop. People are the number-one contamination source in any clean space. This is the full rundown: how bad we are, the bare minimum, the room-by-room kit, and the procedures that actually work.

## Two jobs, one suit

PPE in a grow is not really about you. In most rooms the gear is there to protect the **plant** from you: from the skin you shed, the spores on your jacket, the mites on your shoes and the viroid on your hands. The same coverall that keeps your clothes clean also keeps your contamination off the crop. That is why we call it PPPE, plant _and_ personal protective equipment.

People are the dominant contamination source in any clean space, on the order of **70 to 90 percent** of it[^cleanroom-humans-source]. You cannot stop a human shedding. You can only put a barrier around the human and move them through the building in a controlled way. That is the whole game.

> **KEY — Why this pays for itself**
> 
> One contaminated mother plant or one shared glove can spread Hop Latent Viroid to an entire crop, with up to **100% transmission within four weeks** of propagation from infected stock[^hlvd-transmission-2025]. The spread is mechanical, on tools, cuttings and hands, not airborne. Gloves-per-plant and gowning are not box-ticking; they are crop insurance.

> **NOTE — Two different reasons to gown**
> 
> In cultivation, dry and trim, PPE protects the product. In **extraction** it flips to protecting the worker (solvents, fire), and in the vault it is mostly security. Same word, different purpose, different kit. This paper is about the biosecurity side, with the legal duties that sit under all of it.

## The words you need

**PPE / PPPE** — Personal protective equipment. Here, plant _and_ personal: the same gear protects the crop from the person and the person from hazards.

**Gowning / de-gowning** — Putting on (donning) and taking off (doffing) protective clothing in a defined order, across a clean/dirty line, so contamination never crosses.

**Fomite** — An object that carries and transfers microbes, a phone, a pen, a door handle, a tool. Hands move contamination from fomite to crop.

**Bioaerosol** — Airborne particles carrying living things, skin flakes with bacteria, fungal spores, droplets from speech or a toilet flush.

**Cross-contamination** — Moving contamination from a dirty area or item to a clean one, for example walking from flower back into propagation without re-gowning.

**Hierarchy of controls** — The legal order for managing risk: eliminate, substitute, isolate, engineer, administrate, and only then PPE as the last line[^worksafe-grwm].

**PCBU** — Person Conducting a Business or Undertaking, the NZ legal term for the duty-holding business (your employer) under the Health and Safety at Work Act[^hswa-2015].

**Reasonably practicable** — The legal standard for how far you must go: weigh the risk against the effort and cost of controlling it. High-consequence, cheap-to-control risks must be controlled.

## How bad humans actually are

It is worth sitting with the numbers, because they are the entire argument for gowning up.

> **Diagram.** People are the number-one contamination source in a clean space[^cleanroom-humans-source]. You shed roughly ten million skin flakes a day, about a tenth carrying live bacteria[^cdc-skin-squames], and an occupied room gains tens of millions of bacteria and millions of fungal spores per person per hour[^human-microbial-cloud].

- **Movement is the multiplier.** A gowned person emits about 100,000 particles a minute standing still, a million walking, and up to five million working fast[^cleanroom-humans-source]. Slow, calm movement is itself a control.
- **Your phone is filthier than a toilet seat.** Cultured phones carry roughly an order of magnitude more bacteria than a public toilet seat, and they ride to your face and back to your hands all day[^phone-fomite].
- **Your shoes are a pest and spore taxi.** Soles carry live pathogens and fungal spores, and walking re-launches settled organisms into the air[^shoe-floor-contamination]. Mites and powdery mildew arrive on clothing and footwear.
- **The toilet throws a plume.** A flush lofts aerosols to about 1.5 m within seconds, viable for minutes to hours; a closed lid cuts it sharply[^toilet-plume].

> **NOTE — Hands are the main bridge, and hygiene is not a cure**
> 
> Washing helps but does not sterilise: an alcohol rub removes about 83% of organisms, plain soap and water about 58%[^hand-hygiene-logreduction]. That is why hand hygiene is a frequent loop at every transition, and why gloves and barriers carry the rest.

## The bare minimum, everywhere

Before any room-specific extras, there is a non-negotiable baseline for entering any production or handling area. It mirrors food-GMP personnel rules[^fda-21cfr117-personnel] and WHO good agricultural and collection practice[^who-gacp-2003].

1. **Clean, dedicated outer garment** put on at entry (gown, smock, scrubs or coverall), never your street clothes.
2. **Hair fully restrained**, bouffant or hairnet, plus a beard cover for facial hair.
3. **Single-use nitrile gloves**, intact, changed when damaged or contaminated.
4. **Controlled footwear**, dedicated room shoes or covers, never the boots you wore in from the car park.
5. **Hand hygiene on entry** and after any contamination or absence.
6. **No personal items**, phone, jewellery, watch, makeup, left in a locker outside.

> **NOTE — Strip before you gown**
> 
> Remove jewellery, watches and makeup and store your phone before you put anything on. They cannot be cleaned, they shed particles, and a ring or watch hides bacteria a glove then traps against the crop.

## Different rooms, different kit

PPE intensity tracks the value and vulnerability of what is in the room, not a single suit everywhere. Strictest where the genetics live and where product is open and headed to a patient.

> **Diagram.** PPE escalates from the vault up to the tissue-culture lab. Mother and propagation rooms get the strictest biosecurity because one infected plant propagates to the whole crop[^hlvd-transmission-2025].

| Zone | PPE level | Key points |
| --- | --- | --- |
| Tissue-culture lab | Aseptic / ISO-5 | Scrub to elbow, sterile gloves, lab coat, work in a laminar-flow hood, no jewellery |
| Mother / propagation | Strictest biosecurity | Full gown, fresh gloves per plant, dedicated tools, serviced first in the day |
| Dry / cure | Cleanroom-grade | Product is exposed and microbial spec is a release gate |
| Veg / flower | Standard gown | Gown, hairnet, gloves, dedicated room footwear, sticky mat at the door |
| Trim / pack | Food-contact grade | Hairnet, beard net, gloves, smock, frequent glove changes |
| Vault / store | Minimal (security) | Gloves to keep product clean; controls are mostly security |

*Order people through the day clean-to-dirty: propagation and mothers first, before anyone has been in flower or post-harvest.*

> **NOTE — Visitors gown to the same standard**
> 
> A contractor or visitor is the same contamination risk as staff, often worse (they were just somewhere else). Gown them to the room's standard or keep them out of mother, propagation, tissue culture and dry rooms entirely, and log every entry.

## Gowning, in the right order

Order matters. You gown top-to-bottom so that particles shed while dressing fall onto areas you have not covered yet, and you cross a physical clean/dirty line as you go[^gmp-gowning-procedure].

> **Diagram.** Donning order: strip personal items, hair and beard first, then mask and eyewear, inner gloves, coverall and hood, boot covers as you step over the line, outer gloves over the cuffs, sanitise, enter[^gmp-gowning-procedure].

> **KEY — De-gown in reverse, dirtiest first**
> 
> Coming out, remove the most contaminated items first and do not touch their outer surfaces: outer gloves, boot covers (stepping back over the line), coverall rolled inside-out, eyewear, hood, mask by its loops, hairnet, inner gloves, then wash. Single-use items go in the right bin in the anteroom.

## Hands and gloves

Hands are the main transfer bridge, so hand hygiene is the most repeated action in the building. Do it on entry, before clean or aseptic work, after waste or any contamination, after any absence, and again on re-entry[^who-hand-hygiene].

> **Diagram.** The technique covers every surface (palms, between fingers, backs, thumbs, fingertips and nails). Soap and water for 40 to 60 seconds when hands are soiled; an alcohol rub of at least 60% alcohol for 20 to 30 seconds otherwise[^who-hand-hygiene].

> **Diagram.** Gloves are the most contaminated item, so they come off first and inside-out, glove-to-glove then skin-to-skin, so bare skin never touches the dirty exterior[^cdc-glove-removal].

> **WARN — Gloves do not replace washing**
> 
> A glove is a barrier, not a clean hand. Wash before you don and immediately after you doff[^cdc-glove-removal], and change gloves between plants in mother and propagation and any time they touch a non-clean surface. A dirty glove spreads viroid just as well as a dirty hand.

## The scenarios that catch people out

#### Phones and personal items

No phones, earbuds, jewellery, watches or makeup in production or clean areas. A phone is a fomite you hold to your face and cannot clean[^phone-fomite]. Lockers outside the gowning room, everything in before you gown.

#### The toilet

Toilets must not open into production. A flush throws a viable bioaerosol over a metre in seconds[^toilet-plume], so anyone back from the restroom is a bridge until they have washed and re-gowned.

> **Diagram.** De-gown before the toilet, close the lid before flushing, wash, then wash and sanitise again on return and re-gown with fresh garments before re-entering[^toilet-plume].

#### Eating and breaks

No eating, drinking, gum or vaping in production. De-gown to leave for a break area, then wash and re-gown on the way back.

#### Footwear and the floor

> **Diagram.** Layered threshold controls: a sticky mat captures most particles, a footbath disinfects, and a dedicated room boot or shoe cover goes on as you step over the demarcation line[^shoe-floor-contamination].

#### Cross-contamination: one-way flow

> **Diagram.** Move people, materials and waste one way, dirty to clean, never back. Backtracking means re-gowning, and a dirty-side hand or sleeve must never touch the clean side.

## Who is responsible: HSWA 2015

In New Zealand, PPE and hygiene are not just good practice, they are legal duties under the Health and Safety at Work Act 2015[^hswa-2015], overseen by WorkSafe[^worksafe-grwm].

> **Diagram.** The law requires you to control risk by the hierarchy of controls and treat PPE as the _last_ line, after eliminating, substituting, isolating, engineering and administrative controls[^worksafe-grwm].

**The business (PCBU) must**

- Ensure worker health and safety so far as is reasonably practicable (s36).
- Apply higher controls before relying on PPE.
- **Provide PPE and free replacements, and never charge workers for it** (s27).
- Give information, training, supervision and adequate facilities.

**Workers must**

- Take reasonable care for their own and others' safety (s45).
- Follow reasonable instructions, wear the required PPE, follow gowning and hygiene SOPs.
- Not misuse or interfere with anything provided for safety.
- Visitors carry the same take-care and follow-instruction duties.

> **KEY — PPE is the last control, not the first**
> 
> PPE supplements higher controls, it does not replace them[^worksafe-grwm]. Design the rooms, airflow and flow to remove the hazard first; the gown is what catches what is left. And the business pays for it, charging a worker for required PPE is an offence[^hswa-2015].

## The whole thing, in one place

- **Baseline, every room:** gown, hairnet + beard net, gloves, room shoes, wash, no personal items
- **Gown order:** hair -> mask -> eyewear -> inner gloves -> coverall -> hood -> boot covers -> outer gloves
- **De-gown:** reverse, dirtiest first, then wash
- **Hand wash:** soap 40-60s, or alcohol rub 20-30s (>=60%)
- **Gloves:** off first, inside-out; never replace washing; per-plant in propagation
- **Phones:** banned in clean areas, lockers outside
- **Toilet:** de-gown, lid down, wash, wash + sanitise on return, re-gown
- **Flow:** one way, clean to dirty, re-gown to backtrack
- **Law (NZ):** PCBU provides PPE free (s27); PPE is the last control

> **KEY — The mindset that makes it stick**
> 
> Frame every glove and gown as plant protection first. A human cannot help shedding millions of particles an hour. The suit, the order, the flow and the wash are simply how we keep that off a crop that a single contaminated touch can ruin.

## References

[^cleanroom-humans-source]: Cleanroom contamination analyses: personnel account for roughly 70-90% of contamination; a gowned worker emits ~100,000 particles/min at rest, ~1,000,000 walking, up to ~5,000,000 in active work. https://www.precgroup.com/70-percent-of-cleanroom-contamination/ (industry/manufacturer source)
[^cdc-skin-squames]: Noble / CDC Emerging Infectious Diseases: humans disseminate ~10^7 skin squames per day, of which roughly 10% carry viable bacteria. https://wwwnc.cdc.gov/eid/article/7/2/70-0225_article (peer-reviewed)
[^human-microbial-cloud]: Human microbial-emissions research: an occupied space gains roughly 37 million bacterial and 7 million fungal genome copies per person per hour above the unoccupied baseline. https://pmc.ncbi.nlm.nih.gov/articles/PMC7950481/ (peer-reviewed)
[^phone-fomite]: Mobile phones as fomites: cultured phones average far higher bacterial loads than a public toilet seat (order-of-magnitude), isolates including S. aureus, E. coli and Candida. https://pmc.ncbi.nlm.nih.gov/articles/PMC3939586/ (peer-reviewed)
[^shoe-floor-contamination]: Shoe-sole and floor contamination: soles carry MRSA, C. difficile, E. coli and other organisms; walking re-disperses settled organisms, contributing a meaningful share of airborne CFU. https://www.infectioncontroltoday.com/view/shoe-sole-and-floor-contamination-new-consideration-environmental-hygiene (peer-reviewed)
[^hlvd-transmission-2025]: Mechanical transmission and management of Hop Latent Viroid (HLVd) in cannabis: spread via contaminated tools and cuttings, up to 100% transmission within four weeks; controls include fresh gloves per plant, tool sterilisation and footbaths. Plants (MDPI) 2025, 14:830. https://www.mdpi.com/2223-7747/14/5/830 (peer-reviewed)
[^hand-hygiene-logreduction]: Comparative hand-hygiene efficacy: alcohol-based handrub achieves a larger log reduction (~3 log, ~83%) than plain soap-and-water washing (~2 log, ~58%); neither sterilises. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC117885/ (peer-reviewed)
[^toilet-plume]: Toilet-flush bioaerosol ('toilet plume'): a flush lofts aerosols to ~1.5 m within seconds; particles remain viable for minutes to hours, and a closed lid produces markedly less aerosol. https://pmc.ncbi.nlm.nih.gov/articles/PMC9732293/ (peer-reviewed)
[^fda-21cfr117-personnel]: US FDA. 21 CFR 117.10, Personnel (current good manufacturing practice for food): clean outer garments, personal cleanliness, hand washing, hair restraints, glove integrity. https://www.ecfr.gov/current/title-21/chapter-I/subchapter-B/part-117/subpart-B (industry/manufacturer source)
[^who-gacp-2003]: World Health Organization (2003). WHO guidelines on good agricultural and collection practices (GACP) for medicinal plants. https://www.who.int/publications/i/item/9241546271 (industry/manufacturer source)
[^who-hand-hygiene]: World Health Organization. Hand hygiene: the Five Moments and recommended technique (soap-and-water 40-60s; alcohol-based handrub 20-30s, ≥60% alcohol). https://www.who.int/teams/integrated-health-services/infection-prevention-control/hand-hygiene (industry/manufacturer source)
[^cdc-glove-removal]: US CDC. How to safely remove gloves: glove-to-glove then skin-to-skin, peeling inside-out so bare skin never contacts the contaminated exterior; hand hygiene before and after. https://www.cdc.gov/ebola/media/pdfs/2024/05/poster-how-to-remove-gloves.pdf (industry/manufacturer source)
[^gmp-gowning-procedure]: GMP / cleanroom gowning and de-gowning procedures: top-to-bottom donning order across a clean/dirty demarcation bench, reverse dirtiest-first removal. https://www.pharmanow.live/pharma-manufacturing/cleanroom-gowning-procedures-guide (industry/manufacturer source)
[^hswa-2015]: Health and Safety at Work Act 2015 (NZ): s36 PCBU primary duty of care; s45 worker duties; s27 PCBU must provide what is required (including PPE) and must not charge workers for it. https://www.legislation.govt.nz/act/public/2015/0070/latest/DLM5976894.html (industry/manufacturer source)
[^worksafe-grwm]: WorkSafe New Zealand and the Health and Safety at Work (General Risk and Workplace Management) Regulations 2016, reg 6: control risk by the hierarchy of controls, with PPE as the last resort. https://www.worksafe.govt.nz/managing-health-and-safety/getting-started/introduction-hswa-special-guide/ (industry/manufacturer source)
