# -*- coding: utf-8 -*-
"""SVG diagrams for the PPPE (Plant & Personal Protective Equipment) paper."""
from figs import (G, GD, GL, GXL, INK, INK2, MUT, LINE, AMB, AMBL, RED, REDL,
                  BLU, BLUL, PUR, PURL, PAPER, PANEL2, FS, MN)
from figs_concepts import _svg, _title, _wrap

SKIN = "var(--fig-skin)"


def human_contamination():
    W, H = 720, 300
    p = []; _title(p, "The quantity of contamination that a person releases", "Persons are the primary source. All other sources are much smaller.")
    # silhouette
    cx = 150; cy = 170
    p.append(f'<circle cx="{cx}" cy="{cy-55}" r="22" fill="{SKIN}"/>')
    p.append(f'<path d="M{cx-28},{cy+60} Q{cx-30},{cy-25} {cx},{cy-28} Q{cx+30},{cy-25} {cx+28},{cy+60} Z" fill="{INK2}" opacity=".6"/>')
    # particle cloud
    import_pts = [(-60,-70),(60,-80),(-80,-20),(80,-30),(-70,40),(75,30),(-40,90),(50,95),(0,-110),(30,-100)]
    for ox, oy in import_pts:
        p.append(f'<circle cx="{cx+ox}" cy="{cy+oy}" r="2.6" fill="{MUT}" opacity=".7"/>')
    # stats column
    stats = [("~70-90%", "of the contamination in a cleanroom is from persons", RED),
             ("100k -> 5M", "particles each minute: no movement and fast movement", AMB),
             ("37M + 7M", "bacteria and fungi that a person releases into the air each hour", AMB),
             ("approximately 10 million", "skin flakes each day, ~10% with viable bacteria", AMB)]
    sx = 320
    for i, (big, d, c) in enumerate(stats):
        y = 70 + i * 56
        p.append(f'<text x="{sx}" y="{y}" fill="{c}" font-size="20" font-weight="700" style="{FS}">{big}</text>')
        _wrap(p, sx, y + 18, d, INK2, 52, 11, anchor="start")
    p.append(f'<text x="24" y="{H-12}" fill="{MUT}" font-size="11" style="{FS}">A person cannot stop the particles that the person releases. Thus PPE is a barrier around the person.</text>')
    return _svg(W, H, "Human contamination", p)


def ppe_by_room():
    W, H = 760, 300
    p = []; _title(p, "The grade of PPE for each room", "Use the highest grade where the genetics are and where the product is open")
    zones = [("Vault /\nstorage", "gloves, security", REDL, 1),
             ("Trim /\npackaging", "hairnet, beard net, gloves, smock", AMBL, 3),
             ("Vegetative /\nflowering", "gown, hairnet, gloves, room shoes", GXL, 3),
             ("Dry /\ncure", "cleanroom gown, open product", GL, 4),
             ("Mother /\npropagation", "full gown, new gloves each plant", GL, 5),
             ("Tissue-culture\nlab", "sterile gloves, lab coat, ISO-5 hood", BLUL, 6)]
    bw = (W - 48) / len(zones); x0 = 24; base = 230
    for i, (t, d, c, lvl) in enumerate(zones):
        x = x0 + i * bw
        h = 24 + lvl * 22
        p.append(f'<rect x="{x+6}" y="{base-h}" width="{bw-12}" height="{h}" rx="5" fill="{c}" opacity=".7" stroke="{LINE}"/>')
        yy = base - h + 16
        for ln in t.split("\n"):
            p.append(f'<text x="{x+bw/2}" y="{yy}" text-anchor="middle" fill="{INK}" font-size="11.5" font-weight="700" style="{FS}">{ln}</text>'); yy += 13
        _wrap(p, x+bw/2, base+16, d, INK2, 17, 8.6)
    p.append(f'<text x="24" y="60" fill="{MUT}" font-size="11" style="{FS}">bar height = PPE grade</text>')
    p.append(f'<text x="{W-24}" y="{H-8}" text-anchor="end" fill="{MUT}" font-size="10.5" style="{FS}">Extraction is different: PPE gives protection to the worker (FR clothing, goggles, respirator)</text>')
    return _svg(W, H, "PPE by room", p)


