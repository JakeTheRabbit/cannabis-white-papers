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
TITLE = "The one steering law: coco, rockwool, soil & water"
EYEBROW = "Flowering · Crop steering"
SUB = ("Coco, rockwool, soil and plain water are not four separate skills. They are one way of "
       "steering a plant with water, running on four different sponges. Learn the steering once, with "
       "pictures and no jargon, and you can grow in any of them, because the sponge only changes the numbers.")
META = [("droplet", "Flowering"), ("image", "31 diagrams"),
        ("quote", "Peer-reviewed · 9 sources"), ("clock", "~22 min read")]
RELATED = ["coco-crop-steering", "rockwool-crop-steering", "substrates-overview",
           "root-zone-teros12", "smart-watering-vrwe", "f2-crop-steering"]
REF_IDS = ["caplan2019-drought", "welling2025-aba", "stack2024-drought", "hilhorst2000-ec",
           "abad2005-coir", "noguera2003-cec", "malik2025-media",
           "szerement-dielectric-2019", "tdr-fdr-soil-review-2024"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

# ---------------------------------------------------------------- 0 promise
SECTIONS.append({"id": "the-promise", "kicker": "Start here", "title": "The one sentence you’ll leave with",
  "blocks": [
    lead("A cannabis plant can pour its energy into <strong>leaves</strong> &mdash; a bigger, bushier green "
         "plant &mdash; or into <strong>flower</strong>: the sticky buds you actually harvest. "
         "&lsquo;Steering&rsquo; just means using water to nudge the plant toward one or the other."),
    callout("tip", "Think of it like driving",
      p("Whether you grow in coco, rockwool, soil or plain water, you steer the exact same way &mdash; like "
        "a hatchback, a truck and a sports car all use one wheel, one pedal, one gear stick. You don&rsquo;t "
        "relearn <em>driving</em> for each car. You won&rsquo;t relearn <em>steering</em> for each sponge.")),
    fig("fig-0-leaves-vs-flower",
        "Leaves means a bigger green plant; flower means the buds you harvest. Steering just slides the "
        "plant between the two."),
    p("The three controls never change. Every sponge is driven with the same three:"),
    ul(["<strong>The wheel</strong> &mdash; how full the sponge is right now (growers call it VWC). "
        "The one number you steer on.",
        "<strong>The engine</strong> &mdash; the daily <strong>drink-down</strong> (growers call it dryback): "
        "how far you let the plant wring the sponge dry each day. Your most powerful lever.",
        "<strong>The second dial</strong> &mdash; feed strength (growers call it EC): how strong you make the feed."]),
    p("The sponge itself &mdash; coco, rockwool, soil, water &mdash; is just the <strong>gearbox</strong> "
      "underneath. Swap it and the controls don&rsquo;t change; only the numbers do."),
    fig("fig-1-car-controls",
        "You drive every sponge with the same three controls; the sponge is only the gearbox underneath."),
    p("Here is the whole routine you&rsquo;re about to learn. Each morning when the lights come on: let the "
      "sponge dry a little, fill it back up in small sips, hold it steady through the day, then let it dry "
      "out overnight &mdash; and start again tomorrow. Everything else in this guide is detail hung off this loop."),
    fig("fig-2b-the-loop-hero",
        "The entire job in one daily ring: fill up, drink down, hold, dry, repeat."),
    callout("note", "What&rsquo;s optional here",
      p("Sections 1&ndash;6 and the last one teach you to grow by hand. The two <strong>nerd-bonus</strong> "
        "sections on moisture sensors and auto-watering robots are skippable &mdash; if you&rsquo;re growing "
        "by hand, you lose nothing.")),
    callout("key", "In one sentence",
      p("There&rsquo;s one way to steer a plant with water &mdash; toward leaves or toward flower &mdash; and "
        "coco, rockwool, soil and water just change the numbers, not the steering.")),
  ]})

# ---------------------------------------------------------------- 1 sponge
SECTIONS.append({"id": "everything-is-a-sponge", "kicker": "The one spine image", "title": "Everything is a sponge",
  "blocks": [
    callout("tip", "Think of it like a kitchen sponge",
      p("Hold a kitchen sponge under the tap until it&rsquo;s full, then let it drip. Every way of growing "
        "&mdash; coco, rockwool, soil, even roots dangling in water &mdash; is that same sponge: a fixed "
        "number of little holes that hold either water or air. From here on, one picture: the sponge.")),
    p("A growing medium is just the stuff the roots live in. The total room inside is <strong>fixed</strong>, "
      "and every hole holds either water or air. Push water in and you squeeze air out. <strong>More water "
      "always means less air.</strong>"),
    p("That matters because roots need to <em>breathe</em> as much as drink. Roots drown if it stays too wet "
      "and stall if it stays too dry; every sponge just sits at a different default point on that "
      "water-versus-air see-saw."),
    fig("fig-3-sponge-seesaw",
        "The room inside a sponge is fixed, so you cannot add water without pushing out the air the roots breathe."),
    p("Different sponges keep wildly different amounts of air even when soaking wet" + _c("malik2025-media") +
      ", and that single fact decides how easy each one is to overwater."),
    fig("fig-4-air-when-wet",
        "Coco keeps about a fifth of its room as air even when soaked; rockwool only a tenth &mdash; which is "
        "why coco is so hard to drown."),
    callout("note", "Real numbers",
      ul(["Coco air when soaked: about <strong>22%</strong>" + _c("abad2005-coir") +
          " &middot; rockwool only about <strong>10%</strong>",
          "Peat keeps about <strong>18&ndash;25%</strong> air when wet &middot; coco&rsquo;s total room is about 94&ndash;96%"])),
    p("There&rsquo;s a <strong>second, hidden trait</strong> too, just as important: how much a sponge "
      "<em>forgives a feeding mistake</em>. Some sponges soak up your mistake and protect you" +
      _c("noguera2003-cec") + "; others punish you instantly. We&rsquo;ll measure this properly later &mdash; "
      "for now, just &lsquo;forgiving&rsquo; versus &lsquo;harsh&rsquo;."),
    fig("fig-5-cushion-spectrum",
        "The same feeding mistake is cushioned by forgiving sponges (soil, coco) and breaks straight through "
        "harsh ones (rockwool, water)."),
    callout("key", "In one sentence",
      p("Every way of growing is one sponge with a fixed amount of room, and watering just decides how much "
        "of that room is water versus air.")),
  ]})

# ---------------------------------------------------------------- 2 wheel & engine
SECTIONS.append({"id": "wheel-and-engine", "kicker": "The wheel and the engine", "title": "Water is the steering wheel, the drink-down is the engine",
  "blocks": [
    callout("tip", "Think of it like wringing a sponge",
      p("Water isn&rsquo;t just food &mdash; it&rsquo;s the steering wheel. Picture the plant gripping the "
        "sponge and wringing a little water out each day. How hard you let it wring is the engine of steering. "
        "A gentle wring grows leaves; a hard wring grows flowers.")),
    p("<strong>How-full %</strong> is the one number you steer on &mdash; how full the sponge is right now. "
      "60% means water fills 60 of every 100 holes. The <strong>drink-down</strong> is the fall in how-full % "
      "between waterings: the high after a sip, minus the low before the next."),
    callout("note", "Say it in points, never a bare &lsquo;%&rsquo;",
      p("Always count the drink-down in percentage <strong>POINTS</strong>: 78% down to 58% is a "
        "<strong>20-point</strong> drink-down (a fall of 20 on the 0&ndash;100 scale). A bare "
        "&lsquo;20%&rsquo; is ambiguous, so this guide always says points.")),
    fig("fig-6-dryback-wring",
        "The drink-down is simply how far the water level drops before you water again &mdash; here, 78% down "
        "to 58% is a 20-point drink-down (a rockwool example)."),
    p("<strong>Why drying steers the plant.</strong> A little daily thirst makes the plant act as if summer "
      "is ending, so it hurries to make flowers instead of more leaves" + _c("caplan2019-drought") +
      ". You&rsquo;re gently tapping a &lsquo;hurry up and flower&rsquo; button, and it works through a stress "
      "hormone the plant releases under mild water deficit" + _c("welling2025-aba") + ". It&rsquo;s a "
      "<strong>nudge, not damage</strong> &mdash; you never need the hormone&rsquo;s name to grow."),
    fig("fig-7b-thirst-button",
        "A little thirst makes the plant act as if summer is ending, flipping an inner switch from "
        "grow-leaves to make-flowers &mdash; a gentle nudge, not harm."),
    p("Bigger, deeper drink-downs push flower (make-the-buds); smaller drink-downs, kept wetter, push leaves "
      "and size (grow-the-body). Same lever, different depth. And it&rsquo;s a <strong>bias built over "
      "days</strong>, never an overnight switch: you tip the odds one notch at a time, like turning a dimmer."),
    fig("fig-7c-bias-not-switch",
        "You never flip the plant overnight; you nudge a dimmer one notch a day, across the week, from "
        "mostly-leaves toward mostly-flower."),
    callout("warn", "A drink-down is not a drought",
      p("The difference is dose and timing. Stop it on time and you keep your yield; run it too far and you "
        "crash both yield and quality" + _c("stack2024-drought") + ". Always water before the plant wilts. "
        "Steer with a scalpel, not a hammer.")),
    fig("fig-8-dryback-not-drought",
        "A healthy drink-down is caught and refilled before the plant wilts; a drought keeps falling through "
        "the red zone and crashes the crop."),
    callout("note", "Real numbers (rockwool example &mdash; yours will differ)",
      ul(["Leaves mode: 5&ndash;15 point drink-down &middot; flower mode: 20&ndash;30 point drink-down",
          "Young / early: 5&ndash;10 points &middot; late veg &amp; bulking: 10&ndash;15 points &middot; the "
          "overnight dry-down adds another 5&ndash;15 and re-airs the roots",
          "A real finding: easing the overnight dry-down to leave it ~10% wetter actually <em>lifted</em> "
          "medicinal yield &mdash; some dry-down is essential, too much hurts."])),
    callout("key", "In one sentence",
      p("You steer the plant by how hard you let it wring the sponge dry each day &mdash; gently for leaves, "
        "hard for flowers.")),
  ]})

# ---------------------------------------------------------------- 3 second dial
SECTIONS.append({"id": "the-second-dial", "kicker": "The second dial", "title": "Feed strength, and why the sponge gets saltier as it dries",
  "blocks": [
    callout("tip", "Think of it like squash on a windowsill",
      p("Make a glass of squash, then leave it on a sunny windowsill. As the water evaporates, the drink gets "
        "stronger and sweeter &mdash; same sugar, less water. The root zone does exactly this with the feed.")),
    p("<strong>Feed strength</strong> (growers call it EC) is how strong the fertiliser feed is around the "
      "roots &mdash; higher means stronger and saltier. Here is the one physical fact that ties it to "
      "everything else: as the sponge dries, the water leaves but the food stays behind, so the feed "
      "concentrates and strengthens on its own" + _c("hilhorst2000-ec") + ". A deep drink-down for flower is "
      "therefore partly a <em>feed-strength squeeze</em>, not only a water one. Water and feed are really the "
      "<strong>same lever</strong>."),
    fig("fig-9-squash-concentration",
        "Count the food dots &mdash; always six. As the water drops, the same food crowds closer, so the feed "
        "gets stronger on its own."),
    p("So read the two numbers as <strong>one story</strong>: how-full % falling is the plant drinking (good, "
      "until it falls too far); feed drifting stronger as it dries is normal; a big strength jump means too "
      "salty (water more to dilute); feed drifting weaker over days means the plant is eating faster than you "
      "feed (feed a bit stronger). Weaker and wetter pushes leaves; stronger and drier pushes flower."),
    fig("fig-10b-ec-vwc-together",
        "As the pot dries the feed climbs; every sip resets both &mdash; wetness and feed strength move together."),
    callout("note", "Real numbers (rockwool / water &mdash; yours will differ)",
      ul(["Feed roughly <strong>doubles</strong> as the sponge dries to a third left: a feed set at 3.0 can "
          "read 5.0 in the block by late afternoon",
          "Leaves mode ~3.0 &middot; flower mode ~4.5&ndash;6.0 &middot; healthy daily range ~2&ndash;6",
          "The feed reading gets unreliable once the sponge is nearly dry"])),
    callout("note", "Coco growers, one note",
      p("Coco&rsquo;s forgiving sponge soaks up some of the extra feed, so the strength climbs <strong>more "
        "gently</strong> than in rockwool or plain water. The squash picture is the rockwool/water version "
        "&mdash; coco&rsquo;s is softer.")),
    callout("key", "In one sentence",
      p("When the sponge dries, the water leaves but the food stays &mdash; so drying the plant out also makes "
        "its feed stronger. Water and feed are the same lever.")),
  ]})

# ---------------------------------------------------------------- 4 the cliff
SECTIONS.append({"id": "the-cliff", "kicker": "The two limits", "title": "The cliff: the ‘full’ mark and the danger line",
  "blocks": [
    callout("tip", "Think of it like a lift in a building",
      p("The top floor is &lsquo;full&rsquo; &mdash; fill past it and water just spills out the bottom. The "
        "basement is a trap door: drop the sponge below it and it bakes dry, water runs straight past the "
        "roots, and the dripper can&rsquo;t save it. You steer in the floors between, never hitting either.")),
    p("The <strong>&lsquo;full&rsquo; mark</strong> (growers call it field capacity) is the wettest the sponge "
      "gets after it stops dripping &mdash; your daily ceiling to refill toward. Crucially, it&rsquo;s a "
      "property of <strong>your exact pot and sponge</strong>, not a textbook number, and it shrinks as roots "
      "fill the pot. You learn it from a handful of real waterings."),
    p("The <strong>danger line</strong> (growers call it the recovery floor) is a hard safety limit: dry past "
      "it and the sponge stops soaking water back up &mdash; water just tunnels straight through. From the "
      "dripper that&rsquo;s unfixable; it needs a hand-soak or a fresh sponge. The drink-down is your "
      "steering; the danger line is your safety limit &mdash; two different numbers."),
    fig("fig-11-lift-shaft-limits",
        "A &lsquo;full&rsquo; mark on top you never overflow, a danger line at the bottom you never fall "
        "through &mdash; steer in the safe band between them."),
    fig("fig-12-channeling-cracked-core",
        "Dried past the danger line, the core bakes and cracks, so poured water tunnels down the cracks and "
        "out the bottom while the middle stays bone dry."),
    p("One more friend: the small daily <strong>drip-out</strong> (growers call it runoff) &mdash; about "
      "10&ndash;20% of what you fed, draining out the bottom. It&rsquo;s <em>not</em> waste. It washes out "
      "stacked-up salt, and it&rsquo;s your dipstick for reading the sponge&rsquo;s true feed strength."),
    fig("fig-13-runoff-dipstick",
        "The few drops that run out are not wasted &mdash; they carry off built-up salt and let you read the "
        "real feed strength at the roots."),
    callout("note", "Real numbers (rockwool example &mdash; yours will differ)",
      ul(["Rockwool danger line ~<strong>25&ndash;30%</strong> how-full &middot; working band ~55&ndash;92%",
          "A healthy daily range often sits ~30&ndash;70% how-full &middot; sponge temperature 20&ndash;26&deg;C",
          "Daily drip-out at &lsquo;full&rsquo; ~10&ndash;20% &middot; learn your &lsquo;full&rsquo; mark from "
          "about 5 real, agreeing waterings"])),
    callout("key", "In one sentence",
      p("There&rsquo;s a &lsquo;full&rsquo; mark you never overflow and a danger line you never fall through "
        "&mdash; and steering means swinging the sponge safely between them.")),
  ]})

# ---------------------------------------------------------------- 5 four beats
SECTIONS.append({"id": "one-day-four-beats", "kicker": "The daily rhythm", "title": "One day, four beats",
  "blocks": [
    callout("tip", "Think of it like breathing on a schedule",
      p("A small morning exhale (dry down a little), a big drink (fill up in sips), steady breathing all day "
        "(hold the band), then one deep overnight breath (the big dry-down) that pulls fresh air back to the "
        "roots. Same four beats, every single day.")),
    p("You don&rsquo;t water at random &mdash; you water on a fixed <strong>four-beat schedule</strong> tied "
      "to the lights. Growers label the beats P0, P1, P2, P3; you can just call them:"),
    steps([
      ("Dry a little", "At lights-on, let the sponge dry down a small amount before the first sip &mdash; the first deliberate squeeze of the day."),
      ("Fill up", "Refill in small, slightly growing sips until you hit the day&rsquo;s &lsquo;full&rsquo; peak. Stop the moment you hit it &mdash; you&rsquo;ll rarely give every planned sip."),
      ("Hold steady", "Keep it in a band all day, topping up when it dips, nudging feed strength to steer."),
      ("Wind down", "Stop before lights-off and coast through the night on emergency-only top-ups, letting the big overnight drink-down reset everything."),
    ]),
    fig("fig-14-p0p3-clock",
        "Every lights-on day is the same four beats, in the same order: dry a little, fill up, hold steady, wind down."),
    p("A <strong>sip</strong> (growers call it a shot) is one short timed splash, sized as a small percent of "
      "the sponge&rsquo;s volume. How long to run it, in seconds, is worked out like a recipe &mdash; from pot "
      "size, dripper speed and number of drippers. The controller does that maths; you just give it the three ingredients."),
    p("The healthy signature is a <strong>zig-zag</strong> graph (a sawtooth): a gradual fall (drink-down), a "
      "sharp rise (sip), over and over. A flat line, or a line that only falls, means watering isn&rsquo;t "
      "actually happening &mdash; something&rsquo;s broken."),
    fig("fig-15-sawtooth-heartbeat",
        "If the water graph zig-zags like teeth, steering is working; a line that only falls and flatlines is a fault."),
    p("Here&rsquo;s the punchline that <em>is</em> the one steering law, visible in one room: "
      "<strong>leaves mode and flower mode run the exact same four beats.</strong> Only the target numbers "
      "&mdash; drink-down depth, feed strength, sip size &mdash; change. Never the rhythm."),
    fig("fig-16-veg-gen-same-loop",
        "Leaves mode and flower mode are the same daily loop &mdash; you only slot in a different numbers-card."),
    callout("warn", "Never run factory defaults un-checked",
      p("A placeholder of &lsquo;50% full / 50% drink-down&rsquo; is not your sponge. Learn your own "
        "&lsquo;full&rsquo; mark and danger line first, then set the targets to them.")),
    callout("key", "In one sentence",
      p("Every steered day is the same four beats &mdash; dry a little, fill up, hold steady, wind down "
        "overnight &mdash; and that repeating zig-zag is steering working.")),
  ]})

# ---------------------------------------------------------------- 6 gearbox
SECTIONS.append({"id": "sponge-is-the-gearbox", "kicker": "The keystone", "title": "The sponge is the gearbox",
  "blocks": [
    callout("tip", "Think of it like a gearbox",
      p("You already know how to drive. A gearbox sits between your foot and the wheels &mdash; same pedal, "
        "but it decides how your push turns into speed. The sponge is that gearbox between your watering and "
        "what the roots feel. Swap it and you don&rsquo;t relearn driving &mdash; you just read the new "
        "gearbox&rsquo;s label.")),
    p("This is the keystone. The sponge takes your watering decision and <strong>changes it by fixed "
      "amounts</strong> before the roots feel it &mdash; same input, different output per sponge. So learning "
      "a new sponge is never learning a new way to steer. It&rsquo;s reading the new sponge&rsquo;s label and "
      "dialling in <strong>four numbers</strong>: how wet &lsquo;full&rsquo; is, how much air it keeps when "
      "full, how much it forgives a bad feed, and how dry is too dry."),
    fig("fig-17-gearbox-swap",
        "Your watering goes in, the sponge-gearbox changes it, and that is what the roots feel &mdash; same "
        "driver and wheel, four swappable gearboxes."),
    p("Every sponge fills in the <strong>same form</strong> &mdash; only the numbers differ. That&rsquo;s the "
      "thesis made literal:"),
    fig("fig-18-gearbox-label-cards",
        "Four identical spec cards: every sponge has the same rows (air, forgiveness, prep, danger line), just "
        "with different numbers filled in."),
    table(["What it does", "Coco", "Rockwool", "Living soil", "Plain water (tank)"], [
      ["Air when soaked", "~22% &mdash; keeps the most air, very hard to overwater", "~10% &mdash; drowns easily, holds the most water", "airier than rockwool (peat ~18&ndash;25%)", "roots hang in water; air from an air pump"],
      ["Forgiveness (cushions a bad feed)", "a lot &mdash; a built-in shock absorber", "almost none &mdash; what you set is what the plant gets", "self-fixing &mdash; life &amp; minerals steady it in minutes", "none &mdash; the tank is the only buffer"],
      ["Danger line / main failure", "fades gently; feed reading unreliable when nearly dry; steals cal-mag if not pre-charged", "sharp cliff ~25&ndash;30%; water tunnels below it; felt the same hour", "forgiving; no sharp cliff; overwatering hides then compounds", "no dryness cliff but a heat one: root rot above ~23&deg;C within a day"],
      ["Prep / starting pH", "pre-soak in cal-mag 8&ndash;24 h; feed pH 5.8&ndash;6.2", "starts near pH 8, condition to ~5.5; run 5.5&ndash;6.0; reusable ~3 yrs", "settles its own pH ~5.2&ndash;6.5; usually don&rsquo;t pH the input", "hold pH 5.5&ndash;6.0, tank 18&ndash;20&deg;C, air pump always on"],
      ["Good for a beginner?", "<strong>yes</strong> &mdash; just charge it before planting", "precise but unforgiving; earn your way to it", "<strong>yes</strong> &mdash; top of the forgiveness ladder", "no &mdash; expert only"],
    ], caption="Same fields, different numbers. Picking a sponge isn&rsquo;t learning new steering &mdash; it&rsquo;s choosing your failure mode" + _c("malik2025-media") + "."),
    p("Notice the trade hidden in that table: <strong>the more control a sponge gives you, the less it "
      "protects you from yourself.</strong> So beginners start at the forgiving top of the ladder and earn "
      "their way down."),
    fig("fig-19-forgiveness-ladder",
        "Sponges ranked from most forgiving (living soil, top) to most demanding (plain water, bottom). Start at the top."),
    fig("fig-19b-which-medium-pick",
        "First ever grow? Start with living soil or coco. Earn your way to rockwool and water later."),
    callout("tip", "Start here &mdash; a recipe you can run tonight (coco)",
      table(["", "Leaves mode (grow-the-body)", "Flower mode (make-the-buds)"], [
        ["Lights", "12 / 12", "12 / 12"],
        ["&lsquo;Full&rsquo; mark", "learn per pot", "learn per pot"],
        ["Drink-down", "5&ndash;15 points", "20&ndash;30 points"],
        ["Feed strength", "~3.0", "4.5&ndash;6.0"],
        ["Sips", "many, small", "fewer, bigger"],
      ], caption="Start with this, watch one week, then change one thing at a time.")),
    callout("key", "In one sentence",
      p("The sponge is a gearbox that only changes four numbers and which mistake will hurt you &mdash; the "
        "steering itself never changes.")),
  ]})

# ---------------------------------------------------------------- 7 nerd: probe
SECTIONS.append({"id": "the-probe-can-lie", "kicker": "Nerd bonus — skip if growing by hand", "title": "The dashboard can lie",
  "blocks": [
    callout("note", "Optional section",
      p("Skip this whole part unless you want to understand the sensors. Growing by hand, you don&rsquo;t need "
        "it. The one idea worth taking: your moisture number is a <strong>good guess, not gospel</strong> "
        "&mdash; watch the trend, and get a second opinion before you trust it.")),
    p("How a probe even feels water: water reacts to the probe&rsquo;s tiny electric field <strong>far more "
      "strongly</strong> than dry sponge or air do" + _c("szerement-dielectric-2019") + ". That huge gap is "
      "the whole trick, and it works the same in coco, rockwool and soil."),
    fig("fig-20-permittivity-gap",
        "Water reacts to the probe&rsquo;s electric field far more than dry sponge or air &mdash; that gap is "
        "how a buried probe feels water it cannot see."),
    p("<strong>Precise is not the same as right.</strong> The probe shows lots of decimals but can still be "
      "off by a few points" + _c("tdr-fdr-soil-review-2024") + " &mdash; like a clock that ticks every second "
      "but is set ten minutes fast. Until you calibrate it to your sponge, you may be steering inside the error."),
    fig("fig-21-resolution-vs-accuracy",
        "A number with many decimals can still be wrong &mdash; like a smooth-ticking clock set ten minutes "
        "fast &mdash; until you calibrate it."),
    p("And one probe is one <strong>local witness</strong> &mdash; it only feels a soda-can-sized spot, not "
      "the whole pot. Never wire one probe straight to a valve; get a second witness (water dripping out, or "
      "pot weight) before water moves. Steer on the <em>shape</em> of the drink-down, not the exact number."),
    fig("fig-23-one-witness-second-witness",
        "One probe lights only a soda-can-sized spot, so confirm with a second witness &mdash; drip-out or pot "
        "weight &mdash; before any water moves."),
    callout("warn", "Worth pinning even if you skip the rest",
      p("If your drink-down is <strong>smaller than your sensor&rsquo;s error</strong>, you&rsquo;re guessing. "
        "Calibrate the sensor, or use a bigger drink-down.")),
    callout("key", "In one sentence",
      p("The probe is a fuel gauge, not a dipstick &mdash; it can read a bit wrong, so trust the trend and get "
        "a second opinion before you water.")),
  ]})

# ---------------------------------------------------------------- 8 nerd: brain
SECTIONS.append({"id": "the-auto-waterer-brain", "kicker": "Nerd bonus — skip if growing by hand", "title": "The brain behind an auto-waterer",
  "blocks": [
    callout("note", "Optional section",
      p("Skip this unless you&rsquo;re building an automatic waterer. By hand, <em>you</em> are the brain and "
        "the rest of the guide is enough. The single reassuring idea: never trust one sensor, and never flood "
        "or starve &mdash; when unsure, do the safe thing.")),
    p("A good auto-waterer keeps a running <strong>water tally</strong>, like a piggy bank: water IN (the "
      "dripper sips, known precisely) minus water OUT (the plant breathing water out, like sweating, plus what "
      "drains) equals the real water in the pot. The sensor becomes one <em>opinion</em> to double-check, not "
      "the boss."),
    fig("fig-25-water-bank-account",
        "You can know the water level by adding what went in and subtracting what left &mdash; a piggy bank "
        "&mdash; instead of trusting one twitchy sensor."),
    p("Every guess carries a <strong>confidence level</strong> &mdash; high when the clues agree, low when "
      "they disagree. High lets the robot give a full sip; medium only a small safe sip; low means wait or ask "
      "a human."),
    fig("fig-26-confidence-dial",
        "Only water a full amount when the clues agree; when they don&rsquo;t, do the safe thing &mdash; a "
        "small sip, wait, or ask a human."),
    p("The whole decision is just three choices, all fenced by one rule. A lying sensor can only ever make the "
      "robot <em>more</em> careful &mdash; never trick it into overwatering."),
    fig("fig-27-three-branch-tree",
        "The auto-waterer only ever waters a measured bit, waits, or asks you &mdash; all fenced by &lsquo;never flood, never starve&rsquo;."),
    p("And the reassuring part: <strong>the brain works the same no matter the sponge.</strong> The same "
      "check-the-clues, keep-a-tally, gate-on-confidence routine runs identically for coco, rockwool, soil and "
      "water. The sponge only changes the numbers it learns &mdash; never the logic."),
    callout("key", "In one sentence",
      p("An auto-waterer keeps a water piggy-bank, attaches a confidence to its guess, and only ever errs "
        "toward &lsquo;never flood, never starve&rsquo; &mdash; on any sponge.")),
  ]})

# ---------------------------------------------------------------- 9 one law
SECTIONS.append({"id": "one-law-any-sponge", "kicker": "It all snaps together", "title": "One law, any sponge",
  "blocks": [
    callout("tip", "Step back and look",
      p("Past the dashboard, the gearbox, all of it &mdash; you see one grower doing one thing: watching the "
        "sponge, deciding, watering a little, and letting it dry. Same wheel, same lever, same dial in every "
        "sponge. Now you can grow in any of them.")),
    p("Everything you learned stacks into one machine: the sponge (gearbox), then how-full % (the wheel), then "
      "the drink-down (the engine), then feed strength (the second dial), all running on the four-beat daily "
      "routine. The probe and the auto-brain are optional side-modules &mdash; bolt them on only if you automate."),
    p("The same daily zig-zag works in every sponge &mdash; only the numbers shift it:"),
    fig("fig-30-one-law-overlay",
        "The same daily shape runs in coco, rockwool, soil and water &mdash; only each sponge&rsquo;s own "
        "&lsquo;full&rsquo; mark, danger line and feed strength change."),
    p("Across a whole grow the drink-down has the <strong>same shape on every sponge</strong> &mdash; gentle "
      "and wet early, drier and deeper through mid-flower, easing off near the end. Leaves mode is just gentle "
      "cruising; flower mode is firmer driving &mdash; on the same road."),
    fig("fig-31-whole-grow-arc",
        "Across the whole grow you steer the same way &mdash; gentle early, deepest in mid-flower, easing at "
        "the end &mdash; with feed strength climbing alongside."),
    fig("fig-31b-real-plant-strip",
        "What the dials actually do to a living plant &mdash; seedling, leafy body, fat flowers, ripening "
        "&mdash; start to finish."),
    callout("note", "Real numbers",
      ul(["Forgiveness ladder, most to least: living soil &rarr; coco &rarr; peat &rarr; rockwool &rarr; plain water",
          "Whole-grow rockwool arc: veg gentle; flower wk1&ndash;3 drink-down 10&ndash;18 points; wk4&ndash;6 "
          "deepest, 20&ndash;30 points and feed strongest; wk7&ndash;8 eases to 18&ndash;25 points",
          "Keeping the daytime a bit wetter can give higher yield at the same quality across most of flowering "
          "&mdash; steer by timing and drink-down, not by starving."])),
    p("There&rsquo;s no magic recipe. Start on the forgiving end (living soil or coco), get a probe on the "
      "root zone, learn what <strong>one normal day</strong> looks like, then change one thing at a time. That "
      "discipline &mdash; not a number &mdash; is what makes any sponge repeatable. To go deeper, read the "
      "<a href='coco-crop-steering.html'>coco crop steering</a> and "
      "<a href='rockwool-crop-steering.html'>rockwool crop steering</a> papers, how the "
      "<a href='root-zone-teros12.html'>root-zone sensor</a> really sees, and the "
      "<a href='smart-watering-vrwe.html'>smart watering</a> brain."),
    callout("key", "The promise, now earned",
      p("Steering is one law; the sponge only changes the constants.")),
  ]})

# ---------------------------------------------------------------- glossary
SECTIONS.append({"id": "plain-words", "kicker": "Plain-words glossary", "title": "Every term, in plain English",
  "blocks": [
    p("If a word ever felt like jargon, it&rsquo;s here in plain words. Grower&rsquo;s term first, what it "
      "really means second."),
    defterm("Crop steering", "Controlling when and how much you water to nudge a plant toward leaves (a bigger green plant) or toward flower (the buds you harvest). A gentle bias built over days, not a switch you flip overnight."),
    defterm("Growing medium / substrate (the sponge)", "The stuff a plant&rsquo;s roots live in &mdash; coco, rockwool, soil or a tank of water. Throughout this paper we just call it &lsquo;the sponge&rsquo;."),
    defterm("How-full % (VWC)", "How full the sponge is with water, as a percent of its space. 60% means water fills 60 of every 100 holes. The steering-wheel position &mdash; the one number you steer on."),
    defterm("Drink-down (dryback)", "The fall in how-full % between waterings &mdash; the high minus the low, counted in percentage POINTS (78% to 58% is a 20-point drink-down). How hard the plant wrings the sponge. The single most important steering tool."),
    defterm("Percentage points vs percent", "We always count the drink-down in POINTS: 78 down to 58 is a fall of 20 points. A bare &lsquo;20%&rsquo; is ambiguous, so this paper never writes a bare &lsquo;%&rsquo; for a drink-down."),
    defterm("Feed strength (EC)", "How strong the fertiliser feed is around the roots. Higher means stronger and saltier. It rises on its own as the sponge dries, because the water leaves but the food stays. (Electrical conductivity, in mS/cm &mdash; think of it as a 1-to-10 strength scale.)"),
    defterm("The &lsquo;full&rsquo; mark (field capacity)", "The wettest the sponge gets right after it stops dripping. Your daily &lsquo;full&rsquo; mark. A property of your exact pot and sponge, not a textbook number, and it shrinks as roots fill the pot."),
    defterm("The danger line (recovery floor)", "The hard line the drink-down must never cross (about 25&ndash;30% full in rockwool). Below it the sponge stops soaking water back up and water tunnels straight through &mdash; the dripper can&rsquo;t fix it."),
    defterm("Leaves mode (vegetative)", "Steering the plant toward leaves, stems and size &mdash; kept wetter, with a small drink-down, a weaker feed and many small sips. &lsquo;Grow-the-body.&rsquo;"),
    defterm("Flower mode (generative)", "Steering toward flower, density and resin &mdash; let drier, with a bigger drink-down, a stronger feed and fewer larger sips. &lsquo;Make-the-buds&rsquo; &mdash; the part you harvest."),
    defterm("The thirst alarm (ABA)", "The plant&rsquo;s stress hormone. A little controlled thirst makes the plant release it, which nudges the plant away from leaves and toward flower and resin &mdash; the reason a drink-down steers. You never measure it."),
    defterm("The four daily beats (P0&ndash;P3)", "The four beats of every steered day: dry a little at lights-on, fill up to the &lsquo;full&rsquo; mark in small sips, hold the band all day, then wind down and let the big overnight drink-down reset everything."),
    defterm("Sip (shot)", "One small timed splash of water, sized as a percent of the sponge&rsquo;s volume. Steering replaces one big daily soak with several small sips; how long each runs is worked out from pot size, dripper speed and dripper count."),
    defterm("Zig-zag / sawtooth", "The shape of a healthy how-full graph &mdash; a gradual fall (drink-down) then a sharp rise (sip), over and over. A flat or only-falling line means watering isn&rsquo;t actually happening."),
    defterm("Forgiveness (CEC / buffer)", "How much a sponge cushions your feeding mistakes by holding and releasing food. Coco has lots, living soil self-fixes, rockwool has almost none, plain water has none."),
    defterm("Drip-out (runoff)", "The small fraction of feed that drains out the bottom (about 10&ndash;20%). Not waste &mdash; it washes off stacked salt and is the dipstick that reads the sponge&rsquo;s true feed strength."),
    defterm("Channeling (water tunnelling through)", "When water runs straight down one path and out the bottom, missing the roots, while the core stays dry. You spot it by how fast the water came out, not how much."),
    defterm("Permittivity (how strongly it reacts to the probe)", "How strongly a material responds to the probe&rsquo;s tiny electric field. Water reacts a lot, dry sponge barely, air almost none &mdash; that gap lets a buried probe feel water it can&rsquo;t see."),
    defterm("Precise vs right (resolution vs accuracy)", "Precise = lots of decimals shown; right = actually close to the truth. A sensor can be precise and still be off by a few points until you calibrate it."),
    defterm("Second witness", "An independent check &mdash; water dripping out the bottom, or the pot&rsquo;s weight &mdash; required to confirm a probe reading before any water moves."),
    defterm("Water tally / piggy bank (water balance)", "A running count of water IN (the dripper sips) minus water OUT (the plant breathing it out, plus what drains), giving the real water in the pot without trusting one sensor."),
    defterm("Confidence", "How much to trust today&rsquo;s reading &mdash; high when the clues agree, low when they disagree. High lets an auto-waterer give a full sip; low means a tiny sip, wait, or ask a human."),
    defterm("Never flood, never starve", "The single safety rule on all automatic watering &mdash; water more only when sure there&rsquo;s room, and when in doubt do the safe thing. A lying sensor can only make the system more careful, never trick it into overwatering."),
    defterm("The gearbox (transfer function)", "The plain idea that the sponge takes your watering and changes it by fixed amounts before the roots feel it &mdash; same input, different output per sponge."),
  ]})
