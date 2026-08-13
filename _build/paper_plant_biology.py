# -*- coding: utf-8 -*-
"""Paper: cannabis plant biology and the life cycle — the reference chapter for the site."""
import json, os
from components import (p, lead, h, ul, ol, callout, defterm, table, figure, grid, card, chip, kv, steps)
import figs_lib as L

_FIGS = json.load(open(os.path.join(os.path.dirname(__file__), "figs_plant_biology.json"), encoding="utf-8"))

SLUG = "plant-biology"
TITLE = "Cannabis plant biology and the life cycle"
EYEBROW = "Reference · Biology"
SUB = ("What kind of plant cannabis actually is, every part of it named, and the machinery underneath: "
       "the life cycle stage by stage, how the night triggers flowering, sex and hermaphroditism, "
       "photosynthesis, roots and hormones. The biology every other paper on this site leans on.")
META = [("leaf", "Reference"), ("image", "12 diagrams"),
        ("quote", "Evidence-linked · 16 sources"), ("clock", "~19 min read")]
RELATED = ["flowering-stages", "seeds-germination", "lighting-fundamentals"]

REF_IDS = [
    "small-2015-cannabis-taxonomy",
    "mcpartland-2018-cannabis-systematics",
    "watts-2021-terpene-synthase-labels",
    "hesami-2023-morphological-lifecycle",
    "spitzer-rimon-2019-florogenesis",
    "livingston-2020-trichome-maturation",
    "legris-2019-phytochrome-mechanisms",
    "ahrens-2023-photoperiod-lightleak-revert",
    "ahrens-2023-photoperiod-optimum",
    "kusuma-2021-nir-leds-delay-flowering-phytochrome",
    "toth-2022-autoflower1-early1",
    "divashuk-2014-xy-sex-chromosomes",
    "punja-holmes-2020-hermaphroditism",
    "flajsman-2021-feminized-seed-production",
    "chandra-2008-photosynthetic-response",
    "morard-1996-root-oxygen",
]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

# ------------------------------------------------------------------ 01 start here
SECTIONS.append({"id": "start-here", "kicker": "01 · Start here", "title": "What this is and how to use it",
  "blocks": [
    lead("Every other paper on this site quietly assumes you know what a node is, why the dark period "
         "is sacred, and what a trichome actually does. This is the paper that teaches it. It is the "
         "reference chapter: the plant itself, part by part and stage by stage, with the mechanisms "
         "underneath explained in plain language."),
    p("You do not need any biology background. Every term is defined the first time it appears, and "
      "the whole vocabulary is collected in a quick-reference table at the end. Read it once end to "
      "end before your first grow, then come back whenever a word or a mechanism trips you in "
      "another paper."),
    p("Where a topic has its own dedicated paper, this chapter gives you the biology and hands over: "
      "<a href='seeds-germination.html'>seeds and germination</a> for popping seeds, "
      "<a href='flowering-stages.html'>the flower cycle week by week</a> for running bloom, "
      "<a href='lighting-fundamentals.html'>lighting fundamentals</a> for the hardware side of "
      "light, and <a href='defoliation-training.html'>defoliation and training</a> for shaping the "
      "plant. Here we cover the why that sits under all of them."),
    callout("note", "Who this is for",
      p("Anyone starting out, and anyone mid-grow who keeps meeting words like bract, internode, "
        "phytochrome or sink and wants them nailed down once, properly, with sources.")),
  ]})

# ------------------------------------------------------------------ 02 core answer
SECTIONS.append({"id": "what-kind-of-plant", "kicker": "02 · The core answer", "title": "What kind of plant cannabis is",
  "blocks": [
    lead("Cannabis sativa L. is an annual, normally dioecious, wind-pollinated flowering herb in the "
         "family Cannabaceae — the same small family as hops. It completes its whole life in one "
         "season, keeps male and female flowers on separate plants, and mails its pollen on the "
         "wind." + _c("small-2015-cannabis-taxonomy") + _c("mcpartland-2018-cannabis-systematics")),
    kv([
      ("Family", "Cannabaceae — its closest famous relative is hops (Humulus)" + _c("mcpartland-2018-cannabis-systematics")),
      ("Life span", "Annual: germinates, grows, flowers once and dies within a year"),
      ("Sexes", "Dioecious: male and female are usually separate plants"),
      ("Pollination", "Wind. No petals, no nectar, no insects involved"),
      ("Flowering trigger", "Night length — it is a short-day (really a long-night) plant"),
      ("Chromosomes", "2n = 20: nine autosome pairs plus X and Y sex chromosomes" + _c("divashuk-2014-xy-sex-chromosomes")),
      ("Photosynthesis", "C3 — responds strongly to added light and CO2 when temperature allows" + _c("chandra-2008-photosynthetic-response")),
    ]),
    p("Each of those dry facts is a grow-room rule wearing a lab coat:"),
    ul([
      "<strong>Annual</strong> means no second chances inside a season. The plant runs its program "
      "once. Indoors you replay the seasons with a light timer, which is why the schedule matters "
      "so much.",
      "<strong>Dioecious</strong> means roughly half of regular seeds become males you must find "
      "and remove. Unpollinated females (sinsemilla) put their energy into resin instead of seed.",
      "<strong>Wind-pollinated</strong> means pollen is airborne, abundant and mobile. One shedding "
      "male — or one stressed female throwing anthers — can seed an entire room, and pollen rides "
      "clothing and airflow between rooms.",
      "<strong>Short-day</strong> means an unbroken dark period is the flowering switch. Light "
      "discipline is not a preference, it is the trigger mechanism itself.",
    ]),
    callout("key", "Four facts, most of the rulebook",
      p("Annual, dioecious, wind-pollinated, night-triggered. Nearly every hard rule in cultivation "
        "— cull males early, seal the dark period, plan the whole cycle before you start — is one "
        "of these four facts asserting itself.")),
  ]})

