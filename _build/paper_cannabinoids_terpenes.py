# -*- coding: utf-8 -*-
"""Paper: cannabinoids & terpenes — where the chemistry is made, how it is built, and how it dies."""
import json, os
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        grid, card, chip, kv, steps)
import figs_lib as L

_FIGS = json.load(open(os.path.join(os.path.dirname(__file__), "figs_cannabinoids_terpenes.json"), encoding="utf-8"))

SLUG = "cannabinoids-terpenes"
TITLE = "Cannabinoids and Terpenes"
EYEBROW = "Reference · Chemistry"
SUB = ("The plant makes cannabinoids and terpenes, two groups of compounds, in the same small "
       "gland, as acids, on one pathway. This paper tells you where the plant makes each group and "
       "how the quantity of each group decreases after harvest. It gives the facts about each "
       "compound and corrects incorrect claims about it. It also tells you the decisions of the "
       "grower that change the numbers. After you read this paper, you will know how to read a COA. "
       "You will know the levers that have an effect and the claims of suppliers that have no data.")
META = [("flask", "Reference"), ("image", "10 diagrams"),
        ("quote", "18 sources"), ("clock", "~24 min to read")]
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
    lead("Two groups of molecules cause the differences in the quality of flower, in the results of "
         "a lab test and in the price of flower. The first group is <strong>cannabinoids</strong> "
         "(the potency). The second group is <strong>terpenes</strong> (the aroma and flavor). The "
         "plant makes the two groups in the same small gland on the surface of the flower. This "
         "gland is the <strong>trichome</strong>. Almost all tasks of a grower increase or decrease "
         "the quantity of compounds in this gland.</p><p>This paper tells you where the plant makes "
         "the compounds and how the plant assembles them. It gives the facts about each compound "
         "and corrects incorrect claims about it. It tells you how the compounds decrease in "
         "quantity after harvest, and it tells you the levers that you have."),
    p("Cannabis contains many more compounds than the labels on products show. Reports show more "
      "than 500 different compounds in cannabis. Of these compounds, 125 are cannabinoids and "
      "approximately 120 are terpenes" + _c("radwan2021-constituents") + ". Approximately six "
      "cannabinoids and eight terpenes are the most important in flower products. When you know "
      "these compounds, you can read each COA, each list of cultivars and each claim about a "
      "product."),
    defterm("Cannabinoid", "A group of compounds that almost no other plant makes (THC, CBD, CBG "
            "and related compounds). The compounds have an effect on the receptor systems of a "
            "person. It is possible that the plant makes them for protection. They give the crop "
            "most of its value."),
    defterm("Terpene", "Small oil molecules that evaporate easily. They give plants their aroma, "
            "for example the aroma of pine, citrus, pepper and hops. Many other plants also make "
            "terpenes. Terpenes are all of the aroma and flavor of flower. They evaporate much more "
            "easily than cannabinoids."),
    defterm("Trichome", "The resin gland on flowers and sugar leaves. The gland has a head on a "
            "stalk. You can see the glands as the &lsquo;frost&rsquo; on the flower. The plant "
            "makes the two groups of compounds in the head, and the compounds stay in the head."),
    defterm("Resin", "The tacky oil in the heads of trichomes. It contains cannabinoid acids, "
            "terpenes and waxes. The potency and the flavor of flower are in the resin. Thus the "
            "value of flower is its resin."),
    defterm("THCA", "Tetrahydrocannabinolic acid. THCA is the acid of THC, and the plant makes THCA "
            "and not THC. THCA does not cause intoxication until heat changes it (decarboxylation)."),
    defterm("Decarboxylation", "The step in which heat removes a carboxyl group (–COOH) from a "
            "cannabinoid acid. The reaction releases CO&#8322; as a gas, and the molecule that "
            "stays is active and neutral. Heat causes the reaction. After the gas is in the air, "
            "the reaction cannot occur in the opposite direction. The short name is "
            "&lsquo;decarb&rsquo;."),
    defterm("Chemotype", "The type of cannabinoid ratio of a plant. The types are THC-dominant, a "
            "balance of THC and CBD, CBD-dominant, CBG-dominant and without cannabinoids. The type "
            "is in the genes of the plant from germination. No task of the grower changes it."),
    defterm("COA", "Certificate of Analysis. The COA is the lab report that gives the cannabinoid "
            "content and the terpene content. It shows the result of each decision in this paper."),
    callout("note", "Limits of this paper",
      p("This paper does not tell you the effect of a compound on a person. It gives each effect "
        "only as a <em>report</em> or as an effect for which <em>investigations are in "
        "progress</em>. Most of the data about effects are of these two types. Also, claims about "
        "medical effects are the task of the regulator and of medical personnel, not of a reference "
        "for growers. This paper gives chemistry for growers: the molecules, the sources of the "
        "molecules, and how to keep the molecules.")),
  ]})

# ---------------------------------------------------------------- 1 · core answer
SECTIONS.append({"id": "core-answer", "kicker": "In short", "title": "Basic facts of the chemistry",
  "blocks": [
    p("The plant makes all the compounds that have a value in <strong>trichome heads</strong>. It "
      "makes them as <strong>acids</strong> (THCA and CBDA, not THC and CBD) on <strong>one "
      "pathway</strong>. In the middle of the pathway is one molecule: <strong>CBGA</strong>, the "
      "&lsquo;mother cannabinoid&rsquo;" + _c("gulck2020-biosynthesis") + ".</p><p>The genes "
      "control the <em>ratio</em> of the products (the chemotype). They also control most of the "
      "terpene profile" + _c("demeijer2003-chemotype") + ". The cultivation controls <em>how "
      "much</em> the plant makes. After harvest, the quantity of the compounds can only decrease."),
    p("The two groups decrease for different causes, and half of this paper is about this "
      "difference. <strong>Terpenes evaporate</strong>. When the temperature of a surface "
      "increases, the molecules go from the surface into the air at a higher rate. The light "
      "&lsquo;monoterpenes&rsquo; evaporate at room temperature. Thus during fast drying with hot "
      "air, the room has a strong aroma, but the quantity of terpenes in the product decreases" +
      _c("eyal2023-terpenes") + ".</p><p><strong>Cannabinoids oxidize</strong>. Oxygen changes the "
      "cannabinoids slowly. No enzyme is necessary, and the change cannot occur in the opposite "
      "direction. The oxidation of THC makes CBN. Of all the causes, light makes the degradation of "
      "THC the fastest" + _c("fairbairn1976-stability") + ".</p><p>Warm air decreases the flavor. "
      "Light, oxygen and a long storage time decrease the potency."),
    callout("key", "The primary point of this paper",
      p("The plant makes the potency and the flavor one time only, in the same gland, as acids that "
        "change easily and oils that evaporate easily. The task of the grower has three parts. "
        "Select genetics that can make the compounds. Keep the plant in good condition. It can then "
        "fill the trichomes. From the time of harvest, keep the product cool, in darkness and "
        "sealed, and touch it carefully.")),
  ]})

