# -*- coding: utf-8 -*-
"""Paper: airflow design for indoor cultivation (beginner)."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        stagecard, grid, card, chip, kv, steps)
import figs_lib as L
from figs import (G, GD, GL, GXL, INK, INK2, MUT, LINE, AMB, AMBL, RED, BLU, BLUL,
                  PUR, PURL, PAPER, PANEL2, FS, MN)

SLUG = "airflow-design"
TITLE = "Airflow design for indoor cultivation"
EYEBROW = "Basic · Airflow design"
SUB = ("Each leaf has a layer of still air that decreases the rate of gas exchange. Airflow removes "
       "this layer. After you read this paper, you will know how much air to move and which fans "
       "supply the air. You will also know where to put the fans, to give each leaf a light airflow.")
META = [("wind", "Basic"), ("image", "8 diagrams · 8 photos"),
        ("quote", "18 sources"), ("clock", "~26 min to read")]
RELATED = ["grow-room-systems", "mould-risk", "coco-crop-steering"]
REF_IDS = ["schuepp1993-bl", "dupont2025-wind", "kitaya2004-airvel", "tjosvold2018-air",
           "rm2021-light", "kitaya2010-circ", "gilliham2011-ca", "chehab2009-thigmo",
           "chandra2008-photo", "pipp2026-airflow",
           "bartok-haf", "uconn-haf", "goto1992-tipburn", "ahmed2020-multifan",
           "moosavi2025-vaf", "perfduct2025", "amca-fanlaws", "vas-inrack"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

def _fig_boundary():
    W, H = 720, 300
    p = [f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="The boundary layer of still air on a leaf">']
    p.append(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')
    p.append(f'<text x="24" y="30" fill="{INK}" font-size="15" font-weight="700" style="{FS}">The boundary layer: a layer of still air with high humidity on each leaf</text>')
    # leaf
    lx, ly = 150, 170
    p.append(f'<ellipse cx="{lx+120}" cy="{ly}" rx="150" ry="20" fill="{GL}" stroke="{G}" stroke-width="2"/>')
    p.append(f'<text x="{lx+120}" y="{ly+5}" text-anchor="middle" fill="{GD}" font-size="12" font-weight="700" style="{FS}">leaf surface</text>')
    # boundary layer (still air), shaded band hugging the leaf
    p.append(f'<path d="M{lx-25},{ly-10} q145,-34 290,0 q-145,30 -290,0 Z" fill="{BLUL}" opacity=".8"/>')
    p.append(f'<text x="{lx+120}" y="{ly-22}" text-anchor="middle" fill="{BLU}" font-size="11.5" style="{FS}">layer of still air (boundary layer)</text>')
    # CO2 struggling across (left, thick film)
    p.append(f'<text x="60" y="120" fill="{AMB}" font-size="12" font-weight="700" style="{FS}">CO&#8322;</text>')
    p.append(f'<path d="M70,128 q10,20 12,34" fill="none" stroke="{AMB}" stroke-width="2" stroke-dasharray="3 3" marker-end="url(#a1)"/>')
    p.append(f'<text x="40" y="150" fill="{MUT}" font-size="10.5" style="{FS}">thick layer = slow</text>')
    p.append(f'<text x="40" y="164" fill="{MUT}" font-size="10.5" style="{FS}">gas exchange</text>')
    # moving air (right) thinning the film
    for yy in (96, 112, 128):
        p.append(f'<path d="M470,{yy} q120,0 200,2" fill="none" stroke="{G}" stroke-width="2.4" marker-end="url(#a2)"/>')
    p.append(f'<text x="560" y="80" text-anchor="middle" fill="{GD}" font-size="12" font-weight="700" style="{FS}">moving air makes it thinner</text>')
    p.append(f'<text x="560" y="250" text-anchor="middle" fill="{INK2}" font-size="11.5" style="{FS}">&rarr; CO&#8322; into the leaf, water and heat out, more quickly</text>')
    p.append(f'<defs><marker id="a1" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="{AMB}"/></marker>'
             f'<marker id="a2" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="{G}"/></marker></defs>')
    p.append('</svg>')
    return "".join(p)

# ---------------------------------------------------------------------------
# Fan-type glyphs. Each returns SVG drawn around a centre point (cx, cy),
# roughly 100 wide x 100 tall. Green = the air the fan makes.
# ---------------------------------------------------------------------------
def _g_haf(cx, cy):
    """Hanging basket / horizontal-airflow fan, side view, blowing right."""
    o = [f'<line x1="{cx-34}" y1="{cy-46}" x2="{cx+2}" y2="{cy-46}" stroke="{MUT}" stroke-width="2.5"/>',
         f'<line x1="{cx-16}" y1="{cy-46}" x2="{cx-16}" y2="{cy-22}" stroke="{MUT}" stroke-width="2"/>',
         f'<rect x="{cx-32}" y="{cy-22}" width="30" height="44" rx="6" fill="{PANEL2}" stroke="{INK2}" stroke-width="2"/>']
    for k in range(4):
        o.append(f'<line x1="{cx-27+k*7}" y1="{cy-17}" x2="{cx-27+k*7}" y2="{cy+17}" stroke="{MUT}" stroke-width="1.1"/>')
    o.append(f'<circle cx="{cx-17}" cy="{cy}" r="6" fill="{INK2}"/>')
    for dy, ln in ((-15, 40), (0, 54), (15, 40)):
        o.append(f'<path d="M{cx+6},{cy+dy} h{ln}" stroke="{G}" stroke-width="2.6" fill="none" marker-end="url(#fga)"/>')
    return "".join(o)

def _g_vaf(cx, cy):
    """Vertical airflow fan: flared diffuser above, air driven straight down."""
    o = [f'<line x1="{cx}" y1="{cy-48}" x2="{cx}" y2="{cy-34}" stroke="{MUT}" stroke-width="2"/>',
         f'<path d="M{cx-46},{cy-18} q6,-20 20,-16 q26,8 52,0 q14,-4 20,16 z" fill="{PANEL2}" stroke="{INK2}" stroke-width="2"/>',
         f'<rect x="{cx-22}" y="{cy-18}" width="44" height="20" rx="4" fill="{PANEL2}" stroke="{INK2}" stroke-width="2"/>']
    for k in range(5):
        o.append(f'<line x1="{cx-15+k*8}" y1="{cy-16}" x2="{cx-15+k*8}" y2="{cy}" stroke="{MUT}" stroke-width="1.1"/>')
    for dx, ex in ((-15, -30), (0, 0), (15, 30)):
        o.append(f'<path d="M{cx+dx},{cy+5} L{cx+ex},{cy+42}" stroke="{G}" stroke-width="2.6" fill="none" marker-end="url(#fga)"/>')
    return "".join(o)

def _g_osc(cx, cy):
    """Oscillating wall fan: head on a bracket, sweeping an arc."""
    o = [f'<line x1="{cx-44}" y1="{cy-34}" x2="{cx-44}" y2="{cy+34}" stroke="{MUT}" stroke-width="3"/>',
         f'<line x1="{cx-44}" y1="{cy}" x2="{cx-26}" y2="{cy}" stroke="{MUT}" stroke-width="2.5"/>',
         f'<circle cx="{cx-10}" cy="{cy}" r="18" fill="{PANEL2}" stroke="{INK2}" stroke-width="2"/>',
         f'<circle cx="{cx-10}" cy="{cy}" r="5" fill="{INK2}"/>',
         f'<path d="M{cx-10},{cy-13} a13,13 0 0 1 11,20" fill="none" stroke="{MUT}" stroke-width="1.4"/>',
         f'<path d="M{cx-10},{cy+13} a13,13 0 0 1 -11,-20" fill="none" stroke="{MUT}" stroke-width="1.4"/>',
         f'<path d="M{cx+12},{cy-26} q26,26 0,52" fill="none" stroke="{G}" stroke-width="2.2" stroke-dasharray="4 4"/>']
    for dy in (-22, 0, 22):
        o.append(f'<path d="M{cx+10},{cy+dy*0.55:.0f} L{cx+40},{cy+dy}" stroke="{G}" stroke-width="2.4" fill="none" marker-end="url(#fga)"/>')
    return "".join(o)

def _g_clip(cx, cy):
    """Clip fan: small head on a clamp gripping a tent pole."""
    o = [f'<line x1="{cx-40}" y1="{cy-36}" x2="{cx-40}" y2="{cy+36}" stroke="{MUT}" stroke-width="4"/>',
         f'<path d="M{cx-46},{cy+8} h14 v-16 h-14" fill="none" stroke="{INK2}" stroke-width="2.4"/>',
         f'<line x1="{cx-32}" y1="{cy}" x2="{cx-20}" y2="{cy}" stroke="{MUT}" stroke-width="2.2"/>',
         f'<circle cx="{cx-8}" cy="{cy}" r="13" fill="{PANEL2}" stroke="{INK2}" stroke-width="2"/>',
         f'<circle cx="{cx-8}" cy="{cy}" r="4" fill="{INK2}"/>']
    for dy in (-11, 0, 11):
        o.append(f'<path d="M{cx+8},{cy+dy}" stroke="{G}" stroke-width="2.2" fill="none"/>')
        o.append(f'<path d="M{cx+8},{cy+dy} h22" stroke="{G}" stroke-width="2.2" fill="none" marker-end="url(#fga)"/>')
    return "".join(o)

def _g_drum(cx, cy):
    """Drum / pedestal floor fan: big head on a low stand, hard narrow jet."""
    o = [f'<circle cx="{cx-16}" cy="{cy-8}" r="26" fill="{PANEL2}" stroke="{INK2}" stroke-width="2.2"/>',
         f'<circle cx="{cx-16}" cy="{cy-8}" r="18" fill="none" stroke="{MUT}" stroke-width="1.2"/>',
         f'<circle cx="{cx-16}" cy="{cy-8}" r="10" fill="none" stroke="{MUT}" stroke-width="1.2"/>',
         f'<circle cx="{cx-16}" cy="{cy-8}" r="5" fill="{INK2}"/>',
         f'<path d="M{cx-30},{cy+18} L{cx-16},{cy+34} L{cx-2},{cy+18}" fill="none" stroke="{MUT}" stroke-width="2.4"/>',
         f'<line x1="{cx-38}" y1="{cy+36}" x2="{cx+6}" y2="{cy+36}" stroke="{MUT}" stroke-width="3"/>']
    for dy in (-14, -8, -2):
        o.append(f'<path d="M{cx+12},{cy+dy} h34" stroke="{G}" stroke-width="3.4" fill="none" marker-end="url(#fga)"/>')
    return "".join(o)

def _g_under(cx, cy):
    """Under-canopy fan: low flat body at pot level, air skimming the floor."""
    o = [f'<line x1="{cx-48}" y1="{cy+30}" x2="{cx+48}" y2="{cy+30}" stroke="{MUT}" stroke-width="2.5"/>']
    # pots + the canopy sitting overhead
    o.append(f'<rect x="{cx-22}" y="{cy-42}" width="70" height="22" rx="8" fill="{GL}" stroke="{G}" stroke-width="1.6"/>')
    o.append(f'<text x="{cx+13}" y="{cy-27}" text-anchor="middle" fill="{GD}" font-size="9.5" style="{FS}">canopy</text>')
    for px in (cx + 8, cx + 34):
        o.append(f'<path d="M{px-9},{cy+30} l3,-16 h12 l3,16 z" fill="{PANEL2}" stroke="{MUT}" stroke-width="1.6"/>')
    o.append(f'<rect x="{cx-46}" y="{cy+6}" width="34" height="24" rx="5" fill="{PANEL2}" stroke="{INK2}" stroke-width="2"/>')
    for k in range(3):
        o.append(f'<line x1="{cx-40+k*8}" y1="{cy+10}" x2="{cx-40+k*8}" y2="{cy+26}" stroke="{MUT}" stroke-width="1.1"/>')
    for dy in (12, 20, 27):
        o.append(f'<path d="M{cx-8},{cy+dy} h46" stroke="{G}" stroke-width="2.4" fill="none" marker-end="url(#fga)"/>')
    return "".join(o)

def _g_sock(cx, cy):
    """Perforated poly tube / air sock: fan feeds a tube, air leaves through many holes."""
    o = [f'<rect x="{cx-50}" y="{cy-24}" width="20" height="30" rx="4" fill="{PANEL2}" stroke="{INK2}" stroke-width="2"/>',
         f'<circle cx="{cx-40}" cy="{cy-9}" r="5" fill="{INK2}"/>',
         f'<path d="M{cx-30},{cy-24} h78 v30 h-78 z" fill="{GXL}" stroke="{INK2}" stroke-width="2"/>']
    for k in range(7):
        hx = cx - 24 + k * 11
        o.append(f'<circle cx="{hx}" cy="{cy+1}" r="2.2" fill="{INK2}"/>')
        o.append(f'<path d="M{hx},{cy+8} v18" stroke="{G}" stroke-width="2.1" fill="none" marker-end="url(#fga)"/>')
    o.append(f'<text x="{cx-1}" y="{cy-30}" text-anchor="middle" fill="{MUT}" font-size="9.5" style="{FS}">equal, low-speed supply</text>')
    return "".join(o)

def _g_duct(cx, cy):
    """Inline duct fan: exchange, not circulation. Air pulled out of the room."""
    o = [f'<rect x="{cx-50}" y="{cy-14}" width="26" height="28" rx="3" fill="none" stroke="{MUT}" stroke-width="2"/>',
         f'<rect x="{cx-24}" y="{cy-19}" width="34" height="38" rx="6" fill="{PANEL2}" stroke="{INK2}" stroke-width="2.2"/>',
         f'<circle cx="{cx-7}" cy="{cy}" r="9" fill="none" stroke="{MUT}" stroke-width="1.4"/>',
         f'<circle cx="{cx-7}" cy="{cy}" r="4" fill="{INK2}"/>',
         f'<rect x="{cx+10}" y="{cy-14}" width="26" height="28" rx="3" fill="none" stroke="{MUT}" stroke-width="2"/>',
         f'<path d="M{cx-46},{cy} h{80}" stroke="{BLU}" stroke-width="3.2" fill="none" marker-end="url(#fgb)"/>',
         f'<text x="{cx-6}" y="{cy+34}" text-anchor="middle" fill="{MUT}" font-size="9.5" style="{FS}">room air &rarr; outdoors</text>']
    return "".join(o)

def _fig_fan_gallery():
    """Eight fan types, drawn side-on with the shape of air each one makes."""
    W, H = 760, 500
    cells = [
        (_g_haf,   "HAF fan",         "Hangs high, blows to the side.",  "Makes a loop of air in the room."),
        (_g_vaf,   "VAF fan",         "Blows straight down,",         "through the canopy."),
        (_g_osc,   "Oscillating fan", "Oscillates. Low cost, but",    "each leaf gets air part of the time."),
        (_g_clip,  "Clip fan",        "Only for a tent. It moves the",       "air for approximately one plant."),
        (_g_drum,  "Drum / floor fan","Fast jet with a small width.", "For one area only. Wind damage risk."),
        (_g_under, "Under-canopy fan","Low and flat. It supplies air",     "to the wet zone at pot level."),
        (_g_sock,  "Air sock",        "Many small holes give an equal",  "air supply, no strong jet."),
        (_g_duct,  "Inline duct fan", "Air exchange, not circulation.",   "Pulls air out of the room."),
    ]
    p = [f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="The eight types of fan for an indoor grow room, and the shape of the air that each type makes">',
         f'<rect width="{W}" height="{H}" fill="{PAPER}"/>',
         f'<defs><marker id="fga" markerWidth="7" markerHeight="7" refX="5.5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="{G}"/></marker>'
         f'<marker id="fgb" markerWidth="7" markerHeight="7" refX="5.5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="{BLU}"/></marker></defs>',
         f'<text x="20" y="26" fill="{INK}" font-size="15" font-weight="700" style="{FS}">The eight types of fan, and the shape of air that each type makes</text>',
         f'<text x="20" y="45" fill="{MUT}" font-size="11.5" style="{FS}">Green is the air that the fan moves. The fans are not the same. The shape of the air controls which leaves get air.</text>']
    cw = (W - 24) / 4
    for i, (glyph, name, r1, r2) in enumerate(cells):
        col, row = i % 4, i // 4
        x0 = 12 + col * cw
        y0 = 58 + row * 214
        cx = x0 + cw / 2
        p.append(f'<rect x="{x0+4:.1f}" y="{y0}" width="{cw-8:.1f}" height="200" rx="10" fill="{PANEL2}" stroke="{LINE}" opacity=".55"/>')
        p.append(glyph(int(cx), y0 + 72))
        p.append(f'<text x="{cx:.1f}" y="{y0+150}" text-anchor="middle" fill="{INK}" font-size="12.5" font-weight="700" style="{FS}">{name}</text>')
        p.append(f'<text x="{cx:.1f}" y="{y0+169}" text-anchor="middle" fill="{INK2}" font-size="10.2" style="{FS}">{r1}</text>')
        p.append(f'<text x="{cx:.1f}" y="{y0+183}" text-anchor="middle" fill="{INK2}" font-size="10.2" style="{FS}">{r2}</text>')
    p.append('</svg>')
    return "".join(p)

def _fan_photos():
    """Photoreal reference shot of each type, reusing the site's .tgal gallery styling."""
    shots = [("HAF fan", "haf"), ("VAF fan", "vaf"), ("Oscillating fan", "osc"),
             ("Clip fan", "clip"), ("Drum / floor fan", "drum"), ("Under-canopy fan", "under"),
             ("Air sock", "sock"), ("Inline duct fan", "duct")]
    cells = "".join(
        f"<figure class='tgal-item'><img src='assets/img/airflow-fan-{k}.jpg' alt='{t} in situ' "
        f"loading='lazy'><figcaption>{t}</figcaption></figure>" for t, k in shots)
    return ("<div class='tgal-wrap'><div class='kicker'>A photo of each type "
            "<span class='fcredit'>Grok Imagine</span></div>"
            f"<div class='tgal'>{cells}</div></div>")

