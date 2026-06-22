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
}

# Merge generated citations (non-destructive: existing ids win).
for _genmod in ("data.refs_gen", "data.refs_gen4", "data.refs_gen5", "data.refs_gen6", "data.refs_gen7"):
    try:
        _m = __import__(_genmod, fromlist=["REFS_ADD"])
        for _k, _v in _m.REFS_ADD.items():
            REFS.setdefault(_k, _v)
    except Exception:
        pass
