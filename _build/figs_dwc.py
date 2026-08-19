# -*- coding: utf-8 -*-
"""Bespoke inline-SVG cross-sections and illustrations for the deep-water-culture paper.

Every colour is a CSS custom property from the theme palette, so these render correctly
in both light and dark mode without a filter hack.
"""
from figs import (G, GD, GL, GXL, INK, INK2, MUT, LINE, AMB, AMBL, RED, REDL,
                  BLU, BLUL, PUR, PURL, PAPER, PANEL2, FS, MN)


def _svg(w, h, label, parts):
    return (f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
            f'xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{label}">'
            f'<rect width="{w}" height="{h}" fill="{PAPER}"/>' + "".join(parts) + "</svg>")


def _t(x, y, s, fill=INK, size=11, weight=None, anchor="start", font=FS, style=""):
    w = f' font-weight="{weight}"' if weight else ""
    return (f'<text x="{x}" y="{y}" text-anchor="{anchor}" fill="{fill}" font-size="{size}"'
            f'{w} style="{font};{style}">{s}</text>')


def _title(t, note=""):
    out = [_t(24, 26, t, INK, 15, 700)]
    if note:
        out.append(_t(24, 45, note, MUT, 11.5))
    return out


def _lead(x1, y1, x2, y2, col=MUT):
    return (f'<path d="M{x1},{y1} L{x2},{y2}" stroke="{col}" stroke-width="1" '
            f'stroke-dasharray="2 3"/><circle cx="{x1}" cy="{y1}" r="2.2" fill="{col}"/>')


