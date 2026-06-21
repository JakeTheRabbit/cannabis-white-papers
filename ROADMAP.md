# The Cannabis White Papers — gap analysis & roadmap

Goal: a complete, beginner-to-expert online cultivation guide. This is the map from the
current 21 papers to full coverage, the order a reader should follow, and what's still missing.

## Where we are

21 live papers across propagation, substrate/crop-steering, environment, plant health,
post-harvest, precision/automation, and facility/GMP. Strong on the *systems* and *precision*
end. Thin on plant fundamentals, lighting/climate deep-dives, water/nutrient diagnostics, and
post-harvest testing/extraction.

## The learning tree (order / flow)

Ten tiers, foundations first. `[live]` = published, `[plan]` = gap to fill.

**T0 Foundations — know the plant**
- Cannabis plant biology & life cycle `[plan]`
- Cannabinoids & terpenes: what's in the plant and why `[plan]`
- Genetics, seeds & phenotype hunting `[plan]`

**T1 The grow space — set the environment**
- The grow room: a systems guide `[live]`
- Lighting: spectrum, PPFD & DLI `[plan]`
- Light acclimation `[live]`
- Airflow design `[live]`
- Temperature, humidity & VPD control `[plan]`
- CO2 enrichment `[plan]`
- HVAC, cooling & dehumidification sizing `[plan]`

**T2 Substrate & water — the root-zone foundation**
- Substrates compared: coco, rockwool, soil, hydro `[plan]`
- Precision coco cultivation: crop steering `[live]`
- Source water, RO & alkalinity `[plan]`
- pH: what it is and how to hold it `[plan]`
- Mixing an Athena Pro Line stock tank `[live]`
- Nutrient deficiency & toxicity diagnosis `[plan]`

**T3 Propagation — make plants**
- Seeds, germination & seedlings `[plan]`
- Cloning `[live]`
- Tissue culture (clean genetics) `[live]`
- Mother / stock-plant management `[plan]`
- Transplanting & potting up `[plan]`

**T4 Veg & training — build the plant**
- Defoliation & plant training for yield `[live]`
- Vegetative management & timing `[plan]`

**T5 Flower & ripen — steer to yield and quality**
- The flower cycle, week by week `[plan]`
- Ripening, flush & harvest timing `[plan]`

**T6 Plant health — keep them alive**
- IPM: a working SOP `[live]`
- Pest identification & control (mites, thrips, gnats) `[plan]`
- Root diseases: pythium & fusarium `[plan]`
- Mould risk: bud rot & powdery mildew `[live]`

**T7 Harvest & post — flower into product**
- Harvest, dry, trim & cure `[live]`
- Extraction & concentrates: rosin, solventless, solvent `[plan]`
- GMP hash manufacturing `[live]`
- Lab testing, potency & contaminant COAs `[plan]`

**T8 Precision & automation — dial it in**
- Root-zone state (TEROS-12) `[live]`
- Signal & noise `[live]`
- Smart watering (VRWE) `[live]`
- The closed loop `[live]`
- Plant-state dashboard `[live]`
- F2 crop steering `[live]`
- Irrigation manual `[live]`

**T9 Facility, business & compliance — run it as an operation**
- Designing a facility in 3D `[live]`
- Quality manual / QMS `[live]`
- Compliance, licensing & track-and-trace `[plan]`
- Energy, utilities & sustainability `[plan]`
- Yield per watt & unit economics `[plan]`

## Gap list (22 planned papers), by priority

**Phase A — core beginner gaps (build first):**
seeds-germination, lighting-fundamentals, nutrient-deficiencies, ph-management,
flowering-stages, pest-id, water-quality, substrates-overview.

**Phase B — fill the plant-knowledge and propagation spine:**
cannabis-biology, cannabinoids-terpenes, genetics-phenohunting, transplanting,
mother-plants, co2-supplementation, root-disease, testing-coa.

**Phase C — environment depth, post-harvest breadth, business:**
hvac-dehumidification, climate-vpd, ripening-flush, extraction, compliance-licensing,
energy-sustainability, unit-economics.

## Cross-cutting build work (this pass)

1. **Curriculum page** (`curriculum.html`) renders this tree as the canonical learning path; live papers link, planned show as `soon`.
2. **Auto-interlinking**: a term→paper map auto-links concept words in body prose to the relevant paper (first mention per page, never self, never in headings/code/existing links).
3. **Search upgrade**: full-text section index + synonym/concept expansion (semantic-lite) + keyword ranking, prefix and fuzzy matching, section-level snippets.

Each planned paper follows the same pipeline already in place: research (extract + peer-reviewed
cite) → author from outline against the template → build → verify. Roughly the same per-paper
cost as the Phase 3/4 batches.
