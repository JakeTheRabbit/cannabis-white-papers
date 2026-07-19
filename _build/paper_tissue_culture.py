# -*- coding: utf-8 -*-
"""Paper: cannabis tissue culture (beginner). Rendered through the unified shell."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        stagecard, grid, card, chip, kv, steps, cite)
import figs as F
import figs_extra as FX

SLUG = "tissue-culture"
TITLE = "Cleaning up cannabis genetics with tissue culture"
EYEBROW = "Beginner · Tissue culture"
SUB = ("Tissue culture grows a clean, vigorous, genetically identical mother from a speck of "
       "tissue off a tired or diseased plant. Explained from absolute zero.")
META = [("spark", "Beginner"), ("image", "18 step photos"),
        ("quote", "Evidence-linked · 11 sources"), ("clock", "~22 min read")]
RELATED = ["mould-risk", "grow-room-systems", "gmp-hash-lab"]
REF_IDS = ["hlvd_threat2023", "hlvd_mgmt2025", "holmes2021", "mdpi2024_media",
           "hlvd_thermo2024", "page2019", "pmc9146626", "kurtz2022",
           "torkamaneh2024", "tis2022", "karger2019_cryo", "athena"]

_TITLE_LONG = "Cleaning Up Cannabis Genetics with Tissue Culture: A Complete Beginner's Guide"

def _cite_html(rid):
    n = REF_IDS.index(rid) + 1
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, n)
R = {rid: _cite_html(rid) for rid in REF_IDS}

HERO = """
<header class="hero"><div class="wrap">
  <div class="eyebrow">Plant Tissue Culture &middot; First-Timer's User Guide</div>
  <h1>Cleaning Up Cannabis Genetics with Tissue Culture</h1>
  <p class="sub">Take a tired, possibly diseased cannabis plant and grow a clean, vigorous,
  genetically identical mother from a speck of its tissue. Explained from absolute zero, with
  a benchtop Athena-style kit.</p>
  <div class="meta">
    <span class="chip">Assumes no prior lab experience</span>
    <span class="chip">Stage 0 &rarr; clean mother</span>
    <span class="chip">Built on 2019&ndash;2026 research</span>
    <span class="chip">Honest about what a kit can &amp; can't do</span>
  </div>
