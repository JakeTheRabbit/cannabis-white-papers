# -*- coding: utf-8 -*-
"""Paper-specific bespoke SVG diagrams."""
from figs import (G, GD, GL, GXL, INK, INK2, MUT, LINE, AMB, AMBL, RED, REDL,
                  BLU, BLUL, PUR, PURL, PAPER, PANEL2, FS, MN)
from figs_concepts import _svg, _title, _wrap, WATER, WATERL, DRY, DRYL, SALT, SOLID

GREEN = G; DGREEN = GD


# ---------------------------------------------------------------- seeds
def germination():
    W, H = 760, 250
    p = []; _title(p, "From seed to seedling", "what happens, in order, after the seed takes on water")
    soil = 175
    p.append(f'<rect x="20" y="{soil}" width="{W-40}" height="6" fill="{DRY}" opacity=".5"/>')
    stages = [
        ("Dry seed", "viable, dormant"),
        ("Imbibition", "soaks up water, coat splits"),
        ("Radicle", "taproot emerges, roots down"),
        ("Cotyledons", "shoot hooks up, seed leaves open"),
        ("True leaves", "first real serrated leaves"),
    ]
    bw = (W - 40) / 5
    for i, (t, d) in enumerate(stages):
        cx = 20 + bw * i + bw / 2
        if i == 0:
            p.append(f'<ellipse cx="{cx}" cy="{soil-22}" rx="15" ry="20" fill="{DRY}" stroke="{INK2}"/>')
        elif i == 1:
            p.append(f'<ellipse cx="{cx}" cy="{soil-22}" rx="16" ry="21" fill="{DRYL}" stroke="{INK2}"/>')
            p.append(f'<line x1="{cx-10}" y1="{soil-34}" x2="{cx+8}" y2="{soil-10}" stroke="{INK2}" stroke-width="1.5"/>')
        elif i == 2:
            p.append(f'<ellipse cx="{cx}" cy="{soil-22}" rx="14" ry="18" fill="{DRYL}" stroke="{INK2}"/>')
            p.append(f'<path d="M{cx},{soil} q-4,18 -2,40" fill="none" stroke="{DGREEN}" stroke-width="2.2"/>')
        elif i == 3:
            p.append(f'<path d="M{cx},{soil} q-3,18 -1,38" fill="none" stroke="{DGREEN}" stroke-width="2.2"/>')
            p.append(f'<path d="M{cx},{soil-40} q-2,-26 0,-40" fill="none" stroke="{DGREEN}" stroke-width="2.4"/>')
            for sgn in (-1, 1):
                p.append(f'<ellipse cx="{cx+sgn*12}" cy="{soil-80}" rx="13" ry="6" fill="{GL}" stroke="{DGREEN}" transform="rotate({sgn*20} {cx+sgn*12} {soil-80})"/>')
        else:
            p.append(f'<path d="M{cx},{soil} q-3,18 -1,38" fill="none" stroke="{DGREEN}" stroke-width="2.2"/>')
            p.append(f'<line x1="{cx}" y1="{soil}" x2="{cx}" y2="{soil-95}" stroke="{DGREEN}" stroke-width="2.6"/>')
            for sgn in (-1, 1):
                p.append(f'<ellipse cx="{cx+sgn*11}" cy="{soil-70}" rx="11" ry="5" fill="{GL}" stroke="{DGREEN}" transform="rotate({sgn*22} {cx+sgn*11} {soil-70})"/>')
                p.append(f'<path d="M{cx},{soil-95} q{sgn*22},-4 {sgn*30},10 q{sgn*-6},6 {sgn*-30},-2 z" fill="{G}" stroke="{DGREEN}"/>')
        # taproot below soil for stages 2+
        if i >= 2:
            p.append(f'<path d="M{cx},{soil+2} q2,16 0,30 M{cx},{soil+10} q-8,6 -12,16 M{cx},{soil+10} q8,8 12,18" fill="none" stroke="{DRY}" stroke-width="1.5"/>')
        p.append(f'<text x="{cx}" y="{soil+58}" text-anchor="middle" fill="{DGREEN}" font-size="11.5" font-weight="700" style="{FS}">{i+1}. {t}</text>')
        _wrap(p, cx, soil+74, d, INK2, 20, 9.5)
        if i < 4:
            p.append(f'<text x="{20+bw*(i+1):.0f}" y="{soil-20}" text-anchor="middle" fill="{MUT}" font-size="16">&rarr;</text>')
    return _svg(W, H, "Germination progression", p)


