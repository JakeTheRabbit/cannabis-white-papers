# -*- coding: utf-8 -*-
"""Paper: genetics, seed types and phenotype hunting — where keeper cultivars actually come from."""
import json, os
from components import (p, lead, h, ul, ol, callout, defterm, table, figure, grid, card, chip, kv, steps)
import figs_lib as L

_FIGS = json.load(open(os.path.join(os.path.dirname(__file__), "figs_genetics_phenohunting.json"), encoding="utf-8"))

SLUG = "genetics-phenohunting"
TITLE = "Genetics, seeds and the pheno hunt"
EYEBROW = "Reference · Genetics"
SUB = ("Where keeper cultivars actually come from: what genotype, phenotype and chemotype mean, "
       "why every seed is a gamble by design, how to run a pheno hunt that finds a winner — and "
       "how to keep the cut once you have it.")
META = [("seedling", "Reference"), ("image", "10 diagrams"),
        ("quote", "Evidence-linked · 14 sources"), ("clock", "~24 min read")]
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
{"id": "start-here", "kicker": "Start here", "title": "What this is",
 "blocks": [
    lead("Every cultivar worth growing started life as one individual plant that somebody noticed, "
         "kept and copied. This paper explains the machinery behind that: what genetics can and "
         "cannot promise, why two seeds from the same pack grow into different plants, what the "
         "words on a seed listing actually mean, and how to run a phenotype hunt — a structured "
         "search through seeds for the one plant worth keeping."),
    p("It is written for someone starting from zero, but the process at the end is the same one "
      "commercial operators use, just at different scale. No prior genetics knowledge is assumed; "
      "every term is defined the first time it appears."),
    callout("key", "The core answer in five lines",
      ul(["Seeds vary <em>by design</em>. Cannabis genetics shuffle every generation, and modern lines are barely stabilised, so a pack of seeds is a bag of related-but-different individuals.",
          "A strain name is a brand, not a guarantee. Samples sold under the same name are often genetically different plants.",
          "The pheno hunt is the fix: grow many seeds under identical conditions, score them against criteria you wrote down in advance, and keep the best individual as a clone.",
          "Sample size decides what you can honestly claim. Ten seeds finds the best of ten; a real keeper usually takes more attempts than that.",
          "The keeper cut is the asset. Mothers, backups and a tissue-culture archive protect it; losing it undoes the whole hunt."], "tight")),
    p("The paper runs in grow order: the three layers of what a plant is, where cultivars came "
      "from, why seeds vary, the seed types you can buy, the hunt itself, selection and sample "
      "size, then keeping, testing and breeding from the winner."),
 ]},

# ------------------------------------------------------------------ 2 · three layers
{"id": "three-layers", "kicker": "Core concept 1", "title": "Genotype, phenotype, chemotype — the three layers",
 "blocks": [
    p("Three words carry the whole subject. Get them straight and everything downstream — seed "
      "types, hunts, testing, breeding — becomes simple mechanics."),
    defterm("Genotype", "The plant's DNA sequence — the full set of genetic instructions it was "
            "born with. Fixed at the moment the seed formed, identical in every cell, and copied "
            "exactly into every clone taken from the plant."),
    defterm("Phenotype", "Everything the plant actually is and does: height, branch structure, "
            "leaf shape, vigour, flowering time, smell, resistance to mould. Phenotype is the "
            "genotype <em>expressed through</em> an environment — genes × light, feed, climate and "
            "stress."),
    defterm("Chemotype", "The chemical slice of the phenotype: which cannabinoids dominate "
            "(THC-type, CBD-type or mixed) and the terpene profile. It is what a lab report "
            "measures."),
    figure(_FIGS["layers"], 1,
      "The three layers. A swab can read the genotype, your eyes read the phenotype, and the lab "
      "reads the chemotype. Environment acts on the middle layer — which is why the same clone "
      "grows differently in two different rooms."),
    p("The layers are linked but not interchangeable. The THC:CBD <em>ratio</em> is close to "
      "hard-wired: it is controlled mainly by one genetic locus with two versions (alleles), and "
      "crossing a pure THC plant with a pure CBD plant gives offspring that split into three "
      "chemotypes in a predictable 1:2:1 pattern." + _c("demeijer-2003-chemotype") + " The "
      "<em>absolute</em> potency and terpene numbers, though, move with the grow — light, "
      "ripeness, health — because they sit in the environment-facing phenotype layer."),
    table(["Chemotype", "Dominant cannabinoid", "Genetics underneath"], [
      ["Type I", "THC-dominant", "two THC-type alleles"],
      ["Type II", "Mixed THC + CBD", "one of each — always splits again in seed"],
      ["Type III", "CBD-dominant", "two CBD-type alleles"],
    ], cls="compact", caption="The three major chemotypes and the simple allele pairs behind "
       "them. The region of the genome carrying the THCA/CBDA synthase genes is messy and "
       "rearranged, which is part of why cannabis genetics stayed murky for so long." + _c("laverty-2019-genome-map")),
    callout("note", "Genotype proposes, environment disposes",
      p("A clone in two rooms is one genotype and two phenotypes. When a cut &lsquo;performs "
        "differently&rsquo; at a mate's place, the genetics did not change — the environment did. "
        "Keep this straight and half of all genetics arguments dissolve.")),
 ]},