# ------------------------------------------------------------------ 03 taxonomy
SECTIONS.append({"id": "taxonomy", "kicker": "03 · Naming", "title": "Sativa, indica, ruderalis: the honest version",
  "blocks": [
    p("The folk story says there are two (or three) kinds of cannabis: tall, airy, energising "
      "<em>sativas</em>; short, dense, sedating <em>indicas</em>; and a tiny weedy <em>ruderalis</em> "
      "that flowers on its own. It is a useful shorthand for growth habit. As biology, and "
      "especially as a predictor of effect, it does not hold up."),
    p("Botanically, most taxonomists treat cannabis as a single, extraordinarily variable species — "
      "Cannabis sativa L. — pulled in different directions by thousands of years of human selection "
      "for fibre, seed and resin. The hemp-versus-drug split is a THC threshold written into law, "
      "not a clean biological boundary." + _c("small-2015-cannabis-taxonomy")),
    p("It gets worse for the street labels: in the formal taxonomy, virtually all drug cannabis — "
      "everything sold as sativa <em>and</em> everything sold as indica — sits inside the same "
      "subspecies (C. sativa subsp. indica). The street terms map loosely onto narrow-leaflet versus "
      "broad-leaflet drug lineages, and 'ruderalis' is a debated name for feral, short-season "
      "northern populations rather than a settled species." + _c("mcpartland-2018-cannabis-systematics")),
    p("Genomics settled the practical question. A 2021 study genotyped over 100 commercial samples "
      "at roughly 100,000 genetic markers: samples labelled sativa and indica were genetically "
      "indistinguishable at the whole-genome level. The labels tracked only a handful of aroma "
      "terpenes, controlled by variation in terpene synthase genes — in other words, the label "
      "weakly predicts smell, not ancestry and not pharmacology." + _c("watts-2021-terpene-synthase-labels")),
    defterm("Cultivar (what growers call a strain)",
            "A named, cultivated variety — Wedding Cake, GG4. The horticultural term is cultivar; "
            "'strain' is entrenched grower slang for the same thing."),
    defterm("Chemotype (chemovar)",
            "Classification by chemistry instead of folklore: Type I is THC-dominant, Type II mixed "
            "THC:CBD, Type III CBD-dominant. Read it off a lab certificate of analysis (COA), not "
            "off the label art."),
    defterm("Genotype vs phenotype",
            "Genotype is the genetic deck the plant is dealt; phenotype is how that deck plays out "
            "in your environment. Same clone, two rooms, two phenotype expressions."),
    table(["Folk claim", "Verdict", "What the evidence says"], [
      ["Sativa = energising, indica = sedating",
       "Weak",
       "Labels are genetically indistinct; effects come from cannabinoid dose, terpene mix, the "
       "person and the setting" + _c("watts-2021-terpene-synthase-labels")],
      ["Leaf shape predicts the high",
       "No",
       "Leaflet width tracks lineage and climate history, not pharmacology" + _c("mcpartland-2018-cannabis-systematics")],
      ["Indica and sativa are separate species",
       "Contested, mostly no",
       "Mainstream treatment: one variable species with subspecies; centuries of crossing have "
       "blended the pools anyway" + _c("small-2015-cannabis-taxonomy")],
      ["Ruderalis is the autoflower parent",
       "Broadly yes",
       "Feral short-season populations are day-neutral; breeders introgressed that trait into "
       "modern autoflowers" + _c("toth-2022-autoflower1-early1")],
      ["The strain name tells you what you are getting",
       "Unreliable",
       "Names are unregulated; the same name can differ genetically between suppliers. Trust COAs "
       "and your own logs" + _c("watts-2021-terpene-synthase-labels")],
    ], cls="compact", caption="The folk taxonomy, audited. Keep the words as growth-habit shorthand; drop them as pharmacology."),
    callout("tip", "What to use instead",
      p("Buy and breed on chemotype (COA numbers), documented cultivar behaviour (stretch, finish "
        "time, mould tolerance) and your own grow logs. 'Sativa' and 'indica' still earn their keep "
        "as rough descriptions of plant shape — nothing more.")),
  ]})

# ------------------------------------------------------------------ 04 anatomy tour
SECTIONS.append({"id": "anatomy-tour", "kicker": "04 · Anatomy I", "title": "A tour of the plant, top to bottom",
  "blocks": [
    p("Strip away the mystique and a cannabis plant is a repeating unit stacked on itself: a stem "
      "segment, a node carrying leaves, and a dormant growing tip tucked into each leaf angle. "
      "Learn that unit and you can read any plant in any room."),
    figure(_FIGS["whole-plant"], 1,
      "The whole machine, labelled. Above ground: a main stem of nodes and internodes, fan leaves, "
      "an apical meristem on top and an axillary bud at every node. Below ground: taproot, laterals "
      "and the root hairs that do the actual drinking."),
    defterm("Node and internode",
            "A node is the joint on a stem where leaves, buds and branches attach. The internode is "
            "the bare stem between two nodes. Tight internodes = a compact plant; long internodes = "
            "stretch."),
    defterm("Apical meristem",
            "The main growing tip — a tiny dome of stem cells that builds every new leaf and stem "
            "segment. Cut it off (topping) and the plant does not die; it promotes the reserves."),
    defterm("Axillary bud",
            "A dormant backup meristem sitting in the angle (axil) between leaf stalk and stem at "
            "every node. Every branch, and ultimately every bud site, starts as one of these."),
    defterm("Fan leaf vs sugar leaf",
            "Fan leaves are the big palmate solar panels on long stalks. Sugar leaves are the small "
            "leaves that grow from inside flower clusters, dusted in trichomes — hence the name."),
    defterm("Petiole and stipule",
            "The petiole is the leaf stalk connecting blade to stem. Stipules are the two small "
            "green spikes at each node — beginners regularly mistake them for female pre-flowers."),
    p("The meristems are the plant's growth budget. The apical meristem normally dominates, and the "
      "axillary buds wait. Every training technique — topping, low-stress training, the trellis work "
      "in the <a href='defoliation-training.html'>defoliation and training</a> paper — is just a way "
      "of reassigning that budget to the meristems you want (the hormone mechanics are in section "
      "14)."),
    p("Leaves keep score of maturity. Seedling leaves start with a single leaflet, then three, then "
      "five, up to seven or more per fan leaf as the plant hits its stride." + _c("hesami-2023-morphological-lifecycle") +
      " Leaf arrangement is another tell: young plants place leaves in opposite pairs, and as the "
      "plant approaches flowering it shifts to alternate (staggered) placement — a visible sign the "
      "shoot has switched programs." + _c("spitzer-rimon-2019-florogenesis")),
    p("The stem is the plumbing between the two halves of the plant: xylem hauls water and minerals "
      "up from the roots (driven by transpiration from the leaves), and phloem moves sugar from the "
      "leaves to wherever it is being spent. Keep that two-pipe picture — it is the whole basis of "
      "the photosynthesis and source-sink story in section 12."),
    callout("note", "Seed plant vs clone, underground",
      p("A seed-grown plant builds a taproot with laterals branching off it. A rooted cutting never "
        "gets one — it grows a fibrous ball of adventitious roots from the cut stem instead (see "
        "the <a href='cloning.html'>cloning</a> paper). Both work; clones are simply shallower and "
        "quicker to dry out at the base.")),
  ]})

