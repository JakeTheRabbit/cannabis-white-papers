# -*- coding: utf-8 -*-
"""Paper: the cannabis flower cycle, week by week (beginner)."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        stagecard, grid, card, chip, kv, steps)
import figs_lib as L

SLUG = "flowering-stages"
TITLE = "The flower cycle, one week at a time"
EYEBROW = "Basic · Flower"
SUB = ("This paper shows the eight to ten weeks from the flip (the change of the light cycle) to "
       "the harvest. You will know how to examine the plant in each stage, and how to set the "
       "correct climate and feed for each phase. You will also know how to use the trichomes, and "
       "not the calendar, to select the time to cut.")
META = [("leaf", "Basic"), ("image", "9 diagrams"),
        ("quote", "8 sources"), ("clock", "~12 min to read")]
RELATED = ["coco-crop-steering", "defoliation-training", "harvest-dry-trim-cure"]
REF_IDS = ["ahrens-2023-photoperiod-optimum", "spitzer-rimon-2019-florogenesis",
           "llewellyn-2022-light-intensity-yield", "eichhorn-bilodeau-2019-photobiology",
           "livingston-2020-trichome-maturation", "hesami-2023-morphological-lifecycle",
           "mahmoud-2023-botrytis-budrot", "ahrens-2023-photoperiod-lightleak-revert"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

SECTIONS.append({"id": "what-this-is", "kicker": "01 · Start here", "title": "Purpose and scope",
  "blocks": [
    lead("Cannabis has two large phases: vegetative growth and flowering. In vegetative growth, the "
         "plant makes leaves, stems and roots. In flowering, the plant makes the buds that you "
         "harvest. A change of the light cycle to 12 hours on and 12 hours off (the flip) starts "
         "flowering. For most plants, flowering continues for approximately 8 to 10 weeks. This "
         "paper shows these weeks one week at a time."),
    p("You can use this paper if you are a new grower. Flowering is the last phase. For typical "
      "hybrids, flowering continues for approximately 8 to 10 weeks. Indica types that are not "
      "hybrids can complete flowering in 7 to 8 weeks. Long sativa types can continue for 11 to 13 "
      "weeks." + _c("hesami-2023-morphological-lifecycle")),
    p("A photoperiod plant starts flowering only when the light cycle changes. An autoflower plant "
      "starts flowering because of its age. Thus this paper is about photoperiod plants.</p><p>The "
      "plant shows the stage that it is in. Thus you examine the plant (the pistils, the trichomes "
      "and the leaves) and not only the calendar. If the climate, the light and the feed are "
      "correct each week, the buds have a high density and a high potency. If the climate, the "
      "light or the feed is not correct, the buds can be loose, can have mold, or can have harsh "
      "smoke."),
    figure(L.flow("The two-phase lifecycle",
            [("Seed / clone", "start"), ("Vegetative", "18/6 light, make the structure"),
             ("Flip", "change to 12/12"), ("Flowering", "8-10 weeks, bud production"),
             ("Harvest", "cut after trichome check")]), 1,
      "Flowering is the last half of the cultivation. Before the flip, the plant makes its leaves, "
      "stems and roots. After the flip, the plant makes the buds." +
      _c("hesami-2023-morphological-lifecycle")),
    callout("note", "Who this paper is for",
      p("This paper is for a grower who will do the flip for the first photoperiod crop. The grower "
        "wants information for each week. Use this paper with the <a "
        "href='coco-crop-steering.html'>crop steering</a> paper and with the <a "
        "href='harvest-dry-trim-cure.html'>harvest and cure</a> paper.")),
  ]})

SECTIONS.append({"id": "key-terms", "kicker": "02 · Terms", "title": "Definitions",
  "blocks": [
    p("This paper uses six terms of growers many times. Make sure that you know these six terms. "
      "Then the other sections are easy to read. Each term is easy after the definition."),
    defterm("Flip / 12/12", "The change of the timer of the lights to 12 hours on and 12 hours off. "
            "The photoperiod plant uses the longer dark period as a signal that winter will start. "
            "As a result, flowering starts."),
    defterm("Pistils", "The small white hairs that extend from the bud sites. At the start, the "
            "pistils are white. During ripening, they become orange or brown."),
    defterm("Trichomes", "The small resin glands, each with a stalk and a head, that are on the "
            "buds and on the leaves near the buds. The color of a trichome shows the chemical "
            "maturity, and it is easy to examine the color with a 60&times; loupe or a small "
            "microscope. A transparent trichome shows that the compounds continue to increase in "
            "quantity. A milky (cloudy) trichome shows the peak quantity, and an amber trichome "
            "shows that degradation starts. The trichomes contain most of the THC, the CBD and the "
            "terpenes. Thus the trichomes are the accurate signal for the harvest, and the color of "
            "the pistils is only a first indication with low accuracy."),
    defterm("Calyx, bud and cola", "A calyx is one small part of the flower. A calyx has the shape "
            "of a drop. A bud is a group of many calyxes. A large group of buds on the primary stem "
            "is a cola."),
    defterm("EC and VPD", "EC (electrical conductivity) measures the strength of the nutrient "
            "solution and not the volume (more dissolved minerals in the water give a higher EC). "
            "For most of flowering, a drip EC from approximately 1.8 to 2.8&nbsp;mS&middot;cm&sup1; "
            "is correct (a lower EC causes a deficiency, and a higher EC causes nutrient burn). VPD "
            "(vapor pressure deficit) shows how much the air pulls the moisture from the leaves of "
            "the plant. When the air is dry and warm, the VPD is high, and the plant opens the "
            "stomata and uses water at a high rate (in cool air with high humidity, the VPD is "
            "low). VPD is one value in kPa for the temperature and the humidity together (thus you "
            "can adjust the work that the plant does to keep sufficient water). Cannabis makes the "
            "best flowers at a VPD from approximately 1.0 to 1.4&nbsp;kPa, and the value changes "
            "with the stage."),
    defterm("Defoliation and lollipopping", "Defoliation is the removal of leaves to increase the "
            "airflow and the light in the plant. Lollipopping is the removal of the growth from the "
            "lower third of the plant. As a result, the plant sends its energy to the top buds."),
    figure(L.flow("From calyx to cola",
            [("Calyx", "one flower part"), ("Bud", "many calyxes"),
             ("Cola", "group of buds on a stem"), ("Pistils", "white to orange hairs"),
             ("Trichomes", "transparent to milky to amber")]), 2,
      "The names in the figure are for the same flower at different sizes. The pistils and the "
      "trichomes are the two signals that you monitor to select the time to harvest."),
  ]})

SECTIONS.append({"id": "the-flip", "kicker": "03 · The mechanism", "title": "The effect of the 12/12 flip on the plant",
  "blocks": [
    p("Photoperiod cannabis measures the length of the dark period. The plant uses this length to "
      "find if the time of the year is spring (growth) or autumn (reproduction). When you give the "
      "plant 12 hours of continuous darkness, the plant uses this as a signal that the days become "
      "shorter. As a result, the plant changes to the production of flowers." +
      _c("spitzer-rimon-2019-florogenesis")),
    p("The dark period must have no light. Continuous darkness is necessary to start flowering and "
      "to keep flowering. A light leak in the 12-hour night can cause stress in the plant, also "
      "when the leak is small. The plant can start vegetative growth again, or the plant can make "
      "seeds (hermaphroditism)." + _c("eichhorn-bilodeau-2019-photobiology") +
      " An in vitro test shows that photoperiod plants start vegetative growth again when light "
      "comes into the dark period." + _c("ahrens-2023-photoperiod-lightleak-revert")),
    p("A dark period of twelve hours is the safe value to use. Investigations show that nights that "
      "are longer by a small value can also be correct for some cultivars." +
      _c("ahrens-2023-photoperiod-optimum") + " Most cultivars show the first pre-flower pistils in "
      "7 to 14 days after the flip. Do the flip when the plant is in good condition. The plant must "
      "have approximately half to two-thirds of the height that you want at the end of flowering. "
      "The plant will have a large stretch after the flip."),
    figure(L.zones("Day and night: vegetative cycle and flower cycle",
            0, 24, [(0, 18, L.GL, "18h light"), (18, 24, L.BLUL, "6h night"),
                    (0, 12, L.AMBL, "12h light"), (12, 24, L.PURL, "12h night, sealed")],
            unit="h",
            note="The flip is the change from the top cycle to the bottom cycle. The 12h night block must have no light leaks."), 3,
      "Vegetative growth has long days of light. Flowering has equal periods of light and darkness, "
      "and the dark period is the trigger. If light comes into the dark period, the plant can start "
      "vegetative growth again or make seeds." + _c("eichhorn-bilodeau-2019-photobiology")),
    callout("warn", "The dark period must have no light",
      p("Before you do the flip, put tape on the indicator lights and seal the room. In the dark "
        "period, light from chargers, timer LEDs or door gaps can start vegetative growth again. "
        "The light can also cause hermaphroditism.")),
  ]})

SECTIONS.append({"id": "stretch-bud-set", "kicker": "04 · Weeks 1 to 4", "title": "Stretch and bud set (weeks 1 to 4)",
  "blocks": [
    p("In the first 2 to 3 weeks after the flip, the plant increases in height (the stretch). The "
      "height frequently becomes almost two times larger. The plant makes the structure that holds "
      "the buds, and white pistils start to show at the nodes." +
      _c("hesami-2023-morphological-lifecycle")),
    p("At approximately weeks 3 to 4, the stretch stops. The pistil sites become small buds, and "
      "the calyxes start to be in groups. In this period, each bud gets its position. Thus the "
      "plant is most sensitive to the removal of leaves. If you remove many leaves, the yield "
      "decreases.</p><p>In weeks 1 to 2, the height of the plant can increase by 50 to 100%. Thus "
      "keep the PPFD at approximately 800–900&nbsp;&mu;mol&middot;m&sup2;&middot;s&sup1;. Apply "
      "feed with a moderate EC (drip EC of approximately 2.0 to 2.6), because the growth is fast." +
      _c("llewellyn-2022-light-intensity-yield")),
    figure(L.line("Plant height during the flower cycle",
            [(0, 100), (1, 135), (2, 175), (3, 195), (4, 200), (5, 201),
             (6, 202), (7, 202), (8, 202), (9, 202)],
            ["flip", "wk1", "wk2", "wk3", "wk4", "wk5", "wk6", "wk7", "wk8", "wk9"],
            ylab="height %", ymin=90, ymax=215,
            note="The height is maximum at approximately week 4. Almost all growth is in the first stretch."), 4,
      "The height increases at a high rate in weeks 1 to 3, and then it does not change. Do the "
      "flip when the plant has half to two-thirds of the height that you want. Thus the plant has "
      "space for the stretch." + _c("hesami-2023-morphological-lifecycle")),
    table(["Week", "Phase", "PPFD (µmol·m⁻²·s⁻¹)", "Day / night temperature", "RH", "VPD (kPa)", "Drip EC", "Task"], [
      ["1", "Stretch", "800–850", "26–28 °C (79–82 °F) / 22–24 °C (72–75 °F)", "65–70%", "0.9–1.0", "2.0–2.2", "Lollipopping and small defoliation"],
      ["2", "Stretch", "850–900", "26–28 °C (79–82 °F) / 22–24 °C (72–75 °F)", "62–68%", "1.0–1.1", "2.2–2.4", "Primary defoliation"],
      ["3", "Bud set", "900", "26–28 °C (79–82 °F) / 21–23 °C (70–73 °F)", "60–65%", "1.0–1.1", "2.4–2.6", "The last small defoliation. After this, do not defoliate."],
      ["4", "Bud set", "900", "26–28 °C (79–82 °F) / 21–23 °C (70–73 °F)", "58–62%", "1.1–1.2", "2.4–2.6", "Keep all values stable. Do not remove more leaves."],
    ], cls="compact", caption="Target values for weeks 1 to 4. At the start of flowering, keep the temperature and the humidity moderately high. Then decrease the humidity in small steps during bud set." + _c("eichhorn-bilodeau-2019-photobiology")),
    callout("tip", "Defoliate in the first weeks, or not at all",
      p("Do the lollipopping and the primary defoliation from approximately day 7 to the end of "
        "week 3. Do this work before the buds get their position. After week 3, do not do a large "
        "defoliation. For the method, read the <a href='defoliation-training.html'>defoliation and "
        "training</a> paper.")),
  ]})

SECTIONS.append({"id": "bulking-ripening", "kicker": "05 · Weeks 5 to 10", "title": "Bulking and ripening (weeks 5 to 10)",
  "blocks": [
    p("Weeks 5 to 7 are the peak of bulking. In this period, the buds increase in size at the "
      "highest rate, the quantity of trichomes increases, and the aroma becomes stronger. Thus the "
      "light, the feed and the CO2 have the largest effect at this time." +
      _c("livingston-2020-trichome-maturation")),
    p("From approximately week 7, the ripening of the plant starts. The white pistils become "
      "orange, the transparent trichomes become milky, and the bottom fan leaves become yellow. The "
      "plant moves nutrients from the leaves into the buds.</p><p>Set the light, the feed and the "
      "CO2 to the highest values during bulking. Then, in ripening, decrease these values and "
      "decrease the humidity, to prevent damage to the harvest. During bulking, increase the PPFD "
      "to approximately 900–1100&nbsp;&mu;mol&middot;m&sup2;&middot;s&sup1; (1200–1500 with CO2 "
      "enrichment at 1000–1200&nbsp;ppm). Increase the feed EC to the peak EC." +
      _c("llewellyn-2022-light-intensity-yield")),
    p("In bulking, the climate during the day is approximately 26–28&nbsp;°C (79–82&nbsp;°F). The "
      "RH decreases to approximately 55 to 62% to decrease the risk of mold while the density of "
      "the buds increases. The VPD is approximately 1.1 to 1.3&nbsp;kPa.</p><p>In ripening (from "
      "week 8), decrease the RH to 40 to 50%. Keep the day temperature from the low to the middle "
      "20s&nbsp;°C (68–77&nbsp;°F). Many growers decrease the nutrients in the last 1 to 2 weeks. "
      "In the last weeks of flowering, bottom leaves that become yellow are usual, because the "
      "plant moves nutrients from these leaves to the buds. The yellow color is not always a "
      "deficiency that you must correct."),
    figure(L.bars("Growth in bud mass each week",
            [("wk1", 5), ("wk2", 10), ("wk3", 30), ("wk4", 55), ("wk5", 95),
             ("wk6", 100), ("wk7", 85), ("wk8", 55), ("wk9", 30), ("wk10", 15)],
            unit="%", note="The growth is at the peak in weeks 5 to 7, then decreases during ripening.", maxv=110), 5,
      "The buds get most of their weight in weeks 5 to 7. In this period, the light, the feed and the CO2 have the largest effect." + _c("livingston-2020-trichome-maturation")),
    figure(L.zones("Target humidity decreases during the cycle",
            35, 75, [(0, 4, L.GL, "First stage 55–65%"), (4, 7, L.AMBL, "Bulking 50–60%"),
                     (7, 10, L.BLUL, "Ripening 40–50%")],
            unit="% RH",
            note="The EC increases into bulking, then decreases. The humidity decreases in all stages to prevent rot."), 6,
      "The humidity decreases in steps, one step for each stage, while the density of the buds "
      "increases. The canopy in the last stage has a high density. In this canopy, a high humidity "
      "causes the most damage." + _c("mahmoud-2023-botrytis-budrot")),
  ]})

SECTIONS.append({"id": "when-to-harvest", "kicker": "06 · The decision", "title": "Examine the trichomes to find the time to cut",
  "blocks": [
    callout("evidence", "Limits of the data",
      "<p>The color of the trichomes changes with the maturation. Livingston measured the "
      "morphology of the trichomes and the content of metabolites. The investigation did not "
      "measure the perceived effects, and it did not validate a harvest target for a "
      "pharmacological effect" + _c("livingston-2020-trichome-maturation") + ". A usual method is "
      "to flush the substrate with only water for a long time. Controlled tests frequently show "
      "that a long flush increases the flavor or the potency by only a small value. Thus decrease "
      "the EC when the nutrient uptake of the plant decreases, but do not cause a nutrient "
      "deficiency.</p>"),
    p("The pistils are a first signal with low accuracy, and they can give incorrect information. "
      "The trichomes are the accurate indicator of the time, and you examine them with a loupe or a "
      "small microscope that has a low cost." + _c("livingston-2020-trichome-maturation")),
    p("Harvest when most of the trichomes are milky or cloudy, and a small fraction of the "
      "trichomes are amber. The ratio of 80 to 90% milky trichomes and 5 to 15% amber trichomes is "
      "a value that growers use. It is not a validated target for an effect. The ratios of "
      "transparent, milky and amber trichomes are not sufficient to show if the crop gives an "
      "energetic effect or a heavy effect. If the chemical profile that you want is important, "
      "compare harvest samples with an analysis of the cannabinoids and terpenes." +
      _c("livingston-2020-trichome-maturation")),
    p("Wait until approximately 70% or more of the pistils are orange or brown and bent to the bud. "
      "Then examine the trichomes to make the correct decision.</p><p>Use a magnification of "
      "60&times; or more. Examine the trichomes on the bud and not on the sugar leaves. Examine "
      "some areas of the plant, because the maturity is not the same in all parts of the plant. Do "
      "not use only the calendar to select the time to harvest. A cultivar with a flowering time of "
      "9 weeks can continue until week 10, because of the conditions and the phenotype."),
    figure(L.line("Trichome color during the ripening weeks",
            [(0, 90), (1, 70), (2, 45), (3, 20), (4, 8), (5, 3)],
            ["wk6", "wk7", "wk8", "wk9", "wk10", "wk11"],
            ylab="% transparent", ymin=0, ymax=100, bands=[(0, 12, L.GXL, "harvest period")],
            note="Transparent trichomes decrease. Milky is at the peak and amber starts. The light green area is the usual harvest period."), 7,
      "The transparent trichomes decrease while the milky trichomes increase, and a small quantity "
      "of amber trichomes starts. Cut in the harvest period, as an indicator of the maturity. If "
      "you cut after this period, the heavy effect is frequently stronger. The genotype continues "
      "to have the largest effect." + _c("livingston-2020-trichome-maturation")),
    table(["Signal", "Condition that you see", "Maturity", "Effect if you cut at this time"], [
      ["Pistils", "Most are white and extend from the bud", "Before the harvest period", "Thin buds, harsh smoke, low potency"],
      ["Trichomes", "Most are transparent", "Before the harvest period", "Low maturity"],
      ["Trichomes", "80–90% milky, 5% amber", "Peak period (first part)", "Usual target when you cut at the start of the period"],
      ["Trichomes", "Milky with 10–15% amber", "Peak period (last part)", "Balanced effect"],
      ["Trichomes", "30% or more amber, yellow leaves", "After the harvest period", "Frequently a stronger heavy effect. The genotype continues to have the largest effect."],
    ], cls="compact", caption="Examine the trichomes on the bud with a magnification of 60&times; or more. The color of the pistils is only a first indication." + _c("livingston-2020-trichome-maturation")),
  ]})

SECTIONS.append({"id": "pitfalls", "kicker": "07 · Problems to prevent", "title": "Troubleshooting",
  "blocks": [
    p("Most of the problems in flowering in a first crop are from a small number of errors. These "
      "errors occur frequently: light leaks, too much defoliation, and high humidity when the buds "
      "have a high density. A harvest time from the calendar, and not from the trichomes, is also "
      "an error. It is easy to prevent each error after you know it. The error with the highest "
      "cost is a harvest before the correct time, because you cannot wait."),
    table(["Problem", "Task"], [
      ["Light leaks in the dark period", "Put tape on the LED indicators and seal the gaps at the doors. A bright light in the night, or a light that occurs many times, can stop flowering. Genetics and more than one stress together cause most hermaphrodite plants."],
      ["Too much defoliation, or defoliation after the correct time", "After week 3, do not remove many leaves. The leaves make the sugar for the plant during bulking."],
      ["Humidity too high in the last weeks of flowering", "From week 7, decrease the RH to 40–50%. Buds with a high density and an RH of 60% or more increase the risk of bud rot (botrytis)."],
      ["Nutrient burn", "Decrease the feed EC. Apply a sufficient volume of water for each feed. Tipburn shows that the feed EC is too high."],
      ["A harvest before the correct time, or a harvest that you select with the calendar", "Use the trichomes to select the time. It is better to wait a small number of more days for the correct maturity than to harvest in the week that the calendar gives."],
    ], cls="compact", caption="The five errors that cause problems in most first crops, and the correct task for each error." + _c("mahmoud-2023-botrytis-budrot")),
    callout("danger", "In the last weeks of flowering, monitor the canopy for rot",
      p("Make sure that the air moves in the room. Keep the humidity low during ripening. In the "
        "last weeks of flowering, a canopy has a high density. In this canopy, a high humidity (60% "
        "or more) increases the risk of bud rot very much. Botrytis starts in the bud, where you "
        "cannot see it. Then it causes damage to the full cola." + _c("mahmoud-2023-botrytis-budrot"))),
  ]})

SECTIONS.append({"id": "expectations", "kicker": "08 · Results and limits", "title": "Expected results and limitations",
  "blocks": [
    p("A typical photoperiod crop in a grow room has the time of vegetative growth and "
      "approximately 8 to 10 weeks of flowering. Only in a small number of crops is your first "
      "harvest your best harvest. The yield and the quality increase when you know how to examine "
      "the plant.</p><p>The genetics of the cultivar set the limits. Your light, your climate and "
      "your feed change how near the crop comes to these limits. The breeder gives the flowering "
      "times as estimates. The finish can be a week or more before or after the estimate, because "
      "of the conditions." + _c("hesami-2023-morphological-lifecycle")),
    table(["Week", "Phase", "Changes in the plant", "PPFD", "Day/night temperature", "RH / VPD", "Task"], [
      ["1–2", "Stretch", "The height becomes two times larger. The first pistils start to show.", "800–900", "27 °C (81 °F) / 23 °C (73 °F)", "65% / 1.0 kPa", "Lollipopping and defoliation"],
      ["3–4", "Bud set", "The stretch stops, and small buds start.", "900", "27 °C (81 °F) / 22 °C (72 °F)", "60% / 1.1 kPa", "Stop defoliation"],
      ["5–7", "Bulking", "The buds increase in size at the highest rate. The quantity of trichomes increases.", "1000–1100", "27 °C (81 °F) / 22 °C (72 °F)", "58% / 1.2 kPa", "Peak feed and high light"],
      ["8–10", "Ripening", "The pistils become orange or brown, and the trichomes become milky.", "900", "24 °C (75 °F) / 20 °C (68 °F)", "45% / 1.2 kPa", "Decrease the RH and the EC. Examine the trichomes."],
    ], cls="compact", caption="This table shows each week. It is not a procedure that you must obey. The trichomes make the last decision."),
    figure(L.flow("The stages of the flower cycle",
            [("Stretch", "wk 1-3"), ("Bud set", "wk 3-4"), ("Bulking", "wk 5-7"),
             ("Ripening", "wk 8-10"), ("Trichome check", "the decision"), ("Harvest", "cut")]), 8,
      "The figure shows all the stages in sequence. After each stage, the next stage starts. The "
      "trichome check gives the decision for the harvest."),
    figure(L.bars("The weight added in each stage",
            [("Stretch", 10), ("Bud set", 20), ("Bulking", 55), ("Ripening", 15)],
            unit="%", note="The buds get most of their mass in bulking.", maxv=65), 9,
      "Do most of your work in bulking. In this stage, the light, the climate and the feed have the largest effect on the harvest."),
    callout("key", "Three important items",
      ol(["<strong>The conditions change the finish date.</strong> The genetics set the range of "
          "the finish date. Your climate and your feed change the position in this range. The "
          "position frequently changes by a week or more.",
          "<strong>Keep a short record.</strong> Record the week, the height, the climate, the feed "
          "and the leaves that you removed. A record is the fastest method to make each crop better "
          "than the crop before it.",
          "<strong>The last weeks are slow.</strong> Do not cut before the correct time. The buds "
          "get a large part of their weight and potency in the last weeks."])),
    p("Make sure that the flip is correct. Decrease the humidity while the density of the buds "
      "increases. Use the trichomes to select the time to harvest. Then read the <a "
      "href='coco-crop-steering.html'>crop steering</a> paper to adjust the feed and the dryback. "
      "Then read the <a href='harvest-dry-trim-cure.html'>harvest, dry and cure</a> paper to "
      "prevent damage to the crop."),
  ]})
