# -*- coding: utf-8 -*-
"""Reusable HTML block helpers + inline-SVG icon set. Offline-safe (no icon font)."""
import html as _html

ICONS = {
 "home": '<path d="M4 11.5 12 4l8 7.5"/><path d="M6 10v9h12v-9"/>',
 "grid": '<rect x="4" y="4" width="7" height="7" rx="1"/><rect x="13" y="4" width="7" height="7" rx="1"/><rect x="4" y="13" width="7" height="7" rx="1"/><rect x="13" y="13" width="7" height="7" rx="1"/>',
 "book": '<path d="M6 4h11a1 1 0 0 1 1 1v15H7a1 1 0 0 1-1-1z"/><path d="M6 17h12"/>',
 "search": '<circle cx="11" cy="11" r="6"/><path d="M20 20l-4.5-4.5"/>',
 "spark": '<path d="M12 3l1.8 6.2L20 11l-6.2 1.8L12 19l-1.8-6.2L4 11l6.2-1.8z"/>',
 "droplet": '<path d="M12 4s6 6 6 10a6 6 0 0 1-12 0c0-4 6-10 6-10z"/>',
 "building": '<rect x="5" y="4" width="10" height="16" rx="1"/><path d="M15 9h4v11h-4"/><path d="M8 8h2M8 12h2M8 16h2"/>',
 "wind": '<path d="M4 9h9a2.5 2.5 0 1 0-2.5-2.5"/><path d="M4 14h12a2.5 2.5 0 1 1-2.5 2.5"/>',
 "shield": '<path d="M12 3l7 3v5c0 4-3 7-7 9-4-2-7-5-7-9V6z"/>',
 "gauge": '<path d="M5 17a8 8 0 1 1 14 0"/><path d="M12 13l3.5-3"/>',
 "dashboard": '<rect x="4" y="4" width="16" height="16" rx="2"/><path d="M4 10h16M10 10v10"/>',
 "wave": '<path d="M3 12c2-4 4-4 6 0s4 4 6 0 4-4 6 0"/>',
 "loop": '<path d="M4 9a8 8 0 0 1 13-3l2 2"/><path d="M20 15a8 8 0 0 1-13 3l-2-2"/><path d="M19 4v4h-4"/><path d="M5 20v-4h4"/>',
 "flask": '<path d="M9 3h6"/><path d="M10 3v6l-4.5 8.5A1.5 1.5 0 0 0 7 20h10a1.5 1.5 0 0 0 1.5-2.5L14 9V3"/>',
 "doc": '<path d="M7 3h7l5 5v13H7z"/><path d="M14 3v5h5"/>',
 "list": '<path d="M9 6h11M9 12h11M9 18h11"/><path d="M4.5 6h.01M4.5 12h.01M4.5 18h.01"/>',
 "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
 "x": '<path d="M6 6l12 12M18 6L6 18"/>',
 "chevright": '<path d="M9 6l6 6-6 6"/>',
 "arrowright": '<path d="M5 12h14"/><path d="M13 6l6 6-6 6"/>',
 "clock": '<circle cx="12" cy="12" r="8"/><path d="M12 8v4l3 2"/>',
 "image": '<rect x="4" y="5" width="16" height="14" rx="2"/><path d="M4 16l4-4 4 4 3-3 5 5"/><circle cx="9" cy="10" r="1.3"/>',
 "quote": '<path d="M7 7h4v4c0 2-1.3 3.3-3 4"/><path d="M13 7h4v4c0 2-1.3 3.3-3 4"/>',
 "check": '<path d="M5 12.5l4.5 4.5L19 7"/>',
 "alert": '<path d="M12 4l9 16H3z"/><path d="M12 10v4M12 17h.01"/>',
 "seedling": '<path d="M12 20v-7"/><path d="M12 13c0-3 2.2-5 6-5 0 3.8-2.6 6-6 5z"/><path d="M12 15c0-3-2.2-5-6-5 0 3.8 2.6 6 6 5z"/>',
 "info": '<circle cx="12" cy="12" r="8"/><path d="M12 11v5M12 8h.01"/>',
 "bulb": '<path d="M9 18h6M10 21h4"/><path d="M8 11a4 4 0 1 1 8 0c0 1.6-1 2.5-1.5 3.5H9.5C9 13.5 8 12.6 8 11z"/>',
 "key": '<circle cx="8" cy="12" r="3.5"/><path d="M11.5 12H20l-2 2.5M16 12v3"/>',
 "moon": '<path d="M21 12.8A8 8 0 1 1 11.2 3a6 6 0 0 0 9.8 9.8z"/>',
 "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2M5 5l1.4 1.4M17.6 17.6L19 19M19 5l-1.4 1.4M6.4 17.6L5 19"/>',
 "scissors": '<circle cx="6" cy="6" r="2.4"/><circle cx="6" cy="18" r="2.4"/><path d="M8 7.5L20 18M8 16.5L20 6"/>',
 "leaf": '<path d="M5 20c0-8 6-13 14-13 0 8-6 13-14 13z"/><path d="M5 20c3-5 6-7 10-9"/>',
 "beaker": '<path d="M8 3h8M10 3v6l-4 9a1.5 1.5 0 0 0 1.4 2h11.2a1.5 1.5 0 0 0 1.4-2l-4-9V3"/><path d="M7.5 14h9"/>',
}

