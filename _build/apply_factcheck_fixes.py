# -*- coding: utf-8 -*-
"""Apply fact-check review rewrites to paper modules + site shell.

Run from _build/:  python apply_factcheck_fixes.py
Then:              python build.py
"""
from __future__ import annotations
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)

def read(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def write(path: str, text: str) -> None:
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)

def replace_all(text: str, pairs: list[tuple[str, str]], label: str) -> str:
    for old, new in pairs:
        if old not in text:
            # try normalized quotes / dashes variants already in source
            continue
        count = text.count(old)
        text = text.replace(old, new)
        print(f"  [{label}] x{count}: {old[:70]!r}...")
    return text

def must_contain_or_warn(text: str, needle: str, label: str) -> None:
    if needle not in text:
        print(f"  WARN [{label}] missing expected fragment: {needle[:80]!r}")

# ---------------------------------------------------------------------------
# Global META badge: "Peer-reviewed · N sources" → evidence-linked framing
# ---------------------------------------------------------------------------
def fix_meta_badges(path: str) -> None:
    t = read(path)
    orig = t
    t = re.sub(
        r'\("quote", "Peer-reviewed[^"]*"\)',
        lambda m: m.group(0).replace("Peer-reviewed", "Evidence-linked", 1)
                  .replace("Peer-reviewed +", "Evidence-linked ·"),
        t,
    )
    # catch remaining Peer-reviewed in META quote lines only
    t = t.replace('("quote", "Peer-reviewed', '("quote", "Evidence-linked')
    t = t.replace("Peer-reviewed + Grodan", "Evidence-linked · Grodan")
    t = t.replace("Peer-reviewed + trials", "Evidence-linked · trials")
    t = t.replace("Peer-reviewed + safety", "Evidence-linked · safety")
    if t != orig:
        write(path, t)
        print(f"META badges: {os.path.basename(path)}")

# ---------------------------------------------------------------------------
# Per-file content fixes
# ---------------------------------------------------------------------------
FIXES: dict[str, list[tuple[str, str]]] = {}

FIXES["paper_seeds_germination.py"] = [
    (
        "The newborn seedling has almost no roots, so it drinks largely through its leaves. That "
        "means it needs high humidity, typically 65-80% RH (a VPD of about 0.4-0.8 kPa), often using a "
        "humidity dome or a vented clear bag for the first 7-10 days.",
        "A newborn seedling has a tiny root system, so it loses water easily. High humidity "
        "(typically 65-80% RH, a VPD of about 0.4-0.8 kPa) reduces how hard the air pulls water from "
        "the leaves until roots expand — often with a humidity dome or vented clear bag for the first "
        "7-10 days. Roots still do the drinking; the dome buys time.",
    ),
    (
        "the most popular because you can watch the taproot appear, and it reports near-99% success "
        "when conditions are controlled.",
        "the most popular because you can watch the taproot appear. With fresh seed and steady "
        "warmth and moisture, high germination is common — method choice matters less than seed "
        "quality, temperature, and damp (not soaked) conditions.",
    ),
    (
        "Germination just means giving the seed three things: water, warmth and darkness.",
        "Germination mainly needs water and warmth (and time). Most people also keep seeds dark for "
        "convenience and to avoid drying out, but light is not toxic to germination.",
    ),
    (
        "Keep the medium or towel damp like a wrung-out sponge, never waterlogged, and keep seeds in darkness until they sprout.",
        "Keep the medium or towel damp like a wrung-out sponge, never waterlogged. Darkness is fine "
        "and common; moisture and temperature matter more than strict darkness.",
    ),
    (
        "- **Light:** darkness while germinating. Once sprouted, give gentle light immediately so the stem does not stretch.",
        "- **Light:** optional darkness while germinating (convenience). Once sprouted, give gentle light immediately so the stem does not stretch.",
    ),
    (
        "Photoperiod plants (regular and feminised) only flower when the daily light drops to about 12 hours.",
        "Photoperiod plants (regular and feminised) flower when nights are long enough without light "
        "interruptions — growers usually use 12 hours light / 12 hours dark as a reliable default.",
    ),
    (
        "so the resulting seeds carry only female genetics.",
        "so almost all offspring are female — though stress-related hermaphroditism can still appear.",
    ),
    (
        '["Sex outcome", "~50% male / 50% female", "~99% female", "~99% female"],',
        '["Sex outcome", "~50% male / 50% female", "~99% female (if feminised)", "Feminised autos ~99% female; regular autos ~50/50"],',
    ),
    (
        '["Sex outcome", "~50% male / 50% female", "~99% female", "~99% female"]',
        '["Sex outcome", "~50% male / 50% female", "~99% female (if feminised)", "Feminised autos ~99% female; regular autos ~50/50"]',
    ),
]

FIXES["paper_cloning.py"] = [
    (
        "Water the mother with <strong>half-strength</strong> nutrients the day before. This lowers the "
        "pressure inside the leaves and stems (their turgor) so the stems are less brittle and the cut "
        "is cleaner.",
        "Water the mother thoroughly the day before so cuttings are fully hydrated and turgid. "
        "Wilted or drought-stressed mothers root poorly; firm, well-watered tissue takes cleaner cuts "
        "and holds water status better after cutting.",
    ),
    (
        "Water the mother with **half-strength** nutrients the day before. This lowers the pressure inside the leaves and stems (their turgor) so the stems are less brittle",
        "Water the mother thoroughly the day before so cuttings are fully hydrated and turgid. Avoid drought-stressed mothers; wilted tissue roots poorly",
    ),
]

# cloning may use different HTML-escaped forms - we'll read and fix flexibly

FIXES["paper_tissue_culture.py"] = [
    (
        "and even passes through seed (up to 100% in one cannabis cross).",
        "and can pass through seed and pollen at meaningful rates (often reported in the single digits "
        "to tens of percent depending on parent infection and genotype — test seed lots if purity matters).",
    ),
    (
        "Infected plants can lose up to <strong>~50% of cannabinoids</strong>",
        "In severe symptomatic &lsquo;dud&rsquo; outbreaks, plants can lose a large fraction of "
        "cannabinoids (industry reports sometimes cite losses approaching <strong>~50%</strong>)",
    ),
    (
        "Surveys found HpLVd in roughly <strong>90% of California facilities</strong>\n"
        "and ~40% of Canadian dispensary flower. If you've cloned for years, assume you may have it.",
        "Industry and research surveys have reported very high facility infection rates in California "
        "(~90% in one large testing programme) and frequent positives in Canadian retail flower "
        "(~40% in one study). Treat these as strong warning signals, not a permanent global prevalence "
        "number. If you've cloned for years, assume you may have it.",
    ),
    (
        "Almost every living plant cell carries the complete instructions to rebuild the whole plant. "
        "Give a tiny scrap of the right tissue the right food and the right hormones and it grows roots, "
        "shoots and leaves: a complete new plant. This ability is called <strong>totipotency</strong>. "
        "You are not growing a &lsquo;sample&rsquo;, you are growing a whole new copy.",
        "Many plant cells can, under the right sterile conditions and hormones, regenerate a whole plant "
        "(<strong>totipotency</strong>). In cannabis, only some tissues and genotypes do this reliably "
        "&mdash; which is why early losses are high and the species is called recalcitrant. You are not "
        "growing a &lsquo;sample&rsquo;; when it works, you grow a whole new copy.",
    ),
    (
        "HpLVd gets the headlines, but a clean start also leaves behind fungal root-rots (<em>Fusarium</em>, "
        "<em>Pythium</em>), grey mould (<em>Botrytis</em>), powdery mildew, various viruses, and even "
        "hitch-hiking pests like russet and broad mites and their eggs. You begin clean at the cellular "
        "level instead of fire-fighting forever.",
        "HpLVd gets the headlines. Meristem work plus indexing mainly targets <em>systemic</em> agents "
        "(viroids/viruses). Surface sterilisation removes many surface microbes and hitch-hiking pests "
        "from the explant, but endophytic fungi/bacteria can still emerge later, and mites are an ongoing "
        "hygiene/IPM problem &mdash; not something meristem culture permanently solves alone. You start "
        "cleaner at the tissue level; you still need discipline afterwards.",
    ),
    (
        "The kit does the meristem cut but ships <em>no</em> DNA test (qPCR)",
        "The kit does the meristem cut but ships <em>no</em> RT-qPCR test",
    ),
    (
        "RT-qPCR &mdash; The gold-standard DNA/RNA test",
        "RT-qPCR &mdash; The gold-standard RNA test (reverse-transcription then qPCR)",
    ),
    (
        "DNA test for a viroid",
        "lab test (RT-qPCR) for a viroid",
    ),
]

