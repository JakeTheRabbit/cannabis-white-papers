# -*- coding: utf-8 -*-
"""Render structured Auckland IPM content into the repo's paper section model."""

from components import (
    p,
    lead,
    h,
    ul,
    ol,
    callout,
    defterm,
    table,
    figure,
    photo,
    term_gallery,
    stagecard,
    grid,
    card,
    kv,
    steps,
)
import figs_lib as L

from ipm_blueprint.content import (
    APPROVED_TOOL_FIELDS,
    ATLAS,
    BENEFICIAL_ROWS,
    CONTROL_LAYERS,
    GLOSSARY,
    LEGAL_GATES,
    REFERENCE_PLATES,
    REF_IDS,
    SCOUT_FIELDS,
    SEVERITY,
)


def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (
        rid,
        REF_IDS.index(rid) + 1,
    )


def _atlas_profile(entry, number):
    evidence = "".join(_c(rid) for rid in entry.get("refs", []))
    return "".join(
        [
            h(3, f"{number}. {entry['name']} ({entry['scientific']})"),
            photo(
                entry["image"],
                entry["identify"] + " <strong>An AI tool made this photo. The photo does not show the correct sizes, and the magnification that you see is not the same on all photos.</strong>",
                entry["alt"],
                "OpenAI image generation",
            ),
            kv(
                [
                    ("First signs that show the problem correctly", entry["signs"]),
                    ("Life cycle and movement", entry["biology"]),
                    ("Development and the conditions that change it", entry["development"]),
                    ("Size and magnification for inspection", entry["scale"]),
                    ("Where to look", entry["inspect"]),
                    ("Identification check", entry["confirm"]),
                    ("Problems with the same signs", entry["lookalikes"]),
                    ("Facility threshold", entry["threshold"]),
                    ("First response", entry["response"]),
                    ("Control methods for each layer", entry["controls"]),
                    ("Target stage and plant part", entry["targeting"]),
                    ("Limits from the crop, the workers, the residue and compatibility", entry["constraints"]),
                    ("How to collect and keep the specimen", entry["specimen"]),
                    ("Recheck date and the condition for a good result", entry["recheck"]),
                    ("Source trace and CAPA trigger", entry["capa"]),
                ]
            ),
            p("References for this profile: " + evidence),
        ]
    )


def _input(name, label, wide=False):
    cls = "facility-input wide" if wide else "facility-input"
    if wide:
        field = f"<textarea name='{name}' rows='3'>FACILITY INPUT</textarea>"
    else:
        field = f"<input name='{name}' value='FACILITY INPUT'>"
    return f"<label class='{cls}'><span>{label}</span>{field}</label>"