# ---------------------------------------------------------------- 1. bucket cross-section
def bucket_xsection():
    W, H = 760, 540
    p = _title("Cross-section of one RDWC site",
               "Note the two volumes that are not the same number.")
    bx, bw, bt, bb = 210, 250, 92, 452          # bucket box
    water_y, bulk_y = 150, 392                  # waterline, bulkhead centre

    # bucket wall
    p.append(f'<path d="M{bx},{bt} L{bx+8},{bb} L{bx+bw-8},{bb} L{bx+bw},{bt}" '
             f'fill="{PANEL2}" stroke="{INK2}" stroke-width="2.5" stroke-linejoin="round"/>')
    # solution
    p.append(f'<path d="M{bx+2.2},{water_y} L{bx+8},{bb-2} L{bx+bw-8},{bb-2} L{bx+bw-2.2},{water_y} Z" '
             f'fill="{BLUL}" opacity=".75"/>')
    # leftover volume (below bulkhead) shaded differently
    p.append(f'<path d="M{bx+5.6},{bulk_y} L{bx+8},{bb-2} L{bx+bw-8},{bb-2} L{bx+bw-5.6},{bulk_y} Z" '
             f'fill="{AMBL}" opacity=".85"/>')
    p.append(f'<line x1="{bx+5.6}" y1="{bulk_y}" x2="{bx+bw-5.6}" y2="{bulk_y}" '
             f'stroke="{AMB}" stroke-width="1.4" stroke-dasharray="5 3"/>')
    # waterline
    p.append(f'<line x1="{bx+2.2}" y1="{water_y}" x2="{bx+bw-2.2}" y2="{water_y}" '
             f'stroke="{BLU}" stroke-width="2"/>')

    # lid / planting deck
    p.append(f'<rect x="{bx-14}" y="{bt-16}" width="{bw+28}" height="16" rx="3" '
             f'fill="{INK2}" opacity=".92"/>')
    p.append(f'<rect x="{bx+86}" y="{bt-16}" width="78" height="16" fill="{PAPER}"/>')

    # net pot + clay
    npx, npw = bx + 86, 78
    p.append(f'<path d="M{npx},{bt-16} L{npx+9},{bt+52} L{npx+npw-9},{bt+52} L{npx+npw},{bt-16}" '
             f'fill="none" stroke="{INK}" stroke-width="2"/>')
    for i, (cx, cy, r) in enumerate([(npx+20,bt-2,7),(npx+38,bt-5,8),(npx+57,bt-1,7),
                                     (npx+27,bt+14,8),(npx+48,bt+15,7),(npx+38,bt+31,7),
                                     (npx+22,bt+30,5),(npx+55,bt+29,5)]):
        p.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{AMB}" opacity=".55" stroke="{AMB}" stroke-width="0.8"/>')

    # stem above the waterline
    p.append(f'<path d="M{npx+39},{bt-14} L{npx+39},{bt-46}" stroke="{GD}" stroke-width="3.5" stroke-linecap="round"/>')
    p.append(f'<path d="M{npx+39},{bt-38} q-20,-9 -27,-2 q12,9 27,2z" fill="{G}" opacity=".85"/>')
    p.append(f'<path d="M{npx+39},{bt-32} q20,-9 27,-2 q-12,9 -27,2z" fill="{G}" opacity=".85"/>')

    # root mass
    import math
    for i in range(17):
        x0 = npx + 12 + i * 3.4
        sway = 16 * math.sin(i * 0.8)
        p.append(f'<path d="M{x0:.0f},{bt+50} C{x0-8+sway:.0f},{bt+130} {x0+10+sway:.0f},{bt+200} '
                 f'{x0-4+sway*1.4:.0f},{bt+268}" fill="none" stroke="{PAPER}" stroke-width="3.4" opacity=".55"/>')
        p.append(f'<path d="M{x0:.0f},{bt+50} C{x0-8+sway:.0f},{bt+130} {x0+10+sway:.0f},{bt+200} '
                 f'{x0-4+sway*1.4:.0f},{bt+268}" fill="none" stroke="{INK2}" stroke-width="1.5" opacity=".62"/>')

    # air stone, offset from wall, at the bottom
    asx = bx + 30
    p.append(f'<rect x="{asx}" y="{bb-24}" width="34" height="15" rx="7" fill="{INK2}"/>')
    p.append(f'<line x1="{asx+34}" y1="{bb-17}" x2="{bx+bw-14}" y2="{bb-17}" stroke="{INK2}" stroke-width="2"/>')
    for i, (dx, dy, r) in enumerate([(-6,-34,3.2),(9,-46,3.8),(-14,-74,2.8),(4,-88,4.2),
                                     (18,-104,3.0),(-10,-124,3.6),(7,-146,3.2),(22,-160,3.8),
                                     (-4,-186,3.0),(13,-206,3.6),(27,-224,3.2),(2,-244,3.8),
                                     (19,-266,3.0),(-8,-282,3.4)]):
        p.append(f'<circle cx="{asx+17+dx}" cy="{bb-24+dy}" r="{r}" fill="{PAPER}" '
                 f'stroke="{BLU}" stroke-width="1.3" opacity=".92"/>')

    # bulkhead + recirc line
    p.append(f'<rect x="{bx+bw-8}" y="{bulk_y-9}" width="26" height="18" rx="3" fill="{INK2}"/>')
    p.append(f'<line x1="{bx+bw+18}" y1="{bulk_y}" x2="{W-34}" y2="{bulk_y}" stroke="{INK2}" stroke-width="4"/>')
    p.append(f'<path d="M{W-52},{bulk_y-6} L{W-38},{bulk_y} L{W-52},{bulk_y+6}Z" fill="{INK2}"/>')

    # volume brackets on the left
    def bracket(x, y1, y2, col):
        return (f'<path d="M{x+7},{y1} L{x},{y1} L{x},{y2} L{x+7},{y2}" fill="none" '
                f'stroke="{col}" stroke-width="1.6"/>')
    p.append(bracket(150, water_y, bb - 2, BLU))
    p.append(bracket(112, bulk_y, bb - 2, AMB))
    p.append(_t(146, water_y + 52, "operating", BLU, 11, 700, "end"))
    p.append(_t(146, water_y + 66, "volume", BLU, 11, 700, "end"))
    p.append(_t(146, water_y + 82, "~40 L in a", MUT, 9.8, None, "end"))
    p.append(_t(146, water_y + 94, "49 L module", MUT, 9.8, None, "end"))
    p.append(_t(108, bulk_y + 34, "left-over", AMB, 11, 700, "end"))
    p.append(_t(108, bulk_y + 48, "~11 L", AMB, 10, None, "end"))
    p.append(_t(108, bulk_y + 61, "stays put", MUT, 9.5, None, "end"))

    # right-hand labels
    labels = [
        (bt - 40, "Basal stem stays ABOVE the water", GD),
        (bt - 4, "Net pot + expanded clay", INK2),
        (water_y - 8, "Waterline just under the deck", BLU),
        (bt + 150, "Root mass in free solution", INK2),
        (bulk_y - 16, "Bulkhead + recirculating line", INK2),
        (bb - 18, "Air stone: bottom, off the wall,", INK2),
    ]
    lx = bx + bw + 26
    for y, s, col in labels:
        p.append(_t(lx, y, s, col, 11, 700 if col != INK2 else None))
    p.append(_t(lx, bb - 5, "never under the net pot", RED, 11, 700))
    p.append(_lead(bx + bw - 4, bt - 44, lx - 8, bt - 44))
    p.append(_lead(bx + bw - 20, water_y, lx - 8, water_y - 12))
    p.append(_lead(bx + bw - 30, bt + 146, lx - 8, bt + 146))
    p.append(_lead(bx + bw + 20, bulk_y, lx - 8, bulk_y - 20))
    p.append(_t(24, H - 14, "A ‘full’ change-out drains only to the bulkhead, so it replaces about 71% of the water — not all of it.",
                MUT, 11))
    return _svg(W, H, "Cross-section of one RDWC bucket", p)


