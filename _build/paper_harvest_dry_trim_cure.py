# -*- coding: utf-8 -*-
"""Paper: harvest, dry, trim and cure, the full post-harvest process (beginner)."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        stagecard, grid, card, chip, kv, steps)
import figs_lib as L

SLUG = "harvest-dry-trim-cure"
TITLE = "Harvest, drying, trimming and curing"
EYEBROW = "Post-harvest · Procedure"
SUB = ("This paper gives all the post-harvest steps, from the harvest of the plants to the sealed "
       "flower. It shows when to harvest the plants, how to dry the flower and keep the terpenes in "
       "it, and how to prevent mold. It also shows how to remove the leaves without damage to the "
       "trichomes, and how to do the curing until the water activity is stable. After you read this "
       "paper, you will know the target number for each step and a method that you can do again.")
META = [("scissors", "Post-harvest"), ("image", "9 diagrams"),
        ("quote", "4 sources"), ("clock", "~14 min to read")]
RELATED = ["mould-risk", "airflow-design", "nutrient-mixing-athena"]
REF_IDS = ["punja-2023-trichome-maturation", "birenboim-2024-cultivar-drying",
           "brikenstein-2024-trimming", "fairbairn-1976-light-stability",
           "astm-d8197-water-activity", "fda-water-activity-foods",
           "aqualab-microbial-water-activity", "aroya-drying-water-activity-guide"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

SECTIONS.append({"id": "intro", "kicker": "Start here", "title": "Purpose and scope",
  "blocks": [
    lead("Post-harvest is all the steps that you do after you cut the plant: drying, trimming, "
         "curing and storage. An error in these steps can cause damage to the results of many weeks "
         "of careful cultivation. The damage can occur in a small number of days. If you dry the "
         "flower too quickly or too much, the aroma and the weight decrease. If you dry the flower "
         "too slowly, or the flower is too wet, mold starts."),
    p("Keep the flower in a small safe zone. The flower must be sufficiently dry to prevent mold "
      "growth, but it must not be too dry. If the flower is too dry, the aroma and the weight "
      "decrease. A very dry flower has less mass for sale, but a correct control of this stage "
      "keeps this mass. Most growers dry the flower too much when they do not want to. Thus "
      "supplier figures show that the yield can increase by approximately 5 to 10%." +
      _c("aroya-drying-water-activity-guide")),
    figure(L.flow("The post-harvest steps, from start to end",
            [("Harvest", "cut plants at maturity"), ("Hang-dry", "60F / 60% RH, 10-14 days"),
             ("Takedown", "cut in sections at 0.60-0.62 aw"), ("Trim", "remove leaves, keep trichomes"),
             ("Cure, burp", "aw becomes 0.58-0.60"), ("Seal and keep", "stop burping, completed")],
            note="Each step has a target number. Drying has a room target. Curing has a flower target."), 1,
      "In these five steps, the plant becomes a completed product that is stable. The figure shows "
      "the target number for each step. The next sections give more information about each step."),
    callout("note", "Who this is for",
      p("This paper is for you if you do your initial harvest and want results that you can get "
        "again. It is not necessary to know the post-harvest procedure before you read this paper. "
        "The paper gives a definition of each term where you first read the term. You can use this "
        "paper with the <a href='mould-risk.html'>mold-risk</a> and <a "
        "href='airflow-design.html'>airflow-design</a> papers.")),
  ]})

SECTIONS.append({"id": "key-terms", "kicker": "The terms", "title": "Definitions",
  "blocks": [
    p("Two of these terms are the most important in this paper. It is not necessary to know the "
      "terms at this time. Each term occurs again in the next sections."),
    defterm("Water activity (aw)", "Water activity shows how available the water in the flower is, "
            "on a scale of 0 to 1.00. It is the best indicator of mold growth. Water can move "
            "between the flower and the air around it. When this movement stops, multiply the water "
            "activity by 100 to get the relative humidity of the air." + _c("fda-water-activity-foods")),
    defterm("Moisture content (%)", "The percentage of the total weight of the flower that is "
            "water. It gives information about the yield, but not about the safety. It is a "
            "different number from the water activity."),
    defterm("Relative humidity (RH)", "The quantity of water vapor in the air, from 0 to 100%. The "
            "target for the dry room is 60% RH."),
    defterm("Trichomes", "The glands of resin on the flower. They contain the THC, the terpenes and "
            "the flavonoids. Prevent damage to the trichomes in each step. If you touch the flower, "
            "you can remove trichomes from it."),
    defterm("Terpenes", "The oils that give each cultivar its aroma and flavor. They evaporate if "
            "the flower becomes too dry."),
    defterm("Burping", "A short opening of a sealed container during curing. The opening lets moist "
            "air go out of the container and lets new air go into it."),
    figure(L.flow("Two numbers about water that have different tasks",
            [("Water activity", "0-1.00 scale · shows MOLD risk · controls the procedure"),
             ("Moisture content", "% of weight · shows YIELD · measures the product")],
            note="Water activity shows when the flower is safe and completed. Moisture content shows how much you have."), 2,
      "Water activity is the number that you use to control the procedure. Moisture content is the "
      "number that you give in a report. A frequent error of new growers is to use one number for "
      "the task of the other number." + _c("aroya-drying-water-activity-guide")),
  ]})

SECTIONS.append({"id": "harvest-timing", "kicker": "Step 1, the information", "title": "Harvest timing",
  "blocks": [
    p("Harvest is the procedure in which you cut all the plants after they complete the flowering. "
      "Examine the flower to find the maturity of the plants. Do not use the date on the calendar."),
    p("The trichomes are the best signal of maturity. Examine the trichomes with a loupe. They are "
      "first transparent, then cloudy, then amber when the maturity increases. The change of color "
      "shows the maturity of the resin glands." + _c("punja-2023-trichome-maturation") +
      " A usual procedure uses a set time for the flowering, with plant-work stages at days 7 to "
      "10, 21 to 28 and 42 to 49. At the end, you cut the plants."),
    ul(["Harvest is the procedure in which you cut all the plants after they complete the flowering.",
        "Cut one cultivar at a time, in the sequence on your list of cultivars. Thus the cultivars do not mix.",
        "Keep the tag of each plant attached when you cut the plant. The tag gives traceability of the batches.",
        "Collect the loose buds that fall on the table. Put a label on the buds of each cultivar and dry them independently."]),
    figure(L.line("Harvest is the end of a specified flowering cycle",
            [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)],
            ["trellis d1", "lollipopping d7-10", "defanning d21-28", "last defanning d42-49", "harvest"],
            ylab="plant-work stage", note="Each stage is a task with a set time. Harvest is the last task."), 3,
      "Harvest is the end of a set sequence of plant-work stages in the flowering room."),
    callout("tip", "Use the plant for the decision",
      p("If the calendar shows that you must cut the plants, but most of the trichomes are "
        "transparent, wait. Examine the flower to find the maturity. The date gives only an "
        "approximate indication.")),
  ]})

SECTIONS.append({"id": "harvest-method", "kicker": "Step 2, the procedure", "title": "Harvest method and wet-plant weighing",
  "blocks": [
    p("Cut each whole plant and hang it to dry. Do not remove the buds from the plant first. "
      "Release each plant from the bottom two layers of the trellis net (the net that holds the "
      "plant). Keep the top layer on the plant. The layer holds the plant. Then cut the primary "
      "stalk at the bottom."),
    p("Before you hang the plants, weigh each bin to record the <strong>wet weight</strong>. The "
      "wet weight is the initial weight. After the drying, compare the wet weight with the last dry "
      "weight. Thus you get the dry-to-wet ratio for each cultivar. The dry-to-wet ratio is "
      "approximately 10% of the wet weight of the whole plant (one example batch gave 10.46%). It "
      "shows how much of the mass of the harvested plants is water."),
    steps([
      ("Release the plant", "Cut around the plant through the bottom and middle layers of the trellis net. Keep the top layer attached to hold the plant."),
      ("Cut the stalk", "Cut the primary stalk at the bottom. Then you can remove the plant in one piece."),
      ("Fill the bin", "Put 7 to 10 whole plants in each bin of 208 L (55 gal). Do not put too many plants in the bin. Too many plants cause damage to the flower."),
      ("Weigh the wet plants", "Set the scale to zero when the empty bin is on it. Then weigh the bin with the plants to record the wet weight. The wet weight is the baseline for all the yield records."),
    ]),
    figure(L.bars("Water in the plant when you cut it",
            [("Wet weight", 100), ("Dry weight", 10.46)], unit="%",
            note="Example batch: dry weight was approximately 10.46% of wet weight. The remaining weight was water."), 4,
      "Approximately 90% of the weight of a plant when you cut it is water. The water must move out "
      "of the plant during the drying. When you hang the whole plant, the water moves out more "
      "slowly, and the moisture moves out of the stem at the same rate."),
  ]})

SECTIONS.append({"id": "drying", "kicker": "The primary information", "title": "Drying environment",
  "blocks": [
    p("Keep the dry room at 16 °C (60 °F) and 60% RH, with the fans on and the lights off. Clean "
      "the room fully before you put the plants in it. At these setpoints, the takedown of whole "
      "plants is usually possible after 10 to 14 days." + _c("aroya-drying-water-activity-guide")),
    p("Slow drying in a cool room keeps the terpenes. Terpenes evaporate in heat and in dry air. "
      "Slow drying also prevents the condition where the outer part of the bud is dry and the inner "
      "part stays wet. This condition is the usual cause of mold in the bud that you cannot "
      "see.</p><p>Keep the light off, because light causes the degradation of cannabinoids and "
      "terpenes with time." + _c("fairbairn-1976-light-stability") + " The best drying method can "
      "have small differences for different cultivars. Thus the setpoints are a good start point, "
      "but they are not correct for all cultivars." + _c("birenboim-2024-cultivar-drying")),
    ul(["Setpoints: 16 °C (60 °F), 60% RH, fans on, lights off, doors closed. Keep the number of persons that go into the room as small as possible. Thus the environment stays stable.",
        "The drying of whole plants is approximately 10 to 14 days at these setpoints.",
        "If the RH in the room is more than 60% and the dehumidification is too small, exhaust fans can decrease the humidity.",
        "Keep an equal space between the racks. Thus the air flows to each plant and the buds dry at the same rate. Clean the room fully before each load."]),
    figure(L.line("The humidity in the dry room decreases until the takedown",
            [(0, 64), (1, 62), (2, 61), (3, 60), (4, 60), (5, 59)],
            ["day 0", "day 3", "day 5", "day 8", "day 11", "day 14"],
            ylab="room RH %", ymin=52, ymax=68,
            bands=[(59, 61, L.GL, "target 60% RH"), (61, 68, L.REDL, "high humidity: mold risk"), (52, 59, L.AMBL, "too dry: terpenes evaporate")],
            note="Keep the room in the green zone. The curve decreases when the load dries."), 5,
      "The green zone is the target of 60% RH. If the RH increases to a value more than the green "
      "zone, the risk of mold increases. If the RH stays less than the green zone for a long time, "
      "the terpenes start to evaporate." + _c("aroya-drying-water-activity-guide")),
  ]})

SECTIONS.append({"id": "water-activity", "kicker": "The primary information", "title": "Water activity",
  "blocks": [
    p("After the hang-dry, some moisture stays in the flower. Some moisture is more dangerous than "
      "other moisture. The plant material holds some of the water in its inner part, and this water "
      "is not dangerous. The free water at the surface is the water that microbes use.</p><p>Water "
      "activity (aw) shows how available the remaining moisture is to microbes, on a scale of 0 to "
      "1.00. Mold and yeast can increase in number at 0.70 aw and higher. Bacteria that cause "
      "disease can increase in number at 0.85 aw. The risk increases quickly near these thresholds. "
      "If the aw is less than approximately 0.55, the quality frequently decreases, although the "
      "growth of microbes becomes slower. The ASTM range of 0.55 to 0.65 is the target for dry "
      "flower." + _c("aqualab-microbial-water-activity") + "</p><p>The growth of microbes gives the "
      "maximum value of this range. Quality gives the minimum value. If the aw is less than 0.55, "
      "the terpenes evaporate and the quality decreases."),
    p("These two limits give a range of 0.55 to 0.65 aw. This range is the same as the range in the "
      "ASTM D8197 standard for dry cannabis flower." + _c("astm-d8197-water-activity") +
      " Start the testing of samples at approximately day 7 to 8. The takedown is the removal of "
      "the plants from the racks. Do the takedown when the average aw of the batch is 0.60 to 0.62. "
      "Thus there is headroom to the 0.65 mold limit."),
    figure(L.zones("Safe zone of water activity", 0.50, 0.90,
            [(0.50, 0.55, L.AMBL, "too dry"), (0.55, 0.65, L.GL, "takedown at 0.60-0.62"),
             (0.70, 0.85, L.REDL, "mold and yeast"), (0.85, 0.90, L.RED, "bacteria")],
            note="Do the takedown in the green zone, at approximately 0.60-0.62 aw, with headroom to the 0.65 mold limit."), 6,
      "If the aw is less than 0.55, the terpenes evaporate. If the aw is more than 0.65, there is a "
      "risk of mold. The takedown of the batch is at 0.60 to 0.62 aw." + _c("astm-d8197-water-activity")),
    figure(L.bars("Water activity thresholds for microbe growth",
            [("No growth", 0.60), ("Mold and yeast", 0.70), ("Bacteria", 0.85)], unit=" aw",
            target=0.62, maxv=0.95,
            note="The takedown target (0.62 aw) is less than each growth threshold. The difference is the headroom."), 7,
      "Decrease the aw of the batch to a value less than the 0.70 aw mold limit. The takedown "
      "target of 0.62 aw gives headroom." + _c("aqualab-microbial-water-activity")),
    callout("key", "Water activity is better than a low-cost moisture meter",
      ul(["Water activity is the better number for control, because it has much less variation than the readings of a low-cost moisture meter.",
          "In one example, the measurement of water activity gave a yield precision that was approximately 10 times better (from &plusmn;1% to &plusmn;0.12%).",
          "Flowers with a high density usually have a lower aw at the end of the drying than flowers with a low density. The difference is small. Use the meter as an indication, and also smell the flower."], "tight")),
  ]})

SECTIONS.append({"id": "trimming", "kicker": "Step 3, the procedure", "title": "Trimming and trichome protection",
  "blocks": [
    p("Trimming removes the leaves from the bud, and thus the bud is clean. There are two times for "
      "the trimming. <strong>Wet trim</strong> is the trimming immediately after you cut the "
      "plants, before the drying. <strong>Dry trim</strong> is the trimming after the hang-dry. A "
      "dry trim makes the drying slower, and it causes less damage to the oils that give the aroma. "
      "Thus many facilities select a dry trim to keep more of the terpenes." +
      _c("brikenstein-2024-trimming")),
    p("Do not touch the flower. If you touch the flower, you remove the trichomes that contain the "
      "potency and the aroma. Then the buds have a smooth, matt surface.</p><p>To do a dry trim, do "
      "the takedown. Then cut the plants into sections of 20 to 30 cm (8 to 12 in). Remove the "
      "large fan leaves with your hands. Then cut the smaller sugar leaves with scissors. When "
      "resin collects on the scissors, clean them in 71% alcohol."),
    ul(["<strong>Bucking</strong> is the procedure in which you cut the buds from the stem after the trimming. Do the bucking into a sealed bag. Thus the flower does not become too dry in open air.",
        "Do not touch the flower. If you touch the flower, you cause damage to the trichomes.",
        "Remove the fan leaves with your hands (large leaves with a small number of trichomes). Then cut the sugar leaves with scissors.",
        "When resin collects on the scissors, clean the scissors in 71% alcohol.",
        "After a dry trim, measure the aw again. If you touch the flower and remove the leaves, the reading can change. Thus do not think that the aw from the hang-dry is correct."]),
    table(["", "Wet trim", "Dry trim (this paper)"], [
      ["Time", "Directly after you cut the plants", "After the hang-dry of 10 to 14 days"],
      ["Drying speed", "Faster, with more damage to the flower", "Slower, with less damage to the flower"],
      ["Leaf removal", "Easier (the leaf is soft)", "The leaf breaks easily. You must be more careful."],
      ["Terpenes that you keep", "Lower (you touch the flower more, and the drying is faster)", "Higher. Thus growers select a dry trim."],
      ["Risk of damage when you touch the flower", "More", "Less"],
    ], cls="compact", caption="Wet trim compared with dry trim. This paper uses a dry trim, because it keeps more terpenes and the drying causes less damage." + _c("brikenstein-2024-trimming")),
  ]})

SECTIONS.append({"id": "curing", "kicker": "The primary information", "title": "Curing and storage",
  "blocks": [
    p("Curing makes the water activity the same in all the flower of the batch. It also keeps the "
      "terpenes. Without curing, there can be degradation of the terpenes in storage.</p><p>Keep "
      "the flower in containers at 16 to 18 °C (60 to 65 °F) and 58 to 62% RH. Read the humidity "
      "sensor. When the reading of a bin is more than approximately 60% RH, <strong>burp</strong> "
      "the bin. Remove the lid for 5 to 10 minutes. Then turn the barrel. Record the reading."),
    p("When the flower after the trimming is at 0.58-0.60 aw, you complete the curing. Seal the "
      "flower. Stop the burping. More burping only makes the terpenes and the water evaporate. Thus "
      "the aroma and the weight for sale decrease.</p><p>Curing also keeps the cannabinoids more "
      "stable, because you keep the product at a low temperature and without light. These "
      "conditions decrease the speed of the degradation during storage." +
      _c("fairbairn-1976-light-stability")),
    figure(L.flow("The burp decision each day",
            [("Read sensor", "measure bin humidity"), ("More than 60% RH?", "if yes, burp 5-10 min"),
             ("Turn, record", "turn barrel, record date/RH/bin"), ("At 0.58-0.60 aw?", "if yes, seal, stop burping")],
            note="Do the steps each day until the aw is 0.58-0.60. Then seal and keep it."), 8,
      "Burp the bin while the flower is wet. Turn the barrel to dry the flower at the same rate. "
      "Record each burp. Stop when the flower is at 0.58-0.60 aw."),
    callout("warn", "Too many burps decrease the weight for sale",
      p("When the flower after the trimming is at 0.58-0.60 aw, seal it. Each burp after this point "
        "makes the terpenes and the water evaporate. As a result, the aroma and the weight for sale "
        "decrease. Remove the air from the bags, but do not compress the flower. Do not put bags on "
        "top of other bags. Thus there is no damage to the structure of the buds.")),
  ]})

SECTIONS.append({"id": "pitfalls", "kicker": "When there is a problem", "title": "Troubleshooting",
  "blocks": [
    p("Most post-harvest problems have one of three causes: the drying is too fast, the flower is "
      "too dry, or the space is too full. Too much drying can cause damage that you do not see. A "
      "low-cost moisture meter with an error of &plusmn;1% can show a reading of &lsquo;11% "
      "moisture&rsquo;. At this reading, the aw of the flower can be from 0.53 aw (too dry, with "
      "damage to the flower) to 0.66 aw (mold risk). Thus growers who use one number frequently dry "
      "the flower too much, and the weight and the aroma decrease." + _c("astm-d8197-water-activity")),
    figure(L.bars("One '11% moisture' reading does not show the aw",
            [("Meter low", 0.53), ("Meter high", 0.66), ("aw reading low", 0.617), ("aw reading high", 0.623)],
            unit=" aw", maxv=0.80,
            note="A meter with +/-1% error gives an aw from 0.53 (too dry) to 0.66 (mold). A water activity reading gives only 0.617 to 0.623."), 9,
      "The same reading of &lsquo;11% moisture&rsquo; can show a flower that is too dry and has "
      "damage, or a flower with a risk of mold. Water activity makes this range very small." +
      _c("astm-d8197-water-activity")),
    table(["Error", "Result", "Correction"], [
      ["Too much drying, to less than 0.55 aw", "The terpenes evaporate, the aroma decreases and the weight of water decreases", "Do the takedown at 0.60-0.62 aw. Stop the curing at 0.58-0.60 aw."],
      ["Drying that is too hot or too fast", "The outer part becomes dry and the inner part stays wet. Mold can start in the inner part, and you cannot see it.", "Keep 16 °C (60 °F) and 60% RH. Let the plants dry for 10 to 14 days."],
      ["You use only a low-cost moisture meter for the decision", "An error of &plusmn;1% gives 0.53-0.66 aw, from too dry to a risk of mold.", "Use a water activity test to find when you can complete the procedure."],
      ["Containers that are too full", "The weight compresses the buds, and the moisture cannot move out of them.", "Fill totes and barrels to a maximum of approximately 2/3. Fill curing barrels to a maximum of half."],
      ["You touch the flower, or you do not clean the room fully", "You remove trichomes from the flower, and there is contamination.", "Touch only the stem. Clean the room fully before each load."],
      ["The aw is safe, but you smell that the flower is wet", "The inner part is not dry", "Let the flower dry more. Smell the flower and feel it for the last check."],
    ], cls="compact", caption="The six primary post-harvest errors and their corrections."),
  ]})

SECTIONS.append({"id": "expectations", "kicker": "Typical results", "title": "Expected results and limitations",
  "blocks": [
    p("The hang-dry is approximately 10 to 14 days, and the curing is some more days. After the "
      "curing, the flower is a completed product. All of the post-harvest stage is two to three "
      "weeks. It is not fast, and you cannot make it faster."),
    figure(L.line("The end of the post-harvest stage, day by day",
            [(0, 0.85), (1, 0.72), (2, 0.62), (3, 0.59), (4, 0.59)],
            ["harvest d0", "test d7-8", "takedown d10-14", "trim, cure", "sealed"],
            ylab="aw", ymin=0.50, ymax=0.90,
            bands=[(0.55, 0.65, L.GL, "safe zone 0.55-0.65 aw")],
            note="Testing starts near day 7-8. Takedown is near day 10-14, at 0.60-0.62 aw. Cure to 0.58-0.60 aw, then seal."), 10,
      "A typical curve shows the water activity. It decreases from the harvest, moves into the safe "
      "zone at the takedown, and becomes stable in the curing before you seal the batch." +
      _c("astm-d8197-water-activity")),
    callout("key", "Three primary items",
      ol(["<strong>The post-harvest stage is weeks, not days.</strong> Use two to three weeks for the stage. Do not make the drying faster.",
          "<strong>Do not dry the flower too much.</strong> If you control the drying and the curing correctly, you keep the weight for sale. The figures of approximately 5 to 10% from suppliers are only examples." + _c("aroya-drying-water-activity-guide"),
          "<strong>The cultivar is important.</strong> The drying and the curing are different for each cultivar. Flowers with a high density and flowers with a low density have a different aw at the end. The difference is small. Thus record each batch." + _c("birenboim-2024-cultivar-drying")])),
    p("Record the aw, the RH, the dates and the results for each cultivar. Thus you can get good "
      "results again. The instrument gives an indication and does not make the decision. In the "
      "safe aw zone, smell the flower and feel it to make the last decision. Read the <a "
      "href='mould-risk.html'>mold-risk</a> paper for the procedure if the aw of a batch is more "
      "than the mold limit. Read the <a href='nutrient-mixing-athena.html'>nutrient-mixing</a> "
      "paper for the feed, which has an effect on the quality."),
  ]})
