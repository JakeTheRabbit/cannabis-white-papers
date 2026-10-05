# -*- coding: utf-8 -*-
"""Paper: cannabis tissue culture playbook (start-to-finish). Does not replace tissue-culture."""
from components import (p, lead, h, ul, ol, callout, defterm, table, steps,
                        figure, grid, card, kv, photo, photo_sequence)
import figs as F
import figs_extra as FX
import figs_playbook as FP

SLUG = "cannabis-tissue-culture-playbook"
TITLE = "Cannabis tissue culture from start to end"
TITLE_MAX_PX = 40
EYEBROW = "Propagation · in steps · ~45 min"
SUB = ("This guide shows how to make a cannabis plant from a small piece of tissue in a sterilized "
       "jar. It gives the steps for a home bench and for a licensed facility. Each term has a "
       "definition. Each recipe has numbers. Read the sections in sequence.")

META = [
    ("list", "21 steps"),
    ("gauge", "No lab training necessary"),
    ("leaf", "Cannabis only"),
    ("book", "22 sources"),
    ("clock", "~45 min"),
]
RELATED = ["tissue-culture", "cannabis-tissue-culture-sop", "cloning", "mother-plants"]
REF_IDS = [
    "holmes2021", "lata2009", "lata2016", "das2024", "hlvd_threat2023",
    "hlvd_mgmt2025", "kodym2019", "kurtz2022", "torkamaneh2024", "ioannidis2022",
    "monthony2021", "page2021_dkw", "karger2019_cryo", "tis2022", "pct_howto",
    "pct_ppm", "athena", "murashige1962", "driver1984", "lubell2021",
    "punja2019-pathogens", "cwp_tc_beginner",
]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

IMG = "assets/img/tc-playbook"


SECTIONS = []

# ---------------------------------------------------------------------------
SECTIONS.append({
    "id": "how",
    "kicker": "01",
    "title": "Purpose and scope",
    "blocks": [
        lead("The first time that you use this guide, read the sections in sequence. After that, go to the stage that you are in. The tissue culture SOP has the lists of tasks and the forms. You can print them."),
        p("This guide is for two setups. The first setup is a home bench with a plastic container "
          "and a pressure cooker. The second setup is a licensed facility for medicinal cannabis. "
          "It has a hood with filtered air and written records. The work on the plants is the same. "
          "The tests and the documentation are different."),
        grid([
            card("If you are new to tissue culture", "Read sections 01 to 10. Then do a first batch with stem pieces that have one bud. Do not cut a meristem at this time.", tag="01–10"),
            card("If your setup is at home", "Section 05 gives the list of items to get and shows the bench. Sections 07–14 give the steps of the work.", tag="05, 07–14"),
            card("If your setup is a licensed lab", "Section 06 shows the rooms. Section 16 shows the disease test. Section 18 shows the work for each week.", tag="06, 16, 18"),
            card("If a jar has a problem", "Section 15 shows photos of the problems. Section 19 gives the corrections.", tag="15, 19"),
        ], cols=2),
        callout("key", "Definition of tissue culture",
                p("You cut a small piece from a cannabis plant. You put the piece on a sterilized gel. The gel contains mineral salts and sugar. The gel can also contain plant hormones. In a sealed jar, the piece becomes a new plant. The new plant has the same genetics as the plant that you cut it from.")),
        callout("warn", "Many pieces in your first batch will be defective. This is usual.",
                p("It is not easy to start a culture of cannabis in a jar. Reports from labs show "
                  "that microbes or browning make 45–95% of the first pieces defective."
                  f"{_c("holmes2021")}{_c("das2024")} Use the first batch as a test. Record the "
                  "steps that you do.")),
        defterm("In vitro", "In the sealed jar."),
        defterm("Ex vitro", "Not in the jar. For example, the plant is in a plug, in a pot or in a nursery."),
        defterm("Explant", "The piece of the plant that you put in the jar."),
        defterm("Medium (more than one: media)", "The sterilized material that gives nutrients to the culture. It contains mineral salts, sugar, vitamins and optional hormones. Agar makes it solid."),
        defterm("Agar", "A powder from seaweed. It changes the liquid medium to a solid gel. Thus the plant can stay in a vertical position in the gel."),
    ]})

# ---------------------------------------------------------------------------
SECTIONS.append({
    "id": "glossary",
    "kicker": "02",
    "title": "Definitions",
    "blocks": [
        lead("The table contains all the terms of this guide."),
        table(
            ["Term", "Definition"],
            [["Acclimatization / hardening", "The procedure in which you decrease the humidity in steps. The plant from the jar then adapts to the air of the room and to soil."],
             ["Activated charcoal", "A black powder in the gel. It removes the brown compounds that flow out of the cut surface. It can also remove hormones."],
             ["Agar / gellan / Phytagel", "The material that makes the medium solid. When you add more agar, the gel is harder. A harder gel gives drier air in the jar. As a result, the plants have less glassy growth."],
             ["Aseptic technique", "The procedure of work that prevents the contamination of the medium with microbes."],
             ["Autoclave", "A device that keeps steam at 121 °C (250 °F) and 15 psi. At home, a pressure canner that holds 15 psi does the same task."],
             ["Auxin (IBA, NAA, IAA)", "A type of hormone. It causes the tissue to make roots."],
             ["Callus", "A mass of cells that have no special function. Callus frequently occurs as a side effect. In Holmes 2021, callus was not a good method of production for cannabis."],
             ["Cytokinin (mT, TDZ, BA)", "A type of hormone. It causes the tissue to make shoots."],
             ["DKW", "Driver and Kuniyuki Walnut salts. DKW is an alternative mineral mixture to MS. The result on cannabis is different for each cultivar."],
             ["Endophyte", "A microbe in tissue that shows no sign of disease. Bleach on the surface cannot touch the microbe."],
             ["Explant", "The piece of the plant that you put in the jar."],
             ["GACP / GMP", "GACP is the standard for cultivation. GMP is the standard for manufacturing. Plants for the start of a crop are between the two."],
             ["HEPA / laminar-flow hood", "A fan and a filter. They blow a sheet of clean air across the bench. A laminar-flow hood is not a biosafety cabinet."],
             ["HpLVd / HLVd", "Hop latent viroid. It is the usual cause of “dudding”. It has 256 letters of RNA."],
             ["Hyperhydricity / vitrification", "Glassy growth in the jar. The leaves contain too much water, are transparent and break easily. Frequently, the cause is too much cytokinin or too much humidity."],
             ["In vitro / ex vitro", "In the jar / not in the jar."],
             ["Indexing", "A test of a plant for a specified pathogen. Use “clean” for a plant only after this test."],
             ["Initiation (Stage I)", "The procedure to get the first culture that makes new growth and has no contamination."],
             ["ISO 5 / ISO 7", "Ratings of how clean the air is. ISO 5 is the rating at the work surface of the hood. ISO 7 is the typical rating of the room around the hood."],
             ["Meristem", "The dome of cells that divide at a shoot tip. At this stage, the dome has no sap tubes."],
             ["Meta-Topolin (mT)", "A cytokinin that you can use to start cannabis cultures. If the quantity is too large, the Stage II plants have glassy growth."],
             ["Micropropagation", "The procedure that uses tissue culture to make many plants that are the same."],
             ["MS salts", "Murashige and Skoog, 1962. MS is the standard mineral mixture. The quantity of powder is 4.4 g (0.16 oz) for each liter."],
             ["Nodal segment", "A stem piece with one bud. It is easy to use. Frequently, the contamination continues to be in the inner tissue."],
             ["PGR", "Plant growth regulator. A hormone that you add to the medium."],
             ["Phenolics / browning", "Brown compounds that flow out of the cut surface and cause stains in the gel."],
             ["Photoautotrophic micropropagation", "A method with no sugar. It uses usual fertilizer and more air. The plants are almost the same as cuttings from a nursery."],
             ["PPM", "Plant Preservative Mixture. It is an antimicrobial. You can sterilize it with the medium in an autoclave."],
             ["qPCR / RT-qPCR", "A lab test to find the RNA of the viroid. “Not detected” is not the same as “cannot exist”."],
             ["Recalcitrant species", "A species that is not easy to start in a jar. Cannabis is one."],
             ["Somaclonal variation", "Changes in the genetics that occur after many subcultures in the jar."],
             ["Still-air box", "A transparent plastic container with two arm holes. The air in the container does not move. Thus spores do not move to open jars."],
             ["Subculture", "The procedure to move tissue to new medium."],
             ["Temporary immersion", "The liquid medium makes the shoots wet at times that a timer sets. Then the medium drains."],
             ["TDZ (thidiazuron)", "A very strong cytokinin. Use small doses."],
             ["Totipotency", "A cell of a plant can make a new plant with all its parts."],
             ["Vascular tissue", "Xylem (for water) and phloem (for sap). The viroid moves in the sap tubes."]],
            caption="Table 13. Glossary.",
        ),
    ]})