def _fig_haf_loop():
    """Plan view: HAF fans driving a racetrack loop, with the spacing rules called out."""
    W, H = 760, 416
    x0, x1, y0, y1 = 44, 716, 98, 346
    mid = (y0 + y1) / 2
    p = [f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="A diagram from above of the horizontal airflow in one loop. The air goes along one side and back along the other side.">',
         f'<rect width="{W}" height="{H}" fill="{PAPER}"/>',
         f'<defs><marker id="hla" markerWidth="8" markerHeight="8" refX="6" refY="3.2" orient="auto"><path d="M0,0 L7,3.2 L0,6.4 Z" fill="{G}"/></marker></defs>',
         f'<text x="20" y="26" fill="{INK}" font-size="15" font-weight="700" style="{FS}">Positions of the HAF fans from above: one loop and not a row</text>',
         f'<text x="20" y="45" fill="{MUT}" font-size="11.5" style="{FS}">Air goes along one side and back along the other side. Each fan gives air to the next fan.</text>',
         f'<rect x="{x0}" y="{y0}" width="{x1-x0}" height="{y1-y0}" rx="6" fill="{PANEL2}" stroke="{INK2}" stroke-width="2"/>',
         f'<line x1="{x0}" y1="{mid}" x2="{x1}" y2="{mid}" stroke="{LINE}" stroke-width="1" stroke-dasharray="5 5"/>']
    # canopy blocks
    for by in (y0 + 22, mid + 22):
        p.append(f'<rect x="{x0+70}" y="{by}" width="{x1-x0-140}" height="70" rx="5" fill="{GL}" opacity=".55"/>')
    p.append(f'<text x="{(x0+x1)/2}" y="{y0+64}" text-anchor="middle" fill="{GD}" font-size="11" font-weight="700" style="{FS}">canopy</text>')
    p.append(f'<text x="{(x0+x1)/2}" y="{mid+64}" text-anchor="middle" fill="{GD}" font-size="11" font-weight="700" style="{FS}">canopy</text>')
    # flow lines
    ytop, ybot = y0 + 16, y1 - 16
    p.append(f'<path d="M{x0+18},{ytop} H{x1-40}" stroke="{G}" stroke-width="3" fill="none" marker-end="url(#hla)"/>')
    p.append(f'<path d="M{x1-18},{ybot} H{x0+40}" stroke="{G}" stroke-width="3" fill="none" marker-end="url(#hla)"/>')
    p.append(f'<path d="M{x1-22},{ytop} q26,0 26,{(ybot-ytop)/2:.0f} q0,{(ybot-ytop)/2:.0f} -26,{(ybot-ytop)/2:.0f}" fill="none" stroke="{G}" stroke-width="3" marker-end="url(#hla)"/>')
    p.append(f'<path d="M{x0+22},{ybot} q-26,0 -26,-{(ybot-ytop)/2:.0f} q0,-{(ybot-ytop)/2:.0f} 26,-{(ybot-ytop)/2:.0f}" fill="none" stroke="{G}" stroke-width="3" marker-end="url(#hla)"/>')
    # fans
    def fan(fx, fy, right=True):
        d = 1 if right else -1
        return (f'<circle cx="{fx}" cy="{fy}" r="13" fill="{PAPER}" stroke="{INK2}" stroke-width="2.2"/>'
                f'<circle cx="{fx}" cy="{fy}" r="4" fill="{INK2}"/>'
                f'<path d="M{fx+13*d},{fy} h{22*d}" stroke="{GD}" stroke-width="2.6" fill="none" marker-end="url(#hla)"/>')
    for fx in (150, 350, 550):
        p.append(fan(fx, ytop, True))
    for fx in (610, 410, 210):
        p.append(fan(fx, ybot, False))
    # annotations
    p.append(f'<line x1="{x0}" y1="{y0-10}" x2="150" y2="{y0-10}" stroke="{AMB}" stroke-width="1.4"/>')
    p.append(f'<text x="{(x0+150)/2}" y="{y0-16}" text-anchor="middle" fill="{AMB}" font-size="10.5" font-weight="700" style="{FS}">3&ndash;4.5 m from the wall</text>')
    p.append(f'<line x1="150" y1="{y0-10}" x2="350" y2="{y0-10}" stroke="{AMB}" stroke-width="1.4" stroke-dasharray="4 3"/>')
    p.append(f'<text x="250" y="{y0-16}" text-anchor="middle" fill="{AMB}" font-size="10.5" font-weight="700" style="{FS}">12&ndash;15 m apart</text>')
    p.append(f'<text x="{x0+8}" y="{y1+22}" fill="{MUT}" font-size="10.5" style="{FS}">Fans are approximately a quarter of the room width from the wall, above head height, and operate 24/7.</text>')
    p.append(f'<text x="{x0+8}" y="{y1+38}" fill="{MUT}" font-size="10.5" style="{FS}">In a small room, use the same shape with a smaller distance between the fans: one loop, and do not point two fans at each other.</text>')
    p.append('</svg>')
    return "".join(p)

