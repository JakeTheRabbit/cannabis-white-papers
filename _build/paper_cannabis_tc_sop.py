# -*- coding: utf-8 -*-
"""Paper: cannabis tissue culture SOP (jobs + forms). Does not replace tissue-culture."""
from components import (p, lead, h, ul, ol, callout, defterm, table, steps,
                        figure, grid, card, kv, photo)

import figs as F
import figs_extra as FX
import figs_playbook as FP
import figs_sop as S

SLUG = "cannabis-tissue-culture-sop"
TITLE = "Cannabis tissue culture SOP"
TITLE_MAX_PX = 42
EYEBROW = "Standard operating procedure · with forms"
SUB = ("Do these tasks in sequence to start a clean tissue culture line. Then you can increase the "
       "number of plants of a cultivar that has no disease. You can also give a plantlet with a "
       "test result to your grow room. Each task has a diagram and a form. A number [n] shows a "
       "source. It is not necessary to open the source to do the step.")

META = [
    ("list", "12 tasks"),
    ("doc", "14 forms"),
    ("flask", "Home and licensed facility"),
    ("clock", "Print and use"),
]
RELATED = ["cannabis-tissue-culture-playbook", "tissue-culture", "cloning", "mother-plants"]
REF_IDS = [
    "holmes2021", "lata2009", "lata2016", "das2024", "hlvd_threat2023",
    "hlvd_mgmt2025", "kodym2019", "kurtz2022", "torkamaneh2024", "ioannidis2022",
    "monthony2021", "page2021_dkw", "karger2019_cryo", "tis2022", "pct_howto",
    "pct_ppm", "athena", "murashige1962", "driver1984", "lubell2021",
    "punja2019-pathogens", "laf_buy",
]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

def form(code, title, fields, rows=None, note=None):
    """Printable log. fields = column headers. rows = empty line count."""
    n = rows if rows is not None else 6
    head = "".join(f"<th>{x}</th>" for x in fields)
    body = ""
    for _ in range(n):
        body += "<tr>" + "".join("<td style='height:28px'></td>" for _ in fields) + "</tr>"
    foot = f"<tfoot><tr><td colspan='{len(fields)}'>{note}</td></tr></tfoot>" if note else ""
    return (
        f"<div class='tbl-wrap' id='{code.lower()}'>"
        f"<table class='tbl'>"
        f"<caption><strong>{code}</strong>: {title}</caption>"
        f"<thead><tr>{head}</tr></thead><tbody>{body}</tbody>{foot}"
        f"</table></div>"
    )

IMG = "assets/img/tc-playbook"

SECTIONS = []

# ---------------------------------------------------------------------------
SECTIONS.append({
    "id": "scope",
    "kicker": "00",
    "title": "Purpose and scope",
    "blocks": [
        lead("This document is the SOP that you use to do the work. The tissue culture playbook is a longer document."),
        p("Two setups use the same tasks. A home setup has one room, a still-air box or a hood with a low price, and a pressure canner. A setup in a licensed facility has the same tasks. It also has lot numbers and a disease test."),
        p(f"A small <sup>[n]</sup> after a number or an instruction shows a source. It is not necessary to open the source to do the step. The list of sources is at the end.{_c("holmes2021")}"),
        figure(S.fig_sop_map(), 1, "The 12 tasks. Do tasks 0 to 5 before you try meristem dissection."),
        figure(S.fig_paper_pack(), 2, "Fourteen forms. Print the forms. Write with a pen. One lot number connects F-03, F-04, F-05 and F-10."),
        ul([
            "The format of the lot number is <strong>YYYY-MM-DD-CULTIVAR-NN</strong>. Example: 2026-08-14-MD-01.",
            "In each work period at the hood, use only one cultivar.",
            "If you are not sure that a jar is clean, the jar is dirty. Discard the jar. Record the jar on F-07.",
            "Do not think that a plant is clean if F-10 does not show a negative qPCR result.",
        ]),
        callout("warn", "First batch",
                p(f"Most of the first batch will be defective. Reports show losses of 45% to 95% at the start.{_c("das2024")} Write the steps that you did. Next time, change only one variable.")),
        defterm("Explant", "The piece of the plant that you put in the jar."),
        defterm("Medium", "The sterilized gel. It contains salts, sugar and agar. It can also contain a hormone, but a hormone is optional."),
        defterm("Lot", "A group of items with one number. The group is one mix of medium, or all the explants that you put in jars in one work period."),
    ]})

