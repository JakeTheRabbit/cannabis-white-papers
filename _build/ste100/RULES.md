# Rewriting a paper in ASD-STE100 (Issue 9) — working guide

Read this whole file, then `SUBSTITUTIONS.md` (frequent words and what to write instead) and `EXAMPLES.md`.
Source of the rules: ASD-STE100 Issue 9 (2025-01-15): 53 writing rules in 9 sections and a dictionary of 875 approved words.
The linter checks what a machine can check. A clean lint is **not** certification: you are also the reviewer.
**The tools are frozen while the rewrite runs.** If a tool misbehaves, report it in your final reply; do not work around it silently.

## 1. The job

Rewrite **all prose** of one paper (`_build/paper_<name>.py`) into STE. Keep the paper, change the language.

**Must stay exactly the same** (tools check most of this):
- every fact, number, unit, range, threshold, named product or standard; every caveat and hedge ("in some cases", "no studies show") — keep the hedge, say it in STE;
- every citation placeholder `⟦c:…⟧` and every other placeholder `⟦e1⟧` (you may move one to the end of the sentence it supports);
- section ids and order, table shapes, list lengths, the number of figures, figure numbers, internal links (`<a href=…>`);
- the teaching order: a term is defined where it first appears; Definitions stay definitions;
- inline HTML (`<strong>`, `<em>`, `&times;`, `&deg;` …): keep it and move it with the words it marks.

**Never** add facts, numbers, advice or sources. If a sentence cannot be said in STE without losing meaning, split it, recast it, or use a technical noun (section 4). Do not delete content to make the lint pass. Remove decoration (analogies, jokes, idioms) when it needs unapproved words; keep the literal mechanism.

**Fixed wording across the site** (so that 55 papers agree):
- Level label (EYEBROW / META): `Beginner` → `Basic`.
- META sources label: `Evidence-linked · N sources` and similar → `N sources`.
- META reading time: `~N min read` → `~N min to read`. Diagram count: `N diagrams` (keep). The build finds these labels by the words `read` and `diagram`: keep both words, same position, same numbers.
- EYEBROW keeps the `·` separator (the build splits on it).
- SUB: its first sentence is the card blurb on the home page (max ~165 characters): make it complete and short.
- Evidence labels: `Solid`, `Grower method`, `Weak` replace `solid science`, `operational` / `grower practice`, `grain of salt` (callout titles and `<span class='ev-tag'>…</span>`; keep the markup).
- `Borderline:` → `Limit of the data:`.
- Mandated section titles stay exactly: `Purpose and scope` (always the first section), `Definitions`, `Troubleshooting`, `Expected results and limitations`, `References`. Other titles: sentence case, no final period, no teaser questions (`check_section_structure.py` enforces this).

## 2. Workflow (PY = `C:\Tools\ste-lint\.venv\Scripts\python.exe`; repo root = `C:\Github\cannabis-white-papers`; never `cd` out of it; do NOT run `_build/build.py`; do NOT commit)

1. `PY _build/ste100/ste_units.py extract paper_<name>` (skip if `work/paper_<name>/units.txt` already exists) → `_build/ste100/work/paper_<name>/units.txt`: one `@@ Uxxxx | kind | ctx` header per text unit, the text on the next line.
2. Read `units.txt` in chunks (in order: the section context matters).
3. Rewrite **by writing part files**: `work/paper_<name>/part_01.txt`, `part_02.txt` … Each holds a run of units: header line copied exactly, new text below it, one blank line between units, at most ~60 units per file. Units you do not change you leave out.
4. `PY _build/ste100/ste_merge.py paper_<name>` merges all `part_*.txt` / `fix_*.txt` into `units.txt` and then validates placeholders, HTML tags and `%` specifiers (apply --dry-run). Fix what it reports.
5. `PY _build/ste100/ste_lint.py --units _build/ste100/work/paper_<name>/units.txt --words` → fix every **E**; fix **W** unless you can justify it. Fix by writing `fix_01.txt` (only the units you change), merge, lint again. Loop until E = 0. The lint uses the shared lists plus **your own** `tn_<slug>.txt` / `tv_<slug>.txt` only.
6. `PY _build/ste100/ste_units.py apply paper_<name>` (patches the module; read the number warnings: a changed number is a stop sign).
7. `PY _build/ste100/ste_verify.py check paper_<name>` — parity with the original (sections, shapes, figures, links, citations, numbers) + lint of the **rendered** page. It must say `RESULT: PASS`. (Its unit numbers differ from `units.txt`: search the printed text in `units.txt`.)
8. `PY _build/check_section_structure.py` must print `section-structure OK`.
9. Re-read your own text once, section by section, for meaning: hedges, numbers, comparatives, cause and effect, terms. Compare with `work/paper_<name>/units.original.txt`.
10. **Final reply = the report** (format in section 8). Do NOT write a REPORT.md (the harness refuses it).

