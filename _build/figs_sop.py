# -*- coding: utf-8 -*-
"""Step diagrams for the cannabis TC SOP."""
G = "var(--fig-green)"; GD = "var(--fig-green-d)"; GL = "var(--fig-green-l)"; GXL = "var(--fig-green-xl)"
INK = "var(--fig-ink)"; INK2 = "var(--fig-ink2)"; MUT = "var(--fig-mut)"; LINE = "var(--fig-line)"
AMB = "var(--fig-amber)"; AMBL = "var(--fig-amber-l)"; RED = "var(--fig-red)"; REDL = "var(--fig-red-l)"
BLU = "var(--fig-blue)"; BLUL = "var(--fig-blue-l)"; PUR = "var(--fig-purple)"; PURL = "var(--fig-purple-l)"
PAPER = "var(--fig-bg)"
FS = "font-family:-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif"
MN = "font-family:ui-monospace,Consolas,monospace"


def _svg(W, H, label, body):
    return (f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
            f'xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{label}">'
            f'<rect width="{W}" height="{H}" fill="{PAPER}"/>{body}</svg>')


def _title(t, y=22):
    return f'<text x="20" y="{y}" fill="{INK}" font-size="14.5" font-weight="700" style="{FS}">{t}</text>'


def _panel(x, y, w, h, n, title, lines, fill=None, col=None):
    fill = fill or GXL
    col = col or GD
    s = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="9" fill="{fill}" stroke="{col}"/>']
    s.append(f'<circle cx="{x+16}" cy="{y+16}" r="11" fill="{col}"/>')
    s.append(f'<text x="{x+16}" y="{y+20}" text-anchor="middle" fill="#fff" font-size="11" font-weight="700" style="{MN}">{n}</text>')
    s.append(f'<text x="{x+32}" y="{y+20}" fill="{INK}" font-size="12" font-weight="700" style="{FS}">{title}</text>')
    for i, ln in enumerate(lines):
        s.append(f'<text x="{x+12}" y="{y+40+i*14}" fill="{INK2}" font-size="11" style="{FS}">{ln}</text>')
    return "".join(s)


def fig_sop_map():
    steps = [
        ("0", "Room + hood", "Clean the room. Purchase and install the hood."),
        ("1", "Opening procedure", "Clean. Operate the hood for 20 min. Put on a gown."),
        ("2", "Mix medium", "Weigh. pH. Agar. Fill jars. Sterilize."),
        ("3", "Hold 7 days", "Monitor jars. Discard a jar with a cloud."),
        ("4", "Cut + sterilize", "Cut the piece. Sterilize its surface."),
        ("5", "Put in jars", "One piece in one jar. Make a label. Put the lid on."),
        ("6", "Examine", "Day 7 and 21. Discard dirty jars."),
        ("7", "Multiplication", "Do a subculture of the clean shoots each 3–4 weeks."),
        ("8", "Meristem", "Microscope cut, if you must remove disease."),
        ("9", "Rooting", "IBA in gel, or a dip, then a plug."),
        ("10", "Acclimatization", "Dome. Open the vents. Then a pot."),
        ("11", "Test", "Send tissue for HpLVd qPCR."),
    ]
    W, H = 760, 430
    parts = [_title("SOP tasks. Do them in sequence.")]
    for i, (n, t, d) in enumerate(steps):
        col, row = i % 4, i // 4
        x, y = 16 + col * 186, 40 + row * 124
        parts.append(_panel(x, y, 176, 112, n, t, [d[:28], d[28:] if len(d) > 28 else ""]))
    return _svg(W, H, "SOP map", "".join(parts))


