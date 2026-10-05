# -*- coding: utf-8 -*-
"""Paper: yield denominators and unit economics — g/m², g/W, g/kWh and the cost of a gram."""
import json, os
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        grid, card, chip, kv, steps)
import figs_lib as L

_FIGS = json.load(open(os.path.join(os.path.dirname(__file__), "figs_unit_economics.json"), encoding="utf-8"))

SLUG = "unit-economics"
TITLE = "Yield for each watt and the cost of a gram"
EYEBROW = "Facility · Economics"
SUB = ("This paper shows three yield denominators: g/m² of canopy, g/W of light, and g/kWh all-in. "
       "It shows the function of each denominator and the information that it does not show. The "
       "paper calculates the cost for each gram of an example room of 100 m² (1,076 ft²), and you "
       "can examine each step. The paper gives a reference for each number, or shows how to "
       "calculate it.")
META = [("gauge", "Economics"), ("image", "11 diagrams"),
        ("quote", "14 sources"), ("clock", "~22 min to read")]
RELATED = ["energy-sustainability", "scaling-high-light", "lighting-fundamentals"]
REF_IDS = ["rii-powerscore", "nfd-energy-compare", "toonen2006-yield", "potter2012-gpw",
           "backer2019-yieldgap", "llewellyn2022-light", "westmoreland2021-blue", "rm2021-light",
           "kusuma2020-efficacy", "mills2012-carbon", "summers2021-ghg", "valdes2020-testing",
           "triminator-industrial", "cannabisbenchmarks-q1-2024"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

_N = [0]
def fig(key_or_svg, cap):
    _N[0] += 1
    svg = _FIGS[key_or_svg] if isinstance(key_or_svg, str) and key_or_svg in _FIGS else key_or_svg
    return figure(svg, _N[0], cap)

SECTIONS = []

# ---------------------------------------------------------------- 01 start here
SECTIONS.append({"id": "start-here", "kicker": "01 · Read this first", "title": "Purpose and scope",
  "blocks": [
    callout("warn", "Information, not financial advice",
      p("This paper shows the <strong>arithmetic</strong> of the economics of cultivation. It shows "
        "how to calculate the cost for each gram from given values. It also shows the benchmarks "
        "from the literature and their limits. This paper is not investment advice, business "
        "advice, or tax advice. The <strong>example room</strong> in this paper is a model. No "
        "facility has this room.</p><p>Calculate each table again with the numbers of your room. "
        "The prices, the wages, the price of electricity, and the regulation are very different in "
        "each market. Before you make a decision for your business, speak to an accountant.")),
    lead("Most persons speak about plants when they speak about grow rooms. But the result of one "
         "division shows if the room can continue to operate. The division is: all the dollars that "
         "you pay in one year, divided by all the grams that you sell in that year. If the result "
         "is less than the price that you get for one gram, you have a business. If it is not, you "
         "have a license but no business. Your room has a loss, and no information about terpenes "
         "changes the result."),
    p("The problem is that the usual metrics, g/m² and g/W, are for other tasks. They are metrics "
      "for agronomy, and growers use them to compare results with other growers. Each one ignores a "
      "part of the cost. This paper shows the three usual denominators and the function of each "
      "denominator. It also shows the benchmarks from the literature with their limits, because the "
      "limits are large.</p><p>Then the paper calculates the full list of costs for an example room "
      "of 100 m² (1,076 ft²) and shows each step of the arithmetic. After this, the paper shows "
      "labor (almost all growers think that this cost is smaller than it is), cycles each year (a "
      "number that multiplies the production and that is not easy to see), grades of quality, a "
      "tornado chart of the sensitivity, and the break-even."),
    p("If you can divide two numbers, you can do all the steps in this paper. Unit economics is the "
      "selection of the <em>correct</em> two numbers to divide."),
  ]})

# ---------------------------------------------------------------- 02 vocabulary
SECTIONS.append({"id": "vocabulary", "kicker": "02 · The terms", "title": "Definitions",
  "blocks": [
    p("Nine terms are necessary for the remaining sections. When two growers calculate the "
      "economics of a room and get different results, they frequently use the same term for "
      "different fractions."),
    defterm("Denominator", "The denominator is the bottom number of a fraction. It is the number "
            "that you divide <em>by</em>. You must give the denominator with each yield value. "
            "Examples: yield <em>for each</em> m², for each watt, for each kWh, for each year, or "
            "for each dollar. When you change the denominator, the same harvest gives a different "
            "result."),
    defterm("Canopy area and floor area", "Canopy area is the area in m² that has flowering plants. "
            "Floor area (or total area) includes the aisles, the vegetative room, the drying room, "
            "the entrance, and the room for equipment. A facility with 100 m² of canopy can have "
            "250 m² of floor. You pay rent for the floor area, but the value in g/m² is for the "
            "canopy area. If you use the incorrect area for a value, your model shows a result that "
            "is 2 to 3 times better than the correct result."),
    defterm("Installed watts", "Installed watts are the nameplate power of the fixtures above the "
            "canopy. They are the W in g/W. The value does not show how many hours the fixtures "
            "operate, or how much energy the HVAC uses because of them."),
    defterm("kWh", "A kilowatt-hour is the energy that a device of 1 kW uses in 1 hour. The "
            "electricity bill gives the energy in this unit. Thus g/kWh is the energy metric that "
            "agrees with the bill."),
    defterm("OPEX and CAPEX", "OPEX is the cost of operation that you pay each month: electricity, "
            "wages, media, and rent. CAPEX is the cost of items that you get one time and use for "
            "many years: fixtures, HVAC, benches, and controls. CAPEX also becomes part of the cost "
            "for each gram, as depreciation."),
    defterm("Depreciation", "Depreciation is the cost of one purchase divided by the number of "
            "years in which you use the item. A $300,000 fit-out that you use for 7 years has a "
            "cost of approximately $43,000 each year. You do not get an invoice for this cost. If "
            "you ignore depreciation, you can show a profit, but you cannot replace the equipment."),
    defterm("Cycle length", "The cycle length is the number of days from the start of "
            "flowering of one crop to the start of flowering of the <em>next</em> crop. It is the "
            "days of flowering plus the turn time. The turn time is the days to harvest, to clean, "
            "and to prepare the room. The cycle length, and not the days of flowering, sets the "
            "cycles each year."),
    defterm("Blended price", "The blended price is the average price that you get for all your "
            "harvest: grade A flower, grade B flower, small buds, and trim. The average uses each "
            "price in proportion to the quantity that you sell at that price. An estimate "
            "frequently uses the price of grade A, but your revenue is at the blended price."),
    defterm("Break-even", "Break-even is the condition when the revenue is equal to the cost. In "
            "this condition, the profit is zero. You can calculate the break-even as a yield, as a "
            "price, or as a number of cycles. All of this paper helps you to know on which side of "
            "the break-even your room is."),
  ]})

# ---------------------------------------------------------------- 03 core answer
SECTIONS.append({"id": "core-answer", "kicker": "03 · The primary result", "title": "Summary of the cost for each gram",
  "blocks": [
    callout("key", "Only the cost for each gram shows if the business can pay the rent",
      ul(["<strong>The cost for each gram = all the dollars for the year ÷ all the grams that you "
          "sell in that year.</strong> Do not use the cost for each cycle or the cost for each "
          "room. Do not use a cost that you get only when the room operates correctly. The bank "
          "statement gives the dollars. The scale gives the grams.",
          "This one fraction has three quantities that you can change: <strong>grams for each "
          "cycle</strong> (agronomy), <strong>cycles each year</strong> (operation of the "
          "facility), and <strong>dollars each year</strong> (all the costs of the year). Each "
          "change that makes the business better is a change to one of these three quantities.",
          "g/m², g/W, and g/kWh are <strong>metrics for one part</strong> of the business. They "
          "help you to find problems. If you use them as the primary metric of the business, they "
          "cause errors, because each one ignores a cost that the other metrics include.",
          "The range of the benchmarks from the literature is approximately <strong>6 times in g/W "
          "and much larger in g/m²</strong>, because the conditions are different. Give a range "
          "with its conditions, or do not give it.",
          "Labor and turn time change the result more than the equipment that a supplier sells to "
          "you. Calculate the sensitivity before you pay for equipment."])),
  ]})

# ---------------------------------------------------------------- 04 three denominators
SECTIONS.append({"id": "three-denominators", "kicker": "04 · The three denominators", "title": "g/m², g/W, and g/kWh: how to select the correct metric",
  "blocks": [
    p("The three metrics divide the same harvest by three different quantities, and each metric "
      "gives you different information. The error is not that you use the metrics. The error is "
      "that you use one metric as the primary metric of the business and ignore the information "
      "that the metric does not show."),
    fig("denoms", "The same room and the same harvest give three ‘efficiency’ numbers. Each number "
        "uses one input and ignores the other costs. No one of the three numbers is the total cost."),
    p("<strong>g/m² of canopy</strong> is the number for agronomy. It compares crops, cultivars, "
      "and steering decisions for the same floor area, and most investigations give this number. It "
      "does not include time. Cycles of nine weeks and of twelve weeks can give the same g/m², but "
      "the shorter cycle gives 30% more each year. It also does not include power, labor, or the "
      "quantities of the grades."),
    p("<strong>g/W of installed light</strong> is a metric from the time when growers used it to "
      "compare lamps. Section 06 examines this metric in full. It shows the quantity of crop for "
      "each unit of lighting equipment. But the denominator is the nameplate watts. The metric "
      "ignores the hours in which the lamps operate and all the energy that the HVAC uses. Most "
      "important, it ignores the fixture generation that gives the watts."),
    p("<strong>g/kWh all-in</strong> (or its reciprocal, kWh for each kg) divides by all the "
      "kilowatt-hours that go through the meter: lights, HVAC, dehumidification, pumps, and all "
      "other loads. It is the one denominator that agrees with the electricity bill that you get "
      "from the supplier. It is also the primary metric for benchmarks of facilities. The "
      "PowerScore of the Resource Innovation Institute examines a facility with only two numbers. "
      "The numbers are kWh for each unit of flowering canopy and grams for each kWh. The PowerScore "
      "includes more than 350 growers" + _c("rii-powerscore") + ".</p><p>The difference is very "
      "large: indoor production uses approximately 18 times the energy for each gram that outdoor "
      "production uses" + _c("nfd-energy-compare") + ". Thus this metric is very important for an "
      "indoor room. It is less important for a greenhouse."),
    table(["Metric", "Good for", "Does not include", "Summary"], [
      ["g/m² for each cycle", "To compare crops, cultivars, and steering for the same floor area", "Time, power, labor, grade", "A tool for agronomy. It is not a metric for the business."],
      ["g/W installed", "To select the size of fixtures, and to compare results with other growers", "Hours of operation, HVAC, fixture generation, time", "Less correct each year. Refer to Section 06."],
      ["g/kWh all-in", "The grams for each unit of energy. It agrees with the electricity bill.", "Labor, rent, CAPEX, testing", "The best metric for one quantity. It is not the total cost."],
      ["$ for each gram", "To make the decision about the business", "None, if you include all the costs", "The primary metric of the business"],
    ], caption="Four methods to divide a harvest. The first three help you to find problems. Only the fourth shows if the business can pay the rent."),
    callout("tip", "The error with canopy area",
      p("Each time that a person gives a value for each m², make sure that you know the "
        "<em>area</em> that the value is for. Do the same when you give the value. The area can be "
        "the canopy, the floor of the room, or all the building. A value of 450 g/m² for the canopy "
        "becomes approximately 180 g/m² for the building. The area of the building includes the "
        "aisles, the vegetative room, and the drying room, and the usual ratio of canopy to floor "
        "is 40%. The two values are correct, but only the value for the building agrees with the "
        "area for which you pay rent.")),
  ]})

# ---------------------------------------------------------------- 05 benchmarks
SECTIONS.append({"id": "benchmarks", "kicker": "05 · Benchmarks", "title": "Yield benchmarks from the literature and their limits",
  "blocks": [
    lead("The values for the yield of cannabis in the literature have different conditions and "
         "different denominators. Some values are projections and not measurements. Before you "
         "compare your room with a benchmark, examine the sources and the size of the differences."),
    fig("spread", "Ranges from the literature as the sources give them. Top: g/m² for each cycle" +
        _c("toonen2006-yield") + _c("llewellyn2022-light") + _c("westmoreland2021-blue") +
        _c("backer2019-yieldgap") + ". Bottom: g for each installed W" + _c("toonen2006-yield") +
        _c("potter2012-gpw") + _c("backer2019-yieldgap") + ". The conditions are very different in "
        "each row. Thus you cannot compare the rows."),
    p("<strong>The baseline from police data.</strong> The best large-sample value for g/m² in the "
      "literature is also the first value in time. Police in the Netherlands weighed the plants "
      "from illegal grow rooms that they found. The model for the median room has 15 plants/m² at "
      "510 W/m² of HPS, and it gives <strong>33.7 g for each plant and 505 g/m²</strong>" +
      _c("toonen2006-yield") + ".</p><p>The division of 505 g/m² by 510 W/m² is 0.99 g/W. It is "
      "very possible that this one investigation is the source of the value ‘one gram for each "
      "watt’ that growers frequently give. The investigation is twenty years before this paper, and "
      "it gives a median value for HPS rooms."),
    p("<strong>The tests with careful conditions.</strong> In the tests of Potter and Duncombe, the "
      "HPS lamps operated at 270, 400, and 600 W/m². The tests measured <strong>0.9–1.6 "
      "g/W</strong>, and the best result in g/W was at the <em>lowest</em> power" + _c("potter2012-gpw") +
      ". More light gave more grams, but the value in g/W was lower. The tests measured how the "
      "grams for each unit of power become smaller when the power increases.</p><p>Tests with new "
      "LED fixtures show the same result from the other side. The yield of dry flower continued to "
      "increase almost in proportion to the light intensity, to a maximum of approximately 1,800 "
      "µmol·m⁻²·s⁻¹. There was no plateau" + _c("rm2021-light") + ". A second test at 600–1,000 "
      "µmol found that each 100 µmol more gives approximately 4.6 g for each plant (approximately "
      "51 g/m² at approximately 10 plants/m²). The yields in this range are approximately "
      "<strong>276–447 g/m²</strong>" + _c("llewellyn2022-light") + ". The group of Bugbee did "
      "three tests with hemp at high light for cannabinoids and measured <strong>500–750 "
      "g/m²</strong> in the three tests" + _c("westmoreland2021-blue") + "."),
    p("<strong>The meta-analysis, and the limits of the data.</strong> Backer and the other authors "
      "put together the data from the literature. They found efficiencies in the reports of "
      "<strong>0.31–1.97 g/W</strong>, which is a range of 6 times. They also found projections of "
      "yield for large areas from 3.4 to <strong>3,590 g/m²</strong>, which is a range of "
      "approximately a thousand times. The cause is that the projections use numbers from small "
      "test areas for large areas that did not have a crop" + _c("backer2019-yieldgap") +
      ".</p><p>They also found that the yield for each watt <em>decreased</em> when the installed "
      "W/m² increased. They found that the yield for each m² increased when the time of flowering "
      "was longer. In the two results, the cause is the denominator and not the plant."),
    table(["Source", "Conditions", "Value", "How to read the value"], [
      ["Toonen 2006" + _c("toonen2006-yield"), "Median illegal room in NL, HPS, 15 plants/m²", "505 g/m² · approximately 0.99 g/W", "The source of the value ‘one gram for each watt’"],
      ["Potter and Duncombe 2012" + _c("potter2012-gpw"), "HPS at 270/400/600 W/m²", "0.9–1.6 g/W. The best value is at the lowest power.", "The grams for each watt become smaller when the power increases"],
      ["Rodriguez-Morrison 2021" + _c("rm2021-light"), "Indoor, to a maximum of approximately 1,800 µmol", "The yield is almost in proportion to the light. There is no plateau.", "More light gives more grams, with a cost in power"],
      ["Llewellyn 2022" + _c("llewellyn2022-light"), "LED, 600–1,000 µmol, approximately 10 plants/m²", "Approximately 276–447 g/m². 51 g/m² more for each 100 µmol", "A range that agrees with the data"],
      ["Westmoreland 2021" + _c("westmoreland2021-blue"), "High light, three tests", "500–750 g/m²", "The high end of the range, in tests with careful procedures"],
      ["Backer 2019 meta-analysis" + _c("backer2019-yieldgap"), "Data from the literature put together", "0.31–1.97 g/W. Projections to 3,590 g/m².", "Do not give a benchmark as one number"],
      ["Values that growers give", "No reference. Many persons give the value.", "‘300–600 g/m² for each cycle’", "A possible range with no source. Do not use it as data."],
    ], caption="The benchmark table: each row is correct for its conditions, and you cannot compare two rows if you ignore the limits."),
    callout("evidence", "The cause of the large differences",
      p("These conditions are different in the investigations: the plant density, the cultivar, the "
        "light intensity, the pot size, and the length of flowering. Most important, the item that "
        "the investigations use for <em>yield</em> is different. The yield can be the weight of all "
        "the flower, the weight of grade A flower after trimming, or a projection on paper. These "
        "differences do not make the investigations incorrect. They make a benchmark with one "
        "number incorrect. When a person gives a benchmark, make sure that you know <em>the "
        "conditions and the method of measurement</em>.")),
  ]})

# ---------------------------------------------------------------- 06 g/W autopsy
SECTIONS.append({"id": "gram-per-watt", "kicker": "06 · g/W: a metric for one fixture generation", "title": "Grams for each watt: a lighting metric from the time of HPS",
  "blocks": [
    lead("The value ‘one gram for each watt’ was a good approximate value when all the rooms used "
         "the same lamp. With LED, the metric shows <em>when you got your fixtures</em>, because a "
         "watt in the denominator gives more photons than it gave with HPS."),
    p("The <strong>efficacy</strong> of a fixture is the quantity of photons that the fixture gives "
      "for each joule of energy. The unit is µmol of photons for each joule. Double-ended HPS, the "
      "lamp type for the value ‘one gram for each watt’, gives approximately 1.72 µmol/J.</p><p>In "
      "2020, the best LED fixtures that growers measured gave approximately 3.0 µmol/J (blue/red) "
      "and 2.78 (white/red). The practical limits are approximately 3.4–4.1" + _c("kusuma2020-efficacy") +
      ". In 2014, the best LEDs gave 1.7, which is equal to HPS. In one fixture generation, the "
      "photons for each watt increased to approximately <strong>two times</strong> the previous "
      "value."),
    fig(L.bars("Fixture efficacy: photons for each joule",
        [("HPS (DE)", 1.72), ("Best LED 2014", 1.7), ("Best LED 2020", 3.0), ("White+red limit", 3.4)],
        unit="", note="µmol of photons for each joule, in measured fixtures. Blue+red practical limit ≈4.1 µmol/J.",
        maxv=4.0),
        "Measured fixture efficacy" + _c("kusuma2020-efficacy") + ". Each watt gives almost two "
        "times the photons that it gave with HPS. Thus each g/W value has a date, but the value "
        "does not show the date."),
    p("Examine the effect on g/W when there is <em>no</em> change in agronomy. Use the same example "
      "crop, 450 g/m² at 900 µmol·m⁻²·s⁻¹. HPS at 1.72 µmol/J supplies 900 µmol with 900 ÷ 1.72 = "
      "approximately 523 W/m². An LED at 2.8 µmol/J supplies the same photons with 900 ÷ 2.8 = "
      "approximately 321 W/m².</p><p>The photons, the plants, and the grams are the same. The HPS "
      "grower calculates 450 ÷ 523 = <strong>0.86 g/W</strong>. The LED grower calculates 450 ÷ 321 "
      "= <strong>1.40 g/W</strong>. The agronomy of the two growers is the same."),
    fig(L.hbars("Same crop, same photons, only the fixture changed",
        [("HPS lamp", 0.86), ("LED lamp", 1.4)], unit=" g/W",
        note="Example crop of 450 g/m² at 900 µmol. HPS at 1.72 µmol/J uses 523 W/m². An LED at 2.8 µmol/J uses 321."),
        "The ‘improvement’ in g/W is the effect of the fixture and not of the grower. Compare g/W "
        "only in one fixture generation."),
    p("The change in efficacy also changes the decision about the purchase of fixtures. In the "
      "lighting tests of Bugbee, the white+red LED gave 4.6% <em>less</em> yield for each m² than "
      "HPS. It gave <strong>27% more yield for each dollar of electricity</strong>" +
      _c("westmoreland2021-blue") + ".</p><p>If you use g/m², the LED is worse. If you use the "
      "yield for each dollar of electricity, which is a cost metric, the LED is better. The data "
      "are the same, but the denominator is different and the decision is opposite. This one test "
      "shows the primary result of this paper."),
    callout("key", "How to use g/W at this time",
      ul(["Use it to <strong>do a check of the lighting of a room</strong>. Compare the room with "
          "rooms that have the same fixture generation. If a person tells you that an LED room has "
          "0.6 g/W or 2.5 g/W, examine the data.",
          "Do not compare g/W in different fixture generations. Do not let a supplier do it for you.",
          "For decisions, calculate <strong>g/kWh all-in</strong> (add the hours of operation and "
          "the HVAC), and then <strong>$ for each gram</strong>. Invoices show kilowatt-hours and "
          "do not show watts."])),
  ]})

# ---------------------------------------------------------------- 07 cost stack
SECTIONS.append({"id": "cost-stack", "kicker": "07 · The list of costs", "title": "Cost items for each gram",
  "blocks": [
    p("The cost for each gram uses a short list of items. The method is easy, but you must include "
      "all the items. Eight items are sufficient for a small indoor facility:"),
    ul(["<strong>Labor</strong>: the wages plus the other costs that you pay with the wages (paid "
        "leave, insurance, and tax). The item includes all personnel who touch the crop, <em>also "
        "you, at a market rate</em>.",
        "<strong>Energy</strong>: lights, HVAC, dehumidification, pumps, and controls. Include all "
        "of the energy. Use the value on the electricity bill and not the value on the fixture "
        "nameplate. Two numbers show how large this item is for indoor production. An estimate for "
        "the US shows that indoor production used 1% of all the electricity of the US approximately "
        "ten years before this paper" + _c("mills2012-carbon") + ". The emissions that models give "
        "are 2,283–5,184 kg CO₂e for each kg of flower, and they change with the climate" +
        _c("summers2021-ghg") + ".",
        "<strong>Media + nutrients</strong>: substrate, salts, CO₂, and consumables for IPM.",
        "<strong>Rent</strong>: for the total floor area and not for the canopy area.",
        "<strong>Depreciation</strong>: the fit-out and the equipment, divided by the number of years in which you use them.",
        "<strong>Testing + compliance</strong>: the panels of laboratory tests for each batch, plus "
        "the licenses, the QA time, and the records. Data from California show a cost of "
        "approximately $136 for each pound (approximately $0.30/g) for the mandatory testing only. "
        "This cost includes the sampling and the failure rates" + _c("valdes2020-testing") +
        ". This item is large and you cannot ignore it.",
        "<strong>Packaging + consumables</strong>: bags, totes, labels, and gloves.",
        "<strong>Other overhead</strong>: insurance, security, administration, repairs, and software."]),
    fig(L.flow("How to calculate the cost for each gram",
        [("Count the dollars", "Bank statements for twelve months, with all eight cost items"),
         ("Count the grams", "Grams that you sell in the same twelve months, not grams that you harvest"),
         ("Divide", "Dollars divided by grams is the result. Do not change the result"),
         ("Compare items", "Put the largest item first. This sequence is your list of tasks"),
         ("Change item one", "10% less in item one is better than 50% less in item eight")],
        note="Use numbers for one year. One cycle does not show turn time or seasonality."),
        "The full method. All the sections after this section are examples of these five steps."),
    callout("note", "Use one year, not one cycle",
      p("The cost of one cycle does not include the days when the room has no revenue. Examples are "
        "the turn time, a failure of a batch, and the month when the dehumidifier stopped. The "
        "dollars of twelve months divided by the grams of twelve months include these days "
        "automatically. It is also the only method that your accountant and your bank accept, and "
        "it is necessary for the renewal of your license.")),
  ]})

# ---------------------------------------------------------------- 08 worked example
SECTIONS.append({"id": "worked-example", "kicker": "08 · The example room", "title": "The example room of 100 m²: all the steps",
  "blocks": [
    callout("warn", "Example facility: given values, not data from facilities",
      p("The example in this section is a <strong>model room with given values</strong>. We "
        "selected the values because they are possible and because they divide easily. They are not "
        "the numbers of a facility in operation, and they are not a target. The primary information "
        "is the <em>method</em>. Use the values of your room. The same arithmetic gives your result.")),
    kv([("Flowering canopy", "100 m² (1,076 ft²). Total floor area approximately 250 m² (2,691 ft²). Canopy ratio 40%."),
        ("Lighting", "LED, 2.6 µmol/J, 350 W for each m² of canopy, 35 kW installed"),
        ("Photoperiod and flowering stage", "12 h · 56 days in the flowering stage"),
        ("Turn time", "7 days (harvest, clean, prepare the room, and start the next flowering)"),
        ("Yield value", "450 g/m² for each cycle, in the middle of the ranges. Refer to Section 05."),
        ("Electricity price", "$0.20 for each kWh (the dollars in this paper are not the dollars of a specified market)"),
        ("Energy for the other loads", "All-in electricity = 2.2 × lighting kWh (HVAC, dehumidification, fans, vegetative room, drying room)"),
        ("Personnel", "4.0 FTE (full-time equivalent). $50,000 for each FTE, with all the other costs for personnel"),
        ("Fit-out CAPEX", "$300,000, with equal depreciation each year for 7 years")]),
    steps([
      ("Calculate the installed power",
       "100 m² × 350 W/m² = <strong>35,000 W = 35 kW</strong> installed. Do a check of the light "
       "intensity: 350 W/m² × 2.6 µmol/J = <strong>910 µmol·m⁻²·s⁻¹</strong>. This light intensity "
       "is a usual target for LED in flowering."),
      ("Grams for each cycle",
       "450 g/m² × 100 m² = <strong>45,000 g for each cycle</strong>."),
      ("Cycles each year",
       "56 days of flowering + 7 days of turn time = 63 days of cycle length. 365 ÷ 63 = <strong>5.8 cycles each year</strong>."),
      ("Grams each year",
       "45,000 g × 5.8 = <strong>261,000 g = 261 kg each year</strong>."),
      ("Lighting energy",
       "35 kW × 12 h × 56 days = <strong>23,520 kWh for each cycle</strong> of lighting."),
      ("All-in energy",
       "23,520 × 2.2 = <strong>51,744 kWh for each cycle</strong>. With 5.8 cycles, the result is "
       "approximately <strong>300,000 kWh each year</strong>. Do a check: 300,000 ÷ 261 kg = "
       "approximately 1,150 kWh for each kg. This value is low for indoor production. Many rooms "
       "operate at 2 to 4 times this value" + _c("nfd-energy-compare") + "."),
      ("Calculate the cost of energy",
       "300,000 kWh × $0.20 = <strong>$60,000 each year</strong>."),
      ("Add the other cost items",
       "Labor $200,000 · rent $60,000 · testing + compliance $46,000 · depreciation $43,000 "
       "($300,000 ÷ 7) · other overhead $40,000 · media + nutrients $26,000 · packaging $20,000. "
       "With energy: <strong>$495,000 each year</strong>."),
      ("Divide",
       "$495,000 ÷ 261,000 g = <strong>$1.90 for each gram of product</strong>. The cost for each "
       "gram is the primary metric of the room. All the other parts of this paper are methods to "
       "change it."),
    ]),
    fig("coststack", "The costs of the example room for one year, one above the other. Labor is 40% "
        "of the cost of each gram, more than two times the electricity cost. Most growers think "
        "that the electricity cost is the primary cost."),
    table(["Item", "$ each year", "$ for each gram", "Percentage", "How to calculate the number"], [
      ["Labor", "$200,000", "$0.77", "40%", "4.0 FTE at $50k for each FTE, with all the other costs. The personnel are growers, trimmers, and supervisors."],
      ["Rent", "$60,000", "$0.23", "12%", "250 m² of total floor area × $240 for each m² each year. The canopy is 40% of the floor area."],
      ["Energy", "$60,000", "$0.23", "12%", "300,000 kWh × $0.20. All-in energy = lighting energy × 2.2."],
      ["Testing + compliance", "$46,000", "$0.18", "9%", "52 five-kg batches × $500 + $20k for licenses and QA" + _c("valdes2020-testing")],
      ["Depreciation", "$43,000", "$0.16", "9%", "$300k fit-out ÷ 7 years"],
      ["Other overhead", "$40,000", "$0.15", "8%", "Insurance, security, administration, repairs"],
      ["Media + nutrients", "$26,000", "$0.10", "5%", "Approximately $45 for each m² for each cycle: substrate, salts, CO₂, and IPM"],
      ["Packaging", "$20,000", "$0.08", "4%", "Bags, totes, labels, consumables"],
      ["<strong>Total</strong>", "<strong>$495,000</strong>", "<strong>$1.90</strong>", "100%", "The only number that the bank examines"],
    ], caption="The full list of costs. The values in cents are approximate, but the total is accurate: 77+23+23+18+16+15+10+8 = 190."),
    p("Use each denominator from Section 04 for the same room. The table shows the information that "
      "each denominator gives:"),
    table(["Metric", "Value", "How to calculate it", "Information"], [
      ["g/m² for each cycle", "450", "given value", "In the middle of the ranges in Section 05"],
      ["g/m² each year", "2,610", "450 × 5.8", "The number that a metric for one cycle does not show"],
      ["g/W installed", "1.29", "45,000 ÷ 35,000", "In the top third of the range of 0.31–1.97 from the literature" + _c("backer2019-yieldgap") + ". The cause is the LED fixtures and not a better grower."],
      ["g/kWh all-in", "0.87", "45,000 ÷ 51,744", "= 1,150 kWh for each kg"],
      ["Cost for each gram", "$1.90", "495,000 ÷ 261,000", "The primary metric"],
    ], caption="One room gives five numbers, and all five are correct at the same time. Only the last number helps you to make a decision."),
  ]})

# ---------------------------------------------------------------- 09 labour
SECTIONS.append({"id": "labour", "kicker": "09 · The cost of labor", "title": "Labor costs",
  "blocks": [
    lead("When you speak to a new grower about the cost of indoor production, the grower speaks "
         "about electricity. In the example room, the electricity bill is $0.23 for each gram. The "
         "cost of labor is $0.77 for each gram. It is the largest item, and it is three times "
         "larger than the next item. Many estimates do not include labor, or they give it a value "
         "of zero, because the grower thinks ‘I will do the work myself’."),
    p("Start with the division: $200,000 of payroll divided by 261 kg is <strong>$766 for each "
      "kg</strong>. At a cost of $25/hour with all the other costs, the result is approximately 31 "
      "hours of work for each kg of product. Most of these hours are for one task: <strong>hand "
      "trimming</strong>. The usual rate of a hand trimmer is approximately 0.45–1.4 kg (1–3 lb) of "
      "dried flower in an 8-hour shift.</p><p>The wage is $15–20/hour, or $100–200 for each shift "
      "as a piece rate" + _c("triminator-industrial") + ". Divide the hours of the shift by the "
      "rate: the result is approximately 6–18 hours for each kg for trimming only. Use 10 hours. At "
      "$25/hour with all the other costs, the cost is <strong>$250 for each kg, or $0.25 for each "
      "gram, for trimming only</strong>. The cost of trimming is more than the cost of electricity."),
    fig(L.hbars("Task minutes for each kg of product, example values",
        [("Hand trim", 600), ("Defoliation part", 120), ("Harvest, bucking", 90),
         ("Plant work each day", 90), ("Irrigation + checks", 60), ("Packaging + QA", 60),
         ("Clean + prepare part", 45), ("Drying room work", 30)],
        unit=" min",
        note="Example values, not measurements. Hand trim only: ≈360–1,080 min/kg in different groups. Measure your times."),
        "An example of task minutes for each kg, with a total of approximately 1,095 min (18 h). "
        "The limits for the rate of hand trimming are from the usual rates that growers give" +
        _c("triminator-industrial") + ". For all the other values, use your measurements."),
    p("The sum of the tasks is approximately 18 h/kg, but the payroll gives approximately 31 h/kg. "
      "The 13 missing hours are for work that does not touch a bud. Examples are the work with "
      "mother plants and vegetative plants, meetings, cleaning, records, sick leave, and time "
      "between tasks with no work. The difference is the <strong>utilization</strong>. Thus a model "
      "that calculates the number of personnel from a list of tasks always gives a labor cost that "
      "is less than the payroll. Calculate the labor cost from the payroll, and use the task "
      "minutes to find the items that you must change."),
    ul(["<strong>Measure before the purchase.</strong> A trim machine with a rate of 9–18 kg/h "
        "(20–40 lb/h)" + _c("triminator-industrial") + " is much faster than 0.9 kg for each shift "
        "(2 lb for each shift). Before you pay for the machine, examine the grade of the product "
        "that it makes. Then examine if your buyer accepts this grade (Sections 11 and 14).",
        "<strong>Make the peaks of work smaller.</strong> In the weeks of harvest, you must have 3 "
        "times the personnel of week 3 of flowering. If the rooms start flowering at different "
        "times (Section 10), the problem of the number of personnel becomes a problem of the times "
        "of the tasks.",
        "<strong>Include the cost of your hours.</strong> If the cost of your hours is $0, each "
        "room that has a loss shows a profit in the model."]),
  ]})

# ---------------------------------------------------------------- 10 cycles per year
SECTIONS.append({"id": "cycles", "kicker": "10 · Cycles each year", "title": "Crop cycles each year",
  "blocks": [
    lead("All that you make in one year is the grams for each cycle × the cycles each year. Growers "
         "monitor the first term and ignore the second term. The turn time is the number of days "
         "from the harvest of one crop to the start of flowering of the next crop. The turn time "
         "changes the cycles each year, and thus it changes <em>all</em> the grams that you make in "
         "one year."),
    fig("cycles", "The example room with two turn times. 365 ÷ 63 = 5.8 cycles, and 365 ÷ 77 = 4.7 "
        "cycles. The agronomy and the yield for each cycle are the same, but the slow room sells "
        "47,700 g less each year."),
    p("The effect of the turn time is large because it multiplies the grams of each cycle. With a "
      "turn time of 7 days, the room operates 5.8 cycles each year and sells 261,000 g. If the turn "
      "time becomes 21 days, the room operates 4.7 cycles and sells 213,300 g. Causes can be a slow "
      "cleaning, clones that are not available, or a part that you get one week after the correct "
      "date.</p><p><strong>Two more weeks in each turn time give 47,700 g less each year.</strong> "
      "At a blended price of $2.20, the revenue is more than $100,000 less, and the cost does not "
      "decrease. No feed schedule has an effect of this size."),
    p("In the meta-analysis of Backer, a longer time of <em>flowering</em> increased the yield for "
      "each m²" + _c("backer2019-yieldgap") + ". You must calculate the effect of a longer "
      "flowering time correctly. One more week of flowering must give more grams than the same week "
      "gives in a new cycle. At 45,000 g for each cycle, a cycle length of 63 days gives "
      "approximately 714 g for each day. A cycle length of 70 days must give approximately 50,000 g "
      "for each cycle, which is 11% more, to give the same result. Do this division before you make "
      "the ripening longer, and not after the change."),
    steps([
      ("Write the cycle length", "Write the cycle length in days on the whiteboard. If you do not "
       "measure it, it can become longer. No person knows that the turn time becomes one day longer "
       "in each cycle."),
      ("Prepare before the harvest", "<em>Before</em> the day of the harvest, complete the repair list. Put "
       "the consumables for the room in position. Make sure that the personnel for cleaning are "
       "available. Do the work of the turn time in a short time. It is not a long task."),
      ("Prepare the vegetative plants first", "The most frequent cause of a long turn time is clones that are "
       "not available. The vegetative room must operate one full cycle before the dates of the "
       "flowering room."),
      ("Start the rooms at different times", "Four small rooms that start flowering one after the other give the "
       "same cycles each year as one large room. They make the trim labor equal in all weeks. A "
       "failure of one crop is 25% of the production and not 100%."),
    ]),
    callout("key", "Cycles each year multiply the grams",
      p("Grams for each cycle is agronomy. Cycles each year is about the operation of the facility. "
        "The second value is easier to make better, and it has a lower cost. A metric for one cycle "
        "does not show the second value, but the division for one year shows all of its effect. The "
        "cost for each gram can change when there is no change in the agronomy. Then do a check of "
        "the cycle length first.")),
  ]})

# ---------------------------------------------------------------- 11 quality vs volume
SECTIONS.append({"id": "quality-vs-volume", "kicker": "11 · Price groups", "title": "Higher prices for quality and the quantity of yield",
  "blocks": [
    p("The cost for each gram is only half of the information. Your revenue changes when the price "
      "for each gram changes, and the price is different in each group. In the US spot market at "
      "the start of 2024, the average price for indoor flower was approximately $1,378/lb "
      "($3.04/g). The prices for greenhouse flower and outdoor flower were approximately $725/lb "
      "($1.60/g) and $418/lb ($0.92/g)" + _c("cannabisbenchmarks-q1-2024") + ". The difference of "
      "the prices for the methods of production is 3 times, before you include the grades. "
      "<em>In</em> each method, the prices are different again for each grade: grade A flower, "
      "grade B flower, small buds, and trim."),
    fig(L.zones("Wholesale price groups: averages of one market, only as an example",
        0, 3.6,
        [(0.7, 1.1, L.AMBL, "outdoor ≈$0.92"), (1.3, 1.9, L.GXL, "greenhouse ≈$1.60"),
         (2.4, 3.5, L.GL, "indoor ≈$3.04")],
        unit=" $/g",
        note="US spot market 2024 (≈$418 / $725 / $1,378/lb). Your market is different. Use the structure, not the values."),
        "Price groups for each method of production, data of the US spot market 2024" +
        _c("cannabisbenchmarks-q1-2024") + ". A cost structure for indoor production is possible "
        "only if you always get prices in the indoor group."),
    p("Thus the model must use the <strong>blended price</strong> and not the price of the best "
      "grade. A decision to sell only the best grade changes all the model and not only one item. "
      "Compare two alternatives for the example room, which is almost at the break-even at a "
      "blended price of $1.90:"),
    table(["", "Alternative A: quantity", "Alternative B: grade-first"], [
      ["Production each year", "261 kg", "248 kg (−5%: lower density, slower trimming)"],
      ["Quantity of each grade", "60% A / 40% B", "85% A / 15% B"],
      ["Prices of the grades", "$2.40 A · $1.15 B", "$2.40 A · $1.15 B"],
      ["Blended price", "0.6×2.40 + 0.4×1.15 = <strong>$1.90</strong>", "0.85×2.40 + 0.15×1.15 = <strong>$2.21</strong>"],
      ["Revenue", "261,000 × 1.90 = $495,900", "248,000 × 2.21 = $548,700"],
      ["Cost", "$495,000", "$505,000 (+$10k for trimming and the work with the product)"],
      ["<strong>Profit</strong>", "<strong>approximately $900</strong>", "<strong>approximately $43,700</strong>"],
    ], caption="Example arithmetic with given values. The weight is five percent less, but the profit is forty thousand dollars more. The room is almost at the break-even. The quantities of the grades have a larger effect than the total yield."),
    callout("warn", "Make sure that you get the higher price",
      p("Get a written contract with your buyer before you change the room. Alternative B is "
        "correct only if the buyer pays the price of grade A for the larger quantity. If you try to "
        "get the best grade, the trimming hours increase and the plant density decreases. The cycle "
        "is frequently longer.</p><p>The market can pay only the price of grade B. Then you have "
        "the cost of Alternative B and the revenue of Alternative A. In most models with a profit, "
        "the error is in the lower prices for quality and not in the yield.")),
  ]})

# ---------------------------------------------------------------- 12 sensitivity
SECTIONS.append({"id": "sensitivity", "kicker": "12 · Sensitivity", "title": "Sensitivity of the cost for each gram",
  "blocks": [
    p("Before you pay for a change, use the model to find the input with the largest effect. Start "
      "with the baseline of the example room ($1.90/g). Change <strong>one input at a time</strong> "
      "in a possible range. Keep all the other inputs the same, and calculate again. Show the "
      "results in a chart with the widest range at the top. This chart is a tornado chart:"),
    fig("tornado", "Sensitivity of the cost for each gram in the example room. The yield for each "
        "cycle, labor, and cycle length have the largest effects. The inputs that most growers try "
        "to make better (price of electricity, CAPEX, nutrients) have the smallest effects."),
    table(["Input changed", "Range of change", "Cost/g range", "Difference"], [
      ["Yield for each cycle", "450 g/m² to 540 g/m² or to 360 g/m²", "$1.58–$2.37", "$0.79"],
      ["Labor cost", "±25%", "$1.70–$2.09", "$0.38"],
      ["Cycle length", "63 days to 58 days or to 70 days", "$1.77–$2.08", "$0.32"],
      ["Electricity price", "From $0.20 to 0.10 or to 0.30 for each kWh", "$1.78–$2.01", "$0.23"],
      ["Fit-out CAPEX", "±50%", "$1.81–$1.98", "$0.17"],
      ["Media + nutrients", "±30%", "$1.87–$1.93", "$0.06"],
    ], caption="Each row: one input changed, and all the other inputs at the baseline. In the row for cycle length, the energy changes with the number of cycles."),
    p("The sequence of the bars is the primary information. Compare a change of 20% in the yield "
      "with a change of half (less or more) in <em>all</em> the cost of nutrients. The yield has an "
      "effect that is four times larger. The two largest bars, yield and labor, show the "
      "performance of the grower and the quality of the procedures in the room. The bars that "
      "suppliers speak about most (price of electricity, CAPEX, bottles) are the small "
      "bars.</p><p>The sizes of the changes are also important. A change of 20% in the yield can "
      "occur because of one cycle with a pest problem or one error in steering. A change of 50% in "
      "the price of electricity occurs only if you make a new contract with the electricity "
      "supplier. The large bars are also the <em>easy</em> bars to change, in the two directions."),
    callout("tip", "Make a tornado chart for your room",
      p("Calculate the baseline again with your numbers. Increase and decrease each item 20%. Write "
        "the differences in a list, from the largest to the smallest. You can do this work in "
        "twenty minutes in a spreadsheet. The result frequently changes the sequence of your list "
        "of CAPEX items. The trimming procedure and the turn time are before all the equipment in "
        "the sequence.")),
  ]})

# ---------------------------------------------------------------- 13 break-even
SECTIONS.append({"id": "break-even", "kicker": "13 · Break-even", "title": "How to calculate the break-even",
  "blocks": [
    p("Break-even is the yield, the price, or the number of cycles at which the profit becomes "
      "zero. When you know the break-even, you have targets with numbers. There are three divisions "
      "for the example room:"),
    ul(["<strong>Break-even price</strong> at 450 g/m² and 5.8 cycles: $495,000 ÷ 261,000 g = "
        "<strong>$1.90/g blended price</strong>. If the price is less than this value, you have a "
        "loss for each gram that you sell.",
        "<strong>Break-even yield</strong> at a blended price of $2.20: $495,000 ÷ $2.20 = 225,000 "
        "g, then ÷ (100 m² × 5.8) = approximately <strong>388 g/m² for each cycle</strong>. This "
        "yield is the minimum. A lower yield gives a loss.",
        "<strong>Break-even cycles</strong> at $2.20 and 450 g/m²: 225,000 ÷ 45,000 = 5.0 cycles. "
        "Thus the cycle length must be less than 365 ÷ 5.0 = <strong>73 days</strong>. The cycle "
        "length has a maximum value."]),
    fig(L.line("Cost for each gram and yield, same cost each year",
        [("300", 2.84), ("350", 2.44), ("400", 2.13), ("450", 1.9), ("500", 1.71), ("550", 1.55), ("600", 1.42)],
        ["300", "350", "400", "450", "500", "550", "600"],
        ylab="$/g", ymax=4, ymin=0,
        note="Example room: $495k cost each year, only the yield changes. Example wholesale range: $1.50–2.50.",
        bands=[(1.5, 2.5, L.GXL, "example wholesale range")]),
        "The break-even chart shows where your cost curve goes into your price range. At 300 g/m², "
        "this room has a loss at all possible prices. At 600 g/m², the room has a profit also when "
        "the price becomes very low. The costs are the same for all yields, and thus a problem with "
        "the yield can stop the business. It does not only decrease the profit in proportion."),
    table(["Blended price", "Revenue each year (261 kg)", "Profit"], [
      ["$2.60", "$678,600", "+$183,600"],
      ["$2.20", "$574,200", "+$79,200"],
      ["$1.90", "$495,900", "approximately $0 (break-even)"],
      ["$1.60", "$417,600", "−$77,400"],
    ], caption="Example room with the same production. A change of ±$0.30 in the blended price gives a change of approximately $78k in the profit. Thus a good price group (Section 11) is as important as agronomy."),
    p("Use two methods to make the break-even a good tool. First, calculate it <em>for each "
      "limit</em> (a minimum price, a minimum yield, a maximum cycle length). Thus each person has "
      "a number that the person can change.</p><p>Second, calculate it again after each change. "
      "Costs increase slowly, prices decrease slowly, and a large profit of last year can become "
      "the break-even of this year without one large change. In mature markets, wholesale prices "
      "usually decrease" + _c("cannabisbenchmarks-q1-2024") + ". In the model, use a price range "
      "that decreases and does not increase."),
  ]})

# ---------------------------------------------------------------- 14 mistakes
SECTIONS.append({"id": "mistakes", "kicker": "14 · Causes of failure", "title": "Frequent errors in unit economics",
  "blocks": [
    p("A business can continue after one of these errors, but not if the error occurs many times. "
      "All of them are errors of denominators or missing cost items. None of them is an error of "
      "agronomy."),
    grid([
      card("Yield without the turn time",
        p("If g/m² for each cycle increases 5% and the cycles each year decrease 10%, the room is "
          "‘better’ but makes less. Use g/m² <strong>for each year</strong> and write the cycle "
          "length in days on the wall."), "denominator"),
      card("Labor with a cost of zero",
        p("If your hours have a cost of $0, each room shows a profit. Give your hours a cost at the "
          "market rate. If the model then shows a loss, the business is possible only because you "
          "do shifts without a wage."), "missing item"),
      card("CAPEX is too important",
        p("Automation with a cost of $80,000 makes the cost of the room $6,000 less each year. The "
          "payback is 13 years, but the equipment operates for only 7 years. Calculate the payback "
          "before you get the invoices. In the tornado chart, CAPEX is a small bar."), "payback"),
      card("Model with the price of grade A, revenue at the blended price",
        p("The model uses the price of the best grade for 100% of the production. In operation, "
          "30–50% of the production is grade B flower and small buds, at half of the price. Use the "
          "blended price in the model. If you do not, the revenue in each period of three months is "
          "less than the model shows."), "price"),
      card("g/W in different fixture generations",
        p("If you compare your LED g/W with the g/W of an HPS grower, you compare the efficacy of "
          "the fixtures" + _c("kusuma2020-efficacy") + " and not the agronomy. In one fixture "
          "generation, the g/W is a check of the values. In different fixture generations, the g/W "
          "gives no information."), "metric"),
      card("Loss of weight and batch failures",
        p("The losses are: loss of moisture, failures of tests, remediation, and sales with less "
          "weight than the contract. The model for California gives a failure rate in tests of "
          "approximately 4%" + _c("valdes2020-testing") + ", and this rate is only one of the "
          "losses. Use the grams that you sell, and not the grams that you harvest, in the "
          "denominator."), "missing item"),
    ], cols=2),
  ]})

# ---------------------------------------------------------------- 15 troubleshooting
SECTIONS.append({"id": "troubleshooting", "kicker": "15 · Troubleshooting", "title": "Troubleshooting",
  "blocks": [
    p("Find the symptoms first and then the causes. Do the same for a plant with a disease. But the "
      "bank statement is the sensor, and the time to get a reading is three months."),
    table(["Symptom", "Possible cause", "First check"], [
      ["Cost/g increases slowly, and you know of no change",
       "The turn time becomes longer, or the quantity of lower grades increases. Metrics for one cycle do not show these two changes.",
       "Make a chart of the cycle length in days and the blended price for the last six cycles"],
      ["Good g/m², but no profit",
       "The denominator is good, but the cycles are slow, the labor cost is large, or the price group is less than the model",
       "Calculate $/g again from the bank statements of twelve months, and not from the harvest record"],
      ["The electricity bill is much more than the model",
       "Loads other than the lights (dehumidification in winter, reheat) or a change in the hours with lights on",
       "Put one meter on the lighting circuit and one meter on all the other circuits. Record kWh/kg and compare it with your baseline and not with the values from other growers."],
      ["After each harvest, you do not complete the trimming",
       "The model uses usual rates and not measured rates",
       "Measure the time of one shift. The usual rate of hand trimming is 0.45–1.4 kg (1–3 lb) in 8 h" + _c("triminator-industrial")],
      ["The wholesale revenue is less than the spreadsheet",
       "Lower prices for quality, loss of moisture, batches with a failure or with less weight",
       "Compare the $ in the invoices with the $ in the model for each batch. Record the loss of weight in % as one item."],
      ["Cash flow is good in summer and low in winter",
       "The HVAC and dehumidification loads and the seasonality of prices occur at the same time",
       "Calculate $/g for the last twelve months, and do not examine the room with one cycle only"],
    ], caption="In almost all the rows, the correction is to measure more frequently. It is not a purchase."),
  ]})

# ---------------------------------------------------------------- 16 mental model
SECTIONS.append({"id": "mental-model", "kicker": "16 · Values to change", "title": "Values that you can change in unit economics",
  "blocks": [
    callout("key", "Short summary",
      p("There is one primary number: <strong>dollars for each gram of product, for one "
        "year</strong>. This number has three quantities that you can change: <strong>grams for "
        "each cycle</strong> (agronomy), <strong>cycles each year</strong> (operation of the "
        "facility), and <strong>dollars each year</strong> (all the cost items, counted correctly, "
        "labor first). Each metric in this paper shows one of these quantities, and each change "
        "that makes the business better changes one of the three. The plants are the product. The "
        "division is the business.")),
    p("Do these tasks this week, in this sequence:"),
    ol(["Make a list of your costs for the last twelve months. Include all eight items and the cost "
        "of your hours at the market rate.",
        "Divide by the grams that you <em>sell</em> in the same twelve months. Write the $/g result "
        "in a position where all personnel can see it.",
        "Write the cycle length in days on the whiteboard. Then record it for each cycle.",
        "Measure the time of one full trim shift and of one full harvest day. These two tasks are "
        "your largest labor items. Do these two measurements before you make a decision about a "
        "machine.",
        "Make the tornado chart with your numbers. Change the sequence of your CAPEX list to the sequence of the differences in the chart.",
        "Calculate again after each period of three months. Costs increase slowly, prices decrease slowly, and the model is correct only when its numbers are new."]),
    p("The benchmarks show that you must be careful with numbers from other growers. The literature "
      "has a range of 0.31–1.97 g/W" + _c("backer2019-yieldgap") + " and a difference of more than "
      "two hundred g/m² in the results of correct investigations" + _c("llewellyn2022-light") +
      _c("westmoreland2021-blue") + ". The number of a different person, also the $1.90 of the "
      "example room, is not your number. You can use the method in all rooms, but the results are "
      "different in each room."),
    callout("note", "Limits of this paper",
      p("Information, not financial advice: this paper shows arithmetic with numbers that have "
        "references and an example room. The regulation of licenses and tax, the access to markets, "
        "and the prices are different in each jurisdiction. Get local professional advice before "
        "you use this information for a business decision.")),
  ]})
