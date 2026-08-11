# Slab Irrigation 18-Module Visual System Design

## Objective

Expand the slab-irrigation guide from six illustrative renders into eighteen inline teaching modules. Every module pairs a realistic, label-free recognition image with a separate editable SVG diagram containing the factual labels, measurements, equations, phases, and decision logic.

## Chosen presentation

Use paired inline modules at the point where each concept is taught. Desktop displays the image and diagram side by side; phones stack them image-first. This keeps the visuals in the reading flow, preserves accessibility, and avoids hiding material behind tabs.

Alternatives rejected:

- A visual atlas at the end disconnects explanations from their source paragraphs.
- Interactive image/diagram toggles conceal half the explanation and add unnecessary controls.
- Combined raster infographics make factual text difficult to correct and conflict with the editable-label requirement.

## Coverage map

1. Clear-centre under-canopy layout
2. Dripper delivery chain
3. Three-plant slab, drainage, and root paths
4. Measured shot volume and runtime
5. VWC, field capacity, and dryback terminology
6. Connected block-slab water column
7. Vertical VWC gradient and sampling volume
8. Representative versus misleading sensor placement
9. Level, soak, charge, and slit preparation sequence
10. Rooting-in progression and plant-led exit criteria
11. P0-P1-P2-P3 substrate states
12. Daily VWC and pore-water EC traces
13. Vegetative, setting, bulking, and finish arc
14. Three-plant slab measurement and runoff layout
15. Root-zone EC correction and defined finish decision tree
16. Climate demand, VPD, and irrigation response loop
17. Symptom-to-cause troubleshooting ladder
18. Combined operating-setpoint dashboard

## Image policy

- Reuse the six approved 1536 × 1024 renders for modules 1, 2, 3, 7, 8, and 11.
- Generate twelve new 1536 × 1024 renders through 9Router using `openai/gpt-image-1`.
- Do not ask the image model to render labels, numbers, screens, arrows, charts, or legible text.
- Use the established dark, restrained technical-photography style with realistic stone wool, irrigation hardware, plants, sensors, reservoirs, meters, and room equipment.
- Publish optimized WebP derivatives while retaining PNG masters in the local deliverable asset folder.

## Diagram policy

- Produce all eighteen explanatory diagrams as inline SVG.
- Use a shared visual grammar: charcoal field, pale geometry, green for desired paths/states, amber for caution or EC, and red only for faults.
- Put factual labels, dimensions, rates, formulas, phase names, and arrows in SVG/HTML only.
- Each SVG must have a unique title and description referenced by `aria-labelledby`.

## Integration and responsive behavior

- Each module uses `figure.concept-pair[data-concept]` containing `.concept-image-panel` and `.concept-diagram-panel`.
- Images lazy-load from `assets/slab-irrigation-guide/*.webp` on the site and use the same relative asset structure in the packaged local guide.
- Desktop uses a two-column grid with equal visual weight. Below 720 px, panels stack and diagram labels remain visible.
- Long explanations remain in HTML captions beneath the pair; the SVG carries only the minimum explanatory text needed to read the diagram.

## Acceptance criteria

- Exactly 18 concept pairs, 18 raster images, and 18 SVG diagrams.
- Every teaching section from room setup through combined setpoints has visual coverage.
- No generated raster contains factual labels or is treated as an as-built drawing.
- All images load with natural dimensions of at least 1536 × 1024.
- No horizontal overflow at 1440 px or 390 px.
- Existing content, citations, layout diagram, graphs, search, theme switching, and permalink remain functional.
- The canonical build passes its leak scan and GitHub Pages deployment is verified on the live URL.
