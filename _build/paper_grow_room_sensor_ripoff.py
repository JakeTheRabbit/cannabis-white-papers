# -*- coding: utf-8 -*-
"""Grow-room RH sensor exposé, published verbatim from the standalone mega report.

Body text, tables and SVG graphics come unchanged from
data/grow_room_sensor_ripoff_content.html. Only the markup classes are mapped onto the
site skin (tables, callouts, figures). Report-only CSS and the calculator / brand-filter
script live in static/grow-room-sensor-ripoff/ so the auto-interlinker never touches them.
"""
from __future__ import annotations

import html as _html
import re
from pathlib import Path

from paper_slab_irrigation import _split_blocks

SLUG = "grow-room-sensor-ripoff"
TITLE = "THE $6 CHIP INSIDE YOUR $800 BOX"
EYEBROW = "Investigative Grow-Room Hardware Exposé"
SUB = (
    "How Grow-Tech Brands Sold You Disposable Humidity Sensors, Hid the Chemical Drift, "
    "and Let Your Sprays Wreck Your Rooms — Plus the 20-Minute Protocol to Take Back Control."
)
META = [
    ("wave", "Environment and climate"),
    ("image", "12 Visual Graphs & Diagrams"),
    ("quote", "25 Brands Audited"),
    ("clock", "~45 min to read"),
]
TITLE_MAX_PX = 54
RELATED = ["temp-humidity-vpd", "hvac-dehumidification", "harvest-dry-trim-cure", "signal-and-noise"]
REF_IDS = []

_ASSET_V = "3"
_HEAD = (
    f'<link rel="stylesheet" href="assets/{SLUG}/report.css?v={_ASSET_V}">'
)
_TAIL = f'<script src="assets/{SLUG}/report.js?v={_ASSET_V}" defer></script>'

_PAYLOAD = (Path(__file__).with_name("data") / "grow_room_sensor_ripoff_content.html").read_text(encoding="utf-8")

# Skin mapping: report classes -> site classes. Text is not touched.
_PAYLOAD = (
    _PAYLOAD.replace('class="stat-strip"', 'class="wsr-stats"')
    .replace('class="table-wrap"', 'class="tbl-wrap"')
    .replace('class="data-table', 'class="tbl')
    .replace('<figure class="fig">', '<figure class="fig wsr-fig">')
    .replace('class="pill active"', 'class="tier-pill active"')
    .replace('class="pill"', 'class="tier-pill"')
)
_PAYLOAD = re.sub(
    r'<div class="callout">(.*?)</div>',
    r'<div class="callout warn"><div class="cbody">\1</div></div>',
    _PAYLOAD,
    flags=re.S,
)

_STATS = re.search(r'<!-- STATS -->\s*(<div class="wsr-stats">.*?)\s*<section ', _PAYLOAD, re.S).group(1)
assert _STATS.count('class="stat"') == 4 and _STATS.count("<div") == _STATS.count("</div>")
_FOOT = re.search(r'<!-- FOOTER -->\s*(<p class="wsr-foot">.*?</p>)', _PAYLOAD, re.S).group(1)
_SECTION_RE = re.compile(r'<section id="([^"]+)">\s*<h2>(.*?)</h2>(.*?)</section>', re.S)
_TAG_RE = re.compile(r"<[^>]+>")


def _text(fragment: str) -> str:
    return _html.unescape(_TAG_RE.sub("", fragment)).strip()


SECTIONS = []
for _sid, _h2, _body in _SECTION_RE.findall(_PAYLOAD):
    _num, _title = re.match(r"(\d+)\.\s*(.*)", _text(_h2), re.S).groups()
    SECTIONS.append({"id": _sid, "kicker": f"Part {_num}", "title": _title, "blocks": _split_blocks(_body)})

assert len(SECTIONS) == 10, "expected 10 report sections"
assert _PAYLOAD.count('<figure class="fig wsr-fig">') == 12

SECTIONS[0]["blocks"] = [_HEAD, _STATS] + SECTIONS[0]["blocks"]

# Part 10 (the report's own source list) becomes the site's References block, so the
# rail's References link resolves. Its original heading is kept as the kicker.
_SOURCES = SECTIONS.pop()
RAW_REFERENCES = (
    f'<div class="refs" id="references"><div class="sec-kicker">{_SOURCES["kicker"]} · '
    f'{_html.escape(_SOURCES["title"])}</div><h2>References</h2>'
    + "".join(_SOURCES["blocks"]) + _FOOT + "</div>" + _TAIL
)


def _corpus_block(block: str) -> list[str]:
    if block.startswith(("<link", "<script")) or 'class="brand-controls"' in block or 'class="calc-card"' in block:
        return []
    if block.lstrip().startswith("<figure"):
        cap = re.search(r"<figcaption>(.*?)</figcaption>", block, re.S)
        return [f"<p>{cap.group(1)}</p>"] if cap else []
    return [block]


CORPUS_SECTIONS = [
    {**s, "blocks": [c for b in s["blocks"] for c in _corpus_block(b)]} for s in SECTIONS
] + [{"id": "references", "kicker": "Sources", "title": "References", "blocks": _SOURCES["blocks"]}]
