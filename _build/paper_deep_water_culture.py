# -*- coding: utf-8 -*-
"""Paper: deep water culture from first principles - oxygen, redox, iron and the reservoir."""
from components import (p, lead, ul, ol, callout, defterm, table, figure,
                        grid, card, chip, kv, steps, photo, photo_sequence)
import figs_lib as L
import figs_dwc as D

IMG = "assets/img/deep-water-culture"
GPT = "gpt-image-1"

SLUG = "deep-water-culture"
TITLE = "Deep water culture, from first principles"
EYEBROW = "Water culture · Root-zone oxygen"
SUB = ("Roots hanging in nutrient water have no substrate to hide behind. This paper builds the "
       "system from the physics up: how much oxygen the water can actually hold, why more bubbling "
       "makes iron uptake worse, what an ORP probe is really measuring, and how a commercial RDWC "
       "programme is put together.")
META = [("droplet", "Water culture"), ("image", "17 diagrams · 10 photos"),
        ("quote", "Evidence-linked · 40 sources"), ("clock", "~38 min read")]
RELATED = ["substrates-overview", "water-quality", "ph-management",
           "nutrient-mixing-athena", "one-steering-law"]

REF_IDS = [
    # oxygen: demand, thresholds, enrichment
    "dwc-drew-1997-hypoxia", "dwc-colmer-2010-ion-transport", "dwc-tan-2018-aquaporins",
    "dwc-roosta-2024-o2-nform", "dwc-nitu-2024-nft-oxygen", "dwc-qin-2025-do-enrichment",
    "dwc-nsele-2026-dwc-tomato",
    # physical chemistry
    "dwc-benson-krause-1984", "dwc-bok-2023-o2-solubility",
    # aeration paradox
    "dwc-langenfeld-2024-zero-discharge", "dwc-langenfeld-2025-agitation-iron",
    "dwc-bodenmiller-2017-aeration",
    # nanobubbles
    "dwc-ebina-2013-nanobubble", "dwc-wang-2024-mnb-microbiome", "dwc-mamun-2025-onb-health",
    "dwc-yang-2025-microbubble-ros", "dwc-takahashi-2021-nb-radicals", "dwc-chae-2023-nb-ros-null",
    # redox
    "dwc-stefansson-2005-redox", "dwc-suslow-2004-orp", "dwc-sholikah-2025-pt-electrode",
    # iron
    "dwc-ilyas-2025-fe-chelates", "dwc-klem-2021-eddha", "dwc-mirbolook-2023-fe-source",
    # biology
    "dwc-sutton-2006-pythium", "dwc-scott-2026-do-pythium", "dwc-kenderdine-2026-recirc",
    "dwc-lobanov-2022-plants-dictate", "dwc-canellas-2015-humic",
    "dwc-rashad-2024-biocontrol", "dwc-alattas-2024-pseudomonas",
    # oxidisers
    "dwc-eicher-sodo-2020-h2o2", "dwc-hendrickson-2022-h2o2",
    # temperature, nitrogen, feed
    "dwc-alrawahy-2019-rzt", "dwc-zhu-2021-nh4-no3",
    "dwc-hershkowitz-2025-p-ec", "dwc-caplan-2019-drought", "dwc-hassan-2024-silicon",
    # manufacturer
    "dwc-athena-rdwc-2024", "dwc-athena-proline",
]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

# 1 ------------------------------------------------------------------ intro
SECTIONS.append({"id": "intro", "kicker": "Start here", "title": "A reservoir doing four jobs at once",
  "blocks": [
    lead("In coco or rockwool the substrate is a buffer. It holds water, holds air, holds a charge, "
         "and quietly forgives the feed you got slightly wrong this morning. Deep water culture "
         "deletes that buffer. The roots hang in the nutrient solution itself, and the reservoir "
         "has to do every job the substrate used to do &mdash; simultaneously, continuously, with "
         "no margin."),
    p("That is the whole story of DWC in one sentence. Everything else in this paper is a "
      "consequence of it. The highest growth rates in soilless culture and the fastest crop "
      "failures in soilless culture come from the same property: there is nothing between your "
      "decision and the root. Done well the upside is real &mdash; reviews of deep-water-culture "
      "tomato report consistently better biomass accumulation, photosynthetic efficiency, root "
      "development and yield than soil or other hydroponic systems, attributed to the continuous "
      "supply of oxygenated, nutrient-rich solution" + _c("dwc-nsele-2026-dwc-tomato") + "."),
    figure(L.flow("What the reservoir has to do at the same time",
            [("Hold water", "the entire root system is submerged, permanently"),
             ("Hold oxygen", "no air-filled pores, so every mg of O2 arrives dissolved"),
             ("Hold the feed", "EC and pH with no substrate buffering the swing"),
             ("Hold the biology", "one shared water volume touches every plant")],
            note="Coco does the first three passively. In water culture all four are active, powered systems."), 1,
      "In a substrate these four functions are split between the medium, the drip line and the "
      "drain. In water culture they collapse into one volume of moving water, and any one of them "
      "failing takes the others with it."),
    photo(f"{IMG}/01-rdwc-room.jpg",
      "A commercial RDWC room. Every bucket is plumbed to the same loop, which means every bucket "
      "shares one EC, one pH, one temperature and one microbial population. That is the strength "
      "and the risk in a single image.", model=GPT),
    defterm("Deep water culture (DWC)",
      "Roots suspended directly in an aerated nutrient solution, with the crown held above the "
      "waterline by a net pot and inert media such as expanded clay. A single bucket is DWC. "
      "Buckets plumbed to a shared control reservoir with a circulation pump is "
      "<strong>RDWC</strong>, recirculating deep water culture."),
    figure(D.bucket_xsection(), 2,
      "One site in section. Note the two volumes that are not the same number: the "
      "<strong>operating volume</strong> you dose against, and the <strong>left-over volume</strong> "
      "below the bulkhead that a drain cannot reach." + _c("dwc-athena-rdwc-2024")),
    photo(f"{IMG}/02-bucket-open.jpg",
      "The same thing in the flesh: net pot seated in the lid, expanded clay holding the crown "
      "clear of the water, and the root curtain hanging free in solution. There is no substrate "
      "between the feed and the root.", model=GPT),
    defterm("Control bucket",
      "A plant-free vessel in an RDWC loop that carries the pump, the top-off float, the probes "
      "and the heater or chiller. Every reading and every dose happens here, so no plant site is "
      "ever the measurement point." + _c("dwc-athena-rdwc-2024")),
    callout("key", "The three numbers this paper is built around",
      ul(["<strong>Dissolved oxygen</strong> &mdash; how much O<sub>2</sub> is in the water, in mg/L. "
          "Sets the ceiling on root respiration.",
          "<strong>Solution temperature</strong> &mdash; sets both how much oxygen the water "
          "<em>can</em> hold and how fast the roots and microbes <em>consume</em> it. The master dial.",
          "<strong>ORP</strong> &mdash; oxidation-reduction potential, in millivolts. The most "
          "misread number in hydroponics, and the one this paper spends the most time on."], "tight")),
    callout("note", "Who this is for",
      p("Anyone running or considering water culture, and anyone who has looked at an ORP reading "
        "and not known what to do about it. It assumes you already know what EC and pH are. If you "
        "do not, read the pH and water-quality papers first. Cannabis is the worked example, but "
        "the physics applies to any crop.")),
  ]})

