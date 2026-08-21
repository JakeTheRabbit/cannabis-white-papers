# -*- coding: utf-8 -*-
"""Paper: yield denominators and unit economics — g/m², g/W, g/kWh and the cost of a gram."""
import json, os
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        grid, card, chip, kv, steps)
import figs_lib as L

_FIGS = json.load(open(os.path.join(os.path.dirname(__file__), "figs_unit_economics.json"), encoding="utf-8"))

SLUG = "unit-economics"
TITLE = "Yield per watt and the cost of a gram"
EYEBROW = "Facility · Economics"
SUB = ("The three yield denominators (g/m² of canopy, g/W of light, g/kWh all-in) what each is "
       "actually for, what each hides, and a worked cost stack that turns a fictional 100 m² room "
       "into a cost per gram you can argue with. Every number cited or derived in front of you.")
META = [("gauge", "Economics"), ("image", "11 diagrams"),
        ("quote", "Evidence-linked · 14 sources"), ("clock", "~22 min read")]
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
    callout("warn", "Education, not financial advice",
      p("This paper teaches the <strong>arithmetic</strong> of growing economics: how to build a cost "
        "per gram from stated assumptions, which published benchmarks exist, and how far to trust them. "
        "It is not investment, business or tax advice. The worked example is a <strong>fictional</strong> "
        "facility. Prices, wages, power tariffs and regulation differ wildly by market, rebuild every "
        "table with your own numbers, and take real decisions to your own accountant.")),
    lead("Most grow-room conversations are about plants. Whether the room survives is decided somewhere "
         "less romantic: a division. All the dollars you spent in a year, over all the grams you sold. "
         "If that number is below your selling price, you have a business. If it isn't, you have an "
         "expensive hobby with a licence attached, and no amount of terpene talk changes it."),
    p("The trouble is that the industry's favourite yardsticks, grams per square metre, grams per watt"
      ", were built for other arguments. They are agronomy metrics and forum-bragging metrics, and they "
      "each quietly delete part of the bill. This paper walks through the three common denominators and "
      "what each is actually for, hedges the published benchmarks hard (because they deserve it), then "
      "builds a complete cost stack for a fictional 100 m² room with every step of the arithmetic shown. "
      "From there: labour (the cost line that sneaks up on almost everyone), cycles per year (the hidden "
      "multiplier), quality tiers, a sensitivity tornado, and break-even thinking."),
    p("Beginner-first, as always. If you can divide two numbers, you can follow all of it, the entire "
      "discipline of unit economics is choosing <em>which</em> two numbers to divide."),
  ]})

# ---------------------------------------------------------------- 02 vocabulary
SECTIONS.append({"id": "vocabulary", "kicker": "02 · The vocabulary", "title": "Definitions",
  "blocks": [
    p("Nine terms carry the rest of the paper. Most economic arguments between growers are two people "
      "using the same word for different fractions."),
    defterm("Denominator", "The bottom of a fraction, the thing you divide <em>by</em>. ‘Yield’ "
            "only means something once you say yield <em>per what</em>: per m², per watt, per kWh, per "
            "year, per dollar. Change the denominator and the same harvest tells a different story."),
    defterm("Canopy area vs floor area", "Canopy is the m² actually under flowering plants. Floor (or "
            "gross) area includes aisles, veg, dry room, lobby, plant-room. A facility with 100 m² of "
            "canopy might occupy 250 m² of floor. Rent is paid on floor; g/m² is quoted on canopy, mix "
            "them up and your model flatters itself by 2–3×."),
    defterm("Installed watts", "The nameplate draw of the fixtures over the canopy, the W in g/W. It says "
            "nothing about how many hours they run or what the HVAC burns keeping up with them."),
    defterm("kWh", "A kilowatt-hour: 1 kW drawn for 1 hour. The unit your power bill is written in, which "
            "is exactly why g/kWh is the energy metric that survives contact with accounting."),
    defterm("Opex vs capex", "Opex is what you burn every month: power, wages, media, rent. Capex is what "
            "you buy once and use for years: fixtures, HVAC, benches, controls. Capex sneaks back into "
            "cost per gram as depreciation."),
    defterm("Depreciation", "Spreading a one-off purchase over its useful life. A $300,000 fit-out used "
            "over 7 years is ≈$43,000 a year of cost even though no invoice arrives. Ignoring it is the "
            "classic way to ‘profit’ your way into being unable to replace anything."),
    defterm("Flip-to-flip (turn time)", "Days from putting one crop into flower to putting the <em>next</em> "
            "crop into flower, flowering days plus harvest-out, clean, and reset. This, not flowering "
            "time, sets your cycles per year."),
    defterm("Blended price", "The average price actually received across your whole harvest, A-buds, "
            "B-buds, smalls, trim, weighted by how much of each you sold. Plans quote the A-grade price; "
            "banks receive the blended one."),
    defterm("Break-even", "The point where revenue equals cost: the yield, price or cycle count at which "
            "profit is exactly zero. Everything in this paper is ultimately about which side of it you're on."),
  ]})

# ---------------------------------------------------------------- 03 core answer
SECTIONS.append({"id": "core-answer", "kicker": "03 · The core answer", "title": "Cost per gram in five lines",
  "blocks": [
    callout("key", "Cost per gram is the only score that pays rent",
      ul(["<strong>Cost per gram = every dollar for the year ÷ every gram sold that year.</strong> Not "
          "per cycle, not per room, not ‘once we're dialled in’. The bank statement, over the scale.",
          "That one fraction hides three dials: <strong>grams per cycle</strong> (agronomy), "
          "<strong>cycles per year</strong> (operations), and <strong>dollars per year</strong> (everything "
          "else). Every improvement you will ever make is one of the three.",
          "g/m², g/W and g/kWh are <strong>partial views</strong>, useful for diagnosis, dangerous as "
          "scoreboards, because each one deletes a cost the others see.",
          "Published benchmarks span roughly <strong>6× in g/W and far more in g/m²</strong> depending on "
          "conditions, quote ranges with context or don't quote them at all.",
          "Labour and turn time move the answer more than the gear you're being sold. Run the sensitivity "
          "before the credit card."])),
  ]})