# ---------------------------------------------------------------------------
SECTIONS.append({
    "id": "map",
    "kicker": "03",
    "title": "Tissue culture procedure",
    "blocks": [
        lead("Each tissue culture batch has the same five stages. Cannabis has two more tasks. The first task is to cut the meristem. The disease then stays in the remaining tissue. The second task is a lab test. The test shows if the meristem cut removed the disease."),
        figure(F.fig_5stages(), 1, "Stage 0 is the mother plant that you cut. Stages I–IV are the work in the jar and the movement of the plant to a pot."),
        figure(F.fig_pipeline(), 2, "The figure shows the full sequence that this guide uses. The purple step is the meristem cut. The blue step is the disease test."),
        figure(F.fig_timeline(), 3, "The figure shows typical times for a new operator. The time to make a plant with roots in a pot is approximately 10–15 weeks. The time to make a plant with a negative test for Hop latent viroid is 5–8 months."),
        callout("key", "Two different results. Know the difference.",
                p("<strong>A plant with roots in a pot.</strong> The time is approximately 10–15 "
                  "weeks. You do not know that the plant has no disease.</p><p><strong>A mother "
                  "plant with a negative test for Hop latent viroid.</strong> For this result, you "
                  "do a meristem cut and a lab test. The time is 5–8 months. A kit that makes "
                  "plants only in jars cannot give the second result.")),
        photo_sequence(
            "Jars in good condition at each stage",
            [("Shoot multiplication", f"{IMG}/07-multiplication-shoots.jpg"),
             ("Roots in the gel", f"{IMG}/08-rooted-plantlet.jpg"),
             ("Plant in a plug in a dome", f"{IMG}/11-acclimatization.jpg")],
            "Left: green shoots on transparent amber gel. The gel has no mold. Middle: white roots that you can see in the gel. Right: plants in a humidity dome. If none of your jars is the same as the left photo, stop. Correct the contamination problem before you cut more mother plants.",
            model="Grok Imagine · illustration"),
    ]})

# ---------------------------------------------------------------------------
SECTIONS.append({
    "id": "why",
    "kicker": "04",
    "title": "When to use cannabis tissue culture",
    "blocks": [
        lead("A usual cutting is a copy of the plant. It is also a copy of each pest, fungus and viroid that the plant has. Tissue culture can make a new plant from tissue that does not contain those organisms."),
        figure(F.fig_hplvd(), 4, "Left: a plant without infection. Right: a plant with Hop latent viroid. At the start, the infection frequently has no symptoms that you can see. Thus the infection moves through a clone line for years before a person sees the symptoms."),
        p("Hop latent viroid (HpLVd or HLVd) is a small loop of RNA. It is 256 letters long. It has no protein coat. It is in plant cells and moves in the sap."),
        p("In 2021, an industry report gave the results of approximately 200,000 tissue tests. The "
          "report shows that approximately 90% of the facilities in California had some infection. "
          f"This figure is in frequent use.{_c("hlvd_threat2023")}</p><p>A report on licensed "
          "facilities in Canada gives the results of 15,947 samples from nine provinces. In total, "
          "25.6% of the samples were positive. The rates were different for each province and for "
          f"each year. They were from 5.3% to 92%.{_c("hlvd_mgmt2025")}</p><p>In plants with the "
          "infection, the height and the weight of the flowers were 12–42% less. The loss was "
          "different for each cultivar. No spray touches the viroid because the viroid is in the "
          "cells."),
        ul([
            "<strong>Less space.</strong> A rack of jars holds many plants. The same number of mother plants fills a room.",
            "<strong>The same plant each time.</strong> Cannabis seed has mixed genetics. A crop of medicinal cannabis flower must have the same female chemotype in each cycle. Tissue culture makes copies of one plant.",
            f"<strong>Plant health, not a new genotype.</strong> When you make cuttings from the same plants for many years, mutations and microbes increase.{_c("torkamaneh2024")} When you start from a meristem, you get the same genetics with a smaller number of mutations and microbes. It does not change the DNA.",
            "<strong>Storage and shipping.</strong> It is easier to move a jar, or a frozen shoot tip, than a mother plant of 1.5 m (5 ft). It is also easier to make a backup of a jar or a frozen shoot tip.",
        ]),
        callout("note", "Limits of “cleaning up genetics”",
                p("This procedure does not change the cultivar. It removes the diseases and pests "
                  "that the plant got. A plant with no disease can get the infection again from a "
                  "dirty blade or from a tray that other plants use.")),
    ]})

# ---------------------------------------------------------------------------
SECTIONS.append({
    "id": "anatomy",
    "kicker": "05",
    "title": "Shoot-tip anatomy",
    "blocks": [
        lead("Viroids and viruses move in the sap tubes. The meristem is a dome of cells that divide, at the tip of a shoot. At this stage, those cells do not have sap tubes. They divide faster than the pathogen can move forward. If you cut only that dome, it is possible that the piece does not contain the disease."),
        p(f"These data show how frequently a meristem cut removes the viroid. Punja (2025) cut meristems with a width of 0.2–0.4 mm (0.008–0.016 in) from 91 plants with infection, of 8 cultivars. At six months, 40.7% of the plants had a negative test for Hop latent viroid. The range for the different cultivars was 0% to 100%.{_c("hlvd_mgmt2025")} A meristem cut is a filter. It cannot make sure that the plant has no viroid."),
        photo(f"{IMG}/01-meristem-dome.jpg",
              "The photo shows the inner parts of a cannabis shoot tip. The pale dome in the center is the meristem. The first small leaves (leaf primordia) are around the dome. You cut this dome for disease removal.",
              alt="Photo of a cannabis meristem dome and leaf primordia",
              model="Grok Imagine · illustration"),
        figure(F.fig_meristem(), 5,
               "A shoot tip cut along its length. The red lines are sap tubes. The circle with a broken line is the meristem dome of 0.2–0.5 mm (0.008–0.020 in). There are no red lines in that circle."),
        figure(FP.fig_stem_xsec(), 6,
               "A new cannabis stem, cut across. The sap tubes are in a ring around the soft center (pith). Holmes (2021) found Penicillium in that pith. A stem piece with one bud includes all of this ring. A meristem dome does not."),
        figure(FP.fig_explant_size(), 7,
               "The figure shows three pieces that you can cut. A stem piece with one bud is easy to use and keeps the disease. A shoot tip of less than 5 mm (0.2 in) has a smaller number of internal microbes. Only the meristem dome can possibly give a piece that has no Hop latent viroid."),
        photo(f"{IMG}/04-nodal-explant.jpg",
              "A stem piece with one node, one bud and a short leaf stalk. Use this piece for your first batches. It makes a copy of the plant. It does not always remove the disease.",
              alt="Cannabis stem piece with one bud on sterilized paper",
              model="Grok Imagine · illustration"),
        callout("warn", "A plant with a negative test can get the disease again",
                p("Meristem culture can make a plant with a negative test for the viroid. It does "
                  "not make a plant that cannot get the infection again. The result “negative” is "
                  "correct only after a lab test (section 16).")),
        kv([
            ("Size of the meristem for disease removal", "A dome of 0.2–0.4 mm (0.008–0.016 in) with a maximum of two small leaves"),
            ("Holmes method", "Keep two small leaves on the tip. The leaves give protection from the bleach. Then apply bleach. Then put the tip on the medium."),
            ("Best first piece (Das 2024)", "A shoot tip of less than 5 mm (0.2 in). It has less fungus than stem pieces and less glassy growth than a bare meristem."),
            ("Frequency of contamination in stem pieces", "Approximately 50% in Holmes 2021 (range 10–80%), after a bleach treatment. The microbes are in the stem and not only on the surface."),
        ]),
    ]})