# ---------------------------------------------------------------- 2 · where it's made
SECTIONS.append({"id": "where-made", "kicker": "The production site", "title": "Cells of the trichome that make resin",
  "blocks": [
    p("Cannabis has three types of glandular trichome. The <strong>bulbous trichome</strong> is "
      "very small. The <strong>sessile trichome</strong> is flat on the surface. The "
      "<strong>capitate-stalked trichome</strong> has a resin head on a stalk, and it is the type "
      "that gives the most value. A microscope shows that the heads of stalked trichomes have "
      "<strong>12 to 16 secretory disc cells</strong> at the bottom. The heads of sessile trichomes "
      "have eight.</p><p>The stalked trichome is the type that agrees with a high cannabinoid "
      "content" + _c("livingston2020-trichomes") + ". A stalked trichome starts <em>from</em> a "
      "trichome that looks the same as a sessile trichome, and it changes as the maturity of the "
      "flower increases. The &lsquo;frost&rsquo; on the flower increases during flowering. The "
      "cause is not only that the plant makes more trichomes. The trichomes also change from one "
      "type to a different type" + _c("livingston2020-trichomes") + "."),
    figure(_FIGS["trichome_cell"], 1,
      "A cross-section of the capitate-stalked trichome. The disc cells at the bottom of the head "
      "make the resin. The storage cavity above the disc cells keeps the resin, and a cuticle is "
      "the wall of the cavity. Heads of stalked trichomes have 12 to 16 disc cells and a profile "
      "with a high content of cannabinoids and monoterpenes. Heads of sessile trichomes have eight "
      "disc cells" + _c("livingston2020-trichomes") + "."),
    p("The two parts of the trichome have different tasks. The <strong>disc cells make the "
      "resin</strong>. Isolated trichomes show a high expression of the genes for the biosynthesis "
      "of cannabinoids and terpenes" + _c("livingston2020-trichomes") + ". When the resin is "
      "complete, it goes into the <strong>storage cavity</strong>.</p><p>The only wall of the "
      "cavity is a thin layer of wax, the cuticle. The plant does not absorb the resin again. After "
      "the plant makes the resin, it stays in the cavity. The cavity gives protection to the resin, "
      "but it breaks easily, and it is on the surface of the plant."),
    p("The anatomy of the trichome causes three results for the grower:"),
    ul(["<strong>The potency is on the surface.</strong> The quantity of resin increases with the "
        "surface area of the bracts and sugar leaves, not with the mass of the bud. One result is "
        "that flower with a high density of bracts and good light has a higher potency in a lab "
        "test than low-density flower.",
        "<strong>If you are not careful when you touch the flower, you remove resin.</strong> The "
        "wall of the cavity is a film of wax. Movement of the flower in equipment, pressure on the "
        "flower, many touches and trimming that is not careful break the heads. As a result, the "
        "resin stays on gloves and equipment and not in the jar.",
        "<strong>The solventless methods use this anatomy.</strong> Ice-water hash and dry sift are "
        "methods that remove the heads of trichomes from the flower when the heads are cold. Cold "
        "heads break off the stalk and stay in good condition. Thus the methods collect the storage "
        "cavities without the other parts of the plant."]),
    callout("tip", "Information that only a loupe gives",
      p("A loupe tells you the density of the heads, the size of the heads, and the condition of "
        "the heads after you touch them. A loupe gives you this information faster than a lab test. "
        "If the heads in the product from your trimming room look rough at 60×, the potency is in "
        "the equipment and not in the bag.")),
  ]})

# ---------------------------------------------------------------- 3 · biosynthesis
SECTIONS.append({"id": "biosynthesis", "kicker": "The pathway", "title": "Cannabinoid and terpene biosynthesis",
  "blocks": [
    p("Know the pathway, because the chemotypes, CBG flower, THCV and half of the COA are results "
      "of the pathway. The plant starts with <strong>hexanoyl-CoA</strong>, a starter unit that has "
      "six carbons and is from the metabolism of fatty acids. The plant adds three "
      "<strong>malonyl-CoA</strong> units to it and makes <strong>olivetolic acid</strong>, the "
      "aromatic core. A polyketide synthase does this together with olivetolic acid cyclase (OAC)" +
      _c("gulck2020-biosynthesis") + "."),
    p("Then the two parts of the molecule connect. An enzyme in a membrane, a prenyltransferase, "
      "attaches a terpene unit with ten carbons to olivetolic acid. This terpene unit is "
      "<strong>geranyl diphosphate (GPP)</strong>. A test in 1998 first showed the enzyme as "
      "<strong>GOT</strong>, geranylpyrophosphate:olivetolate geranyltransferase.</p><p>The product "
      "is <strong>cannabigerolic acid (CBGA)</strong>. The enzyme accepts olivetolic acid, but it "
      "does not accept olivetol, which is olivetolic acid without the carboxyl group. Thus each "
      "product of the pathway is an acid" + _c("fellermeier1998-cbga") + "."),
    figure(_FIGS["pathway"], 2,
      "The diagram of the pathway. A starter unit from fatty acids and a terpene unit connect to "
      "make CBGA. Three oxidocyclase enzymes (THCA synthase, CBDA synthase and CBCA synthase) each "
      "change CBGA to a different acid" + _c("gulck2020-biosynthesis") + _c("fellermeier1998-cbga") +
      ". The diagram does not show CBN or neutral THC, because no branch makes them."),
    p("CBGA is in the middle of the pathway: it is the <strong>mother cannabinoid</strong>. Three "
      "synthases use CBGA at the same time. <strong>THCA synthase</strong> changes it to THCA, "
      "<strong>CBDA synthase</strong> changes it to CBDA, and <strong>CBCA synthase</strong> "
      "changes it to CBCA" + _c("gulck2020-biosynthesis") + ". The chemotype locus controls the "
      "enzymes that operate correctly in a plant. A subsequent section gives more information about "
      "the locus."),
    p("The pathway has two more facts. First, the <strong>propyl series</strong>. When the pathway "
      "starts from a shorter starter unit, the same enzymes make divarinic acid, then CBGVA, then "
      "<strong>THCVA and CBDVA</strong>. These compounds are the &lsquo;varin&rsquo; cannabinoids, "
      "which have a side chain with three carbons, for example THCV" + _c("gulck2020-biosynthesis") +
      _c("radwan2021-constituents") + ".</p><p>Second, the plant makes almost no CBN and a very "
      "small quantity of neutral THC. The two compounds are degradation products of the compounds "
      "that the enzymes made. The enzymes do not make them" + _c("gulck2020-biosynthesis") +
      "."),
    callout("note", "The enzyme diagram: information for the grower",
      p("The diagram gives the cause of three results. The first result is CBG flower. Flower with "
        "a high content of CBG is from a plant. In this plant, the synthases after CBGA do not "
        "operate correctly, thus the quantity of CBGA increases.</p><p>The second result is the "
        "chemotype. The chemotype is the set of synthase alleles that the plant gets from its "
        "parents. Thus no change in the environment can change THC to CBD. The third result is CBN "
        "on a COA. CBN is a record of the storage, and it is not a genetic trait. Breeding cannot "
        "increase or decrease CBN, because no synthase makes CBN.")),
  ]})

