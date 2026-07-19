# -*- coding: utf-8 -*-
"""Pass 3: repair garbled replacements and finish remaining critical fixes."""
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent


def fix(name: str, pairs: list[tuple[str, str]]) -> None:
    p = HERE / name
    t = p.read_text(encoding="utf-8")
    orig = t
    for a, b in pairs:
        if a in t:
            t = t.replace(a, b)
            print(f"OK {name}: {a[:70]!r}")
        else:
            print(f"MISS {name}: {a[:70]!r}")
    if t != orig:
        p.write_text(t, encoding="utf-8", newline="\n")


def main() -> None:
    # --- cloning garbled success line ---
    fix("paper_cloning.py", [
        (
            "A well-run propagation room well-run rooms often root clones at ~90 percent or better as an operational target",
            "Well-run propagation rooms often root clones at ~90 percent or better as an operational target",
        ),
        (
            "If the cut end sits in air, the stem draws in an <strong>air embolism</strong> (an air bubble) that blocks water uptake. Keep the end wet f",
            "If the cut end sits in air it dries and stalls water uptake (more desiccation than classic woody-stem embolism). Keep the end wet f",
        ),
        (
            "a synthetic version of a natural plant root hormone called an auxin",
            "an auxin used in rooting products (plants often convert IBA to IAA)",
        ),
    ])

    # --- tissue garbled ---
    fix("paper_tissue_culture.py", [
        (
            "Infected plants can in severe symptomatic dud outbreaks can lose a large fraction of cannabinoids (sometimes approach",
            "In severe symptomatic dud outbreaks, infected plants can lose a large fraction of cannabinoids (sometimes approach",
        ),
        (
            "meristem culture + DNA testing",
            "meristem culture + RT-qPCR testing",
        ),
        (
            "a plant that is <em>probably</em> clean, ",
            "a plant that is <em>probably</em> clean until a lab RT-qPCR says so, ",
        ),
    ])
    # totipotency KEY
    t = (HERE / "paper_tissue_culture.py").read_text(encoding="utf-8")
    t2 = t
    if "Almost every living plant cell" in t2:
        t2 = t2.replace(
            "Almost every living plant cell carries the complete instructions to rebuild the whole plant",
            "Many plant cells can, under the right conditions, rebuild a whole plant",
        )
        print("OK totipotency almost every")
    if "a clean start also leaves behind fungal root-rots" in t2:
        if "leaves behind fungal root-rots" in t2:
            # simpler line-based
            lines = t2.splitlines()
            out = []
            skip = 0
            for i, line in enumerate(lines):
                if skip:
                    skip -= 1
                    continue
                if "a clean start also leaves behind fungal root-rots" in line:
                    out.append(
                        '    p("HpLVd gets the headlines. Meristem work plus indexing mainly targets systemic agents '
                        '(viroids/viruses); surface sterilisation removes many surface microbes and hitch-hikers, '
                        'but endophytes can still emerge and mites remain an IPM problem."),'
                    )
                    # skip following continuation lines of that p()
                    j = i + 1
                    while j < len(lines) and (lines[j].strip().startswith('"') or lines[j].strip().startswith("'")):
                        j += 1
                        skip += 1
                    # if next line ends the p()
                    if j < len(lines) and lines[j].strip().endswith("),") and "leaves" not in lines[j]:
                        pass
                else:
                    out.append(line)
            t2 = "\n".join(out) + ("\n" if t2.endswith("\n") else "")
            print("OK tissue fungal cleanout rewritten")
    # survey card
    t2 = t2.replace(
        'card("It\'s everywhere", "Surveys found HpLVd in roughly <strong>90% of California facilities</strong> and ~40% of Canadian dispensary flower. If you\'ve cloned for years, assume you may have it."',
        'card("It\'s everywhere", "Surveys have reported very high CA facility rates (~90% in one programme) and frequent Canadian retail positives (~40% in one study) &mdash; warning signals, not global law. If you\'ve cloned for years, assume you may have it."',
    )
    if t2 != t:
        (HERE / "paper_tissue_culture.py").write_text(t2, encoding="utf-8", newline="\n")
        print("OK tissue write")

    # --- irrigation cards still inverted ---
    fix("paper_irrigation_manual.py", [
        (
            'card("Vegetative", "Leafy growth and size. Longer drybacks held wetter overall, lower EC.", "Steer"),',
            'card("Vegetative", "Leafy growth and size. Smaller drybacks, held wetter overall, moderate EC.", "Steer"),',
        ),
        (
            'card("Generative", "Flower, density and resin. Shorter, firmer drybacks, higher EC.", "Steer"),',
            'card("Generative", "Flower, density and resin. Larger controlled drybacks and/or higher root-zone EC.", "Steer"),',
        ),
    ])

    # --- ph remaining ---
    fix("paper_ph_management.py", [
        (
            "Drop it too low, below about 5.5, and calcium, magnesium and phosphorus lock out ",
            "Drop it too low, below about 5.5, and calcium, magnesium and phosphorus availability can fall while iron and manganese can push toward toxicity ",
        ),
        (
            "Aim to keep feed and runoff EC within about 10 percent of each ",
            "Treat large runaway gaps (runoff much higher than feed) as salt buildup; advanced steering may hold higher root-zone EC on purpose. Keep an eye on feed and runoff EC each ",
        ),
        (
            '["Veg", "5.8-6.2", "Rising EC means salt buildup", "Monthly", "Runoff EC > feed by >10%"],',
            '["Veg", "5.8-6.2", "Rising EC means salt buildup", "Monthly", "Runoff EC running away above feed"],',
        ),
        (
            '["Flower", "5.8-6.2", "Hold feed and runoff within ~10%", "Monthly", "Runoff EC climbing day on day"],',
            '["Flower", "5.8-6.2", "Watch runoff vs feed (beginner: avoid runaway salts)", "Monthly", "Runoff EC climbing day on day"],',
        ),
    ])

    # --- pppe remaining hygiene numbers ---
    fix("paper_pppe.py", [
        (
            "on the order of <strong>70 to 90 ",
            "typically the <strong>dominant ",
        ),
        (
            "with up to <strong>100% transmission within four weeks</strong> of propagation from infected ",
            "and under experimental conditions infection of linked cuttings can approach complete cohort infection within weeks of propagation from infected ",
        ),
        (
            "Washing helps but does not sterilise: an alcohol rub removes about 83% of organisms, plain soap ",
            "Washing helps but does not sterilise: alcohol rubs often achieve ~2&ndash;3 log reductions (~99&ndash;99.9%) under test conditions; plain soap ",
        ),
        (
            "and water about 58%" + "",
            "and water remove soil and many organisms without sterilising hands",
        ),
        (
            '<strong>Your phone is filthier than a toilet seat.</strong> Cultured phones carry roughly an ',
            '<strong>Your phone is a high-touch fomite.</strong> Phones carry skin and environmental flora, contact faces and hands, and ',
        ),
        (
            "order of magnitude more bacteria than a public toilet seat, and they ride to your face and back to ",
            "cannot be fully cleaned in production &mdash; they ride to your face and back to ",
        ),
        (
            "Move people, materials and waste clean → dirty for people/materials; dirty → exit for waste for people/materials (waste exits dirty), never",
            "Move people and clean materials clean → dirty; waste and used PPE only dirty → exit. Never",
        ),
        (
            "Move people, materials and waste clean \u2192 dirty for people/materials; dirty \u2192 exit for waste for people/materials (waste exits dirty), never",
            "Move people and clean materials clean \u2192 dirty; waste and used PPE only dirty \u2192 exit. Never",
        ),
    ])
    # fix broken soap line if still split
    t = (HERE / "paper_pppe.py").read_text(encoding="utf-8")
    t2 = t.replace(
        "and water about 58%",
        "and water remove soil and many organisms without sterilising",
    )
    # fix "dominant percent" garble if we left broken strong tag
    t2 = re.sub(
        r"typically the <strong>dominant \n\s*percent</strong>",
        "typically the <strong>dominant share</strong> (exact percent varies by facility)",
        t2,
    )
    t2 = t2.replace(
        "typically the <strong>dominant ",
        "typically the <strong>dominant share</strong> (exact percent varies) ",
    )
    # may have left "percent</strong> of contamination"
    t2 = re.sub(
        r"typically the <strong>dominant share</strong> \(exact percent varies\) percent</strong> of",
        "typically the <strong>dominant share</strong> of",
        t2,
    )
    t2 = re.sub(
        r"typically the <strong>dominant share</strong> \(exact percent varies\) ([^<]*)</strong>",
        r"typically the <strong>dominant share</strong> (\1)",
        t2,
    )
    if t2 != t:
        (HERE / "paper_pppe.py").write_text(t2, encoding="utf-8", newline="\n")
        print("OK pppe cleanup")

    # --- mould 3.5x ---
    fix("paper_mould_risk.py", [
        (
            "roughly <strong>3.5× the rate</strong> of non-users",
            "about <strong>3.5× more often</strong> than non-users in one claims analysis (absolute rates still low; immunocompromised patients are the high-stakes group)",
        ),
        (
            "roughly <strong>3.5&times; the rate</strong> of non-users",
            "about <strong>3.5&times; more often</strong> than non-users in one claims analysis (absolute rates still low; immunocompromised patients are the high-stakes group)",
        ),
    ])

    # --- harvest ---
    fix("paper_harvest_dry_trim_cure.py", [
        (
            "Done well, simply dialling in this stage is reported to add 5-10% ",
            "Done well, dialling in this stage often recovers sellable mass versus bone-dry flower; vendor education sometimes cites ~5-10% ",
        ),
        (
            "which lands around 10% in practice (a real example batch ",
            "which is often ~10% of whole-plant wet weight in many rooms (example batch ",
        ),
        (
            "is reported to lift yield 5-10%, mostly by no longer over-drying.",
            "can lift sellable weight when you stop over-drying (vendor ~5-10% figures are illustrative).",
        ),
    ])

    # --- scaling garbled wall ---
    fix("paper_scaling_high_light.py", [
        (
            "CO&#8322; the leaf leaf curves flatten earlier than canopy yield, which can still rise well past 800 ",
            "Under ambient CO&#8322;, leaf curves flatten earlier than canopy yield, which can still rise well past 800 ",
        ),
        (
            ". <strong>The wall:</strong> CO&#8322;, at ~800. <strong>The fix:</strong> above 800 the extra light just ",
            ". <strong>The practical limit:</strong> ambient CO&#8322; lowers efficiency as PPFD climbs. <strong>The fix:</strong> above ~800&ndash;1000 without enrichment, extra light often just ",
        ),
        (
            '["1500", "2.4&ndash;3.2 (advanced: up to ~3.6)", "7&ndash;8", "~7.4 L", "High frequency + volume, daily EC checks", "Either error bites fast',
            '["1500", "2.4&ndash;3.2 (advanced: up to ~3.6)", "advanced if runoff >> feed", "~7.4 L", "High frequency + volume, daily EC checks", "Either error bites fast',
        ),
    ])

    # --- signal WE rules ---
    fix("paper_signal_and_noise.py", [
        (
            'ul(["<strong>7+ points</strong> all trending the same way: a real drift, even inside the limits",',
            'ul(["<strong>Nelson trend (often 6 points)</strong> all trending the same way: a real drift, even inside the limits",',
        ),
        (
            '"<strong>8+ points</strong> on one side of the mean: the process has shifted",',
            '"<strong>Western Electric: 8 points</strong> on one side of the mean: the process has shifted",',
        ),
        (
            "often many alerts in a busy room are noise until tuned: transients ",
            "are often noise until tuned: transients ",
        ),
    ])

    # --- coco flush ---
    fix("paper_coco_crop_steering.py", [
        (
            '("Flush / finish", "Lower EC feeds in the final stretch. Let the plant wind down cleanly."),',
            '("Finish", "Ease EC as demand falls. Long plain-water flushes have weak evidence for quality gains."),',
        ),
    ])

    # --- gmp ---
    t = (HERE / "paper_gmp_hash_lab.py").read_text(encoding="utf-8")
    t2 = t.replace(
        "Extraction multiplies both the good and the bad ",
        "Extraction can concentrate both the good and the bad (often several-fold when mass yield is low) ",
    )
    if t2 != t:
        (HERE / "paper_gmp_hash_lab.py").write_text(t2, encoding="utf-8", newline="\n")
        print("OK gmp multiplies")

    # --- seeds remaining darkness hard language ---
    fix("paper_seeds_germination.py", [
        (
            '], cls="compact", caption="All three supply the same water + warmth + darkness. They differ mainly in whether you can see progress',
            '], cls="compact", caption="All three supply water + warmth (darkness optional). They differ mainly in whether you can see progress',
        ),
        (
            'in darkness until they sprout."),',
            'damp and warm until they sprout (darkness optional)."),',
        ),
        (
            "<strong>Light:</strong> darkness while germinating. Once sprouted, give gentle light immediately so the stem does not stretch.",
            "<strong>Light:</strong> darkness is optional while germinating. Once sprouted, give gentle light immediately so the stem does not stretch.",
        ),
        (
            "Photoperiod plants flower when <em>you</em> shorten their light to 12 hours.",
            "Photoperiod plants flower when nights are long enough (growers usually use 12 hours light / 12 hours dark).",
        ),
    ])

    # --- ipm remaining ---
    fix("paper_ipm_sop.py", [
        (
            "Once more than 3 percent of a room is affected, escalate to approved pesticide ",
            "As an example planning default, once more than 3 percent of a room is affected, escalate to approved pesticide "
            "(zero-tolerance organisms override any percentage) ",
        ),
        (
            "from mothering through day 21 of flower, with no foliar treatment after buds form (a light ",
            "through early flower in many residue-aware facilities (example: day 21); your PHI and QA SOP set the real cutoff (a light ",
        ),
        (
            'p("Biocontrol releases predators that hunt your pests. They are harmless to the cannabis plant ',
            'p("Biocontrol releases predators that hunt your pests when legal in your jurisdiction. They usually leave no chemical residue on the cannabis plant ',
        ),
        (
            'p("Predators are harmless to the plant and to people. When the prey runs out they die off on ',
            'p("Predatory arthropods typically leave no chemical PHI, but allergy risk and legal status matter. When the prey runs out they die off on ',
        ),
        (
            "Spray when the media is fully saturated so the product is not pulled ",
            "Avoid spraying under high light, high VPD, or drought stress so the product is not forced onto ",
        ),
    ])

    # --- grow room taco / VPD ---
    t = (HERE / "paper_grow_room_systems.py").read_text(encoding="utf-8")
    for i, line in enumerate(t.splitlines(), 1):
        if "taco" in line.lower() or "0.8" in line and "1.2" in line:
            print(f"grs L{i}: {line.strip()[:120]}")

    # --- export_corpus / build final branding ---
    for fname in ("export_corpus.py", "build.py"):
        t = (HERE / fname).read_text(encoding="utf-8")
        t2 = t
        for a, b in [
            ("peer-reviewed white papers", "evidence-linked field guides"),
            ("Peer-reviewed white papers", "Evidence-linked field guides"),
            ("peer-reviewed cannabis cultivation", "evidence-linked cannabis cultivation"),
            ("Peer-reviewed cannabis cultivation", "Evidence-linked cannabis cultivation"),
            ("peer-reviewed, beginner-friendly", "evidence-linked, beginner-friendly"),
            ("Peer-reviewed cultivation science", "Evidence-linked cultivation field guides"),
            ("peer-reviewed cultivation science", "evidence-linked cultivation field guides"),
        ]:
            t2 = t2.replace(a, b)
        if t2 != t:
            (HERE / fname).write_text(t2, encoding="utf-8", newline="\n")
            print(f"OK branding {fname}")

    # Fix water DO if sentence is nonsense
    t = (HERE / "paper_water_quality.py").read_text(encoding="utf-8")
    # print DO context
    for i, line in enumerate(t.splitlines(), 1):
        if "dissolved oxygen" in line.lower() or "9 mg" in line or "saturation DO" in line:
            print(f"wq L{i}: {line.strip()[:150]}")

    # Clean water DO paragraph if broken
    t2 = re.sub(
        r"because although saturation DO is still roughly ~9 mg/L at 20 C and ~8 mg/L at 26 C, warm water raises pathogen risk and DO is harder to maintain under root demand; target [^\"]*",
        "because warm, poorly aerated water raises pathogen risk even though saturation DO is still roughly ~9 mg/L at 20 C and ~8 mg/L at 26 C. Target ",
        t,
        count=1,
    )
    if t2 != t:
        (HERE / "paper_water_quality.py").write_text(t2, encoding="utf-8", newline="\n")
        print("OK water DO sentence repair")

    # cloning half-strength leftover
    t = (HERE / "paper_cloning.py").read_text(encoding="utf-8")
    for i, line in enumerate(t.splitlines(), 1):
        if "half-strength" in line or "turgor" in line or "Water the mother" in line:
            print(f"clone L{i}: {line.strip()[:140]}")

    # pppe phone/soap lines after fix
    t = (HERE / "paper_pppe.py").read_text(encoding="utf-8")
    for i, line in enumerate(t.splitlines(), 1):
        if "83%" in line or "58%" in line or "phone" in line.lower() or "dominant" in line or "Move people" in line:
            print(f"pppe L{i}: {line.strip()[:140]}")

    print("\nPass 3 done.")


if __name__ == "__main__":
    main()