def _fig_zones():
    """Section view: the three vertical zones and which fan type serves each."""
    W, H = 760, 424
    fl, ce = 344, 62
    p = [f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="A vertical section of a grow room that shows the three zones of airflow">',
         f'<rect width="{W}" height="{H}" fill="{PAPER}"/>',
         f'<defs><marker id="zna" markerWidth="7" markerHeight="7" refX="5.5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="{G}"/></marker></defs>',
         f'<text x="20" y="26" fill="{INK}" font-size="15" font-weight="700" style="{FS}">Three heights, three tasks: a vertical section of the room shows the gaps</text>',
         f'<text x="20" y="45" fill="{MUT}" font-size="11.5" style="{FS}">Most rooms have fans for only the top zone. Thus rot starts at the bottom.</text>',
         f'<line x1="30" y1="{fl}" x2="600" y2="{fl}" stroke="{INK2}" stroke-width="2.5"/>',
         f'<line x1="30" y1="{ce}" x2="600" y2="{ce}" stroke="{INK2}" stroke-width="2.5"/>']
    # lights
    for lx in (150, 300, 450):
        p.append(f'<rect x="{lx-40}" y="{ce+6}" width="80" height="12" rx="3" fill="{AMBL}" stroke="{AMB}" stroke-width="1.4"/>')
    p.append(f'<text x="80" y="{ce+16}" fill="{MUT}" font-size="10" style="{FS}">lights</text>')
    # canopy + pots
    p.append(f'<rect x="110" y="180" width="400" height="88" rx="8" fill="{GL}" stroke="{G}" stroke-width="1.6"/>')
    p.append(f'<text x="310" y="228" text-anchor="middle" fill="{GD}" font-size="12.5" font-weight="700" style="{FS}">canopy</text>')
    for px in (150, 240, 330, 420, 480):
        p.append(f'<path d="M{px-14},{fl} l4,-26 h20 l4,26 z" fill="{PANEL2}" stroke="{MUT}" stroke-width="1.5"/>')
        p.append(f'<line x1="{px}" y1="{fl-26}" x2="{px}" y2="180" stroke="{G}" stroke-width="2" opacity=".55"/>')
    # zone 1: HAF above canopy
    p.append(f'<circle cx="72" cy="150" r="15" fill="{PAPER}" stroke="{INK2}" stroke-width="2.2"/>')
    p.append(f'<circle cx="72" cy="150" r="4.5" fill="{INK2}"/>')
    for dy in (-10, 0, 10):
        p.append(f'<path d="M88,{150+dy} H{500-abs(dy)*3}" stroke="{G}" stroke-width="2.4" fill="none" marker-end="url(#zna)"/>')
    # zone 2: VAF down through canopy
    p.append(f'<path d="M262,110 q22,-14 44,0 q-8,14 -22,14 q-14,0 -22,-14 z" fill="{PANEL2}" stroke="{INK2}" stroke-width="2"/>')
    p.append(f'<rect x="272" y="110" width="24" height="12" rx="3" fill="{PANEL2}" stroke="{INK2}" stroke-width="1.8"/>')
    for dx, ex in ((-8, -30), (0, 0), (8, 30)):
        p.append(f'<path d="M{284+dx},126 L{284+ex},272" stroke="{G}" stroke-width="2.6" fill="none" marker-end="url(#zna)"/>')
    # zone 3: under-canopy
    p.append(f'<rect x="52" y="{fl-30}" width="34" height="26" rx="5" fill="{PAPER}" stroke="{INK2}" stroke-width="2.2"/>')
    p.append(f'<circle cx="69" cy="{fl-17}" r="4.5" fill="{INK2}"/>')
    for dy in (-22, -13, -5):
        p.append(f'<path d="M92,{fl+dy} H480" stroke="{G}" stroke-width="2.3" fill="none" marker-end="url(#zna)"/>')
    # zone labels
    bands = [(96, 176, "ABOVE THE CANOPY", "Mix air, remove heat layers", "HAF, HVLS, air sock", GL),
             (180, 268, "THROUGH THE CANOPY", "The problem zone. Rot risk.", "VAF, in-rack, defoliation", AMBL),
             (272, fl, "BELOW THE CANOPY", "Most water, still air", "Under-canopy fans", BLUL)]
    for (ty, by, lab, why, kit, col) in bands:
        p.append(f'<rect x="612" y="{ty}" width="132" height="{by-ty}" rx="7" fill="{col}" opacity=".55" stroke="{LINE}"/>')
        p.append(f'<text x="678" y="{ty+21}" text-anchor="middle" fill="{INK}" font-size="10.4" font-weight="700" style="{FS}">{lab}</text>')
        p.append(f'<text x="678" y="{ty+38}" text-anchor="middle" fill="{INK2}" font-size="9.4" style="{FS}">{why}</text>')
        p.append(f'<text x="678" y="{by-12}" text-anchor="middle" fill="{GD}" font-size="9.4" font-weight="700" style="{FS}">{kit}</text>')
    p.append(f'<text x="30" y="{fl+28}" fill="{MUT}" font-size="10.5" style="{FS}">Walk the room. Do the leaf movement test at three heights: above the tops, in the middle of a plant (put a hand in it), and at pot level.</text>')
    p.append(f'<text x="30" y="{fl+44}" fill="{MUT}" font-size="10.5" style="{FS}">If the leaves do not move at one height, you do not have the fan for that height.</text>')
    p.append('</svg>')
    return "".join(p)

