# White-paper Section Title System Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Standardise H2 titles and topic-aware section order across all 55 white papers without changing technical claims or public anchors.

**Architecture:** Keep each paper module as the source of truth, add one read-only structure validator, and rebuild all generated outputs through the existing Python static-site pipeline. Shared injected evidence headings are corrected in the build/export layer; paper-specific headings and ordering are corrected in their own modules.

**Tech Stack:** Python 3.12, repository section-dictionary DSL, PowerShell, GitHub Pages

**Spec:** `docs/superpowers/specs/2026-08-22-white-paper-section-title-system-design.md`

## Global Constraints

- Use sentence case and direct, literal H2 wording.
- Use `Purpose and scope`, `Definitions`, `Troubleshooting`, `Expected results and limitations`, and `References` when those labels accurately describe the whole section.
- Preserve every paper slug and existing section `id` value.
- Reorder sections only when the topic reads or operates better in the new order.
- Do not alter body claims, citations, paper titles, unrelated navigation, imagery, or theme code.
- Edit authoritative `_build` sources only; regenerate root outputs with `python _build/build.py`.
- Never stage `AGENTS.md`, `CLAUDE.md`, or `setpoints.html`.

---

### Task 1: Record the approved architecture

**Files:**
- Create: `docs/superpowers/specs/2026-08-22-white-paper-section-title-system-design.md`
- Create: `docs/superpowers/plans/2026-08-22-white-paper-section-title-system.md`

**Interfaces:**
- Consumes: the approved title and order rules from the design discussion
- Produces: binding requirements for all implementation and review tasks

- [ ] **Step 1: Verify the design captures the approved middle path**

Run: `rg -n "topic|sentence case|Preserve|Definitions|Troubleshooting|Expected results" docs/superpowers/specs/2026-08-22-white-paper-section-title-system-design.md`

Expected: each approved constraint appears in the design.

- [ ] **Step 2: Verify the plan contains no placeholders**

Run: `$terms = @(('T'+'BD'), ('T'+'ODO'), ('implement'+' later'), ('fill in'+' details')); Select-String -Path docs/superpowers/plans/2026-08-22-white-paper-section-title-system.md -Pattern $terms`

Expected: no matches.

- [ ] **Step 3: Commit the architecture**

```powershell
git add docs/superpowers/specs/2026-08-22-white-paper-section-title-system-design.md docs/superpowers/plans/2026-08-22-white-paper-section-title-system.md
git commit -m "docs: define white-paper section title system"
```

### Task 2: Add the structure-policy validator

**Files:**
- Create: `_build/check_section_structure.py`
- Modify: `_build/build.py`

**Interfaces:**
- Consumes: `PAPER_MODULES`, each module's `SLUG` and `SECTIONS`, and the canonical rules in the spec
- Produces: `validate_modules(modules: list[object]) -> list[str]`, where an empty list means the corpus complies

- [ ] **Step 1: Write checker self-tests that contain known-bad fixtures**

Create in-module tests for a duplicate ID, missing reference metadata, banned framing, misordered definitions, troubleshooting after expectations, and skipped numeric kickers. Each fixture must assert the exact diagnostic returned by `validate_modules`.

- [ ] **Step 2: Run the self-tests and verify they fail before implementation**

Run: `python _build/check_section_structure.py --self-test`

Expected: non-zero exit because the validator is not yet implemented.

- [ ] **Step 3: Implement the validator and explicit exception table**

The checker must load the same paper modules as `_build/build.py`, validate stable section metadata without mutating it, print one diagnostic per failure, and support `--self-test` plus a normal corpus check.

- [ ] **Step 4: Run the self-tests**

Run: `python _build/check_section_structure.py --self-test`

Expected: `section-structure self-test OK` and exit 0.

- [ ] **Step 5: Wire the corpus check into the build before export**

Import `validate_modules` in `_build/build.py`, validate `PAPERS`, and raise `SystemExit` with the diagnostics before generated files are written.

- [ ] **Step 6: Demonstrate the current corpus fails against the new policy**

