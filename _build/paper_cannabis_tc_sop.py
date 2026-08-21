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
EYEBROW = "Standard operating procedure · forms included"
SUB = ("Do these jobs in order. Each job has a diagram and a form. "
       "A star in brackets is a source, not extra reading you need before you start.")

META = [
    ("list", "12 jobs"),
    ("doc", "14 forms"),
    ("flask", "Home + licensed"),
    ("clock", "Print and follow"),
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
        f"<caption><strong>{code}</strong> — {title}</caption>"
        f"<thead><tr>{head}</tr></thead><tbody>{body}</tbody>{foot}"
        f"</table></div>"
    )

IMG = "assets/img/tc-playbook"

SECTIONS = []

# ---------------------------------------------------------------------------
SECTIONS.append({
    "id": "scope",
    "kicker": "00",
    "title": "Scope, names, and how to use the stars",
    "blocks": [
        lead("This is the working SOP. The tissue culture playbook is the longer guide. Follow this document if you are doing the work today."),
        p("Two setups share the same jobs. Home: one room, a still-air box or a cheap hood, a pressure canner. Licensed: the same jobs plus lot numbers and a disease test."),
        p(f"A small <sup>[n]</sup> after a number or a rule is a source. You do not need to open it to do the step. The list is at the end.{_c("holmes2021")}"),
        figure(S.fig_sop_map(), 1, "The 12 jobs. Do 0–5 before you try meristems."),
        figure(S.fig_paper_pack(), 2, "Fourteen forms. Print them. Write in pen. One lot number ties F-03, F-04, F-05 and F-10 together."),
        ul([
            "Lot number format: <strong>YYYY-MM-DD-CULTIVAR-NN</strong>. Example: 2026-08-14-MD-01.",
            "One cultivar per hood session.",
            "If a jar is doubtful, it is dirty. Bin it. Log it on F-07.",
            "Do not call a plant clean unless F-10 has a negative qPCR result.",
        ]),
        callout("warn", "First run",
                p(f"Expect to lose most of the first batch. Published start-up losses sit between 45% and 95%.{_c("das2024")} Write what you did. Change one thing next time.")),
        defterm("Explant", "The piece of plant you put in the jar."),
        defterm("Medium", "The sterile jelly: salts, sugar, agar, optional hormone."),
        defterm("Lot", "One mix of medium, or one plating session, under one number."),
    ]})

# ---------------------------------------------------------------------------
SECTIONS.append({
    "id": "room",
    "kicker": "Job 0A",
    "title": "Treat the room before you buy anything else",
    "blocks": [
        lead("Pick one small room or a closed corner. No carpet. No house plants. No cardboard boxes stored in it. A spare bedroom, a laundry, or a sealed cupboard bay will do."),
        figure(S.fig_room_treat(), 3, "Empty. Wash. Bleach. Alcohol. Seal. Then turn the hood on and wait."),
        photo(f"{IMG}/18-tc-room.jpg",
              "What the room should look like before you bring plants in: bare floor, empty walls, one bench, door shut. No cardboard. No house plants.",
              alt="Empty room ready for tissue culture",
              model="Grok Imagine · illustration"),
        steps([
            ("Empty it", "Remove plants, food, cardboard, fabric, pet beds. Wipe dust off the ceiling fittings."),
            ("Wash", "Warm water and household detergent on walls, floor, bench, door, window sill. Rinse."),
            ("Bleach", "Mix 1 part household bleach (about 4–8% sodium hypochlorite) with 9 parts water. Wet surfaces for 10 minutes. Rinse. Wear gloves. Open a window."),
            ("Alcohol", "Wipe hard surfaces with 70% ethanol or isopropyl alcohol. Let it dry."),
            ("Seal", "Tape obvious wall gaps. Add a door sweep if the door has a gap. Cover carpet with sealed vinyl if you cannot rip it up."),
            ("Rules for the room after this", "No eating. No outdoor shoes. No cardboard storage. Door shut while you work. One person at a time at the hood."),
        ]),
        h(3, "Weekly room treatment, after you are running"),
        ul([
            "Floor and door handle: detergent, then 70% alcohol.",
            "Bench and hood steel: 70% alcohol at the start of every work day (Job 1).",
            "Bins: empty after every session. Do not leave dirty jars in the room overnight.",
            "If you have a UV lamp in the hood: run it only with the sash down and nobody in the room. Never look at it. Wipe the tube monthly. UV is extra. It is not a substitute for the HEPA fan.",
        ]),
        form("F-01", "Room daily clean",
             ["Date", "Name", "Floor", "Bench", "Door", "Hood steel", "Bin emptied", "Sign"],
             rows=8,
             note="Tick each box. If you skip a box, do not start cultures that day."),
    ]})

