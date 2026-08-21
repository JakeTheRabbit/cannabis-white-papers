# -*- coding: utf-8 -*-
"""Paper: cannabinoids & terpenes — where the chemistry is made, how it is built, and how it dies."""
import json, os
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        grid, card, chip, kv, steps)
import figs_lib as L

_FIGS = json.load(open(os.path.join(os.path.dirname(__file__), "figs_cannabinoids_terpenes.json"), encoding="utf-8"))

SLUG = "cannabinoids-terpenes"
TITLE = "Cannabinoids and terpenes: the chemistry that matters"
EYEBROW = "Reference · Chemistry"
SUB = ("Two families of molecules carry all the value in this industry. And both are built in the same "
       "microscopic gland, as acids, on one assembly line. This is the grower's field guide to that "
       "chemistry: where it is made, what each compound is and is not, how it degrades, and what you "
       "actually control.")
META = [("flask", "Reference"), ("image", "10 diagrams"),
        ("quote", "Evidence-linked · 18 sources"), ("clock", "~24 min read")]
RELATED = ["lab-testing-coas", "hash-rosin-pressing", "harvest-dry-trim-cure"]
REF_IDS = ["radwan2021-constituents", "livingston2020-trichomes", "gulck2020-biosynthesis",
           "fellermeier1998-cbga", "wang2016-decarb", "ross1997-cbn-age",
           "demeijer2003-chemotype", "demeijer2009-chemotype5", "booth2019-terpenes",
           "eyal2023-terpenes", "ross1996-volatileoil", "gertsch2008-caryophyllene",
           "smith2022-diversity", "russo2011-entourage", "cogan2020-entourage",
           "finlay2020-terpenoids", "fairbairn1976-stability", "rodriguez2021-uvb"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

# ---------------------------------------------------------------- 0 · start here
SECTIONS.append({"id": "start-here", "kicker": "Start here", "title": "Purpose and scope",
  "blocks": [
    lead("Every price negotiation, every lab report, every argument about quality in this industry comes "
         "down to two families of molecules: <strong>cannabinoids</strong> (the potency) and "
         "<strong>terpenes</strong> (the smell and flavour). Both are made in the same microscopic gland "
         "on the flower surface, the <strong>trichome</strong>, and almost everything a grower does "
         "either builds that gland's contents or wastes them. This paper is the field guide: where the "
         "compounds are made, how the plant assembles them, what each one is and is not, how they fall "
         "apart, and which levers you actually hold."),
    p("The scale of the chemistry is bigger than the market suggests: researchers have reported more than "
      "500 distinct compounds from cannabis, including 125 cannabinoids and about 120 terpenes"
      + _c("radwan2021-constituents") + ". Commercially, perhaps six cannabinoids and eight terpenes do "
      "nearly all the talking. Learn those, and every COA, every strain menu and every marketing claim "
      "becomes readable."),
    defterm("Cannabinoid", "A family of compounds effectively unique to cannabis (THC, CBD, CBG and "
            "relatives). They interact with receptor systems in humans; the plant most likely makes them "
            "for defence. The value driver of the crop."),
    defterm("Terpene", "Small, volatile oils that give plants their smell: pine, citrus, pepper, hops. "
            "Not unique to cannabis. They are the entire aroma and flavour of flower, and they evaporate "
            "far more easily than cannabinoids do."),
    defterm("Trichome", "The mushroom-shaped resin gland on flowers and sugar leaves, the visible "
            "&lsquo;frost&rsquo;. Both compound families are made and stored in its head."),
    defterm("Resin", "The sticky oil inside trichome heads: cannabinoid acids + terpenes + waxes. When "
            "people pay for potency or flavour, they are paying for resin."),
    defterm("THCA", "Tetrahydrocannabinolic acid, the form of THC the living plant actually makes. Not "
            "intoxicating until heat converts it (decarboxylation)."),
    defterm("Decarboxylation", "The heat-driven step that snaps a CO&#8322; group off a cannabinoid acid "
            "and switches the molecule to its active, neutral form. &lsquo;Decarb&rsquo; for short."),
    defterm("Chemotype", "A plant's genetically fixed cannabinoid ratio class: THC-dominant, balanced, "
            "CBD-dominant, CBG-dominant or cannabinoid-free. Set at germination; no grow tactic changes it."),
    defterm("COA", "Certificate of Analysis, the lab report listing cannabinoid and terpene content. The "
            "receipt for everything in this paper."),
    callout("note", "What this paper will not do",
      p("It will not tell you what any compound does to a patient. Effects are described here only as "
        "<em>reported</em> or <em>under study</em>, because that is the honest state of most of the "
        "evidence, and because therapeutic claims are the regulator's and clinician's lane, not a grow "
        "guide's. This is chemistry for growers: what the molecules are, where they come from, and how "
        "not to lose them.")),
  ]})

# ---------------------------------------------------------------- 1 · core answer
SECTIONS.append({"id": "core-answer", "kicker": "The short version", "title": "Chemistry overview",
  "blocks": [
    p("Everything the industry trades on is made in <strong>trichome heads</strong>, as <strong>acids</strong> "
      "(THCA, CBDA, not THC and CBD), on <strong>one assembly line</strong> whose hub is a single molecule: "
      "<strong>CBGA</strong>, the &lsquo;mother cannabinoid&rsquo;" + _c("gulck2020-biosynthesis") + ". "
      "Genetics decide the <em>ratio</em> of the outputs (the chemotype) and largely fix the terpene "
      "palette" + _c("demeijer2003-chemotype") + "; the grow decides <em>how much</em> gets made; and "
      "everything after harvest only subtracts."),
    p("The two families die differently, and that difference runs half this paper. <strong>Terpenes "
      "evaporate</strong>, the light &lsquo;monoterpenes&rsquo; at room temperature, which is why hot fast "
      "drying smells wonderful and costs you the product" + _c("eyal2023-terpenes") + ". "
      "<strong>Cannabinoids oxidise</strong>, THC grinds slowly into CBN under oxygen, heat and time, and "
      "light destroys it faster than anything else" + _c("fairbairn1976-stability") + ". Flavour is lost to "
      "warm air; potency is lost to light, oxygen and years."),
    callout("key", "The one-sentence version",
      p("Potency and flavour are built once, in the same gland, as fragile acids and volatile oils, the "
        "grower's job is to pick genetics that can make them, keep the plant healthy enough to fill the "
        "warehouse, and then get out of chemistry's way: cool, dark, gentle, sealed.")),
  ]})

# ---------------------------------------------------------------- 2 · where it's made
SECTIONS.append({"id": "where-made", "kicker": "The factory", "title": "Trichome secretory cells",
  "blocks": [
    p("Cannabis carries three kinds of glandular trichome: tiny <strong>bulbous</strong> glands, "
      "<strong>sessile</strong> glands that sit flat on the surface, and the money-maker, the "
      "<strong>capitate-stalked</strong> trichome, a resin head lifted on a stalk. Detailed microscopy "
      "shows the stalked heads carry <strong>12–16 secretory disc cells</strong> at their base, versus "
      "eight in sessile heads, and it is the stalked type whose signature tracks high cannabinoid "
      "content" + _c("livingston2020-trichomes") + ". Strikingly, stalked trichomes develop <em>from</em> "
      "sessile-looking intermediates as the flower matures, the frost you watch build through flowering "
      "is a population growing up, not just growing more" + _c("livingston2020-trichomes") + "."),
    figure(_FIGS["trichome_cell"], 1,
      "The capitate-stalked trichome in cross-section. The disc cells at the base of the head are the "
      "factory; the cuticle-bound storage cavity above them is the warehouse. Stalked heads carry 12–16 "
      "disc cells and the high-cannabinoid, monoterpene-rich profile; sessile heads make do with "
      "eight" + _c("livingston2020-trichomes") + "."),
    p("The division of labour matters. The <strong>disc cells are the factory floor</strong>, isolated "
      "trichomes show intense expression of the cannabinoid and terpene biosynthesis genes"
      + _c("livingston2020-trichomes") + ", and the finished resin is exported into the "
      "<strong>storage cavity</strong>, a sac whose only wall is a stretched waxy cuticle. The plant does "
      "not reabsorb it. Once made, the inventory just sits there: defended, fragile, and entirely "
      "surface-mounted."),
    p("Three practical consequences fall straight out of the anatomy:"),
    ul(["<strong>Potency lives on the surface.</strong> Resin scales with bract and sugar-leaf surface "
        "area, not bud mass. Which is part of why dense, well-lit flower with high bract density assays "
        "above larfy bulk.",
        "<strong>Every rough touch is theft.</strong> The cavity wall is a film of wax. Tumbling, "
        "squeezing, over-handling and aggressive trimming rupture heads and leave the resin on gloves and "
        "machinery instead of in the jar.",
        "<strong>The whole solventless industry is anatomy.</strong> Ice-water hash and dry sift are just "
        "ways of snapping cold, brittle heads off intact, collecting the warehouse without the building."]),
    callout("tip", "Look at your frost with better eyes",
      p("A loupe tells you more than a lab turnaround: head density, head size, and how intact the heads "
        "are after handling. If your trim room's product looks sandblasted under 60×, the potency you "
        "grew is in the machine, not the bag.")),
  ]})

# ---------------------------------------------------------------- 3 · biosynthesis
SECTIONS.append({"id": "biosynthesis", "kicker": "The assembly line", "title": "Cannabinoid and terpene biosynthesis",
  "blocks": [
    p("The pathway reads like a small factory diagram, and it is worth learning because chemotypes, CBG "
      "flower, THCV and half the COA make sense only downstream of it. The plant starts with "
      "<strong>hexanoyl-CoA</strong>, a six-carbon starter drawn from fatty-acid metabolism, and extends "
      "it with three <strong>malonyl-CoA</strong> units to build <strong>olivetolic acid</strong>, the "
      "aromatic core, using a polyketide synthase working with olivetolic acid cyclase (OAC)"
      + _c("gulck2020-biosynthesis") + "."),
    p("Then the two halves of the molecule meet. A membrane-bound prenyltransferase, first demonstrated "
      "in 1998 as <strong>GOT</strong>, geranylpyrophosphate:olivetolate geranyltransferase, bolts a "
      "ten-carbon terpene unit, <strong>geranyl diphosphate (GPP)</strong>, onto olivetolic acid. The "
      "product is <strong>cannabigerolic acid, CBGA</strong>. The enzyme is fussy: it accepts olivetolic "
      "acid but not its decarboxylated cousin olivetol, which is why the plant's whole line runs in acid "
      "form" + _c("fellermeier1998-cbga") + "."),
    figure(_FIGS["pathway"], 2,
      "The map. A fatty-acid-derived starter plus a terpene unit meet at CBGA, and three oxidocyclase "
      "enzymes (THCA, CBDA and CBCA synthase) each fold CBGA into a different acid"
      + _c("gulck2020-biosynthesis") + _c("fellermeier1998-cbga") + ". Note what is missing: no branch "
      "makes CBN, and no branch makes neutral THC."),
    p("CBGA is the hub, the <strong>mother cannabinoid</strong>. Three synthases compete for it: "
      "<strong>THCA synthase</strong> folds it into THCA, <strong>CBDA synthase</strong> into CBDA, and "
      "<strong>CBCA synthase</strong> into CBCA" + _c("gulck2020-biosynthesis") + ". Which of those "
      "enzymes a plant carries in working order is exactly what the chemotype locus encodes, hold that "
      "thought for two sections."),
    p("Two footnotes worth knowing. First, the <strong>propyl series</strong>: when the line starts from a "
      "shorter starter, the same machinery yields divarinic acid, then CBGVA, then <strong>THCVA and "
      "CBDVA</strong>, the three-carbon-tail &lsquo;varin&rsquo; cannabinoids like THCV"
      + _c("gulck2020-biosynthesis") + _c("radwan2021-constituents") + ". Second, the absences: the plant "
      "makes essentially no CBN and very little neutral THC. Both are breakdown products of what the "
      "enzymes made, not products of the enzymes" + _c("gulck2020-biosynthesis") + "."),
    callout("note", "Why a grower should care about an enzyme map",
      p("Because it converts three market curiosities into obvious chemistry: CBG-rich flower is a plant "
        "whose downstream synthases are broken, so the hub piles up; chemotype is which synthase alleles "
        "you inherited, so no environment trick flips THC into CBD; and CBN on a COA is a storage report, "
        "not a genetic trait you can breed toward or away from at the synthase level.")),
  ]})

# ---------------------------------------------------------------- 4 · acids & decarb
SECTIONS.append({"id": "acids-decarb", "kicker": "Acid vs neutral", "title": "Decarboxylation: THCA and THC",
  "blocks": [
    p("The single most misunderstood fact in cannabis chemistry: <strong>the living plant does not make "
      "THC</strong> in any meaningful quantity. It makes THCA, the same molecule wearing a carboxyl "
      "group (–COOH). And THCA is <strong>not intoxicating</strong> in that form. Raw flower is, "
      "chemically speaking, a bag of inactive acid. Heat removes the carboxyl group as CO&#8322; gas and "
      "switches the molecule on: that is <strong>decarboxylation</strong>" + _c("wang2016-decarb") + "."),
    figure(_FIGS["decarb"], 3,
      "The switch. Heat snaps the –COOH off THCA; CO&#8322; leaves as gas (12.3% of the molecule's mass) "
      "and Δ9-THC remains. The 0.877 factor on every COA is this mass loss, nothing more."),
    p("A lit joint or a vape coil decarbs in a fraction of a second. Everything else (ovens, extracts, "
      "edibles processing) runs on kinetics, and the kinetics have been measured properly. Heating "
      "cannabis extract between 80 °C and 145 °C, Wang and colleagues found decarboxylation follows "
      "clean <strong>first-order</strong> behaviour, with rate constants for THCA of 0.18, 0.66 and "
      "1.83 × 10&#8315;&#179; s&#8315;&#185; at 80, 95 and 110 °C" + _c("wang2016-decarb") + ". Translated: "
      "at 110 °C, half the remaining THCA converts roughly every six minutes."),
    figure(L.line("THCA converting at 110 °C (first-order decay)",
        [("", 100), ("", 71.9), ("", 51.7), ("", 37.2), ("", 26.8), ("", 19.3),
         ("", 13.9), ("", 10.0), ("", 7.2), ("", 5.2), ("", 3.7)],
        ["0", "3", "6", "9", "12", "15", "18", "21", "24", "27", "30"],
        ylab="% THCA remaining",
        note="Computed from the measured first-order rate constant k = 1.83 × 10⁻³ s⁻¹ at 110 °C; half-life ≈ 6.3 min. X-axis in minutes.",
        ymax=100), 4,
      "What first-order means in practice: conversion is fast at the start and asymptotic at the end, "
      "the last few percent of acid take as long as the first fifty. Curve computed from the rate "
      "constant measured by Wang et al." + _c("wang2016-decarb")),
    p("The acids are not all equally willing. THCA converts about <strong>twice as fast</strong> as CBDA "
      "or CBGA at the same temperature. Its activation energy is lower (88 kJ/mol vs 112 and 109)"
      + _c("wang2016-decarb") + ". Anyone processing CBD material on a THC schedule under-decarbs it."),
    figure(L.bars("Half-life of each acid at 110 °C",
        [("THCA", 6.3), ("CBGA", 11.6), ("CBDA", 13.9)],
        unit=" min",
        note="Half-life = ln 2 ÷ k, from the first-order rate constants measured at 110 °C. THCA is the eager one.",
        maxv=16), 5,
      "Same oven, different clocks. CBDA and CBGA need roughly double THCA's time at a given temperature"
      ", derived from the rate constants in Wang et al." + _c("wang2016-decarb")),
    p("Decarb is a two-front war. Stop too early and inactive acid remains; push too hot or too long and "
      "you start burning the building down, the freed THC oxidises onward toward CBN, and the "
      "monoterpenes, whose volatility at decarb temperatures is enormous, stream out of the "
      "material" + _c("eyal2023-terpenes") + ". One detail from the kinetics work is telling: run under "
      "vacuum, THCA converted to THC with <em>no CBN formation observed</em>, starve the reaction of "
      "oxygen and the onward degradation largely stops" + _c("wang2016-decarb") + "."),
    callout("warn", "Decarb never fully stops",
      p("Room temperature is just a very slow oven. Flower in storage drifts from acid toward neutral "
        "over months. Which is why an old jar assays differently from the COA printed at harvest, before "
        "any potency was actually lost. If total THC is stable but the THCA:THC split has moved, you are "
        "watching decarb, not degradation.")),
  ]})

# ---------------------------------------------------------------- 5 · cannabinoid roster
SECTIONS.append({"id": "cannabinoid-roster", "kicker": "The majors", "title": "Major cannabinoids",
  "blocks": [
    p("Six cannabinoids cover nearly every commercial conversation. For each: what it is, where it comes "
      "from, and, just as important, what it is <em>not</em>. Effects language here is deliberately "
      "conservative: <em>reported</em> means human use reports and early studies, not established "
      "medicine."),
    grid([
      card("Δ9-THC / THCA",
        p("<strong>What it is:</strong> the principal intoxicating cannabinoid; in the plant, almost "
          "entirely present as THCA. The molecule the drug-type market prices.<br><strong>What it is "
          "not:</strong> a quality score. Two flowers at 20% total THC can be worlds apart in aroma, "
          "freshness and resin condition. Potency is one column of the COA, not the verdict."),
        tag="the headline act"),
      card("CBD / CBDA",
        p("<strong>What it is:</strong> the major non-intoxicating cannabinoid; dominant in chemotype III "
          "plants and the hemp industry's backbone. Among the most-studied cannabinoids in medicine."
          "<br><strong>What it is not:</strong> a licence for claims. What CBD does or does not treat is "
          "clinical territory; a grower's honest statement stops at the measured percentage."),
        tag="the other pillar"),
      card("CBG / CBGA",
        p("<strong>What it is:</strong> the neutral form of the mother acid. Most flower shows well under "
          "1% because CBGA gets consumed making everything else; chemotype IV cultivars accumulate it "
          "because their downstream synthases are broken" + _c("demeijer2009-chemotype5") + "."
          "<br><strong>What it is not:</strong> &lsquo;the new THC&rsquo;. It is non-intoxicating, and "
          "most claims around it are marketing running ahead of evidence."),
        tag="the mother's remainder"),
      card("CBN",
        p("<strong>What it is:</strong> the oxidation product of THC. Heat, oxygen and time (not any "
          "enzyme) make it. So reliable a breakdown marker that the CBN:THC ratio is used to estimate the "
          "age of stored samples" + _c("ross1997-cbn-age") + ".<br><strong>What it is not:</strong> a "
          "proven sleep aid. The &lsquo;sedating cannabinoid&rsquo; story is popular and thinly "
          "evidenced; on a COA, read CBN first as a freshness flag."),
        tag="the age stamp"),
      card("CBC / CBCA",
        p("<strong>What it is:</strong> the third branch off CBGA, via CBCA synthase; known since the "
          "1960s and genuinely one of the majors on paper" + _c("radwan2021-constituents") + ". "
          "Non-intoxicating; usually present at fractions of a percent.<br><strong>What it is not:</strong> "
          "something most growers will ever select for, labs often don't even report it separately."),
        tag="the quiet branch"),
      card("THCV / THCVA",
        p("<strong>What it is:</strong> THC's short-tailed &lsquo;propyl&rsquo; cousin from the varin "
          "line, first isolated in 1971; certain lineages carry meaningfully more"
          + _c("radwan2021-constituents") + ".<br><strong>What it is not:</strong> an established "
          "appetite or energy product. Reported effects are under active study; supply is scarce and "
          "mostly a breeding story for now."),
        tag="the propyl cousin"),
    ], cols=2),
    callout("note", "The other 119",
      p("Most of the remaining catalogued cannabinoids are trace relatives, isomers, or artefacts of "
        "heat, light and analysis, real chemistry, marginal commerce" + _c("radwan2021-constituents") + ". "
        "If a product sheet leads with an exotic letter combination, ask for the COA line that "
        "quantifies it.")),
  ]})

# ---------------------------------------------------------------- 6 · chemotypes
SECTIONS.append({"id": "chemotypes", "kicker": "Genetics first", "title": "Chemotypes I–V and inherited ratios",
  "blocks": [
    p("Cross a true THC plant with a true CBD plant and score the offspring, and cannabinoid ratio "
      "behaves like a textbook Mendelian trait. The classic genetic work resolved it to a single locus, "
      "<strong>B</strong>, with two codominant alleles: B<sub>T</sub> (functional THCA synthase) and "
      "B<sub>D</sub> (functional CBDA synthase). Two copies of B<sub>T</sub> gives a THC-dominant plant "
      "(chemotype I); two of B<sub>D</sub> gives CBD-dominant (chemotype III); one of each gives the "
      "mixed, roughly 1:1 chemotype II, and F&#8322; crosses segregate 1:2:1, exactly as Mendel would "
      "have it" + _c("demeijer2003-chemotype") + "."),
    figure(_FIGS["chemotypes"], 6,
      "The five chemotypes. I–III are the B-locus story: which synthase alleles the plant carries"
      + _c("demeijer2003-chemotype") + ". Type IV accumulates CBGA because downstream conversion is "
      "crippled; type V, genuinely cannabinoid-free, traces to a recessive knockout (o/o) that also "
      "segregates 1:2:1" + _c("demeijer2009-chemotype5") + "."),
    p("The outer chemotypes complete the map. <strong>Type IV</strong> plants carry non-functional "
      "downstream synthases, so the mother acid CBGA accumulates. This is where CBG flower comes from. "
      "<strong>Type V</strong> plants make no cannabinoids at all: crosses with normal plants showed a "
      "single recessive factor (allele <em>o</em>) that blocks the pathway outright, again segregating "
      "1:2:1" + _c("demeijer2009-chemotype5") + ". Chemotype V is a fibre-breeding and research "
      "curiosity, but it proves the point: every rung of the ratio ladder is genetics."),
    p("The crucial nuance: the locus controls the <strong>ratio</strong>, not the <strong>amount</strong>. "
      "How much total cannabinoid a plant makes is polygenic and environment-sensitive, canopy health, "
      "light, maturity at harvest. So breeding and seed choice set the split; the grow sets the size of "
      "the pie" + _c("demeijer2003-chemotype") + "."),
    callout("tip", "Buying genetics with your eyes open",
      p("Chemotype is testable from a young plant's leaf assay. You do not need to flower out a room to "
        "learn a &lsquo;CBD line&rsquo; is really chemotype II and will run hot on THC. For a medicinal "
        "market that buys certified ratios, verify chemotype before a cultivar earns bench space.")),
  ]})

# ---------------------------------------------------------------- 7 · terpene classes
SECTIONS.append({"id": "terpene-classes", "kicker": "The volatile half", "title": "Terpene classes and volatility",
  "blocks": [
    p("Terpenes are built from five-carbon isoprene units, and the count is the classification: "
      "<strong>monoterpenes</strong> (two units, C10 — myrcene, limonene, pinene, terpinolene, linalool) "
      "and <strong>sesquiterpenes</strong> (three units, C15 — caryophyllene, humulene)"
      + _c("booth2019-terpenes") + ". Cannabis makes both in the same trichomes as the cannabinoids, "
      "around 61 monoterpenes and 51 sesquiterpenes have been reported across the "
      "species" + _c("radwan2021-constituents") + ", and a dedicated family of terpene synthase genes "
      "sets which ones a cultivar leans on" + _c("booth2019-terpenes") + "."),
    p("The class difference that matters operationally is <strong>volatility</strong>. Measured vapour "
      "pressures at 20 °C put the monoterpenes around 1–4 Torr, α-pinene 3.57, β-pinene 2.18, myrcene "
      "1.69, limonene 1.13 — while the sesquiterpenes sit roughly two orders of magnitude lower "
      "(β-caryophyllene 0.021, α-humulene 0.010). The cannabinoids are barely on the same chart: CBD at "
      "6.3 × 10&#8315;&#8310; and THC at 5.2 × 10&#8315;&#8311; Torr" + _c("eyal2023-terpenes") + "."),
    figure(_FIGS["volatility"], 7,
      "Seven orders of magnitude on one ladder. Monoterpenes evaporate at room temperature; "
      "sesquiterpenes hang on ~100× harder; cannabinoids effectively do not evaporate at all. Values "
      "measured at 20 °C" + _c("eyal2023-terpenes") + ". The popular &lsquo;THC boils at 157 °C&rsquo; "
      "charts are wrong, its true boiling point extrapolates past 400 °C" + _c("eyal2023-terpenes") + "."),
    p("This single chart explains the drying room. Track the volatile oil of the same buds fresh and "
      "after air-drying and storage, and the monoterpene share collapses from about <strong>92% to 62%</strong> "
      "over three months while the sesquiterpene share climbs to fill the gap"
      + _c("ross1996-volatileoil") + _c("radwan2021-constituents") + ", the bright, sharp top notes "
      "leave first, and the profile drifts toward pepper and wood. Notably, drying changed the oil's "
      "<em>proportions</em>, not its ingredient list" + _c("ross1996-volatileoil") + ": nothing new "
      "appears, the light fraction just walks away. Cold, slow, dark drying is not folklore; it is "
      "vapour-pressure management."),
    callout("key", "Volatility is also why terpenes are the honesty test of a supply chain",
      p("Potency survives sloppy logistics; aroma does not. A sample can hold its THC number through a "
        "hot van and a month on a shelf while its monoterpenes quietly leave. When flower smells flat "
        "but assays fine, this ladder is what happened.")),
  ]})

# ---------------------------------------------------------------- 8 · terpene roster
SECTIONS.append({"id": "terpene-roster", "kicker": "The big eight", "title": "Commercially relevant terpenes",
  "blocks": [
    p("Commercial cannabis clusters into a small number of terpene profiles. Analysis of tens of "
      "thousands of US retail samples found products fall into three broad groups: high "
      "<strong>caryophyllene + limonene</strong>, high <strong>myrcene + pinene</strong>, and high "
      "<strong>terpinolene + myrcene</strong>" + _c("smith2022-diversity") + ", and that popular "
      "indica/sativa/hybrid labels map poorly onto the underlying chemistry"
      + _c("smith2022-diversity") + ". Here are the eight names worth knowing; aroma is fact, effect "
      "folklore is flagged as folklore."),
    grid([
      card("Myrcene", p("Monoterpene. Earthy, musky, ripe-mango. The most common heavyweight in "
        "commercial flower and an anchor of two of the three market clusters" + _c("smith2022-diversity") + ". "
        "The &lsquo;couch-lock terpene&rsquo; story is folklore. What is demonstrated is aroma and "
        "abundance, not sedation."), tag="the default"),
      card("Limonene", p("Monoterpene. Citrus peel. Pairs with caryophyllene in one major market "
        "cluster" + _c("smith2022-diversity") + ". Bright, volatile (1.13 Torr at 20 °C"
        + _c("eyal2023-terpenes") + "), a freshness indicator as much as a flavour."), tag="citrus"),
      card("α- / β-Pinene", p("Monoterpenes. Pine needle, resin. The most volatile of the majors "
        "(α-pinene 3.57 Torr" + _c("eyal2023-terpenes") + "), first out the door in a warm dry. Memory "
        "and alertness claims remain under study; treat as aroma."), tag="first to leave"),
      card("Terpinolene", p("Monoterpene. Complex, floral, piney, a little petrol. Rarely dominant, but "
        "when it is, it defines the cultivar's whole nose; one of the three cluster signatures"
        + _c("smith2022-diversity") + "."), tag="the outlier"),
      card("β-Caryophyllene", p("Sesquiterpene, pepper, clove. The exception in all of terpene science: "
        "it is a genuine cannabinoid-receptor ligand, a selective CB2 agonist (Ki = 155 nM) with no "
        "CB1 binding, a &lsquo;dietary cannabinoid&rsquo; also found in black pepper"
        + _c("gertsch2008-caryophyllene") + ". CB2 is not the intoxication receptor, so this is "
        "pharmacology, not potency. Low volatility; survives drying well" + _c("eyal2023-terpenes") + "."),
        tag="the special case"),
      card("Linalool", p("Monoterpene alcohol. Lavender. Almost always minor in cannabis, loud when "
        "present. The relaxation story borrows heavily from lavender-oil research, not cannabis "
        "trials, under study, not established."), tag="floral"),
      card("α-Humulene", p("Sesquiterpene, hops (it is the signature hop aroma compound), woody and "
        "bitter. Caryophyllene's constant companion and the least volatile major measured (0.010 Torr"
        + _c("eyal2023-terpenes") + ")."), tag="the survivor"),
      card("Ocimene", p("Monoterpene. Sweet, green, herbal. A frequent supporting player that spikes in "
        "some cultivars; like the other monoterpenes, easily lost to heat."), tag="supporting cast"),
    ], cols=2),
    callout("note", "Why caryophyllene gets a longer entry",
      p("Every terpene gets marketed with receptor language; caryophyllene is the only one where the "
        "receptor claim is demonstrated, replicated pharmacology" + _c("gertsch2008-caryophyllene") + ". "
        "Careful screening of the other majors found no direct CB1 or CB2 activity at plausible "
        "concentrations" + _c("finlay2020-terpenoids") + ". One real example and many assumed ones, "
        "which is the entourage story in miniature.")),
  ]})

# ---------------------------------------------------------------- 9 · entourage honesty
SECTIONS.append({"id": "entourage", "kicker": "Honesty section", "title": "Entourage effect: evidence and marketing claims",
  "blocks": [
    p("The claim: cannabis compounds work better together than in isolation, terpenes and minor "
      "cannabinoids shape, soften or steer THC's effect. The most influential statement of it is Russo's "
      "2011 review proposing phytocannabinoid–terpenoid synergy across a range of indications"
      + _c("russo2011-entourage") + ". It is a genuinely interesting hypothesis paper, and its own "
      "language is conditional: synergy, <em>if proven</em>, would open new product pipelines"
      + _c("russo2011-entourage") + "."),
    p("What does the ledger actually show? On the demonstrated side: caryophyllene really is a CB2 "
      "agonist" + _c("gertsch2008-caryophyllene") + ", cannabis produces hundreds of co-occurring "
      "compounds" + _c("radwan2021-constituents") + ", and pharmacology has plenty of precedent for "
      "mixture effects. On the other side: when the five most common terpenes were tested directly, "
      "alone and combined with THC, at human CB1 and CB2 receptors, they showed <strong>no receptor "
      "activity and no modulation of THC's signal</strong>" + _c("finlay2020-terpenoids") + ". And the "
      "sceptical reviews land hard: the term began as a &lsquo;hypothetical afterthought&rsquo; in 1998 "
      "and has been rebranded and marketed far beyond its evidence, with the possibility of unfavourable "
      "interactions rarely mentioned" + _c("cogan2020-entourage") + "."),
    table(["Status", "Claim", "Where it stands"], [
      ["<strong>Demonstrated</strong>", "β-caryophyllene activates CB2 (Ki 155 nM), no CB1",
       "Replicated receptor pharmacology" + _c("gertsch2008-caryophyllene")],
      ["<strong>Demonstrated</strong>", "Cannabis is polypharmacy, hundreds of co-occurring compounds",
       "Uncontroversial chemistry" + _c("radwan2021-constituents")],
      ["<strong>Not demonstrated</strong>", "Common terpenes act at CB1/CB2 or modulate THC there",
       "Direct tests were negative" + _c("finlay2020-terpenoids")],
      ["<strong>Hypothesis</strong>", "Whole-flower effects differ meaningfully from isolate THC",
       "Proposed, plausible, unproven at product level" + _c("russo2011-entourage") + _c("cogan2020-entourage")],
      ["<strong>Marketing</strong>", "&lsquo;This terpene profile delivers this effect&rsquo;",
       "No controlled evidence for any specific profile→effect map" + _c("cogan2020-entourage")],
    ], cls="compact", caption="The entourage ledger, honestly kept."),
    p("The honest reading is narrow: mixtures <em>might</em> matter, one mechanism is real, the specific "
      "profile-to-effect promises on retail menus are unsupported, and terpene-CB-receptor mechanisms "
      "have been directly tested and found wanting. None of this makes terpenes worthless. They are the "
      "product's flavour, its freshness record, and its identity. That is value enough without borrowed "
      "pharmacology."),
    callout("key", "How to sell chemistry without overselling it",
      p("State what you measured: cannabinoid ratio, total terpenes, the top five by weight, harvest and "
        "test dates. Describe aroma in aroma words. Leave effects to the people licensed to discuss them. "
        "In a medicinal framework, that is a compliance requirement.")),
  ]})

# ---------------------------------------------------------------- 10 · degradation
SECTIONS.append({"id": "degradation", "kicker": "The clock", "title": "Cannabinoid and terpene degradation",
  "blocks": [
    p("Two decays run in parallel from the moment of harvest, and they have different physics. "
      "<strong>Terpenes evaporate</strong>, fastest when warm, monoterpenes first (previous sections). "
      "<strong>Cannabinoids oxidise</strong>. THC's endpoint is CBN, and the drivers are oxygen, heat, "
      "light and time. Neither decay reverses. Every storage decision is a rate control on these two "
      "processes."),
    figure(_FIGS["thc_cbn"], 8,
      "The one-way road. Decarboxylation moves THCA into the active window; oxidation grinds THC on into "
      "CBN. Light is the odd driver out. It destroys THC fastest of all, but by routes that do not "
      "produce CBN" + _c("fairbairn1976-stability") + ". Storage losses shown from the four-year "
      "room-temperature study" + _c("ross1997-cbn-age") + "."),
    p("The numbers are sobering. Flower stored at 20–22 °C in the dark lost on average <strong>16.6% of "
      "its THC in the first year</strong>, 26.8% by year two, 34.5% by year three and 41.4% by year four"
      ", and the CBN:THC ratio climbed so predictably that it is used forensically to estimate sample "
      "age" + _c("ross1997-cbn-age") + "."),
    figure(L.bars("THC remaining in dark room-temperature storage",
        [("Harvest", 100), ("Year 1", 83), ("Year 2", 73), ("Year 3", 66), ("Year 4", 59)],
        unit="%",
        note="Plant material at 20–22 °C in the dark; mean losses (±6–8%) from the four-year storage study.",
        maxv=110), 9,
      "Two-fifths of the potency gone in four years, in <em>good</em> conditions (dark, room "
      "temperature). Warmth, light and air headspace all steepen this curve" + _c("ross1997-cbn-age") + "."),
    p("The classic stability work adds the ranking of enemies. Across two years of storage trials, "
      "<strong>exposure to light, not even direct sun, was the greatest single factor</strong> in "
      "cannabinoid loss; temperature up to 20 °C was insignificant by comparison; and air oxidation "
      "caused significant losses of its own" + _c("fairbairn1976-stability") + ". The same work supplies "
      "the mechanism nuance in Figure 8: THC lost to light does <em>not</em> reappear as CBN, while THC "
      "lost to air in the dark does, so a high-CBN sample was stored warm and airy, not necessarily "
      "bright" + _c("fairbairn1976-stability") + ". Well-kept material, meanwhile, was &lsquo;reasonably "
      "stable&rsquo; for one to two years in the dark at room temperature" + _c("fairbairn1976-stability") + "."),
    p("Terpenes degrade in storage too, not only by evaporation but by <strong>oxidation</strong>, which "
      "changes their character rather than their quantity: oxidised monoterpene notes read as stale, "
      "piney-turned-solvent, old-spice-rack. The proportional drift measured in dried, stored buds (the "
      "92% → 62% monoterpene slide) is both losses stacked together" + _c("ross1996-volatileoil") + "."),
    kv([("Light", "the #1 killer, opaque containers, dark rooms, no display jars" + _c("fairbairn1976-stability")),
        ("Temperature", "cool always beats warm; every process on this page is temperature-driven"),
        ("Oxygen", "the CBN route, full containers, minimal headspace, sealed" + _c("fairbairn1976-stability")),
        ("Surface area", "whole buds keep their own cuticle armour; grinding multiplies every loss"),
        ("Time", "the one you cannot switch off, sell fresh, date everything" + _c("ross1997-cbn-age"))]),
    callout("warn", "The display jar is a slow incinerator",
      p("A clear jar under retail lighting combines the top killer (light), warmth from the fixtures, "
        "and a headspace refreshed at every opening. It is the perfect machine for converting flower "
        "into CBN and flat aroma, keep display stock separate from sale stock.")),
  ]})

# ---------------------------------------------------------------- 11 · grower levers
SECTIONS.append({"id": "grower-levers", "kicker": "Control, honestly ranked", "title": "Cultivation levers and their limits",
  "blocks": [
    p("Ranked by how much they move the number, with the evidence state attached. Because this is where vendor claims and "
      "grow-forum folklore concentrate."),
    ol(["<strong>Genetics, dominant, and it isn't close.</strong> Chemotype is Mendelian"
        + _c("demeijer2003-chemotype") + "; the terpene palette is written in the cultivar's terpene "
        "synthase genes" + _c("booth2019-terpenes") + "; commercial chemistry clusters by cultivar family"
        + _c("smith2022-diversity") + ". If the plant cannot make it, nothing in your environment recipe "
        "will summon it.",
        "<strong>Harvest timing.</strong> Trichome populations mature, heads develop, profiles shift "
        "measurably as flowers ripen" + _c("livingston2020-trichomes") + ". Picking on the calendar "
        "instead of the trichome forfeits chemistry you already paid to grow.",
        "<strong>Plant health and light.</strong> A full, healthy, well-lit canopy grows more trichome "
        "real estate. This is the honest path to &lsquo;more terpenes&rsquo;: more gland, not magic "
        "inputs.",
        "<strong>Environment tweaks, small, contested, cultivar-dependent.</strong> See the UV story "
        "below before spending money here.",
        "<strong>Post-harvest, zero upside, unlimited downside.</strong> Drying, curing and storage "
        "can only preserve (previous section). Rate-control, not production."]),
    p("The <strong>UV myth</strong> deserves its own paragraph because it sells hardware. The story, "
      "UV stress drives THC up as a sunscreen response, leans on small, decades-old studies. When it "
      "was finally tested properly in modern drug-type cultivars indoors, across a range of UV-B doses: "
      "<strong>no increase in cannabinoid concentration, no increase in yield, and progressively more "
      "photosynthetic damage as dose rose</strong>" + _c("rodriguez2021-uvb") + ". That is one careful "
      "trial on two cultivars, not the final word for every genotype and spectrum, but the burden of "
      "proof now sits squarely on the UV vendor, not the sceptic."),
    callout("note", "Evidence state for environment claims, in one line",
      p("Controlled trials keep finding the same shape: genetics and plant health dominate; "
        "environmental &lsquo;stress hacks&rsquo; deliver small, inconsistent, cultivar-specific "
        "chemistry changes at real cost to yield. Any input promising +30% terpenes should come with a "
        "COA pair and a cultivar name, or it's a story.")),
  ]})

# ---------------------------------------------------------------- 12 · COA tie-in
SECTIONS.append({"id": "coa", "kicker": "The receipt", "title": "Cannabinoids and terpenes on a COA",
  "blocks": [
    p("A COA is this whole paper compressed into a table. The cannabinoid section reports <strong>acid "
      "and neutral forms separately</strong>, fresh, well-kept flower shows nearly everything as THCA "
      "with a sliver of THC. The two are combined with the decarb arithmetic from Figure 3:"),
    kv([("total THC", "THC + 0.877 × THCA, the 0.877 is the mass surviving CO&#8322; loss"),
        ("total CBD", "CBD + 0.877 × CBDA, same factor, same reason"),
        ("Why 0.877", "molar masses: 314.5 (neutral) ÷ 358.5 (acid). Bookkeeping, not biology"),
        ("Dry-weight basis", "results are usually corrected for moisture, check which basis before comparing labs")]),
    p("Read past the headline number and the COA becomes a <strong>history of the sample</strong>:"),
    ul(["<strong>High THCA, low THC, negligible CBN</strong>, fresh material, handled cool. What you "
        "want to see.",
        "<strong>Neutral fraction creeping up</strong>, age or heat exposure; decarb has been running "
        "in storage (Section 5).",
        "<strong>CBN present and climbing</strong>, the age stamp: warm, airy or simply old storage"
        + _c("ross1997-cbn-age") + ".",
        "<strong>Terpene total low, sesquiterpene-heavy for the cultivar</strong>. The monoterpenes have "
        "left; hot dry or long shelf time" + _c("ross1996-volatileoil") + ".",
        "<strong>Chemotype mismatch</strong>, a &lsquo;CBD cultivar&rsquo; reporting substantial THC is "
        "chemotype II genetics doing exactly what its B locus says" + _c("demeijer2003-chemotype") + "."]),
    p("Terpene panels typically report a percent-by-weight list with the top handful of compounds doing "
      "most of the total; profile shape is cultivar identity" + _c("smith2022-diversity") + ", and its "
      "condition is your process record. Sampling, uncertainty, and how labs vary is its own subject, "
      "covered in the lab testing paper in this series."),
    callout("tip", "Use the COA pair trick",
      p("One COA describes a sample. Two COAs of the same lot, at packaging and months later, describe "
        "your storage. The deltas (THCA→THC drift, CBN appearance, monoterpene fade) are exactly the "
        "degradation chemistry of this paper, measured on your own product.")),
  ]})

# ---------------------------------------------------------------- 13 · failure modes
SECTIONS.append({"id": "failure-modes", "kicker": "Where potency goes to die", "title": "Common causes of cannabinoid and terpene loss",
  "blocks": [
    p("Every one of these is chemistry from earlier sections wearing work clothes. The COA tell is how "
      "you catch it after the fact; the fix is how you stop paying for it twice."),
    grid([
      card("Harvested on the calendar",
        p("Trichome heads immature or past peak; profile you bred for never fully built"
          + _c("livingston2020-trichomes") + ".<br><strong>Tell:</strong> potency and terpene totals "
          "below cultivar's known ceiling.<br><strong>Fix:</strong> loupe the trichomes; harvest the "
          "plant, not the schedule."), tag="timing"),
      card("Hot, fast dry",
        p("Monoterpenes stream off warm surfaces. Vapour pressure does the stealing"
          + _c("eyal2023-terpenes") + _c("ross1996-volatileoil") + ".<br><strong>Tell:</strong> aroma "
          "flat; terpene panel light and sesquiterpene-skewed.<br><strong>Fix:</strong> cool, slow, "
          "dark dry; the room that feels too cold is about right."), tag="drying"),
      card("Light on stored product",
        p("The single greatest cannabinoid killer in the storage literature"
          + _c("fairbairn1976-stability") + ".<br><strong>Tell:</strong> THC down without matching CBN "
          "rise.<br><strong>Fix:</strong> opaque packaging, dark storerooms, no window displays."), tag="storage"),
      card("Warm + oxygen + months",
        p("The classic CBN route: air oxidation in storage" + _c("fairbairn1976-stability")
          + _c("ross1997-cbn-age") + ".<br><strong>Tell:</strong> CBN line appears and climbs; harsh "
          "flavour.<br><strong>Fix:</strong> cool store, full containers, minimal headspace, sell on "
          "date order."), tag="storage"),
      card("Rough handling & grinding",
        p("Every tumble ruptures cuticle-walled heads; grinding multiplies surface area for both decays."
          "<br><strong>Tell:</strong> shake assays higher than the buds it fell from; product loses nose "
          "within days.<br><strong>Fix:</strong> gentle trim settings, minimal transfers, grind at point "
          "of use only."), tag="handling"),
      card("Paying for stress myths",
        p("UV rigs and stress protocols sold on decades-old data; the controlled trial found no "
          "cannabinoid gain and dose-dependent damage" + _c("rodriguez2021-uvb") + ".<br><strong>Tell:"
          "</strong> spend rises, COAs don't move.<br><strong>Fix:</strong> demand paired-COA evidence "
          "on your cultivar before buying photons you can't sell."), tag="spend"),
    ], cols=3),
  ]})

# ---------------------------------------------------------------- 14 · quick reference
SECTIONS.append({"id": "quick-reference", "kicker": "Look-up tables", "title": "Quick reference",
  "blocks": [
    table(["Compound", "Acid parent", "Origin", "What it is", "What it is not"], [
      ["Δ9-THC", "THCA", "THCA synthase ← CBGA", "The intoxicating one; the priced number", "A quality verdict on its own"],
      ["CBD", "CBDA", "CBDA synthase ← CBGA", "Major non-intoxicating cannabinoid", "A licence for medical claims"],
      ["CBG", "CBGA", "The pathway hub itself", "Mother acid's neutral form; chemotype IV headline", "&lsquo;The new THC&rsquo;"],
      ["CBN", ", (none)", "Oxidised THC, no enzyme", "An age &amp; storage marker" + _c("ross1997-cbn-age"), "A biosynthesised or proven-sedative product"],
      ["CBC", "CBCA", "CBCA synthase ← CBGA", "The quiet third branch; trace levels", "Something most COAs even itemise"],
      ["THCV", "THCVA", "Propyl (varin) series", "Short-tail THC cousin; lineage-dependent", "An established functional ingredient"],
    ], cls="compact", caption="The six cannabinoids that matter commercially."),
    table(["Terpene", "Class", "Aroma", "VP @ 20 °C (Torr)", "Survives drying?"], [
      ["α-Pinene", "Mono", "Pine, resin", "3.57" + _c("eyal2023-terpenes"), "Worst, first to leave"],
      ["β-Pinene", "Mono", "Pine, herbal", "2.18" + _c("eyal2023-terpenes"), "Poor"],
      ["Myrcene", "Mono", "Earthy, mango", "1.69" + _c("eyal2023-terpenes"), "Poor"],
      ["Limonene", "Mono", "Citrus peel", "1.13" + _c("eyal2023-terpenes"), "Poor"],
      ["Terpinolene", "Mono", "Floral-pine, petrol", "—", "Poor (monoterpene)"],
      ["Ocimene", "Mono", "Sweet, green", "—", "Poor (monoterpene)"],
      ["Linalool", "Mono (alcohol)", "Lavender", "—", "Moderate"],
      ["β-Caryophyllene", "Sesqui", "Pepper, clove", "0.021" + _c("eyal2023-terpenes"), "Good, plus the CB2 story" + _c("gertsch2008-caryophyllene")],
      ["α-Humulene", "Sesqui", "Hops, woody", "0.010" + _c("eyal2023-terpenes"), "Best of the majors"],
    ], cls="compact", caption="The big eight (plus β-pinene). Dashes: no measured value in the cited vapour-pressure study."),
    table(["Number to remember", "Value", "Why"], [
      ["Decarb mass factor", "0.877", "total THC = THC + 0.877 × THCA on every COA"],
      ["THCA half-life at 110 °C", "≈ 6.3 min", "and CBDA/CBGA take roughly double" + _c("wang2016-decarb")],
      ["Monoterpene share, fresh → stored", "≈ 92% → 62%", "three months of drying + storage" + _c("ross1996-volatileoil")],
      ["THC loss, year one at 20–22 °C", "≈ 17%", "dark storage; light makes it worse" + _c("ross1997-cbn-age") + _c("fairbairn1976-stability")],
      ["Caryophyllene CB2 Ki", "155 nM", "the one demonstrated terpene–receptor link" + _c("gertsch2008-caryophyllene")],
      ["Chemotype segregation", "1:2:1", "single locus, codominant alleles" + _c("demeijer2003-chemotype")],
    ], cls="compact", caption="Six numbers that carry most of this paper."),
  ]})

# ---------------------------------------------------------------- 15 · mental model
SECTIONS.append({"id": "mental-model", "kicker": "Take this with you", "title": "Cannabinoid and terpene control principles",
  "blocks": [
    figure(L.flow("From seed to certificate: where chemistry is decided",
        [("Genetics", "chemotype + terpene menu locked at seed"),
         ("Trichomes", "the factory builds and stores the stock"),
         ("Harvest", "peak inventory - pick on the trichome"),
         ("Dry & cure", "monoterpenes flee first - go cool and slow"),
         ("Storage", "the oxidation clock - dark, cool, sealed"),
         ("COA", "the receipt for every choice above")],
        note="Production ends at harvest. Every stage after it is rate control on evaporation and oxidation."), 10,
      "The whole paper in one row. Left of harvest you can build chemistry; right of harvest you can "
      "only protect it."),
    callout("key", "The mental model to keep",
      p("<strong>The plant builds it once; everything afterwards is subtraction.</strong> Genetics write "
        "the menu, trichomes cook and store it as fragile acids and volatile oils, and from harvest "
        "onward you are managing two decay rates, evaporation for flavour, oxidation for potency. "
        "Nothing in a bottle adds chemistry back. Cool, dark, gentle, sealed, fresh: that is the entire "
        "post-harvest playbook, and the COA will tell on you either way.")),
    p("Where to next in this series: <strong>lab testing &amp; COAs</strong> for how these numbers are "
      "actually measured (and mismeasured); <strong>harvest, dry, trim &amp; cure</strong> for the "
      "process that spends or saves the terpenes; and <strong>hash &amp; rosin pressing</strong> for "
      "what happens when you collect the trichome heads and take the chemistry somewhere else."),
  ]})
