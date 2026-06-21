# -*- coding: utf-8 -*-
"""Parametric inline-SVG figure builders shared across papers. Light theme, green
data-viz palette, charcoal text. Every svg has an explicit viewBox + role/aria."""
from figs import G, GD, GL, GXL, INK, INK2, MUT, LINE, AMB, AMBL, RED, REDL, BLU, BLUL, PUR, PURL, PAPER, PANEL2, FS, MN

def _wrap(draw, x, y, text, width_chars, lh, fs, fill, anchor="start"):
    words = text.split(); line = ""; out = []
    for w in words:
        if len(line) + len(w) + 1 > width_chars:
            out.append(line); line = w
        else:
            line = (line + " " + w).strip()
    if line: out.append(line)
    for i, ln in enumerate(out):
        draw.append(f'<text x="{x}" y="{y+i*lh}" text-anchor="{anchor}" fill="{fill}" font-size="{fs}" style="{FS}">{ln}</text>')
    return y + len(out) * lh

def _svg(w, h, label, parts):
    head = (f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
            f'xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{label}">'
            f'<rect width="{w}" height="{h}" fill="{PAPER}"/>')
    return head + "".join(parts) + "</svg>"

# ---------------------------------------------------------------- vertical bars
def bars(title, data, unit="", note="", target=None, maxv=None):
    W = 720; H = 320; left = 52; right = 20; top = 58; bot = H - 56
    n = len(data); plotw = W - left - right; step = plotw / n; bw = step * 0.56
    mx = maxv or (max(v for _, v in data) * 1.15) or 1
    p = []
    p.append(f'<text x="24" y="26" fill="{INK}" font-size="15" font-weight="700" style="{FS}">{title}</text>')
    if note:
        p.append(f'<text x="24" y="45" fill="{MUT}" font-size="11.5" style="{FS}">{note}</text>')
    for g in range(0, 5):
        v = mx * g / 4; y = bot - (v / mx) * (bot - top)
        p.append(f'<line x1="{left}" y1="{y:.1f}" x2="{W-right}" y2="{y:.1f}" stroke="{LINE}" stroke-width="0.8" stroke-dasharray="3 4"/>')
        p.append(f'<text x="{left-8}" y="{y+4:.1f}" text-anchor="end" fill="{MUT}" font-size="10" style="{MN}">{v:.0f}</text>')
    if target is not None:
        ty = bot - (target / mx) * (bot - top)
        p.append(f'<line x1="{left}" y1="{ty:.1f}" x2="{W-right}" y2="{ty:.1f}" stroke="{AMB}" stroke-width="1.5" stroke-dasharray="6 3"/>')
        p.append(f'<text x="{W-right}" y="{ty-5:.1f}" text-anchor="end" fill="{AMB}" font-size="10.5" font-weight="700" style="{FS}">target</text>')
    for i, (lab, v) in enumerate(data):
        x = left + i * step + (step - bw) / 2
        bh = (v / mx) * (bot - top)
        p.append(f'<rect x="{x:.1f}" y="{bot-bh:.1f}" width="{bw:.1f}" height="{bh:.1f}" rx="4" fill="{G}" opacity=".9"/>')
        p.append(f'<text x="{x+bw/2:.1f}" y="{bot-bh-6:.1f}" text-anchor="middle" fill="{GD}" font-size="11" font-weight="700" style="{FS}">{v}{unit}</text>')
        p.append(f'<text x="{x+bw/2:.1f}" y="{bot+16:.1f}" text-anchor="middle" fill="{INK2}" font-size="10.5" style="{FS}">{lab}</text>')
    return _svg(W, H, title, p)

# ---------------------------------------------------------------- horizontal bars
def hbars(title, data, unit="", note=""):
    W = 720; rowh = 34; top = 58; H = top + rowh * len(data) + 30; left = 150; right = 60
    mx = max(v for _, v in data) * 1.12 or 1; plotw = W - left - right
    p = []
    p.append(f'<text x="24" y="26" fill="{INK}" font-size="15" font-weight="700" style="{FS}">{title}</text>')
    if note:
        p.append(f'<text x="24" y="45" fill="{MUT}" font-size="11.5" style="{FS}">{note}</text>')
    for i, (lab, v) in enumerate(data):
        y = top + i * rowh
        p.append(f'<text x="{left-10}" y="{y+19}" text-anchor="end" fill="{INK2}" font-size="12" style="{FS}">{lab}</text>')
        bw = (v / mx) * plotw
        p.append(f'<rect x="{left}" y="{y+6}" width="{bw:.1f}" height="20" rx="5" fill="{G}" opacity=".9"/>')
        p.append(f'<text x="{left+bw+8:.1f}" y="{y+21}" fill="{GD}" font-size="11.5" font-weight="700" style="{FS}">{v}{unit}</text>')
    return _svg(W, H, title, p)

