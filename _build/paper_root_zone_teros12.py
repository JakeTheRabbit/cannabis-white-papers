# -*- coding: utf-8 -*-
"""Paper: root-zone state estimation with the TEROS-12 sensor (beginner-first research)."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        stagecard, grid, card, chip, kv, steps)
import figs_lib as L

SLUG = "root-zone-teros12"
TITLE = "Root-zone state estimation with the TEROS-12 sensor"
EYEBROW = "Precision · Root zone"
SUB = ("A TEROS-12 capacitance probe measures three things in your pot. This guide explains what each "
       "number means, why the raw reading is not the truth, and how to turn it into safe irrigation decisions.")
META = [("gauge", "Precision"), ("image", "12 diagrams"),
        ("quote", "Peer-reviewed · 8 sources"), ("clock", "~18 min read")]
RELATED = ["smart-watering-vrwe", "coco-crop-steering", "signal-and-noise"]
REF_IDS = ["topp-1980-dielectric-vwc", "hilhorst-2000-pore-water-ec",
           "fragkos-2024-teros12-soils-ec", "nasta-2024-teros12-temp-correction",
           "kargas-temp-capacitance-correction-2012", "tavan-2021-sensor-irrigation-soilless",
           "nemali-2006-set-point-irrigation", "meter-teros12-manual"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

SECTIONS.append({"id": "what-this-is", "kicker": "Start here", "title": "What this is, and who it's for",
  "blocks": [
    lead("A TEROS-12 is a small probe you bury in growing media: coco, rockwool or soil. It reports three "
         "things down a single digital wire: how much water is in the media, how salty that water is, and "
         "the temperature. This guide explains, from zero, what each of those numbers means, how the probe "
         "arrives at them, and why you should never wire the probe straight to a valve."),
    p("A single probe is one noisy local witness. It samples a roughly 1010 mL pocket of one pot, not the "
      "whole zone." + _c("meter-teros12-manual") +
      " Everything that follows turns that one local, uncertain reading into a number you can actually "
      "steer irrigation on."),
    ul(["The TEROS-12 reports <strong>volumetric water content (VWC)</strong>, <strong>bulk electrical "
        "conductivity (EC)</strong> and <strong>substrate temperature</strong> over a digital protocol "
        "called SDI-12.",
        "Its &lsquo;volume of influence&rsquo; is only about 1010 mL of media around the prongs. It sees "
        "one local spot, not the average of a tray or a zone.",
        "The goal is to convert that noisy local reading into a trustworthy estimate of stored water, with "
        "the uncertainty stated openly rather than hidden.",
        "No prior knowledge of soil sensors is assumed. Every term is defined the first time it appears."]),
    figure(grid([
        card("The probe", "Three steel prongs create a high-frequency electric field and read it back.", "hardware"),
        card("Volume of influence", "Only ~1010 mL of media around the prongs is sensed.", "~1010 mL"),
        card("The rest of the pot", "Everything outside that pocket is invisible to this probe.", "unseen"),
      ], cols=3), 1,
      "What the probe sees: a small ellipsoid of media around the prongs, not the whole root zone." + _c("meter-teros12-manual")),
    callout("note", "Who this is for",
      p("This is for anyone putting a moisture probe in a pot who wants to steer on it honestly. It pairs "
        "with the <a href='smart-watering-vrwe.html'>smart watering (VWC/EC) guide</a> and the "
        "<a href='coco-crop-steering.html'>coco crop-steering paper</a>.")),
  ]})

SECTIONS.append({"id": "key-terms", "kicker": "Vocabulary", "title": "Key terms, defined once",
  "blocks": [
    p("Here is the small set of words this whole field hangs on. You don't need to memorise them. Each one "
      "comes back in context."),
    defterm("Volumetric water content (VWC)", "The fraction of the media's total volume that is liquid "
            "water, in cubic metres of water per cubic metre of media (m&sup3;/m&sup3;). So 0.34 means "
            "34% of the pot's volume is water. This is the headline irrigation number."),
    defterm("Permittivity (dielectric constant)", "How strongly a material responds to an electric "
            "field. Water's is very high (~80), dry media is ~3&ndash;5 and air is ~1. That huge gap "
            "is the entire trick that lets a sensor &lsquo;feel&rsquo; water it cannot see." + _c("topp-1980-dielectric-vwc")),
    defterm("Capacitance sensor", "A sensor that measures permittivity, then infers VWC from it. The "
            "TEROS-12 is one of these."),
    defterm("Bulk EC vs pore-water EC", "Bulk EC is the conductivity of the whole wet-media mixture "
            "(0&ndash;20000 &micro;S/cm on this probe). Pore-water EC is the conductivity of just the "
            "nutrient solution in the pores, the salt the roots actually feel, estimated indirectly."),
    defterm("DUL / container capacity", "Drained upper limit: how much water this <em>specific</em> pot "
            "holds after it stops draining. It is your steering ceiling, and it is a property of your pot "
            "and media, not a textbook constant."),
    defterm("Resolution vs accuracy", "Resolution is the smallest change reported (0.001 m&sup3;/m&sup3; "
            "VWC). Accuracy is how close the number is to the truth (only &plusmn;0.03 m&sup3;/m&sup3; "
            "with the generic calibration). A precise-looking number can still be wrong." + _c("meter-teros12-manual")),
    figure(L.bars("Relative permittivity: why water dominates the reading",
            [("Air", 1), ("Dry substrate", 4), ("Water", 80)], unit="",
            note="Water's permittivity towers over everything else, so it controls the sensor's response.",
            maxv=90), 2,
      "Liquid water has a permittivity around 80 versus ~3&ndash;5 for dry media and ~1 for air, so even "
      "a little water swings the bulk reading hard." + _c("topp-1980-dielectric-vwc")),
    figure(grid([
        card("Solids", "The coir, rockwool fibre or soil grains themselves.", "fraction"),
        card("Air", "Air-filled pore space between the solids.", "fraction"),
        card("Water", "Liquid in the pores. VWC = this volume / total volume.", "VWC"),
      ], cols=3), 3,
      "A unit volume of media splits into solids, air and water. VWC is just the water slice divided by the whole."),
  ]})

SECTIONS.append({"id": "how-it-measures", "kicker": "Core content", "title": "How the probe turns an electric field into a water number",
  "blocks": [
    p("The TEROS-12 is a <strong>capacitance probe</strong>. Its prongs create a high-frequency "
      "electric field in the surrounding media and measure how strongly the media stores that field, "
      "which is its permittivity. Because water's permittivity (~80) towers over dry media (~3&ndash;5) "
      "and air (~1), the bulk permittivity rises steeply and predictably as water content rises. That "
      "makes permittivity a stand-in for VWC." + _c("topp-1980-dielectric-vwc")),
    p("The sensor then applies a <strong>calibration equation</strong> (a generic mineral-soil curve by "
      "default) to map measured permittivity to a VWC number, reporting it to 0.001 m&sup3;/m&sup3; "
      "resolution. The catch is baked in from the start: that mapping is media-specific, and the generic "
      "curve is only good to &plusmn;0.03 m&sup3;/m&sup3;." + _c("meter-teros12-manual")),
    ul(["Capacitance and permittivity are the <em>physical</em> quantity. VWC is a <em>derived, calibrated</em> "
        "estimate sitting on top of it.",
        "The permittivity-to-VWC curve is nonlinear, especially near saturation, where the response "
        "flattens and can fake a &lsquo;full&rsquo; reading.",
        "Substrate temperature is read as a useful output and because temperature shifts the dielectric "
        "response, a known effect that can masquerade as a water swing." + _c("nasta-2024-teros12-temp-correction"),
        "The probe outputs over SDI-12. A stale, NaN, or railed value (pinned at 0 or full-scale) is a "
        "hardware fault, not data."]),
    figure(L.line("Permittivity to VWC: a nonlinear calibration curve",
            [(0, 0.02), (1, 0.10), (2, 0.20), (3, 0.30), (4, 0.40), (5, 0.46), (6, 0.49)],
            ["3", "8", "15", "24", "35", "48", "62"],
            ylab="VWC (m³/m³)", ymin=0, ymax=0.55,
            note="Bottom axis is permittivity. The curve flattens at the top, so response near saturation can mimic 'full'."), 4,
      "VWC rises with permittivity but the curve bends and flattens near saturation, so the same VWC step "
      "covers very different permittivity steps." + _c("topp-1980-dielectric-vwc")),
    figure(L.flow("The measurement chain",
            [("Electric field", "prongs energise the media"),
             ("Permittivity", "media stores the field"),
             ("Calibration", "curve maps to water"),
             ("VWC + EC + temp", "reported over SDI-12")],
            note="Bulk EC and temperature branch off the same measurement; all three leave on the SDI-12 wire."), 5,
      "From electric field to a number: every output is downstream of the same physical measurement."),
  ]})

SECTIONS.append({"id": "calibration", "kicker": "Core content", "title": "Calibration: why the default number lies a little",
  "blocks": [
    p("Out of the box the TEROS-12 uses a generic mineral-soil calibration, specified at roughly "
      "&plusmn;0.03 m&sup3;/m&sup3;. A well-built, media-specific calibration can reduce error, but the "
      "cited TEROS-12 experiment tested six inorganic soils at constant temperature, not cannabis in "
      "coco or rockwool; it does not establish a universal &plusmn;0.01&ndash;0.02 accuracy for those "
      "substrates." + _c("fragkos-2024-teros12-soils-ec") + " That difference is not academic. "
      "Crop-steering dryback windows are often <em>narrower</em> than "
      "the &plusmn;0.03 generic error band, so steering on uncalibrated VWC means steering inside the noise."),
    p("A worked headroom example shows the consequence directly. A naive 256 mL of &lsquo;room to "
      "water&rsquo; shrinks to a safe ~109 mL once you account for &plusmn;0.02 accuracy, and to just "
      "~54 mL under the generic &plusmn;0.03. Same pot, same probe. The only thing that changed is how "
      "honestly you treat the error band." + _c("nemali-2006-set-point-irrigation")),
    figure(L.bars("How accuracy erodes usable headroom (same pot)",
            [("Naive estimate", 256), ("Safe @ ±0.02 cal", 109), ("Safe @ ±0.03 generic", 54)],
            unit=" mL",
            note="Wider error band = less water you can safely add before risking overshoot.",
            maxv=300), 6,
      "Usable &lsquo;safe headroom&rsquo; collapses as calibration error grows: from 256 mL naive to ~54 mL "
      "on the generic curve." + _c("nemali-2006-set-point-irrigation")),
    table(["Calibration type", "VWC accuracy", "Resolution", "Tight steering?"], [
      ["Generic mineral (default)", "&plusmn;0.03 m&sup3;/m&sup3;", "0.001 m&sup3;/m&sup3;", "No. Error wider than dryback window"],
      ["Substrate-specific", "Must be validated gravimetrically", "0.001 m&sup3;/m&sup3;", "Potentially. Prove the residual error first"],
    ], cls="compact", caption="Resolution is identical. Accuracy must be measured in the actual media."),
    callout("warn", "Calibration is not a cure-all",
      p("Calibration corrects an additive <em>offset</em>, but gain error and nonlinearity near "
        "saturation persist and do not cancel out in later math. Treat substrate-specific calibration as "
        "<strong>mandatory</strong> for tight steering, not optional, and still respect the residual error.")),
  ]})

SECTIONS.append({"id": "ec-and-limits", "kicker": "Core content", "title": "What EC tells you, and what the probe cannot see",
  "blocks": [
    p("The TEROS-12 measures <strong>bulk EC</strong>, the conductivity of the whole wet-media mixture, "
      "0&ndash;20000 &micro;S/cm. What growers care about is <strong>pore-water EC</strong>: the salt "
      "concentration in the solution actually touching the roots. You get pore-water EC by combining bulk "
      "EC, VWC and temperature through the Hilhorst (2000) model." + _c("hilhorst-2000-pore-water-ec")),
    p("That model is genuinely useful, but it is parameter-sensitive at roughly &plusmn;20% and "
      "unreliable below VWC 0.10 m&sup3;/m&sup3;, where it should not be used at all. The deeper limit is "
      "<strong>representativeness</strong>. The probe integrates one ~1010 mL spot, so channeling, dry "
      "pockets, or poor probe-to-media contact can make a perfectly healthy probe report a number that is "
      "simply not true of the zone." + _c("fragkos-2024-teros12-soils-ec")),
    ul(["Bulk EC is the raw measurement (0&ndash;20000 &micro;S/cm). Pore-water EC is the derived quantity "
        "the roots experience.",
        "Hilhorst (2000) converts bulk EC + VWC + temp to pore-water EC, but is ~&plusmn;20% sensitive and "
        "invalid below VWC 0.10 m&sup3;/m&sup3;." + _c("hilhorst-2000-pore-water-ec"),
        "Representativeness fault: the probe can be fine while its 1010 mL is <em>not</em> representative "
        "of the zone (channeling, air gap, pulled probe).",
        "The sensor cannot see per-pot runoff, effective substrate volume (it shrinks as roots grow), or "
        "whether a commanded irrigation shot was truly delivered."]),
    figure(grid([
        card("Bulk EC", "Conductivity of solids, water and air together. This is what the probe measures directly.", "measured"),
        card("Hilhorst model", "Combines bulk EC, VWC and temp. ~±20%, invalid below VWC 0.10.", "~±20%"),
        card("Pore-water EC", "Salt in the liquid the roots feel. This is the number you actually want.", "derived"),
      ], cols=3), 7,
      "Bulk EC is measured. Pore-water EC is inferred through Hilhorst (2000) and degrades fast in dry "
      "media." + _c("hilhorst-2000-pore-water-ec")),
    table(["The probe CAN see", "The probe CANNOT see", "Workaround"], [
      ["VWC (local spot)", "True zone average across pots", "Multiple probes, a cohort model"],
      ["Bulk EC", "Per-pot runoff volume", "Runoff trays / drain sensors"],
      ["Substrate temperature", "Effective substrate volume (shrinks with roots)", "Periodic re-learning of DUL"],
      ["Derived pore-water EC", "Whether an emitter actually fired", "Flow meter or load-cell weight jump"],
    ], cls="compact", caption="What one TEROS-12 can and cannot tell you, and the second witness that fills each gap."),
  ]})

SECTIONS.append({"id": "steering", "kicker": "How-to", "title": "Using it to steer irrigation, step by step",
  "blocks": [
    p("The practical recipe is one demotion and one promotion. <strong>Demote</strong> the raw VWC "
      "reading from &lsquo;truth&rsquo; to &lsquo;one noisy witness with a confidence score&rsquo;. "
      "<strong>Promote</strong> a small running water-balance model that holds the belief about stored "
      "water and is only <em>nudged</em> by trusted readings."),
    p("You track <strong>dryback</strong> (the VWC fall between shots), watch <strong>specific yield</strong> "
      "(S = change in VWC per delivered mL) to sense when the pot is filling, and anchor your ceiling on "
      "the observed DUL rather than a guessed number. Steer on <em>derivatives</em>, the shape and slope "
      "of the dryback, more than the absolute level, because trends shrug off additive calibration error" + _c("tavan-2021-sensor-irrigation-soilless") +
      ". Never act on a derivative alone without a second witness such as runoff timing or pot weight."),
    steps([
      ("Calibrate to your substrate", "Substrate-specific calibration is mandatory for tight steering. Without it you steer inside the error band."),
      ("Verify probe contact and position", "Good media contact and a fixed, representative spot. A loose probe reports its air gap, not your root zone."),
      ("Learn this pot's DUL", "Anchor the ceiling on ~5 corroborated runoff/weight events, not one, and prefer water-volume space over a raw VWC number."),
      ("Steer on shape, gated by safe headroom", "Act on dryback slope and specific yield, bounded by a lower-confidence headroom estimate, not the naive point estimate."),
      ("Require a second witness", "Runoff onset or load-cell mass must confirm before any signal moves a valve. The reading never reaches the valve alone."),
    ]),
    figure(L.line("A day of dryback: shots, decay and the DUL ceiling",
            [(0, 0.30), (1, 0.44), (2, 0.40), (3, 0.36), (4, 0.45), (5, 0.41), (6, 0.31)],
            ["P0 end", "shot", "+2h", "+4h", "shot", "+2h", "pre-dark"],
            ylab="VWC (m³/m³)", ymin=0.25, ymax=0.5,
            note="Sharp rises are shots; the decay between them is the dryback. The top is the learned DUL ceiling."), 8,
      "Irrigation shots refill toward the DUL ceiling; the slope of the fall between shots is the steering "
      "signal, not the absolute level."),
    figure(L.flow("The steering loop: the reading never touches the valve",
            [("Probe reading", "raw VWC / EC / temp"),
             ("Confidence score", "how much to trust it"),
             ("Belief model", "water-balance estimate"),
             ("2nd-witness gate", "runoff or weight confirms")],
            note="Only after the confidence gate AND a second witness does a valve action happen."), 9,
      "Every reading passes through a confidence score, a belief model and a second-witness gate before it "
      "is allowed to move water." + _c("tavan-2021-sensor-irrigation-soilless")),
  ]})

SECTIONS.append({"id": "troubleshooting", "kicker": "When it goes wrong", "title": "Troubleshooting and pitfalls",
  "blocks": [
    p("Most TEROS-12 disappointments are not the sensor breaking. They are the sensor being "
      "<em>believed</em> when it shouldn't be. Make the first distinction clearly. A <strong>wrong "
      "reading</strong> (the probe is fine but its 1010 mL isn't the zone) is a representativeness fault "
      "that should lower your trust in absolute VWC. A <strong>railed, flatline, NaN or stale "
      "value</strong> is a hardware or cable fault that should stop you acting entirely."),
    p("Watch for VWC that tracks the daily substrate-temperature swing. That is a contact or calibration "
      "artifact, not a real storage change" + _c("kargas-temp-capacitance-correction-2012") + ". Watch for "
      "wetting-versus-drying paths that diverge abnormally (channeling or hydrophobic media), and for one "
      "pot that drifts away from its identically-treated siblings (a dud probe or blocked emitter)."),
    callout("danger", "The cardinal safety rule",
      p("Temperature and EC should move your <strong>trust</strong> in the reading, never the "
        "stored-water number directly. A diurnal-temperature artifact can drive a real dielectric shift "
        "in dry media that mimics a water change" + _c("nasta-2024-teros12-temp-correction") + ". If you let "
        "it write VWC, you will chase ghosts.")),
    figure(L.flow("Fault triage: trust or act?",
            [("Railed / NaN / stale?", "hardware fault → fallback"),
             ("Tracks temperature?", "contact artifact → down-trust"),
             ("One pot unlike siblings?", "local fault → inspect"),
             ("Otherwise", "treat as a noisy but usable witness")],
            note="Hardware faults stop you acting; representativeness faults only lower your trust."), 10,
      "A simple decision order: rule out hardware first, then artifacts, then local faults, before believing the number."),
    table(["Symptom", "Likely cause", "What it is NOT", "Response"], [
      ["VWC railed / flatline / NaN / stale", "Hardware or cable fault", "Real water reading", "Stop steering. Run a bounded safe routine. Page a human"],
      ["VWC swings with diurnal temp", "Poor contact / cal artifact", "A real water change", "Down-trust absolute VWC; check contact" + _c("kargas-temp-capacitance-correction-2012")],
      ["Wetting vs drying diverge oddly", "Channeling / hydrophobic media", "Sensor failure", "Inspect media; re-wet; check probe seating"],
      ["One pot unlike its siblings", "Dud probe or blocked emitter", "A plant problem (yet)", "Inspect emitter and probe before blaming the plant"],
    ], cls="compact", caption="Symptom to cause to response. Note the &lsquo;what it is NOT&rsquo; column, because misdiagnosis is the real cost."),
    callout("warn", "Never hard-write your anchors",
      p("Never let one manual reading or a single human observation hard-write your capacity anchor or "
        "override a safety interlock. Anchors earn their place from corroborated events, not from one good look.")),
  ]})

SECTIONS.append({"id": "expectations", "kicker": "Reality check", "title": "Realistic expectations",
  "blocks": [
    callout("key", "What one probe can and cannot earn",
      p("A single TEROS-12 will not give you a per-zone, ground-truth picture of your root zone, and "
        "treating it as one is the most common and most expensive mistake. With substrate-specific "
        "calibration you can realistically resolve dryback <em>trends</em> and approximate stored water "
        "to about &plusmn;0.01&ndash;0.02 m&sup3;/m&sup3; in the spot the probe occupies. That is good "
        "enough to steer if you account for the uncertainty and cross-check it." + _c("fragkos-2024-teros12-soils-ec"))),
    figure(L.zones("Trust earned: single probe vs probe + witness + calibration",
            0, 100,
            [(0, 45, L.REDL, "single probe alone, wide band, many caveats"),
             (45, 100, L.GL, "probe + 2nd witness + calibration, steering-ready")],
            unit="% trust",
            note="Adding a calibration and an independent witness is what moves you from caveats to control authority."), 11,
      "A lone probe sits in a wide, caveat-heavy uncertainty band. Calibration plus an independent witness "
      "earns a tighter, steering-ready band." + _c("nemali-2006-set-point-irrigation")),
    ul(["Best case with calibration: trustworthy dryback shape and ~&plusmn;0.01&ndash;0.02 m&sup3;/m&sup3; "
        "stored-water estimate for the probe's local spot.",
        "Not achievable alone: per-zone runoff, delivery verification, or a true zone average across pots.",
        "A <strong>load cell</strong> (pot weight) is the highest-value add-on because it is the one "
        "measurement that does not route through dielectric physics.",
        "Expect, and design for, explicit &lsquo;I cannot tell&rsquo; outputs rather than false precision. "
        "Control authority should be earned, not assumed."]),
    p("The mature stance is to demand that the system say <em>when it cannot tell</em>, rather than emit a "
      "confident number it has not earned. Get the probe calibrated, add one independent witness, and read "
      "the <a href='smart-watering-vrwe.html'>smart watering (VWC/EC) guide</a> for how those signals drive "
      "shots, and the <a href='signal-and-noise.html'>signal-and-noise paper</a> for separating a "
      "real trend from sensor noise."),
  ]})
