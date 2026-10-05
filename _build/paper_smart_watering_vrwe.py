# -*- coding: utf-8 -*-
"""Paper: the smart watering brain (VRWE), in plain English (beginner)."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        stagecard, grid, card, chip, kv, steps)
import figs_lib as L

SLUG = "smart-watering-vrwe"
TITLE = "The VRWE automatic irrigation controller"
EYEBROW = "Precision · Automatic irrigation"
SUB = ("This paper shows how VRWE uses some signals together to calculate the water in the root "
       "zone more accurately than one probe. You will know the cause when VRWE waits and does not "
       "apply water. You will also know how to read the confidence of VRWE and if you can accept "
       "the estimate.")
META = [("gauge", "Precision"), ("image", "9 diagrams"),
        ("quote", "5 sources"), ("clock", "~9 min to read")]
RELATED = ["root-zone-teros12", "signal-and-noise", "closed-loop"]
REF_IDS = ["szerement-seven-rod-2019", "mane-dielectric-calibration-review-2024",
           "koehler-transpiration-vpd-2023", "owen-norden-preferential-flow-2024",
           "hydrus-soilless-substrate-dynamics"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

SECTIONS.append({"id": "what-this-is", "kicker": "Start here", "title": "Purpose and scope",
  "blocks": [
    callout("evidence", "Weak",
      "<p><strong>Limit of the data:</strong> The method of VRWE is good. It uses more than one "
      "signal and it is careful. You cannot be sure that VRWE does not apply too much water or not "
      "sufficient water. The sensors must be in good condition, the calibration must be correct, "
      "and the fail-safe functions must operate. Keep the emergency minimum VWC values. Make sure "
      "that a person can override VRWE.</p>"),
    lead("<strong>Virtual Root-Zone Water Estimator</strong> (VRWE) is a software controller that "
         "selects when to apply water to a plant and how much water to apply. VRWE uses some "
         "signals together and does not obey one sensor. The name includes &lsquo;virtual&rsquo; "
         "because VRWE does not measure the water directly. VRWE calculates the quantity of water "
         "from some signals."),
    p("Each pot has only one moisture sensor. The sensor measures only a small part of the substrate" +
      _c("szerement-seven-rod-2019") + ". If this part is dry, or if water flows around it, the "
      "sensor shows that the pot is dry. A controller that obeys only the sensor then applies too "
      "much water and can cause damage to the plant. VRWE uses the sensor reading as one signal "
      "that it examines. VRWE does not obey the sensor."),
    figure(L.flow("How VRWE operates: three steps",
            [("SENSOR", "one sensor, small area, can be incorrect"),
             ("ESTIMATE", "VRWE calculates the water balance"),
             ("DECISION", "apply water / wait / tell a person")],
            note="The sensor is the first step. It is not the decision."), 1,
      "VRWE gets one signal from the sensor. The sensor measures a small area and can be incorrect. "
      "VRWE compares this signal with other data and calculates an estimate. Then VRWE makes a "
      "careful decision. All of this paper is about the ESTIMATE step."),
    callout("note", "About this paper",
      p("This paper gives information on how the system <em>operates</em>. This paper is not a "
        "report of a laboratory test. Read this paper with the <a "
        "href='root-zone-teros12.html'>root-zone sensor</a> paper (the quantities that one probe "
        "measures) and the <a href='signal-and-noise.html'>signal and noise</a> paper (how to find "
        "if a change is in the plant or only sensor noise).")),
  ]})

SECTIONS.append({"id": "key-terms", "kicker": "Terms", "title": "Definitions",
  "blocks": [
    p("Five terms are important in all parts of this paper. This section gives the five definitions "
      "first. It is not necessary to know them at this time, because each term occurs again in the "
      "sections that follow."),
    defterm("VWC (volumetric water content)", "The quantity of water in the substrate at the "
            "position of the sensor, as a percentage. VRWE compares this sensor reading with other "
            "data."),
    defterm("Runoff / drain", "Water that flows out of the bottom of the pot. The plant does not "
            "use this water."),
    defterm("Full pot (DUL, drained upper limit)", "The maximum quantity of water that the pot can "
            "hold after the drainage stops. The water that you add after this point flows out as "
            "runoff."),
    defterm("Channeling", "Water that flows straight down one channel and does not touch the roots. "
            "An example is a gap between the pot and the liner. All the water uses this easy "
            "channel and not the substrate. The water flows out at the bottom, and the root zone "
            "near the channel stays dry. The water goes in at the top and out at the bottom, and it "
            "does not help the plant."),
    defterm("Confidence", "The value that VRWE gives to show how accurate its estimate is at this "
            "time. High confidence lets VRWE apply more water. Low confidence makes VRWE careful."),
    table(["Term", "Definition"], [
      ["<strong>VWC</strong>", "The quantity of water in the substrate at the position of the sensor"],
      ["<strong>Runoff / drain</strong>", "Water that flows out of the bottom of the pot"],
      ["<strong>Full pot (DUL)</strong>", "The maximum quantity of water that the pot holds after the drainage stops"],
      ["<strong>Channeling</strong>", "Water that flows to the drain and does not touch the roots"],
      ["<strong>Confidence</strong>", "The value that shows how accurate the estimate of VRWE is at this time"],
    ], cls="compact", caption="The five terms that are important in this paper."),
  ]})

SECTIONS.append({"id": "why-fuse", "kicker": "Primary information 1", "title": "Some signals together correct one incorrect reading",
  "blocks": [
    p("VRWE keeps a <strong>water balance</strong> and does not obey one probe. IN is the water "
      "that the drippers supply. The quantity is accurate because you calibrate the drippers. Thus "
      "you know accurately how much water you apply. OUT is the water that the plant uses and the "
      "runoff. The balance is the quantity of water that is in the pot."),
    p("A plant continuously absorbs water through its roots and releases the water as vapor through "
      "small pores in the leaves. When the temperature and the light intensity increase, the plant "
      "releases the vapor at a higher rate. <strong>Transpiration</strong> is the movement of water "
      "from the roots through the stems and out through the leaf pores as vapor.</p><p>You can "
      "measure temperature and light. Thus VRWE can calculate the rate at which the plant uses "
      "water, from these readings only" + _c("koehler-transpiration-vpd-2023") +
      ". As a result, VRWE has an estimate of OUT that does not use the sensor. VRWE compares the "
      "sensor reading with the balance. The sensor is not the only source of correct data."),
    figure(L.bars("One irrigation cycle as a water balance",
            [("Start", 55), ("+ IN (irrigation)", 75), ("- plant uptake", 66), ("- runoff", 60)],
            unit="%", note="Each cycle: add the water you apply. Subtract the plant uptake and the runoff.",
            maxv=85), 2,
      "VRWE calculates the water balance again in each cycle. The last number is the best estimate "
      "of VRWE for the water in the root zone. VRWE gets this number before it examines the sensor "
      "reading."),
    figure(grid([
            card("Inputs IN", "The volume of irrigation water that the calibrated drippers supply.", "accurate"),
            card("Inputs OUT", "The plant uptake and the drainage. VRWE calculates the plant uptake from the temperature and the light.", "approximate"),
            card("One signal", "The VWC reading of the sensor. VRWE compares the reading with other data and does not obey the reading.", "check"),
            card("Estimate + confidence", "VRWE puts all the signals together in one number. It also gives the confidence value for the number.", "output"),
           ], cols=2), 3,
      "Some signals go into one estimate. VRWE has more than one signal from different sources. "
      "Thus the other signals can correct one incorrect signal, and VRWE does not obey the "
      "incorrect signal."),
    callout("key", "Use more than one signal",
      p("If you use only one sensor, one incorrect reading becomes an incorrect decision. If the "
        "estimate uses some signals from different sources, the other signals correct one incorrect "
        "signal. The system stays correct when one input is incorrect.")),
  ]})

SECTIONS.append({"id": "trust-and-uncertainty", "kicker": "Primary information 2", "title": "Confidence: how sure the estimate is",
  "blocks": [
    p("VRWE gives a <strong>confidence meter</strong> with each estimate. The meter shows how sure "
      "VRWE is. If you have only a number, for example &lsquo;58% wet&rsquo;, you do not know how "
      "accurate the number is."),
    p("The confidence is high when the signals from different sources agree. This occurs when the "
      "sensor, the water balance and the uptake estimate show the same result. The confidence "
      "decreases when the signals do not agree. For example, the sensor shows that the substrate is "
      "dry, but the water balance shows that the pot is full.</p><p>A defective sensor can only "
      "make VRWE <em>more careful</em>. The sensor cannot cause VRWE to find more room for water "
      "than the water balance shows. The water balance gives protection to the plant."),
    figure(L.zones("The confidence meter and the decision in each zone", 0, 100,
            [(0, 40, L.REDL, "Low: wait / tell a person"),
             (40, 70, L.AMBL, "Moderate: small safe shot"),
             (70, 100, L.GL, "High: apply a full shot")],
            unit="%",
            note="Higher confidence lets VRWE apply more water. Low confidence makes VRWE careful."), 4,
      "Confidence is a value on a scale. It is not a yes or no. A shot is the quantity of water "
      "that you apply in one irrigation. When the confidence is high, VRWE applies a full shot. "
      "When the confidence is moderate, VRWE applies only a small safe shot. When the confidence is "
      "low, VRWE waits or tells a person."),
    callout("tip", "The system stays safe with a defective sensor",
      ul(["Each estimate has a confidence value, and not only a number.",
          "When signals from different sources agree, the confidence increases. When they do not agree, the confidence decreases.",
          "Low confidence makes VRWE careful. VRWE does not apply a full shot.",
          "A defective sensor causes VRWE to wait. It does not cause too much water or not sufficient water."], "tight")),
  ]})

SECTIONS.append({"id": "what-it-decides", "kicker": "Primary information 3", "title": "Irrigation decisions",
  "blocks": [
    p("VRWE makes one of only three decisions. The decision uses two values: the "
      "<strong>confidence</strong> and the <strong>headroom</strong> (the quantity of water that "
      "you can add before the pot is full)."),
    figure(L.flow("The three decisions of VRWE",
            [("High confidence + headroom", "apply a full shot"),
             ("Not sure", "wait, or apply a small safe shot"),
             ("Signals do not agree", "tell a person and make no decision")],
            note="In all decisions, a small temporary deficit is better than too much water if VRWE is not sure. The emergency VWC minimum is also necessary."), 5,
      "VRWE makes only three decisions. In all three decisions, a small temporary deficit is better "
      "than too much water when VRWE is not sure."),
    p("When the confidence is high and there is headroom, VRWE applies a full shot. When VRWE is "
      "not sure, it waits or applies a small safe shot, and it does not apply a full shot. When the "
      "signals do not agree and VRWE cannot find which signal is correct, it tells a person. In all "
      "three decisions, <strong>a small temporary deficit of water is better than too much water if "
      "VRWE is not sure. The emergency minimum VWC is also necessary.</strong>"),
    callout("key", "The safe decision",
      p("Apply more water only when the confidence is high. If VRWE is not sure, it makes the safe "
        "decision. This one instruction makes automatic irrigation safe.")),
  ]})

SECTIONS.append({"id": "shared-drain-howto", "kicker": "In a facility", "title": "How to read shared-drain measurements",
  "blocks": [
    p("In a facility, the conditions are not as easy as for one pot. Frequently, <strong>three grow "
      "rooms drain into one shared sump</strong> (a bucket that collects the water, with a pump). "
      "The condensate from the air conditioner (AC) and from the dehumidifier also goes into the "
      "same bucket. The pump removes the water from the bucket in a pump cycle. After a pump cycle, "
      "you cannot know if the water is from too much irrigation in a room or only from the AC "
      "condensate. VRWE finds the cause in three steps."),
    steps([
      ("Find the background drip", "At night, irrigation is off. The only water that goes into the sump is the condensate from the AC and from the dehumidifier. VRWE finds the quantity of this stable background drip. Then VRWE subtracts it from each reading that follows."),
      ("Use different irrigation times", "Each room has a different irrigation time. Thus the time of each pump cycle agrees with the irrigation time of one room. As a result, VRWE can find which room caused each pump cycle."),
      ("Show &lsquo;not sure&rsquo; when VRWE cannot find the cause", "If two irrigations occur at the same time, VRWE cannot find the cause of a pump cycle. Then VRWE shows &lsquo;not sure&rsquo; for the reading and gives no cause. VRWE uses the same fail-safe method in all other parts of the system."),
    ]),
    figure(grid([
            card("Room A", "The room drains into the shared sump.", "source"),
            card("Room B", "The room drains into the shared sump.", "source"),
            card("Room C", "The room drains into the shared sump.", "source"),
            card("AC + dehumidifier", "A continuous drip of condensate. VRWE finds the drip at night and subtracts it.", "noise"),
            card("Shared sump + pump", "One bucket and one pump cycle. You cannot know which room caused the cycle.", "problem"),
            card("Find the cause", "Subtract the background drip. Use different irrigation times. Show &lsquo;not sure&rsquo; when VRWE cannot find the cause.", "solution"),
           ], cols=3), 6,
      "Three rooms, the AC and the dehumidifier all send water to one sump. Thus you cannot know "
      "the cause of one pump cycle. The three steps find which room caused each pump cycle."),
    figure(L.line("Different times show the cause of each pump cycle",
            [(0, 5), (1, 38), (2, 12), (3, 6), (4, 41), (5, 14), (6, 7), (7, 39), (8, 10)],
            ["00:00", "A irrigates", "+30m", "B start", "B irrigates", "+30m", "C start", "C irrigates", "+30m"],
            ylab="drain rate", ymin=0, ymax=50,
            note="The low baseline is the AC drip. Each peak occurs when one room receives irrigation."), 7,
      "The rooms have different irrigation times. Thus each peak in the drain rate occurs at the "
      "time of the room that caused it. A pump cycle immediately after the irrigation of a room "
      "shows that the pots of the room are full or have too much water."),
    callout("note", "The information from a pump cycle after irrigation",
      p("A pump cycle <em>immediately after</em> the irrigation of a room shows that the pots of "
        "the room are at &lsquo;full pot&rsquo; and that water flows out. You can use this "
        "information. It is not a fault.")),
  ]})

SECTIONS.append({"id": "pitfalls", "kicker": "When there is a problem", "title": "Troubleshooting",
  "blocks": [
    p("The problems below can occur. VRWE must continue to operate correctly when they occur. VRWE "
      "is the solution to these problems. The protection is the same for each problem. VRWE "
      "compares the reading with the water balance and decreases the confidence. VRWE does not do a "
      "task because of one reading that is possibly incorrect."),
    figure(grid([
            card("Sensor in a dry area", "The probe is in a local dry area and shows that the pot is dry. The remaining part of the pot has the correct water content.", "incorrect"),
            card("Channeling", "Water flows quickly down one side of the pot. It goes around the sensor and the roots, straight to the drain.", "incorrect"),
            card("Shared-drain problem", "One bucket does not show which room had too much water.", "incorrect"),
           ], cols=3), 8,
      "Three usual problems. In each problem, one signal is incorrect. None of the problems causes "
      "VRWE to make an incorrect decision. The water balance and the confidence meter show that the "
      "signals do not agree."),
    p("Look carefully at channeling, because it is not easy to find. In a container, water can flow "
      "in a <strong>preferential flow path</strong>, a fast channel that sends the irrigation water "
      "around the root zone" + _c("owen-norden-preferential-flow-2024") + ". The volume of "
      "irrigation water that you apply is correct, but the water does not touch the roots and shows "
      "only as drain. The properties of a soilless substrate change the speed at which water flows "
      "through the substrate and out of it" + _c("hydrus-soilless-substrate-dynamics") +
      ". Thus VRWE monitors the time of the drain and not only the volume of the drain."),
    figure(grid([
            card("Top of the pot", "The irrigation water goes into the pot here.", "in"),
            card("Preferential flow path", "Water flows quickly down one side. It goes around the sensor and the roots.", "around"),
            card("Drain", "The water flows out at the bottom almost immediately. The roots stay dry.", "out"),
           ], cols=3), 9,
      "A cross-section of channeling: the water goes in at the top and out at the bottom, and it "
      "does not touch the roots. In the water balance, a channel shows as a large quantity of water "
      "in and a large quantity of drain immediately after it. VRWE uses this sign to decrease the "
      "confidence."),
    callout("warn", "The protection is always the same",
      p("VRWE does not obey a reading that is possibly incorrect. VRWE compares the reading with "
        "the water balance. If the two do not agree, VRWE decreases the confidence and is careful. "
        "One incorrect sensor reading does not cause too much water or not sufficient water for the "
        "plant.")),
  ]})

SECTIONS.append({"id": "expectations", "kicker": "The limits", "title": "Expected results and limitations",
  "blocks": [
    callout("key", "The results that VRWE gives and the results that it does not give",
      ol(["<strong>The safe decision.</strong> VRWE applies more water only when the confidence is high. When the confidence is not high, VRWE makes the safe decision. VRWE calculates estimates from signals, and it cannot know more than the signals show.",
          "<strong>The worst result is that VRWE is too careful.</strong> A defective sensor makes VRWE careful. The defective sensor does not cause very bad damage. VRWE will wait or tell a person before it applies too much water or not sufficient water.",
          "<strong>It is usual that VRWE waits or tells a person.</strong> VRWE must make these decisions when it is not sure. They show that the system operates correctly. They do not show a fault.",
          "<strong>Incorrect input gives incorrect output.</strong> The estimate is only as good as the inputs. It is important that the volumes of the drippers are accurate and that VRWE has the drain baseline. Drift in the calibration of the sensor slowly decreases the accuracy of each estimate that uses the sensor." + _c("mane-dielectric-calibration-review-2024")])),
    p("VRWE is slower than a timer by a small quantity, but it is much safer. At some times, VRWE "
      "waits and a controller with only a timer applies water. This difference is the correct "
      "operation of VRWE.</p><p>For more information about the measurements of one probe, read the "
      "<a href='root-zone-teros12.html'>root-zone sensor</a> paper. VRWE finds if a change is in "
      "the plant or only sensor noise before it makes a decision. For information on this check, "
      "read the <a href='signal-and-noise.html'>signal and noise</a> paper."),
  ]})