# ---------------------------------------------------------------- 04 three denominators
SECTIONS.append({"id": "three-denominators", "kicker": "04 · The three denominators", "title": "g/m², g/W and g/kWh: selecting the right metric",
  "blocks": [
    p("All three metrics divide the same harvest by a different resource, and each answers a different "
      "question. The mistake is not using them. It's using one of them as the scoreboard and forgetting "
      "what it can't see."),
    fig("denoms", "Same room, same harvest, three ‘efficiency’ numbers. Each lens counts one "
        "resource and quietly drops the rest. None of them is the bill."),
    p("<strong>g/m² of canopy</strong> is the agronomist's number. It compares crops, cultivars and "
      "steering decisions on the same floor plan, and it's the number most research reports. It contains "
      "no time, a nine-week cycle and a twelve-week cycle can post the same g/m² while one produces 30% "
      "more per year, and no power, no labour, no grade mix."),
    p("<strong>g/W of installed light</strong> is a relic of the lamp-shopping era, and Section 06 gives "
      "it a full autopsy. It usefully asks ‘how much crop per unit of lighting hardware’, but "
      "the denominator is nameplate watts: it ignores how long the lamps run, everything the HVAC burns, "
      "and, fatally, which fixture generation produced the watts."),
    p("<strong>g/kWh all-in</strong> (or its reciprocal, kWh per kg) divides by every kilowatt-hour "
      "through the meter, lights, HVAC, dehumidification, pumps, the lot. It is the one denominator "
      "that reconciles against a document someone actually sends you: the power bill. It's also the "
      "industry's formal benchmarking metric, Resource Innovation Institute's PowerScore scores "
      "facilities on exactly two numbers, kWh per unit of flowering canopy and grams per kWh, across "
      "350+ producers" + _c("rii-powerscore") + ". The spread is enormous: indoor production uses on the "
      "order of 18× the energy per gram of outdoor" + _c("nfd-energy-compare") + ", which is why an "
      "indoor room lives or dies on this metric while a greenhouse barely thinks about it."),
    table(["Metric", "Good for", "Blind to", "Verdict"], [
      ["g/m² per cycle", "Comparing crops, cultivars, steering on one floor plan", "Time, power, labour, grade", "Agronomy tool, never a business score"],
      ["g/W installed", "Sizing fixtures; forum bragging", "Hours run, HVAC, fixture era, time", "Aging badly, see Section 06"],
      ["g/kWh all-in", "Energy productivity; matches the power bill", "Labour, rent, capex, testing", "Best single resource metric, still not the bill"],
      ["$ per gram", "The actual decision", "Nothing, if built honestly", "The scoreboard"],
    ], caption="Four ways to divide a harvest. The first three are diagnostics; only the fourth pays rent."),
    callout("tip", "The canopy trap",
      p("Whenever anyone quotes a per-m² number, yours included, ask <em>which m²</em>. Canopy, room "
        "floor, or whole building? A 450 g/m² canopy figure becomes ≈180 g/m² of building the moment you "
        "include aisles, veg and dry space at a typical 40% canopy-to-floor ratio. Both are true; only "
        "one of them divides into the rent.")),
  ]})

