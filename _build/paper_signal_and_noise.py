# -*- coding: utf-8 -*-
"""Paper: signal and noise, telling a real change from sensor wobble (precision)."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        stagecard, grid, card, chip, kv, steps)
import figs_lib as L

SLUG = "signal-and-noise"
TITLE = "Signal and noise: precision cultivation"
EYEBROW = "Precision · Signal & noise"
SUB = ("Tell a real change in your plants and root zone apart from random sensor wobble, "
       "and act only when it matters.")
META = [("gauge", "Precision"), ("image", "9 diagrams"),
        ("quote", "Evidence-linked · 9 sources"), ("clock", "~14 min read")]
RELATED = ["root-zone-teros12", "smart-watering-vrwe", "closed-loop"]
REF_IDS = ["shewhart-control-chart", "deming-funnel-tampering", "western-electric-rules-anhoj",
           "nyquist-shannon-sampling", "replication-reduces-variance", "bogena-soil-sensor-calibration",
           "roberts-ewma-1959", "greenhouse-uniformity-crop-growth", "snr-engineering-origin"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

SECTIONS.append({"id": "what-this-is", "kicker": "Start here",
  "title": "What this is, and why a grow room is really a listening problem",
  "blocks": [
    callout("evidence", "Grain of salt",
      "<p><strong>Borderline:</strong> Alarm-noise percentages and control-rule mashups should be replaced with "
      "<em>your</em> measured false-positive rate. Name Western Electric vs Nelson rules correctly if you implement them.</p>"),
    lead("Every sensor reading in your grow room is two things added together: the real story "
         "(the <strong>signal</strong>) and meaningless jitter (the <strong>noise</strong>). Your "
         "whole job is seeing the first through the second."),
    p("The hard part of growing has moved from collecting data to reading it. Sensors are cheap and "
      "dashboards are pretty, yet most decisions still run on gut feel. Collecting <em>data</em> used "
      "to be the work. Now the work is separating the meaningful pattern from the meaningless wobble. "
      "This paper teaches you to hear what your plants are telling you above the static, and, just as "
      "important, when to do nothing."),
    p("A single flower room can generate hundreds of thousands of datapoints a week" + _c("greenhouse-uniformity-crop-growth") +
      ", so a method for safely ignoring most of them is not optional. More data is not more insight. "
      "A firehose of low-quality data is harder to act on than a trickle of good data."),
    figure(L.line("The same data, two readings: signal hidden inside noise",
            [(0, 60), (1, 55), (2, 58), (3, 51), (4, 53), (5, 47), (6, 49), (7, 43), (8, 45), (9, 40)],
            ["0h", "", "", "", "", "", "", "", "", "9h"],
            ylab="VWC %", note="Jagged = what the sensor prints. The eye wants to react to every dip. The real story is the steady downward dry-down underneath."), 1,
      "One smooth trend (a normal dry-down) lives under a jagged line of sensor jitter. Same numbers, "
      "two completely different stories. Only one of them is worth acting on."),
    callout("key", "The one-line reframe",
      p("You don't have a data problem. You have a <strong>signal-to-noise problem</strong>. Most "
        "grow-room &lsquo;alerts&rsquo;, are often noise until tuned: transients "
        "that fix themselves before any action would have mattered.")),
  ]})

SECTIONS.append({"id": "key-terms", "kicker": "Plain-language dictionary",
  "title": "Key terms, defined once",
  "blocks": [
    p("The vocabulary comes from radio engineering, manufacturing and statistics, so the words can "
      "sound intimidating. They are not. <strong>Signal-to-noise ratio (SNR)</strong> is how loud the "
      "thing you care about is compared to everything else competing for your "
      "attention" + _c("snr-engineering-origin") + ". A high-SNR room is calm and decisive. A low-SNR "
      "room is anxious and reactive."),
    defterm("Signal", "A real, meaningful change worth acting on: a sustained trend, a step "
            "change, or a repeating daily rhythm."),
    defterm("Noise", "Meaningless fluctuation: single-reading spikes, jitter, or a transient "
            "from a door opening or an HVAC cycle."),
    defterm("Drift", "A slow, one-way sensor error that masquerades as a real trend. The most "
            "dangerous kind of noise, because it looks exactly like signal."),
    defterm("Averaging / aggregation", "Combining many readings, or many plants, so random quirks "
            "cancel out and the shared story remains."),
    defterm("Control limits", "The boundary, drawn from a process's own history, that "
            "separates normal variation from abnormal."),
    defterm("Calibration", "Checking a probe against a known reference and correcting it, so its "
            "readings stay honest over time. <a href='glossary.html#gl-calibration'>Glossary &rarr;</a>"),
    table(["Signal: react to this", "Noise: ignore this"], [
      ["Sustained trend over many readings", "A single-reading spike"],
      ["Step change that holds", "Jitter smaller than the sensor's accuracy"],
      ["Diurnal (day/night) rhythm", "Transient from a door, vent or HVAC cycle"],
      ["Several sensors agree on the move", "One lone probe disagreeing with its neighbours"],
      ["A trend confirmed against a reference", "Slow drift from an uncalibrated probe"],
    ], cls="compact", caption="At a glance: the shapes of signal versus the shapes of noise."),
  ]})

SECTIONS.append({"id": "where-noise-comes-from", "kicker": "Core idea 1",
  "title": "Where the noise comes from",
  "blocks": [
    p("You cannot reduce what you cannot name. Grow-room noise enters through six channels. Three are "
      "<strong>physical and inherent</strong>: the sensor itself (electronic jitter, drift, no "
      "calibration), placement (a probe near a vent or light, or a sample of one), and biology "
      "(one plant differs from the next). The other three are <strong>procedural</strong>, and "
      "therefore the cheapest to fix: the environment (doors, HVAC cycling), the operator (inconsistent "
      "manual sampling) and the data pipeline (logging gaps, mixed-up units, clock skew)."),
    figure(L.flow("The six sources feeding measured noise",
            [("Sensor", "jitter, drift, no cal"), ("Placement", "edges, vents, n-of-1"),
             ("Biology", "plant-to-plant spread"), ("Environment", "doors, HVAC cycles"),
             ("Operator", "inconsistent sampling"), ("Data/process", "gaps, units, clock skew")],
            note="First three are inherent. Last three are procedural and cheap to fix."), 2,
      "An Ishikawa (fishbone) view: six bones feed the &lsquo;measured noise&rsquo; you see on the "
      "dashboard. Start with the cheap procedural ones before you blame the hardware."),
    callout("warn", "Drift is the assassin",
      p("Drift moves slowly in one direction, exactly like a real trend, so it fools "
        "you for weeks. Uncalibrated pH and EC probes can drift measurably over weeks to a month" + _c("bogena-soil-sensor-calibration") +
        ". A single probe is a rumour. Calibration against a known reference is the only defence.")),
    p("Sensor-specific calibration is not a nicety. In low-cost permittivity soil-moisture sensors, "
      "applying a sensor-by-sensor calibration cut error by roughly 70% versus the factory default" + _c("bogena-soil-sensor-calibration") +
      ". Most &lsquo;the room is fighting me&rsquo; stories are really &lsquo;I am fighting the "
      "noise&rsquo; stories."),
    table(["Source", "Signature", "Fix", "Cost to fix"], [
      ["Data / process", "Gaps, wrong units, clock skew", "Audit the pipeline, lock units & timestamps", "Low"],
      ["Operator", "Readings that jump with who took them", "Write an SOP: same time, method, spot", "Low"],
      ["Environment", "Spikes tied to doors / HVAC cycles", "Wider dead-bands, filter transients", "Low–med"],
      ["Sensor", "Jitter, one-way drift", "Calibrate on a schedule against a reference", "Med"],
      ["Placement", "One probe off from its neighbours", "Move off edges into the canopy core", "Med"],
      ["Biology", "Plant-to-plant spread", "Aggregate across many plants (can't remove)", "Inherent"],
    ], cls="compact", caption="Six sources, cheapest fix first. Attack the procedural rows before the physical ones."),
  ]})

SECTIONS.append({"id": "averaging-and-sampling", "kicker": "Core idea 2",
  "title": "Averaging and how often to measure",
  "blocks": [
    p("The most powerful, most ignored noise filter in horticulture is <strong>replication</strong>. "
      "Ask one plant how the room is doing and you get a rumour. Average twelve plants across the bench "
      "and the individual quirks cancel, leaving only the shared room signal. The maths is friendly: "
      "the error of an average shrinks with the square root of how many readings you combine" + _c("replication-reduces-variance") +
      ". Four probes roughly halve the noise, nine cut it to a third."),
    p("How often you measure matters just as much. Sample too slowly and a fast pattern folds into a "
      "slow one that was never there. Engineers call this <strong>aliasing</strong>: the "
      "wagon-wheel-spinning-backwards effect from old films. The rule of thumb, from the "
      "Nyquist&ndash;Shannon sampling theorem, is to sample at least twice as fast as the fastest "
      "pattern you need to see" + _c("nyquist-shannon-sampling") + ". To catch a 30-minute irrigation "
      "response, log every 10&ndash;15 minutes."),
    figure(L.line("Undersampling invents a trend that isn't there",
            [(0, 60), (1, 42), (2, 58), (3, 44), (4, 59), (5, 43), (6, 57), (7, 45), (8, 60), (9, 44)],
            ["", "", "", "", "", "", "", "", "", ""],
            ylab="signal", note="The true fast wave oscillates every step. Sample it every other step and you 'see' a slow phantom drift that never happened."), 3,
      "A true fast oscillation, sampled too sparsely, reconstructs as a slow phantom wave. That fake "
      "trend will tempt you to act on nothing at all."),
    callout("tip", "Faster is not free",
      p("Over-sampling adds noise, storage cost and the constant temptation to react to jitter. You "
        "don't weigh yourself every hour and panic at each wobble. Don't do it to your room "
        "either. Match the cadence to the channel.")),
    table(["Channel", "Cadence", "Why"], [
      ["Substrate VWC / EC", "1–5 min", "Fast irrigation responses, needs to resolve dryback shape"],
      ["Air temp / RH / VPD", "1–5 min", "HVAC swings fast, and VPD is the live steering number"],
      ["CO₂", "1–5 min", "Cycles with doors and injection bursts"],
      ["Pour-through pH / EC", "1×/day, fixed time", "A slow drift metric, daily at the same time beats noisy spot checks"],
      ["Plant morphology", "2–3×/week", "Growth is slow, more often just adds operator noise"],
    ], cls="compact", caption="A sensible cadence per channel. Match the sample rate to how fast the thing actually moves."),
  ]})

SECTIONS.append({"id": "control-limits-spc", "kicker": "Core idea 3",
  "title": "Control limits: knowing when a wiggle deserves a response",
  "blocks": [
    p("The most valuable idea in the paper comes from manufacturing's quality revolution: "
      "<strong>statistical process control (SPC)</strong>. Walter Shewhart, working at Bell "
      "Laboratories, split all variation into two kinds" + _c("shewhart-control-chart") + ". "
      "<strong>Common-cause</strong> variation is the natural jitter of a stable process: it lives "
      "inside the control limits and should be left alone. <strong>Special-cause</strong> variation is "
      "a real, assignable event that breaks outside the limits and earns investigation."),
    p("Control limits are computed from the process's own history, conventionally the mean plus "
      "or minus three standard deviations" + _c("shewhart-control-chart") + ", not from a guess. "
      "Here is the hard part: W. Edwards Deming proved that <strong>tampering</strong> (reacting to "
      "common-cause jitter) amplifies a process's variation rather than reducing it" + _c("deming-funnel-tampering") +
      ". SPC gives you permission to do the hardest thing in cultivation: watch a number move and "
      "correctly do nothing."),
    figure(L.zones("Control chart: most points are harmless, one is a signal", 30, 70,
            [(40, 60, L.GL, "±1σ: normal jitter"),
             (35, 65, L.AMBL, "±3σ: control limits"),
             (66, 70, L.REDL, "special cause: investigate")],
            unit=" %VWC",
            note="Points inside ±3σ are common-cause: leave them. A point that rockets past the limit is special-cause: act."), 4,
      "A mean line with a ±1σ band and control limits at ±3σ. Most readings jitter harmlessly inside. "
      "A lone point past the upper limit is the one that earns a response." + _c("shewhart-control-chart")),
    callout("note", "Beyond the limits: the Western Electric rules",
      ul(["<strong>Nelson trend (often 6 points)</strong> all trending the same way: a real drift, even inside the limits",
          "<strong>Western Electric: 8 points</strong> on one side of the mean: the process has shifted",
          "Abnormal <strong>hugging of the mean</strong>: often a sign the data is being over-smoothed or faked"],
         "tight")),
    p("These pattern rules catch real shifts that a single out-of-limits point would miss, and they "
      "do it without raising false alarms on ordinary noise" + _c("western-electric-rules-anhoj") + ". "
      "The lesson is blunt: the over-reactive grower, nudging a stable process all day, is usually the "
      "room's single biggest noise source."),
  ]})

SECTIONS.append({"id": "playbook", "kicker": "Do this Monday",
  "title": "The operator's playbook, step by step",
  "blocks": [
    p("None of the highest-return moves needs new capital. Most need only discipline, "
      "tackled top-down. Here is the order to do it in."),
    steps([
      ("Stop watching live numbers", "A live ticker invites tampering. Look at decision charts on a schedule, not the raw feed all day."),
      ("Set a sampling cadence per channel", "Use the table above. Fast channels fast, slow channels slow, no faster than you'll act on."),
      ("Add a rolling average to every decision chart", "Smooth the line you decide from, but keep a raw view one click away so a real emergency isn't hidden."),
      ("Aggregate across 6–12 probes", "Never single-source a decision. Report the average and let one weird probe be outvoted."),
      ("Write SOPs for manual readings", "Same time, same method, same spot, every time. That kills operator noise for free."),
      ("Calibrate on a logged schedule", "This quarter: a fixed calibration cadence against a reference is your only defence against drift."),
      ("Compute control limits for your top 3 KPIs", "Mean ±3σ from your own history. Now you know what 'abnormal' actually means."),
      ("Audit placement and widen twitchy dead-bands", "Move probes off edges, vents and lights into the canopy core, and loosen dead-bands that chatter."),
    ]),
    callout("key", "The one-sentence test before reacting to any number",
      p("&ldquo;Has this moved <strong>beyond its normal range</strong>, for <strong>longer than one "
        "reading</strong>, and do my <strong>other sensors agree</strong>?&rdquo; If not all three are "
        "yes, it's noise. Walk away.")),
    figure(L.flow("React-or-ignore: three gates",
            [("Beyond limits?", "outside ±3σ"), ("Persists?", "more than one reading"),
             ("Sensors agree?", "neighbours confirm"), ("All yes → ACT", "it's signal"),
             ("Any no → DO NOTHING", "it's noise")],
            note="Three yes/no gates stand between an alarming-looking reading and an actual decision."), 5,
      "The decision flow drawn out: every gate must pass before you touch a dial. One failed gate "
      "sends you to &lsquo;do nothing&rsquo;."),
    p("Three workhorse filters cover almost all grow data: the <strong>moving average</strong> "
      "(simple), the <strong>EWMA</strong> (exponentially-weighted, leaning on recent readings "
      "so it lags less for the same smoothing" + _c("roberts-ewma-1959") + "), and the "
      "<strong>median filter</strong> (which deletes single-point spikes). Start with a window "
      "spanning roughly 30&ndash;60 minutes and adjust."),
    figure(L.line("Raw vs rolling average: the trend becomes unmistakable",
            [(0, 58), (1, 49), (2, 56), (3, 47), (4, 52), (5, 44), (6, 50), (7, 41), (8, 47), (9, 39)],
            ["0h", "", "", "", "", "", "", "", "", "9h"],
            ylab="VWC %", note="The smoothed trend (mentally trace the centre) shows a clean dry-down the raw spikes were hiding, at the cost of a small lag."), 6,
      "A noisy raw line with the smoothed trend running through its centre. The dry-down is now "
      "obvious. The only price is a small, predictable lag, which is why you keep the raw view "
      "handy for genuine emergencies."),
  ]})

SECTIONS.append({"id": "pitfalls", "kicker": "Watch out",
  "title": "Common pitfalls",
  "blocks": [
    p("The two opposite failures are <strong>over-smoothing</strong> and <strong>tampering</strong>. "
      "Filtering is sugar: a little clarifies, too much rots. Crank the window too wide and you erase a "
      "real fast event, a pump failure or an EC spike from a clogged dripper, at exactly "
      "the moment you needed to see it. The opposite mistake is reacting to every twitch, which "
      "destabilises the very room you were trying to steady" + _c("deming-funnel-tampering") + "."),
    p("A specific systems failure is <strong>hunting</strong>. A feedback loop fed noisy data, or "
      "tuned too tight, over-corrects one way. The noisy measurement says it overshot, so it slams "
      "back the other way, and the room oscillates instead of settling. The fingerprint is a regular "
      "saw-tooth in temperature, RH or VWC that <em>isn't</em> driven by day/night. If your HVAC or "
      "fertigation seems to &lsquo;fight itself&rsquo;, suspect a noisy sensor or a too-tight "
      "dead-band before you suspect broken equipment."),
    figure(L.flow("The feedback loop and where noise sneaks in",
            [("Setpoint", "your target"), ("Controller", "decides the move"),
             ("Actuator", "valve / fan / heater"), ("Plant / room", "the real response"),
             ("Sensor", "← NOISE ENTERS HERE")],
            note="Noise injected at the sensor stage gets treated as a real error and triggers a correction, so filter the input right there."), 7,
      "The loop runs setpoint &rarr; controller &rarr; actuator &rarr; room &rarr; sensor and back. "
      "Noise injected at the sensor is the dangerous one: the controller cannot tell it from a real "
      "error, so it acts on a phantom."),
    callout("danger", "Filter at the source, widen the dead-band",
      p("A wider dead-band plus a filtered input often fixes &lsquo;broken&rsquo; climate gear that "
        "was never broken. Filter the controller's input right at the sensor's output, before it "
        "decides anything. Otherwise every loop in the room is reacting to static.")),
  ]})

SECTIONS.append({"id": "realistic-expectations", "kicker": "What to expect",
  "title": "Realistic expectations",
  "blocks": [
    p("Facilities climb a predictable ladder, and knowing which rung you're on tells you what to do "
      "next."),
    grid([
      card("1 · Blind", "Gut only. No data, no method.", "stage"),
      card("2 · Logged", "Data but no method: a wall of noise to panic at.", "stage"),
      card("3 · Filtered", "Smoothing and sampling rules. The big leap.", "stage"),
      card("4 · Controlled", "Acting only on special cause.", "stage"),
      card("5 · Tuned", "Closed-loop, consistency-driven.", "stage"),
    ], cols=5),
    p("Most commercial rooms sit at <strong>Logged</strong>, which is paradoxically more "
      "stressful than flying blind, because now there's a wall of noise to panic about. The goal is "
      "not the summit overnight. It's one rung up. The jump from Logged to Filtered, just "
      "smoothing plus sampling rules, is the highest-return move in this whole paper, and it "
      "costs almost nothing but habit."),
    p("Track <em>few</em> high-signal KPIs, not forty gauges. The metric most tied to commercial "
      "success is often <strong>uniformity</strong>, measured as the batch coefficient of "
      "variation, not peak yield. Reducing the spatial and temporal fluctuation of your "
      "environment (a lower coefficient of variation) has been shown to improve crop growth and "
      "quality" + _c("greenhouse-uniformity-crop-growth") + ". A batch where every plant yields 95g "
      "sells better than one averaging 110g with a 40g spread."),
    table(["Signal-rich KPIs: track these", "Vanity metrics: ignore these"], [
      ["Grams per kWh", "Instantaneous single-sensor temperature"],
      ["Dryback trend", "Total datapoints logged"],
      ["VPD time-in-range", "Peak / record readings"],
      ["DLI delivered vs planned", "Alert count"],
      ["Batch coefficient of variation", "Number of dashboards"],
    ], cls="compact", caption="Coefficient of variation literally measures the noise in your crop. Consistency beats peak performance commercially."),
    callout("key", "The honest summary",
      p("You're chasing a higher signal-to-noise ratio, not a perfect room. Aim for one rung up the "
        "ladder, smooth before you steer, and earn the right to do nothing when a number wobbles.")),
    p("Next: see how a clean, filtered signal actually drives irrigation in "
      "<a href='smart-watering-vrwe.html'>smart watering by VWC &amp; EC</a>, and how that closes the "
      "loop without hunting in <a href='closed-loop.html'>closed-loop control</a>."),
  ]})
