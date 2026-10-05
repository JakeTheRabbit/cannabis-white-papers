# paper_coco_crop_steering - STE rewrite report (pilot; saved by the coordinator from the agent's reply)
Status: DONE WITH DISPUTES
Lint (units): E=1 W=2 (R6.6 on U0112; fixed since in the linter). Rendered: E=0 W=2.
Verify: FAIL at the time (3x "figure SVG changed" = rewritten diagram labels; the check now ignores label text). Section gate: OK.
Units changed: 118 of 157 (110 prose + 8 of 10 diagram labels)
TN added (7): coconut, husk, pith, porosity, bulk ec, cation exchange capacity, osmotic stress. TV added: none.
Number changes: +10 in U0045 ("single digits" -> "less than 10%"); "~16 min read" -> "Approximately 16 min to read"; ranges as words ("8 to 10", "1 to 2", "3 to 6"); "7+" -> "From week 7".
Content decisions: analogies removed, mechanism kept: sponge (U0018, U0026, U0057), battery (U0039), steering wheel (U0011), seawater (U0045), skin sweat (U0110), wind after a swim (U0112), "scalpel not hammer" (U0060), "jargon name" (U0010).
 lever/dial -> control; strain -> cultivar; flip the lights -> change the light cycle; veg -> vegetative stage; cal-mag -> calcium and magnesium; charge/pre-soak/buffer -> "soak the coco in a solution of calcium and magnesium"; "the claw" -> "leaves that bend down"; sulking -> "not in good condition".
 Approved words with a different STE meaning found only by reading entries: push (force only) -> cause / give more; tight ("not free") -> stronger; burn (heat damage) -> damaged; move (position) -> decreases / increases.
 Hedges kept. "Grain of salt" -> "Be careful with this information" (now site wide: Weak); "Borderline:" -> "Limit of the data:"; "Beginner" -> "Basic"; "Evidence-linked" -> "Data with sources".
 Paragraphs split: U0039, U0045, U0112, U0114. Troubleshooting words 100 -> 234 (terse cells became phrases, nothing dropped).
Needs human review: interpretations "later start / earlier" -> "longer / shorter time before the first shot" (U0102, U0103); "tightens generative growth" -> "becomes stronger" (U0111); "wind down cleanly" (U0127); "single digits" -> 10% (U0045); landing page read-time label length (build.py:372-375). Figure texts under 4 words stay (now captured by newer extractor).
Tool feedback: fixed afterwards by the coordinator (sentence splitter ed./al. bug, R6.6 with </p><p>, R1.7 false positives, global TN lists -> per-paper lexicon, SVG label hash, ste_lookup output).