# ---------------------------------------------------------------------------
SECTIONS.append({
    "id": "home",
    "kicker": "06",
    "title": "Home laboratory setup",
    "blocks": [
        lead("You must have three items. The first item is an area with clean air that does not move. The second item is a device that sterilizes jars at 121 °C (250 °F). The third item is a warm shelf with light. A lab coat is not necessary. A hospital cabinet is not necessary."),
        photo(f"{IMG}/05-home-lab-sab.jpg",
              "The photo shows a home bench for the work. A transparent plastic container with two arm holes (a still-air box) is on its side. The bench also has alcohol spray, tools, jars, a pressure cooker to sterilize media, MS salt powder and a small LED. During the work, make sure that the fans and the air-conditioning are off. Keep pets away from the bench.",
              alt="Home still-air box and pressure cooker on a kitchen bench",
              model="Grok Imagine · illustration"),
        figure(F.fig_lab(), 8, "The figure shows the positions of the items in the still-air box. Open jars only in the center. Sterilize the tools again on one side. Put the waste on the other side. Do not move your hands above an open jar."),
        h(3, "Items to get"),
        table(
            ["Item", "Items that you assemble (approximately $200–550)", "Kit (Athena or Plant Cell Technology)"],
            [["Clean air", "A transparent storage container. Cut two arm holes in one side. Clean it with 70% alcohol. This item is a still-air box.", "A small laminar-flow hood with a HEPA filter (Athena kits include one)."],
             ["Sterilization of media", "A stovetop pressure canner that holds 15 psi for 20 minutes. An Instant Pot does not hold 121 °C.", "The Athena kit includes a small autoclave."],
             ["Medium", "MS powder, table sugar, agar and optional hormones (mT, IBA).", "SHOOTS and ROOTS sachets. Each sachet contains a mixture that the manufacturer made. The recipe is not available."],
             ["Added antimicrobial", "PPM, 0.5–2 mL for each liter of medium. Optional.", "The same, or “Cleanse” from the kit (hypochlorous acid)."],
             ["Jars", "Baby-food jars or Magenta vessels. Fill each jar to approximately one third.", "Jars from the kit. Some of the jars have filter vents."],
             ["A test that shows that the plant has no disease", "None at home. A lab can do a qPCR test. Use this test if you want to show that the plant has no disease. The test has a cost.", "The kit has no test. A lab can do a qPCR test. The test has a cost."]],
            caption="Table 1. Items for a home setup. A kit includes a laminar-flow hood and a powder that the manufacturer mixed. The kit does not change the biology.",
            foot="The street price of the Athena kit was approximately $1,800–2,295. The Plant Cell Technology starter kit is a smaller package of ingredients and vessels. Prices change.",
        ),
        callout("note", "A biosafety cabinet is not necessary",
                p("A biosafety cabinet keeps dangerous microbes away from the person. In this "
                  "procedure, you keep the microbes in the air of the kitchen away from the plant. "
                  "A still-air box or a laminar-flow hood is the correct tool.")),
        h(3, "The laminar-flow hood"),
        p("A fan pushes room air through a HEPA filter, and the filter removes more than 99% of the particles. Then the clean air blows in one sheet across the bench, to you or down. The direction is different for different hoods. Do the work in that sheet of air. Do not put objects in the sheet of air. Do not move your hands upstream of an open jar."),
        h(3, "Shelf settings"),
        table(
            ["Setting", "Target", "Information"],
            [["Temperature", "24–26 °C (75–79 °F)", "Holmes used 25 ± 2 °C (77 ± 4 °F). The range 21–27 °C (70–81 °F) is also satisfactory."],
             ["Day length", "16–18 hours of light", "The plants stay in vegetative growth. A light period of 12 hours will start the flowering stage."],
             ["Light level", "Approximately 70–100 µmol m⁻² s⁻¹ at the jar", "Holmes used 102. Kodym measured approximately 70 in the jar."],
             ["pH of the medium", "5.6–5.8 before you add agar and before you sterilize the medium", "Holmes set the pH to 6.6. After sterilization in an autoclave, the pH was approximately 5.8."],
             ["Wait after you put the medium in the jars", "7 days before you use a new batch of jars", "Microbes with a slow rate of growth show in that week."]],
            caption="Table 2. Conditions on the culture shelf.",
        ),
        callout("danger", "Fire risk. Alcohol does not kill Hop latent viroid.",
                p("If you use alcohol and a flame to sterilize tools, keep the open alcohol far "
                  "from the flame. A glass-bead sterilizer at approximately 250 °C (482 °F) for "
                  "approximately 20 seconds is safer in a plastic container. Punja (2025) found "
                  "that 70% ethanol does not break the RNA of Hop latent viroid. Household bleach "
                  "at 5–10% of 8.25% sodium hypochlorite breaks the RNA in 1–2 minutes. 1000 ppm "
                  "hypochlorous acid breaks the RNA in 1 minute. An Instant Pot is not an autoclave.")),
    ]})

# ---------------------------------------------------------------------------
SECTIONS.append({
    "id": "facility",
    "kicker": "07",
    "title": "Layout of a laboratory in a licensed facility",
    "blocks": [
        lead("A licensed lab does the same work on plants. It also keeps written records. It has a procedure for disease tests. It is not a larger still-air box in a kitchen."),
        photo(f"{IMG}/06-facility-lab.jpg",
              "The photo shows a transfer room. Filtered air comes from the ceiling. The room has two laminar-flow hoods. The operator is in a gown and gloves. There are racks of jars. Three items go out of this room: a plant, a batch number and a test result.",
              alt="Medicinal cannabis tissue-culture transfer room",
              model="Grok Imagine · illustration"),
        figure(FP.fig_home_vs_facility(), 9, "The figure compares a home setup and a licensed facility. The stages are the same. The air and the records are different. The condition for the term “clean” is also different."),
        figure(FP.fig_facility_flow(), 10, "Work and materials go from dirty areas to clean areas. Plants that come into the facility do not go through the transfer room. Discard the defective lots. Do not put them back in the grow room."),
        h(3, "Air ratings"),
        p("ISO 5 and ISO 7 are particle counts. ISO 5 has a smaller number of particles than ISO 7. In a plant lab, ISO 5 is the rating at the work surface of the laminar-flow hood. ISO 7 is a typical rating for the room around the hood.</p><p>Plant tissue culture is not a hospital sterile-fill suite. It is not a biosafety Level 2 lab. You keep microbes from the kitchen out of the medium. The cultures do not contain human pathogens."),
        h(3, "Information that inspectors want"),
        p("The standard for medicinal cannabis flower is usually GACP (Good Agricultural and Collection Practice). The standard for a product from manufacturing can be GMP (Good Manufacturing Practice). The tissue culture lab is between the two.</p><p>An inspector will want two items of information. The first item is how you know that this plant is the cultivar on the label. The second item is how you know that it does not have Hop latent viroid. Give the results of a test to identify the cultivar and of a pathogen test. The bleach procedure is not sufficient."),
        ul([
            "<strong>Air.</strong> Cut the pieces and put them on the medium in a laminar-flow hood. The room is usually ISO 7.",
            "<strong>Personnel.</strong> Put on a gown, a hair cover and gloves. Do not put on jewelry. Go in one direction, from dirty to clean. One person at one hood is one work unit.",
            "<strong>Lot numbers.</strong> Each autoclave load, each batch of medium and each period of cutting has a number for traceability.",
            "<strong>Quarantine.</strong> Mother plants that come into the facility stay in a quarantine room until you do a test of the plants. Discard a plant if its test result is unsatisfactory.",
            "<strong>Replace mother plants.</strong> Mutations increase when you cut the same in-vitro line again (Torkamaneh 2024). Start again from a backup with a negative test.",
        ]),
        photo(f"{IMG}/12-tis-bioreactor.jpg",
              "The photo shows temporary-immersion bottles. The liquid medium makes the shoots wet at times that a timer sets. Then the medium drains and the shoots get air. Use these bottles after your contamination rate is low. They increase the quantity of work, and they do not replace aseptic technique. Kodym and Leeb made cannabis plants on rockwool in jars with vents and with no sugar.",
              alt="Temporary-immersion bottles with cannabis shoots",
              model="Grok Imagine · illustration"),
        callout("tip", "When to get larger vessels",
                p("Get larger vessels after Stage I has no contamination. You must also have a "
                  "recipe that gives good results for that cultivar. In Kodym and Leeb (2019), "
                  "97.5% of the shoots made roots and hardened in 3 weeks on rockwool with no sugar "
                  "and no hormones. Do not get a bioreactor to correct a contamination rate of 60%.")),
    ]})

