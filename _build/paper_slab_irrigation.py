# -*- coding: utf-8 -*-
"""Paper: slab irrigation end to end - block-on-slab rooting-in, the daily cycle,
the week-by-week schedule, and salt management."""
from components import (p, lead, ul, ol, callout, defterm, table, steps,
                        figure, grid, card, kv)

SLUG = "slab-irrigation-strategy"
TITLE = "Slab irrigation, end to end"
EYEBROW = "Feed · Slab steering"
SUB = ("The complete watering strategy for blocks on slabs: why a soaked slab starves a fresh "
       "block, the rooting-in procedure that prevents it, the P0-P3 daily cycle, the week-by-week "
       "schedule to chop, and how to flush without ever touching a hose.")
META = [("droplet", "Feed & steering"), ("image", "3 diagrams"),
        ("quote", "Evidence-linked + Grodan/Athena"), ("clock", "~25 min read")]
RELATED = ["rockwool-crop-steering", "irrigation-manual", "root-zone-teros12", "f2-crop-steering"]

REF_IDS = [
    "grodan-block-slab-interaction",     # 1
    "grodan-slab-handling",              # 2
    "grodan-drainage-stages",            # 3
    "grodan-irrigation-medicinal",       # 4
    "bougoul2006-slab-density",          # 5
    "bougoul2005-stonewool-hydraulic",   # 6
    "dasilva1998-slab-distribution",     # 7
    "hydrus-soilless-substrate-dynamics",# 8
    "caplan2019-drought",                # 9
    "malik2025-media",                   # 10
    "nemali-2006-set-point-irrigation",  # 11
    "owen-norden-preferential-flow-2024",# 12
    "athena-spacing-irrigation",         # 13
    "netafim-irrigation-maintenance",    # 14
    "wtg-e37-bones",                     # 15
    "wtg-e31-sipkoi",                    # 16
]


def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)


# ---------------------------------------------------------------- figures

FIG_MATRIC = """<svg width="660" viewBox="0 0 660 320" style="max-width:100%" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="si-slabwet" x1="0" y1="1" x2="0" y2="0">
      <stop offset="0" stop-color="var(--fig-water)"/><stop offset="1" stop-color="var(--fig-waterl)"/>
    </linearGradient>
    <linearGradient id="si-blockdry" x1="0" y1="1" x2="0" y2="0">
      <stop offset="0" stop-color="var(--fig-waterl)"/><stop offset="1" stop-color="var(--fig-dryl)"/>
    </linearGradient>
    <marker id="si-arr" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
      <path d="M0 0 L8 4 L0 8 z" fill="var(--fig-red)"/>
    </marker>
  </defs>
  <text x="140" y="26" fill="var(--fig-ink)" font-size="13" font-weight="600" text-anchor="middle">Day 0 &#8212; block placed</text>
  <rect x="30" y="180" width="220" height="70" rx="4" fill="url(#si-slabwet)" stroke="var(--fig-line)"/>
  <rect x="95" y="100" width="90" height="80" rx="4" fill="var(--fig-waterl)" stroke="var(--fig-line)"/>
  <text x="140" y="146" fill="var(--fig-ink2)" font-size="11.5" text-anchor="middle">block, wet</text>
  <text x="140" y="222" fill="#fff" font-size="11.5" text-anchor="middle">slab at field capacity</text>
  <text x="440" y="26" fill="var(--fig-ink)" font-size="13" font-weight="600" text-anchor="middle">Day 1&#8211;2 &#8212; block not watered</text>
  <rect x="330" y="180" width="220" height="70" rx="4" fill="url(#si-slabwet)" stroke="var(--fig-line)"/>
  <rect x="395" y="100" width="90" height="80" rx="4" fill="url(#si-blockdry)" stroke="var(--fig-line)"/>
  <text x="440" y="136" fill="var(--fig-ink2)" font-size="11.5" text-anchor="middle">block drains</text>
  <text x="440" y="152" fill="var(--fig-ink2)" font-size="11.5" text-anchor="middle">into the slab</text>
  <path d="M440 186 v26" stroke="var(--fig-red)" stroke-width="2.5" fill="none" marker-end="url(#si-arr)"/>
  <text x="440" y="232" fill="#fff" font-size="11.5" text-anchor="middle">slab still full</text>
  <line x1="585" y1="100" x2="585" y2="250" stroke="var(--fig-mut)" stroke-width="1" stroke-dasharray="3 3"/>
  <text x="593" y="112" fill="var(--fig-mut)" font-size="10.5">higher above</text>
  <text x="593" y="126" fill="var(--fig-mut)" font-size="10.5">the drain =</text>
  <text x="593" y="140" fill="var(--fig-mut)" font-size="10.5">drier once</text>
  <text x="593" y="154" fill="var(--fig-mut)" font-size="10.5">it settles</text>
  <text x="330" y="292" fill="var(--fig-mut)" font-size="11" text-anchor="middle">One connected water column: the block is its highest point, so it drains first &#8212; while the plant drinks from it too.</text>
</svg>"""

