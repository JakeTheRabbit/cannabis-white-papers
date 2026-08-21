# -*- coding: utf-8 -*-
"""Paper: transplanting and potting up cannabis without stalling the plant (beginner-first, operator-grade)."""
import json, os
from components import (p, lead, h, ul, ol, callout, defterm, table, figure, grid, card, chip, kv, steps)
import figs_lib as L

_FIGS = json.load(open(os.path.join(os.path.dirname(__file__), "figs_transplanting.json"), encoding="utf-8"))

SLUG = "transplanting"
TITLE = "Transplanting: potting up without the stall"
EYEBROW = "Propagation · Transplant"
SUB = ("Every transplant is a controlled injury: done on time, into a prepared home, the plant never "
       "notices; done late or rough, it stalls for a week. When to up-pot, the container ladder, the "
       "mechanics, media-to-media moves, the first irrigation, and transplant shock from cause to recovery.")
META = [("seedling", "Propagation"), ("image", "9 diagrams"),
        ("quote", "Evidence-linked · 13 sources"), ("clock", "~17 min read")]
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
SECTIONS.append({"id": "start-here", "kicker": "01 · Start here", "title": "What potting up is, in plain English",
  "blocks": [
    lead("<strong>Transplanting</strong> (or <strong>potting up</strong>) is moving a plant into a bigger "
         "container, or into a different growing medium, before the one it&rsquo;s in starts holding it "
         "back. Cannabis spends its whole indoor life in containers, so most plants get moved two or three "
         "times between cutting and harvest. Each move is a small, deliberate injury: you disturb the roots "
         "on purpose, so the plant can earn a bigger root system than the old pot allowed."),
    p("Done on time, into a prepared new home, a transplant costs the plant almost nothing. It "
      "keeps growing as if nothing happened. Done late, rough, or into a badly prepared pot, it costs "
      "days of stalled growth (called <strong>transplant shock</strong>), and in a room on a schedule, "
      "days are the one thing you can&rsquo;t buy back."),
    p("This guide assumes you&rsquo;ve never done it before and defines every term as it appears. By the "
      "end you&rsquo;ll know when to move a plant, what size to move it into, how to physically do it, "
      "how the first watering works, and how to read, and prevent, the stall."),
    callout("note", "Who this is for",
      p("Anyone moving a rooted cutting or seedling onward: home growers stepping up pots, and operators "
        "running plug &rarr; block &rarr; slab lines. It picks up where the "
        "<a href='cloning.html'>cloning</a> and <a href='seeds-germination.html'>seeds &amp; "
        "germination</a> guides leave off, at a plant with roots that&rsquo;s ready for a bigger home.")),
  ]})

# ---------------------------------------------------------------- 02 vocabulary
SECTIONS.append({"id": "vocabulary", "kicker": "02 · The vocabulary", "title": "Eight words that make the rest read plainly",
  "blocks": [
    p("Transplanting has less jargon than most grow topics, but the few terms it does have carry the "
      "whole logic. Learn these eight and every later section reads in plain English."),
    defterm("Root ball", "The roots plus the media they hold together, in the shape of the old "
            "container. A good root ball slides out whole and keeps its shape in your hand."),
    defterm("Root-bound (pot-bound)", "The state where roots have filled the container, hit the walls, "
            "and started circling instead of branching. The longer it runs, the worse the plant handles "
            "water and the slower it restarts after the move."),
    defterm("Plug / starter cube", "The small rockwool, peat or foam cell a cutting or seed starts in. "
            "Usually 25&ndash;100 mL, a temporary home measured in days, not weeks."),
    defterm("Up-potting", "Moving a plant from a smaller container to a larger one, same media family. "
            "The bread-and-butter transplant."),
    defterm("Watering-in", "The first irrigation immediately after transplanting. It settles the new "
            "media into contact with the root ball and sets the chemistry the roots wake up to."),
    defterm("Transplant shock", "The stall, drooping, paused growth, sometimes leaf yellowing"
            ". That follows a rough or badly timed move. Mostly preventable, which is what this "
            "paper is about."),
    defterm("Rooting-in", "The days after a move when roots grow out of the old ball and claim the new "
            "media. The transplant isn&rsquo;t finished until this is."),
    defterm("Air pruning", "What happens when a root tip grows into open air and dries off: the tip "
            "stops, and the plant branches new roots behind it instead of circling. Fabric pots and "
            "open-sided trays use this on purpose."),
  ]})