FIXES["paper_light_acclimation.py"] = [
    (
        "The 12/12 flip cuts total daily light (DLI) by about 28% even at the same PPFD,",
        "The 12/12 flip cuts total daily light (DLI) by about one-third (~33%) even at the same PPFD,",
    ),
]

FIXES["paper_flowering_stages.py"] = [
    (
        "More clear or milky gives a more energetic, heady effect. More amber means THC is degrading "
        "toward CBN for a heavier, more sedative effect.",
        "Many growers harvest around mostly cloudy trichomes with a little amber. Later harvests often "
        "feel more &lsquo;heavy,&rsquo; but effect is multi-factor (terpenes, minor cannabinoids, dose, "
        "genotype) &mdash; amber percentage is a maturity proxy, not a clean energy-vs-sedation switch, "
        "and human evidence that CBN alone drives couch-lock is limited.",
    ),
    (
        '["Trichomes", "80-90% milky, 5% amber", "Peak window (early)", "Energetic, heady"],\n'
        '        ["Trichomes", "Milky with 10-15% amber", "Peak window (late)", "Balanced"],\n'
        '        ["Trichomes", "30%+ amber, leaves yellow", "Over-ripe", "Sedative, couch-lock"],',
        '["Trichomes", "80-90% milky, 5% amber", "Peak window (early)", "Common early-cut target"],\n'
        '        ["Trichomes", "Milky with 10-15% amber", "Peak window (late)", "Common balanced target"],\n'
        '        ["Trichomes", "30%+ amber, leaves yellow", "Over-ripe", "Often denser/heavier feel; genotype still dominates"],',
    ),
    (
        "Even a phone-screen of light, repeated, can cause hermies",
        "Bright or repeated night interruptions can stall flowering; genetics and multi-stress drive most herms",
    ),
    (
        "many growers lower or flush nutrients in the last 1 to 2 weeks.",
        "many growers ease feed strength in the last 1 to 2 weeks as appetite falls. A long plain-water "
        "&lsquo;flush&rsquo; is traditional, but controlled tests often find little taste or potency benefit "
        "&mdash; avoid starving plants into a collapse.",
    ),
    (
        '["8-10", "Ripening", "Pistils darken, trichomes go milky", "900", "24 C / 20 C", "45% / 1.2", "Lower RH, flush, read trichomes"],',
        '["8-10", "Ripening", "Pistils darken, trichomes go milky", "900", "24 C / 20 C", "45% / 1.2", "Lower RH, ease EC, read trichomes"],',
    ),
    (
        "For the first 2 to 3 weeks after the flip the plant stretches, often nearly doubling in height",
        "For the first 2 to 3 weeks after the flip the plant stretches &mdash; many hybrids gain ~1.5&ndash;2&times; "
        "height, some barely stretch, and some more than double",
    ),
]

FIXES["paper_coco_crop_steering.py"] = [
    (
        "controlled water-deficit has been shown to raise cannabinoid content without costing yield",
        "one carefully timed late-flower drought study raised cannabinoid concentrations "
        "(a related idea to daily drybacks, but not the same protocol)",
    ),
    (
        "Flush / finish &mdash; Lower EC feeds in the final stretch.",
        "Finish &mdash; Step EC down as demand falls late; long plain-water flushes have weak evidence for quality gains.",
    ),
]

FIXES["paper_rockwool_crop_steering.py"] = [
    (
        "so <strong>100% of what you put in goes straight to the plant</strong>",
        "so root-zone EC is basically the EC of the water in the pores &mdash; precise, but unused feed still leaves as runoff or concentrates as the slab dries",
    ),
    (
        "Below roughly 25&ndash;30% WC the slab will not rewet from the dripper",
        "If a slab gets too dry, fibres can stop wicking (often discussed around the mid-20s&ndash;30% WC band, product-dependent)",
    ),
]

FIXES["paper_one_steering_law.py"] = [
    (
        "Root rot above ~23 C within a day if air pump dies",
        "Warm, poorly oxygenated solution speeds root disease (monitor DO; many aim ~18&ndash;21 C)",
    ),
]

FIXES["paper_harvest_dry_trim_cure.py"] = [
    (
        "Done well, simply dialling in this stage is reported to add 5-10% to final yield, because most growers are accidentally over-drying and losing sellable weight.",
        "Done well, dialling in this stage often recovers sellable mass and aroma versus bone-dry flower. "
        "Vendor education sometimes cites roughly 5&ndash;10% recovered weight &mdash; treat that as illustrative, not a guaranteed multi-site result.",
    ),
    (
        "essentially nothing grows below about 0.60 aw.",
        "risk rises sharply toward ~0.70 aw and above; below ~0.55 quality often suffers even as microbes slow. ASTM&rsquo;s 0.55&ndash;0.65 window is the practical target for dried flower.",
    ),
    (
        "which lands around 10% in practice (a real example batch came in at 10.46%). That tells you how much of the harvested mass is water.",
        "which is often on the order of ~10% of whole-plant wet weight in many rooms (a real example batch came in at 10.46%), "
        "but depends on stem share, trim, and how wet weight is defined &mdash; log your own genetics. "
        "Do not confuse whole-plant ratios with bud-only dry-down.",
    ),
    (
        "Trimming itself lowers water activity, so flower that took down at 0.62 aw often reads 0.58-0.60 aw once trimmed",
        "After dry-trim, re-check aw &mdash; handling and leaf removal can change the reading, so do not assume the hang-dry number still holds",
    ),
]

FIXES["paper_gmp_hash_lab.py"] = [
    (
        "Extraction multiplies contaminants ~5- to 10-fold",
        "Extraction can concentrate contaminants several-fold (often ~5&ndash;10&times; when mass yield is ~10&ndash;20% and residues follow the resin &mdash; not universal for every process)",
    ),
]

FIXES["paper_grow_room_systems.py"] = [
    (
        "improving CO2 uptake and water-use efficiency while lowering water loss",
        "improving CO2 uptake and water-use efficiency (more carbon fixed per unit water). Absolute water use often still rises in bright rooms",
    ),
    (
        "Most growth happens around 0.8&ndash;1.2 kPa",
        "A practical mid-band for many indoor crops is around 0.8&ndash;1.2 kPa (cultivar-dependent; cannabis often stretches toward ~1.2&ndash;1.5 kPa late flower)",
    ),
]

