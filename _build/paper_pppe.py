# -*- coding: utf-8 -*-
"""Paper: PPPE, plant and personal protective equipment (PPE as biosecurity)."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        grid, card, chip, kv, steps)
import figs_pppe as PP

SLUG = "pppe"
TITLE = "PPPE: plant and personal protective equipment"
EYEBROW = "Plant health · PPE and biosecurity"
SUB = ("Coveralls, hairnets, gloves and shoe covers give the worker protection from hazards, and "
       "they keep contamination from the worker away from the crop. The contamination is the "
       "particles, the microbes and the pests of the worker. A person is the primary source of "
       "contamination in each clean production space. This paper gives information about the "
       "quantity of contamination that a person releases. It also gives the minimum PPE for each "
       "production area and the equipment for each room. It gives the procedures for gowning and "
       "hand hygiene that stop contamination at the demarcation line between clean and dirty areas.")
META = [("shield", "Biosecurity and PPE"), ("image", "9 diagrams"),
        ("quote", "15 sources"), ("clock", "~17 min to read")]
RELATED = ["ipm-sop", "mould-risk", "tissue-culture", "daily-checks"]
REF_IDS = ["cleanroom-humans-source", "cdc-skin-squames", "human-microbial-cloud", "phone-fomite",
           "shoe-floor-contamination", "hlvd-transmission-2025", "hand-hygiene-logreduction",
           "toilet-plume", "fda-21cfr117-personnel", "who-gacp-2003", "who-hand-hygiene",
           "cdc-glove-removal", "gmp-gowning-procedure", "hswa-2015", "worksafe-grwm"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

# Fact-check jurisdiction banner
JURISDICTION_NOTE = "The PPE duties and the terms of the Health and Safety at Work Act (HSWA) below are for NZ. Other jurisdictions are different."


# 1 -----------------------------------------------------------------
SECTIONS.append({"id": "intro", "kicker": "Start here", "title": "Purpose and scope",
  "blocks": [
    callout("NOTE", "Jurisdiction", JURISDICTION_NOTE),

    lead("In a grow room, PPE is not only for you. In most rooms, the equipment gives protection to "
         "the <strong>plant</strong> from you. The contamination is the skin flakes that you "
         "release. It is also the spores on your jacket, the mites on your shoes and the viroid on "
         "your hands. The same coverall that keeps your clothing clean also keeps your "
         "contamination away from the crop. Thus the name is PPPE: plant <em>and</em> personal "
         "protective equipment."),
    p("Persons are typically the primary source of contamination in each clean space. The "
      "percentage is different in different facilities." + _c("cleanroom-humans-source") +
      " A person cannot stop the particles that the person releases. You can only put a barrier "
      "around the person and control the movement of the person through the building."),
    callout("key", "A glove that you use for more than one plant can cause infection in a crop",
      p("One contaminated mother plant, or one glove that you use for more than one plant, can "
        "cause Hop Latent Viroid infection in the full crop. In tests, the infection of related "
        "cuttings can include almost all the cuttings of the group in some weeks after propagation "
        "from infected stock." + _c("hlvd-transmission-2025") + " The movement of the infection is "
        "mechanical: it is on tools, cuttings and hands. It is not in the air. A change of gloves "
        "for each plant and the gowning procedure are not only checks for compliance. They give "
        "protection to the crop.")),
    callout("note", "Two functions of gowning",
      p("In cultivation, in drying and in trimming, PPE gives protection to the product. In "
        "<strong>extraction</strong>, the function changes: PPE gives protection to the worker "
        "(solvents, fire). In the vault, PPE is mostly for security. The name is the same, but the "
        "function and the equipment are different. This paper is about biosecurity. It also gives "
        "the legal duties that apply to all of these areas.")),
  ]})

# 2 -----------------------------------------------------------------
SECTIONS.append({"id": "terms", "kicker": "Terms", "title": "Definitions",
  "blocks": [
    defterm("PPE / PPPE", "PPE is personal protective equipment. PPPE is plant <em>and</em> "
            "personal protective equipment. The same equipment gives the crop protection from the "
            "person, and it gives the person protection from hazards."),
    defterm("Gowning / de-gowning", "Gowning is the procedure to put on protective clothing "
            "(donning). De-gowning is the procedure to remove protective clothing (doffing). Do "
            "these procedures in a specified sequence, across the demarcation line between the "
            "clean area and the dirty area. Thus the contamination does not go across the "
            "demarcation line."),
    defterm("Fomite", "An object with microbes on it, for example a phone, a pen, a door handle or "
            "a tool. The microbes can move from the object to your hands. Hands move contamination "
            "from the fomite to the crop."),
    defterm("Bioaerosol", "Particles in the air that contain viable organisms. Examples are skin "
            "flakes with bacteria, fungal spores, and drops of liquid from a person who speaks or "
            "when a person flushes a toilet."),
    defterm("Cross-contamination", "The movement of contamination from a dirty area or item to a "
            "clean area or item. For example, a person goes from the room for the flowering stage "
            "to the propagation room and does not do the gowning procedure again."),
    defterm("Hierarchy of controls", "The legal sequence of the controls for risk: elimination, "
            "substitution, isolation, engineering controls, administrative controls, and then PPE "
            "as the last control." + _c("worksafe-grwm")),
    defterm("PCBU", "Person Conducting a Business or Undertaking. PCBU is the NZ legal term for the "
            "business that has the duty (your employer) in HSWA." + _c("hswa-2015")),
    defterm("Reasonably practicable", "The legal limit for the quantity of work that you must do. "
            "Compare the risk with the work and the cost of its control. You must control a risk "
            "when its effect is large and its cost of control is low."),
  ]})

# 3 -----------------------------------------------------------------
SECTIONS.append({"id": "how-bad", "kicker": "The problem", "title": "Risks of contamination from personnel",
  "blocks": [
    p("A person in a cultivation room is the primary source of contamination in the space. The "
      "person releases particles, microbes and pests all the time, only because the person is in "
      "the room."),
    figure(PP.human_contamination(), 1,
      "Persons are the primary source of contamination in a clean space." +
      _c("cleanroom-humans-source") + " A person releases approximately ten million skin flakes "
      "each day, and approximately a tenth of them have viable bacteria on them." +
      _c("cdc-skin-squames") + " A room with persons receives tens of millions of bacteria and "
      "millions of fungal spores for each person each hour." + _c("human-microbial-cloud")),
    ul([
      "<strong>Movement increases the quantity of particles.</strong> A person in a gown releases "
      "approximately 100,000 particles each minute when the person does not move. The person "
      "releases approximately a million when the person walks, and a maximum of five million when "
      "the person works fast." + _c("cleanroom-humans-source") + " Slow movement is a control.",
      "<strong>Your phone is a fomite that you touch frequently.</strong> A phone has skin microbes "
      "and microbes from the environment on it. The phone goes to your head and back to your hands "
      "all day." + _c("phone-fomite"),
      "<strong>Your shoes move pests and spores.</strong> The soles have viable pathogens and "
      "fungal spores on them. When you walk, the organisms on the floor go into the air again." +
      _c("shoe-floor-contamination") + " Mites and powdery mildew come into the room on clothing "
      "and footwear.",
      "<strong>A toilet makes a plume of aerosol.</strong> When a person flushes the toilet, "
      "aerosol goes to a height of approximately 1.5 m (4.9 ft) in seconds. The aerosol stays "
      "viable for minutes to hours. A closed lid decreases the aerosol by a large quantity." +
      _c("toilet-plume"),
    ]),
    callout("note", "Hands move contamination, and hygiene does not remove all of it",
      p("A hand wash helps, but it does not sterilize the hands. In test conditions, an alcohol rub "
        "frequently gives approximately 2 to 3 log reductions (approximately 99 to 99.9%). Soap and "
        "water remove soil and many organisms, but they do not sterilize the hands." +
        _c("hand-hygiene-logreduction") + " Thus you do hand hygiene frequently, at each change of "
        "area. Gloves and barriers give the remaining protection.")),
  ]})

# 4 -----------------------------------------------------------------
SECTIONS.append({"id": "bare-minimum", "kicker": "The minimum", "title": "Minimum necessary PPE",
  "blocks": [
    p("You must use a baseline of PPE to go into each production area or handling area. Add the "
      "items for a specified room after this baseline. The baseline agrees with the personnel "
      "regulations for food GMP" + _c("fda-21cfr117-personnel") + " and with the WHO good "
      "agricultural and collection practice" + _c("who-gacp-2003") + "."),
    ol([
      "<strong>Clean outer clothing for this area only</strong>, which you put on at the entrance "
      "(gown, smock, scrubs or coverall). Do not use your street clothes.",
      "<strong>Hair and beard cover.</strong> Put a bouffant or a hairnet on all of your hair. Put a beard cover on facial hair.",
      "<strong>Single-use nitrile gloves.</strong> Use gloves that have no damage. Replace a glove when it has damage or contamination.",
      "<strong>Footwear for this area only</strong>: room shoes or shoe covers. Do not use the "
      "boots that you wore in the parking area.",
      "<strong>Hand hygiene.</strong> Do hand hygiene at the entrance, after contamination and after you are away from the area.",
      "<strong>No personal items.</strong> Keep your phone, jewelry, watch and makeup in a locker before you go into the area.",
    ]),
    callout("note", "Remove personal items before the gowning procedure",
      p("Remove jewelry, watches and makeup before you put on clothing. Keep your phone in a "
        "locker. You cannot clean these items, and they release particles. A ring or a watch holds "
        "bacteria between the item and the skin. A glove then holds the bacteria against the crop.")),
  ]})

# 5 -----------------------------------------------------------------
SECTIONS.append({"id": "by-room", "kicker": "Each room", "title": "PPE for each room",
  "blocks": [
    p("The grade of PPE is different for each room, because the value of the contents and the risk "
      "to the contents are different. Do not use the same PPE in all rooms. Use the highest grade "
      "where the genetics are, and where the product is open and goes to a patient."),
    figure(PP.ppe_by_room(), 2,
      "The grade of PPE increases from the vault to the tissue-culture lab. Mother rooms and "
      "propagation rooms have the highest biosecurity, because each plant that you propagate from "
      "one infected plant has the infection." + _c("hlvd-transmission-2025")),
    table(["Zone", "PPE grade", "Primary items"],
      [["Tissue-culture lab", "Aseptic / ISO-5", "Scrub the arms to the elbows. Use sterile gloves and a lab coat. Work in a laminar-flow hood. Do not use jewelry."],
       ["Mother / propagation", "Highest biosecurity", "Full gown. New gloves for each plant. Tools for this room only. Work in this room first in the day."],
       ["Dry / cure", "Cleanroom grade", "The product is open, and the microbial specification is a release gate."],
       ["Vegetative stage / flowering stage", "Standard gown", "Gown, hairnet, gloves, footwear for this room only, sticky mat at the door"],
       ["Trim / packaging", "Food-contact grade", "Hairnet, beard net, gloves, smock. Change the gloves frequently."],
       ["Vault / storage", "Minimum (security)", "Gloves to keep the product clean. The controls are mostly for security."]],
      caption="Persons must go through the rooms in sequence, from clean to dirty. They go to propagation rooms and mother rooms first, before they go to the rooms for the flowering stage or to post-harvest areas."),
    callout("note", "Visitors must use the same PPE as personnel",
      p("A contractor or a visitor is the same contamination risk as personnel. Frequently the risk "
        "is larger, because the contractor or visitor was in a different area before. Make sure "
        "that they put on the PPE that is necessary for the room. Or do not let them go into mother "
        "rooms, propagation rooms, tissue-culture rooms and dry rooms. Make a record of each time "
        "that a person goes in.")),
  ]})

# 6 -----------------------------------------------------------------
SECTIONS.append({"id": "gowning", "kicker": "The procedure", "title": "Gowning procedure",
  "blocks": [
    p("The sequence is important. Put on the PPE from the top to the bottom. Thus the particles "
      "that you release when you put on the clothing fall on parts of the body that have no "
      "clothing at this time. At the same time, you go across the demarcation line between the "
      "dirty area and the clean area." + _c("gmp-gowning-procedure")),
    figure(PP.gowning_order(), 3,
      "Do the gowning in this sequence. Remove personal items, then put on the hair cover and the "
      "beard cover. Put on the mask and the eyewear, then the inner gloves, then the coverall and "
      "the hood. Put on the boot covers when you go across the demarcation line. Put the outer "
      "gloves on the cuffs of the coverall. Sanitize your hands and go in." +
      _c("gmp-gowning-procedure")),
    callout("key", "Do the de-gowning in the opposite sequence, with the dirtiest item first",
      p("When you go out, remove the most contaminated items first. Do not touch the outer surfaces "
        "of these items. The sequence is: outer gloves, boot covers (when you go back across the "
        "demarcation line), coverall (remove it inside-out), eyewear, hood, mask (touch only the "
        "loops), hairnet and inner gloves. Then wash your hands. Put the single-use items in the "
        "correct bin in the anteroom.")),
  ]})

# 7 -----------------------------------------------------------------
SECTIONS.append({"id": "hands", "kicker": "The procedure", "title": "Hands and gloves",
  "blocks": [
    p("Hands move most of the contamination from one area to a different area. Thus hand hygiene is "
      "the task that you do most frequently in the building. Do hand hygiene at the entrance, and "
      "before clean work or aseptic work. Do it also after waste or contamination, after you are "
      "away from the area, and when you go in again." + _c("who-hand-hygiene")),
    figure(PP.handwash(), 4,
      "The method is for all surfaces of the hand: palms, the spaces between the fingers, the back "
      "of the hand, thumbs, fingertips and nails. When the hands are dirty, use soap and water for "
      "40 to 60 seconds. When the hands are not dirty, use an alcohol rub with a minimum of 60% "
      "alcohol for 20 to 30 seconds." + _c("who-hand-hygiene")),
    figure(PP.glove_doff(), 5,
      "The gloves are the most contaminated item. Remove them first, inside-out. First, a glove "
      "touches a glove. Then, skin touches skin. Thus bare skin does not touch the dirty outer "
      "surface." + _c("cdc-glove-removal")),
    callout("warn", "Wash your hands also when you use gloves",
      p("A glove is a barrier. It is not a clean hand. Wash your hands before you put on gloves and "
        "immediately after you remove them." + _c("cdc-glove-removal") + " Change the gloves "
        "between plants in mother rooms and propagation rooms. Also change the gloves when they "
        "touch a surface that is not clean. A dirty glove moves viroid from one plant to a "
        "different plant as much as a dirty hand.")),
  ]})

# 8 -----------------------------------------------------------------
SECTIONS.append({"id": "scenarios", "kicker": "The problems of each day", "title": "Frequent errors of compliance",
  "blocks": [
    h(3, "Phones and personal items"),
    p("Do not put phones, earbuds, jewelry, watches or makeup into production areas or clean areas. "
      "A phone is a fomite that you hold to your head, and you cannot clean it." + _c("phone-fomite") +
      " Put all of these items in lockers before you go into the gowning room."),
    h(3, "The toilet"),
    p("A toilet must not have a door into a production area. When a person flushes a toilet, viable "
      "bioaerosol goes to a height of more than 1 m (3 ft) in seconds." + _c("toilet-plume") +
      " Thus a person who comes back from the toilet can move contamination into the area. The risk "
      "continues until the person washes the hands and does the gowning procedure again."),
    figure(PP.toilet_protocol(), 6,
      "Do the de-gowning procedure before you go to the toilet. Close the lid before you flush. "
      "Wash your hands. When you come back, wash and sanitize your hands again. Then put on clean "
      "clothing before you go into the area again." + _c("toilet-plume")),
    h(3, "Food, drink and break areas"),
    p("Do not eat, drink, use chewing gum or use an electronic cigarette in a production area. "
      "Before you go to a break area, do the de-gowning procedure. When you come back, wash your "
      "hands and do the gowning procedure again."),
    h(3, "Footwear and the floor"),
    figure(PP.footwear_barrier(), 7,
      "The controls at the threshold have layers. A sticky mat removes most of the particles from "
      "the shoes. A footbath disinfects the shoes. You put on the boots or shoe covers for the room "
      "when you go across the demarcation line." + _c("shoe-floor-contamination")),
    h(3, "Cross-contamination: flow in one direction"),
    figure(PP.dirty_clean_flow(), 8,
      "Move persons and clean materials from the clean area to the dirty area. Move waste and used "
      "PPE only from the dirty area to the exit. Do not go back. If a person goes back, the person "
      "must do the gowning procedure again. A hand or a sleeve from the dirty side must not touch "
      "the clean side."),
  ]})

# 9 -----------------------------------------------------------------
SECTIONS.append({"id": "hswa", "kicker": "Regulations (NZ)", "title": "Duties in HSWA 2015",
  "blocks": [
    p("In New Zealand, PPE and hygiene are legal duties in the Health and Safety at Work Act 2015 "
      "(HSWA). They are not only good procedures." + _c("hswa-2015") + " WorkSafe monitors the "
      "compliance with these duties." + _c("worksafe-grwm")),
    figure(PP.hierarchy_controls(), 9,
      "The regulations tell you to control risk with the hierarchy of controls. You must use PPE as "
      "the <em>last</em> control, after elimination, substitution, isolation, engineering controls "
      "and administrative controls." + _c("worksafe-grwm")),
    grid([
      card("The business (PCBU) must", ul([
        "Make sure of the health and safety of workers, as far as is reasonably practicable (s36).",
        "Apply the higher controls before you use PPE.",
        "<strong>Supply PPE and replacements. Make sure that the workers have no cost for PPE</strong> (s27).",
        "Give information, training, supervision and sufficient facilities.",
      ], "tight")),
      card("Workers must", ul([
        "Use reasonable care for their safety and for the safety of other persons (s45).",
        "Obey the reasonable instructions. Put on the necessary PPE. Obey the SOPs for gowning and hygiene.",
        "Do not use safety items incorrectly. Do not change them or cause damage to them.",
        "Visitors have the same duties: use reasonable care and obey the instructions.",
      ], "tight")),
    ], cols=2),
    callout("key", "PPE is the last control, not the first",
      p("PPE comes after the higher controls and gives more protection. You must continue to use "
        "the higher controls." + _c("worksafe-grwm") + " First, make the rooms, the airflow and the "
        "flow correct to remove the hazard. The gown holds the contamination that stays. The "
        "business has the cost of the PPE. It is an offense to give a worker the cost of PPE that "
        "is necessary." + _c("hswa-2015"))),
  ]})

# 10 -----------------------------------------------------------------
SECTIONS.append({"id": "quick-reference", "kicker": "Short list", "title": "Reference list",
  "blocks": [
    kv([("Baseline for each room", "Gown, hairnet and beard net, gloves, room shoes, wash the hands, no personal items"),
        ("Gowning sequence", "Hair, then mask, then eyewear, then inner gloves, then coverall, then hood, then boot covers, then outer gloves"),
        ("De-gowning", "Opposite sequence, dirtiest item first, then wash the hands"),
        ("Hand wash", "Soap: 40 to 60 seconds. Alcohol rub: 20 to 30 seconds (minimum 60% alcohol)."),
        ("Gloves", "Remove first, inside-out. Wash your hands also when you use gloves. In propagation, new gloves for each plant."),
        ("Phones", "Do not put phones into clean areas. Use lockers before the gowning room."),
        ("Toilet", "Do the de-gowning procedure. Close the lid. Wash the hands. When you come back, wash and sanitize the hands. Do the gowning procedure again."),
        ("Flow", "Persons and materials: from clean to dirty. Waste: from dirty to the exit. To go back, do the gowning procedure again."),
        ("Regulations (NZ)", "The PCBU supplies PPE at no cost to workers (s27). PPE is the last control.")]),
    callout("key", "Think about the plant first",
      p("Think of each glove and each gown as protection for the plant first. A person releases "
        "millions of particles each hour. The person cannot stop the particles. The suit, the "
        "sequence, the flow and the hand wash keep these particles away from a crop. One "
        "contaminated touch can cause very bad damage to a crop.")),
  ]})