def icon(name, size=18, cls=""):
    inner = ICONS.get(name, ICONS["doc"])
    c = f' class="{cls}"' if cls else ""
    return (f'<svg{c} width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" '
            f'stroke="currentColor" stroke-width="1.7" stroke-linecap="round" '
            f'stroke-linejoin="round" aria-hidden="true">{inner}</svg>')

def esc(s):
    return _html.escape(str(s), quote=True)

# ---------------- prose ----------------
def p(t): return f"<p>{t}</p>"
def lead(t): return f"<p class='lead'>{t}</p>"
def h(level, t, _id=None):
    ida = f" id='{_id}'" if _id else ""
    return f"<h{level}{ida}>{t}</h{level}>"
def ul(items, cls=""):
    c = f" class='{cls}'" if cls else ""
    return f"<ul{c}>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"
def ol(items, cls=""):
    c = f" class='{cls}'" if cls else ""
    return f"<ol{c}>" + "".join(f"<li>{i}</li>" for i in items) + "</ol>"

# ---------------- callouts / definitions ----------------
_CALLOUT_IC = {
    "note": "info", "tip": "bulb", "warn": "alert", "danger": "alert", "key": "key",
    "evidence": "quote",  # community / provisional evidence note
}
def callout(kind, title, body):
    ic = icon(_CALLOUT_IC.get(kind, "info"), 17)
    return (f"<div class='callout {kind}'><div class='cic'>{ic}</div>"
            f"<div class='cbody'><div class='ctitle'>{title}</div>{body}</div></div>")

def defterm(term, body):
    return (f"<div class='defn'><span class='defn-t'>{term}</span>"
            f"<span class='defn-b'>{body}</span></div>")

# ---------------- table ----------------
def table(headers, rows, cls="", caption=None, foot=None):
    cap = f"<caption>{caption}</caption>" if caption else ""
    th = "".join(f"<th>{x}</th>" for x in headers)
    body = ""
    for r in rows:
        body += "<tr>" + "".join(f"<td>{x}</td>" for x in r) + "</tr>"
    footrow = f"<tfoot><tr><td colspan='{len(headers)}'>{foot}</td></tr></tfoot>" if foot else ""
    c = f" {cls}" if cls else ""
    return (f"<div class='tbl-wrap'><table class='tbl{c}'>{cap}"
            f"<thead><tr>{th}</tr></thead><tbody>{body}</tbody>{footrow}</table></div>")