FIXES["paper_lighting_fundamentals.py"] = [
    (
        "Light obeys the inverse-square law: roughly doubling the distance from the canopy cuts PPFD by about 75%.",
        "Intensity falls with distance, but the inverse-square law (quarter intensity at 2&times; distance) is a point-source ideal. "
        "Multi-bar LED panels at typical hang heights fall off more gently &mdash; use the fixture PPFD map and a meter.",
    ),
    (
        "Red light, 600 to 700 nm, is the most photosynthetically efficient band and drives flowering and stretch",
        "Red light, 600 to 700 nm, is the most photosynthetically efficient band; stretch is driven more by low blue and far-red (low R:FR) than by red alone, and flowering is set by photoperiod",
    ),
    (
        '["600-700", "Red", "Highest photosynthetic efficiency, drives flowering and stretch", "Flower"],',
        '["600-700", "Red", "Highest photosynthetic efficiency; flowering is photoperiod-driven", "Flower"],',
    ),
    (
        "| Clone / seedling | 100-300 | ~10-15 | 18/6 |\n"
        "| Early veg | 300-450 | ~20-29 | 18/6 |\n"
        "| Late veg | 450-600 | ~29-39 | 18/6 |\n"
        "| Flower (no CO2) | 700-900 | ~30-45 | 12/12 |\n"
        "| Flower (CO2 1000-1200 ppm) | 1000-1400 | ~40-60 | 12/12 |",
        "| Clone / seedling | 100-250 | ~6-16 | 18/6 |\n"
        "| Early veg | 300-450 | ~19-29 | 18/6 |\n"
        "| Late veg | 450-600 | ~29-39 | 18/6 |\n"
        "| Flower (no CO2) | 700-900 | ~30-39 | 12/12 |\n"
        "| Flower (CO2 1000-1200 ppm) | 1000-1400 | ~43-60 | 12/12 |",
    ),
    (
        "Clones and seedlings want about 100-300 PPFD (DLI ~10-15 mol)",
        "Clones and seedlings want about 100-250 PPFD (DLI roughly ~6-16 mol on 18/6; many start ~150-200)",
    ),
    (
        "and flower about 700-900 PPFD without added CO2 (DLI ~30-45 mol)",
        "and flower about 700-900 PPFD without added CO2 (DLI ~30-39 mol on 12/12)",
    ),
    (
        "600 PPFD x 18h (veg) is roughly the same daily dose as 800 PPFD x 12h (flower).",
        "600 PPFD x 18h (~39 mol) is closer to ~900 PPFD x 12h than to 800 PPFD x 12h (~35 mol).",
    ),
    (
        "*Stage targets. 600 PPFD x 18h (veg) is roughly the same daily dose as 800 PPFD x 12h (flower).*",
        "*Stage targets. Match DLI with a meter; 600 PPFD x 18h (~39 mol) approximates ~900 PPFD x 12h.*",
    ),
    (
        "Modern LED is the efficiency leader at roughly 2.7-3.0 umol/J for good fixtures (budget units 2.0-2.3), runs cooler, and lasts longer",
        "Modern LED is the efficiency leader at roughly 2.7-3.5 umol/J for good fixtures (budget units ~2.0-2.5), runs cooler, and lasts longer",
    ),
]

FIXES["paper_under_canopy_lighting.py"] = [
    (
        "mid and lower canopy is already <strong>red-rich and far-red-dominant</strong> &mdash; the upper leaves absorbed the blue and red",
        "mid and lower canopy is depleted in blue and red and relatively <strong>enriched in green and far-red</strong> &mdash; the upper leaves absorbed much of the blue and red",
    ),
    (
        "red-rich and far-red-dominant",
        "green- and far-red-enriched (blue/red depleted)",
    ),
    (
        "full air exchange every 1&ndash;3 minutes",
        "strong recirculation (sealed rooms: recirculate and dehumidify; do not continuously dump CO&#8322; with vented-room ACH math)",
    ),
    (
        "full air exchange every 1-3 minutes",
        "strong recirculation (sealed rooms: recirculate and dehumidify; do not continuously dump CO2 with vented-room ACH math)",
    ),
    (
        "photosystems I and II must be excited roughly equally",
        "photosystems I and II work best with a balanced spectrum over time",
    ),
    (
        "Viability floor 400&ndash;500",
        "Common commercial target band ~300&ndash;600",
    ),
]

FIXES["paper_co2_enrichment.py"] = [
    (
        "tomato yield rises up to ~80% at 1,000 ppm",
        "many greenhouse C3 crops gain on the order of tens of percent at ~800&ndash;1,200 ppm (extreme published uplifts depend on depleted controls and system)",
    ),
    (
        "its water-use efficiency roughly <strong>doubles</strong>",
        "its water-use efficiency often rises substantially (sometimes toward a large fraction of a doubling in short-term leaf measurements)",
    ),
    (
        "1,000&ndash;2,500 ppm | Measurable dip in concentration and decision-making | Cognition, not danger",
        "1,000&ndash;2,500 ppm | Some indoor studies report small cognitive effects (literature mixed) | Reason for good ventilation during long occupancy, not hard toxicity",
    ),
    (
        "potentially toward percent-level concentrations.",
        "and, if sealed and packed, possibly higher &mdash; measure your own room rather than guessing.",
    ),
    (
        "Because CO2 is denser than air it sinks, so run the supply line above the canopy",
        "At enrichment ppm, fan mixing dominates density differences; still run the supply above the canopy and mix with HAF fans. Pure leaks can pool low, so put life-safety sensors near the floor. Run the supply line above the canopy",
    ),
]

FIXES["paper_scaling_high_light.py"] = [
    (
        "Ambient 420 ppm &rarr; ~800 &micro;mol",
        "Ambient 420 ppm &rarr; diminishing returns (not a hard wall)",
    ),
    (
        "leaf light-saturates around <strong>800</strong> &micro;mol",
        "leaf gas-exchange saturates earlier than canopy yield; whole-plant flower yield can still rise well past 800 &micro;mol under ambient CO&#8322;",
    ),
    (
        "the leaf light-saturates around <strong>800</strong>",
        "leaf curves flatten earlier than canopy yield; canopy yield can still rise well past <strong>800</strong>",
    ),
]

FIXES["paper_substrates_overview.py"] = [
    (
        "within minutes of watering regardless of your water's pH, so you generally do not pH your input at all",
        "over hours to days when the biology is healthy. Many organic growers do not acidify routine waterings, but still avoid extreme alkaline water and monitor slurry/pour-through if problems appear",
    ),
    (
        "Root rot within ~24h",
        "Root health can collapse quickly",
    ),
    (
        "rot within a day",
        "rot can progress quickly",
    ),
]

FIXES["paper_water_quality.py"] = [
    (
        "dissolved oxygen falls from about 5-6 ppm at 20 C to only 3-4 ppm at 26 C",
        "saturation dissolved oxygen is roughly ~9 mg/L at 20 C and ~8 mg/L at 26 C, but warm water still raises pathogen risk because DO is harder to keep high under root demand",
    ),
    (
        "dissolved oxygen falls from about 5&ndash;6 ppm at 20&nbsp;&deg;C to only 3&ndash;4 ppm at 26&nbsp;&deg;C",
        "saturation dissolved oxygen is roughly ~9&nbsp;mg/L at 20&nbsp;&deg;C and ~8&nbsp;mg/L at 26&nbsp;&deg;C, but warm water still raises pathogen risk because DO is harder to keep high under root demand",
    ),
    (
        "capped near <strong>800&ndash;900 ppm</strong>",
        "part of your total EC budget (set flower targets in mS/cm, not a fixed 800&ndash;900 ppm ceiling)",
    ),
    (
        "capped near <strong>800-900 ppm</strong>",
        "part of your total EC budget (set flower targets in mS/cm, not a fixed 800-900 ppm ceiling)",
    ),
    (
        "30&ndash;60",
        "40&ndash;80",
    ),
]

