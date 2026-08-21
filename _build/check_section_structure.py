"""Validate white-paper source section metadata before site generation."""

import importlib
import re
import sys
from types import SimpleNamespace


BANNED_FRAMING = (
    "what this is",
    "what this paper is",
    "words you need",
    "in plain English",
    "honest",
    "actually",
    "mental model",
    "what good looks like",
    "realistic expectations",
    "the whole thing",
    "start here",
    "core answer",
    "named and shamed",
)
DEFINITIONS_VARIANTS = (
    "key terms",
    "every term",
    "the words",
    "eight words",
    "ten terms",
    "glossary",
    "the vocabulary",
)
ACRONYMS = {
    "CO2", "EC", "VPD", "HVAC", "GMP", "GACP", "CAPA", "ALCOA+", "PPFD",
    "DLI", "PAR", "LED", "HPS", "CMH", "PPE", "IPM", "ORP", "PPM", "THC",
    "THCA", "COA", "ICP-MS", "HLVD", "HSWA", "NZ", "P0", "P1", "P2", "P3",
    "VWC", "MQ", "FIM", "LEDS", "A", "B", "W", "I-V",
}
PROPER_NAME_EXCEPTIONS = {
    (
        "cannabis-tissue-culture-playbook",
        "ppm",
        "Plant Preservative Mixture (PPM) and commercial kits",
    ),
    (
        "auckland-ipm-blueprint",
        "nz-legal-gate",
        "Legal eligibility of IPM controls in New Zealand",
    ),
    (
        "daily-checks",
        "autocomplete",
        "Home Assistant check automation",
    ),
    (
        "lab-testing-coas",
        "nz-au",
        "Testing for release in NZ and Australia",
    ),
    (
        "compliance-track-trace",
        "worked-examples",
        "Worked examples: NZ and Australia",
    ),
}
KICKER_NUMBER = re.compile(r"^\s*(\d{2})\s*·\s+\S")
TITLE_WORD = re.compile(r"[^\W_][\w+–-]*", re.UNICODE)


def _non_empty(value):
    return bool(value.strip()) if isinstance(value, str) else bool(value)


def _has_banned_framing(title):
    for phrase in BANNED_FRAMING:
        if re.search(r"\b" + re.escape(phrase) + r"\b", title, re.IGNORECASE):
            return phrase
    return None


def _is_acronym(word):
    normalized = word.upper().replace("–", "-")
    return (normalized in ACRONYMS
            or bool(re.fullmatch(r"P[0-3]-P[0-3]", normalized))
            or bool(re.fullmatch(r"[IVXLCDM]+", normalized)))


def _is_technical_token(word):
    return any(character.isdigit() for character in word) or _is_acronym(word)


def _violates_sentence_case(slug, section_id, title):
    if (slug, section_id, title) in PROPER_NAME_EXCEPTIONS:
        return False
    words = TITLE_WORD.findall(title)
    return any(
        word[0].isupper() and not _is_technical_token(word)
        for word in words[1:]
    )


def validate_title_policy(slug, section_id, title):
    """Return strict title-policy diagnostics for one authoritative title record."""
    diagnostics = []
    normalized_title = title.casefold()
    banned = _has_banned_framing(title)
    if normalized_title == "expected results" or "realistic expectations" in normalized_title:
        diagnostics.append(
            f"{slug}: section '{section_id}': must use canonical title "
            f"'Expected results and limitations' instead of '{title}'"
        )
    elif any(normalized_title.startswith(prefix) for prefix in DEFINITIONS_VARIANTS):
        diagnostics.append(
            f"{slug}: section '{section_id}': must use canonical title "
            f"'Definitions' instead of '{title}'"
        )
    elif banned:
        diagnostics.append(
            f"{slug}: section '{section_id}': banned editorial framing "
            f"'{banned}' in title '{title}'"
        )
    if "?" in title:
        diagnostics.append(
            f"{slug}: section '{section_id}': title must not contain '?': '{title}'"
        )
    if _violates_sentence_case(slug, section_id, title):
        diagnostics.append(f"{slug}: section '{section_id}': title is not sentence case: '{title}'")
    return diagnostics


def _has_audited_slab_references(module, slug):
    # This payload owns a numbered reference list outside REF_IDS so its citations
    # remain stable; no other paper is permitted to use this alternate metadata.
    raw_references = getattr(module, "RAW_REFERENCES", None)
    return (slug == "slab-irrigation-strategy"
            and isinstance(raw_references, str)
            and _non_empty(raw_references))


