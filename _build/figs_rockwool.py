# -*- coding: utf-8 -*-
"""Bespoke SVG diagrams for the rockwool crop-steering paper. Themable (CSS vars)."""
from figs import (G, GD, GL, GXL, INK, INK2, MUT, LINE, AMB, AMBL, RED, REDL,
                  BLU, BLUL, PUR, PURL, PAPER, PANEL2, FS, MN)

WATER = "#4f8fd0"; WATERL = "#dbe9f6"; DRY = "#cdb48b"; DRYL = "#ece0cc"; SALT = "#c98a2a"

def _svg(w, h, label, parts):
    return (f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" xmlns="http://www.w3.org/2000/svg" '
            f'role="img" aria-label="{label}"><rect width="{w}" height="{h}" fill="{PAPER}"/>'
            + "".join(parts) + "</svg>")

# ---------------------------------------------------------------- cube cross-section
def fig_cube_anatomy():
    W, H = 720, 360
    p = [f'<text x="24" y="28" fill="{INK}" font-size="15" font-weight="700" style="{FS}">Inside a rockwool block: where the water actually sits</text>']
    bx, by, bw, bh = 60, 70, 360, 230
    # block body
    p.append(f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="6" fill="{DRYL}" stroke="{MUT}" stroke-width="2"/>')
    # horizontal fibre lines (rockwool is spun horizontal)
    for i in range(1, 11):
        yy = by + i * bh / 11
        p.append(f'<line x1="{bx+6}" y1="{yy:.0f}" x2="{bx+bw-6}" y2="{yy:.0f}" stroke="{DRY}" stroke-width="1.4" opacity=".7"/>')
    # water film at fibre crossings + a saturated lower band
    p.append(f'<rect x="{bx+3}" y="{by+bh-70}" width="{bw-6}" height="64" fill="{WATERL}" opacity=".85"/>')
    for x in range(bx+24, bx+bw-10, 40):
        for y in range(by+18, by+bh-72, 34):
            p.append(f'<circle cx="{x}" cy="{y}" r="3.2" fill="{WATER}" opacity=".8"/>')
    # dripper in
    p.append(f'<path d="M{bx+bw/2},36 L{bx+bw/2},{by}" stroke="{INK2}" stroke-width="3"/>')
    p.append(f'<circle cx="{bx+bw/2}" cy="34" r="6" fill="{INK2}"/>')
    # roots
    p.append(f'<path d="M{bx+bw/2},{by+10} q-30,60 -50,120 M{bx+bw/2},{by+10} q30,70 60,150 M{bx+bw/2},{by+10} q-8,90 -4,160" fill="none" stroke="{GD}" stroke-width="1.6" opacity=".8"/>')
    # drain
    p.append(f'<path d="M{bx+bw/2},{by+bh} l0,22" stroke="{WATER}" stroke-width="3"/>')
    p.append(f'<text x="{bx+bw/2}" y="{by+bh+34}" text-anchor="middle" fill="{WATER}" font-size="11" style="{FS}">runoff / drain</text>')
    # callouts right
    lx = bx + bw + 26
    def cl(y, c, t1, t2):
        s = [f'<circle cx="{lx-12}" cy="{y-4}" r="6" fill="{c}"/>',
             f'<text x="{lx+4}" y="{y}" fill="{INK}" font-size="13" font-weight="700" style="{FS}">{t1}</text>',
             f'<text x="{lx+4}" y="{y+17}" fill="{INK2}" font-size="11.5" style="{FS}">{t2}</text>']
        return "".join(s)
    p.append(cl(90, WATER, "Water held on the fibres", "Clings as a film; this is your WC%."))
    p.append(cl(150, DRY, "Air-filled porosity", "Gaps between fibres = root oxygen."))
    p.append(cl(210, GD, "Roots", "Live in the moist film + air mix."))
    p.append(cl(270, SALT, "Dissolved salts (EC)", "Stay in the water, not the fibre. CEC ≈ 0."))
    p.append(f'<text x="24" y="{H-12}" fill="{MUT}" font-size="11" style="{FS}">Rockwool holds nothing chemically (CEC near zero), so 100% of what you feed reaches the plant, and salts concentrate as the water leaves.</text>')
    return _svg(W, H, "Rockwool block cross-section", p)

# ---------------------------------------------------------------- water-content band gauge
def fig_wc_band():
    W, H = 720, 330
    bands = [(92, 100, WATER, "100-92%", "Saturated, just irrigated, little air"),
             (70, 92, BLU, "92-70%", "Field capacity to wet, vegetative / bulk"),
             (55, 70, G, "70-55%", "Working band, healthy roots + air"),
             (42, 55, AMB, "55-42%", "Generative dryback, more stress, more air"),
             (30, 42, RED, "42-30%", "Stress floor, EC spikes, edges drying"),
             (0, 30, "#7a2d20", "below 30%", "Non-recoverable, channels, hand-soak only")]
    left, right, top, bot = 250, 60, 56, H - 34
    def Y(v): return bot - (v / 100) * (bot - top)
    p = [f'<text x="24" y="26" fill="{INK}" font-size="15" font-weight="700" style="{FS}">The rockwool water-content band</text>',
         f'<text x="24" y="44" fill="{MUT}" font-size="11.5" style="{FS}">WC% = how full the block is. Steer inside the band; never fall off the bottom.</text>']
    for lo, hi, c, rng, lab in bands:
        y1, y2 = Y(hi), Y(lo)
        p.append(f'<rect x="{left}" y="{y1:.0f}" width="{W-left-right}" height="{(y2-y1):.0f}" fill="{c}" opacity=".5"/>')
        p.append(f'<text x="{left+10}" y="{(y1+y2)/2-2:.0f}" fill="{INK}" font-size="12" font-weight="700" style="{FS}">{rng}</text>')
        p.append(f'<text x="{left+10}" y="{(y1+y2)/2+14:.0f}" fill="{INK2}" font-size="10.5" style="{FS}">{lab}</text>')
    # axis
    p.append(f'<line x1="{left}" y1="{top}" x2="{left}" y2="{bot}" stroke="{LINE}" stroke-width="1.4"/>')
    for v in (0, 30, 55, 70, 92, 100):
        p.append(f'<text x="{left-8}" y="{Y(v)+4:.0f}" text-anchor="end" fill="{MUT}" font-size="10.5" style="{MN}">{v}</text>')
    p.append(f'<line x1="{left}" y1="{Y(30):.0f}" x2="{W-right}" y2="{Y(30):.0f}" stroke="#7a2d20" stroke-width="2" stroke-dasharray="6 4"/>')
    p.append(f'<text x="{W-right}" y="{Y(30)-6:.0f}" text-anchor="end" fill="#7a2d20" font-size="11" font-weight="700" style="{FS}">recovery floor</text>')
    return _svg(W, H, "Rockwool water-content band", p)

# ---------------------------------------------------------------- dry-out 4 stages
def _cube(x, y, w, h, water_frac, salt, channel, dry_core):
    s = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="{DRYL}" stroke="{MUT}" stroke-width="1.5"/>']
    for i in range(1, 7):
        s.append(f'<line x1="{x+3}" y1="{y+i*h/7:.0f}" x2="{x+w-3}" y2="{y+i*h/7:.0f}" stroke="{DRY}" stroke-width="1" opacity=".6"/>')
    wh = h * water_frac
    s.append(f'<rect x="{x+2}" y="{y+h-wh:.0f}" width="{w-4}" height="{wh:.0f}" fill="{WATERL}" opacity=".9"/>')
    if dry_core:
        s.append(f'<ellipse cx="{x+w/2}" cy="{y+h/2}" rx="{w*0.28}" ry="{h*0.3}" fill="{DRY}" opacity=".85"/>')
    if salt:
        for sx in range(x+10, x+w-6, 16):
            for sy in range(int(y+h-wh+8), y+h-6, 16):
                s.append(f'<circle cx="{sx}" cy="{sy}" r="2" fill="{SALT}"/>')
    if channel:
        s.append(f'<path d="M{x+w*0.4},{y} L{x+w*0.42},{y+h}" stroke="{WATER}" stroke-width="3"/>')
        s.append(f'<path d="M{x+w*0.65},{y} L{x+w*0.6},{y+h}" stroke="{WATER}" stroke-width="3"/>')
    return "".join(s)

def fig_dryout():
    W, H = 760, 300
    p = [f'<text x="20" y="26" fill="{INK}" font-size="15" font-weight="700" style="{FS}">What happens to a block as it dries</text>']
    cw, gap, x0, y0, ch = 150, 36, 24, 56, 150
    stages = [
        ("1 Saturated", 0.92, False, False, False, "Full of water, little air. Just irrigated.", G),
        ("2 Healthy dryback", 0.6, False, False, False, "Air enters, roots breathe, EC normal. Good.", G),
        ("3 Too dry", 0.38, True, False, False, "Less water, same salt: EC stacks, osmotic stress.", AMB),
        ("4 Non-recoverable", 0.18, True, True, True, "Dry core, water channels straight past it.", RED),
    ]
    for i, (t, wf, salt, ch_, dc, desc, col) in enumerate(stages):
        x = x0 + i * (cw + gap)
        p.append(_cube(x, y0, cw, ch, wf, salt, ch_, dc))
        p.append(f'<text x="{x+cw/2}" y="{y0+ch+22}" text-anchor="middle" fill="{col}" font-size="12.5" font-weight="700" style="{FS}">{t}</text>')
        yy = y0 + ch + 38
        line = ""
        for wd in desc.split():
            if len(line) + len(wd) + 1 > 23:
                p.append(f'<text x="{x+cw/2}" y="{yy}" text-anchor="middle" fill="{INK2}" font-size="10" style="{FS}">{line}</text>'); yy += 12; line = wd
            else: line = (line + " " + wd).strip()
        if line: p.append(f'<text x="{x+cw/2}" y="{yy}" text-anchor="middle" fill="{INK2}" font-size="10" style="{FS}">{line}</text>')
        if i < 3:
            p.append(f'<text x="{x+cw+gap/2-2}" y="{y0+ch/2}" text-anchor="middle" fill="{MUT}" font-size="18" font-weight="700">&rarr;</text>')
    return _svg(W, H, "Rockwool dry-out stages", p)

# ---------------------------------------------------------------- rewet / channeling
def fig_rewet():
    W, H = 720, 320
    p = [f'<text x="24" y="26" fill="{INK}" font-size="15" font-weight="700" style="{FS}">Why a dried-out block won’t just rewet from the dripper</text>']
    for idx, (cx, title, recoverable) in enumerate([(180, "Still moist: rewets evenly", True), (520, "Too dry: water channels past", False)]):
        bx, by, bw, bh = cx-110, 64, 220, 180
        p.append(f'<text x="{cx}" y="56" text-anchor="middle" fill="{(GD if recoverable else RED)}" font-size="12.5" font-weight="700" style="{FS}">{title}</text>')
        p.append(f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="5" fill="{DRYL if not recoverable else WATERL}" stroke="{MUT}" stroke-width="1.5"/>')
        for i in range(1, 7):
            p.append(f'<line x1="{bx+3}" y1="{by+i*bh/7:.0f}" x2="{bx+bw-3}" y2="{by+i*bh/7:.0f}" stroke="{DRY}" stroke-width="1" opacity=".5"/>')
        # dripper
        p.append(f'<circle cx="{cx}" cy="{by-8}" r="5" fill="{INK2}"/>')
        if recoverable:
            # even spread
            p.append(f'<path d="M{cx},{by} q0,40 0,80 M{cx},{by+30} q-50,20 -90,40 M{cx},{by+30} q50,20 90,40" fill="none" stroke="{WATER}" stroke-width="2.4" opacity=".8"/>')
            p.append(f'<text x="{cx}" y="{by+bh+24}" text-anchor="middle" fill="{GD}" font-size="11" style="{FS}">water spreads through the fibres</text>')
        else:
            p.append(f'<ellipse cx="{cx}" cy="{by+bh/2}" rx="62" ry="58" fill="{DRY}" opacity=".9"/>')
            p.append(f'<path d="M{cx-30},{by} L{cx-26},{by+bh}" stroke="{WATER}" stroke-width="4"/>')
            p.append(f'<path d="M{cx+34},{by} L{cx+28},{by+bh}" stroke="{WATER}" stroke-width="4"/>')
            p.append(f'<text x="{cx}" y="{by+bh/2+4}" text-anchor="middle" fill="#7a2d20" font-size="10.5" font-weight="700" style="{FS}">dry core</text>')
            p.append(f'<text x="{cx}" y="{by+bh+24}" text-anchor="middle" fill="{RED}" font-size="11" style="{FS}">runs down channels, core stays dry</text>')
    p.append(f'<text x="24" y="{H-12}" fill="{MUT}" font-size="11" style="{FS}">Below ~30% WC the dry fibre matrix repels even spreading. Water finds preferential channels and exits as runoff, so the drip-rate that hydrated a wet block cannot re-saturate a dry one. You must hand-soak.</text>')
    return _svg(W, H, "Rockwool rewetting and channeling", p)