SECTIONS = []

SECTIONS.append({"id": "start", "kicker": "01 · Read this first", "title": "Purpose and scope",
  "blocks": [
    lead("Airflow keeps the gases at the leaf in movement. This paper shows the effect of airflow, "
         "how much airflow is necessary, which fans supply it, and where to put the fans. Thus each "
         "part of the canopy has a light airflow. The parts include the inner leaves in the middle "
         "of the canopy, where bud rot starts."),
    p("This paper starts with the basic facts. It shows the effect of air movement at the leaf and "
      "how much airflow you want. It also shows which fans make this airflow, how to compare the "
      "fans, and where to hang them."),
  ]})

SECTIONS.append({"id": "terms", "kicker": "02 · The terms", "title": "Definitions",
  "blocks": [
    defterm("Boundary layer", "The thin layer of still air on the surface of each leaf. Gases must "
            "go across this layer by diffusion, and diffusion is slow. Thus the layer decreases the "
            "rate of gas exchange. Airflow makes the layer thinner."),
    defterm("Air velocity", "The speed of the air at the canopy, in meters for each second (m/s). "
            "The air velocity is the value that is important for the plant. The size of the fan is "
            "not important."),
    defterm("Laminar and turbulent airflow", "Laminar airflow is smooth airflow that moves in layers (for "
            "example, a stable jet of air). Turbulent airflow is airflow in which the air changes "
            "direction frequently and mixes. Turbulent airflow is better for leaves."),
    defterm("Transpiration", "In transpiration, the plant absorbs water at the roots and releases "
            "the water as vapor through pores on the leaves. When the air is drier and the air "
            "temperature is higher, the water leaves the plant more quickly. Moving air makes "
            "transpiration faster because it removes the moist air near the leaf. If a layer of "
            "moist air stays on the leaf, the rate of transpiration decreases. Airflow removes this "
            "layer."),
    defterm("Air exchange", "The replacement of the room air with external air (intake and "
            "exhaust). Air exchange is different from recirculation. Recirculation only mixes the "
            "air that is in the room."),
    defterm("HAF / VAF", "The two primary types of fan that hang. A <strong>HAF</strong> "
            "(horizontal airflow) fan hangs above the crop and blows air to the side. Thus it makes "
            "a loop of air around the room. A <strong>VAF</strong> (vertical airflow) fan hangs "
            "above the crop and blows air straight down through the crop."),
    defterm("CFM and FPM", "CFM and FPM are two different values. Some persons think that they are "
            "the same. <strong>CFM</strong> (cubic feet for each minute) is the <em>volume</em> of "
            "air that a fan moves, and the supplier of the fan gives this value. "
            "<strong>FPM</strong> (feet for each minute) is the <em>speed</em> of the air at a "
            "leaf, and this speed is important for the plant. 1 m/s is approximately 200 FPM."),
    defterm("Throw and entrainment", "<strong>Throw</strong> is the distance from the fan to the "
            "point where the jet has the same speed as the air in the room. "
            "<strong>Entrainment</strong> is not easy to see. In entrainment, the jet pulls the "
            "still air of the room along with it. Thus a small fan can move much more air than its "
            "blades push. HAF loops operate because of entrainment."),
  ]})

SECTIONS.append({"id": "boundary", "kicker": "03 · The primary effect", "title": "Leaf boundary layers",
  "blocks": [
    p("The air on the surface of a leaf almost does not move. Thus a thin layer of still air with "
      "high humidity stays on the leaf. The air in this layer almost does not mix with the air in "
      "the room. This layer is the <strong>boundary layer</strong>.</p><p>CO2 must go into the "
      "leaf, and water vapor and heat must go out of the leaf. They must go across the boundary "
      "layer by diffusion, which is slow. When the boundary layer is thicker, they move more slowly" +
      _c("schuepp1993-bl") + "."),
    figure(_fig_boundary(), 1,
      "Still air decreases the rate of movement of gases and heat into and out of the leaf. Moving "
      "air makes the boundary layer thinner. Thus CO2 moves into the leaf more quickly, and water "
      "and heat move out of the leaf more quickly" + _c("dupont2025-wind") + "."),
    p("Moving air makes the boundary layer thinner. A small airflow has an important effect. Tests "
      "show that an added air velocity of less than approximately 0.2 m/s increases the "
      "photosynthesis in the day by 10 to 20%" + _c("dupont2025-wind") + ". Thus fans are necessary "
      "in a grow room."),
  ]})

SECTIONS.append({"id": "how-much", "kicker": "04 · The target", "title": "Airflow targets",
  "blocks": [
    p("More airflow helps, but the effect becomes much smaller each time that the airflow "
      "increases. When the airflow increases from still air to a light airflow, photosynthesis "
      "increases quickly. After this, the curve is flat. Most of the effect occurs when the leaves "
      "move a small distance" + _c("kitaya2004-airvel") + "."),
    figure(L.line("Leaf gas exchange when airflow increases: fast, then flat",
            [(0, 12), (1, 48), (2, 74), (3, 86), (4, 91), (5, 93)],
            ["still air", "0.2", "0.4", "0.6", "0.8", "1.0+"],
            ylab="relative gas exchange", ymin=0, ymax=100,
            note="Air velocity at the leaf (m/s). The effect is large at low velocity and small after a light airflow."), 2,
      "Gas exchange increases quickly and then becomes flat" + _c("kitaya2004-airvel") +
      ". The target is a <strong>light, constant airflow</strong>. At this target, the leaves move "
      "a small distance. They do not shake."),
    figure(L.zones("Air-velocity target at the canopy", 0, 2.0,
            [(0, 0.2, AMBL, "too slow: rot risk"), (0.3, 1.0, GL, "target"),
             (1.3, 2.0, AMBL, "too fast: wind damage")], unit=" m/s",
            note="Target: approximately 0.3 to 1.0 m/s in the canopy. The leaves move a small distance."), 3,
      "When the air velocity is less than approximately 0.2 m/s, disease can start in areas with "
      "still air and high humidity. When the velocity is more than approximately 1.2 m/s, there is "
      "a risk of wind damage, and the plants can become dry. Select a velocity in the middle of "
      "this range." + _c("tjosvold2018-air")),
  ]})

