# -*- coding: utf-8 -*-
"""SVG diagrams for the PPPE (Plant & Personal Protective Equipment) paper."""
from figs import (G, GD, GL, GXL, INK, INK2, MUT, LINE, AMB, AMBL, RED, REDL,
                  BLU, BLUL, PUR, PURL, PAPER, PANEL2, FS, MN)
from figs_concepts import _svg, _title, _wrap

SKIN = "#d8a47f"


def human_contamination():
    W, H = 720, 300
    p = []; _title(p, "How much a person contaminates a room", "people are the number-one source, by a wide margin")
    # silhouette
    cx = 150; cy = 170
    p.append(f'<circle cx="{cx}" cy="{cy-55}" r="22" fill="{SKIN}"/>')
    p.append(f'<path d="M{cx-28},{cy+60} Q{cx-30},{cy-25} {cx},{cy-28} Q{cx+30},{cy-25} {cx+28},{cy+60} Z" fill="{INK2}" opacity=".6"/>')
    # particle cloud
    import_pts = [(-60,-70),(60,-80),(-80,-20),(80,-30),(-70,40),(75,30),(-40,90),(50,95),(0,-110),(30,-100)]
    for ox, oy in import_pts:
        p.append(f'<circle cx="{cx+ox}" cy="{cy+oy}" r="2.6" fill="{MUT}" opacity=".7"/>')
    # stats column
    stats = [("~70-90%", "of cleanroom contamination is the people in it", RED),
             ("100k -> 5M", "particles/min: standing still vs moving fast", AMB),
             ("37M + 7M", "bacteria + fungi shed to the air, per person, per hour", AMB),
             ("~10 million", "skin flakes shed per day, ~10% carry live bacteria", AMB)]
    sx = 320
    for i, (big, d, c) in enumerate(stats):
        y = 70 + i * 56
        p.append(f'<text x="{sx}" y="{y}" fill="{c}" font-size="20" font-weight="700" style="{FS}">{big}</text>')
        _wrap(p, sx, y + 18, d, INK2, 52, 11, anchor="start")
    p.append(f'<text x="24" y="{H-12}" fill="{MUT}" font-size="11" style="{FS}">PPE exists because of these numbers: you cannot stop a human shedding, you can only put a barrier around it.</text>')
    return _svg(W, H, "Human contamination", p)


def ppe_by_room():
    W, H = 760, 300
    p = []; _title(p, "PPE escalates by room", "strictest where the genetics live and where product is open")
    zones = [("Vault /\nstore", "gloves, security", REDL, 1),
             ("Trim /\npack", "hairnet, beard net, gloves, smock", AMBL, 3),
             ("Veg /\nflower", "gown, hairnet, gloves, room shoes", GXL, 3),
             ("Dry /\ncure", "cleanroom gown, product exposed", GL, 4),
             ("Mother /\nprop", "full gown, fresh gloves per plant", GL, 5),
             ("TC\nlab", "sterile gloves, lab coat, ISO-5 hood", BLUL, 6)]
    bw = (W - 48) / len(zones); x0 = 24; base = 230
    for i, (t, d, c, lvl) in enumerate(zones):
        x = x0 + i * bw
        h = 24 + lvl * 22
        p.append(f'<rect x="{x+6}" y="{base-h}" width="{bw-12}" height="{h}" rx="5" fill="{c}" opacity=".7" stroke="{LINE}"/>')
        yy = base - h + 16
        for ln in t.split("\n"):
            p.append(f'<text x="{x+bw/2}" y="{yy}" text-anchor="middle" fill="{INK}" font-size="11.5" font-weight="700" style="{FS}">{ln}</text>'); yy += 13
        _wrap(p, x+bw/2, base+16, d, INK2, 17, 8.6)
    p.append(f'<text x="24" y="60" fill="{MUT}" font-size="11" style="{FS}">bar height = PPE intensity</text>')
    p.append(f'<text x="{W-24}" y="{H-8}" text-anchor="end" fill="{MUT}" font-size="10.5" style="{FS}">extraction is different again: worker-safety PPE (FR clothing, goggles, respirator)</text>')
    return _svg(W, H, "PPE by room", p)


def gowning_order():
    W, H = 720, 330
    p = []; _title(p, "Gowning order: top-down, dirtiest off last", "particles fall onto not-yet-covered areas, so cover the top first")
    don = ["Strip: no phone, jewellery, watch, makeup", "Hairnet / bouffant + beard cover",
           "Face mask, then eyewear", "Inner gloves", "Coverall (not touching the floor) + hood",
           "Boot covers, stepping over the line to clean side", "Outer gloves over the cuffs", "Sanitise hands, enter"]
    x = 60; y0 = 64; step = 30
    for i, t in enumerate(don):
        y = y0 + i * step
        p.append(f'<circle cx="{x}" cy="{y}" r="11" fill="{G}"/>')
        p.append(f'<text x="{x}" y="{y+4}" text-anchor="middle" fill="{PAPER}" font-size="11" font-weight="700" style="{MN}">{i+1}</text>')
        p.append(f'<text x="{x+22}" y="{y+4}" fill="{INK}" font-size="12" style="{FS}">{t}</text>')
        if i < len(don) - 1:
            p.append(f'<line x1="{x}" y1="{y+11}" x2="{x}" y2="{y+step-11}" stroke="{LINE}" stroke-width="1.5"/>')
    p.append(f'<text x="24" y="{H-10}" fill="{MUT}" font-size="11" style="{FS}">De-gown in reverse, dirtiest first: outer gloves, boot covers, coverall rolled inside-out, eyewear, hood, mask by the loops, hairnet, inner gloves, then wash.</text>')
    return _svg(W, H, "Gowning order", p)