# ---------------------------------------------------------------- 05 benchmarks
SECTIONS.append({"id": "benchmarks", "kicker": "05 · Benchmarks", "title": "Published yield benchmarks and their limits",
  "blocks": [
    lead("Published cannabis yield figures are a minefield of mixed conditions, mixed denominators and "
         "outright projection. Before you benchmark against anything, look at what the honest sources "
         "actually report, and how far apart they are."),
    fig("spread", "Published ranges as reported. Top: g/m² per cycle" + _c("toonen2006-yield") +
        _c("llewellyn2022-light") + _c("westmoreland2021-blue") + _c("backer2019-yieldgap") +
        ". Bottom: g per installed W" + _c("toonen2006-yield") + _c("potter2012-gpw") +
        _c("backer2019-yieldgap") + ". Conditions differ wildly between rows. That is the lesson."),
    p("<strong>The forensic baseline.</strong> The most honest large-sample g/m² figure in the "
      "literature is also the oldest: Dutch police weighed confiscated illicit grows, and the model "
      "for the median room, 15 plants/m² under 510 W/m² of HPS, came out at <strong>33.7 g per plant, "
      "505 g/m²</strong>" + _c("toonen2006-yield") + ". Note the division: 505 g/m² over 510 W/m² is "
      "0.99 g/W. That single study is almost certainly where ‘a gram per watt’ folklore comes "
      "from, a median, from HPS rooms, twenty years ago."),
    p("<strong>The controlled trials.</strong> Potter &amp; Duncombe grew under 270, 400 and 600 W/m² of "
      "HPS and measured <strong>0.9–1.6 g/W</strong>, with the best gram-per-watt result at the "
      "<em>lowest</em> wattage" + _c("potter2012-gpw") + ". More light grew more grams but fewer grams "
      "per watt: diminishing returns per unit of power, measured. Modern LED work shows the same shape "
      "from the other side, dry flower yield kept climbing roughly linearly with light intensity up to "
      "≈1,800 µmol·m⁻²·s⁻¹ with no plateau" + _c("rm2021-light") + ", and a follow-up at 600–1,000 "
      "µmol found each extra 100 µmol worth ≈4.6 g/plant (≈51 g/m² at ~10 plants/m²), for yields of "
      "roughly <strong>276–447 g/m²</strong> across that range" + _c("llewellyn2022-light") + ". "
      "Bugbee's group, growing high-light hemp for cannabinoids, reported <strong>500–750 g/m²</strong> "
      "across three trials" + _c("westmoreland2021-blue") + "."),
    p("<strong>The meta-analysis, and why you hedge.</strong> Backer et al. pooled the literature and "
      "found reported efficiencies of <strong>0.31–1.97 g/W</strong>, a 6× spread, and "
      "scaled-up yield projections running from 3.4 to <strong>3,590 g/m²</strong>, a thousand-fold "
      "range driven by extrapolating small-plot numbers to areas nobody actually grew" +
      _c("backer2019-yieldgap") + ". They also found that raising installed W/m² <em>reduced</em> yield "
      "per watt, and that longer flowering periods raised yield per m². Both of which are denominator "
      "stories, not plant stories."),
    table(["Source", "Conditions", "Reported", "Read it as"], [
      ["Toonen 2006" + _c("toonen2006-yield"), "Median illicit NL room, HPS, 15 plants/m²", "505 g/m² · ≈0.99 g/W", "The origin of the folklore"],
      ["Potter &amp; Duncombe 2012" + _c("potter2012-gpw"), "HPS at 270/400/600 W/m²", "0.9–1.6 g/W, best at lowest W", "Diminishing returns per watt"],
      ["Rodriguez-Morrison 2021" + _c("rm2021-light"), "Indoor, up to ≈1,800 µmol", "Yield ≈linear with light, no plateau", "Light buys grams, at a power price"],
      ["Llewellyn 2022" + _c("llewellyn2022-light"), "LED, 600–1,000 µmol, ~10 plants/m²", "≈276–447 g/m²; +51 g/m² per 100 µmol", "A defensible research band"],
      ["Westmoreland 2021" + _c("westmoreland2021-blue"), "High light, three trials", "500–750 g/m²", "The high end, under research care"],
      ["Backer 2019 meta" + _c("backer2019-yieldgap"), "Pooled literature", "0.31–1.97 g/W; projections to 3,590 g/m²", "Why you never quote one number"],
      ["Commercial folklore", "Uncited, everywhere", "‘300–600 g/m² per cycle’", "Plausible band, zero provenance, treat as anecdote"],
    ], caption="The honest benchmark table: every row true under its own conditions, no two rows comparable without caveats."),
    callout("evidence", "Why the spread is that wide",
      p("Plant density, cultivar, light level, pot size, flowering length, and, above all, <em>what "
        "counted as yield</em> (whole flower? trimmed A-bud? paper projection?) all differ between "
        "studies. None of that makes the studies wrong. It makes single-number benchmarks wrong. When "
        "someone quotes ‘you should be getting X’, the only professional response is: "
        "<em>under what conditions, measured how?</em>")),
  ]})

# ---------------------------------------------------------------- 06 g/W autopsy
SECTIONS.append({"id": "gram-per-watt", "kicker": "06 · The aging metric", "title": "Grams per watt as a legacy lighting metric",
  "blocks": [
    lead("‘A gram a watt’ was a useful rule of thumb when every serious room ran the same "
         "lamp. Under LED it has quietly become a measure of <em>when you bought your fixtures</em>, "
         "because the denominator changed underneath the metric."),
    p("A fixture converts watts into photons, and the exchange rate is called <strong>efficacy</strong>, "
      "in µmol of photons per joule. Double-ended HPS, the lamp the folklore was built on, delivers "
      "about 1.72 µmol/J. The best LED fixtures measured in 2020 hit ≈3.0 µmol/J (blue/red) and 2.78 "
      "(white/red), against practical ceilings around 3.4–4.1" + _c("kusuma2020-efficacy") + ". "
      "In 2014 the best LEDs managed 1.7 — HPS parity. In one fixture generation, the photons bought "
      "per watt roughly <strong>doubled</strong>."),
    fig(L.bars("Fixture efficacy, the exchange rate from watts to photons",
        [("HPS (DE)", 1.72), ("Best LED 2014", 1.7), ("Best LED 2020", 3.0), ("White+red ceiling", 3.4)],
        unit="", note="µmol of photons per joule, measured fixtures. Blue+red practical ceiling ≈4.1 µmol/J.",
        maxv=4.0),
        "Measured fixture efficacy" + _c("kusuma2020-efficacy") + ". The same watt now buys nearly "
        "twice the photons it did under HPS, so every g/W figure carries a hidden date stamp."),
    p("Now watch what that does to g/W with <em>zero</em> agronomy. Take the same fictional crop, "
      "450 g/m² at 900 µmol·m⁻²·s⁻¹. Delivering 900 µmol with 1.72 µmol/J HPS takes 900 ÷ 1.72 ≈ "
      "523 W/m²; with a 2.8 µmol/J LED it takes 900 ÷ 2.8 ≈ 321 W/m². Same photons, same plants, same "
      "grams. The HPS grower reports 450 ÷ 523 = <strong>0.86 g/W</strong>; the LED grower reports "
      "450 ÷ 321 = <strong>1.40 g/W</strong>, and neither of them grew better than the other."),
    fig(L.hbars("Same crop, same photons, only the fixture changed",
        [("HPS rig", 0.86), ("LED rig", 1.4)], unit=" g/W",
        note="Fictional 450 g/m² crop at 900 µmol. HPS at 1.72 µmol/J needs 523 W/m²; a 2.8 µmol/J LED needs 321."),
        "The g/W ‘improvement’ is the fixture's, not the grower's. Compare g/W within one "
        "fixture generation or not at all."),
    p("The efficacy shift also rewrites the buying decision. In Bugbee's lighting trials the white+red "
      "LED yielded 4.6% <em>less</em> per m² than HPS, and produced <strong>27% more per dollar of "
      "electricity</strong>" + _c("westmoreland2021-blue") + ". Judged on g/m², the LED loses. Judged "
      "on the metric that pays bills, it wins comfortably. Same data, different denominator, opposite "
      "decision. Which is the entire argument of this paper in one experiment."),
    callout("key", "What to do with g/W now",
      ul(["Use it to <strong>sanity-check a design</strong> against same-era rooms, an LED room "
          "claiming 0.6 g/W or 2.5 g/W deserves questions.",
          "Never compare across fixture generations, and never let a vendor do it for you.",
          "For decisions, translate to <strong>g/kWh all-in</strong> (add hours run and HVAC) and then "
          "to <strong>$ per gram</strong>. Watts don't appear on invoices; kilowatt-hours do."])),
  ]})

