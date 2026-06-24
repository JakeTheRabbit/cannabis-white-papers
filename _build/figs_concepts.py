# -*- coding: utf-8 -*-
"""Reusable, themable SVG concept diagrams shared across papers."""
from figs import (G, GD, GL, GXL, INK, INK2, MUT, LINE, AMB, AMBL, RED, REDL,
                  BLU, BLUL, PUR, PURL, PAPER, PANEL2, FS, MN)

WATER = "var(--fig-water)"; WATERL = "var(--fig-waterl)"; DRY = "var(--fig-dry)"; DRYL = "var(--fig-dryl)"; SALT = "var(--fig-salt)"; SOLID = "var(--fig-solid)"


def _svg(w, h, label, parts):
    return (f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" xmlns="http://www.w3.org/2000/svg" '
            f'role="img" aria-label="{label}"><rect width="{w}" height="{h}" fill="{PAPER}"/>'
            + "".join(parts) + "</svg>")


def _title(p, t, sub=""):
    p.append(f'<text x="24" y="26" fill="{INK}" font-size="15" font-weight="700" style="{FS}">{t}</text>')
    if sub:
        p.append(f'<text x="24" y="44" fill="{MUT}" font-size="11.5" style="{FS}">{sub}</text>')


def _wrap(p, cx, y, text, fill, maxc=22, fs=10, anchor="middle"):
    line = ""
    for wd in text.split():
        if len(line) + len(wd) + 1 > maxc:
            p.append(f'<text x="{cx}" y="{y}" text-anchor="{anchor}" fill="{fill}" font-size="{fs}" style="{FS}">{line}</text>'); y += fs + 2; line = wd
        else:
            line = (line + " " + wd).strip()
    if line:
        p.append(f'<text x="{cx}" y="{y}" text-anchor="{anchor}" fill="{fill}" font-size="{fs}" style="{FS}">{line}</text>')
    return y


# ---- a substrate block at a given water fraction (shared helper) ----
def _block(p, x, y, w, h, wfrac, salt=False):
    p.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="{DRYL}" stroke="{MUT}" stroke-width="1.4"/>')
    for i in range(1, 6):
        p.append(f'<line x1="{x+3}" y1="{y+i*h/6:.0f}" x2="{x+w-3}" y2="{y+i*h/6:.0f}" stroke="{DRY}" stroke-width="1" opacity=".55"/>')
    wh = h * wfrac
    p.append(f'<rect x="{x+2}" y="{y+h-wh:.0f}" width="{w-4}" height="{wh:.0f}" fill="{WATERL}" opacity=".9"/>')
    if salt:
        for sx in range(int(x+10), int(x+w-6), 15):
            for sy in range(int(y+h-wh+8), int(y+h-6), 15):
                p.append(f'<circle cx="{sx}" cy="{sy}" r="2" fill="{SALT}"/>')


def field_capacity():
    W, H = 700, 250
    p = []; _title(p, "Saturation, field capacity and dryback", "the same block at three points in a day")
    stages = [("Saturated", 0.95, "just irrigated, almost no air"),
              ("Field capacity", 0.7, "free water drained, daily peak"),
              ("Dryback low", 0.45, "plant drank, air + oxygen in")]
    bw, x0, y0, bh = 150, 60, 64, 120
    for i, (t, wf, d) in enumerate(stages):
        x = x0 + i * (bw + 60)
        _block(p, x, y0, bw, bh, wf)
        p.append(f'<text x="{x+bw/2}" y="{y0+bh+22}" text-anchor="middle" fill="{GD}" font-size="12.5" font-weight="700" style="{FS}">{t}</text>')
        _wrap(p, x+bw/2, y0+bh+40, d, INK2, 24)
        if i < 2:
            p.append(f'<text x="{x+bw+30}" y="{y0+bh/2}" text-anchor="middle" fill="{MUT}" font-size="22">&rarr;</text>')
    return _svg(W, H, "Field capacity stages", p)