# ------------------------------------------------------------------ 3 · landraces & names
{"id": "landraces-and-names", "kicker": "Core concept 2", "title": "Landraces, polyhybrids, and why strain names mean little",
 "blocks": [
    p("Cannabis was domesticated in East Asia around the early Neolithic, and everything grown "
      "today — hemp and drug types alike — descends from that ancestral pool." + _c("ren-2021-domestication") +
      " As people carried it around the world, isolated regions developed "
      "<strong>landraces</strong>: locally adapted, open-pollinated populations shaped by their "
      "climate and their farmers over many generations."),
    defterm("Landrace", "A regional, open-pollinated population — think of it as a gene pool with "
            "a postcode, not a uniform variety. Individual landrace plants still vary plenty."),
    defterm("Polyhybrid", "A cross of crosses of crosses. Almost every modern &lsquo;strain&rsquo; "
            "is one: decades of largely undocumented breeding stacked on a narrow set of "
            "ancestors, never inbred long enough to become stable."),
    p("Modern drug cannabis is overwhelmingly polyhybrid. Genome-wide studies show the "
      "familiar labels only loosely track reality: the reported &lsquo;sativa&rsquo; or "
      "&lsquo;indica&rsquo; ancestry of commercial strains corresponds only moderately to their "
      "actual genetic structure." + _c("sawler-2015-genetic-structure") + " Worse for the shopper, "
      "samples sold under the <em>same strain name</em> from different sources are frequently "
      "different plants: microsatellite fingerprinting of dispensary samples found genetic "
      "inconsistency within most strain names tested." + _c("schwabe-2019-strain-names")),
    p("None of this means genetics do not matter — they matter enormously. It means the "
      "<em>name</em> is a weak label for them. A name buys you a rough style guide (probable "
      "aroma family, rough structure) and nothing bankable."),
    callout("warn", "Buy breeders, not names",
      p("Judge seed by the breeder's documentation: named parents, filial generation, how the "
        "seed was feminised, tested germination rate, and whether they describe the variation to "
        "expect. A breeder who tells you their line still varies is being honest, not weak — the "
        "one promising uniformity from a polyhybrid cross is the one guessing.")),
 ]},

# ------------------------------------------------------------------ 4 · why seeds vary
{"id": "why-seeds-vary", "kicker": "Core concept 3", "title": "Why seeds vary: heterozygosity and segregation",
 "blocks": [
    p("Cannabis is naturally an outcrossing species — separate male and female plants, wind "
      "pollination, constant mixing. That history makes it highly "
      "<strong>heterozygous</strong>: at many positions in the genome, each plant carries two "
      "different versions of the gene."),
    defterm("Allele", "One version of a gene. Every plant carries two alleles of each gene — one "
            "from each parent."),
    defterm("Heterozygous / homozygous", "Heterozygous = the two alleles differ. Homozygous = "
            "they match. A plant that is homozygous for a trait passes that trait to every "
            "offspring; a heterozygous one passes a coin-flip."),
    defterm("Segregation", "The reshuffling of alleles into seeds. Each seed draws one allele of "
            "each gene from each parent at random — a fresh hand of cards every time."),
    p("This is why seed-grown plants differ: every seed is a new random draw from both parents' "
      "decks. If both parents are true-breeding (homozygous) for the traits you care about, the "
      "first generation — the <strong>F1</strong> — is uniform, because every seed draws the "
      "same hand. Cross that F1 with itself and the <strong>F2</strong> explodes into variety as "
      "the alleles recombine. The classic demonstration is chemotype: pure-CBD × pure-THC parents "
      "give an all-mixed F1, and the F2 splits 1:2:1 into CBD-dominant, mixed and THC-dominant "
      "plants." + _c("demeijer-2003-chemotype")),
    figure(_FIGS["segregation"], 2,
      "Uniform F1, chaotic F2. The catch for cannabis: F1 uniformity requires true-breeding "
      "parents, which modern polyhybrids are not — so most commercial &lsquo;F1&rsquo; packs "
      "already behave like the bottom row."),
    p("Maize breeders solved this a century ago with inbred parent lines and true F1 hybrid "
      "seed. Cannabis mostly has not: prohibition kept breeding informal, so the industry runs "
      "on heterozygous parents and the variation lands in your tray. A pack of ten seeds is ten "
      "related individuals — siblings, not copies."),
    figure(L.bars("Total THC across eight siblings from one pack",
            [("#1", 16.2), ("#2", 18.9), ("#3", 21.4), ("#4", 17.8),
             ("#5", 23.1), ("#6", 15.5), ("#7", 19.7), ("#8", 22.0)],
            unit="%", maxv=26,
            note="Illustrative type-I sibling spread — same pack, same room, same feed."), 3,
      "The kind of spread one pack can hide. The pattern, not the exact numbers, is the point: "
      "siblings share parents, not outcomes. This spread is also the entire reason pheno hunting "
      "works — no variation, nothing to select."),
    callout("note", "Variation is the raw material, not the flaw",
      p("Breeders and hunters <em>want</em> segregation — it is where new keepers come from. The "
        "problem is only being surprised by it: plan for a spread, and the spread works for you.")),
 ]},