# ---------------------------------------------------------------------------
SECTIONS.append({
    "id": "hood-buy",
    "kicker": "Job 0B",
    "title": "Buy a cheap hood from China and set it up",
    "blocks": [
        lead("A still-air box works. A horizontal laminar-flow hood is easier. You can buy one from China for a few hundred dollars if you order the right spec and check it on arrival."),
        figure(S.fig_hood_buy(), 4, "Horizontal flow. H13 or H14 HEPA plus a pre-filter. Metal body. Certificate from the seller."),
        figure(S.fig_hood_flow(), 5, "Air is sucked through a pre-filter, then a HEPA, then blown toward you in one sheet. Work in that sheet. Do not block the filter."),
        h(3, "What the words mean"),
        ul([
            "<strong>Horizontal laminar flow.</strong> Air moves in one direction, from the filter face toward you. That is the type used for plant work. It protects the plant, not your lungs.",
            "<strong>HEPA H13 / H14.</strong> A filter grade. H13 stops 99.95% of 0.3 µm particles. H14 is tighter. Either is fine. “HEPA-like” and foam pads are not.",
            "<strong>Pre-filter.</strong> A cheap washable pad in front of the HEPA. It keeps dust off the expensive filter. If the listing has no pre-filter, skip it.",
            "<strong>Face velocity 0.30–0.50 m/s.</strong> How fast the clean air comes out. Slower than 0.3 is weak. Faster than 0.6 dries tissue and can bounce dirt back.",
        ]),
        h(3, "Where to search"),
        p("Search these exact phrases. Open the listing. Message the seller with the checklist below before you pay." + _c("laf_buy")),
        table(
            ["Site", "Search phrase", "Link"],
            [["AliExpress", "horizontal laminar flow hood H14 HEPA",
              "<a href='https://www.aliexpress.com/w/wholesale-laminar-flow-hoods.html'>aliexpress.com/w/wholesale-laminar-flow-hoods.html</a>"],
             ["AliExpress example class", "H13/H14 hoods around USD 260–500",
              "<a href='https://www.aliexpress.com/item/1005010452823851.html'>item 1005010452823851</a> (check current spec)"],
             ["Alibaba", "horizontal laminar flow hood H14 plant tissue culture",
              "<a href='https://www.alibaba.com/trade/search?SearchText=horizontal+laminar+flow+hood+H14'>alibaba.com search</a>"],
             ["Alibaba branded class", "BIOBASE clean bench / LAF",
              "<a href='https://www.alibaba.com/product-detail/BIOBASE-LAF-laminar-flow-hood-Laminar_1601197354926.html'>BIOBASE LAF listing</a>"]],
            caption="Table 1. Search these. Listings change. Buy the spec, not the brand name.",
            foot="Prices move. Freight and a 220–240 V plug matter more than a $40 difference.",
        ),
        h(3, "Message the seller this, copy-paste"),
        p("Send this as one message. If they cannot answer, do not buy."),
        ul([
            "Is the cabinet horizontal laminar flow (not a biosafety cabinet)?",
            "What HEPA grade? H13 or H14? Send the EN1822 (or equivalent) certificate for this filter lot.",
            "Is there a separate pre-filter? What is the replacement HEPA size and price?",
            "What face velocity at the work opening, in m/s?",
            "Voltage and plug: I need 220–240 V (change this if you are on 110 V).",
            "Work opening width in mm? I need at least 400 mm.",
            "Photos of the filter gasket and the fan nameplate before shipping.",
        ]),
        h(3, "What to pay"),
        ul([
            "Desktop / mini metal hood, H13/H14, 400–700 mm wide: often <strong>USD 260–700</strong> plus freight.",
            "Full clean bench (BIOBASE class): often <strong>USD 800–2,000</strong> plus crate freight.",
            "A used Athena-style portable hood from the second-hand market can cost more than a new Chinese bench. Compare the filter spec, not the logo.",
        ]),
        callout("danger", "Do not buy",
                p("Cardboard mushroom boxes with a furnace filter. Vertical “nail salon” tables with no HEPA grade. Anything that says HEPA but shows a foam sheet. A biosafety cabinet unless you already know you need operator protection. It is the wrong tool and costs more.")),
        h(3, "When it arrives"),
        figure(S.fig_hood_setup(), 6, "Unbox. Place. Match voltage. Run empty 30 minutes. Check the air stream with a tissue. Wipe steel only. Log F-12."),
        steps([
            ("Inspect", "HEPA frame not crushed. Plastic still on the filter face. No rattle in the fan."),
            ("Place", "Level, solid bench. 30 cm of free air behind or below the intake, depending on the model. Do not push it into a curtain."),
            ("Power", "Read the plate. 220–240 V units die on 110 V. Use a surge-protected board."),
            ("First run", "Empty hood. Fan on 30 minutes. Listen. Smell for burning."),
            ("Flow check", "Hold a thin tissue strip in the work opening. It should lean steadily toward you (horizontal hood). If it flaps, flaps back, or hangs dead, message the seller before first use."),
            ("Wipe", "70% alcohol on painted steel and the work tray. Never spray liquid into the HEPA face."),
            ("Optional smoke", "A stick of incense 20 cm in front of the filter. Smoke should leave in one sheet, no swirls back onto the bench."),
            ("Log", "Fill F-12. If the tissue hangs dead, do not plate plants."),
        ]),
        form("F-12", "Hood check",
             ["Date", "Hours run", "Tissue-strip pass?", "Noise / smell", "Pre-filter cleaned?", "Sign"],
             rows=8,
             note="Do this on first setup, then monthly, and after any filter change."),
        callout("note", "No hood yet",
                p("Use a still-air box: a clear tub on its side, two arm holes, 70% alcohol wipe, fans off. Same jobs. Slower. Cheaper. The SOP steps do not change.")),
    ]})