# ------------------------------------------------------------------ 05 flower anatomy
SECTIONS.append({"id": "flower-anatomy", "kicker": "05 · Anatomy II", "title": "Inside the flower: bract, calyx, pistil, stigma",
  "blocks": [
    p("An individual female cannabis flower is tiny and easy to misread: one small ovary wrapped in "
      "a resin-coated leaf-like pod, with two white hairs reaching out of the top. What growers call "
      "a bud is hundreds of these units packed along a stem axis with small sugar leaves between "
      "them." + _c("spitzer-rimon-2019-florogenesis")),
    figure(_FIGS["flower-closeup"], 2,
      "Left: a single female flower — bract, ovary in its thin perianth film, two stigmas. Right: "
      "the stack. A bud is this unit repeated hundreds of times along an axis; a cola is a big "
      "cluster of buds on a main stem." + _c("spitzer-rimon-2019-florogenesis")),
    defterm("Bract",
            "The small resin-dense pod that encloses each ovary. It carries the highest density of "
            "capitate-stalked trichomes on the plant — most of the potency of flower lives on "
            "bracts. Growers almost universally call it a calyx; botanically it is a bract."),
    defterm("Calyx (the real one)",
            "In cannabis, the true calyx is a thin, transparent film of tissue hugging the ovary "
            "inside the bract — you will rarely notice it. Harmless slang aside, know which "
            "structure people actually mean."),
    defterm("Pistil",
            "The complete female organ: ovary plus the stigmas. Grower usage calls the visible "
            "hairs 'pistils'; strictly, the hairs are stigmas."),
    defterm("Stigma",
            "One of the two white hairs protruding from each bract, built to catch airborne pollen. "
            "They emerge white and age to orange-brown whether or not pollination happens — colour "
            "is a maturity hint, not a pregnancy test."),
    defterm("Cola",
            "A large terminal cluster of buds on the end of a main stem or branch — the apical cola "
            "is the big one on top."),
    p("The stigma story explains sinsemilla. If pollen lands, the ovary swells into a seed and the "
      "plant redirects energy from resin and flower-building into seed-filling. Keep every male and "
      "every anther out of the room and the females sit unpollinated, stacking bracts and resin "
      "instead — seedless flower, sinsemilla, which is the entire commercial product."),
    p("Male flowers are a different design for a different job: five small tepals and five hanging "
      "stamens that shake pollen into the airflow, clustered in loose panicles with almost none of "
      "the trichome coverage females carry. They open, shed for days, and die — evolutionarily "
      "they only exist to fill the air with pollen." + _c("small-2015-cannabis-taxonomy")),
    callout("warn", "One open male seeds a room",
      p("A single flowering male sheds millions of airborne grains, and HVAC will deliver them for "
        "you. Unless you are deliberately breeding, males get identified early (section 10) and "
        "removed before any flower opens.")),
  ]})

# ------------------------------------------------------------------ 06 trichomes
SECTIONS.append({"id": "trichomes", "kicker": "06 · Anatomy III", "title": "Trichomes: where the value is made",
  "blocks": [
    p("Everything the market pays for — THC, CBD, the aroma terpenes — is manufactured and stored "
      "in glandular trichomes: microscopic mushroom-shaped glands on the flower surface. The "
      "cannabinoids are not 'in the bud' in some general sense; they sit in a resin reservoir "
      "inside each gland head, between the secretory cells and their waxy cap." + _c("livingston-2020-trichome-maturation")),
    figure(_FIGS["trichome-trio"], 3,
      "The three gland types at a glance. Bulbous glands are tiny and minor. Capitate-sessile "
      "glands sit flush on leaves. Capitate-stalked glands — the tall ones that give flower its "
      "frost — are the main cannabinoid and terpene factories." + _c("livingston-2020-trichome-maturation")),
    defterm("Bulbous trichome",
            "The smallest gland type, a few cells and roughly 10-30 µm across, scattered over most "
            "surfaces. A minor contributor to resin."),
    defterm("Capitate-sessile trichome",
            "A gland head sitting directly on the surface with almost no stalk, built on about "
            "eight secretory cells. Common on leaves and on younger tissue."),
    defterm("Capitate-stalked trichome",
            "The flagship: a multicellular stalk raising a large head built on 12-16 secretory "
            "cells. Densest on the bracts and sugar leaves of female flowers — this type makes "
            "flower sticky and potent."),
    p("The types are connected, not separate castes: as flowers mature, sessile-like glands convert "
      "into capitate-stalked ones — the head is raised on a new stalk and the secretory disc gains "
      "cells (eight in sessile heads, 12-16 in stalked). Gland output shifts with maturity too, "
      "which is part of why harvest timing changes the character of the product, not just its "
      "strength." + _c("livingston-2020-trichome-maturation")),
    figure(L.hbars("Secretory cells per gland head",
            [("Capitate-stalked", 16), ("Capitate-sessile", 8), ("Bulbous", 3)],
            unit=" cells",
            note="Approximate counts. More secretory cells and a bigger storage cavity = more resin per gland."), 4,
      "Why the stalked type dominates production: roughly double the secretory machinery of a "
      "sessile head, raised on a stalk and packed densest on the bracts." + _c("livingston-2020-trichome-maturation")),
    p("Two practical consequences. First, gland heads change colour with age — clear, then milky, "
      "then amber — which is the harvest-timing signal covered properly in "
      "<a href='flowering-stages.html'>the flower cycle paper</a>. Second, the heads sit on "
      "breakable stalks: every rough handle, tumble or warm touch after harvest knocks resin off "
      "the flower, which is why drying, trimming and hash work (see "
      "<a href='hash-rosin-pressing.html'>hash and rosin</a>) are all built around being cold and "
      "gentle."),
    callout("tip", "Buy a loupe before you buy anything else",
      p("A NZ$15 jeweller's loupe (60x) turns trichomes from folklore into data: type, density, "
        "colour, damage. It is the single cheapest instrument in cultivation.")),
  ]})