# ------------------------------------------------------------------ 5 · stability vocabulary
{"id": "stability", "kicker": "Vocabulary", "title": "Stability: what breeders actually mean",
 "blocks": [
    p("Seed catalogues throw around F1, IBL and &lsquo;stable&rsquo; loosely. Here is the "
      "vocabulary with its real meaning, so you can read a listing critically."),
    defterm("True-breeding", "Homozygous for the trait in question — all offspring inherit it. "
            "&lsquo;Stable&rsquo; on a listing should mean this, for named traits. It usually "
            "just means &lsquo;we like it&rsquo;."),
    defterm("Filial generation (F1, F2, F3…)", "Counts generations from a founding cross. F1 = "
            "the first cross, F2 = F1 × F1, and so on. Uniformity at F1 depends entirely on the "
            "parents being true-breeding."),
    defterm("IBL (inbred line)", "A line bred to itself with selection for enough generations "
            "(typically F5 and beyond) that it breeds largely true for its signature traits. "
            "Rare and slow to make in cannabis, which is why genuine IBLs are prized as breeding "
            "stock."),
    defterm("Backcross (BX)", "Crossing offspring back to one parent to reinforce that parent's "
            "traits — BX1, BX2 count the rounds. A common way to lock a special cut's character "
            "into seed form, imperfectly."),
    table(["Label", "How it is made", "Plant-to-plant uniformity"], [
      [chip("F1"), "cross of two parents", "high only if both parents are true-breeding; otherwise modest"],
      [chip("F2"), "F1 × F1", "lowest — maximum shuffle, and the classic hunting ground"],
      [chip("F3–F5"), "selected line, generation after generation", "climbing, if selection is honest"],
      [chip("IBL"), "5+ generations of inbreeding + selection", "high for the selected traits"],
      [chip("S1"), "a plant crossed to itself (selfed)", "reduced spread around the mother's look — not copies"],
      [chip("BX1"), "offspring × parent", "biased toward the recurrent parent, still segregating"],
    ], cls="compact", caption="Generation labels decoded. The letter tells you the process; it "
       "promises nothing about quality."),
    p("Inbreeding is a trade. Each generation of selfing or sibling crossing roughly halves the "
      "remaining heterozygosity, which stabilises traits — but cannabis is an outcrosser, and "
      "hammering it inbred can cost vigour (inbreeding depression). The long-term prize is the "
      "maize model: two inbred parents crossed to make true F1 seed that is both uniform "
      "<em>and</em> vigorous. A handful of seed companies are now working exactly that way; most "
      "of the market is not there yet."),
    callout("tip", "Questions that sort real breeders from labels",
      ul(["What are the parents, and how many generations in is this line?",
          "How was the seed feminised — STS reversal of a tested mother, or stress?",
          "What germination rate do you test to, and how fresh is this lot?",
          "What variation should I expect in flowering time and structure?"], "tight")),
 ]},

