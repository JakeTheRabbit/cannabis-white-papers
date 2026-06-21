# -*- coding: utf-8 -*-
"""Paper: harvest, dry, trim and cure, the full post-harvest process (beginner)."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        stagecard, grid, card, chip, kv, steps)
import figs_lib as L

SLUG = "harvest-dry-trim-cure"
TITLE = "Harvest, dry, trim and cure"
EYEBROW = "Post-harvest · Process"
SUB = ("A beginner's guide to the full post-harvest process: when to cut, how to dry, "
       "how to trim, and how to cure flower so it is safe from mould and keeps its smell, "
       "weight and quality.")
META = [("scissors", "Post-harvest"), ("image", "9 figures"),
        ("quote", "Peer-reviewed · 4 sources"), ("clock", "~14 min read")]
RELATED = ["mould-risk", "airflow-design", "nutrient-mixing-athena"]
REF_IDS = ["punja-2023-trichome-maturation", "birenboim-2024-cultivar-drying",
           "brikenstein-2024-trimming", "fairbairn-1976-light-stability",
           "astm-d8197-water-activity", "fda-water-activity-foods",
           "aqualab-microbial-water-activity", "aroya-drying-water-activity-guide"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

SECTIONS.append({"id": "intro", "kicker": "Start here", "title": "Why the last two weeks decide everything",
  "blocks": [
    lead("Post-harvest is everything that happens after the plant is cut down: drying, trimming, "
         "curing and storage. Weeks of careful growing can be ruined in a few days here. Dry too "
         "fast or too dry and you lose smell and weight. Dry too slow or too wet and mould takes hold."),
    p("Aim for a narrow safe zone: dry enough that mould cannot grow, but not so dry that the smell "
      "and weight evaporate away. Done well, simply dialling in this stage is reported to add 5-10% "
      "to final yield, because most growers are accidentally over-drying and "
      "losing sellable weight." + _c("aroya-drying-water-activity-guide")),
    figure(L.flow("The post-harvest pipeline, start to finish",
            [("Harvest", "cut plants at maturity"), ("Hang dry", "60F / 60% RH, 10-14 days"),
             ("Takedown", "section at 0.60-0.62 aw"), ("Trim", "remove leaf, save trichomes"),
             ("Cure & burp", "settle to 0.58-0.60 aw"), ("Seal & store", "stop burping, finished")],
            note="Each step has a target number. Drying aims for the room, curing aims for the flower."), 1,
      "The five steps that turn a living plant into a finished, stable product. The numbers on each "
      "box are what you steer toward, explained section by section below."),
    callout("note", "Who this is for",
      p("Anyone harvesting their first crop who wants results they can repeat. This guide assumes "
        "zero prior knowledge and defines every term as it appears. It pairs with the "
        "<a href='mould-risk.html'>mould-risk</a> and "
        "<a href='airflow-design.html'>airflow-design</a> papers.")),
  ]})

SECTIONS.append({"id": "key-terms", "kicker": "Vocabulary", "title": "The words you need before we start",
  "blocks": [
    p("Two ideas do most of the work in this guide. Don't memorise them. Each one comes back "
      "in context."),
    defterm("Water activity (aw)", "How &lsquo;available&rsquo; the water in the flower is, on a 0 "
            "to 1.00 scale. It is the single best predictor of whether mould will grow. When the "
            "flower and the air around it reach balance, the air's relative humidity equals water "
            "activity times 100." + _c("fda-water-activity-foods")),
    defterm("Moisture content (%)", "The share of the flower's total weight that is water. This "
            "tells you about yield, not safety. It is a different number from water activity."),
    defterm("Relative humidity (RH)", "How much water vapour is in the air, from 0 to 100%. The "
            "dry-room target is 60% RH."),
    defterm("Trichomes", "The frosty resin glands on the flower that hold the THC, terpenes and "
            "flavonoids. Protect these at every step. Handling knocks them off."),
    defterm("Terpenes", "The aromatic oils that give each strain its smell and flavour. They "
            "evaporate if the flower gets too dry."),
    defterm("Burping", "Briefly opening a sealed container during curing to let humid air out and "
            "fresh air in."),
    figure(L.flow("Two numbers that sound alike but do different jobs",
            [("Water activity", "0-1.00 scale · predicts MOULD · controls the process"),
             ("Moisture content", "% of weight · predicts YIELD · measures the product")],
            note="Water activity tells you when it is safe and done. Moisture content tells you how much you have."), 2,
      "Water activity is the gauge you steer by. Moisture content is the gauge you report. Confusing "
      "the two is the most common beginner mistake." + _c("aroya-drying-water-activity-guide")),
  ]})

SECTIONS.append({"id": "harvest-timing", "kicker": "Step 1 of the science", "title": "When to harvest: reading the plant, not the calendar",
  "blocks": [
    p("Harvest is cutting the plants down once they have finished flowering. Judge maturity by the "
      "flower itself, not by a date on the calendar."),
    p("The clearest signal is the trichomes. Under a loupe they shift from clear, to milky-cloudy, "
      "to amber as the plant ripens, and that colour change tracks how mature the resin glands "
      "are." + _c("punja-2023-trichome-maturation") + " A typical workflow runs plants on a set "
      "flowering timeline with plant-work phases at days 7-10, 21-28 and 42-49, then cuts at the end."),
    ul(["Harvest = cutting down all plants once flowering is complete",
        "Cut one strain at a time, in the order on your strain list, so genetics never get mixed",
        "Keep each plant's tracking tag attached as it is cut. This is how batches stay traceable",
        "Collect loose buds that fall on the table (&lsquo;table nugs&rsquo;) per strain, label them, and dry them separately"]),
    figure(L.line("Harvest is the end of a defined flowering cycle",
            [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)],
            ["trellis d1", "lollipop d7-10", "defan d21-28", "final defan d42-49", "harvest"],
            ylab="plant-work stage", note="Each milestone is a scheduled task. Harvest is the last one."), 3,
      "Harvest is not a surprise. It is the planned end of a sequence of plant-work milestones "
      "across the flowering room."),
    callout("tip", "Let the plant decide",
      p("If the calendar says cut but the trichomes are still mostly clear, wait. Read maturity "
        "off the flower. The date is only a rough guide.")),
  ]})

SECTIONS.append({"id": "harvest-method", "kicker": "Step 2, hands on", "title": "Cutting down and weighing the wet plant",
  "blocks": [
    p("Cut plants whole and hang them to dry, rather than stripping the buds first. Cutters free each "
      "plant from the lower two layers of trellis netting (the support grid the plant grew through), "
      "leave the top layer on for support, then cut the main stalk at its base."),
    p("Before anything is hung, weigh every bin to record the <strong>wet weight</strong>, the "
      "starting weight. Compared against the final dry weight later, this gives the "
      "dry-to-wet ratio for each genetic, which lands around 10% in practice (a real example batch "
      "came in at 10.46%). That tells you how much of the harvested mass is water."),
    steps([
      ("Free the plant", "Cut a circle through the bottom and middle trellis layers. Leave the top layer attached for support."),
      ("Cut the stalk", "Sever the main stalk at its base so the whole plant comes away in one piece."),
      ("Load the bin", "Place 7-10 whole plants per 55-gallon bin. Do not overfill or you bruise the flower."),
      ("Weigh wet", "Tare the bin first, then weigh it to capture wet weight, the baseline for all yield tracking."),
    ]),
    figure(L.bars("How much of a fresh plant is water",
            [("Wet weight", 100), ("Dry weight", 10.46)], unit="%",
            note="Example batch: dry weight was ~10.46% of wet weight. The rest left as water during drying."), 4,
      "Roughly nine-tenths of a freshly cut plant's weight is water that must leave during drying. "
      "Whole-plant hanging slows that loss and lets moisture move out of the stem evenly."),
  ]})

SECTIONS.append({"id": "drying", "kicker": "The core science", "title": "The drying environment: slow, cool, dark, moving air",
  "blocks": [
    p("Hold the dry room at 60&deg;F and 60% RH, with fans running and the lights off, in a room "
      "that was deep-cleaned before any plant went in. At these setpoints whole plants are typically "
      "ready in 10-14 days." + _c("aroya-drying-water-activity-guide")),
    p("Going slow and cool protects the terpenes, which evaporate in heat and dry air, and it stops "
      "the outside of the bud drying while the inside stays wet, the classic recipe for hidden "
      "mould. Keep the light off because it degrades cannabinoids and terpenes over time." + _c("fairbairn-1976-light-stability") +
      " Different cultivars even reward slightly different drying approaches, so the setpoints are a "
      "strong default, not a law." + _c("birenboim-2024-cultivar-drying")),
    ul(["Setpoints: 60&deg;F, 60% RH, fans on, lights off, doors closed. Minimise foot traffic so the environment stays stable",
        "Whole-plant drying takes about 10-14 days at these setpoints",
        "If the room runs above 60% RH and dehumidification is undersized, exhaust fans can pull humidity down",
        "Keep racks evenly spaced so air reaches every plant and buds dry uniformly. A deep clean precedes every load"]),
    figure(L.line("Dry-room humidity should trend down toward takedown",
            [(0, 64), (1, 62), (2, 61), (3, 60), (4, 60), (5, 59)],
            ["day 0", "day 3", "day 5", "day 8", "day 11", "day 14"],
            ylab="room RH %", ymin=52, ymax=68,
            bands=[(59, 61, L.GL, "target 60% RH"), (61, 68, L.REDL, "too humid: mould risk"), (52, 59, L.AMBL, "too dry: terpene loss")],
            note="Hold the room in the green band. The curve drifts down as the load gives up water."), 5,
      "The green band is the 60% RH target. Drift above it and you invite mould. Sit below it for long "
      "and terpenes start to evaporate." + _c("aroya-drying-water-activity-guide")),
  ]})

SECTIONS.append({"id": "water-activity", "kicker": "The core science", "title": "Water activity: the number that controls mould and yield",
  "blocks": [
    p("Water activity is the safe-zone gauge for cannabis. Mould and yeast can grow at 0.70 aw and "
      "above, pathogenic bacteria at 0.85, and essentially nothing grows below about 0.60 aw." + _c("aqualab-microbial-water-activity") +
      " That sets the ceiling. Quality sets the floor: below 0.55 aw the terpenes dry up and quality "
      "falls off."),
    p("Together that leaves a sweet spot of 0.55-0.65 aw, the exact range written into the "
      "ASTM D8197 standard for dry cannabis flower." + _c("astm-d8197-water-activity") + " Start "
      "sample testing around day 7-8, and take plants down when the batch averages 0.60-0.62 aw, "
      "leaving a safety margin below the 0.65 mould line."),
    figure(L.zones("The water-activity safe zone", 0.50, 0.90,
            [(0.50, 0.55, L.AMBL, "too dry"), (0.55, 0.65, L.GL, "sweet spot 0.60-0.62 = take down"),
             (0.70, 0.85, L.REDL, "mould & yeast"), (0.85, 0.90, L.RED, "bacteria")],
            note="Take plants down inside the green band, around 0.60-0.62 aw, well clear of the 0.65 mould line."), 6,
      "Below 0.55 aw you lose terpenes. Above 0.65 aw you risk mould. 0.60-0.62 aw is where you take "
      "the batch down." + _c("astm-d8197-water-activity")),
    figure(L.bars("Water activity thresholds for microbial growth",
            [("No growth", 0.60), ("Mould & yeast", 0.70), ("Bacteria", 0.85)], unit=" aw",
            target=0.62, maxv=0.95,
            note="Take-down target (0.62 aw) sits below every growth threshold. That gap is your safety margin."), 7,
      "Drop the batch below the 0.70 aw mould line, with the take-down target at 0.62 aw giving "
      "headroom." + _c("aqualab-microbial-water-activity")),
    callout("key", "Why water activity beats a cheap moisture meter",
      ul(["Water activity is the better control number because it varies far less than cheap moisture readings.",
          "In one example, measuring on water activity gave roughly 10x tighter yield precision (&plusmn;1% down to &plusmn;0.12%).",
          "Denser flowers tend to finish at a slightly lower aw than fluffy ones. Use the meter as a guide, but also trust your nose."], "tight")),
  ]})

SECTIONS.append({"id": "trimming", "kicker": "Step 3, hands on", "title": "Trimming: wet vs dry, and protecting the trichomes",
  "blocks": [
    p("Trimming removes leaf so the bud looks clean and presentable. There are two timings. "
      "<strong>Wet trim</strong> means trimming right after cutting, before drying. <strong>Dry "
      "trim</strong> means trimming after the hang-dry. Dry trimming slows the dry and is gentler "
      "on the aromatic oils, which is why many operations choose it for better terpene "
      "retention." + _c("brikenstein-2024-trimming")),
    p("Never touch the flower itself. Handling knocks off the trichomes that "
      "carry potency and smell, leaving buds looking shaved and dull. To dry-trim, take plants down, "
      "cut them into 8-12 inch sections, remove the large fan leaves by hand, then scissor off the "
      "smaller sugar leaves, swapping scissors into 71% alcohol as resin builds up."),
    ul(["<strong>Buck</strong> = cut the finished buds off the stem. Do this into a sealed bag so the flower does not over-dry in open air",
        "Never touch the flower. Handling damages trichomes",
        "Remove fan leaves (large, few trichomes) by hand, then scissor off sugar leaves",
        "Clean scissors in 71% alcohol when resin builds up",
        "Trimming itself lowers water activity, so flower that took down at 0.62 aw often reads 0.58-0.60 aw once trimmed"]),
    table(["", "Wet trim", "Dry trim (this guide)"], [
      ["When", "Right after cutting", "After the 10-14 day hang-dry"],
      ["Drying speed", "Faster, harsher", "Slower, gentler"],
      ["Leaf removal", "Easier (leaf is soft)", "Leaf is brittle, more care needed"],
      ["Terpene retention", "Lower (more handling, faster dry)", "Higher, the reason it is chosen"],
      ["Handling risk", "More", "Less"],
    ], cls="compact", caption="Wet vs dry trim. This guide dry-trims for better terpene retention and a gentler dry." + _c("brikenstein-2024-trimming")),
  ]})

SECTIONS.append({"id": "curing", "kicker": "The core science", "title": "Curing and storage: burp, stabilise, then seal",
  "blocks": [
    p("Curing lets the whole batch settle to one even water activity, and preserves terpenes that "
      "would otherwise break down in storage. Hold flower in containers at 60-65&deg;F and "
      "58-62% RH. Read a humidity sensor, and <strong>burp</strong> any bin reading above about "
      "60% RH: lid off for 5-10 minutes, then rotate the barrel "
      "and log the reading."),
    p("Once the trimmed flower sits at 0.58-0.60 aw, it is finished: seal it and stop burping. "
      "Further burping just evaporates terpenes (lost smell) and water (lost sellable weight). "
      "Curing also keeps cannabinoids more stable by keeping the product cool and dark, the same "
      "conditions that slow degradation during storage." + _c("fairbairn-1976-light-stability")),
    figure(L.flow("The daily burp decision",
            [("Read sensor", "check bin humidity"), ("Above 60% RH?", "yes -> burp 5-10 min"),
             ("Rotate & log", "turn barrel, record date/RH/bin"), ("At 0.58-0.60 aw?", "yes -> seal, stop burping")],
            note="Loop daily until the flower holds 0.58-0.60 aw, then seal and store."), 8,
      "Burp while wet, rotate for even drying, log every time, and stop the moment the flower reaches "
      "0.58-0.60 aw."),
    callout("warn", "Over-burping costs you money",
      p("Every burp past the finish line evaporates terpenes and water weight you could have sold. "
        "When trimmed flower reaches 0.58-0.60 aw, seal it. Bags should be free of air but not "
        "compressed, and not stacked, to protect bud structure.")),
  ]})

SECTIONS.append({"id": "pitfalls", "kicker": "What goes wrong", "title": "Common mistakes and how to avoid them",
  "blocks": [
    p("Most post-harvest failures are variations on going too fast, too dry, or too crowded. "
      "Over-drying is the quiet killer. A cheap moisture meter with &plusmn;1% error can read "
      "&lsquo;11% moisture&rsquo; while the flower is anywhere from 0.53 aw (ruined, too dry) to "
      "0.66 aw (mould risk), so growers chasing a single number often dry too far and lose weight "
      "and smell." + _c("astm-d8197-water-activity")),
    figure(L.bars("What a single '11% moisture' reading actually hides",
            [("Cheap meter low", 0.53), ("Cheap meter high", 0.66), ("aw reading low", 0.617), ("aw reading high", 0.623)],
            unit=" aw", maxv=0.80,
            note="A +/-1% moisture meter spans 0.53 (too dry) to 0.66 (mould). A water-activity reading pins it to a 0.617-0.623 band."), 9,
      "The same &lsquo;11% moisture&rsquo; number can mean anything from ruined-too-dry to "
      "mould-risk. Water activity closes that gap to a fraction of a point." + _c("astm-d8197-water-activity")),
    table(["Mistake", "What happens", "Fix"], [
      ["Over-drying below 0.55 aw", "Terpenes evaporate, smell fades, water weight lost", "Take down at 0.60-0.62 aw, stop curing at 0.58-0.60 aw"],
      ["Drying too hot / fast", "Outside dries while inside stays wet, trapping mould", "Hold 60&deg;F / 60% RH and let it take 10-14 days"],
      ["Trusting a cheap moisture meter", "&plusmn;1% spans 0.53-0.66 aw, too dry to mouldy", "Use water-activity testing to decide done"],
      ["Overfilling containers", "Crushed buds, trapped moisture", "Fill totes/barrels no more than ~2/3, curing barrels no more than half"],
      ["Touching the flower / skipping the deep clean", "Knocked-off trichomes, contamination", "Handle by stem only, deep-clean before every load"],
      ["Safe aw but still smells wet", "Inside not finished", "Let it dry more. Your senses are the final check"],
    ], cls="compact", caption="The big six post-harvest mistakes and their fixes."),
  ]})

SECTIONS.append({"id": "expectations", "kicker": "Reality check", "title": "What realistic results look like",
  "blocks": [
    p("Expect roughly 10-14 days of hang-drying plus several more days of curing before flower is "
      "truly finished. The whole post-harvest stage is two-to-three weeks, not overnight, and there "
      "is no rushing it."),
    figure(L.line("The post-harvest finish line, day by day",
            [(0, 0.85), (1, 0.72), (2, 0.62), (3, 0.59), (4, 0.59)],
            ["harvest d0", "test d7-8", "takedown d10-14", "trim & cure", "sealed"],
            ylab="aw", ymin=0.50, ymax=0.90,
            bands=[(0.55, 0.65, L.GL, "safe zone 0.55-0.65 aw")],
            note="Testing starts ~day 7-8. Takedown ~day 10-14 at 0.60-0.62 aw. Cure settles to 0.58-0.60 aw, then seal."), 10,
      "A realistic arc: water activity falls from harvest, enters the safe zone at takedown, and "
      "settles in curing before the batch is sealed." + _c("astm-d8197-water-activity")),
    callout("key", "Three honest truths",
      ol(["<strong>It takes weeks, not days.</strong> Plan two-to-three weeks for the whole post-harvest stage and do not rush the dry.",
          "<strong>The payoff is real.</strong> Dialling in drying and curing is reported to lift yield 5-10%, mostly by no longer over-drying." + _c("aroya-drying-water-activity-guide"),
          "<strong>Genetics matter.</strong> Drying and curing are strain-dependent. Dense and fluffy flowers finish at slightly different aw points, so log every batch." + _c("birenboim-2024-cultivar-drying")])),
    p("Record the aw, RH, dates and outcomes for every genetic so good results are repeatable. The "
      "instrument is a guide, not a boss: inside the safe aw zone, trust smell and feel for the "
      "final call. When you are ready, read the <a href='mould-risk.html'>mould-risk</a> guide for "
      "what to do if a batch slips above the line, and the "
      "<a href='nutrient-mixing-athena.html'>nutrient-mixing</a> guide for the feed side of quality."),
  ]})