def gowning_order():
    W, H = 720, 330
    p = []; _title(p, "Gowning sequence: from the top to the bottom, the dirtiest items last", "Particles fall on parts of the body with no clothing. Put on the clothing for the top first.")
    don = ["Remove the phone, jewelry, watch and makeup", "Hairnet or bouffant and beard cover",
           "Face mask, then eyewear", "Inner gloves", "Coverall and hood. Keep the coverall off the floor.",
           "Boot covers, when you go across the demarcation line", "Outer gloves on the cuffs of the coverall", "Sanitize your hands and go in"]
    x = 60; y0 = 64; step = 30
    for i, t in enumerate(don):
        y = y0 + i * step
        p.append(f'<circle cx="{x}" cy="{y}" r="11" fill="{G}"/>')
        p.append(f'<text x="{x}" y="{y+4}" text-anchor="middle" fill="{PAPER}" font-size="11" font-weight="700" style="{MN}">{i+1}</text>')
        p.append(f'<text x="{x+22}" y="{y+4}" fill="{INK}" font-size="12" style="{FS}">{t}</text>')
        if i < len(don) - 1:
            p.append(f'<line x1="{x}" y1="{y+11}" x2="{x}" y2="{y+step-11}" stroke="{LINE}" stroke-width="1.5"/>')
    p.append(f'<text x="24" y="{H-10}" fill="{MUT}" font-size="11" style="{FS}">De-gowning, dirtiest first: outer gloves, boot covers, coverall (inside-out), eyewear, hood, mask (loops only), hairnet, inner gloves. Then wash.</text>')
    return _svg(W, H, "Gowning order", p)


def handwash():
    W, H = 720, 270
    p = []; _title(p, "Hand hygiene: the method and the times", "Soap and alcohol rub do not sterilize the hands. Thus you do hand hygiene frequently and not one time.")
    steps = ["Water and soap", "Palm to palm", "Between the fingers", "Back of the hand", "Thumbs", "Fingertips and nails"]
    bw = (W - 48) / 6; x0 = 24; y = 110
    for i, t in enumerate(steps):
        x = x0 + i * bw
        p.append(f'<circle cx="{x+bw/2}" cy="{y}" r="22" fill="{BLUL}" opacity=".6" stroke="{LINE}"/>')
        p.append(f'<text x="{x+bw/2}" y="{y+5}" text-anchor="middle" fill="{INK}" font-size="13" font-weight="700" style="{MN}">{i+1}</text>')
        _wrap(p, x+bw/2, y+44, t, INK2, 14, 9.5)
        if i < 5:
            p.append(f'<text x="{x+bw-4}" y="{y+5}" text-anchor="middle" fill="{MUT}" font-size="13">&rarr;</text>')
    p.append(f'<text x="{W/2}" y="200" text-anchor="middle" fill="{INK}" font-size="12.5" font-weight="700" style="{FS}">Soap and water 40 to 60 seconds (for dirty hands)  ·  Alcohol rub 20 to 30 seconds (minimum 60% alcohol)</text>')
    p.append(f'<text x="{W/2}" y="226" text-anchor="middle" fill="{INK2}" font-size="11" style="{FS}">When: at entry, before clean work or aseptic work, after waste or contamination, after you are away from the area, when you go in again.</text>')
    p.append(f'<text x="24" y="{H-10}" fill="{MUT}" font-size="11" style="{FS}">Approximately: an alcohol rub removes 83% (3 log) and a hand wash 58% (2 log). Some organisms stay: do it at each change of area.</text>')
    return _svg(W, H, "Hand hygiene", p)


def glove_doff():
    W, H = 700, 252
    p = []; _title(p, "Remove the gloves and do not touch the dirty side", "First, a glove touches a glove. Then, skin touches skin.")
    panels = [("1", "Hold the outer surface of one cuff", "glove touches glove only"),
              ("2", "Remove it inside-out, hold it", "in the hand with a glove"),
              ("3", "Put bare fingers in the other cuff", "remove it with the first glove in it, then wash")]
    bw = (W - 48) / 3; x0 = 24; cy = 130
    for i, (n, t, d) in enumerate(panels):
        x = x0 + i * bw
        p.append(f'<circle cx="{x+bw/2}" cy="{cy-30}" r="14" fill="{AMB}"/>')
        p.append(f'<text x="{x+bw/2}" y="{cy-26}" text-anchor="middle" fill="{PAPER}" font-size="13" font-weight="700" style="{MN}">{n}</text>')
        # mini hand glyph
        p.append(f'<rect x="{x+bw/2-22}" y="{cy-4}" width="44" height="30" rx="6" fill="{GXL}" stroke="{LINE}"/>')
        _wrap(p, x+bw/2, cy+46, t, INK, 20, 10.5)
        _wrap(p, x+bw/2, cy+80, d, MUT, 24, 9.5)
        if i < 2:
            p.append(f'<text x="{x+bw-2}" y="{cy}" text-anchor="middle" fill="{MUT}" font-size="16">&rarr;</text>')
    p.append(f'<text x="24" y="{H-8}" fill="{MUT}" font-size="11" style="{FS}">Gloves do not replace hand hygiene: wash before and immediately after you use them. Bare skin does not touch the outer surface.</text>')
    return _svg(W, H, "Glove removal", p)


