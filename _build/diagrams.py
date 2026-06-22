# -*- coding: utf-8 -*-
"""Registry: which bespoke SVG diagrams get injected into which paper.
Each entry: (section_hint, callable -> svg_html, caption).
section_hint is matched against section id/title (substring); empty = the key-terms section.
"""
import figs_concepts as C
import figs_papers as P
import figs_rockwool as R
import figs_lib as L
from figs import GL, GXL, AMBL, REDL, BLUL, PURL


# ---- chart-type reusables built from figs_lib (cheap, data-driven) ----
def vpd_zones():
    return L.zones("VPD: the climate sweet spot", 0.2, 1.8,
        [(0.2, 0.4, BLUL, "too humid"), (0.4, 0.8, GL, "clones / veg"),
         (0.8, 1.2, GXL, "flower"), (1.2, 1.4, AMBL, "dry"), (1.4, 1.8, REDL, "stress")],
        unit=" kPa", note="Vapour pressure deficit blends temp and humidity into one number; steer to the band for the stage.")

def water_activity():
    return L.zones("Water activity (aw): the mould line", 0.30, 0.90,
        [(0.30, 0.55, GL, "dry / stable"), (0.55, 0.65, GXL, "cured target"),
         (0.65, 0.75, AMBL, "risky"), (0.75, 0.90, REDL, "mould grows")],
        unit="", note="aw is the free water microbes can use. Cure to ~0.55-0.65: stable and smokeable, below the mould line.")

def action_threshold():
    return L.line("Action threshold: act before the spike",
        [(0, 1), (1, 2), (2, 3), (3, 5), (4, 9), (5, 16)],
        ["day1", "day2", "day3", "day4", "day5", "day6"], ylab="pests per plant", ymin=0, ymax=18,
        bands=[(0, 5, GL, "monitor"), (5, 18, REDL, "act now")],
        note="Set a number that triggers action. Below it you watch; the moment you cross it you treat, before the curve runs away.")

def burping_curve():
    return L.line("Burping walks jar humidity down to target",
        [(0, 68), (1, 64), (2, 62), (3, 61), (4, 60), (5, 60), (6, 60)],
        ["seal", "d1", "d2", "d3", "d4", "d5", "d6"], ylab="jar RH %", ymin=50, ymax=72,
        bands=[(58, 62, GL, "target 58-62%")],
        note="Open the jars daily early in the cure to release moisture; ease off once they hold the target band on their own.")

def ppfd_dli():
    return L.line("PPFD through the day adds up to DLI",
        [(0, 0), (1, 350), (2, 750), (3, 900), (4, 900), (5, 800), (6, 350), (7, 0)],
        ["off", "", "", "midday", "", "", "", "off"], ylab="PPFD umol/m2/s", ymin=0, ymax=1000,
        note="Intensity (PPFD) times hours is the day's total light: DLI in mol/m2/day. The area under this curve is what the plant actually gets.")

def batch_flow():
    return L.flow("A batch moves through quality states",
        [("Quarantine", "just made / received"), ("Testing", "sampled, awaiting result"),
         ("Released", "passed, usable"), ("Rejected", "failed, segregated")],
        note="Nothing is used until it is Released. Failures are quarantined and tracked, never quietly binned.")

def scouting_flow():
    return L.flow("The scouting loop",
        [("Walk", "fixed route, daily"), ("Spot", "pest / symptom"),
         ("Log", "type, place, severity, photo"), ("Act", "treat, then re-check")],
        note="Catch it while it is small. The log turns a daily glance into a trend you can act on.")

def wc_curve():
    return L.line("A daily water-content cycle",
        [(0, 68), (1, 62), (2, 58), (3, 57), (4, 64), (5, 72), (6, 75), (7, 73), (8, 70)],
        ["off", "", "P3 min", "on", "P1", "FC", "P2", "", "off"], ylab="water content %", ymin=0, ymax=100,
        bands=[(55, 90, GL, "working band"), (0, 30, REDL, "too dry")],
        note="Saturate to field capacity, hold it, allow a controlled dryback, repeat. The size of the dryback is the steering lever.")


