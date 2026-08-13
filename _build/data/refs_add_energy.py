# -*- coding: utf-8 -*-
# Energy, utilities & sustainability paper sources: benchmark studies, efficacy,
# demand charges, water reuse, grid carbon.
REFS_ADD = {
    "mills2012-carbon": {
        "cite": "Mills E (2012). The carbon footprint of indoor Cannabis production. "
                "<em>Energy Policy</em> 46:58-67. (End-use split lighting 33% / ventilation+"
                "dehumidification 27% / AC 19%; ~6,074 kWh and 4,600 kg CO2e per kg; ~13,000 kWh/yr "
                "per 4'x4'x8' module; ~1% of US electricity, ~US$6B/yr.)",
        "url": "https://doi.org/10.1016/j.enpol.2012.03.023", "peer": True},
    "summers2021-natsust": {
        "cite": "Summers HM, Sproul E, Quinn JC (2021). The greenhouse gas emissions of indoor "
                "cannabis production in the United States. <em>Nature Sustainability</em> 4:644-650. "
                "(Cradle-to-gate 2,283-5,184 kg CO2e/kg by location, median 3,658; HVAC the largest "
                "contributor everywhere, lights second; surveyed ventilation 12-60 ACH; modelled "
                "electricity ~1,700-5,300 kWh/kg; US grid intensity ~245-766 g CO2e/kWh.)",
        "url": "https://doi.org/10.1038/s41893-021-00691-w", "peer": True},
    "mills2025-oneearth": {
        "cite": "Mills E (2025). Energy-intensive indoor cultivation drives the cannabis industry's "
                "expanding carbon footprint. <em>One Earth</em> 8(2). (Industry-wide ~44 Mt CO2e/yr, "
                "~1% of total US emissions, ~90% from indoor production; ~US$11B annual energy bill; "
                "air-change rates ~60x homes.)",
        "url": "https://www.cell.com/one-earth/fulltext/S2590-3322(25)00005-3", "peer": True},
    "nwpcc2018-cannabis": {
        "cite": "Northwest Power and Conservation Council (2018). Electricity consumption from "
                "Northwest cannabis production (survey of licensed Oregon and Washington producers, "
                "2017 canopy data). (Annual intensity: indoor ~128, mixed 38, greenhouse 12, outdoor "
                "~1 kWh per ft2 of canopy; lighting ~100 of the indoor 128; OR+WA total ~112 aMW.)",
        "url": "https://www.nwcouncil.org/sites/default/files/cannabisReport.pdf", "peer": False},
    "remillard2017-aceee": {
        "cite": "Remillard J, Collins N (2017). Trends and observations of energy use in the cannabis "
                "industry. <em>ACEEE Summer Study on Energy Efficiency in Industry</em>. (~200 W/ft2 "
                "power density; ~2,000 kWh/lb; LED retrofit examples 1,000&rarr;600 W flower and "
                "600&rarr;300 W veg with ~2,300-2,600 kWh/yr saved incl. cooling at COP ~2.9 and 2-4 "
                "yr paybacks; heat-recovery dehumidification 30-50% savings in UC Davis WCEC testing; "
                "energy 20-50% of production cost.)",
        "url": "https://www.aceee.org/files/proceedings/2017/data/polopoly_fs/1.3687880.1501159058!/fileserver/file/790266/filename/0036_0053_000046.pdf", "peer": True},
    "zheng2021-review": {
        "cite": "Zheng Z, Fiddes K, Yang L (2021). A narrative review on environmental impacts of "
                "cannabis cultivation. <em>Journal of Cannabis Research</em> 3:35. (Compiles Mills/"
                "NPCC end-use splits; water use ~22.7 L/plant/day outdoor in season and ~2.5-2.8 "
                "gal/plant/day indoor at peak.)",
        "url": "https://doi.org/10.1186/s42238-021-00090-0", "peer": True},
    "kusuma2020-efficacy": {
        "cite": "Kusuma P, Pattison PM, Bugbee B (2020). From physics to fixtures to food: current "
                "and potential LED efficacy. <em>Horticulture Research</em> 7:56. (1,000 W DE HPS "
                "1.72 umol/J; 2020 LED fixtures 2.5-2.8 white+red and 3.0 blue+red; practical limits "
                "3.4 and 4.1 umol/J.)",
        "url": "https://doi.org/10.1038/s41438-020-0283-7", "peer": True},
    "dlc-hort-v4": {
        "cite": "DesignLights Consortium (2025). Horticultural technical requirements V4.0 and "
                "qualified products list. (Minimum photosynthetic photon efficacy 2.5 umol/J from "
                "April 2025 - >45% above 1,000 W DE HPS; V3.0 floor was 2.30 from March 2023, itself "
                "21% above V2.1's 1.90.)",
        "url": "https://designlights.org/our-work/horticultural-lighting/technical-requirements/hort-v4-0/", "peer": False},
    "rii-led-2022": {
        "cite": "Resource Innovation Institute (2022). Study of cannabis energy use: indoor "
                "cultivation operations using LED lighting demonstrate better efficiency (84-facility "
                "PowerScore analysis: LED-flowering facilities averaged 34% better facility "
                "efficiency and 80% better production efficiency than DE HPS facilities).",
        "url": "https://resourceinnovation.org/press-release/study-of-cannabis-energy-use-shows-indoor-cultivation-operations-using-led-lighting-demonstrate-better-efficiency/", "peer": False},
    "rii-powerscore": {
        "cite": "Resource Innovation Institute. Cannabis PowerScore benchmarking platform (facility "
                "efficiency kWh/ft2 of flowering canopy and production efficiency g/kWh; documented "
                "Oregon HPS&rarr;LED retrofit +68% g/kWh; most facilities estimated able to save "
                ">=30% of energy spend).",
        "url": "https://resourceinnovation.org/blog/welcome-to-the-cannabis-powerscore-an-energy-benchmarking-tool-for-growers-of-all-types/", "peer": False},
    "nrel2017-demand": {
        "cite": "McLaren J, Gagnon P, Anderson K, et al. (2017). Identifying potential markets for "
                "behind-the-meter battery energy storage: a survey of U.S. demand charges. NREL / "
                "Clean Energy Group. (~5 million of 18M US commercial customers can face demand "
                "charges above US$15/kW-month.)",
        "url": "https://www.nrel.gov/news/press/2017/where-commercial-customers-benefit-from-battery-energy-storage.html", "peer": False},
    "nfd2018-energy": {
        "cite": "New Frontier Data, Resource Innovation Institute, Scale Microgrid Solutions (2018). "
                "The 2018 Cannabis Energy Report. (US legal cultivation ~1.1 TWh/yr with +162% "
                "forecast by 2022; electricity-related emissions ~22.7 kg CO2e/kg outdoor and "
                "~326.6 kg CO2e/kg greenhouse.)",
        "url": "https://catalog.resourceinnovation.org/item/the-2018-cannabis-energy-report-407554", "peer": False},
    "cbt-condensate": {
        "cite": "Cannabis Business Times / Desert Aire. A guide to recovering condensate water in "
                "cannabis cultivation facilities. (Large flower-room dehumidification can yield ~500 "
                "gal (~1,900 L) per week of near-distilled condensate; filter, sterilise and "
                "re-mineralise before reuse; watch coil metals and drain-pan biofilm.)",
        "url": "https://www.cannabisbusinesstimes.com/irrigation/news/15687039/a-guide-to-recovering-condensate-water-in-cannabis-cultivation-facilities", "peer": False},
    "mbie-energy-nz": {
        "cite": "NZ Ministry of Business, Innovation &amp; Employment. Energy in New Zealand "
                "(renewable share of electricity generation 85.5% in 2024; 88.1% in 2023).",
        "url": "https://www.mbie.govt.nz/building-and-energy/energy-and-natural-resources/energy-statistics-and-modelling/energy-publications-and-technical-papers/energy-in-new-zealand", "peer": False},
}