# ------------------------------------------------------------------ 07 life cycle
SECTIONS.append({"id": "life-cycle", "kicker": "07 · The arc", "title": "The life cycle, stage by stage",
  "blocks": [
    p("Cannabis is monocarpic: it flowers once, with everything it has, and then dies — harvest is "
      "you interrupting its senescence at the profitable moment. The stages below are one "
      "continuous program; each hands the next its starting conditions." + _c("hesami-2023-morphological-lifecycle")),
    figure(_FIGS["lifecycle-band"], 5,
      "The whole arc in one band. Indoors you control how long the plant sits in veg (the light "
      "schedule holds it there); flowering length is mostly written in the genetics." + _c("hesami-2023-morphological-lifecycle")),
    steps([
      ("Germination (roughly 3-7 days)",
       "The seed takes up water, metabolism switches on, and the radicle — the embryonic root — "
       "breaks out first and steers down with gravity. Everything runs on stored seed reserves. "
       "Detail and technique in the <a href='seeds-germination.html'>seeds and germination</a> paper."),
      ("Seedling (weeks 1-3)",
       "The two round cotyledons (seed leaves) open and the first true, serrated leaves appear — "
       "single leaflets at first, then three, then five. Under the surface the priority is root "
       "establishment; above it the plant is fragile to overwatering and damping-off." + _c("hesami-2023-morphological-lifecycle")),
      ("Vegetative (from ~week 3, as long as you choose)",
       "Pure infrastructure: nodes, leaf area and root mass compound while long days hold flowering "
       "off. The plant also matures internally — a young plant is not yet competent to flower, "
       "which is why cuttings and seedlings need a few weeks before the light flip does anything "
       "clean." + _c("hesami-2023-morphological-lifecycle")),
      ("Pre-flower / transition (1-2 weeks)",
       "With age, small solitary flowers appear at nodes — even under long days — announcing sex "
       "and flowering readiness. The short-night flip then converts the shoot tips from making "
       "leaves to making the packed flower clusters, and the plant stretches hard while it "
       "re-tools." + _c("spitzer-rimon-2019-florogenesis")),
      ("Flowering (7-10 weeks for most cultivars)",
       "Stretch, bud set, bulking, ripening. Buds become the highest-priority sink for sugar "
       "(section 12), stigmas and trichomes mark the clock, and the week-by-week detail lives in "
       "<a href='flowering-stages.html'>the flower cycle paper</a>."),
      ("Senescence (the last stretch)",
       "The wind-down is programmed, not pathological: nitrogen is remobilised out of the fan "
       "leaves into the flowers, so lower leaves yellow and drop; resin matures; a pollinated "
       "plant races to finish seed and shuts down faster. Then the annual dies — or you harvest."),
    ]),
    figure(L.bars("Typical stage lengths, indoor photoperiod grow",
            [("Germinate", 1), ("Seedling", 2), ("Veg (your call)", 6), ("Flower", 9)],
            unit="wk",
            note="Round numbers for planning. Veg is elastic — clones can flip in days, mothers can veg for years.",
            maxv=12), 6,
      "Where the calendar actually goes. The fixed cost is flowering; veg length is a lever you "
      "hold, which is how rooms are scheduled back from harvest dates."),
    p("Autoflowering cultivars compress this map and ignore the light schedule entirely — they get "
      "their own section (09) because the difference is genetic, not managerial."),
  ]})