def seed_anatomy():
    W, H = 640, 300
    p = []; _title(p, "Inside a cannabis seed", "the parts that become the plant")
    cx, cy = 230, 165
    p.append(f'<ellipse cx="{cx}" cy="{cy}" rx="120" ry="90" fill="{DRYL}" stroke="{INK2}" stroke-width="2"/>')
    p.append(f'<ellipse cx="{cx}" cy="{cy}" rx="108" ry="78" fill="none" stroke="{DRY}" stroke-width="1.4" stroke-dasharray="3 3"/>')
    # embryo: radicle + two cotyledons curled
    p.append(f'<path d="M{cx-10},{cy+55} Q{cx-30},{cy} {cx-10},{cy-40}" fill="none" stroke="{DGREEN}" stroke-width="4"/>')
    for sgn in (-1, 1):
        p.append(f'<ellipse cx="{cx+sgn*30}" cy="{cy-30}" rx="34" ry="20" fill="{GL}" stroke="{DGREEN}" transform="rotate({sgn*30} {cx+sgn*30} {cy-30})"/>')
    p.append(f'<circle cx="{cx-12}" cy="{cy+55}" r="6" fill="{DGREEN}"/>')
    # labels
    def lab(x, y, tx, ty, t, c=INK):
        p.append(f'<line x1="{x}" y1="{y}" x2="{tx}" y2="{ty}" stroke="{MUT}" stroke-width="1"/>')
        p.append(f'<circle cx="{x}" cy="{y}" r="2.5" fill="{c}"/>')
        anc = "start" if tx > x else "end"
        p.append(f'<text x="{tx + (6 if tx>x else -6)}" y="{ty+4}" text-anchor="{anc}" fill="{INK}" font-size="11" font-weight="700" style="{FS}">{t}</text>')
    lab(cx+115, cy-40, W-20, 70, "Seed coat (testa)")
    lab(cx+105, cy-12, W-20, 110, "Endosperm")
    lab(cx+30, cy-40, W-20, 150, "Cotyledons (seed leaves)")
    lab(cx-22, cy+10, W-20, 200, "Embryo")
    lab(cx-12, cy+55, W-20, 240, "Radicle (becomes taproot)")
    p.append(f'<text x="24" y="{H-10}" fill="{MUT}" font-size="11" style="{FS}">The coat protects; the endosperm feeds; the embryo is the plant in miniature, radicle down, cotyledons up.</text>')
    return _svg(W, H, "Seed anatomy", p)


# ---------------------------------------------------------------- defoliation / training
def apical_dominance():
    W, H = 700, 290
    p = []; _title(p, "Apical dominance, and how topping releases it", "the tip hormone suppresses the buds below it")
    for i, (t, topped) in enumerate([("Intact: one dominant tip", False), ("Topped: two tips take over", True)]):
        cx = 200 + i * 320; base = 250; topy = 95
        p.append(f'<line x1="{cx}" y1="{base}" x2="{cx}" y2="{topy if not topped else topy+30}" stroke="{DGREEN}" stroke-width="4"/>')
        if not topped:
            p.append(f'<circle cx="{cx}" cy="{topy}" r="10" fill="{GD}"/>')
            p.append(f'<path d="M{cx},{topy+6} l0,80" stroke="{AMB}" stroke-width="2" stroke-dasharray="4 3" marker-end=""/>')
            p.append(f'<text x="{cx+8}" y="{topy+50}" fill="{AMB}" font-size="10" style="{FS}">auxin &darr;</text>')
            for ly in (150, 195):
                for sgn in (-1, 1):
                    p.append(f'<circle cx="{cx+sgn*18}" cy="{ly}" r="5" fill="{MUT}"/>')
            _wrap(p, cx, base+22, "side buds suppressed, plant grows tall and single", INK2, 30)
        else:
            p.append(f'<line x1="{cx}" y1="{topy+30}" x2="{cx-12}" y2="{topy+34}" stroke="{RED}" stroke-width="2" stroke-dasharray="3 2"/>')
            for sgn in (-1, 1):
                p.append(f'<path d="M{cx},{topy+30} q{sgn*30},-10 {sgn*36},-34" fill="none" stroke="{DGREEN}" stroke-width="3.5"/>')
                p.append(f'<circle cx="{cx+sgn*36}" cy="{topy-6}" r="9" fill="{GD}"/>')
            _wrap(p, cx, base+22, "cut breaks the hormone, two colas form", INK2, 30)
        p.append(f'<text x="{cx}" y="80" text-anchor="middle" fill="{DGREEN}" font-size="12.5" font-weight="700" style="{FS}">{t}</text>')
    return _svg(W, H, "Apical dominance", p)