DIAGRAMS = {
    "airflow-design": [
        ("boundary", P.boundary_layer, "The boundary layer is the still-air film on the leaf; airflow's job is to keep it thin so the leaf can breathe and transpire."),
        ("laminar", P.laminar_turbulent, "Smooth (laminar) air slides over the canopy and leaves dead pockets; gentle turbulence mixes air into the plants."),
        ("transpir", P.transpiration, "The transpiration stream: VPD pulls water vapour out of the leaf, which draws water and nutrients up from the roots."),
        ("exchange", P.air_exchange, "Air exchange replaces the whole room's air; air changes per hour (ACH) is how you size it."),
    ],
    "closed-loop": [
        ("setpoint", C.setpoint_band, "You steer to a target band around a setpoint, and act only when the reading leaves the band, not on every wiggle."),
        ("", wc_curve, "Water content, EC and dryback are the levers and signals the loop reads and acts on each day."),
    ],
    "coco-crop-steering": [
        ("field", C.field_capacity, "Saturation, field capacity and the dryback low: the three points your daily water-content curve moves between."),
        ("dryback", wc_curve, "The daily water-content cycle: saturate, hold, dry back, repeat."),
        ("", C.ec_concentration, "As coco dries, the salts stay behind, so the EC the roots feel climbs through the day."),
        ("", C.gen_vs_veg, "Wetter with small drybacks steers vegetative; drier with big drybacks steers generative."),
    ],
    "defoliation-training": [
        ("apical", P.apical_dominance, "Apical dominance: the tip's auxin suppresses the buds below it; topping cuts the signal and two colas take over."),
        ("fim", P.fim_vs_topping, "Topping vs FIM is all in the cut line: a clean cut gives two tops, a high partial pinch gives three to four."),
        ("train", P.training_compare, "Each training method shapes the canopy: more even tops means more light captured and more yield."),
        ("defol", P.lollipop_zones, "Lollipopping strips the unproductive lower third so light and air reach the buds that pay."),
    ],
    "f2-crop-steering": [
        ("", wc_curve, "The daily P0-P3 water-content cycle the controller runs: ramp to field capacity, maintain, controlled dryback."),
        ("field", C.field_capacity, "Saturation, field capacity and dryback low, the points the daily cycle moves between."),
        ("generative", C.gen_vs_veg, "Steer vegetative or generative by where you hold the water and how big a dryback you allow."),
    ],
    "facility-3d": [
        ("", P.floor_plan, "A one-way facility flow: people and product move dirty-to-clean and never double back."),
    ],
    "flowering-stages": [
        ("flip", C.photoperiod, "The flip to 12/12: twelve hours of unbroken dark triggers and holds flowering."),
        ("", P.bud_anatomy, "The parts of a flower: cola, calyx, pistils and the resin trichomes that signal ripeness."),
        ("", vpd_zones, "Hold VPD in the flowering band as the canopy fills in."),
        ("defol", P.lollipop_zones, "Lollipopping and defoliation in flower open the canopy to light and air."),
    ],
    "gmp-hash-lab": [
        ("clean", P.cleanroom_grades, "Cleanroom grades nest cleaner air the closer you get to open product."),
        ("batch", batch_flow, "A batch is quarantined, tested, then released or rejected, with a full record at each step."),
        ("ccp", P.ccp_tree, "The HACCP test for whether a step is a Critical Control Point you must monitor."),
        ("water activity", water_activity, "Water activity is the cold line for microbial safety and stability."),
    ],
    "grow-room-systems": [
        ("stomata", C.stomata, "Stomata open to take in CO2 and transpire, and close to conserve water; climate decides which."),
        ("", ppfd_dli, "Light intensity over the day is what sets DLI, the total light the crop receives."),
        ("", vpd_zones, "Temperature and humidity combine into VPD, the single climate number to steer."),
    ],
    "harvest-dry-trim-cure": [
        ("water activity", water_activity, "Dry and cure to a water activity that is stable and smokeable but below where mould can grow."),
        ("cure", burping_curve, "Burping releases moisture early in the cure until the jars hold the target humidity on their own."),
    ],
    "ipm-sop": [
        ("threshold", action_threshold, "An action threshold turns scouting into a decision: below the line you monitor, above it you treat immediately."),
        ("spray", P.spray_vs_drench, "Foliar spray is contact and fast; a root drench is systemic and lasts, where it lands decides what it does."),
        ("scout", scouting_flow, "The daily scouting loop: walk, spot, log, act."),
    ],
    "irrigation-manual": [
        ("", wc_curve, "The daily water-content cycle the system delivers: saturate, hold, controlled dryback."),
        ("field", C.field_capacity, "Saturation, field capacity and dryback low."),
        ("", C.ec_concentration, "Why EC climbs through the day as the substrate dries, and why runoff resets it."),
    ],
    "light-acclimation": [
        ("", ppfd_dli, "Ramp PPFD (and so DLI) up gradually so the plant acclimates instead of bleaching."),
        ("photoperiod", C.photoperiod, "The light schedule by stage."),
    ],
    "lighting-fundamentals": [
        ("ppfd", ppfd_dli, "Intensity over time is DLI: the area under the daily PPFD curve."),
        ("photoperiod", C.photoperiod, "Photoperiod by stage: 18/6 in veg, 12/12 to flower."),
    ],
    "mould-risk": [
        ("water activity", water_activity, "In storage, keep water activity below the line where mould can grow."),
    ],
    "nutrient-deficiencies": [
        ("mobile", C.nutrient_mobility, "Mobile nutrients show deficiency on old lower leaves first; immobile ones on new upper growth."),
        ("ph", C.ph_availability, "Most deficiencies are really pH lockout: the nutrient is present but unavailable outside the band."),
        ("", C.ec_concentration, "Too-high EC concentrates salts and can mimic or trigger deficiency by stressing uptake."),
    ],
    "ph-management": [
        ("", C.ph_availability, "pH sets which nutrients the plant can actually take up; drift out of the band and you get lockout."),
        ("", C.ec_concentration, "EC and pH move together as the root zone dries; read both."),
    ],
    "plant-state-dashboard": [
        ("setpoint", C.setpoint_band, "Telemetry is judged against a target band, not a single number; the dashboard flags only real departures."),
        ("", wc_curve, "Water content and dryback, read as plant state over the day."),
        ("vpd", vpd_zones, "VPD as a steerable climate signal."),
        ("", ppfd_dli, "PPFD and DLI as the light signal."),
    ],
    "root-zone-teros12": [
        ("", C.field_capacity, "What the sensor reads: saturation, field capacity (container capacity / DUL) and the dryback low."),
        ("", wc_curve, "A day of water content as the probe sees it."),
    ],
    "seeds-germination": [
        ("", P.germination, "Germination in order: a viable seed imbibes water, the radicle emerges as the taproot, the cotyledons rise, then true leaves form."),
        ("", P.seed_anatomy, "Inside the seed: the coat protects, the endosperm feeds, and the embryo (radicle plus cotyledons) becomes the plant."),
    ],
    "signal-and-noise": [
        ("", C.setpoint_band, "Real signal is the reading leaving the band; noise is the wiggle inside it. Act on signal, ignore noise."),
    ],
    "smart-watering-vrwe": [
        ("", wc_curve, "The watering brain holds the daily water-content curve to setpoints instead of a fixed clock."),
        ("", C.field_capacity, "Full pot (drained upper limit) and the dryback low define the band it steers."),
        ("channel", R.fig_rewet, "Channeling: once a pot is too dry, water runs down preferential paths and the core stays dry."),
    ],
    "substrates-overview": [
        ("porosity", C.porosity, "A substrate is solids, water and air; the ratio of water-holding to air-filled porosity is what makes it wet or airy."),
        ("", wc_curve, "Every medium runs a daily wet-to-dry cycle; the shape differs by how much water it holds."),
        ("", C.ph_availability, "pH behaviour and buffering differ by medium and set nutrient availability."),
    ],
    "tissue-culture": [
        ("test", P.qpcr_vs_lamp, "Two ways to test for hop latent viroid: lab RT-qPCR (most sensitive) and in-room RT-LAMP (fast and cheap)."),
    ],
    "water-quality": [
        ("reverse", P.ro_membrane, "Reverse osmosis pushes water through a membrane under pressure, leaving the salts behind to flush away."),
        ("alkalin", P.alkalinity_buffer, "Alkalinity is pH's hidden buffer: high-alkalinity water resists correction, then over-swings."),
        ("ph", C.ph_availability, "Source-water pH and alkalinity set where your feed lands on the availability curve."),
    ],
    "wso-quality-manual": [
        ("qa", P.qa_vs_qc, "QA builds quality into the process; QC checks it in the product. You need both."),
        ("", P.doc_hierarchy, "The document pyramid: policy at the top, the records that prove it at the base."),
    ],
}
