# -*- coding: utf-8 -*-
"""Verified neutral slab-irrigation field guide with editable technical overlays."""
from __future__ import annotations

import html as _html
import re
from pathlib import Path


SLUG = "slab-irrigation-strategy"
TITLE = "Slab irrigation, end to end"
EYEBROW = "Feed · Slab steering"
SUB = (
    "A measured slab-irrigation field guide: room layout, common dripper runtimes, "
    "rooting-in, P0-P3 control, crop-stage steering, EC management and finish."
)
META = [
    ("droplet", "Feed & steering"),
    ("image", "6 technical plates"),
    ("quote", "17 cited sources"),
    ("clock", "~30 min read"),
]
RELATED = [
    "rockwool-crop-steering",
    "irrigation-manual",
    "root-zone-teros12",
    "f2-crop-steering",
]

# The guide carries its audited reference list in the payload so its numbered
# citations stay stable and the source HTML remains straightforward to revise.
REF_IDS = []

_PAYLOAD = (
    Path(__file__).with_name("data") / "slab_irrigation_content.html"
).read_text(encoding="utf-8")
_SECTION_RE = re.compile(
    r'<section class="sec" id="([^"]+)"><div class="sec-kicker">(.*?)</div>'
    r'<h2>(.*?)</h2>(.*?)</section>',
    re.S,
)
_TAG_RE = re.compile(r"<[^>]+>")


def _text(fragment: str) -> str:
    return _html.unescape(_TAG_RE.sub("", fragment)).strip()


def _split_blocks(html_fragment: str) -> list[str]:
    """Split a section body into top-level elements for the corpus exporter."""
    blocks: list[str] = []
    depth = 0
    buffer = ""
    index = 0
    void_tags = {"img", "br", "hr", "rect", "line", "circle", "path", "input"}
    while index < len(html_fragment):
        if html_fragment[index] != "<":
            buffer += html_fragment[index]
            index += 1
            continue
        end = html_fragment.find(">", index)
        if end == -1:
            buffer += html_fragment[index:]
            break
        tag = html_fragment[index : end + 1]
        buffer += tag
        name = re.match(r"</?([a-zA-Z0-9]+)", tag)
        self_closing = tag.endswith("/>") or (
            name and name.group(1).lower() in void_tags
        )
        if name and not self_closing:
            if tag.startswith("</"):
                depth -= 1
                if depth == 0:
                    blocks.append(buffer)
                    buffer = ""
            else:
                depth += 1
        index = end + 1
    if buffer.strip():
        blocks.append(buffer)
    return [block for block in blocks if block.strip()]


SECTIONS = [
    {
        "id": section_id,
        "kicker": _text(kicker),
        "title": _text(title),
        "blocks": _split_blocks(body),
    }
    for section_id, kicker, title, body in _SECTION_RE.findall(_PAYLOAD)
]

_refs_match = re.search(
    r'<div data-slab-references>(.*)</div>\s*$', _PAYLOAD, re.S
)
assert len(SECTIONS) == 13, "expected 13 guide sections"
assert _refs_match, "missing audited reference list"
assert len(re.findall(r'<figure\b[^>]*class="[^"]*\bconcept-pair\b', _PAYLOAD)) == 18
assert len(re.findall(r'\bdata-concept="[^"]+"', _PAYLOAD)) == 18
assert len(re.findall(r'<li\b[^>]*\bid="ref-[^"]+"', _PAYLOAD)) == 17
assert "data:image" not in _PAYLOAD

# The site renderer appends these audited, number-stable citations after the
# related-paper cards; the machine-readable corpus receives only guide content.
RAW_REFERENCES = _refs_match.group(1)


def _corpus_blocks(block: str) -> list[str]:
    if block.lstrip().startswith("<style"):
        return []
    if "technical-plate" in block or "concept-pair" in block:
        return [
            f"<p>{caption}</p>"
            for caption in re.findall(r"<figcaption>(.*?)</figcaption>", block, re.S)
        ]
    return [block]


# Keep editable SVG internals and page-only CSS out of the text corpus while
# retaining each plate's factual caption and the audited source list.
CORPUS_SECTIONS = [
    {
        **section,
        "blocks": [
            cleaned
            for block in section["blocks"]
            for cleaned in _corpus_blocks(block)
        ],
    }
    for section in SECTIONS
]
CORPUS_SECTIONS.append(
    {
        "id": "references",
        "kicker": "Sources",
        "title": "References",
        "blocks": [
            f"<p>{entry}</p>"
            for entry in re.findall(r"<li\b[^>]*>(.*?)</li>", RAW_REFERENCES, re.S)
        ],
    }
)