def validate_modules(modules: list[object]) -> list[str]:
    """Return all section-structure policy violations without modifying modules."""
    diagnostics = []
    for module in modules:
        slug = getattr(module, "SLUG", None)
        label = slug if _non_empty(slug) else getattr(module, "__name__", "<unknown module>")
        if not _non_empty(slug):
            diagnostics.append(f"{label}: missing non-empty SLUG")

        sections = getattr(module, "SECTIONS", None)
        if not _non_empty(sections):
            diagnostics.append(f"{label}: missing non-empty SECTIONS")
        ref_ids = getattr(module, "REF_IDS", None)
        if not _non_empty(ref_ids) and not _has_audited_slab_references(module, slug):
            diagnostics.append(f"{label}: missing non-empty REF_IDS")
        if not isinstance(sections, (list, tuple)):
            continue

        first_title = sections[0].get("title") if sections and isinstance(sections[0], dict) else None
        if first_title != "Purpose and scope":
            diagnostics.append(
                f"{label}: first section must be titled 'Purpose and scope', found {first_title!r}"
            )

        seen_ids = set()
        title_positions = {}
        expected_kicker = 1
        for index, section in enumerate(sections):
            position = index + 1
            if not isinstance(section, dict):
                diagnostics.append(f"{label}: section {position}: must be a dictionary")
                continue

            section_id = section.get("id")
            title = section.get("title")
            kicker = section.get("kicker")
            blocks = section.get("blocks")
            for field, value in (("id", section_id), ("title", title), ("kicker", kicker), ("blocks", blocks)):
                if not _non_empty(value):
                    diagnostics.append(f"{label}: section {position}: missing non-empty {field}")

            if _non_empty(section_id):
                if section_id in seen_ids:
                    diagnostics.append(f"{label}: duplicate section id '{section_id}'")
                seen_ids.add(section_id)

            if isinstance(title, str) and title.strip():
                normalized_title = title.casefold()
                title_positions.setdefault(normalized_title, position)
                diagnostics.extend(validate_title_policy(label, section_id, title))

            if isinstance(kicker, str):
                match = KICKER_NUMBER.match(kicker)
                if match:
                    actual_kicker = int(match.group(1))
                    if actual_kicker != expected_kicker:
                        diagnostics.append(
                            f"{label}: numeric kicker for section '{section_id}' is "
                            f"{actual_kicker:02d}; expected {expected_kicker:02d}"
                        )
                    expected_kicker += 1

        definitions_position = title_positions.get("definitions")
        if definitions_position is not None and definitions_position != 2:
            diagnostics.append(
                f"{label}: 'Definitions' must be section 2, found section {definitions_position}"
            )
        troubleshooting_position = title_positions.get("troubleshooting")
        results_position = title_positions.get("expected results and limitations")
        if (troubleshooting_position is not None and results_position is not None
                and troubleshooting_position > results_position):
            diagnostics.append(
                f"{label}: 'Troubleshooting' must precede 'Expected results and limitations'"
            )
    return diagnostics


def _fixture(slug, sections, ref_ids=("ref",), raw_references=None):
    fixture = SimpleNamespace(SLUG=slug, SECTIONS=sections, REF_IDS=list(ref_ids))
    if raw_references is not None:
        fixture.RAW_REFERENCES = raw_references
    return fixture


