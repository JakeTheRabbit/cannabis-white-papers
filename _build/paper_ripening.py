# -*- coding: utf-8 -*-
"""Paper: ripening, flush and harvest timing - the last two weeks and the call to chop."""
import json, os
from components import (p, lead, h, ul, ol, callout, defterm, table, figure, grid, card, chip, kv, steps)
import figs_lib as L

_FIGS = json.load(open(os.path.join(os.path.dirname(__file__), "figs_ripening.json"), encoding="utf-8"))

SLUG = "ripening-harvest-timing"
TITLE = "Ripening, flush and the harvest call"
EYEBROW = "Flowering · Finish"
SUB = ("The last two weeks and the call to chop: how buds actually ripen, how to read trichomes "
       "with a loupe properly, harvest windows by product goal, what the evidence really says "
       "about flushing, and how to keep botrytis from eating the reward while you wait.")
META = [("spark", "Flowering"), ("image", "10 diagrams"),
        ("quote", "Evidence-linked · 14 sources"), ("clock", "~17 min read")]
RELATED = ["flowering-stages", "harvest-dry-trim-cure", "mould-risk"]
REF_IDS = ["livingston-2020-trichome-maturation", "punja-2023-trichome-maturation",
           "aizpurua-2016-cannabinoid-evolution", "ross-elsohly-1997-cbn-age",
           "maillard-2015-leaf-nutrient-remobilization", "massuela-2022-pruning-cbd-yield",
           "namdar-2018-inflorescence-position", "pressclub-hash-trichome-transition",
           "rxgreen-2019-flushing-trial", "stemeroff-2017-flushing-thesis",
           "mahmoud-2023-botrytis-budrot", "punja2025-budrot-epi",
           "llewellyn-2022-light-intensity-yield", "huebner2024-uv-spectra"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

# ---------------------------------------------------------------- 01 start here
SECTIONS.append({"id": "start-here", "kicker": "01 · Start here", "title": "The last two weeks decide the grade",
  "blocks": [
    lead("Everything you did for eighteen weeks converges on one decision: when to cut. Cut early and "
         "you hand back weight and maturity the plant was still building. Wait too long and you are "
         "gambling finished flower against bud rot for marginal gains. This paper is the finish: how "
         "buds ripen, how to read them honestly, and how to land the chop where your product goal "
         "wants it."),
    p("It is written for a first or second grow, so every term is defined and every claim is graded. "
      "Where the evidence is solid, we say so. Where the industry runs on folklore, and late "
      "flower is where most of the folklore lives. We say that too, plainly. Flushing, amber "
      "percentages, 48-hour darkness, UV finishers: each gets the same treatment. What is shown, "
      "what is tradition, what is marketing."),
    p("Two jobs run in parallel through the final fortnight. Job one: let the plant finish, "
      "weight and resin maturity are still accruing later than most beginners believe" + _c("massuela-2022-pruning-cbd-yield") +
      ". Job two: protect what is already built, a dense, ripening canopy is peak botrytis "
      "habitat, and one wet night can cost more than a week of extra ripening ever adds" + _c("punja2025-budrot-epi") + "."),
    figure(L.flow("The last fortnight, in order",
            [("Peak bulk", "wk 6-7: weight still climbing"),
             ("Fade starts", "lower leaves yellow"),
             ("Clamp RH", "45-55%, air moving"),
             ("Scope q2d", "calyx, fixed spots"),
             ("Window", "cloudy max, amber creeps"),
             ("Chop", "logistics ready")],
            note="Two jobs at once: let the plant finish, and defend it while it does."), 1,
      "The finish is a sequence, not a date. The loupe decides when the window is open; the room "
      "decides whether you are still eligible to wait for it."),
    callout("note", "Who this is for",
      p("Anyone in week 6+ of flower wondering how close they are. Pairs with "
        "<a href='flowering-stages.html'>the flower cycle week by week</a> upstream and "
        "<a href='harvest-dry-trim-cure.html'>harvest, dry, trim and cure</a> downstream. "
        "This paper ends the moment the shears close.")),
  ]})

# ---------------------------------------------------------------- 02 vocabulary
SECTIONS.append({"id": "vocab", "kicker": "02 · Vocabulary", "title": "Eight terms that carry the whole paper",
  "blocks": [
    p("Late flower has its own dialect. These eight terms cover everything below, learn them "
      "once and the rest reads easily."),
    defterm("Trichome", "The mushroom-shaped resin gland coating buds and nearby leaves. The stalked "
            "ones on the flower hold most of the cannabinoids and terpenes, and their appearance "
            "under magnification is the primary ripeness signal."),
    defterm("Pistil (stigma)", "The white hair emerging from each flower. Pistils start white and "
            "brown as flowers age or get pollinated. A coarse, early ripeness cue only."),
    defterm("Calyx (bract)", "The teardrop-shaped pod that makes up the bud. Growers say calyx; "
            "botanically it is mostly bract. They visibly swell late in ripening, and their surface "
            "is where you read trichomes."),
    defterm("The fade", "Late-flower yellowing of fan leaves as the plant pulls mobile nutrients out "
            "of old leaves and into the flower. Normal senescence, not automatically a deficiency."),
    defterm("Flush", "Feeding plain water (or heavily diluted feed) for the final days or weeks, on "
            "the theory it improves flavour and burn. The theory is contested, section 07 "
            "covers what testing actually found."),
    defterm("Harvest window", "The stretch of days where trichome maturity fits your product goal. "
            "It opens gradually, drifts with genotype, and can be slammed shut early by mould."),
    defterm("Foxtailing", "New growth spiking out of a mature bud late in flower, usually from heat "
            "or light stress. It resets pistil and calyx cues and confuses the read."),
    defterm("Staggered harvest", "Cutting the ripe top canopy first and giving the lower canopy "
            "extra days under light to catch up, instead of chopping the whole plant at once."),
  ]})

# ---------------------------------------------------------------- 03 core answer
SECTIONS.append({"id": "core-answer", "kicker": "03 · The core answer", "title": "It is a window, not a date - and the product picks the spot",
  "blocks": [
    p("Strip away the forum noise and the harvest call reduces to three sentences. Ripeness is read "
      "from the trichomes on the calyx surface, not from the calendar, not from pistils. The right "
      "moment inside the ripening arc depends on what the flower is for, hash-makers cut "
      "earlier than flower growers, and extract-bound biomass is the most forgiving of all. And "
      "mould pressure, not impatience, is the only good reason to cut before your target: clean "
      "flower cut a few days early beats perfectly ripe flower with botrytis in it, every time."),
    figure(L.zones("Amber share as a harvest dial",
            0, 40, [(0, 5, L.BLUL, "hash window"), (5, 15, L.GL, "flower window"),
                    (15, 30, L.AMBL, "late / heavier"), (30, 40, L.REDL, "over-ripe")],
            unit="%",
            note="Share of amber heads on the calyx surface, mid-cola. Bands are working conventions, not lab-verified effect boundaries."), 2,
      "One axis, one decision. Where you cut along the amber dial follows from the product goal; "
      "the bands themselves are grower convention and genotype moves them."),
    p("Why waiting is usually right: harvest-timing trials keep finding that inflorescence weight "
      "climbs continuously deep into ripening. In a controlled indoor trial on a CBD cultivar, dry "
      "flower weight rose across every harvest point from week 5 to week 11 while cannabinoid "
      "concentration stayed flat, the best total yield landed at week 9, not week 7" + _c("massuela-2022-pruning-cbd-yield") +
      ". Cannabinoid tracking through flowering shows the same shape: content builds toward a "
      "cultivar-specific peak, and different chemotypes reach it at different times" + _c("aizpurua-2016-cannabinoid-evolution") + "."),
    figure(L.line("Flower weight keeps climbing late (schematic)",
            [(0, 55), (1, 74), (2, 90), (3, 100)],
            ["wk 5", "wk 7", "wk 9", "wk 11"],
            ylab="relative dry weight %", ymin=40, ymax=110,
            note="Schematic of the trend in Massuela et al. 2022: weight climbed at every harvest point; CBD concentration did not change."), 3,
      "The impatience tax, quantified: chopping two weeks early forfeits real weight while gaining "
      "nothing in concentration." + _c("massuela-2022-pruning-cbd-yield")),
    callout("key", "The three-sentence version",
      p("Read trichomes on the calyx, mid-cola, every two days from week 7. Cut where your product "
        "wants: cloudy-dominant with minimal amber for hash, cloudy with 5&ndash;15% amber for "
        "typical flower. If botrytis shows up, the debate is over, cut now.")),
  ]})

# ---------------------------------------------------------------- 04 biology
SECTIONS.append({"id": "how-buds-ripen", "kicker": "04 · The biology", "title": "What ripening actually is",
  "blocks": [
    p("Four visible processes run together in the final weeks, and each one is a signal you can "
      "read. Knowing what drives them is what stops you being fooled when one of them lies."),
    p("<strong>Trichomes mature and change colour.</strong> Through late flower the flower surface "
      "fills with capitate-stalked trichomes, the large, stalked glands that hold most of the "
      "resin. Microscopy work shows these glands change morphology and metabolite content as the "
      "flower matures: contents shift, stalks elongate, and the gland head's appearance tracks its "
      "internal state" + _c("livingston-2020-trichome-maturation") + ". Heads read clear while resin "
      "is still thin and building, turn cloudy or milky as contents mature, then amber as the resin "
      "ages and oxidation begins. How fast that runs, and how much amber ever shows, is strongly "
      "genotype- and age-dependent, some cultivars barely amber before the heads simply "
      "collapse" + _c("punja-2023-trichome-maturation") + "."),
    figure(_FIGS["trichome_stages"], 4,
      "The four stages a loupe shows you, and what each means for the call. Stages are days apart "
      "and genotype sets the pace, judge the population, not a single gland." + _c("punja-2023-trichome-maturation")),
    p("<strong>Cannabinoids build to a peak, then the resin ages.</strong> Weekly tracking through "
      "flowering shows THC and CBD accumulating toward a cultivar-specific peak late in the cycle" + _c("aizpurua-2016-cannabinoid-evolution") +
      ". Past the peak, THC slowly oxidises toward CBN. The degradation pathway is well "
      "documented in stored cannabis, where the CBN:THC ratio is literally used to age samples" + _c("ross-elsohly-1997-cbn-age") +
      ". Amber heads are that process starting on the plant. Be careful with the folklore extension: "
      "&lsquo;amber = couch-lock&rsquo; treats CBN as a sedative switch, and the human evidence for "
      "that is thin. Amber tells you the resin is past peak; it does not promise a specific effect."),
    p("<strong>Pistils brown and recede.</strong> Stigmas are white and receptive early, then brown "
      "and curl as flowers age. Useful as a coarse clock. Mostly-white means far too early"
      ", but they respond to stress and pollination as well as ripeness, and foxtailing resets "
      "them entirely. Pistils tell you when to start scoping. They never make the call."),
    p("<strong>Calyxes swell and the plant fades.</strong> In the last weeks bracts fatten "
      "noticeably, buds look suddenly denser, while fan leaves yellow from the bottom "
      "up. The fade is nutrient remobilisation: senescing leaves export their mobile nutrients "
      "(nitrogen above all) to the developing flower, a process documented across crop species" + _c("maillard-2015-leaf-nutrient-remobilization") +
      ". A gentle fade in week 8 is the plant finishing on schedule, not a deficiency to fix. A "
      "hard, crispy fade in week 6 is a problem, see troubleshooting."),
    callout("note", "Why colour tracks ripeness at all",
      p("The colour shift is the visible face of resin chemistry: thin fresh resin reads glassy, "
        "mature contents scatter light and read milky, and ageing oxidised resin yellows. That is "
        "why the read works. And why it is a proxy, not an assay. Two cultivars at the same "
        "colour stage are not guaranteed the same chemistry" + _c("punja-2023-trichome-maturation") + ".")),
  ]})

# ---------------------------------------------------------------- 05 the read
SECTIONS.append({"id": "reading-ripeness", "kicker": "05 · The read", "title": "Using a loupe properly: where, what, how often",
  "blocks": [
    p("Most bad harvest calls are not bad judgement. They are bad sampling. The grower reads "
      "one photogenic spot, or reads sugar leaves, or reads a different bud each visit, and the "
      "&lsquo;data&rsquo; wanders. Fix the sampling and the call gets easy."),
    p("<strong>Tools.</strong> A 30&ndash;60x jeweller's loupe is enough and costs almost nothing. "
      "A cheap USB or phone-clip microscope (60&ndash;200x) is easier on the eyes, lets you "
      "photograph the same spot over days, and makes the clear/cloudy distinction much less "
      "ambiguous. Use daylight-white light; HPS-orange light makes everything look amber, and blurple "
      "LED makes everything look purple. If the canopy angle is awkward, snip a single calyx and "
      "read it on a bench. A steady image beats a wobbling in-situ one."),
    figure(_FIGS["scope_map"], 5,
      "Where to read and where not to. The top ripens ahead of the bottom, and cannabinoid and "
      "terpene content falls top-to-bottom too" + _c("namdar-2018-inflorescence-position") +
      ", so a top-only read chops the room early, and a larf read makes you wait forever."),
    p("<strong>Where.</strong> Read the surface of the calyxes on the bud itself, mid-cola, at "
      "mid-canopy height. Not the sugar leaves. The small leaves inside the bud carry "
      "trichomes that mature and amber days ahead of the calyx surface, and reading them is the "
      "classic way to chop a week early. Mark two or three scoping spots with a bit of tape on the "
      "branch and return to exactly those spots every visit, plus one top cola so you can see the "
      "vertical gradient moving" + _c("namdar-2018-inflorescence-position") + "."),
    p("<strong>How often.</strong> Every two days from week 7 (or whenever pistils are majority "
      "brown). Trichome stages move on a timescale of days, and a twice-weekly read gives you a "
      "trendline instead of a snapshot. Log a one-line estimate each visit, for example "
      "&lsquo;d52: ~15% clear / 80% cloudy / 5% amber, mid&rsquo;, because the trend across "
      "visits is the actual signal."),
    ol(["Same spots, every visit: 2&ndash;3 marked mid-cola calyx sites plus one top cola.",
        "Same light: daylight-white torch or room lights, never under HPS glow.",
        "Read the calyx dome, ignore sugar-leaf trichomes entirely.",
        "Estimate percentages across the field of view, population, not the prettiest gland.",
        "Write it down. Three data points make a trend; zero data points make a vibe."]),
    figure(_FIGS["ripeness_signals"], 6,
      "The signal ladder. Everything above the loupe row is context that schedules your scoping. "
      "Only the trichome read on the calyx makes the chop decision."),
  ]})

# ---------------------------------------------------------------- 06 product goal
SECTIONS.append({"id": "product-windows", "kicker": "06 · Product goal", "title": "Flower, hash and carts want different chops",
  "blocks": [
    p("The single most useful upgrade to &lsquo;when do I harvest?&rsquo; is realising it is the "
      "wrong question. The right question is &lsquo;what is this flower for?&rsquo;, because "
      "the product defines the window."),
    p("<strong>Ice-water hash and rosin: cut at cloudy max, before amber.</strong> Hash-making is "
      "mechanical separation of intact trichome heads, and it wants them at peak structure: fully "
      "swollen, cloudy, and still cleanly detachable. Hash-makers consistently target maximum milky "
      "coverage with minimal amber. Amber heads are past peak, measurably smaller, and wash "
      "and press into darker, greasier product" + _c("pressclub-hash-trichome-transition") + ". On "
      "some cultivars 10&ndash;20% amber at peak cloudy is unavoidable and acceptable; nobody "
      "washing for quality waits for it on purpose."),
    p("<strong>Flower: cloudy-dominant with 5&ndash;15% amber is the conventional call.</strong> "
      "Smokeable flower has more room to ride the curve into early amber, full maturity, "
      "full weight, developed aroma. Growers chasing a &lsquo;heavier&rsquo; finish deliberately "
      "wait for 20&ndash;30% amber. Be honest about what that buys: documented resin ageing" + _c("ross-elsohly-1997-cbn-age") +
      ", folklore-grade effect claims, and real extra days of rot exposure" + _c("punja2025-budrot-epi") + "."),
    p("<strong>Extract-bound biomass (distillate carts): the widest window.</strong> Distillation "
      "strips and refines the extract anyway, so trichome-stage precision matters least, "
      "total cannabinoid content and clean, mould-free biomass matter most. Cutting a few days "
      "either side of peak moves little; letting botrytis in, or letting flower sit over-ripe and "
      "degrade, still costs potency. Ripeness discipline relaxes; sanitation discipline does not."),
    figure(_FIGS["product_windows"], 7,
      "Same plant, three products, three windows, and the rot-risk clock runs over all of "
      "them. Hash cuts earliest, flower mid, extract biomass is most forgiving." + _c("pressclub-hash-trichome-transition")),
    table(["Product", "Cut at", "Why", "Cost of missing late"], [
      ["Ice-water hash / rosin", "Cloudy max, minimal amber", "Intact, fully-swollen heads separate and press cleanest", "Darker, greasier hash; smaller aged heads wash poorly"],
      ["Flower (typical)", "Cloudy-dominant, 5-15% amber", "Full weight and aroma at resin maturity", "Fades toward harsher, sleepier folklore territory; rot exposure grows"],
      ["Flower (heavier preference)", "15-30% amber", "Deliberate over-ripening for a heavier reputation", "Documented resin ageing; longest rot exposure of any flower cut"],
      ["Distillate carts / extract", "Anywhere near peak", "Refinement forgives trichome-stage drift", "Only real enemies are mould and gross over-ripeness"],
    ], cls="compact", caption="The window by product goal. If one room feeds multiple products, cut hash plants first, flower second, extract biomass last."),
    callout("tip", "Mixed-goal rooms",
      p("Running one cultivar for both hash and flower? Stagger by product: take the hash plants (or "
        "the hash-destined top canopy) at cloudy max, and give the flower plants the extra ripening "
        "days. One room, two chops, both products in their window.")),
  ]})

# ---------------------------------------------------------------- 07 flush debate
SECTIONS.append({"id": "flush-debate", "kicker": "07 · The flush debate", "title": "Flushing: what testing found, and what it didn't",
  "blocks": [
    p("The tradition: feed plain water for the last 7&ndash;14 days so the plant &lsquo;uses up&rsquo; "
      "stored nutrients, giving smoother smoke, better flavour and white ash. It is one of the most "
      "confidently repeated rules in cultivation. It is also the one with the least supportive "
      "evidence, so here is what happens when someone actually tests it."),
    p("<strong>The Rx Green Technologies trial.</strong> The most-cited direct test: Cherry Diesel "
      "flushed for 0, 7, 10 or 14 days before harvest, then measured. No significant differences in "
      "yield (average 97.3 g/plant), THC (average 21.9%) or terpenes across any flush duration. "
      "Flower mineral content did not drop the way the theory requires, nitrogen ran only "
      "~6.7% lower after 14 days, and iron and zinc were actually <em>higher</em> in flushed flower. "
      "A blind consumer panel could not pick the flushed samples, and trended toward preferring the "
      "<em>unflushed</em> one, 36% rated the 0-day smoke smooth versus 19.4% for the 14-day "
      "flush (not statistically significant)" + _c("rxgreen-2019-flushing-trial") + "."),
    figure(L.hbars("Blind smoke panel, Rx Green flushing trial",
            [("0-day flush", 36), ("14-day flush", 19.4)],
            unit="%", note="Share of panellists rating the smoke 'smooth'. Not statistically significant - the point is the direction isn't pro-flush."), 8,
      "The blind panel is the part worth remembering: tasters could not detect flushing, and the "
      "trend ran toward the unflushed flower." + _c("rxgreen-2019-flushing-trial")),
    p("<strong>The Guelph work agrees.</strong> An MSc thesis at the University of Guelph ran "
      "end-of-cycle nutrient-deprivation experiments on medical cannabis and found flushing did not "
      "meaningfully deplete flower elemental content and did not affect yield" + _c("stemeroff-2017-flushing-thesis") +
      ". Neither source is bulletproof. One is a manufacturer white paper on a single "
      "cultivar with a small taste panel, the other a thesis rather than journal-reviewed work "
      "(with a later erratum on a separate chapter), but both independent tests point the "
      "same way, and no controlled study showing the opposite has surfaced."),
    p("<strong>Why the theory was always shaky.</strong> Flushing the root zone rinses the "
      "substrate, not the flower. Minerals already in bud tissue got there through the plant, and "
      "water around the roots does not pull them back out. What actually moves nutrients out of "
      "leaves late in the cycle is senescence-driven remobilisation, the plant's own "
      "salvage program" + _c("maillard-2015-leaf-nutrient-remobilization") + ". Which runs "
      "with or without a flush. What a long flush <em>does</em> do is crash substrate EC and force "
      "the plant onto reserves early, which can accelerate the fade and, pushed hard, trade away "
      "late bulking that trials show is real weight" + _c("massuela-2022-pruning-cbd-yield") + "."),
    table(["Claim", "What testing found", "Verdict"], [
      ["Smoother smoke, better flavour", "Blind panel couldn't detect flushing; trend favoured unflushed", "Unsupported" + _c("rxgreen-2019-flushing-trial")],
      ["Removes minerals from flower", "Flower mineral content essentially unchanged; Fe and Zn higher in flushed", "Contradicted" + _c("rxgreen-2019-flushing-trial") + _c("stemeroff-2017-flushing-thesis")],
      ["White ash proves a clean flush", "Ash colour tracks combustion and moisture, never validated as a flush marker", "Folklore"],
      ["Flushing costs nothing", "Long flushes can force early senescence while weight is still accruing", "False - there is downside" + _c("massuela-2022-pruning-cbd-yield")],
      ["Late-cycle feed tapering", "Uptake falls as the plant senesces; tapering EC to match is agronomy, not flushing", "Reasonable middle ground"],
    ], cls="compact", caption="The flush ledger. The testable claims fail testing; the defensible version is a modest EC taper as appetite falls."),
    callout("evidence", "Where the industry actually sits",
      p("Positions genuinely run both ways. Many commercial SOPs still specify a 7&ndash;14 day "
        "plain-water flush, partly tradition, partly market expectation, and buyers asking "
        "&lsquo;was it flushed?&rsquo; is a real commercial force. Others feed full-strength to the "
        "day of chop, citing the trials above. A common middle path tapers feed EC over the final "
        "week, matching falling uptake without starving the plant. What the evidence rules "
        "out is the strong claim: that a long plain-water flush detectably improves the smoke. If "
        "you flush anyway, keep it short; nobody has shown a benefit that pays for three weeks of "
        "starvation.")),
  ]})

# ---------------------------------------------------------------- 08 the room
SECTIONS.append({"id": "late-environment", "kicker": "08 · The room", "title": "Late-flower environment: taper the room, clamp the ceiling",
  "blocks": [
    p("The environmental job in the last fortnight is asymmetric. The temperature moves are "
      "nice-to-have practitioner practice. The humidity discipline is survival. Get the priority "
      "right: RH ceiling first, everything else after."),
    p("<strong>Temperature: common practice, thin evidence.</strong> Most experienced growers ease "
      "day temperature down a couple of degrees (roughly 26 to 23&deg;C) and let nights run cooler "
      "(21 to 18&deg;C) over the final two weeks. The claimed benefits (preserved terpenes, "
      "tighter buds, purple expression) are mostly untested in controlled cannabis work: "
      "cool nights do trigger purpling in anthocyanin-capable genotypes, but the potency and "
      "terpene-preservation claims remain unverified. The move is low-risk and defensible; just "
      "know one real side-effect: cooler air holds less water, so the same moisture load reads as "
      "<em>higher</em> RH. Every degree you drop makes the humidity job harder, and your "
      "dehumidification has to make up the difference."),
    figure(_FIGS["lateflower_ramp"], 9,
      "A typical last-fortnight ramp: day and night temps taper (practice, not proof) while RH "
      "steps down under a hard ceiling (non-negotiable). Cooling the room raises RH at the same "
      "moisture load, budget dehumidifier capacity for it."),
    p("<strong>Humidity: this is the non-negotiable.</strong> Ripening buds are dense, "
      "self-shading moisture traps, and <em>Botrytis cinerea</em>, bud rot, is the "
      "single most destructive thing that can happen this late. Greenhouse studies of bud rot show "
      "infection risk climbing with humidity and bud density, with the pathogen developing inside "
      "the cola where you cannot see it until the damage is done" + _c("mahmoud-2023-botrytis-budrot") +
      ". Spores are effectively everywhere; epidemiology work frames control as environment and "
      "sanitation, not eradication" + _c("punja2025-budrot-epi") + ". Practically: hold RH "
      "45&ndash;55%, treat 58% as an absolute ceiling, keep air moving through the canopy (not "
      "blasting at it), and watch the lights-off transition, the temperature drop at lights-off "
      "spikes RH and can push dense colas to condensation. That one hour is where most rot starts."),
    figure(L.zones("Late-flower RH bands",
            35, 70, [(35, 45, L.BLUL, "safe but harsh on VPD"), (45, 55, L.GL, "target"),
                     (55, 60, L.AMBL, "caution"), (60, 70, L.REDL, "botrytis territory")],
            unit="% RH",
            note="Ceilings matter more than averages: lights-off spikes and condensation events do the damage."), 10,
      "Run the band, police the ceiling. A 50% average with nightly spikes to 65% is worse than a "
      "steady 55%." + _c("mahmoud-2023-botrytis-budrot")),
    p("<strong>UV &lsquo;finishers&rsquo;: treat the marketing with suspicion.</strong> The pitch"
      ", blast UV in the last weeks to spike THC, keeps failing controlled tests. The "
      "largest indoor light-intensity study found supplemental UV did not increase yield or "
      "cannabinoid content at all" + _c("llewellyn-2022-light-intensity-yield") + ", and a 2024 "
      "spectrum study found UV treatments reduced or left yield unchanged and raised no "
      "cannabinoids, with THC actually <em>lower</em> under the strongest UV-B; the sole positive "
      "was ~20&ndash;30% gains in a few terpenes at very low UVA doses" + _c("huebner2024-uv-spectra") +
      ". If you already own the hardware, a low-dose UVA experiment is defensible. Buying lamps to "
      "chase potency is buying the part of the claim that testing keeps rejecting."),
    callout("warn", "The trade nobody writes on the label",
      p("Every extra ripening day is bought with rot exposure. If your room cannot hold the RH "
        "band (undersized dehumidifier, dense canopy, lights-off spikes) the honest "
        "play is to harvest at the early edge of your window, not to white-knuckle a late chop in "
        "botrytis territory" + _c("punja2025-budrot-epi") + ".")),
  ]})

# ---------------------------------------------------------------- 09 staggered
SECTIONS.append({"id": "staggered-harvest", "kicker": "09 · Staggered harvest", "title": "Cutting the plant in instalments",
  "blocks": [
    p("The vertical gradient is real: top colas get the most light, mature first, and carry the "
      "highest cannabinoid and terpene content, with both falling measurably toward the bottom of "
      "the plant" + _c("namdar-2018-inflorescence-position") + ". A whole-plant chop therefore "
      "harvests the top at peak and the bottom early. The staggered alternative: take the ripe top "
      "third now, then give the suddenly well-lit lower canopy another 4&ndash;10 days to swell and "
      "finish before a second cut."),
    p("It works because the two things the lower canopy lacked, light and time, both "
      "arrive the moment the tops leave, and because late-cycle weight gain is real" + _c("massuela-2022-pruning-cbd-yield") +
      ". The cost is operational: two harvest days, two dry-room loads, longer room occupancy, and "
      "several more days of rot exposure on the remaining canopy. It is a quality play for "
      "small-to-mid rooms, not a free lunch."),
    table(["Factor", "Whole-plant chop", "Staggered (top first)"], [
      ["Lower-bud ripeness", "Cut days early, more larf", "Finishes properly; grade improves"],
      ["Labour + dry room", "One event, one load", "Two events, two loads"],
      ["Room turnover", "Fastest", "+4-10 days occupancy"],
      ["Rot exposure", "Ends at chop", "Continues for the remainder - RH discipline must hold" + _c("punja2025-budrot-epi")],
      ["When it wins", "Big rooms, tight schedules, extract biomass", "Quality-focused rooms with spare days and controlled RH"],
    ], cls="compact", caption="Staggering trades schedule and risk-days for lower-canopy quality. If the room can't hold its RH band, don't stagger."),
    callout("tip", "Do the second read properly",
      p("After the top cut, re-mark scoping spots on the remaining canopy and restart the "
        "two-day loupe cadence. The lower buds accelerate under new light. They often close "
        "the gap faster than the original schedule suggests. And handle the cut surfaces cleanly: "
        "sanitise shears between plants so the first harvest doesn't inoculate the second.")),
  ]})

# ---------------------------------------------------------------- 10 chop day
SECTIONS.append({"id": "day-of-chop", "kicker": "10 · Chop day", "title": "Day-of-chop logistics: the boring list that protects the crop",
  "blocks": [
    p("By chop day the quality is already grown. The job now is purely defensive: move the crop "
      "from room to dry space without bruising it, contaminating it, or stalling it in a bin. "
      "Everything below is decided <em>before</em> the first cut."),
    steps([
      ("Verify the dry space the day before",
       "Dry room running and stable at roughly 15-16 C and ~60% RH (the classic 60/60), dark, "
       "gentle indirect airflow, cleaned and sanitised. Never cut a plant before the place it dries "
       "is proven, a crop waiting in bins while you fix a dehumidifier is a crop composting."),
      ("Final rot scout, then quarantine",
       "Walk every plant with a torch before cutting. Any botrytis, grey fuzz, "
       "brown-from-the-inside bud, colas that pull apart wet, gets cut out first, bagged at "
       "the plant, and removed from the room. Never carry infected material across the canopy, and "
       "never hang it with the clean crop."),
      ("Stage the kit",
       "Sanitised shears (dip between plants), gloves, labels and tags per plant or batch, bins or "
       "hanging lines, scale for wet weights. Decide wet-trim vs dry-trim now, not mid-chop, "
       "the workflow differs from the first cut onward."),
      ("Cut in the right order",
       "One cultivar at a time so genetics never mix. Whole-plant or branch-by-branch per your dry "
       "space. Keep plants off the floor, handle by stem only. Every touch on flower costs "
       "trichomes."),
      ("Weigh and log wet weights",
       "Wet weight per plant or bin, tagged to cultivar and room position. This is the baseline for "
       "dry-down ratio (~10% dry-to-wet is typical) and the start of traceability."),
      ("Hang with space",
       "Colas must not touch each other, contact points dry slowest and rot first. Load the "
       "dry room evenly, close the door, and let the environment do the work. From here, the "
       "<a href='harvest-dry-trim-cure.html'>dry and cure paper</a> takes over."),
    ]),
    p("Two chop-day traditions deserve a flag. <strong>48 hours of darkness before harvest</strong> "
      "(claimed to boost resin) and <strong>harvesting pre-dawn</strong> (claimed to catch peak "
      "terpenes) both lack any controlled cannabis evidence. Neither is harmful, cool, dark "
      "and unstressed is fine for a plant about to be cut, but schedule the chop for when "
      "your team is fresh and the dry room is ready. Those two factors demonstrably matter; the "
      "folklore ones haven't shown up in testing."),
    callout("note", "Mind the room you're leaving",
      p("Removing half a room of transpiring plants crashes the humidity load and the climate "
        "control's assumptions. If other plants remain (staggered harvest, mixed-age rooms), "
        "re-check RH and airflow within the hour, setpoints tuned for a full canopy behave "
        "differently in a half-empty one.")),
  ]})

# ---------------------------------------------------------------- 11 failure modes
SECTIONS.append({"id": "failure-modes", "kicker": "11 · Failure modes", "title": "The six ways the finish goes wrong",
  "blocks": [
    p("Late-flower mistakes cluster hard. Six patterns account for nearly all of them, "
      "three are impatience, two are bad reads, one is neglect."),
    grid([
      card("Harvesting early", "The classic. Pistils half-white, trichomes mostly clear, but the calendar said week 8. "
           "Costs real weight that accrues late" + _c("massuela-2022-pruning-cbd-yield") + " and cuts immature resin. "
           "The fix is boring: scope on cadence, trust the trend, wait for the window.", tag="impatience"),
      card("Chasing amber", "The opposite failure: waiting for 20% amber on a cultivar that barely ambers, while heads "
           "collapse and rot exposure compounds" + _c("punja-2023-trichome-maturation") + ". If cloudy has been maxed "
           "for a week and amber won't come, that plateau is your window.", tag="misread"),
      card("Reading sugar leaves", "Leaf trichomes amber days before calyx trichomes. Reading the pretty frosted leaf "
           "calls the chop early every single time. Calyx dome, mid-cola, fixed spots, nothing else counts.", tag="misread"),
      card("Calendar worship", "Breeder flowering times are marketing medians under someone else's conditions. Same clone, "
           "different rooms, a week or more of spread. Use the number to plan labour, never to cut.", tag="impatience"),
      card("Ignoring mould pressure while waiting", "Every extra day is bought with rot exposure. Waiting for perfect ripeness with RH "
           "bouncing off 65% at lights-off is gambling the whole cola for the last 3% of maturity" + _c("mahmoud-2023-botrytis-budrot") + ". "
           "When the environment can't hold, cut early and clean.", tag="neglect"),
      card("Flush zealotry", "Three weeks of plain water &lsquo;to be safe&rsquo; starves the plant through its final "
           "bulking, forces a hard early fade, and buys smoke quality that blind panels can't detect" + _c("rxgreen-2019-flushing-trial") + ". "
           "If you flush, keep it short.", tag="folklore"),
    ], cols=2),
  ]})

# ---------------------------------------------------------------- 12 troubleshooting
SECTIONS.append({"id": "troubleshooting", "kicker": "12 · Troubleshooting", "title": "Late-flower symptoms, decoded",
  "blocks": [
    p("Quick lookups for the confusing reads. Most of these are the plant and the room disagreeing "
      "with the calendar, believe the plant, then fix the room."),
    table(["What you see", "Most likely cause", "What to do"], [
      ["Week 9+, trichomes cloudy for days, no amber appearing",
       "Genotype that barely ambers; heads will eventually collapse instead",
       "Treat sustained cloudy-max as the window" + _c("punja-2023-trichome-maturation") + ". Don't wait for a colour some cultivars never show"],
      ["Pistils all brown at week 6 but trichomes mostly clear",
       "Stress-browned or pollinated stigmas, not ripeness",
       "Ignore pistils, scope on. Check for seeds and for heat/pollen sources"],
      ["Fresh white pistils erupting from mature buds late",
       "Foxtailing from heat or light stress resetting bud growth",
       "Fix hotspots / lower PPFD; read the original calyxes below the foxtail, not the new growth"],
      ["Amber on sugar leaves, clear-cloudy on calyxes",
       "Normal - leaf trichomes run days ahead",
       "Read only the calyx surface. This gap is why leaf reads chop early"],
      ["Hard crispy fade by week 6, buds still immature",
       "Over-flush, N crash, or root-zone EC collapse - senescence started early",
       "Restore modest feed; accept some cost. Next round, taper instead of starving" + _c("maillard-2015-leaf-nutrient-remobilization")],
      ["Grey fuzz or brown mush inside a cola while you wait for ripeness",
       "Botrytis bud rot - it starts inside, where RH spikes condense",
       "Cut out and bag infected colas immediately; drop RH, add airflow; if spreading, harvest now" + _c("mahmoud-2023-botrytis-budrot")],
      ["Buds seem to stop swelling, trichomes stall for a week+",
       "Cold room, crashed feed, or the plant is simply done",
       "Verify temps and EC first. If the room is right and trichomes sit at cloudy-max, that's the window - cut"],
    ], cls="compact", caption="The two dangerous rows are the last ones: a stalled-but-clean plant costs patience, botrytis costs the crop."),
  ]})

# ---------------------------------------------------------------- 13 mental model
SECTIONS.append({"id": "mental-model", "kicker": "13 · The mental model", "title": "Ripeness is a distribution, not a state",
  "blocks": [
    p("If one idea from this paper survives contact with your first harvest, make it this one:"),
    callout("key", "The distribution model",
      p("A plant is never &lsquo;ripe&rsquo;. It is a population of millions of trichomes spread "
        "across a vertical gradient, each gland moving clear &rarr; cloudy &rarr; amber on its own "
        "schedule" + _c("livingston-2020-trichome-maturation") + _c("namdar-2018-inflorescence-position") +
        ". The harvest call is choosing which slice of that distribution to freeze: hash-makers "
        "freeze it cloudy, flower growers let the amber tail grow first, extractors barely care. "
        "And botrytis is the deadline that truncates the whole curve, the only signal that "
        "outranks the loupe.")),
    p("Everything else in the paper is that model plus logistics. Scoping cadence samples the "
      "distribution honestly. Product windows pick the target slice. The RH ceiling defends your "
      "right to keep waiting. Staggering harvests the gradient in two slices instead of averaging "
      "it. And the flush debate stops mattering once you see that nothing you pour into the "
      "substrate in the last week repaints the trichomes" + _c("rxgreen-2019-flushing-trial") + "."),
    kv([
      ("Scope cadence", "Every 2 days from week 7, logged"),
      ("Scope spots", "2-3 marked mid-cola calyx sites + one top cola"),
      ("Hash call", "Cloudy max, minimal amber"),
      ("Flower call", "Cloudy-dominant, 5-15% amber"),
      ("RH band / ceiling", "45-55% target, 58% absolute ceiling"),
      ("Dry space ready", "15-16 C / ~60% RH, running before the first cut"),
    ]),
    p("From here the crop stops being grown and starts being preserved: "
      "<a href='harvest-dry-trim-cure.html'>harvest, dry, trim and cure</a> covers the next "
      "fortnight, and <a href='mould-risk.html'>the mould-risk paper</a> covers the enemy that "
      "follows the crop into the dry room. Cut clean, cut in the window, and let the loupe, "
      "not the calendar, not the forum, make the call."),
  ]})
