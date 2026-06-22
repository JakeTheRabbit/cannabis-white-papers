# -*- coding: utf-8 -*-
"""SVG diagrams for the Daily Checks paper."""
from figs import (G, GD, GL, GXL, INK, INK2, MUT, LINE, AMB, AMBL, RED, REDL,
                  BLU, BLUL, PUR, PURL, PAPER, PANEL2, FS, MN)
from figs_concepts import _svg, _title, _wrap


def bmap():
    W, H = 700, 250
    p = []; _title(p, "Why a check gets done: B = M × A × P", "behaviour fires only when all three line up")
    items = [("Motivation", "wants to", AMBL), ("Ability", "easy to", GL), ("Prompt", "reminded to", BLUL)]
    x0, y0, bw = 60, 80, 150
    for i, (t, d, c) in enumerate(items):
        x = x0 + i * (bw + 40)
        p.append(f'<rect x="{x}" y="{y0}" width="{bw}" height="70" rx="10" fill="{c}" opacity=".6" stroke="{LINE}"/>')
        p.append(f'<text x="{x+bw/2}" y="{y0+30}" text-anchor="middle" fill="{INK}" font-size="13" font-weight="700" style="{FS}">{t}</text>')
        p.append(f'<text x="{x+bw/2}" y="{y0+50}" text-anchor="middle" fill="{INK2}" font-size="11" style="{FS}">{d}</text>')
        if i < 2:
            p.append(f'<text x="{x+bw+20}" y="{y0+42}" text-anchor="middle" fill="{MUT}" font-size="20" font-weight="700">&times;</text>')
    p.append(f'<text x="{W-90}" y="{y0+42}" text-anchor="middle" fill="{MUT}" font-size="20">&rarr;</text>')
    p.append(f'<text x="24" y="{H-30}" fill="{INK}" font-size="12.5" font-weight="700" style="{FS}">The lever is Ability: make the check easier, not the staff keener.</text>')
    p.append(f'<text x="24" y="{H-12}" fill="{MUT}" font-size="11" style="{FS}">Motivation swings day to day; a check that takes 20 seconds and one tap survives a bad day. Auto-fill what you can.</text>')
    return _svg(W, H, "Fogg behaviour model", p)


def autotick():
    W, H = 720, 250
    p = []; _title(p, "How a check ticks itself", "Home Assistant confirms the measurable items so the human does not")
    steps = [("Sensors", "temp, RH, CO2, doors, tank, pump, power", BLUL),
             ("Template\nbinary_sensor", "is every reading in band?", GXL),
             ("Automation", "if true through the window", AMBL),
             ("To-do item", "ticked: 'Environment OK'", GL)]
    x0, y0, bw, gap = 30, 80, 150, 24
    for i, (t, d, c) in enumerate(steps):
        x = x0 + i * (bw + gap)
        p.append(f'<rect x="{x}" y="{y0}" width="{bw}" height="80" rx="9" fill="{c}" opacity=".6" stroke="{LINE}"/>')
        yy = y0 + 26
        for ln in t.split("\n"):
            p.append(f'<text x="{x+bw/2}" y="{yy}" text-anchor="middle" fill="{INK}" font-size="12.5" font-weight="700" style="{FS}">{ln}</text>'); yy += 15
        _wrap(p, x+bw/2, yy + 4, d, INK2, 22, 9.5)
        if i < 3:
            p.append(f'<text x="{x+bw+gap/2}" y="{y0+44}" text-anchor="middle" fill="{MUT}" font-size="16">&rarr;</text>')
    p.append(f'<text x="24" y="{H-12}" fill="{MUT}" font-size="11" style="{FS}">The operator opens the list and sees only the items a sensor cannot confirm. Everything else is already green.</text>')
    return _svg(W, H, "Auto-tick architecture", p)


def auto_vs_human():
    W, H = 720, 300
    p = []; _title(p, "Split the list: what the system knows vs what a human must see", "")
    cols = [("Auto-ticked by Home Assistant", GL, [
                "Temp / RH / VPD / CO2 in range", "Lights on/off, photoperiod, DLI",
                "Doors closed outside hours", "Tank level OK, no leak/flood",
                "Pump ran, runoff in band", "Root-zone EC / pH / WC in band",
                "All equipment online", "Fridge / chiller in range"]),
            ("Needs a human (one tap / NFC)", AMBL, [
                "Visual plant & canopy inspection", "Pest / IPM scout",
                "Structural / leak eyeball", "Sanitation done & verified",
                "Consumables / stock", "Anything that smells or looks off"])]
    for i, (t, c, items) in enumerate(cols):
        x = 30 + i * 360; w = 330
        p.append(f'<rect x="{x}" y="56" width="{w}" height="{H-80}" rx="8" fill="{c}" opacity=".4" stroke="{LINE}"/>')
        p.append(f'<text x="{x+w/2}" y="80" text-anchor="middle" fill="{INK}" font-size="12.5" font-weight="700" style="{FS}">{t}</text>')
        for k, it in enumerate(items):
            p.append(f'<text x="{x+18}" y="{104+k*24}" fill="{INK}" font-size="11" style="{FS}">{"&#10003;" if i==0 else "&#9633;"}  {it}</text>')
    return _svg(W, H, "Auto vs human split", p)