# ---------------------------------------------------------------------------
SECTIONS.append({
    "id": "room",
    "kicker": "Task 0A",
    "title": "Prepare the work area",
    "blocks": [
        lead("Select one small room or a closed corner. The area must not have a carpet or a houseplant. Do not keep cardboard boxes in the area. Each of these areas is satisfactory: a bedroom that you do not use, a laundry or a sealed space in a cupboard."),
        figure(S.fig_room_treat(), 3, "Make the room empty. Clean with detergent. Clean with bleach. Clean with alcohol. Seal the gaps. Then start the hood and wait."),
        photo(f"{IMG}/18-tc-room.jpg",
              "Before you put plants in the room, the floor must have no carpet and the walls must have no objects. The room must have one bench and a closed door. The room must not have cardboard or houseplants.",
              alt="Empty room prepared for tissue culture",
              model="Grok Imagine · illustration"),
        steps([
            ("Make the room empty", "Remove the plants, the food, the cardboard, the fabric and the pet beds from the room. Remove the dust from the fittings of the ceiling."),
            ("Clean with detergent", "Use warm water and household detergent on the walls, the floor, the bench, the door and the window sill. Then flush the surfaces with water."),
            ("Clean with bleach", "Mix 1 part household bleach (approximately 4–8% sodium hypochlorite) with 9 parts water. Apply the solution to the surfaces and keep them wet for 10 minutes. Flush the surfaces with water. Put on gloves. Open a window."),
            ("Clean with alcohol", "Clean the hard surfaces with 70% ethanol or isopropyl alcohol. Let the surfaces dry."),
            ("Seal the gaps", "Use tape to seal the gaps that you can see in the walls. If the door has a gap, install a door sweep. If you cannot remove the carpet, put sealed vinyl on it."),
            ("Instructions for the room after this step", "Do not eat in the room. Do not go into the room in outdoor shoes. Do not keep cardboard in the room. Keep the door closed while you do the work. Only one person at a time can be at the hood."),
        ]),
        h(3, "Treatment of the room each week, after you start the work"),
        ul([
            "Clean the floor and the door handle with detergent. Then clean them with 70% alcohol.",
            "Clean the bench and the steel of the hood with 70% alcohol at the start of each work day (Task 1).",
            "Remove the waste from the bins after each work period. Do not let dirty jars stay in the room at night.",
            "The hood can have a UV lamp. Operate the UV lamp only when the sash is down and no person is in the room. Make sure that no UV light goes into your eyes. Clean the tube each month. The UV lamp gives more protection, but it does not replace the HEPA fan.",
        ]),
        form("F-01", "Sanitation of the room each day",
             ["Date", "Name", "Floor", "Bench", "Door", "Hood steel", "Waste removed from bin", "Signature"],
             rows=8,
             note="Put a mark in each check box when you do the task. If a check box has no mark, do not start cultures on that day."),
    ]})