</div></header>
"""

# ============================================================ SECTIONS

SECTIONS = []

# ---- 1. Start here -------------------------------------------------------
SECTIONS.append({
  "id": "start", "kicker": "01: Read this first", "title": "What this guide is, and what you'll achieve",
  "blocks": [
    lead("This guide takes you from picking a donor plant to holding a clean, rooted, hardened "
         "young mother in your hands. You will learn what plant tissue culture is, why cannabis "
         "growers use it to &ldquo;clean up&rdquo; their genetics, and exactly how to run the whole "
         "process yourself."),
    p("This is written for someone who has <strong>never set foot in a lab</strong>. Every term is "
      "defined the first time it appears. Nothing is assumed. Where the science is genuinely "
      "uncertain or a product hides its details, this guide says so plainly."),
    callout("key", "The one-sentence version",
      p("Tissue culture regrows an entire plant from a microscopic piece of its growing tip. That "
        "tip is too young to carry most diseases, so the new plant comes out <em>clean</em> even if "
        "its parent was sick.")),
    h(3, "How to use this document"),
    grid([
      card("If you're curious", "Read sections 1&ndash;5. They cover the why and the big picture "
           "with nothing to buy.", tag="Browse"),
      card("If you're about to start", "Read everything. Sections 6&ndash;17 are the hands-on "
           "workflow in the exact order you'll do it.", tag="Do it"),
      card("If you hit a problem", "Jump to section 19 (Troubleshooting) and section 20, the "
           "honest reality check on success rates and cost.", tag="Fix it"),
    ], cols=3),
    callout("warn", "A realistic expectation, set now",
      p("Cannabis is a <strong>recalcitrant</strong> species: it fights back in the jar. Losing most "
        "of your first batch to contamination or browning is <em>normal</em>, not failure. Published "
        "labs report anywhere from ~55% of pieces surviving down to 90&ndash;95% losses at the very "
        "first stage. Treat your first run as a training run.")),
  ]})

# ---- 2. Plain English ---------------------------------------------------
SECTIONS.append({
  "id": "basics", "kicker": "02: The concepts", "title": "Tissue culture in plain English",
  "blocks": [
    p("Tissue culture rests on one fact about plants that animals do not share. Almost every cell "
      "holds the full instructions to rebuild the whole plant."),
    callout("key", "Totipotency: the property that makes all of this work",
      p("Many plant cells can, under the right conditions, carry the complete instructions to rebuild the whole "
        "plant. Give a tiny scrap of the right tissue the right food and the right hormones and it "
        "grows roots, shoots and leaves: a complete new plant. This ability is called "
        "<strong>totipotency</strong>. You are not growing a &lsquo;sample&rsquo;, you are growing a "
        "whole new copy.")),
    p("Here is the vocabulary you need. Get the gist rather than memorising it. Each term comes "
      "back in context later."),
    table(["Term", "What it actually means"], [
      ["<strong>Tissue culture (TC)</strong>", "Growing plant cells, tissues or organs in a sterile container on a jelly-like food, instead of in soil."],
      ["<strong>Micropropagation</strong>", "Using tissue culture specifically to <em>multiply</em> a plant, making many identical copies. The two words are used interchangeably here."],
      ["<strong>In vitro</strong>", "Latin for &lsquo;in glass&rsquo;. Anything happening inside the sterile jar. Its opposite is <strong>ex vitro</strong> / <strong>in vivo</strong>: out in the real world."],
      ["<strong>Explant</strong>", "The small piece of plant you cut off and put into the jar to start a culture. Your seed crystal."],
      ["<strong>Clone</strong>", "A genetically identical copy. Every plant from one mother by TC (or by cutting) is a clone."],
      ["<strong>Aseptic / sterile technique</strong>", "Working so that no bacteria, fungi or yeast get into your culture. The single skill that decides success."],
      ["<strong>Medium (plural: media)</strong>", "The food. A jelly of mineral salts, sugar, vitamins and hormones, set firm with a gelling agent. &lsquo;Pouring media&rsquo; = filling jars with it."],
      ["<strong>PGR (plant growth regulator)</strong>", "A plant hormone added to the medium to steer growth. One type makes shoots, another makes roots. Also just called &lsquo;hormones&rsquo;."],
      ["<strong>Meristem</strong>", "The dome of forever-young, dividing cells at the very tip of every shoot. The cleanest tissue on the plant, and the hero of this whole guide."],
      ["<strong>Node</strong>", "The point on a stem where a leaf and a bud join. A <strong>nodal segment</strong> is a short stem piece containing one bud."],
      ["<strong>Subculture</strong>", "Moving growing tissue onto fresh medium. You repeat this every few weeks to keep cultures alive and multiplying."],
      ["<strong>Contamination</strong>", "The enemy: any microbe that invades the jar and outcompetes your plant. Almost always fatal to that culture."],
      ["<strong>Indexing</strong>", "Lab-testing a plant to confirm it is free of a specific disease (e.g. a RT-qPCR test for a viroid). &lsquo;Proving clean.&rsquo;"],
    ]),
    callout("note", "&lsquo;Cleaning up genetics&rsquo;: what it does and doesn't mean",
      p("It does <strong>not</strong> mean editing or improving the DNA. The strain stays exactly "
        "the same strain. It means stripping away the <em>diseases and pests</em> the plant has "
        "picked up over years of cloning, so the original genetics can finally perform the way they "
        "were bred to. It is a factory reset on plant health, not a genetic upgrade.")),
  ]})

# ---- 3. Why -------------------------------------------------------------
SECTIONS.append({
  "id": "why", "kicker": "03: The reason", "title": "Why clean up genetics? Meet Hop Latent Viroid",
  "blocks": [
    p("Take cuttings from the same mother for years and two things creep in: invisible "
      "<strong>diseases</strong> that spread cutting-to-cutting, and the slow accumulation of "
      "<strong>damage</strong>. The plant looks fine, then yields quietly drop, buds get smaller, "
      "smell fades. The number-one culprit in cannabis has a name."),
    defterm("Hop Latent Viroid (HpLVd, sometimes HLVd)",
      "A viroid: a naked loop of RNA just 256 building-blocks long, far smaller and simpler "
      "than a virus (it has no protein shell at all). It causes the disease growers call "
      "<strong>&lsquo;dudding&rsquo;</strong> or &lsquo;duds&rsquo;." + R["hlvd_threat2023"]),
    figure(F.fig_hplvd(), 1,
      "A clean plant versus a &lsquo;dudded&rsquo; one carrying Hop Latent Viroid. The infection is "
      "often symptomless early on, which is exactly why it spreads through a clone line "
      "undetected until production has quietly collapsed."),
    h(3, "Why HpLVd is such a big deal"),
    grid([
      card("It's everywhere", "Industry and research surveys have reported very high facility infection rates in California (~90% in one large testing programme) and frequent positives in Canadian retail flower (~40% in one study) &mdash; treat as warning signals, not permanent global prevalence. If you've cloned for years, assume you may have it." + R["hlvd_mgmt2025"], tag="Prevalence"),
      card("It's expensive", "In severe symptomatic dud outbreaks, infected plants can lose a large fraction of cannabinoids (sometimes approaching ~50%)</strong>, plus terpenes, trichomes and yield. Industry losses run into tens of millions of dollars a year.", tag="Impact"),
      card("It's stealthy", "It can sit <strong>symptomless</strong> for a long time and is &lsquo;latent&rsquo; by name. By the time plants visibly dud, the whole room is usually infected.", tag="Latent"),
      card("It's tough", "It survives on tools, hands, pots and benches, rides in sap for ~a week and in dried tissue for ~a month, and even passes through seed (at genotype-dependent rates (often single digits to tens of percent — test seed lots)).", tag="Persistent"),
    ], cols=2),
    callout("warn", "Why you can't just spray it away",
      p("No spray cures a viroid-infected plant. It lives <em>inside</em> the plant's "
        "cells and plumbing. The only reliable way to get rid of it is to grow a brand-new plant "
        "from a piece of tissue the viroid hasn't reached yet. That is precisely what "
        "meristem tissue culture does, and it is the heart of this guide.")),
    callout("note", "Other things tissue culture clears out",
      p("HpLVd gets the headlines, but meristem work plus indexing mainly targets systemic agents (viroids/viruses); surface sterilisation removes many surface microbes and hitch-hikers, but endophytes can still emerge and mites remain an IPM problem. "
        "You begin clean at the cellular level instead of fire-fighting forever.")),
  ]})

# ---- 4. Big picture -----------------------------------------------------
SECTIONS.append({
  "id": "overview", "kicker": "04: The map", "title": "The whole journey at a glance",
  "blocks": [
    p("Every plant tissue culture workflow follows the same five classic stages, whether for "
      "orchids, bananas or cannabis. They were first laid out by a scientist named Murashige. "
      "Learn this skeleton and everything that follows hangs neatly on it."),
    figure(F.fig_5stages(), 2,
      "The five classic stages of micropropagation. Stage 0 is preparing the donor plant; Stages "
      "I&ndash;IV happen in and around the sterile jar. The &lsquo;cleanup&rsquo; (meristem work) "
      "and the &lsquo;proof&rsquo; (disease testing) slot into the early stages."),
    p("This guide breaks those five stages into the practical steps you'll actually perform. That "
      "includes the two cannabis-specific extras: the <strong>meristem cleanup</strong> "
      "that removes the viroid, and the <strong>indexing</strong> test that proves it worked."),
    figure(F.fig_pipeline(), 3,
      "The full step-by-step pipeline used in this guide, with rough durations. The purple step "
      "(meristem cleanup) and the blue step (indexing / disease testing) are what turn ordinary "
      "cloning into genetic clean-up. Durations overlap in practice."),
    h(3, "How long does the whole thing take?"),
    p("Longer than you'd hope, and that's worth knowing up front. There are two honest answers, "
      "depending on what you mean by &lsquo;done&rsquo;."),
    figure(F.fig_timeline(), 4,
      "An indicative timeline for a careful beginner. A routine rooted, hardened clone is roughly "
      "2.5&ndash;3.5 months. A <em>verified disease-free mother</em>, including slow "
      "meristem recovery and repeated lab testing, realistically takes 5&ndash;6+ months."),
    callout("key", "The two timelines, stated plainly",
      ul([
        "<strong>A clean, rooted, hardened clone</strong> (no lab proof of disease status): roughly <strong>10&ndash;15 weeks</strong>.",
        "<strong>A confirmed HpLVd-free mother</strong> (meristem culture + RT-qPCR testing): realistically <strong>5&ndash;6 months or more</strong>. It is not a two-week job.",
      ], "tight")),
  ]})

# ---- 5. The science of clean -------------------------------------------
SECTIONS.append({
  "id": "science", "kicker": "05: The clever bit", "title": "Why a meristem tip beats the disease",
  "blocks": [
    p("This is the single most important concept in the whole guide. Once it clicks, everything "
      "about &lsquo;cleaning genetics&rsquo; makes sense."),
    p("Viroids and viruses move around a plant through its <strong>vascular system</strong>: "
      "the internal plumbing (phloem) that carries sap. They spread cell-to-cell from there. But at "
      "the very tip of every growing shoot sits the <strong>meristem</strong>, a dome of furiously "
      "dividing baby cells that is <em>so new the plumbing hasn't been built into it yet</em>."),
    figure(F.fig_meristem(), 5,
      "Inside a shoot tip. The viroid travels up the red vascular tissue but cannot reach the green "
      "meristem dome: there's no plumbing there yet, and the dome's cells divide faster than "
      "the viroid can spread. Excise just that 0.2&ndash;0.5&nbsp;mm dome and you usually leave "
      "the disease behind."),
    callout("key", "Two reasons the dome stays clean",
      ol([
        "<strong>No plumbing yet.</strong> The vascular tissue that carries the viroid hasn't differentiated in the dome, so the pathogen has no road in.",
        "<strong>The cells outrun it.</strong> Meristem cells divide faster than the viroid can copy itself and creep forward, so the newest tip cells stay ahead of the infection.",
      ], "tight")),
    p("Which piece you cut decides whether you merely clone the plant or actually clean it. There is "
      "a direct trade-off: the smaller and younger the piece, the cleaner it is, and the harder it "
      "is to keep alive."),
    figure(FX.fig_explant(), 6,
      "Your three explant choices. A nodal segment is easy but keeps the disease. A meristem dome is "
      "the only choice that reliably clears Hop Latent Viroid, but it's a sub-millimetre "
      "dissection under a microscope and many won't survive. Most beginners start with nodes to "
      "learn the craft, then graduate to meristems for the actual cleanup."),
    callout("warn", "The honest caveat: free is not the same as resistant",
      p("Meristem culture can produce a viroid-<strong>free</strong> plant. It does <strong>not</strong> "
        "make a viroid-<strong>resistant</strong> one. A cleaned plant can be re-infected the moment a "
        "dirty blade or hand touches it. Clean stock only stays clean with disciplined hygiene "
        "afterwards, and it's only truly &lsquo;clean&rsquo; once a lab test says so (section 13).")),
  ]})

# ---- 6. Lab & kit -------------------------------------------------------
SECTIONS.append({
  "id": "lab", "kicker": "06: Your setup", "title": "Your lab and your kit",
  "blocks": [
    p("You do not need a white-coat laboratory. You need a small pocket of genuinely clean air to "
      "work in, a way to sterilise things with heat, and somewhere lit and warm to keep the jars. "
      "Here is the whole picture."),
    h(3, "Clean air: still-air box vs flow hood"),
    grid([
      card("Still-Air Box (SAB)", p("A clear plastic storage tub on its side with two arm-holes cut "
        "in the front, wiped down with alcohol. With all fans and AC off, the air inside goes dead "
        "still so spores can't drift onto your open jars. <strong>Cheap to free, and the recommended "
        "place to start.</strong> Downside: cramped, and moving your arms stirs the air."), tag="Beginner"),
      card("Laminar Flow Hood (LFH)", p("A powered cabinet that blows HEPA-filtered air (removing "
        ">99% of particles) in one smooth sheet across your work, constantly washing contaminants "
        "away. Roomier, faster, far more forgiving. <strong>The upgrade, not a requirement.</strong> "
        "This is what comes in the Athena kit."), tag="Upgrade"),
    ], cols=2),
    callout("note", "You do NOT need a biosafety cabinet",
      p("Those exist to protect the <em>operator</em> from dangerous germs. In plant TC you only need "
        "to protect the <em>plant</em> from germs, so a flow hood (or a still-air box) is "
        "exactly the right tool. A biosafety cabinet is expensive overkill.")),
    figure(F.fig_lab(), 7,
      "The inside of a still-air box or flow hood, laid out for work. There is one sterile field in "
      "the centre where the open jars and cutting happen; tools get re-sterilised on the left, fresh "
      "media and explants wait on the right, waste goes in a discard pile. Hands never pass over open "
      "vessels."),
    h(3, "The Athena Culture Kit, honestly assessed"),
    p("Athena Ag (the company behind the popular &lsquo;Pro Line&rsquo; nutrients) sells an "
      "all-in-one benchtop tissue culture kit aimed squarely at growers with no lab experience. It "
      "bundles the awkward, expensive bits into one toolbox." + R["athena"]),
    figure(FX.fig_athena_kit(), 8,
      "The Athena Culture Kit's confirmed contents (green) and the parts Athena keeps proprietary "
      "(amber). It's a genuinely convenient package, but the media's base and hormones are "
      "trade secrets, and the kit contains nothing to <em>prove</em> a plant is disease-free."),
    p("What's confirmed to be in the box:"),
    ul([
      "A portable <strong>laminar flow hood</strong> (True HEPA H13 filter, airflow 0.5&ndash;0.9&nbsp;m/s, ~2.58&nbsp;ft&sup3; work zone).",
      "A small <strong>one-touch autoclave</strong> (pressure steriliser) for media and tools.",
      "A <strong>toolbox</strong> with scalpel, forceps and the step-by-step procedure printed inside the lid.",
      "Two pre-mixed, &lsquo;just add water&rsquo; media: <strong>SHOOTS</strong> (blue; multiplies shoots) and <strong>ROOTS</strong> (callus and root development / new mothers).",
      "<strong>Cleanse</strong> (a plant-safe hypochlorous-acid sanitiser) and <strong>bleach</strong> as the surface sterilants.",
      "Enough to make up to <strong>~120 culture vessels</strong> out of the box; media, vessels and filters are bought as refills.",
    ]),
    callout("warn", "What the kit deliberately doesn't tell you, and doesn't include",
      ul([
        "<strong>The media base is secret.</strong> Athena won't say whether ROOTS/SHOOTS are built on MS, DKW or a custom blend, nor which hormones, at what doses. You can't tune or troubleshoot what you can't see.",
        "<strong>No disease test.</strong> The kit does the meristem cut but ships <em>no</em> RT-qPCR test and <em>no</em> thermotherapy gear. So it cannot, by itself, prove a plant is HpLVd-free. Budget for independent lab testing (section 13).",
        "<strong>Price moves around:</strong> roughly <strong>$1,800&ndash;$2,295</strong> depending on where and when; refills (media $30&ndash;$40/box, vessels $15 each, HEPA $100) add up over time.",
      ], "tight")),
    callout("tip", "You can do all of this without the Athena kit",
      p("A DIY equivalent (still-air box, a $60 pressure cooker as the autoclave, generic MS "
        "media powder, agar, bleach) runs roughly <strong>$200&ndash;$550</strong> to start. "
        "The kit buys convenience and a real flow hood, not a different outcome. Where this guide "
        "gives a recipe, it gives both the DIY version and the Athena-sachet version.")),
  ]})

# ---- 7. Aseptic technique ----------------------------------------------
SECTIONS.append({
  "id": "aseptic", "kicker": "07: The core skill", "title": "Aseptic technique: the skill that decides everything",
  "blocks": [
    lead("Learn this one thing well above all others. Ninety percent of beginner failures are "
         "contamination, and contamination is a technique problem, not a luck problem."),
    p("&lsquo;Aseptic&rsquo; means working so that no stray microbe lands in your jar. Microbes "
      "are everywhere: on your skin, in your breath, drifting in the air, on every surface. "
      "Your medium is a sugary jelly they would <em>love</em> to eat. Your job is to be the bouncer."),
    h(3, "The four enemies, and how to recognise them"),
    figure(FX.fig_contam(), 9,
      "The four kinds of contamination and their tell-tale signs. The sneakiest is the endophyte, "
      "a microbe living <em>inside</em> healthy-looking mother tissue that surface bleach "
      "can't reach, so it stays hidden for weeks then erupts. This is why a clean-looking first week "
      "means nothing; always wait and watch."),
    h(3, "The aseptic workflow, every single time"),
    steps([
      ("Clean the zone", "Wipe the box/hood interior and the bench with 70% alcohol. Let it flash off. Turn off fans/AC if using a still-air box."),
      ("Glove and spray", "Fresh nitrile gloves, then spray your gloved hands with 70% alcohol. Re-spray often, every time you touch anything outside the sterile field."),
      ("Only what you need", "Bring in only the jars, tools and explants for this session. Clutter is contamination."),
      ("Sterilise tools before EVERY cut", "Dip the scalpel and forceps in alcohol then pass through a flame, OR use a glass-bead steriliser (~250&nbsp;&deg;C, ~20&nbsp;seconds). Then <strong>let them cool</strong>: touching tissue with a hot tool cooks it."),
      ("Work fast, lids off briefly", "Open a jar only at the moment you use it; close it the instant you're done. Never leave a vessel gaping."),
      ("Hands never cross open jars", "Reaching over an open vessel showers it with skin flakes and spores. Approach from the side, always."),
    ]),
    callout("danger", "Flame plus alcohol is a fire risk",
      p("If you dip tools in alcohol and flame them, keep the open alcohol container well away from "
        "the flame and never flame directly over it. A glass-bead steriliser removes the open-flame "
        "risk entirely and is the safer choice in a plastic still-air box.")),
    callout("tip", "The 7-day patience test",
      p("After pouring fresh media, or after starting new cultures, leave them in the culture room "
        "for about <strong>7 days</strong> before you trust them or commit more material. Any "
        "contamination, especially the slow latent kind, will reveal itself. It is far "
        "cheaper to lose one jar to the bin than a whole batch to a hidden microbe.")),
  ]})

# ---- 8. Media -----------------------------------------------------------
SECTIONS.append({
  "id": "media", "kicker": "08: The food", "title": "Making and sterilising the medium",
  "blocks": [
    p("The medium is the jelly your plant lives on. At its simplest it is mineral salts (plant "
      "food), sugar (energy, because a sealed jar is too dim for the plant to feed itself), vitamins, "
      "optional hormones, and a gelling agent to set it firm: all dissolved in pure water, "
      "pH-adjusted, then heat-sterilised."),
    defterm("MS (Murashige &amp; Skoog) salts",
      "The standard, off-the-shelf mineral mix used for most plant tissue culture. Sold as a powder; "
      "you just weigh it out. The safe default for a beginner."),
    defterm("DKW (Driver &amp; Kuniyuki Walnut) salts",
      "An alternative salt mix that several cannabis studies found gives healthier, more vigorous "
      "shoots than MS, though not in every lab. Treat it as an upgrade to experiment with, "
      "not a starting requirement." + R["mdpi2024_media"]),
    h(3, "A starter recipe (per 1 litre)"),
    p("This is a solid, widely-used DIY initiation/multiplication medium. Make it once and you'll "
      "understand what's in every sachet you ever buy."),
    table(["Ingredient", "Amount per litre", "What it does"], [
      ["Distilled / RO water", "start with ~800 mL", "The solvent. Pure water only: tap minerals throw off the recipe."],
      ["MS basal salts", "<span class='num'>4.4 g</span>", "The mineral nutrition (full strength)."],
      ["Sucrose (sugar)", "<span class='num'>30 g</span> (3%)", "Energy source. Plain table sugar works for hobby use."],
      ["Agar", "<span class='num'>6&ndash;8 g</span>", "Gelling agent that sets the jelly. More agar = firmer gel = less hyperhydricity (section 14)."],
      ["myo-Inositol", "<span class='num'>0.1 g</span>", "A growth supplement / sugar-alcohol the cells use."],
      ["Activated charcoal", "<span class='num'>~1 g</span> (optional)", "Soaks up the brown phenolics cannabis leaks, reducing browning."],
      ["Hormone (PGR)", "see table below", "Steers the tissue toward shoots or roots. Optional at initiation."],
      ["PPM (a biocide)", "<span class='num'>1&ndash;2 mL</span> (optional)", "Extra insurance against microbes that survive sterilisation."],
      ["Top up water to", "<span class='num'>1 L</span>; pH to <span class='num'>5.6&ndash;5.8</span>", "Set pH BEFORE adding agar and before sterilising."],
    ], caption="DIY all-purpose cannabis medium. Use full-strength MS for initiation/multiplication; switch to half-strength MS for rooting (section 15)."),
    callout("note", "Order of operations matters",
      p("Dissolve salts and sugar in the water first, <strong>adjust the pH to 5.6&ndash;5.8</strong> "
        "(nudge down with a drop of dilute acid, up with dilute base), <em>then</em> add the agar, "
        "then heat to dissolve the agar, then pour into jars (~&#8531; full) and sterilise. pH set "
        "after the agar is in is much harder to do.")),
    h(3, "The hormone cheat-sheet (for DIY media)"),
    p("Buy a kit and the hormones are already blended in, so you can skip this. Mix your "
      "own and this is the cannabis-specific shortlist."),
    table(["Stage", "Hormone (PGR)", "Typical dose", "Notes"], [
      ["Initiation", "meta-Topolin (mT) <em>or</em> TDZ", "mT ~0.5 mg/L; TDZ 0.1&ndash;0.5 mg/L", "A gentle cytokinin to wake the explant. TDZ is potent: keep it low, or it causes callus and glassy shoots."],
      ["Multiplication", "meta-Topolin (mT)", "0 &ndash; ~0.5 &micro;M", "Less is more in cannabis. Hormone-free often gives the healthiest, most numerous shoots (see section 14)."],
      ["Rooting", "IBA (an auxin)", "2.5 &micro;M (~0.5 mg/L)", "The best rooting hormone for cannabis: roughly double the roots of IAA or NAA."],
    ], caption="Cytokinins (mT, TDZ) push shoots; auxins (IBA) push roots. That's the whole logic of PGRs in three rows."),
    h(3, "Sterilising the medium"),
    p("Raw medium is microbe heaven, so it must be heat-sterilised before use. The home tool is a "
      "<strong>pressure cooker</strong>; the lab tool is an <strong>autoclave</strong> (the Athena "
      "kit includes a small one). Both do the same job: hold the jars at "
      "<strong>121&nbsp;&deg;C / 15&nbsp;psi for ~20 minutes</strong>."),
    grid([
      card("DIY: pressure cooker", "Jars loosely capped, ~20 min at 15 psi. Let it cool and depressurise on its own before opening, with the steam still gently venting, so it doesn't suck room air (and spores) back in.", tag="$"),
      card("Athena: sachet + autoclave", "Empty one SHOOTS or ROOTS sachet into the vessel, add RO water to the line (125 mL or 750 mL), shake to dissolve, run the one-touch autoclave, then pour under the hood.", tag="Kit"),
    ], cols=2),
    callout("warn", "Shelf life",
      p("Plain MS+agar media keeps a few weeks to ~1&ndash;2 months refrigerated and dark. Media with "
        "PPM in it should be used within about <strong>1 month</strong>. Make what you'll use.")),
  ]})

# ---- 9. Stage 0 ---------------------------------------------------------
SECTIONS.append({
  "id": "stage0", "kicker": "09: Stage 0", "title": "Preparing the mother plant",
  "blocks": [
    p("Garbage in, garbage out. The health of your donor plant is the single biggest predictor of "
      "whether your cultures stay clean. A stressed, dusty, pest-ridden mother will defeat even "
      "perfect technique, because some microbes ride <em>inside</em> the tissue where bleach can't "
      "reach (the endophytes from section 7)."),
    stagecard("0", "Condition a clean, vigorous donor", "1&ndash;2 weeks", "".join([
      p("Pick your best, true-to-type plant and get it into peak vegetative health before you cut "
        "anything from it."),
      ul([
        "Keep it <strong>vegetative, never flowering</strong>: long days, 18 h light / 6 h dark.",
        "Aim for <strong>24&ndash;30&nbsp;&deg;C</strong> and a moderate <strong>55&ndash;60% humidity</strong>.",
        "Feed a vegetative nutrient mix and keep it pushing <strong>soft, fast new growth</strong>. That young tissue gives far better, cleaner explants than old woody stems.",
        "Scout and treat <strong>pests and disease</strong> first. Only work from a plant that looks genuinely healthy.",
      ], "tight"),
    ])),
    callout("tip", "The pre-cut conditioning trick",
      ul([
        "For the <strong>1&ndash;2 weeks before cutting</strong>, keep humidity low and stop overhead watering. Dry foliage carries far fewer surface fungi and bacteria.",
        "Some growers apply a systemic fungicide drench/spray in those days to knock back the internal microbe load that surface sterilising can't touch.",
        "Take your explants from the <strong>upper, younger but fully-formed nodes</strong> of an actively growing shoot, not the floppy tip and not the woody base.",
      ], "tight")),
  ]})

# ---- 10. Stage 1 explant + sterilize -----------------------------------
SECTIONS.append({
  "id": "stage1", "kicker": "10: Stage 1", "title": "Taking and sterilising the explant",
  "blocks": [
    p("Now the hands-on work begins. You'll cut a small piece from the conditioned mother and "
      "surface-sterilise it, killing every microbe on its outside without killing the plant "
      "tissue itself. This is the dirtiest, most failure-prone step, so go slowly and follow the "
      "sequence exactly."),
    h(3, "Cut the explant"),
    p("For your <em>first</em> attempts, use a <strong>nodal segment</strong>: a piece of stem ~1 cm "
      "long containing one bud. It's the most forgiving explant and lets you learn sterile technique "
      "before attempting the fiddly meristem dissection (section 12). Strip off large leaves to "
      "reduce the surface area carrying microbes."),
    h(3, "Surface-sterilise it"),
    p("The standard, best-supported beginner protocol is a two-punch: a quick alcohol dip to break "
      "the waxy surface, then a bleach soak to kill everything, then thorough rinsing so no bleach "
      "remains to poison the tissue."),
    figure(F.fig_sterilize(), 10,
      "The surface-sterilisation sequence. Everything from the alcohol step onward happens inside "
      "the still-air box / flow hood with sterilised tools and sterile water. Soak times scale with "
      "how tough the tissue is: too short leaves microbes, too long kills the explant."),
    table(["Step", "What to use", "Time"], [
      ["1. Pre-wash", "Tap water + a drop of dish soap, gently agitated", "10&ndash;20 min"],
      ["2. Alcohol dip", "70% ethanol or isopropyl", "30&ndash;60 sec"],
      ["3. Bleach soak", "10% household bleach (1 part bleach : 9 parts water) + a few drops of Tween-20 / dish soap, swirling", "15&ndash;20 min"],
      ["4. Rinse &times;3", "Sterile distilled water, fresh each time", "3 min each"],
      ["5. Re-trim", "Cut off the bleach-damaged ends on a sterile surface", "&ndash;"],
      ["6. Plate", "Place onto initiation medium, seal the vessel", "&ndash;"],
    ], caption="Beginner surface-sterilisation. The Athena protocol substitutes a Cleanse (hypochlorous acid) wash before the bleach; exact Athena dilutions/times are proprietary." + R["holmes2021"]),
    callout("danger", "The number-one beginner trap: &ldquo;10% bleach&rdquo; is NOT &ldquo;10% NaOCl&rdquo;",
      p("Recipes quote bleach two different ways and people poison their tissue by confusing them. "
        "<strong>Household bleach is only ~5&ndash;8% sodium hypochlorite (NaOCl) to begin with.</strong> "
        "So a 10% dilution of household bleach gives only ~0.5&ndash;0.8% <em>actual</em> NaOCl, "
        "which is correct. If a paper says &lsquo;1% NaOCl&rsquo; that's a stronger solution. Always "
        "check whether a number refers to diluted bleach or to active NaOCl before you mix.")),
    callout("warn", "Don't over-soak",
      p("Beyond ~30 minutes in bleach, cannabis tissue starts dying (one study saw ~75% tissue death "
        "by 45+ min). Under-sterilise and you get contamination; over-sterilise and you get a "
        "dead brown explant. 15&ndash;20 minutes is the beginner sweet spot. Adjust from there.")),
  ]})

# ---- 11. Stage 2 initiation --------------------------------------------
SECTIONS.append({
  "id": "initiation", "kicker": "11: Stage I", "title": "Initiation: waking the explant up",
  "blocks": [
    p("&lsquo;Initiation&rsquo; (also called establishment) is the period after you've placed "
      "the sterile explant on its medium, while it settles in and starts to grow. Your jobs here are "
      "to watch like a hawk for contamination and to keep the tissue from browning to death."),
    stagecard("I", "Establish a clean, growing culture", "2&ndash;4 weeks", "".join([
      ul([
        "Put the plated vessels in the culture room at <strong>~25&nbsp;&deg;C</strong>, "
        "<strong>16 h light / 8 h dark</strong>, gentle light.",
        "<strong>Watch for 7&ndash;14 days.</strong> Bin any vessel showing fungal fuzz, cloudy medium or slimy ooze immediately. One bad jar can seed the shelf.",
        "Expect the bud to swell and push new growth (&lsquo;bud break&rsquo;) in roughly <strong>2&ndash;3 weeks</strong>.",
        "Survivors that are clean and growing graduate to the multiplication stage.",
      ], "tight"),
    ])),
    callout("warn", "Browning: the other way explants die",
      p("Cut cannabis leaks <strong>phenolic</strong> compounds that oxidise and turn the tissue (and "
        "the medium around it) brown, sometimes fatally. Fight it with <strong>activated charcoal in "
        "the medium</strong> (~1 g/L), an antioxidant dip, and moving the explant to fresh medium "
        "early and often in the first couple of weeks.")),
    callout("note", "Why losses are high here, and that's OK",
      p("Initiation is where recalcitrant cannabis sheds the most cultures. Published labs report "
        "anywhere from ~55% of explants surviving to 90&ndash;95% loss across varieties. Start more "
        "explants than you think you need, and don't be discouraged by a thin survival rate on run one.")),
  ]})

# ---- 12. Meristem cleanup ----------------------------------------------
SECTIONS.append({
  "id": "cleanup", "kicker": "12: The cleanup", "title": "Meristem dissection: the actual genetic clean-up",
  "blocks": [
    p("Everything so far also describes ordinary cloning. <strong>This</strong> is the step that "
      "removes the disease. Instead of a 1 cm node, you excise only the tiny meristem dome from "
      "section 5, the part the viroid hasn't reached, and grow your new plant from that."),
    stagecard("M", "Excise the clean meristem dome", "4&ndash;8 weeks to recover", "".join([
      steps([
        ("Sterilise a shoot tip", "Surface-sterilise an actively growing shoot tip exactly as in section 10."),
        ("Go under the scope", "Under a stereo (dissecting) microscope, in the flow hood, use fine sterile needles/forceps to peel away the wrapping baby leaves until the glassy, translucent meristem dome is exposed."),
        ("Cut the dome", "Excise just the dome plus 1&ndash;2 leaf primordia, a piece only <strong>0.2&ndash;0.5 mm</strong> across. Place it on initiation medium."),
        ("Be patient", "Meristems are slow and fragile. Expect ~10 weeks (sometimes up to ~24) to recover into a viable shoot, much slower than a node."),
      ]),
    ])),
    h(3, "How well does it actually work?"),
    p("Here is where honesty matters most. Meristem culture <em>can</em> clear HpLVd, but how "
      "often it succeeds depends enormously on the strain. In one 13-cultivar study using meristem "
      "culture plus mild heat treatment, the disease was fully eradicated in only <strong>5 of 13</strong> "
      "cultivars." + R["hlvd_thermo2024"]),
    figure(FX.fig_hlvd_clearance(), 11,
      "Clearance rates from a single protocol across 13 cannabis cultivars. Some cleared 100% of "
      "the time, others barely 14%. There is no universal recipe: expect to clean several "
      "meristems per strain and test them all. (The strain confusingly named &lsquo;Athena&rsquo; "
      "here is unrelated to the Athena Ag kit.)"),
    callout("note", "Optional adjuncts: thermotherapy and cryotherapy",
      ul([
        "<strong>Thermotherapy</strong>, holding the mother or culture warm (~30&ndash;36&nbsp;&deg;C) for a couple of weeks, lowers viroid levels so you can excise a slightly larger, more survivable meristem that's still clean. On its own it's unreliable (levels rebound; heat can even create mutant viroids), so it's used <em>with</em> meristem excision, not instead.",
        "<strong>Cryotherapy</strong> (briefly freezing shoot tips in liquid nitrogen so only the tiny clean cells survive) is a powerful research method but has no standard, proven cannabis protocol yet. File under &lsquo;advanced/future&rsquo;.",
      ], "tight")),
    callout("warn", "The Athena kit can clean, but it cannot prove",
      p("The kit lets you do the meristem cut. It includes <strong>no heat-treatment hardware and no "
        "DNA test</strong>. So after this step you have a plant that is <em>probably</em> clean until a lab RT-qPCR says so, "
        "not a <em>proven</em> clean one. That proof is the next section, and it's non-negotiable.")),
  ]})

# ---- 13. Indexing -------------------------------------------------------
SECTIONS.append({
  "id": "indexing", "kicker": "13: The proof", "title": "Indexing: proving it's actually clean",
  "blocks": [
    p("A meristem plant that <em>looks</em> healthy is not a clean plant until a lab test says so. "
      "&lsquo;Indexing&rsquo; is that test. Skip it and you can spend six months building a "
      "&lsquo;clean&rsquo; mother that quietly re-seeds your whole room with viroid."),
    defterm("RT-qPCR",
      "The gold-standard RNA test (RT-qPCR) for HpLVd. A lab amplifies any viroid genetic material in your "
      "sample until it's detectable, sensitive down to a handful of copies. You send tissue; "
      "they send back positive/negative. Many cannabis testing labs offer it cheaply per sample."),
    defterm("RT-LAMP",
      "A newer, cheaper test that runs at a single temperature (no expensive thermocycler), making "
      "in-house or field testing practical. Slightly less established than qPCR but increasingly used."),
    callout("key", "How to index properly: timing is everything",
      ul([
        "HpLVd spreads through a new plant unevenly and slowly. It reaches <strong>roots in ~2&ndash;3 weeks</strong> and <strong>foliage in ~4&ndash;6 weeks</strong> after infection.",
        "So <strong>test more than once, on more than one tissue.</strong> Roots are the most reliable early indicator; sample older and newer leaves too.",
        "Test the recovered plantlet, then <strong>re-test as it matures</strong> before you ever promote it to a production mother. A single early negative is not proof.",
      ], "tight")),
    callout("tip", "Budget for it",
      p("This is the line item the kit marketing skips. Independent HpLVd testing is the difference "
        "between hope and proof. Factor a few lab tests per candidate mother into your plan. "
        "It's cheap compared to losing a crop.")),
  ]})

# ---- 14. Multiplication -------------------------------------------------
SECTIONS.append({
  "id": "multiplication", "kicker": "14: Stage II", "title": "Multiplication, and the hyperhydricity trap",
  "blocks": [
    p("Once you have a clean, established shoot, multiplication turns one into many. You move it onto "
      "a cytokinin (shoot-pushing) medium; it produces several shoots; you cut those apart and move "
      "them onto fresh medium; repeat. Each round is a <strong>subculture</strong>, roughly every "
      "4 weeks."),
    stagecard("II", "Multiply shoots, cycle by cycle", "4&ndash;8 weeks (1&ndash;2 cycles)", "".join([
      kv([
        ("Base medium", "Full-strength MS (DKW optional)"),
        ("Hormone", "0 &ndash; ~0.5 &micro;M meta-topolin (often best hormone-free)"),
        ("Sugar / gel / pH", "30 g/L sucrose &middot; 6&ndash;9.5 g/L agar &middot; pH 5.7&ndash;5.8"),
        ("Environment", "25 &plusmn; 2 &deg;C &middot; 16 h light &middot; ~100&ndash;120 &micro;mol/m&sup2;/s"),
        ("Subculture every", "~4 weeks"),
        ("Realistic rate", "~1&ndash;6 new shoots per shoot per cycle (genotype-dependent)"),
      ]),
    ])),
    callout("note", "Counter-intuitive but well-supported: try hormone-free",
      p("You'd expect more cytokinin to mean more shoots. In cannabis, several studies found the "
        "<strong>most</strong> shoots, and the healthiest ones, on hormone-free medium, "
        "with added cytokinin actually reducing shoot count and causing glassy, deformed growth. "
        "Start low or zero, and only add hormone if you genuinely need a higher rate. (With the "
        "Athena SHOOTS sachet the hormones are pre-set and you can't change them.)")),
    h(3, "Hyperhydricity: the disorder that ruins multiplication"),
    defterm("Hyperhydricity (a.k.a. vitrification)",
      "Shoots that turn glassy, translucent, water-soaked and brittle. They look swollen and wet. "
      "Their leaves don't form a proper waxy skin or working pores, so they root badly and usually "
      "<strong>die when you try to move them to soil</strong>. It is the #1 chronic problem of "
      "cannabis multiplication."),
    p("It's caused by too much humidity in the vessel, too much cytokinin, soft watery gel, and poor "
      "air exchange. The fixes are straightforward once you know to look."),
    ul([
      "Use <strong>meta-topolin</strong> instead of older BAP, and keep cytokinin low or zero.",
      "<strong>Firm up the gel.</strong> More agar (toward 9.5 g/L) makes a drier medium the shoots like better.",
      "<strong>Ventilate</strong> the vessels (vented lids / gas-permeable closures) to let humidity and ethylene escape.",
      "<strong>Subculture on schedule</strong> (~4 weeks) so hormones and gases don't build up.",
    ]),
    h(3, "Don't subculture forever: the 5-cycle rule"),
    p("Every time you subculture, a few tiny DNA copying errors (mutations) sneak in. Recent cannabis "
      "research showed these accumulate <em>in direct proportion</em> to the number of subcultures, "
      "a near-straight-line relationship. Push it too far and your &lsquo;identical&rsquo; "
      "clones quietly drift away from the original." + R["torkamaneh2024"]),
    figure(FX.fig_subculture(), 12,
      "Mutations pile up roughly linearly with each subculture (the research found a very tight "
      "correlation). The industry rule of thumb, borrowed from banana propagation, is to reset from "
      "fresh or frozen clean stock by about the fifth cycle rather than subculturing indefinitely."),
    callout("key", "The rule",
      p("Aim to use a culture line for <strong>about 5 subcultures</strong>, then start again from a "
        "freshly cleaned explant or cryo-stored stock. This keeps your clones genuinely true-to-type.")),
  ]})

# ---- 15. Rooting --------------------------------------------------------
SECTIONS.append({
  "id": "rooting", "kicker": "15: Stage III", "title": "Rooting: turning a shoot into a plant",
  "blocks": [
    p("A multiplied shoot has no roots. Rooting fixes that with an <strong>auxin</strong> (the "
      "root-pushing hormone family). There are two routes; both work, and the second is simpler for "
      "beginners."),
    grid([
      card("Route A: in vitro rooting", p("Move shoots onto a sterile rooting medium: "
        "<strong>half-strength MS</strong> + 3% sugar + <strong>IBA ~2.5 &micro;M</strong> (~0.5 mg/L) "
        "+ a pinch of activated charcoal. Roots appear by about week 3. The most-cited cannabis result: "
        "~95% rooting, ~5 roots per shoot." + R["pmc9146626"]), tag="Sterile"),
      card("Route B: ex vitro &lsquo;dip &amp; plant&rsquo;", p("Take the shoot straight out of the "
        "jar, dip the cut end in a rooting gel (e.g. ~1,000&ndash;3,000 ppm IBA), and stick it into a "
        "moist rockwool cube under a humidity dome. Rooting and hardening happen together, outside the "
        "jar. Commercially preferred: better roots, higher survival, one less sterile step." + R["kurtz2022"]), tag="Simpler"),
    ], cols=2),
    stagecard("III", "Induce roots", "2&ndash;4 weeks", "".join([
      ul([
        "<strong>IBA is the best auxin for cannabis</strong>, roughly double the roots of IAA or NAA.",
        "Rooting substrate ranking: <strong>rockwool &gt; peat &gt; coco</strong> (rockwool's air-to-water balance and sterility win clearly).",
        "Harvest shoots for rooting from <strong>younger cultures</strong> (6&ndash;12 weeks old). Rooting success drops sharply from older, tired cultures.",
        "Expect roots in 2&ndash;4 weeks in vitro; 7&ndash;10 days for ex-vitro cuttings under a dome.",
      ], "tight"),
    ])),
    callout("note", "The Athena ROOTS sachet",
      p("Athena's ROOTS medium is their pre-mixed version of a rooting/callus medium, hormones "
        "already blended. Same idea as Route A, no measuring. As always, you can't see or tune what's "
        "in it.")),
  ]})

# ---- 16. Acclimatization ------------------------------------------------
SECTIONS.append({
  "id": "acclim", "kicker": "16: Stage IV", "title": "Acclimatisation: weaning the plantlet to the real world",
  "blocks": [
    p("This is the most heartbreaking stage to rush. A plantlet raised in a sealed jar has been "
      "living in a tropical paradise: ~100% humidity, constant warmth, sugar fed to it, dim light. "
      "Its leaves never bothered to grow a proper waxy skin or working pores. Throw it straight into "
      "room air and it wilts and dies in hours."),
    defterm("Acclimatisation (hardening / weaning)",
      "Gradually toughening the plantlet up: slowly lowering humidity and raising light over a couple "
      "of weeks, so it grows a real cuticle, working stomata and stronger roots before it has to "
      "fend for itself."),
    figure(F.fig_acclim(), 13,
      "The golden rule of hardening: step the humidity down gradually, never all at once. Start with "
      "the dome shut at high humidity, crack the vents a little wider each day, and only remove the "
      "dome entirely after roughly two to three weeks, by which time roots and a working waxy "
      "skin have formed."),
    stagecard("IV", "Harden to ambient conditions", "2&ndash;4 weeks", "".join([
      steps([
        ("Pot up", "Move the rooted plantlet into a clean, sterile substrate, either rockwool or a peat:perlite (1:2) mix, in a small pot or plug."),
        ("Dome on, high humidity", "Cover with a humidity dome / propagator at ~75&ndash;80% humidity. Keep light low at first (~50 &micro;mol/m&sup2;/s). Water gently."),
        ("Step humidity down", "Over ~2&ndash;3 weeks, open the vents a little more each day, taking humidity down toward ~55&ndash;65%. Watch for wilting and back off if needed."),
        ("Ramp light up", "As humidity falls, raise light toward ~500 &micro;mol/m&sup2;/s, roughly a tenfold increase, to build a sturdy plant."),
        ("Dome off", "Once it's holding turgor in open air and pushing new growth, remove the dome. It's now a normal young plant."),
      ]),
    ])),
    callout("warn", "The three killers at this stage",
      ul([
        "<strong>Desiccation</strong>: humidity dropped too fast, so the plant can't close its pores in time and dries out. (The #1 cause; go slow.)",
        "<strong>Hyperhydricity hangover</strong>: glassy shoots from a too-humid multiplication stage simply never harden. Fix it upstream (section 14).",
        "<strong>Damping-off</strong>: fungal rot in the warm, wet substrate. Use sterile substrate and don't overwater.",
      ], "tight")),
    callout("tip", "What good looks like",
      p("Well-run protocols report <strong>90&ndash;100% survival</strong> through hardening. Those "
        "are best-case lab numbers and your first run will likely be lower, but they show "
        "that patient, gradual weaning genuinely works." + R["page2019"])),
  ]})

# ---- 17. Re-establish mother -------------------------------------------
SECTIONS.append({
  "id": "mother", "kicker": "17: The payoff", "title": "Re-establishing the clean mother",
  "blocks": [
    p("You've arrived. The hardened plantlet, ideally one you've had lab-tested clean, "
      "is now grown on into a full <strong>mother (stock) plant</strong>, and from her you take normal "
      "cuttings the easy old-fashioned way, at scale."),
    steps([
      ("Grow her up", "Pot on and veg the clean plantlet under long days (18&ndash;24 h light) in a controlled, scrupulously clean space, ideally isolated from your old, possibly-infected plants."),
      ("Verify clean (again)", "Re-test for HpLVd as she matures, before you rely on her. Only a tested-negative plant earns the title &lsquo;clean mother&rsquo;."),
      ("Take cuttings / retips", "From the established mother, take ordinary stem cuttings or soft apical &lsquo;retips&rsquo;. Cannabis retips root at 76&ndash;81% with no hormone and &gt;90% with IBA at ~1,000 ppm: an easy way to bulk up clean stock fast."),
      ("Keep her clean", "Dedicated, sanitised tools; sanitise hands and surfaces between plants; never let an untested plant near her. Clean stock stays clean only through discipline."),
    ]),
    callout("key", "Good news on quality",
      p("Research confirms tissue-cultured mothers are <strong>chemically faithful</strong>: "
        "cannabinoid content of plants from micropropagation, retips and ordinary cuttings was the "
        "same. TC doesn't change your strain, it just hands it back to you healthy.")),
  ]})

# ---- 18. Storage / latest ----------------------------------------------
SECTIONS.append({
  "id": "advances", "kicker": "18: Going further", "title": "Storing genetics: synthetic seed & cryo (the cutting edge)",
  "blocks": [
    p("Once you can clean and multiply a strain, you can also <em>bank</em> it, preserving a "
      "clean genotype so you never have to re-clean it. Two methods are worth knowing, even as a "
      "beginner, because they're where the field is heading."),
    grid([
      card("Synthetic seed", p("A shoot tip or bud encapsulated in a soft bead of calcium alginate "
        "gel: an &lsquo;artificial seed&rsquo; you can store and ship. Proven at commercial "
        "scale in cannabis: encapsulated &lsquo;Slurricane&rsquo; buds showed 100% regrowth after "
        "150 days of storage. Good for short-to-medium-term keeping and posting genetics."), tag="Storage"),
      card("Cryopreservation", p("Freezing tiny shoot tips in liquid nitrogen (&minus;196&nbsp;&deg;C) "
        "for indefinite storage. It's the gold standard for long-term germplasm banking, and it "
        "neatly &lsquo;resets the clock&rsquo; on the subculture mutations from section 14. Real "
        "but advanced; cannabis protocols recover ~55&ndash;63% of tips." + R["karger2019_cryo"]), tag="Long-term"),
    ], cols=2),
    callout("note", "Where the industry is",
      p("Commercial clean-stock labs (Conception Nurseries, Front Range Biosciences and others) chain "
        "all of this together: test &rarr; meristem-clean &rarr; micropropagate &rarr; verify "
        "true-to-type &rarr; keep elite mothers with a frozen backup &rarr; ship clones or synthetic "
        "seed. The largest runs over 500,000 plants a month. You're doing the same pipeline in "
        "miniature." + R["tis2022"])),
    callout("tip", "A genuinely new development (2025)",
      p("Cannabis has long been &lsquo;recalcitrant&rsquo;, with regeneration only working on a few "
        "strains. A 2025 protocol using cotyledonary-node explants reported ~70&ndash;90% success "
        "across many hemp and medicinal lines, a real step toward methods that work on <em>any</em> "
        "genetics. The science here is still moving fast.")),
  ]})

# ---- 19. Troubleshooting ------------------------------------------------
SECTIONS.append({
  "id": "trouble", "kicker": "19: When it goes wrong", "title": "Troubleshooting",
  "blocks": [
    p("Nearly every beginner problem is on this list. Match the symptom, apply the fix, keep notes."),
    table(["Symptom", "Likely cause", "What to do"], [
      ["Cloudy medium / slimy ooze at the base, sour smell", "Bacterial contamination (often endophytic, from inside the mother)", "Discard the vessel. Improve mother health &amp; pre-conditioning; consider PPM in medium; tighten aseptic technique."],
      ["Fuzzy white/coloured growth spreading on the medium", "Fungal contamination (airborne spores)", "Discard immediately before it spreads. It's an air/technique issue: check your clean-air setup and tool sterilising."],
      ["Everything looked fine for 2 weeks, then crashed", "Latent endophyte erupting on rich medium", "This is why you wait &amp; watch. Start from healthier, pre-treated mother tissue; use smaller/younger explants."],
      ["Explant turns brown and dies", "Phenolic oxidation (browning)", "Add activated charcoal (~1 g/L); antioxidant dip; subculture to fresh medium early and often."],
      ["Shoots glassy, swollen, water-soaked, brittle", "Hyperhydricity / vitrification", "Lower/remove cytokinin; firmer gel (more agar); ventilate vessels; subculture on schedule."],
      ["Few or no new shoots in multiplication", "Too much hormone, or wrong genotype response", "Try hormone-free or lower cytokinin; accept that rate is strain-dependent."],
      ["Shoots won't root", "Wrong/insufficient auxin, or culture too old", "Use IBA ~2.5 &micro;M; harvest shoots from younger (6&ndash;12 wk) cultures; try ex-vitro dip-and-plant."],
      ["Plantlets wilt &amp; die when moved to soil", "Acclimatisation too fast (desiccation)", "Step humidity down slower over 2&ndash;3 weeks; keep the dome on longer; ensure good roots first."],
      ["Cleaned plant tests positive for HpLVd anyway", "Meristem too large, or strain hard to clean", "Cut a smaller dome; clean several meristems per strain; consider thermotherapy adjunct; always re-index."],
      ["Clones drifting from the original over time", "Too many subcultures (mutation build-up)", "Reset from fresh/cryo stock by ~5 subcultures."],
    ], cls="compact"),
  ]})

# ---- 20. Reality check --------------------------------------------------
SECTIONS.append({
  "id": "reality", "kicker": "20: Straight talk", "title": "The honest reality check: cost, success, and limits",
  "blocks": [
    p("So you can decide with eyes open."),
    h(3, "What success rates to actually expect"),
    table(["Stage", "Best-case lab", "Realistic beginner first runs"], [
      ["Initiation survival", "up to ~55% usable", "often much lower; 90&ndash;95% loss is reported and normal"],
      ["Rooting", "95&ndash;100%", "lower, improving with practice"],
      ["Acclimatisation survival", "90&ndash;100%", "lower on first attempts"],
      ["HpLVd clearance (per strain)", "0&ndash;100% (avg ~40%)", "strongly strain-dependent; clean &amp; test several"],
    ], caption="Published figures are best-case. Your first batch will underperform them. That's the learning curve, not failure."),
    h(3, "What it costs"),
    table(["Path", "Up-front", "Ongoing"], [
      ["DIY starter (still-air box + pressure cooker)", "~$200&ndash;$550", "media powder, bleach, agar, gel; cheap"],
      ["Serious home lab", "under ~$1,000", "consumables + optional flow hood later"],
      ["Athena Culture Kit", "~$1,800&ndash;$2,295", "media $30&ndash;$40/box, vessels $15 ea, HEPA $100"],
      ["HpLVd lab testing (essential)", "per-sample fee", "several tests per candidate mother: budget for it"],
    ]),
    callout("danger", "The four limits to be clear-eyed about",
      ol([
        "<strong>Free &ne; resistant.</strong> A cleaned plant can be re-infected instantly by a dirty tool or hand. Hygiene is forever.",
        "<strong>A kit can clean but can't prove.</strong> No qPCR test in the box = no proof of &lsquo;clean&rsquo;. Independent lab testing is mandatory, not optional.",
        "<strong>It's strain-dependent and slow.</strong> Some genetics barely clear; a verified clean mother is a multi-month project.",
        "<strong>Proprietary media is a black box.</strong> Pre-mixed kits trade tunability and troubleshooting insight for convenience: fine for many, limiting if you want to optimise.",
      ])),
    callout("key", "Bottom line",
      p("Tissue culture is the only reliable way to strip Hop Latent Viroid and other diseases out of "
        "a cannabis line and get your genetics performing like they should. It is learnable at home, "
        "a kit makes it convenient, and the biology genuinely works, <em>provided</em> you "
        "respect aseptic technique, go slow on hardening, and prove your results with a lab test "
        "rather than taking &lsquo;it looks healthy&rsquo; on faith.")),
  ]})

# ============================================================ FOOTER

FOOTER = """
<footer class="footer"><div class="wrap">
  <h3>About this guide</h3>
  <p>A first-timer's user guide to cannabis tissue culture for cleaning up genetics, synthesised
  from peer-reviewed literature (2019&ndash;2026) and current commercial practice. Product details
  for the Athena Culture Kit are from Athena Ag's own pages; some of their step-by-step figures are
  proprietary and undisclosed, and are flagged as such throughout. Figures are illustrative
  schematics, not to scale. Nothing here is legal advice: follow the cannabis laws in your
  jurisdiction.</p>

  <h3>Key sources</h3>
  <ul class="refs">
    <li>Holmes et&nbsp;al. 2021, <em>Front. Plant Sci.</em>: canonical cannabis sterilisation &amp; shoot culture. PMC8491305</li>
    <li>2024, <em>Plants/MDPI</em>: media composition &amp; explant type optimisation. PMC11434680</li>
    <li>Page et&nbsp;al. 2019, <em>Plant Methods</em>: photoautotrophic micropropagation &amp; acclimatisation schedule. PMC6660493</li>
    <li>An Alternative In&nbsp;Vitro Propagation Protocol (efficient rooting), 2022. PMC9146626</li>
    <li>Kurtz et&nbsp;al. 2022, <em>HortScience</em>: ex-vitro rooting, retips, mother stock.</li>
    <li>Somatic Mutation Accumulation in Micropropagated Cannabis, 2024, <em>Plants</em>: the 5-subculture rule. PMC11279941</li>
    <li>Hop Latent Viroid: A Hidden Threat, 2023. PMC10053334 &middot; Transmission/Management review, 2025. PMC11902214</li>
    <li>HLVd thermotherapy + meristem clearance across 13 cultivars, 2024&ndash;25 (bioRxiv 2024.04.06.588422 / PCTOC 2025).</li>
    <li>Temporary Immersion System for cannabis, 2022, <em>Front. Plant Sci.</em> &middot; Cryopreservation by droplet vitrification, Karger 2019.</li>
    <li>Athena Ag: Culture Kit, ROOTS/SHOOTS media &amp; Plant/Media/Lab Prep procedure (athenaag.com, store.athenaag.com, support.athenaag.com).</li>
  </ul>
  <p class="disc">Built as a self-contained HTML document: opens offline, no network required.
  Generated for a first-time tissue-culture grower. Verify dilutions, hormone doses and local
  regulations against primary sources before relying on them; cannabis tissue culture is strongly
  genotype-dependent and recipes often need per-strain tuning.</p>
</div></footer>
"""
