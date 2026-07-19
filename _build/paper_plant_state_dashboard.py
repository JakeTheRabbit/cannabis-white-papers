# -*- coding: utf-8 -*-
"""Paper: from telemetry to intelligence, the plant-state dashboard (operational)."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        stagecard, grid, card, chip, kv, steps)
import figs_lib as L

SLUG = "plant-state-dashboard"
TITLE = "From telemetry to intelligence: the plant-state dashboard"
EYEBROW = "Precision · Dashboards"
SUB = ("A grow-room screen should show what the plant is doing, not a wall of raw sensor "
       "numbers. Here is how to design one that does.")
META = [("dashboard", "Precision"), ("image", "11 diagrams"),
        ("doc", "Operational guide"), ("clock", "~13 min read")]
RELATED = ["signal-and-noise", "f2-crop-steering", "root-zone-teros12"]
REF_IDS = ["spc-signal-noise-ed", "preattentive-dataviz", "vpd-plant-response",
           "capacitive-soil-moisture", "alarm-mgmt-isa182"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

SECTIONS.append({"id": "intro", "kicker": "Start here", "title": "What this is, and why it matters",
  "blocks": [
    callout("evidence", "Community / evidence note",
      "<p><strong>Provisional:</strong> On-screen advisories (e.g. tip-burn risk timelines) are product-design "
      "examples for operator UX &mdash; not a validated prognostic model.</p>"),
    lead("A modern grow room is wired with sensors measuring air temperature, humidity, VPD, "
         "CO&#8322;, light, substrate moisture, EC, root-zone temperature, pH and power draw, "
         "second by second. The dashboards built to show all of this are walls of "
         "live numbers and graphs. They tell you <em>what</em> is happening. They never tell you what it "
         "<em>means</em>, what is about to happen, or what to do about it."),
    p("This paper makes the case for a different design centre, which we will call <strong>Plant-State "
      "Intelligence</strong>: a screen that reasons about the plant instead of just displaying the "
      "room. The target is a &lsquo;calm dashboard&rsquo;: one that stays quiet most of the time "
      "and speaks only when it has something worth saying. A telemetry-dump dashboard forces the "
      "human to be the integrator, synthesising fifteen graphs into a judgement in real time, often "
      "while tired. A plant-state dashboard does that synthesis for you."),
    callout("note", "What this paper is, and isn't",
      ul(["This is an <strong>operational and product-design guide</strong>, not a horticulture-science paper. Lead-time examples are illustrative UX, not validated predictions. Most claims here are design opinions backed by worked examples.",
          "The aim is a screen that <strong>infers</strong> the plant's state, <strong>predicts</strong> trouble days early, and <strong>prescribes</strong> the next step with its evidence and confidence attached.",
          "The one-line thesis: <em>a cockpit full of gauges is not a co-pilot.</em>"], "tight")),
    figure(L.flow("Where the thinking happens",
            [("Sensors", "raw streams off the room"),
             ("Wall of graphs", "15 live charts, no synthesis"),
             ("Tired human", "must integrate it all, in real time")],
            note="The conventional path: the human is the integrator."), 1,
      "The telemetry-dump path (above) leaves all the reasoning to the human. Plant-State "
      "Intelligence moves that step into the software: sensors &rarr; fusion and inference &rarr; "
      "one plain-language judgement."),
  ]})

SECTIONS.append({"id": "key-terms", "kicker": "Vocabulary", "title": "Key terms, defined from zero",
  "blocks": [
    p("Here are the words before the argument. Don't memorise them. Each one comes back in context."),
    defterm("Telemetry", "The raw measurements streamed off your sensors, second by second: "
            "temperature, humidity, moisture and the rest, before anything is done with them."),
    defterm("VPD (vapour pressure deficit)", "How &lsquo;thirsty&rsquo; the air is for moisture, "
            "which drives how fast a plant transpires. 1.4&ndash;1.6&nbsp;kPa is fine in late flower "
            "but punishing in early veg. The same number means different things at different "
            "stages."),
    defterm("Crop steering", "Deliberately pushing a plant <strong>vegetative</strong> (leafy "
            "growth) or <strong>generative</strong> (flower and resin) by controlling irrigation and "
            "dryback."),
    defterm("Inference", "Estimating something you cannot measure directly, like plant stress, "
            "by combining several things you can measure."),
    defterm("Sensor fusion", "Combining several signals over time into one conclusion. "
            "&lsquo;Leaf temp up&rsquo; alone is noise. &lsquo;Leaf temp up <em>and</em> "
            "transpiration flat <em>and</em> dryback unusually deep&rsquo; is a diagnosis."),
    defterm("Dryback", "How much the substrate dries between irrigations. <em>Dryback depth</em> and "
            "<em>dryback rate</em> are derived crop-steering metrics that matter more than any raw "
            "moisture number."),
    defterm("Leading vs lagging indicator", "A leading indicator is a precursor that warns early. A "
            "lagging indicator is a symptom that confirms damage already happened."),
    defterm("Baseline / trajectory", "The expected envelope for this cultivar, at this stage and "
            "point in the photoperiod, learned from your own past runs."),
    defterm("PPFD / DLI", "PPFD is instantaneous light intensity. DLI is the total daily light "
            "delivered. EC is the salt concentration in the feed or root-zone pore water."),
  ]})

SECTIONS.append({"id": "sensor-problem", "kicker": "The problem", "title": "Why the sensor dashboard falls short",
  "blocks": [
    p("The conventional dashboard rests on one implicit theory: &lsquo;expose every measurement and a skilled "
      "grower will know what to do.&rsquo; That fails in seven predictable ways. Every sensor "
      "measures the plant's <strong>surroundings</strong>, air, root zone, light, and "
      "none measures vigour, stress or transpiration directly. That leaves an inference gap the human "
      "must cross unaided. Capacitive moisture probes, for instance, report water content in the "
      "substrate, never the plant's own water status" + _c("capacitive-soil-moisture") + "."),
    p("It is also reactive. By the time a line crosses a threshold, salt accumulation or a stalled "
      "dryback has been accruing for hours or days. Its static high/low alarms &lsquo;cry "
      "wolf&rsquo;: they fire on transient blips like a door opening or a lights-on spike, so "
      "growers learn to ignore them. Alarm-management standards from process industries put the "
      "alarm-flood threshold at roughly ten alarms per ten minutes and cap high-priority alarms at "
      "about five percent. A grow-room dashboard that buzzes constantly has already lost the "
      "operator's trust" + _c("alarm-mgmt-isa182") + "."),
    figure(L.flow("Seven ways the sensor dashboard fails",
            [("1 Shows the room", "not the plant"),
             ("2 Reactive", "graph looks bad after stress"),
             ("3 No memory", "no context or history"),
             ("4 Cries wolf", "static alarms, fatigue"),
             ("5 One signal at a time", "no cross-channel view"),
             ("6 Cognitive load", "as if it were a feature"),
             ("7 Stops at symptoms", "never names the cause")],
            note="The summary indictment: we built instruments and called them intelligence."), 2,
      "The seven failure modes of a telemetry-dump dashboard. Each is a place where the human is left "
      "doing work the software could do."),
    figure(L.line("The lag between cause and symptom",
            [(0, 2.6), (1, 2.9), (2, 3.3), (3, 3.8), (4, 4.4)],
            ["Day 22", "Day 23", "Day 24", "Day 25", "Day 26"],
            ylab="Pore-water EC", ymin=2, ymax=5,
            note="EC creeps up for four days. Tip burn only appears on Day 26."), 3,
      "Pore-water EC creeps up for four days while the grower notices nothing, until tip burn "
      "appears on Day 26. A single-channel chart shows the cause the whole time, but nobody is "
      "watching that one line at that moment. That is the lag a plant-state system is built to "
      "close" + _c("spc-signal-noise-ed") + "."),
    callout("warn", "Single-channel widgets hide the truth",
      p("The real story about plant health lives in cross-signal, multivariate patterns: "
        "moisture, EC, VPD and transpiration moving together. A wall of single-channel gauges "
        "structurally cannot express that pattern, no matter how many you add.")),
  ]})

SECTIONS.append({"id": "six-inversions", "kicker": "The shift", "title": "Six inversions: from gauge cluster to calm dashboard",
  "blocks": [
    p("Plant-State Intelligence inverts six assumptions baked into the sensor "
      "dashboard. None of these throws the raw data away. It just moves to the "
      "&lsquo;basement,&rsquo; still available on drill-down for the expert and the post-mortem."),
    table(["Axis", "From: gauge cluster", "To: calm dashboard"], [
      ["<strong>Object</strong>", "Instrumentation: show the environment", "Inference: estimate the plant's state"],
      ["<strong>Reference</strong>", "Fixed thresholds", "Learned baselines per cultivar &times; stage &times; photoperiod phase"],
      ["<strong>Breadth</strong>", "One signal per widget", "Multi-input fusion across signals"],
      ["<strong>Timing</strong>", "Lagging symptoms", "Leading precursors"],
      ["<strong>Output</strong>", "Alert: &lsquo;a number moved&rsquo;", "Prescription: action, deadline, consequence"],
      ["<strong>Posture</strong>", "Always-on wall of graphs", "Exception-based, quiet by default"],
    ], caption="The six inversions. The hardest shift is the last one: silence becomes the default state."),
    callout("key", "The plant should win the fight for attention",
      p("An always-on wall of graphs competes with the plant for the grower's attention, and "
        "the plant should win. That is why a prescription replaces a bare alert. It names the action, "
        "the deadline, and the consequence of ignoring it. And it is why silence, not a full screen, is "
        "the healthy resting state.")),
  ]})

SECTIONS.append({"id": "plant-state-model", "kicker": "Core content", "title": "What the system actually infers",
  "blocks": [
    p("The pipeline estimates four (really five) interacting states. <strong>Environmental "
      "state</strong>, temperature, RH, VPD, CO&#8322;, light, is reframed as integrals "
      "and rates: VPD-hours accumulated today, DLI to date, not instants. Plant response to "
      "VPD is non-linear and cumulative rather than tied to any single reading" + _c("vpd-plant-response") +
      ", so the accumulated quantity is the meaningful one. <strong>Substrate state</strong> adds "
      "derived crop-steering metrics: dryback depth and rate, field-capacity recovery, and "
      "shot-to-shot moisture response."),
    p("The <strong>plant physiological state</strong> is the whole point. It is not measured but "
      "<strong>estimated</strong>, by fusing the others into a transpiration proxy, a stress index, "
      "a vigour/stacking trajectory and a steering-response readout. <strong>Operational/equipment "
      "state</strong> and an optional <strong>vision state</strong> (canopy cameras) round it out. "
      "Sensor health itself is treated as a first-class signal, so the system knows when "
      "it is blind."),
    figure(L.flow("From measured states to the inferred plant state",
            [("Environmental", "VPD-hours, DLI, CO₂"),
             ("Substrate", "dryback depth & rate, recovery"),
             ("Equipment + Vision", "pump/valve health, canopy"),
             ("Plant state (inferred)", "transpiration, stress, vigour, steering response")],
            note="Outer measured layers feed inward into the one inferred state at the centre."), 4,
      "Environmental, substrate and equipment/vision states feed inward into the inferred plant "
      "physiological state. That centre is what the grower actually cares about, and the only thing "
      "no sensor reports."),
    table(["Raw value", "Derived, meaningful form"], [
      ["WC = 42%", "Dryback depth 8%, slower than this cultivar's baseline"],
      ["VPD = 1.5 kPa right now", "VPD-hours 18% above the in-range envelope for the day"],
      ["EC = 5.1 mS/cm", "Pore-water EC rising 4 days straight, tip-burn risk"],
      ["Leaf temp +0.6&deg;C", "Transpiration flat despite higher VPD: stomata closing"],
    ], cls="compact", caption="The same number, raw vs derived. The right column is what a plant-state dashboard shows. The left is in the basement."),
    callout("tip", "The output is a short list of named conditions",
      p("This layer does not emit fifteen numbers. It emits a short list of <strong>named "
        "conditions</strong>: &lsquo;dryback stalling,&rsquo; &lsquo;salt accumulating,&rsquo; "
        "&lsquo;over-transpiring,&rsquo; each with a confidence and an evidence chain. "
        "Cameras already on site for security become a horticultural input: canopy colour and "
        "uniformity, lights-on wilt, height and stacking over days, early discoloration.")),
  ]})

SECTIONS.append({"id": "architecture", "kicker": "Core content", "title": "The six-layer pipeline",
  "blocks": [
    p("The system is a six-layer pipeline that maps cleanly onto a Home Assistant&ndash;centred "
      "stack. Most operations already have layers 0 and 1 without realising it. The intelligence "
      "moves to the dashboard long before the actuation does: autonomous control is earned "
      "channel by channel, after advisories prove correct."),
    steps([
      ("Layer 0: Ingest", "Pull every raw stream onto one shared timebase. Most rooms already do this."),
      ("Layer 1: Derive", "Turn raw into meaningful: VPD, dryback %, DLI, recovery slopes, shot response."),
      ("Layer 2: Baseline", "Build per-cultivar / stage / photoperiod envelopes, seeded from horticultural priors and refined on your own runs."),
      ("Layer 3: Infer", "Fuse everything into named conditions with confidence and evidence: rules plus anomaly detection, optionally an LLM reasoning pass."),
      ("Layer 4: Prescribe", "Map each condition to a concrete action with a deadline."),
      ("Layer 5: Present", "The calm dashboard. Optional gated Layer 5b closes the loop on low-risk, explicitly-licensed actions only."),
    ]),
    figure(L.flow("The six-layer pipeline",
            [("0 Ingest", "one timebase"), ("1 Derive", "raw → meaningful"),
             ("2 Baseline", "learned envelopes"), ("3 Infer", "named conditions"),
             ("4 Prescribe", "action + deadline"), ("5 Present", "calm dashboard")],
            note="Optional 5b Closed-Loop branches off Present for low-risk licensed actions only."), 5,
      "The pipeline, layer by layer. Layer 2 baselines can be seeded from published horticultural "
      "targets (Athena targets are one example) before you have any history of your own."),
    callout("note", "Advisory-first is the design, not a limitation",
      p("The human-in-the-loop posture is deliberate. An operation can run permanently at "
        "&lsquo;advise only&rsquo; and capture most of the value. Layer 5b auto-applies only the "
        "low-risk, explicitly-licensed actions. Anything irreversible or expensive stays "
        "human-approved.")),
  ]})

SECTIONS.append({"id": "dashboard-surface", "kicker": "Core content", "title": "The new dashboard surface: four zones",
  "blocks": [
    p("What the grower opens has four zones, in priority order, and on a good day, "
      "three of them are empty. Zone&nbsp;1 is the <strong>Headline</strong>: one line of plant truth "
      "in plain language with a status colour, which is 90% of what a busy grower needs 90% of the "
      "time. Zone&nbsp;2 is the <strong>Watchlist</strong> of things drifting but not yet wrong, "
      "the precursors, and it exists precisely to make the next zone rare. "
      "Zone&nbsp;3 is <strong>Advisories</strong>, the only zone that should ever interrupt, each "
      "prescriptive and time-bound. Zone&nbsp;4 is the <strong>Evidence and raw basement</strong>, "
      "demoted but never deleted."),
    grid([
      card("Zone 1: Headline", "&lsquo;Flower Day 24 &middot; Room 3 &middot; On-track. Steering generative as intended. No action needed.&rsquo;", "always shown"),
      card("Zone 2: Watchlist", "Drifting but not yet wrong: the precursors. Each item is a sentence, not a graph. Often empty.", "usually quiet"),
      card("Zone 3: Advisories", "The only zone that interrupts. Prescriptive and time-bound. Expands to its evidence chain.", "rare by design"),
      card("Zone 4: Evidence / raw", "The old dashboard, demoted. Fused signals, baselines, raw graphs, for drill-down and the post-mortem.", "the basement"),
    ], cols=2),
    p("Colour and layout do real work here. A calm dashboard leans on pre-attentive cues, a "
      "single status colour, position, one bold line, that the eye reads before conscious "
      "attention engages, so the &lsquo;all clear&rsquo; state is grasped at a glance" + _c("preattentive-dataviz") + "."),
    callout("key", "A sample advisory, in full",
      p("&lsquo;Reduce dryback target 3% in Room 3 (Day 24)&hellip; Tip burn likely soon (illustrative) if "
        "unaddressed. Confidence: high. <em>[Show evidence]</em>&rsquo;, and the evidence "
        "expands to the fused signals, the baseline it violated, and the historical precedent. The "
        "old dashboard was 100% Zone 4. The new one leads with Zones 1&ndash;3 and keeps 4 in the "
        "basement.")),
  ]})

SECTIONS.append({"id": "how-to", "kicker": "How to", "title": "The adoption path: crawl, walk, run",
  "blocks": [
    p("This is not a boil-the-ocean rebuild. Each stage ships value and earns the next, and most of "
      "the payoff lands by Stage&nbsp;3, long before any closed-loop control."),
    figure(L.flow("The adoption ladder",
            [("0 Telemetry", "today's raw graphs"),
             ("1 Derive", "meaningful metrics, low effort"),
             ("2 Baseline", "go quiet, kills alarm fatigue"),
             ("3 Fuse", "watchlist + advisories come alive"),
             ("4 Prescribe", "attach actions + deadlines"),
             ("5 Closed-loop", "opt-in, gated")],
            note="Most of the payoff lands by Stage 3. Stage 5 is optional."), 6,
      "Six rungs from telemetry to closed-loop. Stage 2, baseline and go quiet, is the "
      "single biggest step, because it ends alarm fatigue in one move."),
    steps([
      ("Pick one room, one pattern", "Choose a single failure pattern (say, stalling dryback) and implement Stages 1–3 for just that pattern in Home Assistant."),
      ("Run it shadow-mode for a cycle", "Run alongside the existing dashboard for a full cycle. Don't act on it yet. Watch whether it would have been right."),
      ("Prove the lead time", "Measure the gap between the advisory firing and when the problem would have become visible. Prove it on one advisory before scaling."),
      ("Scale pattern by pattern", "Add the next failure pattern, then the next room. Stage 4 (prescribe) and Stage 5 (closed-loop) are opt-in, channel by channel."),
    ]),
    callout("tip", "Stage 4 is a stable, valuable end state",
      p("Advisory-first is not a stepping stone you are obligated to leave. An operation can sit at "
        "Stage&nbsp;4 forever and capture most of the value. Stage&nbsp;5 closed-loop is optional and "
        "gated to low-risk, licensed actions only.")),
  ]})

SECTIONS.append({"id": "pitfalls", "kicker": "Pitfalls", "title": "Trust, confidence, and failure modes",
  "blocks": [
    p("An advisory system that is wrong <em>and</em> confident is worse than no system at all. Trust "
      "is a balance: you spend it with every wrong call and earn it with every right one, so advisory "
      "<strong>precision</strong>, not raw volume, is what drives action. Five "
      "guardrails are non-negotiable."),
    table(["Guardrail", "Failure it prevents", "Mechanism"], [
      ["Cold-start honestly", "False certainty from one cycle", "Seed from horticultural priors, widen confidence bands, label outputs &lsquo;still learning&rsquo;"],
      ["Cheap to correct", "Resentment at wrong calls", "Every advisory is dismissable and markable as a false positive, and the marks tune the baselines"],
      ["Track precision", "Silent quality drift", "Advisory precision and false-positive rate are first-class, visible metrics"],
      ["Human in the loop", "Irreversible or costly mistakes", "Anything expensive or irreversible stays human-approved"],
      ["Never a black box", "Loss of trust in the WHAT", "Every conclusion expands to its evidence chain"],
    ], cls="compact", caption="The five guardrails. Each prevents a specific way an advisory system loses the grower's trust."),
    callout("danger", "Treat the system's own blindness as a signal",
      p("A drifted, noisy or flatlined sensor is itself an advisory. For example: &lsquo;EC probe in "
        "Room 2 reads implausibly flat: suspect failure, EC-derived advisories "
        "paused.&rsquo; A grower who can't see <em>why</em> will, correctly, stop trusting the "
        "<em>what</em>. The system's job is to make the decision obvious, not to make it alone on "
        "anything irreversible or expensive.")),
  ]})

SECTIONS.append({"id": "expectations", "kicker": "Reality check", "title": "Measuring success and realistic expectations",
  "blocks": [
    p("If the new dashboard is working, the grower looks at it <strong>less</strong>, is surprised "
      "<strong>less</strong>, and harvests <strong>more consistently</strong>. Six run-over-run "
      "metrics make that concrete, and for half of them, the success direction is "
      "<em>down</em>."),
    figure(L.bars("Six KPIs and their target direction (illustrative)",
            [("Lead time ↑", 80), ("Surprises ↓", 15), ("Precision ↑", 85),
             ("Dwell time ↓", 25), ("Decisions/wk ↑", 70), ("Outcome variance ↓", 20)],
            unit="", note="Bars show a healthy target profile, not measured data. Direction matters more than level.",
            maxv=100), 7,
      "A healthy target profile across the six KPIs. Lead time, precision and decisions-per-week "
      "should be high. Surprises, dashboard dwell time and outcome variance should be low."),
    ul(["<strong>Lead time</strong>: hours or days between an advisory and when the problem would have become visible. The core KPI. The whole point is catching drift before it becomes damage.",
        "<strong>Surprises</strong>: visible damage with no prior advisory. Drive this to zero.",
        "<strong>Advisory precision</strong>: acted-upon advisories over total, plus the false-positive rate.",
        "<strong>Dashboard dwell time</strong>: lower is better. Attention should return to the plants, not the screen.",
        "<strong>Decisions surfaced per week</strong>: the output is decisions, not pageviews.",
        "<strong>Outcome variance</strong>: yield and quality consistency, cycle over cycle."]),
    callout("key", "The honest framing",
      p("Most of the payoff lands by Stage&nbsp;3, and advisory-first may well be the right permanent "
        "end state. You are never obligated to chase closed-loop control. The working names "
        "(Plant-State Intelligence, &lsquo;calm dashboard&rsquo;) are explicitly placeholders: "
        "substance over branding.")),
    p("Start small. Build the inference layer that catches drift early, see the "
      "<a href='signal-and-noise.html'>signal-and-noise</a> paper for the statistics underneath it, "
      "and feed it the derived crop-steering metrics from "
      "<a href='f2-crop-steering.html'>f2 crop steering</a>. The dashboard is only as good as the "
      "states it reasons over."),
  ]})
