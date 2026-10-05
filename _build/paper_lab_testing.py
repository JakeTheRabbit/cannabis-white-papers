# -*- coding: utf-8 -*-
"""Paper: lab testing, potency and COAs — how to read a certificate of analysis and not be fooled by it."""
import json, os
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        grid, card, chip, kv, steps)
import figs_lib as L

_FIGS = json.load(open(os.path.join(os.path.dirname(__file__), "figs_lab_testing.json"), encoding="utf-8"))

SLUG = "lab-testing-coas"
TITLE = "Laboratory testing, potency and the COA"
EYEBROW = "Harvest · Quality"
SUB = ("A certificate of analysis (COA) is a measurement of one small sample and is not a property "
       "of your crop. This paper shows how to read a COA row by row and how to calculate the total "
       "THC again. It gives the chemistry behind the 0.877 factor. It tells you about each type of "
       "test, from qPCR to ICP-MS. It also gives the facts about numbers that are too high. Tests "
       "find this problem frequently in cannabis markets.")
META = [("flask", "Quality"), ("image", "10 diagrams"),
        ("quote", "16 sources"), ("clock", "~24 min to read")]
RELATED = ["gmp-hash-lab", "harvest-dry-trim-cure"]
REF_IDS = ["schwabe2023-inflated", "zoorob2021-bunching", "jikomes2018-labs", "wang2016-decarb",
           "dussy2005-thca", "lazarjani2020-methods", "sarma2020-usp", "nist-cannaqap2",
           "mckernan2016-tym", "jameson2022-stateregs", "raber2015-dabs", "geweda2024-audit",
           "giordano2025-accuracy", "hs2024-oregon", "tga-tgo93", "nz-mcs-mqs"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

# ---------------------------------------------------------------- 1. start here
SECTIONS.append({"id": "start-here", "kicker": "Start here", "title": "Purpose and scope",
  "blocks": [
    lead("For each batch that you supply to a buyer, a testing laboratory gives a "
         "<strong>certificate of analysis</strong> (<strong>COA</strong>). In a system for "
         "medicinal cannabis, the laboratory also gives a COA for each batch that you release. The "
         "COA is a document of one page. It shows the materials that the flower contains "
         "(cannabinoids and terpenes) and the materials that the flower must not contain (mold, "
         "heavy metals, pesticides, and mycotoxins).</p><p>Most buyers read only one number on the "
         "COA. This number is <strong>total THC</strong>, and it changes the price. Thus some "
         "persons try to get a higher value for this number more frequently than for other numbers. "
         "Tests with peer review show a systematic error. The values on labels in the retail market "
         "are too high" + _c("schwabe2023-inflated") + _c("zoorob2021-bunching") +
         "."),
    p("One fact is important for all sections of this paper. <strong>A COA is not a property of "
      "your crop.</strong> A COA is the measurement of one small sample. A person collected the "
      "sample with one method. The laboratory prepared it with one method and measured it with one "
      "instrument on one day.</p><p>If one of these items changes, the number changes. Fraud is not "
      "necessary for this change. This fact is the cause of many problems in cannabis testing. Some "
      "persons do not know it, and some persons use it to get a higher price. Examples are the same "
      "product with a different number and labels with numbers that are too high. One more example "
      "is the selection of a laboratory for its high numbers."),
    defterm("COA (certificate of analysis)", "The report of a laboratory on the measurements of one "
            "sample. The report gives the ID of the sample, the potency, the contaminants, the "
            "methods, and a signature that releases the batch."),
    defterm("Analyte", "One item that the laboratory measures. For example, THCA, lead, a "
            "pesticide, and the quantity of mold are analytes. A COA is a list of analytes with "
            "results."),
    defterm("Matrix", "The type of material in the sample. For example, dried flower, oil, and an "
            "edible product are three types of matrix. The matrix changes the method that the "
            "laboratory must use to extract and measure the analyte. It also changes how easy the "
            "task is."),
    defterm("Batch / lot", "The specified quantity of product that one COA gives information about. "
            "The sample is only a small number of grams. The primary problem is how accurately the "
            "sample shows the properties of the batch."),
    defterm("LOD / LOQ", "The limit of detection (LOD) is the minimum quantity that the method can "
            "find with a sure result. The limit of quantitation (LOQ) is the minimum quantity for "
            "which the method gives an accurate number. &lsquo;ND&rsquo; (&lsquo;not "
            "detected&rsquo;) shows that the quantity is less than the LOD. It does not show that "
            "the quantity is zero."),
    defterm("ISO/IEC 17025", "The standard for the correct operation of testing laboratories. We "
            "recommend that you examine each COA for an accreditation to this standard."),
    callout("key", "One primary fact",
      p("The COA gives information for one sample. The sample is approximately one gram. One "
        "laboratory measured it with one procedure on one day. Correct sampling and a laboratory "
        "with accreditation make this information accurate for the sample that the laboratory "
        "measured. But the information is for one sample and not for your crop. All the sections of "
        "this paper help you to know how accurately that sample shows the properties of your batch.")),
  ]})

# ---------------------------------------------------------------- 2. core answer
SECTIONS.append({"id": "core-answer", "kicker": "The primary items", "title": "Primary items of laboratory testing",
  "blocks": [
    p("To read a COA in sixty seconds, examine these eight items in this sequence:"),
    ol(["<strong>The laboratory.</strong> Make sure that the COA gives the name of the laboratory "
        "and an accreditation that you can examine (ISO/IEC 17025 or, in systems for medicinal "
        "cannabis, a GMP certificate)" + _c("nz-mcs-mqs") + ".",
        "<strong>The sample.</strong> Find the sample ID, the batch, the matrix, and the sample "
        "mass. Most important, find <em>the person who collected the sample</em>. "
        "&lsquo;Client-submitted&rsquo; shows that the laboratory did not see your batch.",
        "<strong>The basis.</strong> Find the basis (dry-weight or as-received) and the moisture "
        "content. The basis changes the potency by approximately 10 to 15%.",
        "<strong>The potency table.</strong> A row for the acids (THCA) and a row for the neutral "
        "cannabinoids (THC) show an HPLC method. Then calculate the total THC: total THC = Δ9-THC + "
        "0.877 × THCA. The result must agree with the total on the COA.",
        "<strong>The units.</strong> The units % w/w and mg/g measure the same quantity (1% = 10 "
        "mg/g). Do not let a change of unit cause an error.",
        "<strong>Each type of contaminant</strong> (microbes, metals, pesticides, mycotoxins, and "
        "solvents) has a different test and a different method. The result of each test is "
        "satisfactory or unsatisfactory. The potency does not give information about safety.",
        "<strong>The footnotes.</strong> Find the LOQs, the definition of &lsquo;ND&rsquo;, and the "
        "references to the methods. If the COA has no LOQ column, you do not know the limit for the "
        "result &lsquo;ND&rsquo;.",
        "<strong>The signature.</strong> Find a signature with a name and a date from a person in "
        "QA. In GMP systems, this signature makes the COA a decision to release the batch and not a "
        "tool for marketing" + _c("tga-tgo93") + "."]),
    p("This paper also gives the facts about numbers that are too high. Tests with peer review show "
      "that the potency values on labels in some legal markets have a systematic error. In one "
      "test, the measured value of 70% of the Colorado flower samples was more than 15% less than "
      "the label value" + _c("schwabe2023-inflated") + ". In an audit of three states, the measured "
      "value of 70% of the samples was not in the range of ±20% of the label value" +
      _c("geweda2024-audit") + ". The number of products with a value that is a small quantity more "
      "than the price threshold of 20% THC is too high" + _c("zoorob2021-bunching") +
      ".</p><p>When one number sets the price, some persons will try to change it. Your protection "
      "is to know how the laboratory makes the number. The remaining sections of this paper give "
      "this information."),
  ]})

# ---------------------------------------------------------------- 3. pipeline
SECTIONS.append({"id": "pipeline", "kicker": "From sample to COA", "title": "Laboratory testing procedure",
  "blocks": [
    p("The COA is the last item of a sequence of steps that starts when a person collects the "
      "sample. Each step changes the numbers on the COA. The sampling and the sample preparation "
      "change the numbers more than the instrument does."),
    figure(L.flow("From batch to certificate",
        [("Sample", "samples from all parts of the batch"),
         ("Intake", "Record. Chain of custody starts"),
         ("Prepare", "grind, extract, dilute for tests"),
         ("Instruments", "HPLC, ICP-MS, qPCR, GC"),
         ("QA + COA", "signature to release")],
        note="Each test has a different part of the sample and a different sample preparation. The gram for potency is not the gram for microbes."), 1,
      "The testing procedure. The sample from step 1 is the only item that shows the batch. All "
      "subsequent steps measure that sample and not your room."),
    p("Each type of test uses different physics. Thus a laboratory has approximately six instruments:"),
    table(["Type of test", "Analytes", "Typical instrument", "Typical time"], [
      ["Potency (cannabinoids)", "THCA, Δ9-THC, CBDA, CBD, CBGA, minor cannabinoids", "HPLC-DAD (liquid chromatography)", "1–3 days"],
      ["Terpenes", "volatile compounds of the aroma (for example myrcene and limonene)", "GC-MS / GC-FID (gas chromatography)", "1–3 days"],
      ["Microbes", "TAMC, TYM, pathogens, Aspergillus", "Culture plates (CFU) or qPCR (DNA)", "3 to 7 days for plates and hours for qPCR"],
      ["Heavy metals", "arsenic, cadmium, lead, mercury", "ICP-MS after acid digestion", "1–3 days"],
      ["Pesticides", "panels of many pesticide residues", "LC-MS/MS + GC-MS/MS", "2–5 days"],
      ["Mycotoxins", "aflatoxins B1/B2/G1/G2, ochratoxin A", "LC-MS/MS", "2–5 days"],
      ["Residual solvents", "for example butane, ethanol, and acetone", "headspace GC", "1–3 days"],
      ["Moisture / water activity", "water content and how available the water is", "loss-on-drying balance and a<sub>w</sub> meter", "same day"],
    ], cls="compact", caption="The table shows the primary types of test on a COA for cannabis with all the panels, and the instruments for these tests."),
    callout("note", "Turnaround time changes with the method",
      p("Tests with culture are slow. Some days are necessary for colonies to increase in size. "
        "qPCR decreases this time to a number of hours. The short time is one cause of the change "
        "to qPCR in laboratories and authorities. The section on microbes below compares the two "
        "methods.")),
  ]})

# ---------------------------------------------------------------- 4. read a COA
SECTIONS.append({"id": "read-a-coa", "kicker": "Row by row", "title": "How to read a certificate of analysis",
  "blocks": [
    p("This section has an example COA. It is from a laboratory with the example name <em>Example "
      "Analytical Ltd</em>. The COAs of most laboratories have the same blocks in the same "
      "sequence. The COA has eight areas with numbers. Examine the areas in the sequence of the "
      "numbers."),
    figure(_FIGS["mockcoa"], 2,
      "An example COA with the eight blocks identified. Each COA from a laboratory is a variation "
      "of this sequence of blocks. The blocks are the name of the laboratory, the sample "
      "information, the potency table, the contaminant panels, and a signature that releases the "
      "batch."),
    steps([
      ("Name and accreditation of the laboratory", "A COA from a laboratory with accreditation gives the "
       "name, the address, and the accreditation number of the laboratory. Compare these data with "
       "the public register of the authority that gave the accreditation. A PDF with a logo and no "
       "accreditation number is only a claim."),
      ("Report ID and version", "A report has one version. A laboratory can make a new version "
       "(&lsquo;v2&rsquo;) of a report for a correct cause. But if each new version only increases "
       "the THC value, tell the laboratory to give the cause."),
      ("Sample information", "This block gives the sample ID, the batch or lot, and the matrix. It "
       "also gives the mass that the laboratory received and the dates. It shows the person who "
       "collected the sample. &lsquo;Client-submitted&rsquo; shows that the number is for the "
       "material in the bag that you sent. This result is very different from the result for a "
       "batch with a sample that the laboratory collected."),
      ("Basis and moisture", "This block gives the basis (as-received or dry-weight) and the "
       "measured moisture. Without this row, you cannot compare two COAs. The section on the basis "
       "below gives more information."),
      ("The potency table", "This block has a row for THCA and a row for Δ9-THC (the two rows show "
       "an HPLC method). It also has the minor cannabinoids and a total with an asterisk (*). "
       "Calculate the total THC: total THC = Δ9-THC + 0.877 × THCA. In the example, 0.92 + 0.877 × "
       "24.20 = 22.14%. This result agrees with the total on the COA. If the values are not the "
       "same, find the cause before you accept other data on the page."),
      ("Footnotes and LOQs", "&lsquo;ND&rsquo; shows that the laboratory did not find the analyte "
       "in a quantity more than the limit in the report. It does not show zero. The LOQ column "
       "gives this limit, and thus you can use the result &lsquo;ND&rsquo;. If the report has no "
       "LOQ column, the report is defective."),
      ("Contaminant panels", "Each type (microbes, metals, pesticides, mycotoxins, and solvents) is "
       "a different test on a different part of the sample. A COA can show a very high THC number "
       "and an unsatisfactory result for Aspergillus."),
      ("Signature for release and the last clause", "A person from QA gives a name and a date. Then "
       "there is an ISO clause that limits the results: <em>&lsquo;Results relate only to the "
       "sample as received&rsquo;</em>. This clause shows the limit of all the data above it."),
    ]),
    callout("tip", "Examine the COA as a document",
      p("If you speak to a laboratory with accreditation, the laboratory can tell you if a report "
        "number is correct. Many laboratories give a QR code or a link that you can use to examine "
        "the report. In all markets, some COAs are not from the laboratory that the COA shows, and "
        "a person changed some COAs. A check of two minutes can prevent a problem with a buyer "
        "after you supply the batch.")),
  ]})

# ---------------------------------------------------------------- 5. potency math
SECTIONS.append({"id": "potency-math", "kicker": "The 0.877 factor", "title": "Total THC: how to calculate it, and the chemistry",
  "blocks": [
    p("The plant makes almost no THC. It makes <strong>THCA</strong> (tetrahydrocannabinolic acid). "
      "THCA is THC with an attached chemical group (–COOH). This group makes THCA a "
      "non-intoxicating cannabinoid. THCA is also approximately 13% heavier than THC.</p><p>Heat "
      "removes this group as CO₂ gas. This reaction is <strong>decarboxylation</strong>" +
      _c("wang2016-decarb") + ". After the reaction, the compound is chemically different. The heat "
      "of a flame, a vaporizer, or an oven causes this reaction. Thus this reaction makes most of "
      "the THC that a person uses."),
    figure(_FIGS["totalthc"], 3,
      "The mass balance of decarboxylation. THCA (358.5 g/mol) releases CO₂ (44.0 g/mol) and "
      "becomes THC (314.5 g/mol). The ratio 314.5 ÷ 358.5 = 0.877 shows that one gram of THCA can "
      "make a maximum of 0.877 g of THC. 12.3% of the mass of the acid is not THC."),
    p("<strong>The 0.877 factor is a ratio of molecular weights. It is not a correction.</strong> "
      "THC has a molecular weight of 314.5 g/mol, and THCA has a molecular weight of 358.5 g/mol. "
      "The ratio is 314.5 ÷ 358.5 = 0.877. Thus the standard formula for labels is:"),
    callout("key", "Total THC = Δ9-THC + (0.877 × THCA)",
      p("Authorities and laboratories use this method to calculate the &lsquo;total potential "
        "THC&rsquo;" + _c("zoorob2021-bunching") + _c("jikomes2018-labs") + ". The result is a "
        "<em>maximum</em>. The method is correct only if all the THCA molecules change to THC. But "
        "the heat does not change all the THCA. The quantities of THCA and THC decrease before a "
        "person uses them.")),
    p("A test with controlled conditions measured the speed of the conversion. In an open reaction "
      "vessel, all the THCA changed to THC in approximately 30 minutes at 110 °C (230 °F). The time "
      "was approximately 9 minutes at 130 °C (266 °F) and approximately 6 minutes at 145 °C (293 "
      "°F). When the test applied heat without light and in a vacuum, no important quantity of CBN "
      "(a product of oxidation) occurred" + _c("wang2016-decarb") + ".</p><p>In air, with light, "
      "and at higher temperatures, the quantities of THCA and THC decrease more. The formula is "
      "correct only if all the THCA changes to THC. Thus the formula gives a maximum and not an "
      "estimate of the result."),
    figure(L.line("THCA decreases at 110 °C",
        [("", 100), ("", 52), ("", 27), ("", 14), ("", 7), ("", 4), ("", 2)],
        ["0", "5", "10", "15", "20", "25", "30 min"],
        ylab="% THCA remaining", ymax=100,
        note="First-order decay agrees with the test of Wang (2016): all THCA changes in approximately 30 min at 110 °C (230 °F), 9 min at 130 °C (266 °F), 6 min at 145 °C (293 °F). The curve is only an example."), 4,
      "The speed of decarboxylation. The quantity of the acid shows exponential decay with time. At "
      "a higher temperature, the reaction is faster. But the risk to the THC is also higher, and "
      "the damage to the terpenes is large" + _c("wang2016-decarb") + "."),
    p("Decarboxylation also occurs slowly at room temperature, for example during curing and in "
      "storage. Some THCA changes to THC, and some THC changes slowly to CBN with oxidation. Thus a "
      "previous COA and a new COA for the same batch can show different numbers, and the two "
      "numbers can be correct. The material changed."),
    callout("note", "The factor for CBD is the same",
      p("The change from CBDA to CBD uses a ratio of molecular weights (also 0.877, because the "
        "acid has one CO₂ group more than the neutral cannabinoid). The formula is: total CBD = CBD "
        "+ 0.877 × CBDA. The total of each cannabinoid on a COA must agree with this formula. It is "
        "easy to calculate the total again when the result is important.")),
  ]})

# ---------------------------------------------------------------- 6. methods
SECTIONS.append({"id": "methods", "kicker": "HPLC and GC", "title": "HPLC and GC for potency testing",
  "blocks": [
    p("Two types of chromatography are the primary methods for potency testing. They do not measure "
      "the same molecules. <strong>HPLC</strong> (high-performance liquid chromatography) moves the "
      "extract through a column in a liquid at a temperature near room temperature. Different "
      "molecules move through the column at different speeds. Thus THCA and THC go to the detector "
      "at different times. They make two different peaks.</p><p><strong>GC</strong> (gas "
      "chromatography) must change the sample to a gas in the hot inlet at approximately 250 to 300 "
      "°C (482 to 572 °F). At this temperature, THCA decarboxylates immediately. The acid does not "
      "go to the detector as THCA" + _c("lazarjani2020-methods") + "."),
    figure(_FIGS["hplcgc"], 5,
      "The two methods of measurement. HPLC operates at a low temperature and gives two values, one "
      "for THCA and one for THC. Thus you calculate the total THC with the 0.877 factor. GC breaks "
      "the acid in the hot inlet. It gives one &lsquo;THC&rsquo; number. This number includes the "
      "THCA that changed to THC, but the number does not show this. Only a part of the THCA changes" +
      _c("dussy2005-thca") + "."),
    p("Only a part of the THCA changes to THC in the inlet, and this part is <em>not constant</em>. "
      "A test with THCA without other compounds found that decarboxylation in GC conditions changed "
      "only approximately 70% of the acid. The test also showed that the only accurate method is to "
      "measure THCA and THC as two values and to add the two values. A measurement after "
      "decarboxylation gives a minimum and not the correct value" + _c("dussy2005-thca") +
      ".</p><p>With GC, the laboratory cannot find the acids, unless it first does derivatization "
      "of the acids. Derivatization adds a chemical group to the acid. This group stays on the "
      "molecule at high temperature" + _c("lazarjani2020-methods") + "."),
    table(["", "HPLC-DAD", "GC-FID / GC-MS"], [
      ["Temperature of operation", "approximately 25 to 40 °C (77 to 104 °F) in the column", "approximately 250 to 300 °C (482 to 572 °F) in the inlet, and a hot column"],
      ["Different values for THCA and THC", "Yes, two peaks", "No, the acid decarboxylates in the inlet"],
      ["Total THC", "calculated value: THC + 0.877 × THCA", "one peak for THCA and THC (only a part of the THCA changes" + _c("dussy2005-thca") + ")"],
      ["Derivatization of the acids is necessary", "No", "Yes. Without it, the acids break" + _c("lazarjani2020-methods")],
      ["Typical use at this time", "potency (the usual method)", "terpenes and residual solvents, and potency in some legal markets"],
    ], cls="compact", caption="The two types of chromatography. Each type is correct, but the numbers are not the same and you cannot compare them directly."),
    callout("warn", "A flower COA without a THCA row",
      p("If a flower COA has no THCA row, tell the laboratory to give the method reference. The "
        "cause can be a GC method, and then the total is a minimum and not an accurate number. The "
        "cause can also be a report that does not show all the data. Each laboratory with "
        "accreditation shows the method reference on the COA.")),
  ]})

# ---------------------------------------------------------------- 7. units & basis
SECTIONS.append({"id": "units-basis", "kicker": "Units and water", "title": "Units and moisture basis",
  "blocks": [
    p("The units are easy. <strong>The number in mg/g is the number in % w/w with the decimal point "
      "moved by one position to the right.</strong> 1% w/w = 10 mg/g. For example, 22.14% = 221.4 "
      "mg/g.</p><p>Flower COAs usually give the result in %. COAs for oils and edible products "
      "frequently give the result in mg/g or in mg for each unit. The only problem is that you do "
      "not know the units."),
    p("The basis is the primary problem. Flower contains approximately 10 to 13% water after "
      "correct drying. The laboratory can calculate a potency percentage for the total mass with "
      "this water (<strong>as-received</strong> or &lsquo;as-is&rsquo;). The laboratory can also "
      "calculate it for the solids only (<strong>dry-weight</strong>). The flower and the chemistry "
      "are the same, but the two numbers are different:"),
    figure(_FIGS["basis"], 6,
      "The moisture basis. On an as-received basis, this flower has a result of 20.0% total THC. If "
      "you remove the 12% of water from the denominator, the same flower has a result of 22.7% on a "
      "dry-weight basis. The two numbers are correct. Each number is for a different basis."),
    table(["Moisture content", "As-received reading", "Dry-weight value"], [
      ["8%", "20.0%", "21.7%"],
      ["10%", "20.0%", "22.2%"],
      ["12%", "20.0%", "22.7%"],
      ["15%", "20.0%", "23.5%"],
    ], cls="compact", caption="Dry-weight % = as-received % ÷ (1 − moisture fraction). When the sample has more water, the difference is larger."),
    callout("warn", "Do not compare a dry-weight value with an as-received value",
      p("Examine the basis row on each COA before you compare two values. If the two COAs do not "
        "have the same basis, change one value to the other basis. Then compare the values. A "
        "dry-weight value of 22% and an as-received value of 20% from a different grower have "
        "different denominators. Tests with many laboratories show that laboratories give values "
        "with important differences, also for the moisture measurement" + _c("nist-cannaqap2") +
        ". Thus a small difference of the numbers on two COAs is noise.")),
  ]})

# ---------------------------------------------------------------- 8. sampling
SECTIONS.append({"id": "sampling", "kicker": "Sampling", "title": "Sampling and the accuracy of the result for the batch",
  "blocks": [
    p("The instrument can measure only the sample that the sampling procedure gives. A person does "
      "the sampling before the sample goes to the laboratory.</p><p>A batch can be 12 kg (26.5 lb). "
      "The composite sample is some tens of grams. The part that the laboratory extracts is "
      "approximately <strong>0.5 to 1 g (0.02 to 0.04 oz)</strong>. This one gram must show the "
      "batch. Thus the guidance of the pharmacopoeia identifies the sampling procedure as a quality "
      "attribute and not only as records" + _c("sarma2020-usp") + "."),
    figure(_FIGS["sampling"], 7,
      "The sampling steps. A person collects small samples from different containers and positions "
      "and puts them in one composite sample. The laboratory mixes the composite sample and gets a "
      "smaller part for the test. At each step, the number can become different from the correct "
      "value for the batch."),
    p("Sampling of cannabis is not easy because the analytes are in the trichomes. The quantity of "
      "trichomes is not the same in all parts of the plant. Top colas with more light have a higher "
      "potency than buds at the bottom in the shade. Resin falls from small buds when a person "
      "touches them. In ground material, the kief falls to the bottom.</p><p>A sample from only the "
      "best top buds is not a batch sample. It shows only the best part of the batch."),
    steps([
      ("Set the limits of the batch first", "A batch has one cultivar, one room, one harvest, and one "
       "procedure. If the batch is not the same in all parts, no sampling procedure can correct "
       "this."),
      ("Collect many small samples and not a grab sample", "Collect many small samples from different containers, "
       "positions, and depths. Collect also from the middle and from the bottom. Many small samples "
       "are better than one large quantity from one position."),
      ("Make a composite sample and record", "Make a composite sample from the small samples. Record the person "
       "who collected each small sample, the position, and the time. This step starts the chain of "
       "custody."),
      ("Mix before you divide the sample", "Grind the sample. Then mix the sample. Do these steps before "
       "you remove a part of it. For potency, the laboratory grinds and mixes the part again."),
      ("Keep a second sample", "Divide the sample into two parts. Keep one part in storage. If you "
       "think that a number is incorrect, this part is the only sample that you can measure again."),
    ]),
    callout("warn", "Do not select only the best buds",
      p("Do not send samples from only the top colas. These samples make the numbers on the COA and "
        "in your production data too high. They also make the buyer think that the batch has a "
        "higher quality.</p><p>A person will smoke the batch at some time. This person accepted the "
        "number. An audit can examine your sampling. Collect each sample for this audit. In systems "
        "for medicinal cannabis, an audit will examine your sampling.")),
    p("Correct sampling also gives a variance that is not zero. When one laboratory measures two "
      "composite samples from one batch, the THC values frequently have a difference of "
      "approximately one percentage point. A difference of one to two percentage points is noise. "
      "It is not information."),
  ]})

# ---------------------------------------------------------------- 9. microbial
SECTIONS.append({"id": "microbial", "kicker": "Microbes", "title": "Test methods for microbes",
  "blocks": [
    p("A test for microbes measures two types of item. The first type is <em>the number of "
      "microbes</em> on the sample. Counts measure this number. The counts are "
      "<strong>TAMC</strong> (total aerobic microbial count), <strong>TYM</strong> or TYMC (total "
      "yeast and mold count), and the count of bile-tolerant Gram-negative bacteria.</p><p>The "
      "second type is <em>a dangerous microbe</em> on the sample. A test with a yes or no result "
      "measures this type for specified organisms. The organisms are <em>Salmonella</em>, <em>E. "
      "coli</em> that are pathogens, and the four <em>Aspergillus</em> species that are pathogens "
      "in products for inhalation."),
    defterm("CFU (colony-forming unit)", "One viable organism, or one group of viable organisms, "
            "that makes a colony on a culture plate. You can count the colony. The plate results "
            "are in CFU for each gram."),
    defterm("qPCR", "Quantitative polymerase chain reaction. The method makes a very large number "
            "of copies of a target DNA sequence, until the quantity is sufficient to find and "
            "count. The method makes copies of the target sequence also when a kill step killed the "
            "organism. The method is fast (hours) and it finds only the target species. But the DNA "
            "from killed organisms is a problem after kill steps."),
    table(["Test", "Counted item", "Usual type of limit", "Information"], [
      ["TAMC", "aerobic bacteria (CFU/g)", "approximately 10⁵ CFU/g. The value is different in different legal markets" + _c("jameson2022-stateregs"), "indicator of bioburden"],
      ["TYM / TYMC", "yeast and mold (CFU/g)", "approximately 10⁴ CFU/g. Persons do not agree about this limit", "Flower usually has microbes on the surface"],
      ["Bile-tolerant Gram-negative bacteria", "bacteria from the gut", "approximately 10³ CFU/g", "indicator of hygiene"],
      ["Specified pathogens", "Salmonella, shiga-toxin E. coli", "not found in 1 g (0.035 oz)", "The result is only satisfactory or unsatisfactory"],
      ["Aspergillus (species that are pathogens)", "A. fumigatus, flavus, niger, terreus", "not found in 1 g (0.035 oz)", "usually enrichment + qPCR"],
    ], cls="compact", caption="The panel for microbes. The limits are different in different legal markets, but the types of test are the same" + _c("jameson2022-stateregs") + "."),
    p("Plates and qPCR can give different results for the same sample. A test with metagenomic "
      "sequencing showed that the culture medium selects the organisms. The test sequenced the "
      "organisms that became colonies in standard culture tests for yeast and mold of cannabis. The "
      "colonies on the plates included bacteria. The plates did not show a sufficient quantity of "
      "the fungi that make toxins and that were on the flower. In some tests, the plates can find "
      "none of the organisms that are dangerous for patients" + _c("mckernan2016-tym") +
      ".</p><p>qPCR also counts DNA from killed cells. Thus a batch that had a remediation with "
      "heat or irradiation can have an unsatisfactory result with qPCR and a satisfactory result "
      "with plates."),
    table(["", "Culture plates", "qPCR"], [
      ["Item measured", "organisms that become colonies on that medium at that temperature", "copies of target DNA"],
      ["Time", "3–7 days", "hours"],
      ["Counts killed organisms", "no", "yes, the DNA stays after kill steps"],
      ["Species identification", "not easy without more tests", "The primers identify the species"],
      ["Typical problem", "The target organisms do not become colonies, and other organisms become colonies" + _c("mckernan2016-tym"), "unsatisfactory results that are incorrect because of DNA from killed organisms, and a primer that does not agree with the target"],
    ], cls="compact", caption="The same batch can have a satisfactory result with one method and an unsatisfactory result with the other method. Always read the method row."),
    callout("danger", "The limit for Aspergillus is found or not found, and not a number of organisms",
      p("<em>Aspergillus</em> in a product for inhalation can cause invasive aspergillosis in "
        "patients with a weak immune system. These patients are the persons that use medicinal "
        "cannabis. For a patient with a transplant, a satisfactory dose of <em>Aspergillus</em> by "
        "inhalation is almost zero. Thus a limit with a number of organisms is not correct for this "
        "organism. The specification is: no organism in 1 g (0.035 oz).")),
  ]})

# ---------------------------------------------------------------- 10. metals
SECTIONS.append({"id": "metals", "kicker": "Heavy metals", "title": "Heavy-metal testing by ICP-MS",
  "blocks": [
    p("Cannabis has a high uptake of metals. Growers use hemp for the remediation of soil because "
      "of the same trait. The trait also causes the uptake of cadmium and lead from your substrate, "
      "fertilizer, and water. The plant keeps them in the tissue.</p><p>The panel for metals nearly "
      "always has <strong>four metals</strong>: arsenic, cadmium, lead, and mercury. Some systems "
      "use a test for a larger list of elements" + _c("nist-cannaqap2") + "."),
    table(["Metal", "Typical sources in the flower", "Risk"], [
      ["Arsenic (As)", "groundwater, some amendments from rock", "carcinogen"],
      ["Cadmium (Cd)", "phosphate fertilizers, substrate with contamination", "The plant absorbs it easily. It collects in the kidneys."],
      ["Lead (Pb)", "dust, contact with soil, solder and pipes that are not new, materials with contamination", "neurotoxin. No value of exposure is safe"],
      ["Mercury (Hg)", "not frequent. Water contamination or industrial contamination", "neurotoxin"],
    ], cls="compact", caption="The four metals. The limits are different in different legal markets. The limits are lower for products for inhalation than for oral products" + _c("jameson2022-stateregs") + "."),
    p("The instrument is <strong>ICP-MS</strong> (inductively coupled plasma mass spectrometry). "
      "The laboratory mixes the sample with hot acid until only elements in solution stay. Then the "
      "laboratory puts a spray of the solution into an argon plasma.</p><p>The temperature of the "
      "plasma is thousands of degrees. The instrument finds the ions of each element from their "
      "mass and counts them. The instrument is very sensitive, in the range of ppb. Thus the LOQs "
      "for metals are, for example, 0.01 µg/g."),
    callout("tip", "Control your materials to control metals",
      p("Flower has an unsatisfactory result for metals because a material supplied the metals. "
        "Collect the COAs for each lot of fertilizer and substrate. Do a test of the source water. "
        "Then you can find the cause of an unsatisfactory result for metals in your records. The "
        "limits for inhalation are very low. Thus one lot of a material with contamination can "
        "cause an unsatisfactory result for the batch.")),
  ]})

# ---------------------------------------------------------------- 11. pesticides
SECTIONS.append({"id": "pesticides", "kicker": "Pesticides", "title": "Pesticide panels and their limits",
  "blocks": [
    p("A test for pesticides is a <em>panel</em>. A panel is a specified list of compounds, and the "
      "laboratory compares each compound with an action limit. A satisfactory result shows that the "
      "laboratory found no compound <em>on this list</em> in a quantity more than <em>these "
      "limits</em>. It does not show that the product has no pesticide. It gives no information "
      "about compounds that are not on the panel.</p><p>The panels are very different in different "
      "legal markets. A survey of the regulations in the states of the US found 551 different "
      "pesticides with a limit in some state. The action limits for the same compound change by a "
      "maximum of four orders of magnitude from one state to a different state" +
      _c("jameson2022-stateregs") + "."),
    ul(["<strong>A full panel uses two instruments.</strong> LC-MS/MS finds most residues of new "
        "pesticides. GC-MS/MS finds the volatile compounds and the halogenated compounds. A "
        "laboratory with a large panel uses the two instruments.",
        "<strong>Inhalation changes the toxicology.</strong> Residues in a quantity that is "
        "satisfactory on lettuce can break and make more dangerous compounds when a person smokes "
        "them. Reports show that some fungicides release hydrogen cyanide when they burn. Thus the "
        "limits for cannabis are frequently much lower than the limits for food.",
        "<strong>Previous results show the risk.</strong> Before regulation, tests of concentrates "
        "in California found pesticides in approximately one-third of the samples" +
        _c("raber2015-dabs") + ".",
        "<strong>Drift and carryover are important.</strong> You can have an unsatisfactory result "
        "for a panel when you do not apply pesticide. Agriculture near your facility, used "
        "equipment with contamination, or a trim room that is not clean can put residues on the "
        "flower."]),
    callout("note", "Reading a pesticide section",
      p("A pesticide section has these items: the panel size (the number of analytes), the action "
        "limits and their source, the LOQ for each analyte, and the method (LC-MS/MS, GC-MS/MS, or "
        "the two). A row with only &lsquo;Pesticides: PASS&rsquo; and none of this information is "
        "not a result.")),
  ]})

# ---------------------------------------------------------------- 12. solvents & mycotoxins
SECTIONS.append({"id": "solvents-myco", "kicker": "Solvents · mycotoxins", "title": "Tests for residual solvents and mycotoxins",
  "blocks": [
    p("<strong>Residual solvents</strong> are in extracts. A solvent removes the resin from the "
      "plant. The solvent can be butane, propane, ethanol, or CO₂ and, in a last step, ethanol. A "
      "small quantity of the solvent can stay in the extract, and headspace GC measures it in the "
      "product.</p><p>The limits are different for each solvent. They agree approximately with the "
      "types of solvent for pharmaceutical products. The limit is almost zero for solvents with a "
      "very high toxicity (benzene and toluene). Producers do not add them, but they can occur as "
      "impurities in gas with a low price. The limits are higher for the usual solvents of the "
      "procedure."),
    p("A test for solvents is also necessary for a <em>solventless</em> hash or rosin. There are "
      "three causes. First, in most legal markets the type of the product causes the test, for all "
      "procedures. Second, the test is the only method to <em>make sure</em> that the solventless "
      "claim is correct, and not to accept it without a test. Third, contamination can occur "
      "without an extraction step. Cleaning agents, fuels, and gases from materials in storage can "
      "supply volatile compounds.</p><p>A satisfactory result for the solvent panel on rosin shows, "
      "at a low cost, that your marketing claim is correct. First tests of concentrates found "
      "residual solvents in approximately 30% of the samples. Thus buyers started to examine this "
      "result" + _c("raber2015-dabs") + "."),
    p("<strong>Mycotoxins</strong> are chemical compounds with toxicity that mold makes. They are "
      "the aflatoxins B1, B2, G1, and G2 (from <em>Aspergillus flavus</em> and related species) and "
      "ochratoxin A. LC-MS/MS measures them at limits in the range of ppb" + _c("jameson2022-stateregs") +
      ". Two facts make mycotoxins a different row on the COA and not a footnote to the section on "
      "microbes:"),
    ul(["<strong>The toxins stay after a kill step.</strong> Kill steps (heat, irradiation, and "
        "ozone) can decrease the TYM count a lot, but the toxins do not change. A batch can have a "
        "satisfactory result for microbes and an unsatisfactory result for mycotoxins. This occurs "
        "frequently in a product after remediation.",
        "<strong>They are very dangerous at very low doses.</strong> Aflatoxin B1 is one of the "
        "strongest natural carcinogens that persons know. Thus the limits are in the range of µg/kg "
        "(ppb) in systems for medicinal cannabis" + _c("tga-tgo93") + "."]),
    callout("warn", "Remediation does not remove mycotoxins",
      p("If a batch had a remediation, examine the mycotoxin row most carefully. Flower after "
        "irradiation or heat treatment can have a satisfactory result for plate counts. But the "
        "flower continues to have the toxins that the mold made. Its DNA from killed organisms can "
        "also give an unsatisfactory result with qPCR.")),
  ]})

# ---------------------------------------------------------------- 13. water activity
SECTIONS.append({"id": "water-activity", "kicker": "Water in two numbers", "title": "Water activity and moisture content",
  "blocks": [
    p("A flower COA gives two numbers for water. The two numbers give different information. "
      "<strong>Moisture content</strong> (%) is <em>the quantity</em> of water in the sample. It is "
      "the mass of the water divided by the total mass. <strong>Water activity</strong> "
      "(a<sub>w</sub>, scale 0 to 1) is <em>how available</em> that water is to "
      "microbes.</p><p>Water activity is the equilibrium relative humidity that the sample makes in "
      "a closed space. Two samples can have the same mass of water, but a different water activity. "
      "When the sample holds the water tightly, the water is not available to microbes. Mold can "
      "increase only with available water, and not only with a large quantity of water. Thus "
      "a<sub>w</sub> is the important number for microbes. The pharmacopoeia for cannabis in "
      "storage has a specification of a maximum of 0.65 for water activity" + _c("sarma2020-usp") +
      "."),
    figure(L.zones("Water activity: where mold can and cannot increase", 0.30, 0.90,
        [(0.30, 0.55, L.AMBL, "too dry: breaks easily"),
         (0.55, 0.65, L.GL, "target range"),
         (0.65, 0.70, L.AMBL, "risk"),
         (0.70, 0.90, L.REDL, "mold increases")],
        unit=" aw",
        note="Less than 0.55: lower quality (trichomes break, smoke irritation). 0.55 to 0.65: usual specification. More than approximately 0.65: xerotolerant molds increase."), 8,
      "The scale of water activity for flower in storage. The maximum of 0.65 is the limit that "
      "most specifications use" + _c("sarma2020-usp") + ". The lower value is about the quality of "
      "the product and not about safety."),
    table(["", "Moisture content", "Water activity (a<sub>w</sub>)"], [
      ["Item measured", "the quantity of water (% of mass)", "how available the water is (0 to 1)"],
      ["Instrument", "loss-on-drying balance", "a<sub>w</sub> meter with a chilled mirror or a capacitance sensor"],
      ["Effect on microbes", "The relation to microbes changes with how tightly the sample holds the water", "The thresholds for growth are a<sub>w</sub> thresholds"],
      ["Typical specification for flower", "approximately 10 to 13%", "0.55–0.65"],
    ], cls="compact", caption="The same water, two numbers. A batch can have a usual moisture content and a water activity that is not safe. The opposite is also possible. The sorption curve is different for different cultivars and trims."),
    p("In operation, dry the flower. Then do the curing until the water activity agrees with the "
      "target. Accept the moisture content that the drying gives. The two numbers on the COA also "
      "let you make sure that they agree. For example, a<sub>w</sub> 0.75 with 11% moisture is not "
      "usual for a sample. Find the cause of this result."),
  ]})

# ---------------------------------------------------------------- 14. inflation
SECTIONS.append({"id": "inflation", "kicker": "The problem", "title": "COA values that are too high: data and warning signs",
  "blocks": [
    p("When one number sets the price, there is pressure on the number. Tests with peer review "
      "record this problem in legal markets for cannabis. Each grower that selects a laboratory "
      "must know this fully."),
    figure(L.hbars("THC that does not agree with the label",
        [("2023 flower (CO)", 70), ("2024 flower (3 states)", 70),
         ("2025 flower (CO)", 43), ("2025 concentrates (CO)", 4)],
        unit="%",
        note="Fraction of products with THC that is not the label value: more than 15% less than the label (2023), not in the range of ±20% (2024), not in the range of ±15% (2025)."), 9,
      "The accuracy of labels in tests with peer review in the retail market. In one test, the "
      "measured value of 70% of the Colorado flower samples was more than 15% less than the label" +
      _c("schwabe2023-inflated") + ". In an audit of 107 samples in three states, 70% of the values "
      "were not in the range of ±20% of the label value" + _c("geweda2024-audit") +
      ". In 2025, 43% of the flower samples but only 4% of the concentrates were not in the range "
      "of ±15%" + _c("giordano2025-accuracy") + ". The accuracy problem is in flower, because with "
      "flower a person can change the result most easily with the sampling."),
    p("The data of states show the cause. The potency values for chemotype-I flower from the six "
      "largest laboratories in Washington show a <em>systematic</em> difference. The median total "
      "THC was 17.7% at the laboratory with the lowest values and 23.2% at the laboratory with the "
      "highest values. This difference of 5.5 percentage points stayed when the cultivar and the "
      "producer were the same" + _c("jikomes2018-labs") + ".</p><p>Values a small quantity more "
      "than the price threshold of 20% are also too frequent in the reports. At 20%, the frequency "
      "of products increases suddenly, by 43% in Nevada and by 17% in Washington. At some "
      "laboratories, the frequency increases more. At the two laboratories that the authority "
      "suspended subsequently, the frequency increases by 47%. At the largest laboratory of the "
      "state, the frequency increases by 1%" + _c("zoorob2021-bunching") + ". The value of 20% is a "
      "price threshold and has no cause in biology."),
    figure(L.bars("The 20% threshold: the frequency of products increases suddenly",
        [("less than 20%", 100), ("more than 20% (WA)", 117), ("more than 20% (NV)", 143), ("suspended labs", 147)],
        unit="",
        note="Relative frequency of flower products in the bin more than 20% THC compared with the bin less than 20% (= 100). The cause is not biology.",
        maxv=160), 10,
      "The values in the reports change at 20% THC" + _c("zoorob2021-bunching") +
      ". In biology, a distribution of values has no sudden change at 20%. The frequency of "
      "products increases most at laboratories that the authority suspended subsequently. These "
      "data are a sign that the values are too high."),
    p("<strong>Selection of a laboratory for its high numbers</strong> causes this problem. A "
      "grower divides one batch into three parts and sends the parts to three laboratories. The "
      "grower keeps the highest number. Then the grower gives the work to that laboratory. The "
      "laboratories know this. A laboratory that gives correct values gets less work than a "
      "laboratory that gives high values.</p><p>The methods to make the values too high range from "
      "small changes (a calibration bias for flower only, a rounding to a higher value, and "
      "sampling with a large tolerance) to fraud. In 2024, seven of the eleven laboratories with "
      "accreditation in Oregon had an enforcement action from the authority of the state. The cause "
      "was THC results that were too high. The enforcement action included the claim that personnel "
      "at three laboratories added kief to samples from clients before the test" + _c("hs2024-oregon") +
      ". Enforcement actions about licenses and lawsuits by other laboratories followed in "
      "California and Massachusetts. The causes were potency values that were too high and products "
      "with contamination that had a satisfactory result."),
    callout("evidence", "Variance and fraud: the difference",
      p("The results of different laboratories have a usual variance, also for good laboratories. "
        "Many laboratories measure the same sample in special tests, because it is not easy to "
        "compare cannabis measurements" + _c("nist-cannaqap2") + ". But usual variance gives values "
        "<em>higher and lower</em> than the correct value.</p><p>Values that are too high are "
        "<em>higher only</em>. They always give a better result. If the numbers of a laboratory are "
        "always the best in the area, the cause is not random. The high numbers are a product that "
        "the laboratory supplies.")),
    p("We recommend that a grower does these steps. Select a laboratory because its accreditation "
      "includes your type of test and its COA shows the method.</p><p>Do not select a laboratory "
      "because of its averages. At intervals, divide a sample into two parts. Send the parts to two "
      "laboratories. The usual variation is approximately 1 to 2 percentage points. Keep samples in "
      "storage. A person at a laboratory who <em>tells you the numbers before the test</em> is a "
      "risk for your license.</p><p>In systems for medicinal cannabis with GMP, the incentive is "
      "the opposite. The laboratory gives data for the decision to release the batch and not for "
      "marketing. Thus the numbers are more stable in these systems" + _c("tga-tgo93") +
      _c("nz-mcs-mqs") + "."),
  ]})

# ---------------------------------------------------------------- 15. one number
SECTIONS.append({"id": "single-number", "kicker": "Use of results", "title": "Limits of one result",
  "blocks": [
    p("A COA gives information that you can use in its limits. One COA <em>can</em> show three "
      "items. The first item is the potency group of the sample (a batch with 15% and a batch with "
      "25% are very different).</p><p>The second item is the result of the sample for the panel "
      "(satisfactory or unsatisfactory). The third item is a trend that you can use to control your "
      "crop. For this trend, many batches from your room are necessary, with the same sampling "
      "procedure each time. One COA <em>cannot</em> show these items:"),
    ul(["<strong>The number for your room.</strong> The COA gives information about the sample. The "
        "batch has the same number only if your sampling is accurate.",
        "<strong>Differences of one or two percentage points.</strong> The variation of the "
        "sampling and the variation of the results from different laboratories are larger than "
        "these differences. In a test, the systematic difference from one laboratory to a different "
        "laboratory was 5.5 percentage points, with no other cause" + _c("jikomes2018-labs") +
        ".",
        "<strong>Quality or effect.</strong> The THC percentage has a weak correlation with the "
        "effect of a product when a person uses it. Terpenes, minor cannabinoids, curing, and "
        "freshness cause most of the effect. A high number on the COA is not the correct target.",
        "<strong>The next batch.</strong> A COA is a record of one batch. It does not show the "
        "result for the next batch. The genetics, the environment, and the procedure will change "
        "the next batch."]),
    h(3, "When the number is not usual"),
    table(["Sign", "Possible causes", "Items to examine"], [
      ["THC increased by 3 to 4 percentage points for the same cultivar", "A drift in the sampling (top colas), a change of the basis, a different laboratory, or a different method", "The person who collected the sample. The basis and moisture rows. The laboratory and method IDs on the two COAs."],
      ["Total THC ≠ THC + 0.877 × THCA", "An error in the report, a different formula for the total, or a total from GC", "Calculate again. Tell the laboratory to give the formula and the method that it used."],
      ["Flower with a total THC of 35% or more", "More than the range of values that nearly all cultivars can make. A sample with kief enrichment, or values that are too high", "Divide a sample. Measure it again at an external laboratory. Examine the sample for kief enrichment."],
      ["An unsatisfactory TYM result, then a satisfactory result in a second test", "A different method (plate or qPCR), a different part of the sample, or a remediation between the tests", "The method rows on the two COAs. If the batch had a treatment between the tests."],
      ["An unsatisfactory result for metals with no cause that you know", "A new lot of fertilizer or substrate, a change of the water, contamination of the equipment", "The COAs and lot numbers of the fertilizer and the substrate. A test of the source water."],
      ["The moisture content is 6%, but the flower is usual when you touch it", "The sample became dry when it went to the laboratory, or it stayed for some time before the test", "The water activity at packaging. The number of days between sampling and testing."],
      ["CBD is in a THC cultivar", "Genetics with an incorrect label, or an incorrect identification of the peak at the laboratory", "Make sure that the cultivar is correct. Tell the laboratory to make sure that the identification of the peak is correct."],
    ], cls="compact", caption="This table helps you to find the cause. Read the information about the sample before you think that the chemistry is incorrect. Most unusual numbers are from the sampling, the basis, or the method, and not from the instrument."),
    h(3, "Signs of a problem with a COA"),
    grid([
      card("No accreditation number", p("A PDF is easy to make. If the public register does not "
           "show the laboratory and its accreditation, the document is a claim and not a "
           "certificate."), tag="identification"),
      card("No LOQ column", p("&lsquo;ND&rsquo; without a limit gives no information that you can "
           "use. You do not know the <em>limit</em> for the result. A good laboratory always shows "
           "the limit."), tag="report"),
      card("Only &lsquo;THC&rsquo;, no THCA row", p("The cause is a GC method (the total is a "
           "minimum and not accurate) or a report with data that is not sufficient. In the two "
           "causes, tell the laboratory to give the method reference."), tag="method"),
      card("&lsquo;Client-submitted&rsquo; used as a batch result", p("The laboratory measured a bag that a person "
           "filled. To use this measurement as a batch result is a frequent method of fraud."), tag="sampling"),
      card("The laboratory with the best numbers in the area", p("The laboratory always gives numbers that are 2 to 3 percentage "
           "points higher than all other laboratories in the area. Thus the high numbers are a "
           "product that the laboratory supplies and not a result of chemistry" +
           _c("zoorob2021-bunching") + "."), tag="incentives"),
      card("New report versions with higher numbers", p("A laboratory can make a new version of a COA. If "
           "each new version of a COA only increases the THC value without a cause, do not use the "
           "laboratory."), tag="records"),
    ], cols=3),
    callout("key", "The primary fact",
      p("One COA is one measurement: one sample, one laboratory, and one day. The measurement gives "
        "information in these limits. Do not accept a laboratory with numbers that are always the "
        "highest in the area. The high numbers are a product that the laboratory supplies and not "
        "chemistry.")),
  ]})

# ---------------------------------------------------------------- 16. NZ/AU
SECTIONS.append({"id": "nz-au", "kicker": "Medicinal cannabis", "title": "Testing for release in NZ and Australia",
  "blocks": [
    p("In the systems of Australia and New Zealand for medicinal cannabis, the COA has a different "
      "function from a COA in the retail market. In Australia, a medicinal cannabis product without "
      "approval must agree with <strong>TGO 93</strong> (Therapeutic Goods (Standard for Medicinal "
      "Cannabis) Order 2017). The measured quantity of cannabinoids must be in the range of 90.0 to "
      "110.0% of the label claim. The limits for contaminants (for example aflatoxins and pesticide "
      "residues) apply. The authority can collect product and do a test on it at all times" +
      _c("tga-tgo93") + ".</p><p>In New Zealand, products must agree with the <strong>minimum "
      "quality standard</strong> in the Misuse of Drugs (Medicinal Cannabis) Regulations 2019. "
      "Facilities with a GMP certificate must do the critical tests. For the other tests, the "
      "authority accepts accreditation to ISO/IEC 17025" + _c("nz-mcs-mqs") + "."),
    p("The primary procedure is <strong>release testing</strong>. The laboratory does a test of the "
      "batch and compares the results with a registered specification. A qualified person examines "
      "all the data. Then this person releases the batch or does not release it. The COA is one "
      "source of data for a decision that is in a document. This person makes the decision, gives a "
      "signature, and has liability for it.</p><p>In the retail market, the COA has a primary task: "
      "marketing. Thus the record of values that are too high, in a previous section, is a result "
      "of the different incentive. The document is the same, but the incentive is the opposite."),
    ul(["A range of 90 to 110% of the label claim shows that a batch can be <em>unsatisfactory "
        "because the potency is too high</em>. The target is accuracy and not a high value" +
        _c("tga-tgo93") + ".",
        "The data on stability and the claims on shelf life use the same measurements. Subsequent "
        "measurements examine again the COA that releases the batch. Thus the first numbers must be "
        "accurate.",
        "Testing in GMP uses methods with validation, instruments with qualification, and audit "
        "trails. The laboratory shows the basis of each result in a system of documents. It does "
        "not give a result without data."]),
    callout("note", "This section is not legal advice",
      p("This section gives only the primary items of the systems and not the current data. The "
        "standards, the schedules, and the guidance change. For a person that operates with TGO 93 "
        "or the NZ system, the current documents of the authority are the source" + _c("tga-tgo93") +
        _c("nz-mcs-mqs") + ". The quality agreements of that person are also a source. A white "
        "paper is not a source.")),
    p("The primary fact is the same for growers in other legal markets. Use a testing procedure "
      "with the properties of release testing. The procedure has an SOP for sampling that does not "
      "change, and one laboratory with accreditation. It has samples that you keep, trend charts, "
      "and numbers with no incentive for a high value. When your procedure agrees more with release "
      "testing, your COAs have a higher value for you and for each auditor."),
  ]})
