# -*- coding: utf-8 -*-
"""Paper: the one steering law (beginner synthesis of crop steering across substrates).

A beginner-first synthesis of the coco, rockwool, substrates, root-zone (TEROS-12),
smart-watering (VRWE), F2 and irrigation papers into a single law: steering is one law;
the sponge only changes the constants. The 31 figures are bespoke inline SVGs loaded
from figs_one_steering_law.json (kept out of this module for readability).
"""
import os, json
from components import p, lead, ul, callout, defterm, table, figure, steps

_FIGS = json.load(open(os.path.join(os.path.dirname(__file__), "figs_one_steering_law.json"), encoding="utf-8"))
_N = [0]
def fig(key, cap):
    _N[0] += 1
    return figure(_FIGS[key], _N[0], cap)

SLUG = "one-steering-law"
TITLE = "One steering law: coco, rockwool, soil and water"
EYEBROW = "Flowering · Crop steering"
SUB = ("Coco, rockwool, soil and a tank of water use the same method of steering. This paper gives "
       "the method one time, with diagrams. Then you can use the method with each substrate, "
       "because the substrate changes only the numbers.")
META = [("droplet", "Flowering"), ("image", "31 diagrams"),
        ("quote", "9 sources"), ("clock", "~22 min to read")]
RELATED = ["coco-crop-steering", "rockwool-crop-steering", "substrates-overview",
           "root-zone-teros12", "smart-watering-vrwe", "f2-crop-steering"]