# 2 ------------------------------------------------------------- oxygen budget
SECTIONS.append({"id": "oxygen-budget", "kicker": "Physics", "title": "How much oxygen water can actually hold",
  "blocks": [
    p("Start with the constraint nobody can negotiate. Oxygen is barely soluble in water. At 20 &deg;C "
      "under normal air at sea level, water holds about <strong>9.1 mg/L</strong> of dissolved "
      "oxygen at equilibrium" + _c("dwc-benson-krause-1984") + ". Air itself, by comparison, is "
      "about 280 mg/L of oxygen. Water at saturation carries roughly one-thirtieth of the oxygen "
      "that the same volume of air carries. That is the number a submerged root has to live on."),
    defterm("Saturation",
      "The concentration a gas reaches in a liquid when the liquid is in equilibrium with the gas "
      "above it. It is set by Henry's law: dissolved concentration is proportional to the partial "
      "pressure of that gas in the gas phase." + _c("dwc-bok-2023-o2-solubility")),
    figure(L.line("Air-saturated dissolved oxygen falls as water warms",
            [("10", 11.29), ("14", 10.31), ("18", 9.47), ("20", 9.09), ("22", 8.74),
             ("25", 8.26), ("28", 7.83), ("30", 7.56)],
            ["10 C", "14 C", "18 C", "20 C", "22 C", "25 C", "28 C", "30 C"],
            ylab="mg/L", ymin=6, ymax=12,
            note="Fresh water, 1 atm, in equilibrium with air. Standard solubility tables."), 3,
      "Warming the reservoir from 18 to 28 &deg;C removes about 17% of the oxygen the water can hold, "
      "before a single root has breathed any of it." + _c("dwc-benson-krause-1984")),
    callout("key", "Warming a reservoir is doubly bad",
      p("Solubility falls roughly 1.7% per &deg;C near 20 &deg;C. Over the same 10 &deg;C, biological "
        "oxygen demand roughly <em>doubles</em> &mdash; root and microbial respiration follow a "
        "Q<sub>10</sub> near 2. Supply down about a sixth, demand up about double: the ratio of "
        "available oxygen to oxygen demanded falls by roughly a factor of two and a half. This is why "
        "reservoir temperature, not aeration hardware, is the first thing to check when a system "
        "starts failing.")),
    p("Now the part that confuses people. Growers running an oxygen concentrator through a fine "
      "diffuser routinely report 15&ndash;25 mg/L, and then worry that they are dangerously "
      "supersaturated. Both halves of the following sentence are true, and holding both at once is "
      "the key to understanding the reading."),
    grid([
      card("Relative to air: yes, supersaturated",
           p("At 22 &deg;C air-saturated water holds about 8.7 mg/L. A reading of 20 mg/L is about "
             "<strong>2.3&times; air saturation</strong>. If you switched the gas off and left the "
             "water open to the room, it would slowly out-gas back toward 8.7."), tag="2.3&times;"),
      card("Relative to your gas: not saturated at all",
           p("A pressure-swing concentrator delivers roughly 90&ndash;95% oxygen. Henry's law scales "
             "with partial pressure, so at 22 &deg;C that gas could push water to roughly "
             "<strong>38 mg/L</strong> at equilibrium. Your 20 mg/L is about half of that. While the "
             "gas is flowing, nothing is straining to escape."), tag="~52%"),
    ], cols=2),
    callout("note", "Why that distinction matters operationally",
      p("A solution that is supersaturated relative to <em>air</em> but undersaturated relative to "
        "the <em>gas being injected</em> is stable while the gas flows and decays gently when it "
        "stops. It does not spontaneously nucleate bubbles on root surfaces. The failure mode to "
        "actually worry about is not gas embolism, it is the pump stopping &mdash; at which point "
        "you are on a decay curve toward 8.7 mg/L with a root mass sized for 20.")),
    p("The other lever is bubble size. Conventional air stones make bubbles of a few millimetres "
      "that rise and burst in seconds. Nanobubbles &mdash; below roughly 200 nm &mdash; carry a "
      "negatively charged surface that resists coalescence and a high internal pressure that keeps "
      "gas dissolving. In the original characterisation work they remained measurable in water for "
      "about <strong>70 days</strong>" + _c("dwc-ebina-2013-nanobubble") + ". That is a genuinely "
      "different transport regime, not a marketing gradient: the gas keeps dissolving long after "
      "the visible bubbling has stopped."),
    figure(D.bubble_scale(), 4,
      "Bubble size is not a quality gradient, it is three different physical regimes. Only the "
      "nano regime delivers gas without delivering a rising plume &mdash; which, as the next "
      "section shows, is the whole problem with coarse aeration." + _c("dwc-ebina-2013-nanobubble")),
    photo(f"{IMG}/08-nanobubble.jpg",
      "Left: a coarse air stone, large bubbles, visible turbulent plume. Right: nanobubble water, "
      "an even opalescent haze with no rising column. Same gas, entirely different mechanical "
      "consequence for the root zone.", model=GPT),
  ]})

# 3 ------------------------------------------------------------ how much is enough
SECTIONS.append({"id": "how-much", "kicker": "Targets", "title": "How much oxygen the plant actually needs",
  "blocks": [
    p("The literature is unusually consistent about the bottom of the range and unusually messy "
      "about the top. Both facts are useful."),
    p("At the bottom: in bell pepper grown in floating culture, growth and photosynthesis were "
      "measurably impaired below about <strong>3.8 mg/L</strong> on ammonium nutrition and below "
      "<strong>5.3 mg/L</strong> on nitrate nutrition, with the authors recommending those as hard "
      "floors" + _c("dwc-roosta-2024-o2-nform") + ". That nitrogen-form split is not a curiosity: "
      "nitrate assimilation is itself energetically expensive, so a nitrate-fed root has a higher "
      "oxygen bill than an ammonium-fed one."),
    figure(L.bars("Dissolved-oxygen levels used across the hydroponic literature",
            [("Hypoxic", 2.0), ("NH4 floor", 3.8), ("NO3 floor", 5.3),
             ("Air sat. 20 C", 9.1), ("NFT enriched", 8.8), ("DWC enriched", 15.0),
             ("O2 concentrator", 20.0)], unit=" mg/L",
            note="Floors are experimentally derived; the top two are what enrichment systems deliver, not requirements.",
            maxv=24), 5,
      "The gap between the ~5 mg/L physiological floor and the 15&ndash;20 mg/L that enrichment "
      "hardware delivers is where all the argument lives. Above roughly 8&ndash;10 mg/L the "
      "evidence for further benefit becomes crop-specific and cost-sensitive." +
      _c("dwc-roosta-2024-o2-nform") + _c("dwc-nitu-2024-nft-oxygen") + _c("dwc-qin-2025-do-enrichment")),
    p("At the top, the honest answer is that returns diminish and then stop. Raising NFT lettuce "
      "from about 7 mg/L to about 8.5&ndash;9 mg/L produced large gains &mdash; fresh mass up to "
      "110% higher in one cultivar, root mass up 78%" + _c("dwc-nitu-2024-nft-oxygen") + ". But a "
      "deep-water-culture trial that ran controlled enrichment at 10, 15 and 20 mg/L found the "
      "response was entirely crop-specific: arugula gained 63&ndash;191% above 15 mg/L, kale gained "
      "nothing at any level, and the enrichment carried a <strong>140% higher electricity cost</strong>. "
      "Only arugula at 20 mg/L returned enough to pay for the energy" + _c("dwc-qin-2025-do-enrichment") + "."),
    figure(L.zones("The dissolved-oxygen operating band", 0, 22,
            [(0, 3.8, L.REDL, "Hypoxic: root damage"),
             (3.8, 6.0, L.AMBL, "Marginal"),
             (6.0, 10.0, L.GL, "Good: air-sat and a bit over"),
             (10.0, 22.0, L.BLUL, "Enriched: crop-specific, pay for it")], unit=" mg/L",
            note="Below 3.8 you are damaging roots. Above ~10 you are buying yield you may not get."), 6,
      "Getting from hypoxic to comfortable is the single highest-return move in water culture. "
      "Getting from comfortable to enriched is an economics question, not a horticulture one."),
    callout("warn", "Hypoxia damages the plant before you can see it in the roots",
      p("Low root-zone oxygen does not begin with brown roots. It begins with an energy deficit. "
        "The root cortex may still get enough O<sub>2</sub> to absorb nutrients while the stele "
        "&mdash; the central tissue that loads nutrients into the xylem for transport to the shoot "
        "&mdash; goes hypoxic and its H<sup>+</sup>-ATPases stall" + _c("dwc-colmer-2010-ion-transport") +
        ". The plant takes ions up and cannot ship them. Separately, hypoxia closes aquaporins and "
        "triggers stomatal closure, so water transport falls too" + _c("dwc-tan-2018-aquaporins") +
        ". You see a plant that looks nutrient-deficient and slightly wilty with a perfectly good "
        "feed in the tank. Root browning and lysis come later" + _c("dwc-drew-1997-hypoxia") + ".")),
    callout("tip", "The diagnostic that costs nothing",
      p("A deficiency pattern that does not respond to correcting the feed, in a system whose EC and "
        "pH are on target, should send you to the DO meter and the thermometer before it sends you "
        "to the nutrient shelf.")),
  ]})

