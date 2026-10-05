# -*- coding: utf-8 -*-
"""Paper: deep water culture from first principles - oxygen, redox, iron and the reservoir."""
from components import (p, lead, ul, ol, callout, defterm, table, figure,
                        grid, card, chip, kv, steps, photo, photo_sequence)
import figs_lib as L
import figs_dwc as D

IMG = "assets/img/deep-water-culture"
GPT = "gpt-image-1"

SLUG = "deep-water-culture"
TITLE = "Deep water culture: the basic physics and chemistry"
EYEBROW = "Water culture · Root-zone oxygen"
SUB = ("This paper shows that the temperature of the solution is the primary control for all the "
       "other conditions in water culture. It shows how to set the aeration rate. The correct rate "
       "adds oxygen and does not remove the chemical boundary layer that the roots make. It also "
       "shows the quantity that an ORP probe measures and the quantities that it does not measure. "
       "The example in this paper is cannabis in a recirculating type of deep water culture (RDWC). "
       "The physics of dissolved oxygen and the chemistry of iron apply to all crops.")
META = [("droplet", "Water culture"), ("image", "17 diagrams · 10 photos"),
        ("quote", "40 sources"), ("clock", "~38 min to read")]
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
SECTIONS.append({"id": "intro", "kicker": "Start here", "title": "Purpose and scope",
  "blocks": [
    lead("In coco or rockwool, the substrate is a buffer. The substrate holds water, holds air and "
         "holds an electrical charge. It also decreases the effect of a small error in the feed. "
         "Deep water culture has no buffer. The roots hang in the nutrient solution, and the "
         "reservoir must do all the tasks of the substrate at the same time and continuously. The "
         "reservoir has no headroom."),
    p("All the other sections of this paper are a result of this fact. The highest growth rates in "
      "soilless culture and the fastest crop failure come from the same property. There is no "
      "buffer between your decision and the root.</p><p>If you operate the system correctly, you "
      "can get a better result than in other systems. Reviews of deep-water-culture tomato report "
      "the same result in many tests. The tomato has more biomass, higher efficiency of "
      "photosynthesis, more root growth and higher yield than tomato in soil or in other hydroponic "
      "systems. The reviews give the continuous supply of a solution that contains oxygen and has a "
      "high nutrient content as the cause." + _c("dwc-nsele-2026-dwc-tomato")),
    figure(L.flow("The tasks of the reservoir at the same time",
            [("Hold water", "All the roots are in the water, permanently"),
             ("Hold oxygen", "No pores with air, thus each milligram of O2 is in solution"),
             ("Hold the feed", "EC and pH have no substrate buffer against change"),
             ("Hold the biology", "One water volume touches all the plants")],
            note="Coco does the first three tasks with no power. In water culture, all four tasks use power."), 1,
      "In a substrate system, the medium, the drip line and the drain each do some of these four "
      "functions. In water culture, one volume of water that flows does all four functions. A "
      "malfunction of one function causes malfunctions of the other functions."),
    photo(f"{IMG}/01-rdwc-room.jpg",
      "An RDWC room in a production facility. The same loop connects all the buckets. Thus all the "
      "buckets have the same EC, the same pH, the same temperature and the same group of microbes. "
      "The photo shows a good property and a risk at the same time.", model=GPT),
    defterm("Deep water culture (DWC)",
      "The roots hang directly in a nutrient solution with aeration. A net pot and inert media, for "
      "example expanded clay, hold the crown above the water level. One bucket is DWC. Buckets that "
      "connect to one reservoir with a circulation pump are <strong>RDWC</strong>. RDWC is the "
      "recirculating type of DWC."),
    figure(D.bucket_xsection(), 2,
      "The figure shows a cross section of one plant site. The two volumes are different. The "
      "<strong>operating volume</strong> is the volume that you use to calculate the dose. The "
      "<strong>remaining volume</strong> is the volume below the bulkhead, and the drain cannot "
      "remove it." + _c("dwc-athena-rdwc-2024")),
    photo(f"{IMG}/02-bucket-open.jpg",
      "The photo shows the same system. The net pot is in the lid. Expanded clay holds the crown "
      "above the water. The roots hang free in the solution. There is no substrate between the feed "
      "and the root.", model=GPT),
    defterm("Control bucket",
      "A bucket with no plant in an RDWC loop. The bucket contains the pump, the float valve for "
      "the RO water, the probes, and the heater or chiller. You do all the measurements and add all "
      "the doses in this bucket. Thus no plant site is a point of measurement." +
      _c("dwc-athena-rdwc-2024")),
    callout("key", "The three primary numbers of this paper",
      ul(["<strong>Dissolved oxygen (DO)</strong> is the quantity of O<sub>2</sub> in the water, in "
          "mg/L. It is the ceiling for root respiration.",
          "<strong>Solution temperature</strong> changes the maximum quantity of oxygen that the "
          "water <em>can</em> hold. It also changes the rate at which the roots and microbes "
          "<em>use</em> the oxygen. Solution temperature is the primary control.",
          "<strong>ORP</strong> is the oxidation-reduction potential, in millivolts. Growers read "
          "this number incorrectly more frequently than other numbers in hydroponics. This paper "
          "gives more information about ORP than about the other two numbers."], "tight")),
    callout("note", "Who this is for",
      p("This paper is for a person who operates a water culture system or who thinks about it. It "
        "is also for a person who sees an ORP reading and does not know the next step. This paper "
        "does not give information about EC and pH. If you do not know EC and pH, read the pH paper "
        "and the water-quality paper first. The example is cannabis, but the physics applies to all "
        "crops.")),
  ]})

# 2 ------------------------------------------------------------- oxygen budget
SECTIONS.append({"id": "oxygen-budget", "kicker": "Physics", "title": "Oxygen solubility in nutrient solution",
  "blocks": [
    p("Start with the limit that you cannot change. Only a small quantity of oxygen dissolves in "
      "water. Water holds dissolved oxygen only up to a ceiling. The ceiling changes with the "
      "temperature and the pressure. The water releases the oxygen when its temperature increases "
      "or when you shake the water. When the temperature is higher, the ceiling is lower.</p><p>At "
      "20 &deg;C (68 &deg;F), in equilibrium with usual air at sea level, water holds approximately "
      "<strong>9.1 mg/L</strong> of dissolved oxygen." + _c("dwc-benson-krause-1984") +
      " Air contains approximately 280 mg/L of oxygen. Water at saturation contains approximately "
      "one part in thirty of the oxygen in the same volume of air. A root in the solution has only "
      "this quantity of oxygen."),
    defterm("Saturation",
      "The concentration that a gas has in a liquid when the liquid is in equilibrium with the gas "
      "above it. Henry's law shows that the dissolved concentration is in proportion to the partial "
      "pressure of the gas in the gas phase." + _c("dwc-bok-2023-o2-solubility")),
    figure(L.line("DO decreases when the temperature is higher",
            [("10", 11.29), ("14", 10.31), ("18", 9.47), ("20", 9.09), ("22", 8.74),
             ("25", 8.26), ("28", 7.83), ("30", 7.56)],
            ["10 C", "14 C", "18 C", "20 C", "22 C", "25 C", "28 C", "30 C"],
            ylab="mg/L", ymin=6, ymax=12,
            note="Fresh water, 1 atm, in equilibrium with air. Source: standard solubility tables."), 3,
      "When the reservoir temperature increases from 18 to 28 &deg;C (64&ndash;82 &deg;F), the "
      "water can hold approximately 17% less oxygen. This occurs before the roots use the oxygen." +
      _c("dwc-benson-krause-1984")),
    callout("key", "A higher reservoir temperature causes two problems",
      p("At approximately 20 &deg;C (68 &deg;F), the solubility of oxygen decreases by "
        "approximately 1.7% for each &deg;C. Root respiration and the respiration of microbes have "
        "a Q<sub>10</sub> of approximately 2. Thus, when the temperature increases by 10 &deg;C, "
        "the roots and microbes use approximately <em>two times</em> as much oxygen. At the same "
        "time, the oxygen that the water holds decreases by approximately one sixth. Thus the ratio "
        "of the available oxygen to the oxygen that the roots and microbes use decreases by "
        "approximately two and a half times. When a system has a problem, the first check is the "
        "temperature of the reservoir and not the aeration equipment.")),
    p("Many growers read a high DO value incorrectly. Growers who use an oxygen concentrator with a "
      "diffuser that makes small bubbles frequently report 15&ndash;25 mg/L. Then they think that "
      "the water holds a dangerous quantity of oxygen. Two facts are correct at the same time. Use "
      "the two facts together to read the value correctly."),
    grid([
      card("In relation to air: yes, more than saturation",
           p("At 22 &deg;C (72 &deg;F), water at air saturation holds approximately 8.7 mg/L. A "
             "reading of 20 mg/L is approximately <strong>2.3&times; air saturation</strong>. If "
             "you stop the gas and let the water stay open to the room air, the water will slowly "
             "release oxygen. The value will decrease to 8.7 mg/L."), tag="2.3&times;"),
      card("In relation to your gas: far below saturation",
           p("A pressure-swing concentrator supplies a gas that has approximately 90&ndash;95% "
             "oxygen. Henry's law shows that the concentration is in proportion to the partial "
             "pressure. Thus, at 22 &deg;C (72 &deg;F), this gas can give approximately <strong>38 "
             "mg/L</strong> in the water at equilibrium. Your 20 mg/L is approximately half of this "
             "value. While the gas flows, the oxygen stays in the water."), tag="approximately 52%"),
    ], cols=2),
    callout("note", "This difference is important in operation",
      p("A solution can hold more oxygen than the saturation value for <em>air</em> and less oxygen "
        "than the saturation value for the <em>gas that you inject</em>. This solution is stable "
        "while the gas flows. When the gas stops, the oxygen decreases slowly. The solution does "
        "not make bubbles on the surfaces of the roots.</p><p>The important problem is not gas "
        "embolism. The important problem is that the pump stops. After the pump stops, the oxygen "
        "decreases to 8.7 mg/L, but the root mass has the size for 20 mg/L.")),
    p("The size of the bubbles is the other control. A usual air stone makes bubbles that are some "
      "millimeters in size. These bubbles move up and break in some seconds.</p><p>Nanobubbles are "
      "smaller than approximately 200 nm. The surface of a nanobubble has a negative charge. As a "
      "result, two bubbles do not become one bubble. The pressure in a nanobubble is high, and thus "
      "the gas continues to dissolve.</p><p>In the first tests on nanobubbles, a measurement found "
      "them in water for approximately <strong>70 days</strong>." + _c("dwc-ebina-2013-nanobubble") +
      " The nanobubbles supply the gas by a different method. The gas continues to dissolve for a "
      "long time after the bubbles that you can see stop."),
    figure(D.bubble_scale(), 4,
      "The three bubble sizes are not three grades of quality. The physics of the three sizes is "
      "different. Only nanobubbles supply gas with no plume of bubbles. As the next section shows, "
      "the plume is the primary problem of aeration with large bubbles." +
      _c("dwc-ebina-2013-nanobubble")),
    photo(f"{IMG}/08-nanobubble.jpg",
      "Left: an air stone that makes large bubbles. You can see a plume with turbulence. Right: "
      "water with nanobubbles. The water is not transparent, and there is no plume. The gas is the "
      "same, but the mechanical effect on the root zone is very different.", model=GPT),
  ]})

