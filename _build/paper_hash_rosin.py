# -*- coding: utf-8 -*-
"""Paper: hash rosin pressing — heat, pressure, time and the micron screen (beginner-first)."""
import json, os
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        grid, card, chip, kv, steps)

_FIGS = json.load(open(os.path.join(os.path.dirname(__file__), "figs_hash_rosin.json"), encoding="utf-8"))

SLUG = "hash-rosin-pressing"
TITLE = "Hash rosin, pressed: a solventless systems guide"
EYEBROW = "Harvest · Solventless"
SUB = ("Rosin is mechanical, not chemical: heat, pressure, time and a micron screen acting on a "
       "material whose quality ceiling was already fixed upstream, at harvest, in the wash, in the "
       "dry. This guide maps the whole chain, trichome to dab.")
META = [("flask", "Solventless"), ("image", "8 diagrams"),
        ("quote", "Evidence-linked · 16 sources"), ("clock", "~22 min read")]
RELATED = ["gmp-hash-lab", "harvest-dry-trim-cure"]
REF_IDS = ["pressclub-temp", "pressclub-pressure", "pressclub-thca", "pressclub-static",
           "lowtemp-diamonds", "lowtemp-carts", "triminator-tempchart", "triminator-coldcure",
           "triminator-carts", "hightimes-bubbleman", "hashtek-thca-tek", "hashtek-jam-tek",
           "hashtek-decarb", "resinator-bubblepress", "wang2016-decarb", "eyal2023-terpenes"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

SECTIONS.append({"id": "start-here", "kicker": "Start here", "title": "Purpose and scope",
  "blocks": [
    lead("A cannabis plant is covered in thousands of tiny, mushroom-shaped glands called "
         "<strong>trichomes</strong>, the frosty &lsquo;crystals&rsquo; you can see on good flower. Each "
         "trichome head is a microscopic sac of <strong>resin</strong>: the sticky oil that carries almost "
         "all of the plant's potency, smell and flavour. Every solventless concentrate is really just "
         "<em>those heads, collected and then gently squeezed</em>, with no chemical solvents like butane "
         "or alcohol anywhere in the process."),
    figure(_FIGS["trichome"], 1,
      "The frosty &lsquo;crystals&rsquo; on cannabis are trichomes. Solventless hash-making is the art of "
      "collecting these heads and squeezing the resin out of them."),
    p("It happens in two halves:"),
    ol(["<strong>Make the hash.</strong> Knock the trichome heads off the plant and gather them into a "
        "powder or paste. Two common ways: stir the plant in <em>ice water</em> so the brittle heads snap "
        "off and sink (<strong>bubble hash</strong>), or rub dried plant over fine <em>screens</em> "
        "(<strong>dry sift</strong>).",
        "<strong>Press the hash into rosin.</strong> Seal the hash in a small mesh bag and squeeze it "
        "between two gently heated metal plates. Heat softens the resin; pressure pushes it out through "
        "the mesh as a golden oil. That oil is <strong>rosin</strong>."]),
    p("That is the whole idea, <strong>heat + pressure, no solvents</strong>. The craft is in restraint: "
      "too much heat boils away the flavour, and too much force bursts the bag and pushes plant matter "
      "through the mesh. After pressing, the rosin is <strong>cured</strong> (rested under controlled "
      "warmth or cold) to set its final texture, then either <strong>dabbed</strong> (a small dose "
      "flash-vaporised on a hot surface and inhaled) or loaded into a vape cartridge."),
    figure(_FIGS["press"], 2,
      "Two gently heated plates squeeze the bag. Heat thins the resin; pressure pushes it through the "
      "mesh as golden rosin, leaving plant matter trapped inside."),
    defterm("Trichome", "The tiny resin gland on the plant, the visible &lsquo;crystal&rsquo;. Its head "
            "holds the oil you want."),
    defterm("Hash", "Trichome heads gathered into a powder or paste, before pressing."),
    defterm("Rosin", "The oil pressed out of hash (or flower) using only heat and pressure."),
    defterm("Solventless", "Made with only force, heat, water and ice, never butane, CO&#8322; or "
            "alcohol. That's the appeal."),
    defterm("Micron (µm)", "One-thousandth of a millimetre; the mesh size of the press bag. Smaller "
            "number = finer mesh = cleaner rosin but lower yield."),
    defterm("Cure", "Resting fresh rosin at a set temperature for hours to weeks to fix its texture "
            "and flavour."),
    callout("key", "The one big idea of the whole guide",
      p("The press cannot <em>add</em> quality. It can only lose less of it. Your starting material "
        "(the genetics, the harvest, the wash) sets the ceiling. Heat, pressure, time and mesh size only "
        "decide how close to that ceiling you land.")),
    p("From here on, the guide treats the press as a set of <strong>levers</strong> you can pull, "
      "temperature, pressure, time and mesh (&lsquo;micron&rsquo;) size. And shows what each one does to "
      "yield and quality, what goes wrong, and how to fix it. Hit a word you don't know? Jump to the "
      "glossary at the end."),
  ]})

SECTIONS.append({"id": "glossary", "kicker": "The words", "title": "Definitions",
  "blocks": [
    p("Plain-English definitions for the terms this guide leans on. Skim it once and the technical "
      "sections read easily."),
    table(["Term", "Meaning"], [
      ["Amber trichome", "A resin head aged past its peak, turned amber. A little adds a heavier body effect; too much means lost potency."],
      ["Badder / batter", "A creamy, whipped rosin texture, like frosting. Set by curing and stirring."],
      ["Blowout", "The mesh bag bursting under pressure so raw plant matter floods the oil, ruining the batch."],
      ["Bubble hash", "Hash made by stirring cannabis in ice water so the brittle trichome heads snap off and sink through mesh bags."],
      ["Capitate-stalked trichome", "The large, lollipop-shaped gland that holds the most resin, the prize fraction."],
      ["Chromatography (reabsorption)", "Oil that already flowed out soaking back into the spent material because flow stalled; shows up as poor yield."],
      ["Cloudy / milky trichome", "A head at peak ripeness (peak THCa and terpenes); the target window at harvest."],
      ["Cold chain", "The steps that must stay cold (harvest, wash, dry, collection, storage) because heat degrades quality there."],
      ["Cold cure", "Resting sealed rosin cool (about 10–21 °C) for days to weeks to set a creamy badder."],
      ["Decarb (decarboxylation)", "Heating to convert raw THCa into active THC; required for vape carts, but it destroys diamond potential."],
      ["Diamonds (THCa diamonds)", "Clear crystals of nearly pure THCa grown from rosin, sitting in a pool of &lsquo;sauce&rsquo;."],
      ["Dry sift (kief)", "Hash made by rubbing dried plant over fine screens so trichome heads fall through; the powder is kief."],
      ["Dwell time", "How long the bag is held squeezed under heat during a press."],
      ["Effective pressure (PSI)", "The force actually felt by the bag (force ÷ bag area). What matters, not the raw gauge number."],
      ["Emulsion", "A hazy, unstable blend caused by water trapped in the oil; the rosin looks cloudy."],
      ["Freeze-dryer (lyophiliser)", "A machine that pulls water out under vacuum while frozen, drying hash with no heat. The quality option."],
      ["Fresh-frozen", "Plant flash-frozen right after cutting and never dried, preserving the &lsquo;live&rsquo; aroma; the basis of live rosin."],
      ["Full-melt", "Top-grade hash (5–6 star) pure enough to melt to almost nothing on a hot nail; the cleanest press input."],
      ["Hash hole", "A pre-rolled joint with a core of hash or rosin running down the middle."],
      ["Lipids / waxes", "Natural plant fats that can cloud rosin; flower carries more of them than hash."],
      ["Live rosin", "Rosin pressed from fresh-frozen hash; prized for the most vivid aroma and flavour."],
      ["Melt / star grade (1–6★)", "A quality scale for hash by how cleanly it melts; 6-star is full-melt, 1–2 star is edible-only."],
      ["Monoterpenes", "The lightest, most volatile terpenes (such as pinene and myrcene); the first aromas lost to heat."],
      ["Nucleation", "The moment rosin begins to crystallise or &lsquo;butter up&rsquo;; triggered by cold, time, or stirring."],
      ["PID", "A precise temperature controller that holds the press plates steady at the set temperature."],
      ["Pre-press", "Forming the material into a dense, air-free puck before pressing, to stop channels and blowouts."],
      ["Puck", "The flattened, spent material left inside the bag after pressing."],
      ["Sauce", "The liquid, terpene-rich oil surrounding THCa diamonds (high-terpene solventless hash oil)."],
      ["Static glove tek", "A cleaning trick where a static-charged glove lifts pure trichome heads off a screen, leaving debris behind."],
      ["THCa / THC", "THCa is the raw, non-intoxicating acid in fresh material; heat turns it into active THC. Only THCa forms diamonds."],
      ["Viscosity", "How thick or runny the oil is; heat lowers viscosity so rosin flows."],
      ["Water activity (a<sub>w</sub>)", "A precise measure of free moisture (0–1) used to judge when flower is properly dried (optimal 0.58–0.62)."],
      ["Yield", "How much rosin you get back, usually given as a percentage of the hash weight pressed."],
    ], cls="compact"),
    p("Setpoints, micron guidance and the trichome-to-press logic in this guide are drawn from the "
      "author's solventless knowledge base and operational SOPs, cross-checked against the cited "
      "sources. It is a field guide, not a substitute for testing your own material, verify by "
      "logging your runs."),
  ]})

SECTIONS.append({"id": "core-answer", "kicker": "The short version", "title": "Core press principles",
  "blocks": [
    p("A rosin press has only four levers (<strong>heat, pressure, time and screen (micron)</strong>) "
      "and they all negotiate a single tension: <em>yield versus quality</em> (terpene retention, colour, "
      "clarity)" + _c("pressclub-temp") + ". Heat lowers resin viscosity so it flows; the micron bag "
      "decides what flows <em>with</em> it (pure trichome oil, or fats and plant matter too); pressure and "
      "time only push the process along" + _c("pressclub-pressure") + ". None of them can lift the "
      "ceiling set upstream."),
    callout("key", "Quality in, quality out",
      p("You cannot press 6-star rosin from 3-star input. The wash, the dry and the grade fix the "
        "maximum; the press and the cure only preserve or squander it. Hash presses <em>cooler</em> than "
        "flower, and clean full-melt hash blows out if you rush the pressure.")),
    p("So the whole craft reduces to: fix the input, pick the product, choose a micron that matches the "
      "trichome heads, set the lowest temperature that still flows, ramp pressure only to finish the "
      "flow, collect cold, and cure for texture."),
  ]})

SECTIONS.append({"id": "pipeline", "kicker": "The map", "title": "Rosin production workflow",
  "blocks": [
    p("Hash rosin is the back half of a longer chain. Cold-chain steps (where heat is the enemy) are "
      "marked in blue in the map below; the press and the cure are where heat becomes a tool."),
    figure(_FIGS["pipeline"], 3,
      "Eleven stages from living plant to finished concentrate. Blue marks the cold-chain steps where "
      "heat is the enemy; amber marks the heat steps, the press and the cure. Follow the arrows."),
    steps([
      ("Harvest", "Cut at 80–90% cloudy trichomes, at lights-off."),
      ("Freeze or dry", "Fresh-freeze for live products; slow-dry for dry sift."),
      ("Wash or sift", "Ice-water hash or dry-sift screens, cold room, gentle hands."),
      ("Dry the hash", "Freeze-dry, or cold air-dry as the budget option."),
      ("Grade", "Melt-test and star-grade 1–6★; the grade decides the product options."),
      ("Condition", "Moisture check and pre-chill; pre-press pucks for flower and sift only."),
      ("Press", "Preheat, slow ramp, hold to flow-stop."),
      ("Collect", "Cold tool, fresh parchment, straight into chilled glass."),
      ("Pick the product path", "Badder, sauce, diamonds, cart oil or hash-hole core."),
      ("Cure", "Cold-cure, warm-cure or a staged crystallisation."),
      ("Store", "Sealed glass, cold, dark."),
    ]),
    p("The stage deep-dives later in this paper break each step down with its own parameters. The "
      "matrices and failure modes tell you which lever to move when a stage goes wrong."),
  ]})

SECTIONS.append({"id": "setpoints", "kicker": "Numbers to start from", "title": "Starting setpoints by input material",
  "blocks": [
    p("Where to begin for each of the four input materials. These are <em>starting points</em> to dial "
      "in from, not targets to chase" + _c("triminator-tempchart") + ". Temperatures are platen "
      "temperature; press <em>to flow</em>, not to the clock. Hash sits cooler than flower because its "
      "trichome heads are already isolated and need only enough heat to melt resin" + _c("pressclub-temp") + "."),
    table(["Input material", "Bag micron", "Plate temp", "Band (°C)", "Dwell (s)", "Pressure approach", "Pre-press", "Typical products"], [
      ["Dried flower", "90 µm (75–160)", "88 °C", "82–93", "90–180",
       "Low–medium; slow 30–60 s ramp as resin flows, then ease to firm contact", "Yes",
       "Badder, fresh press; carts at 75 µm"],
      ["Dry sift / kief", "72 µm (25–90 by grade)", "82 °C", "71–88", "60–90",
       "Low; add <em>time</em>, not pressure. Finer material already has good contact", "Yes",
       "Badder, diamonds"],
      ["Fresh-frozen hash (5–6★)", "36 µm (25–45)", "71 °C", "60–77", "60–180",
       "Very low; add heat only if flow stalls. <strong>More pressure is NOT better</strong>. It pushes fats through", "Cold puck only",
       "Live rosin, cold-cure badder, live diamonds, carts, hash holes"],
      ["Dried / cured bubble hash", "45 µm (25–90 by grade)", "77 °C", "71–82", "60–120",
       "Low; a few °C hotter than full-melt to coax flow, but stay gentle", "Cold puck only",
       "Badder, diamonds, carts"],
    ], cls="compact", caption="Starting setpoints by material. Dial in from here, one lever per run."),
    callout("note", "Temperature bands at a glance",
      p("<strong>Cold-cure hold (post-press, not platen):</strong> 10–21 °C for days to ~2 weeks, sets "
        "creamy badder while keeping volatile terpenes" + _c("triminator-coldcure") + ". "
        "<strong>Low-temp press (flavour):</strong> 60–85 °C, max terpene retention, lightest colour; "
        "hash ~60–77 °C, premium flower ~82–88 °C. "
        "<strong>Balanced sweet spot (flower):</strong> 88–99 °C, strong yield, minimal terpene loss; a "
        "good default for unknown <em>flower</em>. "
        "<strong>High-temp press (yield / sauce / carts):</strong> 99–104 °C, max yield, fastest flow, "
        "darker; use it to rescue degraded material" + _c("triminator-tempchart") + ".")),
    figure(_FIGS["tempmap"], 4,
      "Where each input material and goal sits on the platen-temperature scale. Hash presses coolest; "
      "flower needs more heat; the hottest end trades flavour for yield."),
  ]})

SECTIONS.append({"id": "known-unknown", "kicker": "Honesty first", "title": "Evidence, assumptions and unknowns",
  "blocks": [
    h(3, "Knowns (settled)"),
    ul(["Lower platen temperature preserves terpenes and colour; higher temperature buys yield and flow "
        "at their expense" + _c("pressclub-temp") + ".",
        "A tighter (smaller-micron) bag yields <em>cleaner, lighter</em> rosin at <em>lower</em> yield; a "
        "coarser bag does the reverse.",
        "Hash and dry sift press cooler than flower. Their heads are already separated from plant matter.",
        "Sealed heat preserves terpenes better than open-air heat: a sealed headspace saturates so net "
        "evaporation stops, while open air oxidises and strips them" + _c("hashtek-decarb") + ". The "
        "lightest monoterpenes are the most volatile and go first" + _c("eyal2023-terpenes") + ".",
        "Only <strong>THCa</strong> crystallises into diamonds; once decarboxylated to THC it stays "
        "liquid" + _c("lowtemp-diamonds") + ". Carts need full decarb, diamonds need preserved THCa."]),
    h(3, "Assumptions this guide makes"),
    ul(["Your hash is well-made and <em>properly dried</em> (freeze-dried or correctly cold-dried) before "
        "it reaches the plates.",
        "Your press holds temperature accurately (PID or app-controlled) and applies even heat across "
        "both plates.",
        "You work clean and cold, and you log runs so you can move one lever at a time."]),
    h(3, "Unknowns that change the exact numbers"),
    ul(["<strong>Trichome head size &amp; distribution</strong>, cultivar-dependent; dictates the micron "
        "more than anything else.",
        "<strong>Lipid / wax load</strong>, varies by genetics and material type; flower carries more "
        "than hash.",
        "<strong>Crystallisation tendency</strong>, the terpene-to-THCa ratio decides how readily (or "
        "stubbornly) diamonds form.",
        "<strong>Exact moisture</strong>, a few points of RH swing flow, clarity and blowout risk."]),
  ]})

SECTIONS.append({"id": "balances", "kicker": "Core concept", "title": "Four coupled press balances",
  "blocks": [
    p("Like a grow room, a press is best read as a few coupled balances rather than independent knobs. "
      "Move one and the others shift."),
    grid([
      card("B-01 · Heat", "Platen heat versus the thermal mass of the bag. Enough heat melts resin and "
           "drops its viscosity so it flows; too much volatilises terpenes and darkens colour. "
           "<strong>Flow ↔ Flavour.</strong>"),
      card("B-02 · Pressure &amp; flow", "Applied force versus the bag's resistance and the resin's flow "
           "rate. Force should follow the oil, not lead it, excess force ruptures the bag and drives "
           "contaminants through the screen. <strong>Drive ↔ Blowout.</strong>"),
      card("B-03 · Moisture", "Water in the input versus flow and stability. A little aids flow; too much "
           "causes emulsion, haze and instability, and raises blowout risk. Properly dried hash is the "
           "baseline. <strong>Flow ↔ Haze.</strong>"),
      card("B-04 · Purity (screen)", "Screen selectivity: oil passing through versus contaminants held "
           "back. The micron is the gate. Tighter holds more back (cleaner, less yield), coarser lets "
           "more through. <strong>Yield ↔ Clarity.</strong>"),
    ], cols=2),
    callout("key", "The master tension",
      p("All four balances feed one trade: <strong>yield ↔ quality</strong>. Almost every adjustment "
        "trades one for the other. Decide which you are optimising <em>before</em> you touch a lever.")),
    figure(_FIGS["tradeoff"], 5,
      "Push the temperature up and yield climbs, but terpenes and clarity fall. Where the lines cross "
      "is a judgement call: cool for flavour, hot for volume."),
  ]})

SECTIONS.append({"id": "levers", "kicker": "The controls", "title": "Press control variables",
  "blocks": [
    p("The full set of controls, grouped by where they sit in the chain. Upstream levers cap the "
      "ceiling; press levers set the trade; finishing levers set the texture."),
    h(3, "Upstream / material levers"),
    table(["Lever", "What it controls", "Direction of effect"], [
      ["Trichome maturity", "Potency &amp; terpene profile at harvest",
       "Cloudy = peak; clear = immature / low yield; amber = degrading"],
      ["Fresh-frozen vs cured", "&lsquo;Live&rsquo; terpene profile vs stability",
       "Fresh-frozen = highest monoterpenes, presses coolest; cured = a touch warmer to flow"],
      ["Wash / sift quality &amp; melt grade", "Head purity (the star rating)",
       "Higher grade → cleaner melt, higher yield, can press cooler &amp; tighter"],
      ["Micron fraction collected", "Which head sizes you kept (73–120 µm = gold)",
       "Full-melt fractions press cleanest; off-fractions add colour and contaminant"],
      ["Moisture / RH", "Water content of the input",
       "Too dry = poor flow and yield; too wet = haze, emulsion, blowout"],
      ["Cultivar", "Head size, lipid load, crystallisation tendency",
       "Sets the micron, the blowout risk and how readily diamonds form"],
    ], cls="compact"),
    h(3, "Press levers"),
    table(["Lever", "What it controls", "Direction of effect"], [
      ["Plate temperature", "Resin viscosity / flow", "↑ yield and flow; ↓ terpenes and lightness"],
      ["Applied force / effective PSI", "Drive through the screen",
       "↑ yield to a point, then ⚠ blowout &amp; contaminant pass-through" ],
      ["Dwell time", "How long under heat + force", "↑ yield; ↓ terpenes with prolonged heat"],
      ["Ramp profile", "How fast you reach target force",
       "Slow ramp = fewer blowouts, cleaner flow; fast ramp = rupture risk"],
      ["Micron bag", "Screen selectivity (the gate)", "Tighter ↑ purity, ↓ yield; coarser the reverse"],
      ["Fill / loading density", "Flow path &amp; pressure distribution",
       "Even, air-free fill → even flow, fewer channels and blowouts"],
      ["Pre-press", "Forms a dense, air-free puck",
       "Reduces channeling and blowouts (flower / sift); skip for full-melt hash"],
      ["Plate size vs load", "Heat coverage &amp; throughput",
       "Match to batch, overfilling cold edges chokes flow"],
    ], cls="compact"),
    h(3, "Finishing levers"),
    table(["Lever", "What it controls", "Direction of effect"], [
      ["Collection temperature", "Texture lock at the parchment",
       "Cold collection preserves terpenes and sets cleaner textures"],
      ["Cure type / temp / time", "Final consistency",
       "Cold cure → badder; warm cure → sauce; staged → diamonds"],
      ["Agitation / whip", "Homogenisation &amp; nucleation",
       "Whipping drives budder; over-whipping warms the mass and dulls terps"],
      ["Nucleation trigger", "Whether / when it crystallises",
       "Cold cure or gentle heat + stirring starts nucleation"],
      ["Decarb", "THCa → THC for carts", "Required for carts; destroys diamond potential"],
      ["Storage", "Shelf preservation", "Cold, dark, airtight = terpene and cannabinoid retention"],
    ], cls="compact"),
  ]})

SECTIONS.append({"id": "interaction", "kicker": "Cause and effect", "title": "Press-control interaction matrix",
  "blocks": [
    p("What happens to each outcome when you turn a press lever <em>up</em> (or, for micron, "
      "<em>tighter</em>). Direction of effect, all else held equal. ↑ = increases / improves, "
      "↓ = decreases / darkens, → = little change, ⚠ = raises risk."),
    table(["Lever moved →", "Yield", "Terpene retention", "Colour (lighter)", "Clarity", "Blowout risk", "Texture shift"], [
      ["↑ Plate temp", "↑", "↓", "↓", "↑ (thinner oil runs cleaner)", "↓", "toward sap / shatter"],
      ["↑ Pressure / force", "↑ to a point", "→", "↓ if forced", "↓ (pushes fats &amp; fines)", "⚠ ↑↑", "wetter / contaminated"],
      ["↑ Dwell time", "↑", "↓", "↓", "→", "→", "more decarb / sappier"],
      ["↓ Micron (tighter bag)", "↓", "→", "↑", "↑↑", "⚠ ↑ (more restriction)", "cleaner, stiffer"],
      ["↑ Moisture (wetter input)", "↑ then ↓", "→", "→", "↓↓ (haze / emulsion)", "⚠ ↑", "unstable / greasy"],
      ["↑ Pre-press density", "↑", "→", "→", "↑", "↓↓ safer", "even flow"],
    ], cls="compact", caption="Direction of effect for each press lever, all else held equal."),
    p("The pattern to internalise: <strong>temperature and micron are your quality levers; pressure and "
      "time are your finishing levers.</strong> Reach for heat and screen first; use force only to "
      "complete a flow that heat has already started" + _c("pressclub-pressure") + "."),
  ]})

SECTIONS.append({"id": "symptoms", "kicker": "Read the result", "title": "Symptom-to-parameter matrix",
  "blocks": [
    p("Read a result, find the lever that moved too far, make the one corrective change. Adjust a "
      "single lever per run so the next result is interpretable."),
    table(["You observe", "Lever that moved too far", "Corrective change"], [
      ["Low yield, oil won't flow / reabsorbs", "Temp too low · material too dry · pressure too low · screen too tight",
       "+3–6 °C; check moisture; firmer, slower ramp; open the micron one step"],
      ["Dark or green rosin", "Too hot · over-pressed · contaminated input",
       "Drop temp; gentler ramp; tighten micron; start from a cleaner grade"],
      ["Hazy, cloudy or &lsquo;wet&rsquo; rosin", "Excess moisture / lipids",
       "Dry &amp; condition the input; cooler press; tighter bag"],
      ["Flat, weak nose", "Temp too high · dwell too long · hot collection",
       "Cold-press band; shorten dwell; collect cold; seal immediately"],
      ["Bag blowout", "Pressure too fast · overfilled · micron too coarse for the heads · no support sleeve",
       "Slow 15–20 s ramp; 120–160 µm outer sleeve; smaller load; match micron to head size"],
      ["Stays sappy, won't butter", "Not nucleated", "Cold-cure sealed jar 13–16 °C, 24–72 h"],
      ["Auto-budders fast / greasy", "Residual moisture in the input", "Dry the hash more thoroughly before pressing"],
    ], cls="compact"),
  ]})

SECTIONS.append({"id": "worked-example", "kicker": "One change, traced", "title": "Worked example: raising plate temperature by 6 °C",
  "blocks": [
    p("A single nudge cascades. Take full-melt fresh-frozen hash and raise the platen from "
      "<strong>71 °C → 77 °C</strong>, holding everything else constant."),
    h(3, "Lever pulled"),
    p("Plate temperature +6 °C, still inside the hash band (60–77 °C), 36 µm bag, gentle ramp."),
    h(3, "Immediate effects"),
    ul(["Resin viscosity drops, the seam wets sooner and oil runs faster.",
        "Yield rises; less oil is left trapped in the puck.",
        "Blowout risk falls slightly, thinner oil escapes before pressure has to build."]),
    h(3, "Secondary effects"),
    table(["Knock-on", "Direction", "Why"], [
      ["Terpene retention", "↓", "Volatile monoterpenes (&alpha;-pinene, myrcene) start leaving as "
       "temperature climbs" + _c("eyal2023-terpenes")],
      ["Colour", "↓ darker", "More thermal exposure deepens amber"],
      ["Texture", "budder → sap", "Hotter rosin sets saucier; slower to butter"],
      ["Cure behaviour", "slower nucleation", "Higher temp keeps more in solution; a cold cure takes longer"],
    ], cls="compact"),
    callout("warn", "When to take the +6 °C",
      p("Rescuing lower-grade or cured hash that won't give up its oil; pushing for sauce, diamonds or "
        "cart feedstock where a little terpene trade is acceptable for flow and yield.")),
    callout("note", "When not to",
      p("Pressing 5–6★ fresh-frozen for a terpene-forward live badder. Here those six degrees trade "
        "your nose for a few points of yield, a bad deal. Stay at 71 °C and accept the lower number.")),
  ]})

SECTIONS.append({"id": "stages", "kicker": "Step by step", "title": "Process stage deep dives",
  "blocks": [
    p("The full farm-to-dab chain, stage by stage, with the parameters that matter at each. Everything "
      "before the press is a cold-chain step where heat is the enemy."),
    h(3, "Harvest &amp; trichome maturity"),
    p("Everything downstream is capped here. The common practice target is <strong>80–90% milky / "
      "cloudy</strong> capitate-stalked trichomes with <strong>10–20% amber</strong> and zero clear, a "
      "preference band, not a hard rule, and hash-makers often run <em>less</em> amber because amber "
      "heads press darker and greasier. Harvesting at lights-off is common practice rather than settled "
      "science. For dry sift, lean slightly earlier, overripe stalks turn brittle and fragment into "
      "contamination" + _c("hightimes-bubbleman") + "."),
    h(3, "Fresh-freeze vs dry / cure"),
    ul(["<strong>Fresh-frozen (for live / ice-water hash):</strong> flash-freeze whole, undried material "
        "immediately after cutting. It locks in the living monoterpene profile; this is what presses "
        "coolest and cleanest.",
        "<strong>Slow dry (for dry sift):</strong> whole-plant hang at <strong>15–18 °C, 55–60% RH</strong>, "
        "complete darkness, gentle airflow, <strong>10–14 days</strong>. Target stems that snap (not "
        "bend), water activity <strong>0.58–0.62 a<sub>w</sub></strong> (0.55–0.65 is the safe band; at "
        "0.55 you are already at the overdried boundary). Then freeze the trimmed material "
        "4–6 h (ideally 24 h) so the stalks snap cleanly" + _c("hightimes-bubbleman") + "."]),
    h(3, "Ice-water wash (cold chain)"),
    p("For bubble hash, agitate fresh-frozen material in near-freezing water so trichome heads break "
      "free and sink through a micron bag stack" + _c("resinator-bubblepress") + "."),
    table(["Parameter", "Target", "Note"], [
      ["Water temperature", "≤ 4 °C", "Add ice; RO / distilled water keeps it clean. Cold keeps heads intact and brittle"],
      ["Work bag", "220 µm", "Holds plant material; heads pass through into the stack below"],
      ["Collection stack", "160 · 120 · 90 · 73 · 45 · 25 µm",
       "Full-melt heads live in <strong>73–119 µm</strong> (sweet spot 73–90 µm); 120–160 µm is mid-grade; &lt;45 µm is fine-grade"],
      ["Agitation", "Gentle, 1–5 min per wash", "Hand-stir or low-speed machine; gentler = cleaner heads"],
      ["Cycles", "2–4 washes", "The first wash is gentlest and highest quality; later washes give more, dirtier yield"],
    ], cls="compact"),
    h(3, "Dry-sift alternative (cold chain)"),
    p("No water, work frozen material across a descending screen cascade in a cold room (below "
      "10 °C), carding gently 3–5 min per pass" + _c("hightimes-bubbleman") + "."),
    ul(["<strong>Screen stack:</strong> 140 µm (110 LPI) work screen → 107 µm → <strong>70 µm (200 LPI) "
        "&lsquo;money&rsquo; screen</strong> (70–120 µm heads are the gold) → sub-70 µm catch (edible grade).",
        "<strong>Static glove tek:</strong> on a 70 µm (200 LPI) screen, sweep a freezer-chilled black "
        "nitrile glove in smooth circles. Static lifts pure heads and leaves contaminants behind. Whisk "
        "off, re-chill, repeat 3–5 passes. Hover and sweep; never mash" + _c("pressclub-static") + "."]),
    h(3, "Drying the hash (cold chain)"),
    ul(["<strong>Freeze-dry (lyophilise), best:</strong> condenser −40 to −50 °C, vacuum ~100–200 mTorr "
        "(below ~500 workable), 24–48 h until fully dry. Removes water without heat or oxidation.",
        "<strong>Cold air-dry, budget:</strong> microplane the patties onto parchment or screens and dry "
        "in a cold room over 24–72 h. More oxidation and contamination risk; watch for mould."]),
    h(3, "Grading &amp; moisture conditioning"),
    p("Melt-test on a hot nail and grade <strong>1–6 star</strong> (6★ = 95%+ heads, full melt). The "
      "grade sets which products are open to you and how tight and cool you can press. Pre-chill the "
      "hash and the bag before pressing, cold material in the bag means fewer blowouts."),
    table(["Grade", "Purity", "Use"], [
      ["6★ full melt", "95%+ heads", "Dab direct; premium rosin; cart grade"],
      ["5★ near full melt", "85–95%", "Excellent rosin; cart grade with good pressing"],
      ["4★ half melt", "70–85%", "Good rosin; may need more cleaning for carts"],
      ["3★", "50–70%", "Cooking grade, or needs cleaning"],
      ["1–2★", "&lt;50%", "Edibles only, too contaminated for rosin"],
    ], cls="compact"),
    callout("note", "Do you even press 6★?",
      p("Worth knowing: many hash-makers treat <strong>3–4★ as the classic pressing grade</strong> and "
        "keep true 5–6★ full-melt to dab as-is" + _c("pressclub-temp") + ". It already melts clean "
        "without a press. Pressing full-melt into rosin is a choice about texture and product form, not "
        "an upgrade.")),
    h(3, "Pre-press &amp; bag loading"),
    ul(["Load <strong>2–7 g</strong> into the inner bag; fold the open end over twice. Don't overfill, "
        "leave room for flow.",
        "For diamonds / mech-sep and any blowout-prone run, sleeve the inner bag inside a "
        "<strong>120–160 µm support bag</strong>.",
        "Flower and sift: form a dense, air-free pre-press puck to stop channeling. Full-melt hash: no "
        "heated pre-press, at most a gentle cold-formed puck to consolidate the load; melty high-grade "
        "material flows without one.",
        "Place in folded parchment, open seam facing out toward you."]),
    h(3, "The press"),
    ol(["Pre-heat the closed (or near-closed) plates against the bag <strong>30–60 s, no pressure</strong>.",
        "<strong>Slowly ramp</strong> force over 15–20 s, watching for the seam to wet and oil to run.",
        "Hold at working force <strong>60–120 s</strong> (up to 180 s) or until flow stops, press "
        "<em>to flow-stop</em>, not to a number" + _c("pressclub-pressure") + ".",
        "Release. Yield from clean 5–6★ input typically runs <strong>60–80%</strong>" + _c("pressclub-thca") + " — "
        "if you're under 50% on good input, something upstream is wrong."]),
    figure(_FIGS["ramp"], 6,
      "Preheat with little pressure, then ramp up slowly and hold until flow stops. Rushing the ramp "
      "(red) spikes pressure before the resin can escape, and bursts the bag."),
    h(3, "Collection (cold chain)"),
    p("Collect immediately with a cold dab tool onto fresh parchment, then into pre-chilled glass; "
      "seal. Cold collection preserves terpenes and sets a cleaner texture. Move straight to your "
      "product path."),
  ]})

SECTIONS.append({"id": "equipment", "kicker": "The hardware", "title": "Equipment-specific effects",
  "blocks": [
    p("Each tool exposes its own sub-levers. Match the press class to the batch size, and favour "
      "accurate temperature control for low-temp work."),
    h(3, "Press class"),
    table(["Class", "Force", "Batch", "Best for", "Note"], [
      ["Manual lever", "0.5–5 t", "0.5–12 g", "Personal → craft", "Fine for small hash runs; force is harder to hold steady"],
      ["Hydraulic", "5–25 t", "4–150 g", "Craft → commercial", "The workhorse; pair with PID plates for accuracy"],
      ["Pneumatic", "5–8 t", "7–35 g", "Craft → commercial", "Smooth, repeatable ramp, ideal for gentle hash pressing"],
      ["Electric / hybrid", "0.75–20 t", "1–115 g", "Personal → commercial", "Hands-free; app / PID control for tight low-temp accuracy"],
    ], cls="compact", caption="Typical market ranges, not spec-sheet law, individual presses vary."),
    h(3, "Plates, bags &amp; cold-chain gear"),
    table(["Tool", "Lever", "Effect"], [
      ["Plates &amp; heat zones", "PID accuracy, even heat", "Tight, even temperature = predictable flow and colour; cheap plates swing and scorch"],
      ["Micron bag", "Mesh size (the gate)", "Hash 25–45 µm (full-melt) to 90 µm (lower grade); flower 75–160 µm; sift 25–90 µm"],
      ["Support sleeve", "120–160 µm outer bag", "Backs the inner bag against rupture, the main blowout defence"],
      ["Pre-press mould", "Puck density &amp; shape", "Even, air-free puck → even flow; flower and sift only"],
      ["Wash vessel &amp; bags", "Agitation, micron stack", "Gentle agitation + a clean stack = cleaner heads"],
      ["Freeze dryer", "Condenser temp, vacuum, time", "Heat-free drying preserves the live profile; the quality default for hash"],
      ["Collection &amp; storage", "Cold tool, sealed glass, fridge", "Cold collection + cold, dark, sealed storage = terpene retention"],
    ], cls="compact"),
  ]})

SECTIONS.append({"id": "trichome-matrix", "kicker": "Read the material", "title": "Input and trichome interaction matrix",
  "blocks": [
    p("Read the material, under a loupe or scope, and let it pick the settings. The micron is "
      "dictated by head size and debris, never chased for its own sake."),
    figure(_FIGS["mesh"], 7,
      "Bigger, cleaner heads can use a coarser bag for more yield. Small heads and broken fragments "
      "slip through or clog a coarse screen, so they need a tighter bag and a slower, gentler ramp."),
    table(["Material / trichome read", "Bag micron", "Plate temp", "Ramp", "Best product"], [
      ["Heads &gt;100 µm, low contaminant", "90 µm (115 if very clean flower)", "cold end", "gentle", "Badder"],
      ["Heads 70–100 µm", "45–73 µm", "88–99 °C flower / cooler hash", "moderate", "Badder / live"],
      ["Heads &lt;70 µm or high fines", "25–37 µm", "slightly higher to push through", "slow, don't overfill", "Careful, blowout-prone"],
      ["Mostly cloudy + high intact %", "match head size", "71–85 °C", "gentle", "Cold-cure badder"],
      ["Low intact % (ruptured / degraded)", "match head size", "99–104 °C, shorter dwell", "moderate", "Carts / sauce"],
      ["High contaminant %", "tighter (25–37 µm)", "+ a few °C", "firm pre-press, slow ramp", "Recover, don't chase melt"],
      ["Fresh-frozen hash (clean, large heads)", "36–90 µm", "60–85 °C", "gentle", "Live rosin"],
    ], cls="compact"),
    callout("key", "The rule the matrix encodes",
      p("Small heads and fines escape or channel a coarse screen, the classic blowout trigger. Tighten "
        "the micron, slow the ramp, and don't overfill.")),
  ]})

SECTIONS.append({"id": "products", "kicker": "Where it ends up", "title": "Post-press product pathways",
  "blocks": [
    p("The same fresh-pressed rosin diverges into every solventless product through the finishing "
      "levers. The press setpoint sets the starting oil; the cure sets the destination."),
    figure(_FIGS["products"], 8,
      "The press gives you fresh rosin; the cure decides what it becomes. Same starting oil, very "
      "different finished products."),
    table(["Product", "Press setpoint", "Cure / finish", "Result"], [
      ["Fresh-press live rosin", "Cool 60–77 °C (hash)", "Use fresh; keep cold", "Sappy, terpene-forward"],
      ["Cold-cure badder / jam", "Cool press", "Sealed jar <strong>10–21 °C</strong>, days–2 weeks" + _c("triminator-coldcure"),
       "Creamy, buttery"],
      ["Sauce", "Cool press, then nucleate", "Warm cure", "Wet, high-terpene"],
      ["Diamonds &amp; sauce (mechanical separation)", "Nucleate first (cold cure 13–16 °C)",
       "Progressive press <strong>40 → 46 → 52 → 57 °C</strong>" + _c("hashtek-thca-tek") + "; briefly "
       "melt the THCa puck to pour (community practice ~120–130 °C, hot enough to start decarb, keep "
       "it short); recombine with the sauce to taste (~70/30 is a common ratio)", "Clear diamonds in sauce"],
      ["Diamonds (jar / jam tek)", "Press clean rosin",
       "Sealed jar: heat <strong>93 °C, 1–2 h</strong>, then crystallise at <strong>38 °C for "
       "1–2 weeks</strong>" + _c("hashtek-jam-tek"), "Crystal balls in jam"],
      ["Vape / cart oil", "Press clean &amp; cool (low-lipid hash is ideal)",
       "Decarb sealed, low and slow: whole rosin at ~71 °C for ~6 days measured only ~3% terpene "
       "loss" + _c("hashtek-decarb") + "; hotter sealed decarbs are faster but cost terps" + _c("lowtemp-carts") + ". "
       "Degas, fridge-test 24 h, fill at ~32 °C" + _c("triminator-carts"), "Clear, stable cart oil"],
      ["Hash hole core", "Cool 60–77 °C, cohesive full-melt", "Roll to a rope while pliable", "A donut core that melts clean"],
    ], cls="compact", caption="One press, many products: the cure is the fork in the road."),
    callout("danger", "The one irreversible rule",
      p("<strong>Never start a diamond press hot.</strong> At high temperature THCa dissolves <em>into</em> "
        "the terpenes and flows out with them, your diamonds leave with the sauce" + _c("hashtek-thca-tek") + ". "
        "Progressive low-temp pressing removes terpenes gradually so the THCa runs out of solvent and "
        "stays behind. And decarboxylation is one-way" + _c("wang2016-decarb") + ": decarbed THC will "
        "never crystallise" + _c("lowtemp-diamonds") + ".")),
    callout("warn", "Sealed vessels build pressure",
      p("Sealed decarbs and jam teks pressurise as CO&#8322; comes off. Standard mason-jar lids "
        "self-vent at roughly ~5 psi" + _c("hashtek-decarb") + ", use jars and lids rated for the job, "
        "keep them away from your face, and open only after they've cooled.")),
  ]})

SECTIONS.append({"id": "failure-modes", "kicker": "What goes wrong", "title": "Common failure modes",
  "blocks": [
    grid([
      card("F-01 · Blowout", "The bag ruptures and contamination floods the slab. <strong>Cause:</strong> "
           "pressure ramped too fast, bag overfilled, micron too coarse for the heads, or no support "
           "sleeve. <strong>Fix:</strong> 120–160 µm outer sleeve, slow 15–20 s ramp, smaller load, micron "
           "matched to head size. Let heat lead, force follow.", tag="rupture"),
      card("F-02 · Low yield / won't flow", "Oil stalls or reabsorbs into the puck. <strong>Cause:</strong> "
           "temp too low, material too dry, pressure too low, or screen too tight for the heads. "
           "<strong>Fix:</strong> +3–6 °C; condition moisture; firmer, slower ramp; open the micron one "
           "step.", tag="flow"),
      card("F-03 · Hazy / unstable / wet", "Cloudy rosin that separates. <strong>Cause:</strong> excess "
           "moisture (under-dried hash, wet flower) causing emulsion, or a high-lipid flower. "
           "<strong>Fix:</strong> dry and condition the input (freeze-dry hash fully; flower ~60% RH); "
           "press cooler; tighten the bag.", tag="moisture"),
      card("F-04 · Flat, terpene-stripped", "Weak nose, dull flavour. <strong>Cause:</strong> plate too "
           "hot, dwell too long, hot collection, or poor storage. <strong>Fix:</strong> drop into the "
           "cold-press band; shorten dwell; collect cold; store sealed, cold and dark.", tag="heat"),
      card("F-05 · Dark or green rosin", "Colour headed the wrong way. <strong>Cause:</strong> overheated, "
           "over-pressed, or contaminated low-grade input. <strong>Fix:</strong> lower temp; gentler ramp; "
           "tighten micron; start from cleaner 5–6★ material. Colour is mostly an input problem.", tag="colour"),
      card("F-06 · Auto-budders vs won't butter", "Texture with a mind of its own. <strong>Cause:</strong> "
           "residual moisture makes it auto-budder greasy; fresh sap simply hasn't nucleated. "
           "<strong>Fix:</strong> control input moisture; to butter on purpose, cold-cure sealed at "
           "13–16 °C for 24–72 h.", tag="texture"),
      card("F-07 · Diamonds won't form", "No crystals, no terpene layer. <strong>Cause:</strong> cure "
           "temperature too high (THCa stays dissolved), material already decarbed, not nucleated, or "
           "the wrong terpene ratio. <strong>Fix:</strong> drop to ~38 °C; start from fresh, undecarbed, "
           "nucleated rosin; press progressively, never start hot.", tag="crystals"),
      card("F-08 · Batch-to-batch inconsistency", "Every run a surprise. <strong>Cause:</strong> "
           "uncontrolled moisture, an eyeballed ramp, no record of what you did. <strong>Fix:</strong> "
           "log every run (material, grade, micron, temp, time, yield, outcome) and change one lever "
           "at a time.", tag="process"),
    ], cols=2),
  ]})

SECTIONS.append({"id": "hierarchy", "kicker": "In order", "title": "Practical control hierarchy",
  "blocks": [
    p("Set these in order. Each step constrains the next; skipping upstream steps wastes the "
      "downstream ones."),
    steps([
      ("Fix the input ceiling first", "Genetics, harvest maturity, wash / sift quality and moisture set "
       "the maximum. You cannot out-press bad input."),
      ("Pick the product", "Badder, live rosin, diamonds, cart or hash hole. This choice sets the "
       "temperature band and the cure."),
      ("Choose the micron from head size &amp; contamination", "Big clean heads → coarser; small heads "
       "or fines → tighter. Don't chase a small micron for its own sake."),
      ("Set the temperature band for material × product", "The lowest temperature that still flows. "
       "Hash cool, flower warmer, degraded material warmer still."),
      ("Ramp pressure to flow, never chase pressure", "Heat first, force second. Pressure only "
       "completes a flow that heat has already started."),
      ("Collect cold, then cure to texture", "Cold collection locks terpenes; the cure (cold / warm / "
       "staged) decides badder, sauce or diamonds."),
      ("Store &amp; validate", "Seal cold, dark, airtight. Log yield and grade, and adjust one lever "
       "next run."),
    ]),
  ]})

SECTIONS.append({"id": "troubleshooting", "kicker": "Quick reference", "title": "Troubleshooting",
  "blocks": [
    p("Observation → likely cause → first checks. Start at the top. Most problems are upstream of "
      "the plates."),
    table(["Observation", "Likely cause", "First checks"], [
      ["Yield far below 50% on a good grade", "Temp / pressure too low, or material too dry",
       "Confirm platen temp; check moisture; firmer slow ramp; +3–6 °C"],
      ["Rosin dark / green", "Too hot, contaminated, or over-pressed", "Lower temp; verify grade and cleanliness; tighten micron"],
      ["Cloudy / unstable / separates", "Moisture or lipids", "Check dry and conditioning; cooler press; tighter bag"],
      ["Weak smell / taste", "Heat or oxygen exposure", "Cooler press; cold collection; sealed cold storage"],
      ["Bag ruptured", "Ramp too fast / overfilled / micron too coarse", "Support sleeve; slower ramp; smaller load; match micron"],
      ["Diamonds won't crystallise", "Cure temp too high, or decarbed / un-nucleated rosin",
       "Drop to ~38 °C; confirm fresh, nucleated, undecarbed rosin"],
      ["Cart clogs / re-crystallises", "Incomplete decarb, oil still above ~50% THCa by weight recrystallises",
       "Re-decarb sealed to ≥90% conversion; fridge-test 24 h before filling" + _c("lowtemp-carts")],
      ["Results vary run to run", "Uncontrolled variables", "Log everything; change one lever per run"],
    ], cls="compact"),
  ]})

SECTIONS.append({"id": "mental-model", "kicker": "Keep one thing", "title": "Rosin process-control principles",
  "blocks": [
    p("If you keep only one thing, keep the chain:"),
    callout("key", "The pressing chain",
      p("<strong>Trichome grade &amp; moisture</strong> set the ceiling → <strong>heat</strong> lowers "
        "resin viscosity → <strong>pressure</strong> drives flow through the screen → <strong>micron</strong> "
        "selects what passes (pure oil vs fats and plant matter) → so <strong>yield and purity trade</strong> "
        "against each other → <strong>collection temperature</strong> locks the texture → the "
        "<strong>cure</strong> decides badder, sauce or diamonds → <strong>cold, dark, sealed storage</strong> "
        "keeps it.")),
    p("Heat to flow, screen to clean, pressure only to finish, then cure for texture. Quality is set "
      "upstream; the press only preserves it or squanders it."),
  ]})
