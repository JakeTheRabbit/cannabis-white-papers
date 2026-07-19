# -*- coding: utf-8 -*-
"""Paper: the cannabis flower cycle, week by week (beginner)."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        stagecard, grid, card, chip, kv, steps)
import figs_lib as L

SLUG = "flowering-stages"
TITLE = "The flower cycle, week by week"
EYEBROW = "Beginner · Flower"
SUB = ("A beginner's guide to the cannabis flowering stage: the flip to 12/12, the stretch, "
       "bud set, bulking, ripening, and reading the plant to know exactly when to cut.")
META = [("leaf", "Beginner"), ("image", "9 diagrams"),
        ("quote", "Evidence-linked · 8 sources"), ("clock", "~12 min read")]
RELATED = ["coco-crop-steering", "defoliation-training", "harvest-dry-trim-cure"]
REF_IDS = ["ahrens-2023-photoperiod-optimum", "spitzer-rimon-2019-florogenesis",
           "llewellyn-2022-light-intensity-yield", "eichhorn-bilodeau-2019-photobiology",
           "livingston-2020-trichome-maturation", "hesami-2023-morphological-lifecycle",
           "mahmoud-2023-botrytis-budrot", "ahrens-2023-photoperiod-lightleak-revert"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

SECTIONS.append({"id": "what-this-is", "kicker": "01 · Start here", "title": "What this is and who it's for",
  "blocks": [
    lead("Cannabis grows in two big phases: vegetative (building leaves, stems and roots) and "
         "flowering (building the buds you actually harvest). Flowering is triggered by changing "
         "the lights to 12 hours on and 12 hours off, and it runs for roughly 8 to 10 weeks for "
         "most plants. This guide walks that stretch one week at a time."),
    p("You do not need to have grown before to use it. Flowering is the final phase, lasting about "
      "8 to 10 weeks for typical hybrids. Pure indica types can finish in 7 to 8 weeks, and long "
      "sativa types can take 11 to 13." + _c("hesami-2023-morphological-lifecycle")),
    p("Only photoperiod plants need the light change to flower. Autoflower plants flower on their "
      "own with age, so this guide focuses on photoperiod plants. The plant tells you what week it "
      "is in, so you read the plant (pistils, trichomes, leaves) rather than the calendar alone. "
      "Getting the climate, light and feed right each week is the difference between dense, potent "
      "buds and loose, mouldy, or harsh ones."),
    figure(L.flow("The two-phase life cycle",
            [("Seed / clone", "start"), ("Vegetative", "18/6 light, build the frame"),
             ("Flip", "switch to 12/12"), ("Flowering", "8-10 weeks, buds form"),
             ("Harvest", "cut on trichome read")]), 1,
      "Flowering is the back half of the grow. Everything before the flip builds the plant. "
      "Everything after it builds the buds." + _c("hesami-2023-morphological-lifecycle")),
    callout("note", "Who this is for",
      p("Anyone about to flip their first photoperiod grow who wants a week-by-week map. Pairs with "
        "the <a href='coco-crop-steering.html'>crop-steering</a> and "
        "<a href='harvest-dry-trim-cure.html'>harvest and cure</a> papers.")),
  ]})

SECTIONS.append({"id": "key-terms", "kicker": "02 · Vocabulary", "title": "Every term you need, defined",
  "blocks": [
    p("This page uses a handful of grower words repeatedly. Learn these six and the rest of the "
      "guide reads easily. None of them are complicated once defined."),
    defterm("Flip / 12/12", "Changing your light timer to 12 hours on, 12 hours off. This tricks a "
            "photoperiod plant into thinking winter is coming, which starts flowering."),
    defterm("Pistils", "The fine white hairs that emerge from bud sites. They start white and "
            "darken to orange or brown as the plant ripens."),
    defterm("Trichomes", "The tiny mushroom-shaped resin glands that coat the buds. Under "
            "magnification they go clear, then milky, then amber. They hold most of the THC and "
            "aroma and are the real harvest signal."),
    defterm("Calyx, bud and cola", "A calyx is one teardrop floral pod. Many calyxes stacking "
            "together form a bud, and a large bud cluster on a main stem is a cola."),
    defterm("EC and VPD", "EC (electrical conductivity) measures how strong your nutrient water is. "
            "VPD (vapor pressure deficit) is a single number combining temperature and humidity "
            "that tells you how comfortably the plant breathes and drinks."),
    defterm("Defoliation and lollipopping", "Removing leaves to open up airflow and light "
            "(defoliation), and stripping the lower third of the plant so energy goes to the top "
            "buds (lollipopping)."),
    figure(L.flow("From calyx to cola",
            [("Calyx", "one floral pod"), ("Bud", "stacked calyxes"),
             ("Cola", "bud cluster on a stem"), ("Pistils", "white to orange hairs"),
             ("Trichomes", "clear to milky to amber")]), 2,
      "The same flower, named at different scales. Pistils and trichomes are the two signals you "
      "watch to time the harvest."),
  ]})

SECTIONS.append({"id": "the-flip", "kicker": "03 · How it works", "title": "The flip: why 12/12 starts flowering",
  "blocks": [
    p("Photoperiod cannabis measures the length of the dark period to decide whether it is spring "
      "(grow) or autumn (reproduce). When you give it 12 hours of uninterrupted darkness, it reads "
      "that as the days shortening and switches into flower production." + _c("spitzer-rimon-2019-florogenesis")),
    p("The darkness must be truly dark. Uninterrupted darkness is required to trigger and maintain "
      "flowering, and even small light leaks during the 12-hour night can stress the plant back "
      "toward veg or cause it to make seeds (hermaphroditism)." + _c("eichhorn-bilodeau-2019-photobiology") +
      " In vitro work shows photoperiod plants will revert when night length is broken." + _c("ahrens-2023-photoperiod-lightleak-revert")),
    p("Twelve hours is the safe default, though research finds slightly longer nights can also work "
      "for some cultivars." + _c("ahrens-2023-photoperiod-optimum") + " Most strains show their first "
      "pre-flower pistils within 7 to 14 days of the flip. Flip the plant when it is healthy and "
      "roughly half to two-thirds of your final desired height, because it will stretch a lot after "
      "the flip."),
    figure(L.zones("Light vs dark: veg schedule against flower schedule",
            0, 24, [(0, 18, L.GL, "18h light (veg)"), (18, 24, L.BLUL, "6h dark"),
                    (0, 12, L.AMBL, "12h light (flower)"), (12, 24, L.PURL, "12h dark, light-tight")],
            unit="h",
            note="The flip is the switch from the top schedule to the bottom one. The 12h dark block must be sealed."), 3,
      "Vegetative runs long days. Flowering runs an equal split, and the dark half is the trigger. "
      "Break that dark period and the plant can revert or seed." + _c("eichhorn-bilodeau-2019-photobiology")),
    callout("warn", "The dark must be dark",
      p("Stray light from chargers, timer LEDs, or door gaps during lights-off can cause re-vegging "
        "or hermaphroditism. Tape over indicator lights and seal the room before you flip.")),
  ]})

SECTIONS.append({"id": "stretch-bud-set", "kicker": "04 · Weeks 1-4", "title": "The stretch and bud set (weeks 1-4)",
  "blocks": [
    p("For the first 2 to 3 weeks after the flip the plant stretches, often nearly doubling in "
      "height as it builds the frame to hang buds on, while white pistils appear at the nodes." + _c("hesami-2023-morphological-lifecycle")),
    p("Around weeks 3 to 4 the stretch stops and those pistil sites organise into real budlets as "
      "calyxes begin stacking. This is the most sensitive window: every bud's final position is "
      "being set, so heavy leaf removal here costs you yield. In weeks 1 to 2 plants can gain 50 to "
      "100% in height, so keep PPFD around 800 to 900 umol/m2/s and feed at a moderate EC (drip EC "
      "around 2.0 to 2.6) as growth is fast." + _c("llewellyn-2022-light-intensity-yield")),
    figure(L.line("Plant height through the flower cycle",
            [(0, 100), (1, 135), (2, 175), (3, 195), (4, 200), (5, 201),
             (6, 202), (7, 202), (8, 202), (9, 202)],
            ["flip", "wk1", "wk2", "wk3", "wk4", "wk5", "wk6", "wk7", "wk8", "wk9"],
            ylab="height %", ymin=90, ymax=215,
            note="Final height locks in around week 4. Almost all of the gain is the early stretch."), 4,
      "The stretch is steep through weeks 1 to 3, then flat. Flip at half to two-thirds of your "
      "target height to leave room for it." + _c("hesami-2023-morphological-lifecycle")),
    table(["Week", "Phase", "PPFD (umol/m2/s)", "Day / night temp", "RH", "VPD (kPa)", "Drip EC", "Action"], [
      ["1", "Stretch", "800-850", "26-28 C / 22-24 C", "65-70%", "0.9-1.0", "2.0-2.2", "Lollipop, light defoliation"],
      ["2", "Stretch", "850-900", "26-28 C / 22-24 C", "62-68%", "1.0-1.1", "2.2-2.4", "Main defoliation"],
      ["3", "Bud set", "900", "26-28 C / 21-23 C", "60-65%", "1.0-1.1", "2.4-2.6", "Last light defoliation, then stop"],
      ["4", "Bud set", "900", "26-28 C / 21-23 C", "58-62%", "1.1-1.2", "2.4-2.6", "Hold steady, no more leaf removal"],
    ], cls="compact", caption="Weeks 1 to 4 targets. Run early flower slightly warm and humid, then ease humidity down as buds set." + _c("eichhorn-bilodeau-2019-photobiology")),
    callout("tip", "Defoliate early or not at all",
      p("Lollipop and do your main defoliation between roughly day 7 and the end of week 3, before "
        "bud sites lock in. Do not defoliate heavily after week 3. See the "
        "<a href='defoliation-training.html'>defoliation and training</a> paper for technique.")),
  ]})

SECTIONS.append({"id": "bulking-ripening", "kicker": "05 · Weeks 5-10", "title": "Bulking and ripening (weeks 5-10)",
  "blocks": [
    p("Weeks 5 to 7 are peak bulking: buds swell fastest, frost (trichomes) builds, and aroma "
      "intensifies, so this is when light, feed and CO2 pay off most." + _c("livingston-2020-trichome-maturation")),
    p("From roughly week 7 onward the plant ripens: pistils darken from white to orange, trichomes "
      "shift clear to milky, and lower fan leaves yellow as the plant pulls stored nutrients into "
      "the buds. You push hardest during bulking, then ease off and lower humidity into ripening to "
      "protect the harvest. During bulking, push PPFD to about 900 to 1100 umol/m2/s (1200 to 1500 "
      "with CO2 enrichment at 1000 to 1200 ppm) and raise feed to peak EC." + _c("llewellyn-2022-light-intensity-yield")),
    p("Bulking climate runs around 26 to 28 C day, with RH down to about 55 to 62% to limit mould "
      "risk as buds densify, and VPD around 1.1 to 1.3 kPa. In ripening (week 8 and on), drop RH to "
      "40 to 50%, keep temps moderate in the low-to-mid 20s C, and many growers lower or flush "
      "nutrients in the last 1 to 2 weeks. Yellowing lower leaves late in flower is normal nutrient "
      "remobilisation, not always a deficiency to chase."),
    figure(L.bars("Relative bud mass gain per week",
            [("wk1", 5), ("wk2", 10), ("wk3", 30), ("wk4", 55), ("wk5", 95),
             ("wk6", 100), ("wk7", 85), ("wk8", 55), ("wk9", 30), ("wk10", 15)],
            unit="%", note="Peak swelling lands weeks 5 to 7, then tapers as the plant ripens.", maxv=110), 5,
      "Most of the weight goes on weeks 5 to 7. That is where light, feed and CO2 earn their keep." + _c("livingston-2020-trichome-maturation")),
    figure(L.zones("Target humidity falls across the cycle",
            35, 75, [(0, 4, L.GL, "Early 55-65%"), (4, 7, L.AMBL, "Bulking 50-60%"),
                     (7, 10, L.BLUL, "Ripening 40-50%")],
            unit="% RH",
            note="EC rises into bulking then eases in ripening. Humidity comes down the whole way to fend off rot."), 6,
      "Humidity steps down stage by stage as buds get denser. The dense late canopy is where high "
      "humidity does the most damage." + _c("mahmoud-2023-botrytis-budrot")),
  ]})

SECTIONS.append({"id": "when-to-harvest", "kicker": "06 · The decision", "title": "Reading the plant: when to harvest",
  "blocks": [
    p("Pistils are a rough early signal but they lie. Trichomes are the true clock, and you read "
      "them with a cheap jeweler's loupe or pocket microscope." + _c("livingston-2020-trichome-maturation")),
    p("Harvest when most trichomes have turned from clear to milky or cloudy, with a small fraction "
      "going amber. A common target is 80 to 90% milky with 5 to 15% amber. More clear or milky "
      "gives a more energetic, heady effect. More amber means THC is degrading toward CBN for a "
      "heavier feel for some people &mdash; multi-factor, not a CBN switch." + _c("livingston-2020-trichome-maturation")),
    p("Wait until pistils are mostly darkened and curled in (roughly 70% or more), then switch to "
      "checking trichomes for the real call. Use 60x or higher magnification on actual bud, not "
      "sugar leaves, and check several spots, since maturity varies across the plant. Do not harvest "
      "on the calendar alone: a week 9 strain can need week 10 depending on conditions and phenotype."),
    figure(L.line("Trichome colour over the ripening weeks",
            [(0, 90), (1, 70), (2, 45), (3, 20), (4, 8), (5, 3)],
            ["wk6", "wk7", "wk8", "wk9", "wk10", "wk11"],
            ylab="% clear", ymin=0, ymax=100, bands=[(0, 12, L.GXL, "harvest window")],
            note="As clear trichomes vanish, milky peaks and amber creeps in. The shaded band is the common harvest window."), 7,
      "Clear trichomes fade out as milky takes over and a little amber appears. Cut inside the "
      "window as a maturity cue; later cuts often feel heavier, genotype still dominates." + _c("livingston-2020-trichome-maturation")),
    table(["Signal", "What you see", "Readiness", "Effect if cut now"], [
      ["Pistils", "Still mostly white, sticking out", "Too early", "Thin, harsh, low potency"],
      ["Trichomes", "Mostly clear", "Too early", "Underdeveloped"],
      ["Trichomes", "80-90% milky, 5% amber", "Peak window (early)", "Common early-cut target"],
      ["Trichomes", "Milky with 10-15% amber", "Peak window (late)", "Balanced"],
      ["Trichomes", "30%+ amber, leaves yellow", "Over-ripe", "Often denser/heavier feel; genotype still dominates"],
    ], cls="compact", caption="Read trichomes on bud at 60x or more. Pistil colour is only a first hint." + _c("livingston-2020-trichome-maturation")),
  ]})

SECTIONS.append({"id": "pitfalls", "kicker": "07 · Avoid these", "title": "Common beginner mistakes",
  "blocks": [
    p("Most first-grow failures in flower come from a few repeatable errors: light leaks, "
      "over-defoliating, chasing the calendar instead of the trichomes, and letting humidity stay "
      "high as buds get dense. Each is easy to avoid once you know it. The single most expensive "
      "mistake is harvesting too early because you ran out of patience."),
    table(["Pitfall", "The fix"], [
      ["Light leaks in the dark period", "Tape over LED indicators and seal door gaps. Bright or repeated night interruptions can stall flowering; genetics and multi-stress drive most herms"],
      ["Over-defoliating or doing it late", "Stop heavy leaf removal after week 3. Leaves are the plant's sugar factory during bulking"],
      ["Humidity too high in late flower", "Pull RH down to 40-50% from week 7. Dense buds plus 60%+ RH invites bud rot (botrytis)"],
      ["Nutrient burn", "Drop feed EC and give enough water volume per feed. Burnt tips mean the feed is too strong"],
      ["Harvesting too early or by calendar", "Let the trichomes decide. A few extra days to proper maturity beats hitting an exact week"],
    ], cls="compact", caption="The five mistakes that sink most first grows, and the concrete fix for each." + _c("mahmoud-2023-botrytis-budrot")),
    callout("danger", "Watch the late canopy for rot",
      p("High humidity (60% and up) in dense late-flower canopies sharply increases bud rot risk. "
        "Botrytis starts inside the bud where you cannot see it, then collapses a whole cola. Keep "
        "air moving and humidity low through ripening." + _c("mahmoud-2023-botrytis-budrot"))),
  ]})

SECTIONS.append({"id": "expectations", "kicker": "08 · Reality check", "title": "Realistic expectations and a sample timeline",
  "blocks": [
    p("A typical photoperiod indoor grow runs about 8 to 10 weeks of flower on top of veg time, and "
      "your first harvest will rarely be your best. Yield and quality climb as you learn to read the "
      "plant. Strain genetics set the outer limits, while your light, climate and feed decide how "
      "close you get to them. Breeder-stated flowering times are estimates, and the actual finish "
      "varies with conditions by a week or more in either direction." + _c("hesami-2023-morphological-lifecycle")),
    table(["Week", "Phase", "What the plant is doing", "PPFD", "Day/night", "RH / VPD", "Action"], [
      ["1-2", "Stretch", "Doubling in height, first pistils", "800-900", "27 C / 23 C", "65% / 1.0", "Lollipop, defoliate"],
      ["3-4", "Bud set", "Stretch ends, budlets form", "900", "27 C / 22 C", "60% / 1.1", "Stop defoliating"],
      ["5-7", "Bulking", "Buds swell fastest, frost builds", "1000-1100", "27 C / 22 C", "58% / 1.2", "Peak feed, push light"],
      ["8-10", "Ripening", "Pistils darken, trichomes go milky", "900", "24 C / 20 C", "45% / 1.2", "Lower RH, ease EC, read trichomes"],
    ], cls="compact", caption="A week-by-week map, not a rulebook. Let the trichomes have the final word."),
    figure(L.flow("The flower cycle at a glance",
            [("Stretch", "wk 1-3"), ("Bud set", "wk 3-4"), ("Bulking", "wk 5-7"),
             ("Ripening", "wk 8-10"), ("Trichome read", "the call"), ("Harvest", "cut")]), 8,
      "The whole arc on one line. Each stage hands off to the next, and the trichome read gates the "
      "harvest."),
    figure(L.bars("Where the weight goes by stage",
            [("Stretch", 10), ("Bud set", 20), ("Bulking", 55), ("Ripening", 15)],
            unit="%", note="Bulking is where most of the final mass is laid down.", maxv=65), 9,
      "Plan your effort around bulking. That is where light, climate and feed move the harvest most."),
    callout("key", "Three honest truths",
      ol(["<strong>Conditions move the finish date.</strong> Genetics set the range, but your climate "
          "and feed decide where in it you land, often by a week or more.",
          "<strong>Keep simple notes.</strong> Week, height, climate, feed, what you removed. This is "
          "the fastest way to make each grow better than the last.",
          "<strong>The last weeks feel slow.</strong> Resist cutting early, because that is where a lot "
          "of weight and potency finalise."])),
    p("Get the flip clean, ease humidity down as buds densify, and let the trichomes decide. From "
      "here, read the <a href='coco-crop-steering.html'>crop-steering</a> paper to fine-tune feed "
      "and dryback, then the <a href='harvest-dry-trim-cure.html'>harvest, dry and cure</a> paper "
      "to protect everything you just grew."),
  ]})
