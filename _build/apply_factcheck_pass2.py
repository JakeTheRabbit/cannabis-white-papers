# -*- coding: utf-8 -*-
"""Pass 2: fix remaining fact-check issues with exact source strings."""
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent


def patch_file(name: str, pairs: list[tuple[str, str]]) -> None:
    p = HERE / name
    t = p.read_text(encoding="utf-8")
    orig = t
    for a, b in pairs:
        if a not in t:
            print(f"MISS {name}: {a[:80]!r}")
        else:
            n = t.count(a)
            t = t.replace(a, b)
            print(f"OK {name} x{n}: {a[:70]!r}")
    if t != orig:
        p.write_text(t, encoding="utf-8", newline="\n")


def main() -> None:
    # --- seeds ---
    patch_file("paper_seeds_germination.py", [
        (
            "and it reports near-99% success ",
            "and with fresh seed and controlled moisture and temperature high germination is common ",
        ),
    ])

    # Read seeds for remaining leaf/dark/auto issues
    t = (HERE / "paper_seeds_germination.py").read_text(encoding="utf-8")
    for i, line in enumerate(t.splitlines(), 1):
        if any(k in line for k in ("drinks", "darkness", "99% female", "female genetics", "12 hours", "leaf")):
            if any(k in line.lower() for k in ("drink", "dark", "female", "12 hour", "leaves")):
                print(f"seeds L{i}: {line.strip()[:130]}")

    # --- ipm sulphur ---
    patch_file("paper_ipm_sop.py", [
        (
            "to 3 tablespoons per litre, ideally 3, no more than once every 2 weeks, veg and mothers only), ",
            "only at the current registered product label rate and REI/PHI if lawful "
            "(never kitchen tablespoon rates; veg and mothers only when residues allow), ",
        ),
    ])

    # More IPM text
    t = (HERE / "paper_ipm_sop.py").read_text(encoding="utf-8")
    for i, line in enumerate(t.splitlines(), 1):
        if any(k in line for k in ("tablespoon", "Predators are", "day 21", "3 percent", "fully saturated", "harmless")):
            print(f"ipm L{i}: {line.strip()[:140]}")

    # --- flowering ---
    patch_file("paper_flowering_stages.py", [
        (
            'heavier, more sedative effect." + _c("livingston-2020-trichome-maturation")),',
            'heavier feel for some people &mdash; multi-factor, not a CBN switch." + _c("livingston-2020-trichome-maturation")),',
        ),
        (
            'window for a balanced effect, later for a more sedative one." + _c("livingston-2020-trichome-maturation")),',
            'window as a maturity cue; later cuts often feel heavier, genotype still dominates." + _c("livingston-2020-trichome-maturation")),',
        ),
        (
            '(0, 4, L.GL, "Early 60-70%"), (4, 7, L.AMBL, "Bulking 55-62%"),',
            '(0, 4, L.GL, "Early 55-65%"), (4, 7, L.AMBL, "Bulking 50-60%"),',
        ),
    ])

    # --- lighting inverse-square (split string) ---
    t = (HERE / "paper_lighting_fundamentals.py").read_text(encoding="utf-8")
    t2 = t.replace(
        'p("Light obeys the inverse-square law: roughly doubling the distance from the canopy cuts PPFD by "\n'
        '      "about 75%. Height is your coarse intensity dial, the dimmer is the fine dial. Hang about 24 in for "',
        'p("Intensity falls with distance, but the inverse-square law (quarter intensity at 2&times; distance) is a "\n'
        '      "point-source ideal &mdash; multi-bar LEDs fall off more gently. Use the fixture PPFD map and a meter. "\n'
        '      "Height is your coarse intensity dial, the dimmer is the fine dial. Hang about 24 in for "',
    )
    if t2 == t:
        # try looser
        t2 = re.sub(
            r'p\("Light obeys the inverse-square law: roughly doubling the distance from the canopy cuts PPFD by "\s*\n\s*"about 75%\.',
            'p("Intensity falls with distance, but inverse-square (quarter at 2&times; distance) is a point-source ideal for LEDs. '
            'Use a PPFD map and meter. About hang height: ',
            t,
            count=1,
        )
    if t2 != t:
        (HERE / "paper_lighting_fundamentals.py").write_text(t2, encoding="utf-8", newline="\n")
        print("OK lighting inverse-square")
    else:
        lines = t.splitlines()
        for i in range(187, 196):
            print(f"light L{i+1}: {lines[i]}")

    # LED efficacy citation note - soften nelson claim if still there
    t = (HERE / "paper_lighting_fundamentals.py").read_text(encoding="utf-8")
    t2 = t.replace(
        "at roughly 2.7-3.0 umol/J for good fixtures (budget units 2.0-2.3)",
        "at roughly 2.7-3.5 umol/J for good modern fixtures (budget units ~2.0-2.5)",
    )
    t2 = t2.replace(
        "at roughly 2.7-3.0 &micro;mol/J for good fixtures (budget units 2.0-2.3)",
        "at roughly 2.7-3.5 &micro;mol/J for good modern fixtures (budget units ~2.0-2.5)",
    )
    if t2 != t:
        (HERE / "paper_lighting_fundamentals.py").write_text(t2, encoding="utf-8", newline="\n")
        print("OK lighting efficacy band")

    # --- closed loop 70% ---
    t = (HERE / "paper_closed_loop.py").read_text(encoding="utf-8")
    t2 = t.replace(
        "around <strong>70% of raw alerts are ",
        "many <strong>raw alerts are ",
    )
    # also fix the rest of the sentence if needed
    t2 = t2.replace(
        "Every measurement is signal plus noise, and in practice around <strong>70% of raw alerts are ",
        "Every measurement is signal plus noise, and in practice many <strong>raw alerts are ",
    )
    if t2 != t:
        (HERE / "paper_closed_loop.py").write_text(t2, encoding="utf-8", newline="\n")
        print("OK closed-loop 70%")
    else:
        for i, line in enumerate(t.splitlines(), 1):
            if "70%" in line or "raw alerts" in line:
                print(f"closed L{i}: {line}")
                print(f"closed L{i+1}: {t.splitlines()[i]}")

    # --- water quality DO (broken hybrid text) ---
    t = (HERE / "paper_water_quality.py").read_text(encoding="utf-8")
    t2 = t
    t2 = t2.replace(
        "because dissolved oxygen falls from about ~9 mg/L saturation at 20 C to only 3-4 ppm ",
        "because although saturation DO is still roughly ~9 mg/L at 20 C and ~8 mg/L at 26 C, warm water raises pathogen risk and DO is harder to maintain under root demand; target ",
    )
    # fix second bad sentence
    t2 = t2.replace(
        "Dissolved oxygen declines steadily as water warms, from about 5-6 ppm near 20 C down toward ",
        "Saturation dissolved oxygen declines gently as water warms (roughly ~9 mg/L near 20 C toward ",
    )
    t2 = t2.replace(
        "from about 5-6 ppm near 20 C down toward 3-4 ppm near 26 C",
        "from roughly ~9 mg/L near 20 C toward ~8 mg/L near 26 C",
    )
    if t2 != t:
        (HERE / "paper_water_quality.py").write_text(t2, encoding="utf-8", newline="\n")
        print("OK water-quality DO cleanup")
    for i, line in enumerate(t2.splitlines(), 1):
        if "ppm" in line and ("oxygen" in line.lower() or "5-6" in line or "3-4" in line or "9 mg" in line):
            print(f"water L{i}: {line.strip()[:140]}")

    # --- substrates living soil ---
    t = (HERE / "paper_substrates_overview.py").read_text(encoding="utf-8")
    t2 = t.replace(
        "root zone near pH 5.2-6.5 within minutes of watering regardless of your water's pH, so you ",
        "root zone near pH 5.2-6.5 over hours to days when biology is healthy. Many organic growers still ",
    )
    t2 = t2.replace(
        "generally do not pH your input at all",
        "do not acidify routine waterings, but avoid extreme alkaline water and monitor if problems appear",
    )
    if t2 != t:
        (HERE / "paper_substrates_overview.py").write_text(t2, encoding="utf-8", newline="\n")
        print("OK substrates living soil")
    else:
        for i, line in enumerate(t.splitlines(), 1):
            if "minutes of watering" in line or "do not pH" in line:
                print(f"sub L{i}: {line}")
                print(f"sub L{i+1}: {t.splitlines()[i]}")

    # --- under canopy viability ---
    patch_file("paper_under_canopy_lighting.py", [
        (
            '["Viability floor", "400&ndash;500 &micro;mol", "Minimum for adequate flower development"],',
            '["Common commercial band", "300&ndash;600 &micro;mol", "Typical target to fill lower flower (not a hard biological floor)"],',
        ),
    ])

    # --- one steering never flood slogan ---
    t = (HERE / "paper_one_steering_law.py").read_text(encoding="utf-8")
    t2 = t.replace("never flood, never starve", "prefer mild deficit over flooding when uncertain; keep a hard VWC floor")
    t2 = t2.replace("never flood ", "do not flood ")
    if t2 != t:
        (HERE / "paper_one_steering_law.py").write_text(t2, encoding="utf-8", newline="\n")
        print("OK one-steering flood slogan")

    # --- smart watering already fixed; VRWE in one-steering ---

    # --- mould 3.5x absolute risk ---
    t = (HERE / "paper_mould_risk.py").read_text(encoding="utf-8")
    for i, line in enumerate(t.splitlines(), 1):
        if "3.5" in line or "fungal infection" in line.lower():
            print(f"mould L{i}: {line.strip()[:140]}")

    # --- pppe remaining ---
    t = (HERE / "paper_pppe.py").read_text(encoding="utf-8")
    for i, line in enumerate(t.splitlines(), 1):
        if any(k in line for k in ("83%", "58%", "log", "toilet", "70 to 90", "dirty", "clean to dirty", "100% transmission")):
            print(f"pppe L{i}: {line.strip()[:140]}")

    # --- cloning remaining ---
    t = (HERE / "paper_cloning.py").read_text(encoding="utf-8")
    for i, line in enumerate(t.splitlines(), 1):
        if any(k in line for k in ("turgor", "half-strength", "embolism", "IBA", "1.5", "90")):
            print(f"clone L{i}: {line.strip()[:140]}")

    # --- tissue remaining ---
    t = (HERE / "paper_tissue_culture.py").read_text(encoding="utf-8")
    for i, line in enumerate(t.splitlines(), 1):
        if any(k in line for k in ("100%", "50%", "90% of California", "totipoten", "leaves behind fungal", "DNA test", "RT-qPCR")):
            print(f"tc L{i}: {line.strip()[:140]}")

    # --- export_corpus remaining peer-reviewed ---
    t = (HERE / "export_corpus.py").read_text(encoding="utf-8")
    t2 = t
    for a, b in [
        ("peer-reviewed white papers", "evidence-linked field guides"),
        ("peer-reviewed cannabis cultivation white papers", "evidence-linked cannabis cultivation field guides"),
        ("peer-reviewed, beginner-friendly", "evidence-linked, beginner-friendly"),
        ("Every factual claim is cited inline `[n]` to a per-paper References list - peer-reviewed ",
         "Every factual claim is cited inline `[n]` to a per-paper References list - primary literature "),
        ("peer-reviewed sources", "primary literature and official guidance"),
        ("Peer-reviewed sources", "Primary literature and official guidance"),
    ]:
        if a in t2:
            t2 = t2.replace(a, b)
            print(f"export replace: {a[:50]}")
    if t2 != t:
        (HERE / "export_corpus.py").write_text(t2, encoding="utf-8", newline="\n")

    # build.py remaining
    t = (HERE / "build.py").read_text(encoding="utf-8")
    for i, line in enumerate(t.splitlines(), 1):
        if "peer" in line.lower() and "review" in line.lower():
            print(f"build L{i}: {line.strip()[:140]}")

    # --- coco Caplan / dryback ---
    t = (HERE / "paper_coco_crop_steering.py").read_text(encoding="utf-8")
    for i, line in enumerate(t.splitlines(), 1):
        if "Caplan" in line or "cannabinoid" in line.lower() and "yield" in line.lower() or "Flush" in line:
            print(f"coco L{i}: {line.strip()[:140]}")

    # --- harvest AROYA ---
    t = (HERE / "paper_harvest_dry_trim_cure.py").read_text(encoding="utf-8")
    for i, line in enumerate(t.splitlines(), 1):
        if "5-10%" in line or "10%" in line and "wet" in line.lower() or "0.60 aw" in line:
            print(f"harv L{i}: {line.strip()[:140]}")

    # --- scaling ---
    t = (HERE / "paper_scaling_high_light.py").read_text(encoding="utf-8")
    for i, line in enumerate(t.splitlines(), 1):
        if "800" in line or "3.6" in line or "runoff" in line.lower():
            if any(k in line for k in ("800", "3.6", "7", "saturat", "Ambient")):
                print(f"scale L{i}: {line.strip()[:140]}")

    # --- irrigation polarity verify ---
    t = (HERE / "paper_irrigation_manual.py").read_text(encoding="utf-8")
    for i, line in enumerate(t.splitlines(), 1):
        if "dryback" in line.lower() and ("veg" in line.lower() or "gen" in line.lower() or "Vegetative" in line or "Generative" in line):
            print(f"irr L{i}: {line.strip()[:140]}")

    # --- ph 10% ---
    t = (HERE / "paper_ph_management.py").read_text(encoding="utf-8")
    for i, line in enumerate(t.splitlines(), 1):
        if "10 percent" in line or "10%" in line or "phosphoric" in line or "lock out" in line:
            print(f"ph L{i}: {line.strip()[:140]}")

    # --- gmp ---
    t = (HERE / "paper_gmp_hash_lab.py").read_text(encoding="utf-8")
    for i, line in enumerate(t.splitlines(), 1):
        if "5-" in line and "10" in line or "multipl" in line.lower() and "contamin" in line.lower():
            print(f"gmp L{i}: {line.strip()[:140]}")

    # --- daily checks GACP ---
    t = (HERE / "paper_daily_checks.py").read_text(encoding="utf-8")
    t2 = t.replace(
        "for a seed-to-harvest trail under GACP and GMP",
        "for operational seed-to-harvest discipline (regulated GACP/GMP release still needs validated systems and QA-approved procedures",
    )
    # fix possible missing paren
    if t2 != t and t2.count("(") != t2.count(")"):
        t2 = t.replace(
            "for a seed-to-harvest trail under GACP and GMP",
            "for operational seed-to-harvest discipline (regulated GACP/GMP still needs validated systems)",
        )
    if t2 != t:
        (HERE / "paper_daily_checks.py").write_text(t2, encoding="utf-8", newline="\n")
        print("OK daily-checks GACP")

    # --- plant state tip burn ---
    t = (HERE / "paper_plant_state_dashboard.py").read_text(encoding="utf-8")
    t2 = t.replace("tip burn likely within ~48h", "tip burn risk elevated (illustrative UX, not a validated prognosis)")
    t2 = t2.replace("within ~48h", "soon (illustrative)")
    if t2 != t:
        (HERE / "paper_plant_state_dashboard.py").write_text(t2, encoding="utf-8", newline="\n")
        print("OK plant-state tipburn")

    # --- biosignal SUB ---
    t = (HERE / "paper_plant_biosignal.py").read_text(encoding="utf-8")
    t2 = t.replace("water and stress insight", "relative biopotential changes for education only")
    t2 = t2.replace("~85% accurate on this exact hardware class",
                    "one study reported ~85% under its protocol; expect lower performance in noisy rooms")
    if t2 != t:
        (HERE / "paper_plant_biosignal.py").write_text(t2, encoding="utf-8", newline="\n")
        print("OK biosignal residual")

    # --- defoliation day 5-7 ---
    t = (HERE / "paper_defoliation_training.py").read_text(encoding="utf-8")
    t2 = re.sub(
        r"day 5[-–]7 of veg",
        "once plants are established with enough nodes (seed starts need longer than multi-node clones)",
        t,
        count=3,
    )
    if t2 != t:
        (HERE / "paper_defoliation_training.py").write_text(t2, encoding="utf-8", newline="\n")
        print("OK defoliation topping timing")

    # --- grow room VPD lettuce ---
    t = (HERE / "paper_grow_room_systems.py").read_text(encoding="utf-8")
    t2 = t.replace(
        "Most growth happens around 0.8-1.2 kPa",
        "A practical mid-band is around 0.8-1.2 kPa (cultivar-dependent; late flower often ~1.2-1.5)",
    )
    t2 = t2.replace(
        "Most growth happens around 0.8&ndash;1.2 kPa",
        "A practical mid-band is around 0.8&ndash;1.2 kPa (cultivar-dependent; late flower often ~1.2&ndash;1.5)",
    )
    if t2 != t:
        (HERE / "paper_grow_room_systems.py").write_text(t2, encoding="utf-8", newline="\n")
        print("OK grow-room VPD")

    # --- pest mites ---
    t = (HERE / "paper_pest_id.py").read_text(encoding="utf-8")
    # add split note if russet and broad lumped
    if "Russet" in t and "broad" in t.lower() and "do not treat until" not in t:
        t2 = t.replace(
            "Russet and broad mites",
            "Russet and broad mites (confirm at 60&ndash;100&times; before treating; symptoms overlap with heat tacoing and tip burn)",
            1,
        )
        if t2 != t:
            (HERE / "paper_pest_id.py").write_text(t2, encoding="utf-8", newline="\n")
            print("OK pest lookalike note")

    # --- co2 remaining ---
    t = (HERE / "paper_co2_enrichment.py").read_text(encoding="utf-8")
    t2 = t.replace(
        "potentially toward percent-level concentrations",
        "and possibly higher if sealed and packed &mdash; measure your room",
    )
    t2 = t2.replace(
        "Because CO2 is denser than air it sinks, so run the supply line above the canopy",
        "At enrichment ppm, fan mixing dominates; still run the supply above the canopy and mix with HAF. "
        "Pure leaks can pool low, so put life-safety sensors near the floor. Run the supply line above the canopy",
    )
    t2 = t2.replace(
        "Measurable dip in concentration and decision-making",
        "Some studies report small cognitive effects (literature mixed)",
    )
    if t2 != t:
        (HERE / "paper_co2_enrichment.py").write_text(t2, encoding="utf-8", newline="\n")
        print("OK co2 residual")

    # --- harvest residual ---
    t = (HERE / "paper_harvest_dry_trim_cure.py").read_text(encoding="utf-8")
    t2 = t.replace(
        "is reported to add 5-10% to final yield, because most growers are accidentally over-drying and losing sellable weight.",
        "often recovers sellable mass versus bone-dry flower. Vendor education sometimes cites ~5&ndash;10% recovered weight &mdash; illustrative, not guaranteed.",
    )
    t2 = t2.replace(
        "which lands around 10% in practice (a real example batch came in at 10.46%)",
        "which is often ~10% of whole-plant wet weight in many rooms (example batch 10.46%; depends on stem share and definition &mdash; log your genetics)",
    )
    if t2 != t:
        (HERE / "paper_harvest_dry_trim_cure.py").write_text(t2, encoding="utf-8", newline="\n")
        print("OK harvest residual")

    # --- gmp residual ---
    t = (HERE / "paper_gmp_hash_lab.py").read_text(encoding="utf-8")
    t2 = re.sub(
        r"multipl(?:ies|y) contaminants .{0,10}5.?to.?10.?fold",
        "can concentrate contaminants several-fold (often ~5&ndash;10&times; when mass yield is low and residues follow resin &mdash; process-dependent)",
        t,
        count=2,
        flags=re.I,
    )
    if t2 != t:
        (HERE / "paper_gmp_hash_lab.py").write_text(t2, encoding="utf-8", newline="\n")
        print("OK gmp residual")

    # --- signal western electric ---
    t = (HERE / "paper_signal_and_noise.py").read_text(encoding="utf-8")
    for i, line in enumerate(t.splitlines(), 1):
        if "Western" in line or "7+" in line or "8+" in line or "70%" in line or "noise" in line and "alert" in line:
            print(f"sig L{i}: {line.strip()[:140]}")

    # --- f2 numbers disclaimer ---
    t = (HERE / "paper_f2_crop_steering.py").read_text(encoding="utf-8")
    if "probe-native" not in t and "field_capacity" in t:
        t2 = t.replace(
            "Starting VWC targets",
            "Starting VWC targets (one facility's probe-native numbers after hand-watering &mdash; not universal %)",
            1,
        )
        if t2 == t:
            t2 = t.replace(
                "These are starting",
                "These are one facility's probe-native starting",
                1,
            )
        if t2 != t:
            (HERE / "paper_f2_crop_steering.py").write_text(t2, encoding="utf-8", newline="\n")
            print("OK f2 disclaimer")

    # --- root zone cal ---
    t = (HERE / "paper_root_zone_teros12.py").read_text(encoding="utf-8")
    t2 = t.replace(
        "Calibration corrects an additive offset",
        "Calibration reduces error (often more than a simple additive offset; EC and temperature still interact)",
    )
    if t2 != t:
        (HERE / "paper_root_zone_teros12.py").write_text(t2, encoding="utf-8", newline="\n")
        print("OK teros cal")

    # --- facility WAC ---
    t = (HERE / "paper_facility_3d.py").read_text(encoding="utf-8")
    t2 = t.replace(
        "Washington WAC",
        "Washington WAC (illustration only; use your inspecting jurisdiction)",
    )
    # avoid double
    t2 = t2.replace(
        "Washington WAC (illustration only; use your inspecting jurisdiction) (illustration only; use your inspecting jurisdiction)",
        "Washington WAC (illustration only; use your inspecting jurisdiction)",
    )
    if t2 != t:
        (HERE / "paper_facility_3d.py").write_text(t2, encoding="utf-8", newline="\n")
        print("OK facility WAC")

    # --- ph residual ---
    t = (HERE / "paper_ph_management.py").read_text(encoding="utf-8")
    t2 = t.replace(
        "keep feed and runoff EC within about 10 percent of each other",
        "treat large runaway gaps (runoff &raquo; feed) as salt buildup; advanced steering may hold higher root-zone EC on purpose",
    )
    t2 = t2.replace(
        "calcium, magnesium and phosphorus lock out instead",
        "calcium, magnesium and phosphorus availability can fall while iron and manganese can push toward toxicity",
    )
    if t2 != t:
        (HERE / "paper_ph_management.py").write_text(t2, encoding="utf-8", newline="\n")
        print("OK ph residual")

    # --- nutrient deficiencies sulfur + ppm ---
    t = (HERE / "paper_nutrient_deficiencies.py").read_text(encoding="utf-8")
    t2 = t.replace("more than about 200 PPM above input", "rising ~0.3&ndash;0.5 mS/cm above feed for days")
    t2 = t2.replace('["Sulfur (S)", "Immobile"', '["Sulfur (S)", "Limited mobility"')
    if t2 != t:
        (HERE / "paper_nutrient_deficiencies.py").write_text(t2, encoding="utf-8", newline="\n")
        print("OK deficiencies residual")

    # --- tissue clean-out scope ---
    t = (HERE / "paper_tissue_culture.py").read_text(encoding="utf-8")
    t2 = re.sub(
        r"a clean start also leaves behind fungal root-rots.{0,200}eggs\.",
        "meristem work plus indexing mainly targets systemic agents (viroids/viruses); surface sterilisation "
        "removes many surface microbes and hitch-hikers, but endophytes can still emerge and mites remain an IPM problem.",
        t,
        count=1,
        flags=re.S,
    )
    t2 = re.sub(
        r"Surveys found HpLVd in roughly <strong>90% of California facilities</strong>.{0,80}Canadian dispensary flower\.",
        "Industry and research surveys have reported very high facility infection rates in California "
        "(~90% in one large testing programme) and frequent positives in Canadian retail flower (~40% in one study) "
        "&mdash; treat as warning signals, not permanent global prevalence.",
        t2,
        count=1,
        flags=re.S,
    )
    if t2 != t:
        (HERE / "paper_tissue_culture.py").write_text(t2, encoding="utf-8", newline="\n")
        print("OK tissue residual")

    # --- cloning embolism / IBA ---
    t = (HERE / "paper_cloning.py").read_text(encoding="utf-8")
    t2 = re.sub(
        r"air embolism.{0,80}",
        "dried cut that stalls water uptake. ",
        t,
        count=2,
        flags=re.I,
    )
    t2 = re.sub(
        r"a synthetic version of a natural.{0,40}auxin",
        "an auxin used in rooting products (often converted to IAA in the plant)",
        t2,
        count=2,
        flags=re.I,
    )
    if t2 != t:
        (HERE / "paper_cloning.py").write_text(t2, encoding="utf-8", newline="\n")
        print("OK cloning residual")

    # --- coco Caplan ---
    t = (HERE / "paper_coco_crop_steering.py").read_text(encoding="utf-8")
    t2 = re.sub(
        r"raise cannabinoid content without costing yield",
        "raise cannabinoid concentrations in one carefully timed late drought study (related to, but not the same as, daily drybacks)",
        t,
        count=2,
        flags=re.I,
    )
    t2 = t2.replace(
        "Flush / finish",
        "Finish (ease EC; long plain-water flush has weak quality evidence)",
    )
    if t2 != t:
        (HERE / "paper_coco_crop_steering.py").write_text(t2, encoding="utf-8", newline="\n")
        print("OK coco residual")

    # --- mould 3.5x ---
    t = (HERE / "paper_mould_risk.py").read_text(encoding="utf-8")
    t2 = re.sub(
        r"fungal infections at roughly <strong>3\.5.?&times;</strong> the rate of non-users",
        "coded fungal infections about <strong>3.5&times;</strong> more often than non-users in one claims analysis "
        "(absolute rates still low; immunocompromised patients are the high-stakes group)",
        t,
        count=2,
        flags=re.I,
    )
    t2 = re.sub(
        r"3\.5.?&times;.{0,40}non-users",
        "3.5&times; more often than non-users in one claims analysis (absolute rates still low)",
        t2,
        count=2,
        flags=re.I,
    )
    if t2 != t:
        (HERE / "paper_mould_risk.py").write_text(t2, encoding="utf-8", newline="\n")
        print("OK mould residual")

    # --- pppe hand hygiene remaining ---
    t = (HERE / "paper_pppe.py").read_text(encoding="utf-8")
    t2 = re.sub(
        r"~3 log,? ~83%",
        "~2&ndash;3 log (~99&ndash;99.9% under test conditions)",
        t,
        count=3,
    )
    t2 = re.sub(
        r"~2 log,? ~58%",
        "soil and organism removal without sterilisation",
        t2,
        count=3,
    )
    t2 = t2.replace("toilet seat", "high-touch fomite that contacts faces and hands")
    t2 = t2.replace("70 to 90 percent", "typically the dominant share (exact percent varies)")
    t2 = t2.replace("dirty to clean", "clean to dirty for people/materials (waste exits dirty)")
    t2 = re.sub(
        r"up to <strong>100% transmission within four weeks</strong>",
        "under experimental conditions infection of linked cuttings can approach complete cohort infection within weeks",
        t2,
        count=2,
    )
    if t2 != t:
        (HERE / "paper_pppe.py").write_text(t2, encoding="utf-8", newline="\n")
        print("OK pppe residual")

    # --- ipm predators / day21 / 3% ---
    t = (HERE / "paper_ipm_sop.py").read_text(encoding="utf-8")
    t2 = t.replace(
        "Predators are harmless to the plant and to people. There is no residue and no withholding period.",
        "Predatory arthropods typically leave no chemical residue or PHI, but microbials follow labels, "
        "worker allergy risk is real for some beneficials, and agents must be legal in your jurisdiction.",
    )
    t2 = t2.replace(
        "Predators are harmless to the plant and to people",
        "Predatory arthropods usually leave no chemical residue, but must be legal and compatible",
    )
    t2 = re.sub(
        r"only from mothering through day 21 of flower, with no foliar treatment after buds form",
        "in many residue-aware facilities only through early flower (example day 21); your PHI and QA SOP set the real cutoff",
        t2,
        count=2,
    )
    t2 = t2.replace(
        "Once more than 3 percent of a room is affected, escalate to approved pesticide applications",
        "As an example planning default, once more than 3 percent of a room is affected, escalate "
        "(zero-tolerance organisms override any percentage)",
    )
    t2 = t2.replace(
        "Spray when the media is fully saturated so the product is not pulled into the leaves",
        "Avoid foliar applications under high light, high VPD, or drought stress; do not spray wilted plants",
    )
    if t2 != t:
        (HERE / "paper_ipm_sop.py").write_text(t2, encoding="utf-8", newline="\n")
        print("OK ipm residual")

    # --- signal noise remaining ---
    t = (HERE / "paper_signal_and_noise.py").read_text(encoding="utf-8")
    t2 = re.sub(
        r"perhaps 70% in a busy room, are noise",
        "often many alerts in a busy room are noise until tuned",
        t,
        count=2,
    )
    t2 = re.sub(
        r"7\+ points all trending in one direction, or 8\+ points on one side of the mean",
        "Western Electric / Nelson-style rules (e.g. eight consecutive on one side; Nelson trends often use six points)",
        t2,
        count=2,
    )
    if t2 != t:
        (HERE / "paper_signal_and_noise.py").write_text(t2, encoding="utf-8", newline="\n")
        print("OK signal residual")

    # Final peer-reviewed in META should already be Evidence-linked
    print("\n=== Remaining Peer-reviewed in paper modules ===")
    for p in sorted(HERE.glob("paper_*.py")):
        tt = p.read_text(encoding="utf-8")
        if "Peer-reviewed" in tt:
            for i, line in enumerate(tt.splitlines(), 1):
                if "Peer-reviewed" in line:
                    print(f"  {p.name}:{i}: {line.strip()[:100]}")

    print("\nPass 2 complete.")


if __name__ == "__main__":
    main()
