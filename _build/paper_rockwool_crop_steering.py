# -*- coding: utf-8 -*-
"""Paper: crop steering in rockwool, the dryback and saturation mechanics nobody explains."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        stagecard, grid, card, chip, kv, steps)
import figs_lib as L
from figs import GL, GXL, AMBL, REDL, BLUL
import figs_rockwool as R

SLUG = "rockwool-crop-steering"
TITLE = "Crop steering in rockwool: drybacks, saturation and the breaking point"
EYEBROW = "Feed · Rockwool steering"
SUB = ("Rockwool is the most controllable substrate there is, and the least forgiving. This is the "
       "guide to what water content really means, how to read and calculate dryback, how dry a block "
       "can get before it is gone, and how to hold the right saturation from clone to chop without "
       "ever hand-flushing or topping up a cube.")
META = [("droplet", "Feed & steering"), ("image", "7 diagrams"),
        ("quote", "Evidence-linked + Grodan/Netafim/Athena"), ("clock", "~18 min read")]
RELATED = ["coco-crop-steering", "root-zone-teros12", "f2-crop-steering", "irrigation-manual"]
REF_IDS = ["grodan-irrigation-medicinal", "owen-norden-preferential-flow-2024",
           "hydrus-soilless-substrate-dynamics", "moon-rootzone-ec-2018",
           "nemali-2006-set-point-irrigation", "tavan-2021-sensor-irrigation-soilless",
           "caplan2019-drought", "malik2025-media",
           "netafim-irrigation-maintenance", "athena-spacing-irrigation"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

# 1 -----------------------------------------------------------------
SECTIONS.append({"id": "intro", "kicker": "Start here", "title": "Why rockwool rewards and punishes you",
  "blocks": [
    lead("Rockwool (stone wool) is spun rock fibre. It holds no nutrients of its own and reacts with "
         "nothing you feed it, so <strong>root-zone EC is essentially the EC of the pore water (unused feed still leaves as runoff or concentrates on dryback)</strong>" + _c("grodan-irrigation-medicinal") +
         ". That makes it the most precise substrate you can steer with. It also means the block has no "
         "buffer: get the water wrong and the plant feels it the same hour."),
    p("This guide is only about the water and salt in the block, the part most growers run on feel. "
      "By the end you will know exactly what a water-content percentage is, how to calculate a dryback, "
      "the minimum you must feed, the point past which a dried-out block cannot be saved by the dripper, "
      "and how to hold the slab in the right zone for the whole grow using sensors and an irrigation "
      "controller, never a hose."),
    callout("key", "The one-paragraph version",
      p("Saturate the block, then let it lose a controlled amount of water each day (the "
        "<strong>dryback</strong>). The size and timing of that dryback is your main steering lever. "
        "Feed enough each day to refresh the salts and get a little runoff, but never let the block fall "
        "below its recovery floor (around <strong>25-30% water content</strong>), because below that it "
        "channels and will not rewet from a dripper" + _c("owen-norden-preferential-flow-2024") + ".")),
    callout("note", "Written for your kit",
      p("Assumes a slab-and-cube setup on pressure-compensating drippers, with a substrate moisture and "
        "EC sensor and an irrigation controller, the Athena-style 4&Prime; cube on a 3&times;6&times;36 "
        "slab being typical" + _c("athena-spacing-irrigation") + ". The smaller the dripper, the finer your "
        "control of the root zone" + _c("athena-spacing-irrigation") + ".")),
  ]})

# 2 -----------------------------------------------------------------
SECTIONS.append({"id": "terms", "kicker": "Vocabulary", "title": "The words you need",
  "blocks": [
    defterm("Water content (WC%)", "The share of the block's volume that is water right now, as a "
            "percentage. A slab at 70% WC is 70% full of water by volume. This single number is what "
            "you steer."),
    defterm("Saturation / field capacity", "Saturation is the block as full as it can get just after "
            "irrigating. Field capacity is what it settles back to once free water has drained out. Your "
            "daily peak sits around field capacity."),
    defterm("Dryback", "The drop in water content between the daily peak and the next low, caused by the "
            "plant drinking and by evaporation. Measured in percentage points of WC."),
    defterm("Dryback %", "The size of that drop. Can be stated as <em>points</em> (peak 75% to trough "
            "55% = a 20-point dryback) or as a <em>fraction of the peak</em>. This guide uses points "
            "unless it says otherwise."),
    defterm("Runoff (drain / leachate)", "The feed that exits the bottom of the block. A small daily "
            "runoff flushes built-up salt and tells you the EC inside the block."),
    defterm("Substrate EC", "The salt strength of the water <em>inside</em> the block. This, not the "
            "dripper or drain EC, is what the plant actually experiences" + _c("grodan-irrigation-medicinal") +
            " and what you steer to" + _c("moon-rootzone-ec-2018") + "."),
    defterm("Recovery floor", "The lowest water content a block can reach and still rewet evenly from "
            "the dripper. Below it the fibre channels and the core stays dry."),
    defterm("Channeling / preferential flow", "When water runs down a few open paths instead of "
            "spreading through the fibre, so it exits as runoff while the core stays dry" + _c("owen-norden-preferential-flow-2024") + "."),
    defterm("Generative vs vegetative steering", "Drier, bigger drybacks push the plant generative "
            "(toward flower and fruit). Wetter, smaller drybacks keep it vegetative (leafy growth)" + _c("caplan2019-drought") + "."),
    defterm("Shot", "A single timed irrigation pulse. Shot size and spacing build the daily water-content "
            "curve."),
  ]})

# 3 -----------------------------------------------------------------
SECTIONS.append({"id": "anatomy", "kicker": "How it works", "title": "Where the water actually sits",
  "blocks": [
    p("A rockwool block is mostly air. Around 95% of its volume is space between the fibres; the fibre "
      "itself is a tiny fraction" + _c("malik2025-media") + ". Water clings to the fibres as a film and fills "
      "the smaller gaps, while the larger gaps stay full of air. Water content is simply how much of that "
      "space is water versus air at any moment."),
    figure(R.fig_cube_anatomy(), 1,
      "Water held as a film on the fibres is your WC%. The air between fibres is root oxygen. Because the "
      "fibre carries almost no electrical charge (its cation-exchange capacity is near zero), dissolved "
      "salts stay in the water and nothing is held back from the plant" + _c("grodan-irrigation-medicinal") + "."),
    p("Two consequences fall straight out of this. First, when water leaves the block the salt does not, "
      "so the EC of the water left behind climbs as the block dries. Second, because the medium buffers "
      "nothing, the EC and water content you set are the EC and water content the roots get, which is why "
      "rockwool can be steered so precisely and why mistakes show up so fast."),
  ]})

# 4 -----------------------------------------------------------------
SECTIONS.append({"id": "water-content", "kicker": "The number", "title": "What a water-content percentage means",
  "blocks": [
    p("Everything in rockwool steering is a position on one vertical scale: how full the block is. Learn "
      "the band and where the danger is, and the rest is timing."),
    figure(R.fig_wc_band(), 2,
      "The working band runs roughly 55-92% WC. Vegetative and bulking phases sit high; generative pushes "
      "ride lower. The dashed line near 30% is the recovery floor, fall below it and the block channels."),
    callout("note", "These are starting numbers, not laws",
      p("Grodan is explicit that medicinal cultivars are highly variable, so there is no single correct "
        "water content" + _c("grodan-irrigation-medicinal") + ". Treat every figure here as a starting point you "
        "confirm against your own slabs and sensor.")),
    p("Note where the headroom is. The block can sit happily anywhere from field capacity down into the "
      "mid-40s. The cliff is only at the bottom. That asymmetry is the whole reason a controlled dryback "
      "is safe but an uncontrolled one is fatal."),
  ]})

# 5 -----------------------------------------------------------------
_curve = [(0, 70), (1, 66), (2, 62), (3, 59), (4, 56), (5, 57), (6, 65),
          (7, 73), (8, 79), (9, 77), (10, 78), (11, 76), (12, 71)]
_curve_x = ["off", "", "", "", "pre-dawn low", "on · P0", "P1", "", "FC", "P2", "", "P3", "off"]
SECTIONS.append({"id": "dryback", "kicker": "The main lever", "title": "Dryback: what it is, and how to calculate it",
  "blocks": [
    p("A dryback is the block losing water between its daily high and its next low. You create the high by "
      "irrigating to field capacity; the plant and evaporation create the low. The <em>size</em> of that "
      "swing and <em>when</em> you let it happen is the single biggest lever you have over how the plant "
      "grows."),
    figure(L.line("A day in the life of a slab", _curve, _curve_x, ylab="water content %",
            ymin=0, ymax=100,
            bands=[(55, 92, GL, "working band"), (0, 30, REDL, "non-recoverable")],
            note="Overnight P3 dryback to a pre-dawn low, a short P0 morning dryback at lights-on, a P1 ramp back to field capacity, a P2 maintenance plateau, then the last shot into the P3 overnight dryback."), 3,
      "One daily cycle. The trough never approaches the floor, the peak refreshes the block. The gap "
      "between peak and trough is the dryback."),
    callout("key", "How to calculate a dryback",
      p("Dryback in points = <strong>peak WC &minus; trough WC</strong>. If the slab peaks at 78% and "
        "drops to 58% before the next irrigation, that is a <strong>20-point dryback</strong>. As a "
        "fraction of the peak it is 20 &divide; 78 = <strong>26%</strong>. Either way, your sensor gives "
        "you both numbers directly, read the high after the last shot and the low just before the next.")),
    table(["Phase", "Typical daily dryback", "What it steers"],
      [["Propagation / early veg", "5-10 points", "Roots chase water, gentle"],
       ["Late veg / bulk (wet)", "10-15 points", "Maximum growth, vegetative"],
       ["Generative flower push", "20-30 points", "Stacks flower, slows stretch"],
       ["Overnight (any phase)", "add 5-15 points", "Re-oxygenates the root zone"]],
      caption="Dryback sizes as a starting framework. Bigger and earlier is more generative; smaller and later is more vegetative."),
    callout("note", "Why the night dryback matters",
      p("As the block dries overnight, air refills the gaps and the roots and beneficial microbes get "
        "oxygen. Grodan's trials found that easing the standard night dryback by about 10% (a slightly "
        "wetter night) lifted yield in medicinal crops, because the root zone keeps working even while "
        "the canopy rests" + _c("grodan-irrigation-medicinal") + ". Some night dryback is essential; too much is not.")),
  ]})

# 6 -----------------------------------------------------------------
SECTIONS.append({"id": "dryout", "kicker": "The physics", "title": "What happens to a block as it dries",
  "blocks": [
    p("A dryback is good up to a point and dangerous past it. The same process, water leaving the block, "
      "does four different things in sequence as it goes too far."),
    figure(R.fig_dryout(), 4,
      "Stages 1-2 are the healthy dryback you want: water leaves, air and oxygen enter. Stage 3 is too "
      "far: with less water but the same salt, the EC inside the block climbs and the plant feels osmotic "
      "stress" + _c("hydrus-soilless-substrate-dynamics") + ". Stage 4 is past the floor: a dry core forms and water "
      "channels around it."),
    p("The middle stage is the one that catches people out. Because rockwool holds no salt of its own, the "
      "salt that was dissolved in the water stays put while the water disappears. A block drying from 75% "
      "to 45% WC keeps only about three-fifths of its water (45 &divide; 75), so the salt left behind "
      "concentrates by the inverse, roughly two-thirds higher, because EC rises as 1 divided by the "
      "fraction of water remaining" + _c("hydrus-soilless-substrate-dynamics") + ". A 3.0 EC feed can climb past 5.0 "
      "EC in the root zone by late afternoon. That is why big drybacks must be paired with enough volume and "
      "runoff to keep the salt in check, covered below."),
    callout("warn", "Dryback stress is partly salt stress",
      p("When you push a generative dryback, you are not only making the plant work for water, you are "
        "also concentrating its food. Watch substrate EC, not just water content. If EC climbs faster than "
        "you intend on the dryback, shrink the dryback or lower the feed EC.")),
  ]})

# 7 -----------------------------------------------------------------
SECTIONS.append({"id": "breaking-point", "kicker": "The cliff", "title": "The breaking point: when a block is gone",
  "blocks": [
    p("There is a water content below which a rockwool block will not rewet from the dripper no matter how "
      "long you run it. This is the single most important thing in this guide, because it is invisible "
      "until it has already happened."),
    figure(R.fig_rewet(), 5,
      "A block still in the working band rewets evenly: water spreads through the moist fibre. A block "
      "taken too dry develops a dry core that the fibre can no longer pull water into. New water finds the "
      "few open channels, runs straight down them and exits as runoff while the core stays bone "
      "dry" + _c("owen-norden-preferential-flow-2024") + "."),
    p("Below roughly <strong>25-30% WC</strong> the dry fibre stops wicking and preferential flow takes "
      "over" + _c("owen-norden-preferential-flow-2024") + _c("hydrus-soilless-substrate-dynamics") + ". The drip rate that kept a "
      "healthy block topped up cannot re-saturate a dry one, because the water never contacts the dry "
      "interior. Your runoff reads high and your sensor barely moves, the classic signature of a channeling "
      "block."),
    callout("danger", "If a block has gone too dry",
      ul(["Stop trusting the dripper to fix it. More drip just makes more runoff.",
          "Rehydrate by hand or by flooding: a long, slow, low-volume soak (or sitting the block in "
          "shallow feed) until the core takes water back, sometimes over hours.",
          "Then return to a normal schedule and find out why it dried out: a clogged dripper, a missed "
          "P1 ramp, a dead controller, or a dryback set too deep.",
          "A block that has been to the floor repeatedly develops permanent dry pockets and uneven "
          "wetting. Replace it rather than fight it."], "tight")),
    callout("key", "The rule that prevents all of this",
      p("Set a hard minimum water content in your controller and never let the trough cross it. The dryback "
        "is steering; the floor is a safety limit. They are not the same number and you should know both "
        "for every slab.")),
  ]})

# 8 -----------------------------------------------------------------
SECTIONS.append({"id": "minimum-feed", "kicker": "How much", "title": "The minimum you must feed",
  "blocks": [
    p("Feeding rockwool is a balance of two jobs: put back the water the plant drank, and flush enough "
      "fresh feed through to stop salt stacking. Underfeed and EC climbs and the block trends toward the "
      "floor; overfeed and you drown the roots and lose your dryback."),
    steps([
      ("Size each shot to a few points of WC", "A single shot should lift water content by roughly 2-5 "
       "points. Big enough to register on the sensor, small enough not to blow straight to runoff."),
      ("Reach field capacity in the P1 ramp", "Stack several shots after lights-on to climb from the "
       "overnight low back up to field capacity, then hold it."),
      ("Get a small daily runoff", "Aim for around 10-20% runoff once the block is at field capacity. "
       "That runoff is how you flush stacked salt and how you read substrate EC" + _c("grodan-irrigation-medicinal") + "."),
      ("Use runoff EC as the feedback", "If substrate or runoff EC is climbing day over day, you are not "
       "flushing enough, increase shot size or frequency. If EC is falling below target, cut runoff back."),
      ("Never let the trough hit the floor", "Whatever the dryback, the pre-irrigation low must stay above "
       "the recovery floor with margin."),
    ]),
    figure(L.bars("Where a feed's water goes, by phase",
      [("Prop", 4), ("Veg/wet", 14), ("Bulk", 18), ("Generative", 12)], unit="%",
      note="Indicative daily runoff target as a share of feed volume. Higher runoff flushes more salt; too little lets EC stack."),
      6, "Runoff is not waste, it is your salt-management and measurement tool. Size the daily feed so a "
      "controlled fraction drains."),
    callout("note", "Minimum feed is a floor, not a target",
      p("The minimum is whatever volume keeps the block above its recovery floor and substrate EC on "
        "target. In heavy flower under high light that can be a lot of small shots; in propagation it is "
        "very little. Let the sensor and the runoff EC set the number, not a fixed clock" + _c("nemali-2006-set-point-irrigation") + ".")),
  ]})

# 9 -----------------------------------------------------------------
SECTIONS.append({"id": "steering", "kicker": "The lever in use", "title": "Generative vs vegetative, in rockwool",
  "blocks": [
    p("You steer the plant by choosing where the block sits in the band, how big the daily dryback is, and "
      "when you let it happen. Drier and bigger and earlier is generative; wetter and smaller and later is "
      "vegetative" + _c("caplan2019-drought") + "."),
    table(["Lever", "Vegetative (leafy growth)", "Generative (flower / fruit)"],
      [["Daily peak WC", "High, near field capacity", "Lower, mid-band"],
       ["Dryback size", "Small, 5-15 points", "Large, 20-30 points"],
       ["First shot after lights-on", "Early, short ramp", "Delayed, longer overnight dryback"],
       ["Substrate EC", "Lower end of target", "Higher, concentrated by the dryback"],
       ["When to use", "Early flower, bulking, recovery", "Stretch control, flower set, ripening"]],
      caption="The same three controls (peak, dryback, timing) produce both behaviours. You are not changing the feed, you are changing the water curve."),
    callout("note", "Feed generously through the front half of flower",
      p("Grodan's trials found a consistently wetter daytime strategy produced higher yield with the same "
        "cannabinoid levels, especially across the first six of eight flowering weeks" + _c("grodan-irrigation-medicinal") +
        ". Steer generative with timing and dryback, but do not starve the plant of water and feed while "
        "it is still building the crop.")),
  ]})

# 10 -----------------------------------------------------------------
_season = [(0, 8), (1, 10), (2, 12), (3, 15), (4, 20), (5, 24), (6, 26), (7, 22)]
_season_x = ["Clone", "Veg", "Wk1", "Wk2", "Wk3", "Wk4-5", "Wk6", "Wk7-8"]
SECTIONS.append({"id": "maintain", "kicker": "Start to finish", "title": "Holding saturation the whole grow, no hand-flushing",
  "blocks": [
    p("The goal is to never touch a hose: the controller holds the block in the right zone from clone to "
      "chop, flushing salt with daily runoff so you never have to manually leach or top up a dry cube. The "
      "strategy is a planned arc of water content and dryback across the grow."),
    figure(L.line("Dryback grows as the grow matures", _season, _season_x, ylab="target dryback (points)",
            ymin=0, ymax=35,
            note="Small drybacks while building the plant; deeper, more generative drybacks once the crop is set, easing slightly at the very end."),
      7, "An indicative dryback arc. Stay wet and gentle early to build the plant, push drier and more "
      "generative once flower is established, then steady it for ripening" + _c("grodan-irrigation-medicinal") + "."),
    table(["Stage", "Daily peak WC", "Dryback", "Substrate EC", "Runoff"],
      [["Clone / prop", "High, gentle", "5-10 pts", "Start higher than you'd think", "Minimal"],
       ["Veg", "High", "10-15 pts", "Step up", "Low, 5-10%"],
       ["Flower wk 1-3", "High (wet, bulking)", "10-18 pts", "Step up again", "10-15%"],
       ["Flower wk 4-6", "Mid", "20-30 pts", "Highest", "15-20% to flush"],
       ["Flower wk 7-8", "Mid, steady", "18-25 pts", "Ease / as planned", "Maintain"]],
      caption="A complete arc. EC climbs by stage because rockwool is inert and the plant's appetite rises with light" + _c("grodan-irrigation-medicinal") + ". Runoff rises to flush the higher salt load."),
    callout("key", "Why this removes hand-flushing",
      p("A daily controlled runoff continuously replaces the salty water in the block with fresh feed, so "
        "EC never stacks to the point of needing a manual leach. And because the trough never crosses the "
        "recovery floor, no cube ever dries out enough to need a manual soak. The system holds the "
        "equilibrium for you, every day, if you set the limits correctly.")),
  ]})

# 11 -----------------------------------------------------------------
SECTIONS.append({"id": "systems", "kicker": "The kit", "title": "Running it on sensors and a controller",
  "blocks": [
    p("None of this works on a timer alone. Steering rockwool means measuring the block and letting the "
      "controller act on the measurement, closing the loop" + _c("nemali-2006-set-point-irrigation") + _c("tavan-2021-sensor-irrigation-soilless") + "."),
    ul([
      "<strong>Measure inside the block.</strong> A substrate sensor reads water content and EC where the "
      "roots are. Steer to substrate EC, not dripper or drain EC" + _c("grodan-irrigation-medicinal") + _c("moon-rootzone-ec-2018") + ".",
      "<strong>Let the controller hold the curve.</strong> The irrigation controller runs the P1 ramp to "
      "field capacity, the P2 maintenance shots, and the P0/P3 dryback windows automatically, to "
      "water-content set-points rather than fixed times" + _c("nemali-2006-set-point-irrigation") + ".",
      "<strong>Set the safety floor in software.</strong> A hard minimum water content the controller will "
      "always irrigate to defend, so the block can never reach the channeling point even if a dryback is "
      "set too deep.",
      "<strong>Watch the runoff EC daily.</strong> It is your early warning that salt is stacking or that "
      "you are over-flushing.",
    ]),
    p("The companion papers cover the hardware and the daily cycle in depth: what the substrate sensor "
      "actually sees, how the watering brain decides, the P0-P3 cycle itself, and how to install and run "
      "the system."),
    callout("note", "The point of precision",
      p("Because rockwool buffers nothing, a closed-loop controller can steer it to a tighter tolerance "
        "than any buffered medium" + _c("grodan-irrigation-medicinal") + ". The inertness that makes it unforgiving is "
        "exactly what makes it the best substrate to automate.")),
  ]})

# 12 -----------------------------------------------------------------
SECTIONS.append({"id": "troubleshooting", "kicker": "When it goes wrong", "title": "Reading the block's symptoms",
  "blocks": [
    table(["Symptom", "Likely cause", "Fix"],
      [["Runoff high, sensor barely moves", "Block channeling, core too dry", "Hand-soak to rewet, then raise the floor and check drippers"],
       ["Substrate EC climbing day over day", "Not enough runoff, salt stacking", "Bigger or more frequent shots to lift daily runoff"],
       ["Substrate EC falling below target", "Over-flushing, too much runoff", "Cut shot size or frequency"],
       ["WC won't reach field capacity", "Shots too small, clogged dripper, or P1 too short", "Check drippers, lengthen the P1 ramp" + _c("netafim-irrigation-maintenance")],
       ["Dryback far bigger than set", "Plant drinking hard under high light, or a missed shot", "Add P2 shots; verify controller and sensor"],
       ["Slabs uneven across the room", "Dripper flow or placement varies", "Flush and check lines" + _c("netafim-irrigation-maintenance") + "; match dripper count to slab" + _c("athena-spacing-irrigation")]],
      caption="Most rockwool problems are a water-content or EC reading drifting from plan. The sensor tells you which, and the fix follows."),
  ]})

# 13 -----------------------------------------------------------------
SECTIONS.append({"id": "quick-reference", "kicker": "Cheat sheet", "title": "The numbers, in one place",
  "blocks": [
    kv([("Working band", "~55-92% WC"),
        ("Recovery floor (do not cross)", "~25-30% WC"),
        ("Shot size", "lift WC ~2-5 points"),
        ("Daily runoff", "~10-20% at field capacity"),
        ("Vegetative dryback", "5-15 points"),
        ("Generative dryback", "20-30 points"),
        ("EC by stage", "rises prop -> veg -> flower"),
        ("Steer EC to", "the substrate reading, not drain")]),
    callout("key", "The whole method in five lines",
      ul(["Saturate to field capacity each morning with a P1 ramp.",
          "Hold it through the day with P2 maintenance shots and a small runoff.",
          "Let a planned dryback happen, sized to how generative you want to steer.",
          "Never let the trough cross the recovery floor.",
          "Steer to substrate EC and water content, read off the sensor, run by the controller."], "tight")),
  ]})