# ---------------------------------------------------------------------------
SECTIONS.append({
    "id": "hood-buy",
    "kicker": "Task 0B",
    "title": "Selection and installation of a laminar-flow hood",
    "blocks": [
        lead("You can use a still-air box. A horizontal laminar-flow hood is easier to use. You can purchase a hood from China at a low price. Make sure that you tell the seller the correct specification. When you receive the hood, do a check of it."),
        figure(S.fig_hood_buy(), 4, "The hood must have horizontal flow, an H13 or H14 HEPA filter and a pre-filter. The cabinet must be metal. The seller must give a certificate."),
        figure(S.fig_hood_flow(), 5, "A fan pulls the air through a pre-filter and then through a HEPA filter. The air then moves to you in one sheet. Do the work in that sheet of air. Do not put objects on or in front of the filter."),
        h(3, "Definitions of the terms"),
        ul([
            "<strong>Horizontal laminar flow.</strong> The air moves in one direction, from the face of the filter to you. Use this type for work with plants. The hood gives protection to the plant. It does not give protection to your lungs.",
            "<strong>HEPA H13 / H14.</strong> A grade of filter. An H13 filter stops 99.95% of the particles of 0.3 µm. An H14 filter stops a larger percentage of the particles. Each grade is satisfactory. A “HEPA-like” filter and foam pads are not satisfactory.",
            "<strong>Pre-filter.</strong> A pad with a low price that you can clean. It is in front of the HEPA filter. It keeps dust away from the HEPA filter. The HEPA filter has a high price. If the listing has no pre-filter, do not select that listing.",
            "<strong>Face velocity 0.30–0.50 m/s.</strong> The speed of the clean air that comes out of the filter. A speed of less than 0.3 m/s is not sufficient. A speed of more than 0.6 m/s makes the tissue dry and can cause dirt to go back into the work area.",
        ]),
        h(3, "Where to find a hood"),
        p("Use these terms to find hoods. Do not change the terms. Open the listing. Send the checklist below to the seller before you purchase the hood." + _c("laf_buy")),
        table(
            ["Site", "Terms to use", "Link"],
            [["AliExpress", "horizontal laminar flow hood H14 HEPA",
              "<a href='https://www.aliexpress.com/w/wholesale-laminar-flow-hoods.html'>list of hoods on AliExpress</a>"],
             ["AliExpress, example of a type of hood", "H13/H14 hoods at approximately USD 260–500",
              "<a href='https://www.aliexpress.com/item/1005010452823851.html'>item 1005010452823851</a> (examine the current specification)"],
             ["Alibaba", "horizontal laminar flow hood H14 plant tissue culture",
              "<a href='https://www.alibaba.com/trade/search?SearchText=horizontal+laminar+flow+hood+H14'>results on Alibaba</a>"],
             ["Alibaba, type of hood with a brand", "BIOBASE clean bench / LAF",
              "<a href='https://www.alibaba.com/product-detail/BIOBASE-LAF-laminar-flow-hood-Laminar_1601197354926.html'>BIOBASE LAF listing</a>"]],
            caption="Table 1. Use these terms to find hoods. Listings change. Purchase a hood for its specification, not for its brand name.",
            foot="Prices change. The cost of freight and a plug for 220–240 V are more important than a difference of $40.",
        ),
        h(3, "Message to the seller"),
        p("Send the list below to the seller as one message. If the seller cannot give the information, do not purchase the hood."),
        ul([
            "Give the type of the cabinet. It must be a horizontal laminar-flow cabinet and not a biosafety cabinet.",
            "Give the HEPA grade: H13 or H14. Send the EN1822 certificate (or an equivalent certificate) for the lot of this filter.",
            "The hood must have a pre-filter and a HEPA filter as two parts. Give the size and the price of a replacement HEPA filter.",
            "Give the face velocity at the work opening, in m/s.",
            "The voltage and the plug must be for 220–240 V (change this value if your power supply is 110 V).",
            "Give the width of the work opening in mm. The width must be a minimum of 400 mm (16 in).",
            "Send photos of the gasket of the filter and the nameplate of the fan before the shipping.",
        ]),
        h(3, "Prices"),
        ul([
            "A small metal hood for a bench has an H13 or H14 filter and a width of 400–700 mm (16–28 in). The price is frequently <strong>USD 260–700</strong>, plus freight.",
            "A full-size clean bench (BIOBASE type): the price is frequently <strong>USD 800–2,000</strong>, plus freight in a crate.",
            "A portable hood of the Athena type, from the market for used equipment, can have a higher price than a new bench from China. Compare the specifications of the filter, not the brand name.",
        ]),
        callout("danger", "Do not purchase",
                p("Do not purchase a cardboard mushroom box with a furnace filter. Do not purchase a vertical “nail salon” table that has no HEPA grade. Do not purchase a hood that has a foam sheet in the photos and HEPA in the listing. Do not purchase a biosafety cabinet if you are not sure that protection for the operator is necessary. A biosafety cabinet is the incorrect tool, and its price is higher.")),
        h(3, "When you receive the hood"),
        figure(S.fig_hood_setup(), 6, "Remove the packaging and put the hood in position. Make sure that the voltage is correct. Operate the empty hood for 30 minutes. Do a check of the airflow with tissue paper. Clean only the steel. Record the check on F-12."),
        steps([
            ("Examine the hood", "Make sure that the frame of the HEPA filter has no damage. Make sure that the plastic stays on the face of the filter. Make sure that the fan does not make a rattle."),
            ("Put the hood in position", "Use a bench that is level and stable. Keep 30 cm (12 in) of free air behind the intake or below the intake. The correct position is different for different models. Do not push the hood against a curtain."),
            ("Power", "Read the nameplate. A unit for 220–240 V becomes defective when you connect it to 110 V. Use a power board with surge protection."),
            ("First operation", "Make sure that the hood is empty. Operate the fan for 30 minutes. Listen to the fan. Smell the air for a burned odor."),
            ("Check of the airflow", "Hold a thin strip of tissue paper in the work opening. The strip must bend in the direction of the airflow, to you, and stay stable (horizontal hood). The strip must not move up and down, go back to the hood or hang down with no movement. If the strip does this, send a message to the seller before you use the hood."),
            ("Clean the hood", "Clean the painted steel and the work tray with 70% alcohol. Do not spray liquid on the face of the HEPA filter."),
            ("Optional test with smoke", "Hold an incense stick 20 cm (8 in) in front of the filter. The smoke must move away from the filter in one sheet. It must not go back to the bench."),
            ("Record the data", "Write the data on F-12. If the tissue paper hangs down with no movement, do not put plants in jars."),
        ]),
        form("F-12", "Check of the hood",
             ["Date", "Hours of operation", "Tissue paper strip correct?", "Noise / odor", "Pre-filter cleaned?", "Signature"],
             rows=8,
             note="Do this check when you install the hood, then each month, and after each change of a filter."),
        callout("note", "If you have no hood",
                p("Use a still-air box. A still-air box is a transparent plastic container on its side, with two arm holes. Clean the inner surfaces with 70% alcohol. Make sure that the fans are off. The tasks are the same, and the steps of the SOP do not change. The work is slower, but the price is lower.")),
    ]})