def ec_concentration():
    W, H = 700, 250
    p = []; _title(p, "Why EC climbs as the root zone dries", "salt stays put while water leaves")
    for i, (t, wf, n, col) in enumerate([("Full + dilute", 0.9, 6, GD), ("Dry + concentrated", 0.45, 6, RED)]):
        x = 70 + i * 330; bw, by, bh = 200, 64, 130
        _block(p, x, by, bw, bh, wf, salt=True)
        p.append(f'<text x="{x+bw/2}" y="{by+bh+24}" text-anchor="middle" fill="{col}" font-size="12.5" font-weight="700" style="{FS}">{t}</text>')
        if i == 0:
            p.append(f'<text x="{x+bw+65}" y="{by+bh/2}" text-anchor="middle" fill="{MUT}" font-size="22">&rarr;</text>')
    _wrap(p, W/2, H-18, "Same number of salt grains, less water to dissolve them: the EC the roots feel rises as water content falls.", MUT, 70, 11)
    return _svg(W, H, "EC concentration on dryback", p)


def photoperiod():
    W, H = 700, 220
    p = []; _title(p, "Photoperiod: the light schedule flips the plant", "hours of light vs dark over 24h")
    for i, (t, on) in enumerate([("Vegetative 18/6", 18), ("Flower 12/12", 12)]):
        y = 70 + i * 70; x0, bw = 200, 440
        p.append(f'<text x="24" y="{y+18}" fill="{INK}" font-size="12" font-weight="700" style="{FS}">{t}</text>')
        onw = bw * on / 24
        p.append(f'<rect x="{x0}" y="{y}" width="{onw:.0f}" height="28" fill="{AMBL}" stroke="{LINE}"/>')
        p.append(f'<rect x="{x0+onw:.0f}" y="{y}" width="{bw-onw:.0f}" height="28" fill="{INK}" opacity=".55" stroke="{LINE}"/>')
        p.append(f'<text x="{x0+onw/2:.0f}" y="{y+18}" text-anchor="middle" fill="{INK}" font-size="11" font-weight="700" style="{FS}">{on}h light</text>')
        p.append(f'<text x="{x0+onw+(bw-onw)/2:.0f}" y="{y+18}" text-anchor="middle" fill="{PAPER}" font-size="11" font-weight="700" style="{FS}">{24-on}h dark</text>')
    p.append(f'<text x="24" y="{H-12}" fill="{MUT}" font-size="11" style="{FS}">12 hours of uninterrupted dark triggers and holds flowering. A light leak in the dark can revert or stress the plant.</text>')
    return _svg(W, H, "Photoperiod schedule", p)


def ph_availability():
    W, H = 700, 280
    p = []; _title(p, "pH and nutrient availability (soilless)", "most nutrients open up around pH 5.5-6.5")
    left, right, top, bot = 60, 40, 70, 210
    lo, hi = 4.0, 8.0
    def X(v): return left + (v - lo) / (hi - lo) * (W - left - right)
    bands = [(4.0, 5.3, REDL, "locked"), (5.3, 5.8, AMBL, "ok"), (5.8, 6.3, GL, "best"), (6.3, 6.8, AMBL, "ok"), (6.8, 8.0, REDL, "locked")]
    for s, e, c, l in bands:
        p.append(f'<rect x="{X(s):.0f}" y="{top}" width="{X(e)-X(s):.0f}" height="{bot-top}" fill="{c}" opacity=".55"/>')
        p.append(f'<text x="{(X(s)+X(e))/2:.0f}" y="{top+18}" text-anchor="middle" fill="{INK}" font-size="10.5" font-weight="700" style="{FS}">{l}</text>')
    # availability bell
    pts = [(4,.1),(5,.4),(5.5,.8),(6,1.0),(6.5,.85),(7,.5),(8,.15)]
    path = "M" + " L".join(f"{X(v):.0f},{bot-a*(bot-top)*0.8:.0f}" for v, a in pts)
    p.append(f'<path d="{path}" fill="none" stroke="{GD}" stroke-width="3"/>')
    for v in (4, 5, 6, 7, 8):
        p.append(f'<text x="{X(v):.0f}" y="{bot+18}" text-anchor="middle" fill="{MUT}" font-size="10.5" style="{MN}">pH {v}</text>')
    p.append(f'<text x="24" y="{H-8}" fill="{MUT}" font-size="11" style="{FS}">Drift out of the green band and nutrients precipitate or stop being taken up, even though they are in the tank: lockout.</text>')
    return _svg(W, H, "pH nutrient availability", p)