SECTIONS.append({"id": "match-light", "kicker": "05 · The connection", "title": "Airflow and light intensity",
  "blocks": [
    p("When the light is brighter, the leaf must have more air. High light intensity causes a high "
      "rate of photosynthesis and a high rate of transpiration. These two rates are high only if "
      "the boundary layer is thin. The yield of cannabis continues to increase when the light "
      "increases, to very high values" + _c("rm2021-light") + ". But this occurs only if the "
      "airflow and the climate control also increase. A bright room that has weak airflow cannot "
      "use all the light."),
    callout("key", "Airflow must agree with the other conditions in the room",
      p("Light, CO2, temperature, humidity and airflow have an effect on each other (refer to the "
        "<a href='grow-room-systems.html'>systems guide</a>). If you increase the light and do not "
        "increase the airflow, the leaves become hot and stay in the boundary layer of moist air" +
        _c("chandra2008-photo") + ".")),
  ]})

SECTIONS.append({"id": "transpiration", "kicker": "06 · The effects", "title": "Airflow, transpiration and nutrient uptake",
  "blocks": [
    p("When the boundary layer is thinner, CO2 moves into the leaf more quickly and water moves out "
      "of the leaf more quickly. More airflow causes more transpiration. Thus the plant must have "
      "more water and more nutrient at the roots. Two effects are important:"),
    ul([
      "<strong>Calcium tipburn:</strong> Calcium moves into the leaf in the transpiration stream. "
      "Thus the uptake of calcium changes with the flow of water" + _c("gilliham2011-ca") +
      ". If the airflow is very high and the feed is too low, calcium deficiency causes tipburn. "
      "Tipburn occurs also when the tank contains a large quantity of calcium. To correct this, "
      "make the feed agree with the airflow. Do not make the airflow agree with the feed.",
      "<strong>Stronger plants (a good effect).</strong> Air movement is a mechanical signal. When "
      "a plant has a light airflow, it makes stems that are shorter, thicker and stronger. This "
      "effect is thigmomorphogenesis" + _c("chehab2009-thigmo") + ". A plant that has good airflow "
      "can hold heavy colas without stakes.",
    ]),
    callout("note", "A second cause of tipburn",
      p("Tipburn has two opposite causes. The first cause is airflow that is too high with feed "
        "that is too low. The result is a calcium deficiency in the leaf. The second cause is a "
        "dead zone <em>in</em> a dense canopy, where the air does not move. The leaves in the dead "
        "zone cannot transpire. As a result, no calcium moves to these leaves.</p><p>In lettuce, "
        "the result is this: when you blow air directly into the inner leaves, the calcium in the "
        "leaves increases. The tipburn almost stops" + _c("goto1992-tipburn") +
        ". The top-down fans in section 10 are important because of this result.")),
  ]})

SECTIONS.append({"id": "build", "kicker": "07 · The system", "title": "Airflow system functions and equipment",
  "blocks": [
    p("The instruction &ldquo;Add a fan&rdquo; includes three different tasks. In a first room, the "
      "most frequent airflow problem is a fan that is incorrect for the task that you have:"),
    grid([
      card("Recirculation (to mix the air)", p("Move the air that is in the room. Thus each leaf has a "
        "light airflow and no dead zones occur. A dead zone is an area where the air does not move "
        "and the humidity is high. This task is for the boundary layer" + _c("kitaya2010-circ") +
        ". Most of this paper is about this task."), tag="In the room"),
      card("Air exchange (in and out)", p("Replace the room air with external air. The room air has high "
        "humidity and a low CO2 concentration. You can also push the room air through a carbon "
        "filter. Inline duct fans and wall exhaust fans do this task. Air exchange removes water "
        "from the room, but it has almost no effect on the leaf."), tag="Room and external air"),
      card("Conditioning (heating, cooling, drying)", p("An air conditioner, a dehumidifier or an air "
        "handling unit (AHU) changes the temperature and the moisture of the air. The unit must "
        "supply this conditioned air to the correct positions in the room. This supply of the air "
        "to all positions is a different problem."), tag="Change of the air"),
    ], cols=3),
    callout("warn", "Prevent dead zones",
      p("Put the fans where they push air <em>through</em> the canopy, not only along its top. "
        "Defoliate the plants until air can go into the canopy. Air goes where the resistance is "
        "low. It does not go into corners, the bottom of the canopy or the inner part of a dense "
        "canopy. Bud rot starts in these dead zones, where the air does not move and the humidity "
        "is high.")),
  ]})

SECTIONS.append({"id": "messy", "kicker": "08 · The type of airflow", "title": "Turbulent airflow and canopy mixing",
  "blocks": [
    p("Do not point one large fan straight along a row. A jet of laminar airflow makes a thick "
      "boundary layer on each surface that it touches. The air that is not on the axis of the jet "
      "does not move. <strong>Turbulent airflow</strong> comes from many fans that point in "
      "different directions, with oscillation. It changes the boundary layer on each leaf from all "
      "directions at all times. Turbulent airflow makes the boundary layer thinner more than other "
      "types of airflow" + _c("schuepp1993-bl") + _c("dupont2025-wind") + "."),
    callout("tip", "The leaf movement test",
      p("Walk through the room. Examine each leaf, from the top to the bottom and in the plants. "
        "Each leaf must move a small distance. A leaf that does not move is in a dead zone. Supply "
        "air to this area. If a leaf shakes strongly, decrease the speed of that fan.")),
  ]})

SECTIONS.append({"id": "evidence", "kicker": "09 · Test data", "title": "Data from tests in controlled rooms",
  "blocks": [
    p("The sections above are about the physiology of the leaf. This section shows if airflow "
      "changes the yield in a flower room. Pipp Horticulture, with Dr. Allison Justice and the "
      "Cannabis Research Coalition, did a controlled test in three flower rooms that were the same. "
      "The VPD, the temperature and the humidity were constant in all the rooms. Only the airflow "
      "was different" + _c("pipp2026-airflow") + "."),
    p("The three rooms had different supplied air speeds. The test gives these values in feet for "
      "each minute (FPM), a frequent unit in commercial horticulture. The values that the test "
      "compared were approximately 0.5, 1.0 and 2.0 m/s (approximately 100, 200 and 400 FPM). The "
      "test gave one clear result:"),
    figure(L.zones("Test result for each supplied air speed", 0, 420,
            [(0, 200, AMBL, "very small change"),
             (200, 420, GL, "clear, better results")], unit=" FPM",
            note="Less than approximately 200 FPM (1.0 m/s): almost no change in the crop. More than this: clear differences each time."), 4,
      "The effect was a <strong>threshold and not a continuous change</strong>. When the speed was "
      "less than approximately 1.0 m/s (approximately 200 FPM), the crop almost did not change. "
      "When the speed was more than this, the yield, the plant shape and the uniformity became "
      "better together" + _c("pipp2026-airflow") + "."),
    p("It is possible to think that this result does not agree with the flat curve at the leaf in "
      "Figure 2. But the two agree. Figure 2 gives the air velocity at one <em>leaf</em>. The FPM "
      "here is the air speed that the room <em>supplies</em> in total.</p><p>The speed of the air "
      "decreases when the air goes into the canopy. Thus the room must supply an air speed of much "
      "more than 1 m/s at the fans. This air speed gives the bottom leaves and the inner leaves the "
      "light airflow in Figure 3. A supplied air speed of approximately 1.0 m/s (approximately 200 "
      "FPM) is approximately the value that gives <em>each</em> leaf an air velocity in the target "
      "range. It gives this velocity not only to the leaves on the external side of the canopy."),
    p("The rooms with an airflow more than this threshold showed three effects:"),
    ul([
      "<strong>More flower and less larf.</strong> The stems had less biomass, and the plant used "
      "more of its energy for the bud. The trim was approximately 42% in the plants with still air, "
      "and it was much lower with good airflow. Thus less of the harvest became larf" +
      _c("pipp2026-airflow") + ".",
      "<strong>Less stress.</strong> The plants with still air had stems with more red color and "
      "more anthocyanin. Anthocyanin is a sign of stress that you can see. The plants with good "
      "airflow had a higher uniformity and less stress.",
      "<strong>More height, not weaker plants.</strong> At the end, plants with higher airflow had "
      "a height approximately 15 cm (6 in) more than the control plants with still air. Most of the "
      "vertical growth occurred before the end of week three, and the plants put <em>less</em> into "
      "the stem. This difference of height is an effect of less stress from still air. A stronger "
      "airflow that goes straight at the plants has a mechanical effect: it makes the plants "
      "shorter (refer to section 06).",
    ]),
    callout("key", "The primary result: uniformity",
      p("The personnel who did the test controlled the room very accurately, but they found a "
        "difference of position. The first 30 to 60 cm (1 to 2 ft) of each row was different from "
        "the remaining part of the row. Their important result is this: <strong>&ldquo;if airflow "
        "is not uniform, neither is your crop.&rdquo;</strong> The dead zone problem from section "
        "07 is the same problem, and the test measured it. It is more important to make sure that "
        "no leaf stays in still air than to get a high fan speed on average.")),
    callout("note", "The strength of this result",
      p("Think of this result as strong first data from a flower room. At this time, the result is "
        "not sure. The data are from one replicate. A second test is in progress, to make the "
        "statistics stronger" + _c("pipp2026-airflow") + ". The direction of the result agrees with "
        "the physiology of the leaf in the other sections of this paper.")),
  ]})

