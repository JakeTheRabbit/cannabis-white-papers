# -*- coding: utf-8 -*-
"""Paper: transplanting and potting up cannabis without stalling the plant (beginner-first, operator-grade)."""
import json, os
from components import (p, lead, h, ul, ol, callout, defterm, table, figure, grid, card, chip, kv, steps)
import figs_lib as L

_FIGS = json.load(open(os.path.join(os.path.dirname(__file__), "figs_transplanting.json"), encoding="utf-8"))

SLUG = "transplanting"
TITLE = "Transplanting: how to put a plant in a larger pot without transplant shock"
EYEBROW = "Propagation · Transplant"
SUB = ("This paper shows you how to move a plant to a larger container and prevent transplant "
       "shock. Each transplant causes damage that you control. If you do the transplant at the "
       "correct time into a prepared container, the plant shows no effect. If you do the transplant "
       "after the correct time, or if your procedure is not careful, the growth of the plant stops "
       "for a week. The paper gives the correct time to move the plant, the container to use, and "
       "the procedure. The paper also gives the methods for a transplant from one medium to a "
       "different medium, the first irrigation, and the signs of transplant shock.")
META = [("seedling", "Propagation"), ("image", "9 diagrams"),
        ("quote", "13 sources"), ("clock", "~17 min to read")]
