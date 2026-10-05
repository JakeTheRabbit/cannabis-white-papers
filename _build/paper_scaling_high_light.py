# -*- coding: utf-8 -*-
"""Paper: scaling light to the limiting factor (advanced)."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        grid, card)
import figs_lib as L

SLUG = "scaling-high-light"
TITLE = "Set the light to the limiting factor"
EYEBROW = "Advanced · High light"
SUB = ("When you increase the light, the room must supply more CO₂, water, airflow and feed, and "
       "must remove more heat. This paper shows how to calculate the PPFD limit of each supply "
       "system. The lowest limit is the PPFD limit of your room. The paper also shows the equipment "
       "that you can add to get a higher limit.")
META = [("gauge", "Advanced"), ("image", "1 diagram · 5 tables"),
        ("quote", "4 sources"), ("clock", "~16 min to read")]
RELATED = ["grow-room-systems", "co2-enrichment", "coco-crop-steering"]
REF_IDS = ["rm2021-light", "chandra2008-photo", "faust2018-dli", "collado2025-light"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

def _tag(cls, txt):
    return "<span class='tag %s'>%s</span>" % (cls, txt)

def _fig_ceiling():
    return L.bars(
        "System PPFD limits. The lowest limit is the room limit",
        [("CO&#8322;", 1500), ("Irrigation", 1200), ("Cooling", 1140), ("Dehumidifier", 1050)],
        unit="",
        note="Example A: 50 m&sup2; room, 21 kW (6 ton) cooling, 194 L/day (410 pints) dehumidifier, 300 L/day feed, CO&#8322; to 1500 ppm.",
        target=1050, maxv=1600)

SECTIONS = []

SECTIONS.append({"id": "demand", "kicker": "01 · Start here",
  "title": "Purpose and scope",
  "blocks": [
    callout("evidence", "Weak",
      "<p><strong>Limit of the data:</strong> The EC and runoff values for the rows with high PPFD "
      "are for advanced steering. With ambient CO&#8322; at high PPFD, the plant uses the added "
      "light with less efficiency. No test shows that 800 &micro;mol at the canopy is a PPFD limit "
      "for all rooms. Calculate the size of the HVAC and of the water supply from the readings of "
      "your meters. Do not use the value in one cell of a table.</p>"),

    lead("The smallest supply controls the rate of photosynthesis. Light can control the rate only "
         "until a different supply is not sufficient. When a different supply is not sufficient, "
         "more light makes only heat and causes stress to the plant."),
    p("Two laws show this effect. Liebig's <strong>law of the minimum</strong> shows that the "
      "smallest supply controls the growth rate of a crop. This law is correct also when all the "
      "other supplies are very large. Blackman's <strong>law of limiting factors</strong> gives the "
      "same information for the rate of photosynthesis at one time. When you increase the supply of "
      "the limiting factor, the rate increases. When you increase a different supply, the rate does "
      "not change.</p><p>Rodriguez-Morrison and the other authors measured a yield that increases "
      "in a linear relation to 1,800 &micro;mol at ambient CO&#8322;" + _c("rm2021-light") +
      ". Measurements on leaves show that CO&#8322;, light and temperature have an effect on each "
      "other. But they do not show a PPFD limit of 800 &micro;mol at the canopy" +
      _c("chandra2008-photo") + ". A room at 1,500 &micro;mol with ambient CO&#8322; can have low "
      "efficiency, or can cause stress to a cultivar that has a low tolerance for light. Thus use "
      "the crop response and the yield for each kWh to examine the room."),
    p("Calculate <strong>which system has the lowest PPFD limit</strong>. Then increase that limit, "
      "or set the PPFD to a value less than the limit. The paper <a "
      "href='grow-room-systems.html'>Grow-room systems</a> shows that the room is one system. This "
      "paper gives numbers for the system and shows how to find its weakest part."),
    callout("key", "The paper in short",
      p("The light causes the plant to use more CO&#8322;, water and feed. The light also causes "
        "more heat. The room must supply CO&#8322;, water, feed and airflow, and must remove the "
        "heat. The yield increases with the light <em>only when all these supplies are "
        "sufficient</em>. The first supply that is not sufficient gives the PPFD limit of your room.")),
  ]})

SECTIONS.append({"id": "terms", "kicker": "02 · The terms", "title": "Definitions",
  "blocks": [
    p("This paper uses six terms. If you know these terms, go to the next section."),
    defterm("PPFD", "The intensity of the light on the canopy that the plant can use, in "
            "&micro;mol/m&sup2;/s. When you increase the light, you increase this value. PPFD is "
            "the intensity at one time."),
    defterm("DLI", "The daily light integral. It is the total quantity of light that the canopy "
            "receives in one day, in mol/m&sup2;/day. With a 12/12 light cycle, DLI = PPFD &times; "
            "0.0432" + _c("faust2018-dli") + ". DLI is the total light for the day."),
    defterm("Light saturation", "The highest PPFD that a leaf can use. When the PPFD is more than "
            "this value, the light that the leaf cannot use becomes heat. The saturation point "
            "<em>increases</em> when the CO&#8322; and the temperature increase. Thus CO&#8322; "
            "enrichment lets you operate the lights at a higher PPFD" + _c("chandra2008-photo") +
            "."),
    defterm("Limiting factor", "The one supply that is the smallest in relation to the quantity "
            "that the plant can use at the PPFD. Only this supply controls the growth rate. All the "
            "methods in this paper find this one supply."),
    defterm("Sensible heat load and latent heat load", "The climate equipment removes two types of heat. "
            "<strong>Sensible heat</strong> is heat that a thermometer shows. The fixtures make it, "
            "and the cooling system removes it. <strong>Latent heat</strong> is energy in water "
            "vapor, and a thermometer does not show it until the vapor becomes liquid water. The "
            "plants transpire the water vapor, and the dehumidifier removes it from the room. When "
            "the light increases, the two heat loads increase."),
    defterm("Mass flow", "A plant does not use a pump to move water up. The evaporation of water "
            "from the pores of each leaf (the stomata) pulls water up from the roots, and this "
            "movement is the <strong>transpiration stream</strong>. The water at the root zone "
            "contains nutrients in solution, and the transpiration stream moves them to the leaf. "
            "This effect is <strong>mass flow</strong>: the quantity of nutrient that the leaf gets "
            "changes with the rate of transpiration. When the light is brighter, the evaporation is "
            "faster, and more water moves up with more nutrient each day. Thus the <a "
            "href='airflow-design.html'>airflow</a>, the feed EC and the irrigation volume must all "
            "increase when the light increases."),
  ]})

SECTIONS.append({"id": "ladder", "kicker": "03 · The primary tables", "title": "Sequence of light steps",
  "blocks": [
    p("Two tables show the full system, row by row. Find your PPFD in the first column and read "
      "across the row. All the values in the row must be correct at the same time. If they are not "
      "correct, the PPFD in that row is not possible. The first row is for a room with ambient "
      "CO&#8322; (600 &micro;mol). The last row is for a sealed room with all supply systems at "
      "full capacity (1500 &micro;mol)."),
    p("The first table shows the <strong>air and gas</strong> values of each row: the gas that the "
      "plant uses and the climate around the plant."),
    table(
      ["Light (PPFD)", "DLI", "CO&#8322; setpoint", "Air temperature in the day", "VPD (RH)", "Air speed in the canopy", "Result"],
      [
        ["600",  "26", "400&ndash;450 ppm", "25 &deg;C", "1.2 kPa (62%)", "0.3&ndash;0.5 m/s", _tag("g", "Ambient air is sufficient")],
        ["800",  "35", "600&ndash;800 ppm", "26 &deg;C", "1.3 kPa (62%)", "0.4&ndash;0.6 m/s", _tag("g", "CO&#8322; enrichment starts to help the yield")],
        ["1000", "43", "800&ndash;1000 ppm", "27 &deg;C", "1.3 kPa (63%)", "0.5&ndash;0.7 m/s", _tag("w", "CO&#8322; is necessary")],
        ["1200", "52", "1000&ndash;1200 ppm", "28 &deg;C", "1.4 kPa (63%)", "0.6&ndash;0.8 m/s", _tag("w", "Large supply systems")],
        ["1500", "65", "1200&ndash;1500 ppm", "29&ndash;30 &deg;C", "1.4 kPa (65%)", "0.7&ndash;1.0 m/s", _tag("r", "All systems at full capacity")],
      ],
      caption="Table 1 &middot; Climate and gas targets for each PPFD (flowering, 12/12, for each m&sup2; of canopy)",
      foot="The VPD changes only by a small quantity. It is a setpoint for the condition of the "
           "plant, and it does not change with the light. The quantity of water that you add and "
           "remove to <em>keep</em> the VPD changes with the light, because the transpiration "
           "increases (Table 2). The air temperature increases by a small quantity, because "
           "CO&#8322; and heat together increase the light saturation point."),
    p("The second table shows the <strong>water, feed and heat</strong> values of each row: the "
      "quantities that you must supply and remove to keep the PPFD. The cost of a high PPFD is in "
      "this table."),
    table(
      ["Light (PPFD)", "Transpiration (water out of the plant)", "Irrigation (water to the substrate)", "Feed EC", "Heat from the light", "Cooling for sensible heat", "Dehumidification"],
      [
        ["600",  "2.2 L/m&sup2;/d", "3.0 L/m&sup2;/d", "2.0&ndash;2.4", "222 W/m&sup2;", "2.1 kW /10 m&sup2; (0.6 ton)", "2.2 L/m&sup2;/d (4.7 pt)"],
        ["800",  "3.0 L/m&sup2;/d", "4.0 L/m&sup2;/d", "2.4&ndash;2.8", "296 W/m&sup2;", "2.8 kW /10 m&sup2; (0.8 ton)", "3.0 L/m&sup2;/d (6.3 pt)"],
        ["1000", "3.7 L/m&sup2;/d", "4.9 L/m&sup2;/d", "2.8&ndash;3.2", "370 W/m&sup2;", "3.9 kW /10 m&sup2; (1.1 ton)", "3.7 L/m&sup2;/d (7.8 pt)"],
        ["1200", "4.4 L/m&sup2;/d", "5.9 L/m&sup2;/d", "3.2&ndash;3.6", "444 W/m&sup2;", "4.6 kW /10 m&sup2; (1.3 ton)", "4.4 L/m&sup2;/d (9.4 pt)"],
        ["1500", "5.6 L/m&sup2;/d", "7.4 L/m&sup2;/d", "2.4&ndash;3.2 (advanced: a maximum of approximately 3.6)", "556 W/m&sup2;", "5.6 kW /10 m&sup2; (1.6 ton)", "5.6 L/m&sup2;/d (11.7 pt)"],
      ],
      caption="Table 2 &middot; Water, feed and heat removal for each PPFD (for each m&sup2; of canopy, approximately 25% runoff, LED at 2.7 &micro;mol/J)",
      foot="Formulas used: transpiration &asymp; PPFD &times; 0.0037 L/m&sup2;/d. Irrigation = "
           "transpiration &divide; 0.75. Heat from the light = PPFD &divide; 2.7. Dehumidification "
           "load = transpiration (1 L &asymp; 2.1 US pints)" + _c("collado2025-light") +
           ". At the highest PPFD, a high CO&#8322; concentration decreases the transpiration by a "
           "small quantity. For HPS or for LED with 2.0 &micro;mol/J, add approximately 35% to each "
           "value of heat, cooling and airflow."),
    p("Read the two tables together. The problem is then easy to see. From 600 to 1500 &micro;mol, "
      "the light increases 2.5 times. The transpiration, the feed and the heat also increase 2.5 "
      "times.</p><p>You increase the feed EC and the irrigation volume <em>together</em>. Thus the "
      "quantity of nutrient that moves through the plant each day increases approximately "
      "<strong>five times</strong>, and not 2.5 times. Plants in high light do not use only a small "
      "quantity more nutrient. They use much more nutrient and much more water, and they make much "
      "more heat, all at the same time."),
  ]})

SECTIONS.append({"id": "room", "kicker": "04 · An example", "title": "Example of the light steps: a 50 m² flowering room",
  "blocks": [
    p("The tables give values for each m&sup2;. This section uses one room as an example. The room "
      "has a <strong>flowering canopy of 50 m&sup2;</strong>. The room is 10&nbsp;m &times; "
      "5&nbsp;m. It has approximately 35 &times; 650&nbsp;W fixtures and approximately 150 m&sup3; "
      "of air. Use the values in the tables to calculate the list of equipment for the room."),
    table(
      ["Light (PPFD)", "Fixture load", "Cooling for sensible heat", "Airflow of the air handler", "Dehumidification", "Irrigation", "CO&#8322; concentration to keep"],
      [
        ["600",  "11.1 kW", "10.9 kW (3.1 ton)", "approximately 2,100 m&sup3;/h (1,250 CFM)", "111 L/day (235 pt)", "148 L/day", "ambient CO&#8322;"],
        ["800",  "14.8 kW", "14.8 kW (4.2 ton)", "approximately 2,850 m&sup3;/h (1,680 CFM)", "148 L/day (313 pt)", "197 L/day", "approximately 700 ppm"],
        ["1000", "18.5 kW", "18.6 kW (5.3 ton)", "approximately 3,600 m&sup3;/h (2,120 CFM)", "185 L/day (391 pt)", "247 L/day", "approximately 1000 ppm"],
        ["1200", "22.2 kW", "22.2 kW (6.3 ton)", "approximately 4,280 m&sup3;/h (2,520 CFM)", "222 L/day (469 pt)", "296 L/day", "approximately 1200 ppm"],
        ["1500", "27.8 kW", "27.8 kW (7.9 ton)", "approximately 5,370 m&sup3;/h (3,160 CFM)", "278 L/day (587 pt)", "370 L/day", "approximately 1400 ppm"],
      ],
      caption="Table 3 &middot; The capacity that a canopy of 50 m&sup2; must have for each PPFD",
      foot="The cooling for sensible heat is for the fixtures only. In a sealed room, add the heat "
           "from the dehumidifiers and the pumps. The airflow of the air handler is approximately "
           "680 m&sup3;/h for each cooling ton (400 CFM/ton, with 1 cooling ton = 3.5 kW). This "
           "airflow is <em>different from</em> the airflow of the fans in the canopy, which keep "
           "0.5&ndash;1.0 m/s through the leaves. The quantity of CO&#8322; gas for the first fill "
           "of a sealed room of 150 m&sup3; to 1000 ppm is only approximately 90 L. The seal of the "
           "room has the largest effect on the quantity of CO&#8322; that you use each day."),
    p("Examine the values for cooling and dehumidification from 1000 to 1500 &micro;mol. The load "
      "of the fixtures increases by 50%. The dehumidification increases from 185 L/day to 278 L/day "
      "(391 to 587 pints), and the number of dehumidifiers increases from two to three. The cooling "
      "increases from approximately 18.6 kW to 27.8 kW (5.3 to 7.9 tons).</p><p><strong>The photons "
      "are the part with the lowest cost.</strong> The cooling load and the removal of water cause "
      "the large costs and the problems. In almost all rooms, the limiting factor is one of these "
      "two systems, and it is not the lights."),
  ]})

SECTIONS.append({"id": "ec", "kicker": "05 · The root zone", "title": "Control of EC at high PPFD",
  "blocks": [
    p("Examine the feed EC again. You must increase the EC when the light increases. Growers most "
      "frequently do not do this step. As a result, the yield cannot increase, and no clear sign "
      "shows the cause.</p><p>The cause is mass flow. When the light is brighter, the growth is "
      "faster, and the plant absorbs more nutrient each day. The plant gets more nutrient because "
      "of two effects, and <strong>the two effects</strong> increase with the light. First, more "
      "water moves through the plant (the transpiration column of Table 2)" + _c("collado2025-light") +
      ". Second, each milliliter of this water contains more salt (a higher EC).</p><p>If the feed "
      "is not sufficient for a canopy in strong light, the fade starts at the bottom and moves to "
      "the top. The light is available, but the nutrient is not sufficient."),
    table(
      ["Light (PPFD)", "Feed EC (mS/cm)", "Target runoff EC", "Feed for each m&sup2; each day", "Method for the shots", "If the EC is incorrect"],
      [
        ["600",  "2.0&ndash;2.4", "3&ndash;4", "approximately 3.0 L", "Apply a smaller number of shots, with a larger size for each shot. Use a wider dryback.", "Low EC: the new growth is slow and light green."],
        ["800",  "2.4&ndash;2.8", "4&ndash;5", "approximately 4.0 L", "When the canopy becomes larger, increase the frequency of the shots.", "A balanced feed shows at this PPFD."],
        ["1000", "2.8&ndash;3.2", "5&ndash;6", "approximately 4.9 L", "Apply many shots. Use a smaller range.", "Low EC: fade in the bottom part of the canopy."],
        ["1200", "3.2&ndash;3.6", "6&ndash;7", "approximately 5.9 L", "Apply frequent shots. Monitor the runoff EC.", "High EC: tipburn and dry edges on the leaves."],
        ["1500", "2.4&ndash;3.2 (advanced: a maximum of approximately 3.6)", "Advanced, when the runoff EC is much more than the feed EC", "approximately 7.4 L", "Use a high frequency and a large volume. Do a check of the EC each day.", "An EC that is too high or too low causes damage in a short time."],
      ],
      caption="Table 4 &middot; Feed EC and method for the root zone, for each PPFD (controlled substrate, clean source water)",
      foot="The table is for clean source water (EC less than 0.4), a balanced high-ratio nutrient "
           "and an inert substrate. Coir has a buffer for cations. Thus use the lower half of each "
           "range. See <a href='coco-crop-steering.html'>Coco and crop steering</a> and <a "
           "href='nutrient-deficiencies.html'>Nutrient deficiencies</a>. Increase the EC as a lever "
           "only <em>after</em> the irrigation volume is correct. The EC is not an alternative to "
           "the irrigation volume."),
    p("The EC and the light also increase together because of a second cause: the EC is a lever for "
      "<a href='one-steering-law.html'>steering</a>. When the concentration of salt in the solution "
      "around the roots increases, the solution causes a resistance to the flow of water into the "
      "roots. The name of this resistance is <strong>osmotic pressure</strong>.</p><p>A higher EC "
      "in the root zone increases the osmotic pressure and decreases the uptake of water by a small "
      "quantity. As a result, the vegetative growth is slower and the plant changes to generative "
      "growth. This effect helps in the flowering stage. Thus, at high PPFD, you increase the EC "
      "for two tasks at the same time. The first task is to supply feed for the faster growth. The "
      "second task is to keep the generative balance when the irrigation volume is "
      "large.</p><p>When you increase the EC for steering, also increase the irrigation volume. If "
      "the volume is not sufficient, the concentration of the salts increases and causes damage to "
      "the plant."),
  ]})

SECTIONS.append({"id": "find", "kicker": "06 · The method", "title": "Find the limiting factor",
  "blocks": [
    p("Each supply system has a PPFD limit. The limit is the maximum PPFD for which the system is "
      "sufficient. Calculate the limit of each system. <strong>The lowest number is the PPFD limit "
      "of your room.</strong> Light that is more than this limit does not increase the yield. The "
      "table shows how to change each installed system into a PPFD number for each m&sup2; of "
      "canopy."),
    table(
      ["System", "In your room", "PPFD limit of the system"],
      [
        ["<strong>CO&#8322;</strong>", "The setpoint and the measured crop response", "You cannot calculate one PPFD limit from the setpoint only. With ambient CO&#8322;, the yield can increase at a PPFD of more than 800 &micro;mol. CO&#8322; enrichment can increase the efficiency with which the plant uses the added light at high PPFD."],
        ["<strong>Cooling</strong>", "Installed capacity for sensible heat (kW)", "PPFD &le; 2,700 &times; kW &divide; m&sup2; (or 9,500 &times; ton &divide; m&sup2;)"],
        ["<strong>Dehumidification</strong>", "Nameplate capacity (L/day)", "PPFD &le; 270 &times; L/day &divide; m&sup2; (or 128 &times; pints/day &divide; m&sup2;)"],
        ["<strong>Irrigation</strong>", "Maximum L/day that the system can supply", "PPFD &le; 200 &times; L/day &divide; m&sup2;"],
        ["<strong>Feed and EC</strong>", "The highest EC that you can use", "Find the row of Table 4 that agrees with the EC"],
        ["<strong>Airflow</strong>", "Movement of air in the canopy", "A <em>condition</em> that is correct or incorrect, and not a value that you adjust. See below."],
      ],
      caption="Table 5 &middot; The PPFD limit of each system (for each m&sup2; of canopy)",
      foot="All values are for LED at 2.7 &micro;mol/J. For fixtures with less efficiency, decrease "
           "the constant for cooling. Airflow does not give one clear number, because it is a "
           "condition that must be correct first. If you cannot keep 0.3&ndash;1.0 m/s "
           "<em>through</em> all the canopy, the gas exchange decreases and all the other PPFD "
           "limits decrease to approximately 900&ndash;1000 &micro;mol."),
    p("Airflow is different from the other systems, because it is a condition and not a value. A "
      "thin film of air that does not move is on each leaf. The CO&#8322; in the room can go into "
      "the pores of the leaf only through this film, and the movement is diffusion. The name of "
      "this film is the <strong>boundary layer</strong>. When the airflow makes the boundary layer "
      "thin, the CO&#8322; moves easily into the stomata. When the boundary layer is thick, the "
      "plant gets approximately the CO&#8322; concentration of ambient air, also in a room with "
      "1500 ppm.</p><p>A room can have 1500 ppm of CO&#8322;. But the CO&#8322; for the leaf is not "
      "sufficient if the airflow does not remove the <a href='airflow-design.html'>boundary "
      "layer</a>. In a canopy with a high density, air that does not move is a limit for the "
      "CO&#8322;. The sensor in the room does not show this limit. Make sure that the airflow is "
      "correct <em>before</em> you read the other PPFD limits."),
    p("Calculate the six numbers and find the lowest number. This number is the PPFD limit of the "
      "room. The diagram shows an example."),
    figure(_fig_ceiling(), 1,
      "Four systems have four different limits. The cooling system is sufficient for 1140 "
      "&micro;mol, and the CO&#8322; is sufficient for 1500 &micro;mol. But the dehumidifier is "
      "sufficient for a maximum of only 1050 &micro;mol (shown in amber). This value is the PPFD "
      "limit of the room. If you operate the lights at 1300 &micro;mol, the added 250 &micro;mol "
      "makes only humidity that the dehumidifier cannot remove. Set the PPFD to 1050 &micro;mol, or "
      "add more dehumidifier capacity."),
  ]})

SECTIONS.append({"id": "cases", "kicker": "07 · Examples", "title": "Examples of limiting factors",
  "blocks": [
    p("The section gives four examples of the method, for four frequent types of room. In each "
      "room, one supply is not sufficient and all the other supplies are sufficient. This one "
      "supply controls the yield. Do not increase the light to correct the problem."),
    callout("note", "Example A · The dehumidifier is the limiting factor " + _tag("w", "most frequent"),
      p("<strong>The room:</strong> 50 m&sup2;, 21 kW (6 ton) of cooling, CO&#8322; to 1500 ppm, "
        "good fans and two dehumidifiers of 97 L/day each (410 pints/day, 194 L/day in total). "
        "<strong>The numbers:</strong> the PPFD limit of the cooling is 2,700&times;21.1&divide;50 "
        "&asymp; <strong>1140</strong>. The PPFD limit of the dehumidifiers is "
        "270&times;194&divide;50 &asymp; <strong>1050</strong>. The PPFD limit of the CO&#8322; is "
        "<strong>1500</strong>.</p><p><strong>The limiting factor:</strong> the dehumidification, "
        "at approximately 1050 &micro;mol. <strong>The correction:</strong> operate the lights at "
        "1050 &micro;mol, <em>or</em> add a third dehumidifier. The PPFD limit then becomes 1140 "
        "&micro;mol, the limit of the cooling. After that, the cooling is the next limiting factor.")),
    callout("note", "Example B · Ambient air as the PPFD limit " + _tag("g", "low cost to correct"),
      p("<strong>The room:</strong> large cooling and dehumidification capacity, but <em>no</em> "
        "CO&#8322; enrichment. The room has ambient CO&#8322; at 420 ppm. <strong>The "
        "data:</strong> the efficiency of the leaf decreases when the PPFD increases" +
        _c("chandra2008-photo") + ". But Rodriguez-Morrison and the other authors measured a linear "
        "canopy yield to 1,800 &micro;mol at ambient CO&#8322;, in one cultivar and one room" +
        _c("rm2021-light") + ".</p><p><strong>The limit that you use:</strong> there is no PPFD "
        "limit of 800 &micro;mol for all rooms. Monitor the canopy temperature, the bleaching, the "
        "DLI and the yield for each kWh. Decrease the light when the crop has damage. Also decrease "
        "the light when the added yield is not sufficient for the cost of power and climate "
        "control. Before you add CO&#8322;, make sure that the room has sufficient capacity for the "
        "added heat, water and safety load.")),
    callout("note", "Example C · The canopy with air that does not move " + _tag("w", "not easy to see"),
      p("<strong>The room:</strong> CO&#8322; to 1200 ppm, and strong cooling and dehumidification. "
        "But the canopy has a high density, and the laminar air in the bottom half does not move. "
        "<strong>The numbers:</strong> there is no clear number. The airflow does not remove the "
        "boundary layer, and thus the CO&#8322; cannot go into the stomata in the canopy. The PPFD "
        "limit decreases to approximately <strong>900&ndash;1000</strong>, but the room has 1200 "
        "ppm.</p><p><strong>The limiting factor:</strong> the condition of the airflow. <strong>The "
        "sign:</strong> the outer buds are in good condition, but the inner part of the canopy is "
        "moist and has larf. <strong>The correction:</strong> <a "
        "href='defoliation-training.html'>defoliate</a> the canopy and add airflow below the canopy "
        "<em>before</em> you change the lights or the CO&#8322;.")),
    callout("note", "Example D · The root zone is not sufficient " + _tag("w", "caused by the grower"),
      p("<strong>The room:</strong> the climate and the gas are sufficient for 1300 &micro;mol. But "
        "the irrigation is only a small number of short shots, and the feed EC stays at 2.4. "
        "<strong>The numbers:</strong> the canopy must have a minimum of 4.5&nbsp;L/m&sup2;/day and "
        "an EC of 3.4. It gets approximately 3&nbsp;L and an EC of 2.4. The PPFD limit for the "
        "water is approximately <strong>900</strong> (200&times;(the L that the system can "
        "supply)&divide;m&sup2;). The low EC gives approximately the same PPFD "
        "limit.</p><p><strong>The limiting factor:</strong> the irrigation volume and the EC. "
        "<strong>The sign:</strong> wilt in the middle of the day, and light green leaves with fade "
        "in the bottom canopy. <strong>The correction:</strong> make the shot volume and the shot "
        "frequency correct first. <em>Then</em> increase the EC with Table 4. Do not do these steps "
        "in the other sequence.")),
  ]})

SECTIONS.append({"id": "dial", "kicker": "08 · The decision", "title": "Set the light intensity to the limiting factor",
  "blocks": [
    p("When you know your lowest PPFD limit, you have two correct alternatives."),
    p("<strong>Alternative one: set the light to the limit.</strong> If your PPFD limit is 1050 "
      "&micro;mol, operate the lights at 1050 &micro;mol. The photons that make the PPFD more than "
      "this limit do not change into yield. They change into heat, humidity and stress.</p><p>When "
      "you decrease the light to the limit, the growth does not decrease. You also use less power, "
      "you have more cooling headroom, and the room is more stable. For fixtures that you can "
      "adjust to a lower intensity, the change has no cost, and the effect occurs immediately."),
    p("<strong>Alternative two: increase the PPFD limit, then examine the room again.</strong> Add "
      "equipment only to the system that is the <em>limiting factor</em>. If you add CO&#8322; to "
      "the room in Example B, the effect is very large. If you add CO&#8322; to the room in Example "
      "A, there is no effect, because the dehumidifier and not the CO&#8322; is the limiting "
      "factor.</p><p>Persons frequently do not know that <strong>when you increase one PPFD limit, "
      "a different system becomes the limiting factor.</strong> If you correct the dehumidifier in "
      "Example A, the cooling gives a limit of 1140 &micro;mol. If you increase the limits in the "
      "incorrect sequence, you add equipment that does not change the result."),
    callout("warn", "Do not operate the lights at more than the PPFD limit",
      p("Do not operate the lights at a PPFD that is more than the PPFD limit. The added light is "
        "not neutral. It causes bleaching and foxtails on the top buds, and it increases the leaf "
        "temperature and the VPD. When the dehumidifier is the limiting factor, the humidity can "
        "increase to a value at which <a href='mould-risk.html'>bud rot</a> occurs. The added "
        "electricity has a cost, <em>and</em> the quality decreases. When you decrease the light to "
        "the limit, there is no cost.")),
    p("There is also a cost limit, and it is lower than the limit of the plants. The yield "
      "continues to increase to 1500&ndash;1800 &micro;mol" + _c("rm2021-light") +
      ". But the cooling load and the removal of water for the highest PPFD increase more quickly "
      "than the yield. For the last 300 &micro;mol, it can be necessary to add a third dehumidifier "
      "and a larger cooling system (AC). The yield then increases by only one to nine "
      "percent.</p><p>Find your <em>cost</em> limit. At the cost limit, the added yield of the next "
      "100 &micro;mol is not sufficient for the cost of its climate equipment. This cost limit is "
      "frequently one step less than the PPFD that the plants can use."),
  ]})

SECTIONS.append({"id": "trouble", "kicker": "09 · When there is a problem", "title": "Troubleshooting",
  "blocks": [
    p("Each row of the table shows one limiting factor. The symptom shows which limiting factor your room has."),
    table(
      ["Symptom", "The limiting factor", "Correction"],
      [
        ["Bleaching and foxtails on the top buds at high PPFD", "The PPFD, the temperature or the DLI is more than the tolerance of the cultivar or the canopy.", "Measure the canopy temperature and the distribution of the light. Decrease the PPFD. Do a test of the CO&#8322; as a different variable."],
        ["The RH does not decrease. The VPD becomes very low in the middle of the day.", "The transpiration is more than the capacity of the dehumidification.", "Add dehumidifier capacity or decrease the light. Dehumidification is usually the limiting factor."],
        ["High PPFD and a yield that does not increase", "The CO&#8322;, the water or the feed did not increase with the light.", "Find the lowest PPFD limit. Increase it, or set the PPFD to the limit."],
        ["Wilt in the middle of the day at peak light", "The irrigation volume is less than the transpiration.", "Apply larger shots or more shots. Correct the volume before you change the EC."],
        ["Light green leaves and fade in the bottom canopy in the last part of the flowering stage", "The feed EC is too low for the PPFD.", "Increase the EC by one step in Table 4. Do a check of the runoff EC."],
        ["Tipburn and dry edges on the leaves", "The feed EC is too high for the PPFD (more than the value in the row).", "Decrease the EC by one step. Or increase the PPFD and the irrigation volume until they agree with the EC."],
        ["The outer buds are in good condition. The inner canopy has larf and is moist.", "The condition of the airflow is not correct. The airflow does not remove the boundary layer in the canopy.", "Defoliate the canopy and add airflow below the canopy. The CO&#8322; cannot have an effect in air that does not move."],
      ],
      cls="compact"),
  ]})

SECTIONS.append({"id": "expect", "kicker": "10 · The data and their limits", "title": "Expected results and limitations",
  "blocks": [
    p("The yield of cannabis has an almost linear relation with the light, to approximately "
      "1500&ndash;1800 &micro;mol" + _c("rm2021-light") + ". But this result has a condition, and "
      "the tests give the condition. The result is correct <em>only</em> when you increase the "
      "CO&#8322;, the temperature, the water and the feed to agree with the light. If these "
      "supplies are not sufficient, the same lights cause bleaching on the top buds and a heat "
      "problem. The linear relation is correct only when all the supplies increase with the light."),
    p("Your first task is the limiting factor of your room, and it is not the lights. In "
      "approximate sequence, the most frequent limiting factors are the dehumidification, the "
      "cooling, the CO&#8322; and the supply to the root zone. The correction of the current "
      "limiting factor usually gives the yield with the lowest cost. One more kilowatt of light "
      "does not give the yield with the lowest cost.</p><p>Measure the values that show the "
      "limiting factor. These values are the leaf temperature, the runoff EC, the RH and the air "
      "speed in the canopy, and the CO&#8322; below the canopy. A sensor at the edge of the room "
      "does not show the air in the canopy that does not move and has a high humidity."),
    callout("key", "Keep these facts",
      ol([
        "When you increase the light, the room must supply more CO&#8322;, water, feed and airflow, and must remove more heat. <strong>Calculate the size of each supply system for the light</strong> (Tables 1 and 2).",
        "Calculate the <strong>PPFD limit</strong> of each installed system. The <strong>lowest limit</strong> is the limit of the room (Table 5).",
        "<strong>Set the light to that limit.</strong> Light that is more than the limit uses power but does not increase the yield, and it decreases the quality.",
        "To use a higher PPFD, <strong>increase the limit of the system that is the limiting factor. Then examine the room again.</strong> The limiting factor changes.",
      ])),
    p("This paper gives information on one lever of the room. Read it with <a "
      "href='grow-room-systems.html'>Grow-room systems</a>, <a href='co2-enrichment.html'>CO&#8322; "
      "enrichment</a> and <a href='airflow-design.html'>Airflow design</a>."),
  ]})