# ---------------------------------------------------------------- 4 · acids & decarb
SECTIONS.append({"id": "acids-decarb", "kicker": "Acids and neutral compounds", "title": "Decarboxylation: THCA and THC",
  "blocks": [
    p("Many persons do not know this fact: <strong>the plant does not make THC</strong> in an "
      "important quantity. It makes THCA, which is the same molecule with a carboxyl group (–COOH). "
      "THCA <strong>does not cause intoxication</strong>. Flower that you did not heat contains "
      "acid that is not active. Heat removes the carboxyl group as CO&#8322; gas and makes the "
      "molecule active. This reaction is <strong>decarboxylation</strong>" + _c("wang2016-decarb") +
      "."),
    figure(_FIGS["decarb"], 3,
      "The change from THCA to THC. Heat removes the –COOH from THCA. THCA releases CO&#8322; as a "
      "gas (12.3% of the mass of the molecule), and Δ9-THC stays. The number 0.877 on each COA is "
      "only the fraction of the mass that stays."),
    p("When a person burns the flower or applies heat to it in a vaporizer, decarboxylation is "
      "complete in less than one second. In all other methods (ovens, extracts and the production "
      "of edibles), the rate of the reaction controls the result, and tests measured the rate "
      "correctly. The data of Wang show that the decarboxylation of cannabis extract between 80 °C "
      "(176 °F) and 145 °C (293 °F) is <strong>first-order</strong>. The rate constants for THCA "
      "are 0.18, 0.66 and 1.83 × 10&#8315;&#179; s&#8315;&#185; at 80 °C (176 °F), 95 °C (203 °F) "
      "and 110 °C (230 °F)" + _c("wang2016-decarb") + ". Thus at 110 °C (230 °F), half of the THCA "
      "that stays changes to THC in each period of approximately six minutes."),
    figure(L.line("Change of THCA to THC at 110 °C (first-order)",
        [("", 100), ("", 71.9), ("", 51.7), ("", 37.2), ("", 26.8), ("", 19.3),
         ("", 13.9), ("", 10.0), ("", 7.2), ("", 5.2), ("", 3.7)],
        ["0", "3", "6", "9", "12", "15", "18", "21", "24", "27", "30"],
        ylab="% THCA remaining",
        note="Calculated from the measured first-order rate constant k = 1.83 × 10⁻³ s⁻¹ at 110 °C. Half-life ≈ 6.3 min. X-axis in minutes.",
        ymax=100), 4,
      "In a first-order reaction, the conversion is fast at the start and slow at the end. The time "
      "for the last small percentage of acid is the same as the time for the first 50%. The curve "
      "uses the rate constant in the data of Wang" + _c("wang2016-decarb") + "."),
    p("The acids do not change at the same rate. THCA changes approximately <strong>two times as "
      "fast</strong> as CBDA or CBGA at the same temperature. The activation energy of THCA is "
      "lower (88 kJ/mol compared with 112 kJ/mol and 109 kJ/mol)" + _c("wang2016-decarb") +
      ". If a person uses the same schedule of heat for CBD material as for THC, the "
      "decarboxylation of the CBD material is not complete."),
    figure(L.bars("Half-life of each acid at 110 °C",
        [("THCA", 6.3), ("CBGA", 11.6), ("CBDA", 13.9)],
        unit=" min",
        note="Half-life = ln 2 ÷ k, from the first-order rate constants measured at 110 °C. THCA is the fastest.",
        maxv=16), 5,
      "The three acids change at different rates in the same oven. The time for CBDA and CBGA is "
      "approximately two times the time for THCA at the same temperature. The times are from the "
      "rate constants in the data of Wang" + _c("wang2016-decarb") + "."),
    p("Decarboxylation has two risks. If the time of heat is too short, acid that is not active "
      "stays. If the temperature is too high or the time is too long, the THC that the reaction "
      "made oxidizes more and changes to CBN. Also, the monoterpenes evaporate very fast at the "
      "temperature of decarboxylation, and they go from the material into the air" +
      _c("eyal2023-terpenes") + ".</p><p>One result of the tests of the rate is important. In a "
      "vacuum, THCA changed to THC and the test found <em>no CBN</em>. When you remove the oxygen "
      "from the reaction, the degradation of the THC almost stops" + _c("wang2016-decarb") +
      "."),
    callout("warn", "Decarboxylation continues at room temperature",
      p("At room temperature, decarboxylation continues at a very low rate. During some months of "
        "storage, the acids in the flower change slowly to neutral compounds. Thus the COA of a jar "
        "in long storage and the COA at harvest can show different values. The difference occurs "
        "before the potency decreases. When the ratio of THCA to THC changes but the total THC "
        "stays the same, the cause is decarboxylation. It is not degradation.")),
  ]})

# ---------------------------------------------------------------- 5 · cannabinoid roster
SECTIONS.append({"id": "cannabinoid-roster", "kicker": "The primary cannabinoids", "title": "Primary cannabinoids",
  "blocks": [
    p("Six cannabinoids are the most important in flower products. For each cannabinoid, the entry "
      "below gives the definition (It is), the source, and the incorrect claims about it (<em>It is "
      "not</em>). This paper gives effects carefully. An effect that is a <em>report</em> comes "
      "from reports of persons who use the compound, or from first tests. It is not a medical "
      "effect that sufficient tests show."),
    grid([
      card("Δ9-THC / THCA",
        p("<strong>It is:</strong> the primary cannabinoid that causes intoxication. In the plant, "
          "it is almost all THCA. The price of THC-dominant flower is for the quantity of THC.<br> "
          "<strong>It is not:</strong> an indicator of quality. Two flowers with 20% total THC can "
          "be very different in aroma, time since harvest and condition of the resin. The potency "
          "is only one item of the COA, and it does not show all the quality of the flower."),
        tag="primary compound"),
      card("CBD / CBDA",
        p("<strong>It is:</strong> a primary cannabinoid that does not cause intoxication. It is "
          "the dominant cannabinoid in plants of chemotype III, and it is the primary cannabinoid "
          "in hemp production. It is one of the cannabinoids with the most medical "
          "investigations.<br> <strong>It is not:</strong> a license for claims. A claim about the "
          "diseases for which CBD has an effect is the task of medical personnel. The information "
          "that a grower gives stops at the measured percentage."),
        tag="second primary compound"),
      card("CBG / CBGA",
        p("<strong>It is:</strong> the neutral compound of the mother acid. Most flower has much "
          "less than 1% CBG, because the plant uses CBGA to make all the other cannabinoids. "
          "Cultivars of chemotype IV have a high quantity of CBGA, because their synthases after "
          "CBGA do not operate correctly" + _c("demeijer2009-chemotype5") + ".<br> <strong>It is "
          "not:</strong> &lsquo;the new THC&rsquo;. It does not cause intoxication. Suppliers give "
          "most claims about it, and the data are not sufficient for them."),
        tag="neutral compound of the mother acid"),
      card("CBN",
        p("<strong>It is:</strong> the oxidation product of THC. Heat, oxygen and time make CBN, "
          "and no enzyme makes it. CBN is a very good sign of degradation, thus persons use the "
          "ratio of CBN to THC to get an estimate of the storage time" + _c("ross1997-cbn-age") +
          ".<br> <strong>It is not:</strong> a product that causes sedation, with an effect that "
          "tests show. The claim that CBN is a &lsquo;sedating cannabinoid&rsquo; is frequent, but "
          "the data for it are weak. On a COA, read CBN first as a sign of the storage time."),
        tag="sign of storage time"),
      card("CBC / CBCA",
        p("<strong>It is:</strong> the third branch from CBGA, through CBCA synthase. Persons found "
          "CBC in the 1960s, and in the data it is one of the primary cannabinoids" +
          _c("radwan2021-constituents") + ". It does not cause intoxication. The quantity is "
          "usually a fraction of one percent.<br> <strong>It is not:</strong> a cannabinoid that "
          "most growers will select for. Labs frequently give no result for CBC."),
        tag="small branch"),
      card("THCV / THCVA",
        p("<strong>It is:</strong> a compound related to THC that has a short &lsquo;propyl&rsquo; "
          "side chain, from the propyl series. Persons first found THCV in 1971. Some cultivars "
          "contain a much higher quantity" + _c("radwan2021-constituents") + ".<br> <strong>It is "
          "not:</strong> a product for appetite or energy with an effect that tests show. "
          "Investigations of the effects in reports are in progress. The supply is small, and at "
          "this time THCV is mostly a task of breeders."),
        tag="related to THC"),
    ], cols=2),
    callout("note", "The other 119",
      p("Most of the other cannabinoids in the lists occur in trace quantities only. They are "
        "related compounds, isomers, or compounds that heat, light or the lab test makes. They are "
        "correct chemistry, but they have almost no effect on the price of flower" +
        _c("radwan2021-constituents") + ". A data sheet for a product can give a cannabinoid that "
        "is not one of the primary cannabinoids. We recommend that you make sure that the COA gives "
        "the quantity of that cannabinoid.")),
  ]})

