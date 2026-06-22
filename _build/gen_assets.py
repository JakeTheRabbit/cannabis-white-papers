# -*- coding: utf-8 -*-
"""Generate term-gallery + progression images from _gen/assets_manifest.json.
Parallel (4 workers), resumable (skips existing jpgs), compresses to web thumbnails.
Run: python gen_assets.py
"""
import os, sys, json, subprocess, urllib.request, io, time
from concurrent.futures import ThreadPoolExecutor, as_completed
sys.path.insert(0, os.path.dirname(__file__))
from PIL import Image

HF = r"C:\Users\OEM\AppData\Roaming\npm\higgsfield.cmd"
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
IMGDIR = os.path.join(ROOT, "assets", "img"); os.makedirs(IMGDIR, exist_ok=True)
GEN = os.path.join(os.path.dirname(__file__), "_gen")
MAXW = 900
MAN = json.load(open(os.path.join(GEN, "assets_manifest.json"), encoding="utf-8"))

def save_jpg(raw, dest):
    img = Image.open(io.BytesIO(raw)).convert("RGB")
    if img.width > MAXW:
        img = img.resize((MAXW, round(img.height * MAXW / img.width)), Image.LANCZOS)
    img.save(dest, "JPEG", quality=80, optimize=True, progressive=True)

def one(entry):
    dest = os.path.join(IMGDIR, entry["file"])
    if os.path.exists(dest):
        return ("skip", entry["file"])
    try:
        cmd = ["cmd", "/c", HF, "generate", "create", entry["model"], "--prompt", entry["prompt"],
               "--aspect_ratio", entry["ar"], "--resolution", entry.get("res", "1k"),
               "--wait", "--wait-timeout", "5m", "--json"]
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=380)
        if r.returncode != 0:
            return ("fail", entry["file"] + " :: " + (r.stderr or r.stdout)[:160])
        out = r.stdout.strip(); j = out.find("[")
        data = json.loads(out[j:] if j >= 0 else out)
        rec = data[0] if isinstance(data, list) else data
        url = rec.get("result_url") or ""
        if not url or rec.get("status") == "failed":
            return ("fail", entry["file"] + " :: no url / failed")
        save_jpg(urllib.request.urlopen(url, timeout=120).read(), dest)
        return ("ok", entry["file"])
    except Exception as e:
        return ("fail", entry["file"] + " :: " + str(e)[:160])

def main():
    todo = [e for e in MAN if not os.path.exists(os.path.join(IMGDIR, e["file"]))]
    print(f"manifest:{len(MAN)} todo:{len(todo)}", flush=True)
    res = {"ok": [], "skip": [], "fail": []}
    n = 0
    with ThreadPoolExecutor(max_workers=4) as ex:
        futs = {ex.submit(one, e): e for e in MAN}
        for fu in as_completed(futs):
            st, msg = fu.result(); res[st].append(msg); n += 1
            if st != "skip":
                print(f"[{n}/{len(MAN)}] {st} {msg}", flush=True)
    json.dump(res, open(os.path.join(GEN, "assets_done.json"), "w"), indent=1)
    print(f"\nDONE ok={len(res['ok'])} skip={len(res['skip'])} fail={len(res['fail'])}", flush=True)
    for m in res["fail"]:
        print("  FAIL", m, flush=True)

if __name__ == "__main__":
    main()
