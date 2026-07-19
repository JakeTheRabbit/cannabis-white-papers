# -*- coding: utf-8 -*-
"""Paper: defoliation and plant training for maximum yield (beginner)."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        stagecard, grid, card, chip, kv, steps)
import figs_lib as L

SLUG = "defoliation-training"
TITLE = "Defoliation and plant training for maximum yield"
EYEBROW = "Canopy · Training"
SUB = ("A beginner's guide to topping, low-stress training, trellising, lollipopping and "
       "defoliation: what each one does, when to do it, and how to avoid overdoing it.")
META = [("scissors", "Canopy"), ("image", "12 diagrams"),
        ("quote", "Evidence-linked · 8 sources"), ("clock", "~12 min read")]
RELATED = ["airflow-design", "mould-risk", "harvest-dry-trim-cure"]
REF_IDS = ["sikora-2019-apical-bud-hemp", "massuela-2022-pruning-cbd-yield",
           "rodriguez-morrison-2021-ppfd-yield", "danziger-2022-planting-density",
           "wang-2020-shade-avoidance", "mahmoud-2023-budrot-botrytis",
           "anthony-2020-training-light-interception", "massuela-springer-2026-topping-hemp"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

SECTIONS.append({"id": "intro", "kicker": "Start here", "title": "Why we cut and bend the plant on purpose",
  "blocks": [
    lead("Plant training and defoliation are deliberate physical interventions, bending, "
         "tying, and selectively removing leaves and branches, that reshape a cannabis plant "
         "so more of its energy lands in the flowers you actually harvest."),
    p("Left alone, a plant grows tall with one dominant top and a tangle of weak, shaded lower "
      "growth that produces airy, low-value flower. <strong>Training</strong> flattens and widens "
      "the canopy (the leafy roof of growth) so light hits more bud sites evenly. "
      "<strong>Defoliation</strong> removes selected leaves and opens the interior so "
      "light and air reach the middle instead of being blocked. Done right, these techniques raise "
      "yield and quality. Done badly or too aggressively, they stress the plant and cost you flower."),
    ul(["<strong>Two families of technique:</strong> training (reshaping via bending, tying and "
        "cutting growth tips) and defoliation (removing leaves and lower growth).",
        "The goal is an even, flat, well-lit canopy where every bud site gets strong light and airflow.",
        "This is an active, scheduled process tied to specific days of the grow, not a one-time event.",
        "Overdoing it is a real risk. This guide covers what <em>not</em> to remove."]),
    figure(L.flow("Untrained plant vs trained flat canopy",
            [("Untrained", "one tall cola, shaded fluffy lower growth"),
             ("Train + spread", "branches bent flat across a trellis"),
             ("Trained", "many even tops, light reaches every site")],
            note="Flattening the canopy turns one light-hogging top into a field of even bud sites."), 1,
      "An untrained plant wastes light on a single top while the interior stays dark and airy. A "
      "trained, flat canopy shares strong light across dozens of bud sites at the same height."),
    callout("note", "Who this is for",
      p("Anyone growing cannabis who wants repeatable yield instead of a jungle. Pairs with the "
        "<a href='airflow-design.html'>airflow design</a> and "
        "<a href='mould-risk.html'>mould risk</a> papers, since canopy work is half about light "
        "and half about keeping air moving.")),
  ]})

SECTIONS.append({"id": "key-terms", "kicker": "Vocabulary", "title": "Every term, defined once",
  "blocks": [
    p("Before the how-to, here is the full vocabulary used throughout. These terms come up "
      "constantly in grow rooms and many beginners conflate them. Don't memorise them. "
      "Each comes back in context."),
    defterm("Node", "The point on a stem where leaves and branches grow out. Counting nodes is how "
            "training is measured (&lsquo;keep the top 3 nodes&rsquo;)."),
    defterm("Topping", "Cutting off the very top growing tip to stop upward growth and force two new "
            "tops from the node below it."),
    defterm("FIM", "A partial top: cutting most but not all of the tip, which can "
            "produce several new tops instead of just two."),
    defterm("Apical dominance", "The plant's natural tendency to push one main top taller than the "
            "side branches. Topping and LST break this so side branches catch up."),
    defterm("LST (Low-Stress Training)", "Gently bending and tying branches down to spread them "
            "flat, without cutting anything."),
    defterm("Trellis / SCROG (Screen of Green)", "Horizontal netting the canopy grows up through, "
            "used to hold branches spread out and evenly spaced."),
    defterm("Lollipopping", "Stripping the small branches, nodes and leaves off the bottom of the "
            "plant so it looks like a lollipop: bare stick below, canopy on top."),
    defterm("Defanning / defoliation", "Selectively removing large fan leaves to open the canopy "
            "for light and air."),
    defterm("Fan leaves", "The big, classic cannabis leaves that collect light, not the "
            "small sugar leaves growing out of the buds themselves."),
    defterm("Source vs sink", "A &lsquo;source&rsquo; leaf makes more sugar than it uses; a "
            "&lsquo;sink&rsquo; (a flower, or a shaded leaf) consumes more than it makes."),
    figure(L.flow("Anatomy of a plant, bottom to top",
            [("Lollipop zone", "lower ~third: stripped"),
             ("Lateral branches", "side arms, bent flat"),
             ("Nodes + fan leaves", "keep top 3 nodes"),
             ("Growing tip", "topped to make new tops")],
            note="Training works on the tip; lollipopping clears the base; defanning thins the middle."), 2,
      "The parts of the plant each technique acts on, from the bare lower &lsquo;lollipop zone&rsquo; "
      "up to the growing tip that topping removes."),
  ]})

SECTIONS.append({"id": "training-light", "kicker": "The core idea",
  "title": "How training and defoliation actually raise yield",
  "blocks": [
    p("The underlying mechanism is simple: <strong>light and air reaching more of the plant</strong>. "
      "A flat, spread canopy puts dozens of bud sites at the same height under strong light, instead "
      "of one top hogging it all while the rest sits in shade."),
    p("Light intensity is measured in <strong>PPFD</strong> (photosynthetic photon flux density: "
      "how much usable light lands on the canopy each second). Flower-room light climbs from roughly "
      "400&ndash;800 PPFD in early flower to a peak around 1000&ndash;1200 PPFD mid-bloom" +
      _c("rodriguez-morrison-2021-ppfd-yield") + ". That intensity only pays off if it actually "
      "reaches the bud, which is why the interior must be opened up. Cannabis yield keeps "
      "responding to higher light right up into that range when the canopy can use it" +
      _c("rodriguez-morrison-2021-ppfd-yield") + "."),
    figure(L.line("Target canopy light (PPFD) across the grow",
            [(0, 350), (1, 450), (2, 600), (3, 800), (4, 1000), (5, 1150), (6, 1200), (7, 1050), (8, 900)],
            ["veg", "fl wk1", "wk2", "wk3", "wk4", "wk5", "wk6", "wk7", "wk8"],
            ylab="PPFD", ymin=0, ymax=1300,
            note="Light rises into a 1000-1200 plateau mid-bloom, then tapers at the end."), 3,
      "A typical flower-room light curve: 400&ndash;800 PPFD in week 1, a 1000&ndash;1200 plateau "
      "weeks 4&ndash;7, then a taper. Opening the canopy is what lets the plateau reach lower buds." +
      _c("rodriguez-morrison-2021-ppfd-yield")),
    p("The <strong>sources-and-sinks</strong> framework explains the trade-off. A well-lit leaf is a "
      "sugar factory (a source) feeding the buds. But a shaded leaf deep in the canopy flips into a "
      "drain (a sink), consuming more than it makes" + _c("massuela-2022-pruning-cbd-yield") + ". "
      "Opening the canopy converts shaded would-be sinks back into productive sources, and improves "
      "airflow at the same time."),
    figure(L.flow("Sources, sinks, and what opening the canopy changes",
            [("Lit fan leaf", "SOURCE: makes sugar"),
             ("Sugar flow", "feeds the flower"),
             ("Flower", "SINK: consumes sugar"),
             ("Shaded leaf opened up", "flips SINK back to SOURCE")],
            note="A leaf that is fed light pays its way. A shaded one costs you. Open the canopy to flip it back."), 4,
      "Well-lit fan leaves feed the flowers. Shaded interior leaves become a drain. Opening the "
      "canopy turns them back into producers and drops humidity around the buds." +
      _c("massuela-2022-pruning-cbd-yield")),
    p("Better airflow through an open canopy lowers the humidity that pools around dense buds, which "
      "directly reduces bud-rot risk. Aim to keep <strong>VPD</strong> (vapour pressure deficit, a "
      "combined measure of how &lsquo;thirsty&rsquo; the air is) between about 0.8 and 1.2 kPa. "
      "Stagnant, humid air inside a closed canopy is exactly the condition that lets grey mould take "
      "hold in a thick cola" + _c("mahmoud-2023-budrot-botrytis") + "."),
    callout("key", "Why the work pays off",
      ul(["Spreading the canopy flat lets many bud sites share the strongest light instead of one top.",
          "Opening the interior lets that high light reach lower and inner buds that would otherwise stay airy.",
          "Better airflow lowers humidity around dense buds and cuts mould and bud-rot risk" +
          _c("mahmoud-2023-budrot-botrytis") + ".",
          "Keep VPD roughly 0.8&ndash;1.2 kPa. Airflow from defoliation helps hold it there."], "tight")),
  ]})

SECTIONS.append({"id": "topping-lst", "kicker": "The core idea",
  "title": "Topping, FIM and low-stress training in veg",
  "blocks": [
    p("Topping and LST both fight <strong>apical dominance</strong>, the plant's habit of "
      "sending one top racing upward while the side branches lag. Topping cuts that tip off, which "
      "redirects growth hormones to the side branches and turns one main top into two or more, "
      "creating a bushier, wider plant" + _c("sikora-2019-apical-bud-hemp") + ". Removing the apical "
      "bud has been shown to change how the whole plant allocates growth and yield" +
      _c("sikora-2019-apical-bud-hemp") + "."),
    p("<strong>LST</strong> does the same thing without cutting: you bend the tall central stem down "
      "and tie it sideways so the lower branches catch up and the canopy levels out. Because nothing "
      "is cut, there is no recovery time, which makes LST the gentler, beginner-friendly "
      "option, especially in a home tent. Topping is the heavier tool, best reserved for longer veg "
      "cycles or tall, stretchy genetics" + _c("massuela-springer-2026-topping-hemp") + "."),
    figure(L.flow("Topping: one tip becomes two tops",
            [("One apical top", "growing straight up"),
             ("Cut the tip", "remove the top node"),
             ("Two new tops", "emerge from the node below")],
            note="Cutting the tip releases the side shoots from apical dominance."), 5,
      "Topping removes the dominant tip; the node below responds by pushing two new tops, doubling "
      "the bud sites at that height." + _c("sikora-2019-apical-bud-hemp")),
    figure(L.flow("LST: bend, don't cut",
            [("Tall central stem", "dominant, upright"),
             ("Bend + tie down", "pull it sideways to the pot edge"),
             ("Even canopy", "side branches fan out and level off")],
            note="Same flattening as topping, with no wound and no recovery time."), 6,
      "Low-stress training reshapes the plant by bending and tying instead of cutting: lower "
      "stress, no recovery, easy for beginners."),
    p("In commercial veg, the first topping is typically done around <strong>day 5&ndash;7</strong> "
      "of veg, with noticeably taller outlier plants getting 2&ndash;3 nodes removed to match the rest "
      "of the canopy height. In a standard 14-day veg, plants are often topped only once, if at all; "
      "a 21-day veg is where topping becomes routine" + _c("massuela-springer-2026-topping-hemp") + "."),
    table(["Height class", "Typical veg length", "Topping approach"], [
      ["Tall / stretchy genetics", "~8&ndash;10 days", "Top early; remove 2&ndash;3 nodes from outliers"],
      ["Mid genetics", "~10&ndash;14 days", "Top once around day 5&ndash;7, or LST only"],
      ["Short genetics", "~14&ndash;21 days", "Often LST only; topping optional"],
    ], cls="compact",
    caption="Match the technique to veg length and how tall the genetics run. Shorter, faster vegs "
            "lean on LST; longer vegs make routine topping worthwhile." +
            _c("massuela-springer-2026-topping-hemp")),
    callout("tip", "Beginners: start with LST",
      p("If you are new, skip topping for your first run and use LST. Bending and tying gives you "
        "most of the flat-canopy benefit with none of the recovery risk. You can always add "
        "topping once you know how your genetics stretch.")),
  ]})

SECTIONS.append({"id": "trellis-spread", "kicker": "The core idea",
  "title": "Trellising and spreading: locking the canopy flat",
  "blocks": [
    p("A <strong>trellis</strong> is horizontal netting stretched over the table that the plants grow "
      "up through. It does two jobs: early on it holds a spread canopy in place, and later it stops "
      "heavy buds from snapping their branches. Spreading the branches so light reaches the whole "
      "table is what makes the high mid-bloom PPFD actually translate into yield" +
      _c("anthony-2020-training-light-interception") + "."),
    p("A common workflow sets all three trellis layers on <strong>day 1 of flower</strong>, with the "
      "first net placed 1&ndash;2 inches below the top of the canopy. Around day 5&ndash;7 the plants "
      "have grown through that first net and the team <strong>spreads</strong> the branches: "
      "pulling them out from the central stalk and tucking them into open squares so light reaches the "
      "middle and the whole table fills out evenly."),
    figure(L.flow("Three trellis layers, three jobs",
            [("Net 1 (low)", "spread: open the center to light"),
             ("Net 2 (mid)", "support: hold branches as they stretch"),
             ("Net 3 (high)", "support: carry heavy flower weight")],
            note="The first net spreads; the upper nets exist mainly to hold flower weight."), 7,
      "Side view of a flower table with three stacked nets. The lowest spreads the canopy; the upper "
      "two support the weight of bulking flowers." + _c("anthony-2020-training-light-interception")),
    figure(L.flow("Spreading: fill every square",
            [("Central stalk", "branches bunched in the middle"),
             ("Pull outward", "draw each branch into an open square"),
             ("Even grid", "every square filled, center lit")],
            note="Spreading early opens the center and reduces how many leaves you later remove."), 8,
      "Top-down, spreading pulls branches off the central stalk into the empty trellis squares so the "
      "table fills evenly and the interior is no longer shaded."),
    ul(["All trellis levels are set on flower day 1; the first net sits 1&ndash;2 inches below the canopy top.",
        "Plants grow through the first net by about day 5 and are spread out from the central stalk.",
        "Spreading opens the center to light and airflow and reduces how many fan leaves you later remove.",
        "Net count scales with height: short plants need about 2 layers, tall genetics need 3."]),
    callout("note", "Less spreading work, less defoliation later",
      p("The better you spread the canopy early, the fewer fan leaves you will have to remove later. "
        "A well-spread table is already open to light, so defoliation is then a light touch-up, "
        "not major surgery.")),
  ]})

SECTIONS.append({"id": "schedule", "kicker": "Do this",
  "title": "The defoliation and training schedule, day by day",
  "blocks": [
    p("Here is a clear flower-room timeline you can follow as a default and adjust to your genetics. "
      "It runs from trellising on day 1 through to an optional final defan late in bloom."),
    figure(L.flow("The flower-room work timeline",
            [("Day 1", "trellis the tables"),
             ("Day 5-14", "spread through the first net"),
             ("Day 7-10", "Phase 1: lollipop the base"),
             ("Day 21-28", "Phase 2: defan lower leaves"),
             ("Day 42-49", "Phase 3: optional final defan")],
            note="Heavy work is front-loaded into early flower; late work is optional and per-strain."), 9,
      "The default flower timeline, day 1 to week 7. The aggressive structural work happens early; "
      "the only late task is an optional, strain-by-strain final defan."),
    steps([
      ("Day 1: Trellis", "Set all trellis levels. Place the first net 1&ndash;2 inches below the top of the canopy."),
      ("Day 5&ndash;14: Spread", "Once plants grow through the first net, pull branches off the central stalk into the open squares to fill the table evenly."),
      ("Day 7&ndash;10: Phase 1 lollipop", "Strip the small branches, nodes and leaves from the lower half/third. Keep at least the top 3 nodes on each main branch."),
      ("Day 21&ndash;28: Phase 2 defan", "Remove the lower fan leaves across every plant for light penetration and airflow."),
      ("Day 42&ndash;49: Phase 3 defan", "Optional final defan, decided strain by strain. Only do it if a particular strain still needs more light or air in the canopy."),
    ]),
    table(["Flower day", "Action", "Why"], [
      ["Day 1", "Trellis (all levels)", "Lock the canopy structure before growth fills in"],
      ["Day 5&ndash;14", "Spread through first net", "Open the center to light; fill the table evenly"],
      ["Day 7&ndash;10", "Phase 1 lollipopping", "Remove lower larf that would never finish well"],
      ["Day 21&ndash;28", "Phase 2 defanning", "Light and airflow to the lower and inner buds"],
      ["Day 42&ndash;49", "Phase 3 defanning (optional)", "Final touch-up only if that strain needs it"],
    ], cls="compact",
    caption="A default flower-room timeline. The lollipop zone is roughly the bottom 10&ndash;18 "
            "inches (the lower third), where growth would otherwise make small, underdeveloped larf."),
    figure(L.flow("The lollipop zone",
            [("Top: keep", "top 3 nodes per branch stay"),
             ("Middle: thin", "defan for light and air"),
             ("Bottom 10-18in: remove", "lower third stripped to a stick")],
            note="Clear the bottom third; keep the top 3 nodes on every main branch."), 10,
      "Lollipopping removes the lower ~10&ndash;18 inches (the bottom third) and keeps at least the "
      "top 3 nodes on each main branch, so the plant spends energy on flower that will actually finish."),
    callout("warn", "Lollipop early, not late",
      p("Phase 1 lollipopping belongs in the first week or two of flower, while the plant can still "
        "recover and redirect energy. Stripping the base hard late in bloom just wounds the plant "
        "when it should be bulking flower.")),
  ]})

SECTIONS.append({"id": "pitfalls", "kicker": "Avoid these",
  "title": "What NOT to overdo, and common beginner mistakes",
  "blocks": [
    p("The single biggest mistake is <strong>removing too many fan leaves</strong>. Fan leaves are "
      "&lsquo;sources&rsquo; that make more energy than they use, so the goal is to leave as many on "
      "as possible while still achieving light penetration and airflow. Strip too many and you starve "
      "the buds you are trying to grow. Over-pruning can cut into both yield and cannabinoid "
      "content rather than helping" + _c("massuela-2022-pruning-cbd-yield") + "."),
    figure(L.flow("Over-defoliated vs correctly thinned",
            [("Over-stripped", "bare stems, few leaves: STARVED"),
             ("vs", "leave the sources on"),
             ("Correctly thinned", "open interior, plenty of fan leaves: FED + AIRY")],
            note="Open the canopy, but leave the leaves that feed it. More bare stem is not better."), 11,
      "Left: an over-defoliated plant with little leaf area left to feed the flowers. Right: a "
      "correctly thinned plant with an open interior, but plenty of fan-leaf sources retained." +
      _c("massuela-2022-pruning-cbd-yield")),
    p("The second trap is <strong>overcrowding</strong>. Plants packed too close trigger a "
      "<strong>shade-avoidance response</strong>: sensing neighbours' shade, they waste energy "
      "stretching weak inner branches toward light instead of building flower" +
      _c("wang-2020-shade-avoidance") + ". Proper spacing means far less defoliation is needed, "
      "because the canopy was never a jungle to begin with."),
    p("A common starting point is about 2.3 sqft per plant, with a typical working range of "
      "1.8&ndash;3.0 sqft. Denser planting can raise total yield per area but reduces uniformity, so "
      "there is a real trade-off rather than a single &lsquo;correct&rsquo; number" +
      _c("danziger-2022-planting-density") + "."),
    figure(L.zones("Plant spacing: density zones (sqft per plant)",
            1.0, 3.5,
            [(1.0, 1.8, L.REDL, "too dense: shade avoidance"),
             (1.8, 3.0, L.GL, "working range"),
             (3.0, 3.5, L.AMBL, "sparse: wasted space")],
            unit=" sqft",
            note="Start around 2.3 sqft. Below ~1.8 sqft plants stretch and shade each other."), 12,
      "Spacing zones: too dense triggers shade avoidance" + _c("wang-2020-shade-avoidance") +
      ", the 1.8&ndash;3.0 sqft band is the usual working range, and correct spacing means far less "
      "plant work overall." + _c("danziger-2022-planting-density")),
    table(["Mistake", "What goes wrong", "Do this instead"], [
      ["Over-defoliating", "Removes the leaves feeding the buds; yield and potency drop", "Leave as many fan-leaf sources as possible; open just enough"],
      ["Overcrowding", "Shade-avoidance: weak, stretchy inner growth", "Space ~2.3 sqft/plant (1.8&ndash;3.0 range)"],
      ["Topping in flower", "Wounds the plant when it should be bulking", "Do all topping in veg"],
      ["Heavy defan late in bloom", "Stress with no time to recover", "Match aggressive work to early flower"],
      ["Musty smell, dying inner leaves", "Canopy too closed; bud-rot risk rising", "Improve airflow first, not strip every leaf"],
    ], cls="compact",
    caption="The common beginner traps. Note the last row: the fix for a stuffy canopy is airflow, "
            "not stripping it bare." + _c("mahmoud-2023-budrot-botrytis")),
    callout("danger", "Leaves are not the enemy",
      p("It is tempting to keep cutting until the plant looks &lsquo;clean.&rsquo; Resist it. Every "
        "fan leaf you remove was feeding flower. Open the canopy enough for light and air, then "
        "stop. If the room still smells musty, the answer is more airflow, not more cutting. Read the "
        "<a href='airflow-design.html'>airflow design</a> paper." +
        _c("massuela-2022-pruning-cbd-yield"))),
  ]})

SECTIONS.append({"id": "expectations", "kicker": "Reality check",
  "title": "Realistic expectations and how to learn your plants",
  "blocks": [
    p("Training and defoliation are real yield and quality levers, but they are not magic, and the "
      "numbers depend on your genetics, light and environment. Treat the whole approach as "
      "data-driven and iterative: expect to refine over about three runs of the same cultivar before "
      "you hit its sweet spot for yield and quality."),
    figure(L.line("Dialling in a cultivar over three runs",
            [(0, 100), (1, 118), (2, 128)],
            ["run 1", "run 2", "run 3"],
            ylab="yield/quality index", ymin=90, ymax=140,
            note="Same cultivar, same room: training and defoliation get tuned each run."), 13,
      "Yield and quality typically climb across the first three runs of a cultivar as you learn how "
      "it stretches and how much canopy work it actually wants."),
    p("Good planning of genetics and spacing is one of the cheapest gains available. Choosing "
      "the right plant count and layout can move yield per area and uniformity in ways that often matter more than expensive gear with no "
      "extra overhead, because uniformity and light interception both improve" +
      _c("danziger-2022-planting-density") + _c("anthony-2020-training-light-interception") + "."),
    ul(["Expect to refine over about 3 runs of a cultivar before you hit its yield/quality sweet spot.",
        "Good genetic planning and spacing can be worth 15&ndash;30% to the bottom line at no extra cost" +
        _c("danziger-2022-planting-density") + ".",
        "Not every strain needs every phase. The optional Phase 3 defan is decided per strain by observation.",
        "Track and photograph each run so changes are based on your own data, not generic advice.",
        "Slow-growing genetics behave differently and need a gentler, less aggressive hand."]),
    callout("key", "Three honest truths",
      ol(["<strong>There is no universal recipe.</strong> Start from this timeline and tune the day "
          "ranges and how much you remove to <em>your</em> genetics, light and room.",
          "<strong>Less is usually more.</strong> Leave the leaves that feed the plant; open the "
          "canopy just enough for light and air, then stop.",
          "<strong>Your camera is your best tool.</strong> Photograph the canopy each run; next-run "
          "decisions should come from what you actually saw, not a one-size-fits-all rule."])),
    p("Get the canopy flat and spread early, lollipop the base, defan only as much as light and air "
      "require, and write down what you did. That discipline, not any single magic cut, "
      "is what makes training and defoliation pay off. When you are ready to take the "
      "finished plant further, read the "
      "<a href='harvest-dry-trim-cure.html'>harvest, dry, trim and cure</a> paper next, and keep the "
      "<a href='mould-risk.html'>mould risk</a> guide handy through bloom."),
  ]})