SECTIONS.append({"id": "fan-types", "kicker": "10 · The equipment", "title": "Fan types",
  "blocks": [
    lead("Fans are not the same. Each type makes a different <em>shape</em> of airflow, and the "
         "shape controls which leaves get air. Select a fan for the shape of airflow that you want. "
         "Do not select a fan for its cost or for its CFM value."),
    _fan_photos(),
    figure(_fig_fan_gallery(), 5,
      "The eight types of fan in a grow room, shown from the side with the air that each type "
      "makes. The first six are equipment for recirculation. The air sock is a method to supply "
      "air. The inline duct fan is for air exchange and not for circulation."),
    grid([
      card("HAF, horizontal airflow fan",
        p("A HAF fan is a basket fan that hangs above head height and points to the side along the "
          "room. Typically, the blade is 300 to 500&nbsp;mm (12 to 20&nbsp;in) and the motor is "
          "small (1/10 to 1/15&nbsp;hp)" + _c("bartok-haf") + ". Some HAF fans together make one "
          "slow <strong>racetrack loop</strong>: the air goes along one side of the room and back "
          "along the other side. The jet of each fan pulls the still air around it along with it "
          "(entrainment). Thus a small fan moves a large volume of "
          "air.</p><p><strong>Where:</strong> above the canopy, at a quarter of the room width from "
          "the wall. <strong>The problem:</strong> the air of the fan goes <em>along</em> the top "
          "of the crop. In a dense canopy, it does not go to the middle."), tag="Recirculation · primary fan"),
      card("VAF, vertical airflow fan",
        p("A VAF fan hangs above the canopy and blows air <strong>straight down through the "
          "canopy</strong>. Usually, it has a wide diffuser on top. Thus it gets air from a large "
          "area and supplies a wide flow of air, and not a jet with a small width. The VAF fan is "
          "the only type of fan that always supplies air to the leaves in the inner part of a "
          "plant.</p><p><strong>Where:</strong> above the canopy in a grid. Put the fans at a "
          "distance that gives an overlap of their flows of air. <strong>The problem:</strong> each "
          "fan has a higher cost and makes shade. Put the fan in a position where its shade is not "
          "on the crop."), tag="Recirculation · into the canopy"),
      card("Oscillating fan (wall or pole)",
        p("The oscillating fan is the usual fan for a grow room: a head on a bracket that "
          "oscillates. It has a low cost and it is easy to find. It is good in a small room, "
          "because the head oscillates and thus gives the turbulent airflow that section 08 "
          "recommends.</p><p><strong>Where:</strong> on a wall or a pole, pointed to <em>mix</em> "
          "the air in the room. Do not point it straight at the plants. <strong>The "
          "problem:</strong> its air goes to one part of the room at a time. Each leaf gets air for "
          "only a part of each movement of the head. Thus a large number of fans is necessary to "
          "keep a constant airflow in a large room."),
        tag="Recirculation · usual fan for a small room"),
      card("Clip fan",
        p("A clip fan is a very small oscillating fan on a clamp. The clamp attaches to the pole or "
          "the frame of a tent. The fan moves approximately the quantity of air for one "
          "plant.</p><p><strong>Where:</strong> in tents and in setups for one plant only. "
          "<strong>The problem:</strong> a clip fan does not operate correctly in a larger canopy. "
          "When the canopy is more than approximately 2&nbsp;m&sup2; (22&nbsp;ft&sup2;), clip fans "
          "are not a good selection. You get six clip fans that do the task of one hung fan, with a "
          "higher total power and a worse uniformity."), tag="Recirculation · size of a tent"),
      card("Drum / pedestal floor fan",
        p("A drum or pedestal floor fan has a large head with high power on a stand. The jet has a "
          "small width, the speed of the air is very high, and the fan makes much "
          "noise.</p><p><strong>Where:</strong> for a short time only, to remove a dead zone in a "
          "corner or to dry a room quickly after water spills. <strong>The problem:</strong> it is "
          "the most frequent cause of wind damage. The plants on the axis of the fan get a very "
          "strong airflow, and the plants that are not on the axis get no airflow. Do not use these "
          "fans as the primary source of the airflow in a room."), tag="Recirculation · for one point only"),
      card("Under-canopy fan",
        p("An under-canopy fan is a flat, wide fan at the level of the pots. It blows air across "
          "the floor and up into the bottom of the plants. The zone below the canopy has the most "
          "water and the minimum air movement in the room. Cool air moves down, the pots and the "
          "floors release water vapor into this zone, and no fan above the canopy supplies air to "
          "it.</p><p><strong>Where:</strong> at the level of the floor or the bench. Point the fan "
          "along the rows. <strong>The problem:</strong> there is almost none, and thus this fan "
          "gives a very good result for its cost. Keep the fan away from irrigation pipes. Make "
          "sure that the intake is clear of leaves on the floor."),
        tag="Recirculation · the wet zone"),
      card("Air sock (tube with holes)",
        p("An air sock is a long tube of fabric or plastic. A fan or an air handler supplies air to "
          "the tube. The air flows out through many small holes along the full length of the tube. "
          "Because the holes are small and many, the air supply along the tube is very equal, with "
          "no strong jet at one point. An investigation of this system gives approximate target "
          "values: holes of 6 to 10&nbsp;mm with a spacing of 30 to 70&nbsp;mm. The fan keeps a "
          "static pressure of approximately 30 to 40&nbsp;Pa, and thus the tube stays inflated and "
          "circular" + _c("perfduct2025") + ".</p><p><strong>Where:</strong> along the length of a "
          "row, above or below the bench. An air sock is the standard method to supply "
          "<em>conditioned</em> air from an air conditioner or a dehumidifier. It prevents a strong "
          "flow of air in one corner and a dead zone in the other corner. <strong>The "
          "problem:</strong> you must calculate the tube diameter, the hole size and the hole "
          "spacing, and the fan must make the necessary pressure."), tag="Supply · conditioned air"),
      card("Inline duct fan",
        p("An inline duct fan is a fan in a duct. It is a device for <strong>air exchange</strong> "
          "and not a device for circulation. It pulls air out of the room, usually through a carbon "
          "filter, and sends the air outdoors. It controls the humidity and gives new CO2 to a room "
          "with vents.</p><p><strong>Where:</strong> on a duct to the top of the room (hot air with "
          "high humidity moves up). Put an intake at the bottom of the room (with or without a "
          "fan). <strong>The problem:</strong> some persons think that this fan makes the airflow "
          "for the canopy, but it does not. A room that has a large inline duct fan and no "
          "recirculation fans has a canopy with still air and high humidity."), tag="Air exchange · not circulation"),
    ], cols=2),
    p("Three more types of fan are for larger rooms. Use them for the correct task and not for "
      "canopy airflow:"),
    grid([
      card("HVLS / destratification fan",
        p("An HVLS fan is a large ceiling fan with a very low speed. In a room with lights, a layer "
          "of warm air collects near the ceiling. The task of the fan is to break this layer and to "
          "push the air down again. It operates correctly in rooms with a large ceiling height. It "
          "has no effect in a room with a ceiling height of 2.4&nbsp;m."), tag="Recirculation · rooms with a large ceiling height"),
      card("Wall / shutter exhaust fan",
        p("This fan does air exchange for large volumes of air in greenhouses and large rooms. The "
          "shutters open by gravity or with a motor. It is the same type as the inline duct fan, "
          "but it is much larger. A sealed room usually does not have this fan."),
        tag="Air exchange · large volume"),
      card("AHU / HVAC supply",
        p("The AHU is the unit that does the heating, the cooling and the drying of the air. It "
          "controls the VPD. It must also have a method to supply this conditioned air equally "
          "across a canopy. Typically, this method is a duct that connects to air socks."), tag="Conditioning"),
    ], cols=3),
    card("In-rack airflow systems (vertical farms)",
      p("If the plants are on racks with many tiers, no other fan type operates correctly. Each "
        "tier is a closed space with a small height, and fans that hang above the racks cannot "
        "supply air to it. In-rack systems have a fan bar with ducts, and you install the fan bar "
        "in the rack. The fan bar pushes air along each tier or down through each tier" +
        _c("vas-inrack") + ". On racks, an in-rack system is the only system that operates "
        "correctly. The Pipp test in section 09 was a test of this setup."), tag="Recirculation · vertical racks"),
  ]})

