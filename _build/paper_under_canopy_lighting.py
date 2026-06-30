# -*- coding: utf-8 -*-
"""Paper: under-canopy and inter-canopy lighting (SCL / ICL) for indoor cannabis.

Imported from an externally-authored standalone white paper ("Photons at the Floor")
and re-expressed in the build DSL so it gets site chrome, nav, search, manifest and the
markdown corpus. The two bespoke SVG figures are lifted verbatim from the source and
loaded from figs_under_canopy.json.
"""
import os, json
from components import p, lead, ul, ol, callout, table, figure, steps

_FIGS = json.load(open(os.path.join(os.path.dirname(__file__), "figs_under_canopy.json"), encoding="utf-8"))
_N = [0]
def fig(key, cap):
    _N[0] += 1
    return figure(_FIGS[key], _N[0], cap)

SLUG = "under-canopy-lighting"
TITLE = "Under-canopy lighting: photons at the floor"
EYEBROW = "Environment · Lighting"
SUB = ("Under-canopy (SCL) and inter-canopy (ICL) lighting put photons where the overhead array "
       "can't reach. The research is consistent: at equal flux you upgrade grade and uniformity more "
       "than gross weight. This covers the light, spectrum, placement, training, and the thermal and "
       "airflow bill most guides skip.")
META = [("sun", "Environment"), ("image", "2 diagrams"),
        ("quote", "Peer-reviewed + trials · 7 sources"), ("clock", "~16 min read")]