# ------------------------------------------------------------------ 6 · seed types
{"id": "seed-types", "kicker": "Buying", "title": "Seed types: regular, feminised, autoflower, S1 and clone-only",
 "blocks": [
    p("Every seed on the market is one of a few constructions, and the construction tells you "
      "the sex ratio, the variation to expect, and what the seed is for."),
    figure(_FIGS["seedtypes"], 4,
      "The family tree of seed types. The construction — who pollinated whom — sets sex ratio "
      "and variation. Clone-only cuts sit apart because they are not seeds at all: they are the "
      "one genotype, copied."),
    p("<strong>Regular seed</strong> is the natural cross: male pollen onto a female plant. "
      "Roughly half the seedlings will be male, which flower growers cull — males make pollen, "
      "not bud. Regular seed is the cheapest per seed, carries the full genetic shuffle, and is "
      "what breeding programmes need, because it is the only type that yields males."),
    h(3, "How feminised seed is made — and why it is not &lsquo;weaker&rsquo;"),
    p("Feminised seed comes from pollinating a female with pollen from another <em>female</em> "
      "that has been chemically persuaded to grow male flowers. The tool is <strong>silver "
      "thiosulfate (STS)</strong>: silver ions block the plant's ethylene signalling, and with "
      "ethylene action suppressed, a genetically female plant develops viable male "
      "flowers." + _c("ram-sett-1982-sts") + " In practice a dilute STS solution is sprayed on a "
      "mother a few times around the flip, and she produces pollen a few weeks "
      "later." + _c("lubell-brand-2018-sts") + " Because that pollen comes from a plant with two "
      "X chromosomes, every seed it makes is XX — female. Properly made feminised seed runs at "
      "or near 100% female in published trials." + _c("flajsman-2021-feminized-seed-production") + _c("monthony-2021-feminized-sts-comparison")),
    p("The &lsquo;fem seeds are weak / hermie-prone&rsquo; folklore confuses the method with the "
      "parents. STS changes hormone signalling on the mother for a few weeks; it does not mutate "
      "the DNA that goes into the seed. Where feminised seed earns a bad reputation is "
      "<em>parent choice</em>: seed made by stressing plants until they self-pollinate "
      "(rodelization) actively selects for the tendency to throw male flowers under stress, and "
      "that tendency is heritable." + _c("punja-holmes-2020-hermaphroditism") + " Ask how the "
      "seed was made. STS reversal of a stable, tested mother is the standard; stress-derived "
      "seed is the lottery."),
    defterm("STS (silver thiosulfate)", "A silver solution sprayed on a female plant to block "
            "ethylene signalling so she makes pollen. The standard tool for feminised seed and "
            "S1s."),
    defterm("Rodelization", "Letting an unpollinated female sit past ripeness until she "
            "self-pollinates from stress-induced male flowers. Free, and it breeds the "
            "instability in."),
    p("<strong>Autoflower seed</strong> carries a day-neutral flowering trait inherited from "
      "<em>Cannabis ruderalis</em>: the plant flowers on age, not photoperiod. The major locus "
      "behind it (<em>Autoflower1</em>) behaves as a simple recessive, which is why both parents "
      "must carry it and why crossing an auto to a photoperiod plant gives photoperiod offspring "
      "that merely carry the allele." + _c("toth-2022-autoflower1-locus") + " Autos trade "
      "ultimate size and the ability to hold a mother plant (you cannot keep a plant in veg that "
      "flowers on age) for speed and simplicity."),
    p("<strong>S1 seed</strong> is a plant selfed: a female reversed with STS and used to "
      "pollinate herself. The offspring cluster around the mother's character but they are "
      "<em>not</em> copies — every locus where she was heterozygous still segregates. An S1 of a "
      "famous cut is a neighbourhood around the cut, not the cut."),
    p("<strong>Clone-only</strong> means the cultivar exists only as a vegetatively copied cut — "
      "there is no seed line. That is what a keeper becomes after a hunt, and it is the only way "
      "to hold one exact genotype over time. See the <a href='cloning.html'>cloning paper</a> "
      "for the mechanics."),
    table(["Type", "Sex ratio", "Uniformity", "Best for", "Watch for"], [
      ["Regular", "~50/50", "low", "breeding, big hunts", "budget half the pack to the male cull"],
      ["Feminised", "~99%+ female", "low–modest", "hunts and production pops", "how it was made — STS vs stress"],
      ["Autoflower", "as sold (reg or fem)", "low–modest", "speed, small spaces", "no mothers possible; transplant stress costs yield"],
      ["S1", "~99%+ female", "modest", "exploring around a famous cut", "sold as &lsquo;the cut in seed form&rsquo; — it is not"],
      ["Clone-only cut", "female", "exact copy", "holding a proven keeper", "disease travels with cuttings — screen incoming material"],
    ], cls="compact", caption="The five constructions side by side. Uniformity here means "
       "plant-to-plant similarity within a pack, not quality."),
 ]},