SECTIONS.append({"id": "ranking", "kicker": "11 · The selection", "title": "Select fans for canopy airflow",
  "blocks": [
    p("A ranking is correct only for one condition, and you must give this condition. This ranking "
      "is for <strong>the airflow that is important for the crop, for each dollar of installed "
      "cost</strong>. The room is <strong>a sealed indoor flower room with one tier</strong>, with "
      "a canopy of approximately 20 to 200&nbsp;m&sup2; (215 to 2,150&nbsp;ft&sup2;). When the room "
      "is different, the sequence of the fans is different. The points after the table show how."),
    figure(L.hbars("Airflow for each dollar: sealed indoor flower room, one tier",
            [("HAF fan (hung)", 95), ("Under-canopy fan", 84), ("VAF fan (top-down)", 80),
             ("Oscillating fan", 68), ("Air sock from the AHU", 62),
             ("HVLS / destratification", 44), ("Drum / pedestal fan", 30), ("Clip fan", 22)],
            note="Values to compare the fans, not measurements. They are for airflow to the leaves for each dollar and each watt."), 6,
      "The primary fans of the room have a low cost. The two fans at the bottom of the ranking are "
      "the two fans that most new growers get."),
    table(["#", "Fan type", "Effect of the fan", "Depth in the canopy", "Selection"], [
      ["1", "<strong>HAF fan</strong>", "A loop of air around the room. It operates 24/7 with very low power.",
       "Only along the top", "<strong>Make these fans the primary fans of the room.</strong> The minimum cost for uniformity" + _c("bartok-haf")],
      ["2", "<strong>Under-canopy fan</strong>", "Removes the zone with the most water and the minimum air movement in the room",
       "Bottom of the plant", "<strong>The best fan to add, for the cost.</strong> It is for the area where bud rot starts"],
      ["3", "<strong>VAF fan</strong>", "Air that moves down into the middle of the plant",
       "The full depth. The VAF fan is the only fan that supplies air at this depth.", "<strong>Install these fans when the canopy density increases.</strong> Peer-reviewed papers show the effect on the calcium in the inner leaves" + _c("goto1992-tipburn") + _c("moosavi2025-vaf")],
      ["4", "Oscillating fan", "Low cost. Turbulent airflow that changes direction.", "Along the canopy and around it, for short times",
       "It is good as the primary fan for a canopy of less than approximately 20&nbsp;m&sup2; (215&nbsp;ft&sup2;). For a larger canopy, other fans are better."],
      ["5", "Air sock from the AHU", "Equal supply of <em>conditioned</em> air, with no strong flow of air at one point",
       "Along the row, with a light airflow", "Very good, but it has a capital cost, and you must calculate the sizes of the system" + _c("perfduct2025")],
      ["6", "HVLS / destratification", "Breaks the layer of hot air near the ceiling", "It mixes only the large volume of air.",
       "It operates correctly in rooms with a large ceiling height. It has no effect when the ceiling height is small."],
      ["7", "Drum / pedestal fan", "Air with a very high speed at one point", "A very strong airflow on the axis and no airflow in the other areas",
       "Use only to correct one area. The most frequent cause of wind damage."],
      ["8", "Clip fan", "The air for one plant", "One plant",
       "Use only in tents. Six clip fans give a worse result than one hung fan."],
    ], cls="compact",
      foot="The ranking is for the airflow for each dollar in a sealed indoor flower room with one "
           "tier. The ranking does not include equipment for air exchange (inline duct fans and "
           "wall fans). This equipment is necessary, but it does a different task, and you cannot "
           "use it as a recirculation fan."),
    callout("key", "When the ranking changes",
      ul([
        "<strong>Vertical racks:</strong> in-rack systems become #1, and HAF fans are not in the "
        "list. Fans that hang above the racks cannot supply air to the inner part of a tier" +
        _c("vas-inrack") + ".",
        "<strong>Dense canopy with no defoliation:</strong> VAF fans have a higher position than "
        "HAF fans in the ranking. Measurements show that top-down airflow is better than horizontal "
        "airflow to move air, and thus calcium, into the inner leaves" + _c("goto1992-tipburn") +
        _c("ahmed2020-multifan") + ". In greenhouse lettuce, vertical fans decreased the tipburn "
        "rating from 5.0 to less than 0.1. They also decreased the percentage of burned leaves from "
        "39% to less than 7%" + _c("moosavi2025-vaf") + ".",
        "<strong>Tents and setups for one plant:</strong> all the table changes to one or two clip "
        "fans and the inline duct fan. This selection is correct at this size.",
        "<strong>Greenhouses:</strong> HAF fans stay #1, and the air sock gets a higher position, "
        "because you also move heat in the greenhouse" + _c("uconn-haf") + ".",
      ], "tight")),
    callout("warn", "The problem that the ranking prevents",
      p("Select the airflow pattern and not the peak value. Almost all rooms with low performance "
        "have the same problem. <strong>The total CFM is large, but the airflow is not the same in "
        "all areas.</strong> Two drum fans in the corners give a high CFM value on paper. The "
        "middle of the room has still air and high humidity. Six small hung fans in a loop give a "
        "lower CFM value, but each leaf moves.")),
  ]})

SECTIONS.append({"id": "placement", "kicker": "12 · The position", "title": "Fan position",
  "blocks": [
    p("The position of the fans is a problem of airflow pattern and not a problem of area. Do not "
      "try to put a jet of air on each plant. Make all the air in the room move slowly and "
      "constantly in a loop. Then push this moving air down into the canopy."),
    figure(_fig_haf_loop(), 7,
      "The horizontal loop from above. The fans do not each supply air to one area only. The fans "
      "give air to each other around a circuit. The first fan is approximately 3 to 4.5&nbsp;m (10 "
      "to 15&nbsp;ft) from the end wall. The other fans are 12 to 15&nbsp;m (40 to 50&nbsp;ft) "
      "apart, and approximately a quarter of the room width from the side wall" + _c("bartok-haf") +
      _c("uconn-haf") + "."),
    p("Then examine the room in a vertical section. In most rooms, the airflow is only at the top "
      "of the canopy. This condition causes rot to start at the bottom and in the middle:"),
    figure(_fig_zones(), 8,
      "The same room in a vertical section. There are three heights, three different tasks, and "
      "three different fans. If the room has only HAF fans, the airflow is in the top zone only. "
      "The two zones in which disease starts have no airflow."),
    steps([
      ("Make the loop first",
       "Select one direction. Do not change it. Hang the HAF fans to make the air go along one side "
       "and back along the other side. Each fan gives air to the next fan. Do not point two fans at "
       "each other. The loop stops, and a dead zone occurs where the two jets touch" + _c("bartok-haf") +
       "."),
      ("Set the correct height",
       "Hang the fans above head height, approximately 2.1 to 2.4&nbsp;m (7 to 8&nbsp;ft) from the "
       "floor for a crop at floor level. Thus the jet goes above the canopy and does not push into "
       "the canopy" + _c("uconn-haf") + ". If hung baskets or a rack for lights are at this height, "
       "hang the fans above them or below them. Do not hang the fans at the same height."),
      ("Push air down into the canopy",
       "Install top-down fans above the crop in a grid. Put the fans at a distance that gives an "
       "overlap of their flows of air. Almost all persons do not do this step, but it supplies air "
       "to the inner leaves" + _c("goto1992-tipburn") + "."),
      ("Supply air to the floor",
       "Put fans at the level of the pots. Point the fans along the rows. Cold air with high "
       "humidity collects at this level, and no fan above the canopy moves it."),
      ("Mix the air, with no strong jets",
       "Point each fan in a direction with a small difference from the next fan. Let the "
       "oscillation change the direction. The room must have slow, turbulent airflow that mixes the "
       "air, and not a set of jets" + _c("schuepp1993-bl") + "."),
      ("Walk through the room and correct",
       "Do the leaf movement test at three heights. The heights are above the tops, in the middle "
       "of a plant and at the level of the pots. In the middle of a plant, put your hand into the "
       "plant. If the leaves do not move at one height, you do not have the fan for that height. A "
       "strip of tape on a stake, or a low-cost anemometer, gives a reading and not an estimate."),
    ]),
    callout("tip", "Operate the fans at all times",
      p("Operate the circulation fans for <strong>24 hours each day</strong>, when the lights are "
        "on and when the lights are off. The extension service recommends that the fans operate "
        "continuously. The fans can be off when the exhaust fans operate or the vents are open, "
        "because the room has air exchange at these times" + _c("bartok-haf") +
        ". When the lights are off, the leaf temperature decreases and becomes almost the same as "
        "the dew point, and condensation starts. At this time, you must not have still air" +
        _c("uconn-haf") + ".")),
  ]})