# 3 ------------------------------------------------------------ how much is enough
SECTIONS.append({"id": "how-much", "kicker": "Targets", "title": "Plant oxygen demand",
  "blocks": [
    p("The data from tests agree about the bottom of the range, but they do not agree about the top "
      "of the range. These two facts are important."),
    p("At the bottom of the range, a test used bell pepper in floating culture. With ammonium "
      "nutrition, the growth and the photosynthesis decreased when the DO was less than "
      "approximately <strong>3.8 mg/L</strong>. With nitrate nutrition, they decreased when the DO "
      "was less than <strong>5.3 mg/L</strong>. The authors recommended these two values as floors. "
      "The DO must not be less than these values." + _c("dwc-roosta-2024-o2-nform") +
      "</p><p>The difference between the two types of nitrogen is important. Nitrate assimilation "
      "uses a large quantity of energy. Thus a root with nitrate uses more oxygen than a root with "
      "ammonium."),
    figure(L.bars("DO values in hydroponic tests",
            [("Hypoxia", 2.0), ("NH4 floor", 3.8), ("NO3 floor", 5.3),
             ("Saturation 20C", 9.1), ("NFT with O2", 8.8), ("DWC with O2", 15.0),
             ("O2 concentrator", 20.0)], unit=" mg/L",
            note="Tests give the floors. The top two values come from enrichment systems. They are not minimum values.",
            maxv=24), 5,
      "Growers do not agree about the values between the floor of approximately 5 mg/L for the "
      "plant and the 15&ndash;20 mg/L that enrichment equipment supplies. At more than "
      "approximately 8&ndash;10 mg/L, the data show that the effect of more DO is different for "
      "each crop. The cost of the enrichment is also important." + _c("dwc-roosta-2024-o2-nform") +
      _c("dwc-nitu-2024-nft-oxygen") + _c("dwc-qin-2025-do-enrichment")),
    p("At the top of the range, the effect of more oxygen becomes smaller and then stops. In NFT "
      "(nutrient film technique) lettuce, the plants became much larger when the DO increased from "
      "approximately 7 mg/L to approximately 8.5&ndash;9 mg/L. The wet weight was up to 110% higher "
      "in one cultivar, and the root mass was 78% higher." + _c("dwc-nitu-2024-nft-oxygen") +
      "</p><p>A test in deep water culture used controlled enrichment at 10, 15 and 20 mg/L. The "
      "effect was different for each crop. Arugula became 63&ndash;191% larger at more than 15 "
      "mg/L, and kale did not become larger at all the DO values. The enrichment caused a "
      "<strong>140% higher electricity cost</strong>. Only arugula at 20 mg/L gave sufficient value "
      "for the cost of the energy." + _c("dwc-qin-2025-do-enrichment")),
    figure(L.zones("The range of DO for operation", 0, 22,
            [(0, 3.8, L.REDL, "Hypoxia: root damage"),
             (3.8, 6.0, L.AMBL, "Low"),
             (6.0, 10.0, L.GL, "Good: near air saturation"),
             (10.0, 22.0, L.BLUL, "Enrichment: for some crops, at a cost")], unit=" mg/L",
            note="Less than 3.8: root damage. Approximately 10 or more: more cost, and the yield is not sure."), 6,
      "To increase the DO from hypoxia to the Good zone is the task with the highest value for its "
      "cost in water culture. To increase the DO from the Good zone to the Enrichment zone is a "
      "decision about cost and not about horticulture."),
    callout("warn", "Hypoxia causes damage to the plant before you can see it in the roots",
      p("When the oxygen in the root zone is low, the first effect is not brown roots. The first "
        "effect is not sufficient energy. The cortex of the root can continue to get sufficient "
        "O<sub>2</sub> to absorb nutrients. At the same time, the stele has hypoxia.</p><p>The "
        "stele is the inner tissue that loads nutrients into the xylem. The xylem moves the "
        "nutrients to the shoot. The H<sup>+</sup>-ATPases in the stele stop." +
        _c("dwc-colmer-2010-ion-transport") + "</p><p>The plant absorbs ions, but it cannot send "
        "them to the shoot. Hypoxia also closes the aquaporins and causes the stomata to close. As "
        "a result, the plant moves less water." + _c("dwc-tan-2018-aquaporins") +
        "</p><p>The plant shows the symptoms of a nutrient deficiency and a small wilt, but the "
        "tank has a correct feed. Subsequently, the roots become brown and lysis occurs." +
        _c("dwc-drew-1997-hypoxia"))),
    callout("tip", "A check with no cost",
      p("Examine this condition. The EC and pH are on target, but a deficiency symptom does not "
        "change when you correct the feed. In this condition, use the DO meter and the thermometer "
        "first. Do this before you apply other nutrients.")),
  ]})

