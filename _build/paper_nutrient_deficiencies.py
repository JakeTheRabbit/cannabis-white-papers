# -*- coding: utf-8 -*-
"""Paper: nutrient deficiency and toxicity diagnosis (beginner)."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        stagecard, grid, card, chip, kv, steps)
import figs_lib as L

SLUG = "nutrient-deficiencies"
TITLE = "Nutrient deficiency and toxicity diagnosis"
EYEBROW = "Plant health · Diagnosis"
SUB = ("A beginner's visual guide to reading cannabis leaf symptoms: mobile vs immobile nutrients, "
       "deficiency vs toxicity vs pH lockout, and how to confirm and fix the real problem before you "
       "reach for fertiliser.")
META = [("leaf", "Plant health"), ("image", "12 figures"),
        ("quote", "Peer-reviewed · 7 sources"), ("clock", "~14 min read")]
RELATED = ["ph-management", "nutrient-mixing-athena", "water-quality"]
REF_IDS = ["cockson-2019-nutrient-disorders-cannabis", "maillard-2015-leaf-nutrient-remobilization",
           "bevan-2021-npk-soilless-cannabis-flowering", "morad-2023-cannabis-magnesium-supply",
           "saloner-2020-cannabis-nitrogen-supply", "neilsen-1993-rhizosphere-ph-fe-mn-zn",
           "vyn-2007-ufl-nutrient-mobility-diagnosis", "hawkesford-2012-marschner-mineral-nutrition",
           "fageria-2001-nutrient-interactions-antagonism"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

SECTIONS.append({"id": "what-this-is", "kicker": "Start here", "title": "What this is: reading the plant like a gauge",
  "blocks": [
    lead("A cannabis plant tells you what it lacks, or has too much of, through the colour, shape and "
         "position of its leaves. This paper teaches you to read those signals systematically instead "
         "of guessing, so you fix the actual cause rather than randomly adding fertiliser."),
    p("The single most important idea comes first: <strong>where</strong> a symptom appears, on the "
      "old bottom leaves or the new top leaves, usually matters more than what colour it is. Get that "
      "one habit and you have already cut the list of suspects in half."),
    p("A nutrient is one of the roughly 17 chemical elements a plant must absorb to grow" + _c("hawkesford-2012-marschner-mineral-nutrition") +
      ". The ones you adjust most are nitrogen (N), phosphorus (P) and potassium (K), plus calcium "
      "(Ca), magnesium (Mg), sulfur (S), and tiny amounts of micronutrients like iron and zinc."),
    p("Three different problems can look almost identical on a leaf: a true deficiency (not enough of "
      "an element), a toxicity (too much), and a pH lockout (the element is present but the roots "
      "cannot absorb it). Telling them apart is the whole skill."),
    figure(L.flow("How to read a leaf",
            [("Position", "old bottom leaf or new top leaf?"),
             ("Colour pattern", "whole leaf, between veins, or edges?"),
             ("Shape", "flat, curled, clawed, or burnt tips?")],
            note="Three questions, in this order, on every problem leaf."), 1,
      "The plant is a gauge. You observe leaf position and colour, form a hypothesis, then confirm it "
      "with two cheap measurements before changing anything."),
    table(["The look-alike", "Plain meaning", "The telltale sign"], [
      ["<strong>Deficiency</strong>", "Not enough of an element", "Progressive fading, paler new growth"],
      ["<strong>Toxicity</strong>", "Too much of an element or salt", "Dark green, clawed leaves, burnt tips"],
      ["<strong>pH lockout</strong>", "Element present but roots cannot take it up", "Deficiency look despite correct feeding"],
    ], cls="compact", caption="Yellow does not equal hungry. The same colour can come from three opposite causes."),
    callout("warn", "A damaged leaf will not turn green again",
      p("Reading symptoms is diagnostic, not instant. By the time a leaf shows damage the plant has "
        "been short for days, and that leaf will not recover even after you fix the cause. You are "
        "watching new growth for recovery, not the old leaves.")),
  ]})

SECTIONS.append({"id": "key-terms", "kicker": "Vocabulary", "title": "Key terms, defined plainly",
  "blocks": [
    p("Before diagnosing anything you need a handful of words that growers use constantly. These are "
      "deliberately defined in everyday language. Skim once and refer back as needed."),
    defterm("Macronutrient", "An element the plant needs in large amounts: N, P, K, Ca, Mg, S."),
    defterm("Micronutrient", "An element needed in tiny amounts: iron (Fe), manganese (Mn), zinc "
            "(Zn), copper (Cu), boron (B), molybdenum (Mo)."),
    defterm("Mobile nutrient", "One the plant can pull out of an old leaf and resend to new growth "
            "when supply runs short: N, P, K, Mg."),
    defterm("Immobile nutrient", "One that stays locked where it was first placed and cannot be "
            "relocated: Ca, S, Fe, Mn, Zn, B, Cu, Mo."),
    defterm("Chlorosis", "Yellowing, the loss of green chlorophyll. Interveinal chlorosis is "
            "yellowing between the veins while the veins stay green, a very common and specific pattern."),
    defterm("Necrosis", "Dead brown or crispy tissue. It does not come back."),
    defterm("pH", "A 0-14 scale of how acidic or alkaline the root-zone water is. It controls which "
            "nutrients dissolve and can be absorbed."),
    defterm("EC (electrical conductivity)", "How much dissolved salt or fertiliser is in the water, "
            "a proxy for feed strength. PPM is the same thing in different units."),
    defterm("Runoff", "The water that drains out the bottom of the pot. You can measure it to see "
            "what is happening at the roots."),
    figure(L.flow("Mobile vs immobile, and where to look",
            [("Mobile: N P K Mg", "symptoms on OLD bottom leaves first"),
             ("Immobile: Ca S Fe Mn Zn B Cu Mo", "symptoms on NEW top leaves first")],
            note="Mobility decides which end of the plant shows the problem."), 2,
      "Every common element sorts into mobile or immobile, and that decides whether old or new leaves "
      "show symptoms first." + _c("vyn-2007-ufl-nutrient-mobility-diagnosis")),
  ]})

SECTIONS.append({"id": "mobility-why-position", "kicker": "Core concept 1", "title": "Why old leaves vs new leaves is the first question",
  "blocks": [
    p("When a plant runs short of a mobile nutrient, it cannibalises its oldest leaves to feed new "
      "growth, so damage appears at the bottom first and climbs upward. When it runs short of an "
      "immobile nutrient, it cannot move existing stores, so the newest top growth starves while old "
      "leaves stay fine." + _c("maillard-2015-leaf-nutrient-remobilization")),
    p("This single rule lets you cut the list of suspects roughly in half before you even look at colour."),
    ul([
      "<strong>Bottom or old leaves yellowing and dying upward</strong> points to a mobile nutrient: nitrogen, phosphorus, potassium or magnesium.",
      "<strong>Top or new leaves distorted, pale or hooked</strong> while the bottom looks healthy points to an immobile nutrient: calcium, sulfur, iron, zinc, manganese or boron.",
      "<strong>Whole-plant uniform symptoms, or damage on both ends at once</strong>, points away from a single deficiency and toward a pH lockout, a root problem or environmental stress.",
    ]),
    figure(L.flow("The first split: where did it appear FIRST?",
            [("Old / bottom", "mobile shortlist: N P K Mg"),
             ("New / top", "immobile shortlist: Ca S Fe Zn Mn B"),
             ("Whole plant / both", "lockout or environment branch")],
            note="Answer this before you think about colour."), 3,
      "Mobile-nutrient deficiencies present on the older lower leaves; immobile ones present on the "
      "newer upper growth." + _c("cockson-2019-nutrient-disorders-cannabis")),
    callout("note", "Read symptoms against the growth stage",
      p("Nitrogen fading from the bottom up is normal in late flowering as the plant remobilises N "
        "into the buds. The same symptom is healthy at week 7 and a problem at week 2, so always "
        "check the calendar before you act.")),
  ]})

SECTIONS.append({"id": "deficiency-vs-toxicity-vs-lockout", "kicker": "Core concept 2", "title": "Deficiency vs toxicity vs pH lockout",
  "blocks": [
    p("The biggest beginner trap is seeing yellow leaves, assuming hungry, and adding more "
      "fertiliser, which makes a toxicity or lockout dramatically worse. A toxicity shows as dark "
      "green clawed leaves and burnt tips, the opposite of a hunger symptom. A pH lockout means the "
      "nutrient is sitting right there in the pot but the roots physically cannot take it up because "
      "the water is too acidic or too alkaline."),
    ul([
      "<strong>Deficiency:</strong> progressive fading and yellowing, smaller new growth, leaves eventually drop. The plant looks like it is starving and getting paler.",
      "<strong>Toxicity (overfeeding):</strong> leaves go dark green and glossy, tips burn brown and curl, and severe nitrogen excess bends leaf tips into a downward hook called the claw." + _c("saloner-2020-cannabis-nitrogen-supply"),
      "<strong>pH lockout:</strong> classic deficiency patterns, often iron or calcium and magnesium, appear even though you are feeding correctly, because pH is outside the absorbable window." + _c("neilsen-1993-rhizosphere-ph-fe-mn-zn"),
    ]),
    table(["Symptom you see", "If deficiency", "If toxicity", "If lockout", "First action"], [
      ["Yellow leaves", "Too little of an element", "Salt overload starving roots", "pH blocks uptake", "Check pH before feeding"],
      ["Brown crispy tips", "Potassium short (margins)", "Nutrient or salt burn", "Often pH-driven micro shortage", "Check EC of runoff"],
      ["Dark green, clawed", "Rare", "Nitrogen excess", "Not typical", "Reduce feed strength"],
    ], cls="compact", caption="One symptom, three causes. The correct first action is almost never more fertiliser."),
    figure(L.zones("The deficiency-to-toxicity spectrum", 0, 100,
            [(0, 33, L.AMBL, "too little: pale, drop"),
             (33, 67, L.GL, "optimal: healthy green"),
             (67, 100, L.REDL, "too much: dark, claw, burnt")],
            unit="", note="Both ends are bad, and they look different."), 4,
      "Healthy is a middle band. Pale and dropping is one failure mode, dark and clawed is the "
      "opposite one, and chasing the wrong end makes things worse."),
    callout("key", "Check pH first, always",
      p("Before treating any suspected deficiency, check pH. If pH is out of range, fix that and "
        "re-observe for several days before concluding the plant is actually short of anything. pH "
        "outside range causes lockout despite a perfectly good feed." + _c("neilsen-1993-rhizosphere-ph-fe-mn-zn"))),
  ]})

SECTIONS.append({"id": "ph-windows", "kicker": "Core concept 3", "title": "pH: the gatekeeper, and why your medium sets the target",
  "blocks": [
    p("Each nutrient only dissolves and stays available across a specific pH band, so if root-zone pH "
      "drifts out of range, several nutrients drop out of solution at once and the plant starves in a "
      "full pantry. Getting pH right prevents more deficiencies than any fertiliser ever fixes."),
    p("The correct target pH depends entirely on your growing medium. Soil buffers itself and "
      "tolerates a higher band, while coco and hydroponics have no buffer and must be dialled in tightly."),
    figure(L.zones("Nutrient availability vs pH", 4.5, 8.0,
            [(5.5, 6.5, L.GL, "coco / hydro window"),
             (6.0, 7.0, L.BLUL, "soil window")],
            unit="", note="Outside these bands, several nutrients fall out of solution together."), 5,
      "The shaded bands are the absorbable windows. Soil sits a little higher and wider; coco and "
      "hydro sit lower and tighter." + _c("neilsen-1993-rhizosphere-ph-fe-mn-zn")),
    table(["Medium", "Target pH", "Sweet spot", "Check how often", "Buffering"], [
      ["Soil", "6.0-7.0", "6.2-6.8", "Weekly", "High, forgiving"],
      ["Coco", "5.5-6.5", "5.8-6.2", "Every feed", "None"],
      ["Hydro", "5.5-6.5", "5.8-6.2", "Daily", "None"],
    ], cls="compact", caption="Soil is the most forgiving medium. Coco and hydro have no buffer, so pH must be checked far more often."),
    callout("tip", "Direction of drift tells you what locks out",
      ul([
        "<strong>Above ~6.5</strong> in coco or hydro: iron, manganese, zinc and boron fall out. Expect micronutrient-style new-growth chlorosis." + _c("neilsen-1993-rhizosphere-ph-fe-mn-zn"),
        "<strong>Below ~5.5:</strong> calcium, magnesium and phosphorus lock out.",
        "Slightly cycling within the band (e.g. 5.8-6.2) gives every nutrient its turn at peak availability, but stay inside the band for your medium.",
      ], "tight")),
  ]})

SECTIONS.append({"id": "field-guide", "kicker": "Practical reference", "title": "A symptom field guide, nutrient by nutrient",
  "blocks": [
    p("This is the lookup table you return to at the plant. For each nutrient it gives the leaf "
      "position, the colour or shape pattern, and the one detail that separates it from its "
      "look-alikes. Use the old-vs-new rule from earlier to jump straight to the right block."),
    table(["Nutrient", "Mobile?", "Position", "Pattern", "Key differentiator"], [
      ["Nitrogen (N)", "Mobile", "Old / lower", "Whole leaf uniformly pale then yellow, drops", "Most common; excess N = dark clawed leaves"],
      ["Phosphorus (P)", "Mobile", "Old / lower", "Dark, dull, bronze/grey/purple blotches", "Some strains are naturally purple, do not judge on stems alone"],
      ["Potassium (K)", "Mobile", "Old / lower", "Burnt brown crispy tips and edges, centre stays green", "Margins burn, unlike N's whole-leaf fade"],
      ["Magnesium (Mg)", "Mobile", "Old / lower", "Interveinal yellowing, veins stay green", "Starts mid-leaf and creeps in"],
      ["Calcium (Ca)", "Immobile", "New / top", "Distorted, brown-spotted new growth", "Deformity, not just colour"],
      ["Sulfur (S)", "Immobile", "New / top", "Pale or yellow new leaves overall", "Whole new leaf pales, not interveinal"],
      ["Iron (Fe)", "Immobile", "New / top", "Bright interveinal yellowing, sharp green veins", "Very common with high pH; topmost leaves"],
    ], cls="compact", caption="The leaf symptom atlas. Position first, then pattern, then the differentiator."),
    p("Two of these look almost identical and trip up beginners constantly: magnesium and iron both "
      "give interveinal chlorosis with green veins." + _c("morad-2023-cannabis-magnesium-supply") +
      " Position is what tells them apart, magnesium on old lower leaves, iron on the newest top growth."),
    figure(L.flow("Iron vs magnesium: same pattern, opposite end",
            [("Magnesium", "interveinal yellowing on OLD lower leaf"),
             ("Iron", "interveinal yellowing on NEW top leaf")],
            note="The colour pattern is the same. Position is the tell."), 6,
      "Magnesium deficiency is interveinal chlorosis on older leaves; iron is the same look on new "
      "growth." + _c("morad-2023-cannabis-magnesium-supply") + _c("cockson-2019-nutrient-disorders-cannabis")),
    figure(L.bars("Relative leaf demand by macronutrient (flowering)",
            [("Nitrogen", 100), ("Potassium", 95), ("Phosphorus", 45), ("Magnesium", 35)],
            unit="", note="Approximate relative draw; potassium demand climbs through flowering.", maxv=110), 7,
      "Nitrogen and potassium dominate flowering uptake, which is why their deficiencies are the ones "
      "you will meet most." + _c("bevan-2021-npk-soilless-cannabis-flowering")),
  ]})

SECTIONS.append({"id": "confirm-and-fix", "kicker": "Step by step", "title": "Confirm before you treat: pH + EC + runoff",
  "blocks": [
    p("Diagnosis is a loop, not a guess. You observe the leaves, then confirm with two cheap meters "
      "before changing anything. Measuring the EC and pH of both what goes in and what runs out of "
      "the pot tells you whether the root zone is starving, overloaded or locked out."),
    steps([
      ("Step 1, check input pH and EC", "Confirm the feed you are giving is actually in range for your medium: pH 5.8-6.2 in coco or hydro, around 6.5 in soil, at a stage-appropriate strength."),
      ("Step 2, measure runoff", "In coco, runoff EC should come out roughly equal to input. Runoff much higher than input (e.g. more than 200 PPM higher) means salt buildup and overfeeding. Pale plants with low runoff EC mean underfeeding."),
      ("Step 3, match the fix to the cause", "Lockout or salt buildup: flush with correctly pH'd plain or light water until runoff EC normalises, then resume. Underfeeding: raise EC gradually. True single deficiency: correct pH first, then supplement the specific nutrient."),
      ("Step 4, watch new growth", "Look at the new leaves, not the damaged ones, for recovery over 5-10 days. Old damage will not re-green."),
    ]),
    figure(L.line("Stage feed-strength targets (coco / hydro)",
            [(0, 0.6), (1, 1.4), (2, 2.0), (3, 2.7), (4, 1.2)],
            ["seedling", "veg", "early flower", "peak flower", "flush"],
            ylab="EC", ymin=0, ymax=3.2, bands=[(1.0, 2.4, L.GL, "typical working band")],
            note="A rising target, not single points. Verify against your specific nutrient line."), 8,
      "Target EC climbs from seedling through peak flower, then eases for the finish. Seedling roughly "
      "0.4-0.8 (about 250-400 PPM), veg 1.0-1.8, flower 1.6-2.4 rising to 2.4-3.0 late."),
    callout("note", "Runoff EC is your salt gauge",
      p("Coco runoff EC should approximate input EC. Runoff more than about 200 PPM above input "
        "indicates salt is building up faster than the plant can use it, and a flush, not more feed, "
        "is the answer.")),
  ]})

SECTIONS.append({"id": "pitfalls", "kicker": "Troubleshooting", "title": "Common traps and look-alikes that fool beginners",
  "blocks": [
    p("Most deficiencies beginners post about are actually pH lockout, overwatering or light burn "
      "wearing a deficiency costume. Knowing the impostors stops you from dumping fertiliser on a "
      "plant that is drowning, burning or locked out. When in doubt, change one variable at a time "
      "and wait."),
    table(["Impostor", "Imitates", "The giveaway", "Check this, not feed"], [
      ["Overwatering", "Nitrogen toxicity (droopy, clawed)", "Wet medium, slow drinking", "Soil moisture, pot drainage"],
      ["Root rot", "Multiple deficiencies at once", "Brown slimy roots, foul smell", "Root health, oxygen at roots"],
      ["Light / heat stress", "Nutrient burn or deficiency", "Damage only on top canopy near the lamp", "Distance to light, canopy temperature"],
      ["pH lockout", "Iron or cal-mag deficiency", "Deficiency look despite correct feed", "Input and runoff pH"],
      ["Nutrient antagonism", "Cal-mag deficiency", "Followed an over-dose of one element", "Whether you over-supplemented K"],
    ], cls="compact", caption="The five impostors. Each one looks like hunger and each one is made worse by feeding."),
    p("Antagonism is the subtle one: too much of one nutrient blocks another. Excess potassium "
      "suppresses calcium and magnesium uptake, so a cal-mag deficiency can actually be a potassium "
      "excess, which is exactly why over-supplementing single elements backfires." + _c("fageria-2001-nutrient-interactions-antagonism")),
    figure(L.flow("Rule-out order before declaring a deficiency",
            [("pH check", "in range for medium?"),
             ("EC / runoff check", "starving or overloaded?"),
             ("Watering / root check", "drowning or rotting?"),
             ("Light / heat check", "burning at the top?"),
             ("True deficiency", "only now supplement")],
            note="Pass every gate before you reach for fertiliser."), 9,
      "Overwatering and light stress mimic nutrient disorders, so a true single-nutrient deficiency is "
      "the last conclusion, not the first." + _c("fageria-2001-nutrient-interactions-antagonism")),
  ]})

SECTIONS.append({"id": "realistic-expectations", "kicker": "Reality check", "title": "What to realistically expect",
  "blocks": [
    p("Diagnosis gives you a confident shortlist, not lab certainty. Visual symptoms overlap, and "
      "only a tissue or substrate test is definitive." + _c("cockson-2019-nutrient-disorders-cannabis") +
      " Damaged leaves never heal, so success looks like healthy new growth, not the recovery of "
      "burnt ones."),
    ul([
      "Expect to be right about the category (mobile vs immobile, deficiency vs toxicity vs lockout) more often than the exact element, and that is usually enough to act correctly.",
      "After a correct fix, look for normal new growth within roughly 5-10 days. Existing damaged leaves will not re-green and can be left or removed.",
      "A single clean pH and EC routine prevents the large majority of nutrient problems. Chasing individual-element cures is a sign the underlying routine needs fixing.",
      "For high-value or commercial crops, confirm ambiguous cases with leaf-tissue or substrate analysis rather than eyeballing.",
    ]),
    figure(L.bars("Effort: prevention vs cure",
            [("Stable pH / EC routine", 25), ("Diagnose & recover a disorder", 80), ("Lost yield from damage", 60)],
            unit="", note="A small recurring routine costs far less than reacting to disorders.", maxv=100), 10,
      "The cheap habit on the left prevents most of the expensive work on the right. Prevention beats "
      "diagnosis every time."),
    callout("key", "Prevention beats diagnosis",
      p("The visual method is a fast first pass, not the final word. Most problems never appear if pH "
        "and feed strength stay stable, so build the routine first and treat diagnosis as a backstop.")),
    p("Next, lock down the two routines that prevent most of this: read the "
      "<a href='ph-management.html'>pH management</a> guide, then the "
      "<a href='nutrient-mixing-athena.html'>nutrient mixing</a> guide to get your feed right from the start."),
  ]})
