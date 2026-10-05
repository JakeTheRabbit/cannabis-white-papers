# -*- coding: utf-8 -*-
"""Paper: genetics, seed types and phenotype hunting — where keeper cultivars actually come from."""
import json, os
from components import (p, lead, h, ul, ol, callout, defterm, table, figure, grid, card, chip, kv, steps)
import figs_lib as L

_FIGS = json.load(open(os.path.join(os.path.dirname(__file__), "figs_genetics_phenohunting.json"), encoding="utf-8"))

SLUG = "genetics-phenohunting"
TITLE = "Genetics, seeds and the phenotype hunt"
EYEBROW = "Reference · Genetics"
SUB = ("This paper shows the source of keeper cultivars and how to find and keep one. It gives the "
       "definitions of the terms genotype, phenotype and chemotype. It shows that you cannot be "
       "sure of the plant that a seed will make. It also shows how to do a phenotype hunt.")
META = [("seedling", "Reference"), ("image", "10 diagrams"),
        ("quote", "14 sources"), ("clock", "~24 min to read")]
RELATED = ["seeds-germination", "tissue-culture", "cloning"]
REF_IDS = ["demeijer-2003-chemotype", "laverty-2019-genome-map", "ren-2021-domestication",
           "sawler-2015-genetic-structure", "schwabe-2019-strain-names", "ram-sett-1982-sts",
           "lubell-brand-2018-sts", "flajsman-2021-feminized-seed-production",
           "monthony-2021-feminized-sts-comparison", "punja-holmes-2020-hermaphroditism",
           "toth-2022-autoflower1-locus", "toth-2020-chemotype-markers",
           "hlvd_mgmt2025", "torkamaneh2024"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = [

# ------------------------------------------------------------------ 1 · start here
{"id": "start-here", "kicker": "Start here", "title": "Purpose and scope",
 "blocks": [
    lead("Each cultivar that a grower wants to use started as one plant. A person found the plant, "
         "kept it and made copies of it. This paper gives information about the genetics of a "
         "cultivar.</p><p>It shows which results you can be sure of with genetics, and which "
         "results you cannot be sure of. It shows the cause of the differences between two seeds "
         "from the same package. It gives the definitions of the terms on a seed list. It also "
         "shows how to do a phenotype hunt. A phenotype hunt is a controlled procedure to find, in "
         "a group of plants from seeds, the one plant that you want to keep."),
    p("This paper is for a person who does not know genetics. The procedure at the end is the same "
      "procedure that commercial growers use, but with a different number of plants. It is not "
      "necessary to know genetics before you read this paper. Each term has a definition where it "
      "first occurs."),
    callout("key", "The primary information in five items",
      ul(["Seeds are different <em>because of the genetics</em>. In each generation, the genes of cannabis mix in a new combination, and the lines that growers use at this time are not very stable. Thus the plants from the seeds in one package have the same parents, but they are different.",
          "A strain name is a name that a supplier gives to a product. The name does not make sure that the genetics are the same. Samples with the same name are frequently plants with different genetics.",
          "The phenotype hunt is the method to find a good plant in this variation. Cultivate many seeds in the same conditions. Write the criteria before the start. Give each plant a score for each criterion. Keep the best plant as a clone.",
          "If you use more seeds, you can know more from the result. Ten seeds find the best plant of the ten. To find a keeper that has the minimum score for each criterion, you usually must germinate more than ten seeds.",
          "The keeper clone is the most important item. Mother plants, backup cuttings and a tissue-culture archive keep the clone safe. If you do not have the clone, the phenotype hunt gives no result."], "tight")),
    p("The sequence of the sections agrees with the sequence of the work. The sections show the "
      "three layers of a plant, the source of cultivars and the cause of the differences between "
      "seeds. They show the seed types that you can get and the phenotype hunt. Then they show "
      "selection and sample size. The last sections show how to keep the best plant, how to do "
      "tests of it and how to use it in breeding."),
 ]},

# ------------------------------------------------------------------ 2 · three layers
{"id": "three-layers", "kicker": "Basic information 1", "title": "Genotype, phenotype and chemotype",
 "blocks": [
    p("Three terms are in all sections of this paper. If you know these terms correctly, the other "
      "sections are easy: seed types, phenotype hunts, tests and breeding."),
    defterm("Genotype", "The DNA sequence of the plant. It contains all the genetic information "
            "that the plant has from the start. The parents make the seed, and the genotype does "
            "not change after that. It is the same in each cell, and each clone from the plant gets "
            "an accurate copy of it."),
    defterm("Phenotype", "All the traits of the plant, for example height, branch structure, leaf "
            "shape, vigor, flowering time, aroma and resistance to mold. The phenotype is the "
            "result of the genotype <em>in</em> an environment. The environment includes the light, "
            "the feed, the climate and the stress."),
    defterm("Chemotype", "The chemical part of the phenotype: the dominant cannabinoids (THC type, "
            "CBD type or mixed) and the terpene profile. A lab report measures the chemotype."),
    figure(_FIGS["layers"], 1,
      "The three layers. A genetic test of a leaf sample can read the genotype. You can see the "
      "phenotype. The lab measures the chemotype. The environment changes the middle layer. Thus "
      "the same clone has different traits in two different rooms."),
    p("The layers are related, but they are not the same. The genetics cause most of the THC:CBD "
      "<em>ratio</em>. One locus, with two types of the gene (alleles), is the primary cause. For "
      "example, one parent has only THC-type alleles and the other parent has only CBD-type "
      "alleles. The offspring divide into three chemotypes in the ratio 1:2:1." +
      _c("demeijer-2003-chemotype") + " You can calculate this ratio before you make the "
      "cross.</p><p>But the <em>total</em> quantity of cannabinoids and the terpene values are in "
      "the phenotype layer. Thus they change with the cultivation conditions, the light, the "
      "ripeness and the condition of the plant."),
    table(["Chemotype", "Dominant cannabinoid", "Genetics of the chemotype"], [
      ["Type I", "THC-dominant", "Two alleles of the THC type"],
      ["Type II", "Mixed THC and CBD", "One allele of each type. The seeds of these plants always divide again."],
      ["Type III", "CBD-dominant", "Two alleles of the CBD type"],
    ], cls="compact", caption="The three primary chemotypes and the pairs of alleles that cause "
       "them. The area of the genome with the THCA and CBDA synthase genes has many rearrangements. "
       "Growers and breeders did not fully know the genetics of cannabis for a long time, and this "
       "area is one cause." + _c("laverty-2019-genome-map")),
    callout("note", "One genotype, two environments, two phenotypes",
      p("A clone in two rooms is one genotype and two phenotypes. If a clone is different in the "
        "facility of a different grower, the genetics did not change. The environment changed. When "
        "you know this difference, you prevent many errors about genetics.")),
 ]},

# ------------------------------------------------------------------ 3 · landraces & names
{"id": "landraces-and-names", "kicker": "Basic information 2", "title": "Landraces, polyhybrids and the problems with strain names",
 "blocks": [
    p("The domestication of cannabis occurred in East Asia at approximately the time of the first "
      "part of the Neolithic period. All the cannabis that growers cultivate at this time, hemp "
      "types and drug types, is from the same gene pool of ancestors." + _c("ren-2021-domestication") +
      " Growers moved cannabis to many areas. In areas that were far from each other, the plants "
      "became <strong>landraces</strong>. A landrace is a population with open pollination that "
      "adapts to the local area. The climate and the growers of the area changed each landrace in "
      "many generations."),
    defterm("Landrace", "A population in one area, with open pollination. A landrace is a gene pool "
            "for one area. It is not a cultivar with plants that are all the same. The plants of a "
            "landrace continue to be very different from each other."),
    defterm("Polyhybrid", "A cross of crosses of crosses. Almost all strains that growers use at "
            "this time are polyhybrids. They are from many years of breeding, mostly with no "
            "documentation, with a small group of ancestors. The breeders did not continue the "
            "inbreeding for a time that was sufficient to make the plants stable."),
    p("Almost all drug cannabis at this time is polyhybrid. Tests of all the genome show that the "
      "usual labels agree only in part with the genetics. The label &lsquo;sativa&rsquo; or "
      "&lsquo;indica&rsquo; for commercial strains agrees only to a moderate degree with their "
      "genetic structure." + _c("sawler-2015-genetic-structure") + " The problem is worse for the "
      "buyer. Samples with the <em>same strain name</em> from different sources are frequently "
      "different plants. A test with microsatellite fingerprinting of dispensary samples found "
      "genetic differences in most of the strain names that it examined." +
      _c("schwabe-2019-strain-names")),
    p("The problems with names do not show that genetics are not important. Genetics are very "
      "important. The <em>name</em> is only a label, and it agrees only in part with the genetics. "
      "A name gives you only approximate information on the aroma group and the structure. It does "
      "not give you sure information."),
    callout("warn", "Select a breeder, not a name",
      p("Examine the documentation of the breeder. The documentation must show the names of the "
        "parents and the filial generation. It must also show how the breeder made the feminized "
        "seed, the measured germination rate and the possible variation. A breeder who tells you "
        "that the line continues to change gives accurate information. That information does not "
        "show a problem with the line. A breeder who tells you that all plants from a polyhybrid "
        "cross are the same does not know the result.")),
 ]},

# ------------------------------------------------------------------ 4 · why seeds vary
{"id": "why-seeds-vary", "kicker": "Basic information 3", "title": "Seed variation: heterozygosity and segregation",
 "blocks": [
    p("Cannabis is an outcrossing species. It has male plants and female plants, the wind moves the "
      "pollen between plants, and the genes mix again and again. Thus the plant is very "
      "<strong>heterozygous</strong>. At many positions in the genome, each plant has two different "
      "types of the gene."),
    defterm("Allele", "One type of a gene. Each plant has two alleles of each gene, one from each "
            "parent."),
    defterm("Heterozygous / homozygous", "A plant is heterozygous for a gene when the two alleles "
            "are different. A plant is homozygous for a gene when the two alleles are the same. A "
            "plant that is homozygous for a trait gives the trait to all its offspring. A "
            "heterozygous plant gives the trait to an offspring with a probability of one in two."),
    defterm("Segregation", "For each gene, the allele that each seed gets from each parent is "
            "random. Thus each seed has a new combination of alleles."),
    p("Segregation is the cause of the differences between plants from seeds. Each seed is a new "
      "random combination of alleles from the two parents. If the two parents are true-breeding "
      "(homozygous) for the traits that you want, the first generation has high uniformity. This "
      "generation is the <strong>F1</strong>. All the seeds get the same combination of "
      "alleles.</p><p>When you cross F1 plants with other F1 plants, the second generation (the "
      "<strong>F2</strong>) has very large variation, because the alleles mix again in new "
      "combinations. The standard example is chemotype. A cross of a parent with only CBD-type "
      "alleles and a parent with only THC-type alleles gives an F1 where all the plants are mixed. "
      "The F2 divides in the ratio 1:2:1 into CBD-dominant, mixed and THC-dominant plants." +
      _c("demeijer-2003-chemotype")),
    figure(_FIGS["segregation"], 2,
      "F1: high uniformity. F2: very large variation. The problem for cannabis is that F1 "
      "uniformity is only possible if the parents are true-breeding, and polyhybrids are not "
      "true-breeding. Thus most commercial &lsquo;F1&rsquo; packages give plants that are different "
      "from each other. The result is the same as the bottom row of the figure."),
    p("Maize breeders prevented this problem with inbred parent lines and F1 hybrid seed that has "
      "high uniformity, approximately 100 years before this time. Most cannabis breeding does not "
      "use this method. Because of prohibition, breeding stayed without documentation. Thus seed "
      "suppliers use heterozygous parents, and the variation is in the plants in your "
      "tray.</p><p>Ten seeds from one package are ten siblings: plants that have the same parents. "
      "They are not copies."),
    figure(L.bars("Total THC of eight siblings from one package",
            [("#1", 16.2), ("#2", 18.9), ("#3", 21.4), ("#4", 17.8),
             ("#5", 23.1), ("#6", 15.5), ("#7", 19.7), ("#8", 22.0)],
            unit="%", maxv=26,
            note="Example: variation in type I siblings. Same package, room and feed."), 3,
      "The figure shows the variation that one package of seeds can contain. The difference between "
      "the plants is important, and not the values in the figure. Siblings have the same parents, "
      "but they do not have the same results. A phenotype hunt is possible only because of this "
      "variation. If there is no variation, you cannot select a plant."),
    callout("note", "Variation makes selection possible",
      p("Breeders and growers who do phenotype hunts <em>want</em> segregation. Segregation is the "
        "source of new keepers. The only problem is when you do not prepare for the variation. If "
        "you prepare for a range of results, the range helps you.")),
 ]},

# ------------------------------------------------------------------ 5 · stability vocabulary
{"id": "stability", "kicker": "The terms", "title": "Genetic stability",
 "blocks": [
    p("Suppliers of seeds use the terms F1, IBL and &lsquo;stable&rsquo; without precision. This "
      "section gives the definition of each term. Thus you can examine a seed list correctly."),
    defterm("True-breeding", "A plant is true-breeding for a trait when it is homozygous for the "
            "trait. All its offspring inherit the trait. The correct definition of "
            "&lsquo;stable&rsquo; on a seed list is this definition, for the traits that are on the "
            "list. But frequently a supplier uses &lsquo;stable&rsquo; to tell you &lsquo;we like "
            "it&rsquo;."),
    defterm("Filial generation (F1, F2, F3…)", "The numbers of the generations from the first "
            "cross. F1 is the first cross, and F2 is F1 × F1. F3 and the other generations follow "
            "in the same sequence. The uniformity of the F1 is high only if the parents are "
            "true-breeding."),
    defterm("IBL (inbred line)", "A line with inbreeding and selection for a sufficient number of "
            "generations (usually F5 and the generations after F5). As a result, the line is mostly "
            "true-breeding for its primary traits. IBLs are not frequent and slow to make in "
            "cannabis. Thus IBLs that agree with this definition are very important as breeding "
            "stock."),
    defterm("Backcross (BX)", "A cross of offspring with one of its parents. The cross makes the "
            "traits of that parent stronger. BX1 is the first backcross, and BX2 is the second "
            "backcross. Breeders frequently use this method to make seed with the traits of an "
            "important clone. But the seed is not a copy of the clone."),
    table(["Label", "How the breeder makes it", "Uniformity from plant to plant"], [
      [chip("F1"), "A cross of two parents", "High if the two parents are true-breeding. If not, the uniformity is moderate."],
      [chip("F2"), "F1 × F1", "The lowest uniformity. The genes mix to the maximum. The F2 is the usual generation for a phenotype hunt."],
      [chip("F3 to F5"), "A line with selection in each generation", "The uniformity increases if the selection is correct"],
      [chip("IBL"), "5 or more generations of inbreeding and selection", "High for the selected traits"],
      [chip("S1"), "Self-pollination of one plant", "The variation is smaller. The plants have many of the traits of the mother plant, but they are not copies."],
      [chip("BX1"), "offspring × parent", "The offspring have more of the traits of the recurrent parent. The alleles continue to segregate."],
    ], cls="compact", caption="The definitions of the generation labels. The letter in the label "
       "shows the breeding procedure. It does not give information about the quality."),
    p("Inbreeding has results that you want and results that you do not want. Each generation of "
      "self-pollination or sibling crossing decreases the remaining heterozygosity to approximately "
      "half. Thus the traits become more stable.</p><p>But cannabis is an outcrossing species. Some "
      "recessive alleles cause damage to the plant. If you cross plants that have the same "
      "ancestors again and again, these alleles can occur together in pairs and show their effect. "
      "This decreases the condition and the yield of the plant. This cost has the name "
      "<strong>inbreeding depression</strong>.</p><p>The long-term result that breeders want is the "
      "maize model. In this model, a breeder crosses two inbred parents to make F1 seed. The F1 "
      "seed gives plants that have high uniformity <em>and</em> high vigor. A small number of seed "
      "suppliers use this method at this time. Most seed suppliers do not."),
    callout("tip", "Information to get from the breeder",
      ul(["Get the names of the parents and the number of generations of the line.",
          "Find the method that the breeder used to make the feminized seed. It can be STS (silver thiosulfate) on a mother plant with good test results, or stress.",
          "Get the germination rate that the breeder measures, and the age of the seed lot.",
          "Get information about the variation in flowering time and in structure that is possible."], "tight")),
 ]},

# ------------------------------------------------------------------ 6 · seed types
{"id": "seed-types", "kicker": "Seed supply", "title": "Seed types: regular, feminized, autoflower, S1 and clone-only",
 "blocks": [
    p("Each seed that you can get is one of a small number of types. The method that makes the seed "
      "shows the sex ratio and the variation that is possible. It also shows the tasks for which "
      "you can use the seed."),
    figure(_FIGS["seedtypes"], 4,
      "The diagram of the seed types. The method that makes the seed, that is, which plant "
      "pollinated which plant, causes the sex ratio and the variation. Clone-only cultivars are in "
      "a different part of the figure, because they are not seeds. They are one genotype that "
      "growers copy."),
    p("<strong>Regular seed</strong> is the basic cross. The pollen of a male plant pollinates a "
      "female plant. Approximately half of the seedlings will be male. Flower growers remove the "
      "male plants, because male plants make pollen and not buds.</p><p>Regular seed has the lowest "
      "cost for each seed. In regular seed, the genes mix to the maximum. Regular seed is necessary "
      "for breeding work, because it is the only type that gives male plants."),
    h(3, "How breeders make feminized seed. The seed is not &lsquo;weaker&rsquo;"),
    p("A breeder makes feminized seed when the breeder pollinates a female plant with pollen from a "
      "different <em>female</em> plant. A chemical treatment makes this second female plant make "
      "male flowers. Cannabis plants use the hormone ethylene as a signal that keeps them female. "
      "If a treatment stops this signal, the plant makes male flowers, also when the plant has "
      "female genetics. <strong>Silver thiosulfate (STS)</strong> stops the signal. The silver ions "
      "attach to the ethylene receptors of the plant." + _c("ram-sett-1982-sts") +
      "</p><p>A breeder sprays a solution with a low concentration of STS on a mother plant. The "
      "breeder sprays the solution a small number of times, at approximately the time of the change "
      "to the 12/12 light cycle (12 hours of light and 12 hours of darkness). The mother plant "
      "makes pollen some weeks after the sprays." + _c("lubell-brand-2018-sts") +
      " The pollen is from a plant that has two X chromosomes. Thus each seed that the pollen makes "
      "is XX, that is, female. In tests, correctly made feminized seed is 100% female or almost "
      "100% female." + _c("flajsman-2021-feminized-seed-production") +
      _c("monthony-2021-feminized-sts-comparison")),
    p("Some growers think that feminized seeds are weak and that they have a high risk of "
      "hermaphrodites. These growers think that the problem is in the method, but the problem is in "
      "the parents. STS changes the hormone signal in the mother plant for some weeks. STS does not "
      "cause a mutation in the DNA of the seed.</p><p>A problem with some feminized seed is the "
      "<em>selection of the parents</em>. Some breeders make seed from plants that have "
      "self-pollination because of stress (rodelization). This method selects plants that make male "
      "flowers when there is stress, and the offspring inherit this trait." +
      _c("punja-holmes-2020-hermaphroditism") + "</p><p>Speak to the breeder about the method that "
      "makes the seed. STS on a stable mother plant with good test results is the standard method. "
      "With seed from stress, the result is random."),
    defterm("STS (silver thiosulfate)", "A solution of silver that you spray on a female plant. It "
            "stops the ethylene signal, thus the plant makes pollen. STS is the standard tool for "
            "feminized seed and S1 seed."),
    defterm("Rodelization", "A method in which you let a female plant that you did not pollinate "
            "stay in the room after the time of ripeness. The plant then makes seed with "
            "self-pollination, with the male flowers that stress causes. The method has no cost, "
            "but it makes the line not stable."),
    p("<strong>Autoflower seed</strong> has a day-neutral flowering trait. The trait is from "
      "<em>Cannabis ruderalis</em>. The age of the plant causes the flowering, and the photoperiod "
      "does not. The primary locus for the trait (<em>Autoflower1</em>) is a recessive locus. Thus "
      "the two parents must have the allele. If you cross an autoflower plant with a photoperiod "
      "plant, the offspring are photoperiod plants that only have the allele." +
      _c("toth-2022-autoflower1-locus") + "</p><p>Autoflower plants have a smaller maximum size "
      "than photoperiod plants, and you cannot keep them as mother plants. You cannot keep in the "
      "vegetative stage a plant that makes flowers because of its age. But autoflower plants have a "
      "shorter time to harvest, and the work is easier."),
    p("<strong>S1 seed</strong> is the seed from the self-pollination of a plant. The breeder uses "
      "STS for the sex reversal of a female plant, and uses the pollen of this plant to pollinate "
      "the same plant. The offspring have many of the traits of the mother plant, but they are "
      "<em>not</em> copies. Each locus where the mother plant was heterozygous continues to "
      "segregate. An S1 of a clone that many growers know is a group of related plants, and it is "
      "not the clone."),
    p("A <strong>clone-only</strong> cultivar has no seed line. You keep it only as vegetative "
      "copies, that is, cuttings. A keeper becomes a clone-only cultivar after a phenotype hunt. "
      "Clone-only is the only method to keep the same genotype for a long time. For the procedure, "
      "read the <a href='cloning.html'>cloning paper</a>."),
    table(["Type", "Sex ratio", "Uniformity", "Best use", "Possible problem"], [
      ["Regular seed", "Approximately 50/50", "low", "Breeding, and phenotype hunts with many seeds", "Prepare to remove approximately half of the plants because they are male"],
      ["Feminized seed", "Approximately 99% or more female", "Low to moderate", "Phenotype hunts and production populations", "How the breeder made the seed: with STS or with stress"],
      ["Autoflower seed", "Regular or feminized. The supplier gives the type.", "Low to moderate", "Short time to harvest and small spaces", "You cannot keep mother plants. Stress from a transplant decreases the yield."],
      ["S1", "Approximately 99% or more female", "Moderate", "Tests of the offspring of a clone that many growers know", "Some suppliers tell you that it is &lsquo;the clone in seed form&rsquo;. It is not."],
      ["Clone-only cultivar", "female", "Accurate copy", "To keep a keeper that has good results", "Disease can move with the cuttings. Examine all new material."],
    ], cls="compact", caption="A table to compare the five seed types. In this table, uniformity "
       "shows how much the plants from one package are the same. It does not show the quality."),
 ]},

# ------------------------------------------------------------------ 7 · the hunt
{"id": "the-hunt", "kicker": "The procedure", "title": "Procedure for a phenotype hunt",
 "blocks": [
    p("A <strong>phenotype hunt</strong> is a controlled comparison of plants from seeds. You "
      "cultivate a batch of seeds in conditions that are almost the same for all plants. You give "
      "each plant a score for each criterion. You write the criteria before the start. You keep the "
      "best plant as a clone.</p><p>Confounding is the primary problem. It is a difference in "
      "position, pot, feed or time that gives an average plant a high score. It can also give a "
      "very good plant a low score."),
    defterm("Phenotype hunt", "A controlled procedure to find one plant, in a group of plants from "
            "seeds (phenotypes), that you want to keep as a clone. The result is a clone and not a "
            "harvest."),
    defterm("Keeper", "The plant that you select. You keep it as a mother plant, and after that you "
            "propagate it with cuttings."),
    figure(L.flow("Steps of the hunt",
            [("Germinate", "each seed gets an ID"),
             ("Remove males", "test or pre-flowers"),
             ("Backups", "before 12/12"),
             ("Flower", "the same conditions"),
             ("Score", "table, each week"),
             ("Round 2", "best plants again"),
             ("Keep one", "mother, archive")]), 5,
      "The seven steps give one result: a clone with a good result in round 2. The buds that you "
      "harvest during the hunt are not the result."),
    steps([
      ("Select the number of seeds before you germinate them",
       "Calculate how many seeds your space can hold until harvest <em>in one group</em>. Make sure "
       "that you know the probability of a keeper with this number of seeds (read the next "
       "section). Write the scoring table (the criteria, the scoring weights and the thresholds for "
       "removal) before you know the plants."),
      ("Germinate all the seeds at the same time and tag all the plants",
       "Germinate all the seeds in the batch together (read <a href='seeds-germination.html'>seeds "
       "and germination</a>). When the plant has its first true leaves, give each plant a permanent "
       "ID. The ID is the package code and the seed number. Make sure that the tag stays with the "
       "plant in each transplant. If you cannot read the IDs, you cannot use the data of the hunt."),
      ("Find the sex at the first possible time and remove the male plants (regular seed)",
       "Photoperiod plants show their sex with pre-flowers at approximately weeks 4 to 6 of "
       "vegetative growth. A genetic test of a leaf can find the sex at the seedling stage, some "
       "weeks before the pre-flowers show." + _c("toth-2020-chemotype-markers") +
       " If you do not do breeding, remove the male plants from the room before a pollen sac opens."),
      ("Use the same conditions for all plants in the vegetative stage",
       "Use the same pots, the same medium, the same feed and the same topping procedure for each "
       "plant. Record the vegetative vigor and the time to make roots in the log. But do not select "
       "a plant because of these data. Make the selection after the flowering, when you have all "
       "the data."),
      ("Make backup cuttings of each plant",
       "Make two or three cuttings with roots from each plant. Put a label with the ID of the "
       "parent plant on each cutting. Keep the cuttings in the vegetative stage <em>before</em> the "
       "change to the 12/12 light cycle. Beginners frequently do not do this step, and then they "
       "have a problem. The flowering shows the best plant. If you have no cutting of this plant, "
       "you cannot keep it, because the harvest kills the plant."),
      ("Flowering in the same conditions, with a change of positions",
       "Use one room and the same conditions for all plants. Change all the plants to the 12/12 "
       "light cycle at the same time. Each week, move the plants to different positions. Thus, on "
       "average, the edge effects and the effects of hot areas are the same for all plants. A plant "
       "does not get the best score only because it was in the best light."),
      ("Give scores each week with the scoring table",
       "Record these data: stretch, structure, the start of flowering, problems with pests and "
       "mold, and the change of the aroma. Record each trait as a number. Do not select a plant in "
       "week 3. A strong terpene aroma in the first weeks does not show the plant at the end of the "
       "flowering."),
      ("Harvest each plant, measure the weight and examine the plant",
       "Measure the dry weight of each plant. Keep the harvest of each plant in a different "
       "container during the drying and the cure. If you can, send samples to a laboratory for a "
       "test. If you want to make hash, do a small wash test or press test for each plant. Flower "
       "quality and resin yield are different traits."),
      ("Round 2: cultivate the best plants again",
       "Cultivate the backup cuttings of your best two or three plants together, in the same room. "
       "Do this until the end of the flowering stage. The keeper is the plant that gives the same "
       "good results <em>again</em> as a clone. One good crop is only a test. Two good crops make a "
       "cultivar."),
    ]),
    callout("key", "The one necessary condition",
      p("Make cuttings before the change to the 12/12 light cycle. The product of the hunt is a "
        "clone. If a plant has no backup cutting with roots, the plant is not in the hunt, also "
        "when its aroma is very good.")),
 ]},

# ------------------------------------------------------------------ 8 · selection criteria
{"id": "selection", "kicker": "Selection", "title": "Selection criteria other than potency",
 "blocks": [
    p("Growers frequently use potency first, but it is the worst criterion to use as the only "
      "criterion. For example, a plant has a potency of 26%. The plant has mold each autumn, a "
      "large stretch into the lights and a low rooting rate. This plant is a problem, also if the "
      "lab number is good. Growers give scores for all the tasks that the plant must do:"),
    table(["Criterion", "Item to examine", "Method of measurement"], [
      ["Potency and chemotype", "Total cannabinoids and THC:CBD type", "A lab test for each plant"],
      ["Terpene profile", "Strength and type of the aroma, before the cure and after the cure", "Smell the plants from week 6. Smell the flower in a jar after the cure. If you can, do a lab test of the terpenes."],
      ["Yield", "Dry weight of each plant, with equal spacing", "Measure the weight with a scale after the cure"],
      ["Structure", "Internode spacing, branch angles, self-support and larf ratio", "Examine the plants and record the data during the flowering"],
      ["Flowering time", "Days from the change to the 12/12 light cycle until trichome ripeness", "Record the date when each plant is ripe"],
      ["Mold and pest resistance", "Problems with botrytis, mildew and mites when all plants have the same risk", "A log of the problems for each plant"],
      ["Trichome yield (hash)", "Resin yield and quality of the trichome heads, if you want to make hash", "A small wash test or press test for each plant"],
      ["Rooting of cuttings", "Rooting rate and the number of days to make roots on the backup cuttings", "You have these data from step 5"],
      ["Stretch", "The ratio of the height at the peak to the height at the change to the 12/12 light cycle", "Measure at the change to the 12/12 light cycle and on day 21"],
    ], cls="compact", caption="A group of criteria that you can use. Add the criteria that are "
       "important to your buyers. Remove the criteria that are not important to them."),
    figure(_FIGS["matrix"], 6,
      "The scoring table for six siblings that have tags. Plant #9 has the highest total score, but "
      "it does not have the best score in each column. Plant #3 has the best score in two columns, "
      "but the grower removes it because it is a risk to the facility. The grower wrote the scoring "
      "weights and the thresholds for removal before germination. No other method is necessary."),
    figure(L.bars("Days of 12/12 to ripeness, same six siblings",
            [("#3", 56), ("#7", 63), ("#9", 63), ("#12", 60), ("#15", 70), ("#18", 77)],
            unit=" d", maxv=84,
            note="Example. In polyhybrid packages, the time between the first and last plant is frequently three weeks."), 7,
      "The range of the flowering times is a cost: the plants in the room are ripe in groups, at "
      "different times. Flowering time is also a criterion. Plant A has a flowering time of 56 days "
      "and a score of 2 for all criteria. Plant B has a flowering time of 77 days and a score of 3. "
      "Plant A can give more revenue than plant B, because the room can start the next crop more "
      "quickly."),
    callout("tip", "Write the scoring weights before you see the plants",
      p("In the vegetative stage, select the value of each score. For example, compare a 3 for mold "
        "resistance with a 3 for terpenes. Also select the scores that always remove a plant. If "
        "you write the scoring table after you smell the flower in week 5, the table only agrees "
        "with a selection that you made before. The halo effect makes you see only one very good "
        "trait and not the other traits that are not good.")),
 ]},

# ------------------------------------------------------------------ 9 · sample size
{"id": "sample-size", "kicker": "A check of the numbers", "title": "Limits of the sample size",
 "blocks": [
    p("The calculation in this section is not on the seed package. For this calculation, a keeper "
      "occurs in approximately one seed in twenty from a good cross. A keeper is a plant that has "
      "the minimum score for <em>each</em> criterion. This value of 5% is a high estimate for a "
      "scoring table with high thresholds. The probability of one keeper or more increases with the "
      "number of seeds as the figure shows:"),
    figure(L.line("Probability of a keeper and number of seeds",
            [("5", 22.6), ("10", 40.1), ("20", 64.2), ("30", 78.5),
             ("50", 92.3), ("75", 97.9), ("100", 99.4)],
            ["5", "10", "20", "30", "50", "75", "100"],
            ylab="% probability, ≥1 keeper", ymax=100,
            note="P = 1 − 0.95ⁿ, if 1 seed in 20 is a keeper."), 8,
      "With ten seeds, the probability of one keeper or more is 40%. The probability is less than "
      "50%. With fifty seeds, the probability is more than 90%. For regular seed, use half of the "
      "number of seeds in the calculation. The cause is that growers remove the male plants before "
      "the selection starts."),
    figure(_FIGS["funnel"], 9,
      "The number of plants decreases at each stage of a hunt, before the selection starts. Thus a "
      "grower who tells you &lsquo;I germinated ten seeds and found my keeper&rsquo; usually "
      "selected the best of approximately four female plants that completed the flowering."),
    p("This information does not show a problem with small hunts. It shows that the information "
      "about the result must be accurate. Ten seeds always find <em>the best plant of the ten that "
      "you had</em>. It is possible that this plant is a good plant to keep and cultivate for many "
      "years.</p><p>But the probability is small that this plant is the plant that commercial hunts "
      "want: a plant with a very low frequency in a line. A commercial hunt germinates hundreds to "
      "thousands of seeds and keeps one or two plants. The selection intensity is the difference. "
      "The best plant of 10 seeds and the best plant of 500 seeds are not the same, but growers use "
      "the same terms for them."),
    callout("warn", "Two instructions for accurate selection",
      ul(["Write &lsquo;best of N&rsquo; and know the value of N. The value of N shows how much you can know about the plant after the hunt.",
          "Do not select a keeper after one crop. One crop cannot divide the effect of the genotype from the effects of the position, the season and random effects. Round 2 from the backup cuttings shows the difference between a keeper and a good crop."], "tight")),
 ]},

# ------------------------------------------------------------------ 10 · keeping the cut
{"id": "keeping-the-cut", "kicker": "After the hunt", "title": "Maintenance of a keeper clone",
 "blocks": [
    p("At the end of the hunt, you have the most important item in the facility: one plant. After "
      "this, the task is redundancy. A keeper that is only one mother plant has a risk. Root rot, "
      "an infection with viroid or an error in a label can cause you to have no keeper."),
    kv([("Mother plants for each keeper", "A minimum of two, in different spaces if possible"),
        ("Backup cuttings with roots", "A small number of cuttings with labels, in the vegetative stage, at all times"),
        ("Procedure for the age of mother plants", "At regular intervals, make new mother plants from cuttings of the mother plants. Use cuttings from plants in good condition. Keep the mother plants young and with high vigor."),
        ("Disease condition", "Do a test for hop latent viroid (HpLVd) before the clone becomes a mother plant"),
        ("Labels", "The cultivar, the hunt ID and the date, on each plant and each tray, each time")]),
    figure(L.flow("From best plant to safe clone",
            [("Round 2", "same result again"),
             ("Test", "HpLVd test: negative"),
             ("Two mothers", "different spaces"),
             ("New mothers", "from young cuttings"),
             ("Archive", "tissue culture backup")]), 10,
      "The sequence of steps of redundancy for a keeper. Each step has a small cost. The cost of a missing step can be the cultivar."),
    p("Hop latent viroid (HpLVd) causes the disease &lsquo;dudding&rsquo;. It moves from one plant "
      "to a different plant on cuttings and tools. Stock with an infection can give no sign that "
      "you can see for many months.</p><p>Before a plant becomes a mother plant, do a test of it. A "
      "negative result from one test is only a first result. It does not show that the plant is "
      "clean. One test cannot always find a concentration of viroid that is low or not the same in "
      "all parts of the plant." + _c("hlvd_mgmt2025")),
    p("For long-term protection, a <a href='tissue-culture.html'>tissue-culture archive</a> keeps "
      "the genotype in clean storage, away from the grow room. Make the archive when the plant is "
      "young and has a low number of subcultures. Plants in culture collect small somatic "
      "mutations. The number of mutations is approximately in proportion to the number of "
      "subcultures. Thus the best copy for the archive is a copy that you make one time, from a "
      "young plant, with a minimum number of subcultures." + _c("torkamaneh2024")),
    callout("danger", "One mother plant is not sufficient",
      p("After a loss of a clone, each grower tells you the same. The second mother plant and the "
        "backup tray have almost no cost. You cannot replace the clone. Redundancy is not too much "
        "work. It is a necessary condition if you want a plant to be a keeper.")),
 ]},

# ------------------------------------------------------------------ 11 · testing
{"id": "testing", "kicker": "Lab tests", "title": "Uses and limits of genetic tests",
 "blocks": [
    p("Genetic assays do three tasks at a low cost. Before genetic assays, each of these tasks used "
      "weeks of time in the grow room. All three tests use a small sample of a leaf."),
    table(["Test", "Information that it gives", "Information that it cannot give", "When to use it"], [
      ["Sex marker (PCR)",
       "Male or female, from the seedling stage" + _c("toth-2020-chemotype-markers"),
       "If a female plant will stay stable when there is stress",
       "Hunts with regular seed. You can remove the male plants some weeks before the pre-flowers show."],
      ["Chemotype marker (THCAS/CBDAS)",
       "Type I, II or III. The test shows the cannabinoid ratio that the genes of the plant cause." + _c("toth-2020-chemotype-markers") + _c("demeijer-2003-chemotype"),
       "The THC percentage at the end of the crop, the terpene profile and the yield. These traits are in the phenotype.",
       "Breeding work. Also to divide CBD work and THC work at the start of the work."],
      ["HpLVd test (RT-PCR)",
       "If the test can find the viroid in that tissue on that day" + _c("hlvd_mgmt2025"),
       "That the plant is clean. If the concentration of viroid is low, or not the same in all parts of the plant, one negative result is only a first result.",
       "New cuttings, plants that you want to select as keepers, and mother plants at regular intervals"],
    ], cls="compact", caption="The three tests that give good information for their cost. Obey the "
       "instructions of the lab for the sample. Do the test again for each plant that is important."),
    p("Make sure that you know this limit: a genetic test of a leaf sample reads the "
      "<em>genotype</em> layer. The sex and the chemotype are in this layer. Thus markers find them "
      "correctly. The markers examine an area of the synthase genes that has a fully known "
      "structure, but the area has many rearrangements." + _c("laverty-2019-genome-map") +
      " The potency values, the terpene type, the vigor and the yield are in the phenotype layer, "
      "and the cultivation conditions change this layer. No genetic test can calculate them, also "
      "when a supplier tells you that a test can."),
    callout("note", "A test does not replace cultivation",
      p("Markers decrease the number of plants that you must examine. For example, you apply feed "
        "to a smaller number of male plants, and you can remove CBD plants from a THC hunt at the "
        "start. The hunt occurs in the flowering room, because the phenotype is in the flowering "
        "room.")),
 ]},

# ------------------------------------------------------------------ 12 · breeding basics
{"id": "breeding-basics", "kicker": "The next stage", "title": "Basic breeding for growers",
 "blocks": [
    p("After you have a keeper, you will frequently want to make seed from it. There are two "
      "methods. <strong>Open pollination</strong> is a method with male plants and female plants "
      "together in one space. Landraces have open pollination. The recombination is at the maximum, "
      "and you cannot select the parents of each seed. It is good to make a large batch of seed "
      "with many different plants from a population that you want.</p><p>A <strong>controlled "
      "cross</strong> is a cross in which you use the pollen of one selected male plant on selected "
      "branches of one selected mother plant. It is the only method with which you know the cross "
      "that you made."),
    ol(["<strong>Keep the male plant away from the other plants.</strong> Use a different space "
        "with a different airflow. If the plants use the same HVAC, they get the same pollen. Let "
        "the plant open its first flowers above paper or glass.",
        "<strong>Collect and dry the pollen.</strong> Shake the pollen from the flowers. Let it dry "
        "for one or two days. Then put it through a sieve with small holes to remove the pieces of "
        "flower.",
        "<strong>Keep the pollen cold and dry.</strong> Put the pollen in small airtight vials with "
        "a desiccant. Put a label on each vial, and keep the vials in a freezer. The viability "
        "decreases in some months. Use new pollen if you can. Before you use a batch from storage, "
        "do a test with a small quantity on one branch.",
        "<strong>Pollinate selected branches.</strong> Use a small brush to apply pollen to a small "
        "number of bottom branches of the mother plant. Put a tag on those branches. After that, "
        "spray a small quantity of water on the surfaces near the branches. Water kills pollen that "
        "is in other areas.",
        "<strong>Wait, then harvest the seed.</strong> Seeds become ripe in approximately 4 to 6 "
        "weeks. Ripe seeds are dark and hard, and they have stripes. Dry the seeds with the flower. "
        "Then keep them at a low temperature in a dark and dry area."]),
    p("These steps are necessary because you almost cannot see pollen, and pollen pollinates very "
      "easily. One male plant with open flowers, or one hermaphrodite that stress causes, can "
      "pollinate all the plants in a flowering room. Seed from accidental self-pollination gives "
      "the next generation the hermaphrodite trait of the parent, with no sign." +
      _c("punja-holmes-2020-hermaphroditism") + " If you do the breeding in the same building as "
      "the production of sinsemilla, containment is the first task and breeding is the second task."),
    callout("warn", "Pollen is a risk to the facility",
      p("Use clothing only for the male room. Clean your hands and tools after you touch the male "
        "plants. Do not use the same airflow for the male room and the other rooms. Remove the male "
        "plants before flowers open in areas other than the breeding space. Pollen can cause a crop "
        "with seeds. Be careful when you touch pollen.")),
 ]},

# ------------------------------------------------------------------ 13 · IP
{"id": "ip-and-licensing", "kicker": "The conditions", "title": "Intellectual property and licenses",
 "blocks": [
    p("Ownership of a cultivar is possible, but it is not complete, and it is different in "
      "different jurisdictions. Some general information is correct in all jurisdictions. "
      "Frequently, a strain <em>name</em> is only a marketing name, and it has no rights. As the "
      "section on strain names shows, the names frequently do not give the same genotype each time." +
      _c("schwabe-2019-strain-names") + "</p><p>If there are rights, the rights are for the plant "
      "material or for the registered variety. The types of rights are plant variety rights or "
      "plant breeders' rights, and patents in some jurisdictions. More and more clones have a "
      "license with contract terms. A nursery supplies cuttings of a known cultivar with this "
      "license. The agreement has limits for propagation, resale and breeding."),
    p("These procedures are correct in all jurisdictions. Keep records of the source of each "
      "cultivar and of the terms for each cultivar. Read the terms of the license for cuttings "
      "before you use them in breeding or give them to other persons. Keep the provenance log of "
      "your keeper, the records of the hunt, the dates and the test results. You will want this "
      "documentation if you supply or license the keeper.</p><p>For all other information, the "
      "regulations are local. Before you sell genetic material of all types, examine the "
      "regulations in your area. The information in this paper is general. It is not legal advice."),
 ]},

# ------------------------------------------------------------------ 14 · failure modes
{"id": "failure-modes", "kicker": "When there is a problem", "title": "Frequent errors in a phenotype hunt",
 "blocks": [
    p("Most hunts that do not find a keeper have the same six errors. You can prevent each error if "
      "you obey the procedure each time."),
    grid([
      card("A hunt with mixed conditions",
           p("You cultivate plants in different rooms, seasons or feeds, and then compare them as "
             "if the differences were genetic. Confounding makes the selection incorrect. Use one "
             "group and the same conditions for all plants. If you do not, the scores are not "
             "correct."), tag="confounding"),
      card("No backup cuttings",
           p("You find the best plant at harvest, but you have no clone of it. The hunt gave a very "
             "good jar of flower and no cultivar. Make cuttings of each plant before the change to "
             "the 12/12 light cycle. Do this for each plant."),
           tag="permanent loss"),
      card("Selection in week 3",
           p("One plant has a strong aroma in the first weeks, and the grower does not use the "
             "scoring table after that. The aroma in the first weeks is only one value. The "
             "decision must use the ripeness, the yield, the resistance and the product after the "
             "cure."),
           tag="halo effect"),
      card("A keeper from one crop",
           p("A grower selects a keeper after one crop and uses it in production directly, but the "
             "good result does not occur again. The first crop was the effect of the position and "
             "of random effects. Round 2 from the backup cuttings is the step that makes sure of "
             "the result. It is a necessary step."), tag="no round 2"),
      card("Incorrect labels",
           p("At a transplant, tags can fall from the plants, and trays can change positions. Then "
             "you cannot identify &lsquo;the good one&rsquo; in the group of plants that stay. The "
             "hunt is only possible if the IDs stay on the plants in all work. Use tags that you "
             "can touch. Use more than one tag for each plant. Use tags of a usual type."), tag="procedure"),
      card("Pollen that moves out of its space",
           p("A male plant for breeding, or a hermaphrodite that you did not see, uses the same air "
             "as the hunt. The results are plants with seeds, scores that are incorrect, and "
             "unknown seedlings in the corners of the room in the next year."), tag="containment"),
    ], cols=2),
 ]},

# ------------------------------------------------------------------ 15 · troubleshooting
{"id": "troubleshooting", "kicker": "When there is a problem", "title": "Troubleshooting",
 "blocks": [
    table(["Symptom", "Possible cause", "Correction"], [
      ["The plants from one package are all different",
       "Usual segregation of a polyhybrid. The plants are siblings, and not copies.",
       "There is no problem. Tag the plants, give scores and select. This variation is the hunt."],
      ["Feminized seed made male or intersex flowers",
       "Stress (light leaks, heat or timers that are not regular), or seed that came from stress",
       "First, examine the dark period and the environment. If the room is correct, speak to the supplier about the source of the seed." + _c("punja-holmes-2020-hermaphroditism")],
      ["Autoflower plants made flowers when they were very small, in weeks 3 to 4",
       "The age of the plant is the usual trigger. Slow growth in the first weeks makes the effect stronger (transplant shock, cold or too much water).",
       "Start autoflower plants in their last pot. Be careful with the plants in the first weeks. The size is the result of a vegetative stage without problems." + _c("toth-2022-autoflower1-locus")],
      ["The keeper clone gives a lower result than the plant from seed in the hunt",
       "Random effects in round 1 (position, season), or the condition of the clone. It is not the genetics.",
       "Make round 2 equal for all plants: use cuttings in good condition and equal conditions. If the plant again gives a low result, it was not the keeper."],
      ["The sex test showed female, but the plant made pollen sacs",
       "The marker read the genotype correctly, but stress changed the expression",
       "Do the same as for a plant with intersex flowers: remove the plant or put it in a different space. Correct the cause of the stress. Be careful if you want to use this plant in breeding." + _c("toth-2020-chemotype-markers")],
      ["A phenotype with very good flower, but a low hash yield",
       "Flower quality and resin yield are different traits",
       "If you want to make hash, do a wash test on the plants during the hunt, not after the selection."],
      ["The HpLVd test is negative, but the plant continues to show dudding",
       "A concentration of viroid that is low, or not the same in all parts of the plant, can give a negative result in one test. Or the cause is not the viroid.",
       "Do the test again (use root tissue and collect more than one sample). At the same time, examine the environment and the nutrition." + _c("hlvd_mgmt2025")],
      ["Seeds in a room where you did not pollinate",
       "A hermaphrodite or pollen that moved from a different space, and you did not see it",
       "Examine the plants for intersex flowers. Examine the flow of air from each male space. Correct each problem in the dark period."],
    ], cls="compact", caption="Use this table to find the cause of the symptom. Do this before you "
       "think that genetics are the cause, and before you think that genetics are not the cause."),
 ]},

# ------------------------------------------------------------------ 16 · mental model
{"id": "mental-model", "kicker": "Primary information", "title": "Phenotype hunt: selection, round 2 and maintenance",
 "blocks": [
    callout("key", "Three primary items for the hunt",
      ul(["<strong>Probability.</strong> Each seed is a random result. Heterozygous parents make sure that the result is random. The name on the package does not change the probability. The number of seeds changes your probability of a keeper. How much you want a keeper does not change it.",
          "<strong>The scoring table.</strong> A selection is good only if three conditions are correct. You wrote the criteria before you saw the plants. You used the criteria for plants that you cultivated in the same conditions. You made sure of the result in round 2. If one condition is not correct, you only select the plant that you want.",
          "<strong>Protection.</strong> When a clone becomes a keeper, it is the most important item that you have. These four items keep the keeper: two mother plants, new backup cuttings at regular intervals, tests for disease, and a tissue-culture archive."], "tight")),
    p("These papers give more information. Read <a href='seeds-germination.html'>seeds and "
      "germination</a> to germinate the seeds. Read <a href='cloning.html'>cloning</a> to make the "
      "cuttings and the roots that are necessary for the hunt. Read <a "
      "href='tissue-culture.html'>tissue culture</a> for the archive that makes a keeper "
      "permanent.</p><p>The information on the package does not change the genetics. Germinate a "
      "sufficient number of seeds. Give accurate scores. Make sure that the best plant gives the "
      "same good results again in round 2. Keep the clone safe with the same careful work that you "
      "used to find it."),
 ]},

]