# ---------------------------------------------------------------- 03 pot size science
SECTIONS.append({"id": "pot-size-science", "kicker": "03 · The why", "title": "Why pots run out: rooting volume is a growth ceiling",
  "blocks": [
    p("A container isn&rsquo;t just a bucket that holds media. It&rsquo;s a hard limit on how big "
      "the plant&rsquo;s engine can get. A meta-analysis of 65 pot-size experiments found that, on "
      "average, <strong>doubling the container volume increased plant biomass by 43%</strong>" + _c("poorter2012-potsize") +
      ". The interesting part is the mechanism: plants in small pots didn&rsquo;t just run out of water "
      "or feed. They <em>downregulated photosynthesis per unit of leaf area</em>. The plant senses "
      "the restriction and throttles itself before you see a single symptom" + _c("poorter2012-potsize") + "."),
    figure(L.bars("Bigger pot, bigger plant: the meta-analysis average",
            [("1&times; volume", 100), ("2&times;", 143), ("4&times;", 204), ("8&times;", 292)],
            unit="", note="Indexed biomass, compounding the average +43% per doubling from 65 studies. An average tendency, not a law. But the ceiling is real.",
            maxv=320), 1,
      "Rooting volume sets a ceiling on growth. On average across 65 experiments, each doubling of pot "
      "volume bought ~43% more biomass, because restricted roots throttle photosynthesis "
      "itself." + _c("poorter2012-potsize")),
    p("Horticulture has known the practical half of this for decades: transplants raised in larger cells "
      "come out stockier, establish faster, and often crop earlier, and the growth lost to severe root "
      "restriction is not always recovered after planting out" + _c("nesmith1998-container") + _c("uga-b1144-transplants") +
      ". Container size is a real production lever, not a detail."),
    callout("tip", "The 1 g/L rule of thumb",
      p("The same meta-analysis suggests plants stop behaving &lsquo;unrestricted&rsquo; once dry biomass "
        "passes roughly <strong>1 gram per litre of pot</strong>" + _c("poorter2012-potsize") + ". You "
        "don&rsquo;t need to weigh anything. The takeaway is that the ceiling arrives well before "
        "the pot <em>looks</em> full, and long before roots show at the drain holes. If the plant looks "
        "too big for the pot, it&rsquo;s already paying rent.")),
  ]})

# ---------------------------------------------------------------- 04 root physiology
SECTIONS.append({"id": "root-physiology", "kicker": "04 · The why", "title": "What roots actually do in a container",
  "blocks": [
    p("Roots grow outward and down until they hit something. In a smooth-walled pot, &lsquo;something&rsquo; "
      "is plastic: the tip deflects sideways and keeps going, tracing the wall in circles. A circling tip "
      "keeps elongating instead of branching, so the ball develops a dense mat at the wall and stays "
      "sparse in the middle, exactly backwards from what you want."),
    p("Container research shows this plainly: in trials comparing container designs over two seasons, "
      "smooth-sided pots produced the worst root architecture, while air-pruning designs (open or "
      "perforated walls) significantly reduced the share of deformed, circling root mass" + _c("amoroso2010-airpots") +
      ". When a tip meets dry air instead of plastic, it desiccates and stops, and the plant "
      "responds by branching fine roots further back. Same volume, radically better ball."),
    figure(_FIGS["rootball"], 2,
      "Two balls at de-potting. Left: transplant-ready, white tips at the edges, media held "
      "together, no mat. Right: root-bound, a circling wall mat, a coiled base, roots out the "
      "drain holes, and a shrink gap that channels irrigation straight down the wall past the ball."),
    p("The other physiology that matters is the <strong>wound response</strong>. Cut or torn roots are "
      "not simply lost: wounding triggers local auxin (growth hormone) accumulation, which re-establishes "
      "the gradients that tell nearby tissue to build new root primordia" + _c("alaguero2021-woundauxin") +
      ". This is why a gently teased or lightly scored root ball restarts and branches, while an intact "
      "circling mat placed untouched into new media often just&hellip; keeps circling" + _c("rqs-rootbound") +
      ". A clean wound is a signal; a strangled coil is a habit."),
    callout("warn", "Circling isn&rsquo;t cosmetic",
      p("In trees, circling roots eventually girdle the trunk. Cannabis never lives that long, "
        "your cost is different: a circled mat stays pot-shaped for weeks inside the new container, "
        "irrigation channels around it instead of through it, and the plant runs on a fraction of the "
        "volume you paid for. You see it as a plant that wilts fast <em>and</em> sits in wet media.")),
  ]})