# ---------------------------------------------------------------------------
SECTIONS.append({
    "id": "open",
    "kicker": "Task 1",
    "title": "Opening procedure",
    "blocks": [
        lead("Do this task each day that you do the work. Do it before you open a jar."),
        figure(S.fig_day_open(), 7, "Put on clean clothing. Operate the hood for 20 minutes. Clean the room. Clean the steel of the hood. Put on new gloves. Put only the tools for this work period in the hood."),
        steps([
            ("Clothing", "Put on clean clothing with long sleeves. Make sure that your hair does not hang down. Do not go into the room in outdoor shoes. In a licensed lab, put on a gown, a hair cover and gloves. Write the data on F-13."),
            ("Start the hood", "Make sure that the hood is empty. Operate the hood for 20 minutes. If the fan makes a new noise or a burned odor, stop the hood."),
            ("Form F-01", "Clean the floor, the bench, the door, the steel of the hood and the bin. Record the work on the form."),
            ("Gloves", "Put on new nitrile gloves. Spray the gloves with 70% alcohol. Spray the gloves again after you go out of the room."),
            ("Put the items in the hood", "Put the closed jars, the tools and the waste bag for this work period on the left. Do not put other items in the hood."),
        ]),
        form("F-13", "Gown / entry (licensed lab). At home: write “home” and do not write in the columns that you do not use.",
             ["Date", "Time in", "Gown", "Hair cover", "Gloves", "Jewelry removed", "Time out", "Signature"],
             rows=8),
    ]})

# ---------------------------------------------------------------------------
SECTIONS.append({
    "id": "media",
    "kicker": "Task 2",
    "title": "Mix the medium, sterilize it and keep it for 7 days",
    "blocks": [
        lead("The quantity in this task is one liter. Use full-strength MS to start cultures and for multiplication. Use half-strength MS to make roots in gel."),
        figure(S.fig_media_steps(), 8, "Add water, salts and sugar. Set the pH. Add agar. Put the medium in the jars. Sterilize at 121 °C (250 °F) and 103 kPa (15 psi) for 20 minutes. Keep the jars for 7 days."),
        table(
            ["Ingredient", "1 liter", "Information"],
            [["RO or distilled water", "Start with 800 mL. Then add water to 1 L.", "Do not use tap water."],
             ["MS basal salts", "4.4 g", "For half strength, use 2.2 g. Many media for rooting use half strength."],
             ["Sucrose", "30 g", "Table sugar is satisfactory."],
             ["myo-Inositol", "0.1 g", "Add it. Do not add it if your MS contains it."],
             ["Activated charcoal", "1 g (optional)", f"It helps to decrease browning.{_c("holmes2021")}"],
             ["Agar", "6–8 g. Use 9.5 g if the shoots have glassy growth.", f"{_c("das2024")}"],
             ["PPM (optional)", "0.5–2 mL", f"Use the rate on the label. PPM does not replace a meristem cut.{_c("pct_ppm")}"],
             ["pH", "5.6–5.8 before you add agar", "Then sterilize the medium"]],
            caption="Table 2. Standard cannabis medium.",
        ),
        table(
            ["Use for", "Add this after you are sure that MS gives good results", "Dose"],
            [["Start of the culture (usual method)", "TDZ + NAA", f"1 µM + 0.5 µM{_c("holmes2021")}{_c("lata2009")}"],
             ["Start of the culture (weaker hormone)", "meta-Topolin", f"0.48 mg/L{_c("lata2016")}{_c("das2024")}"],
             ["Long-term multiplication", "No hormone, plus more calcium", f"Calcium nitrate 0.71 g/L + calcium gluconate 1.35 g/L{_c("das2024")}"],
             ["Roots in gel", "IBA", f"5 µM. A higher dose gives a worse result.{_c("holmes2021")}"]],
            caption="Table 3. Hormones. Change one hormone at a time.",
        ),
        steps([
            ("Weigh", "Write each mass on F-03 before you put the medium in the jars."),
            ("pH", "Set the pH to 5.6–5.8 before you add agar. To decrease the pH, add dilute acid. To increase the pH, add dilute base."),
            ("Agar and heat", "Dissolve the agar with heat. Fill each jar to one third with medium. Keep the lids loose."),
            ("Sterilize", "Use a stovetop pressure canner that holds 103 kPa (15 psi), or an autoclave. Sterilize at 121 °C (250 °F) and 103 kPa (15 psi) for 20 minutes. An Instant Pot is not satisfactory for this step. Put the jars on a rack. The jars must not be in the water."),
            ("Let the jars become cool", "When the jars are sufficiently cool to touch, tighten the lids. Put a label with the lot number on each jar."),
            ("Hold", "Keep the jars on a shelf for 7 days. If a jar has a cloud or mold, discard all the jars of the lot. Do not put explants in these jars."),
        ]),
        form("F-02", "Load of the autoclave or pressure canner",
             ["Date", "Load ID", "121 °C?", "15 psi?", "20 min?", "Cool / dry", "Defective?", "Signature"],
             rows=6,
             note="If you write no for 121 °C, 15 psi or 20 min, discard the load."),
        form("F-03", "Media batch",
             ["Lot no.", "Date", "MS g", "Sugar g", "Agar g", "pH", "Hormone", "PPM mL", "Jars n", "Clean on day 7?", "Signature"],
             rows=6,
             note="Lot no. = YYYY-MM-DD-MED-NN. Write this number on F-04."),
    ]})