FIXES["paper_ph_management.py"] = [
    (
        "pH Down is usually phosphoric acid and pH Up is usually potassium hydroxide.",
        "Common pH downs include phosphoric, nitric, sulfuric, or organic acids; common pH ups include KOH or potassium carbonate. Each adds nutrients &mdash; account for them.",
    ),
    (
        "Aim to keep feed and runoff EC within about 10 percent of each other.",
        "For beginners, large runaway gaps (runoff &raquo; feed) mean salt buildup. Advanced crop-steering may hold higher root-zone EC intentionally &mdash; know which mode you are in.",
    ),
    (
        "Drop it too low, below about 5.5, and calcium, magnesium and phosphorus lock out instead.",
        "Drop it too low, below about 5.5, and calcium, magnesium and phosphorus availability can fall while iron and manganese can push toward toxicity &mdash; stay in band.",
    ),
    (
        "Ideal irrigation alkalinity is roughly 60-100 ppm CaCO3.",
        "Ideal irrigation alkalinity is roughly 40-80 ppm CaCO3 (many soilless programmes sit near 60-100).",
    ),
    (
        "Ideal irrigation alkalinity is roughly 60&ndash;100 ppm CaCO3.",
        "Ideal irrigation alkalinity is roughly 40&ndash;80 ppm CaCO3 (many soilless programmes sit near 60&ndash;100).",
    ),
]

FIXES["paper_nutrient_mixing_athena.py"] = [
    (
        "roughly four to five times saltier than seawater",
        "roughly six to seven times saltier than seawater (~35 g/L)",
    ),
]

FIXES["paper_nutrient_deficiencies.py"] = [
    (
        "Runoff much higher than input (e.g. more than 200 PPM higher) means salt buildup",
        "Runoff rising ~0.3&ndash;0.5 mS/cm (or more) above feed for days means salt buildup",
    ),
    (
        "Runoff more than about 200 PPM above input indicates salt",
        "Runoff rising ~0.3&ndash;0.5 mS/cm (or more) above feed indicates salt",
    ),
    (
        "Sulfur (S) | Immobile | New / top | Pale or yellow new leaves overall | Whole new leaf pales, not interveinal",
        "Sulfur (S) | Limited mobility | New / top | Pale or yellow new leaves overall | Whole new leaf pales; can mimic N but starts younger",
    ),
]

FIXES["paper_mould_risk.py"] = [
    (
        "Keep flowering RH in the ~60-70% band, lower in late flower",
        "Early flower often ~55-65% RH; mid/late flower commonly ~45-55% (sometimes lower at night) with strong through-canopy air",
    ),
    (
        "Keep flowering RH in the <strong>~60&ndash;70%</strong> band, lower in late flower",
        "Early flower often <strong>~55&ndash;65%</strong> RH; mid/late flower commonly <strong>~45&ndash;55%</strong> with strong through-canopy air",
    ),
    (
        "fungal infections at roughly <strong>3.5&times;</strong> the rate of non-users",
        "coded fungal infections about <strong>3.5&times;</strong> more often than non-users in one large claims analysis (absolute rates still low; immunocompromised patients remain the high-stakes group)",
    ),
]

FIXES["paper_pppe.py"] = [
    (
        "alcohol-based handrub achieves a larger log reduction (~3 log, ~83%) than plain soap-and-water washing (~2 log, ~58%)",
        "alcohol-based handrubs often achieve ~2&ndash;3 log reductions of transient flora when used correctly (~99&ndash;99.9% under test conditions); soap and water remove soil and many organisms but do not sterilise hands",
    ),
    (
        "Move people, materials and waste one way, dirty to clean, never back.",
        "Move people and clean materials clean &rarr; dirty; waste and used PPE only dirty &rarr; exit. Never reverse without re-gowning.",
    ),
    (
        "on the order of 70 to 90 percent",
        "typically the dominant share (exact percent varies by facility design)",
    ),
    (
        "order of magnitude filthier than a toilet seat",
        "a high-touch fomite that contacts faces and hands and cannot be fully cleaned in production",
    ),
    (
        "with up to <strong>100% transmission within four weeks</strong> of propagation from infected stock",
        "and under experimental mechanical-transmission conditions infection of linked cuttings can approach complete cohort infection within weeks",
    ),
]

FIXES["paper_ipm_sop.py"] = [
    (
        "plus sulphur (1 to 3 tablespoons per litre, ideally 3, no more than once every 2 weeks, veg and mothers only)",
        "plus sulphur only if lawful for your crop and product pathway, at the <em>current label rate</em> and REI/PHI for that registered product "
        "(never invent kitchen tablespoon rates; veg and mothers only when residues allow)",
    ),
    (
        "Predators are harmless to the plant and to people. There is no residue and no withholding period.",
        "Predatory arthropods typically leave no chemical residue or PHI, but microbials follow product labels, "
        "worker allergy risk is real for some beneficials, and every agent must be legal in your jurisdiction before release.",
    ),
    (
        "plants are treated only from mothering through day 21 of flower, with no foliar treatment after buds form",
        "many residue-aware facilities hard-stop foliar after early flower (example: day 21) because buds trap residues; "
        "your legal PHI, product pathway, and QA SOP control the real cutoff",
    ),
    (
        "Once more than 3 percent of a room is affected, escalate to approved pesticide applications",
        "As an example two-tier planning default, once more than 3 percent of a room is affected, escalate to approved pesticide applications "
        "(zero-tolerance organisms and clean-stock rooms override any percentage)",
    ),
    (
        "Spray when the media is fully saturated so the product is not pulled into the leaves",
        "Avoid foliar applications under high light, high VPD, or drought stress; irrigate so plants are not wilted before spraying",
    ),
    (
        "metallic hose clamps that can rust and fail heavy-metals testing",
        "corroding product-contact or fertigation hardware that can contribute to metals contamination in some cases",
    ),
]

FIXES["paper_pest_id.py"] = [
    (
        "The cycle runs as fast as 3 days at 27C / ~20% RH, and one female can lay up to ~200 eggs.",
        "Under hot, dry conditions egg-to-adult often finishes in about a week (sometimes under two weeks); "
        "females often lay on the order of ~100 eggs over life (exact times depend on temperature and host).",
    ),
    (
        "roughly one card per 1,000 square feet as a minimum",
        "a mapped density (example: ~1 card / 100 m&sup2; or ~1,000 sq ft) as a starting point",
    ),
]

FIXES["paper_irrigation_manual.py"] = [
    (
        "Vegetative</strong> steering uses longer drybacks and lower EC to encourage root "
        "and leaf growth. <strong>Generative</strong> steering uses shorter drybacks and higher EC",
        "Vegetative</strong> steering uses smaller drybacks, higher VWC, and moderate EC to encourage root "
        "and leaf growth. <strong>Generative</strong> steering uses larger controlled drybacks and/or higher root-zone EC",
    ),
    (
        "Vegetative steering uses longer drybacks and lower EC",
        "Vegetative steering uses smaller drybacks and moderate EC",
    ),
    (
        "Generative steering uses shorter drybacks and higher EC",
        "Generative steering uses larger controlled drybacks and/or higher root-zone EC",
    ),
]

FIXES["paper_signal_and_noise.py"] = [
    (
        "Most grow-room &lsquo;alerts&rsquo;, perhaps 70% in a busy room, are noise: transients "
        "that fix themselves before any action would have mattered.",
        "Untuned grow-room dashboards often produce alarm floods: many &lsquo;alerts&rsquo; are "
        "transients that fix themselves before any action would have mattered. Measure your own false-positive rate.",
    ),
    (
        "7+ points all trending in one direction, or 8+ points on one side of the mean",
        "classic Western Electric / Nelson-style rules (e.g. one point beyond 3&sigma;; eight consecutive on one side of the mean; "
        "Nelson trend often six ascending/descending &mdash; name the rule set you implement)",
    ),
]

FIXES["paper_closed_loop.py"] = [
    (
        "around <strong>70% of raw alerts are noise</strong>",
        "many raw alerts are noise until the system is tuned",
    ),
    (
        "tells you whole-room health and whether to act in under five seconds",
        "aims to surface whole-room health quickly so you act only when it matters",
    ),
    (
        "roughly four days before tip burn",
        "days earlier than tip burn in a worked example (illustrative lead time, not a validated cannabis prognosis)",
    ),
]

