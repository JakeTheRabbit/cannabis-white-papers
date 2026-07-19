# -*- coding: utf-8 -*-
"""Paper: PPPE, plant and personal protective equipment (PPE as biosecurity)."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        grid, card, chip, kv, steps)
import figs_pppe as PP

SLUG = "pppe"
TITLE = "PPPE: plant and personal protective equipment"
EYEBROW = "Plant health · PPE & biosecurity"
SUB = ("Coveralls, hairnets, gloves and shoe covers do two jobs at once: they keep the human safe, and "
       "they keep the human's particles, microbes and pests off the crop. People are the number-one "
       "contamination source in any clean space. This is the full rundown: how bad we are, the bare "
       "minimum, the room-by-room kit, and the procedures that actually work.")
META = [("shield", "Biosecurity & PPE"), ("image", "9 diagrams"),
        ("quote", "Research-backed · 15 sources"), ("clock", "~17 min read")]
RELATED = ["ipm-sop", "mould-risk", "tissue-culture", "daily-checks"]
REF_IDS = ["cleanroom-humans-source", "cdc-skin-squames", "human-microbial-cloud", "phone-fomite",
           "shoe-floor-contamination", "hlvd-transmission-2025", "hand-hygiene-logreduction",
           "toilet-plume", "fda-21cfr117-personnel", "who-gacp-2003", "who-hand-hygiene",
           "cdc-glove-removal", "gmp-gowning-procedure", "hswa-2015", "worksafe-grwm"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

# Fact-check jurisdiction banner
JURISDICTION_NOTE = 'Jurisdiction note: PPE duties and HSWA wording below are NZ-oriented; other jurisdictions differ.'


# 1 -----------------------------------------------------------------
SECTIONS.append({"id": "intro", "kicker": "Start here", "title": "Two jobs, one suit",
  "blocks": [
    callout("NOTE", "Jurisdiction", JURISDICTION_NOTE),
    
    lead("PPE in a grow is not really about you. In most rooms the gear is there to protect the "
         "<strong>plant</strong> from you: from the skin you shed, the spores on your jacket, the mites on "
         "your shoes and the viroid on your hands. The same coverall that keeps your clothes clean also "
         "keeps your contamination off the crop. That is why we call it PPPE, plant <em>and</em> personal "
         "protective equipment."),
    p("People are typically the dominant contamination source in any clean space (exact share varies by facility design)" + _c("cleanroom-humans-source") + ". You cannot stop a human shedding. You can "
      "only put a barrier around the human and move them through the building in a controlled way. That is "
      "the whole game."),
    callout("key", "Why this pays for itself",
      p("One contaminated mother plant or one shared glove can spread Hop Latent Viroid to an entire crop, "
        "and under experimental conditions infection of linked cuttings can approach complete cohort infection within weeks of propagation from infected "
        "stock" + _c("hlvd-transmission-2025") + ". The spread is mechanical, on tools, cuttings and hands, not "
        "airborne. Gloves-per-plant and gowning are not box-ticking; they are crop insurance.")),
    callout("note", "Two different reasons to gown",
      p("In cultivation, dry and trim, PPE protects the product. In <strong>extraction</strong> it flips to "
        "protecting the worker (solvents, fire), and in the vault it is mostly security. Same word, "
        "different purpose, different kit. This paper is about the biosecurity side, with the legal duties "
        "that sit under all of it.")),
  ]})

# 2 -----------------------------------------------------------------
SECTIONS.append({"id": "terms", "kicker": "Vocabulary", "title": "The words you need",
  "blocks": [
    defterm("PPE / PPPE", "Personal protective equipment. Here, plant <em>and</em> personal: the same gear "
            "protects the crop from the person and the person from hazards."),
    defterm("Gowning / de-gowning", "Putting on (donning) and taking off (doffing) protective clothing in a "
            "defined order, across a clean/dirty line, so contamination never crosses."),
    defterm("Fomite", "An object that carries and transfers microbes, a phone, a pen, a door handle, a tool. "
            "Hands move contamination from fomite to crop."),
    defterm("Bioaerosol", "Airborne particles carrying living things, skin flakes with bacteria, fungal "
            "spores, droplets from speech or a toilet flush."),
    defterm("Cross-contamination", "Moving contamination from a dirty area or item to a clean one, for "
            "example walking from flower back into propagation without re-gowning."),
    defterm("Hierarchy of controls", "The legal order for managing risk: eliminate, substitute, isolate, "
            "engineer, administrate, and only then PPE as the last line" + _c("worksafe-grwm") + "."),
    defterm("PCBU", "Person Conducting a Business or Undertaking, the NZ legal term for the duty-holding "
            "business (your employer) under the Health and Safety at Work Act" + _c("hswa-2015") + "."),
    defterm("Reasonably practicable", "The legal standard for how far you must go: weigh the risk against "
            "the effort and cost of controlling it. High-consequence, cheap-to-control risks must be "
            "controlled."),
  ]})

# 3 -----------------------------------------------------------------
SECTIONS.append({"id": "how-bad", "kicker": "The problem", "title": "How bad humans actually are",
  "blocks": [
    p("It is worth sitting with the numbers, because they are the entire argument for gowning up."),
    figure(PP.human_contamination(), 1,
      "People are the number-one contamination source in a clean space" + _c("cleanroom-humans-source") +
      ". You shed roughly ten million skin flakes a day, about a tenth carrying live bacteria" + _c("cdc-skin-squames") +
      ", and an occupied room gains tens of millions of bacteria and millions of fungal spores per person "
      "per hour" + _c("human-microbial-cloud") + "."),
    ul([
      "<strong>Movement is the multiplier.</strong> A gowned person emits about 100,000 particles a minute "
      "standing still, a million walking, and up to five million working fast" + _c("cleanroom-humans-source") +
      ". Slow, calm movement is itself a control.",
      "<strong>Your phone is a high-touch fomite.</strong> Phones carry skin and environmental flora and "
      "order of magnitude more bacteria than a public high-touch fomite that contacts faces and hands, and they ride to your face and back to "
      "your hands all day" + _c("phone-fomite") + ".",
      "<strong>Your shoes are a pest and spore taxi.</strong> Soles carry live pathogens and fungal spores, "
      "and walking re-launches settled organisms into the air" + _c("shoe-floor-contamination") + ". Mites and "
      "powdery mildew arrive on clothing and footwear.",
      "<strong>The toilet throws a plume.</strong> A flush lofts aerosols to about 1.5 m within seconds, "
      "viable for minutes to hours; a closed lid cuts it sharply" + _c("toilet-plume") + ".",
    ]),
    callout("note", "Hands are the main bridge, and hygiene is not a cure",
      p("Washing helps but does not sterilise: alcohol rubs often achieve ~2&ndash;3 log reductions (~99&ndash;99.9%) under test conditions; plain soap "
        "and water remove soil and many organisms without sterilising hands" + _c("hand-hygiene-logreduction") + ". That is why hand hygiene is a frequent loop "
        "at every transition, and why gloves and barriers carry the rest.")),
  ]})

# 4 -----------------------------------------------------------------
SECTIONS.append({"id": "bare-minimum", "kicker": "The floor", "title": "The bare minimum, everywhere",
  "blocks": [
    p("Before any room-specific extras, there is a non-negotiable baseline for entering any production or "
      "handling area. It mirrors food-GMP personnel rules" + _c("fda-21cfr117-personnel") + " and WHO good "
      "agricultural and collection practice" + _c("who-gacp-2003") + "."),
    ol([
      "<strong>Clean, dedicated outer garment</strong> put on at entry (gown, smock, scrubs or coverall), "
      "never your street clothes.",
      "<strong>Hair fully restrained</strong>, bouffant or hairnet, plus a beard cover for facial hair.",
      "<strong>Single-use nitrile gloves</strong>, intact, changed when damaged or contaminated.",
      "<strong>Controlled footwear</strong>, dedicated room shoes or covers, never the boots you wore in "
      "from the car park.",
      "<strong>Hand hygiene on entry</strong> and after any contamination or absence.",
      "<strong>No personal items</strong>, phone, jewellery, watch, makeup, left in a locker outside.",
    ]),
    callout("note", "Strip before you gown",
      p("Remove jewellery, watches and makeup and store your phone before you put anything on. They cannot "
        "be cleaned, they shed particles, and a ring or watch hides bacteria a glove then traps against the "
        "crop.")),
  ]})

# 5 -----------------------------------------------------------------
SECTIONS.append({"id": "by-room", "kicker": "Room by room", "title": "Different rooms, different kit",
  "blocks": [
    p("PPE intensity tracks the value and vulnerability of what is in the room, not a single suit "
      "everywhere. Strictest where the genetics live and where product is open and headed to a patient."),
    figure(PP.ppe_by_room(), 2,
      "PPE escalates from the vault up to the tissue-culture lab. Mother and propagation rooms get the "
      "strictest biosecurity because one infected plant propagates to the whole crop" + _c("hlvd-transmission-2025") + "."),
    table(["Zone", "PPE level", "Key points"],
      [["Tissue-culture lab", "Aseptic / ISO-5", "Scrub to elbow, sterile gloves, lab coat, work in a laminar-flow hood, no jewellery"],
       ["Mother / propagation", "Strictest biosecurity", "Full gown, fresh gloves per plant, dedicated tools, serviced first in the day"],
       ["Dry / cure", "Cleanroom-grade", "Product is exposed and microbial spec is a release gate"],
       ["Veg / flower", "Standard gown", "Gown, hairnet, gloves, dedicated room footwear, sticky mat at the door"],
       ["Trim / pack", "Food-contact grade", "Hairnet, beard net, gloves, smock, frequent glove changes"],
       ["Vault / store", "Minimal (security)", "Gloves to keep product clean; controls are mostly security"]],
      caption="Order people through the day clean-to-dirty: propagation and mothers first, before anyone has been in flower or post-harvest."),
    callout("note", "Visitors gown to the same standard",
      p("A contractor or visitor is the same contamination risk as staff, often worse (they were just "
        "somewhere else). Gown them to the room's standard or keep them out of mother, propagation, tissue "
        "culture and dry rooms entirely, and log every entry.")),
  ]})

# 6 -----------------------------------------------------------------
SECTIONS.append({"id": "gowning", "kicker": "The procedure", "title": "Gowning, in the right order",
  "blocks": [
    p("Order matters. You gown top-to-bottom so that particles shed while dressing fall onto areas you have "
      "not covered yet, and you cross a physical clean/dirty line as you go" + _c("gmp-gowning-procedure") + "."),
    figure(PP.gowning_order(), 3,
      "Donning order: strip personal items, hair and beard first, then mask and eyewear, inner gloves, "
      "coverall and hood, boot covers as you step over the line, outer gloves over the cuffs, sanitise, "
      "enter" + _c("gmp-gowning-procedure") + "."),
    callout("key", "De-gown in reverse, dirtiest first",
      p("Coming out, remove the most contaminated items first and do not touch their outer surfaces: outer "
        "gloves, boot covers (stepping back over the line), coverall rolled inside-out, eyewear, hood, mask "
        "by its loops, hairnet, inner gloves, then wash. Single-use items go in the right bin in the "
        "anteroom.")),
  ]})

# 7 -----------------------------------------------------------------
SECTIONS.append({"id": "hands", "kicker": "The procedure", "title": "Hands and gloves",
  "blocks": [
    p("Hands are the main transfer bridge, so hand hygiene is the most repeated action in the building. Do "
      "it on entry, before clean or aseptic work, after waste or any contamination, after any absence, and "
      "again on re-entry" + _c("who-hand-hygiene") + "."),
    figure(PP.handwash(), 4,
      "The technique covers every surface (palms, between fingers, backs, thumbs, fingertips and nails). "
      "Soap and water for 40 to 60 seconds when hands are soiled; an alcohol rub of at least 60% alcohol "
      "for 20 to 30 seconds otherwise" + _c("who-hand-hygiene") + "."),
    figure(PP.glove_doff(), 5,
      "Gloves are the most contaminated item, so they come off first and inside-out, glove-to-glove then "
      "skin-to-skin, so bare skin never touches the dirty exterior" + _c("cdc-glove-removal") + "."),
    callout("warn", "Gloves do not replace washing",
      p("A glove is a barrier, not a clean hand. Wash before you don and immediately after you doff" + _c("cdc-glove-removal") +
        ", and change gloves between plants in mother and propagation and any time they touch a non-clean "
        "surface. A dirty glove spreads viroid just as well as a dirty hand.")),
  ]})

# 8 -----------------------------------------------------------------
SECTIONS.append({"id": "scenarios", "kicker": "The daily traps", "title": "The scenarios that catch people out",
  "blocks": [
    h(3, "Phones and personal items"),
    p("No phones, earbuds, jewellery, watches or makeup in production or clean areas. A phone is a fomite "
      "you hold to your face and cannot clean" + _c("phone-fomite") + ". Lockers outside the gowning room, "
      "everything in before you gown."),
    h(3, "The toilet"),
    p("Toilets must not open into production. A flush throws a viable bioaerosol over a metre in "
      "seconds" + _c("toilet-plume") + ", so anyone back from the restroom is a bridge until they have washed and "
      "re-gowned."),
    figure(PP.toilet_protocol(), 6,
      "De-gown before the toilet, close the lid before flushing, wash, then wash and sanitise again on "
      "return and re-gown with fresh garments before re-entering" + _c("toilet-plume") + "."),
    h(3, "Eating and breaks"),
    p("No eating, drinking, gum or vaping in production. De-gown to leave for a break area, then wash and "
      "re-gown on the way back."),
    h(3, "Footwear and the floor"),
    figure(PP.footwear_barrier(), 7,
      "Layered threshold controls: a sticky mat captures most particles, a footbath disinfects, and a "
      "dedicated room boot or shoe cover goes on as you step over the demarcation line" + _c("shoe-floor-contamination") + "."),
    h(3, "Cross-contamination: one-way flow"),
    figure(PP.dirty_clean_flow(), 8,
      "Move people and clean materials clean → dirty; waste and used PPE only dirty → exit. Never back. Backtracking means re-gowning, "
      "and a dirty-side hand or sleeve must never touch the clean side."),
  ]})

# 9 -----------------------------------------------------------------
SECTIONS.append({"id": "hswa", "kicker": "The law (NZ)", "title": "Who is responsible: HSWA 2015",
  "blocks": [
    p("In New Zealand, PPE and hygiene are not just good practice, they are legal duties under the Health "
      "and Safety at Work Act 2015" + _c("hswa-2015") + ", overseen by WorkSafe" + _c("worksafe-grwm") + "."),
    figure(PP.hierarchy_controls(), 9,
      "The law requires you to control risk by the hierarchy of controls and treat PPE as the <em>last</em> "
      "line, after eliminating, substituting, isolating, engineering and administrative controls" + _c("worksafe-grwm") + "."),
    grid([
      card("The business (PCBU) must", ul([
        "Ensure worker health and safety so far as is reasonably practicable (s36).",
        "Apply higher controls before relying on PPE.",
        "<strong>Provide PPE and free replacements, and never charge workers for it</strong> (s27).",
        "Give information, training, supervision and adequate facilities.",
      ], "tight")),
      card("Workers must", ul([
        "Take reasonable care for their own and others' safety (s45).",
        "Follow reasonable instructions, wear the required PPE, follow gowning and hygiene SOPs.",
        "Not misuse or interfere with anything provided for safety.",
        "Visitors carry the same take-care and follow-instruction duties.",
      ], "tight")),
    ], cols=2),
    callout("key", "PPE is the last control, not the first",
      p("PPE supplements higher controls, it does not replace them" + _c("worksafe-grwm") + ". Design the rooms, "
        "airflow and flow to remove the hazard first; the gown is what catches what is left. And the "
        "business pays for it, charging a worker for required PPE is an offence" + _c("hswa-2015") + ".")),
  ]})

# 10 -----------------------------------------------------------------
SECTIONS.append({"id": "quick-reference", "kicker": "Cheat sheet", "title": "The whole thing, in one place",
  "blocks": [
    kv([("Baseline, every room", "gown, hairnet + beard net, gloves, room shoes, wash, no personal items"),
        ("Gown order", "hair -> mask -> eyewear -> inner gloves -> coverall -> hood -> boot covers -> outer gloves"),
        ("De-gown", "reverse, dirtiest first, then wash"),
        ("Hand wash", "soap 40-60s, or alcohol rub 20-30s (>=60%)"),
        ("Gloves", "off first, inside-out; never replace washing; per-plant in propagation"),
        ("Phones", "banned in clean areas, lockers outside"),
        ("Toilet", "de-gown, lid down, wash, wash + sanitise on return, re-gown"),
        ("Flow", "clean → dirty for people/materials; dirty → exit for waste, re-gown to backtrack"),
        ("Law (NZ)", "PCBU provides PPE free (s27); PPE is the last control")]),
    callout("key", "The mindset that makes it stick",
      p("Frame every glove and gown as plant protection first. A human cannot help shedding millions of "
        "particles an hour. The suit, the order, the flow and the wash are simply how we keep that off a "
        "crop that a single contaminated touch can ruin.")),
  ]})
