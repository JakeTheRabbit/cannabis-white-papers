# -*- coding: utf-8 -*-
"""Paper: airflow design for indoor cultivation (beginner)."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        stagecard, grid, card, chip, kv, steps)
import figs_lib as L
from figs import G, GD, GL, GXL, INK, INK2, MUT, LINE, AMB, AMBL, RED, BLU, BLUL, PAPER, FS, MN

SLUG = "airflow-design"
TITLE = "Airflow design for indoor cultivation"
EYEBROW = "Beginner · Airflow design"
SUB = ("Every leaf sits inside a film of still air that limits how fast it can breathe. "
       "Airflow strips that film away. Done right it feeds the plant and dries the room. "
       "Done wrong it scorches leaves or breeds rot.")
META = [("wind", "Beginner"), ("image", "3 diagrams"),
        ("quote", "Peer-reviewed · 9 sources"), ("clock", "~14 min read")]
RELATED = ["grow-room-systems", "mould-risk", "coco-crop-steering"]
REF_IDS = ["schuepp1993-bl", "dupont2025-wind", "kitaya2004-airvel", "tjosvold2018-air",
           "rm2021-light", "kitaya2010-circ", "gilliham2011-ca", "chehab2009-thigmo",
           "chandra2008-photo"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

def _fig_boundary():
    W, H = 720, 300
    p = [f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Leaf boundary layer">']
    p.append(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')
    p.append(f'<text x="24" y="30" fill="{INK}" font-size="15" font-weight="700" style="{FS}">The boundary layer: a film of still, humid air on every leaf</text>')
    # leaf
    lx, ly = 150, 170
    p.append(f'<ellipse cx="{lx+120}" cy="{ly}" rx="150" ry="20" fill="{GL}" stroke="{G}" stroke-width="2"/>')
    p.append(f'<text x="{lx+120}" y="{ly+5}" text-anchor="middle" fill="{GD}" font-size="12" font-weight="700" style="{FS}">leaf surface</text>')
    # boundary layer (still air), shaded band hugging the leaf
    p.append(f'<path d="M{lx-25},{ly-10} q145,-34 290,0 q-145,30 -290,0 Z" fill="{BLUL}" opacity=".8"/>')
    p.append(f'<text x="{lx+120}" y="{ly-22}" text-anchor="middle" fill="{BLU}" font-size="11.5" style="{FS}">still-air film (boundary layer)</text>')
    # CO2 struggling across (left, thick film)
    p.append(f'<text x="60" y="120" fill="{AMB}" font-size="12" font-weight="700" style="{FS}">CO&#8322;</text>')
    p.append(f'<path d="M70,128 q10,20 12,34" fill="none" stroke="{AMB}" stroke-width="2" stroke-dasharray="3 3" marker-end="url(#a1)"/>')
    p.append(f'<text x="40" y="150" fill="{MUT}" font-size="10.5" style="{FS}">thick film =</text>')
    p.append(f'<text x="40" y="164" fill="{MUT}" font-size="10.5" style="{FS}">slow breathing</text>')
    # moving air (right) thinning the film
    for yy in (96, 112, 128):
        p.append(f'<path d="M470,{yy} q120,0 200,2" fill="none" stroke="{G}" stroke-width="2.4" marker-end="url(#a2)"/>')
    p.append(f'<text x="560" y="80" text-anchor="middle" fill="{GD}" font-size="12" font-weight="700" style="{FS}">moving air thins it</text>')
    p.append(f'<text x="560" y="250" text-anchor="middle" fill="{INK2}" font-size="11.5" style="{FS}">&rarr; CO&#8322; in, water + heat out, faster</text>')
    p.append(f'<defs><marker id="a1" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="{AMB}"/></marker>'
             f'<marker id="a2" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="{G}"/></marker></defs>')
    p.append('</svg>')
    return "".join(p)

SECTIONS = []

SECTIONS.append({"id": "start", "kicker": "01 · Read this first", "title": "Why airflow is not optional",
  "blocks": [
    lead("Airflow is plumbing for gases, and it is as important as light and feed. Without moving "
         "air, even a perfect light and a perfect feed cannot reach the leaf properly. A still, "
         "humid canopy is exactly where bud rot begins."),
    p("This guide explains, from zero, what air movement does at the leaf, how much you want, and "
      "how to lay out a room so every plant gets it."),
  ]})

SECTIONS.append({"id": "terms", "kicker": "02 · The vocabulary", "title": "The words you need",
  "blocks": [
    defterm("Boundary layer", "The thin film of still air that clings to every leaf surface. Gases "
            "have to diffuse across it slowly, so it is the bottleneck airflow attacks."),
    defterm("Air velocity", "How fast air is moving at the canopy, in metres per second (m/s). This "
            "is what matters, not how big your fan is."),
    defterm("Laminar vs turbulent", "Laminar = smooth, layered airflow (like a calm jet). Turbulent "
            "= messy, mixing airflow. For leaves, messy is better."),
    defterm("Transpiration", "The plant drinking water at the roots and releasing it as vapour from "
            "the leaves. Airflow speeds it up by clearing the humid film."),
    defterm("Air exchange", "Swapping room air with fresh air (intake/exhaust). Different from "
            "recirculation, which only stirs the air already in the room."),
  ]})

SECTIONS.append({"id": "boundary", "kicker": "03 · The core idea", "title": "The invisible skin of still air",
  "blocks": [
    p("Air right against a leaf barely moves. It forms a stagnant film called the "
      "<strong>boundary layer</strong>. CO2 going in, and water vapour and heat coming out, all have "
      "to crawl across that film by slow diffusion. The thicker it is, the more it slows the "
      "leaf" + _c("schuepp1993-bl") + "."),
    figure(_fig_boundary(), 1,
      "Still air insulates the leaf and slows every exchange. Moving air thins the boundary layer so "
      "CO2 gets in faster and water and heat get out faster" + _c("dupont2025-wind") + "."),
    p("Moving air thins that film. Even small breezes make a real difference: gentle wind "
      "(under ~0.2 m/s added) has been shown to lift daytime photosynthesis by 10–20%" + _c("dupont2025-wind") +
      ". This is the reason fans belong in a grow room."),
  ]})

SECTIONS.append({"id": "how-much", "kicker": "04 · The target", "title": "How much air is the right amount?",
  "blocks": [
    p("More airflow helps, but with sharply diminishing returns. Photosynthesis climbs "
      "steeply as you go from dead-still up to a gentle breeze, then flattens out. Most of the "
      "benefit is won by the time leaves are gently fluttering" + _c("kitaya2004-airvel") + "."),
    figure(L.line("Airflow vs leaf gas exchange: steep early, flat later",
            [(0, 12), (1, 48), (2, 74), (3, 86), (4, 91), (5, 93)],
            ["still", "0.2", "0.4", "0.6", "0.8", "1.0+"],
            ylab="relative gas exchange", ymin=0, ymax=100,
            note="Air velocity at the leaf (m/s). The big wins come early. Past a gentle breeze you gain little."), 2,
      "Gas exchange rises fast then plateaus" + _c("kitaya2004-airvel") + ". The practical target is a "
      "<strong>gentle, constant breeze</strong>. Leaves should flutter slightly, not thrash."),
    figure(L.zones("Air-velocity target at the canopy", 0, 2.0,
            [(0, 0.2, AMBL, "too still: rot risk"), (0.3, 1.0, GL, "sweet spot"),
             (1.3, 2.0, AMBL, "too windy: wind-burn")], unit=" m/s",
            note="Aim for roughly 0.3–1.0 m/s moving through the canopy. A flutter, not a gale."), 3,
      "Below ~0.2 m/s, humid pockets and disease creep in. Above ~1.2 m/s you risk wind-stress and "
      "drying the plants out. Aim for the middle." + _c("tjosvold2018-air")),
  ]})

SECTIONS.append({"id": "match-light", "kicker": "05 · The link", "title": "Match airflow to your light",
  "blocks": [
    p("The brighter the room, the more the leaf needs air. High light drives high photosynthesis and "
      "high transpiration, and both depend on the boundary layer staying thin. Cannabis yield keeps "
      "rising with light to very high levels" + _c("rm2021-light") + ", but only if airflow and "
      "climate scale with it. A bright room with weak airflow wastes the light."),
    callout("key", "Airflow moves with the rest of the room",
      p("Light, CO2, temperature, humidity and airflow work together (see the "
        "<a href='grow-room-systems.html'>systems guide</a>). Turning up the light without turning up "
        "the air leaves hot leaves sitting in their own humid film" + _c("chandra2008-photo") + ".")),
  ]})

SECTIONS.append({"id": "transpiration", "kicker": "06 · The trade-off", "title": "Faster air means a hungrier plant",
  "blocks": [
    p("Thinning the boundary layer feeds CO2 in and pulls water out faster. More "
      "airflow means more transpiration, which means the plant needs more water and nutrient at the "
      "roots. There are two beginner gotchas here:"),
    ul([
      "<strong>Calcium tip-burn.</strong> Calcium rides into the leaf on the transpiration stream, "
      "so uptake tracks water flow" + _c("gilliham2011-ca") + ". Crank the airflow and under-feed, "
      "and you get calcium-deficiency tip-burn even with plenty in the tank. Fix: feed to "
      "match the airflow, not the other way round.",
      "<strong>Sturdier plants (a good thing).</strong> Air movement is a mechanical signal. Plants "
      "that feel a breeze grow shorter, thicker, stronger stems, an effect called "
      "thigmomorphogenesis" + _c("chehab2009-thigmo") + ". A well-aired plant holds heavy colas without "
      "staking.",
    ]),
  ]})

SECTIONS.append({"id": "build", "kicker": "07 · The layout", "title": "Building the room: two jobs, two systems",
  "blocks": [
    p("The two air jobs are different, and you need both:"),
    grid([
      card("Recirculation (mixing)", p("Oscillating or clip fans that stir the air already in the "
        "room so every leaf gets that gentle breeze and no humid dead-zones form. This is the "
        "boundary-layer job" + _c("kitaya2010-circ") + "."), tag="Inside the room"),
      card("Air exchange (in/out)", p("Intake and exhaust that swap stale, humid, CO2-depleted room "
        "air for fresh air. This is the climate &amp; humidity job. It removes the water the "
        "plants transpire."), tag="Room ↔ outside"),
    ], cols=2),
    callout("warn", "Mind the dead zones",
      p("Air takes the easy path and skips corners, the lower canopy, and the inside of dense "
        "plants. Those still, humid pockets are where bud rot starts. Place fans to push air "
        "<em>through</em> the canopy, not just over the top of it, and defoliate enough to let air in.")),
  ]})

SECTIONS.append({"id": "messy", "kicker": "08 · A subtlety", "title": "Messy air beats smooth air",
  "blocks": [
    p("Aiming one big fan straight down a row is tempting. Don't. A smooth, laminar jet builds its "
      "own thick boundary layer on whatever it hits, and leaves everything off-axis still. "
      "<strong>Turbulent, mixing air</strong>, from many fans at varied angles with oscillation, "
      "constantly disturbs the film on every leaf from every direction, which is exactly what thins "
      "it best" + _c("schuepp1993-bl") + _c("dupont2025-wind") + "."),
    callout("tip", "The flutter test",
      p("Walk the room. Every leaf, top to bottom and inside the plants, should be gently moving. "
        "Still leaves anywhere = a pocket you need to reach. A leaf that is flapping hard = back that "
        "fan off.")),
  ]})

SECTIONS.append({"id": "trouble", "kicker": "09 · When it goes wrong", "title": "Troubleshooting",
  "blocks": [
    table(["Symptom", "Likely cause", "What to do"], [
      ["Bud rot starting deep in colas", "Dead-zone: air not reaching the canopy interior", "Add through-canopy airflow, defoliate, lower RH"],
      ["Leaf-tip burn despite full tank", "Airflow outran nutrient delivery (calcium)", "Raise feed/EC to match transpiration"],
      ["Leaves clawing / wind-burnt edges", "Air velocity too high / fan pointed at plants", "Reduce speed, aim fans to mix, not blast"],
      ["Tall, weak, floppy stems", "Too little air movement: no mechanical signal", "Add gentle constant breeze across the canopy"],
      ["Room humidity stuck high", "Recirculation OK but not enough air exchange", "Increase intake/exhaust / dehumidification"],
    ], cls="compact"),
  ]})

SECTIONS.append({"id": "expect", "kicker": "10 · Straight talk", "title": "Realistic expectations",
  "blocks": [
    callout("key", "What to remember",
      ol(["Airflow's job is to <strong>thin the boundary layer</strong> on every leaf. That is the whole game.",
          "Aim for a <strong>gentle, turbulent breeze (~0.3–1.0 m/s)</strong> everywhere, including inside the plants.",
          "More air = more thirst: <strong>feed and humidity must keep up</strong>" + _c("gilliham2011-ca") + ".",
          "Most benefit comes early. You do not need a wind tunnel" + _c("kitaya2004-airvel") + "."])),
    p("Airflow is one subsystem of the room. Read it alongside the "
      "<a href='grow-room-systems.html'>systems guide</a> and the "
      "<a href='mould-risk.html'>mould risk</a> paper."),
  ]})