# ---------------------------------------------------------------------------
SECTIONS.append({
    "id": "open",
    "kicker": "Job 1",
    "title": "Open the day",
    "blocks": [
        lead("Do this every day you work, before any jar is opened."),
        figure(S.fig_day_open(), 7, "Clothes. Hood on 20 minutes. Wipe room. Wipe hood steel. New gloves. Only today’s tools."),
        steps([
            ("Clothes", "Clean long sleeves. Hair tied. No outdoor shoes in the room. Licensed lab: gown, hair cover, gloves. Log F-13."),
            ("Hood on", "Empty. 20 minutes. If the fan sounds new or burnt, stop."),
            ("F-01", "Floor, bench, door, hood steel, bin."),
            ("Gloves", "New nitrile. Spray 70% alcohol. Spray again after you leave the room."),
            ("Load the hood", "Today’s closed jars, tools, waste bag on the left. Nothing else."),
        ]),
        form("F-13", "Gown / entry (licensed lab). Home: write “home” and skip unused columns.",
             ["Date", "Time in", "Gown", "Hair cover", "Gloves", "Jewellery off", "Time out", "Sign"],
             rows=8),
    ]})

# ---------------------------------------------------------------------------
SECTIONS.append({
    "id": "media",
    "kicker": "Job 2",
    "title": "Mix medium, autoclave, hold 7 days",
    "blocks": [
        lead("One litre. Full-strength MS for start and multiply. Half-strength MS if you are rooting in gel."),
        figure(S.fig_media_steps(), 8, "Water. Salts. Sugar. pH. Agar. Pour. 121 °C / 15 psi / 20 min. Hold 7 days."),
        table(
            ["Ingredient", "1 litre", "Notes"],
            [["RO or distilled water", "start 800 mL, top to 1 L", "Not tap"],
             ["MS basal salts", "4.4 g", "Half = 2.2 g for many rooting mixes"],
             ["Sucrose", "30 g", "Table sugar is fine"],
             ["myo-Inositol", "0.1 g", "Skip only if your MS already has it"],
             ["Activated charcoal", "1 g optional", f"Helps with browning{_c("holmes2021")}"],
             ["Agar", "6–8 g; 9.5 g if shoots go glassy", f"{_c("das2024")}"],
             ["PPM (optional)", "0.5–2 mL", f"Label rate. Not a meristem.{_c("pct_ppm")}"],
             ["pH", "5.6–5.8 before agar", "Then autoclave"]],
            caption="Table 2. Default cannabis medium.",
        ),
        table(
            ["If you want", "Add this after you know MS works", "Dose"],
            [["Start (classic)", "TDZ + NAA", f"1 µM + 0.5 µM{_c("holmes2021")}{_c("lata2009")}"],
             ["Start (gentler)", "meta-Topolin", f"0.48 mg/L{_c("lata2016")}{_c("das2024")}"],
             ["Long multiply", "No hormone + extra calcium", f"Ca nitrate 0.71 g/L + Ca gluconate 1.35 g/L{_c("das2024")}"],
             ["Root in gel", "IBA", f"5 µM. More is worse.{_c("holmes2021")}"]],
            caption="Table 3. Hormones. Change one at a time.",
        ),
        steps([
            ("Weigh", "Write every mass on F-03 before you pour."),
            ("pH", "5.6–5.8 before agar. Dilute acid down. Dilute base up."),
            ("Agar + heat", "Dissolve. Pour jars one-third full. Lids loose."),
            ("Autoclave", "Stovetop canner that holds 15 psi, or an autoclave. 121 °C, 15 psi, 20 minutes. Instant Pots do not count. Jars on a rack, not drowned."),
            ("Cool", "Tighten lids when cool enough to handle. Label lot number on every jar."),
            ("Hold", "Shelf 7 days. Any cloud or fuzz: bin the whole lot. Do not plate into it."),
        ]),
        form("F-02", "Autoclave / canner load",
             ["Date", "Load ID", "121 °C?", "15 psi?", "20 min?", "Cool / dry", "Fail?", "Sign"],
             rows=6,
             note="If any of 121 / 15 / 20 is no, discard the load."),
        form("F-03", "Media batch",
             ["Lot no.", "Date", "MS g", "Sugar g", "Agar g", "pH", "Hormone", "PPM mL", "Jars n", "Day-7 clear?", "Sign"],
             rows=6,
             note="Lot no. = YYYY-MM-DD-MED-NN. Carry this number onto F-04."),
    ]})