def fim_vs_topping():
    W, H = 700, 280
    p = []; _title(p, "Topping vs FIM: where you cut", "the cut line decides how many new tops you get")
    for i, (t, frac, n, d) in enumerate([("Topping", 1.0, "2 tops", "clean cut below the newest node"),
                                          ("FIM", 0.2, "3-4 tops", "pinch ~80% of the tip, leave the base ragged")]):
        cx = 200 + i * 320; tipy = 90
        p.append(f'<line x1="{cx}" y1="220" x2="{cx}" y2="{tipy}" stroke="{DGREEN}" stroke-width="4"/>')
        for sgn in (-1, 1):
            p.append(f'<ellipse cx="{cx+sgn*22}" cy="160" rx="20" ry="8" fill="{GL}" stroke="{DGREEN}" transform="rotate({sgn*18} {cx+sgn*22} 160)"/>')
        # tip cluster
        p.append(f'<circle cx="{cx}" cy="{tipy}" r="14" fill="{GL}" stroke="{DGREEN}"/>')
        cuty = tipy + (0 if i == 0 else -6)
        p.append(f'<line x1="{cx-30}" y1="{cuty}" x2="{cx+30}" y2="{cuty}" stroke="{RED}" stroke-width="2.5" stroke-dasharray="6 3"/>')
        p.append(f'<text x="{cx+34}" y="{cuty+4}" fill="{RED}" font-size="10" font-weight="700" style="{FS}">cut</text>')
        p.append(f'<text x="{cx}" y="76" text-anchor="middle" fill="{DGREEN}" font-size="12.5" font-weight="700" style="{FS}">{t} &rarr; {n}</text>')
        _wrap(p, cx, 244, d, INK2, 30)
    return _svg(W, H, "FIM vs topping", p)


def lollipop_zones():
    W, H = 660, 290
    p = []; _title(p, "Lollipopping: keep the top, strip the bottom", "light and air reach the buds that pay")
    cx, base, top = 300, 250, 80
    p.append(f'<line x1="{cx}" y1="{base}" x2="{cx}" y2="{top}" stroke="{DGREEN}" stroke-width="4"/>')
    # keep zone (top third) green
    p.append(f'<rect x="{cx-150}" y="{top-10}" width="300" height="80" fill="{GL}" opacity=".4"/>')
    p.append(f'<rect x="{cx-150}" y="{base-70}" width="300" height="70" fill="{REDL}" opacity=".4"/>')
    for ly, keep in [(105, True), (135, True), (170, True), (205, False), (235, False)]:
        for sgn in (-1, 1):
            col = G if keep else MUT
            p.append(f'<ellipse cx="{cx+sgn*36}" cy="{ly}" rx="30" ry="11" fill="{col}" opacity="{0.85 if keep else 0.5}" transform="rotate({sgn*16} {cx+sgn*36} {ly})"/>')
            if not keep:
                p.append(f'<line x1="{cx+sgn*20}" y1="{ly-8}" x2="{cx+sgn*52}" y2="{ly+8}" stroke="{RED}" stroke-width="1.6"/>')
    p.append(f'<text x="{cx+165}" y="{top+30}" fill="{DGREEN}" font-size="11.5" font-weight="700" style="{FS}">KEEP</text>')
    p.append(f'<text x="{cx+165}" y="{base-30}" fill="{RED}" font-size="11.5" font-weight="700" style="{FS}">REMOVE</text>')
    p.append(f'<text x="{cx-200}" y="{base-30}" fill="{MUT}" font-size="10" style="{FS}">larf &amp; shade</text>')
    p.append(f'<text x="24" y="{H-10}" fill="{MUT}" font-size="11" style="{FS}">Remove the lower third (small ‘larf’ buds and shade leaves) so energy, light and airflow go to the productive canopy.</text>')
    return _svg(W, H, "Lollipopping zones", p)


def training_compare():
    W, H = 720, 250
    p = []; _title(p, "Training methods and the canopy they make", "more, even tops = more light = more yield")
    plants = [("Untrained", 1, "tall"), ("Topped", 2, "bushy"), ("LST", 4, "spread"), ("SCROG", 8, "flat even")]
    bw = W / 4
    for i, (t, tops, shape) in enumerate(plants):
        cx = bw * i + bw / 2; base = 190; top = 110
        if shape == "tall":
            p.append(f'<line x1="{cx}" y1="{base}" x2="{cx}" y2="{top-20}" stroke="{DGREEN}" stroke-width="3"/>')
            p.append(f'<circle cx="{cx}" cy="{top-20}" r="9" fill="{GD}"/>')
        else:
            spread = {"bushy": 30, "spread": 55, "flat even": 75}[shape]
            for k in range(tops):
                ox = -spread + (2 * spread) * (k / max(1, tops - 1))
                p.append(f'<line x1="{cx}" y1="{base}" x2="{cx+ox:.0f}" y2="{top}" stroke="{DGREEN}" stroke-width="2.4"/>')
                p.append(f'<circle cx="{cx+ox:.0f}" cy="{top}" r="7" fill="{GD}"/>')
            if shape == "flat even":
                p.append(f'<line x1="{cx-80}" y1="{top+12}" x2="{cx+80}" y2="{top+12}" stroke="{MUT}" stroke-width="1" stroke-dasharray="2 2"/>')
        p.append(f'<text x="{cx}" y="{base+24}" text-anchor="middle" fill="{DGREEN}" font-size="12" font-weight="700" style="{FS}">{t}</text>')
        p.append(f'<text x="{cx}" y="{base+40}" text-anchor="middle" fill="{INK2}" font-size="10" style="{FS}">{tops} main cola{"s" if tops>1 else ""}</text>')
    return _svg(W, H, "Training comparison", p)