RELATED = ["lighting-fundamentals", "airflow-design", "grow-room-systems", "defoliation-training", "mould-risk"]
REF_IDS = ["hawley2018-scl", "icl2025-plants", "fluence-icl-2024", "fluence-broad-2026",
           "farred2025-scirep", "rm2021-light", "aroya-undercanopy"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

# ---------------------------------------------------------------- abstract
SECTIONS.append({"id": "abstract", "kicker": "Abstract", "title": "Photons at the floor",
  "blocks": [
    lead("A top fixture lights a roof, not a plant. By the time photons fight through three or four leaf "
         "layers, the lower third of the canopy is sitting at a fraction of the light its buds need to fill "
         "out &mdash; so it doesn&rsquo;t. Under-canopy lighting (SCL) and inter-canopy lighting (ICL) put "
         "photons where the overhead array can&rsquo;t, and the published work is now consistent: you "
         "don&rsquo;t necessarily gain gross weight at equal total flux, but you upgrade grade, tighten "
         "uniformity, and lift the bottom of the plant from larf to saleable flower."),
    p("None of that is free. Every watt you push below the canopy is a watt of heat in the worst-ventilated "
      "zone in the room, and you&rsquo;re now growing dense bud in air that used to be dead space. This paper "
      "covers the light, the spectrum, the placement, the training, and &mdash; the part most guides skip "
      "&mdash; the thermal and airflow bill that comes due."),
  ]})

# ---------------------------------------------------------------- 1 problem
SECTIONS.append({"id": "light-starved", "kicker": "The problem", "title": "The lower canopy is light-starved",
  "blocks": [
    p("Light attenuates fast through a cannabis canopy. Leaves are extremely good at absorbing the exact "
      "wavelengths that drive photosynthesis, so each layer strips the red and blue out of the beam before it "
      "reaches the next. A top canopy running a healthy 800&ndash;1200 &micro;mol&middot;m&#8315;&sup2;&middot;s&#8315;&sup1; "
      "commonly drops to 100&ndash;200 &micro;mol at the lower bud sites, well under the rough 400&ndash;500 "
      "&micro;mol floor that cannabis needs to set and fill competitive flower."),
    p("The result is the larf you already know: airy, underweight bud on the bottom third that grades B or C, "
      "drags your average down, and costs the same in labour to trim as your A-grade tops. The lower canopy "
      "isn&rsquo;t underperforming because the genetics are weak there. It&rsquo;s underperforming because "
      "it&rsquo;s in the dark."),
    fig("hero", "A top fixture lights a roof. PPFD falls from ~900 &micro;mol at the apex to ~120 at the basal "
        "bud sites; under-canopy bars add the photons the top fixture can&rsquo;t reach."),
    table(["Zone", "PPFD", "Meaning"], [
      ["Top canopy", "800&ndash;1200 &micro;mol", "Typical under a modern LED array"],
      ["Basal bud sites", "100&ndash;200 &micro;mol", "What&rsquo;s left after canopy attenuation"],
      ["Viability floor", "400&ndash;500 &micro;mol", "Minimum for adequate flower development"],
    ], caption="The geometry is the problem, and geometry needs a geometric fix: light delivered at depth, not just from above."),
    callout("note", "SCL vs ICL &mdash; not interchangeable",
      ul(["<strong>SCL (subcanopy / under-canopy):</strong> bars on the bench, pot rims or floor, shining "
          "<em>up</em> into the lower plant.",
          "<strong>ICL (inter-canopy / intracanopy):</strong> bars hung <em>within</em> the canopy, among the "
          "branches, at the basal and middle tiers.",
          "Same goal, different mounting, different airflow consequences."])),
  ]})

# ---------------------------------------------------------------- 2 evidence
SECTIONS.append({"id": "the-evidence", "kicker": "The evidence", "title": "What the research actually shows",
  "blocks": [
    p("The marketing decks all cite &lsquo;20&ndash;60% yield gains&rsquo; without naming a source. The honest "
      "picture from peer-reviewed and controlled commercial work is more specific, and more useful, because it "
      "tells you <em>where</em> the gain comes from."),
    p("<strong>Hawley et al., 2018</strong> &mdash; the Guelph group ran the first controlled cannabis "
      "subcanopy trial in <em>HortScience</em>" + _c("hawley2018-scl") + ". Both red-blue and RGB SCL "
      "significantly increased yield <em>and</em> THC in the lower-canopy bud. The mechanism: improved light "
      "distribution into the lower canopy beats simply raising overhead PPFD &mdash; the whole thesis of the "
      "field. Detail worth tattooing on the wall: in cycle two they <em>left the bottom growth on</em> (instead "
      "of gyping it) and the yield response was stronger. Under SCL, your defoliation logic inverts (Section 7)."),
    p("<strong>2025, TL vs SCL vs ICL head to head</strong> &mdash; a study in <em>Plants</em> compared "
      "traditional top light against SCL and ICL directly" + _c("icl2025-plants") + ". ICL was the standout, "
      "and both methods improved energy-use efficiency &mdash; the gain per watt was real, not just gross "
      "output bought with more power."),
    table(["Metric (ICL vs top-light control)", "Result"], [
      ["Dry inflorescence yield", "+30% (29.95%)"],
      ["THC accumulation", "+24% (24.4%)"],
      ["Total terpene concentration", "+12% (12.5%)"],
    ], caption="The 2025 Plants trial: ICL led on yield, potency and terpenes, and improved energy-use efficiency."),
    p("<strong>Fluence / Texas Original</strong> &mdash; the trial that keeps you honest" + _c("fluence-icl-2024") +
      ". At <strong>equal total light flux</strong>, moving photons into the canopy via ICL did <em>not</em> "
      "reliably raise <em>total</em> yield versus top-light alone &mdash; but it increased lower-canopy bud size "
      "and <strong>upgraded the grade</strong> (B/C &rarr; B/A) with much less variability. In a price-pressured "
      "market, consistency and grade are the margin, not gross weight."),
    callout("tip", "The honest framing",
      p("If a vendor promises &lsquo;+40% yield&rsquo;, ask at what total flux. Adding fixtures adds photons "
        "adds yield &mdash; trivially. The defensible claim is: <strong>at the same total power, do you get "
        "better grade and uniformity?</strong> The controlled answer is yes. Field data lands realistic averages "
        "around 25&ndash;35%" + _c("aroya-undercanopy") + " &mdash; conditional on cultivar, a willingness to "
        "<em>reduce plant count</em> for the fixtures and airflow, and the accommodations this paper is about. "
        "Achievable, not automatic.")),
  ]})

# ---------------------------------------------------------------- 3 spectrum
SECTIONS.append({"id": "spectrum", "kicker": "Spectrum", "title": "The heavy-red trap",
  "blocks": [
    p("Here&rsquo;s the most expensive mistake in the category. Most under-canopy products are <strong>heavy "
      "red</strong> &mdash; cheap, efficient per photon, looks &lsquo;powerful&rsquo;. It is also the wrong "
      "spectrum below the canopy, and the trials prove it."),
    callout("warn", "Photobleaching",
      p("In the Fluence ICL trials, red intercanopy treatments at <strong>80% and 100% red caused "
        "photobleaching</strong>" + _c("fluence-icl-2024") + " &mdash; the lower bud bleaches, loses pigment "
        "and degrades. They dropped to 60% red. Pushing a high-red bar into a dense lower canopy at close range "
        "bleaches the exact flower you were trying to save.")),
    p("Two things are happening. First, the mid and lower canopy is <em>already</em> red-rich and "
      "far-red-dominant &mdash; the upper leaves absorbed the blue and red on the way down. Stacking more "
      "concentrated red onto that imbalance is the opposite of what the plant needs. Second, photosystems I and "
      "II must be excited roughly equally for efficient photosynthesis; monochromatic red unbalances them."),
    p("<strong>Use a balanced, broad spectrum below the canopy</strong> &mdash; closer to what the plant "
      "evolved under than to a red space heater. Broad-spectrum minimises bleaching risk while still driving "
      "photosynthesis" + _c("fluence-broad-2026") + "; Hawley&rsquo;s red-blue gave consistency, RGB moved "
      "terpenes more. Broad-spectrum white with a measured red component is the safe, productive default."),
    p("<strong>Far-red (700&ndash;750 nm) is a scalpel, not a default.</strong> Upside: the Emerson effect "
      "&mdash; FR added to red/white drives photosynthesis <em>synergistically</em> by balancing PSI and PSII, "
      "and end-of-day FR raised cannabinoid yield in some cultivars" + _c("farred2025-scirep") + ". Downside: "
      "FR is the primary trigger of shade-avoidance &mdash; stretch and loose, airy growth, the last thing you "
      "want low in the canopy. Dose it deliberately; never &lsquo;more is better&rsquo;."),
    table(["Spectrum", "Verdict", "Why"], [
      ["Heavy red (80&ndash;100%)", "Avoid", "Bleaches lower bud; doubles down on an already red-skewed sub-canopy"],
      ["Broad / white + moderate red", "Default", "Lowest bleaching risk, balanced PS excitation, proven yield + grade gains"],
      ["Red-blue", "Good", "Consistent cannabinoid / terpene profile (Hawley)"],
      ["RGB", "Situational", "Stronger terpene shift; more profile variability"],
      ["+ Far-red (dosed)", "Scalpel", "Photosynthetic synergy + cannabinoid upside, but drives stretch &mdash; control it"],
    ], caption="Spectrum decision below the canopy. The category default should be broad, not red."),
  ]})

# ---------------------------------------------------------------- 4 par targets
SECTIONS.append({"id": "par-targets", "kicker": "Dose", "title": "PAR targets and how much light to add",
  "blocks": [
    p("The goal isn&rsquo;t to match top-canopy intensity at the floor &mdash; it&rsquo;s to lift the starved "
      "zone over the threshold where bud development becomes viable, without bleaching."),
    table(["Zone", "Unlit PPFD", "Target with SCL/ICL", "Intent"], [
      ["Apical (tops)", "800&ndash;1200", "unchanged", "Driven by the overhead array; don&rsquo;t chase it higher"],
      ["Middle", "300&ndash;450", "500&ndash;700", "ICL territory &mdash; biggest grade upside"],
      ["Basal", "100&ndash;200", "300&ndash;600", "Lift over the ~400 viability floor"],
    ], caption="PPFD targets by stratum (flower), in &micro;mol&middot;m&#8315;&sup2;&middot;s&#8315;&sup1;."),
    p("Think in <strong>added flux at depth</strong>, not bar wattage. A modest contribution &mdash; on the "
      "order of 25&ndash;60 W&middot;m&#8315;&sup2; of installed sub-canopy fixture depending on geometry "
      "&mdash; is usually enough to clear the threshold. Past the bleaching point you&rsquo;re paying in heat "
      "and pigment loss for negative return."),
    callout("tip", "Hold total flux honest",
      p("To test whether SCL &lsquo;works&rsquo;, run it at <strong>constant total facility flux</strong> first "
        "&mdash; pull a little off the top, add it at depth &mdash; and measure grade and uniformity. That "
        "isolates the geometric benefit from the trivial &lsquo;more light = more yield&rsquo; effect. Then "
        "decide whether to add net flux.")),
  ]})

# ---------------------------------------------------------------- 5 light history
SECTIONS.append({"id": "light-history", "kicker": "Photoacclimation", "title": "The leaf was built by yesterday's light",
  "blocks": [
    p("A leaf is not a fixed solar panel. While it expands it builds its own photosynthetic hardware &mdash; "
      "chloroplast structure, electron-transport capacity, Rubisco, photoprotection &mdash; calibrated to the "
      "light it experiences <em>during</em> development. A shade-grown leaf builds thin, low-capacity, "
      "lightly-defended hardware; the same genetics under bright light build a thicker, higher-capacity leaf. "
      "Rodriguez-Morrison, Llewellyn &amp; Zheng (2021) measured this in cannabis" + _c("rm2021-light") +
      ": leaves acclimated to ~91 vs ~1,238 &micro;mol differed by about <strong>50%</strong> at high "
      "intensity. Same cultivar, different light history, different machine."),
    p("<strong>One &mdash; don&rsquo;t trust a single leaf to predict the canopy.</strong> The same study "
      "found leaf-level photosynthesis saturates well below where <em>whole-plant</em> yield keeps climbing: "
      "dry inflorescence yield rose <strong>linearly to 1,800 &micro;mol</strong> (the highest tested) while a "
      "single leaf&rsquo;s curve flattened far earlier. Don&rsquo;t size under-canopy targets off "
      "leaf-saturation logic."),
    p("<strong>Two &mdash; the lower leaves you&rsquo;re about to light grew up in shade.</strong> Their "
      "installed capacity is shade-grade. Throw sudden high intensity at them and you risk <strong>"
      "photoinhibition before production</strong>, because the photoprotective machinery was never assembled. "
      "Newly-developing leaves re-acclimate far better than mature shade leaves &mdash; the mechanistic case "
      "for <em>ramping</em> intensity rather than slamming it on (Section 10)."),
    callout("note", "Proven vs plausible",
      p("<strong>Proven:</strong> light history shapes a leaf&rsquo;s photosynthetic capacity, demonstrated in "
        "cannabis. <strong>Not proven:</strong> that a specific intensity <em>ramp schedule</em> changes "
        "cannabis yield &mdash; no published trial has tested ramp trajectories against constant intensity. "
        "Ramp because the acclimation mechanism says it lowers photoinhibition risk on shade-developed tissue, "
        "not because anyone has proven a number.")),
  ]})

# ---------------------------------------------------------------- 6 placement
SECTIONS.append({"id": "placement", "kicker": "Geometry", "title": "Fixture placement and mounting",
  "blocks": [
    p("<strong>SCL &mdash; bench / floor mount.</strong> Bars on pot rims or low rails, throwing light upward "
      "into the basal bud sites:"),
    ul(["<strong>Aim up and in.</strong> Simplest to install and clean; lowest disruption to your canopy.",
        "<strong>Standoff distance.</strong> Keep enough gap that you&rsquo;re not scorching the nearest bud "
        "&mdash; bleaching risk scales with proximity &times; red fraction. Broad-spectrum tolerates closer placement.",
        "<strong>Coverage uniformity.</strong> Daisy-chained thin bars with overlapping throw beat a few point "
        "sources. Map it (Section 10), don&rsquo;t eyeball it."]),
    p("<strong>ICL &mdash; in-canopy mount.</strong> Bars hung within the branches at basal and middle tiers:"),
    ul(["<strong>More effective for tall, unpruned genotypes</strong> &mdash; exactly the architecture that "
        "benefits most. This is where the strongest study numbers came from.",
        "<strong>Plan plant count down.</strong> Bars in the canopy need lanes &mdash; the &lsquo;reduce plant "
        "count&rsquo; accommodation the field data assumes.",
        "<strong>Waterproof, cleanable, daisy-chainable.</strong> These live in the humid, sprayed, trimmed "
        "zone &mdash; IP-rated housings and DLC certification (rebate eligibility) are baseline."]),
    fig("mount", "SCL lights from the bench upward &mdash; easy to install and clean. ICL places bars among the "
        "branches at multiple depths &mdash; stronger response on tall, unpruned plants, but it costs you plant "
        "lanes and airflow clearance."),
  ]})

# ---------------------------------------------------------------- 7 training
SECTIONS.append({"id": "training", "kicker": "Training", "title": "Plant training changes when you light from below",
  "blocks": [
    p("This separates operators who get the 30% from operators who bleach their bottoms and rot their cores. "
      "Under-canopy lighting and your training regime are one system, not two."),
    p("<strong>The gyping reversal.</strong> Standard practice strips the bottom 20 cm &mdash; gyping, "
      "lollipopping &mdash; because that growth is shaded, contributes nothing, and invites rot. <strong>Once "
      "you light it, that logic flips.</strong> Hawley&rsquo;s second cycle left the lower growth on precisely "
      "because SCL made those previously-useless leaves and bud sites productive. If you light the bottom then "
      "strip it, you&rsquo;ve paid for fixtures to illuminate bare stem."),
    callout("warn", "The trade-off you&rsquo;re now managing",
      p("Keeping lower growth for the light <em>directly conflicts</em> with the airflow and rot-prevention "
        "reasons you stripped it. You&rsquo;re choosing to grow dense bud in the lowest, most humid, "
        "worst-ventilated zone. That&rsquo;s only safe if Sections 8 and 9 are handled. Lighting the bottom "
        "without fixing the air is how you turn larf into botrytis.")),
    ul(["<strong>Keep:</strong> lower bud sites and the leaves directly feeding them &mdash; now lit and earning.",
        "<strong>Remove:</strong> large fan leaves that <em>shade</em> newly-lit bud sites or <em>trap "
        "humidity</em> against them. Selective, not scorched-earth.",
        "<strong>Tuck before you cut</strong> where you can &mdash; redirect shade without removing photosynthetic area.",
        "<strong>Even canopy / SCROG:</strong> a trellised, evenly-spread canopy lets ICL bars thread through "
        "and lets air move. Packed hedges trap air."]),
    p("<strong>Timing:</strong> run structural defoliation around the usual windows (~day 21, a lighter pass "
      "~day 42 if still dense), but re-target it &mdash; you&rsquo;re opening airflow lanes and removing shade "
      "<em>onto lit bud sites</em>, not clearing dead zone. Go light late in flower; aggressive late defoliation "
      "swings transpiration unpredictably in a zone you&rsquo;ve made humid on purpose."),
  ]})

# ---------------------------------------------------------------- 8 heat
SECTIONS.append({"id": "heat", "kicker": "Thermal", "title": "The heat bill: a watt is a watt",
  "blocks": [
    p("Ignore the marketing about LEDs &lsquo;running cool&rsquo;. For HVAC sizing it&rsquo;s false in the way "
      "that matters. In a sealed room, <strong>essentially all the electrical power you feed a fixture ends up "
      "as heat your HVAC has to remove.</strong> A 600 W LED and a 600 W HPS impose the same cooling load. The "
      "LED&rsquo;s advantage is hitting your target PPFD at <em>fewer watts</em> &mdash; you install fewer "
      "watts, not cooler ones."),
    callout("note", "The core calculation",
      ul(["Sensible heat: <strong>BTU/hr = total fixture watts &times; 3.412</strong>",
          "Worked, 20 m&sup2; room: 25 W/m&sup2; &times; 20 = 500 W installed sub-canopy",
          "500 W &times; 3.412 = <strong>1,706 BTU/hr</strong> additional sensible load",
          "Tons = total BTU/hr &divide; 12,000 &middot; add +20% headroom (+30% sealed CO&sub2;) &middot; round up"])),
    p("That 1,706 BTU/hr sits on top of your overhead array, dehumidifier (nearly 100% of its wattage becomes "
      "in-room heat), equipment and people (~400 BTU/hr each). Lighting is typically 70&ndash;85% of total room "
      "cooling load before SCL &mdash; so a retrofit is a direct, calculable increase to your single largest "
      "load. Size it deliberately; don&rsquo;t assume your AC has the margin."),
    p("<strong>How to measure your actual load:</strong> sum measured wattage from driver labels and a clamp "
      "meter (not marketing specs); apply &times;3.412; add dehumidifier watts (~1:1 to heat), people and "
      "ventilation infiltration; then validate against reality &mdash; log the lights-on temp-rise rate; if the "
      "room heats faster than your BTU math predicts, you&rsquo;ve under-counted a load."),
    callout("warn", "The lights-off trap",
      p("Sensible load drops to <strong>zero the instant lights cut</strong> &mdash; but the plants keep "
        "transpiring (latent load). If cooling is oversized and dehumidification isn&rsquo;t decoupled, "
        "temperature craters, RH spikes to dew point, and you get condensation on leaves &mdash; ideal botrytis "
        "and powdery-mildew conditions. SCL makes it worse: you&rsquo;ve added transpiring bud mass low in the "
        "canopy. Decouple dehumidification from cooling.")),
  ]})

# ---------------------------------------------------------------- 9 airflow
SECTIONS.append({"id": "airflow", "kicker": "Airflow", "title": "The lower-canopy microclimate",
  "blocks": [
    p("You have deliberately created flower in the worst-ventilated zone in the room. The lower canopy is "
      "where air stalls, humidity pools, and botrytis germinates inside dense colas from the inside out. Before "
      "SCL that zone was sparse larf or bare stem. Now it&rsquo;s dense, transpiring bud. The airflow problem "
      "isn&rsquo;t a side note &mdash; it&rsquo;s the direct consequence of doing this at all."),
    ul(["<strong>Stagnant dead spots.</strong> Overhead HAF fans sweep the top; the basal zone sits in still "
        "air below the airstream.",
        "<strong>Added latent load, low down.</strong> New bud mass transpires into the zone with the least "
        "air movement. Moisture has nowhere to go.",
        "<strong>Cold floor, warm air.</strong> Condensation forms near pots and the lowest leaves first "
        "&mdash; exactly where you&rsquo;ve put your new flower."]),
    callout("note", "Sizing the air",
      ul(["Whole-room exchange: target a full air exchange every <strong>1&ndash;3 minutes</strong>",
          "CFM = room volume (ft&sup3;) &divide; exchange interval (min). Example: 2,400 ft&sup3; &divide; 2 = <strong>1,200 CFM</strong>",
          "Carbon-filter penalty: a scrubber adds ~20&ndash;25% static pressure &mdash; size the fan +25%, or rate it at 0.25&Prime; static, not free-air"])),
    p("That covers <em>bulk</em> exchange. It does not solve the sub-canopy microclimate, because room-average "
      "airflow says nothing about the dead zone at the bottom. You need dedicated low-level air movement:"),
    ul(["<strong>Dedicated low fans</strong> aimed <em>through</em> the lower canopy &mdash; the single "
        "highest-leverage move once you light the bottom.",
        "<strong>Sweep, never blast.</strong> Gentle turbulent movement that flexes leaves, not a jet at the "
        "buds &mdash; direct blasting dries trichomes and causes wind burn.",
        "<strong>~one oscillating fan per 4&ndash;6 plants</strong> as a starting density, biased to the lower tier.",
        "<strong>Open the structure</strong> (Section 7) so air can thread through &mdash; fans can&rsquo;t fix a packed hedge."]),
    p("<strong>VPD and dew point at depth:</strong> manage VPD where the bud is, not just at the room sensor. "
      "Reasonable flower targets ~0.8&ndash;1.2 kPa early, tightening to 1.2&ndash;1.6 kPa late. Keep leaf "
      "temperature ~6&ndash;8 &deg;C above dew point, especially at lights-off. Put a sensor <em>in the lower "
      "canopy</em> &mdash; the basal zone reads wetter than room average, and that delta is exactly the risk "
      "SCL introduces."),
    callout("warn", "The compounding failure",
      p("SCL adds bud mass &rarr; in the most humid zone &rarr; with the worst airflow &rarr; transpiring into "
        "still air &rarr; at lights-off when RH spikes. Each factor is survivable alone. Stacked, they&rsquo;re "
        "a botrytis machine. The lighting upgrade is only as good as the air and dehumidification upgrade that "
        "goes with it. Budget for both, or don&rsquo;t do it.")),
  ]})

# ---------------------------------------------------------------- 10 commissioning
SECTIONS.append({"id": "commissioning", "kicker": "Setup", "title": "Commissioning: how to dial it in",
  "blocks": [
    p("Don&rsquo;t install to a spec sheet and walk away. Install, measure, adjust, log. The whole value of "
      "SCL is in the lower-canopy numbers, so that&rsquo;s where you measure."),
    steps([
      ("Baseline map", "Before fitting bars, take PPFD at apical, middle and basal strata across a grid &mdash; quantum sensor, three directions at each point. This is your &lsquo;before&rsquo;."),
      ("Install for uniformity, not peak", "Overlapping daisy-chained bars beat hot-spotted point sources. Set standoff generous initially; you can always move closer."),
      ("Re-map", "Confirm middle/basal land in the target bands (500&ndash;700 / 300&ndash;600 &micro;mol). Hunt for hot spots near fixtures &mdash; those are your bleaching risks."),
      ("Ramp, don't slam", "Bring sub-canopy intensity up over several days &mdash; to catch early bleaching and because shade-developed leaves must re-acclimate before they can use the light (Section 5)."),
      ("Re-map the air", "Drop a temp/RH sensor into the basal zone, compare to room average, add low fans until the delta closes and you hold the VPD / dew-point buffer at depth."),
      ("Re-check thermal", "Log lights-on temp-rise against your BTU prediction. Confirm cooling and decoupled dehumidification hold through a full lights-off transition."),
      ("Hold flux constant for the first run", "Evaluate grade and uniformity against your geometric change before deciding to add net flux."),
      ("Log per cultivar", "Response is cultivar-dependent &mdash; bleaching threshold, stretch under FR, grade uplift. Dense, tall, unpruned genotypes gain most; some tight cultivars gain little and rot easily."),
    ]),
    callout("tip", "What to watch, in order of how fast it bites",
      p("<strong>Bleaching</strong> (days, near fixtures) &rarr; <strong>basal RH / dew point</strong> (every "
        "lights-off) &rarr; <strong>stretch</strong> (if running FR) &rarr; <strong>grade uniformity</strong> "
        "(at harvest) &rarr; <strong>energy-use efficiency</strong> (per cycle &mdash; the number that justifies "
        "the capex).")),
  ]})

# ---------------------------------------------------------------- 11 economics
SECTIONS.append({"id": "economics", "kicker": "Economics", "title": "The economics, framed honestly",
  "blocks": [
    p("The return on under-canopy lighting is mostly a <strong>grade story</strong>, not a gross-weight story. "
      "The clearest financial mechanism in the research is converting B/C-grade lower bud into A/B-grade "
      "saleable flower, plus reduced variability &mdash; worth more in a price-pressured, quality-led market "
      "than raw biomass."),
    table(["Line", "Direction", "Notes"], [
      ["Bud grade uplift (B/C &rarr; A/B)", "+ revenue", "The primary, best-evidenced return"],
      ["Uniformity / reduced variability", "+ revenue", "Predictable product, fewer culls"],
      ["Yield at equal flux", "~ flat", "Grade up, gross weight not guaranteed"],
      ["Fixture capex + install", "&minus; capital", "IP-rated, DLC for rebate eligibility"],
      ["Added cooling + dehumidification", "&minus; capex/opex", "Sections 8 + 9 &mdash; the hidden line"],
      ["Reduced plant count (for ICL lanes)", "&minus; density", "Fewer plants, better plants"],
      ["Added power draw", "&minus; opex", "Offset partly by energy-use-efficiency gains"],
    ], caption="Cost / benefit ledger. The return is grade and uniformity, with a real climate-accommodation cost."),
    p("The realistic 25&ndash;35% average improvement is achievable" + _c("aroya-undercanopy") + " &mdash; "
      "conditional on cultivar fit, plant-count discipline and the climate accommodations. Model it on "
      "<em>your</em> grade spread and <em>your</em> power and HVAC costs, not a vendor&rsquo;s headline. If most "
      "of your lower canopy is already saleable, the upside is smaller. If you&rsquo;re throwing away larf every "
      "harvest, that larf is the prize."),
  ]})