SECTIONS.append({"id": "sizing", "kicker": "13 · The numbers", "title": "Size of the system",
  "blocks": [
    p("For many years, the greenhouse industry calculated the size of horizontal airflow. Its "
      "approximate values are also correct for an indoor room. Start with these values. Then "
      "measure the airflow. Adjust the fans:"),
    table(["Item", "Approximate value", "Source"], [
      ["Total circulation capacity",
       "<strong>Approximately 36.6 m&sup3;/h for each m&sup2; of floor</strong> (approximately 2 CFM/ft&sup2;). A greenhouse of 9&nbsp;&times;&nbsp;30&nbsp;m (30&nbsp;&times;&nbsp;100&nbsp;ft) must have a total of approximately 10,000 m&sup3;/h (approximately 6,000 CFM).",
       "Bartok and Grubinger, UConn/UVM Extension" + _c("bartok-haf")],
      ["First fan position", "3 to 4.5&nbsp;m (10 to 15&nbsp;ft) from the end wall, to get the air that turns at the corner.",
       "UConn IPM" + _c("uconn-haf")],
      ["Fan spacing", "12 to 15&nbsp;m (40 to 50&nbsp;ft) apart along the loop. In a small room, decrease the distance in the same ratio.",
       "Bartok and Grubinger" + _c("bartok-haf")],
      ["Horizontal position", "Approximately &frac14; of the room width from the side wall (or the middle of the bay).",
       "UConn IPM" + _c("uconn-haf")],
      ["Installation height", "Above head height. Approximately 2.1 to 2.4&nbsp;m (7 to 8&nbsp;ft) for crops at floor level. Keep a distance from baskets and racks for lights.",
       "Bartok and Grubinger" + _c("bartok-haf")],
      ["Size of each fan", "Blade of 300 to 500&nbsp;mm (12 to 20&nbsp;in), motor of 1/10 to 1/15&nbsp;hp. A large number of small fans is better than a small number of large fans.",
       "Bartok and Grubinger" + _c("bartok-haf")],
      ["Greenhouse velocity target", "0.25 to 0.5 m/s (50 to 100 FPM) for the general movement of air in the room.",
       "UConn IPM" + _c("uconn-haf")],
      ["Cannabis flower-room target", "Approximately 1.0 m/s (approximately 200 FPM) that the room <em>supplies</em>, to give each leaf an air velocity in the target range.",
       "Pipp / Justice test" + _c("pipp2026-airflow")],
      ["Operation time", "24/7, but not while the exhaust fans operate or the vents are open.",
       "Bartok and Grubinger" + _c("bartok-haf")],
      ["Air sock specification", "Holes of 6 to 10&nbsp;mm with a spacing of 30 to 70&nbsp;mm. A static pressure of approximately 30 to 40&nbsp;Pa keeps the tube circular.",
       "Investigation of a duct with holes (CFD)" + _c("perfduct2025")],
    ], cls="compact"),
    callout("note", "The two velocity targets are different",
      p("The greenhouse value (0.25 to 0.5 m/s, or 50 to 100 FPM) and the value for cannabis "
        "(approximately 1.0 m/s, or approximately 200 FPM) are correct for different tasks. The "
        "greenhouse value is for temperature uniformity and to stop condensation on the leaves "
        "during the night. The crop has a more open canopy and less light" + _c("uconn-haf") +
        ". The value for cannabis is from a flower canopy with a high density and high light. In "
        "this canopy, the task is to push air <em>into</em> the plant" + _c("pipp2026-airflow") +
        ".</p><p>A higher canopy density increases the value, and a higher light intensity also "
        "increases the value. Use the greenhouse values for the position of the fans and the value "
        "for cannabis for the target.")),
    p("The last number is the number that decreases the cost the most. The airflow of a fan "
      "increases in the same ratio as the speed, but the shaft power increases with the "
      "<strong>cube</strong> of the speed" + _c("amca-fanlaws") + ". When the speed of a fan "
      "becomes half, the power becomes approximately one eighth. This fact has an effect on the "
      "selection of fans:"),
    callout("key", "More fans at a lower speed is always better",
      p("Two fans at full speed and eight fans at half speed can move almost the same quantity of "
        "air. But the eight fans use approximately a quarter of the power <em>and</em> give a much "
        "better airflow in all areas. The air comes from more directions, and there is a smaller "
        "number of dead zones.</p><p>Fans with an EC motor have a speed control. They have a higher "
        "cost than fans with an AC motor that has one speed, but the higher cost gives a better "
        "result. A fan with an AC motor is usually on or off. To decrease the airflow, you must set "
        "some fans to off. The result is areas without airflow at the positions of the fans that "
        "you stopped.")),
  ]})

SECTIONS.append({"id": "trouble", "kicker": "14 · When there is a problem", "title": "Troubleshooting",
  "blocks": [
    table(["Symptom", "Possible cause", "To correct it"], [
      ["Bud rot starts in the inner part of the colas", "Dead zone: the air does not go to the inner part of the canopy", "Add top-down (VAF) airflow. Defoliate the plants. Decrease the RH."],
      ["The tops of the plants move, but the middle and the bottom do not move", "All the airflow is above the canopy (HAF fans only)", "Add VAF fans above the crop. Add under-canopy fans at the level of the pots."],
      ["Rot and mildew start at the bottom of the plants", "The zone at the floor has the most water and the minimum air movement in the room", "Install under-canopy fans that blow along the rows."],
      ["Leaf tipburn, but the tank is full", "The airflow is too high for the supply of nutrient (calcium)", "Increase the feed EC to agree with the transpiration"],
      ["Tipburn only on new growth in the inner part", "The inner leaves are in still air and cannot transpire. As a result, no calcium moves to them.", "Make air go into the inner part of the canopy and not only along the top"],
      ["Leaves with the claw, or edges with wind damage", "The air velocity is too high, or a fan points at the plants", "Decrease the speed. Point the fans to mix the air and not to make strong jets."],
      ["One end of a row is always different", "The loop does not operate: the fans are too far apart or they point at each other", "Set the racetrack loop again. Do not point two fans at each other."],
      ["Large fans and much noise, but the air continues to be in layers", "The number of fans is too small, and they operate at full speed", "Use more fans at a lower speed. The power increases with the cube of the speed."],
      ["Plants with a large height and weak stems that bend", "Air movement is too low, and thus there is no mechanical signal", "Add a light, constant airflow across the canopy"],
      ["The humidity of the room stays high", "Recirculation is correct, but air exchange is not sufficient", "Increase the intake and the exhaust. Increase the dehumidification."],
      ["A cold or dry area below the outlet of the air conditioner", "The conditioned air goes to one point only", "Send the air through a duct to an air sock along the row"],
    ], cls="compact"),
  ]})

SECTIONS.append({"id": "expect", "kicker": "15 · The limits", "title": "Expected results and limitations",
  "blocks": [
    callout("key", "The primary points",
      ol(["The task of airflow is to <strong>make the boundary layer thinner</strong> on each leaf.",
          "Make a <strong>light, turbulent airflow (approximately 0.3 to 1.0 m/s)</strong> in all areas, and also in the inner part of the plants.",
          "Select the <strong>airflow pattern and not the peak value</strong>. Many small fans in a loop are better than two large fans in the corners.",
          "Supply air at <strong>all three heights</strong>: above, through and below the canopy. Only the first height is easy.",
          "More airflow causes more use of water: <strong>the feed and the humidity control must increase also</strong>" + _c("gilliham2011-ca") + ".",
          "Most of the effect occurs at low air velocity. A very high air velocity is not necessary" + _c("kitaya2004-airvel") + "."])),
    p("Airflow is one part of the system of the room. Read this paper with the <a "
      "href='grow-room-systems.html'>systems guide</a> and the <a href='mould-risk.html'>mold "
      "risk</a> paper."),
  ]})