def bud_anatomy():
    W, H = 640, 300
    p = []; _title(p, "Parts of a flower (bud)", "what you are actually looking at")
    cx, cy = 220, 175
    # cola shape
    p.append(f'<path d="M{cx},80 C{cx-70},120 {cx-60},230 {cx},255 C{cx+60},230 {cx+70},120 {cx},80 Z" fill="{GL}" stroke="{DGREEN}" stroke-width="2"/>')
    # calyxes
    for (ox, oy) in [(-25, 130), (20, 150), (-15, 185), (25, 200), (0, 220)]:
        p.append(f'<ellipse cx="{cx+ox}" cy="{cy+oy-175}" rx="16" ry="12" fill="{G}" opacity=".8"/>')
    # pistils
    for (ox, oy) in [(-30, 120), (25, 140), (-10, 180), (30, 195)]:
        p.append(f'<path d="M{cx+ox},{cy+oy-175} q-6,-12 -14,-16 M{cx+ox},{cy+oy-175} q6,-12 14,-16" fill="none" stroke="{AMB}" stroke-width="2"/>')
    # trichome dots
    for (ox, oy) in [(-40, 110), (35, 125), (-20, 160), (40, 175), (-35, 200), (10, 230)]:
        p.append(f'<circle cx="{cx+ox}" cy="{cy+oy-175}" r="2.4" fill="{PUR}"/>')
    def lab(x, y, tx, ty, t):
        p.append(f'<line x1="{x}" y1="{y}" x2="{tx}" y2="{ty}" stroke="{MUT}" stroke-width="1"/>')
        p.append(f'<text x="{tx+6}" y="{ty+4}" fill="{INK}" font-size="11" font-weight="700" style="{FS}">{t}</text>')
    lab(cx, 85, W-200, 80, "Cola (flower cluster)")
    lab(cx-5, 150, W-200, 130, "Calyx (the bud core)")
    lab(cx+30, 140, W-200, 180, "Pistils (the hairs)")
    lab(cx+40, 175, W-200, 230, "Trichomes (resin)")
    p.append(f'<text x="24" y="{H-10}" fill="{MUT}" font-size="11" style="{FS}">Pistils change colour with maturity; trichomes (not pistils) are the reliable ripeness signal.</text>')
    return _svg(W, H, "Bud anatomy", p)


# ---------------------------------------------------------------- airflow
def boundary_layer():
    W, H = 700, 250
    p = []; _title(p, "The boundary layer: still air on the leaf", "the film that slows water and CO2 exchange")
    lx, ly, lw = 120, 150, 460
    p.append(f'<rect x="{lx}" y="{ly}" width="{lw}" height="16" rx="8" fill="{G}" stroke="{DGREEN}"/>')
    p.append(f'<rect x="{lx}" y="{ly-20}" width="{lw}" height="20" fill="{BLUL}" opacity=".5"/>')
    p.append(f'<text x="{lx+lw/2}" y="{ly-6}" text-anchor="middle" fill="{BLU}" font-size="10.5" style="{FS}">still boundary-layer air</text>')
    for k, (yy, lab, thick) in enumerate([(ly-60, "moving room air", 3)]):
        for xx in range(lx+20, lx+lw-10, 70):
            p.append(f'<path d="M{xx},{yy} l40,0" stroke="{INK2}" stroke-width="{thick}" marker-end=""/>')
            p.append(f'<path d="M{xx+40},{yy} l-7,-4 M{xx+40},{yy} l-7,4" stroke="{INK2}" stroke-width="{thick}" fill="none"/>')
    p.append(f'<text x="{lx}" y="{ly-70}" fill="{INK2}" font-size="10.5" style="{FS}">moving room air</text>')
    p.append(f'<text x="{lx+lw/2}" y="{ly+34}" text-anchor="middle" fill="{DGREEN}" font-size="10.5" style="{FS}">leaf surface</text>')
    p.append(f'<text x="24" y="{H-12}" fill="{MUT}" font-size="11" style="{FS}">Good airflow thins this film so the leaf can transpire and take up CO2. Dead-still air thickens it and the leaf stalls, the airflow goal is to keep it thin, not to blast the plants.</text>')
    return _svg(W, H, "Boundary layer", p)