# 4 --------------------------------------------------------- the aeration paradox
SECTIONS.append({"id": "aeration-paradox", "kicker": "The counter-intuitive part", "title": "More bubbling is not more better",
  "blocks": [
    lead("This is the section most likely to change how you run your system. Aeration delivers "
         "oxygen, which is good. Aeration also delivers <em>agitation</em>, which is not. Past a "
         "modest rate, the agitation costs you more than the oxygen buys."),
    p("The clearest demonstration comes from deep-flow hydroponics run at aeration rates from 0 to "
      "2 L/min. Gentle solution movement &mdash; not violent, gentle &mdash; dramatically reduced "
      "iron uptake and induced chlorosis in sunflower and corn. The same nutrient solution at the "
      "same pH in a peat-based medium produced ample iron and chlorophyll. Tomato was largely "
      "unaffected; species differ" + _c("dwc-langenfeld-2025-agitation-iron") + "."),
    callout("key", "The mechanism: you are stripping the rhizosphere",
      p("A root does not simply absorb whatever is in the bulk solution. It builds a thin unstirred "
        "boundary layer around itself and chemically engineers it &mdash; pumping out protons to "
        "acidify it, exuding reductants and chelators to make iron available. That microenvironment "
        "is <em>the plant's own nutrient-acquisition machinery</em>. Bubbling stirs it away. Turning "
        "the aeration up does not just add oxygen; it demolishes the boundary layer the root built "
        "to feed itself." + _c("dwc-langenfeld-2025-agitation-iron"))),
    figure(D.boundary_layer(), 7,
      "The single most useful picture in this paper. Left: gentle flow, the unstirred layer holds, "
      "the root has acidified it and iron is available. Right: the same root in the same solution "
      "with the air turned up &mdash; the layer is gone, and the root is now negotiating with bulk "
      "chemistry it has no way to modify." + _c("dwc-langenfeld-2025-agitation-iron")),
    p("There is a second, blunter mechanism. Aggressive aeration strips dissolved CO<sub>2</sub> out "
      "of the solution. Carbonic acid is a real contributor to solution pH, so venting it drives pH "
      "up. In a deep-water-culture aquaponics trial the heavily aerated beds yielded "
      "<strong>29% less</strong> than unaerated controls at harvest &mdash; and dissolved oxygen "
      "never dropped below 5 mg/L in any treatment, so oxygen was never the limiting factor. The "
      "authors attributed the loss to the pH shift that came with the aeration" +
      _c("dwc-bodenmiller-2017-aeration") + "."),
    p("So what rate is right? Two independent sources converge on almost exactly the same number, "
      "which is the most reassuring thing in this paper."),
    grid([
      card("From the research",
           p("A zero-discharge hydroponic management system holds DO near saturation with "
             "<strong>gentle aeration at about 100 mL&#183;min<sup>-1</sup> per litre</strong> of "
             "solution, in a bed at least 20 cm deep. Ample depth stabilises concentrations and "
             "reduces root density; gentle aeration improves uniformity without destroying the "
             "rhizosphere." + _c("dwc-langenfeld-2024-zero-discharge")), tag="100 mL/min/L"),
      card("From the manufacturer",
           p("A commercial RDWC procedure specifies <strong>one 5 &times; 5 cm medium round air "
             "stone per 30 L bucket</strong>, positioned at the bottom, about 2.5 cm from the wall, "
             "and explicitly <em>never</em> directly under the net pot &mdash; because &lsquo;too "
             "much turbidity can cause severe damage to new roots&rsquo;." + _c("dwc-athena-rdwc-2024")),
           tag="1 stone / 30 L"),
    ], cols=2),
    callout("note", "Check the arithmetic yourself",
      p("A 30 L bucket at 100 mL&#183;min<sup>-1</sup>&#183;L<sup>-1</sup> wants about 3 L/min of "
        "air. Reckoned on the operating volume of roughly 19 L rather than the nominal bucket size, "
        "it wants about 1.9 L/min. A single medium round air stone at typical manifold pressure "
        "flows somewhere in the 2&ndash;4 L/min range. The peer-reviewed number and the commercial "
        "spec land on the same hardware. A researcher measuring iron chlorosis and a commercial "
        "grower watching root damage found the same limit from opposite directions.")),
    figure(L.zones("Aeration rate: the window is narrower than most people run", 0, 400,
            [(0, 40, L.REDL, "Too little: hypoxia"),
             (40, 160, L.GL, "The window"),
             (160, 400, L.AMBL, "Too much: rhizosphere stripped, CO2 vented, pH drifts up")],
            unit="",
            note="Air flow in mL per minute per litre of solution. Centred on ~100. Most hobby DWC builds sit far right."), 8,
      "Growers instinctively treat aeration as a safety margin and over-provision it. The evidence "
      "says the top of the range has its own failure mode, and it presents as an iron deficiency "
      "you cannot feed your way out of."),
    callout("tip", "Placement is a control variable, not a detail",
      p("Air stones at the bottom of the bucket and offset from the wall let the column rise past "
        "the root mass rather than through it. A stone directly under the net pot drives the "
        "highest-shear part of the plume straight through the youngest, most fragile root tips. "
        "Same air volume, completely different outcome." + _c("dwc-athena-rdwc-2024"))),
    figure(D.airstone_placement(), 9,
      "Identical hardware, identical air volume, opposite result. The left bucket aims the plume "
      "through the root mass; the right one lets it rise alongside." + _c("dwc-athena-rdwc-2024")),
    photo(f"{IMG}/06-airstone.jpg",
      "What you are aiming for underwater: a fine, even column rising near the wall and past the "
      "roots, not a rolling boil through the middle of them.", model=GPT),
    p("This is also the strongest argument for nanobubble generation over conventional stones. "
      "Nanobubbles dissolve gas without producing a rising plume, which decouples oxygen delivery "
      "from mechanical agitation &mdash; the two things a coarse air stone forces you to buy "
      "together. Micro/nanobubble-aerated irrigation at 15 and 30 mg/L produced larger root volume, "
      "richer rhizosphere bacterial communities and higher yields than at 5 mg/L" +
      _c("dwc-wang-2024-mnb-microbiome") + ", and reviews of the technology in controlled "
      "environment agriculture frame it primarily as a way to keep the root zone aerobic enough "
      "for beneficial microbes to function" + _c("dwc-mamun-2025-onb-health") + "."),
  ]})

