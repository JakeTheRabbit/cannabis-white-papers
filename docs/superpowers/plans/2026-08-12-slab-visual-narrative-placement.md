# Slab Visual Narrative Placement Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Reposition all 18 slab-irrigation visual modules at their exact narrative teaching points and remove the detached-gallery presentation.

**Architecture:** Extend the local visual-system generator with explicit DOM anchor relations for every module. Guard the structure with adjacency tests, then export the verified standalone payload into the canonical static-site source and rebuild all generated outputs.

**Tech Stack:** Python 3.12, BeautifulSoup, inline SVG, HTML/CSS, Playwright, GitHub Pages.

## Global Constraints

- Preserve exactly 18 unique image-plus-SVG modules.
- Preserve neutral Athena/CCI fact-checked copy and all 17 references.
- Do not stage untracked `AGENTS.md`, `CLAUDE.md`, or `setpoints.html`.
- Push only after local build, structural, desktop, and phone checks pass.

---

### Task 1: Encode semantic placement requirements

**Files:**
- Modify: `work/test_visual_system_18.py`
- Modify: `work/expand_visual_system.py`

**Interfaces:**
- Consumes: existing `MODULES` visual metadata and standalone guide DOM.
- Produces: explicit anchor selectors and `before`/`after` relations for all 18 modules.

- [ ] Add adjacency assertions for all 18 visual modules.
- [ ] Run the test and confirm the current section-end layout fails.
- [ ] Replace section append logic with semantic anchor insertion.
- [ ] Remove global concept numbering and repetitive disclaimer copy.
- [ ] Regenerate both standalone HTML deliverables and rerun structural tests.

### Task 2: Export and verify the canonical site

**Files:**
- Modify: `_build/data/slab_irrigation_content.html`
- Modify: generated site and corpus outputs from `_build/build.py`

**Interfaces:**
- Consumes: verified standalone guide HTML and 18 WebP assets.
- Produces: canonical public page with the same adjacency structure.

- [ ] Export the standalone guide payload into `_build/data`.
- [ ] Run `python _build/build.py`.
- [ ] Run page structure, content-neutrality, link, asset, and browser tests.
- [ ] Inspect representative desktop and phone captures.

### Task 3: Publish and live-verify

**Files:**
- Commit only intended source, generated outputs, and design/plan documents.

**Interfaces:**
- Consumes: verified canonical repository state.
- Produces: deployed GitHub Pages correction.

- [ ] Run `git diff --check` and audit staged files.
- [ ] Commit and push `main`.
- [ ] Wait for the Pages deployment workflow to succeed.
- [ ] Run the full browser verification against the public URL.