# ---------------------------------------------------------------- 6 · chemotypes
SECTIONS.append({"id": "chemotypes", "kicker": "Genetics first", "title": "Chemotypes I–V and ratios from the parents",
  "blocks": [
    p("One locus (a position on the DNA) controls the cannabinoid ratio. The locus controls the "
      "ratio from the seed, and you cannot change the ratio after that. When you make a cross of a "
      "THC-dominant plant and a CBD-dominant plant and examine the offspring, the cannabinoid ratio "
      "is a Mendelian trait. There are two alleles, and you can calculate the ratios in the "
      "offspring.</p><p>The investigations of genetics show that one locus, <strong>B</strong>, "
      "controls the ratio. The locus has two codominant alleles: B<sub>T</sub> (a THCA synthase "
      "that operates correctly) and B<sub>D</sub> (a CBDA synthase that operates correctly). A "
      "plant with two copies of B<sub>T</sub> is THC-dominant (chemotype I). A plant with two "
      "copies of B<sub>D</sub> is CBD-dominant (chemotype III). A plant with one copy of each is "
      "chemotype II, which has a mixed ratio of approximately 1:1. In F&#8322; crosses, the "
      "chemotypes occur in the ratio 1:2:1, which agrees with the Mendelian ratio" +
      _c("demeijer2003-chemotype") + "."),
    figure(_FIGS["chemotypes"], 6,
      "The five chemotypes. Types I to III are the result of the B locus, and thus of the synthase "
      "alleles of the plant" + _c("demeijer2003-chemotype") + ". Type IV has a high quantity of "
      "CBGA, because the conversion after CBGA does not operate correctly. Type V has no "
      "cannabinoids. A recessive allele (o/o) stops the pathway. In crosses, this allele also gives "
      "the ratio 1:2:1" + _c("demeijer2009-chemotype5") + "."),
    p("The two other chemotypes complete the diagram. <strong>Type IV</strong> plants have "
      "synthases after CBGA that do not operate. Thus the quantity of the mother acid CBGA "
      "increases. The result is CBG flower.</p><p><strong>Type V</strong> plants make no "
      "cannabinoids. Crosses with usual plants showed that one recessive allele (<em>o</em>) stops "
      "the pathway fully. The ratio is again 1:2:1" + _c("demeijer2009-chemotype5") +
      ". Chemotype V is only a plant for fiber breeding and for investigations. It shows that "
      "genetics controls each type of the ratio."),
    p("An important limit: the locus controls the <strong>ratio</strong>, but it does not control "
      "the <strong>quantity</strong>. Many genes and the environment control the total quantity of "
      "cannabinoid that a plant makes. The environment includes the condition of the canopy, the "
      "light and the maturity at harvest. Thus the breeding and the selection of seed control the "
      "ratio. The cultivation controls the total quantity" + _c("demeijer2003-chemotype") +
      "."),
    callout("tip", "Find the chemotype before you give bench space to a cultivar",
      p("A lab test of a leaf from a plant before the flowering stage gives the chemotype. You can "
        "find that a &lsquo;CBD line&rsquo; is chemotype II before the room is in the flowering "
        "stage. A plant of chemotype II will have a high THC content. If the product is for medical "
        "use, the ratios must have a certificate. Make sure of the chemotype before you give bench "
        "space to a cultivar.")),
  ]})

# ---------------------------------------------------------------- 7 · terpene classes
SECTIONS.append({"id": "terpene-classes", "kicker": "Terpene groups", "title": "Terpene groups and volatility",
  "blocks": [
    p("Each terpene contains isoprene units, and each unit has five carbons. "
      "<strong>Monoterpenes</strong> have two units (C10): myrcene, limonene, pinene, terpinolene "
      "and linalool. <strong>Sesquiterpenes</strong> have three units (C15): caryophyllene and "
      "humulene" + _c("booth2019-terpenes") + ". The two types have a different number of "
      "units.</p><p>Cannabis makes the two types in the same trichomes as the cannabinoids. Reports "
      "show approximately 61 monoterpenes and 51 sesquiterpenes in the species" +
      _c("radwan2021-constituents") + ". A group of terpene synthase genes controls the terpenes "
      "that a cultivar makes in a high quantity" + _c("booth2019-terpenes") + "."),
    p("The primary difference of the groups for the grower is the <strong>volatility</strong>. "
      "Volatility is how easily a compound goes from a material into the air. A molecule goes into "
      "the air when it has sufficient energy to go from the surface of the liquid. Monoterpenes "
      "have a high volatility. Sesquiterpenes have a volatility approximately 100 times lower. "
      "Cannabinoids almost do not evaporate.</p><p>The measured vapor pressures at 20 °C (68 °F) "
      "show this. The vapor pressures of monoterpenes are 1 to 4 Torr (α-pinene 3.57, β-pinene "
      "2.18, myrcene 1.69 and limonene 1.13). The vapor pressures of sesquiterpenes are two orders "
      "of magnitude lower (β-caryophyllene 0.021 and α-humulene 0.010). The vapor pressures of "
      "cannabinoids are very much lower: CBD 6.3 × 10&#8315;&#8310; Torr and THC 5.2 × "
      "10&#8315;&#8311; Torr" + _c("eyal2023-terpenes") + "."),
    figure(_FIGS["volatility"], 7,
      "The values are in a range of seven orders of magnitude on one scale. Monoterpenes evaporate "
      "at room temperature. Sesquiterpenes have a volatility approximately 100× lower. Cannabinoids "
      "almost do not evaporate. The test measured the values at 20 °C (68 °F)" + _c("eyal2023-terpenes") +
      ". Charts that show &lsquo;THC boils at 157 °C (315 °F)&rsquo; are incorrect. The correct "
      "boiling point is more than 400 °C (752 °F). The test calculated this value from the data" +
      _c("eyal2023-terpenes") + "."),
    p("This chart gives information about the drying room. A test measured the volatile oil of the "
      "same buds when they were new and after drying in air and storage. The monoterpene proportion "
      "of the oil decreased from approximately <strong>92% to 62%</strong> in three months, and the "
      "sesquiterpene proportion increased" + _c("ross1996-volatileoil") + _c("radwan2021-constituents") +
      ".</p><p>The part of the aroma from the monoterpenes evaporates first, and the profile "
      "changes to a pepper aroma and a wood aroma. The drying changed the <em>proportions</em> of "
      "the oil, but it did not change the list of compounds in the oil" + _c("ross1996-volatileoil") +
      ". No new compound occurs, and the light fraction decreases. Cold, slow drying in darkness is "
      "a method to control the vapor pressure."),
    callout("key", "A weak aroma with a good THC value shows that the terpenes decreased",
      p("The potency stays when the conditions are not good, but the aroma does not. A sample can "
        "keep its THC value after some days in hot conditions and one month on a shelf, but its "
        "monoterpenes evaporate. When flower has a weak aroma but a good lab result, the cause is "
        "the volatility scale in the chart above.")),
  ]})

