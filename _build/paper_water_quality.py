# -*- coding: utf-8 -*-
"""Paper: source water, RO and alkalinity for cannabis (beginner)."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        stagecard, grid, card, chip, kv, steps)
import figs_lib as L

SLUG = "water-quality"
TITLE = "Source water, RO and alkalinity"
EYEBROW = "Feed · Water"
SUB = ("What is in your water before nutrients ever go in: tap vs RO vs well, starting EC, "
       "alkalinity and carbonates, chlorine and chloramine, hardness, and when reverse "
       "osmosis is actually worth the money.")
META = [("droplet", "Beginner"), ("image", "13 figures"),
        ("quote", "Peer-reviewed · 6 sources"), ("clock", "~14 min read")]
RELATED = ["ph-management", "nutrient-mixing-athena", "irrigation-manual"]
REF_IDS = ["bevan-2021-npk-flowering-cannabis",
           "kpai-2024-mineral-nutrition-vegetative-cannabis",
           "umass-water-quality-ph-alkalinity",
           "fisher-purdue-ho242-alkalinity-soilless",
           "ferrarezi-2023-chlorine-phytotoxicity-rex-lettuce",
           "date-2005-chloramines-lettuce-hydroponic",
           "sutton-2006-pythium-hydroponic-etiology",
           "fao-dissolved-oxygen-temperature"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

SECTIONS.append({"id": "intro", "kicker": "What this is",
  "title": "Your water is the first ingredient, not a blank slate",
  "blocks": [
    lead("Every feed you give a cannabis plant starts with water, and that water is almost never "
         "pure. Tap, well, and rainwater all arrive carrying dissolved minerals, gases, and "
         "treatment chemicals that change pH, take up room in your nutrient recipe, and can harm "
         "roots or beneficial microbes before you add a single drop of fertiliser."),
    p("The plant never tastes your nutrients in isolation. It tastes water plus minerals plus "
      "nutrients combined. That is why two growers using the identical feed chart can get opposite "
      "results purely because of source-water differences. You cannot manage what you have not "
      "measured, so a water test comes before any nutrient decision."),
    figure(L.flow("From the tap to the root",
            [("Source water", "tap, well or rain"), ("Dissolved load", "minerals, gases, chlorine"),
             ("Mixing", "pH adjust, nutrients added"), ("Root zone", "what the plant drinks")],
            note="The first box is fixed until you treat it. Everything downstream inherits it."), 1,
      "Your source water and its dissolved load are the starting point. Mixing only adds to what is "
      "already there, so a problem in the first box follows the water all the way to the root."),
    callout("note", "What this paper does",
      p("It walks an absolute beginner from understanding what is in their source water, to testing "
        "it, to deciding whether reverse osmosis is worth the cost. Pairs with the "
        "<a href='ph-management.html'>pH management</a> and "
        "<a href='nutrient-mixing-athena.html'>nutrient mixing</a> papers.")),
  ]})

SECTIONS.append({"id": "key-terms", "kicker": "Key terms",
  "title": "The vocabulary, in plain words",
  "blocks": [
    p("Water-quality talk is full of jargon that hides simple ideas. Get the gist of these and the "
      "rest of the paper reads easily. The big one to grasp early: alkalinity is not the same thing "
      "as pH."),
    defterm("EC (electrical conductivity)", "How well water conducts electricity, which rises with "
            "dissolved salts. Measured in mS/cm or uS/cm. Higher EC means more dissolved stuff."),
    defterm("PPM / TDS (parts per million / total dissolved solids)", "The same idea as EC but "
            "expressed as a weight. Note that PPM pens use a conversion factor (a 500 or 700 scale), "
            "so two meters can disagree on the same water."),
    defterm("pH", "Acidity on a 0-14 scale. Most cannabis nutrient uptake targets pH 5.8-6.2 in "
            "hydro and coco, and 6.2-6.8 in soil."),
    defterm("Alkalinity", "The water's buffering capacity from carbonates and bicarbonates, reported "
            "as ppm CaCO3. High alkalinity pushes root-zone pH up over time even after you pH-down "
            "the tank. This is a different thing from pH itself."),
    defterm("Hardness", "Dissolved calcium and magnesium, reported as ppm CaCO3 or grains per gallon "
            "(1 GPG = 17.1 mg/L)."),
    defterm("RO (reverse osmosis)", "Filtration that forces water through a membrane and strips most "
            "dissolved minerals, leaving near-zero PPM water."),
    figure(L.flow("pH is a snapshot, alkalinity is a spring",
            [("pH now", "a single reading right now"), ("You pH-down", "tank drops to 5.8"),
             ("Alkalinity resists", "carbonates fight back"), ("pH creeps up", "back toward 6.8+")],
            note="pH tells you where you are. Alkalinity tells you how hard the water fights to go back."), 2,
      "pH is where the water sits at this moment. Alkalinity is the buffer that drags it back up "
      "afterwards, which is why a perfect tank reading can still drift in the root zone." + _c("umass-water-quality-ph-alkalinity")),
  ]})

SECTIONS.append({"id": "source-types", "kicker": "The core: where it comes from",
  "title": "Tap, well, and rain: three very different starting points",
  "blocks": [
    p("Municipal tap water is treated and consistent but carries chlorine or chloramine and often "
      "moderate-to-high mineral content, sometimes 150-300+ ppm straight from the faucet" + _c("umass-water-quality-ph-alkalinity") +
      ". Well water is the wild card: it can be very hard, high in iron, manganese, or sulfur, and "
      "it varies seasonally, so it must be tested. Rainwater is naturally low in dissolved minerals "
      "but offers little buffering and can pick up roof and storage contaminants."),
    figure(L.bars("Typical starting TDS by source",
            [("RO", 5), ("Rainwater", 15), ("Soft tap", 90), ("Hard tap", 280), ("Well", 350)],
            unit="", note="Approximate ppm before any nutrients. Well water is highly variable (50-600+).",
            maxv=600), 3,
      "Where your water starts on the PPM scale. RO and rain arrive near zero, soft tap is workable, "
      "and hard tap or well water can eat most of your nutrient headroom before you begin." + _c("umass-water-quality-ph-alkalinity")),
    p("Headroom is the point beginners miss. A working feed strength is commonly capped near "
      "800-900 ppm, so hard tap water at 300+ ppm leaves almost no room before you hit that "
      "ceiling" + _c("bevan-2021-npk-flowering-cannabis") + ". Rainwater typically arrives at only "
      "0-20 ppm, which is closer to RO, but it brings little to no buffering and a risk of pathogens, "
      "roofing contaminants, or sodium near coasts."),
    callout("tip", "Match the source to the habit",
      ul(["<strong>Tap:</strong> consistent and convenient, but expect chlorine or chloramine and a starting EC that eats into your nutrient room.",
          "<strong>Well:</strong> free and unmetered, but composition swings. Test at least twice a year and after heavy rain.",
          "<strong>Rain:</strong> low starting PPM like RO, but low buffering. Filter it and watch for sodium and contaminants."], "tight")),
  ]})

SECTIONS.append({"id": "alkalinity-carbonates", "kicker": "The core: the hidden pH driver",
  "title": "Alkalinity and carbonates: why your pH won't stay put",
  "blocks": [
    p("Alkalinity is the single most misunderstood water parameter for beginners. It is caused by "
      "dissolved carbonates and bicarbonates, and it acts like a chemical spring that drags root-zone "
      "pH back upward even after you adjust the tank to 5.8. A common acceptable range for container "
      "cannabis is roughly 40-100 ppm CaCO3, with many growers targeting 30-60 ppm as an "
      "optimum" + _c("fisher-purdue-ho242-alkalinity-soilless") + ". The conversions to know: "
      "1 meq/L equals 50 ppm CaCO3 equals 61 ppm bicarbonate" + _c("umass-water-quality-ph-alkalinity") + "."),
    figure(L.line("High alkalinity drags root-zone pH back up",
            [(0, 5.8), (1, 6.1), (2, 6.4), (3, 6.7), (4, 6.9), (5, 7.0)],
            ["day 0", "day 1", "day 2", "day 3", "day 4", "day 5"],
            ylab="root-zone pH", ymin=5.4, ymax=7.4,
            note="You pH the tank to 5.8, but high-alkalinity water climbs back over days."), 4,
      "A high-alkalinity water that you pH-down to 5.8 climbs back to 6.8+ within days. A corrected or "
      "naturally low-alkalinity water holds near 5.8-6.0 instead." + _c("fisher-purdue-ho242-alkalinity-soilless")),
    p("Above roughly 100-150 ppm CaCO3, alkalinity steadily raises substrate pH and locks out iron, "
      "manganese, and other micronutrients" + _c("umass-water-quality-ph-alkalinity") + ". You "
      "correct excess alkalinity by adding acid, such as phosphoric, nitric, or citric, to neutralise "
      "the carbonates, not just to hit a pH number once. At the other extreme, very low alkalinity "
      "(RO, rain) means almost no buffer, so pH swings fast and small acid or base errors matter more."),
    figure(L.zones("Alkalinity bands (ppm CaCO3)", 0, 200,
            [(0, 30, L.AMBL, "too low / no buffer"), (30, 100, L.GL, "ideal"),
             (100, 150, L.AMBL, "borderline"), (150, 200, L.REDL, "problematic")],
            unit="", note="Most container cannabis sits happiest in the 30-100 ppm band."), 5,
      "The workable window. Below 30 ppm you lose your buffer, the 30-100 ppm band is comfortable, "
      "and above 150 ppm you fight rising pH and micronutrient lockout." + _c("fisher-purdue-ho242-alkalinity-soilless")),
  ]})

SECTIONS.append({"id": "chlorine-hardness", "kicker": "The core: chemicals and minerals",
  "title": "Chlorine, chloramine, and hardness: what helps and what harms",
  "blocks": [
    p("Municipalities disinfect with chlorine or the more stable chloramine, and both can damage "
      "root tips and beneficial microbes. Root-tip injury has been reported at chlorine "
      "concentrations as low as 0.4 ppm" + _c("ferrarezi-2023-chlorine-phytotoxicity-rex-lettuce") +
      ", which matters most for living-soil and microbe-driven growers. Chlorine off-gasses if water "
      "sits and aerates for about 24 hours, but chloramine does not, and removing it requires a "
      "catalytic carbon filter or RO" + _c("date-2005-chloramines-lettuce-hydroponic") + "."),
    figure(L.flow("Chlorine off-gasses, chloramine does not",
            [("Fill tank", "from the tap"), ("Aerate 24h", "chlorine gasses off"),
             ("Carbon filter", "needed for chloramine"), ("Safe to feed", "no disinfectant left")],
            note="Chlorine leaves overnight with aeration. Chloramine needs catalytic carbon or RO."), 6,
      "The removal path differs by chemical. Standing and aerating clears chlorine, but chloramine is "
      "stable and survives a night out, so it needs catalytic carbon or RO." + _c("date-2005-chloramines-lettuce-hydroponic")),
    table(["", "Stable in standing water", "Removed by 24h aeration", "Removed by carbon", "Removed by RO"], [
      ["<strong>Chlorine</strong>", "No", "Yes", "Yes", "Yes"],
      ["<strong>Chloramine</strong>", "Yes", "No", "Catalytic carbon only", "Yes"],
    ], cls="compact", caption="Chlorine off-gasses overnight. Chloramine is stable and needs a catalytic carbon filter or RO."),
    p("Hardness is the one part of your starting water that is genuinely useful. It is dissolved "
      "calcium and magnesium, and cannabis needs both" + _c("kpai-2024-mineral-nutrition-vegetative-cannabis") +
      ". The catch: in hard water those minerals usually ride along with high alkalinity, so the "
      "helpful Ca and Mg arrive locked up with the carbonates that cause pH problems. Soft water at "
      "under 1 GPG (about 17 ppm) can be low in Ca and Mg and need a CalMag supplement regardless of "
      "whether you run RO."),
    table(["Class", "Hardness", "Cannabis-relevant note"], [
      ["Soft", "<1 GPG / <17 mg/L", "May be low in Ca/Mg, add CalMag"],
      ["Slightly hard", "1-3.5 GPG", "Usually fine, check alkalinity"],
      ["Moderately hard", "3.5-7 GPG", "Watch alkalinity creeping up"],
      ["Hard", "7-10.5 GPG", "Ca/Mg useful but alkalinity likely high"],
      ["Very hard", ">10.5 GPG / >180 mg/L", "Expect lockout and pH problems, consider RO"],
    ], cls="compact", caption="Hardness classes. Helpful minerals at the soft end, pH trouble at the hard end."),
  ]})

SECTIONS.append({"id": "ro-buildback", "kicker": "The core: the RO decision",
  "title": "Why growers use RO, build back, and when you actually need it",
  "blocks": [
    p("Reverse osmosis strips water to near-zero PPM, typically 0-10 ppm TDS, giving a blank canvas "
      "so every mineral the plant gets is one you chose" + _c("umass-water-quality-ph-alkalinity") +
      ". Because RO removes calcium and magnesium too, you must build back. That usually means adding "
      "a CalMag supplement plus your base nutrients to reach a target of roughly 100-200 ppm with "
      "good Ca and Mg before the rest of the feed" + _c("kpai-2024-mineral-nutrition-vegetative-cannabis") + "."),
    figure(L.flow("RO strips the water, then you build it back",
            [("Tap or well", "mixed ions, alkalinity"), ("RO membrane", "stripped to ~0 ppm"),
             ("Add CalMag", "Ca and Mg back in"), ("Base nutrients", "up to target EC")],
            note="Never feed plain RO. It has no Ca/Mg and no buffer."), 7,
      "RO gives you a clean slate, but a clean slate is not a feed. Build back CalMag first, then base "
      "nutrients, so the plant gets the minerals it needs and a working buffer." + _c("kpai-2024-mineral-nutrition-vegetative-cannabis")),
    figure(L.flow("Does this water need RO?",
            [("Water test", "get real numbers"), ("Any red flag?", "high alk, Na, chloramine, EC"),
             ("Yes -> RO", "then build back"), ("No -> tap", "dechlorinate + adjust")],
            note="One clear red flag is usually enough to justify RO."), 8,
      "A simple decision path. RO is recommended when alkalinity is high, sodium is elevated, "
      "chloramine is present, or starting EC is high. Otherwise clean tap is usually fine." + _c("umass-water-quality-ph-alkalinity")),
    callout("key", "When RO is worth it, and when it is not",
      ul(["<strong>Worth it when:</strong> starting EC is high, sodium is elevated, alkalinity is high, or chloramine is present.",
          "<strong>Often skippable when:</strong> tap is soft, low-alkalinity, chlorine-only (off-gassable), and under about 150 ppm.",
          "<strong>The cost:</strong> a wastewater ratio of often 1-4 gallons wasted per gallon made, membrane replacement, and a slower fill rate."], "tight")),
  ]})

SECTIONS.append({"id": "testing-stepbystep", "kicker": "Practical: test and treat",
  "title": "Testing your source water, step by step",
  "blocks": [
    p("Before buying any equipment, get real numbers for your water. A cheap EC/PPM pen and pH pen "
      "tell you starting strength and acidity in seconds, but they will not reveal alkalinity, "
      "sodium, or specific minerals. For that, send a sample to a lab or read your municipal water "
      "report, which lists EC/TDS, pH, alkalinity, calcium, magnesium, sodium, chloride, and any "
      "chlorine or chloramine note."),
    figure(L.bars("Read these off your water report",
            [("EC/TDS", 90), ("pH", 50), ("Alkalinity", 80), ("Ca", 60), ("Mg", 30), ("Na", 25)],
            unit="", note="Illustrative values only. Your report's numbers are what decide treatment.",
            maxv=110), 9,
      "The parameters worth pulling off a lab test or city report. EC and pH are quick pen readings, "
      "but alkalinity, sodium and the individual minerals only come from a fuller test."),
    steps([
      ("Buy and calibrate pens", "Get an EC/PPM pen and a pH pen first. Calibrate with fresh calibration solution, never with tap water."),
      ("Get the full picture", "For alkalinity, sodium, Ca, Mg and micronutrients, use a lab test or your city's annual water-quality report."),
      ("Record starting EC", "Note how much room you have before the ~800-900 ppm feed ceiling, so you know your nutrient headroom."),
      ("Mix in the right order", "Fill water, let chlorine off-gas or filter it, add CalMag if RO or soft, add base nutrients, then adjust pH last."),
      ("Re-test seasonally", "Re-check well and rain sources through the year. Municipal supplies can also switch chlorine to chloramine periodically."),
    ]),
    figure(L.flow("Correct mixing order",
            [("Fill + dechlorinate", "off-gas or filter"), ("CalMag", "if RO or soft"),
             ("Base nutrients", "to target EC"), ("pH adjust last", "verify EC and pH")],
            note="pH always goes last, after every nutrient is in the tank."), 10,
      "Order matters because each addition shifts pH. Adjust pH last, once the full recipe is mixed, "
      "then verify both EC and pH before you feed." + _c("bevan-2021-npk-flowering-cannabis")),
  ]})

SECTIONS.append({"id": "temperature-pitfalls", "kicker": "Troubleshooting and pitfalls",
  "title": "Water temperature and the mistakes beginners make",
  "blocks": [
    p("Water temperature quietly controls dissolved oxygen and disease risk. Aim for roughly "
      "18-22 C (65-72 F), because dissolved oxygen falls from about 5-6 ppm at 20 C to only 3-4 ppm "
      "at 26 C" + _c("fao-dissolved-oxygen-temperature") + ", and root pathogens like Pythium "
      "accelerate above about 23 C" + _c("sutton-2006-pythium-hydroponic-etiology") + ". Warm water "
      "plus low oxygen is an open invitation to root rot."),
    figure(L.line("Warmer water holds less oxygen",
            [(0, 6.0), (1, 5.5), (2, 5.0), (3, 4.4), (4, 3.8), (5, 3.4)],
            ["16 C", "18 C", "20 C", "22 C", "24 C", "26 C"],
            ylab="dissolved O2 ppm", ymin=2, ymax=7,
            note="Dissolved oxygen drops as water warms. The 18-22 C band is the safe target.",
            bands=[(4.8, 6.5, L.GL, "target O2")]), 11,
      "Dissolved oxygen declines steadily as water warms, from about 5-6 ppm near 20 C down toward "
      "3-4 ppm at 26 C. Above roughly 23 C you also enter Pythium risk." + _c("fao-dissolved-oxygen-temperature") + _c("sutton-2006-pythium-hydroponic-etiology")),
    table(["Common mistake", "What actually happens, and the fix"], [
      ["Comparing PPM across meters", "A 500 vs 700 scale makes two pens disagree on the same water. Pick one scale and stick to it"],
      ["pH the tank, ignore alkalinity", "Root-zone pH creeps up within days. Correct the alkalinity, not just the one reading"],
      ["Feeding plain RO or rain", "Calcium and magnesium deficiency. Add CalMag before base nutrients"],
      ["Leaving chloramine to sit out", "Chloramine is stable and survives the night. Use catalytic carbon or RO"],
      ["Water too warm", "Low oxygen and root rot. Cool the reservoir to 18-22 C"],
    ], cls="compact", caption="The five beginner traps, and what to do instead."),
  ]})

SECTIONS.append({"id": "expectations", "kicker": "Realistic expectations",
  "title": "What good water gets you, and what it doesn't",
  "blocks": [
    p("Sorting out your water removes a whole category of mystery problems: stable pH, no chlorine "
      "damage, predictable feed strength. It will not fix bad genetics, poor light, or a broken "
      "nutrient schedule. Good water quality is a foundation, not a yield button. It prevents "
      "problems more than it boosts numbers."),
    figure(L.zones("Do you need RO?", 0, 3,
            [(0, 1, L.GL, "probably skip"), (1, 2, L.AMBL, "consider"), (2, 3, L.REDL, "strongly worth it")],
            unit="", note="Skip: soft, low-alk, chlorine-only, <150 ppm. Worth it: hard, high Na, high alkalinity, chloramine."), 12,
      "A plain-language verdict. Soft low-alkalinity tap usually needs no RO. Hard, high-sodium, "
      "high-alkalinity, or chloraminated water is where RO earns its cost."),
    callout("key", "The honest summary",
      ol(["<strong>Most home growers on clean, soft, low-alkalinity tap</strong> can succeed with simple dechlorination and pH control, and never need RO.",
          "<strong>RO matters most</strong> for very hard, high-sodium, or high-alkalinity sources, for chloramine, and for precision hydro.",
          "<strong>You still manage pH, EC, temperature and CalMag</strong> regardless of which water source you choose."])),
    p("Spend on a water test first, and let the numbers, not marketing, decide whether RO is worth "
      "it. Then take your clean starting water into the "
      "<a href='ph-management.html'>pH management</a> and "
      "<a href='nutrient-mixing-athena.html'>nutrient mixing</a> papers to build the rest of the feed."),
  ]})