def transpiration():
    W, H = 640, 300
    p = []; _title(p, "The transpiration stream", "VPD pulls water up from root to leaf")
    cx = 250
    p.append(f'<line x1="{cx}" y1="80" x2="{cx}" y2="230" stroke="{DGREEN}" stroke-width="5"/>')
    p.append(f'<ellipse cx="{cx-50}" cy="100" rx="40" ry="16" fill="{G}" opacity=".85" transform="rotate(-15 {cx-50} 100)"/>')
    p.append(f'<ellipse cx="{cx+50}" cy="110" rx="40" ry="16" fill="{G}" opacity=".85" transform="rotate(15 {cx+50} 110)"/>')
    p.append(f'<path d="M{cx},230 q-20,16 -30,40 M{cx},230 q20,16 30,40 M{cx},230 q0,20 0,42" fill="none" stroke="{DRY}" stroke-width="2"/>')
    # water arrows up
    for yy in (210, 175, 140):
        p.append(f'<path d="M{cx},{yy} l0,-22" stroke="{WATER}" stroke-width="3"/>')
        p.append(f'<path d="M{cx},{yy-22} l-4,7 M{cx},{yy-22} l4,7" stroke="{WATER}" stroke-width="3" fill="none"/>')
    # vapour out of leaf
    for ox in (-60, 60):
        p.append(f'<path d="M{cx+ox},95 q{ox/6},-20 {ox/4},-30" fill="none" stroke="{BLU}" stroke-width="2" stroke-dasharray="3 3"/>')
    p.append(f'<text x="{cx-150}" y="100" fill="{WATER}" font-size="11" font-weight="700" style="{FS}">uptake</text>')
    p.append(f'<text x="{cx+90}" y="60" fill="{BLU}" font-size="11" font-weight="700" style="{FS}">vapour out (VPD pull)</text>')
    p.append(f'<text x="{cx-60}" y="285" fill="{DRY}" font-size="11" font-weight="700" style="{FS}">roots draw water + nutrients</text>')
    return _svg(W, H, "Transpiration stream", p)


def laminar_turbulent():
    W, H = 700, 240
    p = []; _title(p, "Laminar vs turbulent airflow", "you want gentle turbulence in the canopy")
    for i, (t, turb, d) in enumerate([("Laminar (smooth)", False, "slides over the top, leaves a still pocket below"),
                                      ("Turbulent (mixed)", True, "stirs air into the canopy, thins the boundary layer")]):
        x0 = 60 + i * 340; cy = 120
        p.append(f'<rect x="{x0}" y="{cy+20}" width="240" height="14" rx="7" fill="{G}" stroke="{DGREEN}"/>')
        if not turb:
            for yy in (cy-30, cy-10, cy+5):
                p.append(f'<path d="M{x0},{yy} q120,0 240,0" fill="none" stroke="{INK2}" stroke-width="2"/>')
        else:
            for sx in range(x0+10, x0+230, 40):
                p.append(f'<path d="M{sx},{cy-20} q10,-14 20,0 q10,14 20,0" fill="none" stroke="{INK2}" stroke-width="2"/>')
                p.append(f'<path d="M{sx},{cy+2} q10,-12 20,0 q10,12 20,0" fill="none" stroke="{INK2}" stroke-width="2"/>')
        p.append(f'<text x="{x0+120}" y="{cy-50}" text-anchor="middle" fill="{DGREEN}" font-size="12.5" font-weight="700" style="{FS}">{t}</text>')
        _wrap(p, x0+120, cy+60, d, INK2, 32)
    return _svg(W, H, "Laminar vs turbulent", p)


def air_exchange():
    W, H = 660, 280
    p = []; _title(p, "Air exchange: turning the room over", "fresh in, stale out, mixed throughout")
    rx, ry, rw, rh = 120, 70, 420, 150
    p.append(f'<rect x="{rx}" y="{ry}" width="{rw}" height="{rh}" rx="6" fill="{PANEL2}" stroke="{LINE}" stroke-width="1.5"/>')
    p.append(f'<path d="M{rx-50},{ry+40} l50,0" stroke="{BLU}" stroke-width="4"/>')
    p.append(f'<path d="M{rx},{ry+40} l-8,-5 M{rx},{ry+40} l-8,5" stroke="{BLU}" stroke-width="4" fill="none"/>')
    p.append(f'<text x="{rx-52}" y="{ry+30}" fill="{BLU}" font-size="10.5" style="{FS}">fresh in</text>')
    p.append(f'<path d="M{rx+rw},{ry+rh-40} l50,0" stroke="{AMB}" stroke-width="4"/>')
    p.append(f'<path d="M{rx+rw+50},{ry+rh-40} l-8,-5 M{rx+rw+50},{ry+rh-40} l-8,5" stroke="{AMB}" stroke-width="4" fill="none"/>')
    p.append(f'<text x="{rx+rw+2}" y="{ry+rh-48}" fill="{AMB}" font-size="10.5" style="{FS}">stale out</text>')
    # circulation
    for ccx in (rx+120, rx+250, rx+360):
        p.append(f'<circle cx="{ccx}" cy="{ry+rh/2}" r="26" fill="none" stroke="{GD}" stroke-width="2" stroke-dasharray="4 3"/>')
        p.append(f'<path d="M{ccx+26},{ry+rh/2} l-6,-7 M{ccx+26},{ry+rh/2} l-9,2" stroke="{GD}" stroke-width="2" fill="none"/>')
    p.append(f'<text x="{rx+rw/2}" y="{ry+rh+26}" text-anchor="middle" fill="{MUT}" font-size="11" style="{FS}">Air changes per hour (ACH) = how many times the whole room volume is replaced each hour.</text>')
    return _svg(W, H, "Air exchange", p)


