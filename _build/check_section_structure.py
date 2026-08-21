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
}
KICKER_NUMBER = re.compile(r"^\s*(\d{2})\s*·\s+\S")
TITLE_WORD = re.compile(r"[A-Za-z][A-Za-z0-9+–-]*")


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


def _violates_sentence_case(title):
    words = TITLE_WORD.findall(title)
    uppercase_words = [
        word for word in words[1:]
        if word[0].isupper() and not _is_acronym(word)
    ]
    return len(uppercase_words) >= 3


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
        if not _non_empty(ref_ids):
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
                banned = _has_banned_framing(title)
                if normalized_title == "expected results" or "realistic expectations" in normalized_title:
                    diagnostics.append(
                        f"{label}: section '{section_id}': must use canonical title "
                        f"'Expected results and limitations' instead of '{title}'"
                    )
                elif any(normalized_title.startswith(prefix) for prefix in DEFINITIONS_VARIANTS):
                    diagnostics.append(
                        f"{label}: section '{section_id}': must use canonical title "
                        f"'Definitions' instead of '{title}'"
                    )
                elif banned:
                    diagnostics.append(
                        f"{label}: section '{section_id}': banned editorial framing "
                        f"'{banned}' in title '{title}'"
                    )
                if _violates_sentence_case(title):
                    diagnostics.append(f"{label}: section '{section_id}': title is not sentence case: '{title}'")

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


def _fixture(slug, sections, ref_ids=("ref",)):
    return SimpleNamespace(SLUG=slug, SECTIONS=sections, REF_IDS=list(ref_ids))


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
    print("section-structure OK: 55 papers")


if __name__ == "__main__":
    if sys.argv[1:] == ["--self-test"]:
        _run_self_test()
        print("section-structure self-test OK")
    else:
        _run_corpus_check()