# ---------------------------------------------------------------- 2. root boundary layer
def boundary_layer():
    W, H = 760, 400
    p = _title("The root boundary layer, and what bubbling does to it",
               "The same root, the same solution. Only the water movement differs.")
    for k, (cx, ok) in enumerate([(206, True), (554, False)]):
        cy = 232
        col = G if ok else RED
        band = GL if ok else REDL
        p.append(f'<rect x="{cx-166}" y="86" width="332" height="256" rx="12" '
                 f'fill="{PANEL2}" stroke="{LINE}"/>')
        p.append(_t(cx, 110, "Gentle flow: layer intact" if ok else "Agitated: layer stripped",
                    col, 12.5, 700, "middle"))
        # bulk solution stipple
        for i in range(26):
            import math
            ang = i * 0.9
            rx = cx + (78 + (i % 5) * 15) * math.cos(ang)
            ry = cy + (56 + (i % 4) * 11) * math.sin(ang)
            p.append(f'<circle cx="{rx:.0f}" cy="{ry:.0f}" r="1.9" fill="{MUT}" opacity=".5"/>')
        # boundary layer
        if ok:
            p.append(f'<ellipse cx="{cx}" cy="{cy}" rx="72" ry="60" fill="{col}" opacity=".20"/>')
            p.append(f'<ellipse cx="{cx}" cy="{cy}" rx="72" ry="60" fill="none" stroke="{col}" '
                     f'stroke-width="1.8" stroke-dasharray="5 3"/>')
        else:
            for a in (0, 1, 2, 3, 4, 5):
                import math
                th = a * 1.05
                p.append(f'<path d="M{cx+40*math.cos(th):.0f},{cy+34*math.sin(th):.0f} '
                         f'l{26*math.cos(th):.0f},{22*math.sin(th):.0f}" stroke="{col}" '
                         f'stroke-width="1.3" stroke-dasharray="3 4" opacity=".8"/>')
            p.append(f'<ellipse cx="{cx}" cy="{cy}" rx="44" ry="37" fill="{band}" opacity=".45"/>')
        # the root itself
        p.append(f'<ellipse cx="{cx}" cy="{cy}" rx="30" ry="25" fill="{PAPER}" stroke="{INK}" stroke-width="2"/>')
        p.append(_t(cx, cy + 4, "root", INK, 11, 700, "middle"))
        # chemistry markers inside the layer
        marks = [("H+", -50, -26), ("H+", 44, -30), ("Fe", -48, 30), ("Fe", 46, 26)]
        for s, dx, dy in marks:
            p.append(_t(cx + dx, cy + dy, s, col if ok else MUT, 10.5, 700, "middle", MN,
                        "" if ok else "opacity:.45"))
        # turbulence arrows on the right panel
        if not ok:
            for dy in (-96, -60, 58):
                p.append(f'<path d="M{cx-142},{cy+dy} q32,-11 64,0 q32,11 64,0 q32,-11 64,0 q32,11 64,0" '
                         f'fill="none" stroke="{col}" stroke-width="1.9" opacity=".8"/>')
                p.append(f'<path d="M{cx+108},{cy+dy-5} l8,5 l-8,5" fill="none" stroke="{col}" '
                         f'stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/>')
        p.append(_t(cx, 322,
                    "Acidified, reduced, iron available" if ok else "Bulk pH, bulk chemistry, iron unavailable",
                    INK2, 10.8, None, "middle"))
    p.append(_t(24, H - 14,
                "The root builds this layer to feed itself. Aeration does not just add oxygen — past a point it demolishes the machinery.",
                MUT, 11))
    return _svg(W, H, "Root boundary layer intact versus stripped by agitation", p)