# ---------------------------------------------------------------- 07 cost stack
SECTIONS.append({"id": "cost-stack", "kicker": "07 · The cost stack", "title": "Cost components per gram",
  "blocks": [
    p("Cost per gram is built from a short, boring list. The skill isn't clever accounting. It's "
      "refusing to leave lines out. Eight lines cover a small indoor facility:"),
    ul(["<strong>Labour</strong>, wages plus the on-costs (leave, insurance, tax) for everyone who "
        "touches the crop, <em>including you at a market rate</em>.",
        "<strong>Energy</strong>, lights, HVAC, dehumidification, pumps, controls. All of it, off the "
        "bill, not off the fixture nameplate. For context on how dominant this line is indoors: US "
        "indoor production was estimated at 1% of national electricity a decade ago" + _c("mills2012-carbon") +
        ", and modelled emissions run 2,283–5,184 kg CO₂e per kg of flower depending on climate" +
        _c("summers2021-ghg") + ".",
        "<strong>Media + nutrients</strong>, substrate, salts, CO₂, IPM consumables.",
        "<strong>Rent</strong>, on gross floor area, not canopy.",
        "<strong>Depreciation</strong>, the fit-out and gear, spread over useful life.",
        "<strong>Testing + compliance</strong>, lab panels per batch plus licences, QA time, records. "
        "California data put mandatory testing alone at ≈$136 per pound (≈$0.30/g) once sampling and "
        "failure rates are counted" + _c("valdes2020-testing") + ", a real line, not a rounding error.",
        "<strong>Packaging + consumables</strong>, bags, totes, labels, gloves.",
        "<strong>Other overhead</strong>, insurance, security, admin, repairs, software."]),
    fig(L.flow("Building a cost per gram, the method",
        [("Count the dollars", "Twelve months of bank statement, all eight lines, no exceptions"),
         ("Count the grams", "Grams actually sold in the same twelve months, not harvested, sold"),
         ("Divide", "Dollars over grams. That's the number. Resist adjusting it"),
         ("Rank the lines", "Sort the stack largest first. The order is your to-do list"),
         ("Attack the top", "A 10% cut to line one beats a 50% cut to line eight")],
        note="Annual numbers, always, per-cycle snapshots hide turn time and seasonality."),
        "The whole method. Everything after this section is just practice runs of these five steps."),
    callout("note", "Why annual, not per-cycle",
      p("A per-cycle cost ignores the days the room earned nothing, turn time, a failed batch, the "
        "month the dehumidifier died. Twelve months of dollars over twelve months of grams captures all "
        "of it automatically. It's also the only version your accountant, your bank and your licence "
        "renewal will recognise.")),
  ]})

