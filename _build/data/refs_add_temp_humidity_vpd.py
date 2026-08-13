# -*- coding: utf-8 -*-
"""References added for the temperature / humidity / VPD paper. URLs verified 2026-08."""

REFS_ADD = {
    "fao56-1998": {
        "cite": "Allen RG, Pereira LS, Raes D, Smith M (1998). Crop evapotranspiration - guidelines "
                "for computing crop water requirements. FAO Irrigation and Drainage Paper 56, "
                "Chapter 3: meteorological data (Tetens saturation vapour pressure equation, vapour "
                "pressure deficit and dew point relations). Rome: FAO.",
        "url": "https://www.fao.org/4/x0490e/x0490e07.htm",
        "peer": False,
    },
    "nelson2015-leaftemp": {
        "cite": "Nelson JA, Bugbee B (2015). Analysis of environmental effects on leaf temperature "
                "under sunlight, high pressure sodium and light emitting diodes. <em>PLoS ONE</em> "
                "10(10):e0138930 (well-watered leaves typically within ~2 °C of air; LED "
                "canopies ~1.3 °C cooler than HPS at equal photon flux; water-stressed leaves "
                "modelled 6-12 °C above air).",
        "url": "https://doi.org/10.1371/journal.pone.0138930",
        "peer": True,
    },
    "corredor2025-rh": {
        "cite": "Corredor-Perilla IC, et al. (2025). Elevated relative humidity significantly "
                "decreases cannabinoid concentrations while delaying flowering development in "
                "<em>Cannabis sativa</em> L. <em>Front. Plant Sci.</em> 16:1678142 (flowering at "
                "0.05-0.25 kPa VPD vs 0.92-1.29 kPa: -71% flower biomass, three-week flowering "
                "delay, multi-fold cannabinoid reductions).",
        "url": "https://doi.org/10.3389/fpls.2025.1678142",
        "peer": True,
    },
    "jin2019-cannabis-env": {
        "cite": "Jin D, Jin S, Chen J (2019). Cannabis indoor growing conditions, management "
                "practices, and post-harvest treatment: a review. <em>Am. J. Plant Sci.</em> "
                "10(6):925-946 (recommends ~75% RH for juvenile plants and 55-60% RH through "
                "vegetative growth and flowering at 25 °C).",
        "url": "https://doi.org/10.4236/ajps.2019.106067",
        "peer": True,
    },
    "pulse-vpd-guide": {
        "cite": "Pulse Labs. The ultimate vapor pressure deficit (VPD) guide: leaf-basis VPD "
                "formula, leaf-offset calculator (leaves typically 1-3 °C below air) and stage "
                "bands (~0.8 kPa clones/seedlings, ~1.0 kPa veg, 1.2-1.5 kPa flower). Industry "
                "convention reference, not peer-reviewed.",
        "url": "https://pulsegrow.com/blogs/learn/vpd",
        "peer": False,
    },
    "caird2007-night": {
        "cite": "Caird MA, Richards JH, Donovan LA (2007). Nighttime stomatal conductance and "
                "transpiration in C3 and C4 plants. <em>Plant Physiol.</em> 143(1):4-10 (night "
                "transpiration commonly 5-15% of daytime rates, at times up to ~30%).",
        "url": "https://doi.org/10.1104/pp.106.092940",
        "peer": True,
    },
    "tarara2007-shield": {
        "cite": "Tarara JM, Hoheisel G-A (2007). Low-cost shielding to minimize radiation errors of "
                "temperature sensors in the field. <em>HortScience</em> 42(6):1372-1379 (radiation "
                "loading drives whole-degree errors in unaspirated air-temperature measurement; "
                "shielding and aspiration recover accuracy).",
        "url": "https://doi.org/10.21273/HORTSCI.42.6.1372",
        "peer": True,
    },
}