def fig_room_treat():
    items = [
        ("1", "Empty", "Remove all items.", "No plants. No cardboard."),
        ("2", "Clean", "Warm water + detergent.", "Walls, floor, bench, door."),
        ("3", "Bleach", "10% household bleach.", "Keep wet 10 min. Flush."),
        ("4", "Alcohol", "70% ethanol or IPA.", "Clean. Let it dry."),
        ("5", "Seal gaps", "Use tape. No carpet.", "Door sweep if you can."),
        ("6", "Hold", "Hood on 30 min.", "Then start work."),
    ]
    W, H = 760, 250
    parts = [_title("Prepare the room one time, before first use")]
    for i, (n, t, a, b) in enumerate(items):
        x = 16 + (i % 6) * 124
        parts.append(_panel(x, 40, 116, 190, n, t, [a, b], GL if i < 4 else AMBL, GD if i < 4 else AMB))
    return _svg(W, H, "Room treatment", "".join(parts))


def fig_hood_buy():
    W, H = 760, 300
    parts = [_title("Hood to purchase. Horizontal flow. H13 or H14 HEPA.")]
    rows = [
        ("Must have", GL, GD, [
            "Horizontal laminar flow (air to you)",
            "H13 or H14 HEPA, plus a pre-filter",
            "Metal cabinet. No cardboard. No grow tent",
            "Work opening width: minimum 400 mm",
        ]),
        ("Message to the seller", BLUL, BLU, [
            "EN1822 or equivalent filter certificate",
            "Face velocity 0.30–0.50 m/s (photos + data)",
            "Replacement HEPA size and price",
            "Voltage 220–240 V if you are in AU/NZ/EU",
        ]),
        ("Do not purchase", REDL, RED, [
            "Vertical “biosafety” cabinets for this task",
            "No pre-filter, foam-only, or “HEPA-like”",
            "UV only (it does not replace the hood)",
            "Used filters. Get a new sealed HEPA",
        ]),
    ]
    for i, (t, fill, col, lines) in enumerate(rows):
        x = 16 + i * 248
        parts.append(f'<rect x="{x}" y="44" width="236" height="236" rx="10" fill="{fill}" stroke="{col}"/>')
        parts.append(f'<text x="{x+16}" y="72" fill="{INK}" font-size="14" font-weight="700" style="{FS}">{t}</text>')
        for j, ln in enumerate(lines):
            parts.append(f'<text x="{x+16}" y="{100+j*36}" fill="{INK2}" font-size="12" style="{FS}">{ln}</text>')
    return _svg(W, H, "Hood buy checklist", "".join(parts))


def fig_hood_flow():
    W, H = 760, 260
    parts = [_title("Hood operation. Air in one direction. You are in front.")]
    # box
    parts.append(f'<rect x="80" y="70" width="520" height="150" rx="8" fill="{GXL}" stroke="{GD}" stroke-width="2"/>')
    parts.append(f'<rect x="80" y="70" width="70" height="150" fill="{BLUL}" stroke="{BLU}"/>')
    parts.append(f'<text x="115" y="130" text-anchor="middle" fill="{BLU}" font-size="11" font-weight="700" style="{FS}">Pre-filter</text>')
    parts.append(f'<text x="115" y="146" text-anchor="middle" fill="{BLU}" font-size="11" font-weight="700" style="{FS}">+HEPA</text>')
    for y in (90, 120, 150, 180):
        parts.append(f'<path d="M160,{y} L560,{y}" stroke="{BLU}" stroke-width="2" marker-end="url(#a)"/>')
    parts.append('<defs><marker id="a" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="var(--fig-blue)"/></marker></defs>')
    parts.append(f'<text x="360" y="64" text-anchor="middle" fill="{INK2}" font-size="12" style="{FS}">clean air sheet  →  0.30–0.50 m/s</text>')
    parts.append(f'<text x="360" y="248" text-anchor="middle" fill="{INK2}" font-size="12" style="{FS}">You are here. Do not put objects on or in front of the filter. Do not put high jars behind an open jar.</text>')
    parts.append(f'<rect x="620" y="110" width="90" height="70" rx="8" fill="{PURL}" stroke="{PUR}"/>')
    parts.append(f'<text x="665" y="150" text-anchor="middle" fill="{PUR}" font-size="12" font-weight="700" style="{FS}">you</text>')
    return _svg(W, H, "Hood airflow", "".join(parts))