# ---------------------------------------------------------------- 08 worked example
SECTIONS.append({"id": "worked-example", "kicker": "08 · The worked example", "title": "Worked example: a fictional 100 m² room",
  "blocks": [
    callout("warn", "Fictional facility, assumptions, not survey data",
      p("Everything below is a <strong>made-up room with stated assumptions</strong>, chosen to be "
        "plausible and to divide cleanly. It is not any real facility's numbers and not a target. The "
        "point is the <em>method</em>: swap in your own values line by line and the arithmetic carries.")),
    kv([("Flowering canopy", "100 m² (≈250 m² gross floor, 40% canopy ratio)"),
        ("Lighting", "LED, 2.6 µmol/J, 350 W per m² of canopy → 35 kW installed"),
        ("Photoperiod / flower", "12 h · 56 days in flower"),
        ("Turn time", "7 days (harvest-out, clean, reset, flip)"),
        ("Yield assumption", "450 g/m² per cycle, mid-band, see Section 05"),
        ("Electricity price", "$0.20 per kWh (generic dollars throughout)"),
        ("Non-lighting energy", "All-in electricity = 2.2 × lighting kWh (HVAC, dehu, fans, veg, dry)"),
        ("Staffing", "4.0 FTE all-in at $50,000 loaded each"),
        ("Fit-out capex", "$300,000, straight-line over 7 years")]),
    steps([
      ("Fix the canopy and the light",
       "100 m² × 350 W/m² = <strong>35,000 W = 35 kW</strong> installed. Sanity-check the intensity: "
       "350 W/m² × 2.6 µmol/J = <strong>910 µmol·m⁻²·s⁻¹</strong>, a normal LED flower target."),
      ("Grams per cycle",
       "450 g/m² × 100 m² = <strong>45,000 g per cycle</strong>."),
      ("Cycles per year",
       "56 flower days + 7 turn days = 63 days flip-to-flip. 365 ÷ 63 = <strong>5.8 cycles per year</strong>."),
      ("Grams per year",
       "45,000 g × 5.8 = <strong>261,000 g = 261 kg per year</strong>."),
      ("Lighting energy",
       "35 kW × 12 h × 56 days = <strong>23,520 kWh per cycle</strong> of lighting."),
      ("All-in energy",
       "23,520 × 2.2 = <strong>51,744 kWh per cycle</strong> → × 5.8 ≈ <strong>300,000 kWh per year</strong>. "
       "Cross-check: 300,000 ÷ 261 kg ≈ 1,150 kWh per kg, efficient-end for indoor; plenty of real "
       "rooms run 2–4× this" + _c("nfd-energy-compare") + "."),
      ("Price the energy",
       "300,000 kWh × $0.20 = <strong>$60,000 per year</strong>."),
      ("Add the rest of the stack",
       "Labour $200,000 · rent $60,000 · testing + compliance $46,000 · depreciation $43,000 "
       "($300,000 ÷ 7) · other overhead $40,000 · media + nutrients $26,000 · packaging $20,000. "
       "With energy: <strong>$495,000 per year</strong>."),
      ("Divide",
       "$495,000 ÷ 261,000 g = <strong>$1.90 per finished gram</strong>. That is the room's real "
       "scoreboard, everything else in this paper is a way of moving it."),
    ]),
    fig("coststack", "The fictional room's year, stacked. Labour is 40% of every gram, more than "
        "double the power bill that gets all the attention."),
    table(["Line", "Annual $", "$ per gram", "Share", "Behind the number"], [
      ["Labour", "$200,000", "$0.77", "40%", "4.0 FTE all-in at $50k loaded, grow, trim, lead"],
      ["Rent", "$60,000", "$0.23", "12%", "250 m² gross × $240/m²/yr; canopy is 40% of floor"],
      ["Energy", "$60,000", "$0.23", "12%", "300,000 kWh × $0.20; lighting × 2.2 all-in"],
      ["Testing + compliance", "$46,000", "$0.18", "9%", "52 five-kg batches × $500 + $20k licences/QA" + _c("valdes2020-testing")],
      ["Depreciation", "$43,000", "$0.16", "9%", "$300k fit-out ÷ 7 years"],
      ["Other overhead", "$40,000", "$0.15", "8%", "Insurance, security, admin, repairs"],
      ["Media + nutrients", "$26,000", "$0.10", "5%", "≈$45 per m² per cycle, substrate, salts, CO₂, IPM"],
      ["Packaging", "$20,000", "$0.08", "4%", "Bags, totes, labels, consumables"],
      ["<strong>Total</strong>", "<strong>$495,000</strong>", "<strong>$1.90</strong>", "100%", "The only number the bank sees"],
    ], caption="The full stack. Rounded cents sum exactly: 77+23+23+18+16+15+10+8 = 190."),
    p("Now score the same room on every denominator from Section 04, so you can see what each lens "
      "would have told you:"),
    table(["Metric", "Value", "Derivation", "Comment"], [
      ["g/m² per cycle", "450", "assumed", "Mid-band against Section 05's ranges"],
      ["g/m² per year", "2,610", "450 × 5.8", "The number per-cycle bragging hides"],
      ["g/W installed", "1.29", "45,000 ÷ 35,000", "Top-third of the published 0.31–1.97 range" + _c("backer2019-yieldgap") + ", because LED, not because talent"],
      ["g/kWh all-in", "0.87", "45,000 ÷ 51,744", "= 1,150 kWh per kg"],
      ["Cost per gram", "$1.90", "495,000 ÷ 261,000", "The scoreboard"],
    ], caption="One room, five numbers, all simultaneously true. Only the last one decides anything."),
  ]})

# ---------------------------------------------------------------- 09 labour
SECTIONS.append({"id": "labour", "kicker": "09 · The sneaky #1", "title": "Labour costs",
  "blocks": [
    lead("Ask a new grower what indoor production costs and they'll talk about power. The fictional "
         "room's power bill is $0.23 a gram. Its people are $0.77 — the largest line by a factor of "
         "three, and the one most plans either omit or price at zero because ‘I'll do it myself’."),
    p("Start with the honest division: $200,000 of payroll over 261 kg is <strong>$766 per kg</strong>. "
      "At a loaded $25/hour that's ≈31 hours of paid time per finished kilogram. Where does it go? "
      "Mostly one place: <strong>hand trimming</strong>. Industry throughput for a hand trimmer is "
      "roughly 1–3 lb (0.45–1.4 kg) of dried flower per 8-hour shift, at $15–20/hour or "
      "$100–200 per shift piece-rate" + _c("triminator-industrial") + ". Run the division: that's "
      "≈6–18 hours per kg for trim alone. Call it 10 — at $25/hour loaded, <strong>$250 per kg, "
      "$0.25 per gram, just for trimming</strong>. The scissors out-cost the electricity."),
    fig(L.hbars("Where the minutes go, illustrative task budget per finished kg",
        [("Hand trim", 600), ("Defoliation share", 120), ("Harvest + buck", 90),
         ("Daily plant care", 90), ("Irrigation + checks", 60), ("Pack + QA", 60),
         ("Clean + reset share", 45), ("Dry-room handling", 30)],
        unit=" min",
        note="Planning placeholders, not measurements, hand trim alone spans ≈360–1,080 min/kg across crews. Time your own."),
        "An illustrative task-minute budget totalling ≈1,095 min (18 h) per kg. Hand-trim throughput "
        "bounds from industry practice" + _c("triminator-industrial") + "; everything else is a "
        "placeholder for your own stopwatch."),
    p("Notice the gap: tasks sum to ≈18 h/kg but payroll says ≈31. The missing 13 hours are real work "
      "that never touches a bud, mothers and veg care, meetings, cleaning, records, sick days, and "
      "plain idle time between tasks. That gap is <strong>utilisation</strong>, and it's why headcount "
      "models built from task lists always come in under the real payroll. Budget from payroll; use "
      "task minutes to find what to fix."),
    ul(["<strong>Measure before you buy.</strong> A trim machine at 20–40 lb/hour" + _c("triminator-industrial") +
        " looks unanswerable next to 2 lb/shift, but weigh the grade impact on your product and your "
        "buyer before the capex (Sections 11 and 14).",
        "<strong>Smooth the spikes.</strong> Harvest weeks need 3× the hands of week 3 of flower. "
        "Staggered rooms (Section 10) turn a hiring problem into a scheduling one.",
        "<strong>Price the founder.</strong> If your own hours enter at $0, every bad room you'll ever "
        "build will look profitable on paper."]),
  ]})

