# -*- coding: utf-8 -*-
"""Paper: vegetative management and timing, sizing veg by plant count, pot size and canopy plan."""
import json, os
from components import (p, lead, h, ul, ol, callout, defterm, table, figure, grid, card, chip, kv, steps)
import figs_lib as L

_FIGS = json.load(open(os.path.join(os.path.dirname(__file__), "figs_veg_management.json"), encoding="utf-8"))

SLUG = "veg-management"
TITLE = "Vegetative management: build the frame, then flip"
EYEBROW = "Veg · Timing"
SUB = ("Veg is not the waiting room before the real grow. It is where plant count, pot size and "
       "canopy plan get converted into a number of days, and where almost every week-3-of-flower "
       "problem is either prevented or booked in.")
META = [("leaf", "Vegetative"), ("image", "11 diagrams"),
        ("quote", "Evidence-linked · 14 sources"), ("clock", "~14 min read")]
RELATED = ["defoliation-training", "light-acclimation"]
REF_IDS = ["dang-2022-photoperiod-switch-meta",
           "schober-2024-veg-duration-density",
           "danziger-2022-planting-density",
           "backer-2019-yield-gap",
           "poorter-2012-pot-size",
           "gwe-flowering-stretch",
           "ilgm-stretch-guide",
           "rqs-topping-guide",
           "moher-2022-cannabis-vegetative-light-intensity-morphology",
           "jin-2019-indoor-review",
           "chandra2008-photo",
           "moher2023-photoperiod",
           "saloner-2020-cannabis-nitrogen-supply",
           "grodan-growguide-steering"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

# ---------------------------------------------------------------- 1 · start here
SECTIONS.append({"id": "intro", "kicker": "Start here", "title": "Veg is where the crop is decided",
  "blocks": [
    lead("By the time you flip to 12/12, most of what the harvest can be is already locked in: how "
         "many bud sites exist, how much leaf powers them, whether the canopy is level, and whether "
         "the roots can fund the stretch. Flower doesn't build any of that. Veg does. Flower just "
         "runs the machine that veg built."),
    p("Because veg feels uneventful &mdash; no buds, nothing to weigh &mdash; beginners treat it as "
      "a waiting room and operators treat it as a buffer. Both are expensive. Across published "
      "indoor trials, growers run veg anywhere from about 2 to 26 weeks, with a median around 30 "
      "days" + _c("dang-2022-photoperiod-switch-meta") + ". That spread isn't confusion. Different "
      "rooms genuinely need different veg lengths, and this paper is about calculating yours "
      "instead of guessing it."),
    p("The working logic: veg exists to build a <strong>frame</strong> &mdash; roots, stems, nodes "
      "and leaf &mdash; sized to the share of canopy each plant must fill. Plant count, pot size "
      "and target canopy fix the frame; the frame fixes the days. Everything else in this guide "
      "(stretch budgets, topping timing, environment, feed, root-zone gates) hangs off that."),
    figure(L.flow("What veg is actually building",
            [("Roots", "fill the pot and drive uptake"),
             ("Nodes", "each node is a future bud site"),
             ("Leaves", "the solar array for bulk-up"),
             ("Frame", "scaffold that carries flower")],
            note="Flower fills the frame that veg built. No frame, nothing to fill."), 1,
      "The four things veg builds. Every day of veg should be buying one of them; a day that "
      "isn't is rent."),
    callout("note", "Who this is for",
      p("Anyone who has ever flipped 'when it looked big enough' &mdash; from a first tent to a "
        "licensed room. Pairs with <a href='defoliation-training.html'>defoliation &amp; "
        "training</a> (the how of cutting and bending) and "
        "<a href='light-acclimation.html'>light acclimation</a> (the how of raising PPFD). This "
        "paper is the <em>when and how long</em>.")),
  ]})

# ---------------------------------------------------------------- 2 · glossary
SECTIONS.append({"id": "key-terms", "kicker": "Plain-language glossary", "title": "The words you need before we start",
  "blocks": [
    p("Eight terms carry this whole guide. Skim them once; each comes back in context."),
    defterm("Flip", "Switching the light schedule from long days (usually 18 hours on) to 12/12, "
            "which triggers flowering in photoperiod cannabis. 'Flip day' ends veg."),
    defterm("Node / internode", "A node is the point on a stem where leaves and side branches "
            "emerge; the internode is the bare stem between two nodes. Node count is how plant age "
            "and topping height are measured. Short internodes = a compact, strong plant."),
    defterm("Apical dominance", "The plant's habit of pouring growth into one main tip so it "
            "outraces the side branches. Topping and training exist to break it."),
    defterm("Topping / FIM", "Topping removes the main growing tip entirely, forcing two new "
            "leaders from the node below. FIM cuts through most of the tip instead, giving 3-4 "
            "messier leaders."),
    defterm("Stretch", "The rapid vertical growth in the first 1-3 weeks after the flip, when many "
            "cultivars grow to 1.5-2&times; (sometimes 3&times;) their flip height before vertical "
            "growth stops."),
    defterm("Canopy", "The top layer of the crop that actually intercepts light &mdash; measured "
            "as area (m&sup2;), fullness (how few gaps) and levelness (how even the height)."),
    defterm("Root-bound", "A root system that has run out of container: roots circle the pot wall, "
            "the pot needs constant watering, and growth stalls. A root-bound plant cannot fund a "
            "stretch."),
    defterm("EC (electrical conductivity)", "The strength of the nutrient solution, in mS/cm. "
            "Higher EC = more dissolved fertiliser. Veg feeds ramp EC up as the plant grows."),
  ]})

# ---------------------------------------------------------------- 3 · the why
SECTIONS.append({"id": "what-veg-is-for", "kicker": "The why", "title": "Build the frame that carries flower",
  "blocks": [
    p("Flowering doesn't create structure. Buds form at nodes and branch tips that already exist "
      "when you flip, plus whatever the stretch adds in its first weeks. So the size of the frame "
      "at flip is a hard ceiling on what one plant can carry. This shows up cleanly in trial data: "
      "in a controlled study that varied veg length from 1 to 4 weeks, each extra week of veg "
      "added about <strong>3.3 g of dry flower per plant</strong>, near-linearly" +
      _c("schober-2024-veg-duration-density") + "."),
    figure(L.bars("Extra flower per plant from longer veg",
            [("+1 week", 3.3), ("+2 weeks", 6.6), ("+3 weeks", 9.9)],
            unit=" g", maxv=12,
            note="Cumulative gain over a 1-week-veg baseline; CBD cultivar, controlled environment, 1-4 week veg trial."), 2,
      "Per-plant yield climbs roughly linearly with veg length in the tested range &mdash; bigger "
      "frame, more to carry" + _c("schober-2024-veg-duration-density") + ". The catch: per-plant "
      "is not the same metric as per-room."),
    p("Here is the twist that makes veg length a real decision instead of 'more is better': "
      "<strong>the room doesn't pay you per plant, it pays you per square metre.</strong> A full "
      "canopy of many small plants and a full canopy of a few big plants intercept roughly the "
      "same light. In trial data, packing plants tighter cuts yield per plant while yield per "
      "area holds or climbs" + _c("danziger-2022-planting-density") + ", and across studies plant "
      "density is a poor predictor of yield per m&sup2;" + _c("backer-2019-yield-gap") + ". "
      "Meta-analysis of photoperiod-switch timing points the same way: at fixed area, short veg "
      "periods maximise floral output per unit time, because the canopy refills faster with more, "
      "smaller frames" + _c("dang-2022-photoperiod-switch-meta") + "."),
    p("So veg length is not a lever you push for yield. It is the variable that <em>balances the "
      "equation</em>: however many plants you run, each must build a frame that fills its share of "
      "the canopy &mdash; no more, no less. Few plants, big shares, long veg. Many plants, small "
      "shares, short veg. Same canopy either way; what changes is turns per year, plant count "
      "overhead, and risk (more on that in the economics section)."),
    callout("key", "The core answer",
      p("<strong>Veg for exactly as long as it takes each plant to build its share of the canopy "
        "at or below the maximum flip height &mdash; then flip.</strong> Every day short of that "
        "is unfilled canopy in flower; every day past it is a lost fraction of a turn.")),
  ]})

# ---------------------------------------------------------------- 4 · the core decision
SECTIONS.append({"id": "veg-duration", "kicker": "The core decision", "title": "Plant count × pot size × canopy → days",
  "blocks": [
    p("Work the chain in this order. Days come out the far end &mdash; they are never the input."),
    steps([
      ("Fix the plant count",
       "Licence condition, tag budget, risk appetite or plan &mdash; whatever binds first. This is "
       "usually the least negotiable number in the room."),
      ("Measure the canopy", "Bench or tray area you intend to fill wall-to-wall, in m&sup2;. "
       "Divide by plant count: that is each plant's share &mdash; the frame it must build."),
      ("Match the pot to the frame", "A root zone can only carry so much plant. Small shares run "
       "in 4-6 L; half-metre shares want 10-30 L; full-metre trees want 30 L+ or beds (next "
       "section for why)."),
      ("Pick the training that makes the shape", "Untopped single colas for small shares; one "
       "topping round plus tie-downs for standard shares; staged topping rounds for trees. See "
       "<a href='defoliation-training.html'>defoliation &amp; training</a>."),
      ("Veg until the gate, then flip", "Flip when the canopy is ~80-90% filled, level, and at or "
       "below your maximum flip height (stretch section) &mdash; a state, not a date. The days "
       "this takes <em>is</em> your veg duration; write it down for next run."),
    ]),
    figure(_FIGS["decision"], 3,
      "The decision chain. Plant count, canopy area and pot size are the inputs; veg days are the "
      "output. The three archetypes at the bottom cover most indoor rooms."),
    table(["Archetype", "Plants per m²", "Pot / block", "Typical veg", "Training"], [
      ["Sea of green (SOG)", "10-20+", "4-6 L", "~7-14 days", "None &mdash; single colas"],
      ["Topped standard", "2-4", "10-30 L", "~14-28 days", "Top once + tie-downs + net"],
      ["Trees / count-capped", "~1", "30 L+ or beds", "35+ days", "Staged topping rounds + net"],
    ], cls="compact", caption="Hedged conventions, not lab constants &mdash; cultivar vigour, "
       "environment and transplant size all shift the day counts. The structure of the trade-off "
       "is what published density and veg-length trials support" +
       _c("schober-2024-veg-duration-density") + _c("danziger-2022-planting-density") + "."),
    p("One nuance from the meta-analysis worth knowing: floral <em>biomass</em> favoured short "
      "veg, but cannabinoid <em>concentration</em> peaked with longer veg (roughly 6-7 weeks) in "
      "the pooled data" + _c("dang-2022-photoperiod-switch-meta") + ". Treat that as a weak, "
      "cultivar-dependent signal, not a target &mdash; potency is mostly genetics and flowering "
      "conditions. It mainly says: if you're forced into long veg by a plant-count cap, you are "
      "not obviously giving quality away."),
  ]})

# ---------------------------------------------------------------- 5 · pot size
SECTIONS.append({"id": "pot-size", "kicker": "The clock inside the pot", "title": "Pot size sets how long veg can run",
  "blocks": [
    p("Roots are the half of the frame you can't see, and they cap everything. A meta-analysis of "
      "65 container studies found that, on average, <strong>doubling root-zone volume increased "
      "plant biomass by ~43%</strong> &mdash; and that cramped roots throttle growth mainly by "
      "cutting photosynthesis per unit leaf area, not just by limiting water" +
      _c("poorter-2012-pot-size") + ". A root-bound plant is a solar array running at part load: "
      "it looks leafy, it just quietly stops producing."),
    figure(L.bars("Double the root volume, roughly +43% plant",
            [("Pot volume V", 100), ("Pot volume 2V", 143)],
            unit="%", maxv=160,
            note="Average across a 65-study meta-analysis of rooting volume. The direction is the point, not the exact number."), 4,
      "Container volume is a growth ceiling, and small pots hit it fast &mdash; mostly through "
      "reduced photosynthesis, which no fertiliser fixes" + _c("poorter-2012-pot-size") + "."),
    p("The practical consequence: <strong>every pot size buys a limited veg window</strong> before "
      "the plant outgrows it. Run past the window and you either transplant again (fine, if "
      "planned) or flip a root-bound plant (never fine). The windows below are working "
      "conventions &mdash; vigorous cultivars in warm rooms burn through them faster:"),
    table(["Container", "Comfortable veg window", "Suits"], [
      ["4-6 L pot / 4&Prime; block", "~1-2 weeks", "SOG single colas"],
      ["10-15 L pot / block on slab", "~2-4 weeks", "Topped standard plants"],
      ["25-30 L pot", "~4-6 weeks", "Large topped plants, small trees"],
      ["45 L+ / beds", "6+ weeks", "Trees, mother-adjacent frames"],
    ], cls="compact", caption="Hedged convention: the window ends when roots reach the walls and "
       "the pot needs watering faster than your system wants to water. Match the pot to the "
       "planned days &mdash; or shorten the days to match the pot."),
    callout("danger", "Never flip root-bound",
      p("Stretch roughly doubles water and nutrient demand in three weeks &mdash; precisely when "
        "a root-bound pot can least supply it. The result is wilting between irrigations, early "
        "deficiency in week 2-3 of flower, and small, airy bud on a plant that looked fine at "
        "flip. If roots are circling and the pot dries in hours, pot up and give it a week "
        "<em>before</em> the flip, not after.")),
  ]})

# ---------------------------------------------------------------- 6 · stretch
SECTIONS.append({"id": "stretch", "kicker": "Height planning", "title": "Stretch: plan the flip height backwards from the ceiling",
  "blocks": [
    p("The most common veg sin isn't vegging too short &mdash; it's flipping too tall. After the "
      "flip, most cultivars surge vertically for 1-3 weeks, with the stretch largely finished "
      "around day 21 of flower" + _c("ilgm-stretch-guide") + ". How much they stretch is strongly "
      "cultivar-dependent: compact indica-leaning plants might add ~50%, typical hybrids roughly "
      "double, and stretchy sativa-leaning cultivars can double or more" +
      _c("gwe-flowering-stretch") + _c("ilgm-stretch-guide") + ". Final height &asymp; flip height "
      "&times; 1.5-2 for most plants you'll run &mdash; and you must budget for it before you "
      "flip, because you cannot un-stretch a plant into a fixed ceiling."),
    p("The arithmetic is three lines. Take the room height, subtract the fixture, its hang gap and "
      "the clearance the canopy needs below it (commonly ~60-90 cm all-in for LED, more for HPS), "
      "subtract pot-plus-bench height (~30 cm). What's left is <strong>usable plant height "
      "H</strong>. Divide H by your cultivar's stretch multiplier: that is your <strong>maximum "
      "flip height</strong>. Unknown cultivar? Assume &times;2 &mdash; the industry default of "
      "'flip at half your available height'" + _c("gwe-flowering-stretch") + "."),
    figure(_FIGS["stretch"], 5,
      "Work backwards: ceiling minus fixture stack minus bench gives usable height H; H divided "
      "by the stretch multiplier gives max flip height. The same 45 cm flip is safe at "
      "&times;1.5-2.0 and in the fixture at &times;2.5."),
    table(["Cultivar type", "Typical multiplier", "Max flip height (H = 100 cm)"], [
      ["Compact / indica-leaning", "&times;1.5", "&le;65 cm"],
      ["Typical hybrid", "&times;2.0", "&le;50 cm"],
      ["Stretchy / sativa-leaning", "&times;2.5+", "&le;40 cm"],
    ], cls="compact", caption="Multipliers are hedged industry conventions" +
       _c("gwe-flowering-stretch") + _c("ilgm-stretch-guide") + " &mdash; cultivars vary widely, "
       "and spectrum, temperature regime and topping history all shift stretch. Your own last-run "
       "number beats any table."),
    callout("tip", "Turn the multiplier into data",
      p("Tag one plant per cultivar. Measure height on flip day and again at day 21 of flower. "
        "Divide. That ratio &mdash; written on the strain card &mdash; converts next cycle's "
        "stretch from a gamble into a plan. After two runs you'll trust it more than any "
        "published range, and you should.")),
  ]})

# ---------------------------------------------------------------- 7 · topping
SECTIONS.append({"id": "topping", "kicker": "Cutting on schedule", "title": "Topping and FIM: timing and node counts",
  "blocks": [
    p("Topping is the veg tool that turns one dominant tip into two even leaders and a wider, "
      "flatter frame &mdash; the full how-and-why lives in "
      "<a href='defoliation-training.html'>defoliation &amp; training</a>. What belongs in the "
      "<em>timing</em> paper is the schedule cost, because every cut spends veg days."),
    p("The working rule: top when the plant has <strong>4-6 true nodes</strong>, typically 3-4 "
      "weeks into veg from a rooted clone or seedling, cutting above the 4th node (between the "
      "4th and 5th) &mdash; higher wastes the effect, lower removes too much plant and risks a "
      "stall" + _c("rqs-topping-guide") + ". Count nodes from the bottom, and never count the "
      "cotyledons (the first smooth round leaves). Expect <strong>7-14 days of recovery</strong> "
      "before growth speed returns, and add that time to the veg plan explicitly" +
      _c("rqs-topping-guide") + "."),
    figure(_FIGS["topping"], 6,
      "Left: the cut goes above node 4 on a plant showing 4-6 nodes. Right: two even leaders "
      "rebuild from the top remaining node. The 7-14 day recovery bill" + _c("rqs-topping-guide") +
      " is paid in veg days &mdash; plan it, don't discover it."),
    p("<strong>FIM</strong> (cutting through the top ~&frac34; of the tip rather than below it) "
      "trades predictability for speed: 3-4 leaders instead of 2, less height lost, less even "
      "regrowth. Fine for tents and trees; most commercial rooms prefer the symmetry of a clean "
      "top."),
    ol([
      "<strong>SOG:</strong> don't top at all &mdash; the whole point is one fast cola per plant.",
      "<strong>Topped standard:</strong> one round, at 4-6 nodes, done at least 10-14 days before "
      "the planned flip so recovery finishes in veg" + _c("rqs-topping-guide") + ".",
      "<strong>Trees:</strong> staged rounds &mdash; top, let leaders recover, top the leaders. "
      "Each round adds roughly 1-2 weeks of veg; three rounds is a month-plus of structure time.",
      "<strong>Never</strong> top during the stretch: the plant is re-organising for flower and "
      "responds unevenly, and you've spent recovery time you no longer have.",
    ]),
    callout("warn", "The last-cut deadline",
      p("Count backwards from flip day: <strong>flip minus 10-14 days is the last day for any "
        "major cut.</strong> Topping later than that means either postponing the flip (a real "
        "cost, decide it deliberately) or flipping mid-recovery with uneven leaders &mdash; which "
        "the stretch then amplifies into an uneven canopy for the whole flower run.")),
  ]})

# ---------------------------------------------------------------- 8 · canopy plan
SECTIONS.append({"id": "canopy-plan", "kicker": "One level, one light", "title": "Canopy establishment: level in veg or suffer in flower",
  "blocks": [
    p("Light height is a room-level setting: one fixture height serves every plant under it. That "
      "makes the <em>tallest</em> plant the dictator &mdash; raise the light to protect it and "
      "every shorter plant is suddenly under-lit; hold the light down and the tall plant bleaches "
      "and heat-stresses. An uneven canopy at flip locks in a PPFD spread of hundreds of "
      "&micro;mol between neighbouring plants for the entire flower cycle."),
    figure(_FIGS["uniformity"], 7,
      "One tall plant forces the fixture up and the whole room's light map apart; a canopy "
      "levelled in veg puts every top in the same band. Uniformity is set before the flip, not "
      "after it."),
    p("Uniformity is also a commercial property, not just an agronomic one: denser, less uniform "
      "canopies measurably increase plant-to-plant and within-plant variability in cannabinoid "
      "content &mdash; which is grade risk in any market that tests" +
      _c("danziger-2022-planting-density") + ". Levelling is done in veg with boring tools, in "
      "this order:"),
    ul([
      "<strong>Start level:</strong> one cultivar per light zone, clones from the same cohort "
      "(rooted within a few days of each other), graded by size at transplant. A 30%-undersized "
      "runt never catches up &mdash; cull it or bench it separately.",
      "<strong>Position:</strong> naturally taller plants to the edges and corners where PPFD "
      "falls off; short plants centre-stage under the hot spot.",
      "<strong>Tie down, don't cut down:</strong> from mid-veg, bend and tie the tall leaders "
      "sideways (low-stress training) so short neighbours close the gap &mdash; no recovery time "
      "spent.",
      "<strong>Net on before stretch:</strong> the trellis goes over the canopy in late veg or at "
      "flip while everything is short, then tops get tucked through the squares during weeks 1-3 "
      "of flower.",
    ]),
    callout("note", "A trellis is a plan, not a rescue",
      p("Nets installed in week 3 of flower &mdash; over sticky, branched, tangled plants &mdash; "
        "break branches and cost hours. The net's job is to receive the stretch as it happens. If "
        "it isn't on by flip day, it mostly isn't going on.")),
  ]})

# ---------------------------------------------------------------- 9 · environment
SECTIONS.append({"id": "environment", "kicker": "Targets with sources", "title": "Veg environment: temperature, humidity, light, CO2",
  "blocks": [
    p("Veg wants a slightly warmer, wetter, gentler room than flower: the plant is all leaf, "
      "shallow-rooted early on, and building tissue rather than ripening it. The table gives "
      "working bands; the two figures below unpack the ones people argue about."),
    table(["Parameter", "Early veg (fresh transplant)", "Late veg (pre-flip)", "Basis"], [
      ["Air temp, lights on", "25-28 &deg;C", "25-30 &deg;C",
       "Cannabis leaf photosynthesis peaks around 25-30 &deg;C" + _c("chandra2008-photo") +
       _c("jin-2019-indoor-review")],
      ["Relative humidity", "65-75%", "55-65%",
       "Review targets: ~75% for juveniles stepping down toward ~55-60%" + _c("jin-2019-indoor-review")],
      ["VPD", "~0.8 kPa", "1.0-1.3 kPa",
       "Same review, expressed as vapour-pressure deficit" + _c("jin-2019-indoor-review")],
      ["PPFD", "300-600 &micro;mol/m&sup2;/s, ramping", "600-900 &micro;mol/m&sup2;/s",
       "21-day veg trial across 135-1430 &micro;mol" + _c("moher-2022-cannabis-vegetative-light-intensity-morphology")],
      ["Photoperiod", "18/6 (convention)", "18/6 until flip day",
       "Long days hold veg; cultivars can initiate flower at photoperiods up to ~14 h" + _c("moher2023-photoperiod")],
      ["CO2", "Ambient (~400-600 ppm) is fine", "700-800+ ppm pays only with high PPFD",
       "Photosynthesis rises with CO2 to at least ~750 ppm at high light" + _c("chandra2008-photo")],
    ], cls="compact", caption="Working bands for photoperiod cultivars in soilless media. "
       "Numbers without a citation are hedged convention; treat all of them as starting points "
       "to verify against your own canopy."),
    figure(L.zones("Veg air temperature: where growth actually runs", 16, 36,
            [(16, 20, L.AMBL, "slow"), (20, 25, L.GXL, "good"), (25, 30, L.GL, "optimum"),
             (30, 32, L.AMBL, "edge"), (32, 36, L.REDL, "stress")],
            unit="&deg;C",
            note="Leaf photosynthesis peaks ~25-30 &deg;C; hot rooms also stretch internodes and lengthen the frame you're trying to keep compact."), 8,
      "The veg temperature landscape" + _c("chandra2008-photo") + ". Cooler rooms aren't safer "
      "&mdash; they're just slower, and slow veg is paid for in days."),
    p("<strong>Light in veg steers shape, not just speed.</strong> In the 21-day trial above, "
      "higher PPFD made plants shorter, thicker-stemmed and shorter-internoded, roughly linearly; "
      "~600 &micro;mol produced a more open frame with better airflow, while ~900 &micro;mol "
      "produced the compact, robust transplants commercial rooms want &mdash; with no light-stress "
      "signs even at the top of the tested range" +
      _c("moher-2022-cannabis-vegetative-light-intensity-morphology") + ". Low-light veg (150-300 "
      "&micro;mol) is why home-grown plants arrive at flip lanky and floppy. Ramp intensity up "
      "over days, not in one jump &mdash; the ramp itself is covered in "
      "<a href='light-acclimation.html'>light acclimation</a>."),
    figure(L.bars("Veg PPFD by goal",
            [("Fresh transplant", 300), ("Open, airy frame", 600), ("Compact, robust", 900)],
            unit="", maxv=1000,
            note="&micro;mol/m&sup2;/s at canopy, 18 h photoperiod context; step up over several days per light acclimation."), 9,
      "Veg PPFD is a shape dial: more light, shorter internodes, thicker stems" +
      _c("moher-2022-cannabis-vegetative-light-intensity-morphology") + "."),
    callout("warn", "Guard the photoperiod edge",
      p("Modern cultivars are not all '12 hours or nothing': in a ten-cultivar trial, every one "
        "initiated flowering at photoperiods up to 14 h" + _c("moher2023-photoperiod") + ". A veg "
        "room drifting toward short days &mdash; a failing timer, a mis-set sunrise/sunset "
        "controller, a long power cut &mdash; can start flipping plants you meant to keep "
        "vegetative. Hold veg at 16-18 h and put the light schedule on your daily checks.")),
  ]})

# ---------------------------------------------------------------- 10 · nutrition
SECTIONS.append({"id": "nutrition", "kicker": "Feeding the build", "title": "Veg nutrition: N-forward, EC on a ramp",
  "blocks": [
    p("Veg tissue is protein and chlorophyll factory-work, and both are nitrogen-hungry &mdash; "
      "which is why every veg feed is 'N-forward' relative to bloom formulas. The dose-response "
      "work is unusually clean here: in fertigation trials on medical cannabis, vegetative growth "
      "peaked around <strong>160 mg/L N</strong>, with 30 mg/L plants visibly starved and "
      "320 mg/L plants going backwards" + _c("saloner-2020-cannabis-nitrogen-supply") + ". More "
      "nitrogen is not more growth; it's a curve with a top."),
    p("In drain-to-waste coco or rockwool, the practical control knob is feed EC, ramped with "
      "plant size (hedged conventions, verified against runoff EC and leaf colour):"),
    table(["Stage", "Feed EC (mS/cm)", "What you're doing"], [
      ["Fresh transplant, week 1", "~1.5-1.8", "Gentle start while roots explore the new volume"],
      ["Mid-veg", "~2.0-2.4", "Full N-forward feed; plant in full build mode"],
      ["Last week of veg &rarr; flip", "~2.4-3.0", "Carry EC up so the plant enters stretch with reserves"],
    ], cls="compact", caption="Hedged convention for drain-to-waste soilless systems, in line with "
       "manufacturer stone-wool guidance" + _c("grodan-growguide-steering") + " &mdash; exact "
       "numbers vary by product line and water. Watch trends in runoff EC: climbing hard means "
       "you're feeding stronger than the plant is drinking."),
    p("Two rules of thumb do most of the work. <strong>Colour before calendar:</strong> a veg "
      "plant should hold an even mid-green &mdash; pale, yellowing lower leaves mean the N supply "
      "is behind the build rate; near-black blue-green with clawed tips means it's ahead. "
      "<strong>Don't taper N before the flip:</strong> the stretch runs substantially on nitrogen "
      "mobilised from veg tissue, so a plant sent into 12/12 already pale will fade hard by week "
      "3 of flower, from the bottom up."),
    callout("warn", "Pale at flip is a veg mistake paid in flower",
      p("Week-3 lower-leaf yellowing gets blamed on bloom nutrients constantly. The cause is "
        "usually two weeks earlier: an under-fed, root-limited or light-crushed plant that "
        "entered stretch with no nitrogen reserve. Fix it in veg &mdash; by flip day it is "
        "largely pre-paid.")),
  ]})

# ---------------------------------------------------------------- 11 · root zone
SECTIONS.append({"id": "rootzone", "kicker": "Below the deck", "title": "Root-zone establishment before the flip",
  "blocks": [
    p("The fastest way to lose a week of veg is to drown a fresh transplant. A just-potted plant "
      "has a small root ball in a large, wet volume: keep that volume saturated and the roots "
      "have no reason to explore and no oxygen to do it with. Manufacturer stone-wool guidance "
      "for veg is small, frequent shots &mdash; on the order of ~3% of substrate volume &mdash; "
      "with a modest 5-15% runoff fraction, while avoiding hard drybacks (below roughly 25-30% "
      "water content in blocks) that stall young roots" + _c("grodan-growguide-steering") + ". "
      "The rhythm is: wet enough to live, dry enough that roots keep chasing the water down and "
      "out."),
    p("By flip day the root zone, not the calendar, is the report card. Three checks: roots "
      "visible at the container walls and drain holes (or slab face); a <em>predictable</em> "
      "overnight dryback &mdash; the pot measurably lighter or the sensor showing a repeatable "
      "morning dip; and irrigation demand trending up day over day. That established, exploring "
      "root system is what funds the stretch, when water and nutrient demand roughly doubles in "
      "three weeks. Flip before it exists and the stretch stalls; flip long after and you're "
      "root-bound (section above)."),
    figure(_FIGS["timeline"], 10,
      "An indicative 18-day clone-to-flip block for a topped plant in 10-11 L: root-in, top, "
      "recover, level, then a gate. SOG compresses the same shape to ~7-10 days; trees stretch it "
      "to 5-8 weeks. The gate decides the flip &mdash; the calendar just forecasts it."),
    steps([
      ("Roots at the walls", "White roots at the pot walls/drain holes or wrapping the block "
       "face; daily water demand trending up."),
      ("Height under the line", "Tallest top at or below max flip height (usable height &divide; "
       "stretch multiplier)."),
      ("Canopy level and full", "Tops within ~10 cm of each other; ~80-90% of each plant's canopy "
       "share filled; net on."),
      ("Cuts recovered", "Last topping &ge;10-14 days ago; leaders even; no fresh major wounds "
       "going into stretch" + _c("rqs-topping-guide") + "."),
      ("Fed and green", "No active deficiency; feed at late-veg EC; plant an even mid-green with "
       "N reserves for the stretch."),
    ]),
    callout("key", "The pre-flip gate",
      p("All five, or you don't flip &mdash; you fix the failing one first. A flip delayed two "
        "days to finish root-in costs you two days. A flip forced past a failing gate costs you "
        "the weak version of the entire flower cycle.")),
  ]})

# ---------------------------------------------------------------- 12 · economics
SECTIONS.append({"id": "economics", "kicker": "The business of days", "title": "Veg-length economics: turns versus plant count",
  "blocks": [
    p("Flower length is written in the genetics &mdash; call it 56-63 days and largely "
      "untouchable. Veg length is therefore <em>the</em> schedule lever you own, and it trades "
      "three currencies: " + chip("turns per year") + " " + chip("plants per gram") + " " +
      chip("risk per plant") + "."),
    figure(L.bars("Cycles per room per year vs veg length",
            [("10-day veg", 5.0), ("21-day veg", 4.3), ("35-day veg", 3.7)],
            unit="", maxv=6,
            note="Illustrative arithmetic: 365 / (veg + 56-day flower + 7-day turnaround). Your flower length moves every bar."), 11,
      "Longer veg costs turns: going from 10 to 35 days of veg in the same room drops roughly a "
      "full cycle per year. That cost buys bigger plants and fewer of them &mdash; whether that's "
      "a good trade depends on what caps you."),
    p("<strong>Where plant count is capped, veg length is leverage.</strong> If a licence "
      "condition, agreement or your own risk model limits how many plants you may run, yield per "
      "plant becomes the metric that matters &mdash; and per-plant yield scales with veg length "
      "and frame size" + _c("schober-2024-veg-duration-density") + ". Fewer, bigger plants also "
      "carry real operational discounts: fewer tags and records per gram in a track-and-trace "
      "regime, fewer transplants, fewer IPM scouting units, and lower plant-to-plant variability "
      "risk than a dense canopy" + _c("danziger-2022-planting-density") + ". The inverse holds "
      "where count is free and time is the constraint: short veg, high density, more turns" +
      _c("dang-2022-photoperiod-switch-meta") + "."),
    p("<strong>Veg length also has to fit your veg room.</strong> At steady state, a flower room "
      "flipping a new cohort every N weeks needs the veg area to hold each cohort for the full "
      "veg length. The longer the veg, the more cohorts stack up on the veg benches at once "
      "&mdash; long-veg strategies quietly demand a bigger veg room, more veg light, and more "
      "weeks of exposure to a veg-room pest outbreak. Cheap per m&sup2;, but not free."),
    kv([
      ("Flower block", "56-63 days &mdash; fixed by genetics, not negotiable"),
      ("Veg ~10 days", "&asymp;5 turns/yr &middot; most plants and tags &middot; least per-plant risk exposure"),
      ("Veg ~21 days", "&asymp;4.3 turns/yr &middot; the usual commercial balance"),
      ("Veg 35+ days", "&asymp;3.7 turns/yr &middot; fewest plants per gram &mdash; the count-capped play"),
    ]),
    callout("note", "Decide which currency you're paid in",
      p("Free plant count &rarr; sell time: short veg, high density, maximum turns. Capped plant "
        "count &rarr; sell frame: long veg, big pots, trees. The worst position is the "
        "unexamined middle &mdash; medium plants, medium density, chosen by habit, optimising "
        "nothing.")),
  ]})

# ---------------------------------------------------------------- 13 · mistakes
SECTIONS.append({"id": "mistakes", "kicker": "Where veg goes wrong", "title": "The six classic veg mistakes",
  "blocks": [
    p("Every one of these is cheap to prevent in veg and expensive to discover in flower. Most "
      "rooms that struggle in week 3 of flower committed one of them a month earlier."),
    grid([
      card("Flipping root-bound",
        p("Pot dries out by lunchtime, roots circling the walls, growth stalled &mdash; and it "
          "gets flipped anyway. Stretch demand lands on a root system that can't fund it: "
          "wilting, early fade, airy bud. <strong>Fix:</strong> match pot to planned veg days; "
          "if in doubt, pot up and add a week <em>before</em> flip."), tag="root zone"),
      card("Flipping too tall",
        p("Stretch outruns the ceiling; tops grow into the fixture, bleach and cook, and dimming "
          "to save them starves the rest of the room. <strong>Fix:</strong> max flip height = "
          "usable height &divide; stretch multiplier &mdash; enforced on flip day, no "
          "exceptions."), tag="height"),
      card("Uneven canopy at flip",
        p("One tall cultivar or a few over-vegged plants pin the light high while the rest "
          "under-run for nine weeks. <strong>Fix:</strong> level in veg &mdash; graded clones, "
          "tall plants tied down and benched to the edges, runts culled, net on at flip."),
        tag="uniformity"),
      card("Topping too late",
        p("A cut ten days before flip means flipping mid-recovery: uneven leaders that the "
          "stretch amplifies into a lopsided canopy. <strong>Fix:</strong> last major cut 10-14 "
          "days before flip, on the calendar the day you top."), tag="timing"),
      card("Drowning fresh transplants",
        p("Big new pot kept saturated 'to help it settle in': oxygen-starved roots, no "
          "exploration, fungus gnats, a stalled week. <strong>Fix:</strong> small frequent "
          "shots, modest runoff, let the roots chase moisture into the new volume."),
        tag="irrigation"),
      card("Veg with no target",
        p("'One more week' by vibes, no canopy spec, no gate. Every unplanned week is a lost "
          "fraction of a turn &mdash; the most expensive habit in the room. <strong>Fix:</strong> "
          "write count &times; share &times; max height before transplant; flip on the gate."),
        tag="planning"),
    ], cols=2),
  ]})

# ---------------------------------------------------------------- 14 · troubleshooting
SECTIONS.append({"id": "troubleshooting", "kicker": "Read and fix", "title": "Troubleshooting veg, and the model to keep",
  "blocks": [
    p("Veg problems telegraph themselves early if you read the plant against the plan. The "
      "common ones:"),
    table(["Symptom", "Likely cause", "What to do"], [
      ["Transplant sits still for a week+", "Over-wet root-in; roots not exploring",
       "Cut shot sizes, let the volume breathe between shots; check drainage" + _c("grodan-growguide-steering")],
      ["Long internodes, floppy stems", "PPFD too low for the frame you want",
       "Raise veg light in steps toward ~600-900 &micro;mol" + _c("moher-2022-cannabis-vegetative-light-intensity-morphology") +
       "; add airflow for stem strength"],
      ["Even pale green, lower leaves first", "Nitrogen supply behind growth rate",
       "Lift feed EC / N toward the veg optimum" + _c("saloner-2020-cannabis-nitrogen-supply") + "; recheck in 4-5 days"],
      ["Dark blue-green, clawed tips", "Nitrogen ahead of growth rate",
       "Ease feed EC back; hold N-forward ratio but lower the dose"],
      ["Pistils/flowers forming in the veg room", "Photoperiod fault &mdash; timer, controller or light leak into a &le;14 h day",
       "Audit the schedule and door discipline" + _c("moher2023-photoperiod") + "; single calyxes at nodes (preflowers) are normal maturity, full flowering is not"],
      ["One plant towers over the cohort", "Cultivar mix under one light, or clone-age spread",
       "Tie it down and bench it to the edge now; next run, cohort by cultivar and rooting date"],
      ["Pot needs water 3&times; a day", "Root-bound &mdash; the container clock ran out",
       "Pot up and give it a week, or flip today if all other gates pass; never 'push through' a root-bound stretch" + _c("poorter-2012-pot-size")],
    ], cls="compact", caption="Read symptoms against the plan (target frame, target days), not in "
       "isolation &mdash; the same yellow leaf means different things at day 5 and day 25 of veg."),
    callout("key", "The mental model to keep",
      p("<strong>Veg is a countdown to a canopy spec, not a waiting room.</strong> The spec is "
        "written before transplant: N plants &times; each filling its share of the canopy &times; "
        "at or under max flip height, level, rooted to the walls, green. Every veg day either "
        "moves the room toward that spec or it's rent. When the spec is met, flip &mdash; that "
        "day, not Saturday.")),
    p("From here: the cutting-and-bending toolkit lives in "
      "<a href='defoliation-training.html'>defoliation &amp; training</a>, and the safe way to "
      "carry PPFD from clone light to a 900-&micro;mol veg canopy is in "
      "<a href='light-acclimation.html'>light acclimation</a>."),
  ]})