# ---------------------------------------------------------------- 8 · terpene roster
SECTIONS.append({"id": "terpene-roster", "kicker": "The eight primary terpenes", "title": "Primary terpenes of flower products",
  "blocks": [
    p("Flower products have a small number of terpene profiles. A test of many thousand retail "
      "samples in the US found three primary groups of products. The first group has high "
      "<strong>caryophyllene and limonene</strong>. The second group has high <strong>myrcene and "
      "pinene</strong>. The third group has high <strong>terpinolene and myrcene</strong>" +
      _c("smith2022-diversity") + ". The test also found that the labels indica, sativa and hybrid "
      "do not agree fully with the chemistry" + _c("smith2022-diversity") + ".</p><p>This section "
      "gives eight terpenes that you must know. The data for aroma are facts. This paper marks the "
      "claims about effects as claims without data."),
    grid([
      card("Myrcene", p("Monoterpene. Aroma of soil, musk and mango. Flower products most "
        "frequently contain myrcene in a high quantity. Myrcene is a primary component of two of "
        "the three groups of products" + _c("smith2022-diversity") + ". The claim that myrcene is a "
        "&lsquo;couch-lock terpene&rsquo; has no data. The data show the aroma and the high "
        "quantity, not sedation."), tag="most frequent terpene"),
      card("Limonene", p("Monoterpene. Aroma of citrus peel. Limonene occurs with caryophyllene in "
        "one primary group of products" + _c("smith2022-diversity") + ". Limonene evaporates "
        "easily: the vapor pressure is 1.13 Torr at 20 °C (68 °F)" + _c("eyal2023-terpenes") +
        ". The quantity of limonene shows the storage time of the product, and limonene also gives "
        "flavor."), tag="citrus"),
      card("α- / β-Pinene", p("Monoterpenes. Aroma of pine and resin. Of the primary terpenes, "
        "pinene evaporates the most easily (α-pinene 3.57 Torr" + _c("eyal2023-terpenes") +
        "), thus pinene is the first terpene to evaporate in drying with warm air. Investigations "
        "of the claims about memory and alertness are in progress. At this time, think of pinene as "
        "an aroma only."), tag="first to evaporate"),
      card("Terpinolene", p("Monoterpene. A mixed aroma: floral aroma, pine aroma and a small "
        "quantity of gasoline aroma. Terpinolene is not frequently the dominant terpene, but when "
        "it is, terpinolene gives the aroma of the cultivar. In one of the three groups of "
        "products, the terpinolene content is high" + _c("smith2022-diversity") +
        "."), tag="different from other terpenes"),
      card("β-Caryophyllene", p("Sesquiterpene with an aroma of pepper and clove. Caryophyllene is "
        "different from all other terpenes. It is an agonist of the CB2 receptor (Ki = 155 nM), and "
        "it does not attach to the CB1 receptor. It is a &lsquo;dietary cannabinoid&rsquo; that is "
        "also in black pepper" + _c("gertsch2008-caryophyllene") + ". The CB2 receptor does not "
        "cause intoxication, thus this effect is pharmacology and not potency. The volatility is "
        "low, and caryophyllene stays in the material during drying" + _c("eyal2023-terpenes") +
        "."),
        tag="special terpene"),
      card("Linalool", p("Monoterpene alcohol. Aroma of lavender. The quantity in cannabis is "
        "almost always small, but the aroma is strong when linalool occurs. The data for the claim "
        "about relaxation are mostly from investigations of lavender oil and not from tests on "
        "cannabis. Investigations of the claim are in progress, and the data are not sufficient."), tag="floral aroma"),
      card("α-Humulene", p("Sesquiterpene. Aroma of hops (humulene is the compound with the typical "
        "aroma of hops), wood aroma and bitterness. It frequently occurs with caryophyllene. Of the "
        "primary terpenes that the test measured, it has the lowest volatility (0.010 Torr" +
        _c("eyal2023-terpenes") + ")."), tag="stays in the material"),
      card("Ocimene", p("Monoterpene. Sweet aroma, green aroma and herb aroma. Ocimene frequently "
        "occurs as a secondary terpene. In some cultivars, the quantity is high. It evaporates "
        "easily in heat, the same as the other monoterpenes."), tag="secondary terpene"),
    ], cols=2),
    callout("note", "Caryophyllene and the receptor data",
      p("Suppliers give receptor claims for all terpenes. Caryophyllene is the only terpene for "
        "which the data show the receptor effect, and other tests found the same result" +
        _c("gertsch2008-caryophyllene") + ". A careful test of the other primary terpenes found no "
        "effect on the CB1 receptor or the CB2 receptor. The concentrations in the test can occur "
        "when a person uses the product" + _c("finlay2020-terpenoids") + ". Thus there is one "
        "correct example and many examples without data. The entourage effect has the same "
        "structure.")),
  ]})