def handwash():
    W, H = 720, 270
    p = []; _title(p, "Hand hygiene: the technique and the timing", "neither soap nor rub sterilises, so it is a frequent loop, not a one-off gate")
    steps = ["Wet + soap", "Palm to palm", "Between fingers", "Backs of fingers", "Thumbs", "Fingertips + nails"]
    bw = (W - 48) / 6; x0 = 24; y = 110
    for i, t in enumerate(steps):
        x = x0 + i * bw
        p.append(f'<circle cx="{x+bw/2}" cy="{y}" r="22" fill="{BLUL}" opacity=".6" stroke="{LINE}"/>')
        p.append(f'<text x="{x+bw/2}" y="{y+5}" text-anchor="middle" fill="{INK}" font-size="13" font-weight="700" style="{MN}">{i+1}</text>')
        _wrap(p, x+bw/2, y+44, t, INK2, 14, 9.5)
        if i < 5:
            p.append(f'<text x="{x+bw-4}" y="{y+5}" text-anchor="middle" fill="{MUT}" font-size="13">&rarr;</text>')
    p.append(f'<text x="{W/2}" y="200" text-anchor="middle" fill="{INK}" font-size="12.5" font-weight="700" style="{FS}">Soap + water 40-60s (preferred when soiled)  ·  Alcohol rub 20-30s (&ge;60% alcohol)</text>')
    p.append(f'<text x="{W/2}" y="226" text-anchor="middle" fill="{INK2}" font-size="11" style="{FS}">When: on entry, before clean/aseptic work, after waste or contamination, after any absence, on re-entry.</text>')
    p.append(f'<text x="24" y="{H-10}" fill="{MUT}" font-size="11" style="{FS}">Alcohol rub removes ~83% (about 3 log); plain washing ~58% (about 2 log). Both leave survivors, so repeat at every transition.</text>')
    return _svg(W, H, "Hand hygiene", p)


def glove_doff():
    W, H = 700, 252
    p = []; _title(p, "Taking gloves off without touching the dirty side", "glove-to-glove, then skin-to-skin")
    panels = [("1", "Pinch the outside of one cuff", "glove touches glove only"),
              ("2", "Peel it off inside-out, hold it", "in the still-gloved hand"),
              ("3", "Bare fingers inside the other cuff", "peel off over the first, bin, wash")]
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
    p.append(f'<text x="24" y="{H-8}" fill="{MUT}" font-size="11" style="{FS}">Gloves never replace hand hygiene: wash before donning and immediately after removal. Bare skin never touches a glove exterior.</text>')
    return _svg(W, H, "Glove removal", p)


def footwear_barrier():
    W, H = 700, 250
    p = []; _title(p, "Stopping what walks in on shoes", "feet and floors are a top tracking vector for spores and pests")
    line_x = 430
    p.append(f'<line x1="{line_x}" y1="70" x2="{line_x}" y2="200" stroke="{INK}" stroke-width="2" stroke-dasharray="6 4"/>')
    p.append(f'<text x="{line_x}" y="62" text-anchor="middle" fill="{INK}" font-size="11" font-weight="700" style="{FS}">demarcation line</text>')
    p.append(f'<text x="120" y="62" text-anchor="middle" fill="{RED}" font-size="11" font-weight="700" style="{FS}">DIRTY side</text>')
    p.append(f'<text x="580" y="62" text-anchor="middle" fill="{GD}" font-size="11" font-weight="700" style="{FS}">CLEAN side</text>')
    layers = [("Street shoe", 70, REDL), ("Sticky mat\n~99% @ 0.5um", 180, AMBL), ("Footbath\n(quat / H2O2)", 300, AMBL)]
    for t, x, c in layers:
        p.append(f'<rect x="{x}" y="100" width="100" height="60" rx="6" fill="{c}" opacity=".6" stroke="{LINE}"/>')
        yy = 126
        for ln in t.split("\n"):
            p.append(f'<text x="{x+50}" y="{yy}" text-anchor="middle" fill="{INK}" font-size="10.5" font-weight="700" style="{FS}">{ln}</text>'); yy += 13
    p.append(f'<rect x="480" y="100" width="160" height="60" rx="6" fill="{GL}" opacity=".6" stroke="{LINE}"/>')
    p.append(f'<text x="560" y="126" text-anchor="middle" fill="{INK}" font-size="10.5" font-weight="700" style="{FS}">Dedicated room boot</text>')
    p.append(f'<text x="560" y="140" text-anchor="middle" fill="{INK2}" font-size="9.5" style="{FS}">or shoe cover, step over</text>')
    p.append(f'<text x="24" y="{H-8}" fill="{MUT}" font-size="11" style="{FS}">Boot-swap at the line: street shoe off on the dirty side, clean room boot on as you step over. Never carry outside soles onto the clean side.</text>')
    return _svg(W, H, "Footwear barrier", p)