FIXES["paper_plant_state_dashboard.py"] = [
    (
        "tip burn likely within ~48h",
        "tip burn risk elevated (illustrative UX copy, not a validated prognostic model)",
    ),
    (
        "This is an <strong>operational and product-design guide</strong>, not a horticulture-science paper.",
        "This is an <strong>operational and product-design guide</strong>, not a horticulture-science paper. Lead-time examples are illustrative UX, not validated predictions.",
    ),
]

FIXES["paper_plant_biosignal.py"] = [
    (
        "and turn the drift into water and stress insight.",
        "and log the drift for education and correlation hunting &mdash; not as a validated water, nutrient, or stress meter.",
    ),
    (
        "Commercial plant-biosignal sensors clip electrodes to a plant, amplify the tiny voltages it makes, and turn the drift into water and stress insight. You can build the acquisition side",
        "Commercial plant-biosignal sensors clip electrodes to a plant and amplify the tiny voltages it makes. "
        "You can build the acquisition side",
    ),
    (
        "light-on/off detection (~85% accurate on this exact hardware class)",
        "light-on/off detection (one study reported ~85% under its protocol; expect lower performance in noisy grow rooms)",
    ),
]

FIXES["paper_smart_watering_vrwe.py"] = [
    (
        "never flood, never starve",
        "prefer temporary mild deficit over flooding when uncertain; hard-floor emergency VWC still required",
    ),
]

FIXES["paper_f2_crop_steering.py"] = [
    (
        "These numbers are starting points",
        "These numbers are one facility's probe-native starting points after hand-watering &mdash; not universal % water content. They are starting points",
    ),
]

FIXES["paper_root_zone_teros12.py"] = [
    (
        "Calibration corrects an additive offset",
        "Calibration reduces error (often more than a simple additive offset; EC and temperature still interact)",
    ),
]

FIXES["paper_facility_3d.py"] = [
    (
        "Security requirements cited to Washington WAC",
        "Example security rules (Washington WAC for illustration only; use the jurisdiction that will inspect you)",
    ),
]

FIXES["paper_daily_checks.py"] = [
    (
        "lifts follow-through two to three fold",
        "has a medium positive effect on goal attainment (meta-analytic d&asymp;0.65)",
    ),
    (
        "for GACP/GMP trail",
        "for operational discipline (regulated GxP release still needs validated systems and QA-approved procedures)",
    ),
]

FIXES["paper_defoliation_training.py"] = [
    (
        "lift the bottom line by roughly 15&ndash;30%",
        "move yield per area and uniformity in ways that often matter more than expensive gear",
    ),
    (
        "first topping&hellip; around day 5&ndash;7 of veg",
        "first topping only once plants are established with enough nodes (clone rooms may top early; seed-grown plants need more time)",
    ),
    (
        "around day 5-7 of veg",
        "only once plants are established with enough nodes (often later for seed starts than for multi-node clones)",
    ),
]

FIXES["paper_airflow_design.py"] = [
    (
        "Aim for a <strong>gentle, turbulent breeze (~0.3-1.0 m/s)</strong> everywhere",
        "Aim for a <strong>gentle leaf flutter through the whole canopy (~0.3-1.0 m/s at canopy height as a practical band)</strong>",
    ),
]


def apply_file_fixes(filename: str, pairs: list[tuple[str, str]]) -> int:
    path = os.path.join(HERE, filename)
    if not os.path.exists(path):
        print(f"SKIP missing {filename}")
        return 0
    text = read(path)
    n = 0
    for old, new in pairs:
        if old in text:
            c = text.count(old)
            text = text.replace(old, new)
            n += c
            print(f"  OK {filename}: replaced x{c}  {old[:60]!r}")
        else:
            # softer: collapse whitespace and try again
            old_ws = re.sub(r"\s+", " ", old)
            # try line-by-line fuzzy for short unique phrases
            short = old[:90]
            if short in text and old not in text:
                print(f"  PARTIAL {filename}: found prefix only: {short!r}")
            else:
                print(f"  MISS {filename}: {old[:80]!r}")
    if n:
        write(path, text)
    return n


def fix_cloning_special() -> None:
    path = os.path.join(HERE, "paper_cloning.py")
    t = read(path)
    # turgor / half-strength mechanism
    patterns = [
        (
            r"Water the mother with .{0,40}half-strength.{0,200}?brittle.{0,80}",
            "Water the mother thoroughly the day before so cuttings are fully hydrated and turgid. "
            "Avoid drought-stressed mothers; wilted tissue roots poorly. ",
        ),
        (
            r"If the cut end sits in air, the stem draws in an air embolism.{0,120}",
            "Keep the cut end moist from the moment you cut. Exposed cuts dry and stall water uptake; ",
        ),
        (
            r"IBA.{0,20}a synthetic version of a natural.{0,40}auxin",
            "IBA is an auxin used in rooting products (plants can convert IBA into IAA, the main natural auxin",
        ),
        (
            r"roots clones at 90 to 95 percent success or better",
            "well-run rooms often root clones at ~90 percent or better as an operational target",
        ),
        (
            r"Clone feed should run an EC of about 1\.5 mS/cm",
            "Clone feed often starts milder (~0.6&ndash;1.2 mS/cm, product-dependent) and rises only after roots appear; ~1.5 mS/cm can burn soft cuttings",
        ),
    ]
    for rx, rep in patterns:
        nt, c = re.subn(rx, rep, t, count=1, flags=re.S | re.I)
        if c:
            print(f"  cloning regex OK: {rx[:50]}")
            t = nt
        else:
            print(f"  cloning regex MISS: {rx[:50]}")
    write(path, t)


def fix_site_branding() -> None:
    # build.py hero + meta
    path = os.path.join(HERE, "build.py")
    t = read(path)
    pairs = [
        (
            "Peer-reviewed cultivation science, rewritten so a first-timer can actually ",
            "Evidence-linked cultivation field guides, rewritten so a first-timer can actually ",
        ),
        (
            'desc="Peer-reviewed cannabis cultivation white papers, by grow stage."',
            'desc="Evidence-linked cannabis cultivation field guides, by grow stage."',
        ),
        (
            "Peer-reviewed sources ",
            "Primary literature and official guidance ",
        ),
        (
            "(non-peer-reviewed source)",
            "(industry/manufacturer or non-journal source)",
        ),
    ]
    for o, n in pairs:
        if o in t:
            t = t.replace(o, n)
            print(f"  build.py: {o[:50]}")
        else:
            print(f"  build.py MISS: {o[:50]}")
    write(path, t)

    path = os.path.join(HERE, "export_corpus.py")
    t = read(path)
    pairs = [
        (
            "Beginner-first, peer-reviewed white papers on indoor medical cannabis cultivation - ",
            "Beginner-first, evidence-linked field guides on indoor medical cannabis cultivation - ",
        ),
        (
            "Beginner-first, peer-reviewed white papers on indoor medical cannabis cultivation — ",
            "Beginner-first, evidence-linked field guides on indoor medical cannabis cultivation — ",
        ),
        (
            "Beginner-friendly, peer-reviewed white papers on medical cannabis cultivation: ",
            "Beginner-friendly, evidence-linked field guides on medical cannabis cultivation: ",
        ),
        (
            "Beginner-friendly, peer-reviewed cannabis cultivation reference: ",
            "Beginner-friendly, evidence-linked cannabis cultivation reference: ",
        ),
        (
            "A library of {n} peer-reviewed, beginner-friendly cannabis cultivation white papers. Every ",
            "A library of {n} evidence-linked, beginner-friendly cannabis cultivation field guides. Every ",
        ),
        (
            f"{{len(manifest)}} peer-reviewed cannabis cultivation white papers as clean markdown.\\n",
            f"{{len(manifest)}} evidence-linked cannabis cultivation field guides as clean markdown.\\n",
        ),
        (
            "peer-reviewed white papers",
            "evidence-linked field guides",
        ),
        (
            "peer-reviewed cannabis cultivation white papers",
            "evidence-linked cannabis cultivation field guides",
        ),
        (
            "Every factual claim is cited inline `[n]` to a per-paper References list - peer-reviewed ",
            "Every factual claim is cited inline `[n]` to a per-paper References list - primary literature ",
        ),
    ]
    for o, n in pairs:
        if o in t:
            t = t.replace(o, n)
            print(f"  export_corpus: {o[:55]}")
        else:
            # try without fancy dash
            print(f"  export_corpus MISS: {o[:55]}")
    # broader catch
    t = t.replace("peer-reviewed white papers", "evidence-linked field guides")
    t = t.replace("peer-reviewed cannabis cultivation white papers", "evidence-linked cannabis cultivation field guides")
    t = t.replace("peer-reviewed, beginner-friendly cannabis cultivation white papers",
                  "evidence-linked, beginner-friendly cannabis cultivation field guides")
    t = t.replace("{len(manifest)} peer-reviewed cannabis", "{len(manifest)} evidence-linked cannabis")
    write(path, t)

    # index.html is generated; also fix shell if present
    for name in ("shell.py",):
        p = os.path.join(HERE, name)
        if not os.path.exists(p):
            continue
        t = read(p)
        if "Peer-reviewed" in t:
            t = t.replace("Peer-reviewed cultivation science", "Evidence-linked cultivation field guides")
            t = t.replace("Peer-reviewed cannabis", "Evidence-linked cannabis")
            write(p, t)
            print(f"  {name}: branding")


