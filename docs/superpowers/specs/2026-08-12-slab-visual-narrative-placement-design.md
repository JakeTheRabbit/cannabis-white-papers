# Slab Visual Narrative Placement Design

## Problem

The 18 image-and-diagram modules exist, but each was appended to the end of its section. The visuals therefore read as a detached gallery instead of explanations attached to the relevant prose, table, calculation, or procedure.

## Design

Use just-in-time inline placement. Each module appears immediately before or after the exact content block it explains. Placement is encoded as a semantic anchor relation, not as a section-only destination.

Remove the artificial `Concept 01–18` sequence because the modules are not a single ordered procedure. Each module keeps its subject title plus the functional labels `Recognition image` and `Working diagram`. Replace the repeated disclaimer sentence with the compact legend `Illustrative image · editable factual diagram`.

## Placement map

| Visual | Anchor relation |
|---|---|
| Three-plant slab | after the working-setup key/value block |
| Clear-centre layout | after the existing five-layout comparison figure |
| Dripper delivery chain | after the dripper-introduction paragraph |
| Shot volume/runtime | after the emitter-runtime table |
| Dryback terminology | after the dryback-conversion warning |
| Connected water column | after the paragraph defining block/slab hydraulic connection |
| Vertical VWC gradient | after the existing Day 0–2 hydraulic figure |
| Sensor placement | after the paragraph explaining misleading hand observations |
| Slab preparation | before the preparation steps |
| Rooting progression | after the rooting-in steps and before the single-outlet warning |
| P0–P3 states | after the daily-phase table |
| Daily VWC/EC trace | after the `Model curves for comparison` heading and before calculated graphs |
| Crop-stage arc | after the stage-summary lead and before the target table |
| Measurement/runoff layout | after the practitioner case-study lead and before reported-practice cards |
| EC correction/finish | after the section lead and before corrective steps |
| Climate response | after the demand paragraph and before environmental bands |
| Troubleshooting | before the detailed symptom table |
| Combined setpoints | after the quick-reference setpoint block and before the five rules |

## Responsive behaviour

Desktop keeps the two-panel recognition/diagram plate. Phone layouts stack image above diagram. No module may exceed the content viewport or hide diagram labels.

## Acceptance criteria

- Exactly 18 unique modules, images, and SVG diagrams remain.
- Every module satisfies its semantic adjacency rule.
- No `Concept 01–18` labels or repeated disclaimer sentences remain.
- Neutral guide copy, 13 guide sections, 17 references, calculated graphs, search, theme toggle, and existing room-layout geometry remain unchanged.
- Local and public pages pass desktop 1440 px and phone 390 px browser verification.