# ---------------------------------------------------------------------------
SECTIONS.append({
    "id": "cut",
    "kicker": "Job 3",
    "title": "Take the piece and surface-sterilise it",
    "blocks": [
        lead("First runs: a stem piece with one bud, 10–15 mm. Not a meristem."),
        figure(S.fig_bleach_steps(), 9, "Cut. Soap. 70% alcohol 30–60 s. Bleach 20–30 min. Rinse three times. Trim the burned ends in the hood."),
        steps([
            ("Mother", "Vegetative. Scouted. Young if you can. One cultivar."),
            ("Cut", "Morning. 10–15 mm. Strip large leaves. Keep wet."),
            ("Soap wash", "Tap water + a drop of dish soap or Tween-20. 10–20 min."),
            ("70% alcohol", "30–60 seconds. Drain."),
            ("Bleach", f"Holmes: 10% household bleach (about 0.625% NaOCl) + 0.1% Tween-20, 20 min, stir.{_c("holmes2021")} Das: 1% NaOCl for 30 min.{_c("das2024")} Do not go to 60 min."),
            ("Rinse", "Sterile water, three times, 3–5 min each. Then into the hood."),
            ("Trim", "Cut off white or cooked ends. That cut face goes into the gel."),
        ]),
        photo(f"{IMG}/04-nodal-explant.jpg",
              "A stem piece with one bud. This is the first-run cut.",
              alt="Cannabis nodal explant",
              model="Grok Imagine · illustration"),
    ]})

