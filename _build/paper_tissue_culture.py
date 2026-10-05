# -*- coding: utf-8 -*-
"""Paper: cannabis tissue culture (beginner). Rendered through the unified shell."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        stagecard, grid, card, chip, kv, steps, cite)
import figs as F
import figs_extra as FX

SLUG = "tissue-culture"
TITLE = "Tissue culture for clean cannabis genetics"
EYEBROW = "Basic · Tissue culture"
SUB = ("Tissue culture removes diseases that usual methods to clean a plant cannot remove. It makes "
       "a new plant from a very small piece of the tip of a shoot. When you read this guide, you "
       "will know how to do the full procedure. The procedure starts when you prepare the donor "
       "plant. It ends with a mother plant that can supply cuttings. A test shows that this mother "
       "plant has no disease.")
META = [("spark", "Basic"), ("image", "18 step photos"),
        ("quote", "11 sources"), ("clock", "~22 min to read")]
RELATED = ["mould-risk", "grow-room-systems", "gmp-hash-lab"]
REF_IDS = ["hlvd_threat2023", "hlvd_mgmt2025", "holmes2021", "mdpi2024_media",
           "hlvd_thermo2024", "page2019", "pmc9146626", "kurtz2022",
           "torkamaneh2024", "tis2022", "karger2019_cryo", "athena"]

_TITLE_LONG = "Tissue culture for clean cannabis genetics: a complete guide for growers who are new to the work"

def _cite_html(rid):
    n = REF_IDS.index(rid) + 1
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, n)
R = {rid: _cite_html(rid) for rid in REF_IDS}

HERO = """
<header class="hero"><div class="wrap">
  <div class="eyebrow">Plant Tissue Culture &middot; First-Timer's User Guide</div>
  <h1>Cleaning Up Cannabis Genetics with Tissue Culture</h1>
  <p class="sub">Take a tired, possibly diseased cannabis plant and grow a clean, vigorous,
  genetically identical mother from a speck of its tissue. Explained from absolute zero, with
  a benchtop Athena-style kit.</p>
  <div class="meta">
    <span class="chip">Assumes no prior lab experience</span>
    <span class="chip">Stage 0 &rarr; clean mother</span>
    <span class="chip">Built on 2019&ndash;2026 research</span>
    <span class="chip">Honest about what a kit can &amp; can't do</span>
  </div>