def toilet_protocol():
    W, H = 720, 230
    p = []; _title(p, "The toilet is outside the clean envelope", "a flush plume reaches ~1.5 m in 8 seconds and stays viable for minutes")
    steps = [("De-gown", "before the toilet"), ("Use toilet", "lid down: ~12x less aerosol"),
             ("Wash hands", "soap, 40-60s"), ("Wash + sanitise", "again on return"), ("Re-gown", "fresh garments, re-enter")]
    bw = (W - 48) / 5; x0 = 24; y = 120
    for i, (t, d) in enumerate(steps):
        x = x0 + i * bw
        c = AMBL if i in (0, 1) else GL
        p.append(f'<rect x="{x+6}" y="{y}" width="{bw-12}" height="56" rx="8" fill="{c}" opacity=".6" stroke="{LINE}"/>')
        p.append(f'<text x="{x+bw/2}" y="{y+24}" text-anchor="middle" fill="{INK}" font-size="11.5" font-weight="700" style="{FS}">{t}</text>')
        _wrap(p, x+bw/2, y+40, d, INK2, 18, 9)
        if i < 4:
            p.append(f'<text x="{x+bw-2}" y="{y+30}" text-anchor="middle" fill="{MUT}" font-size="15">&rarr;</text>')
    p.append(f'<text x="24" y="{H-10}" fill="{MUT}" font-size="11" style="{FS}">Toilets must not open into production. Anyone back from the restroom is a bioaerosol bridge until they have washed and re-gowned.</text>')
    return _svg(W, H, "Toilet protocol", p)


def dirty_clean_flow():
    W, H = 700, 250
    p = []; _title(p, "One-way flow: dirty to clean, never back", "people, materials and waste move in one direction only")
    zones = [("Street /\nlockers", REDL), ("Gowning\nairlock", AMBL), ("Clean\nproduction", GL), ("Finished\nout", BLUL)]
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
    p.append(f'<text x="{x0+bw+15}" y="{y-6}" fill="{INK}" font-size="10.5" font-weight="700" style="{FS}">demarcation line: dirty hand never touches clean side</text>')
    p.append(f'<path d="M{x0+2.5*(bw+10)},{y+h+30} l-{1.0*(bw+10):.0f},0" stroke="{RED}" stroke-width="2" stroke-dasharray="5 4"/>')
    p.append(f'<text x="{x0+1.8*(bw+10):.0f}" y="{y+h+26}" text-anchor="middle" fill="{RED}" font-size="10.5" style="{FS}">backtracking = re-gown</text>')
    p.append(f'<text x="24" y="{H-8}" fill="{MUT}" font-size="11" style="{FS}">Positive-pressure, filtered, directional air backs the layout up so dirty air is never pulled toward the canopy.</text>')
    return _svg(W, H, "Dirty to clean flow", p)


def hierarchy_controls():
    W, H = 700, 280
    p = []; _title(p, "PPE is the last line, not the first", "NZ law requires higher controls before you rely on PPE")
    levels = [("Eliminate", "remove the hazard", GL), ("Substitute", "swap for safer", GXL),
              ("Isolate", "separate people from it", GXL), ("Engineer", "guards, airflow, design", AMBL),
              ("Administrative", "SOPs, training, signage", AMBL), ("PPE", "last resort, supplements only", REDL)]
    cx, top, totalh = 350, 56, 200
    n = len(levels)
    for i, (t, d, c) in enumerate(levels):
        y = top + i * (totalh / n)
        w1 = 360 - i * 50; w2 = 360 - (i + 1) * 50
        h = totalh / n - 4
        p.append(f'<path d="M{cx-w1/2:.0f},{y:.0f} L{cx+w1/2:.0f},{y:.0f} L{cx+w2/2:.0f},{y+h:.0f} L{cx-w2/2:.0f},{y+h:.0f} Z" fill="{c}" opacity=".6" stroke="{LINE}"/>')
        p.append(f'<text x="{cx}" y="{y+h/2-1:.0f}" text-anchor="middle" fill="{INK}" font-size="11.5" font-weight="700" style="{FS}">{t}</text>')
        p.append(f'<text x="{cx}" y="{y+h/2+13:.0f}" text-anchor="middle" fill="{INK2}" font-size="9.5" style="{FS}">{d}</text>')
    p.append(f'<text x="40" y="{top+10}" fill="{MUT}" font-size="10.5" style="{FS}">most</text>')
    p.append(f'<text x="40" y="{top+totalh-4}" fill="{MUT}" font-size="10.5" style="{FS}">least</text>')
    p.append(f'<text x="40" y="{top+totalh/2}" fill="{MUT}" font-size="10.5" style="{FS}">effective</text>')
    return _svg(W, H, "Hierarchy of controls", p)