# ---------------------------------------------------------------- GMP / quality
def cleanroom_grades():
    W, H = 700, 250
    p = []; _title(p, "Cleanroom grades: cleaner where it matters", "tighter air the closer you get to open product")
    grades = [("Grade D", "general / packaging", REDL), ("Grade C", "support areas", AMBL), ("Grade B", "background to A", GXL), ("Grade A", "open product / fill", GL)]
    cx, cy = 350, 150;
    for i, (g, d, c) in enumerate(grades):
        rw = 300 - i * 66; rh = 150 - i * 32
        p.append(f'<rect x="{cx-rw/2:.0f}" y="{cy-rh/2:.0f}" width="{rw:.0f}" height="{rh:.0f}" rx="6" fill="{c}" opacity=".6" stroke="{LINE}"/>')
        p.append(f'<text x="{cx:.0f}" y="{cy-rh/2+16:.0f}" text-anchor="middle" fill="{INK}" font-size="10.5" font-weight="700" style="{FS}">{g}</text>')
    p.append(f'<text x="24" y="{H-12}" fill="{MUT}" font-size="11" style="{FS}">Nested zones: each step inward holds fewer airborne particles. Grade A (or ISO 5) is where product is open; outer grades buffer it.</text>')
    return _svg(W, H, "Cleanroom grades", p)


def ccp_tree():
    W, H = 700, 290
    p = []; _title(p, "Is this step a Critical Control Point?", "the HACCP decision, simplified")
    def box(x, y, w, h, t, c=PANEL2):
        p.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{c}" stroke="{LINE}"/>')
        _wrap(p, x+w/2, y+h/2-2, t, INK, int(w/7), 10.5)
    box(280, 55, 140, 40, "Is there a hazard here?")
    box(280, 120, 140, 40, "Can a later step control it?")
    box(60, 195, 150, 44, "CCP: must control & monitor here", GL)
    box(480, 195, 150, 44, "Not a CCP, control it later", AMBL)
    p.append(f'<line x1="350" y1="95" x2="350" y2="120" stroke="{MUT}" stroke-width="1.5"/>')
    p.append(f'<text x="356" y="112" fill="{MUT}" font-size="9" style="{FS}">yes</text>')
    p.append(f'<path d="M280,160 L135,195" stroke="{MUT}" stroke-width="1.5"/>')
    p.append(f'<text x="180" y="180" fill="{MUT}" font-size="9" style="{FS}">no</text>')
    p.append(f'<path d="M420,160 L555,195" stroke="{MUT}" stroke-width="1.5"/>')
    p.append(f'<text x="500" y="180" fill="{MUT}" font-size="9" style="{FS}">yes</text>')
    return _svg(W, H, "CCP decision", p)


def qa_vs_qc():
    W, H = 700, 230
    p = []; _title(p, "QA vs QC", "build it right vs catch what is wrong")
    for i, (t, sub, items, c) in enumerate([
        ("QA  (Quality Assurance)", "process · prevent · proactive", ["SOPs & training", "validated methods", "the system that stops defects"], GL),
        ("QC  (Quality Control)", "product · detect · reactive", ["sampling & testing", "release/reject calls", "checks that catch defects"], BLUL)]):
        x = 40 + i * 340
        p.append(f'<rect x="{x}" y="60" width="300" height="150" rx="8" fill="{c}" opacity=".5" stroke="{LINE}"/>')
        p.append(f'<text x="{x+150}" y="86" text-anchor="middle" fill="{INK}" font-size="13" font-weight="700" style="{FS}">{t}</text>')
        p.append(f'<text x="{x+150}" y="104" text-anchor="middle" fill="{INK2}" font-size="10.5" style="{FS}">{sub}</text>')
        for k, it in enumerate(items):
            p.append(f'<text x="{x+20}" y="{130+k*24}" fill="{INK}" font-size="11" style="{FS}">• {it}</text>')
    return _svg(W, H, "QA vs QC", p)


