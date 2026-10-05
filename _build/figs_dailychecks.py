# -*- coding: utf-8 -*-
"""SVG diagrams for the Daily Checks paper."""
from figs import (G, GD, GL, GXL, INK, INK2, MUT, LINE, AMB, AMBL, RED, REDL,
                  BLU, BLUL, PUR, PURL, PAPER, PANEL2, FS, MN)
from figs_concepts import _svg, _title, _wrap


def bmap():
    W, H = 700, 250
    p = []; _title(p, "The Fogg behavior model for a check: B = M × A × P", "A behavior occurs only when all three occur at the same time")
    items = [("Motivation", "wants to", AMBL), ("Ability", "easy to", GL), ("Prompt", "gets a signal to", BLUL)]
    x0, y0, bw = 60, 80, 150
    for i, (t, d, c) in enumerate(items):
        x = x0 + i * (bw + 40)
        p.append(f'<rect x="{x}" y="{y0}" width="{bw}" height="70" rx="10" fill="{c}" opacity=".6" stroke="{LINE}"/>')
        p.append(f'<text x="{x+bw/2}" y="{y0+30}" text-anchor="middle" fill="{INK}" font-size="13" font-weight="700" style="{FS}">{t}</text>')
        p.append(f'<text x="{x+bw/2}" y="{y0+50}" text-anchor="middle" fill="{INK2}" font-size="11" style="{FS}">{d}</text>')
        if i < 2:
            p.append(f'<text x="{x+bw+20}" y="{y0+42}" text-anchor="middle" fill="{MUT}" font-size="20" font-weight="700">&times;</text>')
    p.append(f'<text x="{W-90}" y="{y0+42}" text-anchor="middle" fill="{MUT}" font-size="20">&rarr;</text>')
    p.append(f'<text x="24" y="{H-30}" fill="{INK}" font-size="12.5" font-weight="700" style="{FS}">Ability has the largest effect. Make the check easier. Do not try to increase motivation.</text>')
    p.append(f'<text x="24" y="{H-12}" fill="{MUT}" font-size="11" style="{FS}">Motivation changes each day. Personnel do a check of 20 seconds and one tap on a bad day. Complete items automatically if possible.</text>')
    return _svg(W, H, "Fogg behaviour model", p)


def autotick():
    W, H = 720, 250
    p = []; _title(p, "How an auto-tick operates", "Home Assistant completes the items that a sensor can measure. Thus the person does not do them.")
    steps = [("Sensors", "climate, doors, tank, pump, power", BLUL),
             ("Template\nbinary_sensor", "are all readings in range?", GXL),
             ("Automation", "if on for all of the check period", AMBL),
             ("To-do item", "completed: 'Environment OK'", GL)]
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
    p.append(f'<text x="24" y="{H-12}" fill="{MUT}" font-size="11" style="{FS}">The person opens the checklist and sees only the items that a sensor cannot examine. All the other items are green.</text>')
    return _svg(W, H, "Auto-tick architecture", p)


def auto_vs_human():
    W, H = 720, 300
    p = []; _title(p, "Divide the checklist: items for the system and items for a person", "")
    cols = [("Auto-tick items (Home Assistant)", GL, [
                "Temperature, RH, VPD, CO2 in range", "Lights, photoperiod and DLI correct",
                "Doors closed out of work hours", "Tank level OK, no leak or spill",
                "Pump operated, runoff in range", "Root-zone EC, pH and WC in range",
                "All equipment connected", "Refrigerator and chiller in range"]),
            ("Items for a person (one tap or NFC)", AMBL, [
                "Visual inspection of the plants and canopy", "IPM inspection for pests",
                "Visual check of the structure and leaks", "Sanitation done and examined",
                "Supplies and stock", "Each unusual smell or condition"])]
    for i, (t, c, items) in enumerate(cols):
        x = 30 + i * 360; w = 330
        p.append(f'<rect x="{x}" y="56" width="{w}" height="{H-80}" rx="8" fill="{c}" opacity=".4" stroke="{LINE}"/>')
        p.append(f'<text x="{x+w/2}" y="80" text-anchor="middle" fill="{INK}" font-size="12.5" font-weight="700" style="{FS}">{t}</text>')
        for k, it in enumerate(items):
            p.append(f'<text x="{x+18}" y="{104+k*24}" fill="{INK}" font-size="11" style="{FS}">{"&#10003;" if i==0 else "&#9633;"}  {it}</text>')
    return _svg(W, H, "Auto vs human split", p)


def pause_timeline():
    W, H = 720, 230
    p = []; _title(p, "Short checklists at pause points, not one long checklist", "You do each checklist at its pause point. The time is 60 to 90 seconds.")
    line_y = 110
    p.append(f'<line x1="40" y1="{line_y}" x2="{W-30}" y2="{line_y}" stroke="{LINE}" stroke-width="2"/>')
    stops = [("Lights-on", "opening: climate, photoperiod, equipment", GL),
             ("First irrigation", "root-zone: VWC, EC, pH, runoff", BLUL),
             ("Mid-day", "walk-around and IPM inspection", GXL),
             ("Pre-dark", "end of the day: dehumidification, locks, waste", AMBL),
             ("On alarm", "steps for the alarm", REDL)]
    n = len(stops); span = (W - 70) / (n - 1)
    for i, (t, d, c) in enumerate(stops):
        x = 40 + i * span
        p.append(f'<circle cx="{x:.0f}" cy="{line_y}" r="8" fill="{c}" stroke="{INK}" stroke-width="1"/>')
        p.append(f'<text x="{x:.0f}" y="{line_y-18}" text-anchor="middle" fill="{INK}" font-size="11.5" font-weight="700" style="{FS}">{t}</text>')
        _wrap(p, x, line_y + 28, d, INK2, 16, 9.5)
    p.append(f'<text x="24" y="{H-10}" fill="{MUT}" font-size="11" style="{FS}">Five short checklists are better than one long checklist. Each is for one pause point and is on one screen, in less than 90 seconds.</text>')
    return _svg(W, H, "Pause-point timeline", p)