def pause_timeline():
    W, H = 720, 230
    p = []; _title(p, "Not one big sheet: short lists at pause points", "each runs at its trigger moment, 60-90 seconds")
    line_y = 110
    p.append(f'<line x1="40" y1="{line_y}" x2="{W-30}" y2="{line_y}" stroke="{LINE}" stroke-width="2"/>')
    stops = [("Lights-on", "opening: climate, photoperiod, equipment", GL),
             ("First irrigation", "root-zone: VWC, EC, pH, runoff", BLUL),
             ("Mid-day", "crop walk + IPM scout", GXL),
             ("Pre-dark", "closing: dehumidify, security, waste", AMBL),
             ("On alarm", "response checklist", REDL)]
    n = len(stops); span = (W - 70) / (n - 1)
    for i, (t, d, c) in enumerate(stops):
        x = 40 + i * span
        p.append(f'<circle cx="{x:.0f}" cy="{line_y}" r="8" fill="{c}" stroke="{INK}" stroke-width="1"/>')
        p.append(f'<text x="{x:.0f}" y="{line_y-18}" text-anchor="middle" fill="{INK}" font-size="11.5" font-weight="700" style="{FS}">{t}</text>')
        _wrap(p, x, line_y + 28, d, INK2, 16, 9.5)
    p.append(f'<text x="24" y="{H-10}" fill="{MUT}" font-size="11" style="{FS}">Five short pause-point lists beat one long sheet: each is tied to a moment, fits on one screen, and stays under 90 seconds.</text>')
    return _svg(W, H, "Pause-point timeline", p)


def limit_bands():
    W, H = 700, 240
    p = []; _title(p, "Green / amber / red, with a forced action on red", "pre-set the limits so the judgement is already made")
    left, right, top, bot = 50, 30, 64, 180
    def Y(v): return bot - v / 100 * (bot - top)
    bands = [(0, 45, REDL, "red: act now"), (45, 60, AMBL, "amber: watch"),
             (60, 80, GL, "green: ok"), (80, 90, AMBL, "amber"), (90, 100, REDL, "red")]
    for lo, hi, c, l in bands:
        p.append(f'<rect x="{left}" y="{Y(hi):.0f}" width="{W-left-right}" height="{Y(lo)-Y(hi):.0f}" fill="{c}" opacity=".5"/>')
        p.append(f'<text x="{left+8}" y="{(Y(lo)+Y(hi))/2+4:.0f}" fill="{INK}" font-size="10" style="{FS}">{l}</text>')
    pts = [70, 72, 68, 71, 63, 58, 49, 44]
    n = len(pts)
    path = "M" + " L".join(f"{left+i/(n-1)*(W-left-right):.0f},{Y(v):.0f}" for i, v in enumerate(pts))
    p.append(f'<path d="{path}" fill="none" stroke="{INK}" stroke-width="2.4"/>')
    p.append(f'<circle cx="{W-right:.0f}" cy="{Y(44):.0f}" r="5" fill="{RED}"/>')
    p.append(f'<text x="24" y="{H-10}" fill="{MUT}" font-size="11" style="{FS}">A reading drifting into red forces a corrective-action note before the check can be closed, so a problem can never be ticked away.</text>')
    return _svg(W, H, "Limit bands", p)


def default_pass():
    W, H = 700, 250
    p = []; _title(p, "Default to pass, tap only for the exception", "the happy path is almost empty")
    steps = [("Open list", "items default to OK", GL),
             ("Walk the route", "NFC tap proves presence", BLUL),
             ("All good?", "one 'Pass all' submit", GL),
             ("Something off?", "tap it: photo + note required", REDL)]
    x0, y0, bw, gap = 30, 80, 150, 24
    for i, (t, d, c) in enumerate(steps):
        x = x0 + i * (bw + gap)
        p.append(f'<rect x="{x}" y="{y0}" width="{bw}" height="78" rx="9" fill="{c}" opacity=".55" stroke="{LINE}"/>')
        p.append(f'<text x="{x+bw/2}" y="{y0+28}" text-anchor="middle" fill="{INK}" font-size="12" font-weight="700" style="{FS}">{t}</text>')
        _wrap(p, x+bw/2, y0+46, d, INK2, 20, 9.5)
        if i < 3:
            p.append(f'<text x="{x+bw+gap/2}" y="{y0+44}" text-anchor="middle" fill="{MUT}" font-size="16">&rarr;</text>')
    p.append(f'<text x="24" y="{H-26}" fill="{INK}" font-size="12" font-weight="700" style="{FS}">3 taps or fewer on a clean day.</text>')
    p.append(f'<text x="24" y="{H-10}" fill="{MUT}" font-size="11" style="{FS}">Only a flagged item expands to demand a photo and a note, exactly where the audit trail needs to be richest.</text>')
    return _svg(W, H, "Default-to-pass flow", p)


def escalation():
    W, H = 680, 250
    p = []; _title(p, "Miss or out-of-range escalates, tier by tier", "the safety net that makes ownership real")
    tiers = [("Item overdue or reading red", PANEL2),
             ("Push to the named owner", GL),
             ("Unresolved? frontline supervisor", AMBL),
             ("Still open? senior management", REDL)]
    x, y = 80, 70
    for i, (t, c) in enumerate(tiers):
        yy = y + i * 44
        p.append(f'<rect x="{x}" y="{yy}" width="{W-160}" height="34" rx="6" fill="{c}" opacity=".6" stroke="{LINE}"/>')
        _wrap(p, x + (W-160)/2, yy+22, t, INK, 50, 11)
        if i < 3:
            p.append(f'<text x="{x+(W-160)/2}" y="{yy+44}" text-anchor="middle" fill="{MUT}" font-size="14">&darr;</text>')
    p.append(f'<text x="24" y="{H-10}" fill="{MUT}" font-size="11" style="{FS}">Design the owner-absent branch explicitly (PTO / sick) so an escalation never silently dead-ends. Escalate only meaningful misses to avoid alert fatigue.</text>')
    return _svg(W, H, "Escalation ladder", p)
