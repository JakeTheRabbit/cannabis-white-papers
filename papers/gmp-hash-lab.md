---
slug: "gmp-hash-lab"
title: "GMP hash manufacturing: facility flow and quality control"
eyebrow: "Facility · GMP"
summary: "How to design a clean, compliant hash and extract factory from scratch: what GMP means, how rooms and people and product move, and how a batch earns its way to market."
track: "Harvest, dry, trim & cure"
read_time: "~18 min read"
diagrams: "13 diagrams"
related: ["mould-risk", "facility-3d"]
url: "https://jaketherabbit.github.io/cannabis-white-papers/gmp-hash-lab.html"
md_url: "https://jaketherabbit.github.io/cannabis-white-papers/papers/gmp-hash-lab.md"
version: "1.0"
updated: "2026-06-24"
license: "CC BY-NC 4.0"
license_url: "https://creativecommons.org/licenses/by-nc/4.0/"
attribution: "The Cannabis White Papers"
refs: [{"id": "ecfr-21cfr211", "n": 1, "cite": "U.S. Food and Drug Administration. 21 CFR Part 211, Current Good Manufacturing Practice for Finished Pharmaceuticals (esp. 211.22 Responsibilities of quality control unit; 211.165 Testing and release for distribution; 211.192 Production record review). Code of Federal Regulations, Title 21.", "url": "https://www.ecfr.gov/current/title-21/chapter-I/subchapter-C/part-211", "peer": false}, {"id": "ich-q3c-r9-ema", "n": 2, "cite": "International Council for Harmonisation. ICH Q3C(R9) Guideline for Residual Solvents (Step 5), reproduced by European Medicines Agency, 2024. EMA/CHMP/ICH/82260/2006.", "url": "https://www.ema.europa.eu/en/documents/scientific-guideline/ich-q3c-r9-guideline-impurities-guideline-residual-solvents-step-5_en.pdf", "peer": false}, {"id": "ehp-cannabis-contaminants-2019", "n": 3, "cite": "Seltenrich N. Cannabis Contaminants: Regulating Solvents, Microbes, and Metals in Legal Weed. Environmental Health Perspectives. 2019;127(8):082001. doi:10.1289/EHP5785.", "url": "https://ehp.niehs.nih.gov/doi/10.1289/EHP5785", "peer": true}, {"id": "en1822-h14-hepa", "n": 4, "cite": "Camfil. EN 1822 and ISO 29463 HEPA filter factory test (EN 1822-1:2019 filter classes; H14 minimum efficiency 99.995% at the Most Penetrating Particle Size, MPPS).", "url": "https://www.camfil.com/en/insights/standard-and-regulations/en-1822-and-iso-29463-hepa-filter-factory-test", "peer": false}, {"id": "sciencedirect-cleanroom-personnel-emissions-2024", "n": 5, "cite": "Meng H, Shiue A, Wang C, Leggett G. Particle and bacterial colony emissions from garments and humans in pharmaceutical cleanrooms. Journal of Building Engineering, 2024;96:110...; ScienceDirect S2352710224023970.", "url": "https://www.sciencedirect.com/science/article/abs/pii/S2352710224023970", "peer": true}, {"id": "pmc-capa-ich-q10-2024", "n": 6, "cite": "Enhancing Pharmaceutical Product Quality With a Comprehensive Corrective and Preventive Actions (CAPA) Framework: From Reactive to Proactive. Cureus, 2024. PMC11490658.", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11490658/", "peer": true}, {"id": "fda-process-validation-2011", "n": 7, "cite": "U.S. Food and Drug Administration, CDER/CBER/CVM. Guidance for Industry, Process Validation: General Principles and Practices. January 2011 (Revision 1).", "url": "https://www.fda.gov/files/drugs/published/Process-Validation--General-Principles-and-Practices.pdf", "peer": false}, {"id": "ispe-cleanroom-design-iso14644-16", "n": 8, "cite": "Pharmaceutical Engineering (ISPE). Pharmaceutical Cleanroom Design & ISO 14644-16, Sep/Oct 2021, air-change-rate optimization for classified cleanrooms.", "url": "https://ispe.org/pharmaceutical-engineering/september-october-2021/pharmaceutical-cleanroom-design-iso-14644-16", "peer": false}]
---

# GMP hash manufacturing: facility flow and quality control

_Facility · GMP · ~18 min read_

> How to design a clean, compliant hash and extract factory from scratch: what GMP means, how rooms and people and product move, and how a batch earns its way to market.

## What This Is: GMP and the Hash Lab From Zero

GMP stands for **Good Manufacturing Practice**: a written, audited system that proves a product is exactly what its label says and that nothing harmful rode along. A GMP hash lab turns cannabis biomass into purified resin concentrates (bubble hash, rosin, live resin, distillate) under tight contamination control.

The same physics that concentrate the cannabinoids you want also concentrate the contaminants you don't. Extraction multiplies both the good and the bad roughly five- to ten-fold[^ehp-cannabis-contaminants-2019], so a pesticide or mould level that looked fine on the raw flower can fail badly once it is squeezed into a gram of resin. Every step in the building is designed to answer one question: _can we prove this material is safe and correctly labelled?_ If yes, it moves forward. If not, it holds.

Two rule-sets do most of the governing. **EU-GMP Annex 1** sets the cleanroom classifications and the contamination-control strategy, and the U.S. **cGMP rules in 21 CFR 210/211** set the production controls, the records, and the authority of the quality unit to release product[^ecfr-21cfr211]. This paper is a reference architecture, not legal advice. The exact limits and grades vary by jurisdiction.

> **KEY — The one rule under all the others**
> 
> ‘If it isn't written down, it didn't happen.’ GMP is a documented, validated, inspectable system. A spotless room with no records fails an audit. A modest room with complete, signed records passes.

> **Diagram.** Four numbers anchor the whole facility: five cleanliness grades, seven mandatory release-test families, full genealogy coverage, and zero open critical deviations permitted at the point of release.

| Standard | What it covers | Facility area it governs |
| --- | --- | --- |
| EU-GMP Annex 1 | Cleanroom classification & contamination-control strategy | All classified rooms |
| cGMP 21 CFR 210/211 | Production controls, records, QC-unit release authority | Whole plant + QA |
| ICH Q7 / Q9 / Q10 | Quality system, risk management, lifecycle | Quality management system |
| ISO 14644-1 | Cleanroom particle-count classes (ISO 5/7/8) | Air classification |
| GACP | Good Agricultural & Collection Practice for biomass | Goods-in / intake |
| NFPA 30 / C1D1 | Flammable liquids & classified electrical areas | Solvent extraction room |

*The governing standards and which part of the building each one rules.*

## Key Terms: The Words You Need First

A handful of terms do the heavy lifting before any diagram makes sense. You don't need to memorise them: each comes back in context.

**Cleanroom grade** — A letter (CNC, D, C, B, A) describing how clean a room's air is, mapped to ISO 14644 particle classes. Grade C = ISO 7, Grade A = ISO 5.

**Batch / lot** — One defined production run with a single lot ID. Everything that happens to it is recorded against that ID. That record is its genealogy.

**Deviation** — Any departure from the approved process. Every deviation is logged, investigated, and closed before the affected batch can be released.

**CAPA** — Corrective And Preventive Action: the loop that fixes the immediate problem (corrective) and stops it recurring (preventive).

**Quarantine / Released / Rejected** — The three exclusive status states every material sits in. Nothing is ‘in between’. Status is always one of these three.

**CCP (Critical Control Point)** — A step where a measured limit prevents a hazard (HACCP language). One example: wash water below 4 °C.

**ALCOA+** — What a good record must be: Attributable, Legible, Contemporaneous, Original, Accurate, plus Complete, Consistent, Enduring, Available.

**Water activity (Aw)** — Free water available to microbes, on a 0–1 scale. Keeping it low starves mould and bacteria. CoA = Certificate of Analysis. C1D1 = a flammable-rated room.

QA, the Quality Assurance function, owns the final release decision, and QA is independent of production[^ecfr-21cfr211]. That separation is the spine of the whole system: the people paid to ship product never get to sign off their own work.

> **Diagram.** The three exclusive status states. Physical location and computer status must always agree.

## Zoning and Cleanroom Grades: Nested Shells

The building is a set of nested cleanliness shells, like the layers of an onion. The **dirty** operations, intake, milling and waste, sit at the outer perimeter. The **cleanest** operations, collection, filling and packaging of open product, sit at the protected core.

The flow rule is simple and absolute: **product moves inward toward purity; people and waste move outward toward the dirty edge, and the two never cross uncontrolled.** Each shell boundary is an airlock plus a one-grade cleanliness step. Under EU-GMP Annex 1, Grade C corresponds to ISO 7 and Grade A to ISO 5[^ispe-cleanroom-design-iso14644-16]. Most recreational and medical hash operations run a D-to-C envelope and treat the fill point as Grade C with local protection. Full Grade A/B is only needed for sterile or pharma-grade dose forms.

> **Diagram.** Concentric zoning from the CNC outer shell through Grade D and C to the clean core. Inward = product to purity; outward = personnel and waste to the dirty edge.

> **Diagram.** Air-change rate scales with grade: ISO 7 (Grade C) rooms run roughly 20–40 changes per hour[^ispe-cleanroom-design-iso14644-16], and a unidirectional Grade A fill point far higher.

| Room | Grade | ISO class | ACH | Activity |
| --- | --- | --- | --- | --- |
| Goods-in / quarantine | CNC | , | 4–6 | Receive & hold biomass |
| Milling / dispensing | Grade D | ISO 8 | 10–20 | Size-reduce, weigh |
| Wash / extraction | Grade C | ISO 7 | 20–40 | Separate trichomes |
| Freeze-dry / press | Grade C | ISO 7 | 20–40 | Dry & press to rosin |
| Solvent recovery | Grade D (C1D1) | ISO 8 | 10–20 | Recover solvent, LEL purge |
| Open-product fill | Grade A | ISO 5 | unidirectional | Fill open product (pharma) |

*Each room with its grade, ISO class, air-change rate, and key activity.*

## Pressure Cascade, HVAC, and Gowning

Air is the main way contamination travels, so the building runs a **positive-pressure cascade**: clean rooms are held at higher pressure than dirtier ones, so air always blows _outward_ from clean to dirty. Open a door and clean air rushes out. It can never suck dirty air toward the product.

Pressures step up shell by shell. EU-GMP Annex 1 recommends roughly a 10–15 Pa difference between adjacent classified zones[^ispe-cleanroom-design-iso14644-16], giving a ladder like 0 Pa (CNC), +15 (D), +30 (C), +45 (B), +60 (A). The solvent room is the one exception: it runs **negative**, around -15 Pa, so flammable vapour is contained and pulled toward the LEL exhaust rather than pushed into the building.

> **Diagram.** Rising positive pressure from CNC to the Grade A core keeps airflow running clean-to-dirty; the C1D1 solvent room runs negative to contain vapour.

People are the single largest source of particles and microbes in a cleanroom[^sciencedirect-cleanroom-personnel-emissions-2024], so entry is a one-way airlock sequence that escalates gowning as the grade rises. Filtration scales with grade too: F9 pre-filters in prep, H13 HEPA in wash and dry, and H14 HEPA at the fill point. An H14 HEPA filter retains at least 99.995% of particles at the most-penetrating size[^en1822-h14-hepa], which is why it guards the cleanest air.

> **Diagram.** A one-way gowning sequence from CNC entry through grade airlocks to the work zone, with a separate dashed de-gown exit so entry and egress never share a door.

> **WARN — Health check at the door**
> 
> Anyone with open wounds, respiratory illness, or gastrointestinal symptoms is excluded at the entry health check, and the exclusion is recorded. Airlocks are interlocked so both doors can never open at once.

| Grade | Temp | RH | Filtration | ΔP | ACH |
| --- | --- | --- | --- | --- | --- |
| CNC | ambient | <70% | F7 | 0 Pa | 4–6 |
| Grade D | 18–24 °C | 45–60% | F9 | +15 Pa | 10–20 |
| Grade C | 18–22 °C | 45–55% | H13 HEPA | +30 Pa | 20–40 |
| Grade A fill | 18–22 °C | 45–55% | H14 HEPA | +60 Pa | unidir. |
| Solvent (C1D1) | 18–24 °C | <55% | F9 | -15 Pa | 10–20 |

*HVAC control matrix: temperature, humidity, filtration, pressure and air changes per grade.*

## How the Product Is Actually Made

Two routes leave the weigh-in. **Solventless** separates the trichome heads (the resin glands) mechanically. **Solvent extraction** dissolves the resin and then recovers it. They share a goal but carry very different hazards.

The solventless route agitates fresh-frozen biomass in ice water, sieves the resin through a stack of screens (220 down to 25 micron), freeze-dries it, and presses it to rosin. Its four **critical control points** are wash temperature (≤4 °C), water quality (RO, <10 CFU/mL), water activity (Aw ≤0.55), and press temperature (≤90 °C). Keeping water activity at or below about 0.55–0.65 starves microbes and fungi before they can grow[^ehp-cannabis-contaminants-2019].

> **Diagram.** The solventless flow from fresh-frozen biomass through agitation, sieving, freeze-drying and pressing, with the four critical control points called out.

Solvent extraction is a closed loop using butane, propane, ethanol, or CO₂. Here the dominant hazards shift to **flammability** and **residual solvent**, the trace of extraction solvent left in the product. Residual butane and propane action limits run roughly 2000–5000 ppm depending on the jurisdiction[^ich-q3c-r9-ema], and ethanol, an ICH Q3C Class 3 solvent, is typically capped near 5000 ppm[^ich-q3c-r9-ema]. Every batch is gated hard by a headspace GC-MS residual-solvent test before it can be released.

> **Diagram.** Charge to solvent pass to winterize to recovery to vacuum purge, with the residual-solvent QC gate and a parallel C1D1 safety overlay.

> **DANGER — Hydrocarbon rooms are C1D1 for a reason**
> 
> Butane and propane extraction must run in an NFPA-classified **C1D1** room: LEL (lower-explosive-limit) gas detection with auto-purge, explosion-proof electrics, a two-person rule, and ASME-rated pressure vessels. This is the highest-consequence area in the building. A single ignition source is catastrophic.

For the solventless line, water is treated as an **ingredient**, not a utility. It runs its own loop: mains to carbon/sediment pre-filter, to RO/DI, to a UV + 0.2-micron polish, to a sanitised ice hopper, to the point of use, with sampling at three points and out-of-spec water sent straight to quarantine.

> **Diagram.** The linear water-treatment train with its three sampling points and out-of-spec quarantine logic.

## Step-by-Step: Testing, Sampling, and Batch Release

Testing happens at **three tiers**, incoming biomass, in-process, and release, across four sampling stations along the value stream. Retained reference samples are kept to expiry + 1 year so any later complaint can be investigated against the actual material.

> **Diagram.** From incoming biomass (S1) through in-process (S2) and bulk concentrate (S3) to finished goods (S4), with what each station tests.

The finished-goods release panel is the legal gate to market. It covers **seven families**: potency, residual solvents, pesticides, microbials, heavy metals, mycotoxins, and water activity/moisture[^ehp-cannabis-contaminants-2019]. Heavy metals (lead, cadmium, arsenic, mercury) are quantified by ICP-MS, the standard method[^ehp-cannabis-contaminants-2019], and the regulated mycotoxins, aflatoxins B1/B2/G1/G2 and ochratoxin A, are carcinogens controlled at parts-per-billion levels.

> **TIP — Always test the concentrate, never just the flower**
> 
> A pesticide or metal level that passes comfortably on raw flower can fail once it is concentrated five- to ten-fold into resin[^ehp-cannabis-contaminants-2019]. Release decisions are made on the _finished concentrate_, full stop.

| Family | Analytes | Method | Why |
| --- | --- | --- | --- |
| Potency | THC, CBD, total cannabinoids | HPLC-DAD | Label accuracy |
| Residual solvents | Butane, propane, ethanol | Headspace GC-MS | Solvent safety |
| Pesticides | State pesticide list | LC-MS/MS, GC-MS/MS | Chemical safety |
| Microbials | TYMC, TAMC, E. coli, Salmonella, Aspergillus | Plate / qPCR | Pathogen control |
| Heavy metals | Pb, Cd, As, Hg | ICP-MS | Toxic-metal limits |
| Mycotoxins | Aflatoxins, ochratoxin A | LC-MS/MS | Carcinogen control |
| Water activity | Aw, moisture | Aw meter / KF | Mould prevention |

*The seven mandatory release families. Pathogens such as Salmonella and E. coli must be absent.*

QA, not production, then runs three sequential gates. Any ‘no’ diverts the batch to remediation. Only a clean pass on all three reaches release with a QP/QA signature and an issued Certificate of Analysis[^ecfr-21cfr211].

1. **Gate 1: Records** — Is the batch record complete and signed end to end (ALCOA+)? If not, the batch cannot proceed.
2. **Gate 2: Results** — Are all seven test families within spec, pathogens absent? Any out-of-spec result routes to OOS investigation.
3. **Gate 3: Deviations** — Are all deviations on this batch closed with CAPA? Any open critical deviation blocks release.
4. **Release** — All three gates pass: QA signs, the CoA is issued, status flips to Released.

> **Diagram.** The three sequential gates, records, results and deviations, routing to QA release or to the return/OOS/hold lanes.

## When It Goes Wrong: Deviations, CAPA, and Common Traps

When reality departs from the approved process, the **deviation system** catches it. ICH Q10 establishes the pharmaceutical quality system, including CAPA and change control, that this loop sits inside[^pmc-capa-ich-q10-2024]. Every deviation runs through a five-stage CAPA loop, and it is _not_ closed until the final effectiveness check passes.

> **Diagram.** Detect, contain, investigate, correct, then prevent-and-verify, with a feedback arrow closing the loop back into the process[^pmc-capa-ich-q10-2024].

Severity triage sets the urgency and the sign-off level. A **critical** deviation, one with patient-safety or recall risk, goes to the QA director with under 24 hours to containment. A **major** goes to QA on a defined timeline. A **minor** goes to a supervisor to be trended. Root-cause tools such as 5-why and Ishikawa (fishbone) diagrams are the standard ways to find what actually went wrong[^pmc-capa-ich-q10-2024].

> **WARN — The three classic traps**
> 
> - **Trusting the biomass CoA.** Extrapolating safety from the raw-flower result instead of testing the concentrate. The number that matters is the one after concentration.
> - **Releasing on a borderline residual-solvent result.** Never. Re-test, re-purge, or reject, and document the disposition.
> - **Letting physical and system status disagree.** Quarantine stock must sit behind a locked cage or controlled rack; the computer and the shelf must always tell the same story.

> **Diagram.** Off-spec product and spent biomass into a locked quarantine cage, rendered unusable, then licensed disposal with a witnessed manifest; solvent waste runs as a separate hazmat stream.

## Realistic Expectations: Cost, Cadence, and What 'Compliant' Really Means

Compliance is a continuous program measured by data, not a one-time build. Management review tracks a handful of KPIs: right-first-time release rate (target ≥98%), deviation rate per batch (<5%), median CAPA closure (≤30 days), environmental-monitoring results within limits (≥95%), and mock-recall retrieval (<24h).

> **Diagram.** The headline KPI targets shown against their thresholds. The system is healthy when right-first-time stays high and deviation rate stays low.

Equipment must be **qualified** before it ever makes releasable product, through the validation V-model: DQ (design), IQ (installation), OQ (operational), PQ (performance), each verifying the leg opposite it. Qualification follows that IQ/OQ/PQ progression[^fda-process-validation-2011], and only then does **process validation** begin: conventionally three consecutive conforming batches to prove the process is reproducible[^fda-process-validation-2011].

> **Diagram.** The descending design leg (URS to build) is verified by the ascending qualification leg (IQ/OQ/PQ), with process validation of three conformance batches following PQ[^fda-process-validation-2011].

Cleaning is validated too, against a calculated **MACO** (Maximum Allowable Carryover) limit measured by swab or rinse with TOC/HPLC and micro acceptance criteria, never ‘looks clean.’ Scale the gowning, monitoring, and grade to what you actually run: a D-to-C envelope is normal for most hash operations, and over-building to Grade A/B that the product doesn't require simply wastes capital.

| Cadence | What is reviewed | Owner |
| --- | --- | --- |
| Per batch | Batch record, release results, deviations | QA reviewer |
| Weekly | EM trends, open deviations, OOS log | QA lead |
| Monthly | CAPA status, KPI dashboard | QA manager |
| Quarterly | Management review, supplier performance | QA director |
| Annually | Product Quality Review (PQR), self-inspection | Quality + ops |

*The fixed review cadence, from per-batch through annual.*

> **KEY — What 'compliant' actually means**
> 
> Not a perfect building: a _provable_ one. Compliant means every batch can be traced, every limit was met or the deviation was closed, and an inspector could reconstruct the whole story from the records alone. Specific limits and grades vary by jurisdiction, so validate against your own licence before you build.

Once the system runs, the contamination side of the picture is where most failures actually originate. Read the [mould-risk](mould-risk.html) paper next for that side of the build.

## References

[^ecfr-21cfr211]: U.S. Food and Drug Administration. 21 CFR Part 211, Current Good Manufacturing Practice for Finished Pharmaceuticals (esp. 211.22 Responsibilities of quality control unit; 211.165 Testing and release for distribution; 211.192 Production record review). Code of Federal Regulations, Title 21. https://www.ecfr.gov/current/title-21/chapter-I/subchapter-C/part-211 (industry/manufacturer source)
[^ich-q3c-r9-ema]: International Council for Harmonisation. ICH Q3C(R9) Guideline for Residual Solvents (Step 5), reproduced by European Medicines Agency, 2024. EMA/CHMP/ICH/82260/2006. https://www.ema.europa.eu/en/documents/scientific-guideline/ich-q3c-r9-guideline-impurities-guideline-residual-solvents-step-5_en.pdf (industry/manufacturer source)
[^ehp-cannabis-contaminants-2019]: Seltenrich N. Cannabis Contaminants: Regulating Solvents, Microbes, and Metals in Legal Weed. Environmental Health Perspectives. 2019;127(8):082001. doi:10.1289/EHP5785. https://ehp.niehs.nih.gov/doi/10.1289/EHP5785 (peer-reviewed)
[^en1822-h14-hepa]: Camfil. EN 1822 and ISO 29463 HEPA filter factory test (EN 1822-1:2019 filter classes; H14 minimum efficiency 99.995% at the Most Penetrating Particle Size, MPPS). https://www.camfil.com/en/insights/standard-and-regulations/en-1822-and-iso-29463-hepa-filter-factory-test (industry/manufacturer source)
[^sciencedirect-cleanroom-personnel-emissions-2024]: Meng H, Shiue A, Wang C, Leggett G. Particle and bacterial colony emissions from garments and humans in pharmaceutical cleanrooms. Journal of Building Engineering, 2024;96:110...; ScienceDirect S2352710224023970. https://www.sciencedirect.com/science/article/abs/pii/S2352710224023970 (peer-reviewed)
[^pmc-capa-ich-q10-2024]: Enhancing Pharmaceutical Product Quality With a Comprehensive Corrective and Preventive Actions (CAPA) Framework: From Reactive to Proactive. Cureus, 2024. PMC11490658. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11490658/ (peer-reviewed)
[^fda-process-validation-2011]: U.S. Food and Drug Administration, CDER/CBER/CVM. Guidance for Industry, Process Validation: General Principles and Practices. January 2011 (Revision 1). https://www.fda.gov/files/drugs/published/Process-Validation--General-Principles-and-Practices.pdf (industry/manufacturer source)
[^ispe-cleanroom-design-iso14644-16]: Pharmaceutical Engineering (ISPE). Pharmaceutical Cleanroom Design & ISO 14644-16, Sep/Oct 2021, air-change-rate optimization for classified cleanrooms. https://ispe.org/pharmaceutical-engineering/september-october-2021/pharmaceutical-cleanroom-design-iso-14644-16 (industry/manufacturer source)