def doc_hierarchy():
    W, H = 640, 270
    p = []; _title(p, "The quality document pyramid", "policy at the top, records at the base")
    levels = [("Policy / Quality Manual", "what & why", GL), ("Procedures (SOPs)", "how, step by step", GXL), ("Work instructions / forms", "the exact detail", AMBL), ("Records", "proof it happened", BLUL)]
    cx, top, totalh = 320, 60, 180
    for i, (t, d, c) in enumerate(levels):
        y = top + i * (totalh / 4)
        w1 = 80 + i * 130; w2 = 80 + (i + 1) * 130
        h = totalh / 4 - 4
        p.append(f'<path d="M{cx-w1/2:.0f},{y:.0f} L{cx+w1/2:.0f},{y:.0f} L{cx+w2/2:.0f},{y+h:.0f} L{cx-w2/2:.0f},{y+h:.0f} Z" fill="{c}" opacity=".65" stroke="{LINE}"/>')
        p.append(f'<text x="{cx}" y="{y+h/2-1:.0f}" text-anchor="middle" fill="{INK}" font-size="10.5" font-weight="700" style="{FS}">{t}</text>')
        p.append(f'<text x="{cx}" y="{y+h/2+13:.0f}" text-anchor="middle" fill="{INK2}" font-size="9" style="{FS}">{d}</text>')
    return _svg(W, H, "Document hierarchy", p)


# ---------------------------------------------------------------- tissue culture / water / ipm
def qpcr_vs_lamp():
    W, H = 700, 240
    p = []; _title(p, "Two ways to test for the viroid", "both find HpLVd; one needs a lab, one does not")
    for i, (t, steps, d) in enumerate([
        ("RT-qPCR", ["extract RNA", "thermal cycle", "fluorescence read"], "gold standard, lab thermocycler, most sensitive"),
        ("RT-LAMP", ["simple prep", "one warm temp", "colour change"], "fast, cheap, in-room, slightly less sensitive")]):
        y = 70 + i * 80; x0 = 150; bw = 130
        p.append(f'<text x="24" y="{y+24}" fill="{DGREEN}" font-size="12.5" font-weight="700" style="{FS}">{t}</text>')
        for k, s in enumerate(steps):
            x = x0 + k * (bw + 20)
            p.append(f'<rect x="{x}" y="{y}" width="{bw}" height="40" rx="6" fill="{GL if i==0 else BLUL}" opacity=".6" stroke="{LINE}"/>')
            _wrap(p, x+bw/2, y+24, s, INK, 16, 10)
            if k < 2:
                p.append(f'<text x="{x+bw+10}" y="{y+26}" fill="{MUT}" font-size="14">&rarr;</text>')
        p.append(f'<text x="{x0}" y="{y+58}" fill="{INK2}" font-size="10" style="{FS}">{d}</text>')
    return _svg(W, H, "qPCR vs LAMP", p)


def ro_membrane():
    W, H = 680, 240
    p = []; _title(p, "Reverse osmosis: pushing water through, leaving salts", "pressure makes clean water; salts are flushed away")
    mx = 340
    p.append(f'<rect x="{mx-6}" y="70" width="12" height="120" fill="{INK2}"/>')
    p.append(f'<text x="{mx}" y="205" text-anchor="middle" fill="{INK2}" font-size="10" style="{FS}">membrane</text>')
    # feed side salts + water
    for sx in range(90, mx-30, 26):
        for sy in range(90, 180, 26):
            p.append(f'<circle cx="{sx}" cy="{sy}" r="3" fill="{SALT}"/>')
    p.append(f'<rect x="80" y="80" width="{mx-90}" height="100" fill="{WATERL}" opacity=".4"/>')
    p.append(f'<text x="{(80+mx)/2:.0f}" y="74" text-anchor="middle" fill="{INK}" font-size="10.5" font-weight="700" style="{FS}">feed: water + salts</text>')
    # permeate side clean
    p.append(f'<rect x="{mx+6}" y="80" width="180" height="100" fill="{WATERL}" opacity=".7"/>')
    p.append(f'<text x="{mx+96}" y="74" text-anchor="middle" fill="{INK}" font-size="10.5" font-weight="700" style="{FS}">pure permeate</text>')
    for yy in (105, 135, 165):
        p.append(f'<path d="M{mx-30},{yy} l60,0" stroke="{WATER}" stroke-width="2.5"/>')
        p.append(f'<path d="M{mx+30},{yy} l-7,-4 M{mx+30},{yy} l-7,4" stroke="{WATER}" stroke-width="2.5" fill="none"/>')
    p.append(f'<path d="M150,200 l-60,20" stroke="{SALT}" stroke-width="2.5"/>')
    p.append(f'<text x="70" y="232" fill="{SALT}" font-size="10" style="{FS}">concentrate to drain</text>')
    return _svg(W, H, "Reverse osmosis", p)


