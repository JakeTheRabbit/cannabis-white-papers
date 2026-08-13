# -*- coding: utf-8 -*-
# Sources for paper_hvac (HVAC, cooling and dehumidification). Merged into data.refs REFS.
REFS_ADD = {
    "desertaire-an25-load": {
        "cite": "Desert Aire. Grow room load determination. Application Note 25 (DA125) "
                "(lighting is the largest sensible load in indoor farming; latent load is "
                "transpiration plus evaporation from media, irrigation and wetted surfaces; "
                "~99% of water delivered to the roots passes through the stomata as vapour; at "
                "lights-off a standard air conditioner satisfies the small sensible demand and "
                "shuts off before the moisture is removed). Manufacturer engineering note.",
        "url": "https://www.desert-aire.com/resources/application-notes/grow-room-load-determination",
        "peer": False},
    "streit2023-hvacd": {
        "cite": "Streit L (IMEG Corp). Cannabis grow facility design 101, part 3: HVACD and air "
                "distribution. <em>PHCP Pros</em> (grow lights are the bulk of the sensible "
                "cooling load; latent load follows irrigation &mdash; water in equals water out; "
                "typical rooms run 20-40 air turns per hour with ~100% recirculation; equipment "
                "tiers from packaged DX plus dehumidifiers, through DX with hot-gas reheat, to "
                "chilled-water plants with reheat). Engineering trade article.",
        "url": "https://www.phcppros.com/articles/16050-cannabis-grow-facility-design-101-part-3-hvacd-and-air-distribution",
        "peer": False},
    "streit2023-water": {
        "cite": "Streit L (IMEG Corp). Cannabis grow facility design 101, part 2: water usage. "
                "<em>PHCP Pros</em> (80-95% of irrigation water is transpired and returns via the "
                "HVACD system as condensate from coils and dehumidifiers; condensate can be "
                "captured, retreated &mdash; typically through RO &mdash; and reused for "
                "irrigation). Engineering trade article.",
        "url": "https://www.phcppros.com/articles/15572-cannabis-grow-facility-design-101-part-2-water-usage",
        "peer": False},
    "quest-perfect-dehu": {
        "cite": "Quest Climate. Grow room dehumidifiers: perfect your setup (water in = water "
                "out sizing: gallons irrigated minus gallons drained, times 8 pints per gallon "
                "&mdash; e.g. 25 gal fed with 5 gal to drain = 160 pints/day to remove; plan "
                "dehumidification for worst-case days). Manufacturer application guide.",
        "url": "https://www.questclimate.com/perfect-grow-room-dehumidifier/",
        "peer": False},
    "quest-dehu101": {
        "cite": "Quest Climate. Dehumidification 101 for cannabis growers (air conditioners "
                "dehumidify poorly and sit idle at lights-off, so dedicated dehumidifiers carry "
                "the overnight moisture; baseline 0.5-2 pints/day per square foot of canopy; "
                "cooling air raises its RH &mdash; a mid-70s &deg;F room at ~57% RH lands near "
                "80% when cooled to 65 &deg;F; excess humidity drives Botrytis and powdery "
                "mildew). Manufacturer application guide.",
        "url": "https://www.questclimate.com/dehumidification-101-cannabis-growers/",
        "peer": False},
    "rii-hvac-bpg": {
        "cite": "Resource Innovation Institute (2019). Best practices guide: HVAC for cannabis "
                "cultivation &amp; controlled environment agriculture (peer-reviewed industry "
                "guide from RII's Technical Advisory Council; energy is 30-60% of indoor "
                "operating expense; centralised CEA dehumidification substantially reduces "
                "operating cost).",
        "url": "https://resourceinnovation.org/blog/riis-hvac-best-practices-guide-demystifies-approaches-to-efficient-cooling-and-dehumidification/",
        "peer": False},
    "hydrobuilder-ac-sizing": {
        "cite": "Hydrobuilder Learning Center. Grow room air conditioner sizing guide (every "
                "watt of equipment makes ~3.41 BTU/h of heat; HPS folklore runs 3.5-4 BTU/W; "
                "dehumidifier draw returns ~100% as heat; ~400 BTU/h per person; add 20-30% "
                "margin; 1 ton = 12,000 BTU/h). Industry sizing guide.",
        "url": "https://learn.hydrobuilder.com/grow-room-air-conditioner-sizing-buying-guide/",
        "peer": False},
    "sylvane-desiccant": {
        "cite": "Sylvane. Desiccant vs. refrigerant dehumidifiers: which is best for you? "
                "(refrigerant units condense moisture on a cold coil and lose capacity as the "
                "space cools, icing at low temperatures; desiccant wheels keep near-full capacity "
                "in cold rooms and add several degrees of regeneration heat to the airstream). "
                "Industry knowledge base.",
        "url": "https://www.sylvane.com/blogs/knowledge-center/desiccant-vs-refrigerant-dehumidifiers",
        "peer": False},
    "ncia-condensate": {
        "cite": "Robinson T, Lisabeth K (Silver Bullet Water Treatment) (2020). Condensate "
                "recapture for cannabis cultivation facilities. National Cannabis Industry "
                "Association member blog (condensate is low-TDS with pH ~5.5-6.5 from dissolved "
                "CO2, but can carry VOCs, coil metals &mdash; lead, zinc, aluminium, copper "
                "&mdash; and microbes; treat with filtration plus UV/AOP disinfection before "
                "reuse, and baseline-test regularly).",
        "url": "https://thecannabisindustry.org/member-blog-condensate-recapture-for-cannabis-cultivation-facilities-making-informed-decisions-to-save-resources-and-improve-efficiency/",
        "peer": False},
    "summers2021-ghg": {
        "cite": "Summers HM, Sproul E, Quinn JC (2021). The greenhouse gas emissions of indoor "
                "cannabis production in the United States. <em>Nature Sustainability</em> "
                "4:644-650 (life-cycle emissions of 2,283-5,184 kg CO2e per kg of dried flower "
                "depending on location; environmental control &mdash; HVAC and ventilation "
                "&mdash; among the dominant energy and emissions drivers alongside lighting and "
                "CO2 supply).",
        "url": "https://doi.org/10.1038/s41893-021-00691-w",
        "peer": True},
}