# ------------------------------------------------------------------ 08 photoperiodism
SECTIONS.append({"id": "photoperiodism", "kicker": "08 · The trigger", "title": "Photoperiodism: the plant counts the night",
  "blocks": [
    p("How does a plant with no eyes measure the seasons? With a light-switchable pigment called "
      "phytochrome. It exists in two interconvertible forms: Pr (inactive) flips to Pfr (active) "
      "the instant red light (~660 nm) hits it, and Pfr flips back under far-red light (~730 nm) — "
      "or slowly, over hours, in darkness. Daylight is rich in red, so all day Pfr stays high: a "
      "chemical flag reading 'the lights are on'." + _c("legris-2019-phytochrome-mechanisms")),
    figure(_FIGS["phytochrome-toggle"], 7,
      "The toggle and the timer. Red light builds active Pfr instantly; darkness drains it slowly. "
      "A long unbroken night lets Pfr fall low enough, for long enough, that the flowering program "
      "runs — and one brief flash of light resets the whole countdown." + _c("legris-2019-phytochrome-mechanisms")),
    p("The slow dark decay is the timer. A short-day plant like cannabis is really a "
      "<strong>long-night</strong> plant: it commits to flowering when the unbroken dark period "
      "exceeds its critical length, night after night. The classic proof is night interruption — "
      "break a long night in the middle with even a brief period of light and the plant behaves as "
      "if the night were short, staying vegetative. That is precisely why growers keep flowering "
      "rooms light-tight and, in reverse, why a mother room can hold plants in veg by never letting "
      "a long night happen." + _c("legris-2019-phytochrome-mechanisms")),
    figure(L.zones("The night is the dial: hours of unbroken darkness per 24 h",
            8, 16,
            [(8, 11, L.BLUL, "stays vegetative"), (11, 12, L.AMBL, "cultivar-dependent edge"),
             (12, 16, L.GL, "flowers reliably")],
            unit="h",
            note="Approximate bands for photoperiod drug cultivars. The dark block must be continuous — total hours do not count if interrupted."), 8,
      "Why 12/12 is the standard: 12 h of clean darkness sits safely past the critical night length "
      "of essentially all photoperiod drug cultivars." + _c("ahrens-2023-photoperiod-optimum")),
    p("Controlled work shows how sharp the response is: cannabis plantlets grown in vitro flowered "
      "under a 12 h photoperiod but stayed vegetative when the light period was extended — small "
      "changes in night length flip the decision cleanly." + _c("ahrens-2023-photoperiod-lightleak-revert") +
      " And 12/12 is a safe default rather than a biological law: a trial across ten indoor "
      "cultivars found most flowered fine under a 13 h day, and several yielded more thanks to the "
      "extra daily light — a cultivar-by-cultivar experiment worth running once a line is stable, "
      "never an assumption." + _c("ahrens-2023-photoperiod-optimum")),
    p("Two subtleties worth owning. First, the full mechanism is more than the toggle: phytochrome "
      "feeds a circadian clock, which gates production of a mobile flowering signal (florigen, the "
      "FT protein) in the leaves that travels to the shoot tips — which is why the whole plant "
      "flowers together." + _c("legris-2019-phytochrome-mechanisms") + " Second, light beyond the "
      "visible red edge still counts: high-intensity near-infrared (~850 nm) delayed cannabis "
      "flowering by 12 days in testing, because phytochrome absorption does not stop dead at "
      "700 nm. At the low intensities of a typical security-camera illuminator a few metres from "
      "the canopy the effect is negligible — but do not park IR floodlights over flowering "
      "plants." + _c("kusuma-2021-nir-leds-delay-flowering-phytochrome")),
    defterm("Photoperiod",
            "The length of the daily light period. 'A photoperiod plant' is grower shorthand for a "
            "cultivar that flowers in response to it (via night length)."),
    defterm("Critical night length",
            "The minimum unbroken darkness that commits a short-day plant to flowering. For "
            "photoperiod cannabis, plan on ~12 h; the exact edge varies by cultivar."),
    callout("warn", "Treat the dark period as infrastructure",
      p("Walk the flowering room during lights-off after 10 minutes of letting your eyes adapt. "
        "Tape over equipment LEDs, seal door frames, check pinholes in ducting. Repeated light "
        "leaks delay and degrade flowering and are one of the stress inputs behind hermaphroditism "
        "(section 11)." + _c("punja-holmes-2020-hermaphroditism"))),
  ]})

# ------------------------------------------------------------------ 09 autoflowers
SECTIONS.append({"id": "autoflowers", "kicker": "09 · No clock needed", "title": "Autoflowers: ruderalis and the broken night-counter",
  "blocks": [
    p("Far northern feral cannabis — the populations often called Cannabis ruderalis, though its "
      "rank as a species is contested — faced summers where nights barely happen. Waiting for long "
      "nights there means dying unpollinated in the frost, so those populations evolved "
      "day-neutrality: flower on age, ignore the photoperiod." + _c("small-2015-cannabis-taxonomy") + _c("mcpartland-2018-cannabis-systematics")),
    p("Breeders moved that trait into modern drug cultivars, and its genetics are now mapped: "
      "autoflowering segregates as a simple recessive trait at a major locus (named Autoflower1), "
      "with additional day-neutral and early-flowering loci known, and the candidate genes sit in "
      "the plant's clock-and-flowering pathway. The practical consequence of 'recessive' matters: "
      "cross an autoflower with a photoperiod plant and the offspring are photoperiod — the trait "
      "hides unless both parents carry it." + _c("toth-2022-autoflower1-early1")),
    p("Running autos is a different management contract. You gain schedule freedom (18-24 h of "
      "light daily from seed to harvest, no light-tight paranoia for the trigger) and a short, "
      "predictable calendar of roughly 10-12 weeks seed to harvest. You give up control: you cannot "
      "hold an auto in veg, cannot keep one as a mother plant, and cannot re-veg your way out of a "
      "mistake — the internal clock only runs forward. Stress that costs a photoperiod plant a week "
      "costs an auto a chunk of its fixed lifespan."),
    table(["", "Photoperiod cultivar", "Autoflower cultivar"], [
      ["Flowering trigger", "Long unbroken nights (the flip to 12/12)", "Internal age clock — flowers regardless of schedule" + _c("toth-2022-autoflower1-early1")],
      ["Veg length", "Yours to choose — days to years", "Fixed by genetics, ~3-4 weeks"],
      ["Mother plants / cloning", "Standard practice", "Impractical — clones share the donor's age clock"],
      ["Light leaks in flower", "Serious risk: delay, reversion, herms", "Irrelevant to the trigger (stress still matters)"],
      ["Recovering from stress", "Extend veg, re-veg possible", "No pause button; damage is permanent"],
      ["Typical calendar", "Veg (your call) + 7-10 wk flower", "~10-12 wk total, seed to harvest"],
    ], cls="compact", caption="Two contracts with the same species. Autos trade control for speed and schedule freedom."),
  ]})

