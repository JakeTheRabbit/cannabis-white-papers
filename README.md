# The Cannabis White Papers

A beginner-first field guide: peer-reviewed cannabis cultivation science, rewritten so
someone new to growing can actually understand it. Every paper defines its terms, shows
its working in diagrams/tables, and cites its sources. Static site, works offline,
deploys to GitHub Pages.

## Status — complete

| | |
|---|---|
| Theme | Variant B — charcoal monochrome + serif; green reserved for diagrams only. Light + **dark mode** (toggle, persisted, honours `prefers-color-scheme`). |
| Live papers | **29**, grouped by grow stage: Propagation, Vegetative, Flowering, Harvest/Dry/Trim/Cure, plus the systems that run across every stage (Environment, Water & feed, Plant health, Precision, Facility) |
| Citations | 160 sources in one registry (mostly peer-reviewed; manufacturer/operational sources labelled) |
| Glossary | 256 plain-English terms |
| Search | Offline command palette (Ctrl/Cmd-K) over every paper, section and term |
| Images | 35 AI-generated example photos/diagrams (Nano Banana 2, GPT Image 2, Cinema Studio via Higgsfield CLI) embedded across all 21 papers; web-optimised JPGs in `assets/img/` (~6.7 MB). Regenerate via `python gen_images.py` (resumable); manifest in `_build/images.py`. |
| Pages | `index.html` (landing), `papers.html` (library), `glossary.html`, one page per paper |
| Deploy | Local build only — not yet pushed (run from `_build/`) |

## How it's built

A small Python build system renders every page through one shared template, so theme,
tone, navigation, glossary and citations stay identical across all papers.

```
_build/
  build.py              orchestrator → emits the site to repo root
  theme.py              the stylesheet (assets/app.css)
  shell.py              page chrome: sidebar, mobile top bar, bottom thumb-nav, rail, search modal
  components.py         block helpers (callout, table, figure, steps…) + inline-SVG icons
  app_js.py             client JS: command-palette search, mobile drawer, scrollspy (assets/app.js)
  figs.py, figs_extra.py   hand-authored inline-SVG figures
  paper_*.py            one module per paper (content)
  data/
    nav.py              the full paper manifest → drives nav everywhere
    glossary.py         site-wide term → plain-English definitions
    refs.py             citation registry (peer-reviewed sources), reused across papers
```

### Rebuild

```
cd _build && python build.py
```

### Add a paper (Phase 2+)

1. Create `_build/paper_<slug>.py` (copy an existing one; set `SLUG, TITLE, EYEBROW, SUB, META, SECTIONS, REF_IDS, RELATED`).
2. Add its figures to `figs*.py`.
3. Flip its `status` to `"live"` in `data/nav.py` and add the module to `PAPERS` in `build.py`.
4. `python build.py`, then render-verify.

## Design system

- **Chrome** (nav, hero, pills, buttons): charcoal monochrome, serif display type.
- **Diagrams/data**: green family + amber/red status — the only colour on the page.
- **Mobile**: sidebar collapses to a drawer; a bottom thumb-bar (Home · Papers · Search · Terms · Menu) stays in reach.
- **Search**: Ctrl/Cmd-K command palette over every paper, section and glossary term. Index is inlined (`assets/search-index.js`) so it works from `file://` with no server.

## Sources

Every factual claim is cited inline `[n]` to a per-paper References list. Peer-reviewed
where possible; manufacturer/operational sources are labelled as such. Cannabis tissue
culture is strongly genotype-dependent — verify dilutions, hormone doses and local
regulations against the primary sources before relying on them.

*Not legal advice. Follow the cannabis laws in your jurisdiction.*
