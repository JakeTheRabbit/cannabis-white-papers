# -*- coding: utf-8 -*-
"""Paper: HVAC, cooling and dehumidification for grow rooms (beginner-first, operator-grade)."""
import json, os
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        grid, card, chip, kv, steps)
import figs_lib as L

_FIGS = json.load(open(os.path.join(os.path.dirname(__file__), "figs_hvac.json"), encoding="utf-8"))

SLUG = "hvac-dehumidification"
TITLE = "HVAC and dehumidification for grow rooms"
EYEBROW = "Environment · Climate system"
SUB = ("Each watt that you put into a grow room becomes heat, and almost all the water that you "
       "apply becomes vapor. This paper shows how to calculate the two loads correctly and how to "
       "select equipment of the correct size. It shows how to control the humidity spike when the "
       "lights stop. It also shows how to prepare for a night when a unit does not operate.")
META = [("wind", "Climate system"), ("image", "11 diagrams"),
        ("quote", "14 sources"), ("clock", "~22 min to read")]
RELATED = ["grow-room-systems", "temp-humidity-vpd", "airflow-design"]
REF_IDS = ["rii-hvac-bpg", "desertaire-an25-load", "streit2023-hvacd", "hpac-latent",
           "grossiord2020-vpd", "hydrobuilder-ac-sizing", "streit2023-water",
           "quest-perfect-dehu", "quest-dehu101", "sylvane-desiccant",
           "punja-budrot-cjb", "ncia-condensate", "chandra2008-photo", "summers2021-ghg"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

# ---------------------------------------------------------------- 01 start here
SECTIONS.append({"id": "start", "kicker": "01 · Read this first", "title": "Purpose and scope",
  "blocks": [
    lead("A grow room is a system that changes electricity into light, light into plant growth, and "
         "water into vapor. Each grower calculates the energy cost of the lights. The lights are "
         "one half of the system. The climate system (cooling, heating and dehumidification) is the "
         "other half. It removes the heat and the water from the room, each hour of each day. It "
         "typically uses 30 to 60% of the energy cost of an indoor facility" + _c("rii-hvac-bpg") +
         "."),
    p("When the system has the correct size, you do not think about it. If you do not calculate the "
      "size, the result is a problem. For example, you select a mini-split from a BTU chart and a "
      "dehumidifier that looks large. You find the problem in week 6 of flowering, at 2 a.m. The "
      "room is cold and saturated, and <em>Botrytis</em> causes damage to the flowers."),
    p("This paper is for a person who selects the equipment for a first large room. It is also for "
      "a person who examines a quotation for mechanical equipment, to make sure that it is correct. "
      "It is not necessary to know about refrigeration. After you read this paper, you can "
      "calculate the loads for your room. You can examine the data sheet of a dehumidifier and make "
      "sure that its rating is correct for your conditions. You can also give the cause of the "
      "humidity of 85% when the lights go off."),
    callout("key", "The two conservation laws",
      p("<strong>1. Each watt that goes in becomes heat.</strong> In a sealed room with insulation, "
        "all of the electrical power of lights, fans, pumps and dehumidifiers becomes heat. The "
        "cooling system must remove this heat.</p><p><strong>2. Each liter of water that goes in "
        "must go away from the room.</strong> Some of the water flows out as runoff through the "
        "drain. A small quantity stays in the plant tissue. The remaining water becomes vapor, and "
        "your equipment must condense this vapor to liquid again. To select the size of a climate "
        "system, you only count these watts and liters correctly.")),
  ]})

# ---------------------------------------------------------------- 02 vocabulary
SECTIONS.append({"id": "terms", "kicker": "02 · The terms", "title": "Definitions",
  "blocks": [
    defterm("Sensible heat", "Heat that changes the <em>temperature</em> of the air. A thermometer "
            "shows the change. Almost all of the heat from the lights is sensible heat."),
    defterm("Latent heat", "Heat that is in water vapor and that a thermometer cannot show. A day "
            "of 26 &deg;C (79 &deg;F) before a thunderstorm, with high humidity, and a dry day of "
            "26 &deg;C (79 &deg;F) give the same thermometer value. But the air with high humidity "
            "contains more energy in the vapor. When 1 L of water evaporates, it absorbs "
            "approximately 0.68 kWh. This energy stays in the air until a cold coil condenses the "
            "vapor to liquid and releases the heat again. The latent heat load is the moisture load."),
    defterm("BTU and ton", "Imperial units of heat. HVAC suppliers continue to use them. 1 kW = "
            "3,412 BTU/h. 1 &ldquo;ton&rdquo; of cooling = 12,000 BTU/h = approximately 3.5 kW. A "
            "&ldquo;5-ton unit&rdquo; moves approximately 17.6 kW of heat."),
    defterm("Pint (dehumidifier rating)", "A US unit for the capacity of a dehumidifier. It is the "
            "quantity of water in pints that the dehumidifier removes each day. 1 US pint = 0.473 "
            "L. Thus a &ldquo;500-pint&rdquo; unit removes approximately 237 L/day at its rating "
            "conditions. At your conditions, the unit can remove a different quantity."),
    defterm("Relative humidity (RH)", "The quantity of vapor in the air, as a percentage of the "
            "maximum quantity that the air can hold at its temperature. When the air temperature "
            "decreases by approximately 10 &deg;C (18 &deg;F), the capacity of the air becomes "
            "approximately half. This one fact is a primary cause of the humidity spike at "
            "lights-off."),
    defterm("Dew point", "The temperature at which the air becomes saturated. At this temperature, "
            "water condenses on each surface that has a temperature equal to or less than the dew "
            "point. The dew point shows the quantity of water in the air, in grams. RH does not "
            "show this quantity. Thus the dew point is the better control target."),
    defterm("VPD", "Vapor pressure deficit. It is the drying power of the air, and you calculate it "
            "from the temperature and the RH. VPD changes the rate of transpiration, and thus it "
            "changes the latent heat load. The <a href='temp-humidity-vpd.html'>temperature, "
            "humidity and VPD paper</a> gives all the information about VPD."),
    defterm("COP", "Coefficient of performance. It is the quantity of heat in kW that the unit "
            "moves for each kW of electricity that it uses. A new compressor has a COP of 3 to 4. "
            "An electric resistance heater has a COP of 1.0, and this value cannot change. Most "
            "persons use this one number when they compare the efficiency of HVAC equipment."),
  ]})

# ---------------------------------------------------------------- 03 core answer
SECTIONS.append({"id": "two-loads", "kicker": "03 · The two loads", "title": "Sensible heat load and latent heat load",
  "blocks": [
    p("An air conditioner (AC) for comfort cooling in an office does one task: it removes dry heat. "
      "A grow room has two tasks: remove heat <em>and</em> remove water. Engineers divide the heat "
      "load into the <strong>sensible heat load</strong> (temperature) and the <strong>latent heat "
      "load</strong> (moisture). In a grow room, for much of the cycle, the latent heat load is as "
      "large as the sensible heat load, or larger. This ratio is not usual. Almost no equipment for "
      "comfort cooling has the correct capacity for it" + _c("desertaire-an25-load") + _c("hpac-latent") +
      "."),
    figure(_FIGS["split"], 1,
      "The two exits for the heat. The lights cause the sensible heat load, and the transpiration "
      "of the crop causes the latent heat load. The two loads have different equipment and "
      "different faults."),
    p("<strong>The source of the sensible heat load:</strong> almost all of it is from the lights. "
      "In a sealed room with insulation, almost all of the electrical power becomes heat that the "
      "cooling system must remove. Lighting is the largest part of this heat" +
      _c("desertaire-an25-load") + _c("streit2023-hvacd") + ". Dehumidifiers, fan motors, pumps and "
      "persons add the remaining heat."),
    p("<strong>The source of the latent heat load:</strong> the plants. A cannabis leaf has many "
      "small pores in its surface. These pores are the stomata. When the stomata are open in the "
      "light, the plant moves water up from the roots and releases it into the air as vapor. The "
      "water that the plant releases is not waste. Evaporation decreases the temperature of the "
      "leaf and moves more water (and dissolved nutrients) up from the root zone.</p><p>In "
      "transpiration, the plant continuously releases water vapor through the stomata, and the "
      "light causes it. Transpiration <em>is</em> the latent heat load. The plant moves "
      "approximately 95% or more of the water that you supply to the root zone out of the stomata "
      "as vapor. The engineering note of Desert Aire gives a value near 99% of the water that the "
      "roots absorb" + _c("desertaire-an25-load") + ". Facility engineers calculate with 80 to 95% "
      "of the total irrigation water that goes into the air again" + _c("streit2023-water") +
      ".</p><p>Your crop is part of the climate system. Your crop <em>is</em> the humidifier. It "
      "releases many liters of water each day. Your lights supply the energy, and the VPD controls "
      "the rate" + _c("grossiord2020-vpd") + "."),
    callout("note", "Plants change sensible heat into latent heat",
      p("When water evaporates, it absorbs heat. A canopy that transpires is a very large "
        "evaporative cooler. Thus the air temperature increases <em>less</em> than the watts of the "
        "lights show.</p><p>A new grower can think that the heat is not a large problem. But the "
        "heat does not go away from the room. It moves into the vapor. The coil that condenses this "
        "vapor must remove the heat again. The total heat that you remove is always equal to the "
        "total watts that go in. The plants change only how much of the heat is sensible heat and "
        "how much is latent heat.")),
  ]})

# ---------------------------------------------------------------- 04 the loads
SECTIONS.append({"id": "loads", "kicker": "04 · The loads", "title": "Calculate the heat loads of the room",
  "blocks": [
    p("All the examples from here use one room. Thus the numbers agree with each other. The room "
      "has <strong>40 m&sup2; of flowering canopy</strong> (approximately 430 square feet), 10 "
      "&times; 700 W LED fixtures, two 800 W dehumidifiers, and approximately 500 W of circulation "
      "fans and pumps.</p><p>The room is sealed and has CO&#8322; enrichment, and the internal "
      "walls have insulation. Two persons are in the room. Replace these numbers with the numbers "
      "of your room. The method is the same."),
    figure(L.hbars("Sources of the sensible heat in a day (example 40 m² room)",
            [("Lights (10 × 700 W LED)", 7.0), ("Dehumidifiers (2 × 800 W)", 1.6),
             ("Fans + pumps", 0.5), ("Persons (2)", 0.2)], unit=" kW",
            note="Sealed room with insulation. Each electrical watt becomes heat that the cooling system must remove."), 2,
      "The connected sensible heat load is 9.3 kW. Examine the second bar: your dehumidifiers are "
      "heaters. Almost 100% of their electrical power becomes heat in the room, and they also "
      "release the latent heat of each liter that they condense" + _c("hydrobuilder-ac-sizing") +
      "."),
    table(["Load", "Type", "In the example room", "Information"], [
      ["Grow lights", "Sensible heat", "7.0 kW", "The largest load. It increases when the installed power in W increases" + _c("streit2023-hvacd") + "."],
      ["Dehumidifiers", "Sensible heat", "1.6 kW of electrical power + heat of condensation", "The dehumidifiers operate mostly at night. They are the heater at night."],
      ["Fans, pumps, controls", "Sensible heat", "approximately 0.5 kW", "Each item is small, but the total is not zero."],
      ["Persons", "Sensible heat and latent heat", "approximately 0.1 kW for each person", "approximately 400 BTU/h for each person" + _c("hydrobuilder-ac-sizing")],
      ["Envelope (walls and roof)", "Sensible heat", "approximately 0 (internal room with insulation)", "The load is not zero in containers, sheds and top floors. Do not use zero for these."],
      ["Transpiration", "Latent heat", "approximately 175 L/day (next section)", "Transpiration is the latent heat load" + _c("desertaire-an25-load") + "."],
      ["Media and wet surfaces", "Latent heat", "Small part", "Water evaporates from the faces of slabs, from trays and from wet floors" + _c("desertaire-an25-load") + "."],
      ["External air", "Sensible heat and latent heat", "approximately 0 (sealed room)", "In rooms with vents, external air with high humidity adds a latent heat load."],
    ], cls="compact", caption="The list of loads. When you install more kilowatts, the sensible heat load increases. When you apply more liters of water, the latent heat load increases."),
    callout("warn", "CO₂ burners add two loads",
      p("A CO&#8322; burner that uses propane or natural gas adds heat <em>and</em> water. "
        "Combustion makes approximately 1.5 kg of water vapor for each kg of propane that burns. "
        "This vapor goes directly into the latent heat load. CO&#8322; from bottles or from a tank "
        "does not add heat or water. When you use burners, the sensible heat load is larger and the "
        "latent heat load is larger.")),
  ]})

# ---------------------------------------------------------------- 05 water balance
SECTIONS.append({"id": "water-balance", "kicker": "05 · The water balance", "title": "Water balance and dehumidification load",
  "blocks": [
    p("The most important fact for the size of the equipment is that <strong>the dehumidification "
      "load is the result of your irrigation schedule</strong>. The volume of the room and the "
      "number of plants do not give this load. The liters of water for each day give it. Water that "
      "goes in and does not flow out through the drain goes into the air" + _c("quest-perfect-dehu") +
      _c("streit2023-water") + "."),
    figure(_FIGS["waterbal"], 3,
      "The balance of water for the example room. You apply 240 L of water. The drain collects 60 L "
      "as runoff. The tissue keeps approximately 5 L. The remaining approximately 175 L/day goes "
      "into the air, and the climate system must condense it to liquid again. Water in and water "
      "out are approximately equal" + _c("quest-perfect-dehu") + "."),
    steps([
      ("Count the water that goes in", "40 m&sup2; of canopy &times; 6 L/m&sup2;/day at the middle of "
       "flowering = <strong>240 L/day</strong>. The irrigation controller records this number."),
      ("Subtract the runoff that you collect", "25% runoff to the drain = 60 L. This water does not touch the "
       "air. 240 &minus; 60 = <strong>180 L/day stays in the room</strong>. (Runoff that stays in "
       "trays evaporates and becomes latent heat load again. Drain the runoff.)"),
      ("Subtract the water that the plant keeps", "Plant tissue holds only a small percentage of the water "
       "that the plant absorbs. Use 5 L/day. The remaining water transpires" +
       _c("desertaire-an25-load") + ". <strong>Approximately 175 L/day becomes vapor.</strong>"),
      ("Change to pints for the data sheet", "175 L &divide; 0.473 = <strong>approximately 370 US "
       "pints/day</strong>. The easy method of Quest (gallons that you apply minus gallons of "
       "runoff, times 8) gives the same result" + _c("quest-perfect-dehu") + "."),
    ]),
    figure(L.line("Example irrigation in a flowering cycle. The latent heat load changes with it.",
            [("w1", 2.5), ("w2", 3.0), ("w3", 4.0), ("w4", 5.0), ("w5", 6.0), ("w6", 6.0),
             ("w7", 5.5), ("w8", 5.0), ("w9", 4.0)],
            ["wk 1", "wk 2", "wk 3", "wk 4", "wk 5", "wk 6", "wk 7", "wk 8", "wk 9"],
            ylab="L/m²/day", ymin=0, ymax=7,
            note="Example drip schedule. The dehumidification load changes with it. The peak is in the middle and last weeks of flowering."), 4,
      "The latent heat load is not constant. It increases with the crop. It has its peak when the "
      "canopy has the highest density and the risk of mold is highest. Select the capacity for the "
      "week of the peak load, not for the average load."),
    callout("tip", "Calculate the load from the data of your room",
      p("It is not necessary to make a model of the transpiration, because you measure it. The "
        "liters of water that go in (from the log of the controller) minus the liters of runoff "
        "(measure the runoff for one typical day) are the latent heat load for one day. Do this for "
        "each room and for each crop stage. These data are better than the estimate of a "
        "consultant, and you have them.</p><p>Record the load in each cycle. The record also shows "
        "when the crop uses a different quantity of water than usual. A different quantity of water "
        "is a signal of plant health, and not only a signal for the HVAC system.")),
  ]})

# ---------------------------------------------------------------- 06 folklore vs load calc
SECTIONS.append({"id": "rules-of-thumb", "kicker": "06 · The size of the cooling system", "title": "Calculate the cooling load",
  "blocks": [
    p("Each forum tells you &ldquo;3,000 to 4,000 BTU for each 1,000 W of light&rdquo;. This number "
      "is not from horticulture. It is a change of units: 1 W of electricity always makes 3.412 "
      "BTU/h of heat, because of physics" + _c("hydrobuilder-ac-sizing") + ". The forum number is "
      "approximately correct for the lights, but it does not include the other equipment. As a "
      "result, rooms have a cooling capacity that is 20 to 30% less than the correct capacity."),
    figure(L.bars("Forum numbers compared with the heat of the room",
            [("3 BTU/W (forum)", 6.2), ("4 BTU/W (forum)", 8.2),
             ("all equipment", 9.3), ("+25% margin", 11.6)], unit=" kW", maxv=13,
            note="10 × 700 W LED example room. 1 kW of electricity = 3,412 BTU/h of heat. The forum numbers count only the lights."), 5,
      "The forum numbers (the two bars on the left) include only the lights. The dehumidifiers, the "
      "fans and the persons also make heat. The margin prevents operation at 100% of the capacity "
      "on a day of 35 &deg;C (95 &deg;F)."),
    steps([
      ("List each watt in the room", "Lights 7,000 W. Dehumidifiers 1,600 W. Fans and pumps 500 W. "
       "Two persons approximately 240 W" + _c("hydrobuilder-ac-sizing") + ". Heat from the "
       "envelope: approximately 0 here. It is not zero if your room has a hot roof or a wall in the "
       "sun."),
      ("Add the values", "7,000 + 1,600 + 500 + 240 = approximately <strong>9.3 kW of sensible heat load</strong>."),
      ("Change to BTU/h and tons", "9.3 kW &times; 3,412 = approximately 31,700 BTU/h = approximately "
       "2.6 tons of cooling."),
      ("Add a margin", "A margin of 20 to 25% is for high external temperatures, dirty "
       "coils and capacity that becomes smaller with time" + _c("hydrobuilder-ac-sizing") +
       ". Select approximately <strong>11.6 kW (approximately 40,000 BTU/h, approximately 3.3 "
       "tons)</strong>."),
      ("Divide the capacity between units", "Two smaller units are better than one large unit. They give "
       "capacity in stages for small loads. If one unit stops, half of the cooling continues to "
       "operate (Section 12)."),
    ]),
    callout("warn", "When the forum numbers are not correct",
      ul(["<strong>Rooms in which air flows through the lights and out to the external "
          "air.</strong> Some of the heat does not go into the room. As a result, the forum numbers "
          "give a capacity that is too large. (This condition is the source of the number &ldquo;3 "
          "BTU/W for vented HPS&rdquo;.)",
          "<strong>Spaces without insulation:</strong> containers, garages and top floors below hot "
          "roofs. The envelope load can add kilowatts that the forum numbers do not include.",
          "<strong>The load does not include the dehumidifiers.</strong> The dehumidifiers add "
          "their electrical power <em>and</em> they release the latent heat of each condensed liter "
          "as sensible heat. If the AC size does not include this heat, the AC can be too small in "
          "the afternoon.",
          "<strong>The cooling capacity is not the capacity for latent heat.</strong> A nameplate "
          "kW of cooling (the kW that the manufacturer gives) is the capacity for sensible heat and "
          "for latent heat together. The part that removes moisture changes if the coil temperature "
          "or the airflow changes. The next section shows how to calculate the capacity for "
          "moisture correctly."])),
  ]})

# ---------------------------------------------------------------- 07 dehu sizing
SECTIONS.append({"id": "dehu-sizing", "kicker": "07 · The size of the dehumidifiers", "title": "Calculate the dehumidifier capacity",
  "blocks": [
    p("To calculate the dehumidifier capacity, start with the water balance from Section 05. Then "
      "make two corrections that most persons do not make. The first correction is for the "
      "<strong>time</strong> at which the moisture goes into the air. The second correction is for "
      "the <strong>quantity of moisture that the unit removes at your conditions</strong>, and not "
      "at the rating conditions of the unit."),
    steps([
      ("Start with the dehumidification load", "Example room: approximately 175 L/day = approximately 370 pints/day in total."),
      ("Divide the day and the night", "Transpiration does not stop when the lights are off. The stomata "
       "close in part, and water continues to evaporate from the media. Use a ratio of 70/30 for "
       "the day and the night. The day has 122 L in 12 h (approximately 10 L/h), and <strong>the "
       "night has 53 L in 12 h (approximately 4.4 L/h)</strong>. Compare the ratio with the "
       "condensate volumes of your room and correct it. The ratio changes with the cultivar and the "
       "night climate."),
      ("The day load", "When the lights are on, the AC coils condense some of the moisture during the "
       "cooling. The dehumidifiers remove the remaining moisture. This period is easy."),
      ("Use the night load for the size", "When the lights are off, there is no sensible heat load, and "
       "the AC stops. The moisture that the AC removes during the cooling also stops" +
       _c("desertaire-an25-load") + ". <strong>Only the dehumidifiers remove moisture, and they "
       "must remove 4.4 L/h.</strong> This <em>rate</em> of removal is equal to 105 L/day."),
      ("Correct the nameplate capacity", "Manufacturers give the ratings at a warm temperature, usually 26.7 "
       "&deg;C (80 &deg;F) and 60% RH. Refrigerant units remove less water when the room becomes "
       "colder" + _c("sylvane-desiccant") + ". The curve from the manufacturer can show "
       "approximately &#8532; of the nameplate capacity at a night temperature of 19 &deg;C (66 "
       "&deg;F). Then approximately 160 L/day of nameplate capacity must be in <em>operation</em> "
       "to hold the night conditions. For example, use two 80 L/day units at maximum capacity."),
      ("Then apply N+1", "If two units supply only the night capacity, a failure of one unit causes "
       "crop loss. Install three units of 80 L/day (or two units of 120 L/day). Then one unit can "
       "stop on a Saturday night without a problem (Section 12)."),
    ]),
    table(["Canopy", "Water in (6 L/m²/day)", "Vapor to remove", "In pints"], [
      ["10 m² (tent or small room)", "60 L/day", "approximately 44 L/day", "approximately 92 pints/day"],
      ["20 m²", "120 L/day", "approximately 87 L/day", "approximately 185 pints/day"],
      ["40 m² (example room)", "240 L/day", "approximately 175 L/day", "approximately 370 pints/day"],
      ["80 m²", "480 L/day", "approximately 349 L/day", "approximately 738 pints/day"],
    ], cls="compact", caption="These values come from arithmetic only. They use irrigation of 6 "
       "L/m²/day and 25% collected runoff. Approximately 97% of the water that stays in the room "
       "becomes vapor. For the irrigation schedule of your room, multiply the values by the ratio "
       "of your irrigation to this irrigation. Then correct the nameplate capacity for your night "
       "temperature and add N+1."),
    p("For each fixture, the example gives 17.5 L (approximately 37 pints) for each light each day. "
      "This number is easy to use, but it comes from the irrigation schedule and it is not a "
      "property of the light. The field guidance of Quest is 0.5 to 2 pints for each square foot of "
      "canopy each day" + _c("quest-dehu101") + ". The example room is in this range, with "
      "approximately 0.86 pints for each square foot. If an approximate number and your arithmetic "
      "agree, you can accept the arithmetic. If they do not agree, use the arithmetic."),
    callout("note", "The result is different for a sealed room and for a room with vents",
      p("The values above are for a sealed room with recirculating air. A sealed room with "
        "CO&#8322; enrichment is the usual room for flowering. A room with vents sends the moist "
        "air out and does not condense it.</p><p>Thus the necessary dehumidifier capacity is less, "
        "but the external climate has an effect on the room. In a summer with high humidity "
        "(Auckland in February, most of Queensland), the air that goes into the room can "
        "<em>add</em> latent heat load and not remove it. The capacity for a room with vents starts "
        "from the psychrometric data for your location, and not from this table.")),
  ]})

# ---------------------------------------------------------------- 08 equipment classes
SECTIONS.append({"id": "equipment", "kicker": "08 · The equipment", "title": "Types of HVAC equipment",
  "blocks": [
    p("There are four types of cooling equipment. You add dehumidifiers to all of them. Engineers "
      "divide the equipment into the same types. At the lowest capital cost, the system is a "
      "packaged unit with direct-expansion (DX) cooling and room dehumidifiers. In the middle, the "
      "system is a DX unit with hot-gas reheat. For a large facility, the system uses chilled water" +
      _c("streit2023-hvacd") + "."),
    figure(_FIGS["equipment"], 6,
      "The four types. The capital cost increases from left to right and from top to bottom. The "
      "quality of control increases in the same direction, and it is easier to add spare equipment" +
      _c("streit2023-hvacd") + "."),
    grid([
      card("Mini-split or multi-split",
        p("A refrigerant line goes to a unit on the wall or on the ceiling. The capital cost is "
          "low, you can get the unit in all areas, and you can install it in one day. The unit is "
          "for cooling, and it removes moisture only as a secondary effect. The control is a wall "
          "thermostat with a tolerance of &plusmn;1 to 2 &deg;C (&plusmn;2 to 4 &deg;F), and there "
          "is no reheat. Thus the unit decreases the temperature too much when it removes moisture. "
          "It is correct for rooms for vegetative growth, for drying rooms and for small flowering "
          "rooms <em>with</em> room dehumidifiers that remove the moisture."), tag="low cost"),
      card("Packaged unit or rooftop unit (RTU)",
        p("One cabinet from the manufacturer is external to the envelope. It has ducts for supply "
          "air and return air. It has direct-expansion (DX) cooling and a high airflow. You can do "
          "the maintenance from an external area.</p><p>This type is standard for one room and for "
          "small facilities. Use dehumidifiers with it also. We recommend compressors with stages "
          "or inverter compressors, and not single-stage compressors" + _c("streit2023-hvacd") +
          "."), tag="standard"),
      card("Chilled water and fan coils",
        p("A central chiller makes cold water. Pipe loops with insulation supply the water to fan "
          "coil units in each room. The system can supply many rooms, and the spare capacity is at "
          "the chillers (two chillers supply cooling to all of the facility). With hot-water coils "
          "or reheat coils, it can control the temperature and the humidity independently" +
          _c("streit2023-hvacd") + ". It must have a mechanical design. Engineers make this system "
          "for each facility, and you cannot select it from a list of units."), tag="scale"),
      card("Integrated unit for grow rooms (HVACD)",
        p("These cabinets are for grow rooms. One cabinet does the cooling, the dehumidification "
          "and the reheat in one controlled sequence. The size comes from the loads that you "
          "calculate, and the control uses the dew point. The manufacturer makes the cabinet for "
          "the problem at lights-off. The capital cost is high. This unit is best for flowering "
          "rooms and drying rooms with accurate control, where a climate error has a large cost" +
          _c("rii-hvac-bpg") + "."), tag="precision"),
    ], cols=2),
    p("<strong>Room dehumidifiers and ducted dehumidifiers.</strong> Room dehumidifiers (above the "
      "canopy or on the floor) have a low capital cost, you can move them, and they are easy to "
      "use. But they release their heat and their noise into the room, and you must remove the "
      "condensate.</p><p>Ducted dehumidifiers are external to the canopy, have drains with correct "
      "pipes, and use the same ducts as the HVAC system. Their installation cost is higher. In the "
      "two types, <strong>connect the drain to a pipe</strong>. Water in a bucket evaporates into "
      "the room again."),
    table(["", "Refrigerant dehumidifier", "Desiccant dehumidifier"], [
      ["How it operates", "The air flows along a cold coil. The vapor condenses to liquid and goes to the drain.", "A desiccant wheel adsorbs the vapor. A heater removes the vapor from the desiccant wheel again."],
      ["Best conditions", "Warm rooms of 18 to 30 &deg;C (64 to 86 &deg;F). These rooms are the rooms for flowering.", "Cool rooms, where ice occurs on coils. The desiccant dehumidifier keeps its full capacity there" + _c("sylvane-desiccant") + "."],
      ["Operation in cold rooms", "The capacity decreases when the room becomes colder. Ice can occur on the coils at less than approximately 15 &deg;C (59 &deg;F).", "Cold does not change its operation. It operates at temperatures near the freezing point" + _c("sylvane-desiccant") + "."],
      ["Heat that the unit adds to the room", "Electrical power of the compressor + latent heat of the condensed water", "More heat. The heater that dries the desiccant wheel puts heat into the airflow, typically +3 to 5 &deg;C or +5 to 9 &deg;F" + _c("sylvane-desiccant") + "."],
      ["Typical use in grow rooms", "The usual selection for rooms for flowering and for vegetative growth.", "Cold drying rooms and curing rooms (16 to 18 &deg;C / 61 to 64 &deg;F), and spaces in winter"],
    ], cls="compact", caption="The usual selection is a refrigerant dehumidifier for the grow room and a desiccant dehumidifier for the cold drying room."),
  ]})

# ---------------------------------------------------------------- 09 lights-off
SECTIONS.append({"id": "lights-off", "kicker": "09 · The primary problem", "title": "Lights-off humidity spike",
  "blocks": [
    p("In the trend graph of a grow room, you see the same change each time. In less than one hour "
      "after the lights go off, the RH increases by 15 to 25 percentage points. Three effects occur "
      "at the same time, and each one increases the RH:"),
    ol([
      "<strong>The sensible heat load stops.</strong> The 7 kW of heat from the lights becomes zero "
      "in one second. The AC condenses moisture as a side effect of the cooling. This removal of "
      "moisture stops when the AC stops" + _c("desertaire-an25-load") + _c("quest-dehu101") +
      ".",
      "<strong>The air becomes colder, and the RH increases with no new water.</strong> When the "
      "temperature decreases by approximately 10 &deg;C (18 &deg;F), the capacity of the air for "
      "vapor becomes approximately half. When the air of the example room changes from 26 &deg;C "
      "(79 &deg;F) and 55% RH to 19 &deg;C (66 &deg;F), the RH is approximately 84%. The quantity "
      "of water in grams is the same, but the air can hold less. The arithmetic of Quest gives the "
      "same result: 57% RH at 24 &deg;C (75 &deg;F) becomes approximately 80% RH at 18 &deg;C (64 "
      "&deg;F)" + _c("quest-dehu101") + ".",
      "<strong>The crop continues to transpire.</strong> The rate is lower when the lights are off, "
      "but it is not near zero. Water also continues to evaporate from wet media all night. In the "
      "example room, the new vapor is approximately 4.4 L each hour.",
    ]),
    figure(_FIGS["lightsoff"], 7,
      "The change at lights-off. The temperature decreases, and the RH increases in the direction "
      "of the mold range. The dehumidification capacity that you installed, or did not install, "
      "causes the difference between the RH at the spike and your night target."),
    figure(L.zones("Humidity in a flowering room, and the start of problems", 30, 80,
            [(30, 40, L.AMBL, "too dry"), (40, 60, L.GL, "flowering range"),
             (60, 70, L.AMBL, "near limit"), (70, 80, L.REDL, "mold zone")], unit="% RH",
            note="Room sensor values. The canopy air is wetter than at a wall sensor. Thus the margin is smaller than the sensor shows."), 8,
      "In the last weeks of flowering, the RH must be in the lower half of the range. Each hour "
      "with an RH of more than approximately 70% at night is an hour in the climate that is best "
      "for <em>Botrytis</em>" + _c("punja-budrot-cjb") + "."),
    p("<strong>This period is very important.</strong> Bud rot (<em>Botrytis cinerea</em>) occurs "
      "in cool air that is almost saturated and does not move. Colas with high density in the last "
      "weeks of flowering contain this microclimate in their inner area" + _c("punja-budrot-cjb") +
      ". The room has its highest RH at its lowest temperature. The crop is at the stage with the "
      "highest risk.</p><p>Dew occurs on each surface that is colder than the dew point. At 26 "
      "&deg;C (79 &deg;F) and 55% RH, dew occurs on each surface that is colder than approximately "
      "16 &deg;C (61 &deg;F). Examples are the surfaces of ducts, external walls and cold glass. "
      "The capacity for the latent heat load at night, which you calculate in Section 07, is not "
      "for comfort. It is for mold control."),
    callout("tip", "Dry the air before lights-off, and decrease the light slowly",
      ul(["<strong>Dry the room before lights-off:</strong> operate the dehumidifiers at maximum "
          "capacity in the last hour of lights-on. Thus the room goes into the night at the lower "
          "end of its RH range, with headroom.",
          "<strong>Decrease the light in a ramp, and not in one step.</strong> If your controller "
          "can do this, decrease the lights in stages in 15 to 30 minutes. Thus the AC and the "
          "dehumidifiers have time to adjust to the change.",
          "<strong>Use the heat of the dehumidifiers.</strong> A dehumidifier releases "
          "approximately 0.68 kWh as heat for each liter of water, plus its electrical power. In "
          "the example room, the heat is approximately 4.6 kW during the night. It is usually most "
          "of the heat that is necessary to hold 19 &deg;C. This night heating has no cost, because "
          "the dehumidifiers must operate at night.",
          "<strong>Set an alarm for the rate at which the RH increases.</strong> If the RH "
          "increases faster than the spike that you calculated, a dehumidifier is not in operation. "
          "It is better to get the alarm at 22:10 than to find mold at 07:00."])),
    callout("danger", "Drops of water on surfaces at lights-off: do the steps that night",
      p("If you see drops of water on walls, ducts or fixtures at lights-off, the room has liquid "
        "water. Liquid water is very bad for the crop, because of the risk of "
        "<em>Botrytis</em>.</p><p>Do these steps that night. Increase the night temperature "
        "setpoint by one degree (air at a higher temperature holds the same water at a lower RH). "
        "Operate each dehumidifier that you have. Open the canopy with airflow.</p><p>Then increase "
        "the capacity before the next period with the lights off. Do not wait for the next crop.")),
  ]})

# ---------------------------------------------------------------- 10 airflow integration
SECTIONS.append({"id": "airflow", "kicker": "10 · Airflow in the room", "title": "HVAC supply air, return air and circulation",
  "blocks": [
    p("The climate system supplies conditioned air, and the air must go to <em>all</em> parts of "
      "the room. There are two systems with two tasks. The air handling loop supplies conditioned "
      "air and moves the warm, moist air to the coils again. A sealed grow room typically moves a "
      "volume of air equal to the room volume 20 to 40 times each hour. The air is approximately "
      "100% recirculating air, to keep the CO&#8322; in the room and to keep external contaminants "
      "out" + _c("streit2023-hvacd") + ". Circulation fans move the air in the canopy, and thus no "
      "leaf stays in a boundary layer of high humidity (the <a href='airflow-design.html'>airflow "
      "design paper</a> gives information about this)."),
    figure(_FIGS["crosssection"], 9,
      "The supply air is at the top on one side, and the return air is at the bottom on the other "
      "side. Thus the conditioned air flows through the canopy zone and not above it. Circulation "
      "fans move the air for the last meter. The dehumidifier drains into a pipe and not into a "
      "bucket."),
    ul([
      "<strong>Put the supply air at the top and the return air at the bottom.</strong> Dry supply "
      "air has a lower density. The air paths are less important than the geometry. Supply the air "
      "across the ceiling and remove the return air at floor level. Thus the air flows through the "
      "canopy, where the load is.",
      "<strong>Do not let the supply air go directly to the return air.</strong> If a supply "
      "diffuser sends air directly into a return air inlet near the diffuser, the conditioned air "
      "stays in the duct system. It does not go into the room. Sensors near that airflow show good "
      "values, but there is rot in the far corner.",
      "<strong>Select the position of the dehumidifiers carefully.</strong> Point the discharge air "
      "along a wall or an aisle. Do not point the hot, dry air at one bench of plants. Put the "
      "intake in the moist zone, and not in the dry plume of the unit. If the intake receives the "
      "discharge air of the same unit, its sensor measures dry air and the unit does not operate. "
      "The canopy stays wet.",
      "<strong>Monitor the compressor for short cycling.</strong> Short cycling occurs when a "
      "single-stage AC is much too large. The room temperature becomes equal to the thermostat "
      "setpoint in minutes, and the AC stops. The coil does not become cold and wet for a "
      "sufficient time to condense much water. You get temperature control, but no "
      "dehumidification, and the compressor has more damage from operation. Capacity in stages or "
      "an inverter, with timers for a minimum operation time, corrects this problem.",
    ]),
  ]})

# ---------------------------------------------------------------- 11 condensate
SECTIONS.append({"id": "condensate", "kicker": "11 · The water from the air", "title": "Condensate drains, measurement and reuse",
  "blocks": [
    p("The water that the coils and the dehumidifiers condense must go away from the equipment. In "
      "the example room, the quantity is approximately 175 L/day. This flow is, in this sequence, a "
      "maintenance problem, a no-cost instrument and a possible source of water."),
    ul([
      "<strong>A maintenance problem:</strong> each unit must have a drain with a trap and a slope, "
      "or a good condensate pump with a float switch. Biofilm occurs in pans and trays, and the "
      "water falls on the canopy. A blocked drain stops a good unit, but in other units the water "
      "flows into the ceiling. Maintenance of the trays and the drains is a task in integrated pest "
      "management (IPM), and it is necessary.",
      "<strong>A no-cost instrument:</strong> when you measure the condensate, you measure the "
      "latent heat load. If the condensate decreases and the irrigation is constant, the runoff is "
      "larger or the removal capacity is smaller. Find the cause by the next morning.",
      "<strong>A source of water:</strong> most of the irrigation water that you apply becomes "
      "condensate again, and this condensate is almost distilled water. You can collect it and use "
      "it again" + _c("streit2023-water") + ".",
    ]),
    figure(L.flow("Correct reuse of condensate",
            [("Collect", "From coil and trays to one tank"),
             ("Filter", "Sediment filter and carbon filter"),
             ("Disinfect", "UV or AOP. Tray water contains microbes."),
             ("Adjust", "RO or mix to target EC"),
             ("Reuse", "Add to irrigation supply")],
            note="Apply the treatment for raw water to condensate, not for RO permeate. It touches coils, trays and drain pipes."), 10,
      "The reuse steps. Condensate has a low EC and a typical pH of 5.5 to 6.5. But it can contain "
      "VOCs, metals from the coils (copper, zinc and lead), and microbes from wet trays. Apply a "
      "treatment to it before it touches the crop" + _c("ncia-condensate") + "."),
    callout("note", "Compliance",
      p("In a GACP quality system, and in most medical license systems, you must control the "
        "quality of the irrigation water and record it. If condensate goes into the crop water "
        "again, your water SOP must include its treatment steps and its test results, as for the "
        "source water. The decision about condensate in the crop water, and its record, are "
        "necessary <em>before</em> an audit" + _c("ncia-condensate") + ".")),
  ]})

# ---------------------------------------------------------------- 12 redundancy
SECTIONS.append({"id": "redundancy", "kicker": "12 · When equipment stops", "title": "Redundancy for failures",
  "blocks": [
    p("Calculate the effect of a failure before it occurs. Example room, week 6, 23:00: two units "
      "of 80 L/day hold the night at approximately ⅔ of the nameplate capacity. One unit stops "
      "because of a defective capacitor. Do the arithmetic: the air in the room is approximately "
      "150 m&sup3; at 19 &deg;C (66 &deg;F) and 60% RH. This air can absorb only approximately "
      "<strong>one more liter of water</strong> before saturation.</p><p>The crop adds "
      "approximately 4.4 L each hour. The remaining unit removes approximately half of this "
      "quantity. In less than one hour, the RH is at its maximum, and condensation starts on the "
      "coldest surfaces. No other equipment in the room can help, because the AC has no sensible "
      "heat load and does not operate.</p><p>The change is not slow, and you do not find it when "
      "you walk through the room in the morning. The RH increases in minutes."),
    p("<strong>N+1</strong> redundancy is the correct method. N units supply the calculated load, "
      "and you install one more unit. Thus, if one unit stops, the remaining units give the full "
      "capacity. Apply it in the sequence of the failures that cause the fastest crop loss:"),
    ol([
      "<strong>Night dehumidification first.</strong> There is no alternative. When a dehumidifier "
      "stops at night, no other equipment removes water. Use three units of 80 L/day where two "
      "units supply the load.",
      "<strong>Cooling second.</strong> For a cooling failure in the day, there is an alternative: "
      "decrease the load. Connect the lights to the cooling with an interlock. When a cooling fault "
      "occurs, the interlock decreases the light to 50% or stops the lights. You can accept one day "
      "with no photosynthesis, but you cannot accept 40 &deg;C for a full photoperiod. Two smaller "
      "ACs are also better than one large AC for this.",
      "<strong>Controls and alarms last.</strong> A spare unit that is defective, and that you do "
      "not know about, gives no protection. Alarms must go to a person who can correct the problem. "
      "The alarms must continue to operate during the same power failure that caused the fault.",
    ]),
    grid([
      card("Night dehumidifier stops", p("The RH increases in minutes (arithmetic above). <strong>How you "
        "find it:</strong> an alarm for the rate at which the RH increases. "
        "<strong>Protection:</strong> N+1 capacity, automatic start after the unit stops, and a "
        "spare capacitor in storage."), tag="worst condition"),
      card("Day AC stops", p("The 9 kW of heat continues to come into the room, and it has no exit. "
        "In a sealed room, the temperature increases by some degrees each hour. <strong>How you "
        "find it:</strong> a temperature alarm and a current sensor on the unit. "
        "<strong>Protection:</strong> the lights interlock decreases the load automatically, and "
        "the second unit supplies the cooling for a day with a lower load."), tag="has an alternative"),
      card("Condensate drain is blocked", p("Water is in a position where it must not be, and the float "
        "switch stops the unit. The result is a failure of capacity with no signal. <strong>How you "
        "find it:</strong> an alarm for a stopped unit, and an inspection of the trays each week. "
        "<strong>Protection:</strong> drains with pipes, a test of the float switches each month, "
        "and the trays in the maintenance schedule."), tag="no signal"),
      card("Ice on the coil", p("The causes are not sufficient airflow (dirty filter), low refrigerant "
        "charge, or a room that is too cold. The unit operates but removes no water. Then the ice "
        "melts, and the water falls from the unit. <strong>How you find it:</strong> operation time "
        "with no condensate flow. <strong>Protection:</strong> a filter schedule, units that can "
        "defrost, and a desiccant dehumidifier in spaces that are very cold" + _c("sylvane-desiccant") +
        "."), tag="slow problem"),
      card("Sensor gives incorrect values", p("The controller uses the incorrect value, and the room "
        "changes to the incorrect condition. <strong>How you find it:</strong> a check each month "
        "with a good handheld meter at canopy height. <strong>Protection:</strong> two sensors in "
        "each room, and control with the worse reading."), tag="dangerous, no signal"),
      card("Short power failure", p("All the equipment stops. It is necessary to know which equipment starts "
        "again. A compressor must have a timer for the interval before it starts again, and some "
        "dehumidifiers go to standby mode and do not operate. A room can look as if it has power, "
        "but the equipment does not operate.</p><p><strong>How you find it:</strong> a checklist "
        "after a power failure, and alarms with power from an uninterruptible power supply (UPS). "
        "<strong>Protection:</strong> do a test of the start after a power failure. Do the test one "
        "time, at a time that you select, and before a power failure in the summer."), tag="make a test"),
    ], cols=2),
    callout("key", "Stop the equipment at a time that you select",
      p("Do this test one time in each cycle, at the start of vegetative growth, when the risk is "
        "low. Stop each climate unit for one hour and monitor the trends. You will know how much "
        "time you have before the problem becomes dangerous (minutes or hours). You will also know "
        "if the alarms operate and if the units start again automatically. This test has a low "
        "cost. It is the only method to make sure that your N+1 is correct and not only a nameplate "
        "value.")),
  ]})

# ---------------------------------------------------------------- 13 controls
SECTIONS.append({"id": "controls", "kicker": "13 · Controls", "title": "Stages and deadbands of the HVAC controls",
  "blocks": [
    p("In a grow room, the heating, the cooling and the dehumidification operate near each other. "
      "Two of the three make the task of the third worse: cooling increases the RH, and "
      "dehumidification adds heat. If there is no control sequence, the units decrease the result "
      "of each other. The AC decreases the temperature too much, the RH increases, the dehumidifier "
      "adds heat, and the AC starts again. This cycle uses much electrical power and causes the "
      "compressors to start and stop many times. The correct method is a control sequence, and not "
      "larger equipment."),
    figure(L.flow("The control loop in stages",
            [("Read", "T + RH aspirated probe at canopy height"),
             ("Compare", "With the day or night setpoint and deadband"),
             ("Stage", "Cooling, dehumidification, then heating"),
             ("Hold", "Minimum on/off timers stop short cycling"),
             ("Log", "Record all values. Use the graph to adjust.")],
            note="One controller for each control variable. If not, each unit decreases the result of the other unit all night."), 11,
      "The loop that each good controller uses. The deadband is the tolerance around the setpoint, "
      "where no equipment starts or stops. The deadband gives each unit time to complete its task "
      "before the next unit starts."),
    ul([
      "<strong>Deadbands:</strong> control to a band and not to one value. For example, the "
      "setpoint in the day is 26 &deg;C (79 &deg;F) &plusmn;0.5 &deg;C, and the RH is 55 to 60%. "
      "Your values are different, because the crop gives the setpoints (read the <a "
      "href='temp-humidity-vpd.html'>VPD paper</a>). The photosynthesis of cannabis operates "
      "correctly at approximately 25 to 30 &deg;C (77 to 86 &deg;F)" + _c("chandra2008-photo") +
      ". A small band can show good control, but it mostly causes frequent starts and stops of the "
      "equipment.",
      "<strong>Sequence:</strong> the heating and the cooling must not operate at the same time "
      "(use a lockout between them). The dehumidification can operate with the heating or with the "
      "cooling. We recommend that the reheat comes from the unit, for example hot-gas reheat, and "
      "not from heaters that decrease the result of the AC" + _c("streit2023-hvacd") +
      ".",
      "<strong>Setpoints for the day and for the night, with ramps.</strong> Use different targets "
      "for lights-on and for lights-off. Connect them with ramps of 15 to 30 minutes. Thus you "
      "control the change (Section 09).",
      "<strong>Control the moisture with the dew point when you can.</strong> The %RH changes with "
      "each small change of temperature, also when the water content is the same. The dew point "
      "shows the quantity of water in grams. At the change between day and night, control with the "
      "dew point is much more stable.",
      "<strong>The position of the sensor is a control decision.</strong> Use an aspirated sensor, "
      "or a sensor with a good shield, at canopy height. Put it away from a jet of supply air and "
      "from the plume of a dehumidifier. The controller can be only as accurate as its sensor "
      "(Section 12, sensor with incorrect values).",
    ]),
  ]})

# ---------------------------------------------------------------- 14 efficiency
SECTIONS.append({"id": "efficiency", "kicker": "14 · The energy cost", "title": "HVAC efficiency, reheat and heat recovery",
  "blocks": [
    p("The climate system is a large part of the energy cost. Energy is 30 to 60% of the operating "
      "cost of an indoor facility" + _c("rii-hvac-bpg") + ". A life-cycle analysis of indoor "
      "production in the US found that environmental control is the primary cause of energy use and "
      "of emissions. The emissions are 2,300 to 5,200 kg CO&#8322;e for each kg of dried flower, "
      "and the value changes with the location" + _c("summers2021-ghg") + ". Each selection of "
      "equipment in this section changes that number."),
    kv([
      ("1 kW of electricity", "3,412 BTU/h of heat, always"),
      ("1 ton of cooling", "12,000 BTU/h = approximately 3.52 kW"),
      ("1 US pint", "0.473 L"),
      ("Condensation of 1 L of vapor", "approximately 0.68 kWh of latent heat that the coil releases"),
      ("Resistance heater", "COP 1.0. This type of heat has the highest cost."),
      ("New compressor", "COP 3 to 4. It moves 3 to 4 kW of heat for each kW that it uses."),
    ]),
    ul([
      "<strong>Hot-gas reheat is the best method.</strong> For dehumidification, the unit decreases "
      "the air temperature to less than its dew point. Then the unit increases the air temperature "
      "again, and thus the room does not become too cold. Electric reheat uses new electrical power "
      "(COP 1) for heat that you removed. Hot-gas reheat uses the heat that the compressor releases "
      "for the reheat. The cost of this reheat is almost zero, and it is standard on DX units of "
      "medium cost and on integrated units" + _c("streit2023-hvacd") + ".",
      "<strong>Select the correct size, and do not select a size that is too large.</strong> A "
      "single-stage unit that is too large has short cycling. The result is worse dehumidification, "
      "lower efficiency and a shorter life of the compressor. Put the margin in capacity in "
      "<em>stages</em> (two circuits or an inverter) and not in one very large unit.",
      "<strong>LEDs change the ratio, but not the physics.</strong> At the same PPFD, LEDs use less "
      "electrical power, and thus the sensible heat load decreases. But the crop transpires almost "
      "the same quantity of water, and thus the latent heat load does not decrease. In LED rooms, "
      "the latent heat load is the primary load. As a result, the dehumidifier capacity and the "
      "heating in winter are <em>more</em> important, and not less important.",
      "<strong>Use again the heat of your equipment.</strong> The heat from the dehumidifiers holds "
      "the night temperature (Section 09). Heat from the condenser can increase the temperature of "
      "drying rooms or of water. You can send heat to the external air in winter and operate COP-1 "
      "heaters in the room at the same time. Then the high energy cost is your selection.",
      "<strong>Maintenance increases efficiency.</strong> Dirty filters and dirty coils decrease "
      "the capacity and the COP for months, with no alarm, before a unit stops. Clean or replace "
      "the filters each month. Clean the coils in each cycle.",
    ]),
  ]})

# ---------------------------------------------------------------- 15 troubleshooting
SECTIONS.append({"id": "trouble", "kicker": "15 · When there is a problem", "title": "Troubleshooting",
  "blocks": [
    table(["Symptom", "Possible cause", "First steps"], [
      ["The RH is 80% or more at each lights-off", "The latent heat load at night is more than the corrected dehumidifier capacity. The AC does not operate at night.", "Measure the water that goes in minus the runoff. Compare it with the installed capacity at the night temperature (Sections 05 to 07). Dry the air in the last hour of lights-on. Add nameplate capacity."],
      ["The temperature of the room increases slowly in the afternoon, and the AC does not stop", "The AC is too small for the full equipment load, the coil or the filter is dirty, or the refrigerant is low", "Count the watts again (Section 06). Clean the coils. Replace the filters. Then get a refrigeration technician."],
      ["The AC starts and stops frequently. The temperature is correct, but the RH does not decrease.", "A single-stage unit that is too large has short cycling. The coil does not stay cold for a sufficient time to condense water.", "Use timers for a minimum operation time. Use capacity in stages or an inverter. Let the dehumidifiers remove the moisture."],
      ["The room is cold <em>and</em> has high humidity", "The cooling operates without reheat, and the problem is frequent when a mini-split is the dehumidifier.", "Increase the cooling setpoint. Add a dehumidifier with reheat (or a unit with hot-gas reheat). Use different equipment for the heating and for the dehumidification."],
      ["Condensation on ducts and walls at night", "The surfaces are colder than the dew point of the air", "Add dehumidifier capacity for the night. Increase the night temperature by a small value. Install insulation on cold surfaces. Measure the result with an IR thermometer."],
      ["The dehumidifier operates all the time, but the tank fills very slowly", "The room is colder than the rating conditions, the coil has ice, or the intake receives the dry plume of the same unit", "Examine the coil for ice and the filter for dust. Read the capacity curve for your temperature. Change the position of the unit. Use a desiccant dehumidifier if the space is very cold."],
      ["Smell of mold, and stains below the units", "Blocked condensate pans or traps, and biofilm in trays", "Clean the trays. Disinfect the trays. Flush the drains. Make sure that the float switch operates. Add the trays to the maintenance schedule for each week."],
      ["One corner is always wetter, and mold starts there", "Dead zone in the airflow", "Correct the geometry of the supply air and the return air (Section 10). Add circulation. Decrease the density of the canopy. Measure the result with a handheld meter."],
      ["The sensors show correct values, but rot occurs on the buds", "The sensor on the wall does not show the microclimate of the canopy", "Measure in the canopy at the height of the colas. Control with the dew point. Add airflow through the canopy" + _c("punja-budrot-cjb") + "."],
    ], cls="compact", caption="Start at the top of the table and continue to the bottom. Measure before you replace equipment. Most &lsquo;broken HVAC&rsquo; equipment operates correctly, but the information that it uses is incorrect."),
  ]})

# ---------------------------------------------------------------- 16 mental model
SECTIONS.append({"id": "remember", "kicker": "16 · Keep this", "title": "Heat and moisture balance",
  "blocks": [
    callout("key", "The primary model",
      p("<strong>Count the watts.</strong> Each kilowatt of equipment becomes a kilowatt of heat, "
        "and the total is the sensible heat load. <strong>Then count the liters.</strong> Each "
        "liter that you apply, minus the drain, becomes vapor, and the total is the latent heat "
        "load. The climate system removes the two loads. It must operate at 02:00 with the lights "
        "off and at 14:00 with the lights on.")),
    ol([
      "Count the watts to get the sensible heat load. The forum numbers count only the lights, but you count all the equipment (Section 06).",
      "Count the liters to get the latent heat load. Use the water that goes in minus the runoff, and change it to pints for the data sheet (Sections 05 and 07).",
      "Use the night load for the size. At night there is no sensible heat load, the AC does not help, and transpiration continues. Calculate the dehumidifier capacity for lights-off at <em>your</em> night temperature, and correct the nameplate capacity.",
      "Use N+1 for the night dehumidification. Connect the lights to the cooling with an interlock. Then stop each unit one time, at a time that you select, and monitor the result.",
      "Control the moisture (dew point) with deadbands and a control sequence. Thus the units operate together. Use a ramp for the change between day and night.",
      "Measure the irrigation, the runoff and the condensate. These measurements give the load continuously at no cost, and they also show when the crop changes.",
    ]),
    p("The climate system is one part of the grow room. Read this paper with the <a "
      "href='grow-room-systems.html'>grow room systems paper</a>. For the correct setpoints, read "
      "the <a href='temp-humidity-vpd.html'>temperature, humidity and VPD paper</a>. For the last "
      "meter of air movement, read the <a href='airflow-design.html'>airflow design paper</a>."),
  ]})
