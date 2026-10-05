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
    return L.zones("VPD: the correct climate band", 0.2, 1.8,
        [(0.2, 0.4, BLUL, "wet air"), (0.4, 0.8, GL, "clone / vegetative"),
         (0.8, 1.2, GXL, "flowering"), (1.2, 1.4, AMBL, "dry"), (1.4, 1.8, REDL, "stress")],
        unit=" kPa", note="VPD is one value for the temperature and the humidity together. Keep it in the band for the stage.")

def water_activity():
    return L.zones("Water activity (aw): the mold limit", 0.30, 0.90,
        [(0.30, 0.55, GL, "dry / stable"), (0.55, 0.65, GXL, "cure target"),
         (0.65, 0.75, AMBL, "risk"), (0.75, 0.90, REDL, "mold growth")],
        unit="", note="aw is the free water that microbes can use. Cure to approximately 0.55-0.65: stable, good to use, below the mold limit.")

def action_threshold():
    return L.line("Action threshold: apply treatment before the increase",
        [(0, 1), (1, 2), (2, 3), (3, 5), (4, 9), (5, 16)],
        ["day1", "day2", "day3", "day4", "day5", "day6"], ylab="pests for each plant", ymin=0, ymax=18,
        bands=[(0, 5, GL, "monitor"), (5, 18, REDL, "apply treatment")],
        note="Set a number that starts treatment. Below it, monitor. Above it, apply treatment before the curve increases.")

def burping_curve():
    return L.line("Burping decreases jar humidity to the target",
        [(0, 68), (1, 64), (2, 62), (3, 61), (4, 60), (5, 60), (6, 60)],
        ["seal", "d1", "d2", "d3", "d4", "d5", "d6"], ylab="jar RH %", ymin=50, ymax=72,
        bands=[(58, 62, GL, "target 58-62%")],
        note="Open the jars each day at the start of the cure to release moisture. Open them less when the jars hold the target band.")

def ppfd_dli():
    return L.line("The PPFD during the day gives the DLI",
        [(0, 0), (1, 350), (2, 750), (3, 900), (4, 900), (5, 800), (6, 350), (7, 0)],
        ["off", "", "", "middle", "", "", "", "off"], ylab="PPFD umol/m2/s", ymin=0, ymax=1000,
        note="The PPFD multiplied by the hours gives the DLI in mol/m2/day. The DLI is the area below this curve.")

def batch_flow():
    return L.flow("Quality conditions of a batch",
        [("Quarantine", "product made or received"), ("Testing", "in test, no result"),
         ("Released", "satisfactory"), ("Rejected", "unsatisfactory, isolated")],
        note="Do not use a batch before its release. Keep each unsatisfactory batch in quarantine. Record it and do not discard it.")

def scouting_flow():
    return L.flow("The scouting loop",
        [("Walk", "same areas, each day"), ("Find", "pest / symptom"),
         ("Record", "type, area, severity, photo"), ("Treatment", "apply it, then do a check again")],
        note="Find the problem when it is small. The records give a trend that you can use.")

def wc_curve():
    return L.line("Water-content cycle for one day",
        [(0, 68), (1, 62), (2, 58), (3, 57), (4, 64), (5, 72), (6, 75), (7, 73), (8, 70)],
        ["off", "", "P3 min", "on", "P1", "FC", "P2", "", "off"], ylab="water content %", ymin=0, ymax=100,
        bands=[(55, 90, GL, "correct band"), (0, 30, REDL, "too dry")],
        note="Fill to field capacity, hold it, make a controlled dryback, and do it again. The dryback size is the steering control.")


