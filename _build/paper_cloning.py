# -*- coding: utf-8 -*-
"""Paper: cloning, taking cannabis cuttings that root reliably (beginner)."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        stagecard, grid, card, chip, kv, steps)
import figs_lib as L

SLUG = "cloning"
TITLE = "Cloning: cuttings that root every time"
EYEBROW = "Propagation · Cloning"
SUB = ("Take cannabis cuttings that root reliably. This walks a beginner from picking a "
       "mother plant to a transplant-ready clone in 14 days.")
META = [("seedling", "Propagation"), ("image", "9 diagrams"),
        ("quote", "Peer-reviewed · 7 sources"), ("clock", "~12 min read")]
RELATED = ["light-acclimation", "ipm-sop", "tissue-culture"]
REF_IDS = ["caplan-2018-stem-cuttings", "esposito-2026-morphology-predictors",
           "kim-2025-light-temp-rh", "landis-2022-iba-hemp-i3", "fattorini-2017-iba-to-iaa",
           "olympios-rootzone-temp", "punja-2023-fusarium-pythium-biocontrol",
           "msu-moisture-propagation", "liu-2023-shade-highlight-acclimation"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

SECTIONS.append({"id": "intro", "kicker": "01 · Start here", "title": "What cloning is and why growers do it",
  "blocks": [
    lead("A <strong>clone</strong> is a cutting taken from a living plant that grows its own roots and "
         "becomes a new, genetically identical plant. No flowers and no seeds are involved. You are "
         "rooting a piece of stem, not germinating a seed."),
    p("Cloning gives every plant in a batch the same genetics as a known, proven plant called the "
      "<strong>mother</strong>. Same genetics means the same growth speed, the same yield and the same "
      "chemistry, so the whole grow runs predictable. That predictability is why nearly every commercial "
      "grow clones rather than seeds."),
    p("A well-run propagation room roots clones at 90 to 95 percent success or better" + _c("caplan-2018-stem-cuttings") +
      ", with cuttings ready to transplant in about 10 to 14 days" + _c("kim-2025-light-temp-rh") +
      ". This guide assumes you have never taken a cutting before and defines every term as it appears."),
    figure(L.flow("From mother plant to transplant",
            [("Mother", "healthy plant kept in growth"), ("Take cutting", "clean 45° cut below a node"),
             ("Stick in cube", "under a humidity dome"), ("Roots emerge", "day 7–14"),
             ("Transplant", "~day 14")]), 1,
      "The whole job in five steps. Roots appear between day 7 and day 14, and the clone "
      "is ready to move on at around two weeks." + _c("kim-2025-light-temp-rh")),
    callout("note", "Who this is for",
      p("Anyone who wants to copy a plant they like and get a uniform batch every time. Pair it with "
        "the <a href='light-acclimation.html'>light acclimation</a> guide for moving fresh clones into "
        "stronger light, and the <a href='ipm-sop.html'>IPM hygiene</a> guide for keeping the room clean.")),
  ]})

SECTIONS.append({"id": "key-terms", "kicker": "02 · The vocabulary", "title": "The words you need before you start",
  "blocks": [
    p("Cloning has its own jargon, and most beginner mistakes come from not knowing what a term means. "
      "Learn these six and the step-by-step sections read plainly."),
    defterm("Node", "The point on a stem where leaves and side-shoots attach. New roots and new "
            "growth both come from nodes, so your cut and your rooting both depend on them."),
    defterm("Mother plant", "A plant kept permanently in vegetative (leafy) growth, never "
            "flowered, purely to supply cuttings."),
    defterm("Cutting / clone", "The severed shoot you are rooting. The two words mean the same thing "
            "once it is off the mother."),
    defterm("Rooting cube", "The rockwool or peat plug the cutting sits in while it roots. It holds "
            "water and air around the stem."),
    defterm("Dome", "The clear plastic lid that traps humidity over the tray. <strong>Burping</strong> "
            "means lifting it briefly to swap stale air for fresh."),
    defterm("Hardening off", "Opening the dome vents in stages, then removing the dome, so the "
            "clones get used to normal room air before transplant."),
    figure(L.flow("Anatomy of a prepared cutting",
            [("Node", "where roots will form"), ("Internode", "bare stem between nodes"),
             ("45° basal cut", "fresh, just below a node"), ("Lower leaves removed", "to reduce water loss"),
             ("Fan tips trimmed", "to ~50–70%"), ("Stem in cube", "1.5–2.5 cm deep")]), 2,
      "A cutting prepared for sticking: a clean angled cut below a node, lower leaves stripped, large "
      "fan-leaf tips trimmed back, and the stem set well into the cube."),
  ]})

SECTIONS.append({"id": "mother-and-cut", "kicker": "03 · The how & why", "title": "Choosing a mother and making the cut",
  "blocks": [
    p("A good clone starts with a good shoot. Pick upright shoots from the upper-to-mid canopy that are "
      "at least 3 mm thick and 15 cm long. Thicker, well-lit shoots carry more stored energy and "
      "root faster than thin, shaded interior growth" + _c("esposito-2026-morphology-predictors") +
      ". Shoot thickness and leaf colour reliably predict how well a cutting will root" + _c("esposito-2026-morphology-predictors") + "."),
    p("Water the mother with <strong>half-strength</strong> nutrients the day before. This lowers the "
      "pressure inside the leaves and stems (their <em>turgor</em>) so the stems are less brittle and "
      "snap less when you cut them. Take cuttings at the start of the light cycle with a sterile blade, "
      "making a clean 45-degree cut just below a node, and drop each cutting straight into a holding jug "
      "of dilute solution so the cut end never sits in air."),
    callout("tip", "Why a 45° cut, and why no air",
      ul(["A <strong>45° cut</strong> exposes more surface area than a flat cut, so more cells can turn into roots.",
          "If the cut end sits in air, the stem draws in an <strong>air embolism</strong> (an air bubble) that blocks water uptake. Keep the end wet from the moment it is cut.",
          "Sterilize the blade between mother plants so you don't carry disease from one to the next." + _c("punja-2023-fusarium-pythium-biocontrol")], "tight")),
    figure(L.bars("Where to take cuttings from on the mother",
            [("Upper-mid (best)", 92), ("Lower interior", 58), ("Soft tip growth", 70)], unit="% root",
            note="Indicative rooting success by shoot origin. Firm, well-lit upper-mid shoots root best.",
            maxv=100), 3,
      "Upright shoots from the well-lit upper-to-mid canopy root most reliably. Weak shaded interior "
      "growth lags well behind." + _c("esposito-2026-morphology-predictors")),
  ]})

SECTIONS.append({"id": "hormone-and-cube", "kicker": "04 · The how & why", "title": "Rooting hormone and the cube",
  "blocks": [
    p("Cuttings have no roots yet, so a <strong>rooting hormone</strong> pushes the stem to "
      "grow them. The active ingredient is usually <strong>IBA (indole-3-butyric acid)</strong>, a "
      "synthetic version of a natural plant root hormone called an auxin" + _c("landis-2022-iba-hemp-i3") +
      ". Inside the stem the plant converts IBA into the active rooting auxin (IAA), which is what "
      "triggers new roots" + _c("fattorini-2017-iba-to-iaa") + ". It sells as a gel or a liquid."),
    p("Make a fresh 45-degree cut right before sticking to expose new tissue, coat the bottom 1&ndash;2 cm "
      "of stem in rooting gel, and insert it 1.5&ndash;2.5 cm into a pre-soaked cube. Firm it just enough "
      "that the cube lifts with the stem when you tug gently, the <em>lift test</em>, but "
      "don't crush the cube."),
    steps([
      ("Pre-soak the cube", "Soak rockwool or peat cubes in clone feed for at least 15 minutes. Let them drain freely. Do NOT squeeze them out, or you crush the air out of them."),
      ("Fresh cut", "Re-cut the stem at 45° just before sticking to open clean, un-embolised tissue."),
      ("Apply hormone", "Gel: dip the cut end about 0.5 in (the lower 1–2 cm). Liquid/alcohol dip: soak the cut end about 30 seconds."),
      ("Stick & lift-test", "Insert 1.5–2.5 cm deep. Tug gently: the cube should rise with the stem."),
    ]),
    callout("warn", "Speed matters",
      p("Keep the time from the final cut to sticking under about 30 seconds. The longer a fresh cut "
        "end sits in air, the more likely an air bubble blocks water uptake and the cutting stalls.")),
    figure(L.line("Hormone concentration vs rooting (typical IBA response)",
            [(0, 55), (1, 74), (2, 88), (3, 90), (4, 78)],
            ["0 (none)", "low", "medium", "high", "too high"],
            ylab="% rooted", ymin=40, ymax=100,
            note="Rooting rises with IBA dose up to a point, then over-strong hormone burns the stem and rooting falls off."), 4,
      "There is a sweet spot. Too little hormone and rooting is slow. Too much scorches the stem base. "
      "Commercial gels come pre-mixed to land in the productive range." + _c("landis-2022-iba-hemp-i3")),
  ]})

SECTIONS.append({"id": "dome-environment", "kicker": "05 · The how & why", "title": "Dome, humidity, temperature and light",
  "blocks": [
    p("A cutting with no roots cannot pull water up the stem, so it survives on humidity until roots "
      "form. That is the entire point of the dome. The dome traps moisture so water enters the "
      "leaves directly from the air while the stem grows roots."),
    p("Keep the air around 24&ndash;26&deg;C and start with very high humidity (85&ndash;95% RH) inside a "
      "closed dome, then step it down as roots develop" + _c("kim-2025-light-temp-rh") + ". Put a heat mat "
      "under the tray to keep the cube itself at 22&ndash;24&deg;C. Roots form faster in warm media than "
      "in warm air, because warm roots grow quicker" + _c("olympios-rootzone-temp") + "."),
    p("Keep light gentle, about 60&ndash;100 PPFD (a measure of light intensity reaching the "
      "plant) in the first days, rising toward 150&ndash;200 by hardening off" + _c("kim-2025-light-temp-rh") +
      ". Measure it <strong>with the dome in place</strong>, because the plastic cuts the light reaching "
      "the cutting underneath."),
    figure(L.zones("Dome humidity by rooting phase", 60, 100,
            [(85, 95, L.GL, "Initial heal (d1–4)"), (80, 85, L.GXL, "Early root (d5–7)"),
             (70, 80, L.AMBL, "Mid root (d8–10)"), (65, 75, L.BLUL, "Harden (d11–14)")],
            unit="% RH",
            note="Humidity is highest at the start and steps down as roots take over water uptake."), 5,
      "Target dome humidity falls in stages across the run as the clone grows roots and can start "
      "drawing its own water." + _c("kim-2025-light-temp-rh")),
    table(["Phase", "Days", "RH", "VPD (kPa)", "Light (PPFD)"], [
      ["Initial healing", "1–4", "85–95%", "0.3–0.5", "60–100"],
      ["Early rooting", "5–7", "80–85%", "0.5–0.7", "80–120"],
      ["Mid rooting", "8–10", "70–80%", "0.6–0.8", "100–150"],
      ["Hardening", "11–14", "65–75%", "0.8–1.0", "150–200"],
    ], cls="compact", caption="Four-phase environment targets, all at 24–26°C air and a 22–24°C cube. VPD is a combined dryness measure; higher = drier air." + _c("kim-2025-light-temp-rh")),
    callout("note", "Air movement, not a fan in the face",
      p("Gentle air movement in the room is good, but never aim a fan directly at un-rooted clones. "
        "With no roots to replace lost water, a direct breeze dries them out and wilts them fast.")),
  ]})

SECTIONS.append({"id": "timeline", "kicker": "06 · Do this", "title": "The 14-day routine, day by day",
  "blocks": [
    p("Cloning is mostly leaving the tray alone at the right times and intervening at the right times. "
      "The schedule below is the whole job."),
    figure(L.flow("The 14-day arc",
            [("d1–4", "dome shut, no touch"), ("d5–7", "first water + open vents"),
             ("d7", "check for white roots"), ("d8–10", "prop vents wider"),
             ("d11", "hardening-off test"), ("d14", "transplant")]), 6,
      "Closed and untouched at the start, then the dome opens in stages as roots appear and the "
      "clone learns to drink for itself."),
    p("<strong>Days 1&ndash;4:</strong> vents fully closed, do not touch. The trapped humidity makes the "
      "cutting close its leaf pores and focus on rooting. <strong>Days 5&ndash;7:</strong> the first "
      "watering usually comes due. Judge it by tray weight. Irrigate when the tray has dropped "
      "40&ndash;50% below its Day 0 weight, and never let it fall below 30% loss, because a permanently "
      "soggy cube rots" + _c("msu-moisture-propagation") + ". The cube fading from dark to light brown is "
      "the same signal."),
    p("Clone feed should run an EC of about 1.5 mS/cm at pH 5.5&ndash;6.0, with the water at "
      "20&ndash;22&deg;C. From day 7 start a daily <strong>burp</strong>, begin propping the vents open, "
      "and lift one edge cube to look for emerging white roots. On day 11 run the hardening-off test: "
      "lift the domes, wait 10 minutes, and if fewer than 5 clones per tray wilt, leave the dome off; if "
      "5 or more wilt, re-dome and retry tomorrow. Transplant at around day 14."),
    figure(L.zones("Vent state across the run", 1, 14,
            [(1, 4, L.REDL, "Closed"), (5, 7, L.AMBL, "Burp 5–10 min/day"),
             (8, 10, L.GXL, "25–50% open"), (11, 14, L.GL, "50–100% open")],
            unit="day",
            note="The dome opens in stages from fully closed to fully off as roots establish."), 7,
      "How far the dome vents are open by day. Closed at the start protects rootless cuttings; fully "
      "open by the end hardens them for room air."),
    table(["Day", "What you do", "What you're looking for"], [
      ["1–4", "Dome shut, do not touch", "Cuttings standing turgid, not wilting"],
      ["5–7", "First water by weight; start opening vents", "Cube fading dark→light; 40–50% weight loss"],
      ["7+", "Daily burp; lift an edge cube", "First white roots emerging"],
      ["11", "Hardening-off test (dome off 10 min)", "<5 wilting per tray → dome stays off"],
      ["14", "Transplant the keepers", "Roots ≥2–3 cm on multiple sides; cube holds together"],
    ], cls="compact", caption="The day-by-day routine condensed. Transplant criteria are the key go/no-go at the end."),
  ]})

SECTIONS.append({"id": "troubleshooting", "kicker": "07 · When it goes wrong", "title": "Why clones fail, and the fix",
  "blocks": [
    p("Most clone failures trace to a handful of causes, and they look distinct enough to diagnose at a "
      "glance. The table below maps each symptom to its likely cause and the fix."),
    table(["Symptom", "Likely cause", "What to do"], [
      ["Severe wilting, days 1–2", "Dome RH too low / light too high / heat mat off", "RH ≥85%, drop PPFD, get the cube to 22–24°C"],
      ["Mold or slimy cubes", "Standing water, poor hygiene, or too warm", "Empty standing water; gloves-only handling; keep cubes <26°C"],
      ["Burnt / crispy leaf tips", "Feed EC or VPD too high (too dry)", "Drop EC 0.2–0.3, raise RH, slow the vent opening"],
      ["Yellowing before roots", "Mother was deficient, or feed EC too low", "Review mother nutrition; nudge EC up next run"],
      ["White fuzzy mold in dome", "Humidity too high with no air exchange", "Burp more often; never skip dome hygiene"],
      ["Uneven / patchy rooting", "Inconsistent cube moisture or hormone", "Soak cubes evenly; consistent gel dip depth"],
    ], cls="compact", caption="Diagnose by symptom, then act. Many of these overlap, so fix the most likely cause first and watch for a day."),
    callout("danger", "Hygiene is non-negotiable",
      p("Disease in a propagation room spreads cutting to cutting through tools and hands. Sterilize "
        "tools for at least 2 minutes in 71% isopropyl alcohol (or chlorine dioxide for at least 180 "
        "seconds), and handle cubes with gloves only. Bare hands spread algae and pathogens" + _c("punja-2023-fusarium-pythium-biocontrol") +
        ". Good hygiene prevents the damping-off and root-rot organisms that wipe out whole trays" + _c("punja-2023-fusarium-pythium-biocontrol") + ".")),
  ]})

SECTIONS.append({"id": "expectations", "kicker": "08 · Reality check", "title": "What good looks like, and what to expect",
  "blocks": [
    p("A realistic first goal is <strong>90 percent</strong> rooting, with experienced rooms hitting 95 "
      "percent or higher" + _c("caplan-2018-stem-cuttings") + ". Expect roots in 10 to 14 days, and treat "
      "anything past 21 days with no roots as a problem to escalate, not a clone to keep waiting on."),
    p("Not every cutting will make it, and that is normal. Sorting at transplant, called "
      "<strong>culling</strong>, is part of the process. <strong>Keepers</strong> have strong "
      "roots and light-green tops. <strong>Rejects</strong> rooted but only put out one to three weak "
      "roots. <strong>Kills</strong> have zero roots and get discarded. Plan for this by taking 15 to 40 "
      "percent more cuttings than the number of plants you actually need, so culls don't leave you short."),
    figure(L.bars("Plan for overage: a 100-plant target at 40% over",
            [("Cuttings taken", 140), ("Veg (rooted)", 120), ("Flowered", 100)], unit=" plants",
            note="Take more than you need so culling at each stage still leaves a full batch.",
            maxv=160), 8,
      "Working back from the number you need to flower, take a healthy surplus up front so culls at "
      "rooting and veg still land you on target."),
    figure(L.bars("Sorting at transplant: keepers, rejects, kills",
            [("Keepers", 90), ("Rejects", 6), ("Kills", 4)], unit="%",
            note="A dialed room sends the large majority through as strong keepers.",
            maxv=100), 9,
      "What a good tray looks like when sorted: most cuttings are strong keepers, with a small tail of "
      "weak rejects and a few kills." + _c("caplan-2018-stem-cuttings")),
    p("Some genetics root slower. For slow-to-root cultivars, take the cuttings a few days "
      "earlier so they still hit the transplant date on schedule. Record everything, tray "
      "weights, EC and pH, success rate per batch, because clone data drives every decision "
      "downstream in the grow."),
    callout("key", "Three honest truths",
      ol(["<strong>90% is the floor, not the ceiling.</strong> A new grower hitting 90% is doing well; a dialed room runs 95%+. Below 80% means something in the environment or hygiene is off.",
          "<strong>Culling is success, not failure.</strong> Throwing out weak clones up front protects the uniformity of the whole batch.",
          "<strong>The environment does the work.</strong> Humidity, cube temperature and light matter more than any brand of hormone. Dial those in first."])),
    p("Once your clones are rooted and hardened off, the next job is moving them into stronger "
      "light without shocking them. See the <a href='light-acclimation.html'>light acclimation</a> "
      "guide. Keep the propagation room clean from day one with the "
      "<a href='ipm-sop.html'>IPM hygiene</a> routine, because a clean room is most of a high success rate."),
  ]})
