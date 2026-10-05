# -*- coding: utf-8 -*-
"""Paper: light acclimation, ramping onto high light without bleaching (beginner)."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        stagecard, grid, card, chip, kv, steps)
import figs_lib as L

SLUG = "light-acclimation"
TITLE = "Increase the PPFD in steps to prevent bleaching"
EYEBROW = "Basic · Light"
SUB = ("This paper shows how plants adapt when the light intensity increases. It shows how to make "
       "a list of PPFD values for each week and how the CO2 sets the safe PPFD limit. It also shows "
       "how to read the first signs of a problem. The paper includes new data (2024-2026) on the "
       "effect of high light on quality, and on far-red light and UV.")
META = [("sun", "Basic"), ("image", "10 diagrams"),
        ("quote", "12 sources"), ("clock", "~11 min to read")]
RELATED = ["coco-crop-steering", "signal-and-noise", "plant-state-dashboard"]
REF_IDS = ["rodriguez-morrison-2021-cannabis-light-intensity-yield",
           "chandra-2008-cannabis-photosynthesis-ppfd-co2-temperature",
           "llewellyn-2022-cannabis-yield-proportional-light-uv",
           "moher-2022-cannabis-vegetative-light-intensity-morphology",
           "takahashi-murata-2008-environmental-stress-photoinhibition",
           "pospisil-2016-ros-photosystem-ii-light-temperature",
           "gjindali-johnson-2023-photosynthetic-acclimation",
           "sun-shade-leaf-thickness-chloroplast-acclimation",
           "saetang2024-high-light-metabolites",
           "farred2025-scirep",
           "rfr2024-yield-vs-metabolites",
           "huebner2024-uv-spectra"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

SECTIONS.append({"id": "intro", "kicker": "Start here", "title": "Purpose and scope",
  "blocks": [
    lead("Two errors of new growers cause most of the light damage in a grow room. The first error "
         "is to apply full-power light to weak clones that have new roots. The second error is the "
         "opposite. The grower applies light that is too low to plants in the flowering stage, "
         "because the grower thinks that the light can burn the plants" +
         _c("rodriguez-morrison-2021-cannabis-light-intensity-yield") + "."),
    p("The two errors have the same correction. The plant <em>adapts to</em> the light intensity in "
      "a period of some weeks. When the plant has time at each value of the PPFD, it changes the "
      "structure of the parts of the leaf that absorb light. Thus its capacity agrees with the "
      "light.</p><p>If you increase the intensity too quickly, or to a value that is too high for "
      "the CO2, the plant has too much energy. This energy does not increase the growth. It causes "
      "damage: white tips with bleaching, and the growth stops."),
    p("The quantity of light that a plant can receive changes very much in one full cycle. A weak "
      "clone can receive approximately 80 &micro;mol/m&sup2;/s. A canopy at peak flower with CO2 "
      "enrichment can receive a maximum of approximately 1500 &micro;mol/m&sup2;/s" +
      _c("llewellyn-2022-cannabis-yield-proportional-light-uv") + ". This paper gives information "
      "on the acclimation of plants and on a list of PPFD values for each week. It also gives "
      "information on the highest PPFD that is safe and on how to read the signs of a problem."),
    figure(L.line("Light is a ramp, not one step",
            [(0, 90), (1, 250), (2, 400), (3, 550), (4, 700), (5, 850), (6, 1000)],
            ["clone", "Vegetative 1", "Vegetative 2", "Vegetative 3", "Photoperiod change", "flower", "peak"],
            ylab="PPFD &micro;mol/m&sup2;/s", ymax=1100,
            note="The correct method: the intensity increases in steps that are sufficiently small."), 1,
      "A ramp in small steps lets the plant make capacity before each new step of light. A fast "
      "change to full power, in one step from low to high, is too fast for the plant. The plant "
      "cannot use all the photons." + _c("gjindali-johnson-2023-photosynthetic-acclimation")),
    callout("note", "The persons for this paper",
      p("This paper is for each person who caused heat damage to a clone. It is also for each "
        "person who does not increase the light because the light can cause damage. Read it with "
        "the papers <a href='coco-crop-steering.html'>crop steering</a> and <a "
        "href='plant-state-dashboard.html'>plant state dashboard</a>.")),
  ]})

SECTIONS.append({"id": "key-terms", "kicker": "Glossary", "title": "Definitions",
  "blocks": [
    p("This paper uses five terms. If you know these terms, the paper is easy to read. Each term "
      "occurs again in the next sections."),
    defterm("PPFD (Photosynthetic Photon Flux Density)", "The intensity of the light at the canopy "
            "that the plant can use. The unit is &micro;mol/m&sup2;/s (micromoles of photons for "
            "each square meter in each second). PPFD is the intensity at one time."),
    defterm("DLI (Daily Light Integral)", "The total quantity of light that a plant can use in one "
            "day, in mol/m&sup2;/day. When the PPFD increases or the number of hours of light "
            "increases, the DLI increases. DLI is the total dose of light for the day."),
    defterm("Photoperiod", "The hours with light and the hours without light in each day. A "
            "photoperiod of 18/6 (18 hours of light) is usual for vegetative growth. A photoperiod "
            "of 12/12 causes flowering."),
    defterm("Photoinhibition and bleaching", "Damage that occurs when a leaf absorbs more light "
            "energy than it can use. The leaf has too much light. The light causes a chemical "
            "reaction that damages the leaf. The molecules that this chemical reaction makes are "
            "<strong>reactive oxygen species</strong> (ROS). ROS cause damage to the leaf tissue, "
            "and the tips of the top leaves become white."),
    defterm("Acclimation", "In a period of some weeks, a plant changes the structure of the parts "
            "of the leaf that use light. The plant makes more chloroplasts, makes the surfaces of "
            "the leaf thicker, and makes protective enzymes. Thus the plant has the capacity for "
            "each new value of the light. The plant adapts to each step before the next step."),
    figure(L.flow("PPFD: intensity at one time. DLI: total for the day",
            [("PPFD", "the intensity at the leaf at one time"),
             ("hours of light", "time with the lights on"),
             ("DLI", "PPFD x hours = dose for the day")],
            note="The same PPFD gives much less DLI with 12/12 than with 18/6."), 2,
      "PPFD is the intensity at one time. DLI is the total of the light for the day. When you "
      "change the photoperiod, the DLI changes, also when the PPFD stays the same."),
  ]})

SECTIONS.append({"id": "how-acclimation-works", "kicker": "How the plant adapts to more light", "title": "Acclimation of the plant to a higher PPFD",
  "blocks": [
    p("The plant makes new parts for the higher PPFD. In each week, the plant makes more "
      "chloroplasts (the small green parts of a cell that absorb light) and thicker protective "
      "surfaces on the leaf. It also makes a higher density of the enzymes that change the absorbed "
      "energy into sugar" + _c("sun-shade-leaf-thickness-chloroplast-acclimation") +
      ". Thus each new step of light has parts that are prepared to use it."),
    p("A plant that has the parts for a moderate PPFD cannot use a sudden large quantity of "
      "photons. The parts that absorb light continue to absorb energy, but the leaf cannot use all "
      "of it. The energy that the leaf cannot use makes ROS faster than the protective enzymes of "
      "the leaf can remove them" + _c("takahashi-murata-2008-environmental-stress-photoinhibition") +
      ". You see tips with bleaching, and the growth stops" +
      _c("pospisil-2016-ros-photosystem-ii-light-temperature") + "."),
    p("Thus a ramp in small steps is the correct method. When you add light in steps that are "
      "sufficiently small for the plant, the capacity increases with the intensity. As a result, "
      "each photon makes sugar and does not cause damage" +
      _c("gjindali-johnson-2023-photosynthetic-acclimation") + "."),
    figure(L.flow("Acclimation in a safe loop",
            [("Small light step", "add one step of PPFD"),
             ("Make new parts", "more chloroplasts and enzymes"),
             ("Higher capacity", "prepared for more light"),
             ("Next step", "again, in safe steps")],
            note="Each step is sufficiently small for the plant to make the parts before the next step."), 3,
      "The safe ramp is a loop. First, the PPFD increases by a small step. Then the plant makes "
      "capacity. Then the next step occurs. " + _c("sun-shade-leaf-thickness-chloroplast-acclimation")),
    figure(L.bars("Fast change and steps: light that the plant uses",
            [("Fast change to full", 35), ("Ramp in steps", 95)], unit="%", maxv=110,
            note="Same PPFD at the end: with the fast change, most light becomes damage and not growth."), 4,
      "If a plant receives a large PPFD before acclimation, it changes much of the light into "
      "damage and not into sugar. A plant with a ramp uses almost all the light." +
      _c("takahashi-murata-2008-environmental-stress-photoinhibition")),
    callout("warn", "The plant makes the damage of bleaching",
      p("Decrease the PPFD, or give the plant more time for acclimation. Do not add more light, "
        "because more light increases the damage. White tips on the top leaves show that the leaf "
        "makes ROS faster than it can remove them. The ROS cause damage to the tissue of the leaf.")),
  ]})

SECTIONS.append({"id": "co2-partnership", "kicker": "How the CO2 sets your PPFD limit", "title": "Light and CO2 together",
  "blocks": [
    p("In each green cell, the plant changes light energy and CO2 into sugar. Sugar is the material "
      "for all growth. The name for this change is <strong>photosynthesis</strong>, and it has two "
      "connected stages. The <strong>light reactions</strong> absorb energy from the photons. Then "
      "the <strong>Calvin cycle</strong> uses CO2 from the air to change this energy into sugar. "
      "The two stages must increase together" +
      _c("chandra-2008-cannabis-photosynthesis-ppfd-co2-temperature") + "."),
    p("If you increase the light but the CO2 stays low, the result is the same as when you increase "
      "the PPFD too quickly. The light reactions continue to absorb energy, but the Calvin cycle "
      "does not have sufficient CO2 to use this energy for sugar. The energy collects in the leaf "
      "and causes <em>the same</em> bleaching from oxidation. When you examine the leaf, you cannot "
      "find the difference between the two errors" +
      _c("pospisil-2016-ros-photosystem-ii-light-temperature") + "."),
    p("A system with high PPFD must have a CO2 concentration that agrees with the PPFD. With "
      "ambient air (approximately 400&ndash;600 ppm CO2), a PPFD of much more than approximately "
      "850 &micro;mol/m&sup2;/s uses electricity, but most of the light does not make sugar" +
      _c("chandra-2008-cannabis-photosynthesis-ppfd-co2-temperature") + ". For 1200 "
      "&micro;mol/m&sup2;/s, the CO2 must be approximately 1000&ndash;1200 ppm. For 1500, the CO2 "
      "must be approximately 1200&ndash;1500 ppm" +
      _c("rodriguez-morrison-2021-cannabis-light-intensity-yield") + "."),
    figure(L.flow("Low CO2: the energy causes damage",
            [("Light reactions full", "photons absorbed quickly"),
             ("Calvin cycle: low CO2", "no CO2 to make sugar"),
             ("Too much energy", "the leaf cannot use it"),
             ("Bleaching", "oxidation damage, white tips")],
            note="High light with low CO2 causes the same damage as a PPFD that increases too fast."), 5,
      "When the CO2 is the limiting factor, more light only increases the damage." +
      _c("takahashi-murata-2008-environmental-stress-photoinhibition")),
    figure(L.zones("The PPFD limit increases with the CO2", 400, 1600,
            [(400, 950, L.GL, "ambient air, approximately 950"),
             (950, 1200, L.AMBL, "with CO2 to 1200"),
             (1200, 1500, L.GXL, "full system 1500")],
            unit="", note="For a higher PPFD range, the CO2 must agree with the range. If not, the result is only bleaching."), 6,
      "The CO2 sets the highest PPFD that the plant can use. When the PPFD is more than the limit "
      "of your CO2, more light does not help and can cause damage." +
      _c("chandra-2008-cannabis-photosynthesis-ppfd-co2-temperature")),
    callout("key", "Keep this fact",
      p("Light increases the growth only when the CO2 is sufficient. When the CO2 is not "
        "sufficient, more light does not increase the growth. The growth stops and the leaf becomes "
        "too hot.")),
  ]})

SECTIONS.append({"id": "ppfd-schedule", "kicker": "The values to use", "title": "PPFD values for acclimation in each growth stage",
  "blocks": [
    p("A cycle of approximately 14 weeks (approximately 98 days) in a grow room is an example. In "
      "this cycle, the light increases stage by stage" +
      _c("moher-2022-cannabis-vegetative-light-intensity-morphology") + ". The PPFD for clones is "
      "low. The PPFD in the vegetative stage increases in regular steps. After the change to the "
      "flowering photoperiod, the PPFD increases again to its peak, and then it decreases by a "
      "small quantity at the end."),
    p("The change to 12/12 decreases the daily light integral (DLI) by approximately one third "
      "(approximately 33%) at the same PPFD. The cause is that the lights are on for a smaller "
      "number of hours" + _c("rodriguez-morrison-2021-cannabis-light-intensity-yield") +
      ". This effect is usual and correct. Do not increase the dimmer to a value that is too high "
      "because of it."),
    figure(L.bars("Daily light integral in the cycle",
            [("Clone", 6), ("Vegetative 1", 16), ("Vegetative 2", 26), ("Vegetative 3", 36),
             ("To 12/12", 26), ("Flower", 40), ("Peak", 52), ("Ripening", 46)],
            unit="", target=None, maxv=58,
            note="DLI in mol/m2/day. The DLI decreases at 12/12, but the PPFD increases."), 7,
      "The DLI increases in the vegetative stage, decreases at the change of the photoperiod (a "
      "smaller number of hours of light), and then increases again when the PPFD for flowering "
      "increases." + _c("moher-2022-cannabis-vegetative-light-intensity-morphology")),
    table(["Stage", "Photoperiod", "PPFD range (&micro;mol/m&sup2;/s)", "Information"], [
      ["Clone", "18/6", "80 &rarr; 300", "Use a low PPFD while the clone makes roots and the parts that use light."],
      ["Vegetative bulking", "18/6", "300 &rarr; 650", "Increase the PPFD by approximately 100 each week."],
      ["Flower acclimation", "12/12", "600 &rarr; 950", "The plant adapts again after the DLI decreases at the change of the photoperiod."],
      ["Peak flower", "12/12", "950, 1200 or 1500", "Keep the PPFD at the limit of your tier."],
      ["Maturation", "12/12", "950 &rarr; 850", "Decrease the PPFD by a small quantity during ripening."],
    ], cls="compact", caption="A ramp for each stage. Use these ranges as start values. You can "
       "change the values for your room. The peak PPFD that you keep changes if your CO2 or your "
       "climate changes." + _c("rodriguez-morrison-2021-cannabis-light-intensity-yield")),
    callout("tip", "The change of the photoperiod",
      p("The DLI decreases at 12/12. This effect is usual and correct. At the start of flowering, "
        "let the plant adapt again from approximately 600 to 950. Do not increase the lights to the "
        "peak PPFD on the day of the change.")),
  ]})

SECTIONS.append({"id": "how-high", "kicker": "Set your PPFD limit", "title": "Set the PPFD limit",
  "blocks": [
    p("The environment of your room sets the safe peak PPFD, and the PPFD that you want does not "
      "set it. The PPFD that you can keep is the PPFD that your CO2, your climate and your cooling "
      "can supply at this time. To increase the limit, you must increase the capacity of the full "
      "system, and not only the dimmer."),
    p("With ambient air, the correct PPFD limit is approximately 950 &micro;mol/m&sup2;/s. When the "
      "PPFD is more than approximately 850, each added &micro;mol gives less yield, because the CO2 "
      "is not sufficient to use the added light" +
      _c("chandra-2008-cannabis-photosynthesis-ppfd-co2-temperature") + ". A middle system with CO2 "
      "that agrees with the PPFD gives a limit of 1200. The 1500 tier is only for advanced growers. "
      "The full system for the environment is necessary for this tier" +
      _c("llewellyn-2022-cannabis-yield-proportional-light-uv") + "."),
    table(["", "Tier 1, Basic", "Tier 2, Middle", "Tier 3, Advanced"], [
      ["Peak PPFD", "approximately 950", "1200", "1500"],
      ["Necessary CO2", "400&ndash;600 ppm (ambient air)", "1000&ndash;1200 ppm", "1200&ndash;1500 ppm"],
      ["Necessary conditions", "None. A PPFD of more than approximately 850 does not help the yield.", "Good control of the VPD, and CO2 enrichment",
       "Control of the leaf temperature, a method for the substrate, and a cultivar that can use the high light"],
    ], cls="compact", caption="Select the tier that your environment can supply. If the CO2 is less "
       "than the value in the table, a higher PPFD causes only bleaching." +
       _c("rodriguez-morrison-2021-cannabis-light-intensity-yield")),
    figure(L.bars("Peak PPFD that each tier can use",
            [("Basic (ambient air)", 950), ("Middle (+CO2)", 1200), ("Advanced (full system)", 1500)],
            unit="", maxv=1650,
            note="Each bar is light that the plant can use only if the CO2 agrees with it."), 8,
      "For the limit of each tier, the full system is necessary, and not only a higher setting of "
      "the light." + _c("llewellyn-2022-cannabis-yield-proportional-light-uv")),
    callout("warn", "Do not add more light than your CO2 can use",
      p("Do not operate Tier 3 light with Tier 1 air. This has the highest cost and causes "
        "bleaching of the plants. First, use the full PPFD limit that you can supply with CO2. Then "
        "try a higher limit.")),
  ]})

SECTIONS.append({"id": "hanging-and-dimming", "kicker": "Adjust the height and the output", "title": "Fixture height and dimmer",
  "blocks": [
    p("Two levers set the PPFD at the canopy: the <strong>dimmer</strong> of the fixture and its "
      "<strong>hanging height</strong> above the plants. The two levers change the quantity of "
      "light on the leaves, but the effect of each lever is different."),
    p("The dimmer is the lever with the best precision for small steps that are the same each time. "
      "It changes the intensity, but it does not change the distribution of the light or the "
      "radiant heat at the canopy. When you change the height of the fixture, the distribution and "
      "the heat also change. Thus a change of the height is a larger adjustment."),
    p("When you use one of the levers, <strong>make sure that the PPFD value is correct.</strong> "
      "Measure the PPFD at the canopy with a meter, or read it from the distance chart of the "
      "fixture. Do not use the watts of the fixture or the position of the dimmer as the PPFD. The "
      "same fixture gives very different values at different heights. Also measure the PPFD again "
      "when the distance between the canopy and the light becomes shorter. As a result of the "
      "stretch of the plants, the PPFD increases also if you make no change."),
    figure(L.flow("Two levers and one correct number",
            [("Dimmer", "small steps, same each time"),
             ("Hanging height", "larger steps and a change of heat"),
             ("Measure at the canopy", "meter or distance chart"),
             ("Measure again", "PPFD increases with stretch")],
            note="Do not use the dimmer position or watts as data. Measure the PPFD at the leaves."), 9,
      "Use the dimmer to set the intensity and the height to set the distribution and heat. Always "
      "measure the PPFD at the canopy. Do not use an estimate."),
    callout("tip", "The distance to the light changes",
      p("A plant can have a stretch of 15 cm (6 in) in the direction of the light in one week. The "
        "distance between the plant and the light then becomes shorter. As a result, the PPFD on "
        "the plant increases by a large quantity, also if you do not touch the lights. Measure the "
        "PPFD again after each period of fast growth.")),
  ]})

SECTIONS.append({"id": "troubleshooting", "kicker": "Read the plant", "title": "Troubleshooting",
  "blocks": [
    p("Too much light causes <strong>white tips with bleaching at the top of the canopy</strong>, "
      "on the leaves near the source. The growth also stops" +
      _c("pospisil-2016-ros-photosystem-ii-light-temperature") + ". But two different errors cause "
      "the same symptom, and you cannot find which error caused it from the leaf only."),
    p("The first error is to increase the intensity too quickly. The second error is high light "
      "with low CO2. The two errors cause too much energy in the leaf and the same damage from "
      "oxidation. Thus the symptoms are the same" +
      _c("takahashi-murata-2008-environmental-stress-photoinhibition") + ". Do not try to find the "
      "error from the leaf only. Prevent the two errors: increase the intensity in small steps "
      "<em>and</em> keep the CO2 correct for your intensity."),
    table(["Symptom", "Possible cause", "Correction"], [
      ["White tips with bleaching at the top of the canopy", "The PPFD increases too quickly, or the light is high and the CO2 is low", "Decrease the PPFD by one step. Make sure that the CO2 agrees with your intensity."],
      ["Bleaching at a PPFD that you think is safe", "The leaf temperature or the VPD is not in the correct range", "First correct the climate. Heat and dry air cause bleaching also at a safe PPFD."],
      ["The growth stops at high light", "The capacity of the plant is not sufficient, or the CO2 is the limiting factor", "Keep the intensity the same. Give the plant time to adapt. Do a check of the CO2."],
      ["Light green leaves, much stretch and flowers with low density", "The light is too low for a long time, because the grower thinks that more light causes damage", "Increase the PPFD in steps. A light that is too low also decreases the yield."],
    ], cls="compact", caption="The damage is the same, but the causes are different. Prevent the two causes before the damage occurs. Do not try to find the cause after the damage."),
    callout("danger", "Do not decrease the light too much after bleaching",
      p("After bleaching, decrease the light by one step only. Then increase the light again in "
        "steps. After bleaching occurs one time, growers frequently decrease the light for "
        "flowering to a value that is much too low. As a result, the yield decreases. A light that "
        "is too low for a long time causes damage to a crop. The damage is as large as the damage "
        "that bleaching causes to plants" + _c("rodriguez-morrison-2021-cannabis-light-intensity-yield") +
        ".")),
  ]})

SECTIONS.append({"id": "latest-research", "kicker": "New data · 2024-2026", "title": "New tests",
  "blocks": [
    lead("Acclimation and the correct CO2 for the PPFD are the primary information in this paper. "
         "New tests (2024-2026) do not change this information. They give more information on three "
         "effects. The first effect is the effect of a high PPFD limit. The other two effects are "
         "from the spectrum levers far-red and UV. The data show that the effects of these two "
         "levers are smaller than many persons think."),
    p("<strong>A high PPFD limit with sufficient CO2 increases the quality, and not only the "
      "weight.</strong> In a test in 2024, the PPFD increased from 600 to 1200 "
      "&micro;mol/m&sup2;/s. The cannabinoid content increased by approximately "
      "<strong>60%</strong>, and the terpenoid content increased by approximately "
      "<strong>40%</strong>. These two increases came from <em>two causes</em>: a heavier "
      "inflorescence and higher concentrations. The light-use efficiency was almost constant" +
      _c("saetang2024-high-light-metabolites") + ".</p><p>A previous test shows that the yield of "
      "dry flower has an almost linear relation with the PPFD, to approximately 1800 &micro;mol" +
      _c("rodriguez-morrison-2021-cannabis-light-intensity-yield") + ". Thus the data agree: a "
      "correct ramp to a high PPFD limit gives a better grade and more mass. This result is correct "
      "<em>if</em> the CO2 and the climate agree with the PPFD. Without sufficient CO2, the added "
      "light causes only bleaching (see the section above)."),
    figure(L.bars("PPFD from 600 to 1200 (with correct CO2): more metabolites",
            [("Cannabinoid content", 60), ("Terpenoid content", 40)], unit="%", maxv=70,
            note="From a test in 2024: more inflorescence mass and higher concentrations."), 10,
      "More light with sufficient CO2 increases the concentration and also the weight. It is a "
      "lever for quality and not only for yield." + _c("saetang2024-high-light-metabolites")),
    p("<strong>Far-red light can increase the cannabinoid yield in some cultivars, but it can "
      "decrease the potency in other cultivars.</strong> Far-red light at the end of the day lets "
      "you decrease the photoperiod from 12 to 10 hours, with approximately 5.5% less energy. In "
      "<em>some</em> cultivars, far-red light at the end of the day increases the cannabinoid "
      "yield. One cultivar showed a total cannabinoid yield that was approximately 70% higher" +
      _c("farred2025-scirep") + ".</p><p>But when you add far-red light to all the spectrum (a "
      "lower ratio of red to far-red), the inflorescence mass can <em>increase, and the "
      "concentration of cannabinoids and terpenes can decrease</em>" +
      _c("rfr2024-yield-vs-metabolites") + ". The buds are higher and larger, have a lower density, "
      "and are weaker. Far-red light also causes stretch. Use far-red light as a tool for one "
      "cultivar at a time. Do not use it as a standard part of the spectrum because you think that "
      "more is better."),
    p("<strong>UV light does not usually increase the potency in new cultivars.</strong> A previous "
      "test found that added UV-B light did not increase the yield or the cannabinoid content" +
      _c("llewellyn-2022-cannabis-yield-proportional-light-uv") + ". A test of UV spectra in 2024 "
      "also showed that the cannabinoids did not increase. High UV-B light <em>decreased</em> the "
      "THC and burned the leaves. Only the lowest dose of UV-A light changed the terpene profile by "
      "a small quantity (linalool +29%, limonene +25%, myrcene +22%), and the yield stayed the same" +
      _c("huebner2024-uv-spectra") + ".</p><p>Cultivars with high THC are near their maximum "
      "potency. Thus do not think that UV light increases the potency. A careful low dose of UV-A "
      "light can change the aroma by a small quantity. This effect is the maximum. Added UV light "
      "usually decreases the efficiency."),
    callout("key", "First the intensity, then the spectrum",
      p("First make the ramp and the CO2 correct. Then change the spectrum. Far-red light and UV "
        "light give small effects, and each has an unwanted effect. You use them with an intensity "
        "that is correct. They are not an alternative to it.</p><p>If a plant does not have full "
        "acclimation and the CO2 is too low, a change of the spectrum does not help. A correct ramp "
        "to your PPFD limit, with sufficient CO2, gives a better result.")),
  ]})

SECTIONS.append({"id": "expectations", "kicker": "Results and limits", "title": "Expected results and limitations",
  "blocks": [
    p("The light intensity is only one input. Each PPFD target in this paper is for an environment "
      "in which all the other values are in range. The leaf temperature is approximately "
      "26&ndash;28&deg;C (79&ndash;82&deg;F). The VPD is 1.2&ndash;1.5 kPa. The root zone has "
      "sufficient capacity. The cultivar has a tolerance for the light load" +
      _c("chandra-2008-cannabis-photosynthesis-ppfd-co2-temperature") + ".</p><p>If you increase "
      "the light and the CO2 without these conditions, the plants become hot and have stress. The "
      "yield does not increase."),
    table(["Necessary for all tiers", "Target"], [
      ["Leaf temperature", "approximately 26&ndash;28&deg;C (79&ndash;82&deg;F)"],
      ["VPD (drying power of the air)", "1.2&ndash;1.5 kPa"],
      ["Root-zone capacity", "Sufficient water and oxygen for the quantity that the plant uses"],
      ["Cultivar", "A cultivar with a tolerance for the light that you use"],
    ], cls="compact", caption="These conditions are necessary for each tier. The light gives a good "
       "result only when the temperature, the humidity and the root zone are also in range."),
    callout("key", "Use the correct tier for your room",
      p("A cycle without errors at the correct PPFD limit gives a better result than a cycle with "
        "errors at a higher limit. For most new growers, the best procedure is to use the ambient "
        "air limit of approximately 950 without errors. First make the acclimation and the CO2 "
        "correct. After that, you can try 1200 or 1500.")),
    p("The light is only one input. It gives a good result only when all the other values of the "
      "environment are correct. The paper <a href='plant-state-dashboard.html'>plant state "
      "dashboard</a> shows how to read all the data of the plant. The paper <a "
      "href='signal-and-noise.html'>signal and noise</a> shows how to use correct signals and not "
      "noise."),
  ]})