# ---------------------------------------------------------------- 05 when to up-pot
SECTIONS.append({"id": "when-to-up-pot", "kicker": "05 · Reading the plant", "title": "When to up-pot: the signs, in order of trust",
  "blocks": [
    p("The calendar is the least reliable signal you have. Genetics, pot size, temperature and light all "
      "change how fast roots fill a container, so read the pot, not the date. In rough order of trust:"),
    ol(["<strong>Drink-down speed.</strong> The pot that used to last two or three days between waterings "
        "now dries in one. Water use tracks root mass almost linearly. This is the earliest honest "
        "signal, and you notice it without touching the plant.",
        "<strong>The slide-out test.</strong> Tip the pot, support the stem between two fingers, and slide "
        "the ball out. Ready: it comes out whole, holds shape, white tips visible at the edges. Too early: "
        "media crumbles away. Late: a brown circling mat" + _c("rqs-rootbound") + ".",
        "<strong>Roots at the drain holes.</strong> A few white tips showing is a move-now signal. A mat "
        "growing <em>out</em> of the holes means you&rsquo;re already late.",
        "<strong>Canopy overshoot.</strong> Practitioner convention: when the plant stands two to three "
        "times the height of its pot, or the leaves span well past the rim, the ratio is wrong and the "
        "ceiling from Section 3 is close.",
        "<strong>Wilting between waterings despite moist media.</strong> A late-stage, root-bound "
        "symptom. The ball can no longer buffer water even when the pot has some" + _c("rqs-rootbound") + "."]),
    table(["Signal", "Too early", "Ready", "Late"], [
      ["Slide-out ball", "Media crumbles off", "Holds shape, white edge tips", "Brown mat, circling coil"],
      ["Drain holes", "Nothing visible", "First white tips", "Root mat growing out"],
      ["Drink-down", "3+ days between waterings", "Daily", "Twice daily / wilts anyway"],
      ["Top growth", "Fits the pot", "~2&ndash;3&times; pot height", "Stalled, pale, hungry"],
    ], cls="compact", caption="Read at least two signals before moving. Any single one can mislead; two agreeing rarely do."),
    p("How costly is being late? Autoflowering cannabis gives the cleanest published answer, because its "
      "fixed internal clock refuses to wait for you. In a New York hemp-program greenhouse trial, "
      "seedlings moved from 40 mL plugs into ~11 L (3-gal) pots at <strong>day 8 or day 15</strong> grew "
      "the same as plants sown directly into the final pot. Held in the plug until <strong>day 22</strong>, "
      "two of three cultivars finished at barely half the height, with fewer branches" + _c("bhattacharya2023-autoflower") + "."),
    figure(L.bars("The window closes: autoflower height vs when it left the plug",
            [("Direct sow", 100), ("Moved day 8", 100), ("Moved day 15", 100), ("Moved day 22", 45)],
            unit="%", note="Final height as % of direct-sown. Two of three CBD autoflower cultivars; the third fell to ~78%.",
            maxv=110), 3,
      "One week too long in a 40 mL plug halved final plant height in two of three autoflower cultivars. "
      "Photoperiod plants forgive more, you can extend veg to let them recover, but they pay "
      "the same class of penalty in time." + _c("bhattacharya2023-autoflower")),
    callout("key", "The asymmetry that decides everything",
      p("Moving slightly <em>early</em> costs a little media and a crumblier ball. Moving <em>late</em> "
        "costs a throttled plant, a circling mat, and a slower restart. When in doubt, move. The window "
        "opens when the ball holds together and never truly reopens once circling sets in.")),
  ]})

# ---------------------------------------------------------------- 06 container ladder
SECTIONS.append({"id": "container-ladder", "kicker": "06 · The plan", "title": "The container ladder: sizes that step, not leap",
  "blocks": [
    p("Indoor cannabis typically climbs a ladder of two to four containers, each step roughly "
      "<strong>2&ndash;4&times; the volume</strong> of the last. The exact litres matter less than the "
      "ratio: big enough that the plant gets weeks of headroom, small enough that roots claim the new "
      "volume fast and the pot still wets and dries on a manageable cycle."),
    figure(_FIGS["ladder"], 4,
      "A typical indoor photoperiod ladder: plug &rarr; 0.5&ndash;1 L &rarr; 4&ndash;7 L &rarr; "
      "11&ndash;19 L final, each step 2&ndash;4&times; the volume, moving on root readiness rather than "
      "dates. Autoflowers skip the ladder: direct to final, or one very early move" + _c("bhattacharya2023-autoflower") + "."),
    table(["Stage", "Container", "Typical volume", "Time in it", "Move when"], [
      ["Propagation", "Plug / cube", "25&ndash;100 mL", "10&ndash;14 d", "Roots show on multiple faces"],
      ["Early veg", "First pot", "0.5&ndash;1 L", "~1&ndash;2 wk", "Ball slides out whole, white tips"],
      ["Veg", "Mid pot", "4&ndash;7 L", "~1&ndash;2 wk", "Daily drink-down, edge tips"],
      ["Late veg &rarr; flower", "Final pot", "11&ndash;19 L indoor", "Root-in, then flip", "&mdash;"],
    ], cls="compact", caption="Volumes are hedged practitioner convention for indoor photoperiod plants; outdoor full-season plants run far larger. The ratios and the move-when signals are the transferable part."),
    p("Why steps instead of one leap into the final pot? Water and oxygen. A small root ball in a huge "
      "container can only drink a fraction of the volume, so the surrounding media stays wet for days. "
      "Roots need wet-dry cycling to pull oxygen through the profile; a permanently damp doughnut around "
      "a small ball is exactly the anaerobic, fungus-gnat-friendly zone where root disease starts. "
      "Growers call planting too small into too big <strong>overpotting</strong>, and it kills more "
      "seedlings than underpotting ever does."),
    callout("note", "Fabric pots and air-pots bend the rules",
      p("Air-pruning containers keep the ball fibrous instead of circling" + _c("amoroso2010-airpots") + ", "
        "which makes long stays in one size more forgiving and transplants out of them gentler, "
        "the ball is all branch-tips, no mat. They dry faster than plastic, so they shift your irrigation, "
        "not your ladder.")),
  ]})

