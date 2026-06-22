# -*- coding: utf-8 -*-
"""Parse the image-plan workflow output into:
  _gen/assets_manifest.json   list of {file, prompt, model, ar, res} to generate
  _gen/embed_map.json         {slug:{gallery:[[term,src]], sequences:[{section_id,title,caption,frames:[[label,src]]}]}}
Appends a uniform medical-facility + PPE + no-text style suffix to every prompt."""
import json, os, re
OUT = r"C:\Users\OEM\AppData\Local\Temp\claude\C--Github\88d48e04-5811-43de-a2d7-078d94466ad8\tasks\wh7t6woec.output"
HERE = os.path.dirname(__file__); GEN = os.path.join(HERE, "_gen")
raw = json.load(open(OUT, encoding="utf-8"))
arr = raw["result"] if isinstance(raw, dict) and "result" in raw else raw

STYLE = (" Photorealistic, inside a clean modern licensed medical cannabis production facility; "
         "hygienic white and stainless surfaces, bright even lighting, documentary realism, sharp "
         "focus, shallow depth of field. Any people present wear correct PPE: nitrile gloves, "
         "hairnet, clean lab coat or gown, closed shoes; no bare hands on product, no smoking, "
         "eating or naked flames. No text, words or labels in the image.")
NB = "nano_banana_2"

def slug(s): return re.sub(r"[^a-z0-9]+", "-", (s or "").lower()).strip("-")[:40]

manifest = {}   # file -> entry (dedupe)
embed = {}      # slug -> {gallery, sequences}
for plan in arr:
    if not plan: continue
    s = plan["slug"]; em = {"gallery": [], "sequences": []}
    nt = 0
    for t in plan.get("terms", []):
        if not t.get("visual") or not (t.get("prompt") or "").strip() or nt >= 6:
            continue
        nt += 1
        f = f"t-{s}-{slug(t['term'])}.jpg"
        manifest[f] = {"file": f, "prompt": t["prompt"].strip() + STYLE, "model": NB, "ar": "4:3", "res": "1k"}
        em["gallery"].append([t["term"], f"assets/img/{f}"])
    for seq in plan.get("sequences", [])[:1]:   # one progression per paper
        frames = []
        for i, fr in enumerate(seq.get("frames", [])[:3]):
            if not (fr.get("prompt") or "").strip():
                continue
            f = f"s-{s}-{slug(seq['id'])}-{i}.jpg"
            manifest[f] = {"file": f, "prompt": fr["prompt"].strip() + STYLE, "model": NB, "ar": "1:1", "res": "1k"}
            frames.append([fr.get("label", ""), f"assets/img/{f}"])
        if frames:
            em["sequences"].append({"section_id": seq.get("section_id", ""), "title": seq.get("title", ""),
                                    "caption": seq.get("caption", ""), "frames": frames})
    embed[s] = em

json.dump(list(manifest.values()), open(os.path.join(GEN, "assets_manifest.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
json.dump(embed, open(os.path.join(GEN, "embed_map.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
ng = sum(len(e["gallery"]) for e in embed.values())
ns = sum(len(s["frames"]) for e in embed.values() for s in e["sequences"])
print(f"papers:{len(embed)}  term-images:{ng}  seq-frames:{ns}  total to generate:{len(manifest)}")
print(f"est credits (nano 1k ~2 cr): ~{len(manifest)*2}")