# 5 -------------------------------------------------------------------- ORP
SECTIONS.append({"id": "orp", "kicker": "The misread number", "title": "What an ORP probe is actually telling you",
  "blocks": [
    lead("Oxidation-reduction potential is the most commonly misinterpreted measurement in water "
         "culture. It is worth getting right, because the correct interpretation changes the "
         "action you take."),
    defterm("ORP / redox potential",
      "The electrical potential, in millivolts, of an inert platinum electrode immersed in the "
      "solution, measured against a reference electrode. It reflects the balance of oxidising and "
      "reducing species &mdash; the solution's overall tendency to accept or donate electrons."),
    p("Here is where most people go wrong, and the correction is not what you would guess. "
      "<strong>Raising dissolved oxygen does reliably raise ORP &mdash; but almost none of that rise "
      "is oxygen acting on the electrode.</strong> Both halves matter. Growers who are told &lsquo;ORP "
      "is not an oxygen measurement&rsquo; and then watch their ORP jump 200 mV when they switch to an "
      "oxygen concentrator quite reasonably conclude they have been misinformed. They have not; the "
      "causal chain just runs through the water rather than through the electrode."),
    p("The O<sub>2</sub>/H<sub>2</sub>O couple has a large standard potential on paper but exchanges "
      "electrons extremely slowly at a platinum surface. In the language of electrochemistry it has a "
      "very low exchange current density: it is kinetically irreversible. Two things follow. The "
      "electrode never actually reaches oxygen equilibrium &mdash; at pH 5.8 a fully equilibrated "
      "oxygen electrode would sit near <strong>690 mV</strong> against a silver/silver-chloride "
      "reference, and real reservoirs read hundreds of millivolts below that. And the <em>direct</em> "
      "response to oxygen concentration is small enough that you can calculate it on the back of an "
      "envelope."),
    callout("key", "Do the arithmetic before you attribute an ORP change to oxygen",
      p("The Nernst slope for a four-electron couple is 59.16 &divide; 4 = <strong>14.8 mV per decade</strong> "
        "of oxygen partial pressure. Going from air (<em>p</em>O<sub>2</sub> 0.21 atm) to a "
        "concentrator at roughly 93% O<sub>2</sub> is 0.65 of a decade. Maximum direct shift: "
        "<strong>about 10 mV</strong>. If your ORP moved by more than a few tens of millivolts, "
        "oxygen did not do it directly. Something in the water changed &mdash; and that is worth "
        "knowing, because it is usually the more important fact.")),
    callout("evidence", "A field case: 220-260 mV on air, about 480 mV on an oxygen concentrator",
      p("A grower running a nanobubbler reported ORP sitting at <strong>220-260 mV</strong> on plain "
        "air. The system mostly worked, but new reservoirs with freshly transplanted clones brought "
        "recurring <em>Pythium</em> and cyanobacteria, persistent biofilm, and one detail that gives "
        "the whole game away: <em>the roots stayed up in the clay pebbles and would not grow down "
        "into the water.</em> After switching the same system to an oxygen concentrator, ORP settled "
        "around <strong>480 mV</strong>, biofilm essentially stopped, and the root-avoidance "
        "resolved.")
      + p("That is a ~240 mV shift where the arithmetic above allows about 10. The other ~230 mV is "
          "not oxygen on the electrode &mdash; it is the reservoir itself having changed. At 220-260 mV "
          "the water was carrying a real load of reduced organic carbon and supporting active "
          "anaerobic and micro-aerophilic metabolism. Those reduced species <em>are</em> fast, "
          "well-poised couples, and they were holding the electrode down. Flooding the system with "
          "oxygen burned that load out and collapsed the population producing it. Remove the "
          "reductants and the electrode floats up to a far higher mixed potential.")
      + p("So the rise is real, it is useful, and it is worth acting on. It simply is not a "
          "measurement of oxygen &mdash; it is the cleanliness readout responding to a cleanliness "
          "change that oxygen caused. Which is exactly what ORP is for.")),
    callout("note", "A second pathway, genuinely unsettled",
      p("Gas-liquid interfaces at micro and nano scale have been shown to generate hydroxyl radicals "
        "with no catalyst at all, driven by hydroxide enrichment and the interfacial electric field" +
        _c("dwc-yang-2025-microbubble-ros") + ", and spin-trap work has detected radical signatures "
        "in microbubble-treated water months after treatment" + _c("dwc-takahashi-2021-nb-radicals") +
        ". Against that, a careful study found no detectable hydroxyl radical from oxygen nanobubbles "
        "under ambient conditions, and showed that a widely used fluorescent probe returns a false "
        "positive because the bubble surface is proton-rich" + _c("dwc-chae-2023-nb-ros-null") + ". "
        "Treat any radical contribution as unproven and second-order. The reductant-removal mechanism "
        "above is sufficient to explain what growers actually observe, and it does not require the "
        "chemistry to be exotic.")),
    callout("key", "What a Pt electrode reads in a dilute solution is a mixed potential",
      p("A rigorous study of natural waters calculated the redox potential separately for six "
        "different couples in the same water. They disagreed by up to <strong>1200 mV</strong>. The "
        "authors concluded that in dilute waters with low concentrations of redox-active species, "
        "the measured platinum potential is a mixed potential of limited quantitative meaning, and "
        "cannot be used to model speciation" + _c("dwc-stefansson-2005-redox") + ". A hydroponic "
        "reservoir is exactly such a water.")),
    figure(D.orp_mixed_potential(), 10,
      "Every redox-active species in the reservoir pulls the electrode toward its own potential, "
      "weighted by how fast it exchanges electrons. The meter shows the compromise. Dissolved "
      "oxygen is the weakest voice in the room." + _c("dwc-stefansson-2005-redox")),
    figure(L.hbars("What actually moves ORP in a nutrient reservoir",
            [("Hypochlorous acid dose", 100), ("Hydrogen peroxide dose", 85),
             ("Oxygen - INDIRECT", 78), ("Iron redox state", 55),
             ("Reduced organic load", 45), ("Microbial respiration", 40),
             ("pH (59 mV per unit)", 35), ("Oxygen - DIRECT on Pt", 8)], unit="",
            note="Relative influence on the reading. Oxygen appears twice, and the two entries are not the same thing."), 11,
      "The distinction that resolves most ORP arguments. Oxygen acting <em>directly</em> on the "
      "electrode is the weakest effect on the chart, capped near 10 mV. Oxygen acting "
      "<em>indirectly</em> &mdash; by oxidising out the reduced organic load and collapsing the "
      "anaerobic population that was holding the reading down &mdash; is one of the strongest, and "
      "is what growers actually observe." + _c("dwc-suslow-2004-orp") + _c("dwc-stefansson-2005-redox")),
    p("The second surprise is that <strong>ORP is meaningless without the pH beside it</strong>. Most "
      "environmentally relevant redox couples consume protons as they accept electrons. The Nernst "
      "equation makes the consequence exact: at 25 &deg;C the potential shifts by about "
      "<strong>59 mV per pH unit</strong>, falling as pH rises."),
    callout("note", "A worked example from a real grower thread",
      p("A grower reported pH moving from 6.0 to 5.8 across a day while ORP went from 476 to 482 mV. "
        "Is that a real change in the chemistry? Run the number: a drop of 0.2 pH units should raise "
        "the potential of a proton-coupled couple by about 0.2 &times; 59 = <strong>12 mV</strong>. "
        "Observed was +6 mV &mdash; same sign, roughly half the magnitude. In other words the "
        "&lsquo;ORP climb&rsquo; was largely the pH change being reported back, and if anything the "
        "underlying redox chemistry drifted slightly <em>downward</em>. Logging ORP without logging "
        "pH alongside it produces exactly this kind of phantom trend.")),
    p("The third surprise explains a common frustration: probes that take hours to settle in the "
      "reservoir but minutes in calibration fluid."),
    defterm("Poise",
      "A solution is well <strong>poised</strong> when it contains a redox couple at high enough "
      "concentration, exchanging electrons fast enough, to drive the electrode to its potential "
      "quickly and hold it there. A poorly poised solution has no such couple, so the electrode "
      "drifts for hours toward an ill-defined mixed potential."),
    callout("tip", "Why calibration standards settle in two minutes and your reservoir takes six hours",
      p("ORP standards such as ZoBell's solution or quinhydrone are <em>engineered</em> to be "
        "strongly poised &mdash; they contain a fast, reversible couple at millimolar concentration "
        "precisely so the electrode locks on. A clean, well-oxygenated, low-organic nutrient "
        "solution is the opposite: chemically it is close to a blank. A probe that takes hours to "
        "settle after being cycled or re-immersed is not faulty. It is correctly reporting that "
        "your solution has almost nothing redox-active in it, which for a mineral hydroponic system "
        "is good news." + _c("dwc-stefansson-2005-redox"))),
    p("None of which means ORP is useless. It means ORP is a <strong>sanitiser and cleanliness "
      "gauge</strong>, and used that way it is genuinely valuable. It is the established control "
      "variable for hypochlorous-acid disinfection in produce handling, where it tracks free "
      "available chlorine far more responsively than a concentration test" + _c("dwc-suslow-2004-orp") + "."),
    p("A commercial RDWC procedure treats it exactly this way, and defines three zones with a "
      "sensory cross-check for each" + _c("dwc-athena-rdwc-2024") + ":"),
    table(["Zone", "What is happening", "Smell", "Consequence"], [
      ["<strong>Anaerobic</strong>", "ORP has fallen; reduced organics and anaerobic metabolism dominate. "
       "A field report of a persistently biofilm-prone air-stone system put this at <strong>220-260 mV</strong>",
       "Putrid", "Pathogen growth, root rot, roots refusing to enter the water"],
      ["<strong>Safe</strong>", "Clean water, oxidiser present but not accumulating",
       "Fresh bean sprouts", "White roots, normal uptake"],
      ["<strong>ORP shock</strong>", "Oxidiser over-dosed; highly oxidised environment",
       "Chlorine", "Root's ability to exchange nutrients is impaired"],
    ], cls="compact", caption="The three ORP zones and their sensory signatures. Note that the smell "
      "test is often faster and more reliable than the probe, and requires no calibration."),
    callout("warn", "ORP shock presents as a nutrient deficiency",
      p("The manufacturer's own warning is explicit: hypochlorous acid is safe to plant tissue, but "
        "<em>overuse in an RDWC system creates a highly oxidised environment that reduces nutrient "
        "uptake</em>, and it &lsquo;appears as a nutrient deficiency &mdash; yellowing or dry, "
        "crusty foliage&rsquo;. RDWC needs much lower ORP than other methods because of the extended "
        "contact time and the sheer volume of solution touching root tissue" + _c("dwc-athena-rdwc-2024") +
        ". Two different root-zone faults &mdash; hypoxia and over-oxidation &mdash; both present as "
        "leaf yellowing. Guessing between them costs you a crop.")),
    grid([
      card("If you dose no chemical oxidiser",
           p("A high, stable ORP mostly means your solution is clean and free of reduced organic "
             "load. There is no oxidiser present to shock anything, so a high number is not a "
             "warning &mdash; read it as a hygiene indicator. It is the <em>low</em> end that should "
             "worry you: a reading that sits low and drifts lower, with no oxidiser in the system, "
             "is reporting an accumulating reduced load and a reservoir heading anaerobic.")),
      card("If you dose hypochlorous or peroxide",
           p("ORP is now tracking your oxidiser residual and the manufacturer's shock zone is a real "
             "risk. This is when the number needs an upper limit, a logged pH beside it, and a "
             "reduction in dose rather than an addition of anything.")),
    ], cols=2),
    callout("tip", "Probe placement: isolate it from the bubble storm",
      p("A probe sitting in an active bubble plume reads the bubbles as much as the water, which is "
        "the usual explanation for a DO reading that swings between 15 and 25 mg/L. Mount probes in "
        "a calm, flow-through pocket &mdash; a perforated bottle or a small stilling well fed by "
        "circulation but shielded from the air stone. Biofilm growing on the electrode surface "
        "itself shifts a platinum reading by hundreds of millivolts" + _c("dwc-sholikah-2025-pt-electrode") +
        ", so probe cleaning is a scheduled task, not a troubleshooting step.")),
    photo(f"{IMG}/10-probe-reading.jpg",
      "Calibration is not optional maintenance in water culture, it is the difference between a "
      "diagnosis and a guess. A drifting ORP probe and a fouled ORP probe look identical on the "
      "display.", model=GPT),
  ]})