# ------------------------------------------------------------------ 7 · the hunt
{"id": "the-hunt", "kicker": "The process", "title": "The pheno hunt, step by step",
 "blocks": [
    p("A <strong>pheno hunt</strong> is a controlled comparison: grow a batch of seeds under "
      "conditions as identical as you can manage, score every plant against criteria fixed in "
      "advance, and keep the best individual as a clone. The enemy is confounding — any "
      "difference in position, pot, feed or timing that lets a mediocre plant look special, or "
      "hides a great one."),
    defterm("Pheno hunt", "A structured search through seed-grown plants (phenotypes) for one "
            "individual worth keeping as a clone. The output is a cut, not a harvest."),
    defterm("Keeper", "The selected individual — kept as a mother plant and propagated by "
            "cutting from then on."),
    figure(L.flow("The hunt at a glance",
            [("Pop + tag", "every seed gets an ID"),
             ("Sex + cull", "swab or preflowers"),
             ("Backup cuts", "before the flip"),
             ("Flower", "identical conditions"),
             ("Score", "rubric, weekly"),
             ("Round 2", "rerun the finalists"),
             ("Keep one", "mother + archive")]), 5,
      "Seven moves, one output: a verified cut. Everything else — the bud you harvest along the "
      "way — is a by-product."),
    steps([
      ("Size the hunt before you germinate",
       "Decide how many seeds your space can carry to harvest <em>as one cohort</em>, and be "
       "honest about the odds that number buys (next section). Write the scoring rubric now, "
       "before you have favourites."),
      ("Pop everything at once, tag everything",
       "Germinate the whole batch together (see <a href='seeds-germination.html'>seeds and "
       "germination</a>). At first true leaves, give every plant a permanent ID — pack code plus "
       "seed number — and make the tag follow the plant through every transplant. An unreadable "
       "hunt is a wasted hunt."),
      ("Sex early and cull males (regular seed)",
       "Photoperiod plants show sex at preflowers around week 4–6 of veg; a leaf-swab genetic "
       "test can call sex weeks earlier at the seedling stage." + _c("toth-2020-chemotype-markers") +
       " Unless you are breeding, males leave the room before any pollen sac opens."),
      ("Veg to a fair comparison",
       "Same pots, same medium, same feed, same topping policy for every plant. Note veg vigour "
       "and rooting speed in the log, but resist selecting on them — the call happens after "
       "flower, on the full picture."),
      ("Take backup cuts of every candidate",
       "Two or three cuttings per plant, labelled with the parent's ID, rooted and parked in "
       "veg <em>before</em> the flip. This is the step beginners skip and regret: flower reveals "
       "the winner, and without a cut the winner is already dead when you meet it."),
      ("Flower identical, rotate positions",
       "One room, one recipe, all plants flipped together. Rotate positions weekly so edge "
       "effects and hot spots average out instead of crowning whoever stood under the best "
       "light."),
      ("Score weekly against the rubric",
       "Stretch, structure, onset of flowering, pest and mould events, aroma as it develops. "
       "Write numbers, not vibes. Do not crown anyone at week 3 — loud early terps are not a "
       "finished plant."),
      ("Harvest, weigh and assess per plant",
       "Dry weight per plant, kept separate through dry and cure. Send samples for testing if "
       "you can; if hash is the goal, run a small wash or press trial per candidate — flower "
       "quality and resin yield are different traits."),
      ("Verify the finalists in round 2",
       "Flower the backup cuts of your top two or three side by side. The keeper is the one "
       "that <em>repeats</em> its performance as a clone. One good run is an audition; two is a "
       "cultivar."),
    ]),
    callout("key", "The one non-negotiable",
      p("Cuts before the flip. The hunt's product is a clone — if a plant has no rooted backup, "
        "it is not really in the hunt, whatever it smells like.")),
 ]},

# ------------------------------------------------------------------ 8 · selection criteria
{"id": "selection", "kicker": "Selection", "title": "Selection criteria beyond potency",
 "blocks": [
    p("Potency is the loudest criterion and the worst one to select on alone. A 26% plant that "
      "moulds every autumn, stretches into the lights and roots badly is a liability with a good "
      "lab number. Operators score across the whole job the plant has to do:"),
    table(["Criterion", "What to look at", "How to measure"], [
      ["Potency / chemotype", "total cannabinoids, THC:CBD type", "lab test per candidate"],
      ["Terpene profile", "intensity and character, raw and cured", "nose at weeks 6+, cured jar test; lab terps if available"],
      ["Yield", "dry weight per plant at equal spacing", "scale, after cure"],
      ["Structure", "internode spacing, branch angles, self-support, larf ratio", "eyes and notes through flower"],
      ["Flowering time", "days from flip to ripe trichomes", "log the date each candidate finishes"],
      ["Mould / pest resilience", "botrytis, mildew and mite events under equal pressure", "incident log per plant"],
      ["Trichome yield (hash)", "resin return and head quality if hash is the goal", "small wash or press trial per candidate"],
      ["Clone-ability", "strike rate and days to root from the backup cuts", "you already have this data from step 5"],
      ["Stretch", "height multiple from flip to peak", "measure at flip and day 21"],
    ], cls="compact", caption="A working criteria set. Add what your market pays for; delete "
       "what it does not."),
    figure(_FIGS["matrix"], 6,
      "The matrix in action across six tagged siblings. #9 wins without owning the single best "
      "score in every column; #3 owns two of them and gets culled on a facility risk. Weights "
      "and cull-thresholds were fixed before germination — that is the entire trick."),
    figure(L.bars("Days of 12/12 to ripeness, same six siblings",
            [("#3", 56), ("#7", 63), ("#9", 63), ("#12", 60), ("#15", 70), ("#18", 77)],
            unit=" d", maxv=84,
            note="Illustrative spread. Three weeks between fastest and slowest is common in polyhybrid packs."), 7,
      "Flowering-time spread is a scheduling tax: a mixed room finishes in waves. It is also a "
      "criterion — a 56-day plant that scores 2 everywhere can out-earn a 77-day plant that "
      "scores 3, because it turns the room over faster."),
    callout("tip", "Write the weights before you meet the plants",
      p("Decide in veg what a 3 on mould resilience is worth against a 3 on terps, and which "
        "scores are automatic culls. Rubrics written after smelling week-5 flower are "
        "rationalisations — the halo effect of one spectacular trait will launder every other "
        "weakness.")),
 ]},