RELATED = ["cloning", "seeds-germination"]
REF_IDS = ["poorter2012-potsize", "nesmith1998-container", "uga-b1144-transplants",
           "amoroso2010-airpots", "alaguero2021-woundauxin", "rqs-rootbound",
           "bhattacharya2023-autoflower", "grodan-growguide-v2", "purdue-transplant-717",
           "umd-planting-transplants", "grossnickle2005-roots", "close2005-shock",
           "sdsu-hardening"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

# ---------------------------------------------------------------- 01 start here
SECTIONS.append({"id": "start-here", "kicker": "01 · Start here", "title": "Purpose and scope",
  "blocks": [
    lead("<strong>Transplanting</strong> (or <strong>up-potting</strong>) is the task in which you "
         "move a plant into a larger container, or into a different growing medium. Move the plant "
         "before the container or the medium starts to decrease the growth of the plant. A cannabis "
         "plant stays in containers for the full time that it is in a grow room. Thus you move most "
         "plants two or three times between the cutting and the harvest.</p><p>Each transplant "
         "causes small damage to the roots. You cause the damage because the plant can then make a "
         "root system that is larger than the previous container can hold."),
    p("If you do a transplant at the correct time into a prepared container, the transplant has "
      "almost no effect on the plant. The plant continues its growth as before. If you do the "
      "transplant after the correct time, or if your procedure is not careful, the growth of the "
      "plant stops for some days. The growth also stops if you do not prepare the container "
      "correctly. The name of this condition is <strong>transplant shock</strong>. In a room where "
      "each task has a specified date, you cannot get these days again."),
    p("This paper is for a grower who does a transplant for the first time. The paper gives a "
      "definition of each term where the term first occurs. After you read the paper, you will know "
      "the correct time to move a plant. You will know the size of the new container and the "
      "procedure for the transplant. You will also know the effect of the first irrigation, the "
      "signs of transplant shock, and the methods to prevent it."),
    callout("note", "Who this is for",
      p("This paper is for each person who moves a cutting that has roots, or a seedling, to a "
        "larger container. These persons are home growers who move plants to larger pots and "
        "operators who use a plug &rarr; block &rarr; slab system. The paper starts at the point "
        "where the papers on <a href='cloning.html'>cloning</a> and on <a "
        "href='seeds-germination.html'>seeds and germination</a> stop. At this point the plant has "
        "roots, and you can move the plant to a larger container.")),
  ]})

# ---------------------------------------------------------------- 02 vocabulary
SECTIONS.append({"id": "vocabulary", "kicker": "02 · The terms", "title": "Definitions",
  "blocks": [
    p("Transplanting has a small number of terms that are important. Make sure that you know these "
      "eight terms. The other sections of this paper use the terms many times."),
    defterm("Root ball", "The roots and the growing medium that they hold together. The root ball "
            "has the shape of the previous container. A good root ball moves out of the container "
            "in one piece and keeps its shape in your hand."),
    defterm("Root-bound (pot-bound)", "The condition in which the roots fill the container, touch "
            "the walls, and go around the wall. The roots make no branches. When this condition "
            "continues for a longer time, the plant has more problems with water. The growth of the "
            "plant also starts again more slowly after the transplant."),
    defterm("Plug / starter cube", "The small cell of rockwool, peat, or foam in which a cutting or "
            "a seed starts. The volume is usually 25&ndash;100 mL (0.85&ndash;3.4 fl oz). The plant "
            "stays in a plug for days and not for weeks."),
    defterm("Up-potting", "The task in which you move a plant from a smaller container to a larger "
            "container with the same type of medium. This task is the most frequent type of "
            "transplant."),
    defterm("Watering-in", "The first irrigation immediately after transplanting. The irrigation "
            "lets the new medium touch the root ball on all sides. It also sets the chemistry of "
            "the solution around the roots when the roots start to absorb water and nutrients again."),
    defterm("Transplant shock", "The condition of a plant after a transplant that is not careful or "
            "at the incorrect time. The signs are wilt and growth that stops for a time. In some "
            "plants, the leaves also have a yellow color. You can usually prevent transplant shock, "
            "and this paper gives the methods."),
    defterm("Rooting-in", "The days after a transplant when the roots go out of the previous root "
            "ball and fill the new medium. The transplant continues until the roots fill the new "
            "medium."),
    defterm("Air pruning", "The effect that occurs when the tip of a root goes into open air and "
            "becomes dry. The tip stops its growth, and the plant makes new roots with branches "
            "behind the tip. These roots do not go around the wall. Pots of fabric and trays with "
            "open sides use this effect."),
  ]})

# ---------------------------------------------------------------- 03 pot size science
SECTIONS.append({"id": "pot-size-science", "kicker": "03 · The data", "title": "Limits on root volume",
  "blocks": [
    p("A container is a limit on the size of the plant. A meta-analysis of 65 tests of pot size "
      "gives the average result. <strong>When the volume of the container became two times larger, "
      "the biomass of the plant increased by 43%</strong>" + _c("poorter2012-potsize") +
      ".</p><p>The cause of this effect is important. Plants in small pots did not decrease their "
      "growth only because they had no more water or feed. The plants also <em>decreased "
      "photosynthesis for each unit of leaf area</em>. The plant senses the limit on its roots and "
      "decreases its photosynthesis before you see a symptom" + _c("poorter2012-potsize") +
      "."),
    figure(L.bars("Larger pot, larger plant: average of the meta-analysis",
            [("1&times; volume", 100), ("2&times;", 143), ("4&times;", 204), ("8&times;", 292)],
            unit="", note="Biomass index. Each bar is 43% higher than the one before (average of 65 tests). The value is not the same for all plants. But there is a limit.",
            maxv=320), 1,
      "Root volume is a limit on growth. In 65 tests, the biomass was on average approximately 43% "
      "larger each time the pot volume became two times larger. The cause is that a limit on the "
      "volume of the roots decreases photosynthesis." + _c("poorter2012-potsize")),
    p("Tests for many years in horticulture show the same effect. Transplants from larger cells "
      "have thicker and shorter stems and start their growth more quickly after the transplant. "
      "They frequently give a crop after a shorter time. If the limit on the roots is very strong, "
      "the plant does not always make this growth again after the transplant" +
      _c("nesmith1998-container") + _c("uga-b1144-transplants") + ". The size of the container has "
      "a large effect on production."),
    callout("tip", "The approximate limit of 1 g/L",
      p("The same meta-analysis shows a possible limit. A plant is no longer "
        "&lsquo;unrestricted&rsquo; when the dry biomass is more than approximately <strong>1 gram "
        "for each liter of pot</strong>" + _c("poorter2012-potsize") + ". It is not necessary to "
        "weigh the plant. The limit occurs before the pot <em>looks</em> full, and a long time "
        "before roots show at the drain holes. If the plant looks too large for the pot, the pot is "
        "a limit on the plant at this time.")),
  ]})

# ---------------------------------------------------------------- 04 root physiology
SECTIONS.append({"id": "root-physiology", "kicker": "04 · The cause", "title": "Root function in containers",
  "blocks": [
    p("Roots become longer in the direction out and down until they touch an object. In a pot with "
      "smooth walls, the object is the plastic wall. The tip of the root changes direction to the "
      "side and goes along the wall around the pot. A tip that goes around the wall becomes longer "
      "and makes no branches. As a result, the root ball has a thick root mat at the wall and only "
      "a small number of roots in the middle. This structure is the opposite of the structure that "
      "you want."),
    p("Tests of different types of container for two seasons show this effect. Pots with smooth "
      "sides made the worst root structure. Air-pruning containers (with open walls or walls with "
      "holes) decreased the percentage of roots with an incorrect shape and of circling roots by a "
      "large quantity" + _c("amoroso2010-airpots") + ". When the tip of a root touches dry air and "
      "not plastic, the tip becomes dry and stops. The plant then makes small branch roots behind "
      "the tip. The volume is the same, but the root ball is much better."),
    figure(_FIGS["rootball"], 2,
      "Two root balls when you remove them from the pots. Left: a root ball that is correct for a "
      "transplant, with white tips at the edges, a medium that stays together, and no root mat. "
      "Right: a root-bound root ball. It has a root mat of circling roots at the wall and a coil at "
      "the bottom. It also has roots out of the drain holes and a shrink gap. The shrink gap lets "
      "the water of the irrigation flow down the wall, around the root ball."),
    p("The other important effect in the plant is the <strong>wound response</strong>. When you cut "
      "a root or cause damage to a root, the plant does more than decrease its root mass. The wound "
      "causes the quantity of auxin (a growth hormone) to increase in the local area. The auxin "
      "makes the gradients again. These gradients tell the tissue near the wound to make new root "
      "primordia (the first cells of new roots)" + _c("alaguero2021-woundauxin") +
      ".</p><p>Thus a root ball that you loosen carefully, or cut lightly, starts its growth again "
      "and makes branches. A root mat of circling roots that you do not touch frequently stays as a "
      "root mat in the new medium" + _c("rqs-rootbound") + ". A clean wound starts the signal for "
      "new roots. A coil that you do not cut stays as a coil."),
    callout("warn", "Circling roots cause a problem for the plant",
      p("In trees, circling roots girdle the trunk after a long time. A cannabis crop is much "
        "shorter, and the problem is different. The root mat keeps the shape of the pot for some "
        "weeks in the new container. The water of the irrigation goes around the root mat and not "
        "through it. As a result, the plant uses only a small part of the volume of the new "
        "container. The signs are a plant that wilts quickly <em>and</em> is in a wet medium.")),
  ]})

# ---------------------------------------------------------------- 05 when to up-pot
SECTIONS.append({"id": "when-to-up-pot", "kicker": "05 · Signals from the plant", "title": "Indicators for the time of a transplant",
  "blocks": [
    p("The date is the signal with the lowest accuracy. Genetics, pot size, temperature, and light "
      "change the speed at which the roots fill a container. Thus examine the pot and not the date. "
      "The list below gives the signals in an approximate sequence, with the most accurate signal "
      "first:"),
    ol(["<strong>Speed at which the plant uses water.</strong> First, the interval between "
        "irrigations is two or three days. When the roots fill the pot, the pot becomes dry in one "
        "day. The quantity of water that the plant uses increases almost in the same ratio as the "
        "root mass. This signal occurs first, and it is accurate. You do not have to touch the "
        "plant to see this signal.",
        "<strong>The root ball test.</strong> Tilt the pot and hold the stem between two fingers. "
        "Move the root ball out of the pot carefully. At the correct time, the root ball moves out "
        "in one piece, keeps its shape, and has white tips at the edges. Before the correct time, "
        "the medium does not hold together. After the correct time, the root ball has a brown root "
        "mat of circling roots" + _c("rqs-rootbound") + ".",
        "<strong>Roots at the drain holes.</strong> If you see a small number of white tips at the "
        "holes, the tips are a signal to move the plant at this time. If the roots make a <em>root "
        "mat</em> at the holes, you are after the correct time for the transplant.",
        "<strong>Canopy that is too large for the pot.</strong> Grower method: the ratio is "
        "incorrect when the height of the plant is two to three times the height of the pot. The "
        "ratio is also incorrect when the canopy is much wider than the pot. In these conditions "
        "the limit from Section 3 is near.",
        "<strong>Wilt between irrigations, with a moist medium.</strong> This symptom occurs in the "
        "last stage of a root-bound condition. The root ball cannot keep water for the plant, also "
        "when the pot contains some water" + _c("rqs-rootbound") + "."]),
    table(["Signal", "Before the correct time", "At the correct time", "After the correct time"], [
      ["Root ball test", "The medium does not hold together", "The root ball keeps its shape and has white tips at the edges", "A brown root mat of circling roots and a coil"],
      ["Drain holes", "You see no roots", "You see the first white tips", "The roots make a root mat at the holes"],
      ["Speed at which the plant uses water", "3 days or more between irrigations", "An irrigation each day", "Two irrigations each day, or the plant wilts after irrigation"],
      ["Growth of the shoots", "The size of the plant agrees with the pot", "Approximately 2&ndash;3&times; the height of the pot", "Growth stops. The leaves have less color. The plant has a nutrient deficiency."],
    ], cls="compact", caption="Examine a minimum of two signals before you move the plant. One signal can give incorrect information. If two signals agree, the information is almost always correct."),
    p("The effect of a transplant after the correct time is clear in the data on autoflower "
      "cannabis. These data are the best data on this effect, because the growth of an autoflower "
      "plant follows a time sequence that does not change. The plant does not wait for you.</p><p>A "
      "test for a hemp program in New York used a greenhouse. The growers moved seedlings from "
      "plugs of 40 mL (1.4 fl oz) into pots of approximately 11 L (3 gal) at <strong>day 8 or day "
      "15</strong>. The seedlings had the same growth as plants that started from seed in the last "
      "pot. The growers kept other seedlings in the plug until <strong>day 22</strong>. In two of "
      "three cultivars, these plants had a height at the end of approximately half the height of "
      "the other plants. They also had a smaller number of branches" + _c("bhattacharya2023-autoflower") +
      "."),
    figure(L.bars("Autoflower height and the day of the transplant",
            [("Not moved", 100), ("Moved day 8", 100), ("Moved day 15", 100), ("Moved day 22", 45)],
            unit="%", note="End height as % of plants not moved. Two of three CBD autoflower cultivars. The third: approximately 78%.",
            maxv=110), 3,
      "One week too long in a 40 mL (1.4 fl oz) plug decreased the end height to approximately half "
      "in two of three autoflower cultivars. The effect on photoperiod plants is smaller. You can "
      "make the vegetative stage longer. Then the plants can start their growth again. But the "
      "longer stage uses more time." + _c("bhattacharya2023-autoflower")),
    callout("key", "The two errors do not have equal effects",
      p("If you move the plant a short time <em>before</em> the correct time, the plant does not "
        "use a small quantity of the new medium. Also, the root ball breaks into pieces more "
        "easily. If you move the plant <em>after</em> the correct time, the plant has less "
        "photosynthesis. It also has a root mat of circling roots and a slower start of "
        "growth.</p><p>If you are not sure, move the plant. The time for the transplant starts when "
        "the root ball holds together. After circling roots start, this time does not start again.")),
  ]})

# ---------------------------------------------------------------- 06 container ladder
SECTIONS.append({"id": "container-ladder", "kicker": "06 · The sequence", "title": "Sequence of container sizes",
  "blocks": [
    p("In a grow room, cannabis typically uses a sequence of two to four containers. Each step is "
      "approximately <strong>2&ndash;4&times; the volume</strong> of the previous container. The "
      "ratio is more important than the volume in liters. The new container must have sufficient "
      "volume for some weeks of growth. The volume must not be too large, because the roots must "
      "fill the new volume quickly. The pot must also become wet and dry in a cycle that you can "
      "control."),
    figure(_FIGS["ladder"], 4,
      "A typical sequence of containers for photoperiod plants in a grow room: plug &rarr; "
      "0.5&ndash;1 L (0.13&ndash;0.26 gal) &rarr; 4&ndash;7 L (1.1&ndash;1.8 gal) &rarr; "
      "11&ndash;19 L (2.9&ndash;5.0 gal) last container. Each step is 2&ndash;4&times; the volume. "
      "Examine the roots to find the time to move the plant. Do not use a date. Autoflower plants "
      "do not use the sequence. They start in the last container, or they have one transplant in "
      "the first stage" + _c("bhattacharya2023-autoflower") + "."),
    table(["Stage", "Container", "Typical volume", "Time in the container", "Move when"], [
      ["Propagation", "Plug / cube", "25&ndash;100 mL (0.85&ndash;3.4 fl oz)", "10&ndash;14 d", "You see roots on more than one side of the plug"],
      ["First stage of vegetative growth", "First pot", "0.5&ndash;1 L (0.13&ndash;0.26 gal)", "Approximately 1&ndash;2 weeks", "The root ball moves out in one piece and has white tips"],
      ["Vegetative growth", "Middle pot", "4&ndash;7 L (1.1&ndash;1.8 gal)", "Approximately 1&ndash;2 weeks", "The pot is dry each day. You see tips at the edges."],
      ["Last stage of vegetative growth &rarr; flowering", "Last pot", "11&ndash;19 L (2.9&ndash;5.0 gal) in a grow room", "Rooting-in, then the change to the flowering stage", "No other transplant"],
    ], cls="compact", caption="The volumes are approximate grower methods for photoperiod plants in a grow room. Plants that stay outdoors for all of the season use much larger volumes. The ratios and the signals for the time of the transplant are the part that you can use in other conditions."),
    p("Water and oxygen are the causes for transplanting in steps and not in one step to the last "
      "pot. A small root ball in a very large container can use only a small part of the volume. As "
      "a result, the medium around the root ball stays wet for days. The roots must have cycles of "
      "wet and dry medium. The cycles move oxygen through the medium.</p><p>A zone of medium that "
      "is always moist around a small root ball has no oxygen. This zone is good for fungus gnats, "
      "and root disease starts in this zone. Growers use the name <strong>overpotting</strong> for "
      "a transplant of a small root ball into a container that is too large. Overpotting kills more "
      "seedlings than a container that is too small."),
    callout("note", "Fabric pots and air-pruning containers are different",
      p("In an air-pruning container, the root ball has many small roots and no circling roots" +
        _c("amoroso2010-airpots") + ". Thus a long time in one container has less effect on the "
        "plant. The transplant from the container also causes less transplant shock, because the "
        "root ball has branch tips and no root mat. These containers become dry more quickly than "
        "plastic pots. As a result, they change your irrigation and not your sequence of containers.")),
  ]})

# ---------------------------------------------------------------- 07 direct vs staged
SECTIONS.append({"id": "direct-vs-staged", "kicker": "07 · Two methods", "title": "Start in the last container or transplant in steps",
  "blocks": [
    p("Some growers do not use the sequence of containers. They start seeds or clones in the last "
      "container. This method is possible, but it has problems. The correct method changes with the "
      "type of plant and with the precision of your irrigation."),
    grid([
      card("Up-potting in stages", ul([
        "<strong>Good:</strong> you control the moisture with more precision at each stage. The "
        "roots fill each volume fully and make a root ball with a high density of roots, in layers. "
        "Small plants are easy to move, and you can put them close together below the lights. If "
        "you remove a plant, you discard a plug and not 15 L (4 gal) of medium.",
        "<strong>Problem:</strong> each transplant is work and can cause transplant shock. When you "
        "touch the plants more times, the risk of a procedure that is not careful is higher. If you "
        "transplant after the correct time, you make the root-bound problem."], "tight"),
        tag="Usual for photoperiod plants"),
      card("Start in the last pot", ul([
        "<strong>Good:</strong> the plant has no transplant in the middle of the crop. This "
        "condition is very important for autoflower plants. The time sequence of an autoflower "
        "plant does not stop to give time for new growth" + _c("bhattacharya2023-autoflower") +
        ". You also do less work for each plant, and there is no risk of a transplant after the "
        "correct time.",
        "<strong>Problem:</strong> a risk of overpotting for some weeks. The irrigation must be "
        "small shots of water at the root ball and not irrigation of the volume of the pot. Each "
        "seedling has a pot full of medium. The wet and dry cycles are slow until the roots fill "
        "the pot."], "tight"),
        tag="Usual for autoflower plants"),
    ], cols=2),
    p("Most growers use these two methods. They transplant <strong>photoperiod plants in "
      "stages</strong>, because the length of the vegetative stage can change. It is more important "
      "to control the root zone than to do less work. They start <strong>autoflower plants in the "
      "last container</strong>, or transplant them one time in the first stage, not after "
      "approximately day 15" + _c("bhattacharya2023-autoflower") + ". In rooms of commercial "
      "growers with drip irrigation, this selection is not necessary, because the media give the "
      "sequence: plug &rarr; block &rarr; slab. The next section gives more information about this "
      "sequence."),
  ]})

# ---------------------------------------------------------------- 08 procedure
SECTIONS.append({"id": "procedure", "kicker": "08 · The procedure", "title": "Transplant procedure",
  "blocks": [
    p("A transplant of one plant is a task of two minutes when you prepare all items before you "
      "start. Do the transplant in the last hours of the light period, or with a lower light "
      "intensity. The plant continuously absorbs water through its roots. It releases the water as "
      "vapor through small pores in its leaves. This movement of water is "
      "<strong>transpiration</strong>.</p><p>When the air is hotter and drier, transpiration is "
      "faster. In the last hours of the light period, transpiration is slower. As a result, the "
      "roots must supply less water at the time of the transplant, when the roots have the most "
      "damage (grower method). Before you touch a plant, prepare all items: pots full of medium, "
      "mixed solution, and clean hands or clean gloves."),
    steps([
      ("Fill the new container and make the medium wet",
       "Before the transplant, fill the new container with medium and make the medium wet with "
       "nutrient solution. Use pre-buffered coco that is fully wet, or soil that is moist and not "
       "too wet. Condition the rockwool and saturate it to its target weight. A saturated block of "
       "15 cm (6 in) must go below the surface when you put it in water. Its weight is near the "
       "minimum weight that the manufacturer gives for a saturated block" + _c("grodan-growguide-v2") +
       ". Make a hole in the medium with the size of the root ball."),
      ("Apply water to the plant 12&ndash;24 h before the transplant",
       "A moist root ball holds together. A dry root ball breaks into pieces, and a root ball that "
       "is too wet does not keep its shape. Data from commercial growers of transplants show that "
       "moisture in the root ball before the transplant decreases transplant stress" +
       _c("uga-b1144-transplants") + "."),
      ("Remove the plant by the root ball and not by the stem",
       "Put two fingers on the medium, one on each side of the stem. Turn the pot with the opening "
       "down, and push the sides of the pot or tap the edge. Let the root ball fall into your hand. "
       "Hold the root ball, or the leaves of a small seedling, and do not pull the stem" +
       _c("purdue-transplant-717") + ". The plant can make a new leaf, but damage to the stem can "
       "kill the plant."),
      ("Examine the root ball, and then change it only if necessary",
       "If the root ball is white and has many small roots, put it in the new medium quickly. Do "
       "not change a root ball that is in good condition. If the root ball has a root mat of "
       "circling roots, loosen the outer coil carefully with your fingers. Or make two or three "
       "cuts with a small depth in the root mat, from top to bottom" + _c("rqs-rootbound") +
       ". A wound on a root tip starts the signal again, and the root makes branches" +
       _c("alaguero2021-woundauxin") + ". A coil that you do not cut stays as a coil."),
      ("Set the depth: put the crown at the level of the surface",
       "Put the top of the root ball at the same level as the new surface, or 5&ndash;10 mm "
       "(0.2&ndash;0.4 in) below it. Put a thin layer of medium on the root ball. A root ball with "
       "no layer on it becomes dry, because it is a wick. Cannabis can make roots on a stem below "
       "the surface. But a soft and green stem has a risk of rot when it is deep in a wet pot. For "
       "a seedling with a long stem, put the long part below the surface and keep the collar zone "
       "dry."),
      ("Fill around the root ball and push carefully",
       "Put medium around the root ball. Push the medium only until you remove the air spaces. The "
       "roots go across a medium that touches them and not across an air space. If the roots do not "
       "touch the medium, the plant starts its growth in the new medium more slowly" +
       _c("grossnickle2005-roots") + ". But too much pressure on the medium decreases the pore "
       "space that the roots use to get oxygen. Do not push the medium with a high pressure."),
      ("Apply the first irrigation",
       "Soak the medium slowly and fully with nutrient solution. Use the same strength that the "
       "plant had before the transplant. Continue until all of the medium is wet and touches the "
       "root ball" + _c("umd-planting-transplants") + ". This irrigation does not flush the medium. "
       "Section 10 gives the numbers."),
      ("Decrease the stress on the plant",
       "VPD (vapor pressure deficit) shows how much water the air can absorb. In a hot and dry "
       "room, the leaves release more water than in a cool and moist room. For 24&ndash;48 h, keep "
       "VPD low while the roots start their growth again. Decrease the light by a small quantity, "
       "and do not do training or defoliation. Then continue your usual tasks. For most "
       "transplants, no other task is necessary.")]),
    figure(_FIGS["depth"], 5,
      "Depth is a step with one decision. A root ball that is above the surface is a wick. It "
      "becomes dry and kills the roots at the top. The correct depth is the top of the root ball at "
      "the level of the surface, with a thin layer of medium. If the crown is below the surface, "
      "the soft stem is in wet medium all the time. This condition can cause collar rot."),
  ]})

# ---------------------------------------------------------------- 09 media transitions
SECTIONS.append({"id": "media-transitions", "kicker": "09 · Media to media", "title": "Transplants between propagation media",
  "blocks": [
    p("Up-potting from soil into soil is the easy condition. Commercial growers usually move plants "
      "<em>between</em> media: rockwool plug into coco, plug into block, and block onto slab. The "
      "<strong>interface</strong> is the connection between the root ball and the new medium. The "
      "result of each of these transplants is good or not good because of the "
      "interface.</p><p>Water moves through small pores because of surface tension. This movement "
      "is <strong>capillary flow</strong>. Three conditions are necessary for capillary flow "
      "between the two media.</p><p>First, the surfaces must <em>touch</em>. Capillary flow stops "
      "fully at an air gap. Second, the new medium must have <em>sufficient water</em> on day one "
      "for the roots to go into it. Third, after day one, the new medium must be <em>drier than the "
      "root ball</em>, by a small quantity. Thus the roots go out into the new volume to find water."),
    figure(_FIGS["mediamap"], 6,
      "The figure shows each transplant between two media. Green cells are the usual procedure. "
      "Amber cells work if you control the interface and the two irrigation procedures. Red cells "
      "have two media with irrigation procedures that cannot agree."),
    h(3, "Plug &rarr; coco"),
    p("Put all of the plug below the surface of the coco. A part of the rockwool above the surface "
      "is a wick, and it makes the plug dry from the top. Before the transplant, make the coco wet "
      "with a solution for vegetative growth at full strength. Then apply small shots at short "
      "intervals at the middle of the plug, until the roots go into the coco. In the first days, "
      "keep the plug moist. The coco around the plug can have water while the plug is dry."),
    h(3, "Plug &rarr; rockwool block"),
    p("Condition the block with a solution of the same strength as the solution of the cuttings. "
      "Cuttings usually use a feed for vegetative growth with a moderate strength of approximately "
      "1.5 mS/cm at pH 5.5&ndash;6.5. Saturate the block fully. The block must go below the surface "
      "when you put it in water. Then put the plug in the hole of the block. The sides and the "
      "bottom of the plug must touch the block.</p><p>Apply the first irrigation in 24 hours or "
      "less, with the same solution" + _c("grodan-growguide-v2") + ". A plug with good roots, with "
      "roots on more than one side, fills a block in days. A weak plug cannot use the water in a "
      "block, and it has too much water."),
    h(3, "Block &rarr; slab"),
    p("This procedure is the usual method in a greenhouse. Cut the holes for the blocks in the "
      "plastic film of the slab. Condition the slab to its target. Put the block on the slab. All "
      "of its bottom must <em>touch</em> the slab. Push it down carefully" + _c("grodan-growguide-v2") +
      ".</p><p><strong>Stop the irrigation.</strong> Let the block dry for the next day or two. "
      "Then the roots go into the wetter slab below the block (rooting-in). Start the drip "
      "irrigation again only when you see roots in the slab. If you continue the drip irrigation to "
      "the block, the roots stay in the block and do not use the slab."),
    h(3, "Soil steps"),
    p("A transplant between media of the same type has the lowest risk in the figure. Examples are "
      "a transplant of seedling mix into potting soil, and a transplant of the same soil into a "
      "larger pot. Use media with the same texture. If a root ball of peat with small particles is "
      "in bark with large pieces, the water flows around the root ball. Make sure that the root "
      "ball and the medium touch each other, then apply the first irrigation" +
      _c("umd-planting-transplants") + ". All the other information in this paper applies, and no "
      "more information is necessary."),
    callout("warn", "Dry root ball in a wet medium: a problem that you cannot see",
      p("After a transplant between media, the root ball and the new medium are two different "
        "systems for water. These systems stay different until the roots connect them. The drippers "
        "make the <em>new</em> medium wet, but capillary flow across the interface is weak. As a "
        "result, the root ball becomes dry in a wet pot. The plant wilts, but your sensors show "
        "good values.</p><p>For the first days, apply water by hand on the root ball, or put a "
        "dripper on it. Continue until you see the roots go across the interface. Until then, think "
        "that the root ball is dry.")),
  ]})

# ---------------------------------------------------------------- 10 watering in
SECTIONS.append({"id": "watering-in", "kicker": "10 · First irrigation", "title": "Watering-in: initial EC and pH",
  "blocks": [
    p("The first irrigation after a transplant has two functions. <strong>Water movement:</strong> "
      "the irrigation lets the new medium touch the root ball on all sides. It closes the air gaps "
      "that stop the movement of water and the movement of roots across the interface" +
      _c("umd-planting-transplants") + ". <strong>Chemistry:</strong> the irrigation sets the "
      "solution in the root zone when the roots start again after the damage. A solution that does "
      "not change is best for roots with damage."),
    p("<strong>EC:</strong> use the same EC that the plant had before the transplant, or an EC that "
      "is lower by a small quantity. The grower method is the known feed EC minus a maximum of "
      "approximately 0.3&ndash;0.4 mS/cm. Do not use an EC that is much higher. In inert media "
      "(rockwool and coco), do not use water without nutrients for the first irrigation. This water "
      "gives no nutrients to the plant and causes a large change of the EC in the root zone. This "
      "change is the opposite of a root zone that does not change" + _c("grodan-growguide-v2") +
      ".</p><p>Vegetable growers use a <em>starter solution</em> for the first irrigation for the "
      "same cause. The starter solution has a low concentration and a high ratio of phosphorus. It "
      "gives a small quantity of nutrients that the roots can use, at the position of the root ball" +
      _c("purdue-transplant-717") + "."),
    figure(L.zones("EC of the first irrigation, compared with the known feed", -1.0, 1.0,
            [(-1.0, -0.5, L.AMBL, "too low: the root zone changes"),
             (-0.5, 0.1, L.GL, "same EC"),
             (0.1, 0.5, L.AMBL, "higher"),
             (0.5, 1.0, L.REDL, "osmotic stress")],
            unit=" mS/cm",
            note="Approximate grower method. 0 = the EC of the plant before the transplant."), 7,
      "The chemistry of the solution must not change. Apply the first irrigation at the same EC as "
      "before, or at a lower EC by a small quantity. A first irrigation with a high EC on roots "
      "with new wounds causes damage. Growers frequently think that the damage is transplant shock, "
      "but the cause is an error in the chemistry."),
    table(["New medium", "EC of the first irrigation", "pH", "Volume", "Then"], [
      ["Coco pot", "Same as the feed for vegetative growth (approximately 1.2&ndash;2.0)", "5.8&ndash;6.2", "Until the first runoff", "Small shots at short intervals at the root ball"],
      ["Rockwool block", "The same solution as the feed for the plug (typically 1.5 or more)", "5.5&ndash;6.1", "In 24 h or less after you put the plug in the block" + _c("grodan-growguide-v2"), "Then shots of approximately 3&ndash;6% of the volume of the block" + _c("grodan-growguide-v2")],
      ["Rockwool slab", "Before the transplant, set the slab to the feed EC", "5.5&ndash;6.1", "None when you put the block on the slab", "Do not apply irrigation. Let the block dry until rooting-in."],
      ["Soil / peat pot", "A feed with a low concentration, or a starter solution" + _c("purdue-transplant-717"), "6.2&ndash;6.8", "Soak the medium fully, with a small quantity of runoff", "Do not apply irrigation for 2&ndash;4 d. The roots get air."],
    ], cls="compact", caption="Targets for the first irrigation for each new medium. The EC and pH ranges are approximate grower methods, and they agree with the instructions of the manufacturers. The sequence is the important part. The solution does not change, the root ball and the medium touch, and then irrigation stops for a time."),
    callout("tip", "Soak one time, then stop",
      p("Apply the first irrigation fully, then do not touch the pot until the surface layer is "
        "dry. After transplanting, a new grower frequently makes one error. The grower applies a "
        "large quantity of water each day to a volume that the roots do not fill. This error is a "
        "type of overpotting. The irrigation causes the error. Oxygen is as necessary as water for "
        "rooting-in.")),
  ]})

# ---------------------------------------------------------------- 11 transplant shock
SECTIONS.append({"id": "transplant-shock", "kicker": "11 · The damage", "title": "Transplant shock: causes, methods to prevent it, and signs of new growth",
  "blocks": [
    p("<strong>Transplant shock</strong> is the condition in which a transplant kills a plant or "
      "stops its growth. The condition occurs a short time after the transplant. The data from "
      "forestry show that transplant shock is not one effect. Forestry has the largest quantity of "
      "data on this problem. Transplant shock is a group of stresses that cause the same symptom" +
      _c("close2005-shock") + ".</p><p>The primary stress in this group is water. A root system "
      "with damage, or a root system that is too small, cannot connect to the new medium quickly. "
      "As a result, it cannot supply the canopy with sufficient water. The plant closes its stomata "
      "to keep water in the plant. Photosynthesis and growth stop until new root growth connects "
      "the roots to the medium again" + _c("grossnickle2005-roots") + "."),
    figure(L.flow("The steps of transplant shock, and where to stop it",
            [("Root damage", "damaged root ball, root mat", L.REDL),
             ("Water limit", "supply less than transpiration", L.REDL),
             ("Stomata close", "photosynthesis decreases", L.AMBL),
             ("Growth stops", "wilt, days without growth", L.AMBL),
             ("New roots", "new tips connect the media", L.GXL),
             ("Usual growth", "turgor again, new growth", L.GL)],
            note="Each method in this paper stops the first two steps: keep the root ball in one piece, keep the surfaces wet and together, and keep transpiration low for 48 h."), 8,
      "Transplant shock is a problem of the water supply that has many different signs. Stop the "
      "sequence at the first steps. Keep the root ball in one piece, make sure that the surfaces "
      "touch, and use a climate with low stress. Then the other steps do not occur." +
      _c("grossnickle2005-roots") + _c("close2005-shock")),
    p("<strong>The causes in a grow room, with the most important cause first:</strong> damage to "
      "the root ball is the first cause. The damage occurs when your procedure is not careful or "
      "the root ball is dry. The next cause is a dry interface (a dry root ball in a wet "
      "medium).</p><p>The next cause is osmotic stress at the first irrigation. Osmotic stress "
      "occurs when the solution around the roots has a higher concentration than the water in the "
      "roots. Then the water goes from the roots to the solution, and the roots do not absorb "
      "water.</p><p>The next cause is a climate with too much stress for a root system with damage "
      "(high VPD, high light). The next cause is a cold medium. Root growth is much slower in a "
      "cold root zone, and a new transplant is only root growth. Keep the medium at approximately "
      "18&ndash;24 &deg;C (64&ndash;75 &deg;F) (grower method). The last cause is a transplant "
      "after the correct time. A root-bound plant is in a weak condition before the transplant."),
    p("<strong>To prevent transplant shock, you mostly use acclimation.</strong> Growers outdoors "
      "use 7&ndash;14 days for the acclimation of transplants. In acclimation, the plant goes to "
      "the new conditions in small steps, and the frequency of irrigation decreases. Acclimation "
      "makes the cuticles thicker and increases the carbohydrate reserves of the plant. These "
      "carbohydrate reserves supply the growth of new roots after the transplant" + _c("sdsu-hardening") +
      ".</p><p>When you move the plant in the same room, the conditions do not change and "
      "acclimation is not necessary. When the conditions in the new position are different, do the "
      "acclimation. For the first 48 h in the new position, change the light and VPD in small "
      "steps. Use the same procedure as when you move clones to the room for vegetative growth."),
    p("<strong>Signs of new growth:</strong> wilt for a small number of hours after the first "
      "irrigation is usual. Two signs show a correct transplant. The leaves have turgor again (the "
      "pressure of the water in their cells) by the start of the next light period. You see new "
      "growth at the top in 3&ndash;5 days.</p><p>If growth stops for more than 7 days, the problem "
      "is not temporary transplant shock. A cause continues to operate. Use the troubleshooting "
      "table. If the plant is very root-bound, the time is longer: growth starts again after "
      "approximately 2 weeks" + _c("rqs-rootbound") + "."),
    callout("note", "Tonics, vitamin B1, and &lsquo;transplant formulas&rsquo;",
      p("Most products for transplant shock are nutrients with a low concentration. No product in a "
        "bottle replaces these four items: a root ball in one piece and a wet interface. The other "
        "two items are a solution that does not change and 48 h with low stress. If you do these "
        "four items correctly, a tonic has no problem to correct. If you do them incorrectly, a "
        "tonic does not correct the problem.")),
  ]})

# ---------------------------------------------------------------- 12 failure modes
SECTIONS.append({"id": "failure-modes", "kicker": "12 · Types of problem", "title": "Frequent transplant problems",
  "blocks": [
    p("Six types of problem cause almost all of the damage in transplants. Make sure that you know "
      "the signs of these problems. Then you find a problem when it occurs and not after the damage."),
    grid([
      card("Overpotting", p("A small root ball in a very large volume of medium that is cold and "
        "wet. The medium does not become dry, oxygen does not move through the medium, and gnats "
        "and root rot start. <em>To correct the problem:</em> use steps with the correct size. If "
        "you start in a large pot, apply small shots of irrigation at the root ball only."), tag="Water"),
      card("Broken root ball", p("You pull a dry root ball out of the pot by the stem. The small root "
        "tips that absorb water break. The plant looks in good condition for a day. Then it wilts "
        "fully. <em>To correct the problem:</em> apply water 12&ndash;24 h before the transplant. "
        "Turn the pot with the opening down and hold the root ball" + _c("uga-b1144-transplants") +
        "."), tag="Procedure"),
      card("Dry root ball in wet medium", p("The drippers make the new medium wet. Capillary flow stops at "
        "the interface, and the root ball becomes dry. You cannot see this condition. The plant "
        "wilts in a &lsquo;wet&rsquo; pot. <em>To correct the problem:</em> apply water by hand on "
        "the root ball until the roots connect the media."), tag="Interface"),
      card("Osmotic stress", p("A medium that has a high EC before the transplant, a first feed with "
        "a high strength, or water without nutrients in an inert medium. These three give a large "
        "change of the chemistry to roots with wounds. Tipburn occurs, or the plant stops its "
        "growth. <em>To correct the problem:</em> apply the first irrigation at the EC that the "
        "plant had before the transplant" + _c("grodan-growguide-v2") + "."), tag="Chemistry"),
      card("Crown below the surface", p("A soft green stem below the surface in a wet medium rots at the "
        "collar. After some weeks, the plant falls at the surface of the medium. <em>To correct the "
        "problem:</em> put the root ball at the surface level, with a maximum of 5&ndash;10 mm "
        "(0.2&ndash;0.4 in) of medium on it. Keep the collar zone dry."), tag="Depth"),
      card("Transplant after the correct time", p("The transplant occurs three weeks after the signs. The coil goes "
        "into the new pot as a coil and stays as a coil. <em>To correct the problem:</em> move the "
        "plant when you see the signals. Loosen a root mat of circling roots, or cut it, to start "
        "the signal again and to cause branches" + _c("alaguero2021-woundauxin") + _c("rqs-rootbound") +
        "."), tag="Time"),
    ], cols=2),
  ]})

# ---------------------------------------------------------------- 13 veg schedule
SECTIONS.append({"id": "veg-schedule", "kicker": "13 · The dates", "title": "Dates of transplants in the vegetative stage",
  "blocks": [
    p("One condition is necessary for all of the dates: <strong>after each transplant, the plant "
      "must have time for rooting-in before the next stress</strong>. A stress on the plant is a "
      "change to flowering, a topping, or a change of the room. If two stresses occur in the same "
      "72 hours, the effects add to each other."),
    p("Example for a photoperiod clone with a typical vegetative stage of 4 weeks: move the plug "
      "with roots into its first pot on day 0. Move the plant to the last container at "
      "approximately day 10&ndash;14. Then start the flowering stage when the roots fill most of "
      "the last pot. Do the last up-potting <strong>7&ndash;14 days before the change to the "
      "flowering stage</strong> (grower method). Weeks 1&ndash;3 of flowering are the stretch, and "
      "in these weeks the water that the plant uses increases at the highest rate. At this time, "
      "the roots must fill the full volume of the container and not connect two media."),
    figure(L.zones("Four weeks of vegetative growth and the transplant times", 0, 28,
            [(0, 2, L.GL, "plug &rarr; first pot"),
             (2, 10, L.GXL, "roots fill"),
             (10, 14, L.GL, "&rarr; last pot"),
             (14, 26, L.GXL, "rooting-in + training"),
             (26, 28, L.AMBL, "no transplants")],
            unit=" d", note="Flowering starts at day 28 when the roots fill the last pot. For other lengths, move the times and keep the ratios."), 9,
      "Do the transplants in the first part of the vegetative stage. Keep a time for rooting-in "
      "before the change to flowering. The last 48 hours before an important change of the plant "
      "are a time without transplants."),
    ul(["<strong>Do not transplant in the flowering stage.</strong> After the change to flowering, "
        "the plant uses energy for the stretch and for bud sites. New root growth uses the same "
        "energy. In an emergency, you can do a transplant in the first days of flowering to help "
        "the plant. Do this transplant only as an emergency task, and not as a usual procedure.",
        "<strong>Keep a minimum of 3&ndash;4 days between stresses.</strong> Do the transplant, and "
        "<em>then</em> do the topping or the defoliation on a different day. One stress has a small "
        "effect. Stresses that add to each other have a large effect.",
        "<strong>For autoflower plants, all dates are close together.</strong> Their time sequence "
        "continues without you. Start the seeds in the last container, or move the plants not after "
        "approximately day 15. After that day, do not change the container" +
        _c("bhattacharya2023-autoflower") + ".",
        "<strong>Mother plants do not follow the sequence of containers.</strong> The root volume "
        "of a mother plant has a <em>small</em> limit, and this limit is necessary. The pot must "
        "have sufficient volume for good condition of the plant. But the pot must be small, to keep "
        "the plant easy to control. Cut the roots, or put the plant in a pot with new medium. Do "
        "the task in the maintenance cycle of the mother plant, and not in the cycle of the crop."]),
  ]})

# ---------------------------------------------------------------- 14 troubleshooting
SECTIONS.append({"id": "troubleshooting", "kicker": "14 · Find the cause", "title": "Troubleshooting",
  "blocks": [
    p("Use the table from the top to the bottom. The most frequent cause is first. Change one item. "
      "Wait 24 hours. Then examine the plant again."),
    table(["Symptom", "Possible cause", "To correct the problem"], [
      ["Wilt for more than 48 h, and the medium is moist", "Damage to roots, or a water supply that is less than transpiration", "Decrease VPD to approximately 0.8 kPa and decrease the light. Do not apply water until the top layer is dry. Wait for new tips."],
      ["Wilt, but the previous root ball is very dry", "Dry root ball in wet medium: the roots do not go across the interface", "Apply water by hand on the root ball. Put a dripper on the root ball until the roots go across the interface."],
      ["The plant wilts quickly <em>and</em> the pot stays wet", "The roots of the root-bound plant did not go out of the root ball", "Do the root ball test. If the root ball has a coil, loosen the root mat or cut it. At the same time, apply small shots at the root ball."],
      ["The bottom leaves have a yellow color in week one", "The plant does not have sufficient feed. The first irrigation had water without nutrients, or the medium has a weak solution.", "Apply feed at the known EC of the plant. Measure the runoff EC to make sure."],
      ["Tipburn on the leaf tips some days after the transplant", "Osmotic stress: the EC of the medium or of the first irrigation is too high", "Irrigate at a lower EC. Thus the EC of the root zone decreases in small steps."],
      ["No new growth for 7 days or more, and no wilt", "Cold root zone, or an air gap that is open", "Put the medium at 18&ndash;24 &deg;C (64&ndash;75 &deg;F). Apply water to make the surfaces touch. Make sure that the pot is not on a cold floor."],
      ["The stem is soft or brown at the surface of the medium", "Crown below the surface, or a wet collar", "Move the medium away from the collar, make the surface dry, and increase the airflow. This condition frequently kills the plant. Remove the plant if the damage goes around the stem."],
      ["The medium stays wet for 5 days or more", "Overpotting", "Stop the irrigation. Apply small shots at the root ball only. Use a higher temperature and more airflow. Wait."],
    ], cls="compact", caption="Wait one day after each correction before the next correction. For most problems after a transplant, there is one cause and not three."),
  ]})

# ---------------------------------------------------------------- 15 mental model
SECTIONS.append({"id": "mental-model", "kicker": "15 · The primary items", "title": "Primary items for a larger root zone",
  "blocks": [
    p("The new volume must be better for the roots than the previous volume, on day one. If it is "
      "not better, the roots do not go into it, and the plant stops its growth."),
    callout("key", "The four items",
      ol(["<strong>A pot is a limit.</strong> Roots with a limit on their volume decrease "
          "photosynthesis before you see a symptom. A plant that looks too large for its pot has "
          "the effect of this limit" + _c("poorter2012-potsize") + ".",
          "<strong>Move the plant on signs and not on dates.</strong> The signs are a root ball "
          "that moves out in one piece, white tips at the edge, and a pot that becomes dry more "
          "quickly. The correct time ends more quickly than it starts" +
          _c("bhattacharya2023-autoflower") + ".",
          "<strong>The interface <em>is</em> the transplant.</strong> The interface must have "
          "water, the surfaces must touch, and the chemistry must not change. All the other items "
          "are less important" + _c("grossnickle2005-roots") + ".",
          "<strong>You cause most of the transplant shock.</strong> Keep the root ball in one "
          "piece, connect the interface, use the same EC, and give 48 h with low stress. If you "
          "stop one step in the sequence, the plant shows no effect of the transplant" +
          _c("close2005-shock") + "."])),
    kv([("Step ratio", "2&ndash;4&times; the volume for each up-potting"),
        ("Last up-potting", "7&ndash;14 d before the change to the flowering stage"),
        ("First irrigation", "Known feed EC, or lower by a maximum of approximately 0.3"),
        ("Depth", "Root ball at the level of the surface, with a layer of medium of 5&ndash;10 mm (0.2&ndash;0.4 in)"),
        ("Correct transplant", "New growth at the top in 3&ndash;5 d"),
        ("Autoflower plants", "Start in the last container, or move by approximately day 15")]),
    p("Before the transplant: the papers on <a href='cloning.html'>cloning</a> and on <a "
      "href='seeds-germination.html'>seeds and germination</a> show how to make the plants that you "
      "move. After the transplant: the roots use the new volume that you give them, for the "
      "remaining time of the crop."),
  ]})
