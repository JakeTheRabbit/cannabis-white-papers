# -*- coding: utf-8 -*-
"""Extra annotated SVGs for the cannabis TC playbook. Theme vars match CWP figs.py."""
G = "var(--fig-green)"; GD = "var(--fig-green-d)"; GL = "var(--fig-green-l)"; GXL = "var(--fig-green-xl)"
INK = "var(--fig-ink)"; INK2 = "var(--fig-ink2)"; MUT = "var(--fig-mut)"; LINE = "var(--fig-line)"
AMB = "var(--fig-amber)"; AMBL = "var(--fig-amber-l)"; RED = "var(--fig-red)"; REDL = "var(--fig-red-l)"
BLU = "var(--fig-blue)"; BLUL = "var(--fig-blue-l)"; PUR = "var(--fig-purple)"; PURL = "var(--fig-purple-l)"
PAPER = "var(--fig-bg)"
FS = "font-family:-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif"
MN = "font-family:ui-monospace,Consolas,monospace"


def fig_stem_xsec():
    """Accurate young cannabis (dicot) stem transverse section — eustele, not succulent."""
    W, H = 760, 420
    p = [f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="A section across a young stem of Cannabis sativa, with notes">']
    p.append(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')
    p.append(f'<text x="24" y="28" fill="{INK}" font-size="15" font-weight="700" style="{FS}">New cannabis stem, cut across</text>')
    p.append(f'<text x="24" y="46" fill="{INK2}" font-size="12" style="{FS}">Sap tubes are in a ring around the pith. HpLVd moves in the sap. At this stage, the meristem tip above this section has no sap tubes.</text>')
    cx, cy, R = 250, 240, 150
    # epidermis + cortex
    p.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="{GL}" stroke="{G}" stroke-width="2"/>')
    p.append(f'<circle cx="{cx}" cy="{cy}" r="{R-18}" fill="{GXL}" stroke="{LINE}"/>')
    # pith
    p.append(f'<circle cx="{cx}" cy="{cy}" r="62" fill="#f4efe4" stroke="{LINE}"/>')
    p.append(f'<text x="{cx}" y="{cy+4}" text-anchor="middle" fill="{MUT}" font-size="11" style="{FS}">pith</text>')
    # vascular bundles in a ring
    import math
    n = 10
    for i in range(n):
        a = -math.pi/2 + i * 2*math.pi/n
        bx = cx + math.cos(a)*98
        by = cy + math.sin(a)*98
        # phloem (outer, red = pathogen highway)
        p.append(f'<ellipse cx="{bx+math.cos(a)*10}" cy="{by+math.sin(a)*10}" rx="11" ry="16" transform="rotate({a*180/math.pi} {bx} {by})" fill="{REDL}" stroke="{RED}" stroke-width="1.2"/>')
        # xylem (inner)
        p.append(f'<ellipse cx="{bx-math.cos(a)*10}" cy="{by-math.sin(a)*10}" rx="10" ry="14" transform="rotate({a*180/math.pi} {bx} {by})" fill="{BLUL}" stroke="{BLU}" stroke-width="1.2"/>')
    # epidermis ticks (hairs)
    for i in range(16):
        a = i * 2*math.pi/16
        x1 = cx + math.cos(a)*(R-1)
        y1 = cy + math.sin(a)*(R-1)
        x2 = cx + math.cos(a)*(R+12)
        y2 = cy + math.sin(a)*(R+12)
        p.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{GD}" stroke-width="1.2"/>')
    # callouts
    lx = 470
    def cl(y, col, t1, t2):
        return (f'<circle cx="{lx}" cy="{y}" r="6" fill="{col}"/>'
                f'<text x="{lx+16}" y="{y+4}" fill="{INK}" font-size="13.5" font-weight="700" style="{FS}">{t1}</text>'
                f'<text x="{lx+16}" y="{y+22}" fill="{INK2}" font-size="11.5" style="{FS}">{t2}</text>')
    p.append(cl(90, GD, "Epidermis + hairs", "Outer skin. Bleach on the surface can touch it."))
    p.append(cl(150, G, "Cortex", "Packing tissue. Endophytes are deeper."))
    p.append(cl(210, RED, "Phloem (outer part of each bundle)", "Sap. HpLVd moves here."))
    p.append(cl(270, BLU, "Xylem (inner part of each bundle)", "Water from the roots. HpLVd does not move here."))
    p.append(cl(330, AMB, "Pith", "Soft center. Fungi can be here (Holmes 2021)."))
    p.append(f'<text x="24" y="{H-16}" fill="{MUT}" font-size="11" style="{FS}">A stem piece with one bud includes all of this ring of sap tubes. A 0.2–0.5 mm meristem dome does not.</text>')
    p.append('</svg>')
    return "".join(p)


def fig_hormone():
    W, H = 760, 280
    p = [f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="The ratio of the hormones cytokinin and auxin. High cytokinin causes shoots, and high auxin causes roots.">']
    p.append(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')
    p.append(f'<text x="24" y="28" fill="{INK}" font-size="15" font-weight="700" style="{FS}">The two hormones that you must know</text>')
    # left cytokinin
    p.append(f'<rect x="24" y="50" width="330" height="190" rx="12" fill="{GL}" stroke="{G}"/>')
    p.append(f'<text x="189" y="82" text-anchor="middle" fill="{GD}" font-size="16" font-weight="700" style="{FS}">Cytokinin high</text>')
    p.append(f'<text x="189" y="108" text-anchor="middle" fill="{INK}" font-size="13" style="{FS}">mT · TDZ · BA</text>')
    p.append(f'<text x="189" y="140" text-anchor="middle" fill="{INK2}" font-size="13" style="{FS}">Causes SHOOTS</text>')
    p.append(f'<text x="189" y="164" text-anchor="middle" fill="{INK2}" font-size="12" style="{FS}">Initiation / multiplication</text>')
    p.append(f'<text x="189" y="196" text-anchor="middle" fill="{MUT}" font-size="11.5" style="{FS}">Too much → glassy growth (hyperhydricity)</text>')
    p.append(f'<text x="189" y="216" text-anchor="middle" fill="{MUT}" font-size="11.5" style="{FS}">in shoots and callus. Use less cytokinin.</text>')
    # right auxin
    p.append(f'<rect x="406" y="50" width="330" height="190" rx="12" fill="{BLUL}" stroke="{BLU}"/>')
    p.append(f'<text x="571" y="82" text-anchor="middle" fill="{BLU}" font-size="16" font-weight="700" style="{FS}">Auxin high</text>')
    p.append(f'<text x="571" y="108" text-anchor="middle" fill="{INK}" font-size="13" style="{FS}">IBA · NAA · IAA</text>')
    p.append(f'<text x="571" y="140" text-anchor="middle" fill="{INK2}" font-size="13" style="{FS}">Causes ROOTS</text>')
    p.append(f'<text x="571" y="164" text-anchor="middle" fill="{INK2}" font-size="12" style="{FS}">Rooting, or a dip of the cut bottom end</text>')
    p.append(f'<text x="571" y="196" text-anchor="middle" fill="{MUT}" font-size="11.5" style="{FS}">Too much IBA can decrease</text>')
    p.append(f'<text x="571" y="216" text-anchor="middle" fill="{MUT}" font-size="11.5" style="{FS}">rooting (Holmes: 5 µM &gt; 42 µM).</text>')
    p.append(f'<text x="380" y="150" text-anchor="middle" fill="{INK}" font-size="22" font-weight="700">↔</text>')
    p.append('</svg>')
    return "".join(p)


def fig_home_vs_facility():
    W, H = 760, 340
    p = [f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="The figure compares a home laboratory with a licensed facility">']
    p.append(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')
    rows = [
        ("Clean air", "Still-air box or small hood", "ISO 7 room + ISO 5 laminar-flow hoods"),
        ("Sterilize media", "Pressure cooker, 15 psi / 20 min", "Validated autoclave + load log"),
        ("Task", "Know the method. Keep a cultivar.", "Mother plants + liners (negative test)"),
        ("Condition for “clean”", "You cannot use “clean”", "qPCR to release a lot. Keep backup samples."),
        ("Quantity of work", "Tens of jars", "Hundreds to thousands of vessels each week"),
        ("Records", "Notes + dates on lids", "Batch record, cultivar ID, chain of custody"),
        ("Cost to start", "Approximately $200–550, or $2,000 for a kit", "Capital cost: hoods, autoclave, HVAC, QC"),
    ]
    p.append(f'<rect x="250" y="16" width="230" height="28" rx="8" fill="{GL}"/>')
    p.append(f'<text x="365" y="35" text-anchor="middle" fill="{GD}" font-size="13" font-weight="700" style="{FS}">HOME LAB</text>')
    p.append(f'<rect x="500" y="16" width="240" height="28" rx="8" fill="{BLUL}"/>')
    p.append(f'<text x="620" y="35" text-anchor="middle" fill="{BLU}" font-size="13" font-weight="700" style="{FS}">LICENSED FACILITY</text>')
    for i, (k, a, b) in enumerate(rows):
        y = 56 + i * 38
        p.append(f'<text x="16" y="{y+18}" fill="{INK}" font-size="12.5" font-weight="700" style="{FS}">{k}</text>')
        p.append(f'<rect x="250" y="{y}" width="230" height="32" rx="7" fill="{GXL}" stroke="{LINE}"/>')
        p.append(f'<text x="365" y="{y+21}" text-anchor="middle" fill="{INK2}" font-size="11" style="{FS}">{a}</text>')
        p.append(f'<rect x="500" y="{y}" width="240" height="32" rx="7" fill="{BLUL}" stroke="{LINE}"/>')
        p.append(f'<text x="620" y="{y+21}" text-anchor="middle" fill="{INK2}" font-size="11" style="{FS}">{b}</text>')
    p.append('</svg>')
    return "".join(p)


def fig_facility_flow():
    W, H = 760, 300
    p = [f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="The flow of material in a facility, from dirty areas to clean areas only">']
    p.append(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')
    p.append(f'<text x="24" y="26" fill="{INK}" font-size="15" font-weight="700" style="{FS}">Material flow: from dirty to clean areas only</text>')
    rooms = [
        ("Intake / quarantine", AMBL, AMB, "Mother plants come in.\nExamine the plants."),
        ("Media kitchen", GL, G, "Weigh, fill jars,\nsterilize."),
        ("Transfer room\nISO 7 / hood ISO 5", BLUL, BLU, "Cut, put in jars,\ndo subcultures."),
        ("Growth room", GL, GD, "Shelves, 16 h\nlight, 24–26 °C"),
        ("Hardening / nursery", GXL, G, "Decrease humidity in steps.\nThen vegetative growth."),
        ("QC / indexing", PURL, PUR, "qPCR, keep samples,\nrelease / discard."),
    ]
    for i, (name, fill, col, note) in enumerate(rooms):
        x = 16 + (i % 3) * 248
        y = 48 + (i // 3) * 118
        p.append(f'<rect x="{x}" y="{y}" width="232" height="104" rx="12" fill="{fill}" stroke="{col}" stroke-width="1.6"/>')
        p.append(f'<circle cx="{x+22}" cy="{y+22}" r="12" fill="{col}"/>')
        p.append(f'<text x="{x+22}" y="{y+26}" text-anchor="middle" fill="#fff" font-size="12" font-weight="700" style="{MN}">{i+1}</text>')
        lines = name.split("\n")
        p.append(f'<text x="{x+42}" y="{y+26}" fill="{INK}" font-size="13" font-weight="700" style="{FS}">{lines[0]}</text>')
        if len(lines) > 1:
            p.append(f'<text x="{x+42}" y="{y+42}" fill="{INK}" font-size="12" font-weight="700" style="{FS}">{lines[1]}</text>')
        for j, ln in enumerate(note.split("\n")):
            p.append(f'<text x="{x+16}" y="{y+68+j*16}" fill="{INK2}" font-size="12" style="{FS}">{ln}</text>')
    p.append('</svg>')
    return "".join(p)


def fig_explant_size():
    W, H = 760, 250
    p = [f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="The effect of the size of the explant on how clean it is and on its survival">']
    p.append(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')
    p.append(f'<text x="24" y="26" fill="{INK}" font-size="15" font-weight="700" style="{FS}">The cut piece changes the result</text>')
    cards = [
        ("Nodal segment", "8–15 mm, one bud", "Easy. Keeps the disease.", "Use it for your first batches.", GL, G),
        ("Shoot tip / microtip", "Less than 5 mm", "Internal microbes: a smaller number.", "Best first piece (Das 2024).", BLUL, BLU),
        ("Meristem dome", "0.2–0.5 mm", "Can give a piece with no HpLVd.", "Use a microscope.", PURL, PUR),
    ]
    for i, (t, size, a, b, fill, col) in enumerate(cards):
        x = 20 + i * 246
        p.append(f'<rect x="{x}" y="46" width="232" height="178" rx="12" fill="{fill}" stroke="{col}"/>')
        p.append(f'<text x="{x+16}" y="76" fill="{INK}" font-size="14.5" font-weight="700" style="{FS}">{t}</text>')
        p.append(f'<text x="{x+16}" y="100" fill="{col}" font-size="13" font-weight="700" style="{MN}">{size}</text>')
        p.append(f'<text x="{x+16}" y="136" fill="{INK2}" font-size="12.5" style="{FS}">{a}</text>')
        p.append(f'<text x="{x+16}" y="160" fill="{INK2}" font-size="12.5" style="{FS}">{b}</text>')
    p.append('</svg>')
    return "".join(p)


def fig_meristem_setup():
    W, H = 760, 400
    p = [f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="The layout of the bench in the hood for when you cut a meristem">']
    p.append(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')
    p.append(f'<text x="24" y="26" fill="{INK}" font-size="15" font-weight="700" style="{FS}">Bench layout in the hood or still-air box</text>')
    p.append(f'<text x="24" y="46" fill="{INK2}" font-size="12" style="{FS}">Air blows from the rear of the hood to you. Do not put high objects behind an open jar.</text>')
    p.append(f'<rect x="20" y="58" width="720" height="280" rx="10" fill="{GXL}" stroke="{GD}" stroke-width="2"/>')
    p.append(f'<text x="380" y="78" text-anchor="middle" fill="{MUT}" font-size="11" style="{FS}">REAR OF HOOD  ·  filtered air comes from here</text>')

    def zone(x, y, w, h, n, title, lines, fill, col):
        s = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="{col}"/>']
        s.append(f'<circle cx="{x+16}" cy="{y+16}" r="11" fill="{col}"/>')
        s.append(f'<text x="{x+16}" y="{y+20}" text-anchor="middle" fill="#fff" font-size="12" font-weight="700" style="{MN}">{n}</text>')
        s.append(f'<text x="{x+32}" y="{y+21}" fill="{INK}" font-size="12.5" font-weight="700" style="{FS}">{title}</text>')
        for i, ln in enumerate(lines):
            s.append(f'<text x="{x+12}" y="{y+42+i*15}" fill="{INK2}" font-size="11.5" style="{FS}">{ln}</text>')
        return "".join(s)

    p.append(zone(36, 92, 200, 82, "1", "Tool area", ["Glass-bead sterilizer here.", "On the left of the dish."], AMBL, AMB))
    p.append(zone(250, 92, 260, 140, "2", "Microscope + dish", ["Stereo microscope, 10–40×.", "Black dish below the lens.", "The only open area on the bench."], GL, GD))
    p.append(zone(524, 92, 200, 82, "3", "New medium", ["Closed jars. Open one jar", "only when the piece is prepared."], BLUL, BLU))
    p.append(zone(36, 188, 200, 82, "4", "Waste", ["Removed leaves, used blades.", "Do not move hands above zone 2."], REDL, RED))
    p.append(zone(524, 188, 200, 82, "5", "You", ["Be in front of the hood.", "Hands come from the front."], PURL, PUR))
    p.append(f'<text x="380" y="318" text-anchor="middle" fill="{INK}" font-size="12.5" style="{FS}">Do not move hands above an open jar or the open dish.</text>')
    p.append(f'<text x="24" y="380" fill="{MUT}" font-size="11" style="{FS}">Home: the same five zones in the still-air box. Fans and air-conditioning off.</text>')
    p.append('</svg>')
    return "".join(p)


def fig_meristem_tools():
    W, H = 760, 250
    p = [f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="The tools that you use to cut a meristem">']
    p.append(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')
    p.append(f'<text x="24" y="24" fill="{INK}" font-size="15" font-weight="700" style="{FS}">Tools. Use these. Do not use kitchen knives.</text>')
    tools = [
        ("A", "Stereo microscope", "10–40×. You cannot", "see 0.3 mm without it."),
        ("B", "Small forceps", "Left hand. Holds the", "stem 3–5 mm down."),
        ("C", "#11 scalpel", "Right hand. Blade with", "a point. Cuts leaves."),
        ("D", "Black dish", "Black. Thus the pale", "dome is easy to see."),
        ("E", "Glass-bead sterilizer", "~250 °C, 20 seconds.", "Safer than open flame."),
        ("F", "70% alcohol", "Gloves and bench.", "Does not kill HpLVd."),
    ]
    for i, (n, t, a, b) in enumerate(tools):
        x = 16 + i * 124
        p.append(f'<rect x="{x}" y="40" width="116" height="190" rx="10" fill="{GXL}" stroke="{LINE}"/>')
        p.append(f'<circle cx="{x+58}" cy="{y if False else 68}" r="16" fill="{GD}"/>')
        p.append(f'<text x="{x+58}" y="73" text-anchor="middle" fill="#fff" font-size="14" font-weight="700" style="{MN}">{n}</text>')
        p.append(f'<text x="{x+58}" y="108" text-anchor="middle" fill="{INK}" font-size="11.5" font-weight="700" style="{FS}">{t}</text>')
        p.append(f'<text x="{x+58}" y="140" text-anchor="middle" fill="{INK2}" font-size="11" style="{FS}">{a}</text>')
        p.append(f'<text x="{x+58}" y="156" text-anchor="middle" fill="{INK2}" font-size="11" style="{FS}">{b}</text>')
    p.append('</svg>')
    return "".join(p)


def fig_meristem_hands():
    W, H = 760, 230
    p = [f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="The positions of the hands when you cut a meristem">']
    p.append(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')
    p.append(f'<text x="24" y="26" fill="{INK}" font-size="15" font-weight="700" style="{FS}">Hand positions. Do not change hands.</text>')
    p.append(f'<rect x="24" y="44" width="350" height="168" rx="12" fill="{GL}" stroke="{G}"/>')
    p.append(f'<text x="199" y="74" text-anchor="middle" fill="{GD}" font-size="15" font-weight="700" style="{FS}">Left hand: forceps</text>')
    p.append(f'<text x="199" y="106" text-anchor="middle" fill="{INK2}" font-size="13" style="{FS}">Hold the stem 3–5 mm below the tip.</text>')
    p.append(f'<text x="199" y="128" text-anchor="middle" fill="{INK2}" font-size="13" style="{FS}">Put your wrist on the bench.</text>')
    p.append(f'<text x="199" y="150" text-anchor="middle" fill="{INK2}" font-size="13" style="{FS}">Do not apply force to the dome.</text>')
    p.append(f'<text x="199" y="180" text-anchor="middle" fill="{INK}" font-size="12.5" font-weight="700" style="{FS}">This hand does not cut.</text>')
    p.append(f'<rect x="386" y="44" width="350" height="168" rx="12" fill="{BLUL}" stroke="{BLU}"/>')
    p.append(f'<text x="561" y="74" text-anchor="middle" fill="{BLU}" font-size="15" font-weight="700" style="{FS}">Right hand: #11 scalpel</text>')
    p.append(f'<text x="561" y="106" text-anchor="middle" fill="{INK2}" font-size="13" style="{FS}">Blade almost flat. Move it below a leaf.</text>')
    p.append(f'<text x="561" y="128" text-anchor="middle" fill="{INK2}" font-size="13" style="{FS}">Remove the leaf, away from the dome.</text>')
    p.append(f'<text x="561" y="150" text-anchor="middle" fill="{INK2}" font-size="13" style="{FS}">The last step is one nick down.</text>')
    p.append(f'<text x="561" y="180" text-anchor="middle" fill="{INK}" font-size="12.5" font-weight="700" style="{FS}">Sterilize again after you remove some leaves.</text>')
    p.append('</svg>')
    return "".join(p)


def fig_meristem_sequence():
    W, H = 760, 500
    p = [f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="The eight movements that you use to cut a meristem">']
    p.append(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')
    p.append(f'<text x="24" y="24" fill="{INK}" font-size="15" font-weight="700" style="{FS}">How to cut, one movement at a time</text>')
    steps = [
        ("1", "Cut a 10–15 mm tip", "Vegetative shoot.", "Remove the large leaves."),
        ("2", "Onto the black dish", "One drop sterilized water.", "At the microscope."),
        ("3", "Hold with forceps", "Left hand, 3–5 mm down.", "Point the tip up."),
        ("4", "Remove the outer leaves", "Blade below the leaf.", "Move the leaf away."),
        ("5", "Remove the next pair", "Same movement. Slow.", "Stop at pale tissue."),
        ("6", "Keep two small leaves", "They give the dome", "protection from bleach."),
        ("7", "Cut below the dome", "One nick, 0.2–0.4 mm.", "Cut one time."),
        ("8", "Move to the gel", "Forceps or a needle.", "Make it vertical. Put the lid on."),
    ]
    for i, (n, t, a, b) in enumerate(steps):
        coln = i % 4
        row = i // 4
        x = 16 + coln * 186
        y = 40 + row * 220
        inkc = PUR if i == 6 else (GD if row == 0 else BLU)
        fill = PURL if i == 6 else (GL if row == 0 else BLUL)
        p.append(f'<rect x="{x}" y="{y}" width="176" height="204" rx="10" fill="{fill}" stroke="{inkc}"/>')
        p.append(f'<circle cx="{x+22}" cy="{y+22}" r="14" fill="{inkc}"/>')
        p.append(f'<text x="{x+22}" y="{y+27}" text-anchor="middle" fill="#fff" font-size="13" font-weight="700" style="{MN}">{n}</text>')
        cx, cy = x + 88, y + 86
        if i == 0:
            p.append(f'<line x1="{cx}" y1="{cy+36}" x2="{cx}" y2="{cy-16}" stroke="{G}" stroke-width="6"/>')
            p.append(f'<ellipse cx="{cx}" cy="{cy-24}" rx="16" ry="12" fill="{G}"/>')
        elif i == 1:
            p.append(f'<ellipse cx="{cx}" cy="{cy+8}" rx="46" ry="26" fill="#222"/>')
            p.append(f'<line x1="{cx}" y1="{cy+8}" x2="{cx}" y2="{cy-16}" stroke="{G}" stroke-width="4"/>')
        elif i == 2:
            p.append(f'<line x1="{cx-28}" y1="{cy+18}" x2="{cx}" y2="{cy}" stroke="{INK}" stroke-width="3"/>')
            p.append(f'<line x1="{cx-24}" y1="{cy+24}" x2="{cx}" y2="{cy}" stroke="{INK}" stroke-width="3"/>')
            p.append(f'<line x1="{cx}" y1="{cy}" x2="{cx}" y2="{cy-26}" stroke="{G}" stroke-width="4"/>')
        elif i in (3, 4):
            p.append(f'<line x1="{cx}" y1="{cy+22}" x2="{cx}" y2="{cy-8}" stroke="{G}" stroke-width="4"/>')
            p.append(f'<path d="M{cx},{cy-6} q24,-14 34,-2" fill="none" stroke="{GD}" stroke-width="3"/>')
            p.append(f'<line x1="{cx+8}" y1="{cy+8}" x2="{cx+38}" y2="{cy-16}" stroke="{INK}" stroke-width="2.5"/>')
        elif i == 5:
            p.append(f'<path d="M{cx-14},{cy+4} Q{cx},{cy-24} {cx+14},{cy+4} Z" fill="{G}"/>')
            p.append(f'<path d="M{cx},{cy+4} q-20,8 -24,18" fill="none" stroke="{GL}" stroke-width="3"/>')
            p.append(f'<path d="M{cx},{cy+4} q20,8 24,18" fill="none" stroke="{GL}" stroke-width="3"/>')
        elif i == 6:
            p.append(f'<path d="M{cx-12},{cy} Q{cx},{cy-22} {cx+12},{cy} Z" fill="{G}"/>')
            p.append(f'<line x1="{cx-26}" y1="{cy+8}" x2="{cx+26}" y2="{cy+8}" stroke="{PUR}" stroke-width="2" stroke-dasharray="4 3"/>')
            p.append(f'<text x="{cx}" y="{cy+26}" text-anchor="middle" fill="{PUR}" font-size="10" font-weight="700" style="{FS}">cut here</text>')
        else:
            p.append(f'<rect x="{cx-20}" y="{cy-4}" width="40" height="32" rx="4" fill="{AMBL}" stroke="{AMB}"/>')
            p.append(f'<line x1="{cx}" y1="{cy-4}" x2="{cx}" y2="{cy-24}" stroke="{G}" stroke-width="3"/>')
            p.append(f'<circle cx="{cx}" cy="{cy-26}" r="5" fill="{G}"/>')
        p.append(f'<text x="{x+88}" y="{y+142}" text-anchor="middle" fill="{INK}" font-size="12" font-weight="700" style="{FS}">{t}</text>')
        p.append(f'<text x="{x+88}" y="{y+162}" text-anchor="middle" fill="{INK2}" font-size="11" style="{FS}">{a}</text>')
        p.append(f'<text x="{x+88}" y="{y+178}" text-anchor="middle" fill="{INK2}" font-size="11" style="{FS}">{b}</text>')
    p.append('</svg>')
    return "".join(p)


def fig_meristem_scope():
    W, H = 760, 270
    p = [f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="The meristem in the microscope while you remove the leaves">']
    p.append(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')
    p.append(f'<text x="24" y="22" fill="{INK}" font-size="15" font-weight="700" style="{FS}">The correct sequence at the microscope</text>')
    views = [
        ("A  Start", "Green. Many leaves.", "Too large. Remove more leaves.", True),
        ("B  Outer leaves off", "Some leaves. Tip shows.", "Remove more leaves.", True),
        ("C  Two small leaves stay", "Pale dome shows.", "Stop. Apply bleach.", False),
        ("D  After you cut", "0.2–0.4 mm piece.", "Put it on the gel.", False),
    ]
    for i, (title, a, b, extra) in enumerate(views):
        x = 20 + i * 185
        r = 18 if extra else 9
        p.append(f'<rect x="{x}" y="36" width="175" height="216" rx="10" fill="{GXL}" stroke="{LINE}"/>')
        cx, cy = x + 88, 118
        p.append(f'<circle cx="{cx}" cy="{cy}" r="50" fill="#1a1a1a"/>')
        if extra:
            for sgn in (-1, 1):
                p.append(f'<path d="M{cx},{cy+4} q{sgn*26},{-8} {sgn*32},{8}" fill="{G}" opacity=".9"/>')
                p.append(f'<path d="M{cx},{cy+10} q{sgn*20},{4} {sgn*24},{14}" fill="{GL}" opacity=".85"/>')
        else:
            p.append(f'<path d="M{cx},{cy+6} q-16,8 -18,18" fill="none" stroke="{GL}" stroke-width="3"/>')
            p.append(f'<path d="M{cx},{cy+6} q16,8 18,18" fill="none" stroke="{GL}" stroke-width="3"/>')
        p.append(f'<path d="M{cx-r},{cy+2} Q{cx},{cy-r-2} {cx+r},{cy+2} Z" fill="{G}"/>')
        p.append(f'<text x="{cx}" y="186" text-anchor="middle" fill="{INK}" font-size="12" font-weight="700" style="{FS}">{title}</text>')
        p.append(f'<text x="{cx}" y="206" text-anchor="middle" fill="{INK2}" font-size="11" style="{FS}">{a}</text>')
        p.append(f'<text x="{cx}" y="222" text-anchor="middle" fill="{INK2}" font-size="11" style="{FS}">{b}</text>')
    p.append('</svg>')
    return "".join(p)


def fig_meristem_size():
    W, H = 760, 190
    p = [f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="The small size of a meristem">']
    p.append(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')
    p.append(f'<text x="24" y="24" fill="{INK}" font-size="15" font-weight="700" style="{FS}">How small the piece is</text>')
    items = [
        (70, "Stem piece", "10–15 mm", "For first batches", 32, G),
        (250, "Shoot tip", "approximately 5 mm", "Das Stage I", 18, BLU),
        (420, "Meristem + 2 leaves", "0.2–0.4 mm", "For disease removal", 6, PUR),
        (590, "Rice grain", "approximately 5 mm", "For scale", 16, AMB),
    ]
    for x, t, sz, note, r, col in items:
        p.append(f'<circle cx="{x+50}" cy="78" r="{r}" fill="{col}" opacity=".9"/>')
        p.append(f'<text x="{x+50}" y="128" text-anchor="middle" fill="{INK}" font-size="12.5" font-weight="700" style="{FS}">{t}</text>')
        p.append(f'<text x="{x+50}" y="146" text-anchor="middle" fill="{col}" font-size="12" font-weight="700" style="{MN}">{sz}</text>')
        p.append(f'<text x="{x+50}" y="164" text-anchor="middle" fill="{INK2}" font-size="11" style="{FS}">{note}</text>')
    p.append('</svg>')
    return "".join(p)

