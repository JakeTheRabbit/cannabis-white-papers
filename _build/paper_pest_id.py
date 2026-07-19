# -*- coding: utf-8 -*-
"""Paper: pest identification and control for cannabis (beginner)."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        stagecard, grid, card, chip, kv, steps)
import figs_lib as L

SLUG = "pest-id"
TITLE = "Pest identification and control"
EYEBROW = "Plant health · Pests"
SUB = ("A beginner's field guide to the eight pests that hit cannabis hardest: how to spot each one, "
       "understand its life cycle, monitor for it, and knock it down with biological controls and "
       "targeted treatments. The companion to your IPM decision process.")
META = [("leaf", "Plant health"), ("image", "8 figures"),
        ("quote", "Evidence-linked · 8 sources"), ("clock", "~18 min read")]
RELATED = ["ipm-sop", "airflow-design", "mould-risk", "cloning"]
REF_IDS = ["ahmed-2024-hemp-pests-florida-jipm", "pulkoski-burrack-2023-piercing-sucking-hemp",
           "cranshaw-2018-phorodon-cannabis-north-america", "cranshaw-wainwright-2020-rice-root-aphid-cannabis",
           "lopez-2023-amblyseius-swirskii-review-jipm", "vanmaanen-2010-broad-mite-swirskii-biocontrol",
           "cloyd-2015-fungus-gnat-ecology-management", "cloyd-2024-biopesticides-cannabis-oregon"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

# Fact-check jurisdiction banner
JURISDICTION_NOTE = 'Jurisdiction note: named biocontrol agents and rates are planning examples only. Confirm legal status and supplier availability in your country (NZ readers: check HSNO/MPI before release).'


SECTIONS.append({"id": "intro", "kicker": "Start here", "title": "What this guide is (and is not)",
  "blocks": [
    callout("NOTE", "Jurisdiction", JURISDICTION_NOTE),
    
    lead("This is a plain-language field guide to identifying and controlling the eight pest groups "
         "that most commonly attack cannabis: spider mites, russet and broad mites, thrips, fungus "
         "gnats, aphids and root aphids, whitefly, and caterpillars. It tells you what each pest "
         "looks like, how fast it breeds, how to monitor for it, and how to treat it with bugs "
         "(biological controls) and sprays."),
    p("It is the &lsquo;who&rsquo;s who&rsquo; companion to the IPM SOP, which is the separate "
      "decision process that tells you <em>when</em> to act and which lever to pull. Read this guide "
      "to recognise the enemy. Read the <a href='ipm-sop.html'>IPM SOP</a> to run the program."),
    ul(["Covers 8 pest groups by name with tell-tale signs, life cycle, monitoring, biocontrol and treatment",
        "Beginner-first: every technical term is defined the first time it appears",
        "Pairs with the IPM SOP (the decision framework), this guide is the identification reference",
        "Bias is toward prevention and early detection, because every pest below breeds faster than you can spray"]),
    figure(table(["Pest", "Where it feeds", "Tell-tale sign", "Fastest cycle", "Primary biocontrol"], [
      ["Spider mites", "Leaf underside", "Fine webbing + pale stippling (30x loupe)", "~3 days", "Phytoseiulus persimilis"],
      ["Russet/broad mites", "Growing tips", "Cupped, glossy, twisted new growth (needs 60-100x)", "~1 week", "Amblyseius swirskii"],
      ["Thrips", "Leaf surface", "Silvery streaks + black frass dots", "~1-2 weeks", "Amblyseius cucumeris"],
      ["Fungus gnats", "Roots / wet media", "Dark flies over the medium, larvae in soil", "~2-3 weeks", "Steinernema feltiae"],
      ["Aphids", "New growth", "Soft clusters, cast white skins, honeydew", "~1 week", "Aphidius parasitoid wasps"],
      ["Root aphids", "Crown / roots", "Yellowing with no visible canopy pest", "~1-2 weeks", "Beneficial nematodes"],
      ["Whitefly", "Leaf underside", "Clouds of white flies when disturbed", "~2-3 weeks", "Encarsia / Eretmocerus"],
      ["Caterpillars", "Flowers / buds", "Frass + bore holes, triggers bud rot", "~2-3 weeks", "Bacillus thuringiensis (Btk)"],
    ], cls="compact",
      caption="Pest at a glance. Cycle times are the fastest seen in warm rooms and shorten further as temperature rises." + _c("ahmed-2024-hemp-pests-florida-jipm")), 1,
      "Eight pest groups, where to look, what to look for, and the first beneficial to reach for."),
  ]})

SECTIONS.append({"id": "key-terms", "kicker": "Vocabulary", "title": "Key terms, defined once",
  "blocks": [
    p("A handful of words appear throughout this guide and the IPM SOP, so define them now. You do "
      "not need to memorise them, each one comes back in context."),
    defterm("IPM (Integrated Pest Management)", "A layered strategy that combines prevention, "
            "monitoring, biological controls and targeted sprays instead of relying on calendar "
            "spraying."),
    defterm("Biocontrol / beneficial", "A living predator (e.g. a predatory mite), parasitoid wasp, "
            "or microbe (fungus or bacterium) you release to eat or infect the pest."),
    defterm("Preventative vs curative", "Preventative agents establish before pests arrive and hold "
            "the line. Curative agents knock down an active outbreak that is already underway."),
    defterm("Life cycle / generation time", "Egg to egg-laying adult. Warm dry rooms shorten this to "
            "under a week for mites, which is why a small spot becomes a crop-wide problem fast."),
    defterm("Loupe / scope", "A 30x hand loupe finds spider mites. Russet and broad mites (confirm at 60&ndash;100&times; before treating; symptoms overlap with heat tacoing and tip burn) are smaller "
            "than a millimetre and need 60-100x magnification to see at all."),
    defterm("Frass, honeydew, stippling", "Pest droppings, the sticky sugar excretion sap-suckers "
            "leave behind, and the fine pale feeding speckles on a leaf, respectively."),
    defterm("Action threshold", "The pest count at which you stop watching and start treating. It is "
            "set per facility, not universal. See the IPM SOP."),
    figure(L.line("Why early establishment wins",
            [(0, 4), (1, 5), (2, 6), (3, 7), (4, 8), (5, 9)],
            ["wk 0", "wk 1", "wk 2", "wk 3", "wk 4", "wk 5"],
            ylab="pest count", ymax=80,
            note="Preventative line (low, flat) vs a curative response that only starts after the population spikes.",
            bands=[(0, 6, L.GL, "preventative held low")]), 2,
      "A preventative beneficial established early keeps the population flat. Waiting until threshold "
      "means treating a spike that is already well ahead of you." + _c("lopez-2023-amblyseius-swirskii-review-jipm")),
  ]})

SECTIONS.append({"id": "sap-suckers", "kicker": "The core pests, part 1",
  "title": "Leaf sap-suckers: spider mites, thrips, aphids and whitefly",
  "blocks": [
    p("These four feed on leaves and stems by piercing cells and sucking sap, so they share a look: "
      "pale stippling, distortion and loss of vigour" + _c("pulkoski-burrack-2023-piercing-sucking-hemp") +
      ". Telling them apart is about the secondary signs each one leaves."),
    ul(["<strong>Spider mites:</strong> leaf-underside stippling plus fine webbing. Under hot, dry conditions egg-to-adult often finishes in about a week (sometimes under two weeks); females often lay on the order of ~100 eggs over life (exact times depend on temperature and host).",
        "<strong>Thrips:</strong> silvery rasping streaks plus tiny black frass dots. They drop to the medium to pupate, so leaf sprays alone miss a whole life stage.",
        "<strong>Aphids:</strong> soft-bodied clusters on new growth, cast white skins, honeydew that grows black sooty mould. They can give live birth, so buildup is explosive.",
        "<strong>Whitefly:</strong> tiny white moth-like adults that flush up in a cloud when disturbed, with uniform yellowing and lower-canopy decline."]),
    p("Note that the aphid most associated with cannabis is its own species, the cannabis aphid "
      "(<em>Phorodon cannabis</em>), now recognised as a pest in North America" + _c("cranshaw-2018-phorodon-cannabis-north-america") +
      ". The shared driver across all four is environment: warm plus dry shortens every life cycle, "
      "so climate control is the first lever, not the spray bottle."),
    figure(grid([
      card("Spider mites", "Webbing + fine pale stipple on leaf undersides. Confirm with a 30x loupe."),
      card("Thrips", "Silver streaks with black frass dots. Pupae hide in the growing medium."),
      card("Aphids", "Curled new growth, clustered bodies, cast white skins and sticky honeydew."),
      card("Whitefly", "Yellowing leaves and white flies that lift off the underside when disturbed."),
    ], cols=2), 3,
      "Four sap-suckers, four damage signatures. The piercing-feeding habit is shared, the secondary "
      "signs are how you tell them apart."),
    figure(L.bars("Spider mite egg-to-adult cycle vs temperature",
            [("27C / 20% RH", 3), ("21C", 7), ("10C", 19)], unit=" days",
            note="Heat and low humidity speed reproduction. A room run warm and dry breeds mites fastest.",
            maxv=22), 4,
      "The warmer and drier the room, the faster the spider mite cycle, from about 3 days in a hot dry "
      "room to nearly 3 weeks in the cold." + _c("ahmed-2024-hemp-pests-florida-jipm")),
  ]})

SECTIONS.append({"id": "hidden-pests", "kicker": "The core pests, part 2",
  "title": "The hidden ones: russet and broad mites, fungus gnats, root aphids and caterpillars",
  "blocks": [
    p("This group is dangerous because the damage shows before the pest does. Russet mites "
      "(<em>Aculops cannabicola</em>, under 1 mm, needs 80-100x) and broad mites (needs ~60x) are "
      "invisible to the naked eye and announce themselves through cupped, glossy or &lsquo;wet-looking&rsquo; "
      "new growth, twisted tops and stunting. Those symptoms are often misread as nutrient or heat "
      "stress" + _c("vanmaanen-2010-broad-mite-swirskii-biocontrol") + "."),
    ul(["<strong>Russet/broad mites:</strong> cupped, glossy, twisted new growth. Sub-millimetre, need 60-100x. Easily mistaken for a nutrient problem.",
        "<strong>Fungus gnats:</strong> larvae eat root hairs in wet media, adults are weak dark fliers over the medium. The larvae open the door to root-rot pathogens.",
        "<strong>Root aphids:</strong> feed at the crown and roots, causing yellowing and stalled growth with no visible canopy pest. Check the root zone and pot base.",
        "<strong>Caterpillars / budworms:</strong> frass and bore holes in flowers, a rapid trigger for bud rot. Scout at dusk when larvae feed."]),
    p("Fungus gnat larvae weaken plants and wound roots, and the damage they cause interacts with "
      "soil-borne disease, which is why a wet-media gnat problem so often turns into a root-rot "
      "problem" + _c("cloyd-2015-fungus-gnat-ecology-management") + ". Cannabis is also a confirmed host "
      "of the rice root aphid, which lives below ground and is missed entirely by canopy scouting" +
      _c("cranshaw-wainwright-2020-rice-root-aphid-cannabis") + "."),
    callout("warn", "Misdiagnosis is the trap",
      p("Twisted, glossy tops look exactly like nutrient burn or heat stress. Confirm with a loupe or "
        "scope and a root inspection <em>before</em> you change the feed. Feeding the plant harder will "
        "not fix a mite.")),
    figure(L.zones("Where each hidden pest lives on the plant", 0, 4, [
            (3, 4, L.GL, "Growing tips: russet + broad mites"),
            (2, 3, L.GXL, "Mid-canopy: (sap-suckers above)"),
            (1, 2, L.AMBL, "Flowers / buds: caterpillars"),
            (0, 1, L.BLUL, "Root zone / crown: fungus gnats + root aphids"),
          ], note="The hidden pests live where you do not normally look: the tips, inside buds, and below the medium."), 5,
      "Map your inspection to where each pest actually lives. Glancing at the mid-canopy misses all "
      "four of these."),
  ]})

SECTIONS.append({"id": "monitoring", "kicker": "Catch it early",
  "title": "Monitoring: traps, loupes and a weekly scouting routine",
  "blocks": [
    p("You cannot control what you do not measure, and early detection is the single biggest lever "
      "you have. Run a fixed weekly scouting walk on the same day, inspecting leaf undersides, "
      "growing tips, flowers and the root zone, and step up to twice weekly as rooms warm up."),
    p("Hang yellow sticky cards at canopy height for thrips, whitefly and fungus-gnat adults at "
      "a mapped density (example: ~1 card / 100 m&sup2; or ~1,000 sq ft) as a starting point, with more cards giving a better signal. "
      "Place fungus-gnat cards low, near the medium surface, where the adults fly. Record the count "
      "on each card every week so you track the trend, not just the snapshot."),
    ul(["Scout weekly on a fixed day, spot-check twice weekly when temperatures and pest development rise",
        "Yellow sticky cards: minimum ~1 per 1,000 sq ft, low at the medium for fungus gnats, canopy height for thrips/whitefly",
        "Log card counts each week, a rising trend (not a single number) is the alarm",
        "30x loupe for spider mites, 60-100x scope for russet/broad mites, inspect undersides, tips, flowers AND roots",
        "Action thresholds are facility-specific, e.g. one grower tolerates 10-15 thrips/card/week, another with virus history tolerates under 5"]),
    figure(L.line("Sticky-card trend: thrips per card",
            [(0, 2), (1, 3), (2, 4), (3, 7), (4, 11), (5, 16)],
            ["wk 1", "wk 2", "wk 3", "wk 4", "wk 5", "wk 6"],
            ylab="thrips / card", ymax=20,
            note="The action threshold (10/card here) is crossed at week 5. The trend warned you a week earlier.",
            bands=[(0, 10, L.GL, "below threshold: monitor")]), 6,
      "Logging the count each week turns sticky cards into a trend line. The slope, not any single "
      "reading, tells you when to trigger the IPM SOP."),
    figure(L.flow("The weekly scouting routine",
            [("Same day", "scout on a fixed weekly day"),
             ("Inspect", "undersides, tips, flowers, roots"),
             ("Log cards", "read and record every sticky card"),
             ("Compare", "this week vs last week"),
             ("Decide", "below threshold = monitor, above = IPM SOP")]), 7,
      "A repeatable five-step walk. The point is consistency: same day, same plants, same cards, every week."),
  ]})

SECTIONS.append({"id": "controls", "kicker": "What to release and spray",
  "title": "Biological controls and treatments, pest by pest",
  "blocks": [
    p("Match the tool to the pest, and to whether you are preventing or reacting. For spider mites "
      "the specialist predator <em>Phytoseiulus persimilis</em> is the fast curative, but it wants "
      "humidity above ~60% RH, while <em>Neoseiulus californicus</em> or <em>Amblyseius swirskii</em> "
      "establish preventatively. Thrips are managed with <em>Amblyseius cucumeris</em> or swirskii at "
      "about 100-300 mites per square metre, with control typically visible around 3 weeks" + _c("lopez-2023-amblyseius-swirskii-review-jipm") + "."),
    p("Aphids respond to species-matched parasitoid wasps (<em>Aphidius colemani</em> for green peach "
      "aphid, <em>Aphidius matricariae</em> for cannabis aphid) plus the insect-killing fungus "
      "<em>Beauveria bassiana</em>. Whitefly are hit with <em>Encarsia</em> or <em>Eretmocerus</em> "
      "wasps and swirskii. Fungus gnats are drenched in the medium with <em>Steinernema feltiae</em> "
      "nematodes and the bacterium Bti every ~2 weeks. Caterpillars are killed with <em>Bacillus "
      "thuringiensis kurstaki</em> (Btk), which only kills larvae that eat it. Several of these "
      "biopesticides have been tested directly on cannabis pests" + _c("cloyd-2024-biopesticides-cannabis-oregon") + "."),
    callout("warn", "Sulphur and flowering do not mix",
      p("Russet and broad mites respond to predatory mites plus micronised sulphur, but never apply "
        "sulphur during flowering. It risks residue, taint and phytotoxicity on the buds.")),
    figure(table(["Pest", "Preventative", "Curative", "Microbial / spray", "Key constraint"], [
      ["Spider mites", "N. californicus / swirskii", "P. persimilis", "Insecticidal soap, oils", "Persimilis needs >60% RH"],
      ["Russet/broad mites", "A. swirskii", "Predatory mites", "Micronised sulphur", "No sulphur in flower"],
      ["Thrips", "cucumeris / swirskii (100-300/m2)", "Soil predators for pupae", "Beauveria bassiana", "Hit canopy AND medium"],
      ["Fungus gnats", "S. feltiae nematodes", "Bti drench (every ~2 wk)", "Bti / Gnatrol", "Treat the wet medium"],
      ["Aphids", "Aphidius wasps", "Match wasp to species", "Beauveria bassiana", "colemani vs matricariae"],
      ["Root aphids", "Beneficial nematodes", "Soil drench", "Beauveria bassiana", "Below-ground, drench roots"],
      ["Whitefly", "Encarsia / Eretmocerus", "Add swirskii", "Insecticidal soap", "Persistent, stay ahead"],
      ["Caterpillars", "Scout + Btk early", "Btk spray", "Bacillus thuringiensis (Btk)", "Larva must ingest it"],
    ], cls="compact",
      caption="Beneficial selection matrix. Release rates and constraints are starting points, tune to your facility and supplier."), 8,
      "Pick the agent by pest and by whether you are preventing or reacting. Timing beats dose: "
      "beneficials only out-breed pests if released before the pest gets a head start."),
  ]})

SECTIONS.append({"id": "pitfalls", "kicker": "Where growers go wrong",
  "title": "Troubleshooting and common pitfalls",
  "blocks": [
    p("Most pest disasters are diagnosis and timing failures, not product failures. The classic "
      "mistakes repeat across facilities, and all of them are avoidable with a scope and a calendar."),
    table(["Symptom", "Likely cause", "Confirm / fix"], [
      ["Twisted, glossy new growth", "Russet or broad mites (not nutrients)", "Confirm at 60-100x before changing the feed"],
      ["Thrips/gnats rebound after spraying", "Soil-dwelling pupae/larvae untouched", "Treat the medium AND the canopy, not just leaves"],
      ["Beneficials released, pest still wins", "Released too late onto an exploding population", "Establish preventatively, predators cannot catch up to a spike"],
      ["Persimilis dies off, mites persist", "Room below ~60% RH, wrong for the agent", "Raise RH or pick a drier-tolerant predator"],
      ["Residue / taint at harvest", "Sulphur or harsh oils used in flower", "Stop sulphur and harsh oils before bloom"],
      ["New crop infested from day one", "Skipped clone/mother quarantine", "Isolate and inspect every incoming plant"],
    ], cls="compact"),
    callout("note", "When a treatment &lsquo;fails&rsquo;",
      p("Re-confirm the pest ID, check you covered every life stage (soil included), and verify the "
        "environment actually suited the agent. Most &lsquo;failed&rsquo; biocontrol is one of those three.")),
    figure(L.flow("Symptom to confirmed cause to action",
            [("Symptom", "twisted tips, yellowing, silver streaks"),
             ("Suspect", "pest vs nutrient/heat?"),
             ("Confirm", "loupe/scope + root check"),
             ("Identify", "name the exact pest"),
             ("Act", "trigger the IPM SOP, never spray blind")]), 9,
      "Never treat on a guess. The confirmation step, between suspecting and acting, is where most "
      "wasted sprays get prevented."),
  ]})

SECTIONS.append({"id": "expectations", "kicker": "What success looks like",
  "title": "Realistic expectations and prevention payoff",
  "blocks": [
    p("Eradication is rarely the goal. Durable suppression below the action threshold is. Expect "
      "biological control to take time: thrips control is often visible only around 3 weeks after "
      "release, and breaking a fungus-gnat cycle by trapping adults while killing larvae usually "
      "takes 4-8 weeks" + _c("cloyd-2015-fungus-gnat-ecology-management") + "."),
    p("The cheapest &lsquo;treatment&rsquo; is prevention. Quarantine and inspect every incoming "
      "clone, keep mother plants clean (an infested mother makes every cutting infested), control "
      "humidity and airflow, sanitise tools and rooms, and run the weekly scout without fail. A "
      "facility that prevents and detects early spends far less on curatives and loses far less crop "
      "than one that fights outbreaks reactively."),
    callout("key", "What to actually expect",
      ul(["The goal is suppression below threshold, not zero pests. Clean crops come from prevention, not heroic sprays.",
          "Biologicals are slow but durable: thrips ~3 weeks to visible control, fungus-gnat cycle ~4-8 weeks to break.",
          "Prevention stack: quarantine clones, keep mothers clean, control RH and airflow, sanitise, scout weekly.",
          "An infested mother plant guarantees infested clones. The mother room is your most important inspection point."], "tight")),
    figure(L.bars("Cost: prevention-led vs reactive program",
            [("Prevention: monitoring", 15), ("Prevention: biocontrol", 20),
             ("Reactive: curatives", 45), ("Reactive: crop loss", 60)], unit=" rel.",
            note="Relative cost. A prevention-led program spends a little steadily, a reactive one pays in curatives and lost crop.",
            maxv=70), 10,
      "Steady, modest prevention spend versus the much larger bill for curatives and crop loss when "
      "you fight outbreaks reactively."),
    p("Track your outcomes against the thresholds in the <a href='ipm-sop.html'>IPM SOP</a> so you "
      "know whether the program is actually holding, and keep the room itself working for you with "
      "good <a href='airflow-design.html'>airflow design</a> that denies pests the warm, still, humid "
      "pockets they love."),
  ]})