Other tools: `PY _build/ste100/ste_lookup.py word […]` prints status, **approved meaning**, alternatives; `--entry word` the raw dictionary page; `ste_lint.py --text "…"` quick test of one sentence.

**Unit kinds you will see:** `p lead li cell th caption callout.title defterm.term defterm.body step.title step.body card.title card.body tag kv.key kv.val …`. `label` units with `in=L.xxx` are **diagram labels** (text drawn inside a figure): rewrite them too, keep each ≤ ~115% of its original length in characters (the drawing has a fixed size), and keep pre-split pairs (two units that are two lines of one label) as two lines. **Flow-diagram step text** (`in=L.flow…`) is wrapped by the drawing code at 16 characters per line: the rewritten text must wrap to **the same number of lines** as the original, or `ste_verify.py` reports `figure SVG changed`. Count the lines of your text with a 16-character wrap before you finish (keep the number of lines, not only the length). `misc` units that are not shown to readers (identifiers, code-like text) stay unchanged. Texts inside `<code>` are code, not prose: leave them.

## 3. Rules the linter enforces (and how to satisfy them)

**Words (R1.1–1.14).** Use only: approved dictionary words, **technical nouns** (TN), **technical verbs** (TV). Use an approved word only as its listed part of speech **and only with its approved meaning** (R1.2, R1.3, R9.2): `ste_lookup.py <word>` shows the meaning. Check every verb, adjective and preposition you are not sure of. Words that look harmless but have a narrow meaning: `push` (apply force; not "push the plant toward flower" → cause / give more), `pull`, `move` (change position), `get` (obtain; not become / increase / decrease), `keep`, `stay`, `hold`, `give` (provide), `show`, `turn` (rotate), `go`, `come`, `put`, `make`, `let`, `fall` (move down by gravity), `drink` (liquids; safety text only), `know` (be sure of data), `see` (with the eyes), `find` (discover / examine), `burn`, `tight`, `full` (maximum), `level` (horizontal), `light` (adj: small weight), `free`, `clear`, `high`/`low` (large/small value), `between`, `with`, `about` (concerned with), `above`/`below` (position only). `test`, `check`, `damage`, `work` are nouns only; `help` is a verb only.
American spelling (R1.14): color, meter, liter, center, fiber, mold, fertilizer, analyze, license, gray. No gendered pronouns (GR-7).

**Verbs (R3.1–3.7).** Allowed: infinitive, imperative, simple present, simple past, simple future (`will`), past participle **as an adjective**. Not allowed: present perfect, past perfect, progressive (`is drying`), `would`, `could`, `should`, `may`, `might`, `shall`. Helpers: `can`, `must`, `will`, `cannot`, `do not`. No `-ing` words unless approved (lighting, opening, remaining, missing, mating, routing, servicing, during) or listed as a technical noun. Active voice (R3.6): "The sensor measures the water content", not "The water content is measured". A "be + participle" that only states a condition ("the valve is closed") is allowed. Never "by + agent". Do not use a noun as a verb or a verb as a noun (R1.7, 1.13, 3.7): not "to water / feed / root / flower / trim"; say "apply water", "make roots". `test`, `check`, `damage`, `cover` are nouns: "do a check of", "do a test", "cause damage to".

**Multi-word nouns (R2.1–2.2).** Maximum 3 words in a row; use `of / for / in / on` or a hyphen for a unit ("root-zone EC sensor"). Write a long technical noun in full once, then a short form.

**Sentences (R4.1–4.5, 5.1, 6.3, 8.4–8.7).** Maximum **20 words** in an instruction (starts with a command verb, or safety text) and **25 words** in a description. Word count: a number with its unit = 1 word, text in parentheses = 1 (its own words are a separate sentence), a hyphenated word = 1, quoted text = 1, an abbreviation = 1. One topic per sentence. Do not drop words to shorten (no "If installed, remove"; articles `the / a / this` where English needs them). No contractions. `that` after "make sure", "show", "recommend". Approved connectors: `and`, `but`, `then`, `thus`, `as a result`, `at the same time`, `because`, `if`, `when`, `before`, `after`, `until`. Condition first in an instruction: "When the block is dry, apply water."

**Paragraphs (R6.4–6.6).** One topic, at most **6 sentences** per paragraph, the first sentence names the topic. A long `p` / `lead` unit may be split by writing `</p><p>` inside its text (nowhere else): each `<p>` is counted on its own.

