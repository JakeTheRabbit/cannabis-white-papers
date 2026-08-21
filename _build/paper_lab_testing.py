# -*- coding: utf-8 -*-
"""Paper: lab testing, potency and COAs — how to read a certificate of analysis and not be fooled by it."""
import json, os
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        grid, card, chip, kv, steps)
import figs_lib as L

_FIGS = json.load(open(os.path.join(os.path.dirname(__file__), "figs_lab_testing.json"), encoding="utf-8"))

SLUG = "lab-testing-coas"
TITLE = "Lab testing, potency and the COA"
EYEBROW = "Harvest · Quality"
SUB = ("A certificate of analysis is a measurement of one small sample, not a property of your crop. "
       "This guide reads a COA line by line, checks the potency maths (the 0.877 factor and the chemistry "
       "behind it), explains every test family from qPCR to ICP-MS, and is honest about the part the "
       "industry keeps getting caught at: inflated numbers.")
META = [("flask", "Quality"), ("image", "10 diagrams"),
        ("quote", "Evidence-linked · 16 sources"), ("clock", "~24 min read")]
RELATED = ["gmp-hash-lab", "harvest-dry-trim-cure"]
REF_IDS = ["schwabe2023-inflated", "zoorob2021-bunching", "jikomes2018-labs", "wang2016-decarb",
           "dussy2005-thca", "lazarjani2020-methods", "sarma2020-usp", "nist-cannaqap2",
           "mckernan2016-tym", "jameson2022-stateregs", "raber2015-dabs", "geweda2024-audit",
           "giordano2025-accuracy", "hs2024-oregon", "tga-tgo93", "nz-mcs-mqs"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

# ---------------------------------------------------------------- 1. start here
SECTIONS.append({"id": "start-here", "kicker": "Start here", "title": "The Piece of Paper That Prices Your Crop",
  "blocks": [
    lead("Every batch you sell (and in a medicinal system, every batch you release) ends its life as a "
         "one-page document from a testing laboratory: the <strong>certificate of analysis</strong>, or "
         "<strong>COA</strong>. It says what is in the flower (cannabinoids, terpenes) and what must not be "
         "(mould, heavy metals, pesticides, mycotoxins). Buyers mostly read one number on it, "
         "<strong>total THC</strong>, and that number moves the price. Which is exactly why it is the most "
         "gamed number in the industry, with peer-reviewed studies documenting systematic inflation on retail "
         "labels" + _c("schwabe2023-inflated") + _c("zoorob2021-bunching") + "."),
    p("Here is the single idea that makes every section of this paper make sense: <strong>a COA is not a "
      "property of your crop.</strong> It is a measurement, of one small sample, pulled one way, prepared one "
      "way, run on one instrument, by one lab, on one day. Change any of those and the number changes, with no "
      "fraud involved. Most of the grief in cannabis testing (&lsquo;same weed, different number&rsquo;, lab "
      "shopping, inflated labels) comes from people forgetting, or exploiting, that distinction."),
    defterm("COA (certificate of analysis)", "The lab's formal report of what it measured in a specific "
            "sample: identity, potency, contaminants, methods, and a release signature."),
    defterm("Analyte", "Any single thing the lab measures, THCA, lead, a pesticide, a mould count. A COA is "
            "a list of analytes with results."),
    defterm("Matrix", "What the sample physically is, dried flower, oil, an edible. The matrix changes how "
            "the lab must extract and measure, and how hard the job is."),
    defterm("Batch / lot", "The defined quantity of product one COA claims to speak for. The whole game is "
            "how honestly a few grams of sample represent it."),
    defterm("LOD / LOQ", "Limit of detection / limit of quantitation, the smallest amount the method can "
            "reliably see / reliably put a number on. &lsquo;ND&rsquo; (not detected) only means &lsquo;below "
            "the LOD&rsquo;, never zero."),
    defterm("ISO/IEC 17025", "The international standard for testing-lab competence. Accreditation to it is "
            "the baseline credential worth checking on any COA."),
    callout("key", "The one big idea",
      p("The certificate is a <em>photograph of one gram</em>, taken through one lab's lens. It can be a "
        "sharp, honest photograph, that is what good sampling and a good lab buy you, but it is never the "
        "landscape. Everything in this paper is about knowing how much landscape your photograph actually "
        "shows.")),
  ]})

# ---------------------------------------------------------------- 2. core answer
SECTIONS.append({"id": "core-answer", "kicker": "The short version", "title": "Core Answer",
  "blocks": [
    p("To read a COA in sixty seconds, check eight things in order:"),
    ol(["<strong>Who tested it</strong>, a named lab with a checkable accreditation (ISO/IEC 17025 or, in "
        "medicinal frameworks, GMP certification)" + _c("nz-mcs-mqs") + ".",
        "<strong>What was tested</strong>, sample ID, batch, matrix, sample mass, and crucially <em>who "
        "pulled the sample</em>. &lsquo;Client-submitted&rsquo; means the lab never saw your batch.",
        "<strong>The basis</strong>, dry-weight or as-received, and the moisture content. This alone moves "
        "potency ~10–15%.",
        "<strong>The potency table</strong>, acids (THCA) and neutrals (THC) on separate rows means an HPLC "
        "method. Then do the maths: total THC = Δ9-THC + 0.877 × THCA. It should reconcile exactly.",
        "<strong>Units</strong>, % w/w and mg/g say the same thing (1% = 10 mg/g); don't let a unit switch "
        "fool you.",
        "<strong>Each contaminant family</strong> (microbial, metals, pesticides, mycotoxins, solvents) is "
        "its own test with its own method and pass/fail. Potency says nothing about safety.",
        "<strong>The footnotes</strong>, LOQs, ND definitions, method references. No LOQ column means "
        "&lsquo;ND&rsquo; is uninterpretable.",
        "<strong>The release</strong>, a named, dated QA signature. In GMP systems this is where a COA "
        "becomes a release decision instead of a marketing asset" + _c("tga-tgo93") + "."]),
    p("And the honesty part, up front: the peer-reviewed record shows reported retail potency in several "
      "legal markets is systematically inflated, 70% of tested Colorado flower samples ran more than 15% "
      "below label in one study" + _c("schwabe2023-inflated") + ", 70% of a three-state audit fell outside "
      "±20% of label" + _c("geweda2024-audit") + ", and product frequencies &lsquo;bunch&rsquo; suspiciously "
      "just above the 20%-THC price threshold" + _c("zoorob2021-bunching") + ". When a single number sets the "
      "price, someone will lean on it. The defence is knowing how the number is made. Which is the rest of "
      "this paper."),
  ]})

# ---------------------------------------------------------------- 3. pipeline
SECTIONS.append({"id": "pipeline", "kicker": "The map", "title": "How a Test Actually Happens",
  "blocks": [
    p("Between &lsquo;cut a sample&rsquo; and &lsquo;PDF lands in your inbox&rsquo; sits a pipeline, and "
      "every stage of it shapes the final numbers. The instrument is the glamorous part; the sampling and the "
      "prep are where the number is really decided."),
    figure(L.flow("From batch to certificate",
        [("Sample", "increments across the whole batch"),
         ("Accession", "logged; chain of custody starts"),
         ("Prep", "grind, extract, dilute, per test"),
         ("Instruments", "HPLC, ICP-MS, qPCR, GC"),
         ("QA + COA", "review, sign, release")],
        note="Each test family gets its own subsample and its own preparation. The potency gram is not the microbial gram."), 1,
      "The testing pipeline. The batch is only ever represented by the sample taken at step 1 — "
      "everything downstream measures that sample, not your room."),
    p("Each family of tests uses different physics, which is why one lab houses half a dozen instruments:"),
    table(["Test family", "What it looks for", "Typical instrument", "Typical timeframe"], [
      ["Potency (cannabinoids)", "THCA, Δ9-THC, CBDA, CBD, CBGA, minor cannabinoids", "HPLC-DAD (liquid chromatography)", "1–3 days"],
      ["Terpenes", "aroma volatiles (myrcene, limonene…)", "GC-MS / GC-FID (gas chromatography)", "1–3 days"],
      ["Microbial", "TAMC, TYM, pathogens, Aspergillus", "Culture plates (CFU) or qPCR (DNA)", "plates 3–7 days; qPCR hours"],
      ["Heavy metals", "arsenic, cadmium, lead, mercury", "ICP-MS after acid digestion", "1–3 days"],
      ["Pesticides", "panels of dozens of residues", "LC-MS/MS + GC-MS/MS", "2–5 days"],
      ["Mycotoxins", "aflatoxins B1/B2/G1/G2, ochratoxin A", "LC-MS/MS", "2–5 days"],
      ["Residual solvents", "butane, ethanol, acetone…", "headspace GC", "1–3 days"],
      ["Moisture / water activity", "water content; water availability", "loss-on-drying balance; a<sub>w</sub> meter", "same day"],
    ], cls="compact", caption="The main test families on a full-panel cannabis COA and the instruments behind them."),
    callout("note", "Why turnaround varies",
      p("Culture-based microbiology is the slow lane, colonies need days to grow. qPCR collapses that to "
        "hours, which is one reason labs and regulators have been migrating to it, with trade-offs covered in "
        "the microbial section below.")),
  ]})

# ---------------------------------------------------------------- 4. read a COA
SECTIONS.append({"id": "read-a-coa", "kicker": "Line by line", "title": "Reading a COA, Block by Block",
  "blocks": [
    p("Below is a mock certificate from a fictional lab, <em>Example Analytical Ltd</em>, laid out the way "
      "most real ones are. The eight callouts are the eight places your eyes should go, in order."),
    figure(_FIGS["mockcoa"], 2,
      "A mock COA with the eight blocks annotated. Every real certificate is a variation on this layout: "
      "identity, sample metadata, potency table, contaminant panels, and a release signature."),
    steps([
      ("Lab identity and accreditation", "A real lab puts its name, address and accreditation number where "
       "you can check them against the accreditation body's public register. A PDF with a logo and no "
       "accreditation number is just a nicely typeset claim."),
      ("Report ID and version", "One report, one version. Amended reports (&lsquo;v2&rsquo;) happen "
       "legitimately, but an amendment that only ever moves THC upward deserves questions."),
      ("Sample metadata", "Sample ID, batch/lot, matrix, mass received, dates. And who did the sampling. "
       "&lsquo;Client-submitted&rsquo; means the number describes whatever was in the bag you sent, which is "
       "a very different claim from a lab-sampled batch result."),
      ("Basis and moisture", "As-received or dry-weight, with the measured moisture. Without this line, two "
       "COAs cannot be compared at all, see the basis section below."),
      ("The potency table", "THCA and Δ9-THC on separate rows (an HPLC signature), minor cannabinoids, a "
       "starred total. Verify: total THC = Δ9-THC + 0.877 × THCA. On the mock: 0.92 + 0.877 × 24.20 = "
       "22.14%. It reconciles. If it doesn't, ask why before you trust anything else on the page."),
      ("Footnotes and LOQs", "ND means &lsquo;not detected above the limit shown&rsquo;, never zero. The "
       "LOQ column is what makes ND mean something. Its absence is a reporting failure."),
      ("Contaminant panels", "Each family (microbial, metals, pesticides, mycotoxins, solvents) is a "
       "separate test on a separate subsample. A stellar THC number and a failed Aspergillus test live "
       "happily on the same certificate."),
      ("Release signature and the small print", "A named QA person, dated. Then the ISO-language honesty "
       "clause: <em>results relate only to the sample as received</em>. That sentence is the legal truth of "
       "everything above it."),
    ]),
    callout("tip", "Verify the certificate itself",
      p("Accredited labs will confirm a report number if you ring them, and many print a QR code or portal "
        "link for verification. Fake and altered COAs circulate in every market. A two-minute check beats "
        "arguing with a buyer later.")),
  ]})

# ---------------------------------------------------------------- 5. potency math
SECTIONS.append({"id": "potency-math", "kicker": "The 0.877 factor", "title": "Total THC: the Maths and the Chemistry",
  "blocks": [
    p("The living plant barely makes any THC. It makes <strong>THCA</strong>, tetrahydrocannabinolic acid, "
      "the same molecule wearing a carboxyl group (–COOH). THCA is not intoxicating; heat converts it to THC "
      "by <strong>decarboxylation</strong>: the carboxyl group breaks off and leaves as CO₂ gas" +
      _c("wang2016-decarb") + ". A lighter, a vape, an oven. That is where most of the THC in your life is "
      "actually created."),
    figure(_FIGS["totalthc"], 3,
      "Mass balance of decarboxylation. THCA (358.5 g/mol) loses CO₂ (44.0 g/mol) and becomes THC "
      "(314.5 g/mol). The ratio 314.5 ÷ 358.5 = 0.877 is why a gram of THCA can only ever yield 0.877 g of "
      "THC, 12.3% of the acid's mass was never THC to begin with."),
    p("That is the whole mystery of the 0.877 factor: <strong>it is a molecular-weight ratio, not a "
      "correction fudge</strong>. THC weighs 314.5 g/mol; THCA weighs 358.5 g/mol; 314.5 ÷ 358.5 = 0.877. So "
      "the standard label formula is:"),
    callout("key", "Total THC = Δ9-THC + (0.877 × THCA)",
      p("This is the &lsquo;total potential THC&rsquo; convention used by regulators and analytics datasets "
        "alike" + _c("zoorob2021-bunching") + _c("jikomes2018-labs") + ". Read it as a <em>ceiling</em>: it "
        "assumes every single THCA molecule survives conversion. Real-world heating never achieves that, "
        "some THCA and THC are destroyed or lost before they reach anyone.")),
    p("How fast does the conversion actually run? In controlled kinetics work, THCA in an open reaction "
      "vessel fully converted in about 30 minutes at 110 °C, about 9 minutes at 130 °C and about 6 minutes "
      "at 145 °C, and, heated in the dark under vacuum, produced no significant CBN (the oxidation "
      "by-product)" + _c("wang2016-decarb") + ". In air, with light and higher temperatures, losses grow, "
      "which is exactly why the formula's assumption of perfect conversion makes it a maximum, not a "
      "prediction."),
    figure(L.line("THCA disappearing at 110 °C",
        [("", 100), ("", 52), ("", 27), ("", 14), ("", 7), ("", 4), ("", 2)],
        ["0", "5", "10", "15", "20", "25", "30 min"],
        ylab="% THCA remaining", ymax=100,
        note="First-order decay consistent with Wang et al. (2016): complete conversion in ~30 min at 110 °C, ~9 min at 130 °C, ~6 min at 145 °C. Curve is schematic."), 4,
      "Decarboxylation kinetics. The acid disappears exponentially with time; hotter is faster but also "
      "riskier for THC itself and brutal on terpenes" + _c("wang2016-decarb") + "."),
    p("Slow decarboxylation also happens at room temperature, during curing and storage, THCA quietly ticks "
      "over to THC, and THC slowly oxidises onward to CBN. This is why an old COA and a fresh one on the same "
      "batch can honestly disagree: the material itself moved."),
    callout("note", "And the same factor family applies to CBD",
      p("CBDA → CBD uses its own molecular-weight ratio (also 0.877, since the acids and neutrals differ by "
        "the same CO₂ group): total CBD = CBD + 0.877 × CBDA. Any &lsquo;total&rsquo; cannabinoid on a COA "
        "should be exactly this arithmetic, recompute it when it matters.")),
  ]})

# ---------------------------------------------------------------- 6. methods
SECTIONS.append({"id": "methods", "kicker": "HPLC vs GC", "title": "Why the Instrument Changes the Answer",
  "blocks": [
    p("Two chromatography families dominate potency testing, and they do not see the same molecules. "
      "<strong>HPLC</strong> (high-performance liquid chromatography) pushes the extract through a column in "
      "liquid at near-room temperature, so THCA and THC arrive at the detector as separate peaks. "
      "<strong>GC</strong> (gas chromatography) must vaporise the sample in an injector inlet at roughly "
      "250–300 °C, and at that temperature THCA decarboxylates on the spot. The acid never reaches the "
      "detector as itself" + _c("lazarjani2020-methods") + "."),
    figure(_FIGS["hplcgc"], 5,
      "The two analysis paths. HPLC runs cool and reports THCA and THC separately, so total THC is computed "
      "with the 0.877 factor. GC destroys the acid in the hot inlet: it reports a single &lsquo;THC&rsquo; "
      "number that silently includes converted THCA. And the conversion is not even complete" +
      _c("dussy2005-thca") + "."),
    p("The nasty detail is that the in-inlet conversion is <em>incomplete and variable</em>. Classic forensic "
      "work isolating pure THCA found decarboxylation under GC conditions converted only around 70% of the "
      "acid, and concluded that the only exact route to total THC is to measure THCA and THC separately and "
      "add them arithmetically. Any post-decarboxylation measurement gives a minimum, not the true "
      "value" + _c("dussy2005-thca") + ". On GC, acids are invisible unless the lab derivatises them first (a "
      "chemical cap that survives the heat)" + _c("lazarjani2020-methods") + "."),
    table(["", "HPLC-DAD", "GC-FID / GC-MS"], [
      ["Operating temperature", "≈25–40 °C column", "≈250–300 °C inlet, hot column"],
      ["Sees THCA and THC separately?", "Yes, two peaks", "No, acid decarboxylates in the inlet"],
      ["Total THC comes from", "arithmetic: THC + 0.877 × THCA", "one merged peak (conversion incomplete" + _c("dussy2005-thca") + ")"],
      ["Derivatisation needed for acids", "No", "Yes, or the acids are lost" + _c("lazarjani2020-methods")],
      ["Typical role today", "potency (industry standard)", "terpenes, residual solvents; potency in some jurisdictions"],
    ], cls="compact", caption="The two chromatography families. Neither is wrong. But their numbers are not directly comparable."),
    callout("warn", "A flower COA with no THCA row is telling you something",
      p("Either the lab ran GC (fine, but the total is a floor, not an exact number), or the report is "
        "hiding detail. Both are reasons to ask for the method reference, which any accredited lab lists on "
        "the certificate.")),
  ]})

# ---------------------------------------------------------------- 7. units & basis
SECTIONS.append({"id": "units-basis", "kicker": "Units and water", "title": "Percent, mg/g and the Moisture Basis",
  "blocks": [
    p("Units first, because this one is mercifully simple: <strong>% w/w and mg/g are the same number, one "
      "decimal place apart.</strong> 1% w/w = 10 mg/g. Flower COAs usually report %, oils and edibles often "
      "report mg/g or mg per unit. 22.14% = 221.4 mg/g. No trap here beyond unfamiliarity."),
    p("The basis is the real trap. Flower is roughly 10–13% water when properly dried. A potency percentage "
      "can be computed against the total mass including that water (<strong>as-received</strong> / "
      "&lsquo;as-is&rsquo;), or against the solids alone (<strong>dry-weight</strong>). Same flower, same "
      "chemistry, two different numbers:"),
    figure(_FIGS["basis"], 6,
      "The moisture basis. On an as-received basis this flower reads 20.0% total THC; strip the 12% of "
      "water out of the denominator and the identical flower reads 22.7% dry-weight. Neither number is "
      "wrong. They are answers to two different questions."),
    table(["Moisture content", "As-received reading", "Dry-weight equivalent"], [
      ["8%", "20.0%", "21.7%"],
      ["10%", "20.0%", "22.2%"],
      ["12%", "20.0%", "22.7%"],
      ["15%", "20.0%", "23.5%"],
    ], cls="compact", caption="Dry-weight % = as-received % ÷ (1 − moisture fraction). The wetter the sample, the bigger the gap."),
    callout("warn", "Never compare across bases",
      p("Your 22% dry-weight COA against a competitor's 20% as-received COA compares two "
        "different denominators. Check the basis line first, convert, then compare. Interlaboratory studies "
        "show labs vary meaningfully even on the moisture measurement itself" + _c("nist-cannaqap2") + ", so "
        "small cross-COA gaps are noise.")),
  ]})

# ---------------------------------------------------------------- 8. sampling
SECTIONS.append({"id": "sampling", "kicker": "Sampling theory", "title": "The Sample Defines the Number",
  "blocks": [
    p("Everything the instrument will ever see is decided before the courier arrives. A batch might be 12 kg; "
      "the composite sample a few tens of grams; the analytical portion that actually gets extracted, "
      "<strong>half a gram to a gram</strong>. That gram speaks for everything. Which is why pharmacopoeial "
      "guidance treats sampling procedure as a quality attribute in its own right, not paperwork" +
      _c("sarma2020-usp") + "."),
    figure(_FIGS["sampling"], 7,
      "The sampling funnel. Increments pulled from multiple containers and positions are combined into a "
      "composite, homogenised, and subsampled down to the analytical portion. Every arrow is a place the "
      "number can drift away from the batch truth."),
    p("Cannabis makes this harder than most matrices because the analyte lives in the trichomes, and "
      "trichomes are not evenly distributed: top colas that grew in strong light run richer than shaded "
      "lower buds, small buds shed resin in handling, and ground material stratifies as kief settles. A "
      "sample built from the prettiest top nugs is not a batch sample. It is a brochure."),
    steps([
      ("Define the batch first", "One cultivar, one room, one harvest, one process. If it isn't homogeneous "
       "by construction, no sampling plan can rescue it."),
      ("Pull increments, not a grab", "Multiple increments from different containers, positions and depths, "
       "including the unglamorous middle and bottom. More, smaller increments beat one big scoop."),
      ("Composite and record", "Combine increments, record who pulled what, from where, when. This is the "
       "start of chain of custody."),
      ("Homogenise before splitting", "Grind and mix before any subsample is taken, for potency, the lab "
       "does this again on its portion."),
      ("Keep a retained twin", "Split a duplicate sample and store it. When a number looks wrong, the "
       "retained sample is your only honest recourse."),
    ]),
    callout("warn", "Cherry-picking is self-deception with a paper trail",
      p("Sending top-cola-only samples inflates the certificate, your customer's expectations, and your own "
        "process data all at once. The batch will eventually be smoked by someone who bought the number. "
        "Sample like you'll be audited, in medicinal frameworks, you will be.")),
    p("Even perfect sampling leaves honest variance: duplicate composites from one batch, run by one lab, "
      "routinely land a point or so of THC apart. Treat differences of one to two percentage points as the "
      "noise floor of the whole exercise, not as information."),
  ]})

# ---------------------------------------------------------------- 9. microbial
SECTIONS.append({"id": "microbial", "kicker": "Microbiology", "title": "Microbial Testing: Plates, qPCR and Aspergillus",
  "blocks": [
    p("Microbial testing asks two kinds of question. <em>How much is growing on this?</em>, answered by "
      "counts: total aerobic microbial count (<strong>TAMC</strong>), total yeast and mould "
      "(<strong>TYM</strong> / TYMC), bile-tolerant Gram-negatives. And <em>is anything dangerous "
      "present?</em>, answered by presence/absence tests for specified organisms: <em>Salmonella</em>, "
      "pathogenic <em>E. coli</em>, and in inhaled products the four pathogenic <em>Aspergillus</em> species."),
    defterm("CFU (colony-forming unit)", "One viable organism (or clump) that grows into a countable colony "
            "on a culture plate. Plate results are CFU per gram."),
    defterm("qPCR", "Quantitative polymerase chain reaction, counts copies of target DNA instead of growing "
            "anything. Fast (hours) and species-specific, but DNA outlives the organism that carried it."),
    table(["Test", "What it counts", "Common limit style", "Notes"], [
      ["TAMC", "aerobic bacteria (CFU/g)", "order of 10⁵ CFU/g; varies by jurisdiction" + _c("jameson2022-stateregs"), "general bioburden indicator"],
      ["TYM / TYMC", "yeasts + moulds (CFU/g)", "order of 10⁴ CFU/g; the contested one", "flower hosts a natural surface flora"],
      ["Bile-tolerant Gram-negatives", "gut-associated bacteria", "order of 10³ CFU/g", "hygiene indicator"],
      ["Specified pathogens", "Salmonella, shiga-toxin E. coli", "absent in 1 g", "hard pass/fail"],
      ["Aspergillus (pathogenic spp.)", "A. fumigatus, flavus, niger, terreus", "not detected in 1 g", "usually enrichment + qPCR"],
    ], cls="compact", caption="The microbial panel. Numeric limits differ across jurisdictions, the shapes of the tests do not" + _c("jameson2022-stateregs") + "."),
    p("Plates and qPCR genuinely disagree, and metagenomic sequencing has shown why: culture media select. "
      "When researchers sequenced what actually grew in standard culture-based yeast-and-mould tests of "
      "cannabis, the plates were growing organisms including bacteria, while toxigenic fungi present on the "
      "flower were under-represented, and organisms of real clinical concern could be missed "
      "entirely" + _c("mckernan2016-tym") + ". Meanwhile qPCR happily counts DNA from dead cells, so a "
      "batch remediated with heat or irradiation can fail qPCR while passing plates."),
    table(["", "Culture plating", "qPCR"], [
      ["Measures", "what grows on that medium, at that temperature", "copies of target DNA"],
      ["Time", "3–7 days", "hours"],
      ["Counts dead organisms?", "no", "yes, DNA persists after kill steps"],
      ["Species identification", "poor without follow-up work", "built into the primers"],
      ["Characteristic failure", "wrong organisms grow; targets don't" + _c("mckernan2016-tym"), "dead-DNA false fails; primer mismatch"],
    ], cls="compact", caption="Why the same batch can pass one microbial method and fail the other. Always read the method line."),
    callout("danger", "Why Aspergillus is presence/absence, not a count",
      p("Inhaled <em>Aspergillus</em> can cause invasive aspergillosis in immunocompromised people, exactly "
        "the population medicinal cannabis serves. A count-based limit makes no sense for an organism where "
        "the acceptable inhaled dose for a transplant patient is effectively zero; hence &lsquo;not detected "
        "in 1 g&rsquo;.")),
  ]})

# ---------------------------------------------------------------- 10. metals
SECTIONS.append({"id": "metals", "kicker": "Heavy metals", "title": "The Big Four and the ICP-MS",
  "blocks": [
    p("Cannabis is an enthusiastic accumulator of metals. The same trait that gets hemp planted for soil "
      "remediation pulls cadmium and lead out of your substrate, fertiliser and water and stores them in "
      "tissue. The panel nearly everywhere centres on the <strong>big four</strong>: arsenic, cadmium, lead "
      "and mercury, with some frameworks screening a wider element list" + _c("nist-cannaqap2") + "."),
    table(["Metal", "Typical routes into flower", "Why it's on the panel"], [
      ["Arsenic (As)", "bore water, some rock-derived amendments", "carcinogen"],
      ["Cadmium (Cd)", "phosphate fertilisers, contaminated substrate", "readily taken up by the plant; accumulates in kidneys"],
      ["Lead (Pb)", "dust and soil contact, old solder/pipework, contaminated inputs", "neurotoxin, no safe exposure level"],
      ["Mercury (Hg)", "rare, water or industrial contamination", "neurotoxin"],
    ], cls="compact", caption="The big four. Limits vary by jurisdiction and are stricter for inhaled products than oral ones" + _c("jameson2022-stateregs") + "."),
    p("The instrument is <strong>ICP-MS</strong>, inductively coupled plasma mass spectrometry. The lab "
      "digests the sample in hot acid until nothing but dissolved elements remain, sprays that solution into "
      "an argon plasma running at thousands of degrees, and counts the resulting ions by mass. It is "
      "absurdly sensitive, parts-per-billion, which is why metals results carry LOQs that look like "
      "0.01 µg/g."),
    callout("tip", "Your inputs are your metals programme",
      p("Flower fails metals because something upstream carried them in. Collect certificates for every "
        "fertiliser and substrate lot, test source water, and a metals fail becomes a lookup instead of a "
        "mystery. Inhalation limits are tight enough that one contaminated input lot can sink a batch.")),
  ]})

# ---------------------------------------------------------------- 11. pesticides
SECTIONS.append({"id": "pesticides", "kicker": "Pesticides", "title": "Pesticide Panels: a List, Not a Guarantee",
  "blocks": [
    p("A pesticide test is a <em>panel</em>: a defined list of compounds, each measured against an action "
      "limit. Pass means &lsquo;nothing on <em>this list</em> was found above <em>these limits</em>&rsquo;, "
      "it does not mean pesticide-free, and it says nothing about compounds the panel doesn't include. That "
      "distinction matters because panels differ absurdly between jurisdictions: a survey of US state rules "
      "found 551 distinct pesticides regulated somewhere, with action limits for the same compound spanning "
      "up to four orders of magnitude between states" + _c("jameson2022-stateregs") + "."),
    ul(["<strong>Two instruments are needed for coverage.</strong> LC-MS/MS catches most modern residues; "
        "GC-MS/MS catches the volatile and halogenated ones. A lab quoting a big panel runs both.",
        "<strong>Inhalation changes the toxicology.</strong> Residues that are tolerated on lettuce can "
        "pyrolyse into nastier chemistry when smoked. Some fungicides are reported to release hydrogen "
        "cyanide on combustion, which is why cannabis limits are often far tighter than food limits.",
        "<strong>History justifies the paranoia.</strong> Pre-regulation Californian concentrate screening "
        "found pesticides in roughly one-third of samples" + _c("raber2015-dabs") + ".",
        "<strong>Drift and carryover count.</strong> You can fail a panel without ever spraying, neighbouring "
        "agriculture, contaminated secondhand equipment, or a dirty trim room can deposit residues."]),
    callout("note", "Reading a pesticide section",
      p("Look for: the panel size (how many analytes), the action limits and their source, the LOQ per "
        "analyte, and the method (LC-MS/MS, GC-MS/MS or both). A one-line &lsquo;Pesticides: PASS&rsquo; "
        "with none of that attached is a vibe, not a result.")),
  ]})

# ---------------------------------------------------------------- 12. solvents & mycotoxins
SECTIONS.append({"id": "solvents-myco", "kicker": "Solvents · mycotoxins", "title": "Residual Solvents and Mycotoxins",
  "blocks": [
    p("<strong>Residual solvents</strong> apply to extracts: whatever chemistry pulled the resin out, "
      "butane, propane, ethanol, CO₂ with ethanol polish. Traces can remain, and headspace GC measures them "
      "in the finished product. Limits are set per solvent, loosely following pharmaceutical solvent classes: "
      "near-zero tolerance for the genuinely toxic ones (benzene, toluene, never used deliberately, but "
      "present as impurities in cheap gas), workaday limits for the common process solvents."),
    p("Why does a <em>solventless</em> hash or rosin still carry a solvent test? Three honest reasons. The "
      "product category triggers the test in most rule sets regardless of process; the test is the only way "
      "to <em>verify</em> the solventless claim rather than take it on faith; and contamination doesn't need "
      "an extraction step, cleaning agents, fuels and off-gassing in storage can introduce volatiles. A "
      "clean solvent panel on rosin is cheap proof your marketing is true. Early concentrate surveys found "
      "residual solvents in around 30% of samples, so buyers learned to ask" + _c("raber2015-dabs") + "."),
    p("<strong>Mycotoxins</strong> are the chemical ghosts of mould: aflatoxins B1, B2, G1, G2 (from "
      "<em>Aspergillus flavus</em> and relatives) and ochratoxin A, measured by LC-MS/MS at parts-per-billion "
      "limits" + _c("jameson2022-stateregs") + ". Two facts make them their own line on the COA rather than a "
      "footnote to the microbial section:"),
    ul(["<strong>They outlive the mould.</strong> Kill steps (heat, irradiation, ozone) can crash a TYM "
        "count while leaving the toxins fully intact. A batch can pass microbiology and still fail "
        "mycotoxins, and remediated product is exactly where to expect that pattern.",
        "<strong>They are potent at absurdly low doses.</strong> Aflatoxin B1 is among the strongest natural "
        "carcinogens known, hence limits in the µg/kg (ppb) range in medicinal frameworks" + _c("tga-tgo93") + "."]),
    callout("warn", "Remediation is not exoneration",
      p("Irradiated or heat-treated flower that now passes plate counts still carries whatever toxins the "
        "mould made first, and its dead DNA may still fail qPCR. If a batch needed remediation, the "
        "mycotoxin line is the one to read hardest.")),
  ]})

# ---------------------------------------------------------------- 13. water activity
SECTIONS.append({"id": "water-activity", "kicker": "Water in two numbers", "title": "Water Activity vs Moisture Content",
  "blocks": [
    p("Two water numbers appear on flower COAs and they answer different questions. <strong>Moisture "
      "content</strong> (%) is <em>how much</em> water is in the sample, mass of water over total mass. "
      "<strong>Water activity</strong> (a<sub>w</sub>, scale 0–1) is <em>how available</em> that water is to "
      "microbes, the equilibrium relative humidity the sample generates in a sealed space. Mould does not "
      "care how much water you have; it cares whether it can get at it. That makes a<sub>w</sub> the "
      "microbially meaningful number, and it is why pharmacopoeial thinking on stored cannabis centres on a "
      "water-activity specification of ≤0.65" + _c("sarma2020-usp") + "."),
    figure(L.zones("Water activity: where mould can and cannot operate", 0.30, 0.90,
        [(0.30, 0.55, L.AMBL, "over-dry: brittle, harsh"),
         (0.55, 0.65, L.GL, "target window"),
         (0.65, 0.70, L.AMBL, "caution"),
         (0.70, 0.90, L.REDL, "mould can grow")],
        unit=" aw",
        note="Below 0.55 the flower suffers (brittle trichomes, harsh smoke); 0.55-0.65 is the widely used spec window; above ~0.65 xerotolerant moulds wake up."), 8,
      "The water-activity scale for stored flower. The 0.65 upper bound is the line most specifications "
      "draw" + _c("sarma2020-usp") + "; the lower bound is about product quality, not safety."),
    table(["", "Moisture content", "Water activity (a<sub>w</sub>)"], [
      ["What it measures", "how much water (% of mass)", "how available the water is (0–1)"],
      ["Instrument", "loss-on-drying balance", "chilled-mirror / capacitive a<sub>w</sub> meter"],
      ["Microbial relevance", "indirect, depends on how water is bound", "direct. Growth thresholds are a<sub>w</sub> thresholds"],
      ["Typical spec for flower", "≈10–13%", "0.55–0.65"],
    ], cls="compact", caption="Same water, two questions. A batch can sit at a normal moisture % and still have unsafe water activity, and vice versa, the sorption curve differs by cultivar and trim."),
    p("Operationally: dry and cure to a water-activity target, and let moisture content be whatever it is. "
      "The paired numbers on the COA also sanity-check each other, a<sub>w</sub> 0.75 with 11% moisture "
      "claims a strange sample; question it."),
  ]})

# ---------------------------------------------------------------- 14. inflation
SECTIONS.append({"id": "inflation", "kicker": "Honesty section", "title": "The Inflation Problem: What the Record Shows",
  "blocks": [
    p("If a single number sets the price, the number comes under pressure. That is the "
      "documented, peer-reviewed history of legal cannabis markets, and any grower choosing a lab should "
      "know it cold."),
    figure(L.hbars("How often measured THC missed the label",
        [("2023 flower (CO)", 70), ("2024 flower (3 states)", 70),
         ("2025 flower (CO)", 43), ("2025 concentrates (CO)", 4)],
        unit="%",
        note="Share of retail products whose measured total THC missed the labelled value: >15% below label (2023); outside +/-20% (2024); outside +/-15% (2025)."), 9,
      "Label accuracy in peer-reviewed retail studies: 70% of Colorado flower samples ran more than 15% "
      "below label" + _c("schwabe2023-inflated") + "; 70% of a 107-sample, three-state audit fell outside "
      "±20% of label" + _c("geweda2024-audit") + "; and in 2025, 43% of flower but only 4% of concentrates "
      "missed a ±15% window" + _c("giordano2025-accuracy") + ". Flower, where sampling is easiest to game, "
      "is where the accuracy problem lives."),
    p("The mechanism is visible in state datasets. Reported potency for chemotype-I flower across "
      "Washington's six largest labs differed <em>systematically</em>: median total THC ranged from 17.7% at "
      "the lowest-reporting lab to 23.2% at the highest, a 5.5-percentage-point spread on comparable "
      "product that persisted after controlling for strain and producer" + _c("jikomes2018-labs") + ". And "
      "reported values &lsquo;bunch&rsquo; just above the magic 20% price threshold: the frequency of "
      "products jumps discontinuously above 20% (a 43% spike in Nevada, 17% in Washington) with the "
      "bunching concentrated at specific labs (two later-suspended labs showed a 47% spike; the state's "
      "largest lab, 1%)" + _c("zoorob2021-bunching") + ". Biology does not know where 20% is. Pricing "
      "does."),
    figure(L.bars("The 20% cliff: products bunch just above the price line",
        [("just below 20%", 100), ("just above (WA)", 117), ("just above (NV)", 143), ("suspended labs", 147)],
        unit="",
        note="Relative frequency of flower products reported in the bin just above 20% THC vs just below (below = 100). The jump has no biological cause.",
        maxv=160), 10,
      "The reporting discontinuity at 20% THC" + _c("zoorob2021-bunching") + ". A smooth biological "
      "distribution should cross 20% smoothly; the observed spike, largest at labs later suspended, is the "
      "statistical fingerprint of inflation."),
    p("<strong>Lab shopping</strong> is the market dynamic that produces this. Split one batch across three "
      "labs, keep the highest number, and give that lab your business. Labs know it. The lab that reports "
      "honestly loses accounts to the lab that reports generously, a race to the bottom wearing a lab coat. "
      "Inflation methods range from soft (flower-only calibration bias, generous rounding, tolerant "
      "sampling) to plainly fraudulent: in 2024 Oregon's regulator charged seven of the state's eleven "
      "accredited labs over inflated THC results, including allegations that staff at three labs spiked "
      "customer samples with kief before analysis" + _c("hs2024-oregon") + ". Licence actions and "
      "competitor lawsuits over inflated potency and passed-but-contaminated product have followed in "
      "California and Massachusetts."),
    callout("evidence", "Variance vs fraud, tell them apart",
      p("Honest inter-lab variance is real even among competent labs, interlaboratory programmes exist "
        "precisely because cannabis measurement comparability is hard" + _c("nist-cannaqap2") + ", but "
        "honest variance is <em>symmetric</em>. It scatters around the truth. Inflation is "
        "<em>directional</em>: always the good news. If a lab's numbers are consistently the best in town, "
        "that is not luck; that is a product they are selling.")),
    p("What an operator does with this: pick a lab for its accreditation scope and method transparency, not "
      "its averages; split-sample occasionally against a second lab and expect ~1–2 points of honest "
      "scatter; keep retained samples; and treat any account manager who <em>promises</em> numbers as a "
      "walking licence risk. In GMP-style medicinal systems the incentive flips, the lab serves batch "
      "release, not marketing. Which is a large part of why those numbers are steadier" + _c("tga-tgo93") +
      _c("nz-mcs-mqs") + "."),
  ]})

# ---------------------------------------------------------------- 15. one number
SECTIONS.append({"id": "single-number", "kicker": "Interpretation", "title": "What One Number Can and Can't Tell You",
  "blocks": [
    p("A COA is genuinely useful, inside its limits. What a single certificate <em>can</em> tell you: the "
      "potency class of the sampled material (a 15% batch and a 25% batch are truly different things); the "
      "pass/fail status of that sample against that panel; and, over many batches from your own room with "
      "consistent sampling, a trend worth steering by. What it <em>cannot</em> tell you:"),
    ul(["<strong>Your whole room's number.</strong> The certificate describes the sample. The batch inherits "
        "it only as far as your sampling was honest.",
        "<strong>Differences of a point or two.</strong> Sampling scatter plus inter-lab spread swamp them, "
        "the documented systematic spread between labs alone was 5.5 points" + _c("jikomes2018-labs") + ".",
        "<strong>Quality, effect or experience.</strong> THC% correlates weakly with what a product is like "
        "to consume; terpenes, minor cannabinoids, cure and freshness carry most of it. Chasing the number "
        "off the certificate is chasing the wrong thing.",
        "<strong>Next batch.</strong> A COA is a record, not a forecast. Genetics × environment × process "
        "will move the next one."]),
    h(3, "When the number looks weird"),
    table(["Symptom", "Most likely explanations", "What to check"], [
      ["THC jumped 3–4 points on the same cultivar", "sampling drift (top colas), basis change, different lab or method", "who sampled; basis + moisture lines; lab and method IDs on both COAs"],
      ["Total THC ≠ THC + 0.877 × THCA", "typo, different total convention, GC-derived total", "recalculate; ask the lab which formula and method they used"],
      ["Flower reporting 35%+ total THC", "biologically implausible for nearly all cultivars, enriched sample or inflation", "split-sample retest at an independent lab; check for kief enrichment"],
      ["TYM failed, retest passed", "different method (plate vs qPCR), different subsample, or remediation in between", "method lines on both COAs; whether the batch was treated between tests"],
      ["Metals failure from nowhere", "new fertiliser or substrate lot, water change, equipment contamination", "input CoAs and lot numbers; source-water test"],
      ["Moisture reads 6% but flower feels normal", "sample dried in transit or sat before analysis", "water activity at pack-out; days between sampling and testing"],
      ["CBD appears in a THC cultivar", "mislabelled genetics, or peak misassignment at the lab", "verify the cultivar; ask the lab to confirm peak identity"],
    ], cls="compact", caption="Triage table: read the metadata before doubting the chemistry, most anomalies live in sampling, basis or method, not in the instrument."),
    h(3, "COA red flags"),
    grid([
      card("No accreditation number", p("Anyone can typeset a PDF. If the lab and its accreditation can't be "
           "verified in a public register, the document is a claim, not a certificate."), tag="identity"),
      card("No LOQ column", p("&lsquo;ND&rsquo; without a limit is uninterpretable, not detected above "
           "<em>what</em>? Serious labs always print it."), tag="reporting"),
      card("Only &lsquo;THC&rsquo;, no THCA row", p("Either a GC method (total is a floor, not exact) or "
           "lazy reporting. Both mean: ask for the method reference."), tag="method"),
      card("Client-submitted, sold as batch-wide", p("The lab measured a bag someone filled. Treating that "
           "as a batch result is the oldest trick in the book."), tag="sampling"),
      card("The local hero lab", p("Always 2–3 points above everyone else in town. That consistency is a "
           "business model, not chemistry" + _c("zoorob2021-bunching") + "."), tag="incentives"),
      card("Amended reports, rising numbers", p("Reissued certificates happen; reissues that only ever move "
           "THC upward with no explanation are a pattern worth walking away from."), tag="paper trail"),
    ], cols=3),
    callout("key", "The mental model to keep",
      p("One certificate = one photograph of one gram, through one lab's lens, on one day. Photographs are "
        "useful. Just never confuse a photograph with the landscape, and be suspicious of anyone whose "
        "photographs are always sunnier than everyone else's.")),
  ]})

# ---------------------------------------------------------------- 16. NZ/AU
SECTIONS.append({"id": "nz-au", "kicker": "Medicinal context", "title": "NZ and Australia: Testing as Release, Not Marketing",
  "blocks": [
    p("In the Australasian medicinal systems the COA plays a structurally different role from a retail "
      "label. In Australia, unapproved medicinal cannabis products must conform to <strong>TGO 93</strong> "
      "(Therapeutic Goods (Standard for Medicinal Cannabis) Order 2017): assayed cannabinoid content must "
      "sit within 90.0–110.0% of the label claim, contaminant limits (including aflatoxins and pesticide "
      "residues) apply, and the regulator can pull and test product at any time" + _c("tga-tgo93") + ". In "
      "New Zealand, products must meet the <strong>minimum quality standard</strong> under the Misuse of "
      "Drugs (Medicinal Cannabis) Regulations 2019, with critical tests performed by GMP-certified "
      "facilities and ISO/IEC 17025 accreditation recognised for the rest" + _c("nz-mcs-mqs") + "."),
    p("The operative concept is <strong>release testing</strong>: a batch is tested against a registered "
      "specification, a qualified person reviews the full data set, and the batch is formally released, or "
      "not. The COA becomes one input to a documented decision, made by someone whose signature carries "
      "liability. Contrast that with a retail market where the COA's main job is to make the jar look good "
      "on a menu, and the potency-inflation record earlier in this paper stops being surprising: same "
      "document, opposite incentive structure."),
    ul(["A 90–110% label-claim window means a batch can <em>fail for being too strong</em>. The target is "
        "accuracy, not magnitude" + _c("tga-tgo93") + ".",
        "Stability data and shelf-life claims ride on the same analytics. The release COA is re-verified "
        "over time, which quietly disciplines the initial numbers.",
        "Testing under GMP means validated methods, qualified instruments and audit trails, the lab's "
        "answer to &lsquo;how do you know?&rsquo; is a documented system, not a shrug."]),
    callout("note", "Scope note, not legal advice",
      p("This section sketches the shape of the frameworks, not their current detail. Standards, schedules "
        "and guidance move; anyone operating under TGO 93 or the NZ scheme should work from the regulator's "
        "current documents" + _c("tga-tgo93") + _c("nz-mcs-mqs") + " and their own quality agreements, not "
        "from a white paper.")),
    p("For growers elsewhere, the takeaway is portable: the closer your own testing practice is to "
      "release-style discipline, fixed sampling SOP, one accredited lab, retained samples, trend charts, "
      "numbers nobody is paid to like. The more your COAs are worth, to you and to anyone auditing you."),
  ]})
