# -*- coding: utf-8 -*-
"""Paper: seeds, germination and seedlings (beginner)."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        stagecard, grid, card, chip, kv, steps)
import figs_lib as L

SLUG = "seeds-germination"
TITLE = "Seeds, germination and seedlings"
EYEBROW = "Basic · Propagation"
SUB = ("This paper shows how to select a seed, how to germinate it, and how to keep the seedling in "
       "good condition. It also gives a definition of a seed. In the first three weeks, the "
       "seedling is very weak.")
META = [("seedling", "Basic"), ("image", "9 figures"),
        ("quote", "9 sources"), ("clock", "~14 min to read")]
RELATED = ["cloning", "light-acclimation", "mould-risk"]
REF_IDS = ["bazzaz-1975-seed-storage-viability", "cockson-2025-hemp-seed-moisture-temperature",
           "smith-2022-hemp-germination-temperature-limits", "flajsman-2021-feminized-seed-production",
           "monthony-2021-feminized-sts-comparison", "toth-2022-autoflower1-locus",
           "moher-2023-twelve-hour-photoperiod-flowering", "rodriguez-2021-cannabis-light-intensity-photosynthesis",
           "zhang-2021-vpd-stomatal-conductance-growth", "lamichhane-2017-damping-off-management",
           "umn-extension-prevent-damping-off"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

SECTIONS.append({"id": "what-this-is", "kicker": "Start here", "title": "Purpose and scope",
  "blocks": [
    lead("This paper is for a new grower. It shows the procedure from a dry cannabis seed to a "
         "seedling in good condition after two to three weeks. The paper gives a definition of each "
         "term where the term first occurs.</p><p>A seed is a small plant in a protective shell. "
         "The plant has no growth until the conditions are correct. Germination is the start of "
         "growth of the seed. A seedling is a small plant in the first weeks after germination."),
    p("Most of the errors that kill a plant occur in the first 21 days. Thus, when you do these "
      "first stages correctly, the other stages of cultivation are much easier. Read this paper "
      "before you get a seed and before you plant it."),
    figure(L.flow("From seed to strong seedling",
            [("Dry seed", "no growth, day 0"), ("Imbibition", "absorbs water"),
             ("Taproot", "root comes out, day 1-3"), ("Planted", "into medium"),
             ("Cotyledons", "seed leaves open"), ("True leaves", "day 7-14"),
             ("Strong", "seedling, day 21")]), 1,
      "The figure shows all the stages in this paper. A dry seed absorbs water, and the taproot "
      "comes out of the seed. You plant the seed, and the seed leaves open. By approximately week "
      "three, the seedling is strong."),
    callout("note", "Information in this paper",
      ul(["How to select a seed, how to germinate it, and how to keep the seedling in good condition until approximately day 21",
          "Germination is the start of growth of a seed. A seedling is a plant in the stage when it is weakest.",
          "Most problems of a new grower have their cause in the first three weeks (rot, seeds that do not germinate, and growth that stops)",
          "Each term has an easy definition where the term first occurs"], "tight")),
  ]})

SECTIONS.append({"id": "key-terms", "kicker": "Terms", "title": "Definitions",
  "blocks": [
    p("This section gives the terms that the other sections of this paper use. It is not necessary "
      "to know the terms at this time, because each term occurs again in the other sections."),
    defterm("Taproot (radicle)", "The first white root. It comes out of the seed and becomes longer "
            "in the down direction. The root is straight. The taproot shows that the seed "
            "germinated."),
    defterm("Cotyledons", "The two round &lsquo;seed leaves&rsquo; that come first. They supply the "
            "plant with the nutrients of the seed, until the true leaves start to supply the plant."),
    defterm("True leaves", "The usual cannabis leaves, with a serrated edge. They come after the "
            "cotyledons. When they come, the growth of the plant starts."),
    defterm("Seed coat", "The outer shell of the seed. It is hard and protective."),
    defterm("Embryo", "The small plant in the seed. Its folded parts are a taproot, two cotyledons, "
            "and a small shoot. The plant has no growth until germination."),
    defterm("Germination rate", "The percentage of seeds in a batch that germinate."),
    defterm("Viable", "A viable seed can germinate. A seed that is not viable cannot germinate. No "
            "task that you do will change this."),
    defterm("Damping-off", "A fungal disease. It makes the seedling rot at the soil surface, and "
            "the seedling falls. No other problem kills more seedlings."),
    table(["Term", "Definition"], [
      ["Taproot / radicle", "The first root of the seed. It becomes longer in the down direction."],
      ["Cotyledons", "The two round &lsquo;seed leaves&rsquo; of the embryo"],
      ["True leaves", "The serrated cannabis leaves that come after the cotyledons"],
      ["Seed coat", "The protective outer shell of the seed"],
      ["Embryo", "The small plant in the seed"],
      ["Germination rate", "The percentage of seeds that germinate"],
      ["Viable", "A seed that can germinate"],
      ["Damping-off", "Fungal rot at the bottom of the seedling stem"],
    ], cls="compact", caption="A short glossary. Use this table again when you read the sections that follow."),
  ]})

SECTIONS.append({"id": "anatomy-and-quality", "kicker": "Primary information 1", "title": "Seed anatomy and quality check",
  "blocks": [
    p("A cannabis seed contains a small plant with all its parts. The plant has no growth until "
      "germination. A hard seed coat gives protection to the embryo. The embryo has a taproot, two "
      "cotyledons, and a small shoot. The seed also contains nutrients. The plant uses these "
      "nutrients in the first days of growth, before the true leaves supply nutrients to the plant."),
    figure(L.flow("Parts in a seed",
            [("Seed coat", "hard outer shell"), ("Embryo", "the small plant"),
             ("Taproot", "first root, folded"), ("Cotyledons", "two seed leaves"),
             ("Nutrients", "for first days")]), 2,
      "The figure shows the inner parts of a seed. The seed coat gives protection to the embryo. "
      "The embryo has the taproot, the cotyledons, and the shoot. The seed contains a small "
      "quantity of nutrients around the embryo."),
    p("You can see some signs of quality. Mature, viable seeds are hard and dark brown. They "
      "frequently have stripes or marks of a different color (&lsquo;tiger stripes&rsquo;). They do "
      "not break when you apply small pressure with your fingers. Pale white, yellow, or "
      "light-green seeds are usually immature, because the grower harvested them before they were "
      "mature. These seeds frequently have a low germination rate, or they make weak plants." +
      _c("bazzaz-1975-seed-storage-viability")),
    p("New seeds that you keep cool, dark, and dry stay viable for years. But the germination rate "
      "decreases when the age of the seeds increases. In this time, degradation of the oils in the "
      "seeds occurs." + _c("cockson-2025-hemp-seed-moisture-temperature") + " A sealed container in "
      "a refrigerator is a good storage area for seeds that you do not use at this time."),
    table(["Check", "Good (viable) seed", "Bad (usually not viable)"], [
      ["Color", "Dark brown, frequently with marks of a different color", "White, yellow, or light green"],
      ["Surface", "Stripes (&lsquo;tiger stripes&rsquo;)", "No stripes, matt surface"],
      ["Hardness", "Hard. The seed does not become flat.", "Soft. The seed changes shape when you apply pressure."],
      ["Test with the fingers", "Keeps its shape", "Breaks"],
    ], cls="compact", caption="Examine the seed and touch it before you start germination. This check is short."),
    callout("tip", "Pale seeds can be viable",
      p("Pale seeds that are immature can germinate, but frequently they make plants that are "
        "weaker and of lower quality. If you can select, plant the dark, hard seeds with stripes "
        "first.")),
  ]})

SECTIONS.append({"id": "seed-types", "kicker": "Primary information 2", "title": "Cannabis seed types",
  "blocks": [
    p("There are three types of seed. Your selection of a type has a large effect on your "
      "cultivation. Regular seeds make approximately half male plants and half female plants. Only "
      "female plants make the flower (the &lsquo;bud&rsquo;) that most growers want. Thus growers "
      "usually remove the male plants."),
    p("Breeders make feminized seeds. These seeds give almost only female plants. Thus it is not "
      "necessary to find male plants and remove them. This prevents work that is not necessary. "
      "Breeders cause a female plant to make pollen with a treatment such as colloidal silver. The "
      "seeds that this pollen makes have only female genetics." +
      _c("flajsman-2021-feminized-seed-production") + _c("monthony-2021-feminized-sts-comparison")),
    p("Autoflower seeds have the genetics of Cannabis ruderalis. These genetics make the plant "
      "start the flowering stage after approximately 2-4 weeks. The light cycle does not change "
      "this. The time from germination to harvest is approximately 60-90 days." +
      _c("toth-2022-autoflower1-locus") + " Photoperiod plants (regular and feminized) start the "
      "flowering stage when the nights are sufficiently long and there is no light in the night "
      "(12/12 is the usual setting)." + _c("moher-2023-twelve-hour-photoperiod-flowering")),
    table(["", "Regular", "Feminized", "Autoflower"], [
      ["Sex of the plants", "Approximately 50% male and 50% female", "Approximately 99% female", "Feminized autoflower seeds: approximately 99% female. Regular autoflower seeds: approximately 50% male and 50% female."],
      ["Flowering trigger", "Change the light cycle to 12h light", "Change the light cycle to 12h light", "Automatic, at a specified age"],
      ["Time to harvest", "Longer than autoflower", "Longer than autoflower", "Approximately 60-90 days after germination"],
      ["Plant size", "Large", "Large", "Approximately 60–120 cm (2–4 ft)"],
      ["Possible yield", "High", "High", "Lower for each plant"],
      ["Easy for a new grower", "No (you must find the male plants and remove them)", "Yes (the easiest)", "Yes (no task to set the time of flowering)"],
    ], cls="compact", caption="Feminized seeds are the easiest first selection. With autoflower seeds, you do not set the time of flowering. Regular seeds are for breeders."),
    callout("note", "Photoperiod and autoflower plants",
      p("Photoperiod plants start the flowering stage when the nights are sufficiently long "
        "(growers usually use 12 hours of light and 12 hours of darkness). Autoflower plants start "
        "the flowering stage at a specified age. The light cycle has no effect on this.")),
  ]})

SECTIONS.append({"id": "germination-methods", "kicker": "Primary information 3", "title": "Germination methods",
  "blocks": [
    p("To start germination, you give the seed three conditions: water, a warm temperature, and "
      "darkness. Darkness is optional. The embryo absorbs water and becomes larger. Then the "
      "taproot comes out through the seed coat. There are three usual methods to give the seed "
      "these conditions."),
    p("In the paper-towel method, you put the seeds between moist paper towels, and you put the "
      "towels between two plates. Growers use this method the most, because they can see the "
      "taproot. With new seed, and with control of the moisture and the temperature, a high "
      "germination rate is frequent." + _c("cockson-2025-hemp-seed-moisture-temperature") +
      " The one risk is that you cause damage to the weak root when you move the seed to its pot."),
    table(["Method", "View of the progress", "Transplant risk", "How easy", "Best for"], [
      ["Paper-towel method", "High (you can see the root)", "Average (touch the root carefully)", "Easy", "Most new growers"],
      ["Direct-sow method", "None (the seed is in the medium)", "None", "Easy", "When you do not want to touch the root"],
      ["Pre-soak method", "Some (the seeds fall in the water and become larger)", "Low", "Easy", "Aged seeds or seeds with a hard seed coat"],
    ], cls="compact", caption="All three methods supply water and a warm temperature. Darkness is optional. The primary difference is that with some methods you can see the progress, and with other methods you cannot."),
    figure(L.flow("The steps of the paper-towel method",
            [("Wet towels", "no free water"), ("Put seeds", "at a distance"),
             ("Towel", "second moist towel"), ("Plates", "put between plates"),
             ("Warm, dark", "21-25C area"), ("Examine 12h", "keep moist"),
             ("Plant", "taproot 0.5-1cm")]), 3,
      "Use towels that are wet but have no free water. Put the seeds apart on a towel, and put a "
      "second towel on them. Keep the seeds warm and dark. Examine the seeds two times each day. "
      "Plant the seed when the taproot is approximately 0.5–1.5 cm (0.2–0.6 in) long." +
      _c("smith-2022-hemp-germination-temperature-limits")),
    callout("tip", "The direct-sow method and the pre-soak method",
      ul(["<strong>Direct-sow:</strong> Plant the seed in the moist medium at a depth of approximately 1–1.5 cm (0.4–0.6 in), with the taproot down. There is no transplant shock, but you cannot see the progress.",
          "<strong>Pre-soak:</strong> Soak the seeds in water at room temperature for 12-24 hours. The seed coat becomes soft. Use this method for aged seeds or for seeds that have a hard seed coat. After this, move the seeds to a towel or to the medium."], "tight")),
  ]})

SECTIONS.append({"id": "conditions-and-timeline", "kicker": "By stage", "title": "Germination conditions and time sequence",
  "blocks": [
    p("The environment has an effect on seeds. Three conditions are important: temperature, "
      "moisture, and light. When all three are in the correct range, most viable seeds germinate "
      "with no other aid."),
    p("Keep the temperature at a stable 21–25 °C (70–77 °F). A lower temperature makes germination "
      "slower. A temperature that is higher, or that changes, causes seeds that do not germinate." +
      _c("smith-2022-hemp-germination-temperature-limits") + " Keep the medium or the towel moist, "
      "but do not make it too wet. Keep the seeds moist and warm until they germinate (darkness is "
      "optional)."),
    figure(L.zones("Best temperature for germination", 14, 34,
            [(14, 21, L.BLUL, "too cold, slow"), (21, 25, L.GL, "best"),
             (25, 28, L.AMBL, "warm, more risk"), (28, 34, L.REDL, "too hot, stops")],
            unit="C",
            note="A stable temperature in the green zone gives fast germination with the highest rate."), 4,
      "Use a temperature in the green zone and keep it stable. Changes of temperature, and a "
      "temperature of more than approximately 28 °C, are a frequent cause of seeds that do not "
      "germinate." + _c("smith-2022-hemp-germination-temperature-limits")),
    figure(L.line("The first 21 days",
            [(0, 0), (2, 1), (4, 2), (7, 3), (10, 4), (14, 5), (21, 6)],
            ["day 0", "day 2", "day 4", "day 7", "day 10", "day 14", "day 21"],
            ylab="growth stage", ymax=7,
            note="Stage 0 seed, 1 taproot, 2 planted, 3 cotyledons, 4-5 first true leaves, 6 strong seedling."), 5,
      "The taproot usually comes out of the seed in 24-72 hours (a maximum of approximately 7 days "
      "for some seeds). The cotyledons open after some days. The first true leaves come at "
      "approximately days 7-14. At approximately day 21, the seedling is strong." +
      _c("cockson-2025-hemp-seed-moisture-temperature")),
    callout("key", "The three conditions",
      ul(["<strong>Temperature:</strong> a stable 21–25 °C (70–77 °F). Do not let the temperature change, and do not let it become more than approximately 28 °C.",
          "<strong>Moisture:</strong> moist, but not too wet. A seed that is too wet cannot get oxygen, and it rots.",
          "<strong>Light:</strong> darkness is optional during germination. After the seed germinates, immediately give light of low intensity, to prevent a stem that is too long and thin."], "tight")),
  ]})

SECTIONS.append({"id": "seedling-care", "kicker": "By stage", "title": "Seedling procedures in the first two to three weeks",
  "blocks": [
    p("The seedling transpires water through its leaves. The rate is higher than the rate at which "
      "the small root system supplies water. Dry, warm air removes water from all objects near it, "
      "and from the leaves of the seedling. Air with high humidity has almost the maximum quantity "
      "of water, and it removes much less water.</p><p>The vapor pressure deficit (VPD) is the "
      "difference between the quantity of water that the air can hold and the quantity that it "
      "holds. The unit is kPa. VPD shows how strongly the air removes water from the leaves. When "
      "the VPD is lower, the air has more humidity and removes less water from the "
      "leaves.</p><p>For the first two weeks, keep the VPD at 0.4–0.8 kPa (65–80 % relative "
      "humidity, RH)." + _c("zhang-2021-vpd-stomatal-conductance-growth") + " A humidity dome, or a "
      "transparent bag with vents, above the seedling can keep this range easily for the first 7–10 "
      "days."),
    p("Keep the light intensity low. In the first week, use approximately 100-200 PPFD. In week "
      "two, use 200-300 PPFD (a DLI near 10-15). Keep the LEDs at a large distance from the "
      "seedlings. This distance prevents stems that are too long and damage to the leaves from the "
      "light." + _c("rodriguez-2021-cannabis-light-intensity-photosynthesis") +
      "</p><p>PPFD is the quantity of light that falls on the plant at this time and that the plant "
      "can use. DLI is the total quantity of light that the plant receives in one day."),
    p("At first, do not apply feed. The cotyledons supply the nutrients for the plant. Start with a "
      "weak nutrient solution, at approximately 25 % strength, only when the first true leaves "
      "show. The first true leaves show in approximately weeks 2–3.</p><p>EC (electrical "
      "conductivity) shows the quantity of nutrients that are in the water. If the EC is too low, "
      "the plant does not get sufficient nutrients. If the EC is too high, the plant has nutrient "
      "burn. At this stage, use an EC of approximately 0.3–0.8 mS/cm.</p><p>Apply only a small "
      "quantity of water, around the bottom of the stem. Between the times that you apply water, "
      "let the surface become less wet. Then the roots become longer, down in the medium, and find "
      "moisture."),
    table(["", "Week 1", "Week 2", "Week 3"], [
      ["Humidity (RH)", "70-80%", "65-75%", "55-65%"],
      ["VPD (kPa)", "0.4-0.6", "0.6-0.8", "0.8-1.0"],
      ["Light (PPFD / DLI)", "100-200 / approximately 10", "200-300 / approximately 13", "250-350 / approximately 15"],
      ["Feed EC (mS/cm)", "None (water only)", "Approximately 0.3-0.6, when the true leaves show", "Approximately 0.6-0.8"],
      ["Apply water", "Spray, or a small quantity of water, near the stem", "A small quantity. Let the surface dry.", "A larger quantity than in week two, but the quantity is small"],
    ], cls="compact", caption="Targets for the seedling in each week. At the start, use a high humidity and weak light. Then decrease the humidity slowly, and increase the light and the feed slowly."),
    figure(L.bars("Light distance and stretch",
            [("Light too far", 18), ("Correct distance", 7)], unit=" cm stem",
            note="Stem height of a seedling at two weeks. If the light is too far, the stem becomes too long and weak.",
            maxv=22), 6,
      "When the light is at a large distance, the seedling becomes long, thin, and weak. At the "
      "correct distance, the seedling stays short and thick. This shape is correct." +
      _c("rodriguez-2021-cannabis-light-intensity-photosynthesis")),
    callout("warn", "Two errors of new growers",
      p("Do not apply too much water. Do not apply feed before the correct time. These two errors "
        "kill more seedlings than all other causes. If you are not sure, apply less water and apply "
        "feed after more time. A seedling with a small nutrient deficiency can be in good condition "
        "again. A seedling with rot cannot.")),
  ]})

SECTIONS.append({"id": "troubleshooting", "kicker": "When a problem occurs", "title": "Troubleshooting",
  "blocks": [
    p("Damping-off is the disease that kills the most seedlings. Soil fungi such as Pythium, "
      "Fusarium, and Rhizoctonia cause this disease. A seedling that was in good condition suddenly "
      "becomes thin and black at the soil surface, and it falls. When the disease starts, it almost "
      "always kills the seedling." + _c("lamichhane-2017-damping-off-management")),
    p("The primary cause is too much water, together with a humidity that is too high and low "
      "airflow. Thus it is better to prevent the disease than to apply a treatment. Use new, "
      "sterilized medium. Apply a small quantity of water. Add a weak circulation of air. When the "
      "true leaves show, decrease the humidity to 40-50%." + _c("umn-extension-prevent-damping-off")),
    figure(L.flow("How damping-off starts (and where to stop the sequence)",
            [("Much water", "high humidity"), ("Low airflow", "no air movement"),
             ("Wet medium", "stays wet"), ("Fungal growth", "in wet soil"),
             ("Damping-off", "the seedling falls")]), 7,
      "Stop the sequence at the start. Apply less water, increase the airflow, and decrease the "
      "humidity after the true leaves show. When the fungus is in the stem, it usually kills the "
      "seedling." + _c("lamichhane-2017-damping-off-management")),
    table(["Symptom", "Usual cause", "Procedure"], [
      ["The stem rots and falls at the soil surface", "Damping-off (too much water, high humidity, no air movement)", "Remove the seedling. Let the medium dry. Increase the airflow and decrease the humidity. These tasks only prevent the disease."],
      ["The seed does not germinate", "Aged seed or immature seed. The temperature is too low. The seed is too deep in the medium. The seed became dry.", "Use new seed. Keep the temperature at 21–25 °C. Plant the seed at a depth of 0.5–1.5 cm (0.2–0.6 in). Keep the medium moist."],
      ["A stem that is long and thin", "The light is too weak or too far from the seedling", "Move the light nearer to the seedling, or use a light with a higher intensity. At the transplant, put the stem deeper in the medium."],
      ["Dry leaf tips (tipburn)", "Feed applied before the correct time, or feed that is too strong", "Stop the feed and apply only water. Then start the feed again at approximately 25% strength."],
      ["A seedling that becomes yellow", "Too much water, or feed that you applied before the correct time", "Let the medium become less wet. Do not apply nutrients until the true leaves show."],
    ], cls="compact", caption="Find the cause for each symptom. For most problems, the correction is to apply less water and less feed, and to give more air."),
    callout("danger", "There is no treatment for damping-off",
      p("Prevent damping-off. Use new, sterilized medium. Apply a small quantity of water. Give "
        "good airflow. After the true leaves show, decrease the humidity to 40-50%." +
        _c("umn-extension-prevent-damping-off") + " When the bottom of a seedling becomes thin, the "
        "seedling cannot be in good condition again.")),
  ]})

SECTIONS.append({"id": "realistic-expectations", "kicker": "Check of the results", "title": "Expected results and limitations",
  "blocks": [
    p("Not all seeds germinate, also when the seeds are good and the procedure is careful. New "
      "feminized seed of good quality frequently has a germination rate of much more than 90%. But "
      "one or two seeds that do not germinate are usual. They do not show that you did a task "
      "incorrectly." + _c("bazzaz-1975-seed-storage-viability")),
    figure(L.bars("Usual germination rate for each seed condition",
            [("New feminized", 95), ("Aged seed", 75), ("Pale or immature", 45), ("Bad storage", 30)],
            unit="%",
            note="Approximate values only. New, dark seed that you keep correctly has the highest rate.",
            maxv=100), 8,
      "New seed of good quality has a high germination rate. A high age, immature seed, and bad "
      "storage all decrease the rate." + _c("cockson-2025-hemp-seed-moisture-temperature")),
    p("The time from the day that you plant the seed to a strong seedling with some groups of true "
      "leaves is approximately 3-4 weeks. After this time, the vegetative growth of the plant "
      "increases quickly. Germinate one or two more seeds as a precaution. It is possible that the "
      "problems in this paper kill a small number of seedlings. Do not apply too much water, and do "
      "not apply feed before the correct time."),
    callout("key", "Good results",
      ul(["A high germination rate is usual for new seed of good quality. But it is possible that one or two seeds do not germinate, also when you do all tasks correctly.",
          "The time from the day that you plant the seed to a strong seedling is approximately 3-4 weeks. After this time, fast growth starts.",
          "Germinate one or two more seeds as a precaution. It is usual for a new grower that a problem kills a seedling from time to time.",
          "The two errors that kill the most seedlings of a new grower are too much water and feed applied before the correct time. It is safer to apply less water and less feed."], "tight")),
    p("In these first weeks, a slow and careful procedure gives the best results. When your "
      "seedling is strong, read the paper on <a href='light-acclimation.html'>light "
      "acclimation</a>. It shows how to increase the light safely. Also read the paper on <a "
      "href='mould-risk.html'>mold risk</a>, because the humidity decreases at this time. For the "
      "next cultivation, you can use <a href='cloning.html'>cloning</a> and not seeds. Cloning "
      "gives you an accurate copy of a plant that you know is good."),
  ]})