# ---------------------------------------------------------------- 10 cycles per year
SECTIONS.append({"id": "cycles", "kicker": "10 · The hidden multiplier", "title": "Annual crop cycles",
  "blocks": [
    lead("Everything you produce in a year is grams-per-cycle × cycles-per-year. The industry obsesses "
         "over the first term and lets the second one rot. Turn time, the days between harvesting one "
         "crop and flipping the next, multiplies <em>everything</em>."),
    fig("cycles", "The fictional room at two turn speeds. 365 ÷ 63 = 5.8 cycles; 365 ÷ 77 = 4.7. Same "
        "agronomy, same per-cycle yield, the slow room ships 47,700 g less a year."),
    p("The arithmetic is brutal because it's a division that compounds. At a 7-day turn the room runs "
      "5.8 cycles and ships 261,000 g. Let the turn drift to 21 days, a slow clean here, a late clone "
      "batch there, a week waiting on a parts order, and it's 4.7 cycles and 213,300 g. <strong>Two "
      "extra weeks per turn costs 47,700 g a year</strong>: at a $2.20 blended price, over $100,000 of "
      "revenue, for zero saved cost. No nutrient program on earth moves the needle like that."),
    p("Backer's meta-analysis found longer <em>flowering</em> raised yield per m²" + _c("backer2019-yieldgap") +
      ", and that's exactly the trade to price properly: an extra week of flower must earn more grams "
      "than the same week would earn as a fresh cycle. At 45,000 g per cycle, a 63-day flip earns "
      "≈714 g per calendar day; a 70-day flip has to yield ≈50,000 g per cycle, 11% more, just to "
      "tie. Run that division before you extend ripening, not after."),
    steps([
      ("Define flip-to-flip", "Flower-in to flower-in, in days, on the whiteboard. If it isn't "
       "measured it will drift, nobody notices a turn stretching one day per cycle."),
      ("Pre-stage the turn", "Repair list closed, room consumables staged, clean crew booked, "
       "<em>before</em> harvest morning. The turn is a pit stop, not a project."),
      ("Keep veg ahead of flower", "The most common turn-killer is clones that aren't ready. Veg "
       "capacity must run one full flip ahead of the flower room's calendar."),
      ("Stagger if you can", "Four small rooms flipping in rotation give the same annual cycles as one "
       "big room, but level the trim labour and turn a crop failure into a 25% event instead of 100%."),
    ]),
    callout("key", "The multiplier mindset",
      p("Grams per cycle is agronomy. Cycles per year is discipline. The second is cheaper to improve, "
        "invisible on every per-cycle metric, and shows up whole in the annual division. When cost per "
        "gram drifts and nothing agronomic changed, check the calendar first.")),
  ]})

# ---------------------------------------------------------------- 11 quality vs volume
SECTIONS.append({"id": "quality-vs-volume", "kicker": "11 · Price tiers", "title": "Quality premiums and yield volume",
  "blocks": [
    p("Cost per gram is half the story; the cheque depends on the price per gram, and price is tiered. "
      "US spot-market averages in early 2024 ran ≈$1,378/lb for indoor flower (≈$3.04/g), $725/lb "
      "greenhouse (≈$1.60/g) and $418/lb outdoor (≈$0.92/g)" + _c("cannabisbenchmarks-q1-2024") + " — "
      "a 3× spread on production method alone, before grade tiers <em>within</em> each method split "
      "further into A-flower, B/smalls and trim, each with its own price."),
    fig(L.zones("Wholesale price tiers, one market's averages, for shape not gospel",
        0, 3.6,
        [(0.7, 1.1, L.AMBL, "outdoor ≈$0.92"), (1.3, 1.9, L.GXL, "greenhouse ≈$1.60"),
         (2.4, 3.5, L.GL, "indoor ≈$3.04")],
        unit=" $/g",
        note="US 2024 spot averages (≈$418 / $725 / $1,378 per lb). Your market will differ. The tier structure is the lesson."),
        "Price tiers by production method, US 2024 spot data" + _c("cannabisbenchmarks-q1-2024") +
        ". An indoor cost structure only makes sense if you reliably clear indoor-tier prices."),
    p("This is why <strong>blended price</strong>, not headline price, belongs in the model, and why "
      "chasing top-shelf changes the whole equation rather than one line of it. Compare two strategies "
      "for the fictional room, which sits near break-even at a $1.90 blended price:"),
    table(["", "Path A, volume", "Path B, grade-first"], [
      ["Annual output", "261 kg", "248 kg (−5%: lower density, slower trim)"],
      ["Grade mix", "60% A / 40% B", "85% A / 15% B"],
      ["Tier prices", "$2.40 A · $1.15 B", "$2.40 A · $1.15 B"],
      ["Blended price", "0.6×2.40 + 0.4×1.15 = <strong>$1.90</strong>", "0.85×2.40 + 0.15×1.15 = <strong>$2.21</strong>"],
      ["Revenue", "261,000 × 1.90 = $495,900", "248,000 × 2.21 = $548,700"],
      ["Cost", "$495,000", "$505,000 (+$10k trim & handling)"],
      ["<strong>Profit</strong>", "<strong>≈ $900</strong>", "<strong>≈ $43,700</strong>"],
    ], caption="Fictional arithmetic, stated assumptions. Five percent less weight, forty grand more profit, near break-even, grade mix is a bigger dial than gross yield."),
    callout("warn", "The premium has to be real",
      p("Path B only works if the channel genuinely pays the A-tier price for your extra grade, a "
        "promise worth getting in writing before you rebuild the room around it. Chasing top-shelf "
        "raises trim hours, lowers plant density, and often stretches the cycle; if the market then "
        "pays you B-tier money anyway, you've built Path B's cost base with Path A's revenue. "
        "Quality-tier discounts, not yield, are where most ‘profitable’ models die.")),
  ]})