# ---------------------------------------------------------------- line chart
def line(title, pts, xlabels, ylab="", note="", ymax=None, ymin=0, bands=None):
    W = 720; H = 320; left = 56; right = 22; top = 50; bot = H - 50
    xs = len(pts); plotw = W - left - right; ploth = bot - top
    ymax = ymax or max(v for _, v in pts) * 1.12
    def X(i): return left + (i / (xs - 1)) * plotw if xs > 1 else left
    def Y(v): return bot - ((v - ymin) / (ymax - ymin)) * ploth
    p = []
    p.append(f'<text x="24" y="26" fill="{INK}" font-size="15" font-weight="700" style="{FS}">{title}</text>')
    if note:
        p.append(f'<text x="24" y="44" fill="{MUT}" font-size="11.5" style="{FS}">{note}</text>')
    if bands:
        for (lo, hi, col, lbl) in bands:
            y1 = Y(hi); y2 = Y(lo)
            p.append(f'<rect x="{left}" y="{y1:.1f}" width="{plotw:.1f}" height="{(y2-y1):.1f}" fill="{col}" opacity=".5"/>')
            p.append(f'<text x="{left+6}" y="{y1+13:.1f}" fill="{GD}" font-size="10" style="{FS}">{lbl}</text>')
    for g in range(0, 5):
        v = ymin + (ymax - ymin) * g / 4; y = Y(v)
        p.append(f'<line x1="{left}" y1="{y:.1f}" x2="{W-right}" y2="{y:.1f}" stroke="{LINE}" stroke-width="0.8" stroke-dasharray="3 4"/>')
        p.append(f'<text x="{left-8}" y="{y+4:.1f}" text-anchor="end" fill="{MUT}" font-size="10" style="{MN}">{v:.0f}</text>')
    for i, lab in enumerate(xlabels):
        p.append(f'<text x="{X(i):.1f}" y="{bot+16:.1f}" text-anchor="middle" fill="{MUT}" font-size="10" style="{MN}">{lab}</text>')
    path = "M" + " L".join(f"{X(i):.1f},{Y(v):.1f}" for i, (_, v) in enumerate(pts))
    p.append(f'<path d="{path}" fill="none" stroke="{GD}" stroke-width="3"/>')
    for i, (_, v) in enumerate(pts):
        p.append(f'<circle cx="{X(i):.1f}" cy="{Y(v):.1f}" r="3.4" fill="{GD}"/>')
    if ylab:
        p.append(f'<text x="16" y="{(top+bot)/2:.1f}" fill="{MUT}" font-size="10.5" style="{FS}" transform="rotate(-90 16,{(top+bot)/2:.1f})" text-anchor="middle">{ylab}</text>')
    return _svg(W, H, title, p)

# ---------------------------------------------------------------- horizontal flow
def flow(title, steps, note=""):
    W = 760; bw = (W - 24 - 12 * (len(steps) - 1)) / len(steps); H = 196
    p = []
    p.append(f'<text x="12" y="24" fill="{INK}" font-size="14" font-weight="700" style="{FS}">{title}</text>')
    x0 = 12
    for i, st in enumerate(steps):
        t = st[0]; d = st[1]; fill = st[2] if len(st) > 2 else GL; col = st[3] if len(st) > 3 else GD
        x = x0 + i * (bw + 12)
        p.append(f'<rect x="{x:.1f}" y="54" width="{bw:.1f}" height="100" rx="10" fill="{fill}" stroke="{LINE}"/>')
        p.append(f'<circle cx="{x+bw/2:.1f}" cy="48" r="15" fill="{col}"/>')
        p.append(f'<text x="{x+bw/2:.1f}" y="53" text-anchor="middle" fill="#fff" font-size="13" font-weight="700" style="{MN}">{i+1}</text>')
        p.append(f'<text x="{x+bw/2:.1f}" y="82" text-anchor="middle" fill="{INK}" font-size="12.5" font-weight="700" style="{FS}">{t}</text>')
        yy = 100; words = d.split(); line = ""
        for wd in words:
            if len(line) + len(wd) + 1 > 16:
                p.append(f'<text x="{x+bw/2:.1f}" y="{yy}" text-anchor="middle" fill="{INK2}" font-size="9.6" style="{FS}">{line}</text>'); yy += 12; line = wd
            else:
                line = (line + " " + wd).strip()
        if line:
            p.append(f'<text x="{x+bw/2:.1f}" y="{yy}" text-anchor="middle" fill="{INK2}" font-size="9.6" style="{FS}">{line}</text>')
        if i < len(steps) - 1:
            p.append(f'<text x="{x+bw+6-1:.1f}" y="108" text-anchor="middle" fill="{MUT}" font-size="15" font-weight="700">&rarr;</text>')
    if note:
        p.append(f'<text x="12" y="180" fill="{MUT}" font-size="11" style="{FS}">{note}</text>')
    return _svg(W, H, title, p)

# ---------------------------------------------------------------- target zones on an axis
def zones(title, lo, hi, bands, unit="", note=""):
    """bands: list of (start, end, color, label). lo/hi = axis range."""
    W = 720; H = 170; left = 24; right = 24; y = 76; bh = 40; plotw = W - left - right
    def X(v): return left + (v - lo) / (hi - lo) * plotw
    p = []
    p.append(f'<text x="24" y="26" fill="{INK}" font-size="15" font-weight="700" style="{FS}">{title}</text>')
    if note:
        p.append(f'<text x="24" y="45" fill="{MUT}" font-size="11.5" style="{FS}">{note}</text>')
    p.append(f'<rect x="{left}" y="{y}" width="{plotw:.1f}" height="{bh}" rx="7" fill="{PANEL2}" stroke="{LINE}"/>')
    for (s, e, col, lbl) in bands:
        x1 = X(s); w = X(e) - X(s)
        p.append(f'<rect x="{x1:.1f}" y="{y}" width="{w:.1f}" height="{bh}" fill="{col}" opacity=".55"/>')
        p.append(f'<text x="{x1+w/2:.1f}" y="{y+bh/2+4:.1f}" text-anchor="middle" fill="{INK}" font-size="10.5" font-weight="700" style="{FS}">{lbl}</text>')
    for tick in (lo, (lo+hi)/2, hi):
        p.append(f'<line x1="{X(tick):.1f}" y1="{y+bh}" x2="{X(tick):.1f}" y2="{y+bh+6}" stroke="{MUT}" stroke-width="1"/>')
        p.append(f'<text x="{X(tick):.1f}" y="{y+bh+20:.1f}" text-anchor="middle" fill="{MUT}" font-size="10.5" style="{MN}">{tick:g}{unit}</text>')
    return _svg(W, H, title, p)
