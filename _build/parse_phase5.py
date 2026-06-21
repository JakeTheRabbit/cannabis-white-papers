# -*- coding: utf-8 -*-
"""Parse Phase-5 output -> data/refs_gen5.py, data/glossary_gen5.py, _gen/<slug>.json."""
import json, os, re
OUT = r"C:\Users\OEM\AppData\Local\Temp\claude\C--Github\88d48e04-5811-43de-a2d7-078d94466ad8\tasks\w39w88zq8.output"
HERE = os.path.dirname(__file__)
GEN = os.path.join(HERE, "_gen"); os.makedirs(GEN, exist_ok=True)
raw = json.load(open(OUT, encoding="utf-8"))
arr = raw["result"] if isinstance(raw, dict) and "result" in raw else raw
import data.refs as RREF
import data.glossary as GLEX
existing_refs = set(RREF.REFS.keys())
existing_terms = {g["term"].strip().lower() for g in GLEX.GLOSSARY}
def slugify(s): return re.sub(r"[^a-z0-9]+", "-", (s or "").lower()).strip("-")
refs_add, gloss_add, manifest = {}, {}, []
for paper in arr:
    slug = paper["slug"]; d = paper.get("data") or {}
    outline = d.get("outline") or {}; refs = d.get("refs") or []
    ref_ids = []
    for r in refs:
        rid = slugify(r.get("id") or slugify(r.get("cite", ""))[:40]) or ("ref-" + str(len(refs_add)))
        if rid not in existing_refs and rid not in refs_add:
            refs_add[rid] = {"cite": (r.get("cite") or "").strip(), "url": (r.get("url") or "").strip(), "peer": bool(r.get("peer"))}
        if rid not in ref_ids: ref_ids.append(rid)
    for g in outline.get("glossary", []):
        t = (g.get("term") or "").strip(); tl = t.lower()
        if t and tl not in existing_terms and tl not in gloss_add:
            gloss_add[tl] = {"term": t, "defn": (g.get("defn") or "").strip(), "tags": ["reference"]}
    rec = {"slug": slug, "title": paper["title"], "eyebrow": paper["eyebrow"], "kind": paper["kind"],
           "sub": outline.get("sub", ""), "reading_min": outline.get("reading_min", 14),
           "related": outline.get("related", []), "ref_ids": ref_ids,
           "ref_lookup": {rid: (refs_add.get(rid, {}).get("cite") or RREF.REFS.get(rid, {}).get("cite", "")) for rid in ref_ids},
           "sections": outline.get("sections", [])}
    json.dump(rec, open(os.path.join(GEN, slug + ".json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    manifest.append((slug, len(rec["sections"]), len(ref_ids)))
with open(os.path.join(HERE, "data", "refs_gen5.py"), "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n# AUTO-GENERATED Phase-5.\nREFS_ADD = {\n")
    for rid, r in refs_add.items():
        f.write('    "%s": {"cite": "%s", "url": "%s", "peer": %s},\n' % (
            rid, r["cite"].replace("\\", "\\\\").replace('"', '\\"'), r["url"].replace('"', '\\"'), r["peer"]))
    f.write("}\n")
with open(os.path.join(HERE, "data", "glossary_gen5.py"), "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n# AUTO-GENERATED Phase-5.\nGLOSSARY_ADD = [\n")
    for g in gloss_add.values():
        f.write('    {"term": "%s", "defn": "%s", "tags": ["reference"]},\n' % (
            g["term"].replace("\\", "\\\\").replace('"', '\\"'), g["defn"].replace("\\", "\\\\").replace('"', '\\"')))
    f.write("]\n")
print("phase-5 papers:", len(manifest), "| new refs:", len(refs_add), "| new terms:", len(gloss_add))
for m in manifest: print("  %-24s sections=%-2d refs=%d" % m)
