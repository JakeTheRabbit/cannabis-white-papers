# -*- coding: utf-8 -*-
"""Paper: crop steering in rockwool, the dryback and saturation mechanics nobody explains."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        stagecard, grid, card, chip, kv, steps)
import figs_lib as L
from figs import GL, GXL, AMBL, REDL, BLUL
import figs_rockwool as R

SLUG = "rockwool-crop-steering"
TITLE = "Crop steering in rockwool: water content, drybacks, and the recovery floor"
EYEBROW = "Feed · Rockwool steering"
SUB = ("The plant gets the feed that you apply in the same hour, because rockwool does not contain "
       "nutrients and has almost no buffer. Thus rockwool is the most accurate substrate to "
       "control, and it shows an error more quickly than other substrates. This paper shows how to "
       "read a water-content percentage, and how to calculate and read a dryback. It also shows the "
       "lowest water content from which the dripper can make a block wet again. It also shows how "
       "to keep the slab in the correct zone from clone to harvest without a hose.")
META = [("droplet", "Feed and steering"), ("image", "7 diagrams"),
        ("quote", "10 sources"), ("clock", "~18 min to read")]
RELATED = ["coco-crop-steering", "root-zone-teros12", "f2-crop-steering", "irrigation-manual"]
REF_IDS = ["grodan-irrigation-medicinal", "owen-norden-preferential-flow-2024",
           "hydrus-soilless-substrate-dynamics", "moon-rootzone-ec-2018",
           "nemali-2006-set-point-irrigation", "tavan-2021-sensor-irrigation-soilless",
           "caplan2019-drought", "malik2025-media",
           "netafim-irrigation-maintenance", "athena-spacing-irrigation"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

# 1 -----------------------------------------------------------------
SECTIONS.append({"id": "intro", "kicker": "Start here", "title": "Purpose and scope",
  "blocks": [
    lead("Rockwool (stone wool) is a fiber of rock. Rockwool does not contain nutrients and does "
         "not change the feed. Thus <strong>the EC of the root zone is approximately the same as "
         "the EC of the pore water (feed that the plant does not use flows out of the block as "
         "runoff or increases in concentration during the dryback)</strong>" +
         _c("grodan-irrigation-medicinal") + ".</p><p>Rockwool is the most accurate substrate to "
         "control, but it has no buffer. If the water content is incorrect, the plant shows the "
         "effect in the same hour."),
    p("This paper is only about the water and the salt in the block. Most growers feel the block "
      "with their hands to find its condition. They do not measure the water and the salt.</p><p>At "
      "the end of this paper, you will know the definition of a water-content percentage and how to "
      "calculate a dryback. You will know the minimum quantity of feed to apply. You will know the "
      "lowest water content from which the dripper can make a dry block wet again. You will also "
      "know how to keep the slab in the correct zone from clone to harvest. For this, you use "
      "sensors and an irrigation controller. You do not use a hose."),
    callout("key", "The method in short",
      p("Saturate the block. Then let the water content decrease by a controlled quantity each day "
        "(the <strong>dryback</strong>). The size and the time of the dryback are the primary "
        "controls for steering. Each day, apply sufficient feed to replace the salts in the block "
        "and to get a small quantity of runoff. Do not let the water content become less than the "
        "recovery floor (approximately <strong>25 to 30% water content</strong>). When the water "
        "content is less than this value, channeling occurs and the dripper cannot make the block "
        "wet again" + _c("owen-norden-preferential-flow-2024") + ".")),
    callout("note", "The equipment that this paper uses",
      p("This paper is for a system of slabs and cubes with pressure-compensating drippers. The "
        "system has a sensor for the moisture and EC of the substrate and an irrigation controller. "
        "A typical system has a 4&Prime; cube of the Athena type on a 3&times;6&times;36 slab" +
        _c("athena-spacing-irrigation") + ". When the dripper is smaller, you can control the root "
        "zone more accurately" + _c("athena-spacing-irrigation") + ".")),
  ]})

# 2 -----------------------------------------------------------------
SECTIONS.append({"id": "terms", "kicker": "Terms", "title": "Definitions",
  "blocks": [
    defterm("Water content (WC%)", "The percentage of the volume of the block that is water at this "
            "time. A slab at 70% WC has water in 70% of its volume. You control this one number."),
    defterm("Saturation and field capacity", "Saturation is the condition when the block is as full "
            "of water as possible, immediately after irrigation. Field capacity is the water "
            "content that stays in the block after the free water drains out. The peak of each day "
            "is approximately at field capacity."),
    defterm("Dryback", "The quantity by which the water content decreases from the peak of the day "
            "to the next trough (the lowest value). The plant uses water, and the water evaporates "
            "from the block. You measure the dryback in percentage points of WC."),
    defterm("Dryback %", "The size of the dryback. You can write it in <em>points</em> (if the peak "
            "is 75% and the trough is 55%, the dryback is 20 points) or as a <em>fraction of the "
            "peak</em>. This paper uses points. If the paper uses a fraction, it tells you."),
    defterm("Runoff (drain or leachate)", "The feed that flows out of the bottom of the block. A "
            "small quantity of runoff each day flushes the salt that collects in the block. The EC "
            "of the runoff gives you information about the EC in the block."),
    defterm("Substrate EC", "The salt strength of the water <em>in the block</em>. This EC, and not "
            "the EC of the dripper or the drain, is the EC that the plant gets" +
            _c("grodan-irrigation-medicinal") + ". It is also the EC that you use as the target for "
            "control" + _c("moon-rootzone-ec-2018") + "."),
    defterm("Recovery floor", "The lowest water content from which the dripper can make a block wet "
            "again. The block then becomes wet equally in all parts. When the water content is less "
            "than this value, channeling occurs in the fiber and the center stays dry."),
    defterm("Channeling (preferential flow)", "The condition in which water flows down through a "
            "small number of open channels and does not go to all parts of the fiber. As a result, "
            "the water flows out of the block as runoff and the center stays dry" +
            _c("owen-norden-preferential-flow-2024") + "."),
    defterm("Generative steering and vegetative steering", "A drier block and larger drybacks cause "
            "generative growth (growth of flowers and fruit). A wetter block and smaller drybacks "
            "keep the plant in vegetative growth (growth of leaves)" + _c("caplan2019-drought") +
            "."),
    defterm("Shot", "One short period of irrigation at a set time. The size of the shots and the "
            "interval between them make the water-content curve for each day."),
  ]})

# 3 -----------------------------------------------------------------
SECTIONS.append({"id": "anatomy", "kicker": "The structure of the block", "title": "Water in rockwool",
  "blocks": [
    p("A rockwool block is mostly air. Approximately 95% of its volume is space between the fibers. "
      "The fibers are a very small fraction of the volume" + _c("malik2025-media") +
      ". Water attaches to the fibers as a film and fills the smaller spaces. The larger spaces "
      "stay full of air. The water content is the quantity of this space that is water, and not "
      "air, at each time."),
    figure(R.fig_cube_anatomy(), 1,
      "The film of water on the fibers is the WC%. The air between the fibers is the oxygen for the "
      "roots. Soil particles have an electrical charge that holds dissolved nutrients and releases "
      "them slowly. Rockwool fibers have almost none of this electrical charge. This property is "
      "the cation exchange capacity (CEC). Because the CEC of rockwool is approximately zero, the "
      "dissolved salts stay in the water and the plant can use all of them" +
      _c("grodan-irrigation-medicinal") + "."),
    p("These properties have two results. First, when the plant and the air remove water from the "
      "block, the salt stays in the block. Thus the EC of the water that stays in the block "
      "increases when the block dries. Second, because rockwool has no buffer, the roots get the EC "
      "and the water content that you set. As a result, you can control rockwool accurately and an "
      "error shows quickly."),
  ]})

# 4 -----------------------------------------------------------------
SECTIONS.append({"id": "water-content", "kicker": "The number", "title": "Read the water-content percentage",
  "blocks": [
    p("In rockwool steering, each condition of the block is a position on one vertical scale. The "
      "scale shows how full of water the block is. Make sure that you know the working band and the "
      "position of the risk. After this, the only other control is the time."),
    figure(R.fig_wc_band(), 2,
      "The working band is approximately 55 to 92% WC. In the vegetative and bulking phases, the "
      "water content is high. In generative steering, the water content is lower. The dashed line "
      "near 30% is the recovery floor. When the water content is less than this value, channeling "
      "occurs in the block."),
    callout("note", "These numbers are start values",
      p("The information from Grodan shows that medicinal cultivars are very different from each "
        "other. Thus there is no one correct water content" + _c("grodan-irrigation-medicinal") +
        ". Each value in this paper is a start value. It is necessary to make sure that the value "
        "is correct for your slabs and your sensor.")),
    p("Make sure that you know the position of the headroom. The block has no problems at all "
      "values from field capacity to approximately 45% WC. The risk is only at the bottom. Thus a "
      "controlled dryback is safe, but a dryback that you do not control is very dangerous."),
  ]})

# 5 -----------------------------------------------------------------
_curve = [(0, 70), (1, 66), (2, 62), (3, 59), (4, 56), (5, 57), (6, 65),
          (7, 73), (8, 79), (9, 77), (10, 78), (11, 76), (12, 71)]
_curve_x = ["off", "", "", "", "trough", "on · P0", "P1", "", "FC", "P2", "", "P3", "off"]
SECTIONS.append({"id": "dryback", "kicker": "Dryback each day", "title": "Calculate and control the dryback",
  "blocks": [
    p("A dryback is the quantity by which the water content decreases from the peak of the day to "
      "the lowest value before the next irrigation. After irrigation, the block is full of water. "
      "Then, during the day, the plant uses water and the air removes water from the block. The "
      "<em>size</em> of the dryback and <em>when</em> you let it occur are the most important "
      "controls for the growth of the plant."),
    figure(L.line("One day for a slab", _curve, _curve_x, ylab="water content %",
            ymin=0, ymax=100,
            bands=[(55, 92, GL, "working band"), (0, 30, REDL, "below the floor")],
            note="In P3, the night dryback goes to its trough before lights-on. P0 is a short dryback at lights-on. P1 is a ramp back to field capacity. P2 keeps the water content stable with maintenance shots. The last shot starts P3."), 3,
      "The curve shows one cycle of one day. The trough is not near the floor. The peak supplies "
      "new feed to the block. The difference between the peak and the trough is the dryback."),
    callout("key", "How to calculate a dryback",
      p("Dryback in points = <strong>peak WC &minus; trough WC</strong>. If the slab has a peak of "
        "78% and decreases to 58% before the next irrigation, the dryback is <strong>20 "
        "points</strong>. As a fraction of the peak, the dryback is 20 &divide; 78 = "
        "<strong>26%</strong>. The sensor gives you the two values directly. Read the peak value "
        "after the last shot and the trough value immediately before the next shot.")),
    table(["Phase", "Usual dryback for each day", "Effect"],
      [["Propagation and the first stage of vegetative growth", "5 to 10 points", "The roots become longer and go to the water. The steering is weak."],
       ["End of vegetative growth and bulking (wet)", "10 to 15 points", "Maximum vegetative growth"],
       ["Generative steering for flowers", "20 to 30 points", "The flowers have a high density, and the stretch is slower."],
       ["During the night (in each phase)", "Add 5 to 15 points", "The root zone gets oxygen again."]],
      caption="These dryback sizes are start values. A larger dryback that starts at a time before the time in vegetative steering is more generative. A smaller dryback that starts at a time after the time in generative steering is more vegetative."),
    callout("note", "The effect of the night dryback",
      p("When the block dries during the night, air fills the spaces again. The roots and the "
        "beneficial microbes get oxygen. Tests by Grodan showed that the yield of medicinal crops "
        "increased when the usual night dryback decreased by approximately 10% (the water content "
        "was higher at night by a small quantity). The yield increased because the root zone "
        "continues to operate when the canopy does not operate" + _c("grodan-irrigation-medicinal") +
        ". Some night dryback is necessary. A night dryback that is too large is not good.")),
  ]})

# 6 -----------------------------------------------------------------
SECTIONS.append({"id": "dryout", "kicker": "The physics", "title": "How a block dries",
  "blocks": [
    p("A dryback is good when it is less than a limit. A dryback that is more than this limit is "
      "dangerous. When the dryback is larger, the plant and the air remove more water from the "
      "block. The removal of water has four different effects, one after the other."),
    figure(R.fig_dryout(), 4,
      "Stages 1 and 2 are the dryback that you want, because the block has less water and more air "
      "and oxygen. Stage 3 is a dryback that is too large, because the block has less water and the "
      "same quantity of salt, thus the EC increases. When the EC is sufficiently high, the salt "
      "concentration around a root cell is more than in the cell. Then the higher concentration "
      "pulls water out of the root and not into the root. This effect is osmotic stress" +
      _c("hydrus-soilless-substrate-dynamics") + ". In stage 4, the water content is less than the "
      "recovery floor, and water flows around a dry center through channels."),
    p("Many growers do not know about stage 3. Rockwool does not contain salt. Thus the salt in the "
      "water stays in the block when the plant and the air remove the water. When a block dries "
      "from 75% to 45% WC, it keeps only approximately three-fifths of its water (45 &divide; "
      "75).</p><p>Thus the concentration of the salt in the block increases by the inverse of this "
      "fraction. This quantity is approximately two-thirds more. The EC after drying is the EC "
      "before drying divided by the fraction of water that stays in the block" +
      _c("hydrus-soilless-substrate-dynamics") + ". A feed with an EC of 3.0 can increase to more "
      "than 5.0 EC in the root zone in the late afternoon. Thus, for a large dryback, you must "
      "apply a sufficient volume of feed and get sufficient runoff to control the salt. The section "
      "about the minimum irrigation volume gives more information."),
    callout("warn", "A part of dryback stress is salt stress",
      p("Monitor the substrate EC and not only the water content. With a generative dryback, the "
        "plant does not get water easily. The concentration of the feed in the block also "
        "increases. If the EC increases too quickly during the dryback, decrease the dryback or "
        "decrease the EC of the feed.")),
  ]})

# 7 -----------------------------------------------------------------
SECTIONS.append({"id": "breaking-point", "kicker": "Recovery floor", "title": "Threshold for a dry block",
  "blocks": [
    p("When the water content of a rockwool block is less than the recovery floor, the dripper "
      "cannot make the block wet again. A long irrigation time does not change this fact. No other "
      "fact in this paper is as important, because you can see the problem only after it occurs."),
    figure(R.fig_rewet(), 5,
      "A block in the working band becomes wet again equally in all parts. The water goes to all "
      "parts of the wet fiber. A block that is too dry has a dry center, and the fiber cannot pull "
      "water into the center. New water finds the small number of open channels. The water flows "
      "straight down through the channels and out of the block as runoff, and the center stays dry" +
      _c("owen-norden-preferential-flow-2024") + "."),
    p("When the water content is less than approximately <strong>25 to 30% WC</strong>, the dry "
      "fiber cannot pull water through the block and preferential flow occurs" +
      _c("owen-norden-preferential-flow-2024") + _c("hydrus-soilless-substrate-dynamics") +
      ". The flow rate of the dripper keeps a block that is in good condition full of water. But "
      "this flow rate cannot saturate a dry block again, because the water does not touch the dry "
      "inner part. The runoff is high and the sensor shows almost no change. These two symptoms "
      "show a block with channeling."),
    callout("danger", "If a block is too dry",
      ul(["Do not use the dripper to repair the block. More drip only causes more runoff.",
          "Soak the block manually. Apply a small volume of water slowly for a long time. You can "
          "also put the block in a small depth of feed. Continue until the center gets water again. "
          "The procedure can continue for some hours.",
          "Then use the usual irrigation times again. Find the cause of the dry block. The cause "
          "can be a dripper with a blockage or a P1 ramp that did not occur. It can also be a "
          "controller that does not operate or a dryback that is too large.",
          "If a block is at the recovery floor many times, it has permanent dry areas. The block "
          "does not become wet equally in all parts. Replace the block. Do not try to repair it."], "tight")),
    callout("key", "The method that prevents all of this",
      p("Set a minimum water content in your controller as a limit. Do not let the trough become "
        "less than this value. The dryback is for steering. The floor is a safety limit. The "
        "dryback and the floor are not the same number. Make sure that you know the two numbers for "
        "each slab.")),
  ]})

# 8 -----------------------------------------------------------------
SECTIONS.append({"id": "minimum-feed", "kicker": "Quantity", "title": "Minimum irrigation volume",
  "blocks": [
    p("When you apply feed to rockwool, two tasks are necessary. First, replace the water that the "
      "plant used. Second, flush sufficient new feed through the block. Then the salt does not "
      "collect. If the quantity of feed is too small, the EC increases and the water content "
      "decreases in the direction of the floor. If you apply too much feed, the roots are in too "
      "much water and the dryback does not occur."),
    steps([
      ("Make each shot increase the WC by a small number of points", "Make each shot increase the water content by "
       "approximately 2 to 5 points. If the shot is too small, the sensor does not show a change. "
       "If the shot is too large, the water goes directly to runoff."),
      ("Fill the block to field capacity in the P1 ramp", "After lights-on, apply some shots in sequence. "
       "Increase the water content from the lowest value of the night to field capacity. Then keep "
       "the water content at field capacity."),
      ("Get a small quantity of runoff each day", "When the block is at field capacity, make the runoff "
       "approximately 10 to 20%. Use this runoff to flush the salt that collects and to read the "
       "substrate EC" + _c("grodan-irrigation-medicinal") + "."),
      ("Use runoff EC as the feedback", "If the substrate EC or the runoff EC increases each day, "
       "you do not flush sufficiently. Increase the size or the frequency of the shots. If the EC "
       "becomes less than the target, decrease the runoff."),
      ("Keep the trough more than the floor value", "For all drybacks, the trough value before irrigation "
       "must stay more than the recovery floor, with some headroom."),
    ]),
    figure(L.bars("Where feed water goes, in each phase",
      [("Propagation", 4), ("Vegetative, wet", 14), ("Bulking", 18), ("Generative", 12)], unit="%",
      note="Approximate runoff target each day (% of the feed volume). More runoff flushes more salt. If runoff is too small, the EC increases."),
      6, "You use the runoff to control the salt and to measure the EC. Select the quantity of feed "
      "for each day. Then a controlled fraction of the feed drains."),
    callout("note", "The minimum feed is a lower limit and not a target",
      p("The minimum is the volume that keeps the water content more than the recovery floor and "
        "keeps the substrate EC at the target. In the stage with heavy flowers and high light, the "
        "minimum can be a large number of small shots. In propagation, the volume is very small. "
        "The sensor and the runoff EC give the number, and a timer does not give the number" +
        _c("nemali-2006-set-point-irrigation") + ".")),
  ]})

# 9 -----------------------------------------------------------------
SECTIONS.append({"id": "steering", "kicker": "Steering methods", "title": "Vegetative and generative steering in rockwool",
  "blocks": [
    p("You control the plant with three selections. The first selection is the position of the "
      "block in the working band. The second is the size of the dryback for each day. The third is "
      "the time when the dryback occurs. In generative steering, the block is drier, the dryback is "
      "larger, and the dryback starts at a time before the time in vegetative steering. In "
      "vegetative steering, the block is wetter, the dryback is smaller, and the dryback starts at "
      "a time after the time in generative steering" + _c("caplan2019-drought") +
      "."),
    table(["Control", "Vegetative (growth of leaves)", "Generative (flower and fruit)"],
      [["Peak WC of each day", "High, at approximately field capacity", "Lower, in the middle of the working band"],
       ["Size of the dryback", "Small, 5 to 15 points", "Large, 20 to 30 points"],
       ["First shot after lights-on", "A short interval after lights-on, and a short ramp", "A longer interval after lights-on, and a longer dryback in the night"],
       ["Substrate EC", "The lower part of the target", "Higher, because the dryback increases the concentration"],
       ["When to use", "First stage of flowering, bulking, and recovery", "Control of stretch, flower set, and ripening"]],
      caption="The same three controls (peak, dryback and time) cause the two types of growth. You do not change the feed. You change the water curve."),
    callout("note", "Apply a large quantity of feed in the first half of flowering",
      p("Tests by Grodan showed that the yield was higher when the block was always wetter during "
        "the day. The cannabinoid levels were the same. The effect occurred most in the first six "
        "of the eight weeks of flowering" + _c("grodan-irrigation-medicinal") +
        ". You can control generative growth with the time and the size of the dryback. But a "
        "quantity of water and feed that is too small is not good for the plant while it continues "
        "to make the crop.")),
  ]})

# 10 -----------------------------------------------------------------
_season = [(0, 8), (1, 10), (2, 12), (3, 15), (4, 20), (5, 24), (6, 26), (7, 22)]
_season_x = ["Clone", "Vegetative", "Week 1", "Week 2", "Week 3", "Week 4-5", "Week 6", "Week 7-8"]
SECTIONS.append({"id": "maintain", "kicker": "From start to end", "title": "Keep rockwool saturated",
  "blocks": [
    p("The controller keeps the block in the correct zone from clone to harvest, and you do not "
      "touch a hose. The runoff of each day flushes the salt. Thus it is not necessary to flush the "
      "block manually or to add water to a dry cube. Set the values of water content and dryback "
      "for each stage of the crop before the crop starts."),
    figure(L.line("The dryback increases during the crop", _season, _season_x, ylab="target dryback (points)",
            ymin=0, ymax=35,
            note="In the first stage, drybacks are small. After flower set, they are larger and more generative. At the end, they decrease by a small quantity."),
      7, "The curve of the dryback is approximate. At first, keep the block wet and the steering "
      "weak, to make the plant larger. After flower set, make the block drier and the steering more "
      "generative. Then keep the dryback stable for ripening" + _c("grodan-irrigation-medicinal") +
      "."),
    table(["Stage", "Peak WC of each day", "Dryback", "Substrate EC", "Runoff"],
      [["Clone and propagation", "High, with weak steering", "5 to 10 points", "Use a start value that is higher than you think is correct", "Very small"],
       ["Vegetative stage", "High", "10 to 15 points", "Increase", "Low, 5 to 10%"],
       ["Weeks 1 to 3 of flowering", "High (wet, bulking)", "10 to 18 points", "Increase again", "10 to 15%"],
       ["Weeks 4 to 6 of flowering", "In the middle of the working band", "20 to 30 points", "Highest", "15 to 20%, to flush the salt"],
       ["Weeks 7 to 8 of flowering", "In the middle of the working band, stable", "18 to 25 points", "Decrease by a small quantity, or use the value that you set before", "Keep the same value"]],
      caption="The table shows the curve for all stages. The EC increases in each stage, because rockwool is an inert substrate and the plant uses more feed when the light increases" + _c("grodan-irrigation-medicinal") + ". The runoff increases to flush the larger quantity of salt."),
    callout("key", "You do not flush the block manually",
      p("A controlled runoff each day continuously replaces the water in the block that has a high "
        "salt concentration with new feed. Thus the EC does not increase to a value at which it is "
        "necessary to flush the block manually. Because the trough does not become less than the "
        "recovery floor, no cube becomes very dry. Thus it is not necessary to soak a cube "
        "manually. The system keeps the water and the salt in balance each day, if the limits that "
        "you set are correct.")),
  ]})

# 11 -----------------------------------------------------------------
SECTIONS.append({"id": "systems", "kicker": "The equipment", "title": "Systems with sensors for crop steering",
  "blocks": [
    p("You cannot use only a timer for this method. To control rockwool, measure the block and let "
      "the controller use the measurement. The result is a closed loop" +
      _c("nemali-2006-set-point-irrigation") + _c("tavan-2021-sensor-irrigation-soilless") +
      "."),
    ul([
      "<strong>Measure in the block.</strong> A substrate sensor reads the water content and the EC "
      "where the roots are. Use the substrate EC as the target for control. Do not use the EC of "
      "the dripper or the drain" + _c("grodan-irrigation-medicinal") + _c("moon-rootzone-ec-2018") +
      ".",
      "<strong>Let the controller keep the curve.</strong> The irrigation controller operates the "
      "P1 ramp to field capacity, the P2 maintenance shots, and the P0 and P3 dryback periods "
      "automatically. It uses water-content setpoints and not a timer" +
      _c("nemali-2006-set-point-irrigation") + ".",
      "<strong>Set the safety floor in the software.</strong> The safety floor is a minimum water "
      "content. The controller always irrigates to keep the water content more than this minimum. "
      "Thus channeling cannot occur in the block, also when the dryback that you set is too large.",
      "<strong>Monitor the runoff EC each day.</strong> It shows when the salt starts to collect "
      "and when you flush too much.",
    ]),
    p("The related papers give more information about the equipment and the cycle of each day. They "
      "show the values that the substrate sensor measures and how the controller makes a decision. "
      "They also show the P0 to P3 cycle and how to install and operate the system."),
    callout("note", "Accuracy and automation",
      p("Rockwool has no buffer. Thus a closed-loop controller can control rockwool with a smaller "
        "tolerance than each substrate that has a buffer" + _c("grodan-irrigation-medicinal") +
        ". Rockwool is an inert substrate, and thus it shows each error. But this property also "
        "makes rockwool the best substrate for automation.")),
  ]})

# 12 -----------------------------------------------------------------
SECTIONS.append({"id": "troubleshooting", "kicker": "When a problem occurs", "title": "Troubleshooting",
  "blocks": [
    table(["Symptom", "Possible cause", "Correction"],
      [["The runoff is high and the sensor shows almost no change", "Channeling occurs in the block, and the center is too dry", "Soak the block manually to make it wet again. Then increase the value of the floor and do a check of the drippers."],
       ["The substrate EC increases each day", "The runoff is not sufficient and the salt collects", "Use larger shots or more frequent shots to increase the runoff of each day"],
       ["The substrate EC becomes less than the target", "You flush too much, and the runoff is too large", "Decrease the size or the frequency of the shots"],
       ["The WC stays less than field capacity", "The shots are too small, a dripper has a blockage, or P1 is too short", "Do a check of the drippers. Make the P1 ramp longer" + _c("netafim-irrigation-maintenance")],
       ["The dryback is much larger than the value that you set", "The plant uses water at a high rate in high light, or a shot did not occur", "Add P2 shots. Do a check of the controller and the sensor"],
       ["The slabs are not the same across the room", "The flow or the position of the drippers is different", "Flush the tubing and do a check of it" + _c("netafim-irrigation-maintenance") + ". Use the correct number of drippers for each slab" + _c("athena-spacing-irrigation")]],
      caption="Most problems with rockwool are a drift of the water content or of the EC from the set value. The sensor shows which reading drifts. Then you know the correction."),
  ]})

# 13 -----------------------------------------------------------------
SECTIONS.append({"id": "quick-reference", "kicker": "The numbers", "title": "Reference targets",
  "blocks": [
    kv([("Working band", "approximately 55 to 92% WC"),
        ("Recovery floor (minimum limit)", "approximately 25 to 30% WC"),
        ("Shot size", "The WC increases by approximately 2 to 5 points"),
        ("Runoff for each day", "approximately 10 to 20% at field capacity"),
        ("Vegetative dryback", "5 to 15 points"),
        ("Generative dryback", "20 to 30 points"),
        ("EC for each stage", "increases from propagation to vegetative growth and then to the flowering stage"),
        ("Target for control of the EC", "the substrate reading and not the drain reading")]),
    callout("key", "The method in five steps",
      ul(["Each morning, saturate the block to field capacity with a P1 ramp.",
          "During the day, keep the block at field capacity with P2 maintenance shots and a small runoff.",
          "Let the dryback that you set occur. Set its size for the quantity of generative steering that you want.",
          "Do not let the trough become less than the recovery floor.",
          "Use the substrate EC and the water content as the targets for control. The sensor gives the values and the controller does the control."], "tight")),
  ]})