# ------------------------------------------------------------------ 9 · sample size
{"id": "sample-size", "kicker": "Reality check", "title": "Sample-size honesty: 10 seeds vs 100",
 "blocks": [
    p("Here is the arithmetic nobody puts on the seed pack. Suppose a genuine keeper — a plant "
      "that clears your bar on <em>every</em> criterion — shows up in about one seed in twenty "
      "from a decent cross. That 5% is generous for a strict rubric, and it compounds like "
      "this:"),
    figure(L.line("Chance of at least one keeper vs seeds popped",
            [("5", 22.6), ("10", 40.1), ("20", 64.2), ("30", 78.5),
             ("50", 92.3), ("75", 97.9), ("100", 99.4)],
            ["5", "10", "20", "30", "50", "75", "100"],
            ylab="% chance of ≥1 keeper", ymax=100,
            note="P = 1 − 0.95ⁿ, assuming 1 seed in 20 clears your full bar."), 8,
      "Ten seeds is a 40% shot at even one true keeper — worse than a coin flip. Fifty gets you "
      "past 90%. Halve the effective numbers again for regular seed, because the males exit "
      "before selection starts."),
    figure(_FIGS["funnel"], 9,
      "Where the seeds actually go. Attrition eats the pack before selection ever gets a vote — "
      "which is why &lsquo;I popped ten and found my keeper&rsquo; usually means &lsquo;I kept "
      "the best of about four finished females&rsquo;."),
    p("This is not an argument against small hunts — it is an argument for honest language. Ten "
      "seeds reliably finds <em>the best plant you had</em>, and that plant may well be worth "
      "keeping and growing for years. It is just unlikely to be the once-in-a-line individual "
      "that commercial hunts chase by popping hundreds to thousands of seeds and keeping one or "
      "two. Selection intensity is the whole difference: best-of-10 and best-of-500 are "
      "different animals wearing the same word."),
    callout("warn", "Two honesty rules",
      ul(["Say &lsquo;best of N&rsquo;, and know your N. It calibrates every claim you make about the plant afterwards.",
          "Never crown after one run. A single grow confounds genotype with position, season and luck — round 2 from the backup cuts is what separates a keeper from a good week."], "tight")),
 ]},

# ------------------------------------------------------------------ 10 · keeping the cut
{"id": "keeping-the-cut", "kicker": "Aftercare", "title": "Keeping the cut: mothers, backups, archive",
 "blocks": [
    p("The hunt ends with the most valuable object in the facility: one plant. From here the job "
      "is redundancy. A keeper held as a single mother is one root-rot event, one viroid "
      "infection or one labelling mistake away from not existing."),
    kv([("Mothers per keeper", "two minimum, in separate spaces if at all possible"),
        ("Rooted backups", "a handful of labelled cuts in veg at all times"),
        ("Mother age policy", "re-cut mothers from their own healthy cuttings on a schedule; keep them young and vigorous"),
        ("Disease status", "HpLVd-screened before the cut earns mother status"),
        ("Labels", "cultivar + hunt ID + date on every plant, every tray, every time")]),
    figure(L.flow("From winner to insured asset",
            [("Verify", "round-2 rerun clean"),
             ("Screen", "HpLVd test negative"),
             ("Two mothers", "separate spaces"),
             ("Rolling refresh", "re-cut mothers young"),
             ("Archive", "tissue culture backup")]), 10,
      "Redundancy ladder for a keeper. Each rung costs little; missing rungs cost the cultivar."),
    p("Screen before you commit. Hop latent viroid (HpLVd) — the &lsquo;dudding&rsquo; pathogen — "
      "spreads silently through cuttings and tools, and infected stock can look normal for "
      "months; test the candidate before it becomes a mother, and treat one negative as "
      "provisional rather than proof, because low, uneven viroid levels can slip past a single "
      "test." + _c("hlvd_mgmt2025")),
    p("For long-term insurance, a <a href='tissue-culture.html'>tissue-culture archive</a> holds "
      "the genotype in clean storage off the grow floor. Archive early and at low passage: "
      "plants held in culture accumulate small somatic mutations roughly in proportion to how "
      "many times they are subcultured, so the best archival copy is made once, young, and "
      "disturbed as little as possible." + _c("torkamaneh2024")),
    callout("danger", "One mother is zero mothers",
      p("Every grower who has lost a cut says the same thing afterwards: the second mother and "
        "the backup tray cost almost nothing, and the cut was irreplaceable. Redundancy is not "
        "paranoia — it is the price of admission for calling something a keeper.")),
 ]},

