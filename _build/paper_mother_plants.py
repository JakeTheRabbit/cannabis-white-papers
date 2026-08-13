# -*- coding: utf-8 -*-
"""Paper: mother plants & stock-plant management — running a cutting factory that never runs dry."""
import json, os
from components import (p, lead, h, ul, ol, callout, defterm, table, figure, grid, card, chip, kv, steps)
import figs_lib as L

_FIGS = json.load(open(os.path.join(os.path.dirname(__file__), "figs_mother_plants.json"), encoding="utf-8"))

SLUG = "mother-plants"
TITLE = "Mother plants: stock management that never runs dry"
EYEBROW = "Propagation · Stock"
SUB = ("How to keep cannabis mother plants healthy for the long haul — room setup, feeding, pruning "
       "architecture, viroid defence, testing rotation and succession — so every batch starts from a "
       "plant you can actually trust.")
META = [("seedling", "Propagation"), ("image", "13 diagrams"),
        ("quote", "Evidence-linked · 14 sources"), ("clock", "~20 min read")]
RELATED = ["cloning", "tissue-culture"]
REF_IDS = ["mp-ahrens-2023-photoperiod", "mp-saloner-2020-nitrogen", "mp-tumi-hlvd-testing",
           "mp-moher-2022-veg-light", "mp-druege-2004-stockplant-n", "mp-caplan-2018-cuttings",
           "mp-adamek-2022-mosaicism", "mp-adamek-2024-subcultures", "mp-punja-2025-hplvd-mgmt",
           "mp-warren-2019-hplvd-ca", "mp-adkar-2023-hidden-threat", "mp-medgen-hlvd",
           "mp-monthony-2021-tc", "mp-kurtz-2022-retip"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

# ---------------------------------------------------------------- 01 start here
SECTIONS.append({"id": "start-here", "kicker": "01 · Start here",
  "title": "What a mother plant is and why it runs the whole grow",
  "blocks": [
    lead("A <strong>mother plant</strong> is a plant you keep permanently in leafy growth and never "
         "flower. Her only job is to supply <strong>cuttings</strong> — genetically identical copies — "
         "on schedule. Every plant that ever reaches your flower room started as a piece of her."),
    p("The formal horticulture word is <strong>stock plant</strong>; growers say mother. Either way, "
      "the deal is the same: you hold one plant back from production and spend light, space and labour "
      "on her, and in exchange every batch starts uniform, known and on time. She is the factory, and "
      "the flower rooms are the shop that sells what the factory makes."),
    p("That position — upstream of everything — is why mother management is worth doing properly. A "
      "weak, sick or mislabeled mother doesn't cost you one plant. It costs you every cutting she "
      "produces, and you usually find out weeks or months later, after the problem has been multiplied "
      "across a whole room. Mother problems are the compound interest of growing: small, quiet, and "
      "ruinous by the time they're visible."),
    figure(L.flow("From mother bank to sale-able flower",
            [("Mother bank", "tested, kept vegetative"), ("Cut", "a batch every 2–3 weeks"),
             ("Root", "10–14 days"), ("Veg", "2–4 weeks"), ("Flower", "the room that pays")]), 1,
      "The propagation engine. Everything downstream inherits whatever the mother carries — vigour, "
      "genetics, and any pathogen she has quietly picked up."),
    callout("note", "Who this is for",
      p("Anyone keeping their first mother, through to operators running a stock room against a "
        "production calendar. This paper is about the plant you cut <em>from</em>. The cutting "
        "technique itself — blades, gel, domes, humidity — is covered in the "
        "<a href='cloning.html'>cloning guide</a>; keeping the room clean is the "
        "<a href='ipm-sop.html'>IPM hygiene</a> guide.")),
  ]})

# ---------------------------------------------------------------- 02 core answer
SECTIONS.append({"id": "core-answer", "kicker": "02 · The short version",
  "title": "The whole job on one page",
  "blocks": [
    lead("If you only read one section, read this one. Everything after it is the why and the how."),
    kv([
      ("Photoperiod", "18 h light / 6 h dark, protected like a fire alarm. Some cultivars initiate flowers at up to 14–15 h" + _c("mp-ahrens-2023-photoperiod") + ", so 18 h is your safety margin."),
      ("Light", "Moderate: ~300–500 µmol·m⁻²·s⁻¹ PPFD. Enough for steady regrowth, not so much that shoots turn short and squat."),
      ("Feed", "Nitrogen-forward veg feed, ~160 mg/L N is the researched optimum" + _c("mp-saloner-2020-nitrogen") + "; EC moderate (~1.4–2.0 mS/cm as practitioner convention). Never push her lush."),
      ("Shape", "Flat, wide, open-centre hedge: a permanent frame of 4–6 scaffolds, harvested for upright shoots every 2–3 weeks."),
      ("Harvest rule", "Take at most about half the shoots per pass; cut above the first node so each stub regrows two."),
      ("Testing", "HpLVd qPCR on every mother every 4–6 weeks, root tissue" + _c("mp-tumi-hlvd-testing") + ". New genetics quarantine + test twice before joining."),
      ("Tools", "Fresh or sanitised blade per plant, every time. The blade is how mother rooms die."),
      ("Replacement", "On evidence — a failed test or a sliding rooting % — never on the calendar alone. Always with an overlap, never cold-turkey."),
      ("Backup", "Two copies of every cultivar you care about, ideally in different rooms or in tissue culture."),
    ]),
    p("Five rules carry most of the value:"),
    ol([
      "<strong>Protect the photoperiod with margin.</strong> Flower initiation has been recorded at photoperiods up to 14 h, and in some cultivars 15 h" + _c("mp-ahrens-2023-photoperiod") + ". 18/6 exists to make timer faults and light leaks survivable.",
      "<strong>Feed for shoots, not for show.</strong> A mother is farmed for firm, pencil-thick regrowth. The dark, droopy, overfed look produces cuttings that wilt and stall.",
      "<strong>Build the frame once, then farm the regrowth.</strong> Architecture decides cutting count more than feed or light do.",
      "<strong>Assume hop latent viroid is hunting you.</strong> Roughly 90% of surveyed California facilities carried it" + _c("mp-adkar-2023-hidden-threat") + ". Blade discipline plus a testing rotation is the entire defence.",
      "<strong>Replace on data, with overlap.</strong> A candidate runs alongside the old mother and proves itself before anything gets culled.",
    ]),
    callout("key", "The one-sentence job",
      p("Keep a genetically known, pathogen-tested plant in permanent vegetative growth, and turn her "
        "into a predictable weekly stream of cuttings without ever letting her tell you a lie.")),
  ]})

# ---------------------------------------------------------------- 03 vocabulary
SECTIONS.append({"id": "vocab", "kicker": "03 · The vocabulary",
  "title": "Eight words that make the rest read plainly",
  "blocks": [
    p("Mother-room talk borrows from horticulture, virology and factory scheduling. These eight terms "
      "cover it; everything else is defined where it appears."),
    defterm("Mother / stock plant", "A plant held permanently in vegetative (leafy) growth, never "
            "flowered, kept purely as a source of cuttings. 'Mother' and 'stock plant' mean the same thing."),
    defterm("Photoperiod", "The hours of light per day. Photoperiod-dependent cannabis flowers when "
            "nights get long; mothers are kept on long days (18 h light) so they never switch."),
    defterm("PPFD", "Photosynthetic photon flux density — how much usable light lands on the leaves, "
            "in µmol·m⁻²·s⁻¹. Mothers run moderate PPFD, not flower-room intensity."),
    defterm("Node", "The point on a stem where leaves and side-shoots attach. Cuts are made relative "
            "to nodes, and every stub left with a node can regrow new shoots."),
    defterm("EC", "Electrical conductivity of the feed water, in mS/cm — a proxy for total dissolved "
            "nutrient strength. Mothers run moderate EC; high EC pushes soft, salty growth."),
    defterm("Viroid", "The smallest known infectious agent: a bare loop of RNA with no protein coat, "
            "a fraction the size of a virus. Hop latent viroid (HpLVd) is the one that matters in cannabis."),
    defterm("Dudding", "The disease syndrome HpLVd causes: outwardly normal plants that finish small, "
            "brittle and weak, with poor trichome set and badly reduced potency."),
    defterm("Indexing", "Systematically testing stock plants for pathogens on a fixed rotation, so a "
            "clean result is recent enough to mean something. Borrowed from certified clean-stock horticulture."),
  ]})

# ---------------------------------------------------------------- 04 the room
SECTIONS.append({"id": "room-setup", "kicker": "04 · The how & why",
  "title": "The room: 18/6, moderate light, boring climate",
  "blocks": [
    p("Photoperiod is the load-bearing wall. Photoperiod-dependent cannabis initiates flowering when "
      "the dark period gets long enough, and the threshold is closer than most people think: in a "
      "six-photoperiod trial, every cultivar tested initiated flowers at photoperiods up to 14 h of "
      "light, and some began initiating at 15 h" + _c("mp-ahrens-2023-photoperiod") + ". An 18 h day "
      "is not a magic number — it is a 3–4 hour safety margin over the worst-case switch point."),
    p("A mother that starts flowering is a genuine mess: you lose weeks reverting her (re-vegging is "
      "slow and the regrowth comes back twisted), and any cuttings taken while she is transitioning "
      "root and grow erratically. Mother rooms rarely fail photoperiod on purpose — they fail by a "
      "dead timer channel, a contactor stuck off, or light bleeding through a doorway from a flowering "
      "room next door. Audit the dark period monthly: stand in the room, lights out, five minutes, and "
      "fix any glow you can see."),
    p("The 18/6 vs 24/0 debate: both keep photoperiod cultivars vegetative. Continuous light costs "
      "about a third more in energy, and the practitioner arguments for giving a dark period — root "
      "growth, recovery — are weakly evidenced in either direction, so treat them as preference, not "
      "fact. 18/6 is the default because it works and costs less. One genuine caveat: "
      "<strong>autoflowering genetics cannot be mothered at all</strong> — they flower on age, not "
      "photoperiod, and no light schedule will stop them."),
    figure(L.zones("Mother-room light target", 0, 800,
            [(0, 150, L.REDL, "starved"), (150, 300, L.AMBL, "slow"),
             (300, 500, L.GL, "target"), (500, 650, L.GXL, "diminishing"),
             (650, 800, L.AMBL, "no gain here")],
            unit="",
            note="Canopy PPFD in µmol·m⁻²·s⁻¹. Practitioner target; the trade-offs behind it are cited in the text."), 2,
      "Moderate light is a choice, not a compromise. A mother is farmed for cuttable regrowth, and "
      "300–500 µmol keeps shoots long enough to cut and thick enough to root."),
    p("Why moderate light and not flower-room intensity? Vegetative cannabis will happily use far more "
      "— growth kept responding across a 135–1430 µmol trial range — but light also reshapes the "
      "plant: internode length and leaf size shrink steadily as intensity rises" + _c("mp-moher-2022-veg-light") +
      ". Run a mother at 900+ µmol and the regrowth comes back short, tight and squat — compact is "
      "great for a production plant, and miserable to cut 8–15 cm shoots from. Run her under ~150 µmol "
      "and shoots come thin, stretched and weak, with the low carbohydrate reserves that root poorly. "
      "300–500 µmol is the working band where regrowth is fast <em>and</em> shaped like cuttings."),
    p("Climate: nothing exotic. Around 22–26 °C days, roughly 55–70% relative humidity, gentle "
      "continuous air movement (practitioner convention). The mother room should be the most boring "
      "room in the facility — every stress event shows up two weeks later as a batch of cuttings that "
      "roots at 60% instead of 90, and you will struggle to connect the two."),
  ]})

# ---------------------------------------------------------------- 05 feeding
SECTIONS.append({"id": "nutrition", "kicker": "05 · The how & why",
  "title": "Feeding a cutting factory: nitrogen-forward, never lush",
  "blocks": [
    p("Mother nutrition has a different goal from flower nutrition. You are not growing buds and you "
      "are not even really growing a plant — you are farming <em>stems and growing tips</em>, "
      "continuously, from the same root system, for months. That means a vegetative, nitrogen-forward "
      "feed, held at moderate strength."),
    p("The nitrogen number has actual research behind it: in a five-level dose trial on medical "
      "cannabis under long days, <strong>160 mg/L N</strong> was the optimum for vegetative growth. At "
      "30 mg/L plants were severely deficient — stunted and yellowing — and at 240–320 mg/L growth "
      "went backwards, with smaller, dark-green plants showing classic over-supply" + _c("mp-saloner-2020-nitrogen") +
      ". More nitrogen is not more shoots. There is a hill, and the top of it is lower than most feed "
      "charts assume."),
    p("Here is the part that catches people: <strong>what makes a cutting root is not nitrogen, it is "
      "carbohydrate.</strong> Classic stock-plant work found rooting is limited primarily by the "
      "carbohydrate status of the cutting; nitrogen matters, but as the secondary factor" + _c("mp-druege-2004-stockplant-n") +
      ". An overfed mother pushes soft, watery, dark shoots — big drooping leaves, hollow stems — that "
      "look magnificent and then wilt flat in the dome and root late or never. Firm, pencil-thick, "
      "slightly hungry-looking regrowth is the factory spec."),
    figure(L.zones("Feed strength for mothers", 0.5, 3.0,
            [(0.5, 1.0, L.AMBL, "hungry"), (1.0, 1.4, L.GXL, "light"),
             (1.4, 2.0, L.GL, "target"), (2.0, 2.4, L.AMBL, "rich"),
             (2.4, 3.0, L.REDL, "soft growth")],
            unit="",
            note="Feed EC in mS/cm — practitioner convention, product-dependent. The N optimum inside it is researched."), 3,
      "Moderate EC keeps regrowth firm. Past ~2.4 mS/cm most mothers drift into the lush, soft growth "
      "that roots badly — the plant looks better and the cuttings perform worse."),
    table(["Parameter", "Working range", "Basis"], [
      ["Nitrogen", "150–200 mg/L, centred on ~160", "Dose-response trial optimum" + _c("mp-saloner-2020-nitrogen")],
      ["Feed EC", "1.4–2.0 mS/cm", "Practitioner convention; watch the plant, not the chart"],
      ["pH", "5.8–6.2 (coco / rockwool)", "Practitioner convention"],
      ["Irrigation", "Steady, small drybacks, no drought cycling", "Stress now = poor rooting in 2 weeks"],
      ["Day before a cut", "Water well; no foliar sprays", "Turgid, dry-leaved shoots handle and root best"],
    ], cls="compact", caption="Mother feed cheat-sheet. Only the nitrogen row carries a researched number; the rest is convention that works, stated as such."),
    callout("tip", "Read the mother, not the bottle",
      p("Your real feedback loop is the <strong>rooting percentage of her cuttings, batch over "
        "batch</strong>. If strike rate drifts down over two or three batches and pests and viroid are "
        "ruled out, audit the feed before you reach for anything exotic — the fix is usually "
        "<em>less</em>: less N, less EC, firmer shoots.")),
  ]})

# ---------------------------------------------------------------- 06 architecture
SECTIONS.append({"id": "architecture", "kicker": "06 · Do this",
  "title": "Build the frame once, then farm the regrowth",
  "blocks": [
    p("Cutting count is mostly architecture, not vigour. A mother left to grow naturally makes one "
      "dominant leader and a handful of weak laterals — a Christmas tree, and a terrible factory. The "
      "fix is the same trick hedge-layers and fruit growers use: remove the leader early, force the "
      "plant wide, and keep it flat."),
    p("The mechanism is <strong>apical dominance</strong> — the top shoot chemically suppresses the "
      "shoots below it. Cut the top off (<strong>topping</strong>) and the suppression lifts: the side "
      "shoots below the cut all push at once. Do this once to the young plant, then once to each of "
      "the released side branches, and you have converted one growing point into eight to twelve. "
      "Those become the <strong>permanent frame</strong>; everything above them is crop."),
    steps([
      ("Establish (weeks 0–2)", "Start from your best <em>tested</em> clone — the mother inherits everything, good and bad. Transplant, let her root out and settle."),
      ("First top (week 2–3)", "Top above the 4th–5th node. The plant answers with 4–6 strong side shoots."),
      ("Build scaffolds (weeks 3–5)", "Select the best 4–6 laterals as permanent scaffolds; top each once so they fork. Remove the rest."),
      ("Open the centre (ongoing)", "Strip weak, inward-facing shoots so light and air reach the middle. A shaded centre grows the thin, stringy shoots that root worst."),
      ("First harvest (week 5–6)", "The tips you would prune anyway are your first cuttings. From here, the plant is in production."),
    ]),
    figure(_FIGS["architecture"], 4,
      "The production shape: a short trunk topped young, 4–6 permanent scaffolds, and a flat harvest "
      "zone of upright shoots. The frame is built once and never cut into; the hedge above it is "
      "harvested every two to three weeks."),
    p("Harvest rules keep the factory running: cut each shoot <strong>above its first node</strong> so "
      "the stub regrows two shoots (the hedge gets denser every pass); take at most about half the "
      "canopy in one pass; and leave every scaffold with working leaves — a fully stripped branch "
      "stalls instead of regrowing. Expect a 2–3 week regrowth cycle between full passes "
      "(practitioner convention)."),
    p("Cut with the finished cutting in mind. The propagation research says a cannabis cutting roots "
      "best with <strong>three or more fully expanded leaves left intact</strong> — and that trimming "
      "leaf tips, the classic nursery habit, dropped rooting success from 71% to 53%" + _c("mp-caplan-2018-cuttings") +
      ". It also found position barely matters: cuttings from apical (top) and basal (lower) shoots "
      "rooted about the same" + _c("mp-caplan-2018-cuttings") + ". So harvest the whole hedge, not "
      "just the pretty tips — but grow shoots big enough to carry three real leaves."),
    figure(L.line("Output of one mid-size mother after planting",
            [("w0", 0), ("w2", 0), ("w4", 6), ("w6", 14), ("w8", 22), ("w10", 28), ("w12", 32), ("w14", 34), ("w16", 35)],
            ["w0", "w2", "w4", "w6", "w8", "w10", "w12", "w14", "w16"],
            ylab="cuttings / week", ymax=40,
            note="Indicative practitioner curve, cultivar- and size-dependent. The frame costs ~6 weeks before it pays."), 5,
      "A mother spends her first six weeks becoming a factory. Plan the build phase into your "
      "production calendar — a new mother is not a source of cuttings on day one."),
    callout("note", "How many cuttings per mother?",
      p("There is no good published number — it depends on cultivar, pot size and frame. Practitioner "
        "ballparks: a compact mother in a 10–15 L pot gives roughly 15–30 cuttings per pass; a large "
        "production mother in 30–50 L can give 50–100+. Treat these as planning starting points and "
        "measure your own plants — your records beat anyone's ballpark within two months.")),
  ]})

# ---------------------------------------------------------------- 07 scheduling
SECTIONS.append({"id": "scheduling", "kicker": "07 · Do this",
  "title": "Scheduling mothers against production demand",
  "blocks": [
    p("Mother count is a supply-chain calculation, not a vibe. Work backwards from the flower room: "
      "how many plants does each flip need, and when? Then inflate for losses. Not every cutting "
      "roots, and not every rooted clone is worth vegging — so take 15–40% more cuttings than the "
      "plant count you actually need, exactly as in the <a href='cloning.html'>cloning guide</a>."),
    table(["Step", "Number", "Working"], [
      ["Plants to flower", "100", "The target the room actually needs"],
      ["Veg cull (~10%)", "keep 110", "Weak and slow clones get binned at transplant"],
      ["Rooting rate (~85%)", "take ≥130", "110 ÷ 0.85 — a realistic strike rate, not a brochure one"],
      ["Round up + buffer", "take 140", "Overage costs cents; a short flower room costs a cycle"],
    ], cls="compact", caption="The demand math for a 100-plant flip. Adjust the two loss rates to your own measured numbers as soon as you have them."),
    figure(L.bars("The demand math: 100 flowering plants",
            [("Cut", 140), ("Rooted", 119), ("Into veg", 110), ("To flower", 100)], unit="",
            note="140 cuttings at 85% rooting ≈ 119; cull to 110 in veg; 100 make the room, with spares.",
            maxv=160), 6,
      "Losses are normal and planned-for. The overage exists so that culling hard at every stage "
      "still fills the flower room on schedule."),
    p("Then divide by output: mothers needed = cuttings per flip ÷ yield per mother per pass. If "
      "mid-size mothers give ~35 cuttings a pass and you need 140 per flip, that is four mothers — "
      "so run <strong>five</strong>. The spare is not optional: it is what lets you retire, rest or "
      "quarantine a plant without missing a flip."),
    p("Stagger the harvests. Split the bank into A and B cohorts and alternate passes so no mother is "
      "stripped hard twice in a row — this keeps every pass inside the take-half rule, and it gives "
      "you a built-in diagnostic: if both cohorts' rooting slips together, suspect the room; if one "
      "cohort slips alone, suspect those plants."),
    callout("tip", "A cuttings calendar beats a headcount",
      p("A smaller bank of well-run, well-tested mothers on a stagger out-produces a crowd of "
        "neglected ones — and every extra plant is another thing to water, prune and test on "
        "rotation" + _c("mp-tumi-hlvd-testing") + ". Size the bank to the calendar, not to comfort.")),
  ]})

# ---------------------------------------------------------------- 08 age & drift
SECTIONS.append({"id": "age-drift", "kicker": "08 · The debate",
  "title": "Do mothers wear out? What the genetics actually say",
  "blocks": [
    p("Grower folklore says a mother 'degrades' and should be replaced every 6–12 months. Plenty of "
      "operators, meanwhile, hold the same mother for five-plus years and swear she is identical. "
      "Both camps are pointing at something real — they are just pointing at different mechanisms."),
    p("<strong>Somatic mutation is real.</strong> Plants do not separate their reproductive cells the "
      "way animals do — every cell that divides can pass a copying error to everything grown from it. "
      "Deep whole-genome sequencing of a single cannabis plant found measurable <strong>genetic "
      "mosaicism</strong> within one individual: the top, middle and bottom of the same plant were not "
      "genetically identical" + _c("mp-adamek-2022-mosaicism") + ". The study was motivated by exactly "
      "the folklore above — growers reporting clonal lines that lose vigour and potency over time" + _c("mp-adamek-2022-mosaicism") + "."),
    p("But the follow-up work reframed the whole debate: across 70 micropropagated clones, mutation "
      "load tracked <strong>the number of propagation cycles</strong> — almost perfectly linearly "
      "(r &gt; 0.92) — and <em>not</em> chronological age" + _c("mp-adamek-2024-subcultures") + ". "
      "Clones of the same calendar age carried very different mutation loads depending on how many "
      "times they had been re-propagated. Every cut-and-regrow round is a burst of cell division, and "
      "cell division is where copying errors happen."),
    figure(L.line("Mutation load rises with propagation cycles, not with age",
            [("0", 0), ("1", 1), ("2", 2), ("3", 3), ("4", 4), ("5", 5), ("6", 6)],
            ["0", "1", "2", "3", "4", "5", "6"],
            ylab="relative mutation load", ymax=8,
            note="Indicative shape. In micropropagated cannabis, variant count rose linearly with subculture number (r > 0.92)."), 7,
      "The x-axis that matters is propagation cycles, not months on the bench. A mother sitting "
      "quietly for two years accrues less mutational churn than a line re-cloned from a clone every "
      "month." + _c("mp-adamek-2024-subcultures")),
    p("What actually degrades long-held mothers, in practice, is usually not the genome: it is "
      "accumulating pathogens (the next two sections), a root-bound pot, an exhausted woody frame, or "
      "care that drifted. All of those are testable and fixable, and none of them is 'age'. Epigenetic "
      "change — heritable gene-expression drift without sequence change — is also documented in clonal "
      "cannabis populations, but its contribution to lost vigour is not yet settled; treat it as an "
      "open question, not a scheduling rule."),
    callout("key", "The verdict",
      p("Keep a mother for as long as she (a) tests clean and (b) her cuttings' rooting rate and "
        "downstream performance hold steady in your records. Replace on evidence, not anniversaries. "
        "And when you do re-mother, start from low-generation, tested material — not from the far end "
        "of a long clone-of-clone chain" + _c("mp-adamek-2024-subcultures") + ".")),
  ]})

# ---------------------------------------------------------------- 09 pathogen amplifier
SECTIONS.append({"id": "pathogen-risk", "kicker": "09 · The risk",
  "title": "The mother room is a pathogen amplifier",
  "blocks": [
    p("Whatever lives in the mother room ships to every room downstream, on schedule, with a courtesy "
      "label on the tray. Spider mites, root aphids, fungus gnats, powdery mildew, root-rot organisms "
      "— the mother room is the reservoir that re-seeds them all, which is why IPM effort concentrated "
      "there pays off everywhere (see the <a href='ipm-sop.html'>IPM SOP</a>)."),
    ul([
      "<strong>Blades and scissors</strong> — sap-to-sap contact, the number one route for the pathogen that matters most.",
      "<strong>Hands and gloves</strong> — change gloves between plants on cut days, not between rooms.",
      "<strong>Shared or recirculated irrigation</strong> — pathogens have been detected moving plant-to-plant through nutrient solution and run-off" + _c("mp-punja-2025-hplvd-mgmt") + ". Mothers should never share a recirculating loop or a flood table.",
      "<strong>Benches, trays and cans</strong> — viroid RNA has been recovered from bench surfaces and watering cans in working facilities" + _c("mp-punja-2025-hplvd-mgmt") + ".",
      "<strong>The cuttings themselves</strong> — the whole point of the room, and the perfect courier.",
    ], "tight"),
    p("Three habits close most of the routes: mothers get <strong>dedicated tools</strong> that never "
      "visit other rooms; work runs <strong>cleanest-first</strong> (mothers before veg, veg before "
      "flower, never backwards through a dirty room); and anything that touches sap gets sanitised or "
      "swapped <strong>between plants</strong>, not between benches. Then there is the organism that "
      "turned all of this from good practice into survival — next section."),
  ]})

# ---------------------------------------------------------------- 10 HpLVd
SECTIONS.append({"id": "hplvd", "kicker": "10 · The threat",
  "title": "Hop latent viroid: the quiet destroyer of stock",
  "blocks": [
    p("<strong>Hop latent viroid (HpLVd)</strong> is a bare, circular strand of RNA about 256 "
      "nucleotides long — no protein coat, no cell, a fraction the size of a virus" + _c("mp-punja-2025-hplvd-mgmt") +
      ". It was first tied to failing cannabis crops in California in 2019, as the cause of what "
      "growers had been calling <strong>dudding</strong>" + _c("mp-warren-2019-hplvd-ca") + ": plants "
      "that look normal through veg, then finish small and brittle with poor trichome set and badly "
      "reduced potency."),
    p("The scale is why it leads this paper. A 2021 industry survey built on roughly 200,000 tissue "
      "tests found about <strong>90% of California cannabis facilities</strong> carried HpLVd, with "
      "around 30% of plants affected in contaminated sites" + _c("mp-adkar-2023-hidden-threat") + ". "
      "Reported losses in dudded plants run to 50–70% of THC content" + _c("mp-adkar-2023-hidden-threat") +
      ", industry estimates put the annual cost near US$4 billion" + _c("mp-medgen-hlvd") + ", and "
      "sampling reported by researchers found roughly 40% of flower on Canadian dispensary shelves "
      "testing positive" + _c("mp-medgen-hlvd") + ". This is not a rare disease; it is the default "
      "state of untested stock."),
    p("The word <em>latent</em> is the trap: <strong>most infected plants show nothing</strong>" + _c("mp-adkar-2023-hidden-threat") +
      ". And a mother plant is the viroid's perfect host — long-lived (time to acquire it), cut "
      "hundreds of times a year (sap exposure at every pass), and upstream of everything (every "
      "cutting inherits it). The viroid has been detected in fully asymptomatic stock plants and in "
      "the rooted cuttings taken from them" + _c("mp-punja-2025-hplvd-mgmt") + ". One quiet mother "
      "means months of infected clones, invisibly."),
    figure(_FIGS["hlvd_tools"], 8,
      "The main route is mechanical: infectious sap carried on the blade from plant to plant. Sap "
      "stays infectious on tools and surfaces for about 7 days, and in dried plant matter for up to 4 "
      "weeks" + _c("mp-punja-2025-hplvd-mgmt") + ". A fresh or sanitised blade per plant converts an "
      "outbreak into a single casualty."),
    p("Transmission, measured: mechanical spread via sap and tools is primary" + _c("mp-adkar-2023-hidden-threat") + _c("mp-punja-2025-hplvd-mgmt") +
      ", but the viroid also moved <strong>root-to-root between plants sharing hydroponic nutrient "
      "solution within about two weeks</strong>, and was recovered from recirculated and run-off "
      "solution, bench surfaces and watering cans" + _c("mp-punja-2025-hplvd-mgmt") + ". After "
      "entering a cut stem it reached roots in 2–3 weeks but foliage only at 4–6 weeks" + _c("mp-punja-2025-hplvd-mgmt") +
      " — which is why a leaf test can pass a freshly infected plant, and why root sampling and "
      "re-testing exist (next section)."),
    figure(L.hbars("Reported worst-case impact of dudding",
            [("THC content", 70), ("Cannabinoid production", 50), ("Terpene production", 50)],
            unit="%", note="Upper ends of reported reduction ranges in infected, symptomatic plants vs clean."), 9,
      "What an infected plant can cost by harvest. Reported reductions reach 50–70% of THC and up to "
      "half of cannabinoid and terpene production — from a plant that looked fine at cutting time." + _c("mp-adkar-2023-hidden-threat")),
    p("Tool protocol: the gold standard is a <strong>fresh single-use blade per mother</strong>. "
      "Failing that, a 10% household-bleach dip between plants" + _c("mp-medgen-hlvd") + " — bleach "
      "and hypochlorous acid degraded viroid RNA in sap in testing, where quats and most 'gentler' "
      "sanitisers did not reliably" + _c("mp-punja-2025-hplvd-mgmt") + ". Two hard truths to go with "
      "it: no disinfectant does anything for a plant already infected — infected means cull" + _c("mp-punja-2025-hplvd-mgmt") +
      " — and isopropyl alcohol alone is not proven against viroid RNA, so the flame-and-wipe habit "
      "is comfort, not control."),
    callout("warn", "Long days hide it; they don't stop it",
      p("In trials, HpLVd spread through the plant <em>faster</em> once plants moved to a 12/12 "
        "flowering photoperiod than under continuous light" + _c("mp-punja-2025-hplvd-mgmt") + ". A "
        "mother on 18 h days can carry a low, slow, hard-to-detect infection that only shows its "
        "teeth downstream in flower. 'My mothers look clean' and 'my mothers are clean' are different "
        "sentences — only a test connects them.")),
  ]})

# ---------------------------------------------------------------- 11 indexing
SECTIONS.append({"id": "indexing", "kicker": "11 · Do this",
  "title": "Indexing: a testing rotation that keeps the bank clean",
  "blocks": [
    p("<strong>Indexing</strong> is the clean-stock habit of testing every stock plant on a fixed "
      "rotation, so that 'she tested clean' always has a date on it. In cannabis the workhorse assay "
      "is RT-qPCR for HpLVd, run from a small tissue sample" + _c("mp-medgen-hlvd") + " — cheap "
      "enough now that the rotation, not the test, is the discipline."),
    p("The cadence that industry testing labs converge on: <strong>every mother, every 4–6 "
      "weeks</strong>" + _c("mp-tumi-hlvd-testing") + ", and always <strong>before a big cutting "
      "day</strong> rather than after it" + _c("mp-medgen-hlvd") + ". Sample <strong>root "
      "tissue</strong> where possible — the viroid concentrates there earliest and most uniformly, "
      "making roots the most reliable single sample" + _c("mp-tumi-hlvd-testing") + _c("mp-punja-2025-hplvd-mgmt") +
      " — and take material from more than one point on the plant, because viroid distribution is "
      "uneven and a single lucky sample can pass an infected plant" + _c("mp-tumi-hlvd-testing") + "."),
    figure(_FIGS["testcal"], 10,
      "A year of indexing on one strip: short-interval HpLVd qPCR on every mother, a quarterly "
      "deep review of pests, hygiene and records, and a quarantine-plus-two-tests gate on anything "
      "new" + _c("mp-tumi-hlvd-testing") + "."),
    p("<strong>Intake is the front door, and it is where most banks get burned.</strong> New genetics "
      "— a bought-in clone, a swap, a rescue — is the single most common way HpLVd enters a facility. "
      "Quarantine everything: separate room (or at minimum a separated bench with its own tools), "
      "test on arrival, hold 2–4 weeks, and test again before it touches the bank. The re-test is not "
      "paranoia: systemic distribution takes around six weeks, so an early sample from a "
      "just-infected plant can genuinely test clean" + _c("mp-medgen-hlvd") + "."),
    figure(L.flow("Intake quarantine: nothing joins the bank untested",
            [("Arrive", "log it, isolate it"), ("Quarantine", "own space + tools"),
             ("Test 1", "qPCR on arrival"), ("Hold", "2–4 weeks"),
             ("Test 2", "roots, pre-release"), ("Join bank", "two clean results")]), 11,
      "The gate for incoming genetics. Two clean tests separated by a hold beats one clean test on "
      "arrival, because a fresh infection can sit below detection for weeks" + _c("mp-medgen-hlvd") + "."),
    p("Keep records like they are part of the plant: per-mother ID, test dates and results, cut "
      "counts, and per-batch rooting %. The rooting trend is your free continuous assay — a mother "
      "whose clones' strike rate slides ten points over three batches is telling you something the "
      "last quarterly test hasn't caught yet."),
    callout("warn", "The positive-result playbook",
      p("Isolate the plant immediately. Re-test to confirm — fresh sample, roots. Trace every plant "
        "the same tools touched since the last clean test and test those. Cull confirmed positives: "
        "bag the plant <em>at the bench</em> and carry it out sealed, don't walk loose infected "
        "material through the facility. Elite genetics can sometimes be rescued through meristem "
        "tissue culture — averaging ~41% pathogen-free recovery, anywhere from 0–100% by genotype" + _c("mp-punja-2025-hplvd-mgmt") +
        " — but that is a months-long lab job (see <a href='tissue-culture.html'>tissue culture</a>), "
        "not a way to save production stock this cycle.")),
  ]})

# ---------------------------------------------------------------- 12 replacement
SECTIONS.append({"id": "replacement", "kicker": "12 · Do this",
  "title": "Replacing a mother without dropping a batch",
  "blocks": [
    p("Mothers are replaced for five reasons: a confirmed pathogen (immediate, no debate); a rooting "
      "rate that trends down across three or more batches with other causes ruled out; a frame gone "
      "woody and slow after many months of harvest; a root-bound pot that feeding can't compensate; "
      "or simple space economics. Only the first one is urgent. Everything else earns a planned "
      "succession — and succession has a shape."),
    steps([
      ("Select the donor", "Take the replacement cutting from the best scaffold of a mother that is testing clean — or from your lowest-generation tested backup. The candidate inherits everything."),
      ("Build the candidate", "Root it and build the frame exactly as in section 06 — expect ~6 weeks before it produces meaningfully."),
      ("Test twice during build", "qPCR at rooting and again before it enters service. A candidate is not a mother until it has two clean results."),
      ("Overlap", "Run old and new side by side for at least one full cutting cycle. Compare rooting % of both cohorts head-to-head."),
      ("Retire the old plant", "Cull, bag and remove; strip and sanitise her station — pot, tray, stakes, drippers — before anything else uses it."),
    ]),
    figure(_FIGS["succession"], 12,
      "Succession on a timeline: the candidate is built and tested while the incumbent still serves, "
      "they overlap for a full cycle, and only then does the old mother retire. The backup copy "
      "exists through the whole story."),
    p("The overlap is the insurance policy — never cut over cold-turkey. If the candidate's cuttings "
      "underperform, you still have the incumbent; if she matches, you cull with confidence. And keep "
      "a <strong>second copy of every cultivar you care about</strong> at all times — a backup mother "
      "in another room, or a culture in a tissue-culture bank" + _c("mp-monthony-2021-tc") + ". A "
      "cultivar with one living copy is one fusarium pot or one positive test away from extinct."),
    p("Two maintenance notes that extend service life: root-bound decline responds to repotting or "
      "root-pruning on a schedule rather than waiting for symptoms (practitioner convention). And "
      "<strong>re-mothering</strong> — starting a fresh mother from the old one's best shoot — resets "
      "her architecture and her pot, but it does <em>not</em> reset her pathogens or her accumulated "
      "mutations: whatever she carries, the new plant carries" + _c("mp-adamek-2024-subcultures") + ". "
      "Test before you promote."),
  ]})

# ---------------------------------------------------------------- 13 clone-from-clone
SECTIONS.append({"id": "clone-from-clone", "kicker": "13 · The alternative",
  "title": "Clone-from-clone: running without mothers",
  "blocks": [
    p("Some operations skip dedicated mothers entirely: each round, they take the next batch of "
      "cuttings from production plants in early veg, just before those plants flip to flower. The "
      "cuttings root while the donors finish. No mother room, no mother labour, a whole room's rent "
      "back. It is a real system with a real cost structure — and a real failure mode."),
    p("The honest evidence first: it works, mechanically. 'Retip' cuttings — cuttings taken from "
      "recently rooted cuttings — rooted at 76–81% even without hormone, and the resulting plants "
      "finished comparably to stem-cutting plants, with no change in cannabinoid content" + _c("mp-kurtz-2022-retip") +
      ". A generation hop, by itself, does not wreck a crop."),
    p("The problem is not any single hop — it is what the chain accumulates:"),
    ul([
      "<strong>The mutation ratchet.</strong> Mutation load rises with every propagation cycle" + _c("mp-adamek-2024-subcultures") + ". A mother bank holds every batch at generation 1; a year of clone-from-clone is 15–25 generations, every one a fresh roll of the dice, with no reference plant to check drift against.",
      "<strong>The pathogen ratchet.</strong> With no long-lived plant, there is nothing to index. Your 'stock' is always two weeks from flowering, so there is no time for a quarantine-and-retest cycle — and an HpLVd hit anywhere in the chain propagates forward invisibly" + _c("mp-adkar-2023-hidden-threat") + ".",
      "<strong>Selection drift.</strong> Whoever takes cuttings picks the biggest, fastest-looking donors. Over many generations that quietly selects for stretch and speed over quality (practitioner observation — unproven, but widely reported).",
      "<strong>No way back.</strong> A mother bank can restart any batch from reference. A chain that goes bad — infected, drifted, or mislabeled — is simply gone, along with the cultivar.",
    ], "tight"),
    figure(_FIGS["lineage"], 13,
      "Hub versus chain. Both produce cuttings; only one has a reference. In the hub, every batch is "
      "generation 1 from a tested plant. In the chain, generation 5 carries whatever generations 1–4 "
      "collected, and nothing was ever re-tested against a known-good original."),
    p("The verdict: clone-from-clone is a legitimate <strong>bridge</strong> — during a build-out, "
      "for short runs, for cultivars you plan to drop — provided every donor round gets tested. As "
      "the <em>permanent</em> plan for genetics you care about, it is a slow-motion loss. The middle "
      "path many operators land on: a tissue-culture bank or one modest, well-tested mother per "
      "keeper cultivar as the anchor" + _c("mp-monthony-2021-tc") + ", plus clone-from-clone for "
      "volume in between."),
  ]})

# ---------------------------------------------------------------- 14 failure modes
SECTIONS.append({"id": "failure-modes", "kicker": "14 · When it goes wrong",
  "title": "How mother programmes die",
  "blocks": [
    p("Mother programmes rarely die loudly. They die in one of six quiet ways, most of them "
      "preventable with the habits already covered."),
    grid([
      card("The silent ratchet",
           p("One latent HpLVd mother plus shared snips. Every pass infects the next plant; nothing "
             "looks wrong until a flower room duds months later. <strong>Counter:</strong> blade per "
             "plant, root-sample qPCR every 4–6 weeks" + _c("mp-tumi-hlvd-testing") + "."),
           tag="viroid"),
      card("The single copy",
           p("One mother per cultivar. One root-rot pot, one positive test, one dropped tray — and "
             "the genetics are extinct. <strong>Counter:</strong> two copies, separate rooms, or a "
             "tissue-culture backup" + _c("mp-monthony-2021-tc") + "."),
           tag="continuity"),
      card("The lush trap",
           p("A proud, dark, overfed mother whose cuttings flop in the dome and rot. Rooting runs on "
             "the cutting's carbohydrate, not its nitrogen" + _c("mp-druege-2004-stockplant-n") + ". "
             "<strong>Counter:</strong> moderate N and EC, firm shoots, watch the strike rate."),
           tag="nutrition"),
      card("The slow strangle",
           p("Eighteen months in a 12 L pot. Vigour fades so gradually nobody sees it, and it gets "
             "blamed on 'age'. <strong>Counter:</strong> repot or root-prune on schedule; track "
             "cuttings-per-week so decline shows up as a number."),
           tag="roots"),
      card("The chain with no anchor",
           p("A year of clone-from-clone with no tests and no reference. The cultivar 'isn't what it "
             "used to be' and nobody can prove why, or get it back" + _c("mp-adamek-2024-subcultures") + ". "
             "<strong>Counter:</strong> keep an anchor — mother or culture — for every keeper."),
           tag="drift"),
      card("The calendar cull",
           p("Replacing proven, clean, productive mothers every six months on folklore — while blade "
             "hygiene, the thing that actually kills stock, goes unmanaged. <strong>Counter:</strong> "
             "replace on evidence" + _c("mp-adamek-2024-subcultures") + "; spend the saved effort on testing."),
           tag="process"),
    ], cols=2),
  ]})

# ---------------------------------------------------------------- 15 troubleshooting
SECTIONS.append({"id": "troubleshooting", "kicker": "15 · When it goes wrong",
  "title": "Symptom → cause → fix",
  "blocks": [
    p("Diagnose from the symptom, check the likely cause, act, and give it one batch cycle before "
      "judging the fix. Most mother problems announce themselves through the cuttings first."),
    table(["Symptom", "Likely cause", "What to do"], [
      ["Rooting % slides batch over batch, mother looks fine", "Early HpLVd; or soft overfed growth; or root-bound decline", "Root-sample qPCR first" + _c("mp-tumi-hlvd-testing") + "; then audit EC/N down; then check the pot"],
      ["Pistils or pre-flowers on a mother", "Photoperiod fault: dead timer, light leak, schedule under ~15 h", "Fix to a verified 18 h; dark-room audit; take no cuttings until regrowth is clean" + _c("mp-ahrens-2023-photoperiod")],
      ["Cuttings soft, stretchy, wilt fast in the dome", "Feed too rich, light too low — lush growth, thin reserves", "Drop EC 0.2–0.4; raise PPFD toward 400–500; firm shoots return in 1–2 passes" + _c("mp-druege-2004-stockplant-n")],
      ["Pale mother, thin shoots, slow regrowth", "Underfed N, or root-bound / root disease", "Lift N toward ~160 mg/L" + _c("mp-saloner-2020-nitrogen") + "; inspect the root ball while you're at it"],
      ["Downstream flower rooms dudding; mothers test-negative on leaves", "Latent HpLVd sitting below leaf detection", "Re-test from roots, multiple points per plant" + _c("mp-tumi-hlvd-testing") + _c("mp-punja-2025-hplvd-mgmt") + "; treat leaf-negative as unproven"],
      ["Pests reappearing in every clone batch", "The mother room is the reservoir", "Treat and monitor mothers first; inspect before every cutting pass — see the <a href='ipm-sop.html'>IPM SOP</a>"],
      ["A mother dies or tests positive and she was the only copy", "No backup existed", "Salvage via meristem culture if the genetics justify months of lab work" + _c("mp-punja-2025-hplvd-mgmt") + "; then fix the system: two copies, always"],
    ], cls="compact", caption="The recurring theme: the cuttings are the assay. A mother's problems show up in her clones' numbers before they show up on her leaves."),
  ]})

# ---------------------------------------------------------------- 16 mental model
SECTIONS.append({"id": "mental-model", "kicker": "16 · Take this with you",
  "title": "The mental model: a living backup that must prove it restores",
  "blocks": [
    p("Treat a mother plant exactly like a backup drive. Nobody trusts a backup because it looks fine "
      "on the shelf — you trust it because you test restores. The mother-room translation: the "
      "<strong>restore test</strong> is her cuttings' rooting rate, batch over batch. The "
      "<strong>integrity check</strong> is the qPCR rotation. The <strong>off-site copy</strong> is "
      "the second mother or the tissue-culture bank. The <strong>retention policy</strong> is "
      "evidence-based replacement with overlap. Run those four and the factory never runs dry."),
    callout("key", "If you remember five things",
      ol([
        "<strong>18/6 is a safety margin, not a magic number.</strong> Initiation has been recorded up to 14–15 h" + _c("mp-ahrens-2023-photoperiod") + " — protect the timer and hunt light leaks.",
        "<strong>Moderate everything.</strong> ~300–500 µmol, ~160 mg/L N" + _c("mp-saloner-2020-nitrogen") + ", moderate EC. The best-looking mother is rarely the best-performing one.",
        "<strong>Architecture is output.</strong> Top young, build 4–6 scaffolds, harvest half the hedge above the first node, every 2–3 weeks.",
        "<strong>The blade is the vector; the test is the defence.</strong> Fresh blade per plant, root-sample qPCR every 4–6 weeks" + _c("mp-tumi-hlvd-testing") + ", quarantine and test everything new twice" + _c("mp-medgen-hlvd") + ".",
        "<strong>Cycles age a line; calendars don't.</strong> Mutation load follows propagation cycles" + _c("mp-adamek-2024-subcultures") + " — keep clean proven mothers, replace on evidence, and never run without a second copy.",
      ])),
    p("From here: the <a href='cloning.html'>cloning guide</a> covers turning each harvested shoot "
      "into a rooted plant, and the <a href='tissue-culture.html'>tissue culture</a> paper covers the "
      "lab-side version of everything in this one — clean-stock banking, meristem rescue and "
      "long-term storage" + _c("mp-monthony-2021-tc") + "."),
  ]})