# 4 --------------------------------------------------------- the aeration paradox
SECTIONS.append({"id": "aeration-paradox", "kicker": "Aeration rate has a ceiling", "title": "Aeration limits and dissolved oxygen",
  "blocks": [
    lead("This section can change how you operate your system more than the other sections can. "
         "Aeration supplies oxygen, which is good. Aeration also supplies <em>movement</em> of the "
         "water, which is not good. At rates that are more than moderate, the bad effect of the "
         "movement is larger than the good effect of the oxygen."),
    p("A test shows this clearly. The test used deep-flow hydroponics at aeration rates of 0 to 2 "
      "L/min. Weak movement of the solution (not strong movement) made the iron uptake much less, "
      "and it caused chlorosis in sunflower and corn. The same nutrient solution at the same pH, in "
      "a medium of peat, gave the plants sufficient iron and chlorophyll. In tomato, the effect was "
      "small. The species are different." + _c("dwc-langenfeld-2025-agitation-iron")),
    callout("key", "Aeration removes the chemical layer that the roots make for nutrient uptake",
      p("A root does not only absorb the material that is in the bulk solution. The root makes a "
        "thin boundary layer around the root, and the solution in this layer does not move. The "
        "root changes the chemistry of this layer. The root releases protons to decrease the pH in "
        "the layer. It also releases reductants and chelators to make iron available.</p><p>This "
        "layer is <em>the nutrient uptake system of the plant</em>. The bubbles mix the layer into "
        "the bulk solution. When you increase the aeration, you add oxygen and you also remove the "
        "boundary layer that the root made to absorb nutrients." +
        _c("dwc-langenfeld-2025-agitation-iron"))),
    figure(D.boundary_layer(), 7,
      "This figure is the most important figure in this paper. Left: weak flow. The layer stays in "
      "position, the root decreases the pH in the layer, and iron is available. Right: the same "
      "root in the same solution with a higher air flow. The layer is not there. The root must use "
      "the chemistry of the bulk solution, and it cannot change this chemistry." +
      _c("dwc-langenfeld-2025-agitation-iron")),
    p("There is a second mechanism. Strong aeration removes dissolved CO<sub>2</sub> from the "
      "solution. Carbonic acid has an effect on the pH of the solution. When the aeration removes "
      "the CO<sub>2</sub>, the pH increases.</p><p>In a deep-water-culture aquaponics test, the "
      "plants with strong aeration gave <strong>29% less</strong> yield at harvest than the control "
      "plants with no aeration. In all the treatments, the dissolved oxygen was always 5 mg/L or "
      "more. Thus oxygen was not the limiting factor. The authors gave the pH change that came with "
      "the aeration as the cause of the smaller yield." + _c("dwc-bodenmiller-2017-aeration")),
    p("The next task is to find the correct rate. Two sources independently give almost the same "
      "number. Thus you can be more sure of this number than of the other numbers in this paper."),
    grid([
      card("From tests",
           p("A zero-discharge hydroponic system holds the DO near saturation. The aeration is at a "
             "low rate of approximately <strong>100 mL&#183;min<sup>-1</sup> for each "
             "liter</strong> of solution. The minimum depth of the solution is 20 cm (8 in). "
             "Sufficient depth makes the concentrations stable and decreases the root density. The "
             "low rate of aeration makes the concentrations more equal and does not cause damage to "
             "the rhizosphere." + _c("dwc-langenfeld-2024-zero-discharge")), tag="100 mL/min/L"),
      card("From the manufacturer",
           p("A manufacturer's RDWC procedure gives <strong>one circular air stone of medium size, "
             "5 &times; 5 cm (2 &times; 2 in), for each 30 L (7.9 gal) bucket</strong>. The "
             "procedure tells you to put the air stone at the bottom, approximately 2.5 cm (1 in) "
             "from the wall. The procedure also gives this instruction: <em>do not</em> put the air "
             "stone directly below the net pot, because &lsquo;too much turbidity can cause severe "
             "damage to new roots&rsquo;." + _c("dwc-athena-rdwc-2024")),
           tag="1 stone / 30 L"),
    ], cols=2),
    callout("note", "Calculate the numbers",
      p("For a 30 L (7.9 gal) bucket at 100 mL&#183;min<sup>-1</sup>&#183;L<sup>-1</sup>, the "
        "necessary air flow is approximately 3 L/min. For the operating volume of approximately 19 "
        "L (5.0 gal) and not the size of the bucket, the necessary air flow is approximately 1.9 "
        "L/min. One circular air stone of medium size, at a usual manifold pressure, has a flow of "
        "2&ndash;4 L/min.</p><p>Thus the number from the paper and the specification of the "
        "manufacturer give the same equipment. The paper measured iron chlorosis. A grower looked "
        "at root damage. The two sources found the same limit from opposite directions.")),
    figure(L.zones("Aeration rate: the window is small, and most growers use more", 0, 400,
            [(0, 40, L.REDL, "Too low: hypoxia"),
             (40, 160, L.GL, "The window"),
             (160, 400, L.AMBL, "Too much: rhizosphere removed, less CO2, pH increases")],
            unit="",
            note="Air flow in mL/min for each liter. The window is at approximately 100. Most hobby growers are far to the right."), 8,
      "Growers frequently think that more aeration gives more safety. Thus they use too much air. "
      "The data show that a high rate has a different problem. The problem shows as an iron "
      "deficiency, and more feed does not correct it."),
    callout("tip", "The position of the air stone is a control",
      p("Put the air stone at the bottom of the bucket and at a distance from the wall. Then the "
        "bubbles move up around the root mass and not through it. A stone directly below the net "
        "pot causes the part of the plume with the highest shear to move straight through the new "
        "root tips. These root tips break easily. The air volume is the same, but the result is "
        "very different." + _c("dwc-athena-rdwc-2024"))),
    figure(D.airstone_placement(), 9,
      "The equipment is the same and the air volume is the same, but the result is the opposite. In "
      "the left bucket, the plume moves through the root mass. In the right bucket, the plume moves "
      "up along the root mass." + _c("dwc-athena-rdwc-2024")),
    photo(f"{IMG}/06-airstone.jpg",
      "The correct result in the water is small bubbles that move up near the wall and around the "
      "roots. It is not a plume with strong turbulence through the middle of the roots.", model=GPT),
    p("The primary good property of nanobubble equipment, compared with usual air stones, is that "
      "it supplies gas without a plume of bubbles. A usual air stone gives you the oxygen supply "
      "and the mechanical movement of the water together. Nanobubble equipment does not.</p><p>A "
      "test compared irrigation at 5 mg/L with irrigation from microbubbles and nanobubbles at 15 "
      "and 30 mg/L. The two higher values gave a larger root volume and a higher yield. The "
      "rhizosphere also had a higher number of species of bacteria." +
      _c("dwc-wang-2024-mnb-microbiome") + " Reviews in controlled environment agriculture show "
      "nanobubbles primarily as a method to keep sufficient oxygen in the root zone for beneficial "
      "microbes." + _c("dwc-mamun-2025-onb-health")),
  ]})