# ---------------------------------------------------------------- 3. air stone placement
def airstone_placement():
    W, H = 760, 372
    p = _title("Air stone placement: same air volume, opposite outcome")
    import math
    for cx, ok in ((206, False), (554, True)):
        col = RED if not ok else G
        bx, bw, bt, bb = cx - 96, 192, 96, 320
        p.append(f'<path d="M{bx},{bt} L{bx+7},{bb} L{bx+bw-7},{bb} L{bx+bw},{bt}" '
                 f'fill="{PANEL2}" stroke="{INK2}" stroke-width="2.2" stroke-linejoin="round"/>')
        p.append(f'<path d="M{bx+1.6},{bt+22} L{bx+7},{bb-2} L{bx+bw-7},{bb-2} L{bx+bw-1.6},{bt+22} Z" '
                 f'fill="{BLUL}" opacity=".7"/>')
        p.append(f'<rect x="{bx-8}" y="{bt-13}" width="{bw+16}" height="13" rx="2.5" fill="{INK2}"/>')
        p.append(f'<rect x="{cx-30}" y="{bt-13}" width="60" height="13" fill="{PAPER}"/>')
        p.append(f'<path d="M{cx-30},{bt-13} L{cx-24},{bt+30} L{cx+24},{bt+30} L{cx+30},{bt-13}" '
                 f'fill="none" stroke="{INK}" stroke-width="1.8"/>')
        # roots
        for i in range(11):
            x0 = cx - 26 + i * 5.2
            sway = 11 * math.sin(i * 0.9)
            p.append(f'<path d="M{x0:.0f},{bt+30} C{x0-6+sway:.0f},{bt+95} {x0+8+sway:.0f},{bt+150} '
                     f'{x0-3+sway:.0f},{bt+198}" fill="none" stroke="{PAPER}" stroke-width="2.4"/>')
        # stone + plume
        sx = cx - 17 if not ok else bx + 22
        p.append(f'<rect x="{sx}" y="{bb-20}" width="30" height="13" rx="6" fill="{INK2}"/>')
        for j, (dy, r) in enumerate([(-30, 3.2), (-58, 4), (-88, 3), (-118, 3.8), (-150, 3.2), (-180, 4)]):
            jx = sx + 15 + (6 * math.sin(j * 1.3) if ok else 3 * math.sin(j * 1.3))
            p.append(f'<circle cx="{jx:.0f}" cy="{bb-20+dy}" r="{r}" fill="{PAPER}" stroke="{col}" stroke-width="1.3"/>')
        p.append(f'<rect x="{cx-96}" y="{H-46}" width="192" height="28" rx="6" '
                 f'fill="{REDL if not ok else GL}" opacity=".8"/>')
        p.append(_t(cx, H - 27,
                    "✗  Under the net pot" if not ok else "✓  Bottom, ~2.5 cm off the wall",
                    INK, 11.5, 700, "middle"))
        p.append(_t(cx, bt + 198,
                    "Plume shears through the" if not ok else "Plume rises past the root",
                    INK2, 10.4, None, "middle"))
        p.append(_t(cx, bt + 211,
                    "youngest root tips" if not ok else "mass, not through it",
                    INK2, 10.4, None, "middle"))
    return _svg(W, H, "Correct and incorrect air stone placement in a DWC bucket", p)


