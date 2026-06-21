# -*- coding: utf-8 -*-
"""Generate all manifest images via the Higgsfield CLI, download, compress to web JPG.
Resumable: skips any img/<slug>-<n>.jpg that already exists.
Run:  python gen_images.py
"""
import os, sys, json, subprocess, urllib.request, io, time
sys.path.insert(0, os.path.dirname(__file__))
from images import IMAGES
from PIL import Image

HF = r"C:\Users\OEM\AppData\Roaming\npm\higgsfield.cmd"
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
IMGDIR = os.path.join(ROOT, "assets", "img")
os.makedirs(IMGDIR, exist_ok=True)
MAXW = 1600

def jpg_path(im): return os.path.join(IMGDIR, f"{im['slug']}-{im['n']}.jpg")
def png_path(im): return os.path.join(IMGDIR, f"{im['slug']}-{im['n']}.png")

def save_web_jpg(raw_bytes, dest):
    img = Image.open(io.BytesIO(raw_bytes)).convert("RGB")
    if img.width > MAXW:
        h = round(img.height * MAXW / img.width)
        img = img.resize((MAXW, h), Image.LANCZOS)
    img.save(dest, "JPEG", quality=82, optimize=True, progressive=True)
    return os.path.getsize(dest)

def generate(im):
    cmd = ["cmd", "/c", HF, "generate", "create", im["model"],
           "--prompt", im["prompt"], "--aspect_ratio", im["ar"],
           "--resolution", im["res"], "--wait", "--wait-timeout", "5m", "--json"]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=380)
    if r.returncode != 0:
        raise RuntimeError("CLI rc=%d: %s" % (r.returncode, (r.stderr or r.stdout)[:300]))
    out = r.stdout.strip()
    start = out.find("[")
    data = json.loads(out[start:]) if start >= 0 else json.loads(out)
    rec = data[0] if isinstance(data, list) else data
    url = rec.get("result_url") or (rec.get("results") or [{}])[0].get("url")
    if not url:
        raise RuntimeError("no result_url in: " + out[:300])
    return url

def main():
    done, fail, skip = [], [], []
    total = len(IMAGES)
    for i, im in enumerate(IMAGES, 1):
        dest = jpg_path(im)
        tag = f"{im['slug']}-{im['n']}"
        if os.path.exists(dest):
            skip.append(tag); print(f"[{i}/{total}] skip {tag} (exists)", flush=True); continue
        # convert a leftover test PNG instead of regenerating
        if os.path.exists(png_path(im)):
            try:
                kb = save_web_jpg(open(png_path(im), "rb").read(), dest) // 1024
                os.remove(png_path(im)); done.append(tag)
                print(f"[{i}/{total}] converted {tag} ({kb} KB)", flush=True); continue
            except Exception as e:
                print(f"[{i}/{total}] png-convert failed {tag}: {e}", flush=True)
        try:
            t0 = time.time()
            url = generate(im)
            raw = urllib.request.urlopen(url, timeout=120).read()
            kb = save_web_jpg(raw, dest) // 1024
            done.append(tag)
            print(f"[{i}/{total}] OK   {tag}  {im['model']}  {kb} KB  {int(time.time()-t0)}s", flush=True)
        except Exception as e:
            fail.append((tag, str(e)[:200]))
            print(f"[{i}/{total}] FAIL {tag}: {e}", flush=True)
    json.dump({"done": done, "skip": skip, "fail": fail},
              open(os.path.join(os.path.dirname(__file__), "_gen", "images_done.json"), "w"), indent=1)
    print(f"\nDONE generated={len(done)} skipped={len(skip)} failed={len(fail)}", flush=True)
    if fail:
        for t, e in fail: print("  FAIL", t, e, flush=True)

if __name__ == "__main__":
    main()