# ------------------------------------------------------------------ 10 sex determination
SECTIONS.append({"id": "sex-determination", "kicker": "10 · Sex", "title": "Sex: XX, XY, and reading pre-flowers",
  "blocks": [
    p("Cannabis carries true sex chromosomes, which is rare in plants: females are XX, males are "
      "XY, and the male is the heterogametic sex — exactly the human arrangement. The X is the "
      "largest chromosome in the set and the Y is larger than any autosome, so sex is decided at "
      "fertilisation, not by growing conditions." + _c("divashuk-2014-xy-sex-chromosomes") +
      " Regular seed therefore runs close to 50:50, and every regular-seed grow is a sexing "
      "exercise: identify the males early, remove them before any flower opens."),
    p("The plant declares itself before the flip. With age, small solitary pre-flowers form in the "
      "leaf axils of upper nodes — under long days, no trigger required — typically from around "
      "week 3-4 of veg." + _c("spitzer-rimon-2019-florogenesis") + " Reading them is a loupe job at "
      "first: females show a pointed pod with two white stigmas; males show small round pollen sacs "
      "on a short stalk, with no hairs. The stipules — those thin green spikes at every node — fool "
      "everyone once; they are on both sexes and mean nothing."),
    figure(_FIGS["preflower-sex"], 9,
      "The node check. Two wispy stigmas from a pointed pod = female, keep. Round balls on a little "
      "stalk = male, cull before anything opens. A female flower with a yellow exposed anther "
      "(banana) = hermaphrodite, treat as a pollen source." + _c("punja-holmes-2020-hermaphroditism")),
    p("If a plant refuses to declare, patience or a brief 12/12 period will force the issue — or "
      "sidestep the whole exercise with feminised seed (next section). For breeding work you keep "
      "your males, of course, but in a separate space with its own airflow, because of section 05's "
      "warning: pollen is the one contaminant you cannot recall."),
    defterm("Pre-flower",
            "The first solitary flower at a node, showing sex weeks before real flowering. Loupe "
            "territory at first appearance."),
    defterm("Sinsemilla",
            "Literally 'without seed': unpollinated female flower, the entire commercial product. "
            "Achieved by having no viable pollen anywhere near the room."),
  ]})

# ------------------------------------------------------------------ 11 herms + feminised seed
SECTIONS.append({"id": "herms-feminised", "kicker": "11 · When sex bends", "title": "Hermaphrodites, stress, and feminised seed",
  "blocks": [
    p("Chromosomes set sex; expression can still bend. A genetically female plant can produce "
      "functional male anthers — either mixed male flowers or the infamous 'banana' (an exposed "
      "anther pushing out of a female flower). Documented drivers: genetic predisposition in some "
      "lines, and stress — light leaks and photoperiod disruption, heat, physical damage, running "
      "far past ripeness. Hermaphroditism in commercial rooms produces viable pollen and unwanted "
      "seed without a single male present." + _c("punja-holmes-2020-hermaphroditism")),
    p("There is a genetic sting in the tail: seed sired by a hermaphrodite's pollen on a female "
      "carries no Y chromosome, so the offspring are female — feminised by accident. Tested "
      "herm-derived seed germinated at 90-95% and produced female progeny, but it is effectively "
      "self-pollination: low genetic variation, and it can quietly select for the herm tendency "
      "itself. Do not build a seed bank out of stress events." + _c("punja-holmes-2020-hermaphroditism")),
    p("Commercial feminised seed uses the same loophole deliberately, with chemistry instead of "
      "stress. Ethylene — a plant hormone — pushes cannabis toward female expression; block "
      "ethylene signalling and a genetic female will push out viable male flowers. The standard "
      "tool is STS (silver thiosulfate): repeated foliar sprays on a chosen female induce pollen "
      "that carries only X chromosomes, that pollen goes onto another female, and essentially all "
      "resulting seed is female. Gibberellin sprays can force maleness too, though less reliably — "
      "and sprayed plants are breeding stock, never product." + _c("flajsman-2021-feminized-seed-production")),
    figure(L.flow("How feminised seed is made (STS method)",
            [("Pick an elite female", "XX, proven in your room"),
             ("Spray STS", "silver blocks ethylene signalling"),
             ("Male flowers form", "on the genetic female"),
             ("X-only pollen", "no Y chromosome exists here"),
             ("Pollinate a female", "an XX by XX cross"),
             ("Feminised seed", "essentially all female")],
            note="Same biology as an accidental herm — done on purpose, on a schedule, to a plant you never sell."), 10,
      "Sex reversal without touching the genetics: every parent and every offspring is XX. This is "
      "why feminised seed exists and why it dominates the seed market." + _c("flajsman-2021-feminized-seed-production")),
    callout("danger", "Bananas shed pollen too",
      p("Treat an exposed anther exactly like a male in the room: isolate or cull the plant, note "
        "the cultivar and the stress that preceded it, and check its neighbours daily for a week. "
        "Anthers can self-seed the plant that made them and everything downwind." + _c("punja-holmes-2020-hermaphroditism"))),
  ]})

# ------------------------------------------------------------------ 12 photosynthesis
SECTIONS.append({"id": "photosynthesis", "kicker": "12 · The engine", "title": "Photosynthesis for growers: light, CO2 and heat are one system",
  "blocks": [
    p("Photosynthesis in one breath: chloroplasts in the leaves use light energy to split water and "
      "bolt CO2 from the air onto sugar molecules. Sugar is the plant's only income — every gram of "
      "root, leaf and flower is bought with it. Light drives the reaction, CO2 is the raw material, "
      "and temperature sets how fast the enzymatic machinery can run."),
    p("Because all three feed one process, they limit each other. Classic gas-exchange work on "
      "cannabis leaves found photosynthesis climbing with light intensity up to roughly "
      "1500 µmol/m²/s at around 30 °C, and rising further when CO2 was enriched toward 750 ppm — "
      "raise one input and the next one becomes the ceiling." + _c("chandra-2008-photosynthetic-response") +
      " That is the entire logic of <a href='co2-enrichment.html'>CO2 enrichment</a>: high light "
      "plus enriched CO2 plus a warmer room move together, or not at all. (Leaf-level numbers from "
      "one variety are a shape, not a setpoint — whole canopies, cultivars and VPD shift the "
      "curve, which is the territory of <a href='grow-room-systems.html'>the grow room as one "
      "system</a>.)"),
    figure(L.line("Photosynthesis vs light: the saturation curve",
            [(0, 4), (1, 42), (2, 72), (3, 100), (4, 95)],
            ["0", "500", "1000", "1500", "2000"],
            ylab="relative photosynthesis %",
            note="Leaf-level response shape near 30 °C at ambient CO2 (PPFD in µmol/m²/s). Past saturation, extra photons buy heat, not sugar.",
            ymax=110, ymin=0), 11,
      "Diminishing returns are built into the leaf. Each step of light buys less than the last, and "
      "past saturation you are just heating the room — unless CO2 and temperature rise to "
      "match." + _c("chandra-2008-photosynthetic-response")),
    p("Where the sugar goes is the other half of the story. Mature leaves are "
      "<strong>sources</strong> (net sugar exporters); growing tips, roots and above all flowers "
      "are <strong>sinks</strong> (net importers). The phloem allocates by demand, and demand has a "
      "pecking order that changes with life stage: in veg, new leaves and roots win; after the "
      "flip, the flowers become the dominant sink and everything else queues behind them."),
    figure(L.flow("Source to sink: follow the sugar",
            [("Light + CO2", "leaf chloroplasts fix carbon"),
             ("Sugars made", "in mature source leaves"),
             ("Phloem ships", "allocation follows demand"),
             ("Sinks spend", "tips, roots, young leaves"),
             ("In flower", "buds outrank everything")],
            note="Remove too many working sources and the sinks starve — that is the entire defoliation trade-off."), 12,
      "The economy under the canopy. Late-flower yellowing of fan leaves is this system working: "
      "the plant strips its own solar panels for parts and ships the nitrogen to the buds."),
    p("This model earns its keep daily: it is why healthy fan leaves are kept until late flower "
      "(they are the income), why <a href='defoliation-training.html'>defoliation</a> targets "
      "shaded, non-earning leaves rather than the well-lit ones, and why late-cycle leaf yellowing "
      "is often remobilisation on schedule rather than a deficiency to chase."),
    defterm("Source and sink",
            "Source: a tissue exporting sugar (mature sunlit leaf). Sink: a tissue importing it "
            "(root tip, young leaf, flower). Yield is sources funding the sinks you care about."),
  ]})