REF_IDS = ["caplan2019-drought", "welling2025-aba", "stack2024-drought", "hilhorst2000-ec",
           "abad2005-coir", "noguera2003-cec", "malik2025-media",
           "szerement-dielectric-2019", "tdr-fdr-soil-review-2024"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

# ---------------------------------------------------------------- 0 promise
SECTIONS.append({"id": "the-promise", "kicker": "Start here", "title": "Purpose and scope",
  "blocks": [
    callout("evidence", "Weak",
      "<p><strong>Limit of the data:</strong> Do not use the electrical conductivity (EC) values of "
      "high-intensity rockwool steering (approximately 3.5 to 6) in coco procedures for new "
      "growers. In deep water culture (DWC), the risk of disease increases when the water is hot "
      "and the dissolved oxygen is low. There is no time limit that is correct for all systems, "
      "such as &lsquo;at a temperature of more than 23 &deg;C (73 &deg;F), the heat kills the plant "
      "in one day&rsquo;.</p>"),

    lead("A cannabis plant can use its energy to make <strong>leaves</strong>. A plant with more "
         "leaves is larger and has more green material. The plant can also use its energy to make "
         "<strong>flower</strong>. Flower is the group of buds with resin that you harvest. "
         "&lsquo;Steering&rsquo; is the control of the plant with water. The water causes a small "
         "change in the plant in the direction of more leaves or more flower."),
    callout("tip", "One method for each substrate",
      p("Coco, rockwool, soil and a tank of water are four substrates. A substrate is the material "
        "that contains the roots. You use the same method of steering in all four. This method is "
        "the <em>steering law</em>. A different substrate does not change the method. It changes "
        "only the numbers.")),
    fig("fig-0-leaves-vs-flower",
        "Leaves make a larger plant with more green material. Flower is the group of buds that you "
        "harvest. Steering changes the plant in the direction of leaves or of flower."),
    p("The three controls do not change. You use the same three controls for each substrate:"),
    ul(["<strong>Water content</strong> is the quantity of water in the substrate at this time. The "
        "grower term is volumetric water content (VWC). Use this one number to control the plant.",
        "<strong>Dryback</strong> is the quantity by which the water content decreases each day. "
        "You control the quantity of water that the plant removes from the substrate. This control "
        "has the largest effect.",
        "<strong>Feed strength</strong> is the concentration of the feed around the roots. The grower term is EC. You select the strength of the feed."]),
    p("The substrate (coco, rockwool, soil or a tank of water) does not change the three controls. "
      "It changes <strong>only the numbers</strong>."),
    fig("fig-1-car-controls",
        "You use the same three controls for each substrate. The substrate changes only the numbers."),
    p("After you read this paper, you will know the full procedure. Each morning, at lights-on, let "
      "the water content decrease by a small quantity. Then fill the substrate again with small "
      "shots. A shot is a small quantity of water that the dripper supplies in a short "
      "time.</p><p>Keep the water content stable during the day. During the night, let the "
      "substrate dry. The next day, start again. The other sections of this paper give more "
      "information about each part of this loop."),
    fig("fig-2b-the-loop-hero",
        "The full task is one cycle each day. You fill the substrate, and the water content decreases (dryback). You keep the water content stable, and the substrate dries. Then the cycle starts again."),
    callout("note", "Optional sections",
      p("Sections 1 to 6 and the last section give the information for manual steering. The two "
        "<strong>optional</strong> sections are about moisture sensors and automatic irrigation "
        "controllers. If you irrigate manually, these two sections are not necessary.")),
    callout("key", "In short",
      p("One method of steering with water controls the plant in the direction of leaves or of "
        "flower. Coco, rockwool, soil and water change only the numbers. They do not change the "
        "steering.")),
  ]})

# ---------------------------------------------------------------- glossary
SECTIONS.append({"id": "plain-words", "kicker": "Glossary", "title": "Definitions",
  "blocks": [
    p("If a term in this paper is new to you, find it in this section. Each item gives the term and "
      "then the definition."),
    defterm("Crop steering", "Crop steering is the control of the time and the quantity of the water that you apply to the plant. It causes a small change in the plant in the direction of leaves (a larger plant with more green material) or flower (the buds that you harvest). The change occurs during some days. The plant does not change in one night."),
    defterm("Substrate (medium)", "The material that contains the roots of the plant: coco, rockwool, soil or a tank of water. This paper uses the term &lsquo;substrate&rsquo; for all four."),
    defterm("Water content (VWC)", "The quantity of water in the substrate, as a percentage of the space in the substrate. At 60%, water fills 60 of each 100 pores. VWC is the volumetric water content. It is the one number that you use to control the plant."),
    defterm("Dryback", "The quantity by which the water content decreases between two shots. It is the high value minus the low value. Measure it in percentage points. When the water content decreases from 78% to 58%, the dryback is 20 points. The dryback shows the quantity of water that the plant removes from the substrate. It is the most important control for steering."),
    defterm("Percentage points and percent", "We always measure the dryback in points. When the water content decreases from 78 to 58, the dryback is 20 points. It is not possible to know if the value &lsquo;20%&rsquo; is a quantity in points or in percent. Thus this paper gives each dryback in points."),
    defterm("Feed strength (EC)", "The concentration of the fertilizer feed around the roots. A higher value is a stronger feed with more salt. When the substrate dries, the quantity of water decreases and the nutrients stay. Thus the EC increases, and you do not add feed. EC is the electrical conductivity, in mS/cm. You can use a scale of strength from 1 to 10 for the EC."),
    defterm("Field capacity", "The highest water content that the substrate has after the drainage of water stops. It is the maximum water content for each day. The value is different for each pot and each substrate. It is not a reference value. The value decreases when the roots fill the pot."),
    defterm("Recovery floor", "The minimum water content, approximately 25 to 30% in rockwool. The dryback must not make the water content less than this value. If the water content is less than this value, the substrate does not absorb water again, and the water flows straight through the substrate. The dripper cannot correct this condition."),
    defterm("Vegetative mode", "Steering of the plant in the direction of leaves, stems and size. The substrate is wetter, the dryback is small, the feed is weaker, and the shots are small and many. In this mode, the plant makes leaves and stems and becomes larger."),
    defterm("Generative mode", "Steering of the plant in the direction of flower, density and resin. The substrate is drier, the dryback is larger, the feed is stronger, the number of shots is smaller and each shot is larger. In this mode, the plant makes the buds that you harvest."),
    defterm("Abscisic acid (ABA)", "The stress hormone of the plant. A small, controlled water deficit causes the plant to release ABA. ABA causes a small change in the plant, away from leaves and in the direction of flower and resin. Thus a dryback controls the plant. You do not measure ABA."),
    defterm("The four phases of each day (P0&ndash;P3)", "The four phases of each day of steering. In the first phase, at lights-on, the water content decreases by a small quantity. In the second phase, you fill the substrate to field capacity with small shots. In the third phase, you keep the water content in a range during the day. In the fourth phase, you stop the shots, and the large night dryback sets the substrate to the start condition for the next day."),
    defterm("Shot", "A small quantity of water that the dripper supplies in a short time. The size of a shot is a percentage of the volume of the substrate. Steering uses some small shots each day, and not one large quantity of water. You calculate the time of each shot from the size of the pot, the flow rate of the dripper and the number of drippers."),
    defterm("Sawtooth", "The shape of a correct graph of the water content. The line decreases slowly (the dryback) and then increases quickly (a shot). The two parts occur again and again. A line that does not change, or a line that only decreases, shows that irrigation does not occur."),
    defterm("Buffer (CEC)", "The quantity by which a substrate decreases the effect of an error in the feed. The substrate holds nutrients and releases them again. CEC is the cation exchange capacity. Coco has a large buffer, and living soil corrects errors in the feed. Rockwool has almost no buffer, and water has no buffer."),
    defterm("Runoff", "The small fraction of the feed that drains from the bottom of the pot, approximately 10 to 20%. Runoff is not waste. It removes the salt that collects in the substrate. When you measure the runoff, you find the correct feed strength of the substrate."),
    defterm("Channeling", "The condition in which the water flows straight down along one line and out of the bottom of the pot. The water does not go to the roots, and the middle of the substrate stays dry. To find channeling, examine the flow rate of the water from the pot, and not the quantity of water."),
    defterm("Permittivity", "The size of the effect that a material has on the weak electric field of the probe. Water has a large effect, dry substrate has a small effect, and air has almost no effect. This difference lets a probe in the substrate find water that you cannot see."),
    defterm("Resolution and accuracy", "Resolution is the number of decimal places that the sensor shows. Accuracy is the size of the error of the reading. A sensor with a small error has a high accuracy. A sensor can have a high resolution and an error of a small number of points until you calibrate it."),
    defterm("Second check", "A check with a different method to make sure that the probe reading is correct. The check can be the water that drains from the pot or the weight of the pot. Do this check before you apply water."),
    defterm("Water balance", "The quantity of water that you apply to the pot, minus the water that the plant transpires and the water that drains. The controller calculates this value all the time. The water that you apply is the water from the shots of the dripper. The water balance gives the quantity of water in the pot. Thus you do not use only one sensor."),
    defterm("Confidence", "A value that shows if the reading is correct. The confidence is high when the data agree and low when the data do not agree. When the confidence is high, the controller can apply a full shot. When the confidence is low, it applies a very small shot, waits, or gives the decision to a person."),
    defterm("Safe irrigation", "The one safety instruction for all automatic irrigation: apply more water only when you know that there is space in the substrate. If you are not sure, do the safe step. A sensor with an incorrect reading can only make the controller more careful. It cannot cause the controller to apply too much water."),
    defterm("Transfer function", "The change that the substrate makes to your irrigation before the roots receive it. The substrate changes the irrigation by constant quantities. The same irrigation gives a different effect on the roots for each substrate."),
  ]})

# ---------------------------------------------------------------- 1 sponge
SECTIONS.append({"id": "everything-is-a-sponge", "kicker": "One model", "title": "Substrate water storage",
  "blocks": [
    callout("tip", "Each substrate has pores",
      p("Each substrate (coco, rockwool, soil, and also roots in water) has a constant number of "
        "small pores. Each pore contains water or air. From here, this paper uses this one model "
        "for all the substrates.")),
    p("The substrate is the material that contains the roots. The total space in the substrate is "
      "<strong>constant</strong>, and each pore contains water or air. When water goes in, the "
      "water pushes air out. <strong>When there is more water, there is always less air.</strong>"),
    p("The quantity of air is important because the roots must have <em>air</em> and water. If the "
      "substrate stays too wet, the roots do not get sufficient air. If it stays too dry, the "
      "growth of the roots stops. Each substrate has a different usual ratio of water to air."),
    fig("fig-3-sponge-seesaw",
        "The space in a substrate is constant. When you add water, the water pushes air out of the pores. The roots use this air."),
    p("Different substrates keep very different quantities of air, also when the substrate is fully "
      "wet" + _c("malik2025-media") + ". This one fact causes the difference between substrates in "
      "the risk that you apply too much water."),
    fig("fig-4-air-when-wet",
        "Coco keeps approximately one part in five of its space as air when it is fully wet. "
        "Rockwool keeps only one part in ten. Thus you cannot easily apply too much water to coco."),
    callout("note", "Numbers",
      ul(["Coco keeps approximately <strong>22%</strong> air when it is fully wet" + _c("abad2005-coir") +
          ". Rockwool keeps only approximately <strong>10%</strong>.",
          "Peat keeps approximately <strong>18 to 25%</strong> air when it is wet. The total space in coco is approximately 94 to 96%."])),
    p("A substrate has a <strong>second trait</strong> that you do not see easily. This trait is "
      "also important: the <em>buffer</em>. The buffer is the quantity by which the substrate "
      "decreases the effect of an error in the feed. Some substrates absorb the error and prevent "
      "damage to the plant" + _c("noguera2003-cec") + ".</p><p>In other substrates, the effect of "
      "the error occurs immediately. This paper gives the measurements in a subsequent section. At "
      "this time, we use only the terms &lsquo;large buffer&rsquo; and &lsquo;small buffer&rsquo;."),
    fig("fig-5-cushion-spectrum",
        "Substrates with a large buffer (soil, coco) absorb the same error in the feed. In "
        "substrates with a small buffer (rockwool, water), the effect of the error occurs "
        "immediately."),
    callout("key", "In short",
      p("Each substrate has a constant quantity of space. Irrigation controls the part of the space "
        "that contains water and the part that contains air.")),
  ]})

# ---------------------------------------------------------------- 2 wheel & engine
SECTIONS.append({"id": "wheel-and-engine", "kicker": "First two controls", "title": "Water content and dryback",
  "blocks": [
    callout("tip", "The plant removes water from the substrate",
      p("Water is not only a material that the plant uses. Water is also a control. Each day, the "
        "plant removes some water from the substrate. You control the quantity of water that the "
        "plant removes. A small dryback causes more leaves. A large dryback causes more flowers.")),
    p("<strong>Water content</strong> is the one number that you use to control the plant. It shows "
      "the quantity of water in the substrate at this time. At 60%, water fills 60 of each 100 "
      "pores. <strong>Dryback</strong> is the quantity by which the water content decreases between "
      "two shots. It is the high value after a shot, minus the low value before the next shot."),
    callout("note", "Give the dryback in points, not in &lsquo;%&rsquo;",
      p("Always measure the dryback in percentage <strong>points</strong>. When the water content "
        "decreases from 78% to 58%, the dryback is <strong>20 points</strong> (the value decreases "
        "by 20 on the scale of 0 to 100). It is not possible to know if the value &lsquo;20%&rsquo; "
        "is a quantity in points or in percent. Thus this paper always gives points.")),
    fig("fig-6-dryback-wring",
        "The dryback is the quantity by which the water content decreases before you apply water "
        "again. Here, the water content decreases from 78% to 58%, and the dryback is 20 points (an "
        "example for rockwool)."),
    p("<strong>How drying controls the plant.</strong> A small water deficit each day causes a "
      "change in the plant. The same change occurs at the end of summer. As a result, the plant "
      "makes flowers quickly, and not more leaves" + _c("caplan2019-drought") +
      ".</p><p>This effect occurs through a stress hormone that the plant releases when it has a "
      "small water deficit" + _c("welling2025-aba") + ". The effect is a <strong>small change, and "
      "not damage</strong>. It is not necessary to know the name of the hormone for the steering."),
    fig("fig-7b-thirst-button",
        "A small water deficit causes a change in the plant. The same change occurs at the end of "
        "summer. The plant changes from the production of leaves to the production of flowers. The "
        "change is small and it is not damage."),
    p("Larger drybacks cause more flower (the buds). Smaller drybacks, with a wetter substrate, "
      "cause more leaves and a larger plant. The control is the same, and only the size of the "
      "dryback is different. The effect increases <strong>during some days</strong>. It does not "
      "occur in one night. Make a small change each day."),
    fig("fig-7c-bias-not-switch",
        "Do not change the plant in one night. Make a small change each day. During the week, the "
        "plant changes from mostly leaves to mostly flower."),
    callout("warn", "A dryback is not a drought",
      p("Always apply water before wilt occurs. The difference between a dryback and a drought is "
        "the dose and the time. When you stop the dryback at the correct time, you keep the yield. "
        "When the dryback continues for too long, the yield and the quality decrease by a large "
        "quantity" + _c("stack2024-drought") + ". Use small and accurate changes, not large changes.")),
    fig("fig-8-dryback-not-drought",
        "You stop a correct dryback and apply water again before wilt occurs. In a drought, the "
        "water content continues to decrease through the red zone, and the drought causes damage to "
        "the crop."),
    callout("note", "Numbers (example for rockwool, your values are different)",
      ul(["Vegetative mode: a dryback of 5 to 15 points. Generative mode: a dryback of 20 to 30 points.",
          "Plants in the first stage: 5 to 10 points. The last stage of vegetative growth and "
          "bulking: 10 to 15 points. The night dryback adds 5 to 15 points more, and air goes to "
          "the roots again.",
          "A test shows that a smaller night dryback, with a substrate that is approximately 10% "
          "wetter, <em>increased</em> the yield of medicinal cannabis. Some dryback is necessary, "
          "but too much dryback causes damage."])),
    callout("key", "In short",
      p("You control the plant with the dryback. The dryback is the quantity of water that the "
        "plant removes from the substrate each day. A small dryback causes more leaves. A large "
        "dryback causes more flowers.")),
  ]})

# ---------------------------------------------------------------- 3 second dial
SECTIONS.append({"id": "the-second-dial", "kicker": "Third control", "title": "Feed strength and root-zone EC",
  "blocks": [
    callout("tip", "Evaporation makes a solution stronger",
      p("When evaporation removes water from a solution, the other material in the solution stays. "
        "As a result, the solution becomes stronger. The root zone does the same with the feed.")),
    p("<strong>Feed strength</strong> (the grower term is EC) is the concentration of the "
      "fertilizer feed around the roots. A higher EC is a stronger feed with more salt. The feed "
      "strength changes when the water content changes. One fact causes this change. When the "
      "substrate dries, the quantity of water decreases and the nutrients stay. Thus the feed "
      "becomes stronger, although you do not add more feed" + _c("hilhorst2000-ec") +
      ".</p><p>As a result, a large dryback for flower is a <em>change in the feed strength</em> "
      "and also a change in the water. Water and feed are the <strong>same control</strong>."),
    fig("fig-9-squash-concentration",
        "Count the nutrients in the diagram. The number is always six. When the water decreases, "
        "the same nutrients are in a smaller volume, and the feed becomes stronger."),
    p("Read the two numbers <strong>together</strong>. When the water content decreases, the plant "
      "uses water. This effect is good until the water content decreases too much. It is usual that "
      "the feed becomes stronger when the substrate dries.</p><p>If the feed strength increases by "
      "a large quantity in a short time, the feed has too much salt. Then apply more water to "
      "decrease the concentration of salt.</p><p>If the feed strength decreases slowly during some "
      "days, the plant uses nutrients faster than the feed supplies them. Then increase the feed "
      "strength by a small quantity. A weaker feed and a wetter substrate cause more leaves. A "
      "stronger feed and a drier substrate cause more flower."),
    fig("fig-10b-ec-vwc-together",
        "When the pot dries, the feed strength increases. Each shot makes the two values go back to the start values. The water content and the feed strength change together."),
    callout("note", "Numbers (example for rockwool and water, your values are different)",
      ul(["The feed strength becomes approximately <strong>two times</strong> larger when only one "
          "part in three of the water stays in the substrate. For example, a feed that you set at "
          "3.0 can read 5.0 in the block at the end of the afternoon.",
          "Vegetative mode: approximately 3.0. Generative mode: approximately 4.5 to 6.0. A good range for each day is approximately 2 to 6.",
          "The reading of the feed strength can be incorrect when the substrate is almost dry."])),
    callout("note", "For coco growers",
      p("Coco has a large buffer. It absorbs some of the nutrients when the feed becomes stronger. "
        "Thus the feed strength increases <strong>more slowly</strong> than in rockwool or in "
        "water. The model in this section is for rockwool and water. In coco, the effect is smaller.")),
    callout("key", "In short",
      p("When the substrate dries, the quantity of water decreases and the nutrients stay. Thus a "
        "dryback also makes the feed stronger. Water and feed are the same control.")),
  ]})

# ---------------------------------------------------------------- 4 the cliff
SECTIONS.append({"id": "the-cliff", "kicker": "Two limits", "title": "Field capacity and dryback limits",
  "blocks": [
    callout("tip", "Keep the water content between two limits",
      p("The maximum limit is field capacity. If you continue to apply water after the water "
        "content is at this value, the water flows out of the bottom of the pot. The minimum limit "
        "is the recovery floor.</p><p>If the substrate dries to less than this value, the water "
        "flows straight through the substrate and does not go to the roots. The dripper cannot "
        "correct this condition. Keep the water content between the two limits. Do not let it "
        "become equal to one of the limits.")),
    p("<strong>Field capacity</strong> is the highest water content that the substrate has after "
      "the drainage of water stops. It is the maximum value of each day, and you fill the substrate "
      "until the water content is at this value. The value is different for <strong>each pot and "
      "each substrate</strong>. It is not a reference value, and it decreases when the roots fill "
      "the pot. You find it from a small number of irrigation events."),
    p("The <strong>recovery floor</strong> is a safety limit. If the substrate dries to less than "
      "this value, it does not absorb water again, and the water flows straight through it. The "
      "dripper cannot correct this condition. You must soak the substrate manually, or use a new "
      "substrate. The dryback is your steering, and the recovery floor is your safety limit. They "
      "are two different numbers."),
    fig("fig-11-lift-shaft-limits",
        "Do not let the water content become more than field capacity at the top. Do not let it "
        "become less than the recovery floor at the bottom. Control the plant in the safe range "
        "between the two limits."),
    fig("fig-12-channeling-cracked-core",
        "If the substrate dries to less than the recovery floor, it becomes very dry and gaps open "
        "in it. The water that you apply flows down the gaps and out of the bottom. The middle "
        "stays dry."),
    p("<strong>Runoff</strong> is the small quantity of feed that drains from the bottom of the pot "
      "each day. It is approximately 10 to 20% of the feed that you apply. Runoff is <em>not</em> "
      "waste. It removes the salt that collects in the substrate. When you measure the runoff, you "
      "find the correct feed strength of the substrate."),
    fig("fig-13-runoff-dipstick",
        "The small quantity of water that drains out removes the salt that collects in the "
        "substrate. It also lets you read the correct feed strength at the roots."),
    callout("note", "Numbers (example for rockwool, your values are different)",
      ul(["The recovery floor of rockwool is approximately <strong>25 to 30%</strong> water content. The range of operation is approximately 55 to 92%.",
          "Frequently, a good range for each day is approximately 30 to 70% water content. The temperature of the substrate is 20 to 26 &deg;C (68 to 79 &deg;F).",
          "The runoff of each day at field capacity is approximately 10 to 20%. Find your field "
          "capacity from approximately 5 irrigation events that agree with each other."])),
    callout("key", "In short",
      p("Do not let the water content become more than field capacity or less than the recovery "
        "floor. Steering is the safe change of the water content between these two limits.")),
  ]})

# ---------------------------------------------------------------- 5 four beats
SECTIONS.append({"id": "one-day-four-beats", "kicker": "The rhythm of each day", "title": "Irrigation phases in each day",
  "blocks": [
    callout("tip", "Four phases in each day",
      p("Each day has four phases. In the morning, the water content decreases by a small quantity. "
        "Then shots fill the substrate. During the day, the water content stays in a range. During "
        "the night, one large dryback lets air go to the roots again. The four phases are the same "
        "each day.")),
    p("Do not apply water at random times. Apply water in <strong>four phases</strong> at the same "
      "times each day. The phases agree with the lights. The four phases have the labels P0, P1, P2 "
      "and P3. In this paper, the phases are:"),
    steps([
      ("Small dryback", "At lights-on, let the water content decrease by a small quantity before the first shot. The dryback of this phase is the first dryback of the day, and you control it."),
      ("Fill", "Fill the substrate again with small shots. Increase the size of each shot by a small quantity. Continue until the water content is at the peak of the day. Stop at this value. Frequently, you do not apply all the shots that you selected for the phase."),
      ("Stable water content", "Keep the water content in a range all day. When the water content is less than the lowest value of the range, apply a small shot. Make small changes to the feed strength to control the plant."),
      ("Night dryback", "Stop the shots before lights-off. During the night, apply water only in an emergency. The large night dryback sets the substrate to the start condition for the next day."),
    ]),
    fig("fig-14-p0p3-clock",
        "Each day with lights-on has the same four phases in the same sequence: small dryback, fill, stable water content and night dryback."),
    p("A <strong>shot</strong> is a small quantity of water that the dripper supplies in a short "
      "time. The size of a shot is a small percentage of the volume of the substrate. The "
      "irrigation controller calculates the time of each shot, in seconds. It uses the size of the "
      "pot, the flow rate of the dripper and the number of drippers. You give the controller these "
      "three values."),
    p("A correct graph of the water content has the shape of a <strong>sawtooth</strong>. The line "
      "decreases slowly (the dryback) and then increases quickly (a shot), and the two parts occur "
      "again and again. A line that does not change, or a line that only decreases, shows that the "
      "irrigation does not occur. There is a fault."),
    fig("fig-15-sawtooth-heartbeat",
        "If the graph of the water content is a sawtooth, the steering operates correctly. A line that only decreases and then does not change shows a fault."),
    p("In one room, the <em>steering law</em> is this: <strong>vegetative mode and generative mode "
      "use the same four phases.</strong> Only the target numbers change. The target numbers are "
      "the size of the dryback, the feed strength and the size of the shot. The rhythm does not "
      "change."),
    fig("fig-16-veg-gen-same-loop",
        "Vegetative mode and generative mode use the same loop each day. You use a different set of numbers."),
    callout("warn", "Check the values from the manufacturer before you use them",
      p("First find the field capacity and the recovery floor of your substrate. Then set the "
        "targets to agree with them. A value of &lsquo;50% water content and 50% dryback&rsquo; "
        "from the manufacturer is not correct for your substrate.")),
    callout("key", "In short",
      p("Each day of steering has the same four phases: a small dryback, a fill, a stable water "
        "content and a night dryback. The sawtooth that occurs again and again shows that the "
        "steering operates correctly.")),
  ]})

# ---------------------------------------------------------------- 6 gearbox
SECTIONS.append({"id": "sponge-is-the-gearbox", "kicker": "Most important section", "title": "Substrate moisture as the control variable",
  "blocks": [
    callout("tip", "The substrate changes the effect of your irrigation",
      p("The substrate is between your irrigation and the roots. It changes the effect of your "
        "irrigation. A different substrate does not cause a new method of steering. You find the "
        "numbers for the new substrate.")),
    p("This section has the most important information in this paper. The substrate has a transfer "
      "function: it <strong>changes your irrigation by constant quantities</strong> before the "
      "roots receive it. The same irrigation has a different effect for each substrate. Thus a new "
      "substrate does not cause a new method of steering. You find only <strong>four "
      "numbers</strong> for the new substrate. The four numbers are the water content at field "
      "capacity, the quantity of air at field capacity, the buffer, and the recovery floor."),
    fig("fig-17-gearbox-swap",
        "Your irrigation goes into the substrate. The substrate changes it, and the roots receive "
        "the changed irrigation. The method of steering is the same for the four different "
        "substrates."),
    p("Each substrate has the <strong>same set of items</strong>, and only the numbers are "
      "different. The table shows this:"),
    fig("fig-18-gearbox-label-cards",
        "Four sets of specifications with the same rows (air, buffer, procedure to prepare the "
        "substrate, recovery floor). The numbers in the rows are different."),
    table(["Specification", "Coco", "Rockwool", "Living soil", "Water (tank)"], [
      ["Air when fully wet", "Approximately 22%. Coco keeps the most air, and you cannot easily apply too much water.", "Approximately 10%. Rockwool holds the most water, and it is easy to apply too much water.", "More air than rockwool. For peat, the value is approximately 18 to 25%.", "The roots are in the water. An air pump supplies the air."],
      ["Buffer (decreases the effect of an incorrect feed)", "A large buffer that is part of the coco.", "Almost no buffer. The plant gets the feed that you set.", "The soil corrects errors in the feed. Organisms and minerals make the feed stable in minutes.", "No buffer. The tank is the only buffer."],
      ["Recovery floor and primary fault", "When the coco dries, the effect on the plant is slow. The reading of the feed strength can be incorrect when the coco is almost dry. If you do not first soak the coco in calcium and magnesium, it removes calcium and magnesium from the feed.", "The limit is at approximately 25 to 30%, and the change at the limit is fast. At less than this value, channeling occurs. The plant shows the effect in the same hour.", "A large buffer. There is no fast change at a limit. Too much water has no effect that you can see at first, and then the problem increases.", "There is no fast change for dry conditions, but there is a limit for heat. Root rot occurs at a temperature of more than approximately 23 &deg;C (73 &deg;F), in one day or less."],
      ["Procedure to prepare the substrate, and pH at the start", "Soak the coco in a solution of calcium and magnesium for 8 to 24 h. The pH of the feed is 5.8 to 6.2.", "The pH at the start is approximately 8. Before you use the rockwool, change the pH to approximately 5.5. Then keep the pH at 5.5 to 6.0. You can use the rockwool again for approximately 3 years.", "The soil sets the pH at approximately 5.2 to 6.5. Usually, you do not adjust the pH of the input water.", "Keep the pH at 5.5 to 6.0. Keep the tank at 18 to 20 &deg;C (64 to 68 &deg;F). Operate the air pump all the time."],
      ["Good for a new grower", "<strong>Yes.</strong> Soak the coco in calcium and magnesium before you put the plants in it.", "It gives accurate control, but it has almost no buffer. Use an easier substrate first.", "<strong>Yes.</strong> It has the largest buffer of the four substrates.", "No. Use it only after you use the easier substrates."],
    ], caption="The rows are the same, and the numbers are different. When you select a substrate, you do not select a new method of steering. You select the primary fault that can occur" + _c("malik2025-media") + "."),
    p("The table shows this: <strong>when a substrate gives more control, it has a smaller buffer "
      "for your errors.</strong> Thus a new grower starts with a substrate that has a large buffer, "
      "and then uses the substrates that have a smaller buffer."),
    fig("fig-19-forgiveness-ladder",
        "The substrates are in a sequence from the largest buffer (living soil, at the top) to the smallest buffer (water, at the bottom). Start at the top."),
    fig("fig-19b-which-medium-pick",
        "For your first cultivation, start with living soil or coco. Use rockwool and water after you use these easier substrates."),
    callout("tip", "Start here: a procedure for coco",
      table(["", "Vegetative mode", "Generative mode"], [
        ["Lights", "12 / 12", "12 / 12"],
        ["Field capacity", "Find the value for each pot.", "Find the value for each pot."],
        ["Dryback", "5 to 15 points", "20 to 30 points"],
        ["Feed strength", "Approximately 3.0", "4.5 to 6.0"],
        ["Shots", "Many small shots", "A small number of large shots"],
      ], caption="Start with these values. Monitor the plants for one week. Then change one control at a time.")),
    callout("key", "In short",
      p("The substrate changes only four numbers and the type of error that causes damage to the "
        "plant. The steering does not change.")),
  ]})

# ---------------------------------------------------------------- 7 nerd: probe
SECTIONS.append({"id": "the-probe-can-lie", "kicker": "Optional: not necessary for manual irrigation", "title": "Sensor accuracy and readings",
  "blocks": [
    callout("note", "Optional section",
      p("It is not necessary to read this section unless you want to know how the sensors operate. "
        "If you irrigate manually, this section is not necessary. One piece of information is "
        "important: the moisture number is an <strong>estimate, and not an accurate value</strong>. "
        "Monitor the trend, and do a second check before you use the number.")),
    p("A probe finds water because water has a <strong>much stronger effect</strong> on the weak "
      "electric field of the probe than dry substrate or air has" + _c("szerement-dielectric-2019") +
      ". The probe uses this large difference in coco, rockwool and soil."),
    fig("fig-20-permittivity-gap",
        "Water has a much stronger effect on the electric field of the probe than dry substrate or "
        "air. This difference lets a probe in the substrate find water that you cannot see."),
    p("<strong>A high resolution is not the same as accuracy.</strong> The probe shows many decimal "
      "places, but it can have an error of a small number of points" + _c("tdr-fdr-soil-review-2024") +
      ". Until you calibrate the probe for your substrate, it is possible that you control the "
      "plant in the range of the error."),
    fig("fig-21-resolution-vs-accuracy",
        "A number with many decimal places can be incorrect until you calibrate the probe."),
    p("One probe is one <strong>local measurement</strong>. It measures only the small volume of "
      "influence around the probe, and not all the pot. Do not connect one probe directly to a "
      "valve. Do a second check (the water that drains from the pot, or the weight of the pot) "
      "before you apply water. Use the <em>shape</em> of the dryback to control the plant, and not "
      "the value of one reading."),
    fig("fig-23-one-witness-second-witness",
        "One probe measures only a small volume. Make sure that a second check agrees before you "
        "apply water: the runoff or the weight of the pot."),
    callout("warn", "Important, also if you do not read the other sections",
      p("If your dryback is <strong>smaller than the error of your sensor</strong>, your steering "
        "is an estimate. Calibrate the sensor, or use a larger dryback.")),
    callout("key", "In short",
      p("The probe gives an estimate of the water content. The estimate can have a small error. "
        "Thus use the trend, and do a second check before you apply water.")),
  ]})

# ---------------------------------------------------------------- 8 nerd: brain
SECTIONS.append({"id": "the-auto-waterer-brain", "kicker": "Optional: not necessary for manual irrigation", "title": "Decisions of the automatic irrigation controller",
  "blocks": [
    callout("note", "Optional section",
      p("It is not necessary to read this section unless you assemble an automatic irrigation "
        "controller. If you irrigate manually, <em>you</em> are the controller, and the other "
        "sections give sufficient information. One important instruction: do not use only one "
        "sensor. Do not apply too much water. Do not let the substrate become too dry. If you are "
        "not sure, do the safe step.")),
    p("A good controller calculates the <strong>water balance</strong> all the time. The controller "
      "adds the water from the shots of the dripper, and you know this quantity accurately. The "
      "controller subtracts the water that the plant transpires and the water that drains. The "
      "result is the quantity of water in the pot. The sensor gives one <em>estimate</em>, and the "
      "controller compares it with the water balance. The sensor is not the only source of data."),
    fig("fig-25-water-bank-account",
        "You can find the quantity of water in the pot. Add the water that you apply. Subtract the "
        "water that the plant transpires and the water that drains. Do not use only one sensor with "
        "readings that are not stable."),
    p("Each estimate has a <strong>confidence</strong>. The confidence is high when the data agree "
      "and low when the data do not agree. When the confidence is high, the controller applies a "
      "full shot. When the confidence is between high and low, it applies only a small, safe shot. "
      "When the confidence is low, the controller waits or gives the decision to a person."),
    fig("fig-26-confidence-dial",
        "Apply a full quantity of water only when the data agree. When the data do not agree, do "
        "the safe step. Apply a small shot, wait, or give the decision to a person."),
    p("The decision has only three possible results, and one safety instruction applies to all "
      "three. A sensor with an incorrect reading can only make the controller <em>more</em> "
      "careful. It cannot cause the controller to apply too much water."),
    fig("fig-27-three-branch-tree",
        "The controller can only apply a measured quantity of water, wait, or give the decision to you. One safety instruction limits all three: &lsquo;If you are not sure, select a small water deficit and not too much water. Keep the VWC always more than the recovery floor.&rsquo;"),
    p("The controller <strong>uses the same method for each substrate.</strong> The method has "
      "three steps, and it is the same for coco, rockwool, soil and water. The controller examines "
      "the data, calculates the water balance, and uses the confidence to select the correct step. "
      "The substrate changes only the numbers that the controller uses. It does not change the "
      "method."),
    callout("key", "In short",
      p("An automatic irrigation controller calculates the water balance and gives a confidence to "
        "each estimate. If the controller makes an error, the error is only in the safe direction. "
        "The safety instruction is: &lsquo;If you are not sure, select a small water deficit and "
        "not too much water. Keep the VWC always more than the recovery floor.&rsquo; The "
        "controller does this with each substrate.")),
  ]})

# ---------------------------------------------------------------- 9 one law
SECTIONS.append({"id": "one-law-any-sponge", "kicker": "All parts together", "title": "The steering law for all substrates",
  "blocks": [
    callout("tip", "The full method",
      p("One grower does one task, with or without sensors and equipment. The grower monitors the "
        "substrate, selects the correct step, applies a small quantity of water, and lets the "
        "substrate dry. The three controls are the same for each substrate. You can use the method "
        "with each of the four substrates.")),
    p("All the information in this paper is for one system. The system has four parts: the "
      "substrate, the water content, the dryback and the feed strength. The four parts operate in "
      "the four phases of each day. The probe and the automatic controller are optional. Add them "
      "only if you use automatic irrigation."),
    p("The same sawtooth of each day is correct for each substrate. Only the numbers are different:"),
    fig("fig-30-one-law-overlay",
        "The same shape of each day occurs in coco, rockwool, soil and water. Only the field "
        "capacity, the recovery floor and the feed strength of each substrate change."),
    p("During a full crop cycle, the dryback has the <strong>same shape on each substrate</strong>. "
      "In the first stage, the dryback is small and the substrate is wet. Through the middle of "
      "flowering, the dryback is larger and the substrate is drier. Near the end, the dryback "
      "becomes smaller. Vegetative mode uses small drybacks, and generative mode uses larger "
      "drybacks. The method of steering is the same."),
    fig("fig-31-whole-grow-arc",
        "In a full crop cycle, you use the same method of steering. The dryback is small in the "
        "first stage, largest in the middle of flowering, and smaller again at the end. The feed "
        "strength increases at the same time."),
    fig("fig-31b-real-plant-strip",
        "The effect of the controls on one plant, from the start to the end. The stages are the "
        "seedling, the plant with leaves, the large flowers and the ripening."),
    callout("note", "Numbers",
      ul(["Sequence from the largest buffer to the smallest buffer: living soil &rarr; coco &rarr; peat &rarr; rockwool &rarr; water",
          "Rockwool, full crop cycle: in vegetative growth, the dryback is small. In weeks 1 to 3 "
          "of flowering, the dryback is 10 to 18 points. In weeks 4 to 6, the dryback is largest, "
          "20 to 30 points, and the feed is strongest. In weeks 7 to 8, the dryback decreases to 18 "
          "to 25 points.",
          "A substrate that is wetter by a small quantity during the day can give a higher yield "
          "with the same quality in most of flowering. Control the plant with the time of the shots "
          "and the dryback, and not with a large water deficit."])),
    p("There is no one set of numbers that is correct for all rooms. Start with a substrate that "
      "has a large buffer (living soil or coco). Put a probe in the root zone. Monitor the data of "
      "the probe for one <strong>usual day</strong>. Then change one control at a time. This "
      "method, and not a number, gives the same results each time in each substrate.</p><p>For more "
      "information, read the papers about <a href='coco-crop-steering.html'>crop steering in "
      "coco</a> and <a href='rockwool-crop-steering.html'>crop steering in rockwool</a>. The paper "
      "about the <a href='root-zone-teros12.html'>root-zone sensor</a> shows how the sensor "
      "measures the substrate. The paper about <a href='smart-watering-vrwe.html'>automatic "
      "irrigation</a> gives information about the controller."),
    callout("key", "The steering law",
      p("The steering law is the same for all substrates. The substrate changes only the numbers in the steering law.")),
  ]})