def fig_hood_setup():
    items = [
        ("1", "Remove packaging", "Do a check of the HEPA seal.", "No damage at the corners."),
        ("2", "Position", "Level, stable bench.", "30 cm free air behind the intake."),
        ("3", "Voltage", "Use the nameplate voltage.", "Power board + surge protection."),
        ("4", "First operation", "On for 30 minutes.", "Empty. No work at this time."),
        ("5", "Flow check", "Tissue strip in the airflow.", "It bends out and stays stable."),
        ("6", "Clean", "70% alcohol on steel.", "Do not spray the HEPA face."),
        ("7", "Record", "Form F-12.", "Date, velocity, result."),
        ("8", "Each day", "On 20 min before work.", "Clean. Then start."),
    ]
    W, H = 760, 310
    parts = [_title("Hood setup, first day")]
    for i, (n, t, a, b) in enumerate(items):
        x = 16 + (i % 4) * 186
        y = 40 + (i // 4) * 130
        parts.append(_panel(x, y, 176, 118, n, t, [a, b]))
    return _svg(W, H, "Hood setup steps", "".join(parts))


def fig_day_open():
    items = [
        ("1", "Clothing", "Clean. Hair up.", "No outdoor shoes in the room."),
        ("2", "Hood on", "20 minutes empty.", "Listen for the fan."),
        ("3", "Clean room", "70% alcohol, bench + door.", "Form F-01."),
        ("4", "Clean hood", "Steel only. Rear to front.", "Not the filter face."),
        ("5", "Gloves", "New nitrile. Spray 70%.", "Spray after you go out."),
        ("6", "Tools in", "Only jars + tools to use.", "Waste bag on the left."),
    ]
    W, H = 760, 250
    parts = [_title("Start of each work day")]
    for i, (n, t, a, b) in enumerate(items):
        x = 16 + (i % 6) * 124
        parts.append(_panel(x, 40, 116, 190, n, t, [a, b]))
    return _svg(W, H, "Daily open", "".join(parts))


def fig_media_steps():
    items = [
        ("1", "Water", "800 mL RO or distilled water", "in a 1 L flask or pot."),
        ("2", "Salts + sugar", "MS 4.4 g. Sugar 30 g.", "Mix until dissolved."),
        ("3", "Other ingredients", "myo-Inositol 0.1 g.", "Charcoal 1 g optional."),
        ("4", "pH", "Set to 5.6–5.8.", "Before agar."),
        ("5", "Agar", "6–8 g (9.5 g if glassy growth).", "Dissolve with heat."),
        ("6", "Fill jars", "To 1/3 of each jar.", "Loose lids."),
        ("7", "Sterilize", "121 °C / 15 psi / 20 min.", "Form F-02 + F-03."),
        ("8", "Hold", "7 days on the shelf.", "Discard jars with a cloud."),
    ]
    W, H = 760, 310
    parts = [_title("Mix and sterilize 1 liter of medium")]
    for i, (n, t, a, b) in enumerate(items):
        x = 16 + (i % 4) * 186
        y = 40 + (i // 4) * 130
        parts.append(_panel(x, y, 176, 118, n, t, [a, b]))
    return _svg(W, H, "Media steps", "".join(parts))


def fig_bleach_steps():
    items = [
        ("1", "Cut", "10–15 mm tip or node.", "Remove large leaves."),
        ("2", "Clean + soap", "Tap water + drop", "of soap. 10–20 min."),
        ("3", "70% alcohol", "30–60 seconds.", "Then drain."),
        ("4", "Bleach", "0.6–1% NaOCl + Tween.", "20–30 min, mix."),
        ("5", "Clean ×3", "Sterilized water.", "3–5 min each."),
        ("6", "Cut ends", "In the hood. Remove", "bleach damage."),
    ]
    W, H = 760, 250
    parts = [_title("Sterilize the surface of the explant")]
    for i, (n, t, a, b) in enumerate(items):
        x = 16 + i * 124
        parts.append(_panel(x, 40, 116, 190, n, t, [a, b]))
    return _svg(W, H, "Bleach steps", "".join(parts))


def fig_plate_steps():
    items = [
        ("1", "Open one jar", "In the airflow.", "Lid face down, to the side."),
        ("2", "Put the piece", "Cut end in the gel.", "Bud above the gel."),
        ("3", "Lid on", "Immediately.", "Do not speak near it."),
        ("4", "Label", "Cultivar, date, type.", "Form F-04."),
        ("5", "Shelf", "24–26 °C, 16 h light.", "Do not open to look."),
        ("6", "Day 7", "Examine. Discard", "dirty jars. Form F-07."),
    ]
    W, H = 760, 250
    parts = [_title("Put one piece in a jar")]
    for i, (n, t, a, b) in enumerate(items):
        x = 16 + i * 124
        parts.append(_panel(x, 40, 116, 190, n, t, [a, b]))
    return _svg(W, H, "Plate steps", "".join(parts))


def fig_scout():
    W, H = 760, 220
    parts = [_title("Examine. Three results.")]
    cards = [
        ("Keep", GL, GD, "Transparent gel. Green tissue.", "No odor. No mold.", "Keep it closed."),
        ("Discard", REDL, RED, "Cloud, slime, or mold.", "Or an unusual odor.", "Seal in a bag. Discard. Record F-07."),
        ("Monitor", AMBL, AMB, "A small cloud, day 3–5.", "Do not open it.", "Examine again on day 7 and 21."),
    ]
    for i, (t, fill, col, a, b, c) in enumerate(cards):
        x = 20 + i * 246
        parts.append(f'<rect x="{x}" y="44" width="232" height="156" rx="10" fill="{fill}" stroke="{col}"/>')
        parts.append(f'<text x="{x+16}" y="74" fill="{INK}" font-size="15" font-weight="700" style="{FS}">{t}</text>')
        parts.append(f'<text x="{x+16}" y="104" fill="{INK2}" font-size="13" style="{FS}">{a}</text>')
        parts.append(f'<text x="{x+16}" y="126" fill="{INK2}" font-size="13" style="{FS}">{b}</text>')
        parts.append(f'<text x="{x+16}" y="156" fill="{INK}" font-size="12.5" style="{FS}">{c}</text>')
    return _svg(W, H, "Scout outcomes", "".join(parts))


def fig_paper_pack():
    W, H = 760, 340
    parts = [_title("Paper forms. Fill these. Write the lot number each time.")]
    forms = [
        ("F-01", "Room clean each day"),
        ("F-02", "Autoclave load"),
        ("F-03", "Media batch"),
        ("F-04", "Initiation / put in jars"),
        ("F-05", "Subculture"),
        ("F-06", "Meristem cut"),
        ("F-07", "Contamination discarded jars"),
        ("F-08", "Rooting"),
        ("F-09", "Acclimatization"),
        ("F-10", "Indexing / qPCR"),
        ("F-11", "Mother plant intake"),
        ("F-12", "Hood check"),
        ("F-13", "Gown / entry"),
        ("F-14", "Lot record"),
    ]
    for i, (code, name) in enumerate(forms):
        x = 16 + (i % 7) * 106
        y = 44 + (i // 7) * 140
        parts.append(f'<rect x="{x}" y="{y}" width="98" height="128" rx="8" fill="{GXL}" stroke="{GD}"/>')
        parts.append(f'<text x="{x+49}" y="{y+40}" text-anchor="middle" fill="{GD}" font-size="13" font-weight="700" style="{MN}">{code}</text>')
        words = name.split()
        parts.append(f'<text x="{x+49}" y="{y+70}" text-anchor="middle" fill="{INK}" font-size="11" style="{FS}">{words[0]}</text>')
        if len(words) > 1:
            parts.append(f'<text x="{x+49}" y="{y+86}" text-anchor="middle" fill="{INK}" font-size="11" style="{FS}">{" ".join(words[1:])}</text>')
    return _svg(W, H, "Forms pack", "".join(parts))