# ---------------------------------------------------------------------------
SECTIONS.append({
    "id": "aseptic",
    "kicker": "08",
    "title": "Aseptic technique",
    "blocks": [
        lead("Contamination causes most of the losses in a first batch. Contamination is almost always a problem of technique. It is not an accident."),
        figure(FX.fig_contam(), 11, "Bacteria cause a cloud in the gel. Fungi make white, green or black mold. Yeast makes colonies of a cream color. Internal microbes (endophytes) can stay in the tissue for two weeks. Then they come out of the cut stem and increase in number."),
        photo(f"{IMG}/09-contamination.jpg",
              "Left: slime from bacteria and a plant piece that the bacteria killed. Right: fungus in all of the air space of the jar. The two jars are defective. Do not open them in the hood that you continue to use for clean work. Seal the jars and put them in a bin.",
              alt="Contamination with bacteria next to contamination with fungi in culture jars",
              model="Grok Imagine · illustration"),
        steps([
            ("Clean the work area", "Clean the still-air box or the hood, and the bench, with 70% alcohol. Let the surfaces dry. If you use a still-air box, make sure that the fans and the air-conditioning are off."),
            ("Gloves", "Use new nitrile gloves. Spray them with 70% alcohol. Spray them again each time you remove a hand from the work area."),
            ("Put only necessary items in the area", "Put in the area only the jars, the tools and the plant pieces for this work. Objects that you do not use collect dust."),
            ("Sterilize the tools before you cut", "Use alcohol and then a flame, or use a glass-bead sterilizer at approximately 250 °C (482 °F) for approximately 20 seconds. Then let the tool become cool. A hot blade kills the plant tissue."),
            ("Open the lid only when you use the jar", "Go to the jar from the side. Do not move your hands above an open jar."),
            ("Wait seven days before you use a jar", "On day 2, you can see that a jar is clean. In week 2, the same jar can have microbes that increase in number. Frequently, internal microbes show at this time."),
        ]),
        callout("key", "A bleach treatment is not sufficient for stem pieces",
                p("Holmes (2021) used a full bleach protocol on stem pieces from mother plants of a "
                  "commercial grower. After the protocol, approximately half of the pieces had "
                  "fungi or bacteria. The microbes are in the pith. PPM at 2 mL/L stopped the "
                  "microbes for 1–3 weeks, but it did not remove them. The meristems had less "
                  "contamination. Thus section 11 gives the meristem procedure.")),
    ]})

# ---------------------------------------------------------------------------
SECTIONS.append({
    "id": "media",
    "kicker": "09",
    "title": "Make and sterilize the medium",
    "blocks": [
        lead("The medium contains mineral salts, sugar, vitamins, optional hormones and agar. First set the pH. Then add the agar. Sterilize the medium last. The light in the sealed jar is too dim for the plant to photosynthesize sufficiently. Thus the sugar is the source of energy."),
        figure(FP.fig_hormone(), 12, "Cytokinins cause the tissue to make shoots. Auxins cause it to make roots. Cannabis frequently gives better results with less hormone than the recipes for orchids. The difference is largest when you increase the number of shoots."),
        h(3, "Basic recipe for 1 liter (initiation or multiplication)"),
        table(
            ["Ingredient", "Quantity for each liter", "Function"],
            [["RO or distilled water", "Start with approximately 800 mL (27 fl oz). Then add water to 1 L (0.26 gal).", "The minerals in tap water change the recipe"],
             ["MS basal salts", "4.4 g (0.16 oz)", "The standard mineral mixture"],
             ["Sucrose (table sugar)", "30 g (1.1 oz)", "Energy"],
             ["myo-Inositol", "0.1 g (0.004 oz)", "Standard component"],
             ["Activated charcoal", "1 g (0.04 oz), optional", "Removes the brown compounds that flow out of the cut surface. Holmes used 1 g (0.04 oz)/L."],
             ["Agar", "6–8 g (0.21–0.28 oz). Use 9.5 g (0.34 oz) if the shoots have glassy growth.", "Makes the medium solid. A harder gel gives less water in the leaves."],
             ["PPM (optional)", "0.5–2 mL", "Decreases the rate of growth of some microbes. It does not replace aseptic technique."],
             ["pH", "5.6–5.8 before you add agar and before you sterilize the medium", "Holmes set the pH to 6.6. After sterilization, the pH was approximately 5.8."]],
            caption="Table 3. General cannabis medium. Use full-strength MS in the start stage and in the multiplication stage. Many rooting recipes use half-strength MS.",
        ),
        h(3, "Hormone quantities in reports on cannabis"),
        table(
            ["Stage", "Hormone", "Dose", "Source"],
            [["Start of the culture", "TDZ + NAA", "1 µM + 0.5 µM", "Lata 2009 / Holmes"],
             ["Start of the culture, with a weaker hormone", "meta-Topolin", "0.48 mg/L", "Das 2024, from Lata 2016"],
             ["Long-term multiplication", "None", "MS plus more calcium", "Das 2024 MM12. The medium gives less glassy growth."],
             ["More calcium", "Calcium nitrate + calcium gluconate", "0.71 g (0.025 oz)/L + 1.35 g (0.048 oz)/L", "Das 2024"],
             ["Roots in the jar", "IBA", "2.5–5 µM (approximately 0.5–1 mg/L)", "Holmes: 5 µM gave better results than 42 µM"],
             ["Roots, optional", "Sodium metasilicate", "6 mg/L", "Holmes: better leaves, and 40% of the pieces made roots"],
             ["Roots, optional", "Silver nitrate", "40 µM with IBA", "Holmes: more roots than with IBA only"],
             ["Roots in a plug, not in gel", "IBA dip", "15 mM for 2–4 minutes", "Ioannidis 2022, a maximum of approximately 100% rooting"]],
            caption="Table 4. Hormone doses for cannabis from reports. The cultivars are different. Start with these doses. Change one item each time.",
        ),
        callout("note", "MS or DKW",
                p("MS is Murashige and Skoog salts, the standard mixture. DKW is Driver and "
                  "Kuniyuki Walnut salts, a different mineral mixture.</p><p>Page (2021) found that "
                  "DKW gave plants in better condition than MS on some cultivars. Holmes found the "
                  "opposite on two cultivars. In Das (2024), the DKW cultures became brown and "
                  "died. Use MS until you get good results. Then try DKW in one test.")),
        steps([
            ("Mix the salts and the sugar", "Use approximately 800 mL of RO or distilled water. Mix until the powder is in solution. Add the vitamins, the charcoal and the PPM if you use them."),
            ("Set pH", "Set the pH to 5.6–5.8 <strong>before</strong> you add agar. A drop of acid solution with a low concentration decreases the pH. A drop of alkaline solution with a low concentration increases the pH."),
            ("Add agar and make the medium hot until the agar is in solution", "Put the medium in the jars. Fill each jar to approximately one third."),
            ("Sterilize with heat", "Sterilize at 121 °C (250 °F) and 15 psi for 20 minutes. In a pressure cooker, use the same numbers. Put the jars on a rack. The jars must not be in a large quantity of water."),
            ("Let the jars become cool", "You can put the jars at an angle while they become cool. Then it is easier to put the explant on the surface of the gel. Keep the new jars for 7 days. If they stay transparent and have no contamination, use them."),
        ]),
    ]})