def _run_self_test():
    fixtures = [
        (
            "first section title",
            _fixture("first-title", [{"id": "start", "title": "Introduction", "kicker": "01 · Start", "blocks": ["x"]}]),
            ["first-title: first section must be titled 'Purpose and scope', found 'Introduction'"],
        ),
        (
            "duplicate section ID",
            _fixture("duplicate-id", [
                {"id": "one", "title": "Purpose and scope", "kicker": "01 · First", "blocks": ["x"]},
                {"id": "one", "title": "Second section", "kicker": "02 · Second", "blocks": ["x"]},
            ]),
            ["duplicate-id: duplicate section id 'one'"],
        ),
        (
            "absent REF_IDS",
            _fixture("missing-refs", [{"id": "one", "title": "Purpose and scope", "kicker": "01 · First", "blocks": ["x"]}], ()),
            ["missing-refs: missing non-empty REF_IDS"],
        ),
        (
            "audited slab references",
            _fixture(
                "slab-irrigation-strategy",
                [{"id": "one", "title": "Purpose and scope", "kicker": "01 · First", "blocks": ["x"]}],
                (),
                "<ol><li>Audited reference</li></ol>",
            ),
            [],
        ),
        (
            "slab RAW_REFERENCES must be a string",
            _fixture(
                "slab-irrigation-strategy",
                [{"id": "one", "title": "Purpose and scope", "kicker": "01 · First", "blocks": ["x"]}],
                (),
                {"audited": True},
            ),
            ["slab-irrigation-strategy: missing non-empty REF_IDS"],
        ),
        (
            "RAW_REFERENCES does not exempt another paper",
            _fixture(
                "other-paper",
                [{"id": "one", "title": "Purpose and scope", "kicker": "01 · First", "blocks": ["x"]}],
                (),
                "<ol><li>Audited reference</li></ol>",
            ),
            ["other-paper: missing non-empty REF_IDS"],
        ),
        (
            "banned editorial framing",
            _fixture("editorial", [
                {"id": "start", "title": "Purpose and scope", "kicker": "01 · First", "blocks": ["x"]},
                {"id": "one", "title": "What this is", "kicker": "02 · Second", "blocks": ["x"]},
            ]),
            ["editorial: section 'one': banned editorial framing 'what this is' in title 'What this is'"],
        ),
        (
            "late Definitions",
            _fixture("late-definitions", [
                {"id": "start", "title": "Purpose and scope", "kicker": "01 · Start", "blocks": ["x"]},
                {"id": "method", "title": "Operating method", "kicker": "02 · Method", "blocks": ["x"]},
                {"id": "definitions", "title": "Definitions", "kicker": "03 · Definitions", "blocks": ["x"]},
            ]),
            ["late-definitions: 'Definitions' must be section 2, found section 3"],
        ),
        (
            "late Troubleshooting",
            _fixture("late-troubleshooting", [
                {"id": "start", "title": "Purpose and scope", "kicker": "01 · Start", "blocks": ["x"]},
                {"id": "definitions", "title": "Definitions", "kicker": "02 · Definitions", "blocks": ["x"]},
                {"id": "results", "title": "Expected results and limitations", "kicker": "03 · Results", "blocks": ["x"]},
                {"id": "troubleshooting", "title": "Troubleshooting", "kicker": "04 · Troubleshooting", "blocks": ["x"]},
            ]),
            ["late-troubleshooting: 'Troubleshooting' must precede 'Expected results and limitations'"],
        ),
        (
            "nonsequential kickers",
            _fixture("kicker-gap", [
                {"id": "start", "title": "Purpose and scope", "kicker": "01 · Start", "blocks": ["x"]},
                {"id": "next", "title": "Next section", "kicker": "03 · Next", "blocks": ["x"]},
            ]),
            ["kicker-gap: numeric kicker for section 'next' is 03; expected 02"],
        ),
        (
            "two-word title case",
            _fixture("two-word", [
                {"id": "start", "title": "Purpose and scope", "kicker": "01 · Start", "blocks": ["x"]},
                {"id": "water", "title": "Water Quality", "kicker": "02 · Water", "blocks": ["x"]},
            ]),
            ["two-word: section 'water': title is not sentence case: 'Water Quality'"],
        ),
        (
            "three-word title case",
            _fixture("three-word", [
                {"id": "start", "title": "Purpose and scope", "kicker": "01 · Start", "blocks": ["x"]},
                {"id": "water", "title": "Water Quality Standards", "kicker": "02 · Water", "blocks": ["x"]},
            ]),
            ["three-word: section 'water': title is not sentence case: 'Water Quality Standards'"],
        ),
        (
            "teaser question",
            _fixture("question", [
                {"id": "start", "title": "Purpose and scope", "kicker": "01 · Start", "blocks": ["x"]},
                {"id": "leds", "title": "Can LEDs save energy?", "kicker": "02 · LEDs", "blocks": ["x"]},
            ]),
            ["question: section 'leds': title must not contain '?': 'Can LEDs save energy?'"],
        ),
        (
            "allowed acronym",
            _fixture("acronym", [
                {"id": "start", "title": "Purpose and scope", "kicker": "01 · Start", "blocks": ["x"]},
                {"id": "ec", "title": "Root-zone EC", "kicker": "02 · EC", "blocks": ["x"]},
            ]),
            [],
        ),
        (
            "allowed digit-bearing token",
            _fixture("digit-token", [
                {"id": "start", "title": "Purpose and scope", "kicker": "01 · Start", "blocks": ["x"]},
                {"id": "sensor", "title": "Irrigation with TEROS-12", "kicker": "02 · Sensor", "blocks": ["x"]},
            ]),
            [],
        ),
        (
            "allowed proper-name exception",
            _fixture("daily-checks", [
                {"id": "start", "title": "Purpose and scope", "kicker": "01 · Start", "blocks": ["x"]},
                {"id": "autocomplete", "title": "Home Assistant check automation", "kicker": "02 · Automation", "blocks": ["x"]},
            ]),
            [],
        ),
        (
            "proper-name near miss",
            _fixture("daily-checks", [
                {"id": "start", "title": "Purpose and scope", "kicker": "01 · Start", "blocks": ["x"]},
                {"id": "autocomplete", "title": "Home Assistant automation", "kicker": "02 · Automation", "blocks": ["x"]},
            ]),
            ["daily-checks: section 'autocomplete': title is not sentence case: 'Home Assistant automation'"],
        ),
    ]
    for name, module, expected in fixtures:
        actual = validate_modules([module])
        assert actual == expected, f"{name}: expected {expected!r}, got {actual!r}"


def _run_corpus_check():
    # PAPER_MODULES is the single source of truth for the build's corpus order.
    from build import PAPER_MODULES

    modules = []
    diagnostics = []
    for module_name in PAPER_MODULES:
        try:
            modules.append(importlib.import_module(module_name))
        except Exception as error:
            diagnostics.append(f"{module_name}: failed to import: {error!r}")
    diagnostics.extend(validate_modules(modules))
    if diagnostics:
        for diagnostic in diagnostics:
            print(diagnostic)
        raise SystemExit(1)
    print(f"section-structure OK: {len(modules)} papers")


if __name__ == "__main__":
    if sys.argv[1:] == ["--self-test"]:
        _run_self_test()
        print("section-structure self-test OK")
    else:
        _run_corpus_check()
