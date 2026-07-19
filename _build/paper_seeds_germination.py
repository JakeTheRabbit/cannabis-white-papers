# -*- coding: utf-8 -*-
"""Paper: seeds, germination and seedlings (beginner)."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        stagecard, grid, card, chip, kv, steps)
import figs_lib as L

SLUG = "seeds-germination"
TITLE = "Seeds, germination and seedlings"
EYEBROW = "Beginner · Propagation"
SUB = ("From a dry seed to a thriving seedling: what a seed is, how to choose one, how to "
       "wake it up, and how to keep it alive through its most fragile three weeks.")
META = [("seedling", "Beginner"), ("image", "9 figures"),
        ("quote", "Evidence-linked · 9 sources"), ("clock", "~14 min read")]
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

SECTIONS.append({"id": "what-this-is", "kicker": "Start here", "title": "What this is",
  "blocks": [
    lead("This paper takes a complete beginner from a dry cannabis seed to a healthy "
         "two-to-three-week-old seedling, defining every term along the way. A seed is a tiny "
         "dormant plant in a protective shell, waiting for the right cues to wake up. Germination "
         "is the act of waking it. A seedling is the baby plant in its first weeks of life."),
    p("Get these early stages right and the rest of the grow is far easier, because most fatal "
      "mistakes happen in the first 21 days. Read this before buying or planting anything."),
    figure(L.flow("From seed to established seedling",
            [("Dry seed", "dormant, day 0"), ("Imbibition", "soaks up water"),
             ("Taproot", "root emerges, day 1-3"), ("Planted", "into medium"),
             ("Cotyledons", "seed leaves open"), ("True leaves", "day 7-14"),
             ("Established", "seedling, day 21")]), 1,
      "The whole arc this paper covers: a dry seed drinks water, pushes out a taproot, gets "
      "planted, opens its first leaves, and becomes a sturdy seedling by about week three."),
    callout("note", "What this covers",
      ul(["Choosing a seed, germinating it, and caring for the seedling through roughly day 21",
          "Germination = waking a dormant seed. Seedling = the plant's most fragile life stage",
          "Most beginner failures (rot, no-sprouts, stunting) trace back to these first three weeks",
          "Every technical term is defined in plain language the first time it appears"], "tight")),
  ]})

SECTIONS.append({"id": "key-terms", "kicker": "Vocabulary", "title": "Key terms, defined once",
  "blocks": [
    p("Before the how-to, here is the small vocabulary the rest of this paper relies on. You do "
      "not need to memorise it, each term comes back in context."),
    defterm("Taproot (radicle)", "The first white root that pokes out of the seed and grows "
            "straight downward. Its appearance is the sign a seed has germinated."),
    defterm("Cotyledons", "The two rounded &lsquo;seed leaves&rsquo; that appear first. They feed "
            "the plant from stored reserves until real leaves take over."),
    defterm("True leaves", "The familiar serrated cannabis leaves that come after the cotyledons. "
            "Their arrival marks the start of real growth."),
    defterm("Seed coat", "The hard protective outer shell of the seed."),
    defterm("Embryo", "The living baby plant inside the seed: a taproot, two cotyledons and a "
            "tiny shoot, all folded up and waiting."),
    defterm("Germination rate", "The percentage of seeds in a batch that successfully sprout."),
    defterm("Viable", "Capable of sprouting. A viable seed is alive. A dead seed will never sprout "
            "no matter what you do."),
    defterm("Damping-off", "A fungal disease that rots seedlings at the soil line and topples "
            "them. The single most lethal seedling problem."),
    table(["Term", "Plain meaning"], [
      ["Taproot / radicle", "First downward root out of the seed"],
      ["Cotyledons", "Rounded embryonic &lsquo;seed leaves&rsquo;"],
      ["True leaves", "Later serrated cannabis leaves"],
      ["Seed coat", "Protective outer shell"],
      ["Embryo", "The living baby plant inside"],
      ["Germination rate", "Percent of seeds that sprout"],
      ["Viable", "Capable of sprouting"],
      ["Damping-off", "Fungal rot at the seedling's stem base"],
    ], cls="compact", caption="Glossary quick-reference. Scan back to this while reading later sections."),
  ]})

SECTIONS.append({"id": "anatomy-and-quality", "kicker": "Core concept 1", "title": "Inside a seed, and how to judge a good one",
  "blocks": [
    p("A cannabis seed is a complete dormant plant. A tough seed coat protects an embryo that "
      "already contains a taproot, two cotyledons and a tiny shoot, plus stored food to fuel the "
      "first days of growth before the plant can feed itself."),
    figure(L.flow("What is inside a seed",
            [("Seed coat", "hard outer shell"), ("Embryo", "the baby plant"),
             ("Taproot", "first root, folded"), ("Cotyledons", "two seed leaves"),
             ("Food store", "fuels first days")]), 2,
      "A cutaway view: the shell guards the embryo, which already holds the taproot, cotyledons "
      "and shoot, surrounded by a small food reserve."),
    p("Quality is partly visible. Mature, viable seeds are firm, dark brown, and often mottled "
      "with a &lsquo;tiger-stripe&rsquo; pattern, and they do not crush under gentle finger "
      "pressure. Pale white, yellow, or light-green seeds were usually harvested too early and "
      "tend to sprout poorly or produce weak plants." + _c("bazzaz-1975-seed-storage-viability")),
    p("Fresh seeds stored cool, dark and dry stay viable for years, but germination rate falls as "
      "seeds age and their stored oils break down." + _c("cockson-2025-hemp-seed-moisture-temperature") +
      " A sealed container in the fridge is a good home for spares."),
    table(["Check", "Good (viable) seed", "Bad (likely dud)"], [
      ["Colour", "Dark brown, often mottled", "Pale white, yellow or green"],
      ["Surface", "&lsquo;Tiger-stripe&rsquo; pattern", "Plain, dull"],
      ["Firmness", "Hard, does not squish", "Soft, gives under pressure"],
      ["Squeeze test", "Holds shape", "Cracks or crushes"],
    ], cls="compact", caption="A quick visual and feel check before you commit a seed to germination."),
    callout("tip", "Pale does not always mean dead",
      p("Immature pale seeds can still sprout, but they tend to give weaker, lower-quality plants. "
        "If you have a choice, plant the dark, firm, striped ones first.")),
  ]})

SECTIONS.append({"id": "seed-types", "kicker": "Core concept 2", "title": "Feminised, regular and autoflower: which seed to buy",
  "blocks": [
    p("There are three seed types and the choice shapes your whole grow. Regular seeds produce "
      "roughly half male and half female plants. Only females make the flower (the &lsquo;bud&rsquo;) "
      "most growers want, so males are usually removed."),
    p("Feminised seeds are bred to produce almost only female plants, removing the guesswork and "
      "wasted effort. They are made by inducing a female plant to make pollen (using treatments "
      "such as colloidal silver), so the resulting seeds carry only female "
      "genetics." + _c("flajsman-2021-feminized-seed-production") + _c("monthony-2021-feminized-sts-comparison")),
    p("Autoflower seeds carry Cannabis ruderalis genetics that make the plant flower automatically "
      "after about 2-4 weeks regardless of the light schedule, finishing in roughly 60-90 days "
      "from sprout." + _c("toth-2022-autoflower1-locus") + " Photoperiod plants (regular and "
      "feminised) flower when nights are long enough without light interruptions (12/12 is the usual default)." + _c("moher-2023-twelve-hour-photoperiod-flowering")),
    table(["", "Regular", "Feminised", "Autoflower"], [
      ["Sex outcome", ("~50% male / 50% female", "~99% female (if feminised)", "Feminised autos ~99% female; regular autos ~50/50")],
      ["Flowering trigger", "Switch to 12h light", "Switch to 12h light", "Automatic, by age"],
      ["Time to harvest", "Longer", "Longer", "~60-90 days from sprout"],
      ["Plant size", "Large", "Large", "Small (~2-4 ft)"],
      ["Yield potential", "High", "High", "Lower per plant"],
      ["Beginner-friendly", "No (must sex/cull)", "Yes (simplest)", "Yes (hands-off timing)"],
    ], cls="compact", caption="Feminised is the simplest first choice. Autoflower is forgiving on timing. Regular suits breeders."),
    callout("note", "Photoperiod vs autoflower in one line",
      p("Photoperiod plants flower when nights are long enough (growers usually use 12 hours light / 12 hours dark). Autoflowers "
        "flower when they reach a certain age, whatever the lights are doing.")),
  ]})

SECTIONS.append({"id": "germination-methods", "kicker": "Core concept 3", "title": "Three ways to germinate, and why",
  "blocks": [
    p("Germination just means giving the seed three things: water and warmth (darkness is optional convenience). The "
      "embryo swells, drinks, and pushes the taproot out through the seed coat. There are three "
      "common ways to deliver those three things."),
    p("The paper-towel method (seeds between damp paper towels, sandwiched between two plates) is "
      "the most popular because you can watch the taproot appear, and with fresh seed and controlled moisture and temperature high germination is common "
      "when conditions are controlled." + _c("cockson-2025-hemp-seed-moisture-temperature") +
      " Its one risk is damaging the fragile root when you move the seed to its pot."),
    table(["Method", "Visibility", "Transplant risk", "Difficulty", "Best for"], [
      ["Paper-towel", "High (you see the root)", "Moderate (handle gently)", "Easy", "Most beginners"],
      ["Direct-sow", "None (hidden in medium)", "None", "Easy", "Avoiding any root handling"],
      ["Pre-soak", "Some (seeds sink/swell)", "Low", "Easy", "Old or hard-shelled seeds"],
    ], cls="compact", caption="All three supply water + warmth (darkness optional). They differ mainly in whether you can see progress."),
    figure(L.flow("The paper-towel method, step by step",
            [("Wet towels", "wring out fully"), ("Place seeds", "spaced apart"),
             ("Cover", "second damp towel"), ("Sandwich", "between two plates"),
             ("Warm dark", "21-25C spot"), ("Check 12h", "keep damp"),
             ("Plant", "taproot 0.5-1cm")]), 3,
      "Wet but wrung-out towels, seeds spaced out and covered, kept warm and dark, checked twice "
      "a day. Plant once the taproot is about 0.5-1.5 cm long." + _c("smith-2022-hemp-germination-temperature-limits")),
    callout("tip", "Direct-sow and pre-soak in brief",
      ul(["<strong>Direct-sow:</strong> plant the seed straight into moist medium about 1-1.5 cm deep, taproot pointing down. No transplant shock, but you cannot see progress.",
          "<strong>Pre-soak:</strong> soak seeds in room-temperature water for 12-24 hours to soften the coat. Useful for old or hard seeds, then move them to towel or medium."], "tight")),
  ]})

SECTIONS.append({"id": "conditions-and-timeline", "kicker": "By stage", "title": "The conditions seeds need, and what to expect when",
  "blocks": [
    p("Seeds are sensitive to their environment. Three settings matter: temperature, moisture and "
      "light. Get all three in range and most viable seeds sprout on their own."),
    p("Hold temperature at a steady 21-25C (70-77F). Cooler slows germination, and warmer or "
      "fluctuating temperatures cause outright failures." + _c("smith-2022-hemp-germination-temperature-limits") +
      " Keep the medium or towel damp like a wrung-out sponge, never waterlogged, and keep seeds "
      "damp and warm until they sprout (darkness optional)."),
    figure(L.zones("Ideal germination temperature", 14, 34,
            [(14, 21, L.BLUL, "too cold, slow"), (21, 25, L.GL, "ideal"),
             (25, 28, L.AMBL, "warm, riskier"), (28, 34, L.REDL, "too hot, fails")],
            unit="C",
            note="Steady warmth in the green band gives the fastest, most reliable sprouting."), 4,
      "Aim for the green band and keep it stable. Swings and heat above ~28C are a common cause of "
      "no-shows." + _c("smith-2022-hemp-germination-temperature-limits")),
    figure(L.line("The first 21 days",
            [(0, 0), (2, 1), (4, 2), (7, 3), (10, 4), (14, 5), (21, 6)],
            ["day 0", "day 2", "day 4", "day 7", "day 10", "day 14", "day 21"],
            ylab="growth stage", ymax=7,
            note="Stage 0 seed, 1 taproot, 2 planted, 3 cotyledons, 4-5 first true leaves, 6 established."), 5,
      "Taproot usually shows in 24-72 hours (up to ~7 days for some seeds), cotyledons open within "
      "days, first true leaves appear around days 7-14, and you have an established seedling by "
      "about day 21." + _c("cockson-2025-hemp-seed-moisture-temperature")),
    callout("key", "The three settings, in one place",
      ul(["<strong>Temperature:</strong> steady 21-25C / 70-77F. Avoid swings and anything above ~28C.",
          "<strong>Moisture:</strong> damp not soaked (wrung-out-sponge feel). Waterlogged seeds suffocate and rot.",
          "<strong>Light:</strong> darkness is optional while germinating. Once sprouted, give gentle light immediately so the stem does not stretch."], "tight")),
  ]})

SECTIONS.append({"id": "seedling-care", "kicker": "By stage", "title": "Seedling care: the first two to three weeks",
  "blocks": [
    p("The newborn seedling has almost no roots, so it has a tiny root system, so it loses water easily. High humidity reduces evaporative demand until roots expand — roots still do the drinking.4-0.8 kPa), often using "
      "a humidity dome or a vented clear bag for the first 7-10 days." + _c("zhang-2021-vpd-stomatal-conductance-growth") +
      " VPD (vapour pressure deficit) is just a measure of how thirsty the air is. Lower means "
      "more humid."),
    p("Keep light gentle: roughly 100-200 PPFD in the first week, rising to 200-300 PPFD by week "
      "two (a DLI near 10-15), with LEDs kept well back to avoid stretch or "
      "burn." + _c("rodriguez-2021-cannabis-light-intensity-photosynthesis") + " PPFD is the "
      "amount of usable light hitting the plant right now. DLI is the total it receives over a day."),
    p("Do not feed at first. The cotyledons supply the plant's food. Start a weak nutrient "
      "solution at about 25% strength (EC roughly 0.3-0.8 mS/cm) only once the first true leaves "
      "appear, around weeks 2-3. Water sparingly around the base and let the surface dry slightly "
      "between waterings so roots reach down to find moisture."),
    table(["", "Week 1", "Week 2", "Week 3"], [
      ["Humidity (RH)", "70-80%", "65-75%", "55-65%"],
      ["VPD (kPa)", "0.4-0.6", "0.6-0.8", "0.8-1.0"],
      ["Light (PPFD / DLI)", "100-200 / ~10", "200-300 / ~13", "250-350 / ~15"],
      ["Feed EC (mS/cm)", "none (plain water)", "~0.3-0.6 at true leaves", "~0.6-0.8"],
      ["Watering", "Mist / light, near stem", "Light, let surface dry", "Slightly more, still sparing"],
    ], cls="compact", caption="Week-by-week seedling targets. Start humid and gentle, then ease humidity down and bring light and feed up slowly."),
    figure(L.bars("Light distance and stretch",
            [("Light too far", 18), ("Correct distance", 7)], unit=" cm stem",
            note="Stem height of a two-week seedling. Too-far light makes the plant stretch tall and weak.",
            maxv=22), 6,
      "A seedling reaching for distant light grows tall, thin and leggy. At the right distance it "
      "stays short and stocky, which is what you want." + _c("rodriguez-2021-cannabis-light-intensity-photosynthesis")),
    callout("warn", "The two newbie traps",
      p("Overwatering and feeding too early kill more seedlings than anything else. When in doubt, "
        "water less and feed later. A seedling that looks a little hungry recovers. One that has "
        "rotted does not.")),
  ]})

SECTIONS.append({"id": "troubleshooting", "kicker": "When it goes wrong", "title": "Damping-off and other common failures",
  "blocks": [
    p("The most lethal seedling disease is damping-off, caused by soil fungi such as Pythium, "
      "Fusarium and Rhizoctonia. A previously healthy seedling suddenly pinches, blackens and "
      "topples at the soil line, and it is almost always fatal once it "
      "strikes." + _c("lamichhane-2017-damping-off-management")),
    p("The dominant cause is overwatering combined with too-high humidity and poor airflow, so "
      "prevention beats cure. Use fresh sterile medium, water sparingly, add gentle air "
      "circulation, and drop humidity toward 40-50% once true leaves "
      "appear." + _c("umn-extension-prevent-damping-off")),
    figure(L.flow("How damping-off takes hold (and where to break the chain)",
            [("Overwater", "+ high humidity"), ("Low airflow", "air stays still"),
             ("Wet medium", "stays soggy"), ("Fungus grows", "in wet soil"),
             ("Damping-off", "seedling collapses")]), 7,
      "Break the chain early: less water, more airflow, lower humidity after true leaves. Once the "
      "fungus is active at the stem, the seedling is usually lost." + _c("lamichhane-2017-damping-off-management")),
    table(["Symptom", "Most likely cause", "What to do"], [
      ["Stem rots and topples at soil line", "Damping-off (overwet, humid, still air)", "Remove the seedling, dry out, add airflow, lower humidity; prevention only"],
      ["Seed never sprouts", "Old or immature seed, too cold, planted too deep, or dried out", "Use fresh seed, hold 21-25C, plant 0.5-1.5 cm, keep damp"],
      ["Tall, thin, leggy", "Light too weak or too far away", "Move light closer / brighter; bury extra stem at transplant"],
      ["Crispy or burnt leaf tips", "Fed too early or too strong", "Back off to plain water, then resume at ~25% strength"],
      ["Yellowing seedling", "Overwatering or premature feeding", "Let medium dry slightly, hold off nutrients until true leaves"],
    ], cls="compact", caption="Match the symptom to its cause. Most fixes are about doing less: less water, less feed, more air."),
    callout("danger", "Damping-off has no cure",
      p("Once a seedling pinches at the base it will not recover. Everything you do for damping-off "
        "is prevention: sterile fresh medium, sparing water, good airflow, and humidity eased to "
        "40-50% after the true leaves show." + _c("umn-extension-prevent-damping-off"))),
  ]})

SECTIONS.append({"id": "realistic-expectations", "kicker": "Reality check", "title": "Realistic expectations",
  "blocks": [
    p("Even with good seeds and care, not every seed sprouts. Fresh quality feminised seed often "
      "runs well above 90% germination, but a dud or two is normal and not a sign you did something "
      "wrong." + _c("bazzaz-1975-seed-storage-viability")),
    figure(L.bars("Typical germination success by seed condition",
            [("Fresh feminised", 95), ("Older seed", 75), ("Pale / immature", 45), ("Poorly stored", 30)],
            unit="%",
            note="Rough expectations, not guarantees. Fresh, dark, well-stored seed sprouts best.",
            maxv=100), 8,
      "Fresh quality seed sprouts reliably. Age, immaturity and bad storage all drag the rate "
      "down." + _c("cockson-2025-hemp-seed-moisture-temperature")),
    p("Budget about 3-4 weeks from planting to a sturdy seedling with several sets of true leaves "
      "before the plant truly takes off into vegetative growth. Germinate one or two extra seeds "
      "as insurance, expect to lose the occasional seedling, and resist the two biggest "
      "temptations: overwatering and feeding too early."),
    callout("key", "What good looks like",
      ul(["High germination is normal for fresh quality seed, but expect the occasional dud even when you do everything right.",
          "Plan ~3-4 weeks from plant to established seedling before vigorous growth begins.",
          "Germinate one or two spares as insurance. Losing a seedling now and then is part of learning.",
          "The two costliest beginner habits are overwatering and feeding too early. Underdoing both is safer."], "tight")),
    p("Slow and gentle wins these first weeks. Once your seedling is established, look at "
      "<a href='light-acclimation.html'>light acclimation</a> to ramp it up safely, and keep "
      "<a href='mould-risk.html'>mould risk</a> in mind as humidity comes down. If you would "
      "rather skip seeds entirely next time, <a href='cloning.html'>cloning</a> gives you an exact "
      "copy of a plant you already trust."),
  ]})