# ------------------------------------------------------------------ 11 · testing
{"id": "testing", "kicker": "Lab options", "title": "Genetic testing: what a swab can and cannot tell you",
 "blocks": [
    p("Cheap genetic assays now cover three jobs that used to cost weeks of grow time. All three "
      "run off a small leaf sample."),
    table(["Test", "What it tells you", "What it cannot tell you", "When to use it"], [
      ["Sex marker (PCR)",
       "male vs female, from the seedling stage" + _c("toth-2020-chemotype-markers"),
       "whether a female will stay stable under stress",
       "regular-seed hunts — cull males weeks before preflowers"],
      ["Chemotype marker (THCAS/CBDAS)",
       "type I / II / III — which cannabinoid ratio the plant is wired for" + _c("toth-2020-chemotype-markers") + _c("demeijer-2003-chemotype"),
       "final THC %, terpene profile, yield — those are phenotype",
       "breeding projects; sorting CBD work from THC work early"],
      ["HpLVd screen (RT-PCR)",
       "whether the viroid is detectable in that tissue on that day" + _c("hlvd_mgmt2025"),
       "that the plant is clean — low, uneven levels mean one negative is provisional",
       "incoming cuts, candidate keepers, mothers on a schedule"],
    ], cls="compact", caption="The three swabs that earn their cost. Sample per the lab's "
       "instructions and retest anything that matters."),
    p("The boundary to hold in your head: a swab reads the <em>genotype</em> layer. Sex and "
      "chemotype class live there, so markers call them well — the synthase-gene region they "
      "probe is well mapped, if messy." + _c("laverty-2019-genome-map") + " Potency numbers, "
      "terpene character, vigour and yield live in the phenotype layer, shaped by the grow. No "
      "swab predicts them, whatever the marketing says."),
    callout("note", "Testing does not replace growing",
      p("Markers prune the search space — fewer males fed, CBD plants out of a THC hunt early. "
        "The hunt itself still happens in the flower room, because that is where phenotype "
        "exists.")),
 ]},

# ------------------------------------------------------------------ 12 · breeding basics
{"id": "breeding-basics", "kicker": "Going further", "title": "Breeding basics for growers",
 "blocks": [
    p("Once you hold a keeper, the next itch is making seed from it. Two modes exist. "
      "<strong>Open pollination</strong> — males and females loose in one space — is how "
      "landraces work: maximum recombination, zero control, fine for making a big diverse seed "
      "batch from a population you like. A <strong>controlled cross</strong> is one chosen "
      "father onto chosen branches of one chosen mother, and it is the only way to know what "
      "you made."),
    ol(["<strong>Isolate the male.</strong> A separate space with separate airflow — shared HVAC "
        "is shared pollen. Let it open its first flowers over paper or glass.",
        "<strong>Collect and dry the pollen.</strong> Tap it free, let it dry for a day or two, "
        "then pass it through a fine sieve to remove flower debris.",
        "<strong>Store it cold and dry.</strong> Small airtight vials with a desiccant, "
        "labelled, in the freezer. Viability fades over months — use fresh where you can, and "
        "test a pinch on one branch before trusting a stored batch.",
        "<strong>Pollinate selectively.</strong> Paint pollen onto a few lower branches of the "
        "mother with a small brush, tag those branches, and mist nearby surfaces afterwards — "
        "water kills stray pollen.",
        "<strong>Wait, then harvest seed.</strong> Seeds mature in roughly 4–6 weeks; ripe ones "
        "are dark, hard and striped. Dry them with the flower, then store cool, dark and dry."]),
    p("The reason for all the ceremony: pollen is nearly invisible and absurdly effective. One "
      "open male — or one stress-induced hermaphrodite — can seed a whole flower room, and "
      "seed set by accidental self-pollination quietly carries the parent's instability "
      "forward." + _c("punja-holmes-2020-hermaphroditism") + " Breeding in the same building as "
      "sinsemilla production is a containment exercise first and a romance second."),
    callout("warn", "Pollen is a facility hazard",
      p("Dedicated clothes for the male room, hands and tools washed after contact, no shared "
        "airflow, and males culled before flowers open anywhere outside the breeding space. If "
        "you would not handle powder that costs you a seeded crop, do not handle pollen "
        "casually.")),
 ]},

# ------------------------------------------------------------------ 13 · IP
{"id": "ip-and-licensing", "kicker": "The fine print", "title": "IP and licensing, lightly",
 "blocks": [
    p("Cultivar ownership is real but patchy, and it varies by jurisdiction. A few generic "
      "truths hold. Strain <em>names</em> are mostly unprotected marketing, and as covered "
      "earlier, often do not even track a consistent genotype." + _c("schwabe-2019-strain-names") +
      " Actual protection, where it exists, attaches to the plant material or the registered "
      "variety: plant variety rights / plant breeders' rights schemes, patents in some "
      "countries, and increasingly, contract terms attached to licensed clone releases — "
      "nurseries supplying verified cuts under agreements that limit propagation, resale or "
      "breeding."),
    p("Practical hygiene for an operator, anywhere: keep records of where every cultivar came "
      "from and under what terms; read the terms on licensed cuts before breeding from or "
      "distributing them; and treat your own keeper's provenance log — hunt records, dates, "
      "test results — as the documentation you would want if you ever release or license it. "
      "For anything beyond that, the rules are local: check them where you are before selling "
      "genetics in any form. This is orientation, not legal advice."),
 ]},

