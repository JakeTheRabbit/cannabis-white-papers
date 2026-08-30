# -*- coding: utf-8 -*-
"""Paper: root-zone state estimation with the TEROS-12 sensor (beginner-first research)."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        stagecard, grid, card, chip, kv, steps)
import figs_lib as L

SLUG = "root-zone-teros12"
TITLE = "What your TEROS-12 measures and how to steer irrigation on it"
EYEBROW = "Precision · Root zone"
SUB = ("A TEROS-12 probe buried in your growing media reports three numbers: how much water is stored, "
       "how salty that water is, and the temperature. This guide explains what each number means, why the "
       "raw reading is not yet the truth, and how to convert it into irrigation decisions you can stake a crop on.")
META = [("gauge", "Precision"), ("image", "12 diagrams"),
        ("quote", "Evidence-linked · 8 sources"), ("clock", "~18 min read")]
RELATED = ["smart-watering-vrwe", "coco-crop-steering", "signal-and-noise"]
REF_IDS = ["topp-1980-dielectric-vwc", "hilhorst-2000-pore-water-ec",
           "fragkos-2024-teros12-soils-ec", "nasta-2024-teros12-temp-correction",
           "kargas-temp-capacitance-correction-2012", "tavan-2021-sensor-irrigation-soilless",
           "nemali-2006-set-point-irrigation", "meter-teros12-manual"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

SECTIONS.append({"id": "what-this-is", "kicker": "Start here", "title": "Purpose and scope",
  "blocks": [
    lead("A TEROS-12 is a small probe you push into growing media — coco, rockwool, or soil. It sends three "
         "numbers down a single digital wire: how much water the media holds, how salty that water is, and "
         "the temperature. This guide starts from zero, explains what each number actually represents, how "
         "the probe arrives at it, and why the raw reading alone should never open a valve."),
    p("The probe samples a pocket of roughly 1010 mL (34.2 fl oz) of media around its prongs, not the "
      "whole root zone." + _c("meter-teros12-manual") +
      " Everything that follows turns that one local, uncertain reading into a number you can actually "
      "steer irrigation on."),
    ul(["The TEROS-12 reports <strong>volumetric water content (VWC)</strong>, <strong>bulk electrical "
        "conductivity (EC)</strong> and <strong>substrate temperature</strong> over a digital protocol "
        "called SDI-12.",
        "Its sensing volume is only about 1010 mL (34.2 fl oz) of media around the prongs — one local spot, "
        "not the average of a tray or a zone.",
        "The goal is to convert that noisy local reading into a trustworthy estimate of stored water, with "
        "the uncertainty stated openly rather than hidden.",
        "No prior knowledge of soil sensors is assumed. Every term is defined the first time it appears."]),
    figure(grid([
        card("The probe", "Three steel prongs create a high-frequency electric field and read it back.", "hardware"),
        card("Volume of influence", "Only ~1010 mL (34.2 fl oz) of media around the prongs is sensed.", "~1010 mL"),
        card("The rest of the pot", "Everything outside that pocket is invisible to this probe.", "unseen"),
      ], cols=3), 1,
      "What the probe sees: a small ellipsoid of media around the prongs, not the whole root zone." + _c("meter-teros12-manual")),
    callout("note", "Who this is for",
      p("This is for anyone putting a moisture probe in a pot who wants to steer on it honestly. It pairs "
        "with the <a href='smart-watering-vrwe.html'>smart watering (VWC/EC) guide</a> and the "
        "<a href='coco-crop-steering.html'>coco crop-steering paper</a>.")),
  ]})

SECTIONS.append({"id": "key-terms", "kicker": "Vocabulary", "title": "Definitions",
  "blocks": [
    p("Six words underpin everything in this field. Each is defined here in plain English first, then "
      "used precisely from that point on. They come back in context as you read."),
    defterm("Volumetric water content (VWC)", "Think of your pot as a fixed container. Some of that container "
            "is solid media, some is air in the gaps, and some is liquid water. VWC is the liquid water's "
            "share of the whole, expressed in cubic metres of water per cubic metre of media "
            "(m&sup3;/m&sup3;). So 0.34 means 34% of the pot's total volume is liquid water. "
            "This is the primary number you steer irrigation on."),
    defterm("Permittivity (dielectric constant)", "Water responds to an electric field roughly twenty times "
            "more strongly than dry growing media does — like how a wet sponge conducts electricity far "
            "better than a dry one, because the water is doing almost all the electrical work. Permittivity "
            "is the name for that responsiveness. Water&rsquo;s is ~80; dry media is ~3&ndash;5; air is ~1. "
            "That contrast is the entire trick the probe uses to detect water." + _c("topp-1980-dielectric-vwc")),
    defterm("Capacitance sensor", "A sensor that measures permittivity by applying a high-frequency electric "
            "field and reading how strongly the surrounding material stores it. The TEROS-12 is one of these. "
            "It infers VWC from that permittivity reading, without touching the water directly."),
    defterm("Bulk EC vs pore-water EC", "The probe measures the conductivity of the whole wet-media mixture "
            "together — solids, water, and air — which is called bulk EC (0&ndash;20000 &micro;S/cm on this probe). "
            "What the roots actually experience is pore-water EC: the salt concentration in the liquid sitting "
            "in the gaps between media particles. You cannot read pore-water EC directly; you estimate it from "
            "bulk EC using the Hilhorst (2000) model."),
    defterm("DUL / container capacity", "Drained upper limit: how much water this <em>specific</em> pot "
            "holds after gravity has pulled out all it can. It is your steering ceiling — and it is a property "
            "of your pot and media, not a textbook constant, so you measure it from your own runoff events."),
    defterm("Resolution vs accuracy", "Resolution is the smallest change the probe can report: "
            "0.001 m&sup3;/m&sup3; VWC. Accuracy is how close that number is to reality: only "
            "&plusmn;0.03 m&sup3;/m&sup3; with the generic calibration. The probe prints a precise-looking "
            "number, but precision is not the same as accuracy — a very precise number can still be "
            "consistently wrong." + _c("meter-teros12-manual")),
    figure(L.bars("Relative permittivity: why water dominates the reading",
            [("Air", 1), ("Dry substrate", 4), ("Water", 80)], unit="",
            note="Water's permittivity towers over everything else, so it controls the sensor's response.",
            maxv=90), 2,
      "Liquid water&rsquo;s permittivity (~80) is roughly twenty times that of dry media (~3&ndash;5) and "
      "eighty times that of air (~1). Even a small amount of water swings the probe&rsquo;s reading hard." + _c("topp-1980-dielectric-vwc")),
    figure(grid([
        card("Solids", "The coir, rockwool fibre or soil grains themselves.", "fraction"),
        card("Air", "Air-filled pore space between the solids.", "fraction"),
        card("Water", "Liquid in the pores. VWC = this volume / total volume.", "VWC"),
      ], cols=3), 3,
      "A unit volume of media splits into solids, air and water. VWC is the water slice divided by the whole."),
  ]})

SECTIONS.append({"id": "how-it-measures", "kicker": "Core content", "title": "How the probe measures water without touching it",
  "blocks": [
    p("The TEROS-12 is a <strong>capacitance probe</strong>. Its prongs push a high-frequency electric field "
      "into the surrounding media and read how strongly the media stores that field — a property called "
      "<strong>permittivity</strong>. Because water&rsquo;s permittivity (~80) is roughly twenty times that "
      "of dry media (~3&ndash;5) and eighty times that of air (~1), the bulk permittivity of the media rises "
      "steeply and predictably as water content rises. That makes permittivity a reliable stand-in for "
      "VWC." + _c("topp-1980-dielectric-vwc")),
    p("The probe then applies a <strong>calibration equation</strong> — a generic mineral-soil curve by "
      "default — to map measured permittivity to a VWC number, reporting it to 0.001 m&sup3;/m&sup3; "
      "resolution. The catch is built in from the start: the mapping is media-specific, and the generic "
      "curve is only accurate to &plusmn;0.03 m&sup3;/m&sup3;." + _c("meter-teros12-manual")),
    ul(["Permittivity is the <em>physical</em> quantity the probe measures. VWC is a <em>derived, "
        "calibrated</em> estimate — one layer of math on top of that measurement.",
        "The permittivity-to-VWC curve is nonlinear, especially near saturation, where the response "
        "flattens. Near-full media can report a &lsquo;full&rsquo; reading even when it is not.",
        "Substrate temperature shifts the dielectric response — a known physical effect that can look like "
        "a change in water content if you do not account for it." + _c("nasta-2024-teros12-temp-correction"),
        "The probe outputs data over SDI-12. A stale, NaN, or railed value (pinned at 0 or full-scale) is a "
        "hardware or cable fault, not a data reading."]),
    figure(L.line("Permittivity to VWC: a nonlinear calibration curve",
            [(0, 0.02), (1, 0.10), (2, 0.20), (3, 0.30), (4, 0.40), (5, 0.46), (6, 0.49)],
            ["3", "8", "15", "24", "35", "48", "62"],
            ylab="VWC (m³/m³)", ymin=0, ymax=0.55,
            note="Bottom axis is permittivity. The curve flattens at the top, so response near saturation can mimic 'full'."), 4,
      "VWC rises with permittivity but the curve bends and flattens near saturation. The same VWC step "
      "covers very different permittivity steps depending on where you are on the curve." + _c("topp-1980-dielectric-vwc")),
    figure(L.flow("The measurement chain",
            [("Electric field", "prongs energise the media"),
             ("Permittivity", "media stores the field"),
             ("Calibration", "curve maps to water"),
             ("VWC + EC + temp", "reported over SDI-12")],
            note="Bulk EC and temperature branch off the same measurement; all three leave on the SDI-12 wire."), 5,
      "From electric field to a number: every output is downstream of the same physical measurement. "
      "Calibration is where media-specific error enters."),
  ]})

SECTIONS.append({"id": "calibration", "kicker": "Core content", "title": "Why you must calibrate to your exact substrate",
  "blocks": [
    p("Out of the box the TEROS-12 uses a generic mineral-soil calibration, accurate to only "
      "&plusmn;0.03 m&sup3;/m&sup3;. A <strong>substrate-specific</strong> calibration for your exact "
      "coco or rockwool tightens that to &plusmn;0.01&ndash;0.02 m&sup3;/m&sup3;." + _c("fragkos-2024-teros12-soils-ec") +
      " That difference matters in practice. Crop-steering dryback windows are often <em>narrower</em> than "
      "the &plusmn;0.03 generic error band. Steering on uncalibrated VWC means steering inside the noise."),
    p("A worked headroom example makes the consequence concrete. A naive 256 mL (8.7 fl oz) of &lsquo;room "
      "to water&rsquo; shrinks to a safe ~109 mL (3.7 fl oz) once you account for &plusmn;0.02 accuracy, "
      "and to just ~54 mL (1.8 fl oz) under the generic &plusmn;0.03. Same pot, same probe — the only thing "
      "that changed is how honestly you treat the error band." + _c("nemali-2006-set-point-irrigation")),
    figure(L.bars("How accuracy erodes usable headroom (same pot)",
            [("Naive estimate", 256), ("Safe @ ±0.02 cal", 109), ("Safe @ ±0.03 generic", 54)],
            unit=" mL",
            note="Wider error band = less water you can safely add before risking overshoot.",
            maxv=300), 6,
      "Usable safe headroom collapses as calibration error grows: from 256 mL (8.7 fl oz) naive to "
      "~54 mL (1.8 fl oz) on the generic curve." + _c("nemali-2006-set-point-irrigation")),
    table(["Calibration type", "VWC accuracy", "Resolution", "Tight steering?"], [
      ["Generic mineral (default)", "&plusmn;0.03 m&sup3;/m&sup3;", "0.001 m&sup3;/m&sup3;", "No — error band wider than a typical dryback window"],
      ["Substrate-specific", "&plusmn;0.01&ndash;0.02 m&sup3;/m&sup3;", "0.001 m&sup3;/m&sup3;", "Yes — required for tight steering"],
    ], cls="compact", caption="Resolution is the same either way. Accuracy is what changes. Calibrate to your media before you steer on it."),
    callout("warn", "Calibration does not fix everything",
      p("Calibration corrects an additive <em>offset</em> in the reading, but gain error and nonlinearity "
        "near saturation remain and do not cancel in later math. Treat substrate-specific calibration as "
        "<strong>mandatory</strong> for tight steering, not optional — and still respect the residual error "
        "that remains after you calibrate.")),
  ]})

SECTIONS.append({"id": "ec-and-limits", "kicker": "Core content", "title": "What the EC reading tells you and where it breaks down",
  "blocks": [
    p("The probe measures <strong>bulk EC</strong> — the conductivity of the whole wet-media mixture, "
      "0&ndash;20000 &micro;S/cm. What growers care about is <strong>pore-water EC</strong>: the salt "
      "concentration in the solution actually in contact with the roots. To get pore-water EC from what "
      "the probe reports, you combine bulk EC, VWC, and temperature using the Hilhorst (2000) model." + _c("hilhorst-2000-pore-water-ec") +
      " Think of it like measuring the saltiness of a wet sponge by pushing current through the whole "
      "thing — sponge fibre and water together. The Hilhorst model then estimates the saltiness of "
      "the water alone."),
    p("That model is useful but parameter-sensitive — roughly &plusmn;20% — and unreliable below "
      "VWC 0.10 m&sup3;/m&sup3;, where you should not use it at all. The deeper limit is "
      "<strong>representativeness</strong>: the probe integrates one ~1010 mL (34.2 fl oz) spot. "
      "Channeling, dry pockets, or poor probe-to-media contact can make a perfectly functioning probe "
      "report a number that does not represent the zone." + _c("fragkos-2024-teros12-soils-ec")),
    ul(["Bulk EC (0&ndash;20000 &micro;S/cm) is what the probe measures directly. Pore-water EC is "
        "estimated from it — they are not the same thing.",
        "The Hilhorst (2000) conversion is ~&plusmn;20% sensitive and invalid below VWC 0.10 m&sup3;/m&sup3;." + _c("hilhorst-2000-pore-water-ec"),
        "A representativeness fault: the probe&rsquo;s 1010 mL (34.2 fl oz) pocket can be unrepresentative "
        "of the zone due to channeling, an air gap, or a pulled probe — while the probe itself is working "
        "perfectly.",
        "The sensor cannot see per-pot runoff volume, effective substrate volume (which shrinks as roots "
        "fill the pot), or whether a commanded irrigation shot was actually delivered."]),
    figure(grid([
        card("Bulk EC", "Conductivity of solids, water and air together. This is what the probe measures directly.", "measured"),
        card("Hilhorst model", "Combines bulk EC, VWC and temp. ~&plusmn;20% sensitive; invalid below VWC 0.10.", "~&plusmn;20%"),
        card("Pore-water EC", "Salt in the liquid the roots actually contact. This is what you want to know.", "derived"),
      ], cols=3), 7,
      "Bulk EC is measured directly. Pore-water EC is derived through Hilhorst (2000) and degrades fast "
      "as the media dries." + _c("hilhorst-2000-pore-water-ec")),
    table(["The probe CAN see", "The probe CANNOT see", "Workaround"], [
      ["VWC (local spot)", "True zone average across pots", "Multiple probes, a cohort model"],
      ["Bulk EC", "Per-pot runoff volume", "Runoff trays / drain sensors"],
      ["Substrate temperature", "Effective substrate volume (shrinks with roots)", "Periodic re-learning of DUL"],
      ["Derived pore-water EC", "Whether an emitter actually fired", "Flow meter or load-cell weight jump"],
    ], cls="compact", caption="What one TEROS-12 can and cannot tell you, and the second witness that fills each gap."),
  ]})

SECTIONS.append({"id": "steering", "kicker": "How-to", "title": "Steering irrigation from TEROS-12 readings",
  "blocks": [
    p("The practical method is one demotion and one promotion. <strong>Demote</strong> the raw VWC "
      "reading from &lsquo;truth&rsquo; to &lsquo;one noisy witness with a confidence score&rsquo;. "
      "<strong>Promote</strong> a small running water-balance model that holds the best estimate of "
      "stored water and is only <em>nudged</em> by trusted readings."),
    p("You track <strong>dryback</strong> — the VWC fall between shots — watch "
      "<strong>specific yield</strong> (how much VWC rises per mL delivered) to sense when the pot is "
      "approaching capacity, and anchor your ceiling on the observed DUL rather than a guessed number. "
      "Steer on <em>trends</em> — the shape and slope of the dryback — more than the absolute level, "
      "because trends are insensitive to additive calibration offset." + _c("tavan-2021-sensor-irrigation-soilless") +
      " Never act on a trend alone without a second witness such as runoff timing or pot weight."),
    steps([
      ("Calibrate to your substrate first", "Substrate-specific calibration is the first requirement. "
       "Without it you are steering inside the error band — the reading cannot be trusted tightly enough."),
      ("Verify probe contact and position", "The probe must be seated firmly in the media at a "
       "representative, fixed spot. A loose probe or an air gap reports its surroundings, not your root zone."),
      ("Learn this pot's DUL from corroborated events", "Anchor the capacity ceiling on approximately "
       "five runoff or weight events — not one — and express it as water-volume space rather than a raw VWC number."),
      ("Steer on the dryback slope, bounded by safe headroom", "Act on dryback slope and specific yield, "
       "bounded by a headroom estimate that accounts for calibration error, not the naive point estimate."),
      ("Confirm with a second witness before moving water", "Runoff onset or load-cell mass must confirm "
       "before any signal reaches a valve. The probe reading never drives a valve on its own."),
    ]),
    figure(L.line("A day of dryback: shots, decay and the DUL ceiling",
            [(0, 0.30), (1, 0.44), (2, 0.40), (3, 0.36), (4, 0.45), (5, 0.41), (6, 0.31)],
            ["P0 end", "shot", "+2h", "+4h", "shot", "+2h", "pre-dark"],
            ylab="VWC (m³/m³)", ymin=0.25, ymax=0.5,
            note="Sharp rises are shots; the decay between them is the dryback. The top is the learned DUL ceiling."), 8,
      "Irrigation shots push VWC up toward the DUL ceiling; the slope of the fall between shots is the "
      "steering signal, not the absolute level at any one moment."),
    figure(L.flow("The steering loop: the reading never touches the valve alone",
            [("Probe reading", "raw VWC / EC / temp"),
             ("Confidence score", "how much to trust it"),
             ("Belief model", "water-balance estimate"),
             ("2nd-witness gate", "runoff or weight confirms")],
            note="Only after the confidence gate AND a second witness does a valve action happen."), 9,
      "Every reading passes through a confidence score, a belief model, and a second-witness gate "
      "before it is allowed to move water." + _c("tavan-2021-sensor-irrigation-soilless")),
  ]})

SECTIONS.append({"id": "troubleshooting", "kicker": "When it goes wrong", "title": "Diagnosing a bad reading before blaming the sensor",
  "blocks": [
    p("Most TEROS-12 problems are not the sensor failing. They are the sensor being "
      "<em>believed</em> when it should not be. Draw the first distinction clearly: a <strong>wrong "
      "reading</strong> — where the probe is working but its 1010 mL (34.2 fl oz) does not represent "
      "the zone — is a representativeness fault. It should lower your trust in the absolute VWC number. "
      "A <strong>railed, flatline, NaN, or stale value</strong> is a hardware or cable fault. "
      "It should stop all automated action."),
    p("Watch for VWC that tracks the daily substrate-temperature cycle. That is a contact or calibration "
      "artifact, not a real change in stored water." + _c("kargas-temp-capacitance-correction-2012") +
      " Watch for wetting and drying paths that diverge abnormally — a sign of channeling or hydrophobic "
      "media. Watch for one pot drifting away from identically-treated neighbours — likely a blocked "
      "emitter or a dud probe, not a plant problem."),
    callout("danger", "Temperature and EC should move your trust, not the water number",
      p("Temperature and EC should move your <strong>trust</strong> in the reading, not the "
        "stored-water estimate directly. A diurnal temperature cycle can produce a real dielectric shift "
        "in dry media that looks like a change in water content." + _c("nasta-2024-teros12-temp-correction") +
        " Let that shift write VWC and you will be irrigating in response to physics, not plant need.")),
    figure(L.flow("Fault triage: hardware first, then artifacts, then local faults",
            [("Railed / NaN / stale?", "hardware fault → fallback"),
             ("Tracks temperature?", "contact artifact → down-trust"),
             ("One pot unlike siblings?", "local fault → inspect"),
             ("Otherwise", "treat as a noisy but usable witness")],
            note="Hardware faults stop you acting; representativeness faults only lower your trust."), 10,
      "Work down the list in order: rule out hardware faults first, then artifacts, then local faults, "
      "before accepting the number as usable."),
    table(["Symptom", "Likely cause", "What it is NOT", "Response"], [
      ["VWC railed / flatline / NaN / stale", "Hardware or cable fault", "Real water reading", "Stop steering. Run a bounded safe routine. Alert a human"],
      ["VWC swings with diurnal temp", "Poor contact / calibration artifact", "A real water change", "Down-trust absolute VWC; check probe seating" + _c("kargas-temp-capacitance-correction-2012")],
      ["Wetting vs drying diverge oddly", "Channeling / hydrophobic media", "Sensor failure", "Inspect media; re-wet; check probe seating"],
      ["One pot unlike its siblings", "Blocked emitter or dud probe", "A plant problem (yet)", "Inspect emitter and probe before blaming the plant"],
    ], cls="compact", caption="Symptom to cause to response. The &lsquo;what it is NOT&rsquo; column is the most useful — misdiagnosis is the real cost."),
    callout("warn", "Anchors must be earned from multiple events",
      p("A single manual reading or one human observation should never hard-write a capacity anchor or "
        "override a safety interlock. Anchors earn their place from corroborated events across multiple "
        "fills, not from one good look.")),
  ]})

SECTIONS.append({"id": "expectations", "kicker": "Reality check", "title": "Expected results and limitations",
  "blocks": [
    callout("key", "The honest account",
      p("A single TEROS-12 will not give you a per-zone, ground-truth picture of your root zone. "
        "Treating it as one is the most common and most expensive mistake. With substrate-specific "
        "calibration you can realistically resolve dryback <em>trends</em> and approximate stored water "
        "to about &plusmn;0.01&ndash;0.02 m&sup3;/m&sup3; in the spot the probe occupies. That is enough "
        "to steer on — if you account for the uncertainty and cross-check it." + _c("fragkos-2024-teros12-soils-ec"))),
    figure(L.zones("Trust earned: single probe vs probe + witness + calibration",
            0, 100,
            [(0, 45, L.REDL, "single probe alone, wide band, many caveats"),
             (45, 100, L.GL, "probe + 2nd witness + calibration, steering-ready")],
            unit="% trust",
            note="Adding a calibration and an independent witness is what moves you from caveats to control authority."), 11,
      "A lone probe sits in a wide, caveat-heavy uncertainty band. Add substrate-specific calibration "
      "and one independent witness and the band tightens to a range you can steer from." + _c("nemali-2006-set-point-irrigation")),
    ul(["Best case with substrate-specific calibration: trustworthy dryback shape and "
        "~&plusmn;0.01&ndash;0.02 m&sup3;/m&sup3; stored-water accuracy for the probe&rsquo;s local spot.",
        "Not achievable with one probe alone: per-zone runoff, delivery verification, or a true zone "
        "average across pots.",
        "A <strong>load cell</strong> (pot weight) is the highest-value add-on because it measures water "
        "stored directly, without routing through dielectric physics.",
        "Design for explicit &lsquo;I cannot tell&rsquo; outputs rather than false precision. "
        "Control authority should be earned from the data, not assumed."]),
    p("The mature approach is to require the system to say <em>when it cannot tell</em>, rather than "
      "emit a confident number it has not earned. Calibrate first, add one independent witness, then read "
      "the <a href='smart-watering-vrwe.html'>smart watering (VWC/EC) guide</a> for how those signals "
      "drive shots, and the <a href='signal-and-noise.html'>signal-and-noise paper</a> for separating "
      "a real trend from sensor noise."),
  ]})