# ---------------------------------------------------------------- 9 · entourage honesty
SECTIONS.append({"id": "entourage", "kicker": "Data and claims", "title": "Entourage effect: data and claims",
  "blocks": [
    p("The claim is that a mixture of the compounds of cannabis has a stronger effect than one "
      "compound only. In this claim, terpenes and the small cannabinoids change the effect of THC. "
      "The most important paper about the claim is the paper of Russo from 2011. This paper gives "
      "the hypothesis of a synergy of cannabinoids and terpenoids for a range of diseases" +
      _c("russo2011-entourage") + ". The paper is about a hypothesis. The paper gives a condition: "
      "a synergy, <em>if tests show it</em>, will make new products possible" +
      _c("russo2011-entourage") + "."),
    p("The table below gives the data. The data show three facts. Caryophyllene is a CB2 agonist" +
      _c("gertsch2008-caryophyllene") + ". Cannabis makes many hundred compounds that occur together" +
      _c("radwan2021-constituents") + ". In pharmacology, there are many examples of effects of "
      "mixtures.</p><p>One test gives the opposite result. It used the five terpenes that occur "
      "most frequently, with THC and without THC, on human CB1 and CB2 receptors. The test showed "
      "<strong>no receptor effect and no change of the signal of THC</strong>" +
      _c("finlay2020-terpenoids") + ".</p><p>Other papers do not agree with the claim. These papers "
      "tell you that the term started as a &lsquo;hypothetical afterthought&rsquo; in 1998. They "
      "tell you that suppliers at this time use the term in claims that show far more than the data "
      "show. They also tell you that persons do not frequently give information about bad effects "
      "of mixtures" + _c("cogan2020-entourage") + "."),
    table(["Condition", "Claim", "Data at this time"], [
      ["<strong>Shown</strong>", "β-caryophyllene is an agonist of the CB2 receptor (Ki 155 nM), and it has no effect on the CB1 receptor",
       "Other tests found the same receptor effect" + _c("gertsch2008-caryophyllene")],
      ["<strong>Shown</strong>", "Cannabis contains many hundred compounds that occur together",
       "Accepted chemistry" + _c("radwan2021-constituents")],
      ["<strong>Not shown</strong>", "The most frequent terpenes have an effect at the CB1 receptor or the CB2 receptor, or they change the effect of THC there",
       "Tests on the receptors found no effect" + _c("finlay2020-terpenoids")],
      ["<strong>Hypothesis</strong>", "The effects of flower with all its compounds are very different from the effects of isolate THC",
       "It is possible, but no test shows it for products" + _c("russo2011-entourage") + _c("cogan2020-entourage")],
      ["<strong>Supplier claim</strong>", "&lsquo;This terpene profile causes this effect&rsquo;",
       "No test with controls shows a connection of a profile to an effect" + _c("cogan2020-entourage")],
    ], cls="compact", caption="The data about the entourage effect, in a correct table."),
    p("The data show only these facts. It is <em>possible</em> that mixtures have an effect. One "
      "mechanism is correct. The claims in the lists of suppliers that give an effect for each "
      "profile have no data. Tests of terpene mechanisms at the CB receptors did not find "
      "them.</p><p>Terpenes continue to have value. They give the flavor of the product, they are a "
      "record of the storage time, and they show the cultivar of the product. This value is "
      "sufficient without pharmacology from other sources."),
    callout("key", "Correct claims about chemistry",
      p("Give the data that you measured. These data are the cannabinoid ratio, the total terpenes, "
        "the five terpenes with the highest weight, and the dates of harvest and test. Use aroma "
        "terms to give the aroma. Do not give information about effects. Only persons with a "
        "license can do this. For medical use, compliance makes this necessary.")),
  ]})

# ---------------------------------------------------------------- 10 · degradation
SECTIONS.append({"id": "degradation", "kicker": "Degradation rates", "title": "Cannabinoid and terpene degradation",
  "blocks": [
    p("From the time of harvest, two changes decrease the quantity of the compounds at the same "
      "time, and they have different causes. <strong>Terpenes evaporate</strong>. They evaporate "
      "the fastest when the temperature is high, and monoterpenes evaporate first (previous "
      "sections).</p><p><strong>Cannabinoids oxidize</strong>. The end product of the oxidation of "
      "THC is CBN. The causes are oxygen, heat, light and time. Each of the two changes occurs in "
      "one direction only. Each decision about storage controls the rate of these two changes."),
    figure(_FIGS["thc_cbn"], 8,
      "The changes occur in one direction only. Decarboxylation changes THCA to THC, which is "
      "active. Oxidation changes THC to CBN. Light is different from the other causes. Light "
      "decreases the THC faster than the other causes, but through mechanisms that do not make CBN" +
      _c("fairbairn1976-stability") + ". The values for storage are from the four-year test at room "
      "temperature" + _c("ross1997-cbn-age") + "."),
    p("Flower in storage at 20 to 22 °C (68 to 72 °F) in darkness had a THC content that was, on "
      "average, <strong>16.6% lower after the first year</strong>. After year two, the THC content "
      "was 26.8% lower. After year three, it was 34.5% lower. After year four, it was 41.4% lower. "
      "The ratio of CBN to THC increased at a rate that you can calculate. Thus persons use the "
      "ratio to get an estimate of the storage time of a sample" + _c("ross1997-cbn-age") +
      "."),
    figure(L.bars("THC remaining: room-temperature storage in darkness",
        [("Harvest", 100), ("Year 1", 83), ("Year 2", 73), ("Year 3", 66), ("Year 4", 59)],
        unit="%",
        note="Plant material at 20–22 °C in darkness. Average values (±6–8%) from the four-year storage test.",
        maxv=110), 9,
      "In <em>good</em> conditions (darkness and room temperature), the potency decreases by "
      "approximately two-fifths in four years. Heat, light and the air in the container each make "
      "the potency decrease faster" + _c("ross1997-cbn-age") + "."),
    p("Tests of storage for two years give the sequence of the causes. Of all causes, <strong>light "
      "decreased the cannabinoids the most</strong>, and the light was not necessarily bright "
      "sunlight. Compared with light, temperature up to 20 °C (68 °F) had no important effect. "
      "Oxidation by air also decreased the cannabinoids by an important quantity" +
      _c("fairbairn1976-stability") + ".</p><p>The same tests give more information about the "
      "mechanisms (Figure 8). When light decreases the THC, the THC does <em>not</em> become CBN. "
      "When oxidation by air in darkness decreases the THC, the THC does become CBN. Thus a sample "
      "with a high CBN content was in warm storage with air, and it was not necessarily in bright "
      "light" + _c("fairbairn1976-stability") + ".</p><p>Material in good storage was "
      "&lsquo;reasonably stable&rsquo; for one to two years in darkness at room temperature" +
      _c("fairbairn1976-stability") + "."),
    p("Terpenes also decrease in storage, and not only by evaporation. They also decrease by "
      "<strong>oxidation</strong>. Oxidation changes the aroma of the terpenes and not their "
      "quantity. Oxidized monoterpenes have a stale aroma: the pine aroma changes to a solvent "
      "aroma. The change in the proportions in dried buds in storage (the monoterpene proportion "
      "from 92% to 62%) is the result of the two decreases together" + _c("ross1996-volatileoil") +
      "."),
    kv([("Light", "Cause number 1 (the largest effect). Use containers that do not transmit light. Keep rooms in darkness. Do not use jars for display" + _c("fairbairn1976-stability") + "."),
        ("Temperature", "Cool storage is always better than warm storage. The temperature controls the rate of each change in this paper."),
        ("Oxygen", "The cause of the change to CBN. Use full, sealed containers with a small volume of air" + _c("fairbairn1976-stability") + "."),
        ("Surface area", "Buds that stay as buds keep the protection of the cuticle. Flower in small pieces has a larger surface area, and the compounds decrease faster."),
        ("Time", "You cannot stop time. Supply the product when it is new, and write a date on each lot" + _c("ross1997-cbn-age") + ".")]),
    callout("warn", "Do not use a clear jar to display flower",
      p("Do not keep flower in a clear jar that has lights above it. A clear jar lets light go in, "
        "and light is the cause with the largest effect. The lights also give heat, and new air "
        "goes into the jar each time you open it. As a result, the flower changes to CBN and the "
        "aroma becomes weak. Keep the stock for display in a different area from your other stock.")),
  ]})