def footwear_barrier():
    W, H = 700, 250
    p = []; _title(p, "Stop the contamination that comes in on shoes", "Shoes and floors are a primary source of spores and pests")
    line_x = 430
    p.append(f'<line x1="{line_x}" y1="70" x2="{line_x}" y2="200" stroke="{INK}" stroke-width="2" stroke-dasharray="6 4"/>')
    p.append(f'<text x="{line_x}" y="62" text-anchor="middle" fill="{INK}" font-size="11" font-weight="700" style="{FS}">demarcation line</text>')
    p.append(f'<text x="120" y="62" text-anchor="middle" fill="{RED}" font-size="11" font-weight="700" style="{FS}">DIRTY side</text>')
    p.append(f'<text x="580" y="62" text-anchor="middle" fill="{GD}" font-size="11" font-weight="700" style="{FS}">CLEAN side</text>')
    layers = [("Dirty shoe", 70, REDL), ("Sticky mat\n~99% at 0.5 µm", 180, AMBL), ("Footbath\n(quat or H2O2)", 300, AMBL)]
    for t, x, c in layers:
        p.append(f'<rect x="{x}" y="100" width="100" height="60" rx="6" fill="{c}" opacity=".6" stroke="{LINE}"/>')
        yy = 126
        for ln in t.split("\n"):
            p.append(f'<text x="{x+50}" y="{yy}" text-anchor="middle" fill="{INK}" font-size="10.5" font-weight="700" style="{FS}">{ln}</text>'); yy += 13
    p.append(f'<rect x="480" y="100" width="160" height="60" rx="6" fill="{GL}" opacity=".6" stroke="{LINE}"/>')
    p.append(f'<text x="560" y="126" text-anchor="middle" fill="{INK}" font-size="10.5" font-weight="700" style="{FS}">Boot for this room only</text>')
    p.append(f'<text x="560" y="140" text-anchor="middle" fill="{INK2}" font-size="9.5" style="{FS}">or shoe cover, go across</text>')
    p.append(f'<text x="24" y="{H-8}" fill="{MUT}" font-size="11" style="{FS}">Remove the shoes on the dirty side. Put on the room boots at the demarcation line. Do not move soles to the clean side.</text>')
    return _svg(W, H, "Footwear barrier", p)


def toilet_protocol():
    W, H = 720, 230
    p = []; _title(p, "The toilet is not in the clean area", "The plume of a flush goes to a height of approximately 1.5 m in 8 seconds and stays viable for minutes")
    steps = [("De-gowning", "before the toilet"), ("Use the toilet", "lid down: ~12 times less aerosol"),
             ("Wash your hands", "soap, 40 to 60 s"), ("Wash and sanitize", "when you come back"), ("Gowning again", "clean clothing, go in again")]
    bw = (W - 48) / 5; x0 = 24; y = 120
    for i, (t, d) in enumerate(steps):
        x = x0 + i * bw
        c = AMBL if i in (0, 1) else GL
        p.append(f'<rect x="{x+6}" y="{y}" width="{bw-12}" height="56" rx="8" fill="{c}" opacity=".6" stroke="{LINE}"/>')
        p.append(f'<text x="{x+bw/2}" y="{y+24}" text-anchor="middle" fill="{INK}" font-size="11.5" font-weight="700" style="{FS}">{t}</text>')
        _wrap(p, x+bw/2, y+40, d, INK2, 18, 9)
        if i < 4:
            p.append(f'<text x="{x+bw-2}" y="{y+30}" text-anchor="middle" fill="{MUT}" font-size="15">&rarr;</text>')
    p.append(f'<text x="24" y="{H-10}" fill="{MUT}" font-size="11" style="{FS}">A toilet must not open into production. A person from the toilet can move bioaerosol until the person washes and does the gowning again.</text>')
    return _svg(W, H, "Toilet protocol", p)