# ---------------------------------------------------------------------------
SECTIONS.append({
    "id": "sterile",
    "kicker": "10",
    "title": "Surface sterilization of the explant",
    "blocks": [
        lead("Surface sterilization kills microbes on the outer surface of the plant. It cannot touch microbes that are in the stem. Use a time that is sufficient to kill the microbes on the surface. A time that is too long kills the plant tissue."),
        figure(F.fig_sterilize(), 13, "The figure shows the sequence. From the alcohol step, do the work in the still-air box or in the hood with sterilized tools. Woody tissue or dirty tissue must stay in the bleach for a longer time. Soft new growth must stay for a shorter time."),
        h(3, "Procedure for stem pieces and shoot tips from a mother plant"),
        steps([
            ("Prepare the mother plant (Stage 0)", "Keep the mother plant in vegetative growth, and monitor it for pests. Use a new plant in a substrate that is clean. Holmes found that plants in coco that were not new were dirtier. On one cultivar, a systemic fungicide (fluopyram, Luna) decreased the contamination from 88% to 32%. We do not recommend that you apply the fungicide to all plants. This result shows that the condition of the mother plant is important."),
            ("Cut in the morning", "Cut shoot tips or stem pieces. Each piece must be 10–15 mm (0.4–0.6 in) long. Remove the large leaves. Keep the pieces wet and cool."),
            ("Clean with soap and water", "Use tap water that flows, with a drop of dish soap or Tween-20. Do this for 10–20 minutes. The soap loosens the film that holds the microbes."),
            ("70% ethanol", "Keep the pieces in the ethanol for 30–60 seconds. A longer time causes damage to cannabis tissue."),
            ("Bleach", "Holmes used 10% household bleach (approximately 0.625% sodium hypochlorite) with 0.1% Tween-20 for 20 minutes. Mix the solution during this time. In Das (2024), 1% sodium hypochlorite for 30 minutes gave 55% of pieces that you can use. A time of 10 minutes gave 100% dirty pieces. A time of 60 minutes killed 100% of the pieces."),
            ("Clean three times with sterilized water", "Keep the pieces in sterilized water for 3–5 minutes each time. Then, in the hood, remove the ends that the bleach touched. Put the piece on the gel."),
        ]),
        table(
            ["Source", "Sodium hypochlorite", "Time", "Notes"],
            [["Holmes 2021", "0.625% (10% household bleach)", "20 min", "With 1 minute of 70% ethanol. Approximately half of the stem pieces had contamination after this treatment."],
             ["Das 2024", "1%", "30 min", "The best rate of pieces that you can use in that test. Carbendazim caused more plants to die."],
             ["Kodym 2019", "0.5%", "20 min", "Then clean three times with sterilized water, 10 minutes each time."],
             ["General blog of Plant Cell Technology", "10–20% bleach", "10–20 min", "The blog is not for cannabis. Start with a weaker bleach solution."],
             ["Plant Cell Technology, calcium hypochlorite", "3.25%", "Not specified", "It causes less damage than sodium hypochlorite on some tissues."]],
            caption="Table 5. Bleach conditions from reports. Record the values that you used. In the next batch, change one number.",
        ),
        callout("warn", "PPM is not a bleach treatment",
                p("The label of Plant Cell Technology gives <strong>0.05–0.2%</strong> (0.5–2 mL/L) "
                  "in the medium. The rate is for usual microbes in the air and in water. You can "
                  "sterilize the PPM with the medium in an autoclave.</p><p>For microbes that are "
                  "in the plant, the label gives a different procedure. Shake the pieces for 4–12 "
                  "hours in 4–5% PPM with MS salts at three times the strength. Then put the pieces "
                  "on a medium with 0.05–0.2% PPM.</p><p>In the tests of Holmes, 2 mL/L stopped the "
                  "contaminants for 1–3 weeks. Then the contaminants showed. PPM gives more "
                  "protection. It does not replace a meristem cut.")),
    ]})

# ---------------------------------------------------------------------------
SECTIONS.append({
    "id": "initiate",
    "kicker": "11",
    "title": "Stage I: start of the first culture",
    "blocks": [
        lead("Use one plant piece in each jar. The task for this month is a culture that has no contamination and makes new growth. The task is not a tray of plants."),
        p("Holmes made shoots from meristems and from stem pieces. The medium was MS with 1 µM TDZ, "
          "0.5 µM NAA and 1 g/L charcoal. The meristems were slower (the measurement was at 10 "
          "weeks) and had less contamination. The stem pieces were faster (the measurement was at 6 "
          "weeks) and were dirtier.</p><p>The result was different for each cultivar. The average "
          "length for Moby Dick meristems was 4.5 cm. The growth of Space Queen was low."
          f"{_c("holmes2021")}"),
        p("Das (2024) got the best start on MS with 0.48 mg/L meta-Topolin. Shoot tips of less than "
          "5 mm had less contamination than full shoot tips or stem pieces. They also had less "
          f"glassy growth than bare meristems.{_c("das2024")}"),
        steps([
            ("Put the piece in the medium", "Put the piece in the gel. The cut bottom end must be in the gel and the bud must be above the gel. Use one piece for each jar until you know the rate of good results."),
            ("Close the jar and put a label on it", "Write the cultivar, the date, the medium and the type of piece on the label. Put the lid on the jar immediately."),
            ("Shelf", "Use 24–26 °C (75–79 °F), 16–18 hours of light and approximately 100 µmol. Do not open the jar each day to examine the culture."),
            ("Discard defective jars quickly", "If the gel has a cloud, mold or an unusual odor, seal the jar in a bag. Put the bag in a bin. Do not open the jar in the clean hood."),
            ("Move the good cultures", "At 3–4 weeks, move the clean growth to new medium. Das found that Stage I recipes gave glassy growth after 2–3 moves. Change to the Stage II recipe in section 12."),
        ]),
        callout("tip", "Wait one week before you cut pieces from a new jar",
                p("A jar that you can see is clean on day 7 can have microbes in week 3. Do not cut new pieces from a culture in the first week.")),
    ]})

# ---------------------------------------------------------------------------
SECTIONS.append({
    "id": "meristem",
    "kicker": "12",
    "title": "Meristem dissection to remove pathogens",
    "blocks": [
        lead("With the meristem cut, it is most possible that the piece does not contain Hop latent viroid. You must have a stereo microscope. First, do stem-piece cultures for two months. In this time, your aseptic technique becomes correct."),
        figure(FP.fig_meristem_size(), 14, "The piece for disease removal is 0.2–0.4 mm (0.008–0.016 in). This size is much smaller than a grain of rice. You cannot do this procedure with only your eyes."),
        h(3, "Prepare the bench first"),
        figure(FP.fig_meristem_setup(), 15, "The figure shows five zones. The microscope and the dish are in the middle. The tools are on the left and the closed jars are on the right. The waste is on the left at the front. You are at the front and the air comes from the rear."),
        photo(f"{IMG}/15-meristem-hood.jpg",
              "The photo shows the layout of a hood. The microscope is in the center, and the black dish is below the lens. The scalpel is on the left, and the forceps are on a wipe. The glass-bead sterilizer is at the rear on the right, and the spray bottle is at the rear on the left. The closed jars are on the right. The piece on the dish must be a green shoot tip and not a piece of waste.",
              alt="Laminar-flow hood prepared for a meristem cut",
              model="Grok Imagine · illustration"),
        h(3, "Tools"),
        figure(FP.fig_meristem_tools(), 16, "The figure shows the tools: a microscope, small forceps, a #11 scalpel, a black dish, a glass-bead sterilizer and 70% alcohol. No other items are on the bench."),
        photo(f"{IMG}/14-meristem-tools.jpg",
              "The photo shows the same items. The items are a stereo microscope, two pairs of small forceps, a #11 scalpel, a black dish, a glass-bead sterilizer and an alcohol spray. Do not use a kitchen knife. Do not use tweezers from a first-aid kit.",
              alt="Meristem tools on a dark mat",
              model="Grok Imagine · illustration"),
        h(3, "Hands"),
        figure(FP.fig_meristem_hands(), 17, "The left hand holds. The right hand cuts. Do not change hands. Put the two wrists on the bench. Then the tools do not shake."),
        photo(f"{IMG}/16-meristem-hands.jpg",
              "The left forceps hold the stem. The right scalpel removes a leaf from the tip. Do the work at the microscope with the ring light. Put the leaves that you remove to the side. The shoot in this photo is larger than the meristem that you put in the jar. The positions of the hands are the same when the piece is 1 mm.",
              alt="Forceps and scalpel that remove leaves from a cannabis shoot tip",
              model="Grok Imagine · illustration"),
        h(3, "The eight movements"),
        figure(FP.fig_meristem_sequence(), 18, "Do these steps in sequence. Do not cut before you do all these steps. If you continue to see green outer leaves, continue to remove the leaves."),
        figure(FP.fig_meristem_scope(), 19, "Stop when you can see a pale dome with two small leaves. At this stage, you apply bleach and then cut. If you remove those last two leaves, the dome frequently dies."),
        photo(f"{IMG}/17-meristem-dome-cut.jpg",
              "The correct result after you remove the leaves is a pale dome and two remaining small leaves. Hold the stem at the bottom with forceps. Cut below the dome. The piece for the jar is 0.2–0.4 mm (0.008–0.016 in), as in Punja (2025).",
              alt="Cannabis meristem dome, two leaf primordia, leaves removed",
              model="Grok Imagine · illustration"),
        figure(FX.fig_hlvd_clearance(), 20, "You can use the term “Tested, not detected” after this procedure. The terms “Virus-free” and “resistant” are not accurate."),
        h(3, "Do the steps in this sequence"),
        steps([
            ("Start with new growth", "In the morning, cut a tip of 10–15 mm (0.4–0.6 in) from a vegetative shoot. Remove the large leaves before you go to the hood. Use new growth. Reports show heat treatments of the mother plant. The rate of removal of the viroid is from 0% to 94% for the different cultivars. Do not use a temperature from a blog."),
            ("Sterilize the tools", "Use the glass-bead sterilizer at approximately 250 °C (482 °F) for 20 seconds. Then let the tools become cool. Or use alcohol and then a flame, and then let the tools become cool. A hot blade kills the dome."),
            ("Dish at the microscope", "Put one drop of sterilized water on the black dish. Put one tip on the drop. First, adjust the microscope at 10–20×. Then go to 30–40×."),
            ("Left forceps, 3–5 mm (0.1–0.2 in) down the stem", "Point the tip up. Put the wrist on the bench. Do not apply force to the dome."),
            ("Remove the outer leaves with the #11 blade", "Hold the blade almost flat. Move the blade below the leaf. Move the leaf away. Sterilize the blade again after you remove some leaves."),
            ("Stop at two small leaves", "Holmes kept two leaf primordia as a protection from the bleach. At this stage, you can see a pale dome. If you see only green, continue to remove leaves."),
            ("Sterilize the surface of that small tip", "Use the same bleach sequence as in section 09, but use a shorter time if the tissue is pale. Then clean the tip in sterilized water."),
            ("One nick below the dome", "The piece is 0.2–0.4 mm (0.008–0.016 in). Cut one time. Do not cut many times. Lift the piece with forceps or a sterilized needle."),
            ("Put it on the gel", "Put the cut bottom end in the gel. Put the lid on the jar immediately. Write the cultivar, the date and “meristem” on the label. The piece becomes a plant in 4–8 weeks. Holmes used MS + 1 µM TDZ + 0.5 µM NAA + 1 g (0.04 oz)/L charcoal."),
            ("Then test it", "Section 16 gives the procedure for the test. One negative test on a plantlet of 1 cm (0.4 in) is a start. Do a test again after the plantlet makes new leaves. Approximately 41% of the plants have a negative test at six months, and not 100%."),
        ]),
        kv([
            ("If the plant continues to have a positive test", "You kept sap tubes on the piece. Next time, remove more leaves or cut a smaller piece."),
            ("If the piece becomes brown and dies", "The piece was too small, the blade was hot, or the bleach time was too long. Cut a tip that is larger by a small quantity. Let it make growth. Then cut it again."),
            ("If fungus shows in week 2", "The piece had pith. Start again from a new shoot."),
        ]),
        callout("danger", "Do not use “clean” for a meristem plant without a test",
                p("A stem-piece culture does not remove pathogens that are in the plant. If you did "
                  "not send a sample to a lab, you made a clone in a jar.")),
    ]})

