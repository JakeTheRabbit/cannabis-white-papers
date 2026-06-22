# -*- coding: utf-8 -*-
"""Apply QA fixes: rewrite prompts for the flagged images, delete their jpgs so
gen_assets regenerates them. Then run: python gen_assets.py"""
import json, os
HERE = os.path.dirname(__file__)
ROOT = os.path.abspath(os.path.join(HERE, ".."))
MANP = os.path.join(HERE, "_gen", "assets_manifest.json")
IMGDIR = os.path.join(ROOT, "assets", "img")

STYLE = (" Photorealistic, inside a clean modern licensed medical cannabis production facility; "
         "hygienic white and stainless surfaces, bright even lighting, documentary realism, sharp "
         "focus, shallow depth of field. Any people present wear correct PPE: nitrile gloves, "
         "hairnet, clean lab coat or gown, closed shoes; no bare hands on product, no smoking, "
         "eating or naked flames. No text, words or labels in the image.")

FIX = {
 "t-ipm-sop-biological-control-biocontrol.jpg": "a paper breeder sachet of live predatory mites clipped onto a cannabis plant stem, tiny live beneficial mites visible around the sachet, a blue-gloved hand steadying it, macro detail",
 "t-pest-id-biocontrol-beneficial.jpg": "a paper breeder sachet of live predatory mites clipped onto a cannabis plant stem, tiny live beneficial mites crawling around it, macro detail",
 "s-closed-loop-trichome-ripeness-0.jpg": "extreme true macro of cannabis flower trichomes at the clear stage, glassy fully transparent ball-tipped stalks standing on a green sugar leaf, sharp focus, no melted or distorted shapes",
 "t-closed-loop-ec-vwc-dryback.jpg": "a handheld nutrient meter and a three-prong moisture probe inserted into a rockwool cube at the base of a cannabis plant, blank instrument screens, a dripper stake feeding the block",
 "t-defoliation-training-fim.jpg": "two blue nitrile-gloved hands pinching out the soft new growth tip of a young cannabis plant in veg, a clean FIM topping pinch, close detail",
 "t-mould-risk-relative-humidity-rh.jpg": "a wall-mounted digital temperature and humidity sensor probe hanging at canopy height among cannabis plants in a grow room, close product detail, no people in frame",
 "s-irrigation-manual-dryback-cycle-2.jpg": "a visibly dry pale rockwool cube on a clean propagation bench, surface matte and light tan, clearly drier and lighter than a wet block, an idle dripper stake beside it",
 "t-light-acclimation-acclimation.jpg": "a healthy deep-green cannabis fan leaf under bright LED grow lighting, turgid and glossy, adapting to strong light, no yellowing and no spots",
 "s-light-acclimation-acclimation-leaf-anatomy-0.jpg": "a single thin broad dark-green cannabis shade leaf held up to backlight so it looks thin and slightly translucent, close macro showing its thin morphology",
 "t-mould-risk-powdery-mildew-pm.jpg": "early powdery mildew on a cannabis fan leaf shown as patchy raised white fungal colonies growing out of the living green leaf surface, not an even dusting of powder, macro detail",
 "t-pest-id-frass-honeydew-stippling.jpg": "a cannabis fan leaf with clear pest damage in macro: pale stippled feeding spots, scattered dark frass specks and shiny sticky honeydew on the leaf surface",
 "s-nutrient-mixing-athena-salt-dissolve-progression-2.jpg": "a 50 litre plastic tank of clear water with white mineral nutrient salts dissolving, a paint-mixer paddle on a cordless drill creating a vortex, white salt clouds swirling in the water, clean grow-room utility area",
}

man = json.load(open(MANP, encoding="utf-8"))
by = {e["file"]: e for e in man}
done = 0
for f, subj in FIX.items():
    if f in by:
        by[f]["prompt"] = subj + STYLE
        done += 1
    p = os.path.join(IMGDIR, f)
    if os.path.exists(p):
        os.remove(p)
json.dump(man, open(MANP, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"updated {done} prompts, deleted jpgs; re-run gen_assets.py to regenerate {len(FIX)} images")
