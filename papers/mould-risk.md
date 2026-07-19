---
slug: "mould-risk"
title: "Mould risk: preventing and stopping bud rot"
eyebrow: "Beginner · Mould risk"
summary: "Mould is the disease most likely to wipe out a harvest in the final weeks, and the one that can quietly make your flower unsafe to consume. Learn the conditions it needs, how to deny them, and what to do the moment you find it."
track: "Plant health"
read_time: "~15 min read"
diagrams: "3 diagrams"
related: ["grow-room-systems", "airflow-design", "tissue-culture"]
url: "https://jaketherabbit.github.io/cannabis-white-papers/mould-risk.html"
md_url: "https://jaketherabbit.github.io/cannabis-white-papers/papers/mould-risk.md"
version: "1.2"
updated: "2026-07-18"
license: "CC BY-NC 4.0"
license_url: "https://creativecommons.org/licenses/by-nc/4.0/"
attribution: "The Cannabis White Papers"
refs: [{"id": "punja-budrot-cjb", "n": 1, "cite": "Mahmoud M, BenRejeb I, Punja ZK, Buirs L, Jabaji S (2023). Understanding bud rot development, caused by Botrytis cinerea, on cannabis grown under greenhouse conditions. Botany / Can. J. Bot. 101(8).", "url": "https://doi.org/10.1139/cjb-2022-0139", "peer": true}, {"id": "punja2025-budrot-epi", "n": 2, "cite": "Punja ZK, et al. (2025). The epidemiology and management of Botrytis cinerea causing bud rot on greenhouse-cultivated cannabis. Can. J. Plant Pathol.", "url": "https://doi.org/10.1080/07060661.2025.2478250", "peer": true}, {"id": "scott2021-pm", "n": 3, "cite": "Scott C, Punja ZK (2021). Evaluation of disease management approaches for powdery mildew on Cannabis sativa L. Can. J. Plant Pathol. 43(3):394-412.", "url": "https://doi.org/10.1080/07060661.2020.1836026", "peer": true}, {"id": "buirs2024-idm", "n": 4, "cite": "Buirs L, Punja ZK (2024). Integrated management of pathogens and microbes in Cannabis sativa L. under greenhouse conditions. Plants 13:786.", "url": "https://doi.org/10.3390/plants13060786", "peer": true}, {"id": "mckernan2016-micro", "n": 5, "cite": "McKernan K, Spangler J, Helbert Y, et al. (2016). Metagenomic analysis of medicinal cannabis samples. F1000Research 5:2471.", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5089129/", "peer": true}, {"id": "alubeed2022-postharvest", "n": 6, "cite": "AL Ubeed HMS, Wills RBH, Chandrapala J (2022). Post-harvest operations to generate high-quality medicinal cannabis products: a systematic review. Molecules 27:1719.", "url": "https://doi.org/10.3390/molecules27051719", "peer": true}, {"id": "sun2025-drying", "n": 7, "cite": "(2025). Post-harvest drying and curing affect cannabinoid contents and microbial levels in industrial hemp (Cannabis sativa L.). Plants 14(3):414.", "url": "https://doi.org/10.3390/plants14030414", "peer": true}, {"id": "benedict2020-cdc", "n": 8, "cite": "Benedict K, Thompson GR, Jackson BR (2020). Cannabis use and fungal infections in a commercially insured population, United States, 2016. Emerg. Infect. Dis. 26(6):1308-1310.", "url": "https://doi.org/10.3201/eid2606.191570", "peer": true}, {"id": "gwinn2023-mycotoxin", "n": 9, "cite": "Gwinn KD, Leung MCK, Stephens AB, Punja ZK (2023). Fungal and mycotoxin contaminants in cannabis and hemp flowers: implications for consumer health. Front. Microbiol. 14:1278189.", "url": "https://doi.org/10.3389/fmicb.2023.1278189", "peer": true}, {"id": "punja2019-pathogens", "n": 10, "cite": "Punja ZK, Collyer D, Scott C, Lung S, Holmes J, Sutton D (2019). Pathogens and molds affecting production and quality of Cannabis sativa L. Front. Plant Sci. 10:1120.", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC6811654/", "peer": true}]
---

# Mould risk: preventing and stopping bud rot

_Beginner · Mould risk · ~15 min read_

> Mould is the disease most likely to wipe out a harvest in the final weeks, and the one that can quietly make your flower unsafe to consume. Learn the conditions it needs, how to deny them, and what to do the moment you find it.

## Why mould is the harvest-killer

You can do everything right for ten weeks and lose it all to grey fuzz in the last two. Mould thrives in exactly the warm, humid, densely-flowered conditions that also grow big buds. The worst of it hides _inside_ the bud, where you can't see it until it's spreading.

There is also a health stake. Cannabis users have been found to get fungal infections at about **3.5× more often** than non-users in one claims analysis (absolute rates still low; immunocompromised patients are the high-stakes group)[^benedict2020-cdc], and some moulds leave behind toxins that survive drying[^gwinn2023-mycotoxin]. This isn't only about yield. It is about safe medicine. This guide assumes you know nothing. Every term is defined.

## The words you need

**Bud rot (Botrytis)** — _Botrytis cinerea_, a grey mould that rots flowers from the inside out. The number-one late-flower killer.

**Powdery mildew (PM)** — A white, flour-like fungus that coats leaf surfaces. Different fungus, different look, also serious.

**Relative humidity (RH)** — How much water vapour the air holds versus the most it could hold, as a percentage. High RH is mould's best friend.

**Leaf wetness / free moisture** — Actual liquid water on the plant (condensation, spray). Many mould spores need it to germinate.

**Water activity** — How much ‘free’ water is available in dried flower for microbes to use. Keep it low in storage and mould can't grow.

**Mycotoxin** — A poison made by some moulds (e.g. _Aspergillus_). It can remain in the flower even after the mould itself is gone[^gwinn2023-mycotoxin].

## The two moulds you'll meet

**Bud rot, Botrytis**

Starts deep in a dense cola, often at a stem or where a leaf meets the bud. You'll see a single leaf go yellow or brown and pull out easily. Inside, the bud is grey, fluffy and crumbling. Spreads fast in the final weeks[^punja-budrot-cjb].

**Powdery mildew, PM**

White, dusty patches on the tops of leaves that wipe off like flour, then return. Loves moderate temps and stagnant, humid air. Coats leaves and chokes photosynthesis[^scott2021-pm].

> **NOTE — They're not the only ones**
>
> Indoor cannabis also hosts _Penicillium_, _Cladosporium_, _Fusarium_ and _Aspergillus_[^punja2019-pathogens]. Botrytis and PM are the two you'll meet first and most.

## The conditions that invite mould

Mould isn't bad luck. It is a recipe. Bud rot takes off when humidity climbs above about **70%** at moderate temperatures (~17–24 °C), especially when there's free moisture and still air[^punja2025-budrot-epi]. Deny the recipe and you deny the mould.

> **Diagram.** Risk rises steeply past ~70% RH[^punja2025-budrot-epi]. The trap: your room sensor can read 60% while the inside of a fat cola sits much higher.

> **Diagram.** The infection chain. Almost all of it happens out of sight, which is why prevention beats cure[^punja-budrot-cjb].

> **DANGER — The dense-canopy trap**
>
> A thick, undefoliated canopy traps warm, humid, still air inside itself, a private climate far wetter than your room reading[^punja-budrot-cjb]. Packing plants tight for yield directly raises rot risk. Spacing and defoliation are mould control, not just tidiness.

## Prevention: the daily routine

Prevention is a handful of boring habits done consistently. This is the whole job:

1. **Hold humidity down** — Keep flowering RH in the ~45–65% stage-dependent band (mid/late flower often ~45–55%), lower in late flower. A dehumidifier sized to your transpiration load is non-negotiable[^buirs2024-idm].
2. **Move air through the canopy** — Aim for ~0.5–1.0 m/s of gentle, turbulent air reaching inside the plants, not just over the top[^buirs2024-idm]. See the airflow paper.
3. **Open the canopy** — Defoliate and space plants so air and light penetrate. Density is the silent risk multiplier.
4. **Avoid free moisture** — No overhead watering or spraying in flower. Prevent condensation by avoiding big temperature swings at lights-off, so surfaces never hit dew point.
5. **Keep it clean** — Sanitise tools, surfaces and hands. HEPA-filter incoming air to cut the airborne spore count[^buirs2024-idm].
6. **Scout every day** — In the last few weeks, inspect daily. Catching one rotten bud early can save the room.

## Scouting: find it before it spreads

Spend five minutes a day in late flower with a bright light, looking _into_ the plants, not just at them:

- **The tell-tale.** A single leaf blade poking from a bud that's gone yellow or brown and slips out with a gentle tug. Pull it and check the bud beneath for grey fluff.
- **Where to look.** The biggest, densest top colas. Spots where a leaf petiole buries into the bud. Anywhere airflow is weak.
- **Powdery mildew.** White dust on upper leaf surfaces that smears like flour.
- **Smell.** A musty, hay-like or ‘off’ smell can precede visible rot.

## What to do when you find it

1. **Stop and isolate** — Don't fan it around. Hold a bag over the spot, cut well below the rot, and remove it from the room before opening the bag.
2. **Cut generously** — Bud rot runs further inside than it looks. Take the whole affected bud and a margin of healthy tissue.
3. **Sanitise** — Clean your tools and hands before touching another plant. Spores travel on everything.
4. **Fix the cause** — Finding rot means your humidity, airflow or density recipe failed somewhere. Drop RH, add through-canopy air, open the canopy.
5. **Consider harvest timing** — If rot is spreading fast late in flower, an early harvest of clean material can beat losing it all.

> **WARN — Don't try to ‘treat’ rotted flower into safety**
>
> Once a bud has rotted, it's waste, not something to dry and smoke. Drying lowers microbe levels but won't undo rot or remove mycotoxins[^sun2025-drying]. Prevention is the only real cure.

## Drying & storage: don't lose it at the finish

Mould can still strike clean flower during a sloppy dry or in storage. The defence is to drive down available water:

- **Dry in controlled conditions:** cool and moderate, with airflow. Drying itself cuts yeast-and-mould counts substantially[^sun2025-drying].
- **Cure and store dry.** Aim for a stable, low water activity. Curing around ~18 °C and ~50–55% RH is a defensible target[^alubeed2022-postharvest].
- **Glass beats plastic.** Sealed glass jars outperform bags for keeping microbes down and cannabinoids stable[^sun2025-drying].

## Why ‘looks fine’ isn't proof

Flower can carry dangerous fungi while looking, smelling and even _testing_ clean. Standard culture-based mould tests can miss some toxin-producing _Aspergillus_[^mckernan2016-micro], and contamination rates across the market are high and inconsistently regulated[^gwinn2023-mycotoxin].

> **KEY — Bottom line on safety**
>
> Prevention in the grow room is your real safety system. Lab testing is a backstop with real blind spots, not a guarantee. For vulnerable users, mouldy cannabis is a genuine health risk[^benedict2020-cdc], which is why clean genetics (see [tissue culture](tissue-culture.html)) and a clean room matter from day one.

## Troubleshooting

| You see… | Likely cause | Do this |
| --- | --- | --- |
| Grey, fluffy, crumbling bud interior | Botrytis bud rot | Bag, cut wide, remove from room, sanitise, drop RH + add airflow |
| White flour on leaf tops | Powdery mildew | Improve airflow and lower RH, remove worst leaves, treat early[^scott2021-pm] |
| Rot appears every run, late flower | Chronic high canopy humidity / dense plants | Bigger dehumidifier, defoliate, through-canopy airflow |
| Condensation at lights-off | Surfaces hitting dew point on the night drop | Soften the temperature drop, keep air moving |
| Mould in jars after cure | Stored too wet | Dry or cure to lower water activity, use sealed glass[^alubeed2022-postharvest] |

## Realistic expectations

> **KEY — What to remember**
>
> 1. Mould is a **recipe (humidity + still air + density + moisture)**. Remove an ingredient and you remove the risk.
> 2. It hides **inside** buds. By the time it's visible, spores are already spreading. Scout daily in late flower.
> 3. **Prevention is the only cure.** You cannot make rotted or mycotoxic flower safe after the fact[^sun2025-drying].
> 4. **Clean looks and passing tests aren't proof** of safety[^mckernan2016-micro].

Mould risk is downstream of your climate and airflow. Read the [systems guide](grow-room-systems.html) and [airflow](airflow-design.html) papers to fix the causes, not just the symptoms.

## References

[^punja-budrot-cjb]: Mahmoud M, BenRejeb I, Punja ZK, Buirs L, Jabaji S (2023). Understanding bud rot development, caused by Botrytis cinerea, on cannabis grown under greenhouse conditions. Botany / Can. J. Bot. 101(8). https://doi.org/10.1139/cjb-2022-0139 (peer-reviewed)
[^punja2025-budrot-epi]: Punja ZK, et al. (2025). The epidemiology and management of Botrytis cinerea causing bud rot on greenhouse-cultivated cannabis. Can. J. Plant Pathol. https://doi.org/10.1080/07060661.2025.2478250 (peer-reviewed)
[^scott2021-pm]: Scott C, Punja ZK (2021). Evaluation of disease management approaches for powdery mildew on Cannabis sativa L. Can. J. Plant Pathol. 43(3):394-412. https://doi.org/10.1080/07060661.2020.1836026 (peer-reviewed)
[^buirs2024-idm]: Buirs L, Punja ZK (2024). Integrated management of pathogens and microbes in Cannabis sativa L. under greenhouse conditions. Plants 13:786. https://doi.org/10.3390/plants13060786 (peer-reviewed)
[^mckernan2016-micro]: McKernan K, Spangler J, Helbert Y, et al. (2016). Metagenomic analysis of medicinal cannabis samples. F1000Research 5:2471. https://pmc.ncbi.nlm.nih.gov/articles/PMC5089129/ (peer-reviewed)
[^alubeed2022-postharvest]: AL Ubeed HMS, Wills RBH, Chandrapala J (2022). Post-harvest operations to generate high-quality medicinal cannabis products: a systematic review. Molecules 27:1719. https://doi.org/10.3390/molecules27051719 (peer-reviewed)
[^sun2025-drying]: (2025). Post-harvest drying and curing affect cannabinoid contents and microbial levels in industrial hemp (Cannabis sativa L.). Plants 14(3):414. https://doi.org/10.3390/plants14030414 (peer-reviewed)
[^benedict2020-cdc]: Benedict K, Thompson GR, Jackson BR (2020). Cannabis use and fungal infections in a commercially insured population, United States, 2016. Emerg. Infect. Dis. 26(6):1308-1310. https://doi.org/10.3201/eid2606.191570 (peer-reviewed)
[^gwinn2023-mycotoxin]: Gwinn KD, Leung MCK, Stephens AB, Punja ZK (2023). Fungal and mycotoxin contaminants in cannabis and hemp flowers: implications for consumer health. Front. Microbiol. 14:1278189. https://doi.org/10.3389/fmicb.2023.1278189 (peer-reviewed)
[^punja2019-pathogens]: Punja ZK, Collyer D, Scott C, Lung S, Holmes J, Sutton D (2019). Pathogens and molds affecting production and quality of Cannabis sativa L. Front. Plant Sci. 10:1120. https://pmc.ncbi.nlm.nih.gov/articles/PMC6811654/ (peer-reviewed)