# ------------------------------------------------------------------ 13 roots
SECTIONS.append({"id": "roots", "kicker": "13 · The hidden half", "title": "Roots: the half you never see",
  "blocks": [
    p("Half the organism is underground and invisible, and most beginner disasters happen there "
      "first. The architecture is simple: from seed, a taproot drives down and lateral roots branch "
      "off it; from a cutting, a fibrous ball of adventitious roots forms instead. Either way the "
      "absorbing surface is not the thick white cables you see at transplant — it is the fuzz of "
      "root hairs just behind the growing tips, fragile, short-lived and constantly rebuilt as the "
      "roots explore."),
    p("Roots run on oxygen. They photosynthesise nothing and respire constantly, burning sugar sent "
      "down from the leaves — and that respiration needs O2 from the air spaces in the substrate. "
      "Flood those spaces and trouble starts within hours: water and nutrient uptake fall, the "
      "plant wilts <em>while sitting in water</em>, and root tissue starts dying — with opportunist "
      "pathogens (pythium and friends) queuing up behind the injury." + _c("morard-1996-root-oxygen") +
      " This is the mechanism behind the classic beginner trap: overwatering and underwatering "
      "look identical from above. One is thirst; the other is suffocation."),
    p("The fix is structural, not behavioural willpower: substrates are engineered air-water "
      "compromises (that is the air-filled porosity story in "
      "<a href='substrates-overview.html'>the substrates paper</a>), and watering is judged by "
      "weight or measured dryback rather than the calendar — the operating system of "
      "<a href='coco-crop-steering.html'>crop steering</a>."),
    p("The last few millimetres around each root — the rhizosphere — is its own ecosystem. Roots "
      "leak sugars and acids into it, feeding a dense microbial community that cycles nutrients, "
      "occupies the real estate pathogens want, and chemically differs from the bulk substrate: pH "
      "at the root surface shifts with which nutrients the plant is absorbing, which is one reason "
      "measured runoff never quite matches what the roots experience (see "
      "<a href='ph-management.html'>pH management</a>)."),
    callout("tip", "Judge the half you cannot see by proxy",
      p("Pot weight, dryback rate, runoff EC/pH, root colour at transplant (white and branching = "
        "good; brown, slimy or smelly = oxygen problem). The roots report daily — through "
        "instruments, not eyesight.")),
  ]})

# ------------------------------------------------------------------ 14 hormones
SECTIONS.append({"id": "hormones", "kicker": "14 · The levers", "title": "Hormones in one table",
  "blocks": [
    p("Five hormone families explain most of what a cannabis plant does — and most of what growers "
      "do to it. Every training technique is hormone manipulation performed with scissors and "
      "timers; every rooting gel and feminisation spray is the chemical version of the same game."),
    table(["Hormone", "Made mainly in", "What it does", "Where growers exploit it"], [
      ["<strong>Auxin</strong>", "Shoot tips (apical meristem)",
       "Enforces apical dominance — the tip suppresses the axillary buds below it; triggers root "
       "initiation at high local concentration",
       "<strong>Topping</strong> removes the auxin source, releasing side shoots into a bushier, "
       "multi-cola plant. LST flattens the auxin gradient for the same effect without cutting. "
       "Rooting gels are synthetic auxins (IBA/NAA) painted onto cuttings"],
      ["<strong>Cytokinin</strong>", "Root tips",
       "Promotes shoot growth and branching; counterweight to auxin; delays leaf ageing",
       "The auxin:cytokinin balance decides shoots-versus-roots — a big healthy root system "
       "literally signals the top to branch. Tissue-culture multiplication runs on added cytokinin "
       "(see <a href='tissue-culture.html'>tissue culture</a>)"],
      ["<strong>Gibberellin (GA)</strong>", "Young leaves, seeds",
       "Drives stem elongation and helps break seed dormancy",
       "The post-flip stretch is GA at work — and part of why crowding and shade (which shift light "
       "quality) make plants leggier. GA sprays can force male flowers for breeding, though STS "
       "does it better" + _c("flajsman-2021-feminized-seed-production")],
      ["<strong>Ethylene</strong>", "Stressed, wounded and ripening tissue",
       "Gas hormone: senescence, ripening, and a push toward female flower expression",
       "Blocking it with STS masculinises a female — the entire feminised-seed industry (section "
       "11). Its stress role is also why wounding and rough handling echo through the plant" + _c("flajsman-2021-feminized-seed-production")],
      ["<strong>ABA (abscisic acid)</strong>", "Roots and leaves under water stress",
       "The drought manager: closes stomata, slows expansion, enforces seed dormancy",
       "Controlled drybacks lean on ABA signalling — part of the mechanism crop steering uses to "
       "push a plant generative. Overdo it and the same hormone stalls growth entirely"],
    ], cls="compact",
       caption="The five levers. Concentrations, ratios and gradients — not on/off switches — decide the outcome."),
    callout("note", "Gradients, not switches",
      p("Hormones act by concentration and ratio, varying tissue by tissue. That is why topping "
        "releases only the nearest few nodes, why rooting gel goes on the cut and not the leaves, "
        "and why one stressor rarely has one tidy effect.")),
  ]})