</div></header>
"""

# ============================================================ SECTIONS

SECTIONS = []

# ---- 1. Start here -------------------------------------------------------
SECTIONS.append({
  "id": "start", "kicker": "01: Read this first", "title": "Purpose and scope",
  "blocks": [
    lead("This guide shows you the full procedure, from the selection of a donor plant to a clean "
         "new mother plant. The new mother plant has roots, and it is in good condition after "
         "acclimatization. You will know the definition of plant tissue culture. You will know that "
         "cannabis growers use it to make their genetics clean. You will also know how to do all "
         "the steps of the procedure."),
    p("This guide is for a person who is <strong>new to laboratory work</strong>. The guide gives "
      "the definition of each term the first time that the term occurs. It gives all the necessary "
      "information. If the data are not sufficient, or if the manufacturer of a product does not "
      "give the information, the guide tells you clearly."),
    callout("key", "The primary fact",
      p("Tissue culture makes a new plant from a very small piece of the tip of a shoot. This tip "
        "is too new to contain most diseases. Thus the new plant is <em>clean</em>, also when the "
        "parent plant has a disease.")),
    h(3, "How to use this guide"),
    grid([
      card("If you want information", "Read sections 1&ndash;5. They give the information about the "
           "problem and a general view of the procedure. It is not necessary to get equipment for "
           "these sections.", tag="Read"),
      card("If you will start tissue culture", "Read all the sections. Sections 6&ndash;17 give the steps "
           "of the procedure in the correct sequence.", tag="Do it"),
      card("If you have a problem", "Go to section 19 (Troubleshooting) and to section 20. The "
           "second of these two sections gives accurate values for the success rates and the cost.", tag="Correct it"),
    ], cols=3),
    callout("warn", "The result of the first batch",
      p("Cannabis is a <strong>recalcitrant species</strong>: its tissue does not easily make a new "
        "plant in a vessel. In your first batch, contamination or browning can kill most of the "
        "cultures. This result is <em>usual</em>. It does not show an error in your work.</p><p>The "
        "best report from a laboratory shows that approximately 55% of the pieces stay in good "
        "condition. Other reports show that 90 to 95% of the pieces do not stay in good condition "
        "at the first stage. Use your first batch as a test of your method.")),
  ]})

# ---- 2. Plain English ---------------------------------------------------
SECTIONS.append({
  "id": "basics", "kicker": "02: The terms", "title": "The terms and facts of tissue culture",
  "blocks": [
    p("Tissue culture uses one fact about plants that animals do not have. Almost all the cells of "
      "a plant contain the full instructions to make a new plant."),
    callout("key", "Totipotency: a very small piece of tissue can make a new plant",
      p("Each cell in the plant contains a copy of all the instructions to make the plant. Most "
        "cells use only a part of the instructions. A root cell uses the instructions for roots, "
        "and a leaf cell uses the instructions for leaves.</p><p>Give a very small piece of the "
        "correct tissue the correct nutrients and signals. Then the cell can use all the "
        "instructions and make a new plant. This property is <strong>totipotency</strong>. You make "
        "a new copy of the plant, not a &lsquo;sample&rsquo;.")),
    p("The table below gives the necessary terms. It is not necessary to know all the terms at this "
      "time. This guide uses each term again in the next sections."),
    table(["Term", "Definition"], [
      ["<strong>Tissue culture (TC)</strong>", "The growth of plant cells, tissues or organs in a vessel without microbes, on a gel with nutrients and not in soil."],
      ["<strong>Micropropagation</strong>", "You use tissue culture to make <em>many</em> copies of a plant. The copies are the same as the first plant. In this guide, tissue culture and micropropagation are the same."],
      ["<strong>In vitro</strong>", "The Latin term for &lsquo;in glass&rsquo;. It is for all that occurs in the vessel. The opposite terms are <strong>ex vitro</strong> and <strong>in vivo</strong>. They are for all that occurs out of the vessel."],
      ["<strong>Explant</strong>", "The small piece of a plant that you cut from the plant and put in a vessel. This piece starts a culture."],
      ["<strong>Clone</strong>", "A copy of a plant with the same genetics. Each plant that you make from one mother plant, by tissue culture or by cuttings, is a clone."],
      ["<strong>Aseptic technique</strong>", "The method that prevents the entry of bacteria, fungi and yeast into your culture. This method has the largest effect on the result."],
      ["<strong>Medium (media)</strong>", "The material that gives nutrients to the culture. It is a gel of mineral salts, sugar, vitamins and hormones. A gelling agent makes the gel hard. &lsquo;Pouring media&rsquo; is the task to fill the vessels with the medium."],
      ["<strong>PGR (plant growth regulator)</strong>", "A plant hormone that you add to the medium to control growth. One type makes shoots. The other type makes roots. This guide also uses &lsquo;hormones&rsquo; as a name for PGRs."],
      ["<strong>Meristem</strong>", "The dome of cells at the tip of each shoot. The cells divide and stay new. This tissue has the smallest quantity of disease in the plant, and it is the primary tissue of this guide."],
      ["<strong>Node</strong>", "The point on a stem where a leaf and a bud attach. A <strong>nodal segment</strong> is a short piece of stem that contains one bud."],
      ["<strong>Subculture</strong>", "The task to move tissue to new medium. Do this task again after some weeks. Thus the cultures stay in good condition and make more shoots."],
      ["<strong>Contamination</strong>", "A microbe that goes into the vessel and increases in number faster than your plant. Almost always, the microbe kills that culture."],
      ["<strong>Indexing</strong>", "A laboratory test to make sure that a plant does not have a specified disease. An example is an RT-qPCR test for a viroid."],
    ]),
    callout("note", "The term &lsquo;cleaning up genetics&rsquo;",
      p("You do <strong>not</strong> change the DNA, and you do not make the DNA better. The "
        "cultivar stays the same cultivar. You remove the <em>diseases and pests</em> that the "
        "plant got during many years of cloning. Then the plant can have the performance of its "
        "initial genetics. The plant is in good condition again, and the genetics are not better.")),
  ]})

# ---- 3. Why -------------------------------------------------------------
SECTIONS.append({
  "id": "why", "kicker": "03: The problem", "title": "Hop latent viroid and clean-stock genetics",
  "blocks": [
    p("When you get cuttings from the same mother plant for many years, two problems occur. The "
      "first problem is <strong>diseases</strong> that you cannot see. They go from one cutting to "
      "the next cutting. The second problem is a slow increase of <strong>damage</strong>. At the "
      "start, the plant shows no problem, but then the yield decreases, the buds become smaller, "
      "and the aroma becomes weaker. In cannabis, the primary cause of these problems has a name."),
    defterm("Hop Latent Viroid (HpLVd or HLVd)",
      "A viroid is a loop of RNA that has only 256 nucleotides (the units of RNA). It is much "
      "smaller than a virus, and it has a smaller number of parts. It has no protein shell. Growers "
      "use the names <strong>&lsquo;dudding&rsquo;</strong> and &lsquo;duds&rsquo; for the disease "
      "that the viroid causes." + R["hlvd_threat2023"]),
    figure(F.fig_hplvd(), 1,
      "A clean plant and a &lsquo;dudded&rsquo; plant that contains Hop Latent Viroid. At the "
      "start, the infection frequently has no symptoms. Thus it moves to all the clones of a mother "
      "plant. The grower does not see it until the production decreases to a very low value."),
    h(3, "HpLVd: movement, cost and effect"),
    grid([
      card("It is frequent", "Reports of tests show very high rates of infection in facilities in California (approximately 90% in one large set of tests). Test results also show the viroid frequently in Canadian retail flower (approximately 40% in one test). Use these values as indications of a risk. They are not permanent values for all facilities. If you made clones for many years, it is possible that you have the infection." + R["hlvd_mgmt2025"], tag="Frequency"),
      card("It has a high cost", "In large outbreaks of &lsquo;duds&rsquo;, the quantity of cannabinoids in an infected plant can decrease by a maximum of approximately <strong>half</strong>. The quantities of terpenes and trichomes, and the yield, also decrease. The cost for growers is more than $10 million each year.", tag="Effect"),
      card("It is not easy to see", "It can stay in a plant for a long time with <strong>no symptoms</strong>. Thus &lsquo;latent&rsquo; is in the name of the viroid. When the plants show the symptoms of &lsquo;dud&rsquo;, the infection is usually in all the plants of the room.", tag="Latent"),
      card("It moves easily", "The viroid can stay on tools, hands, pots and benches. It can stay in sap for approximately one week and in dry tissue for approximately one month. A report of a 2025 test in North America gives a rate of seed transmission of up to 100%. The rate changes with the seed lot and with the method of the test. Thus do a test of each lot." + R["hlvd_mgmt2025"], tag="Seed risk"),
    ], cols=2),
    callout("warn", "A spray cannot remove a viroid infection",
      p("A spray cannot remove the viroid from a plant that has the infection. The viroid is "
        "<em>in</em> the cells and in the tissue through which sap flows. The only method that "
        "gives a good result is to make a new plant. Make the new plant from a piece of tissue that "
        "does not contain the viroid. Meristem tissue culture does this, and it is the primary part "
        "of this guide.")),
    callout("note", "Other problems that tissue culture removes",
      p("Most reports are about HpLVd. Meristem work and indexing are primarily for systemic agents "
        "(viroids and viruses). Sterilization of the surface removes many microbes and other "
        "organisms from the surface. But endophytes can occur in the culture after the "
        "sterilization, and mites stay a problem for IPM. At the start, the cells are clean. Thus "
        "it is not necessary to remove the same problems again and again.")),
  ]})

# ---- 4. Big picture -----------------------------------------------------
SECTIONS.append({
  "id": "overview", "kicker": "04: The procedure", "title": "Tissue culture procedure",
  "blocks": [
    p("Each procedure for plant tissue culture has the same five stages, for orchids, bananas and "
      "cannabis. The first record of these stages is from Murashige. Each step in the next sections "
      "is part of one of the stages."),
    figure(F.fig_5stages(), 2,
      "The five stages of micropropagation. In Stage 0, you prepare the donor plant. Stages "
      "I&ndash;IV occur in the vessel and near the vessel. The &lsquo;cleanup&rsquo; (meristem "
      "work) and the &lsquo;proof&rsquo; (disease testing) are part of the first stages."),
    p("This guide divides the five stages into the steps that you will do. The guide also includes "
      "two more steps for cannabis. The first is the <strong>meristem cleanup</strong>, which "
      "removes the viroid. The second is the <strong>indexing</strong> test, which makes sure that "
      "the cleanup removed the viroid."),
    figure(F.fig_pipeline(), 3,
      "The full procedure of this guide, step by step, with approximate periods. The purple step "
      "(meristem cleanup) and the blue step (indexing, or disease testing) are the two steps that "
      "change usual cloning into a cleanup of the genetics. In your work, a period can start before "
      "the previous period stops."),
    h(3, "Time for the procedure"),
    p("The procedure is longer than you want. It is important to know this before you start. There "
      "are two correct times, for two different results."),
    figure(F.fig_timeline(), 4,
      "The approximate times for a careful person who is new to the work. For a usual clone with "
      "roots, after acclimatization, the time is approximately 2.5&ndash;3.5 months. For a "
      "<em>mother plant that tests show has no disease</em>, the time is 5&ndash;6 months or more. "
      "This time includes the slow growth of the meristem into a shoot and the laboratory tests "
      "that you do more than one time."),
    callout("key", "The two times for the procedure",
      ul([
        "<strong>A clean clone with roots, after acclimatization</strong> (without a laboratory test for disease): approximately <strong>10&ndash;15 weeks</strong>.",
        "<strong>A mother plant that has no HpLVd, as tests show</strong> (meristem culture and RT-qPCR tests): approximately <strong>5&ndash;6 months or more</strong>. The procedure is much longer than two weeks.",
      ], "tight")),
  ]})

# ---- 5. The science of clean -------------------------------------------
SECTIONS.append({
  "id": "science", "kicker": "05: How the meristem stays clean", "title": "Meristem culture to remove pathogens",
  "blocks": [
    p("Viroids and viruses move in a plant through its <strong>vascular system</strong>. The "
      "vascular system is the internal tissue (phloem) through which sap flows. From there, the "
      "viroids and viruses move from cell to cell. But the <strong>meristem</strong> is at the tip "
      "of each shoot. The meristem is a dome of new cells that divide very quickly. It is <em>too "
      "new to have a vascular system</em>."),
    figure(F.fig_meristem(), 5,
      "The inner part of a shoot tip. The viroid moves up in the red vascular tissue. The viroid "
      "cannot go into the green meristem dome. There is no vascular tissue in the dome, and the "
      "cells of the dome divide faster than the viroid can move. If you cut only this dome, "
      "0.2&ndash;0.5&nbsp;mm (0.008&ndash;0.020&nbsp;in), the disease is usually not in the piece."),
    callout("key", "Two causes that keep the dome clean",
      ol([
        "<strong>No vascular tissue.</strong> The viroid moves in vascular tissue, and the dome does not have vascular tissue. Thus the pathogen cannot go into the dome.",
        "<strong>The cells divide faster than the viroid.</strong> Meristem cells divide faster than the viroid can make copies and move forward. Thus the newest cells of the tip stay in front of the infection.",
      ], "tight")),
    p("The piece that you cut gives one of two results: a clone of the plant only, or a clean "
      "plant. When the piece is smaller and newer, it has less disease. But it is also not easy to "
      "keep the piece in good condition."),
    figure(FX.fig_explant(), 6,
      "The three alternatives for the explant. A nodal segment is easy, but it keeps the disease. A "
      "meristem dome is the only alternative that removes Hop Latent Viroid with a good result. But "
      "the dissection is of a piece that is smaller than one millimeter. You do it with a "
      "microscope, and many explants do not stay in good condition. Most growers who are new to the "
      "work start with nodes to know the method. Then they use meristems for the cleanup."),
    callout("warn", "A plant without the viroid is not resistant to the viroid",
      p("Meristem culture can make a plant <strong>without</strong> the viroid. It does "
        "<strong>not</strong> make a plant that is <strong>resistant</strong> to the viroid. A "
        "dirty blade or hand can infect a clean plant again when it touches the plant. Clean stock "
        "stays clean after the cleanup only if you always obey the hygiene procedures. A plant is "
        "clean only when a laboratory test shows that the plant has no viroid (section 13).")),
  ]})

# ---- 6. Lab & kit -------------------------------------------------------
SECTIONS.append({
  "id": "lab", "kicker": "06: Your setup", "title": "Laboratory setup and equipment",
  "blocks": [
    p("It is not necessary to have a special laboratory. Three items are necessary. The first is a "
      "small space of clean air for your work. The second is a method to sterilize objects with "
      "heat. The third is a warm area with light for the vessels. This section gives all the "
      "information."),
    h(3, "Clean air: still-air box or flow hood"),
    grid([
      card("Still-Air Box (SAB)", p("A still-air box is a transparent plastic container on its "
        "side, with two holes for your arms in the front. You clean the inner surface of the "
        "container with alcohol. When all the fans and the AC are off, the air in the box does not "
        "move. Thus spores cannot go onto your open vessels. <strong>The cost is low or zero, and "
        "we recommend that you start with this box.</strong> The box has a small space, and the "
        "movement of your arms moves the air."), tag="Basic"),
      card("Laminar Flow Hood (LFH)", p("A laminar flow hood is an electric cabinet. A fan blows "
        "air through a HEPA filter (the filter removes more than 99% of the particles). The air "
        "flows in one smooth layer across your work and removes contaminants all the time. The hood "
        "has a larger space, the work is faster, and an error has less effect. <strong>The hood is "
        "a better alternative, but it is not necessary.</strong> The Athena kit includes a hood of "
        "this type."), tag="Alternative"),
    ], cols=2),
    callout("note", "A biosafety cabinet is NOT necessary",
      p("A biosafety cabinet gives the <em>operator</em> protection against dangerous microbes. In "
        "plant tissue culture, you must give protection only to the <em>plant</em>. Thus a flow "
        "hood or a still-air box is the correct tool. A biosafety cabinet has a high cost and is "
        "more than necessary.")),
    figure(F.fig_lab(), 7,
      "The inner part of a still-air box or flow hood, with the items in the correct positions for "
      "work. The middle is the clean area. In this area, you open the vessels and you cut. On the "
      "left, you sterilize the tools again. On the right are the new media and the explants. You "
      "put the waste in an area for waste. Do not put your hands above open vessels."),
    h(3, "The Athena Culture Kit: contents and limits"),
    p("Athena Ag is the manufacturer of the &lsquo;Pro Line&rsquo; nutrients, which many growers "
      "use. Athena Ag supplies a tissue culture kit for a bench, with all the items in one set. The "
      "kit is for growers who are new to laboratory work. It puts the items that have a high cost "
      "and that are not easy to get in one toolbox." + R["athena"]),
    figure(FX.fig_athena_kit(), 8,
      "The known contents of the Athena Culture Kit (green), and the parts about which Athena gives "
      "no information (amber). The kit is a set of items that is easy to use. But Athena gives no "
      "information about the basal salts of the media and the hormones. Also, the kit has no item "
      "to <em>show</em> that a plant has no disease."),
    p("Athena gives information about these items in the kit:"),
    ul([
      "A <strong>laminar flow hood</strong> that you can move easily (H13 True HEPA filter, airflow 0.5&ndash;0.9&nbsp;m/s, work zone of approximately 2.58&nbsp;ft&sup3;).",
      "A small <strong>one-touch autoclave</strong> (pressure sterilizer) for media and tools.",
      "A <strong>toolbox</strong> with a scalpel, forceps and the procedure, step by step, on the inner side of the lid.",
      "Two media in sachets. You only add water. <strong>SHOOTS</strong> (blue) is for the multiplication of shoots. <strong>ROOTS</strong> is for callus, the growth of roots and new mother plants.",
      "A sanitizer with hypochlorous acid that is safe for plants (<strong>Cleanse</strong>) and <strong>bleach</strong>. You use these two to sterilize the surface of the explant.",
      "The kit has sufficient material to prepare a maximum of <strong>approximately 120 culture vessels</strong>. You can get media, vessels and filters as refills.",
    ]),
    callout("warn", "Information that Athena does not give, and items that the kit does not include",
      ul([
        "<strong>The information about the basal salts of the media is not available.</strong> Athena does not tell you if ROOTS and SHOOTS use MS, DKW or a special mixture. Athena also does not tell you the hormones, or the dose of each hormone. You cannot adjust a medium or find the cause of a problem if you do not know the components.",
        "<strong>No disease test.</strong> The kit lets you cut the meristem. But it has <em>no</em> RT-qPCR test and <em>no</em> equipment for thermotherapy. Thus the kit cannot show that a plant has no HpLVd. Make sure that your costs include tests in an external laboratory (section 13).",
        "<strong>The cost changes with the supplier and with the date:</strong> it is approximately <strong>$1,800&ndash;$2,295</strong>. Refills (media $30&ndash;$40 for each box, vessels $15 for each vessel, HEPA $100) increase the total cost with time.",
      ], "tight")),
    callout("tip", "You can do all of this without the Athena kit",
      p("A DIY equivalent has a cost of approximately <strong>$200&ndash;$550</strong> for the "
        "start. It includes a still-air box, a pressure cooker for $60 as the autoclave, MS media "
        "powder, agar and bleach. The kit gives a set that is easy to use, and a flow hood. It does "
        "not give a different result. When this guide gives a recipe, it gives the DIY method and "
        "the method for the Athena sachet.")),
  ]})

# ---- 7. Aseptic technique ----------------------------------------------
SECTIONS.append({
  "id": "aseptic", "kicker": "07: The primary method", "title": "Aseptic technique",
  "blocks": [
    lead("Aseptic technique is the most important method of tissue culture. Make sure that you know "
         "it correctly. Ninety percent of the unsatisfactory results of growers who are new to the "
         "work are because of contamination. Contamination is a problem of method. It is not a "
         "random problem."),
    p("Aseptic technique is the method to keep microbes out of your vessel. Microbes are on your "
      "skin, in your breath, in the air and on all surfaces. Your medium is a gel with sugar and "
      "nutrients, and microbes <em>can use</em> it to increase in number. Your task is to prevent "
      "the entry of microbes."),
    h(3, "The four types of contamination and how to find them"),
    figure(FX.fig_contam(), 9,
      "The four types of contamination and the signs of each type. The endophyte is the type that "
      "is not easy to find. It is a microbe that is <em>in</em> the tissue of the mother plant. The "
      "tissue shows no problem, and bleach on the surface does not remove the microbe. Thus you "
      "cannot see the microbe for some weeks. Then the microbe increases quickly. A first week with "
      "no contamination does not show that the culture is clean. Always wait and monitor the "
      "cultures."),
    h(3, "The procedure for aseptic technique, each time"),
    steps([
      ("Clean the work area", "Clean the inner surfaces of the box or hood, and the bench, with 70% alcohol. Let the alcohol dry. If you use a still-air box, make sure that the fans and the AC are off."),
      ("Put on gloves and spray", "Put on new nitrile gloves. Then spray 70% alcohol on the gloves. Spray again each time that you touch an item out of the clean area."),
      ("Only the necessary items", "Put only the vessels, the tools and the explants for this task in the work area. More items cause more risk of contamination."),
      ("Sterilize the tools before each cut", "Put the scalpel and the forceps in alcohol momentarily. Then move them through a flame. Or use a glass-bead sterilizer (approximately 250&nbsp;&deg;C / 482&nbsp;&deg;F for approximately 20&nbsp;seconds). Then <strong>let the tools become cool</strong>. A hot tool burns the tissue when it touches the tissue."),
      ("Open the vessels for a short time", "Open a vessel only when you use it. Close the vessel immediately after you complete the task. Do not let a vessel stay open."),
      ("Do not put your hands above open vessels", "If you put your hand above an open vessel, particles of skin and spores go into the vessel. Always move your hand to the vessel from the side."),
    ]),
    callout("danger", "Flame plus alcohol is a fire risk",
      p("If you use alcohol and a flame, keep the open container of alcohol far from the flame. Do "
        "not put a flame above the container of alcohol. A glass-bead sterilizer removes the risk "
        "of an open flame. It is the safer alternative in a plastic still-air box.")),
    callout("tip", "Wait 7 days before you use a culture",
      p("Fill the vessels with new medium, or start new cultures. Then keep the vessels in the "
        "culture room for approximately <strong>7 days</strong>. Do not use the cultures, and do "
        "not add more material, before the end of this time. Contamination shows in this time, also "
        "the slow latent type. The cost to discard one vessel is much less than the cost of a batch "
        "that has a microbe that you did not find.")),
  ]})

# ---- 8. Media -----------------------------------------------------------
SECTIONS.append({
  "id": "media", "kicker": "08: Prepare the medium", "title": "Make and sterilize the medium",
  "blocks": [
    p("The medium is the gel that holds your plant. The minimum medium contains mineral salts "
      "(nutrients for the plant), sugar, vitamins, hormones (optional) and a gelling agent that "
      "makes the medium solid. The sugar gives energy because the light in a sealed vessel is too "
      "dim for the plant to make sufficient sugar. You dissolve all the items in distilled water or "
      "RO water, adjust the pH, and then sterilize the medium with heat."),
    defterm("MS (Murashige and Skoog) salts",
      "The standard mineral mixture for most plant tissue culture. It is available as a powder, and "
      "you only weigh the correct quantity. It is the safe alternative for a person who is new to "
      "the work."),
    defterm("DKW (Driver and Kuniyuki Walnut) salts",
      "An alternative mixture of salts. Some tests with cannabis show that it gives shoots that are "
      "stronger and in better condition than MS. But the tests of some laboratories do not show a "
      "better result. Use it as an alternative for a test. It is not necessary at the start." +
      R["mdpi2024_media"]),
    h(3, "A recipe for the start (for each 1 liter)"),
    p("The recipe below gives a good DIY medium for initiation and multiplication. Many growers use "
      "it. Make it one time and you will know the contents of each sachet that you get."),
    table(["Component", "Quantity for each liter", "Function"], [
      ["Distilled water or RO water", "Start with approximately 800 mL", "The solvent. Use only distilled water or RO water, because the minerals in tap water change the recipe."],
      ["MS basal salts", "<span class='num'>4.4 g</span>", "The mineral nutrition (full strength)."],
      ["Sucrose (sugar)", "<span class='num'>30 g</span> (3%)", "The source of energy. For a hobby grower, usual table sugar is sufficient."],
      ["Agar", "<span class='num'>6&ndash;8 g</span>", "The gelling agent that makes the gel solid. When you add more agar, the gel is harder and there is less hyperhydricity (section 14)."],
      ["myo-Inositol", "<span class='num'>0.1 g</span>", "A sugar alcohol that the cells use for growth."],
      ["Activated charcoal", "<span class='num'>approximately 1 g</span> (optional)", "Activated charcoal absorbs the phenolic compounds that cannabis releases. Thus browning decreases."],
      ["Hormone (PGR)", "Refer to the table below", "The hormone causes the tissue to make shoots or roots. The hormone is optional at initiation."],
      ["PPM (a biocide)", "<span class='num'>1&ndash;2 mL</span> (optional)", "More protection against microbes that stay in the medium after sterilization."],
      ["Add water to", "<span class='num'>1 L</span>. Adjust the pH to <span class='num'>5.6&ndash;5.8</span>.", "Set the pH BEFORE you add the agar and BEFORE you sterilize."],
    ], caption="A general DIY medium for cannabis. Use MS at full strength for initiation and multiplication. For rooting, use MS at half strength (section 15)."),
    callout("note", "Set the pH before the agar",
      p("First, dissolve the salts and the sugar in the water. Then <strong>adjust the pH to "
        "5.6&ndash;5.8</strong>. To decrease the pH, add a drop of dilute acid. To increase the pH, "
        "add a drop of dilute base.</p><p><em>Then</em> add the agar, and apply heat to dissolve "
        "the agar. Then put the medium in the vessels, to &#8531; of the volume of each vessel, and "
        "sterilize them. It is much less easy to adjust the pH after you add the agar.")),
    h(3, "A short list of hormones for DIY media"),
    p("If you get a kit, the hormones are in the media, thus you can ignore this list. If you mix "
      "the media, this list gives the hormones for cannabis."),
    table(["Stage", "Hormone (PGR)", "Typical dose", "Information"], [
      ["Initiation", "meta-Topolin (mT) <em>or</em> TDZ", "meta-topolin approximately 0.5 mg/L. TDZ 0.1&ndash;0.5 mg/L.", "meta-topolin is a cytokinin with a weak effect. It starts the growth of the explant. TDZ has a strong effect: keep the dose low, or it causes callus and glassy shoots."],
      ["Multiplication", "meta-Topolin (mT)", "0 to approximately 0.5 &micro;M", "In cannabis, a smaller dose frequently gives a better result. A medium without hormone frequently gives the best shoots and the largest number of shoots (refer to section 14)."],
      ["Rooting", "IBA (an auxin)", "2.5 &micro;M (approximately 0.5 mg/L)", "IBA is the best rooting hormone for cannabis. It gives approximately two times the number of roots of IAA or NAA."],
    ], caption="Cytokinins (mT, TDZ) cause shoots. Auxins (IBA) cause roots. The three rows show how PGRs control growth."),
    h(3, "Sterilize the medium"),
    p("Microbes can use the nutrients in a medium that you did not sterilize to increase in number. "
      "Thus you must sterilize the medium with heat before you use it. The DIY tool is a "
      "<strong>pressure cooker</strong>, and the laboratory tool is an <strong>autoclave</strong> "
      "(the Athena kit includes a small autoclave). The two tools do the same task: they hold the "
      "vessels at <strong>121&nbsp;&deg;C (250&nbsp;&deg;F) / 15&nbsp;psi for approximately 20 "
      "minutes</strong>."),
    grid([
      card("DIY: pressure cooker", "Put loose lids on the vessels. Keep them at 15 psi for approximately 20 minutes. Let the pressure cooker become cool and let the pressure decrease before you open it. Make sure that the steam continues to flow out of the vent slowly. Thus the pressure cooker does not pull air of the room, and spores, back into the vessels.", tag="$"),
      card("Athena: sachet and autoclave", "Put the contents of one SHOOTS sachet or ROOTS sachet in the vessel. Add RO water to the mark on the vessel (125 mL or 750 mL). Shake the vessel to dissolve the contents. Operate the one-touch autoclave. Then put the medium in the culture vessels, in the hood.", tag="Kit"),
    ], cols=2),
    callout("warn", "Shelf life",
      p("Media with only MS and agar can stay in good condition for some weeks to approximately "
        "1&ndash;2 months. Keep them in a refrigerator and in darkness. Use media that contains PPM "
        "in a maximum of approximately <strong>1 month</strong>. Make only the quantity that you "
        "will use.")),
  ]})

# ---- 9. Stage 0 ---------------------------------------------------------
SECTIONS.append({
  "id": "stage0", "kicker": "09: Stage 0", "title": "Prepare the mother plant",
  "blocks": [
    p("A donor plant in unsatisfactory condition gives cultures in unsatisfactory condition. The "
      "condition of your donor plant has the largest effect on the result: it changes if your "
      "cultures stay clean. A mother plant that is dirty, has stress or has pests causes "
      "unsatisfactory results, also when your method is correct. Some microbes are <em>in</em> the "
      "tissue, and bleach cannot remove them (the endophytes from section 7)."),
    stagecard("0", "Make the donor plant clean and strong", "1&ndash;2 weeks", "".join([
      p("Select your best plant, with the correct traits of the cultivar. Make the plant vegetative "
        "and in good condition before you cut a piece from it."),
      ul([
        "Keep the plant in <strong>vegetative growth, and not in the flowering stage</strong>. Use long days: 18 h of light and 6 h of darkness.",
        "Keep the temperature at <strong>24&ndash;30&nbsp;&deg;C (75&ndash;86&nbsp;&deg;F)</strong> and the humidity at a moderate <strong>55&ndash;60%</strong>.",
        "Apply a vegetative feed and keep the plant in <strong>soft, fast new growth</strong>. New tissue gives explants that are better and have less disease than the explants from hard stems.",
        "First, examine the plant for <strong>pests and disease</strong> and apply a treatment. Use only a plant that is in good condition.",
      ], "tight"),
    ])),
    callout("tip", "Prepare the plant before the cut",
      ul([
        "In the <strong>1&ndash;2 weeks before you cut</strong>, keep the humidity low and do not apply water from above. Dry foliage has a much smaller number of fungi and bacteria on the surface.",
        "Some growers apply a systemic fungicide during this period, as a drench or as a spray. It decreases the internal load of microbes in the plant, and sterilization of the surface cannot touch these microbes.",
        "Cut your explants from the <strong>top nodes that are new and have their full size</strong>. Use a shoot in active growth. Do not use the soft tip or the hard bottom of the shoot.",
      ], "tight")),
  ]})

# ---- 10. Stage 1 explant + sterilize -----------------------------------
SECTIONS.append({
  "id": "stage1", "kicker": "10: Stage 1", "title": "Cut and sterilize the explant",
  "blocks": [
    p("In this step, you start the work with the plant. You cut a small piece from the mother plant "
      "that you prepared, and you sterilize the surface of the piece. The sterilization kills each "
      "microbe on the outer surface, but it does not kill the plant tissue. This step has the "
      "highest risk of contamination and of unsatisfactory results. Thus do the work slowly and "
      "obey the sequence correctly."),
    h(3, "Cut the explant"),
    p("For your <em>first</em> batches, use a <strong>nodal segment</strong>. A nodal segment is a "
      "piece of stem that is approximately 1 cm (0.4 in) long and contains one bud. With this "
      "explant, an error has less effect. Thus you can find the problems of aseptic technique "
      "before you do the meristem dissection, which is not easy (section 12). Remove the large "
      "leaves to decrease the surface area that has microbes."),
    h(3, "Sterilize the surface of the explant"),
    p("The standard protocol for growers who are new to the work has two primary steps. The data "
      "show that this protocol gives the best results. First, put the explant in alcohol for a "
      "short time, to break the wax on the surface. Second, soak the explant in bleach to kill all "
      "the microbes. Then flush the explant fully with water. Thus no bleach stays on the explant "
      "to cause damage to the tissue."),
    figure(F.fig_sterilize(), 10,
      "The sequence for sterilization of the surface. You do all the steps from the alcohol step in "
      "the still-air box or flow hood, with tools and water that you sterilized. The time in the "
      "liquids changes with how hard the tissue is. A time that is too short leaves microbes on the "
      "explant. A time that is too long kills the explant."),
    table(["Step", "Material", "Time"], [
      ["1. Clean", "Tap water and a drop of dish soap. Move the explant carefully in the liquid.", "10&ndash;20 min"],
      ["2. Put in alcohol", "70% ethanol or isopropyl alcohol", "30&ndash;60 sec"],
      ["3. Put in bleach", "10% household bleach (1 part bleach : 9 parts water) and some drops of Tween-20 or dish soap. Mix the liquid carefully.", "15&ndash;20 min"],
      ["4. Flush &times;3", "Distilled water that you sterilized. Use new water each time.", "3 min each"],
      ["5. Cut again", "Cut the ends that bleach damaged, on a surface that you sterilized.", "&ndash;"],
      ["6. Put on the medium", "Put the explant on the initiation medium. Seal the vessel.", "&ndash;"],
    ], caption="Sterilization of the surface for growers who are new to the work. The Athena protocol cleans the explant with Cleanse (hypochlorous acid) before the bleach. Athena does not give the dilutions and the times." + R["holmes2021"]),
    callout("danger", "The primary error: &ldquo;10% bleach&rdquo; is NOT &ldquo;10% NaOCl&rdquo;",
      p("Recipes use two different values for the quantity of bleach. If you use the incorrect "
        "value, you cause damage to your tissue. <strong>Household bleach contains only "
        "approximately 5&ndash;8% sodium hypochlorite (NaOCl) before you mix it with "
        "water.</strong> Thus a 10% dilution of household bleach gives only approximately "
        "0.5&ndash;0.8% <em>active</em> NaOCl, and this value is correct. A report that gives "
        "&lsquo;1% NaOCl&rsquo; shows a stronger solution. Before you mix, examine if a number is "
        "for diluted bleach or for active NaOCl.")),
    callout("warn", "Do not soak the explant for too long",
      p("After approximately 30 minutes in bleach, necrosis starts in the cannabis tissue. In one "
        "test, 75% of the tissue had necrosis after 45 minutes or more. If you sterilize for too "
        "short a time, there is contamination. If you sterilize for too long, the explant has "
        "necrosis and is brown. A time of 15&ndash;20 minutes is the best start point for growers "
        "who are new to the work. Adjust the time from this value.")),
  ]})

# ---- 11. Stage 2 initiation --------------------------------------------
SECTIONS.append({
  "id": "initiation", "kicker": "11: Stage I", "title": "Culture initiation",
  "blocks": [
    p("&lsquo;Initiation&rsquo; is the period after you put the sterilized explant on its medium. "
      "The period also has the name &lsquo;establishment&rsquo;. In this period, the explant adapts "
      "to the medium and starts to increase in size. Your tasks in this period are two. First, "
      "monitor the cultures carefully for contamination. Second, prevent browning that kills the "
      "tissue."),
    stagecard("I", "Get a clean culture in growth", "2&ndash;4 weeks", "".join([
      ul([
        "Put the vessels with explants in the culture room at <strong>approximately 25&nbsp;&deg;C "
        "(77&nbsp;&deg;F)</strong>. Use <strong>16 h of light and 8 h of darkness</strong>, with "
        "light of low intensity.",
        "<strong>Monitor the vessels for 7&ndash;14 days.</strong> Immediately discard a vessel with fungal growth, a medium that is not transparent, or slime. One vessel with contamination can cause contamination in the other vessels on the shelf.",
        "The bud usually becomes larger and makes new growth (&lsquo;bud break&rsquo;) in approximately <strong>2&ndash;3 weeks</strong>.",
        "Cultures that are clean and in growth go to the multiplication stage.",
      ], "tight"),
    ])),
    callout("warn", "Browning: the second cause that kills explants",
      p("Cut cannabis releases <strong>phenolic</strong> compounds. The oxidation of these "
        "compounds makes the tissue, and the medium around it, brown. The oxidation can kill the "
        "tissue. To decrease browning, add <strong>activated charcoal to the medium</strong> "
        "(approximately 1 g/L). Put the explant in an antioxidant liquid for a short time. In the "
        "first two weeks, move the explant to new medium after a short time, and do this again "
        "frequently.")),
    callout("note", "Low survival at initiation is usual",
      p("Initiation is the stage with the lowest survival, because cannabis is a recalcitrant "
        "species. Reports of laboratories show values for different cultivars. In the best report, "
        "approximately 55% of explants stay in good condition. In other reports, 90&ndash;95% of "
        "explants do not stay in good condition. Start more explants than the number that you think "
        "is necessary. A low survival in your first batch is usual.")),
  ]})

# ---- 12. Meristem cleanup ----------------------------------------------
SECTIONS.append({
  "id": "cleanup", "kicker": "12: Meristem dissection", "title": "Meristem dissection for cleanup of genetics",
  "blocks": [
    p("The steps before this step are the same as the steps of usual cloning. <strong>This "
      "step</strong> removes the disease. You do not use a node of 1 cm (0.4 in). You cut only the "
      "very small meristem dome from section 5, which does not contain the viroid. Then you make "
      "your new plant from this dome."),
    stagecard("M", "Cut the clean meristem dome", "4&ndash;8 weeks for the growth of a shoot", "".join([
      steps([
        ("Sterilize a shoot tip", "Sterilize the surface of a shoot tip in active growth, as in section 10."),
        ("Use the microscope", "Use a stereo microscope (a dissecting microscope) in the flow hood. Use needles or forceps that you sterilized. Remove the small leaves around the shoot tip, one by one. Continue until you see the shiny, transparent meristem dome."),
        ("Cut the dome", "Cut only the dome and 1&ndash;2 leaf primordia. The piece is only <strong>0.2&ndash;0.5&nbsp;mm (0.008&ndash;0.020&nbsp;in)</strong> across. Put it on the initiation medium."),
        ("Wait", "A meristem is slow and weak. The time for a meristem to become a shoot in good condition is approximately 10 weeks. For some meristems, the time is up to approximately 24 weeks. This time is much longer than the time for a node."),
      ]),
    ])),
    h(3, "HpLVd removal rates for each cultivar"),
    p("It is important to give accurate information here. Meristem culture <em>can</em> remove "
      "HpLVd, but the success rate changes very much with the cultivar. One test of 13 cultivars "
      "used meristem culture and a weak heat treatment. In this test, the treatment removed the "
      "disease fully in only <strong>5 of 13</strong> cultivars." + R["hlvd_thermo2024"]),
    figure(FX.fig_hlvd_clearance(), 11,
      "The removal rates of one protocol for 13 cannabis cultivars. The rate was 100% for some "
      "cultivars and only 14% for the other cultivars. There is no recipe for all cultivars. Make "
      "more than one meristem clean for each cultivar, and test all of them. (The cultivar with the "
      "name &lsquo;Athena&rsquo; here has no relation to the Athena Ag kit.)"),
    callout("note", "Optional methods: thermotherapy and cryotherapy",
      ul([
        "<strong>Thermotherapy</strong> is the method to keep the mother plant or the culture warm (approximately 30&ndash;36&nbsp;&deg;C / 86&ndash;97&nbsp;&deg;F) for two weeks. It decreases the viroid level. Thus you can cut a meristem with a small increase in size, and this meristem stays clean and stays in good condition more easily. If you use only thermotherapy, the result is not good each time: the levels increase again, and heat can also make mutant viroids. Thus use thermotherapy <em>with</em> meristem dissection. Do not use it as the only method.",
        "<strong>Cryotherapy</strong> is the method to freeze shoot tips in liquid nitrogen for a short time. Only the very small clean cells stay in good condition. Laboratories use it as a strong method in tests. At this time, there is no standard protocol for cannabis that tests show is correct. Put it in the group &lsquo;advanced/future&rsquo;.",
      ], "tight")),
    callout("warn", "The Athena kit can clean the plant, but it cannot show that the plant is clean",
      p("The kit lets you cut the meristem. It includes <strong>no equipment for heat treatment and "
        "no DNA test</strong>. After this step, the plant is <em>possibly</em> clean. You are "
        "<em>sure</em> that the plant is clean only after a laboratory RT-qPCR test shows no "
        "viroid. The next section gives the test, and the test is mandatory.")),
  ]})

# ---- 13. Indexing -------------------------------------------------------
SECTIONS.append({
  "id": "indexing", "kicker": "13: Disease testing", "title": "Indexing: make sure that the stock has no pathogens",
  "blocks": [
    p("A meristem plant that has <em>no signs</em> of a problem is not a clean plant until a "
      "laboratory test shows that the plant is clean. &lsquo;Indexing&rsquo; is that test. If you "
      "do not do the test, you can make a &lsquo;clean&rsquo; mother plant in six months of work. "
      "Then this mother plant can infect all the plants of your room with the viroid again, without "
      "a sign."),
    defterm("RT-qPCR",
      "The standard RNA test with the highest accuracy for HpLVd. A laboratory increases the "
      "quantity of the viroid RNA in your sample until the test can find it. The test can find a "
      "small number of copies. You send tissue to the laboratory, and the laboratory sends back the "
      "result: viroid found, or viroid not found. Many cannabis testing laboratories do this test "
      "at a low cost for each sample."),
    defterm("RT-LAMP",
      "A test that is newer and costs less. It operates at one temperature, and no thermocycler (an "
      "instrument with a high cost) is necessary. Thus you can do the test in your facility or near "
      "the plants. A smaller number of laboratories use it than qPCR, but the number increases."),
    callout("key", "Indexing: time and tissue for the test",
      ul([
        "HpLVd moves slowly in a new plant, and it is not in all the parts at the same time. It is in the <strong>roots after approximately 2&ndash;3 weeks</strong> and in the <strong>foliage after approximately 4&ndash;6 weeks</strong> from the infection.",
        "Thus <strong>do the test more than one time, on more than one tissue.</strong> Roots are the most accurate indicator in the first period. Also test leaves of different ages.",
        "Do a test of the plantlet. Then <strong>do the test again when the plant becomes larger</strong>, before you use it as a production mother plant. One first test that finds no viroid does not show that the plant is clean.",
      ], "tight")),
    callout("tip", "Include the cost of the tests",
      p("The suppliers of kits do not give information about this cost. Tests of HpLVd in an "
        "external laboratory show if the plant is clean. Without these tests, you do not know if "
        "the plant is clean. Include the cost of some laboratory tests for each mother plant that "
        "you want to use. The cost of the damage to a crop is much more than the cost of the tests.")),
  ]})

# ---- 14. Multiplication -------------------------------------------------
SECTIONS.append({
  "id": "multiplication", "kicker": "14: Stage II", "title": "Multiplication and hyperhydricity",
  "blocks": [
    p("When you have a clean shoot in growth, multiplication makes many shoots from one shoot. You "
      "move the shoot to a medium with a cytokinin (the hormone that causes shoots). The shoot "
      "makes some new shoots. You cut the new shoots from each other and move them to new medium. "
      "Then you do these steps again. Each cycle is a <strong>subculture</strong>, approximately "
      "each 4 weeks."),
    stagecard("II", "Make more shoots, cycle by cycle", "4&ndash;8 weeks (1&ndash;2 cycles)", "".join([
      kv([
        ("Basal medium", "Full-strength MS (DKW optional)"),
        ("Hormone", "0 to approximately 0.5 &micro;M meta-topolin (frequently the best result is with no hormone)"),
        ("Sugar / gel / pH", "30 g/L sucrose &middot; 6&ndash;9.5 g/L agar &middot; pH 5.7&ndash;5.8"),
        ("Environment", "25 &plusmn; 2 &deg;C (77 &plusmn; 4 &deg;F) &middot; 16 h light &middot; approximately 100&ndash;120 &micro;mol/m&sup2;/s"),
        ("Subculture each", "approximately 4 weeks"),
        ("Usual rate", "approximately 1&ndash;6 new shoots for each shoot in each cycle (the rate changes with the cultivar)"),
      ]),
    ])),
    callout("note", "Try a medium without hormone",
      p("You can think that more cytokinin gives more shoots. But in cannabis, some tests show the "
        "<strong>largest</strong> number of shoots, and the shoots in the best condition, on a "
        "medium without hormone. More cytokinin decreases the number of shoots and causes glassy "
        "shoots with an incorrect shape. Start with a low dose or with no hormone. Add hormone only "
        "if you must have a higher rate. (The Athena SHOOTS sachet contains the hormones, and you "
        "cannot change the doses.)")),
    h(3, "Hyperhydricity: the problem that stops multiplication"),
    p("In a sealed vessel at humidity near 100%, the tissue does not make the protective "
      "structures. A plant must have these structures to stay in good condition in open air. Water "
      "saturates the tissue, and the water does not drain from the tissue. Thus the tissue does not "
      "make structures to keep its shape when you remove it from the vessel. When you move this "
      "tissue to usual air, it cannot control the quantity of water that leaves it. This problem is "
      "<strong>hyperhydricity</strong>."),
    defterm("Hyperhydricity (vitrification)",
      "Shoots that become glassy, transparent and full of water, and that break easily. They are "
      "larger than usual and wet. Their leaves do not make a correct layer of wax or stomata that "
      "operate correctly. Thus they make a small number of roots, and they usually <strong>show "
      "wilt and necrosis when you move them to soil</strong>. It is problem number 1 of "
      "multiplication, and it occurs frequently in cannabis."),
    p("The causes are too much humidity in the vessel, too much cytokinin, a soft gel with much "
      "water, and not sufficient air exchange. The corrections are easy when you know the causes:"),
    ul([
      "Use <strong>meta-topolin</strong>, and not the cytokinin BAP. Keep the cytokinin dose low or zero.",
      "<strong>Make the gel harder.</strong> More agar (to a maximum of 9.5 g/L) makes the medium drier, and the shoots are in better condition on it.",
      "<strong>Ventilate</strong> the vessels (lids with vents, or lids that let gas go through) to let humidity and ethylene flow out.",
      "<strong>Do the subcultures at the correct time</strong> (approximately each 4 weeks). Thus hormones and gases do not increase in the vessel.",
    ]),
    h(3, "The limit of 5 subculture cycles"),
    p("Each time that you do a subculture, a small number of very small errors in the copies of DNA "
      "(mutations) occur. A new test with cannabis shows that the mutations increase <em>in "
      "proportion</em> to the number of subcultures. The relation between the two is almost linear. "
      "If you do too many subcultures, your &lsquo;identical&rsquo; clones change slowly and are "
      "not the same as the initial plant." + R["torkamaneh2024"]),
    figure(FX.fig_subculture(), 12,
      "The number of mutations increases approximately linearly with each subculture (the test "
      "found a very close relation). The usual limit for growers is from the propagation of "
      "bananas. By approximately the fifth cycle, start again with new clean stock or frozen clean "
      "stock. Do not do subcultures without a limit."),
    callout("key", "The limit",
      p("Use the cultures from one explant for a maximum of <strong>approximately 5 "
        "subcultures</strong>. Then start again from a new explant that you cleaned, or from stock "
        "in cryopreservation. This procedure keeps the traits of the cultivar in your clones.")),
  ]})

# ---- 15. Rooting --------------------------------------------------------
SECTIONS.append({
  "id": "rooting", "kicker": "15: Stage III", "title": "Rooting",
  "blocks": [
    p("A shoot from multiplication has no roots. Rooting gives the shoot roots with an "
      "<strong>auxin</strong> (the group of hormones that cause roots). There are two procedures. "
      "The two procedures give a good result, and the second procedure is easier for growers who "
      "are new to the work."),
    grid([
      card("Procedure A: in vitro rooting", p("Move the shoots to a rooting medium that you sterilized. "
        "The medium contains <strong>MS at half strength</strong>, 3% sugar, <strong>IBA at "
        "approximately 2.5&nbsp;&micro;M</strong> (approximately 0.5 mg/L) and a small quantity of "
        "activated charcoal. Roots show by approximately week 3. The result for cannabis with the "
        "most citations is approximately 95% rooting, with approximately 5 roots for each shoot." +
        R["pmc9146626"]), tag="Aseptic technique"),
      card("Procedure B: ex vitro &lsquo;dip and plant&rsquo;", p("Remove the shoot from the vessel "
        "and put the bottom end of the shoot in a rooting gel (for example, approximately "
        "1,000&ndash;3,000 ppm IBA). Then put the shoot in a moist rockwool cube, with a humidity "
        "dome above it. Rooting and acclimatization occur together, out of the vessel. Commercial "
        "growers select this procedure because it gives better roots, higher survival and one step "
        "less with aseptic technique." + R["kurtz2022"]), tag="Easier"),
    ], cols=2),
    stagecard("III", "Make roots", "2&ndash;4 weeks", "".join([
      ul([
        "<strong>IBA is the best auxin for cannabis</strong>. It gives approximately two times the number of roots of IAA or NAA.",
        "The rooting substrates from best to worst are <strong>rockwool, peat and coco</strong>. Rockwool is clearly the best because it has a good balance of air and water, and it has no microbes.",
        "Harvest the shoots for rooting from <strong>cultures with a low age</strong> (6&ndash;12 weeks). Cultures with a higher age give a much lower success rate for rooting.",
        "The roots show in 2&ndash;4 weeks in vitro. For ex vitro cuttings with a dome, the roots show in 7&ndash;10 days.",
      ], "tight"),
    ])),
    callout("note", "The Athena ROOTS sachet",
      p("The Athena ROOTS medium is a rooting medium and callus medium that Athena mixes before you "
        "get it, with the hormones in it. The procedure is the same as Procedure A, but you do not "
        "measure the components. As with the other Athena media, you cannot see the components and "
        "you cannot adjust them.")),
  ]})

# ---- 16. Acclimatization ------------------------------------------------
SECTIONS.append({
  "id": "acclim", "kicker": "16: Stage IV", "title": "Plantlet acclimatization",
  "blocks": [
    p("Do this stage slowly. If you do it too fast, many plantlets do not stay in good condition. A "
      "plantlet from a sealed vessel is in conditions with humidity near 100%, a constant warm "
      "temperature, sugar in the medium and dim light. Its leaves did not make a correct layer of "
      "wax or stomata that operate correctly. If you put the plantlet directly in the air of the "
      "room, it shows wilt and necrosis in some hours."),
    defterm("Acclimatization (hardening)",
      "The procedure to make the plantlet stronger gradually. You decrease the humidity slowly and "
      "increase the light slowly during two weeks. Thus the plantlet makes a correct cuticle, "
      "stomata that operate correctly and stronger roots. It then stays in good condition without "
      "the protection of the vessel."),
    figure(F.fig_acclim(), 13,
      "The primary procedure of acclimatization is to decrease the humidity in steps, and not all "
      "at one time. Start with the dome closed, at high humidity. Each day, increase the opening of "
      "the vents by a small quantity. Remove the dome fully only after approximately two to three "
      "weeks. At this time, the plantlet has roots and a correct layer of wax."),
    stagecard("IV", "Acclimatize the plantlet to the conditions of the room", "2&ndash;4 weeks", "".join([
      steps([
        ("Put the plantlet in a pot", "Move the plantlet with roots to a clean substrate that you sterilized. Use rockwool, or a mixture of peat and perlite (1:2), in a small pot or a plug."),
        ("Put the dome on, at high humidity", "Put a humidity dome or a propagator on the plantlet. Keep the humidity at approximately 75&ndash;80%. At the start, keep the light low, at approximately 50&nbsp;&micro;mol/m&sup2;/s. Apply water carefully."),
        ("Decrease the humidity in steps", "During approximately 2&ndash;3 weeks, open the vents by a small quantity more each day. Decrease the humidity to approximately 55&ndash;65%. Monitor the plantlets for wilt. If the plantlets show wilt, close the vents to the previous opening."),
        ("Increase the light in steps", "When the humidity decreases, increase the light to approximately 500&nbsp;&micro;mol/m&sup2;/s, approximately ten times the first value. Thus the plant becomes strong."),
        ("Remove the dome", "When the plantlet keeps turgor in open air and makes new growth, remove the dome. Then the plantlet is a usual plant."),
      ]),
    ])),
    callout("warn", "The three causes that kill plantlets at this stage",
      ul([
        "<strong>Desiccation</strong>: the humidity decreases too fast. The plantlet cannot close its stomata in time, and it becomes dry. Desiccation is cause number 1, thus decrease the humidity slowly.",
        "<strong>Hyperhydricity from Stage II</strong>: glassy shoots from a multiplication stage with too much humidity cannot acclimatize. Correct the cause in the multiplication stage (section 14).",
        "<strong>Damping-off</strong>: fungal rot in the substrate that is warm and wet. Use a substrate that you sterilized. Do not apply too much water.",
      ], "tight")),
    callout("tip", "A good result",
      p("Reports of protocols that laboratories operate correctly show <strong>90&ndash;100% "
        "survival</strong> in acclimatization. These values are for the best conditions in a "
        "laboratory, and your first batch can have lower values. But they show that a slow and "
        "careful acclimatization gives a good result." + R["page2019"])),
  ]})

# ---- 17. Re-establish mother -------------------------------------------
SECTIONS.append({
  "id": "mother", "kicker": "17: The clean mother plant", "title": "Make a new clean mother plant",
  "blocks": [
    p("You have the plantlet after acclimatization. We recommend that a laboratory test shows that "
      "the plantlet is clean. Make the plantlet larger, until it is a <strong>mother plant (stock "
      "plant)</strong>. Then get cuttings from the mother plant with the usual easy method, in "
      "large quantity."),
    steps([
      ("Make the mother plant larger", "Put the clean plantlet in a larger pot. Keep the plantlet in vegetative growth with long days (18&ndash;24 h of light). Use a space that is very clean and has controlled conditions. We recommend that you keep the space away from your previous plants that possibly have the infection."),
      ("Make sure that the plant is clean again", "Do the HpLVd test again when the plant becomes larger, before you use the plant. Only a plant with a test that finds no viroid is a &lsquo;clean mother&rsquo;."),
      ("Get cuttings or retips", "From the mother plant, get usual stem cuttings or soft &lsquo;retips&rsquo; from the tip of a shoot. Cannabis retips make roots at 76&ndash;81% with no hormone, and at more than 90% with IBA at approximately 1,000 ppm. This method is easy and increases the quantity of clean stock quickly."),
      ("Keep the mother plant clean", "Use dedicated tools that you sanitized. Sanitize your hands and the surfaces between plants. Do not let a plant without a laboratory test come near the mother plant. Clean stock stays clean only if you always obey these procedures."),
    ]),
    callout("key", "The quality does not change",
      p("Tests show that mother plants from tissue culture are <strong>chemically the same</strong> "
        "as the initial plants. The cannabinoid content of plants from micropropagation, from "
        "retips and from usual cuttings was the same. Tissue culture does not change your cultivar. "
        "It gives the cultivar back to you in good condition.")),
  ]})

# ---- 18. Storage / latest ----------------------------------------------
SECTIONS.append({
  "id": "advances", "kicker": "18: More methods", "title": "Storage of genetics: synthetic seeds and cryopreservation",
  "blocks": [
    p("When you can clean and multiply a cultivar, you can also <em>keep</em> the clean genotype in "
      "storage. Thus it is not necessary to clean the cultivar again. Two methods are important to "
      "know, also for a person who is new to the work. Growers use these methods more and more."),
    grid([
      card("Synthetic seed", p("A shoot tip or a bud in a soft bead of calcium alginate gel. It is "
        "an &lsquo;artificial seed&rsquo; that you can keep and send. Tests show that the method is "
        "correct in commercial production with cannabis: buds of &lsquo;Slurricane&rsquo; in beads "
        "showed 100% regrowth after 150 days of storage. The method is good for storage of genetics "
        "for a short time or a medium time, and to send genetics."), tag="Storage"),
      card("Cryopreservation", p("You freeze very small shoot tips in liquid nitrogen "
        "(&minus;196&nbsp;&deg;C / &minus;321&nbsp;&deg;F) for storage with no time limit. It is "
        "the best method for long-term storage of germplasm. It also &lsquo;resets the clock&rsquo; "
        "for the mutations of subculture from section 14. It is a correct method, but it is not "
        "easy. In cannabis protocols, approximately 55&ndash;63% of the tips show regrowth." +
        R["karger2019_cryo"]), tag="Long-term"),
    ], cols=2),
    callout("note", "Use in commercial production",
      p("Commercial laboratories for clean stock do all these steps in one sequence. Two examples "
        "are Conception Nurseries and Front Range Biosciences. The first steps are: test &rarr; "
        "meristem cleanup &rarr; micropropagation &rarr; check of the traits. The last steps are: "
        "storage of the best mother plants with a frozen copy &rarr; send clones or synthetic seed. "
        "The largest of these laboratories makes more than 500,000 plants each month. You do the "
        "same procedure, but in a small quantity." + R["tis2022"])),
    callout("tip", "A new method (2025)",
      p("For a long time, cannabis was a recalcitrant species: regeneration was possible with only "
        "a small number of cultivars. A report of a 2025 protocol with cotyledonary-node explants "
        "shows a success rate of approximately 70&ndash;90% for many hemp cultivars and medicinal "
        "cultivars. It is a step to methods for <em>all</em> genetics. The methods continue to "
        "change quickly.")),
  ]})

# ---- 19. Troubleshooting ------------------------------------------------
SECTIONS.append({
  "id": "trouble", "kicker": "19: When there is a problem", "title": "Troubleshooting",
  "blocks": [
    p("Almost all problems of growers who are new to the work are in this table. Find the symptom, correct the cause and record the result."),
    table(["Symptom", "Possible cause", "Correction"], [
      ["The medium is not transparent, there is slime at the bottom of the explant, and you smell a bad vapor from the vessel", "Contamination with bacteria (frequently from an endophyte in the mother plant)", "Discard the vessel. Make the condition of the mother plant better, and prepare the plant before you cut a piece. You can add PPM to the medium. Obey the aseptic technique more carefully."],
      ["White fungal growth, or fungal growth with a color, on the medium. The growth increases in size.", "Fungal contamination (airborne spores)", "Discard the vessel immediately, before the contamination moves to other vessels. The cause is the air or your method. Do a check of your clean-air setup and of the sterilization of the tools."],
      ["The cultures showed no problem for 2 weeks. Then they suddenly changed to an unsatisfactory condition.", "A latent endophyte that increases quickly on a medium with many nutrients", "Wait and monitor the cultures. Start with mother tissue in better condition, to which you applied a treatment before you cut the explants. Use smaller and newer explants."],
      ["The explant becomes brown and has necrosis", "Oxidation of phenolic compounds (browning)", "Add activated charcoal (approximately 1 g/L). Put the explant in an antioxidant liquid for a short time. Move the explant to new medium after a short time, and do this again frequently."],
      ["The shoots are glassy, larger than usual and full of water, and they break easily", "Hyperhydricity (vitrification)", "Decrease the cytokinin or remove it. Make the gel harder (more agar). Ventilate the vessels. Do the subcultures at the correct time."],
      ["A small number of new shoots, or no new shoots, in multiplication", "Too much hormone, or this cultivar gives a low rate with this medium", "Try a medium without hormone, or with less cytokinin. Know that the rate changes with the cultivar."],
      ["The shoots do not make roots", "The auxin is incorrect or not sufficient, or the age of the culture is too high", "Use IBA at approximately 2.5 &micro;M. Harvest shoots from cultures with a low age (6&ndash;12 weeks). Try the ex vitro procedure &lsquo;dip and plant&rsquo;."],
      ["The plantlets show wilt and necrosis when you move them to soil", "Acclimatization that is too fast (desiccation)", "Decrease the humidity in steps, more slowly, during 2&ndash;3 weeks. Keep the dome on for a longer time. Make sure that the plantlet has good roots first."],
      ["A plant that you cleaned has HpLVd in the test result", "The meristem is too large, or the cultivar is not easy to clean", "Cut a smaller dome. Clean some meristems of each cultivar. You can add thermotherapy. Always do the indexing test again."],
      ["The clones change with time and are not the same as the initial plant", "Too many subcultures (increase of mutations)", "Start again from new stock or stock in cryopreservation, by approximately 5 subcultures."],
    ], cls="compact"),
  ]})

# ---- 20. Reality check --------------------------------------------------
SECTIONS.append({
  "id": "reality", "kicker": "20: Accurate information", "title": "Expected results and limitations",
  "blocks": [
    p("Use these values to know the results that are possible before you start."),
    h(3, "Success rates: the best values in reports and the first batch of a new grower"),
    table(["Stage", "Best value in a laboratory", "First batches of new growers"], [
      ["Survival at initiation", "a maximum of approximately 55%", "frequently much lower. Reports show that 90&ndash;95% of the explants do not stay in good condition, and the result is usual."],
      ["Rooting", "95&ndash;100%", "lower, but it increases in the next batches"],
      ["Survival in acclimatization", "90&ndash;100%", "lower in the first batches"],
      ["HpLVd removal (for each cultivar)", "0&ndash;100% (average approximately 40%)", "the rate changes very much with the cultivar. Clean more than one meristem, and test all of them."],
    ], caption="The values in reports are the best values. Your first batch will give lower values. A low value in the first batch is usual, and it does not show an error in your work."),
    h(3, "Costs"),
    table(["Alternative", "At the start", "During use"], [
      ["DIY start (still-air box and pressure cooker)", "approximately $200&ndash;$550", "Media powder, bleach, agar and gel. The cost is low."],
      ["Larger laboratory for a hobby grower", "less than approximately $1,000", "Consumables. A flow hood is optional and you can add it after the start."],
      ["Athena Culture Kit", "approximately $1,800&ndash;$2,295", "Media $30&ndash;$40 for each box, vessels $15 for each vessel, HEPA $100"],
      ["HpLVd laboratory tests (necessary)", "cost for each sample", "Some tests for each mother plant that you want to use. Add this cost to the total."],
    ]),
    callout("danger", "The four limits that you must know",
      ol([
        "<strong>A plant without the viroid is not resistant to the viroid.</strong> A dirty tool or hand can infect a clean plant again immediately. You must always do the hygiene procedures.",
        "<strong>A kit can clean the plant, but it cannot show that the plant is clean.</strong> The kit has no qPCR test, thus it gives no result that shows &lsquo;clean&rsquo;. Tests in an external laboratory are mandatory, not optional.",
        "<strong>The result changes with the cultivar, and the procedure is slow.</strong> For some genetics, the removal of the viroid is very low. The time to make a mother plant that tests show is clean is many months.",
        "<strong>You cannot see the components of the media.</strong> Kits give media that are mixed before you get them. The media are easy to use. But you cannot adjust the media, and it is not easy to find the cause of a problem. Many growers use the media without a problem. It is a limit if you want to make the media better.",
      ])),
    callout("key", "The primary result",
      p("Tissue culture is the only method that gives a good result to remove Hop Latent Viroid and "
        "other diseases from a cannabis cultivar. Then the genetics can give the correct "
        "performance. A hobby grower can do tissue culture, and a kit makes the work easy. The "
        "biology is correct, <em>if</em> you obey aseptic technique, do the acclimatization slowly "
        "and show your results with a laboratory test. Do not accept &lsquo;the plant has no signs "
        "of a problem&rsquo; without a test.")),
  ]})

# ============================================================ FOOTER

FOOTER = """
<footer class="footer"><div class="wrap">
  <h3>About this guide</h3>
  <p>A first-timer's user guide to cannabis tissue culture for cleaning up genetics, synthesised
  from peer-reviewed literature (2019&ndash;2026) and current commercial practice. Product details
  for the Athena Culture Kit are from Athena Ag's own pages; some of their step-by-step figures are
  proprietary and undisclosed, and are flagged as such throughout. Figures are illustrative
  schematics, not to scale. Nothing here is legal advice: follow the cannabis laws in your
  jurisdiction.</p>

  <h3>Key sources</h3>
  <ul class="refs">
    <li>Holmes et&nbsp;al. 2021, <em>Front. Plant Sci.</em>: canonical cannabis sterilisation &amp; shoot culture. PMC8491305</li>
    <li>2024, <em>Plants/MDPI</em>: media composition &amp; explant type optimisation. PMC11434680</li>
    <li>Page et&nbsp;al. 2019, <em>Plant Methods</em>: photoautotrophic micropropagation &amp; acclimatisation schedule. PMC6660493</li>
    <li>An Alternative In&nbsp;Vitro Propagation Protocol (efficient rooting), 2022. PMC9146626</li>
    <li>Kurtz et&nbsp;al. 2022, <em>HortScience</em>: ex-vitro rooting, retips, mother stock.</li>
    <li>Somatic Mutation Accumulation in Micropropagated Cannabis, 2024, <em>Plants</em>: the 5-subculture rule. PMC11279941</li>
    <li>Hop Latent Viroid: A Hidden Threat, 2023. PMC10053334 &middot; Transmission/Management review, 2025. PMC11902214</li>
    <li>HLVd thermotherapy + meristem clearance across 13 cultivars, 2024&ndash;25 (bioRxiv 2024.04.06.588422 / PCTOC 2025).</li>
    <li>Temporary Immersion System for cannabis, 2022, <em>Front. Plant Sci.</em> &middot; Cryopreservation by droplet vitrification, Karger 2019.</li>
    <li>Athena Ag: Culture Kit, ROOTS/SHOOTS media &amp; Plant/Media/Lab Prep procedure (athenaag.com, store.athenaag.com, support.athenaag.com).</li>
  </ul>
  <p class="disc">Built as a self-contained HTML document: opens offline, no network required.
  Generated for a first-time tissue-culture grower. Verify dilutions, hormone doses and local
  regulations against primary sources before relying on them; cannabis tissue culture is strongly
  genotype-dependent and recipes often need per-strain tuning.</p>
</div></footer>
"""