# ---------------------------------------------------------------- 11 · grower levers
SECTIONS.append({"id": "grower-levers", "kicker": "Levers from large to small effect", "title": "Cultivation levers and their limits",
  "blocks": [
    p("The list gives the levers in the sequence of their effect on the numbers. It gives the "
      "condition of the data for each lever. Many claims of suppliers, and many claims of growers "
      "without data, are about these levers."),
    ol(["<strong>Genetics has the largest effect. The effect of each other lever is much "
        "smaller.</strong> The chemotype is a Mendelian trait" + _c("demeijer2003-chemotype") +
        ". The terpene synthase genes of the cultivar control the terpene profile" +
        _c("booth2019-terpenes") + ". The chemistry of flower products is in groups, and each group "
        "agrees with a group of cultivars" + _c("smith2022-diversity") + ". If the plant cannot "
        "make a compound, no setting of the environment will cause the plant to make it.",
        "<strong>Time of harvest.</strong> When the ripeness of the flowers increases, the maturity "
        "of the trichomes increases and the heads change. The profiles also change, and tests can "
        "measure the change" + _c("livingston2020-trichomes") + ". If you harvest on a set date and "
        "not on the condition of the trichomes, you do not get all the compounds. The cultivation "
        "had a cost for these compounds.",
        "<strong>The condition of the plant and the light.</strong> A canopy that is full, in good "
        "condition and has good light has more surface area of trichomes. The correct method to get "
        "&lsquo;more terpenes&rsquo; is more glands. Special inputs do not do this.",
        "<strong>Changes of the environment.</strong> The effect is small, the data do not agree, "
        "and the effect is different for different cultivars. Read the information about UV below "
        "before you accept the cost of equipment for this lever.",
        "<strong>After harvest, the compounds cannot increase, but they can decrease by a large "
        "quantity.</strong> Drying, curing and storage can only keep the compounds (previous "
        "section). They control rates and do not make compounds."]),
    p("The <strong>UV claim</strong> is important, because suppliers of equipment use it. The claim "
      "is that UV stress causes the plant to make more THC as a protection. The claim uses the data "
      "of small tests from many years before. A correct test used current THC-dominant cultivars in "
      "a grow room and a range of UV-B doses. The test showed that <strong>the concentration of "
      "cannabinoids did not increase and the yield did not increase</strong>. It also showed that "
      "<strong>the damage to photosynthesis increased when the dose increased</strong>" +
      _c("rodriguez2021-uvb") + ".</p><p>The test is one careful test on two cultivars. It is not "
      "the last result for each genotype and spectrum. But at this time the supplier of UV "
      "equipment must show test data for the claim."),
    callout("note", "The data for environment claims in short",
      p("Tests with controls give the same result each time. Genetics and the condition of the "
        "plant have the largest effect. &lsquo;Stress hacks&rsquo; in the environment give small "
        "changes in chemistry. The changes are different in each test and different for each "
        "cultivar, and they decrease the yield. We recommend that each input with the claim of +30% "
        "terpenes has a COA pair and the name of a cultivar. If it does not, the claim has no data.")),
  ]})

# ---------------------------------------------------------------- 12 · COA tie-in
SECTIONS.append({"id": "coa", "kicker": "The record", "title": "Cannabinoids and terpenes on a COA",
  "blocks": [
    p("A COA is a table with the results of all the chemistry in this paper. The cannabinoid "
      "section of the COA gives <strong>a result for each acid and a result for each neutral "
      "compound</strong>. New flower in good storage has almost all the THC as THCA and a small "
      "quantity as THC. Use the number for decarboxylation from Figure 3 to get the total:"),
    kv([("total THC", "THC + 0.877 × THCA. The number 0.877 is the fraction of the mass that stays after the molecule releases CO&#8322;."),
        ("total CBD", "CBD + 0.877 × CBDA. The number and the cause are the same."),
        ("Source of the number 0.877", "The molar mass of the neutral compound (314.5) divided by the molar mass of the acid (358.5). The number is only chemistry and not biology."),
        ("Dry weight", "Labs usually correct the results for moisture. Before you compare labs, find if each lab gives the results for dry weight.")]),
    p("When you read more than the primary number on the COA, the COA is a <strong>record of the sample</strong>:"),
    ul(["<strong>High THCA, low THC and almost no CBN:</strong> the material is new, and the "
        "storage was cool. You want this result.",
        "<strong>The neutral fraction increases slowly:</strong> the cause is storage time or heat. "
        "Decarboxylation occurred in storage (Section 5).",
        "<strong>CBN occurs and increases:</strong> CBN is the sign of the storage time. The "
        "storage was warm, had air, or was only for a long time" + _c("ross1997-cbn-age") +
        ".",
        "<strong>The terpene total is low, and the quantity of sesquiterpenes is high for the "
        "cultivar.</strong> The monoterpenes evaporated. The cause is hot drying or a long time on "
        "a shelf" + _c("ross1996-volatileoil") + ".",
        "<strong>Chemotype that does not agree:</strong> a &lsquo;CBD cultivar&rsquo; with a large "
        "THC content has genetics of chemotype II. The B locus causes this result" +
        _c("demeijer2003-chemotype") + "."]),
    p("A terpene panel typically gives a list of compounds in percent by weight. A small number of "
      "compounds make most of the total. The shape of the profile shows the cultivar" +
      _c("smith2022-diversity") + ", and the condition of the profile is the record of your "
      "procedures. The paper about lab testing in this group of papers gives information about "
      "sampling, uncertainty and the differences in the results of different labs."),
    callout("tip", "Use a COA pair",
      p("One COA gives the data of one sample. Two COAs of the same lot give the data about your "
        "storage: one COA at packaging and one COA some months after. The differences are that THCA "
        "changes to THC, CBN occurs, and monoterpenes evaporate. These differences are the "
        "chemistry of degradation in this paper, measured on your product.")),
  ]})

# ---------------------------------------------------------------- 13 · failure modes
SECTIONS.append({"id": "failure-modes", "kicker": "Where the compounds decrease", "title": "Frequent causes of low cannabinoid and terpene content",
  "blocks": [
    p("Each cause in this section is a result of the chemistry in the previous sections. The sign "
      "in the COA shows the cause after the cause occurred. The correction makes sure that the "
      "cause does not occur again."),
    grid([
      card("Harvest on a set date",
        p("The maturity of the trichome heads is too low, or it is after the peak. The profile of "
          "the cultivar does not become full" + _c("livingston2020-trichomes") +
          ".<br> <strong>Sign in the COA:</strong> the totals of potency and terpenes are lower "
          "than the known maximum for the cultivar.<br> <strong>Correction:</strong> examine the "
          "trichomes with a loupe. Harvest on the condition of the plant, not on a set date."), tag="time of harvest"),
      card("Hot, fast drying",
        p("Monoterpenes evaporate from warm surfaces. The vapor pressure causes this" +
          _c("eyal2023-terpenes") + _c("ross1996-volatileoil") + ".<br> <strong>Sign in the "
          "COA:</strong> the aroma is weak, the terpene total in the panel is low, and the "
          "proportion of sesquiterpenes is high.<br> <strong>Correction:</strong> dry the flower "
          "with cool air, slowly, and in darkness. A room that is cold to a person is approximately "
          "correct."), tag="drying"),
      card("Light on product in storage",
        p("In the papers about storage, light is the cause that decreases the cannabinoids the most" +
          _c("fairbairn1976-stability") + ".<br> <strong>Sign in the COA:</strong> the THC content "
          "decreases, but the CBN content does not increase by the same quantity.<br> "
          "<strong>Correction:</strong> use packaging that does not transmit light, keep the "
          "product in rooms in darkness, and do not keep product for display in windows."), tag="storage"),
      card("Heat, oxygen and months",
        p("The usual cause of CBN is oxidation by air in storage" + _c("fairbairn1976-stability") +
          _c("ross1997-cbn-age") + ".<br> <strong>Sign in the COA:</strong> the COA shows CBN, and "
          "the CBN content increases. The flavor is bad.<br> <strong>Correction:</strong> keep the "
          "storage cool. Use full containers with a small volume of air. Supply the stock in the "
          "sequence of the dates."), tag="storage"),
      card("Touch that is not careful, and small pieces of flower",
        p("Each movement of the flower in equipment breaks heads, because the wall of a head is a "
          "cuticle. Flower in small pieces has a larger surface area, thus evaporation and "
          "oxidation are faster.<br> <strong>Sign in the COA:</strong> the loose material that "
          "falls from the buds has a higher potency in a lab test than the buds. The aroma of the "
          "product decreases in some days.<br> <strong>Correction:</strong> use careful settings "
          "for trimming and do not move the product many times. Make the flower into small pieces "
          "only at the time that you use it."), tag="movement"),
      card("Cost of claims about stress",
        p("The claims for UV equipment and stress procedures use only data from many years before. "
          "The test with controls found that the cannabinoids did not increase and that the damage "
          "increased when the dose increased" + _c("rodriguez2021-uvb") + ".<br> <strong>Sign in "
          "the COA:</strong> the cost increases, but the COAs do not change.<br> "
          "<strong>Correction:</strong> make sure that the supplier gives COA pairs for your "
          "cultivar. Do this before you accept the cost of equipment that gives light with no value "
          "in the product."), tag="cost"),
    ], cols=3),
  ]})