# ---------------------------------------------------------------- 07 direct vs staged
SECTIONS.append({"id": "direct-vs-staged", "kicker": "07 · The debate", "title": "Direct-to-final vs staged: the honest trade-offs",
  "blocks": [
    p("Some growers skip the ladder entirely and start seeds or clones in the final container. "
      "It&rsquo;s a legitimate strategy with real costs, and the right answer depends on your plant type "
      "and your irrigation discipline, not on forum ideology."),
    grid([
      card("Staged up-potting", ul([
        "<strong>For:</strong> tight moisture control at every stage; roots colonise each volume fully, "
        "building a dense, layered ball; small plants stay mobile and dense under lights; culls cost a "
        "plug, not 15 L of media.",
        "<strong>Against:</strong> every move is labour and a shock opportunity; more handling means more "
        "chances to do it rough; miss a window and you&rsquo;ve built the root-bound problem yourself."], "tight"),
        tag="Photoperiod default"),
      card("Direct to final pot", ul([
        "<strong>For:</strong> zero mid-run disturbance, decisive for autoflowers, whose clock "
        "won&rsquo;t pause for recovery" + _c("bhattacharya2023-autoflower") + "; fewer labour touches per "
        "plant; no transplant windows to miss.",
        "<strong>Against:</strong> overpotting risk for weeks. Irrigation must be tiny, targeted "
        "shots at the ball, not pot-volume waterings; a whole pot of media bet on every seedling; slow "
        "wet-dry cycles until roots catch up."], "tight"),
        tag="Autoflower default"),
    ], cols=2),
    p("The verdict most rooms land on: <strong>photoperiod plants get staged</strong>, because veg length "
      "is elastic and the control is worth the labour; <strong>autoflowers go direct to final</strong> "
      "(or move once, very early, by about day 15 at the latest" + _c("bhattacharya2023-autoflower") + "). "
      "And in drip-irrigated commercial rooms the question dissolves: the ladder is built into the media "
      "itself, plug &rarr; block &rarr; slab, which is the next section."),
  ]})

# ---------------------------------------------------------------- 08 procedure
SECTIONS.append({"id": "procedure", "kicker": "08 · Do this", "title": "The transplant, step by step",
  "blocks": [
    p("The whole job takes two minutes per plant once staged. Do it late in the light period or under "
      "dimmed light. Transpiration is lower, so the plant loses less water while its roots are "
      "disturbed (practitioner convention). Have everything ready before you touch a plant: filled pots, "
      "mixed solution, clean hands or gloves."),
    steps([
      ("Pre-fill and pre-moisten the new home",
       "Fill the destination with media and wet it with nutrient solution before the plant arrives: coco "
       "pre-buffered and wet through; rockwool conditioned and saturated to its target weight (a 15 cm "
       "block should sink when dunked, and weigh in around its stated saturated minimum)" + _c("grodan-growguide-v2") + "; "
       "soil damp, not soggy. Scoop a hole the size of the incoming ball."),
      ("Water the plant 12&ndash;24 h before the move",
       "A moist ball holds together; a dry one shatters and a saturated one smears. Moistening before "
       "handling measurably reduces transplant stress in commercial transplant practice" + _c("uga-b1144-transplants") + "."),
      ("De-pot by the ball, never the stem",
       "Splay two fingers across the media either side of the stem, invert the pot, squeeze or tap the "
       "rim, and let the ball drop into your hand. Handle by the root ball (or, for small seedlings, the "
       "leaves), never pull the stem" + _c("purdue-transplant-717") + ". A leaf regrows; a crushed "
       "stem is the whole plant."),
      ("Inspect, and only then intervene",
       "White fibrous ball: plant it untouched, fast. Circling mat: gently tease the outer coil loose "
       "with your fingers, or lightly score the mat top-to-bottom in two or three places" + _c("rqs-rootbound") + ". "
       "Wounded root tips re-signal and branch" + _c("alaguero2021-woundauxin") + "; an intact coil keeps "
       "circling. Don&rsquo;t rip a healthy ball apart out of ritual."),
      ("Set the depth: crown at grade",
       "Top of the ball level with, or 5&ndash;10 mm below, the new surface, covered so it "
       "can&rsquo;t wick dry, shallow enough that the stem isn&rsquo;t sitting in wet media. Cannabis "
       "tolerates modest stem burial and can root from buried stem like its garden cousins, but deep "
       "burial of soft green stem in a wet pot trades a maybe-benefit for a real rot risk. Leggy "
       "seedlings are the exception: bury the stretch, then keep the collar zone on the dry side."),
      ("Backfill and firm, gently",
       "Fill around the ball and press just enough to close air pockets. Roots cross a contact, not a "
       "cavity. Establishment is limited by root&ndash;media contact" + _c("grossnickle2005-roots") + ". "
       "But compaction crushes the pore space they breathe through: firm like you&rsquo;re seating it, "
       "not ramming it."),
      ("Water it in",
       "A slow, thorough soak with nutrient solution at the strength the plant already knows, until the "
       "profile is wetted and the media settles onto the ball" + _c("umd-planting-transplants") + ". This "
       "is a settling drink, not a flush. Section 10 covers the numbers."),
      ("Back off",
       "Return the plant to slightly gentler conditions for 24&ndash;48 h, a touch less light, "
       "easy VPD, no training, no defoliation. Then resume. Most transplants need nothing else.")]),
    figure(_FIGS["depth"], 5,
      "Depth is a one-decision step: ball proud of the surface wicks dry and kills the top roots; ball "
      "at grade with a thin cover is right; a buried crown puts soft stem in permanently wet media and "
      "invites collar rot."),
  ]})