# 6 ------------------------------------------------------------------- iron
SECTIONS.append({"id": "iron", "kicker": "Chemistry", "title": "Iron, chelates, and the chlorosis you cannot feed away",
  "blocks": [
    p("Iron is the element water culture punishes you over. It is required in large amounts relative "
      "to other micronutrients, it is almost insoluble in oxygenated water at anything above mildly "
      "acidic pH, and it only stays available because we wrap it in a chelate."),
    defterm("Chelate",
      "An organic molecule that grips a metal ion in multiple places at once, holding it in solution "
      "and stopping it precipitating or reacting. Fertiliser iron is nearly always supplied as a "
      "chelate: Fe-EDTA, Fe-DTPA or Fe-EDDHA."),
    p("The three common chelates are not interchangeable. They differ in how high a pH they can hold "
      "iron at, and in how well they resist having their iron displaced by competing metals."),
    table(["Chelate", "Practical pH ceiling", "Behaviour", "Cost"], [
      ["<strong>Fe-EDTA</strong>", "~6.0&ndash;6.5",
       "Becomes unstable above pH 6.5; iron is displaced and forms insoluble FePO<sub>4</sub> and "
       "Fe(OH)<sub>3</sub>. Also competes with Cu, Zn and Mn for the ligand" + _c("dwc-ilyas-2025-fe-chelates"),
       "Lowest"],
      ["<strong>Fe-DTPA</strong>", "~7.0&ndash;7.5",
       "A meaningful margin above EDTA, and the usual choice when pH cannot be held tightly or when "
       "conditions are oxidising", "Middle"],
      ["<strong>Fe-EDDHA</strong>", "~9.0+",
       "Holds iron under genuinely alkaline conditions; stability is well characterised across pH "
       "and over time" + _c("dwc-klem-2021-eddha") + ". Stains solutions dark red", "Highest"],
    ], caption="Working pH ceilings for the three fertiliser iron chelates. The ceiling is not a "
      "cliff &mdash; degradation is progressive and time-dependent."),
    figure(L.zones("Where each iron chelate still holds its iron", 3.0, 9.5,
            [(3.0, 6.5, L.AMBL, "Fe-EDTA"), (6.5, 7.5, L.GL, "DTPA territory"),
             (7.5, 9.5, L.BLUL, "EDDHA only")], unit=" pH",
            note="Typical RDWC runs pH 5.8-6.3, which sits right at the top of the EDTA band."), 12,
      "A recirculating system that drifts to pH 6.5 has not left the range plants like, but it has "
      "left the range Fe-EDTA is comfortable in." + _c("dwc-ilyas-2025-fe-chelates")),
    callout("note", "What a commercial line actually does about this",
      p("One widely used mineral programme splits the iron between products: the base product "
        "supplies iron as <strong>Fe-EDTA</strong> alongside calcium nitrate and the EDTA-chelated "
        "micronutrients, while the bloom product supplies iron as <strong>Fe-DTPA</strong>" +
        _c("dwc-athena-proline") + ". Read against the pH schedule &mdash; which starts around "
        "6.2&ndash;6.3 and steps down to 5.8 through flower" + _c("dwc-athena-rdwc-2024") + " &mdash; "
        "that is a sensible hedge: EDTA does the cheap work in the acid part of the range, DTPA "
        "provides margin for the early, higher-pH part of the run and for any drift.")),
    callout("warn", "Two different causes, one symptom",
      p("Interveinal chlorosis in new growth &mdash; yellow between green veins on the youngest "
        "leaves &mdash; is the classic iron signature. In water culture it has at least two causes "
        "that call for opposite actions:"
        + ul(["<strong>Chelate failure</strong> &mdash; pH has drifted above what your chelate holds. "
              "Fix the pH, or move to a stronger chelate.",
              "<strong>Rhizosphere stripping</strong> &mdash; aeration is agitating away the boundary "
              "layer the root uses to acquire iron" + _c("dwc-langenfeld-2025-agitation-iron") +
              ". Turn the air <em>down</em>."], "tight")
        + "<p>Adding more iron fixes neither, and in the second case makes the underlying "
          "mismanagement harder to see.</p>")),
    photo(f"{IMG}/05-chlorosis.jpg",
      "Interveinal chlorosis on new growth: pale blade, veins still dark green, older leaves below "
      "unaffected. The pattern tells you it is iron. It does not tell you whether the cause is pH "
      "or aeration &mdash; and those call for opposite corrections.", model=GPT),
    p("Research into alternative iron sources continues &mdash; Schiff-base Fe(II) complexes stable "
      "at alkaline pH have outperformed both Fe-EDTA and Fe-EDDHA on root and shoot dry weight in "
      "maize" + _c("dwc-mirbolook-2023-fe-source") + " &mdash; but none of it is commercially "
      "relevant yet. For now the lever is pH control and chelate selection."),
  ]})

# 7 ---------------------------------------------------------------- organics
SECTIONS.append({"id": "organics", "kicker": "The live-reservoir argument", "title": "Organic inputs in a water reservoir",
  "blocks": [
    p("Ask whether to run kelp, fulvic acid or microbial inoculants in DWC and you will get two "
      "confident, opposite answers. Both camps are describing real experience. The disagreement is "
      "about which constraint binds in <em>their</em> system."),
    callout("key", "The mechanism both sides are arguing about",
      p("Every gram of reduced organic carbon you add to a reservoir is food for heterotrophic "
        "bacteria. Those bacteria multiply and respire, and respiration consumes dissolved oxygen. "
        "In water-treatment language you have added <strong>biochemical oxygen demand</strong>. "
        "You are now spending part of your aeration budget on feeding microbes rather than roots, "
        "and the organic load will also pull ORP down as reduced compounds accumulate.")),
    p("That is the case against. It is a real mechanism and it is why the standard advice for "
      "mineral hydroponics is to keep the solution clean. A commercial RDWC line goes further and "
      "explicitly dose-schedules a hypochlorous-acid product throughout the run precisely to keep "
      "organic load from accumulating, and warns that lines previously used with organic inputs may "
      "need repeated cleaning cycles to clear organic particulates" + _c("dwc-athena-rdwc-2024") + "."),
    p("Now the case for, which deserves a fair hearing. Growers running high dissolved oxygen &mdash; "
      "particularly nanobubble systems holding 15&ndash;20 mg/L &mdash; report running fulvic acid "
      "and biological inputs successfully, with no root disease. That is coherent: BOD is a "
      "<em>rate</em> problem, and if your oxygen supply rate is two to three times what a "
      "conventional air stone delivers, you can carry an organic load that would suffocate a "
      "conventional system. Humic and fulvic substances have well-documented biostimulant effects on "
      "lateral root growth and nutrient-use efficiency" + _c("dwc-canellas-2015-humic") + ", and "
      "reviews of oxygenated nanobubble technology explicitly frame high DO as the enabling "
      "condition for beneficial microbes to function in the root zone" + _c("dwc-mamun-2025-onb-health") + "."),
    grid([
      card("What is actually true",
           p("The microbial community in a recirculating system is not a threat by default. In "
             "deep-water-culture lettuce run over five reuse cycles, bacterial communities shifted "
             "significantly between cycles and some correlated with plant-defence gene expression "
             "&mdash; the authors argue that solution communities which activate plant defences are "
             "a promising route to chemical-free Pythium suppression" + _c("dwc-kenderdine-2026-recirc") + ".")),
      card("And what is over-claimed",
           p("Plants exert a stronger selective influence on their own rhizosphere than the water "
             "column does. In a comparison across hydroponic and aquaponic sources, root community "
             "composition clustered by plant, not by what was dosed upstream" +
             _c("dwc-lobanov-2022-plants-dictate") + ". You have less control over the root "
             "microbiome than the product labels imply.")),
    ], cols=2),
    callout("tip", "How to decide, rather than pick a side",
      p("Ask what your dissolved-oxygen headroom is. Running near air saturation on air stones, at "
        "8&ndash;9 mg/L, you have almost no margin &mdash; keep the reservoir mineral and clean. "
        "Running an oxygen concentrator or nanobubble generator at 15&ndash;20 mg/L, you have real "
        "headroom and can spend some of it on biology. Either way, measure DO before and after you "
        "introduce an organic input. If it drops and stays down, the microbes are eating your "
        "margin.")),
    callout("warn", "The specific trap",
      p("Fulvic and humic products often carry their own iron and chelating capacity, which is why "
        "adding them can visibly move ORP &mdash; an initial drop as reduced carbon enters, then a "
        "sustained shift as the iron equilibrium re-establishes. Do not read that ORP movement as "
        "evidence about oxygen. It is a chemistry change, and it is happening to a chelate system "
        "you have now made more complicated to reason about.")),
    p("If you do want biology, targeted inoculants have better evidence behind them than "
      "general-purpose organic feeds. <em>Bacillus subtilis</em> and <em>Pseudomonas fluorescens</em> "
      "applied together suppressed <em>Pythium aphanidermatum</em> synergistically, upregulating "
      "defence genes and raising survival to 83%" + _c("dwc-rashad-2024-biocontrol") + ", and "
      "<em>Pseudomonas</em> biocontrol across crops can match chemical fungicides &mdash; with the "
      "consistent caveat that field performance is far less reliable than laboratory performance" +
      _c("dwc-alattas-2024-pseudomonas") + "."),
  ]})