# ---------------------------------------------------------------- 4. system schematic
def system_schematic():
    W, H = 760, 400
    p = _title("The RDWC loop: every control lives in the plant-free bucket",
               "Plant sites are dumb. Measurement, dosing, heating and top-off all happen in one place.")
    # plant sites
    sx, sy = 300, 96
    for i in range(3):
        x = sx + i * 132
        p.append(f'<rect x="{x}" y="{sy}" width="104" height="76" rx="9" fill="{GXL}" stroke="{G}" stroke-width="1.6"/>')
        p.append(f'<path d="M{x+52},{sy+52} L{x+52},{sy+26}" stroke="{GD}" stroke-width="2.6"/>')
        p.append(f'<path d="M{x+52},{sy+32} q-15,-7 -21,-2 q9,7 21,2z" fill="{G}"/>')
        p.append(f'<path d="M{x+52},{sy+27} q15,-7 21,-2 q-9,7 -21,2z" fill="{G}"/>')
        p.append(_t(x + 52, sy + 68, "plant site", INK2, 10, None, "middle"))
    # control bucket
    p.append(f'<rect x="{sx-232}" y="{sy+8}" width="182" height="188" rx="11" fill="{PANEL2}" stroke="{INK2}" stroke-width="2"/>')
    p.append(_t(sx - 141, sy + 32, "CONTROL BUCKET", INK, 11.5, 700, "middle"))
    p.append(_t(sx - 141, sy + 46, "no plant in it", MUT, 10, None, "middle"))
    for j, (s, col) in enumerate([("circulation pump", INK2), ("pH · EC · DO · ORP probes", BLU),
                                  ("heater / chiller", AMB), ("RO top-off float", BLU),
                                  ("nutrient addback point", G)]):
        p.append(f'<circle cx="{sx-216}" cy="{sy+68+j*26}" r="3.6" fill="{col}"/>')
        p.append(_t(sx - 205, sy + 72 + j * 26, s, INK2, 10.4))
    # feed and return manifolds
    p.append(f'<path d="M{sx-50},{sy+52} L{sx-24},{sy+52} L{sx-24},{sy+30} L{sx+700-260},{sy+30}" '
             f'fill="none" stroke="{G}" stroke-width="3.4"/>')
    p.append(_t(sx + 150, sy + 22, "feed manifold →", G, 10.5, 700, "middle"))
    p.append(f'<path d="M{sx+700-260},{sy+212} L{sx-24},{sy+212} L{sx-24},{sy+150} L{sx-50},{sy+150}" '
             f'fill="none" stroke="{BLU}" stroke-width="3.4"/>')
    p.append(_t(sx + 150, sy + 227, "← return to control bucket, by gravity", BLU, 10.5, 700, "middle"))
    for i in range(3):
        x = sx + i * 132 + 52
        p.append(f'<line x1="{x}" y1="{sy+30}" x2="{x}" y2="{sy}" stroke="{G}" stroke-width="2"/>')
        p.append(f'<line x1="{x}" y1="{sy+76}" x2="{x}" y2="{sy+212}" stroke="{BLU}" stroke-width="2"/>')
    # air manifold, outside the room
    p.append(f'<line x1="24" y1="{H-96}" x2="{W-24}" y2="{H-96}" stroke="{LINE}" stroke-width="1.6" stroke-dasharray="6 4"/>')
    p.append(_t(W - 26, H - 102, "room wall", MUT, 10, None, "end"))
    p.append(f'<rect x="26" y="{H-72}" width="128" height="40" rx="8" fill="{AMBL}" stroke="{AMB}" stroke-width="1.6"/>')
    p.append(_t(90, H - 53, "air blower", INK, 11, 700, "middle"))
    p.append(_t(90, H - 40, "outside the room", MUT, 9.6, None, "middle"))
    p.append(f'<path d="M154,{H-52} L{W-60},{H-52}" stroke="{AMB}" stroke-width="3"/>')
    for i in range(3):
        x = sx + i * 132 + 78
        p.append(f'<line x1="{x}" y1="{H-52}" x2="{x}" y2="{sy+76}" stroke="{AMB}" stroke-width="1.8" stroke-dasharray="4 3"/>')
    p.append(_t(W - 58, H - 58, "air manifold", AMB, 10.4, 700, "end"))
    return _svg(W, H, "Schematic of a recirculating deep water culture loop", p)