# ---------------------------------------------------------------------------
SECTIONS.append({
    "id": "plate",
    "kicker": "Job 4",
    "title": "Plate, label, shelf",
    "blocks": [
        lead("One piece, one jar, until you know your rate."),
        figure(S.fig_plate_steps(), 10, "Open one jar in the air stream. Stand the piece. Lid on. Label. Shelf. Scout day 7."),
        figure(F.fig_lab(), 11, "Open jars only in the centre of the hood. Tools on the left. Waste on the left front."),
        steps([
            ("Air stream", "Work 10–20 cm in front of the filter, not at the very edge."),
            ("One lid", "Face down to the side. Never above the jar."),
            ("Plant", "Cut base in the gel. Bud above."),
            ("Lid", "On at once. Do not talk over the jar."),
            ("Label", "Cultivar, date, explant type, lot number from F-03."),
            ("Shelf", "24–26 °C. 16–18 h light. About 70–100 µmol m⁻² s⁻¹. Do not open to look."),
        ]),
        form("F-04", "Initiation / plate",
             ["Lot no.", "Cultivar", "Explant", "n plated", "Medium lot", "Date", "Day-7 clean n", "Day-21 clean n", "Sign"],
             rows=8,
             note="n plated must equal what you put in. Day-7 + dumped = n plated."),
    ]})

# ---------------------------------------------------------------------------
SECTIONS.append({
    "id": "scout",
    "kicker": "Job 5",
    "title": "Scout and bin",
    "blocks": [
        lead("Day 7 and day 21. Look through the glass. Do not open a doubtful jar."),
        figure(S.fig_scout(), 12, "Keep. Bin. Watch. If you hesitate, it is a bin."),
        photo(f"{IMG}/09-contamination.jpg",
              "Left: bacteria. Right: fungus. Seal. Bag. Bin. Not in the hood you still use.",
              alt="Dirty jars",
              model="Grok Imagine · illustration"),
        photo(f"{IMG}/10-phenolic-browning.jpg",
              "Brown ring = leak from the cut, not always microbes. Still do not open it next to clean work. Move survivors to fresh charcoal medium.",
              alt="Browning",
              model="Grok Imagine · illustration"),
        photo(f"{IMG}/13-hyperhydricity.jpg",
              "Wet, see-through leaves = too much hormone or water. Next multiply: no cytokinin, 9.5 g/L agar, vented lid.",
              alt="Glassy shoots",
              model="Grok Imagine · illustration"),
        form("F-07", "Contamination cull",
             ["Date", "Lot no.", "Jar ID", "Bacteria / fungus / brown / glass", "Action (bin / watch)", "Sign"],
             rows=10,
             note="Every dumped jar gets a line. This is how you see if technique is improving."),
    ]})

# ---------------------------------------------------------------------------
SECTIONS.append({
    "id": "multiply",
    "kicker": "Job 6",
    "title": "Multiply every 3–4 weeks",
    "blocks": [
        lead("Only from jars that were clean at day 21. New jar every time."),
        figure(FX.fig_subculture(), 13, "Recut. Fresh medium. New lot line on F-05."),
        photo(f"{IMG}/07-multiplication-shoots.jpg",
              "What you are copying: green divided leaves, clear amber gel, no cloud.",
              alt="Clean multiply jar",
              model="Grok Imagine · illustration"),
        steps([
            ("Source", "A day-21 clean jar. One cultivar."),
            ("Cut", "15–25 mm shoot tip or a node with a visible bud."),
            ("New jar", f"Same medium or the no-hormone + calcium mix.{_c("das2024")}"),
            ("Density", "Home: 1–3 per jar. Licensed: what your F-07 rate allows."),
            ("Clock", f"3–4 weeks. Restart the line from a tested mother by about five recuts.{_c("torkamaneh2024")}"),
        ]),
        form("F-05", "Subculture",
             ["Date", "From lot", "New lot", "Cultivar", "n moved", "Medium lot", "Day-21 clean n", "Sign"],
             rows=8),
    ]})

