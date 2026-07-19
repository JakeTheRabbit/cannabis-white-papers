# -*- coding: utf-8 -*-
"""Paper: the smart watering brain (VRWE), in plain English (beginner)."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        stagecard, grid, card, chip, kv, steps)
import figs_lib as L

SLUG = "smart-watering-vrwe"
TITLE = "The smart watering brain (VRWE), in plain English"
EYEBROW = "Precision · Smart watering"
SUB = ("A grow room can water plants on its own by combining several sensor signals "
       "instead of trusting one moisture probe that might be lying.")
META = [("gauge", "Precision"), ("image", "9 diagrams"),
        ("quote", "Evidence-linked · 5 sources"), ("clock", "~9 min read")]
RELATED = ["root-zone-teros12", "signal-and-noise", "closed-loop"]
REF_IDS = ["szerement-seven-rod-2019", "mane-dielectric-calibration-review-2024",
           "koehler-transpiration-vpd-2023", "owen-norden-preferential-flow-2024",
           "hydrus-soilless-substrate-dynamics"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

SECTIONS.append({"id": "what-this-is", "kicker": "Start here", "title": "What this is, and the problem it solves",
  "blocks": [
    callout("evidence", "Grain of salt",
      "<p><strong>Provisional:</strong> Multi-signal caution is sound engineering. Claims of never flooding or "
      "never starving depend on sensor health, calibration, and fail-safes &mdash; keep hard VWC floors and "
      "human override.</p>"),
    lead("VRWE stands for <strong>Virtual Root-Zone Water Estimator</strong>: software that decides "
         "when and how much to water a plant by combining several signals instead of obeying one "
         "sensor. It is a &lsquo;virtual&rsquo; estimator because it never reads the water directly. "
         "It works the amount out from several clues, the way you can tell a kettle is nearly empty "
         "from its weight and how long it has been boiling."),
    p("Each pot has only one moisture sensor, and that sensor feels "
      "only a tiny spot of soil, roughly the volume of a soda can" + _c("szerement-seven-rod-2019") +
      ". If that spot happens to be dry, or if water sneaks past it, the sensor reports "
      "&lsquo;I&rsquo;m dry!&rsquo; and a dumb timer would believe it and drown the plant. VRWE "
      "treats the sensor as one opinion to double-check, not the boss."),
    figure(L.flow("How VRWE thinks: SEE, THINK, DO",
            [("SEE", "one sensor, a tiny view that can lie"),
             ("THINK", "the brain does water-balance math"),
             ("DO", "water a bit / wait / ask a human")],
            note="The sensor is just the first step, not the decision."), 1,
      "VRWE sees one limited signal, thinks by checking it against other evidence, then acts "
      "conservatively. The whole paper is about the THINK box."),
    callout("note", "What kind of paper this is",
      p("This is operational, product-style guidance for how the system <em>behaves</em>, "
        "not a lab study. It pairs with the "
        "<a href='root-zone-teros12.html'>root-zone sensor</a> paper (what a single probe actually "
        "measures) and the <a href='signal-and-noise.html'>signal &amp; noise</a> paper (telling a "
        "real change from sensor jitter).")),
  ]})

SECTIONS.append({"id": "key-terms", "kicker": "Vocabulary", "title": "Key terms, defined once",
  "blocks": [
    p("Five words carry the whole idea, so we define them up front. Don&rsquo;t memorise "
      "them. Each one comes back in context."),
    defterm("VWC (volumetric water content)", "How wet the soil is at the sensor&rsquo;s spot, "
            "as a percentage. This is the raw &lsquo;sensor reading&rsquo; VRWE double-checks."),
    defterm("Runoff / drain", "Water that leaves the bottom of the pot. Water that drains away never "
            "fed the plant."),
    defterm("Full pot (DUL, drained upper limit)", "The most water the pot can hold once it has "
            "finished dripping. Past this point, extra water just runs off."),
    defterm("Channeling", "Water sneaking straight down one path and missing the roots. It "
            "goes in the top and out the bottom without doing any good."),
    defterm("Confidence", "The brain&rsquo;s self-rated trust in its own current guess. High "
            "confidence allows bolder action. Low confidence forces caution."),
    table(["Term", "Plain-English meaning"], [
      ["<strong>VWC</strong>", "How wet the soil is at the sensor&rsquo;s spot"],
      ["<strong>Runoff / drain</strong>", "Water leaving the bottom of the pot"],
      ["<strong>Full pot (DUL)</strong>", "The most water the pot holds once it stops dripping"],
      ["<strong>Channeling</strong>", "Water bypassing the roots straight to the drain"],
      ["<strong>Confidence</strong>", "The brain&rsquo;s trust in its own estimate right now"],
    ], cls="compact", caption="The five words that carry the whole idea."),
  ]})

SECTIONS.append({"id": "why-fuse", "kicker": "Core idea 1", "title": "Why fuse signals: the water bank account",
  "blocks": [
    p("VRWE keeps a <strong>checkbook for water</strong> instead of believing one probe. Money IN "
      "is the water the drippers squirted, known precisely because drippers are calibrated, so "
      "you know exactly how much you put in. Money OUT is what the plant drank plus what "
      "drained away. The running balance is the water really in the pot."),
    p("The plant&rsquo;s drinking, its <strong>transpiration</strong>, can be estimated from heat "
      "and light, because a plant pulls water faster when it is warmer and brighter" +
      _c("koehler-transpiration-vpd-2023") + ". So even without trusting the sensor, the brain has a "
      "good independent guess of OUT. The sensor becomes one statement to check "
      "against the balance, not the sole source of truth."),
    figure(L.bars("One watering cycle, as a bank balance",
            [("Start", 55), ("+ IN (irrigation)", 75), ("- drank (uptake)", 66), ("- drained", 60)],
            unit="%", note="Each cycle: add what you poured in, subtract what the plant drank and what ran off.",
            maxv=85), 2,
      "The estimate is rebuilt every cycle like a running balance. The ending number is the brain&rsquo;s "
      "best guess of real root-zone water, before it even looks at the sensor."),
    figure(grid([
            card("Inputs IN", "Measured irrigation volume from calibrated drippers.", "trusted"),
            card("Inputs OUT", "Plant uptake estimated from temperature and light, plus drainage.", "estimated"),
            card("One vote", "The raw sensor VWC reading, checked, not obeyed.", "cross-check"),
            card("Estimate + confidence", "All signals combined into one number, with a trust score attached.", "output"),
           ], cols=2), 3,
      "Several signals feed one combined estimate. Because the brain has multiple independent clues, "
      "a single wrong signal can be outvoted instead of obeyed."),
    callout("key", "The point of fusing signals",
      p("Listen to only one sensor and a single bad reading becomes a bad decision. When several "
        "independent signals all feed the estimate, one liar gets outvoted. The system stays "
        "right even when one input is wrong.")),
  ]})

SECTIONS.append({"id": "trust-and-uncertainty", "kicker": "Core idea 2", "title": "How trust and uncertainty work",
  "blocks": [
    p("The brain carries a <strong>confidence meter</strong> alongside every estimate, answering "
      "&lsquo;how sure am I?&rsquo;. A number on its own (&lsquo;58% wet&rsquo;) "
      "tells you nothing about whether to bet on it."),
    p("Confidence is high when the independent signals agree, when the sensor, the bank balance and the uptake "
      "estimate all point the same way. Confidence drops when they disagree, when the sensor "
      "says dry but the bank balance says the pot is full. A lying "
      "sensor can only make the system <em>more cautious</em>. It can never trick the brain into "
      "believing there is more room to add water than the balance allows, and that is what "
      "protects the plant."),
    figure(L.zones("The confidence meter and what each zone unlocks", 0, 100,
            [(0, 40, L.REDL, "Low: wait / ask"),
             (40, 70, L.AMBL, "Medium: small safe sip"),
             (70, 100, L.GL, "High: water normally")],
            unit="%",
            note="Higher confidence unlocks bolder action; low confidence forces caution."), 4,
      "Confidence is a dial, not a yes/no. High confidence lets the brain water a full measured "
      "amount. Medium allows only a small safe sip. Low means wait or ask a human."),
    callout("tip", "A faulty sensor is safe",
      ul(["Every estimate ships with a confidence level, not just a number.",
          "Agreement between independent signals raises confidence; disagreement lowers it.",
          "Low confidence triggers caution, never bold action.",
          "A faulty sensor biases toward &lsquo;wait&rsquo;, never toward flooding or starving."], "tight")),
  ]})

SECTIONS.append({"id": "what-it-decides", "kicker": "Core idea 3", "title": "What it actually decides",
  "blocks": [
    p("The brain only ever picks one of three outcomes, driven by "
      "<strong>confidence</strong> and <strong>headroom</strong> (how much room is left before the "
      "pot is full)."),
    figure(L.flow("The three possible decisions",
            [("Confident + room to fill", "water a measured amount"),
             ("Unsure", "wait, or deliver a small safe sip"),
             ("Stuck", "escalate to a human instead of guessing")],
            note="Every path obeys one bound: prefer temporary mild deficit over flooding when uncertain; hard-floor emergency VWC still required."), 5,
      "The whole decision logic collapses to three branches, and all three are bounded by the same "
      "promise."),
    p("It waters a bit when the brain is confident and there is room to fill. It "
      "waits or gives a small safe sip when it is not sure, rather than committing to a full shot. It asks a "
      "human when it is genuinely stuck, when the signals contradict each other and it cannot resolve them. "
      "The whole logic is fenced in by one rule: <strong>prefer temporary mild deficit over flooding when uncertain; hard-floor emergency VWC still required</strong>."),
    callout("key", "The golden rule",
      p("Water more only when confident. When in doubt, do the safe thing. That single bound is what "
        "turns &lsquo;automatic watering&rsquo; from a scary idea into a safe one.")),
  ]})

SECTIONS.append({"id": "shared-drain-howto", "kicker": "In practice", "title": "The shared-drain puzzle, and how it is untangled",
  "blocks": [
    p("A real install is messier than one pot. Often <strong>three grow rooms drain into one shared "
      "sump</strong> (a collection bucket with a pump), and the air conditioner and dehumidifier "
      "drip into that same bucket. When the pump flushes, who caused it is unclear: a "
      "plant overflowing, or just the AC condensate. VRWE untangles this in three steps."),
    steps([
      ("Learn the background drip", "At night, when irrigation is off, the only water reaching the sump is the AC and dehumidifier condensate. The brain learns that steady background drip and subtracts it from every later reading."),
      ("Stagger the watering times", "Each room waters at a different time. Because the flush timing now lines up with one room&rsquo;s watering, the brain can tell which room caused each flush."),
      ("If still ambiguous, say so", "If two events overlap and attribution is genuinely unclear, the reading is marked &lsquo;not sure&rsquo; rather than guessed. The same fail-safe instinct applies as everywhere else."),
    ]),
    figure(grid([
            card("Room A", "Drains into the shared sump.", "source"),
            card("Room B", "Drains into the shared sump.", "source"),
            card("Room C", "Drains into the shared sump.", "source"),
            card("AC + dehumidifier", "Constant condensate drip, learned and subtracted at night.", "noise"),
            card("Shared sump + pump", "One bucket, one flush. Who caused it?", "puzzle"),
            card("Untangle", "Subtract background, stagger timing, flag the unclear ones.", "fix"),
           ], cols=3), 6,
      "Three rooms plus the AC and dehumidifier all empty into one sump, so a single flush is "
      "ambiguous. The three untangling steps recover which room caused which flush."),
    figure(L.line("Staggered watering makes each flush traceable",
            [(0, 5), (1, 38), (2, 12), (3, 6), (4, 41), (5, 14), (6, 7), (7, 39), (8, 10)],
            ["00:00", "A waters", "+30m", "B start", "B waters", "+30m", "C start", "C waters", "+30m"],
            ylab="drain rate", ymin=0, ymax=50,
            note="The low flat baseline is the AC drip; each spike sits under the room that just watered."), 7,
      "Because the rooms water at different times, each drain spike falls directly under the room "
      "that caused it. A flush right after a room waters means that room is full or overflowing."),
    callout("note", "What a post-watering flush tells you",
      p("A flush <em>right after</em> a given room waters is a clear read-back: that room reached "
        "&lsquo;full pot&rsquo; and the extra ran off. That is useful information, not a fault.")),
  ]})

SECTIONS.append({"id": "pitfalls", "kicker": "Watch out", "title": "Pitfalls, and what fools a single sensor",
  "blocks": [
    p("The failure modes below are the situations VRWE is built to survive. They are "
      "the reason it exists. The defence is the same in every case: cross-check against the water "
      "balance and drop confidence, rather than acting on a lone suspicious reading."),
    figure(grid([
            card("Dry-pocket sensor", "The probe sits in a local dry spot and reads dry while the rest of the pot is fine.", "fooled"),
            card("Channeling", "Water races down one side, past both sensor and roots, straight to the drain.", "fooled"),
            card("Shared-drain ambiguity", "One bucket hides which room actually overflowed.", "fooled"),
           ], cols=3), 8,
      "Three classic ways a single signal lies. None of them fools VRWE, because the balance and the "
      "confidence meter catch the contradiction."),
    p("Channeling is worth a closer look, because it is sneaky. In container substrate, water can "
      "follow a <strong>preferential flow path</strong>, a fast channel that routes irrigation "
      "past the root zone entirely" + _c("owen-norden-preferential-flow-2024") + ". The pour-in volume "
      "looks healthy, but the water never reaches the roots. It just shows up as drain. How quickly "
      "water moves through and out of a soilless mix depends on the substrate&rsquo;s own physics" +
      _c("hydrus-soilless-substrate-dynamics") + ", which is why the brain watches drain timing, not "
      "just drain volume."),
    figure(grid([
            card("Top of pot", "Irrigation enters here.", "in"),
            card("Channel path", "Water shoots down one side, past the sensor and roots.", "bypass"),
            card("Drain", "Comes out the bottom almost immediately. Roots stayed dry.", "out"),
           ], cols=3), 9,
      "A cross-section of channeling: water in the top, out the bottom, roots untouched. To the "
      "balance this looks like &lsquo;lots in, lots straight out&rsquo;, a tell-tale the brain "
      "uses to lower confidence."),
    callout("warn", "The defence is always the same",
      p("VRWE does not obey a reading that looks suspicious. It reconciles against the bank "
        "balance, and if they disagree it lowers confidence and acts cautiously. A single fooled "
        "sensor never becomes a flooded or starved plant.")),
  ]})

SECTIONS.append({"id": "expectations", "kicker": "Reality check", "title": "Realistic expectations",
  "blocks": [
    callout("key", "What VRWE promises, and what it does not",
      ol(["<strong>The golden rule.</strong> It waters more only when confident; otherwise it does the safe thing. It is a safety-first estimator, not a mind reader.",
          "<strong>Worst case is over-caution.</strong> A bad sensor makes it cautious, not catastrophic. It will pause or ask before it ever floods or starves.",
          "<strong>Expect &lsquo;wait&rsquo; and &lsquo;ask a human&rsquo; by design.</strong> Those are the system working, not failing.",
          "<strong>Garbage in, garbage out.</strong> The estimate is only as good as its inputs. Accurate dripper volumes and a learned drain baseline matter. Sensor calibration drift quietly erodes every estimate that depends on it." + _c("mane-dielectric-calibration-review-2024")])),
    p("VRWE trades a little speed for a lot of safety. It will occasionally hold back when "
      "a dumb timer would have charged ahead, and that is exactly the point. To go deeper on "
      "what a single probe really measures, read the "
      "<a href='root-zone-teros12.html'>root-zone sensor</a> paper. To understand how the brain tells "
      "a real change from sensor noise before it ever acts, read "
      "<a href='signal-and-noise.html'>signal &amp; noise</a>."),
  ]})