def dirty_clean_flow():
    W, H = 700, 250
    p = []; _title(p, "Flow in one direction: from dirty to clean, not back", "Persons, materials and waste move in one direction only")
    zones = [("Dirty area /\nlockers", REDL), ("Gowning\nairlock", AMBL), ("Clean\nproduction", GL), ("Product\nexit", BLUL)]
    bw = 150; x0 = 30; y = 90; h = 80
    for i, (t, c) in enumerate(zones):
        x = x0 + i * (bw + 10)
        p.append(f'<rect x="{x}" y="{y}" width="{bw}" height="{h}" rx="6" fill="{c}" opacity=".55" stroke="{LINE}"/>')
        yy = y + 34
        for ln in t.split("\n"):
            p.append(f'<text x="{x+bw/2}" y="{yy}" text-anchor="middle" fill="{INK}" font-size="12" font-weight="700" style="{FS}">{ln}</text>'); yy += 15
        if i < 3:
            ax = x + bw; p.append(f'<path d="M{ax},{y+h/2} l10,0" stroke="{GD}" stroke-width="3"/>')
            p.append(f'<path d="M{ax+10},{y+h/2} l-6,-4 M{ax+10},{y+h/2} l-6,4" stroke="{GD}" stroke-width="3" fill="none"/>')
    p.append(f'<text x="{x0+bw+15}" y="{y-6}" fill="{INK}" font-size="10.5" font-weight="700" style="{FS}">demarcation line: a dirty hand does not touch the clean side</text>')
    p.append(f'<path d="M{x0+2.5*(bw+10)},{y+h+30} l-{1.0*(bw+10):.0f},0" stroke="{RED}" stroke-width="2" stroke-dasharray="5 4"/>')
    p.append(f'<text x="{x0+1.8*(bw+10):.0f}" y="{y+h+26}" text-anchor="middle" fill="{RED}" font-size="10.5" style="{FS}">go back: do the gowning procedure again</text>')
    p.append(f'<text x="24" y="{H-8}" fill="{MUT}" font-size="11" style="{FS}">Filtered air with higher pressure in the clean area flows to the dirty area. Thus dirty air does not go to the canopy.</text>')
    return _svg(W, H, "Dirty to clean flow", p)


def hierarchy_controls():
    W, H = 700, 280
    p = []; _title(p, "PPE is the last control, not the first", "The NZ regulations tell you to apply the higher controls before you use PPE")
    levels = [("Elimination", "remove the hazard", GL), ("Substitution", "use a safer item", GXL),
              ("Isolation", "keep persons away from it", GXL), ("Engineering controls", "barriers, airflow, rooms", AMBL),
              ("Administrative controls", "SOPs, training, signs", AMBL), ("PPE", "last control, with the other controls", REDL)]
    cx, top, totalh = 350, 56, 200
    n = len(levels)
    for i, (t, d, c) in enumerate(levels):
        y = top + i * (totalh / n)
        w1 = 360 - i * 50; w2 = 360 - (i + 1) * 50
        h = totalh / n - 4
        p.append(f'<path d="M{cx-w1/2:.0f},{y:.0f} L{cx+w1/2:.0f},{y:.0f} L{cx+w2/2:.0f},{y+h:.0f} L{cx-w2/2:.0f},{y+h:.0f} Z" fill="{c}" opacity=".6" stroke="{LINE}"/>')
        p.append(f'<text x="{cx}" y="{y+h/2-1:.0f}" text-anchor="middle" fill="{INK}" font-size="11.5" font-weight="700" style="{FS}">{t}</text>')
        p.append(f'<text x="{cx}" y="{y+h/2+13:.0f}" text-anchor="middle" fill="{INK2}" font-size="9.5" style="{FS}">{d}</text>')
    p.append(f'<text x="40" y="{top+10}" fill="{MUT}" font-size="10.5" style="{FS}">high</text>')
    p.append(f'<text x="40" y="{top+totalh-4}" fill="{MUT}" font-size="10.5" style="{FS}">low</text>')
    p.append(f'<text x="40" y="{top+totalh/2}" fill="{MUT}" font-size="10.5" style="{FS}">protection</text>')
    return _svg(W, H, "Hierarchy of controls", p)