def nutrient_mobility():
    W, H = 700, 290
    p = []; _title(p, "Mobile vs immobile: where the symptom shows", "the plant moves mobile nutrients to new growth")
    for i, (t, where, col, leaves) in enumerate([
        ("Mobile (N, P, K, Mg)", "old / lower leaves first", AMB, "low"),
        ("Immobile (Ca, Fe, B, S)", "new / upper leaves first", RED, "high")]):
        cx = 200 + i * 320
        # stem
        p.append(f'<line x1="{cx}" y1="80" x2="{cx}" y2="230" stroke="{GD}" stroke-width="3"/>')
        for j, ly in enumerate([95, 130, 165, 200]):
            top_leaf = j <= 1
            sick = (leaves == "high" and top_leaf) or (leaves == "low" and not top_leaf)
            lc = col if sick else G
            for sgn in (-1, 1):
                p.append(f'<ellipse cx="{cx+sgn*26}" cy="{ly}" rx="22" ry="9" fill="{lc}" opacity=".85" transform="rotate({sgn*18} {cx+sgn*26} {ly})"/>')
        p.append(f'<text x="{cx}" y="72" text-anchor="middle" fill="{INK}" font-size="12" font-weight="700" style="{FS}">{t}</text>')
        _wrap(p, cx, 252, "symptom: " + where, col, 30, 11)
    return _svg(W, H, "Nutrient mobility", p)


def stomata():
    W, H = 700, 250
    p = []; _title(p, "Stomata: the leaf's adjustable pores", "guard cells swell to open, slacken to close")
    for i, (t, open_, d) in enumerate([("Open (turgid)", True, "CO2 in, water vapour out, transpiring"),
                                       ("Closed (flaccid)", False, "gas exchange stops, plant conserves water")]):
        cx = 200 + i * 320; cy = 130
        gap = 26 if open_ else 5
        col = G if open_ else AMB
        p.append(f'<path d="M{cx-gap},{cy-50} Q{cx-gap-44},{cy} {cx-gap},{cy+50}" fill="none" stroke="{col}" stroke-width="16" stroke-linecap="round"/>')
        p.append(f'<path d="M{cx+gap},{cy-50} Q{cx+gap+44},{cy} {cx+gap},{cy+50}" fill="none" stroke="{col}" stroke-width="16" stroke-linecap="round"/>')
        if open_:
            p.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{gap-4}" ry="42" fill="{INK}" opacity=".15"/>')
            p.append(f'<text x="{cx}" y="{cy-58}" text-anchor="middle" fill="{WATER}" font-size="13">&uarr;</text>')
        p.append(f'<text x="{cx}" y="{cy+78}" text-anchor="middle" fill="{col}" font-size="12.5" font-weight="700" style="{FS}">{t}</text>')
        _wrap(p, cx, cy+96, d, INK2, 26)
    return _svg(W, H, "Stomata open and closed", p)


def porosity():
    W, H = 700, 250
    p = []; _title(p, "What a substrate is made of", "solids hold structure; pores hold water and air")
    media = [("Coco", 12, 35, 53), ("Rockwool", 4, 30, 66), ("Peat mix", 18, 45, 37)]
    x0, bw, gap, base, hgt = 90, 120, 70, 210, 130
    for i, (name, solid, water, air) in enumerate(media):
        x = x0 + i * (bw + gap); y = base - hgt
        seg = [(SOLID, solid, "solid"), (WATER, water, "water"), ("none", air, "air")]
        cy = y
        for col, pct, lab in seg:
            h = hgt * pct / 100
            if col == "none":
                p.append(f'<rect x="{x}" y="{cy:.0f}" width="{bw}" height="{h:.0f}" fill="{PANEL2}" stroke="{LINE}" stroke-dasharray="3 3"/>')
            else:
                p.append(f'<rect x="{x}" y="{cy:.0f}" width="{bw}" height="{h:.0f}" fill="{col}" opacity=".75" stroke="{LINE}"/>')
            if pct > 12:
                p.append(f'<text x="{x+bw/2}" y="{cy+h/2+4:.0f}" text-anchor="middle" fill="{INK}" font-size="10" font-weight="700" style="{FS}">{lab} {pct}%</text>')
            cy += h
        p.append(f'<text x="{x+bw/2}" y="{base+20}" text-anchor="middle" fill="{GD}" font-size="12" font-weight="700" style="{FS}">{name}</text>')
    p.append(f'<text x="24" y="{H-8}" fill="{MUT}" font-size="11" style="{FS}">Air-filled porosity is root oxygen; water-holding capacity is the buffer. The ratio is what makes a medium wet or airy.</text>')
    return _svg(W, H, "Substrate composition", p)


