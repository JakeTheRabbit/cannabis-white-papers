# -*- coding: utf-8 -*-
"""Paper: making a 50 L Athena Pro Line STOCK CONCENTRATE from a full 25 lb bag."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        stagecard, grid, card, chip, kv, steps)
import figs_lib as L

SLUG = "nutrient-mixing-athena"
TITLE = "Mixing an Athena Pro Line stock tank (metric)"
EYEBROW = "Feed · Nutrient mixing"
SUB = ("Dissolve a full 25 lb bag of Athena Pro Line into a 50 L stock tank to make a "
       "concentrate you dose into your feed later. Covers the chemistry of getting ~227 g/L "
       "of salt fully into solution, and why each part needs its own tank.")
META = [("beaker", "Feed & mixing"), ("image", "6 diagrams"),
        ("quote", "Evidence-linked · 6 sources"), ("clock", "~11 min read")]
RELATED = ["coco-crop-steering", "irrigation-manual", "root-zone-teros12"]
REF_IDS = ["purdue-fertilizer-compatibility", "scienceinhydroponics-caso4",
           "libretexts-temperature-solubility", "saloner-mineral-uptake-dynamics",
           "saloner-bernstein-response-surface-nutrition", "powell-bauerle-uptake-massbalance",
           "valdrighi-reservoir-water-quality", "yep-nacl-cannabis-stress"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

# 1 -----------------------------------------------------------------
SECTIONS.append({"id": "intro", "kicker": "Start here", "title": "What a stock tank is, and why you make one",
  "blocks": [
    lead("This guide covers one job: dissolving a <strong>full 25 lb bag</strong> of "
         "Athena Pro Line into a <strong>50 L tank</strong> to make a concentrated "
         "<strong>stock solution</strong>. You don't feed plants with this. It's far too "
         "strong. You make it once, then dose small amounts into your watering tank to make "
         "the actual feed."),
    p("A stock tank turns an awkward powder into an easy liquid. Weighing powder every time you mix "
      "feed is slow and inconsistent. Dissolve the whole bag once, then pump "
      "or pour a measured number of millilitres per litre into your feed water. Same recipe, every "
      "time, in seconds."),
    callout("key", "The one-sentence version",
      p("A full 25 lb (11.34 kg) bag into 50 L makes a stock at about <strong>227 grams per "
        "litre</strong>, a heavy concentrate. Your whole job is to get every gram truly "
        "dissolved, keep the two parts in <em>separate</em> tanks, and know how many millilitres to "
        "dose downstream.")),
    callout("note", "Your kit",
      p("Written for exactly what you have: a full 25 lb bag, a 50 L tank, jugs of hot water, and a "
        "paint-mixer paddle on a drill. The paddle is not optional at this concentration. "
        "You cannot hand-stir 11 kg of salt into solution.")),
  ]})

# 2 -----------------------------------------------------------------
SECTIONS.append({"id": "terms", "kicker": "Vocabulary", "title": "The words you need",
  "blocks": [
    defterm("Stock solution (concentrate)", "A strong nutrient solution you store and dose from. "
            "Here, one whole bag in 50 L. Never fed to plants neat."),
    defterm("Working solution (feed)", "The diluted solution the plants actually drink, made by "
            "dosing a little stock into a lot of water."),
    defterm("Part A / Pro Core", "The calcium-and-nitrogen base of Athena Pro Line. Gets its "
            "<strong>own</strong> stock tank."),
    defterm("Part B / Pro Grow or Pro Bloom", "The part carrying sulfates and phosphates. Gets a "
            "<strong>separate</strong> stock tank from Part A."),
    defterm("Dosing rate", "How much stock you add per litre of feed water, in millilitres per "
            "litre (mL/L). This is what you use day to day."),
    defterm("Solubility / saturation", "How much salt a given volume of water can hold. Warmer "
            "water holds more. Past its limit, salt won't dissolve and sits as grit" + _c("libretexts-temperature-solubility") + "."),
    defterm("Precipitation / lockout", "When dissolved salts react and fall out as solid, "
            "for example calcium meeting sulfate or phosphate. The nutrient leaves the water and the plant "
            "can't use it" + _c("scienceinhydroponics-caso4") + "."),
    defterm("EC (electrical conductivity)", "A meter reading of total dissolved salt. This is how you "
            "check the strength of your finished feed."),
  ]})

# 3 -----------------------------------------------------------------
SECTIONS.append({"id": "cardinal-rule", "kicker": "The one rule", "title": "Two parts, two tanks, never combine concentrated",
  "blocks": [
    p("Part A and Part B each get their own stock tank, and the two concentrates must never touch. "
      "<strong>This is the rule that saves your crop and your pump.</strong> One 25 lb "
      "bag of Pro Core → one 50 L tank. One 25 lb bag of Pro Grow/Bloom → a different 50 L tank."),
    p("The reason is chemistry. Part A is loaded with <strong>calcium</strong>. Part B carries "
      "<strong>sulfates and phosphates</strong>. In a dilute feed that's fine, but if you pour the "
      "two <em>concentrates</em> together the calcium instantly grabs the sulfate and phosphate and "
      "drops out as solid gypsum and calcium phosphate" + _c("purdue-fertilizer-compatibility") +
      ". You get a tank of useless sludge and a crop starved of the very nutrients you just "
      "added" + _c("scienceinhydroponics-caso4") + "."),
    figure(L.flow("Where the two parts are allowed to meet",
            [("Bag A to Tank A", "Pro Core stock, alone"), ("Bag B to Tank B", "Grow/Bloom stock, alone"),
             ("Feed water", "dose A in, stir"), ("Same water", "then dose B in, stir"),
             ("Plants", "now dilute & safe")],
            note="They only ever meet heavily diluted, in the feed water, added one at a time."), 1,
      "Concentrated A plus concentrated B gives an instant precipitate. Diluted, added separately to feed "
      "water, they coexist fine. That gap is the whole rule."),
    callout("danger", "Never do these",
      ul(["Never pour Part A stock into Part B stock (or vice-versa).",
          "Never add the two concentrates to feed water at the same moment. Add A, stir, then add B, stir.",
          "Never reuse a dosing jug between A and B without rinsing."], "tight")),
  ]})

# 4 -----------------------------------------------------------------
SECTIONS.append({"id": "chemistry", "kicker": "The why", "title": "What it takes to dissolve 11 kg in 50 L",
  "blocks": [
    p("227 grams of salt per litre is a lot, roughly six to seven times saltier than "
      "seawater. Getting it fully into solution isn't automatic. Two bits of physics work against "
      "you."),
    ul([
      "<strong>Dissolving cools the water.</strong> Most of these salts pull heat <em>in</em> as "
      "they dissolve (endothermic), so the tank gets colder as you add powder, and colder "
      "water dissolves less" + _c("libretexts-temperature-solubility") + ". Hot water and a paddle beat "
      "that downward spiral.",
      "<strong>Cold or still water saturates.</strong> Without heat and vigorous mixing, you hit "
      "the saturation limit and the last of the bag sits as grit on the bottom, leaving an "
      "underdosed, inconsistent stock.",
    ]),
    figure(L.line("Warmer water dissolves more salt",
            [(10, 35), (20, 50), (30, 66), (40, 82), (50, 95)],
            ["10C", "20C", "30C", "40C", "50C"], ylab="relative amount dissolvable",
            note="Why you start with hot water: solubility climbs with temperature, and dissolving cools the tank."), 2,
      "Solubility rises with temperature, so hot water both holds more and offsets the cooling the "
      "dissolving salt causes" + _c("libretexts-temperature-solubility") + "."),
    callout("warn", "Hot, not boiling",
      p("Use hot tap water (about 40-50&nbsp;&deg;C), not boiling. Boiling water can damage some "
        "compounds and is a scald hazard with a spinning paddle. Warm is enough to win the "
        "solubility fight.")),
  ]})

# 5 -----------------------------------------------------------------
SECTIONS.append({"id": "method", "kicker": "The method", "title": "Step-by-step: one bag into one 50 L tank",
  "blocks": [
    p("Do this once per part: once for the Pro Core bag (Tank A), once for the Pro "
      "Grow/Bloom bag (Tank B). Same steps each time."),
    steps([
      ("Start with hot water, ~40 L", "Fill the 50 L tank to about 40 L with hot water (about 40-50&nbsp;&deg;C). Leave headroom. 11 kg of powder takes up real volume and you still need room to mix without slopping."),
      ("Start the paddle before adding powder", "Get the paint-mixer turning a vortex first. You want the salt landing in moving water, not piling on a still bottom."),
      ("Add the bag gradually", "Pour the powder in slowly, a steady stream, not the whole bag at once. Dumping it causes clumps that trap dry powder inside (a 'fish-eye') that never dissolves."),
      ("Mix until perfectly clear", "Keep mixing until there is zero grit and the solution is clear (it may be tinted). At this concentration this can take several minutes of active mixing, not seconds."),
      ("Top up to exactly 50 L", "Once fully dissolved, top with warm water to the 50 L mark. Topping up <em>after</em> dissolving keeps your concentration exact."),
      ("Label and date the tank", "Mark it 'PART A, Pro Core' or 'PART B, Grow/Bloom' plus the date. Mixing up two near-identical tanks is how the cardinal rule gets broken."),
      ("Let it cool and settle, then re-check", "As it cools, watch for anything dropping out. A little fine sediment can mean you were at the edge of saturation. Re-mix. If it persists, the bag may need slightly more volume."),
    ]),
    figure(L.flow("The fixed sequence (per bag)",
            [("Hot water ~40 L", "fill first"), ("Paddle on", "make a vortex"),
             ("Add bag slowly", "steady stream"), ("Mix to clear", "zero grit"),
             ("Top to 50 L", "exact strength"), ("Label A or B", "and date")],
            note="Identical for both bags - just two separate, clearly-labelled tanks."), 3,
      "The whole method on one line. Run it twice: once per bag, into two separate tanks."),
  ]})

# 6 -----------------------------------------------------------------
SECTIONS.append({"id": "numbers", "kicker": "The numbers", "title": "Your stock strength, and how to dose it",
  "blocks": [
    p("A full 25 lb bag is <strong>11.34 kg</strong>. In 50 L that gives a stock of:"),
    figure(L.bars("Stock concentration from a full bag in 50 L",
            [("Per litre", 227), ("Per 100 mL", 23)], unit=" g",
            note="11.34 kg / 50 L = 226.8 g/L. That's your concentrate strength.", maxv=260), 4,
      "11.34 kg in 50 L = <strong>226.8 g/L</strong>. Knowing this one number lets you convert your "
      "bag's printed feed rate into a simple millilitres-per-litre dose."),
    p("To use it, you dilute. If your bag (or Athena's chart) says to feed a part at a rate of "
      "<em>X grams per litre</em> of finished feed, then because your stock is 226.8 g/L:"),
    callout("key", "The dosing formula",
      p("<strong>Dose (mL of stock per L of feed) = feed rate (g/L) &divide; 226.8 &times; 1000 "
        "&asymp; feed rate &times; 4.41</strong>" + _c("powell-bauerle-uptake-massbalance") + ". Do this "
        "separately for Part A and Part B using each part's own rate.")),
    table(["If the label feed rate is...", "...dose this much stock per litre of feed"], [
      ["0.5 g/L", "<span class='num'>2.2 mL/L</span>"],
      ["1.0 g/L", "<span class='num'>4.4 mL/L</span>"],
      ["1.5 g/L", "<span class='num'>6.6 mL/L</span>"],
      ["2.0 g/L", "<span class='num'>8.8 mL/L</span>"],
    ], caption="Dosing your 226.8 g/L stock. Always confirm the target rate on your bag - formulas change."),
    callout("warn", "Always finish on a meter",
      p("Dosing math gets you close. Your <strong>EC meter</strong> confirms it. Mix the feed, read "
        "EC, and trust the meter over the calculator, because water and formulas vary" + _c("valdrighi-reservoir-water-quality") + ".")),
  ]})

# 7 -----------------------------------------------------------------
SECTIONS.append({"id": "targets", "kicker": "Downstream", "title": "What strength to feed, by stage",
  "blocks": [
    p("The stock is only a delivery system. The plant cares about the <em>feed</em> strength, read "
      "as EC. Young plants want it weak, bulking plants want it strong, and you taper at the end. "
      "Cannabis nutrient demand genuinely shifts across the cycle" + _c("saloner-mineral-uptake-dynamics") + "."),
    figure(L.zones("Rough feed-EC targets by stage", 0.8, 4.0,
            [(0.8, 1.6, L.BLUL, "clones / seedling"), (1.6, 2.6, L.GL, "veg"),
             (2.6, 3.4, L.GXL, "flower bulk"), (3.4, 4.0, L.AMBL, "late / taper")],
            unit=" EC",
            note="Indicative bands - run your own meter and follow Athena's chart for your cultivar."), 5,
      "Feed weak early, build through veg and flower, taper late" + _c("saloner-bernstein-response-surface-nutrition") +
      ". These are starting bands, not law. Substrate and strain shift them."),
    callout("danger", "Over-feeding is its own stress",
      p("Cranking EC does not mean more growth. Too much salt in the root zone pulls water "
        "back out of the roots (osmotic stress) and burns the plant" + _c("yep-nacl-cannabis-stress") +
        ". When in doubt, feed slightly weaker.")),
  ]})

# 8 -----------------------------------------------------------------
SECTIONS.append({"id": "trouble", "kicker": "When it goes wrong", "title": "Storage & troubleshooting",
  "blocks": [
    table(["Symptom", "Likely cause", "What to do"], [
      ["Grit on the tank bottom", "Hit saturation - water too cold or under-mixed", "Re-mix with the paddle; warm it; if it won't clear, add a little more volume"],
      ["Crystals form in storage", "Stock cooled and dropped out near saturation", "Warm gently and re-mix before dosing; store somewhere not cold"],
      ["Cloudy / milky stock", "Possible cross-contamination of A into B", "Suspect a precipitate - do not feed; check your jugs/labels" + _c("purdue-fertilizer-compatibility")],
      ["Feed EC lower than the math predicts", "Bag didn't fully dissolve / underdosed stock", "Confirm stock fully dissolved; recalibrate the EC meter"],
      ["Sludge after combining", "Concentrates A and B were mixed", "Discard - this is precipitated, unusable; never combine concentrates"],
    ], cls="compact"),
    callout("tip", "Storage",
      p("Keep each stock tank sealed, labelled, out of cold and out of light. Mix before each use in "
        "case anything has settled. Make what you'll use in a reasonable window rather than a year's "
        "supply" + _c("valdrighi-reservoir-water-quality") + ".")),
  ]})

# 9 -----------------------------------------------------------------
SECTIONS.append({"id": "expect", "kicker": "Straight talk", "title": "What good looks like",
  "blocks": [
    callout("key", "Remember",
      ol(["<strong>Two bags, two tanks, never combined concentrated.</strong> This is the rule that prevents ruined stock.",
          "<strong>Hot water + the paddle + patience</strong> get all 226.8 g/L truly dissolved - clear, zero grit.",
          "<strong>Stock is for dosing, not feeding.</strong> Dilute to an EC target and confirm on a meter, every time.",
          "<strong>Match feed strength to stage</strong>, and remember stronger isn't better" + _c("yep-nacl-cannabis-stress") + "."])),
    p("Once your stock is made, the day-to-day is dosing into feed water and watering well. "
      "See <a href='coco-crop-steering.html'>coco &amp; crop steering</a> for how that feed "
      "behaves in the root zone, and the <a href='irrigation-manual.html'>irrigation manual</a> for "
      "delivering it."),
  ]})