# ---------------------------------------------------------------------------
SECTIONS.append({
    "id": "multiply",
    "kicker": "13",
    "title": "Stage II: multiplication of shoots",
    "blocks": [
        lead("The task of this stage is to get more shoots from one clean culture. Cannabis frequently gives better results as one primary shoot in good condition that you cut again. It gives worse results as a group of leaves with glassy growth that hormones cause."),
        photo(f"{IMG}/07-multiplication-shoots.jpg",
              "The photo shows a Stage II jar in good condition. It has green leaves with leaflets, condensation on the glass and amber gel. The gel has no cloud and no mold. If the leaves are wet, transparent and break easily, the culture has glassy growth (hyperhydricity). Use less cytokinin, more agar and a lid with a filter vent.",
              alt="Cannabis shoots in good condition on agar",
              model="Grok Imagine · illustration"),
        figure(FX.fig_subculture(), 21, "Move plants to new medium at intervals of 3–4 weeks. Mutations increase with the number of subcultures (Torkamaneh 2024). Keep a backup from the first subcultures."),
        p("Das (2024) did not add meta-Topolin in Stage II because 0.5 mg/L increased glassy "
          "growth. The best medium in that test was MS with no hormone, more calcium nitrate, more "
          "calcium gluconate and 9.5 g (0.34 oz)/L agar. Shoot tips gave better results than stem "
          "pieces. For eight cultivars, the number of new pieces that you can use from each plant "
          f"was from 1 to 6.{_c("das2024")}"),
        p("Lata (2016) used meta-Topolin to make many shoots at the same time. This method gives good results. If you keep the plants on meta-Topolin for months, the plants have glassy growth. Use meta-Topolin to increase the number of shoots. Then move the line to the Stage II medium with less hormone."),
        steps([
            ("Cut", "Use a clean Stage I plant. Cut a shoot tip of 15–25 mm (0.6–1.0 in), or a stem piece with a bud that you can see."),
            ("New jar", "Use the same medium or the Stage II medium with less hormone. Do not use a jar again."),
            ("Number of pieces for each jar", "Home: 1–3 pieces. Facility: as many pieces as your contamination rate lets you use."),
            ("Time", "The time is 3–4 weeks. If the growth stops, do a check of the pH and of the charcoal (it can remove hormones). It is also possible that this cultivar does not give good results on the medium."),
        ]),
        callout("warn", "Changes in the genetics increase",
                p("Torkamaneh (2024) shows that, in cannabis from tissue culture, mutations "
                  f"increase when you cut the line again more times.{_c("torkamaneh2024")} Do not "
                  "operate production for years from one in-vitro generation. Start again from a "
                  "mother plant with a negative test.")),
    ]})

# ---------------------------------------------------------------------------
SECTIONS.append({
    "id": "root",
    "kicker": "14",
    "title": "Stage III: rooting",
    "blocks": [
        lead("A shoot with no roots is not a plant that you can put in a pot. Rooting is a different step."),
        photo(f"{IMG}/08-rooted-plantlet.jpg",
              "The correct result is white roots with branches that you can see in the gel. The shoot is short and green. There is no brown ring around the bottom. Some stem pieces make roots without a treatment. Do not wait more than five weeks for this.",
              alt="Cannabis plantlet with roots in agar",
              model="Grok Imagine · illustration"),
        h(3, "Four methods from reports"),
        table(
            ["Method", "Procedure", "Result from reports", "Source"],
            [["IBA in the gel", "Half-strength or full-strength MS, 5 µM IBA, 4 weeks", "83% of the pieces made roots at 5 µM, compared with 44% on the shoot medium. 42 µM gave worse results.", "Holmes 2021"],
             ["Silicate or silver", "Sodium metasilicate 6 mg/L, or silver nitrate 40 µM with IBA", "Better leaf shape. More roots.", "Holmes 2021"],
             ["IBA dip, then a plug", "Put the cut bottom end in 15 mM IBA for 2–4 minutes. Then put the piece in a peat sponge or in rockwool.", "A maximum of 100% rooting. The establishment in the field was approximately 95%.", "Ioannidis 2022"],
             ["No sugar, more air", "Rockwool, usual cannabis fertilizer, jars with vents, no sugar, no hormones", "97.5% made roots and hardened in 3 weeks. The survival in the glasshouse was 100%.", "Kodym and Leeb 2019"]],
            caption="Table 6. Rooting methods. Less sugar gives a smaller number of microbes and a shorter hardening time. Thus facilities frequently do not use gel for this step.",
        ),
        p(f"You can remove a shoot from the jar and put it in a plug with rooting hormone. This procedure is the same as for a usual cutting. It is not necessary to make the roots in the gel.{_c("kurtz2022")}"),
        steps([
            ("Select a shoot", "The shoot must be 2–4 cm (0.8–1.6 in) long. It must not have glassy growth. It must not have browning."),
            ("Select a method", "Home: use IBA in the gel, or do an IBA dip and put the shoot in a sterilized plug. Facility: do an IBA dip and put the shoot in a plug. Or use the no-sugar method with jars with vents."),
            ("Wait", "Roots show in 2–4 weeks. If there are no roots at week 5, cut the bottom end again and use less IBA. More hormone does not always give better results."),
            ("Move it", "If the roots are in gel, remove the gel from the roots with sterilized water. If the roots are in a peat sponge or a cube, put that item in the substrate."),
        ]),
    ]})

