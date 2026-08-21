# -*- coding: utf-8 -*-
"""Paper: energy, utilities and sustainability — where the kilowatt-hours go in an indoor grow and how to spend fewer of them."""
import json, os
from components import (p, lead, h, ul, ol, callout, defterm, table, figure, grid, card, chip, kv, steps)
import figs_lib as L

_FIGS = json.load(open(os.path.join(os.path.dirname(__file__), "figs_energy.json"), encoding="utf-8"))

SLUG = "energy-sustainability"
TITLE = "Energy, utilities and sustainability"
EYEBROW = "Facility · Energy"
SUB = ("Where the kilowatt-hours actually go in an indoor grow (lighting, HVAC, dehumidification) "
      "and the cited playbook for spending fewer of them: efficacy, the double dividend, demand "
      "charges, water reuse, and the retrofit order that pays.")
META = [("spark", "Energy"), ("image", "12 diagrams"),
        ("quote", "Evidence-linked · 14 sources"), ("clock", "~18 min read")]
RELATED = ["lighting-fundamentals", "scaling-high-light", "grow-room-systems"]
REF_IDS = ["mills2012-carbon", "summers2021-natsust", "mills2025-oneearth", "nwpcc2018-cannabis",
           "remillard2017-aceee", "zheng2021-review", "kusuma2020-efficacy", "dlc-hort-v4",
           "rii-led-2022", "rii-powerscore", "nrel2017-demand", "nfd2018-energy",
           "cbt-condensate", "mbie-energy-nz"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

_N = [0]
def _fig(svg, cap):
    _N[0] += 1
    return figure(svg, _N[0], cap)

SECTIONS = []

# ---------------------------------------------------------------- 1 start here
SECTIONS.append({"id": "start-here", "kicker": "Start here",
  "title": "Your power bill is a design choice",
  "blocks": [
    lead("Indoor cannabis is one of the most energy-intensive ways humans make anything. Growing one "
         "kilogram of flower in a conventional indoor room takes thousands of kilowatt-hours, the "
         "classic model puts it around 6,000 kWh, about six units of electricity per gram" + _c("mills2012-carbon") +
         ". At industry scale that added up to roughly 1% of US national electricity use back in 2012, "
         "and the 2025 update puts the industry's climate footprint at 44 million tonnes of CO₂e a year"
         ", the emissions of about 10 million cars, with a US energy bill near US$11 billion" + _c("mills2025-oneearth") + "."),
    p("Almost none of that intensity is compulsory. The spread "
      "between an efficient room and a wasteful one growing the same flower is enormous, and the spread "
      "between indoor, greenhouse and outdoor is two orders of magnitude" + _c("nwpcc2018-cannabis") +
      ". Energy is typically one of the top operating costs of a cultivation business, estimates run "
      "from 20% to as much as 50% of production cost" + _c("remillard2017-aceee") + ", and unlike rent "
      "or wages, you can engineer it down without giving anything up. This paper is the map: where the "
      "kilowatt-hours go, what the benchmark studies actually measured, and the order to attack the "
      "bill in."),
    callout("note", "What this paper does",
      p("It walks a beginner from reading their own power bill to running a cited efficiency retrofit. "
        "You do not need an engineering background. Every term is defined on the way through. It pairs "
        "with <a href='lighting-fundamentals.html'>lighting fundamentals</a> (what the photons do), "
        "<a href='grow-room-systems.html'>grow-room systems</a> (what the equipment does), and "
        "<a href='scaling-high-light.html'>scaling to high light</a> (what happens when you push "
        "intensity up).")),
  ]})

# ---------------------------------------------------------------- 2 core answer
SECTIONS.append({"id": "core-answer", "kicker": "The core answer",
  "title": "Four facts that explain the whole bill",
  "blocks": [
    p("<strong>1. Lighting is the biggest single line, climate is the biggest family.</strong> In the "
      "classic end-use model, lighting takes about a third of total energy, and ventilation, "
      "dehumidification and air conditioning together take almost half" + _c("mills2012-carbon") +
      ". A Pacific Northwest utility survey of licensed producers found lighting closer to three "
      "quarters of indoor electric load in that mild climate" + _c("nwpcc2018-cannabis") + ". In "
      "greenhouse-gas terms, the big 2021 life-cycle study found HVAC the largest contributor in every "
      "US location it modelled, with lights second everywhere" + _c("summers2021-natsust") + ". "
      "Whichever way you slice it: lights plus climate is 80–90% of the story, everything else is noise."),
    _fig(_FIGS["anatomy"],
      "The end-use split from Mills' 2012 model of a standard indoor production module: lighting 33%, "
      "ventilation + dehumidification 27%, air conditioning 19%, everything else about 21%" + _c("mills2012-carbon") +
      ". The exact split moves with climate and lighting era, but lights + climate dominating does not."),
    p("<strong>2. Every lighting watt is paid for twice.</strong> Essentially all fixture input power ends "
      "up as heat in the room, which your cooling then removes at a cost of roughly one extra watt for "
      "every three of heat. Cut lighting power and the cooling bill falls with it, the double dividend "
      "(Section 7)."),
    p("<strong>3. You are billed for kW as well as kWh.</strong> Commercial tariffs commonly charge for "
      "your peak demand (kW) on top of your energy (kWh)" + _c("nrel2017-demand") + ". Three flower "
      "rooms flipping on at the same second can set a peak that costs you all month, for zero extra yield."),
    p("<strong>4. You cannot manage what you do not meter.</strong> The facilities that benchmark "
      "(kWh per square metre of canopy, grams per kWh) are the ones that improve, the benchmarking "
      "bodies estimate most growers can cut at least 30% of energy spend with existing measures" + _c("rii-powerscore") + "."),
    callout("key", "The one-sentence version",
      p("Photons are the product; every other kilowatt-hour is cleaning up after the photons, so buy "
        "photons more efficiently first, then move the heat and moisture more intelligently, and meter "
        "everything so you can prove it worked.")),
  ]})

# ---------------------------------------------------------------- 3 key terms
SECTIONS.append({"id": "key-terms", "kicker": "Key terms",
  "title": "kWh literacy: the vocabulary of the bill",
  "blocks": [
    p("Energy talk collapses into a handful of units. Get these straight and every spec sheet, tariff "
      "and benchmark in this paper reads easily."),
    defterm("kWh (kilowatt-hour)", "The unit of energy you buy. One kWh runs a 1,000 W load for one "
            "hour, a single 660 W LED bar on a 12-hour flower day uses about 7.9 kWh per day, "
            "roughly 2,900 kWh a year."),
    defterm("kW (kilowatt) and demand", "The rate of use. How hard you are pulling right now. Utilities "
            "record your highest sustained draw (often the worst 15- or 30-minute window) each month "
            "and many charge for it separately. kWh fills the tank; kW is the size of the hose."),
    defterm("Efficacy (µmol/J)", "How many photosynthetic photons a fixture makes per joule of "
            "electricity. The single most important number on a grow-light spec sheet. HPS ~1.7, "
            "modern LED 2.5–3.5+ (Section 6)."),
    defterm("COP (coefficient of performance)", "How many units of heat a cooling (or heating) system "
            "moves per unit of electricity it eats. COP 3 means 1 kW of compressor power removes 3 kW "
            "of heat. Higher is better; resistance heating is COP 1 by definition."),
    defterm("Energy intensity metrics", "kWh per square metre (or square foot) of canopy per year "
            "compares facilities; kWh per gram (or its inverse, grams per kWh) compares production "
            "efficiency. The industry benchmarking platform tracks both" + _c("rii-powerscore") + "."),
    defterm("Sensible vs latent load", "Sensible heat changes air temperature; latent heat is the "
            "energy carried by water vapour. A grow room's latent load, everything the plants "
            "transpire. Is why dehumidification is its own major energy line."),
    defterm("Time-of-use (TOU) tariff", "A price schedule where a kWh costs more at peak hours and "
            "less off-peak, as opposed to a flat rate. With lights running only half the day anyway, "
            "grows are unusually well placed to exploit it."),
    p("One more habit: convert everything to the same basis before comparing. US sources quote kWh per "
      "square foot and kWh per pound; multiply by 10.8 to get kWh/m² and by 2.2 to get kWh/kg."),
  ]})

# ---------------------------------------------------------------- 4 energy anatomy
SECTIONS.append({"id": "energy-anatomy", "kicker": "Energy anatomy",
  "title": "Where the kilowatt-hours go, measured",
  "blocks": [
    p("Mills (2012) built the first transparent end-use model of a standard indoor production module "
      "and it is still the reference skeleton: lighting about 33% of energy, ventilation and "
      "dehumidification 27%, air conditioning 19%, with CO₂ injection, water handling, space heat and "
      "drying making up the rest" + _c("mills2012-carbon") + _c("zheng2021-review") + ". Power "
      "density in a flowering room runs near 200 W per square foot, the same order as a data "
      "centre" + _c("remillard2017-aceee") + "."),
    p("Real facilities scatter around that skeleton. The Northwest Power and Conservation Council "
      "surveyed licensed producers in Oregon and Washington and measured indoor operations at about "
      "128 kWh per square foot of canopy per year (≈1,380 kWh/m²), roughly 100 of it lighting and 28 "
      "HVAC and pumping, against 12 for greenhouses and about 1 for outdoor" + _c("nwpcc2018-cannabis") +
      ". Mild-climate rooms lean harder on lighting; hot, humid or freezing climates push the HVAC "
      "share up. The 2021 national life-cycle study modelled a facility in every US county and found "
      "climate control the largest greenhouse-gas contributor in all of them, driven partly by "
      "ventilation rates of 12–60 air changes per hour in surveyed grows, versus 0.35 for a house "
      "and a 15-ACH minimum for a hospital operating theatre" + _c("summers2021-natsust") + "."),
    _fig(L.hbars("Annual electricity per unit of licensed canopy",
            [("Indoor", 128), ("Mixed-use", 38), ("Greenhouse", 12), ("Outdoor", 1)],
            unit=" kWh/ft²", note="Pacific NW producer survey; multiply by 10.8 for kWh/m². Indoor ≈ 1,380 kWh/m²·yr."),
      "The production-environment spread in one utility survey: indoor rooms used about ten times the "
      "electricity of greenhouses per unit of canopy, and about a hundred times outdoor" + _c("nwpcc2018-cannabis") +
      ". Nothing else in this paper moves the needle like the decision this chart describes."),
    callout("note", "Why the split flips in an LED room",
      p("Mills' 33/27/19 split describes an HPS-era room. Swap to LED and lighting kWh falls ~40% while "
        "the plants keep transpiring, so the dehumidifier's <em>share</em> of the bill rises even as "
        "the total falls. Post-retrofit, climate is usually your biggest family of load. Plan the "
        "HVAC work (Section 8) as the second act of the same project, not a separate one.")),
  ]})

# ---------------------------------------------------------------- 5 benchmarks
SECTIONS.append({"id": "benchmarks", "kicker": "Benchmarks",
  "title": "kWh per gram: the honest spread",
  "blocks": [
    p("How much electricity does a gram of flower take? The studies disagree, usefully. The spread "
      "tells you how much of the number is physics and how much is choices."),
    _fig(L.bars("Electricity to grow one kilogram, by source",
            [("Modelled low (mild US coast)", 1700), ("Industry estimate (~2,000 kWh/lb)", 4400),
             ("Modelled high (worst climate)", 5300), ("Mills 2012 module", 6074)],
            unit="", note="kWh per kg of dried flower. Bars 1 & 3: Summers et al. 2021 location range. Boundaries differ between studies.",
            maxv=7000),
      "Published electricity intensities for indoor production: the 2021 national model spans roughly "
      "1,700–5,300 kWh/kg depending on location" + _c("summers2021-natsust") + ", the trade "
      "literature's rule of thumb is ~2,000 kWh per pound (≈4,400 kWh/kg)" + _c("remillard2017-aceee") +
      ", and Mills' 2012 module works out near 6,074 kWh/kg" + _c("mills2012-carbon") + "."),
    table(["Source", "What it measured", "Headline number"], [
      ["Mills 2012 (Energy Policy)" + _c("mills2012-carbon"), "Model of a standard indoor module, US average practice",
       "≈6,074 kWh/kg; ~13,000 kWh per year per 4'×4'×8' module"],
      ["Summers et al. 2021 (Nature Sustainability)" + _c("summers2021-natsust"), "Modelled facility in every US county, cradle-to-gate",
       "Electricity ≈1,700–5,300 kWh/kg by location; GHG 2,283–5,184 kg CO₂e/kg"],
      ["ACEEE industry review 2017" + _c("remillard2017-aceee"), "Trade + utility programme data",
       "~2,000 kWh/lb (≈4,400 kWh/kg); ~200 W/ft² power density"],
      ["NW Power &amp; Conservation Council" + _c("nwpcc2018-cannabis"), "Survey of licensed OR/WA producers",
       "Indoor 128 vs greenhouse 12 vs outdoor 1 kWh/ft²·yr"],
      ["Cannabis PowerScore (RII)" + _c("rii-powerscore"), "Self-reported facility benchmarking dataset",
       "Tracks kWh/ft² and g/kWh; most facilities can save ≥30%"],
    ], cls="compact", caption="The benchmark landscape. Read the 'what it measured' column before quoting any of the numbers."),
    p("To make the units concrete: 4,400 kWh/kg is 4.4 kWh per gram, about the electricity a typical "
      "fridge uses in three days, per gram. Flip it into the benchmarking platform's preferred metric "
      "and the same number is ~0.23 g/kWh; the 2021 model's best case (~1,700 kWh/kg) is ~0.6 g/kWh. "
      "Well-run LED rooms report their progress in exactly these units" + _c("rii-powerscore") + "."),
    callout("warn", "Benchmark theatre, compare boundaries, not just numbers",
      p("These studies draw different lines. Some count electricity only; the 2021 model adds natural "
        "gas, upstream materials and CO₂ supply; per-canopy figures ignore veg rooms, drying and "
        "offices unless stated. Comparing your metered kWh/g to a study with a different boundary "
        "proves nothing. Pick one metric you can measure consistently, total facility kWh per gram of "
        "saleable dry flower per cycle is the honest one, and compare yourself to yourself, cycle "
        "over cycle.")),
  ]})

# ---------------------------------------------------------------- 6 lighting
SECTIONS.append({"id": "lighting", "kicker": "Lighting",
  "title": "Efficacy: the most important number you can buy",
  "blocks": [
    p("A grow light's job is photons. Efficacy, photosynthetic photons out per joule of electricity "
      "in, written µmol/J, is the number that decides your lighting bill at any given light level. A "
      "1,000 W double-ended HPS delivers about 1.72 µmol/J" + _c("kusuma2020-efficacy") + ". By 2020, "
      "commercial LED fixtures had reached 2.5–2.8 µmol/J for white+red spectra and 3.0 for blue+red, "
      "with practical limits near 3.4 and 4.1 respectively" + _c("kusuma2020-efficacy") + ". The "
      "DesignLights Consortium's horticultural qualification floor, the minimum to get on the QPL "
      "that rebate programmes reference, is 2.5 µmol/J from April 2025, which the DLC notes is more "
      "than 45% above the best non-LED option" + _c("dlc-hort-v4") + "."),
    _fig(L.hbars("The efficacy ladder (µmol/J)",
            [("1,000 W DE HPS", 1.72), ("DLC QPL floor 2023 (V3)", 2.3), ("DLC QPL floor 2025 (V4)", 2.5),
             ("Top LED fixtures ~2020", 3.0), ("White+red practical limit", 3.4), ("Blue+red practical limit", 4.1)],
            unit="", note="Photosynthetic photon efficacy. Same PPFD at 1.7 vs 3.0 µmol/J = ~43% less lighting power."),
      "From HPS to the LED frontier" + _c("kusuma2020-efficacy") + _c("dlc-hort-v4") + ". Efficacy is "
      "multiplicative with everything else: a room lit at 3.0 µmol/J needs ~43% less lighting power "
      "than the same PPFD at 1.72 — before counting the cooling saving."),
    p("The arithmetic is worth doing once by hand. Delivering the same photon flux at 3.0 µmol/J "
      "instead of 1.72 cuts lighting power by about 43% (1 − 1.72/3.0). That is what the field data "
      "shows too: in a benchmarking analysis of 84 indoor facilities, the ones flowering under LED "
      "averaged 34% better facility energy efficiency and 80% better production efficiency (grams per "
      "unit energy) than double-ended HPS facilities" + _c("rii-led-2022") + ", and a documented "
      "Oregon HPS→LED retrofit improved grams per kWh by 68%" + _c("rii-powerscore") + "."),
    p("Two honesty notes. First, efficacy differences within the LED market are now bigger than the "
      "brand stories suggest, read the tested µmol/J on the QPL listing, not the marketing "
      "page" + _c("dlc-hort-v4") + ". Second, an LED swap changes the room's physics: less radiant "
      "heat means cooler leaf surfaces at the same air temperature, so target air temperature "
      "typically rises a degree or two and humidity control gets harder, not easier, the "
      "<a href='lighting-fundamentals.html'>lighting paper</a> covers the plant side; Section 8 "
      "covers the machine side."),
    callout("tip", "Buying photons, not fixtures",
      ul(["Compare fixtures at <strong>µmol/J and total µmol/s output</strong>, never at watts. Watts are the cost, not the product.",
          "Check the fixture is on the DLC horticultural QPL. That is the tested number, and often the rebate gateway" + _c("dlc-hort-v4") + ".",
          "Dimmed LEDs usually run slightly <em>more</em> efficiently per photon, so sizing fixtures with headroom and running at 80–90% costs little.",
          "Efficacy buys you either the same light for less power or more light for the same power, decide which before you buy (see <a href='scaling-high-light.html'>scaling to high light</a>)."], "tight")),
  ]})

# ---------------------------------------------------------------- 7 double dividend
SECTIONS.append({"id": "double-dividend", "kicker": "The double dividend",
  "title": "Every lighting watt is paid for twice",
  "blocks": [
    p("Here is the physics that makes lighting efficiency the anchor measure. Essentially every watt "
      "you feed a fixture ends up as heat in the room. The photons themselves are absorbed by leaves "
      "and surfaces and become heat too. While lights are on, your cooling must remove that heat, and "
      "a vapour-compression system spends roughly one watt of compressor power per three watts of "
      "heat moved (the ACEEE industry analysis assumed 1.2 kW per ton, a COP of about 2.9, with "
      "cooling required year-round during lights-on)" + _c("remillard2017-aceee") + "."),
    _fig(_FIGS["dividend"],
      "The double dividend, quantified with the ACEEE assumptions" + _c("remillard2017-aceee") + ": "
      "replacing a 1,000 W HPS with a 600 W LED at equal photon delivery saves 400 W at the fixture "
      "and another ~138 W at the compressor. Every avoided lighting watt is worth ~1.3 W off the "
      "whole-room draw."),
    p("Run the numbers over a year and the dividend is most of the payback case. The ACEEE worked "
      "example: a flowering fixture stepping from 1,000 W HID to 600 W LED saves about 2,300 kWh a "
      "year once avoided cooling is counted (12-hour days), and a veg fixture from 600 W to 300 W "
      "saves about 2,600 kWh (18-hour days), simple paybacks of 2–4 years at US$0.12/kWh, before "
      "any rebate" + _c("remillard2017-aceee") + ". At higher power prices the payback shortens "
      "proportionally."),
    callout("warn", "The dividend has two fine-print clauses",
      ul(["<strong>Winter heating can claw some back.</strong> In cold climates, HPS waste heat was "
          "doing free heating during lights-on. After an LED swap you may buy some of that heat back, "
          "ideally with a heat pump at COP 3, not resistance coils at COP 1.",
          "<strong>The latent load does not shrink.</strong> Transpiration is driven by the "
          "environment and canopy, not by fixture wattage. Your dehumidifier keeps working. Less AC "
          "runtime also means less incidental moisture removal on the AC coil, so the dedicated dehu "
          "often works <em>harder</em> post-retrofit. Budget for it (Section 8)."], "tight")),
  ]})

# ---------------------------------------------------------------- 8 hvac
SECTIONS.append({"id": "hvac", "kicker": "HVAC & dehumidification",
  "title": "Moving heat and water for fewer watts",
  "blocks": [
    p("After lighting, the climate plant is where the remaining kilowatt-hours live" + _c("mills2012-carbon") +
      _c("summers2021-natsust") + ". You cannot opt out of the work. The room's heat must leave and "
      "the transpired water must leave, but the same work can be done at wildly different "
      "efficiencies. Four levers, roughly in order of how much they save:"),
    _fig(L.zones("COP, heat moved per unit of electricity", 1, 5,
            [(1, 2, L.REDL, "resistance / worst"), (2, 3, L.AMBL, "aged or abused DX"),
             (3, 4, L.GL, "good modern DX"), (4, 5, L.GXL, "best-in-class / mild-climate")],
            unit="", note="Typical ranges, illustrative. Real COP depends on temperatures, maintenance and load matching."),
      "The COP scale. Every point of COP you gain removes the same heat for ~25–35% fewer watts; "
      "resistance heat and resistance reheat sit at 1.0 by definition, which is why they are the "
      "first thing to engineer out."),
    p("<strong>1. Buy COP and stage it.</strong> Higher-COP equipment does the same job for fewer "
      "watts, but only if it can run in its happy zone. A single oversized unit short-cycles at "
      "part load: it never runs long enough to dehumidify properly, cycles its compressor to death, "
      "and wastes energy on every restart. Multiple smaller staged units, or variable-capacity "
      "compressors, track the room's actual load, which in a grow swings hugely between lights-on "
      "and lights-off. Size for the real post-LED heat load, not the HPS-era one."),
    p("<strong>2. Reuse heat you already paid for.</strong> Dehumidification by sub-cooling needs the "
      "cold air reheated to supply temperature; doing that with electric resistance is a COP-1 "
      "penalty you pay twice. <em>Hot-gas reheat</em> uses the refrigeration circuit's own rejected "
      "heat for free; air-to-air heat-recovery dehumidifiers pre-cool incoming air against the cold "
      "outgoing stream, UC Davis testing of such a system measured 30–50% savings over conventional "
      "units without recovery" + _c("remillard2017-aceee") + ". Desiccant systems can likewise be "
      "recharged with waste heat where it exists" + _c("remillard2017-aceee") + "."),
    p("<strong>3. Use free cooling where the climate offers it.</strong> When outside air is cooler "
      "and drier than the room, an economiser can dump heat for the cost of a fan instead of a "
      "compressor. The surveyed industry runs ventilation anywhere from 12 to 60 air changes per "
      "hour" + _c("summers2021-natsust") + ", sealed CO₂-enriched rooms rightly sit at the low end, "
      "but lights-off hours and shoulder seasons still offer free-cooling windows if the controls "
      "and filtration are designed for it. The trade-offs (CO₂ loss, humidity ingress, filtration, "
      "biosecurity) are covered in <a href='airflow-design.html'>airflow design</a> and "
      "<a href='co2-enrichment.html'>CO₂ enrichment</a>."),
    p("<strong>4. Mind the dehumidifier's own efficiency.</strong> Dehumidifiers are rated in litres "
      "of water removed per kWh; integrated and heat-recovery designs beat fleets of portable "
      "domestic units decisively, and drying rooms deserve the same scrutiny as flower rooms. When "
      "the lights-off period arrives, the room still transpires for hours, lights-off dehu capacity "
      "is a mould-risk control as much as an energy line (see <a href='mould-risk.html'>mould risk</a>)."),
    callout("tip", "Deadbands are free money",
      p("Every controller has a deadband, the gap between 'start cooling' and 'start heating'. "
        "Rooms tuned to fight for ±0.3 °C burn energy purely on nervous equipment. Widen deadbands "
        "to what the plants actually notice (±1 °C is generous), make sure heating and cooling "
        "setpoints can never overlap, and stop the AC and dehu fighting each other, reheat wars "
        "between two controllers are a classic silent kWh leak.")),
  ]})

# ---------------------------------------------------------------- 9 demand & tariffs
SECTIONS.append({"id": "demand-tariffs", "kicker": "Power vs energy",
  "title": "kW, kWh, and why lights-on time is a billing decision",
  "blocks": [
    p("Your bill has two different products on it. <strong>Energy</strong> (kWh) is the total you "
      "used. <strong>Demand</strong> (kW) is the fastest you used it, typically the highest 15- or "
      "30-minute average in the month, and commercial tariffs commonly price it separately. In a US "
      "survey, nearly five million commercial customers were on tariffs with demand charges above "
      "US$15 per kW-month" + _c("nrel2017-demand") + "; at that rate a 190 kW peak costs ~US$2,850 a "
      "month before you have paid for a single kWh."),
    _fig(_FIGS["loadprofile"],
      "Three 50 kW flower rooms on a 40 kW base. Synchronised lights-on peaks the site at 190 kW; "
      "staggering the same rooms 8 hours apart caps it at 140 kW. Both days consume exactly 2,760 "
      "kWh, the kWh line of the bill is identical, the kW line is 26% lower."),
    p("This is the cheapest retrofit in the whole paper: it is a scheduling change. Flower rooms run "
      "12/12 regardless, so staggering their on-times costs no photons, and it also smooths the load "
      "on your own transformer, wiring and HVAC plant, the climate system sees one room's worth of "
      "step change at a time instead of three. If your veg room runs 18/6, park its 6 dark hours "
      "over the flower rooms' overlap window."),
    p("<strong>Tariff thinking, kept generic.</strong> On a flat tariff, only efficiency and demand "
      "management matter. On a time-of-use tariff, a kWh at peak can cost several times an off-peak "
      "kWh, and a 12/12 room is free to put its entire lights-on block wherever the cheap hours "
      "are, typically overnight. Running lights-on through the night also puts your biggest cooling "
      "load into the coolest outdoor air, which raises the real-world COP of every unit rejecting "
      "heat outside. The costs are human: night-shifted rooms need night checks, and any light-leak "
      "discipline problems get harder to spot. Read your actual tariff sheet (fixed charge, energy "
      "rates by period, demand charge, power-factor clause) before optimising anything."),
    table(["Bill line", "What drives it", "Your lever"], [
      ["Fixed / daily charge", "Being connected at your capacity class", "Right-size your supply; don't pay for capacity headroom you never use"],
      ["Energy (kWh)", "Everything in Sections 4–8", "Efficacy, COP, heat recovery, controls"],
      ["Demand (kW)", "Worst 15–30 min of the month", "Stagger lights-on; soft-start big motors; never let all rooms + dehus + irrigation align"],
      ["Time-of-use spread", "When you use, not how much", "Put lights-on blocks in cheap windows; pre-cool before peak windows"],
      ["Power factor (if billed)", "Reactive load from old magnetic ballasts, motors", "Modern LED drivers are near unity; correction capacitors for big motor plant"],
    ], cls="compact", caption="The bill, decomposed. Most growers only ever manage line two."),
    callout("warn", "Check before you shift",
      p("Demand-charge and TOU structures vary enormously between utilities and countries, some "
        "meter demand only at peak times, some all day, some ratchet your worst month across the "
        "year. The strategy above is universal; the arithmetic is not. Model your specific tariff "
        "with a spreadsheet and one month of interval data before committing the facility to a "
        "night schedule.")),
  ]})

# ---------------------------------------------------------------- 10 water
SECTIONS.append({"id": "water", "kicker": "Water",
  "title": "The water bill is an energy bill wearing a raincoat",
  "blocks": [
    p("Indoor cannabis is thirsty in a specific, recoverable way. Reported irrigation demand runs "
      "around 9–11 litres per plant per day for mature indoor plants in peak season, and about 22.7 "
      "L/day for outdoor plants at the height of summer" + _c("zheng2021-review") + ", though "
      "per-plant numbers vary so much with pot size, plant size and stage that the benchmarking "
      "bodies deliberately measure water per unit of canopy instead" + _c("rii-powerscore") + ". In "
      "drain-to-waste systems another 10–30% is pushed through deliberately as runoff to control "
      "salts (see the irrigation papers for why)."),
    p("Here is the part beginners miss: in a sealed room, <strong>almost every litre you irrigate "
      "ends up in the air</strong>, because the plant transpires the overwhelming majority of what "
      "it drinks. Your dehumidifier and AC coils then condense it back to liquid, a large flower-"
      "room dehumidifier can yield around 270 litres a day, roughly 1,900 litres a week, of "
      "near-distilled condensate" + _c("cbt-condensate") + ". That is water you already paid to "
      "pump, treat, and then remove from the air at real electrical cost. Sending it down the drain "
      "is paying full price for a product and binning it at the door."),
    _fig(_FIGS["waterloop"],
      "The sealed-room water loop. Irrigation leaves mostly as transpiration, condenses on the dehu "
      "and AC coils, and can be treated and returned. Condensate is near-distilled but picks up "
      "metals from coils and biofilm from drain pans, so it is filtered, sterilised and "
      "re-mineralised before reuse" + _c("cbt-condensate") + "."),
    p("Rules of thumb for the loop. Treat condensate before reuse, carbon/sediment filtration plus "
      "UV is the common stack, then blend or re-mineralise since near-zero-EC water is aggressive "
      "on plumbing and useless as a calcium source" + _c("cbt-condensate") + ". Collect runoff "
      "separately: it carries nutrients and root-zone microbes, so it needs proper treatment or "
      "disposal, not quiet blending. Keep collection tanks dark, cool and cycled to stop biofilm. "
      "And check your local rules first, jurisdictions differ on whether reclaimed condensate may "
      "touch a consumable crop, on backflow prevention, and on trade-waste discharge of runoff. "
      "Water quality itself (what is in it before nutrients) is covered in "
      "<a href='water-quality.html'>source water, RO and alkalinity</a>."),
    callout("tip", "Condensate is also a free flow meter",
      p("Log your daily condensate volume. It tracks whole-room transpiration, so a sudden drop "
        "flags stalled plants, a failed dehu, or an irrigation fault, often a day before anything "
        "looks wrong. Facilities instrumented for it treat condensate litres as a crop biosignal, "
        "not just reclaimed water.")),
  ]})

# ---------------------------------------------------------------- 11 carbon
SECTIONS.append({"id": "carbon", "kicker": "Carbon",
  "title": "The carbon story: grid × kWh, and the greenhouse question",
  "blocks": [
    p("Carbon follows the same arithmetic as the bill: kWh consumed × the grid's emissions per kWh. "
      "The 2021 national study put cradle-to-gate emissions of indoor production at 2,283–5,184 kg "
      "CO₂e per kg of dried flower depending on location (median 3,658), with US grid intensities "
      "spanning roughly 245–766 g CO₂e/kWh" + _c("summers2021-natsust") + ". Mills' earlier central "
      "estimate was 4,600 kg CO₂e/kg, enough that a single joint carried about 1.5 kg of "
      "CO₂" + _c("mills2012-carbon") + ". The 2025 industry-wide update lands at 44 Mt CO₂e per "
      "year, about 1% of total US emissions, with roughly 90% of it attributable to indoor "
      "production" + _c("mills2025-oneearth") + "."),
    _fig(L.bars("Indoor life-cycle GHG per kg, by location",
            [("Best US location", 2283), ("US median", 3658), ("Worst US location", 5184)],
            unit="", note="kg CO₂e per kg dried flower, cradle-to-gate (Summers et al. 2021). Location = climate + grid mix.",
            maxv=6000),
      "Same product, same method, different postcode: the modelled spread from mild-coast Long "
      "Beach to Kaneohe Bay, Hawaii" + _c("summers2021-natsust") + ". Climate drives the HVAC "
      "work; the local grid decides what each kWh costs the atmosphere."),
    _fig(L.hbars("Emissions per kg by production route",
            [("Outdoor (electricity only)", 23), ("Greenhouse (electricity only)", 327), ("Indoor (full life-cycle, median)", 3658)],
            unit=" kg", note="Boundaries differ: rows 1–2 are electricity-related only (2018 industry report); row 3 is cradle-to-gate."),
      "The route comparison that dominates everything else. Electricity-related emissions were "
      "estimated at ~22.7 kg CO₂e/kg for outdoor and ~326.6 for greenhouse production" + _c("nfd2018-energy") +
      ", versus thousands for indoor life-cycle" + _c("summers2021-natsust") + ". The boundaries "
      "differ, but not by enough to change the conclusion: sunlight is the biggest single carbon "
      "lever that exists."),
    p("For licensed indoor growers the route is usually fixed by regulation, security and quality "
      "requirements, so the honest carbon plan is: cut kWh (everything above), then buy cleaner "
      "kWh. Grid mix matters enormously: the same room emits several times less in a hydro-heavy "
      "region than a coal-heavy one at identical efficiency" + _c("summers2021-natsust") + ". On a "
      "renewables-heavy grid like New Zealand's, 85.5% renewable electricity in "
      "2024" + _c("mbie-energy-nz") + ", the carbon per kWh story softens dramatically. The bill "
      "does not: every efficiency argument in this paper is written in dollars first, and those "
      "survive any grid."),
    callout("note", "Sustainability claims that survive an audit",
      ul(["Claim numbers you metered, in stated units, over a stated boundary, 'we cut facility kWh/g 22% year-on-year' beats 'we're green'.",
          "Cite grid factors with a source and year; grids change annually" + _c("mbie-energy-nz") + ".",
          "Never net off purchased offsets against an intensity claim without saying so.",
          "If you sell into markets with sustainability reporting, per-gram energy and water intensity are the two numbers buyers increasingly ask for" + _c("rii-powerscore") + "."], "tight")),
  ]})

# ---------------------------------------------------------------- 12 retrofit order
SECTIONS.append({"id": "retrofit-order", "kicker": "The retrofit order",
  "title": "Measure → LED → controls → dehu → envelope",
  "blocks": [
    p("Efficiency projects fail by sequencing, not by technology. The order below exists because "
      "each step changes the sizing maths of the next, do them backwards and you buy equipment "
      "twice. It also front-loads the cheap wins so the early savings fund the later capital."),
    _fig(L.flow("The retrofit order",
            [("Measure", "2+ weeks of submetered baseline"), ("LED", "the double dividend"),
             ("Controls", "schedules, staging, deadbands"), ("Dehu", "heat-recovery, right-sized"),
             ("Envelope", "seal, insulate, doors")],
            note="Each step re-sizes the next. Never buy HVAC for a room you are about to relight."),
      "The sequence, left to right. The measurement step is the one everyone skips and the one that "
      "makes every later claim provable."),
    steps([
      ("Measure first, two weeks minimum of baseline",
       "Submeter lighting, HVAC, dehumidification and 'everything else' separately (Section 13), and "
       "log room conditions alongside. You are buying two things: the before-photo that proves every "
       "later saving, and the load numbers that size every later purchase. Benchmarking your kWh/ft² "
       "and g/kWh against the industry dataset tells you how much headroom you have" + _c("rii-powerscore") + "."),
      ("LED retrofit, the anchor measure",
       "Biggest single lever: ~40% off lighting kWh at equal photons plus the cooling dividend "
       "(Sections 6–7), with documented 2–4 year paybacks before rebates" + _c("remillard2017-aceee") +
       " and 34–80% efficiency gaps between LED and HPS facilities in the field" + _c("rii-led-2022") +
       ". Ramp intensity per the <a href='light-acclimation.html'>acclimation paper</a>, an "
       "efficiency project that bleaches a crop pays for nothing."),
      ("Controls and deadbands, near-zero capital",
       "Stagger lights-on across rooms (Section 9). Widen deadbands, fix fighting setpoints, stage "
       "equipment, and relax lights-off targets to what mould risk actually requires rather than "
       "flower-time cosmetics. This step routinely finds 5–15% of the bill for the price of "
       "commissioning time. And it is where an automation stack earns its keep."),
      ("Dehumidification and HVAC upgrade, now sized correctly",
       "With the LED heat load and staggered schedule known, right-size the climate plant: staged or "
       "variable capacity, hot-gas reheat instead of resistance, heat-recovery dehumidification "
       "(30–50% savings in testing" + _c("remillard2017-aceee") + "). This is the step the LED swap "
       "quietly made necessary, the latent share grew (Section 7)."),
      ("Envelope, seal and insulate last",
       "Vapour-seal penetrations, insulate against the climate you fight most, fix door discipline "
       "and strip-curtain the traffic paths. It is last because it is the slowest payback per dollar "
       "in most retrofits, but a leaky envelope quietly taxes every kWh the other four steps saved, "
       "and in humid climates infiltration is a permanent latent load on the dehu you just bought."),
    ]),
    callout("key", "The interaction rule",
      p("LED before HVAC, always: relighting cuts the sensible load 30–40%, so HVAC bought first is "
        "HVAC bought oversized, and oversized units short-cycle and dehumidify badly forever. The "
        "only exception is a failed unit that must be replaced today; even then, size it for the "
        "post-LED room you are about to build.")),
  ]})

# ---------------------------------------------------------------- 13 metering
SECTIONS.append({"id": "metering", "kicker": "Metering",
  "title": "You can't manage what you don't meter",
  "blocks": [
    p("The utility meter tells you one number a month about a building full of separate machines. "
      "Everything in this paper becomes manageable the day you split that number: current-transformer "
      "(CT) submeters on the lighting circuits, the HVAC plant, the dehumidifiers and the pump/"
      "controls remainder cost little per circuit and connect to any modern monitoring or home-"
      "automation platform. From there, three habits do the work:"),
    _fig(L.flow("From meter to management",
            [("Utility meter", "one number, monthly"), ("Submeters", "CTs per end-use & room"),
             ("KPIs", "kWh/g per cycle, kWh/m²"), ("Alarms", "deviation = fault found early")],
            note="Faults show up in the energy trace before they show up in the crop."),
      "The metering ladder. Each step left to right turns invoice pain into an operational signal, "
      "the endpoint is energy as a monitored crop parameter, like VPD or EC."),
    kv([
      ("Meter by end use", "Lighting, cooling, dehu, everything-else, the minimum split that maps to Sections 6–8. Per-room beats per-function once you have it."),
      ("One KPI per cycle", "Facility kWh per gram of saleable dry flower, computed every harvest. It is the only number that catches everything, and the industry benchmark metric" + _c("rii-powerscore") + "."),
      ("Watch the demand trace", "15-minute interval data (your utility often provides it free) shows exactly which coincidence sets your peak. You cannot stagger what you cannot see (Section 9)."),
      ("Alarm on deviation", "A dehu drawing 20% over its baseline is failing; a lighting circuit 10% under has dead drivers; condensate volume falling means transpiration stalled. Energy is the earliest fault sensor you own."),
      ("Log alongside climate", "kWh divorced from room state is trivia. kWh next to temperature, RH and stage is diagnosis."),
    ]),
    p("This is also where the honest sustainability numbers come from (Section 11): a metered kWh/g "
      "trend, cycle over cycle, is the entire audit trail. Facilities that submitted benchmarking "
      "data found on average that at least 30% savings were available with existing "
      "measures" + _c("rii-powerscore") + ", but every one of those savings was discovered by a "
      "meter, not a hunch."),
  ]})

# ---------------------------------------------------------------- 14 failure modes
SECTIONS.append({"id": "failure-modes", "kicker": "Failure modes",
  "title": "The six ways energy projects go wrong",
  "blocks": [
    p("These are the recurring wrecks. Every one of them is avoidable at design time and expensive "
      "afterwards."),
    grid([
      card("The LED swap that made the room wetter",
        p("Lighting kWh fell 40%; RH climbed and mould pressure followed. Less sensible heat means "
          "the AC runs less, so its coil removes less incidental moisture, while transpiration "
          "barely changed. The dedicated dehu was already marginal and now it is the bottleneck. "
          "<strong>Fix:</strong> re-run the latent load maths as part of the LED project, not after "
          "the first scare."), tag="retrofit"),
      card("Oversized HVAC, short cycles",
        p("Cooling sized for the HPS era (or 'to be safe') now short-cycles: temperature holds but "
          "humidity wanders, compressors wear out early, and efficiency dies in the start-stops. "
          "<strong>Fix:</strong> stage multiple smaller units or specify variable capacity; size "
          "from measured post-retrofit load, not the old nameplate sum."), tag="sizing"),
      card("Same kWh, bigger bill",
        p("An efficiency project cut energy 20%, and the bill barely moved, because all rooms "
          "still flip on together and the demand charge holds the total up. "
          "<strong>Fix:</strong> read the tariff, stagger lights-on, and check the interval data "
          "actually shows the peak falling (Section 9)."), tag="demand"),
      card("Sealed the room, forgot the latent bill",
        p("Closing a vented room for CO₂ enrichment ends free moisture dumping, every litre "
          "transpired must now be condensed at electrical cost. Done without heat-recovery dehu, "
          "the sealing 'saving' quietly becomes a bigger dehu bill. "
          "<strong>Fix:</strong> cost the full sealed-room energy balance before sealing; recover "
          "the condensate to claw value back (Section 10)."), tag="design"),
      card("Condensate straight into the feed tank",
        p("Free water, straight to the roots, plus dissolved coil metals and a drain-pan biofilm "
          "inoculum. Root disease and heavy-metal test failures are how this one surfaces. "
          "<strong>Fix:</strong> filter, sterilise, re-mineralise, verify with a lab test, and "
          "check reuse is legal for your licence class" + _c("cbt-condensate") + "."), tag="water"),
      card("Benchmark theatre",
        p("Quoting a flattering kWh/g against a study with a different boundary, electricity-only "
          "vs life-cycle, canopy-only vs whole facility, convinces nobody who checks. "
          "<strong>Fix:</strong> define your boundary once, publish it with the number, and compare "
          "against your own prior cycles first (Section 5)."), tag="reporting"),
    ], cols=2),
  ]})

# ---------------------------------------------------------------- 15 troubleshooting
SECTIONS.append({"id": "troubleshooting", "kicker": "Troubleshooting",
  "title": "Symptom → likely cause → what to check",
  "blocks": [
    p("Energy faults announce themselves on the meter before the crop. Work this table with your "
      "interval data open."),
    table(["Symptom", "Likely cause", "Check"], [
      ["Bill up, yield flat", "Equipment degradation: dirty coils, failing dehu, drifting sensors making HVAC overwork",
       "Per-end-use submeter trend vs last cycle; coil condition; calibrate room sensors"],
      ["Demand charge jumped one month", "A new coincidence, schedule change aligned rooms, or a big motor now starts during the peak window",
       "15-min interval data for the peak day; irrigation/dehu/lights-on timing overlap"],
      ["RH creeping up after LED retrofit", "Latent load unchanged but AC runtime (and its incidental drying) fell",
       "Dehu duty cycle and L/day removed vs pre-retrofit; add staged dehu capacity"],
      ["Dehu running flat out, room still humid", "Undersized after sealing or canopy growth; or short-cycling AC fighting it with reheat",
       "Condensate litres/day vs irrigation litres/day mass balance; setpoint conflict between AC and dehu"],
      ["Lighting kWh 10%+ below normal", "Dead drivers or failed bars. A 'saving' that is really lost photons",
       "Per-circuit draw vs commissioning baseline; PPFD spot map under suspect fixtures"],
      ["Power-factor penalty on the bill", "Aged magnetic ballasts or big uncorrected motors",
       "Bill's PF line; utility interval data; correction capacitors or driver upgrades"],
      ["Condensate volume suddenly down", "Transpiration stalled (irrigation fault, sick crop) or dehu failing, both urgent",
       "Cross-check irrigation logs and substrate sensors; dehu amp draw vs baseline"],
    ], cls="compact", caption="The meter is the first diagnostic instrument. Most rows here are visible in energy data 24–48 h before they are visible on plants."),
  ]})

# ---------------------------------------------------------------- 16 mental model
SECTIONS.append({"id": "mental-model", "kicker": "The mental model",
  "title": "Photons are the product; everything else is overhead",
  "blocks": [
    p("Strip the whole subject to one sentence: an indoor grow converts electricity into photons, "
      "and then spends more electricity cleaning up the heat and humidity the first spend created. "
      "Every kilowatt-hour on your bill is one or the other. That is why efficacy compounds "
      "(Section 6), why the double dividend exists (Section 7), and why the retrofit order runs "
      "lighting before HVAC (Section 12)."),
    callout("key", "The operating rules",
      ol(["<strong>Meter before you spend.</strong> The baseline is the cheapest instrument you will ever buy, and the only proof your project worked" + _c("rii-powerscore") + ".",
          "<strong>Buy photons per joule, not watts.</strong> Efficacy is the one spec that pays twice, at the driver and at the compressor" + _c("kusuma2020-efficacy") + _c("remillard2017-aceee") + ".",
          "<strong>Move heat with COP, never resistance.</strong> Reheat and winter heat by heat pump or hot gas; resistance is a last resort with a meter on it.",
          "<strong>Schedule the peak away.</strong> Staggered lights-on is a free 20–30% off the demand line" + _c("nrel2017-demand") + ".",
          "<strong>Close the water loop.</strong> Condensate is paid-for water and a free crop signal, treat it and use it" + _c("cbt-condensate") + ".",
          "<strong>Report your own trend, not someone else's benchmark.</strong> kWh per gram, same boundary, every cycle" + _c("summers2021-natsust") + "."])),
    p("Set your expectations honestly. You will not reach a greenhouse's numbers in a windowless "
      "room. Sunlight is a subsidy the building cannot match" + _c("nwpcc2018-cannabis") + _c("nfd2018-energy") +
      ". But the gap between an unmanaged room and a measured, LED-lit, staged, heat-recovering one "
      "is the difference between energy as your scariest cost line and energy as a controlled, "
      "boring input, the studies put 30%+ of the bill within reach of existing, proven "
      "measures" + _c("rii-powerscore") + _c("remillard2017-aceee") + ". Start with the meter."),
  ]})