# 5 -------------------------------------------------------------------- ORP
SECTIONS.append({"id": "orp", "kicker": "The quantity that ORP measures", "title": "How to read an ORP value",
  "blocks": [
    lead("Oxidation-reduction potential (ORP) is the measurement that growers read incorrectly more "
         "frequently than the other measurements in water culture. A platinum electrode in the "
         "reservoir gives a voltage in millivolts. The voltage is the balance between oxidizers and "
         "reductants in the solution. It is important to read ORP correctly, because the correct "
         "reading changes the task that you do."),
    defterm("ORP / redox potential",
      "The voltage, in millivolts, of an inert electrode of platinum in the solution. The "
      "measurement uses a reference electrode. The voltage shows the balance between the oxidizers "
      "and the reductants. It also shows if the solution accepts electrons or gives electrons."),
    p("Most growers read ORP incorrectly at this point. <strong>When you increase the dissolved "
      "oxygen, the ORP always increases, but almost none of the ORP change is the effect of oxygen "
      "on the electrode.</strong> Each part is important.</p><p>Growers who hear &lsquo;ORP is not "
      "an oxygen measurement&rsquo; then see the ORP increase by 200 mV when they change to an "
      "oxygen concentrator. These growers think that the information was incorrect. The information "
      "was not incorrect. The change occurs in the water and not at the electrode."),
    p("The O<sub>2</sub>/H<sub>2</sub>O redox couple has a large standard potential on paper, but "
      "it accepts and gives electrons very slowly at a platinum surface. In electrochemistry, the "
      "exchange current density of this redox couple is very low. Two results follow.</p><p>First, "
      "the electrode is not in equilibrium with the oxygen. At pH 5.8, an oxygen electrode in full "
      "equilibrium has approximately <strong>690 mV</strong> against a silver/silver-chloride "
      "reference electrode. Measurements in reservoirs are less than this value by a large number "
      "of millivolts.</p><p>Second, the <em>direct</em> effect of the oxygen concentration is "
      "small, and you can calculate it easily."),
    callout("key", "Calculate before you give oxygen as the cause of an ORP change",
      p("The Nernst slope for a redox couple with four electrons is 59.16 &divide; 4 = <strong>14.8 "
        "mV for each decade</strong> of oxygen partial pressure. A decade is a change of ten times. "
        "The change from air (partial pressure of O<sub>2</sub> 0.21 atm) to a concentrator with "
        "approximately 93% O<sub>2</sub> is 0.65 of a decade. The maximum direct effect is "
        "<strong>approximately 10 mV</strong>.</p><p>If your ORP changes by much more than this "
        "maximum, oxygen did not cause the change directly. Something in the water changed. This "
        "change in the water is usually the more important fact.")),
    callout("evidence", "A report from a grower: 220-260 mV on air, approximately 480 mV on an oxygen concentrator",
      p("A grower who used nanobubble equipment measured an ORP of <strong>220-260 mV</strong> with "
        "air only. The system usually gave good results. But new reservoirs with new clones that "
        "the grower transplanted had <em>Pythium</em> and cyanobacteria again and again, and the "
        "biofilm stayed.</p><p>One sign was important: <em>the roots stayed up in the expanded clay "
        "and did not go into the water.</em> The grower changed the same system to an oxygen "
        "concentrator. Then the ORP stayed at approximately <strong>480 mV</strong>, the biofilm "
        "almost stopped, and the roots went into the water.")
      + p("This change is approximately 240 mV. The maximum effect that you calculate above is "
          "approximately 10 mV. The other approximately 230 mV is not the effect of oxygen on the "
          "electrode. The reservoir changed.</p><p>At 220-260 mV, the water had a large load of "
          "reduced organic carbon. The microbes in the water had active metabolism with no oxygen "
          "or with a low oxygen content. These reductants <em>are</em> fast redox couples with good "
          "poise, and they kept the electrode at a low voltage. The large quantity of oxygen caused "
          "oxidation of this load. It also made the group of microbes that made the load much "
          "smaller. When you remove the reductants, the electrode increases to a much higher mixed "
          "potential.")
      + p("Thus the ORP change is correct and important, and you can do a task because of it. It is "
          "not a measurement of oxygen. The ORP value shows how clean the water is. The oxygen made "
          "the water more clean, and the ORP value showed this change. To show this type of change "
          "is the correct use of ORP.")),
    callout("note", "A second pathway: the test results do not agree",
      p("Tests show that the interfaces of microbubbles and nanobubbles make hydroxyl radicals "
        "without a catalyst. The cause is a high concentration of hydroxide and the electric field "
        "at the interface." + _c("dwc-yang-2025-microbubble-ros") + " Tests with a spin trap found "
        "signs of radicals in water with microbubbles, months after the treatment." +
        _c("dwc-takahashi-2021-nb-radicals") + "</p><p>But a careful test found no hydroxyl radical "
        "from oxygen nanobubbles in usual conditions. The test also showed that a fluorescent "
        "probe, which many tests use, shows a radical when there is no radical. The cause is that "
        "the surface of the bubble has a high concentration of protons." +
        _c("dwc-chae-2023-nb-ros-null") + " Think of a radical effect as a small effect that tests "
        "do not show. The mechanism above, with removal of reductants, is a sufficient cause for "
        "the results that growers see. It does not use unusual chemistry.")),
    callout("key", "A platinum electrode in a dilute solution gives a mixed potential",
      p("A careful test on waters from the environment calculated the redox potential independently "
        "for each of six different redox couples in the same water. The difference between the six "
        "values was up to <strong>1200 mV</strong>. The authors found that, in dilute solutions "
        "with low concentrations of redox-active species, the platinum voltage is a mixed "
        "potential. It gives only approximate numbers, and you cannot use it to calculate the "
        "speciation." + _c("dwc-stefansson-2005-redox") + " A hydroponic reservoir is this type of "
        "solution.")),
    figure(D.orp_mixed_potential(), 10,
      "Each redox-active species in the reservoir changes the voltage of the electrode in the "
      "direction of the voltage of that species. A species that accepts and gives electrons fast "
      "has a larger effect. The meter shows the mixed result. Dissolved oxygen has a very small "
      "effect." + _c("dwc-stefansson-2005-redox")),
    figure(L.hbars("The causes of ORP changes in a nutrient reservoir",
            [("Hypochlorous acid dose", 100), ("Hydrogen peroxide dose", 85),
             ("Oxygen - INDIRECT", 78), ("Iron redox state", 55),
             ("Reduced organic load", 45), ("Respiration of microbes", 40),
             ("pH (59 mV/unit)", 35), ("Oxygen - DIRECT on Pt", 8)], unit="",
            note="Size of the effect on the reading. Oxygen is in the chart two times, and the two entries are different."), 11,
      "Most ORP problems stop when growers know this difference. The <em>direct</em> effect of "
      "oxygen on the electrode is smaller than all the other effects on the chart. The maximum is "
      "approximately 10 mV. The <em>indirect</em> effect of oxygen is one of the largest effects. "
      "Oxygen causes oxidation of the reduced organic load, and it makes the group of anaerobic "
      "microbes that kept the reading low smaller. Growers see this effect." + _c("dwc-suslow-2004-orp") +
      _c("dwc-stefansson-2005-redox")),
    p("The second important fact is that <strong>you cannot use an ORP value without the pH "
      "value</strong>. Most redox couples in the environment use protons when they accept "
      "electrons. The Nernst equation gives the correct result. At 25 &deg;C (77 &deg;F), the "
      "voltage changes by approximately <strong>59 mV for each pH unit</strong>, and it decreases "
      "when the pH increases."),
    callout("note", "An example from a grower",
      p("A grower measured a change of the pH from 6.0 to 5.8 in one day. In the same day, the ORP "
        "changed from 476 to 482 mV. Calculate the number to find if the chemistry changed. When "
        "the pH decreases by 0.2 units, the voltage of a redox couple that uses protons increases "
        "by approximately 0.2 &times; 59 = <strong>12 mV</strong>.</p><p>The measured change was +6 "
        "mV. The sign is the same, and the size is approximately half. The &lsquo;ORP climb&rsquo; "
        "was mostly the pH change that the ORP showed. The redox chemistry possibly changed by a "
        "small value in the <em>down</em> direction. If you record the ORP without the pH, you get "
        "this type of incorrect trend.")),
    p("The third important fact is about a frequent problem. A probe gets a stable value in the "
      "reservoir after some hours, but it gets a stable value in a calibration standard after some "
      "minutes."),
    defterm("Poise",
      "A solution has good <strong>poise</strong> when it contains a redox couple at a sufficient "
      "concentration. The redox couple accepts and gives electrons fast, and the electrode gets its "
      "voltage quickly and keeps it. A solution with low poise has no such redox couple. As a "
      "result, the voltage of the electrode changes slowly for some hours to a mixed potential with "
      "no clear value."),
    callout("tip", "Two minutes for a calibration standard, six hours for your reservoir",
      p("Manufacturers <em>make</em> calibration standards with a high poise. ZoBell's solution and "
        "quinhydrone are examples. They contain a fast redox couple at a concentration in the "
        "millimolar range. Thus the electrode gets its voltage quickly.</p><p>A nutrient solution "
        "that is clean, has a high oxygen content and has a low organic content is the opposite. It "
        "has almost no redox-active compounds. Thus a probe can get a stable value only after some "
        "hours, after you start it again or put it in the solution again. The probe shows the "
        "condition of the solution correctly. This condition is good for a mineral hydroponic "
        "system." + _c("dwc-stefansson-2005-redox"))),
    p("These facts do not show that ORP is not important. ORP is an <strong>indicator of the "
      "sanitizer and of how clean the water is</strong>. When you use ORP for this task, it is very "
      "important. ORP is the usual control value to disinfect with hypochlorous acid in produce "
      "handling. In this task, ORP gives the value for the free available chlorine faster than a "
      "concentration test does." + _c("dwc-suslow-2004-orp")),
    p("A manufacturer's RDWC procedure uses ORP for this task. The procedure gives three zones. For "
      "each zone, it gives a smell as a second check:" + _c("dwc-athena-rdwc-2024")),
    table(["Zone", "Condition of the water", "Smell", "Result"], [
      ["<strong>Anaerobic</strong>", "The ORP is low. The reduced organic load and anaerobic "
       "metabolism are the primary effect. A report from a grower of an air-stone system with "
       "biofilm that stayed gave <strong>220-260 mV</strong> for this zone.",
       "The smell of rot", "Pathogen growth and root rot. The roots do not go into the water."],
      ["<strong>Safe</strong>", "The water is clean. An oxidizer is in the water, but its concentration does not increase.",
       "The smell of clean bean sprouts", "The roots are white, and the uptake is usual."],
      ["<strong>ORP shock</strong>", "The dose of the oxidizer is too large, and the environment has very high oxidation.",
       "The smell of chlorine", "The roots cannot absorb nutrients correctly."],
    ], cls="compact", caption="The three ORP zones and their smells. The smell test is frequently "
      "faster and more accurate than the probe, and you do not calibrate it."),
    callout("warn", "ORP shock shows the same symptoms as a nutrient deficiency",
      p("<em>If you use too much hypochlorous acid in RDWC, the oxidation is very high, and the "
        "nutrient uptake decreases.</em> Hypochlorous acid is safe for plant tissue. The "
        "manufacturer writes that the effect &lsquo;appears as a nutrient deficiency, yellowing or "
        "dry, crusty foliage&rsquo;.</p><p>The roots touch the solution for a long time, and a "
        "large volume of solution touches them." + _c("dwc-athena-rdwc-2024") +
        " Thus an RDWC system must have a much lower ORP than other methods. Hypoxia and too much "
        "oxidation are two different faults in the root zone. The two faults cause yellow leaves. "
        "If you select the cause without a check, you can cause a crop failure.")),
    grid([
      card("If you add no chemical oxidizer",
           p("A high and stable ORP usually shows that your solution is clean and has no reduced "
             "organic load. No oxidizer is in the solution, thus no ORP shock can occur. A high "
             "number does not show a problem, and you can read it as an indicator of hygiene. The "
             "<em>low</em> end is the problem. Examine a reading that is low and decreases, with no "
             "oxidizer in the system. It shows that the reduced organic load increases and the "
             "reservoir becomes anaerobic.")),
      card("If you add hypochlorous acid or peroxide",
           p("In this condition, the ORP shows the quantity of oxidizer that stays in the solution, "
             "and the shock zone of the manufacturer is a risk. The ORP value must have a maximum "
             "limit and a recorded pH value with it. If the ORP is too high, decrease the dose of "
             "oxidizer. Do not add other products.")),
    ], cols=2),
    callout("tip", "The position of the probe: keep it away from the bubbles",
      p("A probe in a plume of bubbles measures the bubbles and the water. This effect is the usual "
        "cause of a DO reading that changes between 15 and 25 mg/L. Put the probes in a bottle with "
        "holes or in a stilling tube. The water in the bottle or tube has low turbulence. "
        "Circulation supplies the water, but the bubbles from the air stone do not go into the "
        "bottle or tube.</p><p>Biofilm on the surface of the electrode changes a platinum reading "
        "by a large number of millivolts." + _c("dwc-sholikah-2025-pt-electrode") +
        " Clean the probe regularly. Do not clean it only when you find a problem.")),
    photo(f"{IMG}/10-probe-reading.jpg",
      "Calibration is not optional in water culture. A calibrated probe gives information that you "
      "can use to find the cause. A probe that you do not calibrate gives only an estimate. A probe "
      "with drift and a dirty probe show the same value on the display.", model=GPT),
  ]})