FIG_ROOTIN = """<svg width="660" viewBox="0 0 660 300" style="max-width:100%" xmlns="http://www.w3.org/2000/svg">
  <rect x="60" y="40" width="450" height="14" rx="7" fill="var(--fig-amber-l)" stroke="var(--fig-line)"/>
  <text x="285" y="32" fill="var(--fig-mut)" font-size="10.5" text-anchor="middle">lights on &#8212; 18 h</text>
  <rect x="510" y="40" width="120" height="14" rx="7" fill="var(--fig-panel)" stroke="var(--fig-line)"/>
  <text x="570" y="32" fill="var(--fig-mut)" font-size="10.5" text-anchor="middle">dark &#8212; 6 h</text>
  <polyline fill="none" stroke="var(--fig-green)" stroke-width="2"
    points="60,90 85,82 90,96 115,84 120,98 145,86 150,100 175,88 180,102 205,88 210,102 235,88 240,102 265,88 270,102 295,88 300,102 325,88 330,102 355,88 360,102 385,88 390,102 415,88 420,102 445,88 450,102 475,88 480,102 510,92 630,118"/>
  <text x="52" y="94" fill="var(--fig-green-d)" font-size="11" text-anchor="end">block WC</text>
  <polyline fill="none" stroke="var(--fig-water)" stroke-width="2" points="60,150 630,158"/>
  <text x="52" y="154" fill="var(--fig-water)" font-size="11" text-anchor="end">slab WC</text>
  <line x1="60" y1="200" x2="630" y2="200" stroke="var(--fig-red)" stroke-width="1.5" stroke-dasharray="5 4"/>
  <text x="52" y="204" fill="var(--fig-red)" font-size="11" text-anchor="end">floor 30%</text>
  <g fill="var(--fig-green)">
    <circle cx="85" cy="76" r="2.5"/><circle cx="115" cy="78" r="2.5"/><circle cx="145" cy="80" r="2.5"/>
  </g>
  <text x="128" y="66" fill="var(--fig-mut)" font-size="10.5">60-second shot every hour, block only</text>
  <text x="345" y="248" fill="var(--fig-mut)" font-size="11" text-anchor="middle">The block sawtooths high on hourly micro-shots; the slab sits near field capacity and is ignored.</text>
  <text x="345" y="266" fill="var(--fig-mut)" font-size="11" text-anchor="middle">Neither line ever approaches the recovery floor.</text>
</svg>"""

FIG_ARC = """<svg width="660" viewBox="0 0 660 320" style="max-width:100%" xmlns="http://www.w3.org/2000/svg">
  <line x1="60" y1="250" x2="630" y2="250" stroke="var(--fig-line)"/>
  <line x1="60" y1="40" x2="60" y2="250" stroke="var(--fig-line)"/>
  <text x="48" y="70" fill="var(--fig-mut)" font-size="10.5" text-anchor="end">90%</text>
  <text x="48" y="150" fill="var(--fig-mut)" font-size="10.5" text-anchor="end">60%</text>
  <text x="48" y="216" fill="var(--fig-mut)" font-size="10.5" text-anchor="end">30%</text>
  <line x1="60" y1="212" x2="630" y2="212" stroke="var(--fig-red)" stroke-width="1.5" stroke-dasharray="5 4"/>
  <text x="626" y="228" fill="var(--fig-red)" font-size="10.5" text-anchor="end">recovery floor &#8212; never cross</text>
  <path d="M60 72 C 180 62, 300 66, 390 82 C 470 96, 560 100, 630 96" fill="none" stroke="var(--fig-green)" stroke-width="2.5"/>
  <path d="M60 92 C 150 88, 230 96, 300 118 C 380 148, 470 178, 520 172 C 570 168, 610 162, 630 160" fill="none" stroke="var(--fig-amber)" stroke-width="2.5" stroke-dasharray="7 4"/>
  <text x="92" y="60" fill="var(--fig-green-d)" font-size="11">daily peak</text>
  <text x="436" y="200" fill="var(--fig-amber)" font-size="11">daily trough</text>
  <g fill="var(--fig-mut)" font-size="10.5" text-anchor="middle">
    <text x="100" y="268">veg on slab</text>
    <text x="215" y="268">flower wk 1</text>
    <text x="330" y="268">wk 2&#8211;3</text>
    <text x="447" y="268">wk 4&#8211;6</text>
    <text x="573" y="268">wk 7&#8211;8</text>
  </g>
  <g stroke="var(--fig-line)" stroke-dasharray="2 4">
    <line x1="160" y1="46" x2="160" y2="250"/><line x1="270" y1="46" x2="270" y2="250"/>
    <line x1="390" y1="46" x2="390" y2="250"/><line x1="505" y1="46" x2="505" y2="250"/>
  </g>
  <text x="345" y="300" fill="var(--fig-mut)" font-size="11" text-anchor="middle">Wet and gentle early, drybacks widen through weeks 4&#8211;6, then steady for ripening.</text>
</svg>"""

# ---------------------------------------------------------------- sections