# ------------------------------------------------------------------ 14 · failure modes
{"id": "failure-modes", "kicker": "When it goes wrong", "title": "Classic ways a hunt fails",
 "blocks": [
    p("Most failed hunts fail the same six ways, and every one is preventable for the cost of "
      "discipline."),
    grid([
      card("The mixed-conditions hunt",
           p("Candidates grown in different rooms, seasons or feeds, then compared as if the "
             "differences were genetic. Confounding beats selection every time — one cohort, "
             "one recipe, or the scores mean nothing."), tag="confounding"),
      card("No backup cuts",
           p("The winner is identified at harvest — and was never cloned. The hunt produced a "
             "great jar and no cultivar. Cuts before the flip, every candidate, no exceptions."),
           tag="irreversible"),
      card("Week-3 crowning",
           p("One plant smells loud early and the rubric dies on the spot. Early aroma is one "
             "data point; finish, yield, resilience and the cured product are the decision."),
           tag="halo effect"),
      card("The one-run keeper",
           p("Crowned after a single grow, scaled straight to production, and the magic does not "
             "repeat — the first run was position and luck. Round 2 from backups is the "
             "verification step, not a formality."), tag="no verification"),
      card("Label drift",
           p("Tags lost at transplant, trays swapped, &lsquo;the good one&rsquo; now "
             "unidentifiable among survivors. The whole hunt rests on IDs surviving every "
             "touch — make tags physical, redundant and boring."), tag="process"),
      card("Pollen escape",
           p("A breeding male, or an unnoticed hermaphrodite, shares air with the hunt. Seeded "
             "candidates, corrupted scores, and next year's mystery seedlings in the room "
             "corners."), tag="containment"),
    ], cols=2),
 ]},

# ------------------------------------------------------------------ 15 · troubleshooting
{"id": "troubleshooting", "kicker": "When it goes wrong", "title": "Troubleshooting",
 "blocks": [
    table(["Symptom", "Most likely cause", "What to do"], [
      ["Plants from one pack all look different",
       "Normal polyhybrid segregation — siblings, not copies",
       "Nothing is wrong. Tag, score, select — that spread is the hunt"],
      ["Feminised seed threw male or intersex flowers",
       "Stress (light leaks, heat, irregular timers) — or stress-derived seed",
       "Audit the dark period and environment first; if the room is clean, question the seed source" + _c("punja-holmes-2020-hermaphroditism")],
      ["Autos flowered tiny at week 3–4",
       "Normal age trigger, magnified by early stunting (transplant shock, cold, overwatering)",
       "Start autos in their final pot and keep early weeks gentle; size comes from an easy veg" + _c("toth-2022-autoflower1-locus")],
      ["Keeper clone underperforms its seed-plant run",
       "Round-1 luck (position, season) — or clone health, not genetics",
       "Judge round 2 fairly: healthy cuts, equal conditions. If it repeats poorly, it was never the keeper"],
      ["Sex swab said female, plant made pollen sacs",
       "Marker read the genotype correctly — stress flipped the expression",
       "Treat as an intersex event: remove or isolate, fix the stressor, do not breed from it casually" + _c("toth-2020-chemotype-markers")],
      ["Great flower pheno, poor hash returns",
       "Flower quality and resin yield are separate traits",
       "If hash is the goal, wash-test candidates during the hunt, not after crowning"],
      ["HpLVd test negative but the plant duds on",
       "Low or uneven viroid levels can evade one test — or the cause is elsewhere",
       "Retest (root tissue, repeat sampling) and review environment and nutrition in parallel" + _c("hlvd_mgmt2025")],
      ["Seeds found in an unpollinated room",
       "A hermaphrodite event or pollen escape you did not see",
       "Inspect for intersex flowers, audit airflow paths from any male space, tighten the dark period"],
    ], cls="compact", caption="Match the symptom to the mechanism before blaming genetics — "
       "and before trusting them."),
 ]},

# ------------------------------------------------------------------ 16 · mental model
{"id": "mental-model", "kicker": "Take-away", "title": "The mental model: lottery, rubric, vault",
 "blocks": [
    callout("key", "Carry these three objects",
      ul(["<strong>The lottery.</strong> Seeds are tickets. Heterozygous parents guarantee the draw is random, names on the packet do not change the odds, and the number of tickets — not enthusiasm — sets your chance of a real keeper.",
          "<strong>The rubric.</strong> Selection only means anything against criteria written before you met the plants, applied to plants grown under the same conditions, and verified in a second round. Everything else is picking a favourite.",
          "<strong>The vault.</strong> The moment a cut earns the name keeper it becomes the most valuable thing you own: two mothers, rolling backups, disease screening and a tissue-culture archive are what &lsquo;keeping&rsquo; actually means."], "tight")),
    p("From here, the practical neighbours: <a href='seeds-germination.html'>seeds and "
      "germination</a> for getting the tickets sprouted, <a href='cloning.html'>cloning</a> for "
      "taking and rooting the cuts the hunt depends on, and "
      "<a href='tissue-culture.html'>tissue culture</a> for the archive that makes a keeper "
      "permanent. The genetics do not care what the packet said — pop enough seeds, score them "
      "honestly, verify the winner, and protect it like it matters. It does."),
 ]},

]