# ---------------------------------------------------------------- 5. ORP mixed potential
def orp_mixed_potential():
    W, H = 760, 400
    p = _title("Why the ORP number is not an oxygen number",
               "Six couples in one water can sit 1200 mV apart. The electrode reports a compromise.")
    ax, ay, aw = 250, 88, 420
    p.append(f'<line x1="{ax}" y1="{ay}" x2="{ax}" y2="{ay+224}" stroke="{LINE}" stroke-width="1.4"/>')
    barmax = 176
    rows = [
        ("O₂ / H₂O", 0.86, "very slow at Pt — barely counts", MUT, 0.30),
        ("HOCl / Cl⁻", 0.96, "fast and strong — dominates if dosed", RED, 1.0),
        ("H₂O₂ / H₂O", 0.80, "fast, strong, short-lived", AMB, 1.0),
        ("Fe³⁺ / Fe²⁺", 0.52, "genuinely poises the solution", PUR, 0.95),
        ("Organic C (reduced)", 0.24, "pulls the reading down", GD, 0.8),
    ]
    for i, (name, frac, note, col, op) in enumerate(rows):
        y = ay + 18 + i * 42
        bw = frac * barmax
        p.append(_t(ax - 12, y + 4, name, INK2, 11, None, "end", MN))
        p.append(f'<rect x="{ax+2}" y="{y-9}" width="{bw:.0f}" height="18" rx="4" fill="{col}" opacity="{op*0.55}"/>')
        p.append(f'<circle cx="{ax+2+bw:.0f}" cy="{y}" r="4.6" fill="{col}" opacity="{op}"/>')
        p.append(_t(ax + 10 + bw, y + 4, note, MUT, 10))
    # the mixed potential the meter shows
    my = ay + 236
    p.append(f'<line x1="{ax}" y1="{my}" x2="{ax+barmax}" y2="{my}" stroke="{LINE}" stroke-width="1"/>')
    mx = ax + 0.60 * barmax
    p.append(f'<rect x="{mx-46:.0f}" y="{my+12}" width="92" height="34" rx="7" fill="{INK2}"/>')
    p.append(_t(mx, my + 27, "what the", PAPER, 10, 700, "middle"))
    p.append(_t(mx, my + 40, "meter shows", PAPER, 10, 700, "middle"))
    p.append(f'<path d="M{mx:.0f},{my+12} L{mx:.0f},{ay+10}" '
             f'stroke="{INK2}" stroke-width="1.4" stroke-dasharray="3 4"/>')
    p.append(_t(ax - 12, my + 32, "mixed potential", INK, 11, 700, "end"))
    p.append(_t(ax, ay - 10, "weakly oxidising", MUT, 10))
    p.append(_t(ax + barmax, ay - 10, "strongly oxidising →", MUT, 10, None, "end"))
    p.append(_t(24, H - 14,
                "Dissolved oxygen sits at the bottom of the list. If you dose no oxidiser, ORP is mostly telling you how clean the water is.",
                MUT, 11))
    return _svg(W, H, "How competing redox couples produce a mixed potential at the electrode", p)


# ---------------------------------------------------------------- 6. bubble scale
def bubble_scale():
    W, H = 760, 320
    p = _title("Three bubble regimes, three completely different behaviours")
    cols = [
        ("Coarse", "air stone", "1–5 mm", "seconds", "rises fast, bursts,\nstirs hard", AMB, AMBL, [16, 12, 19]),
        ("Fine / micro", "diffuser", "10–100 µm", "minutes", "rises slowly,\nmilky appearance", BLU, BLUL, [7, 5, 8, 6, 7]),
        ("Nano", "generator", "< 200 nm", "~70 days", "does not rise,\nkeeps dissolving", G, GL, [2.4] * 14),
    ]
    for i, (name, sub, size, life, note, col, band, radii) in enumerate(cols):
        cx = 152 + i * 232
        p.append(f'<rect x="{cx-104}" y="70" width="208" height="196" rx="11" fill="{PANEL2}" stroke="{LINE}"/>')
        p.append(f'<rect x="{cx-104}" y="70" width="208" height="30" rx="11" fill="{band}" opacity=".85"/>')
        p.append(f'<rect x="{cx-104}" y="90" width="208" height="10" fill="{band}" opacity=".85"/>')
        p.append(_t(cx, 90, name, INK, 12.5, 700, "middle"))
        # bubbles
        import math
        for j, r in enumerate(radii):
            bx = cx - 70 + (j * 47) % 140 + 12 * math.sin(j * 2.1)
            by = 128 + (j * 31) % 76
            p.append(f'<circle cx="{bx:.0f}" cy="{by:.0f}" r="{r}" fill="{PAPER}" stroke="{col}" stroke-width="1.3" opacity=".95"/>')
        p.append(_t(cx, 224, size, col, 12, 700, "middle", MN))
        p.append(_t(cx, 241, "persists ~" + life, INK2, 10.4, None, "middle"))
        for k, ln in enumerate(note.split("\n")):
            p.append(_t(cx, 256 + k * 12, ln, MUT, 9.8, None, "middle"))
        p.append(_t(cx, 285, sub, MUT, 10, None, "middle"))
    p.append(_t(24, H - 12,
                "Nanobubbles decouple oxygen delivery from mechanical agitation — the two things a coarse air stone forces you to buy together.",
                MUT, 11))
    return _svg(W, H, "Coarse, fine and nano bubble regimes compared", p)