Run: `python _build/check_section_structure.py`

Expected: non-zero exit with title/order diagnostics from existing paper sources.

### Task 3: Standardise shared and paper-specific sections

**Files:**
- Modify: `_build/build.py`
- Modify: `_build/export_corpus.py`
- Modify: every `_build/paper_*.py` module listed in `_build/build.py::PAPER_MODULES` whose audit identifies a title or order defect

**Interfaces:**
- Consumes: the approved spec, agent audits, and validator diagnostics
- Produces: compliant `SECTIONS` lists with unchanged IDs and body blocks

- [ ] **Step 1: Change the shared evidence title**

Replace the injected/exported title `Accuracy, self-review, and grain-of-salt notes` with `Evidence and limitations`. Keep its existing section ID.

- [ ] **Step 2: Apply exact audited title replacements**

Edit only each affected section's `title` value. Keep technical capitalization such as CO2, EC, VPD, HVAC, GMP, P0–P3, and cultivar names where required.

- [ ] **Step 3: Apply audited topic-dependent ordering changes**

Move complete section dictionaries without changing their IDs or blocks. Update only numeric kicker prefixes and figure numbering made inconsistent by a move.

- [ ] **Step 4: Verify no section IDs changed**

Compare the pre-change and post-change per-module ordered ID sets. Expected: identical sets for all 55 modules; only order may differ.

- [ ] **Step 5: Run the corpus policy check**

Run: `python _build/check_section_structure.py`

Expected: `section-structure OK: 55 papers` and exit 0.

### Task 4: Rebuild and validate generated outputs

**Files:**
- Regenerate: root `*.html`, `papers/*.md`, `assets/search-index.js`, `manifest.json`, `llms*.txt`, `README.md`, bundles, and archives produced by `_build/build.py`

**Interfaces:**
- Consumes: compliant paper modules and shared build titles
- Produces: deployable static corpus

- [ ] **Step 1: Build all papers**

Run: `python _build/build.py`

Expected: `build OK` and `live papers: 55`, with no module errors or leak-scan failure.

- [ ] **Step 2: Re-run the policy check after the build**

Run: `python _build/check_section_structure.py`

Expected: `section-structure OK: 55 papers`.

- [ ] **Step 3: Verify generated coverage and forbidden old titles**

Run corpus searches against root HTML, `papers/*.md`, `assets/search-index.js`, and `llms-full.txt`. Expected: all 55 outputs contain the new titles and no banned generic variants remain.

- [ ] **Step 4: Verify structural integrity**

Check balanced `<strong>` and `<em>` tags in all generated paper HTML, unique section IDs, valid local fragment links, and sequential figure numbers. Expected: zero failures.

- [ ] **Step 5: Review the generated diff**

Run `git diff --check`, `git diff --stat`, and targeted diffs for source modules plus representative generated outputs. Expected: no whitespace errors or unrelated changes.

### Task 5: Commit, push, and prove the live deployment

**Files:**
- Commit: tracked files changed by Tasks 2–4

**Interfaces:**
- Consumes: verified source and generated outputs
- Produces: a deployed and independently verified GitHub Pages corpus

- [ ] **Step 1: Stage tracked changes only**

Run: `git add -u`

Expected: `AGENTS.md`, `CLAUDE.md`, and `setpoints.html` remain untracked and unstaged.

- [ ] **Step 2: Commit the implementation**

Run: `git commit -m "refactor: standardize paper section titles"`

Expected: one implementation commit containing only in-scope tracked files.

- [ ] **Step 3: Push the explicitly approved main branch**

Run: `git push origin main`

Expected: remote `main` advances to the implementation commit.

- [ ] **Step 4: Wait for the matching Pages build**

Query the GitHub Pages workflow/API until the build for the pushed commit succeeds or fails. Do not infer deployment from the push result.

- [ ] **Step 5: Verify the live corpus**

Fetch all 55 cache-busted live paper URLs. Expected: HTTP 200, new canonical headings present, banned variants absent, unique anchors, and balanced emphasis tags on every page.
