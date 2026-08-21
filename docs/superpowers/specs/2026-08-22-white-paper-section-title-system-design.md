# White-paper section title system design

## Classification

Architectural. The change affects the section hierarchy, navigation labels, search index, Markdown corpus, HTML pages, and authoring conventions across all 55 papers.

## Problem

The corpus uses many titles that narrate, tease, editorialise, or announce that a definition is coming instead of naming the section's contents. Examples include “The words you need,” “What this is,” “What good looks like,” “The mental model,” and claim-like metaphors that hide the subject. Shared section functions also use inconsistent names, and a few papers place definitions or summary material in an awkward order.

## Goals

- Make every H2 useful in a table of contents without requiring surrounding prose.
- Use the same title for the same section function wherever the content genuinely matches.
- Keep each paper in the order that best teaches or operates its subject.
- Use sentence case and direct, literal wording.
- Preserve useful topic-specific distinctions instead of forcing every paper into an identical template.
- Preserve public anchors and generated links.

## Standard section sequence

Papers should follow this sequence when those functions exist:

1. Purpose and scope
2. Definitions
3. Principles and evidence
4. Equipment or setup
5. Procedure or operating method
6. Targets, monitoring, and decisions
7. Troubleshooting
8. Expected results and limitations
9. References

This is a semantic order, not a mandatory nine-heading template. A biology reference, a sequential SOP, and an economics paper should keep the order required by their subjects. Sections move only when the existing order impairs comprehension or operation.

When a genuine `Definitions` section exists, it is always the second source section, immediately after `Purpose and scope`. The energy paper therefore places its summary after `Definitions`: that summary uses the energy metrics established in the definitions section. The nine approved source reorders preserve this rule and remain unchanged. Any future exception must be recorded as an exact `(slug, section_id, exact_title)` entry with a documented semantic reason.

## Title rules

- Every paper's first source section title must be `Purpose and scope`.
- Use sentence case.
- Prefer a short noun phrase or direct action phrase.
- Use `Purpose and scope`, `Definitions`, `Troubleshooting`, `Expected results and limitations`, and `References` when those labels accurately describe the whole section.
- Keep specific titles such as `Stage II: multiplying shoots`, `Root-zone EC`, or `Mock recall procedure` when they identify the content better than a generic label.
- Remove framing such as “what this is,” “the words you need,” “in plain English,” “honest,” “actually,” “the mental model,” “good,” “realistic,” “the whole thing,” and teaser questions unless the word is technically necessary.
- Avoid metaphors, sales language, conversational asides, scolding, and claims masquerading as navigation.
- Do not weaken technical meaning or alter claims merely to make a title shorter.

## Source and rendering architecture

The authoritative section dictionaries remain in `_build/paper_*.py`. Common build-injected evidence material is maintained in `_build/build.py` and `_build/export_corpus.py`. Reference sections are generated from each module's `REF_IDS`; they are not stored in `SECTIONS`. Generated root HTML, `papers/*.md`, search indexes, manifests, LLM exports, bundles, and archives are never hand-edited.

Section `id` values are stable public anchors. Renaming or reordering a section must not change its `id`. When sections move, kicker numbers, figure numbers, references, and any content-dependent navigation must remain coherent.

## Validation

A repository checker will load every module in `_build/build.py::PAPER_MODULES` and fail when:

- a paper lacks sections or reference metadata;
- a paper's first source section title is not `Purpose and scope`;
- section IDs are duplicated;
- headings are not sentence case under the corpus convention;
- headings contain banned editorial framing;
- canonical functional sections use non-canonical variants;
- a paper places `Definitions` after operational procedure without a documented topic reason;
- `Troubleshooting` follows `Expected results and limitations`;
- section kickers with numeric prefixes are not sequential.

The checker may use explicit, reviewed exceptions for technically necessary terms and topic-specific structures. Title exceptions must be keyed by exact `(slug, section_id, exact_title)` values. Any future ordering exception must use the same exact key and document the semantic reason the general rule does not apply.

Completion also requires a clean 55-paper build, a final `References` section in every generated paper, a clean private-information leak scan, balanced emphasis tags, valid internal section links, and verification that the pushed GitHub Pages build serves the updated headings.

## Non-goals

- Rewriting paper body prose or changing technical claims.
- Forcing every paper to contain all nine functional sections.
- Changing paper titles, slugs, or section anchor IDs.
- Reorganising unrelated navigation, theme, imagery, or citations.
