# -*- coding: utf-8 -*-
"""Paper: the closed loop, levers, signal and plant state (beginner)."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        stagecard, grid, card, chip, kv, steps)
import figs_lib as L

SLUG = "closed-loop"
TITLE = "The closed loop: levers, signal and plant state"
EYEBROW = "Precision · Closed loop"
SUB = ("Run a grow room as one self-correcting system. This beginner's guide covers the controls "
       "you pull, how to read what the plants are actually doing, and how to feed that back "
       "without the room chasing its own tail.")
META = [("gauge", "Precision"), ("image", "9 diagrams"),
        ("quote", "Peer-reviewed · 9 sources"), ("clock", "~17 min read")]
RELATED = ["signal-and-noise", "plant-state-dashboard", "f2-crop-steering"]
REF_IDS = ["mohammed-spc-2024", "isa-18-2-alarm-mgmt", "moon-rootzone-ec-2018",
           "huber-dli-co2-2021", "kim-co2-temp-light-msu", "szerement-dielectric-2019",
           "tdr-fdr-soil-review-2024", "choi-ec-transpiration-2015", "saure-tipburn-calcium-2001"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

SECTIONS.append({"id": "what-this-is", "kicker": "Start here", "title": "What this is (and why a grow room is a loop)",
  "blocks": [
    lead("A grow room is a <strong>loop</strong>, not a panel of independent dials you set and forget. "
         "You change a control, the room and plants respond, sensors measure that response, you work "
         "out what it means, and that tells you what to change next. Around and around, every minute "
         "of every day."),
    p("A <strong>closed loop</strong> means the output feeds back to the input: what the plant tells "
      "you decides your next move, and then you watch what that move actually did. This guide teaches "
      "the whole circle as one thing, with three jobs sitting on it: getting the action right "
      "(<em>cause</em>), getting the measurement honest (<em>perception</em>), and getting the meaning "
      "out (<em>cognition</em>)."),
    p("<strong>You never move just one thing.</strong> Every control pushes on four linked balances at "
      "once: heat, water vapour, CO2 and the salt in the root zone. The finished version of this loop "
      "is a room that senses its own state, knows what its actions will do, and corrects its own drift "
      "before that drift becomes damage."),
    figure(L.flow("The closed loop, six steps",
            [("Act", "pull a lever"), ("Room responds", "coupled cascade"),
             ("Sense", "measure + noise"), ("Filter", "signal vs noise"),
             ("Infer", "estimate plant state"), ("Prescribe", "action + setpoint -> back to act")],
            note="The last arrow, Prescribe back to Act, is the one that closes the loop."), 1,
      "Read it as a circle. The room works like a nervous system: muscles (the levers), nerves "
      "(the sensors) and a mind (the inference that decides what it all means)."),
    callout("key", "What 'closed' buys you",
      p("A mature loop tells you whole-room health and whether to act in under five seconds, and it "
        "stays quiet when nothing needs you. Silence is a feature, not a fault.")),
  ]})

SECTIONS.append({"id": "key-terms", "kicker": "Plain-language dictionary", "title": "Key terms, defined once",
  "blocks": [
    p("This field is loaded with jargon, so here is every term you need before the real content. Most "
      "are everyday ideas with intimidating names. Don't memorise them. Each one comes back in "
      "context."),
    defterm("Lever (actuator)", "A control you can move: light brightness, cooling setpoint, "
            "irrigation, CO2 dosing. Around eleven main lever families run a room."),
    defterm("Signal vs noise", "Signal is what the plant and room are truly doing. Noise is sensor "
            "jitter, biological scatter and one-off spikes that mean nothing. Every reading is "
            "signal + noise added together."),
    defterm("Setpoint vs target", "A setpoint is the literal number a machine chases (e.g. cool to "
            "24&deg;C). A target is the outcome you actually want (e.g. keep the plant transpiring "
            "healthily). They are not the same thing."),
    defterm("VPD (vapour pressure deficit)", "How &lsquo;thirsty&rsquo; the air is. It drives "
            "how fast plants lose water. Measured in kilopascals (kPa)."),
    defterm("EC, VWC, dryback", "EC (electrical conductivity) = how salty the feed or root zone is. "
            "VWC = how wet the growing medium is. Dryback = how much the medium dries between waterings."),
    defterm("Plant state", "The plant's actual condition (stressed, steering generative, on-track), "
            "inferred from many signals together rather than read off one gauge."),
  ]})

SECTIONS.append({"id": "the-levers", "kicker": "Core content: the action half", "title": "The levers: every control moves four things at once",
  "blocks": [
    p("The room is one <strong>coupled</strong> system, not a set of independent knobs. Turn up the "
      "light and you have not just added light: you have added heat, made the plants drink and sweat "
      "faster (raising humidity), increased CO2 demand, and sped up how fast the root zone dries and "
      "concentrates salt" + _c("huber-dli-co2-2021") + ". Light is at once a heat source, a "
      "transpiration driver, a CO2-demand creator and an HVAC load" + _c("kim-co2-temp-light-msu") + "."),
    p("Everything you can do sorts into four <strong>balances</strong> you are always disturbing: "
      "energy (heat), moisture (water vapour), carbon (CO2) and salt (root-zone EC), with around "
      "eleven primary lever families acting across them" + _c("kim-co2-temp-light-msu") +
      ". The right question before any change is not &lsquo;what does this lever do?&rsquo; but "
      "&lsquo;which balance am I disturbing, and can the rest of the room absorb it?&rsquo;"),
    figure(L.flow("One lever, four balances",
            [("Raise light / PPFD", "one move"), ("Energy", "leaf temp up, AC runtime up"),
             ("Moisture", "transpiration up, RH up, dehumid load up"),
             ("Carbon", "CO2 demand up"), ("Salt / root zone", "faster dryback, substrate EC up"),
             ("Verdict", "capacity exceeded? = failure mode")],
            note="A single lever fans out into all four balances at once."), 2,
      "One move, four consequences. Lowering the cooling setpoint is the same story: it changes "
      "humidity, VPD, dryback rate and condensation risk together" + _c("choi-ec-transpiration-2015") + "."),
    figure(L.bars("How long a coupled disturbance takes to settle",
            [("Energy (heat)", 8), ("Moisture (RH)", 18), ("Carbon (CO2)", 6), ("Salt (root zone)", 240)],
            unit=" min",
            note="Salt in the root zone settles far slower than air balances. It builds over cycles.",
            maxv=280), 3,
      "The four balances respond on very different timescales, which is why a single lever change can "
      "look fine for hours and still be quietly loading the slowest balance" + _c("moon-rootzone-ec-2018") + "."),
    table(["Balance", "What adds to it", "What removes it", "The lever you reach for"], [
      ["<strong>Energy</strong> (heat)", "Lights, equipment, sun load", "AC, ventilation", "Light level, cooling setpoint, airflow"],
      ["<strong>Moisture</strong> (vapour)", "Transpiration, irrigation", "Dehumidifier, exhaust", "Dehumid setpoint, VPD target, shot size"],
      ["<strong>Carbon</strong> (CO2)", "Dosing", "Plant uptake, exhaust", "CO2 setpoint, exhaust timing"],
      ["<strong>Salt</strong> (root zone)", "Feed EC, dryback", "Plant uptake, runoff", "Shot size/frequency, dryback target, feed EC, runoff %"],
    ], caption="The four balances and the levers that move each. Every classic failure is a coupling failure, not a broken part."),
    callout("warn", "Classic failures are coordination failures",
      p("Cooling that creates humidity, dehumidification that overheats the room, CO2 fighting the "
        "exhaust: nothing broke. The levers were just set as if they were independent. The fix is "
        "order of operations: set biological demand first (stage, light, CO2), then size climate "
        "capacity to match, then set the root-zone strategy to that.")),
  ]})

SECTIONS.append({"id": "reading-plant-state", "kicker": "Core content: sensing and meaning", "title": "Reading the signal, then reading the plant",
  "blocks": [
    p("You have to <em>see</em> the room's response without being fooled, then turn it into meaning. "
      "Every measurement is signal plus noise, and in practice around <strong>70% of raw alerts are "
      "noise</strong> that must be rejected before they ever reach a decision" + _c("isa-18-2-alarm-mgmt") + "."),
    p("Reading plant state is the leap from &lsquo;VWC fell 12% overnight&rsquo; (a number) to "
      "&lsquo;the plant is steering generative as intended, no action needed&rsquo; or &lsquo;reduce "
      "dryback 3% tonight or expect tip burn in about 48 hours&rsquo; (a decision). The goal is to "
      "infer the plant, not just display the room."),
    p("Three signal habits, in order, get you there:"),
    ul(["<strong>Sample at the right speed</strong> for the biology: fast enough to catch a "
        "30-minute irrigation response, slow enough not to log useless jitter.",
        "<strong>Filter out scatter</strong> with rolling or median averages before you look.",
        "<strong>Judge with control limits</strong>, lines drawn from the process's own "
        "history, conventionally the mean and roughly &plusmn;3 standard deviations (sigma)" + _c("mohammed-spc-2024") + "."]),
    figure(L.line("Signal vs noise on one reading",
            [(0, 50), (1, 49), (2, 52), (3, 48), (4, 51), (5, 50), (6, 53), (7, 49)],
            ["t0", "t1", "t2", "t3", "t4", "t5", "t6", "t7"], ylab="reading",
            note="The smooth trend is the story; the jitter around it is noise to be filtered out."), 4,
      "A raw sensor reading wobbles every sample. The trend is what the room is doing; the jitter is "
      "not. Acting on the jitter is acting on events that never happened."),
    figure(L.line("Control chart: when a wiggle earns a response",
            [(0, 50), (1, 51), (2, 49), (3, 50), (4, 52), (5, 48), (6, 51), (7, 49), (8, 50), (9, 52), (10, 49), (11, 78)],
            ["", "", "", "", "", "", "", "", "", "", "", "flag"], ylab="value",
            note="Eleven points jitter harmlessly; the twelfth crosses the limit and is flagged 'special cause'.",
            ymax=90), 5,
      "Inside the band = the room being a room, do nothing. A point past the limit, or a non-random "
      "run, is a special cause to investigate. Distinguishing common-cause from special-cause "
      "variation is the whole basis of statistical process control" + _c("mohammed-spc-2024") + "."),
    p("Then <strong>aggregate, don't trust one reading</strong>: believe n-of-12, not n-of-1. A clean, "
      "classified signal is the only acceptable input to inference. Inference then fuses several "
      "cleaned signals into named conditions, each with a confidence level and an evidence chain, judged "
      "against a <em>learned envelope</em> rather than a fixed line. 1.4 kPa VPD is fine in late "
      "flower but punishing in early veg."),
    figure(L.zones("The four-zone calm dashboard", 0, 4,
            [(0, 1, L.GL, "Zone 1: plant truth"), (1, 2, L.AMBL, "Zone 2: watchlist"),
             (2, 3, L.REDL, "Zone 3: advisory"), (3, 4, L.BLUL, "Zone 4: raw graphs")],
            note="Zone 1 carries ~90% of the value; the raw graph wall is demoted to the basement."), 6,
      "A calm dashboard leads with one green plant-truth headline (&lsquo;Flower Day 24, on-track, no "
      "action needed&rsquo;). Yellow is drifting precursors, orange is the only interrupt, and the raw "
      "graphs sit last."),
  ]})

SECTIONS.append({"id": "closing-the-loop", "kicker": "Core content: putting it together", "title": "Closing the loop: one problem, traced all the way round",
  "blocks": [
    p("The three jobs become one machine here. Watch a single ordinary problem, slow "
      "<strong>salt creep</strong> in the root zone, travel the whole loop."),
    steps([
      ("Cause sets the conditions", "A long dryback plus a flat feed concentrates salt a little more each cycle. The slowest balance is loading."),
      ("Perception refuses to overreact", "It ignores any single EC spike, but flags a sustained four-day rising run past the control limit as a true signal."),
      ("Cognition gives it meaning", "It fuses that run with feed and dryback data into a named precursor, 'salt accumulation, tip-burn precursor', with confidence and evidence."),
      ("Prescribe and act", "It pulls the dryback lever back, closing the loop about four days before tip burn would appear, and the salt balance starts recovering."),
    ]),
    figure(L.flow("Salt creep through the whole loop",
            [("Cause", "dryback long, feed flat, salt concentrates"),
             ("Perception", "single spike ignored, 4-day run past limit = signal"),
             ("Cognition", "fuse EC + feed + dryback -> tip-burn precursor"),
             ("Prescribe -> act", "ease dryback, loop back, correct the same lever")],
            note="The same dryback lever that caused it is the lever the loop pulls to fix it."), 7,
      "Closed-loop correction catches root-zone salt accumulation roughly four days before visible tip "
      "burn would show" + _c("saure-tipburn-calcium-2001") + ", because the EC the roots feel rises "
      "as the medium dries, well before leaves react" + _c("choi-ec-transpiration-2015") + "."),
    callout("note", "No single job catches it alone",
      ul(["A <strong>lever-only</strong> grower never measures it.",
          "A <strong>signal-only</strong> grower sees a number move but not what it means.",
          "A <strong>dashboard-only</strong> grower, without the causal map, prescribes the wrong lever.",
          "Only the whole loop has the emergent property of <strong>self-correction</strong>: sensing its own mistakes and undoing them."], "tight")),
    p("Bridge metrics let the three jobs talk to each other. Dryback %, VPD and VPD-hours, pore-water "
      "EC and recovery slope are each computed once on a consistent definition and read by every part. "
      "Always <strong>prescribe with a number and show your work</strong>: name the action, the "
      "setpoint, the deadline and the expected outcome, expandable to the full evidence on demand. "
      "Never be a black box."),
    table(["Failure", "Cause / coupling at fault", "Signal discipline that catches it", "Inference & prescription"], [
      ["Silent salt creep", "Long dryback + flat feed", "4-day run past EC limit", "Tip-burn precursor → ease dryback"],
      ["Irrigation didn't land", "Clog / pump / line fault", "Expected VWC step absent", "Failed shot → re-fire, alert"],
      ["Stealth morning stress", "VPD spike at lights-on", "VPD-hours over envelope", "Morning stress → ramp climate gently"],
      ["Dehumidifier dying slowly", "Falling removal capacity", "RH drift trend, not spike", "Capacity fade → service before failure"],
      ["The blind sensor", "Flatlined / noisy probe", "Variance collapse or jitter = special cause", "Bad probe → quarantine, don't trust"],
    ], cls="compact", caption="Five failures, one fusion. A flatlined, drifting or noisy probe is itself a detectable special-cause signal" + _c("szerement-dielectric-2019") + "."),
  ]})

SECTIONS.append({"id": "how-to", "kicker": "Do this first", "title": "How to build the loop, step by step",
  "blocks": [
    p("You build the loop one rung at a time, and you do not earn the next rung until the previous one "
      "is genuinely running. Almost none of this needs new capital. Most of it is discipline."),
    steps([
      ("Arc I: get your actions coupling-aware", "Before any change, name which of the four balances it moves and in which direction. Treat every failure as a capacity or coordination problem, not one bad lever."),
      ("Arc II: get your signals honest", "Stop watching live numbers (they invite over-reaction). Set a sampling cadence per channel, put a rolling average on every decision chart, and compute control limits from your own history."),
      ("Arc III: get your decisions inferred", "Judge against an envelope per cultivar/stage/photoperiod. Fuse before you flag, because no signal stands alone. Make every advisory prescribe a number and show its evidence, and go quiet by default."),
      ("Close the loop last, and gently", "Gate the first automated write-back to a low-risk, reversible move, for example a 3-point dryback nudge behind a confirm. Keep expensive or irreversible actions human-approved."),
    ]),
    callout("tip", "Discipline before capital",
      p("The most valuable upgrades on this list cost nothing but habit: a sampling cadence, a rolling "
        "average and a control limit are free. Buy hardware only once the discipline is in place to "
        "use it.")),
  ]})

SECTIONS.append({"id": "pitfalls", "kicker": "What goes wrong", "title": "Pitfalls: oscillation and chasing noise",
  "blocks": [
    p("Two failure modes ruin a loop: <strong>chasing noise</strong> and <strong>oscillation</strong>. "
      "Feed a controller noise, meaning single spikes, jitter and ghost trends, and it acts on events "
      "that never happened, actively destabilising the room. A loop fed noise doesn't help, it amplifies. "
      "Oscillation comes from reacting too fast, too hard, or to readings still inside normal variation, "
      "so the room swings back and forth instead of settling" + _c("mohammed-spc-2024") + "."),
    figure(L.line("Noise-driven oscillation vs calm correction",
            [(0, 50), (1, 64), (2, 38), (3, 66), (4, 36), (5, 62), (6, 40), (7, 58), (8, 44), (9, 50)],
            ["", "", "", "", "", "", "", "", "", ""], ylab="setpoint",
            note="Chasing every jitter makes the setpoint swing wildly; one disciplined correction would hold it flat.",
            ymax=80), 8,
      "Reacting to each wiggle drives the room into a swing it can never settle out of. A filtered loop "
      "makes one decisive correction only when the signal truly crosses a limit."),
    callout("danger", "The one-sentence test before reacting",
      p("Has the reading moved beyond its learned envelope (<em>meaning</em>), for longer than one "
        "reading with sensors in agreement (<em>signal</em>), and do you know which lever answers it "
        "without disturbing another balance (<em>cause</em>)? If it fails any of the three, it's "
        "noise. Do nothing.")),
    ul(["<strong>Aliasing</strong>: sampling too slowly invents phantom trends, and over-sampling logs "
        "jitter you can't act on and tempts you to tamper. Match cadence to the biology" + _c("tdr-fdr-soil-review-2024") + ".",
        "<strong>The Stage-2 trap</strong>: reacting to live numbers is more stressful than flying "
        "blind. It's a wall of noise to panic at.",
        "<strong>Walk the loop, not the wiggle</strong>: smooth enough to act calmly, but never so "
        "smooth you go blind to a real fast event. Keep raw data one click away."]),
  ]})

SECTIONS.append({"id": "expectations", "kicker": "What to actually expect", "title": "Realistic expectations",
  "blocks": [
    callout("key", "The end state is quieter, not flashier",
      p("A working loop means you look at the dashboard less, are surprised less, and harvest more "
        "consistently. Silence is the product: a blank screen means nothing needs you. The "
        "advisory-first stage, where the loop tells you what to do but you still pull the lever, "
        "is a stable, valuable place to stop indefinitely. Full autonomy is opt-in, gated, "
        "and never obligatory.")),
    figure(L.flow("The five-rung maturity ladder",
            [("1 Blind", "gut & eyeball"), ("2 Logged", "data, no method, react to spikes"),
             ("3 Filtered", "sampling + filter + limits (Perception lit)"),
             ("4 Inferred", "fuse to plant state, prescribe (Cognition lit)"),
             ("5 Looped", "gated write-back, predictive (Cause closes back)")],
            note="Rising capability. You don't earn a rung until the one below it genuinely runs."), 9,
      "The single highest-return move is getting from rung 2 to rung 3: stop reacting to live numbers, "
      "start reacting to filtered trends past control limits. It costs nothing but habit and is the "
      "precondition for everything above it."),
    ul(["<strong>You don't have to automate to win.</strong> Intelligence reaches the screen long "
        "before autonomous actuation, and stopping there is a fine, stable outcome.",
        "<strong>Numbers are starting points, not gospel.</strong> Reference setpoints are "
        "commercial-cultivation starting points to calibrate against your own facility's history. The "
        "method is universal; the setpoints are yours.",
        "<strong>Prove it small.</strong> Pick one room and one failure pattern, run it in shadow-mode "
        "for one cycle, and prove the lead time on a single advisory before you scale."]),
    p("Get your actions coupling-aware, your signals honest, and your decisions inferred. Then, and "
      "only then, consider closing the loop. To go deeper on the perception half, read the "
      "<a href='signal-and-noise.html'>signal and noise</a> paper. For the cognition half and how it "
      "reaches you, read the <a href='plant-state-dashboard.html'>plant-state dashboard</a> guide."),
  ]})
