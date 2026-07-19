# -*- coding: utf-8 -*-
"""Insert a few high-value inline community notes into soft-claim hotspots."""
from pathlib import Path

HERE = Path(__file__).resolve().parent


def inject_after_blocks_open(path: Path, section_id_substr: str, note_py: str) -> bool:
    t = path.read_text(encoding="utf-8")
    if "Community / evidence note" in t and note_py[:40] in t:
        print("skip already", path.name)
        return False
    # find SECTIONS.append with matching id
    needle = f'"id": "{section_id_substr}'
    # allow partial
    idx = -1
    for line in t.splitlines():
        if '"id":' in line and section_id_substr in line:
            idx = t.find(line)
            break
    if idx < 0:
        # looser
        idx = t.find(section_id_substr)
    if idx < 0:
        print("no section", path.name, section_id_substr)
        return False
    pos = t.find('"blocks": [', idx)
    if pos < 0:
        print("no blocks", path.name)
        return False
    pos = pos + len('"blocks": [')
    t2 = t[:pos] + "\n" + note_py + t[pos:]
    path.write_text(t2, encoding="utf-8", newline="\n")
    print("ok", path.name, section_id_substr)
    return True


NOTES = {
    "paper_flowering_stages.py": (
        "harvest",
        '''    callout("evidence", "Community / evidence note",
      "<p><strong>Borderline:</strong> Amber trichome share is a <em>maturity</em> cue, not a clean pharmacological "
      "switch. Effect is multi-factor (terpenes, dose, genotype, set/setting). Human evidence that CBN alone drives "
      "&lsquo;couch-lock&rsquo; is limited. Long plain-water flushes are traditional; controlled tests often show little "
      "taste/potency gain &mdash; ease EC as appetite falls rather than starving the plant.</p>"),
''',
    ),
    "paper_coco_crop_steering.py": (
        "steering",
        '''    callout("evidence", "Community / evidence note",
      "<p><strong>Borderline:</strong> Caplan-style single late droughts are <em>related</em> to generative drybacks "
      "but not the same experiment as multi-week daily sawteeth. Use dryback as a gentle bias; never wilt. "
      "Your probe-native % is not a universal media law.</p>"),
''',
    ),
    "paper_plant_biosignal.py": (
        "what",
        '''    callout("evidence", "Community / evidence note",
      "<p><strong>Provisional / experimental:</strong> This build logs relative biopotentials for education and "
      "correlation hunting. It is <em>not</em> a validated water, nutrient, or stress meter. Do not irrigate or "
      "feed from this signal alone.</p>"),
''',
    ),
    "paper_closed_loop.py": (
        "what",
        '''    callout("evidence", "Community / evidence note",
      "<p><strong>Provisional:</strong> Lead-time examples (tip burn in N days, whole-room health in seconds) are "
      "worked UX scenarios, not multi-site cannabis trials. Trust coupled thinking; treat prediction copy as "
      "illustrative until you measure your own false-positive rate.</p>"),
''',
    ),
    "paper_plant_state_dashboard.py": (
        "what",
        '''    callout("evidence", "Community / evidence note",
      "<p><strong>Provisional:</strong> On-screen advisories (e.g. tip-burn risk timelines) are product-design "
      "examples for operator UX &mdash; not a validated prognostic model.</p>"),
''',
    ),
    "paper_scaling_high_light.py": (
        "what",
        '''    callout("evidence", "Community / evidence note",
      "<p><strong>Borderline:</strong> High-rung EC and runoff ladders are advanced steering territory. "
      "Ambient CO&#8322; lowers efficiency of high PPFD but is not a hard 800 &micro;mol canopy wall. "
      "Size HVAC and water from your meters, not from a single ladder cell.</p>"),
''',
    ),
    "paper_f2_crop_steering.py": (
        "what",
        '''    callout("evidence", "Community / evidence note",
      "<p><strong>Operational / provisional:</strong> Default VWC numbers are one facility&rsquo;s probe-native "
      "placeholders after hand-watering. Caplan drought supports controlled deficit as a concept &mdash; not a "
      "copy-paste of these exact setpoints. Calibrate media before arming automation.</p>"),
''',
    ),
    "paper_signal_and_noise.py": (
        "what",
        '''    callout("evidence", "Community / evidence note",
      "<p><strong>Borderline:</strong> Alarm-noise percentages and control-rule mashups should be replaced with "
      "<em>your</em> measured false-positive rate. Name Western Electric vs Nelson rules correctly if you implement them.</p>"),
''',
    ),
    "paper_one_steering_law.py": (
        "what",
        '''    callout("evidence", "Community / evidence note",
      "<p><strong>Borderline:</strong> Do not import high-intensity rockwool substrate EC (mid-3s to 6) into beginner "
      "coco recipes. DWC disease risk rises with heat and low dissolved oxygen &mdash; there is no universal "
      "&lsquo;above 23 &deg;C = dead tomorrow&rsquo; clock.</p>"),
''',
    ),
    "paper_smart_watering_vrwe.py": (
        "what",
        '''    callout("evidence", "Community / evidence note",
      "<p><strong>Provisional:</strong> Multi-signal caution is sound engineering. Claims of never flooding or "
      "never starving depend on sensor health, calibration, and fail-safes &mdash; keep hard VWC floors and "
      "human override.</p>"),
''',
    ),
}


def main():
    for fn, (sec, note) in NOTES.items():
        path = HERE / fn
        if not path.exists():
            print("missing", fn)
            continue
        t = path.read_text(encoding="utf-8")
        # skip if this exact title already for this paper and section attempt
        if 'callout("evidence"' in t or "callout('evidence'" in t:
            # allow multiple? skip if already has one
            print("already evidence", fn)
            continue
        # find a section containing sec substring in id
        lines = t.splitlines(keepends=True)
        out = []
        i = 0
        inserted = False
        while i < len(lines):
            out.append(lines[i])
            if (not inserted and '"id":' in lines[i] and sec in lines[i].lower()):
                # look ahead for blocks
                j = i + 1
                while j < len(lines) and '"blocks"' not in lines[j]:
                    out.append(lines[j])
                    j += 1
                if j < len(lines):
                    out.append(lines[j])  # blocks line
                    # if same line has [, inject after
                    if "[" in lines[j]:
                        out.append(note if note.endswith("\n") else note + "\n")
                        inserted = True
                    i = j + 1
                    continue
            i += 1
        if not inserted:
            # fallback: after first blocks: [
            t2 = "".join(out)
            pos = t2.find('"blocks": [')
            if pos >= 0 and 'callout("evidence"' not in t2:
                pos = pos + len('"blocks": [')
                t2 = t2[:pos] + "\n" + note + t2[pos:]
                path.write_text(t2, encoding="utf-8", newline="\n")
                print("fallback insert", fn)
            else:
                print("FAILED", fn)
        else:
            path.write_text("".join(out), encoding="utf-8", newline="\n")
            print("inserted", fn)


if __name__ == "__main__":
    main()