def limit_bands():
    W, H = 700, 240
    p = []; _title(p, "Green, amber and red, with a corrective action for red", "Set the limits before the check. Thus the person does not make a decision.")
    left, right, top, bot = 50, 30, 64, 180
    def Y(v): return bot - v / 100 * (bot - top)
    bands = [(0, 45, REDL, "red: corrective action"), (45, 60, AMBL, "amber: monitor"),
             (60, 80, GL, "green: OK"), (80, 90, AMBL, "amber"), (90, 100, REDL, "red")]
    for lo, hi, c, l in bands:
        p.append(f'<rect x="{left}" y="{Y(hi):.0f}" width="{W-left-right}" height="{Y(lo)-Y(hi):.0f}" fill="{c}" opacity=".5"/>')
        p.append(f'<text x="{left+8}" y="{(Y(lo)+Y(hi))/2+4:.0f}" fill="{INK}" font-size="10" style="{FS}">{l}</text>')
    pts = [70, 72, 68, 71, 63, 58, 49, 44]
    n = len(pts)
    path = "M" + " L".join(f"{left+i/(n-1)*(W-left-right):.0f},{Y(v):.0f}" for i, v in enumerate(pts))
    p.append(f'<path d="{path}" fill="none" stroke="{INK}" stroke-width="2.4"/>')
    p.append(f'<circle cx="{W-right:.0f}" cy="{Y(44):.0f}" r="5" fill="{RED}"/>')
    p.append(f'<text x="24" y="{H-10}" fill="{MUT}" font-size="11" style="{FS}">For a red reading, the person must write a note about the corrective action. Thus a person cannot remove a problem with only a mark.</text>')
    return _svg(W, H, "Limit bands", p)


def default_pass():
    W, H = 700, 250
    p = []; _title(p, "Set items to OK at the start, and tap only an item that is not OK", "When all items are OK, the person does a very small number of steps.")
    steps = [("Open the checklist", "items are set to OK", GL),
             ("Do the walk-around", "NFC tap records the location", BLUL),
             ("All items OK?", "‘Pass all’ sends the checklist", GL),
             ("An item not OK?", "tap it: you must add a photo and a note", REDL)]
    x0, y0, bw, gap = 30, 80, 150, 24
    for i, (t, d, c) in enumerate(steps):
        x = x0 + i * (bw + gap)
        p.append(f'<rect x="{x}" y="{y0}" width="{bw}" height="78" rx="9" fill="{c}" opacity=".55" stroke="{LINE}"/>')
        p.append(f'<text x="{x+bw/2}" y="{y0+28}" text-anchor="middle" fill="{INK}" font-size="12" font-weight="700" style="{FS}">{t}</text>')
        _wrap(p, x+bw/2, y0+46, d, INK2, 20, 9.5)
        if i < 3:
            p.append(f'<text x="{x+bw+gap/2}" y="{y0+44}" text-anchor="middle" fill="{MUT}" font-size="16">&rarr;</text>')
    p.append(f'<text x="24" y="{H-26}" fill="{INK}" font-size="12" font-weight="700" style="{FS}">A maximum of 3 taps on a day when all items are OK.</text>')
    p.append(f'<text x="24" y="{H-10}" fill="{MUT}" font-size="11" style="{FS}">Only an item that is not OK has a photo and a note. Thus the audit trail has the most information where there is a problem.</text>')
    return _svg(W, H, "Default-to-pass flow", p)


def escalation():
    W, H = 680, 250
    p = []; _title(p, "An item not done, or a reading out of range, escalates one step at a time", "The escalation makes sure that the owner does the check")
    tiers = [("Reading red or item not done by the specified time", PANEL2),
             ("Send an alert to the owner", GL),
             ("If not corrected: the supervisor", AMBL),
             ("If the problem continues: a manager", REDL)]
    x, y = 80, 70
    for i, (t, c) in enumerate(tiers):
        yy = y + i * 44
        p.append(f'<rect x="{x}" y="{yy}" width="{W-160}" height="34" rx="6" fill="{c}" opacity=".6" stroke="{LINE}"/>')
        _wrap(p, x + (W-160)/2, yy+22, t, INK, 50, 11)
        if i < 3:
            p.append(f'<text x="{x+(W-160)/2}" y="{yy+44}" text-anchor="middle" fill="{MUT}" font-size="14">&darr;</text>')
    p.append(f'<text x="24" y="{H-10}" fill="{MUT}" font-size="11" style="{FS}">The escalation must continue when the owner is not at work. Escalate only important problems, to prevent too many alerts.</text>')
    return _svg(W, H, "Escalation ladder", p)