# ---------------------------------------------------------------------------
SECTIONS.append({
    "id": "meristem",
    "kicker": "Job 7",
    "title": "Meristem cut (only after Jobs 1–6 work)",
    "blocks": [
        lead("Microscope. 0.2–0.4 mm. Then a lab test. This job does not make a plant “clean” by itself."),
        figure(FP.fig_meristem_setup(), 14, "Same five zones as the hood layout. Microscope in the middle."),
        figure(FP.fig_meristem_tools(), 15, "Microscope, fine forceps, #11 scalpel, black dish, beads, 70% alcohol."),
        figure(FP.fig_meristem_hands(), 16, "Left holds. Right cuts."),
        figure(FP.fig_meristem_sequence(), 17, "Eight movements. Do not skip to the nick."),
        figure(FP.fig_meristem_scope(), 18, "Stop peeling when you see a pale dome and two tiny leaves."),
        photo(f"{IMG}/14-meristem-tools.jpg",
              "Tool kit.",
              alt="Meristem tools",
              model="Grok Imagine · illustration"),
        photo(f"{IMG}/16-meristem-hands.jpg",
              "Left forceps, right scalpel. Same grip when the piece is 1 mm.",
              alt="Peeling a tip",
              model="Grok Imagine · illustration"),
        photo(f"{IMG}/17-meristem-dome-cut.jpg",
              "Dome plus two tiny leaves. Cut just below. That piece is 0.2–0.4 mm.",
              alt="Meristem dome",
              model="Grok Imagine · illustration"),
        steps([
            ("New flush", "10–15 mm vegetative tip. Strip large leaves before the hood."),
            ("Sterile tools", "Beads ~250 °C, 20 s, then cool."),
            ("Dish", "One drop sterile water. 10–20× then 30–40×."),
            ("Peel", "Outer leaves off. Stop at two tiny leaves."),
            ("Bleach that tip", "Shorter bleach than a woody node. Rinse."),
            ("One nick", f"0.2–0.4 mm.{_c("hlvd_mgmt2025")} Onto Holmes-type start medium.{_c("holmes2021")}"),
            ("Wait", "4–8 weeks. Then F-10. Expect about 41% negative at six months, not 100%."),
        ]),
        form("F-06", "Meristem cut",
             ["Date", "Mother ID", "n tips", "n plated", "Medium lot", "n alive wk 8", "F-10 result", "Sign"],
             rows=6),
    ]})

# ---------------------------------------------------------------------------
SECTIONS.append({
    "id": "root",
    "kicker": "Job 8",
    "title": "Root, then harden",
    "blocks": [
        lead("A shoot with no roots is not a plant. After roots, lower humidity in steps."),
        photo(f"{IMG}/08-rooted-plantlet.jpg",
              "White roots in clear gel. No brown ring.",
              alt="Rooted plantlet",
              model="Grok Imagine · illustration"),
        photo(f"{IMG}/11-acclimatization.jpg",
              "Plugs under a dome. Vents half at day 7. Lid off at day 14.",
              alt="Harden",
              model="Grok Imagine · illustration"),
        figure(F.fig_acclim(), 19, "Do not put a jar plant onto a dry bench."),
        steps([
            ("Pick", "2–4 cm shoot. Not glassy. Not brown."),
            ("Root", f"Option A: 5 µM IBA in gel, 2–4 weeks.{_c("holmes2021")} Option B: dip the base in 15 mM IBA for 2–4 min, then a sterile plug.{_c("ioannidis2022")} Option C: rockwool, ordinary fertiliser, vented jar, no sugar.{_c("kodym2019")}"),
            ("Plug", "Rockwool or coco soaked in mild veg nutrient, pH about 5.8."),
            ("Dome", "Mist the walls. 16 h light. Gentle. 24 °C."),
            ("Vents", "Day 7 half. Day 9 full. Day 14 lid off."),
            ("Pot", "Treat as a new clone. No 12-hour days for several weeks."),
        ]),
        form("F-08", "Rooting",
             ["Date", "From lot", "Method (gel / dip / no-sugar)", "n", "n rooted wk 4", "Sign"],
             rows=6),
        form("F-09", "Harden",
             ["Date out", "Lot", "Plug type", "n", "n alive day 14", "Sign"],
             rows=6),
    ]})