def build_sections():
    sections = []

    sections.append(
        {
            "id": "how-to-use",
            "kicker": "01 · Read this first",
            "title": "Purpose and scope",
            "blocks": [
                lead(
                    "This blueprint is for the operation of an indoor medicinal cannabis facility "
                    "in Auckland. It connects the identification of pests and diseases to clean "
                    "stock and to the safety of workers. It also connects the identification to the "
                    "regulations for products and organisms in New Zealand. It connects the "
                    "identification to the release of batches after the residue test, to "
                    "traceability and to CAPA. We do not want you to have the most sprays. We want "
                    "you to have an alternative when a pest or disease problem and a compliance "
                    "problem occur at the same time."
                ),
                p(
                    "We used the supplied 128-page IPM Book V15 to compare the coverage of this "
                    "paper with the book" + _c("athena-ipm-book-v15") + ". The book includes these "
                    "parts: the basic information about IPM, cultural controls, environmental "
                    "controls, biological controls and chemical controls. It also includes how to "
                    "make a program, eight arthropod profiles, six disease profiles, aids for "
                    "identification, a glossary and tools for operators. This paper is not a copy "
                    "of the book. It does not contain the commercial programs of the book, its "
                    "figures or its rates. For this paper, sources of the authorities in New "
                    "Zealand and primary literature are more important than the book."
                ),
                callout(
                    "danger",
                    "An AI tool made the photos for training",
                    p(
                        "Use a photo to select where to look and which part of the plant to collect "
                        "as a sample. Do not use a photo to make sure that you know the species. An "
                        "AI tool made each photo in this paper. Microscopy is necessary for broad "
                        "mites and russet mites, and RT-qPCR or RT-PCR is necessary for HLVd. A "
                        "diagnostic laboratory is frequently necessary for root diseases and leaf "
                        "diseases. A photo that shows the correct signs is not a test result."
                    ),
                ),
                ul(
                    [
                        "<strong>The current status is more important than this paper.</strong> Examine the current information each time that you get or use a product. Use the information from the Ministry, ACVM, EPA, WorkSafe, the label and the SDS.",
                        "<strong>The thresholds of a facility are controlled values.</strong> The numbers in this blueprint are examples or start values. Use a number from this blueprint only if your approved SOP includes it.",
                        "<strong>Previous damage stays on the plant.</strong> Examine living organisms, new lesions, new growth, traps, roots or laboratory results. Use them to make sure that a control had the correct effect. A plant that is in better condition is not a sign of the effect.",
                        "<strong>Clean stock is the most important part.</strong> A problem in the mother room increases in each clone lot. Thus give the mother room the best protection.",
                    ]
                ),
                figure(
                    L.flow(
                        "From data to task",
                        [
                            ("Monitor", "map scouting, traps, environment or test"),
                            ("Confirm", "microscopy or laboratory where necessary"),
                            ("Classify", "room, incidence, severity, trend, zero-tolerance"),
                            ("Select", "regulation + efficacy + compatibility + residue limit"),
                            ("Examine", "recheck, record, stop or CAPA"),
                        ],
                    ),
                    1,
                    "The figure shows the control sequence. If you do not do the identification check or the legal gate, a small pest or disease problem can become a batch problem.",
                ),
            ],
        }
    )

    sections.append(
        {
            "id": "glossary",
            "kicker": "02 · Reference",
            "title": "Definitions",
            "blocks": [
                p("This section gives the terms for biology, diagnosis, operation and the regulations of New Zealand. The blueprint uses these terms."),
                grid([defterm(term, definition) for term, definition in GLOSSARY], cols=2),
            ],
        }
    )

    sections.append(
        {
            "id": "ipm-system",
            "kicker": "03 · System",
            "title": "Basic information about IPM, control layers and the feedback loop",
            "blocks": [
                p(
                    "IPM is a loop with these steps: prevent the movement of pests into the "
                    "facility, monitor with the same procedure each time, and identify correctly. "
                    "Then compare the finding with a controlled threshold, use compatible controls "
                    "together, record the result and do a recheck. If the recheck shows that the "
                    "result is not satisfactory, the loop starts again with a stronger response. "
                    "The reference on arthropods and the cannabis literature agree with control in "
                    "layers for an indoor crop, and not with one product on a calendar" +
                    _c("ahmed-2024-hemp-pests-florida-jipm") + "."
                ),
                figure(
                    L.flow(
                        "The IPM decision loop",
                        [
                            ("Prevent", "exclusion, sanitation, clean stock"),
                            ("Monitor", "same route, traps, roots, environment"),
                            ("Identify", "organism + life stage + source"),
                            ("Threshold", "risk + incidence + severity + trend"),
                            ("Control + check", "control layers, recheck, record"),
                        ],
                    ),
                    2,
                    "After each control step, do the monitoring again. If you do not do a recheck, the step is only a task and is not control.",
                ),
                table(
                    ["Layer", "Function", "Instruction"],
                    [[name, body, "Use this layer before you use a higher layer."] for name, body in CONTROL_LAYERS],
                    cls="compact",
                    caption="The table shows the control layers in the correct sequence for the operation. Chemical products and low-risk products are in the last layer. They can have the correct effect, but the regulations and the compatibility give them more limits than the products of the other layers.",
                ),
                callout(
                    "key",
                    "Zero tolerance is not the same as the removal of all pests from all areas",
                    p(
                        "HLVd in clean stock and broad mites or russet mites in quarantine are "
                        "exclusion events or quality events. Root aphids in propagation, powdery "
                        "mildew on flowers and Botrytis in a bud are also exclusion events or "
                        "quality events. A low count of adult fungus gnats in a vegetative room "
                        "that is in operation can be a problem that you monitor with trend data. "
                        "Use the organism and the consequence for the room. Do not use one number "
                        "for all organisms and rooms."
                    ),
                ),
                table(
                    ["Severity", "Name", "Definition", "Standard response"],
                    [[n, name, definition, "Monitor" if n == "0" else "Escalate. Use the approved decision matrix."] for n, name, definition in SEVERITY],
                    cls="compact",
                    caption="This table is a severity scale for the site. You must also use the incidence and the trend. For some organisms, zero tolerance is more important than the scale.",
                ),
            ],
        }
    )

    sections.append(
        {
            "id": "nz-legal-gate",
            "kicker": "04 · New Zealand legal gate",
            "title": "The legal gate for IPM controls in NZ",
            "blocks": [
                lead(
                    "In New Zealand, no one document has all the regulations for pests in medicinal "
                    "cannabis. The decision uses these sources of regulations: the regulations for "
                    "medicinal cannabis and the minimum quality standard, ACVM, and the controls of "
                    "HSNO and EPA. It also uses WorkSafe, the release of batches after laboratory "
                    "tests, and the requirements of Auckland for trade waste and for the "
                    "environment."
                ),
                p(
                    "Regulation 18 has limits on the treatment of cannabis crops with pesticides. "
                    "Regulation 7 gives the residues for which a test is necessary and the limits "
                    "for these residues. The current guidance of the Ministry shows the difference "
                    "between inhalation pathways and non-inhalation pathways. The guidance also "
                    "clearly keeps the requirements of ACVM and HSNO" + _c("moh-nz-pesticide-use-2024") +
                    _c("moh-nz-mqs-2026") + ". A residue panel can include abamectin, spinosad, "
                    "pyrethrins or a different analyte. A substance in the panel does not show that "
                    "the regulations let you apply it."
                ),
                p(
                    "For most agricultural compounds, ACVM registration is necessary. Some classes "
                    "of product have an exemption, but you must obey the conditions of the "
                    "exemption and the other regulations" + _c("mpi-nz-acvm-exempt") +
                    ". You must make sure that the approvals and the controls of the EPA are "
                    "correct. This check includes the approval information in section 15 of the "
                    "current New Zealand SDS" + _c("epa-nz-hsno-approvals") + "."
                ),
                steps(LEGAL_GATES),
                callout(
                    "warn",
                    "Do not write SKUs, rates, PHIs or REIs in a general paper",
                    p(
                        "Record these values in the approved-input register with the current label "
                        "and SDS. Use version control for the register. WorkSafe tells you that the "
                        "REI is different for each product, crop, application and exposure. For an "
                        "application that is not on the label, a risk assessment for that "
                        "application is necessary. An indoor area with an REI must have warning "
                        "signs and controlled access" + _c("worksafe-nz-rei") +
                        "."
                    ),
                ),
                table(
                    ["Class of product or organism", "Initial status", "Items to examine"],
                    [
                        ["Soaps of fatty acids and permitted salts", "Possible low-risk contact alternative", "The correct pathway for medicinal cannabis, the approval of the product, the crop site, residue and quality, PPE and REI"],
                        ["Sulfur", "Possible inhalation pathway for the active ingredient", "The approval of the product, the exposure in the indoor area, the limits for the crop stage and the quality, compatibility, and the current label"],
                        ["Hydrogen peroxide", "Possible active pathway for specified applications", "Contact with the crop compared with sanitation of pipes and surfaces, concentration, exposure of workers, phytotoxicity and the discharge route"],
                        ["Active ingredients from food and from permitted food additives", "Possible pathway only if you obey all the conditions", "Conditions for novel food and for composition. The ACVM and HSNO status of the product. The application that you do and the laboratory test route."],
                        ["Active ingredients that are microbes", "The regulation pathway has the names of some species and strains", "The correct species, strain and product. Viability in the application. ACVM and HSNO status. Effects on organisms that are not the target and on beneficial organisms. The label."],
                        ["Conventional pesticide for food crops", "Not automatically an inhalation pathway", "A permitted non-inhalation pathway or a permitted pathway for medicinal cannabis, if there is one. Also how to calculate the residue and how to do the residue tests."],
                        ["Beneficial organism", "Not the same as an active ingredient of a pesticide", "The current status of the organism, the import route and the release route, the supplier, the cold chain, containment, and compatibility with the facility"],
                    ],
                    cls="compact",
                    caption="This table is a first check of pathways. It does not tell you which product to select. The approved-input register shows the current status.",
                ),
                p(
                    "A laboratory can do the tests for pesticides and for the other non-critical "
                    "quality attributes of the minimum quality standard. The laboratory must have "
                    "GMP or ISO/IEC 17025:2017 with the correct scope. For critical quality "
                    "attributes, the laboratory must have GMP. Before you use a release procedure, "
                    "make sure that the scope and the method of the laboratory are correct" +
                    _c("moh-nz-mqs-2026") + "."
                ),
            ],
        }
    )

    sections.append(
        {
            "id": "clean-stock",
            "kicker": "05 · Exclusion",
            "title": "Clean-stock controls in IPM",
            "blocks": [
                lead(
                    "The mother room is not only the area where clones start. It is a system for "
                    "starting material. A problem in the mother room increases in each cutting, "
                    "room and batch downstream."
                ),
                p(
                    "A plant with HLVd can show no symptoms. HLVd moves easily with vegetative "
                    "propagation and with tools that have contamination. Investigations show a risk "
                    "that HLVd can move through roots and through recirculating hydroponic solution" +
                    _c("hlvd_threat2023") + _c("hlvd_mgmt2025") + _c("hlvd-transmission-2025") +
                    ". Thus a visual check of the plant is not a test for release."
                ),
                figure(
                    L.flow(
                        "New genetics",
                        [
                            ("Receive", "approved source + accession ID"),
                            ("Quarantine", "dedicated air, water, tools and personnel"),
                            ("Examine + traps", "arthropods, roots, symptoms"),
                            ("HLVd test", "validated method and tissue for HLVd"),
                            ("Release or destroy", "trace tree starts before release"),
                        ],
                    ),
                    3,
                    "All genetics must go through quarantine. Do not release an accession only because a visual check is satisfactory.",
                ),
                ul(
                    [
                        "Make foundation mothers only from released material. Foundation mothers have the best controls.",
                        "You can trace the parent of each production mother, cutting lot and room.",
                        "Sanitize tools between specified groups of plants. Do not sanitize tools only at the end of the work period.",
                        "Quarantine, foundation stock and production stock do not use the same nutrient solution. They do not use the same return water without validation.",
                        "Before you collect the first sample, write the procedure for a positive result or an inconclusive result. The procedure must show how to hold the plants, do the test again, destroy the plants and do the traceback.",
                    ]
                ),
                table(
                    ["Class of plant", "Typical frequency", "Instruction for sampling", "Instruction for the decision"],
                    [
                        ["Received accession", "At receipt, and again before release from quarantine if the risk makes it necessary", "One sample for each plant. Validated tissue and validated method.", "Do not release the accession until it agrees with the release criteria."],
                        ["Foundation mother", "When you make the mother, and then at the times that the risk makes necessary", "Do one test for each plant. Do not use pooled samples as the usual method, unless you validate the pooled sample.", "Positive result: destroy the mother, hold the connected clones, do an investigation."],
                        ["Production mother", "Before a large production of cuttings, or at the times that the site selects", "One sample for each plant or a validated pooled sample, with reflex testing", "Positive result: stop the movement of clones and trace the clones since the last negative result that you know is correct."],
                        ["Clone lot", "A check that the risk and the status of the mother make necessary", "A sampling procedure for each lot, with controls", "Hold the connected rooms if the status of the source has a problem."],
                        ["Hydro environment", "Investigation or sentinel testing if there is a risk in the system", "Tank, return water and root interface, with a validated method", "A positive result from the hydro environment starts an investigation of all the connected plants. The result does not give an automatic diagnosis of one plant."],
                    ],
                    cls="compact",
                    caption="The table gives typical frequencies only. The controlled sampling procedure must agree with the laboratory method, the age of the plant, the tissue, the risk and the records of the facility.",
                ),
                callout(
                    "danger",
                    "A test each month gives no protection if the genealogy is broken",
                    p(
                        "Make the trace tree first. You must identify each clone lot since the last "
                        "negative result that you know is correct. If you cannot, you do not know "
                        "which rooms have the problem after a positive result for a mother."
                    ),
                ),
            ],
        }
    )

    sections.append(
        {
            "id": "facility-pathways",
            "kicker": "06 · Contamination pathways",
            "title": "Facility contamination pathways",
            "blocks": [
                p(
                    "A vector can move a pest or a pathogen from one area to a different area. It "
                    "is not important which group of personnel has the vector. A clean-stock "
                    "program gives no protection if a worker goes back to a clean area or if "
                    "scissors go between mothers. It also gives no protection if return air "
                    "connects to quarantine or if a reservoir for more than one area moves root "
                    "pathogens. References on cannabis diseases frequently show these routes of "
                    "contamination: stock, tools, water, debris, density and the conditions of the "
                    "environment. The routes have an effect on each other" +
                    _c("punja-2021-emerging-diseases-cannabis") + "."
                ),
                figure(
                    L.flow(
                        "Hygiene gradient, one direction",
                        [
                            ("Clean supplies", "storage, clean PPE, released products"),
                            ("Foundation", "clean stock, dedicated tools and personnel"),
                            ("Production", "mothers, clones, growth, flower"),
                            ("Containment", "quarantine, suspect and treated areas"),
                            ("Waste exit", "bags, records, one direction"),
                        ],
                    ),
                    4,
                    "Movement is usually from clean areas to dirty areas. If an approved exception lets a person go back to a clean area, the person must do a full decontamination first. You must record the exception.",
                ),
                grid(
                    [
                        card("Personnel", "Use gowning for each room class. Move from clean areas to dirty areas in each work period. Do not go back to a clean area without a record. Use controls for the treated areas. Keep training records for the site."),
                        card("Tools", "Keep tools for one room or one plant class only. Make sure that the sanitizer concentration and the contact time are correct. Sanitize tools between groups of plants. Make it easy to know if a tool is clean or dirty."),
                        card("Air", "Isolate quarantine from the other areas. Set the difference of pressure between rooms. Use filtered supply air. Do not use the same return air for an area with contamination and for a clean area. Make a map of the air movement in the canopy and of the dead zones. Do checks for condensation."),
                        card("Water", "Where the consequence of a problem is high, use dedicated tanks and circuits. Do not use recirculating water without validation. Use biofilm control. Make a map of the drains. Prevent backflow."),
                        card("Plants and materials", "Use approved sources. Seal waste. Use clean media and clean pots. Use controls for the beneficial organisms that you receive. Do not let cardboard or packaging go into clean rooms."),
                        card("Waste", "Put crop waste in bags in the room. Record the waste. Contain rinse water and spill liquids. Use approved disposal pathways and trade waste pathways. Do not send waste to stormwater."),
                    ],
                    cols=2,
                ),
                p(
                    "A trade waste agreement with Watercare is necessary if the discharge of a "
                    "facility is not low risk. The trade waste agreement gives the controls and the "
                    "monitoring for the site" + _c("watercare-nz-trade-waste") +
                    ". In the E33 requirements of Auckland, the primary task is to prevent the "
                    "discharge of contaminants. The requirements also make it necessary to have the "
                    "correct control on the site, containment, treatment or permitted disposal" +
                    _c("auckland-unitary-plan-e33") + ". The address of the site, the drainage and "
                    "the classification of the operation are data that the facility must supply."
                ),
            ],
        }
    )

    sections.append(
        {
            "id": "cultural-environmental",
            "kicker": "07 · Prevention",
            "title": "Cultural controls and environmental controls",
            "blocks": [
                p(
                    "These controls continue to operate when the facility becomes larger. Remove "
                    "weeds, algae and plant debris. Keep doors, screens and barriers in good "
                    "condition. Put each source of genetics in quarantine. Move personnel and "
                    "material in one direction.</p><p>Keep the same scouting route. Measure the "
                    "conditions of the root zone and of the canopy. Set the conditions correctly. "
                    "These controls decrease the risk that pests go into the facility, and the rate "
                    "of movement of pests in the facility."
                ),
                table(
                    ["Control point", "Minimum check", "Sign of a problem", "Correction"],
                    [
                        ["External and internal pest reservoirs", "Weeds, algae, drains, debris and standing water", "Frequent high counts of small flies, or pest reservoirs", "Remove the source. Repair the drainage and the leaks. Clean the area. Examine the result."],
                        ["Sanitizer", "Product, concentration, contact time, and a clean surface", "No record of the concentration, a dirty surface, or removal of the sanitizer before the end of the contact time", "Mix the sanitizer again. Clean the surface first. Use the full contact time again."],
                        ["Canopy air", "Air speed at typical points, dead zones and movement of leaves", "Areas with high density and no air movement, condensation, or a zone with frequent Botrytis or powdery mildew", "Adjust the fans and the HVAC, and decrease the density of the canopy"],
                        ["The change from day to night", "Temperature of leaves and surfaces, RH, and the dew-point margin", "Condensation, or a small dew-point margin while the lights are off", "Change humidity removal, air movement, temperature ramp and the time of irrigation"],
                        ["Root zone", "Temperature, dissolved oxygen if it is important, moisture pattern, drain, biofilm and algae", "Warm saturated roots, drainage that is not satisfactory, sloughing, or the same symptoms in the plants of a cohort", "Correct the irrigation, the oxygen and the heat. Isolate the plants. Do a diagnosis."],
                        ["Sticky traps", "ID, color, height, date, and a clean surface that you can read", "Traps that are not on the map, or counts with no position and no record of previous counts", "Replace the traps. Put the traps on the map. Use the same procedure to read the traps."],
                    ],
                    cls="compact",
                    caption="A prevention check must give a result that you can see, which is satisfactory or unsatisfactory. A general instruction to keep the room clean is not a check.",
                ),
                callout(
                    "note",
                    "Room RH is not the leaf microclimate",
                    p(
                        "A canopy with high density, cold surfaces, the time of irrigation and the "
                        "change to darkness can cause wet tissue, or tissue near condensation. At "
                        "the same time, the wall sensor can show a satisfactory value. Measure the "
                        "conditions in the areas where the risk is. Record the trigger for a "
                        "correction."
                    ),
                ),
                figure(
                    L.flow(
                        "Scouting route each week",
                        [
                            ("Prepare", "clean kit, map, previous trends, room sequence"),
                            ("Traps", "read IDs, keep unknown organisms, replace"),
                            ("Plants", "top, underside, meristem, stem, flower"),
                            ("Roots", "media, crown, drain, roots for samples"),
                            ("Record", "photos, samples, threshold, owner, recheck"),
                        ],
                    ),
                    5,
                    "Use the same scouting route, the same points and the same plant parts. Thus you can compare the trend data.",
                ),
            ],
        }
    )

    sections.append(
        {
            "id": "biological-controls",
            "kicker": "08 · Controls with living organisms",
            "title": "Biological control programs",
            "blocks": [
                p(
                    "A biological control program gives a satisfactory result when all of these "
                    "conditions occur. The organism that you receive must be the correct organism "
                    "and a living organism. You release it into a crop and a climate that are "
                    "correct for it. It survives the residues that are in the crop, finds the "
                    "target stage and establishes where necessary. You do a check to make sure that "
                    "the result is satisfactory. Generalist predators and specialist predators are "
                    "not interchangeable, and aphid parasitoids and whitefly parasitoids are not "
                    "interchangeable" + _c("lopez-2023-amblyseius-swirskii-review-jipm") +
                    _c("vanmaanen-2010-broad-mite-swirskii-biocontrol") + "."
                ),
                table(
                    ["Control group", "Typical function", "Checks for the release procedure"],
                    BENEFICIAL_ROWS,
                    cls="compact",
                    caption="The table shows only the groups and the function of each group. Before you select a beneficial organism, make sure that you know the current status of the organism in New Zealand. Make sure that a supplier can supply the organism and that the regulations let you use it.",
                ),
                steps(
                    [
                        ("Get approval", "Make sure that you know which organism or product you will use, and the name of the supplier. Make sure that you know the legal status in NZ, the compatibility and the target stage."),
                        ("Receive", "Record the lot, and the time and temperature when you receive the product or organism. Record the condition of the packaging, the expiry date and the period in which you can use it."),
                        ("Examine viability", "Use the method of the supplier. Examine the movement, the counts, the survival of nematodes or the condition of microbes. Reject material that is not satisfactory."),
                        ("Release", "Make a map of the release rate and the release location. Compare the map with the crop stage, the areas where the pest is, and the conditions of the environment."),
                        ("Establish", "Look for predators, hosts that have parasitoids, mummies, a smaller number of the prey stage, or other specified evidence."),
                        ("Correct", "If the organisms do not establish, find the cause. The cause can be dead organisms, an incorrect species or stage, climate, residues, the time of release or application."),
                    ]
                ),
                p(
                    "Make sure that the regulations let the species of the invertebrate come into "
                    "New Zealand. Make sure that you have the permits and the facilities that are "
                    "necessary. Obey the biosecurity requirements and HSNO. Do not use the list of "
                    "products of a supplier in a different country as the release list for NZ" +
                    _c("mpi-nz-invertebrate-import") + "."
                ),
            ],
        }
    )

    sections.append(
        {
            "id": "input-application",
            "kicker": "09 · Controlled exception",
            "title": "Selection and application of products",
            "blocks": [
                p(
                    "When a finding is more than the threshold, select the smallest number of "
                    "controls. The controls must have an effect on the confirmed organism, the life "
                    "stage and the plant part. The controls must agree with the regulations, be "
                    "safe for workers, be compatible with the beneficial organisms, and not stop "
                    "the release of batches. Where it is important, change the IRAC group or the "
                    "FRAC group each time that you apply a control. You must also make sure that "
                    "physical controls and controls with living organisms are compatible."
                ),
                table(
                    ["Mode", "Function", "Typical problem"],
                    [
                        ["Contact control", "Kills only the organisms that the spray touches", "Coverage that is not satisfactory on the leaf underside or the flower, or life stages in areas that the spray cannot touch"],
                        ["Smothering or desiccation", "Causes mechanical damage to soft-bodied pests", "Damage to the crop at some stages, coverage that is not full, or no compatibility"],
                        ["Microbe that is an insect pathogen", "Causes an infection in a pest stage that this microbe can infect, if the conditions are correct", "Incorrect stage, low viability, humidity that is not correct, or residue that is not compatible"],
                        ["Predator or parasitoid", "A predator eats the target pest. A parasitoid has its development in the target pest.", "A release after the correct time, an incorrect host, dead organisms when you receive them, or no establishment"],
                        ["Root-zone antagonist", "Decreases the establishment and the quantity of the pathogen", "A person uses it to repair dead roots, or mixes it with a sanitizer that kills it"],
                        ["Oxidation and sanitation", "Decreases contamination on the validated application site", "You think that a rate for the sanitation of pipes and surfaces is safe, or has efficacy, on the plants of the crop"],
                        ["Correction of the environment", "Removes a condition that helps the problem", "Correction of the room average only, when the microclimate is not correct"],
                    ],
                    cls="compact",
                    caption="The table gives modes only. It does not give a product. Get the product, the application site and the rate from the controlled register and from the current label and SDS.",
                ),
                callout(
                    "warn",
                    "The quality of the application is part of the efficacy",
                    p(
                        "Calibrate the output. Make sure that the water is correct. Add the "
                        "products in the correct sequence. Make sure that the agitation is correct. "
                        "Select the nozzle, the pressure and the coverage of the target. Set the "
                        "lights and the HVAC correctly.</p><p>Contain the runoff. Clean the "
                        "equipment. Put warning signs in position for the REI. Do a phytotoxicity "
                        "test on a small area of the crop if your approved SOP makes it necessary. "
                        "A product that the regulations let you use gives an unsatisfactory result "
                        "if you apply it incorrectly."
                    ),
                ),
                table(
                    ["Approved-input register field", "Necessary"],
                    [[field, "Yes"] for field in APPROVED_TOOL_FIELDS],
                    cls="compact",
                    caption="Do not release a product to storage until you complete each applicable field and each field has approval.",
                ),
            ],
        }
    )

    arthropods = [entry for entry in ATLAS if entry["kind"] == "arthropod"]
    sections.append(
        {
            "id": "arthropod-atlas",
            "kicker": "10 · Field atlas",
            "title": "Arthropod identification",
            "blocks": [
                lead(
                    "The photo is the start of the diagnosis. Examine the morphology to make sure "
                    "that the identification is correct. Collect a sample from the correct plant "
                    "part. Find the difference between the organism and the problems with the same "
                    "signs. Then select controls that have an effect on the life stage that you "
                    "found."
                ),
                p(
                    "Cannabis has many different piercing-sucking pests and many pests in the root "
                    "zone. Primary references show that, for control in an indoor crop, it is "
                    "important to know the correct identification, the life cycle and the plant "
                    "location" + _c("ahmed-2024-hemp-pests-florida-jipm") +
                    _c("pulkoski-burrack-2023-piercing-sucking-hemp") + "."
                ),
            ]
            + [_atlas_profile(entry, i + 1) for i, entry in enumerate(arthropods)],
        }
    )

    diseases = [entry for entry in ATLAS if entry["kind"] == "disease"]
    sections.append(
        {
            "id": "disease-atlas",
            "kicker": "11 · Field atlas",
            "title": "Disease diagnosis and sampling",
            "blocks": [
                lead(
                    "Disease symptoms can be the same for different diseases. Use the symptoms to "
                    "select the tissue, the records of the environment and the correct laboratory "
                    "route. Do not make a release decision only because a symptom agrees with a "
                    "photo."
                ),
                p(
                    "The cannabis literature on diseases gives evidence for different controls for "
                    "powdery mildew, Botrytis, Pythium, Fusarium and systemic pathogens in "
                    "propagation" + _c("scott-punja-2021-powdery-mildew-management") +
                    _c("mahmoud-2023-botrytis-budrot") + _c("punja-2023-fusarium-pythium-biocontrol") +
                    ". Related species of Septoria make the diagnosis not easy. Thus the color of "
                    "the lesion is not sufficient for the diagnosis" +
                    _c("rahnama-2021-septoria-cannabis") + _c("ujata-2024-septoria-cannabicola") +
                    "."
                ),
            ]
            + [_atlas_profile(entry, i + 1) for i, entry in enumerate(diseases)],
        }
    )

    sections.append(
        {
            "id": "lookalikes",
            "kicker": "12 · Controls for diagnosis",
            "title": "Problems with the same signs",
            "blocks": [
                p(
                    "An atlas without reference plants in good condition makes personnel see "
                    "disease in all plants. Compare the same parts: underside to underside, opened "
                    "flower to opened flower and new meristem to new meristem. Compare roots of the "
                    "same age in the same substrate."
                ),
                term_gallery(REFERENCE_PLATES, "OpenAI image generation"),
                table(
                    ["Two problems with the same signs", "Sign that shows the difference", "Next step"],
                    [
                        ["Adult fungus gnat compared with winged root aphid", "A gnat has the legs and the antennae of a fly, and wing veins. An aphid has a body in the shape of a pear, and cornicles.", "Keep the specimen from the sticky trap near the media. Use microscopy."],
                        ["Broad mites or russet mites compared with tacoing from heat or light", "Mites and eggs on the outer edge of the symptoms, where you collect a sample. Abiotic stress agrees with the pattern of exposure and has no organisms.", "Examine many tips with a microscope before you change the feed or the climate."],
                        ["Powdery mildew compared with dried residue on the leaf", "Powdery mildew makes colonies above the surface that increase in size, and fungal structures. Residue agrees with the pattern of drops and circular marks, and with the spray records.", "Light from one side, microscopy, or a laboratory test. Use a laboratory test if you make the decision about the flower from the identification."],
                        ["Pythium compared with abiotic root stress", "Pythium: roots with water in the tissue, sloughing, and a pattern of disease in connected plants. Abiotic stress: dry tan roots with stress and no evidence of a pathogen.", "Collect samples of roots and water before sanitation. Send the samples to a diagnostic laboratory."],
                        ["HLVd compared with all other causes of stunting", "No visual sign gives a sure diagnosis.", "RT-qPCR or RT-PCR, with a sample that you can trace and with controls"],
                    ],
                    cls="compact",
                    caption="The photos that you use to compare are aids for training. An AI tool made them. They are not reference specimens.",
                ),
            ],
        }
    )

    sections.append(
        {
            "id": "build-programme",
            "kicker": "13 · Operation",
            "title": "The IPM program for each week",
            "blocks": [
                steps(
                    [
                        ("Calculate the consequence", "Room class, clean-stock status, target organism, crop stage and the consequence for product quality."),
                        ("Measure the problem", "Incidence, severity 0-4 and life stages. The pattern in the room and the trend of traps, roots and laboratory results. The density of beneficial organisms."),
                        ("Zero-tolerance findings", "A zero-tolerance finding does not use a threshold with a number. Start containment immediately."),
                        ("Find the source", "Received stock, movement of personnel and tools, air, water, media, packaging, weeds, algae, or pests from the previous crop."),
                        ("Select layers", "First do a correction with cultural controls and environmental controls. Then select biological controls and permitted products that are compatible."),
                        ("Schedule", "Select the target life stage and the date of application or release. Select the room controls, the change of mode, the recheck date, and the instruction to stop or to escalate."),
                        ("Examine the result", "Measure living organisms, new lesions, new growth, establishment and damage to the plants. Examine the effect on residue and if the problem occurs again."),
                        ("Stop or CAPA", "Stop the response only when the result agrees with the condition for a good result. If it does not, examine the cause again and escalate."),
                    ]
                ),
                table(
                    ["Information for the meeting each week", "Decision output"],
                    [
                        ["Trap and scouting trends", "A task for each room or zone, an owner and a recheck"],
                        ["HLVd and pathogen results", "A decision to release, hold, do the test again, destroy and trace"],
                        ["Receipt, release and establishment of beneficial organisms", "A decision to continue, to add more organisms, to replace them, or to do an investigation of a problem with compatibility"],
                        ["Excursions of the environment and of the root zone", "Correction with engineering controls or cultural controls, and a date for the end of the correction"],
                        ["Applications of products and the status of treated areas", "Release of the area from the REI, a check of the efficacy and a check of the residue"],
                        ["Open CAPA and connected batches", "Status of containment, gap in the evidence, quality decision for the batch, and a check of the effect of the CAPA"],
                    ],
                    cls="compact",
                    caption="The meeting each week gives tasks for each room. It does not give a long report that no person uses.",
                ),
                h(3, "Worksheet for the decision about the control method"),
                table(
                    ["Decision item", "Controlled entry"],
                    [
                        ["Confirmed target, life stage and plant part", "FACILITY INPUT"],
                        ["Current problem: incidence, severity, trend and distribution", "FACILITY INPUT"],
                        ["Possible source and pathway, and the evidence", "FACILITY INPUT"],
                        ["Corrections with cultural controls and environmental controls", "FACILITY INPUT"],
                        ["Biological control, evidence of establishment and compatibility", "FACILITY INPUT"],
                        ["Alternative product, legal gate, mode group and residue route", "FACILITY INPUT"],
                        ["Limits from the crop and the workers, REI and release of the treated area", "FACILITY INPUT"],
                        ["Owner, date of the task, recheck date, the condition for a good result, and the instruction to stop or to escalate", "FACILITY INPUT"],
                    ],
                    cls="compact",
                    caption="Complete the worksheet with the current approved-input register and the current register of beneficial organisms. Do not write product names and rates in a paper that has no document control.",
                ),
                h(3, "Table for control steps and releases of beneficial organisms, with dates"),
                table(
                    ["Date and time", "Room or zone", "Target stage", "Task or release", "Mode or organism", "Compatibility and REI", "Recheck"],
                    [["FACILITY INPUT"] * 7 for _ in range(4)],
                    cls="compact",
                    caption="Use sufficient rows for the full period of development of the target. The period changes if the conditions change. Change the rows after each recheck.",
                ),
                h(3, "Table of the target and the approved tool"),
                table(
                    ["Target", "Approved tool at this time", "Target stage and site", "Grade and source of the evidence", "Date of the check of the regulations", "Compatibility", "Measurement of a good result"],
                    [["FACILITY INPUT"] * 7 for _ in range(3)],
                    cls="compact",
                    caption="This table is an interface to the controlled registers. It does not replace them.",
                ),
                figure(
                    L.flow(
                        "From finding to end",
                        [
                            ("Confirm", "organism, life stage, location"),
                            ("Contain", "movement, plants, water, treated area"),
                            ("Control", "permitted control layers"),
                            ("Recheck", "specified data and date"),
                            ("Stop or CAPA", "good result or cause examined again"),
                        ],
                    ),
                    6,
                    "This figure shows the minimum record for each event with a finding that is more than the threshold.",
                ),
            ],
        }
    )

    sections.append(
        {
            "id": "crop-cycle",
            "kicker": "14 · Crop cycle",
            "title": "Crop-cycle IPM operations",
            "blocks": [
                table(
                    ["Stage", "Standard work for each day", "Work for each week, or scheduled work", "Mandatory decision"],
                    [
                        ["Receipt and quarantine", "Accession, check of the source and of the regulations, visual inspection and inspection of roots, dedicated tools and waste", "Traps, procedure for HLVd and pathogens, and a new check of the status", "Release only if the accession agrees with the release criteria for the regulations and for biology."],
                        ["Foundation mothers and production mothers", "Walk to examine the plants, control of tools, irrigation and environment", "Times of the molecular tests, full scouting, audit of hygiene in pruning", "A positive result for HLVd, or a pest that is systemic or has a high consequence: stop, hold, trace."],
                        ["Cuttings and rooting", "Clean cutting procedure, humidity and airflow, dead cuttings, and inspection of roots", "Development of roots, traps, a check for fungus and for root disease", "A pattern of problems starts an investigation of the source and of the water, and a diagnosis."],
                        ["Vegetative", "Inspection of the environment and the root zone. Walk to look for pests that you can see.", "Full scouting, sticky traps, release and establishment of biological controls", "One hotspot with a high risk, or a trend that increases, starts a control step for the target."],
                        ["Flower", "Climate, dew point, air movement and inspection of canopy with high density", "Full scouting. In the last stage of flowering, cut the buds that have the highest risk. Examine the buds. Do a check of residue and application.", "Powdery mildew on a flower, or Botrytis in a bud: start the control steps immediately."],
                        ["Harvest, drying and batch hold", "Hygiene when you move and touch the plant material, separation of waste, condition of the dry room and checks for mold", "Sampling for residue, microbes and unwanted material, and a check of the deviations", "Release the batch or continue the batch hold. Do a remediation if the regulations let you and the method has validation, or reject the batch."],
                    ],
                    cls="compact",
                    caption="The table is a full control model for the crop cycle. Use the approved production procedure for the times. The times change with the cultivar and the facility.",
                ),
                callout(
                    "key",
                    "IPM continues after harvest",
                    p(
                        "Tools with contamination and dirty processing equipment can cause "
                        "contamination of a clean crop. Slow drying, drying at different rates and "
                        "flowers with high density that you do not examine can also cause problems "
                        "for a clean crop. The product stays in batch hold until you have the "
                        "necessary quality evidence and you complete the check of the deviations."
                    ),
                ),
            ],
        }
    )

    sections.append(
        {
            "id": "capa-release",
            "kicker": "15 · Quality system",
            "title": "Containment, investigation and CAPA",
            "blocks": [
                p(
                    "Classify each event as local, room-wide or systemic. First do the containment. "
                    "Then find the root cause and the effect on the batch. Keep the evidence. Do "
                    "not complete the CAPA until the check of the effect shows that the change had "
                    "the correct effect."
                ),
                table(
                    ["Event", "First containment steps", "Investigation of the batch and the crop", "Items for the CAPA"],
                    [
                        ["Mother with a positive result for HLVd", "Stop the movement of clones. Isolate the mother. Put the mother in a bag. Use the SOP. Hold the connected clones.", "All clone lots since the last negative result that you know is correct, and the connected tools and water", "Source, frequency of tests, integrity of samples, sanitation of tools, separation of hydro systems, and traceability"],
                        ["Powdery mildew on flower", "Isolate the zone or the room. Put the tissue with disease in bags. Increase the scouting.", "Size of the area with disease, crop stage, permitted alternatives, residue and the decision for the market", "Microclimate at night, density, airflow, sensitivity of the scouting and compatibility with the program"],
                        ["Botrytis in a flower", "Remove the flower carefully. Prevent the movement of spores. Examine the plants near it.", "Batch hold and size of the area, pattern for each cultivar and zone, records of the environment", "Humidity removal, condensation, structure of the flower, damage when personnel touch the plants, and debris"],
                        ["Root disease in plants that use the same water", "Isolate the circuit. Stop the movement of water and plants. Collect samples before sanitation.", "All connected cohorts and the source stock", "Design of the reservoir and of the return water, biofilm, temperature and DO, cleaning validation, and separation of water"],
                        ["A worker goes into the area during the REI", "Remove the worker. Do the steps for the exposure. Prevent access to the area. Put warning signs in position.", "Examine the contact with the crop, the contamination and the treatment status", "Lockout, position of the warning signs, training, supervision and access control"],
                    ],
                    cls="compact",
                    caption="The CAPA connects the cause in biology, the cause in the workers or the system, and the consequence for the quality of the product.",
                ),
                ol(
                    [
                        "<strong>Release:</strong> the necessary laboratory results, the treatment records, the traceability and the check of the deviations are satisfactory.",
                        "<strong>Continue the batch hold:</strong> a result, a second sample or a connected lot status is not available. Also continue the batch hold while an investigation is in progress.",
                        "<strong>Reject, or do a validated remediation:</strong> the lot does not agree with a limit. Do the same if the treatment records do not agree with the regulations. Do the same if the lot has a connection to systemic contamination. Remediation does not replace prevention.",
                    ]
                ),
            ],
        }
    )

    sections.append(
        {
            "id": "controlled-toolkit",
            "kicker": "16 · Tools for work",
            "title": "Controlled IPM tools",
            "blocks": [
                h(3, "Facility approval sheet"),
                "<style>.facility-input{display:grid;gap:6px}.facility-input input,.facility-input textarea{width:100%;padding:10px;border:1px solid var(--line);border-radius:6px;background:var(--paper);color:var(--ink);font:inherit}.facility-form{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}.facility-input.wide{grid-column:1/-1}@media(max-width:720px){.facility-form{grid-template-columns:1fr}}</style>",
                "<form class='facility-form'>"
                + _input("site_address", "Facility address and Auckland zone")
                + _input("licence_scope", "License, and types of product that the facility will make")
                + _input("room_map", "Version of the controlled room map")
                + _input("quality_owner", "Person who gives approval for quality and IPM")
                + _input("diagnostic_lab", "Approved diagnostic laboratory and scope")
                + _input("release_lab", "Laboratory for release, and the pesticide method and LOQ")
                + _input("watercare_status", "Trade waste classification and trade waste agreement")
                + _input("review_date", "Date of the next check of the document")
                + _input("sampling_density", "Controlled density of scouting, method to select typical sites, and the evidence for the selection", True)
                + _input("zero_tolerance", "Zero-tolerance organisms and room classes for the site", True)
                + _input("thresholds", "Controlled thresholds with numbers and thresholds for trends, and the source of the evidence", True)
                + "</form>",
                h(3, "Scouting record for each week"),
                table(
                    ["Necessary field", "Entry"],
                    [[field, "FACILITY INPUT"] for field in SCOUT_FIELDS]
                    + [["Sites to examine, completed sites, and exceptions for sites that you did not examine or sites without access", "FACILITY INPUT"]],
                    cls="compact",
                    caption="Use one row for each site on the map and for each exception. For an unknown organism, write the reference of the specimen or the photo. Do not write a name that you are not sure of.",
                ),
                h(3, "Log of quarantine and of movement from clean to dirty"),
                table(
                    ["Date and time", "Person or material", "From", "To", "Release and status evidence", "Change of PPE and tools", "Exception approval"],
                    [["FACILITY INPUT"] * 7 for _ in range(4)],
                    cls="compact",
                    caption="Record each movement of an accession and each approved movement back to a clean area on the hygiene gradient.",
                ),
                h(3, "Record of the release and establishment of beneficial organisms"),
                table(
                    ["Field", "Entry"],
                    [
                        ["Species, strain, supplier and lot", "FACILITY INPUT"],
                        ["Evidence of the NZ legal status, and the approval date", "FACILITY INPUT"],
                        ["Time, temperature and condition when you receive the organisms", "FACILITY INPUT"],
                        ["Viability and count check, and the decision to reject", "FACILITY INPUT"],
                        ["Target pest and stage, room map and release rate", "FACILITY INPUT"],
                        ["Climate, and a check of residues that are not compatible", "FACILITY INPUT"],
                        ["Establishment and recheck date, and evidence", "FACILITY INPUT"],
                        ["Corrective action, or the decision to stop the response", "FACILITY INPUT"],
                    ],
                    cls="compact",
                ),
                h(3, "Checklist for the quality of spray and of application"),
                table(
                    ["Check", "Controlled entry"],
                    [
                        ["Event ID, approved product and lot, target, room and zone, crop stage", "FACILITY INPUT"],
                        ["Evidence of the check of the current label, SDS and the regulations for medicinal cannabis, ACVM and HSNO", "FACILITY INPUT"],
                        ["Applicator, calibration, output, nozzle and pressure, and target coverage", "FACILITY INPUT"],
                        ["Water quality, sequence for the mixture, agitation and volume of the mixture", "FACILITY INPUT"],
                        ["Controls for HVAC and lights, containment, and risk of weather and external discharge", "FACILITY INPUT"],
                        ["PPE, warning signs, access control, REI start and end, and release of the treated area", "FACILITY INPUT"],
                        ["Mixture that you did not use, rinse water, disposal of spills and waste, and equipment clean-down", "FACILITY INPUT"],
                        ["Phytotoxicity, efficacy and residue: recheck dates and results", "FACILITY INPUT"],
                    ],
                    cls="compact",
                ),
                h(3, "Record of the outbreak, the effect on the batch, and the CAPA"),
                table(
                    ["Field", "Entry"],
                    [
                        ["Event ID, the first finding, and the person who found it", "FACILITY INPUT"],
                        ["Confirmed organism, evidence and uncertainty", "FACILITY INPUT"],
                        ["Room, zone, plants, mothers, clone lots and batches", "FACILITY INPUT"],
                        ["Connected personnel, tools, air, water, media and lots of products", "FACILITY INPUT"],
                        ["Containment done immediately, and controls for the treated area", "FACILITY INPUT"],
                        ["Investigation of the effect on product quality and on residue", "FACILITY INPUT"],
                        ["Decision to hold, destroy, do a remediation, or release", "FACILITY INPUT"],
                        ["Root cause and other conditions that help to cause the event", "FACILITY INPUT"],
                        ["Corrective action and preventive action, with owners and dates", "FACILITY INPUT"],
                        ["Evidence that the CAPA had the correct effect, and the decision of QA to stop the response", "FACILITY INPUT"],
                    ],
                    cls="compact",
                ),
                h(3, "Worksheet for the dashboard of the population trend"),
                table(
                    ["Week or date", "Room or zone", "Target", "Traps or points for samples", "Count of living organisms, or incidence", "Severity 0-4", "Density of beneficial organisms", "Action threshold", "Decision"],
                    [["FACILITY INPUT"] * 9 for _ in range(5)],
                    cls="compact",
                    caption="Make a graph of the trend of these same controlled fields in the validated record system of the site. Record the denominator and the sites that you did not examine. Thus you can read the graph correctly.",
                ),
                h(3, "Control of spills and waste"),
                ul(
                    [
                        "The current drain map shows which drains go to the sewer or to trade waste, and which drains go to stormwater.",
                        "Secondary containment and spill kits are correct for the substances that you keep and for the spill volume that can occur.",
                        "Do not let pesticide, sanitizer, nutrient concentrate, rinse water with contamination, or spill liquid go into stormwater.",
                        "Show the Watercare and Auckland triggers for a pollution event in a position where personnel can see them. Give personnel training on the triggers.",
                        "The waste contractors and the disposal records are current. The findings of the drill each year go into the CAPA.",
                    ]
                ),
            ],
        }
    )

    sections.append(
        {
            "id": "training",
            "kicker": "17 · Competency",
            "title": "Training for competency",
            "blocks": [
                table(
                    ["Module", "Personnel", "Result that personnel show"],
                    [
                        ["The legal gate for NZ medicinal cannabis", "QA, procurement, IPM leads and cultivation leads", "Reject a possible product, or give approval for it, with a correct record of the evidence"],
                        ["Hygiene zones and movement", "All personnel for cultivation, sanitation and maintenance, and contractors", "Do the room sequence, the changes of tools and PPE, and the procedure for exceptions"],
                        ["Scouting, and how to collect and keep specimens", "Scouts and room leads", "Use the same scouting route. Identify plant parts. Record incidence and severity. Keep unknown specimens."],
                        ["Mother stock and HLVd", "Personnel for the nursery, personnel for the mother plants and QA personnel", "Collect a sample that you can trace. Start a batch hold. Trace the clones. Do the steps for a positive result."],
                        ["Control with beneficial organisms", "IPM personnel and personnel for receipt", "Examine the viability on receipt, the release map, the compatibility and the establishment"],
                        ["Application, REI and PPE", "Applicators, supervisors, QA and EHS", "Calibrate. Mix. Apply. Contain waste. Put warning signs in position. Release the treated area."],
                        ["CAPA and the effect on the batch", "QA, cultivation managers and the IPM lead", "Do a mock event from containment to the check of the effect"],
                    ],
                    cls="compact",
                    caption="WorkSafe makes it necessary to have information, instruction, training and records for the site. Previous training of a person does not remove the duty of the site" + _c("worksafe-nz-hs-training") + ".",
                ),
                callout(
                    "note",
                    "Do drills for events with a very bad effect",
                    p(
                        "Do drills for these events as a minimum. A mother has a positive result "
                        "for HLVd. A cluster of Botrytis occurs in the last stage of flowering. "
                        "Root disease occurs on a circuit for more than one area.</p><p>After "
                        "application, you find a product that the regulations do not let you use. A "
                        "worker goes into an area during the REI. A spill can go to a drain. You "
                        "know that a procedure is satisfactory only after personnel use it in a "
                        "drill."
                    ),
                ),
            ],
        }
    )

    sections.append(
        {
            "id": "revision-register",
            "kicker": "18 · Control of the document",
            "title": "Evidence and version register",
            "blocks": [
                table(
                    ["Class of claim", "Minimum evidence", "Trigger for a new check"],
                    [
                        ["NZ regulations", "A current source from an authority: the Ministry, MPI, EPA, WorkSafe, Watercare or Auckland", "A change of a regulation or guidance, a new product or organism, or the check each year"],
                        ["Biology of pests and diseases", "A primary paper or a review article of high quality, with the limits for the species", "A new result of diagnosis, or an organism with behavior that is different from the behavior in this blueprint"],
                        ["Status of the product or organism", "Current register and approval, label, SDS, supplier and approval of the site", "Each time that you get a product or use it, and each change of the document"],
                        ["Facility threshold", "Records of the site, the evidence for the risk, and quality approval", "A trend that you did not find, crop loss, a false alarm, or a change of production procedure or market"],
                        ["Setpoint for operation", "A facility SOP or validation that you can identify, and measured data", "A change of equipment, cultivar, room, substrate or production procedure"],
                        ["A photo that an AI tool made", "The last prompt, the AI tool, a check of the diagnosis that a person does, and a record that an AI tool made the photo", "An error in the morphology, a problem in training, or a better reference that you know is correct"],
                    ],
                    cls="compact",
                    caption="This blueprint is controlled guidance and can change. Examine the parts that change frequently before you examine the parts that do not change.",
                ),
                callout(
                    "key",
                    "A strong IPM program",
                    p(
                        "In a strong IPM program, the facility has no products that the regulations "
                        "do not let you use, and no genetics with an infection. Water and air do "
                        "not become systems that move pests and pathogens. The movement of "
                        "personnel is easy to see. You can see the release criteria when you select "
                        "a control. All other parts are not necessary."
                    ),
                ),
            ],
        }
    )

    return sections