# ---------------------------------------------------------------------------
SECTIONS.append({
    "id": "harden",
    "kicker": "15",
    "title": "Stage IV: movement of the plant out of the jar",
    "blocks": [
        lead("In the jar, the humidity of the air is almost 100%. The surface of the leaves is thin, with no layer of wax. If you move the plant directly to the air of the bench, the water in the leaves decreases faster than the roots can supply it. Hardening (acclimatization) is the procedure to decrease the humidity gradually. Then the leaf has time to make a protective layer on its surface while it has moisture."),
        photo(f"{IMG}/11-acclimatization.jpg",
              "The photo shows plantlets in plugs in a transparent dome. Drops of water on the plastic are usual. Open the vents gradually during 7–10 days. Then remove the lid.",
              alt="Cannabis tissue-culture plants in hardening, in a humidity dome",
              model="Grok Imagine · illustration"),
        figure(F.fig_acclim(), 22, "Decrease the humidity in steps. Sudden dry air causes wilt in the leaves in one night."),
        table(
            ["Plug or cube", "Survival in Holmes (cultivar Moby Dick)", "Notes"],
            [["Rockwool cubes", "83%", "The plants were the strongest"],
             ["Peat plugs", "76%", "Das (2024): in coco plugs, the survival was 16 of 18 plants (90%)"],
             ["Hydro cloner", "57%", "This method is satisfactory. It has the smallest tolerance for errors."]],
            caption="Table 7. Holmes 2021, approximately 20 plants for each substrate. The statistics show that the three rates are the same. Kodym’s no-sugar method: the survival in the glasshouse was 100% after a ramp of 5 days with the lid off.",
        ),
        steps([
            ("Soak the plug first", "Use a weak nutrient solution for vegetative growth, at approximately pH 5.8. Use rockwool or coco. Do not use heavy soil for pots."),
            ("Put on the dome", "Spray water on the walls of the dome and not on the tops of the plants. Use 16 hours of light, with a low light intensity, at 24 °C (75 °F)."),
            ("Open the vents", "Day 7: open the vents to half. Day 9: open the vents fully. Day 14: remove the lid. Kodym: put the lids on the jars with the top of each lid down, for 3 days. Then remove the lids for 2 days, in low light."),
            ("Then use the same procedure as for a new clone", "Do not change it to 12 hours of light for some weeks."),
        ]),
        callout("tip", "If you made roots with no sugar",
                p("A plant that made roots on rockwool with no sugar has a thicker leaf surface and "
                  "good roots. The time for hardening is a small number of days and not two weeks.")),
    ]})

# ---------------------------------------------------------------------------
SECTIONS.append({
    "id": "fail",
    "kicker": "16",
    "title": "Symptoms of a defective culture",
    "blocks": [
        lead("Most problems are one of four types. Compare the jar with the photos. Change one variable. Do the batch again."),
        photo(f"{IMG}/09-contamination.jpg",
              "Contamination. Left: bacteria. Right: fungus. Seal the jar and put it in a bin. Do not smell the jar. Do not try to keep the plant piece.",
              alt="Cannabis jars with contamination",
              model="Grok Imagine · illustration"),
        photo(f"{IMG}/10-phenolic-browning.jpg",
              "Browning: brown compounds flow out of the cut surface and cause a ring of stain in the gel, and cannabis frequently has this problem. Add 1 g/L charcoal. Or move the piece to new medium after a shorter time. Or make a smaller cut surface. Or do a dip in an antioxidant (PVP or ascorbic acid). If all of the piece is brown, the piece died.",
              alt="Brown ring in agar around a cannabis explant",
              model="Grok Imagine · illustration"),
        photo(f"{IMG}/13-hyperhydricity.jpg",
              "Glassy growth (hyperhydricity): the leaves are wet, transparent and break easily. The gel is too soft and the air in the jar is too wet. Use less cytokinin and more agar (a maximum of 9.5 g/L). Use a lid with a filter vent. Do not increase the number of these cultures. They frequently die when you move them to a pot.",
              alt="Cannabis shoots with glassy growth",
              model="Grok Imagine · illustration"),
        table(
            ["Symptom", "Name", "Correction"],
            [["Cloud in the gel, slime, unusual odor", "Bacteria, frequently from the inner tissue of the stem", "Put the jar in a bin. In the next batch: use a new mother plant, a meristem or a small shoot tip, and an optional treatment with PPM. Do the work more slowly."],
             ["White, green or black mold", "Fungi", "Put the jar in a bin. Holmes found these in the pith. Change the substrate of the mother plant."],
             ["Brown ring, tan plant piece", "Phenolics (browning)", "Charcoal, move after a shorter time, 48 hours in darkness, antioxidant dip."],
             ["Transparent leaves that are wet and break easily", "Hyperhydricity", "Less cytokinin, 9.5 g/L agar, a lid with a vent, the Stage II medium of Das with no hormone."],
             ["No growth, pale, no roots", "Cultivar that is not compatible with the medium, or expired medium", "Try 5 µM IBA or 6 mg/L silicate. Or try DKW one time."],
             ["The jar is in good condition for 18 days. Then microbes show.", "Internal microbes (endophytes)", "Frequent in cannabis. Cut a meristem, or accept some losses."]],
            caption="Table 8. Compare the jar with the photos. Change one item in each batch.",
        ),
        callout("key", "Survival in the first stage: losses are usual",
                p("In Das (2024), 45–95% of the first pieces were defective. The result was "
                  "different for each cultivar. One hemp line kept approximately 75% of the pieces. "
                  "In Holmes, a maximum of half of the stem pieces had contamination. A result of "
                  "40% of the pieces of a new cultivar with growth and no contamination is good for "
                  "the first week.")),
    ]})

# ---------------------------------------------------------------------------
SECTIONS.append({
    "id": "index",
    "kicker": "17",
    "title": "Tests for pathogens in stock plants",
    "blocks": [
        lead("A meristem plant without a test is a clone. Licensed facilities send a test report with the plants. If you do not do the tests in this section, do not use the term “clean” for the plant."),
        figure(FX.fig_hlvd_clearance(), 23, "The figure shows the sequence. Do a meristem cut. Let the plant make new leaves. Send a sample for qPCR. Keep a frozen backup sample. After one month in the nursery, do a test again."),
        p("qPCR (and RT-qPCR) is a lab test to find the RNA of the viroid. “Not detected” shows that the test did not find the RNA in that sample. It does not show that the plant cannot get the viroid after the test. It also does not show that the test finds a low quantity of viroid."),
        table(
            ["Pathogen", "Type", "Removal with tissue culture", "Test method"],
            [["Hop latent viroid (HpLVd)", "Viroid, 256-letter RNA", "Punja 2025: 40.7% negative at 6 months (0–100% for different cultivars)", "RT-qPCR. Roots are the most accurate sample."],
             ["Other viroids", "Viroid", "Same method. Less data for cannabis.", "RT-qPCR panel"],
             ["Lettuce chlorosis, CMV, AMV", "Virus", "Frequently, if you cut a meristem. Do a test to make sure.", "RT-qPCR or ELISA"],
             ["Fusarium and Penicillium in the stem", "Fungus in the pith", "A meristem usually removes it. Stem pieces usually do not.", "Culture plus DNA test"],
             ["Broad mites, russet mites, powdery mildew", "Surface pests or surface fungus", "Yes. These organisms die in a sealed jar.", "Monitor the mother plant. Tissue culture is optional. It is not necessary."],
             ["Hop latent viroid in seed", "The viroid goes from the parent to the seed", "Cut a meristem from the seedling. Then do a test.", "Reports show seed transmission. Think that the seed of a parent with infection has the infection until you do a test."]],
            caption="Table 9. Pathogens that tissue culture can remove. “Tested, not detected” is the accurate term. “Virus-free” is not accurate.",
        ),
        steps([
            ("Select the correct tissue for the sample", "Use a new leaf of full size, or the leaf stalk. The plant must make new growth after the meristem cut. A meristem of 5 mm (0.2 in) does not have sufficient tissue for a test."),
            ("Use a lab that does cannabis tests for Hop latent viroid", "Use a plant health lab or a cannabis diagnostic lab. Strip tests for home use only give a first check. They are not release tests."),
            ("Do a test again", "Do the test after 3–4 weeks in the nursery. Do it again before you use a mother plant for production. The quantity of viroid is not the same in all parts of the plant. This difference can cause a false negative."),
            ("Keep a backup sample", "Freeze tissue from each lot with a negative test. If a flower room shows “dudding” at a subsequent time, you can do a test of the backup sample. Then you know if the liner was positive at the start."),
        ]),
        callout("warn", "A clean plant near a dirty plant will not stay clean",
                p("Hop latent viroid stays on tools, hands, pots and benches. It stays for "
                  "approximately one week in sap and approximately one month in dry tissue. It can "
                  f"move to the seed.{_c("hlvd_mgmt2025")}</p><p>Use dedicated blades. Disinfect "
                  "with 5–10% household bleach or 1000 ppm hypochlorous acid. Do not use 70% "
                  "alcohol. Do not use the same tray for different plants.")),
    ]})

