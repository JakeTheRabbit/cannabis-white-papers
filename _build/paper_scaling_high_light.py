# -*- coding: utf-8 -*-
"""Paper: scaling light to the limiting factor (advanced)."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        grid, card)
import figs_lib as L

SLUG = "scaling-high-light"
TITLE = "Scaling light to the limiting factor"
EYEBROW = "Advanced · Scaling to high light"
SUB = ("Light sets the demand. CO₂, water, airflow, feed and heat-removal have to supply it. "
       "Your yield ceiling is whichever one tops out first — so size every system to the "
       "light, find the wall, and dial the light down to meet it.")
META = [("gauge", "Advanced"), ("image", "1 diagram · 5 tables"),
        ("quote", "Evidence-linked · 4 sources"), ("clock", "~16 min read")]
RELATED = ["grow-room-systems", "co2-enrichment", "coco-crop-steering"]
REF_IDS = ["rm2021-light", "chandra2008-photo", "faust2018-dli", "collado2025-light"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

def _tag(cls, txt):
    return "<span class='tag %s'>%s</span>" % (cls, txt)

def _fig_ceiling():
    return L.bars(
        "Each system's PPFD ceiling &mdash; the lowest one wins",
        [("CO&#8322;", 1500), ("Irrigation", 1200), ("Cooling", 1140), ("Dehu", 1050)],
        unit="",
        note="Case A: 50 m&sup2; room, 6 tons cooling, 410 pints dehu, 300 L/day feed, CO&#8322; to 1500 ppm.",
        target=1050, maxv=1600)

SECTIONS = []

SECTIONS.append({"id": "demand", "kicker": "01 · Read this first",
  "title": "Light is the throttle, not the engine",
  "blocks": [
    lead("Photosynthesis runs at the speed of whatever is in shortest supply. Light can be the "
         "thing that sets the pace &mdash; but only up to the point where something else runs out. "
         "Past that point, more light does nothing except make heat and stress the plant."),
    p("This is an old rule with two names. Liebig's <strong>law of the minimum</strong> says a crop "
      "grows at the rate set by its scarcest resource, no matter how abundant everything else is. "
      "Blackman's <strong>law of limiting factors</strong> says the same about the moment-to-moment "
      "rate of photosynthesis: raise the input that is currently limiting and the rate climbs; raise "
      "anything else and nothing happens. Cannabis yield keeps rising with light to very high "
      "levels" + _c("rm2021-light") + ", but only because CO&#8322;, warmth, water and feed rise with "
      "it" + _c("chandra2008-photo") + ". A room at 1500 &micro;mol on ambient CO&#8322; is really a "
      "room running at its 800 &micro;mol ceiling, with 700 &micro;mol of wasted, heat-making light "
      "on top."),
    p("So the job is not &lsquo;turn the lights up.&rsquo; The job is to work out <strong>which "
      "system tops out first</strong>, and then either raise that ceiling or set the light to it. "
      "The companion paper <a href='grow-room-systems.html'>Grow-room systems</a> makes the case "
      "that the room is one machine; this paper puts numbers on it and shows you how to find the "
      "machine's weakest link."),
    callout("key", "The whole paper in one line",
      p("Light is a demand you create. CO&#8322;, water, feed, airflow and heat-removal are the "
        "supply. Yield tracks light <em>only while every supply line keeps up</em> &mdash; the first "
        "one that can't is your real ceiling.")),
  ]})

SECTIONS.append({"id": "terms", "kicker": "02 · The vocabulary", "title": "The words you need",
  "blocks": [
    p("Six terms carry the rest of the guide. If these are already second nature, skip to the ladder."),
    defterm("PPFD", "The intensity of usable light landing on the canopy, in &micro;mol/m&sup2;/s. "
            "This is the dial you are trying to turn up. Think &lsquo;brightness right now.&rsquo;"),
    defterm("DLI", "Daily light integral &mdash; the total light delivered over a day, in "
            "mol/m&sup2;/day. At a 12/12 flip, DLI = PPFD &times; 0.0432" + _c("faust2018-dli") +
            ". Think &lsquo;the day's total ration.&rsquo;"),
    defterm("Light saturation", "The PPFD above which a leaf can't use any more light, so the extra "
            "just becomes heat. The saturation point <em>rises</em> when you add CO&#8322; and "
            "warmth &mdash; which is the whole reason enrichment lets you run brighter" +
            _c("chandra2008-photo") + "."),
    defterm("Limiting factor", "The single input in shortest supply relative to demand. It, and only "
            "it, sets the growth rate. Every plan in this paper is a hunt for this one thing."),
    defterm("Sensible vs latent load", "Two kinds of heat your climate gear fights. <strong>Sensible"
            "</strong> is dry heat off the fixtures &mdash; the air-conditioner's job. <strong>Latent"
            "</strong> is heat locked in the water vapour the plants transpire &mdash; the "
            "dehumidifier's job. Light drives both."),
    defterm("Mass flow", "Nutrients ride into the roots dissolved in the transpiration stream. Faster "
            "transpiration pulls more water &mdash; and more feed &mdash; through the plant, which is "
            "why <a href='airflow-design.html'>airflow</a>, feed EC and light are all bolted together."),
  ]})

SECTIONS.append({"id": "ladder", "kicker": "03 · The core reference", "title": "The scaling ladder",
  "blocks": [
    p("Here is the whole system on two tables, rung by rung. Pick your light level on the left and "
      "read across: everything in that row has to be true at the same time, or the light in that row "
      "is a lie. The rungs run from an ambient-CO&#8322; room (600 &micro;mol) up to a fully-supported "
      "sealed room (1500 &micro;mol)."),
    p("The first table is the <strong>air and gas</strong> side of the row &mdash; what the plant "
      "breathes and the climate it sits in."),
    table(
      ["Light (PPFD)", "DLI", "CO&#8322; setpoint", "Day air temp", "VPD (RH)", "Canopy airspeed", "Verdict"],
      [
        ["600",  "26", "400&ndash;450 ppm", "25 &deg;C", "1.2 kPa (62%)", "0.3&ndash;0.5 m/s", _tag("g", "Ambient air is fine")],
        ["800",  "35", "600&ndash;800 ppm", "26 &deg;C", "1.3 kPa (62%)", "0.4&ndash;0.6 m/s", _tag("g", "Enrichment starts paying")],
        ["1000", "43", "800&ndash;1000 ppm", "27 &deg;C", "1.3 kPa (63%)", "0.5&ndash;0.7 m/s", _tag("w", "CO&#8322; now required")],
        ["1200", "52", "1000&ndash;1200 ppm", "28 &deg;C", "1.4 kPa (63%)", "0.6&ndash;0.8 m/s", _tag("w", "Heavy support")],
        ["1500", "65", "1200&ndash;1500 ppm", "29&ndash;30 &deg;C", "1.4 kPa (65%)", "0.7&ndash;1.0 m/s", _tag("r", "Everything maxed")],
      ],
      caption="Table 1 &middot; Climate &amp; gas targets by light level (flowering, 12/12, per m&sup2; of canopy)",
      foot="VPD barely moves &mdash; it is a plant-comfort setpoint, not something that scales with light. "
           "What scales is the water you add and remove to <em>hold</em> that VPD while transpiration climbs "
           "(Table 2). Temp is nudged up because CO&#8322; and warmth lift the light-saturation point together."),
    p("The second table is the <strong>water, feed and heat</strong> side of the same row &mdash; what "
      "you have to pour in and pull out to sustain it. This is where the cost of high light lives."),
    table(
      ["Light (PPFD)", "Transpiration (water out)", "Irrigation (water in)", "Feed EC", "Light heat", "Sensible cooling", "Dehumidification"],
      [
        ["600",  "2.2 L/m&sup2;/d", "3.0 L/m&sup2;/d", "2.0&ndash;2.4", "222 W/m&sup2;", "0.6 ton /10 m&sup2;", "4.7 pt/m&sup2;/d"],
        ["800",  "3.0 L/m&sup2;/d", "4.0 L/m&sup2;/d", "2.4&ndash;2.8", "296 W/m&sup2;", "0.8 ton /10 m&sup2;", "6.3 pt/m&sup2;/d"],
        ["1000", "3.7 L/m&sup2;/d", "4.9 L/m&sup2;/d", "2.8&ndash;3.2", "370 W/m&sup2;", "1.1 ton /10 m&sup2;", "7.8 pt/m&sup2;/d"],
        ["1200", "4.4 L/m&sup2;/d", "5.9 L/m&sup2;/d", "3.2&ndash;3.6", "444 W/m&sup2;", "1.3 ton /10 m&sup2;", "9.4 pt/m&sup2;/d"],
        ["1500", "5.6 L/m&sup2;/d", "7.4 L/m&sup2;/d", "2.4&ndash;3.2 (advanced: up to ~3.6)", "556 W/m&sup2;", "1.6 ton /10 m&sup2;", "11.7 pt/m&sup2;/d"],
      ],
      caption="Table 2 &middot; Water, feed &amp; heat-removal by light level (per m&sup2; of canopy, ~25% runoff, LED @ 2.7 &micro;mol/J)",
      foot="Rules used: transpiration &asymp; PPFD &times; 0.0037 L/m&sup2;/d; irrigation = transpiration &divide; 0.75; "
           "light heat = PPFD &divide; 2.7; dehu load = transpiration (1 L &asymp; 2.1 US pints)" + _c("collado2025-light") +
           ". Heavy CO&#8322; trims transpiration a little at the top. On HPS or 2.0 &micro;mol/J LED, add ~35% to every "
           "heat, cooling and airflow figure."),
    p("Read the two tables together and the shape of the problem jumps out. Going from 600 to 1500 "
      "&micro;mol is 2.5&times; the light &mdash; but also 2.5&times; the transpiration, feed and heat. "
      "And because you now raise <em>both</em> feed EC and irrigation volume, the actual nutrient you "
      "push through the plant each day climbs roughly <strong>five-fold</strong>, not 2.5-fold. "
      "High-light plants are not a bit hungrier. They are dramatically hungrier, wetter and hotter, "
      "all at once."),
  ]})

SECTIONS.append({"id": "room", "kicker": "04 · Worked example", "title": "One room, five light levels",
  "blocks": [
    p("Per-m&sup2; numbers are abstract, so put them in a real box. Take a <strong>50 m&sup2; "
      "flowering canopy</strong> &mdash; a 10&nbsp;m &times; 5&nbsp;m room, roughly 35 &times; 650&nbsp;W "
      "fixtures, about 150 m&sup3; of air. Multiply the ladder through and you get the actual gear list."),
    table(
      ["Light (PPFD)", "Fixture load", "Sensible cooling", "Air-handler airflow", "Dehumidification", "Irrigation", "CO&#8322; to hold"],
      [
        ["600",  "11.1 kW", "3.1 tons", "~1,250 CFM", "235 pt/day (111 L)", "148 L/day", "ambient"],
        ["800",  "14.8 kW", "4.2 tons", "~1,680 CFM", "313 pt/day (148 L)", "197 L/day", "~700 ppm"],
        ["1000", "18.5 kW", "5.3 tons", "~2,120 CFM", "391 pt/day (185 L)", "247 L/day", "~1000 ppm"],
        ["1200", "22.2 kW", "6.3 tons", "~2,520 CFM", "469 pt/day (222 L)", "296 L/day", "~1200 ppm"],
        ["1500", "27.8 kW", "7.9 tons", "~3,160 CFM", "587 pt/day (278 L)", "370 L/day", "~1400 ppm"],
      ],
      caption="Table 3 &middot; What a 50 m&sup2; canopy demands at each light level",
      foot="Sensible cooling covers the fixtures only &mdash; add the dehumidifier's reject heat and pumps in a "
           "sealed room. Air-handler airflow at ~400 CFM/ton is <em>separate</em> from the in-canopy fans that keep "
           "0.5&ndash;1.0 m/s moving through the leaves. First CO&#8322; charge of a sealed 150 m&sup3; room to 1000 ppm "
           "is only ~90 L of gas; daily burn depends mostly on how well the room seals."),
    p("Notice the last two columns between 1000 and 1500 &micro;mol. The fixtures rise 50%, but "
      "dehumidification jumps from 391 to 587 pints a day &mdash; two grow dehumidifiers to three &mdash; "
      "and cooling goes from about five tons to eight. <strong>The photons are the cheap part.</strong> "
      "The tonnage and the pints are where the money and the failures live, and they are almost always "
      "what caps a real room before the lights do."),
  ]})

SECTIONS.append({"id": "ec", "kicker": "05 · The root zone", "title": "EC climbs with light",
  "blocks": [
    p("The feed column deserves its own look, because raising EC with light is the step growers most "
      "often skip &mdash; and the one that quietly caps yield. The logic is mass flow: brighter light "
      "means faster growth, which means the plant pulls more nutrient every day. It gets that nutrient "
      "two ways at once, and <strong>both</strong> scale with light &mdash; more water moves through the "
      "plant (Table 2's transpiration column)" + _c("collado2025-light") + ", and each millilitre of "
      "that water carries more salt (higher EC). Under-feed a bright canopy and it fades from the "
      "bottom up; the light is there but the raw material isn't."),
    table(
      ["Light (PPFD)", "Feed EC (mS/cm)", "Target runoff EC", "Daily feed per m&sup2;", "Shot strategy", "If you get it wrong"],
      [
        ["600",  "2.0&ndash;2.4", "3&ndash;4", "~3.0 L", "Fewer, larger shots; wider dryback", "Under: slow, pale new growth"],
        ["800",  "2.4&ndash;2.8", "4&ndash;5", "~4.0 L", "Build shot frequency with canopy", "Balanced feed shows here"],
        ["1000", "2.8&ndash;3.2", "5&ndash;6", "~4.9 L", "Multiple shots, tighter window", "Under: lower-canopy fade"],
        ["1200", "3.2&ndash;3.6", "6&ndash;7", "~5.9 L", "Frequent shots, watch runoff EC", "Over: tip burn, crispy margins"],
        ["1500", "2.4&ndash;3.2 (advanced: up to ~3.6)", "advanced if runoff >> feed", "~7.4 L", "High frequency + volume, daily EC checks", "Either error bites fast"],
      ],
      caption="Table 4 &middot; Feed EC and root-zone strategy by light level (managed substrate, clean source water)",
      foot="Assumes a clean source (&lt;0.4 EC), a balanced high-ratio nutrient and an inert substrate. Coir buffers "
           "cations, so run the lower half of each band. See <a href='coco-crop-steering.html'>Coco &amp; crop steering</a> "
           "and <a href='nutrient-deficiencies.html'>Nutrient deficiencies</a>. Raise EC as a lever <em>after</em> "
           "irrigation volume is right, never instead of it."),
    p("There is a second reason EC and light move together: EC is also a "
      "<a href='one-steering-law.html'>steering</a> lever. A higher root-zone EC raises osmotic pressure "
      "and gently reins in water uptake, pushing the plant generative &mdash; useful in flower. So at high "
      "light you raise EC for two jobs at once: to feed the faster growth, and to hold generative balance "
      "against all that extra irrigation. The trap is raising EC to steer while forgetting volume has to "
      "rise too; starve the volume and the salts simply concentrate and burn."),
  ]})

SECTIONS.append({"id": "find", "kicker": "06 · The method", "title": "Find your limiting factor",
  "blocks": [
    p("Now the payoff. Every support system can sustain some maximum light level &mdash; a PPFD ceiling "
      "of its own. Work out the ceiling for each, and <strong>the lowest number is your room's real "
      "ceiling.</strong> Everything above it is wasted light. Here is how to turn each piece of installed "
      "gear into a PPFD number, per m&sup2; of canopy."),
    table(
      ["System", "What you have", "Its PPFD ceiling"],
      [
        ["<strong>CO&#8322;</strong>", "Your setpoint", "Ambient 420 ppm &rarr; ~800+ &micro;mol with diminishing returns (not a hard wall) &middot; 800 ppm &rarr; ~1000 &middot; 1200 ppm &rarr; ~1300 &middot; 1500 ppm &rarr; ~1500"],
        ["<strong>Cooling</strong>", "Installed sensible tons", "PPFD &le; 9,500 &times; tons &divide; m&sup2;"],
        ["<strong>Dehumidification</strong>", "Rated pints/day", "PPFD &le; 128 &times; pints/day &divide; m&sup2;"],
        ["<strong>Irrigation</strong>", "Max deliverable L/day", "PPFD &le; 200 &times; L/day &divide; m&sup2;"],
        ["<strong>Feed / EC</strong>", "Highest EC you can run", "Match the EC to its rung in Table 4"],
        ["<strong>Airflow</strong>", "Canopy air movement", "A <em>gate</em>, not a dial &mdash; see below"],
      ],
      caption="Table 5 &middot; Turn each system into its PPFD ceiling (per m&sup2; of canopy)",
      foot="All at LED 2.7 &micro;mol/J; scale the cooling constant down for less efficient fixtures. Airflow gives no "
           "clean number because it is a prerequisite: if you can't hold 0.3&ndash;1.0 m/s <em>through</em> the whole "
           "canopy, gas exchange stalls and every other ceiling drops to roughly 900&ndash;1000 &micro;mol."),
    p("Airflow is the odd one out on purpose. You can have 1500 ppm of CO&#8322; in the room and still "
      "starve the leaf if the <a href='airflow-design.html'>boundary layer</a> &mdash; the film of still "
      "air on every leaf surface &mdash; never gets stripped away. Dead air inside a dense canopy is a "
      "CO&#8322; ceiling you can't see on the room sensor. Treat airflow as a pass/fail gate you clear "
      "<em>before</em> reading any other ceiling."),
    p("Run the six numbers, take the minimum, and you have found the wall. The diagram makes it concrete "
      "for a real room."),
    figure(_fig_ceiling(), 1,
      "Four systems, four different ceilings. Cooling could take 1140 and CO&#8322; could feed 1500, but the "
      "dehumidifier tops out at 1050 &micro;mol &mdash; the amber line. That is the room's real ceiling. Run the "
      "lights at 1300 and the extra 250 &micro;mol just makes humidity the dehu can't remove. Dial to 1050, or buy "
      "more dehu."),
  ]})

SECTIONS.append({"id": "cases", "kicker": "07 · Case studies", "title": "Four rooms, four walls",
  "blocks": [
    p("The same method, four common rooms. Each has plenty of everything except one thing &mdash; and "
      "that one thing is the yield. The fix is never &lsquo;more light.&rsquo;"),
    callout("note", "Case A &middot; The dehumidifier is the wall " + _tag("w", "most common"),
      p("<strong>The room:</strong> 50 m&sup2;, 6 tons of cooling, CO&#8322; to 1500 ppm, good fans, two "
        "205-pint dehumidifiers (410 pints/day). <strong>The math:</strong> cooling ceiling 9,500&times;6&divide;50 "
        "= <strong>1140</strong>; dehu ceiling 128&times;410&divide;50 = <strong>1050</strong>; CO&#8322; ceiling "
        "<strong>1500</strong>. <strong>The wall:</strong> dehumidification, at ~1050 &micro;mol. <strong>The fix:"
        "</strong> run the lights at 1050, <em>or</em> add a third dehumidifier to unlock the 1140 the cooling "
        "already allows &mdash; then cooling becomes the next wall.")),
    callout("note", "Case B &middot; The ambient-air ceiling " + _tag("g", "cheap to fix"),
      p("<strong>The room:</strong> big cooling and dehu, but <em>no</em> CO&#8322; supplementation &mdash; "
        "ambient 420 ppm. <strong>The math:</strong> cooling and dehu might support 1200, but at ambient "
        "Under ambient CO&#8322;, leaf curves flatten earlier than canopy yield, which can still rise well past 800 " + _c("chandra2008-photo") +
        ". <strong>The practical limit:</strong> ambient CO&#8322; lowers efficiency as PPFD climbs. <strong>The fix:</strong> above ~800&ndash;1000 without enrichment, extra light often just "
        "bleaches tops and adds heat &mdash; dial down to 800, or add CO&#8322; and suddenly all that cooling and "
        "dehu headroom means something. The cheapest ceiling in the building to raise.")),
    callout("note", "Case C &middot; The stagnant canopy " + _tag("w", "hidden"),
      p("<strong>The room:</strong> CO&#8322; to 1200, strong cooling and dehu &mdash; but a thick canopy with "
        "dead, laminar air in the lower half. <strong>The math:</strong> no clean number; the boundary layer "
        "isn't stripped, so CO&#8322; can't reach the stomata inside the canopy. Effective ceiling collapses to "
        "~<strong>900&ndash;1000</strong> even though the room &lsquo;has&rsquo; 1200 ppm. <strong>The wall:</strong> "
        "airflow gate. <strong>The tell:</strong> lush outer buds, larfy damp interior. <strong>The fix:</strong> "
        "<a href='defoliation-training.html'>defoliate</a> and add under-canopy air <em>before</em> touching the "
        "lights or the CO&#8322;.")),
    callout("note", "Case D &middot; The root zone can't keep up " + _tag("w", "self-inflicted"),
      p("<strong>The room:</strong> climate and gas all support 1300, but irrigation is a couple of short shots "
        "and feed EC is stuck at 2.4. <strong>The math:</strong> the canopy wants 4.5+&nbsp;L/m&sup2;/day and 3.4 "
        "EC; it's getting ~3&nbsp;L and 2.4. Water ceiling 200&times;(deliverable L)&divide;m&sup2; lands near "
        "<strong>900</strong>, and the low EC caps the same rung. <strong>The wall:</strong> irrigation volume + "
        "EC. <strong>The tell:</strong> midday wilt and a pale, fading lower canopy. <strong>The fix:</strong> get "
        "shot volume and frequency right first, <em>then</em> climb EC up Table 4 &mdash; not the other way round.")),
  ]})

SECTIONS.append({"id": "dial", "kicker": "08 · The decision", "title": "Dial the light to the wall",
  "blocks": [
    p("Once you know your lowest ceiling, you have exactly two honest moves."),
    p("<strong>Move one: set the light to the wall.</strong> If your ceiling is 1050 &micro;mol, run 1050. "
      "The photons above it were never converting to yield &mdash; they were converting to heat, humidity "
      "and stress. Dialling down to the wall costs nothing in growth and hands back power, cooling headroom "
      "and a calmer room. On dimmable fixtures this is free and immediate."),
    p("<strong>Move two: raise the wall, then re-check.</strong> Spend on the <em>limiting</em> system and "
      "nothing else. Adding CO&#8322; to a Case-B room is transformative; adding CO&#8322; to a Case-A room "
      "does nothing, because dehu &mdash; not CO&#8322; &mdash; is the wall. And the part people miss: "
      "<strong>the moment you raise one ceiling, a different system becomes the wall.</strong> Fix the dehu "
      "in Case A and cooling caps you at 1140. Chase the ceiling in the wrong order and you buy gear that "
      "changes nothing."),
    callout("warn", "Running light above the wall is worse than wasteful",
      p("It isn't neutral. Excess light past your limiting factor bleaches and foxtails tops, drives leaf "
        "temp and VPD up, and &mdash; when the dehu is the wall &mdash; pushes humidity into "
        "<a href='mould-risk.html'>bud-rot</a> territory. You pay for the extra electricity <em>and</em> lose "
        "quality. The dial-down is the rare free lunch.")),
    p("There is also an economic ceiling below the biological one. Yield keeps climbing toward "
      "1500&ndash;1800 &micro;mol" + _c("rm2021-light") + ", but the tons and pints needed to support the top "
      "rungs climb faster than the yield does. The last 300 &micro;mol might cost a third dehumidifier and a "
      "bigger AC to buy a single-digit-percent bump. Find your <em>economic</em> wall &mdash; where the next "
      "100 &micro;mol stops paying for its own climate gear &mdash; and it often sits a rung below what the "
      "plants could theoretically use."),
  ]})

SECTIONS.append({"id": "trouble", "kicker": "09 · When it goes wrong", "title": "Troubleshooting",
  "blocks": [
    p("Every row here is a limiting factor showing itself. The symptom tells you which wall you hit."),
    table(
      ["Symptom", "Which wall you hit", "What to do"],
      [
        ["Bleached, foxtailed tops under big light", "Light above your CO&#8322; ceiling; tops light-saturated", "Add CO&#8322;, or dial light to the ambient ceiling (~800)"],
        ["RH won't come down; VPD collapses midday", "Transpiration outran dehumidification", "Add dehu capacity or trim light &mdash; usually the real ceiling"],
        ["Big light, flat yield", "CO&#8322;, water or feed didn't scale with the light", "Find the lowest ceiling; raise it or dial light to it"],
        ["Midday wilt at peak light", "Irrigation volume &lt; transpiration", "Bigger/more shots; fix volume before touching EC"],
        ["Pale, fading lower canopy late in flower", "Feed EC too low for the light level", "Step EC up Table 4; check runoff EC"],
        ["Tip burn, crispy leaf margins", "Feed EC too high for the light (above the rung)", "Drop EC a step, or raise light/volume to match"],
        ["Lush outside, larfy damp interior", "Airflow gate &mdash; boundary layer not stripped inside", "Defoliate + under-canopy air; CO&#8322; can't work in dead air"],
      ],
      cls="compact"),
  ]})

SECTIONS.append({"id": "expect", "kicker": "10 · Straight talk", "title": "Realistic expectations",
  "blocks": [
    p("Cannabis yield really does track light almost linearly, up to roughly 1500&ndash;1800 &micro;mol" +
      _c("rm2021-light") + " &mdash; but that finding comes with fine print those studies never hide: it "
      "holds <em>only</em> when CO&#8322;, temperature, water and feed are all lifted to match. Strip the "
      "support away and the same lights give you bleached tops and a heat problem. The linear curve is a "
      "promise conditional on the whole convoy keeping up."),
    p("So spend your attention where the wall is, not where the catalogue is. The most common real ceilings, "
      "in rough order, are dehumidification, then cooling, then CO&#8322;, then root-zone delivery &mdash; and "
      "the cheapest yield you will ever buy is usually removing your current limiting factor, not adding "
      "another kilowatt of light. Measure the things that reveal the wall: leaf temperature, runoff EC, "
      "canopy-level RH and airspeed, room CO&#8322; under the canopy. A gauge at the room's edge won't show "
      "you the dead, humid air where the plant actually lives."),
    callout("key", "What to remember",
      ol([
        "Light is a demand. <strong>Size CO&#8322;, water, feed, airflow and heat-removal to supply it</strong> (Tables 1&ndash;2).",
        "Turn each installed system into a <strong>PPFD ceiling</strong>; the <strong>lowest wins</strong> (Table 5).",
        "<strong>Set the light to that wall</strong> &mdash; running above it wastes power and costs quality.",
        "To go higher, <strong>raise the limiting system, then re-check</strong> &mdash; the wall moves.",
      ])),
    p("This paper is one lever of the room. Read it alongside <a href='grow-room-systems.html'>Grow-room "
      "systems</a>, <a href='co2-enrichment.html'>CO&#8322; enrichment</a> and "
      "<a href='airflow-design.html'>Airflow design</a>."),
  ]})