# ---------------------------------------------------------------- 7. supply vs demand
def supply_demand():
    W, H = 720, 356
    p = _title("Warming the reservoir cuts supply and raises demand at the same time",
               "Two curves moving apart. This is why temperature is the master dial.")
    left, right, top, bot = 62, 34, 74, H - 66
    plotw = W - left - right
    xs = [14, 17, 20, 23, 26, 29, 32]
    sup = [10.31, 9.66, 9.09, 8.56, 8.09, 7.67, 7.31]      # mg/L air-saturated
    dem = [1.0, 1.23, 1.52, 1.87, 2.30, 2.83, 3.48]        # relative respiration, Q10 = 2

    def X(i): return left + i / (len(xs) - 1) * plotw
    def Ys(v): return bot - (v - 6.5) / (11.0 - 6.5) * (bot - top)
    def Yd(v): return bot - (v - 0.8) / (3.8 - 0.8) * (bot - top)

    for g in range(5):
        y = top + g * (bot - top) / 4
        p.append(f'<line x1="{left}" y1="{y:.0f}" x2="{W-right}" y2="{y:.0f}" stroke="{LINE}" '
                 f'stroke-width="0.8" stroke-dasharray="3 4"/>')
    for i, t in enumerate(xs):
        p.append(_t(X(i), bot + 17, f"{t}°C", MUT, 10, None, "middle", MN))
    p.append(f'<path d="M' + " L".join(f"{X(i):.0f},{Ys(v):.0f}" for i, v in enumerate(sup)) +
             f'" fill="none" stroke="{BLU}" stroke-width="3.2"/>')
    p.append(f'<path d="M' + " L".join(f"{X(i):.0f},{Yd(v):.0f}" for i, v in enumerate(dem)) +
             f'" fill="none" stroke="{RED}" stroke-width="3.2"/>')
    for i, v in enumerate(sup):
        p.append(f'<circle cx="{X(i):.0f}" cy="{Ys(v):.0f}" r="3.4" fill="{BLU}"/>')
    for i, v in enumerate(dem):
        p.append(f'<circle cx="{X(i):.0f}" cy="{Yd(v):.0f}" r="3.4" fill="{RED}"/>')
    p.append(_t(X(0) + 8, Ys(sup[0]) - 12, "oxygen the water can hold", BLU, 11, 700))
    p.append(_t(X(6) - 8, Yd(dem[6]) - 14, "oxygen the root demands", RED, 11, 700, "end"))
    # the widening gap
    p.append(f'<path d="M{X(6)-26:.0f},{Ys(sup[6]):.0f} L{X(6)-26:.0f},{Yd(dem[6]):.0f}" '
             f'stroke="{AMB}" stroke-width="1.6" stroke-dasharray="4 3"/>')
    p.append(_t(24, H - 14,
                "Supply falls ~1.7% per °C. Demand roughly doubles per 10 °C. Across 14→32 °C the ratio worsens by about 5×.",
                MUT, 11))
    return _svg(W, H, "Oxygen supply falling and oxygen demand rising with temperature", p)