# ---------------------------------------------------------------- 09 media transitions
SECTIONS.append({"id": "media-transitions", "kicker": "09 · Media to media", "title": "Crossing media: plug to coco, plug to block, block to slab",
  "blocks": [
    p("Up-potting soil into soil is the easy case. Commercial cannabis mostly moves plants "
      "<em>between</em> media (rockwool plug into coco, plug into block, block onto slab) "
      "and every one of those moves lives or dies at the <strong>interface</strong>. Three rules govern "
      "it: the surfaces must <em>touch</em> (capillary flow breaks at an air gap), the destination must "
      "be <em>wet enough to accept roots</em> on day one, and after that it should run slightly "
      "<em>drier than the ball</em>, so roots chase the water out into the new volume."),
    figure(_FIGS["mediamap"], 6,
      "The transition map. Green routes are standard practice; amber works if you manage the interface "
      "and both watering regimes; red pairs two media whose irrigation needs never reconcile."),
    h(3, "Plug &rarr; coco"),
    p("Bury the plug completely, an exposed rockwool shoulder acts as a wick and dries the whole "
      "plug from the top. Pre-charge the coco with full-strength veg solution, then run small, frequent "
      "shots centred over the plug until roots strike into the coco. Keep the plug&rsquo;s own moisture "
      "up in the first days: coco around it can read &lsquo;wet&rsquo; while the plug itself has gone dry."),
    h(3, "Plug &rarr; rockwool block"),
    p("Condition the block with the same-strength solution the cuttings were already on (cuttings "
      "typically run a modest veg feed around 1.5 mS/cm at pH 5.5&ndash;6.5), saturate it fully, "
      "it should sink when dunked, then seat the plug into the hole with full side and base "
      "contact and give the first irrigation within 24 hours with that same solution" + _c("grodan-growguide-v2") + ". "
      "A well-rooted plug with roots showing on multiple faces colonises a block in days; a weak plug "
      "drowns in one."),
    h(3, "Block &rarr; slab"),
    p("The greenhouse standard. Cut the planting holes in the slab wrap, wet the slab to its conditioning "
      "target, and set the block so its base sits in <em>direct, full contact</em> with the slab face"
      ", then press down gently" + _c("grodan-growguide-v2") + ". Now the counterintuitive part: "
      "<strong>stop irrigating</strong>. Let the block dry back over the next day or two so the roots "
      "dive into the wetter slab beneath (rooting-in). Resume drip only once roots are visibly into the "
      "slab. Growers who keep dripping the block grow a plant that lives in the block and treats the "
      "slab as a doormat."),
    h(3, "Soil steps"),
    p("Same-family moves (seedling mix into potting soil, potting soil into a bigger pot) "
      "are the lowest-risk transition on the map. Match texture (a fine peat ball set into coarse bark "
      "drains past itself), firm the contact, water in" + _c("umd-planting-transplants") + ". Everything "
      "else in this paper still applies; nothing extra does."),
    callout("warn", "The island effect, the silent killer in drip rooms",
      p("After any cross-media move, the old ball and the new media are two different hydraulic systems "
        "until roots bridge them. Drippers wet the <em>new</em> media; capillarity across the interface "
        "is weak; the ball becomes a dry island in a wet pot, and the plant wilts while your "
        "sensors read perfect. Hand-water directly over the ball for the first days, or place a dripper "
        "on the ball itself, until roots have visibly crossed. Assume the island until proven bridged.")),
  ]})

