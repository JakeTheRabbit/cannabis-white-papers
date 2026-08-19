# -*- coding: utf-8 -*-
"""Citations for the deep-water-culture paper. Merged into data/refs.py (existing ids win)."""

REFS_ADD = {
    # ---------- dissolved oxygen: thresholds, enrichment, response ----------
    "dwc-roosta-2024-o2-nform": {
        "cite": "Roosta HR, Bikdeloo M, Ghorbanpour M (2024). The responses of pepper plants to nitrogen form and dissolved oxygen concentration of nutrient solution in hydroponics. <em>BMC Plant Biology</em>. (Growth and photosynthesis impaired below 3.8 mg/L with ammonium and 5.3 mg/L with nitrate.)",
        "url": "https://consensus.app/papers/details/9d38d6a7abd25e499356415c9299791a/", "peer": True},
    "dwc-nitu-2024-nft-oxygen": {
        "cite": "Ni&#539;u O, et al. (2024). Optimizing lettuce growth in nutrient film technique hydroponics: evaluating the impact of elevated oxygen concentrations in the root zone under LED illumination. <em>Agronomy</em> 14. (8.1-9.0 vs 6.8-7.8 mg/L; fresh mass up to +110%.)",
        "url": "https://consensus.app/papers/details/5a91b04f87f4574ea8b41ca74a60fca7/", "peer": True},
    "dwc-qin-2025-do-enrichment": {
        "cite": "Qin K, et al. (2025). Boosting hydroponic production of kale and arugula by managing dissolved oxygen. <em>HortScience</em>. (Deep-water culture at 10/15/20 mg/L DO; arugula +63-191% above 15 mg/L, kale unresponsive, energy cost +140%.)",
        "url": "https://consensus.app/papers/details/8061b2ad1e0a5c94bd469cdf12f26c07/", "peer": True},
    "dwc-nsele-2026-dwc-tomato": {
        "cite": "Nsele SN, et al. (2026). Recent insights into tomato (<em>Solanum lycopersicum</em> L.) cultivations in deep water culture systems. <em>Discover Sustainability</em>.",
        "url": "https://consensus.app/papers/details/80def129c06552c6afe262ab87a8582c/", "peer": True},

    # ---------- the aeration paradox ----------
    "dwc-langenfeld-2025-agitation-iron": {
        "cite": "Langenfeld NJ, Bugbee B (2025). Aeration and agitation in hydroponic culture have detrimental effects on iron uptake. <em>Frontiers in Plant Science</em>. (Bubbling-induced agitation reduced iron uptake and caused chlorosis in sunflower and corn; tomato was tolerant.)",
        "url": "https://consensus.app/papers/details/6ffb3bfbc8fe5b65a528ecd0e50d5f7c/", "peer": True},
    "dwc-langenfeld-2024-zero-discharge": {
        "cite": "Langenfeld NJ, Bugbee B (2024). Sustainable hydroponics using zero-discharge nutrient management and automated pH control. <em>HortScience</em>. (Gentle aeration at ~100 mL&#183;min<sup>-1</sup>&#183;L<sup>-1</sup> holds DO near saturation; &ge;20 cm solution depth stabilises the root zone.)",
        "url": "https://consensus.app/papers/details/55797967d9185928bf9582a1148bded7/", "peer": True},
    "dwc-bodenmiller-2017-aeration": {
        "cite": "Bodenmiller D (2017). Effects of aeration on lettuce (<em>Lactuca sativa</em>) growth in deep water culture aquaponics. Tampere University of Applied Sciences. (Heavy aeration stripped CO<sub>2</sub>, raised pH and depressed yield even though DO never fell below 5 mg/L.)",
        "url": "https://consensus.app/papers/details/549a8575046a5948a75e0718d3fb7a55/", "peer": False},

    # ---------- nanobubbles ----------
    "dwc-ebina-2013-nanobubble": {
        "cite": "Ebina K, Shi K, Hirao M, et al. (2013). Oxygen and air nanobubble water solution promote the growth of plants, fishes, and mice. <em>PLoS ONE</em> 8(6):e65339. (Sub-200 nm bubbles remained measurable for ~70 days.)",
        "url": "https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0065339", "peer": True},
    "dwc-wang-2024-mnb-microbiome": {
        "cite": "Wang J, et al. (2024). Micro/nanobubble-aerated drip irrigation affects saline soil microenvironments and tomato growth by altering bacterial communities. <em>Soil and Tillage Research</em>. (DO 5 vs 15 vs 30 mg/L; root volume and yield rose with DO.)",
        "url": "https://consensus.app/papers/details/9fa0c06e4a455472a52a6d287b6dffa7/", "peer": True},
    "dwc-mamun-2025-onb-health": {
        "cite": "Al Mamun M, et al. (2025). Oxygenated nanobubbles as a sustainable strategy to strengthen plant health in controlled environment agriculture. <em>Sustainability</em> 17.",
        "url": "https://consensus.app/papers/details/41096736729a529ebc7b02735f1871f1/", "peer": True},

    # ---------- oxygen physical chemistry ----------
    "dwc-benson-krause-1984": {
        "cite": "Benson BB, Krause D (1984). The concentration and isotopic fractionation of oxygen dissolved in freshwater and seawater in equilibrium with the atmosphere. <em>Limnology and Oceanography</em> 29(3):620-632. (The standard air-saturation tables.)",
        "url": "https://aslopubs.onlinelibrary.wiley.com/doi/10.4319/lo.1984.29.3.0620", "peer": True},
    "dwc-bok-2023-o2-solubility": {
        "cite": "Bok F, Moog HC, Brendler V (2023). The solubility of oxygen in water and saline solutions. <em>Frontiers in Nuclear Engineering</em>. (Temperature-dependent Henry's law function for O<sub>2</sub>; salinity salting-out coefficients.)",
        "url": "https://consensus.app/papers/details/f3300e3a0ef65adf8897f8dc767a2d66/", "peer": True},

    # ---------- redox / ORP ----------
    "dwc-stefansson-2005-redox": {
        "cite": "Stef&#225;nsson A, Arn&#243;rsson S, Sveinbj&#246;rnsd&#243;ttir &#193;E (2005). Redox reactions and potentials in natural waters at disequilibrium. <em>Chemical Geology</em> 221:289-311. (Couples in one water differed by up to 1200 mV; a platinum electrode in a dilute solution reads a mixed potential of limited quantitative meaning.)",
        "url": "https://consensus.app/papers/details/ab285773d82f5ed29ba0965b6dd91115/", "peer": True},
    "dwc-suslow-2004-orp": {
        "cite": "Suslow TV (2004). Oxidation-reduction potential (ORP) for water disinfection monitoring, control, and documentation. <em>UC ANR Publication 8149</em>. (ORP as a control variable for hypochlorous-acid sanitation, not as an oxygen proxy.)",
        "url": "https://escholarship.org/uc/item/9jn7s7d4", "peer": True},
    "dwc-sholikah-2025-pt-electrode": {
        "cite": "Sholikah U, et al. (2025). Continuous water monitoring of platinum and carbon electrode potential for assessing redox potential and biological activity in the intertidal zone. <em>Marine Environmental Research</em>. (Biofilm growth on the electrode itself shifts the reading by hundreds of millivolts.)",
        "url": "https://consensus.app/papers/details/a80f5189c0c55a9fab725429ee370a07/", "peer": True},

    # ---------- iron and chelates ----------
    "dwc-ilyas-2025-fe-chelates": {
        "cite": "Ilyas MF, et al. (2025). Iron solubility and uptake in fava bean and maize as a function of iron chelates under alkaline hydroponic conditions. <em>Journal of Agricultural and Food Chemistry</em>. (Fe-EDTA becomes unstable above pH 6.5; speciation modelling shows Fe displacement to insoluble FePO<sub>4</sub> and Fe(OH)<sub>3</sub>.)",
        "url": "https://consensus.app/papers/details/35bb7b852ddf5b79a6e852ae511fece5/", "peer": True},
    "dwc-klem-2021-eddha": {
        "cite": "Klem-Marciniak E, Huculak-M&#261;czka M, Marecka K, et al. (2021). Chemical stability of the fertilizer chelates Fe-EDDHA and Fe-EDDHSA over time. <em>Molecules</em> 26(7):1933.",
        "url": "https://www.mdpi.com/1420-3049/26/7/1933", "peer": True},
    "dwc-mirbolook-2023-fe-source": {
        "cite": "Mirbolook A, et al. (2023). Synthesis and characterization of the Schiff base Fe(II) complex as a new iron source in nutrient solution. <em>Rhizosphere</em> 25.",
        "url": "https://consensus.app/papers/details/41bdc757d6e557ec892e4dbe88d3575a/", "peer": True},

    # ---------- hypoxia physiology ----------
    "dwc-drew-1997-hypoxia": {
        "cite": "Drew MC (1997). Oxygen deficiency and root metabolism: injury and acclimation under hypoxia and anoxia. <em>Annual Review of Plant Physiology and Plant Molecular Biology</em> 48:223-250.",
        "url": "https://www.annualreviews.org/doi/10.1146/annurev.arplant.48.1.223", "peer": True},
    "dwc-colmer-2010-ion-transport": {
        "cite": "Colmer TD, Greenway H (2011). Ion transport in seminal and adventitious roots of cereals during O<sub>2</sub> deficiency. <em>Journal of Experimental Botany</em> 62(1):39-57. (Stelar hypoxia inhibits xylem-parenchyma H<sup>+</sup>-ATPases, so nutrients are absorbed but not loaded to the shoot.)",
        "url": "https://academic.oup.com/jxb/article/62/1/39/562539", "peer": True},
    "dwc-tan-2018-aquaporins": {
        "cite": "Tan X, Xu H, Khan S, et al. (2018). Plant water transport and aquaporins in oxygen-deprived environments. <em>Journal of Plant Physiology</em> 227:20-30. (Hypoxia closes aquaporins and triggers stomatal closure before any root symptom is visible.)",
        "url": "https://consensus.app/papers/details/763e25b0e3225a5e9e7240a6f9b9e2e7/", "peer": True},

    # ---------- pathology ----------
    "dwc-sutton-2006-pythium": {
        "cite": "Sutton JC, Sopher CR, Owen-Going TN, et al. (2006). Etiology and epidemiology of Pythium root rot in hydroponic crops: current knowledge and perspectives. <em>Summa Phytopathologica</em> 32(4):307-321. (Disinfesting the returning solution has minor impact; suppressing the pathogen in the root zone is what works.)",
        "url": "https://www.scielo.br/j/sp/a/8dNZL9YYqLpMFrJVGWCcXVL/", "peer": True},
    "dwc-scott-2026-do-pythium": {
        "cite": "Scott S, Villouta C (2026). Dissolved oxygen limitation and Pythium root rot in strawberry NFT systems: mechanisms, research gaps, and prospects for substrate-free production. <em>Frontiers in Plant Science</em>. (Low DO and Pythium are one coupled failure, not two independent ones.)",
        "url": "https://consensus.app/papers/details/1cc3745eadb050ce976bbbe08493adc1/", "peer": True},
    "dwc-rashad-2024-biocontrol": {
        "cite": "Rashad YM, et al. (2024). Fostering resistance in common bean: synergistic defense activation by <em>Bacillus subtilis</em> HE18 and <em>Pseudomonas fluorescens</em> HE22 against Pythium root rot. <em>Rhizosphere</em> 29.",
        "url": "https://consensus.app/papers/details/c1a8604a29675f6b91724cfed911f3c2/", "peer": True},
    "dwc-alattas-2024-pseudomonas": {
        "cite": "Alattas H, Glick BR, Murphy DV, Scott C (2024). Harnessing <em>Pseudomonas</em> spp. for sustainable plant crop protection. <em>Frontiers in Microbiology</em> 15.",
        "url": "https://www.frontiersin.org/articles/10.3389/fmicb.2024.1485197/full", "peer": True},

    # ---------- microbiology of a recirculating reservoir ----------
    "dwc-kenderdine-2026-recirc": {
        "cite": "Kenderdine CM, et al. (2026). Continuous recirculation of hydroponic-nutrient solutions shifts bacterial communities and induces plant-defense gene expression in lettuce. <em>Applied and Environmental Microbiology</em>. (Deep-water culture, five reuse cycles, with and without <em>Pythium myriotylum</em>.)",
        "url": "https://consensus.app/papers/details/2e7f31fbef7a5df9a7443b521e38449c/", "peer": True},
    "dwc-lobanov-2022-plants-dictate": {
        "cite": "Lobanov V, Keesman KJ, Joyce A (2022). Plants dictate root microbial composition in hydroponics and aquaponics. <em>Frontiers in Microbiology</em> 13:848057.",
        "url": "https://www.frontiersin.org/articles/10.3389/fmicb.2022.848057/full", "peer": True},
    "dwc-canellas-2015-humic": {
        "cite": "Canellas LP, Olivares FL, Aguiar NO, et al. (2015). Humic and fulvic acids as biostimulants in horticulture. <em>Scientia Horticulturae</em> 196:15-27.",
        "url": "https://www.sciencedirect.com/science/article/pii/S0304423815301722", "peer": True},

    # ---------- oxidisers ----------
    "dwc-eicher-sodo-2020-h2o2": {
        "cite": "Eicher-Sodo M (2020). Hydrogen peroxide: a grower's best friend? MSc thesis, University of Guelph. (0-400 mg/L H<sub>2</sub>O<sub>2</sub> into hydroponic solution; every crop showed visible root injury, cucumber worst.)",
        "url": "https://atrium.lib.uoguelph.ca/items/9c14bcbe-5d5b-4b5d-a5e6-24b62a4cd9f5", "peer": False},
    "dwc-hendrickson-2022-h2o2": {
        "cite": "Hendrickson T, Dunn BL, Goad C, et al. (2022). Effects of hydrogen peroxide products on basil, lettuce, and algae in an ebb and flow hydroponic system. <em>Horticulturae</em> 8(2):143.",
        "url": "https://www.mdpi.com/2311-7524/8/2/143", "peer": True},

    # ---------- temperature ----------
    "dwc-alrawahy-2019-rzt": {
        "cite": "Al-Rawahy MS, Al-Rawahy SA, Al-Mulla YA, Nadaf SK (2019). Influence of nutrient solution temperature on its oxygen level and growth, yield and quality of hydroponic cucumber. <em>Journal of Agricultural Science</em> 11(3):75. (Cooling the solution raised both DO and measured root oxygen consumption.)",
        "url": "https://consensus.app/papers/details/05f91ecdbdfa572da41d834e90866256/", "peer": True},

    # ---------- nitrogen form and pH ----------
    "dwc-zhu-2021-nh4-no3": {
        "cite": "Zhu Y, Qi B, Hao Y, et al. (2021). Appropriate NH<sub>4</sub><sup>+</sup>/NO<sub>3</sub><sup>-</sup> ratio triggers plant growth and nutrient uptake of flowering Chinese cabbage by optimizing the pH value of nutrient solution. <em>Frontiers in Plant Science</em> 12:656144. (Pure nitrate drove solution pH to ~8.0; excess ammonium drove it to 3.6.)",
        "url": "https://www.frontiersin.org/articles/10.3389/fpls.2021.656144/full", "peer": True},

    # ---------- cannabis-specific ----------
    "dwc-hershkowitz-2025-p-ec": {
        "cite": "Hershkowitz JA, Westmoreland FM, Bugbee B (2025). Elevated root-zone P and nutrient concentration do not increase yield or cannabinoids in medical cannabis. <em>Frontiers in Plant Science</em>. (Closed-system hydroponics; doubling EC from 2 to 4 mS/cm added nothing.)",
        "url": "https://consensus.app/papers/details/d07bf531094356f6bdff33b41d9391c6/", "peer": True},
    "dwc-caplan-2019-drought": {
        "cite": "Caplan D, Dixon M, Zheng Y (2019). Increasing inflorescence dry weight and cannabinoid content in medical cannabis using controlled drought stress. <em>HortScience</em> 54(5):964-969.",
        "url": "https://journals.ashs.org/hortsci/view/journals/hortsci/54/5/article-p964.xml", "peer": True},
    "dwc-hassan-2024-silicon": {
        "cite": "Hassan KM, et al. (2024). Silicon: a powerful aid for medicinal and aromatic plants against abiotic and biotic stresses for sustainable agriculture. <em>Horticulturae</em> 10.",
        "url": "https://consensus.app/papers/details/3064de03084c573ea4719679f0a3fbc4/", "peer": True},

    # ---------- manufacturer procedure ----------
    "dwc-athena-rdwc-2024": {
        "cite": "Athena Ag, Inc. (2024). <em>RDWC: recirculating deep water culture procedure</em> (metric edition, Tony Buckets partnership). Manufacturer procedure: operating volumes, air-manifold pressures, stage EC/pH/temperature envelope, addback and change-out protocol, ORP zones.",
        "url": "https://support.athenaag.com/hc/en-us/articles/27951744956955-RDWC-Procedure-for-Athena-Blended-Line", "peer": False},
    "dwc-athena-proline": {
        "cite": "Athena Ag, Inc. Pro Line and Blended Line product composition and feed schedules. (Pro Core supplies iron as Fe-EDTA; Pro Bloom supplies iron as Fe-DTPA; Balance is a potassium silicate; Cleanse is a hypochlorous-acid base.)",
        "url": "https://support.athenaag.com/hc/en-us/articles/17190427112859-Pro-Line-Feed-Schedules", "peer": False},
}