# ------------------------------------------------------------------ 15 failure modes
SECTIONS.append({"id": "failure-modes", "kicker": "15 · What goes wrong", "title": "Failure modes: biology biting back",
  "blocks": [
    p("Most cultivation disasters are one of the mechanisms in this paper running exactly as "
      "designed, against you. The six below account for a large share of ruined first grows."),
    grid([
      card("Light leak in the dark period",
        p("Phytochrome resets, the night count restarts: flowering stalls, plants drift back toward "
          "veg, and the stress feeds herm risk. <strong>Fix:</strong> dark-adapt your eyes and walk "
          "the room during lights-off; tape LEDs, seal doors." + _c("legris-2019-phytochrome-mechanisms")),
        tag="photoperiod"),
      card("Stress stack in late flower",
        p("Heat spikes, light interruptions and damage push genetically female plants to throw "
          "anthers — bananas — and self-seed the room. <strong>Fix:</strong> stable climate, sealed "
          "dark period, herm-prone cultivars culled from the lineup." + _c("punja-holmes-2020-hermaphroditism")),
        tag="herm trigger"),
      card("Overwatering",
        p("Flooded substrate = zero root oxygen = uptake stops within hours. It looks like thirst "
          "from above, so beginners water again. <strong>Fix:</strong> judge by pot weight and "
          "dryback, never by droop alone." + _c("morard-1996-root-oxygen")),
        tag="root oxygen"),
      card("Pollen in the room",
        p("One open male or one banana, and a wind-pollinated species does the rest through your "
          "HVAC: a seeded crop. <strong>Fix:</strong> sex early at the nodes, cull males before "
          "flowers open, quarantine anything breeding-related." + _c("punja-holmes-2020-hermaphroditism")),
        tag="pollen"),
      card("Structural work at the wrong time",
        p("Topping and heavy training in flower spends the plant's budget on recovery while the "
          "buds queue for sugar. <strong>Fix:</strong> shape in veg; from bud set onward the "
          "meristems you care about are making flowers, not frames."),
        tag="timing"),
      card("Shopping by folk label",
        p("Buying 'a relaxing indica' is buying label art: the labels are genetically indistinct "
          "and predict aroma at best. <strong>Fix:</strong> chemotype and COA numbers, cultivar "
          "sheets, your own logs." + _c("watts-2021-terpene-synthase-labels")),
        tag="chemotype"),
    ], cols=2),
  ]})

# ------------------------------------------------------------------ 16 quick reference
SECTIONS.append({"id": "quick-reference", "kicker": "16 · Keep this", "title": "Quick reference: the whole vocabulary in one table",
  "blocks": [
    p("The working vocabulary of this site, one line each. Bookmark this section — every other "
      "paper uses these words without stopping to define them."),
    table(["Term", "Plain meaning", "Why you care"], [
      ["Annual", "Lives one season, flowers once, dies", "No mid-season restarts; plan the whole cycle"],
      ["Dioecious", "Male and female are separate plants", "Regular seed = ~half males to find and cull"],
      ["Chemotype", "Classification by measured chemistry (THC:CBD)", "Beats sativa/indica labels for predicting the product"],
      ["Node / internode", "Stem joint / stem between joints", "Node spacing reads stretch; nodes host every branch and bud"],
      ["Apical meristem", "The main growing tip", "Topping removes it to release side shoots"],
      ["Axillary bud", "Dormant backup tip at each node", "Raw material of every branch and training plan"],
      ["Fan / sugar leaf", "Big solar panels / small in-bud leaves", "Fan leaves fund the plant; sugar leaves flag trim work"],
      ["Bract", "Resin-dense pod around each ovary ('calyx' in slang)", "Highest trichome density on the plant"],
      ["Pistil / stigma", "Female organ / its two white hairs", "Stigma colour is a rough maturity hint"],
      ["Trichome", "Glandular resin factory (bulbous, sessile, stalked)", "Where cannabinoids and terpenes are made and stored"],
      ["Photoperiod", "Daily light length (the schedule)", "The lever that starts and holds flowering"],
      ["Critical night length", "Minimum unbroken darkness that triggers flower", "Why 12/12 works and why leaks break it"],
      ["Phytochrome (Pr/Pfr)", "The red/far-red pigment switch", "The sensor behind every photoperiod rule"],
      ["Autoflower", "Cultivar that flowers on age, not photoperiod", "Different contract: fast, schedule-free, unforgiving"],
      ["Pre-flower", "First solitary flower at a node", "Sexes the plant weeks before real flowering"],
      ["Hermaphrodite", "Female producing male anthers under stress/genetics", "A pollen source with no male in the room"],
      ["STS", "Silver thiosulfate — blocks ethylene signalling", "How feminised seed is made"],
      ["Source / sink", "Sugar exporter / sugar importer", "The economics behind defoliation and late yellowing"],
      ["Rhizosphere", "The living few millimetres around each root", "Where pH, microbes and uptake actually happen"],
    ], cls="compact", caption="The site's vocabulary in one place. Terms are defined in full in their sections above."),
    callout("key", "The mental model to keep",
      p("A cannabis plant is a sugar factory on a night clock. Veg builds the factory — leaves, "
        "roots, nodes. The long night flips the market, and flowers become the only customer. "
        "Hormones are the levers, trichomes are the product, roots are the half you manage by "
        "instruments, and every rule in every other paper traces back to one of those facts.")),
    p("From here, follow the plant's own order: <a href='seeds-germination.html'>seeds and "
      "germination</a> to start one, <a href='flowering-stages.html'>the flower cycle</a> to run "
      "bloom week by week, and <a href='lighting-fundamentals.html'>lighting fundamentals</a> for "
      "the hardware behind the photoperiod rules this chapter explained."),
  ]})
