# -*- coding: utf-8 -*-
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent


def main() -> None:
    # pppe
    p = HERE / "paper_pppe.py"
    t = p.read_text(encoding="utf-8")
    t = t.replace(
        "<strong>Your phone is filthier than a high-touch fomite that contacts faces and hands.</strong> "
        "Cultured phones carry roughly an ",
        "<strong>Your phone is a high-touch fomite.</strong> Phones carry skin and environmental flora and ",
    )
    t = t.replace(
        "<strong>Your phone is filthier than a high-touch fomite that contacts faces and hands.</strong> Cultured phones carry roughly an ",
        "<strong>Your phone is a high-touch fomite.</strong> Phones carry skin and environmental flora and ",
    )
    # Fix dominant share double-speak
    t = re.sub(
        r"People are the dominant contamination source in any clean space, typically the <strong>dominant share</strong> \([^)]*\)[^\"\n]*",
        "People are typically the dominant contamination source in any clean space "
        "(exact share varies by facility design)",
        t,
        count=1,
    )
    # transmission
    t = t.replace(
        "with up to <strong>100% transmission within four weeks</strong>",
        "and under experimental conditions infection of linked cuttings can approach complete cohort infection within weeks",
    )
    # soap residual
    t = t.replace("and water about 58%", "and water remove soil and many organisms without sterilising")
    t = t.replace("removes about 83% of organisms", "often achieve ~2–3 log reductions (~99–99.9%) under test conditions")
    p.write_text(t, encoding="utf-8", newline="\n")
    print("pppe done")

    # grow room
    p = HERE / "paper_grow_room_systems.py"
    t = p.read_text(encoding="utf-8")
    t = t.replace(
        "Most growth happens around 0.8–1.2 kPa. Drier air pushes generative, but past ~1.5 kPa the ",
        "A practical mid-band is around 0.8–1.2 kPa (cultivar-dependent; late flower often ~1.2–1.5). "
        "Drier air can push generative, but past ~1.5 kPa the ",
    )
    t = t.replace(
        '["Leaf edges curling/taco at high light", "VPD too high, so the plant closed its stomata", "Lower VPD (cooler/more humid',
        '["Leaf edges curling/taco at high light", "Often light + leaf heat + VPD, not VPD alone", '
        '"Check PPFD and leaf temp first, then VPD (cooler/more humid',
    )
    p.write_text(t, encoding="utf-8", newline="\n")
    print("grow room done")

    # coco
    p = HERE / "paper_coco_crop_steering.py"
    t = p.read_text(encoding="utf-8")
    if "Flush / finish" in t:
        t = t.replace("Flush / finish", "Finish (ease EC)")
        t = t.replace(
            "Lower EC feeds in the final stretch. Let the plant wind down cleanly.",
            "Ease EC as demand falls; long plain-water flushes have weak quality evidence.",
        )
        p.write_text(t, encoding="utf-8", newline="\n")
        print("coco done")
    else:
        print("coco already ok")

    # cloning embolism
    p = HERE / "paper_cloning.py"
    t = p.read_text(encoding="utf-8")
    t2 = t.replace(
        "draws in an <strong>air embolism</strong> (an air bubble) that blocks water uptake",
        "dries and stalls water uptake (desiccation more than classic woody-stem embolism)",
    )
    t2 = re.sub(
        r"(IBA \(indole-3-butyric acid\)</strong>), a\s*\n\s*\"synthetic version of a natural[^\"]*\"",
        r"\1, an auxin used in rooting products (plants often convert IBA to IAA)\"",
        t2,
        count=1,
    )
    # simpler IBA
    if "synthetic version" in t2:
        t2 = t2.replace("synthetic version of a natural plant root hormone called an auxin",
                        "an auxin used in rooting products (often converted to IAA in the plant)")
        t2 = t2.replace("a synthetic version of a natural", "an")
    if t2 != t:
        p.write_text(t2, encoding="utf-8", newline="\n")
        print("cloning done")
    else:
        for i, line in enumerate(t.splitlines(), 1):
            if "embolism" in line or "synthetic" in line:
                print(f"clone still L{i}: {line[:130]}")

    # ipm predators leftover
    p = HERE / "paper_ipm_sop.py"
    t = p.read_text(encoding="utf-8")
    t2 = t.replace(
        "Predators are harmless to the plant and to people. When the prey runs out they die off on ",
        "Predatory arthropods typically leave no chemical PHI, but legality and allergy risk matter. When the prey runs out they die off on ",
    )
    if t2 != t:
        p.write_text(t2, encoding="utf-8", newline="\n")
        print("ipm predators done")

    # tissue fungal block if still present
    p = HERE / "paper_tissue_culture.py"
    t = p.read_text(encoding="utf-8")
    if "leaves behind fungal root-rots" in t:
        lines = t.splitlines()
        out = []
        i = 0
        while i < len(lines):
            if "leaves behind fungal root-rots" in lines[i]:
                # replace this p() call entirely - find start
                # walk back to p(
                j = i
                while j > 0 and "p(" not in lines[j]:
                    j -= 1
                # remove from j to closing ),
                k = i
                while k < len(lines) and not (lines[k].rstrip().endswith("),") or lines[k].rstrip().endswith(").")):
                    k += 1
                # keep lines before j
                while len(out) and any("fungal root-rots" in x or "HpLVd gets the headlines" in x for x in out[-3:]):
                    # already handled
                    break
                # rebuild: drop j..k and insert new
                # Actually simpler: out already has lines before j if we detect late
                # Reset approach
                pass
            out.append(lines[i])
            i += 1
        # direct replace multi-line via regex
        t2 = re.sub(
            r'p\("HpLVd gets the headlines, but a clean start also leaves behind fungal root-rots ".*?\)\s*,',
            'p("HpLVd gets the headlines. Meristem work plus indexing mainly targets systemic agents '
            '(viroids/viruses); surface sterilisation removes many surface microbes and hitch-hikers, '
            'but endophytes can still emerge and mites remain an IPM problem."),',
            t,
            count=1,
            flags=re.S,
        )
        if t2 != t:
            p.write_text(t2, encoding="utf-8", newline="\n")
            print("tissue fungal done")
        else:
            print("tissue fungal still present - manual")
            for i, line in enumerate(t.splitlines(), 1):
                if "fungal root" in line or "HpLVd gets" in line:
                    print(i, line[:120])

    # one more: pppe 100% transmission
    p = HERE / "paper_pppe.py"
    t = p.read_text(encoding="utf-8")
    if "100% transmission" in t:
        t = t.replace(
            "up to <strong>100% transmission within four weeks</strong> of propagation from infected",
            "under experimental conditions linked cuttings can approach complete infection within weeks of propagation from infected",
        )
        p.write_text(t, encoding="utf-8", newline="\n")
        print("pppe transmission")

    # Final audit
    needles = [
        "tablespoon", "near-99%", "about 28%", "four to five times", "5-6 ppm",
        "3-4 ppm at 26", "83%", "58%", "dirty to clean", "70% of raw", "perhaps 70%",
        "red-rich", "phone-screen", "couch-lock", "100% of what you put",
        "Peer-reviewed cultivation", "leaf leaf curves", "well-run rooms often",
        "longer drybacks held", "Shorter, firmer drybacks", "filthier than a high-touch",
    ]
    print("\n=== AUDIT ===")
    for n in needles:
        hits = []
        for f in HERE.glob("paper_*.py"):
            tt = f.read_text(encoding="utf-8")
            if n in tt:
                hits.append(f.name)
        for f in ["build.py", "export_corpus.py"]:
            tt = (HERE / f).read_text(encoding="utf-8")
            if n in tt:
                hits.append(f)
        if hits:
            print(f"STILL {n!r}: {hits}")
        else:
            print(f"clean {n!r}")


if __name__ == "__main__":
    main()
