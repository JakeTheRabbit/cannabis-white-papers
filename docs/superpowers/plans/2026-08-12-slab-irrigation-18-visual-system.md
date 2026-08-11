# Slab Irrigation 18-Module Visual System Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publish eighteen paired image-and-SVG teaching modules throughout the existing slab-irrigation field guide.

**Architecture:** A workspace integration script owns the module manifest, generates deterministic SVG diagrams, rewrites the packaged guide, and exports the source payload used by the canonical static-site build. Twelve new label-free raster masters join six existing masters; the site build copies optimized WebP derivatives from `_build/static`.

**Tech Stack:** Python 3.12, BeautifulSoup, Pillow, inline SVG/HTML/CSS, 9Router `openai/gpt-image-1`, the repository Python static-site generator, Playwright/Edge.

## Global Constraints

- Work directly on `C:\Github\white-papers` main because the user explicitly authorized pushing.
- Never stage the unrelated untracked `AGENTS.md`, `CLAUDE.md`, or `setpoints.html` files.
- Keep factual labels, measurements, rates, and annotations out of raster images.
- Preserve the neutral Athena/CCI fact-checked prose and all 17 citations.
- Maintain the live permalink `slab-irrigation-strategy.html`.

---

### Task 1: Add the visual-coverage contract

**Files:**
- Create: `C:\Users\BenIsdale\Documents\Codex\2026-08-12\referenced-chatgpt-conversation-this-is-an\work\test_visual_system_18.py`
- Modify: `C:\Users\BenIsdale\Documents\Codex\2026-08-12\referenced-chatgpt-conversation-this-is-an\work\test_published_slab_page.py`

**Interfaces:**
- Consumes: packaged guide HTML and canonical built page.
- Produces: assertions for 18 unique `data-concept` values, 18 images, 18 SVG diagrams, asset dimensions, coverage anchors, and mobile-safe markup.

- [ ] Write a failing test that expects exactly eighteen concept pairs and the eighteen required concept identifiers.
- [ ] Run the test against the current six-render guide and confirm failure because `concept-pair` does not exist.
- [ ] Extend the published-page test to assert the same contract for site-relative WebP assets.

### Task 2: Generate twelve new raster masters

**Files:**
- Modify: `outputs/assets/slab-irrigation-guide/asset-manifest.json`
- Create: twelve PNG files under `outputs/assets/slab-irrigation-guide/`.

**Interfaces:**
- Consumes: twelve prompts defined by the design coverage map.
- Produces: 1536 × 1024 label-free PNG masters with stable descriptive filenames and recorded prompts/hashes.

- [ ] Confirm the 9Router OpenAI image endpoint responds.
- [ ] Generate the twelve assets with one prompt per concept.
- [ ] Inspect all outputs for recognisable hardware, no legible generated labels, and consistent visual direction.
- [ ] Record provider, model, prompt, dimensions, and SHA-256 for all eighteen assets.

### Task 3: Build and integrate eighteen paired modules

**Files:**
- Create: `work/expand_visual_system.py`
- Modify: `outputs/slab-irrigation-field-guide.html`
- Modify: `outputs/slab-irrigation-strategy-athena-cci.html`
- Modify: `outputs/assets/slab-irrigation-guide/*.webp`

**Interfaces:**
- Consumes: the eighteen PNG masters and the existing guide DOM.
- Produces: `render_diagram(concept_id) -> str`, `render_pair(module) -> Tag`, and two byte-identical packaged HTML guides.

- [ ] Define the eighteen-module manifest with identifiers, headings, captions, image filenames, section targets, and insertion anchors.
- [ ] Implement eighteen deterministic SVG diagram functions with unique accessible titles and descriptions.
- [ ] Remove the six legacy overlay-only render figures and insert all eighteen paired modules at their teaching anchors.
- [ ] Add responsive pair CSS and convert all PNG masters to quality-88 WebP derivatives.
- [ ] Run the visual-coverage test until all package assertions pass.

### Task 4: Export through the canonical site source

**Files:**
- Modify: `work/export_slab_site_payload.py`
- Modify: `C:\Github\white-papers\_build\data\slab_irrigation_content.html`
- Modify: `C:\Github\white-papers\_build\static\slab-irrigation-guide\*.webp`
- Regenerate: canonical site outputs including `slab-irrigation-strategy.html`, search index, corpus, manifest, and archive.

**Interfaces:**
- Consumes: packaged guide and eighteen WebP assets.
- Produces: site payload with relative asset URLs and a complete canonical build.

- [ ] Update exporter assertions from six legacy renders to eighteen paired modules.
- [ ] Export the revised payload and copy all eighteen optimized assets to `_build/static`.
- [ ] Run `python _build/build.py` and require 38 live papers with no module errors and a clean leak scan.
- [ ] Run structural, link, citation, image, and `git diff --check` verification.

### Task 5: Browser verification and publication

**Files:**
- Modify: `work/verify_neutral_guide_browser.py`
- Create: screenshots under `work/render/` for local inspection only.

**Interfaces:**
- Consumes: packaged guide, canonical local build, and deployed URL.
- Produces: desktop/mobile measurements and deployment evidence.

- [ ] Verify 1440 px and 390 px layouts, 18 loaded images, 18 SVG diagrams, no overflow, visible mobile labels, theme switching, and search.
- [ ] Inspect representative room, physics, cycle, troubleshooting, and setpoint modules visually.
- [ ] Stage only intended files, commit, and push `main`.
- [ ] Wait for the GitHub Pages workflow to succeed.
- [ ] Run the browser verification against the public permalink and confirm the remote SHA matches `origin/main`.
