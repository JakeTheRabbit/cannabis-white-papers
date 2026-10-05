---
slug: "gmp-hash-lab"
title: "GMP hash lab: zones, flows, and batch release"
eyebrow: "Facility · GMP"
summary: "This paper gives the GMP requirements for a hash facility: the cleanroom grade zones, the flows of product and personnel, and the batch release. A batch must go through seven groups of tests and three release gates to get a signed Certificate of Analysis."
track: "Harvest, dry, trim and cure"
read_time: "~18 min to read"
diagrams: "13 diagrams"
related: ["mould-risk", "facility-3d"]
url: "https://www.growlabs.nz/wiki/gmp-hash-lab.html"
md_url: "https://www.growlabs.nz/wiki/papers/gmp-hash-lab.md"
version: "1.2"
updated: "2026-07-18"
license: "CC BY-NC 4.0"
license_url: "https://creativecommons.org/licenses/by-nc/4.0/"
attribution: "The Cannabis White Papers"
refs: [{"id": "ecfr-21cfr211", "n": 1, "cite": "U.S. Food and Drug Administration. 21 CFR Part 211, Current Good Manufacturing Practice for Finished Pharmaceuticals (esp. 211.22 Responsibilities of quality control unit; 211.165 Testing and release for distribution; 211.192 Production record review). Code of Federal Regulations, Title 21.", "url": "https://www.ecfr.gov/current/title-21/chapter-I/subchapter-C/part-211", "peer": false}, {"id": "ich-q3c-r9-ema", "n": 2, "cite": "International Council for Harmonisation. ICH Q3C(R9) Guideline for Residual Solvents (Step 5), reproduced by European Medicines Agency, 2024. EMA/CHMP/ICH/82260/2006.", "url": "https://www.ema.europa.eu/en/documents/scientific-guideline/ich-q3c-r9-guideline-impurities-guideline-residual-solvents-step-5_en.pdf", "peer": false}, {"id": "ehp-cannabis-contaminants-2019", "n": 3, "cite": "Seltenrich N. Cannabis Contaminants: Regulating Solvents, Microbes, and Metals in Legal Weed. Environmental Health Perspectives. 2019;127(8):082001. doi:10.1289/EHP5785.", "url": "https://ehp.niehs.nih.gov/doi/10.1289/EHP5785", "peer": true}, {"id": "en1822-h14-hepa", "n": 4, "cite": "Camfil. EN 1822 and ISO 29463 HEPA filter factory test (EN 1822-1:2019 filter classes; H14 minimum efficiency 99.995% at the Most Penetrating Particle Size, MPPS).", "url": "https://www.camfil.com/en/insights/standard-and-regulations/en-1822-and-iso-29463-hepa-filter-factory-test", "peer": false}, {"id": "sciencedirect-cleanroom-personnel-emissions-2024", "n": 5, "cite": "Meng H, Shiue A, Wang C, Leggett G. Particle and bacterial colony emissions from garments and humans in pharmaceutical cleanrooms. Journal of Building Engineering, 2024;96:110...; ScienceDirect S2352710224023970.", "url": "https://www.sciencedirect.com/science/article/abs/pii/S2352710224023970", "peer": true}, {"id": "pmc-capa-ich-q10-2024", "n": 6, "cite": "Enhancing Pharmaceutical Product Quality With a Comprehensive Corrective and Preventive Actions (CAPA) Framework: From Reactive to Proactive. Cureus, 2024. PMC11490658.", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11490658/", "peer": true}, {"id": "fda-process-validation-2011", "n": 7, "cite": "U.S. Food and Drug Administration, CDER/CBER/CVM. Guidance for Industry, Process Validation: General Principles and Practices. January 2011 (Revision 1).", "url": "https://www.fda.gov/files/drugs/published/Process-Validation--General-Principles-and-Practices.pdf", "peer": false}, {"id": "ispe-cleanroom-design-iso14644-16", "n": 8, "cite": "Pharmaceutical Engineering (ISPE). Pharmaceutical Cleanroom Design & ISO 14644-16, Sep/Oct 2021, air-change-rate optimization for classified cleanrooms.", "url": "https://ispe.org/pharmaceutical-engineering/september-october-2021/pharmaceutical-cleanroom-design-iso-14644-16", "peer": false}, {"id": "luca2020-pesticide-partition-hemp-extract", "n": 9, "cite": "Luca SV, Roehrer S, Kleigrewe K, Minceva M (2020). Approach for simultaneous cannabidiol isolation and pesticide removal from hemp extracts with liquid-liquid chromatography. Industrial Crops and Products 155:112726. doi:10.1016/j.indcrop.2020.112726.", "url": "https://doi.org/10.1016/j.indcrop.2020.112726", "peer": true}]
---

# GMP hash lab: zones, flows, and batch release

_Facility · GMP · ~18 min to read_

> This paper gives the GMP requirements for a hash facility: the cleanroom grade zones, the flows of product and personnel, and the batch release. A batch must go through seven groups of tests and three release gates to get a signed Certificate of Analysis.

## Purpose and scope

**Good Manufacturing Practice** (GMP) is a system with written records and audits. The system shows that a product agrees with its label, and that no dangerous material went into the product during production. A GMP hash lab makes purified resin concentrates (bubble hash, rosin, live resin, distillate) from cannabis biomass, with full control of contamination.

Extraction can increase the concentration of a contaminant, decrease it, or change where it is. The effect is different for each analyte, process, and mass yield[^luca2020-pesticide-partition-hemp-extract]. A flower result that is in the limits does not show that the finished concentrate agrees with the requirements. Do a test of the incoming material and of the finished batch. Then use the two sets of results to calculate the transfer for each process. Material goes to the next step only when the release data show that it is safe and that its label is correct.

Two sets of regulations give most of the requirements for the facility. **EU-GMP Annex 1** gives the cleanroom classifications and the contamination control strategy. The U.S. **cGMP regulations in 21 CFR 210/211** give the production controls, the records, and the authority of the quality unit to release product[^ecfr-21cfr211]. This paper is a reference model. It is not legal advice. The limits and grades are different in each jurisdiction.

> **KEY: The one basic requirement of GMP**
>
> ‘If there is no record, the task did not occur.’ GMP is a system with documents and validation, and an inspector can examine it. An auditor does not accept a very clean room that has no records. An auditor accepts a basic room that has full, signed records.

> **Diagram.** Four numbers are the primary values for the facility. There are five cleanliness grades. There are seven mandatory groups of release tests. The genealogy coverage is full. At the time of release, the number of open critical deviations must be zero.

| Standard | Content | Area of the facility that it controls |
| --- | --- | --- |
| EU-GMP Annex 1 | Classification of cleanrooms and the contamination control strategy | Each room that has a cleanroom class |
| cGMP 21 CFR 210/211 | Production controls, records, and the authority of the QC unit to release product | All the plant, and QA |
| ICH Q7 / Q9 / Q10 | Quality system, risk management, and lifecycle | Quality management system |
| ISO 14644-1 | Particle-count classes of cleanrooms (ISO 5/7/8) | Classification of air |
| GACP | Good Agricultural and Collection Practice for biomass | Goods-in and intake |
| NFPA 30 / C1D1 | Flammable liquids, and classified electrical areas | Solvent extraction room |

*The standards and the part of the building that each standard controls.*

## Definitions

These terms occur many times in this paper. The paper gives the full information about each term where the term first occurs.

**Cleanroom grade**: A symbol (CNC, D, C, B, A) that shows how clean the air of a room is. Each symbol agrees with an ISO 14644 particle class. Grade C is ISO 7, and Grade A is ISO 5.

**Batch / lot**: One specified production run with one lot ID. Personnel record each event of the batch with that ID. The record is the genealogy of the batch.

**Deviation**: Each difference from the approved process. Personnel record each deviation and do an investigation. The deviation must have the status Closed before the batch with the deviation can have the status Released.

**CAPA**: Corrective And Preventive Action. It is the loop that corrects the problem (corrective) and makes sure that the problem does not occur again (preventive).

**Quarantine / Released / Rejected**: The three statuses of a material. Each material has only one of these three statuses at one time. No material is between two statuses. The status of a material is always one of these three.

**CCP (Critical Control Point)**: A step in which a measured limit prevents a hazard (HACCP term). An example is wash water at less than 4 °C.

**ALCOA+**: The properties that a good record must have: Attributable, Legible, Contemporaneous, Original, Accurate, plus Complete, Consistent, Enduring, Available.

**Water activity (Aw)**: The free water that microbes can use, on a scale of 0 to 1. A low value prevents the growth of mold and bacteria. CoA is Certificate of Analysis. C1D1 is a classified room for flammable material.

QA is the Quality Assurance function. QA makes the last release decision, and QA operates independently of production[^ecfr-21cfr211]. This difference between QA and production is the primary part of the system. The personnel who send product out of the facility must not give the approval for their work.

> **Diagram.** The three statuses. A material has only one status at a time. The location of the material and its status in the system must always agree.

## Zones and cleanroom grades

The building is a set of shells of cleanliness. Each shell is in the next shell. The **dirty** tasks are intake, milling, and waste. They are at the outer edge. The **clean** tasks, with the highest cleanliness, are the collection, the fill, and the packaging of open product. They are in the inner zone.

The flow requirement is easy, and you must always obey it: **Product moves to the zones with more cleanliness, to the inner zone. Personnel and waste move to the dirty edge. Do not let the two flows go through the same area without control.** Between each pair of shells there is an airlock, and the grade changes by one step.In EU-GMP Annex 1, Grade C agrees with ISO 7 and Grade A agrees with ISO 5[^ispe-cleanroom-design-iso14644-16]. Most hash facilities for recreational cannabis and for medicinal cannabis use grades D to C. They use Grade C for the fill point, with local protection. A full Grade A or B is necessary only for sterile dose forms or pharmaceutical dose forms.

> **Diagram.** Each zone is in the next zone, from the CNC outer shell through Grade D and Grade C to the clean inner zone. Product goes to the clean inner zone. Personnel and waste go to the dirty edge.

> **Diagram.** The air-change rate increases with the grade. ISO 7 rooms (Grade C) have approximately 20 to 40 changes each hour[^ispe-cleanroom-design-iso14644-16]. A Grade A fill point with unidirectional airflow has a much higher rate.

| Room | Grade | ISO class | Air changes each hour (ACH) | Task |
| --- | --- | --- | --- | --- |
| Goods-in and quarantine | CNC | , | 4 to 6 | Personnel receive and hold the biomass. |
| Milling and dispensing | Grade D | ISO 8 | 10 to 20 | Personnel make the biomass smaller and weigh it. |
| Wash and extraction | Grade C | ISO 7 | 20 to 40 | Personnel remove the trichomes from the plant material. |
| Freeze-dry and press | Grade C | ISO 7 | 20 to 40 | Personnel dry the material and press it to make rosin. |
| Solvent recovery | Grade D (C1D1) | ISO 8 | 10 to 20 | Personnel recover the solvent and do an LEL purge. |
| Open-product fill | Grade A | ISO 5 | unidirectional | Personnel fill open product (pharmaceutical use). |

*Each room with its grade, ISO class, air-change rate, and primary task.*

## Pressure cascade, HVAC, and gowning

The primary medium for the movement of contamination in a cleanroom is air. Air flows from a high pressure to a low pressure, and not in the opposite direction. A **positive-pressure cascade** uses this effect.The clean rooms have a higher pressure than the adjacent dirtier spaces. Thus air always flows _out_ from clean to dirty. When you open a door, clean air flows out. Dirty air cannot flow back to the product.

The pressure increases in steps, from shell to shell. EU-GMP Annex 1 recommends that the difference between adjacent classified zones is approximately 10 to 15 Pa[^ispe-cleanroom-design-iso14644-16]. This difference gives these values: 0 Pa (CNC), +15 (D), +30 (C), +45 (B), and +60 (A). The solvent room is different: its pressure is **negative**, approximately -15 Pa. As a result, the flammable vapor stays in the room and flows to the LEL exhaust. It does not flow into the building.

> **Diagram.** Positive pressure that increases from CNC to the Grade A inner zone keeps the airflow from clean to dirty. The C1D1 solvent room has a negative pressure to contain vapor.

Personnel are the largest source of particles and microbes in a cleanroom[^sciencedirect-cleanroom-personnel-emissions-2024]. Thus entry is a one-way sequence of airlocks, and the gowning increases when the grade increases.Filtration also changes with the grade. The milling and dispensing rooms have F9 pre-filters. The wash and dry rooms have H13 HEPA filters. The fill point has H14 HEPA filters. An H14 HEPA filter stops a minimum of 99.995% of the particles at the most penetrating particle size[^en1822-h14-hepa]. Thus this filter is at the point with the highest cleanliness.

> **Diagram.** A one-way sequence of gowning from CNC entry, through the airlocks of each grade, to the work zone. A different exit, with a dashed line, is for the removal of the gown. Thus entry and exit do not use the same door.

> **WARN: Health check at the door**
>
> Do not let a person with an open wound, a respiratory illness, or gastrointestinal symptoms go into the cleanroom. Do a health check at the entry, and record each person that you stop. Each airlock has an interlock. Thus the two doors cannot open at the same time.

| Grade | Temperature | Relative humidity (RH) | Filtration | Pressure difference (ΔP) | Air changes each hour (ACH) |
| --- | --- | --- | --- | --- | --- |
| CNC | ambient | less than 70% | F7 | 0 Pa | 4 to 6 |
| Grade D | 18 to 24 °C | 45 to 60% | F9 | +15 Pa | 10 to 20 |
| Grade C | 18 to 22 °C | 45 to 55% | H13 HEPA | +30 Pa | 20 to 40 |
| Grade A fill | 18 to 22 °C | 45 to 55% | H14 HEPA | +60 Pa | unidirectional |
| Solvent (C1D1) | 18 to 24 °C | less than 55% | F9 | -15 Pa | 10 to 20 |

*The HVAC control values for each grade: temperature, humidity, filtration, pressure, and air changes.*

## Hash manufacturing process flow

Two processes start after the weigh-in. The **solventless** process removes the trichome heads (the resin glands) mechanically. The **solvent extraction** process dissolves the resin and then recovers the resin. The two processes make the same type of product, but their hazards are very different.

In the solventless process, personnel agitate fresh-frozen biomass in ice water. They sieve the resin through a stack of screens (220 to 25 micron). They freeze-dry the resin and press it to make rosin. The process has four **critical control points**: wash temperature (≤4 °C (39 °F)), water quality (RO, <10 CFU/mL), water activity (Aw ≤0.55), and press temperature (≤90 °C (194 °F)). A water activity of approximately 0.55 to 0.65 or less prevents the growth of microbes and fungi[^ehp-cannabis-contaminants-2019].

> **Diagram.** The solventless process: personnel agitate fresh-frozen biomass, sieve the resin, freeze-dry it, and press it. The figure shows the four critical control points.

Solvent extraction is a closed loop that uses butane, propane, ethanol, or CO₂. In this process, the primary hazards are **flammability** and **residual solvent**. Residual solvent is the trace of extraction solvent that stays in the product. The action limits for residual butane and propane are approximately 2000 to 5000 ppm, and the limit is different in each jurisdiction[^ich-q3c-r9-ema]. Ethanol is an ICH Q3C Class 3 solvent, and the usual limit for ethanol is approximately 5000 ppm[^ich-q3c-r9-ema]. Each batch must go through a headspace GC-MS test for residual solvent before the release of the batch.

> **Diagram.** Personnel fill the column, apply the solvent, filter and winterize, recover the solvent, and do a vacuum purge. The QC gate for residual solvent is the last step. The C1D1 safety interlocks operate at the same time.

> **DANGER: A hydrocarbon room must be a C1D1 room**
>
> Do butane and propane extraction only in a **C1D1** room (NFPA classification). The room must have LEL (lower explosive limit) gas sensors with an automatic purge. It must have explosion-proof electrical equipment, a two-person rule, and pressure vessels with an ASME rating. This area is the most dangerous area in the building. One source of ignition can cause very large damage.

In the solventless process, water is an **ingredient** and not a utility. The water uses a loop that is only for water. The water goes from the mains to a carbon and sediment pre-filter.Then it goes to RO/DI. Then it goes to a UV unit and a 0.2-micron last filter. Then it goes to a sanitized ice hopper, and then to the point of use. Personnel get samples at three points. Water that is out of specification goes to the quarantine area immediately.

> **Diagram.** The water treatment steps with their three sampling points and the quarantine procedure for water out of specification.

## Testing, sampling, and batch release

Personnel do tests at **three stages**: the incoming biomass, the process, and the release. The tests are at four sampling stations along the value stream. Personnel keep retained reference samples until 1 year after expiry. If a complaint occurs after the release, personnel can examine the kept material.

> **Diagram.** The stations go from incoming biomass (S1), through in-process (S2) and bulk concentrate (S3), to finished goods (S4). The figure shows the tests of each station.

The release panel for finished goods is the legal gate to the market. The panel has **seven groups of tests**: potency, residual solvents, pesticides, microbials, heavy metals, mycotoxins, and water activity and moisture[^ehp-cannabis-contaminants-2019]. Personnel measure the heavy metals (lead, cadmium, arsenic, mercury) with ICP-MS, the standard method[^ehp-cannabis-contaminants-2019]. The mycotoxins in the regulations are aflatoxins B1/B2/G1/G2 and ochratoxin A. They are carcinogens, and their limits are in parts per billion.

> **TIP: Test the finished concentrate**
>
> Extraction changes the distribution of the contaminants[^luca2020-pesticide-partition-hemp-extract]. Thus a raw flower result in the limits does not make sure that the finished concentrate is in the limits. Make the release decision on the finished concentrate. Use the input results and the output results of the same batch to set the carryover factors for each process.

| Group | Analytes | Method | Used for |
| --- | --- | --- | --- |
| Potency | THC, CBD, total cannabinoids | HPLC-DAD | Label accuracy |
| Residual solvents | Butane, propane, ethanol | Headspace GC-MS | Solvent safety |
| Pesticides | State pesticide list | LC-MS/MS, GC-MS/MS | Chemical safety |
| Microbials | TYMC, TAMC, E. coli, Salmonella, Aspergillus | Plate or qPCR | Pathogen control |
| Heavy metals | Pb, Cd, As, Hg | ICP-MS | Limits for toxic metals |
| Mycotoxins | Aflatoxins, ochratoxin A | LC-MS/MS | Carcinogen control |
| Water activity | Aw, moisture | Aw meter or KF | Mold prevention |

*The seven mandatory groups of release tests. Pathogens such as Salmonella and E. coli must not be in the product.*

Then QA, and not production, operates three gates one after the other. If the result of a gate is ‘no’, the batch goes to remediation. Only a batch that all three gates accept gets the release. The release has a QP/QA signature and a Certificate of Analysis that QA gives[^ecfr-21cfr211].

1. **Gate 1: Records**: Make sure that the batch record is full and signed from start to end (ALCOA+). If it is not, the batch cannot go to the next gate.
2. **Gate 2: Results**: Make sure that the results of all seven groups of tests are in the specification, with no pathogens. Each result out of specification (OOS) goes to an investigation.
3. **Gate 3: Deviations**: Make sure that all deviations of the batch have the status Closed, with a CAPA. A critical deviation with the status Open stops the release.
4. **Release**: When all three gates accept the batch, QA writes its signature and QA gives the CoA. Then the status changes to Released.

> **Diagram.** The three gates in sequence are records, results, and deviations. A batch goes to the QA release, or to hold, to OOS, or to remediation.

## Deviations, CAPA, and troubleshooting

When the process is different from the approved process, the **deviation system** finds the difference. ICH Q10 gives the pharmaceutical quality system, with CAPA and change control, and this loop is part of it[^pmc-capa-ich-q10-2024]. Each deviation has a CAPA loop of five stages. The deviation does _not_ get the status Closed until the last effectiveness check gives a correct result.

> **Diagram.** The loop has five stages: find, contain, examine, correct, and prevention with a check. A feedback arrow closes the loop back to the process[^pmc-capa-ich-q10-2024].

The severity of the deviation sets the time limit and the person who gives the approval. A **critical** deviation has a risk to the safety of patients or a risk of a recall. It goes to the QA director, and containment must occur in less than 24 hours. A **major** deviation goes to QA in a specified time. A **minor** deviation goes to a supervisor, and the supervisor examines the trend. Root-cause tools, for example 5-why and Ishikawa (fishbone) diagrams, are the standard methods to find the cause of the problem[^pmc-capa-ich-q10-2024].

> **WARN: The three frequent errors**
>
> - **You use the biomass CoA for the concentrate.** You think that the raw flower result shows that the concentrate is safe. You do not do a test of the concentrate. The important result is the result for the concentrate.
> - **You release a batch with a result for residual solvent near the limit.** Do not release the batch. Do the test again, do the purge again, or reject the batch. Record the decision for the batch.
> - **The status of the material and the status in the system are not the same.** Keep quarantine stock in a locked cage or on a controlled rack. The system and the shelf must always show the same status.

> **Diagram.** Rejected product and used biomass go into a locked quarantine cage. Personnel make them unusable. Then licensed disposal occurs with a manifest with a witness. Solvent waste is a different stream of dangerous material.

## Expected results and limitations

Compliance is a continuous process that personnel measure with data. It is not a task that you do one time. Management review monitors a small number of KPIs.The target for the right-first-time release rate is a minimum of 98%. The target for the deviation rate for each batch is less than 5%. The target for the median time to close a CAPA is a maximum of 30 days. The target for the results of environmental monitoring (EM) in the limits is a minimum of 95%. The target for the retrieval time in a mock recall is less than 24 hours.

> **Diagram.** The primary KPI targets with their thresholds. The system is in good condition when the right-first-time rate stays high and the deviation rate stays low.

Equipment must have a **qualification** before it makes product for release. The qualification follows the validation V-model: DQ (design), IQ (installation), OQ (operation), PQ (performance). Each of these stages makes sure that the stage on the opposite side of the V-model is correct.The qualification follows the IQ, OQ, PQ sequence[^fda-process-validation-2011]. Only then does the **process validation** start. Usually, it is three batches, one after the other, that agree with the specification. They show that the process gives the same result each time[^fda-process-validation-2011].

> **Diagram.** The design leg goes from the URS at the top to the assembly at the bottom. The qualification leg (IQ, OQ, PQ) goes from the bottom to the top, and it makes sure that the design leg is correct. Process validation of three batches that agree with the specification follows PQ[^fda-process-validation-2011].

Cleaning validation also uses a calculated **MACO** (Maximum Allowable Carryover) limit. Personnel measure the carryover with a swab sample or a rinse sample, with TOC or HPLC, and they use microbial acceptance criteria. ‘Looks clean’ is not an acceptance criterion.Select the gowning, the monitoring, and the grade for the process that you use. Grades D to C are usual for most hash operations. If Grade A or B is not necessary for the product, a facility with these grades is a waste of capital.

| Interval | Items for review | Owner |
| --- | --- | --- |
| For each batch | Batch record, release results, deviations | QA reviewer |
| Each week | EM trends, open deviations, OOS log | QA lead |
| Each month | CAPA status, KPI dashboard | QA manager |
| Each three months | Management review, supplier performance | QA director |
| Each year | Product Quality Review (PQR), self-inspection | Quality and operations |

*The set review intervals, from each batch to each year.*

> **KEY: Definition of 'compliant'**
>
> A compliant facility is not a building without faults. It is a building with _evidence_. In this building, each batch has traceability. For each limit, the result was in the limit, or the deviation had the status Closed.
> An inspector can find all the events of the batch in the records only. The limits and grades are different in each jurisdiction. Before you make the facility, make sure that it agrees with the conditions of your license.

When the system operates, most faults start on the contamination side. Next, read the paper [mold risk](mould-risk.html) for that side of the facility.

## References

[^ecfr-21cfr211]: U.S. Food and Drug Administration. 21 CFR Part 211, Current Good Manufacturing Practice for Finished Pharmaceuticals (esp. 211.22 Responsibilities of quality control unit; 211.165 Testing and release for distribution; 211.192 Production record review). Code of Federal Regulations, Title 21. https://www.ecfr.gov/current/title-21/chapter-I/subchapter-C/part-211 (source from a manufacturer or industry)
[^ich-q3c-r9-ema]: International Council for Harmonisation. ICH Q3C(R9) Guideline for Residual Solvents (Step 5), reproduced by European Medicines Agency, 2024. EMA/CHMP/ICH/82260/2006. https://www.ema.europa.eu/en/documents/scientific-guideline/ich-q3c-r9-guideline-impurities-guideline-residual-solvents-step-5_en.pdf (source from a manufacturer or industry)
[^ehp-cannabis-contaminants-2019]: Seltenrich N. Cannabis Contaminants: Regulating Solvents, Microbes, and Metals in Legal Weed. Environmental Health Perspectives. 2019;127(8):082001. doi:10.1289/EHP5785. https://ehp.niehs.nih.gov/doi/10.1289/EHP5785 (source with peer review)
[^en1822-h14-hepa]: Camfil. EN 1822 and ISO 29463 HEPA filter factory test (EN 1822-1:2019 filter classes; H14 minimum efficiency 99.995% at the Most Penetrating Particle Size, MPPS). https://www.camfil.com/en/insights/standard-and-regulations/en-1822-and-iso-29463-hepa-filter-factory-test (source from a manufacturer or industry)
[^sciencedirect-cleanroom-personnel-emissions-2024]: Meng H, Shiue A, Wang C, Leggett G. Particle and bacterial colony emissions from garments and humans in pharmaceutical cleanrooms. Journal of Building Engineering, 2024;96:110...; ScienceDirect S2352710224023970. https://www.sciencedirect.com/science/article/abs/pii/S2352710224023970 (source with peer review)
[^pmc-capa-ich-q10-2024]: Enhancing Pharmaceutical Product Quality With a Comprehensive Corrective and Preventive Actions (CAPA) Framework: From Reactive to Proactive. Cureus, 2024. PMC11490658. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11490658/ (source with peer review)
[^fda-process-validation-2011]: U.S. Food and Drug Administration, CDER/CBER/CVM. Guidance for Industry, Process Validation: General Principles and Practices. January 2011 (Revision 1). https://www.fda.gov/files/drugs/published/Process-Validation--General-Principles-and-Practices.pdf (source from a manufacturer or industry)
[^ispe-cleanroom-design-iso14644-16]: Pharmaceutical Engineering (ISPE). Pharmaceutical Cleanroom Design & ISO 14644-16, Sep/Oct 2021, air-change-rate optimization for classified cleanrooms. https://ispe.org/pharmaceutical-engineering/september-october-2021/pharmaceutical-cleanroom-design-iso-14644-16 (source from a manufacturer or industry)
[^luca2020-pesticide-partition-hemp-extract]: Luca SV, Roehrer S, Kleigrewe K, Minceva M (2020). Approach for simultaneous cannabidiol isolation and pesticide removal from hemp extracts with liquid-liquid chromatography. Industrial Crops and Products 155:112726. doi:10.1016/j.indcrop.2020.112726. https://doi.org/10.1016/j.indcrop.2020.112726 (source with peer review)