# ---------------------------------------------------------------- 10 watering in
SECTIONS.append({"id": "watering-in", "kicker": "10 · First irrigation", "title": "Watering-in: the EC and pH of the first drink",
  "blocks": [
    p("The first irrigation after a transplant does two jobs. <strong>Hydraulic:</strong> it settles the "
      "new media into full contact with the ball, closing the air gaps that block both water movement and "
      "root crossing" + _c("umd-planting-transplants") + ". <strong>Chemical:</strong> it sets the "
      "root-zone solution the disturbed roots wake up to, and disturbed roots want continuity, "
      "not surprises."),
    p("<strong>EC:</strong> match what the plant was already on, or sit slightly below it, "
      "practitioner convention is the known feed EC, minus up to ~0.3&ndash;0.4 mS/cm, never a big jump "
      "up. In inert media (rockwool, coco) don&rsquo;t water-in with plain water: it starves the plant "
      "and swings the root zone, the opposite of continuity" + _c("grodan-growguide-v2") + ". Vegetable "
      "growers water-in with a dilute, phosphorus-forward <em>starter solution</em> for the same reason"
      ", a modest, root-available charge right where the ball sits" + _c("purdue-transplant-717") + "."),
    figure(L.zones("First-drink EC, relative to the feed the plant already knows", -1.0, 1.0,
            [(-1.0, -0.5, L.AMBL, "too soft: swings the root zone"),
             (-0.5, 0.1, L.GL, "match zone"),
             (0.1, 0.5, L.AMBL, "pushing it"),
             (0.5, 1.0, L.REDL, "osmotic cliff")],
            unit=" mS/cm",
            note="Hedged practitioner convention. 0 = the EC the plant was on before the move."), 7,
      "Chemical continuity: land the first irrigation at, or slightly below, the EC the plant already "
      "ran. A hot first drink into freshly wounded roots is how &lsquo;transplant shock&rsquo; gets "
      "blamed for chemistry mistakes."),
    table(["Destination", "First-drink EC", "pH", "Volume", "Then"], [
      ["Coco pot", "Match veg feed (&asymp;1.2&ndash;2.0)", "5.8&ndash;6.2", "To first runoff", "Small frequent shots at the ball"],
      ["Rockwool block", "Same solution as plug feed (&ge;1.5 typical)", "5.5&ndash;6.1", "Within 24 h of seating" + _c("grodan-growguide-v2"), "Then shots ~3&ndash;6% of block volume" + _c("grodan-growguide-v2")],
      ["Rockwool slab", "Slab pre-conditioned at feed EC", "5.5&ndash;6.1", "None at placement", "Hold irrigation; dry the block back to root-in"],
      ["Soil / peat pot", "Dilute feed or starter solution" + _c("purdue-transplant-717"), "6.2&ndash;6.8", "Thorough soak, slight runoff", "Hold 2&ndash;4 d; let it breathe"],
    ], cls="compact", caption="First-irrigation targets by destination. EC and pH bands are hedged convention aligned with manufacturer guidance; the pattern (continuity, contact, then restraint) is the load-bearing part."),
    callout("tip", "Soak once, then stop",
      p("Water-in thoroughly, then leave the pot alone until the surface layer dries. The classic "
        "beginner error after transplanting is daily heavy watering of a volume the roots haven&rsquo;t "
        "claimed. Which is overpotting by irrigation. Rooting-in needs oxygen as much as water.")),
  ]})

# ---------------------------------------------------------------- 11 transplant shock
SECTIONS.append({"id": "transplant-shock", "kicker": "11 · When it hurts", "title": "Transplant shock: causes, prevention, and reading recovery",
  "blocks": [
    p("<strong>Transplant shock</strong> is the umbrella term for death or checked growth soon after a "
      "move, and the forestry literature, which has studied it hardest, is blunt that it&rsquo;s "
      "not one thing but a family of stresses that share a symptom" + _c("close2005-shock") + ". The "
      "dominant member of the family is water: a disturbed or undersized root system can&rsquo;t couple "
      "to the new media fast enough to supply the canopy, the plant closes its stomata to survive, and "
      "photosynthesis, and growth, stall until new root growth restores the connection" + _c("grossnickle2005-roots") + "."),
    figure(L.flow("The shock cascade, and where you break it",
            [("Root loss", "shattered ball, torn mat", L.REDL),
             ("Hydraulic limit", "supply &lt; canopy demand", L.REDL),
             ("Stomata close", "photosynthesis throttles", L.AMBL),
             ("Growth stalls", "days lost, leaves droop", L.AMBL),
             ("Roots rebuild", "new tips bridge the media", L.GXL),
             ("Recovery", "turgid tops, new growth", L.GL)],
            note="Every prevention in this paper attacks the first two boxes: keep the ball intact, keep the interface wet and touching, keep demand low for 48 h."), 8,
      "Shock is a water-supply failure wearing many masks. Break the cascade at the front (intact "
      "ball, real contact, gentle climate) and the rest never happens." + _c("grossnickle2005-roots") + _c("close2005-shock")),
    p("<strong>Ranked causes in an indoor room:</strong> ball damage from rough or dry handling; a dry "
      "interface (the island effect); an osmotic cliff at watering-in; climate too aggressive for a "
      "compromised root system (high VPD, high light); cold media, root growth slows sharply in "
      "cold root zones, and a fresh transplant is nothing but root growth (keep media roughly "
      "18&ndash;24 &deg;C, practitioner convention); and simple lateness, a root-bound plant "
      "enters the move already compromised."),
    p("<strong>Prevention is mostly hardening logic.</strong> Outdoor growers spend 7&ndash;14 days "
      "acclimating transplants (graduated exposure, reduced watering frequency) which "
      "thickens cuticles and banks carbohydrate reserves that fund root regrowth after the move" + _c("sdsu-hardening") +
      ". Indoors, moving within one room, you inherit that benefit for free; recreate it whenever "
      "environments differ across the move: step light and VPD gently for the first 48 h in the new "
      "position, exactly as you would moving clones to the veg room."),
    p("<strong>Reading recovery:</strong> a few hours of soft droop after watering-in is normal. "
      "Re-tensioned leaves by next lights-on and visible new top growth within 3&ndash;5 days is a clean "
      "move. A stall past 7 days is not &lsquo;shock&rsquo; as weather. It&rsquo;s a cause still "
      "operating: go to the troubleshooting table. Badly root-bound rescues run longer, expect "
      "~2 weeks before growth resumes" + _c("rqs-rootbound") + "."),
    callout("note", "Tonics, vitamin B1, &lsquo;transplant formulas&rsquo;",
      p("Marketed shock remedies are mostly dilute nutrients plus hope. Nothing in a bottle substitutes "
        "for an intact ball, a wet touching interface, chemical continuity, and 48 easy hours. Get those "
        "four right and there&rsquo;s nothing left for a tonic to fix; get them wrong and no tonic will.")),
  ]})