# ---------------------------------------------------------------------------
SECTIONS.append({
    "id": "index",
    "kicker": "Job 9",
    "title": "Test, intake, and the lot register",
    "blocks": [
        lead("If F-10 is blank, the plant is a clone. Not a clean mother."),
        figure(FX.fig_hlvd_clearance(), 20, "Cut. Grow new leaves. Sample. Freeze a retain. Test again."),
        steps([
            ("Sample", "New fully expanded leaf or the leaf stalk, after the plant has grown."),
            ("Lab", "A lab that runs cannabis Hop latent viroid RT-qPCR. Roots are the most reliable tissue if they will take them."),
            ("Retest", "3–4 weeks later, and before a mother enters production."),
            ("Retain", "Freeze spare tissue from every pass lot."),
        ]),
        form("F-10", "Index / qPCR",
             ["Date", "Plant / lot", "Tissue", "Lab", "HpLVd", "Other", "Retain ID", "Pass?", "Sign"],
             rows=8,
             note="Pass = not detected. Anything else = quarantine or destroy. Do not write “clean” in this column."),
        form("F-11", "Mother intake / quarantine",
             ["Date in", "Cultivar", "Source", "Room", "Pests?", "F-10 date", "F-10 result", "Release / destroy", "Sign"],
             rows=6),
        form("F-14", "Lot register",
             ["Lot no.", "Opened", "Closed", "Cultivar", "F-03", "F-04 n", "F-07 dumped", "F-10", "Fate"],
             rows=10,
             note="One line per lot. Fate = multiply / root / mother / destroy."),
        callout("warn", "Tools after a dirty plant",
                p(f"70% alcohol does not destroy Hop latent viroid RNA. Use 5–10% household bleach for 1–2 minutes, or 1000 ppm hypochlorous acid for 1 minute, then rinse.{_c("hlvd_mgmt2025")} Dedicated blades per cultivar if you can.")),
    ]})

# ---------------------------------------------------------------------------
SECTIONS.append({
    "id": "week",
    "kicker": "Job 10",
    "title": "The week",
    "blocks": [
        table(
            ["Day", "Home", "Licensed"],
            [["Mon", "F-01. Pour Sunday’s medium.", "F-01 + F-13. Media kitchen: F-02, F-03."],
             ["Tue", "Plate 10–20 nodes. F-04.", "Plate from F-11 released mothers only."],
             ["Wed", "Multiply day-21 cleans. F-05.", "One cultivar per hood. F-05."],
             ["Thu", "Scout. F-07.", "Scout + photo lots. F-07."],
             ["Fri", "Root or dip. F-08. Send F-10 if due.", "qPCR batch. Quarantine fails."],
             ["Sat–Sun", "Do not open jars.", "Alarms only."]],
            caption="Table 4. If the form is blank, the job did not happen.",
        ),
        ul([
            f"Plan about 80–100 transfers per hour at a hood once you are practised.{_c("pct_howto")}",
            "Test production mothers every 3–6 weeks (F-10).",
            f"Restart a production line by about five recuts from a tested backup.{_c("torkamaneh2024")}",
        ]),
    ]})

# ---------------------------------------------------------------------------
SECTIONS.append({
    "id": "fix",
    "kicker": "Job 11",
    "title": "If it fails, change one thing",
    "blocks": [
        table(
            ["What you see", "Change this only"],
            [[">50% dirty by day 7", "Slower hands. Younger mother. Smaller tip."],
             [">50% dirty after day 14", f"Meristem (Job 7). Optional 4–5% PPM soak.{_c("pct_ppm")} Change mother substrate."],
             ["Brown in 48 h", "Shorter bleach. Charcoal. Trim ends."],
             ["Glassy leaves", "No cytokinin. 9.5 g/L agar. Vented lid."],
             ["No roots week 5", "5 µM IBA, or a 15 mM dip, not more hormone."],
             ["Dies under the dome", "Longer half-vent. Rockwool, not a bubbler."],
             ["Looks fine, duds in flower", "F-10 was skipped."]],
            caption="Table 5. One variable per run.",
        ),
    ]})

# ---------------------------------------------------------------------------
SECTIONS.append({
    "id": "sources",
    "kicker": "12",
    "title": "Sources",
    "blocks": [
        p("Stars in the text point here. You do not need this page to run a day."),
        p("Photographs are illustrations. Diagrams are the ones to follow for size and order."),
        callout("note", "Legal",
                p("Only grow cannabis where you are allowed to. This SOP is horticultural, not legal advice.")),
    ]})