# 6 ------------------------------------------------------------------- iron
SECTIONS.append({"id": "iron", "kicker": "Chemistry", "title": "Iron chelates and chlorosis",
  "blocks": [
    p("Iron is the element that causes the most problems in water culture. The plant must have a "
      "larger quantity of iron than of the other micronutrients. In water with oxygen, almost no "
      "iron dissolves when the pH is higher than mildly acidic. Iron stays available only because "
      "we put it in a chelate."),
    defterm("Chelate",
      "An organic molecule that holds a metal ion at more than one point at the same time. The "
      "chelate holds the ion in solution, and the ion does not precipitate or change to other "
      "compounds. Fertilizer iron is almost always a chelate: Fe-EDTA, Fe-DTPA or Fe-EDDHA."),
    p("The three chelates that growers use frequently are not interchangeable. They are different "
      "in the maximum pH at which they can hold iron. They are also different in how strongly they "
      "keep their iron when other metals try to replace it."),
    table(["Chelate", "Maximum pH for use", "Properties", "Cost"], [
      ["<strong>Fe-EDTA</strong>", "approximately 6.0&ndash;6.5",
       "The chelate becomes not stable at a pH of more than 6.5. It releases the iron, and the iron "
       "becomes FePO<sub>4</sub> and Fe(OH)<sub>3</sub>, which do not dissolve. Copper, zinc and "
       "manganese can also replace the iron in the ligand." + _c("dwc-ilyas-2025-fe-chelates"),
       "Low"],
      ["<strong>Fe-DTPA</strong>", "approximately 7.0&ndash;7.5",
       "The maximum pH is higher than for EDTA by a large difference. The chelate is the usual "
       "selection when you cannot keep the pH constant or when the solution has high oxidation.", "Middle"],
      ["<strong>Fe-EDDHA</strong>", "approximately 9.0 or more",
       "The chelate holds iron in alkaline conditions. The data show that it is stable at different "
       "pH values and for different times." + _c("dwc-klem-2021-eddha") + " It makes the solution "
       "dark red.", "High"],
    ], caption="Usual maximum pH values for the three fertilizer iron chelates. The ceiling is not "
      "a sharp limit. Degradation occurs gradually and increases with time."),
    figure(L.zones("The pH at which each iron chelate holds its iron", 3.0, 9.5,
            [(3.0, 6.5, L.AMBL, "Fe-EDTA"), (6.5, 7.5, L.GL, "DTPA range"),
             (7.5, 9.5, L.BLUL, "EDDHA only")], unit=" pH",
            note="A typical RDWC system has a pH of 5.8-6.3, which is near the top of the EDTA range."), 12,
      "The pH of a recirculating system can change slowly to 6.5. This pH is in the good range for "
      "plants, but it is not in the good range for Fe-EDTA." + _c("dwc-ilyas-2025-fe-chelates")),
    callout("note", "The method of a manufacturer for this problem",
      p("One mineral nutrient set that many growers use divides the iron between two products. The "
        "primary product supplies the iron as <strong>Fe-EDTA</strong>, together with calcium "
        "nitrate and the micronutrients that have EDTA as the chelate. The bloom product supplies "
        "the iron as <strong>Fe-DTPA</strong>." + _c("dwc-athena-proline") + "</p><p>Compare this "
        "with the pH schedule. The pH starts at approximately 6.2&ndash;6.3 and decreases to 5.8 "
        "during the flowering stage." + _c("dwc-athena-rdwc-2024") + " This method is good. The "
        "EDTA supplies the iron at a low cost in the acid part of the range. The DTPA gives "
        "headroom in the first part of the crop, when the pH is higher, and for drift of the pH.")),
    callout("warn", "Two different causes, one symptom",
      p("Interveinal chlorosis in new growth shows as yellow tissue between green veins on the new "
        "leaves. It is the usual sign of iron deficiency. In water culture, it has a minimum of two "
        "causes. The corrections for the causes are opposite:" + ul(["<strong>Defective chelate.</strong> The pH changed to a value higher than the "
              "maximum pH of your chelate. Correct the pH, or change to a stronger chelate.",
              "<strong>Rhizosphere removal.</strong> The aeration removes the boundary layer that "
              "the root uses to get iron." + _c("dwc-langenfeld-2025-agitation-iron") +
              " <em>Decrease</em> the aeration."], "tight") + "<p>More iron does not correct the "
        "two causes. For the second cause, more iron also makes the incorrect operation of the "
        "system harder to see.</p>")),
    photo(f"{IMG}/05-chlorosis.jpg",
      "Interveinal chlorosis on new growth. The blade is pale, the veins are dark green, and the "
      "leaves at the bottom of the plant have no symptoms. The symptom shows that the problem is "
      "iron. The symptom does not show if the cause is the pH or the aeration, and the corrections "
      "for these two causes are opposite.", model=GPT),
    p("Tests on other iron sources continue. A test on corn used Schiff-base complexes of Fe(II). "
      "These compounds are stable at alkaline pH. They gave a higher dry weight of roots and shoots "
      "than Fe-EDTA and Fe-EDDHA." + _c("dwc-mirbolook-2023-fe-source") + " But they are not "
      "available for production at this time. At this time, the controls are pH control and "
      "selection of the chelate."),
  ]})

# 7 ---------------------------------------------------------------- organics
SECTIONS.append({"id": "organics", "kicker": "Organics and oxygen headroom", "title": "Organic inputs in recirculating reservoirs",
  "blocks": [
    p("Growers have opposite methods. Some add kelp, fulvic acid or inoculants of microbes to DWC, "
      "and some do not. Each group is sure that it is correct. The results of each group are "
      "correct. The difference is in the limiting factor of the system of <em>each</em> group."),
    callout("key", "The mechanism for the two positions",
      p("Each gram of reduced organic carbon that you add to a reservoir is feed for heterotrophic "
        "bacteria. These bacteria increase in number. Their respiration uses dissolved oxygen. In "
        "water treatment, you add <strong>biochemical oxygen demand (BOD)</strong>. Thus you use a "
        "part of your aeration for the microbes and not for the roots. The organic load also "
        "decreases the ORP when the reduced organic load increases.")),
    p("The position against organic inputs is this. The mechanism is correct. Because of this "
      "mechanism, the usual instruction for mineral hydroponics is to keep the solution clean. A "
      "manufacturer's RDWC procedure does more. The schedule adds a product with hypochlorous acid "
      "during the crop, and thus the organic load does not increase. The manufacturer also writes "
      "that more than one cleaning cycle can be necessary for pipes that had organic inputs before, "
      "to remove organic particles." + _c("dwc-athena-rdwc-2024")),
    p("The other position also has good data. Some growers use a high dissolved oxygen value, for "
      "example with nanobubble systems at 15&ndash;20 mg/L. These growers have good results with "
      "fulvic acid and biological inputs, and they have no root disease. This agrees with the "
      "mechanism: BOD is a problem of <em>rate</em>. If your oxygen supply rate is two to three "
      "times the rate of a usual air stone, you can have a large organic load. A usual system has "
      "hypoxia with this load.</p><p>Tests show that humic substances and fulvic acid have "
      "biostimulant effects on the growth of lateral roots and on nutrient-use efficiency." +
      _c("dwc-canellas-2015-humic") + " Reviews of nanobubble methods with oxygen show that a high "
      "DO is the condition that lets beneficial microbes do their tasks in the root zone." +
      _c("dwc-mamun-2025-onb-health")),
    grid([
      card("The data show",
           p("The group of microbes in a recirculating system is not always a risk. A test used "
             "deep-water-culture lettuce during five cycles with the same solution. The groups of "
             "bacteria changed by a large quantity between cycles. Some groups had a relation to "
             "the expression of plant defense genes. The authors think that groups in the solution "
             "that activate plant defenses can be a good method to decrease Pythium without "
             "chemical products." + _c("dwc-kenderdine-2026-recirc"))),
      card("More than the data show",
           p("The plant has a stronger effect on the group of microbes at its roots than the water "
             "in the reservoir has. A test compared sources in hydroponics and aquaponics. The "
             "groups of microbes on the roots were almost the same for roots of one plant. They "
             "were not the same for roots that had the same upstream product." +
             _c("dwc-lobanov-2022-plants-dictate") + " You have less control of the microbes on the "
             "roots than the labels on the products show.")),
    ], cols=2),
    callout("tip", "Make a decision with data and not with a group",
      p("Find the dissolved-oxygen headroom of your system. If your system is near air saturation "
        "with air stones, at 8&ndash;9 mg/L, you have almost no headroom. Keep the reservoir "
        "mineral and clean.</p><p>If your system uses an oxygen concentrator or nanobubble "
        "equipment at 15&ndash;20 mg/L, you have headroom. You can use some of the headroom for "
        "biology.</p><p>In each condition, measure the DO before and after you add an organic "
        "input. If the DO decreases and stays low, the microbes use your headroom.")),
    callout("warn", "A problem to prevent",
      p("Do not read the ORP change as information about oxygen. Products with fulvic acid or humic "
        "substances frequently contain iron and chelate compounds. Thus the ORP can change when you "
        "add them. First, the ORP decreases when the reduced organic carbon goes into the water. "
        "Then the ORP changes to a different value that stays, when the iron equilibrium becomes "
        "stable again. The cause is a change in the chemistry of a chelate system with more "
        "compounds.")),
    p("If you want to use biology, inoculants for one target have better data than general organic "
      "feeds. A test used <em>Bacillus subtilis</em> and <em>Pseudomonas fluorescens</em> together. "
      "The two bacteria together decreased <em>Pythium aphanidermatum</em> more than the effect of "
      "one of the bacteria plus the effect of the other. They increased the expression of defense "
      "genes, and the survival increased to 83%." + _c("dwc-rashad-2024-biocontrol") +
      " Biocontrol with <em>Pseudomonas</em> in many crops can give the same result as chemical "
      "fungicides. But the results in production are much less sure than the results in the "
      "laboratory." + _c("dwc-alattas-2024-pseudomonas")),
  ]})