# ---------------------------------------------------------------- 12 failure modes
SECTIONS.append({"id": "failure-modes", "kicker": "12 · Failure modes", "title": "The six ways transplants die",
  "blocks": [
    p("Six patterns cover nearly every transplant loss. Learn their shapes and you&rsquo;ll catch them "
      "in the act instead of in the post-mortem."),
    grid([
      card("Overpotting", p("A small ball in a huge, cold, wet volume. The media never dries, oxygen "
        "never cycles, gnats and root rot move in. <em>Fix:</em> right-size steps; if committed to a big "
        "pot, irrigate tiny and targeted at the ball only."), tag="Water"),
      card("Ball shatter", p("Dry ball pulled out by the stem; the fine root tips that do the actual "
        "drinking tear off. The plant looks fine for a day, then collapses. <em>Fix:</em> water "
        "12&ndash;24 h before, de-pot inverted, handle the ball" + _c("uga-b1144-transplants") + "."), tag="Handling"),
      card("The island effect", p("Drippers wet the new media, capillarity fails at the interface, and "
        "the old ball dries out invisibly. Plant wilts in a &lsquo;wet&rsquo; pot. <em>Fix:</em> "
        "hand-water over the ball until roots bridge."), tag="Interface"),
      card("Osmotic cliff", p("Hot pre-charged media, a strong first feed, or plain water in inert "
        "media, a chemistry jump onto wounded roots. Tips burn or the plant sulks. <em>Fix:</em> "
        "first drink at the EC the plant already knows" + _c("grodan-growguide-v2") + "."), tag="Chemistry"),
      card("Buried crown", p("Soft green stem set below grade in wet media rots at the collar, "
        "the plant tips over at the media line weeks later. <em>Fix:</em> ball at grade, "
        "5&ndash;10 mm cover max, collar zone kept on the dry side."), tag="Depth"),
      card("Root-bound denial", p("The move that happened three weeks after the signs. The coil goes "
        "into the new pot as a coil and stays one. <em>Fix:</em> move on signals; tease or score a "
        "circled mat so it re-signals and branches" + _c("alaguero2021-woundauxin") + _c("rqs-rootbound") + "."), tag="Timing"),
    ], cols=2),
  ]})

# ---------------------------------------------------------------- 13 veg schedule
SECTIONS.append({"id": "veg-schedule", "kicker": "13 · The calendar", "title": "Timing transplants against the veg schedule",
  "blocks": [
    p("One rule organises the whole calendar: <strong>every transplant needs a rooting-in buffer before "
      "the next stress event</strong>, a flip, a topping, a room move. Stack two stresses in the "
      "same 72 hours and the recoveries stack too."),
    p("For a photoperiod clone on a typical 4-week veg: up-pot the rooted plug into its first pot on "
      "day 0, move to the final container around day 10&ndash;14, and flip with the final pot "
      "substantially rooted-in. The last up-pot should land <strong>7&ndash;14 days before the flip</strong> "
      "(practitioner convention): weeks 1&ndash;3 of flower are the stretch and the steepest climb in "
      "water demand, and you want that arriving on a root system that has already claimed its full "
      "volume, not one still bridging an interface."),
    figure(L.zones("A four-week veg, with the transplant windows marked", 0, 28,
            [(0, 2, L.GL, "plug &rarr; first pot"),
             (2, 10, L.GXL, "colonise"),
             (10, 14, L.GL, "&rarr; final pot"),
             (14, 26, L.GXL, "root-in + train"),
             (26, 28, L.AMBL, "freeze: no moves")],
            unit=" d", note="Flip at day 28 with the final pot rooted-in. Slide the windows with your veg length; keep the ratios."), 9,
      "Position moves early in veg and protect a rooting-in buffer before the flip. The last 48 hours "
      "before any major event are a transplant-free zone."),
    ul(["<strong>Don&rsquo;t transplant into flower.</strong> After the flip the plant is spending on "
        "stretch and bud sites; root rebuilding competes directly. Emergency rescues in the first days "
        "of flower can work, as triage, not planning.",
        "<strong>Separate stressors by 3&ndash;4 days.</strong> Transplant, <em>then</em> top or "
        "defoliate on another day. Each recovery is cheap alone and expensive stacked.",
        "<strong>Autoflowers compress everything.</strong> Their calendar runs itself: direct-sow or "
        "move by ~day 15, and after that treat the container decision as final" + _c("bhattacharya2023-autoflower") + ".",
        "<strong>Mothers break the ladder rule.</strong> A mother plant is kept <em>slightly</em> "
        "root-restricted on purpose, big enough to stay healthy, small enough to stay manageable"
        ", refreshed by root-pruning or re-potting on its own maintenance cycle, not on the crop&rsquo;s."]),
  ]})

