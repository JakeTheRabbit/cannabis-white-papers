# -*- coding: utf-8 -*-
"""Generate the deep-water-culture photo set via 9router (gpt-image-1) and compress to JPEG.

Usage:  python _build/gen_images_dwc.py [slug ...]
With no args it generates every image that is not already on disk.
"""
import base64, io, json, os, sys, time, urllib.request, urllib.error

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "img", "deep-water-culture")
ENDPOINT = "http://127.0.0.1:20128/v1/images/generations"
KEYFILE = r"C:\tmp\9r-combos-key.txt"
MODEL = "gpt-image-1"
SIZE = "1536x1024"
MAX_W = 1400
QUALITY = 84

STYLE = ("Photorealistic documentary photograph, commercial indoor cannabis cultivation "
         "facility. Neutral colour balance, natural depth of field, no text, no watermarks, "
         "no logos, no people's faces. Clean professional horticultural documentation.")

SHOTS = [
    ("01-rdwc-room",
     "Wide shot of a commercial recirculating deep water culture room. Two neat rows of large "
     "white food-grade buckets with black lids, connected by white PVC manifolds running along "
     "the floor, feeding back to a single larger plant-free control bucket in the foreground. "
     "Healthy vigorous cannabis plants in vegetative growth in each bucket. Overhead LED bar "
     "fixtures. Clean epoxy floor."),
    ("02-bucket-open",
     "Close overhead-angle shot of a single deep water culture bucket with the lid lifted off "
     "and set aside. A black mesh net pot sits in the lid hole, filled with brown expanded clay "
     "pebbles. A dense curtain of bright white cannabis roots hangs from the net pot down into "
     "the nutrient solution below. Fine bubbles rise around the edge of the root mass. The water "
     "line sits just below the underside of the lid."),
    ("03-roots-healthy",
     "Macro photograph of a healthy cannabis root mass lifted just clear of a deep water culture "
     "bucket. Roots are brilliant white to cream, fine, densely branched and fibrous, glistening "
     "wet, with visible fine root hairs. Dark nutrient solution and rising bubbles behind them."),
    ("04-roots-rot",
     "Macro photograph of a diseased cannabis root mass in a hydroponic bucket. Roots are tan to "
     "dark brown, matted, slimy and collapsed, with the outer cortex sloughing off in places to "
     "expose thin pale inner strands. Cloudy brownish nutrient solution. Clear contrast with "
     "healthy white roots."),
    ("05-chlorosis",
     "Close macro photograph of a young cannabis leaf showing classic interveinal chlorosis on "
     "new growth: the leaf blade between the veins is pale yellow while the veins themselves "
     "remain distinctly dark green, creating a sharp green net pattern over yellow tissue. "
     "Older lower leaves behind it stay uniformly dark green."),
    ("06-airstone",
     "Underwater photograph inside a deep water culture bucket looking at the bottom. A round "
     "grey ceramic air stone about five centimetres across rests on the bucket floor, offset "
     "near the wall, releasing a fine even column of small silver bubbles that rises past a "
     "curtain of white roots without pushing through them. Clear nutrient solution."),
    ("07-control-bucket",
     "Close shot of a plant-free hydroponic control bucket with the lid open. Inside: a black "
     "submersible circulation pump, a white float valve on a small RO feed line, and three "
     "electrode probes on cables clipped into a vertical perforated plastic stilling tube that "
     "shields them from bubbles. Clean clear solution. White PVC bulkhead fittings in the "
     "bucket wall."),
    ("08-nanobubble",
     "Studio macro comparison photograph of two clear glass vessels of water side by side "
     "against a dark neutral background. The left vessel has a coarse air stone producing large "
     "visible bubbles that rise quickly in a turbulent plume. The right vessel is filled with a "
     "uniform milky-white opalescent haze of ultra-fine nanobubbles with no visible rising "
     "plume. Crisp side lighting."),
    ("09-changeout",
     "Photograph of a hydroponic system change-out in progress. A white drain manifold valve is "
     "open with dark spent nutrient solution running out into a floor drain, while a clean RO "
     "water line is already positioned to refill. Gloved hands on the valve. Buckets with "
     "flowering cannabis plants in the background, roots still submerged."),
    ("10-probe-reading",
     "Close shot of a handheld waterproof digital water-quality meter held over an open "
     "hydroponic control bucket, its stainless probe tip dipped into clear nutrient solution. "
     "The meter body is visible but the display is blank and unreadable. Calibration solution "
     "sachets and a squeeze bottle of distilled rinse water sit on the bucket rim."),
]


def key():
    with open(KEYFILE) as f:
        return f.read().strip()


def gen(prompt, tries=3):
    body = json.dumps({"model": MODEL, "prompt": prompt, "n": 1, "size": SIZE}).encode()
    req = urllib.request.Request(ENDPOINT, data=body, headers={
        "Authorization": "Bearer " + key(), "Content-Type": "application/json"})
    last = None
    for i in range(tries):
        try:
            with urllib.request.urlopen(req, timeout=300) as r:
                d = json.load(r)
            if "error" in d:
                last = d["error"]; time.sleep(6); continue
            return base64.b64decode(d["data"][0]["b64_json"])
        except Exception as e:                       # noqa: BLE001 - report and retry
            last = e
            time.sleep(6)
    raise RuntimeError("generation failed: %r" % (last,))


def save_jpeg(png_bytes, path):
    from PIL import Image
    im = Image.open(io.BytesIO(png_bytes)).convert("RGB")
    if im.width > MAX_W:
        im = im.resize((MAX_W, round(im.height * MAX_W / im.width)), Image.LANCZOS)
    im.save(path, "JPEG", quality=QUALITY, optimize=True, progressive=True)
    return os.path.getsize(path)


def main():
    os.makedirs(OUT, exist_ok=True)
    want = set(sys.argv[1:])
    for slug, prompt in SHOTS:
        if want and slug not in want:
            continue
        path = os.path.join(OUT, slug + ".jpg")
        if os.path.exists(path) and not want:
            print("skip (exists) %s" % slug); continue
        print("generating %s ..." % slug, flush=True)
        try:
            n = save_jpeg(gen(STYLE + " " + prompt), path)
            print("  wrote %s  %.0f KB" % (slug + ".jpg", n / 1024), flush=True)
        except Exception as e:                       # noqa: BLE001 - keep going
            print("  FAILED %s: %r" % (slug, e), flush=True)
    print("done")


if __name__ == "__main__":
    main()