# ---------------------------------------------------------------------------
SECTIONS.append({
    "id": "cut",
    "kicker": "Task 3",
    "title": "Prepare the explant and sterilize its surface",
    "blocks": [
        lead("In the first batches, use a stem piece with one bud, 10–15 mm (0.4–0.6 in) long. Do not use a meristem."),
        figure(S.fig_bleach_steps(), 9, "Cut the stem piece. Clean it with soap. Put it in 70% alcohol for 30–60 s. Put it in bleach for 20–30 min. Clean it three times with sterilized water. In the hood, remove the ends that have damage from the bleach."),
        steps([
            ("Mother", "The mother plant must be in vegetative growth. Examine it for pests. Use a new plant if you can. Use one cultivar."),
            ("Cut", "Cut in the morning. Each piece must be 10–15 mm (0.4–0.6 in) long. Remove the large leaves. Keep the pieces wet."),
            ("Clean with soap", "Use tap water with a drop of dish soap or Tween-20. Do this for 10–20 min."),
            ("70% alcohol", "Keep the pieces in the alcohol for 30–60 seconds. Then drain the alcohol."),
            ("Bleach", f"Holmes used 10% household bleach (approximately 0.625% NaOCl) with 0.1% Tween-20 for 20 min. Mix the solution during this time.{_c("holmes2021")} Das used 1% NaOCl for 30 min.{_c("das2024")} Do not keep the pieces in the bleach for 60 min."),
            ("Clean with sterilized water", "Clean the pieces three times with sterilized water. Keep the pieces in the water for 3–5 min each time. Then put the pieces in the hood."),
            ("Remove the ends", "Cut the ends from the stem when they are white or have damage from the bleach. Put the new end of the stem in the gel."),
        ]),
        photo(f"{IMG}/04-nodal-explant.jpg",
              "A stem piece with one bud. Use this piece in the first batches.",
              alt="Nodal explant of cannabis",
              model="Grok Imagine · illustration"),
    ]})

# ---------------------------------------------------------------------------
SECTIONS.append({
    "id": "plate",
    "kicker": "Task 4",
    "title": "Explants in jars: labels and incubation",
    "blocks": [
        lead("Put one piece in each jar until you know your rate of good results."),
        figure(S.fig_plate_steps(), 10, "Open one jar in the airflow. Put the piece in the gel with the bud above. Put the lid on the jar. Make a label. Put the jar on a shelf. Examine the jar on day 7."),
        figure(F.fig_lab(), 11, "Open jars only in the center of the hood. Put the tools on the left. Put the waste on the left at the front."),
        steps([
            ("Airflow", "Do the work 10–20 cm (4–8 in) in front of the filter. Do not do the work at the edge of the hood."),
            ("One lid", "Hold the lid with its face down, at the side of the jar. Do not hold the lid above the jar."),
            ("Put the explant in the jar", "Put the end that you cut in the gel. Keep the bud above the gel."),
            ("Lid", "Put the lid on the jar immediately. Do not speak above the jar."),
            ("Label", "Write the cultivar, the date, the type of explant and the lot number from F-03 on the label."),
            ("Shelf", "Keep the jars at 24–26 °C (75–79 °F). Use 16–18 h of light, at approximately 70–100 µmol m⁻² s⁻¹. Do not open a jar to examine the culture."),
        ]),
        form("F-04", "Initiation (explants in jars)",
             ["Lot no.", "Cultivar", "Explant", "n put in jars", "Medium lot", "Date", "Day-7 clean n", "Day-21 clean n", "Signature"],
             rows=8,
             note="The value n put in jars must be the same as the number of explants that you put in the jars. The sum of Day-7 clean n and the number of discarded jars must be the same as n put in jars."),
    ]})