# 8 ----------------------------------------------------------------- pathology
SECTIONS.append({"id": "pathology", "kicker": "Failure mode", "title": "Root rot is an oxygen problem wearing a pathogen costume",
  "blocks": [
    lead("The single most important finding in the water-culture pathology literature is that low "
         "dissolved oxygen and <em>Pythium</em> root rot are not two independent risks. They are one "
         "coupled failure with a shared pathway through root-zone oxygen status."),
    p("A review synthesising hydroponic systems engineering, plant physiology and oomycete pathology "
      "makes the case directly. Progressive root-mat development degrades passive aeration and "
      "creates hypoxic conditions. Hypoxia impairs root membrane integrity and alters the exudate "
      "profile leaking from the root. Those altered exudates are what <em>Pythium</em> zoospores "
      "home in on, encyst against, and use to make the transition from biotrophic to necrotrophic "
      "&mdash; from quietly present to actively killing" + _c("dwc-scott-2026-do-pythium") + "."),
    figure(L.flow("The root-rot cascade",
            [("Oxygen falls", "temperature rises, root mat thickens, or aeration fails"),
             ("Membranes leak", "hypoxic roots lose integrity; exudate profile changes"),
             ("Zoospores home in", "altered exudates are a chemical beacon"),
             ("Necrotrophic switch", "an elicitor triggers browning and active tissue kill"),
             ("Collapse", "root function lost, whole-plant carbon gain falls")],
            note="Every arrow is downstream of the first box. Treating the pathogen without fixing oxygen restarts the cascade."), 13,
      "Root rot in water culture is rarely a hygiene failure in isolation. It is usually an oxygen "
      "failure that a ubiquitous opportunist exploited." + _c("dwc-scott-2026-do-pythium") + _c("dwc-sutton-2006-pythium")),
    photo_sequence("What the cascade looks like at the root",
      [("Healthy", f"{IMG}/03-roots-healthy.jpg"), ("Collapsing", f"{IMG}/04-roots-rot.jpg")],
      "Left: brilliant white, fine, densely branched, glistening. Right: the same root mass after "
      "the cascade &mdash; tan-brown, matted and slimy at the core, with a fringe of white still "
      "surviving at the periphery where oxygen still reaches. That fringe is the tell: this is a "
      "gradient failure, not an infection that arrived all at once.", model=GPT),
    callout("key", "Where to spend your effort",
      p("The definitive review of <em>Pythium</em> in hydroponic crops draws a conclusion that "
        "contradicts how most systems are designed: measures that disinfest the nutrient solution "
        "<em>as it recirculates outside the crop</em> have commonly minor impact on epidemics. What "
        "works is treatment that suppresses the pathogen <strong>in the roots and root zone</strong>" +
        _c("dwc-sutton-2006-pythium") + ". A UV steriliser on the return line is doing less than the "
        "brochure implies if the root zone itself is warm and under-oxygenated.")),
    p("Environmental stress is the other half of the story. The same review highlights the "
      "predisposition of roots to <em>Pythium</em> attack by stress factors, and notes that "
      "infection markedly slows leaf-area expansion and whole-plant carbon gain "
      "<em>without</em> significantly reducing photosynthetic efficiency per unit leaf area" +
      _c("dwc-sutton-2006-pythium") + ". The plant is not sick-looking; it is just quietly building "
      "less canopy than it should. By the time it looks obviously wrong, you have lost weeks."),
    callout("tip", "The tell that arrives before the brown roots",
      p("In water culture there is an early behavioural sign worth more than any probe: "
        "<strong>roots that stay up in the clay pebbles and will not grow down into the "
        "solution.</strong> A root system actively declining to enter the water is telling you the "
        "water is hostile &mdash; too warm, too low in oxygen, or carrying a microbial load it is "
        "avoiding. Growers who fix the oxygen supply report the behaviour reversing. Read it as a "
        "root-zone alarm, not as a slow-establishing plant.")),
    p("On chemical oxidisers as a treatment: they work, and they have a cost. Hydrogen peroxide "
      "applied into hydroponic solution across 0&ndash;400 mg/L produced visible root injury in "
      "every crop tested, with cucumber the most susceptible, and the concentrations needed for "
      "pathogen control sat at or above the injury threshold" + _c("dwc-eicher-sodo-2020-h2o2") + ". "
      "In an ebb-and-flow trial, higher peroxide rates restricted lettuce growth and failed to "
      "control algae at any rate tested" + _c("dwc-hendrickson-2022-h2o2") + "."),
    callout("warn", "The peroxide reflex",
      p("Dumping peroxide into a reservoir at the first sign of brown roots is understandable and "
        "usually counterproductive. It burns root tissue that is already compromised, it is consumed "
        "within hours so it does nothing durable, and it treats the symptom while the cause &mdash; "
        "warm, under-oxygenated water &mdash; is untouched. Check the thermometer and the air "
        "manifold first. A hypochlorous product dosed at a maintenance rate is a more defensible "
        "routine approach than peroxide shocks, and the manufacturer schedules it that way: a large "
        "dose at fill and change-out, then a small continuous maintenance rate through the run" +
        _c("dwc-athena-rdwc-2024") + ".")),
  ]})