def fix_scaling_ec() -> None:
    path = os.path.join(HERE, "paper_scaling_high_light.py")
    t = read(path)
    # Soften extreme EC ladder if present
    t2 = t
    t2 = t2.replace("3.6-4.2", "2.4-3.2 (advanced: up to ~3.6)")
    t2 = t2.replace("3.6&ndash;4.2", "2.4&ndash;3.2 (advanced: up to ~3.6)")
    t2 = t2.replace("runoff 7-8", "runoff often higher than feed (advanced steering; not a beginner default)")
    t2 = t2.replace("runoff 7&ndash;8", "runoff often higher than feed (advanced steering; not a beginner default)")
    t2 = t2.replace("Runoff 7-8", "Runoff: advanced only (often >> feed EC)")
    t2 = t2.replace("7–8", "advanced-only if >> feed")
    if t2 != t:
        write(path, t2)
        print("  scaling-high-light EC ladder softened")
    else:
        print("  scaling EC: no standard patterns (check manually)")


def fix_one_steering_ec() -> None:
    path = os.path.join(HERE, "paper_one_steering_law.py")
    t = read(path)
    # Soften beginner coco 3.0 / 4.5-6.0 if present
    patterns = [
        (r"Feed strength ~3\.0 / 4\.5[–\-]6\.0",
         "Feed strength: learn full mark first; many coco programmes start well below high-intensity rockwool substrate EC (do not copy 3–6 blindly)"),
        (r"~3\.0 veg / 4\.5",
         "moderate veg EC rising with light / advanced flower only toward"),
        (r"4\.5–6\.0", "match runoff and tips; high-intensity only"),
        (r"4\.5-6\.0", "match runoff and tips; high-intensity only"),
    ]
    for rx, rep in patterns:
        t, c = re.subn(rx, rep, t, count=3)
        if c:
            print(f"  one-steering EC: {rx} x{c}")
    write(path, t)


def fix_irrigation_header_key() -> None:
    path = os.path.join(HERE, "paper_irrigation_manual.py")
    t = read(path)
    # KEY box variants
    t2 = re.sub(
        r"Vegetative steering uses longer drybacks and lower EC.{0,80}Generative steering uses shorter drybacks and higher EC",
        "Vegetative steering uses smaller drybacks, higher VWC, and moderate EC; "
        "generative steering uses larger controlled drybacks and/or higher root-zone EC",
        t,
        flags=re.S | re.I,
    )
    t2 = t2.replace(
        "longer drybacks and lower EC to encourage root",
        "smaller drybacks and moderate EC to encourage root",
    )
    t2 = t2.replace(
        "shorter drybacks and higher EC to push",
        "larger controlled drybacks and/or higher root-zone EC to push",
    )
    t2 = t2.replace(
        "shorter drybacks and higher EC",
        "larger controlled drybacks and/or higher root-zone EC",
    )
    if t2 != t:
        write(path, t2)
        print("  irrigation-manual dryback polarity fixed")
    else:
        print("  irrigation-manual: check dryback lines manually")
        # dump relevant lines
        for i, line in enumerate(t.splitlines(), 1):
            if "dryback" in line.lower() and ("veg" in line.lower() or "gen" in line.lower() or "Vegetative" in line or "Generative" in line):
                print(f"    L{i}: {line[:120]}")


def fix_pppe_flow_summary() -> None:
    path = os.path.join(HERE, "paper_pppe.py")
    t = read(path)
    t = t.replace("Flow: one way, clean to dirty", "Flow: people/materials clean → dirty; waste dirty → exit")
    t = t.replace("one way, clean to dirty", "clean → dirty for people/materials; dirty → exit for waste")
    t = t.replace("dirty to clean, never back", "clean → dirty for people/materials; dirty → exit for waste — never reverse without re-gowning")
    write(path, t)
    print("  pppe flow polarity")


def fix_tissue_flexible() -> None:
    path = os.path.join(HERE, "paper_tissue_culture.py")
    t = read(path)
    # flexible replacements for strings that may use HTML entities
    reps = [
        (r"up to 100% in one cannabis cross",
         "at genotype-dependent rates (often single digits to tens of percent — test seed lots)"),
        (r"lose up to .{0,20}50%.{0,20}of cannabinoids",
         "in severe symptomatic dud outbreaks can lose a large fraction of cannabinoids (sometimes approaching ~50%)"),
        (r"Almost every living plant cell carries the complete instructions",
         "Many plant cells can, under the right conditions, carry the complete instructions"),
        (r"DNA test \(qPCR\)", "RT-qPCR test"),
        (r"gold-standard DNA/RNA test", "gold-standard RNA test (RT-qPCR)"),
        (r"DNA test for a viroid", "RT-qPCR test for a viroid"),
    ]
    for rx, rep in reps:
        t, c = re.subn(rx, rep, t, count=3, flags=re.I)
        if c:
            print(f"  tissue-culture flexible x{c}: {rx[:40]}")
    write(path, t)


