# -*- coding: utf-8 -*-
"""Citation registry. One source of truth for peer-reviewed references, reused across
papers. Each paper declares the ref ids it cites; the build numbers them per paper."""

REFS = {
    "holmes2021": {
        "cite": "Holmes JE et al. (2021). Variables affecting shoot growth and plantlet recovery in tissue cultures of drug-type <em>Cannabis sativa</em> L. <em>Frontiers in Plant Science</em>, 12:732344.",
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8491305/", "peer": True},
    "mdpi2024_media": {
        "cite": "Adhikary D et al. (2024). Importance of media composition and explant type in <em>Cannabis sativa</em> tissue culture. <em>Plants (MDPI)</em>.",
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11434680/", "peer": True},
    "page2019": {
        "cite": "Page SRG et al. (2019). Back to the roots: protocol for the photoautotrophic micropropagation of medicinal <em>Cannabis</em>. <em>Plant Methods</em>, 15:54.",
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC6660493/", "peer": True},
    "pmc9146626": {
        "cite": "Mestinšek Mubi Š et al. (2022). An alternative in vitro propagation protocol of <em>Cannabis sativa</em> L. presenting efficient rooting, for commercial production. <em>Plants</em>.",
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9146626/", "peer": True},
    "kurtz2022": {
        "cite": "Kurtz LE et al. (2022). Ex vitro rooting of <em>Cannabis sativa</em> microcuttings and their performance compared to retip and stem cuttings. <em>HortScience</em>, 57(12):1576.",
        "url": "https://journals.ashs.org/hortsci/view/journals/hortsci/57/12/article-p1576.xml", "peer": True},
    "torkamaneh2024": {
        "cite": "Torkamaneh D et al. (2024). Somatic mutation accumulation in micropropagated cannabis is proportional to the number of subcultures. <em>Plants</em>, 13(14):1910.",
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11279941/", "peer": True},
    "hlvd_threat2023": {
        "cite": "Atallah OO et al. (2023). Hop latent viroid: a hidden threat to the cannabis industry. <em>Viruses / PMC</em>.",
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10053334/", "peer": True},
    "hlvd_mgmt2025": {
        "cite": "Transmission, spread, longevity and management of hop latent viroid in cannabis in North America (2025). <em>PMC</em>.",
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11902214/", "peer": True},
    "hlvd_thermo2024": {
        "cite": "Differential gene expression after HpLVd eradication therapy in micropropagation tissue culture (2024–25). <em>bioRxiv / Plant Cell Tiss. Organ Cult.</em>",
        "url": "https://www.biorxiv.org/content/10.1101/2024.04.06.588422v1", "peer": True},
    "tis2022": {
        "cite": "A temporary immersion system to improve <em>Cannabis sativa</em> micropropagation (2022). <em>Frontiers in Plant Science</em>.",
        "url": "https://www.frontiersin.org/articles/10.3389/fpls.2022.895971/full", "peer": True},
    "karger2019_cryo": {
        "cite": "Cryopreservation of shoot tips of elite cultivars of <em>Cannabis sativa</em> L. by droplet vitrification (2019). <em>Medical Cannabis and Cannabinoids (Karger)</em>.",
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8489323/", "peer": True},
    "athena": {
        "cite": "Athena Ag, Culture Kit, ROOTS/SHOOTS media, and Plant/Media/Lab Prep procedure (manufacturer documentation).",
        "url": "https://www.athenaag.com/culture-kit", "peer": False},

    # ---- coco & crop steering ----
    "abad2005-coir": {"cite": "Abad M, Noguera P, Puchades R, Maquieira A, Noguera V (2005). Physical properties of various coconut coir dusts compared to peat. <em>HortScience</em> 40(7):2138-2144.", "url": "https://doi.org/10.21273/HORTSCI.40.7.2138", "peer": True},
    "noguera2003-cec": {"cite": "Noguera P, Abad M, Puchades R, Maquieira A, Noguera V (2003). Influence of particle size on physical and chemical properties of coconut coir dust as container medium. <em>Commun. Soil Sci. Plant Anal.</em> 34(3-4):593-605.", "url": "https://doi.org/10.1081/CSS-120017842", "peer": True},
    "hilhorst2000-ec": {"cite": "Hilhorst MA (2000). A pore water conductivity sensor. <em>Soil Sci. Soc. Am. J.</em> 64(6):1922-1925.", "url": "https://doi.org/10.2136/sssaj2000.6461922x", "peer": True},
    "caplan2019-drought": {"cite": "Caplan D, Dixon M, Zheng Y (2019). Increasing inflorescence dry weight and cannabinoid content in medical cannabis using controlled drought stress. <em>HortScience</em> 54(5):964-969.", "url": "https://doi.org/10.21273/HORTSCI13510-18", "peer": True},
    "stack2024-drought": {"cite": "Stack GM, Cala AR, Quade MA, et al. (2024). Severe drought significantly reduces floral hemp (Cannabis sativa L.) yield and cannabinoid content but moderate drought does not. <em>Ind. Crops Prod.</em> 209:117974.", "url": "https://doi.org/10.1016/j.indcrop.2024.117974", "peer": True},
    "welling2025-aba": {"cite": "Welling MT, et al. (2025). Regulation of secondary metabolism in Cannabis sativa L. by abscisic acid and water deficit during early flower development. <em>Plant Stress</em> 17:100968.", "url": "https://doi.org/10.1016/j.stress.2025.100968", "peer": True},
    "grossiord2020-vpd": {"cite": "Grossiord C, Buckley TN, Cernusak LA, et al. (2020). Plant responses to rising vapor pressure deficit. <em>New Phytologist</em> 226(6):1550-1566.", "url": "https://doi.org/10.1111/nph.16485", "peer": True},
    "moe1995-dif": {"cite": "Myster J, Moe R (1995). Effect of diurnal temperature alternations on plant morphology in some greenhouse crops, a mini review. <em>Scientia Horticulturae</em> 62(4):205-215.", "url": "https://doi.org/10.1016/0304-4238(95)00783-P", "peer": True},
    "moher2023-photoperiod": {"cite": "Moher M, Llewellyn D, Jones M, Zheng Y (2023). Is twelve hours really the optimum photoperiod for promoting flowering in indoor-grown cultivars of Cannabis sativa? <em>Plants</em> 12(14):2605.", "url": "https://doi.org/10.3390/plants12142605", "peer": True},

    # ---- grow-room systems ----
    "chandra2008-photo": {"cite": "Chandra S, Lata H, Khan IA, ElSohly MA (2008). Photosynthetic response of Cannabis sativa L. to variations in photosynthetic photon flux densities, temperature and CO2 conditions. <em>Physiol. Mol. Biol. Plants</em> 14(4):299-306.", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3550641/", "peer": True},
    "rm2021-light": {"cite": "Rodriguez-Morrison V, Llewellyn D, Zheng Y (2021). Cannabis yield, potency, and leaf photosynthesis respond differently to increasing light levels in an indoor environment. <em>Front. Plant Sci.</em> 12:646020.", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8144505/", "peer": True},
    "hawley2018-scl": {"cite": "Hawley D, Graham T, Stasiak M, Dixon M (2018). Improving cannabis bud quality and yield with subcanopy lighting. <em>HortScience</em> 53(11):1593-1599.", "url": "https://doi.org/10.21273/HORTSCI13173-18", "peer": True},
    "icl2025-plants": {"cite": "(2025). Subcanopy and inter-canopy supplemental light enhances and standardizes yields in medicinal cannabis (Cannabis sativa L.). <em>Plants</em> 14(10):1469.", "url": "https://doi.org/10.3390/plants14101469", "peer": True},
    "farred2025-scirep": {"cite": "(2025). The effects of far-red light on medicinal cannabis. <em>Scientific Reports</em> 15.", "url": "https://doi.org/10.1038/s41598-025-99771-6", "peer": True},
    "fluence-icl-2024": {"cite": "Cannabis Business Times / Fluence (2024). Intercanopy lighting trials show compelling increases in cannabis quality and consistency (Texas Original; Poel, Hawley) — grade uplift at equal flux, photobleaching at 80-100% red.", "url": "https://www.cannabisbusinesstimes.com/", "peer": False},
    "fluence-broad-2026": {"cite": "Fluence (2026). Maximizing cannabis yields with intercanopy and subcanopy lighting — broad-spectrum recommendation, bleaching risk, ROI via uniformity.", "url": "https://fluence.science/", "peer": False},
    "aroya-undercanopy": {"cite": "AROYA. Understanding under-canopy lighting — realistic 25-35% averages, conditional on cultivar and plant-count accommodations.", "url": "https://aroya.io/", "peer": False},
    "saetang2024-high-light-metabolites": {"cite": "Sae-Tang W, Heuvelink E, Kohlen W, Argyri E, Nicole CCS, Kaiser E, et al. (2024). High light intensity improves yield of specialized metabolites in medicinal cannabis (Cannabis sativa L.), resulting from both higher inflorescence mass and concentrations of metabolites. <em>J. Appl. Res. Med. Aromat. Plants</em> 43:100583.", "url": "https://doi.org/10.1016/j.jarmap.2024.100583", "peer": True},
    "rfr2024-yield-vs-metabolites": {"cite": "(2024). Decreasing R:FR ratio in a grow light spectrum increases inflorescence yield but decreases plant specialized metabolite concentrations in Cannabis sativa. <em>Environmental and Experimental Botany</em> 228:106036.", "url": "https://www.sciencedirect.com/science/article/pii/S0098847224004179", "peer": True},
    "huebner2024-uv-spectra": {"cite": "Huebner DS, Batarshin M, Beck S, König L, Mewis I, Ulrichs C (2024). Influence of different UV spectra and intensities on yield and quality of cannabis inflorescences. <em>Front. Plant Sci.</em> 15:1480876.", "url": "https://doi.org/10.3389/fpls.2024.1480876", "peer": True},
    "collado2025-light": {"cite": "Collado CE, Hernandez R (2025). Vegetative and reproductive stage lighting interactions on flower yield, water-use efficiency, terpenes and cannabinoids of Cannabis sativa. <em>Scientific Reports</em> 15:s41598-025-27437-4.", "url": "https://www.nature.com/articles/s41598-025-27437-4", "peer": True},
    "faust2018-dli": {"cite": "Faust JE, Logan J (2018). Daily light integral: a research review and high-resolution maps of the United States. <em>HortScience</em> 53(9):1250-1257.", "url": "https://doi.org/10.21273/HORTSCI13144-18", "peer": True},
    "inoue2021-vpd": {"cite": "Inoue T, et al. (2021). Minimizing VPD fluctuations maintains higher stomatal conductance and photosynthesis, improving plant growth in lettuce. <em>Front. Plant Sci.</em> 12:646144.", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8049605/", "peer": True},
    "schymanski2016-wind": {"cite": "Schymanski SJ, Or D (2016). Wind increases leaf water use efficiency. <em>Plant, Cell & Environment</em> 39(7):1448-1459.", "url": "https://onlinelibrary.wiley.com/doi/10.1111/pce.12700", "peer": True},
    "punja2019-pathogens": {"cite": "Punja ZK, Collyer D, Scott C, Lung S, Holmes J, Sutton D (2019). Pathogens and molds affecting production and quality of Cannabis sativa L. <em>Front. Plant Sci.</em> 10:1120.", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC6811654/", "peer": True},
    "punja-budrot-cjb": {"cite": "Mahmoud M, BenRejeb I, Punja ZK, Buirs L, Jabaji S (2023). Understanding bud rot development, caused by Botrytis cinerea, on cannabis grown under greenhouse conditions. <em>Botany / Can. J. Bot.</em> 101(8).", "url": "https://doi.org/10.1139/cjb-2022-0139", "peer": True},
    "malik2025-media": {"cite": "Malik M, Tlustoš P (2025). Soilless growing media for cannabis cultivation. <em>Agriculture</em> 15(18):1955.", "url": "https://www.mdpi.com/2077-0472/15/18/1955", "peer": True},

    # ---- airflow ----
    "kitaya2004-airvel": {"cite": "Kitaya Y, Shibuya T, Yoshida M, Kiyota M (2004). Effects of air velocity on photosynthesis of plant canopies under elevated CO2 levels. <em>Adv. Space Res.</em> 34(7):1466-1469.", "url": "https://doi.org/10.1016/j.asr.2003.08.031", "peer": True},
    "dupont2025-wind": {"cite": "Dupont K, van den Berg TE, Zhang J, Moene AF, Vialet-Chabrand SRM (2025). Beyond the boundary: a new road to improve photosynthesis via wind. <em>J. Exp. Bot.</em> 76(20):5791-5813.", "url": "https://doi.org/10.1093/jxb/eraf325", "peer": True},
    "schuepp1993-bl": {"cite": "Schuepp PH (1993). Tansley Review No. 59: Leaf boundary layers. <em>New Phytologist</em> 125(3):477-507.", "url": "https://doi.org/10.1111/j.1469-8137.1993.tb03898.x", "peer": True},
    "kitaya2010-circ": {"cite": "Kitaya Y, Tsuruyama J, Shibuya T, Yoshida M, Kiyota M (2010). CO2 and air circulation effects on photosynthesis and transpiration of tomato seedlings. <em>Scientia Horticulturae</em> 126(2):326-330.", "url": "https://www.sciencedirect.com/science/article/abs/pii/S0304423810003316", "peer": True},
    "gilliham2011-ca": {"cite": "Gilliham M, et al. (2011). Calcium delivery and storage in plant leaves: exploring the link with water flow. <em>J. Exp. Bot.</em> 62(7):2233-2250.", "url": "https://doi.org/10.1093/jxb/err111", "peer": True},
    "chehab2009-thigmo": {"cite": "Chehab EW, Eich E, Braam J (2009). Thigmomorphogenesis: a complex plant response to mechano-stimulation. <em>J. Exp. Bot.</em> 60(1):43-56.", "url": "https://doi.org/10.1093/jxb/ern315", "peer": True},
    "tjosvold2018-air": {"cite": "Tjosvold SA (2018). Maximize photosynthesis with moving air. <em>UC ANR Greenhouse & Floriculture</em> (extension article).", "url": "https://ucanr.edu/blogs/blogcore/postdetail.cfm?postnum=28455", "peer": False},

    # ---- mould ----
    "benedict2020-cdc": {"cite": "Benedict K, Thompson GR, Jackson BR (2020). Cannabis use and fungal infections in a commercially insured population, United States, 2016. <em>Emerg. Infect. Dis.</em> 26(6):1308-1310.", "url": "https://doi.org/10.3201/eid2606.191570", "peer": True},
    "gwinn2023-mycotoxin": {"cite": "Gwinn KD, Leung MCK, Stephens AB, Punja ZK (2023). Fungal and mycotoxin contaminants in cannabis and hemp flowers: implications for consumer health. <em>Front. Microbiol.</em> 14:1278189.", "url": "https://doi.org/10.3389/fmicb.2023.1278189", "peer": True},
    "punja2025-budrot-epi": {"cite": "Punja ZK, et al. (2025). The epidemiology and management of Botrytis cinerea causing bud rot on greenhouse-cultivated cannabis. <em>Can. J. Plant Pathol.</em>", "url": "https://doi.org/10.1080/07060661.2025.2478250", "peer": True},
    "buirs2024-idm": {"cite": "Buirs L, Punja ZK (2024). Integrated management of pathogens and microbes in Cannabis sativa L. under greenhouse conditions. <em>Plants</em> 13:786.", "url": "https://doi.org/10.3390/plants13060786", "peer": True},
    "scott2021-pm": {"cite": "Scott C, Punja ZK (2021). Evaluation of disease management approaches for powdery mildew on Cannabis sativa L. <em>Can. J. Plant Pathol.</em> 43(3):394-412.", "url": "https://doi.org/10.1080/07060661.2020.1836026", "peer": True},
    "alubeed2022-postharvest": {"cite": "AL Ubeed HMS, Wills RBH, Chandrapala J (2022). Post-harvest operations to generate high-quality medicinal cannabis products: a systematic review. <em>Molecules</em> 27:1719.", "url": "https://doi.org/10.3390/molecules27051719", "peer": True},
    "sun2025-drying": {"cite": "(2025). Post-harvest drying and curing affect cannabinoid contents and microbial levels in industrial hemp (Cannabis sativa L.). <em>Plants</em> 14(3):414.", "url": "https://doi.org/10.3390/plants14030414", "peer": True},
    "mckernan2016-micro": {"cite": "McKernan K, Spangler J, Helbert Y, et al. (2016). Metagenomic analysis of medicinal cannabis samples. <em>F1000Research</em> 5:2471.", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5089129/", "peer": True},

    # ---- CO2 enrichment ----
    "tolbert1995-compensation": {"cite": "Tolbert NE, Benker C, Beck E (1995). The oxygen and carbon dioxide compensation points of C3 plants: possible role in regulating atmospheric oxygen and carbon dioxide concentrations. <em>Proc. Natl. Acad. Sci. USA</em> 92(24):11230-11233.", "url": "https://doi.org/10.1073/pnas.92.24.11230", "peer": True},
    "chandra2011-co2": {"cite": "Chandra S, Lata H, Khan IA, ElSohly MA (2011). Photosynthetic response of <em>Cannabis sativa</em> L., an important medicinal plant, to elevated levels of CO2. <em>Physiol. Mol. Biol. Plants</em> 17(3):291-295.", "url": "https://doi.org/10.1007/s12298-011-0066-6", "peer": True},
    "amthor2024-respiration": {"cite": "Amthor JS (2024). After photosynthesis, what then? Importance of respiration to crop growth and yield. <em>Field Crops Research</em> 321:109638.", "url": "https://www.sciencedirect.com/science/article/pii/S0378429024003915", "peer": True},
    "collalti2019-npp": {"cite": "Collalti A, Prentice IC (2019). Is NPP proportional to GPP? Waring's hypothesis 20 years on. <em>Tree Physiology</em> 39(8):1473-1483 (mean NPP:GPP ~0.46).", "url": "https://doi.org/10.1093/treephys/tpz034", "peer": True},
    "atkin2003-q10": {"cite": "Atkin OK, Tjoelker MG (2003). Thermal acclimation and the dynamic response of plant respiration to temperature. <em>Trends in Plant Science</em> 8(7):343-351 (respiration Q10 ~2).", "url": "https://doi.org/10.1016/S1360-1385(03)00136-5", "peer": True},
    "lv2022-topt": {"cite": "Lv Z, Zhu Y, Liu X, et al. (2022). Elevated [CO2] raises the temperature optimum of photosynthesis and thus promotes net photosynthesis of winter wheat and rice. <em>Physiologia Plantarum</em> 174(6):e13757.", "url": "https://doi.org/10.1111/ppl.13757", "peer": True},
    "doddrell2023-co2": {"cite": "Doddrell NH, Lawson T, Raines CA, Wagstaff C, Simkin AJ (2023). Feeding the world: impacts of elevated [CO2] on nutrient content of greenhouse-grown fruit crops and options for future yield gains. <em>Horticulture Research</em> 10(4):uhad026.", "url": "https://doi.org/10.1093/hr/uhad026", "peer": True},
    "permentier2017-co2poison": {"cite": "Permentier K, Vercammen S, Soetaert S, Schellemans C (2017). Carbon dioxide poisoning: a literature review of an often forgotten cause of intoxication in the emergency department. <em>Int. J. Emerg. Med.</em> 10:14.", "url": "https://doi.org/10.1186/s12245-017-0142-y", "peer": True},
    "azuma2018-cognition": {"cite": "Azuma K, Kagi N, Yanagi U, Osawa H (2018). Effects of low-level inhalation exposure to carbon dioxide in indoor environments: a short review on human health and psychomotor performance. <em>Environment International</em> 121:51-56.", "url": "https://doi.org/10.1016/j.envint.2018.08.059", "peer": True},
    "wang2022-co2cue": {"cite": "Wang X, Lv J, Shi X, et al. (2022). CO2 enrichment in greenhouse production: towards a sustainable approach. <em>Frontiers in Plant Science</em> 13:1029901 (CO2 use efficiency below ~50-60% from leakage).", "url": "https://doi.org/10.3389/fpls.2022.1029901", "peer": True},
    "kader2002-respiration": {"cite": "Kader AA, Saltveit ME (2002). Respiration and gas exchange. In <em>Postharvest Technology of Horticultural Crops</em>, 3rd ed. Univ. of California ANR Publication 3311.", "url": "https://escholarship.org/uc/item/8q37j80t", "peer": False},
    "noaa2024-co2": {"cite": "NOAA Global Monitoring Laboratory (2024). Trends in atmospheric carbon dioxide, global monthly/annual means (2024 global mean 422.8 ppm).", "url": "https://gml.noaa.gov/ccgg/trends/global.html", "peer": False},
    "westmoreland2023-usu": {"cite": "Westmoreland FM (2023). Environmental Physiology of Medical Cannabis. PhD dissertation, Utah State University (Bugbee Crop Physiology Lab): CO2 enrichment to 1,200-1,400 ppm raised dry flower yield ~40%.", "url": "https://digitalcommons.usu.edu/etd2023/243/", "peer": False},
    "ahdb-co2": {"cite": "Agriculture & Horticulture Development Board (AHDB). CO2 enrichment: best-practice guide (a sealed glasshouse can fall to ~200 ppm, cutting canopy photosynthesis ~26%).", "url": "https://horticulture.ahdb.org.uk/knowledge-library/co2-best-practice-guide-background", "peer": False},
    "okstate-co2": {"cite": "Oklahoma State University Extension. Greenhouse carbon dioxide supplementation (HLA-6723).", "url": "https://extension.okstate.edu/fact-sheets/greenhouse-carbon-dioxide-supplementation.html", "peer": False},
    "osha-pel-co2": {"cite": "US OSHA. Annotated Permissible Exposure Limits, Table Z-1, carbon dioxide (CAS 124-38-9): PEL 5,000 ppm 8-hour TWA.", "url": "https://www.osha.gov/annotated-pels/table-z-1", "peer": False},
    "niosh-co2": {"cite": "US NIOSH / CDC. Pocket Guide to Chemical Hazards and IDLH documentation, carbon dioxide: REL 5,000 ppm TWA, STEL 30,000 ppm, IDLH 40,000 ppm; 1 ppm = 1.80 mg/m3.", "url": "https://www.cdc.gov/niosh/idlh/124389.html", "peer": False},
    "worksafenz-co2": {"cite": "WorkSafe New Zealand (2025). Workplace Exposure Standards and Biological Exposure Indices, 15th ed., carbon dioxide: WES-TWA 5,000 ppm, WES-STEL 30,000 ppm.", "url": "https://www.worksafe.govt.nz/topic-and-industry/monitoring/workplace-exposure-standards-and-biological-exposure-indices/all-substances/view/carbon-dioxide/", "peer": False},
    "ifc5307": {"cite": "International Code Council (2021). International Fire Code, Section 5307, carbon dioxide systems: gas detection alarming at 5,000 ppm (low) and 30,000 ppm (high) for installations over 100 lb CO2, with automatic shutoff and ventilation.", "url": "https://codes.iccsafe.org/s/IFC2021P2/part-v-hazardous-materials/IFC2021P2-Pt05-Ch53-Sec5307.3.2", "peer": False},
    "sensirion-scd": {"cite": "Sensirion. SCD30 / SCD4x NDIR CO2 sensor datasheets and SCD30 field-calibration application note (ASC/ABC assumes periodic exposure to ~400 ppm fresh air).", "url": "https://sensirion.com/products/catalog/SCD30", "peer": False},
    "winsen-mq": {"cite": "Zhengzhou Winsen Electronics. MQ-135 and MQ-5 metal-oxide gas sensor datasheets (MQ-135 infers equivalent-CO2 from mixed VOCs; MQ-5 targets LPG / combustible gas).", "url": "https://www.winsen-sensor.com/d/files/MQ-5.pdf", "peer": False},

    # ---- stale air / air exchange (why a sealed room purges) ----
    "epa-hepa": {"cite": "US EPA. What is a HEPA filter? A HEPA filter removes at least 99.97% of airborne particles at 0.3 um (particulates only, not gases).", "url": "https://www.epa.gov/indoor-air-quality-iaq/what-hepa-filter", "peer": False},
    "souza2024-carbon-ethylene": {"cite": "Souza et al. (2024). Ethylene elimination using activated carbons impregnated with copper oxide. <em>Molecules</em> 29(12):2717 (plain activated carbon held ~1,111 ug ethylene/g; ethylene kinetic diameter ~3.9 A).", "url": "https://doi.org/10.3390/molecules29122717", "peer": True},
    "alvarez2024-ethylene": {"cite": "Alvarez-Hernandez MH, et al. (2024). Postharvest handling of ethylene with oxidative and absorptive means (review). <em>PMC10933227</em> (KMnO4 scrubbers ~40-80 mg ethylene/g, irreversible; activated carbon 11-78 mmol/kg; photocatalytic TiO2/UV).", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10933227/", "peer": True},
    "abeles1992-ethylene": {"cite": "Abeles FB, Morgan PW, Saltveit ME (1992). <em>Ethylene in Plant Biology</em>, 2nd ed. Academic Press (response threshold ~10 ppb; half-maximal response 0.1-1 ppm).", "url": "", "peer": True},
    "cornell-ethylene": {"cite": "Cornell University Greenhouse Horticulture. Ethylene in the greenhouse: symptoms, detection and prevention (chronic damage from ~10 ppb; acute epinasty/abscission/chlorosis above 0.1 ppm).", "url": "https://greenhouse.cornell.edu/crops-culture/ethylene-in-the-greenhouse-symptoms-detection-prevention/", "peer": False},
    "wheeler1996-ethylene": {"cite": "Wheeler RM, Peterson BV, Sager JC, Knott WM (1996). Ethylene production by plants in a closed environment. <em>Advances in Space Research</em> 18(4-5):193-196 (sealed NASA CELSS chamber reached 40-120 ppb ethylene from plant emission alone; visible wheat epinasty).", "url": "https://doi.org/10.1016/0273-1177(95)00877-h", "peer": True},
    "hudelson2023-ethylene": {"cite": "Hudelson TJ, et al. (2023). Elevated atmospheric ethylene and high temperature independently inhibit fruit set but not vegetative growth in tomato. <em>HortScience</em> 58 (continuous 20 ppb cut fruit yield to 37-51% of control; 40 ppb to 4-11%; vegetative growth reduced &lt;10%).", "url": "https://journals.ashs.org/hortsci/view/journals/hortsci/58/3/article-p247.xml", "peer": True},
    "monthony2026-ethylene": {"cite": "Monthony AS, et al. (2026). Sex-specific ethylene responses drive floral sexual plasticity in <em>Cannabis sativa</em>. <em>The Plant Journal</em> (cannabis has an intact, sensitive ethylene-signalling pathway).", "url": "", "peer": True},
    "osha-oxygen": {"cite": "US OSHA. 29 CFR 1910.146, permit-required confined spaces: an oxygen-deficient atmosphere is below 19.5% O2 (normal air is ~20.9%).", "url": "https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.146", "peer": False},
    "hpac-latent": {"cite": "HPAC Engineering. Latent loads matter: HVAC for cannabis grow facilities (transpiration returns most irrigation water to room air as vapour, the dominant dehumidification load; filters do not remove it).", "url": "https://www.hpac.com/industrial/article/21270796/latent-loads-matter-hvac-for-cannabis-grow-facilities", "peer": False},
    "zhang2020-canopy-rh": {"cite": "Zhang D, et al. (2020). Substantial differences occur between canopy and ambient climate: quantification of interactions in a greenhouse-canopy system. <em>PLoS ONE</em> 15(5):e0233210 (in-canopy RH ~15-25% higher than surrounding air).", "url": "https://doi.org/10.1371/journal.pone.0233210", "peer": True},
    "baptista2012-ventilation": {"cite": "Baptista FJ, et al. (2012). Effect of nocturnal ventilation on the occurrence of Botrytis cinerea in Mediterranean unheated tomato greenhouses. <em>Crop Protection</em> (ventilation that lowers humidity reduced grey mould).", "url": "", "peer": True},
    "liang2026-cannabis-ach": {"cite": "Liang J, et al. (2026). CO2 and air-change-rate optimisation in photoautotrophic micropropagation of medicinal <em>Cannabis sativa</em>. <em>Industrial Crops and Products</em> (~4.4 air changes/hour optimal at 800 ppm CO2; higher exchange dried the substrate). Plantlet-scale.", "url": "", "peer": True},
}

# Merge generated citations (non-destructive: existing ids win).
for _genmod in ("data.refs_gen", "data.refs_gen4", "data.refs_gen5", "data.refs_gen6", "data.refs_gen7", "data.refs_gen8"):
    try:
        _m = __import__(_genmod, fromlist=["REFS_ADD"])
        for _k, _v in _m.REFS_ADD.items():
            REFS.setdefault(_k, _v)
    except Exception:
        pass