def setpoint_band():
    W, H = 700, 240
    p = []; _title(p, "Setpoint, target band and the real reading", "you steer to a band, not a single number")
    left, right, top, bot = 50, 30, 60, 200
    def Y(v): return bot - v / 100 * (bot - top)
    p.append(f'<rect x="{left}" y="{Y(70):.0f}" width="{W-left-right}" height="{Y(40)-Y(70):.0f}" fill="{GL}" opacity=".5"/>')
    p.append(f'<line x1="{left}" y1="{Y(55):.0f}" x2="{W-right}" y2="{Y(55):.0f}" stroke="{GD}" stroke-width="1.5" stroke-dasharray="6 4"/>')
    p.append(f'<text x="{W-right}" y="{Y(55)-5:.0f}" text-anchor="end" fill="{GD}" font-size="11" font-weight="700" style="{FS}">setpoint</text>')
    p.append(f'<text x="{left+6}" y="{Y(70)+14:.0f}" fill="{INK2}" font-size="10.5" style="{FS}">target band</text>')
    pts = [55, 60, 52, 58, 50, 63, 54, 57, 53, 59, 56]
    n = len(pts)
    path = "M" + " L".join(f"{left+i/(n-1)*(W-left-right):.0f},{Y(v):.0f}" for i, v in enumerate(pts))
    p.append(f'<path d="{path}" fill="none" stroke="{INK}" stroke-width="2.4"/>')
    p.append(f'<text x="24" y="{H-8}" fill="{MUT}" font-size="11" style="{FS}">Act on the signal only when the reading leaves the band, not on every wiggle around the setpoint.</text>')
    return _svg(W, H, "Setpoint and band", p)


def gen_vs_veg():
    W, H = 700, 270
    p = []; _title(p, "Steering the plant with water", "wetter, smaller swings = leafy; drier, bigger swings = flower")
    for i, (t, wet, col, d) in enumerate([("Vegetative", True, G, "high water content, small dryback, fast leafy growth"),
                                          ("Generative", False, AMB, "lower water content, big dryback, flower & ripening")]):
        cx = 200 + i * 320; base = 210
        p.append(f'<line x1="{cx}" y1="100" x2="{cx}" y2="{base}" stroke="{GD}" stroke-width="3"/>')
        spread = 40 if wet else 22
        for ly in (120, 150, 180):
            for sgn in (-1, 1):
                p.append(f'<ellipse cx="{cx+sgn*spread}" cy="{ly}" rx="{spread*0.7:.0f}" ry="10" fill="{G}" opacity=".8" transform="rotate({sgn*15} {cx+sgn*spread} {ly})"/>')
        if not wet:
            p.append(f'<circle cx="{cx}" cy="104" r="9" fill="{AMB}"/>')  # flower
        # water gauge
        gx = cx - 150 if i == 0 else cx + 130
        _block(p, gx, 110, 26, 90, 0.78 if wet else 0.45)
        p.append(f'<text x="{cx}" y="92" text-anchor="middle" fill="{col}" font-size="13" font-weight="700" style="{FS}">{t}</text>')
        _wrap(p, cx, base+22, d, INK2, 30)
    return _svg(W, H, "Generative vs vegetative steering", p)
