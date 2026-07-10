# -*- coding: utf-8 -*-
"""Paper: precision coco cultivation, crop steering in coir (beginner)."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        stagecard, grid, card, chip, kv, steps)
import figs_lib as L

SLUG = "coco-crop-steering"
TITLE = "Precision coco cultivation: crop steering in coir"
EYEBROW = "Beginner · Coco & crop steering"
SUB = ("Coco coir lets you talk to your plants through water. This paper shows you what the root "
       "zone is telling you, and how a daily rhythm of wetting and drying steers a plant toward "
       "leaves or toward flower, explained from zero.")
META = [("droplet", "Beginner"), ("image", "5 diagrams"),
        ("quote", "Peer-reviewed · 10 sources"), ("clock", "~16 min read")]
RELATED = ["root-zone-teros12", "grow-room-systems", "tissue-culture"]
REF_IDS = ["abad2005-coir", "noguera2003-cec", "malik2025-media", "hilhorst2000-ec",
           "caplan2019-drought", "stack2024-drought", "welling2025-aba",
           "grossiord2020-vpd", "moe1995-dif", "moher2023-photoperiod"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

SECTIONS.append({"id": "start", "kicker": "01 · Read this first", "title": "What this paper is",
  "blocks": [
    lead("&lsquo;Crop steering&rsquo; is a simple idea behind a jargon name: by controlling "
         "<em>when</em> and <em>how much</em> you water, you can push a plant to grow bigger and "
         "leafier, or to focus on dense, resinous flower. Coco coir is the easiest substrate to do "
         "this in, because it responds fast and predictably."),
    p("You do not need to have measured a root zone before to use this guide. Every term is defined. "
      "By the end you will know what the numbers on a root-zone sensor mean, and how a daily "
      "wet-and-dry rhythm becomes a steering wheel for your plant."),
    callout("note", "Who this is for",
      p("Anyone growing in coco, or thinking about it, who wants results they can repeat instead of "
        "watering &lsquo;when it feels dry.&rsquo; Pairs with the "
        "<a href='root-zone-teros12.html'>root-zone sensor</a> and "
        "<a href='grow-room-systems.html'>grow-room systems</a> papers.")),
  ]})

SECTIONS.append({"id": "terms", "kicker": "02 · The vocabulary", "title": "The words you need",
  "blocks": [
    p("You do not need to memorise these, just get the gist. Each one comes back in context."),
    defterm("Coco coir", "A growing medium made from the fibrous husk of coconuts. It holds water "
            "like a sponge but still keeps lots of air around the roots."),
    defterm("Substrate", "The general word for whatever the roots grow in: coco, rockwool, "
            "peat or soil. <a href='glossary.html#gl-substrate'>Glossary &rarr;</a>"),
    defterm("VWC (volumetric water content)", "How wet the root zone is, as a percentage of its "
            "volume. 60% VWC means water fills 60% of the pot's space."),
    defterm("EC (electrical conductivity)", "A proxy for how much fertiliser salt is dissolved in "
            "the root zone. Higher EC means a stronger, saltier feed."),
    defterm("Field capacity", "The wettest the substrate gets right after it drains: sponge "
            "full, excess dripped out. This is your daily &lsquo;full&rsquo; mark."),
    defterm("Dryback", "The drop in VWC between waterings as the plant drinks and the substrate "
            "dries. This is the single most important steering tool."),
    defterm("Crop steering", "Deliberately nudging the plant vegetative (leafy) or generative "
            "(flower/resin) using irrigation, climate and light."),
    defterm("Shot", "One short irrigation pulse. Crop steering replaces one big daily soak with "
            "several small, timed shots."),
  ]})

SECTIONS.append({"id": "why-coco", "kicker": "03 · The substrate", "title": "Why coco behaves differently",
  "blocks": [
    p("Coco holds a lot of water <strong>and</strong> a lot of air at the "
      "same time. At field capacity, roughly a fifth to a third of its volume is still "
      "air-filled pore space" + _c("abad2005-coir") + ". That oxygen is what keeps roots "
      "healthy and lets you water often without drowning them."),
    figure(L.bars("Air around the roots at field capacity",
            [("Coco coir", 25), ("Peat", 12), ("Rockwool", 18)], unit="%",
            note="Air-filled porosity: higher means more oxygen at the roots when fully wet.",
            maxv=32), 1,
      "Coco holds more air at field capacity than peat, so roots get oxygen even when the medium is "
      "wet. Exact values vary with the pith-to-chip mix and pot size." + _c("abad2005-coir") + _c("malik2025-media")),
    p("Coco also carries a mild electrical charge on its fibres that grabs and releases nutrients: "
      "its <strong>cation exchange capacity</strong>" + _c("noguera2003-cec") + ". Think of it "
      "as a small battery for feed. It buffers swings, but it also means fresh coco will hold back "
      "some calcium and magnesium until it is &lsquo;charged&rsquo; (pre-soaked in a cal-mag feed)."),
    callout("tip", "Charge your coco first",
      p("New coco can lock up calcium and magnesium for the first week or two. Pre-soak (buffer) it "
        "with a cal-mag solution before planting, or expect early deficiency spots until it settles.")),
  ]})

SECTIONS.append({"id": "reading", "kicker": "04 · The signals", "title": "Reading the root zone: VWC and EC",
  "blocks": [
    p("A root-zone sensor reports two living numbers: <strong>VWC</strong> (how wet) and "
      "<strong>EC</strong> (how salty). Together they tell you what the plant is doing and what to "
      "do next."),
    p("Here is the trick beginners miss: <strong>as the substrate dries, the salt left behind "
      "gets more concentrated, so EC rises</strong>. The water leaves and the fertiliser does not. A "
      "sensor estimates the &lsquo;pore-water EC&rsquo; the roots actually feel from the bulk "
      "reading, the moisture and the temperature" + _c("hilhorst2000-ec") + ". That is why EC "
      "readings get unreliable once VWC falls into single digits."),
    figure(L.line("A normal day in coco: VWC drops, then refills",
            [(0, 60), (1, 57), (2, 53), (3, 49), (4, 47), (5, 60)],
            ["lights on", "+3h", "+6h", "+9h", "pre-dark", "next shot"],
            ylab="VWC %", ymin=40, ymax=66,
            note="The plant drinks the pot down through the day, and irrigation refills it back to field capacity."), 2,
      "A healthy daily curve: a controlled fall (the dryback) followed by a refill to field "
      "capacity. The size and timing of that fall is your steering lever."),
    callout("key", "Two numbers, one story",
      ul(["<strong>VWC falling</strong> means the plant is drinking (good), until it falls too far and growth stalls.",
          "<strong>EC drifting up</strong> as VWC falls is normal. A big jump means the root zone is getting too salty, so water it.",
          "<strong>EC drifting down</strong> over days means the plant is eating salt faster than you feed, so raise feed EC."], "tight")),
  ]})

SECTIONS.append({"id": "dryback", "kicker": "05 · The engine", "title": "Dryback: the engine of steering",
  "blocks": [
    p("A <strong>dryback</strong> is letting the root zone dry by a chosen amount before you "
      "water again. It is the most powerful lever you have, because a mild, controlled water deficit "
      "changes how the plant grows."),
    p("When the root zone dries a little, the plant makes a stress hormone called "
      "<strong>abscisic acid (ABA)</strong>, which shifts it away from leafy growth and toward "
      "flowering and resin production" + _c("welling2025-aba") + ". Done deliberately at the right time, "
      "one controlled water-deficit trial raised cannabinoid concentration; its flower-yield difference "
      "was not statistically significant" + _c("caplan2019-drought") + ". That experiment used one "
      "cultivar and one 11-day drought event in week 7, so it supports a possible response, not the "
      "specific daily dryback targets below."),
    callout("warn", "A dryback is not a drought",
      p("The difference is dose and timing. <strong>Moderate</strong>, measured drybacks that you "
        "stop on time preserve yield. A <strong>severe</strong> drought that runs too long crashes "
        "both yield and cannabinoids" + _c("stack2024-drought") + ". Steer with a scalpel, not a hammer. "
        "Always water before the plant actually wilts.")),
    p("Bigger drybacks push generative (flower). Smaller drybacks, kept wetter, push vegetative "
      "(leaves and size). That one dial, how far you let it dry, is most of crop steering."),
  ]})

SECTIONS.append({"id": "phases", "kicker": "06 · The daily rhythm", "title": "The daily cycle: P0–P3",
  "blocks": [
    p("Growers split the lights-on day into four phases. You do not need fancy gear to think this "
      "way. It is a rhythm of dry, refill, maintain, dry."),
    figure(L.flow("The four phases of the irrigation day",
            [("P0", "morning dryback at lights-on"), ("P1", "ramp up: small shots refill"),
             ("P2", "maintain near field capacity"), ("P3", "overnight dryback")]), 3,
      "P0 is the short morning dryback after lights-on, before the first feed, that gets the plant "
      "drinking. P1 is a series of small shots that climb the root zone back up. P2 holds it full "
      "while the plant works. P3 is the big overnight dryback that falls through the dark."),
    figure(L.bars("Where VWC sits through the phases",
            [("P0 end", 46), ("P1", 54), ("P2", 60), ("P3 start", 57)], unit="%", target=55,
            note="Generative steering runs the whole band lower. Vegetative runs it higher and flatter.", maxv=70), 4,
      "A generative day (shown) lets the dryback run deeper and keeps shots smaller. A vegetative day keeps "
      "VWC higher and the dryback shallow."),
    table(["Phase", "What it is", "What it does"], [
      ["<strong>P0</strong>", "After lights-on, before the first shot, no water", "A short morning dryback that gets the plant drinking before feeding starts"],
      ["<strong>P1</strong>", "A series of small shots after lights-on", "Refills the root zone back to field capacity, gently"],
      ["<strong>P2</strong>", "Maintenance shots", "Holds VWC near full and flushes out built-up salt (EC control)"],
      ["<strong>P3</strong>", "Last shot, then overnight", "The big overnight dryback; sets the generative or vegetative tone for the day"],
    ], caption="The P0–P3 framework. The numbers you choose for each phase are your steering recipe."),
  ]})

SECTIONS.append({"id": "steering", "kicker": "07 · The steering wheel", "title": "Steering generative vs vegetative",
  "blocks": [
    p("&lsquo;Generative&rsquo; means flowers, density and resin. &lsquo;Vegetative&rsquo; means "
      "leaves, stems and size. You bias the plant with a handful of levers that all work by changing "
      "how hard the plant has to work for water."),
    table(["Lever", "Push GENERATIVE (flower)", "Push VEGETATIVE (leaf/size)"], [
      ["Dryback", "Bigger, longer drybacks", "Smaller drybacks, stay wetter"],
      ["Feed EC", "Higher EC (more osmotic stress)", "Lower EC"],
      ["Shots", "Fewer, smaller, later start", "Earlier, more frequent, bigger"],
      ["Day/night temp", "Cooler nights, wider day-night gap", "Warmer, flatter temps"],
      ["VPD / humidity", "Drier air (higher VPD)", "More humid air (lower VPD)"],
    ], caption="Most levers act through transpiration, how fast the plant pulls water. Use one or two at a time, not all at once."),
    p("Temperature is on that list because the gap between day and night temperature controls stretch. "
      "A warm day with a cool night keeps plants compact. A warm night makes them stretch" + _c("moe1995-dif") +
      ". Air dryness (VPD) sets how fast the plant transpires, up to a point, then stomata "
      "close and everything slows" + _c("grossiord2020-vpd") + "."),
    callout("danger", "Change one thing at a time",
      p("Every lever interacts. If you yank the dryback, raise EC, drop humidity and cool the night "
        "all at once, you will not know what helped or hurt, and you may tip a steer into real "
        "stress. Move one dial, watch for a few days, then adjust.")),
  ]})

SECTIONS.append({"id": "week", "kicker": "08 · The arc", "title": "A week-by-week shape",
  "blocks": [
    p("Flowering indoors usually runs about 8–10 weeks once you flip the lights to a 12-hour "
      "night" + _c("moher2023-photoperiod") + ". The steering changes across that arc:"),
    steps([
      ("Late veg", "Steer vegetative: keep VWC high, drybacks small, EC moderate. Build a big, healthy plant and root system."),
      ("Flower wk 1–2 (stretch)", "Plants nearly double in height. Keep nights cooler and the day-night gap modest to limit stretch, and begin gentle generative drybacks."),
      ("Flower wk 3–6 (build)", "Peak generative steering: firm drybacks, higher EC, hold P2 full to feed bulking flowers."),
      ("Flower wk 7+ (ripen)", "Ease off. A controlled late water-deficit can lift potency, but stop before stress shows."),
      ("Flush / finish", "Lower EC feeds in the final stretch. Let the plant wind down cleanly."),
    ]),
  ]})

SECTIONS.append({"id": "trouble", "kicker": "09 · When it goes wrong", "title": "Troubleshooting",
  "blocks": [
    table(["Symptom", "Likely cause", "What to do"], [
      ["EC climbing every day, plant sulking", "Salt building up, drybacks too hard or not enough flush", "Bigger P2 shots to flush, lower feed EC a touch"],
      ["VWC barely drops all day", "Overwatering or plant not drinking (cold/dark/sick)", "Fewer or smaller shots, check root health, temps, light"],
      ["Leaves clawing, tips burnt", "Feed EC too high for conditions", "Drop EC, ensure enough water volume per shot"],
      ["Tall, stretchy, floppy plants", "Too vegetative: warm nights, small drybacks", "Cooler nights, wider day-night gap, firmer drybacks"],
      ["Early cal-mag deficiency", "Fresh coco not buffered", "Pre-charge coco, add cal-mag to early feeds"],
      ["Wilting between shots", "Dryback gone too far (drought, not steer)", "Water sooner, shorten P0/P3. Never let it actually wilt"],
    ], cls="compact"),
  ]})

SECTIONS.append({"id": "expect", "kicker": "10 · Straight talk", "title": "Realistic expectations",
  "blocks": [
    callout("key", "Three honest truths",
      ol(["<strong>There is no universal recipe.</strong> The right VWC, EC and dryback numbers depend on your strain, pot size, climate and light. Start from the ranges here and tune to <em>your</em> plants.",
          "<strong>Steering is a bias, not a switch.</strong> You are nudging odds over days, not flipping a plant overnight.",
          "<strong>The root zone is only one lever.</strong> Light, temperature, humidity and airflow all push the same plant. Read the <a href='grow-room-systems.html'>systems guide</a> next."])),
    p("Get a sensor on the root zone, learn to read one normal day, then change one thing at a time. "
      "That discipline, not a magic number, is what makes coco repeatable."),
  ]})