# ---------------------------------------------------------------- 12 sensitivity
SECTIONS.append({"id": "sensitivity", "kicker": "12 · Sensitivity", "title": "Cost-per-gram sensitivity",
  "blocks": [
    p("Before spending a dollar to improve the room, ask the model which dial is worth touching. The "
      "method: take the fictional baseline ($1.90/g), move <strong>one input at a time</strong> across "
      "a plausible swing, hold everything else, and recompute. Plot the results widest-first and you "
      "get a tornado:"),
    fig("tornado", "Sensitivity of cost per gram in the fictional room. Yield per cycle, labour and "
        "turn time dominate; the inputs people love optimising (power price, capex, nutrients) trail "
        "the field."),
    table(["Input moved", "Swing tested", "Cost/g range", "Span"], [
      ["Yield per cycle", "450 → 540 / 360 g/m²", "$1.58 – $2.37", "$0.79"],
      ["Labour bill", "±25%", "$1.70 – $2.09", "$0.38"],
      ["Cycle length", "63 → 58 / 70 days", "$1.77 – $2.08", "$0.32"],
      ["Electricity price", "$0.20 → 0.10 / 0.30 per kWh", "$1.78 – $2.01", "$0.23"],
      ["Fit-out capex", "±50%", "$1.81 – $1.98", "$0.17"],
      ["Media + nutrients", "±30%", "$1.87 – $1.93", "$0.06"],
    ], caption="Each row: one input moved alone, rest held at baseline. Energy re-scales with cycle count in the cycle-length row."),
    p("Read the order, because it's the whole strategy. A 20% yield move swings cost per gram four times "
      "further than halving-or-adding-half to the <em>entire</em> nutrient budget. The two biggest bars"
      ", yield and labour, are grower skill and process design. The bars vendors talk about most ("
      "power price, capex, bottles) are the small ones. And note what the swing sizes hide: a 20% "
      "yield swing is one bad pest cycle or one steering mistake, while a 50% power-price swing "
      "requires renegotiating with a utility. The big bars are also the <em>easy</em> ones to move, in "
      "both directions."),
    callout("tip", "Run your own tornado",
      p("Rebuild the baseline with your numbers, then move each line ±20% and rank the spans. It takes "
        "twenty minutes in a spreadsheet and it will re-order your capex wishlist, usually by moving "
        "the trim process and the turn calendar above every piece of hardware on it.")),
  ]})

# ---------------------------------------------------------------- 13 break-even
SECTIONS.append({"id": "break-even", "kicker": "13 · Break-even", "title": "Break-even analysis",
  "blocks": [
    p("Break-even is the yield, price or cycle count where profit crosses zero, and knowing where it "
      "sits turns vague anxiety into specific targets. Three divisions, same fictional room:"),
    ul(["<strong>Break-even price</strong> at 450 g/m² and 5.8 cycles: $495,000 ÷ 261,000 g = "
        "<strong>$1.90/g blended</strong>. Below that cheque, every gram ships at a loss.",
        "<strong>Break-even yield</strong> at a $2.20 blended price: $495,000 ÷ $2.20 = 225,000 g → "
        "÷ (100 m² × 5.8) = <strong>≈388 g/m² per cycle</strong>. That's the floor under a bad run.",
        "<strong>Break-even cycles</strong> at $2.20 and 450 g/m²: 225,000 ÷ 45,000 = 5.0 cycles → "
        "flip-to-flip must stay under 365 ÷ 5.0 = <strong>73 days</strong>. The calendar has a red line."]),
    fig(L.line("Cost per gram vs yield, annual spend held flat",
        [("300", 2.84), ("350", 2.44), ("400", 2.13), ("450", 1.9), ("500", 1.71), ("550", 1.55), ("600", 1.42)],
        ["300", "350", "400", "450", "500", "550", "600"],
        ylab="$ per gram", ymax=4, ymin=0,
        note="Fictional room: $495k spend fixed, yield the only mover. Band: an illustrative $1.50–2.50 wholesale range.",
        bands=[(1.5, 2.5, L.GXL, "illustrative wholesale band")]),
        "The break-even picture: where your cost curve crosses your price band. At 300 g/m² this room "
        "loses money at any realistic price; at 600 g/m² it survives a price collapse. Fixed costs are "
        "why yield problems are existential rather than proportional."),
    table(["Blended price", "Annual revenue (261 kg)", "Profit"], [
      ["$2.60", "$678,600", "+$183,600"],
      ["$2.20", "$574,200", "+$79,200"],
      ["$1.90", "$495,900", "≈ $0 — break-even"],
      ["$1.60", "$417,600", "−$77,400"],
    ], caption="Fictional room at fixed output. A ±$0.30 move in blended price swings profit by ≈$78k, price tier discipline (Section 11) is worth as much as agronomy."),
    p("Two habits make break-even thinking useful rather than depressing. First, compute it "
      "<em>per constraint</em> (a price floor, a yield floor, a calendar ceiling) so every team "
      "member owns a number they can actually influence. Second, recompute after every change: costs "
      "creep, prices sag, and last year's comfortable margin can become this year's break-even without "
      "a single dramatic event. Falling wholesale prices have been the norm in maturing markets" +
      _c("cannabisbenchmarks-q1-2024") + ", build the model expecting the band to move down, not up."),
  ]})