# ---------------------------------------------------------------------------
SECTIONS.append({
    "id": "scout",
    "kicker": "Task 5",
    "title": "Examine the cultures and discard defective jars",
    "blocks": [
        lead("Examine the jars on day 7 and on day 21. Look through the glass. Do not open a jar if you are not sure that it is clean."),
        figure(S.fig_scout(), 12, "Keep the jar. Discard the jar. Monitor the jar. If you are not sure, discard the jar."),
        photo(f"{IMG}/09-contamination.jpg",
              "Left: bacteria. Right: fungus. Seal the jar. Put the jar in a bag. Put the bag in the bin. Do not open the jar in the hood that you continue to use.",
              alt="Dirty jars",
              model="Grok Imagine · illustration"),
        photo(f"{IMG}/10-phenolic-browning.jpg",
              "A brown ring is a leak from the area where you cut the explant. It is not always microbes, but do not open the jar next to clean work. Move the cultures that stay in good condition to new medium that contains charcoal.",
              alt="Browning",
              model="Grok Imagine · illustration"),
        photo(f"{IMG}/13-hyperhydricity.jpg",
              "Wet, transparent leaves are a sign of too much hormone or too much water. In the next multiplication, use no cytokinin, use 9.5 g/L agar and use a lid with a vent.",
              alt="Glassy growth",
              model="Grok Imagine · illustration"),
        form("F-07", "Contamination: discarded jars",
             ["Date", "Lot no.", "Jar ID", "Bacteria / fungus / browning / glassy growth", "Decision (discard / monitor)", "Signature"],
             rows=10,
             note="Write one line for each discarded jar. With these lines you can find if your technique becomes better."),
    ]})

# ---------------------------------------------------------------------------
SECTIONS.append({
    "id": "multiply",
    "kicker": "Task 6",
    "title": "Shoot multiplication and subculture",
    "blocks": [
        lead("Use only jars that were clean on day 21. Use a new jar each time."),
        figure(FX.fig_subculture(), 13, "Cut the shoots again. Use new medium. Write the new lot on a new line of F-05."),
        photo(f"{IMG}/07-multiplication-shoots.jpg",
              "A good culture has green leaves with leaflets, transparent amber gel and no cloud.",
              alt="Clean jar for multiplication",
              model="Grok Imagine · illustration"),
        steps([
            ("Source jar", "Use a jar that was clean on day 21. Use one cultivar."),
            ("Cut", "Cut a shoot tip or a node with a bud that you can see. Each piece must be 15–25 mm (0.6–1.0 in) long."),
            ("New jar", f"Use the same medium or the medium that has no hormone and more calcium.{_c("das2024")}"),
            ("Density", "At home, put 1–3 explants in each jar. In a licensed facility, the rate in F-07 gives the number of explants for each jar."),
            ("Time", f"The time for each subculture is 3–4 weeks. After approximately five subcultures, start the line again from a mother plant with a negative test result.{_c("torkamaneh2024")}"),
        ]),
        form("F-05", "Subculture",
             ["Date", "From lot", "New lot", "Cultivar", "n moved", "Medium lot", "Day-21 clean n", "Signature"],
             rows=8),
    ]})

# ---------------------------------------------------------------------------
SECTIONS.append({
    "id": "meristem",
    "kicker": "Task 7",
    "title": "Meristem dissection after process validation",
    "blocks": [
        lead("Use a microscope. The piece is 0.2–0.4 mm (0.008–0.016 in) long. Then do a lab test. This task does not make a plant &ldquo;clean&rdquo; if you do not do the lab test."),
        figure(FP.fig_meristem_setup(), 14, "The five zones are the same as in the layout of the hood. The microscope is in the middle."),
        figure(FP.fig_meristem_tools(), 15, "The tools are a microscope, fine forceps, a #11 scalpel, a black dish, a glass-bead sterilizer and 70% alcohol."),
        figure(FP.fig_meristem_hands(), 16, "The left hand holds. The right hand cuts."),
        figure(FP.fig_meristem_sequence(), 17, "The sequence has eight movements. Do all the movements before you make the nick."),
        figure(FP.fig_meristem_scope(), 18, "Remove the leaves until you see a pale dome and two small leaves. Then stop."),
        photo(f"{IMG}/14-meristem-tools.jpg",
              "The tools for the work.",
              alt="Meristem tools",
              model="Grok Imagine · illustration"),
        photo(f"{IMG}/16-meristem-hands.jpg",
              "Hold the forceps in the left hand and the scalpel in the right hand. Hold them in the same positions when the piece is 1 mm.",
              alt="Tip with leaves removed",
              model="Grok Imagine · illustration"),
        photo(f"{IMG}/17-meristem-dome-cut.jpg",
              "A dome with two small leaves. Cut below the dome, near it. The piece is 0.2–0.4 mm.",
              alt="Meristem dome",
              model="Grok Imagine · illustration"),
        steps([
            ("New growth", "Cut a vegetative tip of 10–15 mm (0.4–0.6 in). Remove the large leaves before you put the tip in the hood."),
            ("Sterilized tools", "Sterilize the tools in a glass-bead sterilizer at approximately 250 °C (approximately 480 °F) for 20 s. Then let the tools become cool."),
            ("Dish", "Put one drop of sterilized water on the dish. Use a magnification of 10–20× and then of 30–40×."),
            ("Remove the leaves", "Remove the outer leaves. Stop when you see two small leaves."),
            ("Put the tip in bleach", "Use a shorter time in the bleach than for a woody node. Then clean the tip with sterilized water."),
            ("One nick", f"Make one nick. The piece must be 0.2–0.4 mm (0.008–0.016 in).{_c("hlvd_mgmt2025")} Put the piece on a start medium of the Holmes type.{_c("holmes2021")}"),
            ("Wait", "Wait for 4–8 weeks. Then do the test on F-10. At six months, approximately 41% of the plants will have a negative test result. It is not 100%."),
        ]),
        form("F-06", "Meristem cut",
             ["Date", "Mother ID", "n tips", "n put in jars", "Medium lot", "n in good condition at week 8", "F-10 result", "Signature"],
             rows=6),
    ]})