def fix_jurisdiction_banners() -> None:
    """Add a short jurisdiction note to IPM/PPE/facility papers if missing."""
    banners = {
        "paper_ipm_sop.py": (
            "Jurisdiction note: product legality, REI/PHI, and organism status are local "
            "(e.g. NZ ACVM/HSNO/WorkSafe vs US EPA WPS). Verify current law and labels before any spray or release."
        ),
        "paper_pest_id.py": (
            "Jurisdiction note: named biocontrol agents and rates are planning examples only. "
            "Confirm legal status and supplier availability in your country (NZ readers: check HSNO/MPI before release)."
        ),
        "paper_pppe.py": (
            "Jurisdiction note: PPE duties and HSWA wording below are NZ-oriented; other jurisdictions differ."
        ),
        "paper_facility_3d.py": (
            "Jurisdiction note: security and egress examples may cite US (WAC/IBC) rules for illustration. "
            "Use the code and licence rules of the jurisdiction that will inspect you."
        ),
    }
    for fname, note in banners.items():
        path = os.path.join(HERE, fname)
        if not os.path.exists(path):
            continue
        t = read(path)
        if "Jurisdiction note:" in t:
            print(f"  banner already in {fname}")
            continue
        # insert into first SECTIONS append lead if possible
        marker = "SECTIONS.append("
        idx = t.find(marker)
        if idx < 0:
            print(f"  no SECTIONS for banner {fname}")
            continue
        # Find first callout or lead after start - simpler: inject a callout block via string after SLUG header area
        insert = (
            "\n# Fact-check jurisdiction banner\n"
            f'JURISDICTION_NOTE = {note!r}\n'
        )
        if "JURISDICTION_NOTE" not in t:
            t = t.replace("SECTIONS = []", "SECTIONS = []\n" + insert, 1)
            # also try to prepend callout in first section blocks - hard; add as module-level used later
            # Inject into first section's blocks list start
            t2, c = re.subn(
                r'(SECTIONS\.append\(\{[^}]*?"blocks":\s*\[)',
                r'\1\n    callout("NOTE", "Jurisdiction", JURISDICTION_NOTE),\n    ',
                t,
                count=1,
                flags=re.S,
            )
            if c:
                t = t2
                write(path, t)
                print(f"  jurisdiction banner: {fname}")
            else:
                # fallback: just leave JURISDICTION_NOTE constant
                write(path, t)
                print(f"  jurisdiction constant only: {fname}")


def fix_seeds_table_auto() -> None:
    path = os.path.join(HERE, "paper_seeds_germination.py")
    t = read(path)
    # Autoflower sex row variants
    t2 = t
    t2 = re.sub(
        r'("~50% male / 50% female",\s*"~99% female",\s*"~99% female")',
        r'("~50% male / 50% female", "~99% female (if feminised)", "Feminised autos ~99% female; regular autos ~50/50")',
        t2,
    )
    t2 = t2.replace(
        '["Sex outcome", "~50% male / 50% female", "~99% female", "~99% female"]',
        '["Sex outcome", "~50% male / 50% female", "~99% female (if feminised)", "Feminised autos ~99% female; regular autos ~50/50"]',
    )
    # leaf drinking flexible
    t2 = re.sub(
        r"drinks largely through its leaves\.[^.]*\.",
        "has a tiny root system, so it loses water easily. High humidity reduces evaporative demand until roots expand — roots still do the drinking.",
        t2,
        count=1,
    )
    t2 = t2.replace("near-99% success when conditions are controlled",
                    "high germination with fresh seed and controlled moisture and temperature")
    t2 = t2.replace("water, warmth and darkness",
                    "water and warmth (darkness is optional convenience)")
    t2 = t2.replace(
        "only flower when the daily light drops to about 12 hours",
        "flower when nights are long enough without light interruptions (12/12 is the usual default)",
    )
    t2 = t2.replace(
        "carry only female genetics",
        "produce almost all female offspring (stress hermaphroditism can still appear)",
    )
    if t2 != t:
        write(path, t2)
        print("  seeds-germination flexible fixes applied")


def fix_lighting_table_rows() -> None:
    path = os.path.join(HERE, "paper_lighting_fundamentals.py")
    t = read(path)
    # table() API uses lists
    reps = [
        (r'\["Clone / seedling", "100-300", "~10-15", "18/6"\]',
         '["Clone / seedling", "100-250", "~6-16", "18/6"]'),
        (r'\["Clone / seedling", "100–300", "~10–15", "18/6"\]',
         '["Clone / seedling", "100–250", "~6–16", "18/6"]'),
        (r'\["Flower \(no CO2\)", "700-900", "~30-45", "12/12"\]',
         '["Flower (no CO2)", "700-900", "~30-39", "12/12"]'),
        (r'\["Flower \(no CO2\)", "700–900", "~30–45", "12/12"\]',
         '["Flower (no CO2)", "700–900", "~30–39", "12/12"]'),
        (r'100-300 PPFD \(DLI ~10-15',
         '100-250 PPFD (DLI roughly ~6-16'),
        (r'700-900 PPFD without added CO2 \(DLI ~30-45',
         '700-900 PPFD without added CO2 (DLI ~30-39'),
        (r'inverse-square law: roughly doubling the distance from the canopy cuts PPFD by about 75%',
         'distance reduces intensity, but inverse-square is a point-source ideal — use a PPFD map and meter for LED bars'),
        (r'drives flowering and stretch',
         'is highly photosynthetic (stretch is more about low blue and far-red; flowering is photoperiod)'),
        (r'600 PPFD x 18h \(veg\) is roughly the same daily dose as 800 PPFD x 12h \(flower\)',
         '600 PPFD x 18h (~39 mol) is closer to ~900 PPFD x 12h than to 800 PPFD x 12h'),
    ]
    for rx, rep in reps:
        t, c = re.subn(rx, rep, t, count=3)
        if c:
            print(f"  lighting x{c}: {rx[:50]}")
    write(path, t)


def fix_water_do() -> None:
    path = os.path.join(HERE, "paper_water_quality.py")
    t = read(path)
    t2 = re.sub(
        r"dissolved oxygen falls from about 5[-–]6 ppm at 20[^.]{0,20}to only 3[-–]4 ppm at 26[^.]{0,20}",
        "saturation dissolved oxygen is roughly ~9 mg/L at 20 C and ~8 mg/L at 26 C, while warm water still raises pathogen risk because DO is harder to maintain under root demand",
        t,
        count=2,
        flags=re.I,
    )
    t2 = re.sub(
        r"5[-–]6 ppm at 20",
        "~9 mg/L saturation at 20",
        t2,
        count=2,
    )
    t2 = re.sub(
        r"3[-–]4 ppm at 26",
        "~8 mg/L saturation at 26",
        t2,
        count=2,
    )
    t2 = t2.replace("800-900 ppm", "your total EC budget (set targets in mS/cm)")
    t2 = t2.replace("800–900 ppm", "your total EC budget (set targets in mS/cm)")
    write(path, t2)
    print("  water-quality DO/EC")


def fix_ipm_sulphur() -> None:
    path = os.path.join(HERE, "paper_ipm_sop.py")
    t = read(path)
    t2 = re.sub(
        r"sulphur \(1 to 3 tablespoons per lit(?:re|er), ideally 3, no more than once every 2 weeks,? veg and mothers only\)",
        "sulphur only if lawful, at the current product label rate and REI/PHI (never kitchen tablespoon rates; veg/mothers only when residues allow)",
        t,
        count=2,
        flags=re.I,
    )
    t2 = re.sub(
        r"1 to 3 tablespoons per lit(?:re|er)[^.]*",
        "only the current registered label rate for that product (never invent tablespoon/L kitchen rates)",
        t2,
        count=2,
        flags=re.I,
    )
    write(path, t2)
    print("  ipm sulphur")


def fix_mould_rh() -> None:
    path = os.path.join(HERE, "paper_mould_risk.py")
    t = read(path)
    t2 = re.sub(
        r"(~?60[-–]70%\s*(?:band|RH|range))",
        r"~45–65% stage-dependent band (mid/late flower often ~45–55%)",
        t,
        count=4,
        flags=re.I,
    )
    t2 = t2.replace(
        "60-70%",
        "45-65% (late flower often 45-55%)",
    )
    t2 = t2.replace(
        "60–70%",
        "45–65% (late flower often 45–55%)",
    )
    write(path, t2)
    print("  mould-risk RH")


def fix_pppe_logs() -> None:
    path = os.path.join(HERE, "paper_pppe.py")
    t = read(path)
    t2 = re.sub(
        r"~?3 log,?\s*~?83%",
        "~2–3 log (~99–99.9% under test conditions)",
        t,
        count=3,
    )
    t2 = re.sub(
        r"~?2 log,?\s*~?58%",
        "soil and organism removal without sterilisation",
        t2,
        count=3,
    )
    t2 = t2.replace("dirty to clean", "clean to dirty for people/materials (waste exits dirty)")
    write(path, t2)
    print("  pppe logs")


