# -*- coding: utf-8 -*-
"""Paper: pest identification and control for cannabis (beginner)."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        stagecard, grid, card, chip, kv, steps)
import figs_lib as L

SLUG = "pest-id"
TITLE = "Pest identification and control"
EYEBROW = "Plant health · Pests"
SUB = ("This paper shows how to identify the eight pests that cause the most damage to cannabis, "
       "and how to keep their numbers small. It gives the life cycle of each pest, how to monitor "
       "it, and the biological controls and treatments that you can apply. Use it with the IPM "
       "decision procedure.")
META = [("leaf", "Plant health"), ("image", "8 figures"),
        ("quote", "8 sources"), ("clock", "~18 min to read")]
RELATED = ["ipm-sop", "airflow-design", "mould-risk", "cloning"]
REF_IDS = ["ahmed-2024-hemp-pests-florida-jipm", "pulkoski-burrack-2023-piercing-sucking-hemp",
           "cranshaw-2018-phorodon-cannabis-north-america", "cranshaw-wainwright-2020-rice-root-aphid-cannabis",
           "lopez-2023-amblyseius-swirskii-review-jipm", "vanmaanen-2010-broad-mite-swirskii-biocontrol",
           "cloyd-2015-fungus-gnat-ecology-management", "cloyd-2024-biopesticides-cannabis-oregon"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

# Fact-check jurisdiction banner
JURISDICTION_NOTE = "The biocontrol agents and the rates in this paper are examples only. Make sure that the regulations in your area let you use each agent, and that a supplier has it. If you are in NZ, examine the regulations of HSNO and MPI before you release an agent."


SECTIONS.append({"id": "intro", "kicker": "Start here", "title": "Purpose and scope",
  "blocks": [
    callout("NOTE", "Jurisdiction", JURISDICTION_NOTE),
    
    lead("This paper is for a new grower. It shows how to identify the eight groups of pests that "
         "most frequently cause damage to cannabis, and how to keep their numbers small. The groups "
         "are: spider mites, russet and broad mites, thrips, fungus gnats, aphids and root aphids, "
         "whitefly, and caterpillars.</p><p>For each pest, the paper shows how it looks, how "
         "quickly its population increases, and how to monitor it. The paper also shows how to "
         "apply a treatment to each pest, with biological controls (organisms) and with sprays."),
    p("Use this paper with the IPM SOP. The IPM SOP is a different paper with the decision "
      "procedure. It tells you <em>when</em> to apply a treatment and which treatment to use. Read "
      "this paper to identify the pests. Read the <a href='ipm-sop.html'>IPM SOP</a> to operate the "
      "program."),
    ul(["The paper names 8 pest groups. For each group, it gives the signs, the life cycle, the monitoring, the biocontrol, and the treatment",
        "The paper is for a new grower. Each term has a definition where the term first occurs",
        "Use this paper with the IPM SOP (the decision procedure). This paper is the reference for identification",
        "Prevention and detection at the start are the most important tasks, because each pest increases in number more quickly than you can spray"]),
    figure(table(["Pest", "Where it eats", "Sign of the pest", "Fastest cycle", "Primary biocontrol"], [
      ["Spider mites", "Bottom surface of the leaf", "Thin webbing and pale stippling (30x loupe)", "Approximately 3 days", "Phytoseiulus persimilis"],
      ["Russet mites and broad mites", "Growing tips", "New growth that is cupped, glossy, and twisted (60-100x necessary)", "Approximately 1 week", "Amblyseius swirskii"],
      ["Thrips", "Leaf surface", "Silver streaks and black frass dots", "Approximately 1-2 weeks", "Amblyseius cucumeris"],
      ["Fungus gnats", "Roots / wet media", "Dark flies above the medium and larvae in the soil", "Approximately 2-3 weeks", "Steinernema feltiae"],
      ["Aphids", "New growth", "Soft groups of aphids, white molted skins, and honeydew", "Approximately 1 week", "Aphidius parasitoid wasps"],
      ["Root aphids", "Crown / roots", "Yellow leaves, and you see no pest in the canopy", "Approximately 1-2 weeks", "Beneficial nematodes"],
      ["Whitefly", "Bottom surface of the leaf", "A large group of white flies in the air when you move the plant", "Approximately 2-3 weeks", "Encarsia / Eretmocerus"],
      ["Caterpillars", "Flowers / buds", "Frass and holes. They cause bud rot.", "Approximately 2-3 weeks", "Bacillus thuringiensis (Btk)"],
    ], cls="compact",
      caption="Short information on each pest. The cycle times are the fastest times in warm rooms. They become shorter when the temperature increases." + _c("ahmed-2024-hemp-pests-florida-jipm")), 1,
      "The eight pest groups, where to look, the signs to look for, and the first biocontrol agent to use."),
  ]})

SECTIONS.append({"id": "key-terms", "kicker": "Terms", "title": "Definitions",
  "blocks": [
    p("This section gives the terms that occur many times in this paper and in the IPM SOP. It is "
      "not necessary to know the terms at this time, because each term occurs again."),
    defterm("IPM (Integrated Pest Management)", "A method with layers: prevention, monitoring, "
            "biological controls, and sprays for one specified pest. IPM does not use a calendar to "
            "apply sprays."),
    defterm("Biocontrol / beneficial", "An organism that you release to eat or infect the pest. It "
            "can be a predator (for example, a predatory mite), a parasitoid wasp, or a microbe (a "
            "fungus or a bacterium)."),
    defterm("Preventative and curative", "Preventative agents are in the room before the pests come. "
            "They keep the pest population small. Curative agents decrease an outbreak that is in "
            "progress."),
    defterm("Life cycle / generation time", "The time from the egg to the adult that makes eggs. In "
            "warm, dry rooms, this time is less than one week for mites. As a result, a small area "
            "of mites becomes a problem in all the crop quickly."),
    defterm("Loupe / scope", "A hand loupe with 30x magnification shows spider mites. Russet mites "
            "and broad mites are smaller than one millimeter. 60-100x magnification is necessary to "
            "see them. Before you apply a treatment, use 60&ndash;100&times; to make sure that you "
            "identify the pest correctly. The symptoms are the same as the symptoms of heat stress "
            "(leaf curl) and tipburn."),
    defterm("Frass, honeydew, stippling", "Frass is the waste of the pest. Honeydew is a sticky "
            "liquid with sugar that sap-suckers make as waste. Stippling is the group of thin, pale "
            "marks that pests make on a leaf when they eat."),
    defterm("Action threshold", "The number of pests at which you stop to monitor and start to "
            "apply a treatment. Each facility sets the action threshold for the facility, and it is "
            "not the same for all facilities. Refer to the IPM SOP."),
    figure(L.line("Biocontrol at the start is best",
            [(0, 4), (1, 5), (2, 6), (3, 7), (4, 8), (5, 9)],
            ["wk 0", "wk 1", "wk 2", "wk 3", "wk 4", "wk 5"],
            ylab="pest count", ymax=80,
            note="Preventative curve (low, flat) and a curative treatment that starts only after the population increases quickly.",
            bands=[(0, 6, L.GL, "preventative kept low")]), 2,
      "A preventative biocontrol agent in the room at the start keeps the population low and "
      "stable. If you wait until the threshold, the population is large when you apply the "
      "treatment, and it increases quickly." + _c("lopez-2023-amblyseius-swirskii-review-jipm")),
  ]})

SECTIONS.append({"id": "sap-suckers", "kicker": "The primary pests, part 1",
  "title": "Pests that remove sap from leaves: spider mites, thrips, aphids, and whiteflies",
  "blocks": [
    p("These four pests are sap-suckers. They make holes in the cells of leaves and stems, and they "
      "remove sap. As a result, they cause the same damage: pale stippling, changes of shape, and "
      "weak growth." + _c("pulkoski-burrack-2023-piercing-sucking-hemp") + " The secondary signs of "
      "each pest are different. Use these signs to identify each pest."),
    ul(["<strong>Spider mites:</strong> stippling on the bottom of the leaf and thin webbing. In hot, dry conditions, the time from egg to adult is frequently approximately one week (in some conditions, less than two weeks). A female frequently makes approximately 100 eggs in its life. The correct times change with the temperature and the host.",
        "<strong>Thrips:</strong> silver streaks, and frass dots that are small and black. The thrips fall to the medium and become pupae there. Thus sprays on the leaves do not touch one full stage of their life.",
        "<strong>Aphids:</strong> soft groups on new growth, white molted skins, and honeydew. Black sooty mold starts on the honeydew. Adult aphids can make new aphids, and not eggs. As a result, the population increases very quickly.",
        "<strong>Whitefly:</strong> small white adults. Their shape is almost the same as the shape of a moth. When you move the plant, a large group of the adults moves into the air. The leaves become equally yellow, and the bottom of the canopy becomes weak."]),
    p("The cannabis aphid (<em>Phorodon cannabis</em>) is the aphid that is most related to "
      "cannabis. At this time, growers know it as a pest in North America." +
      _c("cranshaw-2018-phorodon-cannabis-north-america") + " The same cause applies to all four "
      "pests: the environment. Warm and dry conditions make each life cycle shorter. Thus the first "
      "method is climate control, and not the spray."),
    figure(grid([
      card("Spider mites", "Webbing and thin, pale stippling on the bottom of the leaves. Use a 30x loupe to identify the pest correctly."),
      card("Thrips", "Silver streaks with black frass dots. The pupae are in the growing medium."),
      card("Aphids", "New growth with leaf curl, groups of aphids, white molted skins, and sticky honeydew."),
      card("Whitefly", "Yellow leaves, and white flies that move into the air from the bottom of the leaf when you move the plant."),
    ], cols=2), 3,
      "Four sap-suckers, four different signs of damage. All four pests eat with the same method. "
      "Use the secondary signs to identify each pest."),
    figure(L.bars("Spider mite cycle (egg to adult) and temperature",
            [("27C / 20% RH", 3), ("21C", 7), ("10C", 19)], unit=" days",
            note="Heat and low humidity make mites increase more quickly. A warm, dry room has the fastest increase.",
            maxv=22), 4,
      "When the room is hotter and drier, the spider mite cycle is faster. The cycle is "
      "approximately 3 days in a hot, dry room and almost 3 weeks in a cold room." +
      _c("ahmed-2024-hemp-pests-florida-jipm")),
  ]})

SECTIONS.append({"id": "hidden-pests", "kicker": "The primary pests, part 2",
  "title": "Pests that you do not see: russet and broad mites, fungus gnats, root aphids, and caterpillars",
  "blocks": [
    p("This group is dangerous because the damage shows before you see the pest. Russet mites "
      "(<em>Aculops cannabicola</em>, less than 1 mm, 80-100x necessary) and broad mites "
      "(approximately 60x necessary) are too small to see without magnification. They cause cupped, "
      "glossy, or &lsquo;wet-looking&rsquo; new growth, twisted tops, and growth that stops. "
      "Growers frequently think incorrectly that these symptoms show nutrient stress or heat stress." +
      _c("vanmaanen-2010-broad-mite-swirskii-biocontrol")),
    ul(["<strong>Russet mites and broad mites:</strong> New growth that is cupped, glossy, and twisted. The mites are smaller than one millimeter, and 60-100x magnification is necessary. Growers easily think that the problem is a nutrient problem.",
        "<strong>Fungus gnats:</strong> The larvae eat root hairs in wet media. The adults are weak, dark flies above the medium. The larvae let root-rot pathogens go into the roots.",
        "<strong>Root aphids:</strong> The aphids eat at the crown and at the roots. They cause yellow leaves and growth that stops, and you see no pest in the canopy. Examine the root zone and the bottom of the pot.",
        "<strong>Caterpillars and budworms:</strong> frass and holes in the flowers. They cause bud rot quickly. Do the scouting at the end of the day, when the larvae eat."]),
    p("Fungus gnat larvae make plants weaker and cause wounds on roots. The damage and the diseases "
      "from the soil have an effect on each other. As a result, a gnat problem in wet media "
      "frequently becomes a root-rot problem." + _c("cloyd-2015-fungus-gnat-ecology-management") +
      " Tests show that cannabis is also a host of the rice root aphid. This aphid is below the "
      "ground, and scouting of the canopy does not find it." +
      _c("cranshaw-wainwright-2020-rice-root-aphid-cannabis")),
    callout("warn", "Risk of an incorrect diagnosis",
      p("<em>Before</em> you change the feed, use a loupe or scope and examine the roots. Twisted, "
        "glossy tops look the same as the symptoms of nutrient burn or heat stress. More feed does "
        "not remove mites.")),
    figure(L.zones("The position of each pest on the plant", 0, 4, [
            (3, 4, L.GL, "Growing tips: russet + broad mites"),
            (2, 3, L.GXL, "Middle canopy: (sap-suckers above)"),
            (1, 2, L.AMBL, "Flowers / buds: caterpillars"),
            (0, 1, L.BLUL, "Root zone / crown: fungus gnats + root aphids"),
          ], note="These pests are in positions where you do not usually look: in the tips, in the buds, and below the medium."), 5,
      "Examine the plant in the position of each pest. If you look only at the middle of the "
      "canopy, you do not find these four pests."),
  ]})

SECTIONS.append({"id": "monitoring", "kicker": "Find the pests at the start",
  "title": "Pest monitoring and scouting each week",
  "blocks": [
    p("You cannot keep the population of a pest small if you do not measure it. The most important "
      "method that you have is to find the pests at the start. Do a scouting walk each week on the "
      "same day. Examine the bottom of the leaves, the growing tips, the flowers, and the root "
      "zone. When the rooms become hotter, increase this to two times each week."),
    p("Hang yellow sticky cards at the height of the canopy for thrips, whitefly, and fungus gnat "
      "adults. As a start point, use a density of approximately one card for each 100 m&sup2; "
      "(approximately 1,076 ft&sup2;). More cards give a better signal. Put the cards for fungus "
      "gnats low, near the surface of the medium, where the adults move in the air. Each week, "
      "record the number on each card. Then you know the trend and not only one reading."),
    ul(["Do the scouting each week on the same day. When the temperature and the speed of the life cycle increase, examine the plants two times each week",
        "Yellow sticky cards: a minimum of approximately 1 for each 93 m&sup2; (1,000 ft&sup2;). Put the cards low at the medium for fungus gnats. Put the cards at the height of the canopy for thrips and whitefly",
        "Record the number on each card each week. A trend that increases (not one number) is the alarm",
        "Use a 30x loupe for spider mites and a 60-100x scope for russet mites and broad mites. Examine the bottom of the leaves, the tips, the flowers, and also the roots",
        "Each facility sets the action threshold for the facility. For example, one grower accepts 10-15 thrips/card/week. A different grower, with viruses in the previous crops, accepts less than 5"]),
    figure(L.line("Sticky-card trend: thrips/card",
            [(0, 2), (1, 3), (2, 4), (3, 7), (4, 11), (5, 16)],
            ["wk 1", "wk 2", "wk 3", "wk 4", "wk 5", "wk 6"],
            ylab="thrips / card", ymax=20,
            note="At week 5, thrips are more than the action threshold (10/card here). The trend told you one week before.",
            bands=[(0, 10, L.GL, "less than threshold: monitor")]), 6,
      "When you record the number each week, the sticky cards give a trend curve. The slope of the "
      "curve, and not one reading, shows when to start the IPM SOP."),
    figure(L.flow("Scouting procedure each week",
            [("Same day", "do the scouting each week"),
             ("Examine", "leaf bottom, tips, flowers, roots"),
             ("Cards", "read each card and record the number"),
             ("Compare", "this week and last week"),
             ("Select", "monitor if less than threshold. IPM SOP if more.")]), 7,
      "A scouting walk with five steps that you can do again. Do the same each time: the same day, the same plants, and the same cards, each week."),
  ]})

SECTIONS.append({"id": "controls", "kicker": "Agents to release and sprays to apply",
  "title": "Biological controls and treatments for each pest",
  "blocks": [
    p("Select the correct tool for each pest, and for preventative use or curative use. For spider "
      "mites, the specialist predator <em>Phytoseiulus persimilis</em> is the fast curative agent. "
      "But the humidity must be more than approximately 60% relative humidity (RH) for this "
      "predator. You can use <em>Neoseiulus californicus</em> or <em>Amblyseius swirskii</em> as "
      "preventative agents. For thrips, use <em>Amblyseius cucumeris</em> or swirskii at "
      "approximately 100-300 mites for each square meter. You usually see the effect after "
      "approximately 3 weeks." + _c("lopez-2023-amblyseius-swirskii-review-jipm")),
    p("For aphids, use parasitoid wasps of the correct species (<em>Aphidius colemani</em> for "
      "green peach aphid and <em>Aphidius matricariae</em> for cannabis aphid) and the fungus "
      "<em>Beauveria bassiana</em>, which kills insects. For whitefly, use <em>Encarsia</em> wasps "
      "or <em>Eretmocerus</em> wasps, and swirskii. For fungus gnats, apply a drench in the medium "
      "with <em>Steinernema feltiae</em> nematodes and the bacterium Bti, approximately each 2 "
      "weeks. For caterpillars, use <em>Bacillus thuringiensis kurstaki</em> (Btk). Btk kills only "
      "larvae that eat it. Tests on cannabis pests include some of these biopesticides." +
      _c("cloyd-2024-biopesticides-cannabis-oregon")),
    callout("warn", "No sulfur in flowering",
      p("Do not apply sulfur in flowering. It can cause residue, a bad aroma or flavor, and "
        "phytotoxicity on the buds. Predatory mites and micronized sulfur decrease the number of "
        "russet mites and broad mites.")),
    figure(table(["Pest", "Preventative", "Curative", "Microbial / spray", "Important condition"], [
      ["Spider mites", "N. californicus / swirskii", "P. persimilis", "Insecticidal soap, oils", "P. persimilis: more than 60% RH is necessary"],
      ["Russet mites and broad mites", "A. swirskii", "Predatory mites", "Micronized sulfur", "No sulfur in flowering"],
      ["Thrips", "cucumeris / swirskii (100-300/m2)", "Soil predators for pupae", "Beauveria bassiana", "Apply to the canopy and also to the medium"],
      ["Fungus gnats", "S. feltiae nematodes", "Bti drench (each approximately 2 weeks)", "Bti / Gnatrol", "Apply the treatment to the wet medium"],
      ["Aphids", "Aphidius wasps", "Use the wasp of the correct species", "Beauveria bassiana", "colemani and matricariae"],
      ["Root aphids", "Beneficial nematodes", "Soil drench", "Beauveria bassiana", "The pest is below the ground. Apply a drench to the roots"],
      ["Whitefly", "Encarsia / Eretmocerus", "Add swirskii", "Insecticidal soap", "The pest continues to occur. Start before the population increases."],
      ["Caterpillars", "Scouting and Btk at the start", "Btk spray", "Bacillus thuringiensis (Btk)", "The larva must eat it"],
    ], cls="compact",
      caption="Table to select the biocontrol agent. The rates at which you release the agents, and the conditions, are start points. Adjust them for your facility and your supplier."), 8,
      "Select the agent for the pest, and for preventative use or curative use. The time at which "
      "you release the agents is more important than the dose. Biocontrol agents increase more "
      "quickly than the pests only if you release them before the pests start."),
  ]})

SECTIONS.append({"id": "pitfalls", "kicker": "Frequent errors of growers",
  "title": "Troubleshooting",
  "blocks": [
    p("Most large pest problems have their cause in incorrect diagnosis and an incorrect time of "
      "treatment, and not in the products. The same errors occur in many facilities. A scope and a "
      "calendar prevent all of them."),
    table(["Symptom", "Usual cause", "Make sure and correct"], [
      ["Twisted, glossy new growth", "Russet mites or broad mites (not nutrients)", "Make sure of the cause at 60-100x before you change the feed"],
      ["Thrips or gnats increase again after you spray", "The spray does not touch the pupae or larvae in the soil", "Apply the treatment to the medium and also to the canopy, and not only to the leaves"],
      ["You released biocontrol agents, but the pest population continues to increase", "You released the agents after the correct time, when the pest population increased very quickly", "Release the agents before the pests come (preventative). Predators cannot increase as quickly as the pest population."],
      ["The population of P. persimilis decreases, and the pest mites stay", "The room has less than approximately 60% RH. This humidity is incorrect for the agent", "Increase the RH, or select a predator for drier air"],
      ["Residue, or a bad aroma or flavor, at harvest", "You used sulfur or strong oils in flowering", "Stop the sulfur and the strong oils before bloom starts"],
      ["The new crop has pests from the first day", "You did not do a quarantine of the clones and mother plants", "Isolate and examine each plant that comes into the facility"],
    ], cls="compact"),
    callout("note", "If a treatment has no effect",
      p("There are three possible causes. The identification of the pest is incorrect. The "
        "treatment did not touch each stage of the life cycle (the stage in the soil also). The "
        "environment is not correct for the agent. Most biocontrol that has no effect has one of "
        "these three causes.")),
    figure(L.flow("From symptom to cause to treatment",
            [("Symptom", "twisted tips, yellow leaves, silver streaks"),
             ("Think", "pest or nutrient/heat?"),
             ("Examine", "loupe/scope and root check"),
             ("Identify", "name the correct pest"),
             ("Start", "the IPM SOP. Do not spray if not sure")]), 9,
      "Do not apply a treatment if you are not sure of the cause. The step to make sure of the "
      "cause is between the symptom and the treatment. This step prevents most sprays that are not "
      "necessary."),
  ]})

SECTIONS.append({"id": "expectations", "kicker": "Good results",
  "title": "Expected results and limitations",
  "blocks": [
    p("Usually, you do not remove all the pests. You keep the pest population less than the action "
      "threshold, for a long time. Biological control is slow. You usually see the effect on thrips "
      "approximately 3 weeks after you release the agents. To stop a cycle of fungus gnats, use "
      "traps for the adults and kill the larvae. The time that is necessary is usually 4-8 weeks." +
      _c("cloyd-2015-fungus-gnat-ecology-management")),
    p("Prevention is the treatment with the lowest cost. Put each clone that comes into the "
      "facility in quarantine and examine it. Keep the mother plants clean (a mother plant with "
      "pests makes cuttings with pests). Control the humidity and the airflow. Sanitize the tools "
      "and the rooms. Do the scouting each week, and do not stop.</p><p>A facility that prevents "
      "pests and finds them at the start has much lower costs for curative agents and much less "
      "crop loss. A facility that waits for outbreaks and then applies treatments has higher costs "
      "and more crop loss."),
    callout("key", "Usual results",
      ul(["The correct result is a pest population less than the threshold, and not zero pests. Prevention gives clean crops, and sprays that you apply in an emergency do not.",
          "Biological controls are slow, but they continue for a long time. For thrips, you see the effect after approximately 3 weeks. To stop a cycle of fungus gnats, approximately 4-8 weeks are necessary.",
          "Prevention steps: put clones in quarantine, keep mother plants clean, control RH and airflow, sanitize, and do the scouting each week.",
          "A mother plant with pests always gives clones with pests. The mother room is the most important point to examine."], "tight")),
    figure(L.bars("Cost: preventative and reactive programs",
            [("Prevention: monitoring", 15), ("Prevention: biocontrol", 20),
             ("Reactive: curatives", 45), ("Reactive: crop loss", 60)], unit=" rel.",
            note="Relative cost. Prevention has a small, stable cost. A reactive program has a high cost: curative agents and crop loss.",
            maxv=70), 10,
      "The cost of prevention is stable and small. The cost of curative agents and crop loss is "
      "much larger when you wait for outbreaks and then apply treatments."),
    p("Compare your results with the thresholds in the <a href='ipm-sop.html'>IPM SOP</a>. Then you "
      "know if the program works correctly. Use good <a href='airflow-design.html'>airflow "
      "design</a>. It removes the warm areas with high humidity and no air movement where pests are."),
  ]})