# 9 --------------------------------------------------------------- temperature
SECTIONS.append({"id": "temperature", "kicker": "The master dial", "title": "Solution temperature controls everything else",
  "blocks": [
    p("If you take one operational lever away from this paper, take this one. Reservoir temperature "
      "simultaneously sets oxygen supply, oxygen demand, pathogen growth rate and pH stability. "
      "Nothing else you can adjust touches that many variables at once."),
    p("The experimental case is clean. Cooling a recirculating hydroponic solution across four "
      "setpoints from 33 &deg;C down to 22 &deg;C raised dissolved oxygen in both the feed and the "
      "drain, raised measured <em>oxygen consumption by the roots</em>, and improved every growth, "
      "yield and quality attribute measured, across three cropping seasons over two years" +
      _c("dwc-alrawahy-2019-rzt") + ". Note the second result: cooler roots did not respire less, "
      "they respired more, because they were no longer oxygen-limited."),
    figure(D.supply_demand(), 14,
      "The two curves that make temperature the master dial. Every degree of warming takes oxygen "
      "out of the water and simultaneously asks the root for more of it." +
      _c("dwc-benson-krause-1984") + _c("dwc-alrawahy-2019-rzt")),
    p("Commercial practice tracks a descending ramp rather than a single setpoint. A published RDWC "
      "programme steps solution temperature down through the crop" + _c("dwc-athena-rdwc-2024") + ":"),
    figure(L.line("Commercial RDWC solution-temperature schedule",
            [("Veg", 21.1), ("Fl 1", 20.6), ("Fl 2", 20.0), ("Fl 3", 19.4), ("Fl 4", 18.9),
             ("Fl 5", 18.3), ("Fl 6", 17.8), ("Fl 7", 16.7), ("Fl 8", 16.7), ("Finish", 13.9)],
            ["Veg", "Fl1", "Fl2", "Fl3", "Fl4", "Fl5", "Fl6", "Fl7", "Fl8", "Fin"],
            ylab="°C", ymin=12, ymax=23,
            note="Warm enough to establish, then progressively cooler as root mass and oxygen demand grow."), 15,
      "The ramp is not arbitrary. Root mass and total oxygen demand rise through the crop, so the "
      "supply side has to rise with it &mdash; and the cheapest way to raise dissolved oxygen is to "
      "lower the temperature." + _c("dwc-athena-rdwc-2024")),
    table(["Boundary", "Value", "Why it exists"], [
      ["Do not transplant clones below", "18.9 &deg;C",
       "Cold shock on a root system with no established mass; pH also swings with temperature"],
      ["Uptake begins to fall below", "16.7 &deg;C",
       "Cold roots take up nutrients more slowly &mdash; the floor on the useful range"],
      ["Deliberate cold finish", "13.9 &deg;C for the last ~10 days",
       "Accepts reduced uptake in exchange for colour expression, when uptake no longer matters"],
      ["Pathogen comfort zone", "above ~22&ndash;24 &deg;C",
       "Warm water is where low DO and fast <em>Pythium</em> growth meet"],
    ], cls="compact", caption="Temperature boundaries from a commercial RDWC procedure, with the "
      "reasoning behind each." + _c("dwc-athena-rdwc-2024")),
    callout("tip", "Chiller or no chiller",
      p("In any room warmer than about 24 &deg;C with lights on, an uninsulated reservoir will "
        "equilibrate somewhere unhelpful. Insulate first &mdash; it is free and it flattens the "
        "diurnal swing. Then chill if you still cannot hold the band. Note the interaction with "
        "aeration: a blower drawing hot room air is also a heater, which is one more reason the air "
        "supply belongs outside the canopy space. In a CO<sub>2</sub>-enriched flower room the air "
        "pump should sit outside the room entirely" + _c("dwc-athena-rdwc-2024") + ".")),
  ]})