# ---------------------------------------------------------------- 14 mistakes
SECTIONS.append({"id": "mistakes", "kicker": "14 · Failure modes", "title": "Common unit-economics mistakes",
  "blocks": [
    p("Every one of these is survivable once and fatal as a habit. All of them are denominators or "
      "missing lines. None of them is agronomy."),
    grid([
      card("Counting yield, not turn time",
        p("g/m² per cycle up 5%, cycles per year down 10%, the room got ‘better’ and produced "
          "less. Score g/m² <strong>per year</strong> and put flip-to-flip days on the wall."), "denominator"),
      card("The free-labour illusion",
        p("Founder hours priced at $0 make any room look profitable. Price yourself at market rate; if "
          "the model dies, the business was you subsidising it with unpaid shifts."), "missing line"),
      card("Capex worship",
        p("$80,000 of automation to save $6,000 a year is a 13-year payback on gear with a 7-year life. "
          "Payback maths before invoices, and remember the tornado: capex was the small bar."), "payback"),
      card("Planning at A-grade, selling at blended",
        p("The plan quotes top-tier price on 100% of output. Reality ships 30–50% as B/smalls at "
          "half the tier. Model the blended price or be surprised every single quarter."), "price"),
      card("Cross-era g/W bragging",
        p("Comparing your LED g/W to an HPS grower's is comparing fixture efficacy" + _c("kusuma2020-efficacy") +
          ", not growing. Within one era it's a sanity check; across eras it's astrology."), "metric"),
      card("Forgetting shrink and failed batches",
        p("Moisture loss, failed tests, remediation, short-shipped orders. California's modelled testing "
          "failure rate alone was ≈4%" + _c("valdes2020-testing") + ". Grams sold, not grams harvested, "
          "belong in the denominator."), "missing line"),
    ], cols=2),
  ]})

# ---------------------------------------------------------------- 15 troubleshooting
SECTIONS.append({"id": "troubleshooting", "kicker": "15 · Troubleshooting", "title": "Troubleshooting",
  "blocks": [
    p("Symptoms first, causes second, same as diagnosing a sick plant, except the sensor is the bank "
      "statement and the lag is a full quarter."),
    table(["Symptom", "Likely cause", "Check first"], [
      ["Cost/g creeping up, nothing obviously changed",
       "Turn time stretching or grade mix sliding, both invisible to per-cycle metrics",
       "Plot flip-to-flip days and blended price for the last six cycles"],
      ["Great g/m², still no margin",
       "Denominator theatre: slow cycles, heavy labour, or price tier below plan",
       "Recompute $/g from twelve months of bank statement, not the harvest log"],
      ["Energy bill far above the model",
       "Non-lighting loads (winter dehu, reheat) or lights-on hours drifting",
       "Meter the lighting circuit separately; track kWh/kg against your own baseline, not folklore"],
      ["Trim backlog after every harvest",
       "Throughput planned at folklore rates rather than measured ones",
       "Time one shift: hand trim commonly runs 0.45–1.4 kg per 8 h" + _c("triminator-industrial")],
      ["Wholesale cheque smaller than the spreadsheet",
       "Quality discounts, moisture loss, failed or short batches",
       "Reconcile invoiced $ vs modelled $ per batch; track shrink % as its own line"],
      ["Cash fine in summer, ugly in winter",
       "Seasonal HVAC/dehu load and price seasonality stacking",
       "Twelve-month rolling $/g, never judge the room on a single cycle"],
    ], caption="The common thread: the fix is almost always measurement cadence, not a purchase."),
  ]})

# ---------------------------------------------------------------- 16 mental model
SECTIONS.append({"id": "mental-model", "kicker": "16 · The mental model", "title": "Unit-economics control variables",
  "blocks": [
    callout("key", "The one-paragraph version",
      p("Upstairs there is one number: <strong>dollars per finished gram, per year</strong>. Downstairs "
        "there are three dials: <strong>grams per cycle</strong> (agronomy), <strong>cycles per "
        "year</strong> (discipline), <strong>dollars per year</strong> (every line, honestly counted, "
        "labour first). Every metric in this paper is a window onto one dial; every improvement you "
        "will ever make turns one of the three. The plants are the product. The division is the "
        "business.")),
    p("What to actually do this week, in order:"),
    ol(["Build your own cost stack from the last twelve months of real spending, all eight lines, "
        "founder hours priced at market rate.",
        "Divide by grams <em>sold</em> in the same twelve months. Write the $/g answer somewhere "
        "prominent and slightly uncomfortable.",
        "Put flip-to-flip days on the whiteboard and start the streak.",
        "Time one full trim shift and one full harvest day, your two biggest labour blocks, before "
        "considering any machine.",
        "Run the tornado with your numbers and re-rank your wishlist by span, not by excitement.",
        "Recompute quarterly. Costs creep, prices sag, and the model is only honest while it's fresh."]),
    p("And keep the humility the benchmarks force on you: the published record spans 0.31–1.97 g/W" +
      _c("backer2019-yieldgap") + " and hundreds of g/m² between honest studies" + _c("llewellyn2022-light") +
      _c("westmoreland2021-blue") + ". Nobody else's number, including the fictional room's $1.90 — is "
      "your number. The method is portable; the answers never are."),
    callout("note", "Scope reminder",
      p("Education, not financial advice: this paper shows arithmetic on cited public figures and a "
        "fictional example. Licensing, tax, market access and prices are jurisdiction-specific, get "
        "local professional advice before betting money on any of it.")),
  ]})