# ---------------- figure ----------------
def figure(svg, num, caption):
    return (f"<figure class='fig'>{svg}"
            f"<figcaption><span class='fignum'>Figure {num}.</span> {caption}</figcaption></figure>")

def diagram(svg, caption, label="Diagram"):
    """Injected SVG diagram (no fixed figure number, avoids clashing with inline figures)."""
    return (f"<figure class='fig'>{svg}"
            f"<figcaption><span class='fignum'>{label}.</span> {caption}</figcaption></figure>")

def photo(src, caption, alt="", model=""):
    """Raster example image (AI-generated). src relative to site root, e.g. img/foo.jpg."""
    cred = f"<span class='fcredit'>{model}</span>" if model else ""
    a = esc(alt or caption)
    return (f"<figure class='fig photo'><img src='{esc(src)}' alt='{a}' loading='lazy'>"
            f"<figcaption><span class='fignum'>Example.</span> {caption}{cred}</figcaption></figure>")

def photo_sequence(title, frames, caption, model=""):
    """Image progression: [(label, src), ...] shown as labelled frames with arrows."""
    steps = []
    for i, (label, src) in enumerate(frames):
        steps.append(f"<div class='pseq-step'><img src='{esc(src)}' alt='{esc(label)}' loading='lazy'>"
                     f"<div class='pseq-lab'>{esc(label)}</div></div>")
        if i < len(frames) - 1:
            steps.append("<div class='pseq-arr'>&rarr;</div>")
    cred = f"<span class='fcredit'>{model}</span>" if model else ""
    return (f"<figure class='fig figseq'><div class='pseq-t'>{esc(title)}</div>"
            f"<div class='pseq'>{''.join(steps)}</div>"
            f"<figcaption><span class='fignum'>Sequence.</span> {caption}{cred}</figcaption></figure>")

def term_gallery(items, model=""):
    """Labelled image grid of the page's physical key terms. items = [(term, src), ...]."""
    cells = "".join(
        f"<figure class='tgal-item'><img src='{esc(src)}' alt='{esc(term)}' loading='lazy'>"
        f"<figcaption>{term}</figcaption></figure>" for term, src in items)
    cred = f"<span class='fcredit'>{model}</span>" if model else ""
    return (f"<div class='tgal-wrap'><div class='kicker'>{icon('image',14)} Key terms, in the facility{cred}</div>"
            f"<div class='tgal'>{cells}</div></div>")

# ---------------- stage card / grid / cards / kv / steps ----------------
def stagecard(num, title, dur, body):
    return (f"<div class='stagecard'><div class='stagecard-h'>"
            f"<span class='stagenum'>{num}</span><span class='stagetitle'>{title}</span>"
            f"<span class='stagedur'>{dur}</span></div><div class='stagecard-b'>{body}</div></div>")

def grid(cards, cols=2):
    return f"<div class='grid grid-{cols}'>" + "".join(cards) + "</div>"

def card(title, body, tag=None):
    t = f"<span class='card-tag'>{tag}</span>" if tag else ""
    return f"<div class='card'>{t}<div class='card-title'>{title}</div><div class='card-body'>{body}</div></div>"

def chip(t): return f"<span class='chip'>{t}</span>"

def kv(pairs):
    rows = "".join(f"<div class='kv-row'><span class='kv-k'>{k}</span><span class='kv-v'>{v}</span></div>" for k, v in pairs)
    return f"<div class='kv'>{rows}</div>"

def steps(items):
    lis = ""
    for i, (t, b) in enumerate(items, 1):
        lis += (f"<li class='step'><span class='step-n'>{i}</span>"
                f"<div class='step-c'><div class='step-t'>{t}</div><div class='step-b'>{b}</div></div></li>")
    return f"<ol class='steps'>{lis}</ol>"

# ---------------- citation ----------------
def cite(n, ref_id):
    return f"<sup class='cite'><a href='#ref-{ref_id}'>[{n}]</a></sup>"