# ---------------------------------------------------------------------------
SECTIONS.append({
    "id": "root",
    "kicker": "Task 8",
    "title": "Rooting and acclimatization",
    "blocks": [
        lead("A shoot with no roots is not a plant. In a culture jar, the relative humidity of the "
             "air is almost 100%. Thus the plant cannot close its stomata, and it does not make a "
             "layer of wax on its leaves. In the jar, it is not necessary for the plant to keep "
             "water.</p><p>When you move the plant directly to open air, it wilts in a small number "
             "of hours. The problem is the speed of the change and not the new conditions. Decrease "
             "the humidity in steps. This procedure is acclimatization."),
        photo(f"{IMG}/08-rooted-plantlet.jpg",
              "White roots in transparent gel. There is no brown ring.",
              alt="Plantlet with roots",
              model="Grok Imagine · illustration"),
        photo(f"{IMG}/11-acclimatization.jpg",
              "Plugs in a humidity dome. Open the vents half at day 7. Remove the lid at day 14.",
              alt="Acclimatization",
              model="Grok Imagine · illustration"),
        figure(F.fig_acclim(), 19, "Do not put a plant from a jar on a dry bench."),
        steps([
            ("Select a shoot", "Select a shoot of 2–4 cm (0.8–1.6 in). Do not select a shoot with glassy growth. Do not select a brown shoot."),
            ("Make roots", f"Alternative A: put the shoot in gel with 5 µM IBA for 2–4 weeks.{_c("holmes2021")} Alternative B: put the bottom end of the shoot in 15 mM IBA for 2–4 min. Then put the shoot in a sterilized plug.{_c("ioannidis2022")} Alternative C: put the shoot on rockwool with usual fertilizer, in a jar with a vent and with no sugar.{_c("kodym2019")}"),
            ("Plug", "Use a plug of rockwool or coco. Soak the plug in a weak nutrient solution for vegetative growth. The pH must be approximately 5.8."),
            ("Dome", "Spray water on the walls of the dome. Use 16 h of light, with a low light intensity, at 24 °C (75 °F)."),
            ("Vents", "On day 7, open the vents half. On day 9, open the vents fully. On day 14, remove the lid."),
            ("Pot", "Use the procedure for a new clone. For some weeks, do not use a photoperiod of 12 hours."),
        ]),
        form("F-08", "Rooting",
             ["Date", "From lot", "Method (gel / dip / no-sugar)", "n", "n with roots at week 4", "Signature"],
             rows=6),
        form("F-09", "Acclimatization",
             ["Date out", "Lot", "Plug type", "n", "n in good condition on day 14", "Signature"],
             rows=6),
    ]})

