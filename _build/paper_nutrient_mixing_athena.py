# -*- coding: utf-8 -*-
"""Paper: making a 50 L Athena Pro Line STOCK CONCENTRATE from a full 25 lb bag."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        stagecard, grid, card, chip, kv, steps)
import figs_lib as L

SLUG = "nutrient-mixing-athena"
TITLE = "Dissolve Athena Pro Line powder into a 50 L stock tank"
EYEBROW = "Feed · Mix nutrients"
SUB = ("Dissolve a full 11.34 kg (25 lb) bag of Athena Pro Line in a 50 L tank to make a stock "
       "concentrate. Add a small quantity of the stock to the feed water to make the feed. This "
       "paper shows that the water temperature and the mixing are important at 227 g/L. It shows "
       "that Part A and Part B must be in different tanks. It also shows how to calculate the dose "
       "in milliliters for each liter of feed.")
META = [("beaker", "Feed and mixing"), ("image", "6 diagrams"),
        ("quote", "6 sources"), ("clock", "~11 min to read")]
RELATED = ["coco-crop-steering", "irrigation-manual", "root-zone-teros12"]
REF_IDS = ["purdue-fertilizer-compatibility", "scienceinhydroponics-caso4",
           "libretexts-temperature-solubility", "saloner-mineral-uptake-dynamics",
           "saloner-bernstein-response-surface-nutrition", "powell-bauerle-uptake-massbalance",
           "valdrighi-reservoir-water-quality", "yep-nacl-cannabis-stress"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

# 1 -----------------------------------------------------------------
SECTIONS.append({"id": "intro", "kicker": "Start here", "title": "Purpose and scope",
  "blocks": [
    lead("In this paper, the task is to dissolve a <strong>full 11.34 kg (25 lb) bag</strong> of "
         "Athena Pro Line in a <strong>50 L tank</strong>. The result is a strong <strong>stock "
         "solution</strong>. Do not give this solution to the plants directly, because it is much "
         "too strong. Make the stock solution one time. Then measure a small quantity of the stock "
         "solution. Add it to your irrigation tank to make the feed."),
    p("A stock tank changes a powder that is not easy to use into a liquid that is easy to use. "
      "When you weigh the powder each time you make feed, the procedure is slow and the quantity is "
      "not the same each time. Dissolve the full bag one time. Then add the stock to your feed "
      "water in a quantity that you measure, in milliliters for each liter. Each time, you get the "
      "same feed in seconds."),
    callout("key", "In short",
      p("A full 11.34 kg (25 lb) bag in 50 L makes a stock of approximately <strong>227 grams for "
        "each liter</strong>. The stock is a strong concentrate. Make sure that all the powder "
        "dissolves. Keep the two parts in <em>different</em> tanks. Know how many milliliters of "
        "stock to add to each liter of feed water.")),
    callout("note", "Your equipment",
      p("This paper is for the equipment that you have. The equipment is a full 11.34 kg (25 lb) "
        "bag, a 50 L tank, jugs of hot water, and a paint-mixer paddle on a drill. At this "
        "concentration, you must use the paddle. You cannot mix 11 kg of salt into the solution "
        "manually.")),
  ]})

# 2 -----------------------------------------------------------------
SECTIONS.append({"id": "terms", "kicker": "Terms", "title": "Definitions",
  "blocks": [
    defterm("Stock solution (concentrate)", "A strong nutrient solution that you keep in a tank and "
            "add to the feed water in small quantities. In this paper, it is one full bag in 50 L. "
            "Do not give it to the plants directly."),
    defterm("Working solution (feed)", "The diluted solution that the plants use. You make it when "
            "you add a small quantity of stock to a large quantity of water."),
    defterm("Part A / Pro Core", "The part of Athena Pro Line that contains calcium and nitrogen. "
            "Put <strong>only</strong> Part A in its stock tank."),
    defterm("Part B / Pro Grow or Pro Bloom", "The part of Athena Pro Line that contains sulfates "
            "and phosphates. It must have a <strong>different</strong> stock tank from Part A."),
    defterm("Dose rate", "The quantity of stock that you add to each liter of feed water, in "
            "milliliters for each liter (mL/L). You use this value each day."),
    defterm("Solubility / saturation", "The quantity of salt that a specified volume of water can "
            "hold. Water holds more salt when the temperature is higher. If you add more salt than "
            "this limit, the salt does not dissolve and stays as grit" +
            _c("libretexts-temperature-solubility") + ". Grit is solid particles of salt in the "
            "tank."),
    defterm("Precipitation / lockout", "Dissolved salts make a solid and fall out of the solution. "
            "For example, calcium makes a solid with sulfate or with phosphate. The nutrient is not "
            "in the water, and the plant cannot use it" + _c("scienceinhydroponics-caso4") +
            "."),
    defterm("EC (electrical conductivity)", "A meter reading of the total quantity of dissolved "
            "salt. You use this reading to do a check of the strength of the feed that you make."),
  ]})

# 3 -----------------------------------------------------------------
SECTIONS.append({"id": "cardinal-rule", "kicker": "The primary instruction", "title": "Keep part A and part B in different tanks",
  "blocks": [
    p("Put Part A in one stock tank and Part B in a different stock tank. Do not let the two "
      "concentrates touch each other. <strong>This instruction prevents damage to your crop and to "
      "your pump.</strong> Put one 11.34 kg (25 lb) bag of Pro Core in one 50 L tank. Put one 11.34 "
      "kg (25 lb) bag of Pro Grow/Bloom in a different 50 L tank."),
    p("The cause is chemical. Part A contains a large quantity of <strong>calcium</strong>, and "
      "Part B contains <strong>sulfates and phosphates</strong>. In a diluted feed, there is no "
      "problem. But if you put the two <em>concentrates</em> together, the calcium immediately "
      "makes a solid with the sulfate and the phosphate. The solid is gypsum and calcium phosphate" +
      _c("purdue-fertilizer-compatibility") + ". The result is a tank of sludge that you cannot "
      "use, and the crop does not get the nutrients that you added" + _c("scienceinhydroponics-caso4") +
      "."),
    figure(L.flow("Where the two parts touch",
            [("Bag A to Tank A", "Pro Core stock only"), ("Bag B to Tank B", "Grow/Bloom stock only"),
             ("Feed water", "add A and mix"), ("Same water", "then add B and mix"),
             ("Plants", "safe, diluted feed")],
            note="They touch only when diluted in the feed water. Add them one at a time."), 1,
      "If you put concentrates A and B together, they make a precipitate immediately. If you add A "
      "and B to the feed water one at a time, the water dilutes each concentrate and they stay in "
      "solution. This difference is the cause of the primary instruction."),
    callout("danger", "Do not do these tasks",
      ul(["Do not add Part A stock to Part B stock. Do not add Part B stock to Part A stock.",
          "Do not add the two concentrates to the feed water at the same time. Add A and mix. Then add B and mix.",
          "Clean the jug with water before you use the jug for the other part."], "tight")),
  ]})

# 4 -----------------------------------------------------------------
SECTIONS.append({"id": "chemistry", "kicker": "The cause", "title": "How to dissolve 227 g/L fully",
  "blocks": [
    p("227 grams of salt for each liter is a large quantity. It is approximately six to seven times "
      "more salt than in seawater. It is not automatic that all the salt dissolves. Two effects can "
      "cause some of the salt to stay solid:"),
    ul([
      "<strong>Salt that dissolves makes the water colder.</strong> Most of these salts "
      "<em>absorb</em> heat when they dissolve (endothermic). Thus the tank becomes colder when you "
      "add powder, and less salt dissolves in colder water" + _c("libretexts-temperature-solubility") +
      ". Hot water and a paddle prevent this problem.",
      "<strong>Cold water and water that does not move become saturated.</strong> If you do not use "
      "heat and strong mixing, the solution is at the saturation limit. The last part of the bag "
      "stays as grit on the bottom. Then the stock has a concentration that is too low, and the "
      "concentration is not the same each time.",
    ]),
    figure(L.line("Hot water dissolves more salt",
            [(10, 35), (20, 50), (30, 66), (40, 82), (50, 95)],
            ["10C", "20C", "30C", "40C", "50C"], ylab="solubility index",
            note="Use hot water because solubility increases with temperature. Salt makes the tank colder when it dissolves."), 2,
      "Solubility increases when the temperature increases. Thus hot water holds more salt. Salt "
      "that dissolves makes the water colder, and hot water decreases this effect" +
      _c("libretexts-temperature-solubility") + "."),
    callout("warn", "Hot water, not boiling water",
      p("Use hot tap water at approximately 40&ndash;50&nbsp;&deg;C (104&ndash;122&nbsp;&deg;F). Do "
        "not use boiling water. Boiling water can cause damage to some compounds. Boiling water can "
        "also burn your skin when the paddle moves the water. Warm water gives sufficient "
        "solubility.")),
  ]})

# 5 -----------------------------------------------------------------
SECTIONS.append({"id": "method", "kicker": "The method", "title": "Stock-tank mixing procedure",
  "blocks": [
    p("Do the procedure below one time for each part. Do it one time for the Pro Core bag (Tank A) "
      "and one time for the Pro Grow/Bloom bag (Tank B). The steps are the same each time."),
    steps([
      ("Start with hot water: approximately 40 L", "Fill the 50 L tank to approximately 40 L with hot water at approximately 40&ndash;50&nbsp;&deg;C (104&ndash;122&nbsp;&deg;F). Keep headroom in the tank. The 11 kg of powder increases the volume. The water must not spill when you mix."),
      ("Start the paddle before you add the powder", "Make a vortex in the water with the paddle. The salt must go into water that moves. The salt must not collect on the bottom of the tank."),
      ("Add the powder slowly", "Add the powder slowly and continuously. Do not add the full bag at one time. If you add all the powder at one time, clumps occur. A clump holds dry powder in the middle, and this powder does not dissolve (a &lsquo;fish-eye&rsquo;)."),
      ("Mix until the solution is transparent", "Continue to mix until there is no grit and the solution is transparent. The solution can have a color. At this concentration, it is possible that you must mix for some minutes, and not for seconds."),
      ("Fill to the 50 L mark", "When all the salt dissolves, add warm water until the solution is at the 50 L mark. The concentration is accurate because you add the water <em>after</em> the salt dissolves."),
      ("Put a label and the date on the tank", "Write &lsquo;PART A, Pro Core&rsquo; or &lsquo;PART B, Grow/Bloom&rsquo; and the date on the label. The two tanks look the same. If you use the incorrect tank, you do not obey the primary instruction."),
      ("Let the solution become colder, then do a check again", "When the solution becomes colder, look for solid material that falls out of the solution. A small quantity of sediment can show that the solution was near saturation. Mix the solution again. If the sediment stays, it is possible that you must add a small quantity of water."),
    ]),
    figure(L.flow("The sequence for each bag",
            [("Hot water ≈40 L", "fill first"), ("Paddle on", "make a vortex"),
             ("Add bag slowly", "continuous"), ("Mix fully", "no grit"),
             ("Fill to 50 L", "correct strength"), ("Label: A or B", "and date")],
            note="The same for the two bags. Use two different tanks, each with a label."), 3,
      "The diagram shows all the steps of the method. Do the method two times, one time for each bag, in two different tanks."),
  ]})

# 6 -----------------------------------------------------------------
SECTIONS.append({"id": "numbers", "kicker": "The numbers", "title": "Stock concentration and dose",
  "blocks": [
    p("A full bag weighs <strong>11.34 kg</strong> (25 lb). In 50 L, the stock has this concentration:"),
    figure(L.bars("Stock concentration from a full bag in 50 L",
            [("For each liter", 227), ("For 100 mL", 23)], unit=" g",
            note="11.34 kg / 50 L = 226.8 g/L. This is the strength of your concentrate.", maxv=260), 4,
      "11.34 kg in 50 L = <strong>226.8 g/L</strong>. When you know this number, you can change the "
      "feed rate on your bag to a dose in milliliters for each liter."),
    p("To use the stock, you dilute it. The bag (or the Athena chart) gives the feed rate for a "
      "part. The feed rate is <em>X grams for each liter</em> of diluted feed. Use the formula "
      "below, because your stock is 226.8 g/L."),
    callout("key", "The formula for the dose rate",
      p("<strong>Dose rate (mL of stock for each L of feed) = feed rate (g/L) &divide; 226.8 "
        "&times; 1000 &asymp; feed rate &times; 4.41</strong>" + _c("powell-bauerle-uptake-massbalance") +
        ". Calculate the dose rate for Part A and for Part B. Use the feed rate of each part.")),
    table(["Feed rate on the label", "Dose of stock for each liter of feed"], [
      ["0.5 g/L", "<span class='num'>2.2 mL/L</span>"],
      ["1.0 g/L", "<span class='num'>4.4 mL/L</span>"],
      ["1.5 g/L", "<span class='num'>6.6 mL/L</span>"],
      ["2.0 g/L", "<span class='num'>8.8 mL/L</span>"],
    ], caption="Doses for your stock of 226.8 g/L. Each time, make sure that the target rate agrees with your bag, because formulas change."),
    callout("warn", "Do the last check with a meter",
      p("Mix the feed and read the EC with your <strong>EC meter</strong>. Use the meter reading "
        "and not the calculated dose rate, because water and formulas change" +
        _c("valdrighi-reservoir-water-quality") + ". The calculated dose rate is only an "
        "approximate value.")),
  ]})

# 7 -----------------------------------------------------------------
SECTIONS.append({"id": "targets", "kicker": "The feed", "title": "Feed strength targets for each stage",
  "blocks": [
    p("The stock only supplies the nutrients. The strength of the <em>feed</em> is important for "
      "the plant, and you read the strength as EC. A weak feed is correct for plants in the first "
      "stage, and a strong feed is correct for plants in the bulk stage. At the end of the cycle, "
      "you decrease the strength. The quantity of nutrients that cannabis uses changes during the "
      "cycle" + _c("saloner-mineral-uptake-dynamics") + "."),
    figure(L.zones("Approximate feed EC for each stage", 0.8, 4.0,
            [(0.8, 1.6, L.BLUL, "clones / seedling"), (1.6, 2.6, L.GL, "vegetative stage"),
             (2.6, 3.4, L.GXL, "flower bulk"), (3.4, 4.0, L.AMBL, "end / decrease")],
            unit=" EC",
            note="Approximate ranges: use your meter and follow the Athena chart for your cultivar."), 5,
      "Use a weak feed in the first stage. Increase the strength in the vegetative stage and the "
      "flowering stage. Decrease the strength in the last stage" +
      _c("saloner-bernstein-response-surface-nutrition") + ". These ranges are start values. They "
      "are not limits. The substrate and the cultivar change the ranges."),
    callout("danger", "Too much feed causes stress",
      p("Do not increase the EC for more growth. A high EC does not cause more growth. The salt in "
        "the root zone removes water from the roots, and the plant cannot absorb water. This effect "
        "is osmotic stress" + _c("yep-nacl-cannabis-stress") + ". The plant shows wilt also in a "
        "wet slab. If you are not sure, make the feed weaker by a small quantity.")),
  ]})

# 8 -----------------------------------------------------------------
SECTIONS.append({"id": "trouble", "kicker": "When there is a problem", "title": "Storage and troubleshooting",
  "blocks": [
    table(["Symptom", "Possible cause", "Correction"], [
      ["Grit on the bottom of the tank", "The solution is at saturation. The water is too cold, or you did not mix the solution sufficiently.", "Mix again with the paddle. Increase the temperature of the solution. If the grit stays, add a small quantity of water."],
      ["Crystals in the stock after storage", "The stock became colder, and salt fell out of the solution. The stock was near saturation.", "Increase the temperature of the stock slowly and mix it again before you add it to the feed. Keep the stock where it is not cold."],
      ["The stock is white and not transparent", "Possible contamination of the Part B tank with Part A", "Do not give the stock to the plants, because it is possible that it has a precipitate. Examine your jugs and labels" + _c("purdue-fertilizer-compatibility")],
      ["The EC of the feed is lower than the calculated value", "The salt in the bag did not dissolve fully, and the stock has a concentration that is too low.", "Make sure that the salt dissolves fully in the stock. Calibrate the EC meter again."],
      ["Sludge after you put A and B together", "The concentrates A and B touched each other.", "Discard the sludge. It is a precipitate and you cannot use it. Do not put the concentrates together."],
    ], cls="compact"),
    callout("tip", "Storage",
      p("Keep each stock tank sealed and away from cold and from light. Put a label on each tank. "
        "Mix the stock before you use it, because salt can fall to the bottom of the tank. Make "
        "only the quantity of stock that you will use in a short time. Do not make the supply for a "
        "year" + _c("valdrighi-reservoir-water-quality") + ".")),
  ]})

# 9 -----------------------------------------------------------------
SECTIONS.append({"id": "expect", "kicker": "The limits", "title": "Expected results and limitations",
  "blocks": [
    callout("key", "The primary information",
      ol(["<strong>Two bags and two tanks. Do not put the concentrates together.</strong> This instruction prevents damage to the stock.",
          "<strong>Hot water, the paddle and sufficient time</strong> make all the 226.8 g/L dissolve. The solution is transparent and has no grit.",
          "<strong>Add the stock to the feed water. Do not give the stock to the plants.</strong> Dilute the stock to an EC target. Use a meter each time to make sure of the EC.",
          "<strong>Use a feed strength that agrees with the stage</strong>, and know that a stronger feed is not better" + _c("yep-nacl-cannabis-stress") + "."])),
    p("When you have the stock, the task for each day is to add the stock to the feed water and to "
      "apply the feed correctly. Read the <a href='coco-crop-steering.html'>coco and crop "
      "steering</a> paper for information on the effect of the feed in the root zone. Read the <a "
      "href='irrigation-manual.html'>irrigation manual</a> for information on how to apply the feed."),
  ]})
