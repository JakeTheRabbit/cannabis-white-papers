"""Validate committed/generated white-paper outputs against authoritative modules."""

from __future__ import annotations

import html
from html.parser import HTMLParser
import importlib
import json
from pathlib import Path
import re
import sys
from collections import Counter
from urllib.parse import unquote


VOID_TAGS = {
    "area", "base", "br", "col", "embed", "hr", "img", "input", "link",
    "meta", "param", "source", "track", "wbr",
}
SOURCE_NOTE_OVERRIDES = {
    ("cannabis-tissue-culture-playbook", "sources"): "Evidence sources and image methods",
    ("cannabis-tissue-culture-sop", "sources"): "Source notes",
}


def _attrs(items):
    return {key: value or "" for key, value in items}


class GeneratedPageParser(HTMLParser):
    """Collect document structure while deliberately ignoring IDs inside SVGs."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.svg_depth = 0
        self.document_ids = []
        self.fragments = []
        self.h2 = []
        self.figure_numbers = []
        self.images = []
        self.toc_links = []
        self.rail_links = []
        self.emphasis = {"strong": [0, 0], "em": [0, 0]}
        self._h2_capture = None
        self._figure_capture = None
        self._nav_capture = None

    def _ancestor_id(self, tag=None):
        for entry in reversed(self.stack):
            if (tag is None or entry["tag"] == tag) and entry["id"]:
                return entry["id"]
        return None

    def _nav_context(self):
        for entry in reversed(self.stack):
            if "toc" in entry["classes"]:
                return "toc"
            if entry["tag"] == "aside" and "rail" in entry["classes"]:
                return "rail"
        return None

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        attr = _attrs(attrs)
        classes = set(attr.get("class", "").split())
        if tag == "svg":
            self.svg_depth += 1
        element_id = attr.get("id")
        if element_id and self.svg_depth == 0:
            self.document_ids.append(element_id)
        if tag == "a" and attr.get("href", "").startswith("#"):
            self.fragments.append(unquote(attr["href"][1:]))
        if tag in self.emphasis:
            self.emphasis[tag][0] += 1
        if tag == "h2":
            self._h2_capture = [self._ancestor_id(), []]
        if "fignum" in classes:
            self._figure_capture = []
        if tag == "a":
            context = self._nav_context()
            if context:
                self._nav_capture = [context, attr.get("href", ""), []]
        if tag == "img":
            self.images.append((attr.get("src", ""), self._ancestor_id("section")))
        if tag not in VOID_TAGS:
            self.stack.append({
                "tag": tag,
                "id": element_id,
                "classes": classes,
            })

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag.lower() not in VOID_TAGS:
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag == "h2" and self._h2_capture is not None:
            parent_id, parts = self._h2_capture
            self.h2.append((parent_id, "".join(parts).strip()))
            self._h2_capture = None
        if self._figure_capture is not None:
            for index in range(len(self.stack) - 1, -1, -1):
                entry = self.stack[index]
                if entry["tag"] == tag and "fignum" in entry["classes"]:
                    label = "".join(self._figure_capture).strip()
                    match = re.fullmatch(r"Figure\s+(\d+)\.?", label)
                    if match:
                        self.figure_numbers.append(int(match.group(1)))
                    self._figure_capture = None
                    break
        if tag == "a" and self._nav_capture is not None:
            context, href, parts = self._nav_capture
            record = (href, "".join(parts).strip())
            (self.toc_links if context == "toc" else self.rail_links).append(record)
            self._nav_capture = None
        if tag in self.emphasis:
            self.emphasis[tag][1] += 1
        for index in range(len(self.stack) - 1, -1, -1):
            if self.stack[index]["tag"] == tag:
                del self.stack[index:]
                break
        if tag == "svg":
            self.svg_depth = max(0, self.svg_depth - 1)

    def handle_data(self, data):
        if self._h2_capture is not None:
            self._h2_capture[1].append(data)
        if self._figure_capture is not None:
            self._figure_capture.append(data)
        if self._nav_capture is not None:
            self._nav_capture[2].append(data)


def _plain_title(title):
    return html.unescape(re.sub(r"<[^>]+>", "", title)).strip()


def _expected_rendered_sections(source_sections):
    expected = list(source_sections)
    definitions = next(
        (index for index, (_, title) in enumerate(expected) if title == "Definitions"),
        None,
    )
    insertion = definitions + 1 if definitions is not None else 1
    expected.insert(insertion, ("evidence-notes", "Evidence and limitations"))
    expected.append(("references", "References"))
    return expected


def _parse_page(text):
    parser = GeneratedPageParser()
    parser.feed(text)
    parser.close()
    return parser


def _document_diagnostics(slug, text, source_sections, image_parent_expectations=()):
    from check_section_structure import validate_title_policy

    diagnostics = []
    page = _parse_page(text)
    expected = _expected_rendered_sections(source_sections)
    actual = [(section_id, _plain_title(title)) for section_id, title in page.h2]
    actual_titles = [title for _, title in actual]

    if not actual_titles or actual_titles[0] != "Purpose and scope":
        found = actual_titles[0] if actual_titles else None
        diagnostics.append(f"{slug}: first source H2 must be 'Purpose and scope', found {found!r}")
    reference_h2 = [(parent, title) for parent, title in actual if title == "References"]
    if len(reference_h2) != 1 or reference_h2[0][0] != "references":
        diagnostics.append(
            f"{slug}: expected exactly one References H2 under #references, found {reference_h2!r}"
        )
    if not actual_titles or actual_titles[-1] != "References":
        diagnostics.append(f"{slug}: References must be the final H2")
    if actual != expected:
        diagnostics.append(
            f"{slug}: rendered H2 sequence differs from authoritative source plus Evidence/References"
        )

    definitions = next(
        (index for index, (_, title) in enumerate(actual) if title == "Definitions"),
        None,
    )
    evidence = [index for index, (_, title) in enumerate(actual) if title == "Evidence and limitations"]
    expected_evidence = definitions + 1 if definitions is not None else 1
    if evidence != [expected_evidence]:
        anchor = "'Definitions'" if definitions is not None else "'Purpose and scope'"
        diagnostics.append(f"{slug}: Evidence and limitations must follow {anchor}")

    duplicate_ids = sorted(
        element_id for element_id, count in Counter(page.document_ids).items() if count > 1
    )
    if duplicate_ids:
        diagnostics.append(f"{slug}: duplicate non-SVG document IDs: {duplicate_ids!r}")
    if page.document_ids.count("references") != 1:
        diagnostics.append(
            f"{slug}: expected exactly one #references anchor, found "
            f"{page.document_ids.count('references')}"
        )
    id_set = set(page.document_ids)
    unresolved = sorted(set(fragment for fragment in page.fragments if not fragment or fragment not in id_set))
    if unresolved:
        diagnostics.append(f"{slug}: unresolved same-page fragments: {unresolved!r}")
    for tag, (opening, closing) in page.emphasis.items():
        if opening != closing:
            diagnostics.append(
                f"{slug}: unbalanced <{tag}> tags: {opening} opening / {closing} closing"
            )
    expected_figures = list(range(1, len(page.figure_numbers) + 1))
    if page.figure_numbers != expected_figures:
        diagnostics.append(
            f"{slug}: visible Figure labels {page.figure_numbers!r} are not contiguous "
            f"from 1 ({expected_figures!r})"
        )
    for nav_name, links in (("contents", page.toc_links), ("rail", page.rail_links)):
        reference_links = [href for href, _ in links if href == "#references"]
        if len(reference_links) != 1 or not links or links[-1][0] != "#references":
            diagnostics.append(
                f"{slug}: References must be the single final item in {nav_name} navigation"
            )

    for section_id, title in actual:
        diagnostics.extend(validate_title_policy(slug, section_id, title))

    image_locations = {}
    for src, parent in page.images:
        image_locations.setdefault(src, []).append(parent)
    for src, expected_parent in image_parent_expectations:
        actual_parents = image_locations.get(src, [])
        if actual_parents != [expected_parent]:
            diagnostics.append(
                f"{slug}: image {src!r} parent {actual_parents!r}; expected [{expected_parent!r}]"
            )
    return diagnostics, page


def validate_document(slug, text, source_sections, image_parent_expectations=()):
    """Validate one generated paper document; useful for focused external checks."""
    return _document_diagnostics(slug, text, source_sections, image_parent_expectations)[0]


def _headings(markdown):
    return [match.group(1).strip() for match in re.finditer(r"^##\s+(.+)$", markdown, re.M)]


def _search_sections(root):
    path = root / "assets" / "search-index.js"
    if not path.exists():
        return None, ["search-index.js: missing generated search index"]
    text = path.read_text(encoding="utf-8")
    match = re.match(r"window\.SEARCH_INDEX=(.*?);\s*window\.SEARCH_SYN=", text, re.S)
    if not match:
        return None, ["search-index.js: cannot locate SEARCH_INDEX JSON"]
    try:
        records = json.loads(match.group(1))
    except json.JSONDecodeError as error:
        return None, [f"search-index.js: invalid SEARCH_INDEX JSON: {error}"]
    by_slug = {}
    for record in records:
        if record.get("type") != "section":
            continue
        url = record.get("url", "")
        match = re.fullmatch(r"([^/#]+)\.html#(.+)", url)
        if not match:
            continue
        slug, section_id = match.groups()
        by_slug.setdefault(slug, []).append((section_id, _plain_title(record.get("title", ""))))
    return by_slug, []


def _llms_headings(text, paper_title):
    marker = re.compile(rf"^#\s+{re.escape(_plain_title(paper_title))}\s*$", re.M)
    match = marker.search(text)
    if not match:
        return None
    end = text.find("\n\n---\n\n", match.end())
    chunk = text[match.end():] if end == -1 else text[match.end():end]
    return _headings(chunk)


def _legacy_image_expectations(root, module, registry):
    """Map legacy post-evidence manifest indices to stable source-section parents."""
    source = [(section["id"], _plain_title(section["title"])) for section in module.SECTIONS]
    virtual = source
    if source:
        virtual = [source[0], ("evidence-notes", "Evidence and limitations"), *source[1:]]
    expectations = []
    for entry in registry.by_slug().get(module.SLUG, []):
        if entry.get("ext"):
            candidates = [f"{entry['slug']}-{entry['n']}.{entry['ext']}"]
        else:
            candidates = [
                f"{entry['slug']}-{entry['n']}.jpg",
                f"{entry['slug']}-{entry['n']}.svg",
                f"{entry['slug']}-{entry['n']}.png",
            ]
        filename = next(
            (candidate for candidate in candidates if (root / "assets" / "img" / candidate).exists()),
            None,
        )
        if filename and virtual:
            index = max(0, min(entry["sec"], len(virtual) - 1))
            expectations.append((f"assets/img/{filename}", virtual[index][0]))
    return expectations


def validate_generated_structure(root, modules):
    """Return diagnostics for the built repository rooted at *root*."""
    from check_section_structure import validate_title_policy
    import images as image_registry

    root = Path(root)
    diagnostics = []
    module_slugs = [module.SLUG for module in modules]
    if len(module_slugs) != 55 or len(set(module_slugs)) != 55:
        diagnostics.append(
            f"loaded modules: expected 55 unique slugs, got {len(module_slugs)} total / "
            f"{len(set(module_slugs))} unique"
        )

    manifest_path = root / "manifest.json"
    manifest_slugs = []
    if not manifest_path.exists():
        diagnostics.append("manifest.json: missing generated manifest")
    else:
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest_slugs = [paper["slug"] for paper in manifest.get("papers", [])]
            if manifest.get("count") != len(manifest_slugs):
                diagnostics.append(
                    f"manifest.json: count {manifest.get('count')!r} does not match "
                    f"{len(manifest_slugs)} paper records"
                )
        except (json.JSONDecodeError, KeyError, TypeError) as error:
            diagnostics.append(f"manifest.json: invalid manifest: {error}")
    if len(manifest_slugs) != 55 or len(set(manifest_slugs)) != 55:
        diagnostics.append(
            f"manifest.json: expected 55 unique slugs, got {len(manifest_slugs)} total / "
            f"{len(set(manifest_slugs))} unique"
        )
    if set(manifest_slugs) != set(module_slugs):
        diagnostics.append("manifest.json: slug set differs from successfully loaded paper modules")

    search_by_slug, search_diagnostics = _search_sections(root)
    diagnostics.extend(search_diagnostics)
    llms_path = root / "llms-full.txt"
    llms_text = llms_path.read_text(encoding="utf-8") if llms_path.exists() else None
    if llms_text is None:
        diagnostics.append("llms-full.txt: missing generated full corpus")

    for module in modules:
        slug = module.SLUG
        source_sections = [
            (section["id"], _plain_title(section["title"])) for section in module.SECTIONS
        ]
        expected_text_titles = [title for _, title in source_sections] + ["References"]
        html_path = root / f"{slug}.html"
        if not html_path.exists():
            diagnostics.append(f"{slug}: missing generated paper HTML")
        else:
            image_expectations = _legacy_image_expectations(root, module, image_registry)
            page_diagnostics, _ = _document_diagnostics(
                slug,
                html_path.read_text(encoding="utf-8"),
                source_sections,
                image_expectations,
            )
            diagnostics.extend(page_diagnostics)

        markdown_path = root / "papers" / f"{slug}.md"
        markdown_titles = None
        if not markdown_path.exists():
            diagnostics.append(f"{slug}: missing generated Markdown paper")
        else:
            markdown_titles = _headings(markdown_path.read_text(encoding="utf-8"))
            if markdown_titles != expected_text_titles:
                diagnostics.append(f"{slug}: Markdown H2 titles differ from authoritative source")

        expected_search = source_sections
        actual_search = search_by_slug.get(slug, []) if search_by_slug is not None else None
        if actual_search is not None and actual_search != expected_search:
            diagnostics.append(f"{slug}: search-index section records differ from authoritative source")

        llms_titles = _llms_headings(llms_text, module.TITLE) if llms_text is not None else None
        if llms_titles is not None and llms_titles != expected_text_titles:
            diagnostics.append(f"{slug}: llms-full H2 titles differ from authoritative source")
        elif llms_text is not None and llms_titles is None:
            diagnostics.append(f"{slug}: paper missing from llms-full.txt")

        for surface, records in (
            ("Markdown", list(zip([section_id for section_id, _ in source_sections] + ["references"], markdown_titles or []))),
            ("search index", actual_search or []),
            ("llms-full", list(zip([section_id for section_id, _ in source_sections] + ["references"], llms_titles or []))),
        ):
            for section_id, title in records:
                for error in validate_title_policy(slug, section_id, title):
                    diagnostics.append(f"{surface}: {error}")

    module_by_slug = {module.SLUG: module for module in modules}
    for (slug, section_id), expected_title in SOURCE_NOTE_OVERRIDES.items():
        module = module_by_slug.get(slug)
        actual_title = None
        if module is not None:
            actual_title = next(
                (section.get("title") for section in module.SECTIONS if section.get("id") == section_id),
                None,
            )
        if actual_title != expected_title:
            diagnostics.append(
                f"{slug}: source-note override {section_id!r} is {actual_title!r}; "
                f"expected {expected_title!r}"
            )
    return diagnostics


def _fixture_page(rendered_sections, extra=""):
    toc = "".join(f'<a href="#{section_id}">{title}</a>' for section_id, title in rendered_sections)
    rail = "".join(f'<a href="#{section_id}">{title}</a>' for section_id, title in rendered_sections)
    body = []
    for section_id, title in rendered_sections:
        if section_id == "references":
            body.append(f'<div class="refs" id="references"><h2>{title}</h2></div>')
        else:
            body.append(f'<section id="{section_id}"><h2>{title}</h2></section>')
    return (
        f'<div class="toc">{toc}</div>{"".join(body)}{extra}'
        f'<aside class="rail">{rail}</aside>'
    )


def _run_self_test():
    source = [("start", "Purpose and scope")]
    rendered = _expected_rendered_sections(source)
    valid = _fixture_page(rendered)
    assert validate_document("fixture", valid, source) == []

    cases = [
        (
            "duplicate IDs",
            valid.replace('</section>', '<div id="start"></div></section>', 1),
            source,
            (),
            "duplicate non-SVG document IDs",
        ),
        (
            "broken fragments",
            valid.replace('<div class="toc">', '<div class="toc"><a href="#missing">Missing</a>'),
            source,
            (),
            "unresolved same-page fragments",
        ),
        (
            "wrong References level",
            valid.replace("<h2>References</h2>", "<h3>References</h3>"),
            source,
            (),
            "expected exactly one References H2",
        ),
        (
            "wrong References order",
            _fixture_page([
                ("start", "Purpose and scope"),
                ("references", "References"),
                ("evidence-notes", "Evidence and limitations"),
            ]),
            source,
            (),
            "References must be the final H2",
        ),
        (
            "evidence misplacement",
            _fixture_page([
                ("start", "Purpose and scope"),
                ("evidence-notes", "Evidence and limitations"),
                ("definitions", "Definitions"),
                ("references", "References"),
            ]),
            [("start", "Purpose and scope"), ("definitions", "Definitions")],
            (),
            "Evidence and limitations must follow 'Definitions'",
        ),
        (
            "figure gap",
            valid.replace(
                "</section>",
                '<figcaption><span class="fignum">Figure 2.</span> Gap</figcaption></section>',
                1,
            ),
            source,
            (),
            "visible Figure labels [2] are not contiguous",
        ),
        (
            "title mismatch",
            valid.replace("Purpose and scope", "Purpose and Scope"),
            source,
            (),
            "rendered H2 sequence differs from authoritative source",
        ),
        (
            "image-parent mismatch",
            valid.replace("</section>", '<img src="assets/img/test.jpg"></section>', 1),
            source,
            (("assets/img/test.jpg", "target"),),
            "image 'assets/img/test.jpg' parent ['start']; expected ['target']",
        ),
    ]
    for name, text, fixture_source, image_expectations, expected in cases:
        errors = validate_document("fixture", text, fixture_source, image_expectations)
        assert any(expected in error for error in errors), (
            f"{name}: expected diagnostic containing {expected!r}, got {errors!r}"
        )


def _load_modules_for_cli():
    build = importlib.import_module("build")
    diagnostics = build.validate_paper_imports(
        build.PAPER_MODULES,
        build.PAPERS,
        build.PAPER_ERRORS,
    )
    return build.PAPERS, diagnostics, Path(build.ROOT)


def main():
    if sys.argv[1:] == ["--self-test"]:
        _run_self_test()
        print("generated-structure self-test OK")
        return 0
    modules, diagnostics, root = _load_modules_for_cli()
    diagnostics.extend(validate_generated_structure(root, modules))
    if diagnostics:
        for diagnostic in diagnostics:
            print(diagnostic)
        return 1
    print(f"generated-structure OK: {len(modules)} papers")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