**Punctuation (R8.1–8.3).** **No semicolons.** No dash as a clause break: write two sentences. Parentheses are fine. `and`, not `&` and not `and/or`.

**Procedures and safety (R5, R7).** One instruction per sentence (two actions at the same time are fine). Imperative form. Notes give information only. Safety text (`warn` / `danger` callouts): command or condition first, then the result: "Do not let the water content become less than 25%. A block that is too dry can stop taking in water."

**Writing practices (R9.x, GR-1…8).** If a word-for-word swap changes the meaning, **change the sentence**. No phrasal verbs (set up, carry out, dry out, turn on …). Same words for the same thing every time. No Latin abbreviations (`e.g.`, `i.e.`, `etc.`, `vs.`). `This` needs a noun. Each pronoun needs one clear noun to point to.

## 4. Technical nouns and verbs (TN / TV)

STE lets you use words outside the dictionary **only** as technical nouns (Rule 1.5: a noun that names a specific thing, material, place, measurement, document or life form of the subject field) or technical verbs (Rule 1.12). The lists are `_build/ste100/data/tn_*.txt` / `tv_*.txt`; the lint reads the shared lists plus your own file.
- Try an approved word first (the lint message shows alternatives).
- Add a noun only if it names a real cultivation / lab / equipment / chemistry / regulation concept (`dryback`, `trichome`, `rockwool`, `cultivar`). **Never general English** (thing, purpose, rule, plan, goal, story, moment, idea, mistake, benefit, strategy, recipe, history).
- No jargon or slang (R1.10): `veg`, `flip`, `dehu`, `temp`, `rh` as words, `cal-mag`. Write the full term once; abbreviations in capitals are fine.
- One technical noun per concept in the paper and across papers (R1.11). Reuse the glossary term (`GLOSSARY_TERMS.txt`).
- Adjectives or participles that belong to a technical noun go in as the whole phrase: "relative humidity", "vegetative growth", "dissolved oxygen", "grow room".
- A TV only when no approved verb works (irrigate, saturate, harvest, defoliate, dehumidify, escalate …). A word may be both a TN and a TV when both are real (harvest). Never use a TN as a verb unless it is also listed as a TV.
- Add with `PY _build/ste100/ste_lint.py --add-tn <paper-slug> "word one" word2` and `--add-tv <paper-slug> verb`. List every word you add, with its category, in your final reply. The coordinator audits the lists afterwards.

## 5. Patterns that work

- Definition: "**Dryback** is the quantity by which the water content decreases from the peak to the next low."
- Cause and effect: "When the air temperature increases, the plant uses more water."
- Condition + command: "If the slab is dry, apply water in two short shots."
- Recommendation: "We recommend that you …", or an imperative inside a list.
- Hedge: "It is possible that …", "In some rooms, …", "The data show that …", "No studies show that …".
- Numbers: "approximately 25 °C" (not "~25" or "about 25"); ranges "8 to 10 weeks"; limits "more than 30 °C", "less than 18%".
- Lists: lead-in ends with a colon, then short items. No semicolons, no "etc.".
- Frequent swaps and recurring errors: `SUBSTITUTIONS.md`.

## 6. Do / do not

- **Do** keep sentences concrete: what happens, to what, when, by how much.
- **Do** keep the reader-facing "you".
- **Do not** replace a measure with a vague word, round numbers or convert units.
- **Do not** edit code or touch anything inside `<svg>` (diagram labels are `label` units).
- **Do not** leave a TODO or "(…)" in the final text.
- Mention in your reply, but do not "fix" by dropping content, every nuance that STE forced you to lose.

## 7. When the lint is wrong

The linter is heuristic. A **W** can be a false alarm (say so in your reply). An **E** you believe is a false alarm: rewrite the sentence so the lint is quiet if that is possible without harming the meaning; if it is not, keep the sentence and list it (unit id, text, rule, reason) under "Lint disputes". Do not edit the linter or the dictionary data.

## 8. Final reply = report (<= 350 words, plain text)

```
paper_<name>: DONE | DONE WITH DISPUTES | BLOCKED (reason)
Lint (units file): E=<n> W=<n>   Rendered (ste_verify): E=<n> W=<n>   Verify: PASS/FAIL   Section gate: OK/FAIL
Units changed: <n> of <n> (labels: <n>)
TN added (category): …      TV added (reason): …
Lint disputes: U0123 "…" R… — reason   (or none)
Number changes: every number that appears or disappears, with the reason (or none)
Content decisions: analogies removed, sentences split, claims that needed care, terms unified
Nuance lost / needs human review: …
Tool and rule feedback: <= 6 lines (false positives, missed errors, confusing rules)
```