# ---------------------------------------------------------------------------
SECTIONS.append({
    "id": "ppm",
    "kicker": "18",
    "title": "Plant Preservative Mixture (PPM) and commercial kits",
    "blocks": [
        lead("PPM (Plant Preservative Mixture) is the antimicrobial that most forums for cannabis tissue culture refer to. The rates in this section are from the label. They are not estimates from forums."),
        table(
            ["Task", "Plant Cell Technology label", "Result of Holmes on cannabis"],
            [["In the medium, for usual work", "0.05–0.2% (0.5–2 mL/L). Sterilize it with the medium in an autoclave.", "2 mL/L stopped microbes for 1–3 weeks"],
             ["Work with callus", "0.05–0.075%", "This guide does not give a procedure for this task"],
             ["Microbes in the plant", "4–12 hours in 4–5% PPM with MS salts at three times the strength. Then put the pieces on a medium with 0.05–0.2% PPM.", "When the pieces stayed 4 hours in 5% PPM, the result was not better than bleach on one cultivar"],
             ["Woody plants with a large quantity of microbes", "Put the pieces on a medium with 0.2%", "Cannabis does not have woody tissue. Start at 1–2 mL/L"]],
            caption="Table 10. PPM (Plant Cell Technology). It is stable in heat. The manufacturer gives information that PPM does not change the genetics of the plant. It does not replace a meristem cut.",
        ),
        ul([
            "The cannabis articles of Plant Cell Technology refer to Lata 2016, Monthony 2021 and Ioannidis 2022. Those papers are the correct sources. The articles do not give a full recipe for cannabis.",
            "Their article about plants with no disease is correct on one point: use meristems for pathogens in the plant. Use stem pieces for surface pests and to make more plants.",
            "Their article about a home lab includes a recipe of fertilizer and vitamin tablets. The recipe is for houseplants. Do not use that recipe for cannabis. Use Table 3.",
            "BioCoupler / BioTilt is a small temporary-immersion bottle. Use it after the contamination is low.",
            "The Athena Culture Kit includes a laminar-flow hood, a small autoclave and SHOOTS and ROOTS mixtures that the manufacturer made. It is easy to use. The recipe is not available. Thus you cannot adjust the hormone when a cultivar has glassy growth. The kit does not include a disease test.",
        ]),
        figure(FX.fig_athena_kit(), 24, "The figure shows the items in a typical kit for growers. It also shows the items that the kit does not include: the recipe and the disease test."),
    ]})

# ---------------------------------------------------------------------------
SECTIONS.append({
    "id": "facility-run",
    "kicker": "19",
    "title": "Tissue culture operations for each week",
    "blocks": [
        lead("The number of plants that you send is your contamination rate multiplied by the hours at the hood. Correct the contamination rate before you get more personnel."),
        table(
            ["Day", "Home bench", "Licensed lab"],
            [["Monday", "Clean the still-air box. Put the medium that you sterilized on Sunday in the jars.", "Media kitchen: lot number, pH log and the record from the autoclave."],
             ["Tuesday", "Start 10–20 stem pieces of one cultivar.", "Start cultures only from mother plants that are in quarantine and have a test result."],
             ["Wednesday", "Move the clean jars of the last month to new medium.", "Two persons, two hoods, one cultivar for each hood in each work period."],
             ["Thursday", "Examine each jar. Discard each jar that you are not sure about.", "Walk through the grow room. Remove plants that are not the cultivar. Record each lot with a photo."],
             ["Friday", "Make roots on the largest clean shoots, or do an IBA dip and put them in plugs.", "Send the qPCR samples of the week. Put the plants with a positive test in quarantine. Release the plants with a negative test to the nursery."],
             ["Saturday–Sunday", "Do not open jars to examine them.", "Personnel come to the lab only for alarms of the air-handling system and of the incubator."]],
            caption="Table 11. A usual week.",
        ),
        ul([
            "Use a value of approximately <strong>80–100 transfers for each person in each hour</strong> at a hood. Sluis and Plant Cell Technology use this training figure. Do not use 1,500–2,000 transfers each day to calculate the number of personnel. That number is from sales and is too high.",
            "Ioannidis (2022): 500–600 plants with roots for each square meter of shelf, cycle of 3–4 weeks, peat sponges.",
            "Do a test of the production mother plants at intervals of <strong>3–6 weeks</strong>. A meristem plant does not have a certificate for the full life of the plant.",
            "Reports give some data on costs. When a line is clean, the cost is approximately <strong>USD 0.50–1 for each liner</strong>. The first removal of disease from a dirty cultivar is approximately <strong>USD 2,000–5,000</strong>. The total cost of a lab is different for each site. Do not use “$50,000” from a blog as a value for your cost.",
            "Kodym kept stock plants for a minimum of 6 months in jars of 1.5–2 L (0.4–0.5 gal) with vents, with tipping many times.",
            "Mutations increase with the number of subcultures. Start a production line again after a maximum of approximately <strong>five cycles</strong>, from a backup with a negative test. Keep a backup that is frozen or has slow growth (Uchendu 2019 droplet-vitrification).",
        ]),
        callout("key", "Mother plants and tissue culture together",
                p("Keep a small block of mother plants with a negative test. Use them for new "
                  "cuttings and for tests of the cannabinoid content. Use tissue culture to replace "
                  "the plants of that block. Use it also to make the plants that you send to the "
                  "flower room.</p><p>A lab that discards all mother plants and has cultures only "
                  "on agar will have drift. The lab will not see the drift until the flowering "
                  "stage. A facility that does not use tissue culture will, after some time, have "
                  "Hop latent viroid in the clone line.")),
    ]})

# ---------------------------------------------------------------------------
SECTIONS.append({
    "id": "trouble",
    "kicker": "20",
    "title": "Troubleshooting",
    "blocks": [
        table(
            ["Symptom", "Possible cause", "Change only this item"],
            [["More than 50% of the jars are dirty at day 7", "Technique or a dirty mother plant", "Do the work more slowly. Use a new plant. Use a smaller shoot tip or a meristem."],
             ["More than 50% dirty after day 14", "Microbes in the stem", "Use a meristem. Optional: keep the pieces for 4–12 hours in 4–5% PPM. Change the substrate of the mother plant."],
             ["Pieces become brown in 48 hours", "Browning with damage from bleach", "Use a shorter bleach time. Add charcoal. Cut the ends. Keep the pieces 48 hours in darkness."],
             ["Shoots with glassy growth", "Too much cytokinin or too much water", "Use no hormone in Stage II. Use 9.5 g (0.34 oz)/L agar. Use a lid with a vent."],
             ["No shoots on a new cultivar", "That cultivar does not give good results on this medium", "Try MS + 0.48 mg/L meta-Topolin, or the TDZ+NAA mixture of Holmes. Then try DKW one time."],
             ["Shoots, no roots", "Incorrect auxin quantity", "Use 5 µM IBA, or a dip of 15 mM for 2–4 minutes, or the no-sugar method."],
             ["The plant makes roots, then dies in the dome", "The humidity decreased too quickly", "Use a longer stage with the vents half open. Use rockwool and not a hydro cloner."],
             ["The plant has no symptoms, then shows “dudding” in flower", "You did not do a test", "Section 16."]],
            caption="Table 12. Change one variable in each batch.",
        ),
        callout("tip", "Record the batch",
                p("Record the date, the cultivar and the type of piece that you cut. Record the "
                  "bleach strength, the bleach time and the medium. Record the number of pieces on "
                  "the medium. Record the number that are clean at day 7 and at day 21. Record the "
                  "number that made roots. These data are more important than a second hood.")),
    ]})

# ---------------------------------------------------------------------------
SECTIONS.append({
    "id": "sources",
    "kicker": "21",
    "title": "Sources of data and methods for photos",
    "blocks": [
        p("The basic paper on this site is a shorter guide for a new operator. It gives the same "
          "procedure for disease removal." + _c("cwp_tc_beginner") + "</p><p>The recipes and the "
          "survival numbers are from these papers. The papers are Holmes 2021, Das 2024, Kodym and "
          "Leeb 2019, Ioannidis 2022, Lata 2009 and 2016, and Punja 2025. We read these papers in "
          "full where they are open.</p><p>We used the pages of Plant Cell Technology for the label "
          "rates of products and for the papers that they refer to. These pages do not replace "
          "those papers."),
        p("The photos are illustrations that software made of the objects in this paper. They are "
          "not microscope slides from a lab. The diagrams agree with the anatomy of the shoot tip "
          "and of the stem from reports. One illustration of a stem cross-section showed a "
          "succulent plant and not cannabis. We discarded it and replaced it with Figure 6."),
        callout("note", "Law",
                p("Tissue culture does not change the law. Make cannabis plants only where you have a license or where the law lets you do it. This guide is about horticulture. It is not a legal document.")),
    ]})