SECTIONS = [
    {
        "id": "intro",
        "kicker": "Start here",
        "title": "What this covers",
        "blocks": [
            lead("Irrigation on slabs is one strategy with five phases, and the whole thing "
                 "is steered by a single number: how full the stone wool is."),
            p("Stone wool holds no nutrient of its own and reacts with nothing you feed it, so "
              "100% of what goes in reaches the plant. That makes it the most precise substrate "
              "you can steer, and the least forgiving when the water curve is wrong."
              + _c("grodan-irrigation-medicinal") + _c("malik2025-media") +
              " This paper covers the full run for a block-on-slab room: preparing and charging "
              "the slabs, the rooting-in window where most slab grows quietly fail, the automated "
              "P0-P3 daily cycle, the week-by-week schedule, and salt management without "
              "hand-flushing."),
            callout("key", "The short version",
                    p("Saturate, then let the substrate lose a controlled amount of water each "
                      "day. That drop is called the dryback, and its size is your steering "
                      "lever. During rooting-in, water only the block and ignore the slab "
                      "completely. Once rooted, run P1 to field capacity each morning, hold it "
                      "with P2 shots and 10-20% runoff, and never let the low point cross about "
                      "30% water content, because below that stone wool channels and will not "
                      "rewet from a dripper.")),
        ],
    },
    {
        "id": "room",
        "kicker": "Hardware",
        "title": "The setup",
        "blocks": [
            p("Every number in this paper is calculated for the hardware below. Change a "
              "component and the volumes change with it, so recompute rather than copying the "
              "figures across."),
            kv([
                ("Substrate", "6&Prime; blocks (150 &times; 150 &times; 142 mm) on 1 m slabs"),
                ("Distribution", "One 4 L/h pressure-compensating dripper per plant into a 5&Prime; ring distributor on the block top"),
                ("Layout", "3 trays &times; 7.6 m, two slab rows per tray &mdash; 6 rows"),
                ("Air", "8&Prime; inflatable air tube per tray blowing under-canopy from the room front"),
                ("Light", "800 W top fixtures, six per row, plus under-canopy bars"),
                ("Atmosphere", "CO<sub>2</sub> injection, leaf-VPD-driven climate control"),
                ("Feed", "Athena Pro Line, batch-tank dosed"),
                ("Control", "Automated crop-steering controller on substrate moisture and EC sensors"),
            ]),
            callout("note", "Assumptions &mdash; check these against the room",
                    ul([
                        "7 &times; 1 m slabs per row (7 m of a 7.6 m tray), <strong>3 plants per slab</strong> &rarr; 21 plants per row, <strong>126 plants total</strong>.",
                        "Slab section assumed 150 &times; 75 mm &rarr; <strong>11.25 L per slab</strong>. A 200 mm wide slab is 15 L and stretches every per-point volume by a third, so check the wrapper.",
                        "One dripper per plant. The reference grow this draws on runs two per plant for redundancy; see the warning below.",
                    ])),
            table(
                ["Quantity", "Value", "Working"],
                [["Dripper flow", "66.7 mL/min", "4 L/h &divide; 60"],
                 ["Block volume", "3.20 L", "150 &times; 150 &times; 142 mm"],
                 ["Substrate per plant", "6.95 L", "3.20 L block + 11.25 L &divide; 3 slab share"],
                 ["1 point of water content, whole root zone", "69.5 mL", "1% of 6.95 L"],
                 ["1 point of water content, block only", "32 mL", "1% of 3.20 L"],
                 ["Standard shot, 2&ndash;5 points", "139&ndash;348 mL &rarr; 2 min 5 s to 5 min 13 s", "points &times; 69.5 mL &divide; 66.7 mL/min"],
                 ["Rooting-in shot, block only", "60 s &rarr; 66.7 mL &rarr; 2.1 points of the block", "see the rooting-in section"],
                 ["Row flow, all drippers open", "84 L/h (1.4 L/min)", "21 &times; 4 L/h"],
                 ["Room flow, all six rows", "504 L/h (8.4 L/min)", "pump and manifold must sustain this if zones fire together"]],
                caption="Table 1. The shot maths for this room. Every schedule below is expressed in these units.",
                foot="Full precision kept deliberately: a 30-second error per shot compounds across 15 or more shots a day.",
            ),
            p("The ring distributor matters more than it looks. 4 L/h from a bare dripper is a "
              "point stream, and a point stream on stone wool wets a narrow column rather than "
              "the block. The shortcut that water finds becomes a permanent preferential path."
              + _c("owen-norden-preferential-flow-2024") +
              " The ring spreads each shot across the whole block top, so even a 30 to 60 second "
              "shot lands as a flat wetting front. That is what makes high-frequency micro-shots "
              "workable on a dripper this size."),
            callout("warn", "One dripper per plant is a single point of failure",
                    p("A clogged emitter here means that plant gets <em>zero</em> water, and on "
                      "stone wool a block can pass its recovery floor in a day under high light. "
                      "Either run two 2 L/h drippers into each ring, or make a daily walk of the "
                      "rings part of the standard operating procedure: every ring visibly wet "
                      "during a P1 shot. Powdered nutrient lines demand real filtration and "
                      "scheduled line flushing, so run 120 mesh minimum at the manifold and "
                      "flush laterals weekly." + _c("netafim-irrigation-maintenance"))),
        ],
    },
    {
        "id": "words",
        "kicker": "Jargon",
        "title": "Definitions",
        "blocks": [
            defterm("Water content", "the share of the substrate volume that is water right "
                    "now, written as a percentage. A slab at 70% is 70% water by volume. This "
                    "single number is what you steer."),
            defterm("Field capacity", "what the substrate settles to shortly after irrigation, "
                    "once free water has drained away. Your daily high point sits here."),
            defterm("Dryback", "the drop in water content between the daily high and the next "
                    "low, caused by the plant drinking and by evaporation. Measured in "
                    "percentage points."),
            defterm("Matric suction", "the pull the substrate itself exerts on water. In stone "
                    "wool almost all water is held at very low suction, which is why small "
                    "height differences move a lot of water."),
            defterm("Recovery floor", "about 25 to 30% water content. Below it the dry fibre "
                    "stops wicking, water runs down a few open channels straight to drain, and "
                    "the dripper can no longer rewet the core."),
            defterm("EC stacking", "letting salt concentrate in the substrate, by dryback with "
                    "feed strength held steady, so root-zone EC climbs above input EC on plan."),
            defterm("P0, P1, P2, P3", "the controller's four daily phases. P0 is the morning "
                    "wait before the first shot, P1 the ramp of stacked shots up to field "
                    "capacity, P2 the maintenance shots holding it there, and P3 the "
                    "last-shot-to-lights-off window that sets the overnight dryback."),
            defterm("Runoff", "feed exiting the slab's drain slits. Not waste. It is how salt "
                    "leaves the slab and how you read what the root zone is actually sitting in."),
        ],
    },
    {
        "id": "physics",
        "kicker": "The physics",
        "title": "Why a soaked slab pulls your block dry",
        "blocks": [
            lead("The most counter-intuitive fact in slab growing: a fully saturated slab "
                 "actively drains the block sitting on it."),
            p("Stone wool holds nearly all of its water at suctions of just a few centimetres of "
              "head, and it moves water very freely when close to saturation."
              + _c("bougoul2006-slab-density") + _c("bougoul2005-stonewool-hydraulic") +
              " The practical consequence is that water content stratifies sharply with height "
              "above the drain plane, wet at the bottom and drier at the top, in any connected "
              "column of fibre." + _c("dasilva1998-slab-distribution")),
            p("Set a block on a slab with full contact and you have created one connected "
              "column, and the block is now its highest point. Once it settles, the block must "
              "end up the driest part, because the slab's extra height pulls the block's water "
              "down into itself. Grodan states this directly: the slab extracts moisture from "
              "the block, and this is precisely why drip must keep running on the block several "
              "times a day until roots have penetrated the slab."
              + _c("grodan-block-slab-interaction") +
              " Meanwhile the plant is transpiring out of that same block. The block is being "
              "drained from below and above at once."),
            figure(FIG_MATRIC, 1,
                   "A block sitting on a slab settles into one water column. The soaked slab "
                   "and the light block are not a contradiction, they are what the column "
                   "settles to. Nothing is wrong with the slab; the block simply sits higher "
                   "above the drain."),
            p("So the stage you can feel with your hands, where the block feels light and the "
              "slab feels soaked, is not a watering error to fix by irrigating the slab. It is "
              "the physics working as designed, and the answer is to feed the block, frequently, "
              "until the roots are established in the slab."
              + _c("grodan-block-slab-interaction") + _c("wtg-e37-bones")),
            callout("danger", "If the block dries out",
                    p("All the roots are in the block. If the block crosses the recovery floor "
                      "it channels and the dripper cannot fix it"
                      + _c("owen-norden-preferential-flow-2024") +
                      ", so you lose root mass in the only substrate the plant currently "
                      "occupies, and the transplant stalls exactly when it should be "
                      "accelerating. In the words of one commercial grower running this "
                      "system: if you are not watering that cube, it does not matter about the "
                      "slab, you have to keep that cube hydrated so you do not lose your root "
                      "base." + _c("wtg-e37-bones"))),
        ],
    },
    {
        "id": "prep",
        "kicker": "Phase 0",
        "title": "Slab prep: level, soak, charge, slit",
        "blocks": [
            p("Everything downstream inherits the slab's starting state. Get it wrong here and "
              "you chase it for eight weeks."),
            steps([
                ("Level the trays",
                 "Water content stratifies with height, so a tray tilted along its 7.6 m run "
                 "becomes a wet end and a dry end that no schedule can even out. Check the fall "
                 "with a level before slabs go down, and leave only the deliberate drain fall."),
                ("Fill the slabs inside the wrapper",
                 "Fill through the block holes with veg-strength feed, around EC 2.5 to 3.0 at "
                 "pH 5.5, until the slab is visibly full with no air pockets, then let it stand "
                 "for <strong>24 hours</strong>." + _c("grodan-slab-handling") +
                 " The soak wets every fibre, which matters because dry stone wool sheds water "
                 "well enough to channel from day one if you skip it, and it pre-charges the "
                 "slab so roots arrive into feed rather than plain water."),
                ("Cut drain slits after the soak, in stages",
                 "Small slits first: 1 to 2 cm at 45 degrees at the slab's lowest edge, offset "
                 "from the block positions, two or three per slab. Grodan cuts drainage in "
                 "stages on purpose, because a wetter slab early helps rooting-in, and you "
                 "enlarge the slits later when the generative phase needs faster drainage."
                 + _c("grodan-drainage-stages") +
                 " After slitting, the slab settles from full saturation down to field capacity."),
                ("Open the wrapper under each block position",
                 "Cut the plastic slightly smaller than the block footprint so fibre touches "
                 "fibre with no plastic bridging the gap. Hydraulic contact is the whole "
                 "mechanism, and a strip of wrapper under one corner of a block is an invisible "
                 "rooting failure."),
                ("Place blocks with full flat contact",
                 "Blocks go down once roots are visible at the block base, with the block at "
                 "field capacity. Press down gently and do not let them rock. Contact area sets "
                 "both how fast the slab pulls the block dry <em>and</em> how easily roots cross "
                 "the boundary." + _c("grodan-block-slab-interaction")),
            ]),
        ],
    },
    {
        "id": "rooting",
        "kicker": "Phase 1, the critical window",
        "title": "Rooting-in: water the block, ignore the slab",
        "blocks": [
            lead("Three to five days where the slab sensors mean nothing and the block is "
                 "everything."),
            p("The procedure below is one that commercial slab rooms run at scale"
              + _c("wtg-e37-bones") +
              ", translated to this room's hardware. Their version: 18/6 light, blocks watered "
              "every hour of lights-on, around 17 shots a day, for the three or four days it "
              "takes plants to lock in, with slab water content deliberately ignored. Grodan's "
              "agronomy prescribes the same thing for the same reason, which is to keep drip "
              "running on the block until roots have gone about 2 cm into the slab."
              + _c("grodan-block-slab-interaction")),
            steps([
                ("Run 18/6 with hourly block micro-shots",
                 "First shot as the lights come on. On a 4 L/h dripper through the ring, "
                 "<strong>60 seconds is 66.7 mL, about 2.1 points of the block</strong>, and "
                 "that is the shot. One per hour of lights-on gives 17 to 18 shots a day, "
                 "roughly 1.13 to 1.20 L per plant per day. Expect some block runoff into the "
                 "slab by midday. That through-flow is intended: fresh feed moving through the "
                 "block beats stagnant saturation, and the excess wets the slab's surface layer "
                 "where roots are about to arrive."),
                ("Add one dark-period shot if blocks run light",
                 "Commercial rooms throw an occasional shot in the dark at exactly this stage"
                 + _c("wtg-e37-bones") +
                 ", because stacked stone wool sheds water fast and the block is being drained "
                 "by the slab all night. If the block feels noticeably light in the morning, "
                 "schedule one 45 to 60 second shot mid-dark."),
                ("Take the slab out of the control loop",
                 "This is the automation trap. A slab sensor reads near field capacity all week, "
                 "so a controller steering on it will suppress irrigation while the block "
                 "starves. Run this phase as a <em>timed</em> program, or steer from a sensor "
                 "mounted in the block, and only hand control to the slab sensors when the phase "
                 "ends."),
                ("Leave the slab's top layer alone",
                 "The top 1 to 2 cm of slab dries back on its own as it drains, and that "
                 "moist-but-aerated layer is exactly where roots first spread, because roots "
                 "need water and oxygen together and the saturated depths have no air to spare."
                 + _c("grodan-block-slab-interaction") + _c("wtg-e37-bones") +
                 " Do not chase that surface dryness with water, and never put drippers into "
                 "the slab."),
                ("Exit on roots, not on the calendar",
                 "Lift the edge of a few sample blocks daily. The phase ends when white roots "
                 "are visibly about 2 cm into the slab and the plants have locked in, typically "
                 "day three to five." + _c("grodan-block-slab-interaction") +
                 " Then hand over to the P0-P3 program below. Grodan's greenhouse guidance "
                 "tapers to one or two shots a day at this point, but a high-EC, high-light room "
                 "keeps the frequency up and lets the program manage it, because frequent small "
                 "shots are also what stop EC spiking inside a 3.2 L block."
                 + _c("hydrus-soilless-substrate-dynamics")),
            ]),
            figure(FIG_ROOTIN, 2,
                   "The rooting-in day. Hourly 60-second shots hold the block in a high, shallow "
                   "sawtooth while the slab sits ignored at field capacity. The block never "
                   "approaches the floor, and losing it there is this phase's only real failure "
                   "mode."),
            callout("key", "Light block, soaked slab",
                    p("If the block feels light while the slab feels soaked, the system is "
                      "working. A light block is drainage plus transpiration, both expected. The "
                      "response is the next scheduled block shot. Not slab irrigation, not "
                      "panic, and not trusting a slab sensor that cannot see the only root zone "
                      "that currently exists.")),
        ],
    },
    {
        "id": "cycle",
        "kicker": "Daily cycle",
        "title": "P0 to P3 on your controller",
        "blocks": [
            p("From rooted-in onward, every day has the same four-phase shape. Steering means "
              "moving the settings inside it, not redesigning the day. This is closed-loop "
              "irrigation, where the controller acts on substrate measurements rather than a "
              "clock." + _c("nemali-2006-set-point-irrigation")),
            table(
                ["Phase", "What happens", "What you adjust"],
                [["P0", "Lights on, no water. The overnight dryback finishes and roots re-oxygenate.",
                  "Delay to the first shot. Longer is more generative"],
                 ["P1", "Stacked shots ramp water content from the overnight low back up to field capacity, with the day's first runoff near the top.",
                  "Shot size (2 to 5 points, 139 to 348 mL, 2 to 5.5 minutes), spacing 20 to 30 min"],
                 ["P2", "Maintenance shots hold near field capacity in a small sawtooth. 10 to 20% of the day's volume leaves as runoff.",
                  "Shot count and spacing. Fewer and wider is more generative"],
                 ["P3", "The last shot of the day, through lights-off. The gap until the next P1 sets the overnight dryback.",
                  "Timing of the last shot. Earlier means a deeper overnight dryback"]],
                caption="Table 2. The daily cycle. Vegetative and generative days differ only in these settings.",
            ),
            ul([
                "<strong>Shot size:</strong> each shot lifts whole-root-zone water content by 2 to 5 points, big enough to register on the sensor and small enough not to run straight to drain. On this hardware that is the 2 to 5.5 minute band from Table 1.",
                "<strong>Runoff:</strong> 10 to 20% of applied volume once at field capacity. Runoff is how salt leaves and how you read root-zone EC, not waste." + _c("grodan-irrigation-medicinal"),
                "<strong>Floor:</strong> set a hard software minimum around 30% water content that the controller always defends, separate from the steering program. The dryback is steering; the floor is a safety interlock. They are different numbers." + _c("owen-norden-preferential-flow-2024"),
                "<strong>Sensors:</strong> steer to <em>substrate</em> water content and EC, not dripper or drain EC, because substrate EC is what the roots actually live in." + _c("grodan-irrigation-medicinal") + " Two sensors per row minimum, one in the front third and one in the back third of the 7.6 m run, mid-slab, between plants, full prong depth. Steer each row on its worst-behaved sensor rather than the average.",
                "<strong>Overnight:</strong> some overnight dryback is essential for root-zone oxygen, but Grodan's medicinal trials found a slightly <em>wetter</em> night, around 10% easier than standard, lifted yield. Do not chase maximum overnight dryback by default." + _c("grodan-irrigation-medicinal"),
            ]),
        ],
    },
    {
        "id": "arc",
        "kicker": "Schedule",
        "title": "Veg to chop, week by week",
        "blocks": [
            p("The plan across the grow is a deliberate curve of high point, dryback and EC. Wet "
              "and gentle while the plant is building, drier and saltier once flower is set, "
              "then steady for the finish." + _c("grodan-irrigation-medicinal")
              + _c("caplan2019-drought") +
              " The EC figures are inputs for a high-light LED room running CO<sub>2</sub>, so "
              "they sit at the high-demand end of the published range."
              + _c("athena-spacing-irrigation") + _c("wtg-e37-bones")),
            figure(FIG_ARC, 3,
                   "The dryback curve from veg-on-slab to chop. High point and low point sit "
                   "close together early, spread apart through weeks 4 to 6, then steady out for "
                   "ripening. The floor never moves."),
            table(
                ["Stage", "Daily high", "Dryback", "Feed EC", "Slab EC", "Runoff", "What matters"],
                [["Rooting-in, slab days 1&ndash;5", "block cycles high", "block shallow, slab untouched", "2.5&ndash;2.8", "as pre-charged", "block through-flow", "Hourly 60-second block shots. Slab sensors out of the loop"],
                 ["Veg on slab to flip", "75&ndash;85%", "5&ndash;15 pts", "2.8&ndash;3.0", "3.0&ndash;4.5", "5&ndash;10%", "Build root mass. Hand control to P0-P3 on the sensors"],
                 ["Flower week 1, days 1&ndash;7", "80&ndash;90%", "none deliberate", "3.0&ndash;3.5", "climbing", "10&ndash;15%", "Feed hard: hourly shots of about 3 min (200 mL, 2.9 pts). No dryback before day 7, and treat slab readings as noise until about day 10" + _c("wtg-e37-bones")],
                 ["Flower weeks 2&ndash;3, days 8&ndash;21", "75&ndash;85%", "first real drybacks, low point at or above 30&ndash;35%", "3.0&ndash;3.5", "stack to 6&ndash;9", "10&ndash;15%", "The EC stacking window. Dryback concentrates the slab on plan, so watch substrate EC daily" + _c("wtg-e37-bones")],
                 ["Flower weeks 4&ndash;6", "70&ndash;80%", "20&ndash;30 pts", "3.0&ndash;3.5", "hold 7&ndash;9", "15&ndash;20%", "The generative push, but keep daytime feeding generous. Wetter days yielded more at equal potency in Grodan's trials" + _c("grodan-irrigation-medicinal")],
                 ["Flower weeks 7&ndash;8", "65&ndash;75%", "18&ndash;25 pts", "taper 3.0 to 2.0 by diluting the tank", "ease down", "15&ndash;20%", "The end-of-grow flush is tank dilution from about day 45, never plain water" + _c("wtg-e31-sipkoi")]],
                caption="Table 3. The full schedule. Every cell is a starting point to confirm against your own sensors, because cultivar variation in medicinal crops is large enough that Grodan declines to publish one correct number.",
                foot="Slab EC above about 9, or a low point below 30%, is off-plan regardless of stage. The 6 to 9 stacking band comes from a commercial LED room; introduce it over days, not in one dryback.",
            ),
            callout("warn", "Dryback stress is partly salt stress",
                    p("Water leaves and salt stays, so EC rises as 1 divided by the fraction of "
                      "water remaining. A slab drying from 75% to 45% concentrates by roughly "
                      "two-thirds." + _c("hydrus-soilless-substrate-dynamics") +
                      " A 3.0 feed can read 5 or more in the slab by late afternoon on a big "
                      "dryback. When you push weeks 4 to 6 you are pulling the EC lever and the "
                      "water lever at the same time, so if substrate EC outruns the plan, shrink "
                      "the dryback before you touch the feed.")),
        ],
    },
    {
        "id": "flush",
        "kicker": "Salt management",
        "title": "Flushing",
        "blocks": [
            lead("In this system you never flush with plain water. Half of all high-EC readings "
                 "are not a salt problem at all, and the real ones are fixed with feed."),
            steps([
                ("First, check the reading is real",
                 "A dry block automatically reads high EC, because salt stays put as water "
                 "leaves, so EC scales with 1 divided by the water fraction."
                 + _c("hydrus-soilless-substrate-dynamics") +
                 " A block at 40% water content on a 3.0 feed legitimately reads about 6 with no "
                 "excess salt in it at all. Saturate to field capacity with normal feed, take a "
                 "little runoff, and re-measure. Most cases end here."),
                ("A real flush is the same feed, more throughput",
                 "Stone wool holds effectively no charge, so nothing binds the salt and all of "
                 "it is dissolved and mobile." + _c("malik2025-media") +
                 " Feed at 3.0 EC flowing through a 6.0 slab carries salt out exactly as well as "
                 "plain water, without the shock. Add P2 shots, or size, until runoff reaches "
                 "about 20% or more, hold for a day or two until runoff EC falls back toward "
                 "feed EC, then step back to normal. This is also the end-of-grow method: dilute "
                 "the tank rather than reaching for a hose." + _c("wtg-e31-sipkoi")),
                ("Never plain water",
                 "With no buffer in the substrate you get an instant EC crash at the roots, a "
                 "shock to cells that had adapted to a salty root zone, a nutrient gap, and a "
                 "rebound the moment feed resumes. The swing does more damage than the stacked "
                 "salt did. It also dumps low-EC water into a slab you deliberately pre-charged."),
                ("Know where the block's runoff goes",
                 "Flush-through from the block drains into the slab and pushes slab solution out "
                 "the drain slits, which only works if the slits exist and the fall is right. "
                 "The block's stacked salt exits <em>through</em> the slab's top layer, so "
                 "keeping shots frequent keeps that salt moving out instead of parking where the "
                 "roots are densest."),
                ("If a block or slab has actually channelled",
                 "Past the recovery floor the dripper cannot help, because water bypasses the "
                 "dry core and exits, runoff reads high and the sensor barely moves."
                 + _c("owen-norden-preferential-flow-2024") +
                 " The rescue is a long, slow hand-soak in feed solution until the core takes "
                 "water again, which takes hours rather than minutes. Stone wool that has been "
                 "to the floor repeatedly wets unevenly from then on, so cull the block and make "
                 "a note against the slab."),
            ]),
        ],
    },
    {
        "id": "env",
        "kicker": "The demand side",
        "title": "What the lights, CO2 and airflow do to your water",
        "blocks": [
            p("Irrigation is the supply side of a demand the rest of the room creates. This room "
              "creates a lot of demand, and unusually even demand, which is worth understanding "
              "because it changes what your sensor traces should look like."),
            grid([
                card("Under-canopy light",
                     p("Under-canopy bars put light on leaves that were previously idling, so "
                       "whole-plant water and nutrient demand steps up. One commercial room "
                       "found that adding it forced upgrades to both feed volume and "
                       "dehumidification." + _c("wtg-e37-bones") +
                       " Expect visibly faster drybacks once the bars come on. That is the "
                       "demand signal, not a fault."),
                     tag="more demand"),
                card("High light plus CO2",
                     p("High light intensity with CO<sub>2</sub> enrichment runs warmer and "
                       "raises the transpiration ceiling, and LED rooms feed hungrier than HPS "
                       "at equal coverage, which is why the reference LED figures sit at veg 2.7 "
                       "and flower from 3.5." + _c("wtg-e37-bones") +
                       " Uptake at peak bulk will reach 1.5 to 2 L per plant per day, so across "
                       "126 plants that is 190 to 250 L of uptake, or roughly 220 to 300 L a day "
                       "applied once runoff is included. Size the batch tank for that."),
                     tag="more demand"),
                card("Under-canopy airflow",
                     p("The inflatable air tube's job, as far as irrigation is concerned, is "
                       "evenness. It strips the still, humid layer from under the canopy along "
                       "the whole 7.6 m run, so the front and back of a row transpire alike and "
                       "their dryback curves match. It is also the botrytis insurance for the "
                       "dense lower buds the under-canopy bars will build. Check it with the "
                       "paired sensors: the front and back traces should sit on top of each "
                       "other, and if they drift apart, suspect airflow or a slit before you "
                       "suspect irrigation."),
                     tag="evenness"),
                card("Leaf VPD control",
                     p("Transpiration tracks vapour pressure deficit, so a controller holding "
                       "leaf VPD steady makes daily water demand stable and the dryback curve "
                       "repeatable, which is what lets an automated steering program be "
                       "aggressive safely. The flip side is that any VPD setpoint change "
                       "<em>is</em> an irrigation change. Expect the controller to add or drop "
                       "P2 shots the same day, because demand-driven irrigation follows the "
                       "sensor rather than the schedule."
                       + _c("nemali-2006-set-point-irrigation")),
                     tag="stability"),
            ], cols=2),
        ],
    },
    {
        "id": "faults",
        "kicker": "Faults",
        "title": "Troubleshooting",
        "blocks": [
            table(
                ["Symptom", "Likely cause", "What to do"],
                [["Runoff high but the sensor barely moves", "Channelling, core is past the floor", "Hand-soak with feed to rewet, raise the software floor, then find out why it dried"],
                 ["Substrate EC climbing day over day, off-plan", "Not enough runoff, so salt is stacking", "Add P2 shots or size until runoff EC turns down"],
                 ["Substrate EC sagging below target", "Over-flushing", "Cut runoff back to 10&ndash;15%"],
                 ["Water content never reaches field capacity in P1", "Clogged emitter, a P1 ramp that is too short, or a 200 mm slab you sized as 150", "Walk the rings mid-shot, lengthen P1, re-check the slab dimensions"],
                 ["Fresh transplants stalling while the slab is wet", "Blocks starving on a soaked slab, the rooting-in trap", "Restart hourly block shots immediately and check wrapper contact under the blocks"],
                 ["Front and back of a row drying at different rates", "Airflow gradient or uneven slitting", "Check air-tube inflation and the hole line first, then slit sizes. Steer the row on its wetter sensor in the meantime"],
                 ["Dryback suddenly deeper than programmed", "Demand stepped up (bars on, VPD change, CO<sub>2</sub> ramp) or a shot was missed", "Check the controller log, add P2 shots, and treat it as a demand signal rather than a sensor fault"],
                 ["One plant wilting while its neighbours are fine", "That plant's single dripper is down", "Clear or replace the emitter, and hand-soak its block with feed if it crossed the floor"]],
                caption="Table 4. Symptoms and causes. Most problems are a water-content or EC trace drifting from plan, and the sensor tells you which.",
            ),
        ],
    },
    {
        "id": "numbers",
        "kicker": "Quick reference",
        "title": "Setpoints",
        "blocks": [
            kv([
                ("Working water content", "55&ndash;92%. Recovery floor 25&ndash;30%, with a hard software minimum at 30%"),
                ("Shot size", "2&ndash;5 points, 139&ndash;348 mL, 2 min 5 s to 5 min 13 s at 4 L/h"),
                ("Rooting-in", "60-second block-only shots, hourly on 18/6, three to five days, slab sensors out of the loop"),
                ("Daily runoff", "10&ndash;20% at field capacity, 5&ndash;10% in veg"),
                ("Dryback", "Vegetative 5&ndash;15 points. Generative 20&ndash;30 points"),
                ("Feed EC, LED with CO<sub>2</sub>", "veg 2.5&ndash;3.0, flower 3.0&ndash;3.5, taper to about 2.0 by tank dilution from day 45"),
                ("Slab EC", "3.0&ndash;4.5 in veg, stack to 6&ndash;9 over flower weeks 2&ndash;3, hold, then ease"),
                ("Feed pH", "5.5 for the slab soak, 5.7&ndash;6.0 running"),
                ("Flower week 1", "hourly feeds, no deliberate dryback before day 7, slab readings ignored until about day 10"),
                ("Flushing", "never plain water. Same EC with more throughput, and end-of-grow by tank dilution"),
                ("Room hydraulics", "66.7 mL/min per dripper, 84 L/h per row, 504 L/h all on, 220&ndash;300 L/day tank at peak"),
            ]),
            callout("key", "Five key things to remember",
                    ol([
                        "Rooting-in: hourly 60-second shots to the block, ignore the slab, and stop when roots are 2 cm in.",
                        "Every day after that: P1 up to field capacity, P2 holds it with 10 to 20% runoff, P3 sets the overnight dryback.",
                        "Steer with the daily high, the dryback size and the timing. Wet, small and late is vegetative; dry, big and early is generative.",
                        "Never let any low point cross the 30% floor. It is an interlock, not a setpoint.",
                        "Steer to substrate water content and EC off the sensors, and manage salt with runoff rather than a hose.",
                    ])),
        ],
    },
]
