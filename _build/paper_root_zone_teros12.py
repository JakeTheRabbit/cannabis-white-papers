# -*- coding: utf-8 -*-
"""Paper: root-zone state estimation with the TEROS-12 sensor (beginner-first research)."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        stagecard, grid, card, chip, kv, steps)
import figs_lib as L

SLUG = "root-zone-teros12"
TITLE = "TEROS-12 measurements and how to control irrigation with them"
EYEBROW = "Precision · Root zone"
SUB = ("A TEROS-12 probe in your substrate gives three numbers: the quantity of water in the "
       "substrate, the salt concentration of the water, and the temperature. This guide gives "
       "information about each number. It shows that you must change the raw reading before it is "
       "the correct value. It also shows how to use the reading to make irrigation decisions that "
       "you can be sure of for a crop.")
META = [("gauge", "Precision"), ("image", "12 diagrams"),
        ("quote", "8 sources"), ("clock", "~18 min to read")]
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
    lead("A TEROS-12 is a small probe that you push into substrate: coco, rockwool or soil. It "
         "sends three numbers through one digital wire: the quantity of water in the substrate, the "
         "salt concentration of that water, and the temperature. This guide starts from zero. It "
         "gives information about each number and about how the probe gets the number. It also "
         "gives the cause of an important instruction: do not use only the raw reading to open a "
         "valve."),
    p("The probe measures a volume of approximately 1010 mL (34.2 fl oz) of substrate around its "
      "prongs. It does not measure all the root zone." + _c("meter-teros12-manual") +
      " The next sections show how to change that one local reading, which can have an error, into "
      "a number for irrigation control."),
    ul(["The TEROS-12 gives <strong>volumetric water content (VWC)</strong>, <strong>bulk "
        "electrical conductivity (EC)</strong> and <strong>substrate temperature</strong> through "
        "the digital protocol SDI-12.",
        "The volume of influence of the probe is only approximately 1010 mL (34.2 fl oz) of "
        "substrate around the prongs. This volume is one local position. It is not the average of a "
        "tray or a zone.",
        "This guide changes that local reading, which has noise, into a good estimate of the "
        "quantity of water. The guide always gives the uncertainty of the estimate.",
        "It is not necessary to know about soil sensors before you read this guide. Each term has a definition where it first occurs."]),
    figure(grid([
        card("The probe", "Three steel prongs make a high-frequency electric field and measure the effect of the field on the substrate.", "equipment"),
        card("Volume of influence", "The probe measures only approximately 1010 mL (34.2 fl oz) of substrate around the prongs.", "approximately 1010 mL"),
        card("Other parts of the pot", "The probe cannot measure the substrate that is not in that volume.", "not measured"),
      ], cols=3), 1,
      "The probe measures a small volume of substrate around the prongs, in the shape of an ellipsoid. It does not measure all the root zone." + _c("meter-teros12-manual")),
    callout("note", "Persons for this guide",
      p("This guide is for a person who puts a moisture probe in a pot. The person wants to control "
        "irrigation with the probe and to include the uncertainty. Use this guide with the <a "
        "href='smart-watering-vrwe.html'>guide to smart irrigation (VWC/EC)</a> and the <a "
        "href='coco-crop-steering.html'>paper on crop steering in coco</a>.")),
  ]})

SECTIONS.append({"id": "key-terms", "kicker": "Terms", "title": "Definitions",
  "blocks": [
    p("Six terms are necessary for all the information in this guide. Each term has an easy "
      "definition here. After this section, the guide uses each term with the same definition. The "
      "terms occur again in the next sections."),
    defterm("Volumetric water content (VWC)", "The pot is a container with a volume that does not "
            "change. Some of the volume is solid substrate, some is air in the gaps, and some is "
            "liquid water. VWC is the fraction of the total volume that is liquid water. Its unit "
            "is cubic meters of water for each cubic meter of substrate (m&sup3;/m&sup3;). Thus a "
            "VWC of 0.34 shows that 34% of the total volume of the pot is liquid water. VWC is the "
            "primary number that you use to control irrigation."),
    defterm("Permittivity (dielectric constant)", "An electric field has an effect on water that is "
            "approximately twenty times stronger than the effect on dry substrate. Permittivity is "
            "the property that shows this effect. The permittivity of water is approximately 80, of "
            "dry substrate approximately 3&ndash;5, and of air approximately 1. The probe uses this "
            "large difference to find water." + _c("topp-1980-dielectric-vwc")),
    defterm("Capacitance sensor", "A sensor that measures permittivity. It applies a high-frequency "
            "electric field and measures how strongly the material around the sensor holds the "
            "field. The TEROS-12 is a capacitance sensor. It calculates VWC from the permittivity "
            "reading. It does not touch the water directly."),
    defterm("Bulk EC and pore-water EC", "The probe measures the conductivity of all the wet "
            "substrate together: solids, water and air. This value is bulk EC (0&ndash;20000 "
            "&micro;S/cm on this probe). The roots touch the water in the gaps between the "
            "particles of the substrate. The salt concentration of this water is the pore-water EC. "
            "The probe cannot measure pore-water EC directly. You calculate an estimate of it from "
            "bulk EC with the Hilhorst (2000) model."),
    defterm("DUL / container capacity", "Drained upper limit: the quantity of water that <em>this "
            "pot</em> holds after gravity removes all the water that it can. It is the maximum "
            "value for your steering. It is a property of your pot and substrate, not a general "
            "constant. Thus you measure it from the runoff of your pot."),
    defterm("Resolution and accuracy", "Resolution is the smallest change that the probe can show: "
            "0.001 m&sup3;/m&sup3; VWC. Accuracy shows how near the number is to the correct value: "
            "only &plusmn;0.03 m&sup3;/m&sup3; with the generic calibration. The probe gives a "
            "number with high precision, but precision is not the same as accuracy. A number with "
            "high precision can be incorrect each time." + _c("meter-teros12-manual")),
    figure(L.bars("Relative permittivity: water controls the reading",
            [("Air", 1), ("Dry substrate", 4), ("Water", 80)], unit="",
            note="The permittivity of water is much larger than the other values. Thus water controls the reading.",
            maxv=90), 2,
      "The permittivity of liquid water (approximately 80) is approximately twenty times the "
      "permittivity of dry substrate (approximately 3&ndash;5) and approximately eighty times the "
      "permittivity of air (approximately 1). A small quantity of water causes a large change in "
      "the reading of the probe." + _c("topp-1980-dielectric-vwc")),
    figure(grid([
        card("Solids", "The coir, the rockwool fiber or the particles of soil.", "fraction"),
        card("Air", "Pore space with air between the solids.", "fraction"),
        card("Water", "Liquid in the pores. VWC = this volume / total volume.", "VWC"),
      ], cols=3), 3,
      "One unit of volume of substrate has three parts: solids, air and water. VWC is the fraction of the volume that is water."),
  ]})

SECTIONS.append({"id": "how-it-measures", "kicker": "Primary content", "title": "How the probe measures water and does not touch it",
  "blocks": [
    p("The TEROS-12 is a <strong>capacitance probe</strong>. Its prongs send a high-frequency "
      "electric field into the substrate around them. The probe measures how strongly the substrate "
      "holds the field. This property is <strong>permittivity</strong>.</p><p>The permittivity of "
      "water (approximately 80) is approximately twenty times the permittivity of dry substrate "
      "(approximately 3&ndash;5) and approximately eighty times the permittivity of air "
      "(approximately 1). Thus a change in water content causes a large change in the bulk "
      "permittivity of the substrate. You can calculate the size of this change. As a result, you "
      "can use permittivity to find VWC." + _c("topp-1980-dielectric-vwc")),
    p("Then the probe uses a <strong>calibration equation</strong> to change the measured "
      "permittivity to a VWC number. The equation in the probe is a generic curve for mineral soil. "
      "The probe gives the VWC number with a resolution of 0.001 m&sup3;/m&sup3;. There is a "
      "problem from the start: the equation is different for different substrates, and the generic "
      "curve has an accuracy of only &plusmn;0.03 m&sup3;/m&sup3;." + _c("meter-teros12-manual")),
    ul(["Permittivity is the <em>physical</em> quantity that the probe measures. VWC is a "
        "<em>calculated and calibrated</em> estimate. It is one more step after the measurement.",
        "The curve from permittivity to VWC is not a straight line. It is most different from a "
        "straight line near saturation. There the curve becomes flat. A substrate that is almost "
        "full can give a &lsquo;full&rsquo; reading when it is not full.",
        "The temperature of the substrate changes the dielectric response. The change is a known "
        "physical effect. It can cause a change in the reading that is the same as a change in "
        "water content. Correct the reading for this effect." + _c("nasta-2024-teros12-temp-correction"),
        "The probe sends data through SDI-12. Three values show a fault in the equipment or the "
        "cable. The first is a constant value at 0 or at full scale. The second is a "
        "&lsquo;NaN&rsquo; value (not a number). The third is an expired value (the probe sends the "
        "last value again). These values are not readings of data."]),
    figure(L.line("Permittivity to VWC: a curve that is not straight",
            [(0, 0.02), (1, 0.10), (2, 0.20), (3, 0.30), (4, 0.40), (5, 0.46), (6, 0.49)],
            ["3", "8", "15", "24", "35", "48", "62"],
            ylab="VWC (m³/m³)", ymin=0, ymax=0.55,
            note="The bottom axis is permittivity. The curve becomes flat at the top. Thus a reading near saturation can show 'full'."), 4,
      "VWC increases when the permittivity increases, but the curve bends and becomes flat near "
      "saturation. The same step of VWC is a different step of permittivity in different parts of "
      "the curve." + _c("topp-1980-dielectric-vwc")),
    figure(L.flow("The measurement chain",
            [("Electric field", "prongs send the field"),
             ("Permittivity", "substrate holds the field"),
             ("Calibration", "curve gives the VWC"),
             ("VWC + EC + °C", "sent through SDI-12")],
            note="Bulk EC and temperature come from the same measurement. All three numbers go through the SDI-12 wire."), 5,
      "From electric field to a number: each output comes from the same measurement. The error for "
      "each substrate occurs in the calibration."),
  ]})

SECTIONS.append({"id": "calibration", "kicker": "Primary content", "title": "Calibrate the probe to the substrate that you use",
  "blocks": [
    p("When you receive the TEROS-12, it has a generic calibration for mineral soil. This "
      "calibration has an accuracy of only &plusmn;0.03 m&sup3;/m&sup3;. A "
      "<strong>substrate-specific</strong> calibration for your coco or rockwool decreases the "
      "error to &plusmn;0.01&ndash;0.02 m&sup3;/m&sup3;." + _c("fragkos-2024-teros12-soils-ec") +
      " This difference is important when you use the probe. Frequently, the dryback windows in "
      "crop steering are <em>smaller</em> than the error band of the generic calibration "
      "(&plusmn;0.03). If you use a VWC without calibration for steering, the changes that you want "
      "are in the noise."),
    p("An example of safe headroom shows the result of this difference. An estimate that ignores "
      "the error gives 256 mL (8.7 fl oz) of &lsquo;room to apply water&rsquo;. When you include an "
      "accuracy of &plusmn;0.02, the safe quantity is approximately 109 mL (3.7 fl oz). With the "
      "generic calibration (accuracy &plusmn;0.03), the safe quantity is only approximately 54 mL "
      "(1.8 fl oz). The pot and the probe are the same. The only difference is how you include the "
      "error band when you calculate." + _c("nemali-2006-set-point-irrigation")),
    figure(L.bars("How accuracy decreases safe headroom (same pot)",
            [("Raw estimate", 256), ("Calibrated ±0.02", 109), ("Generic ±0.03", 54)],
            unit=" mL",
            note="A wider error band gives less water that you can add with no risk of overshoot.",
            maxv=300), 6,
      "The safe headroom decreases by a large quantity when the calibration error increases. It "
      "decreases from 256 mL (8.7 fl oz) in the raw estimate to approximately 54 mL (1.8 fl oz) "
      "with the generic curve." + _c("nemali-2006-set-point-irrigation")),
    table(["Calibration type", "VWC accuracy", "Resolution", "Accurate steering?"], [
      ["Generic calibration for mineral soil (in the probe)", "&plusmn;0.03 m&sup3;/m&sup3;", "0.001 m&sup3;/m&sup3;", "No. The error band is wider than a usual dryback window."],
      ["Substrate-specific calibration", "&plusmn;0.01&ndash;0.02 m&sup3;/m&sup3;", "0.001 m&sup3;/m&sup3;", "Yes. It is necessary for accurate steering."],
    ], cls="compact", caption="The resolution is the same for the two types. The accuracy is different. Calibrate the probe to your substrate before you use it for steering."),
    callout("warn", "Calibration does not correct all errors",
      p("Make sure that you use a substrate-specific calibration: it is <strong>necessary</strong> "
        "for accurate steering. Calibration corrects only an additive <em>offset</em> in the "
        "reading. The gain error and the nonlinearity near saturation stay, and they do not cancel "
        "when you calculate with the reading. Include the residual error that stays after the "
        "calibration.")),
  ]})

SECTIONS.append({"id": "ec-and-limits", "kicker": "Primary content", "title": "The EC reading and its limits",
  "blocks": [
    p("The probe measures <strong>bulk EC</strong>, the conductivity of all the wet substrate "
      "(0&ndash;20000 &micro;S/cm). Growers must know <strong>pore-water EC</strong>: the salt "
      "concentration of the solution that touches the roots. To calculate pore-water EC, use the "
      "Hilhorst (2000) model with bulk EC, VWC and temperature." + _c("hilhorst-2000-pore-water-ec") +
      " The bulk EC is the conductivity of the water and the substrate together. The Hilhorst model "
      "then gives an estimate of the conductivity of the water only."),
    p("The model gives a good estimate, but its sensitivity to its parameters is approximately "
      "&plusmn;20%. It does not give correct results when the VWC is less than 0.10 "
      "m&sup3;/m&sup3;. Do not use it in this condition.</p><p>A more important limit is "
      "<strong>representativeness</strong>: the probe measures one position of approximately 1010 "
      "mL (34.2 fl oz). Channeling, dry areas or bad contact between the probe and the substrate "
      "can cause a number that is different from the value of the zone. The probe operates "
      "correctly at this time." + _c("fragkos-2024-teros12-soils-ec")),
    ul(["The probe measures bulk EC (0&ndash;20000 &micro;S/cm) directly. You calculate an estimate "
        "of pore-water EC from bulk EC. The two values are not the same.",
        "The conversion of Hilhorst (2000) has a sensitivity of approximately &plusmn;20%. It does not give correct results when the VWC is less than 0.10 m&sup3;/m&sup3;." + _c("hilhorst-2000-pore-water-ec"),
        "A representativeness fault: the 1010 mL (34.2 fl oz) of substrate that the probe measures "
        "can have a value that is different from the value of the zone. Channeling, an air gap or a "
        "probe that is not fully in the substrate can cause the difference. The probe operates "
        "correctly at the same time.",
        "The sensor cannot measure the volume of runoff from each pot. It cannot measure the "
        "effective substrate volume. This volume decreases when the roots fill the pot. It cannot "
        "find if the system supplied an irrigation shot that the controller started."]),
    figure(grid([
        card("Bulk EC", "The conductivity of solids, water and air together. The probe measures this directly.", "measured"),
        card("Hilhorst model", "The model uses bulk EC, VWC and temperature. The sensitivity is approximately &plusmn;20%. It is not correct when the VWC is less than 0.10.", "approximately &plusmn;20%"),
        card("Pore-water EC", "The salt in the liquid that touches the roots. You must find this value.", "calculated"),
      ], cols=3), 7,
      "The probe measures bulk EC directly. You calculate pore-water EC with the model of Hilhorst "
      "(2000). This estimate becomes less accurate quickly when the substrate becomes dry." +
      _c("hilhorst-2000-pore-water-ec")),
    table(["The probe CAN measure", "The probe CANNOT measure", "Other method"], [
      ["VWC (local position)", "The correct average of the zone for all the pots", "Many probes, a cohort model"],
      ["Bulk EC", "Runoff volume for each pot", "Runoff trays / drain sensors"],
      ["Substrate temperature", "Effective substrate volume (decreases when the roots fill the pot)", "Measure DUL again at intervals"],
      ["Calculated pore-water EC", "If an emitter operated", "Flow meter, or a sudden change of the weight from a load cell"],
    ], cls="compact", caption="The information that one TEROS-12 can and cannot give, and the second witness (a second measurement with a different method) that fills each gap."),
  ]})

SECTIONS.append({"id": "steering", "kicker": "How-to", "title": "Steering of irrigation with TEROS-12 readings",
  "blocks": [
    p("The method has two parts. <strong>Make the raw VWC reading less important.</strong> Do not "
      "use it as a correct value. Use it as one witness that has noise, with a confidence score (a "
      "number that shows how accurate the reading is).</p><p><strong>Make a small water-balance "
      "model more important.</strong> The model holds the best estimate of the water in the "
      "substrate. A reading with a high confidence score can change the estimate only by a "
      "<em>small</em> quantity."),
    p("Monitor <strong>dryback</strong> (the quantity by which the VWC decreases between shots) and "
      "<strong>specific yield</strong> (the quantity by which the VWC increases for each mL "
      "supplied). Specific yield shows when the pot comes near to its capacity. Set the capacity "
      "anchor (the DUL value that the system uses) from the DUL that you measured, and not from a "
      "number without a measurement. Control irrigation with <em>trends</em> (the shape and the "
      "slope of the dryback) more than with the absolute value, because an additive calibration "
      "offset does not change trends." + _c("tavan-2021-sensor-irrigation-soilless") +
      " Do not use only a trend. Always use a second witness, for example the time of runoff or the "
      "weight of the pot."),
    steps([
      ("Calibrate to your substrate first", "A substrate-specific calibration is the first "
       "necessary step. If you do not have it, your steering is in the error band. You cannot be "
       "sure that the reading is sufficiently accurate."),
      ("Make sure that the probe contact and position are correct", "Put the probe tightly in the substrate, in a "
       "representative position that does not change. A loose probe or an air gap gives the reading "
       "of the substrate around it. It does not give the reading of your root zone."),
      ("Measure the DUL of this pot from irrigation events with a second witness", "Set the capacity anchor from approximately "
       "five irrigation events with runoff or weight data. Do not use only one irrigation event. "
       "Give the capacity anchor as a volume of water, and not as a raw VWC number."),
      ("Steering with the slope of the dryback, with a limit from the safe headroom", "Use the slope of the dryback and "
       "the specific yield. Use a limit from a headroom estimate that includes the calibration "
       "error, and not from the raw estimate."),
      ("Use a second witness before you apply water", "A second witness (the start of runoff "
       "or the mass from a load cell) must give the same result before a signal goes to a valve. "
       "The probe reading must not operate a valve if there is no second witness."),
    ]),
    figure(L.line("A day of dryback: shots, drying and the DUL limit",
            [(0, 0.30), (1, 0.44), (2, 0.40), (3, 0.36), (4, 0.45), (5, 0.41), (6, 0.31)],
            ["P0 end", "shot", "+2h", "+4h", "shot", "+2h", "day end"],
            ylab="VWC (m³/m³)", ymin=0.25, ymax=0.5,
            note="A sharp increase is a shot. The decrease between shots is the dryback. The top is the DUL that you measured."), 8,
      "Irrigation shots increase the VWC to the DUL. The steering signal is the slope of the VWC "
      "when it decreases between shots, and not the absolute value at one time."),
    figure(L.flow("The steering loop: the reading is not the only signal for the valve",
            [("Probe reading", "raw VWC / EC / °C"),
             ("Confidence score", "how accurate it is"),
             ("Water model", "water-balance estimate"),
             ("Second witness", "runoff or weight agrees")],
            note="A valve operates only if the confidence score is high AND a second witness agrees."), 9,
      "Each reading has three steps before the system can apply water: a confidence score, a "
      "water-balance model and a check by a second witness." +
      _c("tavan-2021-sensor-irrigation-soilless")),
  ]})

SECTIONS.append({"id": "troubleshooting", "kicker": "When a problem occurs", "title": "Find the cause of a bad reading before you think that the sensor is defective",
  "blocks": [
    p("Most problems with the TEROS-12 do not occur because the sensor is defective. The problem is "
      "that a person <em>thinks</em> that the reading is correct when it is not. First, find the "
      "difference between two conditions. An <strong>incorrect reading</strong> is a "
      "representativeness fault. The probe operates correctly, but the 1010 mL (34.2 fl oz) that it "
      "measures has a different value from the zone. With an incorrect reading, decrease your "
      "confidence in the absolute VWC number.</p><p>A <strong>constant, NaN or expired "
      "value</strong> is a fault in the equipment or the cable. With this value, stop all automatic "
      "operation."),
    p("Monitor for a VWC that changes with the temperature cycle of the substrate each day. This "
      "change is not a change in the quantity of water. It is an artifact: the probe does not touch "
      "the substrate correctly, or the calibration is incorrect." +
      _c("kargas-temp-capacitance-correction-2012") + " Monitor the wetting curve and the drying "
      "curve of each pot. If they are different from the usual curves, the cause is possibly "
      "hydrophobic substrate or channeling.</p><p>Monitor each pot that is different from the pots "
      "near it that have the same treatment. The cause is possibly a blocked emitter or a defective "
      "probe. It is not a problem of the plant."),
    callout("danger", "Temperature and EC change your confidence, not the water number",
      p("Do not let temperature and EC change the estimate of stored water directly. Let them "
        "change your <strong>confidence</strong> in the reading. The temperature cycle of each day "
        "can cause a dielectric change in dry substrate. This change is a physical effect. It has "
        "the same effect on the reading as a change in water content." +
        _c("nasta-2024-teros12-temp-correction") + "</p><p>Do not let that change write the VWC. If "
        "you do, a physical effect causes the irrigation, and not the water uptake of the plant.")),
    figure(L.flow("Fault diagnosis: equipment first, then artifacts, then local faults",
            [("Constant, NaN, expired?", "equipment fault → stop"),
             ("Temperature effect?", "artifact → less confidence"),
             ("One pot different?", "local fault → examine"),
             ("If none", "use it as a witness with noise")],
            note="Equipment faults stop the operation. Representativeness faults only decrease confidence."), 10,
      "Do the checks in sequence: first for equipment faults, then for artifacts and then for local "
      "faults. Use the number only after these checks."),
    table(["Symptom", "Possible cause", "It is NOT", "Task"], [
      ["The VWC is at the limit of the range, is constant, is &lsquo;NaN&rsquo; or is an expired value", "Fault in the equipment or the cable", "A correct reading of water", "Stop steering. Operate a safe procedure with limits. Tell a person."],
      ["The VWC changes with the temperature each day", "Bad contact, or an artifact of the calibration", "A change in the quantity of water", "Decrease the confidence in the absolute VWC. Examine the position of the probe." + _c("kargas-temp-capacitance-correction-2012")],
      ["The wetting curve and the drying curve are very different", "Channeling, or hydrophobic substrate", "Defective sensor", "Examine the substrate. Make the substrate wet again. Examine the position of the probe."],
      ["One pot is different from the pots near it", "Blocked emitter or defective probe", "A problem of the plant, at this time", "Examine the emitter and the probe before you think that the plant has a problem."],
    ], cls="compact", caption="From symptom to cause to task. The &lsquo;It is NOT&rsquo; column is the most important. The primary cost is an incorrect diagnosis."),
    callout("warn", "Use more than one irrigation event to set a capacity anchor",
      p("Do not let one manual reading or one observation by a person set a capacity anchor. Do not "
        "let it override a safety interlock. A capacity anchor must come from more than one "
        "irrigation event, with a second witness for each irrigation event. One good observation is "
        "not sufficient.")),
  ]})

SECTIONS.append({"id": "expectations", "kicker": "Facts and limits", "title": "Expected results and limitations",
  "blocks": [
    callout("key", "The facts",
      p("One TEROS-12 cannot give you the correct condition of the root zone for each zone. If you "
        "think that it can, you make the most frequent error and the error with the highest cost. "
        "With a substrate-specific calibration, you can find the <em>trends</em> of dryback. You "
        "can also calculate an estimate of the water in the substrate with an accuracy of "
        "approximately &plusmn;0.01&ndash;0.02 m&sup3;/m&sup3; in the position of the probe. This "
        "accuracy is sufficient for steering if you include the uncertainty in your decisions and "
        "compare the data with a second witness." + _c("fragkos-2024-teros12-soils-ec"))),
    figure(L.zones("Confidence: one probe, or probe + witness + calibration",
            0, 100,
            [(0, 45, L.REDL, "only one probe, wide error band, many limits"),
             (45, 100, L.GL, "probe + second witness + calibration: for steering")],
            unit="% trust",
            note="A calibration and a second witness change the probe from a source with many limits to a source for control."), 11,
      "Only one probe has a wide error band and many limits. When you add a substrate-specific "
      "calibration and a second witness, the error band becomes smaller. You can use this range for "
      "steering." + _c("nemali-2006-set-point-irrigation")),
    ul(["With a substrate-specific calibration, the best result is a correct shape of the dryback. "
        "The accuracy for the stored water in the local position of the probe is approximately "
        "&plusmn;0.01&ndash;0.02 m&sup3;/m&sup3;.",
        "One probe cannot give the runoff for each zone. It cannot show that the system supplied "
        "water. It cannot give the correct average of the zone for all the pots.",
        "A <strong>load cell</strong> (pot weight) is the most important sensor to add, because it "
        "measures the water in the substrate directly. It does not use the dielectric properties of "
        "the substrate.",
        "Make the system give a clear &lsquo;I cannot tell&rsquo; output. Do not give a precision "
        "that is higher than the accuracy. Let the system control only when the data show that it "
        "can."]),
    p("The best method is to make the system show <em>when it cannot tell</em>. The system must not "
      "give a number with more confidence than the data give. Calibrate first and add a second "
      "witness. Then read the <a href='smart-watering-vrwe.html'>guide to smart irrigation "
      "(VWC/EC)</a> for information on how those signals control the shots. Read the <a "
      "href='signal-and-noise.html'>paper on signal and noise</a> for information on the difference "
      "between a trend and sensor noise."),
  ]})