DIAGRAMS = {
    "airflow-design": [
        ("boundary", P.boundary_layer, "The boundary layer is a film of air that does not move on the leaf. Airflow keeps this film thin. Thus water vapor and CO2 can move between the leaf and the air of the room."),
        ("laminar", P.laminar_turbulent, "Smooth (laminar) air moves along the canopy and leaves areas of air that do not move. A small quantity of turbulence mixes the air into the plants."),
        ("transpir", P.transpiration, "VPD causes water vapor to go out of the leaf (transpiration). As a result, water and nutrients move up from the roots."),
        ("exchange", P.air_exchange, "Air exchange replaces all the air in the room. Use the air changes for each hour (ACH) to calculate the size of the system."),
    ],
    "closed-loop": [
        ("setpoint", C.setpoint_band, "Control the value to a target band around a setpoint. Change the control only when the reading is not in the band. Do not change it for each small difference."),
        ("", wc_curve, "The loop reads the water content, the EC and the dryback each day. It uses them as signals and as controls."),
    ],
    "coco-crop-steering": [
        ("field", C.field_capacity, "The water content moves between three points each day: saturation, field capacity and the dryback low."),
        ("dryback", wc_curve, "The cycle of water content each day: fill the substrate, hold the water, let the substrate dry, and do it again."),
        ("", C.ec_concentration, "When the coco dries, the salts stay in the coco. Thus the EC at the roots increases during the day."),
        ("", C.gen_vs_veg, "Use a wetter substrate and small drybacks for vegetative steering. Use a drier substrate and large drybacks for generative steering."),
    ],
    "defoliation-training": [
        ("apical", P.apical_dominance, "Apical dominance: the auxin in the tip prevents growth of the buds below it. Topping removes this signal. Then two colas become the primary tops."),
        ("fim", P.fim_vs_topping, "You cut the shoot at a different position for topping and for FIM. Topping removes the tip fully and gives two tops. FIM removes the tip not fully and gives three to four tops."),
        ("train", P.training_compare, "Each training method changes the shape of the canopy. When the tops are more equal in height, the plants get more light. As a result, the yield is higher."),
        ("defol", P.lollipop_zones, "Lollipopping removes the bottom third of the plant. This part does not make a good yield. Thus light and air go to the buds that make a good yield."),
    ],
    "f2-crop-steering": [
        ("", wc_curve, "The controller operates the P0-P3 cycle of water content each day: increase to field capacity, keep that value, and then make a controlled dryback."),
        ("field", C.field_capacity, "The cycle each day moves between these points: saturation, field capacity and the dryback low."),
        ("generative", C.gen_vs_veg, "Select vegetative or generative steering with two controls: the water content that you keep and the size of the dryback."),
    ],
    "facility-3d": [
        ("", P.floor_plan, "Flow in the facility goes in one direction. Personnel and product go from dirty areas to clean areas. They do not go back."),
    ],
    "flowering-stages": [
        ("flip", C.photoperiod, "The change to 12/12: 12 hours of dark in one period causes flowering and keeps it in progress."),
        ("", P.bud_anatomy, "The parts of a flower: the cola, the calyx, the pistils and the resin trichomes. The trichomes show the ripeness."),
        ("", vpd_zones, "Keep the VPD in the flowering band while the canopy becomes full."),
        ("defol", P.lollipop_zones, "In flowering, lollipopping and defoliation let light and air go into the canopy."),
    ],
    "gmp-hash-lab": [
        ("clean", P.cleanroom_grades, "Each cleanroom grade is in the grade before it. The air is more clean nearer to open product."),
        ("batch", batch_flow, "A batch starts in quarantine. Then the laboratory does a test on the batch. After the test, you release or reject the batch. You make a full record at each step."),
        ("ccp", P.ccp_tree, "The HACCP test to find if a step is a Critical Control Point. You must monitor each Critical Control Point."),
        ("water activity", water_activity, "Water activity gives the limit for safety from microbes. It also gives the limit for a stable product."),
    ],
    "grow-room-systems": [
        ("stomata", C.stomata, "Stomata open to absorb CO2 and to release water vapor. They close to keep water in the plant. The climate controls when they open and close."),
        ("", ppfd_dli, "The light intensity during the day gives the DLI. The DLI is the total quantity of light that the crop receives."),
        ("", vpd_zones, "The temperature and the humidity together give the VPD. The VPD is the one value to control for the climate."),
    ],
    "harvest-dry-trim-cure": [
        ("water activity", water_activity, "Dry and cure the flower to a water activity at which the product is stable and good to use. The water activity must be below the value at which mold growth is possible."),
        ("cure", burping_curve, "Burping removes moisture at the start of the cure. Do this until the humidity in the jars stays at the target value."),
    ],
    "ipm-sop": [
        ("threshold", action_threshold, "An action threshold gives a decision from the scouting. Below the threshold, you monitor. Above the threshold, you apply treatment immediately."),
        ("spray", P.spray_vs_drench, "A foliar spray touches the leaves and is fast. A root drench is systemic and continues for a longer time. The effect is different because the treatment goes to a different area."),
        ("scout", scouting_flow, "The scouting loop each day: walk, find the problem, make a record, and do the treatment."),
    ],
    "irrigation-manual": [
        ("", wc_curve, "The system gives this cycle of water content each day: fill the substrate, hold the water, and make a controlled dryback."),
        ("field", C.field_capacity, "Saturation, field capacity and the dryback low."),
        ("", C.ec_concentration, "The EC increases during the day when the substrate dries. Runoff decreases the EC to its first value."),
    ],
    "light-acclimation": [
        ("", ppfd_dli, "Increase the PPFD (and thus the DLI) in small steps. Thus the plant has time to adapt, and bleaching does not occur."),
        ("photoperiod", C.photoperiod, "The light cycle for each stage."),
    ],
    "lighting-fundamentals": [
        ("ppfd", ppfd_dli, "The DLI is the area below the curve of the PPFD for one day."),
        ("photoperiod", C.photoperiod, "Photoperiod for each stage: 18/6 in vegetative growth, 12/12 for flowering."),
    ],
    "mould-risk": [
        ("water activity", water_activity, "In storage, keep the water activity below the value at which mold growth is possible."),
    ],
    "nutrient-deficiencies": [
        ("mobile", C.nutrient_mobility, "Mobile nutrients show a deficiency first on the leaves at the bottom of the plant. Immobile nutrients show a deficiency on the new growth at the top."),
        ("ph", C.ph_availability, "pH lockout causes most deficiencies. The nutrient is in the root zone, but the plant cannot absorb it when the pH is not in the band."),
        ("", C.ec_concentration, "An EC that is too high increases the concentration of salts. This stress on the uptake can cause a deficiency, or the same symptoms as a deficiency."),
    ],
    "ph-management": [
        ("", C.ph_availability, "The pH controls which nutrients the plant can absorb. If the pH is not in the band, lockout occurs."),
        ("", C.ec_concentration, "The EC and the pH change together when the root zone dries. Read the two values."),
    ],
    "plant-state-dashboard": [
        ("setpoint", C.setpoint_band, "Compare telemetry with a target band, not with one value. The dashboard shows a warning only for a deviation that is not noise."),
        ("", wc_curve, "The water content and the dryback show the condition of the plant during the day."),
        ("vpd", vpd_zones, "VPD is a climate signal that you can control."),
        ("", ppfd_dli, "PPFD and DLI are the light signal."),
    ],
    "root-zone-teros12": [
        ("", C.field_capacity, "The sensor reads these values: saturation, field capacity (container capacity / DUL) and the dryback low."),
        ("", wc_curve, "One day of water content, as the probe measures it."),
    ],
    "seeds-germination": [
        ("", P.germination, "The sequence of germination: a viable seed absorbs water. The radicle comes out of the seed and becomes the taproot. The cotyledons move up. Then the true leaves start."),
        ("", P.seed_anatomy, "The parts of the seed: the seed coat gives protection, the endosperm gives nutrients, and the embryo (the radicle and the cotyledons) becomes the plant."),
    ],
    "signal-and-noise": [
        ("", C.setpoint_band, "A signal is a reading that is not in the band. Noise is a small change in the band. Change the control for a signal. Do not change it for noise."),
    ],
    "smart-watering-vrwe": [
        ("", wc_curve, "The controller keeps the water-content curve for each day at the setpoints. It does not use a timer."),
        ("", C.field_capacity, "A full pot (the maximum after drainage) and the dryback low give the band that the controller controls."),
        ("channel", R.fig_rewet, "Channeling: when a pot is too dry, the water flows in the same areas each time. The remaining substrate stays dry."),
    ],
    "substrates-overview": [
        ("porosity", C.porosity, "A substrate contains solids, water and air. The ratio of the porosity that holds water to the porosity that holds air shows if the substrate is wet or has more air."),
        ("", wc_curve, "Each medium has a cycle from wet to dry each day. The shape of the cycle changes with the quantity of water that the medium holds."),
        ("", C.ph_availability, "The pH is different in each medium, and the buffer is different. These control the availability of nutrients."),
    ],
    "tissue-culture": [
        ("test", P.qpcr_vs_lamp, "Two test methods for hop latent viroid: RT-qPCR in a laboratory (the most sensitive) and RT-LAMP in the room (fast, and low cost)."),
    ],
    "water-quality": [
        ("reverse", P.ro_membrane, "Reverse osmosis uses pressure to move water through a membrane. The salts stay behind and flow away with the waste water."),
        ("alkalin", P.alkalinity_buffer, "Alkalinity is the buffer of the pH. Water with high alkalinity prevents a correction of the pH. Then the pH can go too far in the other direction."),
        ("ph", C.ph_availability, "The pH and the alkalinity of the source water change where your feed is on the availability curve."),
    ],
}