# 8 ----------------------------------------------------------------- pathology
SECTIONS.append({"id": "pathology", "kicker": "Type of problem", "title": "Root rot: oxygen stress and pathogen risk",
  "blocks": [
    lead("The data on pathology in water culture give one primary result. Low dissolved oxygen and "
         "<em>Pythium</em> root rot are related risks. They are one problem with one pathway: the "
         "oxygen condition of the root zone."),
    p("A review of hydroponic systems, plant physiology and oomycete pathology shows this directly. "
      "As the root mat becomes larger, the passive aeration decreases, and the root zone has "
      "hypoxia. Hypoxia damages the root membranes and changes the exudates that the roots release. "
      "<em>Pythium</em> zoospores move to the changed exudates and attach to the roots.</p><p>The "
      "zoospores also use these exudates to change from the biotrophic phase to the necrotrophic "
      "phase. In the biotrophic phase, the pathogen is in the plant and does not show. In the "
      "necrotrophic phase, the pathogen kills the tissue." + _c("dwc-scott-2026-do-pythium")),
    figure(L.flow("Root rot: the sequence",
            [("Less oxygen", "temperature is high, root mat is large, or aeration stops"),
             ("Membrane damage", "Hypoxia damages the roots, and the exudates change."),
             ("Zoospores attach", "changed exudates are a chemical signal"),
             ("Necrotrophic phase", "a signal makes roots brown, then the pathogen kills tissue"),
             ("Result", "root function stops. The plant gets less carbon, in total.")],
            note="Each arrow is downstream of the first step. If you decrease only the pathogen, the sequence starts again."), 13,
      "Root rot in water culture is not frequently only a hygiene problem. It is usually an oxygen "
      "problem, and a pathogen that is in all environments uses the problem." +
      _c("dwc-scott-2026-do-pythium") + _c("dwc-sutton-2006-pythium")),
    photo_sequence("The sequence at the root",
      [("Good", f"{IMG}/03-roots-healthy.jpg"), ("Root rot", f"{IMG}/04-roots-rot.jpg")],
      "Left: white roots, thin, with many branches and a shiny surface. Right: the same root mass "
      "after the sequence of root rot. The root mass is light brown, with a root mat and slime in "
      "the inner part. The outer edge continues to have white roots, where oxygen continues to get "
      "to the roots. This white edge is the sign. The problem is a gradient of oxygen, and it is "
      "not an infection that came at one time.", model=GPT),
    callout("key", "The task with the largest effect",
      p("The primary review of <em>Pythium</em> in hydroponic crops gives a result that is "
        "different from the method of most systems. Methods that disinfect the nutrient solution "
        "<em>in the pipes, away from the crop,</em> frequently have a small effect on epidemics. A "
        "treatment that decreases the pathogen <strong>in the roots and root zone</strong> has an "
        "effect." + _c("dwc-sutton-2006-pythium") + " A UV sterilizer on the return line does less "
        "than you think, if the root zone is warm and has not sufficient oxygen.")),
    p("Stress from the environment is the other part. The same review finds that roots with stress "
      "get a <em>Pythium</em> infection more easily. The review also shows that an infection makes "
      "the growth of leaf area much slower, and the plant gets less carbon. The efficiency of "
      "photosynthesis for each unit of leaf area does <em>not</em> decrease by a large quantity." +
      _c("dwc-sutton-2006-pythium") + " The plant does not show symptoms, but it makes a smaller "
      "canopy than a plant without infection. When the plant clearly shows a problem, the plant is "
      "behind by some weeks of growth."),
    callout("tip", "The sign before the roots become brown",
      p("In water culture, one sign is more important than a probe. It is the first sign: "
        "<strong>the roots stay up in the expanded clay and do not go into the solution.</strong> "
        "If the roots do not go into the water, the water is not good for the roots. The water is "
        "too warm, it has not sufficient oxygen, or it has a load of microbes that the roots stay "
        "away from. Growers who correct the oxygen supply find that the roots then go into the "
        "water. Read this sign as an alarm for the root zone and not as &lsquo;slow "
        "establishment&rsquo;.")),
    p("Chemical oxidizers have an effect as a treatment, and they also have a bad effect. A test "
      "added hydrogen peroxide to hydroponic solution at 0&ndash;400 mg/L. The peroxide caused root "
      "damage that you can see in each crop in the test. Cucumber was the crop with the most "
      "damage. The concentrations that decrease the pathogen were at the threshold for damage or "
      "more than the threshold." + _c("dwc-eicher-sodo-2020-h2o2") + "</p><p>In a test with "
      "ebb-and-flow irrigation, high peroxide rates made the growth of lettuce smaller, and no rate "
      "decreased algae." + _c("dwc-hendrickson-2022-h2o2")),
    callout("warn", "Peroxide as the first step",
      p("Do not add peroxide to the reservoir at the first sign of brown roots. Many growers do "
        "this, but it usually causes more problems.</p><p>The tissue of the roots is in bad "
        "condition, and the peroxide causes more damage to it. The peroxide decreases to zero in "
        "some hours, and thus its effect does not stay. The peroxide has an effect only on the "
        "symptom. The cause is warm water with not sufficient oxygen, and the peroxide does not "
        "change it.</p><p>First, do a check of the thermometer and the air manifold. A product with "
        "hypochlorous acid at a small continuous dose is a better regular method than peroxide "
        "shocks. The manufacturer gives this schedule: a large dose at fill and change-out, then a "
        "small continuous dose during the crop." + _c("dwc-athena-rdwc-2024"))),
  ]})

# 9 --------------------------------------------------------------- temperature
SECTIONS.append({"id": "temperature", "kicker": "Temperature first", "title": "Solution temperature",
  "blocks": [
    p("If you use only one control from this paper, use this control. The reservoir temperature "
      "changes four values at the same time. They are the oxygen supply, the oxygen demand, the "
      "growth rate of pathogens and how stable the pH is. No other control that you can adjust "
      "changes as many values at the same time."),
    p("The data from tests are clear. A test decreased the temperature of a recirculating "
      "hydroponic solution at four setpoints, from 33 &deg;C (91 &deg;F) to 22 &deg;C (72 &deg;F). "
      "The DO increased in the feed and in the drain. The roots used <em>more oxygen</em>, and the "
      "test measured this. Each measurement of growth, yield and quality was better. The test had "
      "three seasons of crops in two years." + _c("dwc-alrawahy-2019-rzt") + "</p><p>The second "
      "result is important. When the temperature decreased, the respiration of the roots did not "
      "decrease. It increased, because oxygen was no longer the limiting factor."),
    figure(D.supply_demand(), 14,
      "These two curves show that temperature is the primary control. Each degree of temperature "
      "increase removes oxygen from the water. At the same time, the root uses more oxygen." +
      _c("dwc-benson-krause-1984") + _c("dwc-alrawahy-2019-rzt")),
    p("In production, a ramp that decreases is the usual method, and not one setpoint. A procedure "
      "of a manufacturer for RDWC decreases the solution temperature in steps during the crop:" +
      _c("dwc-athena-rdwc-2024")),
    figure(L.line("RDWC solution-temperature schedule (manufacturer)",
            [("Veg", 21.1), ("Fl 1", 20.6), ("Fl 2", 20.0), ("Fl 3", 19.4), ("Fl 4", 18.9),
             ("Fl 5", 18.3), ("Fl 6", 17.8), ("Fl 7", 16.7), ("Fl 8", 16.7), ("Finish", 13.9)],
            ["VEG", "Fl1", "Fl2", "Fl3", "Fl4", "Fl5", "Fl6", "Fl7", "Fl8", "FIN"],
            ylab="°C", ymin=12, ymax=23,
            note="Warm for the new plants. Then it decreases as root mass and oxygen demand increase."), 15,
      "The ramp is not random. The root mass and the total oxygen demand increase during the crop, "
      "thus the oxygen supply must increase also. The method with the lowest cost to increase the "
      "dissolved oxygen is to decrease the temperature." + _c("dwc-athena-rdwc-2024") +
      " On the horizontal axis, VEG is the vegetative stage, each Fl label is a week of flowering, "
      "and FIN is the finish."),
    table(["Limit", "Value", "Cause of the limit"], [
      ["Do not transplant clones at less than", "18.9 &deg;C (66 &deg;F)",
       "Cold shock for a root system with a very small mass. The pH also changes when the temperature changes."],
      ["The uptake starts to decrease at less than", "16.7 &deg;C (62 &deg;F)",
       "Roots at a low temperature absorb nutrients more slowly. This temperature is the floor of the good range."],
      ["Cold finish that you select", "13.9 &deg;C (57 &deg;F) for the last approximately 10 days",
       "You accept less uptake to get more color in the flowers. Do this when the uptake is no longer important."],
      ["Zone of high pathogen growth", "more than approximately 22&ndash;24 &deg;C (72&ndash;75 &deg;F)",
       "In warm water, the DO is low and the growth of <em>Pythium</em> is fast."],
    ], cls="compact", caption="Temperature limits from a manufacturer's RDWC procedure, with the "
      "cause of each limit." + _c("dwc-athena-rdwc-2024")),
    callout("tip", "Chiller or no chiller",
      p("A room can have a temperature of more than approximately 24 &deg;C (75 &deg;F) with the "
        "lights on. In this condition, a reservoir with no insulation will have a temperature that "
        "is not good. First, put insulation on the reservoir. It has no cost, and it decreases the "
        "changes of temperature between day and night. Then, if you cannot keep the temperature in "
        "the range, use a chiller.</p><p>Aeration has a relation to temperature. A blower that "
        "moves hot room air is also a heater. Thus the air supply must be away from the canopy "
        "space. In a flower room with CO<sub>2</sub> enrichment, put the air pump out of the room." +
        _c("dwc-athena-rdwc-2024"))),
  ]})