# 10 -------------------------------------------------------------------- feed
SECTIONS.append({"id": "feed", "kicker": "Nutrition", "title": "Why water culture runs a leaner feed than you expect",
  "blocks": [
    p("Growers moving from coco to RDWC almost always over-feed at first, because the EC numbers "
      "look wrong. They are not wrong. Water culture genuinely runs lower, and the reason is "
      "structural."),
    callout("key", "Contact time is the variable that changed",
      p("In coco, the root sees concentrated feed briefly during a shot and then sits in a substrate "
        "whose pore-water EC it has partly consumed. In DWC the entire root system is in continuous "
        "contact with the full solution volume, all day, every day. The same delivered nutrition "
        "needs a much lower concentration. The manufacturer states it plainly: RDWC EC is lower than "
        "traditional feeding programmes because of the high volume of solution in constant contact "
        "with the root system" + _c("dwc-athena-rdwc-2024") + ".")),
    figure(L.line("Commercial RDWC electrical-conductivity schedule",
            [("Initial", 0.21), ("V2", 0.33), ("V4", 0.67), ("F1", 0.71), ("F2", 0.93),
             ("F3", 1.07), ("F4", 1.21), ("F5", 1.36), ("F6", 1.50), ("F7", 1.36), ("F8", 1.29)],
            ["Init", "V2", "V4", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8"],
            ylab="EC (mS/cm)", ymin=0, ymax=1.8,
            note="Feathering up gradually, peaking mid-late flower, then tapering. Finish runs 0-1.0."), 16,
      "Peak EC around 1.5 mS/cm is roughly half what many coco programmes run at the same stage. "
      "The plant is not being underfed; the delivery mechanism is different." + _c("dwc-athena-rdwc-2024")),
    defterm("Feathering up",
      "Raising EC gradually through repeated small nutrient additions rather than in steps. In a "
      "reservoir shared by every plant, a large single addition is a shock delivered to the whole "
      "crop at once." + _c("dwc-athena-rdwc-2024")),
    defterm("Addback",
      "Nutrient returned to the system through the control bucket to restore EC, which is "
      "continuously depleted both by plant uptake and by fresh-water top-off. In a recirculating "
      "system nutrients are consumed at different rates, so the solution progressively "
      "<em>unbalances</em> even while its EC looks correct &mdash; which is what change-outs exist "
      "to fix."),
    p("There is a strong independent check on the lean-feeding principle. In closed-system "
      "hydroponics with continuous root-zone nutrient quantification, doubling nutrient input from "
      "2 to 4 mS/cm raised nutrient accumulation in solution but produced <strong>no significant "
      "increase in yield or quality</strong> in medical cannabis. Nor did raising phosphorus from 15 "
      "to 90 mg/L, despite flower phosphorus concentration rising 70%. The authors' conclusion is "
      "that cannabis tolerates high nutrient concentrations, but neither excess phosphorus nor "
      "excess fertilisation improves yield or quality" + _c("dwc-hershkowitz-2025-p-ec") + "."),
    p("pH runs a parallel schedule, stepping from about 6.2&ndash;6.3 at fill down to 5.8 and holding "
      "there through flower" + _c("dwc-athena-rdwc-2024") + ". The published guidance calls pH the "
      "most important parameter to adhere to, with a note that it moves rapidly after an addback and "
      "should be allowed to stabilise before correcting &mdash; chasing it immediately after dosing "
      "is how growers end up over-buffering."),
    callout("note", "Nitrogen form is a pH lever, not just a nitrogen choice",
      p("Roots take up cations and anions unequally and balance the charge by exporting H<sup>+</sup> "
        "or OH<sup>-</sup>. Pure nitrate nutrition drove solution pH to about 8.0; excessive ammonium "
        "drove it to 3.6; an appropriate mixed ratio held it near 5.8 with the best yield and "
        "nitrogen-use efficiency" + _c("dwc-zhu-2021-nh4-no3") + ". If your reservoir climbs "
        "relentlessly and you are dosing acid daily, the ammonium fraction of your feed is a lever "
        "worth examining before you buy a bigger acid pump.")),
    p("Two more line items worth understanding. Potassium silicate is commonly used in these "
      "programmes as the pH-up agent, which conveniently delivers silicon at the same time &mdash; "
      "silicon deposits in cell walls, supports antioxidant systems and improves stress tolerance" +
      _c("dwc-hassan-2024-silicon") + ". And the &lsquo;finish&rsquo; phase in water culture runs EC "
      "down toward zero, which is trivially easy here compared to a substrate: you simply stop adding "
      "back and let the plants eat the reservoir down."),
    callout("warn", "One thing water culture cannot do",
      p("Controlled drought stress applied late in flower has been shown to raise cannabinoid "
        "concentration and yield per unit area substantially in container-grown cannabis" +
        _c("dwc-caplan-2019-drought") + ". Water culture cannot execute it. If your steering "
        "strategy depends on generative dryback, DWC is structurally the wrong system &mdash; not a "
        "worse one, a different one. Its advantages lie in uninterrupted vegetative-phase growth "
        "rate, not in water-based steering.")),
  ]})

# 11 ------------------------------------------------------------------- build
SECTIONS.append({"id": "build", "kicker": "Build", "title": "Sizing and building the system",
  "blocks": [
    p("Design decisions in water culture are mostly about buying yourself margin, because the "
      "system has none by default."),
    defterm("Operating volume",
      "The working solution volume with the level sitting just below the planting deck. In a "
      "published commercial spec, roughly 40 L in a 49 L module and roughly 19 L in a 30 L module" +
      _c("dwc-athena-rdwc-2024") + "."),
    defterm("Change-out volume",
      "Operating volume minus the liquid that stays behind when the system drains to the top of the "
      "bulkhead. Worth calculating once: in a published 32-site example, 1325 L operating volume "
      "leaves 375 L behind, so a &lsquo;full&rsquo; change-out actually replaces 946 L &mdash; about "
      "<strong>71%</strong> of the water" + _c("dwc-athena-rdwc-2024") + ". A full change-out is not "
      "a reset to zero, and it matters when you are trying to correct an accumulated imbalance."),
    steps([
      ("Size the volume generously",
       "More water is more thermal mass, more chemical buffer and more time to notice a problem. "
       "Depth also matters independently: at least 20 cm of solution stabilises concentrations and "
       "improves uniformity" + _c("dwc-langenfeld-2024-zero-discharge") + "."),
      ("Put every control in a plant-free bucket",
       "Probes, heater or chiller, top-off float, circulation pump and dosing all belong in the "
       "control bucket. No plant site should ever be the measurement point, and nothing concentrated "
       "should ever meet a root."),
      ("Size aeration to the window, not to the maximum",
       "Around 100 mL&#183;min<sup>-1</sup> per litre" + _c("dwc-langenfeld-2024-zero-discharge") +
       ", or one medium air stone per 30 L bucket" + _c("dwc-athena-rdwc-2024") + ". Published "
       "manifold pressures run about 6.5 kPa in veg and 7.0&ndash;7.5 kPa in flower on a water-column "
       "gauge. Resist the urge to over-provision."),
      ("Place stones deliberately",
       "Bottom of the bucket, offset roughly 2.5 cm from the wall, never directly under the net pot. "
       "Check every stone bubbles uniformly at fill &mdash; a clogged stone is a silent, "
       "single-plant hypoxia event."),
      ("Keep air pumps and blowers out of the room",
       "They are heat sources, and in a CO<sub>2</sub>-enriched room they should be outside it "
       "entirely" + _c("dwc-athena-rdwc-2024") + "."),
      ("Plumb continuous RO top-off",
       "A float valve in the control bucket fed from an RO manifold holds level automatically. "
       "Manual top-off means EC and level both sawtooth, and every plant feels it."),
      ("Rinse and condition the media before it touches a plant",
       "Expanded clay carries dust and fines. The published procedure rinses it, soaks it in "
       "acidified water with a hypochlorous product, then rinses again" + _c("dwc-athena-rdwc-2024") +
       ". Net pots get a sanitiser dunk to remove factory dust and plastic particles."),
      ("Set the crown above the waterline",
       "The basal stem and any rockwool cube must sit above the solution or you get stem rot. The "
       "solution should just bubble over the structural ring beneath the planting deck &mdash; "
       "close enough to reach, not so deep it drowns the crown."),
    ]),
    callout("tip", "Design in a failure mode you can survive",
      p("Ask what happens when the power fails at 2 a.m. A large, cool, well-oxygenated volume "
        "carries a crop for hours. A small, warm, marginal one is in trouble within one. Battery "
        "backup on the air pump buys more crop insurance per dollar than backup on almost anything "
        "else in the room, because the oxygen reserve is the resource with the shortest half-life.")),
    figure(D.system_schematic(), 17,
      "The whole loop. Plant sites are deliberately dumb &mdash; every probe, dose, pump and float "
      "lives in the one bucket with no plant in it, so nothing concentrated ever meets a root and "
      "no single site can be mistaken for the system." + _c("dwc-athena-rdwc-2024")),
    photo(f"{IMG}/07-control-bucket.jpg",
      "A control bucket in practice: pump, float valve on the RO line, and probes clipped into a "
      "perforated stilling tube that shields them from the bubble plume.", model=GPT),
  ]})

# 12 --------------------------------------------------------------------- run
SECTIONS.append({"id": "run", "kicker": "Operate", "title": "Running it: checks, change-outs and diagnosis",
  "blocks": [
    p("Water culture rewards routine and punishes improvisation. The daily round is short; the value "
      "is in doing it every day, at the same time, and writing the numbers down."),
    grid([
      card("Every day", ul([
        "Level at operating volume; top-off working",
        "Solution temperature in band for the stage",
        "Circulation pump flowing; discharge valve clear",
        "Air pump running, every stone bubbling evenly",
        "pH and EC, from a calibrated meter",
        "<strong>Smell the reservoir</strong> &mdash; fresh, not putrid, not chlorine",
        "Look for leaks",
      ], "tight"), tag="~5 min"),
      card("Every week", ul([
        "Calibrate pH and EC probes",
        "Clean the ORP and DO probes &mdash; biofilm is a silent error" + _c("dwc-sholikah-2025-pt-electrode"),
        "Verify pH and EC against a second meter",
        "Inspect a root mass: white and firm, not tan and slimy",
        "Check inline filters",
        "Review the trend, not just today's number",
      ], "tight"), tag="~30 min"),
    ], cols=2),
    p("Change-outs are the reset mechanism, and knowing when to reach for one is most of the skill. "
      "A partial change-out replaces 20&ndash;50% to correct minor imbalance; a full change-out drains "
      "to the bulkhead and rebuilds the solution" + _c("dwc-athena-rdwc-2024") + "."),
    table(["Situation", "Action"], [
      ["Routine, at three weeks of veg", "Partial"],
      ["pH drifting despite correction", "Partial first; full if it persists"],
      ["Plants have slowed feeding despite stable parameters", "Partial"],
      ["pH rising or falling beyond allowable limits", "Full"],
      ["pH correction needs a steadily increasing amount of buffer", "Full"],
      ["Parameters went out of range through operator error", "Full"],
      ["Flipping to bloom after four or more weeks of veg", "Full"],
      ["Post-defoliation, or around days 26&ndash;32", "Full"],
      ["10&ndash;14 days before harvest", "Full"],
    ], cls="compact", caption="Change-out triggers from a published commercial procedure. The pattern "
      "is worth noting: <em>escalating buffer demand</em> is the signal that the solution has "
      "unbalanced, even when EC and pH still read correctly." + _c("dwc-athena-rdwc-2024")),
    callout("warn", "Change-outs are a race",
      p("Roots exposed to air are stressed and damaged fast. Drain quickly, refill immediately, and "
        "power the system down while you do it. Have the replacement water made and tempered "
        "<em>before</em> you open the drain &mdash; the worst version of this job is discovering "
        "mid-drain that the RO tank is empty.")),
    photo(f"{IMG}/09-changeout.jpg",
      "A change-out in progress. Drain open, refill line already staged. The clock is running on "
      "root exposure from the moment the level drops.", model=GPT),
    p("Diagnosis is where the sections of this paper come together. Most water-culture faults present "
      "as one of three symptoms, and each has multiple causes calling for opposite actions:"),
    table(["What you see", "Likely causes", "First check", "Common wrong move"], [
      ["Interveinal chlorosis, new growth",
       "Chelate failed above its pH ceiling; or aeration stripping the rhizosphere",
       "pH history, then aeration rate",
       "Adding more iron"],
      ["General yellowing, dry crusty leaf edges",
       "ORP shock from oxidiser over-dose",
       "Oxidiser dose rate; smell for chlorine",
       "Reading it as a feed deficiency and adding nutrient"],
      ["Slow growth, slight wilt, feed on target",
       "Hypoxia &mdash; stelar oxygen deficit before visible root damage",
       "Solution temperature, then DO, then every air stone",
       "Raising EC"],
      ["Brown, slimy roots; putrid smell",
       "Root rot, downstream of low oxygen",
       "Temperature and aeration &mdash; not the pathogen",
       "Peroxide shock without fixing oxygen"],
      ["pH climbing relentlessly",
       "Nitrate-dominant nitrogen; or CO<sub>2</sub> stripped by over-aeration",
       "Ammonium fraction of the feed; aeration rate",
       "Escalating acid doses"],
      ["DO reading swinging wildly",
       "Probe sitting in the bubble plume",
       "Probe placement &mdash; read in a calm pocket",
       "Believing the number"],
      ["Roots stay in the clay, will not enter the water",
       "Hostile solution: warm, low DO, or high microbial load",
       "Temperature and DO, then reservoir cleanliness",
       "Waiting it out as &lsquo;slow establishment&rsquo;"],
      ["ORP jumped ~200 mV after an equipment change",
       "The reservoir got cleaner &mdash; not a direct oxygen effect",
       "Whether a chemical oxidiser is in play; log pH alongside",
       "Reading it as a dissolved-oxygen measurement"],
    ], caption="The diagnostic table. Note how often the correct action is to turn something "
      "<em>down</em> rather than add something."),
    callout("key", "The five things that matter most, in order",
      ol(["<strong>Solution temperature.</strong> It sets oxygen supply, oxygen demand and pathogen "
          "growth rate simultaneously. Nothing else has that reach.",
          "<strong>Adequate but gentle aeration.</strong> Get above the hypoxic floor, then stop. "
          "The top of the range has its own failure mode.",
          "<strong>pH, held steadily.</strong> It determines whether your iron chelate is doing its "
          "job, and it is the parameter with the least buffering behind it.",
          "<strong>Cleanliness.</strong> Organic load is oxygen demand. Spend your DO headroom "
          "deliberately, not accidentally.",
          "<strong>Written-down numbers.</strong> Every diagnosis in the table above is a trend "
          "question. A single reading answers almost nothing &mdash; least of all an ORP reading "
          "without its pH."], "tight")),
  ]})
