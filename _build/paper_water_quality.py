# -*- coding: utf-8 -*-
"""Paper: source water, RO and alkalinity for cannabis (beginner)."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        stagecard, grid, card, chip, kv, steps)
import figs_lib as L

SLUG = "water-quality"
TITLE = "Testing and treatment of source water for cannabis"
EYEBROW = "Feed · Water"
SUB = ("This paper shows the dissolved materials in tap water, well water and rainwater, before you "
       "add nutrients. It gives information about EC, alkalinity, carbonates, chlorine, chloramine "
       "and hardness. After you read this paper, you will know how to read a water report. You will "
       "also know how to find if the cost of reverse osmosis is correct for your water. You will "
       "know how to use the data about your source water when you calculate the nutrients.")
META = [("droplet", "Basic"), ("image", "13 diagrams"),
        ("quote", "6 sources"), ("clock", "~14 min to read")]
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

SECTIONS.append({"id": "intro", "kicker": "About this paper",
  "title": "Purpose and scope",
  "blocks": [
    lead("Each feed that you give to a cannabis plant starts with water, and this water almost "
         "always has other materials in it. Tap water, well water and rainwater all contain "
         "dissolved minerals, gases and chemical materials from the treatment. These materials "
         "change the pH and use part of the EC that is available for your nutrients. They can also "
         "cause damage to the roots or to beneficial microbes, before you add fertilizer."),
    p("The plant does not use only your nutrients. It uses the water, the minerals and the "
      "nutrients together. Thus two growers who use the same feed chart can get opposite results, "
      "only because their source water is different. You cannot control a value that you do not "
      "measure. Do a water test before each decision about nutrients."),
    figure(L.flow("From the tap to the root",
            [("Source water", "tap, well or rainwater"), ("Dissolved load", "minerals, gases, chlorine"),
             ("Mixing", "adjust the pH, add nutrients"), ("Root zone", "water for the plant")],
            note="Source water does not change until you apply a treatment. The next steps use this water."), 1,
      "Your source water and its dissolved load are the start point. The mixing only adds to the "
      "materials that are in the water. Thus a problem in the source water stays in the water to "
      "the root."),
    callout("note", "How this paper helps you",
      p("This paper shows a new grower how to find the materials in the source water. It also shows "
        "how to do a test of the water, and how to find if the cost of reverse osmosis is correct. "
        "You can use this paper with the <a href='ph-management.html'>pH management</a> and <a "
        "href='nutrient-mixing-athena.html'>nutrient mixing</a> papers.")),
  ]})

SECTIONS.append({"id": "key-terms", "kicker": "The terms",
  "title": "Definitions",
  "blocks": [
    p("The facts about water quality are easy to know, but the terms are not easy. When you know "
      "these terms, the remaining sections of this paper are easy to read. One fact is very "
      "important: alkalinity is not the same as pH."),
    defterm("EC (electrical conductivity)", "Dissolved minerals have a small electric charge. Thus "
            "a measurement of how well electricity flows through the water gives approximately the "
            "quantity of dissolved minerals in it. EC is this reading. You give EC in mS/cm or "
            "µS/cm. A higher EC shows that there is more dissolved material in the water."),
    defterm("PPM / TDS (parts per million / total dissolved solids)", "PPM is an estimate of the "
            "weight for each liter. You calculate it from the EC with a set conversion factor. PPM "
            "pens use the 500 scale or the 700 scale. Thus two meters on the same water can give "
            "different readings. Select one scale and use only this scale."),
    defterm("pH", "The acidity of the water, on a scale of 0 to 14. For the uptake of nutrients, "
            "the target pH for cannabis is usually 5.8 to 6.2 in hydroponics and coco, and 6.2 to "
            "6.8 in soil."),
    defterm("Alkalinity", "Alkalinity is the buffering capacity of the carbonates in the water, in "
            "ppm CaCO3. After you add acid to get a pH of 5.8, the dissolved carbonates slowly "
            "neutralize the acid. Thus the pH increases again in hours to days. Alkalinity is a "
            "different quantity from pH. If the alkalinity is high, the water neutralizes the acid "
            "that you add, also when the initial reading is correct."),
    defterm("Hardness", "The quantity of calcium and magnesium dissolved in the water. You give it "
            "in ppm CaCO3. A different unit is grains for each gallon (GPG): 1 GPG is 17.1 mg/L."),
    defterm("RO (reverse osmosis)", "Filtration in which you push water through a membrane. The "
            "membrane removes most of the dissolved minerals, and the water then has almost zero "
            "PPM."),
    figure(L.flow("pH is one reading, alkalinity is a buffer",
            [("pH reading", "one reading at this time"), ("Add acid", "pH decreases to 5.8"),
             ("Alkalinity buffer", "carbonates neutralize acid"), ("pH increases", "to 6.8+ again")],
            note="pH shows the value at one time. Alkalinity shows how strongly the pH increases again."), 2,
      "The pH is the value of the water at one time. The alkalinity is the buffer of carbonates "
      "that makes the pH increase again after this. Thus a reading in the tank that is correct can "
      "change in the root zone." + _c("umass-water-quality-ph-alkalinity")),
  ]})

SECTIONS.append({"id": "source-types", "kicker": "Primary information: the source of the water",
  "title": "Water source types",
  "blocks": [
    p("A supplier applies a treatment to tap water, and the quality of the water is stable. But the "
      "water contains chlorine or chloramine. It frequently has a moderate or high content of "
      "minerals. The content can be 150 to 300 ppm or more directly from the tap." +
      _c("umass-water-quality-ph-alkalinity") + " Well water can have a very high hardness, and it "
      "can have a high content of iron, manganese or sulfur. It changes with the seasons, thus you "
      "must do a test of the water.</p><p>Rainwater has a low content of dissolved minerals. But it "
      "has a low buffering capacity, and it can collect contaminants from the roof and from the "
      "storage."),
    figure(L.bars("Typical start TDS of each source",
            [("RO", 5), ("Rainwater", 15), ("Soft tap water", 90), ("Hard tap water", 280), ("Well water", 350)],
            unit="", note="Approximate ppm before nutrients. The range for well water is very large (50-600+).",
            maxv=600), 3,
      "The start value of your water on the PPM scale. RO water and rainwater have a value near "
      "zero. You can use soft tap water. Hard tap water or well water gives part of the EC of the "
      "completed feed." + _c("umass-water-quality-ph-alkalinity")),
    p("The start EC gives part of the EC of the completed feed. But a display of 300 ppm TDS does "
      "not show the ion balance or the alkalinity of the water. It also does not show that you "
      "cannot use the water. Measure the source EC, the alkalinity, the sodium, the chloride, the "
      "calcium and the magnesium. Then include the nutrients in the water that the plant can use as "
      "part of the feed. The Bevan test gives the ranges for the effect of NPK on each crop, and "
      "not a limit for source water." + _c("bevan-2021-npk-flowering-cannabis") +
      _c("umass-water-quality-ph-alkalinity") + "</p><p>Rainwater usually has only 0 to 20 ppm, "
      "which is near the value of RO water. But it has a low buffering capacity or no buffering "
      "capacity. There is also a risk of pathogens, contaminants from the roof, or sodium near the "
      "coast."),
    callout("tip", "Select the source for your method",
      ul(["<strong>Tap water:</strong> its quality is stable and it is easy to use, but it contains chlorine or chloramine. The start EC uses part of the EC that is available for your nutrients.",
          "<strong>Well water:</strong> there is no cost for the water and no meter, but the minerals in the water change much. Do a test of the water a minimum of two times each year, and after a large quantity of rain.",
          "<strong>Rainwater:</strong> the start PPM is low, the same as RO, but the buffering is low. Filter the water and monitor the sodium and the contaminants."], "tight")),
  ]})

SECTIONS.append({"id": "alkalinity-carbonates", "kicker": "Primary information: a cause of pH change that you cannot see",
  "title": "Alkalinity and carbonate buffering",
  "blocks": [
    p("Alkalinity is a parameter of the water. New growers frequently have incorrect information "
      "about it. Dissolved carbonates and bicarbonates cause alkalinity. Alkalinity makes the pH of "
      "the root zone increase again, also after you decrease the pH of the tank to 5.8. For "
      "cannabis in containers, a usual satisfactory range is approximately 40 to 100 ppm CaCO3, and "
      "many growers use 30 to 60 ppm as the best target." +
      _c("fisher-purdue-ho242-alkalinity-soilless") + " Use these conversions: 1 meq/L is equal to "
      "50 ppm CaCO3 and to 61 ppm bicarbonate." + _c("umass-water-quality-ph-alkalinity")),
    figure(L.line("High alkalinity makes the root-zone pH increase",
            [(0, 5.8), (1, 6.1), (2, 6.4), (3, 6.7), (4, 6.9), (5, 7.0)],
            ["day 0", "day 1", "day 2", "day 3", "day 4", "day 5"],
            ylab="root-zone pH", ymin=5.4, ymax=7.4,
            note="You decrease the tank pH to 5.8. High alkalinity increases the pH again in days."), 4,
      "If water has high alkalinity and you decrease its pH to 5.8, the pH increases again to 6.8+ "
      "in days. If the alkalinity is low from the start, or you correct it, the pH stays near 5.8 "
      "to 6.0." + _c("fisher-purdue-ho242-alkalinity-soilless")),
    p("If the alkalinity is more than approximately 100 to 150 ppm CaCO3, it continuously increases "
      "the pH of the substrate. It also causes lockout of iron, manganese and other micronutrients." +
      _c("umass-water-quality-ph-alkalinity") + " To correct a high alkalinity, add acid to "
      "neutralize the carbonates. Examples of acid are phosphoric acid, nitric acid and citric "
      "acid. Do not add acid only to get a correct pH reading one time.</p><p>If the alkalinity is "
      "very low (RO water, rainwater), there is almost no buffer. Thus the pH changes quickly, and "
      "small errors in the quantity of acid or base have more effect."),
    figure(L.zones("Alkalinity ranges (ppm CaCO3)", 0, 200,
            [(0, 30, L.AMBL, "too low, no buffer"), (30, 100, L.GL, "best"),
             (100, 150, L.AMBL, "near the limit"), (150, 200, L.REDL, "problem")],
            unit="", note="For most cannabis in containers, the best range is 30-100 ppm."), 5,
      "The range that you can use. If the alkalinity is less than 30 ppm, the buffer is low. The "
      "range of 30 to 100 ppm is correct. If the alkalinity is more than 150 ppm, the pH increases "
      "and there is lockout of micronutrients." + _c("fisher-purdue-ho242-alkalinity-soilless")),
  ]})

SECTIONS.append({"id": "chlorine-hardness", "kicker": "Primary information: chemical materials and minerals",
  "title": "Chlorine, chloramine and hardness",
  "blocks": [
    p("Suppliers of tap water disinfect the water with chlorine or with chloramine, which is more "
      "stable. Chlorine and chloramine can cause damage to the root tips and to beneficial "
      "microbes. A report shows damage to the root tips at a chlorine concentration of only 0.4 ppm." +
      _c("ferrarezi-2023-chlorine-phytotoxicity-rex-lettuce") + " This damage is most important for "
      "growers who use living soil or other systems with microbes.</p><p>Chlorine moves out of the "
      "water as a gas if you keep the water in a container with aeration for approximately 24 "
      "hours. Chloramine does not move out of the water as a gas. To remove chloramine, you must "
      "use a catalytic carbon filter or RO." + _c("date-2005-chloramines-lettuce-hydroponic")),
    figure(L.flow("Chlorine moves out as gas, chloramine does not",
            [("Fill tank", "from the tap"), ("Aeration 24h", "chlorine moves out"),
             ("Carbon filter", "necessary for chloramine"), ("Safe as feed", "no disinfectant stays")],
            note="Aeration removes chlorine in one night. Use catalytic carbon or RO for chloramine."), 6,
      "Each disinfectant has a different removal procedure. If you keep the water in a container "
      "with aeration, the chlorine moves out of the water. Chloramine is stable and stays in the "
      "water after one night. Thus you must use catalytic carbon or RO." +
      _c("date-2005-chloramines-lettuce-hydroponic")),
    table(["", "Stays in water in a container", "Aeration for 24h removes it", "Carbon removes it", "RO removes it"], [
      ["<strong>Chlorine</strong>", "No", "Yes", "Yes", "Yes"],
      ["<strong>Chloramine</strong>", "Yes", "No", "Catalytic carbon only", "Yes"],
    ], cls="compact", caption="Chlorine moves out of the water in one night. Chloramine is stable. To remove chloramine, use a catalytic carbon filter or RO."),
    p("Hardness is the only part of your source water that helps the plant. Hardness is the "
      "quantity of calcium and magnesium in solution, and cannabis must have these two minerals." +
      _c("kpai-2024-mineral-nutrition-vegetative-cannabis") + " But in hard water, these minerals "
      "usually occur with a high alkalinity. Thus the Ca and Mg that help the plant are in the "
      "water with the carbonates that cause problems with the pH. Soft water, with less than 17 "
      "mg/L (1 GPG), can have a low quantity of Ca and Mg. A CalMag supplement can be necessary, "
      "with or without RO."),
    table(["Type", "Hardness", "Information for cannabis"], [
      ["Soft water", "Less than 17 mg/L (less than 1 GPG)", "The Ca and Mg can be low. Add CalMag."],
      ["Slightly hard water", "17 to 60 mg/L (1 to 3.5 GPG)", "Usually correct. Measure the alkalinity."],
      ["Moderately hard water", "60 to 120 mg/L (3.5 to 7 GPG)", "Monitor the alkalinity, because it can increase."],
      ["Hard water", "120 to 180 mg/L (7 to 10.5 GPG)", "The Ca and Mg help the plant, but it is possible that the alkalinity is high."],
      ["Very hard water", "More than 180 mg/L (more than 10.5 GPG)", "Lockout and pH problems occur frequently. Find if RO is necessary."],
    ], cls="compact", caption="Types of hardness. The minerals help the plant when the hardness is low, and pH problems occur when the hardness is high."),
  ]})

SECTIONS.append({"id": "ro-buildback", "kicker": "Primary information: the decision on RO",
  "title": "Reverse osmosis and the minerals that you add",
  "blocks": [
    p("Reverse osmosis removes the minerals from water. The water then has almost zero PPM, usually "
      "0 to 10 ppm TDS. Thus each mineral that the plant gets is a mineral that you select." +
      _c("umass-water-quality-ph-alkalinity") + "</p><p>RO also removes calcium and magnesium. Thus "
      "you must do the build back. In the build back, you add minerals to the water again. For the "
      "build back, you usually add a CalMag supplement and your base nutrients. The target is "
      "approximately 100 to 200 ppm, with sufficient Ca and Mg before the other nutrients of the "
      "feed." + _c("kpai-2024-mineral-nutrition-vegetative-cannabis")),
    figure(L.flow("RO removes the minerals, then you add them again",
            [("Tap or well", "mixed ions, alkalinity"), ("RO membrane", "approximately 0 ppm"),
             ("Add CalMag", "Ca and Mg increase"), ("Base nutrients", "until target EC")],
            note="Do not apply only RO water. It has no Ca, Mg or buffer."), 7,
      "RO water has almost no minerals, but this water is not a feed. Do the build back: add CalMag "
      "first and then the base nutrients. Thus the plant gets the minerals that it must have, and a "
      "buffer that operates correctly." + _c("kpai-2024-mineral-nutrition-vegetative-cannabis")),
    figure(L.flow("Is RO necessary?",
            [("Water test", "get correct data"), ("High values?", "alkalinity, Na, chloramine, EC"),
             ("Yes: use RO", "then add CalMag"), ("No: tap water", "remove chlorine and adjust")],
            note="One high value is usually sufficient for RO."), 8,
      "A short decision procedure. We recommend RO if the alkalinity is high, the sodium is high, "
      "chloramine is in the water, or the start EC is high. If none of these conditions occurs, "
      "clean tap water is usually correct." + _c("umass-water-quality-ph-alkalinity")),
    callout("key", "When to use RO and when not to use RO",
      ul(["<strong>Use RO if:</strong> the start EC, the sodium or the alkalinity is high, or chloramine is in the water.",
          "<strong>RO is frequently not necessary if:</strong> the tap water has a low hardness and a low alkalinity, and it has less than approximately 150 ppm. The water has only chlorine, which moves out of the water as a gas.",
          "<strong>The cost:</strong> the ratio of waste water is frequently 1 to 4 gallons for each gallon of RO water that you make. You must also replace the membrane, and the fill rate is lower."], "tight")),
  ]})

SECTIONS.append({"id": "testing-stepbystep", "kicker": "Procedure: tests and treatment",
  "title": "Source-water testing",
  "blocks": [
    p("Before you get equipment, get correct data for your water. A low-cost EC/PPM pen and a pH "
      "pen give the start strength and the acidity quickly. But they do not show the alkalinity, "
      "the sodium, or the quantity of each mineral. For this, send a sample to a lab, or read the "
      "water report from the supplier of your tap water. The report has a list of EC/TDS, pH, "
      "alkalinity, calcium, magnesium, sodium, chloride, and information on chlorine or chloramine."),
    figure(L.bars("Values to read in your water report",
            [("EC/TDS", 90), ("pH", 50), ("Alkalinity", 80), ("Ca", 60), ("Mg", 30), ("Na", 25)],
            unit="", note="These values are examples only. Use your report to select the treatment.",
            maxv=110), 9,
      "The figure shows the parameters to read in a lab test or in the report from the supplier. "
      "You get EC and pH quickly with pens. But you get the alkalinity, the sodium and the quantity "
      "of each mineral only from a test with more parameters."),
    steps([
      ("Get and calibrate pens", "First, get an EC/PPM pen and a pH pen. Calibrate the pens with new calibration solution. Do not use tap water for the calibration."),
      ("Get all the data", "For alkalinity, sodium, Ca, Mg and micronutrients, use a lab test or the water report of your supplier each year."),
      ("Record the start EC", "Record the part of your target EC that the source water uses. Thus you know the headroom for the nutrients. Set the targets in mS/cm and not in ppm."),
      ("Mix in the correct sequence", "Fill the tank with water. Let the chlorine move out of the water as a gas, or filter the water. If you use RO water or soft water, add CalMag. Add the base nutrients. Then adjust the pH last."),
      ("Do a test again in each season", "Do a test of well water and rainwater again during the year. A supplier of tap water can also change the disinfectant from chlorine to chloramine from time to time."),
    ]),
    figure(L.flow("Correct mixing sequence",
            [("Fill, remove chlorine", "aeration or filter"), ("CalMag", "RO or soft water"),
             ("Base nutrients", "to target EC"), ("Adjust pH last", "measure EC, pH")],
            note="Adjust the pH last, after all the nutrients are in the tank."), 10,
      "The sequence is important, because each material that you add changes the pH. Adjust the pH "
      "last, after you mix all the nutrients. Then measure the EC and the pH before you apply the "
      "feed." + _c("bevan-2021-npk-flowering-cannabis")),
  ]})

SECTIONS.append({"id": "temperature-pitfalls", "kicker": "When there is a problem",
  "title": "Water temperature and frequent errors",
  "blocks": [
    p("The temperature of the water controls the dissolved oxygen and the risk of disease. We "
      "recommend that you keep the water at approximately 18 to 22 °C (65 to 72 °F). In this range, "
      "the saturation dissolved oxygen decreases only slowly, from approximately 9 mg/L at 20 °C to "
      "approximately 8 mg/L at 26 °C." + _c("fao-dissolved-oxygen-temperature") +
      " But warm water with low aeration also increases the risk of pathogens. Root pathogens, for "
      "example Pythium, increase in number more quickly at more than approximately 23 °C." +
      _c("sutton-2006-pythium-hydroponic-etiology") + " Warm water with low oxygen can cause root "
      "rot."),
    figure(L.line("Higher temperature, less oxygen",
            [(0, 9.9), (1, 9.5), (2, 9.1), (3, 8.7), (4, 8.4), (5, 8.1)],
            ["16 C", "18 C", "20 C", "22 C", "24 C", "26 C"],
            ylab="saturation O2 mg/L", ymin=7, ymax=11,
            note="The saturation oxygen decreases only slowly in this range. The 18-22 C range is the safe target.",
            bands=[(8.7, 9.9, L.GL, "target O2")]), 11,
      "The saturation dissolved oxygen decreases slowly when the temperature of the water "
      "increases, from approximately 9 mg/L at 20 °C to approximately 8 mg/L at 26 °C. At more than "
      "approximately 23 °C, the larger risk is Pythium, and not a low quantity of oxygen." +
      _c("fao-dissolved-oxygen-temperature") + _c("sutton-2006-pythium-hydroponic-etiology")),
    table(["Frequent error", "Result and correction"], [
      ["You compare PPM readings from different meters", "A 500 scale and a 700 scale give different readings from two pens on the same water. Select one scale and use only this scale."],
      ["You adjust the pH of the tank, but you do not control the alkalinity", "The pH of the root zone increases again in days. Correct the alkalinity, and do not correct only one reading."],
      ["You apply only RO water or rainwater as feed", "Deficiency of calcium and magnesium. Add CalMag before the base nutrients."],
      ["You keep water with chloramine in a container to remove the chloramine", "Chloramine is stable and stays in the water after one night. Use catalytic carbon or RO."],
      ["The water is too warm", "Low oxygen and root rot. Decrease the temperature of the reservoir to 18 to 22 °C (65 to 72 °F)."],
    ], cls="compact", caption="Five frequent errors of new growers, and the corrections."),
  ]})

SECTIONS.append({"id": "expectations", "kicker": "Typical results",
  "title": "Expected results and limitations",
  "blocks": [
    p("If you correct your water, a large group of problems that are not easy to find does not "
      "occur. The pH is stable, there is no damage from chlorine, and you can calculate the "
      "strength of the feed. Correct water cannot correct genetics of low quality, not sufficient "
      "light, or an incorrect feed schedule. Good water quality gives a good start for the crop, "
      "but it does not increase the yield directly. It prevents problems more than it increases the "
      "results."),
    figure(L.zones("Is RO necessary?", 0, 3,
            [(0, 1, L.GL, "usually not necessary"), (1, 2, L.AMBL, "can be necessary"), (2, 3, L.REDL, "necessary")],
            unit="", note="No RO: soft water, low alkalinity, only chlorine, <150 ppm. RO: hard water, high Na, high alkalinity, chloramine."), 12,
      "A short summary. RO is usually not necessary for soft tap water with low alkalinity. For "
      "hard water, water with high sodium, water with high alkalinity, or water with chloramine, "
      "the cost of RO is correct."),
    callout("key", "The summary",
      ol(["<strong>Most growers who have clean, soft tap water with low alkalinity</strong> can get good results. They only remove the chlorine and control the pH. For them, RO is not necessary.",
          "<strong>RO is most important</strong> for sources with very hard water, high sodium or high alkalinity, for chloramine, and for precision hydroponics.",
          "<strong>You must also control the pH, the EC, the temperature and the CalMag</strong> for each source of water that you select."])),
    p("First, do a water test. Use the numbers to find if the cost of RO is correct. Do not use "
      "marketing to make this decision. Then use your clean source water with the <a "
      "href='ph-management.html'>pH management</a> and <a "
      "href='nutrient-mixing-athena.html'>nutrient mixing</a> papers to make the remaining parts of "
      "the feed."),
  ]})
