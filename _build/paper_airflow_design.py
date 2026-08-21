# -*- coding: utf-8 -*-
"""Paper: airflow design for indoor cultivation (beginner)."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        stagecard, grid, card, chip, kv, steps)
import figs_lib as L
from figs import (G, GD, GL, GXL, INK, INK2, MUT, LINE, AMB, AMBL, RED, BLU, BLUL,
                  PUR, PURL, PAPER, PANEL2, FS, MN)

SLUG = "airflow-design"
TITLE = "Airflow design for indoor cultivation"
EYEBROW = "Beginner · Airflow design"
SUB = ("Every leaf sits inside a film of still air that limits how fast it can breathe. "
       "Airflow strips that film away. Done right it feeds the plant and dries the room. "
       "Done wrong it scorches leaves or breeds rot.")
META = [("wind", "Beginner"), ("image", "8 diagrams · 8 photos"),
        ("quote", "Evidence-linked · 18 sources"), ("clock", "~26 min read")]
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
    p = [f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Leaf boundary layer">']
    p.append(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')
    p.append(f'<text x="24" y="30" fill="{INK}" font-size="15" font-weight="700" style="{FS}">The boundary layer: a film of still, humid air on every leaf</text>')
    # leaf
    lx, ly = 150, 170
    p.append(f'<ellipse cx="{lx+120}" cy="{ly}" rx="150" ry="20" fill="{GL}" stroke="{G}" stroke-width="2"/>')
    p.append(f'<text x="{lx+120}" y="{ly+5}" text-anchor="middle" fill="{GD}" font-size="12" font-weight="700" style="{FS}">leaf surface</text>')
    # boundary layer (still air), shaded band hugging the leaf
    p.append(f'<path d="M{lx-25},{ly-10} q145,-34 290,0 q-145,30 -290,0 Z" fill="{BLUL}" opacity=".8"/>')
    p.append(f'<text x="{lx+120}" y="{ly-22}" text-anchor="middle" fill="{BLU}" font-size="11.5" style="{FS}">still-air film (boundary layer)</text>')
    # CO2 struggling across (left, thick film)
    p.append(f'<text x="60" y="120" fill="{AMB}" font-size="12" font-weight="700" style="{FS}">CO&#8322;</text>')
    p.append(f'<path d="M70,128 q10,20 12,34" fill="none" stroke="{AMB}" stroke-width="2" stroke-dasharray="3 3" marker-end="url(#a1)"/>')
    p.append(f'<text x="40" y="150" fill="{MUT}" font-size="10.5" style="{FS}">thick film =</text>')
    p.append(f'<text x="40" y="164" fill="{MUT}" font-size="10.5" style="{FS}">slow breathing</text>')
    # moving air (right) thinning the film
    for yy in (96, 112, 128):
        p.append(f'<path d="M470,{yy} q120,0 200,2" fill="none" stroke="{G}" stroke-width="2.4" marker-end="url(#a2)"/>')
    p.append(f'<text x="560" y="80" text-anchor="middle" fill="{GD}" font-size="12" font-weight="700" style="{FS}">moving air thins it</text>')
    p.append(f'<text x="560" y="250" text-anchor="middle" fill="{INK2}" font-size="11.5" style="{FS}">&rarr; CO&#8322; in, water + heat out, faster</text>')
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
    o.append(f'<text x="{cx-1}" y="{cy-30}" text-anchor="middle" fill="{MUT}" font-size="9.5" style="{FS}">even, low-speed delivery</text>')
    return "".join(o)

def _g_duct(cx, cy):
    """Inline duct fan: exchange, not circulation. Air pulled out of the room."""
    o = [f'<rect x="{cx-50}" y="{cy-14}" width="26" height="28" rx="3" fill="none" stroke="{MUT}" stroke-width="2"/>',
         f'<rect x="{cx-24}" y="{cy-19}" width="34" height="38" rx="6" fill="{PANEL2}" stroke="{INK2}" stroke-width="2.2"/>',
         f'<circle cx="{cx-7}" cy="{cy}" r="9" fill="none" stroke="{MUT}" stroke-width="1.4"/>',
         f'<circle cx="{cx-7}" cy="{cy}" r="4" fill="{INK2}"/>',
         f'<rect x="{cx+10}" y="{cy-14}" width="26" height="28" rx="3" fill="none" stroke="{MUT}" stroke-width="2"/>',
         f'<path d="M{cx-46},{cy} h{80}" stroke="{BLU}" stroke-width="3.2" fill="none" marker-end="url(#fgb)"/>',
         f'<text x="{cx-6}" y="{cy+34}" text-anchor="middle" fill="{MUT}" font-size="9.5" style="{FS}">room air &rarr; outside</text>']
    return "".join(o)

def _fig_fan_gallery():
    """Eight fan types, drawn side-on with the shape of air each one makes."""
    W, H = 760, 500
    cells = [
        (_g_haf,   "HAF fan",         "Hangs high, blows sideways.",  "Drives the whole-room loop."),
        (_g_vaf,   "VAF fan",         "Blows straight down,",         "through the canopy."),
        (_g_osc,   "Oscillating fan", "Sweeps an arc. Cheap, but",    "each leaf gets a turn."),
        (_g_clip,  "Clip fan",        "Tent scale only. About",       "one plant's worth of air."),
        (_g_drum,  "Drum / floor fan","Hard narrow jet. A spot-fix,", "and a wind-burn risk."),
        (_g_under, "Under-canopy fan","Low and flat. Clears the",     "wet zone at pot level."),
        (_g_sock,  "Air sock",        "Many small holes give even,",  "draught-free delivery."),
        (_g_duct,  "Inline duct fan", "Exchange, not circulation.",   "Pulls air out of the room."),
    ]
    p = [f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="The eight fan types used in indoor growing and the shape of air each one makes">',
         f'<rect width="{W}" height="{H}" fill="{PAPER}"/>',
         f'<defs><marker id="fga" markerWidth="7" markerHeight="7" refX="5.5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="{G}"/></marker>'
         f'<marker id="fgb" markerWidth="7" markerHeight="7" refX="5.5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="{BLU}"/></marker></defs>',
         f'<text x="20" y="26" fill="{INK}" font-size="15" font-weight="700" style="{FS}">The eight fans, and the shape of air each one makes</text>',
         f'<text x="20" y="45" fill="{MUT}" font-size="11.5" style="{FS}">Green = the air it moves. Not interchangeable: the shape decides which leaves get served.</text>']
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
    return ("<div class='tgal-wrap'><div class='kicker'>What each one looks like"
            "<span class='fcredit'>Grok Imagine</span></div>"
            f"<div class='tgal'>{cells}</div></div>")

def _fig_haf_loop():
    """Plan view: HAF fans driving a racetrack loop, with the spacing rules called out."""
    W, H = 760, 416
    x0, x1, y0, y1 = 44, 716, 98, 346
    mid = (y0 + y1) / 2
    p = [f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Plan view of a horizontal airflow racetrack loop">',
         f'<rect width="{W}" height="{H}" fill="{PAPER}"/>',
         f'<defs><marker id="hla" markerWidth="8" markerHeight="8" refX="6" refY="3.2" orient="auto"><path d="M0,0 L7,3.2 L0,6.4 Z" fill="{G}"/></marker></defs>',
         f'<text x="20" y="26" fill="{INK}" font-size="15" font-weight="700" style="{FS}">HAF layout, seen from above: one loop, not a row of blowers</text>',
         f'<text x="20" y="45" fill="{MUT}" font-size="11.5" style="{FS}">Air runs down one side and back the other. Every fan feeds the fan in front of it.</text>',
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
    p.append(f'<text x="{x0+8}" y="{y1+22}" fill="{MUT}" font-size="10.5" style="{FS}">Fans sit about a quarter of the room width in from the wall, above head height, and run 24/7.</text>')
    p.append(f'<text x="{x0+8}" y="{y1+38}" fill="{MUT}" font-size="10.5" style="{FS}">Small rooms use the same shape at metres, not tens of metres: one loop, no fan blowing into another’s face.</text>')
    p.append('</svg>')
    return "".join(p)

def _fig_zones():
    """Section view: the three vertical zones and which fan type serves each."""
    W, H = 760, 424
    fl, ce = 344, 62
    p = [f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Section through a grow room showing the three airflow zones">',
         f'<rect width="{W}" height="{H}" fill="{PAPER}"/>',
         f'<defs><marker id="zna" markerWidth="7" markerHeight="7" refX="5.5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="{G}"/></marker></defs>',
         f'<text x="20" y="26" fill="{INK}" font-size="15" font-weight="700" style="{FS}">Three heights, three jobs: cut the room sideways and the gaps show up</text>',
         f'<text x="20" y="45" fill="{MUT}" font-size="11.5" style="{FS}">Most rooms buy only the top zone, then wonder why rot starts at the bottom.</text>',
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
    bands = [(96, 176, "ABOVE THE CANOPY", "Mix, and break heat layers", "HAF, HVLS, air sock", GL),
             (180, 268, "THROUGH THE CANOPY", "The hard part. Rot risk.", "VAF, in-rack, defoliation", AMBL),
             (272, fl, "BELOW THE CANOPY", "Wettest, stillest air", "Under-canopy fans", BLUL)]
    for (ty, by, lab, why, kit, col) in bands:
        p.append(f'<rect x="612" y="{ty}" width="132" height="{by-ty}" rx="7" fill="{col}" opacity=".55" stroke="{LINE}"/>')
        p.append(f'<text x="678" y="{ty+21}" text-anchor="middle" fill="{INK}" font-size="10.4" font-weight="700" style="{FS}">{lab}</text>')
        p.append(f'<text x="678" y="{ty+38}" text-anchor="middle" fill="{INK2}" font-size="9.4" style="{FS}">{why}</text>')
        p.append(f'<text x="678" y="{by-12}" text-anchor="middle" fill="{GD}" font-size="9.4" font-weight="700" style="{FS}">{kit}</text>')
    p.append(f'<text x="30" y="{fl+28}" fill="{MUT}" font-size="10.5" style="{FS}">Walk the room at three heights: over the tops, hand pushed into the middle of a plant, and down at pot level.</text>')
    p.append(f'<text x="30" y="{fl+44}" fill="{MUT}" font-size="10.5" style="{FS}">Whichever height fails the flutter test is the fan you are missing.</text>')
    p.append('</svg>')
    return "".join(p)

SECTIONS = []

SECTIONS.append({"id": "start", "kicker": "01 · Read this first", "title": "Purpose and scope",
  "blocks": [
    lead("Airflow is plumbing for gases, and it is as important as light and feed. Without moving "
         "air, even a perfect light and a perfect feed cannot reach the leaf properly. A still, "
         "humid canopy is exactly where bud rot begins."),
    p("This guide explains, from zero, what air movement does at the leaf, how much you want, "
      "which fans actually make that air, how to rank them, and where to hang them."),
  ]})

SECTIONS.append({"id": "terms", "kicker": "02 · The vocabulary", "title": "Definitions",
  "blocks": [
    defterm("Boundary layer", "The thin film of still air that clings to every leaf surface. Gases "
            "have to diffuse across it slowly, so it is the bottleneck airflow attacks."),
    defterm("Air velocity", "How fast air is moving at the canopy, in metres per second (m/s). This "
            "is what matters, not how big your fan is."),
    defterm("Laminar vs turbulent", "Laminar = smooth, layered airflow (like a calm jet). Turbulent "
            "= messy, mixing airflow. For leaves, messy is better."),
    defterm("Transpiration", "The plant drinking water at the roots and releasing it as vapour from "
            "the leaves. Airflow speeds it up by clearing the humid film."),
    defterm("Air exchange", "Swapping room air with fresh air (intake/exhaust). Different from "
            "recirculation, which only stirs the air already in the room."),
    defterm("HAF / VAF", "The two main hanging fan types. <strong>HAF</strong> = horizontal airflow: "
            "hangs above the crop and blows sideways to drive a room-wide loop. <strong>VAF</strong> "
            "= vertical airflow: hangs above the crop and blows straight down through it."),
    defterm("CFM and FPM", "Two different things people confuse. <strong>CFM</strong> (cubic feet per "
            "minute) is the <em>volume</em> a fan shifts, which is what it is sold on. "
            "<strong>FPM</strong> (feet per minute) is the <em>speed</em> air arrives at a leaf, which "
            "is what the plant feels. 200 FPM &asymp; 1 m/s."),
    defterm("Throw and entrainment", "<strong>Throw</strong> is how far a fan's jet stays useful. "
            "<strong>Entrainment</strong> is the jet dragging still room air along with it, which is "
            "why a modest hanging fan can stir far more air than it actually pushes through its own "
            "blades. It is the whole reason HAF loops work."),
  ]})

SECTIONS.append({"id": "boundary", "kicker": "03 · The core idea", "title": "Leaf boundary layers",
  "blocks": [
    p("Air right against a leaf barely moves. It forms a stagnant film called the "
      "<strong>boundary layer</strong>. CO2 going in, and water vapour and heat coming out, all have "
      "to crawl across that film by slow diffusion. The thicker it is, the more it slows the "
      "leaf" + _c("schuepp1993-bl") + "."),
    figure(_fig_boundary(), 1,
      "Still air insulates the leaf and slows every exchange. Moving air thins the boundary layer so "
      "CO2 gets in faster and water and heat get out faster" + _c("dupont2025-wind") + "."),
    p("Moving air thins that film. Even small breezes make a real difference: gentle wind "
      "(under ~0.2 m/s added) has been shown to lift daytime photosynthesis by 10–20%" + _c("dupont2025-wind") +
      ". This is the reason fans belong in a grow room."),
  ]})

SECTIONS.append({"id": "how-much", "kicker": "04 · The target", "title": "Airflow targets",
  "blocks": [
    p("More airflow helps, but with sharply diminishing returns. Photosynthesis climbs "
      "steeply as you go from dead-still up to a gentle breeze, then flattens out. Most of the "
      "benefit is won by the time leaves are gently fluttering" + _c("kitaya2004-airvel") + "."),
    figure(L.line("Airflow vs leaf gas exchange: steep early, flat later",
            [(0, 12), (1, 48), (2, 74), (3, 86), (4, 91), (5, 93)],
            ["still", "0.2", "0.4", "0.6", "0.8", "1.0+"],
            ylab="relative gas exchange", ymin=0, ymax=100,
            note="Air velocity at the leaf (m/s). The big wins come early. Past a gentle breeze you gain little."), 2,
      "Gas exchange rises fast then plateaus" + _c("kitaya2004-airvel") + ". The practical target is a "
      "<strong>gentle, constant breeze</strong>. Leaves should flutter slightly, not thrash."),
    figure(L.zones("Air-velocity target at the canopy", 0, 2.0,
            [(0, 0.2, AMBL, "too still: rot risk"), (0.3, 1.0, GL, "sweet spot"),
             (1.3, 2.0, AMBL, "too windy: wind-burn")], unit=" m/s",
            note="Aim for roughly 0.3–1.0 m/s moving through the canopy. A flutter, not a gale."), 3,
      "Below ~0.2 m/s, humid pockets and disease creep in. Above ~1.2 m/s you risk wind-stress and "
      "drying the plants out. Aim for the middle." + _c("tjosvold2018-air")),
  ]})

SECTIONS.append({"id": "match-light", "kicker": "05 · The link", "title": "Matching airflow to light intensity",
  "blocks": [
    p("The brighter the room, the more the leaf needs air. High light drives high photosynthesis and "
      "high transpiration, and both depend on the boundary layer staying thin. Cannabis yield keeps "
      "rising with light to very high levels" + _c("rm2021-light") + ", but only if airflow and "
      "climate scale with it. A bright room with weak airflow wastes the light."),
    callout("key", "Airflow moves with the rest of the room",
      p("Light, CO2, temperature, humidity and airflow work together (see the "
        "<a href='grow-room-systems.html'>systems guide</a>). Turning up the light without turning up "
        "the air leaves hot leaves sitting in their own humid film" + _c("chandra2008-photo") + ".")),
  ]})

SECTIONS.append({"id": "transpiration", "kicker": "06 · The trade-off", "title": "Airflow, transpiration and nutrient demand",
  "blocks": [
    p("Thinning the boundary layer feeds CO2 in and pulls water out faster. More "
      "airflow means more transpiration, which means the plant needs more water and nutrient at the "
      "roots. There are two beginner gotchas here:"),
    ul([
      "<strong>Calcium tip-burn.</strong> Calcium rides into the leaf on the transpiration stream, "
      "so uptake tracks water flow" + _c("gilliham2011-ca") + ". Crank the airflow and under-feed, "
      "and you get calcium-deficiency tip-burn even with plenty in the tank. Fix: feed to "
      "match the airflow, not the other way round.",
      "<strong>Sturdier plants (a good thing).</strong> Air movement is a mechanical signal. Plants "
      "that feel a breeze grow shorter, thicker, stronger stems, an effect called "
      "thigmomorphogenesis" + _c("chehab2009-thigmo") + ". A well-aired plant holds heavy colas without "
      "staking.",
    ]),
    callout("note", "The other half of the calcium story",
      p("Tip-burn cuts both ways, and the direction depends on <em>where</em> the still air is. Too "
        "much airflow with too little feed starves the leaf of calcium. But so does a dead-still "
        "pocket <em>buried inside</em> a dense canopy, because the leaves in there cannot transpire "
        "at all, so no calcium arrives. In lettuce, this is the classic result: blowing air directly "
        "into the inner leaves raises their calcium and largely stops tip-burn" + _c("goto1992-tipburn") +
        ". That is the single best argument for the top-down fans in section 10.")),
  ]})

SECTIONS.append({"id": "build", "kicker": "07 · The layout", "title": "Airflow system functions and equipment",
  "blocks": [
    p("&ldquo;Add a fan&rdquo; hides three separate jobs. Buying the wrong one for the job you "
      "actually have is the most common airflow mistake in a first room:"),
    grid([
      card("Recirculation (mixing)", p("Move the air that is already in the room so every leaf gets a "
        "gentle breeze and no humid dead-zones form. This is the boundary-layer job" +
        _c("kitaya2010-circ") + ", and it is what most of this paper is about."), tag="Inside the room"),
      card("Exchange (in / out)", p("Swap stale, humid, CO2-depleted room air for fresh air, or push "
        "it through a carbon filter. Inline duct fans and wall exhausts. This removes water; it does "
        "almost nothing for the leaf."), tag="Room ↔ outside"),
      card("Conditioning (heat / cool / dry)", p("An air conditioner, dehumidifier or air-handling "
        "unit changes the air's temperature and moisture. It has to <em>deliver</em> that treated air "
        "somewhere, which is a distribution problem of its own."), tag="Changing the air"),
    ], cols=3),
    callout("warn", "Mind the dead zones",
      p("Air takes the easy path and skips corners, the lower canopy, and the inside of dense "
        "plants. Those still, humid pockets are where bud rot starts. Place fans to push air "
        "<em>through</em> the canopy, not just over the top of it, and defoliate enough to let air in.")),
  ]})

SECTIONS.append({"id": "messy", "kicker": "08 · A subtlety", "title": "Turbulent airflow and canopy mixing",
  "blocks": [
    p("Aiming one big fan straight down a row is tempting. Don't. A smooth, laminar jet builds its "
      "own thick boundary layer on whatever it hits, and leaves everything off-axis still. "
      "<strong>Turbulent, mixing air</strong>, from many fans at varied angles with oscillation, "
      "constantly disturbs the film on every leaf from every direction, which is exactly what thins "
      "it best" + _c("schuepp1993-bl") + _c("dupont2025-wind") + "."),
    callout("tip", "The flutter test",
      p("Walk the room. Every leaf, top to bottom and inside the plants, should be gently moving. "
        "Still leaves anywhere = a pocket you need to reach. A leaf that is flapping hard = back that "
        "fan off.")),
  ]})

SECTIONS.append({"id": "evidence", "kicker": "09 · Field evidence", "title": "Evidence from controlled room trials",
  "blocks": [
    p("Everything above is leaf physiology. Does it actually move yield in a real flower room? A "
      "controlled trial by Pipp Horticulture with Dr. Allison Justice and the Cannabis Research "
      "Coalition tested exactly that: three identical flower rooms with VPD, temperature and humidity "
      "held constant, changing only the airflow" + _c("pipp2026-airflow") + "."),
    p("The rooms ran at different delivered air speeds, measured in feet per minute (FPM), the standard "
      "unit for room airflow. They compared near-still air against roughly 100, 200 and 400 FPM "
      "(about 0.5, 1.0 and 2.0 m/s). One clean result fell out:"),
    figure(L.zones("What the trial found, by delivered airflow", 0, 420,
            [(0, 200, AMBL, "muted: little measurable change"),
             (200, 420, GL, "clear, consistent gains")], unit=" FPM",
            note="Below ~200 FPM (≈1.0 m/s) airflow barely moved the crop. Above it, differences were clear and repeatable."), 4,
      "The response was a <strong>threshold, not a gentle slope</strong>: below ~200 FPM little changed; "
      "above it, yield, plant shape and uniformity improved together" + _c("pipp2026-airflow") + "."),
    p("That looks like it fights the leaf-level plateau in Figure 2, but it does not. Figure 2 is the "
      "speed at a single <em>leaf</em>; FPM here is what the whole room <em>delivers</em>. Air slows as it "
      "pushes into the canopy, so a room has to move well over 1 m/s at the fans before the buried lower "
      "and interior leaves feel the gentle breeze Figure 3 asks for. Roughly 200 FPM delivered is about "
      "what it takes to land <em>every</em> leaf in the sweet spot, not just the ones on the outside."),
    p("Above that threshold, the higher-airflow rooms showed three things:"),
    ul([
      "<strong>More sellable flower.</strong> Stems carried less biomass and more of the plant's energy "
      "went into bud. Trim ran about 42% in the still-air plants and was significantly lower with good "
      "airflow, so less of the harvest ended up as larf" + _c("pipp2026-airflow") + ".",
      "<strong>Less stress.</strong> Still-air plants had redder stems and more anthocyanin, a visible "
      "stress marker; the well-aired plants looked more uniform and less stressed.",
      "<strong>Taller, not weaker.</strong> Higher-airflow plants finished roughly 6 inches taller than "
      "the still-air controls, with most vertical growth done by the end of week three, while still "
      "putting <em>less</em> into stem. Here the extra height is relief from still-air stress, not the "
      "mechanical dwarfing you would get under a harder, direct wind (see section 06).",
    ]),
    callout("key", "Uniformity is the real lesson",
      p("Even in a tightly engineered room, the crew saw a positional bias: the first 1–2 feet of each "
        "row behaved differently from the rest. Their takeaway is the one to keep, "
        "<strong>&ldquo;if airflow isn&rsquo;t uniform, neither is your crop.&rdquo;</strong> That is the "
        "dead-zone problem from section 07, now measured. Making sure no leaf is left in still air beats "
        "chasing a high average fan speed.")),
    callout("note", "How solid is this?",
      p("Treat it as strong early field evidence, not settled science: the results so far are one "
        "replicate, with a second run underway to firm up the statistics" + _c("pipp2026-airflow") +
        ". The direction lines up cleanly with the leaf physiology in the rest of this paper.")),
  ]})

SECTIONS.append({"id": "fan-types", "kicker": "10 · The hardware", "title": "Fan types",
  "blocks": [
    lead("Fans are not interchangeable. Each type makes a different <em>shape</em> of air, and the "
         "shape decides which leaves get served. Pick by the shape you need, not by the price tag "
         "or the CFM on the box."),
    _fan_photos(),
    figure(_fig_fan_gallery(), 5,
      "The eight types you will actually meet, drawn side-on with the air each one makes. The first six "
      "are recirculation kit; the air sock is a delivery method; the inline duct fan is exchange, not "
      "circulation at all."),
    grid([
      card("HAF, horizontal airflow fan",
        p("A hanging basket fan, typically a 300&ndash;500&nbsp;mm (12&ndash;20&nbsp;inch) blade on a "
          "small 1/10&ndash;1/15&nbsp;hp motor, hung above head height and aimed sideways down the "
          "room" + _c("bartok-haf") + ". Several of them together drive one slow <strong>racetrack "
          "loop</strong>: air runs down one side of the room and back the other. Its jet drags "
          "surrounding still air along with it (entrainment), so a modest fan stirs a large volume."
          "<br><br><strong>Where:</strong> above the canopy, a quarter of the room width in from the "
          "wall. <strong>The catch:</strong> its air runs <em>over</em> the top of the crop. In a dense "
          "canopy it never reaches the middle."), tag="Recirculation · the backbone"),
      card("VAF, vertical airflow fan",
        p("Hangs above the canopy and blows <strong>straight down through it</strong>, usually with a "
          "flared diffuser on top so it draws air from a wide area and delivers a broad column rather "
          "than a narrow jet. This is the one type that reliably reaches leaves buried inside a plant."
          "<br><br><strong>Where:</strong> over the canopy on a grid, spacing set so the down-columns "
          "overlap. <strong>The catch:</strong> more expensive per unit, and it casts shade, so mind "
          "where you hang it relative to the lights."), tag="Recirculation · canopy penetration"),
      card("Oscillating wall or pole fan",
        p("The classic grow-room fan: a head on a bracket that sweeps an arc. Cheap, everywhere, and "
          "genuinely good in a small room, because the sweep gives you the varied, turbulent air "
          "section 08 asks for."
          "<br><br><strong>Where:</strong> wall or pole mounted, aimed to <em>mix</em> the room, never "
          "pointed straight at plants. <strong>The catch:</strong> it time-shares. Each leaf only gets "
          "air for part of each sweep, so at scale you need a lot of them to hold a constant breeze."),
        tag="Recirculation · small-room default"),
      card("Clip fan",
        p("A miniature oscillating fan on a clamp, gripping a tent pole or frame. Moves roughly one "
          "plant's worth of air."
          "<br><br><strong>Where:</strong> tents and single-plant setups only. <strong>The catch:</strong> "
          "nothing about it scales. If you are running more than about 2&nbsp;m&sup2; of canopy, clip "
          "fans are a false economy: you end up with six of them doing the job of one proper hanging "
          "fan, at higher total wattage and worse uniformity."), tag="Recirculation · tent scale"),
      card("Drum / pedestal floor fan",
        p("A large, powerful head on a stand. Very high thrust, a narrow jet, and a lot of noise. "
          "This is a blunt instrument."
          "<br><br><strong>Where:</strong> temporarily, to break a specific dead corner or dry a room "
          "down fast after a spill. <strong>The catch:</strong> it is the single most common cause of "
          "wind-burn. Plants directly in front get a gale and everything off-axis gets nothing. Do not "
          "build a room's airflow on these."), tag="Recirculation · spot-fix only"),
      card("Under-canopy fan",
        p("A low, flat, wide fan that sits at pot level and blows across the floor and up into the "
          "bottom of the plants. The zone it serves is the wettest and stillest in the room: cool air "
          "sinks, pots and floors evaporate into it, and no overhead fan reaches it."
          "<br><br><strong>Where:</strong> at floor or bench level, blowing along the rows. "
          "<strong>The catch:</strong> almost none, which is why it is such good value. Just keep it "
          "out of the way of irrigation lines and keep the intake clear of leaf litter."),
        tag="Recirculation · the wet zone"),
      card("Air sock / perforated poly tube",
        p("A long fabric or polythene tube, fed by a fan or an air handler, that leaks air through "
          "hundreds of small holes along its whole length. Because the holes are small and numerous, "
          "delivery is remarkably even and there is no single blast anywhere. Research design targets "
          "sit around 6&ndash;10&nbsp;mm holes at 30&ndash;70&nbsp;mm spacing, with the fan holding "
          "roughly 30&ndash;40&nbsp;Pa of static pressure so the tube stays inflated and round" +
          _c("perfduct2025") + "."
          "<br><br><strong>Where:</strong> running the length of a row, over or under the bench. It is "
          "the standard way to deliver <em>conditioned</em> air from an AC or dehumidifier without "
          "creating a draught in one corner and a dead zone in the other. <strong>The catch:</strong> "
          "you have to design it (tube diameter, hole size, hole spacing) and it needs a fan that can "
          "actually make the pressure."), tag="Delivery · conditioned air"),
      card("Inline duct fan",
        p("A fan inside a length of ducting. This is an <strong>exchange</strong> device, not a "
          "circulation device: it pulls air out of the room, usually through a carbon filter, and dumps "
          "it outside. It is what controls humidity and refreshes CO2 in a vented room."
          "<br><br><strong>Where:</strong> ducted to a high point in the room (hot, humid air rises), "
          "with a passive or active intake low down. <strong>The catch:</strong> people count it as "
          "their airflow. It is not. A room with a big extractor and no circulation fans still has a "
          "still, humid canopy."), tag="Exchange · not circulation"),
    ], cols=2),
    p("Three more you will meet in bigger rooms, listed here so you can place them correctly rather "
      "than mistake them for canopy airflow:"),
    grid([
      card("HVLS / destratification fan",
        p("A large, very slow ceiling fan. Its job is to break the warm layer that collects near the "
          "ceiling under lights and push it back down. Useful in tall rooms; pointless under a 2.4&nbsp;m "
          "ceiling."), tag="Recirculation · tall rooms"),
      card("Wall / shutter exhaust fan",
        p("Bulk air exchange for greenhouses and large rooms, with gravity or motorised shutters. Same "
          "class as the inline duct fan, just much bigger. Sealed rooms usually do not have one."),
        tag="Exchange · bulk"),
      card("AHU / HVAC supply",
        p("The air-handling unit that actually heats, cools and dries. It sets your VPD. It still needs "
          "a distribution method, typically ducting into socks, to get that treated air "
          "evenly across a canopy."), tag="Conditioning"),
    ], cols=3),
    card("In-rack airflow systems (vertical farms)",
      p("If you grow on multi-tier racking, none of the above works on its own: each tier is a low, "
        "enclosed slot that overhead fans physically cannot reach. Purpose-built systems mount a "
        "ducted fan bar into the racking itself and push air along or down through every tier" +
        _c("vas-inrack") + ". On racking it is the only thing that works, and "
        "it is the setup the Pipp trial in section 09 was built to test."), tag="Recirculation · vertical racking"),
  ]})

SECTIONS.append({"id": "ranking", "kicker": "11 · The ranking", "title": "Selecting fans for canopy airflow",
  "blocks": [
    p("A ranking is only honest if you say what it is ranking <em>for</em>. This one scores "
      "<strong>crop-relevant airflow bought per dollar installed, in a sealed, single-tier indoor "
      "flower room</strong> of roughly 20&ndash;200&nbsp;m&sup2; of canopy. Change the room and the "
      "order changes; the callout below says how."),
    figure(L.hbars("Value per dollar: sealed single-tier indoor flower room",
            [("HAF fan (hanging)", 95), ("Under-canopy fan", 84), ("VAF fan (top-down)", 80),
             ("Oscillating wall fan", 68), ("Air sock off the AHU", 62),
             ("HVLS / destratification", 44), ("Drum / pedestal fan", 30), ("Clip fan", 22)],
            note="Relative score, not a measurement. Judged on airflow delivered to leaves per dollar and per watt."), 6,
      "The backbone is cheap and the glamour is not. The two lowest-ranked fans are the two "
      "most first-time growers actually buy."),
    table(["#", "Fan type", "What it buys you", "Reach into the canopy", "Verdict"], [
      ["1", "<strong>HAF fan</strong>", "A room-wide loop, running 24/7 on very few watts",
       "Over the top only", "<strong>Build the room on these.</strong> Cheapest uniformity you can buy" + _c("bartok-haf")],
      ["2", "<strong>Under-canopy fan</strong>", "Kills the wettest, stillest zone in the room",
       "Bottom of the plant", "<strong>Best value add-on.</strong> Targets exactly where bud rot starts"],
      ["3", "<strong>VAF fan</strong>", "Air driven down into the middle of the plant",
       "Full depth. The only one that gets there", "<strong>Buy once density rises.</strong> Peer-reviewed for interior-leaf calcium" + _c("goto1992-tipburn") + _c("moosavi2025-vaf")],
      ["4", "Oscillating wall fan", "Cheap, varied, turbulent air", "Over and around, in bursts",
       "Fine as the backbone below ~20&nbsp;m&sup2;. Falls behind above it"],
      ["5", "Air sock off the AHU", "Even delivery of <em>conditioned</em> air, no draughts",
       "Along the row, gentle", "Excellent, but it is capex plus design work" + _c("perfduct2025")],
      ["6", "HVLS / destratification", "Breaks the hot layer under the ceiling", "Bulk mixing only",
       "Only pays in tall rooms. Wasted under a low ceiling"],
      ["7", "Drum / pedestal fan", "Raw thrust into one spot", "A gale on-axis, nothing off it",
       "Spot-fix only. Leading cause of wind-burn"],
      ["8", "Clip fan", "One plant's worth of air", "One plant",
       "Tents only. Six of these lose to one hanging fan"],
    ], cls="compact",
      foot="Ranked on value per dollar for a sealed, single-tier indoor flower room. Exchange kit "
           "(inline duct and wall fans) is deliberately absent: it is mandatory, but it does a "
           "different job and cannot be traded against a circulation fan."),
    callout("key", "When the ranking flips",
      ul([
        "<strong>Vertical racking:</strong> in-rack systems move to #1 outright and HAF drops off the "
        "list. Overhead fans cannot physically reach inside a tier" + _c("vas-inrack") + ".",
        "<strong>Dense, un-defoliated canopies:</strong> VAF overtakes HAF. Top-down airflow is "
        "measurably better than horizontal for getting air, and therefore calcium, into inner "
        "leaves" + _c("goto1992-tipburn") + _c("ahmed2020-multifan") + ". In greenhouse lettuce, vertical "
        "fans cut tip-burn ratings from 5.0 to under 0.1 and burnt leaves from 39% to under 7%" +
        _c("moosavi2025-vaf") + ".",
        "<strong>Tents and single-plant grows:</strong> the whole table collapses to a clip fan or two "
        "plus the extractor, and that is genuinely the right answer at that scale.",
        "<strong>Greenhouses:</strong> HAF stays #1 and the air sock rises, because you are also "
        "distributing heat" + _c("uconn-haf") + ".",
      ], "tight")),
    callout("warn", "The mistake the ranking is really about",
      p("Almost every underperforming room has the same shape of problem: <strong>plenty of total "
        "CFM, badly distributed</strong>. Two drum fans in the corners produce an impressive number on "
        "paper and a still, humid middle. Six small hanging fans on a loop produce a smaller number "
        "and a room where every leaf moves. Buy the pattern, not the peak.")),
  ]})

SECTIONS.append({"id": "placement", "kicker": "12 · Placement", "title": "Fan placement",
  "blocks": [
    p("Fan placement is a pattern problem, not a coverage problem. You are not trying to hit every "
      "plant with a jet; you are trying to set the whole volume of air in the room turning slowly and "
      "consistently, then punch that moving air down into the canopy."),
    figure(_fig_haf_loop(), 7,
      "The horizontal loop, from above. Fans do not each cover a patch. They hand air to each other "
      "around a circuit. First fan roughly 3&ndash;4.5&nbsp;m (10&ndash;15&nbsp;ft) off the end wall, then "
      "12&ndash;15&nbsp;m (40&ndash;50&nbsp;ft) apart, about a quarter of the room width in from the "
      "side" + _c("bartok-haf") + _c("uconn-haf") + "."),
    p("Then cut the room the other way. Most rooms buy airflow for the top of the canopy only, and "
      "that is exactly why rot starts at the bottom and in the middle:"),
    figure(_fig_zones(), 8,
      "The same room in section. Three heights, three different jobs, three different fans. If you only "
      "own HAF fans you own the top band, and the two bands where disease actually starts are unserved."),
    steps([
      ("Set the loop first",
       "Pick a direction and commit. Hang HAF fans so that air runs down one side of the room and "
       "back the other, each fan feeding the next. Never point two fans at each other. You will "
       "cancel the loop and create a dead spot exactly where they meet" + _c("bartok-haf") + "."),
      ("Get the height right",
       "Above head height, roughly 2.1&ndash;2.4&nbsp;m (7&ndash;8&nbsp;ft) off the floor for a "
       "floor-grown crop, so the jet clears the canopy rather than ploughing into it" + _c("uconn-haf") +
       ". Where there are hanging baskets or a light rack in the way, go a clear distance above or "
       "below, not level with them."),
      ("Punch down into the canopy",
       "Add top-down fans over the crop on a grid, spaced so their down-columns overlap. This is the "
       "step almost everyone skips, and it is the one that reaches the interior leaves" +
       _c("goto1992-tipburn") + "."),
      ("Serve the floor",
       "Put low fans at pot level blowing along the rows. Cold, wet air pools down there and no "
       "overhead fan will move it."),
      ("Aim to mix, never to blast",
       "Angle fans slightly off-parallel and let oscillation vary the direction. You want a room full "
       "of slow, turbulent, mixing air, not a set of jets" + _c("schuepp1993-bl") + "."),
      ("Walk it and correct",
       "Run the flutter test at all three heights: over the tops, hand pushed into the middle of a "
       "plant, and down at pot level. Whichever height fails is the fan you are missing. A cheap "
       "anemometer, or a length of flagging tape taped to a cane, turns this from a guess into a "
       "reading."),
    ]),
    callout("tip", "Run them all the time",
      p("Circulation fans should run <strong>24 hours a day</strong>, lights on and lights off. The "
        "extension guidance is to run them continuously except when exhaust fans are running or vents "
        "are open, because that is when the room is being flushed anyway" + _c("bartok-haf") + ". "
        "Lights-off is when leaf temperature drops toward dew point and condensation forms, "
        "precisely when you least want still air" + _c("uconn-haf") + ".")),
  ]})

SECTIONS.append({"id": "sizing", "kicker": "13 · The numbers", "title": "Sizing the system",
  "blocks": [
    p("The greenhouse industry has been sizing horizontal airflow for decades and the rules of thumb "
      "transfer well to an indoor room. Start here, then measure and adjust:"),
    table(["What", "Rule of thumb", "Where it comes from"], [
      ["Total circulation capacity",
       "<strong>2 CFM per ft&sup2; of floor</strong> (&asymp; 36.6 m&sup3;/h per m&sup2;). A 30&nbsp;&times;&nbsp;100&nbsp;ft house needs ~6,000 CFM total.",
       "Bartok &amp; Grubinger, UConn/UVM Extension" + _c("bartok-haf")],
      ["First fan position", "3&ndash;4.5&nbsp;m (10&ndash;15&nbsp;ft) in from the end wall, to catch air coming round the corner.",
       "UConn IPM" + _c("uconn-haf")],
      ["Fan spacing", "12&ndash;15&nbsp;m (40&ndash;50&nbsp;ft) apart along the loop. Scale down proportionally in a small room.",
       "Bartok &amp; Grubinger" + _c("bartok-haf")],
      ["Horizontal position", "About &frac14; of the room width in from the side wall (or centre of the bay).",
       "UConn IPM" + _c("uconn-haf")],
      ["Mounting height", "Above head height; ~2.1&ndash;2.4&nbsp;m (7&ndash;8&nbsp;ft) for floor crops. Clear of baskets and light racks.",
       "Bartok &amp; Grubinger" + _c("bartok-haf")],
      ["Individual fan size", "300&ndash;500&nbsp;mm (12&ndash;20&nbsp;in) blade, 1/10&ndash;1/15&nbsp;hp. Many small beats few large.",
       "Bartok &amp; Grubinger" + _c("bartok-haf")],
      ["Greenhouse velocity target", "50&ndash;100 FPM (0.25&ndash;0.5 m/s) of general room movement.",
       "UConn IPM" + _c("uconn-haf")],
      ["Cannabis flower-room target", "~200 FPM (&asymp;1.0 m/s) <em>delivered</em>, to land every leaf in the sweet spot.",
       "Pipp / Justice trial" + _c("pipp2026-airflow")],
      ["Run time", "24/7, except while exhaust fans run or vents are open.",
       "Bartok &amp; Grubinger" + _c("bartok-haf")],
      ["Air sock design", "6&ndash;10&nbsp;mm holes, 30&ndash;70&nbsp;mm spacing, ~30&ndash;40&nbsp;Pa static to hold the tube round.",
       "Perforated-duct CFD study" + _c("perfduct2025")],
    ], cls="compact"),
    callout("note", "Why the two velocity targets disagree",
      p("The greenhouse standard (50&ndash;100 FPM) and the cannabis figure (~200 FPM) are not in "
        "conflict; they were set for different goals. The greenhouse number is aimed at temperature "
        "uniformity and stopping condensation on leaves overnight in a relatively open, lower-light "
        "crop" + _c("uconn-haf") + ". The cannabis number comes from a dense, high-light flower canopy "
        "where the goal is driving air <em>into</em> the plant" + _c("pipp2026-airflow") + ". Denser "
        "canopy and brighter light both push the number up. Use the greenhouse rules for the layout "
        "and the cannabis number for the target.")),
    p("One last number, and it is the one that saves the most money. Fan airflow rises in step with "
      "speed, but shaft power rises with the <strong>cube</strong> of speed" + _c("amca-fanlaws") + ". "
      "Halving a fan's speed drops it to roughly one-eighth of the power. That has a direct design "
      "consequence:"),
    callout("key", "More fans, slower, always wins",
      p("Two fans at full speed and eight fans at half speed can move similar air, but the eight fans "
        "draw around a quarter of the power <em>and</em> give far better coverage, because the air "
        "arrives from more directions with fewer dead spots. This is why speed-controllable EC-motor "
        "fans are worth the premium over fixed-speed AC fans: an AC fan is effectively on or off, so "
        "to reduce airflow you have to switch fans off, which punches holes in your coverage exactly "
        "where the fan you killed used to be.")),
  ]})

SECTIONS.append({"id": "trouble", "kicker": "14 · When it goes wrong", "title": "Troubleshooting",
  "blocks": [
    table(["Symptom", "Likely cause", "What to do"], [
      ["Bud rot starting deep in colas", "Dead-zone: air not reaching the canopy interior", "Add top-down (VAF) airflow, defoliate, lower RH"],
      ["Tops flutter, middle and bottom dead still", "All your airflow is above the canopy (HAF only)", "Add VAF over the crop and under-canopy fans at pot level"],
      ["Rot and mildew starting at the bottom", "The floor zone is the wettest, stillest air in the room", "Under-canopy fans blowing along the rows"],
      ["Leaf-tip burn despite full tank", "Airflow outran nutrient delivery (calcium)", "Raise feed/EC to match transpiration"],
      ["Tip-burn only on new inner growth", "Inner leaves too still to transpire, so no calcium arrives", "Get air into the canopy interior, not just over it"],
      ["Leaves clawing / wind-burnt edges", "Air velocity too high / fan pointed at plants", "Reduce speed, aim fans to mix, not blast"],
      ["One end of a row always behaves differently", "Broken loop: fans spaced too far apart or facing each other", "Re-set the racetrack; never point two fans head-on"],
      ["Big fans, loud room, still stratified", "Too few fans running flat out", "More fans at lower speed. Power rises with the cube of speed"],
      ["Tall, weak, floppy stems", "Too little air movement: no mechanical signal", "Add gentle constant breeze across the canopy"],
      ["Room humidity stuck high", "Recirculation OK but not enough air exchange", "Increase intake/exhaust / dehumidification"],
      ["Cold or dry patch under the AC outlet", "Conditioned air dumped in one spot instead of distributed", "Duct it into an air sock along the row"],
    ], cls="compact"),
  ]})

SECTIONS.append({"id": "expect", "kicker": "15 · Straight talk", "title": "Expected results and limitations",
  "blocks": [
    callout("key", "What to remember",
      ol(["Airflow's job is to <strong>thin the boundary layer</strong> on every leaf.",
          "Aim for a <strong>gentle, turbulent breeze (~0.3–1.0 m/s)</strong> everywhere, including inside the plants.",
          "Buy the <strong>pattern, not the peak</strong>: many small fans on a loop beat two big ones in the corners.",
          "Serve <strong>all three heights</strong>, above, through and below the canopy. Only the first is easy.",
          "More air = more thirst: <strong>feed and humidity must keep up</strong>" + _c("gilliham2011-ca") + ".",
          "Most benefit comes early. You do not need a wind tunnel" + _c("kitaya2004-airvel") + "."])),
    p("Airflow is one subsystem of the room. Read it alongside the "
      "<a href='grow-room-systems.html'>systems guide</a> and the "
      "<a href='mould-risk.html'>mould risk</a> paper."),
  ]})