def fix_athena() -> None:
    path = os.path.join(HERE, "paper_nutrient_mixing_athena.py")
    t = read(path)
    t = t.replace("four to five times saltier", "six to seven times saltier")
    t = t.replace("4 to 5 times saltier", "six to seven times saltier")
    write(path, t)
    print("  athena seawater")


def fix_under_canopy() -> None:
    path = os.path.join(HERE, "paper_under_canopy_lighting.py")
    t = read(path)
    t = re.sub(r"red-rich and far-red-dominant", "green- and far-red-enriched (blue/red depleted)", t)
    t = re.sub(r"red-rich", "green/FR-enriched", t)
    t = re.sub(
        r"full air exchange every 1[-–]3 minutes",
        "strong recirculation (sealed: dehu/recirc — not continuous vented ACH that dumps CO2)",
        t,
        count=2,
    )
    write(path, t)
    print("  under-canopy spectrum/ACH")


def fix_flowering_flexible() -> None:
    path = os.path.join(HERE, "paper_flowering_stages.py")
    t = read(path)
    t = re.sub(
        r"More amber means THC is degrading toward CBN for a heavier, more sedative effect\.",
        "Later harvests often feel heavier, but effect is multi-factor (terpenes, dose, genotype); "
        "amber % is a maturity proxy, and human evidence that CBN alone drives couch-lock is limited.",
        t,
        count=2,
    )
    t = t.replace("Sedative, couch-lock", "Often denser/heavier feel; genotype still dominates")
    t = t.replace("Energetic, heady", "Common early-cut target")
    t = t.replace(
        "Even a phone-screen of light, repeated, can cause hermies",
        "Bright or repeated night interruptions can stall flowering; genetics and multi-stress drive most herms",
    )
    t = re.sub(
        r"lower or flush nutrients in the last 1 to 2 weeks",
        "ease feed strength in the last 1 to 2 weeks (long plain-water flushes have weak evidence for quality gains)",
        t,
        count=2,
    )
    t = t.replace('"Lower RH, flush, read trichomes"', '"Lower RH, ease EC, read trichomes"')
    write(path, t)
    print("  flowering-stages flexible")


def fix_biosignal_sub() -> None:
    path = os.path.join(HERE, "paper_plant_biosignal.py")
    t = read(path)
    t = t.replace(
        "turn the drift into water and stress insight",
        "log the drift for education — not as a validated water/nutrient/stress meter",
    )
    t = t.replace(
        "water and stress insight",
        "relative biopotential changes for education only",
    )
    # SUB string at top
    t = re.sub(
        r"SUB = \([^)]+water and stress[^)]+\)",
        'SUB = ("Commercial plant-biosignal sensors clip electrodes to a plant and amplify the tiny '
        'voltages it makes. You can build the acquisition side from an M5Stack ESP32, an ECG front-end '
        'chip and ESPHome for about NZ$110, and stream it into Home Assistant — for education and '
        'correlation hunting, not as a validated crop meter.")',
        t,
        count=1,
        flags=re.S,
    )
    write(path, t)
    print("  biosignal")


def fix_signal_70() -> None:
    path = os.path.join(HERE, "paper_signal_and_noise.py")
    t = read(path)
    t = re.sub(r"perhaps 70% in a busy room, are noise",
               "often many alerts in a busy room are noise until tuned", t)
    t = re.sub(r"around 70% of raw alerts are noise",
               "many raw alerts are noise until tuned", t)
    t = re.sub(
        r"7\+ points all trending.{0,40}8\+ points on one side",
        "Western Electric / Nelson control rules (e.g. eight consecutive on one side; Nelson trends often use six points)",
        t,
        count=2,
    )
    write(path, t)
    print("  signal-and-noise")

    path = os.path.join(HERE, "paper_closed_loop.py")
    t = read(path)
    t = re.sub(r"70% of raw alerts are noise", "many raw alerts are noise until tuned", t)
    t = t.replace("in under five seconds", "quickly when the dashboard is well designed")
    t = t.replace("roughly four days before tip burn",
                  "days earlier than tip burn in an illustrative worked example")
    write(path, t)
    print("  closed-loop")


def fix_rockwool_100() -> None:
    path = os.path.join(HERE, "paper_rockwool_crop_steering.py")
    t = read(path)
    t = re.sub(
        r"100% of what you put in goes straight to the plant",
        "root-zone EC is essentially the EC of the pore water (unused feed still leaves as runoff or concentrates on dryback)",
        t,
        count=2,
    )
    write(path, t)
    print("  rockwool 100%")


def fix_caplan_coco() -> None:
    for fname in ("paper_coco_crop_steering.py", "paper_rockwool_crop_steering.py",
                  "paper_one_steering_law.py", "paper_f2_crop_steering.py"):
        path = os.path.join(HERE, fname)
        if not os.path.exists(path):
            continue
        t = read(path)
        t2 = re.sub(
            r"raise cannabinoid content without costing yield",
            "raise cannabinoid concentrations in a single carefully timed late drought study (not the same as daily drybacks)",
            t,
            count=2,
            flags=re.I,
        )
        t2 = re.sub(
            r"without costing yield",
            "in that study setup (daily drybacks are a related idea, not the same experiment)",
            t2,
            count=2,
        )
        if t2 != t:
            write(path, t2)
            print(f"  Caplan mapping: {fname}")


def fix_light_28() -> None:
    path = os.path.join(HERE, "paper_light_acclimation.py")
    t = read(path)
    t = t.replace("by about 28%", "by about one-third (~33%)")
    t = t.replace("about 28%", "about one-third (~33%)")
    write(path, t)
    print("  light-acclimation 33%")


def fix_scaling_ceiling() -> None:
    path = os.path.join(HERE, "paper_scaling_high_light.py")
    t = read(path)
    t = re.sub(
        r"light-saturates around .{0,20}800.{0,20}",
        "leaf curves flatten earlier than canopy yield, which can still rise well past 800 ",
        t,
        count=3,
        flags=re.I,
    )
    t = t.replace("~800 µmol", "~800+ µmol with diminishing returns (not a hard wall)")
    t = t.replace("~800 &micro;mol", "~800+ &micro;mol with diminishing returns (not a hard wall)")
    t = t.replace("→ ~800", "→ diminishing returns past ~800")
    write(path, t)
    print("  scaling 800 wall")


def main() -> None:
    print("=== Fact-check fixes ===")

    # META badges on all paper_*.py
    for fn in sorted(os.listdir(HERE)):
        if fn.startswith("paper_") and fn.endswith(".py"):
            fix_meta_badges(fn)

    fix_site_branding()
    fix_seeds_table_auto()
    fix_cloning_special()
    fix_tissue_flexible()
    fix_light_28()
    fix_flowering_flexible()
    fix_lighting_table_rows()
    fix_under_canopy()
    fix_water_do()
    fix_athena()
    fix_ipm_sulphur()
    fix_mould_rh()
    fix_pppe_logs()
    fix_pppe_flow_summary()
    fix_irrigation_header_key()
    fix_one_steering_ec()
    fix_scaling_ec()
    fix_scaling_ceiling()
    fix_rockwool_100()
    fix_caplan_coco()
    fix_biosignal_sub()
    fix_signal_70()
    fix_jurisdiction_banners()

    # literal pair fixes (best-effort)
    total = 0
    for fname, pairs in FIXES.items():
        total += apply_file_fixes(fname, pairs)

    print(f"\nLiteral pair hits: {total}")
    print("Done applying. Run: python build.py")


if __name__ == "__main__":
    main()