# ---------------------------------------------------------------------------
SECTIONS.append({
    "id": "index",
    "kicker": "Task 9",
    "title": "Tests, intake and lot records",
    "blocks": [
        lead("If F-10 has no result, the plant is a clone. It is not a clean mother plant."),
        figure(FX.fig_hlvd_clearance(), 20, "Cut the plant. Wait for new leaves. Get a sample. Freeze a retain sample. Do the test again."),
        steps([
            ("Sample", "Get a sample from a new leaf of full size, or from the leaf stalk. Do this after the plant makes new growth."),
            ("Lab", "Use a lab that does the RT-qPCR test for cannabis Hop latent viroid. Root tissue gives the most accurate result, if the lab can use roots."),
            ("Test again", "Do the test again 3–4 weeks after the first test, and before a mother plant goes into production."),
            ("Retain sample", "Freeze the remaining tissue from each lot with a “not detected” result."),
        ]),
        form("F-10", "Indexing / qPCR",
             ["Date", "Plant / lot", "Tissue", "Lab", "HpLVd", "Other", "Retain sample ID", "“Not detected” result?", "Signature"],
             rows=8,
             note="Write yes only for a “not detected” result. For a different result, put the plant in quarantine or discard it. Do not write “clean” in this column."),
        form("F-11", "Mother plant intake / quarantine",
             ["Date in", "Cultivar", "Source", "Room", "Pests?", "F-10 date", "F-10 result", "Release / discard", "Signature"],
             rows=6),
        form("F-14", "Lot record",
             ["Lot no.", "Opened", "Closed", "Cultivar", "F-03", "F-04 n", "F-07 discarded", "F-10", "Decision for the lot"],
             rows=10,
             note="Write one line for each lot. In the last column, write one of these: multiplication, rooting, mother plant or discard."),
        callout("warn", "Tools that touch a dirty plant",
                p(f"70% alcohol does not break the RNA of Hop latent viroid. Put the tools in 5–10% household bleach for 1–2 minutes, or in 1000 ppm hypochlorous acid for 1 minute. Then flush the tools with water.{_c("hlvd_mgmt2025")} If you can, use one blade for each cultivar.")),
    ]})

# ---------------------------------------------------------------------------
SECTIONS.append({
    "id": "week",
    "kicker": "Task 10",
    "title": "Operating procedure for each week",
    "blocks": [
        table(
            ["Day", "Home", "Licensed facility"],
            [["Monday", "Use form F-01. Fill the jars with the medium of Sunday.", "Use forms F-01 and F-13. In the media kitchen, use F-02 and F-03."],
             ["Tuesday", "Put 10–20 nodes in jars. Use F-04.", "Use only mother plants with the decision “release” on F-11. Put their explants in jars."],
             ["Wednesday", "Do the multiplication of the jars that were clean on day 21. Use F-05.", "Use one cultivar for each hood. Use F-05."],
             ["Thursday", "Examine the jars. Use F-07.", "Examine the jars. Record each lot with photos. Use F-07."],
             ["Friday", "Make roots in gel or do an IBA dip. Use F-08. If it is the time for a test, send the samples for F-10.", "Do one batch of qPCR tests. Put the plants that have no negative result in quarantine."],
             ["Saturday–Sunday", "Do not open jars.", "Monitor only the alarms."]],
            caption="Table 4. If a form has no data, you did not do the task.",
        ),
        ul([
            f"After you do the procedure many times, you can do approximately 80–100 transfers each hour at a hood.{_c("pct_howto")}",
            "Do the F-10 test on the production mother plants at intervals of 3–6 weeks.",
            f"After approximately five subcultures, start a production line again from a backup with a negative test result.{_c("torkamaneh2024")}",
        ]),
    ]})

# ---------------------------------------------------------------------------
SECTIONS.append({
    "id": "fix",
    "kicker": "Task 11",
    "title": "Troubleshooting",
    "blocks": [
        table(
            ["Problem", "Change only this"],
            [["More than 50% of the jars are dirty at day 7", "Move your hands more slowly. Use a new mother plant. Use a smaller tip."],
             ["More than 50% of the jars are dirty after day 14", f"Use meristem dissection (Task 7). You can also soak the explants in 4–5% PPM.{_c("pct_ppm")} Change the substrate of the mother plant."],
             ["The explants become brown in 48 h", "Use a shorter time in the bleach. Add charcoal. Cut the ends from the stem."],
             ["The leaves have glassy growth", "Use no cytokinin. Use 9.5 g/L agar. Use a lid with a vent."],
             ["No roots at week 5", "Use 5 µM IBA or a 15 mM IBA dip. Do not use more hormone."],
             ["The plants die in the dome", "Keep the vents half open for a longer time. Use rockwool and not a bubbler."],
             ["The plants have no problem that you can see, but they are defective in flower", "You did not do the F-10 test."]],
            caption="Table 5. One variable for each batch.",
        ),
    ]})

# ---------------------------------------------------------------------------
SECTIONS.append({
    "id": "sources",
    "kicker": "12",
    "title": "Information on sources",
    "blocks": [
        p("The marks in this document point to this section. It is not necessary to read this section to do the work for one day."),
        p("The photos are illustrations. Use the diagrams for the size and the sequence."),
        callout("note", "Law",
                p("Do the cultivation of cannabis only where the law lets you do it. This SOP gives information on horticulture. It does not give legal advice.")),
    ]})