# ---------------------------------------------------------------- 14 troubleshooting
SECTIONS.append({"id": "troubleshooting", "kicker": "14 · Triage", "title": "Troubleshooting: symptom &rarr; cause &rarr; fix",
  "blocks": [
    p("Work the table top to bottom. It&rsquo;s ordered by how often each cause turns out to be "
      "the real one. Change one thing, give it 24 hours, reassess."),
    table(["Symptom", "Likely cause", "What to do"], [
      ["Droop &gt;48 h, media moist", "Root damage; hydraulic limit", "Ease VPD (&asymp;0.8 kPa) and light; no more water until the top layer dries; wait for new tips"],
      ["Droop, but the old ball is bone dry", "Island effect, interface never bridged", "Hand-water directly over the ball; dripper on the ball until roots cross"],
      ["Wilts fast <em>and</em> pot stays wet", "Root-bound ball never broke out", "Slide-out check; tease/score the mat if coiled; small targeted shots meanwhile"],
      ["Lower leaves yellow in week one", "Underfed, plain-water water-in or weak media charge", "Feed at the plant&rsquo;s known EC; check runoff EC to confirm"],
      ["Leaf tips burn days after the move", "Osmotic cliff, media pre-charge or first drink too hot", "Irrigate at reduced EC to pull the root zone down gradually"],
      ["No new growth 7+ d, no droop either", "Cold root zone, or a still-open air gap", "Media to 18&ndash;24 &deg;C; water to settle contact; check pot isn&rsquo;t sitting on cold floor"],
      ["Stem soft or brown at the media line", "Buried crown / wet collar", "Pull media back to expose the collar, dry the surface, increase airflow; often terminal, cull if it rings the stem"],
      ["Media stays wet 5+ days", "Overpotted", "Stop watering; tiny shots at the ball only; warmth and airflow; patience"],
    ], cls="compact", caption="Give each fix a day before layering the next. Most post-transplant problems are one cause, not three."),
  ]})

# ---------------------------------------------------------------- 15 mental model
SECTIONS.append({"id": "mental-model", "kicker": "15 · Take this with you", "title": "The mental model: sell the roots a better house",
  "blocks": [
    p("Strip the detail away and transplanting is a real-estate pitch aimed at roots: the new volume has "
      "to be easier to live in than the old one, on day one, or the plant declines the offer and stalls."),
    callout("key", "The whole game in four lines",
      ol(["<strong>Pots are ceilings.</strong> Restricted roots throttle photosynthesis before any "
          "visible symptom, a plant that looks too big for its pot is already paying" + _c("poorter2012-potsize") + ".",
          "<strong>Move on signs, not dates.</strong> Ball slides out whole, white tips at the edge, "
          "drink-down accelerating. The window closes faster than it opens" + _c("bhattacharya2023-autoflower") + ".",
          "<strong>The interface <em>is</em> the transplant.</strong> Wet, touching, chemically "
          "continuous. Everything else is furniture" + _c("grossnickle2005-roots") + ".",
          "<strong>Shock is mostly self-inflicted.</strong> Intact ball, bridged interface, matched EC, "
          "48 easy hours, break any link in the cascade and the plant never notices it moved" + _c("close2005-shock") + "."])),
    kv([("Step ratio", "2&ndash;4&times; volume per up-pot"),
        ("Last up-pot", "7&ndash;14 d before flip"),
        ("First drink", "Known feed EC, or up to ~0.3 below it"),
        ("Depth", "Ball at grade; 5&ndash;10 mm cover"),
        ("Clean recovery", "New top growth within 3&ndash;5 d"),
        ("Autoflower rule", "Direct to final, or moved by ~day 15")]),
    p("Upstream of this paper: raising the plants you&rsquo;ll move, in <a href='cloning.html'>cloning</a> "
      "and <a href='seeds-germination.html'>seeds &amp; germination</a>. Downstream: what the roots do "
      "with the volume you just sold them. Which is the rest of the grow."),
  ]})