# ---------------------------------------------------------------- 14 · quick reference
SECTIONS.append({"id": "quick-reference", "kicker": "Tables for reference", "title": "Reference tables",
  "blocks": [
    table(["Compound", "Parent acid", "Source", "It is", "It is not"], [
      ["Δ9-THC", "THCA", "THCA synthase ← CBGA", "The cannabinoid that causes intoxication. The price is for the quantity of THC.", "An indicator of quality"],
      ["CBD", "CBDA", "CBDA synthase ← CBGA", "A primary cannabinoid that does not cause intoxication", "A license for medical claims"],
      ["CBG", "CBGA", "The middle of the pathway", "The neutral compound of the mother acid. The primary cannabinoid of chemotype IV.", "&lsquo;The new THC&rsquo;"],
      ["CBN", "None", "Oxidized THC. No enzyme makes it.", "A sign of the storage time" + _c("ross1997-cbn-age"), "A product of biosynthesis, or a cause of sedation that tests show"],
      ["CBC", "CBCA", "CBCA synthase ← CBGA", "The small third branch. Trace quantities.", "A compound that most COAs give a result for"],
      ["THCV", "THCVA", "Propyl series (&lsquo;varin&rsquo;)", "A compound related to THC with a short side chain. The quantity is different for different cultivars.", "A compound with an effect that the data show"],
    ], cls="compact", caption="The six cannabinoids that are important in flower products."),
    table(["Terpene", "Group", "Aroma", "Vapor pressure at 20 °C (Torr)", "Stays in the material during drying"], [
      ["α-Pinene", "Monoterpene", "Pine, resin", "3.57" + _c("eyal2023-terpenes"), "Very low. It evaporates first."],
      ["β-Pinene", "Monoterpene", "Pine, herb aroma", "2.18" + _c("eyal2023-terpenes"), "Low"],
      ["Myrcene", "Monoterpene", "Soil, mango", "1.69" + _c("eyal2023-terpenes"), "Low"],
      ["Limonene", "Monoterpene", "Citrus peel", "1.13" + _c("eyal2023-terpenes"), "Low"],
      ["Terpinolene", "Monoterpene", "Floral aroma, pine, gasoline aroma", "—", "Low (monoterpene)"],
      ["Ocimene", "Monoterpene", "Sweet aroma, green aroma", "—", "Low (monoterpene)"],
      ["Linalool", "Monoterpene (alcohol)", "Lavender", "—", "Average"],
      ["β-Caryophyllene", "Sesquiterpene", "Pepper, clove", "0.021" + _c("eyal2023-terpenes"), "High. It also has the CB2 receptor effect" + _c("gertsch2008-caryophyllene")],
      ["α-Humulene", "Sesquiterpene", "Hops, wood aroma", "0.010" + _c("eyal2023-terpenes"), "The highest of the primary terpenes"],
    ], cls="compact", caption="The eight primary terpenes (and β-pinene). A cell without a value shows that the test of vapor pressure that this paper uses has no measured value."),
    table(["Important number", "Value", "Information"], [
      ["Mass number for decarboxylation", "0.877", "Total THC = THC + 0.877 × THCA on each COA"],
      ["THCA half-life at 110 °C", "≈ 6.3 min", "The half-life of CBDA and CBGA is approximately two times longer" + _c("wang2016-decarb")],
      ["Monoterpene proportion, new product → product in storage", "≈ 92% → 62%", "Three months of drying and storage" + _c("ross1996-volatileoil")],
      ["The THC content decreases in year one at 20–22 °C (68–72 °F)", "≈ 17%", "Storage in darkness. Light makes the potency decrease faster" + _c("ross1997-cbn-age") + _c("fairbairn1976-stability")],
      ["Caryophyllene CB2 Ki", "155 nM", "The only connection of a terpene to a receptor that tests show" + _c("gertsch2008-caryophyllene")],
      ["Ratio of chemotypes in the offspring", "1:2:1", "One locus with codominant alleles" + _c("demeijer2003-chemotype")],
    ], cls="compact", caption="Six numbers that contain most of the information in this paper."),
  ]})

# ---------------------------------------------------------------- 15 · mental model
SECTIONS.append({"id": "mental-model", "kicker": "The model", "title": "Control of cannabinoids and terpenes",
  "blocks": [
    figure(L.flow("From seed to certificate: the control of the chemistry",
        [("Genetics", "chemotype and terpene profile: in the seed"),
         ("Trichomes", "trichomes make and keep the compounds"),
         ("Harvest", "peak quantity: harvest by the trichomes"),
         ("Dry, cure", "monoterpenes evaporate first: dry cool, slowly"),
         ("Storage", "oxidation with time: darkness, cool, sealed"),
         ("COA", "the record of each decision above")],
        note="Production stops at harvest. Each stage after it controls the rates of evaporation and oxidation."), 10,
      "All of this paper in one row. Before harvest (on the left), you can make compounds. After "
      "harvest (on the right), you can only keep them."),
    callout("key", "The plant makes the compounds one time, then you slow the degradation",
      p("<strong>The plant makes the compounds one time. After that, the quantity can only "
        "decrease.</strong> The genetics set the profile. The trichomes make the compounds and keep "
        "them as acids that change easily and oils that evaporate easily. From the time of harvest, "
        "you control two rates: evaporation for the flavor and oxidation for the potency.</p><p>No "
        "product can add the compounds again. The complete procedure after harvest has five parts: "
        "cool storage, darkness, sealed containers, careful movement of the product, and a short "
        "storage time. The COA is the correct record of each decision above.")),
    p("Read these papers after this paper: <strong>lab testing and COAs</strong>, <strong>harvest, "
      "dry, trim and cure</strong>, and <strong>hash and rosin pressing</strong>. The paper about "
      "lab testing and COAs tells you how labs measure these numbers, and how labs measure them "
      "incorrectly. The paper about harvest, dry, trim and cure tells you the procedure that "
      "decreases or keeps the terpenes. The paper about hash and rosin pressing tells you the "
      "result when you collect the trichome heads and use the compounds in a different product."),
  ]})
