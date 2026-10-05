# -*- coding: utf-8 -*-
"""Paper: ripening, flush and harvest timing - the last two weeks and the call to chop."""
import json, os
from components import (p, lead, h, ul, ol, callout, defterm, table, figure, grid, card, chip, kv, steps)
import figs_lib as L

_FIGS = json.load(open(os.path.join(os.path.dirname(__file__), "figs_ripening.json"), encoding="utf-8"))

SLUG = "ripening-harvest-timing"
TITLE = "Ripening, flush, and the time to harvest"
EYEBROW = "Flowering · Ripening"
SUB = ("This paper shows the ripening of cannabis buds in the last two weeks and how to select the "
       "time to harvest. You will know how to read trichomes accurately with a loupe. You will know "
       "which harvest window is correct for your product. You will know the results of tests on "
       "flush. You will also know how to prevent botrytis. Botrytis can cause damage to all the "
       "crop that you made in eighteen weeks.")
META = [("spark", "Flowering"), ("image", "10 diagrams"),
        ("quote", "14 sources"), ("clock", "~17 min to read")]
RELATED = ["flowering-stages", "harvest-dry-trim-cure", "mould-risk"]
REF_IDS = ["livingston-2020-trichome-maturation", "punja-2023-trichome-maturation",
           "aizpurua-2016-cannabinoid-evolution", "ross-elsohly-1997-cbn-age",
           "maillard-2015-leaf-nutrient-remobilization", "massuela-2022-pruning-cbd-yield",
           "namdar-2018-inflorescence-position", "pressclub-hash-trichome-transition",
           "rxgreen-2019-flushing-trial", "stemeroff-2017-flushing-thesis",
           "mahmoud-2023-botrytis-budrot", "punja2025-budrot-epi",
           "llewellyn-2022-light-intensity-yield", "huebner2024-uv-spectra"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

# ---------------------------------------------------------------- 01 start here
SECTIONS.append({"id": "start-here", "kicker": "01 · Start here", "title": "Purpose and scope",
  "blocks": [
    lead("After eighteen weeks of tasks, you must make one decision: the time to cut the plant. If "
         "you harvest before the correct time, you do not get the weight and maturity that the "
         "plant continues to make. If you harvest after the correct time, the plant adds only a "
         "small quantity of weight, but the flower has a risk of bud rot.</p><p>This paper is about "
         "the last stage. It shows the ripening of the buds and how to read the buds correctly. It "
         "also shows how to select the time of harvest that is correct for your product."),
    p("We wrote this paper for a grower who makes a first or second crop. Thus we give information "
      "about each term. We also give a grade to the data for each item. When the data are strong, "
      "we tell you this.</p><p>Some methods that growers use have no test data to show that they "
      "are correct. These methods are mostly for the last stage of flowering. We tell you this "
      "clearly. We use the same procedure for each of these items: flush, the percentage of amber, "
      "48 hours of darkness, and UV finishers. For each item, we show the test data, the method of "
      "growers, and the information that suppliers give."),
    p("Two tasks occur at the same time in the last two weeks. The first task is to let the plant "
      "complete ripening. The weight and the resin maturity continue to increase for a longer time "
      "than the growers of a first crop think" + _c("massuela-2022-pruning-cbd-yield") +
      ". The second task is to prevent damage to the crop that you made. In a canopy with high "
      "density, the risk of botrytis is at its maximum during ripening. One wet night can cause "
      "more damage than the weight and maturity that one more week of ripening adds" +
      _c("punja2025-budrot-epi") + "."),
    figure(L.flow("The last two weeks, in sequence",
            [("Bud weight", "weeks 6-7: weight increases"),
             ("Fade starts", "Yellow bottom leaves"),
             ("Hold RH", "45-55%, with airflow"),
             ("Read calyx", "each 2 days, same positions"),
             ("Window", "cloudy peak, amber starts"),
             ("Harvest", "tasks prepared")],
            note="Two tasks at the same time: let the plant complete ripening, and prevent rot."), 1,
      "The last stage is a sequence of steps and not a date. The loupe shows when the window "
      "starts. The condition of the room shows if you can continue to wait."),
    callout("note", "Who this is for",
      p("This paper is for a person who is in week 6 of flowering or after this week. The person "
        "wants to know the time to the harvest. <a href='flowering-stages.html'>The paper about the "
        "weeks of flowering</a> is the paper before this paper. <a "
        "href='harvest-dry-trim-cure.html'>The paper about harvest, drying, trimming and curing</a> "
        "is the paper after this paper. This paper stops when you cut the first plant.")),
  ]})

# ---------------------------------------------------------------- 02 vocabulary
SECTIONS.append({"id": "vocab", "kicker": "02 · The terms", "title": "Definitions",
  "blocks": [
    p("This paper uses these eight terms many times. Make sure that you know the terms before you "
      "continue."),
    defterm("Trichome", "A trichome is a small gland that makes resin. It is on the surface of the "
            "buds and of the leaves near the buds. A trichome has a stalk and a head. Most "
            "cannabinoids and terpenes in the flower are in the trichomes with a stalk. The color "
            "of the heads when you examine them with a loupe is the primary signal of ripeness."),
    defterm("Pistil (stigma)", "A pistil is a white hair on each flower. At the start, pistils are "
            "white. They become brown while ripening continues, and also when pollen touches the "
            "flower. A pistil is only an approximate sign of ripeness in the first stage."),
    defterm("Calyx (bract)", "A calyx is a small part of the bud, and a bud is a group of calyxes. "
            "Growers use the term calyx, but in biology the part is mostly a bract. In the last "
            "stage of ripening, the calyxes increase in size, and you can see this. You read the "
            "trichomes on the surface of the calyx."),
    defterm("The fade", "The fade is the time in the last stage of flowering when the fan leaves "
            "become yellow. The plant moves mobile nutrients out of the leaves and into the flower. "
            "The fade is usual senescence. The fade is not always a deficiency."),
    defterm("Flush", "A flush is the procedure in which you apply only water (or feed with a very "
            "low concentration) in the last days or weeks. Growers do this because they think that "
            "a flush makes the flavor better and makes the flower burn better. Some growers think "
            "that a flush has this effect, and some growers think that it does not. Section 07 "
            "gives the results of tests."),
    defterm("Harvest window", "The harvest window is the period of days in which the maturity of "
            "the trichomes is correct for your product. The window starts slowly, and its time is "
            "different for each genotype. Mold can stop the window quickly, before its usual end."),
    defterm("Foxtailing", "Foxtailing is new growth from a bud in the last stage of flowering. The "
            "cause is usually heat or light stress. The signs of ripeness from the pistils and the "
            "calyxes start again. As a result, you cannot read the bud correctly."),
    defterm("Staggered harvest", "A staggered harvest is a procedure in which you first cut the top "
            "canopy, at full ripeness. Then you give the bottom canopy more days with light, to let "
            "it complete ripening. You do not cut all the plant at the same time."),
  ]})

# ---------------------------------------------------------------- 03 core answer
SECTIONS.append({"id": "core-answer", "kicker": "03 · The primary points", "title": "Ripening windows for each product",
  "blocks": [
    p("The decision to harvest has three parts. First, read ripeness from the trichomes on the "
      "surface of the calyx. Do not read ripeness from the calendar or from the "
      "pistils.</p><p>Second, the correct time in ripening is different for each product. A hash "
      "maker harvests before a flower grower does. For biomass for extraction, the harvest window "
      "is the widest.</p><p>Third, cut before your target only if there is pressure from mold. "
      "Flower without mold that you harvest some days before your target is always better than "
      "flower that has full ripeness and botrytis."),
    figure(L.zones("Amber percentage for harvest",
            0, 40, [(0, 5, L.BLUL, "hash window"), (5, 15, L.GL, "flower window"),
                    (15, 30, L.AMBL, "&lsquo;heavier&rsquo; effect"), (30, 40, L.REDL, "after peak")],
            unit="%",
            note="Percentage of amber heads on the calyx at mid-cola. The zones are grower methods. No laboratory test shows these limits."), 2,
      "One scale gives one decision. The percentage of amber at harvest is different for each "
      "product. The zones are grower methods, and the genotype changes the limits of the zones."),
    p("Usually it is correct to wait. Many tests of the time of harvest find that the weight of the "
      "inflorescence continues to increase in the last stage of ripening. One test was in a grow "
      "room with controlled conditions, with a CBD cultivar. In this test, the dry weight of the "
      "flower increased at each harvest time from week 5 to week 11. The concentration of "
      "cannabinoids did not change. The best total yield was at week 9 and not at week 7" +
      _c("massuela-2022-pruning-cbd-yield") + ".</p><p>Measurements of cannabinoids during "
      "flowering show the same trend. The content increases to a peak that is different for each "
      "cultivar. The peak occurs at different times for different chemotypes" +
      _c("aizpurua-2016-cannabinoid-evolution") + "."),
    figure(L.line("Flower weight increases in the last stage",
            [(0, 55), (1, 74), (2, 90), (3, 100)],
            ["wk 5", "wk 7", "wk 9", "wk 11"],
            ylab="dry weight, % of maximum", ymin=40, ymax=110,
            note="Diagram of the trend in Massuela (2022). The weight increased at each harvest. The CBD concentration did not change."), 3,
      "If you harvest two weeks before the last harvest in the test, the weight is less, but the "
      "concentration is the same." + _c("massuela-2022-pruning-cbd-yield")),
    callout("key", "The three parts of the decision",
      p("Read the trichomes on the calyx at mid-cola, at an interval of two days from week "
        "7.</p><p>Cut at the stage that is correct for your product. For hash, cut when most heads "
        "are cloudy and the percentage of amber heads is at its minimum. For usual flower, cut when "
        "most heads are cloudy and 5&ndash;15% of the heads are amber.</p><p>If botrytis occurs, do "
        "not wait. Harvest the plant immediately.")),
  ]})

# ---------------------------------------------------------------- 04 biology
SECTIONS.append({"id": "how-buds-ripen", "kicker": "04 · The biology", "title": "Ripening biology",
  "blocks": [
    p("Four changes that you can see occur together in the last weeks, and each change is a signal "
      "that you can read. When you know the cause of each change, you can find the error if one "
      "signal is incorrect."),
    p("<strong>The color of the trichomes changes in ripening.</strong> In the last stage of "
      "flowering, the surface of the flower has many capitate-stalked trichomes. These trichomes "
      "are large glands with a stalk. Most resin is in these glands. Tests with a microscope show "
      "that these glands change in shape and in chemical content while ripening continues. The "
      "contents change, the stalks become longer, and the color of the head shows the condition of "
      "its contents" + _c("livingston-2020-trichome-maturation") + ".</p><p>A head is clear "
      "(transparent) when the resin is thin and its quantity increases. When the contents are at "
      "maturity, the head becomes cloudy (white and not transparent). When oxidation of the resin "
      "starts, the head becomes amber. The speed of this change and the quantity of amber heads are "
      "very different for each genotype and for each age of the plant. Some cultivars show almost "
      "no amber before the heads collapse" + _c("punja-2023-trichome-maturation") +
      "."),
    figure(_FIGS["trichome_stages"], 4,
      "The figure shows the four stages that you see with a loupe, and the decision for each stage. "
      "The stages are some days apart, and the genotype changes the speed. Examine many heads and "
      "not one gland." + _c("punja-2023-trichome-maturation")),
    p("<strong>The cannabinoids increase to a peak, and then oxidation of the resin "
      "starts.</strong> Measurements each week during flowering show that THC and CBD increase to a "
      "peak that is different for each cultivar. The peak occurs in the last stage of the cycle" +
      _c("aizpurua-2016-cannabinoid-evolution") + ". After the peak, THC changes slowly into CBN, a "
      "related cannabinoid with different properties. This chemical change occurs in one direction "
      "only. The change is oxidation.</p><p>Tests show oxidation in cannabis that is in storage. In "
      "these tests, the CBN:THC ratio shows how long the samples were in storage" +
      _c("ross-elsohly-1997-cbn-age") + ". Amber heads show the start of this change on the "
      "plant.</p><p>Some growers think that amber heads give a sedative effect "
      "(&lsquo;couch-lock&rsquo;) because of CBN. Be careful: the data on this effect for persons "
      "are weak. Amber shows that the resin is after its peak. Amber does not give information "
      "about the effect of the flower."),
    p("<strong>The pistils become brown and bend.</strong> At the start, the stigmas are white and "
      "can receive pollen. Then they become brown and bend while ripening continues. Use the "
      "pistils only as an approximate indication of the time in ripening. If most pistils are "
      "white, it is not the time to harvest.</p><p>But stress and pollen also cause the pistils to "
      "change, and not only ripeness. Foxtailing starts the pistils again. The pistils show you "
      "when to start to examine the trichomes with a loupe. Do not use the pistils to make the "
      "decision to harvest."),
    p("<strong>The calyxes increase in size and the fade occurs.</strong> In the last weeks, the "
      "bracts become larger, and you can see this. The buds have a higher density, and the fan "
      "leaves become yellow from the bottom leaves to the top leaves. The fade is the movement of "
      "mobile nutrients from the leaves to the flower.</p><p>Leaves in senescence send mobile "
      "nutrients (mostly nitrogen) to the flower. Tests on many crop species show the same movement "
      "of nutrients" + _c("maillard-2015-leaf-nutrient-remobilization") + ".</p><p>A small fade in "
      "week 8 shows that the plant completes ripening at the correct time. It is not a deficiency. "
      "Do not correct it. A strong fade with dry leaves in week 6 is a problem. Refer to "
      "Troubleshooting."),
    callout("note", "Color is a sign of ripeness",
      p("The color change shows the chemical condition of the resin. New, thin resin is clear. "
        "Contents at maturity scatter the light, and the head is cloudy. Resin in oxidation becomes "
        "yellow. Thus the reading of the color is a correct method, but the color is only a sign "
        "and not a measurement in a laboratory. Two cultivars at the same color stage can have "
        "different chemistry" + _c("punja-2023-trichome-maturation") + ".")),
  ]})

# ---------------------------------------------------------------- 05 the read
SECTIONS.append({"id": "reading-ripeness", "kicker": "05 · The reading", "title": "Ripeness check with a loupe",
  "blocks": [
    p("The cause of most incorrect harvest decisions is the sampling. The grower reads one area "
      "that is easy to see, or reads the sugar leaves, or reads a different bud each time. As a "
      "result, the data change from one reading to the next. If you correct the sampling, the "
      "decision is easy."),
    p("<strong>Tools.</strong> A 30&ndash;60x loupe is sufficient, and its cost is very low. A USB "
      "microscope (60&ndash;200x), or a microscope that you attach to a phone, has a low cost and "
      "is easier for the eyes. With a microscope, you can record images of the same position on "
      "different days. A microscope also makes the difference between clear and cloudy heads easier "
      "to see.</p><p>Use white light with the color of daylight. With HPS lamps (orange light), all "
      "the heads show an amber color. With LED lamps that have blue and purple light, all the heads "
      "show a purple color. If the position of the canopy makes the reading not easy, cut one calyx "
      "and read it on a bench. An image that is stable is better than an image that moves."),
    figure(_FIGS["scope_map"], 5,
      "The figure shows where to read and where not to read. The ripening of the top of the plant "
      "occurs before the ripening of the bottom. The content of cannabinoids and terpenes also "
      "decreases from the top to the bottom" + _c("namdar-2018-inflorescence-position") +
      ". Thus if you read only the top, you harvest the room before the correct time. If you read "
      "larf, you harvest after the correct time."),
    p("<strong>Where.</strong> Read the surface of the calyxes at mid-cola, at the middle height of "
      "the canopy. Do not read the sugar leaves. The small leaves in the bud have trichomes that "
      "become cloudy and then amber some days before the trichomes on the surface of the calyx. If "
      "you read these leaves, you can harvest a week before the correct time. This error is "
      "usual.</p><p>Identify two or three positions on the branch with a small piece of tape. Read "
      "the same positions each time. Also read one top cola, to monitor the vertical gradient" +
      _c("namdar-2018-inflorescence-position") + "."),
    p("<strong>Frequency.</strong> Read the trichomes at an interval of two days from week 7, or "
      "when most pistils are brown. The trichome stages change in some days. As a result, two "
      "readings each week give you a trend and not only one value. Record an estimate each time, "
      "for example &lsquo;d52: ~15% clear / 80% cloudy / 5% amber, mid&rsquo;. The trend between "
      "the readings is the primary signal."),
    ol(["Use the same positions each time: 2&ndash;3 positions with a mark on the calyx at mid-cola, and one top cola.",
        "Use the same light: white light with the color of daylight, or the room lights. Do not use the light of HPS lamps.",
        "Read the surface of the calyx. Do not read the trichomes on the sugar leaves.",
        "Make an estimate of the percentages for all the heads in the loupe, and not for one gland.",
        "Record the readings. Three readings give a trend. With no readings, you have no data."]),
    figure(_FIGS["ripeness_signals"], 6,
      "The figure shows the signals in rows. The signals above the row for the loupe tell you when "
      "to start to examine the trichomes. Only the reading of the trichomes on the calyx gives the "
      "decision to harvest."),
  ]})

# ---------------------------------------------------------------- 06 product goal
SECTIONS.append({"id": "product-windows", "kicker": "06 · The product", "title": "Harvest windows for each type of product",
  "blocks": [
    p("Do not start with &lsquo;when do I harvest?&rsquo; Start with &lsquo;what is this flower "
      "for?&rsquo; because each product has a different window."),
    p("<strong>Ice-water hash and rosin: harvest at the maximum of cloudy heads, before "
      "amber.</strong> To make hash, you use a mechanical procedure to disconnect the trichome "
      "heads from the plant. The heads must have no damage. They must have their maximum structure: "
      "they must be at full size, cloudy, and easy to remove from the stalk.</p><p>Hash makers try "
      "to get the highest number of cloudy heads with a minimum of amber heads. Amber heads are "
      "after the peak, and measurements show that they are smaller. The hash and the rosin from "
      "amber heads have a darker color and a greasy texture" + _c("pressclub-hash-trichome-transition") +
      ". For some cultivars, you cannot prevent 10&ndash;20% amber at the cloudy peak, and the hash "
      "is satisfactory. A hash maker who wants high quality does not wait for amber."),
    p("<strong>Flower: the usual method is to harvest when most heads are cloudy and 5&ndash;15% of "
      "the heads are amber.</strong> For flower that persons smoke, you can wait until the first "
      "amber heads occur. Then the flower has full maturity, full weight, and a full "
      "aroma.</p><p>Some growers want a &lsquo;heavier&rsquo; effect, and they wait until "
      "20&ndash;30% of the heads are amber. Be careful: if you wait for this effect, you get three "
      "results. The first result is oxidation of the resin, which tests show" +
      _c("ross-elsohly-1997-cbn-age") + ". The second result is effects for which there are no test "
      "data. The third result is more days with a risk of rot" + _c("punja2025-budrot-epi") +
      "."),
    p("<strong>Biomass for extraction (distillate cartridges): the widest window.</strong> "
      "Distillation makes the extract clean. Thus the precision of the trichome stage is not very "
      "important. The total cannabinoid content and clean biomass with no mold are the most "
      "important.</p><p>If you harvest some days before or after the peak, the change is small. If "
      "botrytis occurs in the biomass, or if you harvest after the window and the quality of the "
      "flower decreases, the potency decreases. You can be less careful about ripeness. You must be "
      "careful about sanitation."),
    figure(_FIGS["product_windows"], 7,
      "The figure shows one plant with three products and three windows. The risk of rot continues "
      "during all three windows. A hash maker harvests first, a flower grower harvests in the "
      "middle, and biomass for extraction has the widest window." +
      _c("pressclub-hash-trichome-transition")),
    table(["Product", "Harvest at", "Cause", "Result if you harvest after the window"], [
      ["Ice-water hash / rosin", "Maximum of cloudy heads, minimum of amber heads", "Heads at full size with no damage are easy to remove. They give hash and rosin that are very clean.", "The hash has a darker color and a greasy texture. Amber heads are smaller and give an unsatisfactory result in the wash."],
      ["Flower (usual)", "Most heads cloudy, 5-15% amber", "Full weight and aroma at resin maturity", "Growers think that the smoke is not &lsquo;smooth&rsquo; and that the flower has a sedative effect, but no test shows this. The risk of rot increases."],
      ["Flower (&lsquo;heavier&rsquo; effect)", "15-30% amber", "Growers wait after full ripeness because they want a &lsquo;heavier&rsquo; effect.", "Tests show oxidation of the resin. This harvest has the longest time with a risk of rot of all flower harvests."],
      ["Distillate cartridges / extract", "Some days before or after the peak", "Distillation makes the extract clean, thus a small error in the trichome stage is not important.", "Only mold and a harvest a very long time after the peak are a problem."],
    ], cls="compact", caption="The window for each product. If one room supplies more than one product, harvest the hash plants first. Then harvest the flower, and last the biomass for extraction."),
    callout("tip", "Rooms with more than one product",
      p("If you use one cultivar for hash and for flower, do a staggered harvest for each product. "
        "Harvest the hash plants (or the top canopy for hash) when the number of cloudy heads is at "
        "its maximum. Give the flower plants more days of ripening. Thus you have one room and two "
        "harvests, and each product is in its window.")),
  ]})

# ---------------------------------------------------------------- 07 flush debate
SECTIONS.append({"id": "flush-debate", "kicker": "07 · The flush", "title": "Flush and the results of tests",
  "blocks": [
    p("Many growers apply only water in the last 7&ndash;14 days. They think that the plant then "
      "uses the nutrients that it keeps in its tissue. They also think that the smoke is more "
      "&lsquo;smooth&rsquo;, the flavor is better, and the ash is white. Growers use this method "
      "frequently. But almost no test data show that it is correct. Here are the results of tests."),
    p("<strong>The test by Rx Green Technologies.</strong> Growers refer to this test most "
      "frequently. In the test, plants of the cultivar Cherry Diesel had a flush of 0, 7, 10 or 14 "
      "days before the harvest. After the harvest, the test measured the plants.</p><p>The flush "
      "time did not cause statistically significant differences in the yield (average 97.3 g (3.4 "
      "oz) for each plant), the THC (average 21.9%), or the terpenes. The flush did not decrease "
      "the mineral content of the flower by the quantity that growers think. Nitrogen was only "
      "approximately 6.7% less after 14 days, and iron and zinc were <em>higher</em> in flower with "
      "a flush.</p><p>A blind panel is a group of persons who do not know which samples had a "
      "flush. This panel did not find the samples with a flush. The trend was to the sample with "
      "<em>no flush</em>. 36% of the panel found the smoke of the 0-day flush &lsquo;smooth&rsquo;. "
      "19.4% of the panel found the smoke of the 14-day flush &lsquo;smooth&rsquo; (this difference "
      "is not statistically significant)" + _c("rxgreen-2019-flushing-trial") +
      "."),
    figure(L.hbars("Blind panel test, Rx Green flush test",
            [("0-day flush", 36), ("14-day flush", 19.4)],
            unit="%", note="Percentage of the panel that found the smoke &lsquo;smooth&rsquo;. Not statistically significant: the trend is not for a flush."), 8,
      "The result of the blind panel is important. The panel did not find the flower that had a "
      "flush, and the trend was to the flower with no flush." + _c("rxgreen-2019-flushing-trial")),
    p("<strong>The test at Guelph shows the same result.</strong> An MSc thesis at the University "
      "of Guelph gives the results of tests on medical cannabis with no nutrients at the end of the "
      "cycle. The tests found that a flush did not decrease the element content of the flower by an "
      "important quantity, and did not change the yield" + _c("stemeroff-2017-flushing-thesis") +
      ".</p><p>The two sources have limits. One source is a white paper from a manufacturer, with "
      "one cultivar and a small panel. The other source is a thesis. It has no journal peer review "
      "(a subsequent erratum applies to a different chapter). But the two tests have no connection, "
      "and they show the same result. We do not know of a controlled test that shows the opposite "
      "result."),
    p("<strong>A flush cleans the substrate and not the flower.</strong> A flush cleans the root "
      "zone. The minerals in the tissue of the buds came there through the plant. Water around the "
      "roots does not remove them from the tissue.</p><p>In the last stage of the cycle, the "
      "senescence of the leaves moves mobile nutrients out of the leaves and into the flower" +
      _c("maillard-2015-leaf-nutrient-remobilization") + ". This movement occurs with or without a "
      "flush.</p><p>A long flush <em>does</em> decrease the EC of the substrate very quickly. The "
      "plant must then use the nutrients that it keeps before the correct time. The fade can become "
      "faster. If the flush is very long, the weight that the plant adds in the last stage can be "
      "less. Tests show that the plant adds this weight" + _c("massuela-2022-pruning-cbd-yield") +
      "."),
    table(["Claim", "Results of tests", "Grade"], [
      ["Smoke that is more &lsquo;smooth&rsquo;, better flavor", "A blind panel did not find the flush. The trend was to the flower with no flush.", "No test shows this" + _c("rxgreen-2019-flushing-trial")],
      ["Removes minerals from the flower", "The mineral content of the flower is almost the same. Iron and zinc are higher in flower with a flush.", "Tests show the opposite" + _c("rxgreen-2019-flushing-trial") + _c("stemeroff-2017-flushing-thesis")],
      ["White ash shows that the flush is correct", "The color of the ash changes with combustion and moisture. No test shows that the color of the ash is a sign of a flush.", "No test data"],
      ["A flush has no bad effect", "A long flush can cause senescence before the correct time, while the plant continues to add weight.", "Incorrect: there is a bad effect" + _c("massuela-2022-pruning-cbd-yield")],
      ["A lower feed EC in the last stage", "Uptake decreases while senescence continues. A lower EC that agrees with the uptake is agronomy and not a flush.", "A satisfactory method between a flush and no flush"],
    ], cls="compact", caption="The table of claims about a flush. Tests show that the claims that they examine are incorrect. It is correct to decrease the EC slowly, by a small quantity, when the uptake decreases."),
    callout("evidence", "The methods that commercial growers use",
      p("Some growers do a flush, and some growers do not do a flush. In many SOPs of commercial "
        "growers, the procedure is a flush with only water for 7&ndash;14 days. One cause is that "
        "growers always did a flush. A second cause is that buyers want to know if the flower had a "
        "flush, and this has a strong effect on commercial growers.</p><p>Other growers apply feed "
        "at full strength until the day of the harvest, and they refer to the tests above. Many "
        "growers use a method between a flush and feed at full strength. They decrease the feed EC "
        "slowly in the last week, to agree with the lower uptake. The plant continues to receive "
        "feed.</p><p>The data show that a long flush with only water does not make the smoke "
        "better, and that persons cannot find a difference. If you do a flush, keep it short. No "
        "test shows a good effect that is sufficient for three weeks of only water.")),
  ]})

# ---------------------------------------------------------------- 08 the room
SECTIONS.append({"id": "late-environment", "kicker": "08 · The room", "title": "Climate control in the last stage of flowering",
  "blocks": [
    p("In the last two weeks, one task for the climate is more important than the other tasks. The "
      "changes of temperature are a method of growers, and they are not necessary. The control of "
      "humidity is necessary to keep the crop in good condition. First control the limit for the "
      "relative humidity (RH). Then do the other controls."),
    p("<strong>Temperature: a frequent method, but weak data.</strong> Most growers decrease the "
      "day temperature by a small quantity in the last two weeks, from approximately 26 to 23 "
      "&deg;C (79 to 73 &deg;F). They also decrease the night temperature to 21 to 18 &deg;C (70 to "
      "64 &deg;F). The claims for this method are terpenes that stay in the flower, buds with a "
      "higher density, and purple color. Almost no controlled test on cannabis examines these "
      "claims. Cool nights do cause purple color in genotypes that can make anthocyanin, but no "
      "test shows the claims for potency and for terpenes.</p><p>The risk of this method is low, "
      "and the method is satisfactory. But the method has one side effect, and you must know it. "
      "Warm air can hold more water vapor than cool air. When the temperature decreases, the same "
      "quantity of moisture in the room is a larger percentage of the capacity of the air. As a "
      "result, the relative humidity increases, but you do not add water. Each degree of lower "
      "temperature increases the RH, and your dehumidification must remove more water."),
    figure(_FIGS["lateflower_ramp"], 9,
      "The figure shows a usual change of the climate in the last two weeks. The day and night "
      "temperatures decrease. Growers use this method, but no test shows that it is correct. The RH "
      "decreases to a value less than the RH limit, and you must not change this limit. A lower "
      "room temperature increases the RH for the same moisture load. Make sure that the "
      "dehumidifier has sufficient capacity for the higher RH."),
    p("<strong>Humidity: this control is necessary.</strong> Buds in ripening have a high density, "
      "they make shade for each other, and they keep moisture. Bud rot, from <em>Botrytis "
      "cinerea</em>, is the problem that causes the most damage in the last stage. Tests in "
      "greenhouses show that the risk of infection with bud rot increases when the humidity and the "
      "bud density increase. The pathogen is in the cola, where you cannot see it, until the damage "
      "occurs" + _c("mahmoud-2023-botrytis-budrot") + ".</p><p>Spores occur in almost all areas. "
      "Epidemiology tests show that you control the spores with the environment and with "
      "sanitation, and that you cannot remove all the spores" + _c("punja2025-budrot-epi") +
      ".</p><p>Use these procedures. Hold the RH at 45&ndash;55%. Do not let the RH become more "
      "than 58%. Keep a flow of air through the canopy. Do not point a strong airflow at the "
      "canopy. Monitor the change at lights-off.</p><p>At lights-off, the temperature decreases, "
      "the RH increases quickly, and condensation can occur on colas with high density. Most rot "
      "starts in this one hour."),
    figure(L.zones("RH zones for ripening",
            35, 70, [(35, 45, L.BLUL, "safe, but VPD is high"), (45, 55, L.GL, "target"),
                     (55, 60, L.AMBL, "be careful"), (60, 70, L.REDL, "risk of botrytis")],
            unit="% RH",
            note="The maximum RH is more important than the average. Spikes at lights-off and condensation cause the damage."), 10,
      "Keep the RH in the target zone and less than the RH limit. An average RH of 50% with spikes "
      "to 65% each night is worse than a stable 55%." + _c("mahmoud-2023-botrytis-budrot")),
    p("<strong>UV &lsquo;finishers&rsquo;: be careful with the claims of the suppliers.</strong> "
      "The claim is to apply strong UV in the last weeks, to make the THC higher. Controlled tests "
      "frequently show that this claim is incorrect. The largest test of light intensity in a grow "
      "room found that more UV light did not increase the yield or the cannabinoid content" +
      _c("llewellyn-2022-light-intensity-yield") + ".</p><p>A test in 2024 of the light spectrum "
      "found that the UV treatments decreased the yield or did not change it. The treatments did "
      "not increase the cannabinoids. The THC was <em>lower</em> with the strongest UV-B. The only "
      "good result was that some terpenes were approximately 20&ndash;30% higher, with very low UVA "
      "doses" + _c("huebner2024-uv-spectra") + ".</p><p>If you have the equipment, a test with a "
      "low dose of UVA is a satisfactory method. Do not get lamps to increase the potency. Tests "
      "show that this claim is incorrect."),
    callout("warn", "The risk of more days of ripening",
      p("If your room cannot keep the RH in the target zone, harvest at the start of your window. "
        "Do not wait for more days when the RH is in the zone of botrytis risk. Each day of "
        "ripening that you add is a day with a risk of rot" + _c("punja2025-budrot-epi") +
        ". Some causes are a dehumidifier that is too small, a canopy with high density, and spikes "
        "at lights-off.")),
  ]})

# ---------------------------------------------------------------- 09 staggered
SECTIONS.append({"id": "staggered-harvest", "kicker": "09 · Staggered harvest", "title": "Staggered harvest",
  "blocks": [
    p("There is a vertical gradient in the plant. The top colas receive the most light, have "
      "ripeness first, and contain the highest quantity of cannabinoids and terpenes. The two "
      "quantities decrease from the top to the bottom of the plant" +
      _c("namdar-2018-inflorescence-position") + ". Thus a harvest of all the plant at the same "
      "time harvests the top at the peak and the bottom before its correct time.</p><p>The "
      "alternative is the staggered harvest. First cut the top third of the plant when it is at "
      "full ripeness. Then give the bottom canopy 4&ndash;10 more days. The bottom canopy then has "
      "more light, and it increases in size and completes ripening. After this, cut the bottom "
      "canopy."),
    p("This method is correct because the bottom canopy gets light and time when you remove the "
      "tops. The bottom canopy did not have light and time before. Also, the plant continues to add "
      "weight in the last stage" + _c("massuela-2022-pruning-cbd-yield") + ".</p><p>The staggered "
      "harvest is a method for quality in small rooms and rooms of moderate size. It is not a "
      "method without a cost. The cost is in operations. You have two harvest days and two loads "
      "for the drying room. You use the room for a longer time. The remaining canopy has some more "
      "days with a risk of rot."),
    table(["Item", "Harvest of all the plant", "Staggered harvest (top first)"], [
      ["Ripeness of the bottom buds", "You cut the bottom buds some days before the correct time. There is more larf.", "The bottom buds complete ripening correctly. The grade is better."],
      ["Personnel and drying room", "One harvest, one load", "Two harvests, two loads"],
      ["Time to use the room again", "The shortest time", "More days in the room: 4-10"],
      ["Risk of rot", "The risk stops at the harvest", "The risk continues for the remaining plants. You must keep the RH in the target zone" + _c("punja2025-budrot-epi")],
      ["When it is the best method", "Large rooms, a short time for the harvest, and biomass for extraction", "Rooms for high quality with more days available and controlled RH"],
    ], cls="compact", caption="A staggered harvest gives better quality in the bottom canopy, but it uses more time and gives more days with a risk of rot. If the room cannot keep the RH in the target zone, do not do a staggered harvest."),
    callout("tip", "Do the second reading correctly",
      p("After you cut the top canopy, identify new positions on the remaining canopy. Start the "
        "loupe readings again at an interval of two days. The ripening of the bottom buds becomes "
        "faster in the new light. Frequently the bottom buds complete ripening in less time than "
        "the initial times show.</p><p>Keep the surfaces that you cut clean. Sanitize the shears "
        "between plants. Thus the first harvest does not cause an infection in the second harvest.")),
  ]})

# ---------------------------------------------------------------- 10 chop day
SECTIONS.append({"id": "day-of-chop", "kicker": "10 · Harvest day", "title": "Tasks for harvest day",
  "blocks": [
    p("On harvest day, the quality of the crop is complete. The only task is to prevent damage. "
      "Move the crop from the room to the drying room. Do not cause damage to the buds. Do not "
      "cause contamination of the buds. Do not let the buds stay in a bin.</p><p>You must select "
      "all the procedures below <em>before</em> you cut the first plant."),
    steps([
      ("Examine the drying room on the day before",
       "Make sure that the drying room operates and is stable at approximately 15–16 &deg;C (59–61 "
       "&deg;F) and approximately 60% RH (the usual 60/60). The room must have no light and a light "
       "airflow that does not point at the crop. The room must be clean and sanitized. Do not cut a "
       "plant before you make sure that the drying room is correct. A crop that waits in bins while "
       "you correct a fault in a dehumidifier has a risk of rot."),
      ("Last check for rot, then quarantine",
       "Before you cut, examine each plant with a light. Find these signs: botrytis, gray mold, "
       "buds with brown tissue in the inner part, and colas that divide when wet. Cut this material "
       "from the plant first. Put it in a bag at the plant. Remove the bag from the room. Do not "
       "move this material across the canopy or hang it with the clean crop."),
      ("Prepare the equipment",
       "Prepare these items: sanitized shears, gloves, and labels and tags for each plant or batch. "
       "Prepare bins or drying lines, and a scale for wet weights. Put the shears in sanitizer "
       "between plants. Select a wet trim or a dry trim before the harvest, and not in the middle "
       "of it. The procedure for a wet trim is different from the procedure for a dry trim. The "
       "difference starts when you cut the first plant."),
      ("Cut in the correct sequence",
       "Harvest one cultivar at a time. Thus the genetics do not mix. Select the method that agrees "
       "with your drying room: cut all the plant, or cut one branch at a time. Keep the plants off "
       "the floor and hold each plant only by the stem. Each time that you touch the flower, you "
       "remove trichomes."),
      ("Weigh the plants and record the wet weights",
       "Record the wet weight for each plant or bin. Connect each wet weight to the cultivar and "
       "the room position. The wet weights are the baseline for the dry-to-wet ratio (approximately "
       "10% dry-to-wet is usual) and the start of traceability."),
      ("Hang the plants with space",
       "The colas must not touch each other. The points where the colas touch dry more slowly, and "
       "rot starts there first. Put the same quantity of plants in each area of the drying room. "
       "Close the door. The environment does the work. After this step, use the <a "
       "href='harvest-dry-trim-cure.html'>paper about drying and curing</a>."),
    ]),
    p("Growers use two methods on harvest day, and no controlled test on cannabis shows that the "
      "methods are correct. The first method is <strong>48 hours of darkness before the "
      "harvest</strong>. Growers think that this method increases the resin. The second method is "
      "<strong>pre-dawn harvest</strong>. Growers think that this method keeps the peak quantity of "
      "terpenes.</p><p>No method causes damage. Cool conditions with no light and no stress are "
      "satisfactory for a plant that you will cut. But schedule the harvest for the time when your "
      "personnel are in good condition and the drying room is correct. These two items are "
      "important, and you can show this. The two methods above do not show an effect in tests."),
    callout("note", "The room after the harvest",
      p("The plants that you remove do not transpire in the room, and the humidity load decreases "
        "very quickly. The settings of the climate control are then not correct. If other plants "
        "stay in the room (staggered harvest or a room with plants of different ages), a check of "
        "the RH and the airflow is necessary again in one hour or less. Setpoints that are correct "
        "for a full canopy give different results in a canopy that is half empty.")),
  ]})

# ---------------------------------------------------------------- 11 failure modes
SECTIONS.append({"id": "failure-modes", "kicker": "11 · The faults", "title": "Usual faults in the last stage",
  "blocks": [
    p("Six faults cause almost all the errors in the last stage of flowering. Three faults are "
      "about the time of the harvest. Two faults are errors of reading. One fault is a risk that "
      "you do not monitor."),
    grid([
      card("A harvest before the correct time", "This fault is usual. The pistils are half white and most trichomes "
           "are clear, but the calendar shows week 8. The weight is less, because the plant adds "
           "weight in the last stage" + _c("massuela-2022-pruning-cbd-yield") +
           ", and the resin is not at maturity. To correct this, read the trichomes at the correct "
           "interval. Use the trend. Wait for the window.", tag="time"),
      card("Wait for amber heads", "This fault is the opposite fault. You wait for 20% amber on a cultivar "
           "that almost does not make amber heads. The heads collapse, and the risk of rot increases" +
           _c("punja-2023-trichome-maturation") + ". If the cloudy heads are at their maximum for "
           "one week and amber heads do not occur, this period is your window.", tag="reading"),
      card("A reading of the sugar leaves", "The trichomes on the leaves become amber some days before the "
           "trichomes on the calyx. If you read a leaf that has many trichomes, you harvest before "
           "the correct time each time. Read only the surface of the calyx, at mid-cola, at the "
           "same positions. Do not read other parts.", tag="reading"),
      card("Decision from the calendar", "The flowering time that a breeder gives is an average for the "
           "conditions of a different grower. The same clone has a difference of one week or more "
           "in different rooms. Use the number to schedule the personnel. Do not use the number to "
           "select the time to cut.", tag="time"),
      card("Pressure from mold that you do not monitor", "Each day that you add is a day with a risk of "
           "rot. The RH can become 65% at lights-off while you wait for full ripeness. Then all the "
           "cola is at risk, and you get only the last 3% of maturity" +
           _c("mahmoud-2023-botrytis-budrot") + ". If the room cannot keep the RH in the target "
           "zone, harvest before the end of the window. Keep the flower clean.", tag="risk"),
      card("A flush for too long", "A flush with only water for three weeks, &lsquo;to be safe&rsquo;, "
           "gives no feed to the plant while it adds weight in the last stage. The plant has a "
           "strong fade before the correct time. Blind panels cannot find a better smoke" +
           _c("rxgreen-2019-flushing-trial") + ". If you do a flush, keep it short.", tag="no test data"),
    ], cols=2),
  ]})

# ---------------------------------------------------------------- 12 troubleshooting
SECTIONS.append({"id": "troubleshooting", "kicker": "12 · Troubleshooting", "title": "Troubleshooting",
  "blocks": [
    p("Use this table to find the cause of a reading that is not usual. In most rows, the plant and "
      "the room do not agree with the calendar. Use the plant and not the calendar. Then correct "
      "the room."),
    table(["Sign", "Possible cause", "Correction"], [
      ["Week 9 or after: the trichomes are cloudy for some days, and amber does not occur",
       "A genotype that almost does not make amber heads. The heads will collapse.",
       "A long period at the maximum of cloudy heads is the window" + _c("punja-2023-trichome-maturation") + ". Do not wait for an amber color that some cultivars do not show."],
      ["All pistils are brown at week 6, but most trichomes are clear",
       "The stigmas are brown because of stress or pollen, and not because of ripeness",
       "Do not use the pistils. Continue to examine the trichomes. Examine the plants for seeds and for sources of heat and pollen."],
      ["New white pistils occur on buds in the last stage of ripening",
       "Foxtailing because of heat or light stress. The foxtailing starts bud growth again.",
       "Correct the hot areas. Decrease the PPFD. Read the first calyxes below the new growth. Do not read the new growth."],
      ["The trichomes on the sugar leaves are amber, and the trichomes on the calyxes are clear or cloudy",
       "Usual condition: the trichomes on the leaves become amber some days before the trichomes on the calyxes",
       "Read only the surface of the calyx. This difference is the cause of a harvest before the correct time when you read the leaves."],
      ["A strong fade with dry leaves by week 6, and the buds are not at maturity",
       "A flush for too long, a fast decrease of the nitrogen (N), or an EC in the root zone that collapses. Senescence started before the correct time.",
       "Apply a moderate feed again. You cannot correct some of the damage. For the next crop, decrease the EC slowly. Do not stop the feed." + _c("maillard-2015-leaf-nutrient-remobilization")],
      ["Gray mold or soft brown tissue in a cola while you wait for ripeness",
       "Botrytis bud rot. It starts in the inner part of the cola, where the RH spikes cause condensation.",
       "Cut the colas with infection from the plant immediately. Put the colas in a bag. Decrease the RH and increase the airflow. If the infection moves to other plants, harvest immediately." + _c("mahmoud-2023-botrytis-budrot")],
      ["The buds do not increase in size, and the trichomes do not change for one week or more",
       "The room is cold, the feed EC is very low, or the plant is at the end of ripening",
       "First examine the temperatures and the EC. If the room is correct and the trichomes are at the maximum of cloudy heads, the plant is in the window. Cut the plants."],
    ], cls="compact", caption="The last two rows are the dangerous rows. If the plant does not change but is clean, you only wait for more time. Botrytis can cause damage to all the crop."),
  ]})

# ---------------------------------------------------------------- 13 mental model
SECTIONS.append({"id": "mental-model", "kicker": "13 · The model", "title": "Ripeness variation and harvest decisions",
  "blocks": [
    p("If you use only one model from this paper for your first harvest, use this model:"),
    callout("key", "The distribution model",
      p("A plant does not have one &lsquo;ripeness&rsquo;. The plant has a very large number of "
        "trichomes in a vertical gradient. Each gland changes from clear &rarr; cloudy &rarr; "
        "amber, and the time is different for each gland" + _c("livingston-2020-trichome-maturation") +
        _c("namdar-2018-inflorescence-position") + ".</p><p>When you harvest, the distribution "
        "stops at that stage. You select the stage. A hash maker selects the stage with cloudy "
        "heads. A flower grower waits until the number of amber heads increases.</p><p>For biomass "
        "for extraction, the stage is not very important. Botrytis is the limit of time for all the "
        "distribution. Botrytis is the only signal that is more important than the loupe.")),
    p("All the other parts of this paper are this model and the procedures to apply it. The "
      "interval of the loupe readings gives a correct sample of the distribution. The product "
      "windows select the part that you want. The RH limit gives you the time to continue to wait. "
      "A staggered harvest harvests the gradient in two parts and does not use an average. A flush "
      "is not important, because no material that you apply to the substrate in the last week "
      "changes the color of the trichomes" + _c("rxgreen-2019-flushing-trial") +
      "."),
    kv([
      ("Reading interval", "Each 2 days from week 7, with a record"),
      ("Reading positions", "2-3 positions with a mark on the calyx at mid-cola, and one top cola"),
      ("Hash decision", "Maximum of cloudy heads, minimum of amber heads"),
      ("Flower decision", "Most heads cloudy, 5-15% amber"),
      ("RH zone / limit", "45-55% target, 58% maximum limit"),
      ("Drying room prepared", "15–16 &deg;C (59–61 &deg;F) / approximately 60% RH, in operation before you cut the first plant"),
    ]),
    p("After the harvest, you keep the quality of the crop, and you do not make it. The paper about "
      "<a href='harvest-dry-trim-cure.html'>harvest, drying, trimming and curing</a> gives the "
      "procedures for the next two weeks. The paper about <a href='mould-risk.html'>mold risk</a> "
      "is about the mold that goes with the crop into the drying room. Cut clean flower, and cut in "
      "the window. Let the loupe make the decision. Do not let the calendar or the forum make the "
      "decision."),
  ]})