# 10 -------------------------------------------------------------------- feed
SECTIONS.append({"id": "feed", "kicker": "Nutrition", "title": "Nutrient concentration in deep-water culture",
  "blocks": [
    p("Growers who change from coco to RDWC almost always apply too much feed at first, because the "
      "EC numbers look incorrect. The numbers are correct. Water culture uses smaller EC values, "
      "and the cause is the structure of the system."),
    callout("key", "The roots touch the solution all the time",
      p("In coco, the roots touch concentrated feed for a short time during a shot. Then the roots "
        "are in a substrate, and they use a part of the nutrients in the pore water. In DWC, all "
        "the roots touch the full volume of the solution continuously, all day and each day. For "
        "the same nutrition, a much smaller concentration is sufficient. The manufacturer writes "
        "that the EC for RDWC is less than the EC of usual feed schedules. The cause is that a "
        "large volume of solution touches the root system continuously." + _c("dwc-athena-rdwc-2024"))),
    figure(L.line("RDWC electrical-conductivity schedule (manufacturer)",
            [("Initial", 0.21), ("V2", 0.33), ("V4", 0.67), ("F1", 0.71), ("F2", 0.93),
             ("F3", 1.07), ("F4", 1.21), ("F5", 1.36), ("F6", 1.50), ("F7", 1.36), ("F8", 1.29)],
            ["Start", "V2", "V4", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8"],
            ylab="EC (mS/cm)", ymin=0, ymax=1.8,
            note="Feathering up, a peak in the second half of flower, then the EC decreases. The finish is 0-1.0."), 16,
      "The peak EC of approximately 1.5 mS/cm is approximately half the EC that many coco feed "
      "schedules use at the same stage. The plant has sufficient feed. The supply method is "
      "different." + _c("dwc-athena-rdwc-2024")),
    defterm("Feathering up",
      "A method to increase the EC gradually. You add small quantities of nutrient many times, and "
      "you do not add the nutrient in large steps. In a reservoir that all the plants use, one "
      "large dose is a shock to all the plants at the same time." + _c("dwc-athena-rdwc-2024")),
    defterm("Addback",
      "The nutrient that you add to the system through the control bucket to increase the EC to the "
      "correct value. The EC decreases continuously, because the plants absorb nutrient and because "
      "you add fresh water. In a recirculating system, the plants use the nutrients at different "
      "rates. As a result, the solution becomes <em>less balanced</em> with time, also when the EC "
      "looks correct. A change-out corrects this problem."),
    p("A test from a different source agrees strongly with the low-EC feed method. The test used "
      "closed-system hydroponics and measured the nutrients in the root zone continuously. When the "
      "test applied two times more nutrient, from 2 to 4 mS/cm, the nutrient in the solution "
      "increased. But the yield and the quality of the medical cannabis <strong>did not increase "
      "clearly</strong>.</p><p>The test also increased the phosphorus from 15 to 90 mg/L. The "
      "phosphorus concentration in the flower increased by 70%, but the yield and the quality did "
      "not increase. The authors found that cannabis can have high nutrient concentrations without "
      "damage. But more phosphorus and more fertilizer do not make the yield or the quality better." +
      _c("dwc-hershkowitz-2025-p-ec")),
    p("The pH also has a schedule. The pH decreases in steps from approximately 6.2&ndash;6.3 at "
      "fill to 5.8, and then it stays there during the flowering stage." + _c("dwc-athena-rdwc-2024") +
      " The instructions of the manufacturer tell you that the pH is the most important value to "
      "keep on target. The instructions also tell you that the pH changes quickly after an addback. "
      "Let the pH become stable before you correct it. If you correct the pH immediately after a "
      "dose, you can add too much buffer."),
    callout("note", "The type of nitrogen changes the pH, and it is not only a selection of nitrogen",
      p("Roots absorb cations and anions in different quantities. The roots keep the electrical "
        "charge balanced when they release H<sup>+</sup> or OH<sup>-</sup>. With only nitrate, the "
        "solution pH increased to approximately 8.0. With too much ammonium, the pH decreased to "
        "3.6. A correct mixed ratio kept the pH at approximately 5.8, and it gave the best yield "
        "and the best nitrogen-use efficiency." + _c("dwc-zhu-2021-nh4-no3") +
        "</p><p>If the pH increases continuously and you add acid each day, examine the ammonium "
        "fraction of your feed. Do this before you get a larger acid pump.")),
    p("Two more points are important. Potassium silicate is frequently the pH-up agent in these "
      "schedules, and it also supplies silicon. Silicon goes into the cell walls, helps the "
      "antioxidant systems and increases the tolerance to stress." + _c("dwc-hassan-2024-silicon") +
      "</p><p>In the &lsquo;finish&rsquo; phase of water culture, the EC decreases to a value near "
      "zero. This phase is very easy, compared with a substrate. Stop the addback, and the plants "
      "use the nutrients in the reservoir."),
    callout("warn", "A task that water culture cannot do",
      p("Water culture cannot do controlled drought stress in the last weeks of flower. This stress "
        "increases the cannabinoid concentration by a large quantity. It also increases the yield "
        "for each unit of area by a large quantity. Tests show this for cannabis in containers." +
        _c("dwc-caplan-2019-drought") + "</p><p>If your crop steering uses generative dryback, DWC "
        "is structurally the incorrect system. DWC is not a worse system. It is a different "
        "system.</p><p>DWC is good for a continuous growth rate in the vegetative stage. It is not "
        "good for steering with water.")),
  ]})

# 11 ------------------------------------------------------------------- build
SECTIONS.append({"id": "build", "kicker": "Assembly", "title": "DWC system: size and assembly",
  "blocks": [
    p("Most decisions for a water culture system are about headroom, because a system has no "
      "headroom unless you make it."),
    defterm("Operating volume",
      "The volume of solution in the system when the water level is directly below the planting "
      "deck. In the specification of a manufacturer, the operating volume is approximately 40 L "
      "(10.6 gal) in a 49 L (12.9 gal) module. It is approximately 19 L (5.0 gal) in a 30 L (7.9 "
      "gal) module." + _c("dwc-athena-rdwc-2024")),
    defterm("Change-out volume",
      "The operating volume minus the liquid that stays in the system when the system drains to the "
      "top of the bulkhead. Calculate it one time. In a 32-site example from a manufacturer, the "
      "operating volume is 1325 L (350 gal), and 375 L (99 gal) stays in the system. Thus a "
      "&lsquo;full&rsquo; change-out replaces 946 L (250 gal), approximately <strong>71%</strong> "
      "of the water." + _c("dwc-athena-rdwc-2024") + " A full change-out does not set the system to "
      "zero. This fact is important when the solution has an imbalance and you want to correct it."),
    steps([
      ("Make the volume large",
       "More water gives more thermal mass, more chemical buffer and more time to see a problem. "
       "Depth is also important independently. A minimum of 20 cm (8 in) of solution makes the "
       "concentrations stable and makes them more equal." + _c("dwc-langenfeld-2024-zero-discharge")),
      ("Put all the controls in a bucket with no plant",
       "Put the probes and the heater or chiller in the control bucket. Put the float valve, the "
       "circulation pump and the dose point in the same bucket. Do not use a plant site as a point "
       "of measurement. Do not let a concentrated product touch a root."),
      ("Set the aeration to the window and not to the maximum",
       "Use approximately 100 mL&#183;min<sup>-1</sup> for each liter," +
       _c("dwc-langenfeld-2024-zero-discharge") + " or one air stone of medium size for each 30 L "
       "(7.9 gal) bucket." + _c("dwc-athena-rdwc-2024") + " The manufacturer gives manifold "
       "pressures on a water-column gauge. They are approximately 6.5 kPa in the vegetative stage "
       "and 7.0&ndash;7.5 kPa in flower. Do not supply too much air."),
      ("Put the air stones in the correct position",
       "Put each air stone at the bottom of the bucket, approximately 2.5 cm (1 in) from the wall. "
       "Do not put an air stone directly below the net pot. At fill, do a check that bubbles come "
       "out of each stone at the same rate. A clogged stone causes hypoxia for one plant, and there "
       "is no sign."),
      ("Keep air pumps and blowers out of the room",
       "The air pumps and blowers are sources of heat. In a room with CO<sub>2</sub> enrichment, "
       "put them out of the room." + _c("dwc-athena-rdwc-2024")),
      ("Connect a continuous supply of RO water",
       "A float valve in the control bucket, with water from an RO manifold, keeps the water level "
       "constant automatically. If you add water by hand, the EC and the water level increase and "
       "decrease again and again. Each plant shows the effect."),
      ("Clean and prepare the media before it touches a plant",
       "Expanded clay contains dust and small particles. The procedure of the manufacturer has "
       "three steps." + _c("dwc-athena-rdwc-2024") + " Flush the expanded clay with water. Soak it "
       "in water with acid and a product with hypochlorous acid. Flush it again with water. Put the "
       "net pots in a sanitizer for a short time to remove dust and particles of plastic."),
      ("Set the crown above the water level",
       "The basal stem and the rockwool cube must stay above the solution. If they are in the "
       "solution, stem rot occurs. The solution must be at the structural ring below the planting "
       "deck. At this level, the roots get the solution easily, and the solution is not above the "
       "crown."),
    ]),
    callout("tip", "Prepare for a time with no power",
      p("At 2 a.m., the power can stop. A large volume of cool water with a high oxygen content "
        "keeps the crop in good condition for some hours. A small volume of warm water with not "
        "sufficient oxygen has a problem in one hour. For each dollar, a battery for the air pump "
        "gives more protection for the crop than a battery for almost all other equipment. The "
        "cause is that the oxygen in the water decreases faster than the other quantities in the "
        "system.")),
    figure(D.system_schematic(), 17,
      "The full loop. The plant sites have no probes, no pumps and no float valves. All the probes, "
      "doses, pumps and float valves are in one bucket with no plant. Thus no concentrated product "
      "touches a root, and you cannot use one plant site as a measurement of the system." +
      _c("dwc-athena-rdwc-2024")),
    photo(f"{IMG}/07-control-bucket.jpg",
      "A control bucket: the photo shows the pump, the float valve on the RO pipe, and the probes "
      "in a stilling tube with holes. The stilling tube keeps the probes away from the plume of "
      "bubbles.", model=GPT),
  ]})

# 12 --------------------------------------------------------------------- run
SECTIONS.append({"id": "run", "kicker": "Operate", "title": "Operation and troubleshooting",
  "blocks": [
    p("Water culture gives good results when you do a regular procedure. It gives bad results when "
      "you do tasks without a procedure. The procedure for each day is short. Do the same tasks "
      "each day, at the same time, and write the numbers."),
    grid([
      card("Each day", ul([
        "Make sure that the water level is at the operating volume and that the float valve operates.",
        "Make sure that the solution temperature is in the range for the stage.",
        "Make sure that the circulation pump operates and that the drain valve has no blockage.",
        "Make sure that the air pump operates and that bubbles come out of each stone at the same rate.",
        "Measure the pH and EC with a calibrated meter.",
        "<strong>Smell the reservoir.</strong> The smell must be clean. It must not be the smell of rot or of chlorine.",
        "Look for leaks",
      ], "tight"), tag="approximately 5 min"),
      card("Each week", ul([
        "Calibrate pH and EC probes",
        "Clean the ORP and DO probes. Biofilm causes an error that you cannot see." + _c("dwc-sholikah-2025-pt-electrode"),
        "Compare the pH and EC readings with a second meter.",
        "Examine a root mass. The roots must be white and hard, and not light brown with slime.",
        "Do a check of the inline filters.",
        "Examine the trend and not only the number for this day.",
      ], "tight"), tag="approximately 30 min"),
    ], cols=2),
    p("A change-out is the method to start the solution again. The primary task is to know when to "
      "do a change-out. A partial change-out replaces 20&ndash;50% of the solution to correct a "
      "small imbalance. A full change-out drains the system to the bulkhead, and you make the "
      "solution again." + _c("dwc-athena-rdwc-2024")),
    table(["Condition", "Task"], [
      ["Usual change-out at three weeks of the vegetative stage", "Partial change-out"],
      ["The pH changes slowly although you correct it", "Partial change-out first. If the problem stays, full change-out."],
      ["The plants absorb less nutrient, but the values are stable", "Partial change-out"],
      ["The pH increases or decreases to a value that is out of the permitted limits", "Full change-out"],
      ["To correct the pH, you must add more and more buffer each time", "Full change-out"],
      ["The values went out of range because the operator made an error", "Full change-out"],
      ["Change to the flowering stage after four or more weeks of the vegetative stage", "Full change-out"],
      ["After defoliation, or at approximately days 26&ndash;32", "Full change-out"],
      ["10&ndash;14 days before harvest", "Full change-out"],
    ], cls="compact", caption="Conditions for a change-out, from a manufacturer's procedure. An "
      "important point: <em>more and more buffer</em> is the signal that the solution has a "
      "nutrient imbalance, also when the EC and pH read correctly." + _c("dwc-athena-rdwc-2024")),
    callout("warn", "A change-out must be fast",
      p("Roots in air get stress, and damage occurs fast. Drain the system quickly. Fill it again "
        "immediately. Stop the power to the system while you do the change-out. Make the new water "
        "and set its temperature <em>before</em> you open the drain. The worst condition is an RO "
        "tank that is empty when the drain is in progress.")),
    photo(f"{IMG}/09-changeout.jpg",
      "A change-out in progress. The drain is open, and the pipe for the new water is in position. "
      "The time that the roots are in air starts when the water level decreases.", model=GPT),
    p("To find the cause of a fault, use the information from all the sections of this paper. Most "
      "water-culture faults show as one of three symptoms. Each symptom has more than one cause, "
      "and the corrections can be opposite:"),
    table(["Symptom", "Possible causes", "First check", "Frequent incorrect step"], [
      ["Interveinal chlorosis, new growth",
       "The chelate does not hold the iron above its maximum pH, or the aeration removes the rhizosphere layer.",
       "The pH record, then the aeration rate",
       "More iron"],
      ["The leaves are yellow, and the edges of the leaves are dry and hard.",
       "ORP shock because the dose of oxidizer is too large",
       "The dose rate of the oxidizer. Smell for chlorine.",
       "You think that it is a feed deficiency, and you add nutrient."],
      ["The growth is slow, there is a small wilt, and the feed is on target.",
       "Hypoxia: the stele has not sufficient oxygen before you can see root damage.",
       "The solution temperature, then the DO, then each air stone",
       "More EC"],
      ["The roots are brown with slime, and the smell is the smell of rot.",
       "Root rot, downstream of low oxygen",
       "The temperature and the aeration, and not the pathogen",
       "A peroxide shock without a correction of the oxygen"],
      ["The pH increases continuously",
       "Nitrogen with a high fraction of nitrate, or too much aeration that removes CO<sub>2</sub>",
       "The ammonium fraction of the feed, then the aeration rate",
       "Acid doses that increase each time"],
      ["The DO value changes by a very large quantity",
       "The probe is in the plume of bubbles",
       "The position of the probe. Read the value in an area with low turbulence.",
       "You think that the number is correct."],
      ["The roots stay in the expanded clay and do not go into the water",
       "The solution is not good for the roots: it is warm, or the DO is low, or the load of microbes is high",
       "The temperature and the DO, then how clean the reservoir is",
       "You wait, and you think that it is &lsquo;slow establishment&rsquo;"],
      ["The ORP increased by approximately 200 mV after a change of equipment",
       "The reservoir became more clean. The cause is not the direct effect of oxygen.",
       "Find if a chemical oxidizer is in the water. Record the pH with the ORP.",
       "You read it as a measurement of dissolved oxygen."],
    ], caption="The table of faults. Frequently the correct step is to <em>decrease</em> something "
      "and not to add something."),
    callout("key", "The five most important points, in sequence",
      ol(["<strong>Solution temperature.</strong> It changes the oxygen supply, the oxygen demand "
          "and the pathogen growth rate at the same time. No other control has this effect.",
          "<strong>Sufficient aeration at a low rate.</strong> Increase the DO to more than the "
          "floor for hypoxia, then stop. The top of the range has a different problem.",
          "<strong>A stable pH.</strong> If the pH is too high, your iron chelate does not hold the "
          "iron. The pH is the value with a very small buffer.",
          "<strong>A clean reservoir.</strong> The organic load is oxygen demand. Use your DO "
          "headroom with a decision, and not by accident.",
          "<strong>Recorded numbers.</strong> To find the cause of each fault in the table above, "
          "examine the trend. One reading gives almost no information. An ORP reading without the "
          "pH gives no information."], "tight")),
  ]})