def alkalinity_buffer():
    W, H = 680, 250
    p = []; _title(p, "Alkalinity is pH's hidden buffer", "high-alkalinity water resists your pH-down, then drops fast")
    left, right, top, bot = 60, 30, 60, 200
    def X(f): return left + f * (W - left - right)
    def Y(v): return bot - (v - 4) / (8 - 4) * (bot - top)
    # buffered curve: flat high then steep drop
    pts = [(0, 7.6), (.2, 7.4), (.4, 7.1), (.55, 6.8), (.65, 6.2), (.72, 5.4), (.8, 4.6), (1, 4.2)]
    path = "M" + " L".join(f"{X(f):.0f},{Y(v):.0f}" for f, v in pts)
    p.append(f'<path d="{path}" fill="none" stroke="{GD}" stroke-width="3"/>')
    for v in (4, 5, 6, 7, 8):
        p.append(f'<line x1="{left}" y1="{Y(v):.0f}" x2="{W-right}" y2="{Y(v):.0f}" stroke="{LINE}" stroke-width=".8" stroke-dasharray="3 4"/>')
        p.append(f'<text x="{left-8}" y="{Y(v)+4:.0f}" text-anchor="end" fill="{MUT}" font-size="10" style="{MN}">{v}</text>')
    p.append(f'<text x="{X(.3):.0f}" y="{Y(7.3):.0f}" fill="{INK2}" font-size="10" style="{FS}">buffer resists</text>')
    p.append(f'<text x="{X(.78):.0f}" y="{Y(5.2):.0f}" fill="{RED}" font-size="10" style="{FS}">crash</text>')
    p.append(f'<text x="{(left+W)/2:.0f}" y="{bot+22:.0f}" text-anchor="middle" fill="{MUT}" font-size="10.5" style="{FS}">acid added &rarr;</text>')
    p.append(f'<text x="24" y="{H-8}" fill="{MUT}" font-size="11" style="{FS}">Treat alkalinity (bicarbonate), not just pH: high-alkalinity water fights every correction, then over-swings.</text>')
    return _svg(W, H, "Alkalinity buffering", p)


def spray_vs_drench():
    W, H = 680, 250
    p = []; _title(p, "Foliar spray vs root drench", "where the product lands decides what it can do")
    for i, (t, foliar, d) in enumerate([("Foliar spray", True, "coats leaf surfaces; contact action, fast, washes/wears off"),
                                        ("Root drench", False, "into the medium; taken up by roots, systemic, lasts longer")]):
        cx = 200 + i * 320; base = 200; top = 105
        p.append(f'<line x1="{cx}" y1="{base}" x2="{cx}" y2="{top}" stroke="{DGREEN}" stroke-width="3"/>')
        for ly in (120, 150, 180):
            for sgn in (-1, 1):
                p.append(f'<ellipse cx="{cx+sgn*24}" cy="{ly}" rx="22" ry="8" fill="{G}" opacity=".85" transform="rotate({sgn*16} {cx+sgn*24} {ly})"/>')
        p.append(f'<rect x="{cx-46}" y="{base}" width="92" height="22" rx="3" fill="{DRYL}" stroke="{MUT}"/>')
        if foliar:
            for sgn in (-1, 1):
                for ly in (120, 150):
                    p.append(f'<circle cx="{cx+sgn*30}" cy="{ly-6}" r="2" fill="{BLU}"/>')
            p.append(f'<text x="{cx}" y="100" text-anchor="middle" fill="{BLU}" font-size="10">droplets on leaves</text>')
        else:
            p.append(f'<path d="M{cx},{base+22} l0,12" stroke="{WATER}" stroke-width="3"/>')
            for dy in (210,):
                p.append(f'<path d="M{cx-20},{base+8} q20,6 40,0" fill="none" stroke="{WATER}" stroke-width="2"/>')
        p.append(f'<text x="{cx}" y="92" text-anchor="middle" fill="{DGREEN}" font-size="12.5" font-weight="700" style="{FS}">{t}</text>')
        _wrap(p, cx, base+40, d, INK2, 30)
    return _svg(W, H, "Spray vs drench", p)


def floor_plan():
    W, H = 700, 280
    p = []; _title(p, "A clean one-way facility flow", "people and product move dirty-to-clean, never back")
    rooms = [("Intake / mother", 40, 70, 150, 80, GXL), ("Veg", 200, 70, 120, 80, GL),
             ("Flower", 330, 70, 150, 80, GL), ("Dry / cure", 490, 70, 110, 80, AMBL),
             ("Trim / pack", 490, 170, 110, 70, BLUL), ("QA / vault", 330, 170, 150, 70, PURL)]
    for t, x, y, w, h, c in rooms:
        p.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="{c}" opacity=".55" stroke="{LINE}"/>')
        _wrap(p, x+w/2, y+h/2+4, t, INK, int(w/7), 10.5)
    # flow arrows
    for (x1, y1, x2, y2) in [(190,110,200,110),(320,110,330,110),(480,110,490,110),(545,150,545,170),(490,205,480,205),(330,205,250,205)]:
        p.append(f'<path d="M{x1},{y1} L{x2},{y2}" stroke="{DGREEN}" stroke-width="2.5"/>')
        dx, dy = x2-x1, y2-y1
        p.append(f'<circle cx="{x2}" cy="{y2}" r="3" fill="{DGREEN}"/>')
    p.append(f'<text x="24" y="{H-12}" fill="{MUT}" font-size="11" style="{FS}">One-directional flow keeps clean product away from incoming material and waste, the backbone of contamination control.</text>')
    return _svg(W, H, "Facility flow", p)
